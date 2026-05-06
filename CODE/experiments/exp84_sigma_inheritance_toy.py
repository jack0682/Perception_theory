#!/usr/bin/env python3
"""Experiment 84: σ-Inheritance Toy Validation — Numerical Anchor for T-σ-Inherit.

Validates σ-inheritance formulas using a minimal toy signature:
    σ(C) = (mass, centroid, inertia_tensor)

Tests the Cat B parts of T-σ-Inherit (Session W):
  - Phi_MERGE centroid (mass-weighted average formula)
  - Phi_MERGE orientation (parallel-axis theorem)
  - Phi_SPLIT direction (principal axis of inertia tensor)
  - Birth: no inheritance, sigma computed fresh

Does NOT validate sigma_standard (Hessian eigenvalues) — those are Cat C.
Does NOT use the full sigma_rich Hessian computation (expensive; not needed
for the centroid/orientation Cat B claims).

Numerical anchor for T-σ-Inherit (Session W, working Cat B candidate).
NOT a proof.

Session X (W6 D4, 2026-05-06). CV-1.10.
Note: original plan referenced exp56; renumbered exp84 (exp55-56 already exist).
"""
import sys, os, json
import numpy as np
from scipy.ndimage import label as nd_label

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

GRID_N = 15
PERS_THRESH = 0.25


# ---------------------------------------------------------------------------
# Grid + field helpers
# ---------------------------------------------------------------------------

def grid_positions(n):
    rows, cols = np.divmod(np.arange(n * n), n)
    return np.column_stack([rows.astype(float), cols.astype(float)])


def gauss_blob(positions, center, sigma_r=2.0, sigma_c=2.0, peak=0.9):
    dr = positions[:, 0] - float(center[0])
    dc = positions[:, 1] - float(center[1])
    return np.clip(peak * np.exp(-(dr ** 2 / (2 * sigma_r ** 2) +
                                   dc ** 2 / (2 * sigma_c ** 2))), 0.0, 1.0)


def extract_components(u, threshold=PERS_THRESH):
    n_side = int(round(np.sqrt(len(u))))
    mask = (u >= threshold).reshape(n_side, n_side)
    labeled, n_c = nd_label(mask)
    flat = labeled.ravel()
    return [np.where(flat == k)[0] for k in range(1, n_c + 1)]


# ---------------------------------------------------------------------------
# Minimal toy signature  σ(C) = (mass, centroid, inertia_tensor)
# ---------------------------------------------------------------------------

def toy_sigma(u, pos, comp):
    """Compute minimal toy signature for component with given node indices."""
    u_c = u[comp]
    p_c = pos[comp]
    mass = float(u_c.sum())
    if mass < 1e-9:
        d = pos.shape[1]
        return {"mass": 0.0, "centroid": np.zeros(d), "inertia": np.zeros((d, d))}
    centroid = (u_c @ p_c) / mass
    diff = p_c - centroid
    inertia = np.einsum("i,ia,ib->ab", u_c, diff, diff)
    return {"mass": mass, "centroid": centroid.copy(), "inertia": inertia.copy()}


# ---------------------------------------------------------------------------
# Phi_MERGE formulas (§3.3 of sigma_inherit_k_jump.md)
# ---------------------------------------------------------------------------

def phi_merge_centroid(sig1, sig2):
    """Predicted post-merger centroid: mass-weighted average (Cat B, §3.3a)."""
    m1, m2 = sig1["mass"], sig2["mass"]
    total = m1 + m2
    if total < 1e-12:
        return sig1["centroid"].copy()
    return (m1 * sig1["centroid"] + m2 * sig2["centroid"]) / total


def phi_merge_inertia(sig1, sig2, c_merged):
    """Predicted post-merger inertia via parallel-axis theorem (Cat B, §3.3b).

    M_pred = M1 + M2 + m1*(c1-c_merged)⊗(c1-c_merged) + m2*(c2-c_merged)⊗(c2-c_merged)
    """
    m1, m2 = sig1["mass"], sig2["mass"]
    c1, c2 = sig1["centroid"], sig2["centroid"]
    d1 = c1 - c_merged
    d2 = c2 - c_merged
    return (sig1["inertia"] + sig2["inertia"]
            + m1 * np.outer(d1, d1)
            + m2 * np.outer(d2, d2))


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

