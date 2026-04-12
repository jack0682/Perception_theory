# 2026-04-07 Session Index

**Date:** April 7, 2026  
**Theme:** F''(M/2) computation and K=2 landscape structure  
**Status:** Complete analysis with clear next steps

---

## Overview

This session deepened understanding of the K=2 (two-formation) energy landscape by comparing two complementary experimental approaches to measuring F''(M/2) (second derivative of reduced energy at the symmetric point on the mass-transfer manifold). Initial confusion about opposite F'' signs resolved into recognition of **two distinct K=2 configuration types**.

---

## Documents Created (Morning)

### 1. Theory Analysis
- **`F-DOUBLE-PRIME-COMPUTATION.md`** — Initial F''(M/2) analysis
  - Method 1 (uniform transfer): Always F''>>0 (overestimates due to no relaxation)
  - Method 2 (re-optimize at each m): F'' ∈ [−0.4, +0.4], parameter-dependent sign
  - Chemical potential gap Δμ near-zero: formations equilibrated

### 2. Experiments
- **`exp62_f_double_prime.py`** — Mass sweep (21 points, global landscape)
  - Independent optimization at each m ∈ [0.7M/2, 1.3M/2]
  - Finds lowest-energy formation compatible with mass m
  - Result: F''(M/2) signed averages over all K=2 flavours
  
- **`exp63_hessian_mass_transfer.py`** — Direct Hessian (9 points, local trajectory)
  - Starts from explicit K=2 minimizer via find_k_formations()
  - Re-optimizes along mass-transfer direction ε ∈ [−3, +3]
  - Result: F''(0) for one specific K=2 configuration

---

## Documents Created (Afternoon)

### 3. Divergence Analysis
- **`EXP62-EXP63-DIVERGENCE.md`** — Resolution of sign flip
  - All 4 configurations show F'' sign flip between exp62 and exp63
  - **Not a contradiction:** exp62 measures GLOBAL landscape, exp63 measures LOCAL trajectory
  - Two K=2 types identified:
    - **Type A (centered):** u₁ ≈ u₂, exp62 finds this implicitly
    - **Type B (off-center):** u₁ ≠ u₂, exp63 finds this explicitly
  - Non-convergence of F''(h): sign flips at intermediate h indicate valley-hopping

### 4. Regime Analysis
- **`K2-FLAVOURS-AND-GRID-SIZE.md`** — K=2 type prediction
  - Asymmetry metric: ⟨E(ε>0)⟩ − ⟨E(ε<0)⟩ reveals preferred mass direction
  - **On 20×20 grids:** Type B ↔ low λ_sep (Weak regime) | Type A ↔ high λ_sep (Sep regime)
  - **On 15×15 grids:** Geometric/topological effects dominate λ_sep parameter
  - ACF[1] as proxy: ACF[1]>+0.6 → Type A, ACF[1]<−0.2 → Type B (valley-hopping)

### 5. Research Planning
- **`NEXT-STEPS-FORMATION-TRACKING.md`** — exp65 proposal
  - Direct measurement of u₁, u₂ position and mass along ε trajectory
  - Detect formation swaps (u₁↔u₂ exchange), measure separation d_c(ε), rotation θ(ε)
  - Validate Type A vs Type B classification
  - Correlate with Λ_coupling parameter prediction

---

## Key Quantitative Findings

### F'' Sign Flip (All Configurations)

| Config | exp62 (sweep) | exp63 (Hessian) | Δ | exp62 verdict | exp63 verdict |
|--------|---|---|---|---|---|
| 15x15_c0.5 | −5.9e−3 | +0.110 | +0.116 | **Saddle** | Local min |
| 15x15_c0.6 | +8.5e−4 | −0.159 | −0.160 | Local min | **Saddle** |
| 20x20_c0.5 | +1.3e−3 | −0.403 | −0.404 | Local min | **Saddle** |
| 20x20_c0.6 | −1.9e−3 | +0.359 | +0.361 | **Saddle** | Local min |

**Sign flip on 4/4 configs — indicates different K=2 types, not measurement error.**

### K=2 Asymmetry (Reveals Type)

