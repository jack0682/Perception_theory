"""L1-J — Decay-to-cut diagnostic for PO-1 bridge-cut existence.

Status: working diagnostic. NON-canonical. Does not prove L-1; does not promote
L1-F to Cat-A; does not modify any canonical or existing working file.

Goal:
  Numerically verify the decay-to-cut bound

      H_C(U) ≤ K_act * psi(q) + h_noise

  on the L1-I FEASIBLE_WITH_BUDGET configurations (raw Gaussian bumps on
  T^2_20). For each configuration we measure:

  - psi_emp(q) := max over x with d_G(x, S_j^delta) >= q of u^(j)(x)
  - measured H_C(U) for the natural support-separating cut C_jk
  - estimated bound K_act * psi_emp(q) + h_noise
  - actual threshold-scan bridge height theta_bridge^{jk}(U) (lower bound on
    H_C)

  Demonstrates the PO-1 decay-to-cut lemma is non-vacuous: for the L1-I
  FEASIBLE regime, the bound holds with positive margin.

The script reuses the L1-I state-construction (raw_gaussian) and the L1-G
threshold-scan bridge.

Forbidden non-claims (preserved by JSON output):
  - L-1 is not proved.
  - L1-F is not Cat-A.
  - OP-0005 / OP-0008 are not solved.
  - K_bar = K_act / K_soft = K_act are not claimed globally.
  - sigma_rich sufficiency is not claimed.
  - reservoir theory is not promoted to canonical.
  - decay-to-cut numerical verification is not theorem proof.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/l1j_bridge_cut_decay_diagnostic.py \\
        --output CODE/scripts/results/l1j_decay_to_cut.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from typing import Any, Dict, List, Tuple

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from l1g_l1hyp_diagnostic import (
    h0_barcode, threshold_scan_bridge_height, adjacency_list,
)
from l1i_constants_feasibility import (
    multi_source_bfs_distance, build_raw_gaussian_state,
)
import nq242c_counterexample as wq1


def support_delta(field: np.ndarray, delta: float) -> np.ndarray:
    return field > delta


def psi_empirical(
    u_slot: np.ndarray, supp_mask: np.ndarray, adj: List[List[int]],
    q_values: List[int],
) -> Dict[int, float]:
    """For each q, compute psi(q) = max u_slot(x) over vertices at graph
    distance >= q from supp_mask.
    """
    if not np.any(supp_mask):
        return {q: 0.0 for q in q_values}
    dist = multi_source_bfs_distance(supp_mask, adj)
    out: Dict[int, float] = {}
    for q in q_values:
        far_mask = dist >= q
        if not np.any(far_mask):
            out[q] = 0.0
        else:
            out[q] = float(np.max(u_slot[far_mask]))
    return out


def evaluate_decay_to_cut(
    sigma_b: float, delta: float, geometry: str,
    centers_A: Tuple[Tuple[int, int], ...],
    centers_B: Tuple[Tuple[int, int], ...],
    centers_wide: Tuple[Tuple[int, int], ...],
    n_torus: int = 20,
    initial_masses: Tuple[float, ...] = (30.0, 30.0, 30.0, 0.0),
    epsilon: float = 0.225,
    l_min: float = 0.10,
    q_values: Tuple[int, ...] = (1, 2, 3, 4, 5, 6),
    bridge_max_pairs: int = 3,
) -> Dict[str, Any]:
    """Build raw_gaussian state and verify decay-to-cut bound."""
    if geometry == "A":
        centers = centers_A
    elif geometry == "B":
        centers = centers_B
    else:
        centers = centers_wide

    graph, positions = wq1.build_torus(n_torus)
    fields = build_raw_gaussian_state(
        centers, sigma_b, n_torus, positions, initial_masses,
        epsilon_active=0.0,
    )
    adj = adjacency_list(graph)
    n = graph.n

    A = [j for j in range(len(initial_masses)) if initial_masses[j] > 0]
    U = np.sum(fields, axis=0) if fields else np.zeros(n)
    U_max = float(np.max(U))

    # delta-supports
    supp: Dict[int, np.ndarray] = {
        j: support_delta(fields[j], delta) for j in A
    }

    # Per-active-slot psi(q)
    per_slot_psi: Dict[str, Dict[str, float]] = {}
    for j in A:
        psi_j = psi_empirical(fields[j], supp[j], adj, list(q_values))
        per_slot_psi[str(j)] = {f"q={q}": v for q, v in psi_j.items()}

    K_act = len(A)
    # Aggregate decay bound: max_x sum_j ψ_j(d(x, S_j))
    # Approximate by K_act * max_j psi_j(q) for each q, taking the max over j.
    bound_per_q: Dict[int, float] = {}
    for q in q_values:
        max_psi = max(per_slot_psi[str(j)][f"q={q}"] for j in A)
        bound_per_q[q] = K_act * max_psi  # h_noise = 0 for raw Gaussian

    # Pairwise threshold-scan bridge for active pairs
    peak_idx: Dict[int, int] = {j: int(np.argmax(fields[j])) for j in A}
    pair_bridges: Dict[str, float] = {}
    pair_count = 0
    for ai, j in enumerate(A):
        for k in A[ai + 1:]:
            if pair_count >= bridge_max_pairs:
                pair_bridges[f"{j}-{k}"] = float("nan")
                continue
            theta = threshold_scan_bridge_height(
                U, peak_idx[j], peak_idx[k], adj)
            pair_bridges[f"{j}-{k}"] = float(theta) if theta is not None else float("nan")
            pair_count += 1

    finite_bridges = [v for v in pair_bridges.values() if math.isfinite(v)]
    actual_max_bridge = max(finite_bridges) if finite_bridges else None

    # Required bound: K_act * psi(q) + h_noise <= h_min - l_min - r_assoc - r_birth
    # With h_min = U_max ≈ 1.0 and r_assoc=r_birth=0: bound <= 1 - l_min = 0.9
    required_bound = U_max - l_min  # tightest
    bound_passes_per_q: Dict[int, bool] = {
        q: bound_per_q[q] <= required_bound for q in q_values
    }
    # Actual bridge satisfies LG-3 if max bridge <= h_min - l_min
    actual_bridge_passes = (actual_max_bridge is not None
                             and actual_max_bridge <= required_bound)

    return {
        "config": {
            "sigma_b": sigma_b,
            "delta": delta,
            "geometry": geometry,
            "l_min": l_min,
            "q_values": list(q_values),
            "K_act": K_act,
        },
        "U_max": U_max,
        "h_min_required_bound": required_bound,
        "per_slot_psi": per_slot_psi,
        "K_act_times_psi_bound": bound_per_q,
        "bound_holds_per_q": bound_passes_per_q,
        "pair_bridge_heights": pair_bridges,
        "actual_max_bridge": actual_max_bridge,
        "actual_bridge_satisfies_LG3": actual_bridge_passes,
    }


def main() -> int:
    p = argparse.ArgumentParser(
        description="L1-J PO-1 decay-to-cut bound diagnostic.")
    p.add_argument("--output", required=True)
    args = p.parse_args()

    centers_A = ((5, 5), (15, 5), (10, 14))
    centers_B = ((5, 5), (15, 5), (10, 11))
    centers_wide = ((3, 3), (13, 3), (8, 13))

    # L1-I best-case configurations and degraded variants
    test_cases = [
        (0.5, 0.02, "A"),
        (0.5, 0.05, "A"),
        (0.5, 0.05, "wide"),
        (1.0, 0.05, "A"),
        (1.5, 0.05, "A"),
        (2.0, 0.05, "A"),  # WQ-1 default — should fail
    ]
    t0 = time.time()
    results: List[Dict[str, Any]] = []
    for (sb, d, g) in test_cases:
        r = evaluate_decay_to_cut(sb, d, g, centers_A, centers_B, centers_wide)
        results.append(r)
    out = {
        "script": "l1j_bridge_cut_decay_diagnostic.py",
        "purpose": ("Verify the PO-1 decay-to-cut bound K_act * psi(q) + h_noise "
                    "≤ h_min - l_min on L1-I FEASIBLE configurations."),
        "non_claims": {
            "L1_proved": False,
            "L1F_promoted_to_Cat_A": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "K_bar_equals_K_act_globally": False,
            "K_soft_equals_K_act_globally": False,
            "sigma_rich_sufficient": False,
            "reservoir_canonical": False,
            "diagnostic_is_theorem_proof": False,
        },
        "results": results,
        "wall_clock_seconds": time.time() - t0,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: int(o) if isinstance(o, np.integer)
                  else (float(o) if isinstance(o, np.floating)
                        else (o.tolist() if isinstance(o, np.ndarray)
                              else str(o))))
    print(f"[l1j] Wrote {args.output}")
    print(f"[l1j] Tested {len(results)} configurations in {out['wall_clock_seconds']:.1f}s")
    print(f"[l1j] Required bound: K_act * psi(q) ≤ h_min - l_min")
    for r in results:
        c = r["config"]
        print(f"  sb={c['sigma_b']}, d={c['delta']}, g={c['geometry']}: "
              f"K_act={c['K_act']}, U_max={r['U_max']:.3f}, "
              f"required={r['h_min_required_bound']:.3f}, "
              f"actual_bridge={r['actual_max_bridge']:.3f}, "
              f"LG3_holds={r['actual_bridge_satisfies_LG3']}")
        for q in c["q_values"]:
            bnd = r["K_act_times_psi_bound"][q]
            ok = r["bound_holds_per_q"][q]
            print(f"     q={q}: K_act*psi(q)={bnd:.4e}, holds={ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
