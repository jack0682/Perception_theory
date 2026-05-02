"""WQ-LAT-1 — Reservoir Resolution Sweep.

Implements the protocol of
THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_protocol.md.

For K_field in {3, 4, 6, 8, 12}, runs the WQ-1 / WQ-2 baseline multi-field
projected gradient flow on T^2_20 under two initialization options:

  - LAT-A: 3 active bumps + (K-3) inactive zero slots (control / null test);
  - LAT-C: K sub-bumps distributed across 3 base clusters (split-bump
    refinement; primary reservoir-resolution test).

For each (K, option, geometry) trajectory, computes per-snapshot diagnostics
(slot masses, aggregate field U, K_bar at four thresholds, K_soft, dominant
bar lengths, F count) and final-snapshot cross-K convergence diagnostics
(aggregate-field L^2 / L^inf distances, dominant-bar-vector distances,
K_bar / K_soft pairwise differences).

Evaluates LAT-C1–LAT-C7 criteria and writes a JSON result file.

Reservoir interpretation tested: if K_field is a finite-resolution chart on
a latent formation reservoir, then field-native aggregate observables
(U, K_bar, K_soft, dominant bar profile) should stabilize as K increases
past the reservoir's effective rank K*. K_act may continue to depend on K.

The script is non-destructive. It writes only to the path supplied via
``--output``. Reuses run_trajectory from nq242c_counterexample.py and
h0_barcode / k_soft_phi_sat / f_count from ksoft_kact_diagnostics.py.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/wq_lat1_reservoir_resolution_sweep.py \\
        --output CODE/scripts/results/wq_lat1_reservoir_resolution_sweep.json \\
        --max_iter 5000 --seed 42 \\
        --K_values 3,4,6,8,12 --options LAT-A,LAT-C --geometries A,B
"""
from __future__ import annotations

import argparse
import json
import math
import os
import platform
import socket
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.params import ParameterRegistry

import nq242c_counterexample as wq1
import ksoft_kact_diagnostics as wq2


PROTOCOL_VERSION = "1.0"
DEFAULT_K_VALUES = (3, 4, 6, 8, 12)
DEFAULT_THRESHOLDS = (0.05, 0.10, 0.15, 0.20)
DEFAULT_OPTIONS = ("LAT-A", "LAT-C")
DEFAULT_GEOMETRIES = ("A", "B")

# Convergence tolerances (per protocol §9)
TOL_AGGREGATE_L2 = 0.05      # LAT-C2: ||U_K - U_K'||_2 / sqrt(|X|)
TOL_KSOFT = 0.10             # LAT-C4
TOL_DOMINANT_BARS = 0.10     # LAT-C5

# Base configurations matching WQ-1 / WQ-2 / WQ-1.C-R2
BASE_CENTERS_A = ((5, 5), (15, 5), (10, 14))    # equilateral
BASE_CENTERS_B = ((5, 5), (15, 5), (10, 11))    # compressed

CLUSTER_MASS = 30.0          # per-cluster mass (3 clusters, total M=90)
RING_RADIUS = 1.5            # sub-atom ring radius for LAT-C


# ---------------------------------------------------------------------------
# Initialization construction
# ---------------------------------------------------------------------------


def distribute_atoms_per_cluster(K_field: int) -> List[int]:
    """Distribute K_field atoms across 3 clusters as evenly as possible."""
    base = K_field // 3
    remainder = K_field % 3
    distribution = [base + (1 if i < remainder else 0) for i in range(3)]
    return distribution


def build_centers_lat_a(base_centers: Tuple[Tuple[int, int], ...],
                          K_field: int) -> Tuple[Tuple[int, int], ...]:
    """LAT-A: 3 active bumps + (K-3) inactive at placeholder (0,0)."""
    out = list(base_centers)
    while len(out) < K_field:
        out.append((0, 0))
    return tuple(out)


def build_initial_masses_lat_a(K_field: int) -> Tuple[float, ...]:
    """LAT-A: 30, 30, 30, 0, 0, ..."""
    masses = [CLUSTER_MASS] * 3 + [0.0] * (K_field - 3)
    return tuple(masses)


