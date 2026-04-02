#!/usr/bin/env python3
"""Experiment 56: Formation Nucleation from Random Initial Conditions.

Tests MK-1: K_nucleation from random IC = K_eigengap.

Method:
  1. Create graph (grid, SBM, barbell)
  2. Initialize with random field
  3. Run gradient flow to convergence
  4. Count number of distinct formations
  5. Compare with K_eigengap prediction

Multiple random seeds for statistics.
"""
import sys, os, json, time
import numpy as np
from scipy import sparse as sp
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume, find_formation
from scc.multi import spectral_k_estimate


def count_formations(u, graph, theta=0.3):
    """Count distinct formations via connected components of superlevel set."""
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
            # BFS
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


def evolve_single_field(graph, params, total_mass, max_iter=3000, rng=None):
    """Run gradient flow on a SINGLE field (not K-field) from random IC."""
    if rng is None:
        rng = np.random.RandomState(42)
    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    # Random initialization
    u = rng.rand(n) * 0.3 + 0.05
    u = project_volume(u, total_mass)

    dt = 0.01
    prev_gnorm = float('inf')

    history = []
    for tau in range(1, max_iter + 1):
        if tau == 1 or tau % 100 == 0 or tau == max_iter:
            K = count_formations(u, graph, theta=0.3)
            peak = float(np.max(u))
            e = float(ec.energy(u)[0])
            history.append({'iter': tau, 'K': K, 'peak': peak, 'energy': e})

        g = ec.gradient(u)
        g_sigma = g - np.mean(g)
        gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))

        u = u - dt * g_sigma
        u = project_volume(u, total_mass)

        if gnorm > prev_gnorm * 1.5 and tau > 5:
            dt = max(dt * 0.7, 1e-8)
        elif gnorm < prev_gnorm * 0.95:
            dt = min(dt * 1.05, 0.1)
        prev_gnorm = gnorm

        if tau > 200 and gnorm < 1e-5:
            K = count_formations(u, graph, theta=0.3)
            history.append({'iter': tau, 'K': K, 'peak': float(np.max(u)),
                            'energy': float(ec.energy(u)[0]), 'converged': True})
            break

    return history, u


def make_barbell(n_side, bridge_weight):
    g1 = GraphState.grid_2d(n_side, n_side)
    n1 = g1.n
    W = np.zeros((2*n1, 2*n1))
    W[:n1, :n1] = g1.W.toarray()
    W[n1:, n1:] = g1.W.toarray()
    W[n1-n_side//2, n1+n_side//2] = bridge_weight
    W[n1+n_side//2, n1-n_side//2] = bridge_weight
    return GraphState(sp.csr_matrix(W))


def make_sbm(sizes, p_in=0.3, p_out=0.005, rng=None):
    if rng is None:
        rng = np.random.RandomState(99)
    n = sum(sizes)
    W = np.zeros((n, n))
    for i, si in enumerate(sizes):
        for j, sj in enumerate(sizes):
            p = p_in if i == j else p_out
            ri, rj = sum(sizes[:i]), sum(sizes[:j])
            W[ri:ri+si, rj:rj+sj] = (rng.rand(si, sj) < p).astype(float)
    W = (W + W.T) / 2
    np.fill_diagonal(W, 0)
    return GraphState(sp.csr_matrix(W))


def main():
    print("Experiment 56: Formation Nucleation from Random IC")
    print("=" * 70)
    t0 = time.time()

    params = ParameterRegistry(a_cl=3.0, beta_bd=20.0, volume_fraction=0.30)
    n_seeds = 10
    all_results = []

    graphs = [
        ('grid_10x10', GraphState.grid_2d(10, 10)),
        ('grid_15x15', GraphState.grid_2d(15, 15)),
        ('barbell_6_w1', make_barbell(6, 1.0)),
        ('barbell_6_w01', make_barbell(6, 0.1)),
        ('barbell_6_w001', make_barbell(6, 0.01)),
        ('sbm_2x30', make_sbm([30, 30])),
        ('sbm_3x20', make_sbm([20, 20, 20])),
        ('sbm_4x15', make_sbm([15, 15, 15, 15])),
    ]

    for label, graph in graphs:
        n = graph.n
        total_mass = 0.30 * n

        spec = spectral_k_estimate(graph, params)
        k_eigengap = spec['k_eigengap']
        k_threshold = spec['k_estimate']

        K_counts = []
        for seed in range(n_seeds):
            history, u_final = evolve_single_field(
                graph, params, total_mass, max_iter=3000,
                rng=np.random.RandomState(seed),
            )
            K_final = history[-1]['K']
            K_counts.append(K_final)

        mean_K = np.mean(K_counts)
        std_K = np.std(K_counts)
        mode_K = int(np.median(K_counts))

        print(f"  {label:>20}: K_eigengap={k_eigengap}, K_thresh={k_threshold}, "
              f"K_nucleated={mean_K:.1f}±{std_K:.1f} (mode={mode_K}), counts={K_counts}")

        all_results.append({
            'graph': label, 'n': n,
            'k_eigengap': k_eigengap, 'k_threshold': k_threshold,
            'eigenvalues': spec['eigenvalues'][:6],
            'gaps': spec['gaps'][:5],
            'K_counts': K_counts,
            'K_mean': mean_K, 'K_std': std_K, 'K_mode': mode_K,
        })

    # Correlation analysis
    print(f"\n{'='*70}")
    print(f"NUCLEATION SUMMARY")
    k_eigs = [r['k_eigengap'] for r in all_results]
    k_modes = [r['K_mode'] for r in all_results]
    k_means = [r['K_mean'] for r in all_results]

    if len(k_eigs) > 2:
        corr_mode = np.corrcoef(k_eigs, k_modes)[0, 1]
        corr_mean = np.corrcoef(k_eigs, k_means)[0, 1]
        print(f"  Corr(K_eigengap, K_mode) = {corr_mode:.3f}")
        print(f"  Corr(K_eigengap, K_mean) = {corr_mean:.3f}")

    matches = sum(1 for a, b in zip(k_eigs, k_modes) if a == b)
    print(f"  Exact matches (eigengap vs mode): {matches}/{len(k_eigs)}")

    output = {
        'experiment': 'exp56_nucleation',
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp56_nucleation.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}, time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
