# 03_integration_and_new_open.md — Integration with Canonical, A-01 Revision, CN Sharpening, New Open Questions

**Session:** 2026-04-24
**Target (from plan.md):** σ-signature 정의·정리의 canonical 통합 + 기존 OP 와의 관계 + 새 open question 수집.
**This file covers:** §4.5 Integration + §4.6 New open questions. Plus prompt template feedback.
**Depends on reading:** 본 세션 `01_exploration.md`, `02_development.md`; `canonical.md` §6 (axiom groups), §11 (commitments), §12 (open problems), §13 (theorem catalog), §14 (CN1–CN14); `working/SF/symmetry_moduli.md` §3.7 (G-D); `working/canonical_drafts/` (현재 비어있음).

---

## §1. σ-signature 의 canonical 통합

### 1.1 Axiom S1' v1 redraft (canonical-ready proposal)

본 세션의 σ-정의 (`02_development.md` §2) 와 Lemma 1, Theorem 1, Theorem 2 의 결과를 종합하여, R23 evening 의 Axiom S1' (atom-borrowed) 을 SCC-intrinsic 어휘로 재작성한 v1 draft. **Canonical 직접 수정 없음**; 이것은 stage 6 weekly merge 에서 사용자가 검토할 proposal.

> **Axiom S1' (Cohesion Mode Quantization, v1, 2026-04-24).**
>
> Let $G = (X, E)$ be a finite simple connected graph, $\Gamma = \text{Aut}(G)$, $\mathcal{E} : \Sigma_m \to \mathbb{R}$ the SCC energy with $b_D = 0$ and $\mathcal{E}_\text{tr}$ omitted (single-time formation analysis). Suppose $u^* \in \Sigma_m$ is a Morse-index-0 local minimum of $\mathcal{E}$ on $\Sigma_m$.
>
> **(S1'-i) Local-maxima count.** The integer
> $$\mathcal{F}(u^*) := |\{i \in X : u^*(i) > u^*(j) \text{ for all } j \sim i\}|$$
> is the **threshold-independent formation count** of $u^*$.
>
> **(S1'-ii) Spectral signature.** Fix a cutoff $K \leq n - 1$ via the spectral-gap rule
> $$K := \min\{k > 0 : \lambda_k(H(u^*)) > 10 \cdot \lambda_{0+}\},$$
> where $\lambda_{0+}$ is the smallest Hessian eigenvalue larger than the translation-Goldstone band (Theorem 1 of `02_development.md` §5). For each $k = 0, 1, \ldots, K-1$, the orbit data
> - **Nodal count** $n_k := \mathcal{N}(\phi_k) \in \mathbb{Z}_{\geq 1}$ (graph-intrinsic, Lemma 2(i));
> - **Irrep class** $[\rho_k] \in \widehat{S(u^*)}$ (canonical via isotypic projector, Lemma 1);
> - **Eigenvalue** $\lambda_k \in \mathbb{R}_{\geq 0}$;
>
> together comprise the cohesion signature
> $$\sigma(u^*) := \big(\mathcal{F}(u^*);\; \{(n_k, [\rho_k], \lambda_k)\}_{k=0}^{K-1}\big).$$
>
> **(S1'-iii) Identity claim.** Two minimizers $u^*, u^{*\prime}$ are $\Gamma$-equivalent if and only if they admit the same signature, $\sigma(u^*) = \sigma(u^{*\prime})$, in the sense of Definition 2.3 of `02_development.md`. Cohesion identity is determined by signature.
>
> **(S1'-iv) Observable bridge.** $K_\text{step}(u^*; \tau) \leq \mathcal{F}(u^*)$ for every $\tau \in (0, 1)$, with equality iff for each $k$ with $\lambda_k$ below the depth scale $\beta/(4\alpha)$ the eigenvector $\phi_k$ has nodal count $n_k = 1$ (single-domain modes only). $\widehat{K}$, the protocol-empirical formation count, is a separate **protocol-parameterized observable** (CN16 below) and need not equal $K_\text{step}$ or $\mathcal{F}$ in general.

**Canonical placement proposal**: §11 의 fixed commitments 의 14번째 항목으로 추가, 또는 §6 에 새 axiom group "S" (single-formation signature) 신설. CN17 (`pre_brainstorm` §7.3) 의 SCC-intrinsic 정형화로서 동시에 기능.

**SCC-intrinsic verification** (pre_brainstorm §6.3 의 AN/PSN/ON):
- (AN) Axiomatic naturality: A1' (closure contraction), A2 (closure stabilization), B-axioms (adjacency), C-axioms (co-belonging derived only), D-Ax (distinction), E-axioms (transport) 와 충돌 없음. $b_D = 0$ commitment (Item 13) 가 명시 사용 → 의존 정확.
- (PSN) Proof-structural naturality: 기존 single-formation Cat A (T8-Core, Cor 2.2, Prop 1.3a/b) 의 statement 와 호환. 단, T8-Core 의 "single excitation mode" 라는 implicit assumption 이 σ-framework 에서 "K=1, n_0=1, [ρ_0]=trivial, mode is Fiedler" 의 specialization 이라 명시할 필요.
- (ON) Observable naturality: $K_\text{step}$, $\widehat{K}$, energy 모두 derived. (S1'-iv) 의 inequality 가 explicit bridge.

### 1.2 CN17 (Orbital-Labeled Formation Quantization) — sharpened

> **CN17 (Cohesion Signature as Primary Formation Identity).**
>
> *Claim*: Single-formation identity is determined by the cohesion signature σ (Axiom S1' v1), not by any single observable such as $K_\text{step}$, $\widehat{K}$, or energy alone.
>
> *Without CN17*: Multiple distinct stable minimizers (R23 §10: 56 distinct on 32×32) collapse to a few "$K_\text{step}$ classes", losing topological/spectral structure. Theorems formulated in terms of $K_\text{step}$ alone (e.g., previously claimed K-uniqueness) are partial.
>
> *With CN17*: Each minimizer carries a richer structural label. Theorems can be stated as "for each σ-class, the following holds...", allowing finer regimes.
>
> *Falsification test*: σ identifies the same equivalence class as Aut(G)-orbit (S1'-iii). Counterexamples would be (a) two minimizers in distinct Aut(G)-orbits with identical σ (= ambiguity in σ), or (b) two Aut(G)-equivalent minimizers with different σ (= σ over-specifies). Falsification (a) likely at non-generic parameter points (cf. §02 §8.1); (b) impossible by Lemma 1+2 invariance.
>
> *Independent evidence*: R23 §10 — 56 stable minimizers, 52 distinct $(F, K_\text{step})$, 37 distinct mode-1 angular labels. The fact that 56 > 52 > 37 indicates that no single coarse label suffices; richer signature needed. σ provides this.

### 1.3 CN15 (Static/Dynamic Separation) — sharpened

> **CN15 (Static Landscape vs Dynamic Observable Separation).**
>
> *Claim*: The static energy landscape $\mathcal{E}$ on $\Sigma_m$ (with its critical points, basins, σ-signatures) and the dynamic observables (gradient flow endpoints, $\widehat{K}$, basin selection probabilities) are **structurally decoupled**. Static $K_\text{global} = 1$ (isoperimetric ordering, T-Merge (b)) and observed $\widehat{K} > 1$ (R17 §X1 etc.) are mutually consistent under this separation.
>
> *Without CN15*: The two facts (static K=1 vs dynamic $\widehat{K} \approx 7.76$) appear contradictory. One would have to dispute either F(K) monotonicity (canonical theorem) or empirical measurement (Cat A data).
>
> *With CN15*: The discrepancy is structurally expected. $K_\text{global}$ is the global minimum of $\mathcal{E}$; $\widehat{K}$ is the protocol-conditional gradient-flow attractor.
>
> *Falsification test*: Slow-anneal protocol $\sigma_0 \to 0$ quasi-statically from a random IC. If the system reliably reaches $K_\text{global} = 1$, CN15 is weak (kinetic barriers thermalizable). If barriers remain insurmountable across all protocols of interest, CN15 supported. (NQ-124 of pre_brainstorm.) **Pertinent**: under canonical zero-temperature gradient flow, no thermal protocol exists (P-F open). CN15 is currently a **statement about the structure of the landscape and the deterministic flow**, not about thermal dynamics.
>
> *Independent evidence*: R17 ($\widehat K = 7.76$), R18 (torus K=1), R22 X1 V5 hysteresis (different ICs → different $\widehat{K}$). All consistent with static ≠ dynamic.

### 1.4 CN16 (Protocol-Parameterized Observables) — sharpened

> **CN16 (Protocol-Parameterized Observables).**
>
> *Claim*: Observables of the SCC system separate into two classes:
> - (Class I) **Protocol-invariant**: σ-signature, energy, Hessian spectrum at a given $u^*$, $\mathcal{F}$, $K_\text{step}$ at $u^*$.
> - (Class II) **Protocol-conditional**: empirical $\widehat{K}$, basin-selection probability, time-to-reach.
>
> Class I depends only on $(\mathcal{E}, \Sigma_m, u^*)$; Class II depends additionally on the protocol $\pi$ (initialization, noise, descent rule).
>
> *Without CN16*: Theorems mixing both classes have undefined truth conditions. E.g., "$\widehat{K} = 1$" needs protocol specification to be falsifiable.
>
> *With CN16*: Each canonical theorem is labeled (I) or (II); (II) statements come with explicit protocol family.
>
> *Falsification test*: A claimed protocol-invariant that varies with reasonable protocol changes. (No counterexample yet observed; σ-signature is candidate-stable.)
>
> *Independent evidence*: R22 X1 V5 hysteresis directly demonstrates protocol selection. V7 P3 shows distribution of $\widehat{K}$ under one protocol family.

### 1.5 Compatibility audit with canonical

| Canonical entity | Relation to σ / S1' v1 | Status |
|---|---|---|
| §3 $\mathfrak{C}^\text{soft}$ formal universe | σ uses $u_t$, $X_t$, derived. $\Gamma = \text{Aut}(G)$ from $X_t$ structure (graph). | Compatible |
| §11 Commitment 1 (primacy of $u$) | σ derived from $u^*$; $u^*$ remains primitive | Compatible |
| §11 Commitment 5 (4-term independence) | σ uses Hessian of full $\mathcal{E}$, not per-term. Per-term frustration (A5) is separate analysis. | Compatible |
| §11 Commitment 6 (CN6: K kinetic) | σ-(S1'-iv) inequality $K_\text{step} \leq \mathcal{F}$ is static. Dynamic $\widehat K$ separated by CN15/16. | Compatible |
| §11 Commitment 11 (diagnostic vector primary) | σ does **not** replace $\mathbf{d} = (\text{Bind, Sep, Inside, Persist})$. σ is signature, $\mathbf{d}$ is diagnostic; complementary. | Compatible |
| §13 T-Birth-Parametric (Cat A, D₄) | σ extends T-Birth: T-Birth predicts existence of bifurcating mode in irrep $E$ of $D_4$ at first pitchfork; σ provides the post-bifurcation labeling. | Compatible (σ extends) |
| §13 Prop 1.3a (Cat A, mode count at uniform) | σ extends Prop 1.3a beyond uniform to general $u^*$: Prop 1.3a is "σ at $u^* = c\mathbf{1}$"; σ generalizes. | Compatible (σ extends) |
| §13 Cor 2.2 quantitative (tanh ansatz, Cat A) | σ uses Cor 2.2 ansatz in Theorem 1 (Goldstone exponential decay) and §7 (continuum). | Compatible (σ uses) |
| §14 CN5 (4-term independence) | σ does not merge terms. | Compatible |
| §14 CN8 (formations metastable) | σ is feature of metastable minimizer, doesn't claim global optimality. | Compatible |
| §14 CN10 (contrastive not reductive) | σ-language is graph-intrinsic, not borrowed. SCC-intrinsic vs atomic comparison is contrastive (Theorem 1 §5.5 explicitly). | Compatible (CN10 reinforced) |

→ S1' v1 + CN17 sharpening 은 canonical 의 어떤 commitment 와도 충돌 없음. **Stage 6 weekly merge 후보.**

---

## §2. A-01 statement revision recommendation

R23 의 A-01 (Cat A empirical) 의 statement 가 Theorem 1 (`02_development.md` §5) 에 의해 수정 권고됨.

### 2.1 현행 A-01 (R23 §09 §10)

> **A-01.** Across all tested configurations (16×16, 32×32 free-BC grids, pure $\mathcal{E}_\text{bd}$ and full SCC), low-lying Hessian eigenmode structure exhibits consistent **p-dominant (ℓ=1) Mode 0** and **d-dominant (ℓ=2) Mode 1**. Pattern reproducible across (β, c). **Cat A empirical.**

### 2.2 수정 권고 (revised A-01)

> **A-01' (revised 2026-04-24).** Across all tested configurations (16×16, 32×32 free-BC grids), the lowest non-trivial mode of $H(u^*)|_{\mathbf{1}^\perp}$ at any bulk-localized stable minimizer $u^*$ has eigenvalue $\lambda_0 \ll \lambda_1$ and angular multipole power concentrated in the ℓ=1 channel. Per Theorem 1 (`THEORY/logs/daily/2026-04-24/02_development.md` §5), this Mode 0 is the **translation pseudo-Goldstone** carrying the $E$ irrep of $D_4$, with $\lambda_0 = O(\exp(-d_*/\xi_0))$. **It is not a genuine orbital excitation** in the same sense as ℓ ≥ 2 modes; the apparent "p-dominant" character reflects the basis $(x, y)$ of the $E$ irrep matching ℓ=1 angular Fourier components.
>
> The first **non-Goldstone** orbital excitation is Mode 1, with angular power 0.38–0.41 in the ℓ=2 channel, irrep label $\in \{B_1, B_2\}$ generically. **Cat A empirical** (existence of mode hierarchy); **Cat B** (Mode 0 = Goldstone interpretation, pending direct verification of $\lambda_0 \ll \lambda_1$ on R23 dataset).

### 2.3 정정의 의미

- **The empirical content of A-01 (existence of Hessian hierarchy) survives unchanged.** This is the Cat A core.
- **The interpretive label of Mode 0 changes**: from "p-orbital excitation" to "translation pseudo-Goldstone".
- This is a **promotion**, not a retraction: A-01' is more precise. The original A-01 was correct in observation but used misleading labels.
- **No silent resolution of any open problem.** N-1 (soft-hard switching), F-1 (K=2 vacuity), MO-1 (Morse), P-A through P-H all remain open.

### 2.4 Verification action item (next session)

R23 dataset (`exp_orbital_fullscale.json`) 의 56 stable minimizer 에 대해:
1. $\lambda_0 / \lambda_1$ ratio 의 distribution 측정
2. $u^*$ 의 center-of-mass 및 boundary distance $d_*$ 측정
3. $\lambda_0 \cdot e^{d_*/\xi_0}$ 가 grid-size-independent 한지 확인 (Theorem 1 의 prediction)

이 검증이 수행되면 A-01' 가 Cat A 로 승급. 본 세션은 statement 수정의 **이론적 근거** 를 제공.

---

## §3. 기존 open problem 과의 관계 (partial-resolution table)

각 OP 에 대해 (a) 본 세션이 영향 미쳤는가, (b) 어떻게, (c) 여전히 open 인 부분, 명시. **No silent resolution.**

| OP | 본 세션의 영향 | 영향 type | 여전히 open |
|---|---|---|---|
| **F-1** (K=2 vacuity) | 간접: σ 가 (S1'-iv) 에서 $K_\text{step} \leq \mathcal{F}$ → K=2 가 single $u^*$ 안의 multi-formation 이 아닌 multi-disconnected-formation 임을 명시. | reframing | F-1 핵심 (K=2 가 global stable 인지) 는 σ 와 무관, 여전히 open. |
| **M-1** (K=1 preference) | 간접: σ-(S1'-iv) 가 $K_\text{step}$ 과 $\mathcal{F}$ 분리 → "K=1 is global min" 이 $K_\text{step}$ 또는 $\widehat K$ 차원에서 의미. $\mathcal{F}$ 차원에서는 minimum $\mathcal{F}$ 가 closure 하에서 1 이 아님 (Theorem 2). | partial reframing | M-1 의 isoperimetric ordering 자체 (T-Merge (b)) 는 open 변동 없음. **새 question**: $\mathcal{F}$-차원의 "K=1 preference" 는 무엇인가? 현재 Theorem 2 가 이 답을 거부. |
| **MO-1** (Morse inapplicability) | 간접: σ 는 Morse-0 minimizer 에 한정. saddle / corner manifold 위 σ 정의 안 됨. | scope clarification | MO-1 (corner manifold) 는 σ 의 scope 밖이므로 본 세션은 직접 영향 없음. |
| **OP-0001..0007** (canonical open list) | 본 세션은 OP-0007 (signature/identity question) 에 부분적 답 시도 — σ 정의 자체가 답 후보. | partial answer | OP-0001..0006 는 본 세션 무관. |
| **N-1** (Soft-Hard Switching Asymmetry) | 직접: σ 의 (S1'-iv) bridge 가 soft ($u, \mathcal{F}$) 와 hard ($K_\text{step}$) 의 명시적 inequality 관계 제공. | partial answer | N-1 의 핵심 (왜 두 layer 가 둘 다 필요한가) 는 reframed: "soft σ 는 invariant, hard $K_\text{step}$ 은 thresholded observable" — 이것이 N-1 의 부분 응답이지만 N-1 의 모든 측면 (P-A, P-D 등) 해결 안 됨. |
| **P-A** (Integer-K vs continuous-u mismatch) | 직접: σ-(i) $\mathcal{F}$ 와 σ-(iv) $K_\text{step}$ 가 둘 다 정수 invariant 제공 (continuous $u$ 에서). | partial answer | P-A 의 핵심 ("smooth connection") 는 여전히 open: $\mathcal{F}, K_\text{step}$ 는 정수이지 smooth 함수가 아님. |
| **P-B** (External substrate dependence) | 무관 | none | open 변동 없음 |
| **P-C** (Missing third mode, co-belonging) | 무관 | none | open 변동 없음. C-Axioms 와 σ 직접 관계 없음. |
| **P-D** (Threshold non-principled) | 직접: σ 는 thresholded observable ($K_\text{step}$ at τ) 의존성을 (S1'-iv) 에서 explicit. $\mathcal{F}$ 는 threshold-free → P-D 의 부분 회피. | partial circumvention | P-D 의 핵심 (Core, Inside 의 θ_core, θ_in 임의성) 는 σ 와 무관, 여전히 open. |
| **P-E** (Parameter origin) | 무관 | none | σ 는 parameter 가 정해진 후 정의 |
| **P-F** (Zero-T metastability) | 간접 — Theorem 1 의 Goldstone 은 zero-T 에서 정의 가능; CN15 가 zero-T deterministic 하에서 statement. | clarification | P-F (entropy / noise framework) 자체 open 변동 없음 |
| **P-G** (Axiom-implementation divorce) | 직접: 본 세션이 $b_D = 0$ commitment 명시 사용 → P-G 의 "axiom 와 코드 가 분리됨" 의 한 instance 를 explicit. | clarification (negative) | P-G 의 다른 instance (E3 demotion, A1' weakening) open 변동 없음 |
| **P-H** (Time pre-theoretic) | 무관 (single-time analysis) | none | open 변동 없음 |

**Silent resolution 점검**: 위 표의 어느 항목도 "now resolved" 라 주장 안 함. 모두 "partial answer / partial reframing / clarification" 표시. **§5 의 audit 와 일관.**

---

## §4. 새 제안 정리 / 추측 의 status sketch

본 세션에서 새로 등장한 명제들의 정리·추측 계열 분류 (canonical 의 theorem_status.md 미반영, 본 세션 자가 평가).

| ID | Statement | Cat | 의존 |
|---|---|---|---|
| Def-σ | Cohesion signature σ is well-defined for Morse-0 minimizers | A definitional | (O3) cutoff 선택 |
| Lem-1 | Irrep decomposition of Hessian eigenspaces under stabilizer | A | Maschke, isotypic projector |
| Lem-2(i,ii,iv) | Nodal count is graph-intrinsic, Aut(G)-equivariant, sign-flip invariant | A | standard graph theory |
| Lem-2(iii) | Courant bound $\mathcal{N}(\phi_k) \leq k+1$ for SCC Hessian | C | signed-Laplacian frustration index, Lange-Liu-Peyerimhoff-Post 2015 |
| Thm-1 | Mode 0 of bulk-localized minimizer is translation pseudo-Goldstone, $\lambda_0 = O(e^{-d_*/\xi_0})$ | B | Cor 2.2 tail, $D_4$ rep theory |
| Thm-1 corollary | A-01 revision (Mode 0 reinterpretation) | B | depends on Thm-1 |
| Thm-2 | Pre-objective: closure removes F=1 stable minimizer under (C1)–(C5) | C | (C5) explicit threshold pending |
| §7 corollary | Continuum shell-Schrödinger spectrum + $D_4$ correction | C | continuum approximation, finite-size mixing |
| AS1' v1 | Axiom S1' v1 (canonical-ready proposal) | (proposal) | Def-σ, Lem-1, Lem-2 |
| CN15 sharpened | Static/Dynamic Separation with explicit falsification test | A (empirical confirmation, R17/R18/R22) | data |
| CN16 sharpened | Protocol-Parameterized Observables, Class I/II split | A (definitional) | observation patterns |
| CN17 sharpened | Cohesion Signature as Primary Formation Identity | A (definitional) | Def-σ |
| Pre-objective Theorem 2 (full-rigor version) | F=1 removal with explicit (C5) | (open) | Thm-2 sketch |
| F=1 → F≥5 jump explanation | Why minimum $\mathcal{F}$ is 5 (not 2 or 3) under full SCC | (open conjecture) | spectral gap + Cor 2.2 interaction |

위 표는 stage 6 weekly merge 시 theorem_status.md 의 추가 후보. 본 세션은 **canonical 또는 theorem_status.md 직접 수정 없음**.

---

## §5. Silent-resolution audit

본 세션 종료 직전 점검. 다음 OP 에 대해 "이 세션이 해결했다" 고 주장하는가?

| OP | 본 세션이 해결 주장? | 비고 |
|---|---|---|
| F-1 | **No** | reframing 만 (위 §3 표) |
| M-1 | **No** | reframing 만 |
| MO-1 | **No** | scope clarification 만 |
| OP-0001..0006 | **No** | 무관 |
| OP-0007 | **부분 답 시도** (σ 가 identity 정의의 후보) | 명시: "σ-정의 자체가 OP-0007 의 답 후보; 단, OP-0007 의 다른 측면 (e.g. metric on identity space) 는 open" |
| N-1 | **No** (partial answer 명시) | (S1'-iv) bridge 가 partial |
| P-A | **No** (partial answer 명시) | $\mathcal{F}, K_\text{step}$ 정수 invariant 추가, smooth connection 여전 open |
| P-B | **No** | 무관 |
| P-C | **No** | 무관 |
| P-D | **No** (partial circumvention 명시) | $\mathcal{F}$ threshold-free 라는 우회 |
| P-E | **No** | 무관 |
| P-F | **No** | 무관 (zero-T 안에서 Theorem 1) |
| P-G | **No** (한 instance 명시) | $b_D = 0$ explicit 사용 |
| P-H | **No** | 무관 |

→ **Silent resolution: 0 건**. 모든 영향이 "partial / reframing / clarification / circumvention" 으로 명시.

---

## §6. 새 open question 수집 (NQ-125 onwards)

R23 의 NQ 카운트 ~78 개 후. 본 세션에서 발생한 새 open question.

### 6.1 σ-정의 관련

- **NQ-125**: σ 의 cutoff $K$ 의 (O3) 옵션 K-A 에서 spectral-gap multiple $c=10$ 의 정당화 — universal? graph-class-dependent? regime-dependent?
- **NQ-126**: σ 가 distinct Aut(G)-orbit 을 distinct σ-class 로 separate 하는가의 질문. §02 §8.1 의 시도 1 의 generic 주장 → quantitative bound 필요. K cutoff 의 함수로서 Pr[σ-class = orbit] 의 scaling.
- **NQ-127**: σ 의 stability under perturbation: 작은 parameter 변동 $(c, \beta)$ 에 대해 σ 의 component (특히 [ρ_k]) 가 어떻게 변하는가? Phase-transition 처럼 jump 가 있는가?

### 6.2 Mode-0 / Theorem 1 관련

- **NQ-128**: R23 56 stable minimizer 의 $\lambda_0 / \lambda_1$ ratio 분포. $< 0.1$ 의 fraction = Theorem 1 적용 fraction.
- **NQ-129**: $\lambda_0 \cdot e^{d_*/\xi_0}$ 의 universal 상수 scaling 검증 — Theorem 1(b) 의 정확한 prefactor.
- **NQ-130**: Boundary-touching minimizer (Theorem 1 가정 위반) 의 Mode 0 character — 진짜 orbital 인가, 다른 종류의 broken symmetry 인가?
- **NQ-131**: Torus (정확한 translation symmetry) 에서 Goldstone 이 정확한 zero mode 인지의 직접 검증. R23 R18 (torus) 데이터에 적용.

### 6.3 Theorem 2 / Pre-objective 관련

- **NQ-132**: (C5) 의 explicit threshold $\lambda_\text{cl}^\text{crit}(L, \beta, a_\text{cl}, c)$ 의 closed form 또는 numeric scaling.
- **NQ-133**: F=1 → F≥5 의 jump 에서 "왜 5 인가?" 의 spectral 설명. Spectral gap argument 의 quantification.
- **NQ-134**: cl 와 sep 각각의 disk-destabilizing 효과 분리 — pure cl ($\lambda_\text{sep} = 0$) 과 pure sep ($\lambda_\text{cl} = 0$) 에서 disk minimum 의 stability scan.
- **NQ-135**: Pre-objective theorem 의 일반화: F=1 뿐 아니라 임의의 $\mathcal{F} \leq F_*(\lambda_\text{cl}, \lambda_\text{sep}, \beta, c)$ 가 destabilized 인 threshold $F_*$ 의 존재.

### 6.4 Continuum / spectrum 관련

- **NQ-136**: §7 의 effective Schrödinger spectrum 의 closed form 또는 numerical 확인. Shell-well bound state 수.
- **NQ-137**: Continuum 예측의 finite-grid 32×32 spectrum 과의 부합도. Lowest 20 modes 의 (n, ℓ) 라벨 vs nodal/irrep label 의 cross-check (= G2/G3 의 numerical 작업).
- **NQ-138**: $D_4$ correction 의 mixing matrix element scaling — pre_brainstorm §4.3 의 $(\xi_0/r_0)^k$ 가설의 정량 확인.

### 6.5 Bifurcation / catalog 관련 (A4 후속)

- **NQ-139**: 56 stable minimizer 를 disk → secondary bifurcation tree 위에 배치. 각 minimizer 의 "출현 분기 점" β-위치.
- **NQ-140**: Equivariant secondary bifurcation 의 cubic-coefficient 분석 (R22 §3.3 의 first pitchfork 와 같은 형식으로). Axis vs diagonal 외 더 다양한 isotropy subgroup.

### 6.6 σ 와 다른 framework 의 관계

- **NQ-141**: σ-signature 와 R23 §07 의 orbital taxonomy (1s, 2p, 2d, 3d, 4f, 5g) 의 정확한 대응. Continuum limit 에서 (n, ℓ) → (n_k, [ρ_k]) 의 명시적 map.
- **NQ-142**: σ 와 R22 SF_layer_classification 의 layer 1/2/3 분류와의 관계. σ 가 어느 layer 에 속하는가? 또는 cross-layer 객체인가?

### 6.7 후속 세션 즉시 가용 NQ 후보

위 18 개 NQ 중 다음 5 개가 **next session (2026-04-25) 에서 numerical 작업으로 즉시 검증 가능** (R23 데이터 재분석만):

1. **NQ-128** ($\lambda_0/\lambda_1$ ratio 분포 — Theorem 1 검증)
2. **NQ-137** (lowest 20 modes 의 (n, ℓ) vs (n_k, [ρ_k]) cross-check — σ-정의 검증, plan G2/G3 의 본업)
3. **NQ-141** (σ ↔ orbital taxonomy 대응 map)
4. **NQ-126** (σ-class = Aut(G)-orbit 의 generic 주장 정량 검증)
5. **NQ-133** (F=1 → F≥5 jump 의 spectral 설명)

→ **권고**: 내일 plan.md 의 target 으로 위 5 NQ 중 (NQ-128 + NQ-137) 결합. R23 데이터 재분석 + Theorem 1 / σ-정의의 numerical 검증.

---

## §7. Prompt template 개선 제안

본 세션이 사용한 `MAIN_PROMPT.md` 템플릿에 대한 피드백.

### 7.1 잘 작동한 부분

- §3 진입 절차의 순서 — 실제로 plan.md → canonical → working → 최근 daily 순서로 읽으면 context 잘 누적됨.
- §4 "최소 3개 접근" 의 강제 — 단일 path 에 빠지는 위험 방지. 본 세션에서 5 개 접근 생성하여 primary 선택 명확.
- §6 출력 파일 번호 prefix (01, 02, 03, 99) — naviation 용이.
- §8 hard constraints — 특히 Silent resolution 금지 + canonical 직접 수정 금지 가 내내 가드 역할.
- §10 자가 점검 list — 세션 종료 직전 명시 audit.

### 7.2 개선 제안 (프롬프트 v2 후보)

1. **(개선 A) Pre-brainstorm 의 위치 명시.** 이번 세션은 사용자가 plan.md 외에 `pre_brainstorm.md` 도 미리 작성 → 세션 입력 context 가 풍부. 이것이 매우 효과적이었음. 프롬프트 템플릿에 "사용자가 pre_brainstorm.md 를 작성한 경우 plan.md 다음 즉시 읽기" 명시 권고.

2. **(개선 B) "단일 target" 정의 완화.** Plan.md 가 5 goal (G1–G5) 을 가졌으나 모두 단일 meta-target ("orbital empirical → SCC-intrinsic") 의 sub-task. 프롬프트 §4 의 "단일 target" 표현이 약간 misleading; "단일 meta-target + 다수 sub-deliverable" 시나리오 도 허용임을 명시.

3. **(개선 C) 출력 파일 사이즈 가이드.** 02_development.md 의 적정 크기가 명시 안 됨. "10+ section 까지 허용, ~700-1200 줄 권장" 정도의 가이드 추가.

4. **(개선 D) Numerical task vs theory task 분리.** Plan.md G2/G3 가 numerical (`exp_orbital_fullscale.json` 재분석 + scripts 작성) 을 요구했지만, 본 세션의 출력은 theory only (logs/daily 출력 규약). 이 mismatch 가 처음에 약간의 ambiguity. 프롬프트 §6 에 "numerical 작업 (코드 작성·실행) 은 별도 사용자 세션에서 처리; logs/daily 는 theory-output 만" 명시 권고.

5. **(개선 E) §12 "예상 오류 패턴" 의 SCC-specific 항목 추가.** 예시: "translation Goldstone 과 orbital excitation 혼동" (Theorem 1 의 핵심), "$K_\text{step}$ 과 $\mathcal{F}$ 혼동" (R23 핵심), "atomic orbital 의 (n, ℓ) 표기를 SCC 정의로 사용" (N-1 borrowing trap). 본 프롬프트의 §12 가 일반적 함정에 머무름.

6. **(개선 F) Working 디렉토리 references 의 일괄 표.** 프롬프트 §3 에 "최근 working 의 어느 파일이 어느 주제" 표가 있으면 세션 진입 빨라짐. 현재 세션마다 manually inspect.

위 6 개 개선은 사용자 검토 후 v2 분기 결정.

---

## §8. 본 파일의 자기 평가

- §1 σ-canonical 통합 (S1' v1 redraft + CN17 sharpening) ✓
- §1.3-1.4 CN15 / CN16 sharpened ✓
- §1.5 canonical compatibility audit ✓
- §2 A-01 revision recommendation + verification action item ✓
- §3 기존 OP partial-resolution 표 (silent resolution 0건) ✓
- §4 새 정리 sketch 의 status table ✓
- §5 silent-resolution audit (0건) ✓
- §6 18 개 새 NQ 수집 + 후속 세션 5 추천 ✓
- §7 prompt template 개선 제안 6 개 ✓

다음 파일: `99_summary.md` — 3-5 sentence 요약 + 내일 plan.md 권고.
