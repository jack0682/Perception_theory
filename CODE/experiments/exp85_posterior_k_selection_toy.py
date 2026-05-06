#!/usr/bin/env python3
"""Experiment 85: Posterior K-Selection Toy — Numerical Anchor for T-K-Select-OBS.

Validates F_obs(K) = E_SCC(u_K^*) + lambda_photo * ||u_K^* - I||^2, where
u_K^* = find_formation(u_init=sector_K_init) is the prior sector MAP.

This is the zero-temperature Method B approximation from §8.3 of
k_select_obs_posterior.md: evaluating the combined free energy at the
sector-constrained prior MAP to compare K=1 vs K=2 under observation.

Three tests:
  1. obs_2blobs:  I = two-blob image → F_obs(K=2) < F_obs(K=1)  (obs pushes K=2)
  2. obs_1blob:   I = one-blob image  → F_obs(K=1) < F_obs(K=2)  (obs pushes K=1)
  3. lambda_to_0: lambda_photo → 0   → F_obs ordering = prior E_SCC ordering

Canonical likelihood model: Phi_obs(u;O) = (lambda_photo/2)*sum_x (u(x)-f(x))^2
(uniform c=1; LM1-LM3 verified in k_select_obs_posterior.md §2.4)

Numerical anchor for T-K-Select-OBS (Session S, working Cat B candidate).
NOT a proof. Session Y (W6 D4, 2026-05-06). CV-1.11 candidate.
Note: renumbered exp85 (exp54_closure_threshold.py already exists).
"""
import sys, os, json
import numpy as np
from scipy.ndimage import label as nd_label

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, project_volume

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

GRID_N = 12           # 12x12 = 144 nodes
PERS_THRESH = 0.28    # K_act threshold proxy
LAMBDA_PHOTO = 3.0    # observation coupling
LAMBDA_SMALL = 1e-3   # near-zero coupling for lambda→0 test


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def grid_positions(n):
    rows, cols = np.divmod(np.arange(n * n), n)
    return np.column_stack([rows.astype(float), cols.astype(float)])


def gauss_blob(positions, center, sigma=2.0, peak=0.9):
    d2 = np.sum((positions - np.asarray(center, dtype=float)) ** 2, axis=1)
    return np.clip(peak * np.exp(-d2 / (2.0 * sigma ** 2)), 0.0, 1.0)


def k_act(u, n_side=GRID_N, threshold=PERS_THRESH):
    """K_act = #PersComp proxy via threshold superlevel-set CC."""
    mask = (u >= threshold).reshape(n_side, n_side)
    _, n_c = nd_label(mask)
    return int(n_c)


def f_obs(u, I_obs, lam, ec):
    """F_obs(K) = E_SCC(u) + lam * ||u - I||^2 (zero-temperature sector free energy)."""
    E, terms = ec.energy(u)
    obs_loss = float(np.sum((u - I_obs) ** 2))
    return float(E), float(E + lam * obs_loss), float(obs_loss), terms


# ---------------------------------------------------------------------------
# Sector initializations (well-separated, yielding stable K=1 and K=2 minima)
# ---------------------------------------------------------------------------

