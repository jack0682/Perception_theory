# eps_raw Positivity Role Note

**Date:** 2026-04-12
**Session:** Cycle 118 — how sampled raw exclusion sharpens the positivity condition
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/SAMPLED-RAW-EXCLUSION-PRINCIPLE.md; docs/04-12/proof/DELTA-ACCESS-COMBINATION-PATTERN.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note explains how the sampled/checkpointed raw exclusion principle tightens the theorem-facing role of `eps_raw` in the positivity condition

```text
eta_seed(G, lambda; U_B) > eps_raw(G, lambda; U_B).
```

---

## 2. Core Interpretation

The sampled raw exclusion principle says:

```text
at the observational resolution currently available,
raw protocol states do not visit the strict local target-family chart.
```

This strengthens the meaning of `eps_raw` from a vague small number into an **obstruction-controlled ceiling**.

So `eps_raw` should now be read as:

```text
a small upper bound justified by checkpointed non-entry
into the strict target-family chart.
```

---

## 3. Why This Helps the Positivity Condition

The positivity condition for the direct protocol gap is

```text
eta_seed > eps_raw.
```

The sampled raw exclusion principle does not by itself prove positivity, but it improves the negative side in exactly the right way:

- it makes `eps_raw` structurally interpretable,
- it ties smallness of `eps_raw` to a concrete pathwise failure mode,
- and it prevents `eps_raw` from floating as a purely empirical fit with no theorem-facing meaning.

So the role of the obstruction principle is:

```text
sampled strict exclusion
=> eps_raw should be small enough to be a meaningful ceiling.
```

---

## 4. Exp79 as the Prototype

Exp79 already shows the raw-side pattern needed here:

- strict target-family thresholds give zero or near-zero raw hits,
- looser thresholds admit only superficial near-misses.

So the theorem-facing meaning of `eps_raw` is no longer merely “some small number”; it is the numerical shadow of strict raw non-entry into the target chart.

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> sampled raw exclusion makes the obstruction side of the accessibility comparison explicit enough that positivity can be pursued by strengthening the seeded floor against a now-structured raw ceiling.

This is still not a theorem, but it is a clean step beyond descriptive raw failure.

---

## 6. What This Does Not Yet Do

This note does **not** yet prove that `eps_raw` is analytically tiny.
It only clarifies why `eps_raw` should be treated as the obstruction-controlled side of the positivity condition.

The remaining job is to decide whether the next theorem lane should:

1. sharpen the seeded floor `eta_seed`, or
2. promote the current raw-side smallness into a stronger symbolic estimate.

---

## 7. Next Trigger

The next refinement should compare two positivity routes:

1. strengthen `eta_seed` as the positive side, or
2. sharpen `eps_raw` further as the obstruction side.
