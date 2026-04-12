# Exp71 Branch-Continuation Threshold Design

**Date:** 2026-04-10
**Session:** Cycle 51 — branch-continuation threshold design
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-10/audit/BRANCH-RESELECTION-THRESHOLD-ESTIMATE.md; docs/04-10/proof/POSITIVE-REPULSION-BRANCH-RESELECTION.md

---

## 1. Purpose

Independent multi-start optimization at each `lambda_rep` does not preserve branch identity, so it cannot estimate the finite-candidate reselection threshold

```text
lambda > DeltaE_0 / DeltaR.
```

Exp71 uses warm-start continuation to track candidate branches across `lambda_rep`.

---

## 2. Protocol

Track two branch families:

1. **Up branch:** optimize at `lambda=0`, then warm-start through increasing `lambda` values.
2. **Down branch:** optimize at high `lambda`, then warm-start through decreasing `lambda` values.

At each continuation step, record:

- source energy at current lambda,
- inferred zero-repulsion energy `E0 = E_lambda - lambda * overlap`,
- overlap `<u1,u2>`,
- center offset and separation,
- branch type label.

---

## 3. Threshold Estimator

For two matched candidate branches `A` and `B`, estimate:

```text
lambda_star = (E0_A - E0_B) / (R_B - R_A)
```

where `A` is the lower-overlap candidate and `R_B > R_A`.

This is meaningful only when both branches are tracked as identities, not independently rediscovered.

---

## 4. Implementation

Implemented in:

```text
experiments/exp71_branch_continuation_threshold.py
```

---

## 5. Next Trigger

Run a smoke continuation on `10x10:0.6` and inspect whether up/down branches remain distinct or collapse to the same branch.
