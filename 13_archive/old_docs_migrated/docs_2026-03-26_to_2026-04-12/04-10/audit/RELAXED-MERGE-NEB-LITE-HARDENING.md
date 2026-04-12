# Relaxed Merge NEB-Lite Hardening

**Date:** 2026-04-10
**Session:** Cycle 38 — exp68 diagnostic hardening
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-NEB-LITE-SCAFFOLD.md; experiments/exp68_relaxed_merge_neb.py

---

## 1. CURRENT GAP

The NEB-lite scaffold needed diagnostics to distinguish real communication-height improvement from constraint artifacts.

---

## 2. Added Diagnostics

`experiments/exp68_relaxed_merge_neb.py` now reports:

| Diagnostic | Meaning |
|---|---|
| `max_box_low_violation` | lower box violation over path |
| `max_box_high_violation` | upper box violation over path |
| `max_simplex_violation` | violation of `u1+u2<=1` |
| `max_total_mass_error` | error in `sum(u1+u2)=M` |
| `history.monotone_nonincreasing` | whether recorded max-delta decreased monotonically |
| `improvement` | direct initial max_delta minus relaxed max_delta |

---

## 3. Hardened Smoke Result

Command:

```bash
python3 experiments/exp68_relaxed_merge_neb.py \
  --config 10x10:0.6 \
  --lambda-rep 1 \
  --n-images 9 \
  --n-iter 60 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 300 \
  --output experiments/results/exp68_relaxed_merge_neb_lite_smoke.json
```

Observed:

| Quantity | Value |
|---|---:|
| initial max_delta | 9.115258 |
| relaxed max_delta | 8.446759 |
| improvement | 0.668499 |
| max mass error | 1.151e-12 |
| max simplex violation | 0 |
| history monotone | true |

---

## 4. Interpretation

The relaxed path improvement is not explained by obvious constraint violation: mass and simplex constraints remain satisfied to numerical precision.

Thus exp68 is now a more defensible communication-height estimator scaffold, though still not a rigorous NEB solver.

---

## 5. Remaining Limitations

- heuristic projection, not exact manifold projection;
- no tangent/perpendicular NEB decomposition;
- no adaptive image spacing;
- no convergence theorem;
- only one smoke config;
- source branch may vary due optimizer initialization.

---

## 6. Next Trigger

Run a small multi-config exp68 comparison or freeze current results and prepare a commit/handoff.

First move:

> Run exp68 on `10x10:0.5`, `10x10:0.6`, and maybe `12x12:0.6` with fixed low iteration counts to see whether NEB-lite consistently lowers direct interpolation without constraint violations.
