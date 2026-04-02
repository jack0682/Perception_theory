#!/usr/bin/env python3
"""Experiment 46: Weak-Strong Regime Transition Validation.

Sweeps lambda_rep from very low (formations merge) to high (well-separated).
Uses coupling_strength() with mu_floor regularization.

Key prediction: as lambda_rep decreases, Lambda_coupling increases
toward the merge bifurcation at Lambda = 1/(K-1).
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import (find_k_formations, inter_formation_distances,
                        classify_regime, formation_overlap, coupling_strength)


def main():
    print("Experiment 46: Weak-Strong Regime Transition (lambda_rep sweep)")
    print("=" * 70)
    t0 = time.time()

    grid = GraphState.grid_2d(10, 10)
    n = grid.n
    vf = 0.45  # high volume fraction forces interaction
    m_each = vf * n

    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,  # low beta for diffuse tails
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=vf,
    )

    results = []
    # Wide range: very low (overlap forced) to high (full separation)
    lambda_rep_values = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2,
                         0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    print(f"\n  {'lam_rep':>8s}  {'d_min':>5s}  {'ovlp':>5s}  {'omega':>8s}  "
          f"{'mu_min':>7s}  {'mu_flr':>6s}  {'Lambda':>10s}  "
          f"{'geom':>20s}  {'lambda':>20s}")
    print(f"  {'-' * 105}")

    for lam_rep in lambda_rep_values:
        try:
            sources = find_k_formations(
                grid, params, K=2,
                lambda_rep=lam_rep,
                max_iter=1000, n_restarts=3,
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

            geom_regime = classify_regime(fields, grid, method='geometric')
            lambda_regime = cs['predicted_regime']

            print(f"  {lam_rep:8.3f}  {d_min:5.0f}  {overlap:5.0f}  {omega_max:8.5f}  "
                  f"{mu_min:7.3f}  {cs['mu_floor']:6.3f}  {Lambda:10.5f}  "
                  f"{geom_regime:>20s}  {lambda_regime:>20s}")

            results.append({
                'lambda_rep': lam_rep,
                'd_min': float(d_min),
                'overlap': float(overlap),
                'omega_max': omega_max,
                'mu_per_formation': cs['mu_per_formation'],
                'mu_min': mu_min,
                'mu_floor': cs['mu_floor'],
                'Lambda_coupling': Lambda,
                'regime_geometric': geom_regime,
                'regime_lambda': lambda_regime,
                'diagnostics': [
                    {'bind': float(s.diagnostics.bind),
                     'sep': float(s.diagnostics.sep),
                     'inside': float(s.diagnostics.inside)}
                    for s in sources
                ],
            })

        except Exception as e:
            print(f"  {lam_rep:8.3f}  FAILED: {e}")
            results.append({'lambda_rep': lam_rep, 'error': str(e)})

    # Summary
    print(f"\n  --- Summary ---")
    valid = [r for r in results if 'Lambda_coupling' in r]
    for method in ['regime_geometric', 'regime_lambda']:
        for regime in ['well-separated', 'weakly-interacting', 'strongly-interacting']:
            count = sum(1 for r in valid if r.get(method) == regime)
            if count:
                lam_vals = [r['lambda_rep'] for r in valid if r.get(method) == regime]
                print(f"  {method}: {regime} ({count}) at lam_rep={lam_vals}")

    # Monotonicity check: Lambda should decrease with lambda_rep
    lambdas = [(r['lambda_rep'], r['Lambda_coupling']) for r in valid]
    monotone_violations = 0
    for i in range(1, len(lambdas)):
        if lambdas[i][0] > lambdas[i-1][0] and lambdas[i][1] > lambdas[i-1][1]:
            monotone_violations += 1
    print(f"  Lambda monotonicity violations (should decrease with lam_rep): {monotone_violations}/{len(lambdas)-1}")

    # Save
    output = {
        'experiment': 'exp46_weak_strong',
        'description': 'Weak-Strong regime transition via lambda_rep sweep with coupling_strength',
        'grid': '10x10',
        'K': 2,
        'vf': vf,
        'beta': 10.0,
        'lambda_rep_values': lambda_rep_values,
        'results': results,
        'elapsed_seconds': time.time() - t0,
    }

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp46_weak_strong.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to {outpath}")
    print(f"  Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
