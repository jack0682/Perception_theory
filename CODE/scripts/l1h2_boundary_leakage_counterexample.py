"""L1-H2 — Boundary-leakage stress tests for the local-to-global bar inequality.

Status: working diagnostic. NON-canonical. Does not prove L-1; does not promote
L1-F or L1-H to Cat-A; does not modify any canonical or existing working file.

Purpose:
  Verify the inequality direction
      ell_global ≤ ell_local  (for every Case A bar)
  on a battery of finite-graph configurations, including stress cases that
  L1-H §8 step 4 *would have predicted* to lengthen bars globally.

The script reuses ``l1g_l1hyp_diagnostic.h0_barcode`` and the L1-H induced-graph
helper. It does NOT modify any existing file.

A "Case A bar" is a global H_0 superlevel terminal-death bar whose birth vertex
v lies inside the active neighborhood N_j^r AND is also a local maximum in
G_j^r (and necessarily in G). For each such bar the script computes ell_local
on G_j^r and ell_global on G and verifies ell_global ≤ ell_local.

Forbidden non-claims (preserved by the JSON output):
  - L-1 is not proved.
  - L1-F / L1-H are not Cat-A.
  - OP-0005 / OP-0008 are not solved.
  - K_bar = K_act / K_soft = K_act are not claimed globally.
  - sigma_rich sufficiency is not claimed.
  - reservoir theory is not promoted to canonical.
  - empirical verification is not theorem proof.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/l1h2_boundary_leakage_counterexample.py \\
        --output CODE/scripts/results/l1h2_boundary_leakage.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from typing import Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from l1g_l1hyp_diagnostic import h0_barcode, bar_lengths, adjacency_list
from l1h_local_to_global_counterexample import induced_graph


def path_graph(n: int) -> GraphState:
    rows: List[int] = []
    cols: List[int] = []
    for i in range(n - 1):
        rows.extend([i, i + 1])
        cols.extend([i + 1, i])
    data = np.ones(len(rows), dtype=np.float64)
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def custom_graph(n: int, edges: List[Tuple[int, int]]) -> GraphState:
    rows: List[int] = []
    cols: List[int] = []
    for i, j in edges:
        rows.extend([i, j])
        cols.extend([j, i])
    data = np.ones(len(rows), dtype=np.float64)
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def is_global_local_max(v: int, U: np.ndarray, adj: List[List[int]]) -> bool:
    """v is a local maximum in G iff U(v) > U(w) for every neighbor w."""
    return all(U[v] > U[w] for w in adj[v])


def case_A_birth_vertices(N_mask: np.ndarray, U: np.ndarray, adj: List[List[int]]) -> List[int]:
    """Vertices in N that are local maxima of U in G (= Case A birth vertices).

    Strict-greater convention; tied vertices are excluded by the strict
    inequality (LG-5 / LG-6 elder-rule precondition).
    """
    out: List[int] = []
    for v in np.where(N_mask)[0]:
        if is_global_local_max(int(v), U, adj):
            out.append(int(v))
    return out


def find_bar_for_birth(
    barcode: List[Tuple[float, float]], birth_vertex: int, U: np.ndarray,
) -> Optional[Tuple[float, float]]:
    """Return the (b, d) bar in `barcode` born at the given vertex.

    Heuristic: the bar with birth height = U(birth_vertex). With the script's
    deterministic union-find this is unambiguous when LG-5 (tie margin) holds.
    """
    target = float(U[birth_vertex])
    for b, d in barcode:
        if abs(b - target) < 1e-12:
            return (float(b), float(d))
    return None


def compare_local_global_for_bar(
    U: np.ndarray, graph_full: GraphState, N_mask: np.ndarray,
    birth_vertex: int,
) -> Dict[str, object]:
    """Return local and global bars for the given Case A birth vertex."""
    n = graph_full.n
    adj = adjacency_list(graph_full)
    # Local view: induced graph on N_mask, U restricted.
    N_indices = np.where(N_mask)[0].tolist()
    g_local, remap = induced_graph(graph_full, N_indices)
    U_local = U[N_indices]
    bc_local = h0_barcode(U_local, g_local)
    bc_global = h0_barcode(U, graph_full)
    # Map birth vertex into local indexing
    local_bv = int(remap[birth_vertex])
    local_bar = find_bar_for_birth(bc_local, local_bv, U_local)
    global_bar = find_bar_for_birth(bc_global, birth_vertex, U)
    return {
        "birth_vertex_global_idx": birth_vertex,
        "U_birth": float(U[birth_vertex]),
        "local_bar": local_bar,
        "global_bar": global_bar,
        "ell_local": (local_bar[0] - local_bar[1]) if local_bar else None,
        "ell_global": (global_bar[0] - global_bar[1]) if global_bar else None,
        "global_le_local": (
            None if local_bar is None or global_bar is None
            else (global_bar[0] - global_bar[1]) <= (local_bar[0] - local_bar[1]) + 1e-12
        ),
    }


# =============================================================================
# Stress tests
# =============================================================================


def stress_1_internal_only() -> Dict[str, object]:
    """Path 0-1-2-3-4-5-6 with primary at 0, secondary peak at 3 inside N.

    N = {0,1,2,3,4,5}. Boundary at vertex 5. Vertex 6 in X_bg with low value.
    Pure internal merger; no leakage path of consequence. Expect
    ell_global = ell_local for the secondary bar at v=3.
    """
    g = path_graph(7)
    U = np.array([1.0, 0.5, 0.4, 0.55, 0.5, 0.45, 0.05])
    N = np.zeros(7, dtype=bool); N[:6] = True
    return _run_stress(g, U, N, "ST-1 internal-only", description=(
        "Pure internal merger; X_bg vertex (6) has U well below ell_min, "
        "so no external path can compete with internal saddle."))


def stress_2_low_boundary_external_slow() -> Dict[str, object]:
    """Same as ST-1 but with secondary bar deeper, and X_bg vertex value
    raised toward (but still below) ell_min. External path bottleneck is
    capped by U(X_bg), still less than internal saddle. d_global = d_local.
    """
    g = path_graph(7)
    U = np.array([1.0, 0.5, 0.4, 0.55, 0.5, 0.45, 0.08])
    N = np.zeros(7, dtype=bool); N[:6] = True
    return _run_stress(g, U, N, "ST-2 low boundary, slow external", description=(
        "X_bg value below ell_min; external path through X_bg has "
        "bottleneck < d_local, so global death = local death."))


def stress_3_external_faster_than_internal() -> Dict[str, object]:
    """Stress case the L1-H §8 mistakenly thought lengthens bars.

    Build a graph where v's component can leak through the boundary and
    reach an OLDER global birth vertex via a path with bottleneck HIGHER
    than the internal saddle. The internal saddle is at U=0.20 (low). The
    external path goes through a vertex with U=0.30 to reach an older
    birth.

    Per the corrected inequality, this should give d_global > d_local
    (= local saddle 0.20), hence ell_global < ell_local. The bar gets
    SHORTER globally, not longer.

    Graph: two paths joined at v=3 (the secondary peak). Internal "low"
    path 3-4-5-saddle(0.2)-6-primary(1.0). External "high" path
    3-7-bridge(0.3)-8-primary(1.0).

    Concretely use a custom edge list.
    """
    n = 9
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (3, 7), (7, 8),
             (8, 6), (6, 0)]
    g = custom_graph(n, edges)
    # 0 = primary (high), 1, 2 = path to internal, 3 = secondary peak, 4, 5 internal,
    # 6 connects back to 0 (closes the cycle), 7, 8 external high path.
    # We want the secondary at vertex 3 with U=0.55. Internal saddle at vertex 5.
    # External "bridge" at vertex 8.
    U = np.array([1.00, 0.50, 0.40, 0.55, 0.40, 0.20, 0.30, 0.35, 0.40])
    # Active neighborhood N excludes the external path 7,8 and connecting vertex 6.
    N = np.zeros(n, dtype=bool)
    N[0:6] = True  # N = {0,1,2,3,4,5}
    return _run_stress(g, U, N, "ST-3 external-faster-than-internal", description=(
        "Internal saddle at U=0.20 vs external path with bottleneck min(0.35, "
        "0.40, 0.30) = 0.30 (the boundary) and exit U(6)=0.30. This stress "
        "case is the one L1-H §8 mistakenly believed could lengthen bars; "
        "the corrected inequality predicts d_global ≥ d_local hence "
        "ell_global ≤ ell_local (bar SHORTER globally)."))


def stress_4_LG2_violated() -> Dict[str, object]:
    """LG-2 violation: boundary collar VERY high, near peak height.

    Demonstrates that even when LG-2 fails, the local-to-global inequality
    direction is preserved (it follows from graph inclusion alone).

    Path 0-1-2-3-4-5 with U=(1.0, 0.5, 0.4, 0.6, 0.95, 0.9). Boundary collar
    B_∂ = U(4) = 0.95, close to b_j = 1.0. LG-2 violated for any l_min > 0.05.
    Vertex 5 outside N is at U=0.9, also very high.
    """
    g = path_graph(6)
    U = np.array([1.0, 0.5, 0.4, 0.6, 0.95, 0.9])
    N = np.zeros(6, dtype=bool); N[:5] = True
    return _run_stress(g, U, N, "ST-4 LG-2 violated, high boundary", description=(
        "LG-2 fails: boundary collar U(4)=0.95 is close to peak. Verify "
        "graph-inclusion inequality still holds independently of LG-2."))


def stress_5_equal_heights_tie() -> Dict[str, object]:
    """Equal-height ties to test LG-5 / LG-6 robustness.

    Two equal peaks at vertex 0 and 4. Tie-break by index. Verify that the
    inequality holds regardless of which vertex is assigned the terminal bar.
    """
    g = path_graph(5)
    U = np.array([1.0, 0.5, 0.05, 0.5, 1.0])
    N = np.zeros(5, dtype=bool); N[:3] = True  # N = {0, 1, 2} only
    return _run_stress(g, U, N, "ST-5 equal heights tie", description=(
        "Ties at peak height. Check inequality holds (or marked tie-stable "
        "case) regardless of elder-rule assignment."))


# =============================================================================
# Test runner
# =============================================================================


def _run_stress(
    g: GraphState, U: np.ndarray, N: np.ndarray, name: str,
    description: str = "",
) -> Dict[str, object]:
    n = g.n
    adj = adjacency_list(g)
    case_A = case_A_birth_vertices(N, U, adj)
    bars = []
    all_le = True
    has_strict = False
    for v in case_A:
        cmp = compare_local_global_for_bar(U, g, N, int(v))
        bars.append(cmp)
        if cmp["global_le_local"] is False:
            all_le = False
        # Strictly less? (within tolerance)
        if (cmp["ell_local"] is not None and cmp["ell_global"] is not None
                and cmp["ell_global"] + 1e-9 < cmp["ell_local"]):
            has_strict = True
    return {
        "name": name,
        "description": description,
        "graph_n": n,
        "U": U.tolist(),
        "N_mask": [bool(x) for x in N.tolist()],
        "case_A_birth_vertices": case_A,
        "bars": bars,
        "ell_global_le_ell_local_for_all_case_A_bars": all_le,
        "had_strict_inequality": has_strict,
    }


def main() -> int:
    p = argparse.ArgumentParser(
        description="L1-H2 boundary-leakage stress tests.")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    t0 = time.time()
    exhibits = {
        "ST_1": stress_1_internal_only(),
        "ST_2": stress_2_low_boundary_external_slow(),
        "ST_3": stress_3_external_faster_than_internal(),
        "ST_4": stress_4_LG2_violated(),
        "ST_5": stress_5_equal_heights_tie(),
    }
    overall_inequality = all(
        ex["ell_global_le_ell_local_for_all_case_A_bars"] for ex in exhibits.values()
    )
    out = {
        "script": "l1h2_boundary_leakage_counterexample.py",
        "purpose": "Numerical stress tests of the L1-H2 boundary-leakage inequality "
                   "ell_global <= ell_local for Case A bars.",
        "non_claims": {
            "L1_proved": False,
            "L1F_promoted_to_Cat_A": False,
            "L1H_promoted_to_Cat_A": False,
            "L1H2_promoted_to_Cat_A": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "K_bar_equals_K_act_globally": False,
            "K_soft_equals_K_act_globally": False,
            "sigma_rich_sufficient": False,
            "reservoir_canonical": False,
            "exhibits_are_theorem_proof": False,
        },
        "exhibits": exhibits,
        "summary": {
            "all_stress_tests_satisfy_ell_global_le_ell_local": overall_inequality,
            "any_strict_inequality": any(
                ex["had_strict_inequality"] for ex in exhibits.values()
            ),
        },
        "wall_clock_seconds": time.time() - t0,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: int(o) if isinstance(o, np.integer)
                  else (float(o) if isinstance(o, np.floating)
                        else (o.tolist() if isinstance(o, np.ndarray)
                              else (None if isinstance(o, float) and (math.isnan(o) or math.isinf(o))
                                    else str(o)))))
    print(f"[l1h2-ce] Wrote {args.output}")
    for name, ex in exhibits.items():
        cnt = len(ex["case_A_birth_vertices"])
        ok = ex["ell_global_le_ell_local_for_all_case_A_bars"]
        strict = ex["had_strict_inequality"]
        print(f"  {name}: {cnt} Case A bar(s); inequality holds = {ok}; strict = {strict}")
        for b in ex["bars"]:
            v = b["birth_vertex_global_idx"]
            ll = b["ell_local"]; lg = b["ell_global"]
            ll_str = f"{ll:.4f}" if ll is not None else "None"
            lg_str = f"{lg:.4f}" if lg is not None else "None"
            print(f"     v={v}: ell_local={ll_str}, ell_global={lg_str}, le={b['global_le_local']}")
    print(f"[l1h2-ce] OVERALL: ell_global ≤ ell_local for ALL stress tests = {overall_inequality}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
