# Energy/Capture Criterion Inside U_B(lambda)

**Date:** 2026-04-12
**Session:** Cycle 99 — theorem-facing energy/capture side of the target neighborhood
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/DISTFAMILY-VS-ENERGY-CAPTURE-DECISION.md; docs/04-12/proof/UB-NEIGHBORHOOD-DEFINITION.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Purpose

This note formalizes the energy/capture part of the theorem-facing neighborhood `U_B(lambda)` while leaving the branch-family metric itself provisional.

---

## 2. Energy-Admissible Capture Template

A safe local criterion is:

```text
x belongs to the capture-compatible side of U_B(lambda)
if
  E(x) <= E(B(lambda)) + delta_E
and
  descent from x returns to the target family B(lambda)
with probability/rate at least c_ret.
```

So the neighborhood is not just “low energy,” and not just “close in shape,” but:

- energetically admissible relative to the target family, and
- dynamically captured by the target family under the fixed protocol.

---

## 3. Why Energy Alone Is Not Enough

Energy tolerance `delta_E` serves only as a filter.

By itself it cannot distinguish:
- the right basin from a nearby wrong basin,
- or a low-energy false positive from a truly captured state.

Therefore the capture condition is essential.

---

## 4. Why Capture Matters

The central theorem-lane phenomenon is:

```text
hard to enter, easy to keep.
```

The “easy to keep” side is naturally expressed by a capture/return criterion:

```text
P(return to B(lambda) | x in local neighborhood) >= c_ret.
```

This is the theorem-facing form of the Exp80 observation.

---

## 5. Experimental Anchor

### Exp80 anchor

Exp80 and dense Exp80 show that perturbations around the continued target branch return to the same family with near-perfect frequency on the tested sigma ladder.

So the current local-basin evidence already supports the following numerical reading:

```text
for tested local perturbations, c_ret is empirically very close to 1.
```

This is not yet a theorem bound, but it is a strong numerical prototype.

---

## 6. Current Safe Use

The strongest current theorem-support use of the energy/capture criterion is:

> once a state lies in a sufficiently small, energetically admissible neighborhood of the target family, the descent dynamics are numerically observed to return to that family with very high reliability.

This is enough to support local-basin language in the fixed-protocol lane.

---

## 7. What Remains Open

- how `delta_E` should scale with config / lambda;
- how to state capture without already presupposing a perfect family metric;
- how to combine the capture criterion with a theorem-usable version of `dist_family`.

---

## 8. Next Trigger

Return to the deferred geometric side and decide how much of `dist_family` must be formalized for the theorem lane to proceed.
