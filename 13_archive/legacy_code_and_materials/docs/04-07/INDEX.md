# 04-07 Index

**Date:** 2026-04-07
**Focus:** §13 correction, F''(M/2) computation, papers retraction update

---

## Theory

| File | Description | Status |
|------|-------------|--------|
| `theory/F-DOUBLE-PRIME-COMPUTATION.md` | F''(M/2) numerical computation — mass-transfer curvature at K=2 symmetric point | complete |

## Key Results

1. **F''(M/2) is parameter-dependent** — confirmed Cat B. Competing energy terms nearly cancel, giving |F''| ~ O(0.1). Sign varies with grid size and c_ref.
2. **Canonical Spec §13 corrected** to 35A/4B/5C/5R with erratum notes
3. **Papers updated** with merge theorem retraction, honest counts
4. **d_min formula** — confirmed Cat B (regression fit, not analytical)

## Experiments

| File | Description |
|------|-------------|
| `experiments/exp62_f_double_prime.py` | Mass sweep F(m) with fixed normalization |
| `experiments/exp63_hessian_mass_transfer.py` | Direct Hessian test at K=2 minimum |
