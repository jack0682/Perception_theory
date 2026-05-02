"""WQ-1.C-R2 — Projected Layer-II Aggregate σ Test.

Reanalyzes the WQ-2 Layer II trajectories (multi-field shared-pool flow on
T^2_20 with default WQ-1 parameters) by computing sigma_standard on the
*aggregate* field U(u(t)) = sum_j u^(j)(t) at H_0 superlevel-bar-death
event brackets.

WQ-2.D-1 already established that both A (equilateral) and B (compressed)
trajectories exhibit K_bar^{0.10}(U) : 3 -> 1 transitions under Layer II
multi-field dynamics. This script tests whether sigma_standard on the
aggregate distinguishes A and B at the post-event snapshots while matching
at the pre-event snapshots.

Since CODE/scripts/results/ksoft_kact_diag.json contains only scalar
diagnostics (no per-snapshot u-fields), this script reruns the same
deterministic Layer II trajectories (seed=42) and computes sigma_standard
on aggregate U at event brackets. No existing files are modified.

Status: working diagnostic. Reuses run_trajectory and h0_barcode from
prior scripts. Sigma extraction uses scc/sigma_rich.py::compute_sigma_rich
applied directly to the aggregate single field U (1-d input).

Conclusion is restricted to:
  - the projected FD-Hessian sigma_standard implementation;
  - the specific Layer II configuration (T^2_20, K_field=4, M=90, equilateral
    vs compressed, lambda_rep=10, lambda_bar=100);
  - the aggregate H_0 superlevel bar-death event observed in WQ-2.D-1.

NO claim about multi-formation OP-0008 sigma_standard incompleteness across
labelled K_act-jumps. NO claim about sigma_rich sufficiency. NO claim about
K-Selection.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/wq1c_r2_projected_layerII_aggregate_sigma.py \\
        --output CODE/scripts/results/wq1c_r2_projected_layerII_aggregate_sigma.json \\
        --max_iter 5000 --seed 42
"""
from __future__ import annotations

import argparse
import json
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
from scc.sigma_rich import compute_sigma_rich

import nq242c_counterexample as wq1
import ksoft_kact_diagnostics as wq2


PROTOCOL_VERSION = "1.0"
DEFAULT_THRESHOLDS = (0.05, 0.10, 0.15, 0.20)
DEFAULT_TOLERANCES = (1e-4, 1e-3, 1e-2)


# ---------------------------------------------------------------------------
# Event detection on aggregate U
# ---------------------------------------------------------------------------


def aggregate_at_snapshots(traj: "wq1.TrajectoryResult") -> List[np.ndarray]:
    """Aggregate field U(t) = sum_j u^(j)(t) at each snapshot."""
    return [np.sum(snap.fields, axis=0) for snap in traj.snapshots]


def bar_count_trajectory(
    U_seq: List[np.ndarray],
    graph,
    thresholds: Tuple[float, ...],
) -> Dict[float, List[int]]:
    """Compute K_bar^{ell}(U(t)) for each threshold across the snapshot sequence."""
    out = {ell: [] for ell in thresholds}
    for U in U_seq:
        barcode = wq2.h0_barcode(U, graph)
        ells = wq2.bar_lengths(barcode)
        for ell in thresholds:
            out[ell].append(int(sum(1 for e in ells if e >= ell)))
    return out


def first_bar_death(K_bar_traj: List[int]) -> Optional[Tuple[int, int, int, int]]:
    """Return (idx_pre, idx_post, K_pre, K_post) for the first decrease, or None."""
    for i in range(len(K_bar_traj) - 1):
        if K_bar_traj[i + 1] < K_bar_traj[i]:
            return i, i + 1, K_bar_traj[i], K_bar_traj[i + 1]
    return None


# ---------------------------------------------------------------------------
# Sigma comparison with tolerance sweep
# ---------------------------------------------------------------------------


def sigma_compare(sa: tuple, sb: tuple, tol: float) -> Tuple[bool, float, Optional[int]]:
    """Compare two sigma_standard tuples within tolerance."""
    if sa is None or sb is None:
        return False, float("nan"), None
    if len(sa) != len(sb):
        return False, float("inf"), None
    max_diff = 0.0
    offender: Optional[int] = None
    for k, ((na, _, la), (nb, _, lb)) in enumerate(zip(sa, sb)):
        if na != nb:
            return False, float("inf"), k
        diff = abs(float(la) - float(lb))
        if diff > max_diff:
            max_diff = diff
            offender = k
    equal = max_diff < tol
    return equal, max_diff, (offender if not equal else None)


