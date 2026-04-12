# C4 T-Persist-K-Weak Regime Audit

**Date:** 2026-04-10
**Session:** Cycle 11 — T-Persist-K-Weak regime audit
**Category:** audit
**Status:** complete
**Depends on:** C3-TPERSIST-K-SEP-REGIME.md; Canonical Spec v2.1.md §12-13

---

## 1. CURRENT GAP

**Canonical item:** C4 — T-Persist-K-Weak.

**Current category:** Category C.

---

## 2. Hypothesis Analysis

| Hypothesis | Meaning | Removable? | Reason |
|---|---|---|---|
| WI | boundary overlap is small relative to core | No for Weak theorem | defines weakly-interacting regime |
| SR / NB-K | joint spectral gap remains positive | No for persistence proof | needed for joint IFT / basin control |
| per-formation T-Persist | inherited from single-formation theorem | No | component persistence is prerequisite |
| shifted-threshold fallback on overlap boundary | structural | exact threshold fails at negotiated boundary |

---

## 3. R1 Interaction

R1 shows branch and tie-breaker data matter even when soft overlap is zero. For weak overlap regimes, branch data matters even more. Therefore T-Persist-K-Weak must remain branch/regime-conditioned; it cannot be upgraded to a branch-free global theorem.

---

## 4. Decision

T-Persist-K-Weak is:

> PROVED/CONDITIONALLY PROVED within the weak-interaction regime, with WI/SR/NB-K as non-removable regime and spectral hypotheses.

Category C remains appropriate for the official global theorem bucket.

---

## 5. Next Trigger

Proceed to C5 — T-Persist-K-Unified.
