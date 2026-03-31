# Definitive Proto-Cohesion Diagnostic Table

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 7 Supplement

---

## Complete Diagnostic Vector: Bind(ℓ²) + Sep(C_t) + Inside(Q_morph)

| Field | Bind | Sep_Ct | Inside | **ProtoCoh** | Notes |
|-------|------|--------|--------|-------------|-------|
| β=1, m=9 | 0.924 | 0.871 | 0.579 | **0.579** | Inside bottleneck |
| β=5, m=9 | 0.951 | 0.892 | 0.749 | **0.749** | |
| β=10, m=9 | 0.972 | 0.898 | 0.841 | **0.841** | |
| β=20, m=9 | 0.982 | 0.901 | 0.886 | **0.886** | |
| β=50, m=9 | 0.972 | 0.908 | 0.916 | **0.908** | Sep becomes bottleneck |
| uniform 0.36 | 0.000 | 0.000 | 0.000 | **0.000** | Correctly rejected |
| uniform 1.0 | 0.942 | 0.989 | 0.000 | **0.000** | Inside kills saturated |
| checkerboard | 0.690 | 0.000 | 1.000 | **0.000** | Sep kills fragmented |
| random | 0.882 | 0.502 | 0.949 | **0.502** | Marginal |
| 3×3 block | 0.910 | 0.907 | 1.000 | **0.907** | Clean formation |

## Satisfiability Summary

| Threshold θ | Minimizers passing | Pathological passing |
|-------------|-------------------|---------------------|
| 0.5 | 15/15 | 4/10 |
| 0.7 | 11/15 | 3/10 |
| 0.8 | 6/15 | 2/10 |
| 0.9 | 3/15 | 1/10 |

## Bottleneck Transitions

- Low β: Inside (weak boundary sharpness)
- Medium β: Inside closing gap with Sep
- High β: Sep (distinction operator ceiling)
- High m: Bind (closure leaks at formation edge)

## Persistence Diagrams

All formation minimizers: 1-2 PD features, essential feature >99% of total persistence. Formations are topologically simple (single dominant connected component).
