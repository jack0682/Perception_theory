"""VP-10 (Gate 6 — OP-OMS-026): Pseudo-Δ³ branch map.

Tetrahedral grid on the full simplex Δ³ = {λ ∈ R^4_{≥0} : Σ λ_i = 1}.
Per-point optimization, branch-id, and edge-based transition counting.

This is **pseudo-Δ³** because we use a static scene (single time slice),
on which E_tr is degenerate (λ_tr-direction is gauge-redundant by
Prop CW2). The result tests SB11 (B)–(C) at the codim-1 level: the
transition surface should remain ≤ 2-dimensional in the 3-D simplex.

Method:
  1. Tetrahedral grid: all (i, j, k, l) with i+j+k+l = K, K=8 → 165 points.
  2. At each point λ = (i/K, j/K, k/K, l/K), run `find_formation`,
     record branch identifier (n_core, n_high).
  3. Edges: 4 neighbors per interior point in the tetrahedral lattice
     (move one of the 4 coordinates ±1, change another ∓1).
  4. Σ_branch ≈ edges with different branch identifiers at endpoints.
  5. Report dominant branch fractions and codim-1 evidence.

Outputs:
  CODE/experiments/results/observer_moduli/vp10_sigma_branch_delta3.json
  CODE/experiments/results/observer_moduli/vp10_sigma_branch_delta3.md
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


def make_scene_P12() -> GraphState:
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


def tetrahedral_grid(K: int) -> list[tuple[int, int, int, int]]:
    """All (i, j, k, l) with i + j + k + l = K, i, j, k, l ≥ 0."""
    pts = []
    for i in range(K + 1):
        for j in range(K - i + 1):
            for k in range(K - i - j + 1):
                l = K - i - j - k
                pts.append((i, j, k, l))
    return pts


def tet_neighbors(idx_map: dict, K: int) -> list[tuple[int, int]]:
    """Neighbors: change one coordinate +1, another -1 (12 directions)."""
    edges = []
    for (i, j, k, l), idx_a in idx_map.items():
        coords = (i, j, k, l)
        for p in range(4):
            for q in range(4):
                if p == q:
                    continue
                new = list(coords)
                new[p] += 1; new[q] -= 1
                if all(0 <= x <= K for x in new) and tuple(new) in idx_map:
                    idx_b = idx_map[tuple(new)]
                    if idx_a < idx_b:
                        edges.append((idx_a, idx_b))
    return edges


THETA_CORE = 0.9


def evaluate_lambda(graph: GraphState, lam: tuple[float, float, float, float],
                    volume_fraction: float = 0.3,
                    n_restarts: int = 2) -> dict:
    params = ParameterRegistry()
    params.w_cl  = float(lam[0])
    params.w_sep = float(lam[1])
    params.w_bd  = float(lam[2])
    params.w_tr  = float(lam[3])
    params.volume_fraction = volume_fraction
    params.n_restarts = n_restarts

    try:
        result = find_formation(graph, params)
    except Exception as exc:
        return {"ok": False, "error": str(exc)}

    u = result.u
    n_high = int(np.sum(u > 0.5))
    n_core = int(np.sum(u >= THETA_CORE))
    return {
        "ok": True,
        "energy": float(result.energy),
        "u_max": float(u.max()),
        "n_high": n_high,
        "n_core": n_core,
        "branch_id": (n_core, n_high),
    }


def map_scene_delta3(graph: GraphState, scene_name: str, K: int = 8,
                     volume_fraction: float = 0.3) -> dict:
    pts = tetrahedral_grid(K)
    idx_map = {p: i for i, p in enumerate(pts)}
    print(f"\n  ── Scene {scene_name}: K={K} → {len(pts)} tetrahedral points ──",
          flush=True)

    evaluations = []
    t_start = time.time()
    for i, (a, b, c, d) in enumerate(pts):
        lam = (a / K, b / K, c / K, d / K)
        ev = evaluate_lambda(graph, lam, volume_fraction)
        ev["index"]     = i
        ev["lam"]       = list(lam)
        ev["barycoord"] = (a, b, c, d)
        evaluations.append(ev)
        if (i + 1) % 25 == 0 or i == 0:
            elapsed = time.time() - t_start
            eta = elapsed / (i + 1) * (len(pts) - i - 1)
            print(f"   [{i+1:>3}/{len(pts)}] λ=({lam[0]:.2f},{lam[1]:.2f},"
                  f"{lam[2]:.2f},{lam[3]:.2f}) branch={ev.get('branch_id', '?')}  "
                  f"E={ev.get('energy', float('nan')):.3f}  "
                  f"elapsed={elapsed:.0f}s  eta={eta:.0f}s",
                  flush=True)

    edges = tet_neighbors(idx_map, K)

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
            })

    branch_classes: dict[tuple[int, int], int] = {}
    for ev in evaluations:
        if not ev.get("ok"):
            continue
        b = tuple(ev["branch_id"])
        branch_classes[b] = branch_classes.get(b, 0) + 1

    elapsed = time.time() - t_start
    print(f"\n  → {len(branch_classes)} distinct branches; "
          f"{len(transition_edges)} transition edges (out of {len(edges)} total)",
          flush=True)
    for b, n in sorted(branch_classes.items(), key=lambda x: -x[1])[:8]:
        print(f"    branch {b}: {n} grid points ({100.0*n/len(pts):.1f}%)",
              flush=True)

    # Codim-1 evidence: ratio of transition edges to total edges
    n_edges = len(edges)
    transition_fraction = len(transition_edges) / max(n_edges, 1)

    # If Σ_branch is codim-1 in 3-D simplex, transition edges should be ~ a 2D surface.
    # In a tetrahedral lattice with K subdivisions, # interior 1-cells ≈ O(K^3).
    # # transition edges ≈ # tet faces hit by Σ_branch ≈ O(K^2).
    # So transition_fraction ~ 1/K. For K=8, expected ~0.125 if fully codim-1.
    expected_codim1 = 1.0 / K

    return {
        "scene": scene_name,
        "K": K,
        "n_points": len(pts),
        "n_restarts": 2,
        "volume_fraction": volume_fraction,
        "evaluations": [{k: (list(v) if isinstance(v, tuple) else v)
                         for k, v in ev.items()}
                        for ev in evaluations],
        "n_branch_classes": len(branch_classes),
        "branch_classes": [
            {"branch_id": list(b), "count": n,
             "fraction": n / len(pts)}
            for b, n in sorted(branch_classes.items(), key=lambda x: -x[1])
        ],
        "transition_edges": transition_edges,
        "n_transition_edges": len(transition_edges),
        "n_total_edges": n_edges,
        "transition_fraction": transition_fraction,
        "expected_codim1_fraction": expected_codim1,
        "codim1_consistent": (transition_fraction <= 3 * expected_codim1),
        "elapsed_s": round(elapsed, 1),
    }


def main():
    t0 = time.time()
    print("=== VP-10 (Gate 6): Pseudo-Δ³ Σ_branch map ===", flush=True)
    print("Tetrahedral grid in λ ∈ Δ³; per-point optimizer; codim-1 check.",
          flush=True)
    print("PSEUDO-Δ³: static scene → λ_tr is gauge-redundant (Prop CW2). "
          "Tests SB11 (B)-(C) at the 3D-simplex codim-1 level.\n",
          flush=True)

    # Use only P12 (smallest, fastest) at K=8 for tractable runtime
    # K=8 → 165 points × ~0.5–2s each = 80–300s
    scenes = [
        ("P12_path", make_scene_P12(), 8),
    ]

    all_results = {}
    for name, graph, K in scenes:
        all_results[name] = map_scene_delta3(graph, name, K=K)

    elapsed = time.time() - t0

    print(f"\n=== VP-10 SUMMARY ===", flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)
    for name, res in all_results.items():
        print(f"  {name}: {res['n_branch_classes']} branches, "
              f"{res['n_transition_edges']}/{res['n_total_edges']} transition edges "
              f"({res['transition_fraction']:.3f} fraction; "
              f"expected codim-1 ≤ {3*res['expected_codim1_fraction']:.3f})",
              flush=True)
        print(f"    codim-1 consistent: "
              f"{'YES' if res['codim1_consistent'] else 'NO'}",
              flush=True)

    output = {
        "experiment": "VP-10 Pseudo-Δ³ Σ_branch map",
        "date": "2026-05-08",
        "session": "Session 6 (OMS-2.0 push)",
        "method": "Tetrahedral grid (K=8) on Δ³, static scene "
                  "(λ_tr-direction degenerate by Prop CW2). "
                  "Tests SB11 (B)-(C) codim-1 evidence.",
        "PSEUDO_DELTA3_caveat": ("This is a pseudo-Δ³ map: λ_tr is "
                                  "gauge-redundant on the static scene. "
                                  "Full temporal Δ³ would require multi-time "
                                  "scc.multi infrastructure."),
        "scenes": list(all_results.keys()),
        "per_scene": all_results,
        "total_elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-026 (full Δ³ Σ_branch)", "Theorem SB11 (B)-(C)"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp10_sigma_branch_delta3.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    md = ["# VP-10 — Pseudo-Δ³ Σ_branch Map Summary",
          "",
          f"**Date:** 2026-05-08  ",
          f"**Experiment:** vp10_sigma_branch_delta3.py  ",
          f"**Attack:** OP-OMS-026 — full Σ_branch on Δ³  ",
          f"**Caveat:** **PSEUDO-Δ³** (static scene; λ_tr-direction degenerate by Prop CW2).  ",
          f"**Elapsed:** {elapsed:.1f}s  ",
          "",
          "## Method",
          "",
          "Tetrahedral grid on the 3-simplex Δ³ ⊂ R^4 (4 weights summing to 1).",
          "K = 8 → $\\binom{K+3}{3} = 165$ grid points per scene.",
          "Per-point `find_formation`, branch identifier $(n_{\\mathrm{core}}, n_{\\mathrm{high}})$.",
          "Edges = unit moves in tetrahedral lattice (12 directions per interior point).",
          "Transition edges = endpoints with different branch IDs ⇒ Σ_branch crosses the edge.",
          "",
          "## Codim-1 evidence criterion",
          "",
          "If Σ_branch is codim-1 in 3D Δ³, transition edges should constitute "
          "a fraction $\\sim 1/K$ of all edges (the surface intersects the 1-skeleton "
          "in $O(K^2)$ edges out of $O(K^3)$ total). Fraction within $3 \\times 1/K$ "
          "is taken as 'codim-1 consistent'.",
          "",
          "## Per-scene results",
          ""]

    for name, res in all_results.items():
        md.append(f"### {name}")
        md.append("")
        md.append(f"- K = {res['K']} → {res['n_points']} grid points")
        md.append(f"- distinct branches: {res['n_branch_classes']}")
        md.append(f"- transition edges: {res['n_transition_edges']} / "
                  f"{res['n_total_edges']} = {res['transition_fraction']:.3f}")
        md.append(f"- expected codim-1 fraction (≤ 3/K): "
                  f"{3 * res['expected_codim1_fraction']:.3f}")
        md.append(f"- **codim-1 consistent: "
                  f"{'YES' if res['codim1_consistent'] else 'NO'}**")
        md.append("")
        md.append("| branch (n_core, n_high) | count | fraction |")
        md.append("|---|---|---|")
        for c in res["branch_classes"][:10]:
            md.append(f"| {tuple(c['branch_id'])} | {c['count']} | "
                      f"{c['fraction']:.2%} |")
        md.append("")

    md += ["## Conclusion",
           "",
           "**OP-OMS-026 codim-1 part computational support:**"]

    all_codim1 = all(r["codim1_consistent"] for r in all_results.values())
    if all_codim1:
        md.append("All scenes pass the codim-1 consistency check. "
                  "Theorem SB11 (B)-(C) is COMPUTATIONALLY SUPPORTED.")
    else:
        md.append("Some scenes exceed the codim-1 budget. Possible explanations: "
                  "K=8 is too coarse; or the scene has many small branches. "
                  "(P12 had 7 branches on Δ² at K=10; expect more on Δ³.)")
    md.append("")
    md.append("**Pseudo-Δ³ caveat acknowledged.** The result tests the codim-1 "
              "structure on the simplex with $\\lambda_{tr}$ included formally "
              "but degenerate. Full temporal Δ³ would require non-degenerate "
              "$E_{tr}$, achievable via `scc.multi.transport_k_formations` on a "
              "two-time-slice scene; deferred as a sub-OP.")
    md.append("")

    md_path = os.path.join(RESULTS_DIR, "vp10_sigma_branch_delta3.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
