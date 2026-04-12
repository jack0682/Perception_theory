# Phase A-B Synthesis: Generalized Multi-Formation Persistence

**Date:** 2026-04-02
**Session:** Proof execution — generalization of T-Persist across regimes
**Category:** synthesis
**Status:** complete
**Depends on:** Tasks #1-5 (Phase A-1, A-2, A-3, B-1, B-2)

---

## 1. Overview

This document synthesizes the results of Phase A (condition analysis, regime comparison, necessity analysis, parametrization) and Phase B (unified theorem, λ_coupling reconciliation) into a unified picture of multi-formation persistence across the Sep-Weak-Strong regime spectrum.

### What Changed (Old → New)

| Theorem / Component | Old Status | New Status | Key Change |
|---------------------|-----------|------------|------------|
| T-Persist-1 conditions | 7 conditions | **4 conditions** (PS, ND, BC', TC) | H2' proved; H3/GT absorbed; NB/WR' replaced |
| T-Persist-K-Sep | Cat B (proved w/ WS+SR) | **Unchanged** (recovered as corollary) | Now a limiting case of Unified |
| T-Persist-K-Weak | Cat C (conditional) | **Unchanged** (recovered as corollary) | NB-K absorbed into BC'-K |
| T-Persist-K-Strong | Theorem ladder | **Unchanged** (ladder preserved) | Coexistence branch = Λ < 1/(K-1) |
| T-Persist-K-Unified | Did not exist | **NEW: single parametric theorem** | 5 conditions, Λ_coupling parametrization |
| λ_coupling definition | Two competing definitions | **Reconciled**: Λ = λ_rep·ω_jk/min(μ_j,μ_k) | Spectral, dimensionless, identifies bifurcation |
| Isoperimetric ordering | Assumed needed for persistence | **Not needed** for persistence; metastability only | Separate theorem for landscape characterization |

## 2. Phase A Results

### Task #1: T-Persist-1 Conditional Analysis (CONDITIONAL-CONDITIONS-ANALYSIS.md)

**Outcome:** 7 conditions streamlined to 4.

| Original | Disposition | Rationale |
|----------|------------|-----------|
| (H2') Core² ≠ ∅ | Removed (proved) | Isoperimetric inradius: m ≥ 25, β ≥ 58α |
| (H3) β > 11α | Absorbed into (PS) | Phase separation subsumes; formation-structured β > 7α |
| (NB) μ ≥ 4.1 | Replaced by (BC') | Directional basin 10-100× weaker threshold |
| (GT) gentle transition | Absorbed into (BC') | Both sub-conditions subsumed by directional criterion |
| (WR') ρ < 1 | Replaced by (TC) | Transport confinement strictly weaker; exp40 confirms |

**Irreducible structural requirements:** μ > 0 (non-degeneracy), perturbation within basin, transport stays local.

### Task #2: Regime Conditions Comparative (REGIME-CONDITIONS-COMPARATIVE.md)

**Outcome:** d_min cannot be fully absorbed into Λ_coupling; two-parameter classification needed.

- **Universal conditions:** (H1-K) and (SR) appear in all persistence regimes
- **d_min** provides geometric guarantees (simplex satisfaction, separation budget) not captured by Λ
- **Spatial Decoupling Lemma** bridges: d_min ≥ 3 ⟹ Λ ≈ 0 + geometric guarantees
- **NB-K absorbed** into joint version of BC'
- **Recommended 5-condition set:** PS, ND, BC'-K, TC-K, SR-Λ

### Task #3: Isoperimetric/Transport Necessity (ISOPERIMETRIC-TRANSPORT-NECESSITY.md)

**Outcome:** Isoperimetric ordering not needed for persistence; TC strictly weaker than WR'.

- **Isoperimetric ordering:** Sufficient but NOT necessary for persistence. Necessary only for metastability characterization. No failing topologies found experimentally (exp35, 24 configs).
- **Transport confinement:** Analytical bound 25-100× too loose at natural parameters. Tightening path: perturbative Lipschitz (~5-10×), boundary-localized mass (~3-5×), fingerprint cost (~2×). Feasible but not yet done.
- **(TC) vs (WR'):** TC strictly weaker. exp40 shows persistence ≥ 0.999 in 6/6 configs but WR' fails in 3/6.

## 3. Phase B Results

### λ_coupling Reconciliation

Two competing definitions existed:
- Task #4 (UNIFIED-REGIME-PARAMETRIZATION.md): Λ = λ_rep · ω_jk / min(μ_j, μ_k) — spectral
- Task #5 draft: λ = |O_jk| / min(|Core_j|, |Core_k|) — geometric

**Decision:** Task #4's spectral definition adopted as canonical. It is dimensionless, captures spectral information, and correctly identifies the merge bifurcation at Λ = 1/(K-1). The geometric ratio is recovered as the special case ω_jk ≈ |O_jk|/min(|Core|) when field values are approximately uniform within formations.

### T-Persist-K-Unified Theorem (T-PERSIST-K-UNIFIED.md)

**Status:** All placeholders filled. Self-consistent document.

**Universal hypotheses (5 conditions):**

| # | Condition | Replaces |
|---|-----------|----------|
| 1 | (PS) Phase separation: β/α > β_crit | H3, H2' |
| 2 | (ND) Non-degeneracy: μ_k > 0 | ND |
| 3 | (BC'-K) Directional basin containment | NB-K, GT |
| 4 | (TC-K) Transport confinement | WR' |
| 5 | (SR-Λ) Spectral coupling: Λ_coupling < 1/(K-1) | WS, WI, SR |

**Regime-dependent conclusions:**
- **I (Sep):** Λ ≈ 0, per-formation persistence (proved)
- **II (Weak):** Λ ≪ 1, deep-core persistence + boundary fallback (conditional)
- **III-a (Strong-Coexist):** Λ < 1/(K-1), local K-branch continuation (conditional)
- **III-b through III-g:** Theorem ladder (local stability proved, merge conjectural)

**Merge handoff:** At Λ = 1/(K-1), the IFT fails. The unified theorem explicitly delineates its boundary and refers to the conjectured merge dichotomy (CT-KS4, MS1-MS4).

## 4. Experimental Validation (Pending)

Three experiments designed but not yet run:

| Experiment | Tests | Prediction |
|-----------|-------|-----------|
| **exp45** Sep boundary | Vary d_min on 15×15, 20×20 | Regime transition matches Λ threshold |
| **exp46** Weak→Strong | Vary overlap ratio | Mechanism change matches Λ |
| **exp47** Full phase diagram | 2D sweep (d_min, μ) | Unified phase diagram |

Plus three testable predictions from UNIFIED-REGIME-PARAMETRIZATION.md:
- P-Unified-1: Continuous degradation of Persist with Λ
- P-Unified-2: Depth-dependent onset of transport concentration
- P-Unified-3: Bifurcation sharpness at Λ = 1/(K-1)

## 5. Canonical Spec v2.1 Changes (Pending)

### Proposed §13 Updates

1. **T-Persist-1:** Note streamlined conditions (7→4) with Task #1 analysis reference
2. **T-Persist-K-Sep/Weak:** Mark as corollaries of T-Persist-K-Unified
3. **T-Persist-K-Unified:** New entry with 5-condition statement and regime-dependent conclusions
4. **Isoperimetric ordering:** Separate theorem, not persistence hypothesis

### Proposed New Section: Regime Classification

- Definition of Λ_coupling (canonical formula)
- Spatial Decoupling Lemma
- Phase diagram (two smooth crossovers + one sharp bifurcation)
- Predicted regime boundaries

### Decision: Defer Spec v2.1 until exp45-47 validate the regime boundaries.

## 6. Theorem Dependency Graph

```
T1 (existence) ──┐
T8-Core (phase)──┤
T14 (grad flow)──┤
                 ↓
         T-Persist-1(a-e)  [streamlined: PS+ND+BC'+TC]
                 ↓
         Spatial Decoupling Lemma
                 ↓
         T-Persist-K-Unified
         ├── Corollary I (Sep): d_min ≥ 3 ⟹ Λ ≈ 0
         ├── Corollary II (Weak): η < 0.2 ⟹ Λ ≪ 1
         └── Corollary III-a (Strong-Coexist): Λ < 1/(K-1)
                 ↓
         Bifurcation boundary: Λ = 1/(K-1)
                 ↓
         Conjecture C-KS (Merge dichotomy) [MS1-MS4 open]

Separate (landscape characterization):
  Isoperimetric Energy Ordering ──→ Metastability theorem
  K=2 Local Stability ──→ Barrier model
```

## 7. Open Items

- [ ] Run exp45-47 to validate regime boundaries
- [ ] Prove analytical transport confinement at natural parameters (tightening path in Task #3 §2.3)
- [ ] Prove generic soft-mode fraction f₁ = O(n^{-1/(2d)}) for automatic (BC') satisfaction
- [ ] Tighter spectral perturbation beyond Weyl for strong-regime coexistence
- [ ] Merge theorem beyond bifurcation (MS1-MS4)
- [ ] Barrier exponent derivation (experimental 0.89, no theory)
- [ ] Canonical Spec v2.1 (after experimental validation)
- [ ] Paper update with unified theorem narrative
- [ ] Update CHANGELOG.md with this session's results
