#!/usr/bin/env python3
"""Experiment 17: Energy barrier measurement.

For grids 8x8, 10x10, 15x15 and beta in {20, 50, 100, 200}:
- Find formation, compute E* and E_uniform
- Measure energy along linear interpolation path (barrier)
- Compute numerical Hessian projected onto Sigma_m tangent space
- Get lambda_max, compute r_basin = sqrt(2 * Delta / lambda_max)
- Verify r_basin >= 0.210
"""
import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer


def numerical_hessian_projected(ec, u, h=1e-5):
    """Compute numerical Hessian projected onto Sigma_m tangent space.

    H[i,j] = (grad(u + h*e_j) - grad(u - h*e_j)) / (2h)
    Then project each column: subtract mean from each column.
    """
    n = len(u)
    H = np.zeros((n, n))
    for j in range(n):
        e_j = np.zeros(n)
        e_j[j] = 1.0
        g_plus = ec.gradient(u + h * e_j)
        g_minus = ec.gradient(u - h * e_j)
        col = (g_plus - g_minus) / (2 * h)
        # Project onto tangent space of Sigma_m: subtract mean
        col -= np.mean(col)
        H[:, j] = col
    # Symmetrize
    H = 0.5 * (H + H.T)
    return H


def run_single(N, beta_val):
    """Run experiment for one grid size and beta value."""
    n = N * N
    g = GraphState.grid_2d(N, N)
    p = ParameterRegistry(beta_bd=beta_val, volume_fraction=0.3)
    r = find_formation(g, p)
    u = r.u

    ec = EnergyComputer(g, p)
    E_star, _ = ec.energy(u)

    # Uniform field with same total mass
    m = float(np.sum(u))
    u_unif = np.full(n, m / n)
    E_uniform, _ = ec.energy(u_unif)

    # Upper bound on barrier
    Delta_upper = E_uniform - E_star

    # Energy along linear path: u_hat + t * (u_unif - u_hat)
    ts = np.linspace(0, 1, 21)
    path_energies = []
    direction = u_unif - u
    for t in ts:
        u_t = u + t * direction
        E_t, _ = ec.energy(u_t)
        path_energies.append(E_t)

    path_barrier = max(path_energies) - E_star
    path_max_t = ts[np.argmax(path_energies)]

    # Numerical Hessian
    H = numerical_hessian_projected(ec, u, h=1e-5)
    eigvals = np.linalg.eigvalsh(H)
    lambda_max = float(eigvals[-1])

    # Basin radius
    if lambda_max > 0 and Delta_upper > 0:
        r_basin = float(np.sqrt(2.0 * Delta_upper / lambda_max))
    else:
        r_basin = float('inf')

    return {
        'N': N, 'beta': beta_val, 'n': n,
        'E_star': E_star, 'E_uniform': E_uniform,
        'Delta_upper': Delta_upper,
        'path_barrier': path_barrier,
        'path_max_t': path_max_t,
        'lambda_max': lambda_max,
        'lambda_min_nonzero': float(eigvals[1]) if n > 1 else 0.0,  # skip zero mode
        'r_basin': r_basin,
        'converged': r.converged,
    }


def main():
    grids = [8, 10, 15]
    betas = [20, 50, 100, 200]

    print("=" * 72)
    print("  Exp17: Energy Barrier Measurement")
    print("=" * 72)

    all_results = []
    t0 = time.time()

    for N in grids:
        for beta_val in betas:
            print(f"\n--- Grid {N}x{N}, beta={beta_val} ---")
            t1 = time.time()
            res = run_single(N, beta_val)
            dt = time.time() - t1
            all_results.append(res)

            print(f"  Converged: {res['converged']}")
            print(f"  E* = {res['E_star']:.4f}")
            print(f"  E_uniform = {res['E_uniform']:.4f}")
            print(f"  Δ_upper = E_unif - E* = {res['Delta_upper']:.4f}")
            print(f"  Path barrier = {res['path_barrier']:.4f} (max at t={res['path_max_t']:.2f})")
            print(f"  λ_max(H) = {res['lambda_max']:.4f}")
            print(f"  λ_min_nonzero = {res['lambda_min_nonzero']:.4f}")
            print(f"  r_basin = sqrt(2Δ/λ_max) = {res['r_basin']:.4f}")
            print(f"  r_basin ≥ 0.210: {'PASS' if res['r_basin'] >= 0.210 else 'FAIL'}")
            print(f"  Time: {dt:.1f}s")

    total_time = time.time() - t0

    # Summary table
    print("\n" + "=" * 72)
    print("  SUMMARY TABLE")
    print("=" * 72)
    print(f"{'Grid':>6} {'β':>5} {'E*':>10} {'E_unif':>10} {'Δ_upper':>10} "
          f"{'PathΔ':>10} {'λ_max':>10} {'r_basin':>8} {'Pass':>5}")
    print("-" * 78)
    for res in all_results:
        passed = 'PASS' if res['r_basin'] >= 0.210 else 'FAIL'
        print(f"{res['N']:>3}x{res['N']:<3} {res['beta']:>5} {res['E_star']:>10.4f} "
              f"{res['E_uniform']:>10.4f} {res['Delta_upper']:>10.4f} "
              f"{res['path_barrier']:>10.4f} {res['lambda_max']:>10.4f} "
              f"{res['r_basin']:>8.4f} {passed:>5}")

    # Verification
    print("\n" + "=" * 72)
    print("  VERIFICATION")
    print("=" * 72)
    all_pass = all(r['r_basin'] >= 0.210 for r in all_results)
    r_basin_vals = [r['r_basin'] for r in all_results]
    print(f"  r_basin ≥ 0.210 (all configs): {'PASS' if all_pass else 'FAIL'}")
    print(f"  r_basin range: [{min(r_basin_vals):.4f}, {max(r_basin_vals):.4f}]")
    print(f"  r_basin mean: {np.mean(r_basin_vals):.4f}")

    # Delta positivity
    all_delta_pos = all(r['Delta_upper'] > 0 for r in all_results)
    print(f"  Δ_upper > 0 (all configs): {'PASS' if all_delta_pos else 'FAIL'}")

    print(f"\n  Total time: {total_time:.1f}s")


if __name__ == '__main__':
    main()