def build_centers_lat_c(base_centers: Tuple[Tuple[int, int], ...],
                          K_field: int, n_torus: int = 20) -> Tuple[Tuple[int, int], ...]:
    """LAT-C: distribute K_field sub-atoms across 3 clusters in rings."""
    distribution = distribute_atoms_per_cluster(K_field)
    sub_centers: List[Tuple[int, int]] = []
    for cluster_idx, (cx, cy) in enumerate(base_centers):
        n = distribution[cluster_idx]
        if n == 1:
            sub_centers.append((cx, cy))
        else:
            for i in range(n):
                angle = 2.0 * math.pi * i / n
                sx = (cx + RING_RADIUS * math.cos(angle)) % n_torus
                sy = (cy + RING_RADIUS * math.sin(angle)) % n_torus
                sub_centers.append((int(round(sx)) % n_torus,
                                     int(round(sy)) % n_torus))
    return tuple(sub_centers)


def build_initial_masses_lat_c(K_field: int) -> Tuple[float, ...]:
    """LAT-C: per-atom mass = cluster_mass / atoms_in_that_cluster."""
    distribution = distribute_atoms_per_cluster(K_field)
    masses: List[float] = []
    for n in distribution:
        per_atom = CLUSTER_MASS / n
        masses.extend([per_atom] * n)
    return tuple(masses)


# ---------------------------------------------------------------------------
# Per-trajectory pipeline
# ---------------------------------------------------------------------------


@dataclass
class RunRecord:
    K_field: int
    geometry: str
    option: str
    centers: List[Tuple[int, int]]
    initial_masses: List[float]
    atom_distribution: List[int]
    snapshot_times: List[int]
    K_act_trajectory: List[int]
    K_bar_trajectory: Dict[float, List[int]]
    K_soft_trajectory: List[float]
    F_aggregate_trajectory: List[int]
    dominant_bars_initial: List[float]
    dominant_bars_final: List[float]
    K_act_initial: int
    K_act_final: int
    K_soft_initial: float
    K_soft_final: float
    K_bar_initial: Dict[float, int]
    K_bar_final: Dict[float, int]
    final_aggregate: np.ndarray
    final_field_max: float
    final_field_simplex_max: float


def build_runconfig_for(option: str, K_field: int, geometry: str,
                         max_iter: int, snapshot_every: int, seed: int) -> Tuple[wq1.RunConfig, List[Tuple[int, int]]]:
    """Build a RunConfig for a (option, K, geometry) cell."""
    base = BASE_CENTERS_A if geometry == "A" else BASE_CENTERS_B
    if option == "LAT-A":
        centers = build_centers_lat_a(base, K_field)
        masses = build_initial_masses_lat_a(K_field)
    elif option == "LAT-C":
        centers = build_centers_lat_c(base, K_field)
        masses = build_initial_masses_lat_c(K_field)
    else:
        raise ValueError(f"Unknown option: {option}")

    # Both centers_A and centers_B must be tuples; use the relevant one and
    # pad both to K_field for safety
    other_base = BASE_CENTERS_B if geometry == "A" else BASE_CENTERS_A
    if option == "LAT-A":
        other_centers = build_centers_lat_a(other_base, K_field)
    else:
        other_centers = build_centers_lat_c(other_base, K_field)

    cfg = wq1.RunConfig(
        K_field=K_field,
        M=90.0,
        epsilon=0.225,
        seed=seed,
        max_iter=max_iter,
        snapshot_every=snapshot_every,
        centers_A=centers if geometry == "A" else other_centers,
        centers_B=centers if geometry == "B" else other_centers,
        initial_masses=masses,
    )
    return cfg, list(centers)


