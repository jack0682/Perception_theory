#!/usr/bin/env python3
"""
exp_hessian_uniform.py — Round 12 Proposition 1.3 direct validation.

Target claim (Round 12 §1.5.3):
  Morse index of u_uniform = c·1 on Σ_m at temperature T=0
  equals N_unst(β, α, T=0, c) = #{k ≥ 2 : μ_k < 0}
  where μ_k = β W''(c) + 4α λ_k(G) + r_cl_sep (T=0 case).

Critical gap identified in exp audit (Round 14 §3.7):
  No existing experiment measures Hessian spectrum AT u_uniform directly.
  exp37 validates β_crit (k=2 boundary) only.
  exp62/63 measure Hessian at K=2 symmetric point, not at uniform.

This experiment:
  1. Construct u_uniform = c·1 ∈ Σ_m (no find_formation).
  2. Compute full constrained Hessian H on 1^⊥ via finite-difference on gradient.
  3. Count negative eigenvalues (Morse index).
  4. Compare with theoretical N_unst(β).
  5. Scan β values crossing multiple β_crit^(k) thresholds.

Expected runtime: ~5-15 min on 8x8 grid (full Hessian construction).
Larger grids (12x12, 16x16) scale as O(n²) in energy evaluations.

Usage:
  cd CODE && python3 experiments/exp_hessian_uniform.py [--grid-size 8] [--betas ...]
"""
import sys, os, time, json, argparse
import numpy as np
from scipy.sparse.csgraph import laplacian

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer


def double_well_second_derivative(c):
    """W(u) = u²(1-u)², W''(u) = 12u² - 12u + 2. W''(c) for c in spinodal < 0."""
    return 12.0 * c * c - 12.0 * c + 2.0


def compute_graph_laplacian_spectrum(graph):
    """Compute full Laplacian spectrum of graph G = (X, W)."""
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.asarray(graph.W)
    L = np.diag(W.sum(axis=1)) - W
    # Ensure symmetric
    L = 0.5 * (L + L.T)
    eigs = np.linalg.eigvalsh(L)
    eigs = np.sort(eigs)
    return eigs


def predict_N_unst(lap_eigs, beta, alpha, c, r_cl_sep):
    """Theoretical N_unst from Round 12 Prop 1.3.

    μ_k = β W''(c) + 4α λ_k + r_cl_sep
    Unstable iff μ_k < 0, i.e., 4α λ_k < -β W''(c) - r_cl_sep = β|W''(c)| - r_cl_sep
    (since W''(c) < 0 in spinodal).
    """
    W_ddot = double_well_second_derivative(c)  # W''(c), negative in spinodal
    # Exclude lowest eigenvalue (λ_1 = 0, constant direction, removed by Σ_m projection)
    nontrivial_eigs = lap_eigs[1:]
    threshold = (beta * abs(W_ddot) - r_cl_sep) / (4.0 * alpha)
    n_unst = int(np.sum(nontrivial_eigs < threshold))
    mu_k = beta * W_ddot + 4.0 * alpha * nontrivial_eigs + r_cl_sep
    return {
        'n_unst': n_unst,
        'threshold_lambda': float(threshold),
        'W_ddot': float(W_ddot),
        'mu_k_values': mu_k.tolist(),
        'num_mu_negative': int(np.sum(mu_k < 0)),
    }


