# Task #2: Regime Conditions Comparative Analysis

**Date:** 2026-04-02
**Session:** Phase A — regime condition unification
**Category:** analysis
**Status:** complete
**Depends on:** THREE-REGIME-SYNTHESIS.md, T-PERSIST-K-STRONG-MORSE-ATTEMPT.md, Canonical Spec v2.0 §10-13

---

## 1. Conditions by Regime (Side-by-Side Table)

### Regime I: Well-Separated (T-Persist-K-Sep)

| Condition | Symbol | Mathematical Form | Controls |
|-----------|--------|-------------------|----------|
| Per-formation hypotheses | (H1-K) | Each $u^k$ satisfies T-Persist-1 (H1)-(H4) | Single-formation persistence package |
| Well-separation | (WS) | $d_{\min}(j,k) \geq D_{\text{sep}} \geq 3$; $4\varepsilon_1/\min_k \mu_k < D_{\text{sep}} - 2$ | Exponential core decoupling; automatic simplex satisfaction |
| Spectral-repulsion compatibility | (SR) | $\min_k \mu_k > (K-1)\lambda_{\text{rep}}$ | Positive joint spectral gap via Weyl bound |

**Status:** Proved. Three conditions total.

### Regime II: Weakly-Interacting (T-Persist-K-Weak)

| Condition | Symbol | Mathematical Form | Controls |
|-----------|--------|-------------------|----------|
| Per-formation hypotheses | (H1-K) | Each $u^k$ satisfies T-Persist-1 (H1)-(H4) | Single-formation persistence package |
| Weak interaction | (WI) | $\|O_{jk}\| \leq 0.2 \cdot \min(\|\text{Core}_j\|, \|\text{Core}_k\|)$ | Overlap limited to boundary scale |
| Spectral-repulsion compatibility | (SR) | $\min_k \mu_k > (K-1)\lambda_{\text{rep}}$ | Positive joint spectral gap |
| Joint non-bifurcation | (NB-K) | $\mu_{\text{joint}} > \mu_0$ | IFT displacement bounded; basin containment |

**Status:** Conditionally proved. Four conditions total.

### Regime III: Strongly-Interacting (T-Persist-K-Strong)

#### Branch A: Coexistence (CT-KS1)

| Condition | Symbol | Mathematical Form | Controls |
|-----------|--------|-------------------|----------|
| Per-formation hypotheses | (H1-K) | Each $u^k$ satisfies T-Persist-1 (H1)-(H4) | Single-formation persistence package |
| Spectral-repulsion compatibility | (SR) | $\min_k \mu_k > (K-1)\lambda_{\text{rep}}$ | Positive joint spectral gap |
| Overlap spectral stability | $\mu_{\text{overlap}} > 0$ | $\lambda_{\min}(H_{\text{joint}}\|_{O_{jk}}) > 0$ | Local energy landscape non-degenerate at overlap |
| Strong-regime selection | (SS) | Transported/reoptimized branch stays on K-formation continuation | Rules out branch jumping |

**Status:** Conditionally defensible. Four conditions total.

#### Branch B: Merge (CT-KS4, conditional)

| Condition | Symbol | Mathematical Form | Controls |
|-----------|--------|-------------------|----------|
| Overlap instability | $\mu_{\text{overlap}} \leq 0$ | $\lambda_{\min}(H_{\text{joint}}\|_{O_{jk}}) \leq 0$ | Loss of strict local minimality in overlap direction |
| Morse non-degeneracy | (MS1) | Transversality near overlapping branch | Controlled saddle structure |
| Lower competitor existence | (MS2) | $\exists$ $(K{-}1)$-formation critical point in same sublevel component | Merge target exists |
| Flow confinement | (MS3) | Projected gradient flow stays in sublevel component | No escape to another K-branch |
| Transport selection | (MS4) | Transport continuation compatible with descending branch | Correct branch selected |

**Status:** Conjectured. Five conditions total, none of (MS1)-(MS4) proved.

---

## 2. Universal vs Regime-Specific Conditions

