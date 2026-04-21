#!/usr/bin/env python3
"""
exp_mode_emergence.py — Round 12 Mode-Count Emergence Theorem (b) validation.

Target claim (Round 12 §1.5.1, part (b)):

  Expected number of emergent modes under Fokker-Planck / Langevin dynamics
  starting from u_uniform + η (small noise), for T < T*_2:

    K̂(β, α, T, c) ~ 1 + Θ( sqrt(N_unst) )   (2D grid heuristic)

  where N_unst is the Morse index at u_uniform (Round 12 Prop 1.3).

Critical gap (Round 14 §3.5): exp51/exp55 validate K*=1 universally at T=0
(gradient flow limit), but Mode-Count Emergence (b) is about T > 0 Langevin
SHORT-TIME emergence before long-time isoperimetric coarsening.

This experiment probes SHORT-TIME dynamics:
  - For β ∈ {β_crit·1.5, β_crit·3, β_crit·6} → predict N_unst ∈ {1, few, many}
  - For each β, run Langevin from u_uniform + tiny noise at T = T_c·2 (mid regime)
  - Track K_soft(t) evolution: short-time peak K̂_peak, long-time K̂_∞
  - Compare K̂_peak with Round 12 prediction

Expected runtime: 30min-2h (Langevin runs × multiple β).

Usage:
  cd CODE && python3 experiments/exp_mode_emergence.py [--grid-size 10] [...]
"""
import sys, os, time, json, argparse
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.langevin import projected_langevin
try:
    from scc.k_soft import k_soft
    HAS_KSOFT = True
except ImportError:
    HAS_KSOFT = False


def double_well_second_derivative(c):
    return 12.0 * c * c - 12.0 * c + 2.0


def compute_laplacian_spectrum(graph):
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.asarray(graph.W)
    L = np.diag(W.sum(axis=1)) - W
    return np.sort(np.linalg.eigvalsh(0.5 * (L + L.T)))


def predict_N_unst(lap_eigs, beta, alpha, c, r_cl_sep=0.125):
    """Round 12 Prop 1.3 prediction."""
    W_ddot = double_well_second_derivative(c)
    threshold = (beta * abs(W_ddot) - r_cl_sep) / (4.0 * alpha)
    # Exclude λ_1 = 0
    nontrivial = lap_eigs[1:]
    return int(np.sum(nontrivial < threshold))


