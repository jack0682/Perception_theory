#!/usr/bin/env python3
"""Experiment 13: Core Depth Hypothesis (H2) Verification.

H2 (Canonical Spec §13, T-Persist-Full): δ_min ≥ 2, where
    δ_min := min_{x ∈ Core} d_G(x, ∂Core)
is the minimum graph distance from any core site to the core boundary.

The transport concentration theorem (T-Persist result 2) applies to "deep core"
sites with δ(x) ≥ 2. If δ_min ≥ 2 for ALL core sites, concentration holds
everywhere in the core. On finite grids, the core boundary layer always has
δ = 1 sites, so we measure TWO things:

(A) Literal H2: does δ_min ≥ 2? (Expected: fails on finite grids — boundary
    core sites always neighbor non-core sites.)
(B) Deep core non-emptiness: does the deep core {x : δ(x) ≥ 2} exist?
    What fraction of core mass does it contain?

(B) is what actually matters for T-Persist: the transport concentration bound
applies to deep core sites, and the Persist predicate integrates over them.

Sweeps:
- Grid sizes: 8×8, 10×10, 15×15, 20×20
- β_bd (phase separation): 5, 10, 20, 50, 100
- Volume fraction c: 0.2, 0.3, 0.4, 0.5
- a_cl (closure strength): 2.0, 3.0, 3.5, 3.9

Spinodal filter: skip c outside (0.211, 0.789).
"""
import sys, os, time, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation

# --- Parameter grid ---
GRID_SIZES = [(8, 8), (10, 10), (15, 15), (20, 20)]
BETAS = [5.0, 10.0, 20.0, 50.0, 100.0]
VOLUME_FRACS = [0.2, 0.3, 0.4, 0.5]
A_CLS = [2.0, 3.0, 3.5, 3.9]

SPINODAL_LO = 0.211
SPINODAL_HI = 0.789
THETA_CORE = 0.9


def compute_core_depth_profile(u, graph, theta_core=THETA_CORE):
    """Compute full depth profile of the core region.

    Depth δ(x) for a core site x = shortest graph distance from x to
    any non-core site (via multi-source BFS from all non-core nodes).

    Returns dict with:
      n_core, delta_min, delta_max, delta_mean,
      n_deep (sites with δ≥2), deep_mass_frac (u-weighted fraction in deep core),
      depth_histogram {depth: count}
    """
    core_mask = u >= theta_core
    n_core = int(np.sum(core_mask))

    if n_core == 0:
        return {'n_core': 0, 'delta_min': float('nan'), 'delta_max': float('nan'),
                'delta_mean': float('nan'), 'n_deep': 0, 'deep_mass_frac': 0.0,
                'depth_histogram': {}}

    from collections import deque

    W = graph.W
    non_core_idx = np.where(~core_mask)[0]

    if len(non_core_idx) == 0:
        return {'n_core': n_core, 'delta_min': n_core, 'delta_max': n_core,
                'delta_mean': float(n_core), 'n_deep': n_core, 'deep_mass_frac': 1.0,
                'depth_histogram': {n_core: n_core}}

    core_indices = np.where(core_mask)[0]
    depths = np.full(graph.n, -1, dtype=int)

    # Multi-source BFS from all non-core nodes
    queue = deque()
    for nc in non_core_idx:
        queue.append(nc)
        depths[nc] = 0

    while queue:
        node = queue.popleft()
        row = W.getrow(node)
        for nb in row.indices:
            if depths[nb] == -1:
                depths[nb] = depths[node] + 1
                queue.append(nb)

    core_depths = depths[core_indices]
    core_u = u[core_indices]

    delta_min = int(np.min(core_depths))
    delta_max = int(np.max(core_depths))
    delta_mean = float(np.mean(core_depths))

    # Deep core: δ ≥ 2
    deep_mask = core_depths >= 2
    n_deep = int(np.sum(deep_mask))
    total_core_mass = float(np.sum(core_u))
    deep_mass = float(np.sum(core_u[deep_mask])) if n_deep > 0 else 0.0
    deep_mass_frac = deep_mass / total_core_mass if total_core_mass > 1e-15 else 0.0

    # Depth histogram
    depth_hist = {}
    for d in range(delta_min, delta_max + 1):
        cnt = int(np.sum(core_depths == d))
        if cnt > 0:
            depth_hist[d] = cnt

    return {
        'n_core': n_core,
        'delta_min': delta_min,
        'delta_max': delta_max,
        'delta_mean': delta_mean,
        'n_deep': n_deep,
        'deep_mass_frac': deep_mass_frac,
        'depth_histogram': depth_hist,
    }


