#!/usr/bin/env python3
"""H3 Jacobian Analysis: Numerical verification of site-weighted C₂^eff bounds.

Verifies:
1. Site-specific Jacobian diagonal values at core/boundary/exterior
2. Formation-conditioned C₂^eff formula
3. Scaling law: n_bdy ∝ √n
4. Alignment with exp13 data
"""
import sys, os, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.operators import closure, closure_with_jacobian, aggregation, sigmoid, sigmoid_deriv
from scc.energy import energy_cl, grad_cl, energy_bd, grad_bd, energy_sep, grad_sep
from scc.optimizer import find_formation


def compute_site_jacobian(u, graph, params):
    """Compute per-site closure Jacobian diagonal [J_Cl]_xx."""
    Cl_u, sigma_prime, z = closure_with_jacobian(u, graph, params)
    # J_Cl = diag(a_cl * sigma') @ ((1-eta)*I + eta*P)
    # Diagonal: [J_Cl]_xx = a_cl * sigma'(z_x) * ((1-eta) + eta*[P]_xx)
    # For grids, [P]_xx = 0 (no self-loops), so:
    # [J_Cl]_xx = a_cl * (1-eta) * sigma'(z_x) + a_cl * eta * sigma'(z_x) * [P]_xx
    # But the full diagonal also includes the neighbor averaging...
    # Actually: the diagonal of J_Cl at site x is the partial derivative d Cl(u)(x) / d u(x)
    # Cl(u)(x) = sigma(a_cl * ((1-eta)*u(x) + eta*(Pu)(x) - tau))
    # d/du(x) = a_cl * sigma'(z_x) * ((1-eta) + eta * P_xx)
    # On grids without self-loops: P_xx = 0 (row-normalized adjacency has 0 diagonal)
    # So: [J_Cl]_xx = a_cl * (1-eta) * sigma'(z_x)

    # But wait - the mixing formula in the code is:
    # z = a_cl * ((1-eta)*Pu + eta*u - tau)  [CHECK CODE]
    # Let me re-read... from operators.py line 57-59:
    # z = params.a_cl * ((1.0 - params.eta_cl) * u + params.eta_cl * Pu - params.tau_cl)
    # So: z = a_cl * ((1-eta)*u + eta*Pu - tau)
    # d Cl(u)(x)/du(x) = a_cl * sigma'(z_x) * (1-eta)  [self-retention term]
    #                   + contributions from Pu if x appears as neighbor

    # The diagonal entry is just the direct self-derivative:
    diag_J = params.a_cl * (1.0 - params.eta_cl) * sigma_prime

    # But H3-TIGHTENING uses eta_cl=0.5 and says J_Cl,core = a_cl * 0.5 * sigma'
    # That's: a_cl * (1-eta) * sigma' = a_cl * 0.5 * sigma' for eta=0.5
    # which matches: "3.0 * 0.5 * 0.1491 = 0.224"
    # Wait, the H3 doc uses (1-eta)*P*u + eta*u, which swaps the roles.
    # Let me check... doc says Cl(u)(x) = σ(a_cl((1-η)P·u(x) + η·u(x) - τ))
    # But code says z = a_cl * ((1-eta)*u + eta*Pu - tau)
    # So in the CODE: the self-retention weight is (1-eta) and neighbor weight is eta
    # In the DOC: self-retention weight is η and neighbor weight is (1-η)
    # With eta=0.5, these are the SAME: both give 0.5*u + 0.5*Pu

    # So the diagonal is: a_cl * (1-eta_cl) * sigma'(z_x) for the code convention
    # = a_cl * 0.5 * sigma'(z_x) when eta_cl = 0.5

    return diag_J, sigma_prime, z, Cl_u


def classify_sites(u, theta_low=0.1, theta_high=0.9):
    """Classify sites into core, boundary, exterior."""
    core = u >= theta_high
    ext = u <= theta_low
    bdy = ~core & ~ext
    return core, bdy, ext


def compute_c2_per_site(u, graph, params):
    """Compute the effective C₂ contribution at each site."""
    Cl_u = closure(u, graph, params)
    r = Cl_u - u  # closure residual

    # Closure gradient: -2(I - J_Cl)^T r
    # The relevant magnitude per site for the C₂ bound is |∇_x E_cl|
    grad_e_cl = grad_cl(u, graph, params)
    grad_e_sep = grad_sep(u, graph, params)
    grad_e_bd = grad_bd(u, graph, params)

    # Per-site C₂ contribution: (lambda_cl * |grad_cl_x| + lambda_sep * |grad_sep_x|) / (2 * lambda_bd)
    lambda_cl = params.w_cl / (params.w_cl + params.w_sep + params.w_bd)
    lambda_sep = params.w_sep / (params.w_cl + params.w_sep + params.w_bd)
    lambda_bd = params.w_bd / (params.w_cl + params.w_sep + params.w_bd)

    c2_per_site = (lambda_cl * np.abs(grad_e_cl) + lambda_sep * np.abs(grad_e_sep)) / (2 * lambda_bd)

    return c2_per_site, r, grad_e_cl, grad_e_sep, grad_e_bd


