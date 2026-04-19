#!/usr/bin/env python3
"""Exp73: K=2 branch catalog and frozen energy-line comparison.

Runs multiple initialized K=2 optimizations at selected lambda_rep values,
clusters resulting branches by coarse geometry/overlap, and compares frozen
energy lines E_lambda = E0 + lambda * overlap across candidate branches.
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
from scc.multi import find_k_formations, classify_regime
from scc.optimizer import project_volume
from experiments.exp72_frozen_branch_threshold import parse_config, branch_metrics, threshold_between


def make_init_fields(n: int, mass_each: float, seed: int, mode: str):
    rng = np.random.RandomState(seed)
    if mode == 'random':
        a = rng.rand(n)
        b = rng.rand(n)
    elif mode == 'anti_random':
        a = rng.rand(n)
        b = 1.0 - a + 0.05 * rng.rand(n)
    else:
        a = rng.randn(n)
        b = rng.randn(n)
    return [project_volume(a, mass_each), project_volume(b, mass_each)]


def branch_key(m: dict) -> str:
    return '|'.join([
        m['branch_type'],
        f"co{round(m['center_offset_norm'], 2):.2f}",
        f"ov{round(m['overlap'], 1):.1f}",
        f"sep{round(m['separation'], 1):.1f}",
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='10x10:0.6')
    ap.add_argument('--source-lambdas', nargs='+', type=float, default=[0.0, 1.0])
    ap.add_argument('--eval-lambdas', nargs='+', type=float, default=[0, 0.01, 0.05, 0.1, 0.5, 1, 5])
    ap.add_argument('--n-inits', type=int, default=8)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp73_branch_catalog.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp73_branch_catalog.csv')
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    n = side * side
    half_c = c_ref / 2.0
    mass_each = half_c * n
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=half_c, n_restarts=1, max_iter=args.max_iter)

    candidates = []
    modes = ['random', 'anti_random']
    for lam in args.source_lambdas:
        for i in range(args.n_inits):
            init = make_init_fields(n, mass_each, seed=1000 + i, mode=modes[i % len(modes)])
            results = find_k_formations(graph, params, K=2, lambda_rep=lam, lambda_bar=args.lambda_bar,
                                        n_restarts=1, max_iter=args.max_iter, init_fields=init)
            fields = [r.u.copy() for r in results]
            m = branch_metrics(f'cand_lam{lam:g}_init{i}', fields, graph, params, side, args.lambda_bar)
            m['source_lambda'] = lam
            m['init_index'] = i
            m['key'] = branch_key(m)
            candidates.append(m)

    # Cluster: keep lowest E0 per coarse key
    clusters = {}
    for c in candidates:
        if c['key'] not in clusters or c['E0'] < clusters[c['key']]['E0']:
            clusters[c['key']] = c
    reps = list(clusters.values())

    energy_rows = []
    for c in reps:
        for lam in args.eval_lambdas:
            energy_rows.append({
                'key': c['key'],
                'branch': c['branch'],
                'source_lambda': c['source_lambda'],
                'init_index': c['init_index'],
                'eval_lambda': lam,
                'E_lambda': c['E0'] + lam * c['overlap'],
                'E0': c['E0'],
                'overlap': c['overlap'],
                'center_offset_norm': c['center_offset_norm'],
                'separation': c['separation'],
                'branch_type': c['branch_type'],
            })

    thresholds = []
    for i in range(len(reps)):
        for j in range(i+1, len(reps)):
            thresholds.append({
                'a_key': reps[i]['key'],
                'b_key': reps[j]['key'],
                'lambda_cross': threshold_between(reps[i], reps[j]),
                'E0_a': reps[i]['E0'], 'E0_b': reps[j]['E0'],
                'overlap_a': reps[i]['overlap'], 'overlap_b': reps[j]['overlap'],
            })

    out = {'experiment': 'exp73_branch_catalog', 'config': args.config, 'candidates': candidates, 'representatives': reps, 'energy_rows': energy_rows, 'thresholds': thresholds}
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(energy_rows[0].keys()))
        writer.writeheader(); writer.writerows(energy_rows)

    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV: {args.output_csv}")
    print(f"candidates={len(candidates)} representatives={len(reps)}")
    for c in sorted(reps, key=lambda x: x['E0']):
        print(f"{c['key']}: E0={c['E0']:.6f} overlap={c['overlap']:.6f} source_lam={c['source_lambda']} init={c['init_index']}")


if __name__ == '__main__':
    main()
