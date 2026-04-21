#!/usr/bin/env python3
"""
exp_alpha_scan_v2.py — Round 13 Cor 2.2 validation, improved over v1.

v1 issues (from first run 2026-04-21):
  1. Mode pollution: different (α, β) hit different local minima (K=1 sharp vs K=2).
     |B| range 1-24 reflects mode variation, not just ξ_0 scaling.
  2. Per=0 NaN (3/18): graph-edge perimeter degenerate for very sharp formations.
  3. Grid 12x12 too small for large ξ_0 (α=5, β=30 gives ξ_0=0.41 >> 1/12).

v2 fixes:
  1. K_soft filter: reject runs with K_soft > 1.3 (not single-mode).
  2. Multi-threshold perimeter: average Per_G(A_θ) over θ ∈ {0.4, 0.5, 0.6}.
     Also provide site-boundary alternative |∂_site A| = |{x ∈ A : ∃y ∉ A, x~y}|.
  3. Larger grid (default 24x24) + more n_inits (default 16).
  4. Restrict to ξ_0 < 0.25 regime (Modica-Mortola asymptotic).

Usage:
  cd CODE && python3 experiments/exp_alpha_scan_v2.py [--grid-size 24] [...]
"""
import sys, os, time, json, argparse
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
try:
    from scc.k_soft import k_soft
    HAS_KSOFT = True
except ImportError:
    HAS_KSOFT = False
    print("WARNING: scc.k_soft not found. K_soft filtering disabled.")


def edge_perimeter(u_core_bool, W):
    """Count edges crossing the core boundary (undirected, once per edge)."""
    n = len(u_core_bool)
    p = 0
    for i in range(n):
        if not u_core_bool[i]:
            continue
        neighbors = W[i].indices
        for j in neighbors:
            if j > i and not u_core_bool[j]:
                p += 1
    return p


def site_boundary(u_core_bool, W):
    """Count core sites with at least one non-core neighbor."""
    n = len(u_core_bool)
    count = 0
    for i in range(n):
        if not u_core_bool[i]:
            continue
        neighbors = W[i].indices
        for j in neighbors:
            if not u_core_bool[j]:
                count += 1
                break
    return count


def multi_threshold_perimeter(u, graph, thetas=(0.4, 0.5, 0.6)):
    """Average perimeter over multiple threshold levels."""
    W = graph.W.tocsr()
    edge_pers = []
    site_bds = []
    for theta in thetas:
        core = u >= theta
        if core.sum() == 0 or core.sum() == len(u):
            continue
        edge_pers.append(edge_perimeter(core, W))
        site_bds.append(site_boundary(core, W))
    if not edge_pers:
        return {'edge_per_mean': 0, 'site_bd_mean': 0, 'thetas_used': []}
    return {
        'edge_per_mean': float(np.mean(edge_pers)),
        'edge_per_values': edge_pers,
        'site_bd_mean': float(np.mean(site_bds)),
        'site_bd_values': site_bds,
        'thetas_used': list(thetas),
    }


def measure_interface_v2(u, graph, grid_size,
                         theta_low=0.1, theta_high=0.9):
    """Enhanced measurement:
      - |B| = |{x : theta_low < u_x < theta_high}|
      - Per via multi-threshold
      - K_soft (for mode filtering)
      - Asymmetry: mass balance check
    """
    n = graph.n
    in_band = (u > theta_low) & (u < theta_high)
    interface_size = int(np.sum(in_band))

    per_info = multi_threshold_perimeter(u, graph)

    # K_soft for mode classification
    k_s = None
    if HAS_KSOFT:
        try:
            k_s = float(k_soft(u, grid_size))
        except Exception:
            pass

    return {
        'interface_size': interface_size,
        'edge_perimeter_mean': per_info['edge_per_mean'],
        'edge_perimeter_values': per_info.get('edge_per_values', []),
        'site_boundary_mean': per_info['site_bd_mean'],
        'site_boundary_values': per_info.get('site_bd_values', []),
        'k_soft': k_s,
    }


