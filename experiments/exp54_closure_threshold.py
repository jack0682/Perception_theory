#!/usr/bin/env python3
"""Experiment 54: Closure Strength Critical Threshold.

Sweeps a_cl from 3.5 down to 0 under L4 constraints (shared mass, no rep, no simplex).
Finds the critical a_cl* where multi-formation collapses.

Also compares: with vs without closure (SCC vs pure Allen-Cahn).
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume


def evolve_shared_mass(graph, params, K, total_mass, max_iter=2000, noise_std=0.0, rng=None):
    """Gradient descent with shared total mass, no repulsion, no simplex."""
    if rng is None:
        rng = np.random.RandomState(42)
    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    m_k = total_mass / K

    # Clustered init
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

    dt = 0.01
    prev_gnorm = float('inf')
    history = []

    for tau in range(1, max_iter + 1):
        if tau == 1 or tau % 50 == 0 or tau == max_iter:
            peaks = [float(np.max(f)) for f in fields]
            masses = [float(np.sum(f)) for f in fields]
            cores = [int(np.sum(f > 0.5)) for f in fields]
            alive = sum(1 for p in peaks if p > 0.3)
            e_total = sum(float(ec.energy(f)[0]) for f in fields)
            history.append({
                'iter': tau, 'alive': alive, 'energy': e_total,
                'peaks': peaks, 'masses': masses, 'cores': cores,
            })

        max_gnorm = 0.0
        new_fields = []
        for k in range(K):
            g = ec.gradient(fields[k])
            g_sigma = g - np.mean(g)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)
            u_new = fields[k] - dt * g_sigma
            if noise_std > 0:
                u_new += noise_std * rng.randn(n)
            u_new = np.clip(u_new, 0.0, 1.0)
            new_fields.append(u_new)

        # Shared mass rescaling
        total_now = sum(float(np.sum(f)) for f in new_fields)
        if total_now > 1e-10:
            scale = total_mass / total_now
            new_fields = [np.clip(f * scale, 0.0, 1.0) for f in new_fields]
        fields = new_fields

        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt = max(dt * 0.7, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt = min(dt * 1.05, 0.1)
        prev_gnorm = max_gnorm

        if tau > 100 and max_gnorm < 1e-5:
            break

    return history, fields


def main():
    print("Experiment 54: Closure Strength Critical Threshold")
    print("=" * 70)
    t0 = time.time()

    grid = GraphState.grid_2d(10, 10)
    n = grid.n
    K = 4
    total_mass = 0.25 * n * K
    all_results = []

    # Sweep a_cl from 3.5 down to 0
    a_cl_values = [3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.1, 0.0]

    print(f"\n{'a_cl':>5} {'K_final':>7} {'peaks':>30} {'E':>8}")
    print(f"{'-'*60}")

    for a_cl in a_cl_values:
        params = ParameterRegistry(
            a_cl=min(a_cl, 3.99),  # must be < 4
            beta_bd=20.0,
            volume_fraction=0.25,
        )

        history, fields = evolve_shared_mass(
            grid, params, K=K, total_mass=total_mass,
            max_iter=2000, rng=np.random.RandomState(42),
        )

        final = history[-1]
        peaks_str = ','.join(f'{p:.2f}' for p in final['peaks'])
        print(f"{a_cl:5.1f} {final['alive']:>7} {peaks_str:>30} {final['energy']:8.1f}")

        all_results.append({
            'a_cl': a_cl, 'K_final': final['alive'],
            'peaks': final['peaks'], 'masses': final['masses'],
            'cores': final['cores'], 'energy': final['energy'],
            'history': history,
        })

    # Also test with different beta
    print(f"\n--- Beta sweep at a_cl=0 (pure Allen-Cahn) ---")
    for beta in [10, 20, 40, 80]:
        params = ParameterRegistry(a_cl=0.01, beta_bd=float(beta), volume_fraction=0.25)
        history, fields = evolve_shared_mass(
            grid, params, K=K, total_mass=total_mass,
            max_iter=2000, rng=np.random.RandomState(42),
        )
        final = history[-1]
        peaks_str = ','.join(f'{p:.2f}' for p in final['peaks'])
        print(f"  beta={beta:3d} K_final={final['alive']} peaks=[{peaks_str}]")
        all_results.append({
            'a_cl': 0.01, 'beta': beta, 'K_final': final['alive'],
            'peaks': final['peaks'], 'label': f'AC_beta{beta}',
            'history': history,
        })

    # Find critical threshold
    print(f"\n--- Critical threshold analysis ---")
    for r in all_results:
        if 'label' not in r:
            status = "ALIVE" if r['K_final'] >= K else f"DEAD(K={r['K_final']})"
            print(f"  a_cl={r['a_cl']:.1f}: {status}")

    output = {
        'experiment': 'exp54_closure_threshold',
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp54_closure_threshold.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}, time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
