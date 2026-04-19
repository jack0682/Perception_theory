"""exp48: Systematic Λ_coupling regime sweep.

Validates the unified regime parametrization by sweeping λ_rep
at high volume fraction (vf=0.45) where formations are forced to interact.

Computes Λ_coupling = λ_rep * ω_jk / min(μ_j, μ_k) and compares:
  - Predicted regime from Λ thresholds
  - Actual regime from classify_regime()

Tests three predictions:
  P-Unified-1: Persist degrades continuously with Λ
  P-Unified-2: Depth onset δ_min increases with Λ
  P-Unified-3: Bifurcation sharpness at Λ = 1/(K-1)
"""
import json
import time
import numpy as np
from scc import GraphState
from scc.params import ParameterRegistry as PR
from scc.multi import find_k_formations, inter_formation_distances, classify_regime
from scc.operators import closure, distinction
from scc.diagnostics import DiagnosticVector


def compute_spectral_gap(u, graph, params):
    """Compute constrained Hessian spectral gap μ for a formation."""
    n = len(u)
    L = graph.L.toarray() if hasattr(graph.L, 'toarray') else np.array(graph.L)
    W2 = 2.0 * (1.0 - 6.0 * u + 6.0 * u**2)
    H = 4.0 * params.alpha_bd * L + params.beta_bd * np.diag(W2)
    P = np.eye(n) - np.outer(np.ones(n), np.ones(n)) / n
    H_proj = P @ H @ P
    eigs = np.sort(np.linalg.eigvalsh(H_proj))
    return float(eigs[1])  # First nonzero eigenvalue


def compute_lambda_coupling(fields, graph, params, lambda_rep):
    """Compute Λ_coupling = max_{j≠k} λ_rep * ω_jk / min(μ_j, μ_k)."""
    K = len(fields)

    # Per-formation spectral gaps
    mus = [compute_spectral_gap(f, graph, params) for f in fields]

    # Pairwise coupling
    max_Lambda = 0.0
    max_omega = 0.0
    for j in range(K):
        for k in range(j+1, K):
            inner = float(np.sum(fields[j] * fields[k]))
            norm_j = float(np.sum(fields[j]**2))
            norm_k = float(np.sum(fields[k]**2))
            omega_jk = inner / min(norm_j, norm_k) if min(norm_j, norm_k) > 1e-10 else 0
            mu_min = max(min(mus[j], mus[k]), 1e-6)
            Lambda_jk = lambda_rep * omega_jk / mu_min
            max_Lambda = max(max_Lambda, Lambda_jk)
            max_omega = max(max_omega, omega_jk)

    return max_Lambda, max_omega, mus


def predict_regime(Lambda, K=2):
    """Predict regime from Λ_coupling thresholds."""
    if Lambda < 0.001:
        return "well-separated"
    elif Lambda < 1.0 / (K - 1):
        return "weakly-interacting"
    else:
        return "strongly-interacting"


def compute_depth_stats(u, graph, theta_core=0.5):
    """Compute core depth statistics."""
    n = len(u)
    core = u > theta_core
    if not np.any(core):
        return {'max_depth': 0, 'mean_depth': 0, 'core_size': 0}

    # BFS from non-core to compute depths
    L = graph.L.toarray() if hasattr(graph.L, 'toarray') else np.array(graph.L)
    adj = (L != 0) & ~np.eye(n, dtype=bool)

    depth = np.zeros(n, dtype=int)
    visited = ~core  # Start from non-core
    frontier = set(np.where(~core)[0])
    d = 0
    while frontier:
        next_frontier = set()
        for node in frontier:
            for nb in np.where(adj[node])[0]:
                if not visited[nb]:
                    visited[nb] = True
                    depth[nb] = d + 1
                    next_frontier.add(nb)
        frontier = next_frontier
        d += 1

    core_depths = depth[core]
    return {
        'max_depth': int(np.max(core_depths)) if len(core_depths) > 0 else 0,
        'mean_depth': float(np.mean(core_depths)) if len(core_depths) > 0 else 0,
        'core_size': int(np.sum(core))
    }


