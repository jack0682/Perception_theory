#!/usr/bin/env python3
"""
exp_x1_v7_predictions.py — Test 3 predictions of F1-SSU-v3/v4.

Prediction 1: Softmax crossover at bistable β
  P(K̂=k | β) follows softmax around transition β_c.
  Test: β ∈ {8.8, 8.9, 8.95, 9.0, 9.05, 9.1, 9.2} × 50 seeds.

Prediction 2: Selector transition width ∝ noise level
  Transition width in β should scale with eps_init.
  Test: eps ∈ {0.001, 0.01, 0.1} at fine β scan around β_c≈7.08.

Prediction 3: Multi-basin geometry at fixed β
  Fixed β=9.0, 200 seeds → histogram K̂ → reveal basin probability map.
"""
import os
os.environ['OMP_NUM_THREADS'] = '2'
os.environ['OPENBLAS_NUM_THREADS'] = '2'
os.environ['VECLIB_MAXIMUM_THREADS'] = '2'
os.environ['MKL_NUM_THREADS'] = '2'

import sys, json, argparse, time
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import _optimize_single, find_formation
from scc.energy import EnergyComputer


def build_cycle_1d(n: int) -> GraphState:
    row = np.concatenate([np.arange(n), np.arange(n)])
    col = np.concatenate([(np.arange(n) + 1) % n, (np.arange(n) - 1) % n])
    data = np.ones(2 * n)
    adj = sp.csr_matrix((data, (row, col)), shape=(n, n))
    return GraphState(adj)


def count_cycle(u: np.ndarray, threshold: float = 0.5) -> int:
    above = u > threshold
    if not np.any(above):
        return 0
    if np.all(above):
        return 1
    diff = np.diff(np.concatenate([above[-1:], above.astype(int)]))
    return int(np.sum(diff == 1))


def run_single(graph, c, alpha, beta, eps_init, seed, max_iter=10000):
    """Run one realization: find_formation from random-noise init seed, return K and E."""
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=max_iter, n_restarts=1,
        dt_init=0.01, eps_init=eps_init,
    )
    ec = EnergyComputer(graph, params)

    u, E, _, _, _, conv, _ = _optimize_single(graph, params, ec, seed=seed)
    K = count_cycle(u)
    return K, float(E), bool(conv)


def worker(args):
    idx, n_total, n_graph, c, alpha, beta, eps_init, seed, max_iter = args
    try:
        graph = build_cycle_1d(n_graph)
        K, E, conv = run_single(graph, c, alpha, beta, eps_init, seed, max_iter)
        return idx, {
            'beta': beta, 'eps_init': eps_init, 'seed': seed,
            'K': K, 'E': E, 'converged': conv, 'success': True,
        }
    except Exception as exc:
        return idx, {
            'beta': beta, 'eps_init': eps_init, 'seed': seed,
            'error': str(exc), 'success': False,
        }


def run_sweep(beta_list, eps_init, seeds, n_graph, c, alpha, max_iter, workers, label=''):
    """Run (β × seed) × (single eps_init)."""
    tasks = []
    idx = 0
    for beta in beta_list:
        for seed in range(seeds):
            tasks.append((idx, 0, n_graph, c, alpha, beta, eps_init, seed, max_iter))
            idx += 1
    tasks = [(t[0], len(tasks), *t[2:]) for t in tasks]

    print(f"[{label}] {len(tasks)} runs ({len(beta_list)} β × {seeds} seeds, eps={eps_init})")
    results = [None] * len(tasks)
    t0 = time.time()
    completed = [0]
    last_report = [t0]

    def report(idx, res):
        completed[0] += 1
        now = time.time()
        if now - last_report[0] > 8 or completed[0] == len(tasks):
            pct = 100.0 * completed[0] / len(tasks)
            eta = (now - t0) * (len(tasks) - completed[0]) / max(completed[0], 1)
            print(f"  [{label}] {completed[0]}/{len(tasks)} ({pct:.1f}%), elapsed {now-t0:.0f}s, ETA {eta:.0f}s", flush=True)
            last_report[0] = now

    if workers <= 1:
        for task in tasks:
            idx, res = worker(task)
            results[idx] = res
            report(idx, res)
    else:
        import multiprocessing as mp
        ctx = mp.get_context('spawn')
        with ctx.Pool(processes=workers) as pool:
            for idx, res in pool.imap_unordered(worker, tasks):
                results[idx] = res
                report(idx, res)

    return results, time.time() - t0


