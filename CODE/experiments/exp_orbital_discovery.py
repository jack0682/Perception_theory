"""exp_orbital_discovery — Test whether orbital shape modes exist in SCC.

Theoretical context: `logs/daily/2026-04-23/07_shape_modes_orbital_hypothesis.md`
and `08_orbital_discovery_program.md`.

Question: Does the Hessian at an SCC K=1 minimizer have an angular-mode structure
analogous to atomic orbitals (1s, 2p, 2d, 3d, ...)?

Protocol:
  1. Find K=1 minimizer u* on 2D square grid at (c, β) with Fiedler-init.
  2. Build finite-difference Hessian H at u* (constrained to T(Σ_m)).
  3. Compute top-k low-lying eigenvalues + eigenvectors.
  4. For each eigenvector, compute angular multipole decomposition around u*'s center.
  5. Report (n_radial, ell) labels; check for expected 1s/2p/2d/3d hierarchy.

Supports multiple (c, β) configs to build a small discovery database.

Usage:
    cd CODE && python3 experiments/exp_orbital_discovery.py --grid 24 --c 0.5 --beta 30 --n-modes 30
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation


# ---------------------------------------------------------------------------
# Constrained finite-difference Hessian
# ---------------------------------------------------------------------------

def constrained_hessian_fd(
    ec: EnergyComputer, u_star: np.ndarray, h: float = 1e-5
) -> np.ndarray:
    """Build dense Hessian H on T(Σ_m) via finite-difference of gradient.

    For small graphs (n up to ~1000), this is fast and reliable.

    Returns n×n symmetric matrix. The constraint Σu=const is handled by
    using *projected* gradients (mean-subtracted).
    """
    n = len(u_star)
    g0 = ec.gradient_projected(u_star)
    H = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        u_perturb = u_star.copy()
        u_perturb[i] += h
        # Re-project to constraint manifold
        u_perturb -= (u_perturb.sum() - u_star.sum()) / n
        g1 = ec.gradient_projected(u_perturb)
        H[:, i] = (g1 - g0) / h
    # Symmetrize
    return 0.5 * (H + H.T)


def compute_low_spectrum(H: np.ndarray, n_modes: int = 30) -> tuple[np.ndarray, np.ndarray]:
    """Return (eigenvalues, eigenvectors) for smallest n_modes (algebraically)."""
    # Dense eigendecomposition for reliability
    eigvals, eigvecs = np.linalg.eigh(H)
    idx = np.argsort(eigvals)
    return eigvals[idx[:n_modes]], eigvecs[:, idx[:n_modes]]


# ---------------------------------------------------------------------------
# Angular multipole decomposition on 2D grid
# ---------------------------------------------------------------------------

def center_of_mass_2d(u: np.ndarray, rows: int, cols: int) -> tuple[float, float]:
    """Compute intensity-weighted center on the grid.

    Returns (row_c, col_c) in lattice units, centered in [0, rows-1] x [0, cols-1].
    """
    u2 = u.reshape(rows, cols)
    u_shift = u2 - u2.min()  # ensure non-negative weights
    total = u_shift.sum()
    if total < 1e-12:
        return (rows - 1) / 2.0, (cols - 1) / 2.0
    rr, cc = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')
    row_c = (rr * u_shift).sum() / total
    col_c = (cc * u_shift).sum() / total
    return float(row_c), float(col_c)


def angular_multipole_coeffs(
    mode: np.ndarray, rows: int, cols: int, center: tuple[float, float], ell_max: int = 6
) -> dict:
    """Decompose a mode (flat length n=rows*cols) into angular multipole components.

    Integrates mode(r, θ) * e^{iℓθ} weighted by r over the grid.

    Returns dict with keys 'c_ell[ell]' (complex coeff) and 'power_ell[ell]'.
    """
    mode2 = mode.reshape(rows, cols)
    row_c, col_c = center

    # Build radial + angular coordinates per grid point
    rr, cc = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')
    dr = rr - row_c
    dc = cc - col_c
    r = np.sqrt(dr**2 + dc**2)
    theta = np.arctan2(dc, dr)  # angle

    coeffs = {}
    powers = {}
    for ell in range(ell_max + 1):
        if ell == 0:
            # Radial integral weighted by ell=0 (just mean over angles)
            c = (mode2 * np.ones_like(theta)).sum()
        else:
            # c_ell = integral of mode(r,θ) * exp(i*ell*θ) * r dr dθ
            # On grid, weight by r (makes it a "moment")
            weight = r  # radial weighting
            c_cos = (mode2 * np.cos(ell * theta) * weight).sum()
            c_sin = (mode2 * np.sin(ell * theta) * weight).sum()
            c = complex(c_cos, c_sin)
        coeffs[ell] = c
        powers[ell] = abs(c) ** 2
    # Normalize powers so sum = 1
    tot = sum(powers.values())
    if tot > 0:
        powers = {k: v / tot for k, v in powers.items()}
    return {'coeffs': coeffs, 'power': powers}


def classify_orbital(power: dict, threshold: float = 0.3) -> str:
    """Given angular power distribution, label orbital type.

    Rules:
    - Dominant ell=0: 's' (radial)
    - Dominant ell=1: 'p' (dipole)
    - Dominant ell=2: 'd' (quadrupole)
    - Dominant ell=3: 'f' (hexapole)
    - Dominant ell=4: 'g' (octupole)
    """
    names = {0: 's', 1: 'p', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'i'}
    max_ell = max(power, key=power.get)
    max_pow = power[max_ell]
    if max_pow < threshold:
        return f"mixed(max ell={max_ell}, p={max_pow:.2f})"
    return f"{names.get(max_ell, f'ell{max_ell}')}({max_pow:.2f})"


# ---------------------------------------------------------------------------
# Count local maxima (topological F)
# ---------------------------------------------------------------------------

def count_local_maxima_2d(u: np.ndarray, rows: int, cols: int) -> int:
    """Count strict local maxima on 4-neighbor 2D grid."""
    u2 = u.reshape(rows, cols)
    count = 0
    for r in range(rows):
        for c in range(cols):
            val = u2[r, c]
            is_max = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if u2[nr, nc] >= val - 1e-10:
                        # Require strict max (tie-breaking: upper-left wins)
                        if u2[nr, nc] > val + 1e-10:
                            is_max = False
                            break
                        if (nr, nc) < (r, c):
                            is_max = False
                            break
            if is_max:
                count += 1
    return count


# ---------------------------------------------------------------------------
# K_step (connected components at threshold)
# ---------------------------------------------------------------------------

def k_step_2d(u: np.ndarray, rows: int, cols: int, tau: float = 0.5) -> int:
    """Count connected components of {u > tau} on 4-neighbor grid."""
    u2 = u.reshape(rows, cols)
    mask = u2 > tau
    visited = np.zeros_like(mask, dtype=bool)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if mask[r, c] and not visited[r, c]:
                # BFS
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    if 0 <= cr < rows and 0 <= cc < cols and mask[cr, cc] and not visited[cr, cc]:
                        visited[cr, cc] = True
                        stack.extend([(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)])
                count += 1
    return count


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_config(rows: int, cols: int, c: float, beta: float, alpha: float,
               n_modes: int, ell_max: int, seed: int = 0,
               normalize: bool = False) -> dict:
    """Single-config orbital signature extraction."""
    t0 = time.time()
    graph = GraphState.grid_2d(rows, cols)
    params = ParameterRegistry(
        volume_fraction=c,
        alpha_bd=alpha,
        beta_bd=beta,
        w_cl=0.0,   # Turn off closure for cleaner test (pure Allen-Cahn first)
        w_sep=0.0,  # Turn off separation
        w_bd=1.0,
        max_iter=30000,
        n_restarts=1,
        eps_init=0.02,
    )

    # Custom init: Fiedler mode + small uniform noise
    n = rows * cols
    fiedler = graph.fiedler_vector()
    fiedler = fiedler / np.linalg.norm(fiedler)
    rng = np.random.RandomState(seed)
    u_init = c * np.ones(n) + 0.1 * fiedler + 0.01 * rng.randn(n)
    u_init = np.clip(u_init, 0.0, 1.0)
    # Project to mass constraint
    u_init = u_init + (c * n - u_init.sum()) / n
    u_init = np.clip(u_init, 0.0, 1.0)

    result = find_formation(graph, params, normalize=normalize, u_init=u_init, verbose=False)
    u_star = result.u
    t_opt = time.time() - t0

    # Analyze minimizer
    k_step = k_step_2d(u_star, rows, cols, tau=0.5)
    f_count = count_local_maxima_2d(u_star, rows, cols)
    center = center_of_mass_2d(u_star, rows, cols)

    # Build Hessian, extract spectrum
    ec = EnergyComputer(graph, params)
    if normalize:
        ec.normalize_weights()
    t1 = time.time()
    H = constrained_hessian_fd(ec, u_star, h=1e-5)
    eigvals, eigvecs = compute_low_spectrum(H, n_modes=n_modes)
    t_hess = time.time() - t1

    # Angular decomposition per mode
    modes_info = []
    for i in range(n_modes):
        mode = eigvecs[:, i]
        mult = angular_multipole_coeffs(mode, rows, cols, center, ell_max=ell_max)
        label = classify_orbital(mult['power'])
        modes_info.append({
            'idx': i,
            'eigenvalue': float(eigvals[i]),
            'power_by_ell': {str(k): float(v) for k, v in mult['power'].items()},
            'orbital_label': label,
        })

    # Summary
    morse_index = int((eigvals < -1e-6).sum())
    near_zero = int((np.abs(eigvals) < 1e-4).sum())

    # Field values summary
    u_min = float(u_star.min())
    u_max = float(u_star.max())
    u_mean = float(u_star.mean())

    return {
        'config': {
            'grid': [rows, cols],
            'c': c,
            'beta': beta,
            'alpha': alpha,
            'seed': seed,
            'normalize': normalize,
        },
        'minimizer_summary': {
            'u_min': u_min,
            'u_max': u_max,
            'u_mean': u_mean,
            'energy': float(result.energy),
            'K_step_tau_0.5': k_step,
            'F_local_max': f_count,
            'center_of_mass': list(center),
            'converged': bool(result.converged),
            'n_iter': int(result.n_iter),
        },
        'spectrum_summary': {
            'n_modes_computed': n_modes,
            'eigenvalue_range': [float(eigvals[0]), float(eigvals[-1])],
            'morse_index': morse_index,
            'near_zero_count': near_zero,
            'first_10_eigvals': [float(v) for v in eigvals[:10]],
        },
        'modes': modes_info,
        'timing': {
            'optimize_s': t_opt,
            'hessian_s': t_hess,
        }
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid', type=int, default=16, help='grid side')
    ap.add_argument('--c', type=float, default=0.5)
    ap.add_argument('--beta', type=float, default=30.0)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--n-modes', type=int, default=30)
    ap.add_argument('--ell-max', type=int, default=6)
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--normalize', action='store_true')
    ap.add_argument('--output', type=str, default='results/exp_orbital_discovery.json')
    ap.add_argument('--multi-config', action='store_true',
                    help='Run multiple configs instead of single')
    args = ap.parse_args()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.multi_config:
        configs = [
            {'c': 0.5, 'beta': 30.0, 'alpha': 1.0},  # R18-like
            {'c': 0.3, 'beta': 30.0, 'alpha': 1.0},  # R17-like (low-c multi-mode)
            {'c': 0.5, 'beta': 10.0, 'alpha': 1.0},  # Near-critical
            {'c': 0.5, 'beta': 5.0,  'alpha': 1.0},  # Barely supercritical
        ]
        all_results = {'configs': []}
        for cfg in configs:
            print(f"\n== Config: c={cfg['c']}, beta={cfg['beta']}, alpha={cfg['alpha']} ==")
            r = run_config(
                args.grid, args.grid, cfg['c'], cfg['beta'], cfg['alpha'],
                args.n_modes, args.ell_max, seed=args.seed, normalize=args.normalize,
            )
            print(f"  K_step={r['minimizer_summary']['K_step_tau_0.5']}, "
                  f"F={r['minimizer_summary']['F_local_max']}, "
                  f"morse_ind={r['spectrum_summary']['morse_index']}, "
                  f"first_3_eigvals={r['spectrum_summary']['first_10_eigvals'][:3]}")
            print(f"  first 5 mode labels: {[m['orbital_label'] for m in r['modes'][:5]]}")
            all_results['configs'].append(r)

        with open(out_path, 'w') as f:
            json.dump(all_results, f, indent=2)
        print(f"\nSaved to {out_path}")
    else:
        r = run_config(
            args.grid, args.grid, args.c, args.beta, args.alpha,
            args.n_modes, args.ell_max, seed=args.seed, normalize=args.normalize,
        )
        with open(out_path, 'w') as f:
            json.dump(r, f, indent=2)

        # Print summary
        print("\n===== Orbital Discovery =====")
        print(f"Config: grid={args.grid}x{args.grid}, c={args.c}, beta={args.beta}")
        print(f"Minimizer: K_step={r['minimizer_summary']['K_step_tau_0.5']}, "
              f"F={r['minimizer_summary']['F_local_max']}, "
              f"converged={r['minimizer_summary']['converged']}")
        print(f"Spectrum: Morse index={r['spectrum_summary']['morse_index']}, "
              f"near-zero={r['spectrum_summary']['near_zero_count']}")
        print(f"First 10 eigenvalues: {r['spectrum_summary']['first_10_eigvals']}")
        print(f"\nLow-lying modes and angular labels:")
        for m in r['modes'][:12]:
            p = m['power_by_ell']
            top_ells = sorted(p.items(), key=lambda x: -x[1])[:3]
            top_str = ", ".join(f"l={k}:{v:.2f}" for k, v in top_ells)
            print(f"  mode {m['idx']:2d}: λ={m['eigenvalue']:+.4f}  "
                  f"label={m['orbital_label']:20s}  top: {top_str}")
        print(f"\nSaved to {out_path}")


if __name__ == '__main__':
    main()