def run_single(grid_size, alpha, beta, n_inits, volume_fraction=0.3, seed=42):
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)

    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=volume_fraction,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=5000,
        n_restarts=n_inits,
        dt_init=0.01,
        eps_init=0.01,
    )

    t0 = time.time()
    result = find_formation(graph, params, verbose=False)
    dt = time.time() - t0

    u = result.u
    measurements = measure_interface_v2(u, graph, grid_size)
    xi_0 = float(np.sqrt(alpha / beta))

    # Use edge perimeter (more standard) but also record site boundary
    ep = measurements['edge_perimeter_mean']
    sb = measurements['site_boundary_mean']

    ratio_edge = measurements['interface_size'] / ep if ep > 0 else float('nan')
    ratio_site = measurements['interface_size'] / sb if sb > 0 else float('nan')

    return {
        'grid_size': grid_size, 'n': n,
        'alpha': alpha, 'beta': beta,
        'xi_0': xi_0, 'alpha_over_beta': float(alpha / beta),
        'energy': float(result.energy),
        'converged': bool(result.converged),
        'n_iter': int(result.n_iter),
        'time_sec': round(dt, 2),
        'ratio_edge': ratio_edge,
        'ratio_site': ratio_site,
        'k_soft': measurements['k_soft'],
        **{k: v for k, v in measurements.items() if k not in ('k_soft',)},
        'u_max': float(u.max()),
        'u_min': float(u.min()),
    }


