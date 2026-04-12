# Next Steps: Formation Tracking (exp65) and K=2 Type Resolution

**Date:** 2026-04-07  
**Session:** Synthesis of exp62-exp63 divergence analysis  
**Category:** research planning  
**Status:** Proposal for exp65 design

---

## Context

The exp62-exp63 divergence reveals that the K=2 energy landscape has **two distinct minima types** that produce opposite F''(M/2) signs. Both are mathematically sound — they measure different physical configurations.

The current Canonical Spec §13 treats F''(M/2) as a single Cat B quantity without distinguishing which K=2 type is being measured. To resolve the theory, we need:

1. **Determine which K=2 type** the Spec's regime classification (T-Persist-K-Sep vs T-Persist-K-Weak) refers to
2. **Validate the type prediction** (λ_sep → asymmetry) with direct measurement
3. **Understand grid-size effects** that make 15×15 anomalous

---

## Proposed exp65: Formation Tracking at K=2 Minimum

### Goal
Directly measure u₁(ε), u₂(ε) formation positions and masses as mass transfers along M_2, to **identify K=2 type** and correlate with λ_sep.

### Method

**Setup:** Same as exp63 (9-point perturbation along mass-transfer)
```
ε ∈ [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]
```

**At each ε, record:**

1. **Formation center positions:**
   - (x₁, y₁) = center of mass of u₁ = (Σ_i x_i·u₁[i]) / (Σ_i u₁[i])
   - (x₂, y₂) = center of mass of u₂ = (Σ_i x_i·u₂[i]) / (Σ_i u₂[i])

2. **Formation masses:**
   - m₁(ε) = Σ_i u₁[i]
   - m₂(ε) = Σ_i u₂[i]

3. **Formation separation:**
   - d_c(ε) = √[(x₁−x₂)² + (y₁−y₂)²]

4. **Overlap and rotation:**
   - θ(ε) = angle from (x₁,y₁) to (x₂,y₂)
   - overlap(ε) = u₁ · u₂ (spatial correlation)

5. **Orientation stability:**
   - Δθ = θ(ε) − θ(0) (rotation of formation pair)
   - Detect if formations swap: dθ/dε large → likely u₁↔u₂ swap

### Output

CSV file with columns:
```
epsilon, x1, y1, x2, y2, m1, m2, d_c, theta, overlap, swap_detected
```

### Analysis

#### Type Detection
```
Type A (centered): |m₁ − m₂| < 0.1M throughout ε range
Type B (off-center): max(|m₁ − m₂|) > 0.2M at some ε
```

#### Formation swaps
Count how many ε values show formation swap (θ discontinuity or dθ/dε sign change). Correlate with:
- ACF[1] from exp63 (high ACF[1] → no swaps?)
- Energy reversals (oscillations → repeated swaps?)

#### Λ_coupling Validation
For each config, compute:
$$\Lambda_\text{coupling} = \lambda_\text{rep} \cdot \frac{\omega_{jk}}{\min(\mu_j, \mu_k)}$$

where ω_jk measures formation overlap (from exp65), and μ_j, μ_k are chemical potentials.

Predict: Type B dominates when Λ_coupling large (weak interaction).

---

## Predicted Outcomes

### If Hypothesis Correct

**20×20_c0.6 (λ_sep=0.108, Type B):**
- m₁ ≫ M/2 or m₁ ≪ M/2 at ε≠0
- d_c(ε) shows exponential decay (formations merging)
- Multiple formation swaps as ε increases
- ACF[1] < −0.2 predicts high swap rate ✓

**20×20_c0.5 (λ_sep=0.202, Type A):**
- m₁ ≈ M/2 throughout
- d_c(ε) monotonic (consistent separation)
- No formation swaps
- ACF[1] ≈ −0.4 seems to contradict? (should be high if Type A)

