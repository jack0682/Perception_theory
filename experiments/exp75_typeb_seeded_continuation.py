#!/usr/bin/env python3
"""Exp75: seeded continuation from the best zero-lambda Type B branch.

Hardest-sentinel follow-up for 20x20:0.6 (or another config). The script:
1. searches many lambda=0 initializations for the best Type B candidate,
2. reuses that discovered field pair as the initialization for positive lambdas,
3. measures whether the resulting positive-lambda optimizers remain in the same
   branch family or immediately switch away.
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
from experiments.exp73_branch_catalog import make_init_fields
from experiments.exp74_branch_family_match import family_distance


def discover_best_typeb(graph, params, side, source_lambda: float, n_inits: int, max_iter: int, lambda_bar: float):
    n = side * side
    mass_each = params.volume_fraction * n
    modes = ['random', 'anti_random']
    best = None
    best_fields = None
    for i in range(n_inits):
        init = make_init_fields(n, mass_each, seed=1000 + i, mode=modes[i % len(modes)])
        results = find_k_formations(graph, params, K=2, lambda_rep=source_lambda, lambda_bar=lambda_bar,
                                    n_restarts=1, max_iter=max_iter, init_fields=init)
        fields = [r.u.copy() for r in results]
        m = branch_metrics(f'zero_seed_{i}', fields, graph, params, side, lambda_bar)
        m['source_lambda'] = source_lambda
        m['init_index'] = i
        if m['branch_type'] != 'Type B candidate':
            continue
        if best is None or m['E0'] < best['E0']:
            best = m
            best_fields = fields
    return best, best_fields


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--source-lambda', type=float, default=0.0)
    ap.add_argument('--target-lambdas', nargs='+', type=float, default=[0.05, 0.1, 0.2, 0.5, 1.0])
    ap.add_argument('--n-inits', type=int, default=24)
    ap.add_argument('--n-restarts', type=int, default=4)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--distance-threshold', type=float, default=5.0)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp75_typeb_seeded_continuation.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp75_typeb_seeded_continuation.csv')
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.n_restarts, max_iter=args.max_iter)

    base, base_fields = discover_best_typeb(graph, params, side, args.source_lambda, args.n_inits, args.max_iter, args.lambda_bar)
    if base is None or base_fields is None:
        raise RuntimeError('No Type B candidate found at source lambda')

    rows = []
    for lam in args.target_lambdas:
        results = find_k_formations(graph, params, K=2, lambda_rep=lam, lambda_bar=args.lambda_bar,
                                    n_restarts=args.n_restarts, max_iter=args.max_iter, init_fields=base_fields)
        fields = [r.u.copy() for r in results]
        m = branch_metrics(f'target_lambda_{lam:g}', fields, graph, params, side, args.lambda_bar)
        m['target_lambda'] = lam
        m['family_distance_from_base'] = family_distance(base, m, side)
        m['within_threshold'] = m['family_distance_from_base'] <= args.distance_threshold
        rows.append(m)

    out = {
        'experiment': 'exp75_typeb_seeded_continuation',
        'config': args.config,
        'distance_threshold': args.distance_threshold,
        'base': base,
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = ['target_lambda', 'branch_type', 'E0', 'overlap', 'center_offset_norm', 'separation', 'family_distance_from_base', 'within_threshold']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r[k] for k in fieldnames})

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('Base:', base['branch'], base['branch_type'], f"E0={base['E0']:.6f}", f"overlap={base['overlap']:.6f}")
    for r in rows:
        print(f"lambda={r['target_lambda']}: type={r['branch_type']} E0={r['E0']:.6f} overlap={r['overlap']:.6f} dist={r['family_distance_from_base']:.6f} within={r['within_threshold']}")


if __name__ == '__main__':
    main()
