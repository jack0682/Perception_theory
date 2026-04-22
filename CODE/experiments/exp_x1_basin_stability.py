#!/usr/bin/env python3
"""
exp_x1_basin_stability.py — Test B1 (Secondary Bifurcation) + C Basin-Stability Hierarchy.

## Experimental question
For 1D cycle C_1024 at c=0.7, α=1.0:
- R20 observed K̂ transition at β_c ≈ 8.5 (K̂=1→4 between β=8 and β=9)
- N_unst at u_uniform saturates at β=8 and does NOT change at the transition
- Hypothesis B1 (Secondary Bifurcation): the K=1 minimizer u*_1 itself loses stability
  at β_c; its Hessian λ_min crosses zero

## Method
For each β in [7.0, 8.0, 8.5, 9.0, 9.5, 10.0, 12.0]:
  1. Find K=1 minimizer u*_1(β) via low-noise Fiedler-init gradient flow
  2. Compute smallest eigenvalue of Hess E at u*_1 (constrained to T Σ_m)
  3. Record λ_min

## Prediction (B1)
λ_min(u*_1; β=8) > 0   (K=1 is strict min)
λ_min(u*_1; β=9) ≤ 0   (K=1 has become saddle)
Zero-crossing somewhere in β ∈ (8, 9).

If λ_min > 0 at β=9 too: B1 refuted, B4 or B8 implicated.
If u*_1 cannot be found at β=9 (find_formation escapes): B3 (saddle-node) confirmed.

## Runtime estimate
- find_formation at C_1024: ~1-2 min per β
- eigsh (smallest eigenvalue via LinearOperator): ~2-4 min per β
- 7 β × ~5 min = ~30 min total serial
- With --workers 6: ~7 min (β configs are independent)

## Usage
  cd CODE && python3 experiments/exp_x1_basin_stability.py [--workers 6] [--n 1024]
"""
import os
# P0 FIX: Set BLAS thread caps BEFORE numpy/scipy import to actually take effect
os.environ['OMP_NUM_THREADS'] = os.environ.get('OMP_NUM_THREADS_WORKER', '2')
os.environ['OPENBLAS_NUM_THREADS'] = os.environ.get('OPENBLAS_NUM_THREADS_WORKER', '2')
os.environ['VECLIB_MAXIMUM_THREADS'] = os.environ.get('VECLIB_MAXIMUM_THREADS_WORKER', '2')
os.environ['MKL_NUM_THREADS'] = os.environ.get('MKL_NUM_THREADS_WORKER', '2')

import sys, json, argparse, time, threading, traceback
import numpy as np
from scipy.sparse.linalg import eigsh, LinearOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation
import scipy.sparse as sp


def build_cycle_1d(n: int) -> GraphState:
    """1D cycle C_n."""
    row = np.concatenate([np.arange(n), np.arange(n)])
    col = np.concatenate([(np.arange(n) + 1) % n, (np.arange(n) - 1) % n])
    data = np.ones(2 * n)
    adj = sp.csr_matrix((data, (row, col)), shape=(n, n))
    return GraphState(adj)


def count_formations_cycle(u: np.ndarray, threshold: float = 0.5) -> int:
    """Count connected arcs above threshold on 1D cycle."""
    above = u > threshold
    if not np.any(above):
        return 0
    if np.all(above):
        return 1
    # Count 0→1 transitions (cyclic)
    diff = np.diff(np.concatenate([above[-1:], above.astype(int)]))
    return int(np.sum(diff == 1))