if __name__ == '__main__':
    print("Experiment 48: Systematic Λ_coupling Regime Sweep")
    print("=" * 70)

    all_results = []

    # Sweep parameters
    grid_configs = [(8, 8), (10, 10)]
    vfs = [0.40, 0.45]
    lreps = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]

    t0 = time.time()
    total = len(grid_configs) * len(vfs) * len(lreps)
    done = 0

    for N_x, N_y in grid_configs:
        g = GraphState.grid_2d(N_x, N_y)
        n = N_x * N_y

        for vf in vfs:
            p = PR(volume_fraction=vf, beta_bd=10)

            print(f"\n--- {N_x}x{N_y}, vf={vf} ---")
            print(f"{'lrep':>8} {'d_min':>5} {'ovlp':>5} {'omega':>8} {'Lambda':>10} "
                  f"{'pred':>20} {'actual':>20} {'match':>5}")

            for lrep in lreps:
                done += 1
                try:
                    results = find_k_formations(g, p, K=2, lambda_rep=lrep, n_restarts=2)
                    fields = [r.u for r in results]
                    u1, u2 = fields[0], fields[1]

                    # Overlap
                    overlap = int(np.sum((u1 > 0.1) & (u2 > 0.1)))

                    # Lambda_coupling
                    Lambda, omega, mus = compute_lambda_coupling(fields, g, p, lrep)

                    # Distance
                    dmat = inter_formation_distances(fields, g)
                    d_min = float(dmat[0, 1])

                    # Regimes
                    actual = classify_regime(fields, g)
                    predicted = predict_regime(Lambda, K=2)
                    match = "YES" if predicted == actual else "no"

                    # Diagnostics per formation
                    diags = []
                    depths = []
                    for r in results:
                        d = r.diagnostics
                        diags.append({
                            'bind': float(d.bind),
                            'sep': float(d.sep),
                            'inside': float(d.inside),
                            'persist': float(d.persist) if hasattr(d, 'persist') else None,
                        })
                        depths.append(compute_depth_stats(r.u, g))

                    entry = {
                        'grid': f'{N_x}x{N_y}',
                        'vf': vf,
                        'lambda_rep': lrep,
                        'd_min': d_min,
                        'overlap': overlap,
                        'omega_jk': float(omega),
                        'mu_1': float(mus[0]),
                        'mu_2': float(mus[1]),
                        'Lambda_coupling': float(Lambda),
                        'predicted_regime': predicted,
                        'actual_regime': actual,
                        'match': match == "YES",
                        'diagnostics': diags,
                        'depth_stats': depths,
                    }
                    all_results.append(entry)

                    print(f"{lrep:8.3f} {d_min:5.0f} {overlap:5d} {omega:8.4f} "
                          f"{Lambda:10.5f} {predicted:>20} {actual:>20} {match:>5}")

                except Exception as e:
                    print(f"{lrep:8.3f} ERROR: {str(e)[:50]}")
                    all_results.append({
                        'grid': f'{N_x}x{N_y}', 'vf': vf,
                        'lambda_rep': lrep, 'error': str(e)[:100]
                    })

    elapsed = time.time() - t0

    # Summary
    matches = sum(1 for r in all_results if r.get('match', False))
    valid = sum(1 for r in all_results if 'Lambda_coupling' in r)

    print(f"\n{'=' * 70}")
    print(f"Summary: {matches}/{valid} regime predictions correct ({100*matches/max(valid,1):.0f}%)")
    print(f"Total time: {elapsed:.1f}s")

    # Regime distribution
    for regime in ['well-separated', 'weakly-interacting', 'strongly-interacting']:
        count = sum(1 for r in all_results if r.get('actual_regime') == regime)
        print(f"  {regime}: {count} configs")

    # Lambda ranges by regime
    for regime in ['well-separated', 'weakly-interacting', 'strongly-interacting']:
        lambdas = [r['Lambda_coupling'] for r in all_results
                   if r.get('actual_regime') == regime and 'Lambda_coupling' in r]
        if lambdas:
            print(f"  {regime} Λ range: [{min(lambdas):.5f}, {max(lambdas):.5f}]")

    # Save
    output = {
        'experiment': 'exp48_regime_sweep',
        'description': 'Systematic Lambda_coupling regime validation',
        'params': {
            'grids': [f'{x}x{y}' for x, y in grid_configs],
            'vfs': vfs,
            'lreps': lreps,
            'beta': 10, 'K': 2
        },
        'results': all_results,
        'summary': {
            'total': len(all_results),
            'valid': valid,
            'matches': matches,
            'accuracy': matches / max(valid, 1),
            'elapsed_s': elapsed,
        }
    }

    with open('experiments/results/exp48_regime_sweep.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to experiments/results/exp48_regime_sweep.json")