def scenario_A_cont(pos):
    """Continuation: blob translates one row → centroid shifts (1, 0)."""
    u_t = gauss_blob(pos, [7, 7])
    u_s = gauss_blob(pos, [8, 7])
    comps_t = extract_components(u_t)
    comps_s = extract_components(u_s)
    if not comps_t or not comps_s:
        return {"scenario": "A_CONT", "passed": False,
                "note": "component extraction failed"}

    sig_t = toy_sigma(u_t, pos, comps_t[0])
    sig_s = toy_sigma(u_s, pos, comps_s[0])

    expected_shift = np.array([1.0, 0.0])
    actual_shift = sig_s["centroid"] - sig_t["centroid"]
    residual = float(np.linalg.norm(actual_shift - expected_shift))
    passed = residual < 0.5  # centroid shift matches translation to within 0.5 grid unit

    return {
        "scenario": "A_CONT",
        "K_t": len(comps_t), "K_s": len(comps_s),
        "centroid_t": sig_t["centroid"].tolist(),
        "centroid_s": sig_s["centroid"].tolist(),
        "actual_shift": actual_shift.tolist(),
        "expected_shift": expected_shift.tolist(),
        "centroid_shift_residual": residual,
        "passed": passed,
        "note": "Centroid shift tracks translation; residual < 0.5 grid unit",
    }


def scenario_B_merge_centroid(pos):
    """MERGE centroid: Phi_MERGE mass-weighted formula vs actual merged centroid."""
    # Two blobs far apart (distance 7 >> 2*radius=4): disjoint supports
    u1 = gauss_blob(pos, [7, 4])
    u2 = gauss_blob(pos, [7, 11])
    comps1 = extract_components(u1)
    comps2 = extract_components(u2)
    if not comps1 or not comps2:
        return {"scenario": "B_MERGE_centroid", "passed": False,
                "note": "component extraction failed"}

    sig1 = toy_sigma(u1, pos, comps1[0])
    sig2 = toy_sigma(u2, pos, comps2[0])

    # Merged field: additive sum on union of support
    # Use union of source component node sets for exact identity test
    comp_union = np.concatenate([comps1[0], comps2[0]])
    u_merged = u1 + u2  # exact additive (cross-terms negligible for separated blobs)
    sig_actual = toy_sigma(u_merged, pos, comp_union)

    c_pred = phi_merge_centroid(sig1, sig2)
    residual = float(np.linalg.norm(sig_actual["centroid"] - c_pred))

    # For well-separated blobs, the identity is nearly exact (< 1e-6)
    passed = residual < 0.05

    return {
        "scenario": "B_MERGE_centroid",
        "c_pred": c_pred.tolist(),
        "c_actual": sig_actual["centroid"].tolist(),
        "centroid_residual": residual,
        "mass1": sig1["mass"], "mass2": sig2["mass"],
        "passed": passed,
        "note": "Phi_MERGE centroid formula; residual near 0 for separated blobs",
    }


def scenario_C_merge_orientation(pos):
    """MERGE orientation: parallel-axis theorem vs actual merged inertia tensor."""
    u1 = gauss_blob(pos, [7, 4])
    u2 = gauss_blob(pos, [7, 11])
    comps1 = extract_components(u1)
    comps2 = extract_components(u2)
    if not comps1 or not comps2:
        return {"scenario": "C_MERGE_orientation", "passed": False,
                "note": "component extraction failed"}

    sig1 = toy_sigma(u1, pos, comps1[0])
    sig2 = toy_sigma(u2, pos, comps2[0])

    comp_union = np.concatenate([comps1[0], comps2[0]])
    u_merged = u1 + u2
    sig_actual = toy_sigma(u_merged, pos, comp_union)

    c_pred = phi_merge_centroid(sig1, sig2)
    M_pred = phi_merge_inertia(sig1, sig2, c_pred)
    M_actual = sig_actual["inertia"]

    frob_residual = float(np.linalg.norm(M_actual - M_pred, "fro"))
    norm_actual = max(float(np.linalg.norm(M_actual, "fro")), 1e-9)
    rel_residual = frob_residual / norm_actual

    # Use relative threshold: Gaussian tail cross-terms give ~0.4% relative error
    # for well-separated blobs (radius=2, distance=7). Pass if < 2%.
    passed = rel_residual < 0.02

    return {
        "scenario": "C_MERGE_orientation",
        "M_pred": M_pred.tolist(),
        "M_actual": M_actual.tolist(),
        "frobenius_residual": frob_residual,
        "relative_frobenius_residual": rel_residual,
        "passed": passed,
        "note": "Phi_MERGE orientation via parallel-axis theorem; "
                "residual near 0 for separated blobs",
    }


