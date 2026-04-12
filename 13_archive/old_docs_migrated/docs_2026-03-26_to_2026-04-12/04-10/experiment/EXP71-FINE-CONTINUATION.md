# Exp71 Fine Branch Continuation Near Lambda 0

**Date:** 2026-04-10
**Session:** Cycle 53 — fine continuation near lambda in [0, 0.1]
**Category:** experiment
**Status:** complete
**Depends on:** EXP71-BRANCH-CONTINUITY-DIAGNOSTICS.md; experiments/exp71_branch_continuation_threshold.py

---

## 1. CURRENT GAP

After jump diagnostics invalidated the coarse `lambda=0.1` threshold estimate, we ran a finer continuation grid near `lambda in [0,0.1]`.

---

## 2. Protocol

```bash
python3 experiments/exp71_branch_continuation_threshold.py \
  --config 10x10:0.6 \
  --lambdas 0 0.01 0.02 0.05 0.075 0.1 \
  --n-restarts 1 \
  --max-iter 300 \
  --output-json experiments/results/exp71_branch_continuation_fine_10x10_c06.json \
  --output-csv experiments/results/exp71_branch_continuation_fine_10x10_c06.csv
```

---

## 3. Main Result

The fine sweep still shows branch jumps:

| Direction | lambda | type | overlap | field_l2_step | center_step | jump |
|---|---:|---|---:|---:|---:|---|
| up | 0.00 | Type B | 9.939493 | 0 | 0 | false |
| up | 0.01 | Type B | 1.605478 | 0.447746 | 0.218389 | true |
| up | 0.02 | Type B | 1.533961 | 0.021189 | 0.005054 | false |
| up | 0.05 | Type B | 1.288951 | 0.017076 | 0.005175 | false |
| up | 0.075 | Type B | 1.037708 | 0.017393 | 0.005596 | false |
| up | 0.10 | Type B | 0.826546 | 0.017694 | 0.005508 | false |
| down | 0.00 | Type B | 2.317804 | 0.033203 | 0.008183 | false |
| down | 0.01 | Type B | 2.296491 | 0.048542 | 0.011009 | false |
| down | 0.02 | Type B | 2.293762 | 0.038784 | 0.009580 | false |
| down | 0.05 | Type B | 2.112820 | 0.033255 | 0.009148 | false |
| down | 0.075 | Type B | 2.073710 | 0.447187 | 0.189276 | true |
| down | 0.10 | Mixed | 9.229214 | 0 | 0 | false |

---

## 4. Threshold Estimates

All finite threshold estimates are compromised:

- `lambda=0.01` has an up-branch jump.
- `lambda=0.075` has a down-branch jump.
- other rows give negative or branch-inconsistent thresholds.

Therefore:

```text
No robust branch-reselection threshold estimate is available from Exp71 yet.
```

---

## 5. Interpretation

The branch landscape near zero repulsion is highly basin-sensitive. Even fine warm-start continuation can jump between branches unless branch identity is constrained more strongly.

This supports the theorem-level position that branch selection requires explicit selection/history data and cannot be reduced to a simple scalar threshold from independent or weakly controlled continuation.

---

## 6. Next Trigger

Before attempting another threshold estimate, harden branch continuation:

1. use smaller lambda steps;
2. allow `max_iter` lower per continuation step to avoid full basin switching;
3. add branch identity matching under label swaps;
4. record branch distance to initial seed, not only previous step;
5. optionally freeze branch by evaluating energy without reoptimizing.