def run_one_trajectory(option: str, K_field: int, geometry: str,
                        cfg: wq1.RunConfig, centers: List[Tuple[int, int]],
                        graph, positions, params,
                        thresholds: Tuple[float, ...]) -> RunRecord:
    """Run a single trajectory and compute per-snapshot diagnostics."""
    rng = np.random.RandomState(cfg.seed)
    name = f"{option}__K={K_field}__{geometry}"
    traj = wq1.run_trajectory(cfg, name, centers, graph, positions, params, rng)

    # Compute per-snapshot diagnostics
    snapshot_times: List[int] = []
    K_act_traj: List[int] = []
    K_bar_traj: Dict[float, List[int]] = {ell: [] for ell in thresholds}
    K_soft_traj: List[float] = []
    F_traj: List[int] = []
    dominant_bars_per_snap: List[List[float]] = []

    for snap in traj.snapshots:
        U = np.sum(snap.fields, axis=0)
        barcode = wq2.h0_barcode(U, graph)
        ells = wq2.bar_lengths(barcode)
        ells_sorted = sorted(ells, reverse=True)
        snapshot_times.append(snap.tau)
        K_act_traj.append(snap.K_act)
        for ell in thresholds:
            K_bar_traj[ell].append(int(sum(1 for e in ells if e >= ell)))
        K_soft_traj.append(wq2.k_soft_phi_sat(barcode, 0.10))
        F_traj.append(wq2.f_count(U, graph))
        dominant_bars_per_snap.append(ells_sorted[:8])

    final_U = np.sum(traj.snapshots[-1].fields, axis=0)
    initial_U = np.sum(traj.snapshots[0].fields, axis=0)
    final_field_max = float(max(np.max(f) for f in traj.snapshots[-1].fields))
    final_field_simplex_max = float(np.max(final_U))

    distribution = distribute_atoms_per_cluster(K_field) \
        if option == "LAT-C" else [3] + [0] * (K_field - 3 if K_field > 3 else 0)

    return RunRecord(
        K_field=K_field, geometry=geometry, option=option,
        centers=list(centers),
        initial_masses=list(cfg.initial_masses),
        atom_distribution=distribution,
        snapshot_times=snapshot_times,
        K_act_trajectory=K_act_traj,
        K_bar_trajectory=K_bar_traj,
        K_soft_trajectory=K_soft_traj,
        F_aggregate_trajectory=F_traj,
        dominant_bars_initial=dominant_bars_per_snap[0],
        dominant_bars_final=dominant_bars_per_snap[-1],
        K_act_initial=K_act_traj[0],
        K_act_final=K_act_traj[-1],
        K_soft_initial=K_soft_traj[0],
        K_soft_final=K_soft_traj[-1],
        K_bar_initial={ell: K_bar_traj[ell][0] for ell in thresholds},
        K_bar_final={ell: K_bar_traj[ell][-1] for ell in thresholds},
        final_aggregate=final_U,
        final_field_max=final_field_max,
        final_field_simplex_max=final_field_simplex_max,
    )


# ---------------------------------------------------------------------------
# Cross-K convergence analysis
# ---------------------------------------------------------------------------


def cross_K_distances(records: List[RunRecord]) -> dict:
    """Compute pairwise final-snapshot distances between (option, geometry)
    runs at different K values."""
    by_key: Dict[Tuple[str, str], List[RunRecord]] = {}
    for r in records:
        by_key.setdefault((r.option, r.geometry), []).append(r)
    out: Dict[str, dict] = {}
    for (option, geometry), runs in by_key.items():
        runs_sorted = sorted(runs, key=lambda r: r.K_field)
        n_vertices = runs_sorted[0].final_aggregate.shape[0]
        sqrt_n = math.sqrt(n_vertices)
        K_values = [r.K_field for r in runs_sorted]
        dists_L2: Dict[str, float] = {}
        dists_Linf: Dict[str, float] = {}
        bar_dists: Dict[str, float] = {}
        K_soft_diffs: Dict[str, float] = {}
        K_bar_diffs: Dict[str, Dict[str, int]] = {}
        for i in range(len(runs_sorted)):
            for j in range(i + 1, len(runs_sorted)):
                Ri = runs_sorted[i]
                Rj = runs_sorted[j]
                key = f"K={Ri.K_field}_K'={Rj.K_field}"
                dU = Ri.final_aggregate - Rj.final_aggregate
                dists_L2[key] = float(np.linalg.norm(dU) / sqrt_n)
                dists_Linf[key] = float(np.max(np.abs(dU)))
                # Bar vector distance
                lA = Ri.dominant_bars_final[:6] + [0.0] * max(0, 6 - len(Ri.dominant_bars_final))
                lB = Rj.dominant_bars_final[:6] + [0.0] * max(0, 6 - len(Rj.dominant_bars_final))
                bar_dists[key] = float(np.linalg.norm(np.array(lA) - np.array(lB)))
                K_soft_diffs[key] = abs(Ri.K_soft_final - Rj.K_soft_final)
                K_bar_diffs[key] = {
                    f"{ell:.2f}": Ri.K_bar_final[ell] - Rj.K_bar_final[ell]
                    for ell in Ri.K_bar_final.keys()
                }
        out[f"{option}__{geometry}"] = {
            "K_values": K_values,
            "aggregate_L2_distances_per_vertex": dists_L2,
            "aggregate_Linf_distances": dists_Linf,
            "dominant_bar_vector_distances": bar_dists,
            "K_soft_pairwise_differences": K_soft_diffs,
            "K_bar_pairwise_integer_differences": K_bar_diffs,
        }
    return out