def run_one(grid_size, beta, c, a_cl):
    """Run one parameter combination. Returns result dict or None if skipped."""
    if c < SPINODAL_LO or c > SPINODAL_HI:
        return None

    rows, cols = grid_size
    graph = GraphState.grid_2d(rows, cols)

    params = ParameterRegistry(
        a_cl=a_cl,
        beta_bd=beta,
        volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=2000,
        n_restarts=3,
        dt_init=0.01,
    )

    result = find_formation(graph, params)
    u = result.u
    dp = compute_core_depth_profile(u, graph)
    diag = result.diagnostics

    return {
        'grid': f'{rows}x{cols}',
        'n': rows * cols,
        'beta_bd': beta,
        'c': c,
        'a_cl': a_cl,
        'energy': result.energy,
        'converged': result.converged,
        'Bind': diag.bind,
        'Sep': diag.sep,
        'Inside': diag.inside,
        'n_core': dp['n_core'],
        'delta_min': dp['delta_min'],
        'delta_max': dp['delta_max'],
        'delta_mean': dp['delta_mean'],
        'n_deep': dp['n_deep'],
        'deep_mass_frac': dp['deep_mass_frac'],
        'depth_histogram': dp['depth_histogram'],
        'u_min': float(u.min()),
        'u_max': float(u.max()),
        'u_std': float(u.std()),
    }


