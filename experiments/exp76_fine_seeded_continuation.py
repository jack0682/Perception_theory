#!/usr/bin/env python3
"""Exp76: fine lambda-grid seeded continuation from recovered Type B seed.

Tracks a single recovered zero-lambda Type B branch across a finer positive-lambda
sequence using warm continuation. Records branch labels and family-distance drift
relative to both the original seed and the previous step.
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--source-lambda', type=float, default=0.0)
    ap.add_argument('--target-lambdas', nargs='+', type=float, default=[0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0])
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--n-restarts', type=int, default=4)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--distance-threshold', type=float, default=5.0)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp76_fine_seeded_continuation.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp76_fine_seeded_continuation.csv')
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.n_restarts, max_iter=args.max_iter)

    base, base_fields = discover_best_typeb(
        graph, params, side, args.source_lambda, args.discover_inits, args.max_iter, args.lambda_bar
    )
    if base is None or base_fields is None:
        raise RuntimeError('No Type B candidate found at source lambda')

    prev_fields = [u.copy() for u in base_fields]
    prev_metrics = base
    rows = []

    for lam in args.target_lambdas:
        results = find_k_formations(
            graph,
            params,
            K=2,
            lambda_rep=lam,
            lambda_bar=args.lambda_bar,
            n_restarts=args.n_restarts,
            max_iter=args.max_iter,
            init_fields=prev_fields,
        )
        fields = [r.u.copy() for r in results]
        m = branch_metrics(f'target_lambda_{lam:g}', fields, graph, params, side, args.lambda_bar)
        m['target_lambda'] = lam
        m['family_distance_from_base'] = family_distance(base, m, side)
        m['family_distance_from_prev'] = family_distance(prev_metrics, m, side)
        m['within_base_threshold'] = m['family_distance_from_base'] <= args.distance_threshold
        m['within_prev_threshold'] = m['family_distance_from_prev'] <= args.distance_threshold
        rows.append(m)
        prev_fields = fields
        prev_metrics = m

    first_non_typeb = next((r['target_lambda'] for r in rows if r['branch_type'] != 'Type B candidate'), None)

    out = {
        'experiment': 'exp76_fine_seeded_continuation',
        'config': args.config,
        'distance_threshold': args.distance_threshold,
        'base': base,
        'first_non_typeb_lambda': first_non_typeb,
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'target_lambda', 'branch_type', 'E0', 'overlap', 'center_offset_norm', 'separation',
            'family_distance_from_base', 'family_distance_from_prev', 'within_base_threshold', 'within_prev_threshold'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r[k] for k in fieldnames})

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('Base:', base['branch_type'], f"E0={base['E0']:.6f}", f"overlap={base['overlap']:.6f}")
    print('first_non_typeb_lambda=', first_non_typeb)
    for r in rows:
        print(
            f"lambda={r['target_lambda']}: type={r['branch_type']} E0={r['E0']:.6f} overlap={r['overlap']:.6f} "
            f"d_base={r['family_distance_from_base']:.6f} d_prev={r['family_distance_from_prev']:.6f}"
        )


if __name__ == '__main__':
    main()
