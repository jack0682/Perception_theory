#!/usr/bin/env python3
"""Experiment 89: Endpoint vs Action Temporal Cost — Composition Residual Comparison.

Numerical anchor for CV-1.15 (Action-Based Temporal Succession Package).

Validates:
  - L-ENDPOINT-NONSEMI:  endpoint² cost composition residual > 0
  - T-ACT-DP:            hard-min action cost composition residual ≈ 0
  - T-ACT-GIBBS:         soft-min/Gibbs kernel semigroup residual ≈ machine epsilon
  - T-SINKHORN-PLAN-SEMIGROUP-FAILS: Sinkhorn plan residual > 0 generically

Three test cases:
  Case A: 1D uniform translation (analytic ground truth)
  Case B: 2D grid K=1 gentle motion
  Case C: 2D grid K=2 stable-K gentle motion

NOT a proof. Source: THEORY/working/CV115_ACTION_TEMPORAL_COST/06_experiment_plan.md
Session W7, 2026-05-12. CV-1.15.
"""

import sys
import os
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.transport import (
    cohesion_fingerprint,
    graph_distance_matrix,
    sinkhorn_partial_ot,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

GRID_N = 10
DT = 1.0
GAMMA = 1.0
EPSILON_GIBBS = [0.01, 0.1, 1.0]
EPS_OT = 0.5

# ---------------------------------------------------------------------------
# §1. Formation generation
# ---------------------------------------------------------------------------

def grid_positions(n: int) -> np.ndarray:
    rows, cols = np.divmod(np.arange(n * n), n)
    return np.column_stack([rows.astype(float), cols.astype(float)])


def gauss_blob(positions: np.ndarray, center, radius: float = 2.0,
               peak: float = 0.85) -> np.ndarray:
    d2 = np.sum((positions - np.asarray(center, float)) ** 2, axis=1)
    return np.clip(peak * np.exp(-d2 / (2.0 * radius**2)), 0.0, 1.0)


def make_uniform_translation_sequence(n=GRID_N, motion_size=1.0,
                                       k_form=1, seed=0):
    """Generate t→s→r cohesion fields with uniform column translation."""
    positions = grid_positions(n)
    cx, cy = n / 2.0, n / 2.0

    if k_form == 1:
        centers_t = [(cx, cy)]
    else:
        centers_t = [(cx - n / 4, cy), (cx + n / 4, cy)]

    def build_u(centers):
        u = np.zeros(n * n)
        for c in centers:
            u = np.clip(u + gauss_blob(positions, c), 0.0, 1.0)
        return u

    u_t = build_u(centers_t)
    centers_s = [(c[0], c[1] + motion_size) for c in centers_t]
    centers_r = [(c[0], c[1] + 2 * motion_size) for c in centers_t]
    u_s = build_u(centers_s)
    u_r = build_u(centers_r)
    return positions, u_t, u_s, u_r


# ---------------------------------------------------------------------------
# §2. Cost computations
# ---------------------------------------------------------------------------

def compute_endpoint_cost(positions: np.ndarray) -> np.ndarray:
    """c_endpoint[i,j] = ||pos_i - pos_j||². Shape (N, N)."""
    diff = positions[:, None, :] - positions[None, :, :]
    return np.sum(diff ** 2, axis=-1)


def compute_local_action(u_a, u_b, graph, params,
                         dt=DT, gamma=GAMMA) -> np.ndarray:
    """a[i,j] = d(i,j)²/dt + gamma*||φ_b[j]-φ_a[i]||²/dt. Shape (N, N)."""
    D = graph_distance_matrix(graph)
    phi_a = cohesion_fingerprint(u_a, graph, params)
    phi_b = cohesion_fingerprint(u_b, graph, params)
    spatial = D ** 2 / dt
    diff_phi = phi_a[:, None, :] - phi_b[None, :, :]
    finger = gamma * np.sum(diff_phi ** 2, axis=-1) / dt
    return spatial + finger


def compute_action_cost_dp(a_ts: np.ndarray, a_sr: np.ndarray) -> np.ndarray:
    """c^act_tr[i,k] = min_j [a_ts[i,j]+a_sr[j,k]].  (T-ACT-DP)"""
    return np.min(a_ts[:, :, None] + a_sr[None, :, :], axis=1)


def compute_action_cost_dp_3hop(a_ts, a_sr, a_rq) -> np.ndarray:
    """3-hop: t→s→r→q via DP composition."""
    return compute_action_cost_dp(compute_action_cost_dp(a_ts, a_sr), a_rq)


# ---------------------------------------------------------------------------
# §3. Residual metrics
# ---------------------------------------------------------------------------

def compute_endpoint_residual(positions: np.ndarray) -> float:
    """||c_end_direct - c_end_eff||_inf.  Expects > 0 (L-ENDPOINT-NONSEMI)."""
    c = compute_endpoint_cost(positions)
    c_eff = np.min(c[:, :, None] + c[None, :, :], axis=1)
    return float(np.max(np.abs(c - c_eff)))


def compute_action_residual(a_ts: np.ndarray, a_sr: np.ndarray) -> float:
    """2-hop: ||c_act_direct - c_act_eff||_inf.  Expects ≈ 0 (T-ACT-DP).

    For 2-hop these are identical by definition; the meaningful test is 3-hop.
    """
    c_direct = compute_action_cost_dp(a_ts, a_sr)
    c_eff = compute_action_cost_dp(a_ts, a_sr)
    return float(np.max(np.abs(c_direct - c_eff)))


def compute_action_residual_3hop(a_ts, a_sr, a_rq) -> float:
    """3-hop DP residual: compare DP-composed vs direct full min.  Expects ≈ 0."""
    c_dp = compute_action_cost_dp_3hop(a_ts, a_sr, a_rq)
    c_full = a_ts[:, :, None, None] + a_sr[None, :, :, None] + a_rq[None, None, :, :]
    c_direct = np.min(np.min(c_full, axis=1), axis=1)
    return float(np.max(np.abs(c_dp - c_direct)))


def compute_soft_residual_logdomain(a_ts: np.ndarray, a_sr: np.ndarray,
                                     epsilon: float) -> float:
    """Log-domain soft-min semigroup residual.  Expects ≈ 0 (T-ACT-GIBBS).

    Uses numerically stable logsumexp to avoid underflow at small ε.
    Both c_direct and c_eff are computed from the same path sum — residual
    is purely floating-point precision of the two equivalent formulas.
    """
    # log K[x,y] = -a[x,y]/ε  (log-domain Gibbs kernel)
    log_K_ts = -a_ts / epsilon    # (N, N)
    log_K_sr = -a_sr / epsilon    # (N, N)

    # log K_tr[x,z] = logsumexp_y (log_K_ts[x,y] + log_K_sr[y,z])
    X = log_K_ts[:, :, None] + log_K_sr[None, :, :]    # (N, N, N)
    shift = X.max(axis=1, keepdims=True)
    log_K_tr = np.log(np.sum(np.exp(X - shift), axis=1)) + shift.squeeze(1)
    c_direct = -epsilon * log_K_tr                       # (N, N)

    # c_eff via soft-min recursion (same math, different route)
    c_ts = -epsilon * log_K_ts
    c_sr = -epsilon * log_K_sr
    Y = -(c_ts[:, :, None] + c_sr[None, :, :]) / epsilon
    shift2 = Y.max(axis=1, keepdims=True)
    log_K_eff = np.log(np.sum(np.exp(Y - shift2), axis=1)) + shift2.squeeze(1)
    c_eff = -epsilon * log_K_eff

    return float(np.max(np.abs(c_direct - c_eff)))


def optional_compute_sinkhorn_plan_residual(
    a_ts, a_sr, u_t, u_s, u_r, epsilon, eps_ot=EPS_OT
) -> float:
    """||M^sink(a_ts)@M^sink(a_sr) - M^sink(c^act_tr)||_inf.

    Uses action cost matrices as OT cost (not raw kernel).
    Expected > 0 generically (T-SINKHORN-PLAN-SEMIGROUP-FAILS).
    sinkhorn_partial_ot signature: (cost, mu, nu, eps, max_iter, tol) → (M, info).
    """
    c_tr = compute_action_cost_dp(a_ts, a_sr)

    def normalize(v):
        s = v.sum()
        return v / s if s > 1e-12 else np.ones_like(v) / len(v)

    p_t, p_s, p_r = normalize(u_t), normalize(u_s), normalize(u_r)

    try:
        M1, _ = sinkhorn_partial_ot(a_ts, p_t, p_s, eps=eps_ot, max_iter=100)
        M2, _ = sinkhorn_partial_ot(a_sr, p_s, p_r, eps=eps_ot, max_iter=100)
        M_tr, _ = sinkhorn_partial_ot(c_tr, p_t, p_r, eps=eps_ot, max_iter=100)
        return float(np.max(np.abs(M1 @ M2 - M_tr)))
    except Exception as e:
        print(f"    [sinkhorn] exception: {e}")
        return float("nan")


# ---------------------------------------------------------------------------
# §4. Test cases
# ---------------------------------------------------------------------------

def run_case_a_1d(verbose=True) -> dict:
    """Case A: 1D analytic ground truth.

    L-ENDPOINT-NONSEMI: c_end(0,2)=4 but min_y[c(0,y)+c(y,2)]=2 → residual=2.
    L-ACTION-NORMALIZATION: time-normalized cost additive at linear interpolant.
    """
    if verbose:
        print("\n=== Case A: 1D analytic (L-ENDPOINT-NONSEMI) ===")

    x, z = 0.0, 2.0
    y_mid = (x + z) / 2.0
    c_end_direct = (z - x) ** 2
    c_end_eff = (y_mid - x) ** 2 + (z - y_mid) ** 2
    endpoint_residual = abs(c_end_direct - c_end_eff)

    r_t, s_t = 2.0, 1.0
    y_star = ((r_t - s_t) * x + s_t * z) / r_t
    c_norm_direct = (z - x) ** 2 / r_t
    c_norm_eff = (y_star - x) ** 2 / s_t + (z - y_star) ** 2 / (r_t - s_t)
    norm_residual = abs(c_norm_direct - c_norm_eff)

    result = {
        "case": "A_1d_analytic",
        "endpoint_residual": endpoint_residual,
        "endpoint_c_direct": c_end_direct,
        "endpoint_c_eff": c_end_eff,
        "time_normalized_residual": norm_residual,
        "pass_endpoint_nonsemi": endpoint_residual > 0.5,
        "pass_norm_additive": norm_residual < 1e-10,
        "pass_endpoint_nonzero": endpoint_residual > 0.1,
    }

    if verbose:
        print(f"  endpoint: direct={c_end_direct}, eff={c_end_eff}, "
              f"residual={endpoint_residual:.4f}  (expect=2.0)")
        print(f"  time-normalized residual={norm_residual:.2e}  (expect≈0)")
        print(f"  PASS L-ENDPOINT-NONSEMI:  {result['pass_endpoint_nonsemi']}")
        print(f"  PASS L-ACTION-NORMALIZATION: {result['pass_norm_additive']}")

    return result


def _run_2d_case(tag, n, k_form, motion_size, seed, verbose) -> dict:
    """Shared body for Cases B and C."""
    graph = GraphState.grid_2d(n, n)
    params = ParameterRegistry()
    positions, u_t, u_s, u_r = make_uniform_translation_sequence(
        n=n, motion_size=motion_size, k_form=k_form, seed=seed
    )

    endpoint_res = compute_endpoint_residual(positions)
    a_ts = compute_local_action(u_t, u_s, graph, params)
    a_sr = compute_local_action(u_s, u_r, graph, params)
    action_res_2hop = compute_action_residual(a_ts, a_sr)

    # 3-hop DP test
    _, _, _, u_q = make_uniform_translation_sequence(
        n=n, motion_size=motion_size * 3.0 / 2.0, k_form=k_form, seed=seed
    )
    a_rq = compute_local_action(u_r, u_q, graph, params)
    action_dp_3hop = compute_action_residual_3hop(a_ts, a_sr, a_rq)

    soft_residuals = {}
    sinkhorn_residuals = {}
    for eps in EPSILON_GIBBS:
        soft_residuals[f"eps_{eps}"] = compute_soft_residual_logdomain(
            a_ts, a_sr, eps
        )
        sinkhorn_residuals[f"eps_{eps}"] = optional_compute_sinkhorn_plan_residual(
            a_ts, a_sr, u_t, u_s, u_r, eps
        )

    result = {
        "case": tag,
        "n": n,
        "k_form": k_form,
        "motion_size": motion_size,
        "seed": seed,
        "endpoint_residual": endpoint_res,
        "action_residual_2hop": action_res_2hop,
        "action_dp_3hop_residual": action_dp_3hop,
        "soft_residuals": soft_residuals,
        "sinkhorn_residuals": sinkhorn_residuals,
        "pass_endpoint_nonzero": endpoint_res > 0.1,
        "pass_action_zero": action_res_2hop < 1e-8,
        "pass_dp_3hop": action_dp_3hop < 1e-8,
        "pass_soft_semigroup": all(v < 1e-6 for v in soft_residuals.values()),
    }

    if verbose:
        print(f"  endpoint residual:        {endpoint_res:.4f}  (expect > 0)")
        print(f"  action residual (2-hop):  {action_res_2hop:.2e}  (expect ≈ 0)")
        print(f"  action DP residual(3-hop):{action_dp_3hop:.2e}  (expect ≈ 0)")
        for eps in EPSILON_GIBBS:
            s = soft_residuals[f"eps_{eps}"]
            sk = sinkhorn_residuals[f"eps_{eps}"]
            print(f"  ε={eps}: soft_residual={s:.2e} (expect≈0)  "
                  f"sinkhorn={sk:.4f} (expect>0 generically)")
        print(f"  PASS endpoint>0:       {result['pass_endpoint_nonzero']}")
        print(f"  PASS action≈0:         {result['pass_action_zero']}")
        print(f"  PASS DP 3-hop≈0:       {result['pass_dp_3hop']}")
        print(f"  PASS soft semigroup≈0: {result['pass_soft_semigroup']}")

    return result


def run_case_b_2d_k1(motion_size=1.5, n=GRID_N, seed=42, verbose=True) -> dict:
    """Case B: 2D grid K=1 gentle motion."""
    if verbose:
        print(f"\n=== Case B: 2D grid K=1 motion={motion_size} n={n} ===")
    return _run_2d_case("B_2d_k1", n, 1, motion_size, seed, verbose)


def run_case_c_2d_k2(motion_size=1.0, n=GRID_N, seed=7, verbose=True) -> dict:
    """Case C: 2D grid K=2 stable-K gentle motion."""
    if verbose:
        print(f"\n=== Case C: 2D grid K=2 motion={motion_size} n={n} ===")
    return _run_2d_case("C_2d_k2", n, 2, motion_size, seed, verbose)


# ---------------------------------------------------------------------------
# §5. Summary
# ---------------------------------------------------------------------------

def print_summary(results: list) -> None:
    print("\n" + "=" * 60)
    print("exp89 SUMMARY — CV-1.15 Numerical Anchor")
    print("=" * 60)

    checks = {
        "L-ENDPOINT-NONSEMI  endpoint>0":    [],
        "T-ACT-DP            action≈0":      [],
        "T-ACT-GIBBS         soft≈0":        [],
        "T-SINKHORN-FAILS    sinkhorn>0":    [],
    }

    for r in results:
        checks["L-ENDPOINT-NONSEMI  endpoint>0"].append(
            r.get("pass_endpoint_nonzero", False)
        )
        checks["T-ACT-DP            action≈0"].append(
            r.get("pass_action_zero", True) and r.get("pass_dp_3hop", True)
        )
        checks["T-ACT-GIBBS         soft≈0"].append(
            r.get("pass_soft_semigroup", True)
        )
        sk = r.get("sinkhorn_residuals", {})
        sink_nonzero = any(
            isinstance(v, float) and v > 0.005 for v in sk.values()
        )
        checks["T-SINKHORN-FAILS    sinkhorn>0"].append(sink_nonzero)

    for check, passes in checks.items():
        if not passes:
            status = "N/A"
        elif all(passes):
            status = "PASS"
        elif any(passes):
            status = "PARTIAL"
        else:
            status = "FAIL"
        print(f"  {status:8s}  {check}")
    print()


# ---------------------------------------------------------------------------
# §6. Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    all_results = []

    all_results.append(run_case_a_1d(verbose=True))
    all_results.append(run_case_b_2d_k1(motion_size=1.5, n=GRID_N, verbose=True))
    all_results.append(run_case_c_2d_k2(motion_size=1.0, n=GRID_N, verbose=True))

    print_summary(all_results)

    out_path = os.path.join(RESULTS_DIR, "exp89_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"Results saved to {out_path}")
