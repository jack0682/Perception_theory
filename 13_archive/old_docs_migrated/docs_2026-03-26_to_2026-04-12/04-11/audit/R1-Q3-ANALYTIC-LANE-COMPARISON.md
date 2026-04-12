# Analytic Lane Comparison After Exp79–Exp81

**Date:** 2026-04-11
**Session:** Cycle 76 — choose the stronger explanatory line
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md; docs/04-11/experiment/EXP81-ACTIVE-SET-TRANSITION-PROXY-20x20_c0.6.md

---

## 1. Candidate Explanatory Lines

### Line A

**Continuation-accessible valleys + basin-access asymmetry**

Interpretation: the lower-energy Type B basin is real and locally robust, but random starts rarely enter it.

### Line B

**Active-set trapping**

Interpretation: raw and seeded trajectories differ because they hit different active-set / simplex-penalty-region patterns early, and this drives later branch divergence.

---

## 2. Current Evidence for Line A

From Exp79:

- raw starts on `20x20:0.6`, `lambda=0.5` have zero hits into the continued Type B family at all strict thresholds up to `4.0`.

From Exp80:

- local perturbations around the continued Type B branch return with 100% success for all tested sigmas up to `0.10`.

Together these say:

- the branch is easy to keep once entered,
- but hard to access from far-away random starts.

That is exactly the continuation-access / basin-access picture.

---

## 3. Current Evidence for Line B

From Exp81:

- the raw trajectory shows 30 coarse region transitions,
- the seeded trajectory shows 12,
- and the final branch families differ.

This is meaningful evidence that path geometry / coarse region changes differ across protocols.

However, it is still a proxy:

- the logged quantities are coarse,
- they do not yet prove a specific active-set obstruction,
- they do not isolate which transition actually causes the branch-family split.

---

## 4. Decision

**Choose Line A as the stronger explanatory line to formalize next.**

### Reason

- Line A is supported by two complementary diagnostics (Exp79 and Exp80) that directly address access versus local robustness.
- Line B is promising, but currently rests on a single coarse proxy diagnostic.
- So Line B should remain a secondary hypothesis until more explicit transition logging exists.

Working priority order after this note:

1. continuation-accessible valleys + basin-access asymmetry,
2. active-set trapping,
3. deeper geometric refinements of basin structure.

---

## 5. Next Trigger

Write a compact “continuation-access conjecture register” that records the strongest current analytic hypothesis and the minimal diagnostics that would strengthen or weaken it.
