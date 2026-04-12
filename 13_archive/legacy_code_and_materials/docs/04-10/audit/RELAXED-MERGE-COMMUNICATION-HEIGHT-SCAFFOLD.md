# Relaxed Merge Communication-Height Computation Scaffold

**Date:** 2026-04-10
**Session:** Cycle 36 — relaxed merge communication-height scaffold
**Category:** audit
**Status:** complete
**Depends on:** KRAMERS-COMMUNICATION-HEIGHT-SCHEMA.md; experiments/exp67_relaxed_merge_paths.py

---

## 1. CURRENT GAP

We need an empirical/procedural scaffold for estimating branch-conditioned communication height

```text
H(A,B) = inf_gamma max_t E_R(gamma(t))
```

for relaxed merge paths.

---

## 2. Scaffold Implemented

Created:

```text
experiments/exp67_relaxed_merge_paths.py
```

It compares two explicit path classes for one selected branch:

1. `direct_relaxed_interpolation`, from `(u1,u2)` to `(u_merge,0)`;
2. `diffuse_shortcut`, which softens/spreads `u2`, transfers diffuse mass, then reconcentrates.

This is not a minimizer/NEB solver. It is a path-class comparison scaffold.

---

## 3. Smoke Result

Command:

```bash
python3 experiments/exp67_relaxed_merge_paths.py \
  --config 10x10:0.6 \
  --lambda-rep 1.0 \
  --n-restarts 1 \
  --max-iter 300 \
  --n-steps 11 \
  --output experiments/results/exp67_relaxed_merge_paths_smoke.json
```

Observed:

| Path | max_delta |
|---|---:|
| direct_relaxed_interpolation | 8.568470 |
| diffuse_shortcut | 75.978909 |

In this smoke configuration, the naive diffuse shortcut is much worse than direct interpolation. This does **not** prove direct interpolation is the MEP; it only falsifies this particular simple shortcut as a low-energy route.

---

## 4. Interpretation

The scaffold now permits systematic comparison of path classes. The initial result shows that “diffuse shortcut” is not automatically low energy; spreading may pay a high morphology/double-well cost.

However, this is still numerical support only. A true communication-height estimate requires:

1. optimized path search such as NEB/string on `R_M^2`,
2. multiple source branches and targets,
3. path discretization convergence checks,
4. comparison across beta/lambda regimes.

---

## 5. Next Trigger

Upgrade exp67 from two hand-designed paths to a simple path optimizer / NEB-lite method on the relaxed manifold.

First move:

> Add a projected path-relaxation routine for intermediate images that lowers the max energy while keeping endpoints fixed and preserving `R_M^2` constraints.
