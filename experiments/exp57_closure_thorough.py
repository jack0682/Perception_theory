#!/usr/bin/env python3
"""Experiment 57: Thorough Closure Role Investigation.

Fixes the methodological issue in exp54: gradient projection g - mean(g)
implicitly preserves per-formation mass. This experiment uses RAW gradients
without mean subtraction, allowing genuine mass transfer between formations.

Three modes:
  A) Raw gradient (no projection, no mass constraint)
  B) Single-field: merge all K fields into one, run single gradient flow
  C) Coupled gradient: K fields share a single gradient flow on the product space

Tests on multiple grid sizes: 8x8, 10x10, 15x15.
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume


def evolve_raw_gradient(graph, params, K, total_mass, max_iter=3000,
                         record_interval=20, rng=None):
    """K-field evolution with RAW gradient — no mean subtraction, no mass constraint.
    Mass is free to redistribute between formations AND total mass can change.
    Only clipping [0,1] applied.
    """
    if rng is None:
        rng = np.random.RandomState(42)
    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    m_k = total_mass / K

    side = int(np.sqrt(n))
    fields = []
    for k in range(K):
        u = np.zeros(n)
        cx, cy = side * (k + 0.5) / K, side / 2
        for i in range(side):
            for j in range(side):
                idx = i * side + j
                if idx < n:
                    u[idx] = np.exp(-((i-cx)**2 + (j-cy)**2) / max((side/K)**2, 1.0))
        fields.append(project_volume(u, m_k))

    dt = 0.005
    history = []

    for tau in range(1, max_iter + 1):
        if tau == 1 or tau % record_interval == 0 or tau == max_iter:
            peaks = [float(np.max(f)) for f in fields]
            masses = [float(np.sum(f)) for f in fields]
            cores = [int(np.sum(f > 0.5)) for f in fields]
            alive = sum(1 for p in peaks if p > 0.3)
            total_m = sum(masses)
            e_total = sum(float(ec.energy(f)[0]) for f in fields)
            history.append({
                'iter': tau, 'alive': alive, 'energy': e_total,
                'peaks': peaks, 'masses': masses, 'cores': cores,
                'total_mass': total_m,
            })

        new_fields = []
        for k in range(K):
            g = ec.gradient(fields[k])  # RAW gradient, no projection!
            u_new = fields[k] - dt * g
            u_new = np.clip(u_new, 0.0, 1.0)  # only clip, no mass conservation
            new_fields.append(u_new)
        fields = new_fields

    return history, fields


def evolve_single_field_multi_init(graph, params, K, total_mass, max_iter=3000,
                                    record_interval=20, rng=None):
    """Start with K bumps in a SINGLE field, run single-field gradient flow.
    This is the most direct test: if K bumps merge into 1, closure doesn't help.
    """
    if rng is None:
        rng = np.random.RandomState(42)
    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    side = int(np.sqrt(n))
    u = np.zeros(n)
    for k in range(K):
        cx, cy = side * (k + 0.5) / K, side / 2
        for i in range(side):
            for j in range(side):
                idx = i * side + j
                if idx < n:
                    u[idx] += np.exp(-((i-cx)**2 + (j-cy)**2) / max((side/K)**2, 1.0))
    u = np.clip(u, 0, 1)
    u = project_volume(u, total_mass)

    dt = 0.01
    prev_gnorm = float('inf')
    history = []

    for tau in range(1, max_iter + 1):
        if tau == 1 or tau % record_interval == 0 or tau == max_iter:
            # Count formations in single field
            K_count = count_formations(u, graph, 0.3)
            peak = float(np.max(u))
            e = float(ec.energy(u)[0])
            mass = float(np.sum(u))
            history.append({
                'iter': tau, 'K': K_count, 'peak': peak, 'energy': e, 'mass': mass,
            })

        g = ec.gradient(u)
        g_sigma = g - np.mean(g)  # project to preserve total mass
        gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
        u = u - dt * g_sigma
        u = project_volume(u, total_mass)

        if gnorm > prev_gnorm * 1.5 and tau > 5:
            dt = max(dt * 0.7, 1e-8)
        elif gnorm < prev_gnorm * 0.95:
            dt = min(dt * 1.05, 0.1)
        prev_gnorm = gnorm
        if tau > 200 and gnorm < 1e-5:
            break

    return history, u


def count_formations(u, graph, theta=0.3):
    """Count connected components of superlevel set."""
    n = len(u)
    above = u >= theta
    if not np.any(above):
        return 0
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    adj = (W > 0)
    visited = np.zeros(n, dtype=bool)
    components = 0
    for start in range(n):
        if above[start] and not visited[start]:
            components += 1
            queue = [start]
            visited[start] = True
            while queue:
                node = queue.pop(0)
                for nb in range(n):
                    if adj[node, nb] and above[nb] and not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
    return components


def main():
    print("Experiment 57: Thorough Closure Role Investigation")
    print("=" * 70)
    t0 = time.time()

    all_results = []

    grid_sizes = [8, 10, 15]
    a_cl_values = [3.0, 1.5, 0.5, 0.0]
    K = 4

    # === Mode A: Raw gradient, K separate fields ===
    print("\n=== MODE A: Raw Gradient (no mass conservation) ===")
    print(f"{'grid':>6} {'a_cl':>5} {'K_final':>7} {'peaks':>25} {'masses':>25}")

    for side in grid_sizes:
        grid = GraphState.grid_2d(side, side)
        n = grid.n
        total_mass = 0.25 * n * K

        for a_cl in a_cl_values:
            params = ParameterRegistry(a_cl=max(a_cl, 0.01), beta_bd=20.0, volume_fraction=0.25)
            history, fields = evolve_raw_gradient(
                grid, params, K=K, total_mass=total_mass,
                max_iter=3000, rng=np.random.RandomState(42),
            )
            final = history[-1]
            pk = ','.join(f'{p:.2f}' for p in final['peaks'])
            ms = ','.join(f'{m:.0f}' for m in final['masses'])
            print(f"{side}x{side:>2} {a_cl:5.1f} {final['alive']:>7} {pk:>25} {ms:>25}")

            all_results.append({
                'mode': 'A_raw', 'grid': f'{side}x{side}', 'n': n,
                'a_cl': a_cl, 'K_init': K,
                'K_final': final['alive'],
                'peaks': final['peaks'], 'masses': final['masses'],
                'total_mass_final': final['total_mass'],
                'history': history,
            })

    # === Mode B: Single field with K initial bumps ===
    print("\n=== MODE B: Single Field (K bumps → gradient flow → count formations) ===")
    print(f"{'grid':>6} {'a_cl':>5} {'K_final':>7} {'peak':>6} {'mass':>6}")

    for side in grid_sizes:
        grid = GraphState.grid_2d(side, side)
        n = grid.n
        total_mass = 0.30 * n

        for a_cl in a_cl_values:
            params = ParameterRegistry(a_cl=max(a_cl, 0.01), beta_bd=20.0, volume_fraction=0.30)
            history, u = evolve_single_field_multi_init(
                grid, params, K=K, total_mass=total_mass,
                max_iter=3000, rng=np.random.RandomState(42),
            )
            final = history[-1]
            print(f"{side}x{side:>2} {a_cl:5.1f} {final['K']:>7} {final['peak']:6.2f} {final['mass']:6.0f}")

            # Track K(t) trajectory
            k_traj = [h['K'] for h in history]
            all_results.append({
                'mode': 'B_single', 'grid': f'{side}x{side}', 'n': n,
                'a_cl': a_cl, 'K_init': K,
                'K_final': final['K'], 'peak': final['peak'],
                'K_trajectory': k_traj,
                'history': history,
            })

    # Summary
    print(f"\n{'='*70}")
    print(f"THOROUGH CLOSURE INVESTIGATION SUMMARY")
    print(f"{'='*70}")

    print(f"\nMode A (Raw gradient, K fields):")
    for r in all_results:
        if r['mode'] == 'A_raw':
            print(f"  {r['grid']} a_cl={r['a_cl']:.1f}: K_final={r['K_final']}, "
                  f"total_mass={r.get('total_mass_final', '?'):.0f} (init={0.25*r['n']*K:.0f})")

    print(f"\nMode B (Single field, K bumps):")
    for r in all_results:
        if r['mode'] == 'B_single':
            k_traj = r.get('K_trajectory', [])
            print(f"  {r['grid']} a_cl={r['a_cl']:.1f}: K trajectory = {k_traj[0]} → {k_traj[-1]}")

    # The key comparison: does closure affect K-survival?
    print(f"\n=== KEY COMPARISON: Does closure affect formation count? ===")
    for side in grid_sizes:
        for mode in ['A_raw', 'B_single']:
            with_cl = [r for r in all_results if r['mode']==mode and r['grid']==f'{side}x{side}' and r['a_cl']==3.0]
            no_cl = [r for r in all_results if r['mode']==mode and r['grid']==f'{side}x{side}' and r['a_cl']==0.0]
            if with_cl and no_cl:
                kf = 'K_final' if 'K_final' in with_cl[0] else 'K'
                print(f"  {side}x{side} {mode}: a_cl=3.0 → K={with_cl[0].get(kf, with_cl[0].get('K_final'))}, "
                      f"a_cl=0.0 → K={no_cl[0].get(kf, no_cl[0].get('K_final'))}")

    output = {
        'experiment': 'exp57_closure_thorough',
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp57_closure_thorough.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}, time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
