#!/usr/bin/env python3
"""Experiment 7: Allen-Cahn vs SCC basin depth comparison.

Compares basin depth around minimizers for:
  Config A: BD-only (pure Allen-Cahn / Ginzburg-Landau)
  Config B: Full SCC (closure + separation + boundary)

Theorem 4 predicts SCC basins are deeper due to self-referential terms.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, project_volume
from scc.diagnostics import compute_diagnostics

GRID = (15, 15)
BETA = 20.0
C = 0.3
N_PERTURBATIONS = 20  # number of random perturbation directions per delta
DELTAS = [0.01, 0.02, 0.05, 0.1, 0.2]

CONFIGS = {
    'BD-only (Allen-Cahn)': {'w_cl': 0.0, 'w_sep': 0.0, 'w_bd': 1.0},
    'Full SCC':             {'w_cl': 1.0, 'w_sep': 1.0, 'w_bd': 1.0},
}


def estimate_basin_depth(ec, u_star, E_star, m, deltas, n_pert, rng):
    """Estimate basin depth by perturbing u_star and measuring energy increase.

    For each delta, generate n_pert random perturbation directions,
    project back to Sigma_m, and compute E(u_pert) - E(u_star).
    Returns dict: delta -> (mean_dE, std_dE, max_dE).
    """
    n = len(u_star)
    results = {}
    for delta in deltas:
        dEs = []
        for _ in range(n_pert):
            noise = rng.randn(n)
            noise -= np.mean(noise)  # zero-mean to respect volume
            noise /= (np.linalg.norm(noise) + 1e-15)
            u_pert = u_star + delta * noise
            u_pert = project_volume(u_pert, m)
            E_pert, _ = ec.energy(u_pert)
            dEs.append(E_pert - E_star)
        results[delta] = (np.mean(dEs), np.std(dEs), np.max(dEs))
    return results


def estimate_hessian_min_eigenvalue(ec, u_star, m, n_power=50, h=1e-5):
    """Estimate smallest eigenvalue of projected Hessian via inverse power iteration.

    Uses finite differences of projected gradient on the constraint tangent space.
    Returns estimated smallest eigenvalue (positive = stable minimum).
    """
    n = len(u_star)
    rng = np.random.RandomState(42)

    # Power iteration for LARGEST eigenvalue first (to get spectral range)
    def hessian_vec(v):
        """Hv via finite difference of projected gradient."""
        g_plus = ec.gradient_projected(u_star + h * v)
        g_minus = ec.gradient_projected(u_star - h * v)
        Hv = (g_plus - g_minus) / (2 * h)
        Hv -= np.mean(Hv)  # project to tangent space
        return Hv

    # Largest eigenvalue via power iteration
    v = rng.randn(n)
    v -= np.mean(v)
    v /= np.linalg.norm(v)
    lam_max = 0.0
    for _ in range(n_power):
        Hv = hessian_vec(v)
        lam_max = float(v @ Hv)
        nHv = np.linalg.norm(Hv)
        if nHv < 1e-15:
            break
        v = Hv / nHv

    # Smallest eigenvalue via shifted inverse power iteration
    # Use shift = lam_max + small margin, then iterate with (H - shift*I)
    # Actually, simpler: use power iteration on (lam_max*I - H) to find largest
    # eigenvalue of that, then lam_min = lam_max - result
    v = rng.randn(n)
    v -= np.mean(v)
    v /= np.linalg.norm(v)
    lam_shifted = 0.0
    for _ in range(n_power):
        Hv = hessian_vec(v)
        shifted_v = lam_max * v - Hv
        shifted_v -= np.mean(shifted_v)
        lam_shifted = float(v @ shifted_v)
        ns = np.linalg.norm(shifted_v)
        if ns < 1e-15:
            break
        v = shifted_v / ns

    lam_min = lam_max - lam_shifted
    return lam_min, lam_max


def main():
    graph = GraphState.grid_2d(*GRID)
    n = graph.n
    m = C * n
    rng = np.random.RandomState(123)

    print("=" * 70)
    print("Experiment 7: Allen-Cahn vs SCC Basin Depth Comparison")
    print(f"Grid: {GRID[0]}x{GRID[1]} ({n} nodes), beta={BETA}, c={C}")
    print("=" * 70)

    results = {}
    t0 = time.time()

    for config_name, weights in CONFIGS.items():
        print(f"\n--- {config_name} ---")
        params = ParameterRegistry(
            beta_bd=BETA, volume_fraction=C,
            w_cl=weights['w_cl'], w_sep=weights['w_sep'], w_bd=weights['w_bd'],
            max_iter=5000, n_restarts=3,
        )

        # Find minimizer
        result = find_formation(graph, params, normalize=True, verbose=False)
        u_star = result.u
        E_star = result.energy
        diag = result.diagnostics
        print(f"  Minimizer: E={E_star:.6f}, converged={result.converged}, "
              f"iters={result.n_iter}")
        print(f"  Diagnostics: {diag}")

        # Build EnergyComputer with same normalization
        ec = EnergyComputer(graph, params)
        ec.normalize_weights()
        E_star_check, terms = ec.energy(u_star)

        # Basin depth via perturbations
        basin = estimate_basin_depth(ec, u_star, E_star_check, m, DELTAS,
                                     N_PERTURBATIONS, rng)

        # Hessian eigenvalues
        lam_min, lam_max = estimate_hessian_min_eigenvalue(ec, u_star, m)

        results[config_name] = {
            'E_star': E_star_check,
            'terms': terms,
            'diag': diag,
            'basin': basin,
            'lam_min': lam_min,
            'lam_max': lam_max,
            'converged': result.converged,
        }

        print(f"  Hessian eigenvalues: lam_min={lam_min:.4f}, lam_max={lam_max:.4f}")
        print(f"  Basin depths (mean dE for each delta):")
        for delta in DELTAS:
            mean_dE, std_dE, max_dE = basin[delta]
            print(f"    delta={delta:.3f}: mean_dE={mean_dE:.6f} "
                  f"(+/- {std_dE:.6f}), max={max_dE:.6f}")

    elapsed = time.time() - t0

    # Comparison table
    print("\n" + "=" * 70)
    print("COMPARISON TABLE")
    print("=" * 70)

    header = f"{'Metric':<25s}"
    for name in CONFIGS:
        header += f"  {name:>20s}"
    print(header)
    print("-" * len(header))

    # Energy
    row = f"{'E_total':<25s}"
    for name in CONFIGS:
        row += f"  {results[name]['E_star']:>20.6f}"
    print(row)

    # Hessian eigenvalues
    row = f"{'lam_min (Hessian)':<25s}"
    for name in CONFIGS:
        row += f"  {results[name]['lam_min']:>20.4f}"
    print(row)

    row = f"{'lam_max (Hessian)':<25s}"
    for name in CONFIGS:
        row += f"  {results[name]['lam_max']:>20.4f}"
    print(row)

    row = f"{'condition number':<25s}"
    for name in CONFIGS:
        lmin = results[name]['lam_min']
        lmax = results[name]['lam_max']
        cond = lmax / lmin if abs(lmin) > 1e-12 else float('inf')
        row += f"  {cond:>20.1f}"
    print(row)

    # Basin depths
    for delta in DELTAS:
        row = f"{'dE(delta=' + f'{delta:.2f})':<25s}"
        for name in CONFIGS:
            mean_dE = results[name]['basin'][delta][0]
            row += f"  {mean_dE:>20.6f}"
        print(row)

    # Diagnostics
    for comp in ['bind', 'sep', 'inside']:
        row = f"{'Diag: ' + comp:<25s}"
        for name in CONFIGS:
            val = getattr(results[name]['diag'], comp)
            row += f"  {val:>20.3f}"
        print(row)

    # Ratio analysis
    print("\n--- Basin Depth Ratio (SCC / Allen-Cahn) ---")
    ac_name = 'BD-only (Allen-Cahn)'
    scc_name = 'Full SCC'
    for delta in DELTAS:
        ac_dE = results[ac_name]['basin'][delta][0]
        scc_dE = results[scc_name]['basin'][delta][0]
        ratio = scc_dE / ac_dE if abs(ac_dE) > 1e-12 else float('inf')
        print(f"  delta={delta:.3f}: ratio={ratio:.3f} "
              f"(SCC dE={scc_dE:.6f}, AC dE={ac_dE:.6f})")

    lam_ratio = results[scc_name]['lam_min'] / results[ac_name]['lam_min'] \
        if abs(results[ac_name]['lam_min']) > 1e-12 else float('inf')
    print(f"\n  Hessian lam_min ratio (SCC/AC): {lam_ratio:.3f}")

    scc_deeper = all(
        results[scc_name]['basin'][d][0] >= results[ac_name]['basin'][d][0]
        for d in DELTAS
    )
    print(f"\n  Theorem 4 prediction (SCC basin >= AC basin): "
          f"{'CONFIRMED' if scc_deeper else 'NOT CONFIRMED'}")

    print(f"\nTotal runtime: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