def fit_cor_2_2_v2(results, k_soft_max=1.3):
    """Fit with K_soft filter."""
    # Filter: K=1 single-mode only (K_soft ≤ k_soft_max)
    if HAS_KSOFT:
        valid = [r for r in results if r.get('k_soft') is not None
                 and r['k_soft'] <= k_soft_max
                 and not np.isnan(r['ratio_edge'])]
    else:
        valid = [r for r in results if not np.isnan(r['ratio_edge'])]

    n_filtered = len(results) - len(valid)
    print(f"\n  Filter: kept {len(valid)}/{len(results)} "
          f"(removed {n_filtered}: K_soft>{k_soft_max} or NaN)")

    if len(valid) < 3:
        return {'error': 'insufficient filtered data', 'n_valid': len(valid)}

    xi_0 = np.array([r['xi_0'] for r in valid])
    ratio_edge = np.array([r['ratio_edge'] for r in valid])
    ratio_site = np.array([r['ratio_site'] for r in valid])

    results_fits = {}
    for name, ratio in [('edge_perimeter', ratio_edge), ('site_boundary', ratio_site)]:
        mask = (ratio > 0) & (xi_0 > 0) & np.isfinite(ratio)
        if mask.sum() < 3:
            results_fits[name] = {'error': 'too few points'}
            continue

        # Linear fit
        A = np.vstack([xi_0[mask], np.ones(mask.sum())]).T
        coef, _, _, _ = np.linalg.lstsq(A, ratio[mask], rcond=None)
        C_lin, b_lin = float(coef[0]), float(coef[1])

        # Log-log fit
        A_log = np.vstack([np.log(xi_0[mask]), np.ones(mask.sum())]).T
        coef_log, _, _, _ = np.linalg.lstsq(A_log, np.log(ratio[mask]), rcond=None)
        slope, intercept = float(coef_log[0]), float(coef_log[1])

        # R² for log-log
        log_ratio = np.log(ratio[mask])
        pred = slope * np.log(xi_0[mask]) + intercept
        ss_res = np.sum((log_ratio - pred) ** 2)
        ss_tot = np.sum((log_ratio - np.mean(log_ratio)) ** 2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

        results_fits[name] = {
            'n_points': int(mask.sum()),
            'linear_C': C_lin, 'linear_intercept': b_lin,
            'loglog_slope': slope, 'loglog_intercept_log_C': intercept,
            'loglog_r2': r2,
            'expected_slope': 1.0,
            'slope_consistent': 0.7 < slope < 1.3,
        }

    return {'n_valid': len(valid), 'fits': results_fits}


def main():
    parser = argparse.ArgumentParser(description='Round 13 Cor 2.2 α-scan v2')
    parser.add_argument('--grid-size', type=int, default=24)
    parser.add_argument('--n-inits', type=int, default=16)
    parser.add_argument('--volume-fraction', type=float, default=0.3)
    parser.add_argument('--output', default='experiments/results/exp_alpha_scan_v2.json')
    parser.add_argument('--alphas', type=str, default='0.1,0.2,0.5,1.0,2.0')
    parser.add_argument('--betas', type=str, default='30.0,50.0,100.0,200.0')
    parser.add_argument('--k-soft-max', type=float, default=1.3,
                        help='reject runs with K_soft > this (mode filter)')
    parser.add_argument('--xi-max', type=float, default=0.25,
                        help='skip (α,β) with sqrt(α/β) > xi_max (Modica-Mortola asymptotic)')
    args = parser.parse_args()

    alphas = [float(x) for x in args.alphas.split(',')]
    betas = [float(x) for x in args.betas.split(',')]

    # Filter (α, β) pairs by ξ_0
    pairs = []
    for beta in betas:
        for alpha in alphas:
            xi = np.sqrt(alpha / beta)
            if xi <= args.xi_max:
                pairs.append((alpha, beta, float(xi)))

    print("=" * 78)
    print(f"Round 13 Corollary 2.2 α-axis scan v2 (improved)")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={args.grid_size**2}), "
          f"vol_frac: {args.volume_fraction}, n_inits: {args.n_inits}")
    print(f"α values: {alphas}")
    print(f"β values: {betas}")
    print(f"ξ_max cutoff: {args.xi_max} → {len(pairs)} valid (α,β) pairs")
    print(f"K_soft filter: K_soft ≤ {args.k_soft_max} (single-mode only)")
    print(f"K_soft available: {HAS_KSOFT}")
    print("=" * 78)

    results = []
    t_total = time.time()

    for alpha, beta, xi in pairs:
        print(f"\n--- α={alpha}, β={beta}, ξ_0={xi:.4f} ---")
        try:
            r = run_single(args.grid_size, alpha, beta, args.n_inits,
                           args.volume_fraction, seed=42 + int(alpha*100) + int(beta))
            results.append(r)
            k_str = f"{r['k_soft']:.3f}" if r['k_soft'] is not None else "N/A"
            print(f"  E={r['energy']:.4f}, |B|={r['interface_size']}, "
                  f"K_soft={k_str}")
            print(f"  Per_edge={r['edge_perimeter_mean']:.1f} "
                  f"(θ={r['edge_perimeter_values']}), "
                  f"site_bd={r['site_boundary_mean']:.1f}")
            print(f"  ratio_edge={r['ratio_edge']:.3f}, ratio_site={r['ratio_site']:.3f}")
            print(f"  time={r['time_sec']}s")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            results.append({'alpha': alpha, 'beta': beta, 'error': str(e)})

    # Fit
    fit = fit_cor_2_2_v2(results, k_soft_max=args.k_soft_max)

    # Table
    print(f"\n{'='*95}")
    print("RESULTS TABLE (v2)")
    print(f"{'='*95}")
    print(f"{'α':>6} {'β':>6} {'ξ_0':>7} {'K_soft':>7} {'|B|':>5} "
          f"{'edge_Per':>8} {'site_Bd':>7} {'ratio_E':>8} {'ratio_S':>8}")
    print("-" * 95)
    for r in results:
        if 'error' in r:
            continue
        k_str = f"{r['k_soft']:.2f}" if r['k_soft'] is not None else "N/A"
        print(f"{r['alpha']:>6.2f} {r['beta']:>6.1f} {r['xi_0']:>7.4f} "
              f"{k_str:>7} {r['interface_size']:>5d} "
              f"{r['edge_perimeter_mean']:>8.1f} {r['site_boundary_mean']:>7.1f} "
              f"{r['ratio_edge']:>8.3f} {r['ratio_site']:>8.3f}")

    # Fit output
    print(f"\n{'='*95}")
    print("COROLLARY 2.2 FIT v2")
    print(f"{'='*95}")
    if 'error' not in fit:
        for name, f in fit['fits'].items():
            if 'error' in f:
                continue
            print(f"\n  [{name}]")
            print(f"    Points: {f['n_points']}")
            print(f"    Linear: ratio = {f['linear_C']:.3f}·ξ_0 + {f['linear_intercept']:.3f}")
            print(f"    Log-log: slope = {f['loglog_slope']:.3f} (expect 1.0), "
                  f"R² = {f['loglog_r2']:.3f}")
            print(f"    Consistent with Cor 2.2: "
                  f"{'PASS' if f['slope_consistent'] else 'FAIL'}")
    else:
        print(f"  FIT ERROR: {fit.get('error')}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_alpha_scan_v2',
            'round_ref': 'Round 13 Cor 2.2 v2 (v1 fixes)',
            'params': vars(args),
            'results': results,
            'fit': fit,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2, default=str)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
