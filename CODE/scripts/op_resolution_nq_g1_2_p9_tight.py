"""op_resolution_nq_g1_2_p9_tight.py — NQ-G1-2 (P9-tight) regime experiment.

Status: working diagnostic. NON-canonical. Does not modify any canonical or
existing working file. Empirical post-processing only.

NQ-G1-2 (per `THEORY/logs/daily/2026-05-04/op_resolution.md` §10):
  Original L1-J P9: ‖R_j‖_∞ ≤ ρ_pert / 2.
  (P9-tight) variant: ‖R_j‖_∞ ≤ ρ_pert / 4.
  Under (P9-tight), the Type-N bottleneck-stability shift bound tightens to use
  ρ_pert / 2 instead of ρ_pert, expanding τ_*^post-R2 and enabling factor-1
  sharpening in R-1's perturbation argument.

  Question: in the L1-I FEASIBLE_WITH_BUDGET set (439/1920 baseline at
  budget=0.05), how many configurations also satisfy the (P9-tight) regime
  empirically?

Interpretation in l1i terms (per op_resolution.md §10.3-§10.4 step 2):
  The l1i script's H6' clause checks `l_min - max_l2 ≥ budget`. The 0.05 default
  budget is interpreted as `3·ρ_pert` (i.e., ρ_pert ≈ 0.0167). Under (P9-tight)
  with ρ_pert' = ρ_pert / 2, the corresponding H6' margin requirement halves
  from 0.05 (= 3·ρ_pert) to 0.025 (= 3·ρ_pert / 2 = 1.5·ρ_pert).

  This script re-classifies the existing baseline JSON
  (`scripts/results/l1i_constants_feasibility.json`, 1920 configs, all margins
  recorded) under multiple budget regimes WITHOUT re-running the expensive
  feasibility computation.

Regimes tested:
  R0 standard           : all-clause budget = 0.05  (baseline 439/1920)
  R1 P9-tight H6-only   : all-clause budget = 0.05, H6 budget = 0.025 (faithful
                          to op_resolution.md §10.4 step 2; only H6' margin
                          requirement halved per ρ_pert' = ρ_pert/2)
  R2 P9-tight all-halved: all-clause budget = 0.025                  (stronger
                          relaxation; if all margins inherit ρ_pert scaling)
  R3 H6-doubled         : all-clause budget = 0.05, H6 budget = 0.10 (sanity
                          check: how many configs survive a stricter H6')
  R4 all-doubled        : all-clause budget = 0.10                    (sanity)

Outputs:
  - JSON comparison report at scripts/results/op_resolution_nq_g1_2_p9_tight.json
  - Console summary

Usage::

    PYTHONPATH=CODE python3 CODE/scripts/op_resolution_nq_g1_2_p9_tight.py

Forbidden non-claims (preserved):
  - L1-J' regime is not promoted to canonical.
  - (P9-tight) is not adopted as the canonical regime.
  - Factor-1 sharpening for Lemma L-M-2 §5.4 R-1 is not claimed.
  - This experiment does not change Cat A conditional status of T-L1-M.
  - OP-0005 / OP-0008 / OP-0009 are not affected.

This script is a follow-on to:
  - `op_resolution_nq_g3_3_kact_epsilon.py` (NQ-G3-3 K_act ε perturbation)
"""
from __future__ import annotations

import json
import os
import platform
import socket
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

SCRIPT_VERSION = "0.1.0"

BASELINE_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "results",
    "l1i_constants_feasibility.json",
)
OUTPUT_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "results",
    "op_resolution_nq_g1_2_p9_tight.json",
)

# Match l1i constants
MARGINAL_TOL = 0.01
FEASIBLE_WITH_BUDGET = "FEASIBLE_WITH_BUDGET"
RAW_FEASIBLE = "RAW_FEASIBLE"
MARGINAL = "MARGINAL"
INFEASIBLE = "INFEASIBLE"
INCONCLUSIVE = "INCONCLUSIVE"


