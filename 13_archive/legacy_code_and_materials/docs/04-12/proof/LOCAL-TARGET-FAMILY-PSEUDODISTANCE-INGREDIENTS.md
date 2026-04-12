# Local Target-Family Pseudodistance Ingredients

**Date:** 2026-04-12
**Session:** Cycle 101 — minimum ingredients for the local target-family pseudodistance
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/WEAKEST-USEFUL-DISTFAMILY-NOTION.md; docs/04-12/proof/UB-NEIGHBORHOOD-DEFINITION.md

---

## 1. Purpose

This note lists the minimum ingredients needed for a local target-family pseudodistance in the fixed-protocol theorem lane.

The goal is not a globally canonical branch metric. The goal is only a usable local notion centered on one target family.

---

## 2. Ingredient 1 — Target representative

The pseudodistance must be anchored at a specific representative of the target family, typically:

- the continued branch representative, or
- the seeded-recovery representative.

Why needed:
- without a chosen representative, the phrase “distance to the family” has no concrete local chart.

---

## 3. Ingredient 2 — Allowed symmetry / label identifications

The pseudodistance should explicitly factor out only the obvious identifications that do not change family membership, for example:

- permutation of equivalent labels,
- graph symmetries already known to preserve the branch,
- trivial sign/ordering conventions if present in the chosen parameterization.

Why needed:
- otherwise the same family may look artificially far from itself.

---

## 4. Ingredient 3 — Local validity range

The pseudodistance must be declared valid only in a small neighborhood around the chosen representative.

Why needed:
- away from the local chart, branch crossings, bifurcation effects, and unrelated families can destroy geometric meaning.

This keeps the object theorem-serving rather than overambitious.

---

## 5. Ingredient 4 — Compatibility with capture language

The pseudodistance must be compatible with the local capture criterion:

```text
small pseudodistance + energetic admissibility
should be enough to test whether return to the target family is plausible.
```

Why needed:
- the theorem lane is about accessibility and persistence, not geometry for its own sake.

---

## 6. Ingredient 5 — Exclusion of obvious wrong-family states

The pseudodistance should separate:
- genuinely nearby target-family states,
from
- coarse lookalikes that are still dynamically Type A / wrong-family outcomes.

Why needed:
- this is exactly the failure mode already seen in Exp79.

---

## 7. Minimal Safe Reading

So the local target-family pseudodistance should be read as:

```text
an anchored, symmetry-aware, locally valid pseudodistance
used only to support the target neighborhood and local capture language.
```

This is enough for the current fixed-protocol theorem lane.

---

## 8. Next Trigger

The next step should decide whether the first concrete formalization move is:

1. specifying the target representative/identifications, or
2. specifying the local validity range and exclusion rule.
