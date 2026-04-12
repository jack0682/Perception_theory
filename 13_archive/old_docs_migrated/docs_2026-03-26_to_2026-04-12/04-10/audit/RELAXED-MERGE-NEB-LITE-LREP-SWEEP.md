# Relaxed Merge NEB-Lite Lambda-Rep Sweep

**Date:** 2026-04-10
**Session:** Cycle 41 — targeted exp69 lambda-rep sweep
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-NEB-SWEEP-SCAFFOLD.md; experiments/exp69_relaxed_merge_neb_sweep.py

---

## 1. CURRENT GAP

Assess whether relaxed merge communication-height proxy depends strongly on inter-formation repulsion `lambda_rep`.

---

## 2. Protocol

Config:

```text
10x10:0.6
```

Sweep:

```text
lambda_rep = 0, 1, 5
```

Common settings:

```text
n_images = 7
n_iter = 25
step = 0.001
spring = 0.05
n_restarts = 1
max_iter = 250
```

Outputs:

```text
experiments/results/exp69_relaxed_merge_neb_sweep_lrep_smoke.json
experiments/results/exp69_relaxed_merge_neb_sweep_lrep_smoke.csv
```

---

## 3. Results

| lambda_rep | initial max_delta | relaxed max_delta | improvement | improvement frac | simplex violation | history monotone |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 0.000000 | 0.000000 | 0.000000 | 0.0000 | 0 | true |
| 1 | 9.506985 | 9.183101 | 0.323884 | 0.0341 | 0 | true |
| 5 | 33.203337 | 29.397537 | 3.805800 | 0.1146 | 0 | true |

---

## 4. Interpretation

This is strong numerical evidence for the branch-conditioned picture:

- At `lambda_rep=0`, the relaxed merge communication proxy collapses to zero in this setup. This matches the theoretical zero-repulsion degeneracy results.
- Positive repulsion creates a nonzero path barrier proxy.
- Larger repulsion substantially increases the communication-height proxy.
- NEB-lite relaxation reduces the direct proxy more strongly when repulsion is larger.

This supports the theorem-level conclusion that relaxed merge barriers are not universal constants; they are repulsion-, branch-, and path-class-conditioned.

---

## 5. Status

| Claim | Status |
|---|---|
| `lambda_rep=0` can have zero relaxed communication proxy | numerical support consistent with theorem obstruction |
| positive repulsion increases path barrier proxy | numerical support |
| NEB-lite reduces direct path proxy | numerical support |
| exact communication height | not proved |
| Kramers rate | not proved; requires stochastic model and communication height |

---

## 6. Next Trigger

Given the amount of generated material, the next highest-value step is a final handoff / commit-prep review rather than more exploratory sweeps.

First move:

> Create `docs/04-10/audit/FINAL-RALPH-HANDOFF.md` summarizing all deliverables, fresh verification, known risks, and proposed commit scope.
