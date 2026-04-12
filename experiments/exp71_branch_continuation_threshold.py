#!/usr/bin/env python3
"""Exp71: warm-start branch continuation for lambda_rep threshold estimates."""

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
from scc.multi import find_k_formations, classify_regime
from experiments.exp65_formation_tracking import center_of_mass


def parse_config(config: str):
    side_s, c_ref_s = config.split(':', 1)
    side = int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)
    return side, float(c_ref_s)


def _field_distance(a_fields, b_fields, grid_size: int) -> dict:
    """Distance between two ordered field pairs."""
    diffs = [b_fields[k] - a_fields[k] for k in range(len(b_fields))]
    n = len(b_fields[0])
    field_l2 = float(np.sqrt(sum(np.dot(d, d) for d in diffs)) / np.sqrt(n))
    field_linf = float(max(np.max(np.abs(d)) for d in diffs))
    a_centers = [center_of_mass(f, grid_size) for f in a_fields]
    b_centers = [center_of_mass(f, grid_size) for f in b_fields]
    center_step = float(max(
        np.hypot(b_centers[k][0] - a_centers[k][0], b_centers[k][1] - a_centers[k][1])
        for k in range(len(b_fields))
    ) / max(grid_size - 1, 1))
    return {'field_l2_step': field_l2, 'field_linf_step': field_linf, 'center_step': center_step}


def branch_distance(prev_fields, fields, grid_size: int, root_fields=None) -> dict:
    """Measure warm-start branch displacement with label-swap matching.

    The K=2 labels are arbitrary.  We compute both direct and swapped distances
    to the previous fields and use the smaller one for jump detection.  If a
    root branch is provided, also record distance to the original branch seed.
    """
    if prev_fields is None:
        base = {
            'field_l2_step': 0.0,
            'field_linf_step': 0.0,
            'center_step': 0.0,
            'label_swapped': False,
            'field_l2_from_root': 0.0,
            'center_from_root': 0.0,
            'jump_flag': False,
        }
        return base

    direct = _field_distance(prev_fields, fields, grid_size)
    swapped_fields = [fields[1], fields[0]] if len(fields) == 2 else fields
    swapped = _field_distance(prev_fields, swapped_fields, grid_size)
    use_swapped = swapped['field_l2_step'] < direct['field_l2_step']
    chosen = swapped if use_swapped else direct

    if root_fields is not None:
        root_direct = _field_distance(root_fields, swapped_fields if use_swapped else fields, grid_size)
        root_l2 = root_direct['field_l2_step']
        root_center = root_direct['center_step']
    else:
        root_l2 = 0.0
        root_center = 0.0

    # Heuristic jump flag: conservative; intended for audit, not theorem.
    jump = bool(chosen['field_l2_step'] > 0.25 or chosen['field_linf_step'] > 0.5 or chosen['center_step'] > 0.10)
    return {
        **chosen,
        'label_swapped': bool(use_swapped),
        'field_l2_from_root': float(root_l2),
        'center_from_root': float(root_center),
        'jump_flag': jump,
    }


def pair_metrics(fields, graph, params, lambda_rep, lambda_bar, grid_size):
    u1, u2 = fields
    ec = EnergyComputer(graph, params)
    ec.normalize_weights(c=params.volume_fraction)
    e1, _ = ec.energy(u1)
    e2, _ = ec.energy(u2)
    overlap = float(np.dot(u1, u2))
    simplex = np.maximum(0.0, u1 + u2 - 1.0)
    barrier = lambda_bar * float(np.dot(simplex, simplex))
    e_lambda = float(e1 + e2 + lambda_rep * overlap + barrier)
    e0 = float(e1 + e2 + barrier)
    c1 = center_of_mass(u1, grid_size)
    c2 = center_of_mass(u2, grid_size)
    pair_mid = ((c1[0] + c2[0]) / 2.0, (c1[1] + c2[1]) / 2.0)
    grid_center = ((grid_size - 1) / 2.0, (grid_size - 1) / 2.0)
    center_offset = float(np.hypot(pair_mid[0] - grid_center[0], pair_mid[1] - grid_center[1]) / max(grid_size - 1, 1))
    sep = float(np.hypot(c2[0] - c1[0], c2[1] - c1[1]))
    if center_offset < 0.08:
        branch_type = 'Type A candidate'
    elif center_offset >= 0.12:
        branch_type = 'Type B candidate'
    else:
        branch_type = 'Mixed/ambiguous'
    return {
        'E_lambda': e_lambda,
        'E0_inferred': e0,
        'self1': float(e1),
        'self2': float(e2),
        'overlap': overlap,
        'simplex_penalty': barrier,
        'center_offset_norm': center_offset,
        'separation': sep,
        'branch_type': branch_type,
        'regime_lambda': classify_regime(fields, graph, params, lambda_rep=lambda_rep, method='lambda'),
    }


