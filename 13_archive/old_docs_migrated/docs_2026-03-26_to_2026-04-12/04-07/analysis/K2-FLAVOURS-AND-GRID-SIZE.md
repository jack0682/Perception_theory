# K=2 Flavours and Grid-Size Effects in Mass-Transfer Manifold

**Date:** 2026-04-07  
**Session:** F''(M/2) divergence analysis  
**Category:** analysis  
**Status:** Preliminary insights  
**Related:** docs/04-07/theory/EXP62-EXP63-DIVERGENCE.md, Canonical Spec §10-11

---

## Summary

exp62 vs exp63 divergence reveals two distinct K=2 configurations that can exist on the mass-transfer manifold M_2:

- **Type A (centered):** u₁ ≈ u₂ (balanced mass), symmetric w.r.t. mass transfer → exp62 finds this implicitly
- **Type B (off-center):** u₁ ≠ u₂ (unbalanced, preferring one direction), asymmetric → exp63 finds this explicitly

The **choice of K=2 type is grid-size dependent**:
- **15×15 (small grid):** Geometric effects dominate, both types coexist with comparable stability
- **20×20 (large grid):** λ_sep parameter dominates, regime (K-Sep vs K-Weak) determines type

---

## Empirical Pattern

| Config | Grid | λ_sep | Asym | Regime | ACF[1] | Pattern |
|--------|------|-------|------|--------|--------|---------|
| 15x15_c0.5 | 15×15 | 0.204 | **+0.103** | K-Sep | +0.734 | anomaly: high λ_sep but off-center |
| 15x15_c0.6 | 15×15 | 0.108 | −0.005 | Weak | −0.401 | anomaly: low λ_sep but centered |
| 20x20_c0.5 | 20×20 | 0.202 | −0.061 | K-Sep | −0.452 | **consistent:** high λ_sep → centered |
| 20x20_c0.6 | 20×20 | 0.108 | **+0.375** | Weak | −0.218 | **consistent:** low λ_sep → off-center |

**Pattern on 20×20:** Off-center K=2 correlates with low λ_sep (Weak regime)  
**Pattern on 15×15:** No clear correlation — grid-size effects dominate

---

## Physical Interpretation: Grid Size as a Competing Effect

The K=2 type choice (centered vs off-center) is determined by two competing factors:

### Factor 1: Separation Parameter (λ_sep)

**High λ_sep (K-Sep regime):**
- Strong repulsion between formations pushes them apart
- Prefer balanced K=2 to maximize inter-formation distance
- Type A (centered): m₁ ≈ M/2, m₂ ≈ M/2 for maximum d_c

**Low λ_sep (K-Weak regime):**
- Weak repulsion allows formations to merge without strong barrier
- Prefer unbalanced K=2: one large, one small
- Type B (off-center): m₁ >> M/2 or m₁ << M/2 for asymmetric stability

### Factor 2: Geometric/Topological Constraint (Grid Size n)

On small grids (n=225 for 15×15):
- Discrete topology effects are O(1/√n) ≈ 6.7%
- Boundary effects penetrate the domain
- Limited space for two formations → geometric frustration
- Both Type A and Type B may be nearly isoenergetic

On large grids (n=400 for 20×20):
- Discrete topology effects are O(1/√n) ≈ 5%
- Bulk behavior dominates, boundaries negligible
- Sufficient space for formation positioning
- Parameter effects (λ_sep) determine stability unambiguously

---

## Hypothesis: λ_sep Asymmetry Coupling

The asymmetry magnitude may be predicted by a coupling parameter involving λ_sep and geometry:

$$\text{Asymmetry} \approx f(\lambda_\text{sep}, d_\text{c}, n)$$

where d_c is the characteristic inter-formation separation.

**Predictions:**
- Λ_coupling large (weak interaction) → large asymmetry (Type B favored)
- Λ_coupling small (strong repulsion) → small asymmetry (Type A stable)

**Test (from data):**
- 20x20_c0.6: λ_sep=0.108 (tiny), Asym=+0.375 (huge) ✓ consistent
- 20x20_c0.5: λ_sep=0.202 (large), Asym=−0.061 (small) ✓ consistent
- 15×15 cases: Data suggests grid dominates λ_sep effect, inconsistent with simple coupling

---

## Connection to Regime Classification

The Canonical Spec v2.1 distinguishes:
- **T-Persist-K-Sep:** Well-separated formations (λ_rep·ω_jk / min(μ_j, μ_k) large)
- **T-Persist-K-Weak:** Weakly-interacting formations (coupling small)

**Reinterpretation via K=2 flavours:**

**K-Sep regime (15×15_c0.5, 20×20_c0.5):**
- Type A (centered) is stable and lower-energy
- K=2 state balances masses m₁ ≈ m₂
- Formations maintain distinct identities despite proximity
- Asymmetry ∈ [−0.06, +0.10] (near-zero)

**K-Weak regime (15×15_c0.6, 20×20_c0.6):**
- Type B (off-center) becomes competitive or dominant
- K=2 state has one formation much larger
- Larger formation dominates, smaller is satellite
- Asymmetry scales with weakness: 20×20_c0.6 shows +0.375

---

## Implications for F''(M/2) Categorization

The sign flip between exp62 and exp63 is now understood:

**exp62 measures:** F''(M/2) for **averaged K=2 flavours** in global sweep
- Both Type A and Type B may contribute at different parts of sweep
- Final F'' sign depends on which type is lower-energy at M/2

**exp63 measures:** F''(0) for **one explicit K=2 flavour** (Type B, off-center)
- Directly samples the local curvature of one type
- Sign reflects curvature of that flavor's valley

**Consequence:** F''(M/2) should be promoted from Category B (parameter-dependent) to **Category C (landscape-dependent, requires trajectory specification)** until we classify which K=2 type is being measured.

---

## Recommendation: exp65 (Formation Tracking)

To resolve which K=2 type is present at each configuration:

1. **Track u₁ position:** Record spatial location (x₁, y₁) of formation 1 center
2. **Record formation masses:** m₁(ε), m₂(ε) to quantify asymmetry *directly*
3. **Identify swaps:** Detect if u₁ ↔ u₂ exchange occurs (indices swap)
4. **Classify type:** 
   - Type A: |m₁ − m₂| < 0.1M throughout
   - Type B: |m₁ − m₂| > 0.2M at minimum point

Then correlate (Type, λ_sep, asymmetry) to validate the coupling prediction.

---

## Open Questions

1. **Why is 15×15_c0.5 anomalous?**
   - High λ_sep (K-Sep) but shows off-center K=2 (Type B)
   - Grid size effect should be symmetric across c_ref values
   - Possible confound: different optimizer behavior at different c_ref?

2. **Is ACF[1] a proxy for K=2 type?**
   - ACF[1] > +0.6 ↔ Type A (monotonic, single valley)
   - ACF[1] < −0.2 ↔ Type B (oscillatory, multi-valley hopping)
   - Test in exp65: does formation tracking show correlated behavior?

3. **Can the regime boundary be predicted?**
   - Current Spec uses Λ_coupling threshold
   - Should we add grid-size term?
   - Is there a critical Λ_coupling(n) function?

4. **What drives the 15×15_c0.6 consistency?**
   - Only config with ACF[1] negative yet asymmetry near-zero
   - How can optimizer hop between valleys yet find centered K=2?
