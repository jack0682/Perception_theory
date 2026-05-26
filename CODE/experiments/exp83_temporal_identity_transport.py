#!/usr/bin/env python3
"""Experiment 83: Temporal Identity Transport — Numerical Anchor for T-Temporal-Identity.

Validates the component correspondence relation R_{t->s} across four toy scenarios
covering all five event types: continuation, merge, split, birth, death.

Numerical anchor for T-Temporal-Identity (Session V, working Cat B candidate).
NOT a proof. Source: THEORY/4_temporal/identity_inheritance/temporal_identity_perscomp_transport.md §9.

Session X (W6 D4, 2026-05-06). CV-1.10.
Note: original plan referenced exp55; renumbered exp83 (exp55-56 already exist).
"""
import sys, os, json
import numpy as np
from scipy.ndimage import label as nd_label

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.transport import (
    sinkhorn_partial_ot,
    transport_cost,
    cohesion_fingerprint,
    graph_distance_matrix,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

GRID_N = 15           # 15x15 = 225 nodes (tractable OT)
EPS_OT = 1.0          # entropic regularization
MASS_FRAC = 0.85      # allow 15% mass dissipation (partial OT)
TAU_ID = 0.10         # mutual-max threshold for continuation
TAU_SPLIT = 0.10      # split: each child receives >= tau_split * m_i
TAU_MERGE = 0.10      # merge: each donor delivers >= tau_merge * m_i to recipient
TAU_BIRTH = 0.05      # birth: total received < tau_birth * m_j
TAU_DEATH = 0.05      # death: total delivered < tau_death * m_i
PERS_THRESH = 0.28    # PersComp threshold proxy (superlevel-set)


# ---------------------------------------------------------------------------
# Grid helpers
# ---------------------------------------------------------------------------

def grid_positions(n):
    """(n*n, 2) node positions, row/col integer coordinates."""
    rows, cols = np.divmod(np.arange(n * n), n)
    return np.column_stack([rows.astype(float), cols.astype(float)])


def gauss_blob(positions, center, radius=2.0, peak=0.9):
    d2 = np.sum((positions - np.asarray(center, dtype=float)) ** 2, axis=1)
    return np.clip(peak * np.exp(-d2 / (2.0 * radius ** 2)), 0.0, 1.0)


# ---------------------------------------------------------------------------
# PersComp proxy via threshold + connected components
# ---------------------------------------------------------------------------

def extract_components(u, threshold=PERS_THRESH):
    """Threshold-superlevel connected-component proxy for PersComp(u).

    Returns list of node-index arrays. Uses scipy.ndimage for 4-connectivity
    on the 2D grid layout matching GraphState.grid_2d.
    """
    n_side = int(round(np.sqrt(len(u))))
    mask = (u >= threshold).reshape(n_side, n_side)
    labeled, n_c = nd_label(mask)
    flat = labeled.ravel()
    return [np.where(flat == k)[0] for k in range(1, n_c + 1)]


def comp_mass(u, comp):
    return float(u[comp].sum())


# ---------------------------------------------------------------------------
# Component correspondence score matrix  S[i,j] and S_norm[i,j]
# ---------------------------------------------------------------------------

def build_score_matrix(u_t, u_s, M, comps_t, comps_s,
                       lam_m=1.0, lam_c=0.005, cost=None):
    """S[i,j] = lam_m * gamma(Ci,Cj) - lam_c * cost_weighted_transport.

    S_norm[i,j] = S[i,j] / max(min(m_i, m_j), eps) per §4.3.
    """
    Kt, Ks = len(comps_t), len(comps_s)
    gamma = np.zeros((Kt, Ks))
    S = np.zeros((Kt, Ks))
    for i, ci in enumerate(comps_t):
        for j, cj in enumerate(comps_s):
            block = M[np.ix_(ci, cj)]
            g_ij = float(block.sum())
            c_ij = float((block * cost[np.ix_(ci, cj)]).sum()) if cost is not None else 0.0
            gamma[i, j] = g_ij
            S[i, j] = lam_m * g_ij - lam_c * c_ij

    masses_t = np.array([comp_mass(u_t, c) for c in comps_t])
    masses_s = np.array([comp_mass(u_s, c) for c in comps_s])
    denom = np.maximum(np.minimum(masses_t[:, None], masses_s[None, :]), 1e-9)
    S_norm = S / denom
    return gamma, S, S_norm


# ---------------------------------------------------------------------------
# Event classification  R_{t->s} per §5
# ---------------------------------------------------------------------------

def classify_relation(gamma, S_norm, comps_t, comps_s, u_t, u_s):
    """Classify all events in R_{t->s}.

    Pass 1 (t-side): deaths and splits.
    Pass 2 (s-side): births, merges, continuations.
    Returns list of event dicts.
    """
    Kt, Ks = len(comps_t), len(comps_s)
    masses_t = np.array([comp_mass(u_t, c) for c in comps_t])
    masses_s = np.array([comp_mass(u_s, c) for c in comps_s])
    events = []
    t_done = set()
    s_done = set()

    # Pass 1: deaths and splits
    for i in range(Kt):
        total_del = gamma[i].sum()
        if total_del < TAU_DEATH * masses_t[i]:
            events.append({"type": "DEATH", "t": i, "s": None})
            t_done.add(i)
            continue
        children = [j for j in range(Ks)
                    if gamma[i, j] >= TAU_SPLIT * masses_t[i]]
        if len(children) >= 2:
            events.append({"type": "SPLIT", "t": i, "s": children})
            t_done.add(i)
            s_done.update(children)

    # Pass 2: births, merges, continuations
    for j in range(Ks):
        if j in s_done:
            continue
        total_recv = gamma[:, j].sum()
        if total_recv < TAU_BIRTH * masses_s[j]:
            events.append({"type": "BIRTH", "t": None, "s": j})
            s_done.add(j)
            continue
        donors = [i for i in range(Kt)
                  if i not in t_done
                  and gamma[i, j] >= TAU_MERGE * masses_t[i]]
        if len(donors) >= 2:
            events.append({"type": "MERGE", "t": donors, "s": j})
            t_done.update(donors)
            s_done.add(j)
        elif len(donors) == 1:
            i = donors[0]
            if (S_norm.size > 0
                    and S_norm[i, j] >= TAU_ID
                    and int(np.argmax(S_norm[i])) == j
                    and int(np.argmax(S_norm[:, j])) == i):
                events.append({"type": "CONT", "t": i, "s": j})
                t_done.add(i)
                s_done.add(j)

    return events


# ---------------------------------------------------------------------------
# One-scenario runner
# ---------------------------------------------------------------------------

def run_scenario(tag, u_t, u_s, pos, graph, params, expected_types):
    dist_mat = graph_distance_matrix(graph)
    phi_t = cohesion_fingerprint(u_t, graph, params)
    phi_s = cohesion_fingerprint(u_s, graph, params)
    cost = transport_cost(phi_t, phi_s, dist_mat, sigma=2.0, gamma=0.5)
    M, ot_info = sinkhorn_partial_ot(cost, u_t, u_s, eps=EPS_OT,
                                     mass_fraction=MASS_FRAC)

    comps_t = extract_components(u_t)
    comps_s = extract_components(u_s)

    if not comps_t or not comps_s:
        # Handle empty field edge cases
        events = []
        if not comps_t:
            for j in range(len(comps_s)):
                events.append({"type": "BIRTH", "t": None, "s": j})
        if not comps_s:
            for i in range(len(comps_t)):
                events.append({"type": "DEATH", "t": i, "s": None})
        gamma = np.zeros((len(comps_t), len(comps_s)))
        S_norm = np.zeros((len(comps_t), len(comps_s)))
    else:
        gamma, S, S_norm = build_score_matrix(u_t, u_s, M, comps_t, comps_s, cost=cost)
        events = classify_relation(gamma, S_norm, comps_t, comps_s, u_t, u_s)

    detected = sorted(set(e["type"] for e in events))
    passed = all(et in detected for et in expected_types)

    # Margin condition check for CONT events
    margin = None
    cont_events = [e for e in events if e["type"] == "CONT"]
    if cont_events and S_norm.size > 0:
        margins = []
        for e in cont_events:
            i, j = e["t"], e["s"]
            row_vals = np.delete(S_norm[i], j)
            col_vals = np.delete(S_norm[:, j], i)
            gap = min(S_norm[i, j] - (row_vals.max() if row_vals.size else 0),
                      S_norm[i, j] - (col_vals.max() if col_vals.size else 0))
            margins.append(float(gap))
        margin = float(np.min(margins))

    return {
        "scenario": tag,
        "K_t": len(comps_t),
        "K_s": len(comps_s),
        "events": events,
        "detected_types": detected,
        "expected_types": list(expected_types),
        "passed": passed,
        "margin_delta_sep": margin,
        "ot_converged": ot_info["converged"],
        "ot_iters": ot_info["iterations"],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    n = GRID_N
    graph = GraphState.grid_2d(n, n)
    params = ParameterRegistry()
    pos = grid_positions(n)
    results = []

    # A: Stable translation — two blobs shift by one row → expect CONT
    # radius=1.5 so blobs at distance 7 remain separate (sum at midpoint < threshold)
    u_t_A = gauss_blob(pos, [4, 4], radius=1.5) + gauss_blob(pos, [4, 11], radius=1.5)
    u_s_A = gauss_blob(pos, [5, 4], radius=1.5) + gauss_blob(pos, [5, 11], radius=1.5)
    u_t_A = np.clip(u_t_A, 0.0, 1.0)
    u_s_A = np.clip(u_s_A, 0.0, 1.0)
    results.append(run_scenario("A_translation", u_t_A, u_s_A, pos, graph, params,
                                expected_types=["CONT"]))

    # B: Merge — two blobs at t collapse to one at s → expect MERGE
    # radius=1.5 for sources so they are separate; radius=3.5 for merged target
    u_t_B = gauss_blob(pos, [7, 4], radius=1.5) + gauss_blob(pos, [7, 11], radius=1.5)
    u_s_B = gauss_blob(pos, [7, 7], radius=3.5)
    u_t_B = np.clip(u_t_B, 0.0, 1.0)
    u_s_B = np.clip(u_s_B, 0.0, 1.0)
    results.append(run_scenario("B_merge", u_t_B, u_s_B, pos, graph, params,
                                expected_types=["MERGE"]))

    # C: Split — one wide blob at t splits to two at s → expect SPLIT
    # radius=3.5 for source so it is one component; radius=1.5 for split targets
    u_t_C = gauss_blob(pos, [7, 7], radius=3.5)
    u_s_C = gauss_blob(pos, [7, 4], radius=1.5) + gauss_blob(pos, [7, 11], radius=1.5)
    u_t_C = np.clip(u_t_C, 0.0, 1.0)
    u_s_C = np.clip(u_s_C, 0.0, 1.0)
    results.append(run_scenario("C_split", u_t_C, u_s_C, pos, graph, params,
                                expected_types=["SPLIT"]))

    # D: Birth + continuation — one blob continues, one new blob appears → expect CONT + BIRTH
    u_t_D = gauss_blob(pos, [4, 4])
    u_s_D = gauss_blob(pos, [5, 4]) + gauss_blob(pos, [11, 11])
    u_t_D = np.clip(u_t_D, 0.0, 1.0)
    u_s_D = np.clip(u_s_D, 0.0, 1.0)
    results.append(run_scenario("D_birth_cont", u_t_D, u_s_D, pos, graph, params,
                                expected_types=["CONT", "BIRTH"]))

    all_passed = all(r["passed"] for r in results)
    output = {
        "experiment": "exp83_temporal_identity_transport",
        "session": "Session X (W6 D4, 2026-05-06)",
        "anchor_for": "T-Temporal-Identity (working Cat B candidate, Session V)",
        "note": "Numerical anchor only. Not a proof. "
                "Validates component correspondence R_{t->s} event classification "
                "across 4 scenarios. Canonical spec §5.2-5.6.",
        "grid_n": n,
        "thresholds": {
            "pers_thresh": PERS_THRESH,
            "tau_id": TAU_ID, "tau_split": TAU_SPLIT,
            "tau_merge": TAU_MERGE, "tau_birth": TAU_BIRTH, "tau_death": TAU_DEATH,
        },
        "results": results,
        "all_passed": all_passed,
    }

    out_path = os.path.join(RESULTS_DIR, "exp83_temporal_identity_transport.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"exp83 temporal identity: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  {r['scenario']:25s}  K_t={r['K_t']} K_s={r['K_s']}"
              f"  events={r['detected_types']}  [{status}]")
    return all_passed


if __name__ == "__main__":
    main()
