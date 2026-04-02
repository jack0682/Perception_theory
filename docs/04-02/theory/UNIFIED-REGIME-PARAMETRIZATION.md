# Unified Regime Parametrization: λ_coupling Design

**Date:** 2026-04-02
**Session:** Generalization of T-Persist-K structural conditions + unified regime spectrum
**Category:** theory
**Status:** active — adopted as canonical coupling definition (reconciled 2026-04-02)
**Depends on:** THREE-REGIME-SYNTHESIS.md, MULTI-TEMPORAL-THEORY.md, TRANSPORT-SELECTION-ANALYSIS.md, Canonical Spec v2.0 §10-13

---

## Resume Note

This file contains a **working proposal**, not a settled parametrization.

**What to preserve:**
- The central idea that all three regimes are controlled by a coupling-to-stabilization ratio.
- The dimensional-analysis framing.
- The bifurcation interpretation near `Lambda_coupling = 1 / (K - 1)`.

**Reconciliation outcome (2026-04-02):**
- **Adopted:** Λ_coupling = λ_rep · ω_jk / min(μ_j, μ_k) as the canonical coupling definition (soft overlap weight, spectral, dimensionless).
- **d_min retained** as secondary spatial parameter via Spatial Decoupling Lemma (REGIME-CONDITIONS-COMPARATIVE.md §4.4). One scalar is sufficient for Weak/Strong; Sep needs d_min for geometric guarantees (simplex, separation budget).
- **Overlap weight:** Soft inner-product-based ω_jk (adopted, not support-based or spectral-loss-based).
- **Strong-regime threshold:** Tied to Weyl bound (1/(K-1)). May be conservative; tighter spectral perturbation is an open problem (ISOPERIMETRIC-TRANSPORT-NECESSITY.md §3.3).

## 1. Motivation

The current multi-formation temporal persistence theory has three separate theorems:

| Theorem | Regime | Key condition | Status |
|---------|--------|---------------|--------|
| T-Persist-K-Sep | Well-separated | d_min ≥ D_sep ≥ 3 | Proved |
| T-Persist-K-Weak | Weakly-interacting | \|O_jk\| ≤ 0.2·min(\|Core_j\|,\|Core_k\|) | Conditional |
| T-Persist-K-Strong | Strongly-interacting | \|O_jk\| > 0.2·min(\|Core_j\|,\|Core_k\|) | Conjectured |

**Hypothesis**: These are not three independent theorems but **special cases of one parametric family** indexed by a coupling strength measure λ_coupling. The persistence mechanism transitions smoothly across regimes, controlled by how much inter-formation coupling leaks into each formation's spectral/basin structure.

---

## 2. Analysis of Structural Conditions Across Regimes

### 2.1. What Each Regime Actually Controls

Examining the proof mechanisms:

**Sep regime** — The core mechanism is *spectral decoupling*. The joint Hessian's off-diagonal blocks V_jk = λ_rep · I are present everywhere, but their *effect* on any formation k is exponentially suppressed at deep core sites because other formations' fields are exponentially small there. The Weyl bound μ_joint ≥ min_k(μ_k) − (K−1)λ_rep gives the spectral gap, but the stronger statement is that per-formation perturbation at core sites is O(exp(−c₀·D_sep)).

**Weak regime** — Core spectral decoupling still holds at depth ≥ 2, but boundary sites experience O(1) coupling. The proof works because: (a) deep core persistence is inherited from single-formation theory, (b) boundary overlap sites get a shifted-threshold fallback. The critical quantity is the *overlap-to-core ratio* η = |O_jk|/min(|Core_j|,|Core_k|) < 0.2.

**Strong regime** — The overlap penetrates into core sites. Spectral decoupling fails at the overlap subspace. Persistence depends on whether the joint Hessian restricted to the overlap has positive spectral gap: μ_overlap(j,k) > 0 (coexistence) vs ≤ 0 (merge). The critical quantity becomes the *overlap spectral gap*.

