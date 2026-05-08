"""VP-9 (Gate 4 — OP-OMS-002+): Basin test for non-trivial V_2 / V_{2,τ}.

Tests the OP-OMS-002+ closure: a non-trivial admissible V with at
least 2 basins exists. We evaluate V_2 and V_{2,τ} on a triangular grid
of Δ² (static face), run discrete gradient descent on the grid, and
count attractors with their P^sm readouts.

Method:
  1. Pick two targets λ^(1) = (0.70, 0.15, 0.15) (cl-dominant) and
                       λ^(2) = (0.15, 0.70, 0.15) (sep-dominant)
     and pre-compute their P^sm readouts y_1, y_2 ∈ R^6.
  2. Build a triangular grid on Δ² with K subdivisions (K=12 → 91 points).
  3. At each grid point λ, run `find_formation`, compute P^sm(λ), then
     V_{2,τ}(λ) = -τ log(exp(-D_1/τ) + exp(-D_2/τ)) for τ ∈ {0.01, 0.1}
     with D_i = ||P^sm(λ) - y_i||^2.
  4. Discrete gradient descent on the grid: from each point, follow
     V_{2,τ} downhill via the 6-neighbor adjacency until reaching a local
     min.
  5. Cluster grid points by their attractor and report basin sizes /
     P^sm distinctness.

Outputs:
  CODE/experiments/results/observer_moduli/vp9_nontrivial_v_basin.json
  CODE/experiments/results/observer_moduli/vp9_nontrivial_v_basin.md
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


def make_scene_S3() -> GraphState:
    return GraphState.grid_2d(6, 6)


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


SCENES = {
    "P12_path":   make_scene_P12,
    "S3_grid6x6": make_scene_S3,
}


# ---------------------------------------------------------------------------
# Target λ points
# ---------------------------------------------------------------------------

TARGETS = {
    "y1_cl_dominant":  np.array([0.70, 0.15, 0.15]),
    "y2_sep_dominant": np.array([0.15, 0.70, 0.15]),
}


# ---------------------------------------------------------------------------
# P^sm readout
# ---------------------------------------------------------------------------

def evaluate_psm(graph: GraphState, lam: np.ndarray,
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

    P_sm = np.array([d.bind, d.sep, d.inside, d.persist,
                     float(l_max), float(l_second)])
    n_high = int(np.sum(u > 0.5))
    n_core = int(np.sum(u >= 0.9))
    return {
        "ok": True,
        "P_sm": P_sm.tolist(),
        "branch_id": (n_core, n_high),
        "energy": float(result.energy),
    }


# ---------------------------------------------------------------------------
# Triangular grid
# ---------------------------------------------------------------------------

def triangular_grid(K: int) -> list[tuple[int, int, int]]:
    pts = []
    for i in range(K + 1):
        for j in range(K - i + 1):
            k = K - i - j
            pts.append((i, j, k))
    return pts


def grid_neighbors_dict(idx_map: dict, K: int) -> dict[int, list[int]]:
    neighbors: dict[int, list[int]] = {}
    for (i, j, k), idx_a in idx_map.items():
        adj = []
        for di, dj, dk in [(1, -1, 0), (-1, 1, 0),
                            (1, 0, -1), (-1, 0, 1),
                            (0, 1, -1), (0, -1, 1)]:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni <= K and 0 <= nj <= K and 0 <= nk <= K \
                    and ni + nj + nk == K and (ni, nj, nk) in idx_map:
                adj.append(idx_map[(ni, nj, nk)])
        neighbors[idx_a] = adj
    return neighbors


# ---------------------------------------------------------------------------
# V_{2,τ} construction
# ---------------------------------------------------------------------------

def soft_min(D1: float, D2: float, tau: float) -> float:
    """V_{2,τ} = -τ log(exp(-D1/τ) + exp(-D2/τ)) with stable computation."""
    if tau <= 0:
        return min(D1, D2)
    a = -D1 / tau
    b = -D2 / tau
    m = max(a, b)
    return -tau * (m + float(np.log(np.exp(a - m) + np.exp(b - m))))


# ---------------------------------------------------------------------------
# Discrete gradient descent on grid
# ---------------------------------------------------------------------------

def descent_to_attractor(start: int, V: np.ndarray,
                         neighbors: dict[int, list[int]]) -> int:
    """Greedy descent: from `start`, repeatedly move to the lowest-V
    neighbor until no neighbor has lower V. Returns the attractor index."""
    cur = start
    visited = {cur}
    while True:
        best_n = None
        best_v = V[cur]
        for nb in neighbors[cur]:
            if V[nb] < best_v - 1e-12 and nb not in visited:
                best_v = V[nb]
                best_n = nb
        if best_n is None:
            return cur
        visited.add(best_n)
        cur = best_n


# ---------------------------------------------------------------------------
# Main routine
# ---------------------------------------------------------------------------

def run_scene(graph: GraphState, scene_name: str, K: int = 12,
              taus: list[float] = (0.01, 0.1),
              volume_fraction: float = 0.3) -> dict:
    print(f"\n  ── Scene {scene_name} (n={graph.n}) — K={K} ──", flush=True)

    pts = triangular_grid(K)
    idx_map = {p: i for i, p in enumerate(pts)}
    neighbors = grid_neighbors_dict(idx_map, K)
    n_pts = len(pts)
    print(f"  {n_pts} grid points; computing P^sm at each…", flush=True)

    # Step 1: compute P^sm at targets
    target_psms: dict[str, np.ndarray] = {}
    for tname, tlam in TARGETS.items():
        ev = evaluate_psm(graph, tlam, volume_fraction)
        if not ev["ok"]:
            return {"ok": False, "error": f"target {tname} failed: {ev.get('error')}"}
        target_psms[tname] = np.array(ev["P_sm"])
        print(f"    target {tname}: λ={tlam.tolist()}  P^sm={[round(x, 3) for x in ev['P_sm']]} branch={ev['branch_id']}",
              flush=True)
    y1 = target_psms["y1_cl_dominant"]
    y2 = target_psms["y2_sep_dominant"]
    sep_y = float(np.linalg.norm(y1 - y2))
    print(f"    ||y1 - y2|| = {sep_y:.4f}", flush=True)

    # Step 2: evaluate P^sm at every grid point
    psms = np.zeros((n_pts, 6))
    branches: list[tuple[int, int]] = []
    energies = np.zeros(n_pts)
    psm_ok = np.zeros(n_pts, dtype=bool)
    t0 = time.time()
    for i, (a, b, c) in enumerate(pts):
        lam = np.array([a / K, b / K, c / K])
        ev = evaluate_psm(graph, lam, volume_fraction, n_restarts=2)
        if not ev["ok"]:
            branches.append((-1, -1))
            continue
        psms[i] = np.array(ev["P_sm"])
        branches.append(tuple(ev["branch_id"]))
        energies[i] = ev["energy"]
        psm_ok[i] = True
        if (i + 1) % 20 == 0 or i == 0:
            elapsed = time.time() - t0
            eta = elapsed / (i + 1) * (n_pts - i - 1)
            print(f"   [{i+1:>3}/{n_pts}] {elapsed:.0f}s elapsed, eta {eta:.0f}s",
                  flush=True)

    # Step 3: V_{2,τ} on grid for each τ
    per_tau_results = {}
    for tau in taus:
        D1 = np.sum((psms - y1) ** 2, axis=1)
        D2 = np.sum((psms - y2) ** 2, axis=1)
        V = np.array([soft_min(float(D1[i]), float(D2[i]), tau)
                      for i in range(n_pts)])
        # Mark non-ok points as +∞
        V[~psm_ok] = np.inf

        # Discrete descent
        attractor = np.zeros(n_pts, dtype=int)
        for i in range(n_pts):
            if not psm_ok[i]:
                attractor[i] = -1
                continue
            attractor[i] = descent_to_attractor(i, V, neighbors)

        # Cluster
        unique_attr = sorted({int(a) for a in attractor if a >= 0})
        basins: dict[int, list[int]] = {a: [] for a in unique_attr}
        for i in range(n_pts):
            if attractor[i] >= 0:
                basins[int(attractor[i])].append(i)

        # P^sm of each attractor + which target it's closer to
        attractor_info = []
        for a in unique_attr:
            psm_a = psms[a]
            d_to_y1 = float(np.linalg.norm(psm_a - y1))
            d_to_y2 = float(np.linalg.norm(psm_a - y2))
            label = "y1" if d_to_y1 < d_to_y2 else "y2"
            attractor_info.append({
                "attractor_index": a,
                "lam": [pts[a][0] / K, pts[a][1] / K, pts[a][2] / K],
                "P_sm": psm_a.tolist(),
                "branch_id": list(branches[a]),
                "V_value": float(V[a]),
                "d_to_y1": d_to_y1,
                "d_to_y2": d_to_y2,
                "closer_to": label,
                "basin_size": len(basins[a]),
                "basin_fraction": len(basins[a]) / n_pts,
            })

        # Distinct-readout pairs
        n_distinct_readouts = 0
        for i in range(len(attractor_info)):
            for j in range(i + 1, len(attractor_info)):
                d_ij = float(np.linalg.norm(
                    np.array(attractor_info[i]["P_sm"]) - np.array(attractor_info[j]["P_sm"])
                ))
                if d_ij > 0.1:
                    n_distinct_readouts += 1

        per_tau_results[f"tau={tau}"] = {
            "tau": tau,
            "n_attractors": len(unique_attr),
            "attractors": attractor_info,
            "n_distinct_readout_pairs": n_distinct_readouts,
            "min_attractor_V": float(V[unique_attr].min()) if unique_attr else None,
            "max_attractor_V": float(V[unique_attr].max()) if unique_attr else None,
            "basin_sizes": [len(basins[a]) for a in unique_attr],
            "basin_fractions": [len(basins[a]) / n_pts for a in unique_attr],
        }
        print(f"   τ={tau}: {len(unique_attr)} attractors, "
              f"basins={[len(basins[a]) for a in unique_attr]}, "
              f"distinct-readout pairs={n_distinct_readouts}",
              flush=True)

    return {
        "ok": True,
        "scene": scene_name,
        "K": K,
        "n_grid_points": n_pts,
        "n_grid_ok": int(psm_ok.sum()),
        "y1_target_psm": y1.tolist(),
        "y2_target_psm": y2.tolist(),
        "norm_y1_y2": sep_y,
        "per_tau": per_tau_results,
    }


def main():
    t0 = time.time()
    print("=== VP-9 (Gate 4): Non-trivial V basin test (V_{2,τ}) ===",
          flush=True)
    print("Compute V_{2,τ} on Δ² grid; discrete descent; count attractors.",
          flush=True)

    all_results = {}
    for scene_name, scene_fn in SCENES.items():
        graph = scene_fn()
        K = 12 if scene_name == "P12_path" else 8  # smaller K for S3 for speed
        all_results[scene_name] = run_scene(graph, scene_name, K=K,
                                             taus=(0.01, 0.1))

    elapsed = time.time() - t0

    # Summarize: did each scene exhibit ≥ 2 attractors with distinct readouts?
    print(f"\n=== VP-9 SUMMARY ===", flush=True)
    nontrivial_count = 0
    total_count = 0
    for scene_name, res in all_results.items():
        if not res.get("ok"):
            continue
        for tau_key, tau_res in res["per_tau"].items():
            total_count += 1
            n_attr = tau_res["n_attractors"]
            n_dist = tau_res["n_distinct_readout_pairs"]
            verdict = "✓ NONTRIVIAL" if (n_attr >= 2 and n_dist >= 1) else "✗ trivial"
            if n_attr >= 2 and n_dist >= 1:
                nontrivial_count += 1
            print(f"  {scene_name} {tau_key}: {n_attr} attractors, "
                  f"{n_dist} distinct readout pairs  → {verdict}",
                  flush=True)
    print(f"\n  Nontrivial cases: {nontrivial_count}/{total_count}",
          flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)

    output = {
        "experiment": "VP-9 Non-trivial V basin test",
        "date": "2026-05-08",
        "session": "Session 6 (OMS-2.0 push)",
        "method": "V_{2,τ} on triangular Δ² grid; discrete gradient "
                  "descent on grid; basin counting + P^sm-distinctness check.",
        "targets": {k: v.tolist() for k, v in TARGETS.items()},
        "taus": [0.01, 0.1],
        "scenes": list(SCENES.keys()),
        "per_scene": all_results,
        "n_nontrivial_cases": nontrivial_count,
        "n_total_cases": total_count,
        "OP_OMS_002_status": ("COMPUTATIONALLY_SUPPORTED"
                               if nontrivial_count == total_count
                               else "PARTIALLY_SUPPORTED"
                               if nontrivial_count > 0
                               else "NOT_SUPPORTED"),
        "elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-002+", "Prop NV7 (basin nontriviality)"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp9_nontrivial_v_basin.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    md = ["# VP-9 — Non-trivial V Basin Test Summary",
          "",
          f"**Date:** 2026-05-08  ",
          f"**Experiment:** vp9_nontrivial_v_basin_test.py  ",
          f"**Attacks:** OP-OMS-002+ (non-trivial admissible V; Prop NV7)  ",
          f"**Elapsed:** {elapsed:.1f}s",
          "",
          "## Method",
          "",
          "Build $V_{2,\\tau}(\\lambda) = -\\tau \\log(\\exp(-D_1/\\tau) + \\exp(-D_2/\\tau))$ "
          "with $D_i = \\|P^{\\mathrm{sm}}(\\lambda) - y_i\\|_2^2$ for two targets "
          "$y_1, y_2$ (cl-dominant and sep-dominant readouts).",
          "Evaluate on triangular Δ² grid; discrete gradient descent on the 6-neighbor adjacency; "
          "cluster grid points by attractor; report basin sizes and P^sm distinctness.",
          "",
          "## Per-scene results",
          ""]
    for scene_name, res in all_results.items():
        md.append(f"### {scene_name}")
        md.append("")
        if not res.get("ok"):
            md.append(f"FAILED: {res.get('error')}")
            md.append("")
            continue
        md.append(f"- K = {res['K']} → {res['n_grid_points']} grid points "
                  f"(ok: {res['n_grid_ok']})")
        md.append(f"- ||y_1 - y_2|| = {res['norm_y1_y2']:.4f}")
        md.append("")
        for tau_key, tau_res in res["per_tau"].items():
            md.append(f"**{tau_key}:** {tau_res['n_attractors']} attractors, "
                      f"basin sizes {tau_res['basin_sizes']}, "
                      f"distinct readout pairs = {tau_res['n_distinct_readout_pairs']}")
            md.append("")
            md.append("| attractor | λ | branch | basin frac | closer_to | V |")
            md.append("|---|---|---|---|---|---|")
            for a in tau_res["attractors"]:
                md.append(f"| {a['attractor_index']} | "
                          f"({a['lam'][0]:.2f},{a['lam'][1]:.2f},{a['lam'][2]:.2f}) | "
                          f"{tuple(a['branch_id'])} | "
                          f"{a['basin_fraction']:.2%} | "
                          f"{a['closer_to']} | {a['V_value']:.4f} |")
            md.append("")

    md.append("## OP-OMS-002+ classification")
    md.append("")
    md.append(f"**Nontrivial cases (≥2 attractors with distinct readouts):** "
              f"{nontrivial_count}/{total_count}")
    md.append("")
    if nontrivial_count == total_count:
        md.append("All scenes / τ settings exhibit ≥ 2 distinct attractors. "
                  "**OP-OMS-002+ COMPUTATIONALLY SUPPORTED.**")
    elif nontrivial_count > 0:
        md.append("Some but not all scenes / τ settings exhibit ≥ 2 distinct attractors. "
                  "**OP-OMS-002+ PARTIALLY SUPPORTED.**")
    else:
        md.append("No scene / τ exhibits ≥ 2 distinct attractors. **OP-OMS-002+ NOT SUPPORTED** "
                  "(would invalidate Prop NV7 / require larger τ-c offset).")

    md_path = os.path.join(RESULTS_DIR, "vp9_nontrivial_v_basin.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
