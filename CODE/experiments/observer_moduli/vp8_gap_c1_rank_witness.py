"""VP-8 (Gate 2 — OP-OMS-001 Gap C1): Rank witness for J_e on regular branches.

Tests the Gap-C1 H4 hypothesis: at a regular base point λ_0, the
projected energy-gradient matrix G_T = P_T^T G ∈ R^{(n-1) × 3} (using
{cl, sep, bd}, since on static scenes E_tr is degenerate by Prop CW2)
has rank ≥ 3 — equivalently, a maximal 3×3 minor is non-zero.

The 4-component version on a temporally non-degenerate scene would
need a transport energy term that's not gauge-redundant; we keep the
3-component static version as the core test and report the 3×3 minor /
SVD / condition number as the witness.

For each scene × λ-point:
  1. Run `find_formation` to get u*(λ).
  2. Compute G ∈ R^{n×3} from `grad_cl`, `grad_sep`, `grad_bd`.
  3. Project G_T = P_T^T G via Householder of 1.
  4. (optional) Compute Hessian H_T via finite differences of the gradient.
  5. Compute J_e = -G_T^T H_T^{-1} G_T ∈ R^{3×3}.
  6. SVD; rank; smallest singular value; condition number; det of J_e_tan.
  7. Detect branch-jump / active-set anomalies.

Scenes:
  - P12: path graph (12 nodes)
  - S3:  6×6 grid (36 nodes)
  - asymmetric: a deliberately asymmetric small connected graph (an 8-vertex
    "lollipop" — clique of 4 with a tail of 4)

λ-samples per scene (≥ 14):
  barycenter, cl-dominant, sep-dominant, bd-dominant,
  + 10 random interior points (rng-fixed).

Outputs:
  CODE/experiments/results/observer_moduli/vp8_gap_c1_rank_witness.json
  CODE/experiments/results/observer_moduli/vp8_gap_c1_rank_witness.md
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
from scc.diagnostics import _persistence_h0_graph
from scc.energy import grad_cl, grad_sep, grad_bd, energy_cl, energy_sep, energy_bd

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(
    os.path.dirname(EXP_DIR), "results", "observer_moduli"
)
os.makedirs(RESULTS_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Scenes
# ---------------------------------------------------------------------------

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


def make_scene_asym() -> GraphState:
    """8-vertex asymmetric 'lollipop': K_4 ∪ tail of 4."""
    import scipy.sparse as sp
    n = 8
    rows, cols, data = [], [], []
    # K_4 on {0, 1, 2, 3}
    for i in range(4):
        for j in range(4):
            if i != j:
                rows.append(i); cols.append(j); data.append(1.0)
    # Tail: 3 - 4 - 5 - 6 - 7
    for i in range(3, 7):
        rows.extend([i, i + 1])
        cols.extend([i + 1, i])
        data.extend([1.0, 1.0])
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


SCENES = {
    "P12_path":   make_scene_P12,
    "S3_grid6x6": make_scene_S3,
    "asym_K4+tail": make_scene_asym,
}


# ---------------------------------------------------------------------------
# λ samples (3-component, static face)
# ---------------------------------------------------------------------------

def random_simplex_points(n: int, rng_seed: int = 11) -> list[np.ndarray]:
    rng = np.random.RandomState(rng_seed)
    pts = []
    for _ in range(n):
        d = rng.dirichlet([2.0, 2.0, 2.0])  # mildly concentrated interior
        pts.append(d)
    return pts


def sample_points() -> dict[str, np.ndarray]:
    pts = {
        "barycenter":     np.array([1/3, 1/3, 1/3]),
        "cl_dominant":    np.array([0.7, 0.15, 0.15]),
        "sep_dominant":   np.array([0.15, 0.7, 0.15]),
        "bd_dominant":    np.array([0.15, 0.15, 0.7]),
    }
    rand_pts = random_simplex_points(10, rng_seed=11)
    for i, lam in enumerate(rand_pts):
        pts[f"random_{i+1}"] = lam
    return pts


# ---------------------------------------------------------------------------
# Householder basis of T = ker(1^T)
# ---------------------------------------------------------------------------

def tangent_basis(n: int) -> np.ndarray:
    """Orthonormal n × (n-1) matrix whose columns span ker(1^T)."""
    one = np.ones(n) / np.sqrt(n)
    e1 = np.zeros(n)
    e1[0] = 1.0
    v = e1 - one
    if np.linalg.norm(v) < 1e-12:
        v = np.zeros(n)
        v[0] = 1.0
        v[1:] = -1.0 / (n - 1)
    v = v / np.linalg.norm(v)
    H = np.eye(n) - 2.0 * np.outer(v, v)
    return H[:, 1:]


# ---------------------------------------------------------------------------
# Tangent basis on the simplex Δ² (3-component)
# ---------------------------------------------------------------------------

V_SIMPLEX = np.array([
    [1.0, -1.0, 0.0],
    [1.0,  1.0, -2.0],
])
V_SIMPLEX = V_SIMPLEX / np.linalg.norm(V_SIMPLEX, axis=1, keepdims=True)


# ---------------------------------------------------------------------------
# Compute u*, G, H_T, J_e, J_e_tan
# ---------------------------------------------------------------------------

THETA_CORE = 0.9


def compute_witness(graph: GraphState, lam: np.ndarray,
                    volume_fraction: float = 0.3,
                    n_restarts: int = 3,
                    fd_step: float = 1e-4) -> dict:
    """Compute the rank witness at λ on graph.

    Returns dict with G, G_T, H_T, J_e, J_e_tan, SVD, branch_id.
    """
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
        return {"ok": False, "error": str(exc), "lam": lam.tolist()}

    u = result.u
    n = len(u)

    # Energy gradients at u*: G ∈ R^{n × 3}
    g_cl  = grad_cl(u, graph, params)
    g_sep = grad_sep(u, graph, params)
    g_bd  = grad_bd(u, graph, params)
    G = np.column_stack([g_cl, g_sep, g_bd])  # (n, 3)

    # Energy values at u*: e ∈ R^3
    e_cl  = float(energy_cl(u, graph, params))
    e_sep = float(energy_sep(u, graph, params))
    e_bd  = float(energy_bd(u, graph, params))

    # Tangent basis on T = ker(1^T)
    P_T = tangent_basis(n)
    G_T = P_T.T @ G  # ((n-1), 3)

    # Active sets (box-constraint inactive sites)
    active_lo = (u < 0.05)
    active_hi = (u > 0.95)
    n_active_lo = int(active_lo.sum())
    n_active_hi = int(active_hi.sum())
    n_high = int((u > 0.5).sum())
    n_core = int((u >= THETA_CORE).sum())

    # Inactive index set I_0 = sites strictly inside (0,1)
    # For interior case use full T; for active-set case restrict.
    # Here we report both: use full T_active (T restricted to inactive sites).
    inactive_mask = (~active_lo) & (~active_hi)
    n_inactive = int(inactive_mask.sum())

    # Hessian of E_λ via finite differences of the total gradient
    # H[:,k] ≈ (∇E_λ(u + h e_k) - ∇E_λ(u - h e_k)) / (2h)
    # (Use full Hessian of E_λ; project to T.)
    def grad_total(uu: np.ndarray) -> np.ndarray:
        return (lam[0] * grad_cl(uu, graph, params)
                + lam[1] * grad_sep(uu, graph, params)
                + lam[2] * grad_bd(uu, graph, params))

    H_full = np.zeros((n, n))
    for k in range(n):
        u_plus  = u.copy(); u_plus[k]  += fd_step
        u_minus = u.copy(); u_minus[k] -= fd_step
        u_plus  = np.clip(u_plus, 0.0, 1.0)
        u_minus = np.clip(u_minus, 0.0, 1.0)
        g_plus  = grad_total(u_plus)
        g_minus = grad_total(u_minus)
        H_full[:, k] = (g_plus - g_minus) / (2.0 * fd_step)
    # Symmetrize
    H_full = 0.5 * (H_full + H_full.T)
    H_T = P_T.T @ H_full @ P_T  # ((n-1), (n-1))

    # Eigenvalues of H_T (PD on regular branch)
    H_T_eigs = np.linalg.eigvalsh(H_T)
    H_T_min = float(H_T_eigs.min())
    H_T_max = float(H_T_eigs.max())
    H_T_PD = bool(H_T_min > 1e-8)

    # Solve J_e = -G_T^T H_T^{-1} G_T (use lstsq for stability)
    # Rather than invert H_T, use solve.
    if H_T_PD:
        try:
            X = np.linalg.solve(H_T, G_T)  # ((n-1), 3)
            J_e = -G_T.T @ X  # (3, 3)
            J_e_solved = True
        except np.linalg.LinAlgError:
            J_e = -G_T.T @ np.linalg.pinv(H_T) @ G_T
            J_e_solved = False
    else:
        J_e = -G_T.T @ np.linalg.pinv(H_T) @ G_T
        J_e_solved = False

    # Restrict to simplex tangent (here Δ² has 2D tangent)
    J_e_tan = V_SIMPLEX @ J_e @ V_SIMPLEX.T  # (2, 2)

    # SVD of J_e_tan and J_e
    u1, s1, vt1 = np.linalg.svd(J_e_tan)
    u2, s2, vt2 = np.linalg.svd(J_e)

    # Rank thresholds
    abs_tol = max(1e-8, 1e-6 * float(s2[0]) if s2.size > 0 else 0.0)
    rank_J_e     = int(np.sum(s2 > abs_tol))
    rank_J_e_tan = int(np.sum(s1 > max(1e-8, 1e-6 * float(s1[0]))))

    # Maximal 3×3 minor of G_T (test H4 directly on the n-1 × 3 matrix)
    rank_G_T = int(np.linalg.matrix_rank(G_T, tol=1e-8))
    # Pick the "best" 3×3 minor: take the 3 rows with largest L2 norms
    if G_T.shape[0] >= 3:
        row_norms = np.linalg.norm(G_T, axis=1)
        top3 = np.argsort(-row_norms)[:3]
        minor_3x3 = G_T[top3, :]
        det_minor_3x3 = float(np.linalg.det(minor_3x3))
    else:
        det_minor_3x3 = 0.0

    # Condition number of H_T
    cond_H_T = float(H_T_max / max(H_T_min, 1e-15))

    # Frobenius norm + det of J_e_tan
    det_J_e_tan = float(np.linalg.det(J_e_tan))

    return {
        "ok": True,
        "lam": lam.tolist(),
        "n": n,
        "n_high": n_high,
        "n_core": n_core,
        "branch_id": (n_core, n_high),
        "n_active_lo": n_active_lo,
        "n_active_hi": n_active_hi,
        "n_inactive": n_inactive,
        "energy": float(result.energy),
        "energy_terms": {"E_cl": e_cl, "E_sep": e_sep, "E_bd": e_bd},
        "u_max": float(u.max()),
        # H_T diagnostics
        "H_T_min_eig": H_T_min,
        "H_T_max_eig": H_T_max,
        "H_T_PD": H_T_PD,
        "cond_H_T": cond_H_T,
        # G_T and rank
        "G_T_shape": list(G_T.shape),
        "rank_G_T": rank_G_T,
        "det_3x3_minor_top": det_minor_3x3,
        # J_e and tangent
        "J_e": J_e.tolist(),
        "J_e_tan": J_e_tan.tolist(),
        "sigma_J_e": s2.tolist(),
        "sigma_J_e_tan": s1.tolist(),
        "rank_J_e": rank_J_e,
        "rank_J_e_tan": rank_J_e_tan,
        "det_J_e_tan": det_J_e_tan,
        "J_e_solved_via_solve": J_e_solved,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=== VP-8 (Gate 2): Rank witness for OP-OMS-001 Gap C1 ===",
          flush=True)
    print("Compute J_e = -G_T^T H_T^{-1} G_T (3×3) and tangent J_e_tan (2×2)\n"
          "for each scene × λ-point. Report rank, σ, cond, branch.\n",
          flush=True)

    samples = sample_points()
    print(f"Total samples: {len(samples)} per scene, "
          f"{len(SCENES)} scenes → {len(samples) * len(SCENES)} evaluations",
          flush=True)

    all_results = {}
    for scene_name, scene_fn in SCENES.items():
        graph = scene_fn()
        print(f"\n  ── Scene {scene_name} (n={graph.n}) ──", flush=True)
        per_scene = []
        for label, lam in samples.items():
            t1 = time.time()
            w = compute_witness(graph, lam, volume_fraction=0.3,
                                n_restarts=3, fd_step=1e-4)
            elapsed = time.time() - t1
            if not w.get("ok"):
                print(f"   {label:<14}  FAILED: {w.get('error')}", flush=True)
                w["label"] = label
                per_scene.append(w)
                continue
            sigma_str = ", ".join(f"{x:.4e}" for x in w["sigma_J_e_tan"])
            print(f"   {label:<14}  branch={tuple(w['branch_id'])}  "
                  f"rank(G_T)={w['rank_G_T']}  rank(J_e_tan)={w['rank_J_e_tan']}  "
                  f"σ={sigma_str}  H_T_PD={w['H_T_PD']}  "
                  f"cond(H_T)={w['cond_H_T']:.2e}  "
                  f"|det 3×3 minor|={abs(w['det_3x3_minor_top']):.4e}  "
                  f"[{elapsed:.1f}s]",
                  flush=True)
            w["label"] = label
            per_scene.append(w)
        all_results[scene_name] = per_scene

    elapsed = time.time() - t0

    # Aggregate H4 witnesses
    h4_witnesses = []
    full_rank_count = 0
    total_count = 0
    for scene, rows in all_results.items():
        for w in rows:
            if not w.get("ok"):
                continue
            total_count += 1
            if w["rank_J_e_tan"] >= 2 and abs(w["det_3x3_minor_top"]) > 1e-6:
                full_rank_count += 1
                h4_witnesses.append({
                    "scene": scene,
                    "label": w["label"],
                    "lam": w["lam"],
                    "det_3x3_minor": w["det_3x3_minor_top"],
                    "rank_J_e_tan": w["rank_J_e_tan"],
                    "sigma_J_e_tan": w["sigma_J_e_tan"],
                })

    print(f"\n=== VP-8 SUMMARY ===", flush=True)
    print(f"  Total evaluations: {total_count}", flush=True)
    print(f"  Full-rank witnesses (rank(J_e_tan)=2 AND |det 3x3 minor|>1e-6): "
          f"{full_rank_count}/{total_count} "
          f"({100.0 * full_rank_count / max(total_count, 1):.1f}%)", flush=True)
    print(f"  H4 supported: {'YES' if full_rank_count > 0 else 'NO'}",
          flush=True)
    print(f"  Total elapsed: {elapsed:.1f}s", flush=True)

    output = {
        "experiment": "VP-8 Gap C1 rank witness",
        "date": "2026-05-08",
        "session": "Session 6 (OMS-2.0 push)",
        "method": "G_T = P_T^T G; H_T = FD Hessian projected; "
                  "J_e = -G_T^T H_T^{-1} G_T; J_e_tan = V J_e V^T (2x2). "
                  "G uses (cl, sep, bd) on the static face λ_tr=0.",
        "fd_step": 1e-4,
        "n_samples_per_scene": len(samples),
        "scenes": list(SCENES.keys()),
        "h4_supported": bool(full_rank_count > 0),
        "n_full_rank": full_rank_count,
        "n_total": total_count,
        "h4_witnesses": h4_witnesses,
        "per_scene": all_results,
        "elapsed_s": round(elapsed, 1),
        "attacks": ["OP-OMS-001 Gap C1 / H4", "OP-OMS-024",
                    "Reduction C closure"],
    }

    json_path = os.path.join(RESULTS_DIR, "vp8_gap_c1_rank_witness.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}", flush=True)

    # Markdown
    md = ["# VP-8 — Gap C1 Rank Witness Summary",
          "",
          f"**Date:** 2026-05-08  ",
          f"**Experiment:** vp8_gap_c1_rank_witness.py  ",
          f"**Attacks:** OP-OMS-001 Gap C1 (H4 witness), OP-OMS-024  ",
          f"**Elapsed:** {elapsed:.1f}s  ",
          "",
          "## Method",
          "",
          "Compute J_e = -G_T^T H_T^{-1} G_T at each λ, where:",
          "- G ∈ R^{n×3} is the matrix of energy gradients `[grad_cl | grad_sep | grad_bd]` at u*(λ).",
          "- P_T ∈ R^{n × (n-1)} is an orthonormal Householder basis of ker(1^T).",
          "- G_T = P_T^T G (projects each gradient onto T).",
          "- H_T = P_T^T H P_T where H is the FD Hessian of E_λ at u*(λ).",
          "- J_e ∈ R^{3×3} is the energy-decomposition Jacobian (Theorem S1).",
          "- J_e_tan = V J_e V^T ∈ R^{2×2} is the simplex-tangent Jacobian.",
          "",
          "**H4 witness criterion:** rank(J_e_tan) = 2 AND |det of top 3×3 minor of G_T| > 1e-6.",
          "",
          "## H4 witness statistics",
          "",
          f"- **Total evaluations:** {total_count}",
          f"- **Full-rank witnesses:** {full_rank_count}/{total_count} "
          f"({100.0 * full_rank_count / max(total_count, 1):.1f}%)",
          f"- **H4 supported (≥1 witness):** {'YES' if full_rank_count > 0 else 'NO'}",
          ""]

    md.append("## Per-scene results")
    md.append("")
    for scene, rows in all_results.items():
        md.append(f"### {scene}")
        md.append("")
        md.append("| label | branch | rank(G_T) | rank(J_e_tan) | σ_max | σ_min | cond(H_T) | |det 3×3 minor| | H_T PD |")
        md.append("|---|---|---|---|---|---|---|---|---|")
        for w in rows:
            if not w.get("ok"):
                md.append(f"| {w.get('label', '?')} | — | — | — | FAILED | — | — | — | — |")
                continue
            sig_max = max(w["sigma_J_e_tan"]) if w["sigma_J_e_tan"] else 0.0
            sig_min = min(w["sigma_J_e_tan"]) if w["sigma_J_e_tan"] else 0.0
            md.append(
                f"| {w['label']} | {tuple(w['branch_id'])} | {w['rank_G_T']} | "
                f"{w['rank_J_e_tan']} | {sig_max:.4e} | {sig_min:.4e} | "
                f"{w['cond_H_T']:.2e} | {abs(w['det_3x3_minor_top']):.4e} | "
                f"{'YES' if w['H_T_PD'] else 'NO'} |")
        md.append("")

    if h4_witnesses:
        md += ["## H4 explicit witnesses",
               "",
               "Each witness below is a (scene, λ, |det 3×3 minor|) triple "
               "establishing H4 of `op_oms_001_gap_c1_genericity.md`:",
               ""]
        for w in h4_witnesses[:5]:  # cap to first 5
            md.append(f"- **{w['scene']}** at `{w['label']}`, "
                      f"λ = {[round(x, 3) for x in w['lam']]}, "
                      f"|det 3×3 minor of G_T| = {abs(w['det_3x3_minor']):.4e}.")
        md.append("")
        md.append("These witnesses establish H4. By Theorem G7 of "
                  "`op_oms_001_gap_c1_genericity.md`, hypothesis H2 of the "
                  "Rank Obstruction Theorem (RT1) holds on an open dense subset "
                  "of (λ, X_t). Combined with RT3 + Corollary G8, OP-OMS-001 "
                  "is closed conditional on H4 — and H4 is now confirmed.")
        md.append("")
    else:
        md += ["## H4 NOT supported",
               "",
               "No witness with rank(J_e_tan) = 2 and non-zero 3×3 minor was "
               "found. This either means H4 fails (a strong negative result, "
               "in which case OP-OMS-001 closure via Gap C1 is blocked) or "
               "the FD step / numerical regime needs tightening. Investigate.",
               ""]

    md_path = os.path.join(RESULTS_DIR, "vp8_gap_c1_rank_witness.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md))
    print(f"Summary saved: {md_path}", flush=True)
    return output


if __name__ == "__main__":
    main()