| Condition | Sep | Weak | Strong-Coexist | Strong-Merge | Role |
|-----------|-----|------|----------------|--------------|------|
| **(H1-K)** per-formation | **Yes** | **Yes** | **Yes** | N/A | Single-formation persistence package |
| **(SR)** spectral-repulsion | **Yes** | **Yes** | **Yes** | Violated | Joint spectral gap positivity |
| **(WS)** well-separation | **Yes** | No | No | No | Exponential gradient decoupling at cores |
| **(WI)** weak interaction bound | No | **Yes** | No | No | Overlap bounded to boundary scale |
| **(NB-K)** joint non-bifurcation | Implied by (WS)+(SR) | **Yes** (explicit) | Subsumed by $\mu_{\text{overlap}} > 0$ | N/A | Quantitative IFT control |
| **$\mu_{\text{overlap}} > 0$** | Automatic | Automatic | **Yes** | Violated | Overlap-block stability |
| **(SS)** strong selection | Trivial | Not needed | **Yes** | N/A | Branch uniqueness |
| **(MS1-MS4)** Morse hypotheses | N/A | N/A | N/A | **Yes** (all four) | Merge branch selection |

### Classification

**Universal conditions** (present in all persistence-type regimes):
1. **(H1-K)**: Per-formation T-Persist-1 hypotheses — structurally necessary in every regime.
2. **(SR)**: Spectral-repulsion compatibility — structurally necessary for positive joint spectral gap. In Sep regime, practically automatic (exponentially small coupling). In Strong-Merge, it is violated by definition.

**Regime-specific conditions:**
- **(WS)** is Sep-specific: provides the exponential decay estimates that make coupling negligible.
- **(WI)** is Weak-specific: quantitative overlap bound. The 0.2 threshold is conservative.
- **(NB-K)** is explicitly stated only in Weak, but is logically present (and automatically satisfied) in Sep.
- **$\mu_{\text{overlap}} > 0$** is Strong-specific: becomes the decisive criterion only when overlap is core-scale.
- **(SS)** and **(MS1-MS4)** are Strong-specific: branch selection and Morse structure.

---

## 3. Common Control Parameters

Five parameters govern the regime landscape. Their roles shift across regimes:

### 3.1. $\mu_k$ (per-formation spectral gap)

| Regime | Role |
|--------|------|
| Sep | Determines IFT displacement bound: $\|u^k_s - u^k_t\| \leq 2\varepsilon_1/\mu_k$. Enters (SR) as $\min_k \mu_k$. |
| Weak | Same as Sep, plus controls joint spectral gap denominator: $\mu_{\text{joint}} \geq \min_k \mu_k - (K{-}1)\lambda_{\text{rep}}$. |
| Strong | Determines whether the coexistence window exists. Large $\mu_k$ can compensate for large $\lambda_{\text{rep}} \cdot \omega_{jk}$. |

### 3.2. $\lambda_{\text{rep}}$ (repulsion strength)

| Regime | Role |
|--------|------|
| Sep | Enters only through (SR). Gradient perturbation at core sites is exponentially small regardless of $\lambda_{\text{rep}}$. |
| Weak | Dual role: maintains separation (beneficial) but also contributes off-diagonal coupling $V_{jk} = \lambda_{\text{rep}} I$ (harmful). Net effect controlled by (SR). |
| Strong | Directly sets coupling strength. The ratio $\lambda_{\text{rep}}/\mu_k$ is the primary regime discriminant. |

### 3.3. $d_{\min}$ (inter-formation distance)

| Regime | Role |
|--------|------|
| Sep | **Defining parameter.** Controls exponential decay: $u^k(x) \leq 2\exp(-c_0 \cdot d_{\min})$ at other formations' cores. Determines simplex automatic satisfaction. |
| Weak | Not directly referenced. Overlap size $\|O_{jk}\|$ replaces $d_{\min}$ as the geometric control. |
| Strong | Irrelevant — formations overlap at core scale, so $d_{\min} = 0$ or $O(1)$. |

### 3.4. $\omega_{jk}$ (overlap weight / overlap ratio)

| Regime | Role |
|--------|------|
| Sep | $\omega_{jk} = O(\exp(-c_0 \cdot d_{\min})) \approx 0$. Negligible. |
| Weak | $\omega_{jk} \approx \|O_{jk}\|/\min(\|\text{Core}_j\|, \|\text{Core}_k\|) = \eta < 0.2$. Intermediate. |
| Strong | $\omega_{jk} = O(1)$. Dominates the coupling. |

