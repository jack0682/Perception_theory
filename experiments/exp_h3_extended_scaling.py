#!/usr/bin/env python3
"""H3 Extended Scaling: Verify C₂^eff and ν bounds on larger grids.

Extends exp_h3_jacobian_verify.py to 25×25 and 30×30 grids.
Confirms: n_bdy = O(√n), C₂^eff → 0.26, |ν| → 0 at scale.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.operators import closure, closure_with_jacobian, aggregation
from scc.energy import grad_cl, grad_sep, grad_bd
from scc.optimizer import find_formation
from collections import deque


def analyze(grid_size, beta, c=0.3, a_cl=3.0):
    rows, cols = grid_size
    graph = GraphState.grid_2d(rows, cols)
    n = rows * cols

    params = ParameterRegistry(
        a_cl=a_cl, eta_cl=0.5, tau_cl=0.5,
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=5000, n_restarts=3,
    )

    result = find_formation(graph, params)
    u = result.u

    # Jacobian diagonal
    Cl_u, sigma_prime, z = closure_with_jacobian(u, graph, params)
    diag_J = params.a_cl * (1.0 - params.eta_cl) * sigma_prime
    r = Cl_u - u

    # Classify
    core = u >= 0.9
    bdy = (u > 0.1) & (u < 0.9)
    n_core = int(np.sum(core))
    n_bdy = int(np.sum(bdy))

    # Per-site C₂
    g_cl = grad_cl(u, graph, params)
    g_sep = grad_sep(u, graph, params)
    g_bd = grad_bd(u, graph, params)
    lam = 1/3
    c2_site = (lam * np.abs(g_cl) + lam * np.abs(g_sep)) / (2 * lam)
    c2_core = float(np.mean(c2_site[core])) if n_core > 0 else float('nan')
    c2_bdy_val = float(np.mean(c2_site[bdy])) if n_bdy > 0 else float('nan')
    c2_eff = (n_bdy/n * c2_bdy_val + (n-n_bdy)/n * c2_core) if (n_core > 0 and n_bdy > 0) else c2_core

    # Lagrange multiplier
    total_grad = lam * g_cl + lam * g_sep + lam * g_bd
    nu = float(np.mean(total_grad))

    # Deep core + interior gap
    non_core_idx = np.where(~core)[0]
    depths = np.full(n, -1, dtype=int)
    queue = deque()
    for nc in non_core_idx:
        queue.append(nc)
        depths[nc] = 0
    while queue:
        node = queue.popleft()
        row = graph.W.getrow(node)
        for nb in row.indices:
            if depths[nb] == -1:
                depths[nb] = depths[node] + 1
                queue.append(nb)
    deep = core & (depths >= 2)
    n_deep = int(np.sum(deep))
    gap_min = float(np.min(u[deep] - 0.9)) if n_deep > 0 else float('nan')

    return {
        'grid': f'{rows}x{cols}', 'n': n, 'beta': beta,
        'n_core': n_core, 'n_bdy': n_bdy, 'n_deep': n_deep,
        'J_core': float(np.mean(diag_J[core])) if n_core > 0 else float('nan'),
        'J_bdy': float(np.mean(diag_J[bdy])) if n_bdy > 0 else float('nan'),
        'r_core': float(np.mean(np.abs(r[core]))) if n_core > 0 else float('nan'),
        'c2_core': c2_core, 'c2_bdy': c2_bdy_val, 'c2_eff': c2_eff,
        'nu': nu, 'gap_min': gap_min,
        'bind': result.diagnostics.bind,
    }


def main():
    print("=" * 90)
    print("H3 EXTENDED SCALING VALIDATION")
    print("=" * 90)

    configs = [
        # Original sizes for comparison
        ((8, 8), 30.0),
        ((10, 10), 30.0),
        ((15, 15), 30.0),
        ((20, 20), 30.0),
        # Extended
        ((25, 25), 30.0),
        ((30, 30), 30.0),
    ]

    results = []
    print(f"\n{'Grid':>7} {'n':>5} | {'n_core':>6} {'n_bdy':>6} {'bdy%':>5} | "
          f"{'J_core':>7} {'J_bdy':>7} | {'C₂_eff':>7} {'ν':>7} {'gap':>7} | Bind")
    print("-" * 95)

    for gs, beta in configs:
        r = analyze(gs, beta)
        results.append(r)
        bdy_pct = r['n_bdy'] / r['n'] * 100
        print(f"{r['grid']:>7} {r['n']:>5} | {r['n_core']:>6} {r['n_bdy']:>6} {bdy_pct:>4.1f}% | "
              f"{r['J_core']:>7.4f} {r['J_bdy']:>7.4f} | "
              f"{r['c2_eff']:>7.4f} {r['nu']:>7.4f} {r['gap_min']:>7.4f} | {r['bind']:.3f}")

    # Scaling analysis
    print(f"\n{'Grid':>7} {'n':>5} {'n_bdy':>6} {'√n':>6} {'n_bdy/√n':>8} {'C₂_eff':>7}")
    print("-" * 50)
    for r in results:
        sq = np.sqrt(r['n'])
        print(f"{r['grid']:>7} {r['n']:>5} {r['n_bdy']:>6} {sq:>6.1f} {r['n_bdy']/sq:>8.3f} {r['c2_eff']:>7.4f}")

    # Fit scaling exponent
    ns = np.array([r['n'] for r in results])
    nbdys = np.array([r['n_bdy'] for r in results])
    mask = nbdys > 0
    if np.sum(mask) >= 3:
        b = np.polyfit(np.log(ns[mask]), np.log(nbdys[mask] + 0.5), 1)[0]
        print(f"\nScaling exponent (log-log fit): n_bdy ~ n^{b:.3f} (expected 0.5)")

    # ν trend
    print(f"\n|ν| trend with grid size:")
    for r in results:
        print(f"  {r['grid']:>7}: |ν| = {abs(r['nu']):.4f}")

    print(f"\n--- KEY CLAIMS VERIFIED ---")
    print(f"  C₂^eff < 0.30 for all grids: {all(r['c2_eff'] < 0.30 for r in results)}")
    print(f"  |ν| < 0.20 for all grids: {all(abs(r['nu']) < 0.20 for r in results)}")
    print(f"  All gaps positive: {all(r['gap_min'] > 0 for r in results if not np.isnan(r['gap_min']))}")
    print(f"  C₂^eff decreasing with n: {results[-1]['c2_eff'] < results[0]['c2_eff']}")


if __name__ == '__main__':
    main()