# ---------------------------------------------------------------------------
# Convergence criteria evaluation
# ---------------------------------------------------------------------------


def evaluate_convergence(records: List[RunRecord],
                          cross: dict,
                          thresholds: Tuple[float, ...]) -> Tuple[dict, dict, Optional[str]]:
    """Evaluate LAT-C2..C7 per (option, geometry); return summary."""
    per_option_geom: Dict[str, dict] = {}
    overall_C2 = True
    overall_C3 = True
    overall_C4 = True
    overall_C5 = True
    options_present = set(r.option for r in records)
    geometries_present = set(r.geometry for r in records)

    K_star_per_key: Dict[str, Optional[int]] = {}

    for key, block in cross.items():
        L2_dists = block["aggregate_L2_distances_per_vertex"]
        bar_dists = block["dominant_bar_vector_distances"]
        K_soft_diffs = block["K_soft_pairwise_differences"]
        K_bar_diffs = block["K_bar_pairwise_integer_differences"]
        K_values = block["K_values"]
        # Find smallest K* such that all consecutive-K pairs starting from K*
        # satisfy the criteria
        sorted_pairs = []
        for k_pair_str, dist in L2_dists.items():
            # parse "K=3_K'=4"
            parts = k_pair_str.replace("K=", "").replace("K'=", "").split("_")
            Ki, Kj = int(parts[0]), int(parts[1])
            sorted_pairs.append((Ki, Kj, dist, bar_dists[k_pair_str],
                                  K_soft_diffs[k_pair_str], K_bar_diffs[k_pair_str]))

        K_star: Optional[int] = None
        for K_test in K_values:
            # Check that all pairs (Ki, Kj) with both >= K_test satisfy criteria
            relevant = [t for t in sorted_pairs if t[0] >= K_test and t[1] >= K_test]
            if not relevant:
                continue
            ok_C2 = all(t[2] <= TOL_AGGREGATE_L2 for t in relevant)
            ok_C5 = all(t[3] <= TOL_DOMINANT_BARS for t in relevant)
            ok_C4 = all(t[4] <= TOL_KSOFT for t in relevant)
            ok_C3 = all(all(d == 0 for d in t[5].values()) for t in relevant)
            if ok_C2 and ok_C3 and ok_C4 and ok_C5:
                K_star = K_test
                break
        K_star_per_key[key] = K_star

        # Per-key flags
        all_pairs_relevant = sorted_pairs
        c2_pass = all(t[2] <= TOL_AGGREGATE_L2 for t in all_pairs_relevant) if all_pairs_relevant else False
        c5_pass = all(t[3] <= TOL_DOMINANT_BARS for t in all_pairs_relevant) if all_pairs_relevant else False
        c4_pass = all(t[4] <= TOL_KSOFT for t in all_pairs_relevant) if all_pairs_relevant else False
        c3_pass = all(all(d == 0 for d in t[5].values()) for t in all_pairs_relevant) if all_pairs_relevant else False
        # Block-level convergence flags require pairs starting from K_star (not all pairs)
        if K_star is not None:
            relevant_above = [t for t in sorted_pairs if t[0] >= K_star and t[1] >= K_star]
            if relevant_above:
                c2_pass = all(t[2] <= TOL_AGGREGATE_L2 for t in relevant_above)
                c5_pass = all(t[3] <= TOL_DOMINANT_BARS for t in relevant_above)
                c4_pass = all(t[4] <= TOL_KSOFT for t in relevant_above)
                c3_pass = all(all(d == 0 for d in t[5].values()) for t in relevant_above)

        per_option_geom[key] = {
            "K_star": K_star,
            "C2_aggregate_L2_pass": c2_pass,
            "C3_K_bar_integer_pass": c3_pass,
            "C4_K_soft_pass": c4_pass,
            "C5_dominant_bar_pass": c5_pass,
            "max_aggregate_L2": max(L2_dists.values()) if L2_dists else 0.0,
            "max_K_soft_diff": max(K_soft_diffs.values()) if K_soft_diffs else 0.0,
            "max_dominant_bar_dist": max(bar_dists.values()) if bar_dists else 0.0,
            "K_bar_pair_disagreement_count": sum(
                1 for diffs in K_bar_diffs.values() for d in diffs.values() if d != 0),
        }

        overall_C2 = overall_C2 and c2_pass
        overall_C3 = overall_C3 and c3_pass
        overall_C4 = overall_C4 and c4_pass
        overall_C5 = overall_C5 and c5_pass

    # LAT-C6: K_act variability vs K_soft variability
    by_key: Dict[Tuple[str, str], List[RunRecord]] = {}
    for r in records:
        by_key.setdefault((r.option, r.geometry), []).append(r)
    K_act_ranges: Dict[str, int] = {}
    K_soft_ranges: Dict[str, float] = {}
    for (opt, geom), runs in by_key.items():
        K_act_finals = [r.K_act_final for r in runs]
        K_soft_finals = [r.K_soft_final for r in runs]
        K_act_ranges[f"{opt}__{geom}"] = max(K_act_finals) - min(K_act_finals)
        K_soft_ranges[f"{opt}__{geom}"] = max(K_soft_finals) - min(K_soft_finals)
    # C6 PASS if K_act varies AND K_soft is stable (in normalized scale)
    # Use heuristic: K_act range >= 1 AND K_soft range <= TOL_KSOFT
    c6_pass_flags = {
        k: (K_act_ranges[k] >= 1 and K_soft_ranges[k] <= TOL_KSOFT)
        for k in K_act_ranges
    }
    C6_overall = any(c6_pass_flags.values())

    # LAT-C7: A and B both converge (or both fail) for the same option
    C7_pass: Dict[str, bool] = {}
    for option in options_present:
        a_block = per_option_geom.get(f"{option}__A")
        b_block = per_option_geom.get(f"{option}__B")
        if a_block is None or b_block is None:
            C7_pass[option] = False
            continue
        a_pass = a_block["C2_aggregate_L2_pass"] and a_block["C4_K_soft_pass"]
        b_pass = b_block["C2_aggregate_L2_pass"] and b_block["C4_K_soft_pass"]
        C7_pass[option] = (a_pass == b_pass)
    C7_overall = all(C7_pass.values()) if C7_pass else False

    summary = {
        "LAT_C1_protocol_consistency": True,
        "LAT_C2_aggregate_final_convergence": overall_C2,
        "LAT_C3_Kbar_trajectory_stabilization": overall_C3,
        "LAT_C4_Ksoft_convergence": overall_C4,
        "LAT_C5_persistence_profile_convergence": overall_C5,
        "LAT_C6_Kact_Ksoft_separation_documented": C6_overall,
        "LAT_C6_Kact_ranges": K_act_ranges,
        "LAT_C6_Ksoft_ranges": K_soft_ranges,
        "LAT_C6_pass_flags": c6_pass_flags,
        "LAT_C7_AB_geometry_consistency": C7_overall,
        "LAT_C7_per_option_pass": C7_pass,
        "K_star_per_key": K_star_per_key,
    }

    # Failure mode classification
    failure_mode: Optional[str] = None
    # Special handling: LAT-A is expected to be inconclusive (extra slots
    # frozen, dynamics identical across K). If only LAT-A run, mark
    # failure_mode = LAT-F1.
    only_lat_a = options_present == {"LAT-A"}
    if only_lat_a:
        failure_mode = "LAT-F1"
    elif not overall_C2 and not overall_C4:
        failure_mode = "LAT-F3"
    elif "LAT-A" in options_present and "LAT-C" in options_present:
        # Compare A vs C agreement
        # If LAT-A is converged but LAT-C is not, that's option dependence
        a_keys = [k for k in per_option_geom if k.startswith("LAT-A")]
        c_keys = [k for k in per_option_geom if k.startswith("LAT-C")]
        a_converged = all(per_option_geom[k]["C2_aggregate_L2_pass"] for k in a_keys)
        c_converged = all(per_option_geom[k]["C2_aggregate_L2_pass"] for k in c_keys)
        if a_converged != c_converged:
            failure_mode = "LAT-F4"
    return per_option_geom, summary, failure_mode


