# Relaxed Merge Sublevel-Set Separation / Shortcut Analysis

**Date:** 2026-04-10
**Session:** Cycle 26 — relaxed merge sublevel connectivity analysis
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/proof/RELAXED-MERGE-MEP-AFTER-ESCAPE.md; docs/04-10/proof/RELAXED-LOCAL-BASIN-BARRIER.md

---

## 1. CURRENT GAP

The current question is whether, after exiting the local basin of a strict K=2 branch `B`, every path to the embedded K=1 target `T=(u_merged,0)` must pay an additional boundary/morphology cost.

Equivalently:

```text
Are the local exit sphere and T disconnected inside low sublevel sets of E_R?
```

---

## 2. Decision Summary

A post-escape barrier is **not automatic**. It is a sublevel-set separation condition.

The dissolve-spread-transfer-reconcentrate route is a real admissible path class in the relaxed manifold unless explicitly forbidden. It does not by itself prove zero additional barrier, but it invalidates any proof that only analyzes direct interpolation or core-core overlap.

Thus the correct status is:

```text
OPEN-CONDITIONAL:
additional barrier requires either
  (a) sublevel-set disconnection proof, or
  (b) path-class restriction excluding diffuse transfer shortcuts.
```

---

## 3. Why Direct-Path Barriers Overestimate MEP

Direct interpolation typically forces two high-density cores to overlap or pass through spinodal mixtures. That can create an `O(beta)` double-well cost.

But the relaxed manifold permits paths that first lower density / spread one component before transfer. These paths can avoid direct core-core overlap. Therefore:

```text
direct interpolation barrier >= true MEP barrier
```

with strict inequality possible.

---

## 4. Shortcut Path Class

A schematic shortcut path is:

1. **soften:** reduce peak of `u2` while preserving total mass across `u1+u2`;
2. **spread:** distribute `u2` over a broad low-density region;
3. **transfer:** move diffuse mass into `u1` or total field without core-core collision;
4. **reconcentrate:** relax total field toward `u_merged`.

This path may pay boundary/morphology cost during spreading, but that cost is not the same as direct overlap cost and may be lower.

---

## 5. What Would Prove Separation

To prove additional `eta>0`, one must show that every path from the local exit sphere to `T` crosses a morphology bottleneck. Possible sufficient conditions:

| Condition | Meaning |
|---|---|
| mass-density constraint | disallow arbitrarily diffuse transfer states |
| core-preservation path class | require each formation core remains above threshold until transfer event |
| bounded interface length | prevent spreading over arbitrarily large boundary |
| lower bound on double-well excursion | show any dissolution pays at least fixed `W` cost |
| sublevel topology theorem | prove `T` and exit sphere lie in different components of `{E_R <= h}` |

None of these is currently part of the unrestricted relaxed path class.

---

## 6. What Can Be Claimed Now

| Claim | Status |
|---|---|
| local basin barrier | proved |
| target outside local basin under mass/radius condition | proved |
| direct interpolation barrier | path-specific upper bound |
| additional post-escape barrier | unproved, path-class conditional |
| diffuse shortcut | real obstruction class |
| universal global MEP lower bound | not established |

---

## 7. Corrected Theorem Form

A valid future theorem should be stated as:

> For a specified relaxed path class `P` satisfying a no-diffuse-transfer or morphology-bottleneck condition, the post-escape sublevel set containing the local exit sphere is separated from the K=1 target below level `E_R(B)+local_escape+eta`. Hence the relaxed merge barrier is at least `local_escape+eta`.

Without such a condition, the best current lower bound is the local escape barrier.

---

## 8. Registry Delta

R4 remains **OPEN-CONDITIONAL**.

The campaign has now isolated the exact missing theorem:

> sublevel-set separation for the chosen relaxed path class.

---

## 9. Next Trigger

Proceed to define a restricted path class where a morphology bottleneck theorem might be true.

First move:

> Define `P_core-preserving`: paths where both formations retain a core above threshold until a discrete transfer event. Prove a lower bound or show this path class is too artificial for SCC dynamics.
