#!/usr/bin/env python3
"""Experiment 28: T-Persist stress test across wide parameter sweep.

Comprehensive sweep of (grid_size, β, ε) to find the validity boundary
of the T-Persist-1 chain. Tests parts (a)(b)(c)(d) with warm-start;
skips transport (part e) since exp27 showed it always passes.

Edge cases: small formations, very large β, near-bifurcation scan.

Reference: Canonical Spec v2.0 §13 (T-Persist-1), exp27 chain verification.
"""

import sys
import os
import time
import numpy as np
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.energy import EnergyComputer


# ============================================================================
# Configuration
# ============================================================================

GRID_SIZES = [6, 8, 10, 12, 15]
BETA_VALUES = [10, 20, 50, 100, 200]
EPS_VALUES = [0.01, 0.05, 0.1, 0.2]

THETA_CORE = 0.9
THETA_DEEP = 0.95
CORE_RELAX = 0.05     # relaxation for part (d)


def find_core(u, theta):
    return np.where(u >= theta)[0]


def build_adj_list(graph):
    W_coo = graph.W.tocoo()
    adj = [[] for _ in range(graph.n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)
    return adj


def bfs_depth(adj_list, core_set):
    """BFS from boundary of core inward; return depth array."""
    n = len(adj_list)
    depth = np.full(n, -1, dtype=int)
    boundary = []
    for x in core_set:
        for nb in adj_list[x]:
            if nb not in core_set:
                boundary.append(x)
                break
    queue = list(boundary)
    for x in queue:
        depth[x] = 0
    head = 0
    while head < len(queue):
        x = queue[head]; head += 1
        for nb in adj_list[x]:
            if nb in core_set and depth[nb] == -1:
                depth[nb] = depth[x] + 1
                queue.append(nb)
    return depth


def check_chain(g, p_t, u_t, eps_frac, adj):
    """Run parts (a)(b)(c)(d) of T-Persist chain.

    Returns dict with pass/fail for each part and key metrics.
    """
    n = g.n
    res = {}

    # --- Part (c): Deep core analysis ---
    core_idx = find_core(u_t, THETA_CORE)
    core_set = set(core_idx.tolist())
    depth = bfs_depth(adj, core_set)
    core2_idx = np.array([x for x in core_idx if depth[x] >= 2])
    interior_gap = float(np.min(u_t[core2_idx] - THETA_CORE)) if len(core2_idx) > 0 else 0.0
    res['core_size'] = len(core_idx)
    res['core2_size'] = len(core2_idx)
    res['interior_gap'] = interior_gap
    res['part_c'] = len(core2_idx) > 0 and interior_gap > 0.01

    # --- Part (a): IFT continuity under warm-start ---
    alpha_s = p_t.alpha_bd * (1.0 + eps_frac)
    p_s = ParameterRegistry(beta_bd=p_t.beta_bd, alpha_bd=alpha_s)
    res_s = find_formation(g, p_s, u_init=u_t)
    u_s = res_s.u

    field_diff = float(np.linalg.norm(u_s - u_t))

    # Estimate μ via curvature
    ec = EnergyComputer(g, p_t)
    ec.normalize_weights()
    E_t, _ = ec.energy(u_t)
    delta_u_norm = np.linalg.norm(u_s - u_t)
    if delta_u_norm > 1e-12:
        E_at_us, _ = ec.energy(u_s)
        mu_est = max(2.0 * (E_at_us - E_t) / (delta_u_norm**2), 0.01)
    else:
        mu_est = 1.0

    eps1 = abs(alpha_s - p_t.alpha_bd)
    ift_bound = 2.0 * eps1 / mu_est
    res['field_diff'] = field_diff
    res['mu_est'] = mu_est
    res['ift_bound'] = ift_bound
    res['part_a'] = field_diff < ift_bound * 5

    # --- Part (d): Threshold preservation ---
    core_t_in_relaxed = sum(1 for x in core_idx if u_s[x] >= THETA_CORE - CORE_RELAX)
    frac_relaxed = core_t_in_relaxed / max(len(core_idx), 1)
    core_t_exact = sum(1 for x in core_idx if u_s[x] >= THETA_CORE)
    frac_exact = core_t_exact / max(len(core_idx), 1)
    res['frac_preserved'] = frac_exact
    res['frac_relaxed'] = frac_relaxed
    res['part_d'] = frac_relaxed >= 0.9

    # --- Part (b): Gradient flow convergence (warm-start from u_t, check matches u_s) ---
    # Simplified: since we already warm-started to get u_s, check that
    # re-optimizing from u_s gives the same result (basin stability)
    m_target = p_s.volume_fraction * n
    u_perturbed = project_volume(np.clip(u_t + 0.01 * np.random.randn(n), 0, 1), m_target)
    res_flow = find_formation(g, p_s, u_init=u_perturbed)
    u_flow = res_flow.u
    dist_flow = float(np.linalg.norm(u_flow - u_s))
    dist_flow_rel = dist_flow / max(np.linalg.norm(u_s), 1e-12)
    res['dist_flow_rel'] = dist_flow_rel
    res['flow_converged'] = res_flow.converged
    res['part_b'] = dist_flow_rel < 0.1 and res_flow.converged

    # --- Persist overlap ---
    overlap = float(np.sum(np.minimum(u_t, u_s)) / max(np.sum(u_t), np.sum(u_s)))
    res['persist_overlap'] = overlap

    # Chain score
    parts = [res['part_a'], res['part_b'], res['part_c'], res['part_d']]
    res['chain_score'] = sum(parts)
    res['all_pass'] = all(parts)

    return res


def run_sweep():
    """Run the main parameter sweep."""
    print("=" * 80)
    print("  Experiment 28: T-Persist Stress Test — Wide Parameter Sweep")
    print("=" * 80)
    print(f"  Grid sizes: {GRID_SIZES}")
    print(f"  β values:   {BETA_VALUES}")
    print(f"  ε values:   {EPS_VALUES}")
    print(f"  Total combos: {len(GRID_SIZES) * len(BETA_VALUES) * len(EPS_VALUES)}")
    print()

    np.random.seed(42)
    results = []

    # Cache formations per (grid, beta) to avoid redundant optimization
    formation_cache = {}

    t_start = time.time()

    for N in GRID_SIZES:
        g = GraphState.grid_2d(N, N)
        adj = build_adj_list(g)
        n = N * N

        for beta in BETA_VALUES:
            # Find base formation (shared across ε values)
            cache_key = (N, beta)
            p_t = ParameterRegistry(beta_bd=beta)

            t0 = time.time()
            res_t = find_formation(g, p_t)
            dt = time.time() - t0
            u_t = res_t.u

            if not res_t.converged:
                print(f"  WARNING: {N}×{N} β={beta} base formation did not converge")

            formation_cache[cache_key] = (u_t, res_t)

            for eps in EPS_VALUES:
                try:
                    r = check_chain(g, p_t, u_t, eps, adj)
                    r['N'] = N
                    r['beta'] = beta
                    r['eps'] = eps
                    r['base_converged'] = res_t.converged
                    results.append(r)

                    status = "PASS" if r['all_pass'] else f"FAIL({r['chain_score']}/4)"
                    print(f"  {N:>2}×{N:<2} β={beta:>3} ε={eps:.2f} → {status}  "
                          f"|Core|={r['core_size']:>3} |Core²|={r['core2_size']:>2} "
                          f"gap={r['interior_gap']:.4f} ‖Δu‖={r['field_diff']:.4f} "
                          f"pres={r['frac_relaxed']:.3f} overlap={r['persist_overlap']:.3f}")
                except Exception as e:
                    print(f"  {N:>2}×{N:<2} β={beta:>3} ε={eps:.2f} → ERROR: {e}")
                    results.append({
                        'N': N, 'beta': beta, 'eps': eps,
                        'all_pass': False, 'chain_score': 0,
                        'part_a': False, 'part_b': False,
                        'part_c': False, 'part_d': False,
                        'core_size': 0, 'core2_size': 0,
                        'interior_gap': 0, 'field_diff': 0,
                        'frac_relaxed': 0, 'persist_overlap': 0,
                        'mu_est': 0, 'ift_bound': 0,
                        'frac_preserved': 0, 'dist_flow_rel': 0,
                        'flow_converged': False, 'base_converged': False,
                    })

    elapsed = time.time() - t_start
    print(f"\n  Sweep complete in {elapsed:.1f}s")

    return results, formation_cache


def print_summary_tables(results):
    """Print summary tables and validity boundary."""

    # === Table 1: Max ε where all 4 parts pass, per (grid, β) ===
    print(f"\n{'='*70}")
    print("  Table 1: Max ε where all 4 parts pass (a)(b)(c)(d)")
    print(f"{'='*70}")
    print(f"  {'Grid':<8}", end="")
    for beta in BETA_VALUES:
        print(f"  β={beta:<4}", end="")
    print()
    print(f"  {'----':<8}", end="")
    for _ in BETA_VALUES:
        print(f"  {'------':<6}", end="")
    print()

    for N in GRID_SIZES:
        print(f"  {N}×{N:<5}", end="")
        for beta in BETA_VALUES:
            matching = [r for r in results if r['N'] == N and r['beta'] == beta and r['all_pass']]
            if matching:
                max_eps = max(r['eps'] for r in matching)
                print(f"  {max_eps:<6.2f}", end="")
            else:
                print(f"  {'---':<6}", end="")
        print()

    # === Table 2: Chain score heatmap ===
    print(f"\n{'='*70}")
    print("  Table 2: Chain score (0-4) at ε=0.2 (hardest perturbation)")
    print(f"{'='*70}")
    print(f"  {'Grid':<8}", end="")
    for beta in BETA_VALUES:
        print(f"  β={beta:<4}", end="")
    print()
    print(f"  {'----':<8}", end="")
    for _ in BETA_VALUES:
        print(f"  {'------':<6}", end="")
    print()

    for N in GRID_SIZES:
        print(f"  {N}×{N:<5}", end="")
        for beta in BETA_VALUES:
            matching = [r for r in results if r['N'] == N and r['beta'] == beta and r['eps'] == 0.2]
            if matching:
                score = matching[0]['chain_score']
                print(f"  {score}/4   ", end="")
            else:
                print(f"  {'?':<6}", end="")
        print()

    # === Table 3: Part-by-part failure analysis ===
    print(f"\n{'='*70}")
    print("  Table 3: Part-by-part failure rates")
    print(f"{'='*70}")
    total = len(results)
    for part_key, label in [('part_a', '(a) IFT'), ('part_b', '(b) Flow'),
                             ('part_c', '(c) Core'), ('part_d', '(d) Thresh')]:
        n_pass = sum(1 for r in results if r.get(part_key, False))
        n_fail = total - n_pass
        print(f"  {label:<15} PASS: {n_pass:>3}/{total}  FAIL: {n_fail:>3}  "
              f"({100*n_pass/total:.1f}%)")

    all_pass_count = sum(1 for r in results if r['all_pass'])
    print(f"  {'Full chain':<15} PASS: {all_pass_count:>3}/{total}  "
          f"({100*all_pass_count/total:.1f}%)")

    # === Table 4: Failure modes by ε ===
    print(f"\n{'='*70}")
    print("  Table 4: Pass rate by perturbation strength")
    print(f"{'='*70}")
    for eps in EPS_VALUES:
        matching = [r for r in results if r['eps'] == eps]
        n_pass = sum(1 for r in matching if r['all_pass'])
        print(f"  ε={eps:.2f}:  {n_pass}/{len(matching)} pass "
              f"({100*n_pass/len(matching):.0f}%)")


def run_edge_cases():
    """Run edge case tests."""
    print(f"\n\n{'='*80}")
    print("  Edge Cases")
    print(f"{'='*80}")

    np.random.seed(42)

    # --- Edge case 1: Small formation (6×6, c=0.3) ---
    print("\n  [Edge 1] Small formation: 6×6 grid")
    g = GraphState.grid_2d(6, 6)
    adj = build_adj_list(g)
    for beta in [20, 50, 100, 200]:
        p = ParameterRegistry(beta_bd=beta)
        res = find_formation(g, p)
        u = res.u
        core = find_core(u, THETA_CORE)
        core_set = set(core.tolist())
        depth = bfs_depth(adj, core_set)
        core2 = [x for x in core if depth[x] >= 2]
        max_d = int(depth[core].max()) if len(core) > 0 else 0
        print(f"    β={beta:>3}: |Core|={len(core):>2}, |Core²|={len(core2):>2}, "
              f"max_depth={max_d}, u_range=[{u.min():.3f}, {u.max():.3f}]")

    # --- Edge case 2: Very large β ---
    print("\n  [Edge 2] Very large β (deep phase separation)")
    for N in [8, 10, 12]:
        g = GraphState.grid_2d(N, N)
        adj = build_adj_list(g)
        for beta in [300, 500]:
            p = ParameterRegistry(beta_bd=beta)
            try:
                res = find_formation(g, p)
                u = res.u
                core = find_core(u, THETA_CORE)
                core_set = set(core.tolist())
                depth = bfs_depth(adj, core_set)
                core2 = [x for x in core if depth[x] >= 2]
                igap = float(np.min(u[core2] - THETA_CORE)) if len(core2) > 0 else 0.0
                print(f"    {N}×{N} β={beta}: |Core|={len(core):>3}, |Core²|={len(core2):>2}, "
                      f"gap={igap:.4f}, u_max={u.max():.4f}, converged={res.converged}")
            except Exception as e:
                print(f"    {N}×{N} β={beta}: ERROR: {e}")

    # --- Edge case 3: Near-bifurcation scan ---
    print("\n  [Edge 3] Near-bifurcation: find β where μ estimate drops")
    for N in [8, 10, 12]:
        g = GraphState.grid_2d(N, N)
        n = N * N
        print(f"\n    {N}×{N} grid (n={n}):")
        beta_scan = [5, 8, 10, 15, 20, 30, 50]
        for beta in beta_scan:
            p = ParameterRegistry(beta_bd=beta)
            res = find_formation(g, p)
            u = res.u
            u_max = u.max()
            u_min = u.min()
            separation = u_max - u_min

            # Quick μ estimate: perturb and measure curvature
            ec = EnergyComputer(g, p)
            ec.normalize_weights()
            E0, _ = ec.energy(u)
            # Random perturbation in tangent space
            dv = np.random.randn(n) * 0.01
            dv -= dv.mean()  # stay on volume constraint
            u_pert = np.clip(u + dv, 0, 1)
            u_pert = project_volume(u_pert, p.volume_fraction * n)
            E1, _ = ec.energy(u_pert)
            du_norm = np.linalg.norm(u_pert - u)
            mu_approx = max(2 * (E1 - E0) / (du_norm**2), 0.0) if du_norm > 1e-12 else 0.0

            phase = "separated" if separation > 0.5 else "mixed"
            print(f"      β={beta:>3}: u∈[{u_min:.3f},{u_max:.3f}] sep={separation:.3f} "
                  f"μ≈{mu_approx:.3f} [{phase}]")


def main():
    # Main sweep
    results, cache = run_sweep()

    # Summary tables
    print_summary_tables(results)

    # Edge cases
    run_edge_cases()

    # Final verdict
    all_pass = sum(1 for r in results if r['all_pass'])
    total = len(results)
    print(f"\n\n{'='*80}")
    print(f"  FINAL VERDICT")
    print(f"{'='*80}")
    print(f"  {all_pass}/{total} parameter combos have complete T-Persist chain (a)(b)(c)(d)")

    # Identify weakest link
    for part, label in [('part_a', 'IFT'), ('part_b', 'Flow'),
                         ('part_c', 'Core'), ('part_d', 'Thresh')]:
        fails = [(r['N'], r['beta'], r['eps']) for r in results if not r.get(part, False)]
        if fails:
            print(f"  {label} failures ({len(fails)}): "
                  f"e.g. {fails[0][0]}×{fails[0][0]} β={fails[0][1]} ε={fails[0][2]}")

    # Validity boundary summary
    print(f"\n  Validity boundary (max ε per grid):")
    for N in GRID_SIZES:
        passing = [r for r in results if r['N'] == N and r['all_pass']]
        if passing:
            max_eps = max(r['eps'] for r in passing)
            # What β range works at max eps?
            betas_at_max = sorted(set(r['beta'] for r in passing if r['eps'] == max_eps))
            print(f"    {N}×{N}: max ε = {max_eps:.2f} "
                  f"(works at β ∈ {betas_at_max})")
        else:
            print(f"    {N}×{N}: NO combos pass all 4 parts")

    print(f"{'='*80}")


if __name__ == "__main__":
    main()
