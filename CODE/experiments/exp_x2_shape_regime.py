#!/usr/bin/env python3
"""
exp_x2_shape_regime.py — Test D1 (α-Absolute Threshold) vs D7 (β/α Gradient-Stiffness Ratio).

## Experimental question
R21 discovered two shape regimes:
  Regime A (6/9 R21 configs): p ≥ 5 (fit saturated), sharp non-tanh
  Regime B (3/9): p ≈ 1.14-1.34, near-tanh (R²>0.999)

Regime B configs share: α ≥ 20 AND β ≤ 5.

Competing hypotheses (post-audit):
  D1: α-absolute threshold, α > α_c ⇒ Regime B
  D7 (NEW): 393·β/α < 100 ⇒ Regime B (stiffness ratio, β·|W''(c)|/(α·λ_2(L)))

D1 and D7 agree on most R21 configs BUT disagree on:
  (α=5, β=0.5):   D1 predicts A (low α);  D7 predicts B (393·0.5/5 = 39 < 100)
  (α=100, β=20):  D1 predicts B;           D7 predicts A (393·20/100 = 78.6 — marginal)
  (α=1, β=0.25):  D1 predicts A;           D7 predicts B (98 — marginal)

## Configs
4×4 grid: α ∈ {1, 5, 20, 100} × β ∈ {0.5, 2.5, 5, 20} = 16 configs

## Discriminators (MUST agree with one hypothesis)
  (α=5, β=0.5) — cleanest D1 A / D7 B split
  (α=100, β=0.5) — deep supra-lattice high-α check
  (α=1, β=0.5) — absolute-low-α check

## Runtime
  16 configs × ~60s each (48×48 grid, 24 n_inits) = ~16 min serial
  With --workers 6: ~3 min parallel

## Usage
  cd CODE && python3 experiments/exp_x2_shape_regime.py --workers 6
"""
import os
# P0 FIX: BLAS thread caps BEFORE numpy import (setdefault was ineffective for inherited env)
os.environ['OMP_NUM_THREADS'] = os.environ.get('OMP_NUM_THREADS_WORKER', '2')
os.environ['OPENBLAS_NUM_THREADS'] = os.environ.get('OPENBLAS_NUM_THREADS_WORKER', '2')
os.environ['VECLIB_MAXIMUM_THREADS'] = os.environ.get('VECLIB_MAXIMUM_THREADS_WORKER', '2')
os.environ['MKL_NUM_THREADS'] = os.environ.get('MKL_NUM_THREADS_WORKER', '2')

import sys, json, argparse, time, threading
import numpy as np

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_CODE_DIR = os.path.dirname(_THIS_DIR)
sys.path.insert(0, _CODE_DIR)
sys.path.insert(0, _THIS_DIR)

# Reuse core functions from exp_profile_fit (located in experiments/)
try:
    from exp_profile_fit import measure_at_config
except ImportError as exc:
    raise ImportError(
        f"x2 requires exp_profile_fit.py in {_THIS_DIR}. Error: {exc}"
    ) from exc


# D1/D7 discriminator configs
CONFIGS = [
    # α=1 row — all low-α
    (1.0, 0.5), (1.0, 2.5), (1.0, 5.0), (1.0, 20.0),
    # α=5 row — includes critical (5, 0.5) D1-vs-D7 discriminator
    (5.0, 0.5), (5.0, 2.5), (5.0, 5.0), (5.0, 20.0),
    # α=20 row — boundary of R21 Regime B observations
    (20.0, 0.5), (20.0, 2.5), (20.0, 5.0), (20.0, 20.0),
    # α=100 row — deep high-α region
    (100.0, 0.5), (100.0, 2.5), (100.0, 5.0), (100.0, 20.0),
]


