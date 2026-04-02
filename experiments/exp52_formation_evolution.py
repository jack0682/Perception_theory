#!/usr/bin/env python3
"""Experiment 52: Formation Evolution — ES Perspective.

Observes multi-formation dynamics as an evolutionary process:
  - Each formation = individual competing for resources (volume)
  - Fitness = negative energy (lower energy = fitter)
  - Selection pressure = gradient descent on total energy
  - Competition = repulsion term + simplex constraint
  - Death = formation mass collapses below threshold
  - Merge = two formations overlap significantly

Tracks per-formation statistics at each iteration:
  - Mass (total field value)
  - Energy (self-energy)
  - Core size (nodes above threshold)
  - Peak value (max field value)
  - Overlap with neighbors

Tests on: grids (homogeneous), SBM (community structure), barbell (bottleneck)
"""
import sys, os, json, time
import numpy as np
from scipy import sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume
from scc.multi import formation_overlap


def make_barbell(n_side, bridge_weight=0.01):
    """Two grids connected by a weak bridge."""
    g1 = GraphState.grid_2d(n_side, n_side)
    n1 = g1.n
    n_total = 2 * n1
    W = np.zeros((n_total, n_total))
    W[:n1, :n1] = g1.W.toarray()
    W[n1:, n1:] = g1.W.toarray()
    mid1 = n1 - n_side // 2
    mid2 = n1 + n_side // 2
    W[mid1, mid2] = bridge_weight
    W[mid2, mid1] = bridge_weight
    return GraphState(sp.csr_matrix(W))


def make_sbm(sizes, p_in=0.3, p_out=0.01, rng=None):
    """Stochastic Block Model."""
    if rng is None:
        rng = np.random.RandomState(42)
    n = sum(sizes)
    W = np.zeros((n, n))
    for i, si in enumerate(sizes):
        for j, sj in enumerate(sizes):
            p = p_in if i == j else p_out
            ri, rj = sum(sizes[:i]), sum(sizes[:j])
            block = (rng.rand(si, sj) < p).astype(float)
            W[ri:ri+si, rj:rj+sj] = block
    W = (W + W.T) / 2
    np.fill_diagonal(W, 0)
    return GraphState(sp.csr_matrix(W))


