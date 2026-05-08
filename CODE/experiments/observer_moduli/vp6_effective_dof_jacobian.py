"""VP-6: Effective DOF via Jacobian singular spectrum.

Attacks OP-OMS-016 (computational d_eff) and OP-OMS-005 (effective DOF) by
computing finite-difference Jacobians of the readout map P_top:Δ→R^p along
the simplex tangent and reporting the singular spectrum.

Two variants are run:

  (a) Static face Δ²_static = {λ_cl + λ_sep + λ_bd = 1, λ_tr = 0}
      Tangent dim = 2; readout R_vec ∈ R^7  (Persist excluded — degenerate=1
      on static scenes by Prop CW2; the dimension we want is intrinsic to
      the static observer face).
  (b) Full simplex Δ³  (4 weights)
      Tangent dim = 3; readout R_vec ∈ R^8 (Persist included).

Smooth components of P_top used for the Jacobian (CV-aware: discrete
quantities K_core and n_high are recorded but excluded from the SVD):

  R_vec(λ) = (Bind, Sep, Inside, [Persist if 4D],
              l_max, l_second, articulation_gap, c_max)

Sample points (per scene):

  P1..P6 from VP-4 (cl/sep/balanced/cl_sep/bd/tr-dominant) — projected onto
  the relevant simplex (P6 dropped from static face).
  CE-1 pair from VP-1 (λ_A and λ_B).
  Several barycenter-perturbed random points.

Outputs:
  CODE/experiments/results/observer_moduli/vp6_jacobian_spectra.json
  CODE/experiments/results/observer_moduli/vp6_effective_dof_summary.md

CLI args: none. Adjust SCENES list and SAMPLES dict at the top.
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

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(
    os.path.dirname(EXP_DIR), "results", "observer_moduli"
)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Scenes (reused from VP-3 / VP-4)
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Tangent bases on the simplex
# ---------------------------------------------------------------------------

# Orthonormal basis of {v ∈ R^3 : sum v = 0}
TANGENT_3 = np.array([
    [1.0, -1.0, 0.0],
    [1.0,  1.0, -2.0],
])
TANGENT_3 = TANGENT_3 / np.linalg.norm(TANGENT_3, axis=1, keepdims=True)

# Orthonormal basis of {v ∈ R^4 : sum v = 0}
TANGENT_4 = np.array([
    [1.0, -1.0,  0.0,  0.0],
    [1.0,  1.0, -2.0,  0.0],
    [1.0,  1.0,  1.0, -3.0],
])
TANGENT_4 = TANGENT_4 / np.linalg.norm(TANGENT_4, axis=1, keepdims=True)


def project_to_simplex(lam: np.ndarray) -> np.ndarray:
    """Clip to non-negative and renormalize. Used to keep finite-difference
    perturbations in Δ even if a step pushes a coordinate just below zero."""
    lam = np.clip(lam, 0.0, None)
    s = lam.sum()
    if s <= 1e-12:
        return np.full_like(lam, 1.0 / len(lam))
    return lam / s


# ---------------------------------------------------------------------------
# R_vec readout (smooth components only; discrete quantities returned as branch_id)
# ---------------------------------------------------------------------------

THETA_CORE = 0.9


def evaluate_lambda(graph: GraphState, lam: np.ndarray,
                    volume_fraction: float = 0.3) -> dict:
    """Run the SCC optimizer at λ and return the smooth readout R_vec plus
    branch identifiers."""
    params = ParameterRegistry()
    if len(lam) == 3:
        params.w_cl  = float(lam[0])
        params.w_sep = float(lam[1])
        params.w_bd  = float(lam[2])
        params.w_tr  = 0.0
    elif len(lam) == 4:
        params.w_cl  = float(lam[0])
        params.w_sep = float(lam[1])
        params.w_bd  = float(lam[2])
        params.w_tr  = float(lam[3])
    else:
        raise ValueError(f"len(lam)={len(lam)} invalid (expected 3 or 4)")
    params.volume_fraction = volume_fraction

    try:
        result = find_formation(graph, params)
    except Exception as exc:
        return {"ok": False, "error": str(exc)}

    u = result.u
    d = diagnostic_vector(u, graph, params)
    l_max, l_second = _persistence_h0_graph(u, graph)
    artic_gap = float(l_max - l_second)
    c_max = float(u.max())

    # Branch identifiers (excluded from R_vec but used to flag jumps)
    n_high = int(np.sum(u > 0.5))
    n_core = int(np.sum(u >= THETA_CORE))

    if len(lam) == 3:
        R_vec = np.array([d.bind, d.sep, d.inside,
                          float(l_max), float(l_second), artic_gap, c_max])
    else:
        R_vec = np.array([d.bind, d.sep, d.inside, d.persist,
                          float(l_max), float(l_second), artic_gap, c_max])

    return {
        "ok": True,
        "lam": lam.tolist(),
        "R_vec": R_vec.tolist(),
        "bind": float(d.bind),
        "sep":  float(d.sep),
        "inside": float(d.inside),
        "persist": float(d.persist),
        "l_max": float(l_max),
        "l_second": float(l_second),
        "artic_gap": artic_gap,
        "c_max": c_max,
        "energy": float(result.energy),
        "n_high": n_high,
        "n_core": n_core,
        "branch_id": (n_core, n_high),
    }


# ---------------------------------------------------------------------------
# Finite-difference Jacobian on the simplex tangent
# ---------------------------------------------------------------------------

def compute_jacobian(graph: GraphState, lam: np.ndarray, h: float,
                     volume_fraction: float = 0.3) -> dict:
    """Centered finite-difference Jacobian of R_vec along the orthonormal
    tangent basis of the simplex containing λ.

    For len(lam)==3: tangent dim = 2 (static face).
    For len(lam)==4: tangent dim = 3 (full Δ³).
    """
    if len(lam) == 3:
        T = TANGENT_3
    elif len(lam) == 4:
        T = TANGENT_4
    else:
        raise ValueError("len(lam) must be 3 or 4")

    base = evaluate_lambda(graph, lam, volume_fraction)
    if not base["ok"]:
        return {"ok": False, "error": base.get("error", "base failed"),
                "lam": lam.tolist()}

    R0 = np.array(base["R_vec"])
    branch0 = base["branch_id"]
    p = R0.size  # readout dimension
    k = T.shape[0]  # tangent dim

    J = np.zeros((p, k))
    branch_jumps = []
    fd_pairs = []

    for j in range(k):
        v = T[j]
        lam_plus = project_to_simplex(lam + h * v)
        lam_minus = project_to_simplex(lam - h * v)

        ev_plus = evaluate_lambda(graph, lam_plus, volume_fraction)
        ev_minus = evaluate_lambda(graph, lam_minus, volume_fraction)
        if not ev_plus["ok"] or not ev_minus["ok"]:
            return {"ok": False,
                    "error": "perturbation eval failed",
                    "lam": lam.tolist()}

        R_plus = np.array(ev_plus["R_vec"])
        R_minus = np.array(ev_minus["R_vec"])

        # Branch consistency check
        same_branch = (ev_plus["branch_id"] == branch0
                       and ev_minus["branch_id"] == branch0)
        if not same_branch:
            branch_jumps.append({
                "tangent_j": j,
                "branch0": list(branch0),
                "branch_plus": list(ev_plus["branch_id"]),
                "branch_minus": list(ev_minus["branch_id"]),
            })

        J[:, j] = (R_plus - R_minus) / (2.0 * h)
        fd_pairs.append({
            "j": j,
            "tangent": v.tolist(),
            "lam_plus": lam_plus.tolist(),
            "lam_minus": lam_minus.tolist(),
            "R_plus": R_plus.tolist(),
            "R_minus": R_minus.tolist(),
            "same_branch": bool(same_branch),
        })

    return {
        "ok": True,
        "lam": lam.tolist(),
        "h": h,
        "tangent_basis": T.tolist(),
        "R0": R0.tolist(),
        "J": J.tolist(),
        "branch_id": list(branch0),
        "branch_jumps": branch_jumps,
        "fd_pairs": fd_pairs,
        "base_eval": {k: v for k, v in base.items()
                      if k != "R_vec"},
    }


def svd_summary(J: np.ndarray) -> dict:
    """SVD of J and effective-dimension classification."""
    U, S, Vt = np.linalg.svd(J, full_matrices=False)
    sigma = np.array(S, dtype=float)
    s1 = float(sigma[0]) if sigma.size > 0 else 0.0

    abs_thresholds = [1e-3, 1e-2, 5e-2, 1e-1]
    rel_thresholds = [1e-3, 1e-2, 5e-2, 1e-1]

    d_eff_abs = {f"abs_{t:.0e}": int(np.sum(sigma >= t))
                 for t in abs_thresholds}
    d_eff_rel = {}
    if s1 > 0:
        for t in rel_thresholds:
            d_eff_rel[f"rel_{t:.0e}"] = int(np.sum(sigma / s1 >= t))
    else:
        for t in rel_thresholds:
            d_eff_rel[f"rel_{t:.0e}"] = 0

    # Right singular vectors (tangent directions ranked by sensitivity)
    V_dominant = Vt.tolist()

    return {
        "sigma": sigma.tolist(),
        "sigma_max": s1,
        "sigma_min": float(sigma[-1]) if sigma.size > 0 else 0.0,
        "d_eff_abs": d_eff_abs,
        "d_eff_rel": d_eff_rel,
        "U": U.tolist(),
        "Vt": Vt.tolist(),
        "tangent_directions_ranked": V_dominant,
    }


# ---------------------------------------------------------------------------
# Sample points
# ---------------------------------------------------------------------------

# Static face samples (λ_cl, λ_sep, λ_bd) — λ_tr = 0
SAMPLES_STATIC = {
    "P1_cl_dominant":  np.array([0.70, 0.15, 0.15]),
    "P2_sep_dominant": np.array([0.15, 0.70, 0.15]),
    "P3_balanced":     np.array([1/3, 1/3, 1/3]),
    "P4_cl_sep":       np.array([0.45, 0.45, 0.10]),
    "P5_bd_dominant":  np.array([0.15, 0.15, 0.70]),
    "CE1_lambda_A":    np.array([0.60, 0.20, 0.20]),
    "CE1_lambda_B":    np.array([0.50, 0.30, 0.20]),
    # Random interior points (rng-fixed)
    "R1_random":       np.array([0.50, 0.30, 0.20]),  # near CE1_B
    "R2_random":       np.array([0.20, 0.50, 0.30]),
    "R3_random":       np.array([0.30, 0.20, 0.50]),
    # Near the approximate-symmetry locus {λ_cl = λ_sep} (OP-OMS-017)
    "S_cl_eq_sep":     np.array([0.40, 0.40, 0.20]),
    "S_bd_face_near":  np.array([0.10, 0.10, 0.80]),
}

SAMPLES_FULL = {
    "P1_cl_dominant":  np.array([0.70, 0.10, 0.10, 0.10]),
    "P2_sep_dominant": np.array([0.10, 0.70, 0.10, 0.10]),
    "P3_balanced":     np.array([0.25, 0.25, 0.25, 0.25]),
    "P4_cl_sep":       np.array([0.40, 0.40, 0.10, 0.10]),
    "P5_bd_dominant":  np.array([0.10, 0.10, 0.70, 0.10]),
    "P6_tr_dominant":  np.array([0.10, 0.10, 0.10, 0.70]),
    "CE1_lambda_A":    np.array([0.55, 0.15, 0.15, 0.15]),  # CE1 lifted
    "CE1_lambda_B":    np.array([0.45, 0.25, 0.15, 0.15]),
    "S_cl_eq_sep":     np.array([0.35, 0.35, 0.15, 0.15]),
}


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def run_variant(graph: GraphState, scene_name: str, samples: dict,
                variant: str, h: float = 1e-3,
                volume_fraction: float = 0.3) -> dict:
    print(f"\n  ── Scene {scene_name}, variant {variant} (h={h}, "
          f"k_tangent={2 if variant=='static' else 3}) ──", flush=True)

    rows = []
    for label, lam in samples.items():
        t0 = time.time()
        # Project onto simplex (defensive)
        lam_normed = project_to_simplex(lam)
        jac = compute_jacobian(graph, lam_normed, h, volume_fraction)
        elapsed = time.time() - t0

        if not jac["ok"]:
            print(f"  {label:<22}  FAILED: {jac.get('error')}", flush=True)
            rows.append({"label": label, "ok": False,
                         "error": jac.get("error"),
                         "lam": lam_normed.tolist()})
            continue

        J = np.array(jac["J"])
        svd = svd_summary(J)
        s = svd["sigma"]

        clean = (len(jac["branch_jumps"]) == 0)
        flag = "" if clean else "  [BRANCH-JUMP]"
        sigma_str = ", ".join(f"{si:.4f}" for si in s)
        print(f"  {label:<22}  branch={tuple(jac['branch_id'])}  "
              f"σ=[{sigma_str}]  d_eff(rel,5e-2)="
              f"{svd['d_eff_rel']['rel_5e-02']}{flag}  [{elapsed:.1f}s]",
              flush=True)

        rows.append({
            "label": label,
            "ok": True,
            "variant": variant,
            "lam": lam_normed.tolist(),
            "branch_id": jac["branch_id"],
            "branch_jumps": jac["branch_jumps"],
            "branch_clean": clean,
            "R0": jac["R0"],
            "J_shape": list(J.shape),
            "J": jac["J"],
            "sigma": svd["sigma"],
            "d_eff_abs": svd["d_eff_abs"],
            "d_eff_rel": svd["d_eff_rel"],
            "tangent_directions_ranked": svd["tangent_directions_ranked"],
            "energy": jac["base_eval"].get("energy"),
            "diagnostics": {
                "bind":   jac["base_eval"].get("bind"),
                "sep":    jac["base_eval"].get("sep"),
                "inside": jac["base_eval"].get("inside"),
                "persist": jac["base_eval"].get("persist"),
            },
            "elapsed_s": elapsed,
        })

    return {"scene": scene_name, "variant": variant, "h": h,
            "n_samples": len(samples), "rows": rows}


def aggregate_d_eff(per_scene_results: dict, key: str = "rel_5e-02") -> dict:
    counts = {}
    sigma_max = []
    sigma_min = []
    sigma_ratio = []
    n_clean = 0
    n_total = 0
    src_field = "d_eff_rel" if key.startswith("rel_") else "d_eff_abs"
    for sn, sr in per_scene_results.items():
        for v_name, v_res in sr.items():
            for row in v_res["rows"]:
                if not row.get("ok"):
                    continue
                n_total += 1
                if row["branch_clean"]:
                    n_clean += 1
                d_eff = row[src_field][key]
                counts.setdefault(v_name, {}).setdefault(d_eff, 0)
                counts[v_name][d_eff] += 1
                sig = np.array(row["sigma"])
                if sig.size > 0:
                    sigma_max.append(float(sig[0]))
                    sigma_min.append(float(sig[-1]))
                    if sig[0] > 0 and sig.size > 1:
                        sigma_ratio.append(float(sig[-1] / sig[0]))
    return {
        "criterion": f"d_eff with {key} threshold",
        "histogram": counts,
        "sigma_max_avg": float(np.mean(sigma_max)) if sigma_max else None,
        "sigma_max_min": float(np.min(sigma_max)) if sigma_max else None,
        "sigma_max_max": float(np.max(sigma_max)) if sigma_max else None,
        "sigma_min_avg": float(np.mean(sigma_min)) if sigma_min else None,
        "sigma_ratio_min_avg": float(np.mean(sigma_ratio)) if sigma_ratio else None,
        "n_clean": n_clean,
        "n_total": n_total,
    }


def main():
    t0 = time.time()
    print("=== VP-6: Effective DOF via Jacobian Singular Spectrum ===", flush=True)

    scenes = {
        "S3_grid6x6":     make_scene_S3(),
        "S4_two_cliques": make_scene_S4(),
    }

    per_scene = {}
    for scene_name, graph in scenes.items():
        per_scene[scene_name] = {
            "static": run_variant(graph, scene_name, SAMPLES_STATIC,
                                  variant="static", h=1e-3),
            "full":   run_variant(graph, scene_name, SAMPLES_FULL,
                                  variant="full", h=1e-3),
        }

    elapsed = time.time() - t0

    summary_rel = aggregate_d_eff(per_scene, key="rel_5e-02")
    summary_abs = aggregate_d_eff(per_scene, key="abs_5e-02")

    print(f"\n=== VP-6 SUMMARY ===", flush=True)
    print(f"  Total samples evaluated: {summary_rel['n_total']}  "
          f"(branch-clean: {summary_rel['n_clean']})", flush=True)
    print(f"  σ_max average: {summary_rel['sigma_max_avg']:.4f}", flush=True)
    print(f"  σ_min/σ_max average ratio: "
          f"{summary_rel['sigma_ratio_min_avg']:.4f}", flush=True)
    print(f"  d_eff(rel, 5e-2) histogram:", flush=True)
    for v_name, hist in summary_rel["histogram"].items():
        print(f"    {v_name}: {hist}", flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)

    output = {
        "experiment": "VP-6 Effective DOF via Jacobian Singular Spectrum",
        "date": "2026-05-08",
        "fd_step_h": 1e-3,
        "thresholds_abs": [1e-3, 1e-2, 5e-2, 1e-1],
        "thresholds_rel": [1e-3, 1e-2, 5e-2, 1e-1],
        "tangent_basis_3": TANGENT_3.tolist(),
        "tangent_basis_4": TANGENT_4.tolist(),
        "samples_static": {k: v.tolist() for k, v in SAMPLES_STATIC.items()},
        "samples_full":   {k: v.tolist() for k, v in SAMPLES_FULL.items()},
        "per_scene": per_scene,
        "aggregate_d_eff_rel_5e-2": summary_rel,
        "aggregate_d_eff_abs_5e-2": summary_abs,
        "elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-016", "OP-OMS-005", "Hyp RG1"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp6_jacobian_spectra.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    # Markdown summary
    md = ["# VP-6 Effective DOF Summary", "",
          "**Date:** 2026-05-08  ",
          "**Experiment:** vp6_effective_dof_jacobian.py  ",
          "**Attacks:** OP-OMS-016 (computational d_eff), OP-OMS-005 "
          "(effective DOF), Hypothesis RG1 (d_eff^typical(0.05) ∈ [2,4])  ",
          f"**Elapsed:** {elapsed:.1f}s",
          "",
          "## Method", "",
          "Centered finite-difference Jacobian of the smooth components of "
          "P_top, sampled along the orthonormal tangent basis of the simplex.",
          "",
          "Static face: 7-dim readout × 2-dim tangent → J ∈ R^{7×2}.",
          "Full simplex: 8-dim readout × 3-dim tangent → J ∈ R^{8×3}.",
          "",
          "## Per-scene singular spectra", ""]

    for scene_name, sr in per_scene.items():
        md.append(f"### Scene: {scene_name}")
        md.append("")
        for v_name, v_res in sr.items():
            md.append(f"**Variant:** `{v_name}`  (k_tangent="
                      f"{2 if v_name=='static' else 3})")
            md.append("")
            md.append("| label | branch | σ values | d_eff(rel,5e-2) | "
                      "branch_clean |")
            md.append("|---|---|---|---|---|")
            for row in v_res["rows"]:
                if not row.get("ok"):
                    md.append(f"| {row['label']} | — | FAILED | — | — |")
                    continue
                sigma_str = ", ".join(f"{x:.4f}" for x in row["sigma"])
                md.append(
                    f"| {row['label']} | {tuple(row['branch_id'])} | "
                    f"[{sigma_str}] | {row['d_eff_rel']['rel_5e-02']} | "
                    f"{'YES' if row['branch_clean'] else 'NO'} |")
            md.append("")

    md.append("## Aggregate d_eff(rel, 5e-2) histograms")
    md.append("")
    for v_name, hist in summary_rel["histogram"].items():
        md.append(f"- **{v_name}**: {dict(sorted(hist.items()))}")
    md.append("")
    md.append("## Sigma statistics")
    md.append("")
    md.append(f"- σ_max average: {summary_rel['sigma_max_avg']:.4f}")
    md.append(f"- σ_max range: [{summary_rel['sigma_max_min']:.4f}, "
              f"{summary_rel['sigma_max_max']:.4f}]")
    md.append(f"- σ_min/σ_max average ratio: "
              f"{summary_rel['sigma_ratio_min_avg']:.4f}")
    md.append("")
    md.append("## Branch-cleanness")
    md.append("")
    md.append(f"- Samples without branch jumps in any FD pair: "
              f"{summary_rel['n_clean']} / {summary_rel['n_total']}")
    md.append("")
    md.append("Branch-jumping samples cross a u*(λ) regularity boundary "
              "within the FD stencil. Their Jacobian is contaminated by a "
              "discrete component switch and over-states σ on the affected "
              "tangent direction. They corroborate OP-OMS-018 — global C^1 "
              "regularity of u*(λ) fails on these stencils.")

    md_path = os.path.join(RESULTS_DIR, "vp6_effective_dof_summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
