#!/usr/bin/env python3
"""Experiment 29: λ_tr Sweep — Fixed-Point Multiplicity in Transport Iteration

Tests whether the self-referential fixed-point iteration in transport_fixed_point
produces multiple distinct fixed points when started from different initializations.

Theory context:
- Weak regime (small λ_tr): Φ is a contraction → unique fixed point
- Strong regime (large λ_tr): Schauder guarantees existence, uniqueness is open
- This experiment sweeps λ_tr and tests 5 different initializations per config

For each (grid, λ_tr), we:
1. Find a formation u* via find_formation
2. Run a custom fixed-point loop from 5 different starting points:
   (a) u_s^0 = u* (default, same as transport_fixed_point)
   (b) u_s^0 = uniform field (m/n everywhere)
   (c) u_s^0 = anti-correlated (1 - u*, re-projected to Σ_m)
   (d) u_s^0 = random field (projected to Σ_m)
   (e) u_s^0 = spatially shifted u* (rolled by ~grid_width/4)
3. Cluster converged fields by L2 distance; report distinct fixed points
"""
import sys, os, time, json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot, transport_field,
)

# ── Configuration ──────────────────────────────────────────────────────────
GRIDS = [(10, 10), (15, 15)]
BETA = 50.0
VOLUME_FRACTION = 0.3
LAMBDA_TR_VALUES = np.logspace(-2, 1, 12)  # 0.01 to 10, 12 points
SIGMA = 1.0
GAMMA = 1.0
EPS_OT = 1.0
MAX_FP_ITER = 25
FP_TOL = 1e-4
DISTINCT_THRESHOLD = 0.05  # L2/sqrt(n) threshold for "distinct" fields
N_RESTARTS = 3
RNG_SEED = 42


def make_params():
    return ParameterRegistry(
        beta_bd=BETA, volume_fraction=VOLUME_FRACTION,
        n_restarts=N_RESTARTS, max_iter=2000,
    )


def custom_fixed_point(u_t, u_s_init, graph, params,
                       sigma=SIGMA, gamma=GAMMA, eps_ot=EPS_OT,
                       lambda_tr=0.1, max_iter=MAX_FP_ITER, tol=FP_TOL):
    """Run fixed-point iteration from a custom u_s^0 initialization.

    Mimics transport_fixed_point but allows arbitrary starting field.
    """
    n = graph.n
    u_s = u_s_init.copy()
    dist_matrix = graph_distance_matrix(graph)
    phi_t = cohesion_fingerprint(u_t, graph, params)

    fp_residuals = []
    M = np.zeros((n, n))
    cost = np.zeros((n, n))
    converged = False
    iterations = 0

    for k in range(1, max_iter + 1):
        iterations = k

        # Fingerprint at current u_s
        phi_s = cohesion_fingerprint(u_s, graph, params)

        # Transport cost
        cost = transport_cost(phi_t, phi_s, dist_matrix, sigma, gamma)

        # OT plan
        M, _info = sinkhorn_partial_ot(cost, u_t, u_s, eps_ot)

        # Transported field
        u_transported = transport_field(M, u_s)

        # Re-optimize with transport as warm start
        result = find_formation(graph, params, u_init=u_transported)
        u_s_new = result.u

        # Convergence check
        norm_u_s = np.linalg.norm(u_s)
        residual = np.linalg.norm(u_s_new - u_s) / max(norm_u_s, 1e-12)
        fp_residuals.append(float(residual))

        u_s = u_s_new
        if residual < tol:
            converged = True
            break

    transport_energy = float(lambda_tr * np.sum(M * cost))
    return {
        'u_s': u_s,
        'converged': converged,
        'iterations': iterations,
        'fp_residuals': fp_residuals,
        'transport_energy': transport_energy,
    }


