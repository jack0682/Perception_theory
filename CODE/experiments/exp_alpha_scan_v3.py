#!/usr/bin/env python3
"""
exp_alpha_scan_v3.py — final α-scan validation of Cor 2.2.

v2 findings (2026-04-21):
  - v2 filter K_soft ≤ 1.3 too loose; most data was K=2 or partial K=1
    (sharp K=1 has K_soft ≈ 0.5 per Prop 4.1).
  - Small-ξ_0 points dominated by discretization floor.
  - Large-ξ_0 points actually roughly consistent with 3.45·ξ_0 prediction.

Cross-validation from exp_interface_ansatz (same session):
  |B|/Per_edge = (π·ln 9)/2·ξ_0 ≈ 3.449·ξ_0 with R² ≥ 0.998 at n = 1024-262144.

v3 strategy:
  1. Tight K_soft filter ≤ 0.55 (sharp K=1 only, calibrated from Prop 4.1).
  2. Asymptotic regime only: ξ_0 ∈ [0.10, 0.25] to avoid discretization floor.
  3. Grid 48×48 (balance between resolution and runtime).
  4. n_inits = 24 for reliable global K=1.
  5. Direct comparison: measured ratio vs predicted 3.449·ξ_0.

If this v3 succeeds, closes Cor 2.2 numerical validation across 3 independent
axes: exp42 (n-scan), exp_interface_ansatz (direct), exp_alpha_scan_v3 (α-scan).

Expected runtime: 10-20 min on 48×48 grid.

Usage:
  cd CODE && python3 experiments/exp_alpha_scan_v3.py [--grid-size 48]
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


# Cor 2.2 predicted constant (from exp_interface_ansatz, tanh profile, edge perimeter)
COR_2_2_C_TANH_EDGE = np.pi * np.log(9.0) / 2.0  # ≈ 3.449
COR_2_2_C_TANH_SITE = COR_2_2_C_TANH_EDGE / np.sqrt(2.0)  # ≈ 2.439


def measure_interface_full(u, graph, theta_low=0.1, theta_high=0.9, thetas_core=(0.4, 0.5, 0.6)):
    n = graph.n
    W = graph.W.tocsr()

    in_band = (u > theta_low) & (u < theta_high)
    interface_size = int(np.sum(in_band))

    edge_pers = []
    site_bds = []
    for theta in thetas_core:
        core = u >= theta
        if core.sum() in (0, n):
            continue
        per_e, site_bd = 0, 0
        for i in range(n):
            if not core[i]:
                continue
            neighbors = W[i].indices
            has_ext = False
            for j in neighbors:
                if not core[j]:
                    has_ext = True
                    if j > i:
                        per_e += 1
            if has_ext:
                site_bd += 1
        edge_pers.append(per_e)
        site_bds.append(site_bd)

    return {
        'interface_size': interface_size,
        'edge_perimeter_mean': float(np.mean(edge_pers)) if edge_pers else 0.0,
        'site_boundary_mean': float(np.mean(site_bds)) if site_bds else 0.0,
        'k_soft': float(k_soft(u, int(np.sqrt(n)))) if HAS_KSOFT else None,
    }


def run_single(grid_size, alpha, beta, n_inits, volume_fraction=0.3, seed=42):
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=volume_fraction,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=5000, n_restarts=n_inits,
        dt_init=0.01, eps_init=0.01,
    )
    t0 = time.time()
    r = find_formation(graph, params, verbose=False)
    dt = time.time() - t0

    u = r.u
    meas = measure_interface_full(u, graph)
    xi_0 = float(np.sqrt(alpha / beta))

    ratio_edge = (meas['interface_size'] / meas['edge_perimeter_mean']
                  if meas['edge_perimeter_mean'] > 0 else float('nan'))
    ratio_site = (meas['interface_size'] / meas['site_boundary_mean']
                  if meas['site_boundary_mean'] > 0 else float('nan'))

    pred_edge = COR_2_2_C_TANH_EDGE * xi_0
    pred_site = COR_2_2_C_TANH_SITE * xi_0

    return {
        'alpha': alpha, 'beta': beta, 'xi_0': xi_0, 'grid_size': grid_size,
        'energy': float(r.energy), 'converged': bool(r.converged),
        'time_sec': round(dt, 1),
        **meas,
        'ratio_edge': ratio_edge, 'ratio_site': ratio_site,
        'predicted_ratio_edge': pred_edge,
        'predicted_ratio_site': pred_site,
        'relative_error_edge': (ratio_edge - pred_edge) / pred_edge if pred_edge > 0 else float('nan'),
        'relative_error_site': (ratio_site - pred_site) / pred_site if pred_site > 0 else float('nan'),
    }


def main():
    parser = argparse.ArgumentParser(description='Cor 2.2 α-scan v3 (asymptotic regime, tight filter)')
    parser.add_argument('--grid-size', type=int, default=48)
    parser.add_argument('--n-inits', type=int, default=24)
    parser.add_argument('--volume-fraction', type=float, default=0.3)
    parser.add_argument('--k-soft-max', type=float, default=0.55,
                        help='sharp K=1 requires K_soft ≲ 0.5 (Prop 4.1 calibrated)')
    parser.add_argument('--xi-min', type=float, default=0.10)
    parser.add_argument('--xi-max', type=float, default=0.25)
    parser.add_argument('--alphas', type=str, default='0.5,1.0,2.0')
    parser.add_argument('--betas', type=str, default='20.0,30.0,50.0,80.0')
    parser.add_argument('--output', default='experiments/results/exp_alpha_scan_v3.json')
    args = parser.parse_args()

    alphas = [float(x) for x in args.alphas.split(',')]
    betas = [float(x) for x in args.betas.split(',')]

    # Filter (α,β) by ξ_0 range
    pairs = []
    for beta in betas:
        for alpha in alphas:
            xi = np.sqrt(alpha / beta)
            if args.xi_min <= xi <= args.xi_max:
                pairs.append((alpha, beta, float(xi)))

    pairs.sort(key=lambda x: x[2])  # sort by ξ_0

    print("=" * 85)
    print("exp_alpha_scan v3 — final Cor 2.2 α-scan validation")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={args.grid_size**2}), "
          f"n_inits: {args.n_inits}")
    print(f"K_soft filter: ≤ {args.k_soft_max} (sharp K=1 per Prop 4.1)")
    print(f"ξ_0 regime: [{args.xi_min}, {args.xi_max}] (asymptotic, discretization-safe)")
    print(f"Valid (α,β) pairs: {len(pairs)}")
    print(f"Predicted C_edge = π·ln(9)/2 = {COR_2_2_C_TANH_EDGE:.4f}")
    print(f"Predicted C_site = C_edge/√2 = {COR_2_2_C_TANH_SITE:.4f}")
    print("=" * 85)

    results = []
    t_total = time.time()

    for alpha, beta, xi in pairs:
        print(f"\n--- α={alpha}, β={beta}, ξ_0={xi:.4f} ---")
        try:
            r = run_single(args.grid_size, alpha, beta, args.n_inits,
                           args.volume_fraction,
                           seed=42 + int(alpha * 100) + int(beta))
            results.append(r)
            k_str = f"{r['k_soft']:.3f}" if r['k_soft'] is not None else "N/A"
            print(f"  E={r['energy']:.3f}, K_soft={k_str}, |B|={r['interface_size']}, "
                  f"Per_e={r['edge_perimeter_mean']:.1f}, Site_bd={r['site_boundary_mean']:.1f}")
            print(f"  ratio_edge={r['ratio_edge']:.3f} (predicted {r['predicted_ratio_edge']:.3f}, "
                  f"err {100*r['relative_error_edge']:+.1f}%)")
            print(f"  ratio_site={r['ratio_site']:.3f} (predicted {r['predicted_ratio_site']:.3f}, "
                  f"err {100*r['relative_error_site']:+.1f}%)")
            print(f"  time={r['time_sec']}s")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            results.append({'alpha': alpha, 'beta': beta, 'xi_0': xi, 'error': str(e)})

    # Filter to sharp K=1 only
    filtered = []
    if HAS_KSOFT:
        for r in results:
            if 'error' in r:
                continue
            if r['k_soft'] is not None and r['k_soft'] <= args.k_soft_max:
                filtered.append(r)
    else:
        filtered = [r for r in results if 'error' not in r]

    n_total = len([r for r in results if 'error' not in r])
    print(f"\n{'=' * 85}")
    print(f"K_soft ≤ {args.k_soft_max} filter: kept {len(filtered)}/{n_total}")
    print(f"{'=' * 85}")

    # Table
    print(f"\n{'α':>6} {'β':>6} {'ξ_0':>7} {'K_sft':>6} {'|B|':>5} "
          f"{'Per_e':>7} {'ratio_E':>8} {'pred_E':>8} {'err%':>6}")
    print("-" * 85)
    for r in filtered:
        k = f"{r['k_soft']:.3f}" if r['k_soft'] is not None else "N/A"
        err = 100 * r['relative_error_edge']
        print(f"{r['alpha']:>6.2f} {r['beta']:>6.1f} {r['xi_0']:>7.4f} "
              f"{k:>6} {r['interface_size']:>5d} {r['edge_perimeter_mean']:>7.1f} "
              f"{r['ratio_edge']:>8.3f} {r['predicted_ratio_edge']:>8.3f} "
              f"{err:>+6.1f}")

    # Fit
    if len(filtered) >= 3:
        xi_arr = np.array([r['xi_0'] for r in filtered])
        ratio_edge_arr = np.array([r['ratio_edge'] for r in filtered])
        ratio_site_arr = np.array([r['ratio_site'] for r in filtered])

        # Linear fit (through origin or free intercept)
        print(f"\n{'=' * 85}")
        print("FITS (filtered K=1 only)")
        print(f"{'=' * 85}")

        for name, arr, pred_C in [('edge', ratio_edge_arr, COR_2_2_C_TANH_EDGE),
                                    ('site', ratio_site_arr, COR_2_2_C_TANH_SITE)]:
            mask = np.isfinite(arr) & (arr > 0)
            if mask.sum() < 3:
                continue
            x = xi_arr[mask]
            y = arr[mask]

            # Free linear
            A = np.vstack([x, np.ones(len(x))]).T
            coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
            C_free, b_free = float(coef[0]), float(coef[1])

            # Through origin
            C_zero = float(np.dot(x, y) / np.dot(x, x))

            # R² for free fit
            pred = C_free * x + b_free
            ss_res = np.sum((y - pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

            # Mean / median relative error vs predicted
            rel_err = (y - pred_C * x) / (pred_C * x)
            median_err = float(np.median(np.abs(rel_err)))
            mean_err = float(np.mean(np.abs(rel_err)))

            print(f"\n[{name}_perimeter] (predicted C = {pred_C:.3f})")
            print(f"  Free fit:    ratio = {C_free:.3f}·ξ_0 + {b_free:.3f}  (R²={r2:.3f})")
            print(f"  Through origin: C = {C_zero:.3f}  ({100*(C_zero/pred_C - 1):+.1f}% vs predicted)")
            print(f"  Median |relative error|: {100*median_err:.1f}%")
            print(f"  Mean |relative error|:   {100*mean_err:.1f}%")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_alpha_scan_v3',
            'round_ref': 'Round 13 Cor 2.2 α-scan final (post-ansatz calibration)',
            'params': vars(args),
            'predicted_C_edge': float(COR_2_2_C_TANH_EDGE),
            'predicted_C_site': float(COR_2_2_C_TANH_SITE),
            'all_results': results,
            'filtered_results': filtered,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2, default=str)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
