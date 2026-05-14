> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# exp02b-Smooth-NEB: T-ST-5b Regime B Summary

## Setup

- Grid: 20x20, alpha=1.0, beta=4.0, rho_pers=0.05
- Smooth adjacency: w_ij = w_2d * exp(-λ_z * |z_i - z_j|²)
- Δz sweep: [0.25, 0.5, 1.0, 2.0]
- λ_z sweep: [0.5, 1.0, 2.0, 4.0, 8.0]

## Flat reference

K_flat=2, barrier_flat=0.0000

## Results grid

| Δz | λ_z | product | w_bridge | K_act | barrier | ratio |
|---|---|---|---|---|---|---|
| 0.25 | 0.5 | 0.0312 | 0.969233 | 2 | 0.0 | nan |
| 0.25 | 1.0 | 0.0625 | 0.939413 | 2 | 0.0 | nan |
| 0.25 | 2.0 | 0.125 | 0.882497 | 2 | 0.0 | nan |
| 0.25 | 4.0 | 0.25 | 0.778801 | 2 | 0.0 | nan |
| 0.25 | 8.0 | 0.5 | 0.606531 | 2 | 0.0 | nan |
| 0.5 | 0.5 | 0.125 | 0.882497 | 2 | 0.0 | nan |
| 0.5 | 1.0 | 0.25 | 0.778801 | 2 | 0.0 | nan |
| 0.5 | 2.0 | 0.5 | 0.606531 | 2 | 0.0 | nan |
| 0.5 | 4.0 | 1.0 | 0.367879 | 2 | 0.0 | nan |
| 0.5 | 8.0 | 2.0 | 0.135335 | 2 | 0.0 | nan |
| 1.0 | 0.5 | 0.5 | 0.606531 | 2 | 0.0 | nan |
| 1.0 | 1.0 | 1.0 | 0.367879 | 2 | 0.0 | nan |
| 1.0 | 2.0 | 2.0 | 0.135335 | 2 | 0.0 | nan |
| 1.0 | 4.0 | 4.0 | 0.018316 | 2 | 0.0 | nan |
| 1.0 | 8.0 | 8.0 | 0.000335 | 2 | 0.0 | nan |
| 2.0 | 0.5 | 2.0 | 0.135335 | 2 | 0.0 | nan |
| 2.0 | 1.0 | 4.0 | 0.018316 | 2 | 0.0 | nan |
| 2.0 | 2.0 | 8.0 | 0.000335 | 2 | 0.0 | nan |
| 2.0 | 4.0 | 16.0 | 0.0 | 2 | 0.0 | nan |
| 2.0 | 8.0 | 32.0 | 0.0 | 2 | 0.0 | nan |

## Summary

- K=2 stable configurations: 20/20
- Max barrier (smooth): 0.0000
- Barrier flat: 0.0000
- Monotone in λ_z (Δz=1.0): True
- Monotone in Δz (λ_z=4.0): True

## T-ST-5b Claim Status: **PARTIAL**

Cat B promotion requires: monotone barrier increase in BOTH Δz and λ_z sweeps,
and max_barrier > barrier_flat in the K=2-stable regime.
