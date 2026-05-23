> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# VP-9 — Non-trivial V Basin Test Summary

**Date:** 2026-05-08  
**Experiment:** vp9_nontrivial_v_basin_test.py  
**Attacks:** OP-OMS-002+ (non-trivial admissible V; Prop NV7)  
**Elapsed:** 97.4s

## Method

Build $V_{2,\tau}(\lambda) = -\tau \log(\exp(-D_1/\tau) + \exp(-D_2/\tau))$ with $D_i = \lVert P^{\mathrm{sm}}(\lambda) - y_i \rVert_2^2$ for two targets $y_1, y_2$ (cl-dominant and sep-dominant readouts).
Evaluate on triangular Δ² grid; discrete gradient descent on the 6-neighbor adjacency; cluster grid points by attractor; report basin sizes and P^sm distinctness.

## Per-scene results

### P12_path

- K = 12 → 91 grid points (ok: 91)
- ||y_1 - y_2|| = 0.2424

**tau=0.01:** 3 attractors, basin sizes [48, 24, 19], distinct readout pairs = 2

| attractor | λ | branch | basin frac | closer_to | V |
|---|---|---|---|---|---|
| 20 | (0.08,0.58,0.33) | (3, 4) | 52.75% | y2 | -0.0000 |
| 33 | (0.17,0.67,0.17) | (3, 4) | 26.37% | y2 | -0.0000 |
| 77 | (0.67,0.08,0.25) | (2, 3) | 20.88% | y1 | 0.0010 |

**tau=0.1:** 2 attractors, basin sizes [45, 46], distinct readout pairs = 0

| attractor | λ | branch | basin frac | closer_to | V |
|---|---|---|---|---|---|
| 64 | (0.50,0.08,0.42) | (2, 4) | 49.45% | y1 | -0.0544 |
| 72 | (0.58,0.17,0.25) | (2, 4) | 50.55% | y1 | -0.0543 |

### S3_grid6x6

- K = 8 → 45 grid points (ok: 45)
- ||y_1 - y_2|| = 0.3238

**tau=0.01:** 4 attractors, basin sizes [21, 12, 2, 10], distinct readout pairs = 4

| attractor | λ | branch | basin frac | closer_to | V |
|---|---|---|---|---|---|
| 15 | (0.12,0.75,0.12) | (7, 12) | 46.67% | y2 | 0.0000 |
| 29 | (0.38,0.62,0.00) | (7, 12) | 26.67% | y2 | 0.0000 |
| 30 | (0.50,0.00,0.50) | (1, 8) | 4.44% | y1 | 0.0079 |
| 36 | (0.62,0.12,0.25) | (3, 9) | 22.22% | y1 | 0.0003 |

**tau=0.1:** 2 attractors, basin sizes [27, 18], distinct readout pairs = 0

| attractor | λ | branch | basin frac | closer_to | V |
|---|---|---|---|---|---|
| 25 | (0.38,0.12,0.50) | (5, 11) | 60.00% | y1 | -0.0421 |
| 41 | (0.75,0.25,0.00) | (2, 11) | 40.00% | y1 | -0.0425 |

## OP-OMS-002+ classification

**Nontrivial cases (≥2 attractors with distinct readouts):** 2/4

Some but not all scenes / τ settings exhibit ≥ 2 distinct attractors. **OP-OMS-002+ PARTIALLY SUPPORTED.**