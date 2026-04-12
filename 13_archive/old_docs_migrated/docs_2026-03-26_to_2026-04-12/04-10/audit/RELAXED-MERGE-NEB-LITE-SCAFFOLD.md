# Relaxed Merge NEB-Lite Scaffold

**Date:** 2026-04-10
**Session:** Cycle 37 — projected path-relaxation scaffold
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-COMMUNICATION-HEIGHT-SCAFFOLD.md; experiments/exp68_relaxed_merge_neb.py

---

## 1. CURRENT GAP

We need a computational scaffold that can lower path communication height beyond hand-designed direct/diffuse paths.

---

## 2. Implementation

Created:

```text
experiments/exp68_relaxed_merge_neb.py
```

It starts from direct relaxed interpolation and relaxes intermediate images by projected gradient descent plus a spring/smoothing term under heuristic projection to `R_M^2`.

This is **NEB-lite**, not a rigorous MEP solver.

---

## 3. Smoke Result

Command:

```bash
python3 experiments/exp68_relaxed_merge_neb.py \
  --config 10x10:0.6 \
  --lambda-rep 1 \
  --n-images 9 \
  --n-iter 40 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 300 \
  --output experiments/results/exp68_relaxed_merge_neb_lite_smoke.json
```

Observed:

| Path | max_delta |
|---|---:|
| direct initial | 9.912147 |
| NEB-lite relaxed | 9.409110 |

The path relaxation lowered the communication-height proxy by about `0.503`.

---

## 4. Interpretation

This confirms that direct interpolation is not locally optimal even in the simple smoke setup. It also gives a working scaffold for future communication-height experiments.

However:

- projection is heuristic;
- no tangent-only NEB force decomposition yet;
- no convergence proof;
- no discretization refinement;
- no multi-branch comparison.

Therefore the result is numerical support only.

---

## 5. Next Trigger

Improve exp68 from heuristic NEB-lite to a more defensible communication-height estimator:

1. add monotonic history checks;
2. add endpoint/constraint violation diagnostics;
3. run direct vs NEB-lite vs diffuse across multiple seeds/configs;
4. decide whether a theorem or only empirical support is possible.
