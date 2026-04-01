#!/usr/bin/env python3
"""Experiment 46: Weak-to-Strong Regime Transition

Varies overlap ratio between K=2 formations by adjusting spatial positions.
Measures transition in persistence mechanism as overlap increases.

Key questions:
1. Is the transition smooth or sharp?
2. How does Hessian structure change across the boundary?
3. At what overlap ratio does μ_joint → 0?
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, project_volume
from scc.multi import (
    find_k_formations, inter_formation_distances, formation_overlap,
    classify_regime, transport_k_formations,
)
from scc.diagnostics import compute_diagnostics

# ── Configuration ─────────────────────────────────────────────────────────
RNG_SEED = 42
GRID = (20, 20)
K = 2
BETA = 50.0
VOLUME_FRACTION = 0.15
# Overlap control: vary separation from touching to deep overlap
SEPARATIONS = list(range(1, 11))  # distance in grid units between seeds
LAMBDA_REPS = [1.0, 5.0, 10.0, 20.0]
N_TRIALS = 3


def make_params(**overrides):
    defaults = dict(beta_bd=BETA, volume_fraction=VOLUME_FRACTION,
                    n_restarts=3, max_iter=2000)
    defaults.update(overrides)
    return ParameterRegistry(**defaults)


def place_formations(rows, cols, separation, rng):
    """Place K=2 formation seeds with controlled separation along x-axis."""
    n = rows * cols
    mid_row = rows // 2
    mid_col = cols // 2
    offset = separation // 2

    fields = []
    for fid in range(2):
        u = np.zeros(n)
        center_col = mid_col - offset + fid * separation
        center_col = max(2, min(cols - 3, center_col))
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                dist_sq = (i - mid_row)**2 + (j - center_col)**2
                u[idx] = 0.8 * np.exp(-dist_sq / 3.5)
        m = VOLUME_FRACTION * n
        u = project_volume(u, m)
        fields.append(u)
    return fields


def hessian_structure_analysis(fields, graph, params, lambda_rep):
    """Analyze joint Hessian structure at the K-formation minimizer.

    Returns dict with:
    - per_formation_mu: list of per-formation spectral gaps
    - mu_joint_weyl: Weyl lower bound on joint spectral gap
    - coupling_norm: ||V_{jk}|| = lambda_rep (for uniform repulsion)
    - off_diag_energy: cross-energy contribution
    """
    K = len(fields)
    ec = EnergyComputer(graph, params)
    n = graph.n
    eps = 1e-4

    per_mu = []
    for k in range(K):
        u = fields[k]
        e0 = ec.total_energy(u)
        min_curv = np.inf
        rng = np.random.RandomState(42 + k)
        n_dirs = min(30, n)
        for _ in range(n_dirs):
            v = rng.randn(n)
            v -= v.mean()
            v /= np.linalg.norm(v)
            ep = ec.total_energy(project_volume(u + eps * v, u.sum()))
            em = ec.total_energy(project_volume(u - eps * v, u.sum()))
            curv = (ep + em - 2 * e0) / eps**2
            min_curv = min(min_curv, curv)
        per_mu.append(float(min_curv))

    # Cross-energy: E_inter = lambda_rep * sum_x u^j(x) * u^k(x)
    cross_energies = []
    for j in range(K):
        for kk in range(j + 1, K):
            e_cross = lambda_rep * float(np.sum(fields[j] * fields[kk]))
            cross_energies.append(e_cross)

    mu_joint_weyl = min(per_mu) - (K - 1) * lambda_rep

    return {
        'per_formation_mu': per_mu,
        'mu_joint_weyl': float(mu_joint_weyl),
        'coupling_norm': float(lambda_rep),
        'cross_energies': cross_energies,
    }


def transport_persistence_test(fields, graph, params, lambda_rep, rng):
    """Test persistence under gentle perturbation."""
    from scipy.sparse import csr_matrix

    n = graph.n
    W_dense = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    noise = rng.uniform(0.95, 1.05, W_dense.shape)
    noise = (noise + noise.T) / 2
    W_pert = W_dense * noise
    np.fill_diagonal(W_pert, 0)
    graph_s = GraphState(csr_matrix(W_pert))

    try:
        transported = transport_k_formations(
            fields, graph, graph_s, params,
            lambda_rep=lambda_rep, mode='correction'
        )
        t_fields = [tr.u_s for tr in transported]

        persist_scores = []
        for k in range(K):
            overlap = np.sum(np.minimum(fields[k], t_fields[k]))
            norm = max(np.sum(fields[k]), np.sum(t_fields[k]))
            persist_scores.append(float(overlap / norm) if norm > 0 else 0.0)

        return {
            'persist_scores': persist_scores,
            'mean_persist': float(np.mean(persist_scores)),
            'converged': True,
        }
    except Exception as e:
        return {
            'persist_scores': [],
            'mean_persist': 0.0,
            'converged': False,
            'error': str(e),
        }


def run_experiment():
    np.random.seed(RNG_SEED)
    rows, cols = GRID
    graph = GraphState.grid_2d(rows, cols)
    n = graph.n
    results = []

    print(f"=== Exp46: Weak-to-Strong Transition on {rows}x{cols} grid ===\n")

    for lambda_rep in LAMBDA_REPS:
        print(f"\n--- λ_rep = {lambda_rep} ---")
        for sep in SEPARATIONS:
            for trial in range(N_TRIALS):
                rng = np.random.RandomState(RNG_SEED + trial * 100 + sep)
                params = make_params()

                init_fields = place_formations(rows, cols, sep, rng)

                try:
                    formation_results = find_k_formations(
                        graph, params, K=K, lambda_rep=lambda_rep,
                        init_fields=init_fields, max_iter=2000
                    )
                    fields = [fr.u for fr in formation_results]

                    # Metrics
                    D = inter_formation_distances(fields, graph)
                    d_min = float(D[0, 1])

                    O = formation_overlap(fields)
                    overlap_01 = float(O[0, 1])
                    min_core = min(float(O[0, 0]), float(O[1, 1]))
                    overlap_ratio = overlap_01 / max(min_core, 1.0)

                    regime = classify_regime(fields, graph)

                    # Hessian analysis
                    hess = hessian_structure_analysis(fields, graph, params, lambda_rep)

                    # Transport persistence
                    transport = transport_persistence_test(fields, graph, params, lambda_rep, rng)

                    result = {
                        'separation': sep,
                        'lambda_rep': lambda_rep,
                        'trial': trial,
                        'd_min': d_min,
                        'overlap_ratio': overlap_ratio,
                        'overlap_count': overlap_01,
                        'regime': regime,
                        'hessian': hess,
                        'transport': transport,
                    }
                    results.append(result)

                    tag = regime[:4].upper()
                    print(f"  sep={sep:2d} trial={trial}: d_min={d_min:.0f} "
                          f"overlap={overlap_ratio:.3f} regime={tag} "
                          f"μ_joint={hess['mu_joint_weyl']:.2f} "
                          f"persist={transport['mean_persist']:.3f}")

                except Exception as e:
                    print(f"  sep={sep:2d} trial={trial}: ERROR {e}")
                    results.append({
                        'separation': sep, 'lambda_rep': lambda_rep,
                        'trial': trial, 'error': str(e),
                    })

    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'results',
                            'exp46_weak_to_strong_transition.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {len(results)} results to {out_path}")

    # Summary: find crossover points
    print("\n=== Crossover Summary ===")
    for lambda_rep in LAMBDA_REPS:
        lr_results = [r for r in results if r.get('lambda_rep') == lambda_rep
                     and 'error' not in r]
        if not lr_results:
            continue
        print(f"\nλ_rep = {lambda_rep}:")

        # Group by separation
        by_sep = {}
        for r in lr_results:
            s = r['separation']
            if s not in by_sep:
                by_sep[s] = []
            by_sep[s].append(r)

        for s in sorted(by_sep.keys()):
            rr = by_sep[s]
            avg_overlap = np.mean([r['overlap_ratio'] for r in rr])
            avg_mu = np.mean([r['hessian']['mu_joint_weyl'] for r in rr])
            avg_persist = np.mean([r['transport']['mean_persist'] for r in rr])
            regimes = [r['regime'] for r in rr]
            dominant = max(set(regimes), key=regimes.count)
            print(f"  sep={s:2d}: overlap={avg_overlap:.3f} μ_joint={avg_mu:.2f} "
                  f"persist={avg_persist:.3f} regime={dominant}")


if __name__ == '__main__':
    t0 = time.time()
    run_experiment()
    print(f"\nTotal time: {time.time() - t0:.1f}s")
