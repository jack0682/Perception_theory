# eps_raw Branch-Distance vs Energy/Capture Decision

**Date:** 2026-04-12
**Session:** Cycle 113 — choose what should control the raw-access upper bound first
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/ARAW-UPPER-BOUND-TEMPLATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-12/proof/ENERGY-CAPTURE-CRITERION.md

---

## 1. Options

### Option A — tie `eps_raw` first to branch-distance exclusion

Meaning:

> use the fact that raw trajectories fail to enter the strict branch-family neighborhood as the primary controlling structure for `eps_raw`.

Pros:
- matches Exp79 most directly;
- gives a clean obstruction picture: raw trajectories remain outside the target-family chart;
- is the most natural starting point for a small-access upper bound.

Cons:
- branch-distance is still only partially formalized;
- may inherit some geometric ambiguity from the local pseudodistance side.

### Option B — tie `eps_raw` first to the energy/capture side

Meaning:

> make the raw upper bound depend first on failure of energetic admissibility or local capture compatibility.

Pros:
- uses more native energetic/dynamical objects;
- may eventually integrate better with stable-entry language.

Cons:
- raw failure is currently seen most clearly before capture, at the level of strict neighborhood exclusion;
- can blur the clean empirical message that raw runs simply fail to get close enough in the first place.

---

## 2. Decision

**Choose Option A first: tie `eps_raw` to branch-distance exclusion.**

Reason:

1. Exp79 already gives the cleanest present raw-side fact: strict branch-family access is zero or near-zero;
2. this makes branch-distance exclusion the most direct empirical prototype for a small `eps_raw`;
3. energy/capture can still enter later as a refinement, but the initial obstruction is geometrically “failed entry,” not “entered but failed capture.”

---

## 3. Consequence

The next proof note should state a theorem-facing raw-access obstruction of the form:

```text
strict branch-distance exclusion implies small A_raw.
```

This keeps the first raw upper-bound target tightly aligned with the strongest current evidence.

---

## 4. What Gets Deferred

The energy/capture route is **deferred, not rejected**.
It should return later when the theorem lane needs to connect the raw upper bound more tightly to the local-basin side.

---

## 5. Next Trigger

Write a compact proof note describing the weakest useful branch-distance-exclusion template for controlling `eps_raw`.