def evaluate_sigma_brackets(
    sigA_pre, sigA_post, sigB_pre, sigB_post,
    tolerances: Tuple[float, ...],
) -> dict:
    """Tolerance sweep over R2-C2 / R2-C3."""
    out = {}
    for tol in tolerances:
        eq_pre, dmax_pre, off_pre = sigma_compare(sigA_pre, sigB_pre, tol)
        eq_post, dmax_post, off_post = sigma_compare(sigA_post, sigB_post, tol)
        # R2-C2 requires equality with tolerance; R2-C3 requires inequality with margin
        c2 = bool(eq_pre)
        c3 = (not eq_post) and dmax_post > 10.0 * tol
        out[f"{tol:.0e}"] = {
            "tol": tol,
            "C2_pre_equal": c2,
            "C2_max_lambda_diff_pre": dmax_pre,
            "C2_offending_cluster_pre": off_pre,
            "C3_post_distinct": c3,
            "C3_max_lambda_diff_post": dmax_post,
            "C3_offending_cluster_post": off_post,
        }
    return out


# ---------------------------------------------------------------------------
# Per-trajectory pipeline
# ---------------------------------------------------------------------------


def process_trajectory(
    cfg: wq1.RunConfig,
    name: str,
    centers,
    graph,
    positions,
    params: ParameterRegistry,
    rng: np.random.RandomState,
    thresholds: Tuple[float, ...],
    n_stab_post: int,
    n_eig_sigma: int,
) -> dict:
    """Run a Layer II trajectory, compute aggregate diagnostics, extract sigma at brackets."""
    traj = wq1.run_trajectory(cfg, name, centers, graph, positions, params, rng)
    U_seq = aggregate_at_snapshots(traj)
    K_bar = bar_count_trajectory(U_seq, graph, thresholds)
    K_act_traj = [s.K_act for s in traj.snapshots]
    snapshot_times = [s.tau for s in traj.snapshots]

    # First bar-death event per threshold
    events: Dict[str, dict] = {}
    sigma_at_bracket: Dict[int, tuple] = {}
    for ell in thresholds:
        ev = first_bar_death(K_bar[ell])
        if ev is None:
            events[f"{ell:.2f}"] = None
            continue
        idx_pre, idx_post, kp, kc = ev
        idx_post_stab = min(idx_post + n_stab_post, len(U_seq) - 1)
        # Mark snapshots needing sigma extraction
        sigma_at_bracket.setdefault(idx_pre, None)
        sigma_at_bracket.setdefault(idx_post_stab, None)
        events[f"{ell:.2f}"] = {
            "idx_pre": idx_pre, "idx_post": idx_post,
            "idx_post_stab": idx_post_stab,
            "tau_pre": snapshot_times[idx_pre],
            "tau_post": snapshot_times[idx_post],
            "tau_post_stab": snapshot_times[idx_post_stab],
            "K_bar_pre": kp, "K_bar_post": kc,
        }

    # Compute sigma_standard on aggregate U at the bracket snapshots
    for idx in sorted(sigma_at_bracket.keys()):
        sr = compute_sigma_rich(
            u_field=U_seq[idx],
            graph_state=graph,
            params=params,
            positions=positions,
            n_eig=n_eig_sigma,
        )
        sigma_at_bracket[idx] = sr.sigma_standard

    # Attach sigma to event records
    for ell_key, ev in events.items():
        if ev is None:
            continue
        ev["sigma_pre"] = sigma_at_bracket[ev["idx_pre"]]
        ev["sigma_post"] = sigma_at_bracket[ev["idx_post_stab"]]

    return {
        "name": name,
        "centers": [list(c) for c in centers],
        "snapshot_times": snapshot_times,
        "K_act_trajectory": K_act_traj,
        "K_bar_trajectory": {f"{ell:.2f}": K_bar[ell] for ell in thresholds},
        "events": events,
        "dominant_bar_lengths_pre_post": {
            f"{ell:.2f}": (
                {"pre": sorted(wq2.bar_lengths(wq2.h0_barcode(
                    U_seq[ev["idx_pre"]], graph)), reverse=True)[:5],
                 "post": sorted(wq2.bar_lengths(wq2.h0_barcode(
                    U_seq[ev["idx_post_stab"]], graph)), reverse=True)[:5]}
                if ev is not None else None
            )
            for ell, ev in zip(thresholds, events.values())
        },
    }


# ---------------------------------------------------------------------------
# Cross-trajectory criteria evaluation
# ---------------------------------------------------------------------------


