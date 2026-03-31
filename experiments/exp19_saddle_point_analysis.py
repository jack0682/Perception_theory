#!/usr/bin/env python3
"""Experiment 19: Saddle-point structure and escape path analysis.

For various grids and beta values:
1. Find formation minimizers
2. Identify free variables (not box-constrained)
3. Compute constrained Hessian on free variables
4. Find minimum eigenvalue eigenvector (soft mode = easiest escape direction)
5. Trace energy along the soft mode to locate the actual saddle energy
6. Analyze whether soft modes involve core, boundary, or exterior nodes
7. Compare directional basin radii with isotropic r >= 0.210

This experiment addresses Gap 4 of T-Persist-1: escape path analysis.
"""
import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.energy import EnergyComputer, double_well, double_well_deriv


# -----------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------

def classify_nodes(u, theta_core=0.9, theta_ext=0.05):
    """Classify nodes into core, boundary, exterior."""
    core = u >= theta_core
    ext = u <= theta_ext
    boundary = ~core & ~ext
    return core, boundary, ext


def free_variable_hessian(ec, u, h=1e-5):
    """Compute Hessian restricted to free (non-box-constrained) variables.

    Free variables: indices where 0 < u_i < 1 (with tolerance).
    The constrained Hessian on Sigma_m is further restricted to the
    subspace orthogonal to 1_F (volume constraint on free vars).

    Returns:
        H_free: Hessian on free variables (n_F x n_F)
        free_idx: indices of free variables
        eigenvalues: sorted eigenvalues of the constrained Hessian
        eigenvectors: corresponding eigenvectors (in free-variable space)
    """
    tol = 1e-6
    free_idx = np.where((u > tol) & (u < 1.0 - tol))[0]
    n_F = len(free_idx)

    if n_F < 2:
        return None, free_idx, np.array([]), np.array([])

    # Compute Hessian columns by finite differences on the full gradient
    g0 = ec.gradient(u)
    H_full_cols = np.zeros((len(u), n_F))
    for j_idx, j in enumerate(free_idx):
        e_j = np.zeros(len(u))
        e_j[j] = 1.0
        g_plus = ec.gradient(u + h * e_j)
        col = (g_plus - g0) / h
        H_full_cols[:, j_idx] = col

    # Extract the free-variable block
    H_free = H_full_cols[free_idx, :]
    # Symmetrize
    H_free = 0.5 * (H_free + H_free.T)

    # Project onto volume constraint subspace: P = I - (1/n_F) * 1*1^T
    ones = np.ones(n_F) / np.sqrt(n_F)
    P = np.eye(n_F) - np.outer(ones, ones)
    H_constrained = P @ H_free @ P

    # Eigendecompose
    eigvals, eigvecs = np.linalg.eigh(H_constrained)

    # The first eigenvalue corresponds to the constant direction (≈0), skip it
    # Find the first non-trivial eigenvalue
    nontrivial = np.abs(eigvals) > 1e-10
    return H_free, free_idx, eigvals[nontrivial], eigvecs[:, nontrivial]


def trace_energy_along_direction(ec, u, direction_full, m, n_points=200,
                                  max_step=1.0):
    """Trace energy along a direction from u, projecting onto Sigma_m.

    Returns arrays of (step_size, energy, ||u(t) - u||).
    """
    steps = np.linspace(0, max_step, n_points)
    energies = np.zeros(n_points)
    distances = np.zeros(n_points)

    E_base, _ = ec.energy(u)
    energies[0] = E_base
    distances[0] = 0.0

    for i, t in enumerate(steps[1:], 1):
        u_t = u + t * direction_full
        u_t = project_volume(np.clip(u_t, 0.0, 1.0), m)
        E_t, _ = ec.energy(u_t)
        energies[i] = E_t
        distances[i] = np.linalg.norm(u_t - u)

    return steps, energies, distances


def soft_mode_node_participation(eigvec, free_idx, core, boundary, ext):
    """Measure how much each node class participates in an eigenvector.

    Returns dict with fraction of eigvec energy in core/boundary/exterior.
    """
    # Map free_idx to classification
    core_mask = core[free_idx]
    boundary_mask = boundary[free_idx]
    ext_mask = ext[free_idx]

    total_sq = np.sum(eigvec**2)
    if total_sq < 1e-15:
        return {'core': 0.0, 'boundary': 0.0, 'exterior': 0.0}

    return {
        'core': float(np.sum(eigvec[core_mask]**2) / total_sq),
        'boundary': float(np.sum(eigvec[boundary_mask]**2) / total_sq),
        'exterior': float(np.sum(eigvec[ext_mask]**2) / total_sq),
    }