def evolve_k_formations(graph, params, K, lambda_rep, lambda_bar, max_iter,
                         init_mode='random', record_interval=5, rng=None):
    """Run K-field gradient descent with per-step recording.

    Returns:
        history: list of dicts, one per recorded step
        final_fields: list of K arrays
    """
    if rng is None:
        rng = np.random.RandomState(42)

    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    vf = params.volume_fraction
    m_k = vf * n  # per-formation mass

    # Initialize K fields
    fields = []
    if init_mode == 'random':
        for k in range(K):
            u = rng.rand(n) * 0.5 + 0.01
            u = project_volume(u, m_k)
            fields.append(u)
    elif init_mode == 'spectral':
        # Use first K eigenvectors for spatial separation
        eigs = graph.spectrum(K + 1)
        from scipy.sparse.linalg import eigsh
        _, vecs = eigsh(graph.L.astype(np.float64), k=min(K+1, n-1), which='SM')
        idx = np.argsort(np.linalg.eigvalsh(graph.L.toarray()) if n < 50
                         else eigs)
        for k in range(K):
            # Use k-th eigenvector to bias initialization
            if k == 0:
                u = np.ones(n) * vf
            else:
                v = vecs[:, min(k, vecs.shape[1]-1)]
                u = vf + 0.3 * v / max(np.abs(v).max(), 1e-10)
            u = np.clip(u, 0.01, 0.99)
            u = project_volume(u, m_k)
            fields.append(u)
    elif init_mode == 'clustered':
        # Place formations at different spatial locations
        side = int(np.sqrt(n))
        for k in range(K):
            u = np.zeros(n)
            # Place Gaussian bump at different location
            cx = side * (k + 0.5) / K
            cy = side / 2
            for i in range(side):
                for j in range(side):
                    idx_node = i * side + j
                    if idx_node < n:
                        d2 = (i - cx)**2 + (j - cy)**2
                        u[idx_node] = np.exp(-d2 / (side/K)**2)
            u = project_volume(u, m_k)
            fields.append(u)

    history = []
    dt = 0.01
    prev_gnorm = float('inf')

    for tau in range(1, max_iter + 1):
        # Record state
        if tau == 1 or tau % record_interval == 0 or tau == max_iter:
            snapshot = {'iter': tau, 'formations': []}
            total_E = 0.0

            for k in range(K):
                u_k = fields[k]
                e_k = float(ec.energy(u_k)[0])
                total_E += e_k
                mass_k = float(np.sum(u_k))
                core_k = int(np.sum(u_k > 0.5))
                peak_k = float(np.max(u_k))
                mean_k = float(np.mean(u_k[u_k > 0.1])) if np.any(u_k > 0.1) else 0.0

                snapshot['formations'].append({
                    'mass': mass_k,
                    'energy': e_k,
                    'core_size': core_k,
                    'peak': peak_k,
                    'mean_active': mean_k,
                })

            # Add repulsion energy
            for j in range(K):
                for ki in range(j+1, K):
                    e_rep = lambda_rep * float(np.sum(fields[j] * fields[ki]))
                    total_E += e_rep

            # Overlap matrix
            ovlp = formation_overlap(fields, theta_supp=0.1)
            overlaps = []
            for j in range(K):
                for ki in range(j+1, K):
                    overlaps.append(float(ovlp[j, ki]))

            snapshot['total_energy'] = total_E
            snapshot['max_overlap'] = max(overlaps) if overlaps else 0
            snapshot['alive_count'] = sum(1 for f in snapshot['formations'] if f['core_size'] > 0)

            history.append(snapshot)

        # Gradient descent step
        max_gnorm = 0.0
        for k in range(K):
            g_intra = ec.gradient(fields[k])
            g_rep = lambda_rep * sum(fields[j] for j in range(K) if j != k)
            S = sum(fields)
            violation = np.maximum(0.0, S - 1.0)
            g_barrier = lambda_bar * 2.0 * violation
            g_total = g_intra + g_rep + g_barrier
            g_sigma = g_total - np.mean(g_total)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)
            u_new = fields[k] - dt * g_sigma
            u_new = project_volume(u_new, m_k)
            fields[k] = u_new

        # Adaptive step size
        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt *= 0.7
            dt = max(dt, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt *= 1.05
            dt = min(dt, 0.1)
        prev_gnorm = max_gnorm

        if tau > 50 and max_gnorm < 1e-5:
            # Record final state
            if tau % record_interval != 0:
                snapshot = {'iter': tau, 'formations': [], 'converged': True}
                for k in range(K):
                    u_k = fields[k]
                    snapshot['formations'].append({
                        'mass': float(np.sum(u_k)),
                        'energy': float(ec.energy(u_k)),
                        'core_size': int(np.sum(u_k > 0.5)),
                        'peak': float(np.max(u_k)),
                    })
                snapshot['alive_count'] = sum(1 for f in snapshot['formations'] if f['core_size'] > 0)
                history.append(snapshot)
            break

    return history, fields


def analyze_evolution(history, label):
    """Print evolution summary."""
    print(f"\n  === {label} ===")
    print(f"  {'iter':>6} {'K_alive':>7} {'E_total':>10} {'masses':>30} {'cores':>20} {'overlap':>8}")

    for h in history[::max(1, len(history)//15)]:  # Show ~15 snapshots
        masses = [f'{f["mass"]:.1f}' for f in h['formations']]
        cores = [f'{f["core_size"]}' for f in h['formations']]
        print(f"  {h['iter']:6d} {h.get('alive_count', '?'):>7} "
              f"{h.get('total_energy', 0):10.2f} "
              f"{','.join(masses):>30} {','.join(cores):>20} "
              f"{h.get('max_overlap', 0):8.0f}")

    # Key events
    alive_trajectory = [h.get('alive_count', len(h['formations'])) for h in history]
    iters = [h['iter'] for h in history]

    death_events = []
    for i in range(1, len(alive_trajectory)):
        if alive_trajectory[i] < alive_trajectory[i-1]:
            death_events.append((iters[i], alive_trajectory[i-1], alive_trajectory[i]))

    if death_events:
        print(f"  Death events:")
        for it, before, after in death_events:
            print(f"    iter {it}: K {before} -> {after}")
    else:
        print(f"  No death events (all {alive_trajectory[-1]} formations survived)")

    return {
        'alive_trajectory': alive_trajectory,
        'iters': iters,
        'death_events': death_events,
        'final_alive': alive_trajectory[-1],
    }


def main():
    print("Experiment 52: Formation Evolution (ES Perspective)")
    print("=" * 70)
    t0 = time.time()

    rng = np.random.RandomState(42)
    all_results = []

    configs = [
        # (label, graph, K_init, params_overrides, init_mode)
        ('grid_10x10_K4', GraphState.grid_2d(10, 10), 4, {'beta_bd': 20.0, 'volume_fraction': 0.25}, 'random'),
        ('grid_10x10_K4_clustered', GraphState.grid_2d(10, 10), 4, {'beta_bd': 20.0, 'volume_fraction': 0.20}, 'clustered'),
        ('grid_15x15_K6', GraphState.grid_2d(15, 15), 6, {'beta_bd': 20.0, 'volume_fraction': 0.15}, 'random'),
        ('barbell_6_K2', make_barbell(6, 0.01), 2, {'beta_bd': 15.0, 'volume_fraction': 0.30}, 'random'),
        ('barbell_6_K4', make_barbell(6, 0.01), 4, {'beta_bd': 15.0, 'volume_fraction': 0.20}, 'random'),
        ('sbm_3x20_K3', make_sbm([20, 20, 20], p_in=0.3, p_out=0.005, rng=rng), 3, {'beta_bd': 15.0, 'volume_fraction': 0.25}, 'random'),
        ('sbm_3x20_K6', make_sbm([20, 20, 20], p_in=0.3, p_out=0.005, rng=rng), 6, {'beta_bd': 15.0, 'volume_fraction': 0.15}, 'random'),
    ]

    for label, graph, K_init, p_overrides, init_mode in configs:
        print(f"\n{'─'*50}")
        print(f"Config: {label} (n={graph.n}, K_init={K_init})")

        params = ParameterRegistry(
            a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
            a_D=5.0, lambda_D=1.0, tau_D=0.0,
            alpha_bd=1.0,
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
            **p_overrides,
        )

        history, final_fields = evolve_k_formations(
            graph, params, K=K_init,
            lambda_rep=5.0, lambda_bar=50.0,
            max_iter=2000, record_interval=10,
            init_mode=init_mode, rng=np.random.RandomState(42),
        )

        analysis = analyze_evolution(history, label)

        all_results.append({
            'label': label,
            'n': graph.n,
            'K_init': K_init,
            'init_mode': init_mode,
            'params': p_overrides,
            'history': history,
            'analysis': {
                'final_alive': analysis['final_alive'],
                'death_events': analysis['death_events'],
                'total_iters': history[-1]['iter'],
            },
        })

    # Summary
    print(f"\n{'='*70}")
    print(f"EVOLUTION SUMMARY")
    print(f"{'='*70}")
    print(f"{'Config':>30} {'K_init':>6} {'K_final':>7} {'Deaths':>6} {'Iters':>6}")
    for r in all_results:
        print(f"{r['label']:>30} {r['K_init']:>6} {r['analysis']['final_alive']:>7} "
              f"{len(r['analysis']['death_events']):>6} {r['analysis']['total_iters']:>6}")

    # Key findings
    print(f"\nKey findings:")
    all_survive = sum(1 for r in all_results if r['analysis']['final_alive'] == r['K_init'])
    some_die = sum(1 for r in all_results if r['analysis']['final_alive'] < r['K_init'])
    print(f"  All survive: {all_survive}/{len(all_results)}")
    print(f"  Some die: {some_die}/{len(all_results)}")

    # Save
    output = {
        'experiment': 'exp52_formation_evolution',
        'description': 'Formation evolution from ES perspective',
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp52_formation_evolution.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {outpath}")
    print(f"Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
