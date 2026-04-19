#!/usr/bin/env python3
"""Experiment 40: End-to-end T-Persist with transport confinement verification.

Validates the NEW transport confinement condition (C_conf·√m < r_basin)
from the proved confinement bound in ISOPERIMETRIC-TRANSPORT-PROOFS.md.

Three parts:
  1. Condition verification: is C_conf·√m < r_basin for typical configs?
  2. End-to-end persistence: does persist ≥ 0.9 when confinement holds?
  3. Bound tightness: actual displacement vs theoretical bound.

Old condition WR': λ_tr·γ·‖∂φ/∂u‖/(ε_OT·μ) < 1 (Banach contraction)
New condition: C_conf·√m < r_basin where C_conf = O(σ·√(ε_OT·log n))
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.energy import EnergyComputer, energy_bd, grad_bd, energy_cl, grad_cl, energy_sep, grad_sep
from scc.transport import (
    transport_fixed_point, cohesion_fingerprint, graph_distance_matrix,
    transport_cost, sinkhorn_partial_ot, transport_field, TransportResult,
)
from scc.diagnostics import compute_diagnostics
from scipy.sparse.linalg import LinearOperator, eigsh


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_params(beta=50.0, vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


def numerical_hessian_action(u, graph, params, ec, v, h=1e-5):
    """Compute H·v via finite differences of the gradient."""
    g_plus = ec.gradient(u + h * v)
    g_minus = ec.gradient(u - h * v)
    return (g_plus - g_minus) / (2 * h)


def compute_hessian_smallest_eigenvalue(u, graph, params, ec, k=3):
    """Compute smallest eigenvalue of the Hessian restricted to T(Σ_m).

    Projects out the constant mode (volume constraint tangent space).
    Returns (μ, eigvec) where μ is the smallest eigenvalue.
    """
    n = len(u)
    ones = np.ones(n) / np.sqrt(n)

    def hess_projected(v):
        # Project v to tangent space
        v = v - np.dot(v, ones) * ones
        Hv = numerical_hessian_action(u, graph, params, ec, v)
        # Project result to tangent space
        Hv = Hv - np.dot(Hv, ones) * ones
        return Hv

    H_op = LinearOperator((n, n), matvec=hess_projected, dtype=np.float64)

    try:
        eigvals, eigvecs = eigsh(H_op, k=min(k, n - 2), which='SM')
        # Filter out near-zero eigenvalues (the constant mode leakage)
        valid = eigvals > 1e-8
        if np.any(valid):
            mu = eigvals[valid][0]
            vec = eigvecs[:, valid][:, 0]
        else:
            mu = eigvals[0]
            vec = eigvecs[:, 0]
        return float(mu), vec
    except Exception:
        return 0.0, np.zeros(n)


def compute_barrier_height(u, graph, params, ec, soft_mode, n_steps=50):
    """Estimate energy barrier by walking along the soft mode.

    Walks from u* along ±soft_mode, projecting to Σ_m at each step,
    until energy rises then falls (barrier) or we hit domain boundary.
    """
    m = float(np.sum(u))
    E_star = ec.energy(u)[0]

    best_barrier = 0.0
    for sign in [1.0, -1.0]:
        direction = sign * soft_mode / np.linalg.norm(soft_mode)
        E_prev = E_star
        max_E = E_star
        passed_barrier = False

        for step in range(1, n_steps + 1):
            alpha = step * 0.05  # step size
            u_test = u + alpha * direction
            u_test = project_volume(np.clip(u_test, 0, 1), m)
            E_test = ec.energy(u_test)[0]

            if E_test > max_E:
                max_E = E_test
            elif E_test < max_E - 1e-10 and max_E > E_star + 1e-10:
                passed_barrier = True
                break

        barrier = max_E - E_star
        if barrier > best_barrier:
            best_barrier = barrier

    return float(best_barrier)


def compute_fingerprint_jacobian_norm(u, graph, params, n_samples=10):
    """Estimate ‖∂φ/∂u‖ via finite differences (operator norm)."""
    n = len(u)
    h = 1e-5
    phi0 = cohesion_fingerprint(u, graph, params)  # (n, 3)
    max_norm = 0.0

    rng = np.random.RandomState(42)
    for _ in range(n_samples):
        v = rng.randn(n)
        v /= np.linalg.norm(v)
        phi_plus = cohesion_fingerprint(u + h * v, graph, params)
        dphi = (phi_plus - phi0) / h  # (n, 3)
        norm = np.linalg.norm(dphi)
        if norm > max_norm:
            max_norm = norm

    return float(max_norm)


def compute_old_wr_condition(u, graph, params, sigma=1.0, gamma=1.0,
                             eps_ot=1.0, lambda_tr=1.0, mu=1.0):
    """Old WR' condition: λ_tr·γ·‖∂φ/∂u‖/(ε_OT·μ) < 1."""
    dphi_norm = compute_fingerprint_jacobian_norm(u, graph, params)
    wr_value = lambda_tr * gamma * dphi_norm / (eps_ot * max(mu, 1e-12))
    return float(wr_value), float(dphi_norm)


