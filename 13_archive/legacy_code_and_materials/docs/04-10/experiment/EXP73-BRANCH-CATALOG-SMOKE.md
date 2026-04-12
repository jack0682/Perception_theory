# Exp73 Branch Catalog Smoke

**Date:** 2026-04-11
**Session:** Cycle 56 — branch catalog and frozen lower-envelope audit
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-10/experiment/EXP72-FROZEN-BRANCH-THRESHOLD.md; docs/04-10/proof/POSITIVE-REPULSION-BRANCH-RESELECTION.md; experiments/exp73_branch_catalog.py

---

## 1. CURRENT GAP

Exp72 showed that a two-candidate frozen comparison can miss the true zero-repulsion winner because candidate discovery was too narrow. Exp73 widens the candidate set by running multiple K=2 optimizations at `lambda_rep=0` and `lambda_rep=1`, then compares the frozen energy lines

```text
E_lambda(B) = E0(B) + lambda * overlap(B)
```

across the discovered catalog.

---

## 2. Smoke Protocol

```bash
python3 experiments/exp73_branch_catalog.py \
  --config 10x10:0.6 \
  --source-lambdas 0 1 \
  --n-inits 6 \
  --max-iter 250 \
  --output-json experiments/results/exp73_branch_catalog_smoke.json \
  --output-csv experiments/results/exp73_branch_catalog_smoke.csv
```

Observed output:

```text
candidates=12 representatives=12
```

So this smoke run produced 12 frozen candidate branches and the coarse key did not merge any pair.

---

## 3. Lowest-E0 Representatives

| Rank | Key | Source lambda | E0 | Overlap | Branch type | Regime at zero |
|---:|---|---:|---:|---:|---|---|
| 1 | `Type A candidate|co0.05|ov1.4|sep5.0` | 0 | 6.180398 | 1.360079 | Type A candidate | strongly-interacting |
| 2 | `Type A candidate|co0.02|ov0.0|sep5.6` | 1 | 6.181634 | 0.000000 | Type A candidate | weakly-interacting |
| 3 | `Type A candidate|co0.05|ov0.1|sep5.6` | 0 | 6.181960 | 0.079258 | Type A candidate | weakly-interacting |
| 4 | `Type A candidate|co0.06|ov0.0|sep5.5` | 1 | 6.316247 | 0.002438 | Type A candidate | weakly-interacting |
| 5 | `Type A candidate|co0.05|ov0.7|sep2.6` | 0 | 6.411743 | 0.686511 | Type A candidate | strongly-interacting |
| 6 | `Type A candidate|co0.03|ov0.2|sep5.5` | 0 | 6.557545 | 0.168074 | Type A candidate | weakly-interacting |

Two facts matter immediately:

1. the best `lambda_rep=0` representative is **not** low-overlap — it is the strongly-interacting branch `Type A candidate|co0.05|ov1.4|sep5.0`;
2. a near-degenerate weakly-interacting branch discovered from `lambda_rep=1` has slightly larger `E0` but zero measured overlap.

---

## 4. Frozen Lower Envelope

The best-zero-energy branch and the best-zero-overlap branch satisfy

```text
DeltaE0 = 0.001236644
DeltaR  = 1.360078552
lambda_cross = DeltaE0 / DeltaR = 0.000909245
```

Therefore the frozen lower envelope changes as follows in the smoke catalog:

| Lambda range | Lower-envelope representative |
|---|---|
| `lambda = 0` | `Type A candidate|co0.05|ov1.4|sep5.0` |
| `0 < lambda < 0.000909245` | `Type A candidate|co0.05|ov1.4|sep5.0` |
| `lambda > 0.000909245` | `Type A candidate|co0.02|ov0.0|sep5.6` |

On the sampled evaluation grid, this appears as:

| Eval lambda | Winning representative | Energy |
|---:|---|---:|
| 0 | `Type A candidate|co0.05|ov1.4|sep5.0` | 6.180398 |
| 0.01 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |
| 0.05 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |
| 0.1 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |
| 0.5 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |
| 1 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |
| 5 | `Type A candidate|co0.02|ov0.0|sep5.6` | 6.181634 |

The next-best crossing in the catalog is with `Type A candidate|co0.05|ov0.1|sep5.6` at `lambda_cross = 0.001219538`, so the zero-overlap branch is already the first lower-envelope replacement.

---

## 5. Interpretation

### What this supports

- **Finite-candidate branch reselection is real in the catalog.** A branch with larger `E0` but much smaller overlap can overtake the `lambda=0` winner at a tiny positive `lambda`.
- **Candidate discovery was the real Exp72 bottleneck.** Once the catalog contains both the strongly-interacting `lambda=0` branch and a near-degenerate zero-overlap branch, a positive crossing reappears.
- **The relevant competition in this smoke run is not Type A vs Type B.** The crossing is between two distinct **Type A candidates** with very different overlap/separation signatures.

### What this does **not** support

- not a theorem-level quantitative threshold for the full SCC problem;
- not a proof that `lambda_cross \approx 9.1e-4` is stable across grids or initialization budgets;
- not a proof that the global selected branch is unique;
- not a proof that the catalog is exhaustive.

So the honest label remains:

> **NUMERICAL SUPPORT ONLY** for a candidate-conditioned tiny-positive threshold in the smoke catalog.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| branch catalog machinery works | yes |
| candidate discovery problem reduced relative to Exp72 | yes |
| positive frozen crossing exists in smoke catalog | yes, `lambda_cross \approx 9.09e-4` |
| threshold is theorem-level or universal | no |
| catalog is exhaustive | no |
| next requirement | expand catalog across configs / source lambdas / restart budget |

---

## 7. Next Trigger

Run an expanded catalog, not just a smoke run:

> Evaluate `exp73_branch_catalog.py` on `10x10:0.6`, `15x15:0.5`, `15x15:0.6`, `20x20:0.5`, `20x20:0.6` with `source_lambdas = 0, 0.05, 0.1, 1` and a larger restart budget, then measure whether the lower-envelope replacement remains tiny-positive, disappears, or becomes branch-family dependent.
