#!/usr/bin/env python3
"""Experiment 1: λ_sep/λ_bd sweep — R10 Resolution.

11 ratios × 10 seeds = 110 runs on 10×10 grid.
Tests whether separation energy provides genuine formation improvement.
"""
import sys, os, time, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, _optimize_single
from scc.energy import EnergyComputer
from scc.operators import distinction
from scc.diagnostics import compute_diagnostics

GRID = (10, 10)
BETA = 20.0
C = 0.5  # volume_fraction: half the nodes participate, maximizes phase-transition sensitivity
RATIOS = [0, 1e-4, 1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1000.0, 1e4, 1e5]
N_SEEDS = 10


def run_one(graph, ratio, seed):
    params = ParameterRegistry(
        beta_bd=BETA, volume_fraction=C,
        w_cl=1.0, w_sep=ratio, w_bd=1.0,
        max_iter=1000, n_restarts=1, dt_init=0.01,
        eps_init=0.01 + 0.005 * seed,
    )
    ec = EnergyComputer(graph, params)
    u, E, terms, _, _, conv, niter = _optimize_single(graph, params, ec, seed=0)
    d = compute_diagnostics(u, graph, params)

    # Also compute Sep_old (u-weighted)
    D_u = distinction(u, graph, params)
    m = np.sum(u)
    sep_old = float(np.sum(u * D_u) / m) if m > 1e-12 else 0.0

    return {
        'ratio': ratio, 'seed': seed,
        'energy': E, 'Bind': d.bind, 'Sep_new': d.sep, 'Sep_old': sep_old,
        'Inside': d.inside, 'u_std': float(u.std()),
        'converged': conv, 'n_iter': niter,
    }


def main():
    graph = GraphState.grid_2d(*GRID)
    print(f"λ_sep/λ_bd sweep: {len(RATIOS)} ratios × {N_SEEDS} seeds = {len(RATIOS)*N_SEEDS} runs")
    print(f"Grid: {GRID}, β={BETA}, c={C}")
    print()

    all_results = []
    t0 = time.time()

    for ratio in RATIOS:
        seed_results = []
        for seed in range(N_SEEDS):
            r = run_one(graph, ratio, seed)
            seed_results.append(r)
            all_results.append(r)

        binds = [r['Bind'] for r in seed_results]
        seps_old = [r['Sep_old'] for r in seed_results]
        seps_new = [r['Sep_new'] for r in seed_results]
        insides = [r['Inside'] for r in seed_results]

        elapsed = time.time() - t0
        print(f"λ_sep/λ_bd={ratio:>10.4g}: "
              f"Bind={np.mean(binds):.3f}±{np.std(binds):.3f}  "
              f"Sep_old={np.mean(seps_old):.3f}±{np.std(seps_old):.3f}  "
              f"Sep_new={np.mean(seps_new):.3f}±{np.std(seps_new):.3f}  "
              f"Inside={np.mean(insides):.3f}±{np.std(insides):.3f}  "
              f"[{elapsed:.1f}s]")

    total = time.time() - t0
    print(f"\nTotal: {total:.1f}s")

    # Write CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'exp1_results.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
        writer.writeheader()
        writer.writerows(all_results)
    print(f"Results saved to {csv_path}")


if __name__ == '__main__':
    main()
