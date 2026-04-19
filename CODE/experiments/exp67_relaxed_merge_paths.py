#!/usr/bin/env python3
"""Exp67: relaxed merge path communication-height scaffold.

Compares path-specific energy maxima for a selected K=2 branch:

1. direct relaxed interpolation from (u1,u2) to (u_merge,0)
2. diffuse shortcut: soften/spread u2, transfer its mass into u1, then
   reconcentrate toward the K=1 target

This is evidence for R4: communication height depends on path class.  It is
not a theorem proof and must not be used as a category upgrade.
"""

from __future__ import annotations

import argparse
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
from scc.optimizer import find_formation, project_volume


def total_energy_relaxed(fields, ec: EnergyComputer, lambda_rep: float, lambda_bar: float) -> dict:
    u1, u2 = fields
    e1, t1 = ec.energy(u1)
    e2, t2 = ec.energy(u2)
    rep = lambda_rep * float(np.dot(u1, u2))
    violation = np.maximum(0.0, u1 + u2 - 1.0)
    bar = lambda_bar * float(np.dot(violation, violation))
    total = e1 + e2 + rep + bar
    return {
        'total': float(total),
        'self1': float(e1),
        'self2': float(e2),
        'rep': float(rep),
        'barrier': float(bar),
        'bd1': float(t1.get('E_bd', 0.0)),
        'bd2': float(t2.get('E_bd', 0.0)),
    }


def uniform_field(n: int, mass: float) -> np.ndarray:
    return np.full(n, mass / n)


def path_stats(name: str, points, ec, lambda_rep, lambda_bar, source_energy):
    rows = []
    for i, fields in enumerate(points):
        terms = total_energy_relaxed(fields, ec, lambda_rep, lambda_bar)
        rows.append({'i': i, **terms, 'overlap': float(np.dot(fields[0], fields[1])), 'delta': terms['total'] - source_energy})
    max_row = max(rows, key=lambda r: r['total'])
    max_overlap_row = max(rows, key=lambda r: r['overlap'])
    source_overlap = rows[0]['overlap']
    max_overlap_excess = max(row['overlap'] - source_overlap for row in rows)
    return {
        'name': name,
        'n_points': len(rows),
        'max_total': max_row['total'],
        'max_delta': max_row['delta'],
        'max_index': max_row['i'],
        'source_overlap': source_overlap,
        'max_overlap': max_overlap_row['overlap'],
        'max_overlap_index': max_overlap_row['i'],
        'max_overlap_excess': max_overlap_excess,
        'rows': rows,
    }


def direct_path(u1, u2, u_merge, n_steps: int):
    pts = []
    zero = np.zeros_like(u2)
    for a in np.linspace(0.0, 1.0, n_steps):
        pts.append(((1-a)*u1 + a*u_merge, (1-a)*u2 + a*zero))
    return pts


def diffuse_shortcut_path(u1, u2, u_merge, n_steps: int):
    """Three-stage heuristic shortcut.

    Stage 1: diffuse u2 to uniform mass m2.
    Stage 2: transfer uniform u2 mass into u1_total while keeping u2 diffuse.
    Stage 3: reconcentrate u1 from u1+m2/n toward u_merge.
    """
    n = len(u1)
    m2 = float(np.sum(u2))
    u2_flat = uniform_field(n, m2)
    u1_plus_flat = np.clip(u1 + u2_flat, 0.0, 1.0)
    # Project total target mass into u1 component; relaxed path may otherwise
    # lose tiny mass numerically through clipping.
    u1_plus_flat = project_volume(u1_plus_flat, float(np.sum(u1) + m2))
    zero = np.zeros_like(u2)

    pts = []
    # Stage 1: soften/spread u2
    for a in np.linspace(0.0, 1.0, n_steps):
        pts.append((u1.copy(), (1-a)*u2 + a*u2_flat))
    # Stage 2: transfer diffuse mass to u1
    for a in np.linspace(0.0, 1.0, n_steps)[1:]:
        pts.append(((1-a)*u1 + a*u1_plus_flat, (1-a)*u2_flat + a*zero))
    # Stage 3: reconcentrate u1
    for a in np.linspace(0.0, 1.0, n_steps)[1:]:
        pts.append(((1-a)*u1_plus_flat + a*u_merge, zero.copy()))
    return pts


