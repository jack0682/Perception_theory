#!/usr/bin/env python3
"""
exp_alpha_scan.py — Round 13 Corollary 2.2 validation via α-axis scan.

Target theorem (Round 13 §2.5.4):
  |B(u*)| ≤ O( sqrt(α/β) · Per_G(A*) )
  where B(u*) = {x : 0.1 < u*_x < 0.9}, A* = {x : u*_x ≥ 0.5}.

Critical gap identified in exp1-exp73 audit (Round 14 §3.8.2):
  All experiments fix α=1. Corollary 2.2's dimensional form sqrt(α/β) is
  empirically unverified across α.

This experiment:
  - Scans α ∈ {0.1, 0.25, 0.5, 1, 2, 5} and β ∈ {30, 50, 100}.
  - Measures |B(u*)| and Per_G(A*) for K=1 minimizer.
  - Fits ratio |B|/Per vs sqrt(α/β) — expected slope 1, intercept 0.

Expected runtime: ~15-30 min on 12x12 grid (18 (α,β) points, multi-init).

Usage:
  cd CODE && python3 experiments/exp_alpha_scan.py [--grid-size 12] [--n-inits 8]
"""
import sys, os, time, json, argparse
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation


def measure_interface_and_perimeter(u, graph, theta_low=0.1, theta_high=0.9, theta_core=0.5):
    """Compute |B(u)| (interface band) and Per_G(A) (graph perimeter of core).

    Returns:
        dict with:
          'interface_size': |{x : theta_low < u_x < theta_high}|
          'perimeter': |∂A| where A = {x : u_x >= theta_core}
          'core_size': |A|
          'ratio': |B| / Per_G(A) — the Cor 2.2 quantity
    """
    n = graph.n
    W = graph.W.tocsr()

    # Interface band B(u)
    in_band = (u > theta_low) & (u < theta_high)
    interface_size = int(np.sum(in_band))

    # Core A
    in_core = u >= theta_core
    core_size = int(np.sum(in_core))

    # Graph perimeter Per_G(A) = |{(x,y) edge : x in A, y not in A}|
    # (Undirected, count each boundary edge once)
    perimeter = 0
    for i in range(n):
        if not in_core[i]:
            continue
        neighbors = W[i].indices
        for j in neighbors:
            if j > i and not in_core[j]:  # avoid double counting
                perimeter += 1

    ratio = interface_size / perimeter if perimeter > 0 else float('nan')

    return {
        'interface_size': interface_size,
        'core_size': core_size,
        'perimeter': perimeter,
        'ratio': ratio,
    }


def run_single(grid_size, alpha, beta, n_inits, volume_fraction=0.3, seed=42):
    """Run find_formation with given (alpha, beta) and measure interface + perimeter."""
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)

    # Note: current scc API uses w_cl, w_sep, w_bd for term weights.
    # α (smoothness coefficient) is encoded via w_bd scale. Here we interpret
    # α = w_bd directly (β = beta_bd is the W(u) coefficient).
    # If scc API differs, adjust: some implementations use separate `alpha` param.
    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=volume_fraction,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,   # α via w_bd scale
        max_iter=5000,
        n_restarts=n_inits,
        dt_init=0.01,
        eps_init=0.01,
    )

    t0 = time.time()
    result = find_formation(graph, params, verbose=False)
    dt = time.time() - t0

    u = result.u
    measurements = measure_interface_and_perimeter(u, graph)

    # Theoretical scale
    xi_0 = np.sqrt(alpha / beta)

    return {
        'grid_size': grid_size,
        'n': n,
        'alpha': alpha,
        'beta': beta,
        'xi_0': float(xi_0),
        'alpha_over_beta': float(alpha / beta),
        'sqrt_a_over_b': float(xi_0),
        'energy': float(result.energy),
        'converged': bool(result.converged),
        'n_iter': int(result.n_iter),
        'time_sec': round(dt, 2),
        **measurements,
        'u_max': float(u.max()),
        'u_min': float(u.min()),
    }


