"""op_resolution_nq_g3_1_epsilon_stability.py — NQ-G3-1 ε-stability sweep.

Status: working diagnostic. NON-canonical. Does not modify any canonical or
existing working file. Empirical re-run of l1i_constants_feasibility under
multiple ε thresholds.

NQ-G3-1 (per `THEORY/logs/daily/2026-05-04/op_resolution.md` §11):
  Question: how does the L1-I FEASIBLE_WITH_BUDGET fraction change under ε
  perturbations? Specifically: f(ε) = |FEASIBLE_WITH_BUDGET(ε)| / 1920 for
  ε ∈ {0.001, 0.05, 0.10, 0.15, 0.225, 0.30, 0.50, 1.0, 5.0, 25.0, 29.99,
       30.0, 30.01, 35.0}.

Theoretical pre-analysis (§11.3):
  ε determines the active set A^ε = {j : ‖u^(j)‖_1 > ε}. For the canonical
  L1-I configuration (initial_masses = (30, 30, 30, 0)) under wq1 mass-
  projection, post-projection masses are (30, 30, 30, 0) exactly. Therefore:
    - ε ∈ (0, 30): n_active = 3, identical active set across ε → identical
                    feasibility chain → identical 439/1920 FEASIBLE.
    - ε ≥ 30:      n_active = 0 (strict comparison m > ε at line 279 of
                    l1i_constants_feasibility.py), all configs INCONCLUSIVE.
  Predicted f(ε) is **piecewise constant**: 22.9% on (0, 30); 0% on [30, ∞).

Difference from NQ-G1-2 post-processing wrapper (CHANGELOG 13th addendum):
  NQ-G1-2 changed budget thresholds applied to *stored* margins → JSON post-
  processing was equivalent to fresh full re-run.
  NQ-G3-1 changes ε which determines the active set, which changes which
  sites are X_bg, which changes LG-4 measurement, etc. The entire feasibility
  chain re-computes per ε. So we run l1i.compute_feasibility for each ε.
  This is essentially "Phase B" (fresh-full-run) per op_resolution.md §11.5
  step 2; "Phase A" (post-processing) is structurally inapplicable here.

Output:
  - JSON sweep report at scripts/results/op_resolution_nq_g3_1_epsilon_stability.json
  - Console summary

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py

Forbidden non-claims (preserved from l1i_constants_feasibility.py):
  - L1_proved: False
  - L1F_promoted_to_Cat_A: False (T-L1-F is conditional on L1-J regime)
  - L1H_promoted_to_Cat_A: False
  - OP_0005_solved: False
  - OP_0008_solved: False
  - K_bar_equals_K_act_globally: False
  - K_soft_equals_K_act_globally: False
  - sigma_rich_sufficient: False
  - reservoir_canonical: False
  - feasibility_is_theorem_proof: False
  - This experiment does not change Cat A conditional status of T-L1-M.
  - This experiment does not modify Commitment 16 ε-convention.
"""
from __future__ import annotations

import json
import os
import platform
import socket
import sys
import time
from typing import Any, Dict, List, Tuple

# Make CODE/ importable so `from scripts.l1i_constants_feasibility import ...`
# works regardless of cwd.
HERE = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.dirname(HERE)
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

import numpy as np  # noqa: E402

from scripts.l1i_constants_feasibility import (  # noqa: E402
    FeasibilityResult,
    aggregate_results,
    compute_feasibility,
    feas_result_to_dict,
    make_full_sweep,
    INCONCLUSIVE,
)

SCRIPT_VERSION = "0.1.0"

OUTPUT_JSON = os.path.join(HERE, "results", "op_resolution_nq_g3_1_epsilon_stability.json")

# ε sweep — covers below baseline, baseline, interior, boundary transition,
# and above-boundary. Per §11.3 pre-analysis, expected piecewise-constant
# transition at ε = 30 (post-projection mass of active slots).
EPSILON_SWEEP: Tuple[float, ...] = (
    0.001,   # very small (residual probe)
    0.05,    # below baseline
    0.10,
    0.15,
    0.225,   # baseline (matches l1i hard-coded default)
    0.30,
    0.50,
    1.0,
    5.0,
    25.0,    # interior, near boundary
    29.99,   # just below transition
    30.0,    # at transition (strict comparison m > ε; m = 30 fails)
    30.01,   # just above
    35.0,    # well above
)

