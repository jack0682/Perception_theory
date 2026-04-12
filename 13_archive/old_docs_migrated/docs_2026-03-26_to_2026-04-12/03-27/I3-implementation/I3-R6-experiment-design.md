# Iteration 3 R6 — Experiment Designer: λ_sep/λ_bd Sweep (R10 Resolution)

**Author:** Experiment Designer
**Date:** 2026-03-27
**Iteration:** 3, Round 6

---

## THE EXPERIMENT THAT RESOLVES R10

11 configurations: λ_sep/λ_bd from 0 to 1000. 10×10 grid, β=10, c=0.5. 110 runs.

Plus Hessian decomposition ON Σ_m (addressing all 3 Rigor Auditor caveats) and Hessian-normalized comparison.

## KEY PREDICTIONS

- P-S1: "Goldilocks" range at λ_sep/λ_bd ∈ [10⁻³, 10⁻¹]
- P-S2: R10's 10⁵× is a normalization artifact → reduces to 1-10× when normalized
- P-S3: Separation enhances but does not replace the double-well
- P-S5: Anti-Turing pattern may survive at moderate λ_sep (genuine finding)

## THE VERDICT QUESTION

Is there a λ_sep/λ_bd range where formations are QUALITATIVELY BETTER than pure Allen-Cahn? If yes → separation is genuine contributor. If no → separation is decorative.

## BUDGET: ~15 minutes of compute

This is the highest-ROI experiment in Iteration 3.
