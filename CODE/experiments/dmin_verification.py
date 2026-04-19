#!/usr/bin/env python3
"""d_min verification: measure tail decay profiles and compare with analytical predictions.

For each grid L and beta:
1. Find single formation (K=1) at c=0.3
2. Measure u(r) tail profile vs distance from center of mass
3. Fit exponential decay u(r) ~ A*exp(-c0*r) for r > R
4. Compare c0 with theory: c0_theory = arccosh(1 + beta/(2*alpha*4)) for 2D grid
5. Compute predicted d_min = (2/c0)*ln(2A/u_sp) where u_sp = 0.2113
"""
import sys, os, json
import numpy as np
from scipy.optimize import curve_fit
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation


def measure_tail_profile(u, L):
    """Measure radial profile u(r) from center of mass on LxL grid."""
    side = L
    # Compute center of mass
    coords = np.array([(i, j) for i in range(side) for j in range(side)], dtype=float)
    total = np.sum(u) + 1e-15
    cx = np.sum(u * coords[:, 0]) / total
    cy = np.sum(u * coords[:, 1]) / total

    # Compute distance from CoM for each node
    dists = np.sqrt((coords[:, 0] - cx)**2 + (coords[:, 1] - cy)**2)

    # Bin by distance (0.5 spacing)
    max_dist = np.max(dists)
    bin_edges = np.arange(0, max_dist + 0.5, 0.5)
    r_vals = []
    u_vals = []

    for i in range(len(bin_edges) - 1):
        mask = (dists >= bin_edges[i]) & (dists < bin_edges[i+1])
        if np.sum(mask) > 0:
            r_vals.append((bin_edges[i] + bin_edges[i+1]) / 2)
            u_vals.append(np.mean(u[mask]))

    return np.array(r_vals), np.array(u_vals)


def fit_exponential_tail(r, u, r_min=2.0, u_min=0.01):
    """Fit u(r) = A*exp(-c0*r) in the tail region (r > r_min, u > u_min)."""
    mask = (r > r_min) & (u > u_min) & (u < 0.5)  # tail region only
    if np.sum(mask) < 3:
        # Relax constraints
        mask = (r > 1.0) & (u > 0.001) & (u < 0.8)
    if np.sum(mask) < 3:
        return None, None, None, None

    r_fit = r[mask]
    u_fit = u[mask]

    # Linear fit in log space: ln(u) = ln(A) - c0*r
    log_u = np.log(u_fit + 1e-15)
    try:
        coeffs = np.polyfit(r_fit, log_u, 1)
        c0_fit = -coeffs[0]
        A_fit = np.exp(coeffs[1])
        return A_fit, c0_fit, r_fit, u_fit
    except:
        return None, None, None, None


def theoretical_c0(beta, alpha, d_graph=4):
    """Theoretical decay rate for 2D grid.
    c0 = arccosh(1 + beta/(2*alpha*d)) where d=4 is degree of 2D grid.
    """
    arg = 1.0 + beta / (2.0 * alpha * d_graph)
    return np.arccosh(arg)


