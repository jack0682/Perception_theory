#!/usr/bin/env python3
"""SCC Experiment Suite — Iteration 8

Runs all 4 priority experiments:
1. λ_sep/λ_bd sweep (110 runs) — resolves R10
2. Phase transition verification (β sweep around β_crit)
3. Energy ablation (6 configs)
4. Formation quality on grids (5×5, 10×10, 20×20)
"""
import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer, double_well_second_deriv
from scc.diagnostics import compute_diagnostics


def run_single(graph, params, normalize=False, skip_validation=False):
    """Run formation finding, return key metrics dict."""
    if skip_validation:
        # Bypass validation for experiments that intentionally test sub-critical params
        from scc.optimizer import _optimize_single, FormationResult
        ec = EnergyComputer(graph, params)
        u, E, terms, ehist, ghist, conv, niter = _optimize_single(graph, params, ec, seed=0)
        d = compute_diagnostics(u, graph, params)
        result = FormationResult(u=u, energy=E, energy_terms=terms, diagnostics=d,
                                 converged=conv, n_iter=niter,
                                 energy_history=ehist, grad_norm_history=ghist)
    else:
        try:
            result = find_formation(graph, params, normalize=normalize)
        except ValueError:
            # Validation failure — return degenerate result
            n = graph.n
            u = np.full(n, params.volume_fraction)
            d = compute_diagnostics(u, graph, params)
            return {
                'energy': 0.0, 'E_bd': 0, 'E_cl': 0, 'E_sep': 0,
                'Bind': d.bind, 'Sep': d.sep, 'Inside': d.inside, 'Persist': d.persist,
                'converged': False, 'n_iter': 0,
                'u_min': float(u.min()), 'u_max': float(u.max()), 'u_std': 0.0,
            }
    d = result.diagnostics
    return {
        'energy': result.energy,
        'E_bd': result.energy_terms.get('E_bd', 0),
        'E_cl': result.energy_terms.get('E_cl', 0),
        'E_sep': result.energy_terms.get('E_sep', 0),
        'Bind': d.bind, 'Sep': d.sep, 'Inside': d.inside, 'Persist': d.persist,
        'converged': result.converged, 'n_iter': result.n_iter,
        'u_min': float(result.u.min()), 'u_max': float(result.u.max()),
        'u_std': float(result.u.std()),
    }


def aggregate(seed_results, key):
    vals = [r[key] for r in seed_results]
    return np.mean(vals), np.std(vals)


# ===========================================================================
# EXPERIMENT 1: λ_sep/λ_bd sweep (R10 Resolution)
# ===========================================================================

