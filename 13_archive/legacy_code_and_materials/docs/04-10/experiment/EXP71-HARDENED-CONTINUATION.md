# Exp71 Hardened Branch Continuation

**Date:** 2026-04-10
**Session:** Cycle 52b — label-swap-aware branch-distance diagnostics
**Category:** experiment
**Status:** complete
**Depends on:** EXP71-FINE-CONTINUATION.md; experiments/exp71_branch_continuation_threshold.py

---

## 1. CURRENT GAP

Fine continuation still showed jumps. Exp71 was hardened with:

- label-swap-aware distance between successive branch states,
- distance to initial/root branch,
- center-of-mass step distance,
- conservative jump flag.

---

## 2. Added Diagnostics

| Field | Meaning |
|---|---|
| `field_l2_step` | label-matched L2 field displacement from previous continuation step |
| `field_linf_step` | label-matched max field displacement |
| `center_step` | max center-of-mass displacement normalized by grid width |
| `label_swapped` | whether label swap gave smaller step distance |
| `field_l2_from_root` | distance from initial branch seed |
| `center_from_root` | center displacement from initial branch seed |
| `jump_flag` | heuristic jump detector |

---

## 3. Hardened Smoke Result

Command:

```bash
python3 experiments/exp71_branch_continuation_threshold.py \
  --config 10x10:0.6 \
  --lambdas 0 0.01 0.02 0.05 0.075 0.1 \
  --n-restarts 1 \
  --max-iter 200 \
  --output-json experiments/results/exp71_branch_continuation_hardened_10x10_c06.json \
  --output-csv experiments/results/exp71_branch_continuation_hardened_10x10_c06.csv
```

Key jump rows:

| Direction | lambda | type | overlap | field_l2_step | center_step | root L2 | root center | jump |
|---|---:|---|---:|---:|---:|---:|---:|---|
| up | 0.01 | Type A | 2.650033 | 0.381972 | 0.248327 | 0.381972 | 0.248327 | true |
| down | 0.075 | Mixed | 0.795660 | 0.438311 | 0.286470 | 0.438311 | 0.286470 | true |

---

## 4. Threshold Consequence

The branch-reselection threshold remains non-identifiable from current continuation:

- The apparent threshold rows are contaminated by branch jumps.
- Label-swap matching does not remove the jumps.
- Distance-to-root confirms large branch departures.
- Warm-start continuation with full optimization still falls into different basins.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| label-swap artifact caused jumps | not supported |
| branch jumps persist after hardening | yes |
| robust threshold estimate from current Exp71 | unavailable |
| next experimental option | lower `max_iter` / predictor-corrector continuation / frozen-branch energy evaluation |
| theorem interpretation | branch reselection threshold is not observable without a stronger branch identity protocol |

---

## 6. Next Trigger

Choose between:

1. **Frozen-branch energy evaluation**: evaluate fixed branch candidates across lambda without reoptimization, giving clean finite-candidate thresholds.
2. **Predictor-corrector continuation**: use small lambda steps and constrained local optimization with trust-region radius to preserve branch identity.

Recommended next: frozen-branch evaluation, because it directly matches the finite-candidate theorem.