# Canonical l1i parameters (mirror line 604–612 of l1i_constants_feasibility.py)
BASE_CENTERS_A: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 14))
BASE_CENTERS_B: Tuple[Tuple[int, int], ...] = ((5, 5), (15, 5), (10, 11))
BASE_CENTERS_WIDE: Tuple[Tuple[int, int], ...] = ((3, 3), (13, 3), (8, 13))
N_TORUS = 20
M_TOTAL = 90.0
INITIAL_MASSES: Tuple[float, ...] = (30.0, 30.0, 30.0, 0.0)
DEFAULT_BUDGET = 0.05
BRIDGE_MAX_PAIRS = 6


def run_sweep_at_epsilon(
    cfgs: List[Any],
    epsilon: float,
    budget: float,
) -> List[FeasibilityResult]:
    """Run l1i.compute_feasibility for all configs at a fixed ε."""
    results: List[FeasibilityResult] = []
    for cfg in cfgs:
        try:
            r = compute_feasibility(
                cfg, BASE_CENTERS_A, BASE_CENTERS_B, BASE_CENTERS_WIDE,
                n_torus=N_TORUS, M_total=M_TOTAL,
                initial_masses=INITIAL_MASSES, epsilon=epsilon,
                budget=budget, bridge_max_pairs=BRIDGE_MAX_PAIRS,
            )
        except Exception as e:
            r = FeasibilityResult(
                config=cfg, n_active=0, h_min_measured=None,
                lg1_disjoint=None, lg1_overlap_count=0,
                boundary_collars={}, lg2_min_margin=None, lg2_pass=None,
                bridge_heights={}, lg3_min_margin=None, lg3_pass=None,
                bg_max_U=None, bg_size=0,
                lg4_margin=None, lg4_pass=None,
                slot_l2={}, h6_min_margin=None, h6_pass=None,
                max_bridge=None, ledger_margin=None, ledger_pass=None,
                feasibility_class=INCONCLUSIVE,
                failing_clauses=["exception"],
                notes=[f"compute_feasibility raised: {type(e).__name__}: {e}"],
            )
        results.append(r)
    return results