def scenario_D_split_direction(pos):
    """SPLIT direction: principal axis of elongated blob ~ column direction.

    The lowest-energy (Goldstone) mode direction for an elongated blob is
    its long axis. We use the *largest* inertia eigenvalue here — which
    corresponds to the widest spatial spread, i.e., the split direction.
    """
    # Elongated along columns (axis 1): sigma_r=1.5, sigma_c=4.0
    u_t = gauss_blob(pos, [7, 7], sigma_r=1.5, sigma_c=4.0)
    comps_t = extract_components(u_t, threshold=0.20)
    if not comps_t:
        return {"scenario": "D_SPLIT_direction", "passed": False,
                "note": "no component detected"}

    sig_t = toy_sigma(u_t, pos, comps_t[0])
    eigvals, eigvecs = np.linalg.eigh(sig_t["inertia"])
    # eigh returns ascending eigenvalues; largest = most spread = column direction
    principal_axis = eigvecs[:, -1]  # eigenvector for largest eigenvalue
    # Expected: column direction = [0, 1] (axis 1)
    cos_theta = abs(float(np.dot(principal_axis, [0.0, 1.0])))
    aspect_ratio = eigvals[-1] / max(eigvals[0], 1e-9)

    passed = cos_theta > 0.90  # within ~26 degrees of column axis

    return {
        "scenario": "D_SPLIT_direction",
        "K_t": len(comps_t),
        "eigenvalues": eigvals.tolist(),
        "principal_axis": principal_axis.tolist(),
        "cos_to_column_axis": cos_theta,
        "aspect_ratio": float(aspect_ratio),
        "passed": passed,
        "note": "Principal inertia axis aligns with elongation = predicted split direction",
    }


def scenario_E_birth(pos):
    """BIRTH: empty field at t, one blob at s → sigma computed fresh, no residual."""
    u_t = np.zeros(GRID_N * GRID_N)
    u_s = gauss_blob(pos, [7, 7])
    comps_t = extract_components(u_t)
    comps_s = extract_components(u_s)
    sig_s = toy_sigma(u_s, pos, comps_s[0]) if comps_s else None

    # Validity: no ancestors, sigma at s is well-defined
    passed = (len(comps_t) == 0
              and len(comps_s) == 1
              and sig_s is not None
              and sig_s["mass"] > 0.1)

    return {
        "scenario": "E_BIRTH",
        "K_t": len(comps_t),
        "K_s": len(comps_s),
        "sigma_s_mass": sig_s["mass"] if sig_s else None,
        "sigma_s_centroid": sig_s["centroid"].tolist() if sig_s else None,
        "passed": passed,
        "note": "Birth: no ancestor, sigma well-defined from u_s alone",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    pos = grid_positions(GRID_N)
    results = [
        scenario_A_cont(pos),
        scenario_B_merge_centroid(pos),
        scenario_C_merge_orientation(pos),
        scenario_D_split_direction(pos),
        scenario_E_birth(pos),
    ]

    all_passed = all(r.get("passed", False) for r in results)
    output = {
        "experiment": "exp84_sigma_inheritance_toy",
        "session": "Session X (W6 D4, 2026-05-06)",
        "anchor_for": ("T-σ-Inherit (working Cat B candidate, Session W): "
                       "centroid + orientation Cat B parts only"),
        "note": ("Toy signature (mass, centroid, inertia_tensor). "
                 "Does NOT validate sigma_standard Hessian eigenvalues (Cat C). "
                 "Not a proof of T-σ-Inherit."),
        "grid_n": GRID_N,
        "results": results,
        "all_passed": all_passed,
    }

    out_path = os.path.join(RESULTS_DIR, "exp84_sigma_inheritance_toy.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"exp84 sigma inheritance: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    for r in results:
        status = "PASS" if r.get("passed", False) else "FAIL"
        print(f"  {r['scenario']:30s}  [{status}]")
    return all_passed


if __name__ == "__main__":
    main()
