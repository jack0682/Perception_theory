# 06_open_problems_digest.md — Open Problem Consolidation (Pre-existing + New)

**Session:** 2026-04-24 (evening)
**Origin:** 사용자 요청 — "남은 open problem 과 새로 생긴 open problem 정리 및 설명".
**This file covers:** (A) 본 세션 이전 catalogued OP 의 현재 status (각각 본 세션 영향 명시) · (B) 본 세션이 생성한 26 새 NQ (NQ-125..150) 의 정리 + 분류 · (C) Strategic clustering · (D) 다음 세션 priority ranking.
**Depends on reading:** `canonical/open_problems.md` (OP-0001..0007), `working/open_problems_reframing_2026-04-19.md` (N-1 / P-A..H), 본 세션 `02_development.md` `03_integration_and_new_open.md` `04_orbital_proofs.md` `05_orbital_essence.md`.

---

## §A. Pre-existing open problems — current status

세 그룹으로 organized: (A1) Critical 3 (F-1, M-1, MO-1) · (A2) Reformulation series (N-1 + P-A..H) · (A3) Canonical original list (OP-0001..0007).

### A1. Critical 3 (canonical, since 2026-03-xx)

#### **F-1 — K=2 Vacuity**
- **Statement**: K=2 global stability requires external per-formation mass constraint; without it, K=1 is always energetically cheaper (~50% less energy).
- **본 세션 영향**: σ-(S1'-iv) bridge ($K_\text{step} \leq \mathcal{F}$) 가 K-counting 의 layer 분리 명시. K=2 가 single $u^*$ 의 multi-formation 인지 multi-disconnected-formation 인지 식별 가능.
- **여전히 open**: F-1 의 핵심 — "K=2 가 어떤 setup 에서 global stable 인가" — 는 σ 와 무관, 변동 없음. **Cat: open conjecture, since 2026-03 onset.**

#### **M-1 — K=1 Energetic Preference**
- **Statement**: K=2 energy landscape $E(m_1, m_2)$ 가 K=1 방향으로 monotone decreasing.
- **본 세션 영향**: Theorem 2 (`02_development.md` §6) 가 closure 하에 F=1 (single-disk) 가 saddle 임을 sketched. 이는 M-1 의 "K=1 preference" 가 **layer-dependent**: $K_\text{step}$ layer 에서는 여전히 K=1 우선이지만 $\mathcal{F}$ layer 에서는 minimum $\mathcal{F}$ 가 1 이 아님.
- **여전히 open**: M-1 의 isoperimetric ordering (T-Merge (b)) 자체는 변동 없음. **새 question 발생** (위 §3 표): $\mathcal{F}$-차원의 "K=1 preference" 의 의미. **Cat: open, partial reframing.**

#### **MO-1 — Morse Theory Inapplicability**
- **Statement**: K=2 constrained manifold $\Sigma^2_M$ 에 corner 가 있어 standard Morse theory 적용 불가.
- **본 세션 영향**: σ 가 Morse-0 minimizer 에 한정 → corner manifold 위 σ 정의 안 됨, MO-1 의 scope 밖.
- **여전히 open**: MO-1 핵심 (corner manifold 위 stratified Morse) 변동 없음. **Cat: open, scope clarified only.**

### A2. Reformulation series (2026-04-19 N-1 + 8 P-issues)

#### **N-1 — Soft-Hard Switching Asymmetry (umbrella)**
- **Statement**: 이론 ontology 는 continuous (graded $u$), operations 는 discrete (integer K, threshold) 의존. F-1, M-1, MO-1 의 root cause.
- **본 세션 영향**: 
  - σ-(S1'-iv) bridge: soft 와 hard 의 명시적 inequality 관계 ($K_\text{step} \leq \mathcal{F}$).
  - **`05_orbital_essence.md`** 의 reframing: N-1 이 "bug to fix" 에서 "feature to characterize" 로 전환. σ-framework 자체가 "continuous → discrete emergence" 의 mathematical 정형화.
- **여전히 open** (3 sub-questions, `05_orbital_essence.md` §3.4):
  - **N-1.A** (NQ-A): σ 가 parameter 변동 (β, c) 하 어떻게 jump? — orbital phase transition 의 정형화.
  - **N-1.B** (NQ-B): 두 σ-class 사이 transition path (saddle, NEB) 의 dynamics — emergence 의 동역학적 측면.
  - **N-1.C** (NQ-C): σ 의 universality — random graph, SBM 등에서도 작동? graph-class-specific?
- **Cat: open, partial answer + reframe.**

#### **P-A — Integer-K vs Continuous-u Mismatch**
- **Statement**: $u_t \in [0,1]$ 연속, K (formation count) 정수; smooth connection 부재.
- **본 세션 영향**: σ-(i) ($\mathcal{F} \in \mathbb{Z}_{\geq 0}$) + σ-(iv) ($K_\text{step} \in \mathbb{Z}_{\geq 0}$) 가 두 정수 invariant 제공. Continuous → discrete map 정의.
- **여전히 open**: "smooth connection" 자체는 부재. $\mathcal{F}, K_\text{step}$ 는 정수 점프 함수 (smooth 아님). 그러나 위 N-1 reframing 으로 이 비-smoothness 가 결함이 아님이 정립.
- **Cat: open, partial answer (정수 invariants 정형화 ✓; smooth connection 거부됨).**

#### **P-B — External Substrate Dependence**
- **Statement**: $X_t$ (sites), $N_t$ (adjacency) 가 pre-theoretic input. "Pre-objective" claim 이 pre-given relational structure 에 의존.
- **본 세션 영향**: 무관.
- **여전히 open**: 변동 없음. **Cat: open, untouched.**

#### **P-C — Missing Third Mode (Co-belonging)**
- **Statement**: Cl 와 D 가 energy-bearing, Co-belonging $\mathbf{C}_t$ 가 derived diagnostic 로 강등 (canonical Item 12). Justifying 가 부재.
- **본 세션 영향**: 무관 (σ-framework 가 $\mathbf{C}_t$ 사용 안 함).
- **여전히 open**: 변동 없음. **Cat: open, untouched.**

#### **P-D — Threshold Non-Principled Embedding**
- **Statement**: Core, Inside, Boundary 가 임의 threshold $\theta$ 의존. Threshold-free 정형화 부재.
- **본 세션 영향**: $\mathcal{F}$ (σ-(i)) 는 threshold-free → P-D 의 부분 회피. (S1'-iv) 의 $K_\text{step}$ 은 여전히 $\tau$-의존.
- **여전히 open**: $\theta_\text{core}, \theta_\text{in}$ 임의성 변동 없음. $\mathcal{F}$ 가 추가 threshold-free invariant 로 합류. **Cat: open, partial circumvention.**

#### **P-E — Parameter Origin Problem**
- **Statement**: 25+ external parameters ($a_\text{cl}, \beta, \lambda_\text{rep}$, 등) origin 부재.
- **본 세션 영향**: 무관 (σ 는 parameters 가 정해진 후 정의).
- **여전히 open**: 변동 없음. **Cat: open, untouched.**

#### **P-F — Zero-Temperature Metastability Claim**
- **Statement**: 이론이 metastability 주장하나 temperature/entropy/noise framework 부재 (zero-T deterministic).
- **본 세션 영향**: 간접 — Theorem 1 의 Goldstone 은 zero-T 에서 정의 가능; CN15 (sharpened) 가 zero-T deterministic 하의 statement.
- **여전히 open**: P-F 자체 (entropy/noise framework 도입) 변동 없음. **Cat: open, clarified scope.**

#### **P-G — Axiom-Implementation Divorce**
- **Statement**: A1 → A1' weakening, $b_D = 0$ implicit D-Ax3 위반, E3 axiom→constraint 강등 등 axiom 과 코드의 분리.
- **본 세션 영향**: 본 세션이 $b_D = 0$ commitment (canonical Item 13) 명시 사용 → P-G 의 한 instance explicit 화.
- **여전히 open**: 다른 instances (A1' weakening, E3 demotion) 변동 없음. **Cat: open, one instance explicated.**

#### **P-H — Time Pre-theoretic**
- **Statement**: $T$ 가 pre-given ordered set, 그러나 이론의 가장 강한 concept 이 "temporal persistence". Time 의 status substrate-dependent.
- **본 세션 영향**: 무관 (single-time analysis).
- **여전히 open**: 변동 없음. **Cat: open, untouched.**

### A3. Canonical original list (OP-0001..0007)

각 OP 의 정확한 statement 는 `canonical/open_problems.md` 에 기록되어 있음 (직접 참조 권고). 본 세션 영향:

- **OP-0001** (binary co-belonging form): 무관, untouched.
- **OP-0002** (transition operator $T_t$): 무관 (canonical 에서 demoted, 본 세션 무관), untouched.
- **OP-0003** (crisp recovery systematic): σ 가 "discrete derivative" 로서 부분 답이지만 OP-0003 은 "객체 추출" 이라 다른 layer. **Cat: open, parallel framework.**
- **OP-0004** (b_D = 0 의 axiom-level justification): P-G 와 같은 issue. **Cat: open, untouched.**
- **OP-0005** (K kinetic vs thermodynamic selection): R23 R22 에서 negative resolution 명시 ("no thermodynamic mechanism"). 본 세션 무관. **Cat: closed via negative resolution (CN6).**
- **OP-0006** (per-formation Hessian decomposition for $K \geq 2$): 본 세션 무관, untouched.
- **OP-0007** (formation identity definition): **σ 가 답 후보** (`03_integration_and_new_open.md` §5). 단 OP-0007 의 다른 측면 (e.g. metric on identity space) 는 open. **Cat: open, partial answer via σ.**

### A4. Critical 3 status table (consolidated)

| OP | 본 세션 status |
|---|---|
| F-1 | open (untouched core) |
| M-1 | open + new question (F-차원 K=1 preference 의 의미) |
| MO-1 | open (scope clarified, σ doesn't address) |
| OP-0001..0006 | mostly open (OP-0005 closed by negative; others untouched) |
| OP-0007 | open + partial answer (σ as identity definition candidate) |
| N-1 | open + reframe (bug→feature, σ as emergence formalization) + 3 sub-questions |
| P-A | open + partial answer (정수 invariants 정형화) |
| P-B | open (untouched) |
| P-C | open (untouched) |
| P-D | open + partial circumvention ($\mathcal{F}$ threshold-free) |
| P-E | open (untouched) |
| P-F | open + scope clarified |
| P-G | open + one instance explicated ($b_D = 0$) |
| P-H | open (untouched) |

**총 14 pre-existing OP**: 본 세션이 영향 미친 것 = 9 (F-1, M-1, OP-0007, N-1, P-A, P-D, P-F, P-G, MO-1) + closure of OP-0005 (negative). 5 fully untouched (P-B, P-C, P-E, P-H, OP-0001..0004 일부).

**Silent resolution: 0건** (재차 확인).

---

## §B. New open questions — this session (NQ-125..150, 26 items)

각 NQ 의 origin file + statement + difficulty + 후속 가용성.

### B1. σ-definition robustness (3 NQ, from `03_integration_and_new_open.md` §6.1)

#### NQ-125 — Spectral cutoff multiple
- **Statement**: σ-cutoff (O3) option K-A 의 spectral-gap multiple $c = 10$ 의 정당화. universal? graph-class-dependent? regime-dependent?
- **Difficulty**: medium (analytical or numerical scan).
- **즉시 가용**: yes — R23 데이터의 lowest 50 modes 의 gap distribution 분석으로 가능.

#### NQ-126 — σ-class = Aut(G)-orbit equivalence
- **Statement**: σ 가 distinct Aut(G)-orbit 을 distinct σ-class 로 separate 하는가의 generic 주장 → quantitative bound. K cutoff 의 함수로서 $\Pr[\sigma\text{-class} = \text{orbit}]$ scaling.
- **Difficulty**: medium-high (probabilistic / numerical).
- **즉시 가용**: 부분 — R23 56 stable minimizer 의 σ-class 분포로 numerical.

#### NQ-127 — σ stability under parameter perturbation
- **Statement**: 작은 $(c, \beta)$ 변동에 σ 의 component (특히 $[\rho_k]$) 가 어떻게 변하는가? Phase-transition 처럼 jump 가 있는가?
- **Difficulty**: medium (parameter sweep + tracking).
- **즉시 가용**: yes — R23 외 추가 parameter scan 필요 가능.

### B2. Mode-0 / Theorem 1 verification (4 NQ, from §6.2)

#### NQ-128 — $\lambda_0/\lambda_1$ ratio distribution **(highest priority)**
- **Statement**: R23 56 stable minimizer 의 $\lambda_0 / \lambda_1$ 분포. < 0.1 fraction = Theorem 1 적용 가능 fraction.
- **Difficulty**: low (R23 데이터 직접 측정).
- **즉시 가용**: yes — 30분 numerical. **Theorem 1 의 Cat A 승급의 직접 증거.**

#### NQ-129 — Goldstone universal scaling
- **Statement**: $\lambda_0 \cdot e^{d_*/\xi_0}$ 의 universal 상수 scaling 검증 — Theorem 1(b) 의 정확한 prefactor.
- **Difficulty**: low-medium (R23 + scaling 분석).
- **즉시 가용**: yes — NQ-128 직후.

#### NQ-130 — Boundary-touching minimizer Mode 0
- **Statement**: Boundary-touching minimizer (Theorem 1 가정 위반) 의 Mode 0 character — 진짜 orbital? 다른 broken-symmetry?
- **Difficulty**: medium.
- **즉시 가용**: yes — R23 의 boundary-touching subset 분석.

#### NQ-131 — Torus exact Goldstone verification
- **Statement**: Torus (정확한 translation symmetry) 에서 Goldstone 이 exact zero mode 인지 직접 검증. R23 R18 (torus) 데이터.
- **Difficulty**: low (R18 데이터).
- **즉시 가용**: yes.

### B3. Theorem 2 / pre-objective sharpening (4 NQ, from §6.3)

#### NQ-132 — Pre-objective threshold (C5) explicit
- **Statement**: Theorem 2 의 (C5) explicit threshold $\lambda_\text{cl}^\text{crit}(L, \beta, a_\text{cl}, c)$ 의 closed form 또는 numerical scaling.
- **Difficulty**: high (analytical) or medium (numerical scan).
- **즉시 가용**: numerical 으로만 (analytical 은 후속).

#### NQ-133 — F=1 → F≥5 jump explanation
- **Statement**: "왜 5 인가?" 의 spectral gap argument 정량화. Cor 2.2 + Prop 1.3a 결합.
- **Difficulty**: medium (theory).
- **즉시 가용**: theory analysis 가능.

#### NQ-134 — cl vs sep separation effect
- **Statement**: Pure cl ($\lambda_\text{sep} = 0$) 와 pure sep ($\lambda_\text{cl} = 0$) 에서 disk minimum 의 stability 비교 — 어느 항이 destabilization 의 majority?
- **Difficulty**: low-medium (numerical scan).
- **즉시 가용**: yes (parameter scan).

#### NQ-135 — Generalized pre-objective theorem
- **Statement**: F=1 뿐 아니라 임의 $\mathcal{F} \leq F_*(\lambda_\text{cl}, \lambda_\text{sep}, \beta, c)$ 가 destabilized 인 threshold $F_*$ 의 존재.
- **Difficulty**: high (theory + numerics).
- **즉시 가용**: 부분 — R23 데이터에서 minimum stable $\mathcal{F}$ 추출 가능.

### B4. Continuum / spectrum (3 NQ, from §6.4)

#### NQ-136 — Effective Schrödinger spectrum closed form
- **Statement**: `02_development.md` §7 의 shell-Schrödinger spectrum 의 closed form 또는 numerical. Bound state 수.
- **Difficulty**: high (analytical) or medium (1D ODE solver).
- **즉시 가용**: numerically.

#### NQ-137 — Continuum vs finite-grid spectrum agreement **(high priority)**
- **Statement**: §7 continuum 예측의 finite-grid 32×32 spectrum 과 부합도. Lowest 20 modes 의 (n, ℓ) 라벨 vs (n_k, [ρ_k]) cross-check.
- **Difficulty**: medium (numerical).
- **즉시 가용**: yes — **σ-framework 의 핵심 검증**, plan G2/G3 의 본업.

#### NQ-138 — D₄ correction mixing scaling
- **Statement**: pre_brainstorm §4.3 의 mixing $\sim (\xi_0/r_0)^k$ 가설의 정량 확인.
- **Difficulty**: medium (numerical + scaling fit).
- **즉시 가용**: yes.

### B5. Bifurcation catalog (2 NQ, from §6.5)

#### NQ-139 — 56 stable basin bifurcation tree
- **Statement**: R23 56 stable minimizer 를 disk → secondary bifurcation tree 위에 배치. 각 minimizer 의 출현 분기점 β-위치.
- **Difficulty**: high (β-cascade numerical, large compute).
- **즉시 가용**: no — 추가 numerical 필요.

#### NQ-140 — Equivariant secondary bifurcation analysis
- **Statement**: Secondary pitchfork 의 cubic-coefficient 분석 (R22 §3.3 의 first pitchfork extension).
- **Difficulty**: high (analytical, multiple isotropy subgroups).
- **즉시 가용**: theory work 가능.

### B6. σ-framework integration (2 NQ, from §6.6)

#### NQ-141 — σ ↔ R23 orbital taxonomy correspondence **(high priority)**
- **Statement**: σ-signature 와 R23 §07 orbital taxonomy (1s, 2p, 2d, ...) 의 정확한 대응. Continuum (n, ℓ) → discrete $(n_k, [\rho_k])$ map.
- **Difficulty**: medium (theory + R23 data).
- **즉시 가용**: yes.

#### NQ-142 — σ vs Three-Layer classification
- **Statement**: σ 와 R22 SF_layer_classification (Layer 1/2/3) 의 관계. σ 가 어느 layer? Cross-layer?
- **Difficulty**: low (review).
- **즉시 가용**: yes.

### B7. From `04_orbital_proofs.md` §6 (4 NQ)

#### NQ-143 — F-tie convention
- **Statement**: Theorem 4 의 $\mathcal{F}$-tie 처리. Strict-max vs plateau-max convention 의 σ-framework 의미. 어느 것이 R23 measurement 와 부합?
- **Difficulty**: low.
- **즉시 가용**: yes.

#### NQ-144 — $\kappa_{\ell=1}^{D_4}$ exact value
- **Statement**: Lemma 3 의 angular ℓ=1 power 하한 $\kappa_{\ell=1}^{D_4}$ 의 정확한 closed form. 본 세션은 ballpark.
- **Difficulty**: medium (analytical integration).
- **즉시 가용**: theory work.

#### NQ-145 — Secondary pitchfork σ
- **Statement**: Theorem 4 의 $\beta = \beta_\text{crit}^{(2)} + \epsilon$ 외, $\beta = \beta_\text{crit}^{(?)} + \epsilon$ 의 더 high mode 분기 σ.
- **Difficulty**: high.
- **즉시 가용**: theory + numerical 결합.

#### NQ-146 — Higher-ℓ angular ↔ irrep map
- **Statement**: Lemma 3 의 ℓ=2, ℓ=3, ℓ=4 평행 정리. 각 ℓ 가 어느 D₄ irrep 와 연결?
- **Difficulty**: low-medium (group-theoretic computation).
- **즉시 가용**: yes (theory).

### B8. From `05_orbital_essence.md` §7 (4 NQ)

#### NQ-147 — Multi-source discreteness depth quantification
- **Statement**: σ 의 세 source 중 어느 것이 어느 regime 에서 dominant? trivial-stabilizer 영역 vs 풍부한 stabilizer 영역.
- **Difficulty**: medium (regime analysis).
- **즉시 가용**: 부분 — R23 데이터의 stabilizer 분포 분석.

#### NQ-148 — σ-jump (orbital phase transition) formalization
- **Statement**: §3 의 "characterize emergence" 후속. σ 가 parameter 변동 하 jump 하는 mechanism (NQ-127 의 deeper version).
- **Difficulty**: high (theory).
- **즉시 가용**: theory work.

#### NQ-149 — Self-referential vs external-structure emergence quantification
- **Statement**: §4.2 의 "self-referential emergence" (SCC) 와 "external-structure emergence" (atom 의 fixed Coulomb) 의 mathematical 차이의 quantitative statement. σ 의 sensitivity to $\lambda_\text{cl}, \lambda_\text{sep}$ vs atomic insensitivity to nuclear potential normalization.
- **Difficulty**: high (theory + numerics).
- **즉시 가용**: 부분.

#### NQ-150 — σ universality across graph classes
- **Statement**: 다른 graph (random, SBM, hyperbolic, 등) 에서 σ-framework 의 작동. graph-class-specific universality?
- **Difficulty**: high (multi-graph numerics).
- **즉시 가용**: no — multi-graph 실험 필요.

---

## §C. Strategic clustering — OP cluster 구조

위 14 pre-existing + 26 new = 40 OP 를 4 strategic cluster 로 묶음:

### C1. Cluster "Continuous-to-Discrete Emergence" (가장 큰)
- N-1 (umbrella) + N-1.A/B/C
- P-A (integer-K vs continuous-u)
- P-D (threshold)
- OP-0007 (formation identity)
- NQ-125 (cutoff), NQ-126 (σ-orbit), NQ-127 (parameter jump), NQ-147 (source dominance), NQ-148 (jump formalization), NQ-149 (self-ref), NQ-150 (universality)

**총 13 OP**. 본 세션의 σ-framework 가 cluster 의 backbone partial answer. 나머지는 σ 의 robustness, depth, universality 의 추가 정량화.

### C2. Cluster "Pre-objective Mechanism"
- F-1 (K=2 vacuity)
- M-1 (K=1 preference)
- MO-1 (Morse inapplicability)
- NQ-132 (C5 threshold), NQ-133 (F-jump), NQ-134 (cl/sep separation), NQ-135 (generalized pre-objective)

**총 7 OP**. Theorem 2 sketched, (C5) 정량화 후속. 본 세션 직접 영향 받은 가장 active cluster.

### C3. Cluster "Goldstone & Spectral Verification"
- NQ-128 (λ_0/λ_1), NQ-129 (universal scaling), NQ-130 (boundary), NQ-131 (torus), NQ-136 (Schrödinger), NQ-137 (continuum agreement), NQ-138 (D₄ mixing), NQ-141 (orbital taxonomy), NQ-143 (F-tie), NQ-144 (κ exact), NQ-146 (higher ℓ)

**총 11 OP**. R23 데이터 재분석으로 다수 즉시 가용. 본 세션 정리들의 numerical 검증 cluster.

### C4. Cluster "Infrastructure" (이론 외부 dependencies)
- P-B (substrate dependence), P-C (co-belonging), P-E (parameter origin), P-F (zero-T), P-G (axiom-impl divorce), P-H (time)
- OP-0001..0006 (canonical 미해결 list 일부)
- NQ-139 (bifurcation tree), NQ-140 (secondary), NQ-142 (layer relation), NQ-145 (secondary σ)

**총 9-10 OP**. 본 세션과 무관 또는 long-term theory project. P-cluster 다수가 fundamental 이론적 도전.

---

## §D. Priority ranking — 다음 세션 (2026-04-25) target

위 cluster 위 priority + 즉시 가용성 + 결과의 leverage 종합.

### D1. P0 (next session target candidates)

가장 가치 높음 + 즉시 가용 + Cat A 승급 가능:

1. **NQ-128** ($\lambda_0/\lambda_1$ ratio): 30분, **Theorem 1 Cat B → Cat A 승급**, 본 세션 narrative core 확정.
2. **NQ-137** (continuum vs finite-grid agreement): 2-3시간, **σ-framework 의 R23 데이터 위 검증**, 가장 큰 leverage.
3. **NQ-141** (σ ↔ orbital taxonomy map): 1-2시간, σ-framework 와 R23 의 연결, narrative 완결.

**조합 권고**: 하루 = NQ-128 (오전) + NQ-137 (오후) + NQ-141 (저녁). 단일 metablock target = "σ-framework 의 numerical 검증".

### D2. P1 (시간 허용 시)

4. **NQ-126** (σ-class = orbit): R23 56 stable 의 σ 분포 → orbit 분리 검증.
5. **NQ-129** (Goldstone universal scaling): NQ-128 의 deepening.
6. **NQ-131** (torus exact Goldstone): R18 데이터.
7. **NQ-134** (cl vs sep separation): pre-objective mechanism 의 source 식별.

### D3. P2 (theory 작업, 시간 풍부 시)

8. **NQ-133** (F-jump explanation): theory only, ~3-4시간.
9. **NQ-144** (κ exact): theory only, ~2-3시간.
10. **NQ-146** (higher-ℓ irrep map): theory only, ~1-2시간.

### D4. Long-term projects (수 세션에 걸친 작업)

- **Cluster C4 의 P-issues**: P-B, P-C, P-E, P-F 각각 별도 세션 필요. 각 issue 가 fundamental.
- **NQ-150** (universality): multi-graph numerical 실험 program (W5).
- **NQ-148** (σ-jump formalization): theory 깊이 작업, 2-3 세션.
- **NQ-139** (bifurcation tree): 대규모 numerical, 1-2 일.

---

## §E. Total open count

| 분류 | 갯수 |
|---|---|
| Pre-existing OP (canonical + reformulation) | 14 |
| New NQ (this session) | 26 |
| Closed via negative (this session) | 1 (OP-0005) |
| **Total active OP after session** | **40** |

세션 entry 시점 (78 NQ 누적, R23) 대비 +26 새 NQ (NQ-125..150). 이 26 중 약 12 개가 next session R23 데이터 재분석으로 즉시 검증 가능.

---

## §F. 한 페이지 요약 (chat-ready)

**3 개의 sentence 요약**:

1. 본 세션 이후에도 **14 pre-existing OP** (F-1, M-1, MO-1, OP-0001..0007 일부, N-1 + P-A..H) 는 여전히 open 이지만, 그 중 9 개가 σ-framework 또는 Theorem 1/2 에 의해 partial answer / reframing / scope clarification 받았다 (특히 N-1 의 frame 이 "bug to fix" 에서 "feature to characterize" 로 전환).
2. 본 세션이 **26 새 NQ** (NQ-125..150) 를 생성, 이들은 4 strategic cluster (continuous-discrete emergence, pre-objective mechanism, Goldstone/spectral verification, infrastructure) 로 묶이며, 11 개가 R23 데이터 재분석으로 즉시 가용.
3. 다음 세션 P0 target = **NQ-128 + NQ-137 + NQ-141** 의 조합 (Theorem 1 Cat A 승급 + σ-framework numerical 검증 + R23 orbital taxonomy 와의 정확한 대응 map). 이 셋이 이행되면 본 세션의 σ-framework 가 fully empirically grounded.

**End of 06_open_problems_digest.md.**
