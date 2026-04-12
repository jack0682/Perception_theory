# Sampled/Checkpointed Raw Exclusion Principle

**Date:** 2026-04-12
**Session:** Cycle 117 — evidence-aligned obstruction form for the raw-access upper bound
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ALL-ITERATE-VS-SAMPLED-EXCLUSION-DECISION.md; docs/04-12/proof/SYMBOLIC-LOCAL-CHART-EXCLUSION-CONDITION.md

---

## 1. Purpose

This note states the current strongest evidence-aligned obstruction form for the raw-access upper bound.

---

## 2. Principle

A safe current principle is:

```text
If the sampled/checkpointed states of the raw trajectory
remain outside the strict local target-family chart,
then the raw protocol's accessibility to the target neighborhood is small.
```

This is the checkpointed analogue of the stronger all-iterate obstruction principle.

---

## 3. Why This Is the Right Strength Now

It is stronger than a purely qualitative statement because it ties raw failure to a specific pathwise observational condition.
It is weaker than a full dynamical theorem because it only asserts exclusion at the states the current diagnostics actually inspect.

That is exactly the right tradeoff for the current stage.

---

## 4. Relation to Exp79 and Exp82

### Exp79

Exp79 already reports exclusion at the level of observed raw outputs relative to the strict target-family thresholds.

### Exp82

Exp82 supports the broader picture that raw trajectories occupy the wrong corridor from the start.
This makes the sampled/checkpointed exclusion principle more plausible than a mere final-state coincidence.

Together, these two experiments justify a pathwise obstruction principle at the sampled/checkpointed level.

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> at the observational resolution currently available, raw trajectories do not visit the strict target-family chart in a way that would support nontrivial raw accessibility.

This is enough to support the present raw upper-bound route.

---

## 6. What Remains Open

- whether checkpointed exclusion can later be upgraded to all-iterate exclusion;
- how dense the checkpoints must be for theorem use;
- how to express the checkpointed exclusion principle more symbolically in local-chart terms.

---

## 7. Next Trigger

The next step should merge the sampled raw exclusion principle back into the raw upper-bound route and ask how it contributes quantitatively to the positivity condition `eta_seed > eps_raw`.
