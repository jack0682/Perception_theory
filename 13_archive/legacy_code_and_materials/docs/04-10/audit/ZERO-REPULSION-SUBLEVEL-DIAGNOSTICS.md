# Zero-Repulsion Sampled Sublevel Diagnostics

**Date:** 2026-04-10
**Session:** Cycle 45 — zero-repulsion sampled sublevel connectivity diagnostics
**Category:** audit
**Status:** complete
**Depends on:** ZERO-REPULSION-RELAXED-MERGE-ZERO-BARRIER.md; experiments/results/exp69_relaxed_merge_neb_sweep_lrep_config_grid.json

---

## 1. CURRENT GAP

The theorem says zero relaxed barrier at `lambda_rep=0` holds when source and target are connected inside the source-energy sublevel set. We now check whether the sampled exp69 paths satisfy that sufficient condition.

---

## 2. Diagnostic Method

For each `lambda_rep=0` exp69 result, inspect both sampled paths:

- `initial` direct path,
- `relaxed` NEB-lite path.

For each path, compute:

```text
max_total = max_i E(path_i)
max_delta = max_i (E(path_i)-E(source))
all_below = all_i E(path_i) <= E(source)
```

---

## 3. Results

| File | Config | Path | Source energy | Max total | Max delta | all_below |
|---|---|---|---:|---:|---:|---|
| lrep_config_grid | 10x10:0.5 | initial | 18.976022 | 18.976022 | 0 | true |
| lrep_config_grid | 10x10:0.5 | relaxed | 18.976022 | 18.976022 | 0 | true |
| lrep_config_grid | 10x10:0.6 | initial | 15.013111 | 15.013111 | 0 | true |
| lrep_config_grid | 10x10:0.6 | relaxed | 15.013111 | 15.013111 | 0 | true |
| lrep_config_grid | 12x12:0.6 | initial | 21.144904 | 21.144904 | 0 | true |
| lrep_config_grid | 12x12:0.6 | relaxed | 21.144904 | 21.144904 | 0 | true |
| lrep_smoke | 10x10:0.6 | initial | 14.973883 | 14.973883 | 0 | true |
| lrep_smoke | 10x10:0.6 | relaxed | 14.973883 | 14.973883 | 0 | true |

---

## 4. Interpretation

For all sampled `lambda_rep=0` paths, the path remains inside the source-energy sublevel set. This is direct numerical evidence for the sufficient condition in `ZERO-REPULSION-RELAXED-MERGE-ZERO-BARRIER.md`.

Thus, for these sampled branches/path conventions:

```text
DeltaE_R^+ = 0
```

at `lambda_rep=0`.

---

## 5. Limitations

- This is sampled path evidence, not proof for all sources/targets.
- The equality may reflect the endpoint/path convention used by exp67-exp69.
- It does not imply zero barrier when `lambda_rep>0`.
- It does not imply zero barrier for path classes that force direct core preservation or forbid the sampled route.

---

## 6. Next Trigger

The zero-repulsion case is now sufficiently diagnosed. The next useful theorem target is positive-repulsion scaling:

> Determine whether the relaxed merge communication-height proxy has first-order lower bound proportional to `lambda_rep` times an overlap/transfer functional for small positive `lambda_rep`.
