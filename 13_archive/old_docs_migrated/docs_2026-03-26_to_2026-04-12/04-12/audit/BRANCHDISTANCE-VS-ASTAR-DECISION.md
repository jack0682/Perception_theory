# Branch-Distance vs A_* Decision

**Date:** 2026-04-12
**Session:** Cycle 105 — choose the next refinement after the consolidated local-neighborhood template
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md; docs/04-12/proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md; docs/04-12/proof/WEAKEST-USEFUL-DISTFAMILY-NOTION.md

---

## 1. Options

### Option A — sharpen the branch-distance symbolic form

Meaning:

> keep refining the local pseudodistance side until `dist_family` has a more explicit symbolic form.

Pros:
- would clean up the remaining geometric ambiguity;
- could make neighborhood membership more explicit.

Cons:
- the local pseudodistance is already strong enough for the current theorem lane;
- more branch-geometry refinement risks over-investing in the local scaffold instead of the actual theorem quantity.

### Option B — sharpen the accessibility surrogate `A_*`

Meaning:

> return to the protocol-gap object and choose a theorem-usable surrogate for accessibility under the now-stabilized local neighborhood.

Pros:
- directly advances the quantity that appears in the fixed-protocol accessibility gap;
- matches the main theorem-facing bottleneck after the local neighborhood scaffold is in place;
- uses Exp79/Exp80/Exp82 more directly.

Cons:
- still depends on the local neighborhood template being accepted as sufficiently stable;
- may need to revisit branch-distance details later.

---

## 2. Decision

**Choose Option B first: sharpen `A_*`.**

Reason:

1. the local branch-distance side is now adequate as a theorem-serving scaffold;
2. the real unresolved quantity in the fixed-protocol theorem lane is still the accessibility object itself;
3. Exp79, Exp80, and Exp82 already suggest what kind of accessibility surrogate is natural, so this is now the more proof-feasible move.

---

## 3. Consequence

The next proof note should identify the **weakest useful theorem-usable accessibility surrogate** for the fixed-protocol lane.

That surrogate should be:
- protocol-tagged,
- local-neighborhood based,
- compatible with the current capture language,
- and simple enough to compare between `S_raw` and `S_seed`.

---

## 4. What Gets Deferred

The symbolic polishing of `dist_family` is deferred, not rejected.
It can return later once the accessibility surrogate has been fixed and the remaining geometric ambiguity is easier to isolate.

---

## 5. Next Trigger

Write a compact proof note defining the weakest useful theorem-usable accessibility surrogate `A_*` for the fixed-protocol basin-access lane.
