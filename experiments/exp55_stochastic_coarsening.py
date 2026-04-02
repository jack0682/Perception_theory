#!/usr/bin/env python3
"""Experiment 55: Stochastic Coarsening — SCC vs Allen-Cahn.

Adds noise to gradient descent to enable barrier crossing.
Compares:
  - SCC (a_cl=3.0): enhanced metastability from closure
  - Allen-Cahn (a_cl=0): no closure, only double-well

Measures:
  - Time to first merge event (K → K-1)
  - Coarsening trajectory K(t)
  - Barrier crossing frequency
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume


def evolve_stochastic(graph, params, K, total_mass, noise_std, max_iter=5000,
                       record_interval=25, rng=None):
    """Langevin-like dynamics: gradient descent + noise."""
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

    dt = 0.005  # smaller dt for stability with noise
    history = []
    merge_threshold = 0.3  # peak below this = dead

    for tau in range(1, max_iter + 1):
        if tau == 1 or tau % record_interval == 0:
            peaks = [float(np.max(f)) for f in fields]
            masses = [float(np.sum(f)) for f in fields]
            alive = sum(1 for p in peaks if p > merge_threshold)
            e_total = sum(float(ec.energy(f)[0]) for f in fields)

            # Check for merges (high overlap between any pair)
            overlaps = []
            for j in range(K):
                for ki in range(j+1, K):
                    ov = float(np.sum(np.minimum(fields[j], fields[ki])))
                    overlaps.append(ov)
            max_overlap = max(overlaps) if overlaps else 0

            history.append({
                'iter': tau, 'alive': alive, 'energy': e_total,
                'peaks': peaks, 'masses': masses,
                'max_overlap': max_overlap,
            })

        # Gradient + noise
        new_fields = []
        for k in range(K):
            g = ec.gradient(fields[k])
            g_sigma = g - np.mean(g)
            noise = noise_std * rng.randn(n)
            u_new = fields[k] - dt * g_sigma + np.sqrt(dt) * noise
            u_new = np.clip(u_new, 0.0, 1.0)
            new_fields.append(u_new)

        # Shared mass
        total_now = sum(float(np.sum(f)) for f in new_fields)
        if total_now > 1e-10:
            scale = total_mass / total_now
            new_fields = [np.clip(f * scale, 0.0, 1.0) for f in new_fields]
        fields = new_fields

    return history


def main():
    print("Experiment 55: Stochastic Coarsening (SCC vs Allen-Cahn)")
    print("=" * 70)
    t0 = time.time()

    grid = GraphState.grid_2d(10, 10)
    n = grid.n
    K = 4
    total_mass = 0.25 * n * K

    noise_levels = [0.01, 0.05, 0.1, 0.2, 0.5]
    all_results = []

    for noise in noise_levels:
        print(f"\n--- noise_std = {noise} ---")

        for label, a_cl in [('SCC', 3.0), ('AC', 0.01)]:
            params = ParameterRegistry(a_cl=a_cl, beta_bd=20.0, volume_fraction=0.25)

            history = evolve_stochastic(
                grid, params, K=K, total_mass=total_mass,
                noise_std=noise, max_iter=5000, record_interval=50,
                rng=np.random.RandomState(42),
            )

            alive_seq = [h['alive'] for h in history]
            first_death = None
            for i, h in enumerate(history):
                if h['alive'] < K:
                    first_death = h['iter']
                    break

            final_K = alive_seq[-1]
            print(f"  {label:>3}: K_final={final_K}, first_death={'iter '+str(first_death) if first_death else 'NONE'}, "
                  f"E_final={history[-1]['energy']:.1f}")

            all_results.append({
                'noise': noise, 'model': label, 'a_cl': a_cl,
                'K_final': final_K, 'first_death_iter': first_death,
                'alive_trajectory': alive_seq,
                'history': history,
            })

    # Summary
    print(f"\n{'='*70}")
    print(f"STOCHASTIC COARSENING SUMMARY")
    print(f"{'='*70}")
    print(f"{'noise':>6} {'model':>5} {'K_final':>7} {'first_death':>12} {'coarsening':>12}")
    for r in all_results:
        fd = str(r['first_death_iter']) if r['first_death_iter'] else 'NEVER'
        coarsen = f"K={K}→{r['K_final']}" if r['K_final'] < K else 'NONE'
        print(f"{r['noise']:6.2f} {r['model']:>5} {r['K_final']:>7} {fd:>12} {coarsen:>12}")

    # SCC vs AC comparison
    print(f"\nSCC vs AC comparison:")
    for noise in noise_levels:
        scc = [r for r in all_results if r['noise'] == noise and r['model'] == 'SCC'][0]
        ac = [r for r in all_results if r['noise'] == noise and r['model'] == 'AC'][0]
        scc_fd = scc['first_death_iter'] or float('inf')
        ac_fd = ac['first_death_iter'] or float('inf')
        ratio = scc_fd / ac_fd if ac_fd < float('inf') else ('SCC=inf' if scc_fd == float('inf') else f'AC=inf')
        print(f"  noise={noise:.2f}: SCC death@{scc_fd}, AC death@{ac_fd}, ratio={ratio}")

    output = {
        'experiment': 'exp55_stochastic_coarsening',
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp55_stochastic_coarsening.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}, time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
