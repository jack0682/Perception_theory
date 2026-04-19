#!/usr/bin/env python3
"""Exp82: raw-vs-seeded access-path trajectory comparison.

Logs total energy and overlap along one raw run and one seeded run so we can
identify the earliest clear divergence point.
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
from scc.optimizer import project_volume
from experiments.exp72_frozen_branch_threshold import parse_config
from experiments.exp73_branch_catalog import make_init_fields
from experiments.exp75_typeb_seeded_continuation import discover_best_typeb
from experiments.exp78_search_protocol_upgrade import warm_continue_fields


def run_traj(graph, params, init_fields, lambda_rep, lambda_bar, max_iter, log_every):
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
            g_rep = lambda_rep * fields[1-k]
            S = fields[0] + fields[1]
            violation = np.maximum(0.0, S - 1.0)
            g_barrier = lambda_bar * 2.0 * violation
            g = g_intra + g_rep + g_barrier
            g_sigma = g - np.mean(g)
            max_gnorm = max(max_gnorm, float(np.linalg.norm(g_sigma) / np.sqrt(n)))
            fields[k] = project_volume(fields[k] - dt * g_sigma, masses[k])
        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt = max(dt * 0.7, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt = min(dt * 1.05, 0.1)
        prev_gnorm = max_gnorm
        if tau == 1 or tau % log_every == 0 or tau == max_iter:
            E1,_ = ec.energy(fields[0]); E2,_ = ec.energy(fields[1])
            overlap = float(fields[0] @ fields[1])
            simplex = np.maximum(0.0, fields[0] + fields[1] - 1.0)
            total = float(E1 + E2 + lambda_rep * overlap + lambda_bar * float(simplex @ simplex))
            logs.append({'iter': tau, 'total_energy': total, 'overlap': overlap, 'max_gnorm': max_gnorm})
    return logs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='20x20:0.6')
    ap.add_argument('--target-lambda', type=float, default=0.5)
    ap.add_argument('--discover-inits', type=int, default=24)
    ap.add_argument('--raw-seed', type=int, default=0)
    ap.add_argument('--max-iter', type=int, default=200)
    ap.add_argument('--log-every', type=int, default=5)
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
    path=[]
    if args.target_lambda >= 0.05: path.append(0.05)
    if args.target_lambda >= 0.1: path.append(0.1)
    if args.target_lambda not in path: path.append(args.target_lambda)
    seeded_fields, _ = warm_continue_fields(graph, params, side, args.lambda_bar, base_fields, path, 4, args.max_iter)
    raw_fields = make_init_fields(n, mass_each, seed=2000 + args.raw_seed, mode='random')

    raw_logs = run_traj(graph, params, raw_fields, args.target_lambda, args.lambda_bar, args.max_iter, args.log_every)
    seed_logs = run_traj(graph, params, seeded_fields, args.target_lambda, args.lambda_bar, args.max_iter, args.log_every)

    # earliest divergence by simple thresholds
    earliest = None
    for rl, sl in zip(raw_logs, seed_logs):
        if abs(rl['total_energy'] - sl['total_energy']) > 0.5 or abs(rl['overlap'] - sl['overlap']) > 0.1:
            earliest = rl['iter']
            break

    out = {'experiment':'exp82_access_path_trajectory','config':args.config,'target_lambda':args.target_lambda,'earliest_divergence_iter':earliest,'raw_logs':raw_logs,'seed_logs':seed_logs}
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames=['trajectory','iter','total_energy','overlap','max_gnorm']
        writer=csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for name, logs in [('raw', raw_logs), ('seed', seed_logs)]:
            for log in logs:
                row={'trajectory':name}
                row.update(log)
                writer.writerow(row)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    print('earliest_divergence_iter', earliest)
    print('raw_first', raw_logs[:3])
    print('seed_first', seed_logs[:3])


if __name__ == '__main__':
    main()
