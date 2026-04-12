# Local Validity Range and Exclusion Rule

**Date:** 2026-04-12
**Session:** Cycle 103 — validity and exclusion side of the local target-family pseudodistance
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/TARGET-REPRESENTATIVE-AND-IDENTIFICATIONS.md; docs/04-12/proof/ENERGY-CAPTURE-CRITERION.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note formalizes the remaining side of the local target-family pseudodistance:

1. the **local validity range**, and
2. the **wrong-family exclusion rule**.

---

## 2. Local Validity Range

The anchored pseudodistance should be declared valid only for states inside a small chart around the chosen target representative.

A safe theorem-facing reading is:

```text
The pseudodistance is valid only on the region where
- branch identity does not visibly jump,
- the chosen identifications remain stable,
- and the local capture criterion is still meaningful.
```

So “small enough” means: small enough that the target branch family still behaves as one coherent local object.

---

## 3. Why a Local Range Is Necessary

Without an explicit local range:
- unrelated branch families may enter the chart,
- bifurcation effects may invalidate the pseudodistance,
- and branch membership may become chart-dependent.

Therefore the pseudodistance must be local by contract, not merely by intuition.

---

## 4. Wrong-Family Exclusion Rule

A state should be excluded from the target neighborhood if it is only a coarse lookalike of the target family.

A safe working exclusion rule is:

```text
exclude x if it fails either:
1. the local energy/capture side, or
2. the local branch-anchor compatibility test.
```

In practical terms, this means a state is not admitted if:
- it is too far from the anchored representative in the local chart,
- or it does not return to the target family under the fixed protocol,
- or it is an obviously wrong-family low-quality proxy despite superficial similarity.

---

## 5. Exp79 Anchor for the Exclusion Rule

Exp79 already shows the relevant failure mode:

- coarse Type A outputs can appear “not too far” only under loose thresholds,
- yet they remain clearly worse in energy and wrong in family identity.

So the exclusion rule must explicitly prevent those states from counting as members of `U_B(lambda)`.

This is why the neighborhood cannot be based on a loose family-threshold alone.

---

## 6. Combined Local Reading

Putting the pieces together, the target neighborhood is now best read as:

```text
U_B(lambda)
= states inside a small anchored chart,
  energetically admissible,
  capture-compatible,
  and not merely coarse wrong-family lookalikes.
```

This is not yet fully canonical, but it is precise enough for the current fixed-protocol theorem lane.

---

## 7. What Remains Open

- how to phrase the local range in theorem-ready symbolic form;
- how to make the branch-anchor compatibility test more explicit;
- how to convert the exclusion rule from a narrative criterion into a compact usable condition.

---

## 8. Next Trigger

The next step should compress the current ingredients into one consolidated theorem-facing local neighborhood statement.
