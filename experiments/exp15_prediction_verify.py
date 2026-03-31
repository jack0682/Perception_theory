#!/usr/bin/env python3
"""Experiment 15: Multi-formation prediction verification (P1-K through P4-K).

Predictions:
  P1-K: Deep core Persist is independent of K (decoupling at depth >= 2)
  P2-K: Simplex violation in weakly-interacting regime is O(|dCore|), not O(|Core|)
  P3-K: Reoptimize improves Persist at boundary but not deep core
  P4-K: Repulsion increases effective spectral gap (mu_joint > min mu_k)

Plus: E2 reproducibility check with 3 seeds.
"""
import sys, os, time
import numpy as np
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer, energy_bd, grad_bd, energy_cl, grad_cl, energy_sep, grad_sep
from scc.multi import (
    find_k_formations, transport_k_formations,
    inter_formation_distances, formation_overlap, classify_regime,
)
from scc.transport import persist_transport, transport_fixed_point

THETA_CORE = 0.8  # match persist_transport default


# ============================================================
# Utility: core depth computation (adapted from exp13)
# ============================================================

def compute_core_depths(u, graph, theta_core=THETA_CORE):
    """Return array of depths for all nodes. Non-core nodes get depth 0."""
    core_mask = u >= theta_core
    n_core = int(np.sum(core_mask))
    depths = np.zeros(graph.n, dtype=int)
    if n_core == 0 or n_core == graph.n:
        return depths

    non_core_idx = np.where(~core_mask)[0]
    dist = np.full(graph.n, -1, dtype=int)
    queue = deque()
    for nc in non_core_idx:
        queue.append(nc)
        dist[nc] = 0
    while queue:
        node = queue.popleft()
        row = graph.W.getrow(node)
        for nb in row.indices:
            if dist[nb] == -1:
                dist[nb] = dist[node] + 1
                queue.append(nb)
    # Only set depths for core sites
    for i in np.where(core_mask)[0]:
        depths[i] = dist[i]
    return depths


def persist_restricted(u_t, u_s, M, sites_mask, theta_core=THETA_CORE):
    """Compute Persist restricted to a subset of sites.

    Only counts core-to-core transport for source sites in sites_mask.
    """
    core_t = (u_t >= theta_core) & sites_mask
    core_s = u_s >= theta_core
    if not np.any(core_t) or not np.any(core_s):
        return 0.0
    M_sub = M[np.ix_(core_t, core_s)]
    inherited = np.sum(M_sub * u_s[core_s][np.newaxis, :])
    rho = np.sum(u_t[core_t])
    return float(np.clip(inherited / max(rho, 1e-15), 0.0, 1.0))


def core_boundary_size(u, graph, theta_core=THETA_CORE):
    """Count boundary core sites (depth == 1) and total core sites."""
    depths = compute_core_depths(u, graph, theta_core)
    core_mask = u >= theta_core
    n_core = int(np.sum(core_mask))
    n_boundary = int(np.sum(depths[core_mask] == 1)) if n_core > 0 else 0
    n_deep = int(np.sum(depths[core_mask] >= 2)) if n_core > 0 else 0
    return n_core, n_boundary, n_deep


# ============================================================
# P1-K: Deep core Persist independent of K
# ============================================================

