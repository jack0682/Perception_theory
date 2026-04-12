# Basin-Access Geometry Statement

**Date:** 2026-04-11
**Session:** Cycle 88 — compact geometry statement for continuation access
**Category:** theory
**Status:** complete
**Depends on:** docs/04-11/audit/POST-EVIDENCE-CHAIN-LANE-DECISION.md; docs/04-11/audit/CONTINUATION-ACCESS-EVIDENCE-CHAIN.md

---

## 1. Statement Type

This is a **non-theorem conceptual statement** summarizing the current best geometric reading of the branch-selection experiments.

---

## 2. Statement

In the tested SCC K=2 branch-selection regimes, the current evidence is consistent with the following geometry:

> there exist low-energy Type B basins that are locally robust once entered, but that have poor accessibility from generic raw multistart initializations.

Equivalently, the observed branch-selection asymmetry can be read as a mismatch between:

- **local basin robustness**, and
- **global basin accessibility from the chosen search protocol**.

---

## 3. Consequence

Under this geometry picture, branch-selection outcomes are governed by two different questions:

1. **Can the optimizer stay in the basin once it is nearby?**
2. **Can the optimizer reach the basin from the initialization rule it is given?**

The current experiments suggest that, for the tested Type B branches, the answer to (1) is often yes while the answer to (2) is often no.

---

## 4. Methodological Corollary

Therefore:

> failure of raw multistart search to return a branch is weak evidence of branch nonexistence when seeded continuation demonstrates both entry and local robustness.

That is the central methodological implication of the current campaign state.

---

## 5. What This Does Not Claim

This statement does **not** claim:

- a theorem of SCC,
- a universal description of all configurations,
- or that Type B is always globally optimal.

It is a compact explanatory summary of the current tested evidence only.

---

## 6. Next Trigger

If the campaign continues, the natural next step is to decide whether to keep abstracting this geometry into a formal conjecture/theorem-support ladder, or to return to instrumented diagnostics that quantify the access asymmetry more sharply.