def fit_cor_2_2(results):
    """Fit |B|/Per vs sqrt(α/β) across all (α, β) pairs.

    Corollary 2.2 predicts: ratio = C * sqrt(α/β), so log-log slope ≈ 1.
    Also tests: ratio = C + D·sqrt(α/β) (linear in xi_0, intercept ≈ 0).
    """
    valid = [r for r in results if r['perimeter'] > 0 and not np.isnan(r['ratio'])]

    if len(valid) < 3:
        return {'error': 'insufficient data'}

    xi_0 = np.array([r['xi_0'] for r in valid])
    ratio = np.array([r['ratio'] for r in valid])

    # Linear fit: ratio = C * xi_0 + b (Cor 2.2 predicts b ≈ 0)
    A = np.vstack([xi_0, np.ones(len(xi_0))]).T
    coef_linear, residuals_linear, _, _ = np.linalg.lstsq(A, ratio, rcond=None)
    C_linear, b_linear = float(coef_linear[0]), float(coef_linear[1])

    # Log-log fit: log(ratio) = slope * log(xi_0) + log(C)
    # Cor 2.2 predicts slope ≈ 1
    mask = (ratio > 0) & (xi_0 > 0)
    if mask.sum() >= 3:
        A_log = np.vstack([np.log(xi_0[mask]), np.ones(mask.sum())]).T
        coef_log, _, _, _ = np.linalg.lstsq(A_log, np.log(ratio[mask]), rcond=None)
        slope_log, intercept_log = float(coef_log[0]), float(coef_log[1])
    else:
        slope_log = intercept_log = float('nan')

    return {
        'n_points': len(valid),
        'linear_fit': {
            'C': C_linear,
            'intercept_b': b_linear,
            'prediction': 'ratio = C·sqrt(α/β)',
            'b_near_zero': abs(b_linear) < 1.0,
        },
        'loglog_fit': {
            'slope': slope_log,
            'intercept_log_C': intercept_log,
            'expected_slope': 1.0,
            'slope_consistent': 0.7 < slope_log < 1.3,
        },
    }


def main():
    parser = argparse.ArgumentParser(description='Round 13 Cor 2.2 α-scan validation')
    parser.add_argument('--grid-size', type=int, default=12)
    parser.add_argument('--n-inits', type=int, default=8)
    parser.add_argument('--volume-fraction', type=float, default=0.3)
    parser.add_argument('--output', default='experiments/results/exp_alpha_scan.json')
    parser.add_argument('--alphas', type=str, default='0.1,0.25,0.5,1.0,2.0,5.0')
    parser.add_argument('--betas', type=str, default='30.0,50.0,100.0')
    args = parser.parse_args()

    alphas = [float(x) for x in args.alphas.split(',')]
    betas = [float(x) for x in args.betas.split(',')]

    print("=" * 78)
    print(f"Round 13 Corollary 2.2 α-axis scan (|B(u*)| = O(sqrt(α/β)·Per_G(A*)))")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={args.grid_size**2}), "
          f"volume_fraction: {args.volume_fraction}, n_inits: {args.n_inits}")
    print(f"α values: {alphas}")
    print(f"β values: {betas}")
    print("=" * 78)

    results = []
    t_total = time.time()

    for beta in betas:
        for alpha in alphas:
            print(f"\n--- α={alpha}, β={beta}, ξ_0=sqrt(α/β)={np.sqrt(alpha/beta):.4f} ---")
            try:
                r = run_single(args.grid_size, alpha, beta, args.n_inits,
                               args.volume_fraction)
                results.append(r)
                print(f"  E={r['energy']:.4f}, |B|={r['interface_size']}, "
                      f"Per={r['perimeter']}, ratio={r['ratio']:.3f}")
                print(f"  core={r['core_size']}, u ∈ [{r['u_min']:.3f}, {r['u_max']:.3f}]")
                print(f"  converged={r['converged']}, time={r['time_sec']}s")
            except Exception as e:
                print(f"  ERROR: {e}")
                results.append({'alpha': alpha, 'beta': beta, 'error': str(e)})

    fit = fit_cor_2_2(results)

    # Table
    print(f"\n{'='*78}")
    print("RESULTS TABLE")
    print(f"{'='*78}")
    print(f"{'α':>6} {'β':>6} {'ξ_0':>8} {'|B|':>6} {'Per':>6} "
          f"{'|B|/Per':>9} {'|Core|':>7}")
    print("-" * 78)
    for r in results:
        if 'error' in r:
            continue
        print(f"{r['alpha']:>6.2f} {r['beta']:>6.1f} {r['xi_0']:>8.4f} "
              f"{r['interface_size']:>6d} {r['perimeter']:>6d} "
              f"{r['ratio']:>9.4f} {r['core_size']:>7d}")

    # Fit output
    print(f"\n{'='*78}")
    print("COROLLARY 2.2 FIT — ratio = C · sqrt(α/β) + b")
    print(f"{'='*78}")
    if 'error' not in fit:
        lf = fit['linear_fit']
        llf = fit['loglog_fit']
        print(f"  Linear fit:  C = {lf['C']:.4f}, intercept b = {lf['intercept_b']:.4f}")
        print(f"    Cor 2.2 expects b ≈ 0:  {'PASS' if lf['b_near_zero'] else 'FAIL'}")
        print(f"  Log-log fit: slope = {llf['slope']:.4f} (expected 1.0)")
        print(f"    Slope consistent with Cor 2.2: "
              f"{'PASS' if llf['slope_consistent'] else 'FAIL'}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_alpha_scan',
            'round_ref': 'Round 13 Cor 2.2 validation',
            'params': {
                'grid_size': args.grid_size,
                'n_inits': args.n_inits,
                'volume_fraction': args.volume_fraction,
                'alphas': alphas, 'betas': betas,
            },
            'results': results,
            'fit': fit,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
