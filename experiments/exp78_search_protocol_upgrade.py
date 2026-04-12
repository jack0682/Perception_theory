#!/usr/bin/env python3
"""Exp78: inject recovered continuation branch into direct optimization.

For representative lambdas, compare:
- the seeded continuation branch total energy,
- the best raw-catalog discovered competitor,
- the best branch returned by direct optimization when the seeded branch is
  supplied as an initializer/restart seed.
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
from experiments.exp74_branch_family_match import family_distance
from experiments.exp75_typeb_seeded_continuation import discover_best_typeb
from experiments.exp77_selection_vs_persistence import total_energy


def warm_continue_fields(graph, params, side, lambda_bar, base_fields, lambda_path, n_restarts, max_iter):
    prev_fields = [u.copy() for u in base_fields]
    prev_metrics = None
    for lam in lambda_path:
        results = find_k_formations(
            graph, params, K=2, lambda_rep=lam, lambda_bar=lambda_bar,
            n_restarts=n_restarts, max_iter=max_iter, init_fields=prev_fields,
        )
        prev_fields = [r.u.copy() for r in results]
        prev_metrics = branch_metrics(f'continue_{lam:g}', prev_fields, graph, params, side, lambda_bar)
    return prev_fields, prev_metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--lambdas', nargs='+', type=float, default=[0.1, 0.5, 1.0])
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--seed-restarts', type=int, default=4)
    ap.add_argument('--direct-restarts', type=int, default=6)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--catalog-json', type=Path, required=True)
    ap.add_argument('--output-json', type=Path, required=True)
    ap.add_argument('--output-csv', type=Path, required=True)
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.direct_restarts, max_iter=args.max_iter)
    catalog = json.loads(args.catalog_json.read_text())['representatives']

    base, base_fields = discover_best_typeb(graph, params, side, 0.0, args.discover_inits, args.max_iter, args.lambda_bar)
    if base is None or base_fields is None:
        raise RuntimeError('No Type B candidate found at source lambda')

    rows = []
    lambda_path = []
    for lam in sorted(args.lambdas):
        lambda_path.append(lam)
        cont_fields, cont_metrics = warm_continue_fields(
            graph, params, side, args.lambda_bar, base_fields, lambda_path, args.seed_restarts, args.max_iter
        )
        cont_total = total_energy(cont_metrics, lam)
        best_catalog = min(catalog, key=lambda c: total_energy(c, lam))
        best_catalog_total = total_energy(best_catalog, lam)

        results = find_k_formations(
            graph, params, K=2, lambda_rep=lam, lambda_bar=args.lambda_bar,
            n_restarts=args.direct_restarts, max_iter=args.max_iter, init_fields=cont_fields,
        )
        best_fields = [r.u.copy() for r in results]
        best_metrics = branch_metrics(f'direct_best_{lam:g}', best_fields, graph, params, side, args.lambda_bar)
        best_total = total_energy(best_metrics, lam)

        rows.append({
            'lambda': lam,
            'continued_branch_type': cont_metrics['branch_type'],
            'continued_total': cont_total,
            'catalog_best_key': best_catalog['key'],
            'catalog_best_type': best_catalog['branch_type'],
            'catalog_best_total': best_catalog_total,
            'direct_best_type': best_metrics['branch_type'],
            'direct_best_total': best_total,
            'direct_minus_cont': best_total - cont_total,
            'direct_minus_catalog': best_total - best_catalog_total,
            'distance_direct_to_cont': family_distance(cont_metrics, best_metrics, side),
            'distance_direct_to_base': family_distance(base, best_metrics, side),
        })

    out = {
        'experiment': 'exp78_search_protocol_upgrade',
        'config': args.config,
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
