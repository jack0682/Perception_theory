#!/usr/bin/env python3
"""Experiment 51: Spectral K-Selection.

Tests the hypothesis: K* = #{Laplacian eigenvalues below phase transition threshold}.

Phase A: Homogeneous grids (expect K*=1 always)
Phase B: Barbell graphs with varying bridge weight (expect K*=2 at low weight)
Phase C: Spectral correlation across all graphs
Phase D: Structured graphs (SBM, random geometric)

References:
  - von Luxburg (2007): Eigengap heuristic for spectral clustering
  - Lee, Oveis Gharan, Trevisan (2012): Higher-order Cheeger inequalities
  - SCC T8-Core: phase transition threshold beta*|W''(c)|/(4*alpha)
"""
import sys, os, json, time
import numpy as np
from scipy import sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations, spectral_k_estimate, find_optimal_k
from scc.optimizer import find_formation


def make_barbell(n_side, bridge_weight=1.0):
    """Create a barbell graph: two n_side x n_side grids connected by a bridge."""
    g1 = GraphState.grid_2d(n_side, n_side)
    n1 = g1.n
    n_total = 2 * n1
    W = np.zeros((n_total, n_total))
    W1 = g1.W.toarray()
    W[:n1, :n1] = W1
    W[n1:, n1:] = W1
    # Bridge: connect the rightmost column of g1 to leftmost column of g2
    # Just connect one pair of nodes for simplicity
    mid1 = n1 - n_side // 2  # middle of right edge of g1
    mid2 = n1 + n_side // 2  # middle of left edge of g2
    W[mid1, mid2] = bridge_weight
    W[mid2, mid1] = bridge_weight
    return GraphState(sp.csr_matrix(W))


def make_sbm(communities, p_in=0.3, p_out=0.01, rng=None):
    """Create a Stochastic Block Model graph."""
    if rng is None:
        rng = np.random.RandomState(42)
    sizes = communities
    n = sum(sizes)
    W = np.zeros((n, n))
    offset = 0
    for i, si in enumerate(sizes):
        for j, sj in enumerate(sizes):
            p = p_in if i == j else p_out
            block = (rng.rand(si, sj) < p).astype(float)
            W[offset:offset+si, sum(sizes[:j]):sum(sizes[:j])+sj] = block
        offset += si
    W = (W + W.T) / 2
    np.fill_diagonal(W, 0)
    return GraphState(sp.csr_matrix(W))


def make_random_geometric(n, radius=0.3, rng=None):
    """Create a random geometric graph."""
    if rng is None:
        rng = np.random.RandomState(42)
    pos = rng.rand(n, 2)
    W = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            d = np.sqrt(np.sum((pos[i] - pos[j])**2))
            if d < radius:
                W[i, j] = 1.0
                W[j, i] = 1.0
    return GraphState(sp.csr_matrix(W))


def run_k_sweep(graph, params_base, K_max, lambda_rep, vf_total, label):
    """Sweep K=1..K_max and return energies."""
    n = graph.n
    results = {}

    for K in range(1, K_max + 1):
        vf_k = vf_total / K
        if vf_k < 0.05 or vf_k > 0.90:
            break

        params_k = ParameterRegistry(
            a_cl=params_base.a_cl, eta_cl=params_base.eta_cl, tau_cl=params_base.tau_cl,
            a_D=params_base.a_D, lambda_D=params_base.lambda_D, tau_D=params_base.tau_D,
            alpha_bd=params_base.alpha_bd, beta_bd=params_base.beta_bd,
            w_cl=params_base.w_cl, w_sep=params_base.w_sep, w_bd=params_base.w_bd,
            volume_fraction=vf_k,
        )

        try:
            if K == 1:
                res = find_formation(graph, params_k)
                e = res.energy
            else:
                results_k = find_k_formations(
                    graph, params_k, K=K, lambda_rep=lambda_rep,
                    max_iter=800, n_restarts=2,
                )
                e = sum(r.energy for r in results_k)
                fields = [r.u for r in results_k]
                for j in range(K):
                    for ki in range(j+1, K):
                        e += lambda_rep * float(np.sum(fields[j] * fields[ki]))
            results[K] = float(e)
        except Exception as ex:
            results[K] = float('inf')
            print(f"      K={K} failed: {ex}")

    k_star = min(results, key=results.get) if results else 1
    return k_star, results


