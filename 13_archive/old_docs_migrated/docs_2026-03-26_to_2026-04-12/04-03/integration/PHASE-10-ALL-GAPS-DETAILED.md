# Phase 10: 모든 미증명 부분 (Complete Gap Analysis)

**Date:** 2026-04-03  
**Status:** Comprehensive audit of all proofs  
**Purpose:** Identify every logical jump, unjustified assumption, incomplete proof

---

## DOCUMENT 1: H3-ANALYTICAL-BOUND.md

### GAP 1.1: Deep Core Simplification (§2.2, Line 43-56)

**What's claimed:**
```
At deep-core sites x ∈ Core²(û) (graph distance ≥ 2 from boundary):
∇_x E_bd = 4α(Lû)_x + βW'(û_x)

"At deep core sites with û(x) ≈ 1:
- W'(1) = 0
- (Lû)_x ≈ 0
Therefore ∇_x E_bd ≈ 0"
```

**What's missing:**
1. **W'(1) = 0 claim:** 
   - Verified: W'(u) = 2u(1-u)(1-2u)
   - W'(1) = 2·1·0·(-1) = 0 ✓
   - BUT: What about the SECOND derivative? W''(1)?
   - Linearization validity: Requires |(Lû)_x| to be small enough
   - **No bound on |(Lû)_x| | at deep core before using it**

2. **(Lû)_x ≈ 0 claim:**
   - Justified AFTER in line 99-104 (exp50 data)
   - But used HERE in line 53
   - **CIRCULAR: The assumption is justified AFTER the proof**
   - Should say: "We will show |(Lû)_x| is small (exp50)"

3. **"All neighbors also near 1" claim:**
   - Why? Because δ(x) ≥ 2 means x is at distance ≥2 from Core boundary
   - This means: neighbors y ~ x are at distance ≥1 from boundary
   - So neighbors are IN Core (û ≥ 0.9) but could be at δ=1
   - Are δ=1 neighbors also "near 1"?
   - **MISSING: Proof that all neighbors of δ≥2 sites have û ≥ 0.9**

**Severity:** MODERATE (structure is correct, but logical order needs fixing)

**Fix:** Reorder proof or cite exp50 earlier

---

### GAP 1.2: Linearization Validity (§2.3, Line 61-67)

**What's claimed:**
```
W'(1 - v_x) = 2(1-v_x)v_x(1-2(1-v_x)) ≈ -2v_x + O(v_x²)

"when v_x ≪ 1"
```

**What's missing:**
1. **Expansion accuracy bound:**
   - First-order Taylor: W'(1-v_x) = W'(1) + W''(1)(-v_x) + O(v_x²)
   - W'(1) = 0 ✓
   - W''(u) = 2[(1-u)(1-2u) + u(-1)(1-2u) + u(1-u)(-2)]
   - W''(1) = 2[0 + 0 + 0] = 0
   - **WAIT: Second derivative also vanishes at u=1!**
   - **This means linearization gives W'(1-v_x) = O(v_x²), not -2v_x!**

