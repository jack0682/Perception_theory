# Exp66 Branch Sweep Preliminary

**Date:** 2026-04-10
**Session:** Cycle 2 preliminary next-trigger execution
**Category:** experiment
**Status:** active
**Depends on:** docs/04-10/audit/NEXT-TRIGGER.md; experiments/exp66_branch_selection_sweep.py; experiments/results/exp65_sweep_20x20_c06_lrep_*.json

---

## Scope

This is a preliminary start of the R1-Q next trigger. It is not a complete branch-selection diagram. It covers only `20x20_c0.6` for `lambda_rep <= 1.0` using the exp65 tracking summaries currently present.

## Preliminary Data

| lambda_rep | Type label | mean center offset | mean separation | mean soft overlap | energy asymmetry E(+)-E(-) | Interpretation |
|---:|---|---:|---:|---:|---:|---|
| 0 | Type B candidate | 0.188 | 10.62 | 0.0117 | -0.0238 | off-center / weakly overlapping |
| 0.05 | Type A candidate | 0.016 | 12.50 | 0.0000 | +0.0601 | centered branch |
| 0.10 | Type A candidate | 0.020 | 12.54 | 0.0000 | +0.0516 | centered branch |
| 0.20 | Type A candidate | 0.028 | 12.42 | 0.0000 | +0.0682 | centered branch |
| 0.50 | Type A candidate | 0.040 | 12.30 | 0.0000 | +0.0945 | centered branch |
| 1.00 | Type A candidate | 0.046 | 12.16 | 0.0000 | +0.0571 | centered branch |

## Preliminary Inference

For `20x20_c0.6`, current data suggests a sharp branch-selection change between `lambda_rep = 0` and `lambda_rep = 0.05`. This supports the Cycle 1 conclusion that branch type is repulsion/selection dependent.

## Proof Status

**NUMERICAL SUPPORT ONLY.** This does not prove an exact threshold. It motivates the next formal step: run continuation in both directions and compare branch energies to distinguish a true bifurcation from multi-start branch selection.

## Required Completion

1. Finish `lambda_rep ∈ {2, 5, 10}` for `20x20_c0.6` using the same sweep driver.
2. Run all four target configs.
3. Add warm-start increasing and decreasing modes, not just independent runs.
4. Record possible energy crossing or hysteresis.
