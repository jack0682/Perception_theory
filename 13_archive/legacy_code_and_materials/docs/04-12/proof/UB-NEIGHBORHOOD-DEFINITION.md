# U_B(lambda) Neighborhood Definition

**Date:** 2026-04-12
**Session:** Cycle 98 — theorem-facing neighborhood for the target branch family
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ASTAR-VS-UB-LANE-DECISION.md; docs/04-12/proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Purpose

This note proposes a theorem-facing neighborhood `U_B(lambda)` for the target branch family `B(lambda)` in the fixed-protocol accessibility-gap lane.

The goal is not to give a final theorem definition, but to replace the vague phrase “near the target branch” with a structured object tied to existing experiments.

---

## 2. Schematic Definition

A safe current template is:

```text
U_B(lambda; delta_F, delta_E)
  := { x : dist_family(x, B(lambda)) <= delta_F
            and E(x) <= E(B(lambda)) + delta_E }.
```

Interpretation:
- `dist_family(x, B(lambda))` measures geometric/family closeness to the target branch family,
- `delta_F` controls branch-family proximity,
- `delta_E` prevents obviously high-energy states from being counted as neighborhood members merely because of coarse shape similarity.

This is more stable than using energy alone or family distance alone.

---

## 3. Why This Matches Existing Evidence

### Exp79 connection

Exp79 already uses a family-distance threshold relative to the continued branch.

So Exp79 supplies a numerical precursor of the `dist_family <= delta_F` part.

### Exp80 connection

Exp80 perturbs the continued branch and checks whether optimization returns to the same family.

So Exp80 supplies a numerical precursor of the idea that states initialized inside a suitable local neighborhood should return to `B(lambda)`.

### Combined reading

Together, Exp79 and Exp80 suggest the same basic geometric picture:

- there is a neighborhood around the continued branch family that supports reliable return,
- but raw search rarely lands inside that neighborhood.

This is exactly the role `U_B(lambda)` must play in the theorem lane.

---

## 4. Why Purely Distance-Based Neighborhoods Are Not Enough

A family-distance threshold alone is too loose for theorem use because:

1. coarse geometric similarity can still include obviously worse Type A states,
2. different families may come near each other in some projections,
3. the eventual theorem must distinguish “close but wrong basin” from “actually captured by the target family.”

So a mixed definition using both family-distance and energy tolerance is safer.

---

## 5. Why Purely Energy-Based Neighborhoods Are Not Enough

Energy alone is also unsafe because:

1. different branch families may have nearby energies,
2. a low-energy state need not belong to the same target family,
3. the whole accessibility problem is partly about branch identity, not only scalar energy ranking.

Hence `U_B(lambda)` should remain branch-family anchored.

---

## 6. Current Status of Ingredients

| Ingredient | Current level | Role |
|---|---|---|
| family-distance to continued branch | numerical convention already used | primary geometric anchor |
| energy comparison to target branch | available in experiments, not yet standardized | filters out coarse false positives |
| return-to-family criterion after perturbation | strong numerical support | justifies local basin reading |
| theorem-level portability of `dist_family` | open | main unresolved part of the neighborhood definition |

---

## 7. Safe Current Reading

The strongest current reading is:

> there is already a practical numerical approximation to `U_B(lambda)` in the experiments, but its branch-distance component is still a numerical convention rather than a theorem-level metric.

So `U_B(lambda)` is now clearer, but not yet canonical.

---

## 8. Next Trigger

The next refinement should decide which part of `U_B(lambda)` to formalize first:

1. the family-distance component `dist_family`, or
2. the energy tolerance `delta_E` and capture criterion.