def experiment_1_sep_bd_sweep():
    print("=" * 70)
    print("EXPERIMENT 1: λ_sep/λ_bd SWEEP (R10 RESOLUTION)")
    print("  10×10 grid, β=20, c=0.5, 11 ratios × 10 seeds = 110 runs")
    print("=" * 70)

    graph = GraphState.grid_2d(10, 10)
    ratios = [0, 1e-4, 1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1000.0, 1e4, 1e5]
    n_seeds = 10
    results = {}
    t0 = time.time()

    for ratio in ratios:
        seed_results = []
        for seed in range(n_seeds):
            params = ParameterRegistry(
                beta_bd=20.0, volume_fraction=0.5,
                w_cl=1.0, w_sep=ratio, w_bd=1.0,
                max_iter=1000, n_restarts=1, dt_init=0.01, eps_init=0.05,
            )
            # Use seed-based restart index via modifying n_restarts behavior
            # Actually, the optimizer uses seed=0..n_restarts-1 internally
            # We just vary the params to get variety
            params_seed = ParameterRegistry(
                beta_bd=20.0, volume_fraction=0.5,
                w_cl=1.0, w_sep=ratio, w_bd=1.0,
                max_iter=1000, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005*seed,  # vary init to get different seeds
            )
            r = run_single(graph, params_seed, normalize=False)
            seed_results.append(r)

        bm, bs = aggregate(seed_results, 'Bind')
        sm, ss = aggregate(seed_results, 'Sep')
        im, ist = aggregate(seed_results, 'Inside')
        em, es = aggregate(seed_results, 'energy')
        um, us = aggregate(seed_results, 'u_std')

        results[ratio] = {
            'Bind_mean': bm, 'Bind_std': bs,
            'Sep_mean': sm, 'Sep_std': ss,
            'Inside_mean': im, 'Inside_std': ist,
            'E_mean': em, 'u_std_mean': um,
        }

        elapsed = time.time() - t0
        print(f"  λ_sep/λ_bd={ratio:>10.4g}: Bind={bm:.3f}±{bs:.3f}  "
              f"Sep={sm:.3f}±{ss:.3f}  Inside={im:.3f}±{ist:.3f}  "
              f"u_std={um:.4f}  [{elapsed:.1f}s]")

    print(f"\nTotal: {time.time()-t0:.1f}s for {len(ratios)*n_seeds} runs")

    # Verdict
    print("\n--- R10 VERDICT ---")
    bd_only = results[0]
    bd_quality = min(bd_only['Bind_mean'], bd_only['Sep_mean'], bd_only['Inside_mean'])
    print(f"BD-only baseline: Bind={bd_only['Bind_mean']:.3f} Sep={bd_only['Sep_mean']:.3f} "
          f"Inside={bd_only['Inside_mean']:.3f} (min={bd_quality:.3f})")

    best_ratio, best_improvement = None, 0
    for ratio in ratios:
        if ratio == 0:
            continue
        r = results[ratio]
        quality = min(r['Bind_mean'], r['Sep_mean'], r['Inside_mean'])
        imp = quality - bd_quality
        if imp > best_improvement:
            best_improvement = imp
            best_ratio = ratio
        # Also check if any term improved significantly
        sep_imp = r['Sep_mean'] - bd_only['Sep_mean']
        if abs(sep_imp) > 0.05:
            print(f"  ratio={ratio:.4g}: Sep Δ={sep_imp:+.3f}, "
                  f"Bind Δ={r['Bind_mean']-bd_only['Bind_mean']:+.3f}, "
                  f"Inside Δ={r['Inside_mean']-bd_only['Inside_mean']:+.3f}")

    if best_improvement > 0.05:
        print(f"\n→ POSITIVE: Best ratio={best_ratio:.4g}, quality Δ=+{best_improvement:.3f}")
        print(f"  Separation IS a genuine contributor.")
    elif best_improvement > 0.01:
        print(f"\n→ MARGINAL: Best ratio={best_ratio:.4g}, quality Δ=+{best_improvement:.3f}")
    else:
        print(f"\n→ NEGATIVE: No ratio improves over pure Allen-Cahn.")

    # P-S1 check: Goldilocks range?
    print("\n--- P-S1 CHECK: Goldilocks range? ---")
    for ratio in [1e-3, 1e-2, 0.1]:
        r = results.get(ratio, {})
        if r:
            q = min(r['Bind_mean'], r['Sep_mean'], r['Inside_mean'])
            print(f"  ratio={ratio:.4g}: min(Bind,Sep,Inside)={q:.3f}")

    return results


# ===========================================================================
# EXPERIMENT 2: Phase Transition Verification
# ===========================================================================

