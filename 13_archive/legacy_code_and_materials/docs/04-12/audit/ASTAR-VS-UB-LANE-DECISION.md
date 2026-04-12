# A_* vs U_B Lane Decision

**Date:** 2026-04-12
**Session:** Cycle 97 — choose the first ambiguity-reduction step for the fixed-protocol accessibility gap
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md; docs/04-12/proof/FIXED-PROTOCOL-BASIN-ACCESS-THEOREM-CANDIDATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Options

### Option A — sharpen the accessibility surrogate `A_*`

Meaning:

> choose one theorem-usable surrogate for accessibility first, such as entry probability, finite-step capture probability, or return probability under perturbation.

Pros:
- moves the protocol-gap quantity closer to a theorem statement;
- could unify Exp79/Exp80/Exp82 under one probabilistic object;
- helps later comparison inequalities.

Cons:
- still depends on what counts as being "inside" the target family;
- risks defining a quantity before its target set is stable;
- may force premature choices between incompatible surrogates.

### Option B — sharpen the neighborhood `U_B(lambda)`

Meaning:

> first define more clearly what neighborhood captures the target branch family for theorem purposes.

Pros:
- stabilizes the target of every later accessibility quantity;
- fits the current evidence, which already uses family-distance and seeded-return neighborhoods implicitly;
- avoids building theorem language on a moving target.

Cons:
- does not by itself solve the probability/surrogate question;
- still leaves the quantitative accessibility object open.

---

## 2. Decision

**Choose Option B first: sharpen `U_B(lambda)`.**

Reason:

1. every candidate `A_*` depends on a target neighborhood, so defining `A_*` first would build on an unstable base;
2. the current experiments already give practical neighborhood surrogates (family-distance thresholds in Exp79 and perturbation-return neighborhoods in Exp80);
3. a sharper `U_B(lambda)` should make it easier to decide later whether `A_*` should be an entry probability, a capture probability, or another surrogate.

---

## 3. Consequence

The next theorem-facing artifact should define a neighborhood candidate of the form:

```text
U_B(lambda) = { states sufficiently close to the continued / seeded target branch family }
```

and explain:
- how closeness is measured,
- why this neighborhood is compatible with the existing experiments,
- and which parts are merely numerical conventions versus plausible theorem ingredients.

---

## 4. What Gets Deferred

Choosing `U_B(lambda)` first does **not** reject the accessibility-surrogate lane.

It only says that the surrogate should be chosen *after* the target neighborhood is no longer ambiguous.

---

## 5. Next Trigger

Write a compact note proposing a theorem-facing definition of `U_B(lambda)` and mapping it to the existing family-distance and seeded-return diagnostics.
