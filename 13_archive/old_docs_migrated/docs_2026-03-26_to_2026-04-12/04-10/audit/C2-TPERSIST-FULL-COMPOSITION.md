# C2 T-Persist-Full Composition Audit

**Date:** 2026-04-10
**Session:** Cycle 9 — T-Persist-Full composition audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/C1-TPERSIST-EXACT-THRESHOLD.md; Canonical Spec v2.1.md §13; docs/03-31/synthesis/T-PERSIST-FULL-PROOF.md

---

## 1. CURRENT GAP

**Canonical item:** C2 — T-Persist-Full.

**Current category:** Category C.

T-Persist-Full is not a single primitive theorem; it is a composition of T-Persist-1(a)-(e). Its status is determined by the weakest component.

---

## 2. Component Split

| Component | Status | Notes |
|---|---|---|
| (a) minimizer persistence via IFT | proved | nondegenerate branch-local continuation |
| (b) gradient-flow convergence / basin | proved | directional basin / soft-mode analysis |
| (c) shifted-threshold core inclusion | proved | robust fallback |
| (d) exact-threshold preservation | Category C | requires interior-gap / beta / deep-core condition |
| (e) transport concentration | proved for deep core under transport hypotheses | two-tier: deep core strong, boundary weak |

---

## 3. Three Distinct Full-Theorem Variants

| Variant | Statement | Status |
|---|---|---|
| Shifted-threshold persistence | formation persists with threshold margin loss | PROVED / robust |
| Deep-core exact persistence | deep-core sites preserve exact threshold under positive interior gap | PROVED UNDER EXPLICIT CONDITIONS |
| All-core exact persistence | all core sites, including boundary, preserve exact threshold uniformly | FALSE / too strong |
| Near-bifurcation remnant | only shrinking-window / shifted/deep-core remnant survives as `mu -> 0` | CONDITIONALLY CHARACTERIZED |

---

## 4. Corrected T-Persist-Full Schema

The honest composition theorem is:

> Under nondegenerate branch persistence, basin containment, transport concentration, and phase-separated deep-core interior gap, temporal persistence holds. The shifted-threshold version is robust. Exact-threshold persistence is valid only on the protected deep-core subset and only when transition displacement is smaller than the interior margin.

Thus T-Persist-Full should be read as a **tiered theorem**, not one uniform all-core exact-threshold theorem.

---

## 5. Decision for C2

| Claim | Decision |
|---|---|
| T-Persist-Full with shifted threshold | can be treated as proved composition |
| T-Persist-Full with deep-core exact threshold | conditionally proved |
| T-Persist-Full with all-core exact threshold | reject / too strong |
| Category C status | keep for full exact-threshold statement |

---

## 6. Registry Delta

No Canonical Spec category change.

C2 remains Category C because the official full theorem includes C1 exact-threshold preservation. A future spec cleanup could split it into:

1. `T-Persist-Full-Shifted` — proved;
2. `T-Persist-Full-DeepExact` — proved under explicit interior-gap conditions;
3. `T-Persist-Full-AllCoreExact` — not valid as universal statement.

---

## 7. Next Trigger

Proceed to C3 — T-Persist-K-Sep.

First move:

> Decide whether WS/SR are theorem hypotheses that should remain Category C, or whether T-Persist-K-Sep should be relabeled as a proved regime theorem rather than a globally conditional theorem.