def evaluate_criteria(
    traj_A: dict, traj_B: dict,
    thresholds: Tuple[float, ...],
    tolerances: Tuple[float, ...],
) -> Tuple[dict, dict, Optional[str]]:
    """Cross-trajectory R2-C1/C2/C3 evaluation, plus aggregate criteria summary."""
    comparisons: Dict[str, dict] = {}
    any_C1 = False
    pass_per_ell: Dict[float, List[float]] = {}
    for ell in thresholds:
        ell_key = f"{ell:.2f}"
        evA = traj_A["events"][ell_key]
        evB = traj_B["events"][ell_key]
        comp = {
            "ell_min": ell,
            "A_event": evA,
            "B_event": evB,
            "C1_events_both": False,
            "tolerance_sweep": None,
        }
        if evA is None or evB is None:
            comparisons[ell_key] = comp
            continue
        comp["C1_events_both"] = True
        any_C1 = True
        sweep = evaluate_sigma_brackets(
            evA["sigma_pre"], evA["sigma_post"],
            evB["sigma_pre"], evB["sigma_post"],
            tolerances,
        )
        comp["tolerance_sweep"] = sweep
        # Pass at this ell_min iff exists a tolerance with C2 ∧ C3
        passing_tols = [
            tol_val for tol_val, tol_record in sweep.items()
            if tol_record["C2_pre_equal"] and tol_record["C3_post_distinct"]
        ]
        comp["passing_tolerances"] = passing_tols
        if passing_tols:
            pass_per_ell.setdefault(ell, []).extend(passing_tols)
        comparisons[ell_key] = comp

    # Aggregate criteria
    any_C2 = any(
        any(t["C2_pre_equal"] for t in c["tolerance_sweep"].values())
        for c in comparisons.values() if c["tolerance_sweep"]
    )
    any_C3 = any(
        any(t["C3_post_distinct"] for t in c["tolerance_sweep"].values())
        for c in comparisons.values() if c["tolerance_sweep"]
    )
    C5 = len(pass_per_ell) >= 2
    # C6: tolerance robustness — same tolerance passes across multiple ell_min
    tols_passing_globally = set.intersection(*[set(v) for v in pass_per_ell.values()]) \
        if pass_per_ell else set()
    C6 = len(tols_passing_globally) >= 1 if pass_per_ell else False

    summary = {
        "R2_C1_events_both": any_C1,
        "R2_C2_same_pre_sigma": any_C2,
        "R2_C3_different_post_sigma": any_C3,
        "R2_C4_same_projected_protocol": True,
        "R2_C5_threshold_robustness": C5,
        "R2_C5_passing_per_ell": {f"{ell:.2f}": tols
                                   for ell, tols in pass_per_ell.items()},
        "R2_C6_tolerance_robustness": C6,
        "R2_C6_tolerances_passing_globally": sorted(tols_passing_globally),
    }

    # Failure mode
    if not any_C1:
        # Check if WQ-2 said events should exist (3->1 expected)
        failure_mode = "R2-F2"
    elif not any_C2:
        failure_mode = "R2-F3"
    elif not any_C3:
        failure_mode = "R2-F4"
    elif not C5:
        failure_mode = "R2-F6"
    elif not C6:
        failure_mode = "R2-F7"
    else:
        failure_mode = None

    return comparisons, summary, failure_mode


def classify_status(summary: dict) -> str:
    must = (summary["R2_C1_events_both"]
            and summary["R2_C2_same_pre_sigma"]
            and summary["R2_C3_different_post_sigma"]
            and summary["R2_C4_same_projected_protocol"])
    robust = (summary["R2_C5_threshold_robustness"]
              and summary["R2_C6_tolerance_robustness"])
    if must and robust:
        return "success"
    if must:
        return "weak_success"
    return "failed"


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _sigma_to_json(s):
    if s is None:
        return None
    return [list(t) for t in s]


def _strip_sigma(traj: dict) -> dict:
    """Replace sigma tuples with JSON-friendly lists."""
    out = json.loads(json.dumps(traj, default=_json_default_pre))
    return out


