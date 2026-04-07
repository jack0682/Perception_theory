"""Exp63: Direct Hessian test in mass-transfer direction at K=2 minimum.

Instead of sweeping mass (noisy due to optimizer), directly compute:
  d²E_K/dε² along the mass-transfer direction at the K=2 minimum.

At K=2 minimum (u₁*, u₂*) on Σ_{M/2} × Σ_{M/2}, the mass-transfer
perturbation transfers δm from formation 2 to formation 1:
  u₁ → u₁ + ε·v₁   (with Σv₁ᵢ = 1)
  u₂ → u₂ - ε·v₂   (with Σv₂ᵢ = 1)

where v₁, v₂ are the optimal response directions (minimize ∂²E/∂ε²).

Method: finite difference on the total K-field energy.
  E(ε) = E_self(u₁ + ε·v₁) + E_self(u₂ - ε·v₂) + λ_rep⟨u₁+ε·v₁, u₂-ε·v₂⟩

For simplicity, use v_k = (1/n)·1 (uniform mass transfer) as a first test,
then also try the optimal response (re-optimize at each ε).
"""

import numpy as np
import json
import sys
sys.path.insert(0, '/home/jack/ex')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.multi import find_k_formations
from scc.optimizer import project_volume


def compute_chemical_potential(ec, u):
    """Compute Lagrange multiplier μ = mean of gradient at interior points."""
    g = ec.gradient(u)
    interior = (u > 1e-6) & (u < 1 - 1e-6)
    if np.sum(interior) > 0:
        return float(np.mean(g[interior]))
    return float(np.mean(g))


