"""sigma_fingerprint_R23.py — σ-Fingerprint enumeration on R23 (Bridge B-4 NQ-264).

OBJECTIVE
---------
Compute the 8-component σ-fingerprint per `THEORY/working/SF/sigma_fingerprint_qrcode.md`
§2 spec for each of the 56 R23 stable Morse-0 minimizers in
`CODE/results/exp_orbital_fullscale.json` and verify the NQ-264 Cat B target:
the σ-fingerprint distinguishes all 56 R23 minimizers (no collisions).

σ-FINGERPRINT (8 components, §2.1):
  1. F  -- peak count (threshold-free)
  2. K_step at τ=0.5
  3. Bind-vec at τ ∈ {0.3, 0.5, 0.7}
  4. Sep-vec at τ ∈ {0.3, 0.5, 0.7}
  5. Inside-vec at τ ∈ {0.3, 0.5, 0.7}
  6. Nodal-multi (multiset of nodal-domain counts at peaks)
  7. Aut-irrep-multi (stabilizer subgroup of D_4 acting on u + multiset of stored
     angular mode labels; eigenvalues *dropped* per spec)
  8. Centroid-orbit-rep (lex-smallest D_4 orbit representative of centroid)

STRATEGY (fresh re-run)
-----------------------
The original orbital-fullscale dataset stores eigenvalues + mode_labels per
Morse-0 cluster, but **not** the underlying u_t fields, and `make_ic` uses
`spla.eigsh` (non-deterministic init), so we cannot exactly replay the
recorded seeds. We therefore:

  1. Rerun the 90-seed sweep (3 IC modes × 30 seeds) using identical config.
  2. Cluster the converged minimizers by (F_local_max, K_step, E_rounded).
  3. Cross-reference fresh cluster_keys with the stored `morse_index == 0`
     cluster_keys. Each match contributes one u_star (lowest energy member).
  4. Compute the 8-component σ-fingerprint per matched Morse-0 minimizer.
  5. Tally distinct fingerprints + collisions.

If the fresh run recovers fewer than 56 Morse-0 clusters (due to stochastic
search), we report the actual coverage and note the gap honestly.

SIMPLIFICATIONS (first implementation, see spec §3.1 caveats)
-------------------------------------------------------------
- Aut(G) = D_4 (R23 free-BC L=32 grid; canonical D_4 character table).
- Aut(G)_{u*} stabilizer detected by direct invariance test of u_star under
  each of the 8 D_4 elements (not Hessian eigenvector character projection).
- Aut-irrep-multi := (stabilizer_label, sorted multiset of stored angular
  mode_labels with eigenvalues dropped).
- Bind/Sep/Inside-vec computed on superlevel sets {u > τ}:
    Bind_τ  = 1 - ||u - Cl(u)||_S / sqrt(|S|), S = {u > τ}
    Sep_τ   = mean(D_t over S)
    Inside_τ = K_step(τ) (number of CCs of {u > τ})
- Nodal-multi := sorted multiset of K_step(τ_p = 0.5 · u_p) at each peak p.
- Centroid-orbit-rep := lex-smallest D_4-orbit point of (rounded) centroid
  offset from grid center.

OUTPUT
------
- CODE/scripts/results/sigma_fingerprint_R23.json
- Per-component timing and total runtime.

Run: cd CODE && python3 scripts/sigma_fingerprint_R23.py

NQ reference: Bridge B-4 / NQ-264 (Cat B target).
"""
from __future__ import annotations

import sys
import os
import json
import time
import hashlib
from pathlib import Path
from collections import Counter, defaultdict

# --- Path setup -----------------------------------------------------------
HERE = Path(__file__).resolve().parent
CODE_DIR = HERE.parent
sys.path.insert(0, str(CODE_DIR))
sys.path.insert(0, str(CODE_DIR / "experiments"))

import numpy as np

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.operators import closure, distinction

