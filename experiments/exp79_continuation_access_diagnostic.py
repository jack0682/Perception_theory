#!/usr/bin/env python3
"""Exp79: continuation-access diagnostic for search failure.

Hypothesis tested: a lower-energy branch family is continuation-accessible but
rarely discovered from independent raw random initializations at the same lambda.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations
from experiments.exp72_frozen_branch_threshold import parse_config, branch_metrics
from experiments.exp73_branch_catalog import make_init_fields
from experiments.exp74_branch_family_match import family_distance
from experiments.exp75_typeb_seeded_continuation import discover_best_typeb
from experiments.exp78_search_protocol_upgrade import warm_continue_fields
from experiments.exp77_selection_vs_persistence import total_energy


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--target-lambda', type=float, default=0.5)
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--raw-inits', type=int, default=16)
    ap.add_argument('--seed-restarts', type=int, default=4)
    ap.add_argument('--raw-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--distance-threshold', type=float, default=5.0)
    ap.add_argument('--output-json', type=Path, required=True)
    ap.add_argument('--output-csv', type=Path, required=True)
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.raw_restarts, max_iter=args.max_iter)

    base, base_fields = discover_best_typeb(graph, params, side, 0.0, args.discover_inits, args.max_iter, args.lambda_bar)
    if base is None or base_fields is None:
        raise RuntimeError('No Type B candidate found at lambda=0')

    # Build continued target family at target lambda by warm continuation path.
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
    cont_total = total_energy(cont_metrics, args.target_lambda)

    n = side * side
    mass_each = params.volume_fraction * n
    modes = ['random', 'anti_random']
    raw_rows = []
    hits = 0
    for i in range(args.raw_inits):
        init = make_init_fields(n, mass_each, seed=2000 + i, mode=modes[i % len(modes)])
        results = find_k_formations(
            graph, params, K=2, lambda_rep=args.target_lambda, lambda_bar=args.lambda_bar,
            n_restarts=1, max_iter=args.max_iter, init_fields=init,
        )
        fields = [r.u.copy() for r in results]
        m = branch_metrics(f'raw_target_{i}', fields, graph, params, side, args.lambda_bar)
        dist = family_distance(cont_metrics, m, side)
        total = total_energy(m, args.target_lambda)
        hit = dist <= args.distance_threshold
        hits += int(hit)
        raw_rows.append({
            'raw_index': i,
            'branch_type': m['branch_type'],
            'total_energy': total,
            'E0': m['E0'],
            'overlap': m['overlap'],
            'family_distance_to_continued': dist,
            'within_threshold': hit,
        })

    out = {
        'experiment': 'exp79_continuation_access_diagnostic',
        'config': args.config,
        'target_lambda': args.target_lambda,
        'distance_threshold': args.distance_threshold,
        'continued_branch': {
            'branch_type': cont_metrics['branch_type'],
            'total_energy': cont_total,
            'E0': cont_metrics['E0'],
            'overlap': cont_metrics['overlap'],
        },
        'raw_hit_count': hits,
        'raw_total_count': len(raw_rows),
        'raw_hit_rate': hits / len(raw_rows) if raw_rows else None,
        'raw_rows': raw_rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = list(raw_rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(raw_rows)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('continued_branch', cont_metrics['branch_type'], f"total={cont_total:.6f}", f"overlap={cont_metrics['overlap']:.6f}")
    print('raw_hit_rate', hits, '/', len(raw_rows), '=', hits / len(raw_rows) if raw_rows else None)
    best_raw = min(raw_rows, key=lambda r: r['total_energy'])
    print('best_raw', best_raw)


if __name__ == '__main__':
    main()
