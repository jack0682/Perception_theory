# Exp79 Continuation-Access Diagnostic on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 73 — first concrete analytic diagnostic for R1-Q3
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/audit/ANALYTIC-SEARCH-FAILURE-HYPOTHESES.md; experiments/exp79_continuation_access_diagnostic.py

---

## 1. Goal

Test the leading analytic hypothesis:

> the lower-energy Type B branch family is continuation-accessible but rarely or never reached by independent raw random starts at the same lambda.

---

## 2. Protocol

- config: `20x20:0.6`
- target lambda: `0.5`
- first recover the zero-lambda Type B branch
- warm-continue it to `lambda=0.5`
- then launch 16 independent raw starts directly at `lambda=0.5`
- measure family distance from each raw result to the continued branch

---

## 3. Main Result

Continued branch at `lambda=0.5`:

- branch type: `Type B candidate`
- total energy: `17.930247`
- overlap: `0.047949`

Raw-start accessibility counts by family-distance threshold:

| Threshold | Raw hits | Rate |
|---:|---:|---:|
| 2.0 | 0 / 16 | 0.0000 |
| 2.5 | 0 / 16 | 0.0000 |
| 3.0 | 0 / 16 | 0.0000 |
| 4.0 | 0 / 16 | 0.0000 |
| 5.0 | 7 / 16 | 0.4375 |

Crucially:

- there are **zero** raw hits below thresholds `2.0`, `2.5`, `3.0`, and `4.0`;
- only at the loose threshold `5.0` do some raw starts count as nearby, and those are still coarse Type A outputs with much higher energy.

---

## 4. Best Raw Result

Best raw start among the 16 tested initializations:

- branch type: `Type A candidate`
- total energy: `26.222776`
- family distance to continued Type B branch: `4.647792`

So even the best raw-discovered branch is far in family space and dramatically worse in energy than the continued Type B branch.

---

## 5. Interpretation

This is the first direct piece of evidence favoring the **continuation-accessible valleys** hypothesis over a naive “raw search should find the same family if it exists” picture.

The current read is:

1. the desired Type B valley is easy to follow once a seed inside it is available;
2. random direct starts at the same lambda do not enter that valley at practical rates in this test;
3. therefore the search gap is not just about final energy ranking, but about **valley accessibility**.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| continuation-accessible valleys should be the first instrumented analytic hypothesis | supported |
| raw starts frequently enter the same Type B family on `20x20:0.6`, `lambda=0.5` | rejected in this diagnostic |
| analytic search-failure lane has a concrete first bridge result | yes |

---

## 7. Next Trigger

Promote this into a compact diagnostic-design decision note and then decide whether the next follow-up should be:

1. a basin-volume asymmetry estimate, or
2. active-set transition logging along raw vs continued runs.