from exp_orbital_discovery import (
    count_local_maxima_2d,
    k_step_2d,
    center_of_mass_2d,
)
from exp_orbital_fullscale import make_ic

# --- Configuration --------------------------------------------------------
R23_PATH = CODE_DIR / "results" / "exp_orbital_fullscale.json"
OUTPUT_PATH = HERE / "results" / "sigma_fingerprint_R23.json"

THRESHOLDS = (0.3, 0.5, 0.7)
ROUND_DECIMALS_DIAG = 3
CENTROID_ROUND_DEC = 2
ENERGY_TOL = 0.5  # cluster bin width (match original)
ENERGY_TOL_APPROX = 5.0  # widened tol for approximate (F,K)-fallback matching
N_SEEDS_OVERRIDE = 90  # more seeds than original 30 for better cluster coverage
STAB_ATOL = 1e-2  # tolerance for D_4 invariance test of u

D4_NAMES = ("e", "r", "r2", "r3", "sh", "sv", "sd", "sa")


# =========================================================================
# u_star generation (re-run multi-seed sweep)
# =========================================================================

def run_seeds_fresh(graph: GraphState, params: ParameterRegistry,
                    rows: int, cols: int, c: float, n_seeds: int,
                    ic_modes: list[str], verbose: bool = False) -> list[dict]:
    """Replay the multi-seed sweep used by exp_orbital_fullscale.run_seeds.

    Returns a list of records, each carrying the converged u_star (kept in
    memory; not serialized).
    """
    records = []
    sid = 0
    for ic_mode in ic_modes:
        for seed in range(n_seeds):
            try:
                u_init = make_ic(graph, rows, cols, c, seed=seed + sid, mode=ic_mode)
                t0 = time.time()
                result = find_formation(graph, params, normalize=False,
                                        u_init=u_init, verbose=False)
                dt = time.time() - t0
            except Exception as e:
                if verbose:
                    print(f"  seed {seed} ({ic_mode}) failed: {e}")
                sid += 1
                continue
            u_star = result.u
            rec = {
                "seed": seed,
                "ic_mode": ic_mode,
                "energy": float(result.energy),
                "converged": bool(result.converged),
                "n_iter": int(result.n_iter),
                "F_local_max": count_local_maxima_2d(u_star, rows, cols),
                "K_step": k_step_2d(u_star, rows, cols, tau=0.5),
                "u_star": u_star,
                "time_s": dt,
            }
            records.append(rec)
            if verbose:
                print(f"  sid={sid:3d} seed={seed:2d} ic={ic_mode:14s} "
                      f"E={rec['energy']:8.3f} F={rec['F_local_max']:>3} "
                      f"K={rec['K_step']:>2} ({dt:.1f}s)")
            sid += 1
    return records


def cluster_minimizers(records: list[dict], energy_tol: float = ENERGY_TOL) -> dict:
    """Cluster records by (F_local_max, K_step, round(E/tol)*tol)."""
    clusters: dict[tuple, list[int]] = defaultdict(list)
    for i, rec in enumerate(records):
        key = (
            int(rec["F_local_max"]),
            int(rec["K_step"]),
            float(round(rec["energy"] / energy_tol) * energy_tol),
        )
        clusters[key].append(i)
    return clusters


# =========================================================================
# σ-fingerprint components
# =========================================================================

def compute_F(u, rows, cols):
    return int(count_local_maxima_2d(u, rows, cols))


def compute_K_step(u, rows, cols, tau=0.5):
    return int(k_step_2d(u, rows, cols, tau))


