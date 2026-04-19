#!/usr/bin/env python3
"""Exp65: formation tracking along the K=2 mass-transfer direction.

This experiment continues the exp62/exp63 gap analysis.  exp62 measures a
global reduced energy curve while exp63 measures a local K=2 trajectory; their
opposite F'' signs suggest that the optimizer moves among distinct K=2
configuration types.  Exp65 records the missing spatial data: centers,
separation, orientation, overlap, regime, and swap events as mass is
transferred between the two fields.

Outputs:
  - experiments/results/exp65_formation_tracking.json
  - experiments/results/exp65_formation_tracking.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scc.graph import GraphState
from scc.multi import (
    classify_regime,
    coupling_strength,
    find_k_formations,
    formation_overlap,
    inter_formation_distances,
    soft_overlap_weight,
)
from scc.optimizer import project_volume
from scc.params import ParameterRegistry


DEFAULT_EPSILONS = [-3.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0]


@dataclass
class TrackingRow:
    config: str
    grid_size: int
    n: int
    c_ref: float
    epsilon: float
    mass1: float
    mass2: float
    x1: float
    y1: float
    x2: float
    y2: float
    pair_mid_x: float
    pair_mid_y: float
    center_offset: float
    center_offset_norm: float
    d_c: float
    theta: float
    theta_mod_pi: float
    delta_theta_mod_pi: float
    hard_overlap: float
    soft_overlap: float
    d_min: float
    lambda_coupling: float
    regime_lambda: str
    regime_geometric: str
    total_energy: float
    swap_from_previous: bool
    elapsed_s: float


def grid_coordinates(grid_size: int) -> tuple[np.ndarray, np.ndarray]:
    """Return x/y coordinates for row-major grid indices."""
    y, x = np.divmod(np.arange(grid_size * grid_size), grid_size)
    return x.astype(float), y.astype(float)


def center_of_mass(u: np.ndarray, grid_size: int) -> tuple[float, float]:
    """Compute center of mass in grid coordinates."""
    x, y = grid_coordinates(grid_size)
    mass = float(np.sum(u))
    if mass <= 1e-12:
        return float("nan"), float("nan")
    return float(np.dot(x, u) / mass), float(np.dot(y, u) / mass)


def angle_mod_pi(theta: float) -> float:
    """Map an unoriented line angle to [-pi/2, pi/2)."""
    return float(((theta + math.pi / 2) % math.pi) - math.pi / 2)


def angle_diff_mod_pi(theta: float, theta_ref: float) -> float:
    """Smallest difference between two unoriented line angles."""
    return angle_mod_pi(theta - theta_ref)


def total_k_energy_from_results(results, lambda_rep: float, lambda_bar: float) -> float:
    fields = [r.u for r in results]
    total = float(sum(r.energy for r in results))
    for j in range(len(fields)):
        for k in range(j + 1, len(fields)):
            total += lambda_rep * float(np.dot(fields[j], fields[k]))
    simplex = np.maximum(0.0, sum(fields) - 1.0)
    total += lambda_bar * float(np.dot(simplex, simplex))
    return total


def is_swap(
    previous: tuple[tuple[float, float], tuple[float, float]] | None,
    current: tuple[tuple[float, float], tuple[float, float]],
) -> bool:
    """Detect whether labels appear swapped relative to the previous row."""
    if previous is None:
        return False
    (px1, py1), (px2, py2) = previous
    (cx1, cy1), (cx2, cy2) = current
    same = math.hypot(cx1 - px1, cy1 - py1) + math.hypot(cx2 - px2, cy2 - py2)
    crossed = math.hypot(cx1 - px2, cy1 - py2) + math.hypot(cx2 - px1, cy2 - py1)
    return crossed + 1e-9 < same


def parse_config(config: str) -> tuple[int, float]:
    """Parse CONFIG strings like '15x15:0.5' or '15:0.5'."""
    left, right = config.split(":", 1)
    if "x" in left:
        side = int(left.lower().split("x", 1)[0])
    else:
        side = int(left)
    return side, float(right)


def run_config(
    grid_size: int,
    c_ref: float,
    epsilons: Iterable[float],
    lambda_rep: float,
    lambda_bar: float,
    n_restarts: int,
    max_iter: int,
    verbose: bool,
) -> dict:
    """Run formation tracking for one grid/c_ref configuration."""
    n = grid_size * grid_size
    total_mass = c_ref * n
    half_mass = total_mass / 2.0
    c_half = half_mass / n
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(volume_fraction=c_half)
    grid_center = ((grid_size - 1) / 2.0, (grid_size - 1) / 2.0)

    print(f"\n{'=' * 80}")
    print(f"exp65 config: {grid_size}x{grid_size}, c_ref={c_ref}, c_half={c_half:.4f}")
    print(f"{'=' * 80}")

    t0 = time.time()
    base_results = find_k_formations(
        graph,
        params,
        K=2,
        lambda_rep=lambda_rep,
        lambda_bar=lambda_bar,
        n_restarts=n_restarts,
        max_iter=max_iter,
        verbose=verbose,
    )
    base_fields = [r.u.copy() for r in base_results]
    base_energy = total_k_energy_from_results(base_results, lambda_rep, lambda_bar)
    base_coms = [center_of_mass(u, grid_size) for u in base_fields]
    base_theta = math.atan2(
        base_coms[1][1] - base_coms[0][1],
        base_coms[1][0] - base_coms[0][0],
    )
    base_theta_mod = angle_mod_pi(base_theta)
    print(
        f"base K=2: E={base_energy:.6f}, "
        f"COM1=({base_coms[0][0]:.2f},{base_coms[0][1]:.2f}), "
        f"COM2=({base_coms[1][0]:.2f},{base_coms[1][1]:.2f})"
    )

    rows: list[TrackingRow] = []
    prev_coms = None

    for eps in epsilons:
        row_t0 = time.time()
        m1 = half_mass + eps
        m2 = half_mass - eps
        if m1 <= 0 or m2 <= 0:
            print(f"  eps={eps:+.2f}: skipped invalid masses")
            continue

        init_fields = [
            project_volume(base_fields[0] + eps * np.ones(n) / n, m1),
            project_volume(base_fields[1] - eps * np.ones(n) / n, m2),
        ]

        results = find_k_formations(
            graph,
            params,
            K=2,
            lambda_rep=lambda_rep,
            lambda_bar=lambda_bar,
            m_per_formation=[m1 / n, m2 / n],
            n_restarts=max(1, min(n_restarts, 3)),
            max_iter=max_iter,
            verbose=False,
            init_fields=init_fields,
        )
        fields = [r.u for r in results]
        (x1, y1), (x2, y2) = [center_of_mass(u, grid_size) for u in fields]
        pair_mid_x = (x1 + x2) / 2.0
        pair_mid_y = (y1 + y2) / 2.0
        center_offset = math.hypot(pair_mid_x - grid_center[0], pair_mid_y - grid_center[1])
        d_c = math.hypot(x2 - x1, y2 - y1)
        theta = math.atan2(y2 - y1, x2 - x1)
        theta_m = angle_mod_pi(theta)
        delta_theta = angle_diff_mod_pi(theta_m, base_theta_mod)

        hard_O = formation_overlap(fields)
        soft_O = soft_overlap_weight(fields)
        dists = inter_formation_distances(fields, graph)
        regime_geo = classify_regime(fields, graph, params, lambda_rep, method="geometric")
        cpl = coupling_strength(fields, graph, params, lambda_rep)
        regime_lambda = str(cpl["predicted_regime"])
        total_energy = total_k_energy_from_results(results, lambda_rep, lambda_bar)

        current_coms = ((x1, y1), (x2, y2))
        swapped = is_swap(prev_coms, current_coms)
        prev_coms = current_coms

        row = TrackingRow(
            config=f"{grid_size}x{grid_size}_c{c_ref}",
            grid_size=grid_size,
            n=n,
            c_ref=c_ref,
            epsilon=float(eps),
            mass1=float(np.sum(fields[0])),
            mass2=float(np.sum(fields[1])),
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            pair_mid_x=float(pair_mid_x),
            pair_mid_y=float(pair_mid_y),
            center_offset=float(center_offset),
            center_offset_norm=float(center_offset / max(grid_size - 1, 1)),
            d_c=float(d_c),
            theta=float(theta),
            theta_mod_pi=float(theta_m),
            delta_theta_mod_pi=float(delta_theta),
            hard_overlap=float(hard_O[0, 1]),
            soft_overlap=float(soft_O[0, 1]),
            d_min=float(dists[0, 1]),
            lambda_coupling=float(cpl["Lambda"]),
            regime_lambda=regime_lambda,
            regime_geometric=regime_geo,
            total_energy=float(total_energy),
            swap_from_previous=swapped,
            elapsed_s=float(time.time() - row_t0),
        )
        rows.append(row)
        print(
            f"  eps={eps:+5.1f} E={total_energy:9.4f} "
            f"d_c={d_c:5.2f} center={row.center_offset_norm:5.3f} "
            f"Λ={row.lambda_coupling:8.2e} {regime_lambda:<18} "
            f"swap={str(swapped):<5} ({row.elapsed_s:.1f}s)"
        )

    summary = summarize_config(rows, base_energy, time.time() - t0)
    return {
        "config": f"{grid_size}x{grid_size}_c{c_ref}",
        "grid_size": grid_size,
        "n": n,
        "c_ref": c_ref,
        "c_half": c_half,
        "lambda_rep": lambda_rep,
        "lambda_bar": lambda_bar,
        "n_restarts": n_restarts,
        "max_iter": max_iter,
        "base_energy": float(base_energy),
        "base_coms": [{"x": x, "y": y} for x, y in base_coms],
        "summary": summary,
        "rows": [asdict(r) for r in rows],
    }


def summarize_config(rows: list[TrackingRow], base_energy: float, elapsed_s: float) -> dict:
    if not rows:
        return {"elapsed_s": elapsed_s}

    center_offsets = np.array([r.center_offset_norm for r in rows], dtype=float)
    separations = np.array([r.d_c for r in rows], dtype=float)
    overlaps = np.array([r.soft_overlap for r in rows], dtype=float)
    lambdas = np.array([r.lambda_coupling for r in rows], dtype=float)
    swaps = int(sum(r.swap_from_previous for r in rows))

    # Energy asymmetry: mean E(eps>0) - mean E(eps<0), matching 04-07 docs.
    e_pos = [r.total_energy for r in rows if r.epsilon > 0]
    e_neg = [r.total_energy for r in rows if r.epsilon < 0]
    energy_asymmetry = float(np.mean(e_pos) - np.mean(e_neg)) if e_pos and e_neg else float("nan")

    # Conservative type labels; do not overclaim when signals conflict.
    mean_center = float(np.mean(center_offsets))
    max_center = float(np.max(center_offsets))
    max_rotation = float(np.max(np.abs([r.delta_theta_mod_pi for r in rows])))
    if max_center < 0.08 and swaps == 0 and max_rotation < 0.35:
        type_label = "Type A candidate (centered/stable)"
    elif max_center > 0.12 or swaps > 0 or max_rotation > 0.75:
        type_label = "Type B candidate (off-center/swap-prone)"
    else:
        type_label = "Mixed/ambiguous"

    return {
        "elapsed_s": float(elapsed_s),
        "base_energy": float(base_energy),
        "energy_asymmetry_pos_minus_neg": energy_asymmetry,
        "mean_center_offset_norm": mean_center,
        "max_center_offset_norm": max_center,
        "mean_separation": float(np.mean(separations)),
        "min_separation": float(np.min(separations)),
        "max_separation": float(np.max(separations)),
        "mean_soft_overlap": float(np.mean(overlaps)),
        "max_soft_overlap": float(np.max(overlaps)),
        "mean_lambda_coupling": float(np.mean(lambdas)),
        "max_lambda_coupling": float(np.max(lambdas)),
        "swap_count": swaps,
        "max_abs_delta_theta_mod_pi": max_rotation,
        "type_label": type_label,
    }


def write_outputs(results: list[dict], json_path: Path, csv_path: Path) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump({"experiment": "exp65_formation_tracking", "results": results}, f, indent=2)

    rows = [row for result in results for row in result["rows"]]
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Exp65 formation tracking")
    parser.add_argument(
        "--configs",
        nargs="+",
        default=["15x15:0.5", "15x15:0.6", "20x20:0.5", "20x20:0.6"],
        help="Configs as SIDE: c_ref, e.g. 15x15:0.5",
    )
    parser.add_argument("--epsilons", nargs="+", type=float, default=DEFAULT_EPSILONS)
    parser.add_argument("--lambda-rep", type=float, default=10.0)
    parser.add_argument("--lambda-bar", type=float, default=100.0)
    parser.add_argument("--n-restarts", type=int, default=4)
    parser.add_argument("--max-iter", type=int, default=1500)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=REPO_ROOT / "experiments/results/exp65_formation_tracking.json",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=REPO_ROOT / "experiments/results/exp65_formation_tracking.csv",
    )
    args = parser.parse_args()

    all_results = []
    for cfg in args.configs:
        grid_size, c_ref = parse_config(cfg)
        all_results.append(
            run_config(
                grid_size=grid_size,
                c_ref=c_ref,
                epsilons=args.epsilons,
                lambda_rep=args.lambda_rep,
                lambda_bar=args.lambda_bar,
                n_restarts=args.n_restarts,
                max_iter=args.max_iter,
                verbose=args.verbose,
            )
        )

    write_outputs(all_results, args.output_json, args.output_csv)
    print(f"\nSaved JSON: {args.output_json}")
    print(f"Saved CSV:  {args.output_csv}")

    print("\nSummary:")
    for result in all_results:
        s = result["summary"]
        print(
            f"  {result['config']}: {s['type_label']}; "
            f"center_mean={s['mean_center_offset_norm']:.3f}, "
            f"swaps={s['swap_count']}, "
            f"E_asym={s['energy_asymmetry_pos_minus_neg']:+.4f}, "
            f"Λ_max={s['max_lambda_coupling']:.2e}"
        )


if __name__ == "__main__":
    main()
