"""L1-G — Empirical L1Hyp Diagnostic for the L-1 hard-bar / active-count bridge.

Status: working diagnostic. NON-canonical. Does not prove L-1, does not promote
L1-F to Cat-A, does not solve OP-0005 / OP-0008.

This script computes measurable proxies for the L1Hyp clauses H1-H10 of
``THEORY/working/MF/kbar_kact_bridge_L1F_synthesis.md``, evaluated on existing
WQ-LAT-style multi-formation trajectories.

----------------------------------------------------------------------------
Operating modes
----------------------------------------------------------------------------

  --mode summary
      Read an existing diagnostic JSON (e.g. ``ksoft_kact_diag.json``) and
      compute the *subset* of L1Hyp diagnostics that depend only on summary
      statistics (m_j, K_act, K_bar, dominant_bar_lengths, pairwise_overlaps,
      min_support_distance). Diagnostics that require per-vertex u^(j)(x)
      fields are flagged NOT_MEASURABLE_FROM_CURRENT_OUTPUTS.

  --mode rerun  (default)
      Regenerate the WQ-1 (NQ-242c) configuration-A and configuration-B
      trajectories using the deterministic seed/config and access full
      per-snapshot multi-formation fields. Compute the full Level 1 set of
      L1Hyp diagnostics, plus an optional Level 2 max-min bridge height via
      threshold scan.

----------------------------------------------------------------------------
Diagnostic levels
----------------------------------------------------------------------------

Level 1 (Easy measurable proxies — implemented):
  active masses m_j; active set A^eps; K_act; aggregate U; K_bar^{l_min}(U);
  dominant bar lengths; peak heights b_j^U; residual height ||R_inact||_inf;
  secondary slot bar lengths l_{j,2}; support connectedness of S_j^delta;
  support distances d_G(S_j^delta, S_k^delta); raw margin
      h_min - max_{k!=j} B_jk - (l_min + r_assoc + r_birth)
  with B_jk estimated as the threshold-scan bridge height where feasible
  and otherwise reported as unknown.

Level 2 (Harder graph diagnostics — partially implemented):
  Threshold-scan max-min bridge height theta_bridge^jk(U) (Option B of L1F
  guidance: build superlevel graph at descending thresholds and detect when
  p_j and p_k become connected).
  EXACT min-cut height H_cut^jk and slot-to-bar association map are NOT
  implemented — they are documented as future work.

----------------------------------------------------------------------------
Outcome interpretation
----------------------------------------------------------------------------

Outcomes are classified as:
  STRONG_SUPPORT, WEAK_SUPPORT, MIXED, FAIL, INCONCLUSIVE.
  No outcome is called "proof". L1-F remains LEMMA-CAND.

----------------------------------------------------------------------------
Forbidden non-claims (preserved by this script)
----------------------------------------------------------------------------

  - L-1 is not proved.
  - L1-F is not Cat-A.
  - OP-0005 / OP-0008 are not solved.
  - K_bar = K_act is not claimed globally.
  - K_soft = K_act is not claimed globally.
  - sigma_rich sufficiency is not claimed.
  - Reservoir theory is not promoted to canonical.
  - Empirical evidence here is not treated as a theorem.

----------------------------------------------------------------------------
Usage
----------------------------------------------------------------------------

Smoke test (rerun mode, small budget)::

    PYTHONPATH=CODE python3 CODE/scripts/l1g_l1hyp_diagnostic.py \\
        --mode rerun --max_iter 200 --max_snapshots 4 \\
        --output CODE/scripts/results/l1g_l1hyp_diagnostic_smoke.json

Full diagnostic (rerun mode)::

    PYTHONPATH=CODE python3 CODE/scripts/l1g_l1hyp_diagnostic.py \\
        --mode rerun --max_iter 5000 \\
        --output CODE/scripts/results/l1g_l1hyp_diagnostic.json

Summary mode (existing JSON)::

    PYTHONPATH=CODE python3 CODE/scripts/l1g_l1hyp_diagnostic.py \\
        --mode summary \\
        --input CODE/scripts/results/ksoft_kact_diag.json \\
        --output CODE/scripts/results/l1g_l1hyp_diagnostic_from_ksoft.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import platform
import socket
import sys
import time
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# Import path setup: scripts/ first (sibling modules), then CODE/ (scc package).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


SCRIPT_VERSION = "0.1"


# ===========================================================================
# Status tags for clause measurability
# ===========================================================================

EXACTLY_MEASURABLE = "EXACTLY_MEASURABLE"
PROXY_MEASURABLE = "PROXY_MEASURABLE"
PARTIALLY_MEASURABLE = "PARTIALLY_MEASURABLE"
NOT_MEASURABLE = "NOT_MEASURABLE_FROM_CURRENT_OUTPUTS"

# Outcome tags
STRONG_SUPPORT = "STRONG_SUPPORT"
WEAK_SUPPORT = "WEAK_SUPPORT"
MIXED = "MIXED"
FAIL = "FAIL"
INCONCLUSIVE = "INCONCLUSIVE"


# ===========================================================================
# Pure topology / persistence helpers (graph-agnostic GraphState)
# ===========================================================================


def adjacency_list(graph) -> List[List[int]]:
    """Build undirected adjacency list from a GraphState."""
    n = graph.n
    W_coo = graph.W.tocoo()
    adj: List[List[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[int(i)].append(int(j))
    return adj


def h0_barcode(u: np.ndarray, graph) -> List[Tuple[float, float]]:
    """Full H_0 superlevel persistence barcode using terminal-death convention.

    Returns list of (birth, death) pairs sorted by length descending. The
    surviving (essential) component is recorded as (max(u), 0.0) — terminal
    death convention required by L1-C.
    """
    n = graph.n
    if n == 0:
        return []
    order = np.argsort(-u)
    adj = adjacency_list(graph)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    active = np.zeros(n, dtype=bool)
    bars: List[Tuple[float, float]] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        idx = int(idx)
        active[idx] = True
        birth_val[idx] = u[idx]
        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            if birth_val[ri] >= birth_val[rn]:
                bars.append((float(birth_val[rn]), float(u[idx])))
                parent[rn] = ri
            else:
                bars.append((float(birth_val[ri]), float(u[idx])))
                parent[ri] = rn

    bars.append((float(np.max(u)), 0.0))
    bars.sort(key=lambda bd: bd[0] - bd[1], reverse=True)
    return bars


def bar_lengths(barcode: List[Tuple[float, float]]) -> List[float]:
    return [b - d for (b, d) in barcode]


def k_bar(barcode: List[Tuple[float, float]], l_min: float) -> int:
    return int(sum(1 for ell in bar_lengths(barcode) if ell >= l_min))


def support_delta(field: np.ndarray, delta: float) -> np.ndarray:
    return field > delta


def induced_connected(mask: np.ndarray, adj: List[List[int]]) -> bool:
    """Is the induced subgraph on mask connected (as a single component)?"""
    nodes = np.where(mask)[0]
    if len(nodes) == 0:
        return False
    if len(nodes) == 1:
        return True
    seen = {int(nodes[0])}
    stack = [int(nodes[0])]
    while stack:
        x = stack.pop()
        for nb in adj[x]:
            if mask[nb] and nb not in seen:
                seen.add(int(nb))
                stack.append(int(nb))
    return len(seen) == int(np.sum(mask))


def n_connected_components(mask: np.ndarray, adj: List[List[int]]) -> int:
    """Number of connected components in the induced subgraph on mask."""
    nodes = np.where(mask)[0]
    if len(nodes) == 0:
        return 0
    seen = set()
    n_cc = 0
    for start in nodes:
        s = int(start)
        if s in seen:
            continue
        n_cc += 1
        seen.add(s)
        stack = [s]
        while stack:
            x = stack.pop()
            for nb in adj[x]:
                if mask[nb] and nb not in seen:
                    seen.add(int(nb))
                    stack.append(int(nb))
    return n_cc


def support_distance(mask_a: np.ndarray, mask_b: np.ndarray, adj: List[List[int]]) -> float:
    """Multi-source BFS shortest-path distance between two vertex sets.

    Returns inf if either set is empty or they are disconnected. Returns 0
    if the sets overlap.
    """
    if not np.any(mask_a) or not np.any(mask_b):
        return float("inf")
    if np.any(mask_a & mask_b):
        return 0.0
    n = len(mask_a)
    dist = np.full(n, -1, dtype=int)
    queue: List[int] = []
    for i in np.where(mask_a)[0]:
        dist[i] = 0
        queue.append(int(i))
    head = 0
    best = float("inf")
    while head < len(queue):
        x = queue[head]
        head += 1
        if mask_b[x]:
            best = min(best, float(dist[x]))
            # Continue: BFS from a multi-source frontier already gives shortest;
            # the first hit on mask_b is the answer. Break.
            return best
        for nb in adj[x]:
            if dist[nb] < 0:
                dist[nb] = dist[x] + 1
                queue.append(int(nb))
    return float("inf")


def threshold_scan_bridge_height(
    U: np.ndarray, p_j: int, p_k: int, adj: List[List[int]],
    n_thresholds: int = 50,
) -> Optional[float]:
    """Max-min bridge height theta_bridge^jk(U) via descending threshold scan.

    Sort unique values of U descending. For each threshold theta from high
    to low, mark vertex active iff U(x) >= theta and union with already-active
    neighbors. The earliest theta at which p_j and p_k lie in the same
    component is the bridge height.

    Returns None if either peak has U(p) < min(U) (degenerate) or scan
    exhausts all vertices without joining the peaks.

    Complexity: O(|X| * alpha(|X|)) using union-find.
    """
    n = len(U)
    if p_j < 0 or p_k < 0 or p_j >= n or p_k >= n:
        return None
    if p_j == p_k:
        return float(U[p_j])

    # Sort vertices by U descending. Use stable sort for determinism.
    order = np.argsort(-U, kind="stable")
    parent = np.arange(n, dtype=int)
    active = np.zeros(n, dtype=bool)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        idx = int(idx)
        active[idx] = True
        for nb in adj[idx]:
            if active[nb]:
                ri, rn = find(idx), find(nb)
                if ri != rn:
                    parent[max(ri, rn)] = min(ri, rn)
        # Check whether both peaks are now active and connected
        if active[p_j] and active[p_k] and find(int(p_j)) == find(int(p_k)):
            # Bridge height is the value of the most recently added vertex
            return float(U[idx])
    return None


# ===========================================================================
# Per-snapshot diagnostic computation (rerun mode)
# ===========================================================================


def per_snapshot_diagnostic(
    fields: List[np.ndarray],
    graph,
    adj: List[List[int]],
    epsilon: float,
    delta: float,
    l_min: float,
    bridge_max_pairs: int = 6,
) -> Dict[str, Any]:
    """Compute Level 1 + (small) Level 2 diagnostics for a single snapshot.

    Inputs
    ------
    fields : list of K per-vertex numpy arrays u^(j)(x).
    graph : GraphState (used for adjacency).
    adj : precomputed adjacency list.
    epsilon, delta, l_min : L1Hyp thresholds.

    Returns
    -------
    dict with the per-snapshot diagnostic block.
    """
    K = len(fields)
    n = graph.n

    masses = [float(f.sum()) for f in fields]
    A = [j for j, m in enumerate(masses) if m > epsilon]
    K_act = len(A)

    U = np.sum(fields, axis=0) if fields else np.zeros(n)
    U_act = np.sum([fields[j] for j in A], axis=0) if A else np.zeros(n)
    R_inact = U - U_act

    # Aggregate barcode
    bc_U = h0_barcode(U, graph)
    ells_U = bar_lengths(bc_U)
    K_bar_v = k_bar(bc_U, l_min)
    dominant_bars = sorted(ells_U, reverse=True)[: max(8, K + 2)]

    # Per-active-slot quantities
    slot_mass: Dict[str, float] = {}
    slot_peak_idx: Dict[str, int] = {}
    slot_b_U: Dict[str, float] = {}
    slot_l1: Dict[str, float] = {}
    slot_l2: Dict[str, float] = {}
    slot_support_size: Dict[str, int] = {}
    slot_support_connected: Dict[str, bool] = {}
    slot_support_n_cc: Dict[str, int] = {}

    support_masks: Dict[int, np.ndarray] = {}

    for j in A:
        f = fields[j]
        peak_idx = int(np.argmax(f))
        slot_peak_idx[str(j)] = peak_idx
        slot_b_U[str(j)] = float(U[peak_idx])
        slot_mass[str(j)] = masses[j]
        # Slot-internal barcode (full graph) and sorted lengths
        bc_j = h0_barcode(f, graph)
        ells_j = sorted(bar_lengths(bc_j), reverse=True)
        slot_l1[str(j)] = float(ells_j[0]) if ells_j else 0.0
        slot_l2[str(j)] = float(ells_j[1]) if len(ells_j) > 1 else 0.0
        # delta-support
        mask = support_delta(f, delta)
        support_masks[j] = mask
        slot_support_size[str(j)] = int(np.sum(mask))
        slot_support_n_cc[str(j)] = n_connected_components(mask, adj)
        slot_support_connected[str(j)] = (slot_support_n_cc[str(j)] == 1
                                            and slot_support_size[str(j)] > 0)

    # Pairwise support distances and threshold-scan bridge heights for active pairs
    pair_distances: Dict[str, float] = {}
    pair_bridge_heights: Dict[str, Optional[float]] = {}
    pair_count = 0
    for i_idx, j in enumerate(A):
        for k in A[i_idx + 1:]:
            key = f"{j}-{k}"
            mj = support_masks.get(j)
            mk = support_masks.get(k)
            if mj is None or mk is None:
                pair_distances[key] = float("inf")
            else:
                pair_distances[key] = float(support_distance(mj, mk, adj))
            # Threshold-scan bridge between peaks (cap on number to keep cost low)
            if pair_count < bridge_max_pairs:
                theta = threshold_scan_bridge_height(
                    U, slot_peak_idx[str(j)], slot_peak_idx[str(k)], adj)
                pair_bridge_heights[key] = theta
            else:
                pair_bridge_heights[key] = None  # not computed; capacity exceeded
            pair_count += 1

    # Inactive residual stats
    R_inf = float(np.max(R_inact)) if R_inact.size else 0.0
    bc_R = h0_barcode(R_inact, graph) if A else h0_barcode(U, graph)
    K_bar_R = k_bar(bc_R, l_min)

    # H4-like raw margin: h_min(measured) - max_{k != j} bridge - l_min
    # We use measured h_min = min_j b_j^U as h_min, and the max over pairs as the
    # effective worst-case bridge. r_assoc and r_birth are L1Hyp constants we
    # cannot estimate from data alone, so the diagnostic reports the "raw"
    # margin without those error budgets.
    if A and pair_bridge_heights:
        finite_bridges = [v for v in pair_bridge_heights.values()
                          if v is not None and math.isfinite(v)]
        max_bridge = max(finite_bridges) if finite_bridges else None
        h_min_measured = min(slot_b_U.values()) if slot_b_U else None
        if max_bridge is not None and h_min_measured is not None:
            raw_margin = h_min_measured - max_bridge - l_min
        else:
            raw_margin = None
    else:
        max_bridge = None
        h_min_measured = None
        raw_margin = None

    # Coverage proxy (H8): K_bar(U) - K_act
    coverage_excess = K_bar_v - K_act

    return {
        "K_act": K_act,
        "active_set": A,
        "K_bar": K_bar_v,
        "coverage_excess": coverage_excess,
        "dominant_bars": dominant_bars,
        "masses": masses,
        "slot_b_U": slot_b_U,
        "slot_l1": slot_l1,
        "slot_l2": slot_l2,
        "slot_support_size": slot_support_size,
        "slot_support_connected": slot_support_connected,
        "slot_support_n_cc": slot_support_n_cc,
        "pair_distances": pair_distances,
        "pair_bridge_heights": pair_bridge_heights,
        "max_bridge": max_bridge,
        "h_min_measured": h_min_measured,
        "raw_margin_h_min_minus_bridge_minus_lmin": raw_margin,
        "R_inact_inf": R_inf,
        "K_bar_R_inact": K_bar_R,
        "U_max": float(np.max(U)) if U.size else 0.0,
    }


# ===========================================================================
# Clause-by-clause classifier
# ===========================================================================


def classify_clauses(
    snap_diag: Dict[str, Any], l_min: float, mode: str,
) -> Dict[str, Dict[str, Any]]:
    """Classify each L1Hyp clause H1-H10 against the snapshot diagnostic.

    Returns a dict mapping clause name to {status, value, threshold, pass,
    note}. ``pass`` is True/False/None where None means UNKNOWN.
    """
    out: Dict[str, Dict[str, Any]] = {}

    A = snap_diag.get("active_set", [])
    K_act = snap_diag.get("K_act", 0)
    K_bar = snap_diag.get("K_bar", 0)
    R_inact_inf = snap_diag.get("R_inact_inf", float("nan"))
    K_bar_R = snap_diag.get("K_bar_R_inact", -1)

    # H1 — Active mass and support
    h1_pass: Optional[bool] = None
    if mode == "rerun":
        all_supports_ok = all(
            snap_diag["slot_support_connected"].get(str(j), False)
            and snap_diag["slot_support_size"].get(str(j), 0) > 0
            for j in A
        )
        # Pairwise separation positive (>0) for all active pairs
        positive_distances = all(
            d > 0 for d in snap_diag["pair_distances"].values()
        )
        h1_pass = bool(all_supports_ok and (positive_distances or len(A) <= 1))
        out["H1"] = {
            "status": EXACTLY_MEASURABLE,
            "value": {
                "supports_connected": dict(snap_diag["slot_support_connected"]),
                "support_sizes": dict(snap_diag["slot_support_size"]),
                "support_n_cc": dict(snap_diag["slot_support_n_cc"]),
                "pair_distances": dict(snap_diag["pair_distances"]),
            },
            "pass": h1_pass,
            "note": "Active masses + delta-supports + connectivity + graph distances.",
        }
    else:
        out["H1"] = {
            "status": PARTIALLY_MEASURABLE,
            "value": {"K_act": K_act,
                       "min_support_distance": snap_diag.get("min_support_distance")},
            "pass": None,
            "note": "Summary mode: support connectedness not measurable from JSON.",
        }

    # H2 — Birth / peak height
    if mode == "rerun":
        b_U = snap_diag.get("slot_b_U", {})
        h_min_meas = snap_diag.get("h_min_measured")
        out["H2"] = {
            "status": EXACTLY_MEASURABLE,
            "value": {"slot_b_U": dict(b_U), "h_min_measured": h_min_meas},
            "pass": (h_min_meas is not None and h_min_meas >= l_min),
            "threshold": l_min,
            "note": "Peak-based birth heights b_j^U = U(p_j); h_min is min over active slots.",
        }
    else:
        out["H2"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Summary JSON does not contain U(p_j); rerun required.",
        }

    # H3 — Low bridge via cuts
    if mode == "rerun":
        bridges = snap_diag.get("pair_bridge_heights", {})
        finite_bridges = {k: v for k, v in bridges.items()
                          if v is not None and math.isfinite(v)}
        not_computed = [k for k, v in bridges.items() if v is None]
        # Pass condition: every finite bridge below h_min - l_min margin
        h_min_meas = snap_diag.get("h_min_measured")
        if h_min_meas is None or not finite_bridges:
            h3_pass: Optional[bool] = None
        else:
            margin_target = h_min_meas - l_min
            h3_pass = all(v <= margin_target for v in finite_bridges.values())
        out["H3"] = {
            "status": PROXY_MEASURABLE,
            "value": {"pair_bridge_heights": bridges,
                       "max_bridge": snap_diag.get("max_bridge"),
                       "uncomputed_pairs": not_computed},
            "pass": h3_pass,
            "threshold": l_min,
            "note": ("Threshold-scan max-min bridge height between peaks. "
                     "Exact min-cut height H_cut^jk not implemented (Level 2 future)."),
        }
    else:
        out["H3"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Summary JSON does not contain U(x); rerun required for bridge height.",
        }

    # H4 — Persistence-margin compatibility
    if mode == "rerun":
        raw_margin = snap_diag.get("raw_margin_h_min_minus_bridge_minus_lmin")
        out["H4"] = {
            "status": PARTIALLY_MEASURABLE,
            "value": {"raw_margin": raw_margin,
                       "comment": "raw margin = h_min - max_bridge - l_min; "
                                  "r_assoc and r_birth not estimable from data."},
            "pass": (raw_margin is not None and raw_margin >= 0),
            "note": "L1Hyp constants r_assoc, r_birth not derivable empirically.",
        }
    else:
        out["H4"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Requires birth heights and bridge heights.",
        }

    # H5 — Slot-to-bar association
    out["H5"] = {
        "status": NOT_MEASURABLE,
        "value": None,
        "pass": None,
        "note": ("Stable slot-to-bar association map A_bar requires birth-vertex "
                 "tracking through superlevel filtration; not implemented (Level 2)."),
    }

    # H6 — Active secondary-bar suppression
    if mode == "rerun":
        l2 = snap_diag.get("slot_l2", {})
        # Pass condition: every active slot has l_{j,2} < l_min
        if A and l2:
            h6_pass: Optional[bool] = all(l2.get(str(j), 0.0) < l_min for j in A)
        else:
            h6_pass = None
        out["H6"] = {
            "status": PROXY_MEASURABLE,
            "value": {"slot_l2": dict(l2)},
            "pass": h6_pass,
            "threshold": l_min,
            "note": ("Slot-internal full-graph H_0 secondary bar; full local barcode "
                     "on G_j^r not implemented."),
        }
    else:
        out["H6"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Requires per-slot fields.",
        }

    # H7 — Inactive residual suppression
    if mode == "rerun":
        out["H7"] = {
            "status": PROXY_MEASURABLE,
            "value": {"R_inact_inf": R_inact_inf, "K_bar_R_inact": K_bar_R},
            "pass": (R_inact_inf < l_min and K_bar_R == 0),
            "threshold": l_min,
            "note": "Aggregate residual height + barcode on R_inact alone.",
        }
    else:
        out["H7"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Requires per-slot fields.",
        }

    # H8 — No non-slot dominant bars
    out["H8"] = {
        "status": EXACTLY_MEASURABLE,
        "value": {"K_bar_minus_K_act": K_bar - K_act,
                   "K_bar": K_bar, "K_act": K_act},
        "pass": (K_bar == K_act),
        "note": ("Exact integer count comparison. K_bar > K_act => possible "
                 "non-slot bar overcount; K_bar < K_act => undercount "
                 "(association failure)."),
    }

    # H9 — Tie/plateau stability
    # Approximate by minimum gap among (sorted) dominant bar lengths and l_min.
    if snap_diag.get("dominant_bars"):
        bars = snap_diag["dominant_bars"]
        gaps: List[float] = []
        for i in range(len(bars) - 1):
            gaps.append(abs(bars[i] - bars[i + 1]))
        for v in bars:
            gaps.append(abs(v - l_min))
        if gaps:
            min_gap = float(min(gaps))
            out["H9"] = {
                "status": PROXY_MEASURABLE,
                "value": {"min_gap_to_lmin": min_gap},
                "pass": (min_gap > 1e-6),
                "note": "Gap proxy; true tau_tie requires plateau detection on field.",
            }
        else:
            out["H9"] = {
                "status": PARTIALLY_MEASURABLE,
                "value": {"min_gap_to_lmin": None},
                "pass": None,
                "note": "No bars in this snapshot.",
            }
    else:
        out["H9"] = {
            "status": NOT_MEASURABLE,
            "value": None,
            "pass": None,
            "note": "Bars not available.",
        }

    # H10 — Local-to-global compatibility
    out["H10"] = {
        "status": NOT_MEASURABLE,
        "value": None,
        "pass": None,
        "note": ("Local-to-global barcode transfer is the central theorem-grade gap. "
                 "It cannot be empirically measured; requires proof or counterexample."),
    }

    return out


def aggregate_classification(
    clauses: Dict[str, Dict[str, Any]],
) -> Tuple[str, Dict[str, int]]:
    """Aggregate clause statuses into a single outcome label.

    Outcome classification rules (intentionally conservative):
      - FAIL if any of H1, H2, H3, H6, H7, H8 has explicit pass=False.
      - STRONG_SUPPORT if all of H1, H2, H3, H4, H6, H7, H8 are pass=True
        (H5, H9, H10 may remain unknown).
      - WEAK_SUPPORT if at least H1 and H8 pass and no explicit failure on
        H2, H3, H6, H7.
      - MIXED if there is at least one pass and at least one explicit fail
        not in the FAIL set above.
      - INCONCLUSIVE otherwise.
    """
    counts = {"pass": 0, "fail": 0, "unknown": 0}
    fail_critical = []
    for h in ["H1", "H2", "H3", "H6", "H7", "H8"]:
        if clauses.get(h, {}).get("pass") is False:
            fail_critical.append(h)
    for h, c in clauses.items():
        v = c.get("pass")
        if v is True:
            counts["pass"] += 1
        elif v is False:
            counts["fail"] += 1
        else:
            counts["unknown"] += 1

    if fail_critical:
        return FAIL, counts

    strong_set = {"H1", "H2", "H3", "H4", "H6", "H7", "H8"}
    if all(clauses.get(h, {}).get("pass") is True for h in strong_set):
        return STRONG_SUPPORT, counts

    if (clauses.get("H1", {}).get("pass") is True
            and clauses.get("H8", {}).get("pass") is True):
        none_fail = all(clauses.get(h, {}).get("pass") is not False
                        for h in ["H2", "H3", "H6", "H7"])
        if none_fail:
            return WEAK_SUPPORT, counts

    if counts["pass"] > 0 and counts["fail"] > 0:
        return MIXED, counts

    return INCONCLUSIVE, counts


# ===========================================================================
# Mode: rerun (uses nq242c_counterexample to regenerate trajectories)
# ===========================================================================


def run_rerun_mode(args) -> Dict[str, Any]:
    """Regenerate WQ-1 (NQ-242c) trajectories and compute L1G diagnostics."""
    # Local imports so summary mode does not require scc to import.
    import nq242c_counterexample as wq1
    from scc.params import ParameterRegistry

    cfg = wq1.RunConfig(
        seed=args.seed,
        max_iter=args.max_iter,
        snapshot_every=args.snapshot_every,
        lambda_rep=args.lambda_rep,
    )
    if args.compress_B is not None:
        cfg.centers_B = ((5, 5), (15, 5), (10, args.compress_B))

    graph, positions = wq1.build_torus(cfg.n_torus)
    params = ParameterRegistry()
    adj = adjacency_list(graph)

    def _run_one(name: str, centers, rng_seed: int) -> Dict[str, Any]:
        rng = np.random.RandomState(rng_seed)
        traj = wq1.run_trajectory(
            cfg, name, list(centers), graph, positions, params, rng,
        )
        snapshots = traj.snapshots
        if args.max_snapshots is not None and args.max_snapshots > 0:
            # Always keep the first and last; subsample interior.
            n = len(snapshots)
            if args.max_snapshots >= n:
                keep = list(range(n))
            else:
                keep = sorted(set([0, n - 1]
                                   + list(np.linspace(0, n - 1,
                                                       args.max_snapshots,
                                                       dtype=int).tolist())))
            snapshots = [snapshots[i] for i in keep]

        per_snap: List[Dict[str, Any]] = []
        for snap in snapshots:
            diag = per_snapshot_diagnostic(
                snap.fields, graph, adj,
                epsilon=cfg.epsilon, delta=args.delta, l_min=args.l_min,
                bridge_max_pairs=args.bridge_max_pairs,
            )
            classes = classify_clauses(diag, l_min=args.l_min, mode="rerun")
            outcome, counts = aggregate_classification(classes)
            per_snap.append({
                "tau": int(snap.tau),
                "diagnostic": diag,
                "clauses": classes,
                "outcome": outcome,
                "counts": counts,
            })
        # Trajectory-level outcome: report worst over snapshots in a fixed order.
        order = [STRONG_SUPPORT, WEAK_SUPPORT, MIXED, INCONCLUSIVE, FAIL]

        def _worst(a: str, b: str) -> str:
            return a if order.index(a) > order.index(b) else b

        traj_outcome = INCONCLUSIVE
        for s in per_snap:
            traj_outcome = _worst(traj_outcome, s["outcome"])

        return {
            "name": name,
            "centers": [list(c) for c in centers],
            "n_snapshots": len(per_snap),
            "snapshots": per_snap,
            "trajectory_outcome": traj_outcome,
            "no_k_jump": traj.no_k_jump,
            "jump_time": traj.jump_time,
        }

    t0 = time.time()
    diag_A = _run_one("equilateral_disk_triangle", cfg.centers_A, cfg.seed)
    diag_B = _run_one("isosceles_disk_triangle", cfg.centers_B, cfg.seed + 1)
    wall = time.time() - t0

    return {
        "mode": "rerun",
        "trajectory_A": diag_A,
        "trajectory_B": diag_B,
        "config": {
            "K_field": cfg.K_field, "M": cfg.M,
            "epsilon": cfg.epsilon,
            "lambda_rep": cfg.lambda_rep,
            "seed": cfg.seed,
            "max_iter": cfg.max_iter,
            "snapshot_every": cfg.snapshot_every,
            "n_torus": cfg.n_torus,
            "centers_A": [list(c) for c in cfg.centers_A],
            "centers_B": [list(c) for c in cfg.centers_B],
            "l_min": args.l_min,
            "delta": args.delta,
            "bridge_max_pairs": args.bridge_max_pairs,
        },
        "wall_clock_seconds": wall,
    }


# ===========================================================================
# Mode: summary (read existing JSON; partial diagnostics only)
# ===========================================================================


def run_summary_mode(args) -> Dict[str, Any]:
    """Read an existing diagnostic JSON and compute the partial L1G slice.

    Recognized inputs: ``ksoft_kact_diag.json`` style (per-snapshot
    K_act/K_bar/dominant_bar_lengths/min_support_distance/m_j_trajectory).
    """
    if not args.input or not os.path.exists(args.input):
        return {
            "mode": "summary",
            "error": f"Input file missing: {args.input}",
            "unavailable_diagnostics": [
                "H1 connectedness", "H2", "H3", "H4", "H5", "H6", "H7",
                "H9 (raw fields needed)", "H10",
            ],
        }
    with open(args.input) as fh:
        d = json.load(fh)

    out_trajs: Dict[str, Any] = {}
    # Heuristic: ksoft_kact_diag.json layout
    for tname in ["trajectory_A", "trajectory_B"]:
        traj = d.get(tname)
        if traj is None:
            continue
        m_j_traj = traj.get("m_j_trajectory") or []
        K_act_list = traj.get("K_act") or []
        K_bar_list = traj.get("K_bar") or []
        dominant = traj.get("dominant_bar_lengths") or []
        min_dist = traj.get("min_support_distance") or []
        n = len(K_act_list)
        per_snap: List[Dict[str, Any]] = []
        for i in range(n):
            snap_diag = {
                "K_act": int(K_act_list[i]),
                "K_bar": int(K_bar_list[i]),
                "active_set": [j for j, m in enumerate(m_j_traj[i] or [])
                                if m > (d.get("config", {}).get("epsilon", 0.225))],
                "dominant_bars": dominant[i] if i < len(dominant) else [],
                "masses": m_j_traj[i] if i < len(m_j_traj) else [],
                "min_support_distance": (min_dist[i]
                                          if i < len(min_dist) else None),
                "U_max": None,
            }
            classes = classify_clauses(snap_diag, l_min=args.l_min, mode="summary")
            outcome, counts = aggregate_classification(classes)
            per_snap.append({
                "tau": traj.get("snapshot_times", list(range(n)))[i],
                "diagnostic": snap_diag,
                "clauses": classes,
                "outcome": outcome,
                "counts": counts,
            })

        out_trajs[tname] = {
            "name": traj.get("name", tname),
            "n_snapshots": n,
            "snapshots": per_snap,
        }

    return {
        "mode": "summary",
        "source_input": args.input,
        "trajectories": out_trajs,
        "unavailable_diagnostics": [
            "H1 (connectedness, full pair distances)",
            "H2 (b_j^U requires U(x))",
            "H3 (theta_bridge requires U(x))",
            "H4 (depends on H2 + H3)",
            "H5 (slot-to-bar association map)",
            "H6 (slot-internal secondary bar requires u^(j))",
            "H7 (R_inact requires u^(j))",
            "H10 (theorem-grade gap)",
        ],
        "config": {"l_min": args.l_min, "delta": args.delta},
    }


# ===========================================================================
# CLI
# ===========================================================================


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="L1-G empirical L1Hyp diagnostic on WQ-LAT trajectories.",
    )
    p.add_argument("--mode", choices=["rerun", "summary"], default="rerun")
    p.add_argument("--input", type=str, default=None,
                   help="Input JSON for --mode summary.")
    p.add_argument("--output", type=str, required=True,
                   help="Output JSON path.")
    p.add_argument("--l_min", type=float, default=0.10)
    p.add_argument("--epsilon", type=float, default=0.225,
                   help="Activity mass threshold (overrides RunConfig if rerun).")
    p.add_argument("--delta", type=float, default=0.05,
                   help="Slot delta-support threshold.")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--snapshot_every", type=int, default=25)
    p.add_argument("--lambda_rep", type=float, default=10.0)
    p.add_argument("--max_snapshots", type=int, default=None,
                   help="If set, subsample to at most N snapshots per trajectory "
                        "(0 or unset = keep all).")
    p.add_argument("--bridge_max_pairs", type=int, default=6,
                   help="Cap on number of pairwise bridge-height computations "
                        "per snapshot to control runtime.")
    p.add_argument("--compress_B", type=int, default=None,
                   help="Override centers_B[2] = (10, compress_B). Default 11.")
    return p.parse_args()


def _json_default(o):
    if isinstance(o, (np.integer, np.int32, np.int64)):
        return int(o)
    if isinstance(o, (np.floating, np.float32, np.float64)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Not JSON-serializable: {type(o)}")


def main() -> int:
    args = parse_args()

    if args.mode == "rerun":
        result = run_rerun_mode(args)
    else:
        result = run_summary_mode(args)

    out = {
        "script": "l1g_l1hyp_diagnostic.py",
        "script_version": SCRIPT_VERSION,
        "purpose": "Empirical L1Hyp clause diagnostic for the L-1 hard-bar / "
                   "active-count bridge candidate (L1-F).",
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
        "result": result,
        "metadata": {
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }

    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[l1g] Wrote {output_path}")
    if args.mode == "rerun":
        for tname in ["trajectory_A", "trajectory_B"]:
            t = out["result"].get(tname, {})
            if not t:
                continue
            print(f"[l1g] {tname}: outcome={t.get('trajectory_outcome')}, "
                  f"n_snap={t.get('n_snapshots')}, no_k_jump={t.get('no_k_jump')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
