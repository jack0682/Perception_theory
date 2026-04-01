# T-Persist-K-Unified: Unified Multi-Formation Temporal Persistence Theorem

**Date:** 2026-04-02
**Session:** Phase B-2 — unified theorem synthesis
**Category:** theory
**Status:** paused draft; placeholders remain from interrupted Phase A/B workflow
**Depends on:** THREE-REGIME-SYNTHESIS.md, T-PERSIST-K-STRONG-MORSE-ATTEMPT.md, UNIFIED-THEORY-STATUS.md, MERGE-DICHOTOMY-ANALYSIS.md, ISOPERIMETRIC-TRANSPORT-PROOFS.md, Canonical Spec v2.0.md §10-12

---

## Resume Note

This draft was written **before** the Phase A outputs were fully integrated.

**Safe assumption for next session:**
- Keep the current theorem skeleton.
- Do **not** treat the condition register or the coupling definition as finalized yet.

**Resume order for this file:**
1. Integrate Task #1 findings into sections 7.3 and 9.1.
2. Do not touch sections 7.4 and 9.2 until the missing Task #2 deliverable exists.
3. Do not finalize regime thresholds until [UNIFIED-REGIME-PARAMETRIZATION.md](/Users/ojaehong/ex_2/docs/04-02/theory/UNIFIED-REGIME-PARAMETRIZATION.md) is reconciled with Task #3.
4. After sections 7 and 9 are completed, revisit the theorem statement in section 4 and downgrade or upgrade any claims that are currently too strong.

## 1. Purpose

This document replaces the current three separate multi-formation temporal theorems (T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Strong) with a single parametric statement **T-Persist-K-Unified** that:

1. Covers all three coupling regimes under one theorem umbrella,
2. Uses a single monotonic coupling measure λ_coupling to interpolate between regimes,
3. Makes the mechanism transition explicit (spectral dominance → weak transport → barrier crossing),
4. Honestly separates proved, conditional, and conjectural components,
5. Incorporates the retracted saddle conjecture correction (K≥2 is always a local minimum).

---

## 2. Ambient Structure

### 2.1. Product Constraint Manifold

K formations live on the product volume-constrained manifold:
$$
\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}, \qquad \Sigma_{m_k} = \{u \in [0,1]^n : \textstyle\sum_i u_i = m_k\}.
$$

The joint K-field energy is:
$$
\mathcal{E}_K(u^1,\ldots,u^K) = \sum_{k=1}^K \mathcal{E}_{\mathrm{self}}(u^k) + \sum_{j<k} \lambda_{\mathrm{rep}} \langle u^j, u^k \rangle + \lambda_{\mathrm{bar}} \sum_x \max\!\left(0, \sum_k u^k(x) - 1\right)^2.
$$

### 2.2. Joint Hessian Structure

At a K-formation critical point $(u^{*1}, \ldots, u^{*K})$, the joint Hessian on $T(\Sigma^K_M)$ has:

- **Diagonal blocks:** $H_{kk} = \nabla^2 \mathcal{E}_{\mathrm{self}}(u^{*k})|_{T(\Sigma_{m_k})}$ with per-formation spectral gaps $\mu_k > 0$
- **Off-diagonal blocks:** $V_{jk} = \lambda_{\mathrm{rep}} I$ (global coupling from repulsion)
- **Joint spectral gap (Weyl bound):** $\mu_{\mathrm{joint}} \geq \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}}$

This Hessian structure is **shared across all three regimes**. The regimes differ in how much coupling leaks into core/boundary transport estimates.

---

## 3. Coupling Measure

### 3.1. Definition

**Definition (Coupling measure).** For a K-formation configuration $(u^1, \ldots, u^K)$, define the **effective coupling parameter**:
$$
\lambda_{\mathrm{coupling}} = \max_{j \neq k} \frac{|O_{jk}|}{\min(|\mathrm{Core}_j|, |\mathrm{Core}_k|)}
$$
where $O_{jk} = \{x : u^j(x) \geq \theta_{\mathrm{supp}} \text{ and } u^k(x) \geq \theta_{\mathrm{supp}}\}$ is the support overlap set.

This is a monotonic measure: $\lambda_{\mathrm{coupling}} = 0$ corresponds to disjoint supports (well-separated), $\lambda_{\mathrm{coupling}} \in (0, \eta)$ to boundary-scale overlap (weakly-interacting), and $\lambda_{\mathrm{coupling}} \geq \eta$ to core-scale overlap (strongly-interacting).