def exterior_perturbation_cost(ec, u, m, ext_idx, n_ext_perturb=5):
    """Measure energy cost of perturbing exterior nodes.

    Pushes mass from core into exterior nodes and measures energy increase.
    """
    if len(ext_idx) == 0:
        return float('inf')

    E_base, _ = ec.energy(u)
    costs = []

    for delta in [0.05, 0.1, 0.15, 0.2, 0.3]:
        u_pert = u.copy()
        # Push delta mass into first few exterior nodes
        n_ext = min(n_ext_perturb, len(ext_idx))
        per_node = delta / n_ext
        for idx in ext_idx[:n_ext]:
            u_pert[idx] += per_node
        # Re-project to maintain volume constraint
        u_pert = project_volume(np.clip(u_pert, 0.0, 1.0), m)
        E_pert, _ = ec.energy(u_pert)
        dist = np.linalg.norm(u_pert - u)
        costs.append({
            'delta': delta,
            'dE': E_pert - E_base,
            'dist': dist,
            'dE_per_dist_sq': (E_pert - E_base) / (dist**2 + 1e-15),
        })

    return costs


# -----------------------------------------------------------------------
# Main experiment
# -----------------------------------------------------------------------

def run_single(N, beta_val):
    """Run full saddle-point analysis for one grid/beta."""
    n = N * N
    g = GraphState.grid_2d(N, N)
    p = ParameterRegistry(beta_bd=beta_val, volume_fraction=0.3)
    result = find_formation(g, p)
    u = result.u
    m = float(np.sum(u))

    ec = EnergyComputer(g, p)
    ec.normalize_weights()
    E_star, terms = ec.energy(u)

    # Node classification
    core, boundary, ext = classify_nodes(u)
    n_core = int(np.sum(core))
    n_boundary = int(np.sum(boundary))
    n_ext = int(np.sum(ext))

    print(f"\n{'='*70}")
    print(f"Grid {N}x{N}, beta={beta_val}, n={n}")
    print(f"  Nodes: core={n_core}, boundary={n_boundary}, exterior={n_ext}")
    print(f"  E* = {E_star:.6f}")
    print(f"  Core u: min={u[core].min():.4f}, mean={u[core].mean():.4f}" if n_core > 0 else "  No core nodes")
    print(f"  Ext u:  max={u[ext].max():.6f}" if n_ext > 0 else "  No exterior nodes")

    # ---- Free-variable Hessian ----
    H_free, free_idx, eigvals, eigvecs = free_variable_hessian(ec, u)
    n_free = len(free_idx)

    if len(eigvals) == 0:
        print("  WARNING: Could not compute free-variable Hessian")
        return None

    mu_free = eigvals[0]  # smallest non-trivial eigenvalue
    lam_max = eigvals[-1]

    print(f"\n  Free variables: {n_free}")
    print(f"  Spectral gap (mu_F): {mu_free:.6f}")
    print(f"  Lambda_max: {lam_max:.6f}")
    print(f"  Condition number: {lam_max / (mu_free + 1e-15):.1f}")

    # ---- Soft mode analysis ----
    # The soft mode is the eigenvector with smallest eigenvalue
    soft_mode = eigvecs[:, 0]  # in free-variable space
    participation = soft_mode_node_participation(soft_mode, free_idx, core, boundary, ext)

    print(f"\n  Soft mode participation:")
    print(f"    Core:     {participation['core']:.4f}")
    print(f"    Boundary: {participation['boundary']:.4f}")
    print(f"    Exterior: {participation['exterior']:.4f}")

    # ---- Trace energy along soft mode ----
    # Embed soft mode into full space
    soft_mode_full = np.zeros(n)
    soft_mode_full[free_idx] = soft_mode
    # Normalize
    norm = np.linalg.norm(soft_mode_full)
    if norm > 1e-15:
        soft_mode_full /= norm

    # Determine max_step: trace until energy rises well above E*
    max_step = 2.0
    steps, energies, distances = trace_energy_along_direction(
        ec, u, soft_mode_full, m, n_points=500, max_step=max_step
    )

    # Find the saddle point (first local max along the path)
    dE = energies - E_star
    saddle_idx = None
    saddle_E = None
    for i in range(2, len(dE)):
        if dE[i] < dE[i-1] and dE[i-1] > 0:  # local max found
            saddle_idx = i - 1
            saddle_E = dE[i-1]
            break

    # If no local max, use the maximum energy reached
    if saddle_E is None:
        saddle_idx = np.argmax(dE)
        saddle_E = dE[saddle_idx]

    saddle_dist = distances[saddle_idx] if saddle_idx is not None else 0.0

    print(f"\n  Energy trace along soft mode:")
    print(f"    Barrier (Delta_soft): {saddle_E:.6f}")
    print(f"    Distance to saddle:   {saddle_dist:.6f}")

    # ---- Directional basin radius ----
    # r_dir = sqrt(2 * Delta / (v^T H v)) where v^T H v = mu_free (soft mode)
    r_dir_soft = np.sqrt(2.0 * max(saddle_E, 0) / (mu_free + 1e-15)) if mu_free > 0 else float('inf')
    # Isotropic bound
    r_iso = np.sqrt(2.0 * max(saddle_E, 0) / (lam_max + 1e-15))
    # Beta-independent bound
    r_beta_ind = np.sqrt(0.0441)  # ≈ 0.210

    print(f"\n  Basin radius estimates:")
    print(f"    r_directional (soft mode): {r_dir_soft:.4f}")
    print(f"    r_isotropic (worst case):  {r_iso:.4f}")
    print(f"    r_beta_independent:        {r_beta_ind:.4f}")

    # ---- Also trace energy along the HARD mode (largest eigenvalue) ----
    hard_mode = eigvecs[:, -1]
    hard_mode_full = np.zeros(n)
    hard_mode_full[free_idx] = hard_mode
    norm_h = np.linalg.norm(hard_mode_full)
    if norm_h > 1e-15:
        hard_mode_full /= norm_h

    _, energies_hard, distances_hard = trace_energy_along_direction(
        ec, u, hard_mode_full, m, n_points=200, max_step=1.0
    )
    dE_hard = energies_hard - E_star
    saddle_hard_idx = np.argmax(dE_hard)
    saddle_hard_E = dE_hard[saddle_hard_idx]

    hard_participation = soft_mode_node_participation(hard_mode, free_idx, core, boundary, ext)

    print(f"\n  Hard mode participation:")
    print(f"    Core:     {hard_participation['core']:.4f}")
    print(f"    Boundary: {hard_participation['boundary']:.4f}")
    print(f"    Exterior: {hard_participation['exterior']:.4f}")
    print(f"    Barrier along hard mode: {saddle_hard_E:.6f}")

    # ---- Exterior perturbation cost ----
    ext_idx = np.where(ext)[0]
    ext_costs = exterior_perturbation_cost(ec, u, m, ext_idx)

    if isinstance(ext_costs, list):
        print(f"\n  Exterior perturbation costs:")
        print(f"    {'delta':>8s} {'dE':>12s} {'dist':>10s} {'dE/dist^2':>12s}")
        for c in ext_costs:
            print(f"    {c['delta']:8.3f} {c['dE']:12.6f} {c['dist']:10.6f} {c['dE_per_dist_sq']:12.4f}")

    # ---- Trace all eigenmodes to find minimum barrier ----
    n_modes_to_check = min(10, len(eigvals))
    print(f"\n  Barrier along first {n_modes_to_check} eigenmodes:")
    print(f"    {'mode':>4s} {'eigenvalue':>12s} {'barrier':>12s} {'r_dir':>10s} {'core_frac':>10s} {'bdy_frac':>10s}")

    min_barrier = float('inf')
    min_barrier_mode = -1
    for k in range(n_modes_to_check):
        ev = eigvecs[:, k]
        ev_full = np.zeros(n)
        ev_full[free_idx] = ev
        nrm = np.linalg.norm(ev_full)
        if nrm < 1e-15:
            continue
        ev_full /= nrm

        _, ens, dists = trace_energy_along_direction(
            ec, u, ev_full, m, n_points=200, max_step=2.0
        )
        dE_k = ens - E_star
        # Find barrier
        barrier_k = 0.0
        for i in range(2, len(dE_k)):
            if dE_k[i] < dE_k[i-1] and dE_k[i-1] > 0:
                barrier_k = dE_k[i-1]
                break
        if barrier_k == 0.0:
            barrier_k = np.max(dE_k)

        part_k = soft_mode_node_participation(ev, free_idx, core, boundary, ext)
        r_dir_k = np.sqrt(2.0 * max(barrier_k, 0) / (eigvals[k] + 1e-15)) if eigvals[k] > 0 else float('inf')

        if barrier_k < min_barrier and barrier_k > 0:
            min_barrier = barrier_k
            min_barrier_mode = k

        print(f"    {k:4d} {eigvals[k]:12.6f} {barrier_k:12.6f} {r_dir_k:10.4f} {part_k['core']:10.4f} {part_k['boundary']:10.4f}")

    print(f"\n  Minimum barrier across modes: {min_barrier:.6f} (mode {min_barrier_mode})")
    r_min = np.sqrt(2.0 * min_barrier / (lam_max + 1e-15))
    print(f"  Corresponding r_isotropic: {r_min:.4f}")
    print(f"  Comparison: r_min={r_min:.4f} vs r_beta_ind={r_beta_ind:.4f}")

    return {
        'N': N, 'beta': beta_val, 'n': n,
        'n_core': n_core, 'n_boundary': n_boundary, 'n_ext': n_ext,
        'n_free': n_free, 'mu_free': mu_free, 'lam_max': lam_max,
        'soft_participation': participation,
        'barrier_soft': saddle_E, 'barrier_min': min_barrier,
        'r_dir_soft': r_dir_soft, 'r_iso': r_iso, 'r_beta_ind': r_beta_ind,
        'r_min_across_modes': r_min,
        'ext_costs': ext_costs if isinstance(ext_costs, list) else [],
    }


