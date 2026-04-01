#!/usr/bin/env python3
"""Experiment 37: Bifurcation crossing — formation birth/death as β sweeps through β_crit.

Level 3 open item in T-Persist theory: what happens at the pitchfork bifurcation?

Part 1: β sweep — track formation emergence (strength, core, energy, spectral gap, soft-Fiedler correlation)
Part 2: Branch selection — perturb with ±Fiedler near β_crit, test pitchfork vs transcritical
Part 3: Hysteresis — forward vs backward sweep, check if β_crit differs
"""
import sys, os, json, time
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.energy import EnergyComputer


def hessian_vec_product(ec, u, v, eps=1e-5):
    """Hessian-vector product via central finite differences."""
    gp = ec.gradient(u + eps * v)
    gm = ec.gradient(u - eps * v)
    return (gp - gm) / (2 * eps)


def projected_hessian_smallest(ec, u, k=3):
    """Compute k smallest eigenvalues/vectors of Hessian projected to T(Sigma_m).

    Uses dense decomposition for reliability on 12x12 grid.
    Returns (eigenvalues, eigenvectors, all_nonzero_eigenvalues).
    """
    n = len(u)
    P = np.eye(n) - np.ones((n, n)) / n

    H_dense = np.zeros((n, n))
    for i in range(n):
        ei = np.zeros(n)
        ei[i] = 1.0
        ei_proj = P @ ei
        Hv = hessian_vec_product(ec, u, ei_proj)
        H_dense[:, i] = P @ Hv
    H_dense = 0.5 * (H_dense + H_dense.T)

    evals, evecs = np.linalg.eigh(H_dense)

    # Skip near-zero eigenvalues from null space of projection
    nz_mask = np.abs(evals) > 1e-8
    evals_nz = evals[nz_mask]
    evecs_nz = evecs[:, nz_mask]

    k_ret = min(k, len(evals_nz))
    return evals_nz[:k_ret], evecs_nz[:, :k_ret], evals_nz