def analyze_distribution(results):
    """Group by (β, eps_init) and compute K distribution per group."""
    groups = {}
    for r in results:
        if not r or not r.get('success'):
            continue
        key = (round(r['beta'], 4), round(r['eps_init'], 5))
        groups.setdefault(key, []).append(r['K'])
    return {key: ks for key, ks in groups.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=1024)
    ap.add_argument('--c', type=float, default=0.7)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--max-iter', type=int, default=10000)
    ap.add_argument('--workers', type=int, default=6)
    ap.add_argument('--test', choices=['p1', 'p2', 'p3', 'all'], default='all')
    ap.add_argument('--out', default='results/exp_x1_v7_predictions.json')
    args = ap.parse_args()

    output = {'session': '2026-04-22_X1_v7_predictions', 'config': vars(args)}
    t_start = time.time()

    # --- Prediction 1: Softmax at bistable β (R20 β=9 region) ---
    if args.test in ('p1', 'all'):
        print("\n" + "=" * 70)
        print("PREDICTION 1: Softmax crossover at β ≈ 9.0 (K=1 ↔ K=multi)")
        print("=" * 70)
        beta_p1 = [8.5, 8.7, 8.8, 8.9, 8.95, 9.0, 9.05, 9.1, 9.2, 9.3, 9.5]
        res_p1, elapsed_p1 = run_sweep(
            beta_p1, eps_init=0.01, seeds=50,
            n_graph=args.n, c=args.c, alpha=args.alpha,
            max_iter=args.max_iter, workers=args.workers, label='P1'
        )
        output['p1_results'] = res_p1
        output['p1_elapsed'] = elapsed_p1
        output['p1_beta_list'] = beta_p1

        dist_p1 = analyze_distribution(res_p1)
        print(f"\n--- P1 K̂ distribution per β (eps=0.01) ---")
        print(f"{'β':>6} | {'mean':>6} | {'std':>5} | {'P(K=1)':>8} | distribution")
        print("-" * 75)
        for beta in beta_p1:
            ks = dist_p1.get((round(beta, 4), 0.01), [])
            if not ks:
                continue
            ks_arr = np.array(ks)
            mean = ks_arr.mean()
            std = ks_arr.std()
            p_k1 = float((ks_arr == 1).sum()) / len(ks)
            unique, counts = np.unique(ks, return_counts=True)
            dist_str = ", ".join(f"K={int(u)}:{int(c)}" for u, c in zip(unique, counts))
            print(f"{beta:>6.2f} | {mean:>6.2f} | {std:>5.2f} | {p_k1:>8.3f} | {dist_str}")

    # --- Prediction 2: eps_init sensitivity ---
    if args.test in ('p2', 'all'):
        print("\n" + "=" * 70)
        print("PREDICTION 2: Selector transition width ∝ eps_init")
        print("=" * 70)
        beta_p2 = [6.95, 7.00, 7.03, 7.05, 7.07, 7.08, 7.10, 7.12, 7.15, 7.20]
        all_p2 = []
        output['p2_eps_list'] = [0.001, 0.01, 0.1]
        output['p2_beta_list'] = beta_p2
        for eps in [0.001, 0.01, 0.1]:
            print(f"\n  Running eps_init={eps}...")
            res, elapsed = run_sweep(
                beta_p2, eps_init=eps, seeds=30,
                n_graph=args.n, c=args.c, alpha=args.alpha,
                max_iter=args.max_iter, workers=args.workers, label=f'P2[eps={eps}]'
            )
            all_p2.extend(res)

            # Show HIGH-E fraction per β (captures branch selection)
            print(f"\n  --- P2 branch selection at eps={eps} ---")
            print(f"  {'β':>6} | {'E_mean':>8} | {'P(HIGH)':>8}")
            print("  " + "-" * 35)
            for beta in beta_p2:
                Es = [r['E'] for r in res if r.get('success') and round(r['beta'],4)==round(beta,4)]
                if not Es:
                    continue
                Es = np.array(Es)
                p_high = float((Es > 100).sum()) / len(Es)
                print(f"  {beta:>6.2f} | {Es.mean():>8.2f} | {p_high:>8.3f}")
        output['p2_results'] = all_p2

    # --- Prediction 3: Multi-basin geometry at fixed β ---
    if args.test in ('p3', 'all'):
        print("\n" + "=" * 70)
        print("PREDICTION 3: Basin geometry at β=9.0 (200 seeds)")
        print("=" * 70)
        res_p3, elapsed_p3 = run_sweep(
            [9.0], eps_init=0.01, seeds=200,
            n_graph=args.n, c=args.c, alpha=args.alpha,
            max_iter=args.max_iter, workers=args.workers, label='P3'
        )
        output['p3_results'] = res_p3
        output['p3_elapsed'] = elapsed_p3

        ks = [r['K'] for r in res_p3 if r.get('success')]
        if ks:
            ks_arr = np.array(ks)
            print(f"\n  --- P3 K̂ full histogram at β=9.0 (n={len(ks)}) ---")
            unique, counts = np.unique(ks, return_counts=True)
            for u, c in zip(unique, counts):
                bar = '█' * int(40.0 * c / len(ks))
                print(f"    K={int(u):>3} | {int(c):>3} ({100.0*c/len(ks):>5.1f}%) | {bar}")
            print(f"\n  mean={ks_arr.mean():.2f}, std={ks_arr.std():.2f}, range=[{ks_arr.min()}, {ks_arr.max()}]")

    total = time.time() - t_start
    output['total_elapsed'] = total

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n\n[v7] TOTAL DONE in {total:.1f}s. Wrote {out_path}")


if __name__ == '__main__':
    main()
