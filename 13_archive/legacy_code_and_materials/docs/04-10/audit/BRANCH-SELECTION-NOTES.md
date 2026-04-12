# Branch Selection Notes

**Date:** 2026-04-10
**Session:** Cycle 1 branch-selection notes
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/CURRENT-TARGET.md; docs/04-10/audit/PROOF-ATTEMPTS.md

---

## Branch-Conditioned Vocabulary

| Term | Working definition |
|---|---|
| Branch | A connected local KKT solution family under continuation in parameters within a fixed or piecewise-fixed active-set stratification |
| Selected branch | The branch obtained by an explicitly stated selection rule: warm-start continuation, multi-start global best, specified seed, or analytic branch label |
| Type A candidate | Branch with small normalized pair midpoint offset, no swaps, stable orientation over epsilon |
| Type B candidate | Branch with substantial pair midpoint offset or persistent off-center geometry |
| Branch event | Hessian degeneracy, active-set change, energy crossing, or branch-selection rule discontinuity |

## Corrected Branch-Selection Claim

Unsafe:

> The K=2 type is determined by grid size and volume fraction.

Safe:

> For a specified graph, parameter vector, active stratum, and branch-selection rule, nondegenerate K=2 local minimizer branches continue locally. Type A/B classification is a branch observable and may change only through branch events or a change in selection rule.

## Implication for F''(M/2)

`F''(M/2)` must be indexed by branch:

```text
F''_B(M/2; branch b, selection rule S)
```

Without branch index b and selection rule S, the symbol conflates distinct local trajectories.

## Lambda-Rep Sweep Update — 20x20_c0.6

| `lambda_rep` | Type label | Mean center offset | Mean separation | Swaps | E(+)-E(-) |
|---:|---|---:|---:|---:|---:|
| 0.00 | Type B candidate | 0.1877 | 10.62 | 0 | -0.0238 |
| 0.05 | Type A candidate | 0.0164 | 12.50 | 0 | +0.0601 |
| 0.10 | Type A candidate | 0.0195 | 12.54 | 0 | +0.0516 |
| 0.20 | Type A candidate | 0.0280 | 12.42 | 0 | +0.0682 |
| 0.50 | Type A candidate | 0.0397 | 12.30 | 0 | +0.0945 |
| 1.00 | Type A candidate | 0.0459 | 12.16 | 0 | +0.0571 |

**Updated hypothesis:** the observed branch change is concentrated at the singular endpoint `lambda_rep=0`, not a broad positive threshold in `[0.05,1]`.

## R1-G Update — Centeredness Requires Tie-Breaker

Positive repulsion selects minimum overlap, but minimum overlap does not imply centeredness. Opposite-corner and adjacent-corner disjoint placements can both have zero overlap while only the opposite-corner pair is centered. Therefore Type A should not be defined by overlap alone.

Working corrected branch rule candidate:

1. minimize overlap,
2. among zero/minimum-overlap placements maximize separation or boundary-clearance,
3. only then infer centered/symmetric Type A where graph symmetry supports it.