def init_k1(pos, m):
    """K=1 init: single blob at center."""
    u = gauss_blob(pos, [GRID_N // 2, GRID_N // 2], sigma=2.5)
    return project_volume(u, m)


def init_k2(pos, m):
    """K=2 init: two blobs at far corners (sigma=1.5, peak=1.0 for clean separation)."""
    u = (gauss_blob(pos, [2, 2], sigma=1.5, peak=1.0) +
         gauss_blob(pos, [9, 9], sigma=1.5, peak=1.0))
    return project_volume(np.clip(u, 0.0, 1.0), m)


def find_sector_map(graph, params, u_init):
    """Find prior sector MAP via find_formation with sector-specific init."""
    return find_formation(graph, params, u_init=u_init, allow_outside_spinodal=True)


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

def scenario_obs_2blobs(pos, graph, params, ec, m, u1_prior, u2_prior):
    """Obs→K=2: two-blob observation makes F_obs(K=2) < F_obs(K=1)."""
    I_obs = np.clip(gauss_blob(pos, [2, 2], sigma=1.5, peak=1.0) +
                    gauss_blob(pos, [9, 9], sigma=1.5, peak=1.0), 0.0, 1.0)

    E1, F1, obs1, _ = f_obs(u1_prior, I_obs, LAMBDA_PHOTO, ec)
    E2, F2, obs2, _ = f_obs(u2_prior, I_obs, LAMBDA_PHOTO, ec)

    passed = bool(F2 < F1)
    return {
        "scenario": "obs_2blobs",
        "K1_act": k_act(u1_prior), "K2_act": k_act(u2_prior),
        "E_scc_K1": E1, "E_scc_K2": E2,
        "obs_loss_K1": obs1, "obs_loss_K2": obs2,
        "F_obs_K1": F1, "F_obs_K2": F2,
        "delta_F": float(F1 - F2),      # positive → K=2 preferred
        "lambda_photo": float(LAMBDA_PHOTO),
        "passed": passed,
        "note": "Two-blob obs: F_obs(K=2) < F_obs(K=1) required (obs matches K=2 MAP)",
    }


def scenario_obs_1blob(pos, graph, params, ec, m, u1_prior, u2_prior):
    """Obs→K=1: one-blob observation makes F_obs(K=1) < F_obs(K=2)."""
    I_obs = gauss_blob(pos, [GRID_N // 2, GRID_N // 2], sigma=3.0)

    E1, F1, obs1, _ = f_obs(u1_prior, I_obs, LAMBDA_PHOTO, ec)
    E2, F2, obs2, _ = f_obs(u2_prior, I_obs, LAMBDA_PHOTO, ec)

    passed = bool(F1 < F2)
    return {
        "scenario": "obs_1blob",
        "K1_act": k_act(u1_prior), "K2_act": k_act(u2_prior),
        "E_scc_K1": E1, "E_scc_K2": E2,
        "obs_loss_K1": obs1, "obs_loss_K2": obs2,
        "F_obs_K1": F1, "F_obs_K2": F2,
        "delta_F": float(F2 - F1),      # positive → K=1 preferred
        "lambda_photo": float(LAMBDA_PHOTO),
        "passed": passed,
        "note": "One-blob obs: F_obs(K=1) < F_obs(K=2) required (obs matches K=1 MAP)",
    }


def scenario_lambda_to_zero(pos, graph, params, ec, m, u1_prior, u2_prior):
    """Lambda→0: F_obs ordering converges to pure prior E_SCC ordering."""
    # Use the two-blob observation (arbitrary choice; doesn't matter at lambda→0)
    I_obs = np.clip(gauss_blob(pos, [2, 2], sigma=1.5, peak=1.0) +
                    gauss_blob(pos, [9, 9], sigma=1.5, peak=1.0), 0.0, 1.0)

    E1, _, obs1, _ = f_obs(u1_prior, I_obs, 0.0, ec)
    E2, _, obs2, _ = f_obs(u2_prior, I_obs, 0.0, ec)
    prior_preferred = int(1 if E1 < E2 else 2)

    _, F1_s, _, _ = f_obs(u1_prior, I_obs, LAMBDA_SMALL, ec)
    _, F2_s, _, _ = f_obs(u2_prior, I_obs, LAMBDA_SMALL, ec)
    small_preferred = int(1 if F1_s < F2_s else 2)

    passed = bool(prior_preferred == small_preferred)
    return {
        "scenario": "lambda_to_zero",
        "E_scc_K1": E1, "E_scc_K2": E2,
        "prior_preferred": prior_preferred,
        "F_obs_K1_small": F1_s, "F_obs_K2_small": F2_s,
        "small_lambda_preferred": small_preferred,
        "lambda_small": float(LAMBDA_SMALL),
        "passed": passed,
        "note": "lambda→0: posterior ordering matches prior E_SCC ordering",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    n = GRID_N
    graph = GraphState.grid_2d(n, n)
    params = ParameterRegistry()
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    m = float(params.volume_fraction * n * n)
    pos = grid_positions(n)

    # Find prior sector MAPs once; reuse across all scenarios
    res1 = find_sector_map(graph, params, init_k1(pos, m))
    res2 = find_sector_map(graph, params, init_k2(pos, m))
    u1_prior, u2_prior = res1.u, res2.u

    results = [
        scenario_obs_2blobs(pos, graph, params, ec, m, u1_prior, u2_prior),
        scenario_obs_1blob(pos, graph, params, ec, m, u1_prior, u2_prior),
        scenario_lambda_to_zero(pos, graph, params, ec, m, u1_prior, u2_prior),
    ]

    all_passed = all(r["passed"] for r in results)
    output = {
        "experiment": "exp85_posterior_k_selection_toy",
        "session": "Session Y (W6 D4, 2026-05-06)",
        "anchor_for": "T-K-Select-OBS (working Cat B candidate, Session S)",
        "method": ("Method B zero-temperature: F_obs(K) = E_SCC(u_K^*) + lambda * ||u_K^*-I||^2 "
                   "evaluated at prior sector MAP u_K^* = find_formation(sector_K_init)"),
        "canonical_likelihood": (
            "Phi_obs(u;O) = (lambda_photo/2)*sum_x(u(x)-f(x))^2; "
            "LM1-LM3 verified in k_select_obs_posterior.md §2.4"
        ),
        "note": "NOT a proof of T-K-Select-OBS.",
        "grid_n": n,
        "pers_thresh": PERS_THRESH,
        "lambda_photo": float(LAMBDA_PHOTO),
        "K1_act_prior": k_act(u1_prior),
        "K2_act_prior": k_act(u2_prior),
        "E_scc_K1_prior": float(res1.energy),
        "E_scc_K2_prior": float(res2.energy),
        "results": results,
        "all_passed": all_passed,
    }

    out_path = os.path.join(RESULTS_DIR, "exp85_posterior_k_selection_toy.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"exp85 posterior K-selection: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    print(f"  Prior MAPs: K1_act={k_act(u1_prior)} E={res1.energy:.4f}, "
          f"K2_act={k_act(u2_prior)} E={res2.energy:.4f}")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        delta = r.get("delta_F", r.get("F_obs_K1_small", 0) - r.get("F_obs_K2_small", 0))
        print(f"  {r['scenario']:25s}  [{status}]  delta_F={delta:.4f}")
    return all_passed


if __name__ == "__main__":
    main()
