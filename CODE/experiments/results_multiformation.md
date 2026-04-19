# Experiment 6: Multi-Formation (K=2) Results

**Date:** 2026-03-30
**Grid:** 20x20 (n=400), 4-connectivity
**Volume:** 0.25 per formation (m=100 each, total 0.50)
**Restarts:** 3, max_iter=2000, lambda_bar=100

## Summary

The K-field architecture from I9 successfully produces **two spatially separated formations** on a 2D grid. Repulsion strength controls the degree of separation.

## Results by Regime

### Weak repulsion (lambda_rep = 1)

| Metric | Formation 1 | Formation 2 |
|--------|------------|------------|
| Bind | 0.884 | 0.885 |
| Sep | 0.800 | 0.792 |
| Inside | 0.745 | 0.756 |
| Persist | 1.000 | 1.000 |
| E_self | 12.39 | 12.61 |
| Max u | 0.79 | 0.80 |

- Overlap: 0.075 (small but nonzero)
- CoM distance: 12.4 grid units
- Both formations achieve strong diagnostics (Bind > 0.88, Sep > 0.79, Inside > 0.74)
- Mild repulsion allows nearly independent optimization

### Moderate repulsion (lambda_rep = 10)

| Metric | Formation 1 | Formation 2 |
|--------|------------|------------|
| Bind | 0.880 | 0.884 |
| Sep | 0.487 | 0.416 |
| Inside | 0.152 | 0.097 |
| Persist | 1.000 | 1.000 |
| E_self | 26.53 | 29.09 |
| Max u | 0.58 | 0.55 |

- Overlap: 0.000 (complete separation)
- CoM distance: 8.9 grid units
- Stronger repulsion forces flatter profiles (max u drops to ~0.55), reducing Sep and Inside scores
- Formations are spatially disjoint

### Strong repulsion (lambda_rep = 100)

| Metric | Formation 1 | Formation 2 |
|--------|------------|------------|
| Bind | 0.840 | 0.841 |
| Sep | 0.218 | 0.207 |
| Inside | 0.013 | 0.013 |
| Persist | 1.000 | 1.000 |
| E_self | 42.47 | 42.74 |
| Max u | 0.51 | 0.51 |

- Overlap: 0.000 (complete separation)
- CoM distance: 5.0 grid units
- Very strong repulsion flattens formations to near-uniform ~0.25 within their support, destroying phase separation (Inside ~ 0)
- Formations remain spatially separated but lose internal structure

## Key Findings

1. **K-field architecture works.** Two distinct formations emerge with different spatial supports, confirming the I9 architecture is implementable.

2. **Repulsion-quality tradeoff.** There is a clear tradeoff between inter-formation separation and per-formation quality:
   - Weak: high-quality formations with mild overlap
   - Moderate: zero overlap but reduced distinction/morphology
   - Strong: zero overlap, near-uniform fields (no phase structure)

3. **Optimal regime.** lambda_rep ~ 1-5 appears to be the sweet spot: sufficient to break symmetry and induce spatial separation while allowing each formation to develop rich internal structure.

4. **Spatial symmetry breaking.** The Fiedler-based initialization successfully breaks the K! label symmetry, producing spatially distinct formations across restarts.

5. **Simplex constraint respected.** At no point does sum_k u^k(x) significantly exceed 1 (barrier term is effective).

## Spatial Layout (strong regime)

```
+ x 2 2 2 x + + x + x x + x x + x 2 2 x
x + x + x x x x x x 2 2 2 2 2 2 2 2 x +
2 2 x + 1 + x x + + 2 2 2 2 2 2 2 2 + x
...
1 1 1 1 1 x x + 1 1 1 x + x 1 1 x 1 1 1
x + x 1 1 1 1 1 x 1 1 + x x 1 + x 1 1 1
x + x 1 1 1 1 1 1 1 x 1 1 1 1 x x 1 1 1
```
Formation 1 occupies bottom-left, Formation 2 occupies top-right.

## Implementation Notes

- Reuses `EnergyComputer` for per-formation intra-gradients (no code duplication)
- Reuses `project_volume` from optimizer.py
- Simplex constraint enforced via soft barrier (lambda_bar * max(0, S-1)^2), not hard projection
- Fiedler-based spatial initialization critical for symmetry breaking
- Runtime: ~1.8s per regime (3 restarts x 2000 iters on 400-node graph)
