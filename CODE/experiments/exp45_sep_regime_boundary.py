#!/usr/bin/env python3
"""Experiment 45: Sep Regime Boundary Verification

Systematically varies d_min between K=2 formations on 15x15 and 20x20 grids
to map where the T-Persist-K-Sep condition threshold changes.

Measures: persistence, spectral gap (μ_joint), repulsion strength, d_min.
Predicts: sharp boundary at d_min = D_sep where well-separated regime begins.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, project_volume, FormationResult
from scc.multi import (
    find_k_formations, inter_formation_distances, formation_overlap,
    classify_regime, transport_k_formations,
)
from scc.diagnostics import compute_diagnostics

# ── Configuration ─────────────────────────────────────────────────────────
RNG_SEED = 42
GRIDS = [(15, 15), (20, 20)]
K = 2
BETA = 50.0
VOLUME_FRACTION = 0.15  # per formation (total 0.30 for K=2)
LAMBDA_REPS = [1.0, 5.0, 10.0]
# d_min is controlled by spatial initialization offset between formations
# We vary the separation gap by placing formation seeds at different distances
N_TRIALS = 3  # trials per config for robustness


def make_params(**overrides):
    defaults = dict(beta_bd=BETA, volume_fraction=VOLUME_FRACTION,
                    n_restarts=3, max_iter=2000)
    defaults.update(overrides)
    return ParameterRegistry(**defaults)


def place_k2_seeds(rows, cols, separation):
    """Create K=2 init fields with controlled inter-formation distance.

    Places two Gaussian bumps at (rows//4, cols//2) and (rows//4 + separation, cols//2).
    Returns list of two initial fields.
    """
    n = rows * cols
    cx, cy = cols // 2, rows // 4  # center of formation 1

    fields = []
    for fid in range(2):
        u = np.zeros(n)
        center_row = rows // 4 + fid * separation
        center_col = cols // 2
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                dist_sq = (i - center_row)**2 + (j - center_col)**2
                u[idx] = 0.8 * np.exp(-dist_sq / 4.0)
        # Project to volume constraint
        m = VOLUME_FRACTION * n
        u = project_volume(u, m)
        fields.append(u)
    return fields


def compute_hessian_spectral_gap(fields, graph, params, lambda_rep):
    """Compute the minimum eigenvalue of the joint Hessian (approximate).

    Uses per-formation Hessian + repulsion coupling.
    Returns μ_joint estimate.
    """
    K = len(fields)
    mus = []
    for k in range(K):
        ec = EnergyComputer(graph, params)
        # Approximate μ_k via finite-difference Hessian smallest eigenvalue
        u = fields[k]
        n = len(u)
        if n > 100:
            # Too expensive for full Hessian; use energy curvature estimate
            e0 = ec.total_energy(u)
            eps = 1e-4
            min_curv = np.inf
            # Sample random directions on tangent space
            rng = np.random.RandomState(42 + k)
            for _ in range(min(20, n)):
                v = rng.randn(n)
                v -= v.mean()  # project to tangent space
                v /= np.linalg.norm(v)
                ep = ec.total_energy(project_volume(u + eps * v, u.sum()))
                em = ec.total_energy(project_volume(u - eps * v, u.sum()))
                curv = (ep + em - 2 * e0) / eps**2
                min_curv = min(min_curv, curv)
            mus.append(min_curv)
        else:
            mus.append(1.0)  # placeholder for tiny grids

    # Weyl bound: μ_joint ≥ min_k(μ_k) - (K-1)*λ_rep
    mu_min = min(mus)
    mu_joint = mu_min - (K - 1) * lambda_rep
    return mu_joint, mus


def perturb_graph(graph, epsilon=0.05, rng=None):
    """Create a gently perturbed graph (simulating temporal transition)."""
    if rng is None:
        rng = np.random.RandomState(99)
    # Perturb node positions slightly (for grid graphs, this means
    # small weight changes)
    n = graph.n
    W_dense = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    noise = rng.uniform(1.0 - epsilon, 1.0 + epsilon, W_dense.shape)
    noise = (noise + noise.T) / 2  # symmetrize
    W_perturbed = W_dense * noise
    np.fill_diagonal(W_perturbed, 0)
    # Create new graph
    from scipy.sparse import csr_matrix
    return GraphState(csr_matrix(W_perturbed))


def run_experiment():
    np.random.seed(RNG_SEED)
    results = []

    for rows, cols in GRIDS:
        graph = GraphState.grid_2d(rows, cols)
        n = graph.n

        # Vary separation from 1 (overlapping) to rows//2 (well-separated)
        max_sep = rows // 2
        separations = list(range(1, max_sep + 1))

        for lambda_rep in LAMBDA_REPS:
            for sep in separations:
                for trial in range(N_TRIALS):
                    rng = np.random.RandomState(RNG_SEED + trial * 100 + sep)
                    params = make_params()

                    # Initialize with controlled separation
                    init_fields = place_k2_seeds(rows, cols, sep)

                    try:
                        # Find K=2 formations
                        formation_results = find_k_formations(
                            graph, params, K=K, lambda_rep=lambda_rep,
                            init_fields=init_fields, max_iter=2000
                        )
                        fields = [fr.u for fr in formation_results]

                        # Measure actual d_min
                        D = inter_formation_distances(fields, graph)
                        d_min_actual = float(D[0, 1])

                        # Classify regime
                        regime = classify_regime(fields, graph)

                        # Overlap
                        O = formation_overlap(fields)
                        overlap_ratio = float(O[0, 1]) / max(float(O[0, 0]), float(O[1, 1]), 1.0)

                        # Spectral gap estimate
                        mu_joint, per_mus = compute_hessian_spectral_gap(
                            fields, graph, params, lambda_rep
                        )

                        # Persistence test: perturb graph and transport
                        graph_s = perturb_graph(graph, epsilon=0.05, rng=rng)
                        try:
                            transported = transport_k_formations(
                                fields, graph, graph_s, params,
                                lambda_rep=lambda_rep, mode='correction'
                            )
                            t_fields = [tr.u_s for tr in transported]

                            # Persistence metric: overlap between original and transported
                            persist_scores = []
                            for k in range(K):
                                overlap = np.sum(np.minimum(fields[k], t_fields[k]))
                                norm = max(np.sum(fields[k]), np.sum(t_fields[k]))
                                persist_scores.append(float(overlap / norm) if norm > 0 else 0.0)
                            mean_persist = np.mean(persist_scores)
                            transport_ok = True
                        except Exception as e:
                            mean_persist = 0.0
                            transport_ok = False

                        # Diagnostics per formation
                        diag_list = []
                        for k in range(K):
                            d = compute_diagnostics(fields[k], graph, params)
                            diag_list.append({
                                'Bind': float(d.Bind),
                                'Sep': float(d.Sep),
                                'Inside': float(d.Inside),
                            })

                        result = {
                            'grid': f'{rows}x{cols}',
                            'n': n,
                            'target_sep': sep,
                            'd_min_actual': d_min_actual,
                            'lambda_rep': lambda_rep,
                            'trial': trial,
                            'regime': regime,
                            'overlap_ratio': overlap_ratio,
                            'mu_joint': float(mu_joint),
                            'per_formation_mu': [float(m) for m in per_mus],
                            'mean_persist': mean_persist,
                            'transport_ok': transport_ok,
                            'diagnostics': diag_list,
                        }
                        results.append(result)

                        tag = "SEP" if regime == 'well-separated' else ("WEAK" if regime == 'weakly-interacting' else "STRONG")
                        print(f"[{rows}x{cols}] sep={sep} λ_rep={lambda_rep} trial={trial}: "
                              f"d_min={d_min_actual:.0f} regime={tag} "
                              f"μ_joint={mu_joint:.2f} persist={mean_persist:.3f}")

                    except Exception as e:
                        print(f"[{rows}x{cols}] sep={sep} λ_rep={lambda_rep} trial={trial}: ERROR {e}")
                        results.append({
                            'grid': f'{rows}x{cols}',
                            'target_sep': sep,
                            'lambda_rep': lambda_rep,
                            'trial': trial,
                            'error': str(e),
                        })

    # Save results
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'exp45_sep_regime_boundary.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {len(results)} results to {out_path}")

    # Summary: boundary analysis
    print("\n=== Sep Regime Boundary Summary ===")
    for rows, cols in GRIDS:
        for lambda_rep in LAMBDA_REPS:
            grid_results = [r for r in results if r.get('grid') == f'{rows}x{cols}'
                           and r.get('lambda_rep') == lambda_rep and 'error' not in r]
            if not grid_results:
                continue
            # Find transition point
            sep_regimes = {}
            for r in grid_results:
                s = r['target_sep']
                if s not in sep_regimes:
                    sep_regimes[s] = []
                sep_regimes[s].append(r['regime'])

            boundary = None
            for s in sorted(sep_regimes.keys()):
                regimes = sep_regimes[s]
                if all(r == 'well-separated' for r in regimes):
                    boundary = s
                    break

            print(f"\n{rows}x{cols}, λ_rep={lambda_rep}:")
            print(f"  Boundary d_min (first all-sep): {boundary}")
            for s in sorted(sep_regimes.keys()):
                counts = {}
                for r in sep_regimes[s]:
                    counts[r] = counts.get(r, 0) + 1
                print(f"  sep={s}: {counts}")


if __name__ == '__main__':
    t0 = time.time()
    run_experiment()
    print(f"\nTotal time: {time.time() - t0:.1f}s")