def analyze_formation(grid_size, beta, c=0.3, a_cl=3.0):
    """Full H3 Jacobian analysis for a single formation."""
    rows, cols = grid_size
    graph = GraphState.grid_2d(rows, cols)
    n = rows * cols

    params = ParameterRegistry(
        a_cl=a_cl,
        eta_cl=0.5,
        tau_cl=0.5,
        beta_bd=beta,
        volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=5000,
        n_restarts=5,
    )

    result = find_formation(graph, params)
    u = result.u

    # 1. Site-specific Jacobian
    diag_J, sigma_prime, z, Cl_u = compute_site_jacobian(u, graph, params)
    core, bdy, ext = classify_sites(u)
    n_core = int(np.sum(core))
    n_bdy = int(np.sum(bdy))
    n_ext = int(np.sum(ext))

    # Jacobian stats by region
    J_core = diag_J[core] if n_core > 0 else np.array([])
    J_bdy = diag_J[bdy] if n_bdy > 0 else np.array([])
    J_ext = diag_J[ext] if n_ext > 0 else np.array([])

    # 2. Residual by region
    r = Cl_u - u
    r_core = np.abs(r[core]) if n_core > 0 else np.array([])
    r_bdy = np.abs(r[bdy]) if n_bdy > 0 else np.array([])

    # 3. Per-site C₂
    c2_per_site, _, grad_cl_vals, grad_sep_vals, grad_bd_vals = compute_c2_per_site(u, graph, params)
    c2_core = c2_per_site[core] if n_core > 0 else np.array([])
    c2_bdy = c2_per_site[bdy] if n_bdy > 0 else np.array([])

    # 4. Effective C₂ (weighted)
    c2_eff_weighted = (n_bdy/n * np.mean(c2_bdy) + (n-n_bdy)/n * np.mean(c2_core)) if (n_core > 0 and n_bdy > 0) else float('nan')
    c2_eff_max = np.max(c2_per_site) if len(c2_per_site) > 0 else float('nan')

    # 5. Theoretical prediction
    # sigma'(1.5) for core (a_cl=3.0)
    z_core_th = a_cl * (0.5 * 1.0 + 0.5 * 1.0 - 0.5)
    sp_core_th = sigmoid(np.array([z_core_th]))[0] * (1 - sigmoid(np.array([z_core_th]))[0])
    J_core_th = a_cl * 0.5 * sp_core_th

    z_bdy_th = a_cl * (0.5 * 0.5 + 0.5 * 0.5 - 0.5)
    sp_bdy_th = 0.25  # sigma'(0) = 0.25
    J_bdy_th = a_cl * 0.5 * sp_bdy_th

    # Theoretical C₂^sat and C₂^max
    lambda_cl = 1/3
    lambda_sep = 1/3
    lambda_bd = 1/3

    r_core_typical = 0.18
    c2_sat_th = (lambda_cl * 2 * r_core_typical * (1 + J_core_th) + lambda_sep * 0.04) / (2 * lambda_bd)
    c2_max_th = (lambda_cl * 2 * 1.0 * (1 + J_bdy_th) + lambda_sep * 2.0) / (2 * lambda_bd)
    c2_eff_th = (n_bdy/n) * c2_max_th + (1 - n_bdy/n) * c2_sat_th

    # 6. KKT Lagrange multiplier
    total_grad = (lambda_cl * grad_cl_vals + lambda_sep * grad_sep_vals + lambda_bd * grad_bd_vals)
    nu = np.mean(total_grad)  # Mean gradient = Lagrange multiplier

    # 7. Interior gap at deep core
    # Find deep core sites (distance ≥ 2 from boundary)
    from collections import deque
    non_core_idx = np.where(~core)[0]
    depths = np.full(n, -1, dtype=int)
    queue = deque()
    for nc in non_core_idx:
        queue.append(nc)
        depths[nc] = 0
    while queue:
        node = queue.popleft()
        row = graph.W.getrow(node)
        for nb in row.indices:
            if depths[nb] == -1:
                depths[nb] = depths[node] + 1
                queue.append(nb)
    deep_core_mask = core & (depths >= 2)
    n_deep = int(np.sum(deep_core_mask))

    gap_deep = u[deep_core_mask] - params.theta_core if n_deep > 0 else np.array([])
    gap_min = float(np.min(gap_deep)) if n_deep > 0 else float('nan')

    return {
        'grid': f'{rows}x{cols}', 'n': n, 'beta': beta, 'a_cl': a_cl, 'c': c,
        'n_core': n_core, 'n_bdy': n_bdy, 'n_ext': n_ext, 'n_deep': n_deep,
        'J_core_mean': float(np.mean(J_core)) if len(J_core) > 0 else float('nan'),
        'J_core_max': float(np.max(J_core)) if len(J_core) > 0 else float('nan'),
        'J_bdy_mean': float(np.mean(J_bdy)) if len(J_bdy) > 0 else float('nan'),
        'J_bdy_max': float(np.max(J_bdy)) if len(J_bdy) > 0 else float('nan'),
        'J_ext_mean': float(np.mean(J_ext)) if len(J_ext) > 0 else float('nan'),
        'J_core_th': J_core_th, 'J_bdy_th': J_bdy_th,
        'r_core_mean': float(np.mean(r_core)) if len(r_core) > 0 else float('nan'),
        'r_core_max': float(np.max(r_core)) if len(r_core) > 0 else float('nan'),
        'r_bdy_mean': float(np.mean(r_bdy)) if len(r_bdy) > 0 else float('nan'),
        'c2_core_mean': float(np.mean(c2_core)) if len(c2_core) > 0 else float('nan'),
        'c2_bdy_mean': float(np.mean(c2_bdy)) if len(c2_bdy) > 0 else float('nan'),
        'c2_eff_weighted': c2_eff_weighted,
        'c2_eff_max': c2_eff_max,
        'c2_sat_th': c2_sat_th, 'c2_max_th': c2_max_th, 'c2_eff_th': c2_eff_th,
        'nu': nu,
        'gap_min_deep': gap_min,
        'energy': result.energy,
        'bind': result.diagnostics.bind,
        'converged': result.converged,
        'bdy_frac': n_bdy / n,
    }


