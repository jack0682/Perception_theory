#!/usr/bin/env python3
"""
exp_x3_mirror_ic.py — Test E1 (Initial Condition Sign Bias) vs E3 (Static Cubic Asymmetry).

## Experimental question
R19 observed that K̂(c=0.7) ≠ K̂(c=0.3) despite the energy's exact u↔1-u symmetry.
Competing attribution:
  E1 (dynamic, 80%): Noise realization ξ_k has sign bias under protocol.
                     Same seed ξ at c and 1-c yields DIFFERENT trajectories.
  E3 (static, 20%): Prop 1.3b (d) cubic term γ_D'' flips sign at c=0.5,
                     giving 2.5× factor in N^sep_unst between c and 1-c.
                     But 2.5× cannot produce observed ∞-ratio (K̂=4.76 vs 1.00).

## Method — Seed-Matched Mirroring
For each seed k ∈ {0, ..., N_seeds-1}:
  1. Generate xi_k ~ N(0, I) from RandomState(k)
  2. Run Condition A (c=0.3, standard): u_init = 0.3·1 + eps·xi_k
  3. Run Condition B (c=0.7, standard): u_init = 0.7·1 + eps·xi_k  (same xi!)
  4. Run Condition C (c=0.7, mirrored): u_init = 1 - [0.3·1 + eps·xi_k] = 0.7·1 - eps·xi_k

Compare K̂ distributions across A, B, C:
  - If E1 primary: K̂_C ≈ K̂_A (mirroring restores c=0.3 statistics)
  - If E3 primary: K̂_C ≈ K̂_B (static asymmetry persists regardless of IC)

## Configs
- 2D square 32×32 at β=0.5 (where R19 showed 4.76 vs 1.00 strongest contrast)
- (optional) 1D cycle C_1024 at β=0.5 (29 vs 1.00 - even larger contrast)
- N_seeds=50 (matching R17/R19 statistics)

## Runtime
- 50 seeds × 3 conditions × 1 graph = 150 runs at n=1024 (2D) or 1024 (1D)
- Each ~10-30s → ~45-90 min serial
- With --workers 6: ~8-15 min

## Usage
  cd CODE && python3 experiments/exp_x3_mirror_ic.py --workers 6
"""
import os
# P0 FIX: BLAS thread caps BEFORE numpy import (setdefault was ineffective for inherited env)
os.environ['OMP_NUM_THREADS'] = os.environ.get('OMP_NUM_THREADS_WORKER', '1')
os.environ['OPENBLAS_NUM_THREADS'] = os.environ.get('OPENBLAS_NUM_THREADS_WORKER', '1')
os.environ['VECLIB_MAXIMUM_THREADS'] = os.environ.get('VECLIB_MAXIMUM_THREADS_WORKER', '1')
os.environ['MKL_NUM_THREADS'] = os.environ.get('MKL_NUM_THREADS_WORKER', '1')

import sys, json, argparse, time, threading
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import _optimize_single_from, project_volume


def build_square_free(L: int) -> GraphState:
    return GraphState.grid_2d(L, L)


def build_cycle_1d(n: int) -> GraphState:
    row = np.concatenate([np.arange(n), np.arange(n)])
    col = np.concatenate([(np.arange(n) + 1) % n, (np.arange(n) - 1) % n])
    data = np.ones(2 * n)
    adj = sp.csr_matrix((data, (row, col)), shape=(n, n))
    return GraphState(adj)


def count_formations_square(u: np.ndarray, L: int, threshold: float = 0.5) -> int:
    """Count connected components above threshold on 2D square (4-connected)."""
    grid = (u.reshape(L, L) > threshold).astype(np.int32)
    visited = np.zeros_like(grid)
    count = 0
    for i in range(L):
        for j in range(L):
            if grid[i, j] == 1 and visited[i, j] == 0:
                count += 1
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < L and 0 <= y < L and grid[x, y] == 1 and visited[x, y] == 0:
                        visited[x, y] = 1
                        stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    return count