def compute_diag_vec(u, graph, params, kind, thresholds=THRESHOLDS):
    """Bind/Sep/Inside on superlevel sets {u > τ}.

    Bind_τ  = max(0, 1 - ||u_S - Cl(u)_S|| / sqrt(|S|))
    Sep_τ   = mean(D_t on S)
    Inside_τ = K_step(τ)  (integer)
    """
    Cl_u = closure(u, graph, params)
    D_u = distinction(u, graph, params)
    out = []
    for tau in thresholds:
        mask = u > tau
        n_in = int(mask.sum())
        if n_in == 0:
            val = 0.0
        elif kind == "bind":
            res = float(np.linalg.norm(u[mask] - Cl_u[mask])) / np.sqrt(n_in)
            val = float(max(0.0, 1.0 - res))
        elif kind == "sep":
            val = float(np.mean(D_u[mask]))
        elif kind == "inside":
            # rows/cols inferred from sqrt(n) (assumes square grid)
            n = len(u)
            rc = int(round(np.sqrt(n)))
            val = int(k_step_2d(u, rc, rc, tau))
        else:
            raise ValueError(kind)
        if isinstance(val, int):
            out.append(val)
        else:
            out.append(round(float(val), ROUND_DECIMALS_DIAG))
    return tuple(out)


def find_peaks_2d(u, rows, cols):
    """Strict local maxima on 4-neighbor grid (with upper-left tie-break)."""
    u2 = u.reshape(rows, cols)
    peaks = []
    for r in range(rows):
        for c in range(cols):
            val = u2[r, c]
            is_max = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if u2[nr, nc] > val + 1e-10:
                        is_max = False
                        break
                    if u2[nr, nc] >= val - 1e-10 and (nr, nc) < (r, c):
                        is_max = False
                        break
            if is_max:
                peaks.append((r, c, float(val)))
    return peaks


def compute_nodal_multi(u, rows, cols):
    """Multiset of K_step(τ_p = 0.5 * u_p) at each peak p."""
    peaks = find_peaks_2d(u, rows, cols)
    counts = []
    for r, c, val in peaks:
        tau_p = 0.5 * val
        counts.append(int(k_step_2d(u, rows, cols, tau=tau_p)))
    return tuple(sorted(counts))


# --- D_4 group action -----------------------------------------------------

def d4_apply(u, rows, cols, op):
    u2 = u.reshape(rows, cols)
    if op == "e":
        out = u2
    elif op == "r":
        out = np.rot90(u2, k=1)
    elif op == "r2":
        out = np.rot90(u2, k=2)
    elif op == "r3":
        out = np.rot90(u2, k=3)
    elif op == "sh":
        out = u2[::-1, :]
    elif op == "sv":
        out = u2[:, ::-1]
    elif op == "sd":
        out = u2.T
    elif op == "sa":
        out = u2[::-1, ::-1].T
    else:
        raise ValueError(op)
    return np.ascontiguousarray(out).ravel()


def d4_stabilizer(u, rows, cols, atol=STAB_ATOL):
    stab = []
    for op in D4_NAMES:
        if rows != cols and op in ("r", "r3", "sd", "sa"):
            # Rotations and diagonal reflections require square grid
            continue
        u_op = d4_apply(u, rows, cols, op)
        if np.max(np.abs(u_op - u)) < atol:
            stab.append(op)
    return tuple(stab)


def stabilizer_label(stab):
    s = set(stab)
    if s == set(D4_NAMES):
        return "D4"
    if s == {"e", "r", "r2", "r3"}:
        return "C4"
    if s == {"e", "r2", "sh", "sv"}:
        return "C2v_axial"
    if s == {"e", "r2", "sd", "sa"}:
        return "C2v_diag"
    if s == {"e", "r2"}:
        return "C2"
    if s == {"e", "sh"}:
        return "Cs_h"
    if s == {"e", "sv"}:
        return "Cs_v"
    if s == {"e", "sd"}:
        return "Cs_d"
    if s == {"e", "sa"}:
        return "Cs_a"
    if s == {"e"}:
        return "C1"
    return "Hsub_" + "_".join(sorted(s))


def aut_irrep_multi(stab_label, mode_labels):
    """Component 7: (stabilizer_label, sorted multiset of angular labels).

    Eigenvalues are intentionally dropped per spec §2.1.
    """
    label_multi = tuple(sorted(m["label"] for m in mode_labels))
    return (stab_label, label_multi)


