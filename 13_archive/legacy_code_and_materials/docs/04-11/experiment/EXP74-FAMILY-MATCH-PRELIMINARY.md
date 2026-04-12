# Exp74 Family-Match Preliminary

**Date:** 2026-04-11
**Session:** Cycle 58 — family-matched branch-threshold audit
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-10/experiment/EXP73-CATALOG-GRID-PRELIMINARY.md; experiments/exp74_branch_family_match.py; experiments/results/exp74_family_match_summary.json

---

## 1. CURRENT GAP

The expanded Exp73 catalog showed that the first source-0 anchored frozen crossing is not uniformly tiny. The next question is sharper:

> are those early crossings caused by smooth continuation within the same branch family, or by switching to a different family altogether?

Exp74 adds a family-matching layer based on branch type, center offset, overlap, and separation jointly.

---

## 2. Matching Rule

For each config:

1. select the best discovered source-`lambda=0` representative;
2. compute the **global** first frozen crossing against every discovered representative;
3. among positive-`lambda` representatives with the **same branch type**, find the nearest family match using

```text
sqrt(((Δ center_offset)/0.03)^2 + ((Δ overlap)/0.75)^2 + ((Δ separation)/(0.15*side))^2)
```

4. accept that candidate as a matched family only if the distance is at most `2.5`.

This does not prove true analytic continuation, but it is stricter than the raw catalog minimum.

---

## 3. Global vs Family-Matched Crossings

| Config | Global first crossing | Matched-family crossing | Interpretation |
|---|---:|---:|---|
| `10x10:0.6` | 0.092337553 | 2.076845235 | matched-family crossing is later than global crossing |
| `15x15:0.5` | 4.605138006 | — | nearest matched family has no lower-overlap replacement |
| `15x15:0.6` | 0.218990587 | 1.987772005 | matched-family crossing is later than global crossing |
| `20x20:0.5` | 4.194568996 | — | nearest matched family has no lower-overlap replacement |
| `20x20:0.6` | 2.869514812 | — | no matched family within threshold |

---

## 4. Main Findings

- `10x10:0.6`: global crossing is `0.092337553`, but matched-family crossing is much later at `2.076845235`.
- `15x15:0.5`: global crossing exists at `4.605138006`, but the nearest matched Type B family has **no** lower-overlap crossing at all.
- `15x15:0.6`: global crossing is `0.218990587`, while matched-family crossing is delayed to `1.987772005`.
- `20x20:0.5`: global crossing is `4.194568996`, but the nearest matched mixed family again has **no** lower-overlap crossing.
- `20x20:0.6`: no same-type matched family survives within the distance threshold, even though a global crossing exists at `2.869514812`.

---

## 5. Interpretation

This is the strongest numerical indication so far that the early/moderate global crossings in R1-Q are often driven by **family switching**, not by smooth within-family continuation.

In particular:

1. a raw catalog minimum can overstate how early branch replacement occurs if it is allowed to jump across families;
2. same-family continuation can be much more stable than the global lower envelope suggests;
3. in some configs, the source-0 family appears not to admit any lower-overlap matched successor at the tested positive `lambda` seeds.

So the safe bridge statement is now:

> **NUMERICAL SUPPORT ONLY:** early global branch replacement is frequently a family-switch phenomenon, and the within-family threshold can be substantially larger or absent in the current catalog.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| early global crossing = within-family continuation | rejected as a default interpretation |
| family-switch explanation | supported numerically |
| family-matched threshold law | still open |
| R1-Q closed | no |

---

## 7. Next Trigger

Increase the catalog budget and sweep the family-distance threshold:

> rerun Exp73 on sentinel configs with larger `n_inits`, then rerun Exp74 for distance thresholds such as `2.0, 2.5, 3.0, 4.0` to test whether the family-switch diagnosis is robust or just a clustering hyperparameter artifact.