def test_p1k():
    print("=" * 60)
    print("P1-K: Deep core Persist independence from K")
    print("=" * 60)

    grid = GraphState.grid_2d(15, 15)
    params = ParameterRegistry(volume_fraction=0.3, beta_bd=50.0, a_cl=3.5)

    # K=1: single formation
    print("\n  Finding K=1 formation on 15x15...")
    r1 = find_formation(grid, params)
    tr1 = transport_fixed_point(r1.u, grid, params, sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10)
    p1_full = persist_transport(tr1.u_t, tr1.u_s, tr1.M)

    depths1 = compute_core_depths(r1.u, grid)
    deep_mask1 = depths1 >= 2
    boundary_mask1 = (r1.u >= THETA_CORE) & (depths1 == 1)
    p1_deep = persist_restricted(tr1.u_t, tr1.u_s, tr1.M, deep_mask1)
    n_core1, n_bnd1, n_deep1 = core_boundary_size(r1.u, grid)

    print(f"  K=1: Persist_full={p1_full:.4f}, Persist_deep={p1_deep:.4f}")
    print(f"       Core={n_core1}, Boundary={n_bnd1}, Deep={n_deep1}")

    # K=2: two formations
    print("\n  Finding K=2 formations on 15x15...")
    sources2 = find_k_formations(grid, params, K=2, lambda_rep=50.0, max_iter=1500, n_restarts=3)
    d_min = inter_formation_distances([s.u for s in sources2], grid)
    regime = classify_regime([s.u for s in sources2], grid)
    print(f"  K=2: d_min={d_min[0,1]:.0f}, regime={regime}")

    results2 = transport_k_formations(
        sources2, grid, params, lambda_rep=50.0,
        sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10,
    )

    for k in range(2):
        p_full = persist_transport(results2[k].u_t, results2[k].u_s, results2[k].M)
        depths_k = compute_core_depths(sources2[k].u, grid)
        deep_mask_k = depths_k >= 2
        p_deep = persist_restricted(results2[k].u_t, results2[k].u_s, results2[k].M, deep_mask_k)
        nc, nb, nd = core_boundary_size(sources2[k].u, grid)
        print(f"  K=2, formation {k}: Persist_full={p_full:.4f}, Persist_deep={p_deep:.4f}")
        print(f"       Core={nc}, Boundary={nb}, Deep={nd}")

    print(f"\n  P1-K prediction: deep core Persist for K=1 ~ K=2 formations")
    print(f"  K=1 deep Persist: {p1_deep:.4f}")
    p2_deeps = []
    for k in range(2):
        depths_k = compute_core_depths(sources2[k].u, grid)
        deep_mask_k = depths_k >= 2
        pd = persist_restricted(results2[k].u_t, results2[k].u_s, results2[k].M, deep_mask_k)
        p2_deeps.append(pd)
    print(f"  K=2 deep Persist: {p2_deeps}")
    diff = abs(p1_deep - np.mean(p2_deeps))
    print(f"  |Difference|: {diff:.4f}")
    print(f"  PASS: {diff < 0.15}" if diff < 0.15 else f"  FAIL: {diff:.4f} >= 0.15")


# ============================================================
# P2-K: Simplex violation scaling
# ============================================================

def test_p2k():
    print("\n" + "=" * 60)
    print("P2-K: Simplex violation scaling with boundary size")
    print("=" * 60)

    grid = GraphState.grid_2d(15, 15)
    params = ParameterRegistry(
        volume_fraction=0.3, beta_bd=50.0, a_cl=3.5,
    )

    print(f"\n  {'lam_rep':>8} {'d_min':>6} {'regime':>20} {'max_viol':>10} "
          f"{'L1_viol':>10} {'|dCore|':>8} {'|Core|':>8} {'viol/dC':>10} {'viol/C':>10}")
    print("  " + "-" * 110)

    for lam_rep in [0.5, 1.0, 5.0, 10.0, 25.0, 50.0, 100.0]:
        sources = find_k_formations(grid, params, K=2, lambda_rep=lam_rep, max_iter=1500, n_restarts=3)
        fields = [s.u for s in sources]
        d_min = inter_formation_distances(fields, grid)
        regime = classify_regime(fields, grid)

        # Transport WITHOUT correction to see raw violation
        results = transport_k_formations(
            sources, grid, params, lambda_rep=lam_rep, phase2_mode='none',
            sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10,
        )

        S = sum(r.u_s for r in results)
        violation = np.maximum(0.0, S - 1.0)
        max_viol = float(np.max(violation))
        l1_viol = float(np.sum(violation))

        # Average boundary and core sizes across formations
        total_boundary = 0
        total_core = 0
        for k in range(2):
            nc, nb, nd = core_boundary_size(sources[k].u, grid)
            total_boundary += nb
            total_core += nc

        viol_per_bnd = l1_viol / max(total_boundary, 1)
        viol_per_core = l1_viol / max(total_core, 1)

        print(f"  {lam_rep:>8.1f} {d_min[0,1]:>6.0f} {regime:>20} {max_viol:>10.4f} "
              f"{l1_viol:>10.4f} {total_boundary:>8} {total_core:>8} "
              f"{viol_per_bnd:>10.4f} {viol_per_core:>10.4f}")

    print("\n  P2-K prediction: viol/|dCore| ~ constant, viol/|Core| decreases with separation")


