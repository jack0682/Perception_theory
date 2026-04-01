#!/usr/bin/env python3
"""Experiment 47: Full Phase Diagram + Near-Bifurcation Behavior

Systematic sweep over (d_min, μ, overlap) to produce the 2D/3D phase diagram
showing all three regimes: well-separated, weakly-interacting, strongly-interacting.

Also probes near-bifurcation behavior where μ_joint → 0.

Output:
- Phase diagram data (d_min vs λ_rep colored by regime)
- Persistence basin boundary map
- Near-bifurcation persistence measurements
- Comparison of theoretical vs experimental boundaries
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
GRID = (15, 15)
K = 2
VOLUME_FRACTION = 0.15

# Sweep parameters
BETAS = [20.0, 35.0, 50.0, 75.0]           # phase separation strength
LAMBDA_REPS = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]  # repulsion strength
SEPARATIONS = list(range(1, 8))              # formation seed distance
N_TRIALS = 2  # per config


def make_params(beta=50.0, **overrides):
    defaults = dict(beta_bd=beta, volume_fraction=VOLUME_FRACTION,
                    n_restarts=3, max_iter=2000)
    defaults.update(overrides)
    return ParameterRegistry(**defaults)


def place_formations(rows, cols, separation):
    """Place K=2 seeds with controlled separation."""
    n = rows * cols
    fields = []
    mid_row = rows // 2
    mid_col = cols // 2
    offset = separation // 2
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


def estimate_spectral_gap(fields, graph, params, lambda_rep):
    """Quick spectral gap estimate via random curvature probing."""
    ec = EnergyComputer(graph, params)
    n = graph.n
    eps = 1e-4
    per_mu = []
    for k in range(len(fields)):
        u = fields[k]
        e0 = ec.total_energy(u)
        min_curv = np.inf
        rng = np.random.RandomState(42 + k)
        for _ in range(min(15, n)):
            v = rng.randn(n)
            v -= v.mean()
            v /= np.linalg.norm(v)
            ep = ec.total_energy(project_volume(u + eps * v, u.sum()))
            em = ec.total_energy(project_volume(u - eps * v, u.sum()))
            curv = (ep + em - 2 * e0) / eps**2
            min_curv = min(min_curv, curv)
        per_mu.append(float(min_curv))
    mu_joint = min(per_mu) - (len(fields) - 1) * lambda_rep
    return mu_joint, per_mu


def persistence_test(fields, graph, params, lambda_rep, rng):
    """Quick persistence test under gentle perturbation."""
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
        for k in range(len(fields)):
            overlap = np.sum(np.minimum(fields[k], t_fields[k]))
            norm = max(np.sum(fields[k]), np.sum(t_fields[k]))
            persist_scores.append(float(overlap / norm) if norm > 0 else 0.0)
        return float(np.mean(persist_scores)), True
    except Exception:
        return 0.0, False


def run_experiment():
    np.random.seed(RNG_SEED)
    rows, cols = GRID
    graph = GraphState.grid_2d(rows, cols)
    n = graph.n
    results = []
    total_configs = len(BETAS) * len(LAMBDA_REPS) * len(SEPARATIONS) * N_TRIALS
    done = 0

    print(f"=== Exp47: Phase Diagram on {rows}x{cols} grid ===")
    print(f"Total configs: {total_configs}\n")

    for beta in BETAS:
        params = make_params(beta=beta)
        for lambda_rep in LAMBDA_REPS:
            for sep in SEPARATIONS:
                for trial in range(N_TRIALS):
                    done += 1
                    rng = np.random.RandomState(RNG_SEED + trial * 1000 + sep * 10)

                    init_fields = place_formations(rows, cols, sep)

                    try:
                        formation_results = find_k_formations(
                            graph, params, K=K, lambda_rep=lambda_rep,
                            init_fields=init_fields, max_iter=2000
                        )
                        fields = [fr.u for fr in formation_results]

                        D = inter_formation_distances(fields, graph)
                        d_min = float(D[0, 1])

                        O = formation_overlap(fields)
                        overlap_01 = float(O[0, 1])
                        min_core = min(float(O[0, 0]), float(O[1, 1]))
                        overlap_ratio = overlap_01 / max(min_core, 1.0)

                        regime = classify_regime(fields, graph)

                        mu_joint, per_mu = estimate_spectral_gap(
                            fields, graph, params, lambda_rep
                        )

                        persist, persist_ok = persistence_test(
                            fields, graph, params, lambda_rep, rng
                        )

                        # Compute λ_coupling proxy (to be refined after Task #4)
                        # Preliminary: λ_coupling = (K-1)*λ_rep / min(μ_k)
                        mu_min = min(per_mu) if per_mu else 1.0
                        lambda_coupling = (K - 1) * lambda_rep / max(mu_min, 1e-6)

                        result = {
                            'beta': beta,
                            'lambda_rep': lambda_rep,
                            'separation': sep,
                            'trial': trial,
                            'd_min': d_min,
                            'overlap_ratio': overlap_ratio,
                            'regime': regime,
                            'mu_joint': float(mu_joint),
                            'per_mu': [float(m) for m in per_mu],
                            'lambda_coupling': float(lambda_coupling),
                            'persist': persist,
                            'persist_ok': persist_ok,
                        }
                        results.append(result)

                        if done % 20 == 0 or done == total_configs:
                            print(f"  [{done}/{total_configs}] β={beta} λ_rep={lambda_rep} "
                                  f"sep={sep}: regime={regime[:4]} μ={mu_joint:.1f} "
                                  f"persist={persist:.3f}")

                    except Exception as e:
                        results.append({
                            'beta': beta, 'lambda_rep': lambda_rep,
                            'separation': sep, 'trial': trial,
                            'error': str(e),
                        })
                        done += 0  # already counted

    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'results',
                            'exp47_phase_diagram.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {len(results)} results to {out_path}")

    # Phase diagram summary
    print("\n=== Phase Diagram Summary ===")
    valid = [r for r in results if 'error' not in r]

    # Group by (beta, lambda_rep) → boundary sep
    print("\nBoundary sep (first all-sep) by (β, λ_rep):")
    print(f"{'β':>6} {'λ_rep':>8} {'boundary':>10} {'avg_persist_sep':>16} {'avg_persist_weak':>16}")
    for beta in BETAS:
        for lambda_rep in LAMBDA_REPS:
            subset = [r for r in valid if r['beta'] == beta
                     and r['lambda_rep'] == lambda_rep]
            if not subset:
                continue

            by_sep = {}
            for r in subset:
                s = r['separation']
                if s not in by_sep:
                    by_sep[s] = []
                by_sep[s].append(r)

            boundary = '-'
            for s in sorted(by_sep.keys()):
                if all(r['regime'] == 'well-separated' for r in by_sep[s]):
                    boundary = str(s)
                    break

            sep_persist = [r['persist'] for r in subset if r['regime'] == 'well-separated']
            weak_persist = [r['persist'] for r in subset if r['regime'] == 'weakly-interacting']
            avg_sep = f"{np.mean(sep_persist):.3f}" if sep_persist else '-'
            avg_weak = f"{np.mean(weak_persist):.3f}" if weak_persist else '-'

            print(f"{beta:6.0f} {lambda_rep:8.1f} {boundary:>10} {avg_sep:>16} {avg_weak:>16}")

    # Near-bifurcation analysis
    print("\n=== Near-Bifurcation (μ_joint near 0) ===")
    near_bif = [r for r in valid if abs(r['mu_joint']) < 5.0]
    if near_bif:
        for r in sorted(near_bif, key=lambda x: x['mu_joint']):
            print(f"  β={r['beta']:.0f} λ_rep={r['lambda_rep']:.1f} sep={r['separation']} "
                  f"μ_joint={r['mu_joint']:.2f} regime={r['regime'][:4]} "
                  f"persist={r['persist']:.3f}")
    else:
        print("  No configs with μ_joint near 0 found.")


if __name__ == '__main__':
    t0 = time.time()
    run_experiment()
    print(f"\nTotal time: {time.time() - t0:.1f}s")
