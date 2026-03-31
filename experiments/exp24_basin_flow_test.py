"""Experiment 24: Test actual basin of attraction via gradient flow.

The sublevel set gives a conservative lower bound. Test whether gradient flow
converges even from perturbations MUCH larger than r_soft.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.optimizer import project_volume

def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p


def gradient_flow(u0, ec, m, max_iter=5000, tol=1e-10, dt=0.01):
    """Simple projected gradient descent."""
    u = u0.copy()
    for i in range(max_iter):
        g = ec.gradient_projected(u)
        u = u - dt * g
        u = project_volume(np.clip(u, 0, 1), m)
        gn = np.linalg.norm(g)
        if gn < tol:
            return u, True, i
    return u, False, max_iter


def test_basin(n_grid, beta, n_trials=20):
    g = GraphState.grid_2d(n_grid, n_grid)
    p = make_params(beta_bd=beta)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()
    res = find_formation(g, p)
    u_star = res.u
    m = p.volume_fraction * g.n
    n = len(u_star)

    # Compute soft mode
    tol_box = 1e-6
    free_mask = (u_star > tol_box) & (u_star < 1 - tol_box)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)

    if n_f < 3:
        return None

    h = 1e-5
    g0 = ec.gradient(u_star)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u_star + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]
    H = 0.5 * (H + H.T)
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10
    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]
    mu = eigvals[0]

    soft_mode = np.zeros(n)
    soft_mode[free_idx] = eigvecs[:, 0]
    soft_mode -= np.mean(soft_mode)
    soft_mode /= np.linalg.norm(soft_mode)

    # Test convergence at increasing distances along soft mode
    results = []
    for eps in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0]:
        u0 = project_volume(np.clip(u_star + eps * soft_mode, 0, 1), m)
        actual_dist = np.linalg.norm(u0 - u_star)

        u_final, converged, n_iter = gradient_flow(u0, ec, m)
        dist_to_star = np.linalg.norm(u_final - u_star)
        returned = dist_to_star < 0.1  # converged back to same minimizer

        results.append({
            'eps': eps, 'actual_dist': actual_dist,
            'converged': converged, 'returned': returned,
            'dist_final': dist_to_star, 'n_iter': n_iter,
        })

    # Also test random directions
    rng = np.random.RandomState(42)
    random_results = []
    for eps in [0.1, 0.5, 1.0, 2.0]:
        successes = 0
        for trial in range(n_trials):
            v = rng.randn(n)
            v -= np.mean(v)
            v /= np.linalg.norm(v)
            u0 = project_volume(np.clip(u_star + eps * v, 0, 1), m)
            u_final, converged, n_iter = gradient_flow(u0, ec, m)
            dist = np.linalg.norm(u_final - u_star)
            if dist < 0.1:
                successes += 1
        random_results.append({'eps': eps, 'success_rate': successes / n_trials})

    return {
        'mu': mu, 'soft_mode_results': results,
        'random_results': random_results, 'n_grid': n_grid, 'beta': beta,
    }


def main():
    print("=" * 100)
    print("EXPERIMENT 24: Actual Basin of Attraction via Gradient Flow")
    print("=" * 100)

    # Focus on the problematic configurations
    configs = [
        (8, 50), (10, 100), (12, 150), (15, 50),  # Small r_soft
        (10, 50), (10, 30), (12, 100),  # Larger r_soft
    ]

    for n_grid, beta in configs:
        print(f"\n{'='*70}")
        print(f"Grid: {n_grid}x{n_grid}, β={beta}")
        print(f"{'='*70}")

        r = test_basin(n_grid, beta)
        if r is None:
            print("  Too few free variables")
            continue

        print(f"  μ = {r['mu']:.4f}")
        print(f"\n  Soft mode direction (escape along softest eigenvector):")
        print(f"  {'ε':<8} {'Actual dist':<14} {'Returned?':<12} {'Final dist':<12} {'Iters':<8}")
        print(f"  {'-'*54}")
        for s in r['soft_mode_results']:
            status = '✓' if s['returned'] else '✗'
            print(f"  {s['eps']:<8.2f} {s['actual_dist']:<14.4f} {status:<12} "
                  f"{s['dist_final']:<12.4f} {s['n_iter']:<8}")

        # Find basin radius (last epsilon that returns)
        last_good = 0
        for s in r['soft_mode_results']:
            if s['returned']:
                last_good = s['eps']
        print(f"\n  Empirical soft-mode basin radius: ε ≥ {last_good}")

        print(f"\n  Random directions (success rate = fraction returning to minimizer):")
        for rr in r['random_results']:
            print(f"  ε={rr['eps']:.1f}: {rr['success_rate']*100:.0f}%")


if __name__ == '__main__':
    main()
