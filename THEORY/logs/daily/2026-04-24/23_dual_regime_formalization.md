# 23_dual_regime_formalization.md — Dual-Regime SCC: Mathematical Formalization (Phase A)

**Session:** 2026-04-24 (very late night, post-C3-family)
**Purpose:** 사용자 요청 — "이중구조를 명확히 조사하고 검증하며 수학적으로 제대로 정의하라".
**Phase:** A (formalization); Phase B (experiment) + Phase C (synthesis) 가 후속.
**Depends on:** 본 세션 `21_C3T_results_theorem1_regime.md` (regime discovery), `22_C3_family_final.md`, `canonical.md` Cor 2.2.

---

## §1. Discovery recap — empirical basis of dual-regime

본 세션 여러 experiment 에서 일관되게 관찰:
- **Canonical SCC** ($\beta = 30$, $\alpha = 1$): $\xi_0 = 0.183$, $a = 1$, $\xi_0/a = 0.183$
- **G1 L=16 free-BC center disk**: $\lambda_0 = 25.27$ (orbital scale, NOT Goldstone)
- **C3-T L=12, 16 torus F=1**: $\lambda_0 \approx 24$ (orbital scale)
- **NQ-138 $D_4$ mixing scan**: no clean $(\xi_0/r_0)^k$ scaling; splittings $O(1)$ intrinsic
- All consistent: **no Goldstone in $\xi_0 < a$**

**Contrast**: continuum PN theory predicts $\lambda_0 \sim \exp(-c r_0/\xi_0) \to 0$. Breaks down at sub-lattice.

**Hypothesis**: Two distinct regimes with qualitative transition at $\xi_0 / a = O(1)$.

---

## §2. Definitions

### 2.1 Lattice spacing and regime parameter

> **Definition 2.1 (Lattice spacing).** For a graph $G = (X, E)$ embedded in metric space (physical graph, e.g. $\mathbb{Z}^2$), the **lattice spacing** $a$ is the nearest-neighbor distance. For unit $\mathbb{Z}^2$ grid or torus $(\mathbb{Z}/L)^2$: $a = 1$.

> **Definition 2.2 (Interface width).** With canonical parameters $(\alpha, \beta, c)$, the **interface width** $\xi_0 = \sqrt{\alpha/\beta}$ from Cor 2.2 quantitative.

> **Definition 2.3 (Regime parameter $\zeta$).**
> $$\zeta := \frac{\xi_0}{a} = \frac{\sqrt{\alpha/\beta}}{a}.$$
> $\zeta$ is dimensionless, independent of graph size $L$ or mass $m$.

### 2.2 Regime classification

> **Definition 2.4 (Regime classification).**
> - **Sub-lattice regime**: $\zeta < \zeta_*^\text{sub}$ for some threshold $\zeta_*^\text{sub} \in (0, 1)$.
> - **Super-lattice regime**: $\zeta > \zeta_*^\text{super}$ for some threshold $\zeta_*^\text{super} \in (1, 2)$.
> - **Crossover regime**: $\zeta \in [\zeta_*^\text{sub}, \zeta_*^\text{super}]$ (transition).
>
> Thresholds $\zeta_*^\text{sub}, \zeta_*^\text{super}$ are empirically determined; theoretical prediction $\zeta_*^\text{sub} \approx \zeta_*^\text{super} \approx 1$ (sharp transition hypothesis).

### 2.3 Physical interpretation

- **Sub-lattice** ($\zeta \ll 1$): interface narrower than 1 lattice spacing → binary sharp profile. Disk is a set of lattice sites with $u \approx 1$ interior and $u \approx 0$ exterior; interface is 1-cell-thick.
- **Super-lattice** ($\zeta \gg 1$): interface spans many lattice sites → smooth profile. Disk has continuous-like transition.
- **Crossover** ($\zeta \sim 1$): interface approximately 1 lattice thick.

---

## §3. Dual-Regime Spectrum Theorem (central statement)

### 3.1 Formal statement