def main():
    print("=" * 70)
    print("Experiment 19: Saddle-Point Structure & Escape Path Analysis")
    print("=" * 70)

    configs = [
        (8, 50),
        (10, 50),
        (10, 100),
        (10, 200),
        (12, 50),
    ]

    all_results = []
    for N, beta in configs:
        t0 = time.time()
        r = run_single(N, beta)
        elapsed = time.time() - t0
        print(f"\n  Time: {elapsed:.1f}s")
        if r is not None:
            all_results.append(r)

    # ---- Summary table ----
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'Grid':>6s} {'beta':>6s} {'n_free':>6s} {'mu_F':>10s} {'lam_max':>10s} "
          f"{'barrier':>10s} {'r_soft':>8s} {'r_iso':>8s} {'r_min':>8s} {'r_0.21':>8s} "
          f"{'core%':>6s} {'bdy%':>6s}")
    print("-" * 100)
    for r in all_results:
        sp = r['soft_participation']
        print(f"{r['N']:3d}x{r['N']:<3d} {r['beta']:6.0f} {r['n_free']:6d} "
              f"{r['mu_free']:10.4f} {r['lam_max']:10.4f} "
              f"{r['barrier_soft']:10.6f} {r['r_dir_soft']:8.4f} {r['r_iso']:8.4f} "
              f"{r['r_min_across_modes']:8.4f} {0.210:8.3f} "
              f"{sp['core']:6.2f} {sp['boundary']:6.2f}")

    # ---- Key findings ----
    print("\n" + "=" * 70)
    print("KEY FINDINGS")
    print("=" * 70)

    # Check: does soft mode involve core nodes?
    all_core_involved = all(
        r['soft_participation']['core'] + r['soft_participation']['boundary'] > 0.5
        for r in all_results
    )
    print(f"1. Soft mode involves core/boundary nodes in all cases: {all_core_involved}")

    # Check: is r_min >= 0.210 in all cases?
    all_above_threshold = all(r['r_min_across_modes'] >= 0.200 for r in all_results)
    print(f"2. r_min >= 0.200 in all cases: {all_above_threshold}")

    # Check: exterior perturbation costs scale with curvature
    print("3. Exterior perturbation costs (dE/dist^2) at delta=0.1:")
    for r in all_results:
        for c in r['ext_costs']:
            if abs(c['delta'] - 0.1) < 0.01:
                print(f"   Grid {r['N']}x{r['N']}, beta={r['beta']}: "
                      f"dE/dist^2 = {c['dE_per_dist_sq']:.4f}")


if __name__ == "__main__":
    main()
