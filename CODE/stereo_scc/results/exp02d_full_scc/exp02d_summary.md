# exp02d: Full SCC Smooth Barrier Summary

**T-ST-5b claim**: ΔE_smooth > ΔE_flat, monotone in Δz and λ_z.

Grid: 12×12  β=20.0  vol_frac=0.3

## Per-variant results

### gl_only
- Flat barrier: -0.10116
- Max smooth barrier: -0.01001
- K=2 configs with barrier > flat: 5/6
- Monotone in Δz (λ_z=4.0): False
- Monotone in λ_z (Δz=1.0): False
- **T-ST-5b status: PARTIAL (barrier above flat, monotonicity not confirmed)**

### bd_cl
- Flat barrier: -0.72222
- Max smooth barrier: -0.17920
- K=2 configs with barrier > flat: 4/6
- Monotone in Δz (λ_z=4.0): False
- Monotone in λ_z (Δz=1.0): True
- **T-ST-5b status: PARTIAL (barrier above flat, monotonicity not confirmed)**

### bd_sep
- Flat barrier: -0.24232
- Max smooth barrier: 0.18197
- K=2 configs with barrier > flat: 1/6
- Monotone in Δz (λ_z=4.0): True
- Monotone in λ_z (Δz=1.0): False
- **T-ST-5b status: PARTIAL (barrier above flat, monotonicity not confirmed)**

### full_scc
- Flat barrier: -10.95281
- Max smooth barrier: -0.29105
- K=2 configs with barrier > flat: 6/6
- Monotone in Δz (λ_z=4.0): False
- Monotone in λ_z (Δz=1.0): True
- **T-ST-5b status: PARTIAL (barrier above flat, monotonicity not confirmed)**

## T-ST-5b Cat C → Cat B promotion criteria

1. K=2 genuine local minima under smooth adjacency (positive NEB barrier)
2. max smooth barrier > flat barrier (smooth creates additional barrier)
3. Barrier monotone in Δz (depth separation) and λ_z (weight sharpness)
4. Holds for at least one energy variant with E_cl active

## Key question

Does adding E_cl (closure energy) to GL-only (E_bd) create a smooth-adjacency
barrier? Compare gl_only vs bd_cl results above.
