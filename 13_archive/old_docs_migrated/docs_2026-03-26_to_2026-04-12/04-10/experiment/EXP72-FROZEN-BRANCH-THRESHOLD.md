# Exp72 Frozen-Branch Threshold Smoke

**Date:** 2026-04-10
**Session:** Cycle 54 — frozen-candidate branch threshold evaluation
**Category:** experiment
**Status:** complete
**Depends on:** POSITIVE-REPULSION-BRANCH-RESELECTION.md; EXP71-HARDENED-CONTINUATION.md; experiments/exp72_frozen_branch_threshold.py

---

## 1. CURRENT GAP

Branch continuation could not robustly preserve identity. Exp72 freezes candidate branches and evaluates their exact finite-candidate energy lines

```text
E_lambda(B) = E0(B) + lambda * overlap(B)
```

without reoptimization.

---

## 2. Smoke Protocol

```bash
python3 experiments/exp72_frozen_branch_threshold.py \
  --config 10x10:0.6 \
  --branch-lambdas 0 1 \
  --eval-lambdas 0 0.01 0.05 0.1 0.5 1 5 \
  --n-restarts 2 \
  --max-iter 400 \
  --output-json experiments/results/exp72_frozen_branch_threshold_smoke.json \
  --output-csv experiments/results/exp72_frozen_branch_threshold_smoke.csv
```

---

## 3. Candidate Branches

| Branch | Source lambda | E0 | Overlap | Type | Center offset | Separation |
|---|---:|---:|---:|---|---:|---:|
| branch_from_lambda_0 | 0 | 5.812146 | 3.172980 | Type B | 0.180971 | 4.754062 |
| branch_from_lambda_1 | 1 | 4.854491 | 0.000000 | Type A | 0.034761 | 6.416018 |

---

## 4. Threshold

The crossing estimate is

```text
lambda_cross = -0.301815
```

because the positive-repulsion / Type A candidate already has lower inferred `E0` at `lambda=0` **and** lower overlap.

Therefore, in this smoke run, the Type A candidate dominates the Type B candidate for all `lambda >= 0`.

---

## 5. Interpretation

This is a clean finite-candidate application of the branch-reselection theorem, but it does not show a positive threshold. It shows that the selected `lambda=0` optimization did not find the best zero-repulsion branch among the frozen candidate set.

Thus the practical issue is not only threshold estimation; it is candidate discovery.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| frozen-candidate energy evaluation works | yes |
| Type A candidate lower E0 and lower overlap in smoke | yes |
| positive threshold found | no; crossing is negative |
| zero-lambda optimizer finds best zero-lambda branch | falsified in smoke candidate set |
| next requirement | candidate discovery / multi-start branch catalog |

---

## 7. Next Trigger

Build a branch catalog:

> Run multiple K=2 optimizations at `lambda=0` and `lambda=1`, cluster branches by overlap/center/separation/E0, then apply frozen-candidate energy-line comparison to all candidate pairs.
