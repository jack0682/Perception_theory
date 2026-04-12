# Entry Event vs Horizon Decision

**Date:** 2026-04-12
**Session:** Cycle 106 — choose the first concrete refinement inside the accessibility surrogate A_*
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/WEAKEST-USEFUL-ASTAR-SURROGATE.md; docs/04-12/proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md

---

## 1. Options

### Option A — formalize the event “enter `U_B(lambda)`” first

Meaning:

> define exactly what counts as entering the target local neighborhood before refining the protocol horizon.

Pros:
- the event is logically prior to the probability built from it;
- avoids discussing horizons for an event that is still ambiguous;
- aligns with the current state of the project, where `U_B(lambda)` has only just been consolidated.

Cons:
- still leaves the time/horizon part open;
- may produce a partially specified accessibility object.

### Option B — formalize the protocol horizon/stopping rule first

Meaning:

> fix the finite optimization horizon or stopping rule before clarifying entry itself.

Pros:
- could standardize comparisons across protocols;
- directly addresses one explicit open item in the surrogate note.

Cons:
- horizon without a precise event is secondary;
- risks over-specifying runtime details before the mathematical object is settled.

---

## 2. Decision

**Choose Option A first: formalize the event “enter `U_B(lambda)`”.**

Reason:

1. the entry event is the semantic core of the accessibility surrogate;
2. once the entry event is fixed, the horizon becomes a technical wrapper around an already meaningful object;
3. current experiments are already organized around practical entry/exclusion judgments, so the event side is closer to existing evidence than the horizon side.

---

## 3. Consequence

The next proof note should define what it means for a protocol trajectory to count as entering the theorem-facing local neighborhood.

At minimum, it should explain:
- whether entry means first hit of `U_B(lambda)`,
- whether transient hits count,
- and how entry interacts with capture compatibility.

---

## 4. What Gets Deferred

The protocol horizon/stopping rule is **deferred, not rejected**.
It should return after the event itself is precise enough to support a probability statement.

---

## 5. Next Trigger

Write a short proof note defining the event “enter `U_B(lambda)`” for the fixed-protocol theorem lane.
