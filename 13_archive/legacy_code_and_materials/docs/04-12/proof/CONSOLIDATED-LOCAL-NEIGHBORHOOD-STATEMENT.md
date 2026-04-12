# Consolidated Local Neighborhood Statement

**Date:** 2026-04-12
**Session:** Cycle 104 — merged local-neighborhood template for the fixed-protocol theorem lane
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/TARGET-REPRESENTATIVE-AND-IDENTIFICATIONS.md; docs/04-12/proof/LOCAL-VALIDITY-AND-EXCLUSION-RULE.md; docs/04-12/proof/ENERGY-CAPTURE-CRITERION.md; docs/04-12/proof/UB-NEIGHBORHOOD-DEFINITION.md

---

## 1. Purpose

This note merges the local ingredients developed so far into one theorem-facing neighborhood template for the fixed-protocol basin-access lane.

---

## 2. Consolidated Template

A safe consolidated local neighborhood around the target branch family is:

```text
U_B(lambda)
:= { x :
     x lies inside the small anchored chart around the chosen continued/seeded target representative,
     x is compared modulo the minimal allowed identifications,
     x is energetically admissible relative to B(lambda),
     x is capture-compatible under the fixed protocol,
     and x is not an obvious wrong-family lookalike }.
```

This should be read as a **local theorem-serving neighborhood**, not as a global canonical basin definition.

---

## 3. Ingredient Breakdown

### A. Anchor

The neighborhood is centered on the continued/seeded representative of the target family `B(lambda)` used in the accessibility diagnostics.

### B. Allowed identifications

Only the narrow identification set is factored out:
- equivalent labels,
- known local symmetries preserving the branch,
- trivial convention changes.

### C. Local validity range

The neighborhood is only valid where:
- branch identity does not visibly jump,
- the chosen identifications remain stable,
- and local return/capture still has meaning.

### D. Energy admissibility

States must satisfy a target-relative energy filter such as:

```text
E(x) <= E(B(lambda)) + delta_E.
```

### E. Capture compatibility

States must remain compatible with strong local return:

```text
P(return to B(lambda) | x in local neighborhood) >= c_ret.
```

### F. Wrong-family exclusion

States are excluded if they are merely coarse lookalikes that fail the local branch-anchor or energy/capture side.

---

## 4. Why This Is the Right Level of Consolidation

This merged statement is strong enough to support the fixed-protocol theorem lane because it now says, in one place, what “near the target family” means operationally.

At the same time, it remains weak enough to avoid overclaiming:
- it is local,
- it is protocol-tagged,
- it is branch-family anchored,
- and it does not pretend to solve the global branch-geometry problem.

---

## 5. Relation to Existing Experiments

### Exp79

Supports the exclusion side: raw states can remain outside the target neighborhood even when loose similarity thresholds suggest superficial proximity.

### Exp80

Supports the capture side: sufficiently near states return to the target family with very high reliability.

### Combined role

So the current experiments already instantiate the two most important pieces of the local-neighborhood story:

```text
outside U_B(lambda): hard to enter,
inside U_B(lambda): easy to keep.
```

---

## 6. Current Theorem-Support Reading

The strongest current reading is:

> there is now a coherent theorem-facing local neighborhood template for the target branch family, but its branch-distance component and accessibility surrogate are still only partially formalized.

So this statement is a **structured scaffold**, not a theorem.

---

## 7. What Remains Open

The next remaining ambiguities are now narrower:

1. how to express the local branch-distance piece more symbolically,
2. how to choose a theorem-usable accessibility surrogate `A_*`,
3. how to turn the protocol-gap object into a sharper inequality.

---

## 8. Next Trigger

The next artifact should decide whether to return first to:

1. the branch-distance symbolic form, or
2. the accessibility surrogate `A_*`.
