"""NQ-242c Counterexample Protocol — executable WQ-1 script.

Implements the protocol of THEORY/working/MF/nq242c_counterexample_protocol.md.

Constructs two trajectories (Configuration A: equilateral disk-triangle;
Configuration B: isosceles disk-triangle) on the 20x20 torus, runs them under
a shared multi-field projected gradient flow with variable per-formation mass
(Option D-2 of the protocol), detects the first K-jump in each, computes
sigma_standard pre/post and sigma_rich pre/post, evaluates C1-C4 criteria,
and writes a JSON anchor conforming to
``CODE/scripts/results/nq242c_result_schema.json``.

This script is non-destructive. It writes only to the path supplied via
``--output`` and does not edit any other repository file.

The conclusion is restricted to the projected sigma_standard implementation
of ``scc/sigma_rich.py::_sigma_standard`` (FD-Hessian of aggregate field
``u.mean(axis=0)``), per the working-only Cat B sketch status of that module.
The script makes no claim about full multi-formation joint Hessian
sigma_standard, no claim about sigma_rich sufficiency, and no claim about
Phi_rich determinism. See protocol section 15 for the complete list of
forbidden non-claims.

Usage::

    cd CODE
    python3 scripts/nq242c_counterexample.py \\
        --output scripts/results/nq242c_results.json \\
        --seed 42 --max_iter 5000

Robustness run::

    cd CODE
    python3 scripts/nq242c_counterexample.py \\
        --output scripts/results/nq242c_results_robust.json \\
        --seed 137 --max_iter 5000 \\
        --robustness center_perturb

Run from the CODE/ directory so that ``scc`` resolves on sys.path.
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
from typing import List, Optional, Tuple

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# scc imports — assume run from CODE/ or with PYTHONPATH=CODE.
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume
from scc.sigma_rich import compute_sigma_rich, SigmaRich


PROTOCOL_VERSION = "1.0"


# ---------------------------------------------------------------------------
# Configuration dataclasses
# ---------------------------------------------------------------------------


@dataclass
class RunConfig:
    """All knobs of a single NQ-242c run."""
    K_field: int = 4
    M: float = 90.0
    epsilon: float = 0.225  # 0.01 * (M / K_field) = 0.01 * 22.5
    sigma_b: float = 2.0
    lambda_rep: float = 10.0
    lambda_bar: float = 100.0
    dt: float = 1e-3
    max_iter: int = 5000
    snapshot_every: int = 25
    tolerance_eigen: float = 1e-3
    seed: int = 42
    integrator: str = "Option_D2"
    n_torus: int = 20
    n_eig_sigma: int = 6
    grad_stagnation_window: int = 50
    grad_stagnation_threshold: float = 1e-5
    # Robustness perturbations (None = not applied to this run)
    center_perturb_B: Optional[Tuple[int, int]] = None
    sigma_b_perturb: Optional[float] = None
    # Initial centers
    centers_A: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 14))
    centers_B: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 11))
    # Mass per active formation, inactive slot 0
    initial_masses: Tuple[float, float, float, float] = (30.0, 30.0, 30.0, 0.0)


@dataclass
class Snapshot:
    tau: int
    fields: List[np.ndarray]
    m_j: List[float]
    K_act: int
    active_set: List[int]


@dataclass
class TrajectoryResult:
    name: str
    centers: List[Tuple[int, int]]
    initial_masses: List[float]
    snapshots: List[Snapshot] = field(default_factory=list)
    jump_time: Optional[int] = None
    K_act_pre: Optional[int] = None
    K_act_post: Optional[int] = None
    active_set_pre: Optional[List[int]] = None
    active_set_post: Optional[List[int]] = None
    sigma_pre: Optional[tuple] = None
    sigma_post: Optional[tuple] = None
    sigma_rich_pre: Optional[SigmaRich] = None
    sigma_rich_post: Optional[SigmaRich] = None
    multi_merger: bool = False
    no_k_jump: bool = False
    pre_snapshot_idx: Optional[int] = None
    post_snapshot_idx: Optional[int] = None


# ---------------------------------------------------------------------------
# Torus graph with positions
# ---------------------------------------------------------------------------


def build_torus(n: int) -> Tuple[GraphState, np.ndarray]:
    """Build T^2_n torus graph with explicit (x, y) positions per node.

    The repository's GraphState exposes ``grid_2d`` (with boundary) but no
    ``torus_2d`` constructor. Build periodic boundary conditions explicitly,
    matching the row-major vertex convention idx = r * n + c.
    Positions are an (n*n, 2) array of integer (row, col) coordinates.
    """
    rows = cols = n
    n_nodes = rows * cols
    row_idx: List[int] = []
    col_idx: List[int] = []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            # Right neighbor (with wrap)
            r_nb = idx - c + ((c + 1) % cols)
            row_idx.extend([idx, r_nb])
            col_idx.extend([r_nb, idx])
            # Down neighbor (with wrap)
            d_nb = ((r + 1) % rows) * cols + c
            row_idx.extend([idx, d_nb])
            col_idx.extend([d_nb, idx])
    data = np.ones(len(row_idx), dtype=np.float64)
    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n_nodes, n_nodes))
    # Deduplicate (each undirected edge added twice in both row/col_idx orders;
    # the right/down construction above also adds each edge twice via wrap;
    # CSR sums duplicate entries, so cap weights at 1.0).
    adj.data = np.minimum(adj.data, 1.0)
    g = GraphState(adj)
    positions = np.array([(i, j) for i in range(rows) for j in range(cols)],
                         dtype=np.float64)
    g.positions = positions  # ensure compute_sigma_rich can find them
    return g, positions


def torus_distance(p: np.ndarray, q: np.ndarray, n: int) -> np.ndarray:
    """Per-axis wrapped L2 distance on T^n."""
    d = np.abs(p - q)
    d = np.minimum(d, n - d)
    return np.sqrt(np.sum(d ** 2, axis=-1))


# ---------------------------------------------------------------------------
# Initial state construction
# ---------------------------------------------------------------------------


def build_initial_state(
    cfg: RunConfig,
    centers: List[Tuple[int, int]],
    positions: np.ndarray,
) -> List[np.ndarray]:
    """Construct K-field initial state with active_set = [0, 1, 2], slot 3 zero.

    Returns a list of K_field arrays each of length |X|.
    Enforces:
      - per-formation mass = cfg.initial_masses[k];
      - per-formation values in [0, 1];
      - simplex constraint sum_k u^(k)(x) <= 1 (best-effort via uniform scaling).
    """
    K = cfg.K_field
    n_torus = cfg.n_torus
    n_nodes = positions.shape[0]
    sigma_b = cfg.sigma_b if cfg.sigma_b_perturb is None else cfg.sigma_b_perturb

    fields: List[np.ndarray] = []
    for k in range(K):
        if cfg.initial_masses[k] <= 0:
            fields.append(np.zeros(n_nodes))
            continue
        c = np.array(centers[k], dtype=np.float64)
        d = torus_distance(positions, c, n_torus)
        u = np.exp(-(d ** 2) / (2.0 * sigma_b * sigma_b))
        # Normalize to mass
        u = u * (cfg.initial_masses[k] / u.sum())
        fields.append(u)

    # Clip + simplex enforcement loop
    for _ in range(5):
        # Clip individual fields to [0, 1]
        for k in range(K):
            fields[k] = np.clip(fields[k], 0.0, 1.0)
        # Re-project per-formation mass
        for k in range(K):
            if cfg.initial_masses[k] > 0:
                fields[k] = project_volume(fields[k], cfg.initial_masses[k])
                fields[k] = np.clip(fields[k], 0.0, 1.0)
        # Check simplex constraint
        S = sum(fields)
        violation = float(np.max(np.maximum(0.0, S - 1.0)))
        if violation < 1e-3:
            break
        # Uniform downscale all active fields by (1 - violation)
        scale = 1.0 / max(1.0 + violation, 1.001)
        for k in range(K):
            if cfg.initial_masses[k] > 0:
                fields[k] = fields[k] * scale

    # Re-normalize masses one final time
    for k in range(K):
        if cfg.initial_masses[k] > 0:
            fields[k] = fields[k] * (cfg.initial_masses[k] / max(fields[k].sum(), 1e-12))

    return fields


# ---------------------------------------------------------------------------
# Variable-per-formation-mass projection (Option D-2)
# ---------------------------------------------------------------------------


def project_to_layer_II_D2(
    fields: List[np.ndarray],
    M_total: float,
) -> List[np.ndarray]:
    """Option D-2 projection per protocol section 6.3.

    Clip each formation to [0, 1], allow per-formation mass to drift, then
    rescale all formations by a common factor so total mass returns to M.
    """
    fields = [np.clip(f, 0.0, 1.0) for f in fields]
    total_now = sum(float(f.sum()) for f in fields)
    if total_now <= 1e-12:
        return fields
    rescale = M_total / total_now
    fields = [f * rescale for f in fields]
    fields = [np.clip(f, 0.0, 1.0) for f in fields]
    return fields


# ---------------------------------------------------------------------------
# Trajectory loop with snapshots
# ---------------------------------------------------------------------------


def run_trajectory(
    cfg: RunConfig,
    name: str,
    centers: List[Tuple[int, int]],
    graph: GraphState,
    positions: np.ndarray,
    params: ParameterRegistry,
    rng: np.random.RandomState,
) -> TrajectoryResult:
    """Run a single Layer II projected gradient flow with snapshotting.

    Energy:
        E = sum_k E_self(u^k) + lambda_rep * sum_{j<k} <u^j, u^k>
            + lambda_bar * sum_x max(0, S(x) - 1)^2
    Integrator: Option D-2 of protocol.
    """
    K = cfg.K_field
    n = positions.shape[0]
    fields = build_initial_state(cfg, centers, positions)

    # Slots that started at zero mass are architectural-only: their dynamics
    # are masked so they remain at zero. This preserves the protocol's
    # spare-slot semantics under Option D-2 (mean-subtraction injects
    # uniform mass into zero slots otherwise).
    active_slot_mask = [cfg.initial_masses[k] > 0 for k in range(K)]

    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    result = TrajectoryResult(
        name=name,
        centers=list(centers),
        initial_masses=list(cfg.initial_masses),
    )

    # Snapshot at tau = 0
    result.snapshots.append(_make_snapshot(0, fields, cfg.epsilon))

    dt = cfg.dt
    grad_norm_history: List[float] = []

    for tau in range(1, cfg.max_iter + 1):
        max_gnorm = 0.0
        for k in range(K):
            if not active_slot_mask[k]:
                continue  # spare slot: no update, stays at zero
            g_intra = ec.gradient(fields[k])
            g_rep = np.zeros(n)
            for j in range(K):
                if j != k and active_slot_mask[j]:
                    g_rep += fields[j]
            g_rep *= cfg.lambda_rep
            S = sum(fields)
            violation = np.maximum(0.0, S - 1.0)
            g_bar = cfg.lambda_bar * 2.0 * violation
            g_total = g_intra + g_rep + g_bar
            g_proj = g_total - np.mean(g_total)
            gnorm = float(np.linalg.norm(g_proj) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)
            fields[k] = fields[k] - dt * g_proj

        # Option D-2 projection (preserves zero on masked slots since they
        # never received any mass; the rescale only redistributes among
        # active slots).
        active_fields = [fields[k] for k in range(K) if active_slot_mask[k]]
        active_fields = project_to_layer_II_D2(active_fields, cfg.M)
        for idx, k in enumerate([kk for kk in range(K) if active_slot_mask[kk]]):
            fields[k] = active_fields[idx]

        grad_norm_history.append(max_gnorm)

        # Adaptive step size (matches multi.py heuristic)
        if tau > 5 and len(grad_norm_history) > 2:
            prev = grad_norm_history[-2]
            if max_gnorm > prev * 1.5:
                dt = max(dt * 0.7, 1e-8)
            elif max_gnorm < prev * 0.95:
                dt = min(dt * 1.05, 0.1)

        # Snapshot
        if tau % cfg.snapshot_every == 0:
            result.snapshots.append(_make_snapshot(tau, fields, cfg.epsilon))
            # K-jump detection
            prev_K_act = result.snapshots[-2].K_act
            curr_K_act = result.snapshots[-1].K_act
            if curr_K_act < prev_K_act and result.jump_time is None:
                result.jump_time = tau
                result.K_act_pre = prev_K_act
                result.K_act_post = curr_K_act
                result.active_set_pre = result.snapshots[-2].active_set
                result.active_set_post = result.snapshots[-1].active_set
                result.pre_snapshot_idx = len(result.snapshots) - 2
                result.post_snapshot_idx = len(result.snapshots) - 1
                if prev_K_act - curr_K_act >= 2:
                    result.multi_merger = True

        # Stagnation stop
        if (len(grad_norm_history) >= cfg.grad_stagnation_window
                and all(g < cfg.grad_stagnation_threshold
                        for g in grad_norm_history[-cfg.grad_stagnation_window:])):
            break

    if result.jump_time is None:
        result.no_k_jump = True

    return result


def _make_snapshot(tau: int, fields: List[np.ndarray], eps: float) -> Snapshot:
    m_j = [float(f.sum()) for f in fields]
    active = [j for j, m in enumerate(m_j) if m > eps]
    return Snapshot(
        tau=tau,
        fields=[f.copy() for f in fields],
        m_j=m_j,
        K_act=len(active),
        active_set=active,
    )


# ---------------------------------------------------------------------------
# σ-rich extraction at pre/post snapshots
# ---------------------------------------------------------------------------


def extract_sigma_rich_at_snapshot(
    snap: Snapshot,
    graph: GraphState,
    params: ParameterRegistry,
    positions: np.ndarray,
    n_eig: int,
) -> SigmaRich:
    u_field = np.stack(snap.fields, axis=0)  # (K, n)
    return compute_sigma_rich(
        u_field=u_field,
        graph_state=graph,
        params=params,
        positions=positions,
        n_eig=n_eig,
    )


def post_stabilization_index(
    result: TrajectoryResult,
    n_stab: int = 4,
) -> int:
    """Pick the post-stabilization snapshot index = jump_idx + n_stab,
    clamped to last available snapshot."""
    if result.post_snapshot_idx is None:
        return len(result.snapshots) - 1
    target = result.post_snapshot_idx + n_stab
    return min(target, len(result.snapshots) - 1)


# ---------------------------------------------------------------------------
# σ-standard tolerance comparator
# ---------------------------------------------------------------------------


def sigma_standard_compare(
    sa: tuple,
    sb: tuple,
    tol: float,
) -> Tuple[bool, float, Optional[int]]:
    """Compare two sigma_standard tuples within tolerance.

    Returns (equal, max_lambda_diff, offending_cluster_index).
    Equal iff: same number of clusters, same cluster sizes, and
    |lambda_k_a - lambda_k_b| < tol for all k.
    """
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
    return equal, max_diff, offender if not equal else None


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------


def sigma_rich_to_dict(sr: SigmaRich) -> dict:
    return {
        "sigma_standard": [list(t) for t in sr.sigma_standard],
        "centroids": sr.centroids.tolist(),
        "orientations": sr.orientations.tolist(),
        "wigner_data": sr.wigner_data.tolist(),
    }


def trajectory_to_dict(result: TrajectoryResult) -> dict:
    sigma_pre = ([list(t) for t in result.sigma_pre]
                 if result.sigma_pre is not None else None)
    sigma_post = ([list(t) for t in result.sigma_post]
                  if result.sigma_post is not None else None)
    return {
        "name": result.name,
        "centers": [list(c) for c in result.centers],
        "initial_masses": result.initial_masses,
        "sigma_pre": sigma_pre,
        "sigma_post": sigma_post,
        "K_act_pre": result.K_act_pre,
        "K_act_post": result.K_act_post,
        "jump_time": result.jump_time,
        "multi_merger": result.multi_merger,
        "no_k_jump": result.no_k_jump,
        "active_set_pre": result.active_set_pre,
        "active_set_post": result.active_set_post,
    }


# ---------------------------------------------------------------------------
# Main run
# ---------------------------------------------------------------------------


def run_protocol(cfg: RunConfig) -> dict:
    """Execute the full NQ-242c protocol and return the result dict."""
    t0 = time.time()
    rng = np.random.RandomState(cfg.seed)
    graph, positions = build_torus(cfg.n_torus)
    params = ParameterRegistry()

    # Apply center perturbation to B if requested
    centers_A = list(cfg.centers_A)
    centers_B = list(cfg.centers_B)
    if cfg.center_perturb_B is not None:
        dx, dy = cfg.center_perturb_B
        c3 = centers_B[2]
        centers_B[2] = ((c3[0] + dx) % cfg.n_torus, (c3[1] + dy) % cfg.n_torus)

    # Run both trajectories with same seed (independent rng instances)
    rng_A = np.random.RandomState(cfg.seed)
    rng_B = np.random.RandomState(cfg.seed)
    result_A = run_trajectory(cfg, "equilateral_disk_triangle", centers_A,
                              graph, positions, params, rng_A)
    result_B = run_trajectory(cfg, "isosceles_disk_triangle", centers_B,
                              graph, positions, params, rng_B)

    # σ-rich at pre/post snapshots, when K-jump occurred
    for result in (result_A, result_B):
        if result.no_k_jump:
            continue
        pre_idx = result.pre_snapshot_idx
        post_idx = post_stabilization_index(result)
        if pre_idx is not None:
            sr_pre = extract_sigma_rich_at_snapshot(
                result.snapshots[pre_idx], graph, params, positions,
                cfg.n_eig_sigma)
            result.sigma_rich_pre = sr_pre
            result.sigma_pre = sr_pre.sigma_standard
        if post_idx is not None:
            sr_post = extract_sigma_rich_at_snapshot(
                result.snapshots[post_idx], graph, params, positions,
                cfg.n_eig_sigma)
            result.sigma_rich_post = sr_post
            result.sigma_post = sr_post.sigma_standard

    # C1, C2, C3 evaluation
    have_both_jumps = (result_A.sigma_pre is not None
                       and result_B.sigma_pre is not None
                       and result_A.sigma_post is not None
                       and result_B.sigma_post is not None)
    if have_both_jumps:
        c1_eq, c1_max_diff, c1_offender = sigma_standard_compare(
            result_A.sigma_pre, result_B.sigma_pre, cfg.tolerance_eigen)
        c2_eq, c2_max_diff, c2_offender = sigma_standard_compare(
            result_A.sigma_post, result_B.sigma_post, cfg.tolerance_eigen)
        c1_pass = c1_eq
        c2_pass = (not c2_eq) and c2_max_diff > 10.0 * cfg.tolerance_eigen
    else:
        c1_pass, c2_pass = False, False
        c1_max_diff, c2_max_diff = float("nan"), float("nan")
        c1_offender, c2_offender = None, None
    c3_pass = True  # by construction (single shared cfg)

    # Status classification
    if result_A.no_k_jump or result_B.no_k_jump:
        status = "failed"
        failure_mode: Optional[str] = "F2"
    elif not c1_pass:
        status = "failed"
        failure_mode = "F1"
    elif not c2_pass and c2_max_diff < cfg.tolerance_eigen:
        status = "failed"
        failure_mode = "F3"
    elif not c2_pass:
        status = "failed"
        failure_mode = "F4"
    elif c1_pass and c2_pass and c3_pass:
        status = "weak_success"  # success only after C4 robustness check
        failure_mode = None
    else:
        status = "failed"
        failure_mode = "F4"

    # Conclusion mapping
    if status == "weak_success":
        conclusion_label = "weak"
    elif status == "failed" and failure_mode in ("F1", "F2"):
        conclusion_label = "undetermined"
    elif status == "failed" and failure_mode == "F3":
        conclusion_label = "not_supported"
    elif status == "failed" and failure_mode == "F4":
        conclusion_label = "weak"
    else:
        conclusion_label = "undetermined"

    wall = time.time() - t0

    out = {
        "protocol_id": "NQ-242c",
        "protocol_version": PROTOCOL_VERSION,
        "status": status,
        "graph": {"type": "torus_grid", "n": cfg.n_torus},
        "parameters": {
            "K_field": cfg.K_field, "M": cfg.M,
            "epsilon": cfg.epsilon,
            "lambda_rep": cfg.lambda_rep, "lambda_bar": cfg.lambda_bar,
            "sigma_b": cfg.sigma_b, "dt": cfg.dt,
            "max_iter": cfg.max_iter,
            "snapshot_every": cfg.snapshot_every,
            "tolerance_eigen": cfg.tolerance_eigen,
            "seed": cfg.seed,
            "integrator": cfg.integrator,
            "center_perturb": (list(cfg.center_perturb_B)
                               if cfg.center_perturb_B else None),
            "sigma_b_perturb": cfg.sigma_b_perturb,
        },
        "configuration_A": trajectory_to_dict(result_A),
        "configuration_B": trajectory_to_dict(result_B),
        "criteria": {
            "C1_same_pre_sigma": c1_pass,
            "C1_max_lambda_diff": c1_max_diff,
            "C1_cluster_size_match": (
                len(result_A.sigma_pre) == len(result_B.sigma_pre)
                if (result_A.sigma_pre is not None
                    and result_B.sigma_pre is not None)
                else None
            ),
            "C2_different_post_sigma": c2_pass,
            "C2_max_lambda_diff": c2_max_diff,
            "C2_offending_cluster": c2_offender,
            "C3_same_protocol": c3_pass,
            "C4_robustness": None,  # set by post-processing combining runs
            "C4_robustness_notes": [],
        },
        "diagnostics": {
            "sigma_rich_pre_A": (sigma_rich_to_dict(result_A.sigma_rich_pre)
                                 if result_A.sigma_rich_pre else None),
            "sigma_rich_pre_B": (sigma_rich_to_dict(result_B.sigma_rich_pre)
                                 if result_B.sigma_rich_pre else None),
            "sigma_rich_post_A": (sigma_rich_to_dict(result_A.sigma_rich_post)
                                  if result_A.sigma_rich_post else None),
            "sigma_rich_post_B": (sigma_rich_to_dict(result_B.sigma_rich_post)
                                  if result_B.sigma_rich_post else None),
            "k_act_trajectory_A": [s.K_act for s in result_A.snapshots],
            "k_act_trajectory_B": [s.K_act for s in result_B.snapshots],
            "m_j_trajectory_A": [s.m_j for s in result_A.snapshots],
            "m_j_trajectory_B": [s.m_j for s in result_B.snapshots],
            "snapshot_times_A": [s.tau for s in result_A.snapshots],
            "snapshot_times_B": [s.tau for s in result_B.snapshots],
        },
        "conclusion": {
            "standard_sigma_incomplete": conclusion_label,
            "sigma_rich_sufficiency": "not_claimed",
            "scope_caveat": (
                "Conclusion restricted to the projected sigma_standard of "
                "scc/sigma_rich.py::_sigma_standard, which builds the "
                "FD-Hessian on u.mean(axis=0). Full multi-formation joint "
                "Hessian sigma_standard is not implemented."
            ),
            "failure_mode": failure_mode,
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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="NQ-242c counterexample protocol — WQ-1 executable.")
    p.add_argument("--output", type=str, required=True,
                   help="Path to write JSON result.")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--epsilon", type=float, default=0.225)
    p.add_argument("--lambda_rep", type=float, default=10.0)
    p.add_argument("--lambda_bar", type=float, default=100.0)
    p.add_argument("--sigma_b", type=float, default=2.0)
    p.add_argument("--dt", type=float, default=1e-3)
    p.add_argument("--snapshot_every", type=int, default=25)
    p.add_argument("--tolerance_eigen", type=float, default=1e-3)
    p.add_argument("--robustness", type=str, default=None,
                   help="Comma-separated robustness perturbations: "
                        "center_perturb,sigma_b_perturb")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    cfg = RunConfig(
        seed=args.seed,
        max_iter=args.max_iter,
        epsilon=args.epsilon,
        lambda_rep=args.lambda_rep,
        lambda_bar=args.lambda_bar,
        sigma_b=args.sigma_b,
        dt=args.dt,
        snapshot_every=args.snapshot_every,
        tolerance_eigen=args.tolerance_eigen,
    )

    if args.robustness:
        perturbations = args.robustness.split(",")
        if "center_perturb" in perturbations:
            cfg.center_perturb_B = (0, 1)  # shift c_3^B by (0, +1)
        if "sigma_b_perturb" in perturbations:
            cfg.sigma_b_perturb = cfg.sigma_b * 1.25

    print(f"[nq242c] Starting protocol — seed={cfg.seed}, "
          f"max_iter={cfg.max_iter}, integrator={cfg.integrator}")
    out = run_protocol(cfg)
    print(f"[nq242c] Done. status={out['status']}, "
          f"wall={out['metadata']['wall_clock_seconds']:.1f}s")

    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[nq242c] Wrote {output_path}")

    # Print C1-C4 summary
    crit = out["criteria"]
    print(f"[nq242c] C1 (same pre-σ):    {crit['C1_same_pre_sigma']} "
          f"(max λ diff = {crit['C1_max_lambda_diff']})")
    print(f"[nq242c] C2 (diff post-σ):   {crit['C2_different_post_sigma']} "
          f"(max λ diff = {crit['C2_max_lambda_diff']})")
    print(f"[nq242c] C3 (same protocol): {crit['C3_same_protocol']}")
    print(f"[nq242c] C4 (robustness):    {crit['C4_robustness']} "
          f"(post-processing required)")
    print(f"[nq242c] conclusion: {out['conclusion']['standard_sigma_incomplete']}")
    if out["conclusion"]["failure_mode"]:
        print(f"[nq242c] failure_mode: {out['conclusion']['failure_mode']}")

    return 0


def _json_default(o):
    if isinstance(o, (np.integer, np.int32, np.int64)):
        return int(o)
    if isinstance(o, (np.floating, np.float32, np.float64)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Not JSON-serializable: {type(o)}")


if __name__ == "__main__":
    sys.exit(main())