> **Theorem (Dual-Regime Spectrum, 2026-04-24 formalization):** 
> Let $G$ be a finite connected graph with lattice spacing $a$. Let $u^*$ be a Morse-0 local minimum of pure $\mathcal{E}_\text{bd}$ on $\Sigma_m$ with $\mathcal{F}(u^*) = 1$, boundary distance $d_* \geq L/4$. Let $H = H(u^*)$ be the constrained Hessian on $\mathbf{1}^\perp$, with lowest non-tangent eigenvalue $\lambda_0(u^*)$.
>
> (A) **Sub-lattice regime** ($\zeta < \zeta_*^\text{sub}$, $\zeta_*^\text{sub} \approx 1$):
> $$\lambda_0(u^*) \geq c_A \cdot \beta$$
> for constant $c_A > 0$ depending on $c, \alpha, L$. Low-lying spectrum is **genuine orbital band**: eigenvalues $\{\lambda_k\}_{k=0}^{\text{cutoff}}$ clustered in $[\lambda_0, \lambda_0 + \Delta\lambda_\text{band}]$ with $\Delta\lambda_\text{band}/\lambda_0 = O(\xi_0^2/r_0^2)$.
>
> (B) **Super-lattice regime** ($\zeta > \zeta_*^\text{super}$, $\zeta_*^\text{super} \approx 1$):
> $$\lambda_0(u^*) \leq c_B \cdot e^{-\kappa r_0 / \xi_0}$$
> for constants $c_B, \kappa > 0$. Low-lying spectrum has **Goldstone band** (translation pseudo-Goldstone) separated from orbital band by gap $\Delta_\text{Gold-orb} \sim \beta$.
>
> (C) **Crossover regime** ($\zeta \in (\zeta_*^\text{sub}, \zeta_*^\text{super})$): continuous transition. $\lambda_0(\zeta)$ decreases rapidly (plausibly exponentially) through the crossover.

### 3.2 Cat assignments (pre-experimental)

- **(A) Sub-lattice**: **Cat A** empirical (본 세션 multiple confirmation). Rigorous proof = Cat B (analytic lower bound $c_A$).
- **(B) Super-lattice**: **Cat C conjecture**. Based on continuum PN physics extrapolation. Needs dedicated experiment.
- **(C) Crossover**: **Cat C**. ζ-scan experiment 필요.

---

## §4. Supporting lemmas

### 4.1 Sub-lattice disk structure

> **Lemma 4.1 (Binary profile in sub-lattice).** For $\zeta \ll 1$, the minimizer $u^*$ of pure $\mathcal{E}_\text{bd}$ satisfies:
> - $u^*(i) \in \{0 + O(e^{-1/\zeta}), 1 + O(e^{-1/\zeta})\}$ for all "interior" or "exterior" $i$
> - Number of interface sites $\mathcal{I} = \{i : u^*(i) \in (\varepsilon, 1-\varepsilon)\}$ for small $\varepsilon$: $|\mathcal{I}| = O(P(\text{disk}))$ where $P$ is perimeter.

**Proof sketch**: $\xi_0 < a$ means double-well $W(u)$ 의 near-$0, 1$ attractors 지배. Interface energy $\propto \xi_0$ vs bulk interior/exterior energy → interface sites minimize by choosing nearest ($0$ or $1$). 정확한 bound $O(e^{-1/\zeta})$ 는 Allen-Cahn sharp-interface Γ-convergence 의 discrete analog.

**Cat B** for precise constants.

### 4.2 Super-lattice continuum approximation

> **Lemma 4.2 (Continuum emergence).** For $\zeta \gg 1$, the disk minimizer $u^*$ admits continuum representation $u^*(x, y) \approx \frac{1}{2}(1 - \tanh((r - r_0)/\xi_0))$ up to lattice correction $O((a/\xi_0)^2)$.

**Proof sketch**: Modica-Mortola Γ-convergence (Cat A canonical Cor 2.2 qualitative) 의 standard statement, discrete-to-continuum lattice correction.

**Cat A** for the continuum limit (Cor 2.2 canonical); lattice correction **Cat B**.

### 4.3 Peierls-Nabarro barrier estimate

> **Lemma 4.3 (PN barrier in super-lattice).** For $\zeta \gg 1$ and disk on torus $T_L$ with $r_0 \gg \xi_0$:
> $$\lambda_0^\text{PN} \approx A \cdot \beta \cdot e^{-\pi^2 r_0 / \xi_0}$$
> for constant $A$ depending on disk profile. As $\zeta \to \infty$, the disk becomes continuum-like and PN barrier vanishes.

**Proof sketch**: Frenkel-Kontorova / sine-Gordon kink discrete PN formula applied to disk interface. Standard reference: Braun-Kivshar "Frenkel-Kontorova Model" (2004) §1.2.

**Cat C** (sketched, needs formal derivation in SCC context).

### 4.4 Sub-lattice rigidity

> **Lemma 4.4 (Pinning rigidity).** For $\zeta < \zeta_*^\text{sub}$, the minimum translation step $u^* \mapsto \tau u^*$ on discrete graph requires energy $\geq E_\text{pin} = O(\beta)$ per lattice step.