def count_formations_cycle(u: np.ndarray, threshold: float = 0.5) -> int:
    above = u > threshold
    if not np.any(above):
        return 0
    if np.all(above):
        return 1
    diff = np.diff(np.concatenate([above[-1:], above.astype(int)]))
    return int(np.sum(diff == 1))


def run_one_condition(task):
    """Worker: run one (graph, c, seed, mirror) condition."""
    (idx, n_total, graph_name, graph_spec, c, seed, condition,
     beta, alpha, eps_init, n_iter) = task
    # BLAS thread caps already set at module level (top of file), workers inherit via spawn

    t_start = time.time()

    # Rebuild graph in worker (sparse matrices pickle OK but rebuild is cheap)
    if graph_name == 'square':
        L = graph_spec
        graph = build_square_free(L)
        count_fn = lambda u: count_formations_square(u, L)
    elif graph_name == 'cycle':
        n = graph_spec
        graph = build_cycle_1d(n)
        count_fn = count_formations_cycle
    else:
        raise ValueError(f"unknown graph: {graph_name}")

    n = graph.n
    m = c * n

    # Generate noise from seed (identical xi_k across conditions A, B, C)
    rng = np.random.RandomState(seed)
    xi = rng.randn(n)

    # Construct init based on condition
    if condition == 'A_c03_std':
        u_init_pre = 0.3 + eps_init * xi
    elif condition == 'B_c07_std':
        u_init_pre = 0.7 + eps_init * xi
    elif condition == 'C_c07_mirror':
        u_init_pre = 0.7 - eps_init * xi
    elif condition == 'D_c03_mirror':
        u_init_pre = 0.3 - eps_init * xi
    else:
        raise ValueError(f"unknown condition: {condition}")

    # P0 FIX: Assert clipping is inactive (required for project_volume to preserve mirror symmetry)
    pre_min, pre_max = float(u_init_pre.min()), float(u_init_pre.max())
    n_clipped = int(np.sum((u_init_pre < 0.0) | (u_init_pre > 1.0)))
    if n_clipped > 0:
        return idx, {
            'graph': graph_name, 'c': c, 'seed': seed, 'condition': condition,
            'error': (f'u_init_pre out of [0,1]: min={pre_min:.4f} max={pre_max:.4f} '
                     f'n_clipped={n_clipped}. Reduce eps_init to preserve mirror symmetry.'),
            'success': False, 'elapsed_sec': 0.0,
        }

    u_init = project_volume(u_init_pre, m)

    # Run optimization
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=n_iter, n_restarts=1,
        dt_init=0.01, eps_init=eps_init,
    )
    ec = EnergyComputer(graph, params)

    # P1 FIX: apply Hessian normalization to match R17/R19 protocol (find_formation default)
    # Without this, effective weights differ → K̂ asymmetry from R19 is not reproduced
    try:
        ec.normalize_weights()
    except Exception as exc:
        return idx, {
            'graph': graph_name, 'c': c, 'seed': seed, 'condition': condition,
            'error': f'normalize_weights failed: {exc}',
            'success': False, 'elapsed_sec': 0.0,
        }

    try:
        u_final, E_final, terms, _, _, converged, iters = _optimize_single_from(
            graph, params, ec, u_init
        )
        K = count_fn(u_final)
        elapsed = time.time() - t_start
        return idx, {
            'graph': graph_name, 'graph_spec': graph_spec,
            'c': c, 'seed': seed, 'condition': condition,
            'beta': beta, 'alpha': alpha, 'eps_init': eps_init,
            'K': K,
            'energy': float(E_final),
            'converged': converged, 'iters': iters,
            'elapsed_sec': elapsed,
            'success': True,
        }
    except Exception as exc:
        elapsed = time.time() - t_start
        return idx, {
            'graph': graph_name, 'c': c, 'seed': seed, 'condition': condition,
            'beta': beta, 'error': str(exc), 'elapsed_sec': elapsed, 'success': False,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L-square', type=int, default=32, help='2D square side length')
    ap.add_argument('--n-cycle', type=int, default=1024, help='1D cycle length')
    ap.add_argument('--beta', type=float, default=0.5)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--eps-init', type=float, default=0.01)
    ap.add_argument('--seeds', type=int, default=50)
    ap.add_argument('--n-iter', type=int, default=5000)
    ap.add_argument('--skip-square', action='store_true')
    ap.add_argument('--skip-cycle', action='store_true')
    ap.add_argument('--workers', type=int, default=1)
    ap.add_argument('--out', default='results/exp_x3_mirror_ic.json')
    args = ap.parse_args()

    # P1 FIX: 4 conditions — A (c=0.3 std), B (c=0.7 std), C (c=0.7 mirror=1-A), D (c=0.3 mirror=1-B)
    # D added for bidirectional symmetry test (E1 hypothesis requires both directions to hold)
    conditions = ['A_c03_std', 'B_c07_std', 'C_c07_mirror', 'D_c03_mirror']

    # Build task list
    tasks = []
    idx = 0
    graphs = []
    if not args.skip_square:
        graphs.append(('square', args.L_square))
    if not args.skip_cycle:
        graphs.append(('cycle', args.n_cycle))

    if not graphs:
        sys.exit('[x3] ERROR: no graphs selected (--skip-square + --skip-cycle). Nothing to run.')

    for graph_name, graph_spec in graphs:
        for cond in conditions:
            c_value = 0.3 if cond in ('A_c03_std', 'D_c03_mirror') else 0.7
            for seed in range(args.seeds):
                tasks.append((idx, 0, graph_name, graph_spec, c_value, seed,
                            cond, args.beta, args.alpha, args.eps_init, args.n_iter))
                idx += 1

    # Patch n_total
    tasks = [(t[0], len(tasks), *t[2:]) for t in tasks]

    print(f"[x3] E1 vs E3 asymmetry attribution via seed-mirrored IC")
    print(f"[x3] β={args.beta}, α={args.alpha}, eps_init={args.eps_init}")
    print(f"[x3] {args.seeds} seeds × {len(conditions)} conditions × {len(graphs)} graphs = {len(tasks)} runs")
    print(f"[x3] workers={args.workers}")
    print()

    t0 = time.time()
    results = [None] * len(tasks)

    # Progress reporter (parent thread)
    last_report = [t0]
    completed_count = [0]

    def progress_update(idx, res):
        completed_count[0] += 1
        now = time.time()
        if now - last_report[0] > 10 or completed_count[0] == len(tasks):
            pct = 100.0 * completed_count[0] / len(tasks)
            eta = (now - t0) * (len(tasks) - completed_count[0]) / max(completed_count[0], 1)
            print(f"  [x3 progress] {completed_count[0]}/{len(tasks)} ({pct:.1f}%), "
                  f"elapsed {now-t0:.0f}s, ETA {eta:.0f}s", flush=True)
            last_report[0] = now

    if args.workers <= 1:
        for task in tasks:
            idx, res = run_one_condition(task)
            results[idx] = res
            progress_update(idx, res)
    else:
        import multiprocessing as mp
        ctx = mp.get_context('spawn')
        with ctx.Pool(processes=args.workers) as pool:
            for idx, res in pool.imap_unordered(run_one_condition, tasks):
                results[idx] = res
                progress_update(idx, res)

    elapsed = time.time() - t0

    # Aggregate statistics per (graph, condition)
    summary = {}
    for graph_name, graph_spec in graphs:
        for cond in conditions:
            c_value = 0.3 if cond in ('A_c03_std', 'D_c03_mirror') else 0.7
            ks = [r['K'] for r in results
                  if r and r.get('success')
                  and r.get('graph') == graph_name and r.get('condition') == cond]
            if ks:
                unique_vals, counts = np.unique(ks, return_counts=True)
                summary[f'{graph_name}_{cond}'] = {
                    'c': c_value, 'n_seeds': len(ks),
                    'K_mean': float(np.mean(ks)), 'K_std': float(np.std(ks)),
                    'K_min': int(np.min(ks)), 'K_max': int(np.max(ks)),
                    'K_distribution': {int(k): int(v) for k, v in zip(unique_vals, counts)},
                }

    output = {
        'session': '2026-04-22_X3_mirror_ic',
        'purpose': 'E1 vs E3 attribution via seed-mirrored IC',
        'config': vars(args),
        'results': results,
        'summary': {k: {kk: (int(vv) if isinstance(vv, (np.int64, np.int32)) else vv)
                      for kk, vv in v.items() if kk != 'K_distribution'}
                   for k, v in summary.items()},
        'K_distributions': {k: {str(int(kk)): int(vv) for kk, vv in v['K_distribution'].items()}
                         for k, v in summary.items()},
        'total_elapsed_sec': elapsed,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n[x3] done in {elapsed:.1f}s. Wrote {out_path}")
    print("\n--- K̂ distribution summary ---")
    print(f"{'Condition':>20} | {'n':>3} | {'K_mean ± K_std':>18} | {'range':>8}")
    print("-" * 65)
    for key, v in summary.items():
        print(f"{key:>20} | {v['n_seeds']:>3} | "
              f"{v['K_mean']:>7.3f} ± {v['K_std']:>6.3f} | "
              f"{v['K_min']:>2}-{v['K_max']:>2}")

    # Interpretation with Mann-Whitney U-test (P1 FIX: replaces brittle 10% heuristic)
    print("\n--- Interpretation (Mann-Whitney U, two-sided) ---")
    from scipy.stats import mannwhitneyu
    for graph_name, _ in graphs:
        kvals = {}
        for cond in conditions:
            ks = [r['K'] for r in results
                  if r and r.get('success') and r.get('graph') == graph_name and r.get('condition') == cond]
            if ks:
                kvals[cond] = ks

        A = kvals.get('A_c03_std')
        B = kvals.get('B_c07_std')
        C = kvals.get('C_c07_mirror')
        D = kvals.get('D_c03_mirror')

        if not (A and B and C):
            continue
        print(f"\n  {graph_name}:  A={np.mean(A):.2f}  B={np.mean(B):.2f}  C={np.mean(C):.2f}" + (f"  D={np.mean(D):.2f}" if D else ""))

        # Forward direction: does mirrored c=0.7 IC give c=0.3 statistics?
        try:
            _, p_CA = mannwhitneyu(C, A, alternative='two-sided')
            _, p_CB = mannwhitneyu(C, B, alternative='two-sided')
            print(f"    P(K_C = K_A) = {p_CA:.4g}  (if high → E1 supported)")
            print(f"    P(K_C = K_B) = {p_CB:.4g}  (if high → E3 supported)")
        except ValueError as exc:
            print(f"    Mann-Whitney failed: {exc}")
            p_CA, p_CB = None, None

        # Backward direction (if D available): does mirrored c=0.3 IC give c=0.7 statistics?
        if D:
            try:
                _, p_DB = mannwhitneyu(D, B, alternative='two-sided')
                _, p_DA = mannwhitneyu(D, A, alternative='two-sided')
                print(f"    P(K_D = K_B) = {p_DB:.4g}  (if high → E1 bidirectional)")
                print(f"    P(K_D = K_A) = {p_DA:.4g}  (if high → E3 bidirectional)")
            except ValueError as exc:
                p_DB, p_DA = None, None

        # Verdict
        ALPHA = 0.05
        if p_CA is not None and p_CB is not None:
            if p_CA > ALPHA and p_CB < ALPHA:
                print(f"    → **E1 PRIMARY** on {graph_name} (mirroring restores c=0.3 stats, distinct from c=0.7)")
            elif p_CA < ALPHA and p_CB > ALPHA:
                print(f"    → **E3 PRIMARY** on {graph_name} (static asymmetry persists under mirroring)")
            elif p_CA > ALPHA and p_CB > ALPHA:
                print(f"    → AMBIGUOUS: K_A and K_B distributions not distinguishable (need more seeds or contrast)")
            else:
                print(f"    → MIXED: K_C differs from both K_A and K_B (intermediate regime)")


if __name__ == '__main__':
    main()
