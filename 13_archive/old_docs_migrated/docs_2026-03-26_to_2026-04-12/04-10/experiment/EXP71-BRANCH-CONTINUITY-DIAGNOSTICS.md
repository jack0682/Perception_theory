# Exp71 Branch-Continuity Diagnostics

**Date:** 2026-04-10
**Session:** Cycle 52 — branch-distance and jump diagnostics for continuation thresholds
**Category:** experiment
**Status:** complete
**Depends on:** EXP71-BRANCH-CONTINUATION-SMOKE.md; experiments/exp71_branch_continuation_threshold.py

---

## 1. CURRENT GAP

Threshold estimates from branch continuation are meaningful only on continuous branch segments. Exp71 now records field and center displacement between continuation steps.

---

## 2. Added Diagnostics

Each continuation row now includes:

```text
field_l2_step
field_linf_step
center_step
jump_flag
```

A heuristic jump is flagged when:

```text
field_l2_step > 0.25
or field_linf_step > 0.5
or center_step > 0.10
```

---

## 3. Smoke Result

Command:

```bash
python3 experiments/exp71_branch_continuation_threshold.py \
  --config 10x10:0.6 \
  --lambdas 0 0.1 0.5 1.0 \
  --n-restarts 1 \
  --max-iter 300 \
  --output-json experiments/results/exp71_branch_continuation_threshold_smoke.json \
  --output-csv experiments/results/exp71_branch_continuation_threshold_smoke.csv
```

Key branch rows:

| Direction | lambda | type | overlap | field_l2_step | center_step | jump |
|---|---:|---|---:|---:|---:|---|
| up | 0.0 | Type A | 7.336876 | 0 | 0 | false |
| up | 0.1 | Type A | 0.001661 | 0.393710 | 0.219546 | true |
| up | 0.5 | Type A | 0 | 0.052831 | 0.012585 | false |
| up | 1.0 | Type A | 0 | 0.027958 | 0.007513 | false |
| down | 0.0 | Type A | 0 | 0.043139 | 0.015922 | false |
| down | 0.1 | Type A | 0 | 0.068480 | 0.027446 | false |
| down | 0.5 | Type A | 0 | 0.135258 | 0.055351 | false |
| down | 1.0 | Type A | 0.000065 | 0 | 0 | false |

---

## 4. Threshold Estimate Consequence

The only row that previously looked like a plausible finite threshold (`lambda=0.1`) is now marked discontinuous on the up branch.

Therefore it should **not** be used as a reliable branch-continuation threshold estimate.

Current result:

```text
No robust branch-reselection threshold estimate yet.
```

The method now correctly refuses to report unstable estimates as theorem evidence.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| jump diagnostics added | yes |
| lambda=0.1 finite threshold row reliable | rejected; jump detected |
| continuation threshold estimate available | not yet |
| next requirement | finer lambda grid / smaller warm-start step / stronger branch matching |

---

## 6. Next Trigger

Run finer continuation near `lambda in [0,0.1]` with smaller steps and report only continuous segments.