# ============================================================
# P3-K: Reoptimize effect on deep vs boundary Persist
# ============================================================

def test_p3k():
    print("\n" + "=" * 60)
    print("P3-K: Reoptimize effect on deep vs boundary Persist")
    print("=" * 60)

    grid = GraphState.grid_2d(15, 15)
    params = ParameterRegistry(
        volume_fraction=0.3, beta_bd=50.0, a_cl=3.5,
    )

    # Use moderate repulsion for weakly-interacting regime
    print("\n  Finding K=2 formations (lambda_rep=5.0, weakly-interacting target)...")
    sources = find_k_formations(grid, params, K=2, lambda_rep=5.0, max_iter=1500, n_restarts=3)
    regime = classify_regime([s.u for s in sources], grid)
    d_min = inter_formation_distances([s.u for s in sources], grid)
    print(f"  d_min={d_min[0,1]:.0f}, regime={regime}")

    transport_kw = dict(sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10)

    print(f"\n  {'mode':>12} {'k':>3} {'P_full':>8} {'P_deep':>8} {'P_bnd':>8} {'n_deep':>7} {'n_bnd':>7}")
    print("  " + "-" * 65)

    for mode in ['none', 'correction', 'reoptimize']:
        results = transport_k_formations(
            sources, grid, params, lambda_rep=5.0,
            phase2_mode=mode, **transport_kw,
        )
        for k in range(2):
            p_full = persist_transport(results[k].u_t, results[k].u_s, results[k].M)
            depths_k = compute_core_depths(sources[k].u, grid)
            deep_mask = depths_k >= 2
            bnd_mask = (sources[k].u >= THETA_CORE) & (depths_k == 1)
            p_deep = persist_restricted(results[k].u_t, results[k].u_s, results[k].M, deep_mask)
            p_bnd = persist_restricted(results[k].u_t, results[k].u_s, results[k].M, bnd_mask)
            n_deep = int(np.sum(deep_mask))
            n_bnd = int(np.sum(bnd_mask))
            print(f"  {mode:>12} {k:>3} {p_full:>8.4f} {p_deep:>8.4f} {p_bnd:>8.4f} {n_deep:>7} {n_bnd:>7}")

    print("\n  P3-K prediction: deep core Persist unchanged across modes;")
    print("                   boundary Persist improved by reoptimize")


# ============================================================
# P4-K: Repulsion increases spectral gap
# ============================================================

