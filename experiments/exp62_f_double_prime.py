"""Exp62: Compute F''(M/2) — curvature of reduced energy on mass-transfer manifold.

F(m) = min_{u in Sigma_m} E_self(u)  with FIXED normalization weights.

The sign of F''(M/2) determines whether the symmetric K=2 state is:
  F'' > 0 → local minimum on M_2 (merge has barrier)
  F'' < 0 → saddle on M_2 (merge spontaneous along mass-transfer)

Two approaches:
  1. Mass sweep: compute E_self(u*_m) for many m, fit quadratic at M/2
  2. Chemical potential: mu(m) = mean gradient at optimum, check d(mu)/dm sign

Key fix from 04-06: normalize_weights must be FIXED at reference c,
not recomputed at each mass. Otherwise F(m) uses a different functional at each m.
"""

import numpy as np
import json
import sys
sys.path.insert(0, '/home/jack/ex')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer, energy_bd, energy_cl, energy_sep, grad_bd, grad_cl, grad_sep
from scc.optimizer import project_volume


def optimize_at_mass(graph, params, ec, m, n_restarts=5, max_iter=2000, tol=1e-7):
    """Find formation at mass m using the GIVEN ec (fixed normalization)."""
    n = graph.n
    best_u = None
    best_E = float('inf')
    best_mu = None

    for seed in range(n_restarts):
        rng = np.random.RandomState(seed + 1000)
        c_local = m / n

        # Initialize
        if seed == 0:
            try:
                v2 = graph.fiedler_vector()
                v2 = v2 / (np.linalg.norm(v2) + 1e-12)
                u = np.full(n, c_local) + 0.01 * v2
            except Exception:
                u = np.full(n, c_local) + 0.01 * rng.randn(n)
        else:
            u = np.full(n, c_local) + 0.01 * rng.randn(n)
        u = project_volume(u, m)

        dt = 0.1
        E_old, _ = ec.energy(u)

        for it in range(1, max_iter + 1):
            g = ec.gradient(u)
            g_sigma = g - np.mean(g)
            gnorm = np.linalg.norm(g_sigma) / np.sqrt(n)
            if gnorm < tol:
                break

            u_new = u - dt * g_sigma
            u_new = project_volume(u_new, m)
            E_new, _ = ec.energy(u_new)

            if E_new > E_old and it > 5:
                dt *= 0.5
                if dt < 1e-10:
                    break
                continue

            # BB step
            du = u_new - u
            dg = ec.gradient(u_new) - g
            dg_sigma = dg - np.mean(dg)
            dot_ss = float(du @ du)
            dot_sy = float(du @ dg_sigma)
            if dot_sy > 1e-15:
                dt = min(dot_ss / dot_sy, 10.0)

            u = u_new
            E_old = E_new

        # Chemical potential = mean of gradient at optimum (Lagrange multiplier)
        g_final = ec.gradient(u)
        interior = (u > 1e-6) & (u < 1 - 1e-6)
        if np.sum(interior) > 0:
            mu = float(np.mean(g_final[interior]))
        else:
            mu = float(np.mean(g_final))

        E_final, _ = ec.energy(u)
        if E_final < best_E:
            best_E = E_final
            best_u = u.copy()
            best_mu = mu

    return best_u, best_E, best_mu


