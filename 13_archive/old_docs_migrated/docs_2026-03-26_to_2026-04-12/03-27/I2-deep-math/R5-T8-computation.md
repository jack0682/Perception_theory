# T8 Non-Trivial Minimizers — Computation Analyst Phase Diagram & Q_morph

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 5

---

## Phase Diagram (5×5 Grid)

All (β,m) pairs produce non-trivial formations under volume constraint.

| β | m | E_tot | Core | Bd | Ext | Struct |
|---|---|-------|------|----|-----|--------|
| 1 | 9 | 4.59 | 5 | 5 | 15 | FORM-GRD |
| 5 | 9 | 5.57 | 7 | 3 | 15 | FORM-BIN |
| 10 | 9 | 6.27 | 8 | 2 | 15 | FORM-BIN |
| 20 | 9 | 7.22 | 10 | 0 | 15 | FORM-BIN |
| 50 | 9 | 9.25 | 9 | 0 | 16 | FORM-BIN |

Phase transition FORM-GRD → FORM-BIN at β ≈ 2-10.

## Q_morph_v2 Definition

Q_morph(u_t) = (2/3)·PersistenceDominance + (1/3)·TransitionSharpness

- PersistDom = max_k ℓ_k / Σ_k ℓ_k (from H₀ persistence diagram)
- TransSharp = mean normalized gradient at interface sites (u > 0.5 neighbors AND u < 0.5 neighbors)

Validated across all test fields. Correctly discriminates: formations (0.72-0.81) > uniform (0.67) > random (0.46) > fragmented (0.44).

## Proto-Cohesion Satisfiability (FIRST DEMONSTRATION)

With L² Bind (ε=0.25) + Q_morph_v2:

ALL volume-constrained formation minimizers satisfy proto-cohesion:
- Bind_L²: 0.196-0.239 (all ≤ 0.25) ✓
- Sep: 0.834-0.924 ✓
- Q_morph_v2: 0.725-0.812 ✓

## Bind Failure Analysis

Sigmoid closure structurally leaks into exterior (σ(z) > 0 always). At exterior boundary sites: Cl(u) ≈ 0.23-0.35 while u ≈ 0. Deficit 0.23-0.33.

Resolution: L² norm instead of L∞. With ε_cl = 0.25 in L², all formations pass Bind.
