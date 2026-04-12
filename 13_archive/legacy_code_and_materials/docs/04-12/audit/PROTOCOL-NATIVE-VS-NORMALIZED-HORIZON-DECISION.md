# Protocol-Native vs Normalized-Horizon Decision

**Date:** 2026-04-12
**Session:** Cycle 110 — decide whether horizon normalization is needed after stable-entry strengthening
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/STABLE-ENTRY-CRITERION.md; docs/04-12/proof/PROTOCOL-HORIZON-AND-STOPPING-RULE.md; docs/04-12/proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md

---

## 1. Options

### Option A — keep the protocol-native finite horizon

Meaning:

> treat each protocol's own finite stopping rule as sufficient for the current theorem lane.

Pros:
- remains faithful to the protocol-tagged nature of the theory;
- matches the actual experimental evidence already on hand;
- avoids premature normalization before theorem-level bounds exist.

Cons:
- cross-protocol comparisons remain less elegant;
- later theorem statements may need a cleaner common time scale.

### Option B — introduce a normalized stopping notion now

Meaning:

> force different protocols to be compared under one more standardized horizon rule.

Pros:
- could improve formal comparability;
- might help future theorem presentation.

Cons:
- risks artificial standardization of genuinely different protocols;
- introduces another layer of abstraction before the bound side is ready;
- may overfit presentation rather than the actual current mathematical bottleneck.

---

## 2. Decision

**Choose Option A first: keep the protocol-native finite horizon.**

Reason:

1. the current lane is explicitly protocol-sensitive, so protocol-native termination is not a defect but part of the object being studied;
2. the next real open problem is no longer horizon specification, but turning the resulting accessibility quantities into useful upper/lower bounds;
3. normalization can be deferred until theorem-level comparison needs actually force it.

---

## 3. Consequence

The fixed-protocol accessibility surrogate is now stable enough for the current theorem lane:

```text
A_S(G, lambda; U_B)
= probability of stable entry into U_B(lambda)
  before the protocol S terminates under its own finite run.
```

So the next step should no longer polish the definition of `A_*`, but instead ask how to move from measured accessibility to theorem-facing inequalities.

---

## 4. What Gets Deferred

Normalized stopping notions are **deferred, not rejected**.
They may become useful later if a theorem compares multiple protocols under one shared asymptotic or budget-normalized framework.

---

## 5. Next Trigger

Write a compact note asking what the weakest useful theorem-facing upper/lower-bound form on `A_*` should be.