def hessian_vec_product_factory(ec: EnergyComputer, u_star: np.ndarray,
                                h: float = 1e-5, central: bool = True):
    """Returns a callable Hv(v) computing Hess E @ v via finite differences,
    projected onto tangent T Σ_m (mean-zero subspace).

    P1 FIX: central=True by default, gives O(h^2) accuracy vs O(h) one-sided.
    Better for detecting near-zero eigenvalues (B1 test near β_c).
    h=1e-5 rather than 1e-6 — more robust to roundoff in gradient cancellation.
    """
    if not central:
        g0 = ec.gradient(u_star)
        def Hv(v: np.ndarray) -> np.ndarray:
            v_t = v - np.mean(v)
            g1 = ec.gradient(u_star + h * v_t)
            Hv_out = (g1 - g0) / h
            Hv_out -= np.mean(Hv_out)
            return Hv_out
    else:
        def Hv(v: np.ndarray) -> np.ndarray:
            v_t = v - np.mean(v)
            g_plus = ec.gradient(u_star + h * v_t)
            g_minus = ec.gradient(u_star - h * v_t)
            Hv_out = (g_plus - g_minus) / (2.0 * h)
            Hv_out -= np.mean(Hv_out)
            return Hv_out

    return Hv


def compute_lambda_min(ec: EnergyComputer, u_star: np.ndarray, n: int,
                      k_eigs: int = 3, tol: float = 1e-6, maxiter: int = 500) -> dict:
    """Compute k smallest algebraic eigenvalues of constrained Hessian at u_star.

    Uses shifted operator M = shift*I - H. eigsh with 'LM' gives k largest
    M-eigenvalues = k smallest H-eigenvalues.

    Returns multiple eigenvalues because on symmetric graphs (e.g., C_n)
    u*_1 has a Goldstone mode (eigenvalue = 0 from translation symmetry).
    The INTERPRETATIVE smallest eigenvalue is the second (first above Goldstone).
    """
    Hv = hessian_vec_product_factory(ec, u_star)

    # Estimate spectral radius to choose shift
    rng = np.random.RandomState(0)
    v = rng.randn(n)
    v -= np.mean(v)
    v /= np.linalg.norm(v)

    sigma_upper = 0.0
    for _ in range(30):
        w = Hv(v)
        nw = np.linalg.norm(w)
        if nw < 1e-15:
            break
        sigma_upper = nw
        v = w / nw

    shift = 2.0 * sigma_upper + 1.0

    def shifted_Hv(v):
        return shift * v - Hv(v)

    linop = LinearOperator((n, n), matvec=shifted_Hv, dtype=np.float64)

    # Start vector in tangent
    v0 = rng.randn(n)
    v0 -= np.mean(v0)
    v0 /= np.linalg.norm(v0)

    try:
        # Get k smallest H-eigenvalues
        vals_M, vecs_M = eigsh(linop, k=k_eigs, which='LM', tol=tol,
                              maxiter=maxiter, v0=v0)
        # Convert: λ_H = shift - λ_M
        eigs_H = sorted([shift - float(v) for v in vals_M])

        # Goldstone identification: eigenvalue very close to 0 (within tolerance)
        goldstone_threshold = max(1e-4, tol * shift * 10)
        goldstone_count = sum(1 for e in eigs_H if abs(e) < goldstone_threshold)

        # Stability-decisive eigenvalue: smallest NON-Goldstone
        nontrivial_eigs = [e for e in eigs_H if abs(e) >= goldstone_threshold]
        lambda_min_decisive = nontrivial_eigs[0] if nontrivial_eigs else eigs_H[0]

        return {
            'lambda_min_raw': eigs_H[0],  # Including Goldstone
            'eigenvalues_smallest': eigs_H,
            'goldstone_count': goldstone_count,
            'goldstone_threshold': goldstone_threshold,
            'lambda_min_decisive': lambda_min_decisive,  # Smallest non-Goldstone
            'shift_used': shift,
            'sigma_upper_estimate': sigma_upper,
            'success': True,
        }
    except Exception as exc:
        import traceback
        return {
            'lambda_min_raw': None,
            'lambda_min_decisive': None,
            'error': str(exc),
            'traceback': traceback.format_exc(),
            'success': False,
        }