### 3.5. $\beta/\alpha$ (phase separation strength)

| Regime | Role |
|--------|------|
| All regimes | Controls single-formation structure (core/boundary sharpness, interior gap). Enters through (H1-K) via the phase separation condition (PS). |
| Strong (barrier) | Additionally controls K-merge barrier height: barrier $\sim O(\beta^{0.89})$ (exp38). Larger $\beta$ makes metastable K-formation states more persistent. |

---

## 4. Is $d_{\min}$ Independent of $\Lambda_{\text{coupling}}$?

This is the central question for unified parametrization. The proposed coupling measure from UNIFIED-REGIME-PARAMETRIZATION.md is:

$$\Lambda_{\text{coupling}} = \max_{j \neq k} \frac{\lambda_{\text{rep}} \cdot \omega_{jk}}{\min(\mu_j, \mu_k)}$$

### 4.1. How $d_{\min}$ enters $\Lambda_{\text{coupling}}$

In the Sep regime, $d_{\min}$ determines $\omega_{jk}$ through the Interior Gap Proposition:

$$\omega_{jk} = O\!\left(\frac{|\partial\text{Core}| \cdot e^{-c_0 \cdot d_{\min}}}{\min(\|u^j\|_2^2, \|u^k\|_2^2)}\right)$$

So $\Lambda_{\text{coupling}}$ does encode $d_{\min}$ information — but only through its effect on $\omega_{jk}$.

### 4.2. What $d_{\min}$ provides that $\Lambda_{\text{coupling}}$ does not

The well-separation condition (WS) is **not** just about small overlap. It provides three geometrically distinct guarantees:

1. **Exponential decay at core sites** (pointwise): $u^k(x) \leq 2\exp(-c_0 \cdot d_{\min})$ at $x \in \text{Core}(u^j)$. This is a pointwise bound used in the gradient perturbation estimate. $\Lambda_{\text{coupling}}$ (which is an aggregate ratio) does not directly provide pointwise bounds.

2. **Simplex automatic satisfaction** (T-Persist-K-Sep part (e)): $\sum_k u^k(x) \leq 1 + O(K\exp(-c_0(D_{\text{sep}} - 4\varepsilon_1/\min_k \mu_k)))$. This geometric guarantee depends on the spatial gap $d_{\min}$, not on aggregate overlap.

3. **Separation preservation under perturbation** (T-Persist-K-Sep part (b)): $d_{\min}(s) \geq d_{\min}(t) - 4\varepsilon_1/\min(\mu_j,\mu_k)$. The separation budget inequality $4\varepsilon_1/\min_k \mu_k < D_{\text{sep}} - 2$ in (WS) is a purely geometric statement about distance that has no natural expression in terms of overlap ratios.

### 4.3. Can $\Lambda_{\text{coupling}}$ capture these?

**Partial yes for (1):** If $\Lambda_{\text{coupling}}$ is small, then $\omega_{jk}$ is small relative to $\mu_k/\lambda_{\text{rep}}$. On regular graphs with well-characterized decay (the Interior Gap Proposition), small $\omega_{jk}$ implies a lower bound on $d_{\min}$. But this inverse implication is **geometry-dependent** — on irregular graphs, $\omega_{jk}$ can be small without large $d_{\min}$ (e.g., two formations on opposite arms of a star graph with short geodesic distance but no overlap).

**No for (2) and (3):** Simplex satisfaction and separation preservation are inherently spatial properties. Two formations can have $\omega_{jk} = 0$ (zero overlap) yet $d_{\min} = 1$ (adjacent supports), in which case temporal perturbation could create overlap at the next timestep. The (WS) condition's separation budget prevents this; $\Lambda_{\text{coupling}}$ does not.

### 4.4. Verdict: Two-parameter regime classification needed

**$d_{\min}$ cannot be fully absorbed into $\Lambda_{\text{coupling}}$.** The correct regime classification requires at least two coordinates:

$$\text{Regime} = f(\Lambda_{\text{coupling}}, d_{\min})$$