### 2.2. The Common Control Quantity

All three regimes are ultimately controlled by **how much the inter-formation coupling degrades the per-formation spectral gap at core sites**. Define:

$$\delta\mu_k := \mu_k^{\text{single}} - \mu_k^{\text{joint}}$$

the spectral gap loss of formation k due to coupling. Then:

| Regime | δμ_k behavior |
|--------|---------------|
| Sep | δμ_k = O(exp(−c₀·d_min)) ≈ 0 |
| Weak | δμ_k = O(λ_rep · η) where η = overlap ratio |
| Strong | δμ_k = O(λ_rep) — full coupling |

The persistence theorem quality degrades smoothly as δμ_k increases from 0 toward μ_k.

---

## 3. Proposed Coupling Measure: λ_coupling

### 3.1. Definition

For a pair of formations (j,k), define:

$$\lambda_{\text{coupling}}(j,k) := \frac{\lambda_{\text{rep}} \cdot \omega_{jk}}{\min(\mu_j, \mu_k)}$$

where ω_jk is the **effective overlap weight**:

$$\omega_{jk} := \frac{\sum_{x \in X} u^j(x) \cdot u^k(x)}{\min\left(\sum_x (u^j(x))^2,\; \sum_x (u^k(x))^2\right)}$$

This is the soft (u-weighted) overlap ratio: the inner product ⟨u^j, u^k⟩ normalized by the smaller formation's self-energy.

For the full K-formation system, define:

$$\Lambda_{\text{coupling}} := \max_{j \neq k} \lambda_{\text{coupling}}(j,k)$$

### 3.2. Dimensional Analysis

- **Numerator**: λ_rep · ω_jk has units of [energy/field²] · [dimensionless] = [energy/field²]. This is the effective per-site coupling strength felt by formation k due to formation j.
- **Denominator**: μ_k has units of [energy/field²] — the per-formation spectral gap (minimum Hessian eigenvalue).
- **Ratio**: λ_coupling is dimensionless — it measures coupling relative to self-stabilization.

### 3.3. Limiting Cases

**Claim**: λ_coupling recovers the three regimes in the correct limits.

#### Case 1: λ_coupling → 0 (Sep regime)

When d_min ≥ D_sep ≥ 3, the formations' supports are disjoint at threshold θ_supp. The soft overlap weight satisfies:

$$\omega_{jk} = \frac{\langle u^j, u^k \rangle}{\min(\|u^j\|_2^2, \|u^k\|_2^2)} \leq \frac{\sum_x u^j(x) \cdot u^k(x)}{\min(\|u^j\|_2^2, \|u^k\|_2^2)}$$

At separation d_min ≥ 3, the Interior Gap Proposition gives u^j(x) ≤ 2exp(−c₀) at sites x where u^k(x) is appreciable (core of k). With c₀ = arccosh(1 + κ²/d_min) and typical κ = √(β/(2α)) ≈ 5, we get c₀ ≈ 3.2, so u^j(x) ≤ 2e^{−3.2} ≈ 0.08 at core sites of k. The inner product is dominated by boundary contributions:

$$\omega_{jk} = O\left(\frac{|\partial\text{Core}| \cdot e^{-c_0 \cdot d_{\min}}}{\text{min}(\|u^j\|_2^2, \|u^k\|_2^2)}\right) \ll 1$$

Therefore λ_coupling ≈ λ_rep · O(e^{−c₀·d_min}) / μ_k → 0 exponentially in d_min.

**Recovered condition**: λ_coupling < ε_sep ⟺ Sep regime ✓

#### Case 2: λ_coupling ~ O(η) with η < 0.2 (Weak regime)

When overlap is boundary-scale (|O_jk| ≤ η·min(|Core|)), the soft overlap weight satisfies:

