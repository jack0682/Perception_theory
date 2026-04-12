# Omega_0 Overlap Diagnostics for Zero-Repulsion Paths

**Date:** 2026-04-10
**Session:** Cycle 47 — overlap maxima diagnostics for first-order repulsion coefficient
**Category:** audit
**Status:** complete
**Depends on:** POSITIVE-REPULSION-MERGE-FIRST-ORDER.md; experiments/exp69_relaxed_merge_neb_sweep.py

---

## 1. CURRENT GAP

Positive-repulsion first-order theory depends on whether zero-excess paths have unavoidable overlap:

```text
Omega_0 = inf_{gamma in P_0} max_t <u1(t),u2(t)>.
```

If sampled zero-excess paths have nonzero overlap, they would acquire first-order repulsion cost under `lambda_rep > 0`.

---

## 2. Diagnostic Update

Updated experiment summaries to include:

```text
initial_max_overlap
relaxed_max_overlap
```

in `exp67` / `exp69` path summaries.

---

## 3. Smoke Result

Command:

```bash
python3 experiments/exp69_relaxed_merge_neb_sweep.py \
  --configs 10x10:0.6 \
  --lambda-reps 0 \
  --n-images 7 \
  --n-iter 25 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 250 \
  --output-json experiments/results/exp69_overlap_diag_lrep0_smoke.json \
  --output-csv experiments/results/exp69_overlap_diag_lrep0_smoke.csv
```

Observed:

| Config | lambda_rep | max_delta | initial_max_overlap | relaxed_max_overlap |
|---|---:|---:|---:|---:|
| 10x10:0.6 | 0 | 0 | 8.983722 | 8.983722 |

---

## 4. Interpretation

The sampled zero-repulsion path has zero energy excess but nonzero overlap. Therefore the same sampled path would acquire a positive first-order repulsion contribution:

```text
lambda_rep * 8.983722
```

This explains why positive `lambda_rep` produces a barrier proxy in exp69.

However, this does **not** prove `Omega_0>0`, because another zero-excess path might avoid overlap. It only proves:

```text
sampled_path_overlap > 0.
```

---

## 5. Decision

| Claim | Outcome |
|---|---|
| sampled zero-excess path has nonzero overlap | verified numerically |
| sampled path has positive first-order repulsion cost | follows from decomposition |
| unavoidable overlap `Omega_0>0` | not proved |
| need search for overlap-avoiding zero-excess path | remains open |

---

## 6. Next Trigger

Search for overlap-avoiding zero-excess paths at `lambda_rep=0`.

First move:

> Modify/design a path that transfers mass only after separating supports, and check whether max overlap can be reduced while keeping zero excess.