def reclassify_one(
    result: Dict[str, Any],
    *,
    budget: float,
    h6_budget: Optional[float] = None,
) -> str:
    """Re-classify a single l1i result under given (budget, h6_budget).

    Mirrors the classification logic in l1i_constants_feasibility.compute_feasibility
    (lines 423-470) but with a per-clause H6 budget override.

    If h6_budget is None, H6 inherits the global `budget`.
    """
    if h6_budget is None:
        h6_budget = budget

    failing: List[str] = []
    margins: List[float] = []
    h6_margin: Optional[float] = None

    # Aggregate margins / failure flags per clause, mirroring l1i lines 424-449
    if result.get("lg1_disjoint") is False:
        failing.append("LG-1")
    if result.get("lg2_pass") is False:
        failing.append("LG-2")
    if result.get("lg2_min_margin") is not None:
        margins.append(float(result["lg2_min_margin"]))
    if result.get("lg3_pass") is False:
        failing.append("LG-3")
    if result.get("lg3_min_margin") is not None:
        margins.append(float(result["lg3_min_margin"]))
    if result.get("lg4_pass") is False:
        failing.append("LG-4")
    if result.get("lg4_margin") is not None:
        margins.append(float(result["lg4_margin"]))
    if result.get("h6_pass") is False:
        failing.append("H6")
    if result.get("h6_min_margin") is not None:
        h6_margin = float(result["h6_min_margin"])
        margins.append(h6_margin)
    if result.get("ledger_pass") is False:
        failing.append("ledger")
    if result.get("ledger_margin") is not None:
        margins.append(float(result["ledger_margin"]))

    # Inconclusive if no margins to evaluate (insufficient data)
    if not margins:
        return INCONCLUSIVE

    # Hard fail: any clause-level pass is False
    if failing:
        return INFEASIBLE

    worst = min(margins)

    # MARGINAL: any margin slightly below 0
    if worst < -MARGINAL_TOL:
        return INFEASIBLE
    if worst < 0:
        return MARGINAL

    # Determine FEASIBLE_WITH_BUDGET: all clauses pass `budget` AND H6 passes h6_budget
    non_h6_margins = [m for m in margins if m is not h6_margin]
    if non_h6_margins:
        non_h6_min = min(non_h6_margins)
    else:
        non_h6_min = float("inf")

    h6_ok = (h6_margin is None) or (h6_margin >= h6_budget)
    non_h6_ok = non_h6_min >= budget

    if h6_ok and non_h6_ok:
        return FEASIBLE_WITH_BUDGET

    return RAW_FEASIBLE


def reclassify_all(
    baseline_results: List[Dict[str, Any]],
    *,
    budget: float,
    h6_budget: Optional[float] = None,
) -> Dict[str, int]:
    """Re-classify every result and return class-count summary."""
    counts: Dict[str, int] = {
        FEASIBLE_WITH_BUDGET: 0,
        RAW_FEASIBLE: 0,
        MARGINAL: 0,
        INFEASIBLE: 0,
        INCONCLUSIVE: 0,
    }
    for r in baseline_results:
        cls = reclassify_one(r, budget=budget, h6_budget=h6_budget)
        counts[cls] = counts.get(cls, 0) + 1
    return counts


def regime_label(name: str, budget: float, h6_budget: Optional[float]) -> str:
    if h6_budget is None or h6_budget == budget:
        return f"{name}: budget={budget:.4f} (uniform)"
    return f"{name}: budget={budget:.4f}, h6_budget={h6_budget:.4f}"


