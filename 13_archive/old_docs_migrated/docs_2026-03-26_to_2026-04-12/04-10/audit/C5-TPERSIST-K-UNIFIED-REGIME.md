# C5 T-Persist-K-Unified Regime Audit

**Date:** 2026-04-10
**Session:** Cycle 12 — T-Persist-K-Unified regime audit
**Category:** audit
**Status:** complete
**Depends on:** C3-TPERSIST-K-SEP-REGIME.md; C4-TPERSIST-K-WEAK-REGIME.md; docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md

---

## 1. CURRENT GAP

**Canonical item:** C5 — T-Persist-K-Unified.

**Current category:** Category C.

---

## 2. Hypothesis Analysis

T-Persist-K-Unified uses five major hypotheses:

| Hypothesis | Status |
|---|---|
| PS | structural phase-separation entry condition |
| ND | nondegeneracy / positive Hessian gap |
| BC'-K | basin containment condition |
| TC-K | transport confinement condition |
| SR-Lambda | spectral/repulsion compatibility |

These are not cosmetic. They define the domain in which a unified theorem can honestly compose Sep, Weak, and Strong-Coexist behavior.

---

## 3. R1/B1/B3/B4 Consequence

The current scalar `Lambda_coupling` is useful for spectral coupling but incomplete for branch identity. R1 proved:

- overlap/minimum coupling does not imply centered branch identity;
- branch selection also requires tie-breaker/history/geometric state.

Therefore T-Persist-K-Unified cannot be a single scalar theorem over `Lambda` alone if it is meant to classify branches. It can remain a persistence theorem over explicitly selected branches/regimes.

---

## 4. Corrected Theorem Schema

The honest unified theorem should be read as:

> Given a selected K-formation branch satisfying PS, ND, BC'-K, TC-K, and SR-Lambda, temporal persistence holds with regime-dependent degradation. The theorem does not select the branch; branch selection is external data.

---

## 5. Decision

| Claim | Decision |
|---|---|
| unified persistence conditional on selected branch + five hypotheses | conditionally proved |
| scalar `Lambda` as full branch classifier | false / incomplete |
| Category C status | keep |
| future improvement | add branch-selection descriptor to theorem inputs |

---

## 6. Gap-Set Status

All formal Category B and Category C items in `LATEST-GAP-TABLE.md` have now been processed into proof/audit decisions in the 04-10 campaign artifacts. No Canonical Spec category changes were made.

---

## 7. Next Trigger

Proceed to research blocker R2 — near-bifurcation persistence (`mu -> 0`).

First move:

> Build a center-manifold / shrinking-window problem statement separating what remains of persistence as Hessian gap tends to zero.