def run_emergence(grid_size, beta, alpha, c, T, n_steps, dt, seed,
                  noise_amplitude=0.02, use_k_soft=True, gamma_K=0.05):
    """Start from u_uniform + small noise, run Langevin, track K_soft over time."""
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=100,
    )

    rng = np.random.default_rng(seed)
    u_init = c * np.ones(n)
    perturb = rng.standard_normal(n)
    perturb -= np.mean(perturb)
    perturb /= np.std(perturb) + 1e-12
    u_init = u_init + noise_amplitude * perturb
    u_init = np.clip(u_init, 1e-3, 1 - 1e-3)
    u_init *= (c * n) / u_init.sum()

    t0 = time.time()
    result = projected_langevin(
        u_init, graph, params,
        T=T, n_steps=n_steps, dt=dt,
        gamma_K=gamma_K,
        use_k_soft=use_k_soft and HAS_KSOFT,
        grid_size=grid_size,
        seed=seed,
        subsample=max(1, n_steps // 500),  # fine time resolution
        verbose=False,
    )
    dt_run = time.time() - t0

    # Analyze K_soft(t): peak and final
    k_softs = result['k_soft']
    times = result['times']

    if k_softs is None or len(k_softs) == 0:
        return {
            'beta': beta, 'error': 'k_soft unavailable',
            'time_sec': round(dt_run, 1),
        }

    # Peak in first half (short-time emergence)
    n_half = len(k_softs) // 2
    k_peak_idx = int(np.argmax(k_softs[:n_half]))
    k_peak = float(k_softs[k_peak_idx])
    t_peak = float(times[k_peak_idx])

    # Long-time average (last quarter)
    n_quarter = len(k_softs) // 4
    k_final = float(np.mean(k_softs[-n_quarter:]))
    k_final_std = float(np.std(k_softs[-n_quarter:]))

    return {
        'beta': beta, 'alpha': alpha, 'T': T, 'c': c,
        'grid_size': grid_size, 'n': n,
        'n_steps': n_steps, 'dt': dt,
        'k_peak': k_peak,
        'k_peak_time': t_peak,
        'k_final_mean': k_final,
        'k_final_std': k_final_std,
        'k_soft_timeseries': k_softs.tolist(),
        'times': times.tolist(),
        'final_u_stats': {
            'min': float(result['final_u'].min()),
            'max': float(result['final_u'].max()),
            'std': float(result['final_u'].std()),
            'mean': float(result['final_u'].mean()),
        },
        'time_sec': round(dt_run, 1),
    }


def main():
    parser = argparse.ArgumentParser(description='Round 12 Mode-Count Emergence (b) validation')
    parser.add_argument('--grid-size', type=int, default=10)
    parser.add_argument('--alpha', type=float, default=1.0)
    parser.add_argument('--c', type=float, default=0.5)
    parser.add_argument('--T', type=float, default=0.15,
                        help='target temperature (should be > T_c ≈ 0.06, < T*_uniform)')
    parser.add_argument('--beta-multipliers', type=str, default='1.5,2.5,4.0,7.0,12.0',
                        help='β as multiples of β_crit^(2)')
    parser.add_argument('--n-steps', type=int, default=30000)
    parser.add_argument('--dt', type=float, default=5e-4)
    parser.add_argument('--noise-amplitude', type=float, default=0.02)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--n-replicates', type=int, default=3,
                        help='number of independent seeds per β (for statistics)')
    parser.add_argument('--output', default='experiments/results/exp_mode_emergence.json')
    args = parser.parse_args()

    # Laplacian spectrum, β_crit boundaries
    graph = GraphState.grid_2d(args.grid_size, args.grid_size)
    lap_eigs = compute_laplacian_spectrum(graph)
    W_ddot = double_well_second_derivative(args.c)
    r_cl_sep = 0.125

    beta_crit_2 = (4.0 * args.alpha * lap_eigs[1] + r_cl_sep) / abs(W_ddot)
    beta_crit_k = [(k+1, float((4 * args.alpha * lap_eigs[k] + r_cl_sep) / abs(W_ddot)))
                   for k in range(1, min(8, len(lap_eigs)))]

    multipliers = [float(x) for x in args.beta_multipliers.split(',')]
    betas = [beta_crit_2 * mu for mu in multipliers]

    print("=" * 78)
    print("Round 12 Mode-Count Emergence (b) validation")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={args.grid_size**2})")
    print(f"α={args.alpha}, c={args.c}, T={args.T}, noise_amp={args.noise_amplitude}")
    print(f"β_crit^(2) = {beta_crit_2:.4f}")
    print(f"β_crit^(k) reference values:")
    for k, bk in beta_crit_k:
        print(f"  k={k}: β_crit^(k) = {bk:.4f}")
    print(f"β values scanned: {[f'{b:.2f}' for b in betas]}")
    print(f"Replicates per β: {args.n_replicates}")
    print(f"K_soft available: {HAS_KSOFT}")
    print("=" * 78)

    if not HAS_KSOFT:
        print("ERROR: scc.k_soft not available. Cannot measure K_soft(t). Abort.")
        return

    all_results = []
    t_total = time.time()

    for mu, beta in zip(multipliers, betas):
        N_unst = predict_N_unst(lap_eigs, beta, args.alpha, args.c, r_cl_sep)
        k_hat_predicted = 1 + np.sqrt(max(0, N_unst))  # Round 12 (b) heuristic

        print(f"\n{'*' * 60}")
        print(f"β = {beta:.3f} ({mu}× β_crit^(2))")
        print(f"  Predicted N_unst = {N_unst}")
        print(f"  Predicted K̂_peak ~ 1 + sqrt(N_unst) = {k_hat_predicted:.3f}")
        print(f"{'*' * 60}")

        replicate_results = []
        for rep in range(args.n_replicates):
            seed_rep = args.seed + rep * 1000 + int(mu * 100)
            print(f"\n  Replicate {rep+1}/{args.n_replicates} (seed={seed_rep})")
            try:
                r = run_emergence(args.grid_size, beta, args.alpha, args.c,
                                  args.T, args.n_steps, args.dt, seed_rep,
                                  args.noise_amplitude)
                r['replicate'] = rep
                r['beta_multiplier'] = mu
                r['N_unst_predicted'] = N_unst
                r['k_hat_predicted'] = float(k_hat_predicted)
                replicate_results.append(r)
                if 'error' in r:
                    print(f"    ERROR: {r['error']}")
                    continue
                print(f"    K̂_peak={r['k_peak']:.3f} at t={r['k_peak_time']:.3f}")
                print(f"    K̂_final={r['k_final_mean']:.3f} ± {r['k_final_std']:.3f}")
                print(f"    time={r['time_sec']}s")
            except Exception as e:
                print(f"    ERROR: {e}")
                import traceback; traceback.print_exc()
                replicate_results.append({'error': str(e), 'replicate': rep})

        # Aggregate over replicates
        valid = [r for r in replicate_results if 'error' not in r]
        if valid:
            k_peaks = [r['k_peak'] for r in valid]
            k_finals = [r['k_final_mean'] for r in valid]
            agg = {
                'beta': beta, 'beta_multiplier': mu,
                'N_unst_predicted': N_unst,
                'k_hat_predicted': float(k_hat_predicted),
                'k_peak_mean': float(np.mean(k_peaks)),
                'k_peak_std': float(np.std(k_peaks)),
                'k_final_mean_ensemble': float(np.mean(k_finals)),
                'k_final_std_ensemble': float(np.std(k_finals)),
                'replicates': replicate_results,
            }
            all_results.append(agg)
            print(f"\n  [Aggregate] K̂_peak = {agg['k_peak_mean']:.3f} ± {agg['k_peak_std']:.3f}  "
                  f"(vs predicted {k_hat_predicted:.3f})")
            print(f"  [Aggregate] K̂_final = {agg['k_final_mean_ensemble']:.3f}")

    # Summary
    print(f"\n{'='*78}")
    print("MODE-COUNT EMERGENCE SUMMARY")
    print(f"{'='*78}")
    print(f"{'β':>8} {'β/βc':>6} {'N_unst':>7} {'K̂_pred':>8} {'K̂_peak':>10} "
          f"{'K̂_final':>10}")
    print("-" * 78)
    for agg in all_results:
        print(f"{agg['beta']:>8.3f} {agg['beta_multiplier']:>6.2f} "
              f"{agg['N_unst_predicted']:>7d} {agg['k_hat_predicted']:>8.3f} "
              f"{agg['k_peak_mean']:>8.3f}±{agg['k_peak_std']:<.2f} "
              f"{agg['k_final_mean_ensemble']:>8.3f}±{agg['k_final_std_ensemble']:<.2f}")

    # Fit: K̂_peak vs sqrt(N_unst)
    if len(all_results) >= 3:
        n_unst_vals = np.array([a['N_unst_predicted'] for a in all_results])
        k_peak_vals = np.array([a['k_peak_mean'] for a in all_results])
        # Fit: K̂_peak = 1 + c * sqrt(N_unst)
        mask = n_unst_vals > 0
        if mask.sum() >= 2:
            x = np.sqrt(n_unst_vals[mask])
            y = k_peak_vals[mask] - 1.0
            slope = float(np.dot(x, y) / (np.dot(x, x) + 1e-12))
            print(f"\nFit: K̂_peak - 1 = c · sqrt(N_unst)")
            print(f"  Empirical c = {slope:.3f}")
            print(f"  Round 12 (b) prediction: c ≈ 1.0 (2D grid heuristic)")
            print(f"  Consistency: {'within order-of-magnitude' if 0.3 < slope < 3.0 else 'off'}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_mode_emergence',
            'round_ref': 'Round 12 Mode-Count Emergence (b) validation',
            'params': vars(args),
            'beta_crit_2': float(beta_crit_2),
            'beta_crit_k': beta_crit_k,
            'results': all_results,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2, default=str)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
