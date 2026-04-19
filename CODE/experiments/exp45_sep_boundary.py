#!/usr/bin/env python3
"""Experiment 45: Sep-Weak Regime Boundary Validation.

Validates the Sep -> Weak regime transition by varying formation placement
distance on a small grid with high volume fraction, forcing formations
to interact as distance decreases.

Uses coupling_strength() with mu_floor regularization for Lambda computation.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import (find_k_formations, inter_formation_distances,
                        classify_regime, formation_overlap, coupling_strength)
from scc.optimizer import project_volume


def _make_init_fields(grid, K, m_each, center_distance):
    """Create initial fields with controlled center distance on a grid."""
    n = grid.n
    side = int(np.sqrt(n))
    mid = side // 2

    offset = center_distance / 2.0
    centers = [(mid - offset, mid), (mid + offset, mid)]

    fields = []
    for k in range(K):
        cx, cy = centers[k]
        u = np.zeros(n)
        for i in range(side):
            for j in range(side):
                idx = i * side + j
                dist_sq = (i - cx)**2 + (j - cy)**2
                u[idx] = np.exp(-dist_sq / 3.0)
        u = project_volume(u, m_each)
        fields.append(u)
    return fields


def main():
    print("Experiment 45: Sep-Weak Regime Boundary (distance sweep)")
    print("=" * 70)
    t0 = time.time()

    # Small grid + high vf to force interaction
    grid = GraphState.grid_2d(10, 10)
    n = grid.n
    vf = 0.40
    m_each = vf * n
    lambda_rep = 1.0  # moderate repulsion

    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=15.0,  # lower beta for diffuse formations
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=vf,
    )

    results = []

    print(f"\n  {'cdist':>5s}  {'d_min':>5s}  {'overlap':>7s}  {'omega':>8s}  "
          f"{'mu_min':>7s}  {'Lambda':>10s}  {'geom':>20s}  {'lambda':>20s}")
    print(f"  {'-' * 95}")

    for center_dist in [1, 2, 3, 4, 5, 6, 7, 8]:
        try:
            init_fields = _make_init_fields(grid, 2, m_each, center_dist)

            sources = find_k_formations(
                grid, params, K=2,
                lambda_rep=lambda_rep,
                init_fields=init_fields,
                max_iter=1000, n_restarts=2,
            )

            fields = [s.u for s in sources]

            # Use coupling_strength for unified Lambda computation
            cs = coupling_strength(fields, grid, params, lambda_rep)
            Lambda = cs['Lambda']
            omega_max = float(np.max(cs['omega_matrix'] - np.eye(2)))
            mu_min = min(cs['mu_per_formation'])
            pred_lambda = cs['predicted_regime']

            # Also get geometric classification for comparison
            d_min_mat = inter_formation_distances(fields, grid)
            d_min = d_min_mat[0, 1]
            overlap_mat = formation_overlap(fields)
            overlap = overlap_mat[0, 1]
            geom_regime = classify_regime(fields, grid, method='geometric')

            print(f"  {center_dist:5d}  {d_min:5.0f}  {overlap:7.0f}  {omega_max:8.5f}  "
                  f"{mu_min:7.3f}  {Lambda:10.5f}  {geom_regime:>20s}  {pred_lambda:>20s}")

            results.append({
                'center_distance': center_dist,
                'd_min': float(d_min),
                'overlap': float(overlap),
                'omega_max': omega_max,
                'mu_per_formation': cs['mu_per_formation'],
                'mu_min': mu_min,
                'mu_floor': cs['mu_floor'],
                'Lambda_coupling': Lambda,
                'regime_geometric': geom_regime,
                'regime_lambda': pred_lambda,
            })

        except Exception as e:
            print(f"  {center_dist:5d}  FAILED: {e}")
            results.append({'center_distance': center_dist, 'error': str(e)})

    # Summary
    print(f"\n  --- Summary ---")
    geom_regimes = [r.get('regime_geometric') for r in results if 'regime_geometric' in r]
    lambda_regimes = [r.get('regime_lambda') for r in results if 'regime_lambda' in r]
    agreements = sum(1 for g, l in zip(geom_regimes, lambda_regimes) if g == l)
    print(f"  Geometric-Lambda agreement: {agreements}/{len(geom_regimes)}")

    for method, regimes in [('geometric', geom_regimes), ('lambda', lambda_regimes)]:
        transitions = [(i, regimes[i-1], regimes[i])
                       for i in range(1, len(regimes)) if regimes[i] != regimes[i-1]]
        print(f"  {method} transitions: {len(transitions)}")
        for idx, r_from, r_to in transitions:
            print(f"    At step {idx}: {r_from} -> {r_to}")

    # Save
    output = {
        'experiment': 'exp45_sep_boundary',
        'description': 'Sep-Weak regime boundary: distance sweep with coupling_strength',
        'grid': '10x10',
        'K': 2,
        'lambda_rep': lambda_rep,
        'vf': vf,
        'beta': 15.0,
        'results': results,
        'elapsed_seconds': time.time() - t0,
    }

    os.makedirs('experiments/results', exist_ok=True)
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp45_sep_boundary.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to {outpath}")
    print(f"  Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