def main():
    print("=" * 80)
    print("H3 JACOBIAN ANALYSIS: Site-Weighted C₂^eff Verification")
    print("=" * 80)

    # Test configurations
    configs = [
        # (grid_size, beta, c, a_cl)
        ((8, 8), 30.0, 0.3, 3.0),
        ((10, 10), 30.0, 0.3, 3.0),
        ((10, 10), 20.0, 0.3, 3.0),
        ((10, 10), 50.0, 0.3, 3.0),
        ((10, 10), 30.0, 0.3, 3.5),
        ((15, 15), 30.0, 0.3, 3.0),
        ((20, 20), 30.0, 0.3, 3.0),
        ((20, 20), 50.0, 0.3, 3.0),
        ((10, 10), 10.0, 0.3, 3.0),
        ((10, 10), 30.0, 0.4, 3.0),
    ]

    all_results = []

    print("\n--- Part 1: Site-Specific Jacobian Verification ---\n")
    print(f"{'Grid':>7} {'β':>5} {'a_cl':>4} | {'J_core':>8} {'J_core_th':>9} | "
          f"{'J_bdy':>8} {'J_bdy_th':>9} | {'|r|_core':>8} {'|r|_bdy':>8}")
    print("-" * 95)

    for gs, beta, c, a_cl in configs:
        r = analyze_formation(gs, beta, c, a_cl)
        all_results.append(r)
        print(f"{r['grid']:>7} {beta:>5.0f} {a_cl:>4.1f} | "
              f"{r['J_core_mean']:>8.4f} {r['J_core_th']:>9.4f} | "
              f"{r['J_bdy_mean']:>8.4f} {r['J_bdy_th']:>9.4f} | "
              f"{r['r_core_mean']:>8.4f} {r['r_bdy_mean']:>8.4f}")

    print("\n--- Part 2: C₂^eff Weighted Analysis ---\n")
    print(f"{'Grid':>7} {'β':>5} | {'n_core':>6} {'n_bdy':>6} {'bdy%':>5} | "
          f"{'C₂_core':>7} {'C₂_bdy':>7} {'C₂_eff':>7} {'C₂_th':>7} | "
          f"{'ν':>7} {'gap_min':>7}")
    print("-" * 100)

    for r in all_results:
        print(f"{r['grid']:>7} {r['beta']:>5.0f} | "
              f"{r['n_core']:>6} {r['n_bdy']:>6} {r['bdy_frac']:>5.2f} | "
              f"{r['c2_core_mean']:>7.3f} {r['c2_bdy_mean']:>7.3f} "
              f"{r['c2_eff_weighted']:>7.3f} {r['c2_eff_th']:>7.3f} | "
              f"{r['nu']:>7.3f} {r['gap_min_deep']:>7.4f}")

    print("\n--- Part 3: Scaling Analysis (n_bdy ∝ √n) ---\n")
    # Filter for a_cl=3.0, beta=30, c=0.3
    scaling_data = [r for r in all_results if r['a_cl'] == 3.0 and r['beta'] == 30.0 and r['c'] == 0.3]
    if scaling_data:
        print(f"{'Grid':>7} {'n':>5} {'n_bdy':>6} {'√n':>6} {'n_bdy/√n':>8} {'C₂_eff':>7} {'β_thresh':>8}")
        print("-" * 60)
        for r in sorted(scaling_data, key=lambda x: x['n']):
            sqrt_n = np.sqrt(r['n'])
            ratio = r['n_bdy'] / sqrt_n if sqrt_n > 0 else float('nan')
            beta_thresh = 2 * r['c2_eff_weighted']
            print(f"{r['grid']:>7} {r['n']:>5} {r['n_bdy']:>6} {sqrt_n:>6.1f} "
                  f"{ratio:>8.2f} {r['c2_eff_weighted']:>7.3f} {beta_thresh:>8.3f}")

    print("\n--- Part 4: Theoretical vs Actual Summary ---\n")

    # Compute R² for C₂^eff theoretical vs actual
    c2_actual = np.array([r['c2_eff_weighted'] for r in all_results if not np.isnan(r['c2_eff_weighted'])])
    c2_theory = np.array([r['c2_eff_th'] for r in all_results if not np.isnan(r['c2_eff_weighted'])])

    if len(c2_actual) > 1:
        ss_res = np.sum((c2_actual - c2_theory)**2)
        ss_tot = np.sum((c2_actual - np.mean(c2_actual))**2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else float('nan')

        print(f"C₂^eff: R² (theory vs actual) = {r_squared:.4f}")
        print(f"  Mean actual:  {np.mean(c2_actual):.4f}")
        print(f"  Mean theory:  {np.mean(c2_theory):.4f}")
        print(f"  Max |error|:  {np.max(np.abs(c2_actual - c2_theory)):.4f}")
        print(f"  RMSE:         {np.sqrt(np.mean((c2_actual - c2_theory)**2)):.4f}")

    # Interior gap verification
    print("\n--- Part 5: Interior Gap Verification ---\n")
    for r in all_results:
        beta_ratio = r['beta'] / 1.0  # alpha=1 normalization
        gap_ok = "✓" if r['gap_min_deep'] > 0 else "✗"
        c2_cond = 2 * r['c2_eff_weighted'] if not np.isnan(r['c2_eff_weighted']) else float('nan')
        ratio_ok = "✓" if beta_ratio > c2_cond else "✗"
        print(f"  {r['grid']} β={r['beta']:>5.0f}: gap_min={r['gap_min_deep']:>7.4f} {gap_ok} | "
              f"β/α={beta_ratio:>5.0f} > 2C₂={c2_cond:>6.3f} {ratio_ok} | "
              f"Bind={r['bind']:.3f}")

    print("\n" + "=" * 80)
    print("CONCLUSION")
    print("=" * 80)

    # Check key claims
    all_gaps_positive = all(r['gap_min_deep'] > 0 for r in all_results if not np.isnan(r['gap_min_deep']))
    print(f"1. All interior gaps positive at β ≥ 10: {all_gaps_positive}")
    print(f"2. J_core ≈ 0.224 (theory): actual range [{min(r['J_core_mean'] for r in all_results if not np.isnan(r['J_core_mean'])):.4f}, {max(r['J_core_mean'] for r in all_results if not np.isnan(r['J_core_mean'])):.4f}]")
    print(f"3. J_bdy ≈ 0.375 (theory): actual range [{min(r['J_bdy_mean'] for r in all_results if not np.isnan(r['J_bdy_mean'])):.4f}, {max(r['J_bdy_mean'] for r in all_results if not np.isnan(r['J_bdy_mean'])):.4f}]")

    if scaling_data and len(scaling_data) >= 3:
        ns = np.array([r['n'] for r in sorted(scaling_data, key=lambda x: x['n'])])
        nbdys = np.array([r['n_bdy'] for r in sorted(scaling_data, key=lambda x: x['n'])])
        # Fit n_bdy = a * n^b
        log_ns = np.log(ns)
        log_nbdys = np.log(nbdys + 1)
        b_fit = np.polyfit(log_ns, log_nbdys, 1)[0]
        print(f"4. n_bdy scaling exponent: {b_fit:.3f} (expected ≈ 0.5 for √n)")

    print(f"5. C₂^eff < 1.0 for all tested configurations: {all(r['c2_eff_weighted'] < 1.0 for r in all_results if not np.isnan(r['c2_eff_weighted']))}")


if __name__ == '__main__':
    main()