def compute_hessian_fd(ec, u, graph, eps=1e-5):
    """Compute full Hessian matrix via FD on gradient.

    Tries multiple scc API patterns:
      - ec.energy(u) returns (E, grad)
      - ec.gradient(u) returns grad
      - fallback: central FD on energy (O(n²) evals, slower)

    Returns symmetric n×n Hessian.
    """
    n = len(u)

    # Try to get gradient
    grad_fn = None
    try:
        out = ec.energy(u)
        if isinstance(out, tuple) and len(out) == 2 and out[1] is not None:
            g_test = out[1]
            if hasattr(g_test, '__len__') and len(g_test) == n:
                grad_fn = lambda uu: ec.energy(uu)[1]
    except Exception:
        pass

    if grad_fn is None:
        try:
            g_test = ec.gradient(u)
            if hasattr(g_test, '__len__') and len(g_test) == n:
                grad_fn = ec.gradient
        except Exception:
            pass

    if grad_fn is not None:
        print(f"  Using analytic gradient via FD (O(n) grad calls)")
        H = np.zeros((n, n))
        g0 = np.asarray(grad_fn(u))
        for i in range(n):
            u_plus = u.copy()
            u_plus[i] += eps
            g_plus = np.asarray(grad_fn(u_plus))
            H[:, i] = (g_plus - g0) / eps
        H = 0.5 * (H + H.T)
        return H

    # Fallback: pure FD on energy (O(n²) energy calls, slow)
    print(f"  FALLBACK: FD on energy (O(n²) evals, slow for n>100)")
    H = np.zeros((n, n))
    E0 = ec.energy(u)
    if isinstance(E0, tuple):
        E0 = E0[0]
    E0 = float(E0)

    for i in range(n):
        for j in range(i, n):
            if i == j:
                u_p = u.copy(); u_p[i] += eps
                u_m = u.copy(); u_m[i] -= eps
                Ep = ec.energy(u_p); Ep = Ep[0] if isinstance(Ep, tuple) else Ep
                Em = ec.energy(u_m); Em = Em[0] if isinstance(Em, tuple) else Em
                H[i, i] = (float(Ep) + float(Em) - 2*E0) / (eps * eps)
            else:
                u_pp = u.copy(); u_pp[i] += eps; u_pp[j] += eps
                u_mm = u.copy(); u_mm[i] -= eps; u_mm[j] -= eps
                u_pm = u.copy(); u_pm[i] += eps; u_pm[j] -= eps
                u_mp = u.copy(); u_mp[i] -= eps; u_mp[j] += eps
                Epp = ec.energy(u_pp); Epp = Epp[0] if isinstance(Epp, tuple) else Epp
                Emm = ec.energy(u_mm); Emm = Emm[0] if isinstance(Emm, tuple) else Emm
                Epm = ec.energy(u_pm); Epm = Epm[0] if isinstance(Epm, tuple) else Epm
                Emp = ec.energy(u_mp); Emp = Emp[0] if isinstance(Emp, tuple) else Emp
                H[i, j] = (float(Epp) + float(Emm) - float(Epm) - float(Emp)) / (4 * eps * eps)
                H[j, i] = H[i, j]
    return H


def project_onto_volume_tangent(H, n):
    """Project Hessian onto 1^⊥ (volume-preserving tangent space).

    H_proj = P H P where P = I - (1/n) 11^T.
    """
    one = np.ones(n) / np.sqrt(n)
    P = np.eye(n) - np.outer(one, one)
    return P @ H @ P


def morse_index_on_tangent(H, n, tol=1e-6):
    """Count negative eigenvalues of H restricted to 1^⊥ (tangent of Σ_m)."""
    H_tan = project_onto_volume_tangent(H, n)
    eigs = np.linalg.eigvalsh(H_tan)
    eigs_sorted = np.sort(eigs)
    # Drop the one ~0 eigenvalue corresponding to the constant direction we projected out
    # (the projection makes it exactly 0, or near-0 numerically)
    # Count negatives with tolerance
    n_neg = int(np.sum(eigs_sorted < -tol))
    n_zero = int(np.sum(np.abs(eigs_sorted) <= tol))
    n_pos = int(np.sum(eigs_sorted > tol))
    return {
        'morse_index': n_neg,
        'n_zero': n_zero,
        'n_pos': n_pos,
        'min_eig': float(eigs_sorted[0]),
        'max_eig': float(eigs_sorted[-1]),
        'eigs_sorted': eigs_sorted.tolist(),
    }


def run_single(grid_size, beta, alpha, c, r_cl_sep_est):
    """One (grid, β, α) run: compute Hessian at u_uniform, count Morse index."""
    n = grid_size * grid_size
    graph = GraphState.grid_2d(grid_size, grid_size)

    # Theoretical: Laplacian spectrum
    lap_eigs = compute_graph_laplacian_spectrum(graph)
    theory = predict_N_unst(lap_eigs, beta, alpha, c, r_cl_sep_est)

    # Numerical: Hessian at u_uniform
    u_uniform = c * np.ones(n)

    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=100,
    )
    ec = EnergyComputer(graph, params)

    t0 = time.time()
    H = compute_hessian_fd(ec, u_uniform, graph)
    morse = morse_index_on_tangent(H, n)
    dt = time.time() - t0

    return {
        'grid_size': grid_size, 'n': n,
        'beta': beta, 'alpha': alpha, 'c': c,
        'lap_eigs_first6': lap_eigs[:6].tolist(),
        'lap_lambda_2': float(lap_eigs[1]) if len(lap_eigs) > 1 else None,
        'theory': theory,
        'numerical': morse,
        'match': morse['morse_index'] == theory['n_unst'],
        'time_sec': round(dt, 2),
    }