def experiment_2_phase_transition():
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: PHASE TRANSITION VERIFICATION")
    print("=" * 70)

    graph = GraphState.grid_2d(10, 10)
    c = 0.5
    lambda_2 = graph.fiedler
    W_pp = abs(double_well_second_deriv(c))
    # T8-Core: beta_crit = 4*alpha*lambda_2 / |W''(c)|
    beta_crit = 4 * 1.0 * lambda_2 / W_pp
    print(f"  λ₂ = {lambda_2:.4f}, |W''(c)| = {W_pp:.4f}, β_crit = {beta_crit:.4f}")

    multipliers = [0.1, 0.2, 0.5, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0]
    n_seeds = 5
    results = {}
    t0 = time.time()

    for mult in multipliers:
        beta = mult * beta_crit
        seed_results = []
        for seed in range(n_seeds):
            params = ParameterRegistry(
                beta_bd=beta, alpha_bd=1.0, volume_fraction=c,
                w_cl=1.0, w_sep=1.0, w_bd=1.0,
                max_iter=1000, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005*seed,
            )
            r = run_single(graph, params, normalize=False, skip_validation=True)
            seed_results.append(r)

        im, ist = aggregate(seed_results, 'Inside')
        um, us = aggregate(seed_results, 'u_std')
        bm, _ = aggregate(seed_results, 'Bind')
        sm, _ = aggregate(seed_results, 'Sep')

        results[mult] = {
            'beta': beta, 'Inside_mean': im, 'Inside_std': ist,
            'u_std_mean': um, 'Bind_mean': bm, 'Sep_mean': sm,
        }

        elapsed = time.time() - t0
        print(f"  β/β*={mult:5.1f} (β={beta:8.3f}): Inside={im:.3f}±{ist:.3f}  "
              f"u_std={um:.4f}  Bind={bm:.3f}  Sep={sm:.3f}  [{elapsed:.1f}s]")

    print(f"\nTotal: {time.time()-t0:.1f}s")

    # Find transition
    print("\n--- PHASE TRANSITION ANALYSIS ---")
    mults = sorted(results.keys())
    prev_inside = None
    for i, mult in enumerate(mults):
        inside = results[mult]['Inside_mean']
        if prev_inside is not None and prev_inside < 0.3 and inside > 0.3:
            print(f"TRANSITION detected between β/β*={mults[i-1]:.1f} and {mult:.1f}")
            print(f"  Theory predicts transition at β/β*=1.0 (±20% → [0.8, 1.2])")
            if 0.8 <= mults[i-1] <= 1.2 or 0.8 <= mult <= 1.2:
                print(f"  → CONSISTENT with theory (within ±20%)")
            else:
                print(f"  → INCONSISTENT with theory")
        prev_inside = inside

    return results


# ===========================================================================
# EXPERIMENT 3: Energy Ablation (6 configs)
# ===========================================================================

def experiment_3_ablation():
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: ENERGY ABLATION STUDY")
    print("  10×10 grid, β=20, c=0.5, 6 configs × 10 seeds")
    print("=" * 70)

    graph = GraphState.grid_2d(10, 10)
    n_seeds = 10

    configs = {
        'BD-only':      {'w_cl': 0, 'w_sep': 0,  'w_bd': 1},
        'BD+CL':        {'w_cl': 1, 'w_sep': 0,  'w_bd': 1},
        'BD+SEP':       {'w_cl': 0, 'w_sep': 1,  'w_bd': 1},
        'Full-SCC':     {'w_cl': 1, 'w_sep': 1,  'w_bd': 1},
        'SEP-dominant': {'w_cl': 0, 'w_sep': 10, 'w_bd': 1},
        'SEP-only':     {'w_cl': 0, 'w_sep': 1,  'w_bd': 0},
    }

    results = {}
    t0 = time.time()

    for name, weights in configs.items():
        seed_results = []
        for seed in range(n_seeds):
            params = ParameterRegistry(
                beta_bd=20.0, volume_fraction=0.5,
                w_cl=weights['w_cl'], w_sep=weights['w_sep'], w_bd=weights['w_bd'],
                max_iter=1000, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005*seed,
            )
            r = run_single(graph, params, normalize=False)
            seed_results.append(r)

        bm, bs = aggregate(seed_results, 'Bind')
        sm, ss = aggregate(seed_results, 'Sep')
        im, ist = aggregate(seed_results, 'Inside')
        um, _ = aggregate(seed_results, 'u_std')

        results[name] = {
            'Bind_mean': bm, 'Bind_std': bs,
            'Sep_mean': sm, 'Sep_std': ss,
            'Inside_mean': im, 'Inside_std': ist,
            'u_std_mean': um,
            'E_bd_mean': np.mean([r['E_bd'] for r in seed_results]),
            'E_cl_mean': np.mean([r['E_cl'] for r in seed_results]),
            'E_sep_mean': np.mean([r['E_sep'] for r in seed_results]),
        }

        elapsed = time.time() - t0
        print(f"  {name:>15s}: Bind={bm:.3f}  Sep={sm:.3f}  Inside={im:.3f}  "
              f"u_std={um:.4f}  [{elapsed:.1f}s]")

    print(f"\nTotal: {time.time()-t0:.1f}s")

    # Analysis
    print("\n--- ABLATION ANALYSIS ---")
    bd = results['BD-only']
    full = results['Full-SCC']
    for name in ['BD-only', 'BD+CL', 'BD+SEP', 'Full-SCC', 'SEP-dominant', 'SEP-only']:
        r = results[name]
        q = min(r['Bind_mean'], r['Sep_mean'], r['Inside_mean'])
        delta_q = q - min(bd['Bind_mean'], bd['Sep_mean'], bd['Inside_mean'])
        print(f"  {name:>15s}: quality={q:.3f} (Δ={delta_q:+.3f} vs BD-only)")

    sep_only = results['SEP-only']
    if sep_only['Inside_mean'] < 0.3:
        print("\n→ Separation alone CANNOT produce formations. Double-well is essential.")
    else:
        print(f"\n→ Separation alone CAN produce formations (Inside={sep_only['Inside_mean']:.3f})!")

    return results


