# M₂ Energy Landscape — Corrected Computation

**Date**: 2026-04-06  
**Grid**: 15×15 (n=225)  
**Method**: Correct per-mass `volume_fraction` in `ParameterRegistry`

## Critical Bug Analysis

### Where `volume_fraction` (= c) is used

| Location | How c is used | Impact on energy |
|----------|--------------|-----------------|
| `energy_bd`, `energy_cl`, `energy_sep` | **NOT used** — these depend only on field `u` and graph | None directly |
| `EnergyComputer.normalize_weights()` | Linearizes Hessian at `u = c·1` to compute spectral norms σ_i, then sets λ_i = w_i / σ_i | **Changes relative weights** of E_cl, E_sep, E_bd |
| `find_formation` / `_optimize_single` | Sets mass constraint `m = c·n` | **Changes feasible set** Σ_m |
| `params.validate()` | Checks c ∈ spinodal (0.2113, 0.7887) | Rejects invalid c |
| `params.beta_critical()` | Uses W''(c) to compute phase transition threshold | Changes validation |

### Verdict

**The raw energy functions are c-independent**, but the **Hessian-normalized weights** depend on c through the linearization point. Using `volume_fraction=0.3` (total mass) while optimizing at `m = M/2` (half mass) gives **wrong normalized weights**. The magnitude of error: **ΔE = 4.66** (for c=0.3 vs c=0.15 normalization).

## Part 1: E*(m) Landscape

E*(m) = min_{u ∈ Σ_m} E_self(u) with correctly matched `volume_fraction = m/n`.

**Spinodal constraint**: m must satisfy 0.2113 < m/n < 0.7887, i.e., m ∈ (47.5, 177.5).

| m | c = m/n | E*(normalized) | E*(raw) | Converged | Bind | Sep |
|---|---------|---------------|---------|-----------|------|-----|
| 10–40 | 0.044–0.178 | — | — | Outside spinodal | — | — |
| 50 | 0.2222 | 4.579 | 27.37 | ✓ | 0.850 | 0.947 |
| 60 | 0.2667 | 4.354 | 29.40 | ✓ | 0.854 | 0.938 |
| 95 | 0.4222 | 3.810 | — | ✓ | — | — |
| 100 | 0.4444 | 3.768 | — | ✓ | — | — |
| 105 | 0.4667 | 3.974 | — | ✓ | — | — |
| 110 | 0.4889 | 4.190 | — | ✓ | — | — |
| 115 | 0.5111 | 3.965 | — | ✓ | — | — |
| 120 | 0.5333 | 3.825 | — | ✓ | — | — |
| 125 | 0.5556 | 3.735 | — | ✓ | — | — |
| 130 | 0.5778 | 3.602 | — | ✓ | — | — |

**Note**: The E*(m) landscape is non-monotonic due to changing Hessian normalization at each c. The normalized weights λ_cl, λ_sep, λ_bd change with c, making cross-mass energy comparison ambiguous.

## Part 2: Curvature at M/2

Using finite differences at m = 105, 110, 115 (near M/2 = 112.5):

**E\*''(m ≈ 110) ≈ −0.0177** (negative → concave)

However, this curvature is computed across **different normalization schemes** (each mass has its own λ weights), so its physical meaning is questionable. The E*(m) function is not a single well-defined functional — it's a family indexed by c.

## Part 3: K=2 vs K=1 — Correct Computation

### Default mass: total c = 0.3 (M = 67.5)

| Configuration | E_total | Notes |
|--------------|---------|-------|
| K=1, m = 67.5 | **4.127** | Single formation, c = 0.300 |
| K=2 equal, m₁ = m₂ = 33.75 | 14.357 | c_half = 0.150 — **OUTSIDE SPINODAL** |
| K=2 asymm, m₁ = 66.5, m₂ = 1 | 10.088 | Small formation can't phase-separate |

**ΔE(K=2 − K=1) = +10.23** → K=1 overwhelmingly preferred.

**Critical**: Equal split at c = 0.3 gives c_half = 0.15, which is **below the spinodal lower bound** (0.2113). Phase separation is theoretically impossible for each half-formation. The K=2 optimization ran but produced poor formations.

### Higher masses (both halves in spinodal)

| Total c | M | c_half | E(K=1) | E(K=2) | ΔE | Winner |
|---------|---|--------|--------|--------|-----|--------|
| 0.50 | 112.5 | 0.250 ✓ | 4.078 | 9.226 | +5.15 | K=1 |
| 0.60 | 135.0 | 0.300 ✓ | 3.574 | 8.590 | +5.02 | K=1 |
| 0.70 | 157.5 | 0.350 ✓ | 3.797 | 8.306 | +4.51 | K=1 |

**K=1 is preferred at ALL tested total masses.** The energy roughly doubles for K=2 because each half-formation independently pays boundary costs.

### Normalization sensitivity

For total c = 0.5:

| Normalization | λ_cl | λ_sep | λ_bd |
|--------------|------|-------|------|
| K=1 (c=0.50) | 0.508 | 0.204 | 0.046 |
| K=2 (c=0.25) | 0.508 | 0.356 | 0.034 |

The separation weight λ_sep nearly doubles when c drops from 0.5 to 0.25 (because the Hessian of E_sep has smaller spectral norm at lower c). This makes E_sep contribute more to total energy, further penalizing K=2.

Using K=1's normalization for K=2 fields ("wrong" normalization): E = 8.86 instead of 9.23. The error is ~4%, not negligible but doesn't change the conclusion.

## Part 4: Why K=1 Always Wins on 15×15

### Physical argument
On a 15×15 grid, a single formation concentrates mass into one contiguous blob with one boundary. Splitting into two formations creates two boundaries, roughly doubling E_bd (the dominant term). The boundary cost is:

E_bd = 2α · u^T L u + β · Σ W(u_i)

Two half-formations each have their own boundary, so E_bd(K=2) ≈ 2 · E_bd(K=1 at half mass). The savings from E_cl and E_sep don't compensate.

### Structural reason
The 15×15 grid has Fiedler eigenvalue λ₂ = 0.0437. The spectral K-estimate gives K* = 1 for default parameters (only one eigenvalue below the phase transition threshold). For K=2 to be preferred, we would need:
- A graph with natural 2-cluster structure (much larger Fiedler gap)
- Or parameters where E_rep between overlapping formations exceeds the boundary cost savings

### Repulsion energy
In all K=2 runs, E_rep = 0. The formations separate spatially on their own, so repulsion adds nothing. The "cost" of K=2 is purely the doubled boundary energy.

## Conclusions

1. **The `volume_fraction` bug is real but limited**: Raw energies don't depend on c, but normalized weights do. Error magnitude: ~5% on normalized energies, up to 4.66 absolute units.

2. **K=1 is robustly preferred** on 15×15 grids across all total masses tested (c = 0.3 to 0.7). The margin is large: E(K=2)/E(K=1) ≈ 2.0–2.5.

3. **For default c=0.3, K=2 equal split is impossible**: c_half = 0.15 falls outside the spinodal range, making phase separation theoretically forbidden for each half-formation.

4. **The E*(m) curvature at M/2 is negative** (E*'' ≈ −0.018), but this doesn't imply K=2 preference because the curvature is computed across different normalization schemes. The relevant comparison is the actual optimized K=2 total energy vs K=1 energy.

5. **K=2 global stability (from prior analysis) is correct but vacuous**: K=2 can be a valid configuration, but K=1 achieves strictly lower energy on this grid. The prior analysis showing K=2 stability proved that K=2 is a local minimum of the K-field energy, not that it's the global minimum.