def run_experiment():
    t0 = time.time()
    print("=" * 70)
    print("Experiment 37: Bifurcation Crossing")
    print("=" * 70)

    # Setup
    grid_size = 12
    n = grid_size * grid_size  # 144
    graph = GraphState.grid_2d(grid_size, grid_size)
    c = 0.3
    m = c * n

    fiedler_vec = graph.fiedler_vector()
    fiedler_vec = fiedler_vec / np.linalg.norm(fiedler_vec)
    fiedler_eval = graph.fiedler
    print(f"Grid: {grid_size}x{grid_size} (n={n}), volume_fraction={c}")
    print(f"Fiedler eigenvalue λ₂ = {fiedler_eval:.6f}")
    print()

    # =========================================================================
    # Part 1: β sweep — formation emergence
    # =========================================================================
    print("Part 1: β sweep (β = 5 to 54)")
    print("-" * 70)
    beta_values = np.arange(5, 55, 1).astype(float)
    sweep_results = []

    header = f"{'β':>5} | {'strength':>9} | {'core':>5} | {'energy':>10} | {'μ_min':>10} | {'Fiedler_corr':>12}"
    print(header)
    print("-" * len(header))

    for beta in beta_values:
        params = ParameterRegistry(
            beta_bd=beta, volume_fraction=c,
            n_restarts=5, max_iter=3000
        )
        result = find_formation(graph, params)
        u = result.u

        strength = float(np.max(u) - np.min(u))
        core_size = int(np.sum(u >= 0.8))
        energy = result.energy

        # Spectral gap: smallest eigenvalue of projected Hessian at u*
        ec = EnergyComputer(graph, params)
        ec.normalize_weights()
        try:
            evals_small, evecs_small, all_evals = projected_hessian_smallest(ec, u, k=3)
            mu_min = float(evals_small[0]) if len(evals_small) > 0 else float('nan')
            soft_mode = evecs_small[:, 0] if len(evals_small) > 0 else np.zeros(n)
        except Exception as e:
            mu_min = float('nan')
            soft_mode = np.zeros(n)

        # Correlation of soft mode with Fiedler vector
        if np.linalg.norm(soft_mode) > 1e-12:
            corr = abs(float(np.dot(soft_mode, fiedler_vec)))
        else:
            corr = 0.0

        row = {
            'beta': float(beta),
            'strength': strength,
            'core_size': core_size,
            'energy': energy,
            'mu_min': mu_min,
            'fiedler_corr': corr,
            'converged': result.converged,
        }
        sweep_results.append(row)

        print(f"{beta:5.0f} | {strength:9.4f} | {core_size:5d} | {energy:10.4f} | {mu_min:10.4f} | {corr:12.4f}")

    # Identify β_crit: first β where strength > 0.1
    beta_crit = None
    for r in sweep_results:
        if r['strength'] > 0.1:
            beta_crit = r['beta']
            break

    if beta_crit is None:
        beta_crit = float(beta_values[-1])
        print("\nWARNING: No formation emerged in sweep range!")

    print(f"\nβ_crit (strength > 0.1) ≈ {beta_crit}")

    # Also find theoretical β_crit from T8-Core: β/α > 4λ₂/|W''(c)|
    from scc.energy import double_well_second_deriv
    W_pp = double_well_second_deriv(c)
    alpha_default = 1.0  # default alpha_bd
    beta_crit_theory = 4.0 * alpha_default * fiedler_eval / abs(W_pp)
    print(f"Theoretical β_crit (T8-Core) = 4α·λ₂/|W''(c)| = {beta_crit_theory:.4f}")
    print(f"  (α={alpha_default}, λ₂={fiedler_eval:.6f}, W''({c})={W_pp:.6f})")

    # =========================================================================
    # Part 2: Branch selection near β_crit
    # =========================================================================
    print()
    print("Part 2: Branch selection near β_crit")
    print("-" * 70)

    beta_test = beta_crit + 2  # slightly above critical
    params_branch = ParameterRegistry(
        beta_bd=beta_test, volume_fraction=c,
        n_restarts=1, max_iter=5000
    )
    delta = 0.05
    u_uniform = np.full(n, c)

    # +Fiedler perturbation
    u_plus_init = project_volume(u_uniform + delta * fiedler_vec, m)
    # -Fiedler perturbation
    u_minus_init = project_volume(u_uniform - delta * fiedler_vec, m)

    # Override initial condition via direct optimization
    from scc.optimizer import _optimize_single
    ec_branch = EnergyComputer(graph, params_branch)
    ec_branch.normalize_weights()

    # For branch selection, manually set initial conditions and optimize
    # Use find_formation but with eps_init=0 to start near our prescribed u_init
    # Actually, we'll use the internal optimizer with our init
    def optimize_from_init(u_init):
        """Run gradient descent from a specific initial condition."""
        u = u_init.copy()
        dt = params_branch.dt_init
        E_old, _ = ec_branch.energy(u)
        for tau in range(5000):
            g = ec_branch.gradient(u)
            g_sigma = g - np.mean(g)
            u_new = project_volume(u - dt * g_sigma, m)
            E_new, _ = ec_branch.energy(u_new)
            if E_new > E_old and tau > 5:
                dt *= 0.5
                if dt < 1e-12:
                    break
                continue
            s = u_new - u
            g_new = ec_branch.gradient(u_new)
            y = (g_new - np.mean(g_new)) - g_sigma
            sy = float(np.dot(s, y))
            ss = float(np.dot(s, s))
            if sy > 1e-15:
                dt = min(ss / sy, 10.0 * dt)
            dt = np.clip(dt, 1e-8, 1.0)
            if ss < 1e-14:
                break
            u = u_new
            E_old = E_new
        return u, E_old

    print(f"Testing at β = {beta_test} (β_crit + 2)")
    u_plus, E_plus = optimize_from_init(u_plus_init)
    u_minus, E_minus = optimize_from_init(u_minus_init)

    strength_plus = float(np.max(u_plus) - np.min(u_plus))
    strength_minus = float(np.max(u_minus) - np.min(u_minus))
    overlap = float(np.dot(u_plus, u_minus) / (np.linalg.norm(u_plus) * np.linalg.norm(u_minus)))
    field_diff = float(np.linalg.norm(u_plus - u_minus))
    anti_corr = float(np.corrcoef(u_plus, u_minus)[0, 1])

    # Check if they're the same formation or mirror images
    # For pitchfork: u_plus and u_minus should be distinct (potentially mirror)
    # Compute spatial center of mass
    coords = np.array([(i // grid_size, i % grid_size) for i in range(n)])
    com_plus = np.average(coords, axis=0, weights=u_plus)
    com_minus = np.average(coords, axis=0, weights=u_minus)

    print(f"  +Fiedler branch: strength={strength_plus:.4f}, E={E_plus:.4f}, CoM=({com_plus[0]:.2f},{com_plus[1]:.2f})")
    print(f"  -Fiedler branch: strength={strength_minus:.4f}, E={E_minus:.4f}, CoM=({com_minus[0]:.2f},{com_minus[1]:.2f})")
    print(f"  Field overlap (cos): {overlap:.4f}")
    print(f"  Field difference ||u+ - u-||: {field_diff:.4f}")
    print(f"  Pearson correlation: {anti_corr:.4f}")

    com_dist = float(np.linalg.norm(com_plus - com_minus))
    is_pitchfork = (field_diff > 0.5 and com_dist > 1.0)
    bifurcation_type = "pitchfork (two distinct branches)" if is_pitchfork else "transcritical or single branch"
    print(f"  CoM distance: {com_dist:.4f}")
    print(f"  Bifurcation type: {bifurcation_type}")

    branch_result = {
        'beta_test': beta_test,
        'strength_plus': strength_plus,
        'strength_minus': strength_minus,
        'energy_plus': E_plus,
        'energy_minus': E_minus,
        'field_diff': field_diff,
        'overlap': overlap,
        'correlation': anti_corr,
        'com_plus': com_plus.tolist(),
        'com_minus': com_minus.tolist(),
        'com_distance': com_dist,
        'bifurcation_type': bifurcation_type,
    }

    # =========================================================================
    # Part 3: Hysteresis test
    # =========================================================================
    print()
    print("Part 3: Hysteresis test (forward vs backward sweep)")
    print("-" * 70)

    # Forward sweep: start from uniform, increase β
    beta_fine = np.arange(5, 55, 0.5)
    forward_strengths = []
    u_prev = np.full(n, c)

    print("Forward sweep (uniform → high β)...")
    for beta in beta_fine:
        params_fwd = ParameterRegistry(
            beta_bd=beta, volume_fraction=c,
            n_restarts=1, max_iter=2000, eps_init=0.001
        )
        result_fwd = find_formation(graph, params_fwd)
        strength = float(np.max(result_fwd.u) - np.min(result_fwd.u))
        forward_strengths.append(strength)
        u_prev = result_fwd.u.copy()

    # Backward sweep: start from last formation, decrease β
    backward_strengths = []
    u_warm = u_prev.copy()  # start from the formation at β=54.5

    print("Backward sweep (formation → low β)...")
    for beta in reversed(beta_fine):
        params_bwd = ParameterRegistry(
            beta_bd=beta, volume_fraction=c,
            n_restarts=1, max_iter=2000, eps_init=0.001
        )
        # Use warm start: optimize from previous formation
        ec_bwd = EnergyComputer(graph, params_bwd)
        ec_bwd.normalize_weights()
        u_opt, E_opt = optimize_from_init(project_volume(u_warm, m))
        strength = float(np.max(u_opt) - np.min(u_opt))
        backward_strengths.append(strength)
        u_warm = u_opt.copy()

    backward_strengths = list(reversed(backward_strengths))

    # Find crossing thresholds
    threshold = 0.1
    beta_crit_fwd = None
    for i, s in enumerate(forward_strengths):
        if s > threshold:
            beta_crit_fwd = float(beta_fine[i])
            break

    beta_crit_bwd = None
    for i in range(len(backward_strengths) - 1, -1, -1):
        if backward_strengths[i] > threshold:
            if i == 0 or backward_strengths[i - 1] <= threshold:
                beta_crit_bwd = float(beta_fine[i])
                break
    # If backward never drops below threshold in the range, find where it first drops
    if beta_crit_bwd is None:
        for i, s in enumerate(backward_strengths):
            if s <= threshold:
                beta_crit_bwd = float(beta_fine[max(0, i - 1)])
                break

    hysteresis_gap = 0.0
    if beta_crit_fwd is not None and beta_crit_bwd is not None:
        hysteresis_gap = beta_crit_fwd - beta_crit_bwd

    print(f"  Forward β_crit  (strength > {threshold}): {beta_crit_fwd}")
    print(f"  Backward β_crit (strength > {threshold}): {beta_crit_bwd}")
    print(f"  Hysteresis gap: {hysteresis_gap:.2f}")

    if abs(hysteresis_gap) < 1.5:
        hysteresis_verdict = "No significant hysteresis (continuous/supercritical pitchfork)"
    elif hysteresis_gap > 0:
        hysteresis_verdict = f"Hysteresis detected (Δβ={hysteresis_gap:.2f}): forward delayed, backward persists lower"
    else:
        hysteresis_verdict = f"Reverse hysteresis (Δβ={hysteresis_gap:.2f}): formation emerges earlier going forward"

    print(f"  Verdict: {hysteresis_verdict}")

    hysteresis_result = {
        'beta_fine': beta_fine.tolist(),
        'forward_strengths': forward_strengths,
        'backward_strengths': backward_strengths,
        'beta_crit_forward': beta_crit_fwd,
        'beta_crit_backward': beta_crit_bwd,
        'hysteresis_gap': hysteresis_gap,
        'verdict': hysteresis_verdict,
    }

    # =========================================================================
    # Summary
    # =========================================================================
    elapsed = time.time() - t0
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"β_crit (empirical, Part 1):     {beta_crit}")
    print(f"β_crit (theoretical, T8-Core):  {beta_crit_theory:.4f}")
    print(f"Bifurcation type:               {bifurcation_type}")
    print(f"Hysteresis:                      {hysteresis_verdict}")
    print(f"Total time:                      {elapsed:.1f}s")

    # Key physics check
    if beta_crit_theory > 0:
        ratio = beta_crit / beta_crit_theory
        print(f"Empirical/Theoretical ratio:    {ratio:.3f}")
        if 0.7 < ratio < 1.5:
            print("  → Theory and experiment are broadly consistent")
        else:
            print(f"  → Significant discrepancy (ratio={ratio:.3f})")

    # Save JSON
    output = {
        'experiment': 'exp37_bifurcation_crossing',
        'grid_size': grid_size,
        'n': n,
        'volume_fraction': c,
        'fiedler_eigenvalue': fiedler_eval,
        'beta_crit_empirical': beta_crit,
        'beta_crit_theoretical': beta_crit_theory,
        'sweep_results': sweep_results,
        'branch_selection': branch_result,
        'hysteresis': hysteresis_result,
        'elapsed_seconds': elapsed,
    }

    outpath = os.path.join(os.path.dirname(__file__), 'results', 'exp37_bifurcation_crossing.json')
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {outpath}")


if __name__ == '__main__':
    run_experiment()
