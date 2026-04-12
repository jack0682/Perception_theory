# Entry Event Definition for U_B(lambda)

**Date:** 2026-04-12
**Session:** Cycle 106 — event-level refinement of the accessibility surrogate
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ENTRY-EVENT-VS-HORIZON-DECISION.md; docs/04-12/proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md; docs/04-12/proof/WEAKEST-USEFUL-ASTAR-SURROGATE.md

---

## 1. Purpose

This note defines the event “enter `U_B(lambda)`” for the fixed-protocol accessibility surrogate.

---

## 2. Event Template

A safe current event is:

```text
Enter_{S}(G, lambda; U_B)
:= there exists an iteration/time within the protocol run
   at which the trajectory state x_t satisfies the local-neighborhood conditions defining U_B(lambda).
```

So entry means a **first hit of the theorem-facing local neighborhood** during the protocol run.

---

## 3. Why First-Hit Language Is Best Right Now

First-hit language is the weakest useful event because:
- it matches the idea of accessibility directly,
- it does not yet force a stronger permanence condition,
- and it can later be strengthened if theorem needs require stable residence rather than simple entry.

At this stage, “can the protocol reach the target neighborhood at all?” is the primary question.

---

## 4. Relation to Capture Compatibility

Entry alone is not the whole theorem lane.

The local-neighborhood template already includes capture compatibility, so the intended reading is:

```text
entry into U_B(lambda)
means entry into a neighborhood that is already designed
so that local return/capture is meaningful.
```

Thus the event is not a loose geometric hit on a raw set; it is a hit on the **theorem-facing local neighborhood**.

---

## 5. Why Transient Near-Misses Should Not Count

A transient near-miss should not count as entry if it does not satisfy the neighborhood conditions simultaneously.

This is important because:
- loose superficial similarity was already shown to be misleading in Exp79,
- and the theorem lane is trying to track genuine access to the target family, not brief accidental proximity.

So the event should require an actual hit of the full local neighborhood template, not just partial similarity.

---

## 6. Safe Current Reading

The strongest current reading is:

> a protocol has accessed the target family when its trajectory first enters the consolidated local neighborhood `U_B(lambda)` during the fixed run.

This gives the accessibility surrogate a meaningful event without yet overcommitting on time asymptotics.

---

## 7. What Remains Open

- whether the event should later be strengthened from first-hit to stable-entry;
- how the stopping horizon should be fixed;
- how to estimate or bound the resulting event probability analytically.

---

## 8. Next Trigger

Now that the event is explicit, the next step is to define the protocol horizon/stopping rule that turns this event into a complete accessibility probability.
