"""WQ-2 ksoft / kact bridge diagnostics.

Reruns the WQ-1 NQ-242c trajectories with per-snapshot diagnostics for the
K_soft / K_act bridge analysis of THEORY/working/MF/ksoft_kact_bridge_lemma.md.

For each snapshot u(t) of a trajectory:
  - per-slot mass m_j(t)
  - active count K_act^epsilon(t)
  - aggregate field U(t) = sum_j u^(j)(t)
  - H_0 superlevel barcode of U(t) on the torus graph G
  - dominant bar lengths
  - hard-bar count K_bar^{l_min}(U(t)) = #{i : l_i(U(t)) >= l_min}
  - soft count K_soft^phi(U(t)) with phi(l) = l / (l + l_min) by default
  - aggregate F (number of strict local maxima of U(t))
  - per-formation F (number of strict local maxima of each active u^(j)(t))
  - pairwise overlaps O_{jk}(t)
  - regime label (well-separated / overlap / multimodal / corner-saturated /
    ambiguous)

The script does NOT edit any canonical or existing working file. It writes
only to the path supplied via --output.

Status: working diagnostic. The persistence pipeline reuses
``scc.diagnostics._persistence_h0_graph``; per-formation distances reuse
``scc.multi.inter_formation_distances``. No new persistence implementation.

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/ksoft_kact_diagnostics.py \\
        --output CODE/scripts/results/ksoft_kact_diag.json \\
        --max_iter 5000 --seed 42

Sweep multiple configurations::

    PYTHONPATH=CODE python3 CODE/scripts/ksoft_kact_diagnostics.py \\
        --output CODE/scripts/results/ksoft_kact_sweep.json \\
        --max_iter 5000 --seed 42 \\
        --sweep lambda_rep:10,30,100 compress_B:8,7,6
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
from dataclasses import asdict
from typing import Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.diagnostics import _persistence_h0_graph
from scc.multi import inter_formation_distances

import nq242c_counterexample as wq1


DIAG_VERSION = "1.0"


def aggregate_field(fields: List[np.ndarray]) -> np.ndarray:
    return np.sum(fields, axis=0)


def h0_barcode(u: np.ndarray, graph) -> List[Tuple[float, float]]:
    """Full H_0 superlevel persistence barcode on a GraphState.

    Reimplements scc.persistence.persistence_h0 in graph-agnostic form
    (the wrapper in scc.persistence is grid-only).
    Returns list of (birth, death) pairs.
    """
    n = graph.n
    if n == 0:
        return []
    order = np.argsort(-u)
    W_coo = graph.W.tocoo()
    adj: List[List[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(int(j))

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    active = np.zeros(n, dtype=bool)
    bars: List[Tuple[float, float]] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        active[idx] = True
        birth_val[idx] = u[idx]
        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            if birth_val[ri] >= birth_val[rn]:
                bars.append((float(birth_val[rn]), float(u[idx])))
                parent[rn] = ri
            else:
                bars.append((float(birth_val[ri]), float(u[idx])))
                parent[ri] = rn

    bars.append((float(np.max(u)), 0.0))
    bars.sort(key=lambda bd: bd[0] - bd[1], reverse=True)
    return bars


def bar_lengths(barcode: List[Tuple[float, float]]) -> List[float]:
    return [b - d for (b, d) in barcode]


def k_bar(barcode: List[Tuple[float, float]], l_min: float) -> int:
    return sum(1 for ell in bar_lengths(barcode) if ell >= l_min)


def k_soft_phi_sat(barcode: List[Tuple[float, float]], l_min: float) -> float:
    """phi(l) = l / (l + l_min) — saturating, normalized so phi(l_min) = 0.5."""
    return float(sum(ell / (ell + l_min) for ell in bar_lengths(barcode)
                     if ell > 0.0))


def f_count(u: np.ndarray, graph) -> int:
    """Number of strict local maxima of u over graph adjacency."""
    n = graph.n
    W_coo = graph.W.tocoo()
    adj: List[List[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(int(j))
    cnt = 0
    for x in range(n):
        if all(u[x] > u[y] for y in adj[x]):
            cnt += 1
    return cnt


def pairwise_overlap_matrix(fields: List[np.ndarray]) -> List[List[float]]:
    K = len(fields)
    out = [[0.0] * K for _ in range(K)]
    for j in range(K):
        for k in range(j, K):
            v = float(np.sum(fields[j] * fields[k]))
            out[j][k] = v
            out[k][j] = v
    return out


def classify_regime(
    K_act: int,
    K_bar_v: int,
    K_soft_v: float,
    F_aggregate: int,
    F_per_formation: List[int],
    min_support_distance: float,
    max_overlap: float,
    min_mass: float,
    max_field_value: float,
    max_simplex_sum: float,
    epsilon: float,
    D_sep_threshold: float,
    eta_threshold: float,
    field_boundary_tol: float,
    simplex_boundary_tol: float,
) -> str:
    if (min_mass < epsilon + 2 * epsilon
            or max_field_value > 1.0 - field_boundary_tol
            or max_simplex_sum > 1.0 - simplex_boundary_tol):
        return "corner-saturated"
    if K_act > K_bar_v:
        return "overlap"
    if F_aggregate > K_act and any(f >= 2 for f in F_per_formation):
        return "multimodal"
    if max_overlap > eta_threshold:
        return "overlap"
    if min_support_distance < D_sep_threshold:
        return "overlap"
    if K_act == K_bar_v and max_overlap <= eta_threshold \
            and min_support_distance >= D_sep_threshold:
        return "well-separated"
    return "ambiguous"


def support_delta(field: np.ndarray, delta: float) -> np.ndarray:
    return field > delta


def compute_diagnostics_for_trajectory(
    cfg: wq1.RunConfig,
    name: str,
    centers,
    graph,
    positions,
    params,
    rng,
    l_min: float,
    delta: float,
    D_sep_threshold: float,
    eta_threshold: float,
    field_boundary_tol: float = 1e-3,
    simplex_boundary_tol: float = 1e-3,
) -> dict:
    """Run a single trajectory and return per-snapshot diagnostics."""
    result = wq1.run_trajectory(cfg, name, centers, graph, positions, params, rng)

    snapshot_times: List[int] = []
    K_act_list: List[int] = []
    K_bar_list: List[int] = []
    K_soft_list: List[float] = []
    F_aggregate_list: List[int] = []
    F_per_formation_list: List[List[int]] = []
    dominant_bars_list: List[List[float]] = []
    subdominant_bars_count_list: List[int] = []
    pairwise_overlaps_list: List[List[List[float]]] = []
    min_support_distance_list: List[float] = []
    max_overlap_list: List[float] = []
    regime_label_list: List[str] = []
    m_j_list: List[List[float]] = []

    for snap in result.snapshots:
        fields = snap.fields
        U = aggregate_field(fields)
        barcode = h0_barcode(U, graph)
        ells = bar_lengths(barcode)
        ells_sorted = sorted(ells, reverse=True)
        Kbar = k_bar(barcode, l_min)
        Ksoft = k_soft_phi_sat(barcode, l_min)
        Fagg = f_count(U, graph)
        Fper = []
        for j, f in enumerate(fields):
            if snap.m_j[j] > cfg.epsilon:
                Fper.append(f_count(f, graph))
            else:
                Fper.append(0)
        overlap_mat = pairwise_overlap_matrix(fields)
        K = cfg.K_field
        max_overlap = 0.0
        for j in range(K):
            for k in range(j + 1, K):
                if snap.m_j[j] > cfg.epsilon and snap.m_j[k] > cfg.epsilon:
                    if overlap_mat[j][k] > max_overlap:
                        max_overlap = overlap_mat[j][k]
        # support distances
        try:
            D = inter_formation_distances(fields, graph, theta_supp=delta)
            min_dist = float("inf")
            for j in range(K):
                for k in range(j + 1, K):
                    if snap.m_j[j] > cfg.epsilon and snap.m_j[k] > cfg.epsilon:
                        if D[j][k] < min_dist:
                            min_dist = float(D[j][k])
            if not np.isfinite(min_dist):
                min_dist = -1.0
        except Exception:
            min_dist = -1.0
        active_masses = [m for m in snap.m_j if m > cfg.epsilon]
        min_active_mass = min(active_masses) if active_masses else 0.0
        max_field_value = float(max(np.max(f) for f in fields))
        max_simplex_sum = float(np.max(U))
        regime = classify_regime(
            snap.K_act, Kbar, Ksoft, Fagg, Fper,
            min_dist, max_overlap, min_active_mass,
            max_field_value, max_simplex_sum,
            cfg.epsilon, D_sep_threshold, eta_threshold,
            field_boundary_tol, simplex_boundary_tol,
        )

        snapshot_times.append(snap.tau)
        K_act_list.append(snap.K_act)
        K_bar_list.append(Kbar)
        K_soft_list.append(Ksoft)
        F_aggregate_list.append(Fagg)
        F_per_formation_list.append(Fper)
        dominant_bars_list.append(ells_sorted[: max(8, K + 2)])
        subdominant_bars_count_list.append(
            sum(1 for ell in ells if 1e-6 < ell < l_min))
        pairwise_overlaps_list.append(overlap_mat)
        min_support_distance_list.append(min_dist)
        max_overlap_list.append(max_overlap)
        regime_label_list.append(regime)
        m_j_list.append(snap.m_j)

    return {
        "name": name,
        "centers": [list(c) for c in centers],
        "snapshot_times": snapshot_times,
        "K_act": K_act_list,
        "K_bar": K_bar_list,
        "K_soft": K_soft_list,
        "F_aggregate": F_aggregate_list,
        "F_per_formation": F_per_formation_list,
        "dominant_bar_lengths": dominant_bars_list,
        "subdominant_bar_count": subdominant_bars_count_list,
        "pairwise_overlaps": pairwise_overlaps_list,
        "min_support_distance": min_support_distance_list,
        "max_overlap": max_overlap_list,
        "regime_label": regime_label_list,
        "m_j_trajectory": m_j_list,
        "jump_time": result.jump_time,
        "no_k_jump": result.no_k_jump,
    }


def summarize_trajectory(traj_diag: dict) -> dict:
    """Top-line summary for the WQ-2 decision rule (I-1 ... I-4)."""
    K_act = traj_diag["K_act"]
    K_bar = traj_diag["K_bar"]
    K_soft = traj_diag["K_soft"]
    regimes = traj_diag["regime_label"]
    dominant_bars = traj_diag["dominant_bar_lengths"]

    K_bar_changed = any(K_bar[i] != K_bar[0] for i in range(len(K_bar)))
    K_soft_range = (max(K_soft) - min(K_soft)) if K_soft else 0.0
    K_soft_changed_smooth = K_soft_range > 0.05  # heuristic; tune as needed
    regime_changed = len(set(regimes)) > 1
    dominant_bar_drift = 0.0
    if dominant_bars and len(dominant_bars[0]) > 0:
        first_bar0 = dominant_bars[0][0]
        last_bar0 = dominant_bars[-1][0] if dominant_bars[-1] else first_bar0
        dominant_bar_drift = abs(last_bar0 - first_bar0)
    return {
        "I_1_K_soft_changed_smooth": K_soft_changed_smooth,
        "I_1_K_soft_range": K_soft_range,
        "I_2_K_bar_changed": K_bar_changed,
        "I_2_K_bar_first": K_bar[0] if K_bar else None,
        "I_2_K_bar_last": K_bar[-1] if K_bar else None,
        "I_3_regime_changed": regime_changed,
        "I_3_regime_first": regimes[0] if regimes else None,
        "I_3_regime_last": regimes[-1] if regimes else None,
        "I_4_dominant_bar_drift": dominant_bar_drift,
        "K_act_first": K_act[0] if K_act else None,
        "K_act_last": K_act[-1] if K_act else None,
        "K_act_changed": any(K_act[i] != K_act[0] for i in range(len(K_act))),
    }


def recommend_retry_path(summary_A: dict, summary_B: dict) -> str:
    """Apply the WQ-1 retry decision rule from
    THEORY/working/MF/ksoft_kact_bridge_lemma.md §9.1."""
    any_K_bar_change = (summary_A["I_2_K_bar_changed"]
                        or summary_B["I_2_K_bar_changed"])
    any_K_soft_change = (summary_A["I_1_K_soft_changed_smooth"]
                        or summary_B["I_1_K_soft_changed_smooth"])
    any_regime_change = (summary_A["I_3_regime_changed"]
                        or summary_B["I_3_regime_changed"])
    if any_K_bar_change:
        return "WQ-1.C (Layer I H_0 jump reframe)"
    if any_K_soft_change or any_regime_change:
        return "WQ-1.C with smooth/regime-transition framing"
    return "WQ-1.A (true joint projection)"


def run_one(cfg: wq1.RunConfig, args) -> dict:
    t0 = time.time()
    rng = np.random.RandomState(cfg.seed)
    graph, positions = wq1.build_torus(cfg.n_torus)
    params = wq1.ParameterRegistry()

    centers_A = list(cfg.centers_A)
    centers_B = list(cfg.centers_B)

    rng_A = np.random.RandomState(cfg.seed)
    rng_B = np.random.RandomState(cfg.seed)
    diag_A = compute_diagnostics_for_trajectory(
        cfg, "equilateral_disk_triangle", centers_A,
        graph, positions, params, rng_A,
        l_min=args.l_min, delta=args.delta,
        D_sep_threshold=args.D_sep_threshold,
        eta_threshold=args.eta_threshold,
    )
    diag_B = compute_diagnostics_for_trajectory(
        cfg, "isosceles_disk_triangle", centers_B,
        graph, positions, params, rng_B,
        l_min=args.l_min, delta=args.delta,
        D_sep_threshold=args.D_sep_threshold,
        eta_threshold=args.eta_threshold,
    )
    summary_A = summarize_trajectory(diag_A)
    summary_B = summarize_trajectory(diag_B)
    retry = recommend_retry_path(summary_A, summary_B)
    wall = time.time() - t0
    return {
        "diag_version": DIAG_VERSION,
        "config": {
            "K_field": cfg.K_field, "M": cfg.M,
            "epsilon": cfg.epsilon,
            "lambda_rep": cfg.lambda_rep, "lambda_bar": cfg.lambda_bar,
            "sigma_b": cfg.sigma_b, "dt": cfg.dt,
            "max_iter": cfg.max_iter, "snapshot_every": cfg.snapshot_every,
            "seed": cfg.seed, "n_torus": cfg.n_torus,
            "centers_A": [list(c) for c in cfg.centers_A],
            "centers_B": [list(c) for c in cfg.centers_B],
            "initial_masses": list(cfg.initial_masses),
            "l_min": args.l_min,
            "delta": args.delta,
            "phi_family": "phi-sat",
            "phi_params": {"l_min": args.l_min},
            "D_sep_threshold": args.D_sep_threshold,
            "eta_threshold": args.eta_threshold,
        },
        "trajectory_A": diag_A,
        "trajectory_B": diag_B,
        "summary_A": summary_A,
        "summary_B": summary_B,
        "recommendation": retry,
        "wall_clock_seconds": wall,
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=(
        "WQ-2 ksoft/kact bridge diagnostics on NQ-242c trajectories."))
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_iter", type=int, default=5000)
    p.add_argument("--lambda_rep", type=float, default=10.0)
    p.add_argument("--snapshot_every", type=int, default=25)
    p.add_argument("--l_min", type=float, default=0.10)
    p.add_argument("--delta", type=float, default=0.05)
    p.add_argument("--D_sep_threshold", type=float, default=3.0)
    p.add_argument("--eta_threshold", type=float, default=0.5)
    p.add_argument("--compress_B", type=int, default=None,
                   help="If set, c_3^B = (10, compress_B). Default 11.")
    return p.parse_args()


def _git_commit() -> Optional[str]:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
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
    raise TypeError(f"Not JSON-serializable: {type(o)}")


def main() -> int:
    args = parse_args()

    cfg = wq1.RunConfig(
        seed=args.seed, max_iter=args.max_iter,
        lambda_rep=args.lambda_rep,
        snapshot_every=args.snapshot_every,
    )
    if args.compress_B is not None:
        cfg.centers_B = ((5, 5), (15, 5), (10, args.compress_B))

    print(f"[ksoft_kact] Running diagnostics — seed={cfg.seed}, "
          f"lambda_rep={cfg.lambda_rep}, max_iter={cfg.max_iter}")
    out = run_one(cfg, args)
    out["metadata"] = {
        "git_commit": _git_commit(),
        "host": socket.gethostname(),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                              time.gmtime()),
    }
    output_path = args.output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(out, fh, indent=2, default=_json_default)
    print(f"[ksoft_kact] Wrote {output_path}")
    print(f"[ksoft_kact] Wall: {out['wall_clock_seconds']:.1f}s")
    print(f"[ksoft_kact] A: K_act {out['summary_A']['K_act_first']}->"
          f"{out['summary_A']['K_act_last']}, "
          f"K_bar {out['summary_A']['I_2_K_bar_first']}->"
          f"{out['summary_A']['I_2_K_bar_last']} "
          f"(changed={out['summary_A']['I_2_K_bar_changed']}), "
          f"K_soft range={out['summary_A']['I_1_K_soft_range']:.3f}, "
          f"regime {out['summary_A']['I_3_regime_first']}->"
          f"{out['summary_A']['I_3_regime_last']}")
    print(f"[ksoft_kact] B: K_act {out['summary_B']['K_act_first']}->"
          f"{out['summary_B']['K_act_last']}, "
          f"K_bar {out['summary_B']['I_2_K_bar_first']}->"
          f"{out['summary_B']['I_2_K_bar_last']} "
          f"(changed={out['summary_B']['I_2_K_bar_changed']}), "
          f"K_soft range={out['summary_B']['I_1_K_soft_range']:.3f}, "
          f"regime {out['summary_B']['I_3_regime_first']}->"
          f"{out['summary_B']['I_3_regime_last']}")
    print(f"[ksoft_kact] recommendation: {out['recommendation']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
