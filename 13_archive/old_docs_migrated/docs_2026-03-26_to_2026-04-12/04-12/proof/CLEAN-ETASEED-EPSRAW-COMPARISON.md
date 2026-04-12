# Clean eta_seed vs eps_raw Comparison Form

**Date:** 2026-04-12
**Session:** Cycle 120 — clean theorem-facing comparison between the seeded floor and the raw ceiling
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/ETASEED-STRUCTURAL-SUPPORT-NOTE.md; docs/04-12/proof/EPSRAW-POSITIVITY-ROLE-NOTE.md; docs/04-12/proof/DELTA-ACCESS-COMBINATION-PATTERN.md

---

## 1. Purpose

This note states the cleanest current theorem-facing comparison between `eta_seed` and `eps_raw` inside the direct protocol-gap inequality.

---

## 2. Clean Comparison Form

The current comparison should be read as:

```text
seeded stable-entry floor > raw obstruction-controlled ceiling.
```

More explicitly,

```text
eta_seed(G, lambda; U_B) > eps_raw(G, lambda; U_B).
```

This is the right current comparison form because it keeps both sides tied to their distinct roles:
- `eta_seed` = positive access floor supported by stable-entry-compatible seeded access,
- `eps_raw` = small ceiling supported by sampled/checkpointed strict exclusion of the raw path.

---

## 3. Why This Is Cleaner Than the Raw Algebra Alone

The algebraic subtraction

```text
Delta_access >= eta_seed - eps_raw
```

is correct, but it hides the asymmetry unless the two ingredients are interpreted structurally.

The cleaner theorem-facing reading is:

- the seeded side is a **floor of meaningful access**,
- the raw side is a **ceiling created by structured non-entry**,
- and positivity means the floor dominates the ceiling.

That is the conceptual form the theorem lane should preserve.

---

## 4. Structural Reading of Each Side

### Seeded side

`eta_seed` is not just “some positive number.” It stands for the positive stable-entry support that the seeded protocol enjoys relative to the target local neighborhood.

### Raw side

`eps_raw` is not just “some small number.” It stands for an obstruction-controlled ceiling justified by sampled raw exclusion from the strict local target-family chart.

So the comparison is not symmetric in meaning even if it is symmetric in algebra.

---

## 5. Safe Current Interpretation

The strongest current theorem-support reading is:

> the direct protocol-gap becomes positive when the structurally supported seeded access floor exceeds the structurally controlled raw non-entry ceiling.

This is the cleanest current comparison statement available.

---

## 6. What Remains Open

- how large a strict positivity margin must be to count as theorem-useful;
- whether `eta_seed` and `eps_raw` can be controlled by comparable local quantities;
- whether a stronger direct statement can be made without first improving one side further.

---

## 7. Next Trigger

The next step should decide whether to tighten the comparison by:

1. strengthening the seeded floor further, or
2. shrinking the raw ceiling further.