def main():
    parser = argparse.ArgumentParser(description='Round 12 Prop 1.3 Hessian-at-uniform validation')
    parser.add_argument('--grid-size', type=int, default=8)
    parser.add_argument('--c', type=float, default=0.5, help='uniform volume fraction (in spinodal)')
    parser.add_argument('--alpha', type=float, default=1.0)
    parser.add_argument('--r-cl-sep', type=float, default=0.125,
                        help='closure+sep contribution at uniform (canonical default ≈ 0.125)')
    parser.add_argument('--betas', type=str,
                        default='1.0,2.0,5.0,10.0,15.0,20.0,30.0,50.0,100.0')
    parser.add_argument('--output', default='experiments/results/exp_hessian_uniform.json')
    args = parser.parse_args()

    betas = [float(x) for x in args.betas.split(',')]

    # Pre-compute β_crit^{(k)} for k=2..6 for reference
    graph = GraphState.grid_2d(args.grid_size, args.grid_size)
    lap_eigs = compute_graph_laplacian_spectrum(graph)
    W_ddot = double_well_second_derivative(args.c)
    beta_crit_k = []
    for k in range(1, min(7, len(lap_eigs))):
        # β_crit^(k+1) : 4α λ_{k+1} = β |W''(c)| - r_cl_sep
        beta_k = (4.0 * args.alpha * lap_eigs[k] + args.r_cl_sep) / abs(W_ddot)
        beta_crit_k.append({'k': k + 1, 'lambda_k': float(lap_eigs[k]), 'beta_crit': float(beta_k)})

    print("=" * 78)
    print(f"Round 12 Proposition 1.3 validation (Morse index at u_uniform)")
    print(f"Grid: {args.grid_size}x{args.grid_size} (n={args.grid_size**2}), "
          f"c={args.c}, α={args.alpha}, r_cl_sep={args.r_cl_sep}")
    print(f"W''(c) = {W_ddot:.4f}")
    print(f"Theoretical β_crit thresholds (first 6 modes):")
    for bk in beta_crit_k:
        print(f"  k={bk['k']}: λ_k={bk['lambda_k']:.4f}, β_crit^(k)={bk['beta_crit']:.4f}")
    print(f"β values scanned: {betas}")
    print("=" * 78)

    results = []
    t_total = time.time()

    for beta in betas:
        print(f"\n--- β={beta} ---")
        try:
            r = run_single(args.grid_size, beta, args.alpha, args.c, args.r_cl_sep)
            results.append(r)
            th = r['theory']
            nm = r['numerical']
            match = "✓ MATCH" if r['match'] else "✗ MISMATCH"
            print(f"  Theory N_unst = {th['n_unst']},  Numerical Morse = {nm['morse_index']}  {match}")
            print(f"  (min_eig={nm['min_eig']:.4f}, max_eig={nm['max_eig']:.4f})")
            print(f"  time={r['time_sec']}s")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            results.append({'beta': beta, 'error': str(e)})

    # Summary table
    print(f"\n{'='*78}")
    print(f"{'β':>8} {'N_unst(theory)':>16} {'Morse(numerical)':>18} {'match':>8}")
    print("-" * 78)
    for r in results:
        if 'error' in r:
            print(f"{r['beta']:>8} {'ERROR':>16}")
            continue
        th = r['theory']['n_unst']
        nm = r['numerical']['morse_index']
        ok = "PASS" if r['match'] else "FAIL"
        print(f"{r['beta']:>8} {th:>16d} {nm:>18d} {ok:>8}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_hessian_uniform',
            'round_ref': 'Round 12 Prop 1.3 validation',
            'params': vars(args),
            'beta_crit_k': beta_crit_k,
            'results': results,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
