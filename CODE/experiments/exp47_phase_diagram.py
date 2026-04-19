#!/usr/bin/env python3
"""Experiment 47: Full Phase Diagram Sweep.

Sweeps beta_bd x lambda_rep to map the (beta, lambda_rep) -> regime phase diagram.
Compares geometric classification with Lambda-based prediction from coupling_strength().

Tests P-Unified-1: Persist degrades continuously with Lambda.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import (find_k_formations, inter_formation_distances,
                        classify_regime, formation_overlap, coupling_strength)


def main():
    print("Experiment 47: Full Phase Diagram (beta x lambda_rep)")
    print("=" * 70)
    t0 = time.time()

    grid_configs = [
        ('8x8', GraphState.grid_2d(8, 8)),
        ('10x10', GraphState.grid_2d(10, 10)),
    ]
    beta_values = [5, 10, 20, 40]
    lambda_rep_values = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
    vf = 0.45  # high vf to force interaction

    all_results = []
    total_configs = len(grid_configs) * len(beta_values) * len(lambda_rep_values)
    config_idx = 0

    for grid_name, grid in grid_configs:
        n = grid.n

        for beta in beta_values:
            for lam_rep in lambda_rep_values:
                config_idx += 1
                print(f"  [{config_idx}/{total_configs}] grid={grid_name}, "
                      f"beta={beta}, lam_rep={lam_rep}...", end='', flush=True)

                params = ParameterRegistry(
                    a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
                    a_D=5.0, lambda_D=1.0, tau_D=0.0,
                    alpha_bd=1.0, beta_bd=float(beta),
                    w_cl=1.0, w_sep=1.0, w_bd=1.0,
                    volume_fraction=vf,
                )

                try:
                    sources = find_k_formations(
                        grid, params, K=2,
                        lambda_rep=lam_rep,
                        max_iter=800, n_restarts=2,
                    )

                    fields = [s.u for s in sources]
                    cs = coupling_strength(fields, grid, params, lam_rep)

                    Lambda = cs['Lambda']
                    omega_max = float(np.max(cs['omega_matrix'] - np.eye(2)))
                    mu_min = min(cs['mu_per_formation'])

                    d_min_mat = inter_formation_distances(fields, grid)
                    d_min = d_min_mat[0, 1]
                    overlap_mat = formation_overlap(fields)
                    overlap = overlap_mat[0, 1]

                    geom = classify_regime(fields, grid, method='geometric')
                    pred = cs['predicted_regime']
                    agrees = (geom == pred)

                    agree_str = "OK" if agrees else "MISMATCH"
                    print(f" Lambda={Lambda:.5f}, geom={geom}, pred={pred} [{agree_str}]")

                    all_results.append({
                        'grid': grid_name,
                        'n': n,
                        'beta': beta,
                        'lambda_rep': lam_rep,
                        'd_min': float(d_min),
                        'overlap': float(overlap),
                        'omega_max': omega_max,
                        'mu_per_formation': cs['mu_per_formation'],
                        'mu_min': mu_min,
                        'mu_floor': cs['mu_floor'],
                        'Lambda_coupling': Lambda,
                        'regime_geometric': geom,
                        'regime_lambda': pred,
                        'agrees': agrees,
                        'diagnostics': [
                            {'bind': float(s.diagnostics.bind),
                             'sep': float(s.diagnostics.sep),
                             'inside': float(s.diagnostics.inside)}
                            for s in sources
                        ],
                    })

                except Exception as e:
                    print(f" FAILED: {e}")
                    all_results.append({
                        'grid': grid_name, 'n': n, 'beta': beta,
                        'lambda_rep': lam_rep, 'error': str(e),
                    })

    # Summary
    valid = [r for r in all_results if 'agrees' in r]
    n_agree = sum(1 for r in valid if r['agrees'])
    n_total = len(valid)
    n_failed = len(all_results) - n_total

    print(f"\n  {'=' * 50}")
    print(f"  Phase Diagram Summary")
    print(f"  {'=' * 50}")
    print(f"  Total configs: {len(all_results)}")
    print(f"  Successful: {n_total}")
    print(f"  Failed: {n_failed}")
    print(f"  Geometric-Lambda agreement: {n_agree}/{n_total} ({100*n_agree/max(n_total,1):.1f}%)")

    for regime in ['well-separated', 'weakly-interacting', 'strongly-interacting']:
        subset_g = [r for r in valid if r['regime_geometric'] == regime]
        subset_l = [r for r in valid if r['regime_lambda'] == regime]
        print(f"    {regime}: geometric={len(subset_g)}, lambda={len(subset_l)}")

    # Lambda distribution by geometric regime
    print(f"\n  Lambda by geometric regime:")
    for regime in ['well-separated', 'weakly-interacting', 'strongly-interacting']:
        lambdas = [r['Lambda_coupling'] for r in valid if r['regime_geometric'] == regime]
        if lambdas:
            print(f"    {regime}: Λ in [{min(lambdas):.5f}, {max(lambdas):.5f}], "
                  f"mean={np.mean(lambdas):.5f}")

    # Mismatches
    mismatches = [r for r in valid if not r['agrees']]
    if mismatches:
        print(f"\n  Mismatches ({len(mismatches)}):")
        for r in mismatches[:10]:
            print(f"    grid={r['grid']}, beta={r['beta']}, lam_rep={r['lambda_rep']}: "
                  f"geom={r['regime_geometric']}, pred={r['regime_lambda']}, "
                  f"Λ={r['Lambda_coupling']:.5f}")

    # Save
    output = {
        'experiment': 'exp47_phase_diagram',
        'description': 'Full phase diagram with coupling_strength Lambda',
        'grid_configs': ['8x8', '10x10'],
        'beta_values': beta_values,
        'lambda_rep_values': lambda_rep_values,
        'vf': vf,
        'results': all_results,
        'summary': {
            'total': len(all_results),
            'successful': n_total,
            'failed': n_failed,
            'agreement_rate': n_agree / max(n_total, 1),
        },
        'elapsed_seconds': time.time() - t0,
    }

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp47_phase_diagram.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to {outpath}")
    print(f"  Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