$$\omega_{jk} \approx \frac{|O_{jk}| \cdot \theta_{\text{avg}}^2}{\min(|{\text{Core}}_j|, |{\text{Core}}_k|) \cdot \theta_{\text{avg}}^2} = \frac{|O_{jk}|}{\min(|{\text{Core}}_j|, |{\text{Core}}_k|)} = \eta$$

where θ_avg is the average field value at overlap sites (approximately θ_core ≈ 0.7-0.9). Thus:

$$\lambda_{\text{coupling}} \approx \frac{\lambda_{\text{rep}} \cdot \eta}{\mu_k}$$

With typical values λ_rep = 10, η = 0.1, μ_k = 100: λ_coupling ≈ 0.01. The spectral-repulsion compatibility (SR) condition min_k(μ_k) > (K−1)λ_rep ensures λ_coupling < 1/(K−1) < 1.

**Recovered condition**: ε_sep ≤ λ_coupling < η_crit ⟺ Weak regime ✓

#### Case 3: λ_coupling ~ O(1) or > 1 (Strong regime)

When overlap is core-scale (|O_jk| comparable to |Core|), ω_jk = O(1), and:

$$\lambda_{\text{coupling}} = O\left(\frac{\lambda_{\text{rep}}}{\mu_k}\right)$$

If λ_rep / μ_k ≥ 1/(K−1), the spectral-repulsion compatibility (SR) is violated, and the joint spectral gap can vanish or become negative. This is exactly the strong-regime merge criterion: μ_overlap ≤ 0.

**Recovered condition**: λ_coupling ≥ η_crit ⟺ Strong regime ✓

### 3.4. Monotonicity Properties

λ_coupling is monotonically:
- **Increasing** in λ_rep (stronger repulsion → stronger coupling)
- **Increasing** in ω_jk (more overlap → stronger coupling)
- **Decreasing** in μ_k (larger spectral gap → better self-stabilization → less relative coupling)
- **Decreasing** in d_min (larger separation → smaller ω → smaller coupling)

All four monotonicities match the physical intuition for coupling strength. ✓

---

## 4. Predicted Phase Diagram

### 4.1. Phase Boundaries

Define two critical thresholds:

$$\lambda_{\text{sep}} := \frac{\lambda_{\text{rep}} \cdot \omega_{\text{sep}}}{\mu} \qquad \text{(Sep-Weak boundary)}$$

where ω_sep is the overlap weight at d_min = D_sep = 3 (exponentially small).

$$\lambda_{\text{crit}} := \frac{1}{K-1} \qquad \text{(Weak-Strong boundary)}$$

This corresponds to the (SR) condition: when λ_coupling = 1/(K−1), we have λ_rep · ω_jk = μ_k/(K−1), i.e., the Weyl bound gives μ_joint = 0.

### 4.2. Phase Diagram (K=2)

```
λ_coupling
    ^
    |
1.0 |  ···································
    |  · STRONG: merge-prone           ·
    |  · (μ_overlap ≤ 0)               ·
    |  · Persistence: conjectured      ·
    |  ···································
    |
0.5 |  -----------------------------------  λ_crit = 1/(K-1) = 1
    |  | STRONG: coexistence            |
    |  | (μ_overlap > 0, SR violated)   |
    |  | Persistence: conditional       |
    |  -----------------------------------
    |
η_c |  ===================================  η_crit ≈ 0.2·λ_rep/μ
    |  | WEAK: boundary overlap         |
    |  | Deep core decoupled            |
    |  | Persistence: conditional       |
    |  ===================================
    |
ε_s |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ε_sep ~ exp(-c₀·D_sep)
    |  | SEP: fully decoupled           |
    |  | Per-formation persistence      |
    |  | Persistence: proved            |
    |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |
  0 +--------------------------------------> (physical parameters)
        d_min large          d_min small
        λ_rep small          λ_rep large
        μ large              μ small
```

### 4.3. Refined Strong Regime Sub-Diagram

The strong regime itself has internal structure (THREE-REGIME-SYNTHESIS.md §5). We can further decompose using:

