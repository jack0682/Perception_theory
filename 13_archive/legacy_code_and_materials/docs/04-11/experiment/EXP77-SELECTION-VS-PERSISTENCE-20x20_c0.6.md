# Exp77 Selection vs Persistence on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 63 — compare persistent Type B continuation against discovered competitors
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP76-FINE-SEEDED-CONTINUATION-20x20_c0.6.md; experiments/exp77_selection_vs_persistence.py

---

## 1. CURRENT GAP

Exp76 showed that a seeded Type B branch on `20x20:0.6` persists through `lambda=1.0`. The next question was whether this persistent branch is merely metastable, or whether it actually beats the best discovered competitors in total energy.

---

## 2. Comparison Rule

For each lambda in the Exp76 continuation grid, compare

```text
E_total(lambda) = E0 + lambda * overlap
```

for:

1. the persistent seeded Type B continuation branch;
2. every representative in the high-budget `exp73_catalog_xrich_20x20_0.6.json` catalog.

This is still a comparison against the **best discovered catalog branch**, not a proof of the true global optimum.

---

## 3. Matched-Lambda Total Energy Table

| Lambda | Continuation total | Best discovered catalog total | Gap (cont - best) | Best discovered branch |
|---:|---:|---:|---:|---|
| 0.05 | 18.749377 | 20.221166 | -1.471789 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.10 | 18.128738 | 20.392262 | -2.263525 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.15 | 17.781710 | 20.563358 | -2.781648 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.20 | 17.333020 | 20.734454 | -3.401434 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.30 | 17.063992 | 21.076646 | -4.012653 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.40 | 16.827254 | 21.418838 | -4.591583 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.50 | 16.750327 | 21.761029 | -5.010702 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 0.75 | 16.691789 | 22.616509 | -5.924720 | `Type B candidate|co0.12|ov3.4|sep5.2` |
| 1.00 | 16.609606 | 23.471988 | -6.862382 | `Type B candidate|co0.12|ov3.4|sep5.2` |

---

## 4. Main Findings

1. **The persistent continuation branch beats the raw catalog everywhere on the tested grid.** The gap is negative at every sampled lambda from `0.05` to `1.0`.
2. **The best discovered catalog branch is fixed across the whole grid** in this comparison: `Type B candidate|co0.12|ov3.4|sep5.2`.
3. **The gap widens with lambda.** This happens because the persistent continuation rapidly lowers its overlap while keeping a favorable self-energy.

---

## 5. Interpretation

This changes the active diagnosis again.

The current data do **not** support the picture that the persistent Type B branch is a merely inferior metastable remnant. Instead, on the tested grid:

- the warm-continued Type B branch is energetically better than every branch discovered by the raw high-budget catalog search;
- therefore the real obstruction is now strongly concentrated in **search quality / branch discovery**, not in branch persistence;
- any theorem or heuristic about selected branch structure must distinguish between
  - existence of a persistent branch,
  - quality of the optimizer/search used to find it,
  - and actual global branch selection.

Safe statement:

> **NUMERICAL SUPPORT ONLY:** on `20x20:0.6`, the persistent seeded Type B branch outperforms the best discovered raw-catalog competitors on the tested lambda grid, so current non-seeded catalog search is not reliable evidence about the selected branch.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| persistent Type B branch is obviously dominated by discovered competitors | rejected |
| catalog search currently resolves selected-branch structure on `20x20:0.6` | rejected |
| search/discovery quality is now the main bottleneck | supported |
| R1-Q closed | no |

---

## 7. Next Trigger

Upgrade the search protocol itself:

> rerun direct optimization at selected lambdas with the seeded continuation branch injected as an initializer/restart candidate, then compare whether the optimizer returns the same branch and whether any better branch remains.
