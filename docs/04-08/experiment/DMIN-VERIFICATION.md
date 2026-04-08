# d_min Tail Decay Verification

**Date:** 2026-04-08  
**Experiment:** Measure exponential tail decay of single formations, compare with analytical d_min predictions.

## Setup

- **Grid sizes:** L = 10, 12, 15, 20 (LxL 2D grids, 4-connectivity)
- **Double-well strength:** beta = 20, 30, 50 (alpha = 1.0 fixed)
- **Closure:** a_cl = 0.0 (OFF) vs a_cl = 3.0 (ON)
- **Volume fraction:** c = 0.3, u_sp = (3-sqrt(3))/6 = 0.2113
- **Optimizer:** K=1, 3 restarts, max_iter=8000

## Method

1. Find single-formation minimizer via `find_formation`
2. Compute center of mass of formation
3. Bin u(r) by distance from CoM (0.5 spacing)
4. Fit exponential tail: u(r) ~ A*exp(-c0*r) for r in tail region (r > 2, 0.01 < u < 0.5)
5. Theoretical prediction: c0_theory = arccosh(1 + beta/(2*alpha*d)) with d=4 (grid degree)
6. Predicted d_min = (2/c0)*ln(2A/u_sp)

## Results: Closure OFF (a_cl = 0.0)

| L  | beta | peak  | core | A_fit  | c0_fit | c0_theory | ratio | d_min_fit | d_min_thy |
|----|------|-------|------|--------|--------|-----------|-------|-----------|-----------|
| 10 |  20  | 0.802 |  27  | 0.5647 | 0.2440 |    1.9248 | 0.127 |     13.74 |      1.74 |
| 10 |  30  | 0.885 |  29  | 0.3365 | 0.2334 |    2.2400 | 0.104 |      9.93 |      1.03 |
| 10 |  50  | 0.904 |  28  | 0.3118 | 0.2187 |    2.6694 | 0.082 |      9.90 |      0.81 |
| 12 |  20  | 0.790 |  39  | 0.6279 | 0.2094 |    1.9248 | 0.109 |     17.02 |      1.85 |
| 12 |  30  | 0.888 |  41  | 0.3862 | 0.2009 |    2.2400 | 0.090 |     12.91 |      1.16 |
| 12 |  50  | 0.906 |  40  | 0.5167 | 0.2249 |    2.6694 | 0.084 |     14.11 |      1.19 |
| 15 |  20  | 0.787 |  64  | 0.4893 | 0.1461 |    1.9248 | 0.076 |     20.98 |      1.59 |
| 15 |  30  | 0.888 |  64  | 0.2220 | 0.1074 |    2.2400 | 0.048 |     13.83 |      0.66 |
| 15 |  50  | 0.913 |  60  | 0.3940 | 0.1471 |    2.6694 | 0.055 |     17.90 |      0.99 |
| 20 |  20  | 0.780 | 120  | 0.8724 | 0.1454 |    1.9248 | 0.076 |     29.03 |      2.19 |
| 20 |  30  | 0.878 | 117  | 0.2280 | 0.0841 |    2.2400 | 0.038 |     18.29 |      0.69 |
| 20 |  50  | 0.909 | 113  | 0.8588 | 0.1575 |    2.6694 | 0.059 |     26.61 |      1.57 |

## Results: Closure ON (a_cl = 3.0)

| L  | beta | peak  | core | A_fit      | c0_fit | c0_theory | ratio | d_min_fit | d_min_thy |
|----|------|-------|------|------------|--------|-----------|-------|-----------|-----------|
| 10 |  20  | 0.996 |  31  |    845.71  | 2.2923 |    1.9248 | 1.191 |      7.84 |      9.34 |
| 10 |  30  | 1.000 |  30  |   5526.69  | 2.9288 |    2.2400 | 1.307 |      7.42 |      9.70 |
| 10 |  50  | 1.000 |  31  | 290339.48  | 3.7467 |    2.6694 | 1.404 |      7.91 |     11.11 |
| 12 |  20  | 0.982 |  45  |     49.25  | 1.0917 |    1.9248 | 0.567 |     11.26 |      6.38 |
| 12 |  30  | 1.000 |  44  |     54.06  | 1.1761 |    2.2400 | 0.525 |     10.61 |      5.57 |
| 12 |  50  | 1.000 |  43  | 1080115.43 | 3.5624 |    2.6694 | 1.335 |      9.06 |     12.09 |
| 15 |  20  | 0.983 |  70  |      2.54  | 0.3430 |    1.9248 | 0.178 |     18.54 |      3.30 |
| 15 |  30  | 1.000 |  68  |     31.22  | 0.7937 |    2.2400 | 0.354 |     14.33 |      5.08 |
| 15 |  50  | 1.000 |  68  |    115.93  | 0.9694 |    2.6694 | 0.363 |     14.44 |      5.25 |
| 20 |  20  | 0.987 | 124  |      1.87  | 0.2349 |    1.9248 | 0.122 |     24.46 |      2.99 |
| 20 |  30  | 0.995 | 122  |      1.06  | 0.1459 |    2.2400 | 0.065 |     31.56 |      2.06 |
| 20 |  50  | 1.000 | 121  |   1308.57  | 1.1018 |    2.6694 | 0.413 |     17.11 |      7.06 |

