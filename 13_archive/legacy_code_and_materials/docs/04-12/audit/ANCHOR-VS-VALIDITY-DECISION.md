# Anchor/Identification vs Validity/Exclusion Decision

**Date:** 2026-04-12
**Session:** Cycle 102 — choose the first concrete formalization move for the local target-family pseudodistance
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/LOCAL-TARGET-FAMILY-PSEUDODISTANCE-INGREDIENTS.md; docs/04-12/proof/WEAKEST-USEFUL-DISTFAMILY-NOTION.md

---

## 1. Options

### Option A — anchor / identification first

Meaning:

> first specify the target representative and the symmetry/label identifications that are factored out.

Pros:
- gives the pseudodistance a concrete center immediately;
- resolves the most basic ambiguity in “distance to the family”;
- makes later validity/exclusion rules easier to state.

Cons:
- still leaves the size of the valid neighborhood open;
- does not yet explain where the pseudodistance stops being trustworthy.

### Option B — validity / exclusion first

Meaning:

> first specify the local validity range and the exclusion rule for obvious wrong-family states.

Pros:
- directly targets false positives and overreach;
- makes the pseudodistance safer even before the full anchor side is polished.

Cons:
- difficult to state cleanly without a fixed representative;
- risks describing the boundary of an object whose center is still vague.

---

## 2. Decision

**Choose Option A first: anchor / identification.**

Reason:

1. a local pseudodistance cannot be formalized without first saying what local chart it is centered on;
2. symmetry/label identifications determine when two states count as the “same family” before any validity radius is meaningful;
3. once the anchor side is explicit, the validity/exclusion side becomes a secondary refinement rather than a foundational ambiguity.

---

## 3. Consequence

The next proof note should specify:

- what counts as the target representative,
- which identifications are factored out,
- and why these are the minimum invariances needed for the fixed-protocol theorem lane.

---

## 4. What Gets Deferred

Validity range and wrong-family exclusion are **deferred, not rejected**.
They should be stated next, after the anchor side is fixed.

---

## 5. Next Trigger

Write a short proof note defining the target representative and allowed identifications for the local target-family pseudodistance.
