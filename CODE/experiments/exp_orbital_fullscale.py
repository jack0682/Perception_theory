"""exp_orbital_fullscale — Enumerate distinct orbital modes via multi-seed search.

Question: Are there ≥2 structurally distinct stable minimizers (= "modes") of SCC?

If only one minimizer type exists, "orbital theory" collapses to "ground state only."
If multiple distinct stable minimizers exist with different orbital character,
orbital framework is empirically justified as more than metaphor.

Protocol:
  1. Multi-seed sweep: N_seeds independent random IC → gradient flow.
  2. Cluster minimizers by (F_local_max, K_step, energy rounded, u-signature).
  3. For each distinct cluster, compute Hessian spectrum + orbital label.
  4. Report: number of distinct modes + their orbital types.

Usage:
    cd CODE && python3 experiments/exp_orbital_fullscale.py --grid 24 --c 0.5 --beta 30 --n-seeds 40
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from collections import defaultdict

import numpy as np
import scipy.sparse.linalg as spla

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation

# Reuse diagnostics
sys.path.insert(0, str(Path(__file__).resolve().parent))
from exp_orbital_discovery import (
    count_local_maxima_2d,
    k_step_2d,
    center_of_mass_2d,
    angular_multipole_coeffs,
    classify_orbital,
)


# ---------------------------------------------------------------------------
# Matrix-free Hessian operator for eigenvalue extraction
# ---------------------------------------------------------------------------

def make_hessian_matvec(ec: EnergyComputer, u_star: np.ndarray, h: float = 1e-5):
    """Return LinearOperator for H @ v via finite-difference on projected gradient."""
    n = len(u_star)
    g0 = ec.gradient_projected(u_star)

    def matvec(v):
        v = np.asarray(v).ravel()
        # Ensure v is tangent
        v_t = v - v.mean()
        norm = np.linalg.norm(v_t)
        if norm < 1e-15:
            return np.zeros_like(v_t)
        # Step along v_t
        step = h / norm
        u_pert = u_star + step * v_t
        u_pert -= (u_pert.sum() - u_star.sum()) / n
        g1 = ec.gradient_projected(u_pert)
        Hv = (g1 - g0) / step
        Hv -= Hv.mean()
        return Hv

    return spla.LinearOperator((n, n), matvec=matvec, dtype=np.float64)


def compute_orbital_spectrum(ec: EnergyComputer, u_star: np.ndarray,
                              n_modes: int = 10) -> tuple[np.ndarray, np.ndarray]:
    """Compute smallest n_modes eigenvalues + eigenvectors of constrained Hessian.

    Uses matrix-free LinearOperator + shift-invert Lanczos.
    """
    n = len(u_star)
    Hop = make_hessian_matvec(ec, u_star)
    # Use shift-invert with sigma near 0 to get smallest eigvals
    try:
        eigvals, eigvecs = spla.eigsh(
            Hop, k=min(n_modes, n - 2), sigma=0.0, which='LM', tol=1e-6,
        )
    except Exception:
        # Fallback: use 'SA' (smallest algebraic)
        eigvals, eigvecs = spla.eigsh(
            Hop, k=min(n_modes, n - 2), which='SA', tol=1e-6,
        )
    idx = np.argsort(eigvals)
    return eigvals[idx], eigvecs[:, idx]


# ---------------------------------------------------------------------------
# Initial condition generators
# ---------------------------------------------------------------------------

def make_ic(graph: GraphState, rows: int, cols: int, c: float, seed: int,
            mode: str = 'fiedler_random', noise_scale: float = 0.1) -> np.ndarray:
    """Generate initial condition with specified seeding strategy."""
    n = rows * cols
    rng = np.random.RandomState(seed)
    u0 = c * np.ones(n)

    if mode == 'fiedler_random':
        fiedler = graph.fiedler_vector()
        fiedler = fiedler / np.linalg.norm(fiedler)
        # Random sign and amplitude on Fiedler + uncorrelated noise
        amp = noise_scale * (0.5 + rng.rand())
        sign = 1.0 if rng.rand() > 0.5 else -1.0
        u0 = u0 + sign * amp * fiedler + 0.02 * rng.randn(n)
    elif mode == 'random':
        u0 = u0 + noise_scale * rng.randn(n)
    elif mode == 'eigmode_combo':
        # Combine several low Laplacian eigenvectors
        k_modes = 5
        try:
            eigvals, eigvecs = spla.eigsh(
                graph.L.astype(np.float64), k=k_modes + 1, which='SM',
            )
            idx = np.argsort(eigvals)[1:k_modes + 1]  # skip k=0 constant
            coeffs = rng.randn(k_modes)
            for i, ki in enumerate(idx):
                v = eigvecs[:, ki]
                u0 = u0 + noise_scale * coeffs[i] * v / np.linalg.norm(v)
        except Exception:
            u0 = u0 + noise_scale * rng.randn(n)
    else:
        raise ValueError(f"Unknown IC mode: {mode}")

    # Project to constraint + clip
    u0 = np.clip(u0, 0.0, 1.0)
    u0 = u0 + (c * n - u0.sum()) / n
    u0 = np.clip(u0, 0.0, 1.0)
    return u0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_seeds(graph: GraphState, params: ParameterRegistry, rows: int, cols: int,
              c: float, n_seeds: int, ic_modes: list[str], verbose: bool = False) -> list[dict]:
    """Run gradient flow from n_seeds * len(ic_modes) initial conditions."""
    records = []
    sid = 0
    for ic_mode in ic_modes:
        for seed in range(n_seeds):
            t0 = time.time()
            u_init = make_ic(graph, rows, cols, c, seed=seed + sid, mode=ic_mode)
            try:
                result = find_formation(graph, params, normalize=False,
                                         u_init=u_init, verbose=False)
            except Exception as e:
                if verbose:
                    print(f"  seed {seed} ({ic_mode}) failed: {e}")
                continue
            u_star = result.u
            elapsed = time.time() - t0

            rec = {
                'seed': seed,
                'ic_mode': ic_mode,
                'energy': float(result.energy),
                'converged': bool(result.converged),
                'n_iter': int(result.n_iter),
                'K_step': k_step_2d(u_star, rows, cols, tau=0.5),
                'F_local_max': count_local_maxima_2d(u_star, rows, cols),
                'center_of_mass': list(center_of_mass_2d(u_star, rows, cols)),
                'u_min': float(u_star.min()),
                'u_max': float(u_star.max()),
                'u_mean': float(u_star.mean()),
                'time_s': elapsed,
                # u_star itself too large to store; cluster via summary
                '_u_star': u_star,  # temp (removed before JSON save)
            }
            records.append(rec)
            if verbose:
                print(f"  seed {sid:3d} ({ic_mode:16s}): "
                      f"E={rec['energy']:7.3f} K_step={rec['K_step']} F={rec['F_local_max']} "
                      f"conv={rec['converged']} ({elapsed:.1f}s)")
            sid += 1
    return records


def cluster_minimizers(records: list[dict], energy_tol: float = 0.05) -> dict:
    """Cluster records by (F_local_max, K_step, energy rounded to tol).

    Returns dict cluster_id -> list of record indices.
    """
    clusters = defaultdict(list)
    for i, rec in enumerate(records):
        key = (
            rec['F_local_max'],
            rec['K_step'],
            round(rec['energy'] / energy_tol) * energy_tol,
        )
        clusters[key].append(i)
    return clusters


def representative_of_cluster(records: list[dict], indices: list[int]) -> int:
    """Pick the 'representative' record (lowest energy) from a cluster."""
    best_idx = indices[0]
    for i in indices[1:]:
        if records[i]['energy'] < records[best_idx]['energy']:
            best_idx = i
    return best_idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid', type=int, default=24)
    ap.add_argument('--c', type=float, default=0.5)
    ap.add_argument('--beta', type=float, default=30.0)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--n-seeds', type=int, default=40)
    ap.add_argument('--n-hessian-modes', type=int, default=10)
    ap.add_argument('--energy-tol', type=float, default=0.5,
                    help='cluster by energy within ±tol')
    ap.add_argument('--with-closure', action='store_true',
                    help='include closure + separation energies (default: pure bd)')
    ap.add_argument('--ic-modes', type=str, default='fiedler_random,random,eigmode_combo')
    ap.add_argument('--output', type=str,
                    default='/home/jack/Perception_theory/CODE/results/exp_orbital_fullscale.json')
    ap.add_argument('--verbose', action='store_true')
    args = ap.parse_args()

    rows = cols = args.grid
    n = rows * cols
    graph = GraphState.grid_2d(rows, cols)
    if args.with_closure:
        params = ParameterRegistry(
            volume_fraction=args.c, alpha_bd=args.alpha, beta_bd=args.beta,
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
            max_iter=50000, n_restarts=1, eps_init=0.02,
        )
    else:
        params = ParameterRegistry(
            volume_fraction=args.c, alpha_bd=args.alpha, beta_bd=args.beta,
            w_cl=0.0, w_sep=0.0, w_bd=1.0,
            max_iter=50000, n_restarts=1, eps_init=0.02,
        )

    ic_modes = args.ic_modes.split(',')
    print(f"Config: grid={rows}×{cols}={n}, c={args.c}, β={args.beta}, "
          f"closure={args.with_closure}")
    print(f"Seeds per IC mode: {args.n_seeds}, IC modes: {ic_modes}, "
          f"total runs = {args.n_seeds * len(ic_modes)}")
    print()

    # ---------- Phase 1: multi-seed search ----------
    t_phase1 = time.time()
    records = run_seeds(graph, params, rows, cols, args.c,
                         args.n_seeds, ic_modes, verbose=args.verbose)
    phase1_s = time.time() - t_phase1
    print(f"\nPhase 1 complete: {len(records)} minimizers in {phase1_s:.1f}s")

    # ---------- Phase 2: clustering ----------
    clusters = cluster_minimizers(records, energy_tol=args.energy_tol)
    print(f"\nPhase 2: {len(clusters)} distinct clusters (F, K_step, E-rounded)")
    cluster_list = sorted(clusters.items(), key=lambda kv: kv[0])
    print(f"{'ClusterID (F,K,E)':25s}  {'Count':>6s}  {'Eng range':>20s}")
    for key, indices in cluster_list:
        energies = [records[i]['energy'] for i in indices]
        print(f"  {str(key):25s}  {len(indices):>6d}  "
              f"[{min(energies):7.3f}, {max(energies):7.3f}]")

    # ---------- Phase 3: orbital signature per cluster ----------
    ec = EnergyComputer(graph, params)
    t_phase3 = time.time()
    cluster_summaries = []
    for key, indices in cluster_list:
        F, K_step, E_round = key
        rep_idx = representative_of_cluster(records, indices)
        rep = records[rep_idx]
        u_star = rep['_u_star']
        print(f"\nCluster {key}: rep seed={rep['seed']} ic={rep['ic_mode']} "
              f"E={rep['energy']:.4f}, computing Hessian spectrum...")
        t0 = time.time()
        try:
            eigvals, eigvecs = compute_orbital_spectrum(
                ec, u_star, n_modes=args.n_hessian_modes,
            )
        except Exception as e:
            print(f"  Hessian spectrum failed: {e}")
            continue
        hess_s = time.time() - t0

        center = rep['center_of_mass']
        # Angular decomposition of each mode
        mode_labels = []
        for i in range(len(eigvals)):
            mult = angular_multipole_coeffs(
                eigvecs[:, i], rows, cols, center, ell_max=6,
            )
            label = classify_orbital(mult['power'])
            mode_labels.append({
                'idx': i,
                'eigenvalue': float(eigvals[i]),
                'power': {str(k): float(v) for k, v in mult['power'].items()},
                'label': label,
            })

        morse_index = int((eigvals < -1e-6).sum())

        summary = {
            'cluster_key': list(key),
            'F_local_max': F,
            'K_step': K_step,
            'E_rounded': E_round,
            'count': len(indices),
            'rep_seed': rep['seed'],
            'rep_ic_mode': rep['ic_mode'],
            'rep_energy': rep['energy'],
            'rep_center_of_mass': center,
            'rep_u_range': [rep['u_min'], rep['u_max']],
            'morse_index': morse_index,
            'eigenvalues': [float(v) for v in eigvals],
            'mode_labels': mode_labels,
            'hessian_time_s': hess_s,
        }
        cluster_summaries.append(summary)
        print(f"  Morse={morse_index}, eigvals[:5]={[round(v,3) for v in eigvals[:5]]}")
        print(f"  mode labels: {[m['label'] for m in mode_labels[:5]]}")

    phase3_s = time.time() - t_phase3

    # ---------- Phase 4: mode-type enumeration ----------
    # A "mode type" is a cluster_key (F, K_step, E rounded) with morse_index=0
    stable_modes = [c for c in cluster_summaries if c['morse_index'] == 0]
    print(f"\nPhase 4: mode-type summary")
    print(f"  Total clusters: {len(cluster_summaries)}")
    print(f"  Stable (Morse=0): {len(stable_modes)}")

    # Categorize by (F, K_step) pair
    fk_types = defaultdict(list)
    for c in stable_modes:
        fk_types[(c['F_local_max'], c['K_step'])].append(c)

    print(f"  Distinct (F, K_step) pairs: {len(fk_types)}")
    for fk, cs in sorted(fk_types.items()):
        print(f"    (F={fk[0]}, K_step={fk[1]}): {len(cs)} cluster(s), "
              f"energies = {sorted(round(c['rep_energy'], 2) for c in cs)}")

    # Categorize by mode-1 orbital label (primary bifurcation mode)
    mode1_types = defaultdict(list)
    for c in stable_modes:
        # Mode 0 is near-zero; mode 1 is first stable nonzero
        if len(c['mode_labels']) >= 2:
            label = c['mode_labels'][1]['label']
            mode1_types[label].append(c)

    print(f"  Distinct mode-1 orbital labels: {len(mode1_types)}")
    for label, cs in mode1_types.items():
        print(f"    '{label}': {len(cs)} cluster(s)")

    # ---------- Save output ----------
    # Strip u_star from records before saving
    clean_records = []
    for r in records:
        clean = {k: v for k, v in r.items() if k != '_u_star'}
        clean_records.append(clean)

    out = {
        'config': {
            'grid': [rows, cols],
            'c': args.c, 'beta': args.beta, 'alpha': args.alpha,
            'n_seeds_per_ic_mode': args.n_seeds,
            'ic_modes': ic_modes,
            'with_closure': args.with_closure,
            'energy_tol': args.energy_tol,
            'n_hessian_modes': args.n_hessian_modes,
        },
        'timing': {
            'phase1_search_s': phase1_s,
            'phase3_hessian_s': phase3_s,
        },
        'records': clean_records,
        'cluster_summaries': cluster_summaries,
        'n_total_clusters': len(cluster_summaries),
        'n_stable_modes': len(stable_modes),
        'fk_type_counts': {
            str(fk): len(cs) for fk, cs in fk_types.items()
        },
        'mode1_label_counts': {
            label: len(cs) for label, cs in mode1_types.items()
        },
    }
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(out_path, 'w'), indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == '__main__':
    main()