def sequential_zero_overlap_path(u1, u2, u_merge, n_steps: int):
    """Heuristic path that avoids simultaneous u1/u2 occupancy by sequencing.

    This path is intentionally restrictive and discontinuity-prone in branch
    identity: first remove u2 while adding its mass to currently low-u1 sites,
    then morph the single remaining field to u_merge with u2=0.  It tests
    whether low/zero overlap can coexist with low energy excess.
    """
    n = len(u1)
    total_mass = float(np.sum(u1) + np.sum(u2))
    zero = np.zeros_like(u2)
    # Reservoir: add u2 mass to the lowest u1 sites first.
    reservoir = np.zeros_like(u1)
    order = np.argsort(u1)
    remaining = float(np.sum(u2))
    for idx in order:
        add = min(1.0 - u1[idx], remaining)
        if add <= 0:
            continue
        reservoir[idx] = add
        remaining -= add
        if remaining <= 1e-12:
            break
    u1_loaded = project_volume(np.clip(u1 + reservoir, 0.0, 1.0), total_mass)

    pts = []
    # Stage 1: remove u2 while loading reservoir in u1.
    for a in np.linspace(0.0, 1.0, n_steps):
        v1 = (1-a)*u1 + a*u1_loaded
        v2 = (1-a)*u2
        pts.append((v1, v2))
    # Stage 2: with u2 gone, morph to target.
    for a in np.linspace(0.0, 1.0, n_steps)[1:]:
        v1 = (1-a)*u1_loaded + a*u_merge
        pts.append((v1, zero.copy()))
    return pts


def run(config: str, lambda_rep: float, lambda_bar: float, n_steps: int, n_restarts: int, max_iter: int):
    side_s, c_ref_s = config.split(':', 1)
    side = int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)
    c_ref = float(c_ref_s)
    n = side * side
    total_mass = c_ref * n
    half_c = c_ref / 2.0

    graph = GraphState.grid_2d(side, side)
    params_half = ParameterRegistry(volume_fraction=half_c, n_restarts=n_restarts, max_iter=max_iter)
    params_total = ParameterRegistry(volume_fraction=c_ref, n_restarts=n_restarts, max_iter=max_iter)

    k2 = find_k_formations(graph, params_half, K=2, lambda_rep=lambda_rep, lambda_bar=lambda_bar,
                           n_restarts=n_restarts, max_iter=max_iter)
    u1, u2 = k2[0].u, k2[1].u
    k1 = find_formation(graph, params_total, normalize=True, verbose=False)
    u_merge = k1.u

    ec = EnergyComputer(graph, params_half)
    ec.normalize_weights(c=half_c)
    src_terms = total_energy_relaxed((u1, u2), ec, lambda_rep, lambda_bar)
    source_energy = src_terms['total']

    paths = [
        path_stats('direct_relaxed_interpolation', direct_path(u1, u2, u_merge, n_steps), ec, lambda_rep, lambda_bar, source_energy),
        path_stats('diffuse_shortcut', diffuse_shortcut_path(u1, u2, u_merge, n_steps), ec, lambda_rep, lambda_bar, source_energy),
        path_stats('sequential_zero_overlap', sequential_zero_overlap_path(u1, u2, u_merge, n_steps), ec, lambda_rep, lambda_bar, source_energy),
    ]

    return {
        'experiment': 'exp67_relaxed_merge_paths',
        'config': config,
        'n': n,
        'lambda_rep': lambda_rep,
        'lambda_bar': lambda_bar,
        'n_steps': n_steps,
        'n_restarts': n_restarts,
        'max_iter': max_iter,
        'source_energy': source_energy,
        'source_terms': src_terms,
        'target_self_energy': float(k1.energy),
        'masses': {'u1': float(np.sum(u1)), 'u2': float(np.sum(u2)), 'target': float(np.sum(u_merge))},
        'paths': paths,
    }


def main():
    parser = argparse.ArgumentParser(description='Exp67 relaxed merge path comparison')
    parser.add_argument('--config', default='10x10:0.6')
    parser.add_argument('--lambda-rep', type=float, default=1.0)
    parser.add_argument('--lambda-bar', type=float, default=100.0)
    parser.add_argument('--n-steps', type=int, default=21)
    parser.add_argument('--n-restarts', type=int, default=2)
    parser.add_argument('--max-iter', type=int, default=800)
    parser.add_argument('--output', type=Path, default=REPO_ROOT / 'experiments/results/exp67_relaxed_merge_paths.json')
    args = parser.parse_args()

    result = run(args.config, args.lambda_rep, args.lambda_bar, args.n_steps, args.n_restarts, args.max_iter)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    print(f"Saved: {args.output}")
    print(f"Source energy: {result['source_energy']:.6f}")
    for p in result['paths']:
        print(f"{p['name']}: max_delta={p['max_delta']:.6f} max_overlap={p['max_overlap']:.6f} overlap_excess={p['max_overlap_excess']:.6f} at index {p['max_index']}")


if __name__ == '__main__':
    main()