However, the roles split cleanly:

- **$\Lambda_{\text{coupling}}$** controls the **spectral/energetic** aspects: joint Hessian positivity, IFT displacement, transport concentration depth.
- **$d_{\min}$** controls the **geometric/spatial** aspects: pointwise decay, simplex satisfaction, separation preservation under perturbation.

In the Weak and Strong regimes, $d_{\min}$ becomes uninformative (formations share support) and $\Lambda_{\text{coupling}}$ alone suffices. But for the Sep $\to$ Weak transition, $d_{\min}$ provides essential geometric guarantees that the scalar $\Lambda_{\text{coupling}}$ cannot capture.

**Compromise proposal:** Use $\Lambda_{\text{coupling}}$ as the primary regime parameter in the unified theorem statement, but retain $d_{\min}$ as a **secondary spatial guarantee** in the Sep regime via a lemma:

> **Spatial Decoupling Lemma.** If $d_{\min} \geq D_{\text{sep}} \geq 3$, then $\Lambda_{\text{coupling}} = O(\exp(-c_0 D_{\text{sep}}))$, simplex violation is $< K \cdot 10^{-3}$, and the separation budget condition is automatically satisfied for $\varepsilon_1 < (\min_k \mu_k)(D_{\text{sep}} - 2)/4$.

This lemma converts the geometric guarantee into the scalar parameter while preserving the spatial content where it matters.

---

## 5. Regime Boundary Analysis

### 5.1. Sep $\to$ Weak Transition

**Location:** Occurs when $d_{\min}$ decreases below $D_{\text{sep}} = 3$ (or equivalently, when formation supports begin to overlap at threshold $\theta_{\text{supp}}$).

**Nature: Smooth crossover, not sharp transition.**

Arguments:
- At $d_{\min} = 3$: overlap $\omega_{jk} \leq 2\exp(-3c_0) < 10^{-3}$. All Sep guarantees hold with exponentially small corrections.
- At $d_{\min} = 2$: $\omega_{jk}$ grows to $O(10^{-1})$ but remains boundary-scale. The Weak regime conditions (WI) begin to provide the relevant bounds.
- At $d_{\min} = 1$: overlap reaches $O(\eta)$ with $\eta \approx 0.1$-$0.2$. Full Weak regime.

The transition is smooth because the persistence guarantees degrade continuously:
- Deep core preservation holds throughout (depth $\geq 2$ remains decoupled)
- Only boundary sites gradually lose full concentration guarantees
- The shifted-threshold fallback interpolates between Sep (no shift) and Weak (shift at overlap sites)

In $\Lambda_{\text{coupling}}$ coordinates: the crossover occurs at $\Lambda_{\text{coupling}} \sim \varepsilon_{\text{sep}} \approx \lambda_{\text{rep}} \cdot e^{-c_0 \cdot 3} / \mu \ll 1$.

### 5.2. Weak $\to$ Strong Transition

**Location:** Occurs when $\|O_{jk}\|$ exceeds $\eta_{\text{crit}} \cdot \min(\|\text{Core}_j\|, \|\text{Core}_k\|)$ with $\eta_{\text{crit}} = 0.2$.

**Nature: Smooth crossover in the coexistence branch; eventually sharp at the merge bifurcation.**

Arguments:
- The 0.2 threshold in (WI) is quantitatively conservative (CONDITIONAL-CONDITIONS-ANALYSIS.md §T-Persist-K-Weak). There is no discontinuity in the proof mechanism at exactly $\eta = 0.2$.
- The IFT-based persistence statement works identically for $\eta = 0.19$ and $\eta = 0.21$; only the quantitative bounds change.
- The actual sharp transition occurs later, at the **merge bifurcation**: $\Lambda_{\text{coupling}} = 1/(K{-}1)$, where $\mu_{\text{joint}} = 0$ and the IFT fails.

In $\Lambda_{\text{coupling}}$ coordinates:
- Weak $\to$ Strong-Coexistence: smooth at $\Lambda_{\text{coupling}} = \eta_{\text{crit}} \cdot \lambda_{\text{rep}}/\mu$.
- Strong-Coexistence $\to$ Strong-Merge: **sharp** at $\Lambda_{\text{coupling}} = 1/(K{-}1)$ (sign change of $\mu_{\text{joint}}$).