# ===========================================================================
# EXPERIMENT 4: Formation Quality on Different Grid Sizes
# ===========================================================================

def experiment_4_grid_sizes():
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: FORMATION QUALITY VS GRID SIZE")
    print("  5×5, 10×10, 20×20 grids, β=20, c=0.5, 10 seeds each")
    print("=" * 70)

    grids = [(5, 5), (10, 10), (20, 20)]
    n_seeds = 10
    results = {}
    t0 = time.time()

    for rows, cols in grids:
        graph = GraphState.grid_2d(rows, cols)
        lambda_2 = graph.fiedler
        W_pp = abs(double_well_second_deriv(0.5))
        beta_crit = 4 * 1.0 * lambda_2 / W_pp

        seed_results = []
        for seed in range(n_seeds):
            params = ParameterRegistry(
                beta_bd=20.0, volume_fraction=0.5,
                w_cl=1.0, w_sep=1.0, w_bd=1.0,
                max_iter=1500, n_restarts=1, dt_init=0.01,
                eps_init=0.01 + 0.005*seed,
            )
            r = run_single(graph, params, normalize=False)
            seed_results.append(r)

        bm, bs = aggregate(seed_results, 'Bind')
        sm, ss = aggregate(seed_results, 'Sep')
        im, ist = aggregate(seed_results, 'Inside')
        um, _ = aggregate(seed_results, 'u_std')
        success_rate = np.mean([1.0 if r['Inside'] > 0.5 else 0.0 for r in seed_results])

        key = f"{rows}x{cols}"
        results[key] = {
            'n': rows*cols, 'lambda_2': lambda_2, 'beta_crit': beta_crit,
            'beta_ratio': 20.0/beta_crit,
            'Bind_mean': bm, 'Bind_std': bs,
            'Sep_mean': sm, 'Sep_std': ss,
            'Inside_mean': im, 'Inside_std': ist,
            'u_std_mean': um, 'success_rate': success_rate,
        }

        elapsed = time.time() - t0
        print(f"  {key:>5s} (n={rows*cols:4d}, λ₂={lambda_2:.4f}, β/β*={20.0/beta_crit:.1f}): "
              f"Bind={bm:.3f}  Sep={sm:.3f}  Inside={im:.3f}  "
              f"success={success_rate:.0%}  [{elapsed:.1f}s]")

    print(f"\nTotal: {time.time()-t0:.1f}s")

    # Success criteria
    print("\n--- SUCCESS CRITERIA (I3-R4) ---")
    r10 = results.get('10x10', {})
    if r10:
        checks = [
            ('Bind ≥ 0.9', r10['Bind_mean'] >= 0.9, r10['Bind_mean']),
            ('Sep ≥ 0.8', r10['Sep_mean'] >= 0.8, r10['Sep_mean']),
            ('Inside ≥ 0.5', r10['Inside_mean'] >= 0.5, r10['Inside_mean']),
            ('8/10 seeds', r10['success_rate'] >= 0.8, r10['success_rate']),
        ]
        for label, passed, val in checks:
            status = 'PASS' if passed else 'FAIL'
            print(f"  {label:15s}: {status} ({val:.3f})")

    return results


# ===========================================================================
# MAIN
# ===========================================================================

if __name__ == '__main__':
    print("SCC EXPERIMENT SUITE — ITERATION 8")
    print(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    t_total = time.time()

    r1 = experiment_1_sep_bd_sweep()
    r2 = experiment_2_phase_transition()
    r3 = experiment_3_ablation()
    r4 = experiment_4_grid_sizes()

    total = time.time() - t_total
    print("\n" + "=" * 70)
    print(f"ALL EXPERIMENTS COMPLETE. Total wall time: {total:.1f}s")
    print("=" * 70)
