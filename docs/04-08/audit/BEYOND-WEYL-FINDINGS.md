# Beyond-Weyl 33× Improvement: Grid-Size Scan

**Date:** 2026-04-08
**Category:** audit
**Status:** preliminary finding — needs further investigation

---

## Finding: "33× improvement" is grid-specific, not universal

Computed ε_BMD (soft-mode exterior fraction) across grid sizes at β=30:

| L | n | μ_min | ψ²_core | ψ²_bdy | ψ²_ext | improvement |
|---|---|-------|---------|--------|--------|-------------|
| 8 | 64 | ~0 | 0.297 | 0.125 | 0.578 | 1.7× |
| 10 | 100 | ~0 | 0.310 | 0.030 | 0.660 | 1.5× |
| 12 | 144 | ~0 | 0.299 | 0.076 | 0.625 | 1.6× |
| **15** | **225** | **0.41** | **0.066** | **0.919** | **0.015** | **67.6×** |
| 18 | 324 | ~0 | 0.309 | 0.012 | 0.679 | 1.5× |
| 20 | 400 | ~0 | 0.305 | 0.025 | 0.670 | 1.5× |

β dependence (15×15, different runs):

| β | ψ²_ext | improvement |
|---|--------|-------------|
| 20 | 0.627 | 1.6× |
| 30 | 0.653 | 1.5× |
| 50 | 0.676 | 1.5× |
| 100 | 0.680 | 1.5× |

## Root Cause

**The soft mode (smallest Hessian eigenvalue) is usually a TRANSLATION mode**, not a stability mode.

- Translation mode: formation slides across the grid. ψ is spread across exterior. μ ≈ 0.
- Stability mode: formation shape deforms. ψ concentrated on boundary. μ > 0.

BMD theorem applies to the **stability mode**, but the translation mode has a smaller eigenvalue. The 15×15 anomaly (improvement=67×) occurred because that particular formation was well-localized with translation suppressed (μ_min = 0.41 > 0).

## Implication

The "33× improvement over Weyl" from the original analysis (12×12 grid, exp46-47) was likely measured on a formation where translation modes were suppressed. The **generic improvement is only ~1.5×** (barely better than standard Weyl).

## What the bound formula actually guarantees

The mathematical bound μ_joint ≥ min_k μ_k - (K-1)λ_rep · ω^soft is **correct** (Cat A). But ω^soft ≈ 0.65 generically (not 0.03), so the practical improvement is:

- Original claim: Λ_max ≈ 33/(K-1)
- **Actual (generic): Λ_max ≈ 1.5/(K-1)** — only 50% wider than Weyl

## Status

- Bound formula: **Cat A** (unchanged — the math is correct)
- "33× improvement": **should be downgraded or qualified** — it's a best-case, not typical
- Need to investigate: can translation modes be rigorously excluded from the BMD analysis?
