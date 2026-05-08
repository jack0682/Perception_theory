"""VP-6 path test: u*(λ) regularity along simplex paths.

Numerical companion to OP-OMS-018 attack. Traverses 5 paths in Δ³ and
measures field-level / diagnostic / topology jumps to detect:

  - smooth branches (R1 of `op_oms_018_regular_u_star.md`)
  - kinks (R2 — fixed active-set transitions)
  - branch-switching surfaces Σ_branch (Prop R3 (3))
  - active-set changes (#{u_i ~= 0} or #{u_i ~= 1})

Paths (line segments from λ_start to λ_end, sampled at K=11 points):

  Path 1 (cl-axis):     barycenter → cl-dominant      (P3 → P1, VP-4 labels)
  Path 2 (sep-axis):    barycenter → sep-dominant     (P3 → P2)
  Path 3 (bd-axis):     barycenter → bd-dominant      (P3 → P5)
  Path 4 (VP-1 CE):     λ_A → λ_B (the VP-1 K_core=2 ↔ K_core=1 transition line)
  Path 5 (random):      a fixed-seed pseudo-random line

Outputs:
  CODE/experiments/results/observer_moduli/vp6_u_star_path_results.json
  CODE/experiments/results/observer_moduli/vp6_u_star_path_summary.md
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


def make_scene_S4() -> GraphState:
    import scipy.sparse as sp
    n = 10
    rows, cols, data = [], [], []
    for i in range(5):
        for j in range(5):
            if i != j:
                rows.append(i); cols.append(j); data.append(1.0)
    for i in range(5, 10):
        for j in range(5, 10):
            if i != j:
                rows.append(i); cols.append(j); data.append(1.0)
    rows.extend([4, 5]); cols.extend([5, 4]); data.extend([0.05, 0.05])
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


THETA_CORE = 0.9
ACTIVE_LO = 0.05
ACTIVE_HI = 0.95


def evaluate_lambda(graph: GraphState, lam: np.ndarray,
                    volume_fraction: float = 0.3) -> dict:
    """Evaluate the optimizer at λ, return u*, energy decomp, diagnostics,
    topology summaries, and active-set sizes."""
    params = ParameterRegistry()
    params.w_cl  = float(lam[0])
    params.w_sep = float(lam[1])
    params.w_bd  = float(lam[2])
    params.w_tr  = float(lam[3]) if len(lam) >= 4 else 0.0
    params.volume_fraction = volume_fraction

    try:
        result = find_formation(graph, params)
    except Exception as exc:
        return {"ok": False, "error": str(exc), "lam": lam.tolist()}

    u = result.u
    d = diagnostic_vector(u, graph, params)
    l_max, l_second = _persistence_h0_graph(u, graph)

    return {
        "ok": True,
        "lam": lam.tolist(),
        "u": u.tolist(),
        "energy": float(result.energy),
        "energy_terms": {k: float(v) for k, v in result.energy_terms.items()},
        "bind":   float(d.bind),
        "sep":    float(d.sep),
        "inside": float(d.inside),
        "persist": float(d.persist),
        "l_max":  float(l_max),
        "l_second": float(l_second),
        "u_max":   float(u.max()),
        "u_mean":  float(u.mean()),
        "n_active_lo": int(np.sum(u < ACTIVE_LO)),
        "n_active_hi": int(np.sum(u > ACTIVE_HI)),
        "n_high":     int(np.sum(u > 0.5)),
        "n_core":     int(np.sum(u >= THETA_CORE)),
        "converged":  bool(result.converged),
        "n_iter":     int(result.n_iter),
    }


def project_simplex(lam: np.ndarray) -> np.ndarray:
    lam = np.clip(lam, 0.0, None)
    s = lam.sum()
    if s <= 1e-12:
        return np.full_like(lam, 1.0 / len(lam))
    return lam / s


def traverse_path(graph: GraphState, lam_start: np.ndarray, lam_end: np.ndarray,
                  K: int = 11, label: str = "path") -> dict:
    """Sample u*(λ_t) at K points along λ_t = (1-t) λ_start + t λ_end."""
    print(f"\n  Path {label}:  λ_start={lam_start}  →  λ_end={lam_end}", flush=True)
    print(f"  {'t':>5}  {'energy':>10}  {'bind':>6}  {'inside':>6} "
          f"{'n_high':>7} {'n_core':>7} {'n_lo':>5} {'n_hi':>5}", flush=True)
    print(f"  {'-' * 70}", flush=True)
    samples = []
    u_prev = None
    for k in range(K):
        t = k / (K - 1)
        lam_t = project_simplex((1 - t) * lam_start + t * lam_end)
        ev = evaluate_lambda(graph, lam_t)
        ev["t"] = float(t)
        ev["k"] = int(k)
        if not ev["ok"]:
            print(f"  {t:>5.3f}  FAILED: {ev.get('error')}", flush=True)
            samples.append(ev)
            u_prev = None
            continue

        u_now = np.array(ev["u"])
        if u_prev is not None:
            ev["delta_u_l2"]   = float(np.linalg.norm(u_now - u_prev))
            ev["delta_u_linf"] = float(np.max(np.abs(u_now - u_prev)))
        else:
            ev["delta_u_l2"] = None
            ev["delta_u_linf"] = None

        # Active-set changes
        if k > 0 and samples[-1].get("ok"):
            prev = samples[-1]
            ev["delta_n_high"] = ev["n_high"] - prev["n_high"]
            ev["delta_n_core"] = ev["n_core"] - prev["n_core"]
            ev["delta_n_lo"]   = ev["n_active_lo"] - prev["n_active_lo"]
            ev["delta_n_hi"]   = ev["n_active_hi"] - prev["n_active_hi"]
            ev["delta_inside"] = ev["inside"] - prev["inside"]
        else:
            ev["delta_n_high"] = ev["delta_n_core"] = 0
            ev["delta_n_lo"] = ev["delta_n_hi"] = 0
            ev["delta_inside"] = 0.0

        samples.append(ev)
        u_prev = u_now
        print(f"  {t:>5.3f}  {ev['energy']:>10.4f}  {ev['bind']:>6.3f} "
              f"{ev['inside']:>6.3f}  {ev['n_high']:>7}  {ev['n_core']:>7} "
              f"{ev['n_active_lo']:>5} {ev['n_active_hi']:>5}", flush=True)

    # Detect events
    branch_jumps = []
    active_set_changes = []
    big_field_jumps = []
    for k in range(1, K):
        s = samples[k]
        if not s.get("ok") or samples[k-1].get("ok") is False:
            continue
        if s.get("delta_n_core", 0) != 0 or s.get("delta_n_high", 0) != 0:
            branch_jumps.append({"k": k, "t": s["t"],
                                  "delta_n_core": s["delta_n_core"],
                                  "delta_n_high": s["delta_n_high"]})
        if s.get("delta_n_lo", 0) != 0 or s.get("delta_n_hi", 0) != 0:
            active_set_changes.append({"k": k, "t": s["t"],
                                        "delta_n_lo": s["delta_n_lo"],
                                        "delta_n_hi": s["delta_n_hi"]})
        if s.get("delta_u_linf") and s["delta_u_linf"] > 0.3:
            big_field_jumps.append({"k": k, "t": s["t"],
                                     "delta_u_linf": s["delta_u_linf"],
                                     "delta_u_l2": s["delta_u_l2"]})

    # Smoothness summary
    valid = [s for s in samples if s.get("ok") and s.get("delta_u_l2") is not None]
    if valid:
        avg_du_l2 = float(np.mean([s["delta_u_l2"] for s in valid]))
        max_du_l2 = float(np.max([s["delta_u_l2"] for s in valid]))
        avg_du_linf = float(np.mean([s["delta_u_linf"] for s in valid]))
        max_du_linf = float(np.max([s["delta_u_linf"] for s in valid]))
    else:
        avg_du_l2 = max_du_l2 = avg_du_linf = max_du_linf = 0.0

    if branch_jumps:
        verdict = "branch-switch detected"
    elif big_field_jumps:
        verdict = "field jump (possible kink)"
    elif active_set_changes:
        verdict = "active-set change (R2 boundary)"
    else:
        verdict = "smooth branch (R1)"

    return {
        "label": label,
        "lam_start": lam_start.tolist(),
        "lam_end":   lam_end.tolist(),
        "n_samples": K,
        "samples":   samples,
        "branch_jumps":         branch_jumps,
        "active_set_changes":   active_set_changes,
        "big_field_jumps":      big_field_jumps,
        "avg_delta_u_l2":   avg_du_l2,
        "max_delta_u_l2":   max_du_l2,
        "avg_delta_u_linf": avg_du_linf,
        "max_delta_u_linf": max_du_linf,
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Path definitions
# ---------------------------------------------------------------------------

PATHS = [
    ("cl_axis",
     np.array([0.25, 0.25, 0.25, 0.25]),
     np.array([0.70, 0.10, 0.10, 0.10])),
    ("sep_axis",
     np.array([0.25, 0.25, 0.25, 0.25]),
     np.array([0.10, 0.70, 0.10, 0.10])),
    ("bd_axis",
     np.array([0.25, 0.25, 0.25, 0.25]),
     np.array([0.10, 0.10, 0.70, 0.10])),
    ("CE1_pair",
     np.array([0.60, 0.20, 0.20, 0.00]),
     np.array([0.50, 0.30, 0.20, 0.00])),
    ("random",
     np.array([0.30, 0.40, 0.20, 0.10]),
     np.array([0.55, 0.10, 0.25, 0.10])),
]


def main():
    t0 = time.time()
    print("=== VP-6 Path Test: u*(λ) regularity along simplex paths ===", flush=True)
    print(f"K = 11 samples per path; 5 paths; 2 scenes", flush=True)

    scenes = {
        "S3_grid6x6":     make_scene_S3(),
        "S4_two_cliques": make_scene_S4(),
    }

    all_results = {}
    for scene_name, graph in scenes.items():
        print(f"\n--- Scene: {scene_name} (n={graph.n}) ---", flush=True)
        scene_paths = {}
        for label, lam_s, lam_e in PATHS:
            path_res = traverse_path(graph, lam_s, lam_e, K=11, label=label)
            scene_paths[label] = path_res
            print(f"  → verdict: {path_res['verdict']}  (max ||Δu||_∞ = "
                  f"{path_res['max_delta_u_linf']:.3f})", flush=True)
        all_results[scene_name] = scene_paths

    elapsed = time.time() - t0
    print(f"\n=== VP-6 Path Test Summary ===", flush=True)
    for scene_name, paths in all_results.items():
        print(f"  {scene_name}:", flush=True)
        for label, p in paths.items():
            print(f"    {label:<12}  {p['verdict']}  branch_jumps="
                  f"{len(p['branch_jumps'])}  AS_changes="
                  f"{len(p['active_set_changes'])}", flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)

    output = {
        "experiment": "VP-6 Path Test (u*(λ) regularity)",
        "date": "2026-05-08",
        "paths": [(p[0], p[1].tolist(), p[2].tolist()) for p in PATHS],
        "K_per_path": 11,
        "thresholds": {
            "active_lo": ACTIVE_LO, "active_hi": ACTIVE_HI,
            "big_field_jump_linf": 0.3,
        },
        "per_scene": all_results,
        "elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-018", "Prop R1", "Prop R3 (3)", "OP-OMS-026"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp6_u_star_path_results.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    md = ["# VP-6 Path Test — u*(λ) Regularity Summary",
          "",
          f"**Date:** 2026-05-08  ",
          f"**Experiment:** vp6_u_star_regular_path_test.py  ",
          f"**Paths:** 5 line segments × 2 scenes × 11 samples each  ",
          f"**Elapsed:** {elapsed:.1f}s",
          "",
          "## Per-scene path verdicts",
          ""]

    for scene_name, paths in all_results.items():
        md.append(f"### {scene_name}")
        md.append("")
        md.append("| path | verdict | branch_jumps | AS_changes | "
                  "max ||Δu||_∞ | max ||Δu||_2 |")
        md.append("|---|---|---|---|---|---|")
        for label, p in paths.items():
            md.append(f"| {label} | {p['verdict']} | "
                      f"{len(p['branch_jumps'])} | "
                      f"{len(p['active_set_changes'])} | "
                      f"{p['max_delta_u_linf']:.3f} | "
                      f"{p['max_delta_u_l2']:.3f} |")
        md.append("")

    md += ["## Interpretation",
           "",
           "Following `op_oms_018_regular_u_star.md`:",
           "",
           "- 'smooth branch (R1)' = no branch jump, no active-set change, "
           "no field jump → consistent with Theorem R1 (interior IFT branch).",
           "- 'active-set change (R2 boundary)' = #{u_i ~= 0} or #{u_i ~= 1} "
           "changes along the path, but no branch jump → consistent with "
           "Theorem R2 piecewise C^1 across an active-set boundary.",
           "- 'field jump (possible kink)' = ||Δu||_∞ > 0.3 between adjacent "
           "samples without a branch-id flip → suggestive of a non-smooth "
           "kink within a single branch.",
           "- 'branch-switch detected' = K_core or n_high jumps → R3 (3) "
           "obstruction; the u*-correspondence is multi-valued at some "
           "λ_c on this path. Locates Σ_branch (OP-OMS-026).",
           "",
           "## OP-OMS-018 status update",
           "",
           "Combine path-test results with the proofs in "
           "`op_oms_018_regular_u_star.md`:",
           "",
           "- Theorem R1 / R2 are PROVED (theory).",
           "- Path test demonstrates which paths in Δ³ realize each regime "
           "computationally, distinguishing R1, R2, kink, and branch-switch.",
           "- Branch switches in the path test = empirical realization of "
           "Σ_branch (OP-OMS-026).",
           ""]

    md_path = os.path.join(RESULTS_DIR, "vp6_u_star_path_summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
