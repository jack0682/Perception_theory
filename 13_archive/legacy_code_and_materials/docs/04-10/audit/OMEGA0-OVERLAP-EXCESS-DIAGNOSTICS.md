# Omega_0 Overlap-Excess Diagnostics

**Date:** 2026-04-10
**Session:** Cycle 47b — overlap excess diagnostics for positive-repulsion first-order analysis
**Category:** audit
**Status:** complete
**Depends on:** OMEGA0-OVERLAP-DIAGNOSTICS.md; POSITIVE-REPULSION-MERGE-FIRST-ORDER.md; experiments/results/exp69_overlap_excess_smoke.csv

---

## 1. Why This Update Was Needed

The previous overlap diagnostic measured `max_overlap` along a sampled path. But first-order communication excess should compare overlap along the path against overlap already present at the source branch:

```text
max_overlap_excess = max_t <u1(t),u2(t)> - <u1(0),u2(0)>.
```

If the maximum overlap is simply the source overlap, it does not create additional barrier relative to the source energy.

---

## 2. Diagnostic Update

Updated experiment summaries to include:

```text
initial_source_overlap
initial_max_overlap
initial_max_overlap_excess
relaxed_source_overlap
relaxed_max_overlap
relaxed_max_overlap_excess
```

---

## 3. Smoke Results

Command:

```bash
python3 experiments/exp69_relaxed_merge_neb_sweep.py \
  --configs 10x10:0.6 \
  --lambda-reps 0 1 \
  --n-images 7 \
  --n-iter 25 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 250 \
  --output-json experiments/results/exp69_overlap_excess_smoke.json \
  --output-csv experiments/results/exp69_overlap_excess_smoke.csv
```

| lambda_rep | max_delta | source_overlap | max_overlap | max_overlap_excess |
|---:|---:|---:|---:|---:|
| 0 | 0.000000 | 8.901995 | 8.901995 | 0.000000 |
| 1 | 9.050788 | 0.047627 | 4.771763 | 4.724136 |

---

## 4. Interpretation

At `lambda_rep=0`, the sampled zero-excess path does **not** increase overlap above the source. Its max overlap equals source overlap. Therefore this sampled path would not produce a first-order excess if the source branch were held fixed.

At `lambda_rep=1`, the optimizer selects a very different source branch with low source overlap, and the path creates large overlap excess. Thus the positive barrier proxy is not explained solely by adding repulsion to the same zero-repulsion branch/path. It also reflects branch re-selection under positive repulsion.

---

## 5. Theorem Consequence

The earlier first-order formula remains correct but must be branch-consistent:

```text
DeltaE_lambda(gamma) - DeltaE_lambda(source)
  contains lambda * (max_path_overlap - source_overlap).
```

A positive first-order lower bound requires unavoidable **overlap excess**, not merely nonzero overlap.

Define:

```text
Omega_0^excess(B,T;P)
  = inf_{gamma in P_0(B,T)} max_t ( <u1(t),u2(t)> - <u1(0),u2(0)> ).
```

Then a first-order lower bound needs

```text
Omega_0^excess > 0.
```

The sampled zero-repulsion path has

```text
Omega_sampled^excess = 0.
```

---

## 6. Decision

| Claim | Outcome |
|---|---|
| nonzero sampled overlap implies first-order barrier | corrected / false relative to source if no overlap excess |
| sampled zero-repulsion overlap excess | 0 |
| positive-lambda barrier source | includes branch re-selection and overlap-excess effects |
| theorem target | use `Omega_0^excess`, not raw `Omega_0` |

---

## 7. Next Trigger

Reformulate `POSITIVE-REPULSION-MERGE-FIRST-ORDER.md` around overlap-excess and branch consistency, then decide whether any positive first-order lower bound survives for a fixed branch.
