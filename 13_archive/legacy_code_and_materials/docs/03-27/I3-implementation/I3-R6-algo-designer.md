# Iteration 3 R6 — Algorithm Designer: Parameter Selection

**Author:** Algorithm Designer
**Date:** 2026-03-27
**Iteration:** 3, Round 6

---

## THE λ_sep/λ_bd PROBLEM

R10's claim of 10⁵× separation dominance is likely wrong. Hessian analysis suggests O(1) to O(10²) depending on parameters. But parameter normalization IS mandatory.

## THREE ALGORITHMS

1. **Scale Normalization (Static):** Evaluate each E_i at init, normalize λ_i = w_i·E_target/E_i. Problem: E_bd smooth = 0 at uniform.

2. **Hessian Normalization (Better):** Normalize by spectral norms of per-term Hessians. Cost: O(30|E|) via Lanczos. Principled and cheap. **RECOMMENDED DEFAULT.**

3. **Annealing (Dynamic):** Start with E_bd only (Allen-Cahn), ramp up E_cl then E_sep. Robust for difficult regimes. **FALLBACK.**

## PARAMETER ADMISSIBILITY CHECKER

Complete validator: contraction (a_cl<4), volume range (c∈(0.211,0.789)), phase transition (β/α>4λ₂/|W''(c)|), resolvent convergence (α_C<1/ρ), distinction (a_D>τ_D), analyticity (b_D=0), FULL Hessian instability check.

## USER-FACING PARAMETERS

Relative weights w_cl, w_sep, w_bd ∈ [0,1] with automatic internal scaling. Users never set λ_sep = 10⁻⁵ directly.

## PHASE DIAGRAM

The phase transition depends on ALL λ's, not just β/α. Full Hessian check reveals complex boundary in (β/α, λ_sep/λ_bd) space.