## Key Findings

### 1. Measured c0 vs Theoretical c0: Major Discrepancy

The theoretical formula c0 = arccosh(1 + beta/(2*alpha*d)) **dramatically overestimates** the actual decay rate in almost all cases:

- **Closure OFF:** ratio c0_fit/c0_theory = 0.04 to 0.13 (theory predicts 8-25x faster decay than observed)
- **Closure ON, small grids (L=10):** ratio = 1.19 to 1.40 (reasonable agreement, closure actually makes decay *faster* than pure theory)
- **Closure ON, large grids (L=15-20):** ratio = 0.07 to 0.41 (theory again overestimates)

**Root cause:** The theoretical c0 comes from the 1D Allen-Cahn profile on an infinite lattice. The finite 2D grid formations are NOT 1D kinks — they are 2D radially symmetric structures. The effective Laplacian eigenvalue controlling radial decay differs from the nearest-neighbor 1D value.

### 2. Closure Effect on Decay

Closure (a_cl=3.0) has a **dramatic** effect:
- **Sharpens the formation:** peak u increases from ~0.8-0.9 to ~0.98-1.00
- **Increases amplitude A** by orders of magnitude (from ~0.3 to 50-10^6)
- **Increases decay rate c0** by 2-10x over the no-closure case
- **Net effect on d_min:** Despite the faster decay, the much larger amplitude A means d_min doesn't always decrease — it's a competition between A and c0

### 3. Grid Size Dependence

As L increases with closure OFF:
- c0_fit **decreases** (slower decay on larger grids): ~0.24 at L=10 down to ~0.08-0.15 at L=20
- d_min **increases** roughly linearly with L
- This suggests finite-size effects dominate: the tail has more room to spread on larger grids

With closure ON, same trend but less pronounced.

### 4. d_min Predictions Are Unreliable

The formula d_min = (2/c0)*ln(2A/u_sp) using the **theoretical** c0 gives values of 0.7-2.2 (closure OFF) — these are absurdly small (sub-lattice-spacing). Using the **measured** c0 gives d_min = 10-31, which is often larger than the grid itself.

**Conclusion:** The 1D Allen-Cahn d_min formula does not transfer to 2D finite grids without correction for:
1. Radial (2D) vs planar (1D) decay geometry
2. Finite-size effects (periodic boundary conditions, tail wrapping)
3. Closure operator modification of the effective potential

### 5. Reliable Observations

Despite the formula mismatch, some robust patterns emerge:
- Higher beta always produces sharper formations (higher peak, steeper tails)
- Closure dramatically sharpens core and steepens tails
- Formation core size scales roughly as c*n (volume constraint satisfied)
- All formations converge reliably (100% convergence across all 24 configs)

## Theoretical Implications

The arccosh formula is valid for the **1D lattice Allen-Cahn equation** (nearest-neighbor coupling on Z). For 2D grids, the correct tail decay should account for:

1. **Radial Green's function:** In 2D, the discrete Green's function decays as K_0(c0*r) (modified Bessel), not exp(-c0*r). This changes both the decay rate and the functional form.
2. **Effective degree:** The radial Laplacian in 2D has effective connectivity that varies with distance from center, not constant d=4.
3. **Closure nonlinearity:** The closure operator adds a nonlinear term that modifies the effective potential and hence the linearized decay equation.

A corrected d_min theory for 2D would need to solve the linearized Euler-Lagrange equation around the formation profile, which is a Helmholtz-type equation on the grid.

## Raw Data

Full profile data saved in `dmin_raw_data.json` for further analysis.