**Proof sketch**: Binary profile (Lemma 4.1) 에서 translation 이 "flip" 을 수반 — 한 interior site 를 exterior 로 (or vice versa), 비용 $\approx \beta \cdot |W(1) - W(0)| + \text{boundary}$. Since $W(0) = W(1) = 0$ exactly, cost comes from interface reconfiguration $\sim \beta \cdot O(1)$.

**Cat B** for precise constants.

---

## §5. Regime-specific σ-signature

σ-framework (Axiom S1' v1) 의 regime-specific refinement:

### 5.1 Sub-lattice σ structure

> **Proposition 5.1 (σ signature in sub-lattice):** For $\zeta < \zeta_*^\text{sub}$:
> - $\mathcal{F}$ 가 discrete integer (strict-max convention, Cat A via NQ-143)
> - $\{(n_k, [\rho_k], \lambda_k)\}$: all $\lambda_k = O(\beta)$, $[\rho_k]$ full spectrum of $S(u^*)$ irreps
> - **No degenerate Goldstone band** in spectrum
> - Nodal count $n_k$ discrete well-defined

### 5.2 Super-lattice σ structure

> **Proposition 5.2 (σ signature in super-lattice):** For $\zeta > \zeta_*^\text{super}$:
> - $\mathcal{F} = 1$ stable with "soft" Goldstone band (near-zero modes)
> - $\{(n_k, [\rho_k], \lambda_k)\}$: lowest 2 modes ($k = 0, 1$) with $\lambda \approx 0$ (Goldstone doublet for 2D translation)
> - **Goldstone band + orbital band** separation visible
> - $(n_0, n_1)$ = Goldstone nodal count $(2, 2)$, irrep $[\rho_0] = [\rho_1] = E$ of $D_4$ (on free-BC center) or exact translation irrep (on torus)

### 5.3 σ regime-dependent interpretation

σ framework 자체는 regime-independent (definition 변화 없음). **Interpretation 이 regime-specific**:
- Sub-lattice: σ 의 component 가 "rigid orbital modes" 표현
- Super-lattice: σ 의 일부 component 가 "mobile Goldstone modes" (translation)

---

## §6. Threshold $\zeta_*$ 의 이론적 예측

### 6.1 Frenkel-Kontorova analogy

Frenkel-Kontorova model 에서 commensurate-incommensurate transition 은 $\zeta \sim 1$ 에서 발생:
- $\zeta < 1$ (commensurate): soliton pinned to lattice
- $\zeta > 1$ (incommensurate): soliton mobile

이 analogy 로 SCC 도 $\zeta_* \approx 1$ 예상.

### 6.2 Predicted sharp transition

> **Conjecture (Sharp dual-regime transition):** $\zeta_*^\text{sub} = \zeta_*^\text{super} = 1$ exactly (up to graph-class finite-size correction $O(1/L)$).

**Rationale**:
- $\zeta < 1$: interface width $<$ lattice spacing → discrete PN dominates
- $\zeta > 1$: interface $>$ lattice spacing → continuum emerges
- Transition at $\zeta = 1$ (interface-width = 1 lattice step)

**Cat C conjecture**, verified by Phase B experiment.

### 6.3 Numerical scan plan

Phase B experiment design (다음 파일 `24_*.py` 또는 `25_*.md`):
- Fix $L = 16$, $c = 0.5$, $\alpha = 1$
- Vary $\beta$ such that $\zeta \in \{0.18, 0.3, 0.5, 0.8, 1.0, 1.3, 1.8, 2.4\}$
  - β values: 30, 11.1, 4.0, 1.56, 1.0, 0.59, 0.31, 0.17
- For each, find F=1 center disk minimizer
- Compute Hessian spectrum, extract $\lambda_0, \lambda_1, \lambda_2$
- Plot $\lambda_0(\zeta)$ and $\lambda_0/\lambda_2$ ratio

**Expected**: Sharp drop in $\lambda_0$ near $\zeta = 1$.

---

## §7. Canonical 문서와의 연계

### 7.1 Canonical Cor 2.2 확장

현재 Cor 2.2 quantitative 에는 **continuum (super-lattice) case 만** 명시. Dual-regime framework 하에서:

> **Cor 2.2 revised (dual-regime):** Pure $\mathcal{E}_\text{bd}$ disk minimizer interface width scales as $\xi_0 = \sqrt{\alpha/\beta}$:
> - Super-lattice ($\zeta > 1$): Smooth tanh profile $u^*(r) = \tfrac{1}{2}(1 - \tanh((r-r_0)/\xi_0))$ with continuum Γ-limit as $\zeta \to \infty$
> - Sub-lattice ($\zeta < 1$): Binary lattice profile $u^*(i) \in \{0, 1\}$ with interface confined to single-cell thickness; tanh approximation NOT valid.

**Stage 6 weekly merge 후보**: canonical Cor 2.2 에 dual-regime 명시.

### 7.2 T-Birth-Parametric + dual-regime

T-Birth-Parametric (canonical Cat A) 은 uniform → non-uniform first pitchfork. 이 분기 자체는 regime-independent (T8-Core condition $\beta > \beta_\text{crit}^{(2)}$ 는 Fiedler-based, regime 무관). 단 **post-bifurcation minimizer** 의 character 가 regime 에 따라 다름:
- Sub-lattice: binary disk
- Super-lattice: smooth tanh disk

### 7.3 Axiom S1' v1 + dual-regime

Axiom S1' v1 은 regime-independent. $\zeta$ parameter 를 σ tuple 에 explicit 추가 가능:
$$\sigma(u^*) = (\mathcal{F}(u^*); \zeta, \{(n_k, [\rho_k], \lambda_k)\}_k)$$
또는 $\zeta$ 를 context variable 로 assumed.

---

## §8. Sub-lattice vs super-lattice 의 ontological implication

### 8.1 Two "pre-objective physics"

**Sub-lattice SCC**:
- Rigid, lattice-pinned formations
- Binary profiles, discrete configuration space
- Pre-objective = "set of lattice sites with cohesion" (near-crisp)
- R23 empirical domain

**Super-lattice SCC**:
- Mobile, continuum-like formations
- Smooth profiles, nearly continuous configuration space
- Pre-objective = "smooth graded field, translationally mobile"
- Continuum limit, PDE regime

### 8.2 SCC pre-objective 의 regime-dependence

Canonical §2 commitment 1 ("soft cohesion primitive") 이 두 regime 에서 다른 manifestation:

- **Sub-lattice**: Softness 가 proto-cohesion diagnostic **$\mathbf{d} = (\text{Bind, Sep, Inside, Persist})$** 의 continuity 에서 유지 (필드는 binary 하지만 diagnostic 이 graded). **"Crisp-like 필드, graded diagnostic"**.
- **Super-lattice**: Softness 가 필드 자체 의 continuum smoothness 에서 유지. **"Graded 필드, graded diagnostic"**.

두 regime 모두 SCC의 pre-objective commitment 를 만족하지만 서로 다른 방식. 이것이 **SCC 의 ontological flexibility** — 하나의 framework 가 두 개의 distinct physics 를 수용.

### 8.3 σ-framework 의 dual-regime 통일

σ-signature 는 **양 regime 의 공통 언어**. Discrete (F), spectral (λ, n_k), group-theoretic ([ρ_k]) 모두 regime-independent. σ 를 통해 두 regime 을 compare + transition study 가능.

이것이 σ-framework 의 **universal 성** 의 근거: 단순히 R23 regime 분류 도구가 아니라 **두 regime 을 잇는 bridge**.

---

## §9. Phase A 정리 — formalization 의 핵심

**정의된 것**:
- $\zeta = \xi_0/a$ regime parameter
- Sub-lattice / super-lattice / crossover 3 regime
- Dual-Regime Spectrum Theorem 상태 (Cat A/B/C 분류)
- Regime-specific σ interpretation

**예측 (Cat C conjecture, Phase B 검증 대상)**:
- $\zeta_* \approx 1$ sharp transition
- $\lambda_0(\zeta)$ 가 $\zeta = 1$ 근처에서 급격히 떨어짐
- 2D 에서 Goldstone doublet emerge at $\zeta > 1$

**연계된 canonical items**:
- Cor 2.2 (regime-specific extension 필요)
- T-Birth-Parametric (regime-independent)
- Axiom S1' v1 (regime-independent definition, interpretation regime-dep)
- Commitment 1 (pre-objective, regime-dep manifestation)

---

## §10. Phase B experiment 즉시 필요

다음 파일: **`24_dual_regime_zeta_scan.py`** (script), **`25_dual_regime_results.md`** (analysis).

실험 design 은 §6.3 에 명시. 예상 runtime ~5-10 분 (ζ scan × 8 values × Hessian computation at L=16). 매우 가볍.

**Phase B** 진행 가능.

---

**End of 23_dual_regime_formalization.md. Phase A complete. Proceed to Phase B immediately.**
