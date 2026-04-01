#!/usr/bin/env python3
"""Experiment 31: β threshold for deep core existence (û ≥ θ at depth-2).

Scans β from 3α to 100α on grids 8×8 through 20×20, measuring the minimum
field value at depth-2 sites across multiple optimizer restarts. This
determines the empirical β_crit for Theorem 1 (Core Depth).

Key findings (summary):
- β ≥ 7α suffices on 10×10 for θ=0.9
- β ≥ 15α suffices robustly across all tested grids
- The conservative proof bound β ≥ 58α can be tightened to β ≥ 20α
- Actual cl/sep gradient corrections at depth-2 are 4-10% of worst-case Prop 3 bounds
"""
import sys, os, time
import numpy as np
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation
from scc.operators import closure, distinction


def compute_depth(graph, u, threshold=0.5):
    """Compute graph distance from each support site to the boundary of support."""
    L_dense = graph.L.toarray()
    n = graph.n
    support = set(np.where(u > threshold)[0])
    if len(support) < 4:
        return {}, support

    # BFS from non-support to compute distances
    boundary = set(range(n)) - support
    dist = {}
    queue = deque()
    for x in boundary:
        dist[x] = 0
        queue.append(x)
    while queue:
        x = queue.popleft()
        for y in range(n):
            if L_dense[x, y] < 0 and y not in dist:
                dist[y] = dist[x] + 1
                queue.append(y)

    return dist, support


def get_depth_k_stats(graph, u, k=2, threshold=0.5):
    """Get field statistics at sites with depth ≥ k from support boundary."""
    dist, support = compute_depth(graph, u, threshold)
    depth_k = [x for x in support if dist.get(x, -1) >= k]
    if not depth_k:
        return None
    vals = [u[x] for x in depth_k]
    return {
        "n_sites": len(depth_k),
        "min_u": min(vals),
        "max_u": max(vals),
        "mean_u": np.mean(vals),
        "support_size": len(support),
    }


def experiment_beta_scan():
    """Main experiment: scan β × grid size, report min û at depth-2."""
    print("=" * 72)
    print("Exp 31: β Threshold for Deep Core Existence (θ_core = 0.9)")
    print("=" * 72)

    grid_sizes = [8, 10, 12, 15, 20]
    betas = [3, 5, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100]
    n_trials = 5
    theta = 0.9

    results = {}

    print(f"\n{'β':>4s} | ", end="")
    for n in grid_sizes:
        print(f"  {n}×{n:>2d}  |", end="")
    print()
    print("-" * (8 + 10 * len(grid_sizes)))

    for beta in betas:
        row = f"{beta:4d} | "
        for n in grid_sizes:
            p = ParameterRegistry(beta_bd=float(beta))
            g = GraphState.grid_2d(n, n)

            worst_min = 1.0
            best_trial = None
            for trial in range(n_trials):
                r = find_formation(g, p)
                stats = get_depth_k_stats(g, r.u, k=2)
                if stats is not None:
                    if stats["min_u"] < worst_min:
                        worst_min = stats["min_u"]
                        best_trial = stats

            if best_trial is not None:
                marker = "+" if worst_min >= theta else "-"
                row += f" {worst_min:.4f}{marker} |"
                results[(beta, n)] = worst_min
            else:
                row += "   ---   |"
                results[(beta, n)] = None
        print(row)

    # Find threshold for each grid size
    print("\n" + "=" * 72)
    print("Empirical β_crit (smallest β where ALL trials have min_u ≥ 0.9):")
    print("=" * 72)
    for n in grid_sizes:
        threshold_beta = None
        for beta in betas:
            key = (beta, n)
            if key in results and results[key] is not None and results[key] >= theta:
                # Check all higher betas also pass
                all_pass = all(
                    results.get((b, n), 0) is not None
                    and results.get((b, n), 0) >= theta
                    for b in betas
                    if b >= beta
                )
                if all_pass:
                    threshold_beta = beta
                    break
        if threshold_beta:
            print(f"  {n}×{n}: β_crit = {threshold_beta}α")
        else:
            print(f"  {n}×{n}: β_crit > {betas[-1]}α (not found)")

    return results


