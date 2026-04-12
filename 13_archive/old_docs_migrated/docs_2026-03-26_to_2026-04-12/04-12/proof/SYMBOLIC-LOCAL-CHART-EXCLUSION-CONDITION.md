# Symbolic Local-Chart Exclusion Condition

**Date:** 2026-04-12
**Session:** Cycle 114 — symbolic form of strict branch-distance exclusion for the raw-access upper bound
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/BRANCH-DISTANCE-EXCLUSION-TEMPLATE.md; docs/04-12/proof/TARGET-REPRESENTATIVE-AND-IDENTIFICATIONS.md; docs/04-12/proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md

---

## 1. Purpose

This note rewrites the phrase “strict branch-distance exclusion” into a more theorem-facing local-chart condition for the target family neighborhood.

---

## 2. Local-Chart Exclusion Template

Let the target family `B(lambda)` be represented by its chosen continued/seeded representative and local chart.

A safe symbolic condition is:

```text
for all raw trajectory states x_t produced before protocol termination,
raw-path local deviation from the target chart stays outside the strict admission band.
```

Equivalently, in schematic form:

```text
x_t 
otin U_B^{strict}(lambda)
for every trajectory state visited by the raw protocol,
```

where `U_B^{strict}(lambda)` denotes the strict local target-family neighborhood determined by:
- the anchored local chart,
- the allowed identifications,
- the strict branch-distance threshold,
- and the current local admissibility conventions.

---

## 3. Why This Is More Useful Than the Informal Phrase

The phrase “strict branch-distance exclusion” is helpful descriptively, but the theorem lane needs a condition that already points toward a pathwise statement.

The local-chart form does that because it says:
- not merely that final outputs are far,
- but that the raw protocol fails to visit the admissible target chart at all.

That is closer to the kind of condition an upper bound on `A_raw` would actually use.

---

## 4. Relation to Exp79

Exp79 is the empirical prototype of exactly this condition:
- under strict thresholds, raw outcomes do not count as members of the target family neighborhood,
- while looser thresholds admit only superficial near-misses.

So Exp79 motivates the local-chart exclusion statement as the right symbolic abstraction of the current evidence.

---

## 5. Safe Current Reading

The strongest current reading is:

> raw accessibility is small because the raw protocol's visited states remain outside the strict local target-family chart during its finite run.

This is still not a theorem, but it is a theorem-facing symbolic obstruction.

---

## 6. What Remains Open

- how to quantify the strict admission band most cleanly;
- whether the exclusion condition should be checked for all iterates or only for the relevant sampled trajectory states;
- how to connect this pathwise exclusion condition to a small explicit `eps_raw` bound.

---

## 7. Next Trigger

Now that the raw upper-bound route has a symbolic obstruction form, the next natural step is to return to the complementary seeded lower-bound route.
