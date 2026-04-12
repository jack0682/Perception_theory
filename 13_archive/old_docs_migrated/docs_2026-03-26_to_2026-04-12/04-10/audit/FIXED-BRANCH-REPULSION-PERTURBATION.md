# Fixed-Branch Positive-Repulsion Perturbation Test

**Date:** 2026-04-10
**Session:** Cycle 48 — fixed zero-repulsion branch/path repulsion evaluation
**Category:** audit
**Status:** complete
**Depends on:** OMEGA0-OVERLAP-EXCESS-DIAGNOSTICS.md; POSITIVE-REPULSION-MERGE-FIRST-ORDER.md; experiments/exp70_fixed_branch_repulsion_eval.py

---

## 1. CURRENT GAP

We needed to separate two effects:

1. pure first-order repulsion added to the same zero-repulsion branch/path;
2. branch re-selection when optimizing at positive `lambda_rep`.

---

## 2. Experiment Implemented

Created:

```text
experiments/exp70_fixed_branch_repulsion_eval.py
```

Protocol:

1. select source branch at `source_lambda=0`,
2. generate paths once from that fixed source and endpoint,
3. evaluate those same paths at `lambda_eval = 0, 0.1, 1, 5`,
4. report max energy excess and overlap excess relative to source.

---

## 3. Smoke Result

Command:

```bash
python3 experiments/exp70_fixed_branch_repulsion_eval.py \
  --config 10x10:0.6 \
  --source-lambda 0 \
  --lambda-evals 0 0.1 1 5 \
  --n-steps 11 \
  --n-restarts 1 \
  --max-iter 250 \
  --output-json experiments/results/exp70_fixed_branch_repulsion_eval_smoke.json \
  --output-csv experiments/results/exp70_fixed_branch_repulsion_eval_smoke.csv
```

Key observations:

| lambda_eval | Path | max_delta | max_overlap_excess |
|---:|---|---:|---:|
| 0 | direct | 0.065844 | 0 |
| 0.1 | direct | 0.063855 | 0 |
| 1 | direct | 0.045957 | 0 |
| 5 | direct | 0.000000 | 0 |
| 0 | diffuse | 0.361024 | 0 |
| 1 | diffuse | 0.353859 | 0 |
| 5 | diffuse | 0.325197 | 0 |
| 0 | sequential | 0.239364 | 0 |
| 1 | sequential | 0.130830 | 0 |
| 5 | sequential | 0.000000 | 0 |

---

## 4. Interpretation

For this fixed zero-repulsion source/path, every tested path has

```text
max_overlap_excess = 0.
```

Therefore increasing `lambda_eval` does **not** add first-order barrier through overlap excess. In fact, some path max-deltas decrease because the source already has high overlap, so positive repulsion raises the source energy as much as or more than it raises the path maximum.

This means the larger positive-repulsion barriers seen in exp69 are not simply the same zero-repulsion branch/path plus a repulsion term. They mainly reflect **branch re-selection**: optimizing the source at positive repulsion selects a low-overlap branch, and merge paths from that branch create overlap excess.

---

## 5. Theorem Consequence

The correct first-order theorem must be branch-consistent:

```text
Delta_lambda(gamma;B)
  = max_t [E_0(gamma(t))-E_0(B)
           + lambda( R(gamma(t))-R(B) ) ].
```

If

```text
max_t [R(gamma(t))-R(B)] = 0,
```

then repulsion does not create positive first-order excess for that fixed branch/path.

Positive-repulsion barriers require either:

1. unavoidable positive overlap excess for the fixed branch/path class, or
2. branch re-selection to a low-overlap source branch from which merge creates overlap excess.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| fixed zero-repulsion branch/path gains positive first-order barrier from lambda | falsified in smoke path set |
| positive-lambda exp69 barrier mainly from branch re-selection | supported |
| first-order formula using overlap excess | retained |
| raw overlap coefficient | rejected |

---

## 7. Next Trigger

Target branch re-selection theorem:

> Prove that positive repulsion selects lower-overlap source branches to first order, and that merge paths from those branches can have positive overlap excess. This separates source-selection energy from path communication energy.
