#!/usr/bin/env python3
"""Experiment 2: Phase transition verification — β sweep.

Sweeps β from 0.5 to 100 on 10×10 grid, c=0.5.
Verifies T8-Core: phase transition at β_crit = 4αλ₂/|W''(c)|.
"""
import sys, os, time, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import _optimize_single
from scc.energy import EnergyComputer, double_well_second_deriv
from scc.diagnostics import compute_diagnostics

GRID = (10, 10)
C = 0.5
N_SEEDS = 5


def main():
    graph = GraphState.grid_2d(*GRID)
    lambda_2 = graph.fiedler
    W_pp = abs(double_well_second_deriv(C))
    beta_crit = 4 * 1.0 * lambda_2 / W_pp

    print(f"Phase transition verification on {GRID} grid")
    print(f"λ₂ = {lambda_2:.4f}, |W''(c)| = {W_pp:.4f}, β_crit = {beta_crit:.4f}")
    print()

    multipliers = [0.1, 0.2, 0.5, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0]
    all_results = []
    t0 = time.time()

    for mult in multipliers:
        beta = mult * beta_crit
        seed_results = []
        for seed in range(N_SEEDS):
            params = ParameterRegistry(
                beta_bd=beta, alpha_bd=1.0, volume_fraction=C,
                w_cl=1.0, w_sep=1.0, w_bd=1.0,
                max_iter=1000, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005 * seed,
            )
            ec = EnergyComputer(graph, params)
            u, E, terms, _, _, conv, niter = _optimize_single(graph, params, ec, seed=0)
            d = compute_diagnostics(u, graph, params)
            r = {
                'beta_ratio': mult, 'beta': beta, 'seed': seed,
                'energy': E, 'Bind': d.bind, 'Sep': d.sep, 'Inside': d.inside,
                'u_std': float(u.std()), 'u_min': float(u.min()), 'u_max': float(u.max()),
                'converged': conv,
            }
            seed_results.append(r)
            all_results.append(r)

        im = np.mean([r['Inside'] for r in seed_results])
        um = np.mean([r['u_std'] for r in seed_results])
        bm = np.mean([r['Bind'] for r in seed_results])

        elapsed = time.time() - t0
        marker = " <-- β_crit" if abs(mult - 1.0) < 0.01 else ""
        print(f"β/β*={mult:5.1f} (β={beta:8.3f}): Inside={im:.3f}  u_std={um:.4f}  "
              f"Bind={bm:.3f}  [{elapsed:.1f}s]{marker}")

    total = time.time() - t0
    print(f"\nTotal: {total:.1f}s")

    # Write CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'exp2_results.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
        writer.writeheader()
        writer.writerows(all_results)
    print(f"Results saved to {csv_path}")


if __name__ == '__main__':
    main()