$$\mu_{\text{overlap}}(j,k) = \lambda_{\min}\left(H_{\text{joint}}\big|_{O_{jk}}\right)$$

- **Strong-Coexistence**: λ_coupling > η_crit but μ_overlap > 0 → local IFT persistence
- **Strong-Merge**: λ_coupling > η_crit and μ_overlap ≤ 0 → instability, conjectured merge

The transition between these is a **bifurcation line** in parameter space, not a smooth crossover. This is the key distinction from the Sep→Weak transition (which is smooth).

---

## 5. Generalization of T-Persist-K Structural Conditions

### 5.1. Unified Hypothesis Set

Replace the three separate hypothesis sets with a single parametric family:

**Hypothesis (H-K-Unified).** Given K formations (u¹,...,u^K) on Σ^K_M with coupling parameter Λ_coupling:

- **(H1-K)** Per-formation: each u^k satisfies T-Persist-1 hypotheses (H1)-(H4)
- **(SR-λ)** Spectral-coupling bound: Λ_coupling < 1/(K−1)
  - Implies: μ_joint > 0 (positive joint spectral gap)
  - Reduces to: (SR) when ω_jk computed from actual overlaps
- **(TC-K)** Transport confinement (per-formation): for each k, the transport map T_k confines to B_{r_k}(u^k_t)
  - Reduces to: trivial in Sep regime (transport from u^k_t stays near u^k_t because other formations are far)
  - Non-trivial in Weak/Strong: requires self-referential cost to bias toward source structure (TRANSPORT-SELECTION-ANALYSIS.md Argument 4)

### 5.2. Unified Persistence Statement

**Theorem (T-Persist-K-Unified, predicted form).**

Let (u¹_t,...,u^K_t) be a joint minimizer of E_{K,t} on Σ^K_M. Under (H1-K), (SR-λ), (TC-K), and ε-gentle transition from t to s:

**(a) Joint minimizer persistence.** E_{K,s} has a joint minimizer with:

$$\|u^k_s - u^k_t\| \leq \frac{2\varepsilon_1}{\mu_k(1 - (K-1)\Lambda_{\text{coupling}})}$$

Note the denominator: as Λ_coupling → 1/(K−1), the displacement bound diverges — the persistence guarantee weakens smoothly.

**(b) Deep core preservation (depth-dependent).**

At core sites with depth δ(x) ≥ δ_min(Λ_coupling):

$$|u^k_s(x) - u^k_t(x)| \leq C \cdot \exp(-c_0 \cdot (\delta(x) - \delta_{\min}))$$

where δ_min is the minimum depth at which coupling effects become negligible:

$$\delta_{\min}(\Lambda_{\text{coupling}}) = \left\lceil \frac{\log(\Lambda_{\text{coupling}} \cdot \mu_k / \lambda_{\text{rep}})}{\log(1/\rho_{\text{decay}})} \right\rceil$$

with ρ_decay the per-step decay rate of coupling effects into the core interior.

- **Sep regime**: δ_min = 0 (all core sites are decoupled)
- **Weak regime**: δ_min = 1-2 (boundary sites affected, deep core safe)
- **Strong regime**: δ_min can be O(diameter) — coupling penetrates everywhere

**(c) Shifted-threshold fallback (coupling-dependent).**

At sites with depth δ(x) < δ_min:

$$u^k_s(x) \geq \theta_{\text{core}} - \frac{2\varepsilon_1}{\mu_k(1 - (K-1)\Lambda_{\text{coupling}})} - C_{\text{coup}} \cdot \Lambda_{\text{coupling}}$$

The threshold shift grows linearly with Λ_coupling.

**(d) Post-hoc correction bound.**

Simplex correction displacement:

$$\|\tilde{u}^k_s - u^k_s\|_2 \leq \frac{C_{\text{corr}} \cdot \omega_{\max} \cdot m}{1 + \lambda_{\text{bar}} / \lambda_{\text{rep}}}$$

