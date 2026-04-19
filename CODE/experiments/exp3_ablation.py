#!/usr/bin/env python3
"""Experiment 3: Energy ablation study — 6 configurations.

Tests each energy term's contribution by enabling/disabling them.
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
C = 0.5
N_SEEDS = 10

CONFIGS = {
    'BD-only':      {'w_cl': 0, 'w_sep': 0,  'w_bd': 1},
    'BD+CL':        {'w_cl': 1, 'w_sep': 0,  'w_bd': 1},
    'BD+SEP':       {'w_cl': 0, 'w_sep': 1,  'w_bd': 1},
    'Full-SCC':     {'w_cl': 1, 'w_sep': 1,  'w_bd': 1},
    'SEP-dominant': {'w_cl': 0, 'w_sep': 10, 'w_bd': 1},
    'SEP-only':     {'w_cl': 0, 'w_sep': 1,  'w_bd': 0},
}


def main():
    graph = GraphState.grid_2d(*GRID)
    print(f"Energy ablation: {len(CONFIGS)} configs × {N_SEEDS} seeds")
    print(f"Grid: {GRID}, β={BETA}, c={C}")
    print()

    all_results = []
    t0 = time.time()

    for name, weights in CONFIGS.items():
        seed_results = []
        for seed in range(N_SEEDS):
            params = ParameterRegistry(
                beta_bd=BETA, volume_fraction=C,
                w_cl=weights['w_cl'], w_sep=weights['w_sep'], w_bd=weights['w_bd'],
                max_iter=1000, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005 * seed,
            )
            ec = EnergyComputer(graph, params)
            u, E, terms, _, _, conv, niter = _optimize_single(graph, params, ec, seed=0)
            d = compute_diagnostics(u, graph, params)

            # Sep_old for comparison
            D_u = distinction(u, graph, params)
            m = np.sum(u)
            sep_old = float(np.sum(u * D_u) / m) if m > 1e-12 else 0.0

            r = {
                'config': name, 'seed': seed,
                'energy': E,
                'E_bd': terms.get('E_bd', 0), 'E_cl': terms.get('E_cl', 0),
                'E_sep': terms.get('E_sep', 0),
                'Bind': d.bind, 'Sep_new': d.sep, 'Sep_old': sep_old,
                'Inside': d.inside, 'u_std': float(u.std()),
                'converged': conv,
            }
            seed_results.append(r)
            all_results.append(r)

        bm = np.mean([r['Bind'] for r in seed_results])
        so = np.mean([r['Sep_old'] for r in seed_results])
        sn = np.mean([r['Sep_new'] for r in seed_results])
        im = np.mean([r['Inside'] for r in seed_results])

        elapsed = time.time() - t0
        print(f"{name:>15s}: Bind={bm:.3f}  Sep_old={so:.3f}  Sep_new={sn:.3f}  "
              f"Inside={im:.3f}  [{elapsed:.1f}s]")

    total = time.time() - t0
    print(f"\nTotal: {total:.1f}s")

    # Write CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'exp3_results.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
        writer.writeheader()
        writer.writerows(all_results)
    print(f"Results saved to {csv_path}")


if __name__ == '__main__':
    main()