def continue_branch(graph, params, grid_size, lambdas, lambda_bar, n_restarts, max_iter, init_fields=None):
    rows = []
    fields = init_fields
    prev_fields = None
    root_fields = [f.copy() for f in init_fields] if init_fields is not None else None
    for lam in lambdas:
        start_fields = [f.copy() for f in fields] if fields is not None else None
        results = find_k_formations(
            graph, params, K=2, lambda_rep=lam, lambda_bar=lambda_bar,
            n_restarts=n_restarts, max_iter=max_iter, init_fields=fields,
        )
        fields = [r.u.copy() for r in results]
        if root_fields is None:
            root_fields = [f.copy() for f in fields]
        metrics = pair_metrics(fields, graph, params, lam, lambda_bar, grid_size)
        step_metrics = branch_distance(prev_fields if prev_fields is not None else start_fields, fields, grid_size, root_fields=root_fields)
        rows.append({'lambda_rep': lam, **metrics, **step_metrics})
        prev_fields = [f.copy() for f in fields]
    return rows, fields


def estimate_threshold(up_rows, down_rows):
    estimates = []
    by_lam_down = {r['lambda_rep']: r for r in down_rows}
    for up in up_rows:
        lam = up['lambda_rep']
        down = by_lam_down.get(lam)
        if not down:
            continue
        # Lower-overlap candidate A and higher-overlap candidate B
        if up['overlap'] <= down['overlap']:
            A, B = up, down
            A_name, B_name = 'up', 'down'
        else:
            A, B = down, up
            A_name, B_name = 'down', 'up'
        dE0 = A['E0_inferred'] - B['E0_inferred']
        dR = B['overlap'] - A['overlap']
        estimates.append({
            'lambda_rep': lam,
            'lower_overlap_branch': A_name,
            'higher_overlap_branch': B_name,
            'delta_E0': float(dE0),
            'delta_R': float(dR),
            'lambda_star': float(dE0 / dR) if dR > 1e-12 else None,
            'same_type': up['branch_type'] == down['branch_type'],
            'up_type': up['branch_type'],
            'down_type': down['branch_type'],
            'up_jump': bool(up.get('jump_flag', False)),
            'down_jump': bool(down.get('jump_flag', False)),
            'estimate_continuous': not bool(up.get('jump_flag', False) or down.get('jump_flag', False)),
        })
    return estimates


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='10x10:0.6')
    ap.add_argument('--lambdas', nargs='+', type=float, default=[0, 0.05, 0.1, 0.2, 0.5, 1.0])
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--n-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=500)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp71_branch_continuation_threshold.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp71_branch_continuation_threshold.csv')
    args = ap.parse_args()

    grid_size, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=args.n_restarts, max_iter=args.max_iter)
    lambdas_up = args.lambdas
    lambdas_down = list(reversed(args.lambdas))

    up_rows, _ = continue_branch(graph, params, grid_size, lambdas_up, args.lambda_bar, args.n_restarts, args.max_iter)
    down_rows_rev, _ = continue_branch(graph, params, grid_size, lambdas_down, args.lambda_bar, args.n_restarts, args.max_iter)
    down_rows = list(reversed(down_rows_rev))
    estimates = estimate_threshold(up_rows, down_rows)

    output = {
        'experiment': 'exp71_branch_continuation_threshold',
        'config': args.config,
        'lambdas': args.lambdas,
        'up_branch': up_rows,
        'down_branch': down_rows,
        'threshold_estimates': estimates,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = ['direction', 'lambda_rep', 'E_lambda', 'E0_inferred', 'overlap', 'center_offset_norm', 'separation', 'branch_type', 'regime_lambda', 'field_l2_step', 'field_linf_step', 'center_step', 'label_swapped', 'field_l2_from_root', 'center_from_root', 'jump_flag']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in up_rows:
            writer.writerow({'direction': 'up', **{k: row[k] for k in fieldnames if k != 'direction'}})
        for row in down_rows:
            writer.writerow({'direction': 'down', **{k: row[k] for k in fieldnames if k != 'direction'}})

    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV:  {args.output_csv}")
    for est in estimates:
        print(f"lambda={est['lambda_rep']}: up={est['up_type']} down={est['down_type']} dE0={est['delta_E0']:.4f} dR={est['delta_R']:.4f} lambda*={est['lambda_star']} continuous={est['estimate_continuous']}")


if __name__ == '__main__':
    main()