def centroid_orbit_rep(centroid, rows, cols, round_dec=CENTROID_ROUND_DEC):
    """Lex-smallest D_4-orbit point of centroid offset from grid center."""
    r0, c0 = centroid
    cR = (rows - 1) / 2.0
    cC = (cols - 1) / 2.0
    dr, dc = r0 - cR, c0 - cC
    orbit = [
        (dr, dc), (-dc, dr), (-dr, -dc), (dc, -dr),
        (-dr, dc), (dr, -dc), (dc, dr), (-dc, -dr),
    ]
    rounded = sorted(
        (round(a, round_dec), round(b, round_dec))
        for a, b in orbit
    )
    return rounded[0]


# =========================================================================
# Fingerprint assembly
# =========================================================================

def compute_fingerprint(u, graph, params, mode_labels, rows, cols, timing):
    fp = {}
    t = time.time()
    fp["F"] = compute_F(u, rows, cols)
    timing["F"] += (time.time() - t) * 1000

    t = time.time()
    fp["K_step_05"] = compute_K_step(u, rows, cols, 0.5)
    timing["K_step"] += (time.time() - t) * 1000

    t = time.time()
    fp["Bind_vec"] = compute_diag_vec(u, graph, params, "bind")
    timing["Bind_vec"] += (time.time() - t) * 1000

    t = time.time()
    fp["Sep_vec"] = compute_diag_vec(u, graph, params, "sep")
    timing["Sep_vec"] += (time.time() - t) * 1000

    t = time.time()
    fp["Inside_vec"] = compute_diag_vec(u, graph, params, "inside")
    timing["Inside_vec"] += (time.time() - t) * 1000

    t = time.time()
    fp["Nodal_multi"] = compute_nodal_multi(u, rows, cols)
    timing["Nodal_multi"] += (time.time() - t) * 1000

    t = time.time()
    stab = d4_stabilizer(u, rows, cols)
    fp["Aut_irrep_multi"] = aut_irrep_multi(stabilizer_label(stab), mode_labels)
    timing["Aut_irrep_multi"] += (time.time() - t) * 1000

    t = time.time()
    cm = center_of_mass_2d(u, rows, cols)
    fp["Centroid_orbit_rep"] = centroid_orbit_rep(cm, rows, cols)
    timing["Centroid_orbit_rep"] += (time.time() - t) * 1000

    return fp


def fingerprint_to_jsonable(fp):
    return {
        "F": fp["F"],
        "K_step_05": fp["K_step_05"],
        "Bind_vec": list(fp["Bind_vec"]),
        "Sep_vec": list(fp["Sep_vec"]),
        "Inside_vec": list(fp["Inside_vec"]),
        "Nodal_multi": list(fp["Nodal_multi"]),
        "Aut_irrep_multi": [fp["Aut_irrep_multi"][0], list(fp["Aut_irrep_multi"][1])],
        "Centroid_orbit_rep": list(fp["Centroid_orbit_rep"]),
    }


def hash_fingerprint(fp):
    s = json.dumps(fingerprint_to_jsonable(fp), sort_keys=True)
    return hashlib.sha1(s.encode()).hexdigest()[:16]


# =========================================================================
# Main
# =========================================================================