def run_experiment():
    grid_sizes = [10, 12, 15, 20]
    betas = [20, 30, 50]
    a_cl_values = [0.0, 3.0]  # closure OFF vs ON
    u_sp = (3 - np.sqrt(3)) / 6  # ≈ 0.2113

    results = []
    raw_profiles = {}

    for L in grid_sizes:
        for beta in betas:
            for a_cl in a_cl_values:
                label = f"L={L}, β={beta}, a_cl={a_cl}"
                print(f"\n{'='*60}")
                print(f"Running: {label}")
                print(f"{'='*60}")

                g = GraphState.grid_2d(L, L)
                p = ParameterRegistry(
                    beta_bd=float(beta),
                    alpha_bd=1.0,
                    a_cl=float(a_cl),
                    volume_fraction=0.3,
                    max_iter=8000,
                    n_restarts=3,
                )

                res = find_formation(g, p)
                u = res.u

                print(f"  Energy: {res.energy:.6f}, converged: {res.converged}, iter: {res.n_iter}")
                print(f"  Peak u: {np.max(u):.4f}, Core(>0.5): {np.sum(u > 0.5)}")

                # Measure profile
                r, u_profile = measure_tail_profile(u, L)

                # Fit exponential
                A_fit, c0_fit, r_fit, u_fit = fit_exponential_tail(r, u_profile)

                # Theoretical prediction
                c0_theory = theoretical_c0(beta, 1.0, d_graph=4)

                # Predicted d_min
                if A_fit is not None and c0_fit > 0:
                    d_min_pred = (2.0 / c0_fit) * np.log(2.0 * A_fit / u_sp)
                    d_min_theory = (2.0 / c0_theory) * np.log(2.0 * A_fit / u_sp)
                else:
                    d_min_pred = None
                    d_min_theory = None

                row = {
                    'L': L, 'beta': beta, 'a_cl': a_cl,
                    'energy': float(res.energy),
                    'converged': res.converged,
                    'peak_u': float(np.max(u)),
                    'core_size': int(np.sum(u > 0.5)),
                    'A_fit': float(A_fit) if A_fit is not None else None,
                    'c0_fit': float(c0_fit) if c0_fit is not None else None,
                    'c0_theory': float(c0_theory),
                    'd_min_pred': float(d_min_pred) if d_min_pred is not None else None,
                    'd_min_theory': float(d_min_theory) if d_min_theory is not None else None,
                    'c0_ratio': float(c0_fit / c0_theory) if c0_fit is not None else None,
                }
                results.append(row)

                # Save raw profile
                key = f"L{L}_b{beta}_acl{a_cl}"
                raw_profiles[key] = {
                    'r': r.tolist(),
                    'u': u_profile.tolist(),
                    'u_field': u.tolist(),
                }

                if A_fit is not None:
                    print(f"  A_fit={A_fit:.4f}, c0_fit={c0_fit:.4f}")
                    print(f"  c0_theory={c0_theory:.4f}, ratio={c0_fit/c0_theory:.3f}")
                    if d_min_pred is not None:
                        print(f"  d_min(measured)={d_min_pred:.2f}, d_min(theory)={d_min_theory:.2f}")
                else:
                    print(f"  Fit failed (not enough tail data)")
                    print(f"  c0_theory={c0_theory:.4f}")

    # Save raw data
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'docs', '04-08', 'experiment')
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, 'dmin_raw_data.json'), 'w') as f:
        json.dump({'results': results, 'profiles': raw_profiles}, f, indent=2)

    # Print summary table
    print("\n\n" + "="*100)
    print("SUMMARY TABLE")
    print("="*100)
    print(f"{'L':>3} {'β':>4} {'a_cl':>5} {'peak':>6} {'core':>5} {'A':>8} {'c0_fit':>8} {'c0_thy':>8} {'ratio':>7} {'d_min_f':>8} {'d_min_t':>8}")
    print("-"*100)
    for row in results:
        A_str = f"{row['A_fit']:.4f}" if row['A_fit'] is not None else "N/A"
        c0f_str = f"{row['c0_fit']:.4f}" if row['c0_fit'] is not None else "N/A"
        ratio_str = f"{row['c0_ratio']:.3f}" if row['c0_ratio'] is not None else "N/A"
        dmin_f = f"{row['d_min_pred']:.2f}" if row['d_min_pred'] is not None else "N/A"
        dmin_t = f"{row['d_min_theory']:.2f}" if row['d_min_theory'] is not None else "N/A"
        print(f"{row['L']:>3} {row['beta']:>4} {row['a_cl']:>5.1f} {row['peak_u']:>6.3f} {row['core_size']:>5} {A_str:>8} {c0f_str:>8} {row['c0_theory']:>8.4f} {ratio_str:>7} {dmin_f:>8} {dmin_t:>8}")

    print(f"\nu_sp = {u_sp:.4f}")
    print(f"\nResults saved to {out_dir}/dmin_raw_data.json")

    return results, raw_profiles


if __name__ == '__main__':
    results, profiles = run_experiment()
