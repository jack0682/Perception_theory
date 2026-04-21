#!/usr/bin/env python3
"""
exp_three_regime.py — Round 4 Theorem 2.1 three-regime phase diagram validation.

Target (Round 4 Theorem 2.1 in logs/daily/2026-04-21/07_round4_verification.md):

  For c ∈ spinodal, the (T, c)-parameter space of F_C+E decomposes into:
    - Low-T (T < T_c ≈ 0.06 per E-16 code verification):
        K_soft ≈ 1 (single-mode preferred)
    - Mid-T (T_c < T < T*_uniform ≈ 7.37):
        K_soft ≈ 2+ (multi-mode entropy-driven)
    - High-T (T > T*_uniform):
        u → uniform (entropy maximization)

NQ-18 (unverified since Round 4): numerical verification at T ∈ {0.1, 1, 5, 10}.

This experiment:
  - Canonical params: β=30, α=1, grid=10, c=0.5
  - For each T in {0.01, 0.05, 0.1, 0.5, 1, 2, 5, 10}:
    - Run projected Langevin from u_init = c·1 + small noise
    - Equilibrate for n_eq steps
    - Sample for n_sample steps, measure K_soft distribution and mean_u
  - Regime classification from samples

Expected runtime: several hours (100k+ Langevin steps × 8 temperatures).

Usage:
  cd CODE && python3 experiments/exp_three_regime.py \\
       [--grid-size 10] [--n-steps 50000] [--temperatures ...]
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


def classify_regime(k_soft_samples, mean_u_samples, c, tol_uniform=0.05):
    """Classify which of three regimes the ensemble fits.

    Heuristic:
      - If u stays near uniform (|u - c| < tol across samples): 'uniform'
      - elif K_soft mean < 1.3: 'single-mode'
      - else: 'multi-mode'
    """
    if k_soft_samples is None:
        # Fall back to using mean_u std only
        std_mu = np.std(mean_u_samples) if len(mean_u_samples) > 0 else 0
        if std_mu < tol_uniform:
            return 'uniform-or-low-variation'
        return 'unknown-no-k_soft'

    k_mean = float(np.mean(k_soft_samples))
    k_std = float(np.std(k_soft_samples))

    if k_mean < 1.3:
        regime = 'single-mode'
    elif k_mean < 1.8:
        regime = 'mixed/transition'
    else:
        regime = 'multi-mode'

    return regime


def run_single_T(grid_size, T, beta, alpha, c, n_steps, dt, seed,
                 n_equilibrate_frac=0.3, use_k_soft=True, gamma_K=0.05):
    """Run Langevin at single T, return ensemble statistics."""
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=100,
    )

    # Initial: uniform + small noise (mean-preserving)
    rng = np.random.default_rng(seed)
    u_init = c * np.ones(n)
    perturb = rng.standard_normal(n)
    perturb -= np.mean(perturb)
    u_init = u_init + 0.01 * perturb
    u_init = np.clip(u_init, 1e-3, 1 - 1e-3)
    # Rescale to exact mass
    u_init *= (c * n) / u_init.sum()

    t0 = time.time()
    result = projected_langevin(
        u_init, graph, params,
        T=T,
        n_steps=n_steps,
        dt=dt,
        gamma_K=gamma_K,
        use_k_soft=use_k_soft and HAS_KSOFT,
        grid_size=grid_size,
        seed=seed,
        subsample=max(1, n_steps // 200),
        verbose=True,
    )
    dt_run = time.time() - t0

    # Drop first n_equilibrate_frac as burn-in
    n_eq = int(n_equilibrate_frac * len(result['energies']))

    energies_eq = result['energies'][n_eq:]
    mean_us_eq = result['mean_u'][n_eq:]
    k_softs_eq = result['k_soft'][n_eq:] if result['k_soft'] is not None else None

    regime = classify_regime(k_softs_eq, mean_us_eq, c)

    return {
        'T': T, 'beta': beta, 'alpha': alpha, 'c': c,
        'grid_size': grid_size, 'n': n,
        'n_steps': n_steps, 'dt': dt,
        'regime': regime,
        'energy_mean': float(np.mean(energies_eq)),
        'energy_std': float(np.std(energies_eq)),
        'mean_u_mean': float(np.mean(mean_us_eq)),
        'mean_u_std': float(np.std(mean_us_eq)),
        'k_soft_mean': float(np.mean(k_softs_eq)) if k_softs_eq is not None else None,
        'k_soft_std': float(np.std(k_softs_eq)) if k_softs_eq is not None else None,
        'k_soft_hist': np.histogram(k_softs_eq, bins=20)[0].tolist() if k_softs_eq is not None else None,
        'final_u_stats': {
            'min': float(result['final_u'].min()),
            'max': float(result['final_u'].max()),
            'std': float(result['final_u'].std()),
        },
        'time_sec': round(dt_run, 1),
    }


def predict_T_star_uniform(beta, alpha, lambda_2, c, r_cl_sep=0.125):
    """Round 4 Theorem 1.1 prediction."""
    W_ddot = 12.0 * c * c - 12.0 * c + 2.0  # W''(c)
    return c * (1 - c) * (beta * abs(W_ddot) - 4.0 * alpha * lambda_2 - r_cl_sep)


def main():
    parser = argparse.ArgumentParser(description='Round 4 Thm 2.1 three-regime validation')
    parser.add_argument('--grid-size', type=int, default=10)
    parser.add_argument('--beta', type=float, default=30.0)
    parser.add_argument('--alpha', type=float, default=1.0)
    parser.add_argument('--c', type=float, default=0.5)
    parser.add_argument('--n-steps', type=int, default=50000)
    parser.add_argument('--dt', type=float, default=5e-4)
    parser.add_argument('--temperatures', type=str,
                        default='0.01,0.05,0.1,0.5,1.0,2.0,5.0,10.0')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--gamma-K', type=float, default=0.05)
    parser.add_argument('--output', default='experiments/results/exp_three_regime.json')
    args = parser.parse_args()

    temperatures = [float(x) for x in args.temperatures.split(',')]

    # Predict T*_uniform for reference
    graph = GraphState.grid_2d(args.grid_size, args.grid_size)
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.asarray(graph.W)
    L = np.diag(W.sum(axis=1)) - W
    lap_eigs = np.sort(np.linalg.eigvalsh(0.5 * (L + L.T)))
    lambda_2 = float(lap_eigs[1])

    T_star_uniform = predict_T_star_uniform(args.beta, args.alpha, lambda_2, args.c)

    print("=" * 78)
    print("Round 4 Theorem 2.1 three-regime phase diagram validation")
    print(f"Grid: {args.grid_size}x{args.grid_size}, β={args.beta}, α={args.alpha}, c={args.c}")
    print(f"λ_2(G) = {lambda_2:.4f}")
    print(f"Predicted T*_uniform ≈ {T_star_uniform:.3f} (Round 4 Thm 1.1)")
    print(f"Predicted T_c ≈ 0.06 (E-16, 12x12 numerical)")
    print(f"Temperatures scanned: {temperatures}")
    print(f"K_soft available: {HAS_KSOFT}")
    print("=" * 78)

    results = []
    t_total = time.time()

    for T in temperatures:
        print(f"\n{'*' * 60}")
        print(f"T = {T}")
        print(f"{'*' * 60}")
        try:
            r = run_single_T(args.grid_size, T, args.beta, args.alpha, args.c,
                             args.n_steps, args.dt, args.seed + int(T * 100),
                             gamma_K=args.gamma_K)
            results.append(r)
            print(f"\n  Regime: {r['regime']}")
            print(f"  <E>={r['energy_mean']:.3f} ± {r['energy_std']:.3f}")
            print(f"  <mean(u)>={r['mean_u_mean']:.4f} ± {r['mean_u_std']:.4f} (target c={args.c})")
            if r['k_soft_mean'] is not None:
                print(f"  <K_soft>={r['k_soft_mean']:.3f} ± {r['k_soft_std']:.3f}")
            print(f"  final u: min={r['final_u_stats']['min']:.3f}, "
                  f"max={r['final_u_stats']['max']:.3f}, "
                  f"std={r['final_u_stats']['std']:.3f}")
            print(f"  Time: {r['time_sec']}s")
        except Exception as e:
            print(f"  ERROR at T={T}: {e}")
            import traceback; traceback.print_exc()
            results.append({'T': T, 'error': str(e)})

    # Summary
    print(f"\n{'='*78}")
    print("THREE-REGIME CLASSIFICATION SUMMARY")
    print(f"{'='*78}")
    print(f"{'T':>8} {'<K_soft>':>10} {'<mean(u)>':>10} {'std(u)':>9} {'regime':>22}")
    print("-" * 78)
    for r in results:
        if 'error' in r:
            print(f"{r['T']:>8} {'ERROR':>10}")
            continue
        k = f"{r['k_soft_mean']:.3f}" if r['k_soft_mean'] is not None else "N/A"
        print(f"{r['T']:>8.3f} {k:>10} {r['mean_u_mean']:>10.4f} "
              f"{r['final_u_stats']['std']:>9.4f} {r['regime']:>22}")

    print(f"\nPredicted regime boundaries:")
    print(f"  T_c ≈ 0.06 (single-mode ↔ multi-mode)")
    print(f"  T*_uniform ≈ {T_star_uniform:.3f} (multi-mode ↔ uniform)")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_three_regime',
            'round_ref': 'Round 4 Thm 2.1 validation (NQ-18)',
            'params': vars(args),
            'lambda_2': lambda_2,
            'T_star_uniform_predicted': float(T_star_uniform),
            'T_c_predicted': 0.06,
            'results': results,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
