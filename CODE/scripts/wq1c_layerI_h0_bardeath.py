"""WQ-1.C — Layer I H_0 Bar-Death Counterexample Protocol.

Implements the protocol of THEORY/working/MF/wq1c_layerI_h0_bardeath_protocol.md.

Constructs two single-field aggregate trajectories (A-I: equilateral 3-bump,
B-I: compressed 3-bump) on the 20x20 torus, runs them under the canonical
SCC single-field projected gradient flow on Sigma_M(G), detects H_0 bar-death
events at multiple thresholds, computes sigma_standard pre/post each event,
and evaluates C1-C6 criteria.

Three initialization variants:
  V0 = saturated_gaussian (continuity with WQ-1 / WQ-2 aggregate)
  V1 = capped_smooth (avoids u(x) = 1 saturation; tests F-C5 saturation
       artifact)
  V2 = low_mass (M = 45; sensitivity probe)

The script is non-destructive. It writes only to the path supplied via
``--output`` and does not edit any other repository file.

The conclusion is restricted to:
  - the projected FD-Hessian sigma_standard implementation of
    scc/sigma_rich.py::_sigma_standard;
  - the specific graph T^2_20 (4-regular periodic);
  - the constructed A-I / B-I geometric configurations;
  - unlabelled Layer I aggregate topology, NOT labelled K_act jumps.

The script makes NO claim about multi-formation sigma-standard incompleteness
(OP-0008), NO claim about sigma-rich sufficiency, NO claim about K-Selection.
See protocol section 4 for the complete list of forbidden non-claims.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/wq1c_layerI_h0_bardeath.py \\
        --output CODE/scripts/results/wq1c_layerI_h0_bardeath_results.json \\
        --max_iter 5000 --seed 42

Smoke test::

    PYTHONPATH=CODE python3 CODE/scripts/wq1c_layerI_h0_bardeath.py \\
        --output /tmp/wq1c_smoke.json \\
        --max_iter 200 --snapshot_every 25 --skip_v2
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
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume
from scc.sigma_rich import compute_sigma_rich

# Reuse torus + persistence pipeline from prior work
import nq242c_counterexample as wq1
import ksoft_kact_diagnostics as wq2


PROTOCOL_VERSION = "1.0"
DEFAULT_ELL_MIN_SWEEP = (0.05, 0.10, 0.15, 0.20)


# ---------------------------------------------------------------------------
# Configuration dataclasses
# ---------------------------------------------------------------------------


@dataclass
class WQ1CConfig:
    """All knobs of the WQ-1.C protocol."""
    M_default: float = 90.0
    M_low_mass: float = 45.0
    sigma_b: float = 2.0
    u_max_capped: float = 0.7
    dt: float = 1e-3
    max_iter: int = 5000
    snapshot_every: int = 25
    tau_lambda: float = 1e-3
    ell_min_sweep: Tuple[float, ...] = DEFAULT_ELL_MIN_SWEEP
    ell_min_default: float = 0.10
    n_eig_sigma: int = 6
    n_stab_post: int = 4
    seed: int = 42
    n_torus: int = 20
    grad_stagnation_window: int = 50
    grad_stagnation_threshold: float = 1e-5
    centers_A: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 14))
    centers_B: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 11))
    skip_v2: bool = False


# ---------------------------------------------------------------------------
# Initial state construction (single-field aggregate)
# ---------------------------------------------------------------------------


def _aggregate_gaussian(centers, sigma_b, positions, n_torus) -> np.ndarray:
    """Sum of unit-amplitude Gaussian bumps centered at the given centers."""
    u = np.zeros(positions.shape[0], dtype=np.float64)
    for c in centers:
        cv = np.array(c, dtype=np.float64)
        d = wq1.torus_distance(positions, cv, n_torus)
        u += np.exp(-(d ** 2) / (2.0 * sigma_b * sigma_b))
    return u


def _project_to_sigma_M(u: np.ndarray, M: float, u_max: float = 1.0,
                        max_iter: int = 5) -> np.ndarray:
    """Project a non-negative field to {u: sum=M, 0 <= u <= u_max}.
    Iterates clip + linear shift to enforce both constraints."""
    u = np.maximum(u, 0.0)
    for _ in range(max_iter):
        s = float(u.sum())
        if s < 1e-12:
            return u
        u = u * (M / s)
        u = np.minimum(u, u_max)
        u = np.maximum(u, 0.0)
        s_after = float(u.sum())
        if abs(s_after - M) < 1e-3:
            break
        # If clipping reduced mass, redistribute the residual to non-saturated
        # vertices uniformly
        residual = M - s_after
        if residual <= 0:
            # All vertices are at u_max; cannot fit more mass
            break
        capacity_mask = u < u_max - 1e-9
        n_capacity = int(capacity_mask.sum())
        if n_capacity == 0:
            break
        u[capacity_mask] += residual / n_capacity
        u = np.minimum(u, u_max)
    return u


def build_initial_state(
    cfg: WQ1CConfig,
    centers,
    variant: str,
    positions: np.ndarray,
) -> Tuple[np.ndarray, float]:
    """Construct the single-field aggregate u(0) for the given variant.

    Returns (u_field, M_used).
    """
    if variant == "V0_saturated_gaussian":
        M = cfg.M_default
        u_max = 1.0
    elif variant == "V1_capped_smooth":
        M = cfg.M_default
        u_max = cfg.u_max_capped
    elif variant == "V2_low_mass":
        M = cfg.M_low_mass
        u_max = 1.0
    else:
        raise ValueError(f"Unknown variant: {variant}")

    raw = _aggregate_gaussian(centers, cfg.sigma_b, positions, cfg.n_torus)
    # Initial mass scaling
    raw = raw * (M / raw.sum())
    if variant == "V1_capped_smooth":
        u = _project_to_sigma_M(raw, M, u_max=u_max, max_iter=10)
    else:
        u = project_volume(raw, M)
        u = np.clip(u, 0.0, u_max)
        # Re-project after clip to restore mass
        u = project_volume(u, M)
    return u, M


# ---------------------------------------------------------------------------
# Single-field projected gradient flow on Sigma_M(G)
# ---------------------------------------------------------------------------


@dataclass
class SnapshotL1:
    tau: int
    u: np.ndarray
    K_bar: Dict[float, int]  # one per ell_min
    K_soft: float
    bar_lengths: List[float]
    F: int  # number of strict local maxima
    sigma_standard: Optional[tuple] = None  # set lazily at event-bracketing snapshots


@dataclass
class TrajectoryL1:
    name: str
    variant: str
    centers: List[Tuple[int, int]]
    M: float
    snapshots: List[SnapshotL1] = field(default_factory=list)
    # Event records per ell_min: list of (snap_idx_pre, snap_idx_post, K_pre, K_post)
    events: Dict[float, List[Tuple[int, int, int, int]]] = field(default_factory=dict)


def run_single_field_trajectory(
    cfg: WQ1CConfig,
    name: str,
    variant: str,
    centers,
    graph: GraphState,
    positions: np.ndarray,
    params: ParameterRegistry,
) -> TrajectoryL1:
    """Run single-field SCC projected gradient flow with snapshots."""
    u, M = build_initial_state(cfg, centers, variant, positions)
    n = u.shape[0]

    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    traj = TrajectoryL1(
        name=name, variant=variant,
        centers=list(centers), M=M,
    )
    traj.events = {ell: [] for ell in cfg.ell_min_sweep}

    # Snapshot at tau = 0
    traj.snapshots.append(_build_snapshot(0, u, graph, cfg))

    dt = cfg.dt
    grad_norm_history: List[float] = []

    for tau in range(1, cfg.max_iter + 1):
        g = ec.gradient(u)
        g_proj = g - np.mean(g)  # project onto T(Sigma_M)
        gnorm = float(np.linalg.norm(g_proj) / np.sqrt(n))
        u = u - dt * g_proj
        u = project_volume(u, M)
        # No simplex barrier needed at Layer I; box constraint is handled by project_volume.

        grad_norm_history.append(gnorm)

        # Adaptive step size (matches WQ-1 heuristic)
        if tau > 5 and len(grad_norm_history) > 2:
            prev = grad_norm_history[-2]
            if gnorm > prev * 1.5:
                dt = max(dt * 0.7, 1e-8)
            elif gnorm < prev * 0.95:
                dt = min(dt * 1.05, 0.1)

        if tau % cfg.snapshot_every == 0:
            traj.snapshots.append(_build_snapshot(tau, u, graph, cfg))
            # Detect bar-death event at each ell_min
            prev_snap = traj.snapshots[-2]
            curr_snap = traj.snapshots[-1]
            for ell in cfg.ell_min_sweep:
                kp = prev_snap.K_bar[ell]
                kc = curr_snap.K_bar[ell]
                if kc < kp:
                    traj.events[ell].append((
                        len(traj.snapshots) - 2,
                        len(traj.snapshots) - 1,
                        kp, kc,
                    ))

        if (len(grad_norm_history) >= cfg.grad_stagnation_window
                and all(g < cfg.grad_stagnation_threshold
                        for g in grad_norm_history[-cfg.grad_stagnation_window:])):
            break

    return traj


def _build_snapshot(tau: int, u: np.ndarray, graph: GraphState,
                    cfg: WQ1CConfig) -> SnapshotL1:
    barcode = wq2.h0_barcode(u, graph)
    ells = wq2.bar_lengths(barcode)
    K_bar = {ell: int(sum(1 for e in ells if e >= ell))
             for ell in cfg.ell_min_sweep}
    K_soft = wq2.k_soft_phi_sat(barcode, cfg.ell_min_default)
    F = wq2.f_count(u, graph)
    return SnapshotL1(
        tau=tau, u=u.copy(),
        K_bar=K_bar, K_soft=K_soft,
        bar_lengths=sorted(ells, reverse=True)[:8],
        F=F,
    )


# ---------------------------------------------------------------------------
# σ-standard extraction at event-bracketing snapshots
# ---------------------------------------------------------------------------


def attach_sigma_at_events(
    traj: TrajectoryL1,
    cfg: WQ1CConfig,
    graph: GraphState,
    params: ParameterRegistry,
    positions: np.ndarray,
) -> None:
    """Compute sigma_standard at the bracketing snapshots of the first event
    for each ell_min."""
    snapshot_idxs_to_compute = set()
    for ell, events in traj.events.items():
        if not events:
            continue
        pre_idx, post_idx, _, _ = events[0]
        snapshot_idxs_to_compute.add(pre_idx)
        # Post-stabilization snapshot
        target = post_idx + cfg.n_stab_post
        target = min(target, len(traj.snapshots) - 1)
        snapshot_idxs_to_compute.add(target)
    for idx in sorted(snapshot_idxs_to_compute):
        snap = traj.snapshots[idx]
        sr = compute_sigma_rich(
            u_field=snap.u,
            graph_state=graph,
            params=params,
            positions=positions,
            n_eig=cfg.n_eig_sigma,
        )
        snap.sigma_standard = sr.sigma_standard


def post_event_index(traj: TrajectoryL1, ell: float, n_stab: int) -> Optional[int]:
    if not traj.events.get(ell):
        return None
    _, post_idx, _, _ = traj.events[ell][0]
    return min(post_idx + n_stab, len(traj.snapshots) - 1)


# ---------------------------------------------------------------------------
# σ-standard tolerance comparator (reused from WQ-1)
# ---------------------------------------------------------------------------


def sigma_compare(sa: tuple, sb: tuple, tol: float) -> Tuple[bool, float, Optional[int]]:
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


# ---------------------------------------------------------------------------
# Per-comparison evaluation
# ---------------------------------------------------------------------------


def evaluate_comparison(
    traj_A: TrajectoryL1,
    traj_B: TrajectoryL1,
    ell: float,
    cfg: WQ1CConfig,
) -> dict:
    eventsA = traj_A.events.get(ell, [])
    eventsB = traj_B.events.get(ell, [])
    out = {
        "ell_min": ell,
        "variant": traj_A.variant,
        "A_event_idx_pre": None, "A_event_idx_post": None,
        "B_event_idx_pre": None, "B_event_idx_post": None,
        "A_event_time": None, "B_event_time": None,
        "A_K_bar_pre": None, "A_K_bar_post": None,
        "B_K_bar_pre": None, "B_K_bar_post": None,
        "A_sigma_pre": None, "A_sigma_post": None,
        "B_sigma_pre": None, "B_sigma_post": None,
        "C1": False, "C2": False, "C3": False,
        "C2_max_lambda_diff": None, "C2_offending_cluster": None,
        "C3_max_lambda_diff": None, "C3_offending_cluster": None,
    }
    if not eventsA or not eventsB:
        return out
    out["C1"] = True
    pre_idx_A, post_idx_A, kp_A, kc_A = eventsA[0]
    pre_idx_B, post_idx_B, kp_B, kc_B = eventsB[0]
    stab_A = post_event_index(traj_A, ell, cfg.n_stab_post)
    stab_B = post_event_index(traj_B, ell, cfg.n_stab_post)
    out["A_event_idx_pre"] = pre_idx_A
    out["A_event_idx_post"] = stab_A
    out["B_event_idx_pre"] = pre_idx_B
    out["B_event_idx_post"] = stab_B
    out["A_event_time"] = traj_A.snapshots[post_idx_A].tau
    out["B_event_time"] = traj_B.snapshots[post_idx_B].tau
    out["A_K_bar_pre"] = kp_A; out["A_K_bar_post"] = kc_A
    out["B_K_bar_pre"] = kp_B; out["B_K_bar_post"] = kc_B
    sA_pre = traj_A.snapshots[pre_idx_A].sigma_standard
    sA_post = traj_A.snapshots[stab_A].sigma_standard if stab_A is not None else None
    sB_pre = traj_B.snapshots[pre_idx_B].sigma_standard
    sB_post = traj_B.snapshots[stab_B].sigma_standard if stab_B is not None else None
    out["A_sigma_pre"] = sA_pre
    out["A_sigma_post"] = sA_post
    out["B_sigma_pre"] = sB_pre
    out["B_sigma_post"] = sB_post
    eq2, dmax2, off2 = sigma_compare(sA_pre, sB_pre, cfg.tau_lambda)
    out["C2"] = bool(eq2)
    out["C2_max_lambda_diff"] = dmax2
    out["C2_offending_cluster"] = off2
    eq3, dmax3, off3 = sigma_compare(sA_post, sB_post, cfg.tau_lambda)
    # C3 requires INequality with margin
    c3_pass = (not eq3) and (dmax3 > 10.0 * cfg.tau_lambda)
    out["C3"] = bool(c3_pass)
    out["C3_max_lambda_diff"] = dmax3
    out["C3_offending_cluster"] = off3
    return out


# ---------------------------------------------------------------------------
# Aggregate criteria summary
# ---------------------------------------------------------------------------


def aggregate_criteria(comparisons: List[dict]) -> Tuple[dict, Optional[str]]:
    if not comparisons:
        return {
            "C1_bar_death_exists": False,
            "C2_same_pre_sigma": False,
            "C3_different_post_sigma": False,
            "C4_same_protocol": True,
            "C5_threshold_robustness": False,
            "C5_threshold_robustness_notes": ["no comparisons computed"],
            "C6_saturation_robustness": False,
            "C6_saturation_robustness_notes": ["no comparisons computed"],
        }, "F-C1"
    any_C1 = any(c["C1"] for c in comparisons)
    any_C2 = any(c["C2"] for c in comparisons)
    any_C3 = any(c["C3"] for c in comparisons)
    # C5 — multiple ell_min satisfy C2 ∧ C3
    pass_per_ell = {}
    for c in comparisons:
        key = (c["ell_min"], c["variant"])
        if c["C1"] and c["C2"] and c["C3"]:
            pass_per_ell.setdefault(c["variant"], []).append(c["ell_min"])
    C5 = any(len(v) >= 2 for v in pass_per_ell.values())
    C5_notes = [f"variant {k}: ell_min passing = {v}" for k, v in pass_per_ell.items()]
    if not C5_notes:
        C5_notes = ["no (variant, ell_min) combination passes C2 ∧ C3"]
    # C6 — at least one non-saturated variant passes
    non_sat_variants = {"V1_capped_smooth", "V2_low_mass"}
    C6 = any(v in non_sat_variants for v in pass_per_ell.keys())
    C6_notes = [f"passing variants = {sorted(pass_per_ell.keys())}"]
    summary = {
        "C1_bar_death_exists": any_C1,
        "C2_same_pre_sigma": any_C2,
        "C3_different_post_sigma": any_C3,
        "C4_same_protocol": True,
        "C5_threshold_robustness": C5,
        "C5_threshold_robustness_notes": C5_notes,
        "C6_saturation_robustness": C6,
        "C6_saturation_robustness_notes": C6_notes,
    }
    # Failure mode classification
    if not any_C1:
        return summary, "F-C1"
    if not any_C2:
        return summary, "F-C2"
    if not any_C3:
        # Distinguish F-C3 (post-sigma equal) vs F-C6 (sigma can't distinguish at all)
        # Use C3_max_lambda_diff: if any comparison has dmax3 > 10·tau_lambda but
        # cluster sizes/counts differ structurally, that's not pure F-C3.
        # For this script, classify all "C3 failed" as F-C3 by default.
        return summary, "F-C3"
    if not summary["C5_threshold_robustness"]:
        return summary, "F-C4"
    if not summary["C6_saturation_robustness"]:
        return summary, "F-C5"
    return summary, None


def classify_status(summary: dict) -> str:
    must = (summary["C1_bar_death_exists"]
            and summary["C2_same_pre_sigma"]
            and summary["C3_different_post_sigma"]
            and summary["C4_same_protocol"])
    robustness = (summary["C5_threshold_robustness"]
                  and summary["C6_saturation_robustness"])
    if must and robustness:
        return "success"
    if must:
        return "weak_success"
    return "failed"


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------


def trajectory_to_dict(traj: TrajectoryL1, cfg: WQ1CConfig) -> dict:
    return {
        "name": traj.name,
        "variant": traj.variant,
        "centers": [list(c) for c in traj.centers],
        "M": traj.M,
        "snapshot_times": [s.tau for s in traj.snapshots],
        "K_bar_trajectory": {
            f"{ell:.2f}": [s.K_bar[ell] for s in traj.snapshots]
            for ell in cfg.ell_min_sweep
        },
        "K_soft_trajectory": [s.K_soft for s in traj.snapshots],
        "F_trajectory": [s.F for s in traj.snapshots],
        "dominant_bar_lengths": [s.bar_lengths for s in traj.snapshots],
        "events": {
            f"{ell:.2f}": [
                {
                    "snap_idx_pre": e[0], "snap_idx_post": e[1],
                    "K_bar_pre": e[2], "K_bar_post": e[3],
                    "tau_pre": traj.snapshots[e[0]].tau,
                    "tau_post": traj.snapshots[e[1]].tau,
                }
                for e in traj.events[ell]
            ]
            for ell in cfg.ell_min_sweep
        },
        "sigma_standard_at_event_brackets": {
            str(idx): [list(t) for t in traj.snapshots[idx].sigma_standard]
            for idx in range(len(traj.snapshots))
            if traj.snapshots[idx].sigma_standard is not None
        },
    }


def comparison_to_dict(c: dict) -> dict:
    out = dict(c)
    for k in ("A_sigma_pre", "A_sigma_post", "B_sigma_pre", "B_sigma_post"):
        v = out.get(k)
        if v is None:
            continue
        out[k] = [list(t) for t in v]
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_protocol(cfg: WQ1CConfig) -> dict:
    t0 = time.time()
    graph, positions = wq1.build_torus(cfg.n_torus)
    params = ParameterRegistry()

    variants = ["V0_saturated_gaussian", "V1_capped_smooth"]
    if not cfg.skip_v2:
        variants.append("V2_low_mass")

    runs: Dict[str, dict] = {}
    trajectories_by_key: Dict[str, TrajectoryL1] = {}
    for variant in variants:
        for label, centers in [("A_I", cfg.centers_A), ("B_I", cfg.centers_B)]:
            key = f"{variant}__{label}"
            print(f"[wq1c] Running {key} ...")
            traj = run_single_field_trajectory(
                cfg,
                name=("equilateral_aggregate" if label == "A_I"
                      else "compressed_aggregate"),
                variant=variant,
                centers=centers,
                graph=graph,
                positions=positions,
                params=params,
            )
            attach_sigma_at_events(traj, cfg, graph, params, positions)
            trajectories_by_key[key] = traj
            runs[key] = trajectory_to_dict(traj, cfg)

    # Comparisons per (variant, ell_min)
    comparisons: List[dict] = []
    for variant in variants:
        traj_A = trajectories_by_key[f"{variant}__A_I"]
        traj_B = trajectories_by_key[f"{variant}__B_I"]
        for ell in cfg.ell_min_sweep:
            comp = evaluate_comparison(traj_A, traj_B, ell, cfg)
            comparisons.append(comp)

    summary, failure_mode = aggregate_criteria(comparisons)
    status = classify_status(summary)

    if status == "success":
        conclusion_label = "supported"
    elif status == "weak_success":
        conclusion_label = "weak"
    elif failure_mode in ("F-C1", "F-C2"):
        conclusion_label = "undetermined"
    elif failure_mode == "F-C3":
        conclusion_label = "not_supported"
    elif failure_mode in ("F-C4", "F-C5"):
        conclusion_label = "weak"
    else:
        conclusion_label = "undetermined"

    wall = time.time() - t0
    out = {
        "protocol_id": "WQ-1.C",
        "protocol_version": PROTOCOL_VERSION,
        "status": status,
        "graph": {"type": "torus_grid", "n": cfg.n_torus},
        "state_space": "Sigma_M(G)",
        "parameters": {
            "M_default": cfg.M_default,
            "M_low_mass": cfg.M_low_mass,
            "sigma_b": cfg.sigma_b,
            "u_max_capped": cfg.u_max_capped,
            "dt": cfg.dt,
            "max_iter": cfg.max_iter,
            "snapshot_every": cfg.snapshot_every,
            "tau_lambda": cfg.tau_lambda,
            "ell_min_values": list(cfg.ell_min_sweep),
            "ell_min_default": cfg.ell_min_default,
            "n_eig_sigma": cfg.n_eig_sigma,
            "n_stab_post": cfg.n_stab_post,
            "seed": cfg.seed,
            "initialization_variants": variants,
        },
        "configurations": {
            "A_I": {"name": "equilateral_aggregate",
                    "centers": [list(c) for c in cfg.centers_A]},
            "B_I": {"name": "compressed_aggregate",
                    "centers": [list(c) for c in cfg.centers_B]},
        },
        "runs": runs,
        "comparisons": [comparison_to_dict(c) for c in comparisons],
        "criteria_summary": summary,
        "failure_mode": failure_mode,
        "conclusion": {
            "layerI_h0_sigma_incompleteness": conclusion_label,
            "multi_formation_OP0008": "not_claimed",
            "sigma_rich_sufficiency": "not_claimed",
            "scope_caveat": (
                "Restricted to projected FD-Hessian sigma_standard of "
                "scc/sigma_rich.py::_sigma_standard on T^2_20 single-field "
                "Layer I; not multi-formation; not a proof of OP-0008."
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
        description="WQ-1.C Layer I H_0 bar-death counterexample protocol.")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--snapshot_every", type=int, default=25)
    p.add_argument("--skip_v2", action="store_true",
                   help="Skip the V2 low-mass variant.")
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
    raise TypeError(f"Not JSON-serializable: {type(o)}")


def main() -> int:
    args = parse_args()
    cfg = WQ1CConfig(
        seed=args.seed, max_iter=args.max_iter,
        snapshot_every=args.snapshot_every,
        skip_v2=args.skip_v2,
    )
    print(f"[wq1c] Starting WQ-1.C protocol — seed={cfg.seed}, "
          f"max_iter={cfg.max_iter}, skip_v2={cfg.skip_v2}")
    out = run_protocol(cfg)
    print(f"[wq1c] Done. status={out['status']}, "
          f"wall={out['metadata']['wall_clock_seconds']:.1f}s")

    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[wq1c] Wrote {output_path}")

    # Print criteria summary
    cs = out["criteria_summary"]
    print(f"[wq1c] C1 (bar-death exists):        {cs['C1_bar_death_exists']}")
    print(f"[wq1c] C2 (same pre σ):              {cs['C2_same_pre_sigma']}")
    print(f"[wq1c] C3 (different post σ):        {cs['C3_different_post_sigma']}")
    print(f"[wq1c] C4 (same protocol):           {cs['C4_same_protocol']}")
    print(f"[wq1c] C5 (threshold robustness):    {cs['C5_threshold_robustness']}")
    print(f"[wq1c] C6 (saturation robustness):   {cs['C6_saturation_robustness']}")
    print(f"[wq1c] failure_mode: {out['failure_mode']}")
    print(f"[wq1c] conclusion: {out['conclusion']['layerI_h0_sigma_incompleteness']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
