#!/usr/bin/env python3
"""
exp_hessian_uniform_v2.py — Round 12 Prop 1.3 refined validation.

v1 findings (2026-04-21):
  - Systematic MISMATCH at low-to-mid β (theory underestimates N_unst 2-5×).
  - At β=1: theory min_eig ≈ -0.27, numerical min_eig = -5.12 (20× off!).
  - PASS only at saturation (β=50+, all directions unstable).

Diagnosis:
  The simple form `r_cl_sep ≈ 0.125·I` from Round 4 §1.2 is a LOWER BOUND,
  not exact. Real Hessian of E_cl + E_sep at uniform has non-scalar structure
  with additional negative contributions.

v2 strategy:
  1. Pure E_bd mode (w_cl=0, w_sep=0): isolates Laplacian-based theory,
     which SHOULD match exactly.
  2. Full E mode (canonical w_cl=w_sep=1): measures empirical r_cl_sep(β, α)
     as a STRUCTURAL operator, not scalar.
  3. Larger grid (16×16 default, 24×24 option) to avoid Morse-index saturation.
  4. Extract effective r_cl_sep matrix via difference:
     H_cl_sep := H_full - H_bd_only  → eigenvalue analysis.

This also discovers what REAL Prop 1.3 should look like.

Expected runtime:
  - 16×16: ~1-5 min (n=256, 256 grad evals per β)
  - 24×24: ~10-30 min (n=576)

Usage:
  cd CODE && python3 experiments/exp_hessian_uniform_v2.py [--grid-size 16]
"""
import sys, os, time, json, argparse
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer


def double_well_second_derivative(c):
    return 12.0 * c * c - 12.0 * c + 2.0


def compute_laplacian_spectrum(graph):
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.asarray(graph.W)
    L = np.diag(W.sum(axis=1)) - W
    return np.sort(np.linalg.eigvalsh(0.5 * (L + L.T)))


def predict_N_unst_pure_ebd(lap_eigs, beta, alpha, c):
    """Pure E_bd theory — should be exact.
    μ_k = β·W''(c) + 4α·λ_k  (no cl/sep contribution)
    """
    W_ddot = double_well_second_derivative(c)
    threshold = beta * abs(W_ddot) / (4.0 * alpha)  # no r_cl_sep
    nontrivial = lap_eigs[1:]
    mu_k = beta * W_ddot + 4.0 * alpha * nontrivial
    return {
        'n_unst': int(np.sum(mu_k < 0)),
        'threshold_lambda': float(threshold),
        'mu_k_values': mu_k.tolist(),
        'min_mu': float(mu_k.min()),
        'max_mu': float(mu_k.max()),
    }


def get_gradient_fn(ec, n):
    """Detect gradient interface. Returns callable or None."""
    try:
        u_test = 0.5 * np.ones(n)
        out = ec.energy(u_test)
        if isinstance(out, tuple) and len(out) == 2 and out[1] is not None:
            g_test = np.asarray(out[1])
            if g_test.shape == (n,):
                return lambda u: np.asarray(ec.energy(u)[1])
    except Exception:
        pass
    try:
        g_test = np.asarray(ec.gradient(0.5 * np.ones(n)))
        if g_test.shape == (n,):
            return ec.gradient
    except Exception:
        pass
    return None


def compute_hessian_fd(grad_fn, u, eps=1e-5):
    """Compute full Hessian matrix via FD on gradient. O(n) grad calls."""
    n = len(u)
    H = np.zeros((n, n))
    g0 = np.asarray(grad_fn(u))
    for i in range(n):
        u_plus = u.copy(); u_plus[i] += eps
        H[:, i] = (np.asarray(grad_fn(u_plus)) - g0) / eps
    return 0.5 * (H + H.T)


def project_onto_volume_tangent(H, n):
    one = np.ones(n) / np.sqrt(n)
    P = np.eye(n) - np.outer(one, one)
    return P @ H @ P


def morse_stats(H, n, tol=1e-6):
    """Eigenvalue analysis on 1^⊥."""
    H_tan = project_onto_volume_tangent(H, n)
    eigs = np.sort(np.linalg.eigvalsh(H_tan))
    n_neg = int(np.sum(eigs < -tol))
    n_zero = int(np.sum(np.abs(eigs) <= tol))
    n_pos = int(np.sum(eigs > tol))
    return {
        'morse_index': n_neg,
        'n_zero': n_zero,
        'n_pos': n_pos,
        'min_eig': float(eigs[0]),
        'max_eig': float(eigs[-1]),
        'eigs_sorted_first20': eigs[:20].tolist(),
        'eigs_sorted_last5': eigs[-5:].tolist(),
    }


