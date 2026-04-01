#!/usr/bin/env python3
"""Experiment 36: Boundary dynamics under temporal perturbation.

Track how boundary vs deep core nodes respond to perturbation near bifurcation.
Validates three-tier persistence: deep core survives, boundary fails first.

Grid: 12×12 (n=144)
β values: [15, 20, 30, 50, 100]
ε values: [0.01, 0.05, 0.10, 0.15, 0.20]
5 random perturbation trials per (β, ε) pair.
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume


GRID = (12, 12)
BETAS = [15, 20, 30, 50, 100]
EPSILONS = [0.01, 0.05, 0.10, 0.15, 0.20]
N_TRIALS = 5
THETA_CORE = 0.8  # fallback; overridden by params.theta_core if available


def classify_nodes(u, graph, theta):
    """Classify nodes into deep core, shallow core, exterior.

    Deep core: u >= theta AND all neighbors also have u >= theta (depth >= 2).
    Shallow core: u >= theta but at least one neighbor has u < theta.
    Exterior: u < theta.
    """
    n = graph.n
    core_mask = u >= theta
    W = graph.W

    deep = np.zeros(n, dtype=bool)
    shallow = np.zeros(n, dtype=bool)

    for i in range(n):
        if not core_mask[i]:
            continue
        # Check all neighbors
        row = W.getrow(i)
        neighbors = row.indices
        if len(neighbors) > 0 and np.all(core_mask[neighbors]):
            deep[i] = True
        else:
            shallow[i] = True

    exterior = ~core_mask
    return deep, shallow, exterior


def layer_stats(u_new, u_star, mask, theta):
    """Compute per-layer statistics."""
    if np.sum(mask) == 0:
        return {
            'n_nodes': 0,
            'mean_delta': 0.0,
            'max_delta': 0.0,
            'frac_cross': 0.0,
        }
    delta = np.abs(u_new[mask] - u_star[mask])
    # Threshold crossing: was core and now isn't, or wasn't and now is
    was_core = u_star[mask] >= theta
    now_core = u_new[mask] >= theta
    crossings = np.sum(was_core != now_core)
    return {
        'n_nodes': int(np.sum(mask)),
        'mean_delta': float(np.mean(delta)),
        'max_delta': float(np.max(delta)),
        'frac_cross': float(crossings / np.sum(mask)),
    }


def run_experiment():
    graph = GraphState.grid_2d(*GRID)
    n = graph.n
    theta = THETA_CORE

    results = []
    print(f"Exp36: Boundary dynamics, {GRID[0]}x{GRID[1]} grid (n={n})")
    print(f"β values: {BETAS}, ε values: {EPSILONS}, {N_TRIALS} trials each")
    print(f"Total optimizations: {len(BETAS) * (1 + len(EPSILONS) * N_TRIALS)}")
    print("-" * 90)

    t0 = time.time()

    for beta in BETAS:
        # Find reference formation
        params = ParameterRegistry(
            beta_bd=beta,
            volume_fraction=0.3,
            max_iter=5000,
            n_restarts=3,
        )
        theta = getattr(params, 'theta_core', THETA_CORE)

        ref = find_formation(graph, params)
        u_star = ref.u.copy()

        deep, shallow, exterior = classify_nodes(u_star, graph, theta)
        n_deep = int(np.sum(deep))
        n_shallow = int(np.sum(shallow))
        n_ext = int(np.sum(exterior))
        print(f"\nβ={beta:3d}: E={ref.energy:.4f}, conv={ref.converged}, "
              f"deep={n_deep}, shallow={n_shallow}, ext={n_ext}")

        m = params.volume_fraction * n  # volume constraint target

        for eps in EPSILONS:
            # Accumulate stats across trials
            accum = {'deep': [], 'shallow': [], 'exterior': []}

            for trial in range(N_TRIALS):
                rng = np.random.RandomState(42 + trial)
                noise = rng.randn(n) * eps
                u_pert = project_volume(u_star + noise, m)

                # Re-optimize from perturbed field
                res = find_formation(graph, params, u_init=u_pert)
                u_new = res.u

                for name, mask in [('deep', deep), ('shallow', shallow), ('exterior', exterior)]:
                    stats = layer_stats(u_new, u_star, mask, theta)
                    accum[name].append(stats)

            # Average across trials
            row = {'beta': beta, 'eps': eps, 'n_deep': n_deep,
                   'n_shallow': n_shallow, 'n_ext': n_ext}
            for name in ['deep', 'shallow', 'exterior']:
                trials = accum[name]
                if trials[0]['n_nodes'] == 0:
                    row[f'mean_delta_{name}'] = 0.0
                    row[f'max_delta_{name}'] = 0.0
                    row[f'frac_cross_{name}'] = 0.0
                else:
                    row[f'mean_delta_{name}'] = float(np.mean([t['mean_delta'] for t in trials]))
                    row[f'max_delta_{name}'] = float(np.mean([t['max_delta'] for t in trials]))
                    row[f'frac_cross_{name}'] = float(np.mean([t['frac_cross'] for t in trials]))

            # Key ratio
            md_deep = row['mean_delta_deep']
            md_shallow = row['mean_delta_shallow']
            row['ratio_shallow_deep'] = (md_shallow / md_deep) if md_deep > 1e-12 else float('inf')

            results.append(row)
            print(f"  ε={eps:.2f}: Δu deep={md_deep:.5f}, shallow={md_shallow:.5f}, "
                  f"ratio={row['ratio_shallow_deep']:.2f}, "
                  f"cross_deep={row['frac_cross_deep']:.3f}, cross_shallow={row['frac_cross_shallow']:.3f}")

    elapsed = time.time() - t0
    print(f"\n{'=' * 90}")
    print(f"Total time: {elapsed:.1f}s")

    # Summary table
    print(f"\n{'β':>4} {'ε':>5} {'Δu_deep':>9} {'Δu_shal':>9} {'Δu_ext':>9} "
          f"{'ratio':>7} {'cross_d':>8} {'cross_s':>8}")
    print("-" * 70)
    for r in results:
        print(f"{r['beta']:4d} {r['eps']:5.2f} {r['mean_delta_deep']:9.5f} "
              f"{r['mean_delta_shallow']:9.5f} {r['mean_delta_exterior']:9.5f} "
              f"{r['ratio_shallow_deep']:7.2f} {r['frac_cross_deep']:8.3f} "
              f"{r['frac_cross_shallow']:8.3f}")

    # Save JSON
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'exp36_boundary_dynamics.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump({'config': {'grid': GRID, 'betas': BETAS, 'epsilons': EPSILONS,
                              'n_trials': N_TRIALS, 'theta_core': THETA_CORE,
                              'elapsed_s': elapsed},
                   'results': results}, f, indent=2)
    print(f"\nResults saved to {out_path}")

    return results


if __name__ == '__main__':
    run_experiment()
