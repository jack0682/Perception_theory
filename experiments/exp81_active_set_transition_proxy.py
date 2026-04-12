#!/usr/bin/env python3
"""Exp81: active-set / simplex-region transition proxy for raw vs seeded starts.

Runs a simplified K=2 optimizer loop while logging coarse region statistics that
approximate active-set/penalty-region transitions.
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
from scc.multi import _total_energy
from scc.optimizer import project_volume
from experiments.exp72_frozen_branch_threshold import parse_config, branch_metrics, _support_signature
from experiments.exp73_branch_catalog import make_init_fields
from experiments.exp75_typeb_seeded_continuation import discover_best_typeb
from experiments.exp78_search_protocol_upgrade import warm_continue_fields


def snapshot(fields, graph, params, ec, lambda_rep, lambda_bar):
    S = fields[0] + fields[1]
    simplex_violation = np.maximum(0.0, S - 1.0)
    sig1 = _support_signature(fields[0], graph, 0.1)
    sig2 = _support_signature(fields[1], graph, 0.1)
    comps = sorted([sig1['components'], sig2['components']])
    counts = sorted([sig1['count'], sig2['count']])
    return {
        'simplex_count': int((simplex_violation > 1e-8).sum()),
        'simplex_mass': float(simplex_violation.sum()),
        'near_zero_count': int(((fields[0] < 1e-6).sum()) + ((fields[1] < 1e-6).sum())),
        'near_one_count': int(((fields[0] > 1 - 1e-6).sum()) + ((fields[1] > 1 - 1e-6).sum())),
        'tau01_count_min': counts[0],
        'tau01_count_max': counts[1],
        'tau01_comp_min': comps[0],
        'tau01_comp_max': comps[1],
        'total_energy': float(_total_energy(fields, ec, graph, lambda_rep, lambda_bar)),
    }


def run_logged_trajectory(graph, params, init_fields, lambda_rep, lambda_bar, max_iter, log_every):
    n = graph.n
    masses = [params.volume_fraction * n, params.volume_fraction * n]
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    fields = [project_volume(init_fields[0].copy(), masses[0]), project_volume(init_fields[1].copy(), masses[1])]
    dt = params.dt_init
    prev_gnorm = float('inf')
    logs = []

    for tau in range(1, max_iter + 1):
        max_gnorm = 0.0
        for k in range(2):
            g_intra = ec.gradient(fields[k])
            g_rep = lambda_rep * fields[1 - k]
            S = fields[0] + fields[1]
            violation = np.maximum(0.0, S - 1.0)
            g_barrier = lambda_bar * 2.0 * violation
            g_total = g_intra + g_rep + g_barrier
            g_sigma = g_total - np.mean(g_total)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)
            fields[k] = project_volume(fields[k] - dt * g_sigma, masses[k])
        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt = max(dt * 0.7, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt = min(dt * 1.05, 0.1)
        prev_gnorm = max_gnorm
        if tau == 1 or tau % log_every == 0 or tau == max_iter:
            snap = snapshot(fields, graph, params, ec, lambda_rep, lambda_bar)
            snap['iter'] = tau
            snap['max_gnorm'] = max_gnorm
            logs.append(snap)
    return fields, logs


def transition_count(logs):
    if not logs:
        return 0
    keys = ['simplex_count','near_zero_count','near_one_count','tau01_count_min','tau01_count_max','tau01_comp_min','tau01_comp_max']
    prev = tuple(logs[0][k] for k in keys)
    cnt = 0
    for log in logs[1:]:
        cur = tuple(log[k] for k in keys)
        if cur != prev:
            cnt += 1
            prev = cur
    return cnt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--target-lambda', type=float, default=0.5)
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--raw-seed', type=int, default=0)
    ap.add_argument('--max-iter', type=int, default=200)
    ap.add_argument('--log-every', type=int, default=10)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--output-json', type=Path, required=True)
    ap.add_argument('--output-csv', type=Path, required=True)
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2.0, n_restarts=1, max_iter=args.max_iter)
    n = side * side
    mass_each = params.volume_fraction * n

    base, base_fields = discover_best_typeb(graph, params, side, 0.0, args.discover_inits, args.max_iter, args.lambda_bar)
    if base is None or base_fields is None:
        raise RuntimeError('No Type B base found')

    path = []
    if args.target_lambda >= 0.05:
        path.append(0.05)
    if args.target_lambda >= 0.1:
        path.append(0.1)
    if args.target_lambda not in path:
        path.append(args.target_lambda)
    seeded_fields, _ = warm_continue_fields(graph, params, side, args.lambda_bar, base_fields, path, 4, args.max_iter)
    raw_fields = make_init_fields(n, mass_each, seed=2000 + args.raw_seed, mode='random')

    raw_final, raw_logs = run_logged_trajectory(graph, params, raw_fields, args.target_lambda, args.lambda_bar, args.max_iter, args.log_every)
    seed_final, seed_logs = run_logged_trajectory(graph, params, seeded_fields, args.target_lambda, args.lambda_bar, args.max_iter, args.log_every)

    raw_metrics = branch_metrics('raw_final', raw_final, graph, params, side, args.lambda_bar)
    seed_metrics = branch_metrics('seed_final', seed_final, graph, params, side, args.lambda_bar)

    out = {
        'experiment': 'exp81_active_set_transition_proxy',
        'config': args.config,
        'target_lambda': args.target_lambda,
        'raw_transition_count': transition_count(raw_logs),
        'seed_transition_count': transition_count(seed_logs),
        'raw_final': raw_metrics,
        'seed_final': seed_metrics,
        'raw_logs': raw_logs,
        'seed_logs': seed_logs,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = ['trajectory','iter','simplex_count','simplex_mass','near_zero_count','near_one_count','tau01_count_min','tau01_count_max','tau01_comp_min','tau01_comp_max','total_energy','max_gnorm']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for traj, logs in [('raw', raw_logs), ('seed', seed_logs)]:
            for log in logs:
                row = {'trajectory': traj}
                row.update({k: log[k] for k in fieldnames if k != 'trajectory'})
                writer.writerow(row)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('raw_transition_count', out['raw_transition_count'], 'raw_final_type', raw_metrics['branch_type'])
    print('seed_transition_count', out['seed_transition_count'], 'seed_final_type', seed_metrics['branch_type'])


if __name__ == '__main__':
    main()
