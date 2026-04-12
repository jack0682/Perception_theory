# Protocol Horizon and Stopping Rule

**Date:** 2026-04-12
**Session:** Cycle 107 — finite horizon for the theorem-usable accessibility surrogate
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/ENTRY-EVENT-DEFINITION.md; docs/04-12/proof/WEAKEST-USEFUL-ASTAR-SURROGATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note specifies the finite protocol horizon / stopping rule that pairs with the entry event to complete the accessibility surrogate `A_*`.

---

## 2. Safe Current Rule

A safe theorem-facing stopping rule is:

```text
Use the protocol's own declared finite run:
- fixed initialization rule,
- fixed optimizer update rule,
- fixed stopping condition or iteration budget,
- then evaluate whether entry into U_B(lambda) occurred before termination.
```

So the horizon is not an external asymptotic limit. It is the **native finite run associated with the named protocol**.

---

## 3. Why This Is the Right Level of Precision

This choice is strong enough because:
- it makes the event probability well-defined,
- it respects the fact that current evidence comes from actual finite optimization procedures,
- it avoids pretending that we already control infinite-time or search-neutral behavior.

It is weak enough because:
- it does not force one universal global horizon across unrelated protocols,
- it allows theorem language to remain protocol-tagged.

---

## 4. Practical Interpretation

For a named protocol `S`, the accessibility surrogate is now read as:

```text
A_S(G, lambda; U_B)
:= probability that the trajectory produced by S,
under its own stated finite run specification,
first enters U_B(lambda) before termination.
```

So the stopping rule is whatever legitimately terminates the fixed protocol instance:
- a fixed iteration budget,
- a convergence test,
- or another explicitly stated finite stopping condition.

---

## 5. Why Not Force One Universal Horizon Yet

A single universal horizon across all protocols would currently overstate what is known because:
- different protocols already differ structurally,
- the theorem lane is explicitly protocol-sensitive,
- and current evidence is comparative rather than universal.

So the safest move is:
> **protocol-native finite horizon first, universalized comparison later if possible.**

---

## 6. Relation to Existing Evidence

### Exp79

Exp79 already uses a fixed finite run of the raw search protocol at the target lambda.
So it naturally instantiates the horizon rule.

### Exp80
nExp80 uses a fixed perturb-and-reoptimize procedure, which likewise gives a finite protocol-native run.

### Combined reading

The current evidence therefore already supports a finite-horizon accessibility notion; it was just not previously stated explicitly.

---

## 7. Safe Current Statement

The strongest current theorem-support reading is:

> accessibility under a protocol means first entry into the target local neighborhood before that protocol's own declared finite run terminates.

This is enough to complete the current minimal accessibility surrogate.

---

## 8. What Remains Open

- whether later theorem versions should normalize different protocols to a common horizon notion;
- whether convergence-based stopping and budget-based stopping are interchangeable enough for theorem use;
- whether first-hit should later be strengthened to stable-entry before termination.

---

## 9. Next Trigger

The next step should merge the event and horizon pieces into one compact finalized fixed-protocol accessibility-surrogate statement.
