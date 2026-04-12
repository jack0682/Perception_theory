# Counterexamples and Obstructions

**Date:** 2026-04-10
**Session:** Cycle 1 adversarial audit for R1
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/PROOF-ATTEMPTS.md; experiments/results/exp65_lambda_rep0_20x20_c06.json; experiments/results/exp65_formation_tracking.json

---

## Obstruction Taxonomy

| Obstruction | Consequence |
|---|---|
| Multiple local minimizer branches | “The K=2 minimizer” is not a well-defined object without selection rule |
| Symmetry or near-symmetry of graph | Branches may occur in orbits or near-degenerate families |
| Active-set changes | Analytic continuation is only piecewise; proof must stop at event boundaries |
| Hessian degeneracy | Branch may bifurcate or lose local minimality |
| Energy crossing | Optimizer-selected branch can change even when both local branches remain stable |
| Optimizer initialization / restart policy | Numerical selected branch may not equal global or canonical branch |
| Lambda_coupling = 0 on disjoint branches | Coupling scalar alone misses geometric branch data |
| Repulsion sensitivity | Same grid/c_ref can show different branch type as lambda_rep changes |

## Concrete Current Counterexample to Overstrong Wording

The overstrong wording “`20x20_c0.6` is Type B” or “K=2 type is determined by `(grid_size,c_ref)`” is contradicted by exp65:

| config | lambda_rep | center_offset_norm | classification |
|---|---:|---:|---|
| 20x20_c0.6 | 10 | 0.022 | Type A candidate |
| 20x20_c0.6 | 1 | 0.023 | Type A candidate |
| 20x20_c0.6 | 0 | 0.165 | Type B candidate |

This is not a theorem-level counterexample to all possible branch-selection laws. It is a counterexample to any law that omits repulsion/branch-selection data.

## Counterexample Templates Still To Test

1. Non-D4 asymmetric graph with degenerate low eigenspace.
2. Square grid with multiple restart seeds selecting symmetry-related branches.
3. Fixed graph/parameters but varied `lambda_bar`, testing penalty vs hard simplex behavior.
4. Same branch under continuation vs multi-start global reoptimization, testing energy-crossing selection.

## CEX-4 — Minimum overlap does not imply centeredness

**Claim threatened.** Positive repulsion / minimum overlap selects Type A centered placement.

**Counterexample.** On a large square grid, place two small automorphic copies of a formation in opposite corners or adjacent corners. Both pairs can have zero overlap, equal self-energy, and zero simplex-barrier violation. The opposite-corner pair is centered; the adjacent-corner pair is off-center. Energies are equal for all `lambda_rep >= 0`.

**Status.** Formal counterexample schema. See `docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md`.
