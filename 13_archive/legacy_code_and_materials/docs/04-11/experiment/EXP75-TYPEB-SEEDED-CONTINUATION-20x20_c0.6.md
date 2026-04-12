# Exp75 Type-B Seeded Continuation on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 61 — targeted seeded continuation for the hardest sentinel
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP74-HIGH-BUDGET-ROBUSTNESS.md; experiments/exp75_typeb_seeded_continuation.py

---

## 1. CURRENT GAP

The hardest remaining numerical obstruction was `20x20:0.6`: even with a larger catalog and richer family descriptor, the raw Exp73/Exp74 pipeline still found no matched family. The key question became:

> is the missing matched family physical, or is it just a discovery failure of the catalog search?

Exp75 attacks this directly by taking the best discovered source-`lambda=0` Type B branch and using it as the initialization for positive `lambda` runs.

---

## 2. Protocol

```bash
python3 experiments/exp75_typeb_seeded_continuation.py   --config 20x20:0.6   --source-lambda 0   --target-lambdas 0.05 0.1 0.2 0.5 1.0   --n-inits 24   --n-restarts 4   --max-iter 300   --distance-threshold 5.0   --output-json experiments/results/exp75_typeb_seeded_continuation_20x20_0.6.json   --output-csv experiments/results/exp75_typeb_seeded_continuation_20x20_0.6.csv
```

Base branch discovered at `lambda=0`:

- branch type: `Type B candidate`
- `E0 = 20.050070`
- `overlap = 3.421918`

---

## 3. Seeded Continuation Results

| Target lambda | Branch type | E0 | Overlap | Family distance from base | Within threshold 5.0 |
|---:|---|---:|---:|---:|---|
| 0.05 | Type B candidate | 18.992503 | 1.928690 | 2.334438 | True |
| 0.10 | Type B candidate | 19.012002 | 1.208757 | 3.190994 | True |
| 0.20 | Type B candidate | 19.048174 | 0.512760 | 4.281578 | True |
| 0.50 | Mixed/ambiguous | 19.108585 | 0.070598 | 4.922685 | True |
| 1.00 | Mixed/ambiguous | 19.132465 | 0.014810 | 4.998794 | True |

---

## 4. Main Findings

1. **A positive-lambda Type B continuation does exist.** At `lambda = 0.05, 0.1, 0.2`, the optimizer remains in `Type B candidate` when initialized from the best zero-lambda Type B branch.
2. **The family distance stays controlled.** Even at `lambda = 0.5` and `1.0`, the solutions remain within the threshold-5.0 neighborhood, though the coarse branch-type label degrades to `Mixed/ambiguous`.
3. **Therefore the missing matched family in Exp73/Exp74 was not decisive evidence of physical absence.** It was at least partly a search/discovery failure of the raw catalog pipeline.

---

## 5. Interpretation

This is the strongest evidence so far that the hardest-sentinel obstruction is **not** simply “Type B cannot persist for positive lambda”. Instead:

- a Type B-like family can be continued at least up to moderate positive `lambda` under targeted initialization;
- the catalog pipeline can miss that family even when it exists;
- the real gap has shifted from crude existence/nonexistence to **how long the branch persists, how it deforms, and when/where it loses its Type B label**.

Safe updated bridge statement:

> **NUMERICAL SUPPORT ONLY:** on `20x20:0.6`, positive-lambda Type B-like continuation exists under seeded initialization, so catalog-level absence of a matched family should not be treated as physical impossibility.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| no positive-lambda matched family exists on `20x20:0.6` | rejected |
| hardest-sentinel family-switch diagnosis | weakened substantially |
| catalog-discovery failure | supported |
| R1-Q closed | no |

---

## 7. Next Trigger

Move from discovery to continuation:

> perform targeted branch continuation from the recovered `20x20:0.6` Type B seed across a finer lambda grid, record where the branch-type label changes, and distinguish true loss of branch family from mere coarse-label drift.
