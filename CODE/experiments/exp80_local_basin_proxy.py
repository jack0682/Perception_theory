#!/usr/bin/env python3
"""Exp80: local basin proxy around the continued branch.

Perturb the continued target branch with controlled Gaussian noise and measure
how often optimization returns to the same family. This approximates local basin
thickness and complements the raw-start accessibility diagnostic.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations
from experiments.exp72_frozen_branch_threshold import parse_config, branch_metrics
from experiments.exp74_branch_family_match import family_distance
from experiments.exp75_typeb_seeded_continuation import discover_best_typeb
from experiments.exp78_search_protocol_upgrade import warm_continue_fields
from scc.optimizer import project_volume


def perturb_fields(fields, mass_each, sigma, seed):
    rng = np.random.RandomState(seed)
    out = []
    for u in fields:
        v = u + sigma * rng.randn(*u.shape)
        out.append(project_volume(v, mass_each))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--target-lambda', type=float, default=0.5)
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--n-perturbs', type=int, default=8)
    ap.add_argument('--sigmas', nargs='+', type=float, default=[0.01, 0.02, 0.05, 0.1])
    ap.add_argument('--seed-restarts', type=int, default=4)
    ap.add_argument('--raw-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--distance-threshold', type=float, default=4.0)
    ap.add_argument('--output-json', type=Path, required=True)
    ap.add_argument('--output-csv', type=Path, required=True)
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.raw_restarts, max_iter=args.max_iter)
    n = side * side
    mass_each = params.volume_fraction * n

    base, base_fields = discover_best_typeb(graph, params, side, 0.0, args.discover_inits, args.max_iter, args.lambda_bar)
    if base is None or base_fields is None:
        raise RuntimeError('No Type B candidate found at lambda=0')

    path = []
    if args.target_lambda >= 0.05:
        path.append(0.05)
    if args.target_lambda >= 0.1:
        path.append(0.1)
    if args.target_lambda not in path:
        path.append(args.target_lambda)
    cont_fields, cont_metrics = warm_continue_fields(
        graph, params, side, args.lambda_bar, base_fields, path, args.seed_restarts, args.max_iter
    )

    rows = []
    for sigma in args.sigmas:
        hits = 0
        for i in range(args.n_perturbs):
            init = perturb_fields(cont_fields, mass_each, sigma, seed=3000 + i)
            results = find_k_formations(
                graph, params, K=2, lambda_rep=args.target_lambda, lambda_bar=args.lambda_bar,
                n_restarts=1, max_iter=args.max_iter, init_fields=init,
            )
            fields = [r.u.copy() for r in results]
            m = branch_metrics(f'pert_sigma{sigma:g}_{i}', fields, graph, params, side, args.lambda_bar)
            dist = family_distance(cont_metrics, m, side)
            hit = dist <= args.distance_threshold
            hits += int(hit)
            rows.append({
                'sigma': sigma,
                'trial': i,
                'branch_type': m['branch_type'],
                'family_distance_to_continued': dist,
                'within_threshold': hit,
                'E0': m['E0'],
                'overlap': m['overlap'],
            })

    summary = []
    for sigma in args.sigmas:
        sub = [r for r in rows if r['sigma'] == sigma]
        hits = sum(int(r['within_threshold']) for r in sub)
        summary.append({'sigma': sigma, 'hits': hits, 'total': len(sub), 'hit_rate': hits/len(sub) if sub else None})

    out = {
        'experiment': 'exp80_local_basin_proxy',
        'config': args.config,
        'target_lambda': args.target_lambda,
        'distance_threshold': args.distance_threshold,
        'continued_branch_type': cont_metrics['branch_type'],
        'summary': summary,
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader(); writer.writerows(rows)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('continued_branch_type', cont_metrics['branch_type'])
    for s in summary:
        print(s)


if __name__ == '__main__':
    main()
