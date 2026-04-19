#!/usr/bin/env python3
"""Experiment 43: 50x50 scale test — SCC scaling predictions up to n=2500.

Tests formation existence, core/boundary structure, diagnostics, and
transport fixed point across grids from 10x10 to 50x50. Verifies
boundary ratio scaling O(n^{-1/2}).
"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.diagnostics import diagnostic_vector
from scc.transport import transport_fixed_point

BETA = 50.0
VOLUME_FRACTION = 0.3
GRID_SIZES = [10, 15, 20, 30, 40, 50]
MAX_TIME_PER_GRID = 300  # 5 min per grid — skip 50 if 40 exceeds this


def make_params(n, max_iter=2000, n_restarts=1):
    return ParameterRegistry(
        beta_bd=BETA,
        volume_fraction=VOLUME_FRACTION,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=max_iter,
        n_restarts=n_restarts,
        dt_init=0.01,
        eps_init=0.01,
    )


def core_analysis(u, graph):
    """Compute core, deep core, and boundary metrics."""
    n = graph.n
    W_csr = graph.W.tocsr()
    theta = 0.8
    core = u >= theta

    core_size = int(np.sum(core))
    if core_size == 0:
        return {'core_size': 0, 'deep_size': 0, 'boundary_size': 0,
                'deep_ratio': 0.0, 'boundary_ratio': 0.0}

    deep = np.zeros(n, dtype=bool)
    for i in range(n):
        if not core[i]:
            continue
        neighbors = W_csr[i].indices
        if all(core[j] for j in neighbors):
            deep[i] = True
    deep_size = int(np.sum(deep))

    boundary = core & ~deep
    boundary_size = int(np.sum(boundary))

    return {
        'core_size': core_size,
        'deep_size': deep_size,
        'boundary_size': boundary_size,
        'deep_ratio': deep_size / core_size if core_size > 0 else 0.0,
        'boundary_ratio': boundary_size / core_size if core_size > 0 else 0.0,
    }


def run_grid(side, max_iter=2000, n_restarts=1, do_transport=True):
    """Run formation + diagnostics + optional transport for a grid."""
    n = side * side
    print(f"\n{'='*60}")
    print(f"Grid {side}x{side} (n={n})")
    print(f"{'='*60}")

    result = {'side': side, 'n': n}

    # Formation
    t0 = time.time()
    graph = GraphState.grid_2d(side, side)
    params = make_params(n, max_iter=max_iter, n_restarts=n_restarts)
    fr = find_formation(graph, params, verbose=False)
    t_form = time.time() - t0

    u = fr.u
    result['formation'] = {
        'energy': float(fr.energy),
        'energy_terms': {k: float(v) for k, v in fr.energy_terms.items()},
        'converged': fr.converged,
        'n_iter': fr.n_iter,
        'max_u': float(np.max(u)),
        'min_u': float(np.min(u)),
        'std_u': float(np.std(u)),
        'formation_strength': float(np.max(u) - np.min(u)),
        'time_sec': round(t_form, 2),
    }
    print(f"  Formation: E={fr.energy:.4f}, max(u)={np.max(u):.3f}, "
          f"min(u)={np.min(u):.3f}, converged={fr.converged}, "
          f"iters={fr.n_iter}, time={t_form:.1f}s")

    # Core analysis
    ca = core_analysis(u, graph)
    result['core'] = ca
    print(f"  Core: |Core|={ca['core_size']}, |Deep|={ca['deep_size']}, "
          f"|Boundary|={ca['boundary_size']}")
    print(f"  Deep/Core={ca['deep_ratio']:.3f}, Boundary/Core={ca['boundary_ratio']:.3f}")

    # Diagnostics
    dv = diagnostic_vector(u, graph, params)
    result['diagnostics'] = {
        'Bind': float(dv.bind),
        'Sep': float(dv.sep),
        'Inside': float(dv.inside),
        'Persist': float(dv.persist),
        'min_score': float(dv.min_score),
        'mean_score': float(dv.mean_score),
    }
    print(f"  Diagnostics: Bind={dv.bind:.3f} Sep={dv.sep:.3f} "
          f"Inside={dv.inside:.3f} Persist={dv.persist:.3f}")

    # Transport (only for grids <= 30)
    if do_transport:
        t0 = time.time()
        try:
            tr = transport_fixed_point(
                u_t=u, graph=graph, params=params,
                sigma=1.0, gamma=1.0, eps_ot=1.0, lambda_tr=0.1,
                max_fp_iter=20, fp_tol=1e-4,
            )
            t_tr = time.time() - t0
            result['transport'] = {
                'converged': tr.converged,
                'iterations': tr.iterations,
                'transport_energy': float(tr.transport_energy),
                'time_sec': round(t_tr, 2),
            }
            print(f"  Transport: converged={tr.converged}, iters={tr.iterations}, "
                  f"E_tr={tr.transport_energy:.4f}, time={t_tr:.1f}s")
        except Exception as e:
            t_tr = time.time() - t0
            result['transport'] = {'error': str(e), 'time_sec': round(t_tr, 2)}
            print(f"  Transport: ERROR — {e}")
    else:
        result['transport'] = {'skipped': True, 'reason': 'grid too large'}
        print(f"  Transport: skipped (n={n} too large)")

    return result, t_form


def boundary_scaling_fit(results):
    """Fit log(boundary/core) vs log(n) to check O(n^{-1/2}) scaling."""
    ns, ratios = [], []
    for r in results:
        br = r['boundary_scaling']['boundary_over_core']
        if br > 0:
            ns.append(r['n'])
            ratios.append(br)

    if len(ns) < 2:
        return {'error': 'insufficient data points'}

    log_n = np.log(ns)
    log_r = np.log(ratios)
    coeffs = np.polyfit(log_n, log_r, 1)
    slope = float(coeffs[0])

    return {
        'ns': ns,
        'ratios': ratios,
        'slope': slope,
        'expected_slope': -0.5,
        'interpretation': (
            f"Slope={slope:.3f} (expected ~-0.5 for O(n^{{-1/2}}) scaling). "
            f"{'CONSISTENT' if -0.8 < slope < -0.2 else 'UNEXPECTED'}"
        ),
    }


def main():
    print("=" * 60)
    print("Experiment 43: 50x50 Scale Test")
    print(f"beta={BETA}, volume_fraction={VOLUME_FRACTION}")
    print(f"Grids: {GRID_SIZES}")
    print("=" * 60)

    t_start = time.time()
    results = []
    skip_remaining = False

    for side in GRID_SIZES:
        if skip_remaining:
            print(f"\nSkipping {side}x{side} — previous grid exceeded time budget.")
            break

        n = side * side
        # Scale parameters for larger grids
        if n > 1000:
            max_iter, n_restarts = 2000, 1
        elif n > 400:
            max_iter, n_restarts = 3000, 2
        else:
            max_iter, n_restarts = 5000, 3

        do_transport = (side <= 30)

        r, t_form = run_grid(side, max_iter=max_iter, n_restarts=n_restarts,
                             do_transport=do_transport)
        r['boundary_scaling'] = {
            'n': n,
            'boundary_over_core': r['core']['boundary_ratio'],
        }
        results.append(r)

        # If this grid took > 5 min, skip larger grids
        if t_form > MAX_TIME_PER_GRID:
            print(f"\n  Grid {side}x{side} took {t_form:.0f}s > {MAX_TIME_PER_GRID}s — "
                  f"skipping larger grids.")
            skip_remaining = True

    # Scaling table
    print(f"\n{'='*70}")
    print("SCALING TABLE")
    print(f"{'='*70}")
    header = (f"{'Grid':>8} {'n':>6} {'Energy':>10} {'max(u)':>8} "
              f"{'Deep/Core':>10} {'Bd/Core':>8} {'Bind':>6} {'Sep':>6} "
              f"{'Inside':>6} {'Time(s)':>8}")
    print(header)
    print("-" * len(header))

    for r in results:
        f = r['formation']
        c = r['core']
        d = r['diagnostics']
        print(f"{r['side']:>3}x{r['side']:<4} {r['n']:>6} {f['energy']:>10.3f} "
              f"{f['max_u']:>8.3f} {c['deep_ratio']:>10.3f} "
              f"{c['boundary_ratio']:>8.3f} {d['Bind']:>6.3f} {d['Sep']:>6.3f} "
              f"{d['Inside']:>6.3f} {f['time_sec']:>8.1f}")

    # Boundary scaling fit
    bs_fit = boundary_scaling_fit(results)
    print(f"\nBoundary scaling: {bs_fit.get('interpretation', bs_fit)}")

    # Summary
    total_time = time.time() - t_start
    summary = {
        'experiment': 'exp43_50x50_scale',
        'params': {'beta': BETA, 'volume_fraction': VOLUME_FRACTION},
        'grids': results,
        'boundary_scaling_fit': bs_fit,
        'total_time_sec': round(total_time, 2),
    }

    # Save results
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'exp43_50x50_scale.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")
    print(f"Total time: {total_time:.1f}s")

    return summary


if __name__ == '__main__':
    main()
