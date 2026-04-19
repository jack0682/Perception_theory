#!/usr/bin/env python3
"""Exp70: evaluate positive repulsion on a fixed zero-repulsion branch/path.

Separates pure overlap-excess effects from branch re-selection by:
1. selecting the K=2 source branch at source_lambda (default 0),
2. generating path images once from that fixed source and target,
3. evaluating the same path at multiple lambda_eval values.
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
from scc.energy import EnergyComputer
from scc.multi import find_k_formations
from scc.optimizer import find_formation
from experiments.exp67_relaxed_merge_paths import (
    direct_path,
    diffuse_shortcut_path,
    sequential_zero_overlap_path,
    path_stats,
    total_energy_relaxed,
)


def run(config: str, source_lambda: float, lambda_evals: list[float], lambda_bar: float, n_steps: int, n_restarts: int, max_iter: int) -> dict:
    side_s, c_ref_s = config.split(':', 1)
    side = int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)
    c_ref = float(c_ref_s)
    n = side * side
    half_c = c_ref / 2.0
    graph = GraphState.grid_2d(side, side)
    params_half = ParameterRegistry(volume_fraction=half_c, n_restarts=n_restarts, max_iter=max_iter)
    params_total = ParameterRegistry(volume_fraction=c_ref, n_restarts=n_restarts, max_iter=max_iter)

    k2 = find_k_formations(graph, params_half, K=2, lambda_rep=source_lambda, lambda_bar=lambda_bar,
                           n_restarts=n_restarts, max_iter=max_iter)
    u1, u2 = k2[0].u, k2[1].u
    k1 = find_formation(graph, params_total, normalize=True, verbose=False)
    u_merge = k1.u
    ec = EnergyComputer(graph, params_half)
    ec.normalize_weights(c=half_c)

    path_images = {
        'direct_relaxed_interpolation': direct_path(u1, u2, u_merge, n_steps),
        'diffuse_shortcut': diffuse_shortcut_path(u1, u2, u_merge, n_steps),
        'sequential_zero_overlap': sequential_zero_overlap_path(u1, u2, u_merge, n_steps),
    }

    rows = []
    detailed = []
    for lam in lambda_evals:
        source_energy = total_energy_relaxed((u1, u2), ec, lam, lambda_bar)['total']
        for name, images in path_images.items():
            stats = path_stats(name, images, ec, lam, lambda_bar, source_energy)
            row = {
                'config': config,
                'source_lambda': source_lambda,
                'lambda_eval': lam,
                'path': name,
                'source_energy': source_energy,
                'max_delta': stats['max_delta'],
                'max_index': stats['max_index'],
                'source_overlap': stats.get('source_overlap', 0.0),
                'max_overlap': stats.get('max_overlap', 0.0),
                'max_overlap_excess': stats.get('max_overlap_excess', 0.0),
                'predicted_overlap_excess_cost': lam * stats.get('max_overlap_excess', 0.0),
            }
            rows.append(row)
            detailed.append({'lambda_eval': lam, 'path': name, 'stats': stats})
    return {
        'experiment': 'exp70_fixed_branch_repulsion_eval',
        'config': config,
        'source_lambda': source_lambda,
        'lambda_evals': lambda_evals,
        'lambda_bar': lambda_bar,
        'n_steps': n_steps,
        'n_restarts': n_restarts,
        'max_iter': max_iter,
        'source_overlap': float(np.dot(u1, u2)),
        'rows': rows,
        'details': detailed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='10x10:0.6')
    ap.add_argument('--source-lambda', type=float, default=0.0)
    ap.add_argument('--lambda-evals', nargs='+', type=float, default=[0.0, 0.1, 1.0, 5.0])
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--n-steps', type=int, default=11)
    ap.add_argument('--n-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=250)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp70_fixed_branch_repulsion_eval.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp70_fixed_branch_repulsion_eval.csv')
    args = ap.parse_args()

    result = run(args.config, args.source_lambda, args.lambda_evals, args.lambda_bar, args.n_steps, args.n_restarts, args.max_iter)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(result['rows'][0].keys()))
        writer.writeheader()
        writer.writerows(result['rows'])
    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV: {args.output_csv}")
    for row in result['rows']:
        print(f"lambda={row['lambda_eval']:>4g} {row['path']:<30} max_delta={row['max_delta']:.6f} overlap_excess={row['max_overlap_excess']:.6f}")


if __name__ == '__main__':
    main()