Basin safety holds when this is < r_basin.

**(e) Transport concentration (depth-dependent).**

For sites with δ(x) ≥ δ_min + 2:

$$\frac{\sum_{y \in \text{Core}^k_s} M^*_k(x,y)}{\sum_y M^*_k(x,y)} \geq 1 - n \cdot \exp\left(-\frac{\gamma \Delta_\varphi^2(\delta - \delta_{\min})}{\varepsilon_{\text{OT}}}\right)$$

The fingerprint gap Δ_φ² is evaluated at *effective depth* δ − δ_min, reducing to the single-formation result when δ_min = 0.

### 5.3. Recovery of Existing Theorems

**T-Persist-K-Sep recovery**: When d_min ≥ D_sep, we have Λ_coupling = O(exp(−c₀·D_sep)) → 0, so:
- (a) displacement bound → 2ε₁/μ_k (single-formation)
- (b) δ_min = 0, all core sites decoupled
- (c) no coupling shift
- (d) simplex correction ~ 0
- (e) full transport concentration at depth ≥ 2

This is exactly T-Persist-K-Sep. ✓

**T-Persist-K-Weak recovery**: When η < 0.2, Λ_coupling ≈ λ_rep·η/μ_k ≪ 1, so:
- (a) displacement bound ≈ 2ε₁/μ_k · (1 + O(λ_rep·η/μ_k))
- (b) δ_min = 1-2 (boundary sites affected)
- (c) shifted threshold at overlap sites
- (d) correction bounded by overlap size
- (e) deep core (δ ≥ 2) concentration preserved

This is exactly T-Persist-K-Weak. ✓

**Strong-Coexistence recovery**: When Λ_coupling < 1/(K−1) but ω_jk = O(1):
- (a) displacement bound is O(ε₁/μ_joint) with μ_joint = μ_k − (K−1)λ_rep·ω_jk
- (b) δ_min can be large — coupling penetrates deeply
- (c) shifted threshold applies to most sites
- (d) correction can be O(1) — basin safety is the binding constraint
- (e) transport concentration only at very deep core sites

This matches the strong-regime coexistence branch (THREE-REGIME-SYNTHESIS.md §5.3A). ✓

---

## 6. The Bifurcation Boundary

### 6.1. Where the Unified Theorem Breaks

The unified theorem fails precisely at Λ_coupling = 1/(K−1), where:
- μ_joint → 0 (IFT fails)
- Displacement bound → ∞
- δ_min → ∞ (no depth is safe)

This is the **bifurcation line** separating coexistence from merge. It is NOT a failure of the parametrization — it correctly identifies the mathematical boundary.

### 6.2. What Happens Beyond the Bifurcation

At Λ_coupling > 1/(K−1):
- The joint Hessian has a negative eigenvalue
- The K-formation minimizer becomes a saddle point
- Gradient flow descends to a (K−1)-formation configuration

This is the merge branch (THREE-REGIME-SYNTHESIS.md §5.3B), which requires Morse-theoretic analysis beyond the IFT. The unified parametrization correctly **predicts where this happens** even though it cannot prove the merge outcome.

### 6.3. Sharp vs Smooth Transitions

| Transition | Nature | λ_coupling behavior |
|-----------|--------|-------------------|
| Sep → Weak | **Smooth** crossover | λ_coupling increases continuously from ~0 to ~0.2λ_rep/μ |
| Weak → Strong-Coexist | **Smooth** crossover | λ_coupling increases continuously past η_crit |
| Strong-Coexist → Merge | **Sharp** bifurcation | λ_coupling crosses 1/(K−1); μ_joint changes sign |

The first two transitions are smooth degradation of persistence guarantees. The third is a genuine phase transition (saddle-node bifurcation on Σ^K_M).

---

## 7. Comparison with Existing Regime Classification

The current `classify_regime()` in `scc/multi.py` uses discrete thresholds:
- d_min ≥ 3 → Sep
- |O_jk|/min(|Core|) < 0.2 → Weak
- else → Strong