def main():
    total_combos = len(GRID_SIZES) * len(BETAS) * len(VOLUME_FRACS) * len(A_CLS)
    print("Experiment 13: Core Depth Hypothesis (H2) Verification")
    print(f"Parameter grid: {len(GRID_SIZES)} grids x {len(BETAS)} beta x "
          f"{len(VOLUME_FRACS)} c x {len(A_CLS)} a_cl = {total_combos} combinations")
    print(f"(Skipping c outside spinodal [{SPINODAL_LO}, {SPINODAL_HI}])")
    print(f"theta_core = {THETA_CORE}")
    print()
    print("Two measures:")
    print("  (A) Literal H2: delta_min >= 2 for ALL core sites")
    print("  (B) Deep core exists: {x : delta(x) >= 2} is non-empty")
    print()

    all_results = []
    n_tested = 0
    n_skipped = 0
    # Counters for literal H2
    n_h2_literal = 0
    # Counters for deep core
    n_deep_exists = 0
    n_deep_empty = 0
    n_no_core = 0
    t0 = time.time()

    for grid_size in GRID_SIZES:
        for beta in BETAS:
            for c in VOLUME_FRACS:
                for a_cl in A_CLS:
                    r = run_one(grid_size, beta, c, a_cl)
                    if r is None:
                        n_skipped += 1
                        continue

                    n_tested += 1
                    all_results.append(r)

                    if r['n_core'] == 0:
                        n_no_core += 1
                        tag = "NO_CORE"
                    elif r['delta_min'] >= 2:
                        n_h2_literal += 1
                        n_deep_exists += 1
                        tag = "H2_LITERAL"
                    elif r['n_deep'] > 0:
                        n_deep_exists += 1
                        tag = f"DEEP={r['n_deep']:3d} ({r['deep_mass_frac']:.0%})"
                    else:
                        n_deep_empty += 1
                        tag = "SHALLOW"

                    elapsed = time.time() - t0
                    dm = f"{r['delta_mean']:.2f}" if not np.isnan(r['delta_mean']) else "nan"
                    print(f"[{n_tested:3d}] {r['grid']:5s} b={beta:5.0f} c={c:.1f} "
                          f"a={a_cl:.1f} | core={r['n_core']:3d} "
                          f"d_min={r['delta_min']} d_max={r['delta_max']} "
                          f"d_mean={dm:>5} deep={r['n_deep']:3d} "
                          f"| {tag} [{elapsed:.1f}s]")

    total_time = time.time() - t0
    n_with_core = n_tested - n_no_core

    # --- Summary ---
    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"Total combinations:    {total_combos}")
    print(f"Skipped (spinodal):    {n_skipped}")
    print(f"Tested:                {n_tested}")
    print(f"  No core (empty):     {n_no_core}")
    print(f"  With core:           {n_with_core}")
    print()
    print(f"(A) Literal H2 (delta_min >= 2 for ALL core sites):")
    print(f"    Pass:              {n_h2_literal}/{n_with_core}")
    if n_with_core > 0:
        print(f"    Rate:              {n_h2_literal/n_with_core*100:.1f}%")
    print()
    print(f"(B) Deep core non-empty (exists site with delta >= 2):")
    print(f"    Pass:              {n_deep_exists}/{n_with_core}")
    if n_with_core > 0:
        print(f"    Rate:              {n_deep_exists/n_with_core*100:.1f}%")
    print(f"    Fail (all shallow):{n_deep_empty}/{n_with_core}")
    print()
    print(f"Total time:            {total_time:.1f}s")

    # Deep core mass fraction statistics
    deep_fracs = [r['deep_mass_frac'] for r in all_results
                  if r['n_core'] > 0 and r['n_deep'] > 0]
    if deep_fracs:
        print(f"\nDeep core mass fraction (over {len(deep_fracs)} cases with deep core):")
        print(f"  min:    {min(deep_fracs):.3f}")
        print(f"  median: {np.median(deep_fracs):.3f}")
        print(f"  mean:   {np.mean(deep_fracs):.3f}")
        print(f"  max:    {max(deep_fracs):.3f}")

    # Shallow-only failures: what parameters cause them?
    shallow_cases = [r for r in all_results if r['n_core'] > 0 and r['n_deep'] == 0]
    if shallow_cases:
        print(f"\n--- SHALLOW-ONLY CASES ({len(shallow_cases)}) ---")
        print("(Core exists but no site has delta >= 2; transport concentration inapplicable)")
        for s in shallow_cases:
            print(f"  {s['grid']} beta={s['beta_bd']} c={s['c']} a_cl={s['a_cl']} "
                  f"n_core={s['n_core']} delta_max={s['delta_max']}")

    # Depth distribution across all formations
    with_core = [r for r in all_results if r['n_core'] > 0]
    if with_core:
        dmax_vals = [r['delta_max'] for r in with_core if not np.isnan(r['delta_max'])]
        print(f"\ndelta_max distribution (N={len(dmax_vals)} with core):")
        for d in sorted(set(dmax_vals)):
            cnt = dmax_vals.count(d)
            print(f"  delta_max = {d}: {cnt} cases ({cnt/len(dmax_vals)*100:.1f}%)")

    # Breakdown by grid size
    print("\n--- Breakdown by grid size ---")
    for gs in GRID_SIZES:
        label = f'{gs[0]}x{gs[1]}'
        subset = [r for r in all_results if r['grid'] == label and r['n_core'] > 0]
        if not subset:
            continue
        n_sub = len(subset)
        n_deep_sub = sum(1 for r in subset if r['n_deep'] > 0)
        fracs = [r['deep_mass_frac'] for r in subset if r['n_deep'] > 0]
        frac_str = f"mean mass frac={np.mean(fracs):.3f}" if fracs else "no deep core"
        print(f"  {label}: {n_deep_sub}/{n_sub} have deep core, {frac_str}")

    # Breakdown by beta
    print("\n--- Breakdown by beta_bd ---")
    for beta in BETAS:
        subset = [r for r in all_results if r['beta_bd'] == beta and r['n_core'] > 0]
        if not subset:
            continue
        n_sub = len(subset)
        n_deep_sub = sum(1 for r in subset if r['n_deep'] > 0)
        fracs = [r['deep_mass_frac'] for r in subset if r['n_deep'] > 0]
        frac_str = f"mean mass frac={np.mean(fracs):.3f}" if fracs else "no deep core"
        print(f"  beta={beta:5.0f}: {n_deep_sub}/{n_sub} have deep core, {frac_str}")

    # --- Write CSV ---
    csv_path = os.path.join(os.path.dirname(__file__), 'exp13_results.csv')
    if all_results:
        csv_rows = []
        for r in all_results:
            row = {k: v for k, v in r.items() if k != 'depth_histogram'}
            row['delta_mean'] = f"{r['delta_mean']:.3f}" if not np.isnan(r['delta_mean']) else ''
            csv_rows.append(row)
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys())
            writer.writeheader()
            writer.writerows(csv_rows)
        print(f"\nResults saved to {csv_path}")

    # --- Conclusion ---
    print("\n" + "=" * 72)
    print("CONCLUSION")
    print("=" * 72)
    if n_h2_literal == n_with_core and n_with_core > 0:
        print(f"H2 (literal delta_min >= 2) holds universally across {n_with_core} cases.")
    elif n_deep_exists == n_with_core and n_with_core > 0:
        print("H2 (literal) FAILS universally: boundary core sites always have delta=1.")
        print(f"However, deep core (delta >= 2) exists in ALL {n_with_core} formations")
        print("with non-empty core. The transport concentration theorem applies to")
        print(f"median {np.median(deep_fracs):.0%} of core mass.")
        print()
        print("RECOMMENDATION: Weaken H2 to 'deep core non-emptiness' (delta_max >= 2).")
        print("This is what the transport concentration proof actually requires")
        print("(it conditions on delta(x) >= 2 per-site, not delta_min >= 2 globally).")
    else:
        print(f"Mixed results: {n_deep_exists}/{n_with_core} have deep core, "
              f"{n_deep_empty} are all-shallow.")


if __name__ == '__main__':
    main()