def main() -> int:
    cfgs = make_full_sweep()
    n_cfgs = len(cfgs)
    print(f"[nq-g3-1] Sweeping ε across {len(EPSILON_SWEEP)} values "
          f"× {n_cfgs} configs = {len(EPSILON_SWEEP) * n_cfgs} total runs.")

    t0 = time.time()
    per_eps_results: Dict[float, Dict[str, Any]] = {}

    for eps in EPSILON_SWEEP:
        t_eps = time.time()
        results = run_sweep_at_epsilon(cfgs, eps, DEFAULT_BUDGET)
        wall_eps = time.time() - t_eps

        from collections import Counter
        n_act_dist = Counter(r.n_active for r in results)
        fc_dist = Counter(r.feasibility_class for r in results)

        feasible_with_budget = fc_dist.get("FEASIBLE_WITH_BUDGET", 0)
        per_eps_results[eps] = {
            "epsilon": eps,
            "wall_seconds": wall_eps,
            "n_configs": n_cfgs,
            "n_active_distribution": dict(n_act_dist),
            "feasibility_class_distribution": dict(fc_dist),
            "feasible_with_budget": feasible_with_budget,
            "feasible_fraction": feasible_with_budget / n_cfgs,
        }

        print(f"[nq-g3-1] ε={eps:8.4f}  n_active_dist={dict(n_act_dist)}  "
              f"FEASIBLE_WITH_BUDGET={feasible_with_budget:4d}/{n_cfgs}  "
              f"({100.0 * feasible_with_budget / n_cfgs:5.2f}%)  "
              f"[{wall_eps:5.1f}s]")

    total_wall = time.time() - t0

    # Verify §11.3 prediction
    baseline_eps = 0.225
    baseline_feasible = per_eps_results[baseline_eps]["feasible_with_budget"]
    boundary_below = per_eps_results[29.99]["feasible_with_budget"]
    boundary_at = per_eps_results[30.0]["feasible_with_budget"]
    boundary_above = per_eps_results[30.01]["feasible_with_budget"]

    prediction_holds_below = all(
        per_eps_results[e]["feasible_with_budget"] == baseline_feasible
        for e in EPSILON_SWEEP if e < 30.0
    )
    prediction_holds_above = all(
        per_eps_results[e]["feasible_with_budget"] == 0
        for e in EPSILON_SWEEP if e >= 30.0
    )
    piecewise_constant_verdict = prediction_holds_below and prediction_holds_above

    out = {
        "script": "op_resolution_nq_g3_1_epsilon_stability.py",
        "script_version": SCRIPT_VERSION,
        "purpose": ("NQ-G3-1 ε-stability sweep over the L1-I 1920-config baseline. "
                    "Verifies §11.3 piecewise-constant prediction: f(ε) ≈ 22.9% on "
                    "ε ∈ (0, 30); 0% on ε ≥ 30."),
        "non_claims": {
            "L1_proved": False,
            "L1F_promoted_to_Cat_A": False,
            "L1H_promoted_to_Cat_A": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "K_bar_equals_K_act_globally": False,
            "K_soft_equals_K_act_globally": False,
            "sigma_rich_sufficient": False,
            "reservoir_canonical": False,
            "feasibility_is_theorem_proof": False,
            "Commitment_16_modified": False,
            "T_L1_M_status_modified": False,
            "Commitment_16_epsilon_promoted_to_axiom": False,
        },
        "config": {
            "n_torus": N_TORUS,
            "M_total": M_TOTAL,
            "initial_masses": list(INITIAL_MASSES),
            "epsilon_sweep": list(EPSILON_SWEEP),
            "centers_A": [list(c) for c in BASE_CENTERS_A],
            "centers_B": [list(c) for c in BASE_CENTERS_B],
            "budget_threshold": DEFAULT_BUDGET,
            "bridge_max_pairs": BRIDGE_MAX_PAIRS,
            "n_configs_per_epsilon": n_cfgs,
            "state_mode_per_config": "wq1 or raw_gaussian per FeasibilityConfig.state_mode",
        },
        "per_epsilon_results": {
            f"{eps}": per_eps_results[eps] for eps in EPSILON_SWEEP
        },
        "verdict": {
            "baseline_epsilon": baseline_eps,
            "baseline_feasible_with_budget": baseline_feasible,
            "boundary_29_99": boundary_below,
            "boundary_30_00": boundary_at,
            "boundary_30_01": boundary_above,
            "prediction_holds_below_30": prediction_holds_below,
            "prediction_holds_above_30": prediction_holds_above,
            "piecewise_constant_verdict": piecewise_constant_verdict,
            "piecewise_constant_threshold": 30.0,
            "interpretation": (
                "If piecewise_constant_verdict is True, §11.3 theoretical "
                "prediction is empirically confirmed: f(ε) is constant at "
                f"{baseline_feasible}/1920 on ε ∈ (0, 30) and 0/1920 on "
                "ε ≥ 30. NQ-G3-1 closure verdict: ✅ EXECUTED with "
                "prediction confirmed."
            ),
        },
        "wall_clock_seconds_total": total_wall,
        "metadata": {
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }

    os.makedirs(os.path.dirname(os.path.abspath(OUTPUT_JSON)), exist_ok=True)
    with open(OUTPUT_JSON, "w") as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: int(o) if isinstance(o, np.integer)
                  else (float(o) if isinstance(o, np.floating)
                        else (o.tolist() if isinstance(o, np.ndarray) else str(o))))

    print()
    print(f"[nq-g3-1] Wrote {OUTPUT_JSON}")
    print(f"[nq-g3-1] Total wall-clock: {total_wall:.1f}s "
          f"({len(EPSILON_SWEEP)} ε values × {n_cfgs} configs)")
    print(f"[nq-g3-1] Verdict: piecewise_constant_verdict = {piecewise_constant_verdict}")
    print(f"[nq-g3-1]   prediction_holds_below_30 = {prediction_holds_below}")
    print(f"[nq-g3-1]   prediction_holds_above_30 = {prediction_holds_above}")
    print(f"[nq-g3-1]   baseline ε=0.225 → {baseline_feasible}/{n_cfgs} "
          f"({100.0 * baseline_feasible / n_cfgs:.2f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
