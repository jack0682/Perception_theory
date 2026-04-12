# A_raw vs A_seed vs Gap Decision

**Date:** 2026-04-12
**Session:** Cycle 111 — choose the weakest useful inequality form for the accessibility surrogate
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/PROTOCOL-NATIVE-HORIZON-SUFFICIENCY.md; docs/04-12/proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Options

### Option A — upper bound on `A_raw`

Meaning:

> prove or target a theorem-facing statement that raw accessibility is small.

Pros:
- directly reflects Exp79-style rarity;
- isolates the search-failure side clearly.

Cons:
- says nothing positive about the seeded protocol;
- can understate the full asymmetry by treating only one side.

### Option B — lower bound on `A_seed`

Meaning:

> prove or target a theorem-facing statement that seeded accessibility is large.

Pros:
- aligns with the continuation/persistence side;
- works naturally with Exp80-style local return evidence.

Cons:
- alone it does not distinguish seeded success from raw failure;
- still leaves the comparative claim implicit.

### Option C — direct gap bound `A_seed - A_raw`

Meaning:

> target a theorem-facing inequality that accessibility under the seeded protocol exceeds accessibility under the raw protocol by a positive margin.

Pros:
- matches the actual protocol-comparison thesis most directly;
- keeps both sides of the asymmetry in one object;
- is the most faithful inequality form for the current fixed-protocol theorem lane.

Cons:
- depends on understanding both sides at once;
- may need one-sided bounds as sublemmas later.

---

## 2. Decision

**Choose Option C first: the direct gap bound `A_seed - A_raw`.**

Reason:

1. the current theorem lane is explicitly comparative and protocol-tagged;
2. the strongest supported interpretation is not merely “raw is bad” or “seeded is good,” but “seeded access is materially better than raw access”;
3. one-sided bounds can still appear later as supporting lemmas, but the direct gap is the most honest next theorem-facing target.

---

## 3. Consequence

The next proof note should define the weakest useful theorem-facing form of a direct protocol-gap inequality, something like:

```text
A_seed(G, lambda; U_B) - A_raw(G, lambda; U_B) >= Delta_access
```

for a positive comparison quantity `Delta_access` that is still local, protocol-tagged, and finite-horizon.

---

## 4. What Gets Deferred

Separate one-sided upper/lower bounds are **deferred, not rejected**.
They may still be the natural route to proving the direct gap later.

---

## 5. Next Trigger

Write a compact proof note stating the weakest useful direct-gap inequality template for the fixed-protocol accessibility surrogate.
