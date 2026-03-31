"""Exp20: Fingerprint Jacobian norm computation at actual formations.

Computes ‖∂φ/∂u‖_op (operator norm of the fingerprint Jacobian)
at formation-structured minimizers for various grid sizes and parameters.
This tightens the conservative estimate of ~3 used in the contraction-
concentration compatibility analysis (Gap 5).

Also verifies fingerprint amplification: Δ_φ² at deep core vs boundary.

References: PERSIST-OT-ANALYSIS.md §2, §7; PERSIST-SYNTHESIS.md §2.1.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.operators import (
    closure_with_jacobian, distinction_with_jacobian,
    closure, distinction, resolvent_diagonal, aggregation,
    sigmoid_deriv,
)
from scc.transport import cohesion_fingerprint


def fingerprint_jacobian_fd(u, graph, params, eps=1e-5):
    """Compute full fingerprint Jacobian via finite differences."""
    n = graph.n
    phi0 = cohesion_fingerprint(u, graph, params)  # (n, 4)
    J = np.zeros((n, 4, n))  # J[i, k, j] = ∂φ_k(x_i)/∂u(x_j)
    for j in range(n):
        u_pert = u.copy()
        u_pert[j] += eps
        phi_pert = cohesion_fingerprint(u_pert, graph, params)
        J[:, :, j] = (phi_pert - phi0) / eps
    return J


def fingerprint_jacobian_analytical(u, graph, params):
    """Compute fingerprint Jacobian analytically (block structure).

    φ = (u, Cl(u), D(u), C_norm(u)) ∈ R^{n×4}

    The Jacobian ∂φ/∂u is a (4n × n) matrix with block structure:
        Block 0: ∂u/∂u = I
        Block 1: ∂Cl/∂u = diag(σ'·a_cl) @ ((1-η)I + η·P)
        Block 2: ∂D/∂u = diag(σ'_D·a_D·(1+λ_D)) @ P
        Block 3: ∂C_norm/∂u (computed via FD for resolvent)

    Returns the operator norm (largest singular value) of the stacked matrix.
    """
    n = graph.n
    import scipy.sparse as sp

    # Block 0: Identity
    J0 = np.eye(n)

    # Block 1: Closure Jacobian
    _, sigma_prime_cl, _ = closure_with_jacobian(u, graph, params)
    scale_cl = sigma_prime_cl * params.a_cl
    mix = (1.0 - params.eta_cl) * sp.eye(n) + params.eta_cl * graph.P
    J1 = (sp.diags(scale_cl) @ mix).toarray()

    # Block 2: Distinction Jacobian
    _, sigma_prime_D, _ = distinction_with_jacobian(u, graph, params)
    scale_D = sigma_prime_D * params.a_D * (1.0 + params.lambda_D)
    J2 = (sp.diags(scale_D) @ graph.P).toarray()

    # Block 3: Resolvent diagonal Jacobian (FD — resolvent is complex)
    eps_fd = 1e-5
    c0 = resolvent_diagonal(u, graph, params)
    c0_norm = np.clip((c0 - 1.0) / np.maximum(c0, 1e-12), 0.0, 1.0)
    J3 = np.zeros((n, n))
    for j in range(n):
        u_pert = u.copy()
        u_pert[j] += eps_fd
        c_pert = resolvent_diagonal(u_pert, graph, params)
        c_pert_norm = np.clip((c_pert - 1.0) / np.maximum(c_pert, 1e-12), 0.0, 1.0)
        J3[:, j] = (c_pert_norm - c0_norm) / eps_fd

    # Stack into (4n × n) matrix
    J_full = np.vstack([J0, J1, J2, J3])

    return J_full


def compute_norms_at_formation(grid_size, params=None, rng_seed=42):
    """Find a formation and compute Jacobian norms."""
    if params is None:
        params = ParameterRegistry()

    graph = GraphState.grid_2d(grid_size, grid_size)
    n = graph.n

    result = find_formation(graph, params)
    u = result.u

    # Compute fingerprint
    phi = cohesion_fingerprint(u, graph, params)

    # Core/exterior classification
    core_mask = u >= params.theta_core
    ext_mask = u < 0.1
    n_core = core_mask.sum()
    n_ext = ext_mask.sum()

    # Fingerprint gap analysis
    if n_core > 0 and n_ext > 0:
        phi_core_mean = phi[core_mask].mean(axis=0)
        phi_ext_mean = phi[ext_mask].mean(axis=0)
        gap_per_component = (phi_core_mean - phi_ext_mean) ** 2
        total_gap = gap_per_component.sum()
    else:
        gap_per_component = np.zeros(4)
        total_gap = 0.0

    # Deep core vs shallow core fingerprint gap
    # Deep core: graph distance >= 2 from boundary
    from scipy.sparse.csgraph import shortest_path
    adj_binary = (graph.W > 0).astype(np.float64)
    dist_all = shortest_path(adj_binary, method='D', directed=False)

    boundary_nodes = []
    for i in range(n):
        if core_mask[i]:
            neighbors = graph.W[i].nonzero()[1]
            if any(not core_mask[j] for j in neighbors):
                boundary_nodes.append(i)

    if boundary_nodes and n_core > 0:
        # Distance from each core node to boundary of core
        core_depth = np.full(n, -1.0)
        for i in range(n):
            if core_mask[i]:
                min_dist_to_boundary = min(
                    dist_all[i, b] for b in boundary_nodes
                ) if boundary_nodes else np.inf
                core_depth[i] = min_dist_to_boundary

        deep_core = np.array([i for i in range(n) if core_mask[i] and core_depth[i] >= 2])
        shallow_core = np.array([i for i in range(n) if core_mask[i] and core_depth[i] == 1])
        # Include core boundary nodes (distance 0) as shallow
        boundary_core = np.array([i for i in range(n) if core_mask[i] and core_depth[i] < 1])
        shallow_core = np.concatenate([shallow_core, boundary_core]) if len(boundary_core) > 0 else shallow_core

        # Fingerprint values at different tiers
        if len(deep_core) > 0:
            phi_deep = phi[deep_core].mean(axis=0)
            u_deep_mean = u[deep_core].mean()
        else:
            phi_deep = np.zeros(4)
            u_deep_mean = 0.0

        if len(shallow_core) > 0:
            phi_shallow = phi[shallow_core].mean(axis=0)
            u_shallow_mean = u[shallow_core].mean()
        else:
            phi_shallow = np.zeros(4)
            u_shallow_mean = 0.0

        # Gap from shallow core to nearest exterior
        if len(shallow_core) > 0 and n_ext > 0:
            ext_indices = np.where(ext_mask)[0]
            shallow_to_ext_gap = np.min([
                np.sum((phi[sc] - phi[ext_indices].mean(axis=0))**2)
                for sc in shallow_core
            ]) if len(shallow_core) > 0 else 0.0
        else:
            shallow_to_ext_gap = 0.0
    else:
        deep_core = np.array([])
        shallow_core = np.array([])
        u_deep_mean = 0.0
        u_shallow_mean = 0.0
        shallow_to_ext_gap = 0.0

    # Jacobian computation
    J_full = fingerprint_jacobian_analytical(u, graph, params)

    # Operator norm = largest singular value
    op_norm = np.linalg.svd(J_full, compute_uv=False)[0]

    # Also compute per-block norms
    J0_norm = 1.0  # Identity
    J1_norm = np.linalg.svd(J_full[n:2*n, :], compute_uv=False)[0]
    J2_norm = np.linalg.svd(J_full[2*n:3*n, :], compute_uv=False)[0]
    J3_norm = np.linalg.svd(J_full[3*n:4*n, :], compute_uv=False)[0]

    # Frobenius norm (alternative)
    frob_norm = np.linalg.norm(J_full, 'fro') / np.sqrt(n)  # per-site

    # Verify with FD
    J_fd = fingerprint_jacobian_fd(u, graph, params)
    # Reshape FD Jacobian to (4n × n)
    J_fd_stacked = J_fd.reshape(n * 4, n, order='C')
    # Actually J_fd is (n, 4, n) so stack as blocks
    J_fd_stacked = np.vstack([J_fd[:, k, :] for k in range(4)])
    fd_op_norm = np.linalg.svd(J_fd_stacked, compute_uv=False)[0]

    return {
        'grid_size': grid_size,
        'n': n,
        'n_core': int(n_core),
        'n_deep_core': len(deep_core),
        'n_shallow_core': len(shallow_core),
        'n_ext': int(n_ext),
        'u_deep_mean': float(u_deep_mean),
        'u_shallow_mean': float(u_shallow_mean),
        'op_norm': float(op_norm),
        'fd_op_norm': float(fd_op_norm),
        'J_cl_norm': float(J1_norm),
        'J_D_norm': float(J2_norm),
        'J_C_norm': float(J3_norm),
        'frob_per_site': float(frob_norm),
        'fingerprint_gap': float(total_gap),
        'gap_components': gap_per_component.tolist(),
        'shallow_to_ext_gap': float(shallow_to_ext_gap),
        'energy': float(result.diagnostics.get('energy', 0)) if isinstance(result.diagnostics, dict) else 0.0,
    }


def main():
    print("=" * 70)
    print("Exp20: Fingerprint Jacobian Norm at Formation Minimizers")
    print("=" * 70)

    # Test multiple grid sizes
    grid_sizes = [8, 10, 15]

    print("\n--- Table 1: Jacobian Operator Norms ---")
    print(f"{'Grid':>6} {'n':>5} {'‖∂φ/∂u‖_op':>12} {'‖∂φ/∂u‖_FD':>12} "
          f"{'‖J_Cl‖':>8} {'‖J_D‖':>8} {'‖J_C‖':>8}")
    print("-" * 70)

    all_results = []
    for gs in grid_sizes:
        r = compute_norms_at_formation(gs)
        all_results.append(r)
        print(f"{gs:>4}x{gs:<1} {r['n']:>5} {r['op_norm']:>12.4f} "
              f"{r['fd_op_norm']:>12.4f} {r['J_cl_norm']:>8.4f} "
              f"{r['J_D_norm']:>8.4f} {r['J_C_norm']:>8.4f}")

    print("\n--- Table 2: Core Structure ---")
    print(f"{'Grid':>6} {'Core':>5} {'Deep':>5} {'Shallow':>7} "
          f"{'u_deep':>8} {'u_shallow':>10}")
    print("-" * 50)
    for r in all_results:
        print(f"{r['grid_size']:>4}x{r['grid_size']:<1} {r['n_core']:>5} "
              f"{r['n_deep_core']:>5} {r['n_shallow_core']:>7} "
              f"{r['u_deep_mean']:>8.4f} {r['u_shallow_mean']:>10.4f}")

    print("\n--- Table 3: Fingerprint Gap Analysis ---")
    print(f"{'Grid':>6} {'Δ_φ²':>8} {'u²':>8} {'Cl²':>8} "
          f"{'D²':>8} {'C²':>8} {'shallow→ext':>12}")
    print("-" * 70)
    for r in all_results:
        gc = r['gap_components']
        print(f"{r['grid_size']:>4}x{r['grid_size']:<1} {r['fingerprint_gap']:>8.4f} "
              f"{gc[0]:>8.4f} {gc[1]:>8.4f} {gc[2]:>8.4f} "
              f"{gc[3]:>8.4f} {r['shallow_to_ext_gap']:>12.4f}")

    print("\n--- Table 4: Contraction-Concentration Compatibility ---")
    print(f"{'Grid':>6} {'‖∂φ/∂u‖':>10} {'μ₀(deep)':>10} {'μ₀(bdy)':>10}")
    print("-" * 45)
    for r in all_results:
        n = r['n']
        norm = r['op_norm']
        log_n_C = np.log(n) + 1  # log n + C with C ≈ 1
        lambda_tr = 1.0
        deep_gap = r['fingerprint_gap']
        shallow_gap = max(r['shallow_to_ext_gap'], 0.01)

        mu0_deep = log_n_C * lambda_tr * norm / max(deep_gap, 0.01)
        mu0_bdy = log_n_C * lambda_tr * norm / shallow_gap

        print(f"{r['grid_size']:>4}x{r['grid_size']:<1} {norm:>10.4f} "
              f"{mu0_deep:>10.2f} {mu0_bdy:>10.2f}")

    # Analytical upper bound on ‖∂φ/∂u‖_op
    print("\n--- Analytical Bounds ---")
    p = ParameterRegistry()
    # J_Cl: ‖diag(σ'·a_cl) · ((1-η)I + η·P)‖ ≤ (a_cl/4) · max(1-η+η, 1) = a_cl/4
    # since max(σ') = 0.25 (at z=0), and ‖(1-η)I + ηP‖ ≤ 1
    cl_bound = p.a_cl / 4.0
    # J_D: ‖diag(σ'_D·a_D·(1+λ_D)) · P‖ ≤ a_D·(1+λ_D)/4 · ‖P‖ = a_D·(1+λ_D)/4
    d_bound = p.a_D * (1 + p.lambda_D) / 4.0
    # Stacked: ‖[I; J_Cl; J_D; J_C]‖ ≤ sqrt(1 + cl_bound² + d_bound² + ‖J_C‖²)
    # But operator norm is NOT submultiplicative for stacked blocks — use sqrt of sum of squares
    # Actually for stacked matrix [A; B; C; D], ‖·‖_op² ≤ ‖A‖² + ‖B‖² + ‖C‖² + ‖D‖²
    total_bound = np.sqrt(1 + cl_bound**2 + d_bound**2 + 1.0)  # J_C ≤ 1 estimate
    print(f"  a_cl/4 = {cl_bound:.4f}  (closure Jacobian bound)")
    print(f"  a_D(1+λ_D)/4 = {d_bound:.4f}  (distinction Jacobian bound)")
    print(f"  Stacked bound √(1 + {cl_bound:.2f}² + {d_bound:.2f}² + 1²) = {total_bound:.4f}")
    print(f"  Conservative estimate used in analysis: 3.0")
    print(f"  Actual measured norms: {[r['op_norm'] for r in all_results]}")

    # Summary
    mean_norm = np.mean([r['op_norm'] for r in all_results])
    print(f"\n  *** Mean measured ‖∂φ/∂u‖_op = {mean_norm:.4f} ***")
    if mean_norm < 3.0:
        improvement = (3.0 - mean_norm) / 3.0 * 100
        print(f"  *** This is {improvement:.1f}% tighter than the conservative estimate of 3.0 ***")
        print(f"  *** Minimum μ₀ for deep core is reduced by factor {3.0/mean_norm:.2f}x ***")


if __name__ == "__main__":
    main()