def run_hessian_test(grid_size=20, c_ref=0.5):
    """Compute F'' via finite differences at K=2 minimum."""
    n = grid_size * grid_size
    M = c_ref * n
    m_half = M / 2
    c_half = m_half / n

    print(f"Grid: {grid_size}x{grid_size}, n={n}, M={M:.1f}, c_half={c_half:.4f}")

    # Check spinodal
    if c_half < 0.2113 or c_half > 0.7887:
        print(f"WARNING: c_half={c_half:.4f} outside spinodal!")
        return None

    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(volume_fraction=c_half)

    # Find K=2 formations (returns list of FormationResult)
    print("Finding K=2 formations...")
    results = find_k_formations(graph, params, K=2, n_restarts=8)
    u1 = results[0].u
    u2 = results[1].u
    E_K2 = results[0].energy + results[1].energy

    m1 = np.sum(u1)
    m2 = np.sum(u2)
    overlap = float(u1 @ u2)
    print(f"K=2 result: E={E_K2:.6f}, m1={m1:.2f}, m2={m2:.2f}, overlap={overlap:.4f}")

    # Setup energy computer with fixed normalization
    ec = EnergyComputer(graph, params)
    ec.normalize_weights(c=c_half)

    # Chemical potentials at K=2
    mu1 = compute_chemical_potential(ec, u1)
    mu2 = compute_chemical_potential(ec, u2)
    print(f"Chemical potentials: μ₁={mu1:.6f}, μ₂={mu2:.6f}, Δμ={mu1-mu2:.6e}")

    # --- Method 1: Uniform mass transfer ---
    print(f"\n--- Method 1: Uniform transfer (v = 1/n) ---")
    v_uniform = np.ones(n) / n  # transfer direction: Σv = 1

    epsilons = np.array([-2, -1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.5, 1, 2])
    energies_uniform = []
    for eps in epsilons:
        u1_pert = project_volume(u1 + eps * v_uniform, m_half + eps)
        u2_pert = project_volume(u2 - eps * v_uniform, m_half - eps)
        # Compute total K-field energy
        E1, _ = ec.energy(u1_pert)
        E2, _ = ec.energy(u2_pert)
        E_rep = 10.0 * float(u1_pert @ u2_pert)  # default lambda_rep=10
        E_tot = E1 + E2 + E_rep
        energies_uniform.append(E_tot)
        idx = len(energies_uniform) - 1
        E0_ref = energies_uniform[5] if len(energies_uniform) > 5 else energies_uniform[0]
        print(f"  ε={eps:+6.2f}  E={E_tot:.6f}  ΔE={E_tot - E0_ref:.6e}")

    # FD at ε=0 (index 5)
    E = np.array(energies_uniform)
    h = 0.1
    idx0 = 5  # ε=0
    F_pp_uniform = (E[6] - 2*E[5] + E[4]) / h**2  # using ε=±0.1
    print(f"  F'' (h=0.1): {F_pp_uniform:.6e}")
    F_pp_uniform2 = (E[7] - 2*E[5] + E[3]) / 0.2**2  # using ε=±0.2
    print(f"  F'' (h=0.2): {F_pp_uniform2:.6e}")

    # --- Method 2: Re-optimize at each ε (the true F(m)) ---
    print(f"\n--- Method 2: Re-optimize at each ε ---")
    from scc.optimizer import find_formation

    eps_reopt = np.array([-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3])
    energies_reopt = []
    mus_reopt = []

    for eps in eps_reopt:
        m_new = m_half + eps
        c_new = m_new / n
        if c_new < 0.2113 or c_new > 0.7887:
            print(f"  ε={eps:+6.2f}  SKIP (c={c_new:.4f} outside spinodal)")
            energies_reopt.append(float('nan'))
            mus_reopt.append(float('nan'))
            continue

        # Use FIXED ec (normalization at c_half), optimize at mass m_new
        params_local = ParameterRegistry(volume_fraction=c_new)
        result_local = find_formation(graph, params_local)
        u_opt = result_local.u
        # Evaluate with FIXED normalization
        E_opt, _ = ec.energy(u_opt)
        mu_opt = compute_chemical_potential(ec, u_opt)
        energies_reopt.append(E_opt)
        mus_reopt.append(mu_opt)
        print(f"  ε={eps:+6.2f}  m={m_new:.1f}  c={c_new:.4f}  E={E_opt:.6f}  μ={mu_opt:.6f}  Bind={result_local.diagnostics.bind:.3f}")

    E_reopt = np.array(energies_reopt)
    mu_reopt = np.array(mus_reopt)

    # F'' from re-optimized curve
    # ε = [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]
    #       0    1   2    3   4   5   6  7  8
    if not np.isnan(E_reopt[3]) and not np.isnan(E_reopt[5]):
        F_pp_reopt_05 = (E_reopt[5] - 2*E_reopt[4] + E_reopt[3]) / 0.5**2
        print(f"\n  F'' (re-opt, h=0.5): {F_pp_reopt_05:.6e}")
    if not np.isnan(E_reopt[2]) and not np.isnan(E_reopt[6]):
        F_pp_reopt_1 = (E_reopt[6] - 2*E_reopt[4] + E_reopt[2]) / 1.0**2
        print(f"  F'' (re-opt, h=1.0): {F_pp_reopt_1:.6e}")
    if not np.isnan(E_reopt[1]) and not np.isnan(E_reopt[7]):
        F_pp_reopt_2 = (E_reopt[7] - 2*E_reopt[4] + E_reopt[1]) / 2.0**2
        print(f"  F'' (re-opt, h=2.0): {F_pp_reopt_2:.6e}")

    # Chemical potential derivative
    if not np.isnan(mu_reopt[2]) and not np.isnan(mu_reopt[6]):
        dmu_dm = (mu_reopt[6] - mu_reopt[2]) / 2.0
        print(f"  dμ/dm (h=1.0): {dmu_dm:.6e}")

    # --- Summary ---
    print(f"\n{'='*60}")
    print(f"SUMMARY for {grid_size}x{grid_size}, c_ref={c_ref}")
    print(f"  K=2 energy: {E_K2:.6f}")
    print(f"  Chemical potential gap: Δμ = {mu1-mu2:.6e}")
    print(f"  F'' (uniform transfer): {F_pp_uniform:.6e}")
    if not np.isnan(E_reopt[2]) and not np.isnan(E_reopt[6]):
        print(f"  F'' (re-optimized, h=1): {F_pp_reopt_1:.6e}")

    sign = "POSITIVE (local min, barrier)" if F_pp_uniform > 0 else "NEGATIVE (saddle, spontaneous merge)"
    print(f"  Verdict: F'' is {sign}")

    return {
        'grid_size': grid_size,
        'c_ref': c_ref,
        'c_half': c_half,
        'E_K2': float(E_K2),
        'mu1': float(mu1),
        'mu2': float(mu2),
        'delta_mu': float(mu1 - mu2),
        'F_pp_uniform': float(F_pp_uniform),
        'epsilons_reopt': eps_reopt.tolist(),
        'energies_reopt': [float(e) if not np.isnan(e) else None for e in E_reopt],
    }


if __name__ == '__main__':
    all_results = {}
    for gs in [15, 20]:
        for c_ref in [0.5, 0.6]:
            key = f'{gs}x{gs}_c{c_ref}'
            print(f"\n{'#'*60}")
            print(f"# {key}")
            print(f"{'#'*60}")
            r = run_hessian_test(grid_size=gs, c_ref=c_ref)
            if r is not None:
                all_results[key] = r

    with open('/home/jack/ex/experiments/results/exp63_hessian_mass_transfer.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to experiments/results/exp63_hessian_mass_transfer.json")
