#!/usr/bin/env python3
"""
exp_x1_v5_hysteresis.py — Forward/backward sweep to test well-switching vs protocol-selection.

## Hypothesis under test
V1 showed E(β) has two clusters: HIGH (E≈403, β≤7.05) and LOW (E≈30, β≥7.10).
V2 showed max_iter increase doesn't change this.

Question: is this
  (A) TRUE fold bifurcation (LOW basin doesn't exist at β≤7.05)
  (B) PROTOCOL SELECTION (LOW basin exists everywhere, Fiedler init just can't find it)

Test: warm-start continuation from LOW branch back to low β.
- If LOW persists all the way to β=7.00 → case (B), sigmoid-like landscape
- If LOW jumps back to HIGH somewhere → case (A), real fold

## Method
Step 1: Forward sweep (Fiedler init) — confirm V1 pattern.
Step 2: Backward sweep starting from β_max LOW branch:
  β_{i+1} gradient-flow result → init for β_i (i decreasing)
Step 3: Compare forward vs backward at each β.
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
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, _optimize_single_from, project_volume


def build_cycle_1d(n: int) -> GraphState:
    row = np.concatenate([np.arange(n), np.arange(n)])
    col = np.concatenate([(np.arange(n) + 1) % n, (np.arange(n) - 1) % n])
    data = np.ones(2 * n)
    adj = sp.csr_matrix((data, (row, col)), shape=(n, n))
    return GraphState(adj)


def count_formations_cycle(u: np.ndarray, threshold: float = 0.5) -> int:
    above = u > threshold
    if not np.any(above):
        return 0
    if np.all(above):
        return 1
    diff = np.diff(np.concatenate([above[-1:], above.astype(int)]))
    return int(np.sum(diff == 1))


def run_forward(graph, c, alpha, beta, eps_init, max_iter):
    """Fiedler-init gradient flow."""
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=max_iter, n_restarts=1,
        dt_init=0.01, eps_init=eps_init,
    )
    result = find_formation(graph, params, verbose=False, normalize=False)
    return result.u, float(result.energy), bool(getattr(result, 'converged', False))


def run_warm_start(graph, c, alpha, beta, u_init, max_iter):
    """Gradient flow from given initial condition."""
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=max_iter, n_restarts=1,
        dt_init=0.01, eps_init=0.0,
    )
    ec = EnergyComputer(graph, params)
    # Project u_init onto Σ_m for the target c
    m = c * graph.n
    u_init_proj = project_volume(u_init.copy(), m)

    u_final, E_final, terms, _, _, conv, iters = _optimize_single_from(
        graph, params, ec, u_init_proj
    )
    return u_final, float(E_final), bool(conv)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=1024)
    ap.add_argument('--c', type=float, default=0.7)
    ap.add_argument('--alpha', type=float, default=1.0)
    ap.add_argument('--eps-init', type=float, default=0.01)
    ap.add_argument('--max-iter', type=int, default=30000)
    ap.add_argument('--beta-list', type=str,
                    default='7.00,7.05,7.10,7.15,7.20,7.25,7.30,7.40,7.50',
                    help='β values, in ASCENDING order (script handles reverse for backward)')
    ap.add_argument('--out', default='results/exp_x1_v5_hysteresis.json')
    args = ap.parse_args()

    beta_list = sorted([float(b.strip()) for b in args.beta_list.split(',') if b.strip()])
    print(f"[v5] Hysteresis test: forward + backward on C_{args.n}, c={args.c}, α={args.alpha}")
    print(f"[v5] β range: {beta_list[0]} → {beta_list[-1]} ({len(beta_list)} points)")
    print(f"[v5] max_iter: {args.max_iter}")
    print()

    graph = build_cycle_1d(args.n)
    t0 = time.time()

    # -------- FORWARD sweep --------
    print("=" * 60)
    print("FORWARD sweep (Fiedler init at each β)")
    print("=" * 60)
    forward = {}
    for beta in beta_list:
        t_i = time.time()
        u, E, conv = run_forward(graph, args.c, args.alpha, beta, args.eps_init, args.max_iter)
        K = count_formations_cycle(u)
        elapsed = time.time() - t_i
        forward[beta] = {'E': E, 'K': K, 'converged': conv, 'u': u, 'elapsed': elapsed}
        branch = "HIGH" if E > 100 else "LOW"
        print(f"  β={beta:5.2f}: E={E:8.3f}  K={K}  conv={conv}  ({branch}) [{elapsed:.1f}s]")

    # -------- BACKWARD sweep (warm-start from highest β LOW branch) --------
    print()
    print("=" * 60)
    print("BACKWARD sweep (warm-start from previous β's result)")
    print("=" * 60)
    backward = {}
    # Start from the LAST β (highest) result, which should be LOW
    u_prev = forward[beta_list[-1]]['u']
    for beta in reversed(beta_list):
        t_i = time.time()
        u, E, conv = run_warm_start(graph, args.c, args.alpha, beta, u_prev, args.max_iter)
        K = count_formations_cycle(u)
        elapsed = time.time() - t_i
        backward[beta] = {'E': E, 'K': K, 'converged': conv, 'u': u, 'elapsed': elapsed}
        branch = "HIGH" if E > 100 else "LOW"
        print(f"  β={beta:5.2f}: E={E:8.3f}  K={K}  conv={conv}  ({branch}) [{elapsed:.1f}s]")
        u_prev = u  # use current result as init for next (lower) β

    total = time.time() - t0

    # -------- Compare --------
    print()
    print("=" * 60)
    print("HYSTERESIS COMPARISON")
    print("=" * 60)
    print(f"{'β':>6} | {'E_forward':>10} | {'E_backward':>11} | {'Δ':>8} | Verdict")
    print("-" * 70)
    verdicts = []
    for beta in beta_list:
        E_f = forward[beta]['E']
        E_b = backward[beta]['E']
        delta = E_f - E_b
        if abs(delta) < 1.0:
            verdict = "same branch (no hysteresis)"
        elif E_f > E_b:
            verdict = "**HYSTERESIS** — forward HIGH, backward LOW"
        else:
            verdict = "inverse hysteresis (unexpected)"
        verdicts.append((beta, E_f, E_b, verdict))
        print(f"{beta:>6.2f} | {E_f:>10.3f} | {E_b:>11.3f} | {delta:>8.3f} | {verdict}")

    # -------- Interpretation --------
    print()
    print("=" * 60)
    print("INTERPRETATION")
    print("=" * 60)
    n_hysteresis = sum(1 for b, f, bk, v in verdicts if 'HYSTERESIS' in v)
    if n_hysteresis > 0:
        print(f"**{n_hysteresis}/{len(beta_list)} β values show HYSTERESIS**")
        print("→ LOW basin exists all the way to β_min; Fiedler init merely fails to find it")
        print("→ **CASE (B): PROTOCOL-DEPENDENT SELECTION** — landscape is smooth, not a true fold")
        print("→ Sigmoid universality hypothesis REVIVED (with protocol-dependent caveat)")
    else:
        print("NO hysteresis across β range")
        print("→ Backward sweep also reverts to HIGH branch at β < β_c")
        print("→ **CASE (A): TRUE FOLD BIFURCATION** — LOW basin disappears")
        print("→ Well-switching hypothesis confirmed")

    # -------- Save --------
    out = {
        'session': '2026-04-22_X1_v5_hysteresis',
        'config': vars(args),
        'beta_list': beta_list,
        'forward': {str(b): {k: v for k, v in d.items() if k != 'u'} for b, d in forward.items()},
        'backward': {str(b): {k: v for k, v in d.items() if k != 'u'} for b, d in backward.items()},
        'verdicts': [{'beta': b, 'E_forward': f, 'E_backward': bk, 'verdict': v} for b, f, bk, v in verdicts],
        'n_hysteresis': n_hysteresis,
        'total_elapsed_sec': total,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\n[v5] done in {total:.1f}s. Wrote {out_path}")


if __name__ == '__main__':
    main()
