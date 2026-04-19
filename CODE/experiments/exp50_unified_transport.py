#!/usr/bin/env python3
"""Experiment 50: P-Unified-1/2 with Transport-Based Persist.

Proper validation of:
  P-Unified-1: Persist degrades continuously with Lambda
  P-Unified-2: Core depth onset increases with Lambda

Key improvements over exp49:
  1. Transport-based persist (persist_transport) instead of core overlap
  2. Baseline subtraction: K=1 persist measured first, K=2 compared
  3. Parameter perturbation (delta_beta) for natural temporal change
  4. Medium grids (10x10, 12x12) for good formation quality
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations, coupling_strength
from scc.optimizer import find_formation
from scc.transport import transport_fixed_point, persist_transport


def measure_single_persist(graph, params_t, params_s, verbose=False):
    """Measure K=1 persistence under parameter change (baseline)."""
    res_t = find_formation(graph, params_t)
    u_t = res_t.u

    # Transport from t to s
    tr = transport_fixed_point(u_t, graph, params_s, sigma=1.0, gamma=1.0,
                                eps_ot=1.0, lambda_tr=0.1, max_fp_iter=10)
    u_s = tr.u_s
    M = tr.M

    p = persist_transport(u_t, u_s, M, theta_core=0.5)
    overlap = float(np.sum(np.minimum(u_t, u_s)) / max(np.sum(u_t), np.sum(u_s), 1e-10))

    if verbose:
        print(f"    K=1: persist_transport={p:.4f}, overlap={overlap:.4f}, "
              f"converged={tr.converged}, iters={tr.iterations}")
    return {
        'persist_transport': p,
        'persist_overlap': overlap,
        'converged': tr.converged,
        'iterations': tr.iterations,
    }


def measure_multi_persist(graph, params_t, params_s, K, lambda_rep, verbose=False):
    """Measure K-formation persistence under parameter change."""
    # Find formations at time t
    sources_t = find_k_formations(graph, params_t, K=K, lambda_rep=lambda_rep,
                                   max_iter=800, n_restarts=2)
    fields_t = [s.u for s in sources_t]

    # Compute Lambda
    cs = coupling_strength(fields_t, graph, params_t, lambda_rep)
    Lambda = cs['Lambda']

    # Per-formation transport and persist
    persists = []
    overlaps = []
    for k in range(K):
        u_t_k = fields_t[k]
        # Transport each formation independently
        tr = transport_fixed_point(u_t_k, graph, params_s, sigma=1.0, gamma=1.0,
                                    eps_ot=1.0, lambda_tr=0.1, max_fp_iter=10)
        u_s_k = tr.u_s
        M_k = tr.M

        p = persist_transport(u_t_k, u_s_k, M_k, theta_core=0.5)
        ov = float(np.sum(np.minimum(u_t_k, u_s_k)) /
                   max(np.sum(u_t_k), np.sum(u_s_k), 1e-10))
        persists.append(p)
        overlaps.append(ov)

    mean_persist = float(np.mean(persists))
    mean_overlap = float(np.mean(overlaps))

    if verbose:
        print(f"    K={K}, lrep={lambda_rep}: Lambda={Lambda:.5f}, "
              f"persist_tr={mean_persist:.4f}, overlap={mean_overlap:.4f}")

    return {
        'Lambda': Lambda,
        'mu_per_formation': cs['mu_per_formation'],
        'mu_floor': cs['mu_floor'],
        'omega_matrix': cs['omega_matrix'].tolist(),
        'predicted_regime': cs['predicted_regime'],
        'persists_transport': persists,
        'persists_overlap': overlaps,
        'mean_persist_transport': mean_persist,
        'mean_persist_overlap': mean_overlap,
    }


def compute_core_depth(u, graph, theta_core=0.5):
    """Compute core depth statistics."""
    n = len(u)
    core = u >= theta_core
    if not np.any(core):
        return {'max_depth': 0, 'mean_depth': 0.0, 'core_size': 0}

    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    adj = (W > 0) & ~np.eye(n, dtype=bool)

    depth = np.zeros(n, dtype=int)
    visited = ~core.copy()
    frontier = set(np.where(~core)[0])
    d = 0
    while frontier:
        nf = set()
        for node in frontier:
            for nb in np.where(adj[node])[0]:
                if not visited[nb]:
                    visited[nb] = True
                    depth[nb] = d + 1
                    nf.add(nb)
        frontier = nf
        d += 1

    cd = depth[core]
    return {
        'max_depth': int(np.max(cd)) if len(cd) > 0 else 0,
        'mean_depth': float(np.mean(cd)) if len(cd) > 0 else 0,
        'core_size': int(np.sum(core)),
    }


def main():
    print("Experiment 50: P-Unified-1/2 with Transport-Based Persist")
    print("=" * 70)
    t0 = time.time()

    grid_configs = [
        ('10x10', GraphState.grid_2d(10, 10)),
        ('12x12', GraphState.grid_2d(12, 12)),
    ]

    # Parameter perturbation: change beta
    delta_betas = [1.0, 2.0, 5.0]

    # Lambda sweep via lambda_rep
    lrep_values = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0]

    all_results = []

    for grid_name, grid in grid_configs:
        n = grid.n
        vf = 0.40
        beta_t = 20.0

        print(f"\n{'='*50}")
        print(f"Grid: {grid_name}, vf={vf}, beta_t={beta_t}")

        for delta_beta in delta_betas:
            beta_s = beta_t + delta_beta

            params_t = ParameterRegistry(
                a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
                a_D=5.0, lambda_D=1.0, tau_D=0.0,
                alpha_bd=1.0, beta_bd=beta_t,
                w_cl=1.0, w_sep=1.0, w_bd=1.0,
                volume_fraction=vf,
            )
            params_s = ParameterRegistry(
                a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
                a_D=5.0, lambda_D=1.0, tau_D=0.0,
                alpha_bd=1.0, beta_bd=beta_s,
                w_cl=1.0, w_sep=1.0, w_bd=1.0,
                volume_fraction=vf,
            )

            print(f"\n  delta_beta={delta_beta} (beta: {beta_t} -> {beta_s})")

            # K=1 baseline
            print(f"  --- Baseline (K=1) ---")
            try:
                baseline = measure_single_persist(grid, params_t, params_s, verbose=True)
            except Exception as e:
                print(f"    K=1 FAILED: {e}")
                baseline = {'persist_transport': None, 'error': str(e)}

            # K=2 with Lambda sweep
            print(f"  --- K=2 Lambda sweep ---")
            for lrep in lrep_values:
                try:
                    result = measure_multi_persist(grid, params_t, params_s,
                                                   K=2, lambda_rep=lrep, verbose=True)

                    # Baseline-subtracted persist
                    if baseline.get('persist_transport') is not None and baseline['persist_transport'] > 0:
                        persist_ratio = result['mean_persist_transport'] / baseline['persist_transport']
                    else:
                        persist_ratio = None

                    # Depth stats
                    sources_t = find_k_formations(grid, params_t, K=2, lambda_rep=lrep,
                                                   max_iter=500, n_restarts=1)
                    depths = [compute_core_depth(s.u, grid) for s in sources_t]

                    entry = {
                        'grid': grid_name,
                        'n': n,
                        'vf': vf,
                        'beta_t': beta_t,
                        'beta_s': beta_s,
                        'delta_beta': delta_beta,
                        'lambda_rep': lrep,
                        'baseline_persist': baseline.get('persist_transport'),
                        'baseline_overlap': baseline.get('persist_overlap'),
                        'persist_ratio': persist_ratio,
                        'depths': depths,
                        **result,
                    }
                    all_results.append(entry)

                except Exception as e:
                    print(f"    lrep={lrep} FAILED: {e}")
                    all_results.append({
                        'grid': grid_name, 'delta_beta': delta_beta,
                        'lambda_rep': lrep, 'error': str(e),
                    })

    # Analysis
    valid = [r for r in all_results if 'Lambda' in r]
    print(f"\n{'='*70}")
    print(f"Summary: {len(valid)}/{len(all_results)} successful")

    if valid:
        # P-Unified-1: persist_ratio vs Lambda
        print(f"\n--- P-Unified-1: Persist ratio vs Lambda ---")
        lambdas = np.array([r['Lambda'] for r in valid])
        p_tr = np.array([r['mean_persist_transport'] for r in valid])
        p_ratios = np.array([r['persist_ratio'] for r in valid if r['persist_ratio'] is not None])
        l_ratios = np.array([r['Lambda'] for r in valid if r['persist_ratio'] is not None])

        print(f"  Transport persist range: [{min(p_tr):.4f}, {max(p_tr):.4f}]")
        if len(p_ratios) > 0:
            print(f"  Persist ratio range: [{min(p_ratios):.4f}, {max(p_ratios):.4f}]")

        # Correlation
        mask = lambdas > 1e-5
        if np.sum(mask) > 2:
            corr_raw = np.corrcoef(lambdas[mask], p_tr[mask])[0, 1]
            print(f"  Corr(Lambda, persist_transport) = {corr_raw:.3f}")

        mask2 = (l_ratios > 1e-5)
        if np.sum(mask2) > 2:
            corr_ratio = np.corrcoef(l_ratios[mask2], p_ratios[mask2])[0, 1]
            print(f"  Corr(Lambda, persist_ratio) = {corr_ratio:.3f}")

        # Fit: 1-persist_ratio ~ C * Lambda^alpha
        mask3 = (l_ratios > 1e-5) & (p_ratios < 1.0) & (p_ratios > 0)
        if np.sum(mask3) > 2:
            x = np.log(l_ratios[mask3])
            y = np.log(np.maximum(1 - p_ratios[mask3], 1e-10))
            slope, intercept = np.polyfit(x, y, 1)
            print(f"  Fit: 1 - persist_ratio ~ {np.exp(intercept):.4f} * Lambda^{slope:.2f}")
            print(f"  Expected exponent: ~2.0, got: {slope:.2f}")

        # By delta_beta
        print(f"\n  By delta_beta:")
        for db in delta_betas:
            sub = [r for r in valid if r['delta_beta'] == db]
            if sub:
                pt = [r['mean_persist_transport'] for r in sub]
                ls = [r['Lambda'] for r in sub]
                print(f"    db={db}: n={len(sub)}, persist=[{min(pt):.4f},{max(pt):.4f}], "
                      f"Lambda=[{min(ls):.5f},{max(ls):.5f}]")

        # P-Unified-2: Depth vs Lambda
        print(f"\n--- P-Unified-2: Core depth vs Lambda ---")
        depths_mean = [np.mean([d['mean_depth'] for d in r['depths']]) for r in valid if 'depths' in r]
        lambdas_d = [r['Lambda'] for r in valid if 'depths' in r]
        if len(depths_mean) > 2 and len(lambdas_d) > 2:
            corr_depth = np.corrcoef(lambdas_d, depths_mean)[0, 1]
            print(f"  Corr(Lambda, mean_depth) = {corr_depth:.3f}")

    # Save
    output = {
        'experiment': 'exp50_unified_transport',
        'description': 'P-Unified-1/2 with transport-based persist + baseline',
        'grid_configs': [g for g, _ in grid_configs],
        'delta_betas': delta_betas,
        'lrep_values': lrep_values,
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp50_unified_transport.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {outpath}")
    print(f"Total time: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
