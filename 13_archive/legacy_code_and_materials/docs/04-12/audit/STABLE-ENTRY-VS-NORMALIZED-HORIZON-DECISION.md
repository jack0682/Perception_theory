# Stable-Entry vs Normalized-Horizon Decision

**Date:** 2026-04-12
**Session:** Cycle 109 — choose the next strengthening move for the fixed-protocol accessibility surrogate
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md; docs/04-12/proof/ENTRY-EVENT-DEFINITION.md; docs/04-12/proof/PROTOCOL-HORIZON-AND-STOPPING-RULE.md

---

## 1. Options

### Option A — strengthen first-hit to stable-entry

Meaning:

> replace the weakest event notion (“first hit”) with a stronger notion that requires meaningful residence/capture after entry.

Pros:
- aligns more closely with the actual local-basin interpretation;
- reduces the risk that brief accidental hits are overcounted;
- stays close to the Exp80-style return/capture evidence.

Cons:
- requires a sharper notion of what counts as “stable enough” after entry;
- may complicate the event definition.

### Option B — strengthen the protocol-native horizon to a normalized stopping notion

Meaning:

> try to normalize different protocol horizons before strengthening the event itself.

Pros:
- could make cross-protocol comparison cleaner;
- directly targets the comparability issue.

Cons:
- compares horizons before the event semantics are fully mature;
- risks standardizing a quantity whose event side is still intentionally weak.

---

## 2. Decision

**Choose Option A first: strengthen first-hit toward stable-entry.**

Reason:

1. the main remaining semantic weakness is still on the event side, not the horizon side;
2. the current local-neighborhood theory is built around capture compatibility, so strengthening the event is the most natural next move;
3. a better event definition will make any later horizon normalization more meaningful.

---

## 3. Consequence

The next proof note should define a strengthened event of the form:

```text
enter U_B(lambda) and remain capture-compatible in a short local sense.
```

This should still remain finite and protocol-tagged, but be stronger than a bare first-hit.

---

## 4. What Gets Deferred

Normalized stopping notions are **deferred, not rejected**.
They should return once the event side is semantically strong enough that horizon comparison is not premature.

---

## 5. Next Trigger

Write a short proof note defining a stable-entry refinement of the current first-hit event.