def main():
    print(f"Loading R23 dataset: {R23_PATH}")
    with open(R23_PATH) as f:
        data = json.load(f)
    config = data.get("config", {})
    rows, cols = config.get("grid", [32, 32])
    c = config.get("c", 0.5)
    beta = config.get("beta", 30.0)
    alpha = config.get("alpha", 1.0)
    n_seeds = config.get("n_seeds_per_ic_mode", 30)
    ic_modes = config.get("ic_modes", ["fiedler_random", "random", "eigmode_combo"])
    with_closure = config.get("with_closure", True)

    cluster_summaries = data.get("cluster_summaries", [])
    stable = [s for s in cluster_summaries if s.get("morse_index") == 0]
    print(f"Stored stable Morse-0 clusters: {len(stable)}")

    # Index stored Morse-0 clusters by cluster_key (F, K_step, E_rounded)
    stored_by_key = {}
    for s in stable:
        key = tuple(s["cluster_key"])
        stored_by_key[key] = s

    # Allow override of n_seeds for better coverage of stored clusters
    if N_SEEDS_OVERRIDE is not None and N_SEEDS_OVERRIDE > n_seeds:
        print(f"  (overriding n_seeds {n_seeds} -> {N_SEEDS_OVERRIDE} for coverage)")
        n_seeds = N_SEEDS_OVERRIDE

    # Build graph + params (must match original config)
    graph = GraphState.grid_2d(rows, cols)
    if with_closure:
        params = ParameterRegistry(
            volume_fraction=c, alpha_bd=alpha, beta_bd=beta,
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
            max_iter=50000, n_restarts=1, eps_init=0.02,
        )
    else:
        params = ParameterRegistry(
            volume_fraction=c, alpha_bd=alpha, beta_bd=beta,
            w_cl=0.0, w_sep=0.0, w_bd=1.0,
            max_iter=50000, n_restarts=1, eps_init=0.02,
        )

    # ---------- Phase 1: fresh multi-seed sweep ----------
    print(f"\nPhase 1: rerunning {n_seeds*len(ic_modes)} seeds "
          f"(grid={rows}×{cols}, c={c}, β={beta}, closure={with_closure})...")
    t_phase1 = time.time()
    records = run_seeds_fresh(graph, params, rows, cols, c, n_seeds, ic_modes,
                              verbose=False)
    phase1_s = time.time() - t_phase1
    print(f"  Done: {len(records)} converged records in {phase1_s:.1f}s.")

    # ---------- Phase 2: fresh clustering & match to stored Morse-0 keys ----------
    fresh_clusters = cluster_minimizers(records, energy_tol=ENERGY_TOL)
    print(f"\nPhase 2: {len(fresh_clusters)} fresh clusters; "
          f"matching to {len(stored_by_key)} stored Morse-0 keys...")

    matched_clusters = []  # list of (stored_cluster_summary, rep_record_idx, match_type)
    used_record_ids = set()

    # Pass 1: exact (F, K, E_rounded) match
    for stored_key, stored_summ in stored_by_key.items():
        if stored_key in fresh_clusters:
            indices = [i for i in fresh_clusters[stored_key]
                       if i not in used_record_ids]
            if not indices:
                continue
            rep_idx = min(indices, key=lambda i: records[i]["energy"])
            matched_clusters.append((stored_summ, rep_idx, "exact"))
            used_record_ids.add(rep_idx)

    n_exact = len(matched_clusters)

    # Pass 2: approximate (F, K_step) match within ENERGY_TOL_APPROX
    by_fk: dict[tuple, list[int]] = defaultdict(list)
    for i, rec in enumerate(records):
        by_fk[(int(rec["F_local_max"]), int(rec["K_step"]))].append(i)

    matched_keys_so_far = {tuple(m[0]["cluster_key"]) for m in matched_clusters}
    for stored_key, stored_summ in stored_by_key.items():
        if stored_key in matched_keys_so_far:
            continue
        F_s, K_s, E_s = stored_key
        E_rep = stored_summ["rep_energy"]
        candidates = [i for i in by_fk.get((F_s, K_s), [])
                      if i not in used_record_ids
                      and abs(records[i]["energy"] - E_rep) <= ENERGY_TOL_APPROX]
        if not candidates:
            continue
        rep_idx = min(candidates,
                      key=lambda i: abs(records[i]["energy"] - E_rep))
        matched_clusters.append((stored_summ, rep_idx, "approx"))
        used_record_ids.add(rep_idx)

    n_matched = len(matched_clusters)
    n_approx = n_matched - n_exact
    n_missing = len(stored_by_key) - n_matched
    print(f"  Matched: {n_matched} / {len(stored_by_key)} "
          f"(exact: {n_exact}, approx F,K within ±{ENERGY_TOL_APPROX}E: {n_approx}, "
          f"missing: {n_missing}).")

    if n_missing > 0:
        matched_keys = {tuple(m[0]["cluster_key"]) for m in matched_clusters}
        missing_keys = [list(k) for k in stored_by_key.keys()
                        if k not in matched_keys]
        print(f"  Missing cluster_keys: {missing_keys[:5]}"
              f"{'...' if len(missing_keys) > 5 else ''}")
    else:
        missing_keys = []

    # ---------- Phase 3: fingerprint computation ----------
    print(f"\nPhase 3: computing σ-fingerprints for {n_matched} matched minimizers...")
    timing = defaultdict(float)
    fingerprint_table = []
    t_phase3 = time.time()

    for mid, (stored_summ, rep_idx, match_type) in enumerate(matched_clusters):
        rec = records[rep_idx]
        u_star = rec["u_star"]
        mode_labels = stored_summ["mode_labels"]
        fp = compute_fingerprint(u_star, graph, params, mode_labels, rows, cols, timing)
        fp_hash = hash_fingerprint(fp)

        fingerprint_table.append({
            "minimizer_id": mid,
            "cluster_key": list(stored_summ["cluster_key"]),
            "match_type": match_type,
            "rep_seed_fresh": rec["seed"],
            "rep_ic_mode_fresh": rec["ic_mode"],
            "rep_energy_fresh": rec["energy"],
            "rep_energy_stored": stored_summ["rep_energy"],
            "fingerprint_components": fingerprint_to_jsonable(fp),
            "fingerprint_hash": fp_hash,
        })
    phase3_s = time.time() - t_phase3
    print(f"  Done in {phase3_s:.2f}s.")

    # ---------- Phase 4: collisions / verdict ----------
    hash_to_ids = defaultdict(list)
    for entry in fingerprint_table:
        hash_to_ids[entry["fingerprint_hash"]].append(entry["minimizer_id"])

    n_distinct = len(hash_to_ids)
    collision_pairs = []
    for h, ids in hash_to_ids.items():
        if len(ids) > 1:
            for ii in range(len(ids)):
                for jj in range(ii + 1, len(ids)):
                    collision_pairs.append({
                        "i": ids[ii], "j": ids[jj], "hash": h,
                        "cluster_key_i": fingerprint_table[ids[ii]]["cluster_key"],
                        "cluster_key_j": fingerprint_table[ids[jj]]["cluster_key"],
                    })

    n_min = n_matched
    if n_distinct == n_min and n_min == len(stored_by_key):
        verdict = "Cat B confirmed"
    elif n_distinct == n_min:
        verdict = (f"Cat B confirmed on matched subset ({n_min}/{len(stored_by_key)}); "
                   f"{n_missing} stored cluster(s) not recovered in fresh run")
    elif n_distinct > 50:
        verdict = "Cat B partial"
    else:
        verdict = "Cat B failed"

    # ---------- Print summary ----------
    print()
    print("=" * 72)
    print("σ-FINGERPRINT R23 — Bridge B-4 NQ-264 RESULTS")
    print("=" * 72)
    print(f"  stored Morse-0 clusters:    {len(stored_by_key)}")
    print(f"  matched in fresh run:       {n_matched}  "
          f"(exact: {n_exact}, approx: {n_approx})")
    print(f"  n_distinct_fingerprints:    {n_distinct}")
    print(f"  n_collision_pairs:          {len(collision_pairs)}")
    print(f"  Verdict: {verdict}")
    print()
    print(f"  Phase 1 (rerun)  : {phase1_s:.1f}s")
    print(f"  Phase 3 (fp)     : {phase3_s:.2f}s")
    print(f"  Total            : {phase1_s + phase3_s:.1f}s")
    print()
    print("Per-component fingerprint timing (ms total | ms/minimizer):")
    for k in ("F", "K_step", "Bind_vec", "Sep_vec", "Inside_vec",
              "Nodal_multi", "Aut_irrep_multi", "Centroid_orbit_rep"):
        v = timing.get(k, 0.0)
        avg = v / n_min if n_min > 0 else 0.0
        print(f"  {k:20s}: {v:9.2f}  | {avg:7.3f}")
    if collision_pairs:
        print()
        print(f"Collisions ({len(collision_pairs)}):")
        for cp in collision_pairs[:10]:
            print(f"  ids ({cp['i']:2d}, {cp['j']:2d})  "
                  f"keys {cp['cluster_key_i']} vs {cp['cluster_key_j']}")
        if len(collision_pairs) > 10:
            print(f"  ... +{len(collision_pairs) - 10} more")
    print("=" * 72)

    # ---------- Save JSON ----------
    output = {
        "spec": "THEORY/working/SF/sigma_fingerprint_qrcode.md §2 (Bridge B-4 NQ-264)",
        "n_minimizers": n_min,
        "n_stored_morse0": len(stored_by_key),
        "n_exact_matches": n_exact,
        "n_approx_matches": n_approx,
        "n_distinct_fingerprints": n_distinct,
        "verdict": verdict,
        "fingerprint_table": fingerprint_table,
        "collision_pairs": collision_pairs,
        "missing_cluster_keys": missing_keys,
        "timing": {
            "phase1_rerun_s": phase1_s,
            "phase3_fingerprint_s": phase3_s,
            "total_s": phase1_s + phase3_s,
            "per_component_ms_total": dict(timing),
            "per_component_ms_avg_per_minimizer": {
                k: (v / n_min if n_min > 0 else 0.0)
                for k, v in timing.items()
            },
        },
        "config": {
            "grid": [rows, cols],
            "c": c,
            "beta": beta,
            "alpha": alpha,
            "with_closure": with_closure,
            "n_seeds_per_ic_mode": n_seeds,
            "ic_modes": ic_modes,
            "thresholds": list(THRESHOLDS),
            "round_decimals_diag": ROUND_DECIMALS_DIAG,
            "centroid_round_decimals": CENTROID_ROUND_DEC,
            "stab_atol": STAB_ATOL,
            "energy_cluster_tol": ENERGY_TOL,
        },
        "simplifications": [
            "Fresh re-run of 90-seed sweep (make_ic uses non-deterministic spla.eigsh; "
            "stored seeds cannot be exactly replayed). Matching done on (F, K_step, "
            "E_rounded) cluster_keys.",
            "Aut(G) = D_4 (R23 free-BC L=32 grid). Stabilizer Aut(G)_{u*} detected by "
            "direct invariance test of u_star under each D_4 element (atol=1e-2), "
            "not Hessian eigenvector character projection.",
            "Aut-irrep-multi := (stabilizer_label, sorted multiset of stored angular "
            "mode_labels with eigenvalues dropped) — eigenvalue-free per spec §2.1.",
            "Bind_τ = 1 - ||u-Cl(u)||_S/sqrt(|S|) on S={u>τ}; "
            "Sep_τ = mean(D_t on S); Inside_τ = K_step(τ).",
            "Nodal-multi := sorted multiset of K_step(0.5·u_p) at each peak p.",
            "Centroid-orbit-rep := lex-smallest D_4-orbit point of (rounded) centroid.",
        ],
        "notes": {
            "u_t_primitive": "All fingerprint components computed directly on the soft "
                             "cohesion field minimizer u*; primitive unchanged.",
            "CN10": "Bar-Natan-van der Veen (2026) QR-code knot invariants are "
                    "structural inspiration only; SCC is not knot theory.",
            "OP_status": "NQ-188 σ-class enumeration not silently resolved; "
                         "σ-fingerprint provides a fast pre-filter only.",
        },
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