def _worker(task):
    idx, n_total, alpha, beta, kwargs = task
    # BLAS thread caps already set at module level (top of file), workers inherit via spawn

    xi_th = float(np.sqrt(alpha / beta))
    # P0 FIX: coefficient 393 documented as empirical calibration, not theoretical.
    #   Theoretical: β·|W''(c)|/(α·λ_2(L)). For 48×48 free-BC, c=0.3:
    #     λ_2 = 2(1-cos(π/48)) ≈ 0.00428, |W''(0.3)| = 0.52
    #     → theoretical coeff = 0.52/0.00428 ≈ 121 (sans 4α factor)
    #     OR with 4α normalization: 121/4 ≈ 30
    #   Empirical (R21-calibrated): coeff ≈ 400 placing threshold at β/α=0.25 (R21 Regime B boundary)
    # We keep 393 as empirical calibration to R21; D7 threshold = 100 is empirical.
    # For key discriminator (α=5, β=0.5), both theoretical (121) and empirical (393)
    # give score < 100, so D7 predicts Regime B consistently.
    stiffness_score = 393.0 * beta / alpha  # empirical, R21-calibrated
    d1_pred = "B" if alpha >= 20 else "A"  # D1: α-absolute threshold (empirical from R21)
    d7_pred = "B" if stiffness_score <= 100 else "A"
    discrim = "**" if d1_pred != d7_pred else "  "

    print(f"  [{idx+1}/{n_total}]{discrim} START α={alpha} β={beta} ξ_th={xi_th:.2f} "
          f"D1={d1_pred} D7={d7_pred} (393β/α={stiffness_score:.1f})", flush=True)

    t_i = time.time()
    res = measure_at_config(alpha, beta, **kwargs)
    elapsed = time.time() - t_i
    res['elapsed_sec'] = elapsed
    res['d1_prediction'] = d1_pred
    res['d7_prediction'] = d7_pred
    res['stiffness_score_393'] = stiffness_score

    if res.get('found'):
        p = res['fits']['generalized'].get('p', None)
        observed = "B" if (p is not None and p < 2.0) else "A"
        d1_match = "✓" if observed == d1_pred else "✗"
        d7_match = "✓" if observed == d7_pred else "✗"
        print(f"  [{idx+1}/{n_total}]{discrim} DONE α={alpha} β={beta}: "
              f"K_soft={res['k_soft']:.3f}, p={p:.3f}, observed={observed} "
              f"D1={d1_match} D7={d7_match} ({elapsed:.1f}s)", flush=True)
        res['regime_observed'] = observed
    else:
        print(f"  [{idx+1}/{n_total}]{discrim} SKIP α={alpha} β={beta}: "
              f"{res.get('reason')} ({elapsed:.1f}s)", flush=True)
        res['regime_observed'] = None

    return idx, res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid-size', type=int, default=48)
    ap.add_argument('--n-inits', type=int, default=24)
    ap.add_argument('--c', type=float, default=0.3)
    ap.add_argument('--k-soft-max', type=float, default=0.55)
    ap.add_argument('--workers', type=int, default=1)
    ap.add_argument('--out', default='results/exp_x2_shape_regime.json')
    args = ap.parse_args()

    print(f"[x2] D1 vs D7 shape regime discrimination")
    print(f"[x2] grid={args.grid_size} n_inits={args.n_inits} c={args.c} workers={args.workers}")
    print(f"[x2] {len(CONFIGS)} (α, β) configs, critical discriminators marked **")
    print()

    t0 = time.time()
    kwargs = dict(
        grid_size=args.grid_size,
        c=args.c,
        n_inits=args.n_inits,
        k_soft_max=args.k_soft_max,
    )
    tasks = [(i, len(CONFIGS), a, b, kwargs) for i, (a, b) in enumerate(CONFIGS)]

    results = [None] * len(CONFIGS)
    if args.workers <= 1:
        for task in tasks:
            idx, res = _worker(task)
            results[idx] = res
    else:
        import multiprocessing as mp
        ctx = mp.get_context('spawn')
        with ctx.Pool(processes=args.workers) as pool:
            for idx, res in pool.imap_unordered(_worker, tasks):
                results[idx] = res

    elapsed = time.time() - t0

    # Tally
    d1_correct = sum(1 for r in results if r and r.get('regime_observed') == r.get('d1_prediction'))
    d7_correct = sum(1 for r in results if r and r.get('regime_observed') == r.get('d7_prediction'))
    n_found = sum(1 for r in results if r and r.get('found'))

    output = {
        'session': '2026-04-22_X2_shape_regime',
        'purpose': 'D1 (α-threshold) vs D7 (393·β/α stiffness) discrimination',
        'config': {
            'grid_size': args.grid_size, 'c': args.c, 'n_inits': args.n_inits,
            'k_soft_max': args.k_soft_max, 'configs': CONFIGS,
        },
        'results': results,
        'tally': {
            'n_configs': len(CONFIGS),
            'n_found': n_found,
            'd1_correct': d1_correct,
            'd7_correct': d7_correct,
        },
        'total_elapsed_sec': elapsed,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n[x2] done in {elapsed:.1f}s. Wrote {out_path}")
    print(f"[x2] {n_found}/{len(CONFIGS)} PASS")
    print(f"[x2] D1 correct: {d1_correct}/{n_found}")
    print(f"[x2] D7 correct: {d7_correct}/{n_found}")

    # Detail table
    print("\n--- Shape regime results ---")
    print(f"{'α':>5} {'β':>5} {'ξ_th':>5} {'393β/α':>8} {'D1':>3} {'D7':>3} {'obs':>4} {'p':>6}")
    print("-" * 60)
    for r in results:
        if r is None:
            continue
        alpha, beta = r['alpha'], r['beta']
        xi_th = r['xi_theory']
        score = r.get('stiffness_score_393', 0)
        d1p = r.get('d1_prediction', '?')
        d7p = r.get('d7_prediction', '?')
        obs = r.get('regime_observed', '?')
        p_val = r['fits']['generalized'].get('p') if r.get('found') else None
        p_str = f"{p_val:.3f}" if p_val is not None else "  N/A"
        print(f"{alpha:>5.1f} {beta:>5.2f} {xi_th:>5.2f} {score:>8.1f} "
              f"{d1p:>3} {d7p:>3} {str(obs):>4} {p_str:>6}")


if __name__ == '__main__':
    main()