def run_experiment(grid_size=20, c_ref=0.3, n_mass_points=25):
    """Sweep mass and compute F(m), mu(m), F''(M/2)."""
    n = grid_size * grid_size
    M = c_ref * n  # total mass

    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry()

    # Fix normalization at reference c
    ec = EnergyComputer(graph, params)
    norms = ec.normalize_weights(c=c_ref)
    print(f"Grid: {grid_size}x{grid_size}, n={n}, M={M}, c_ref={c_ref}")
    print(f"Fixed normalization: λ_cl={ec.lambda_cl:.4f}, λ_sep={ec.lambda_sep:.4f}, λ_bd={ec.lambda_bd:.4f}")
    print(f"Spectral norms: {norms}")

    # Mass range: each formation must stay in spinodal (0.2113 < m/n < 0.7887)
    m_center = M / 2
    m_spin_lo = n * 0.22  # just above spinodal lower bound
    m_spin_hi = n * 0.78  # just below spinodal upper bound
    # Sweep ±30% around M/2, clamped to spinodal
    m_lo = max(m_center * 0.7, m_spin_lo)
    m_hi = min(m_center * 1.3, m_spin_hi)

    masses = np.linspace(m_lo, m_hi, n_mass_points)
    energies = []
    mus = []

    print(f"\nSweeping mass from {m_lo:.1f} to {m_hi:.1f} (center={m_center:.1f})")
    print(f"{'m':>8} {'c=m/n':>8} {'E_self':>12} {'mu':>12}")
    print("-" * 44)

    for m in masses:
        u_opt, E_opt, mu_opt = optimize_at_mass(graph, params, ec, m)
        energies.append(E_opt)
        mus.append(mu_opt)
        print(f"{m:8.2f} {m/n:8.4f} {E_opt:12.6f} {mu_opt:12.6f}")

    masses = np.array(masses)
    energies = np.array(energies)
    mus = np.array(mus)

    # Compute F''(M/2) via finite differences
    # Find points closest to M/2
    idx_center = np.argmin(np.abs(masses - m_center))
    dm = masses[1] - masses[0]

    if idx_center > 0 and idx_center < len(masses) - 1:
        F_pp = (energies[idx_center + 1] - 2 * energies[idx_center] + energies[idx_center - 1]) / dm**2
    else:
        F_pp = float('nan')

    # Also fit quadratic near center
    # Use 5 points around center
    i_lo = max(0, idx_center - 2)
    i_hi = min(len(masses), idx_center + 3)
    m_local = masses[i_lo:i_hi]
    E_local = energies[i_lo:i_hi]
    if len(m_local) >= 3:
        coeffs = np.polyfit(m_local - m_center, E_local, 2)
        F_pp_fit = 2 * coeffs[0]
    else:
        F_pp_fit = float('nan')

    # Chemical potential slope: dmu/dm
    if idx_center > 0 and idx_center < len(masses) - 1:
        dmu_dm = (mus[idx_center + 1] - mus[idx_center - 1]) / (2 * dm)
    else:
        dmu_dm = float('nan')

    print(f"\n{'='*50}")
    print(f"RESULTS at M/2 = {m_center:.2f}")
    print(f"  F''(M/2) [FD]:   {F_pp:.6e}")
    print(f"  F''(M/2) [fit]:  {F_pp_fit:.6e}")
    print(f"  dmu/dm at M/2:   {dmu_dm:.6e}")
    print()
    if F_pp > 0:
        print("  >>> F'' > 0: K=2 symmetric point is LOCAL MINIMUM on M_2")
        print("  >>> Merge requires overcoming a barrier")
    elif F_pp < 0:
        print("  >>> F'' < 0: K=2 symmetric point is SADDLE on M_2")
        print("  >>> Merge is spontaneous along mass-transfer direction")
    else:
        print("  >>> F'' ≈ 0: marginal case")

    # Also test on a larger grid for scaling
    results = {
        'grid_size': grid_size,
        'n': n,
        'M': float(M),
        'c_ref': c_ref,
        'lambda_cl': float(ec.lambda_cl),
        'lambda_sep': float(ec.lambda_sep),
        'lambda_bd': float(ec.lambda_bd),
        'masses': masses.tolist(),
        'energies': energies.tolist(),
        'chemical_potentials': mus.tolist(),
        'F_pp_fd': float(F_pp),
        'F_pp_fit': float(F_pp_fit),
        'dmu_dm': float(dmu_dm),
    }
    return results


def run_multi_grid():
    """Run on multiple grid sizes and c_ref values.

    c_ref must be large enough that M/2 per formation is still in spinodal:
    c_half = c_ref/2 > 0.2113 → c_ref > 0.4226.
    Use c_ref in {0.5, 0.6, 0.7} so both halves are well within spinodal.
    """
    all_results = {}
    for gs in [15, 20]:
        for c_ref in [0.5, 0.6, 0.7]:
            key = f'{gs}x{gs}_c{c_ref}'
            print(f"\n{'#'*60}")
            print(f"# Grid {gs}x{gs}, c_ref={c_ref}")
            print(f"{'#'*60}")
            results = run_experiment(grid_size=gs, c_ref=c_ref, n_mass_points=21)
            all_results[key] = results

    # Save results
    with open('/home/jack/ex/experiments/results/exp62_f_double_prime.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to experiments/results/exp62_f_double_prime.json")

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY: F''(M/2) across grid sizes and c_ref values")
    print(f"{'Key':>14} {'n':>6} {'M':>8} {'c_half':>8} {'F_pp_FD':>12} {'F_pp_fit':>12} {'dmu/dm':>12}")
    print("-" * 70)
    for gs in [15, 20]:
        for c_ref in [0.5, 0.6, 0.7]:
            key = f'{gs}x{gs}_c{c_ref}'
            r = all_results[key]
            c_half = c_ref / 2
            print(f"{key:>14} {r['n']:>6} {r['M']:>8.1f} {c_half:>8.3f} {r['F_pp_fd']:>12.6e} {r['F_pp_fit']:>12.6e} {r['dmu_dm']:>12.6e}")


if __name__ == '__main__':
    run_multi_grid()
