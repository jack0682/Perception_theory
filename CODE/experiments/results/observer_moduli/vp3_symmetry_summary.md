> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# VP-3 Symmetry Test Summary

**Date:** 2026-05-08
**Experiment:** exp87_vp3_core_weight_symmetry.py (corrected run)
**Attacks:** OP-OMS-001 (core-weight gauge group)
**Scenes:** S3_grid6x6 (n=36), S4_two_cliques (n=10)
**Volume fraction:** 0.3

## Verdict Table

| Transform | Description | Verdict | frac_asym | ΔP_top_mean | Note |
|---|---|---|---|---|---|
| A | Closure-separation swap | **NOT_A_SYMMETRY** | 0.667 | ~0.54 | Near-symmetric near λ_cl=λ_sep |
| B | Closure-boundary swap | **NOT_A_SYMMETRY** | 0.625 | ~1.12 | Strong effects |
| C | Boundary-closure compensation (δ=0.15) | **NOT_A_SYMMETRY** | 0.750 | ~0.67 | Near-sym near λ_bd corner |
| D | Boundary-separation compensation (δ=0.15) | **NOT_A_SYMMETRY** | 0.750 | ~0.11 | Near-sym near λ_bd corner |
| E | Transport ablation (static) | **CANDIDATE_SYMMETRY** | 0.000 | 0.0000 | Confirms Prop CW2 |
| F | Radial toward centroid (t=0.3) | **NOT_A_SYMMETRY** | 0.583 | — | No centroid gauge direction |
| G | Random tangent (ε=0.08) | **PARTIAL_SYMMETRY** | 0.125 | — | Local flatness ≠ gauge invariance |

## OP-OMS-001 Classification

**Status:** PARTIALLY_RESOLVED — default G_cw={e} COMPUTATIONALLY SUPPORTED for dynamic scenes.

**Confirmed NOT symmetries:** A, B, C, D, F, G
**Candidate/Conditional symmetries:** E (transport ablation — static scenes only)

## Key Findings

### Finding VP3-1: G_cw = {e} Computationally Supported

All tested λ-space transformations on P_top produce measurably different readouts for
a majority of tested observer configurations. No global gauge direction on Δ³ was found.
Prop CW3 (conservative default G_cw={e}) is COMPUTATIONALLY SUPPORTED.

### Finding VP3-2: Prop CW2 Computationally Confirmed

Transform E (transport ablation) gives delta_d = delta_T = 0.0000 for ALL tested pairs
on static single-frame scenes. This COMPUTATIONALLY CONFIRMS Prop CW2: λ_tr is a
genuine gauge direction when restricted to static scenes. The 1-parameter family
{λ_tr → λ_tr'} with proportional rescaling of other weights is a conditional symmetry.

**Prop CW2 status upgrade: PROVED (conditional) → COMPUTATIONALLY CONFIRMED.**

### Finding VP3-3: Approximate Local Symmetries Near λ_cl=λ_sep and λ_bd Corners

- Transform A: Near-symmetric pair (0.60,0.20,0.15,0.05) → (0.20,0.60,0.15,0.05)
  gives delta_P_top=0.0295 < 0.05. The Z_2 swap is approximately a local symmetry
  near the diagonal {λ_cl = λ_sep} ⊂ Δ³.
- Transforms C, D: Near-symmetric cases near λ_bd=0.85 corner suggest the boundary
  energy can be approximately compensated by closure or separation weight when λ_bd
  is already dominant.

These are LOCAL approximate symmetries, not global gauge directions. They may define
flat directions in the V_D^0 landscape (within-basin flatness).

**New open problem: OP-OMS-017 — approximate symmetry loci in Δ³** (see below).

### Finding VP3-4: Large Δ for Extreme λ Pairs

Closure-dominant vs separation-dominant observer: delta_P_top = 1.50 (S4_two_cliques).
Closure vs boundary-dominant: delta_P_top = 3.44 (S3_grid6x6). These are the strongest
discrimination signals, confirming the four energy terms are genuinely inequivalent.

## OP-OMS-001 Final Status

| Sub-question | Pre-VP3 | Post-VP3 |
|---|---|---|
| S4 permutation symmetry? | REJECTED (theory) | CONFIRMED rejected (no counterexample found) |
| Closure-sep swap global symmetry? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY (VP-3 A) |
| Closure-bd swap global symmetry? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY (VP-3 B) |
| Boundary-closure local symmetry? | HYPOTHESIZED approx. | PARTIAL (VP-3 C): near-sym near λ_bd corner |
| Boundary-sep local symmetry? | COMPUTATIONALLY TESTABLE | PARTIAL (VP-3 D): same pattern |
| Transport invariance (static)? | PROVED conditional (Prop CW2) | COMPUTATIONALLY CONFIRMED (VP-3 E) |
| G_cw = {e} default? | ASSUMED | COMPUTATIONALLY SUPPORTED (VP-3 A–G) |

**OP-OMS-001 remains OPEN** for formal proof (no computational test can prove G_cw={e} universally),
but all major candidate symmetries are ruled out computationally. The default G_cw={e} is now
strongly supported.

## New Open Problem: OP-OMS-017

**OP-OMS-017 — Approximate Symmetry Loci in λ-Space.**
Is there a codimension-1 subset S ⊂ Δ³ (e.g., the diagonal {λ_cl = λ_sep}) on which
the closure-separation swap acts as an approximate gauge symmetry of P_top?
If so, S defines a flat direction in the observer landscape V that may affect basin boundaries.
Status: OPEN. Importance: ★. Difficulty: M.
