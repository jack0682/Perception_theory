"""WQ-LAT-1.B — Phi-envelope refinement post-processing for WQ-LAT-1.

The WQ-LAT-1 result showed that the default phi-saturating envelope
phi(ell) = ell / (ell + ell_min) accumulates sub-resolution bars under
split-bump refinement, causing K_soft to grow with K_field. This script
evaluates alternative phi-envelopes against the same persistence data to
identify which (if any) achieve chart-invariance under reservoir
refinement.

Approach:
  1. Re-run the 20 deterministic WQ-LAT-1 trajectories (seed=42, identical
     params; bit-for-bit reproducible) to recover the full final-snapshot
     H_0 superlevel barcodes (the original JSON saved only top 8).
  2. For each candidate phi-envelope (Phi-0 default through Phi-6 various)
     and each ell_min in {0.05, 0.10, 0.15, 0.20}, compute K_soft^phi at
     the final snapshot of every (K, option, geometry) trajectory.
  3. Compute metrics M1-M7 across K for each (phi, ell_min, option, geometry).
  4. Rank candidates against success criteria LAT1B-C1..C6.

Output: CODE/scripts/results/wq_lat1b_phi_envelope_refinement.json with all
metrics, plus a concise summary table.

This script does NOT modify any existing file. It REUSES torus building,
trajectory running, and barcode extraction from prior scripts.

Conclusion is restricted to:
  - the WQ-1/WQ-2/WQ-LAT-1 baseline configuration (T^2_20, K_field
    sweep, M=90, equilateral A vs compressed B, lambda_rep=10);
  - the final-snapshot bar profile under Option D-2 dynamics;
  - the candidate phi-envelopes evaluated.

NO claim about reservoir framework canonicality, OP-0005, OP-0008, sigma_rich
sufficiency, or generalization to other graphs / dynamics.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/wq_lat1b_phi_envelope_refinement.py \\
        --output CODE/scripts/results/wq_lat1b_phi_envelope_refinement.json \\
        --max_iter 5000 --seed 42
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
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.params import ParameterRegistry

import nq242c_counterexample as wq1
import ksoft_kact_diagnostics as wq2
import wq_lat1_reservoir_resolution_sweep as wqlat1


PROTOCOL_VERSION = "1.0"
DEFAULT_K_VALUES = (3, 4, 6, 8, 12)
DEFAULT_THRESHOLDS = (0.05, 0.10, 0.15, 0.20)
DEFAULT_OPTIONS = ("LAT-A", "LAT-C")
DEFAULT_GEOMETRIES = ("A", "B")

RANGE_TOLERANCE = 0.10  # LAT1B-C2: max - min K_soft^phi across K
TARGET_VALUE_TOLERANCE = 0.20  # LAT1B-C3: closeness to K_bar reference


# ---------------------------------------------------------------------------
# Phi-envelope catalog
# ---------------------------------------------------------------------------


def phi_default_sat(ell: float, ell_min: float) -> float:
    """Phi-0: default saturating envelope ell / (ell + ell_min)."""
    return ell / (ell + ell_min) if ell > 0 else 0.0


def phi_hard(ell: float, ell_min: float) -> float:
    """Phi-1: hard threshold."""
    return 1.0 if ell >= ell_min else 0.0


def phi_shift_lin(ell: float, ell_min: float) -> float:
    """Phi-2: shifted linear envelope max(0, (ell-ell_min)/(1-ell_min))."""
    if ell <= ell_min or ell_min >= 1.0:
        return 0.0
    return min(1.0, (ell - ell_min) / (1.0 - ell_min))


def make_phi_shift_sat(beta: float) -> Callable[[float, float], float]:
    """Phi-3: shifted saturating envelope 1 - exp(-beta * max(0, ell-ell_min))."""
    def fn(ell: float, ell_min: float) -> float:
        d = max(0.0, ell - ell_min)
        return 1.0 - math.exp(-beta * d)
    return fn


def make_phi_logistic(s: float) -> Callable[[float, float], float]:
    """Phi-4: logistic soft threshold, normalized to phi(0) = 0 and unbounded."""
    def fn(ell: float, ell_min: float) -> float:
        # Logistic centered at ell_min, slope s
        sigma = 1.0 / (1.0 + math.exp(-s * (ell - ell_min)))
        # Subtract the value at ell=0 so phi(0) = 0
        sigma_at_zero = 1.0 / (1.0 + math.exp(s * ell_min))
        # Clamp non-negative
        return max(0.0, sigma - sigma_at_zero)
    return fn


PHI_CATALOG: Dict[str, Callable[[float, float], float]] = {
    "Phi-0_default_sat": phi_default_sat,
    "Phi-1_hard": phi_hard,
    "Phi-2_shift_lin": phi_shift_lin,
    "Phi-3a_shift_sat_b2": make_phi_shift_sat(2.0),
    "Phi-3b_shift_sat_b5": make_phi_shift_sat(5.0),
    "Phi-3c_shift_sat_b10": make_phi_shift_sat(10.0),
    "Phi-3d_shift_sat_b20": make_phi_shift_sat(20.0),
    "Phi-4a_logistic_s20": make_phi_logistic(20.0),
    "Phi-4b_logistic_s50": make_phi_logistic(50.0),
    "Phi-4c_logistic_s100": make_phi_logistic(100.0),
}


def compute_k_soft(barcode_lengths: List[float], phi_fn: Callable[[float, float], float],
                    ell_min: float) -> float:
    return float(sum(phi_fn(ell, ell_min) for ell in barcode_lengths if ell > 0))


def compute_k_soft_topr(barcode_lengths: List[float], r: int,
                         ell_min: float, phi_fn: Callable[[float, float], float]) -> float:
    """Phi-5: top-r truncated."""
    sorted_ells = sorted([e for e in barcode_lengths if e > 0], reverse=True)[:r]
    return float(sum(phi_fn(e, ell_min) for e in sorted_ells))


def compute_k_soft_normalized(barcode_lengths: List[float],
                                ell_min: float, phi_fn: Callable[[float, float], float],
                                norm: str) -> float:
    """Phi-6: normalized envelope.
    norm in {'count', 'totalpers', 'topr_pers'}."""
    positives = [e for e in barcode_lengths if e > 0]
    if not positives:
        return 0.0
    raw = sum(phi_fn(e, ell_min) for e in positives)
    if norm == "count":
        denom = len(positives)
    elif norm == "totalpers":
        denom = sum(positives)
    elif norm == "topr_pers":
        topr = sorted(positives, reverse=True)[:6]
        denom = sum(topr)
    else:
        raise ValueError(f"Unknown norm: {norm}")
    return raw / denom if denom > 0 else 0.0


# ---------------------------------------------------------------------------
# Trajectory rerun (deterministic; reuses WQ-LAT-1 infrastructure)
# ---------------------------------------------------------------------------


def rerun_and_get_final_barcode(
    option: str, K_field: int, geometry: str,
    max_iter: int, snapshot_every: int, seed: int,
    graph, positions, params: ParameterRegistry,
) -> Tuple[List[float], int, dict]:
    """Re-run a single trajectory and return:
       - full final-snapshot barcode lengths,
       - K_act final,
       - meta dict with K_bar (all thresholds) and aggregate L_inf max."""
    cfg, centers = wqlat1.build_runconfig_for(
        option, K_field, geometry, max_iter, snapshot_every, seed)
    rng = np.random.RandomState(cfg.seed)
    name = f"{option}__K={K_field}__{geometry}"
    traj = wq1.run_trajectory(cfg, name, centers, graph, positions, params, rng)
    final_snap = traj.snapshots[-1]
    U_final = np.sum(final_snap.fields, axis=0)
    barcode = wq2.h0_barcode(U_final, graph)
    bar_lengths = [b - d for (b, d) in barcode]
    bar_lengths_positive = [e for e in bar_lengths if e > 1e-9]

    K_bar_at_thresholds = {
        f"{ell:.2f}": int(sum(1 for e in bar_lengths if e >= ell))
        for ell in DEFAULT_THRESHOLDS
    }
    F_aggregate = wq2.f_count(U_final, graph)
    meta = {
        "K_field": K_field,
        "option": option,
        "geometry": geometry,
        "K_act_final": final_snap.K_act,
        "K_bar_final": K_bar_at_thresholds,
        "F_aggregate_final": F_aggregate,
        "n_positive_bars": len(bar_lengths_positive),
        "max_bar": float(max(bar_lengths_positive)) if bar_lengths_positive else 0.0,
        "median_bar": (float(sorted(bar_lengths_positive)[len(bar_lengths_positive)//2])
                       if bar_lengths_positive else 0.0),
        "min_bar": float(min(bar_lengths_positive)) if bar_lengths_positive else 0.0,
        "tau_final": final_snap.tau,
    }
    return bar_lengths_positive, final_snap.K_act, meta


# ---------------------------------------------------------------------------
# Per-envelope evaluation
# ---------------------------------------------------------------------------


def evaluate_envelope(
    bars_per_run: Dict[Tuple[str, int, str], List[float]],
    phi_name: str, phi_fn: Callable[[float, float], float],
    ell_min: float,
) -> Dict[str, dict]:
    """For a single phi at a single ell_min, compute K_soft per (option, K, geom)
    and aggregate metrics per (option, geom) across K."""
    by_option_geom: Dict[Tuple[str, str], Dict[int, float]] = {}
    for (option, K_field, geometry), bars in bars_per_run.items():
        ksoft = compute_k_soft(bars, phi_fn, ell_min)
        by_option_geom.setdefault((option, geometry), {})[K_field] = ksoft
    out: Dict[str, dict] = {}
    for (option, geometry), per_K in by_option_geom.items():
        Ks = sorted(per_K.keys())
        vals = [per_K[K] for K in Ks]
        if vals:
            mean = float(np.mean(vals))
            std = float(np.std(vals))
            rng = float(max(vals) - min(vals))
            cv = std / mean if abs(mean) > 1e-12 else float("inf")
            # Monotonic drift: Spearman-like check
            sorted_idx = sorted(range(len(Ks)), key=lambda i: Ks[i])
            sorted_vals = [vals[i] for i in sorted_idx]
            monotonic_inc = all(sorted_vals[i+1] >= sorted_vals[i] - 1e-9
                                  for i in range(len(sorted_vals)-1))
            monotonic_dec = all(sorted_vals[i+1] <= sorted_vals[i] + 1e-9
                                  for i in range(len(sorted_vals)-1))
        else:
            mean = std = rng = 0.0
            cv = 0.0
            monotonic_inc = monotonic_dec = False
        out[f"{option}__{geometry}"] = {
            "values_per_K": {str(K): per_K[K] for K in Ks},
            "K_values": Ks,
            "mean": mean, "std": std, "range": rng, "CV": cv,
            "monotonic_increasing": monotonic_inc,
            "monotonic_decreasing": monotonic_dec,
        }
    return out


def evaluate_topr(
    bars_per_run: Dict[Tuple[str, int, str], List[float]],
    r: int, ell_min: float,
) -> Dict[str, dict]:
    """Phi-5 top-r truncated default-sat envelope."""
    by_option_geom: Dict[Tuple[str, str], Dict[int, float]] = {}
    for (option, K_field, geometry), bars in bars_per_run.items():
        ksoft = compute_k_soft_topr(bars, r, ell_min, phi_default_sat)
        by_option_geom.setdefault((option, geometry), {})[K_field] = ksoft
    out: Dict[str, dict] = {}
    for (option, geometry), per_K in by_option_geom.items():
        Ks = sorted(per_K.keys())
        vals = [per_K[K] for K in Ks]
        if vals:
            mean = float(np.mean(vals))
            std = float(np.std(vals))
            rng = float(max(vals) - min(vals))
            cv = std / mean if abs(mean) > 1e-12 else float("inf")
            monotonic_inc = all(vals[i+1] >= vals[i] - 1e-9
                                 for i in range(len(vals)-1))
            monotonic_dec = all(vals[i+1] <= vals[i] + 1e-9
                                 for i in range(len(vals)-1))
        else:
            mean = std = rng = 0.0; cv = 0.0
            monotonic_inc = monotonic_dec = False
        out[f"{option}__{geometry}"] = {
            "values_per_K": {str(K): per_K[K] for K in Ks},
            "K_values": Ks,
            "mean": mean, "std": std, "range": rng, "CV": cv,
            "monotonic_increasing": monotonic_inc,
            "monotonic_decreasing": monotonic_dec,
        }
    return out


def evaluate_normalized(
    bars_per_run: Dict[Tuple[str, int, str], List[float]],
    norm: str, ell_min: float,
) -> Dict[str, dict]:
    """Phi-6 normalized envelope."""
    by_option_geom: Dict[Tuple[str, str], Dict[int, float]] = {}
    for (option, K_field, geometry), bars in bars_per_run.items():
        ksoft = compute_k_soft_normalized(bars, ell_min, phi_default_sat, norm)
        by_option_geom.setdefault((option, geometry), {})[K_field] = ksoft
    out: Dict[str, dict] = {}
    for (option, geometry), per_K in by_option_geom.items():
        Ks = sorted(per_K.keys())
        vals = [per_K[K] for K in Ks]
        if vals:
            mean = float(np.mean(vals))
            std = float(np.std(vals))
            rng = float(max(vals) - min(vals))
            cv = std / mean if abs(mean) > 1e-12 else float("inf")
            monotonic_inc = all(vals[i+1] >= vals[i] - 1e-9
                                 for i in range(len(vals)-1))
            monotonic_dec = all(vals[i+1] <= vals[i] + 1e-9
                                 for i in range(len(vals)-1))
        else:
            mean = std = rng = 0.0; cv = 0.0
            monotonic_inc = monotonic_dec = False
        out[f"{option}__{geometry}"] = {
            "values_per_K": {str(K): per_K[K] for K in Ks},
            "K_values": Ks,
            "mean": mean, "std": std, "range": rng, "CV": cv,
            "monotonic_increasing": monotonic_inc,
            "monotonic_decreasing": monotonic_dec,
        }
    return out


# ---------------------------------------------------------------------------
# Ranking
# ---------------------------------------------------------------------------


def rank_candidates(envelope_results: Dict[str, Dict[str, Dict[str, dict]]],
                     range_tolerance: float) -> List[dict]:
    """Rank candidates by max-range across (option, geometry) pairs at default
    ell_min = 0.10. Smaller is better.

    envelope_results format:
      envelope_results[envelope_name][f"{ell_min:.2f}"][option__geom] = {range, CV, ...}
    """
    rankings: List[dict] = []
    target_ell = "0.10"
    for env_name, per_ell in envelope_results.items():
        ell_block = per_ell.get(target_ell)
        if ell_block is None:
            continue
        max_range_LAT_C = max(
            (b["range"] for k, b in ell_block.items() if k.startswith("LAT-C__")),
            default=0.0)
        max_range_LAT_A = max(
            (b["range"] for k, b in ell_block.items() if k.startswith("LAT-A__")),
            default=0.0)
        # Mean K_soft on LAT-C (across K, A and B)
        lat_c_means = []
        for k, b in ell_block.items():
            if k.startswith("LAT-C__"):
                lat_c_means.append(b["mean"])
        mean_LAT_C = float(np.mean(lat_c_means)) if lat_c_means else 0.0
        rankings.append({
            "envelope": env_name,
            "max_range_LAT_C_K3to12": max_range_LAT_C,
            "max_range_LAT_A": max_range_LAT_A,
            "mean_LAT_C_value": mean_LAT_C,
            "passes_LAT1B_C2": max_range_LAT_C <= range_tolerance,
        })
    rankings.sort(key=lambda d: d["max_range_LAT_C_K3to12"])
    return rankings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description="WQ-LAT-1.B phi-envelope refinement.")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--snapshot_every", type=int, default=25)
    args = p.parse_args()

    t0 = time.time()
    cfg_template = wq1.RunConfig(seed=args.seed, max_iter=args.max_iter,
                                   snapshot_every=args.snapshot_every)
    graph, positions = wq1.build_torus(cfg_template.n_torus)
    params = ParameterRegistry()

    print(f"[wq-lat1b] Re-run for full final-snapshot barcodes; "
          f"seed={args.seed}, max_iter={args.max_iter}")

    # Step 1: rerun and collect full barcodes
    bars_per_run: Dict[Tuple[str, int, str], List[float]] = {}
    metas: List[dict] = []
    for option in DEFAULT_OPTIONS:
        for K_field in DEFAULT_K_VALUES:
            for geometry in DEFAULT_GEOMETRIES:
                print(f"[wq-lat1b]   option={option} K={K_field} geom={geometry}")
                bars, K_act, meta = rerun_and_get_final_barcode(
                    option, K_field, geometry,
                    args.max_iter, args.snapshot_every, args.seed,
                    graph, positions, params)
                bars_per_run[(option, K_field, geometry)] = bars
                metas.append(meta)

    # Step 2: evaluate envelopes Phi-0..Phi-4 across all ell_min values
    envelope_results: Dict[str, Dict[str, Dict[str, dict]]] = {}
    for env_name, phi_fn in PHI_CATALOG.items():
        envelope_results[env_name] = {}
        for ell_min in DEFAULT_THRESHOLDS:
            envelope_results[env_name][f"{ell_min:.2f}"] = evaluate_envelope(
                bars_per_run, env_name, phi_fn, ell_min)

    # Step 3: evaluate Phi-5 (top-r truncated default-sat) at default ell_min=0.10
    topr_results: Dict[str, Dict[str, Dict[str, dict]]] = {}
    for r in [1, 2, 3, 4, 6]:
        env_name = f"Phi-5_topr={r}"
        topr_results[env_name] = {}
        for ell_min in DEFAULT_THRESHOLDS:
            topr_results[env_name][f"{ell_min:.2f}"] = evaluate_topr(
                bars_per_run, r, ell_min)
    envelope_results.update(topr_results)

    # Step 4: evaluate Phi-6 normalized envelopes
    norm_results: Dict[str, Dict[str, Dict[str, dict]]] = {}
    for norm in ["count", "totalpers", "topr_pers"]:
        env_name = f"Phi-6_norm_{norm}"
        norm_results[env_name] = {}
        for ell_min in DEFAULT_THRESHOLDS:
            norm_results[env_name][f"{ell_min:.2f}"] = evaluate_normalized(
                bars_per_run, norm, ell_min)
    envelope_results.update(norm_results)

    # Step 5: rank candidates at ell_min=0.10
    rankings = rank_candidates(envelope_results, RANGE_TOLERANCE)

    # Step 6: identify best-performing candidates
    best_passing = [r for r in rankings if r["passes_LAT1B_C2"]]
    overall_best = rankings[0] if rankings else None

    # Step 7: criteria evaluation
    LAT1B_C1 = False  # Default phi reproduces drift on LAT-C
    default_phi_block = envelope_results["Phi-0_default_sat"]["0.10"]
    lat_c_default_ranges = [
        b["range"] for k, b in default_phi_block.items() if k.startswith("LAT-C__")]
    if lat_c_default_ranges and max(lat_c_default_ranges) > RANGE_TOLERANCE:
        LAT1B_C1 = True

    LAT1B_C2 = len(best_passing) > 0
    # LAT1B-C3: best candidate's mean is close to K_bar(0.10) reference (= 1)
    # for LAT-C
    LAT1B_C3 = False
    if best_passing:
        # Pick the smooth (non-hard) best candidate if any; else hard
        smooth_passing = [r for r in best_passing
                           if not r["envelope"].startswith("Phi-1")]
        candidate = smooth_passing[0] if smooth_passing else best_passing[0]
        LAT1B_C3 = abs(candidate["mean_LAT_C_value"] - 1.0) <= TARGET_VALUE_TOLERANCE

    # LAT1B-C4: candidate is robust across A/B
    LAT1B_C4 = False
    if best_passing:
        cand_name = best_passing[0]["envelope"]
        block = envelope_results[cand_name]["0.10"]
        a_range = block.get("LAT-C__A", {}).get("range", 0.0)
        b_range = block.get("LAT-C__B", {}).get("range", 0.0)
        LAT1B_C4 = (a_range <= RANGE_TOLERANCE) and (b_range <= RANGE_TOLERANCE)

    # LAT1B-C5: candidate's behavior across thresholds
    LAT1B_C5 = False
    if best_passing:
        cand_name = best_passing[0]["envelope"]
        passing_at_thresholds = []
        for ell_str, block in envelope_results[cand_name].items():
            lat_c_max = max(
                (b["range"] for k, b in block.items() if k.startswith("LAT-C__")),
                default=0.0)
            if lat_c_max <= RANGE_TOLERANCE:
                passing_at_thresholds.append(ell_str)
        LAT1B_C5 = len(passing_at_thresholds) >= 2

    # LAT1B-C6: theoretically interpretable — by construction (we chose
    # interpretable forms). Candidates are: hard, shifted-linear,
    # shifted-saturating, logistic, top-r, normalized — all interpretable.
    LAT1B_C6 = LAT1B_C2  # if any passes, it's interpretable by construction

    # Status
    if LAT1B_C1 and LAT1B_C2 and LAT1B_C3 and LAT1B_C4 and LAT1B_C5 and LAT1B_C6:
        status = "success"
    elif LAT1B_C1 and LAT1B_C2 and LAT1B_C4 and LAT1B_C6:
        status = "weak_success"
    elif LAT1B_C1 and not LAT1B_C2:
        status = "failed"  # No phi suppresses drift
    else:
        status = "inconclusive"

    failure_mode: Optional[str] = None
    if not LAT1B_C2:
        # Check if only hard threshold passes
        hard_pass = any(r["envelope"].startswith("Phi-1") and r["passes_LAT1B_C2"]
                        for r in rankings)
        if hard_pass:
            failure_mode = "LAT1B-F3"
        else:
            failure_mode = "LAT1B-F2"

    wall = time.time() - t0

    out = {
        "protocol_id": "WQ-LAT-1.B",
        "protocol_version": PROTOCOL_VERSION,
        "status": status,
        "failure_mode": failure_mode,
        "graph": {"type": "torus_grid", "n": cfg_template.n_torus},
        "parameters": {
            "M": cfg_template.M,
            "K_values": list(DEFAULT_K_VALUES),
            "options": list(DEFAULT_OPTIONS),
            "geometries": list(DEFAULT_GEOMETRIES),
            "ell_min_values": list(DEFAULT_THRESHOLDS),
            "max_iter": args.max_iter,
            "seed": args.seed,
            "snapshot_every": args.snapshot_every,
            "range_tolerance": RANGE_TOLERANCE,
            "target_value_tolerance": TARGET_VALUE_TOLERANCE,
        },
        "per_run_meta": metas,
        "bars_per_run": {
            f"{opt}__K={K}__{g}": bars
            for (opt, K, g), bars in bars_per_run.items()
        },
        "envelope_results": envelope_results,
        "rankings_at_ell_min_010": rankings,
        "best_passing_candidates": best_passing,
        "overall_best": overall_best,
        "criteria": {
            "LAT1B_C1_baseline_failure_reproduced": LAT1B_C1,
            "LAT1B_C2_some_phi_suppresses_drift": LAT1B_C2,
            "LAT1B_C3_candidate_preserves_dominant_morphology": LAT1B_C3,
            "LAT1B_C4_robust_across_AB_geometry": LAT1B_C4,
            "LAT1B_C5_robust_across_thresholds": LAT1B_C5,
            "LAT1B_C6_theoretically_interpretable": LAT1B_C6,
        },
        "wall_clock_seconds": wall,
        "metadata": {
            "git_commit": _git_commit(),
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }

    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[wq-lat1b] Wrote {output_path}")
    print(f"[wq-lat1b] Wall: {wall:.1f}s")
    print(f"[wq-lat1b] status: {status}, failure_mode: {failure_mode}")
    print(f"[wq-lat1b] Top 5 candidates by max LAT-C range at ell_min=0.10:")
    for r in rankings[:5]:
        print(f"  {r['envelope']:30s}  range={r['max_range_LAT_C_K3to12']:.4f}  "
              f"mean_LAT-C={r['mean_LAT_C_value']:.3f}  "
              f"pass_C2={r['passes_LAT1B_C2']}")
    print(f"[wq-lat1b] Criteria:")
    for k, v in out["criteria"].items():
        print(f"  {k}: {v}")
    return 0


def _git_commit() -> Optional[str]:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return None


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


if __name__ == "__main__":
    sys.exit(main())
