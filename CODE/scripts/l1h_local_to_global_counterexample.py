"""L1-H — Local-to-Global counterexample exhibits.

Status: working diagnostic. NON-canonical. Does not prove L-1; does not promote
any working result; does not modify any canonical or existing working file.

Goal:
  Construct small finite-graph examples where the *local* H_0 superlevel
  barcodes on neighborhoods G_j^r differ from the *global* H_0 superlevel
  barcode on G, demonstrating concretely that local barcode control alone is
  insufficient and that LG-1..LG-7 of L1-H are non-vacuous.

The script reuses the terminal-death union-find barcode from
``CODE/scripts/l1g_l1hyp_diagnostic.py``.

Counterexample exhibits implemented (Section 5 of L1-H document):

  CE-1  high-corridor merge: 5-vertex path graph with two unit peaks at
        endpoints, low-low-low-corridor variant matches local sum (2 dominant
        bars), high-corridor variant produces a third dominant global bar from
        the corridor itself. Defeated by LG-3 (bridge height bound) and LG-4
        (background suppression).

  CE-2  background dominant residual: dumbbell with two unit-peak active
        neighborhoods and an isolated X_bg vertex carrying a residual spike of
        height >= l_min. The spike adds an independent terminal bar globally.
        Defeated by LG-4.

  CE-3  local secondary that almost crosses l_min: two-peak slot inside one
        active neighborhood, with secondary peak height tuned so that the local
        secondary bar length lies just below l_min. Under aggregate
        perturbation by another slot, the global secondary bar length is
        boosted by ~rho_pert, exposing the perturbation gap in the bottleneck
        argument. Used to motivate the H6 tightening to ell_min - 3 rho_pert.

  CE-4  terminal-bar reassignment: two equal-height active peaks. The
        terminal bar is assigned to one of them by elder rule (index-tie).
        K_bar count is unchanged; the example only documents that LG-6
        elder-rule compatibility is needed to make the assignment well-defined.

Each exhibit prints local barcodes per active neighborhood and the global
barcode, with K_bar^{l_min} computed at l_min = 0.10 by default.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/l1h_local_to_global_counterexample.py \\
        --output CODE/scripts/results/l1h_counterexample.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from typing import Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState

# Reuse the L1-G barcode helpers: same terminal-death convention, same
# union-find recipe.
from l1g_l1hyp_diagnostic import (
    h0_barcode, bar_lengths, k_bar, adjacency_list,
)


def path_graph(n: int) -> GraphState:
    """Linear path graph 0 - 1 - 2 - ... - (n-1)."""
    rows: List[int] = []
    cols: List[int] = []
    for i in range(n - 1):
        rows.extend([i, i + 1])
        cols.extend([i + 1, i])
    data = np.ones(len(rows), dtype=np.float64)
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def induced_graph(graph: GraphState, vertex_subset: List[int]) -> Tuple[GraphState, np.ndarray]:
    """Induced subgraph on a vertex subset, plus a remap array.

    Returns (sub_graph, remap) where remap[i] = new index of original vertex i,
    or -1 if not in subset.
    """
    n = graph.n
    remap = np.full(n, -1, dtype=int)
    for new, old in enumerate(vertex_subset):
        remap[old] = new
    W_full_coo = graph.W.tocoo()
    rows: List[int] = []
    cols: List[int] = []
    for i, j in zip(W_full_coo.row, W_full_coo.col):
        if remap[int(i)] >= 0 and remap[int(j)] >= 0:
            rows.append(int(remap[int(i)]))
            cols.append(int(remap[int(j)]))
    n_sub = len(vertex_subset)
    if rows:
        data = np.ones(len(rows), dtype=np.float64)
        W_sub = sp.csr_matrix((data, (rows, cols)), shape=(n_sub, n_sub))
    else:
        W_sub = sp.csr_matrix((n_sub, n_sub), dtype=np.float64)
    return GraphState(W_sub), remap


def barcode_summary(bars: List[Tuple[float, float]], l_min: float) -> Dict[str, object]:
    ells = bar_lengths(bars)
    sorted_ells = sorted(ells, reverse=True)
    return {
        "all_bars": [list(b) for b in bars],
        "sorted_lengths": sorted_ells,
        "k_bar_at_l_min": k_bar(bars, l_min),
        "l_min": l_min,
    }


# -----------------------------------------------------------------------------
# CE-1 — high corridor on a path graph
# -----------------------------------------------------------------------------


def ce_1(l_min: float) -> Dict[str, object]:
    """Path graph 0 - 1 - 2 - 3 - 4 with two unit peaks at endpoints.

    High-corridor variant: U = (1.0, 0.5, 0.95, 0.5, 1.0).
      Locally, N_1 = {0, 1} and N_2 = {3, 4} each have one dominant bar of
      length 1.0 (terminal-death essential bar). Globally, the corridor vertex
      x = 2 (in X_bg) is born at 0.95 and dies when both endpoints' components
      annex it at lower threshold, giving an EXTRA finite bar.

    Low-corridor variant: U = (1.0, 0.5, 0.05, 0.5, 1.0).
      Background is suppressed; global K_bar matches local sum.
    """
    g = path_graph(5)
    adj = adjacency_list(g)

    high = np.array([1.0, 0.5, 0.95, 0.5, 1.0])
    low = np.array([1.0, 0.5, 0.05, 0.5, 1.0])

    out: Dict[str, object] = {"description": "Path graph 5, two unit peaks at endpoints"}

    for label, U in [("high_corridor", high), ("low_corridor", low)]:
        global_bars = h0_barcode(U, g)
        # Local neighborhoods (radius 1 around peaks):
        # N_1 = {0, 1}, N_2 = {3, 4}.
        N_1 = [0, 1]
        N_2 = [3, 4]
        g1, _ = induced_graph(g, N_1)
        g2, _ = induced_graph(g, N_2)
        U_N1 = U[N_1]
        U_N2 = U[N_2]
        local_bars_1 = h0_barcode(U_N1, g1)
        local_bars_2 = h0_barcode(U_N2, g2)
        # X_bg = {2}, U value on X_bg
        bg_vertex_value = float(U[2])

        out[label] = {
            "U": U.tolist(),
            "global": barcode_summary(global_bars, l_min),
            "local_N1": barcode_summary(local_bars_1, l_min),
            "local_N2": barcode_summary(local_bars_2, l_min),
            "X_bg_vertices": [2],
            "X_bg_max_U": bg_vertex_value,
            "LG4_passes": bg_vertex_value < l_min,
        }

    # Diagnose the discrepancy
    out["interpretation"] = {
        "high_corridor": (
            "U(corridor) >= l_min, so LG-4 fails. The corridor produces an "
            "extra global bar from a vertex in X_bg."),
        "low_corridor": (
            "U(corridor) < l_min, so LG-4 holds. Global K_bar matches the "
            "sum of local dominant bars (= 2)."),
        "lesson": (
            "LG-4 (background suppression) is necessary. CE-1 demonstrates "
            "the high-corridor failure mode listed in L1F-F2 and the "
            "background-bar failure mode L1H-F3."),
    }
    return out


# -----------------------------------------------------------------------------
# CE-2 — background dominant residual on a dumbbell
# -----------------------------------------------------------------------------


def ce_2(l_min: float) -> Dict[str, object]:
    """Dumbbell-like graph: two cliques A and B joined by a path; an extra
    isolated background spike vertex with high residual.

    Vertices:
      0, 1   : N_A (active region 1, two-vertex clique)
      2, 3   : path bridging the two regions
      4, 5   : N_B (active region 2, two-vertex clique)
      6      : isolated background spike vertex (only adjacent to vertex 3)

    U values:
      U(0) = 1.0, U(1) = 0.9   peak in A
      U(2) = 0.05              low corridor
      U(3) = 0.05              low corridor
      U(4) = 0.9, U(5) = 1.0   peak in B
      U(6) = 0.5               background spike >= l_min

    Local barcodes on N_A and N_B each give one dominant bar near 1.0.
    Global barcode contains an extra dominant bar of length ~0.5 from the
    background spike vertex 6 in X_bg.
    """
    n = 7
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (3, 6)]
    rows: List[int] = []
    cols: List[int] = []
    for i, j in edges:
        rows.extend([i, j])
        cols.extend([j, i])
    data = np.ones(len(rows), dtype=np.float64)
    g = GraphState(sp.csr_matrix((data, (rows, cols)), shape=(n, n)))
    U = np.array([1.0, 0.9, 0.05, 0.05, 0.9, 1.0, 0.5])

    global_bars = h0_barcode(U, g)
    N_A = [0, 1]
    N_B = [4, 5]
    g1, _ = induced_graph(g, N_A)
    g2, _ = induced_graph(g, N_B)
    local_bars_A = h0_barcode(U[N_A], g1)
    local_bars_B = h0_barcode(U[N_B], g2)
    bg_max_U = float(np.max(U[[2, 3, 6]]))
    return {
        "description": "Dumbbell-like + isolated background spike",
        "U": U.tolist(),
        "edges": edges,
        "global": barcode_summary(global_bars, l_min),
        "local_N_A": barcode_summary(local_bars_A, l_min),
        "local_N_B": barcode_summary(local_bars_B, l_min),
        "X_bg_vertices": [2, 3, 6],
        "X_bg_max_U": bg_max_U,
        "LG4_passes": bg_max_U < l_min,
        "interpretation": (
            "Vertex 6 has U(6) = 0.5 >= l_min = 0.10, so LG-4 fails. Globally "
            "vertex 6 produces a finite bar (born at 0.5, dying at 0.05 when "
            "vertex 3 enters), of length 0.45. Locally on N_A and N_B this "
            "bar is invisible, so K_bar(global) - sum local = 1 (overcount) "
            "demonstrating the L1H-F3 failure mode."),
    }


# -----------------------------------------------------------------------------
# CE-3 — local secondary near l_min, perturbation-defeated
# -----------------------------------------------------------------------------


def ce_3(l_min: float) -> Dict[str, object]:
    """Single neighborhood with a primary peak and a borderline-secondary peak.

    Path: 0 - 1 - 2 - 3 - 4 (so N = whole graph here for simplicity).
    Slot field u^(1):  U(0) = 1.0, U(1) = 0.5, U(2) = 0.4, U(3) = 0.5, U(4) = 0.55.
      Primary at vertex 0, secondary near vertex 4.
      Local secondary bar length ~ U(4) - U(2) = 0.55 - 0.4 = 0.15 (just above
      l_min = 0.10).

    A second slot u^(2) (small perturbation): adds a uniform 0.05 to every
    vertex.  Then U_total = u^(1) + u^(2):
      (1.05, 0.55, 0.45, 0.55, 0.60). Same barcode topology, lengths shifted by
      0 (uniform shift cancels in bar lengths).

    A non-uniform perturbation may push the secondary above or below l_min.
    The example illustrates that the bottleneck stability adds 2 rho_pert in
    the WRONG direction; tighter H6 is needed.
    """
    g = path_graph(5)
    u_slot = np.array([1.0, 0.5, 0.4, 0.5, 0.55])
    bars_slot = h0_barcode(u_slot, g)
    # Perturbation that targets the secondary peak (push secondary up)
    rho_pert = 0.04
    perturb = np.array([0.0, 0.0, 0.0, 0.0, rho_pert])  # bumps vertex 4
    u_total = u_slot + perturb
    bars_total = h0_barcode(u_total, g)

    # Slot-internal barcode: ell_{j,2}
    ells_slot = sorted(bar_lengths(bars_slot), reverse=True)
    ells_total = sorted(bar_lengths(bars_total), reverse=True)
    return {
        "description": "Single 5-vertex path; slot u^(1) with borderline-secondary",
        "u_slot_only": u_slot.tolist(),
        "u_perturbed": u_total.tolist(),
        "rho_pert_applied": rho_pert,
        "slot_bars": barcode_summary(bars_slot, l_min),
        "perturbed_bars": barcode_summary(bars_total, l_min),
        "ell_{j,2}_slot_only": ells_slot[1] if len(ells_slot) > 1 else 0.0,
        "ell_{j,2}_perturbed": ells_total[1] if len(ells_total) > 1 else 0.0,
        "interpretation": (
            "Slot-internal secondary bar length is ~0.15 > l_min = 0.10. A "
            "non-uniform residual perturbation can push it further; in the "
            "bottleneck-stability argument the bound is "
            "|ell_{j,2}(U) - ell_{j,2}(u^(j))| <= 2 rho_pert. So H6 must be "
            "tightened to ell_{j,2}(u^(j)) <= l_min - 3 rho_pert (1 buffer + "
            "2 from bottleneck) for the upper-bound argument to close. CE-3 "
            "documents this constant-tightening obligation."),
    }


# -----------------------------------------------------------------------------
# CE-4 — terminal-bar reassignment with equal peaks
# -----------------------------------------------------------------------------


def ce_4(l_min: float) -> Dict[str, object]:
    """Two equal-height active peaks: both N_1 and N_2 give a bar of length 1.0
    locally; globally one is the terminal essential bar (length 1.0) and the
    other becomes a finite bar that dies at the corridor merge level.

    Path 0-1-2-3-4, U = (1.0, 0.5, 0.05, 0.5, 1.0).  Same as low-corridor
    CE-1, repeated here for clarity of the elder-rule reassignment point.
    """
    g = path_graph(5)
    U = np.array([1.0, 0.5, 0.05, 0.5, 1.0])
    bars = h0_barcode(U, g)
    return {
        "description": "Two equal-height peaks; elder-rule terminal bar",
        "U": U.tolist(),
        "global": barcode_summary(bars, l_min),
        "interpretation": (
            "Both peaks born at 1.0; one survives as terminal (death=0, "
            "length 1.0), the other dies at corridor merge level (length "
            "~0.95). K_bar count = |A| = 2 either way, so this is NOT a "
            "counterexample to the count theorem. It only documents that "
            "LG-6 elder-rule compatibility is required to make the bar-to-"
            "slot assignment well-defined."),
    }


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(
        description="L1-H counterexample / boundary exhibit script.")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--l_min", type=float, default=0.10)
    args = p.parse_args()

    t0 = time.time()
    out = {
        "script": "l1h_local_to_global_counterexample.py",
        "purpose": "Finite-graph counterexamples / boundary exhibits for "
                   "L1-H Local-to-Global Barcode Transfer (working-grade).",
        "non_claims": {
            "L1_proved": False,
            "L1F_promoted_to_Cat_A": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "K_bar_equals_K_act_globally": False,
            "K_soft_equals_K_act_globally": False,
            "sigma_rich_sufficient": False,
            "reservoir_canonical": False,
            "exhibit_is_theorem_proof": False,
        },
        "l_min": args.l_min,
        "exhibits": {
            "CE_1": ce_1(args.l_min),
            "CE_2": ce_2(args.l_min),
            "CE_3": ce_3(args.l_min),
            "CE_4": ce_4(args.l_min),
        },
        "wall_clock_seconds": time.time() - t0,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=2, default=lambda o: o.tolist()
                  if isinstance(o, np.ndarray) else
                  (int(o) if isinstance(o, (np.integer,)) else
                   (float(o) if isinstance(o, (np.floating,)) else
                    (_ for _ in ()).throw(TypeError(f"unsupported {type(o)}")))))

    # Console summary
    print(f"[l1h-ce] Wrote {args.output}")
    for name in ["CE_1", "CE_2", "CE_3", "CE_4"]:
        ex = out["exhibits"][name]
        if name == "CE_1":
            for v in ["high_corridor", "low_corridor"]:
                e = ex[v]
                print(f"  {name}/{v}: K_bar(global)={e['global']['k_bar_at_l_min']}, "
                      f"K_bar(N1)={e['local_N1']['k_bar_at_l_min']}, "
                      f"K_bar(N2)={e['local_N2']['k_bar_at_l_min']}, "
                      f"LG4_passes={e['LG4_passes']}")
        elif name == "CE_2":
            print(f"  {name}: K_bar(global)={ex['global']['k_bar_at_l_min']}, "
                  f"K_bar(N_A)={ex['local_N_A']['k_bar_at_l_min']}, "
                  f"K_bar(N_B)={ex['local_N_B']['k_bar_at_l_min']}, "
                  f"LG4_passes={ex['LG4_passes']}")
        elif name == "CE_3":
            print(f"  {name}: ell_{{j,2}} slot={ex['ell_{j,2}_slot_only']:.3f}, "
                  f"perturbed={ex['ell_{j,2}_perturbed']:.3f}, "
                  f"K_bar(global)={ex['perturbed_bars']['k_bar_at_l_min']}")
        elif name == "CE_4":
            print(f"  {name}: K_bar(global)={ex['global']['k_bar_at_l_min']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
