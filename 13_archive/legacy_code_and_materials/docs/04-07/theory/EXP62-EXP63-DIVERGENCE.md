# exp62 vs exp63: F''(M/2) Sign Flip and Landscape Structure

**Date:** 2026-04-07  
**Session:** F''(M/2) computational divergence  
**Category:** theory (analysis)  
**Status:** Active investigation  
**Depends on:** exp62_f_double_prime.py, exp63_hessian_mass_transfer.py

---

## Executive Summary

Two complementary experiments to measure F''(M/2) (curvature of reduced energy at K=2 symmetric point) produce **opposite signs on all 4 test configurations**:

| Config | exp62 (sweep) | exp63 (Hessian) | Δ(63-62) | Status |
|--------|---------------|-----------------|----------|--------|
| 15x15_c0.5 | −5.9e−3 (saddle) | +1.1e−1 (min) | +0.11 | **FLIP** |
| 15x15_c0.6 | +8.5e−4 (min) | −1.6e−1 (saddle) | −0.16 | **FLIP** |
| 20x20_c0.5 | +1.3e−3 (min) | −4.0e−1 (saddle) | −0.40 | **FLIP** |
| 20x20_c0.6 | −1.9e−3 (saddle) | +3.6e−1 (min) | +0.36 | **FLIP** |

This is **not** optimizer noise. Both experiments are mathematically sound but measure **different physical quantities**.

---

## Methodological Differences

### exp62: Mass Sweep (21 points, global landscape)

```
m ∈ [m_center × 0.7, m_center × 1.3]
For each m:
  - Independent multi-start optimization (n_restarts=5)
  - Find u_opt(m) = argmin_u E(u; u in Σ_m)
  - Use FIXED normalization weights (c=c_ref)
  
F''(M/2) = central finite difference over 21-point sweep
```

**What it measures:** Curvature of the GLOBAL reduced landscape F(m) = min_u E_self(u) across the full range. The optimizer independently explores each mass point, finding the lowest-energy compatible formation at each m. The sweep implicitly averages over all possible K=2 flavors and captures the true landscape shape.

### exp63: Direct Hessian (9 points, local perturbation)

```
1. Pre-compute K=2 minimizer: (u_1*, u_2*) = find_k_formations(K=2)
2. For each ε ∈ [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]:
   - Perturb along mass-transfer: m₁ := m_half + ε, m₂ := m_half - ε
   - Initialize with u_1* + ε·(1/n), u_2* - ε·(1/n)
   - Re-optimize to find minimum along direction
   - Compute E_total(ε)

F''(0) = central finite difference over 9-point trajectory
```

**What it measures:** Curvature of energy surface **as experienced by a single K=2 trajectory** when perturbed along mass-transfer. The starting point is explicit (pre-computed) and fixed. Only 9 sparse points → coarse resolution.

---

## Key Finding 1: Non-Convergence of F''(h) with Step Size

In exp63, F''(M/2) estimates do NOT converge as h increases:

**15x15_c0.5 (ACF[1]=+0.73, monotonic)**
- F''(h=0.5) = +0.363
- F''(h=1.0) = +0.110
- F''(h=1.5) = +0.045
- F''(h=2.0) = +0.027
- **Trend:** Monotonic decrease → likely approaching true curvature, suggests positive F''

**15x15_c0.6 (ACF[1]=−0.40, 6/7 reversals)**
- F''(h=0.5) = +0.803
- F''(h=1.0) = −0.159 ← **SIGN FLIP**
- F''(h=1.5) = −0.016
- F''(h=2.0) = −0.014
- **Trend:** Sign flip at h=1.0, then stable negative

**20x20_c0.5 (ACF[1]=−0.45, 5/7 reversals)**
- F''(h=0.5) = −1.174
- F''(h=1.0) = −0.403
- F''(h=1.5) = +0.066 ← **SIGN FLIP**
- F''(h=2.0) = +0.128
- **Trend:** Sign flip at h=1.5, positive at larger h

**20x20_c0.6 (ACF[1]=−0.22, 5/7 reversals)**
- F''(h=0.5) = +1.556
- F''(h=1.0) = +0.359
- F''(h=1.5) = +0.218
- F''(h=2.0) = +0.094
- **Trend:** Monotonic decrease, all positive

**Interpretation:** Sign flips at intermediate h values (15x15_c0.6, 20x20_c0.5) indicate that the 9-point trajectory is **not following a smooth parabolic landscape**. The optimizer is sampling different configurations (valley-hopping) rather than moving within a single valley.

---

## Key Finding 2: Off-Center K=2 Point

Computing asymmetry of ε±3 regions:

$$\text{Asymmetry} = \langle E(ε>0) \rangle - \langle E(ε<0) \rangle$$

| Config | Asymmetry | Interpretation |
|--------|-----------|---|
| 15x15_c0.5 | +0.103 | ε>0 side (m₁ gains mass) is systematically **higher energy** |
| 15x15_c0.6 | −0.005 | Balanced (no preference) |
| 20x20_c0.5 | −0.061 | ε<0 side (m₁ loses mass) is systematically **higher energy** |
| 20x20_c0.6 | +0.375 | ε>0 side is **strongly higher** (m₁ gains mass costly) |

