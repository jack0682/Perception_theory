"""Experiment 23: Barrier vs spectral gap — testing Δ_soft ~ μ² relationship.

Tests whether the soft-mode barrier scales with μ², which would give
r_basin ~ μ/√λ_max — a μ-dependent bound replacing the claimed β-independent one.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.optimizer import project_volume

def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p

def compute_soft_mode_and_barrier(n_grid, beta):
    g = GraphState.grid_2d(n_grid, n_grid)
    p = make_params(beta_bd=beta)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()
    res = find_formation(g, p)
    u = res.u
    m = p.volume_fraction * g.n
    n = len(u)

    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)
    if n_f < 3:
        return None

    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]
    H = 0.5 * (H + H.T)

    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10
    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]

    mu = eigvals[0]
    lam_max = np.max(np.linalg.eigvalsh(H))

    soft_mode = np.zeros(n)
    soft_mode[free_idx] = eigvecs[:, 0]
    soft_mode -= np.mean(soft_mode)
    norm = np.linalg.norm(soft_mode)
    if norm > 1e-15:
        soft_mode /= norm

    # Trace energy along soft mode
    ts = np.linspace(-3.0, 3.0, 1000)
    energies = []
    for t in ts:
        u_p = project_volume(np.clip(u + t * soft_mode, 0, 1), m)
        E, _ = ec.energy(u_p)
        energies.append(E)
    energies = np.array(energies)
    E0 = res.energy

    # Find barrier
    center = len(ts) // 2
    barriers = []
    for direction in [1, -1]:
        start = center
        for i in range(1, len(ts)//2):
            idx = center + direction * i
            if 0 <= idx < len(ts) and idx - direction >= 0 and idx - direction < len(ts):
                if energies[idx] < energies[idx - direction] and i > 5:
                    barriers.append(energies[idx - direction] - E0)
                    break
        else:
            # No local max found — use endpoint
            idx = center + direction * (len(ts)//2 - 1)
            if 0 <= idx < len(ts):
                barriers.append(energies[idx] - E0)

    delta_soft = min(barriers) if barriers else 0.0
    r_soft = np.sqrt(2 * max(delta_soft, 0) / lam_max) if lam_max > 0 else 0

    # Also compute L3 (3rd derivative in soft mode direction) via FD
    # E''(0) = μ (by definition)
    # E(t) ≈ E0 + μ/2 t² + L3/6 t³ + L4/24 t⁴
    dt = 0.01
    E_plus = energies[center + int(dt / (ts[1]-ts[0]))]
    E_minus = energies[center - int(dt / (ts[1]-ts[0]))]
    E_2plus = energies[center + 2*int(dt / (ts[1]-ts[0]))]
    E_2minus = energies[center - 2*int(dt / (ts[1]-ts[0]))]

    # FD estimates
    E2 = (E_plus - 2*E0 + E_minus) / dt**2  # ≈ E''(0) = curvature along soft mode
    E3 = (E_2plus - 2*E_plus + 2*E_minus - E_2minus) / (2*dt**3)  # ≈ E'''(0)

    # Perturbation budget
    pert_budget = 0.07  # typical 2ε₂ + 2ε₁/μ

    return {
        'mu': mu, 'lam_max': lam_max, 'delta_soft': delta_soft,
        'r_soft': r_soft, 'E2': E2, 'E3': E3, 'n_f': n_f,
        'eigvals_5': eigvals[:5].tolist(),
        'safe': r_soft > pert_budget,
    }


def main():
    print("=" * 100)
    print("EXPERIMENT 23: Barrier vs Spectral Gap — Testing Δ ~ μ² Scaling")
    print("=" * 100)

    configs = []
    for n_grid in [8, 10, 12, 15]:
        for beta in [10, 20, 30, 50, 70, 100, 150, 200]:
            configs.append((n_grid, beta))

    print(f"\n{'Grid':<8} {'β':<6} {'μ':<10} {'λ_max':<10} {'Δ_soft':<12} "
          f"{'r_soft':<10} {'Δ/μ²':<10} {'E2':<10} {'E3':<12} {'Safe?':<6}")
    print("-" * 104)

    mus = []
    deltas = []
    r_softs = []

    for n_grid, beta in configs:
        try:
            r = compute_soft_mode_and_barrier(n_grid, beta)
            if r is None:
                continue
            ratio = r['delta_soft'] / r['mu']**2 if r['mu'] > 1e-10 else float('inf')
            print(f"{n_grid}x{n_grid:<4} {beta:<6} {r['mu']:<10.4f} {r['lam_max']:<10.4f} "
                  f"{r['delta_soft']:<12.6f} {r['r_soft']:<10.4f} {ratio:<10.4f} "
                  f"{r['E2']:<10.4f} {r['E3']:<12.4f} {'✓' if r['safe'] else '✗'}")
            mus.append(r['mu'])
            deltas.append(r['delta_soft'])
            r_softs.append(r['r_soft'])
        except Exception as e:
            print(f"{n_grid}x{n_grid:<4} {beta:<6} ERROR: {e}")

    # Regression: Δ ~ a * μ^b
    if len(mus) > 5:
        mus = np.array(mus)
        deltas = np.array(deltas)
        r_softs = np.array(r_softs)

        # Filter out zeros
        valid = deltas > 1e-8
        if np.sum(valid) > 3:
            log_mu = np.log(mus[valid])
            log_delta = np.log(deltas[valid])
            # Linear regression: log(Δ) = a + b*log(μ)
            A = np.vstack([np.ones_like(log_mu), log_mu]).T
            coeffs = np.linalg.lstsq(A, log_delta, rcond=None)[0]
            print(f"\n  Regression: Δ_soft ~ {np.exp(coeffs[0]):.4f} * μ^{coeffs[1]:.2f}")
            print(f"  (If b ≈ 2, then Δ ~ C*μ² confirming quadratic scaling)")

        # r_soft vs μ
        valid_r = r_softs > 1e-8
        if np.sum(valid_r) > 3:
            log_mu_r = np.log(mus[valid_r])
            log_r = np.log(r_softs[valid_r])
            A = np.vstack([np.ones_like(log_mu_r), log_mu_r]).T
            coeffs_r = np.linalg.lstsq(A, log_r, rcond=None)[0]
            print(f"  Regression: r_soft ~ {np.exp(coeffs_r[0]):.4f} * μ^{coeffs_r[1]:.2f}")

    # Critical finding summary
    print("\n  CRITICAL FINDINGS:")
    unsafe_count = sum(1 for r in r_softs if r < 0.07)
    print(f"  Configurations where r_soft < 0.07 (typical pert budget): {unsafe_count}/{len(r_softs)}")
    print(f"  Minimum r_soft observed: {min(r_softs):.4f}" if r_softs.size > 0 else "  No data")
    print(f"  r_soft < 0.210 in {sum(1 for r in r_softs if r < 0.210)}/{len(r_softs)} configs")


if __name__ == '__main__':
    main()