def test_p4k():
    print("\n" + "=" * 60)
    print("P4-K: Repulsion increases effective spectral gap")
    print("=" * 60)
    print("\n  Note: d^2/du^k^2 (lambda_rep * u^j . u^k) = 0 (linear in u^k),")
    print("  so repulsion does NOT directly add to the Hessian. P4-K predicts that")
    print("  repulsion changes the equilibrium point such that the self-energy")
    print("  Hessian has better curvature (deeper basin) at the new equilibrium.")

    grid = GraphState.grid_2d(10, 10)
    params = ParameterRegistry(volume_fraction=0.3, beta_bd=50.0, a_cl=3.5)
    n = grid.n
    ec = EnergyComputer(grid, params)
    ec.normalize_weights()

    def fd_hessian_spectral_norm(grad_fn, u0, n_iter=50, h=1e-5):
        """Estimate largest eigenvalue of Hessian via power iteration."""
        g0 = grad_fn(u0)
        rng = np.random.RandomState(42)
        v = rng.randn(len(u0))
        v -= np.mean(v)
        v /= np.linalg.norm(v)
        sigma = 0.0
        for _ in range(n_iter):
            gv = grad_fn(u0 + h * v)
            Hv = (gv - g0) / h
            Hv -= np.mean(Hv)
            sigma = np.linalg.norm(Hv)
            if sigma < 1e-15:
                break
            v = Hv / sigma
        return sigma

    def fd_hessian_min_eigenvalue(grad_fn, u0, n_iter=80, h=1e-5):
        """Estimate smallest non-trivial eigenvalue via shift-invert."""
        g0 = grad_fn(u0)
        mu_max = fd_hessian_spectral_norm(grad_fn, u0)
        rng = np.random.RandomState(42)
        v = rng.randn(len(u0))
        v -= np.mean(v)
        v /= np.linalg.norm(v)
        sigma = 0.0
        for _ in range(n_iter):
            gv = grad_fn(u0 + h * v)
            Hv = (gv - g0) / h
            Hv -= np.mean(Hv)
            shifted = mu_max * v - Hv
            sigma = np.linalg.norm(shifted)
            if sigma < 1e-15:
                break
            v = shifted / sigma
        return mu_max - sigma

    def self_grad(u, _ec=ec):
        return _ec.gradient_projected(u)

    # Compare self-energy Hessian at equilibria found with varying repulsion
    print(f"\n  {'lam_rep':>8} {'mu_min_0':>10} {'mu_min_1':>10} {'mu_max_0':>10} {'mu_max_1':>10} {'d_min':>6}")
    print("  " + "-" * 60)

    all_mu_mins = {}
    for lam_rep in [0.1, 1.0, 10.0, 50.0]:
        sources = find_k_formations(grid, params, K=2, lambda_rep=lam_rep, max_iter=1500, n_restarts=3)
        d_min = inter_formation_distances([s.u for s in sources], grid)

        mu_mins = []
        mu_maxs = []
        for k in range(2):
            mu_min = fd_hessian_min_eigenvalue(self_grad, sources[k].u)
            mu_max = fd_hessian_spectral_norm(self_grad, sources[k].u)
            mu_mins.append(mu_min)
            mu_maxs.append(mu_max)

        all_mu_mins[lam_rep] = mu_mins
        print(f"  {lam_rep:>8.1f} {mu_mins[0]:>10.4f} {mu_mins[1]:>10.4f} "
              f"{mu_maxs[0]:>10.4f} {mu_maxs[1]:>10.4f} {d_min[0,1]:>6.0f}")

    mu_low = min(all_mu_mins[0.1])
    mu_high = min(all_mu_mins[50.0])
    print(f"\n  min eigenvalue at lam_rep=0.1: {mu_low:.4f}")
    print(f"  min eigenvalue at lam_rep=50.0: {mu_high:.4f}")
    print(f"  mu_joint > min(mu_k): {mu_high > mu_low}")
    print(f"  Ratio: {mu_high / max(abs(mu_low), 1e-15):.4f}")


# ============================================================
# E2 Reproducibility: 3 seeds
# ============================================================

def test_e2_reproducibility():
    print("\n" + "=" * 60)
    print("E2 Reproducibility: 3 seeds for multi-formation transport")
    print("=" * 60)

    grid = GraphState.grid_2d(15, 15)

    transport_kw = dict(sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10)

    print(f"\n  {'seed':>6} {'d_min':>6} {'regime':>20} {'P_0':>8} {'P_1':>8} {'max_viol':>10}")
    print("  " + "-" * 70)

    all_persists = []
    for seed in range(3):
        rng = np.random.RandomState(seed)
        params = ParameterRegistry(
            volume_fraction=0.3, beta_bd=50.0, a_cl=3.5,
            eps_init=0.01 + 0.003 * seed,
        )

        sources = find_k_formations(grid, params, K=2, lambda_rep=50.0, max_iter=1500, n_restarts=3)
        d_min = inter_formation_distances([s.u for s in sources], grid)
        regime = classify_regime([s.u for s in sources], grid)

        results = transport_k_formations(
            sources, grid, params, lambda_rep=50.0, **transport_kw,
        )

        persists = [persist_transport(r.u_t, r.u_s, r.M) for r in results]
        S = sum(r.u_s for r in results)
        max_viol = float(np.max(np.maximum(0.0, S - 1.0)))

        all_persists.append(persists)
        print(f"  {seed:>6} {d_min[0,1]:>6.0f} {regime:>20} "
              f"{persists[0]:>8.4f} {persists[1]:>8.4f} {max_viol:>10.4f}")

    arr = np.array(all_persists)
    print(f"\n  Mean Persist: {np.mean(arr):.4f} +/- {np.std(arr):.4f}")
    print(f"  Per-formation mean: [{np.mean(arr[:,0]):.4f}, {np.mean(arr[:,1]):.4f}]")
    print(f"  Per-formation std:  [{np.std(arr[:,0]):.4f}, {np.std(arr[:,1]):.4f}]")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    t0 = time.time()
    test_p1k()
    test_p2k()
    test_p3k()
    test_p4k()
    test_e2_reproducibility()
    print(f"\n{'='*60}")
    print(f"Total time: {time.time()-t0:.1f}s")
