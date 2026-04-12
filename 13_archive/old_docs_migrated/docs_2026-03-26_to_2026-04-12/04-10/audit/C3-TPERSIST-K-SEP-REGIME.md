# C3 T-Persist-K-Sep Regime Audit

**Date:** 2026-04-10
**Session:** Cycle 10 — T-Persist-K-Sep regime audit
**Category:** audit
**Status:** complete
**Depends on:** Canonical Spec v2.1.md §12-13; docs/03-31/repair/MULTI-TEMPORAL-THEORY.md

---

## 1. CURRENT GAP

**Canonical item:** C3 — T-Persist-K-Sep.

**Current category:** Category C.

---

## 2. Are WS/SR Removable?

| Hypothesis | Meaning | Removable? | Reason |
|---|---|---|---|
| WS | well-separated supports / sufficient distance | No for Sep theorem | it defines the Sep regime; without it the theorem becomes Weak/Strong regime |
| SR | spectral-repulsion compatibility / positive joint gap | No for IFT proof | without positive joint gap, local minimizer persistence is not guaranteed by IFT |
| per-formation T-Persist conditions | each component has single-formation persistence | No | K theorem composes single-formation persistence |

---

## 3. Decision

T-Persist-K-Sep is best classified as:

> PROVED AS A REGIME THEOREM under explicit Sep-regime hypotheses, but Category C if read as a global theorem over all K-formation configurations.

The condition is not a proof artifact. It is a domain restriction.

---

## 4. Registry Delta

No Canonical Spec category change.

Recommended future naming:

- `T-Persist-K-Sep-Regime`: proved within regime;
- global `T-Persist-K`: remains conditional / multi-regime.

---

## 5. Next Trigger

Proceed to C4 — T-Persist-K-Weak.