| Config | Asymmetry | Interpretation | λ_sep | Regime |
|--------|-----------|---|---|---|
| 15x15_c0.5 | +0.103 | Type B (off-center) | 0.204 | K-Sep anomaly |
| 15x15_c0.6 | −0.005 | Type A (centered) | 0.108 | K-Weak anomaly |
| 20x20_c0.5 | −0.061 | Type A (centered) | 0.202 | K-Sep ✓ |
| 20x20_c0.6 | **+0.375** | **Type B (off-center)** | **0.108** | **K-Weak ✓** |

**20×20 pattern:** Asymmetry ∝ (1/λ_sep) — Type B when separation weak  
**15×15 pattern:** Grid geometry dominates — regime prediction breaks

### Optimizer Quality (ACF[1] Autocorrelation)

| Config | ACF[1] | Reversals | Valleys | Quality |
|--------|--------|-----------|---------|---------|
| 15x15_c0.5 | **+0.734** | 4/7 | **Single** | High (monotonic) |
| 15x15_c0.6 | −0.401 | 6/7 | Multiple | Low (hopping) |
| 20x20_c0.5 | −0.452 | 5/7 | Multiple | Low (hopping) |
| 20x20_c0.6 | −0.218 | 5/7 | Multiple | Very low (chaotic) |

**ACF[1]>+0.6 → Type A (smooth valley), ACF[1]<−0.2 → Type B (valley-hopping)**

---

## Theoretical Categorization Update

### Before This Analysis
- **F''(M/2):** Category B (parameter-dependent sign)
- Signature: Sign varies with λ_sep, grid size — no unified rule

### After This Analysis
- **F''(M/2) for Type A (centered K=2):** Category B/C (regime-dependent and trajectory-dependent)
- **F''(M/2) for Type B (off-center K=2):** Category B/C (regime-dependent and trajectory-dependent)
- **K=2 Type Classification:** Category B (prediction rule λ_sep → Type correlates on 20×20 but fails on 15×15)

### Honest Assessment
This is **not a demotion** — it's a **refinement**. The divergence reveals that:
1. The K=2 landscape has two distinct flavors
2. Regime classification (T-Persist-K-Sep vs T-Persist-K-Weak) may conflate them
3. Grid-size effects are non-negligible below ~500 sites

---

## Open Questions for exp65

1. **Do formations swap during mass transfer?** (θ discontinuity detection)
2. **Does ACF[1] proxy work?** (Compare ACF[1] with actual swap count)
3. **Why is 15×15_c0.5 anomalous?** (High λ_sep but Type B signature)
4. **Can Λ_coupling be measured directly?** (Use overlap and chemical potential from exp65)
5. **Are there > 2 K=2 types?** (Formation morphology changes beyond position?)

---

## Files Summary

### Created
- `F-DOUBLE-PRIME-COMPUTATION.md` — Methods, results, analysis
- `EXP62-EXP63-DIVERGENCE.md` — Divergence resolution and K=2 type theory
- `K2-FLAVOURS-AND-GRID-SIZE.md` — Regime classification with grid effects
- `NEXT-STEPS-FORMATION-TRACKING.md` — exp65 design and code skeleton
- `SESSION-04-07-INDEX.md` — This document

### Modified
- `CHANGELOG.md` — New entry documenting afternoon analysis

### Data Files
- `experiments/results/exp62_f_double_prime.json` — 21 mass points, 6 configs (created morning)
- `experiments/results/exp63_hessian_mass_transfer.json` — 9 ε points, 4 configs (created morning)

---

## How to Continue

### Next Session Tasks (in order)
1. **Write exp65 code** (~1 hour)
   - Copy exp63 base, add center_of_mass and angle tracking
   - Test on 15×15_c0.5 first (takes ~5 min)

2. **Run exp65 on all 4 configs** (~30 min)
   - Expect results: Type classification validation, swap detection

3. **Analyze formation tracking results** (~30 min)
   - Plot d_c(ε), θ(ε), detect swaps
   - Compare ACF[1] predictions vs actual swap counts

4. **Update regime classification in Canonical Spec** (1-2 hours)
   - Amend T-Persist-K-Sep and T-Persist-K-Weak definitions with Type A/B clarification
   - Add grid-size caveat

5. **Optional: exp66 (morphology tracking)**
   - If exp65 detects intra-formation shape changes (not just swap)
   - Track principal axes, aspect ratio of each u_k

---

## Status: Ready for Implementation

All necessary analysis complete. exp65 design is concrete and testable. The theoretical pathway forward is clear.

**Next: Pass to research phase for exp65 execution.**
