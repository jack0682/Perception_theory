#!/usr/bin/env python3
"""Exp72: frozen-candidate branch reselection threshold.

Optimizes two K=2 candidate branches at two source repulsion values, freezes
those fields, and evaluates E_lambda = E0 + lambda * overlap over a lambda grid
without reoptimization. This directly matches the finite-candidate theorem in
POSITIVE-REPULSION-BRANCH-RESELECTION.md.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.csgraph as csgraph

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.multi import find_k_formations, classify_regime
from experiments.exp65_formation_tracking import center_of_mass




def _support_signature(u, graph, tau: float):
    mask = np.asarray(u >= tau, dtype=bool)
    count = int(mask.sum())
    if count == 0:
        return {'count': 0, 'components': 0, 'largest': 0}
    idx = np.flatnonzero(mask)
    sub = graph.W[idx][:, idx]
    n_comp, labels = csgraph.connected_components(sub, directed=False, return_labels=True)
    sizes = np.bincount(labels, minlength=n_comp) if n_comp > 0 else np.array([], dtype=int)
    largest = int(sizes.max()) if sizes.size else 0
    return {'count': count, 'components': int(n_comp), 'largest': largest}


def _pair_signature(fields, graph, tau: float):
    sigs = [_support_signature(u, graph, tau) for u in fields]
    counts = sorted(sig['count'] for sig in sigs)
    comps = sorted(sig['components'] for sig in sigs)
    largest = sorted(sig['largest'] for sig in sigs)
    overlap_nodes = int(np.logical_and(fields[0] >= tau, fields[1] >= tau).sum())
    return {
        f'tau{str(tau).replace('.', 'p')}_count_min': counts[0],
        f'tau{str(tau).replace('.', 'p')}_count_max': counts[1],
        f'tau{str(tau).replace('.', 'p')}_components_min': comps[0],
        f'tau{str(tau).replace('.', 'p')}_components_max': comps[1],
        f'tau{str(tau).replace('.', 'p')}_largest_min': largest[0],
        f'tau{str(tau).replace('.', 'p')}_largest_max': largest[1],
        f'tau{str(tau).replace('.', 'p')}_overlap_nodes': overlap_nodes,
    }

def parse_config(config: str):
    side_s, c_ref_s = config.split(':', 1)
    side = int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)
    return side, float(c_ref_s)


def branch_metrics(name, fields, graph, params, grid_size, lambda_bar):
    u1, u2 = fields
    ec = EnergyComputer(graph, params)
    ec.normalize_weights(c=params.volume_fraction)
    e1, _ = ec.energy(u1)
    e2, _ = ec.energy(u2)
    overlap = float(np.dot(u1, u2))
    simplex = np.maximum(0, u1 + u2 - 1)
    bar = lambda_bar * float(np.dot(simplex, simplex))
    e0 = float(e1 + e2 + bar)
    c1 = center_of_mass(u1, grid_size)
    c2 = center_of_mass(u2, grid_size)
    mid = ((c1[0]+c2[0])/2, (c1[1]+c2[1])/2)
    gmid = ((grid_size-1)/2, (grid_size-1)/2)
    center_offset = float(np.hypot(mid[0]-gmid[0], mid[1]-gmid[1]) / max(grid_size-1, 1))
    sep = float(np.hypot(c2[0]-c1[0], c2[1]-c1[1]))
    if center_offset < 0.08:
        btype = 'Type A candidate'
    elif center_offset >= 0.12:
        btype = 'Type B candidate'
    else:
        btype = 'Mixed/ambiguous'
    out = {
        'branch': name,
        'E0': e0,
        'self1': float(e1),
        'self2': float(e2),
        'overlap': overlap,
        'simplex_penalty': bar,
        'center_offset_norm': center_offset,
        'separation': sep,
        'branch_type': btype,
        'regime_at_zero': classify_regime(fields, graph, params, lambda_rep=0, method='lambda'),
    }
    out.update(_pair_signature(fields, graph, 0.1))
    out.update(_pair_signature(fields, graph, 0.2))
    return out


def threshold_between(a, b):
    # Solve E0_a + l R_a = E0_b + l R_b.
    denom = a['overlap'] - b['overlap']
    if abs(denom) < 1e-12:
        return None
    return float((b['E0'] - a['E0']) / denom)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='10x10:0.6')
    ap.add_argument('--branch-lambdas', nargs='+', type=float, default=[0.0, 1.0])
    ap.add_argument('--eval-lambdas', nargs='+', type=float, default=[0, 0.01, 0.05, 0.1, 0.5, 1, 5])
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--n-restarts', type=int, default=3)
    ap.add_argument('--max-iter', type=int, default=500)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp72_frozen_branch_threshold.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp72_frozen_branch_threshold.csv')
    args = ap.parse_args()

    side, c_ref = parse_config(args.config)
    graph = GraphState.grid_2d(side, side)
    params = ParameterRegistry(volume_fraction=c_ref / 2, n_restarts=args.n_restarts, max_iter=args.max_iter)

    branches = []
    for blam in args.branch_lambdas:
        results = find_k_formations(graph, params, K=2, lambda_rep=blam, lambda_bar=args.lambda_bar,
                                    n_restarts=args.n_restarts, max_iter=args.max_iter)
        fields = [r.u.copy() for r in results]
        metrics = branch_metrics(f'branch_from_lambda_{blam:g}', fields, graph, params, side, args.lambda_bar)
        metrics['source_lambda'] = blam
        branches.append(metrics)

    rows = []
    for b in branches:
        for lam in args.eval_lambdas:
            rows.append({
                'branch': b['branch'],
                'source_lambda': b['source_lambda'],
                'eval_lambda': lam,
                'E_lambda': b['E0'] + lam * b['overlap'],
                'E0': b['E0'],
                'overlap': b['overlap'],
                'center_offset_norm': b['center_offset_norm'],
                'separation': b['separation'],
                'branch_type': b['branch_type'],
            })

    thresholds = []
    for i in range(len(branches)):
        for j in range(i+1, len(branches)):
            thresholds.append({
                'a': branches[i]['branch'],
                'b': branches[j]['branch'],
                'lambda_cross': threshold_between(branches[i], branches[j]),
                'E0_a': branches[i]['E0'],
                'E0_b': branches[j]['E0'],
                'overlap_a': branches[i]['overlap'],
                'overlap_b': branches[j]['overlap'],
            })

    out = {'experiment': 'exp72_frozen_branch_threshold', 'config': args.config, 'branches': branches, 'rows': rows, 'thresholds': thresholds}
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)
    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV: {args.output_csv}")
    print('Branches:')
    for b in branches:
        print(f"  {b['branch']}: E0={b['E0']:.6f} overlap={b['overlap']:.6f} type={b['branch_type']} center={b['center_offset_norm']:.3f}")
    print('Thresholds:')
    for t in thresholds:
        print(t)


if __name__ == '__main__':
    main()