def main():
    print("Experiment 51: Spectral K-Selection")
    print("=" * 70)
    t0 = time.time()

    params_base = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=20.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.30,
    )
    lambda_rep = 10.0
    vf_total = 0.30
    K_max = 4
    all_results = []

    # === Phase A: Homogeneous Grids ===
    print("\n--- Phase A: Homogeneous Grids ---")
    for side in [8, 10, 15]:
        grid = GraphState.grid_2d(side, side)
        label = f"{side}x{side}"
        print(f"  {label} (n={grid.n})...", end='', flush=True)

        spec = spectral_k_estimate(grid, params_base)
        k_star, energies = run_k_sweep(grid, params_base, K_max, lambda_rep, vf_total, label)

        e_list = [energies.get(k, float('inf')) for k in range(1, K_max+1)]
        e_str = ', '.join(f'{e:.2f}' for e in e_list)
        print(f" K*={k_star}, K_spec={spec['k_estimate']}, E=[{e_str}]")

        all_results.append({
            'phase': 'A', 'graph': label, 'n': grid.n,
            'k_star': k_star, 'k_spectral': spec['k_estimate'],
            'energies': energies, 'threshold': spec['threshold'],
            'eigenvalues': spec['eigenvalues'][:5],
        })

    # === Phase B: Barbell Graphs ===
    print("\n--- Phase B: Barbell Graphs ---")
    for w in [1.0, 0.1, 0.01, 0.001]:
        graph = make_barbell(6, bridge_weight=w)
        label = f"barbell_6x6_w{w}"
        print(f"  {label} (n={graph.n})...", end='', flush=True)

        spec = spectral_k_estimate(graph, params_base)
        k_star, energies = run_k_sweep(graph, params_base, min(K_max, 3), lambda_rep, vf_total, label)

        print(f" K*={k_star}, K_spec={spec['k_estimate']}, "
              f"lambda2={spec['eigenvalues'][1] if len(spec['eigenvalues'])>1 else 'N/A':.4f}, "
              f"thresh={spec['threshold']:.4f}")

        all_results.append({
            'phase': 'B', 'graph': label, 'n': graph.n,
            'bridge_weight': w,
            'k_star': k_star, 'k_spectral': spec['k_estimate'],
            'energies': energies, 'threshold': spec['threshold'],
            'eigenvalues': spec['eigenvalues'][:5],
        })

    # === Phase C: Spectral Correlation ===
    print("\n--- Phase C: Spectral Correlation ---")
    k_stars = [r['k_star'] for r in all_results]
    k_specs = [r['k_spectral'] for r in all_results]
    if len(k_stars) > 2:
        corr = np.corrcoef(k_stars, k_specs)[0, 1]
        matches = sum(1 for a, b in zip(k_stars, k_specs) if a == b)
        print(f"  Correlation(K*, K_spec): {corr:.3f}")
        print(f"  Exact matches: {matches}/{len(k_stars)}")

    # === Phase D: Structured Graphs ===
    print("\n--- Phase D: Structured Graphs ---")
    rng = np.random.RandomState(42)

    # SBM with 3 communities
    graph_sbm = make_sbm([25, 25, 25], p_in=0.3, p_out=0.01, rng=rng)
    label = "sbm_3x25"
    print(f"  {label} (n={graph_sbm.n})...", end='', flush=True)
    spec = spectral_k_estimate(graph_sbm, params_base)
    k_star, energies = run_k_sweep(graph_sbm, params_base, K_max, lambda_rep, vf_total, label)
    print(f" K*={k_star}, K_spec={spec['k_estimate']}, "
          f"eigs={[f'{e:.4f}' for e in spec['eigenvalues'][:5]]}")
    all_results.append({
        'phase': 'D', 'graph': label, 'n': graph_sbm.n,
        'k_star': k_star, 'k_spectral': spec['k_estimate'],
        'energies': energies, 'threshold': spec['threshold'],
        'eigenvalues': spec['eigenvalues'][:5],
    })

    # SBM with 2 communities
    graph_sbm2 = make_sbm([35, 35], p_in=0.3, p_out=0.01, rng=rng)
    label = "sbm_2x35"
    print(f"  {label} (n={graph_sbm2.n})...", end='', flush=True)
    spec = spectral_k_estimate(graph_sbm2, params_base)
    k_star, energies = run_k_sweep(graph_sbm2, params_base, min(K_max, 3), lambda_rep, vf_total, label)
    print(f" K*={k_star}, K_spec={spec['k_estimate']}, "
          f"eigs={[f'{e:.4f}' for e in spec['eigenvalues'][:5]]}")
    all_results.append({
        'phase': 'D', 'graph': label, 'n': graph_sbm2.n,
        'k_star': k_star, 'k_spectral': spec['k_estimate'],
        'energies': energies, 'threshold': spec['threshold'],
        'eigenvalues': spec['eigenvalues'][:5],
    })

    # Random geometric
    graph_rg = make_random_geometric(80, radius=0.25, rng=rng)
    label = "rg_80_r025"
    print(f"  {label} (n={graph_rg.n})...", end='', flush=True)
    spec = spectral_k_estimate(graph_rg, params_base)
    k_star, energies = run_k_sweep(graph_rg, params_base, K_max, lambda_rep, vf_total, label)
    print(f" K*={k_star}, K_spec={spec['k_estimate']}, "
          f"eigs={[f'{e:.4f}' for e in spec['eigenvalues'][:5]]}")
    all_results.append({
        'phase': 'D', 'graph': label, 'n': graph_rg.n,
        'k_star': k_star, 'k_spectral': spec['k_estimate'],
        'energies': energies, 'threshold': spec['threshold'],
        'eigenvalues': spec['eigenvalues'][:5],
    })

    # === Final Summary ===
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")

    k_stars_all = [r['k_star'] for r in all_results]
    k_specs_all = [r['k_spectral'] for r in all_results]
    if len(k_stars_all) > 2:
        corr = np.corrcoef(k_stars_all, k_specs_all)[0, 1]
        matches = sum(1 for a, b in zip(k_stars_all, k_specs_all) if a == b)
        print(f"Overall correlation(K*, K_spec): {corr:.3f}")
        print(f"Exact matches: {matches}/{len(k_stars_all)} ({100*matches/len(k_stars_all):.0f}%)")

    print(f"\nPer-graph:")
    for r in all_results:
        match = "OK" if r['k_star'] == r['k_spectral'] else "MISMATCH"
        print(f"  {r['graph']:>20s}: K*={r['k_star']}, K_spec={r['k_spectral']} [{match}]")

    # Save
    output = {
        'experiment': 'exp51_k_selection',
        'description': 'Spectral K-selection validation',
        'params': {'beta': 20.0, 'alpha': 1.0, 'vf': vf_total, 'lambda_rep': lambda_rep},
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp51_k_selection.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {outpath}")
    print(f"Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
