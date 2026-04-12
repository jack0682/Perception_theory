# Q_morph Formalization — Computation Analyst Results

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 7

---

## Q_morph_v4 (Final Candidate)

$$Q_{\mathrm{morph}}(u) = \text{TransitionSharpness}(u) \times \text{FormationQuality}(u)$$

- TransSharp = max_{edge (x,y)} |u(x) - u(y)| ∈ [0,1]
- FormationQuality = TopPersistence / max(u) ∈ [0,1]

## Axiom Verification

| Axiom | Status |
|-------|--------|
| QM1 (Range [0,1]) | ✓ |
| QM2 (Zero for uniform) | ✓ (TransSharp = 0) |
| QM3 (Monotone under sharpening p≥1) | ✓ |
| QM4 (Binary block maximizes) | ✓ (Q = 1.0) |

## Proto-Cohesion on Energy Minimizers (5×5 grid, m=9)

| β | Bind | Sep | Inside(Q_morph) | ProtoCoh(min) |
|---|------|-----|-----------------|---------------|
| 1 | 0.924 | 0.840 | 0.579 | **0.579** |
| 5 | 0.951 | 0.866 | 0.749 | **0.749** |
| 10 | 0.972 | 0.880 | 0.841 | **0.841** |
| 20 | 0.983 | 0.888 | 0.886 | **0.886** |
| 50 | 0.972 | 0.900 | 0.916 | **0.900** |

ProtoCoh increases monotonically with β. Inside is bottleneck at low β, Sep at high β.

## Known Limitation

FormationQuality = TopPersistence/max(u) = 1.0 for ALL non-trivial fields on 5×5 grid (one component always dominates on small connected graphs). Q_morph_v4 reduces to TransSharp on small graphs. Degeneracy resolves on larger graphs.

## Recommendation

Q_morph_v4 as PROVISIONAL realization. C_t-based alternative (spectral gap of co-belonging graph) as next candidate.
