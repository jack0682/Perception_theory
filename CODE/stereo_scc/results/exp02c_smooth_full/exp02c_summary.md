# exp02c: Smooth-Barrier Full-Energy Summary
## T-ST-5b Claim: ΔE_smooth > ΔE_flat, increasing in Δz and λ_z

## Per-β summary

### β=4.0
- flat baseline barrier: 0.0000
- K=2 stable configs: 16/16
- Max smooth barrier: 0.0000
- Configs above flat: 0/16
- Monotone in λ_z (Δz=1.0): True
- Monotone in Δz (λ_z=4.0): True
- **Status: NOT_SUPPORTED (no K=2 minima)**

### β=10.0
- flat baseline barrier: 0.0000
- K=2 stable configs: 16/16
- Max smooth barrier: 0.0000
- Configs above flat: 0/16
- Monotone in λ_z (Δz=1.0): True
- Monotone in Δz (λ_z=4.0): True
- **Status: NOT_SUPPORTED (no K=2 minima)**

### β=20.0
- flat baseline barrier: 0.4103
- K=2 stable configs: 16/16
- Max smooth barrier: 0.4103
- Configs above flat: 15/16
- Monotone in λ_z (Δz=1.0): True
- Monotone in Δz (λ_z=4.0): True
- **Status: SUPPORTED**

### β=50.0
- flat baseline barrier: 0.0000
- K=2 stable configs: 16/16
- Max smooth barrier: 0.0000
- Configs above flat: 0/16
- Monotone in λ_z (Δz=1.0): True
- Monotone in Δz (λ_z=4.0): True
- **Status: NOT_SUPPORTED (no K=2 minima)**

## T-ST-5b Promotion Criteria

Cat C → Cat B requires:
1. K=2 genuine local minima under smooth adjacency (K_act=2 with positive NEB barrier)
2. Barrier monotone increasing in Δz (fixed λ_z) and in λ_z (fixed Δz)
3. max barrier > flat baseline barrier
4. Result holds for at least one (β, Δz, λ_z) regime

Note: T-ST-5b is a *regime* claim — it need not hold for all β,
only for sufficiently strong phase separation (large β) and depth separation.
