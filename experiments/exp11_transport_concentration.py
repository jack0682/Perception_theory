#!/usr/bin/env python3
"""Experiment 11: Transport Concentration Verification
Verifies that entropy-regularized OT maps core sites to core sites.

Theory predicts:
- Core fraction of transport mass >= 1 - n*exp(-gamma*Delta_phi^2/eps_ot)
- Deep core: exponentially strong concentration
- Shallow core: weak concentration
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot,
)

GRID = (15, 15)
BETA = 50.0
C = 0.3
THETA_CORE = 0.8
GAMMAS = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
EPS_OTS = [0.1, 0.5, 1.0]


def compute_core_transport_fraction(M, core_mask_t, core_mask_s):
    """Fraction of transport mass from core_t that lands in core_s."""
    row_mass = M[core_mask_t, :].sum()
    if row_mass < 1e-15:
        return 0.0
    core_core_mass = M[np.ix_(core_mask_t, core_mask_s)].sum()
    return float(core_core_mass / row_mass)


def compute_deep_core_fraction(M, deep_core_t, core_mask_s):
    """Fraction of transport mass from deep core_t that lands in core_s."""
    if not np.any(deep_core_t):
        return 0.0
    row_mass = M[deep_core_t, :].sum()
    if row_mass < 1e-15:
        return 0.0
    core_mass = M[np.ix_(deep_core_t, core_mask_s)].sum()
    return float(core_mass / row_mass)


def theory_lower_bound(n, gamma, delta_phi_sq, eps_ot):
    """Theoretical lower bound: 1 - n * exp(-gamma * delta_phi_sq / eps_ot)."""
    exponent = -gamma * delta_phi_sq / eps_ot
    if exponent < -500:
        return 1.0
    return max(0.0, 1.0 - n * np.exp(exponent))


def classify_depth(u, graph, theta_core=THETA_CORE):
    """Return boolean masks for deep core (δ>=2) and shallow core (δ=1)."""
    core_mask = u >= theta_core
    n = graph.n
    if not np.any(core_mask):
        return np.zeros(n, bool), np.zeros(n, bool)

    # Use adjacency to find boundary
    W_dense = graph.W.toarray()
    noncore = ~core_mask

    # For each core site, check if any neighbor is non-core
    boundary_core = np.zeros(n, bool)
    for i in np.where(core_mask)[0]:
        neighbors = np.where(W_dense[i, :] > 0)[0]
        if np.any(noncore[neighbors]):
            boundary_core[i] = True

    shallow_core = boundary_core  # δ = 1
    deep_core = core_mask & ~boundary_core  # δ >= 2
    return deep_core, shallow_core


def main():
    print("Experiment 11: Transport Concentration Verification")
    print(f"Grid: {GRID}, β={BETA}, c={C}, θ_core={THETA_CORE}")
    print()

    t0 = time.time()

    graph = GraphState.grid_2d(*GRID)
    n = graph.n
    params = ParameterRegistry(
        beta_bd=BETA, volume_fraction=C, n_restarts=5, max_iter=5000,
    )
    result = find_formation(graph, params)
    u = result.u

    print(f"Formation found: E={result.energy:.6f}")
    print(f"Diagnostics: {result.diagnostics}")
    print(f"Core sites: {np.sum(u >= THETA_CORE)}, n={n}")
    print()

    # Compute fingerprints and distances
    phi = cohesion_fingerprint(u, graph, params)
    dist_matrix = graph_distance_matrix(graph)
    core_mask = u >= THETA_CORE
    deep_core, shallow_core = classify_depth(u, graph)

    print(f"Deep core sites (δ≥2): {np.sum(deep_core)}")
    print(f"Shallow core sites (δ=1): {np.sum(shallow_core)}")
    print()

    # Compute fingerprint gaps
    noncore = ~core_mask
    if np.any(noncore) and np.any(deep_core):
        phi_deep_mean = phi[deep_core].mean(axis=0)
        phi_noncore_mean = phi[noncore].mean(axis=0)
        delta_phi_sq_deep = float(np.sum((phi_deep_mean - phi_noncore_mean)**2))
    else:
        delta_phi_sq_deep = 0.0

    if np.any(noncore) and np.any(shallow_core):
        phi_shallow_mean = phi[shallow_core].mean(axis=0)
        phi_noncore_mean = phi[noncore].mean(axis=0)
        delta_phi_sq_shallow = float(np.sum((phi_shallow_mean - phi_noncore_mean)**2))
    else:
        delta_phi_sq_shallow = 0.0

    print(f"Fingerprint gap (deep core): Δ_φ² = {delta_phi_sq_deep:.4f} (theory ≈ 2.87)")
    print(f"Fingerprint gap (shallow core): Δ_φ² = {delta_phi_sq_shallow:.4f} (theory ≈ 0.05)")
    print()

    # Sweep gamma and eps_ot
    print("="*90)
    print("Transport Concentration: Core-to-Core Mass Fraction")
    print("="*90)
    print(f"  {'gamma':>6s} {'eps_ot':>7s} {'core_frac':>10s} {'deep_frac':>10s} "
          f"{'theory_lb':>10s} {'theory_lb_d':>12s} {'Sinkhorn':>10s}")
    print(f"  {'-'*6} {'-'*7} {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*10}")

    for eps_ot in EPS_OTS:
        for gamma in GAMMAS:
            # Compute transport cost and solve OT (self-transport: t=s)
            cost = transport_cost(phi, phi, dist_matrix, sigma=2.0, gamma=gamma)
            M, info = sinkhorn_partial_ot(cost, u, u, eps_ot, max_iter=200, tol=1e-8)

            core_frac = compute_core_transport_fraction(M, core_mask, core_mask)
            deep_frac = compute_deep_core_fraction(M, deep_core, core_mask)
            lb_all = theory_lower_bound(n, gamma, delta_phi_sq_deep, eps_ot)
            lb_deep = theory_lower_bound(n, gamma, delta_phi_sq_deep, eps_ot)

            sk_status = "conv" if info['converged'] else f"err={info['marginal_error']:.1e}"

            print(f"  {gamma:>6.1f} {eps_ot:>7.2f} {core_frac:>10.6f} {deep_frac:>10.6f} "
                  f"{lb_all:>10.6f} {lb_deep:>12.6f} {sk_status:>10s}")
        print()

    # Detailed analysis for one (gamma, eps_ot) pair
    gamma_detail = 2.0
    eps_detail = 0.5
    print("="*90)
    print(f"Detailed Analysis: gamma={gamma_detail}, eps_ot={eps_detail}")
    print("="*90)

    cost = transport_cost(phi, phi, dist_matrix, sigma=2.0, gamma=gamma_detail)
    M, info = sinkhorn_partial_ot(cost, u, u, eps_detail, max_iter=200, tol=1e-8)

    # Per-site core mass fraction
    core_mass_per_site = np.zeros(n)
    for i in range(n):
        row_sum = M[i, :].sum()
        if row_sum > 1e-15:
            core_mass_per_site[i] = M[i, core_mask].sum() / row_sum

    print(f"  {'Category':<20s} {'n_sites':>8s} {'mean_core_frac':>15s} {'min_core_frac':>15s}")
    print(f"  {'-'*20} {'-'*8} {'-'*15} {'-'*15}")

    if np.any(deep_core):
        vals = core_mass_per_site[deep_core]
        print(f"  {'Deep core (δ≥2)':<20s} {np.sum(deep_core):>8d} {vals.mean():>15.6f} {vals.min():>15.6f}")

    if np.any(shallow_core):
        vals = core_mass_per_site[shallow_core]
        print(f"  {'Shallow core (δ=1)':<20s} {np.sum(shallow_core):>8d} {vals.mean():>15.6f} {vals.min():>15.6f}")

    if np.any(noncore):
        vals = core_mass_per_site[noncore]
        print(f"  {'Non-core':<20s} {np.sum(noncore):>8d} {vals.mean():>15.6f} {vals.min():>15.6f}")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
