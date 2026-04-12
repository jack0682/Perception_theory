# Branch-Distance Exclusion Template for eps_raw

**Date:** 2026-04-12
**Session:** Cycle 113 — weakest useful branch-distance obstruction for the raw-access upper bound
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/EPSRAW-BRANCHDISTANCE-VS-ENERGYCAPTURE-DECISION.md; docs/04-12/proof/ARAW-UPPER-BOUND-TEMPLATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note states the weakest useful branch-distance-exclusion template for controlling the raw-access upper bound `eps_raw`.

---

## 2. Template

A safe current template is:

```text
if the raw protocol fails to enter the strict branch-family neighborhood
at the chosen target lambda,
then A_raw(G, lambda; U_B) <= eps_raw(G, lambda; U_B)
with eps_raw small.
```

More suggestively:

```text
strict branch-distance exclusion
=> small raw accessibility.
```

At this stage, `eps_raw` is still a theorem-facing placeholder, not an analytic formula.

---

## 3. Why This Is the Right First Obstruction

The raw-access side is currently sharpest at the level of **not getting close enough** to the target family.

That is exactly what Exp79 measures:
- under strict family-distance thresholds,
- raw hits are zero or near-zero,
- even though looser thresholds admit superficial near-misses.

So the first theorem-facing obstruction should preserve that structure.

---

## 4. What This Template Captures

It captures the most immediate negative statement available now:

- the raw protocol does not meaningfully enter the local target-family chart,
- therefore its accessibility to the target neighborhood is small.

This is the natural obstruction half of the direct protocol gap.

---

## 5. What It Does Not Yet Capture

This template does not yet say:
- why branch-distance exclusion happens,
- how to compute `eps_raw` analytically,
- or how branch-distance exclusion interacts with the later capture side.

Those are later refinements.

---

## 6. Safe Current Reading

The strongest current theorem-support reading is:

> raw accessibility should first be controlled through the empirical fact that raw trajectories fail to enter the strict target-family neighborhood at the target lambda.

This is weaker than a full theorem, but it is the clearest starting form for `A_raw <= eps_raw`.

---

## 7. Next Trigger

The next refinement should ask how to translate strict branch-distance exclusion into a more symbolic condition on the local target-family chart.
