#!/usr/bin/env python3
"""Experiment 49: Unified Predictions P-Unified-1/2 Validation.

Tests two predictions from T-Persist-K-Unified:
  P-Unified-1: Persist degrades continuously with Lambda: Persist ~ 1 - C * Lambda^2
  P-Unified-2: Core depth onset delta_min increases with Lambda

Method: K=2 formations at various lambda_rep, apply temporal perturbation,
measure per-formation persist and core depth statistics.

Uses coupling_strength() for Lambda computation and transport for persist.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import (find_k_formations, coupling_strength,
                        inter_formation_distances, formation_overlap)
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, project_volume
from scc.diagnostics import compute_diagnostics


def perturb_graph(graph, rng, strength=0.05):
    """Create a gently perturbed graph (simulate temporal change)."""
    n = graph.n
    W = graph.W.toarray().copy() if hasattr(graph.W, 'toarray') else graph.W.copy()
    # Add small random weight perturbation
    noise = rng.randn(n, n) * strength
    noise = (noise + noise.T) / 2  # symmetrize
    W_new = np.maximum(W + noise * (W > 0).astype(float), 0)
    np.fill_diagonal(W_new, 0)
    from scipy.sparse import csr_matrix
    return GraphState(csr_matrix(W_new))


def compute_core_depth(u, graph, theta_core=0.5):
    """Compute depth statistics for formation core."""
    n = len(u)
    core = u >= theta_core
    if not np.any(core):
        return {'max_depth': 0, 'mean_depth': 0.0, 'core_size': 0, 'deep_core_frac': 0.0}

    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    adj = (W > 0) & ~np.eye(n, dtype=bool)

    depth = np.zeros(n, dtype=int)
    visited = ~core.copy()
    frontier = set(np.where(~core)[0])
    d = 0
    while frontier:
        next_f = set()
        for node in frontier:
            for nb in np.where(adj[node])[0]:
                if not visited[nb]:
                    visited[nb] = True
                    depth[nb] = d + 1
                    next_f.add(nb)
        frontier = next_f
        d += 1

    core_depths = depth[core]
    deep = np.sum(core_depths >= 2)
    return {
        'max_depth': int(np.max(core_depths)) if len(core_depths) > 0 else 0,
        'mean_depth': float(np.mean(core_depths)) if len(core_depths) > 0 else 0,
        'core_size': int(np.sum(core)),
        'deep_core_frac': float(deep / max(np.sum(core), 1)),
    }


def compute_persist_overlap(u_t, u_s):
    """Compute core-overlap persistence (no transport needed)."""
    return float(np.sum(np.minimum(u_t, u_s)) / max(np.sum(u_t), np.sum(u_s), 1e-10))


def main():
    print("Experiment 49: P-Unified-1/2 Validation (Persist vs Lambda)")
    print("=" * 70)
    t0 = time.time()

    rng = np.random.RandomState(42)

    configs = [
        ('15x15', GraphState.grid_2d(15, 15), 0.35),
        ('20x20', GraphState.grid_2d(20, 20), 0.30),
    ]

    # Lambda_rep sweep — low values force interaction, high values separate
    lrep_values = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    perturbation_strengths = [0.02, 0.05, 0.10]

    all_results = []
    total = len(configs) * len(lrep_values) * len(perturbation_strengths)
    done = 0

    for grid_name, grid, vf in configs:
        n = grid.n

        params = ParameterRegistry(
            a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
            a_D=5.0, lambda_D=1.0, tau_D=0.0,
            alpha_bd=1.0, beta_bd=15.0,
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
            volume_fraction=vf,
        )

        print(f"\n--- {grid_name}, vf={vf} ---")

        for lrep in lrep_values:
            # Find K=2 formations at time t
            try:
                sources_t = find_k_formations(
                    grid, params, K=2, lambda_rep=lrep,
                    max_iter=1000, n_restarts=2,
                )
                fields_t = [s.u for s in sources_t]
            except Exception as e:
                print(f"  lrep={lrep}: formation FAILED: {e}")
                continue

            # Compute Lambda
            cs = coupling_strength(fields_t, grid, params, lrep)
            Lambda = cs['Lambda']

            # Depth stats at time t
            depths_t = [compute_core_depth(f, grid) for f in fields_t]

            for eps in perturbation_strengths:
                done += 1
                print(f"  [{done}/{total}] {grid_name} lrep={lrep} eps={eps}...", end='', flush=True)

                try:
                    # Create perturbed graph (simulate temporal change)
                    graph_s = perturb_graph(grid, rng, strength=eps)

                    # Find formations at time s (warm-started from time t)
                    sources_s = find_k_formations(
                        graph_s, params, K=2, lambda_rep=lrep,
                        init_fields=fields_t,
                        max_iter=500, n_restarts=1,
                    )
                    fields_s = [s.u for s in sources_s]

                    # Compute per-formation persist (core overlap method)
                    persists = [compute_persist_overlap(fields_t[k], fields_s[k]) for k in range(2)]
                    mean_persist = np.mean(persists)

                    # Depth stats at time s
                    depths_s = [compute_core_depth(f, graph_s) for f in fields_s]

                    # Depth change
                    depth_changes = [depths_s[k]['mean_depth'] - depths_t[k]['mean_depth']
                                     for k in range(2)]

                    print(f" Lambda={Lambda:.5f} Persist={mean_persist:.4f} "
                          f"depth_delta={np.mean(depth_changes):+.2f}")

                    all_results.append({
                        'grid': grid_name,
                        'n': n,
                        'vf': vf,
                        'lambda_rep': lrep,
                        'perturbation': eps,
                        'Lambda_coupling': Lambda,
                        'mu_per_formation': cs['mu_per_formation'],
                        'mu_floor': cs['mu_floor'],
                        'persist_per_formation': persists,
                        'mean_persist': mean_persist,
                        'depths_t': depths_t,
                        'depths_s': depths_s,
                        'depth_changes': depth_changes,
                        'mean_depth_change': float(np.mean(depth_changes)),
                    })

                except Exception as e:
                    print(f" FAILED: {e}")
                    all_results.append({
                        'grid': grid_name, 'lambda_rep': lrep,
                        'perturbation': eps, 'error': str(e),
                    })

    # Analysis
    valid = [r for r in all_results if 'Lambda_coupling' in r]
    print(f"\n{'='*70}")
    print(f"Summary: {len(valid)}/{len(all_results)} successful configs")

    # P-Unified-1: Persist vs Lambda
    print(f"\n--- P-Unified-1: Persist ~ 1 - C*Lambda^2 ---")
    if valid:
        lambdas = np.array([r['Lambda_coupling'] for r in valid])
        persists = np.array([r['mean_persist'] for r in valid])
        # Fit: persist = 1 - C * lambda^2
        # log(1-persist) ~ log(C) + 2*log(lambda) for lambda > 0
        mask = (lambdas > 1e-6) & (persists < 1.0)
        if np.sum(mask) > 2:
            x = np.log(lambdas[mask])
            y = np.log(np.maximum(1 - persists[mask], 1e-10))
            slope, intercept = np.polyfit(x, y, 1)
            C_fit = np.exp(intercept)
            print(f"  Fit: 1-Persist ~ {C_fit:.4f} * Lambda^{slope:.2f}")
            print(f"  Expected exponent: 2.0, got: {slope:.2f}")
            print(f"  P-Unified-1 {'SUPPORTED' if 1.5 < slope < 3.0 else 'NOT SUPPORTED'}")
        else:
            print(f"  Not enough non-trivial data for fitting")

    # P-Unified-2: Depth onset vs Lambda
    print(f"\n--- P-Unified-2: Depth delta_min proportional to Lambda ---")
    if valid:
        lambdas = np.array([r['Lambda_coupling'] for r in valid])
        depth_deltas = np.array([abs(r['mean_depth_change']) for r in valid])
        mask = lambdas > 1e-6
        if np.sum(mask) > 2:
            corr = np.corrcoef(lambdas[mask], depth_deltas[mask])[0, 1]
            print(f"  Correlation(Lambda, |depth_change|) = {corr:.3f}")
            print(f"  P-Unified-2 {'SUPPORTED' if corr > 0.3 else 'WEAK/NOT SUPPORTED'}")

    # Persist by grid
    for grid_name in ['15x15', '20x20']:
        subset = [r for r in valid if r['grid'] == grid_name]
        if subset:
            ps = [r['mean_persist'] for r in subset]
            ls = [r['Lambda_coupling'] for r in subset]
            print(f"\n  {grid_name}: {len(subset)} configs, "
                  f"Persist=[{min(ps):.4f}, {max(ps):.4f}], "
                  f"Lambda=[{min(ls):.5f}, {max(ls):.5f}]")

    # Save
    output = {
        'experiment': 'exp49_unified_predictions',
        'description': 'P-Unified-1/2 validation: persist vs Lambda on large grids',
        'configs': [{'grid': g, 'vf': v} for g, _, v in configs],
        'lambda_rep_values': lrep_values,
        'perturbation_strengths': perturbation_strengths,
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp49_unified_predictions.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {outpath}")
    print(f"Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
