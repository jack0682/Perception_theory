"""Experiment 22: Measure actual energy barrier along soft mode.

Following Cycle 1 discovery that the soft mode concentrates on boundary nodes,
we trace the energy landscape along the soft mode to find the actual saddle
energy and compare with the r≥0.210 estimate.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.optimizer import project_volume

np.set_printoptions(precision=8, linewidth=120)

def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p


def compute_soft_mode(u, graph, ec):
    """Compute the softest eigenvector of the constrained Hessian on free variables."""
    n = len(u)
    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)

    if n_f < 3:
        return None, None, None

    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]

    H = 0.5 * (H + H.T)

    # Project onto Σ_m tangent space
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P

    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10

    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]

    # Expand softest mode to full space
    soft_mode = np.zeros(n)
    soft_mode[free_idx] = eigvecs[:, 0]
    # Project to tangent space of Σ_m
    soft_mode -= np.mean(soft_mode)
    norm = np.linalg.norm(soft_mode)
    if norm > 1e-15:
        soft_mode /= norm

    return eigvals[0], soft_mode, free_idx


def trace_energy_along_direction(u, direction, ec, m, max_t=5.0, n_points=500):
    """Trace E(project(u + t*direction)) for t in [-max_t, max_t]."""
    ts = np.linspace(-max_t, max_t, n_points)
    energies = np.zeros(n_points)
    for i, t in enumerate(ts):
        u_perturbed = u + t * direction
        u_proj = project_volume(np.clip(u_perturbed, 0, 1), m)
        E, _ = ec.energy(u_proj)
        energies[i] = E
    return ts, energies


def find_saddle_energy(ts, energies, E_min):
    """Find the energy barrier = max energy along direction minus minimum."""
    # The saddle is a local max in energy along the escape direction
    # Starting from the minimum at t≈0, find the first local max on each side
    center = len(ts) // 2
    E0 = energies[center]

    barriers = []
    # Forward
    for i in range(center + 1, len(ts)):
        if i > center + 2 and energies[i] < energies[i-1]:
            barriers.append(energies[i-1] - E0)
            break
    else:
        barriers.append(energies[-1] - E0)

    # Backward
    for i in range(center - 1, -1, -1):
        if i < center - 2 and energies[i] < energies[i+1]:
            barriers.append(energies[i+1] - E0)
            break
    else:
        barriers.append(energies[0] - E0)

    return min(barriers) if barriers else 0.0


def main():
    print("=" * 80)
    print("EXPERIMENT 22: Actual Energy Barrier Along Soft Mode")
    print("=" * 80)

    configs = [
        (8, 20), (8, 50), (8, 100),
        (10, 20), (10, 50), (10, 100),
        (12, 50), (12, 100),
    ]

    print(f"\n{'Grid':<8} {'β':<6} {'μ':<10} {'Δ_soft':<12} {'Δ_core(0.0441β)':<16} "
          f"{'r_soft':<10} {'r_core(0.210)':<14} {'Ratio':<8}")
    print("-" * 90)

    for n_grid, beta in configs:
        g = GraphState.grid_2d(n_grid, n_grid)
        p = make_params(beta_bd=beta)
        ec = EnergyComputer(g, p)
        ec.normalize_weights()

        res = find_formation(g, p)
        u = res.u
        m = p.volume_fraction * g.n

        mu, soft_mode, free_idx = compute_soft_mode(u, g, ec)
        if soft_mode is None:
            continue

        # Trace energy along soft mode
        ts, energies = trace_energy_along_direction(u, soft_mode, ec, m, max_t=3.0, n_points=1000)
        E_min = res.energy
        delta_soft = find_saddle_energy(ts, energies, E_min)

        # Compute λ_max for r = sqrt(2Δ/λ_max)
        # Approximate λ_max from Hessian
        n = len(u)
        tol = 1e-6
        free_mask = (u > tol) & (u < 1 - tol)
        free_idx_arr = np.where(free_mask)[0]
        n_f = len(free_idx_arr)

        h = 1e-5
        g0 = ec.gradient(u)
        H = np.zeros((n_f, n_f))
        for j in range(n_f):
            e_j = np.zeros(n)
            e_j[free_idx_arr[j]] = h
            g1 = ec.gradient(u + e_j)
            H[:, j] = ((g1 - g0) / h)[free_idx_arr]
        H = 0.5 * (H + H.T)
        lam_max = np.max(np.linalg.eigvalsh(H))

        delta_core = 0.0441 * beta * ec.lambda_bd  # scaled by weight
        r_soft = np.sqrt(2 * delta_soft / lam_max) if delta_soft > 0 else 0
        r_core = 0.210  # theoretical

        ratio = r_soft / r_core if r_core > 0 else float('inf')

        print(f"{n_grid}x{n_grid:<4} {beta:<6} {mu:<10.4f} {delta_soft:<12.6f} "
              f"{delta_core:<16.6f} {r_soft:<10.4f} {r_core:<14.4f} {ratio:<8.3f}")

    # Also trace multiple directions (soft mode + 2nd softest + random)
    print("\n\nDETAILED TRACE: 10x10, β=50")
    print("-" * 60)
    g = GraphState.grid_2d(10, 10)
    p = make_params(beta_bd=50)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()
    res = find_formation(g, p)
    u = res.u
    m = p.volume_fraction * g.n

    n = len(u)
    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx_arr = np.where(free_mask)[0]
    n_f = len(free_idx_arr)

    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx_arr[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx_arr]
    H = 0.5 * (H + H.T)
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10
    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]

    for k, label in [(0, "softest"), (1, "2nd softest"), (2, "3rd softest")]:
        mode = np.zeros(n)
        mode[free_idx_arr] = eigvecs[:, k]
        mode -= np.mean(mode)
        mode /= np.linalg.norm(mode)

        ts, energies = trace_energy_along_direction(u, mode, ec, m, max_t=3.0, n_points=500)
        barrier = find_saddle_energy(ts, energies, res.energy)

        # Core fraction
        theta = 0.9
        core_mask = u >= theta
        core_frac = np.sum(mode[core_mask]**2)

        print(f"  Mode {k} ({label}): barrier={barrier:.6f}, "
              f"core_frac={core_frac:.3f}, eigenvalue={eigvals[k]:.4f}")

    # Try a pure core perturbation direction
    core_mask = u >= 0.9
    core_dir = np.zeros(n)
    core_nodes = np.where(core_mask)[0]
    if len(core_nodes) > 0:
        # Perturbation that moves one core node down, compensated by mean shift
        core_dir[core_nodes[0]] = -1.0
        core_dir -= np.mean(core_dir)
        core_dir /= np.linalg.norm(core_dir)

        ts, energies = trace_energy_along_direction(u, core_dir, ec, m, max_t=1.0, n_points=500)
        barrier_core = find_saddle_energy(ts, energies, res.energy)
        print(f"\n  Pure core perturbation: barrier={barrier_core:.6f}")
        print(f"  (This is what r≥0.210 estimates)")

    print(f"\n  For reference: 0.0441*β*λ_bd = {0.0441*50*ec.lambda_bd:.6f}")


if __name__ == '__main__':
    main()
