# Exp76 Fine Seeded Continuation on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 62 — fine-grained continuation of the recovered Type B branch
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP75-TYPEB-SEEDED-CONTINUATION-20x20_c0.6.md; experiments/exp76_fine_seeded_continuation.py

---

## 1. CURRENT GAP

Exp75 showed that a Type B-like family on `20x20:0.6` survives to positive `lambda` under seeded initialization. The next question was whether the later branch-label changes reflected true family breakup or only coarse diagnostic drift.

Exp76 resolves the first part of that question by running a finer warm continuation grid from the recovered zero-lambda Type B seed.

---

## 2. Protocol

```bash
python3 experiments/exp76_fine_seeded_continuation.py   --config 20x20:0.6   --source-lambda 0   --target-lambdas 0.05 0.1 0.15 0.2 0.3 0.4 0.5 0.75 1.0   --discover-inits 24   --n-restarts 4   --max-iter 300   --distance-threshold 5.0   --output-json experiments/results/exp76_fine_seeded_continuation_20x20_0.6.json   --output-csv experiments/results/exp76_fine_seeded_continuation_20x20_0.6.csv
```

Base branch:

- type: `Type B candidate`
- `E0 = 19.309893`
- `overlap = 3.094218`

---

## 3. Fine-Grid Continuation Table

| Lambda | Branch type | E0 | Overlap | Distance from base | Distance from previous |
|---:|---|---:|---:|---:|---:|
| 0.05 | Type B candidate | 18.662769 | 1.732169 | 1.995849 | 1.995849 |
| 0.10 | Type B candidate | 18.052205 | 0.765325 | 3.346672 | 1.379042 |
| 0.15 | Type B candidate | 17.727387 | 0.362154 | 3.976506 | 0.659105 |
| 0.20 | Type B candidate | 17.285409 | 0.238056 | 4.127291 | 0.278019 |
| 0.30 | Type B candidate | 17.024741 | 0.130837 | 4.319792 | 0.323524 |
| 0.40 | Type B candidate | 16.802701 | 0.061383 | 4.447834 | 0.258074 |
| 0.50 | Type B candidate | 16.729262 | 0.042130 | 4.497056 | 0.218231 |
| 0.75 | Type B candidate | 16.681058 | 0.014308 | 4.547628 | 0.096026 |
| 1.00 | Type B candidate | 16.596422 | 0.013184 | 4.551617 | 0.107112 |

---

## 4. Main Findings

1. **There is no branch-type loss on the tested grid.** The first non-Type-B lambda is `None`; the continuation remains labeled `Type B candidate` all the way through `lambda = 1.0`.
2. **The deformation is gradual.** Distances from the previous step remain small, while distance from the original base grows monotonically and then saturates near `4.55`.
3. **Overlap collapses smoothly rather than catastrophically.** The branch moves from overlap `3.094218` at `lambda=0` down to roughly `0.013184` at `lambda=1.0` without losing the Type B label.

---

## 5. Interpretation

This sharply weakens the earlier obstruction story.

For `20x20:0.6` we now have numerical evidence that:

- a seeded Type B branch is not only present for small positive `lambda`,
- it can be warm-continued across the entire tested interval up to `lambda=1.0`,
- and the previous `Type B -> Mixed/ambiguous` observation from the coarser Exp75 grid was not stable under finer continuation.

So the active gap is no longer branch-family existence or label persistence. The sharper question is now:

> when this persistent Type B branch coexists with lower-overlap competitors, is it still globally selected, metastable, or already dominated in total energy?

---

## 6. Decision

| Claim | Outcome |
|---|---|
| Type B family disappears before `lambda=1.0` on `20x20:0.6` | rejected on current grid |
| Exp75 mixed-label drift was decisive evidence of family loss | rejected |
| seeded Type B continuation persists to `lambda=1.0` | numerical support |
| R1-Q closed | no |

---

## 7. Next Trigger

Shift from continuation existence to branch selection:

> compare the total energy of the persistent seeded Type B continuation against the catalog/global competitors at the same lambdas to determine where persistence and selection diverge.
