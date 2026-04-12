# Iteration 3 R9 — Multi-Formation Discovery Pipeline

**Sys Engineer + Experiment Designer | Iteration 3, Round 9**

---

## ARCHITECTURE (Sys Engineer)

Post-optimization analysis pipeline: optimize single field → compute C_t → threshold/cluster → extract formations → evaluate per-formation diagnostics.

### Three Discovery Methods
1. **C_t Thresholding**: Threshold C_t graph, find connected components. Adaptive threshold via gap detection.
2. **Persistence on C_t Diagonal**: H₀ of C_t(x,x) superlevel filtration. Long bars = formations. Threshold-free.
3. **Spectral Clustering on C_t**: Top-k eigenvectors, k-means, eigengap heuristic.

### Limitations
- Full C_t needed: O(n²) memory, limits to n ≤ 2500
- Contraction regime (a_cl < 4) → unique closure fixed point → single-field favors single formation
- Multi-formation is POST-HOC extraction, not variational
- PRELIMINARY module; theory deferred to Iteration 4

## EXPERIMENTS (Experiment Designer)

6 synthetic multi-formation test fields (MF1-MF6): separated, touching, merged, three formations, unequal, single (control). Plus optimizer-produced multi-component fields.

5 discovery methods compared (D1-D4 + baseline spectral clustering on raw adjacency).

### Key Predictions
- P-MF1: Persistence on C_t diagonal is most reliable
- P-MF2: All methods fail on merged blobs (correct answer IS K=1)
- P-MF3: C_t spectral > raw adjacency clustering (non-local wins)
- P-MF5: Optimizer rarely produces multi-formation in contraction regime

### Budget: ~1 hour (dominated by optimizer runs)
