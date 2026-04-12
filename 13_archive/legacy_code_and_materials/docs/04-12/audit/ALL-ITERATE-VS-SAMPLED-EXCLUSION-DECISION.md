# All-Iterate vs Sampled-Exclusion Decision

**Date:** 2026-04-12
**Session:** Cycle 117 — choose the pathwise strength of the raw exclusion statement
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/EPSRAW-STRUCTURAL-CONTROL-NOTE.md; docs/04-12/proof/SYMBOLIC-LOCAL-CHART-EXCLUSION-CONDITION.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Options

### Option A — all-iterate exclusion

Meaning:

> require that every iterate of the raw protocol remain outside the strict target-family chart.

Pros:
- gives the strongest possible obstruction form;
- would be especially clean as a theorem statement.

Cons:
- stronger than what current evidence directly monitors;
- may overstate pathwise control relative to the current diagnostics.

### Option B — sampled/checkpointed exclusion

Meaning:

> require exclusion only for the sampled or checkpointed trajectory states that the current diagnostics actually track.

Pros:
- matches existing evidence directly;
- avoids pretending to know full iterate-level geometry already;
- still gives a theorem-facing obstruction principle at the observational resolution currently available.

Cons:
- weaker than an all-iterate statement;
- may need strengthening later if finer pathwise control becomes necessary.

---

## 2. Decision

**Choose Option B first: sampled/checkpointed exclusion.**

Reason:

1. current evidence is strongest at the sampled/checkpointed level, not at a full iterate-by-iterate level;
2. the theorem lane should not silently smuggle in stronger pathwise control than the diagnostics justify;
3. once a sampled exclusion principle is explicit, it can later be strengthened if finer trajectory control is actually needed.

---

## 3. Consequence

The raw upper-bound route should now be read as:

```text
sampled/checkpointed raw states remain outside the strict target-family chart
=> raw accessibility is small.
```

This keeps the obstruction principle honest and evidence-aligned.

---

## 4. What Gets Deferred

The all-iterate form is **deferred, not rejected**.
It can return later if the theorem lane eventually demands stronger dynamical control than the checkpointed diagnostics provide.

---

## 5. Next Trigger

Write a short proof note stating the sampled/checkpointed exclusion principle as the current raw-side obstruction form.
