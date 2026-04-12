# Weakest Useful dist_family Notion

**Date:** 2026-04-12
**Session:** Cycle 100 — minimal geometric notion for the fixed-protocol theorem lane
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/UB-NEIGHBORHOOD-DEFINITION.md; docs/04-12/proof/ENERGY-CAPTURE-CRITERION.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note asks what the **weakest useful** version of `dist_family` is for the fixed-protocol basin-access theorem lane.

The answer is: we do **not** need a global canonical metric on all branch families yet.
We only need a local, target-anchored notion strong enough to distinguish:

1. states genuinely near the target branch family, from
2. states that are only coarsely similar but dynamically belong elsewhere.

---

## 2. Weakest Useful Requirement

For the current theorem lane, `dist_family` only needs to support the following implication:

```text
if dist_family(x, B(lambda)) is small enough
and x is energetically admissible,
then x is eligible for the local capture/return criterion.
```

So the geometric notion is only required to be:
- **local**,
- **target-family anchored**,
- **compatible with the fixed protocol**,
- and **strong enough to exclude obvious wrong-family states**.

It does **not** yet need to be:
- globally canonical,
- symmetric across all branch families,
- or invariant under every future continuation scenario.

---

## 3. Candidate Minimal Form

The weakest currently useful form is a **local branch-chart pseudodistance** relative to the continued target branch:

```text
dist_family(x, B(lambda)) := local deviation of x from the chosen branch chart
around the continued/seeded representative of B(lambda),
with obvious label/symmetry identifications factored out when needed.
```

Interpretation:
- fix one target representative of `B(lambda)` obtained by continuation/seeded recovery;
- measure deviation relative to that local branch chart;
- use it only near that representative, not as a global metric on the full solution set.

---

## 4. Why This Is Enough Right Now

### Exp79 need

Exp79 only needs a threshold notion saying whether a raw result is near the continued target family or not.
It does not require a global metric geometry of every branch family.

### Exp80 need

Exp80 only needs a local notion saying whether perturbed states return to the same target family.
Again, this is a local family-anchor question, not a global branch taxonomy problem.

### Theorem-lane need

The fixed-protocol theorem lane is trying to state:

```text
hard to enter, easy to keep,
for one named target family under one fixed protocol pair.
```

For that, a local target-anchored pseudodistance is sufficient.

---

## 5. What dist_family Does Not Need To Do Yet

At the current stage, `dist_family` does **not** need to:

1. classify every possible branch family globally;
2. compare arbitrary pairs of unrelated branch families;
3. produce a search-neutral branch ontology;
4. survive large branch jumps across bifurcation points.

Those would be stronger future requirements, but they are not needed for the present theorem lane.

---

## 6. Safe Working Definition

The safest working reading is:

> `dist_family` is presently a local branch-membership surrogate centered on the continued target branch, not a universal metric on the full branch landscape.

This is enough to support:
- Exp79-style exclusion of raw states from the target neighborhood,
- Exp80-style return-to-family language,
- and the local side of the fixed-protocol accessibility-gap statement.

---

## 7. Immediate Consequence

The next geometric refinement should therefore be modest:

```text
formalize dist_family only as a local target-family pseudodistance,
not as a global branch metric.
```

That keeps the theorem lane moving without over-solving the wrong problem.

---

## 8. Next Trigger

Write a compact note describing what ingredients a local target-family pseudodistance should contain (for example representative choice, symmetry/label identifications, and a small-neighborhood validity range).
