# Target Representative and Allowed Identifications

**Date:** 2026-04-12
**Session:** Cycle 102 — anchor side of the local target-family pseudodistance
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ANCHOR-VS-VALIDITY-DECISION.md; docs/04-12/proof/LOCAL-TARGET-FAMILY-PSEUDODISTANCE-INGREDIENTS.md

---

## 1. Purpose

This note fixes the anchor side of the local target-family pseudodistance for the fixed-protocol theorem lane.

---

## 2. Target Representative

The default anchor should be:

```text
the continued/seeded representative of the target branch family B(lambda)
used in the accessibility diagnostics.
```

Concretely, this means:
- start from the named target family obtained by continuation or seeded recovery,
- use that recovered representative at the target `lambda` as the center of the local chart.

Why this choice is best now:
- it is already the object used in Exp79 and Exp80,
- it is the branch family whose accessibility/persistence asymmetry is actually under study,
- and it avoids pretending that a search-neutral representative has already been identified.

---

## 3. Allowed Identifications

The pseudodistance should factor out only the minimum obvious identifications:

1. **label permutations** that do not change family membership in the chosen representation;
2. **known graph symmetries** already recognized to preserve the branch in the local setting;
3. **trivial convention changes** (ordering / sign / indexing conventions) that do not alter the branch family itself.

This list should stay narrow.

Reason:
- every extra identification weakens the geometry,
- and the current theorem lane needs a strict local object, not a permissive global quotient.

---

## 4. Safe Working Rule

A state `x` is compared to the target family by first:

1. choosing the continued/seeded target representative,
2. quotienting by the small allowed identification set,
3. then measuring local deviation in that anchored chart.

So the pseudodistance is not “distance to every equivalent thing imaginable,” but distance to the target family after only the most unavoidable local identifications are removed.

---

## 5. Why This Fits Existing Experiments

### Exp79

Exp79 already measures closeness to the continued target branch, not to a global search-neutral family average.

### Exp80

Exp80 already tests perturb-and-return relative to the same continued target branch.

So the anchor side was already implicit; this note simply makes it explicit.

---

## 6. What Remains Open

- how large the local chart may be before the pseudodistance loses meaning;
- how to formulate the exclusion rule for wrong-family lookalikes;
- whether additional identifications become necessary in harder symmetry cases.

---

## 7. Next Trigger

Now that the anchor side is explicit, the next step is to define the local validity range and the wrong-family exclusion rule.