# ---------------------------------------------------------------------------
# Configs
# ---------------------------------------------------------------------------

CONFIGS = [
    {"name": "10x10_b30", "grid": (10, 10), "beta": 30.0},
    {"name": "10x10_b50", "grid": (10, 10), "beta": 50.0},
    {"name": "15x15_b30", "grid": (15, 15), "beta": 30.0},
    {"name": "15x15_b50", "grid": (15, 15), "beta": 50.0},
    {"name": "15x15_b100", "grid": (15, 15), "beta": 100.0},
    {"name": "20x20_b50", "grid": (20, 20), "beta": 50.0},
]


# ---------------------------------------------------------------------------
# Part 1: Confinement condition verification
# ---------------------------------------------------------------------------

def run_part1(configs):
    """Verify C_conf·√m < r_basin for each config."""
    print("=" * 70)
    print("PART 1: Transport confinement condition verification")
    print("=" * 70)

    results = []
    for cfg in configs:
        t0 = time.time()
        name = cfg["name"]
        rows, cols = cfg["grid"]
        beta = cfg["beta"]
        n = rows * cols

        print(f"\n--- {name} (n={n}, β={beta}) ---")

        graph = GraphState.grid_2d(rows, cols)
        params = make_params(beta=beta)
        ec = EnergyComputer(graph, params)
        ec.normalize_weights()

        # Find formation
        result = find_formation(graph, params)
        u_star = result.u
        m = float(np.sum(u_star))
        E_star = result.energy

        print(f"  Formation: m={m:.2f}, E={E_star:.4f}, converged={result.converged}")

        # C_conf = σ·√(ε_OT·log(n)) with σ=1, ε_OT=1
        sigma, eps_ot = 1.0, 1.0
        C_conf = sigma * np.sqrt(eps_ot * np.log(n))
        confinement_radius = C_conf * np.sqrt(m)

        # Hessian spectral gap μ (smallest eigenvalue on tangent space)
        mu, soft_mode = compute_hessian_smallest_eigenvalue(u_star, graph, params, ec)
        print(f"  Hessian spectral gap μ = {mu:.6f}")

        # Energy barrier Δ_bdy
        if mu > 1e-8 and np.linalg.norm(soft_mode) > 0.5:
            delta_bdy = compute_barrier_height(u_star, graph, params, ec, soft_mode)
        else:
            delta_bdy = 0.0
        print(f"  Energy barrier Δ_bdy = {delta_bdy:.6f}")

        # Basin radius r_basin = √(2·Δ_bdy / λ_max_H)
        # Use largest Hessian eigenvalue for conservative estimate
        lambda_max_H = mu + 100  # rough upper bound; refine below
        try:
            def hess_mv(v):
                return numerical_hessian_action(u_star, graph, params, ec, v)
            H_op = LinearOperator((n, n), matvec=hess_mv, dtype=np.float64)
            lambda_max_H = float(eigsh(H_op, k=1, which='LM', return_eigenvectors=False)[0])
        except Exception:
            pass

        r_basin = np.sqrt(2 * delta_bdy / max(lambda_max_H, 1e-12))

        confined = confinement_radius < r_basin
        print(f"  C_conf·√m = {confinement_radius:.4f}")
        print(f"  r_basin   = {r_basin:.4f}")
        print(f"  CONFINED: {'YES' if confined else 'NO'}")

        # Old WR' condition
        wr_value, dphi_norm = compute_old_wr_condition(
            u_star, graph, params, sigma=sigma, gamma=1.0,
            eps_ot=eps_ot, lambda_tr=1.0, mu=max(mu, 1e-12)
        )
        wr_holds = wr_value < 1.0
        print(f"  WR' value = {wr_value:.4f} ({'holds' if wr_holds else 'FAILS'})")

        elapsed = time.time() - t0
        print(f"  Time: {elapsed:.1f}s")

        results.append({
            "config": name,
            "n": n,
            "beta": beta,
            "m": m,
            "E_star": E_star,
            "C_conf": float(C_conf),
            "C_conf_sqrt_m": float(confinement_radius),
            "mu_hessian": mu,
            "delta_bdy": delta_bdy,
            "lambda_max_H": float(lambda_max_H),
            "r_basin": float(r_basin),
            "confined": confined,
            "wr_value": wr_value,
            "wr_holds": wr_holds,
            "dphi_norm": dphi_norm,
            "elapsed_s": elapsed,
        })

    return results


