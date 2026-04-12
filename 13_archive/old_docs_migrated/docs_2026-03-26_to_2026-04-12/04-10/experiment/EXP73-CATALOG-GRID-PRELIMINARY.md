# Exp73 Catalog Grid Preliminary

**Date:** 2026-04-11
**Session:** Cycle 57 — expanded branch-catalog stability sweep
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-10/experiment/EXP73-BRANCH-CATALOG-SMOKE.md; experiments/exp73_branch_catalog.py

---

## 1. CURRENT GAP

The Exp73 smoke run suggested a tiny-positive frozen crossing, but that estimate used a small candidate set. The next question is whether the source-`lambda=0` winner is generically replaced at an equally tiny positive `lambda`, or whether the threshold is strongly configuration/catalog dependent.

---

## 2. Expanded Protocol

For each configuration in `{10x10:0.6, 15x15:0.5, 15x15:0.6, 20x20:0.5, 20x20:0.6}`, run:

```bash
python3 experiments/exp73_branch_catalog.py   --config <cfg>   --source-lambdas 0 0.05 0.1 1   --n-inits 8   --max-iter 250   --output-json experiments/results/exp73_catalog_<cfg>.json   --output-csv experiments/results/exp73_catalog_<cfg>.csv
```

Then anchor the threshold computation at the **best source-`lambda=0` representative** and compute the smallest positive frozen crossing against the rest of the catalog.

---

## 3. Source-0 Anchored Threshold Table

| Config | Representatives | Best source-0 branch | Type | E0 | Overlap | First crossing `lambda_cross` | Crossing branch | Crossing source lambda |
|---|---:|---|---|---:|---:|---:|---|---:|
| `10x10:0.6` | 31 | `Type A candidate|co0.05|ov0.7|sep2.6` | Type A candidate | 6.255586 | 0.659393 | 0.092337553 | `Type A candidate|co0.06|ov0.0|sep5.5` | 1.00 |
| `15x15:0.5` | 29 | `Type B candidate|co0.18|ov0.6|sep4.1` | Type B candidate | 12.437533 | 0.637413 | 4.605138006 | `Type A candidate|co0.07|ov0.0|sep4.2` | 0.10 |
| `15x15:0.6` | 32 | `Type B candidate|co0.14|ov3.8|sep2.9` | Type B candidate | 14.087105 | 3.795014 | 0.218990587 | `Type A candidate|co0.06|ov1.6|sep6.2` | 0.10 |
| `20x20:0.5` | 32 | `Mixed/ambiguous|co0.11|ov1.2|sep4.6` | Mixed/ambiguous | 27.234639 | 1.222781 | 4.194568996 | `Type A candidate|co0.03|ov0.1|sep8.4` | 1.00 |
| `20x20:0.6` | 32 | `Mixed/ambiguous|co0.12|ov4.3|sep4.4` | Mixed/ambiguous | 21.171365 | 4.266443 | 2.869514812 | `Type A candidate|co0.05|ov0.2|sep3.0` | 1.00 |

Threshold range observed in this expanded catalog:

```text
min lambda_cross = 0.092337553   (10x10:0.6)
max lambda_cross = 4.605138006   (15x15:0.5)
```

So the tiny-positive smoke crossing near `9e-4` is **not** stable once the catalog is expanded and the computation is anchored at the best discovered `lambda=0` branch.

---

## 4. Main Observations

1. **The source-0 optimum changes when the catalog broadens.** In `10x10:0.6`, the best discovered `lambda=0` branch is no longer the `ov≈1.36` smoke representative; it is a different Type A branch with `overlap≈0.659`, pushing the first anchored crossing out to `lambda_cross≈0.0923`.
2. **Threshold scale is highly configuration dependent.** The anchored first crossing ranges from `O(10^-1)` to `O(1)`, not uniformly near zero.
3. **Branch-family replacement is heterogeneous.** `15x15:0.5` and `15x15:0.6` start from Type B source-0 winners and switch to lower-overlap Type A candidates; `20x20` starts from mixed/ambiguous source-0 winners and also switches to Type A candidates.
4. **Finite-catalog thresholds remain candidate conditioned.** These numbers depend on which representatives were found from the chosen source-lambda set and restart budget.

---

## 5. Interpretation

### What this supports

- the Exp73 smoke claim must be weakened: the `9.09e-4` crossing is a **small-catalog artifact**, not a stable summary of R1-Q;
- frozen candidate replacement is still real, but its scale is configuration dependent and can be moderate rather than tiny;
- the best positive-`lambda` competitor is frequently a lower-overlap Type A branch, even when the source-0 winner is Type B or mixed.

### What this does **not** support

- not a universal threshold law;
- not a monotone function of grid size or volume fraction from this sample alone;
- not an exhaustive branch-family phase diagram;
- not a theorem-category upgrade.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| tiny-positive universal threshold picture | rejected |
| finite-catalog branch replacement | supported numerically |
| threshold scale stability across configs | falsified |
| R1-Q theorem closure | still open |
| next requirement | normalize branch families and compare thresholds within matched families / larger catalogs |

---

## 7. Next Trigger

Construct a family-matched catalog summary:

> cluster Exp73 representatives by branch family more robustly than the current coarse key, then recompute source-0 anchored crossings within matched families and across larger restart budgets to determine whether the threshold variability is physical or catalog-induced.