def make_initializations(u_star, graph, params, rng):
    """Generate 5 different starting fields for the fixed-point iteration."""
    n = graph.n
    m = u_star.sum()  # target volume

    inits = {}

    # (a) Default: u_s^0 = u* (same as transport_fixed_point)
    inits['default'] = u_star.copy()

    # (b) Uniform field: m/n everywhere
    inits['uniform'] = np.full(n, m / n)

    # (c) Anti-correlated: 1 - u*, re-projected to Σ_m
    anti = 1.0 - u_star
    inits['anti'] = project_volume(anti, m)

    # (d) Random field projected to Σ_m
    rand_field = rng.random(n)
    inits['random'] = project_volume(rand_field, m)

    # (e) Spatially shifted: roll by grid_width/4
    grid_w = int(np.sqrt(n))
    shift = max(grid_w // 4, 1)
    shifted = np.roll(u_star, shift)
    inits['shifted'] = project_volume(shifted, m)

    return inits


def cluster_fields(fields, threshold=DISTINCT_THRESHOLD):
    """Count distinct fields by pairwise L2/sqrt(n) distance."""
    if not fields:
        return 0, []

    n = len(fields[0])
    sqrt_n = np.sqrt(n)
    clusters = []

    for f in fields:
        found = False
        for c in clusters:
            dist = np.linalg.norm(f - c[0]) / sqrt_n
            if dist < threshold:
                c.append(f)
                found = True
                break
        if not found:
            clusters.append([f])

    return len(clusters), clusters


def run_experiment():
    rng = np.random.default_rng(RNG_SEED)
    params = make_params()
    results = []

    print("=" * 75)
    print("Experiment 29: λ_tr Sweep — Fixed-Point Multiplicity")
    print("=" * 75)
    print(f"Grids: {GRIDS}")
    print(f"β = {BETA}, volume_fraction = {VOLUME_FRACTION}")
    print(f"λ_tr range: {LAMBDA_TR_VALUES[0]:.3f} — {LAMBDA_TR_VALUES[-1]:.1f} ({len(LAMBDA_TR_VALUES)} values)")
    print(f"Distinct threshold: {DISTINCT_THRESHOLD}")
    print()

    for gw, gh in GRIDS:
        n = gw * gh
        print(f"\n{'='*75}")
        print(f"Grid: {gw}x{gh} (n={n})")
        print(f"{'='*75}")

        graph = GraphState.grid_2d(gw, gh)

        # Find base formation
        t0 = time.time()
        base_result = find_formation(graph, params)
        u_star = base_result.u
        t_base = time.time() - t0
        print(f"Base formation: E={base_result.energy:.4f}, "
              f"core={np.sum(u_star >= 0.8)}, time={t_base:.1f}s")

        # Generate initializations
        inits = make_initializations(u_star, graph, params, rng)

        for ltr in LAMBDA_TR_VALUES:
            print(f"\n  λ_tr = {ltr:.4f}")
            t_start = time.time()

            converged_fields = []
            init_details = []

            for init_name, u_s0 in inits.items():
                try:
                    res = custom_fixed_point(
                        u_t=u_star, u_s_init=u_s0, graph=graph, params=params,
                        lambda_tr=ltr,
                    )
                    converged_fields.append(res['u_s'])
                    detail = {
                        'init': init_name,
                        'converged': res['converged'],
                        'iterations': res['iterations'],
                        'transport_energy': res['transport_energy'],
                        'final_residual': res['fp_residuals'][-1] if res['fp_residuals'] else float('nan'),
                    }
                except Exception as e:
                    detail = {'init': init_name, 'error': str(e)}
                    converged_fields.append(None)

                init_details.append(detail)

            # Filter out failed runs
            valid_fields = [f for f in converged_fields if f is not None]
            n_distinct, clusters = cluster_fields(valid_fields)

            elapsed = time.time() - t_start

            # Pairwise distances for detail
            pairwise = []
            names = [d['init'] for d in init_details if 'error' not in d]
            for i in range(len(valid_fields)):
                for j in range(i + 1, len(valid_fields)):
                    dist = np.linalg.norm(valid_fields[i] - valid_fields[j]) / np.sqrt(n)
                    pairwise.append((names[i], names[j], dist))

            max_dist = max((d for _, _, d in pairwise), default=0.0)

            entry = {
                'grid': f'{gw}x{gh}',
                'lambda_tr': float(ltr),
                'n_distinct': n_distinct,
                'n_valid': len(valid_fields),
                'max_pairwise_dist': float(max_dist),
                'elapsed': float(elapsed),
                'details': init_details,
            }
            results.append(entry)

            status = "MULTIPLE" if n_distinct > 1 else "unique"
            conv_str = "/".join(
                ("Y" if d.get('converged', False) else "N")
                for d in init_details if 'error' not in d
            )
            print(f"    distinct={n_distinct}/{len(valid_fields)}, "
                  f"max_dist={max_dist:.4f}, conv=[{conv_str}], "
                  f"time={elapsed:.1f}s  {'*** ' + status if n_distinct > 1 else status}")

            # Print pairwise distances if multiplicity detected
            if n_distinct > 1:
                for ni, nj, d in pairwise:
                    marker = " <-- DISTINCT" if d >= DISTINCT_THRESHOLD else ""
                    print(f"      {ni} vs {nj}: {d:.4f}{marker}")

    # ── Summary Table ──────────────────────────────────────────────────────
    print("\n\n" + "=" * 75)
    print("SUMMARY TABLE")
    print("=" * 75)
    print(f"{'Grid':<8} {'λ_tr':>8} {'Distinct':>8} {'MaxDist':>10} {'Conv':>6} {'Time':>6}")
    print("-" * 52)
    for r in results:
        conv_count = sum(1 for d in r['details'] if d.get('converged', False))
        print(f"{r['grid']:<8} {r['lambda_tr']:>8.4f} "
              f"{r['n_distinct']:>4}/{r['n_valid']:<3} "
              f"{r['max_pairwise_dist']:>10.4f} "
              f"{conv_count:>3}/{r['n_valid']:<2} "
              f"{r['elapsed']:>5.1f}s")

    # ── Multiplicity verdict ───────────────────────────────────────────────
    multi_cases = [r for r in results if r['n_distinct'] > 1]
    print(f"\n{'='*75}")
    if multi_cases:
        print(f"MULTIPLICITY DETECTED in {len(multi_cases)} configurations:")
        for r in multi_cases:
            print(f"  grid={r['grid']}, λ_tr={r['lambda_tr']:.4f}, "
                  f"distinct={r['n_distinct']}, max_dist={r['max_pairwise_dist']:.4f}")
    else:
        print("NO MULTIPLICITY DETECTED — all initializations converged to the same field")
        print("(within L2/√n threshold of {:.3f})".format(DISTINCT_THRESHOLD))
    print("=" * 75)

    # ── Contraction analysis ───────────────────────────────────────────────
    print("\nCONTRACTION ANALYSIS (convergence rate vs λ_tr):")
    for r in results:
        default_detail = next((d for d in r['details'] if d.get('init') == 'default'), None)
        if default_detail and default_detail.get('converged'):
            print(f"  grid={r['grid']}, λ_tr={r['lambda_tr']:.4f}: "
                  f"iters={default_detail['iterations']}, "
                  f"final_res={default_detail['final_residual']:.2e}")

    # ── Save JSON ──────────────────────────────────────────────────────────
    out_path = os.path.join(os.path.dirname(__file__), 'exp29_results.json')
    # Convert for JSON serialization
    for r in results:
        for d in r['details']:
            for k, v in d.items():
                if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
                    d[k] = str(v)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    run_experiment()