# ---------------------------------------------------------------------------
# Part 2: End-to-end persistence verification
# ---------------------------------------------------------------------------

def run_part2(configs, part1_results):
    """For configs where confinement holds, verify persistence end-to-end."""
    print("\n" + "=" * 70)
    print("PART 2: End-to-end persistence verification")
    print("=" * 70)

    results = []
    for cfg, p1 in zip(configs, part1_results):
        t0 = time.time()
        name = cfg["name"]
        rows, cols = cfg["grid"]
        beta = cfg["beta"]

        print(f"\n--- {name} ---")

        graph = GraphState.grid_2d(rows, cols)
        params = make_params(beta=beta)

        # Find formation
        result = find_formation(graph, params)
        u_star = result.u
        m = float(np.sum(u_star))

        # Transport fixed point
        tr = transport_fixed_point(
            u_t=u_star, graph=graph, params=params,
            sigma=1.0, gamma=1.0, eps_ot=1.0, lambda_tr=1.0,
        )
        print(f"  Transport FP: converged={tr.converged}, iters={tr.iterations}")

        # Temporal perturbation
        rng = np.random.RandomState(123)
        eps_pert = 0.10
        u_pert = u_star + eps_pert * rng.randn(len(u_star))
        u_pert = project_volume(np.clip(u_pert, 0, 1), m)

        # Re-optimize from perturbed initial point
        params_reopt = make_params(beta=beta)
        ec_reopt = EnergyComputer(graph, params_reopt)
        ec_reopt.normalize_weights()
        from scc.optimizer import _optimize_single_from
        u_reopt, _, _, _, _, _, _ = _optimize_single_from(
            graph, params_reopt, ec_reopt, u_pert
        )

        # Persist metric: overlap
        persist = float(np.sum(np.minimum(u_star, u_reopt)) /
                        max(np.sum(u_star), np.sum(u_reopt)))
        persist_good = persist >= 0.9

        # Also compute diagnostics
        diag = compute_diagnostics(u_star, graph, params)

        elapsed = time.time() - t0
        print(f"  Persist (overlap) = {persist:.4f} ({'PASS' if persist_good else 'FAIL'})")
        print(f"  Diagnostics: {diag}")
        print(f"  Time: {elapsed:.1f}s")

        results.append({
            "config": name,
            "transport_converged": tr.converged,
            "transport_iters": tr.iterations,
            "persist_overlap": persist,
            "persist_pass": persist_good,
            "bind": diag.bind,
            "sep": diag.sep,
            "inside": diag.inside,
            "confined": p1["confined"],
            "elapsed_s": elapsed,
        })

    return results


# ---------------------------------------------------------------------------
# Part 3: Confinement bound tightness
# ---------------------------------------------------------------------------