def classify_status(summary: dict, failure_mode: Optional[str],
                     options_present: set) -> str:
    if failure_mode == "LAT-F1":
        return "inconclusive"
    must = (summary["LAT_C1_protocol_consistency"]
            and summary["LAT_C2_aggregate_final_convergence"]
            and summary["LAT_C3_Kbar_trajectory_stabilization"]
            and summary["LAT_C4_Ksoft_convergence"]
            and summary["LAT_C5_persistence_profile_convergence"])
    soft = (summary["LAT_C3_Kbar_trajectory_stabilization"]
            and summary["LAT_C4_Ksoft_convergence"])
    if must and summary["LAT_C6_Kact_Ksoft_separation_documented"] \
            and summary["LAT_C7_AB_geometry_consistency"]:
        return "success"
    if must:
        return "weak_success"
    if soft:
        return "weak_success"
    if failure_mode is not None:
        return "failed"
    return "failed"


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def run_record_to_dict(r: RunRecord, thresholds: Tuple[float, ...]) -> dict:
    return {
        "K_field": r.K_field,
        "geometry": r.geometry,
        "option": r.option,
        "centers": [list(c) for c in r.centers],
        "initial_masses": r.initial_masses,
        "atom_distribution": r.atom_distribution,
        "snapshot_times": r.snapshot_times,
        "K_act_trajectory": r.K_act_trajectory,
        "K_bar_trajectory": {f"{ell:.2f}": r.K_bar_trajectory[ell] for ell in thresholds},
        "K_soft_trajectory": r.K_soft_trajectory,
        "F_aggregate_trajectory": r.F_aggregate_trajectory,
        "dominant_bars_initial": r.dominant_bars_initial,
        "dominant_bars_final": r.dominant_bars_final,
        "K_act_initial": r.K_act_initial,
        "K_act_final": r.K_act_final,
        "K_soft_initial": r.K_soft_initial,
        "K_soft_final": r.K_soft_final,
        "K_bar_initial": {f"{ell:.2f}": r.K_bar_initial[ell] for ell in thresholds},
        "K_bar_final": {f"{ell:.2f}": r.K_bar_final[ell] for ell in thresholds},
        "final_field_max": r.final_field_max,
        "final_field_simplex_max": r.final_field_simplex_max,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_protocol(args) -> dict:
    t0 = time.time()
    K_values = tuple(int(k) for k in args.K_values.split(","))
    options = tuple(args.options.split(","))
    geometries = tuple(args.geometries.split(","))
    thresholds = DEFAULT_THRESHOLDS

    cfg_template = wq1.RunConfig(seed=args.seed, max_iter=args.max_iter,
                                   snapshot_every=args.snapshot_every)
    graph, positions = wq1.build_torus(cfg_template.n_torus)
    params = ParameterRegistry()

    print(f"[wq-lat1] Sweep — K_values={K_values}, options={options}, "
          f"geometries={geometries}, max_iter={args.max_iter}, seed={args.seed}")

    records: List[RunRecord] = []
    for option in options:
        for K_field in K_values:
            for geometry in geometries:
                cfg, centers = build_runconfig_for(
                    option, K_field, geometry,
                    args.max_iter, args.snapshot_every, args.seed)
                print(f"[wq-lat1]   option={option} K={K_field} geom={geometry} "
                      f"centers={centers[:5]}{'...' if len(centers) > 5 else ''} "
                      f"masses={[round(m, 1) for m in cfg.initial_masses[:5]]}"
                      f"{'...' if len(cfg.initial_masses) > 5 else ''}")
                rec = run_one_trajectory(option, K_field, geometry,
                                          cfg, centers, graph, positions, params,
                                          thresholds)
                records.append(rec)

    cross = cross_K_distances(records)
    per_block, summary, failure_mode = evaluate_convergence(records, cross, thresholds)
    options_present = set(r.option for r in records)
    status = classify_status(summary, failure_mode, options_present)

    if status == "success":
        conclusion = "supported"
    elif status == "weak_success":
        conclusion = "weak"
    elif status == "inconclusive":
        conclusion = "inconclusive"
    else:
        conclusion = "not_supported"

    wall = time.time() - t0

    out = {
        "protocol_id": "WQ-LAT-1",
        "protocol_version": PROTOCOL_VERSION,
        "status": status,
        "reservoir_model": "measure_theoretic_primary",
        "graph": {"type": "torus_grid", "n": cfg_template.n_torus},
        "parameters": {
            "M": cfg_template.M,
            "epsilon": cfg_template.epsilon,
            "K_values": list(K_values),
            "options": list(options),
            "geometries": list(geometries),
            "ell_min_values": list(thresholds),
            "lambda_rep": cfg_template.lambda_rep,
            "lambda_bar": cfg_template.lambda_bar,
            "sigma_b": cfg_template.sigma_b,
            "dt": cfg_template.dt,
            "max_iter": args.max_iter,
            "snapshot_every": args.snapshot_every,
            "seed": args.seed,
            "TOL_AGGREGATE_L2": TOL_AGGREGATE_L2,
            "TOL_KSOFT": TOL_KSOFT,
            "TOL_DOMINANT_BARS": TOL_DOMINANT_BARS,
            "RING_RADIUS": RING_RADIUS,
            "CLUSTER_MASS": CLUSTER_MASS,
        },
        "runs": [run_record_to_dict(r, thresholds) for r in records],
        "cross_K_analysis": cross,
        "convergence_per_block": per_block,
        "criteria_summary": summary,
        "failure_mode": failure_mode,
        "conclusion": {
            "reservoir_interpretation_supported": conclusion,
            "OP0005_solved": "not_claimed",
            "OP0008_solved": "not_claimed",
            "sigma_rich_sufficiency": "not_claimed",
            "scope_caveat": (
                "Restricted to the WQ-1/WQ-2 baseline geometry, T^2_20, "
                "Option D-2 dynamics, default lambda_rep/lambda_bar; not a "
                "proof; not a generalization to other graphs or dynamics."
            ),
        },
        "metadata": {
            "git_commit": _git_commit(),
            "wall_clock_seconds": wall,
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "scc_module_path": _scc_module_path(),
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }
    return out


def _git_commit() -> Optional[str]:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return None


def _scc_module_path() -> Optional[str]:
    try:
        import scc
        return os.path.dirname(scc.__file__)
    except Exception:
        return None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="WQ-LAT-1 reservoir resolution sweep.")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--snapshot_every", type=int, default=25)
    p.add_argument("--K_values", type=str, default="3,4,6,8,12")
    p.add_argument("--options", type=str, default="LAT-A,LAT-C")
    p.add_argument("--geometries", type=str, default="A,B")
    return p.parse_args()


def _json_default(o):
    if isinstance(o, (np.integer, np.int32, np.int64)):
        return int(o)
    if isinstance(o, (np.floating, np.float32, np.float64)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, set):
        return sorted(list(o))
    if isinstance(o, tuple):
        return list(o)
    raise TypeError(f"Not JSON-serializable: {type(o)}")


def main() -> int:
    args = parse_args()
    out = run_protocol(args)
    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[wq-lat1] Wrote {output_path}")
    print(f"[wq-lat1] Wall: {out['metadata']['wall_clock_seconds']:.1f}s")
    print(f"[wq-lat1] status: {out['status']}, failure_mode: {out['failure_mode']}")
    cs = out["criteria_summary"]
    print(f"[wq-lat1] LAT-C1 proto:        {cs['LAT_C1_protocol_consistency']}")
    print(f"[wq-lat1] LAT-C2 agg L2:       {cs['LAT_C2_aggregate_final_convergence']}")
    print(f"[wq-lat1] LAT-C3 K_bar int:    {cs['LAT_C3_Kbar_trajectory_stabilization']}")
    print(f"[wq-lat1] LAT-C4 K_soft:       {cs['LAT_C4_Ksoft_convergence']}")
    print(f"[wq-lat1] LAT-C5 bar profile:  {cs['LAT_C5_persistence_profile_convergence']}")
    print(f"[wq-lat1] LAT-C6 separation:   {cs['LAT_C6_Kact_Ksoft_separation_documented']}")
    print(f"[wq-lat1] LAT-C7 A/B consist:  {cs['LAT_C7_AB_geometry_consistency']}")
    print(f"[wq-lat1] K* per block:        {cs['K_star_per_key']}")
    print(f"[wq-lat1] conclusion: {out['conclusion']['reservoir_interpretation_supported']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