def experiment_gradient_analysis():
    """Measure actual cl/sep gradient magnitudes at depth-2 vs Proposition 3 bounds."""
    print("\n" + "=" * 72)
    print("Gradient Analysis at Depth-2 Sites")
    print("=" * 72)

    for n in [10, 15, 20]:
        for beta in [10, 20, 50]:
            p = ParameterRegistry(beta_bd=float(beta))
            g = GraphState.grid_2d(n, n)
            ec = EnergyComputer(g, p)
            ec.normalize_weights()
            r = find_formation(g, p)
            u = r.u

            # Finite-difference gradients of E_cl and E_sep
            eps = 1e-6
            cl0 = closure(u, g, p)
            E_cl0 = np.sum((u - cl0) ** 2)
            d0 = distinction(u, g, p)
            E_sep0 = np.sum((u * (1 - d0)) ** 2)

            grad_cl = np.zeros_like(u)
            grad_sep = np.zeros_like(u)

            for i in range(len(u)):
                u_p = u.copy()
                u_p[i] += eps
                cl_p = closure(u_p, g, p)
                grad_cl[i] = (np.sum((u_p - cl_p) ** 2) - E_cl0) / eps
                d_p = distinction(u_p, g, p)
                grad_sep[i] = (np.sum((u_p * (1 - d_p)) ** 2) - E_sep0) / eps

            # Depth-2 stats
            dist, support = compute_depth(g, u)
            depth2 = [x for x in support if dist.get(x, -1) >= 2]

            if depth2:
                max_gcl = max(abs(grad_cl[x]) for x in depth2)
                max_gsep = max(abs(grad_sep[x]) for x in depth2)
                G_cl_prop3 = 2 * (1 + p.a_cl / 4)  # = 3.75
                G_sep_prop3 = 2.0

                C2_actual = ec.lambda_cl * max_gcl + ec.lambda_sep * max_gsep
                C2_worst = ec.lambda_cl * G_cl_prop3 + ec.lambda_sep * G_sep_prop3

                print(
                    f"  {n}×{n} β={beta:3d}: "
                    f"|∇E_cl|={max_gcl:.4f}/{G_cl_prop3:.2f} ({max_gcl / G_cl_prop3:.1%}), "
                    f"|∇E_sep|={max_gsep:.4f}/{G_sep_prop3:.2f} ({max_gsep / G_sep_prop3:.1%}), "
                    f"C₂_eff={C2_actual:.4f}/{C2_worst:.4f} ({C2_actual / C2_worst:.1%})"
                )


def experiment_screened_poisson_check():
    """Verify the screened Poisson bound v_x ≤ C₁exp(-c₀δ) + C₂/β at depth-2."""
    print("\n" + "=" * 72)
    print("Screened Poisson Bound Verification at Depth-2")
    print("=" * 72)

    n = 15
    alpha = 1.0
    d_min = 4  # 2D grid interior degree

    print(f"\n  {'β':>4s} | {'c₀':>6s} | {'exp(-2c₀)':>10s} | {'v_bound':>8s} | {'v_actual':>8s} | {'ratio':>6s}")
    print("  " + "-" * 60)

    for beta in [5, 7, 10, 15, 20, 30, 50, 100]:
        kappa2 = beta / (2 * alpha)
        c0 = np.arccosh(1 + kappa2 / d_min)
        exp_term = np.exp(-2 * c0)

        # The E_bd-only bound with boundary v ≤ 0.4:
        C1 = 0.4
        # Source term from cl/sep corrections (empirical C₂_eff ≈ 0.15)
        C2_source = 0.15  # conservative from gradient analysis
        v_bound = C1 * exp_term + C2_source / beta

        # Actual value
        p = ParameterRegistry(beta_bd=float(beta))
        g = GraphState.grid_2d(n, n)
        r = find_formation(g, p)
        stats = get_depth_k_stats(g, r.u, k=2)
        v_actual = 1 - stats["min_u"] if stats else float("nan")

        ratio = v_actual / v_bound if v_bound > 0 else float("nan")
        marker = "✓" if v_actual <= 0.1 else "✗"
        print(
            f"  {beta:4d} | {c0:6.3f} | {exp_term:10.6f} | {v_bound:8.5f} | {v_actual:8.5f} | {ratio:6.3f} {marker}"
        )


if __name__ == "__main__":
    t0 = time.time()
    experiment_beta_scan()
    experiment_gradient_analysis()
    experiment_screened_poisson_check()
    print(f"\nTotal time: {time.time() - t0:.1f}s")
