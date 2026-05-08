"""VP-7 (OP-OMS-026 attack): Fine-grid Σ_branch mapping on the static face Δ².

Dense triangular grid on the simplex {λ_cl + λ_sep + λ_bd = 1, λ_tr = 0}.
At each grid point, run `find_formation` and record the branch identifier
(K_core, n_high). Adjacent grid points with different branch identifiers
locate the branch-switching surface Σ_branch.

Scenes:
  - P12: path graph on 12 nodes (matches VP-1 setup; smallest non-trivial
    scene where branch transitions are expected).
  - S3:  6×6 grid (matches VP-3 / VP-4 / VP-6).

Grid resolution K — number of subdivisions per simplex side. The
triangular grid has $(K+1)(K+2)/2$ points. K=10 gives 66 points; K=12
gives 91; K=14 gives 120.

Output:
  results/observer_moduli/vp7_branch_map.json   — full grid data
  results/observer_moduli/vp7_branch_map.md     — summary
"""
from __future__ import annotations

import json
import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.diagnostics import diagnostic_vector, _persistence_h0_graph

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(
    os.path.dirname(EXP_DIR), "results", "observer_moduli"
)
os.makedirs(RESULTS_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Scenes
# ---------------------------------------------------------------------------

def make_scene_P12() -> GraphState:
    """Path graph on 12 nodes (matches VP-1)."""
    import scipy.sparse as sp
    n = 12
    rows, cols, data = [], [], []
    for i in range(n - 1):
        rows.extend([i, i + 1])
        cols.extend([i + 1, i])
        data.extend([1.0, 1.0])
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def make_scene_S3() -> GraphState:
    return GraphState.grid_2d(6, 6)


# ---------------------------------------------------------------------------
# Triangular grid on Δ² = {λ_cl + λ_sep + λ_bd = 1}
# ---------------------------------------------------------------------------

def triangular_grid(K: int) -> list[tuple[int, int, int]]:
    """All non-negative integer triples (i, j, k) with i + j + k = K.
    These are (K+1)(K+2)/2 points; (i/K, j/K, k/K) are barycentric."""
    points = []
    for i in range(K + 1):
        for j in range(K - i + 1):
            k = K - i - j
            points.append((i, j, k))
    return points


def grid_neighbors(idx_map: dict, K: int) -> list[tuple[int, int]]:
    """Return adjacency edges in the triangular grid as pairs of point indices.
    Two grid points (i,j,k), (i',j',k') are adjacent iff exactly two of
    (i'-i, j'-j, k'-k) have absolute value 1 and they sum to zero."""
    edges = []
    for (i, j, k), idx_a in idx_map.items():
        for di, dj, dk in [(1, -1, 0), (-1, 1, 0),
                            (1, 0, -1), (-1, 0, 1),
                            (0, 1, -1), (0, -1, 1)]:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni <= K and 0 <= nj <= K and 0 <= nk <= K \
                    and ni + nj + nk == K \
                    and (ni, nj, nk) in idx_map:
                idx_b = idx_map[(ni, nj, nk)]
                if idx_a < idx_b:
                    edges.append((idx_a, idx_b))
    return edges


# ---------------------------------------------------------------------------
# Evaluate λ
# ---------------------------------------------------------------------------

THETA_CORE = 0.9


def evaluate_lambda(graph: GraphState, lam: tuple[float, float, float],
                    volume_fraction: float = 0.3,
                    n_restarts: int = 2) -> dict:
    params = ParameterRegistry()
    params.w_cl  = float(lam[0])
    params.w_sep = float(lam[1])
    params.w_bd  = float(lam[2])
    params.w_tr  = 0.0
    params.volume_fraction = volume_fraction
    params.n_restarts = n_restarts

    try:
        result = find_formation(graph, params)
    except Exception as exc:
        return {"ok": False, "error": str(exc)}

    u = result.u
    d = diagnostic_vector(u, graph, params)
    l_max, l_second = _persistence_h0_graph(u, graph)
    n_high = int(np.sum(u > 0.5))
    n_core = int(np.sum(u >= THETA_CORE))
    n_lo   = int(np.sum(u < 0.05))
    n_hi   = int(np.sum(u > 0.95))
    return {
        "ok": True,
        "energy": float(result.energy),
        "bind":   float(d.bind),
        "sep":    float(d.sep),
        "inside": float(d.inside),
        "persist": float(d.persist),
        "l_max": float(l_max),
        "l_second": float(l_second),
        "u_max": float(u.max()),
        "n_high": n_high,
        "n_core": n_core,
        "n_lo":   n_lo,
        "n_hi":   n_hi,
        "branch_id": (n_core, n_high),
    }


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def map_scene(graph: GraphState, scene_name: str, K: int = 10,
              volume_fraction: float = 0.3,
              n_restarts: int = 2) -> dict:
    pts = triangular_grid(K)
    idx_map = {p: i for i, p in enumerate(pts)}
    print(f"\n  ── Scene {scene_name}: K={K} → {len(pts)} grid points ──",
          flush=True)

    evaluations = []
    t_start = time.time()
    for i, (a, b, c) in enumerate(pts):
        lam = (a / K, b / K, c / K)
        ev = evaluate_lambda(graph, lam, volume_fraction, n_restarts)
        ev["index"]     = i
        ev["lam"]       = list(lam)
        ev["barycoord"] = (a, b, c)
        evaluations.append(ev)
        if (i + 1) % 10 == 0 or i == 0:
            elapsed = time.time() - t_start
            eta = elapsed / (i + 1) * (len(pts) - i - 1)
            print(f"   [{i+1:>3}/{len(pts)}] λ=({lam[0]:.2f},{lam[1]:.2f},"
                  f"{lam[2]:.2f}) branch={ev.get('branch_id', '?')}  "
                  f"E={ev.get('energy', float('nan')):.3f}  "
                  f"elapsed={elapsed:.0f}s  eta={eta:.0f}s",
                  flush=True)

    edges = grid_neighbors(idx_map, K)

    # Identify branch-transition edges
    transition_edges = []
    for a, b in edges:
        ev_a, ev_b = evaluations[a], evaluations[b]
        if not ev_a.get("ok") or not ev_b.get("ok"):
            continue
        if ev_a["branch_id"] != ev_b["branch_id"]:
            transition_edges.append({
                "edge": (a, b),
                "lam_a": ev_a["lam"],
                "lam_b": ev_b["lam"],
                "branch_a": list(ev_a["branch_id"]),
                "branch_b": list(ev_b["branch_id"]),
                "delta_n_core": ev_b["branch_id"][0] - ev_a["branch_id"][0],
                "delta_n_high": ev_b["branch_id"][1] - ev_a["branch_id"][1],
            })

    # Tally distinct branches
    branch_classes: dict[tuple[int, int], int] = {}
    branch_members: dict[tuple[int, int], list[int]] = {}
    for ev in evaluations:
        if not ev.get("ok"):
            continue
        b = tuple(ev["branch_id"])
        branch_classes[b] = branch_classes.get(b, 0) + 1
        branch_members.setdefault(b, []).append(ev["index"])

    print(f"\n  → {len(branch_classes)} distinct branches; "
          f"{len(transition_edges)} transition edges", flush=True)
    for b, n in sorted(branch_classes.items(), key=lambda x: -x[1]):
        print(f"    branch {b}: {n} grid points", flush=True)

    elapsed = time.time() - t_start
    return {
        "scene": scene_name,
        "K": K,
        "n_points": len(pts),
        "n_restarts": n_restarts,
        "volume_fraction": volume_fraction,
        "evaluations": [{k: (list(v) if isinstance(v, tuple) else v)
                         for k, v in ev.items()}
                        for ev in evaluations],
        "n_branch_classes": len(branch_classes),
        "branch_classes": [
            {"branch_id": list(b),
             "count": n,
             "member_indices": branch_members[b],
             "fraction": n / len(pts)}
            for b, n in sorted(branch_classes.items(), key=lambda x: -x[1])
        ],
        "transition_edges": transition_edges,
        "n_transition_edges": len(transition_edges),
        "elapsed_s": round(elapsed, 1),
    }


def main():
    t0 = time.time()
    print("=== VP-7 (OP-OMS-026): Σ_branch mapping on Δ² ===", flush=True)
    print("Dense triangular grid; per-point optimization; "
          "edge-based branch transitions.", flush=True)

    scenes = [
        ("P12_path", make_scene_P12(), 10),  # 66 points
        ("S3_grid6x6", make_scene_S3(),  8),  # 45 points (smaller grid =
                                              #  fewer optimizer calls)
    ]

    all_results = {}
    for name, graph, K in scenes:
        all_results[name] = map_scene(graph, name, K=K, n_restarts=2)

    elapsed = time.time() - t0

    print(f"\n=== VP-7 SUMMARY ===", flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)
    for name, res in all_results.items():
        print(f"  {name}: {res['n_branch_classes']} branches, "
              f"{res['n_transition_edges']} transition edges, "
              f"{res['n_points']} grid points", flush=True)

    output = {
        "experiment": "VP-7 Σ_branch mapping (OP-OMS-026 attack)",
        "date": "2026-05-08",
        "session": "Session 5 continuation",
        "tangent_basis_3": [[1, -1, 0], [1, 1, -2]],
        "method": "fine triangular grid on Δ² static face; per-point "
                  "optimizer; branch-id from (n_core, n_high)",
        "scenes": list(all_results.keys()),
        "per_scene": all_results,
        "total_elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-026", "OP-OMS-024"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp7_branch_map.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    # Markdown summary
    md = ["# VP-7 Σ_branch Mapping Summary",
          "",
          "**Date:** 2026-05-08  ",
          "**Experiment:** vp7_branch_map.py  ",
          "**Attack:** OP-OMS-026 (Σ_branch characterization), "
          "OP-OMS-024 (constant-rank regions)  ",
          f"**Elapsed:** {elapsed:.1f}s",
          "",
          "## Method",
          "",
          "Triangular grid on the static face Δ² ⊂ Δ³ "
          "(λ_cl, λ_sep, λ_bd, λ_tr=0).",
          "Per-point optimization with `find_formation` (n_restarts=2).",
          "Branch identifier = (n_core, n_high). "
          "Edges connect adjacent grid points; "
          "Σ_branch is approximated by edges whose endpoints have "
          "different branch IDs.",
          "",
          "## Per-scene results",
          ""]

    for name, res in all_results.items():
        md.append(f"### {name}")
        md.append("")
        md.append(f"- K = {res['K']} → {res['n_points']} grid points")
        md.append(f"- distinct branches: {res['n_branch_classes']}")
        md.append(f"- transition edges (Σ_branch crossings): "
                  f"{res['n_transition_edges']}")
        md.append("")
        md.append("| branch (n_core, n_high) | count | fraction |")
        md.append("|---|---|---|")
        for c in res["branch_classes"]:
            md.append(f"| {tuple(c['branch_id'])} | {c['count']} | "
                      f"{c['fraction']:.2%} |")
        md.append("")

    md += ["## Interpretation",
           "",
           "**Multiple branches** = multiple perceptual observer types coexist on "
           "the static face. Each branch corresponds to a distinct "
           "(n_core, n_high) signature of u*(λ).",
           "",
           "**Transition edges** = approximate location of the codim-1 "
           "branch-switching surface Σ_branch.",
           "",
           "**Constant-rank region candidates (OP-OMS-024):** Open subsets of "
           "the simplex on which all interior grid points share the same "
           "branch identifier. The largest such subset per scene is a "
           "candidate for a constant-rank region of J_R.",
           ""]

    md_path = os.path.join(RESULTS_DIR, "vp7_branch_map.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
