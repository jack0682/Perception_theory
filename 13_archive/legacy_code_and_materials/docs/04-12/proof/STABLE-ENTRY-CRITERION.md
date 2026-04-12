# Stable-Entry Criterion

**Date:** 2026-04-12
**Session:** Cycle 109 — strengthened event for the fixed-protocol accessibility surrogate
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/STABLE-ENTRY-VS-NORMALIZED-HORIZON-DECISION.md; docs/04-12/proof/ENTRY-EVENT-DEFINITION.md; docs/04-12/proof/ENERGY-CAPTURE-CRITERION.md

---

## 1. Purpose

This note strengthens the entry event from bare first-hit to a **stable-entry** notion that is more faithful to the local-basin interpretation.

---

## 2. Stable-Entry Template

A safe strengthened event is:

```text
StableEnter_S(G, lambda; U_B)
:= the protocol trajectory enters U_B(lambda)
   and, after entry, remains compatible with the local capture/return criterion
   for the short local verification window built into the fixed protocol analysis.
```

So stable-entry means more than “touched once”; it means “entered in a way that is not immediately lost.”

---

## 3. Why This Is a Better Event

The theorem lane is not about accidental intersection with the neighborhood.
It is about meaningful access to a target family that is locally stable once reached.

Therefore a stronger event should require:
- actual entry into the theorem-facing local neighborhood,
- and short local persistence/capture compatibility after that entry.

---

## 4. Why This Still Avoids Overreach

This is not yet an asymptotic stability requirement.
It does **not** require:
- infinite-time residence,
- full convergence proof after entry,
- or global basin certification.

It is still local, finite, and protocol-tagged.

---

## 5. Relation to Existing Evidence

### Exp79

Exp79 motivates why first-hit can be too weak: loose closeness alone can misclassify wrong-family states.

### Exp80

Exp80 supplies the strongest current reason to strengthen the event: once the target family is genuinely entered locally, return/capture is highly reliable.

So stable-entry is much closer to the phenomenon actually supported by the current evidence.

---

## 6. Safe Current Reading

The strongest current reading is:

> a protocol has meaningfully accessed the target family when it enters the local neighborhood in a way that remains capture-compatible over the short local verification window.

This is a better event for theorem-facing work than bare first-hit.

---

## 7. What Remains Open

- how to define the short local verification window most cleanly;
- whether stable-entry should later be expressed via repeated hits, local return, or explicit short-time residence;
- how to combine stable-entry with a later normalized stopping notion across protocols.

---

## 8. Next Trigger

Now that the event side is strengthened, the next step is to return to the horizon side and decide whether a more normalized stopping notion is needed.