**15×15 configs:**
- Both types might coexist with comparable stability
- exp65 might show trajectory switching between types
- Formation tracking reveals geometry-driven competition

### Alternative Outcome

If formations **don't swap** even when exp63 shows ACF[1]<0:
- Valley-hopping is NOT u₁↔u₂ swap
- Instead, likely **intra-formation shape change**: u₁ morphs into different shape (e.g., elongated vs circular)
- This would require morphology analysis beyond mass/position
- Suggests ACF[1] reflects shape variability, not type switching

---

## Timeline and Prerequisites

### Before exp65
1. ✅ Complete exp62-exp63 analysis (DONE)
2. ✅ Document K=2 type hypothesis (DONE)
3. Draft formation tracking code (1 hour)
4. Test on 1 config (15×15_c0.5) to validate tracking method (30 min)

### exp65 Execution
- Run all 4 configs (20×20 configs: ~10 min each due to optimization, 15×15 configs: ~5 min)
- Total wall time: ~30 min
- Analysis: pattern detection, swap counting (30 min)

### Follow-up
- Write doc comparing predicted vs observed type (30 min)
- If successful: propose exp66 (morphology tracking) or exp67 (Λ_coupling sweep)

---

## Code Skeleton

```python
def track_formation(graph, params, ec, u1_init, u2_init, epsilons):
    """Track formations along mass-transfer perturbation."""
    results = []
    
    for eps in epsilons:
        # Re-optimize (as in exp63)
        u1_opt, u2_opt = re_optimize_k2(...)
        
        # Compute geometric quantities
        center1 = center_of_mass(u1_opt, graph)
        center2 = center_of_mass(u2_opt, graph)
        m1, m2 = np.sum(u1_opt), np.sum(u2_opt)
        d_c = distance(center1, center2)
        theta = angle(center1, center2)
        overlap = u1_opt @ u2_opt
        
        # Detect potential swap (θ jump > π/2?)
        swap = False
        if eps > epsilons[0] and abs(theta - results[-1]['theta']) > np.pi/2:
            swap = True
        
        results.append({
            'epsilon': eps,
            'x1': center1[0], 'y1': center1[1],
            'x2': center2[0], 'y2': center2[1],
            'm1': m1, 'm2': m2,
            'd_c': d_c, 'theta': theta,
            'overlap': overlap,
            'swap_detected': swap,
        })
    
    return results
```

---

## Implications for Canonical Spec

**Current state:** F''(M/2) is Cat B (parameter-dependent sign).

**After exp65:** F''(M/2) will be **Cat C (K=2 type dependent)** with:
- **Cat A:** Characterization of which K=2 type is lower-energy given (λ_sep, grid_size)
- **Cat B/C:** F''(M/2) values for each type (parameter-specific, landscape-dependent)

This is an **honest refinement**, not a demotion. It clarifies what the quantity depends on.

**Theory implication:** The regime classification T-Persist-K-Sep vs T-Persist-K-Weak may need amendment:
- T-Persist-K-Sep: Type A (centered K=2) + strong inter-formation repulsion
- T-Persist-K-Weak: Type B (off-center K=2) + weak repulsion → formation size asymmetry

---

## Expected Impact

✅ Resolve the exp62-exp63 sign flip paradox  
✅ Validate or refute the λ_sep → Type B hypothesis  
✅ Explain 15×15 anomalies (grid geometry effects)  
✅ Provide direct measurement for Λ_coupling parameter  
✅ Enable more precise regime classification in future work  
✅ Support exp66 (morphology tracking) if shape changes are detected  

---

## References

- `docs/04-07/theory/EXP62-EXP63-DIVERGENCE.md` — Methodological divergence
- `docs/04-07/analysis/K2-FLAVOURS-AND-GRID-SIZE.md` — K=2 type classification
- `experiments/exp63_hessian_mass_transfer.py` — Base code for exp65
- Canonical Spec v2.1 §10-11 — Regime classification definitions