2. **Second-order correction:**
   - Need W'''(1) or next-order term
   - **MISSING: Full Taylor expansion**

3. **At what v_x magnitude is linearization valid?**
   - exp50 shows v_x ≤ 0.12
   - For v_x = 0.1: W'(1-0.1) = W'(0.9) = 2·0.9·0.1·(1-1.8) = 2·0.9·0.1·(-0.8) = -0.144
   - Compare: -2·0.1 = -0.2 (error ≈ 30%)
   - **MISSING: Error bound on linearization**

**Severity:** CRITICAL (affects validity of screened Poisson bound)

**Fix:** Derive full Taylor expansion: W'(1-v_x) = -2v_x + O(v_x²) with explicit O(v_x²) term

---

### GAP 1.3: Screened Poisson Screening Parameter (§2.4, Line 81-83)

**What's claimed:**
```
At a deep-core site x ∈ Core² with δ(x) ≥ 2, the deviation v_x 
satisfies a discrete screened Poisson equation:

2β·v_x - 4α(Lv)_x = S_x

with screening parameter κ² = β/(2α)
```

**What's missing:**
1. **Where does this equation come from?**
   - From KKT: ∇E_bd + ∇E_cl + ∇E_sep = ν
   - ∇E_bd ≈ -2β·v_x + 4α(Lû)_x
   - But (Lû)_x = ... = -(Lv)_x (since û = 1 - v at deep core)
   - **Missing: Derivation from KKT to screened equation**

2. **What is S_x exactly?**
   - Line says: "source terms: operator gradients minus the global Lagrange multiplier ν"
   - But exact formula for S_x is not given here
   - **Missing: Explicit S_x = ν - λ_cl∇E_cl - λ_sep∇E_sep definition**

3. **Boundary conditions for screened Poisson:**
   - "decays exponentially from the core boundary"
   - But what are the actual boundary values v(∂Core²)?
   - Are they all equal?
   - **Missing: Specification of boundary conditions**

**Severity:** HIGH (fundamental equation not fully derived)

**Fix:** Add full derivation section before §2.4

---

### GAP 1.4: Maximum Principle on Discrete Graphs (§2.4, Line 81-84)

**What's claimed:**
```
The fundamental solution decays exponentially from the 
core boundary with screening length c₀ = arccosh(1 + κ²/(2d_min)).
At depth δ ≥ 2:
v_x ≤ C₁e^{-c₀·δ} + C₂^eff/β
```

**What's missing:**
1. **Maximum Principle for discrete Laplacian:**
   - Quoted as fact, not proved
   - Does discrete maximum principle hold on finite graphs?
   - What are the exact conditions?
   - **Missing: Statement of discrete maximum principle with conditions**

2. **Screening length formula:**
   - c₀ = arccosh(1 + κ²/(2d_min))
   - Where does this formula come from?
   - Is it from Helmholtz equation on graphs?
   - **Missing: Derivation or reference**

3. **Solution decay formula:**
   - "v_x ≤ C₁e^{-c₀·δ} + C₂^eff/β"
   - This assumes: exponential decay from boundary + source term contribution
   - Is this the exact solution form or an upper bound?
   - **Missing: Justification of this formula**

**Severity:** HIGH (relies on unproven PDE/graph theory)

**Fix:** Either add proof of discrete maximum principle or cite authoritative reference

---

### GAP 1.5: Boundary Condition C₁ ≈ 0.4 (§2.4, Line 87)

**What's claimed:**
```
C₁ is the boundary value (~0.4)
```

**What's missing:**
1. **Why 0.4?**
   - At Core boundary (δ=1): û ≈ 0.5 (transition layer)
   - So v = 1 - 0.5 = 0.5 (not 0.4!)
   - **Inconsistency: boundary says 0.4, but transition layer says 0.5**

2. **Is v_boundary uniform?**
   - Different boundary sites could have different û values
   - Could vary from 0.4 to 0.6
   - **Missing: Analysis of boundary value variation**

3. **Proof that C₁·e^{-2c₀} = 0.034:**
   - Uses C₁ = 0.4
   - exp50 data shows actual: varies 0.03-0.05
   - **Missing: Justification for using 0.4 specifically**

**Severity:** MODERATE (small numerical impact, but logically loose)

**Fix:** Clarify boundary layer analysis: what is the actual range of v at δ=1?

---

### GAP 1.6: Operator Correction C₂^eff Bound (§2.4, Line 89-93)

**What's claimed:**
```
Closure contribution: λ_cl · 2|r_x|(1 + J_Cl,core) ≤ 0.63 at core
Separation contribution: λ_sep · 0.04 at core (D ≈ 1)
Total C₂^eff ≤ 0.671 for n ≥ 100
```

**What's missing:**
1. **Where does "2|r_x|(1 + J_Cl,core)" come from?**
   - ∇E_cl = -2r + 2(J_Cl^T r)
   - | ∇E_cl | ≤ 2(|r| + |J_Cl^T r|) ≤ 2(|r| + J_Cl |r|) = 2|r|(1 + J_Cl)
   - OK, this is correct ✓
   - **BUT: Is |J_Cl| = J_Cl,core everywhere? Or only at core?**
   - **Missing: Clarification of where this bound applies**

2. **Why is λ_sep contribution 0.04?**
   - ∇E_sep = (1 - D) - J_D u
   - At core: D ≈ 1, so |1-D| ≈ 0
   - **Missing: Exact derivation of 0.04 bound**

3. **How is C₂^eff ≤ 0.671 computed?**
   - References §3.3, which gives weighted average formula
   - But that section is in the NEXT PILLAR (Jacobian analysis)
   - **Circular reference: uses result from Pillar 2 within Pillar 1**

**Severity:** HIGH (creates dependency between pillars)

**Fix:** Either move Jacobian analysis before KKT, or state C₂^eff as a placeholder here

---

### GAP 1.7: Hop Correction Factor (§2.5, Line 114)

**What's claimed:**
```
"With safety factor 2 for hop corrections and the boundary layer: 
β > 3α suffices for n ≥ 100. The conservative universal threshold 
β > 7α provides additional margin"
```

**What's missing:**
1. **What is "hop correction factor 2"?**
   - Where does this factor come from?
   - Why is it exactly 2, not 1.5 or 2.5?
   - **Missing: Explicit justification**

2. **Why is β > 3α raised to β > 7α?**
   - The document says this is "additional margin for small grids"
   - But by how much?
   - For what grid sizes is β > 3α insufficient?
   - **Missing: Analysis of which grids need β > 7α**

3. **Is β > 7α empirically optimal?**
   - exp31 shows β_crit = 5-10α depending on grid
   - Why report β > 7α as the "conservative universal threshold"?
   - Could use β > 5α instead?
   - **Missing: Justification for factor of 7 specifically**

**Severity:** MODERATE (affects reported threshold, not proof validity)

**Fix:** Document the hop correction factor derivation explicitly

---

### GAP 1.8: Sard's Theorem Application (§4, Line 217)

**What's claimed:**
```
"The condition |Core| ≥ 25 and β > 7α defines an open set in 
parameter space. The set of parameters where the minimizer is 
degenerate (i.e., the Hessian has a zero eigenvalue on the volume 
constraint tangent space) is a codimension-1 submanifold, hence 
measure-zero by Sard's theorem."
```

**What's missing:**
1. **What is the parameter space exactly?**
   - Is it (α, β, λ_cl, λ_sep)?
   - Or is it (α, β) with weights fixed?
   - Dimensionality matters for Sard!
   - **Missing: Explicit parameter space definition**

2. **Is the degeneracy set really codimension-1?**
   - Degeneracy: Hessian has zero eigenvalue on T Σ_m
   - This requires a manifold constraint (dimension n-1)
   - The condition is an additional equation (reduces dimension by 1)
   - So in parameter space... dimension reduction depends on structure
   - **Missing: Rigorous dimensional analysis**

3. **Does Sard's theorem apply?**
   - Sard: smooth map f : M → N, critical values have measure zero
   - But we need: "degenerate parameters" ⊂ parameter space to have measure zero
   - This requires the degeneracy CONDITION to be a smooth map
   - **Missing: Verification that degeneracy condition is smooth**

4. **What does "measure-zero" mean for Sard?**
   - Sard's theorem uses Hausdorff measure
   - In ℝ⁴, codimension-1 = dimension 3, hence measure 0 in ℝ⁴ ✓
   - But is the parameter space actually ℝ⁴?
   - Or is it constrained (e.g., α, β > 0)?
   - **Missing: Measure-theoretic specification**

**Severity:** MODERATE (Sard is standard, but application details missing)

**Fix:** Add precise statement: "In the open cone α, β > 0, λ ∈ Δ_3, the set..."

---

### GAP 1.9: T-Persist-1(d) Upgrade Logic (§6.1, Line 288-294)

**What's claimed:**
```
"With H3 proved (β > 7α suffices), the remaining condition is the 
IFT smallness ε₁ < μ·γ_int/2, which is satisfied when the temporal 
perturbation is small relative to the spectral gap — a structurally 
necessary condition, not an additional hypothesis.

Status: T-Persist-1(d) → Cat A"
```

**What's missing:**
1. **Is ε₁ < μ·γ_int/2 automatic or additional?**
   - The text claims it's "structurally necessary"
   - But is it PROVEN to hold?
   - Or is it an assumption of T-Persist-1(d)?
   - **Missing: Citation to where this is proved**

2. **Is T-Persist-1(d) definition satisfied?**
   - T-Persist-1(d) requires: γ_int > 2ε₁/μ
   - H3 proves: γ_int > 0.37
   - Are ε₁ and μ bounded such that 2ε₁/μ < 0.37?
   - **Missing: Quantitative verification**

3. **Does H3 Cat A imply T-Persist-1(d) Cat A?**
   - T-Persist-1(d) has components (a)-(e)
   - We showed (d) γ_int > 0 is satisfied
   - But what about (a) IFT condition?
   - **Missing: Check that ALL components are satisfied**

**Severity:** HIGH (categorical claim without full verification)

**Fix:** Explicitly verify all T-Persist-1(d) conditions before upgrading to Cat A

---

## DOCUMENT 2: H3-JACOBIAN-ANALYSIS.md

### GAP 2.1: Tightness of Jacobian Bounds (§2.2, Line 69-85)

**What's claimed:**
```
"These are **tight** values, not just upper bounds. They are exact 
when the field is exactly at the idealized values (u=1 at core, u=0 
at exterior, u=0.5 at boundary)."
```

**What's missing:**
1. **Are these really "tight"?**
   - "Tight" typically means: ∃ example where bound is achieved
   - Measured J_core ∈ [0.237, 0.255], theory 0.224
   - Measured is LARGER than theory!
   - **This contradicts the "tight" claim**

2. **"Exact when field is at idealized values":**
   - But u is NEVER exactly 1 at any site
   - exp50 shows u_core max 0.98, typically 0.95
   - So the "exact" condition is never met
   - **This makes the claim vacuous**

3. **Why is measured J_core > theory?**
   - Theory assumes û ≥ 0.9 → z ≥ 1.2 → σ'(z) ≤ 0.176 → J ≤ 0.264 ✓
   - But measured mean 0.220 < theory 0.224
   - This is CONSISTENT (measured < tight upper bound) ✓
   - **But the text says "tight" which is misleading**

**Severity:** LOW (terminology issue, bounds are correct)

**Fix:** Replace "tight" with "sharp upper bound" or "near-optimal"

---

### GAP 2.2: Formation-Conditioned Residual Bounds (§3.2, Line 113-117)

**What's claimed:**
```
"At boundary sites: The worst-case trivial bound is |r_x| ≤ 1, but 
at actual minimizers the residual is **also** O(0.15–0.20).

Measured: mean |r_x| = 0.15–0.20 at boundary sites. This is because 
the energy balance constrains the field even at boundary sites — the 
formation is a KKT equilibrium, not an arbitrary field."
```

**What's missing:**
1. **Why is |r_x| ≤ 0.20 at boundary?**
   - Intuition: "energy balance constrains the field"
   - But where is the PROOF?
   - **Missing: Rigorous derivation from KKT equilibrium**

2. **Is this bound universal or grid-dependent?**
   - Data shows variation: 0.125 to 0.202
   - Is this because different grids have different properties?
   - **Missing: Analysis of variation with grid size, β, etc.**

3. **For small grids (n < 64), is 0.20 still valid?**
   - Examined: 8×8, 10×10, 15×15, 20×20
   - All show similar residuals
   - But what about n = 64 (critical threshold)?
   - **Missing: Verification at boundary n = 64**

**Severity:** HIGH (this is the key formation-conditioned assumption)

**Fix:** Add rigorous KKT-based derivation: show why |r_x| ≤ 0.20 at boundary

---

### GAP 2.3: Separation Gradient at Core (§3.2, Line 127)

**What's claimed:**
```
Separation contribution: λ_sep · 0.04 at core (D ≈ 1)
```

**What's missing:**
1. **How is 0.04 derived?**
   - ∇E_sep = (1 - D) - J_D u
   - At core: D ≈ 1, u ≈ 1
   - So |∇E_sep| ≈ |0 - J_D·1| = |J_D|
   - What is J_D,core?
   - **Missing: Explicit calculation**

2. **Is D really ≈ 1 at core?**
   - D measures distinction from exterior
   - At core (û ≈ 1): yes, D → 1 ✓
   - But how close? D = 0.98? 0.99?
   - **Missing: Quantitative analysis of D at core**

3. **Default λ_sep value:**
   - The doc uses λ_sep = 1/3 (equal weights)
   - Is 0.04 derived with this assumption?
   - What if λ_sep = 0.5 (different weights)?
   - **Missing: Sensitivity analysis**

**Severity:** MODERATE (relatively minor contribution to C₂^eff)

**Fix:** Derive D behavior and J_D bound explicitly

---

### GAP 2.4: Site-Weighted C₂^eff Formula Justification (§3.4, Line 164-168)

**What's claimed:**
```
"Proposition 4 (Site-Weighted C₂^eff):
C₂^eff = (n_bdy/n)·C₂^max + (1 - n_bdy/n)·C₂^sat

Proof. The Lagrange multiplier ν couples all sites via the volume 
constraint. The effective operator correction at any deep-core site 
is bounded by the spatially averaged gradient magnitude, since ν is 
the mean and each site contributes proportionally."
```

**What's missing:**
1. **"ν is the mean":**
   - ν is NOT exactly the mean, it's the Lagrange multiplier
   - The PROOF claims: ν = (1/n)·Σ∇E (approximately)
   - Is this approximate or exact?
   - **Missing: Rigorous connection between ν and mean**

2. **"Each site contributes proportionally":**
   - How is this formalized?
   - Different sites have different ∇E magnitudes
   - Why is the weighting (n_bdy/n) and not something else?
   - **Missing: Formal derivation of weighting**

3. **Is the formula really a bound, or an approximation?**
   - "C₂^eff ≤ ..." (should be an upper bound)
   - But the derivation sounds like an equality or average
   - **Missing: Clarification of ≤ vs =**

4. **Independence of weighting from β?**
   - Does n_bdy change with β?
   - If interface width ∝ 1/√β, then for large β, interface shrinks
   - Does n_bdy become smaller?
   - **Missing: β-dependence of n_bdy**

**Severity:** CRITICAL (this is the KEY result of Pillar 2)

**Fix:** Add formal theorem with:
- Explicit definition of n_bdy in terms of field structure
- Proof that C₂^eff ≤ weighted average (with inequalities)
- Analysis of β-dependence

---

### GAP 2.5: Scaling Exponent n_bdy (§4.1, Line 97-112)

**What's claimed:**
```
n_bdy = O(√n) confirmed. Ratio n_bdy/√n ∈ [0.10, 0.60] with 
variability from formation shape.

Extended validation:
n_bdy/n = 2.9% at 25×25
n_bdy/n = 2.7% at 30×30

"n_bdy scaling exponent ≈ 0.93 (interface width grows slightly with L). 
Key: n_bdy/n → 0 (2.7% at 30×30)"
```

**What's missing:**
1. **Is the scaling really O(√n)?**
   - Exponent 0.93 ≈ 1, not 0.5
   - If n_bdy ∝ n^0.93, then n_bdy ≈ n (almost linear!)
   - But tables show n_bdy/n → 0
   - **Inconsistency: how can n_bdy ∝ n^0.93 but n_bdy/n → 0?**

2. **Variability from formation shape:**
   - Table shows n_bdy/√n ∈ [0.10, 0.80]
   - This is HUGE variability (8× range)
   - Which shapes give 0.10 vs 0.80?
   - **Missing: Characterization of shape dependence**

3. **Theoretical prediction:**
   - From Modica-Mortola: interface width ∝ 1/√β
   - At interface width ∝ 1/√β, how many sites does it span?
   - Should be O(1) sites (constant width) not O(√n)
   - **Missing: Reconciliation with PDE theory**

**Severity:** MODERATE (exponent claim is approximate, but trend n_bdy/n→0 is correct)

**Fix:** Clarify: "n_bdy ∝ L^0.93, hence n_bdy/n = O(n^{-0.07}) → 0"

---

### GAP 2.6: Asymptotic C₂^eff (§4.2, Line 190-194)

**What's claimed:**
```
C₂^eff → C₂^sat ≈ 0.26 as n → ∞
For large grids, C₂^eff ≤ 0.671 → β > 1.34α

With formation-structured bound C₂^sat ≈ 0.42 (wait, different from 0.26?):
β ≥ 7α suffices
```

**What's missing:**
1. **Two different C₂^sat values:**
   - Line 192: C₂^sat ≈ 0.26
   - Line 234: C₂^sat ≈ 0.42
   - Which is correct?
   - **Contradiction in document**

2. **Asymptotic formula:**
   - "C₂^eff = O(n^{-1/2})·C₂^max + (1 - O(n^{-1/2}))·C₂^sat"
   - Plugging in: C₂^eff ≈ (1)·C₂^sat = 0.42 (or 0.26?)
   - But numerically at n=100: C₂^eff = 0.671
   - Why is measured 0.671 >> predicted 0.42?
   - **Missing: Explanation of discrepancy**

3. **Convergence rate:**
   - "n_bdy/n = O(n^{-0.07})"
   - Convergence is VERY slow (barely noticeable by n=10000)
   - Is the asymptotic formula useful for finite n?
   - **Missing: Discussion of convergence speed**

**Severity:** HIGH (contains internal contradictions and inconsistencies)

**Fix:** Clarify all C₂ values and reconcile with numerics

---

## DOCUMENT 3: H3-KKT-ANALYSIS.md

### GAP 3.1: ν Scaling Correction (§2.2-2.3, Line 56-75)

**What's claimed:**
```
"The Lagrange multiplier ν is determined by the full energy gradient 
(including β·W'(u) at boundary sites), so |ν| = O(β·n_bdy/n) = O(β/√n)"

But then measured values show:
β=5:   |ν|=0.50
β=30:  |ν|=0.83
β=100: |ν|=2.66

Ratio |ν|/β:
β=5:   0.10
β=30:  0.028
β=100: 0.027
```

**What's missing:**
1. **Is |ν| = O(β/√n)?**
   - Prediction: |ν| ∝ β·√(n_bdy/n)
   - At β=5, n=100: predicted |ν| ∝ 5·√(0.01) = 5·0.1 = 0.5 ✓ Match!
   - At β=30, n=100: predicted |ν| ∝ 30·0.1 = 3.0, measured 0.83 ✗ Mismatch!
   - **What explains factor of 3.6× discrepancy?**

2. **"ν is determined by the boundary balance":**
   - Claimed: ν = (β/n)·Σ W'(û) + O(1)
   - But this assumes W' varies significantly between core and boundary
   - At core: û ≈ 1, W'(1) = 0
   - At boundary: û ≈ 0.5, W'(0.5) = 2·0.5·0.5·(-1) = -0.5
   - So: Σ W' ≈ n_bdy·(-0.5)
   - Therefore: ν ≈ -(β/n)·0.5·n_bdy = -0.5·β·(n_bdy/n)
   - At β=30, n_bdy/n = 0.01: ν ≈ -0.15, measured 0.83
   - **Still 5.5× off!**
   - **Missing: Explanation of scaling discrepancy**

3. **Why can ν be both negative and positive?**
   - exp50 shows ν ranges from -0.099 to +0.177
   - Sign changes?
   - **Missing: Analysis of sign changes**

**Severity:** HIGH (fundamental discrepancy in ν scaling)

**Fix:** Reconcile theoretical O(β/√n) with measured |ν|/β ≈ 0.03

---

### GAP 3.2: Mean-Subtracted Source Term (§3.3, Line 138-142)

**What's claimed:**
```
"At deep core, the mean-subtracted source f_x = ∇_x E - ν 
satisfies: f_x = -2β v_x - 4α(Lv)_x

Since v_x > 0 and (Lv)_x ≈ 0, we get f_x ≈ -2β v_x < 0.
This means v_x = |f_x|/(2β), and |f_x| is an O(1) quantity."
```

**What's missing:**
1. **Is |f_x| = O(1)?**
   - f_x = ∇_x E - ν
   - ∇_x E ≤ (closure max) + (sep max) = ... = O(1)? or O(β)?
   - ν = O(β·n_bdy/n) = O(β/√n)
   - So f_x = O(1) - O(β/√n) ≈ -O(β/√n) for large β
   - **This is NOT O(1), it's O(β)!**
   - **Critical error in the claim**

2. **How does "mean subtraction" work?**
   - At each site x, we subtract the GLOBAL average ν
   - But ν is determined by the BOUNDARY sites' gradients
   - At deep core, ∇E is small, but we subtract a large ν from it
   - The result could be either positive or negative
   - **Missing: Detailed accounting of sign and magnitude**

**Severity:** CRITICAL (affects fundamental screened Poisson structure)

**Fix:** Redo calculation: f_x = ∇E(x) - ν where ν is determined by boundary

---

### GAP 3.3: Source Bound S_x ≤ C₂^eff (§6.2, Line 300-308)

**What's claimed:**
```
"The source S_x at core consists of operator gradient residuals:
S_x = λ_cl∇E_cl + λ_sep∇E_sep - (mean of these across all sites)

Since the mean subtraction removes the O(β) component...
we get |S_x| ≤ C₂^eff"
```

**What's missing:**
1. **What is "the mean"?**
   - Mean of ∇E_cl across all sites?
   - Mean of ∇E_sep across all sites?
   - Or mean of ALL energies?
   - **Missing: Explicit definition of which mean**

2. **Does mean subtraction really remove O(β) terms?**
   - ∇E_cl = -2r + 2(J_Cl^T r): no β dependence
   - ∇E_sep = (1-D) - J_D u: no β dependence
   - Where is the O(β) term to remove?
   - **The claim seems backwards: ∇E_cl and ∇E_sep don't have β in them!**

3. **Is |S_x| ≤ C₂^eff justified?**
   - The connection between mean subtraction and C₂^eff is unclear
   - **Missing: Explicit proof that |S_x| ≤ C₂^eff**

**Severity:** CRITICAL (links Pillar 1 and Pillar 2, but connection not clear)

**Fix:** Carefully re-derive S_x formula and show |S_x| ≤ C₂^eff

---

### GAP 3.4: Comparison of Bounds (§7.1, Table 232-245)

**What's claimed:**
```
| β=7  | 0.034 + 0.096 = 0.130  vs  measured 0.114 | 1.5× margin
```

**What's missing:**
1. **Why are different β values compared?**
   - Row shows β=7, but other rows have β=5, 10, 15, etc.
   - Why not compare at the SAME β?
   - **Missing: Justification for β=7 specifically**

2. **Is 1.5× margin sufficient?**
   - Bound says v_x ≤ 0.130
   - Measured max v_x = 0.114
   - Ratio: 0.130/0.114 = 1.14 (not 1.5!)
   - **Arithmetic error in the document**

3. **Which β should we use?**
   - For β=7: bound 0.17, measured 0.034 (5× margin)
   - For β=10: bound 0.131, measured 0.027 (4.8× margin)
   - For β=30: bound 0.064, measured 0.029 (2.2× margin)
   - The margin DECREASES with β!
   - **Missing: Explanation of why margin shrinks**

**Severity:** LOW (numerical/presentation issue)

**Fix:** Check all arithmetic, explain β-dependent margin behavior

---

## DOCUMENT 4: H3-TIGHTENING.md

### GAP 4.1: Closure Residual "Tension" (§3.1, Line 89-96)

**What's claimed:**
```
"The closure fixed point c* ≈ 0.676 (solving c = σ(3(c-0.5))).
The energy minimizer û has core values pushed toward 1 by the 
double-well, but closure pulls them toward 0.676.
The residual at core sites is r_x ≈ 0.82 - 0.95 = -0.13"
```

**What's missing:**
1. **Is c* really 0.676?**
   - Equation: c = σ(3(c - 0.5))
   - Try c = 0.676: σ(3·0.176) = σ(0.528) ≈ 0.629 ≠ 0.676
   - **Calculation error!**
   - **Missing: Correct numerical solution**

2. **Why is equilibrium û ≈ 0.95?**
   - At core, double-well pushes toward 1
   - Closure pushes toward 0.676
   - What's the equilibrium?
   - **Missing: Balance equation derivation**

3. **Measured residuals:**
   - exp50 shows |r_x| ≈ 0.16-0.19 at core
   - This is LESS than the "tension" magnitude |0.82 - 0.95| = 0.13
   - Are these the same thing?
   - **Missing: Clarification of relationship**

**Severity:** MODERATE (numerical error, but overall intuition OK)

**Fix:** Correct the closure fixed point calculation

---

### GAP 4.2: Formation-Conditioned ν_eff Formula (§4, Line 160-172)

**What's claimed:**
```
"ν_eff = |ν| + λ_cl·G_cl + λ_sep·G_sep + 4α·2d·v_max ≤ 2.47

With individual bounds:
|ν| ≲ 1.0
G_cl ≤ 0.63
G_sep ≤ 0.04
4α·2d·v_max ≤ 0.8
Total: ≤ 2.47"
```

**What's missing:**
1. **Sum of absolute bounds:**
   - 1.0 + 0.63 + 0.04 + 0.8 = 2.47 ✓ Arithmetic checks
   - **But:** Each bound is worst-case, assumed independently
   - Actual values likely have sign cancellations
   - exp50 shows max ν_eff = 4.59 from table (exceeds 2.47!)
   - **The table itself CONTRADICTS this bound**

2. **|ν| ≲ 1.0 is claimed incorrect:**
   - The document later (KKT section) says |ν| = O(β/√n)
   - exp50 shows |ν| can reach 2.66 (for β=100)
   - So |ν| ≤ 1.0 is FALSE
   - **Missing: Acknowledgment of this being disproved**

3. **v_max ≤ 0.05:**
   - Used in the Laplacian bound
   - But this assumes H3 is already proved!
   - **Circular: uses v_x bound to prove v_x bound**

**Severity:** CRITICAL (contains multiple errors and circular reasoning)

**Fix:** Acknowledge that ν_eff calculation needs refinement

---

## DOCUMENT 5: CORE-DEPTH-ISOPERIMETRIC.md

### GAP 5.1: Γ-Convergence Application (§4, Step 1, Line 121-126)

**What's claimed:**
```
"By T11, as β → ∞ with α fixed, minimizers of E_bd converge in L¹ 
to minimizers of the perimeter functional. The full energy E adds 
closure and separation terms that are perturbative for large β, so 
minimizers of E also converge to the same Γ-limit."
```

**What's missing:**
1. **Are closure and separation perturbative?**
   - E_cl = ||Cl(û) - û||² is O(1) (residual squared)
   - E_sep = ||D - 1||² is O(1)
   - E_bd ∝ β (the boundary energy scales with β)
   - Relative: E_cl/E_bd ∼ O(1)/O(β) = O(1/β) → 0 ✓
   - **But this is already mentioned, so not really a gap**

2. **Convergence of minimizers:**
   - Γ-convergence gives convergence of min values
   - Do minimizers themselves converge?
   - Need sequential compactness argument
   - **Missing: Argument that minimizers (not just values) converge**

**Severity:** LOW (Γ-convergence standard result, just needs more detail)

**Fix:** Add compactness argument for minimizer convergence

---

### GAP 5.2: Deep Interior Core Membership (§4, Step 4c, Line 156-192)

**What's claimed:**
```
"At the minimizer û_β, each interior node x satisfies the 
projected stationarity condition...

Bootstrap argument using the Euler-Lagrange structure...
v_x ≤ C_1·exp(-c_0·k) + C_2/β

For k = 2 and β ≥ 11α: v_x ≤ 0.100 + 5.75/β ≈ 0.187"
```

**What's missing:**
1. **"Projected stationarity condition":**
   - What does "projected" mean here?
   - Is it KKT conditions? Gradient projection?
   - **Missing: Definition of "projected stationarity"**

2. **Bootstrap argument:**
   - Claims: once v_x = O(1/β), the exponential bound applies
   - But the exponential bound REQUIRES O(1/β) to hold
   - **Is this circular?**
   - **Missing: Rigorous induction argument**

3. **Condition β ≥ 11α vs β ≥ 7α:**
   - This section uses β ≥ 11α
   - But H3 claims β > 7α is sufficient
   - Why the discrepancy?
   - **Missing: Explanation of different thresholds**

**Severity:** HIGH (core argument for deep core existence)

**Fix:** Separate initial bound (v_x = O(1/β) from rough KKT) from refined bound (exponential from screening)

---

### GAP 5.3: Erratum on Tightened β Threshold (§4, Line 196-200)

**What's claimed:**
```
"Erratum (2026-04-01): Tightened β threshold from 58α to 20α 
via maximum principle contraction."
```

**What's missing:**
1. **Where is the "20α" argument?**
   - The erratum header says "to be expanded"
   - But the full derivation is NOT included
   - **Missing: Actual proof of 20α**

2. **Discrepancy with H3 claim (β > 7α):**
   - CORE-DEPTH says β ≥ 20α
   - H3 says β > 7α
   - Which is correct?
   - **Missing: Reconciliation**

3. **"Maximum principle contraction":**
   - What is this?
   - Is it the same as screened Poisson maximum principle?
   - **Missing: Definition and application**

**Severity:** CRITICAL (incomplete erratum, contradicts main H3 result)

**Fix:** Either complete the 20α argument OR explain why β > 7α is better

---

## SUMMARY TABLE: ALL GAPS

| # | Document | Section | Gap | Severity |
|----|----------|---------|-----|----------|
| 1.1 | H3-ANALYTICAL-BOUND | 2.2 | Deep core simplification logic | MODERATE |
| 1.2 | H3-ANALYTICAL-BOUND | 2.3 | Linearization validity | **CRITICAL** |
| 1.3 | H3-ANALYTICAL-BOUND | 2.4 | Screened Poisson derivation | HIGH |
| 1.4 | H3-ANALYTICAL-BOUND | 2.4 | Discrete maximum principle | HIGH |
| 1.5 | H3-ANALYTICAL-BOUND | 2.4 | Boundary condition C₁ | MODERATE |
| 1.6 | H3-ANALYTICAL-BOUND | 2.4 | C₂^eff within Pillar 1 | HIGH |
| 1.7 | H3-ANALYTICAL-BOUND | 2.5 | Hop correction factor | MODERATE |
| 1.8 | H3-ANALYTICAL-BOUND | 4 | Sard's theorem details | MODERATE |
| 1.9 | H3-ANALYTICAL-BOUND | 6.1 | T-Persist-1(d) verification | HIGH |
| 2.1 | H3-JACOBIAN-ANALYSIS | 2.2 | "Tight" vs upper bound terminology | LOW |
| 2.2 | H3-JACOBIAN-ANALYSIS | 3.2 | Boundary residual |r_x|≤0.20 | **CRITICAL** |
| 2.3 | H3-JACOBIAN-ANALYSIS | 3.2 | Separation gradient | MODERATE |
| 2.4 | H3-JACOBIAN-ANALYSIS | 3.4 | C₂^eff weighting formula | **CRITICAL** |
| 2.5 | H3-JACOBIAN-ANALYSIS | 4.1 | Scaling exponent n_bdy | MODERATE |
| 2.6 | H3-JACOBIAN-ANALYSIS | 4.2 | Contradictory C₂^sat values | HIGH |
| 3.1 | H3-KKT-ANALYSIS | 2.2-2.3 | ν scaling vs measured | HIGH |
| 3.2 | H3-KKT-ANALYSIS | 3.3 | Mean-subtracted source |f_x| | **CRITICAL** |
| 3.3 | H3-KKT-ANALYSIS | 6.2 | Source bound S_x ≤ C₂^eff | **CRITICAL** |
| 3.4 | H3-KKT-ANALYSIS | 7.1 | Bound verification arithmetic | LOW |
| 4.1 | H3-TIGHTENING | 3.1 | Closure fixed point calc | MODERATE |
| 4.2 | H3-TIGHTENING | 4 | ν_eff formula contradictions | **CRITICAL** |
| 5.1 | CORE-DEPTH-ISOPERIMETRIC | 4 | Γ-convergence details | LOW |
| 5.2 | CORE-DEPTH-ISOPERIMETRIC | 4.4c | Bootstrap argument | HIGH |
| 5.3 | CORE-DEPTH-ISOPERIMETRIC | 4 | Incomplete erratum (20α) | **CRITICAL** |

---

## GRAND TOTAL

```
CRITICAL gaps (must fix for Cat A):  8
HIGH gaps (should fix):              8
MODERATE gaps (nice to fix):         9
LOW gaps (minor):                    2

Total gaps: 27
```

---

**Next Step:** Prioritize fixing all CRITICAL (8) and HIGH (8) gaps = 16 gaps requiring immediate attention.
