# Phase A-B Synthesis: Generalized Multi-Formation Persistence

**Date:** 2026-04-02
**Session:** Proof execution — generalization of T-Persist across regimes
**Category:** synthesis
**Status:** interrupted at Phase A/Phase B handoff
**Depends on:** Tasks #1-5 (Phase A-1, A-2, A-3, B-1, B-2)

---

## Stop Point / Resume Here

This synthesis document is the main handoff location for the interrupted Phase A/B project.

**Observed stop point on 2026-04-02:**
- Task #1 is complete and should be treated as the only fully finished analytical output.
- Task #4 and Task #5 were drafted ahead of full integration, but both remain provisional.
- Task #2 and Task #3 are still missing as finished documents.
- The integration step into this synthesis file never happened.

**Start here tomorrow:**
1. Read [CONDITIONAL-CONDITIONS-ANALYSIS.md](/Users/ojaehong/ex_2/docs/04-02/analysis/CONDITIONAL-CONDITIONS-ANALYSIS.md) and extract the exact replacements for ND/NB/GT, H2'/H3, and WR'/TC.
2. Produce the missing Task #2 document before editing any theorem statements.
3. Produce the missing Task #3 document before trusting the current `lambda_coupling` proposal.
4. Re-open [UNIFIED-REGIME-PARAMETRIZATION.md](/Users/ojaehong/ex_2/docs/04-02/theory/UNIFIED-REGIME-PARAMETRIZATION.md) and decide whether one scalar parameter is sufficient or whether `d_min` must remain an independent axis.
5. Then update [T-PERSIST-K-UNIFIED.md](/Users/ojaehong/ex_2/docs/04-02/theory/T-PERSIST-K-UNIFIED.md) section 7.3, 7.4, and section 9 placeholders.
6. Only after those edits, return to this file and fill Sections 2-5 in order.
7. Treat `exp45`-`exp47` as post-integration verification work, not as the next immediate step.

## 1. Overview

This document synthesizes the results of Phases A and B into a unified picture of multi-formation persistence across the Sep-Weak-Strong regime spectrum.

### What Changed (Old → New)

| Theorem | Old Status | New Status | Key Change |
|---------|-----------|------------|------------|
| T-Persist-1(b) | Conditional (GT+ND+NB) | *pending Task #1* | μ scaling refined |
| T-Persist-1(d) | Conditional (H2'+H3) | *pending Task #1* | deep core condition |
| T-Persist-1(e) | Conditional (Schauder) | *pending Task #1* | concentration bounds |
| T-Persist-K-Sep | Cat B (proved w/ WS+SR) | *pending Task #2* | structural param |
| T-Persist-K-Weak | Cat C (conditional) | *pending Task #2* | condition relaxation |
| — | — | *pending Task #4* | λ_coupling parametrization |
| — | — | *pending Task #5* | T-Persist-K-Unified |

## 2. Phase A Results

### Task #1: T-Persist-1 Conditional Analysis

*[To be filled when Task #1 completes]*

- μ scaling behavior:
- Conditions relaxed:
- Conditions tightened:
- Near-bifurcation refinement:

### Task #2: T-Persist-K Generalization

*[To be filled when Task #2 completes]*

- Sep structural conditions generalized:
- Weak structural conditions generalized:
- Common structure identified:

### Task #3: Isoperimetric/Transport Necessity

*[To be filled when Task #3 completes]*

- Which conditions are necessary vs sufficient:
- Tightness of bounds:
- Counterexamples found:

## 3. Phase B Results

### Task #4: Unified Regime Parametrization

*[To be filled when Task #4 completes]*

- λ_coupling definition:
- Regime boundaries:
- Phase diagram structure:

### Task #5: Unified K-Formation Persistence Theorem

*[To be filled when Task #5 completes]*

- T-Persist-K-Unified statement:
- Proof strategy:
- Special cases recover T-Persist-K-Sep and T-Persist-K-Weak:

## 4. Experimental Validation

### exp45: Sep Regime Boundary
*[To be filled after experiment runs]*

### exp46: Weak-to-Strong Transition
*[To be filled after experiment runs]*

### exp47: Full Phase Diagram
*[To be filled after experiment runs]*

## 5. Canonical Spec v2.1 Changes

### §13 Updates

1. **Category A additions:** *pending*
2. **Category B modifications:** *pending*
3. **Category C modifications:** *pending*
4. **New section: Regime Classification:** *pending*

### §12 Updates (Open Problems)

- Multi-formation temporal persistence: *update status*
- Strong regime: *update status*

### §15 Updates (Closing Summary)

- Largest remaining gaps: *update*

## 6. Theorem Dependency Graph

```
T1 (existence) ──┐
T8-Core (phase)──┤
T14 (grad flow)──┤
                 ↓
         T-Persist-1(a) ← IFT
         T-Persist-1(b) ← basin + GT
         T-Persist-1(c) ← shift threshold
         T-Persist-1(d) ← deep core (H2'+H3)
         T-Persist-1(e) ← Schauder + fingerprint
                 ↓
         T-Persist-Full ← (a)-(e) + WR'+PS+ND+NB
                 ↓
         ┌───────┴───────┐
         ↓               ↓
  T-Persist-K-Sep   T-Persist-K-Weak
  (WS + SR)         (WI + SR + NB-K)
         ↓               ↓
         └───────┬───────┘
                 ↓
       T-Persist-K-Unified  ← Task #5
       (λ_coupling parametrization)
```

## 7. Open Items

- [ ] Integrate Task #1 results
- [ ] Integrate Task #2 results
- [ ] Integrate Task #3 results
- [ ] Integrate Task #4 results (λ_coupling)
- [ ] Integrate Task #5 results (unified theorem)
- [ ] Run exp45-47
- [ ] Write Canonical Spec v2.1
- [ ] Update CHANGELOG.md
- [ ] First resume step tomorrow: create the missing Task #2 and Task #3 deliverables
