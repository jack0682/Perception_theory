# Exp74 High-Budget Robustness Sweep

**Date:** 2026-04-11
**Session:** Cycle 59 — high-budget family-switch robustness sweep
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP74-FAMILY-MATCH-PRELIMINARY.md; experiments/results/exp73_catalog_hi_*.json; experiments/results/exp74_family_match_hi_t*.json

---

## 1. CURRENT GAP

Exp74 preliminarily suggested that early global crossings are often family-switch events. This cycle asks whether that diagnosis survives:

1. a larger branch-catalog budget (`n_inits=16`), and
2. multiple family-distance thresholds (`2.0, 2.5, 3.0, 4.0`).

---

## 2. High-Budget Protocol

Sentinel configs:

- `10x10:0.6`
- `15x15:0.6`
- `20x20:0.6`

High-budget catalog:

```bash
python3 experiments/exp73_branch_catalog.py   --config <cfg>   --source-lambdas 0 0.05 0.1 1   --n-inits 16   --max-iter 300   --output-json experiments/results/exp73_catalog_hi_<cfg>.json   --output-csv experiments/results/exp73_catalog_hi_<cfg>.csv
```

Then threshold sweep:

```bash
python3 experiments/exp74_branch_family_match.py   --input-glob 'experiments/results/exp73_catalog_hi_*.json'   --distance-threshold <2.0|2.5|3.0|4.0>
```

---

## 3. Robustness Table

| Config | Global crossing | Matched crossing @2.0 | Matched crossing @2.5 | Matched crossing @3.0 | Matched crossing @4.0 |
|---|---:|---:|---:|---:|---:|
| `10x10:0.6` | 0.606017417 | 0.606017417 | 0.606017417 | 0.606017417 | 0.606017417 |
| `15x15:0.6` | 0.336199568 | — | — | — | — |
| `20x20:0.6` | 3.038207426 | — | — | — | — |

---

## 4. Main Findings

- `10x10:0.6`: the diagnosis **changes** at higher budget. The global crossing is now `0.606017417`, and it is also the matched-family crossing across all tested thresholds. So here the earlier family-switch interpretation was a small-catalog artifact.
- `15x15:0.6`: the global crossing is `0.336199568`, but the nearest matched-family candidate still has **no** lower-overlap crossing at any tested threshold. This remains a family-switch-dominated case.
- `20x20:0.6`: the global crossing is `3.038207426`, and there is still **no matched family** even up to threshold `4.0`. This is the strongest current family-switch case.
- Threshold-sweep sensitivity is low **once the high-budget catalog is fixed**: the qualitative outcome is unchanged from `2.0` to `4.0` for all three sentinel configs.

---

## 5. Interpretation

The robustness sweep refines the previous conclusion:

1. **family-switch is not universal** — `10x10:0.6` flips to a same-family interpretation once the catalog budget is raised;
2. **family-switch remains robust in harder configs** — `15x15:0.6` and especially `20x20:0.6` still resist a within-family explanation;
3. the decisive sensitivity seems to come more from **catalog budget** than from the moderate threshold range `2.0` to `4.0`.

So the safe updated bridge statement is:

> **NUMERICAL SUPPORT ONLY:** whether an early global crossing is a family-switch effect is catalog-budget dependent; after budget expansion, some configs admit same-family replacement, while others still do not.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| family-switch explanation is universal | rejected |
| family-switch remains robust for all sentinel configs | rejected |
| catalog-budget sensitivity matters | supported |
| threshold-sweep sensitivity (2.0-4.0) dominates the diagnosis | not supported |
| R1-Q closed | no |

---

## 7. Next Trigger

Focus on the hardest survivor:

> increase catalog budget further for `20x20:0.6`, and add richer family descriptors (for example support topology or branch provenance) to test whether the absence of a matched family is physical or still a representation artifact.