### 5.3. Summary of Boundary Character

| Transition | Location ($\Lambda_{\text{coupling}}$) | Nature | Detectable by |
|-----------|---------------------------------------|--------|---------------|
| Sep $\to$ Weak | $\sim e^{-c_0 \cdot 3} \cdot \lambda_{\text{rep}}/\mu$ | Smooth crossover | $d_{\min}$ dropping below 3 |
| Weak $\to$ Strong-Coexist | $\sim 0.2 \cdot \lambda_{\text{rep}}/\mu$ | Smooth crossover | $\eta$ exceeding 0.2 (conventional) |
| Strong-Coexist $\to$ Merge | $= 1/(K{-}1)$ | **Sharp bifurcation** | $\mu_{\text{joint}}$ sign change |

---

## 6. Integration with Task #1 Streamlined Conditions

Task #1 (CONDITIONAL-CONDITIONS-ANALYSIS.md) reduced the single-formation T-Persist-1 conditions from 7 to 4:

| Streamlined | Original | Content |
|-------------|----------|---------|
| **(PS)** Phase separation | (PS), (H3), (H2') | $\beta/\alpha > \beta_{\text{crit}}$ |
| **(ND)** Non-degeneracy | (ND) | $\mu > 0$ (generic by Sard) |
| **(BC')** Directional basin containment | (NB), (GT) | $\|\delta u\| < r_{\text{eff}}(\mu, \mu_2, \Delta_{\text{bdy}}, f_1)$ |
| **(TC)** Transport confinement | (WR') | $\|\text{transport}(u_s) - \hat{u}_t\| < r_{\text{basin}}$ |

### 6.1. Mapping onto Regime-Specific Conditions

**Sep regime.** The (H1-K) hypothesis in T-Persist-K-Sep requires each formation to satisfy T-Persist-1. Under Task #1's streamlining:

$$(H1\text{-}K)_{\text{streamlined}} = \bigwedge_{k=1}^K \big[\text{PS}(u^k) \wedge \text{ND}(u^k) \wedge \text{BC}'(u^k) \wedge \text{TC}(u^k)\big]$$

The regime-specific conditions (WS) and (SR) remain as written — they are multi-formation conditions that Task #1 does not touch.

**Weak regime.** Same as Sep, plus:
- (WI) remains unchanged — it is a multi-formation geometric condition
- (NB-K) can be absorbed into a joint version of (BC'): replace per-formation $\mu$ with $\mu_{\text{joint}}$ in the directional basin criterion

$$(BC'\text{-}K) \quad \|\delta u^{\text{joint}}\| < r_{\text{eff}}(\mu_{\text{joint}}, \mu_2^{\text{joint}}, \Delta_{\text{bdy}}^{\text{joint}}, f_1^{\text{joint}})$$

This absorbs (NB-K) into the streamlined framework, eliminating the explicit $\mu_0 \gtrsim 4.1$ threshold.

**Strong regime (coexistence).** The strong-regime selection hypothesis (SS) cannot be absorbed into the streamlined conditions. It is a fundamentally new condition about branch topology that has no single-formation analogue.

### 6.2. Effect on Regime Boundaries

Task #1's streamlining does **not** change the regime boundaries because:

1. The regime boundaries are defined by multi-formation geometric parameters ($d_{\min}$, $\|O_{jk}\|$, $\mu_{\text{overlap}}$), not by single-formation conditions.
2. The streamlined conditions weaken the per-formation hypotheses but do not alter what counts as "well-separated" vs "weakly-interacting."
3. The one cross-regime effect is that (BC'-K) replaces the explicit (NB-K) threshold, which slightly shifts the effective Tier 1/Tier 2 boundary within the Weak regime — but this is a quantitative refinement, not a regime boundary change.

### 6.3. Unified Condition Set for T-Persist-K-Unified

Combining Task #1's streamlining with the multi-formation conditions:

| # | Condition | Scope | Source |
|---|-----------|-------|--------|
| 1 | **(PS)** Phase separation: $\beta/\alpha > \beta_{\text{crit}}$ | Per-formation | Task #1 |
| 2 | **(ND)** Non-degeneracy: $\mu_k > 0$ for all $k$ | Per-formation | Task #1 |
| 3 | **(BC'-K)** Directional basin containment (joint) | Multi-formation | Task #1 extended to joint Hessian |
| 4 | **(TC-K)** Transport confinement (per-formation) | Multi-formation | Task #1 extended to K-formation transport |
| 5 | **(SR-$\Lambda$)** Spectral-coupling bound: $\Lambda_{\text{coupling}} < 1/(K{-}1)$ | Multi-formation | UNIFIED-REGIME-PARAMETRIZATION.md |

Five conditions total. Conditions 1-4 are streamlined versions of (H1-K). Condition 5 replaces the three separate regime conditions (WS, WI/$\eta$, SR) with a single scalar bound, plus the Spatial Decoupling Lemma for Sep-regime geometric guarantees.

---

## 7. Conclusions for T-Persist-K-Unified

### Key Finding 1: One scalar is almost but not quite sufficient.

$\Lambda_{\text{coupling}}$ successfully unifies the spectral/energetic content of the three regimes. It correctly recovers Sep ($\Lambda \to 0$), Weak ($\Lambda \sim \eta \cdot \lambda_{\text{rep}}/\mu$), Strong-Coexistence ($\Lambda < 1/(K{-}1)$), and predicts the merge bifurcation ($\Lambda = 1/(K{-}1)$). However, $d_{\min}$ must be retained as a secondary spatial parameter for the Sep regime's geometric guarantees (simplex satisfaction, separation budget).

### Key Finding 2: Three universal conditions plus one regime control.

The unified theorem needs:
- **(H1-K)** streamlined to (PS) + (ND) + (BC'-K) + (TC-K) — four per-formation conditions (reduced from seven by Task #1)
- **(SR-$\Lambda$)**: $\Lambda_{\text{coupling}} < 1/(K{-}1)$ — one multi-formation spectral condition
- Plus the Spatial Decoupling Lemma for Sep-regime applications

### Key Finding 3: Two smooth crossovers and one sharp bifurcation.

The Sep $\to$ Weak and Weak $\to$ Strong-Coexistence boundaries are smooth degradations of persistence quality. The Strong-Coexistence $\to$ Merge boundary is a genuine bifurcation ($\mu_{\text{joint}}$ sign change). The unified theorem naturally handles the smooth crossovers via $\Lambda_{\text{coupling}}$-dependent bounds; the sharp bifurcation is where the unified IFT-based theorem ceases to apply.

### Key Finding 4: The merge branch requires fundamentally different tools.

No smoothly parametrized extension of the IFT-based persistence theorem can cover the merge regime ($\Lambda_{\text{coupling}} \geq 1/(K{-}1)$). The merge branch requires Morse-theoretic analysis (saddle structure, sublevel connectivity, branch selection) that is outside the scope of the unified coexistence theorem. The unified theorem should explicitly state that it covers $\Lambda_{\text{coupling}} < 1/(K{-}1)$ and should cleanly hand off to the conjectured merge dichotomy at the bifurcation boundary.

### Key Finding 5: (BC'-K) absorbs (NB-K), eliminating one condition.

The directional basin containment from Task #1 generalizes to the joint Hessian, replacing the explicit non-bifurcation threshold $\mu_0 \gtrsim 4.1$ with a geometrically tighter criterion. This means the Weak regime no longer needs (NB-K) as a separate condition — it is subsumed by the joint version of (BC').

### Recommended Unified Theorem Structure

```
T-Persist-K-Unified:
  Hypotheses: (PS), (ND), (BC'-K), (TC-K), (SR-Λ)
  Conclusion: Λ-dependent persistence bounds that degrade continuously
  
  Corollary (Sep): d_min ≥ 3 ⟹ Λ ≈ 0 ⟹ per-formation persistence
  Corollary (Weak): η < 0.2 ⟹ Λ ≪ 1 ⟹ deep-core persistence + boundary fallback  
  Corollary (Strong-Coexist): Λ < 1/(K-1) ⟹ local K-branch continuation
  
  Handoff: At Λ = 1/(K-1), the IFT fails. See Conjecture C-KS.
```