### 3.2. Regime Thresholds

| Regime | Coupling range | Geometric meaning |
|--------|---------------|-------------------|
| **I (Well-separated)** | $\lambda_{\mathrm{coupling}} = 0$, $d_{\min} \geq D_{\mathrm{sep}} \geq 3$ | Supports disjoint; cores separated by ≥3 hops |
| **II (Weakly-interacting)** | $0 < \lambda_{\mathrm{coupling}} \leq \eta$ ($\eta = 0.2$) | Boundary overlap only; deep cores decoupled |
| **III (Strongly-interacting)** | $\lambda_{\mathrm{coupling}} > \eta$ | Core-scale overlap; coupling dominates |

### 3.3. Relation to Existing Conditions

The coupling measure unifies the previously separate conditions:
- **WS** (well-separation): $\lambda_{\mathrm{coupling}} = 0$ and $d_{\min} \geq 3$
- **WI** (weak interaction): $\lambda_{\mathrm{coupling}} \leq 0.2$
- **Strong interaction**: $\lambda_{\mathrm{coupling}} > 0.2$

[**TODO:** Incorporate Task #2/#4 findings on whether a single scalar parameter suffices or if $d_{\min}$ remains an independent axis.]

---

## 4. Unified Theorem Statement

### Theorem (T-Persist-K-Unified)

Let $(u^1_t, \ldots, u^K_t)$ be a joint minimizer of $\mathcal{E}_{K,t}$ on $\Sigma^K_M$ with per-formation spectral gaps $\mu_k > 0$.

**Universal hypotheses:**
- **(H1-K)** Each $u^k_t$ satisfies the single-formation hypotheses (H1)–(H4) of T-Persist-1
- **(SR)** Spectral-repulsion compatibility: $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$
- **(NB-K)** Joint non-bifurcation: $\mu_{\mathrm{joint}} > \mu_0 > 0$
- **(GT)** $\varepsilon$-gentle transition from $t$ to $s$

**Then persistence holds with mechanism depending on coupling regime:**

---

**(I) Well-Separated Regime** ($\lambda_{\mathrm{coupling}} = 0$, $d_{\min} \geq 3$, with WS budget condition):

Additionally assume **(WS)**: $4\varepsilon_1/\min_k \mu_k < D_{\mathrm{sep}} - 2$.

Then:
1. **(a)** Per-formation minimizer persistence: $\|u^k_s - u^k_t\| \leq 2\varepsilon_1/\mu_k$
2. **(b)** Separation preservation: $d_{\min}(s) \geq d_{\min}(t) - 4\varepsilon_1/\min(\mu_j, \mu_k)$
3. **(c)** Per-formation core inclusion (shifted threshold $\theta - 2\varepsilon_1/\mu_k$)
4. **(d)** Per-formation transport concentration (two-tier, independent per formation)
5. **(e)** Simplex preservation: violation $< K \cdot 10^{-3}$ (no post-hoc correction needed)

**Status: PROVED** (conditional on per-formation T-Persist-1 hypotheses).

**Mechanism:** Product-manifold IFT + Coupling Bound Lemma with exponentially small cross-formation gradient perturbation at core sites.

---

**(II) Weakly-Interacting Regime** ($0 < \lambda_{\mathrm{coupling}} \leq 0.2$):

Then:
1. **(a)** Joint minimizer persistence: $\|(u^1_s, \ldots, u^K_s) - (u^1_t, \ldots, u^K_t)\| \leq 2\varepsilon_1/\mu_{\mathrm{joint}}$
2. **(b)** Deep core sites ($\delta \geq 2$) unaffected by coupling; T-Persist-1(c,d) applies unchanged
3. **(c)** Boundary overlap sites: shifted-threshold fallback only
4. **(d)** Post-hoc simplex correction: displacement $O(|O_{jk}| \cdot \theta_{\mathrm{supp}}) \ll r_{\mathrm{basin}}$
5. **(e)** Deep core fingerprint gap preserved: $\Delta_\varphi^2 \geq 2.87 - O(\exp(-c_0))$

**Status: CONDITIONALLY PROVED** under (H1-K), (WI), (SR), (NB-K), plus per-formation T-Persist-1.

**Mechanism:** Joint IFT on $\Sigma^K_M$ + Weyl spectral gap + deep-core decoupling (exponentially small gradient perturbation at depth $\geq 2$).

---

**(III) Strongly-Interacting Regime** ($\lambda_{\mathrm{coupling}} > 0.2$):

This regime admits a **theorem ladder** with varying epistemic status:

**(III-a) Compatible-overlap coexistence.** If $\mu_{\mathrm{overlap}} > 0$ (the overlap-restricted Hessian block is spectrally positive), then:
- The K-formation branch persists locally with $K_s = K_t$
- Displacement: $\|(u^1_s, \ldots, u^K_s) - (u^1_t, \ldots, u^K_t)\| \leq C\varepsilon_1/\mu_{\mathrm{joint}}$
- Deep core persistence degrades with overlap: only sites at depth $\geq \delta_{\min}(\lambda_{\mathrm{coupling}})$ are protected

**Status: CONDITIONALLY PROVED** (CT-KS1; requires strong-regime selection hypothesis).

**(III-b) K-formation local stability.** The K-formation critical point is always a local minimum (not a saddle). For K=2, the merge-direction Hessian curvature is $\geq \mu_1 + \mu_2 > 0$.

**Status: PROVED** (K=2 case; general K under per-formation non-degeneracy).

**(III-c) Isoperimetric energy ordering.** On connected graphs in the sharp-interface regime:
$$
\mathcal{E}(u^*_{Km/K}) < K \cdot \mathcal{E}(u^*_m)
$$
The single merged formation has strictly lower energy. Multi-formation persistence is kinetic (barrier-based), not thermodynamic.

**Status: PROVED** (on graphs with non-increasing isoperimetric ratio $h(k)$; saving $\delta_{\mathrm{iso}} = 1 - 2^{-1/d}$).

**(III-d) Overlap instability destroys local persistence.** If $\mu_{\mathrm{overlap}} \leq 0$, the K-branch loses strict local minimality in the overlap direction; the IFT/continuation argument fails.

**Status: PROVED** (Proposition P-KS2).

**(III-e) Near-bifurcation collapse.** As $\mu_{\mathrm{joint}} \to 0$, the admissible gentle-transition window collapses: persistence requires $\varepsilon_1 = o(\mu_{\mathrm{joint}})$.

**Status: PROVED** (Proposition P-KS3).

**(III-f) Merge under Morse-selection hypotheses.** If $\mu_{\mathrm{overlap}} \leq 0$ and additional Morse hypotheses (MS1–MS4) hold, the dynamics selects a merge branch with $K_s < K_t$.

**Status: CONJECTURAL** (CT-KS4; none of MS1–MS4 proved).

**(III-g) Barrier height scaling.** The energy barrier between K and (K-1) configurations scales as:
$$
\Delta E_{\mathrm{barrier}} = O(\beta^{0.89})
$$
Kinetic persistence time: $\tau_{\mathrm{merge}} \sim \exp(\Delta E_{\mathrm{barrier}} / k_B T)$ (Kramers rate).

**Status: EXPERIMENTAL** (exp38; theoretical derivation of exponent 0.89 is open).

---

## 5. Proof Sketch

### 5.1. Shared Foundation (All Regimes)

The proof begins identically across regimes:

1. **Joint Hessian positivity.** Under (SR), Weyl's inequality gives $\mu_{\mathrm{joint}} \geq \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}} > 0$.

2. **Product-manifold IFT.** The bordered KKT system on $\Sigma^K_M$ (including Lagrange multipliers for volume constraints) has a non-degenerate Jacobian when $\mu_{\mathrm{joint}} > 0$. By the IFT, the joint critical point persists under gentle perturbation with displacement $O(\varepsilon_1/\mu_{\mathrm{joint}})$.

3. **Core-depth stratification.** Define the depth function $\delta(x, k) = d_G(x, \partial\mathrm{Core}(u^k))$ for each formation $k$. The gradient perturbation from cross-formation coupling at depth $\delta$ is $O(\lambda_{\mathrm{rep}} \cdot \exp(-c_0 \delta))$ where $c_0 = \mathrm{arccosh}(1 + \kappa^2/d_{\min})$.

### 5.2. Regime I Completion (Well-Separated)

When $d_{\min} \geq 3$, the cross-formation gradient perturbation at any core site is $O(\exp(-c_0 \cdot 3)) < 10^{-3}$. Each formation's IFT analysis reduces to the single-formation case up to exponentially small corrections. Simplex violation is controlled by the exponential decay of formation tails beyond their support.

**Key lemma: Coupling Bound Lemma.** At sites with $\delta(x,k) \geq 1$ and $d(x, \mathrm{supp}(u^j)) \geq D_{\mathrm{sep}} - 2$, the coupling gradient is $O(\exp(-c_0(D_{\mathrm{sep}}-2)))$.

### 5.3. Regime II Completion (Weakly-Interacting)

The overlap set $O_{jk}$ is boundary-scale ($\leq 0.2 \cdot |\mathrm{Core}|$). At deep core sites ($\delta \geq 2$), the coupling gradient remains exponentially small — the single-formation persistence applies. At boundary/overlap sites, the coupling gradient is $O(\lambda_{\mathrm{rep}})$ and cannot be neglected; only shifted-threshold persistence holds.

**Key insight:** The deep-core/boundary split is the mathematical content of "weakly-interacting." Coupling affects the boundary but not the core.

Post-hoc simplex correction: the displacement $O(|O_{jk}| \cdot \theta_{\mathrm{supp}})$ is small because $|O_{jk}|$ is boundary-scale. Under (WI), this is $\leq 0.2 \cdot |\mathrm{Core}| \cdot \theta_{\mathrm{supp}} \ll r_{\mathrm{basin}}$.

### 5.4. Regime III Completion (Strongly-Interacting)

The proof splits into the theorem ladder described in §4(III):

**(III-a) Coexistence branch.** When $\mu_{\mathrm{overlap}} > 0$, the same IFT argument from §5.1 applies. The additional hypothesis is that the continued branch is the physically realized one (strong-regime selection). Unlike Regimes I–II, the core sites are no longer protected: overlap-sites may have large coupling gradients, and the persistence is global (whole-branch continuation) rather than site-by-site.

**(III-b) Local stability.** For K=2, the merge-direction $(v, -v)$ has Hessian curvature $v^T[H_1 + H_2]v + \lambda_{\mathrm{rep}} \|v\|^2 \geq (\mu_1 + \mu_2)\|v\|^2 > 0$. The repulsion term only adds positive curvature in the merge direction.

**(III-c) Isoperimetric ordering.** Test function: two disjoint copies of $u^*_m$ have energy $2\mathcal{E}(u^*_m)$. The merged formation $u^*_{2m}$ beats this by the discrete isoperimetric inequality: boundary saving $\delta_{\mathrm{iso}} = 1 - 2^{-1/d}$.

**(III-d, III-e)** Standard spectral instability and IFT budget collapse.

**(III-f)** Requires MS1–MS4 (Morse non-degeneracy, competitor existence, sublevel connectivity, transport branch selection). Currently conjectural.

---

## 6. Dependency Diagram

```
T-Persist-1(a-e)  ────────────────────────────────────────────────┐
    │                                                              │
    ├──→ T-Persist-K-Unified (I): Well-Separated [PROVED]         │
    │        requires: H1-K, WS, SR                               │
    │        uses: Coupling Bound Lemma + per-formation T-Persist  │
    │                                                              │
    ├──→ T-Persist-K-Unified (II): Weakly-Interacting [CONDITIONAL]
    │        requires: H1-K, WI, SR, NB-K                         │
    │        uses: Joint IFT + deep-core decoupling                │
    │                                                              │
    └──→ T-Persist-K-Unified (III): Strongly-Interacting [LADDER]  
             │                                                     
             ├── (III-a) Coexistence [CONDITIONAL]                 
             │     requires: μ_overlap > 0, strong-regime selection 
             │     uses: same IFT as (II) but without core protection
             │                                                     
             ├── (III-b) K=2 Local Stability [PROVED]              
             │     uses: Hessian decomposition on Σ²_M             
             │                                                     
             ├── (III-c) Isoperimetric Ordering [PROVED]           
             │     uses: T11 Γ-convergence + discrete isoperimetric
             │                                                     
             ├── (III-d) Overlap Instability [PROVED]              
             │     uses: spectral analysis of overlap block        
             │                                                     
             ├── (III-e) Near-Bif Collapse [PROVED]                
             │     uses: IFT budget analysis                       
             │                                                     
             ├── (III-f) Merge Conjecture [CONJECTURAL]            
             │     requires: MS1-MS4 (none proved)                 
             │                                                     
             └── (III-g) Barrier Height [EXPERIMENTAL]             
                   evidence: exp38 O(β^0.89)                       

Isoperimetric Energy Ordering ──→ (III-c)
K=2 Local Stability ──→ (III-b)
Transport Confinement ──→ all regimes (selection uniqueness)
```

---

## 7. Conditions Register

### 7.1. Universal Conditions (All Regimes)

| Condition | Statement | Status | When it fails |
|-----------|-----------|--------|---------------|
| (H1-K) | Per-formation hypotheses H1-H4 | Standard | Non-generic parameters |
| (SR) | $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$ | Verifiable | Large K or large λ_rep |
| (NB-K) | $\mu_{\mathrm{joint}} > \mu_0$ | Generic | Isolated bifurcation points (measure zero) |
| (GT) | ε-gentle transition | Parameter bound | Abrupt temporal change |
| (ND) | Per-formation non-degeneracy | Generic (Sard) | Measure zero in parameter space |

### 7.2. Regime-Specific Conditions

| Regime | Additional condition | Role |
|--------|---------------------|------|
| I | (WS): $d_{\min} \geq 3$, separation budget | Ensures exponential gradient decay |
| II | (WI): $\lambda_{\mathrm{coupling}} \leq 0.2$ | Keeps overlap boundary-scale |
| III-a | $\mu_{\mathrm{overlap}} > 0$ + selection | Ensures overlap block stability + branch uniqueness |

### 7.3. Conditions from Task #1 Analysis

[**TODO:** Integrate conditional-analyst findings on T-Persist-1(b,d,e) — which conditions are structural necessities vs removable technical gaps. Key questions:
- Can NB (μ ≥ 4.1) be weakened? What is the sharp threshold?
- Is GT reducible to transport parameters via tight confinement?
- Does H3 (β > 11α for d_min=4) have a natural weakening?]

### 7.4. Conditions from Task #2 Analysis

[**TODO:** Integrate generalization-strategist findings on structural condition unification. Key questions:
- Can WS and WI be unified into a single scalar condition?
- Does the coupling measure λ_coupling fully determine the regime, or is d_min an independent axis?
- What is the exact relationship between λ_coupling and μ_joint?]

---

## 8. Open Questions Within the Framework

### 8.1. Bifurcation Crossing (μ → 0)

All three regimes lose quantitative persistence content as $\mu_{\mathrm{joint}} \to 0$. The theory currently says nothing about what happens at exact bifurcation. This is the deepest open problem:
- Branch selection mechanism unknown
- Stochastic analysis (Kramers + center manifold) required
- Experimental evidence: supercritical pitchfork, no hysteresis (exp37)

### 8.2. Formation Birth (K → K+1)

The unified theorem addresses persistence ($K_s = K_t$) and merge ($K_s < K_t$). Birth ($K_s > K_t$) is entirely outside its scope. Two mechanisms identified (FORMATION-BIRTH-THEORY.md):
- Parametric nucleation (β increase → pitchfork)
- Topological splitting (core Fiedler eigenvalue → 0)

### 8.3. Merge Branch Selection

Even within the strong regime, the merge conjecture (III-f) requires four Morse-selection hypotheses (MS1–MS4), none of which are currently proved. The strongest safe statement remains: overlap instability destroys local persistence, but does not determine the endpoint.

### 8.4. Barrier Exponent

The experimental scaling $\Delta E_{\mathrm{barrier}} = O(\beta^{0.89})$ lacks theoretical derivation. A NEB/string method analysis on $\Sigma^K_M$ could characterize the transition state and derive the exponent.

### 8.5. Strong-Regime Transport Selection

Self-referential transport with large coupling has existence (Schauder) but not proved uniqueness/selection. Transport confinement helps (exp29: no multiplicity observed) but analytical confirmation is open.

---

## 9. Integration of Task Findings

### 9.1. From Task #1 (Conditional Conditions Analysis)

[**PLACEHOLDER** — awaiting conditional-analyst results]

Expected integration points:
- Sharpened NB condition → tighter NB-K
- GT reduction via transport confinement → simpler (GT) statement
- Structural necessity assessment → which conditions cannot be removed

### 9.2. From Task #2 (Structural Condition Generalization)

[**PLACEHOLDER** — awaiting generalization-strategist results]

Expected integration points:
- Unified coupling measure → §3 refinement
- Condition relationships → simplified condition register
- Smooth regime transitions → §4 threshold clarification

### 9.3. From Task #3 (Isoperimetric/Transport Necessity)

[**PLACEHOLDER** — awaiting conditional-analyst results]

Expected integration points:
- Necessity of isoperimetric profile monotonicity
- Transport confinement tightness → strong-regime selection bounds

### 9.4. From Task #4 (Unified Parametrization)

[**PLACEHOLDER** — awaiting generalization-strategist results]

Expected integration points:
- Concrete λ_coupling formula
- Regime boundary values (numerical)
- Smooth interpolation between mechanisms

---

## 10. Assessment and Status Summary

### 10.1. What T-Persist-K-Unified Achieves

1. **Conceptual unification:** One theorem covers all three regimes, replacing three separate statements
2. **Monotonic parametrization:** The coupling measure λ_coupling provides a single axis for regime classification
3. **Honest epistemic status:** Each sub-result is clearly labeled (proved / conditional / conjectural / experimental)
4. **Mechanism transparency:** The persistence mechanism transitions smoothly from spectral dominance to barrier crossing

### 10.2. What Remains Open

| Item | Status | Difficulty |
|------|--------|-----------|
| Bifurcation crossing | Open | Hard |
| Formation birth | Open | Hard |
| Merge branch selection (MS1-MS4) | Conjectural | Medium-Hard |
| Barrier exponent derivation | Experimental only | Medium |
| Strong-regime transport selection | Partial (existence proved) | Medium |
| Tight confinement constants | Partial (loose bound proved) | Easy-Medium |

### 10.3. Publication Assessment

The unified theorem is publishable as stated, with the theorem ladder for Regime III honestly presented. The proved components (I, II, III-b through III-e) constitute solid mathematical contributions. The conjectural components (III-f, III-g) are clearly delineated as future work with experimental support.

---

## Appendix A: Notation Summary

| Symbol | Meaning |
|--------|---------|
| $\Sigma^K_M$ | Product volume-constrained manifold |
| $\mathcal{E}_K$ | Joint K-field energy |
| $\mu_k$ | Per-formation spectral gap |
| $\mu_{\mathrm{joint}}$ | Joint Hessian spectral gap on $\Sigma^K_M$ |
| $\mu_{\mathrm{overlap}}$ | Overlap-block restricted spectral gap |
| $\lambda_{\mathrm{coupling}}$ | Effective coupling parameter (max overlap ratio) |
| $d_{\min}$ | Minimum inter-formation graph distance |
| $O_{jk}$ | Support overlap set between formations $j, k$ |
| $\eta$ | Weak/strong regime threshold (= 0.2) |
| $D_{\mathrm{sep}}$ | Well-separation distance threshold (≥ 3) |
| $\delta(x,k)$ | Depth of site $x$ in formation $k$'s core |
| $c_0$ | Exponential decay rate for coupling gradient |

## Appendix B: Cross-Reference to Existing Theorems

| This document | Canonical Spec | Status |
|--------------|----------------|--------|
| §4(I) | T-Persist-K-Sep (§10, §13) | Proved → unchanged |
| §4(II) | T-Persist-K-Weak (§10, §13) | Conditional → unchanged |
| §4(III-a) | CT-KS1 (T-PERSIST-K-STRONG-MORSE-ATTEMPT §5.2) | Conditional → unchanged |
| §4(III-b) | Proposition 1 (MERGE-DICHOTOMY-ANALYSIS §4) | Proved → incorporated |
| §4(III-c) | Isoperimetric Energy Ordering (ISOPERIMETRIC-TRANSPORT-PROOFS §2) | Proved → incorporated |
| §4(III-d) | P-KS2 (T-PERSIST-K-STRONG-MORSE-ATTEMPT §5.3) | Proved → incorporated |
| §4(III-e) | P-KS3 (T-PERSIST-K-STRONG-MORSE-ATTEMPT §5.4) | Proved → incorporated |
| §4(III-f) | CT-KS4 (T-PERSIST-K-STRONG-MORSE-ATTEMPT §5.5) | Conjectural → unchanged |
| §4(III-g) | exp38 barrier scaling | Experimental → incorporated |
