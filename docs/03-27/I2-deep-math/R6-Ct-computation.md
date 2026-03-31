# C_t Formalization — Computation Analyst Full Numerical Results

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 6

---

## Setup
5×5 grid, β=10, m=9 formation minimizer from R5.

## Key Results

### C_t Discrimination: 3 Orders of Magnitude
| Zone | C_t range |
|------|-----------|
| Core-core adjacent | 0.064–0.158 |
| Core-core 2-hop | 0.046–0.122 |
| Core↔transition | 0.085–0.104 |
| Transition↔boundary | **0.000007–0.000029** |
| Any→exterior | **0.000000** |

### C_t Self-Co-Belonging (Diagonal)
```
Row 0: [0.108  0.141  0.120  0.141  0.108]  ← core
Row 1: [0.066  0.092  0.076  0.092  0.066]  ← transition
Row 2: [0.000  0.000  0.000  0.000  0.000]  ← boundary/exterior
```
Monotone in u(x) ✓

### Symmetry Issue
‖C_t - C_tᵀ‖_max = 0.058 — NOT symmetric.
Concentrated at core↔transition edges. Fix: symmetrize post-hoc.

### C_t-Weighted Sep vs Original
- E_sep(original) = 1.114
- E_sep(C_t-weighted) = 0.944
- **15% reduction** — boundary noise smoothed

### Boundary Identification
Core→transition: C_t ≈ 0.088
Transition→boundary: C_t ≈ 0.00003
**2940–12500× drop at formation boundary.** Binary-sharp despite soft field.

### Cesàro Convergence
P⁵ vs P²⁰ vs P⁵⁰: mixing fast. ‖P²⁰ - P⁵⁰‖ = 9.5×10⁻³.
Oscillation from bipartite-like structure resolved by Cesàro averaging.