def run_one_config(graph, beta, alpha, c, w_cl, w_sep, w_bd):
    """Compute Hessian at u_uniform for given term weights."""
    n = graph.n
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=w_cl, w_sep=w_sep, w_bd=w_bd,
        max_iter=100,
    )
    ec = EnergyComputer(graph, params)
    grad_fn = get_gradient_fn(ec, n)
    if grad_fn is None:
        raise RuntimeError("No usable gradient interface in scc.energy")

    u_uniform = c * np.ones(n)
    H = compute_hessian_fd(grad_fn, u_uniform)
    stats = morse_stats(H, n)
    return H, stats


def main():
    parser = argparse.ArgumentParser(description='Round 12 Prop 1.3 v2 — pure E_bd + full E comparison')
    parser.add_argument('--grid-size', type=int, default=16)
    parser.add_argument('--c', type=float, default=0.5)
    parser.add_argument('--alpha', type=float, default=1.0)
    parser.add_argument('--betas', type=str,
                        default='1.0,2.0,5.0,10.0,20.0,40.0,80.0,150.0,300.0')
    parser.add_argument('--output', default='experiments/results/exp_hessian_uniform_v2.json')
    parser.add_argument('--skip-full', action='store_true',
                        help='skip full E run, only pure E_bd (faster)')
    args = parser.parse_args()

    betas = [float(x) for x in args.betas.split(',')]
    n = args.grid_size * args.grid_size

    graph = GraphState.grid_2d(args.grid_size, args.grid_size)
    lap_eigs = compute_laplacian_spectrum(graph)
    W_ddot = double_well_second_derivative(args.c)

    # Max Morse index = n - 1 (one direction removed by volume constraint)
    max_morse = n - 1

    # β_crit thresholds (pure E_bd)
    beta_crit_k = []
    for k in range(1, min(10, len(lap_eigs))):
        bk = 4.0 * args.alpha * lap_eigs[k] / abs(W_ddot)
        beta_crit_k.append({'k': k + 1, 'lambda_k': float(lap_eigs[k]), 'beta_crit_pure': float(bk)})

    print("=" * 88)
    print("Round 12 Prop 1.3 v2 — pure E_bd validation + full E comparison")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={n}, max Morse = {max_morse})")
    print(f"c={args.c}, α={args.alpha}, W''(c) = {W_ddot:.4f}")
    print(f"Laplacian spectrum λ_2..λ_6: {lap_eigs[1:6].tolist()}")
    print(f"β_crit^(k) (PURE E_bd) for k=2..5:")
    for bk in beta_crit_k[:4]:
        print(f"  k={bk['k']}: λ_k={bk['lambda_k']:.4f}, β_crit^(k)={bk['beta_crit_pure']:.4f}")
    print(f"β values: {betas}")
    print("=" * 88)

    results = []
    t_total = time.time()

    for beta in betas:
        print(f"\n{'*' * 60}")
        print(f"β = {beta}")
        print(f"{'*' * 60}")
        entry = {'beta': beta, 'grid_size': args.grid_size, 'n': n, 'c': args.c, 'alpha': args.alpha}

        # Theoretical (pure E_bd)
        theory_pure = predict_N_unst_pure_ebd(lap_eigs, beta, args.alpha, args.c)
        entry['theory_pure_ebd'] = theory_pure
        print(f"  Theory (pure E_bd): N_unst = {theory_pure['n_unst']}, "
              f"min μ_k = {theory_pure['min_mu']:.3f}")

        # Numerical: pure E_bd (w_cl=0, w_sep=0)
        print("  [A] Pure E_bd (w_cl=0, w_sep=0)")
        try:
            t0 = time.time()
            H_bd, stats_bd = run_one_config(graph, beta, args.alpha, args.c,
                                             w_cl=0.0, w_sep=0.0, w_bd=1.0)
            dt_bd = time.time() - t0
            entry['numerical_pure_ebd'] = stats_bd
            entry['numerical_pure_ebd']['time_sec'] = round(dt_bd, 2)

            match_pure = (stats_bd['morse_index'] == theory_pure['n_unst']) or \
                         (stats_bd['morse_index'] == max_morse and theory_pure['n_unst'] == max_morse)
            entry['pure_match'] = bool(match_pure)
            tag = "✓ MATCH" if match_pure else "✗ MISMATCH"
            print(f"    Morse = {stats_bd['morse_index']} (theory {theory_pure['n_unst']})  {tag}")
            print(f"    min_eig = {stats_bd['min_eig']:.3f}, max_eig = {stats_bd['max_eig']:.3f}")
            print(f"    time = {dt_bd:.1f}s")
        except Exception as e:
            print(f"    ERROR: {e}")
            entry['numerical_pure_ebd'] = {'error': str(e)}
            import traceback; traceback.print_exc()
            results.append(entry)
            continue

        # Numerical: full E (w_cl=w_sep=w_bd=1)
        if not args.skip_full:
            print("  [B] Full E (w_cl=w_sep=w_bd=1)")
            try:
                t0 = time.time()
                H_full, stats_full = run_one_config(graph, beta, args.alpha, args.c,
                                                    w_cl=1.0, w_sep=1.0, w_bd=1.0)
                dt_full = time.time() - t0
                entry['numerical_full'] = stats_full
                entry['numerical_full']['time_sec'] = round(dt_full, 2)

                print(f"    Morse = {stats_full['morse_index']}")
                print(f"    min_eig = {stats_full['min_eig']:.3f}, max_eig = {stats_full['max_eig']:.3f}")

                # Extract structural cl/sep contribution
                # H_cl_sep := H_full - H_bd (on 1^⊥)
                H_diff = H_full - H_bd
                H_diff_tan = project_onto_volume_tangent(H_diff, n)
                eigs_diff = np.sort(np.linalg.eigvalsh(H_diff_tan))
                entry['cl_sep_hessian'] = {
                    'min_eig': float(eigs_diff[0]),
                    'max_eig': float(eigs_diff[-1]),
                    'mean_diag': float(np.mean(np.diag(H_diff_tan))),
                    'eigs_first10': eigs_diff[:10].tolist(),
                    'eigs_last5': eigs_diff[-5:].tolist(),
                    'n_negative': int(np.sum(eigs_diff < -1e-6)),
                }
                print(f"    cl_sep contribution: min_eig = {eigs_diff[0]:.3f}, "
                      f"max_eig = {eigs_diff[-1]:.3f}")
                print(f"    cl_sep negative eigs: {entry['cl_sep_hessian']['n_negative']}")
                print(f"    time = {dt_full:.1f}s")
            except Exception as e:
                print(f"    ERROR: {e}")
                entry['numerical_full'] = {'error': str(e)}

        results.append(entry)

    # Summary table
    print(f"\n{'='*88}")
    print("PURE E_bd VALIDATION TABLE (Prop 1.3 in isolation)")
    print(f"{'='*88}")
    print(f"{'β':>8} {'N_pred':>8} {'N_numer':>8} {'min_eig':>10} {'match':>8}")
    print("-" * 88)
    for r in results:
        if 'numerical_pure_ebd' in r and 'error' not in r['numerical_pure_ebd']:
            th = r['theory_pure_ebd']['n_unst']
            nu = r['numerical_pure_ebd']['morse_index']
            me = r['numerical_pure_ebd']['min_eig']
            tag = "PASS" if r.get('pure_match') else "FAIL"
            print(f"{r['beta']:>8} {th:>8d} {nu:>8d} {me:>10.3f} {tag:>8}")

    if not args.skip_full:
        print(f"\n{'='*88}")
        print("FULL E COMPARISON TABLE (Prop 1.3 with canonical cl/sep)")
        print(f"{'='*88}")
        print(f"{'β':>8} {'N_pure':>8} {'N_full':>8} {'Δ=N_f-N_p':>12} "
              f"{'cl_sep min_eig':>16}")
        print("-" * 88)
        for r in results:
            if 'numerical_full' in r and 'error' not in r['numerical_full']:
                np_ = r['numerical_pure_ebd']['morse_index']
                nf_ = r['numerical_full']['morse_index']
                cs_min = r['cl_sep_hessian']['min_eig']
                print(f"{r['beta']:>8} {np_:>8d} {nf_:>8d} {nf_ - np_:>12d} "
                      f"{cs_min:>16.3f}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_hessian_uniform_v2',
            'round_ref': 'Round 12 Prop 1.3 v2 (pure E_bd isolation)',
            'params': vars(args),
            'n': n,
            'max_morse': max_morse,
            'W_ddot': W_ddot,
            'lap_eigs_first10': lap_eigs[:10].tolist(),
            'beta_crit_k_pure': beta_crit_k,
            'results': results,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2, default=str)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
