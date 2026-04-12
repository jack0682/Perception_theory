# Protocol-Native Horizon Sufficiency

**Date:** 2026-04-12
**Session:** Cycle 110 — why the current theorem lane can keep the protocol-native horizon
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/PROTOCOL-NATIVE-VS-NORMALIZED-HORIZON-DECISION.md; docs/04-12/proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md

---

## 1. Claim

For the current fixed-protocol theorem lane, the protocol-native finite horizon is sufficient.

---

## 2. Meaning

This means the present accessibility object can safely remain:

```text
A_S(G, lambda; U_B)
:= probability of stable entry into U_B(lambda)
   before termination of protocol S under its own declared finite run.
```

No additional normalization is yet required.

---

## 3. Why This Is Sufficient Now

### A. The lane is already protocol-tagged

The whole point of the current theorem lane is to avoid false search-neutrality.
So letting each protocol keep its own finite run is consistent with the problem statement.

### B. The main missing piece is bounds, not time normalization

What is still absent is not a better time axis, but a theorem-facing way to say:
- raw accessibility is small,
- seeded accessibility is larger,
- and the gap is structurally meaningful.

### C. The evidence is natively finite-horizon

Exp79, Exp80, Exp81, and Exp82 all come from explicit finite optimization procedures.
So using the protocol-native horizon is the most faithful reading of the evidence.

---

## 4. Safe Theorem Reading

The safest current theorem-support reading is:

> if accessibility is defined relative to a named protocol and a theorem-facing local neighborhood, then the protocol's own finite stopping rule is an adequate horizon for the current stage of the theory.

This keeps the surrogate complete without introducing unnecessary extra structure.

---

## 5. What This Does Not Settle

This does **not** yet settle:
- how the eventual theorem should compare protocols asymptotically,
- whether later work should introduce a common budget notion,
- or whether accessibility should ultimately be bounded in horizon-free form.

It only says those questions can be postponed.

---

## 6. Next Trigger

The next refinement should shift from defining `A_*` to asking what theorem-facing inequality form is weakest but useful: upper bound on `A_raw`, lower bound on `A_seed`, or direct gap bound.