def run_part3(configs, part1_results):
    """Compare actual transport displacement with theoretical bound."""
    print("\n" + "=" * 70)
    print("PART 3: Confinement bound tightness")
    print("=" * 70)

    results = []
    for cfg, p1 in zip(configs, part1_results):
        t0 = time.time()
        name = cfg["name"]
        rows, cols = cfg["grid"]
        beta = cfg["beta"]

        print(f"\n--- {name} ---")

        graph = GraphState.grid_2d(rows, cols)
        params = make_params(beta=beta)

        # Find formation
        result = find_formation(graph, params)
        u_star = result.u

        # Run transport to get transported field
        tr = transport_fixed_point(
            u_t=u_star, graph=graph, params=params,
            sigma=1.0, gamma=1.0, eps_ot=1.0, lambda_tr=1.0,
        )

        # Actual displacement
        actual_disp = float(np.linalg.norm(tr.u_s - u_star))

        # Theoretical bound
        C_conf_sqrt_m = p1["C_conf_sqrt_m"]

        ratio = actual_disp / max(C_conf_sqrt_m, 1e-12)

        elapsed = time.time() - t0
        print(f"  Actual displacement ‖ũ - u*‖ = {actual_disp:.6f}")
        print(f"  Theoretical bound C_conf·√m  = {C_conf_sqrt_m:.6f}")
        print(f"  Ratio (actual/bound)         = {ratio:.4f}")
        print(f"  Bound valid: {'YES' if ratio < 1.0 else 'NO'}")
        print(f"  Time: {elapsed:.1f}s")

        results.append({
            "config": name,
            "actual_displacement": actual_disp,
            "theoretical_bound": C_conf_sqrt_m,
            "ratio": ratio,
            "bound_valid": ratio < 1.0,
            "elapsed_s": elapsed,
        })

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Experiment 40: Transport Confinement Verification")
    print("=" * 70)
    print(f"Configs: {len(CONFIGS)}")
    print()

    t_total = time.time()

    p1_results = run_part1(CONFIGS)

    p2_results = run_part2(CONFIGS, p1_results)

    p3_results = run_part3(CONFIGS, p1_results)

    # Summary table
    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    header = f"{'Config':<14} {'n':>4} {'m':>6} {'C√m':>8} {'r_basin':>8} {'Conf?':>6} {'WR?':>5} {'Persist':>8} {'Disp':>8} {'Ratio':>7}"
    print(header)
    print("-" * len(header))

    for p1, p2, p3 in zip(p1_results, p2_results, p3_results):
        conf_str = "YES" if p1["confined"] else "no"
        wr_str = "YES" if p1["wr_holds"] else "no"
        print(f"{p1['config']:<14} {p1['n']:>4} {p1['m']:>6.1f} "
              f"{p1['C_conf_sqrt_m']:>8.4f} {p1['r_basin']:>8.4f} "
              f"{conf_str:>6} {wr_str:>5} "
              f"{p2['persist_overlap']:>8.4f} "
              f"{p3['actual_displacement']:>8.6f} {p3['ratio']:>7.4f}")

    elapsed_total = time.time() - t_total
    print(f"\nTotal time: {elapsed_total:.1f}s")

    # Count results
    n_confined = sum(1 for r in p1_results if r["confined"])
    n_persist = sum(1 for r in p2_results if r["persist_pass"])
    n_bound_valid = sum(1 for r in p3_results if r["bound_valid"])
    print(f"\nConfinement holds: {n_confined}/{len(CONFIGS)}")
    print(f"Persistence ≥ 0.9: {n_persist}/{len(CONFIGS)}")
    print(f"Bound valid (ratio < 1): {n_bound_valid}/{len(CONFIGS)}")

    # Key finding
    all_confined_persist = all(
        p2["persist_pass"] for p1, p2 in zip(p1_results, p2_results) if p1["confined"]
    )
    print(f"\nKey finding: All confined configs have persist ≥ 0.9: {all_confined_persist}")

    # Save JSON
    output = {
        "experiment": "exp40_persist_confinement",
        "description": "Transport confinement condition verification",
        "part1_condition": p1_results,
        "part2_persistence": p2_results,
        "part3_tightness": p3_results,
        "summary": {
            "n_configs": len(CONFIGS),
            "n_confined": n_confined,
            "n_persist_pass": n_persist,
            "n_bound_valid": n_bound_valid,
            "all_confined_persist": all_confined_persist,
            "total_time_s": elapsed_total,
        },
    }

    os.makedirs("experiments/results", exist_ok=True)
    with open("experiments/results/exp40_persist_confinement.json", "w") as f:
        json.dump(output, f, indent=2, default=lambda x: bool(x) if isinstance(x, np.bool_) else float(x))

    print("\nResults saved to experiments/results/exp40_persist_confinement.json")
    return output


if __name__ == "__main__":
    main()
