#!/usr/bin/env python3
"""Experiment 10: Fingerprint Gap Verification
Verifies the two-tier transport concentration theory.

Theory predicts:
- Deep core (delta >= 2): fingerprint gap Δ_φ² ≈ 2.87
- Shallow core (delta = 1): fingerprint gap ≈ 0.05
- Operator triad amplifies raw u-gap (0.72) by ~4×
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.transport import cohesion_fingerprint, graph_distance_matrix

GRID = (20, 20)
BETA = 50.0  # high β_bd ensures sharp core boundary, needed for clear depth stratification
C = 0.3
THETA_CORE = 0.8


def classify_by_depth(u, graph, theta_core=THETA_CORE):
    """Classify sites by topological depth δ (distance from boundary of core).

    Returns dict: depth -> list of node indices.
    Also returns exterior sites (depth=0 means non-core, negative = deep exterior).
    """
    core_mask = u >= theta_core
    n = graph.n

    if not np.any(core_mask):
        return {}, core_mask

    # Compute graph distances from each node to every other node
    dist = graph_distance_matrix(graph)

    # For core sites: depth = min distance to any non-core neighbor
    # For non-core sites: depth = -(min distance to any core site)
    core_indices = np.where(core_mask)[0]
    noncore_indices = np.where(~core_mask)[0]

    depths = {}

    if len(noncore_indices) == 0:
        # All nodes are core — depth = distance to boundary of grid
        for i in core_indices:
            depths[i] = int(np.min(dist[i, :][dist[i, :] > 0]))  # min nonzero
        return _group_by_depth(depths, core_mask), core_mask

    if len(core_indices) == 0:
        return {}, core_mask

    # Core depths: min distance to any non-core site
    for i in core_indices:
        d_to_noncore = dist[i, noncore_indices]
        depths[i] = int(np.min(d_to_noncore))

    # Non-core: assign negative depth (distance to nearest core site)
    for i in noncore_indices:
        d_to_core = dist[i, core_indices]
        depths[i] = -int(np.min(d_to_core))

    return _group_by_depth(depths, core_mask), core_mask


def _group_by_depth(depths, core_mask):
    """Group node indices by depth value."""
    groups = {}
    for idx, d in depths.items():
        if d not in groups:
            groups[d] = []
        groups[d].append(idx)
    return groups


def main():
    print("Experiment 10: Fingerprint Gap Verification")
    print(f"Grid: {GRID}, β={BETA}, c={C}, θ_core={THETA_CORE}")
    print()

    t0 = time.time()

    graph = GraphState.grid_2d(*GRID)
    params = ParameterRegistry(
        beta_bd=BETA, volume_fraction=C, n_restarts=5, max_iter=5000,
    )
    result = find_formation(graph, params)
    u = result.u

    print(f"Formation found: E={result.energy:.6f}")
    print(f"Diagnostics: {result.diagnostics}")
    print(f"Core sites (u >= {THETA_CORE}): {np.sum(u >= THETA_CORE)}")
    print(f"u range: [{u.min():.4f}, {u.max():.4f}]")
    print()

    # Compute fingerprints
    phi = cohesion_fingerprint(u, graph, params)

    # Classify by depth
    depth_groups, core_mask = classify_by_depth(u, graph)

    # Compute mean exterior fingerprint (non-core sites far from core)
    exterior_indices = []
    for d, indices in depth_groups.items():
        if d <= -2:  # deep exterior
            exterior_indices.extend(indices)
    if not exterior_indices:
        # fallback: all non-core
        exterior_indices = list(np.where(~core_mask)[0])

    if len(exterior_indices) == 0:
        print("WARNING: No exterior sites found. Cannot compute fingerprint gaps.")
        return

    phi_ext_mean = phi[exterior_indices].mean(axis=0)
    u_ext_mean = u[exterior_indices].mean()

    print(f"Exterior reference ({len(exterior_indices)} sites):")
    print(f"  mean u = {u_ext_mean:.4f}")
    print(f"  mean φ = [{', '.join(f'{v:.4f}' for v in phi_ext_mean)}]")
    print()

    # Theory predictions (from PERSIST-SYNTHESIS.md §1.2)
    theory_table = {
        'u':  {'deep_core': 0.90, 'deep_ext': 0.05, 'gap_sq': 0.72},
        'Cl': {'deep_core': 0.80, 'deep_ext': 0.17, 'gap_sq': 0.40},
        'D':  {'deep_core': 0.98, 'deep_ext': 0.01, 'gap_sq': 0.94},
        'C':  {'deep_core': 1.00, 'deep_ext': 0.10, 'gap_sq': 0.81},
    }
    theory_total_gap = 2.87
    theory_shallow_gap = 0.05

    # Print component-level analysis for deep core
    deep_core_indices = []
    for d, indices in depth_groups.items():
        if d >= 2:
            deep_core_indices.extend(indices)

    shallow_core_indices = []
    for d, indices in depth_groups.items():
        if d == 1:
            shallow_core_indices.extend(indices)

    print("="*80)
    print("Component-Level Fingerprint Analysis (Deep Core δ≥2)")
    print("="*80)
    comp_names = ['u', 'Cl', 'D', 'C']
    if deep_core_indices:
        phi_deep = phi[deep_core_indices]
        u_deep = u[deep_core_indices]
        print(f"  Deep core sites: {len(deep_core_indices)}")
        print(f"  {'Component':<10s} {'Core mean':>10s} {'Ext mean':>10s} {'Gap²':>10s} {'Theory Gap²':>12s}")
        print(f"  {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*12}")
        total_gap_sq = 0.0
        for j, name in enumerate(comp_names):
            core_mean = phi_deep[:, j].mean()
            ext_mean = phi_ext_mean[j]
            gap_sq = (core_mean - ext_mean) ** 2
            total_gap_sq += gap_sq
            theory_gs = theory_table[name]['gap_sq']
            print(f"  {name:<10s} {core_mean:>10.4f} {ext_mean:>10.4f} {gap_sq:>10.4f} {theory_gs:>12.2f}")
        print(f"  {'TOTAL':<10s} {'':>10s} {'':>10s} {total_gap_sq:>10.4f} {theory_total_gap:>12.2f}")
        print(f"  Amplification factor: {total_gap_sq / max((phi_deep[:,0].mean() - phi_ext_mean[0])**2, 1e-10):.2f}x")
    else:
        print("  No deep core sites found (δ≥2)")

    # Depth-level summary table
    print()
    print("="*80)
    print("Depth-Level Summary")
    print("="*80)
    print(f"  {'Depth':>6s} {'n_sites':>8s} {'mean_u':>8s} {'Δ_φ²':>10s} {'Theory Δ_φ²':>12s} {'Category':<15s}")
    print(f"  {'-'*6} {'-'*8} {'-'*8} {'-'*10} {'-'*12} {'-'*15}")

    for d in sorted(depth_groups.keys()):
        indices = depth_groups[d]
        n_sites = len(indices)
        mean_u = u[indices].mean()
        phi_d = phi[indices].mean(axis=0)
        gap_sq = float(np.sum((phi_d - phi_ext_mean)**2))

        if d >= 2:
            theory = f"{theory_total_gap:.2f}"
            cat = "deep core"
        elif d == 1:
            theory = f"{theory_shallow_gap:.2f}"
            cat = "shallow core"
        elif d == 0:
            theory = "—"
            cat = "boundary"
        else:
            theory = "—"
            cat = "exterior"

        print(f"  {d:>6d} {n_sites:>8d} {mean_u:>8.4f} {gap_sq:>10.4f} {theory:>12s} {cat:<15s}")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
