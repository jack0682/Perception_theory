#!/usr/bin/env python3
"""Exp68: NEB-lite projected path relaxation for relaxed merge paths.

Starts from an exp67 direct relaxed interpolation path and relaxes intermediate
images by projected gradient descent on the relaxed total-mass manifold R_M^2.
This is a communication-height scaffold, not a rigorous MEP solver.
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
from scc.optimizer import find_formation
from experiments.exp67_relaxed_merge_paths import direct_path, path_stats, total_energy_relaxed


def project_relaxed_pair(u1: np.ndarray, u2: np.ndarray, total_mass: float, n_iter: int = 20):
    """Heuristic projection to R_M^2: 0<=uk<=1, u1+u2<=1, sum(u1+u2)=M."""
    u1 = np.clip(u1.copy(), 0.0, 1.0)
    u2 = np.clip(u2.copy(), 0.0, 1.0)
    for _ in range(n_iter):
        s = u1 + u2
        over = s > 1.0
        if np.any(over):
            scale = np.ones_like(s)
            scale[over] = 1.0 / (s[over] + 1e-12)
            u1 *= scale
            u2 *= scale
        mass = float(np.sum(u1 + u2))
        diff = total_mass - mass
        if abs(diff) < 1e-10:
            break
        cap = np.maximum(0.0, 1.0 - (u1 + u2)) if diff > 0 else (u1 + u2)
        cap_sum = float(np.sum(cap))
        if cap_sum < 1e-12:
            break
        delta = diff * cap / cap_sum
        if diff > 0:
            # add to component with lower occupancy to avoid immediate simplex violation
            choose1 = u1 <= u2
            d1 = np.where(choose1, delta, 0.0)
            d2 = np.where(~choose1, delta, 0.0)
            u1 += d1
            u2 += d2
        else:
            frac1 = np.divide(u1, u1 + u2 + 1e-12)
            u1 += delta * frac1
            u2 += delta * (1.0 - frac1)
        u1 = np.clip(u1, 0.0, 1.0)
        u2 = np.clip(u2, 0.0, 1.0)
    return u1, u2


def relaxed_gradient_pair(u1, u2, ec: EnergyComputer, lambda_rep: float, lambda_bar: float):
    g1 = ec.gradient(u1) + lambda_rep * u2
    g2 = ec.gradient(u2) + lambda_rep * u1
    s = u1 + u2
    viol = np.maximum(0.0, s - 1.0)
    if lambda_bar:
        g1 = g1 + 2.0 * lambda_bar * viol
        g2 = g2 + 2.0 * lambda_bar * viol
    # project out total-mass direction over both components
    mean = (np.sum(g1) + np.sum(g2)) / (2 * len(u1))
    return g1 - mean, g2 - mean


def path_constraint_diagnostics(images, total_mass: float) -> dict:
    """Return max constraint violations over a path in R_M^2."""
    max_box_low = 0.0
    max_box_high = 0.0
    max_simplex = 0.0
    max_mass_error = 0.0
    for u1, u2 in images:
        max_box_low = max(max_box_low, float(max(0.0, -np.min(u1), -np.min(u2))))
        max_box_high = max(max_box_high, float(max(0.0, np.max(u1) - 1.0, np.max(u2) - 1.0)))
        max_simplex = max(max_simplex, float(np.max(np.maximum(0.0, u1 + u2 - 1.0))))
        max_mass_error = max(max_mass_error, abs(float(np.sum(u1 + u2) - total_mass)))
    return {
        'max_box_low_violation': max_box_low,
        'max_box_high_violation': max_box_high,
        'max_simplex_violation': max_simplex,
        'max_total_mass_error': max_mass_error,
    }


def history_diagnostics(history: list[dict]) -> dict:
    """Summarize monotonicity of recorded max-delta history."""
    vals = [float(h['max_delta']) for h in history]
    if len(vals) < 2:
        return {'history_points': len(vals), 'monotone_nonincreasing': True, 'max_increase': 0.0}
    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    return {
        'history_points': len(vals),
        'monotone_nonincreasing': all(d <= 1e-9 for d in diffs),
        'max_increase': float(max(diffs)),
        'initial_recorded_max_delta': vals[0],
        'final_recorded_max_delta': vals[-1],
    }


def smooth_path(images, spring: float):
    out = [images[0]]
    for i in range(1, len(images)-1):
        u1, u2 = images[i]
        p1, p2 = images[i-1]
        n1, n2 = images[i+1]
        lap1 = 2*u1 - p1 - n1
        lap2 = 2*u2 - p2 - n2
        out.append((lap1, lap2))
    out.append(images[-1])
    return out


def relax_images(images, ec, lambda_rep, lambda_bar, total_mass, source_energy, n_iter, step, spring):
    images = [(a.copy(), b.copy()) for a, b in images]
    history = []
    for it in range(n_iter):
        springs = smooth_path(images, spring)
        new_images = [images[0]]
        for i in range(1, len(images)-1):
            u1, u2 = images[i]
            g1, g2 = relaxed_gradient_pair(u1, u2, ec, lambda_rep, lambda_bar)
            sg1, sg2 = springs[i]
            v1 = u1 - step * (g1 + spring * sg1)
            v2 = u2 - step * (g2 + spring * sg2)
            new_images.append(project_relaxed_pair(v1, v2, total_mass))
        new_images.append(images[-1])
        images = new_images
        if it % 10 == 0 or it == n_iter - 1:
            stats = path_stats('relaxed', images, ec, lambda_rep, lambda_bar, source_energy)
            history.append({'iter': it, 'max_delta': stats['max_delta'], 'max_total': stats['max_total']})
    return images, history


def run(config, lambda_rep, lambda_bar, n_images, n_iter, step, spring, n_restarts, max_iter):
    side_s, c_ref_s = config.split(':', 1)
    side = int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)
    c_ref = float(c_ref_s)
    n = side * side
    half_c = c_ref / 2.0
    total_mass = c_ref * n
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
    source_energy = total_energy_relaxed((u1,u2), ec, lambda_rep, lambda_bar)['total']
    initial = direct_path(u1, u2, u_merge, n_images)
    initial_stats = path_stats('direct_initial', initial, ec, lambda_rep, lambda_bar, source_energy)
    relaxed, history = relax_images(initial, ec, lambda_rep, lambda_bar, total_mass, source_energy, n_iter, step, spring)
    relaxed_stats = path_stats('neb_lite_relaxed', relaxed, ec, lambda_rep, lambda_bar, source_energy)
    initial_constraints = path_constraint_diagnostics(initial, total_mass)
    relaxed_constraints = path_constraint_diagnostics(relaxed, total_mass)
    hist_diag = history_diagnostics(history)
    return {
        'experiment': 'exp68_relaxed_merge_neb_lite',
        'config': config,
        'lambda_rep': lambda_rep,
        'lambda_bar': lambda_bar,
        'n_images': n_images,
        'n_iter': n_iter,
        'step': step,
        'spring': spring,
        'source_energy': source_energy,
        'initial': initial_stats,
        'relaxed': relaxed_stats,
        'history': history,
        'diagnostics': {
            'initial_constraints': initial_constraints,
            'relaxed_constraints': relaxed_constraints,
            'history': hist_diag,
            'improvement': float(initial_stats['max_delta'] - relaxed_stats['max_delta']),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='10x10:0.6')
    ap.add_argument('--lambda-rep', type=float, default=1.0)
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--n-images', type=int, default=11)
    ap.add_argument('--n-iter', type=int, default=80)
    ap.add_argument('--step', type=float, default=0.002)
    ap.add_argument('--spring', type=float, default=0.1)
    ap.add_argument('--n-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--output', type=Path, default=REPO_ROOT / 'experiments/results/exp68_relaxed_merge_neb_lite.json')
    args = ap.parse_args()
    result = run(args.config, args.lambda_rep, args.lambda_bar, args.n_images, args.n_iter, args.step, args.spring, args.n_restarts, args.max_iter)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2))
    print(f"Saved: {args.output}")
    print(f"initial max_delta={result['initial']['max_delta']:.6f}")
    print(f"relaxed max_delta={result['relaxed']['max_delta']:.6f}")
    print(f"improvement={result['diagnostics']['improvement']:.6f}")
    print(f"relaxed max_mass_error={result['diagnostics']['relaxed_constraints']['max_total_mass_error']:.3e}")
    print(f"relaxed max_simplex_violation={result['diagnostics']['relaxed_constraints']['max_simplex_violation']:.3e}")
    print(f"history monotone={result['diagnostics']['history']['monotone_nonincreasing']}")


if __name__ == '__main__':
    main()
