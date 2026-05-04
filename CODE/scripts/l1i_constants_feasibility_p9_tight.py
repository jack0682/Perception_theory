"""L1-I P9-tight variant — NQ-G1-2 fresh-full-run (per op_resolution.md §10.4).

Copy of `l1i_constants_feasibility.py` with ONE structural addition: optional
per-clause H6 budget override via `--h6-budget`. All other logic identical.

When `--h6-budget` is set (and differs from `--budget`), FEASIBLE_WITH_BUDGET
requires:
  - all non-H6 clause margins ≥ `--budget`
  - H6 margin ≥ `--h6-budget`

When `--h6-budget` is omitted, this script behaves identically to the parent.

Faithful (P9-tight) per op_resolution.md §10.4 step 2: ρ_pert/2 → ρ_pert/4,
so H6' margin requirement of 3·ρ_pert → 1.5·ρ_pert, equivalent to halving
`--h6-budget` from 0.05 to 0.025 while keeping `--budget` = 0.05.

Fresh-full-run validation for `op_resolution_nq_g1_2_p9_tight.py` (the
post-processing wrapper), per user "빡세게 돌릴수있으니까" directive.

ORIGINAL DOCSTRING (preserved):

L1-I — Constants Feasibility Study for the L1-H regime.

Status: working diagnostic. NON-canonical. Does not prove L-1; does not promote
L1-F or L1-H to Cat-A; does not solve OP-0005 / OP-0008; does not modify any
canonical or existing working file. Empirical feasibility, not theorem proof.

Goal:
  Determine empirically whether the L1-H regime is non-empty on initial
  Gaussian-bump configurations on T^2_{20}. Specifically, sweep over
  (sigma_b, delta, r, ell_min, geometry) and measure all of the L1-H
  inequalities:

    LG-1  N_j^r ∩ N_k^r = ∅              (disjoint active neighborhoods)
    LG-2  max_{∂N_j^r} U ≤ b_j - ℓ_min - r_assoc           (boundary collar)
    LG-3  θ_bridge^{jk}(U) ≤ min(b_j,b_k) - ℓ_min - r_assoc (low bridge)
    LG-4  ‖U‖_{∞,X_bg} ≤ ℓ_min - ρ_bg                       (background)
    H6'   ℓ_{j,2}(u^(j)) ≤ ℓ_min - 3 ρ_pert                 (tightened)
    LDG   h_min - max_jk θ_bridge^{jk} ≥ ℓ_min + r_assoc + r_birth  (ledger)

  Classify each configuration as FEASIBLE_WITH_BUDGET / RAW_FEASIBLE /
  MARGINAL / INFEASIBLE / INCONCLUSIVE.

The script reuses:
  - nq242c_counterexample.build_torus, build_initial_state for graph + state
  - l1g_l1hyp_diagnostic.h0_barcode, threshold_scan_bridge_height,
    adjacency_list, support_distance, n_connected_components

It does NOT modify any canonical or existing working file.

Forbidden non-claims (preserved by the JSON output):
  - L-1 is not proved.
  - L1-F / L1-H are not Cat-A.
  - OP-0005 / OP-0008 are not solved.
  - K_bar = K_act / K_soft = K_act are not claimed globally.
  - sigma_rich sufficiency is not claimed.
  - reservoir theory is not promoted to canonical.
  - empirical feasibility is not theorem proof.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/l1i_constants_feasibility.py \\
        --output CODE/scripts/results/l1i_constants_feasibility.json \\
        --mode full

    PYTHONPATH=CODE python3 CODE/scripts/l1i_constants_feasibility.py \\
        --output CODE/scripts/results/l1i_constants_feasibility_smoke.json \\
        --mode smoke
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
from collections import Counter
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from l1g_l1hyp_diagnostic import (
    h0_barcode,
    bar_lengths,
    threshold_scan_bridge_height,
    adjacency_list,
    n_connected_components,
)
import nq242c_counterexample as wq1


SCRIPT_VERSION = "0.1"


# ===========================================================================
# Feasibility classification
# ===========================================================================

FEASIBLE_WITH_BUDGET = "FEASIBLE_WITH_BUDGET"
RAW_FEASIBLE = "RAW_FEASIBLE"
MARGINAL = "MARGINAL"
INFEASIBLE = "INFEASIBLE"
INCONCLUSIVE = "INCONCLUSIVE"

# Default budget for "feasible with budget" (positive margin threshold).
DEFAULT_BUDGET = 0.05
# Tolerance for "marginal" (small negative margin).
MARGINAL_TOL = 0.01


# ===========================================================================
# Geometry helpers
# ===========================================================================


def vertex_xy(idx: int, n_torus: int) -> Tuple[int, int]:
    return (idx // n_torus, idx % n_torus)


def torus_distance_idx(i: int, j: int, n: int) -> float:
    ri, ci = vertex_xy(i, n)
    rj, cj = vertex_xy(j, n)
    dr = min(abs(ri - rj), n - abs(ri - rj))
    dc = min(abs(ci - cj), n - abs(ci - cj))
    return float(np.sqrt(dr * dr + dc * dc))


def multi_source_bfs_distance(
    sources: np.ndarray, adj: List[List[int]],
) -> np.ndarray:
    """Graph distance from each vertex to the nearest source vertex.

    Returns array of distances; vertices unreachable are np.inf.
    """
    n = len(sources)
    dist = np.full(n, -1, dtype=int)
    queue: List[int] = []
    for i in np.where(sources)[0]:
        dist[int(i)] = 0
        queue.append(int(i))
    head = 0
    while head < len(queue):
        x = queue[head]
        head += 1
        for nb in adj[x]:
            if dist[nb] < 0:
                dist[nb] = dist[x] + 1
                queue.append(int(nb))
    out = np.where(dist < 0, np.inf, dist).astype(float)
    return out


def boundary_vertices(neighborhood_mask: np.ndarray, adj: List[List[int]]) -> np.ndarray:
    """Vertices in N which have at least one neighbor outside N."""
    n = len(neighborhood_mask)
    boundary = np.zeros(n, dtype=bool)
    for v in np.where(neighborhood_mask)[0]:
        for nb in adj[int(v)]:
            if not neighborhood_mask[nb]:
                boundary[int(v)] = True
                break
    return boundary


# ===========================================================================
# Configuration evaluation
# ===========================================================================


@dataclass
class FeasibilityConfig:
    sigma_b: float
    delta: float
    r: int
    l_min: float
    geometry: str  # 'A', 'B', or 'wide' (artificial well-separated)
    state_mode: str = "wq1"  # 'wq1' = WQ-1 mass-projection; 'raw_gaussian' = peak=1 unforced


@dataclass
class FeasibilityResult:
    config: FeasibilityConfig
    n_active: int
    # Inputs
    h_min_measured: Optional[float]
    # LG-1
    lg1_disjoint: Optional[bool]
    lg1_overlap_count: int
    # LG-2
    boundary_collars: Dict[str, float]  # B_∂,j per active slot
    lg2_min_margin: Optional[float]      # min over j of (b_j - l_min - B_∂,j)
    lg2_pass: Optional[bool]
    # LG-3
    bridge_heights: Dict[str, float]
    lg3_min_margin: Optional[float]      # min over pairs of (min(b_j,b_k) - l_min - bridge)
    lg3_pass: Optional[bool]
    # LG-4
    bg_max_U: Optional[float]
    bg_size: int
    lg4_margin: Optional[float]          # l_min - bg_max
    lg4_pass: Optional[bool]
    # H6 tightened
    slot_l2: Dict[str, float]
    h6_min_margin: Optional[float]       # l_min - max_j ell_{j,2}
    h6_pass: Optional[bool]
    # Ledger
    max_bridge: Optional[float]
    ledger_margin: Optional[float]
    ledger_pass: Optional[bool]
    # Aggregate
    feasibility_class: str
    failing_clauses: List[str]
    notes: List[str]


def build_raw_gaussian_state(
    centers: Tuple[Tuple[int, int], ...],
    sigma_b: float,
    n_torus: int,
    positions: np.ndarray,
    initial_masses: Tuple[float, ...],
    epsilon_active: float,
) -> List[np.ndarray]:
    """Idealized state: u^(j)(x) = exp(-d_T(x, c_j)^2 / (2 sigma_b^2)).

    No forced mass projection, no simplex barrier, no clipping. Peak = 1.0 at
    each active center. Inactive slots (mass <= epsilon_active in
    initial_masses) are zero. This tests L1-H feasibility on a clean
    Gaussian-bump exhibit independent of the WQ-1 dynamical normalization
    (which inflates supports via uniform-floor projection).
    """
    K = len(initial_masses)
    n = positions.shape[0]
    fields: List[np.ndarray] = []
    for k in range(K):
        if initial_masses[k] <= epsilon_active:
            fields.append(np.zeros(n))
            continue
        c = np.array(centers[k], dtype=np.float64)
        d = wq1.torus_distance(positions, c, n_torus)
        u = np.exp(-(d ** 2) / (2.0 * sigma_b * sigma_b))
        fields.append(u)
    return fields


def compute_feasibility(
    cfg: FeasibilityConfig,
    base_centers_A: Tuple[Tuple[int, int], ...],
    base_centers_B: Tuple[Tuple[int, int], ...],
    base_centers_wide: Tuple[Tuple[int, int], ...],
    n_torus: int,
    M_total: float,
    initial_masses: Tuple[float, ...],
    epsilon: float,
    budget: float,
    bridge_max_pairs: int = 6,
    h6_budget: Optional[float] = None,
) -> FeasibilityResult:
    """Build state from cfg and evaluate all L1-H constants."""
    if cfg.geometry == "A":
        centers = base_centers_A
    elif cfg.geometry == "B":
        centers = base_centers_B
    elif cfg.geometry == "wide":
        centers = base_centers_wide
    else:
        raise ValueError(f"Unknown geometry: {cfg.geometry}")

    rc = wq1.RunConfig(
        K_field=len(initial_masses),
        M=M_total,
        epsilon=epsilon,
        sigma_b=cfg.sigma_b,
        seed=42,
        max_iter=0,
        snapshot_every=1,
        n_torus=n_torus,
        centers_A=centers,
        centers_B=centers,  # only used for build_initial_state
        initial_masses=initial_masses,
    )
    graph, positions = wq1.build_torus(n_torus)
    if cfg.state_mode == "wq1":
        fields = wq1.build_initial_state(rc, list(centers), positions)
    elif cfg.state_mode == "raw_gaussian":
        fields = build_raw_gaussian_state(
            centers, cfg.sigma_b, n_torus, positions, initial_masses,
            epsilon_active=0.0,
        )
    else:
        raise ValueError(f"Unknown state_mode: {cfg.state_mode}")
    masses = [float(f.sum()) for f in fields]
    if cfg.state_mode == "wq1":
        A = [j for j, m in enumerate(masses) if m > epsilon]
    else:
        # raw_gaussian: A = slots whose nominal initial_mass > 0 (i.e. real bumps)
        A = [j for j in range(len(initial_masses)) if initial_masses[j] > 0]
    n_active = len(A)
    notes: List[str] = []

    if n_active == 0:
        return FeasibilityResult(
            config=cfg, n_active=0, h_min_measured=None,
            lg1_disjoint=None, lg1_overlap_count=0,
            boundary_collars={}, lg2_min_margin=None, lg2_pass=None,
            bridge_heights={}, lg3_min_margin=None, lg3_pass=None,
            bg_max_U=None, bg_size=0,
            lg4_margin=None, lg4_pass=None,
            slot_l2={}, h6_min_margin=None, h6_pass=None,
            max_bridge=None, ledger_margin=None, ledger_pass=None,
            feasibility_class=INCONCLUSIVE,
            failing_clauses=["no_active_slots"],
            notes=["No active slots (all masses below epsilon)."],
        )

    n = graph.n
    adj = adjacency_list(graph)
    U = np.sum(fields, axis=0)

    # ----- per-slot supports and neighborhoods -----
    support_masks: Dict[int, np.ndarray] = {}
    neigh_masks: Dict[int, np.ndarray] = {}
    peak_idx: Dict[int, int] = {}
    b_U: Dict[int, float] = {}
    slot_l2: Dict[str, float] = {}

    for j in A:
        f = fields[j]
        # δ-support
        smask = (f > cfg.delta)
        support_masks[j] = smask
        if not np.any(smask):
            notes.append(f"slot {j}: empty delta-support at delta={cfg.delta}")
        # peak
        peak_idx[j] = int(np.argmax(f))
        b_U[str(j)] = float(U[peak_idx[j]])
        # active neighborhood: vertices within graph distance r of S_j^δ
        if np.any(smask):
            dist_to_supp = multi_source_bfs_distance(smask, adj)
            nmask = (dist_to_supp <= cfg.r)
        else:
            nmask = np.zeros(n, dtype=bool)
        neigh_masks[j] = nmask
        # slot-internal H_0 secondary
        bc = h0_barcode(f, graph)
        ells = sorted(bar_lengths(bc), reverse=True)
        slot_l2[str(j)] = float(ells[1]) if len(ells) > 1 else 0.0

    h_min_measured: Optional[float] = (min(b_U.values()) if b_U else None)

    # ----- LG-1: disjoint active neighborhoods -----
    overlap_count = 0
    pair_overlaps: Dict[str, int] = {}
    for ai, j in enumerate(A):
        for k in A[ai + 1:]:
            ov = int(np.sum(neigh_masks[j] & neigh_masks[k]))
            pair_overlaps[f"{j}-{k}"] = ov
            if ov > 0:
                overlap_count += 1
    lg1_disjoint = overlap_count == 0

    # ----- LG-2: boundary collar B_∂,j -----
    boundary_collars: Dict[str, float] = {}
    lg2_margins: List[float] = []
    for j in A:
        nmask = neigh_masks[j]
        if not np.any(nmask):
            boundary_collars[str(j)] = float("nan")
            continue
        bmask = boundary_vertices(nmask, adj)
        if not np.any(bmask):
            # Boundary undefined (neighborhood is the entire graph)
            boundary_collars[str(j)] = float("nan")
            notes.append(f"slot {j}: boundary undefined (N_j^r covers all of X)")
            continue
        B_partial = float(np.max(U[bmask]))
        boundary_collars[str(j)] = B_partial
        lg2_margins.append(b_U[str(j)] - cfg.l_min - B_partial)
    lg2_min_margin = (min(lg2_margins) if lg2_margins else None)
    lg2_pass = (lg2_min_margin is not None and lg2_min_margin >= 0)

    # ----- X_bg and LG-4 -----
    bg_mask = np.ones(n, dtype=bool)
    for j in A:
        bg_mask &= ~neigh_masks[j]
    bg_size = int(np.sum(bg_mask))
    if bg_size > 0:
        bg_max_U = float(np.max(U[bg_mask]))
        lg4_margin = cfg.l_min - bg_max_U
        lg4_pass = lg4_margin >= 0
    else:
        bg_max_U = None
        lg4_margin = None
        lg4_pass = None  # vacuous; classify carefully
        notes.append("Background X_bg is empty — LG-4 vacuous.")

    # ----- LG-3: bridge heights between active peak pairs -----
    bridge_heights: Dict[str, float] = {}
    pair_count = 0
    lg3_margins: List[float] = []
    for ai, j in enumerate(A):
        for k in A[ai + 1:]:
            if pair_count >= bridge_max_pairs:
                bridge_heights[f"{j}-{k}"] = float("nan")
                continue
            theta = threshold_scan_bridge_height(
                U, peak_idx[j], peak_idx[k], adj)
            if theta is None or not math.isfinite(theta):
                bridge_heights[f"{j}-{k}"] = float("nan")
                pair_count += 1
                continue
            bridge_heights[f"{j}-{k}"] = float(theta)
            lg3_margins.append(min(b_U[str(j)], b_U[str(k)]) - cfg.l_min - theta)
            pair_count += 1
    lg3_min_margin = (min(lg3_margins) if lg3_margins else None)
    lg3_pass = (lg3_min_margin is not None and lg3_min_margin >= 0)

    # ----- H6 tightened (raw form: l_min - max_j ell_{j,2}) -----
    if slot_l2:
        max_l2 = max(slot_l2.values())
        h6_min_margin: Optional[float] = cfg.l_min - max_l2
        h6_pass: Optional[bool] = h6_min_margin >= 0
    else:
        h6_min_margin = None
        h6_pass = None

    # ----- Ledger -----
    finite_bridges = [v for v in bridge_heights.values() if math.isfinite(v)]
    if finite_bridges and h_min_measured is not None:
        max_bridge: Optional[float] = max(finite_bridges)
        ledger_margin: Optional[float] = h_min_measured - max_bridge - cfg.l_min
        ledger_pass: Optional[bool] = ledger_margin >= 0
    else:
        max_bridge = None
        ledger_margin = None
        ledger_pass = None

    # ----- Classify -----
    failing: List[str] = []
    margins: List[float] = []
    if not lg1_disjoint:
        failing.append("LG-1")
    if lg2_pass is False:
        failing.append("LG-2")
    if lg2_min_margin is not None:
        margins.append(lg2_min_margin)
    if lg3_pass is False:
        failing.append("LG-3")
    if lg3_min_margin is not None:
        margins.append(lg3_min_margin)
    if lg4_pass is False:
        failing.append("LG-4")
    if lg4_margin is not None:
        margins.append(lg4_margin)
    if h6_pass is False:
        failing.append("H6")
    if h6_min_margin is not None:
        margins.append(h6_min_margin)
    if ledger_pass is False:
        failing.append("LDG")
    if ledger_margin is not None:
        margins.append(ledger_margin)

    # P9-tight variant: support per-clause H6 budget. If h6_budget is None,
    # fall back to uniform `budget` (parent-script behavior).
    effective_h6_budget = budget if h6_budget is None else h6_budget

    if not lg1_disjoint or any(p is False for p in [lg2_pass, lg3_pass, lg4_pass, h6_pass, ledger_pass]):
        # Pick classification based on margin badness
        worst = min(margins) if margins else float("nan")
        # LG-1 has no continuous margin; treat overlap as INFEASIBLE if overlap
        if not lg1_disjoint:
            cls = INFEASIBLE
        elif math.isnan(worst):
            cls = INCONCLUSIVE
        elif worst < -MARGINAL_TOL:
            cls = INFEASIBLE
        elif worst < 0:
            cls = MARGINAL
        else:
            cls = RAW_FEASIBLE  # all pass with budget=0
    else:
        # All clauses pass with budget 0. Classify FEASIBLE_WITH_BUDGET with
        # per-clause H6 budget if differs from global budget.
        non_h6_margins: List[float] = []
        if lg2_min_margin is not None:
            non_h6_margins.append(lg2_min_margin)
        if lg3_min_margin is not None:
            non_h6_margins.append(lg3_min_margin)
        if lg4_margin is not None:
            non_h6_margins.append(lg4_margin)
        if ledger_margin is not None:
            non_h6_margins.append(ledger_margin)

        non_h6_ok = (not non_h6_margins) or (min(non_h6_margins) >= budget)
        h6_ok = (h6_min_margin is None) or (h6_min_margin >= effective_h6_budget)

        if margins and non_h6_ok and h6_ok:
            cls = FEASIBLE_WITH_BUDGET
        else:
            cls = RAW_FEASIBLE

    return FeasibilityResult(
        config=cfg,
        n_active=n_active,
        h_min_measured=h_min_measured,
        lg1_disjoint=lg1_disjoint,
        lg1_overlap_count=overlap_count,
        boundary_collars=boundary_collars,
        lg2_min_margin=lg2_min_margin,
        lg2_pass=lg2_pass,
        bridge_heights=bridge_heights,
        lg3_min_margin=lg3_min_margin,
        lg3_pass=lg3_pass,
        bg_max_U=bg_max_U,
        bg_size=bg_size,
        lg4_margin=lg4_margin,
        lg4_pass=lg4_pass,
        slot_l2=slot_l2,
        h6_min_margin=h6_min_margin,
        h6_pass=h6_pass,
        max_bridge=max_bridge,
        ledger_margin=ledger_margin,
        ledger_pass=ledger_pass,
        feasibility_class=cls,
        failing_clauses=failing,
        notes=notes,
    )


# ===========================================================================
# Sweep
# ===========================================================================


def make_smoke_sweep() -> List[FeasibilityConfig]:
    sb_grid = [0.5, 1.0, 2.0]
    delta_grid = [0.05, 0.10]
    r_grid = [1, 2]
    lmin_grid = [0.10]
    geoms = ["A", "B"]
    state_modes = ["wq1", "raw_gaussian"]
    cfgs: List[FeasibilityConfig] = []
    for sm in state_modes:
        for sb in sb_grid:
            for d in delta_grid:
                for r in r_grid:
                    for lm in lmin_grid:
                        for g in geoms:
                            cfgs.append(FeasibilityConfig(sb, d, r, lm, g, sm))
    return cfgs


def make_full_sweep() -> List[FeasibilityConfig]:
    sb_grid = [0.5, 1.0, 1.5, 2.0]
    delta_grid = [0.02, 0.05, 0.10, 0.15, 0.20]
    r_grid = [0, 1, 2, 3]
    lmin_grid = [0.05, 0.10, 0.15, 0.20]
    geoms = ["A", "B", "wide"]
    state_modes = ["wq1", "raw_gaussian"]
    cfgs: List[FeasibilityConfig] = []
    for sm in state_modes:
        for sb in sb_grid:
            for d in delta_grid:
                for r in r_grid:
                    for lm in lmin_grid:
                        for g in geoms:
                            cfgs.append(FeasibilityConfig(sb, d, r, lm, g, sm))
    return cfgs


def aggregate_results(results: List[FeasibilityResult]) -> Dict[str, Any]:
    cls_counter: Counter = Counter()
    fail_counter: Counter = Counter()
    for r in results:
        cls_counter[r.feasibility_class] += 1
        for c in r.failing_clauses:
            fail_counter[c] += 1
    # Best cases: FEASIBLE_WITH_BUDGET first, then RAW_FEASIBLE, then MARGINAL by least-bad margin.
    def sort_key(r: FeasibilityResult) -> Tuple[int, float]:
        order = {FEASIBLE_WITH_BUDGET: 0, RAW_FEASIBLE: 1, MARGINAL: 2,
                 INFEASIBLE: 3, INCONCLUSIVE: 4}
        margins = [m for m in [r.lg2_min_margin, r.lg3_min_margin,
                                r.lg4_margin, r.h6_min_margin,
                                r.ledger_margin] if m is not None]
        worst_margin = min(margins) if margins else float("nan")
        return (order[r.feasibility_class], -worst_margin if not math.isnan(worst_margin) else 0.0)
    sorted_results = sorted(results, key=sort_key)
    best = sorted_results[:5]
    return {
        "class_counts": dict(cls_counter),
        "failure_counts": dict(fail_counter),
        "n_total": len(results),
        "best_cases": [feas_result_to_dict(r) for r in best],
    }


def feas_result_to_dict(r: FeasibilityResult) -> Dict[str, Any]:
    d = asdict(r)
    # Replace floats that are NaN/inf to keep JSON valid.
    return _scrub(d)


def _scrub(o: Any) -> Any:
    if isinstance(o, float):
        if math.isnan(o):
            return None
        if math.isinf(o):
            return None
        return o
    if isinstance(o, dict):
        return {k: _scrub(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_scrub(x) for x in o]
    return o


# ===========================================================================
# CLI
# ===========================================================================


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="L1-I empirical constants feasibility study.",
    )
    p.add_argument("--output", required=True)
    p.add_argument("--mode", choices=["smoke", "full"], default="full")
    p.add_argument("--budget", type=float, default=DEFAULT_BUDGET)
    p.add_argument("--h6-budget", type=float, default=None,
                   help="Per-clause H6 margin budget. If omitted, inherits --budget. "
                        "Set differently to test (P9-tight) per op_resolution.md §10.4 step 2.")
    p.add_argument("--bridge_max_pairs", type=int, default=6)
    return p.parse_args()


def main() -> int:
    args = parse_args()

    base_centers_A = ((5, 5), (15, 5), (10, 14))
    base_centers_B = ((5, 5), (15, 5), (10, 11))
    # 'wide': artificial maximally-separated 3-bump configuration on T^2_20
    # (vertices at distance ~7 from each other under torus L^2 metric)
    base_centers_wide = ((3, 3), (13, 3), (8, 13))
    n_torus = 20
    M_total = 90.0
    initial_masses = (30.0, 30.0, 30.0, 0.0)
    epsilon = 0.225

    cfgs = make_smoke_sweep() if args.mode == "smoke" else make_full_sweep()

    t0 = time.time()
    results: List[FeasibilityResult] = []
    for i, cfg in enumerate(cfgs):
        try:
            r = compute_feasibility(
                cfg, base_centers_A, base_centers_B, base_centers_wide,
                n_torus=n_torus, M_total=M_total,
                initial_masses=initial_masses, epsilon=epsilon,
                budget=args.budget, bridge_max_pairs=args.bridge_max_pairs,
                h6_budget=args.h6_budget,
            )
        except Exception as e:
            r = FeasibilityResult(
                config=cfg, n_active=0, h_min_measured=None,
                lg1_disjoint=None, lg1_overlap_count=0,
                boundary_collars={}, lg2_min_margin=None, lg2_pass=None,
                bridge_heights={}, lg3_min_margin=None, lg3_pass=None,
                bg_max_U=None, bg_size=0,
                lg4_margin=None, lg4_pass=None,
                slot_l2={}, h6_min_margin=None, h6_pass=None,
                max_bridge=None, ledger_margin=None, ledger_pass=None,
                feasibility_class=INCONCLUSIVE,
                failing_clauses=["exception"],
                notes=[f"compute_feasibility raised: {type(e).__name__}: {e}"],
            )
        results.append(r)

    summary = aggregate_results(results)
    wall = time.time() - t0

    out = {
        "script": "l1i_constants_feasibility.py",
        "script_version": SCRIPT_VERSION,
        "purpose": ("Empirical feasibility study for L1-H constants on initial "
                    "Gaussian-bump configurations on T^2_20."),
        "non_claims": {
            "L1_proved": False,
            "L1F_promoted_to_Cat_A": False,
            "L1H_promoted_to_Cat_A": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "K_bar_equals_K_act_globally": False,
            "K_soft_equals_K_act_globally": False,
            "sigma_rich_sufficient": False,
            "reservoir_canonical": False,
            "feasibility_is_theorem_proof": False,
        },
        "config": {
            "n_torus": n_torus,
            "M_total": M_total,
            "initial_masses": list(initial_masses),
            "epsilon": epsilon,
            "centers_A": [list(c) for c in base_centers_A],
            "centers_B": [list(c) for c in base_centers_B],
            "budget_threshold": args.budget,
            "h6_budget_threshold": args.h6_budget,
            "h6_budget_inherits_budget": args.h6_budget is None,
            "marginal_tolerance": MARGINAL_TOL,
            "mode": args.mode,
            "n_configs_tested": len(cfgs),
        },
        "summary": summary,
        "results": [feas_result_to_dict(r) for r in results],
        "wall_clock_seconds": wall,
        "metadata": {
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: int(o) if isinstance(o, np.integer)
                  else (float(o) if isinstance(o, np.floating)
                        else (o.tolist() if isinstance(o, np.ndarray) else str(o))))
    print(f"[l1i] Wrote {args.output}")
    print(f"[l1i] Tested {len(results)} configurations in {wall:.1f}s")
    print(f"[l1i] class_counts: {summary['class_counts']}")
    print(f"[l1i] failure_counts: {summary['failure_counts']}")
    print(f"[l1i] best classes (top 3):")
    for r in summary["best_cases"][:3]:
        cfg = r["config"]
        print(f"   sigma_b={cfg['sigma_b']}, delta={cfg['delta']}, r={cfg['r']}, "
              f"l_min={cfg['l_min']}, geom={cfg['geometry']} -> {r['feasibility_class']}, "
              f"failing={r['failing_clauses']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