def main() -> int:
    if not os.path.isfile(BASELINE_JSON):
        print(f"[NQ-G1-2] ERROR: baseline JSON not found at {BASELINE_JSON}",
              file=sys.stderr)
        print("Run l1i_constants_feasibility.py with --mode full first.",
              file=sys.stderr)
        return 1

    with open(BASELINE_JSON, "r") as fh:
        baseline = json.load(fh)

    n_configs = len(baseline["results"])
    baseline_budget = baseline.get("config", {}).get("budget_threshold", 0.05)

    # Define regimes per docstring
    regimes: List[Tuple[str, float, Optional[float], str]] = [
        ("R0_standard", 0.05, None,
         "Baseline: all-clause budget = 0.05 (matches T-L1-F empirical anchor)"),
        ("R1_p9tight_h6only", 0.05, 0.025,
         "P9-tight (faithful, op_resolution.md §10.4 step 2): only H6 margin halved (ρ_pert/2 in H6)"),
        ("R2_p9tight_all", 0.025, None,
         "P9-tight (strong): all-clause budget halved (if all margins inherit ρ_pert scaling)"),
        ("R3_h6doubled", 0.05, 0.10,
         "Sanity (H6 doubled): only H6 margin doubled (stricter perturbation absorption)"),
        ("R4_all_doubled", 0.10, None,
         "Sanity (all doubled): all-clause budget doubled"),
    ]

    t0 = time.time()
    regime_results: List[Dict[str, Any]] = []
    for name, budget, h6_budget, descr in regimes:
        counts = reclassify_all(baseline["results"], budget=budget, h6_budget=h6_budget)
        feasible = counts.get(FEASIBLE_WITH_BUDGET, 0)
        regime_results.append({
            "name": name,
            "description": descr,
            "budget": budget,
            "h6_budget": h6_budget,
            "counts": counts,
            "feasible_with_budget": feasible,
            "feasible_fraction": feasible / n_configs,
            "label": regime_label(name, budget, h6_budget),
        })
    wall = time.time() - t0

    # Cross-regime overlap analysis: which configs FEASIBLE in R0 are still FEASIBLE in R1?
    r0_feasible_idx = set()
    r1_feasible_idx = set()
    r2_feasible_idx = set()
    r3_feasible_idx = set()
    for i, r in enumerate(baseline["results"]):
        if reclassify_one(r, budget=0.05, h6_budget=None) == FEASIBLE_WITH_BUDGET:
            r0_feasible_idx.add(i)
        if reclassify_one(r, budget=0.05, h6_budget=0.025) == FEASIBLE_WITH_BUDGET:
            r1_feasible_idx.add(i)
        if reclassify_one(r, budget=0.025, h6_budget=None) == FEASIBLE_WITH_BUDGET:
            r2_feasible_idx.add(i)
        if reclassify_one(r, budget=0.05, h6_budget=0.10) == FEASIBLE_WITH_BUDGET:
            r3_feasible_idx.add(i)

    overlap = {
        "r0_only": len(r0_feasible_idx - r1_feasible_idx),
        "r0_and_r1": len(r0_feasible_idx & r1_feasible_idx),
        "r1_only": len(r1_feasible_idx - r0_feasible_idx),
        "r0_subset_of_r1": r0_feasible_idx.issubset(r1_feasible_idx),
        "r0_subset_of_r2": r0_feasible_idx.issubset(r2_feasible_idx),
        "r3_subset_of_r0": r3_feasible_idx.issubset(r0_feasible_idx),
        "r1_minus_r0_size": len(r1_feasible_idx - r0_feasible_idx),
        "r2_minus_r0_size": len(r2_feasible_idx - r0_feasible_idx),
        "r0_minus_r3_size": len(r0_feasible_idx - r3_feasible_idx),
    }

    out: Dict[str, Any] = {
        "script": "op_resolution_nq_g1_2_p9_tight.py",
        "script_version": SCRIPT_VERSION,
        "purpose": (
            "NQ-G1-2 (P9-tight) regime empirical study: re-classify L1-I "
            "FEASIBLE_WITH_BUDGET configurations under (P9-tight) interpretation "
            "where ρ_pert halves and H6' margin requirement halves accordingly."
        ),
        "non_claims": {
            "L1J_prime_promoted_to_canonical": False,
            "P9_tight_adopted_as_canonical_regime": False,
            "factor_1_sharpening_for_LM2_R1": False,
            "TL1M_Cat_A_conditional_status_changed": False,
            "OP_0005_solved": False,
            "OP_0008_solved": False,
            "OP_0009_resolved": False,
        },
        "baseline_source": BASELINE_JSON,
        "baseline_summary": baseline.get("summary", {}),
        "n_configs": n_configs,
        "regimes": regime_results,
        "overlap": overlap,
        "interpretation_notes": [
            "Baseline R0 = 439/1920 FEASIBLE_WITH_BUDGET matches T-L1-F empirical anchor.",
            "R1 (P9-tight H6-only halved) is the faithful translation of op_resolution.md §10.4 step 2.",
            "R0 ⊆ R1 expected since H6 margin requirement is relaxed (≤ 0.05 → ≤ 0.025).",
            "R2 (all-clause halved) is a stronger relaxation; tests whether other margins also inherit ρ_pert scaling.",
            "R3 (H6 doubled) inverts: how restrictive is a tighter H6 alone? r3_subset_of_r0 expected True.",
            "Per op_resolution.md §10.4 step 6 verdict: if R1 (or R2) feasible count > 200/1920, "
            "(P9-tight) is candidate for L1-J' regime promotion enabling factor-1 sharpening.",
            "Per step 5: if R1 < 50/1920, (P9-tight) regime too restrictive; (P9) standard stays.",
            "Cat A conditional status of T-L1-M is unaffected regardless of outcome — this experiment "
            "informs whether factor-1 sharpening is empirically supportable, not whether L-M is correct.",
        ],
        "wall_clock_seconds": wall,
        "metadata": {
            "host": socket.gethostname(),
            "python_version": platform.python_version(),
            "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w") as fh:
        json.dump(out, fh, indent=2)

    # Console summary
    print(f"[NQ-G1-2] Wrote {OUTPUT_JSON}")
    print(f"[NQ-G1-2] Re-classified {n_configs} configs in {wall:.3f}s (no re-computation).")
    print()
    print(f"{'Regime':<24}{'Budget':<12}{'H6 budget':<12}{'FEASIBLE':<12}{'Fraction':<10}")
    print("-" * 70)
    for r in regime_results:
        h6b = r["h6_budget"] if r["h6_budget"] is not None else "(=budget)"
        h6b_str = f"{h6b:.4f}" if isinstance(h6b, (int, float)) else h6b
        print(f"{r['name']:<24}{r['budget']:<12.4f}{h6b_str:<12}"
              f"{r['feasible_with_budget']:<12}{r['feasible_fraction']:<10.3f}")
    print()
    print(f"Overlap (r0 = standard 439, r1 = P9-tight H6-only):")
    for k, v in overlap.items():
        print(f"  {k}: {v}")
    print()

    # Verdict per op_resolution.md §10.4 step 5/6
    r1_count = next(r["feasible_with_budget"] for r in regime_results if r["name"] == "R1_p9tight_h6only")
    r2_count = next(r["feasible_with_budget"] for r in regime_results if r["name"] == "R2_p9tight_all")

    verdict_lines: List[str] = []
    if r1_count >= 200:
        verdict_lines.append(
            f"R1 (P9-tight H6-only) FEASIBLE = {r1_count}/{n_configs} ≥ 200 — "
            "(P9-tight) is a CANDIDATE for L1-J' regime promotion enabling factor-1 sharpening."
        )
    elif r1_count < 50:
        verdict_lines.append(
            f"R1 (P9-tight H6-only) FEASIBLE = {r1_count}/{n_configs} < 50 — "
            "(P9-tight) regime too restrictive; (P9) standard stays."
        )
    else:
        verdict_lines.append(
            f"R1 (P9-tight H6-only) FEASIBLE = {r1_count}/{n_configs} (50–199 range) — "
            "INCONCLUSIVE; further regime analysis needed."
        )

    if r2_count >= 200:
        verdict_lines.append(
            f"R2 (P9-tight all-halved) FEASIBLE = {r2_count}/{n_configs} ≥ 200 — "
            "all-clause halving also viable as stronger relaxation."
        )

    print("Verdict per op_resolution.md §10.4 step 5/6:")
    for line in verdict_lines:
        print(f"  • {line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
