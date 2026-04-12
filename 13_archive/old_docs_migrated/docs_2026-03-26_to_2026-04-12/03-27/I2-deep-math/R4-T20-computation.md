# T20 Axiom Consistency — Computation Analyst Numerical Verification

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 4

---

## Setup

X_t = 10-site path graph. N_t(i,i+1) = 1. Parameters: a_cl=4, η=0.5, τ=0.3.
Bump field: u = [0, 0.2, 0.6, 0.9, 1.0, 0.9, 0.6, 0.2, 0, 0].

## Key Numerical Results

### Closure Computation

| x | u(x) | P_t u(x) | blend | Cl(u)(x) | Cl-u | A1? |
|---|------|----------|-------|----------|------|-----|
| 0 | 0.0 | 0.200 | 0.100 | 0.310 | +0.310 | n/a |
| 1 | 0.2 | 0.300 | 0.250 | 0.450 | +0.250 | ✓ |
| 2 | 0.6 | 0.550 | 0.575 | 0.750 | +0.150 | ✓ |
| 3 | 0.9 | 0.800 | 0.850 | 0.900 | +0.000 | ✓ (barely) |
| 4 | 1.0 | 0.900 | 0.950 | 0.931 | −0.069 | **✗ FAIL** |
| 5 | 0.9 | 0.800 | 0.850 | 0.900 | +0.000 | ✓ (barely) |
| 6 | 0.6 | 0.550 | 0.575 | 0.750 | +0.150 | ✓ |
| 7 | 0.2 | 0.300 | 0.250 | 0.450 | +0.250 | ✓ |
| 8 | 0.0 | 0.100 | 0.050 | 0.269 | +0.269 | n/a |
| 9 | 0.0 | 0.000 | 0.000 | 0.231 | +0.231 | n/a |

**A1 fails at site 4** (peak): σ < 1 always, so u(x)=1 is structurally impossible to satisfy.

### Iterated Closure Convergence

Converges in 21 iterations to uniform u* ≡ 0.924. All spatial structure destroyed.

### C_t Diffusion

- C_t(4,5) = 0.208 (within formation) ✓
- C_t(2,7) = 0.000 (across gap) ✓
- C_t(x,x) monotone increasing in u(x) ✓
- All C1-C4 verified ✓

### Energy at Special States

| State | E_cl | E_sep | E_bd | Total |
|-------|------|-------|------|-------|
| u ≡ 0 | 0.14 | 0.00 | 0.00 | **0.14** |
| u ≡ 1 | 0.14 | 0.17 | 0.00 | **0.31** |
| bump | 0.40 | 0.78 | 0.30 | **1.48** |

Trivial states dominate. Volume constraint mandatory.

### Broader A1 Survey

100 parameter combinations × 5 test fields. Only 42-51% satisfy A1 depending on field. A1 failure is structural, not parametric.

### Stability Verification

Non-idempotent Hessian: 25/25 strictly positive eigenvalues (min = 0.287).
Idempotent comparison: 21/25 positive, 4 zero eigenvalues.
**Non-idempotent advantage confirmed quantitatively.**

### Turing Instability

Full energy Hessian at uniform states: 24-25 negative eigenvalues out of 25. All uniform states wildly unstable.