def _json_default_pre(o):
    if isinstance(o, tuple):
        return list(o)
    if isinstance(o, (np.integer, np.int32, np.int64)):
        return int(o)
    if isinstance(o, (np.floating, np.float32, np.float64)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Not JSON-serializable: {type(o)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_protocol(args) -> dict:
    t0 = time.time()
    thresholds = DEFAULT_THRESHOLDS
    tolerances = DEFAULT_TOLERANCES
    n_stab_post = 4
    n_eig_sigma = 6

    cfg = wq1.RunConfig(
        seed=args.seed, max_iter=args.max_iter,
        snapshot_every=args.snapshot_every,
    )
    graph, positions = wq1.build_torus(cfg.n_torus)
    params = ParameterRegistry()

    print(f"[wq1c-r2] Layer II rerun, seed={cfg.seed}, max_iter={cfg.max_iter}")
    rng_A = np.random.RandomState(cfg.seed)
    rng_B = np.random.RandomState(cfg.seed)
    print("[wq1c-r2] Trajectory A (equilateral) ...")
    traj_A = process_trajectory(
        cfg, "equilateral_aggregate", list(cfg.centers_A),
        graph, positions, params, rng_A,
        thresholds, n_stab_post, n_eig_sigma,
    )
    print("[wq1c-r2] Trajectory B (compressed) ...")
    traj_B = process_trajectory(
        cfg, "compressed_aggregate", list(cfg.centers_B),
        graph, positions, params, rng_B,
        thresholds, n_stab_post, n_eig_sigma,
    )

    comparisons, summary, failure_mode = evaluate_criteria(
        traj_A, traj_B, thresholds, tolerances)
    status = classify_status(summary)

    if status == "success":
        conclusion_label = "supported"
    elif status == "weak_success":
        conclusion_label = "weak"
    elif failure_mode in ("R2-F2", "R2-F1"):
        conclusion_label = "undetermined"
    elif failure_mode == "R2-F3":
        conclusion_label = "undetermined"
    elif failure_mode == "R2-F4":
        conclusion_label = "not_supported"
    elif failure_mode in ("R2-F6", "R2-F7"):
        conclusion_label = "weak"
    else:
        conclusion_label = "undetermined"

    wall = time.time() - t0
    out = {
        "protocol_id": "WQ-1.C-R2",
        "protocol_version": PROTOCOL_VERSION,
        "status": status,
        "source": "WQ-2 Layer II aggregate projections (rerun)",
        "graph": {"type": "torus_grid", "n": cfg.n_torus},
        "thresholds": list(thresholds),
        "sigma_tolerances": list(tolerances),
        "parameters": {
            "K_field": cfg.K_field, "M": cfg.M,
            "epsilon": cfg.epsilon,
            "lambda_rep": cfg.lambda_rep, "lambda_bar": cfg.lambda_bar,
            "sigma_b": cfg.sigma_b, "dt": cfg.dt,
            "max_iter": cfg.max_iter,
            "snapshot_every": cfg.snapshot_every,
            "seed": cfg.seed,
            "n_eig_sigma": n_eig_sigma,
            "n_stab_post": n_stab_post,
            "centers_A": [list(c) for c in cfg.centers_A],
            "centers_B": [list(c) for c in cfg.centers_B],
        },
        "trajectory_A": _strip_sigma(traj_A),
        "trajectory_B": _strip_sigma(traj_B),
        "comparisons": comparisons,
        "criteria_summary": summary,
        "failure_mode": failure_mode,
        "conclusion": {
            "layerI_projected_aggregate_sigma_incompleteness": conclusion_label,
            "multi_formation_OP0008": "not_claimed",
            "sigma_rich_sufficiency": "not_claimed",
            "scope_caveat": (
                "Restricted to projected FD-Hessian sigma_standard of "
                "scc/sigma_rich.py::_sigma_standard applied to aggregate U(t) "
                "at WQ-2 Layer II bar-death event brackets; not multi-formation "
                "labelled K_act-jump test; not a proof of OP-0008."
            ),
            "notes": [],
        },
        "metadata": {
            "git_commit": _git_commit(),
            "wall_clock_seconds": wall,
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "scipy_version": _scipy_version(),
            "scc_module_path": _scc_module_path(),
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                  time.gmtime()),
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


def _scipy_version() -> Optional[str]:
    try:
        import scipy
        return scipy.__version__
    except ImportError:
        return None


def _scc_module_path() -> Optional[str]:
    try:
        import scc
        return os.path.dirname(scc.__file__)
    except Exception:
        return None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="WQ-1.C-R2 — projected Layer II aggregate sigma test.")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--snapshot_every", type=int, default=25)
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
    print(f"[wq1c-r2] Wrote {output_path}")
    print(f"[wq1c-r2] Wall: {out['metadata']['wall_clock_seconds']:.1f}s")
    cs = out["criteria_summary"]
    print(f"[wq1c-r2] R2-C1 events both:        {cs['R2_C1_events_both']}")
    print(f"[wq1c-r2] R2-C2 same pre sigma:     {cs['R2_C2_same_pre_sigma']}")
    print(f"[wq1c-r2] R2-C3 different post sig: {cs['R2_C3_different_post_sigma']}")
    print(f"[wq1c-r2] R2-C4 same protocol:      {cs['R2_C4_same_projected_protocol']}")
    print(f"[wq1c-r2] R2-C5 thresh robustness:  {cs['R2_C5_threshold_robustness']}")
    print(f"[wq1c-r2] R2-C6 tol robustness:     {cs['R2_C6_tolerance_robustness']}")
    print(f"[wq1c-r2] failure_mode: {out['failure_mode']}")
    print(f"[wq1c-r2] conclusion: {out['conclusion']['layerI_projected_aggregate_sigma_incompleteness']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
