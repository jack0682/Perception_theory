# eps_raw Structural Control Note

**Date:** 2026-04-12
**Session:** Cycle 116 — weakest useful structural control for the raw-access ceiling
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/EPSRAW-VS-ETASEED-POSITIVITY-DECISION.md; docs/04-12/proof/BRANCH-DISTANCE-EXCLUSION-TEMPLATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note asks what the weakest useful structural control on `eps_raw` should be.

---

## 2. Candidate Control Shape

The present theorem-facing direction is:

```text
eps_raw is small because the raw protocol remains outside the strict local target-family chart.
```

So the natural structural control should be something like:

```text
strict local-chart exclusion under the raw protocol
=> small eps_raw.
```

This is weaker than a full dynamical theorem, but already stronger than a purely empirical statement.

---

## 3. Why This Is the Right Next Refinement

At the current stage, `eps_raw` does not need a global closed-form formula.
It only needs a structural obstruction principle explaining why the raw protocol rarely accesses `U_B(lambda)`.

The branch-distance-exclusion side is already closest to that goal.

---

## 4. Safe Current Reading

The strongest current theorem-support reading is:

> raw accessibility is small because the raw optimization path stays outside the strict target-family chart over the protocol's finite run.

This is the obstruction principle that should be sharpened next.

---

## 5. What Remains Open

- whether the strict chart exclusion should be stated pointwise for all iterates or in a weaker sampled-trajectory form;
- how to quantify the admission band of the chart;
- how to eventually translate this structural obstruction into an explicit small quantity.

---

## 6. Next Trigger

The next step should decide whether the raw structural control should be phrased at the level of all iterates or only at the level of sampled/checkpointed trajectory states.