This is a **coarsening** of the λ_coupling spectrum. The continuous parametrization is strictly more informative:

| classify_regime() | λ_coupling range | What's lost |
|-------------------|-----------------|-------------|
| 'well-separated' | [0, ε_sep] | Nothing (regime is clean) |
| 'weakly-interacting' | [ε_sep, η_crit] | Gradation within weak regime; how close to strong boundary |
| 'strongly-interacting' | [η_crit, ∞) | Coexistence vs merge distinction; distance to bifurcation |

**Recommendation**: Augment `classify_regime()` with a continuous `coupling_strength()` function returning Λ_coupling, and add a sub-classification for the strong regime (coexist vs merge-prone).

---

## 8. Feasibility Assessment

### 8.1. What is Proved by This Analysis

1. **λ_coupling is well-defined** for any K-formation configuration (requires only overlaps, spectral gaps, and λ_rep — all computable).
2. **Correct limiting behavior**: recovers Sep, Weak, and Strong-Coexistence theorems in the appropriate limits.
3. **Correct monotonicity**: all four physical monotonicities hold.
4. **Correct bifurcation**: identifies the merge boundary at Λ_coupling = 1/(K−1).

### 8.2. What Remains Open

1. **Quantitative δ_min formula**: The depth at which coupling effects become negligible needs tighter bounds. Currently estimated via the Interior Gap Proposition's exponential decay, but the exact crossover depth depends on formation geometry.

2. **Transport confinement in coupled setting**: TC-K extends the single-formation transport confinement (TRANSPORT-SELECTION-ANALYSIS.md) to K formations. The self-referential cost argument (Argument 4) should generalize, but the analytical bound on coupled transport displacement is harder.

3. **Strong-regime coexistence tightness**: The condition Λ_coupling < 1/(K−1) is sufficient (from Weyl bound) but may not be necessary. The actual bifurcation could occur at a larger Λ_coupling if the Weyl bound is loose.

4. **Merge theorem**: What happens beyond the bifurcation is outside the scope of the unified IFT-based theorem. Requires Morse theory on Σ^K_M.

### 8.3. Experimental Predictions

The unified parametrization makes three testable predictions:

**P-Unified-1 (Continuous degradation):** Persist should degrade continuously as λ_coupling increases, not jump at regime boundaries. Specifically, Persist(deep core) ≈ 1 − C·Λ_coupling² for small Λ_coupling.

**P-Unified-2 (Depth-dependent onset):** The minimum depth δ at which transport concentration holds should increase with Λ_coupling. At fixed β, plot δ_min vs λ_coupling across configurations: expect a positive monotone relationship.

**P-Unified-3 (Bifurcation sharpness):** Near Λ_coupling = 1/(K−1), Persist should exhibit critical slowing (longer optimizer convergence) and eventually jump discontinuously when the bifurcation is crossed. The discontinuity distinguishes bifurcation from smooth degradation.

---

## 9. Summary

| Aspect | Result |
|--------|--------|
| **Coupling measure** | Λ_coupling = max_{j≠k} (λ_rep · ω_jk / min(μ_j, μ_k)) |
| **Sep regime** | Λ_coupling ≈ 0 (exponentially small) |
| **Weak regime** | Λ_coupling ∈ (0, η_crit), η_crit ≈ 0.2·λ_rep/μ |
| **Strong-Coexist** | Λ_coupling ∈ [η_crit, 1/(K−1)) |
| **Merge bifurcation** | Λ_coupling = 1/(K−1) |
| **Unified theorem** | Single IFT-based statement with λ_coupling-dependent bounds |
| **Key insight** | All three regimes are controlled by coupling-to-stabilization ratio |
| **Phase diagram** | Two smooth crossovers + one sharp bifurcation |
| **Testable predictions** | 3 (continuous degradation, depth onset, bifurcation sharpness) |
