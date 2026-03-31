"""Experiment 21: Structural analysis of T-Persist-1 gaps 4/5/6.

Investigates the common structural root of all three gaps:
1. Saddle-point eigenvector structure (Gap 4): Do soft modes involve core nodes?
2. Fingerprint Jacobian norm (Gap 5): Tight bound on ||∂φ/∂u||
3. Interior gap vs core depth (Gap 6): Verify exponential saturation law

This experiment provides numerical evidence for the research loop.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.operators import closure, distinction
from scc.energy import grad_bd, grad_cl, grad_sep, double_well_second_deriv

np.set_printoptions(precision=6, linewidth=120)

def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p


def compute_constrained_hessian_free(u, graph, ec):
    """Compute constrained Hessian on free (non-box-constrained) variables.

    Returns eigenvalues, eigenvectors, free_mask.
    """
    n = len(u)
    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)

    if n_f < 3:
        return None, None, free_mask

    # Compute Hessian via finite differences on free variables
    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]

    # Symmetrize
    H = 0.5 * (H + H.T)

    # Project onto tangent space of Sigma_m (remove constant mode)
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P

    eigvals, eigvecs = np.linalg.eigh(H_proj)
    # Skip the zero eigenvalue from the projection
    nonzero = np.abs(eigvals) > 1e-10

    return eigvals[nonzero], eigvecs[:, nonzero], free_mask


def analyze_saddle_eigenvectors(u, graph, ec, n_grid):
    """Analyze what the soft mode eigenvector looks like spatially."""
    eigvals, eigvecs, free_mask = compute_constrained_hessian_free(u, graph, ec)
    if eigvals is None:
        return None

    free_idx = np.where(free_mask)[0]
    theta = 0.9
    core_mask = u >= theta

    # Minimum eigenvalue = softest direction
    mu = eigvals[0]
    soft_mode_free = eigvecs[:, 0]

    # Expand to full vector
    soft_mode = np.zeros(len(u))
    soft_mode[free_idx] = soft_mode_free

    # How much of the soft mode is on core vs boundary vs exterior?
    core_weight = np.sum(soft_mode[core_mask]**2)
    boundary_mask = free_mask & ~core_mask
    boundary_weight = np.sum(soft_mode[boundary_mask]**2)
    exterior_mask = ~free_mask & ~core_mask  # box-constrained at 0
    exterior_weight = np.sum(soft_mode[~free_mask]**2)  # should be 0

    total = core_weight + boundary_weight + exterior_weight
    if total > 0:
        core_frac = core_weight / total
        boundary_frac = boundary_weight / total
    else:
        core_frac = boundary_frac = 0

    # Core depth of soft mode concentration
    # Which nodes does the soft mode concentrate on?
    top_nodes = np.argsort(np.abs(soft_mode))[-5:]
    top_depths = []
    for node in top_nodes:
        if core_mask[node]:
            # BFS distance to boundary
            from collections import deque
            adj = graph.W
            visited = {node}
            q = deque([(node, 0)])
            min_dist = n_grid * 2
            while q:
                curr, d = q.popleft()
                row = adj.getrow(curr)
                for nb in row.indices:
                    if not core_mask[nb]:
                        min_dist = min(min_dist, d + 1)
                    elif nb not in visited:
                        visited.add(nb)
                        q.append((nb, d + 1))
            top_depths.append(min_dist)
        else:
            top_depths.append(0)

    return {
        'mu': mu,
        'n_free': len(free_idx),
        'n_core': int(np.sum(core_mask)),
        'core_frac': core_frac,
        'boundary_frac': boundary_frac,
        'top_5_depths': top_depths,
        'eigvals_first5': eigvals[:5].tolist(),
    }


def compute_fingerprint_jacobian(u, graph, params):
    """Compute ||∂φ/∂u||_op via finite differences at a formation."""
    n = len(u)
    h = 1e-5

    # φ(u) = (u, Cl(u), D(x; 1-u), C(x,x))
    from scc.operators import resolvent_diagonal as _rd

    def phi(v):
        # Clip to [0,1] to avoid operator domain issues
        v_safe = np.clip(v, 0.0, 1.0)
        cl = closure(v_safe, graph, params)
        d = distinction(v_safe, graph, params)
        # resolvent diagonal for co-belonging
        r = _rd(v_safe, graph, params)
        return np.concatenate([v_safe, cl, d, r])

    phi0 = phi(u)

    # Build full Jacobian via column-wise FD (feasible for n ≤ 100)
    J = np.zeros((len(phi0), n))
    for i in range(n):
        ei = np.zeros(n)
        ei[i] = h
        J[:, i] = (phi(u + ei) - phi0) / h

    # Operator norm = largest singular value
    from numpy.linalg import svd
    s = svd(J, compute_uv=False)
    return float(s[0])


def analyze_interior_gap(u, graph, n_grid):
    """Measure interior gap as function of core depth."""
    theta = 0.9
    core_mask = u >= theta
    n = len(u)

    if not np.any(core_mask):
        return {}

    # BFS from non-core to compute depth for each core node
    from collections import deque
    adj = graph.W
    depth = np.full(n, -1)
    q = deque()

    # Initialize from all non-core nodes
    for i in range(n):
        if not core_mask[i]:
            depth[i] = 0
            q.append(i)

    while q:
        curr = q.popleft()
        row = adj.getrow(curr)
        for nb in row.indices:
            if depth[nb] == -1:
                depth[nb] = depth[curr] + 1
                q.append(nb)

    # For each depth level, compute min u value
    max_depth = int(np.max(depth[core_mask])) if np.any(core_mask) else 0
    depth_stats = {}
    for d in range(1, max_depth + 1):
        mask = core_mask & (depth == d)
        if np.any(mask):
            depth_stats[d] = {
                'count': int(np.sum(mask)),
                'min_u': float(np.min(u[mask])),
                'max_u': float(np.max(u[mask])),
                'mean_u': float(np.mean(u[mask])),
                'gap': float(np.min(u[mask]) - theta),
            }

    return depth_stats


def main():
    print("=" * 80)
    print("EXPERIMENT 21: Structural Analysis of T-Persist-1 Gaps 4/5/6")
    print("=" * 80)

    results = {}

    for n_grid in [8, 10, 12]:
        for beta in [20, 50, 100]:
            print(f"\n{'='*60}")
            print(f"Grid: {n_grid}x{n_grid}, β={beta}")
            print(f"{'='*60}")

            g = GraphState.grid_2d(n_grid, n_grid)
            p = make_params(beta_bd=beta)
            ec = EnergyComputer(g, p)
            ec.normalize_weights()

            res = find_formation(g, p)
            u = res.u

            print(f"  Energy: {res.energy:.4f}, Converged: {res.converged}")
            print(f"  Diagnostics: {res.diagnostics}")

            # --- Gap 4: Saddle-point eigenvector analysis ---
            print(f"\n  --- Gap 4: Saddle-Point Analysis ---")
            saddle_info = analyze_saddle_eigenvectors(u, g, ec, n_grid)
            if saddle_info:
                print(f"  μ (min eigenvalue): {saddle_info['mu']:.6f}")
                print(f"  Free variables: {saddle_info['n_free']}")
                print(f"  Core nodes: {saddle_info['n_core']}")
                print(f"  Soft mode on core: {saddle_info['core_frac']:.3f}")
                print(f"  Soft mode on boundary: {saddle_info['boundary_frac']:.3f}")
                print(f"  Top-5 node depths: {saddle_info['top_5_depths']}")
                print(f"  First 5 eigenvalues: {saddle_info['eigvals_first5']}")

            # --- Gap 5: Fingerprint Jacobian ---
            print(f"\n  --- Gap 5: Fingerprint Jacobian ---")
            if n_grid <= 10:  # expensive for large grids
                sigma_phi = compute_fingerprint_jacobian(u, g, p)
                print(f"  ||∂φ/∂u||_op ≈ {sigma_phi:.4f}")
                print(f"  (Current estimate used in theory: 3.0)")

            # --- Gap 6: Interior gap vs depth ---
            print(f"\n  --- Gap 6: Interior Gap vs Core Depth ---")
            depth_stats = analyze_interior_gap(u, g, n_grid)
            for d, stats in sorted(depth_stats.items()):
                print(f"  depth={d}: count={stats['count']}, "
                      f"min_u={stats['min_u']:.8f}, gap={stats['gap']:.8f}")

            # Check theoretical prediction
            alpha = p.alpha_bd
            kappa_sq = beta / (2 * alpha)
            d_min = 4  # square grid
            c0 = np.arccosh(1 + kappa_sq / d_min)
            print(f"\n  Theoretical: κ²={kappa_sq:.1f}, c₀={c0:.4f}")
            for d in sorted(depth_stats.keys()):
                predicted_gap = 0.1 - np.exp(-c0 * d)
                actual_gap = depth_stats[d]['gap']
                print(f"  depth={d}: predicted_gap≥{predicted_gap:.8f}, "
                      f"actual={actual_gap:.8f}, "
                      f"{'✓' if actual_gap >= predicted_gap else '✗'}")

            results[(n_grid, beta)] = {
                'saddle': saddle_info,
                'depth': depth_stats,
            }

    # --- Summary ---
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print("\n1. ESCAPE PATH ANALYSIS (Gap 4):")
    print("   Key question: Does the soft mode concentrate on core or boundary?")
    for (ng, beta), r in results.items():
        if r['saddle']:
            s = r['saddle']
            print(f"   {ng}x{ng} β={beta}: core_frac={s['core_frac']:.3f}, "
                  f"boundary_frac={s['boundary_frac']:.3f}, μ={s['mu']:.4f}")

    print("\n2. CORE DEPTH (Gap 6):")
    print("   Key question: Is δ_min ≥ 2 universal?")
    for (ng, beta), r in results.items():
        if r['depth']:
            max_depth = max(r['depth'].keys())
            has_depth2 = 2 in r['depth']
            print(f"   {ng}x{ng} β={beta}: max_depth={max_depth}, "
                  f"has_depth≥2={has_depth2}")


if __name__ == '__main__':
    main()