def run_at_beta(args):
    """Worker: find u*_1 at given β, compute λ_min of Hessian.

    P0 FIX: skip Hessian if K != 1 (optimizer landed on wrong branch).
    P0 FIX: call find_formation with normalize=False to match raw-weight Hessian.
    P1 FIX: max_iter now configurable, default much higher to ensure convergence.
    """
    idx, n_total, beta, n_cycle, c, alpha, eps_init, max_iter = args

    print(f"  [{idx+1}/{n_total}] START β={beta:.1f} on C_{n_cycle}", flush=True)
    t_start = time.time()

    # Heartbeat
    _stop = threading.Event()
    def _hb():
        while not _stop.wait(8.0):
            elapsed = time.time() - t_start
            print(f"      ... β={beta:.1f} running (elapsed {elapsed:.0f}s)", flush=True)
    _thread = threading.Thread(target=_hb, daemon=True)
    _thread.start()

    try:
        graph = build_cycle_1d(n_cycle)
        params = ParameterRegistry(
            beta_bd=beta, volume_fraction=c,
            w_cl=1.0, w_sep=1.0, w_bd=alpha,
            max_iter=max_iter, n_restarts=1,  # Only Fiedler seed (seed=0)
            dt_init=0.01, eps_init=eps_init,
        )

        # Step 1: Find K=1 minimizer with low noise (Fiedler init = seed 0)
        # P0 FIX: normalize=False so raw-weight Hessian matches what u_star minimizes
        result = find_formation(graph, params, verbose=False, normalize=False)
        u_star = result.u
        converged_flag = bool(getattr(result, 'converged', False))
        final_gnorm = float(result.grad_norm_history[-1]) if getattr(result, 'grad_norm_history', None) else None

        # Verify K=1 via connected component count
        K_count = count_formations_cycle(u_star)
        energy = float(result.energy)

        # P0 FIX: Skip Hessian when K != 1 (optimizer landed on wrong branch)
        if K_count != 1:
            hess_info = {
                'success': False,
                'lambda_min_raw': None,
                'lambda_min_decisive': None,
                'error': f'K_count={K_count} != 1: Hessian would be at wrong critical point',
                'hess_skipped': True,
            }
        else:
            ec = EnergyComputer(graph, params)
            hess_info = compute_lambda_min(ec, u_star, n_cycle)

        elapsed = time.time() - t_start
        output = {
            'beta': beta,
            'K_observed': K_count,
            'energy': energy,
            'converged': converged_flag,
            'final_gnorm': final_gnorm,
            'elapsed_sec': elapsed,
            **hess_info,
        }

        _stop.set()

        if K_count == 1:
            status = "K=1"
        else:
            status = f"K={K_count}! (SKIPPED eigsh — wrong branch)"
        if hess_info.get('success'):
            lam_dec = hess_info.get('lambda_min_decisive')
            g_count = hess_info.get('goldstone_count', 0)
            lam_str = f"λ_min_dec={lam_dec:.6f} (Goldstone modes: {g_count})"
        elif hess_info.get('hess_skipped'):
            lam_str = "λ_min SKIP"
        else:
            lam_str = "λ_min FAILED"
        print(f"  [{idx+1}/{n_total}] DONE β={beta:.1f}: {status}, {lam_str} ({elapsed:.1f}s)", flush=True)
        return idx, output

    except Exception as exc:
        _stop.set()
        elapsed = time.time() - t_start
        err = traceback.format_exc()
        print(f"  [{idx+1}/{n_total}] ERROR β={beta:.1f}: {exc} ({elapsed:.1f}s)", flush=True)
        return idx, {
            'beta': beta, 'success': False, 'error': str(exc), 'traceback': err,
            'elapsed_sec': elapsed,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=1024, help='Cycle length (default 1024)')
    ap.add_argument('--c', type=float, default=0.7)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--eps-init', type=float, default=0.01,
                    help='Noise amplitude for Fiedler initialization')
    ap.add_argument('--beta-list', type=str,
                    default='7.0,8.0,8.5,9.0,9.5,10.0,12.0',
                    help='Comma-separated β values')
    ap.add_argument('--max-iter', type=int, default=30000,
                    help='Max gradient-flow iterations (default 30000, was 5000)')
    ap.add_argument('--workers', type=int, default=1)
    ap.add_argument('--out', default='results/exp_x1_basin_stability.json')
    args = ap.parse_args()

    beta_list = [float(b.strip()) for b in args.beta_list.split(',') if b.strip()]

    print(f"[x1] C_{args.n}, c={args.c}, α={args.alpha}, eps_init={args.eps_init}")
    print(f"[x1] β sweep: {beta_list}")
    print(f"[x1] max_iter: {args.max_iter}, workers: {args.workers}")

    t0 = time.time()
    tasks = [(i, len(beta_list), b, args.n, args.c, args.alpha, args.eps_init, args.max_iter)
             for i, b in enumerate(beta_list)]

    results = [None] * len(beta_list)
    if args.workers <= 1:
        for task in tasks:
            idx, res = run_at_beta(task)
            results[idx] = res
    else:
        import multiprocessing as mp
        ctx = mp.get_context('spawn')
        with ctx.Pool(processes=args.workers) as pool:
            for idx, res in pool.imap_unordered(run_at_beta, tasks):
                results[idx] = res

    elapsed = time.time() - t0

    output = {
        'session': '2026-04-22_X1_basin_stability',
        'purpose': 'Test B1 Secondary Bifurcation + C Basin-Stability Hierarchy',
        'config': {
            'n': args.n, 'c': args.c, 'alpha': args.alpha,
            'eps_init': args.eps_init, 'beta_list': beta_list,
        },
        'results': results,
        'total_elapsed_sec': elapsed,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n[x1] done in {elapsed:.1f}s. Wrote {out_path}")

    # Summary table
    print("\n--- Basin Stability Analysis: λ_min(u*_1) vs β ---")
    print(f"{'β':>6} | {'K':>3} | {'λ_min_decisive':>14} | {'λ_min_raw':>11} | {'Gold':>4} | {'energy':>10}")
    print("-" * 75)
    for r in results:
        if r is None:
            continue
        if r.get('success'):
            lam_dec = r.get('lambda_min_decisive')
            lam_raw = r.get('lambda_min_raw')
            K = r.get('K_observed')
            E = r.get('energy')
            g_ct = r.get('goldstone_count', 0)
            dec_str = f"{lam_dec:>14.6f}" if lam_dec is not None else "         N/A"
            raw_str = f"{lam_raw:>11.6f}" if lam_raw is not None else "      N/A"
            E_str = f"{E:>10.4f}" if E is not None else "       N/A"
            marker = "  ← SADDLE" if (lam_dec is not None and lam_dec < 0) else ""
            print(f"{r['beta']:>6.1f} | {K:>3} | {dec_str} | {raw_str} | {g_ct:>4} | {E_str}{marker}")
        else:
            print(f"{r.get('beta', '?'):>6} | FAIL: {r.get('error', 'unknown')}")

    print("\n--- B1 Secondary Bifurcation Prediction Check ---")
    # Find transition point
    decisive_series = [(r['beta'], r.get('lambda_min_decisive'))
                       for r in results if r and r.get('success') and r.get('lambda_min_decisive') is not None]
    sign_flip = None
    for i in range(len(decisive_series) - 1):
        b1, l1 = decisive_series[i]
        b2, l2 = decisive_series[i+1]
        if l1 > 0 and l2 < 0:
            sign_flip = (b1, b2)
            break
    if sign_flip:
        print(f"  ✓ λ_min_decisive zero-crossing detected in β ∈ ({sign_flip[0]}, {sign_flip[1]})")
        print(f"    → B1 Secondary Bifurcation hypothesis CONFIRMED")
    else:
        print(f"  ✗ No clear sign flip in λ_min_decisive across β range")
        if all(l > 0 for _, l in decisive_series):
            print(f"    → B1 refuted (all stable); B4/B8 implicated")
        elif all(l < 0 for _, l in decisive_series):
            print(f"    → u*_1 saddle across all β; transition happens below β_min")


if __name__ == '__main__':
    main()