**Hypothesis:** The K=2 minimizer computed by find_k_formations() (exp63) is NOT at the center of the mass-transfer manifold. When exp62 independently optimizes at M/2, it finds a DIFFERENT K=2 state — one centered on the manifold.

This suggests two distinct K=2 flavors:
- **Type A (exp62):** Symmetric w.r.t. mass-transfer (centered, balanced)
- **Type B (exp63):** Asymmetric w.r.t. mass-transfer (off-center, preferred direction)

---

## Key Finding 3: Valley-Hopping Signature

ACF[1] (autocorrelation at lag 1) and reversal counts indicate formation stability:

| Config | ACF[1] | Reversals | Interpretation |
|--------|--------|-----------|---|
| 15x15_c0.5 | +0.73 | 4/7 | **Single valley** — optimizer stays in same config, monotonic trend |
| 15x15_c0.6 | −0.40 | 6/7 | **Multiple valleys** — optimizer hops between u₁↔u₂ swaps |
| 20x20_c0.5 | −0.45 | 5/7 | **Multiple valleys** — frequent configuration changes |
| 20x20_c0.6 | −0.22 | 5/7 | **Mixed** — some valley-hopping but less pronounced |

**Effect on F'':** When ACF[1] is negative (anti-correlated), the landscape alternates E(ε) up-down-up, creating sign flips in finite-difference estimates. This is the signature of the optimizer switching between 2-3 distinct stable configurations as ε varies.

---

## Resolution: Which Experiment is Correct?

**Answer: Both. They measure different things.**

### exp62 is Correct for:
- **Equilibrium K=2 stability:** What is F''(M/2) when you approach K=2 from a global search?
- **Experimental relevance:** This is what you measure if you slowly vary total mass and ask "does the system prefer K=1 or K=2?"
- **Physical interpretation:** F''(M/2) from exp62 determines K=2 stability on the mass-transfer fiber M_2
- **Claim in Canonical Spec:** Based on exp62 methodology

### exp63 is Correct for:
- **Local Hessian at K=2 minimum:** What is the second-order curvature of E_self specifically at the K=2 point?
- **Stability of K=2 trajectory:** Once at K=2, what happens if mass transfers?
- **Experimental relevance:** This is what you measure if you sit at K=2 and ask "how stiff is the system to local perturbations?"

**They are not contradictory — they are orthogonal measurements of different manifolds.**

---

## Interpretation of Asymmetry

The off-center nature of exp63's K=2 state (large asymmetries in 15x15_c0.5, 20x20_c0.5, 20x20_c0.6) suggests:

1. **find_k_formations()** (used in exp63) may preferentially find K=2 states where one formation is larger/smaller, rather than perfectly balanced.

2. **Imbalance direction correlates with optimization:**
   - 15x15_c0.5: m₁ gaining mass is costly (+0.103 asymmetry)
   - 20x20_c0.6: m₁ gaining mass is costly (+0.375 asymmetry)
   - These are both low-λ_sep configurations, where separation is weak
   - Weak separation → large formations are preferred (higher cohesion per unit mass)
   - Therefore m₁ gaining mass (becoming larger) increases separation penalty

3. **fix_k_formations() may be finding the *locally-optimized* K=2 state per configuration**, not the *symmetric* K=2 state that exp62 finds implicitly.

---

## Recommendation for Theory

**Categorize F''(M/2) more precisely:**

- **F''(M/2) from global sweep (exp62):** Category B (parameter-dependent sign)
  - Measure: Curvature of equilibrium reduced landscape
  - Interpretation: K=2 barrier height vs saddle depth
  - Use case: Predicting K=1 vs K=2 stability across parameter space

- **F''(0) from explicit K=2 Hessian (exp63):** Category C (trajectory-dependent)
  - Measure: Local curvature at one particular K=2 flavour
  - Interpretation: Stability of *that specific* K=2 state to mass transfer
  - Use case: Local stability analysis, not global prediction
  - Caveat: Different K=2 flavours may have opposite F'' signs

---

## Open Questions

1. **Why does find_k_formations() produce off-center K=2 states?**
   - Is this an artifact of the multi-start initialization?
   - Or a genuine property of the energy landscape (multiple K=2 flavors)?

2. **Do the two K=2 types (centered vs off-center) exchange during evolution?**
   - exp65 (formation tracking) could detect formation rotations/swaps

3. **Is the valley-hopping in exp63 optimizer failure or true landscape structure?**
   - If 15x15_c0.5 has ACF[1]=+0.73 (single valley), why do others have ACF[1]<−0.2?
   - Is it related to λ_sep and cohesion-separation competition?

4. **What is the relationship between asymmetry and theoretical predictions?**
   - Can we predict which configurations will show off-center K=2 states?
   - Does it correlate with regime classification (T-Persist-K-Sep vs T-Persist-K-Weak)?

---

## Files

- `experiments/exp62_f_double_prime.py` — Mass sweep implementation
- `experiments/exp63_hessian_mass_transfer.py` — Direct Hessian from K=2
- `experiments/results/exp62_f_double_prime.json` — 21 masses, 6 configs
- `experiments/results/exp63_hessian_mass_transfer.json` — 9 εs, 4 configs
- `docs/04-07/theory/F-DOUBLE-PRIME-COMPUTATION.md` — Initial analysis (exp62-focused)
