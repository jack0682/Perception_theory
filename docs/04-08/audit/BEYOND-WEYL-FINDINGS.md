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

## CORRECTION (same session)

**The initial finding was WRONG.** Mode #0 (ψ_ext ≈ 0.67) is the volume constraint null mode (ψ = 1/√n, μ = 0 exactly). It should be excluded from the analysis as it's not a physical mode.

After excluding mode #0:

| L | first boundary mode μ | ψ²_ext | improvement |
|---|----------------------|--------|-------------|
| 12 | 0.54 | 0.016 | **63×** |
| 15 | 0.63 | 0.016 | **63×** |
| 18 | 0.86 | 0.021 | **49×** |
| 20 | 1.92 | 0.018 | **54×** |

**BMD holds consistently, improvement 49-63× across grid sizes.** The original "33×" was actually a CONSERVATIVE estimate.

## Corrected Status

- Bound formula: **Cat A** (unchanged)
- BMD theorem: **Cat A** (confirmed — boundary modes have ψ_ext ≈ 0.02)
- "33× improvement": **CONFIRMED and actually 50×+** across grid sizes
- ω^soft ≈ 0.016-0.021 is grid-size-independent → **Cat A upgrade viable**
- The improvement factor 1/ω^soft ≈ 50-63 is STABLE, not grid-specific
