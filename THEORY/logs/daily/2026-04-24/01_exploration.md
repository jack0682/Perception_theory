# 01_exploration.md — Restatement, Multi-Approach, Primary Selection

**Session:** 2026-04-24
**Target (from plan.md):** "어제 발견된 orbital structure를 atomic-physics 차용 → SCC-intrinsic definition 으로 전환." 즉 R23 의 Cat A empirical (A-01..A-04) 을 graph-intrinsic + axiomatically-grounded **structural Cat A** 로 승격하기 위한 **신호 체계 (signature) 의 정의·다중 접근·주 접근 선택**.
**This file covers:** §4.1 Restatement (with surfaced assumptions) · §4.2 Multi-approach (5 mathematically independent routes) · §4.3 Primary selection rationale.
**Depends on reading:** `canonical.md` §3, §11, §13 (T-Birth-Parametric, T8-Core, Prop 1.3a/b, Cor 2.2), `canonical.md` §14 (CN1, CN5, CN6, CN8, CN10), `working/SF/mode_count.md` §1–§2 (Prop 1.3a/b), `working/SF/symmetry_moduli.md` §3 (equivariant bifurcation, $\Phi_4$ computation), `working/open_problems_reframing_2026-04-19.md` (N-1 framing), `logs/daily/2026-04-23/{07,09,10,11,12,99}_*.md`, `logs/daily/2026-04-24/{plan,pre_brainstorm}.md`.

---

## §1. Restatement (with surfaced assumptions)

### 1.1 What plan.md asks, in one paragraph

R23 evening 에 다음이 empirically Cat A 로 promoted 되었다:

- **A-01** (orbital hierarchy exists): 16×16 / 32×32 free-BC grid 의 minimizer Hessian 의 low-lying spectrum 이 "Mode 0 = ℓ=1-dominant, Mode 1 = ℓ=2-dominant" 패턴을 (β, c) 변동에도 robust 하게 보임.
- **A-02** (quadrupole as first excited): low-to-moderate β 에서 Mode 1 의 angular power 가 ℓ=2 channel 에 0.38–0.41 집중.
- **A-03** (multiple stable orbital basins coexist): 동일 (β, c)=(30, 0.5) on 32×32 에서 90 random-IC 가 56 distinct stable Morse-0 minimizers 로 수렴, 52 distinct $(F, K_\text{step})$, 37 distinct mode-1 angular labels.
- **A-04** (closure removes F=1 ground state): full SCC 에서 single-disk minimizer 가 saddle 로 변함.

위 네 명제의 statement 는 **현재 (n, ℓ) 라는 atomic-orbital 차용 표기**로 쓰여 있다. (n, ℓ) 은 SCC 의 primitive 어휘에 속하지 않는다. 따라서 "Cat A" 라벨은 정확히는 **"Cat A by analogy at specific config"** 이다 — 명제의 진릿값(truth content) 자체는 empirical 이지만, **명제가 말하는 대상의 정체(what the proposition is about)** 가 차용이다.

오늘의 과제는 이 차용을 제거하고 **graph-intrinsic 어휘로 statement 를 재작성** + **그 statement 가 canonical 의 axiom · 정리 와 자연스럽게 연결되도록 정의를 도입**하는 것이다.

### 1.2 두 가지 동시 요구

이 과제는 두 종류의 작업을 동시에 요구한다:

1. **Definitional**: 새로운 합성 정의 (e.g. *cohesion signature*) 를 도입하여 atomic 차용 라벨 $(n, \ell)$ 의 자리를 SCC-intrinsic 객체 (irrep, nodal count, Hessian eigenvalue) 로 채운다.
2. **Justificatory**: 그 정의가 (i) 기존 canonical 과 충돌 없음, (ii) R23 empirical 데이터를 자연스럽게 분류, (iii) atom 과 SCC 가 서로 다른 spectrum 을 가질 것이라는 **이론적 예측** 을 생성, 임을 보인다.

(2-iii) 가 핵심: SCC-intrinsic 어휘의 가치는 단지 atomic 어휘를 갈아끼우는 게 아니라, **atom 에는 없는 SCC-specific 현상** 을 자연스럽게 포함하는 데 있다. 예: pre_brainstorm §2.4 의 "translation Goldstone 이 p-symmetry 를 흡수 → SCC 의 first excited 가 d 가 됨"은 atomic 어휘 안에서는 단지 anomaly 로 보이지만 SCC-intrinsic 어휘 (volume-constrained simplex 위 Aut(G)-equivariant Hessian) 안에서는 **자연스러운 따름결과**가 되어야 한다.

### 1.3 plan.md 가 암묵적으로 깔고 있는 가정 (surface)

다음은 plan.md 와 pre_brainstorm 이 명시하지 않았으나 사용 중인 가정들이다. 이 자리에서 표면화하여 후속 검증·반증 가능성을 두어야 한다.

| # | 암묵 가정 | 표면화 후 status | 검증 채널 |
|---|---|---|---|
| H1 | 32×32 grid 의 minimizer 가 grid 의 4-fold 회전·8-elem $D_4$ 중심점에 정렬되어 있어, $u^*$ 의 안정자(stabilizer)가 적어도 nontrivial subgroup of $D_4$ 를 포함 | 적어도 56 stable 중 일부에 대해 **참**일 것 (low-F ground states); high-F 일부는 stabilizer trivial 일 가능성 | Stab$_G(u^*)$ 직접 계산 (G3 외부 작업) |
| H2 | Hessian eigenmode 의 angular multipole power decomposition 이 **irrep label 의 proxy** 로서 일관성 있게 작동 | 일반적으로 **부분 참**: angular power 는 continuum-limit irrep 추정에 가까우나, finite-grid $D_4$ irrep 와 정확히 일치하지 않을 수 있음 (mixing 발생) | M1 irrep projection vs angular multipole cross-check (G2의 본질) |
| H3 | "Mode 0" 이 stable minimizer 에서 **항상 의미 있는 직교 mode** 이다 | **부분 거짓**으로 보임: pre_brainstorm §2.3 의 통찰 — Mode 0 이 near-zero eigenvalue 를 갖는 translation Goldstone 일 가능성. 즉 Hess의 0-mode (또는 near-0) 는 orbital excitation 이 아닌 broken-symmetry zero mode | Hessian eigenvalue $\lambda_0$ 의 절댓값 + IPR (inverse participation ratio) 측정 |
| H4 | $K_\text{step}$ 과 $\mathcal{F}$ 의 차이는 high-β / bilobed 영역에서만 의미가 있고, 일반적으로 두 양은 같다 | **거짓**: §10 데이터에서 K=1 with F up to 13 까지 흔하게 관측. 두 양은 generically 다름 | (이미 R23 에서 확립, plan.md non-goal) |
| H5 | $D_4$-equivariant Crandall-Rabinowitz 의 cubic-coefficient 분석 (R22 §3.3) 이 적용되는 first pitchfork 의 axis-aligned 선택이 **모든 stable orbital** 의 분류에 외삽 가능 | **부분 거짓**: cubic 분석은 first pitchfork 에서 axis vs diagonal 만 결정. 더 high mode 에는 직접 적용 불가; equivariant transversality 가 더 풍부한 secondary bifurcation tree 를 요함 | (G4 영역, 오늘 부분 다룸) |
| H6 | Continuum limit 에서의 spectrum 이 finite grid 32×32 의 spectrum 의 **유의미한 근사**이다 | **잠정 참**: 32×32 의 lowest 20 mode 에 한해 continuum approximation 양호 (단, $D_4$ correction 비섭동 항이 high mode 에서 활성) | M2 (G4) 의 본업 |
| H7 | "Pre-objective" 라는 SCC 핵심 commitment 가 closure 의 F=1-removal 효과로 **수학적 정리** 화 가능 | 이것이 오늘 §02 §6 의 추측 정리 (pre-objective theorem). Cat C 잠정 | (오늘 §02 의 작업) |

위 7 가지 가정 표면화는 후속 세션이 "어떤 가정을 깨뜨려 보아야 하는가" 의 카탈로그를 자동으로 갖추게 한다.

### 1.4 무엇이 성공인가, 무엇이 실패인가

세션 종료 시 자가 평가의 명시적 기준:

- **성공 (S)**: $\sigma(u^*) = (\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^{K})$ 의 **graph-intrinsic 정의** 가 수학적으로 well-defined (모호함 없음) + canonical 의 어떤 정리·공리와도 모순 없음 + R23 의 A-01..A-04 statement 를 σ-언어로 재작성 가능 + 새 정의가 적어도 1 가지 **새 falsifiable 예측** 생성.
- **부분 성공 (PS)**: 정의 자체는 well-defined 이나 canonical 과의 통합에서 1–2 곳 미해결 (e.g. C-Axioms 와의 관계).
- **실패 (F)**: σ-정의가 모호한 자유도를 남기거나 (e.g. "lowest K modes" 의 K 가 임의), R23 데이터를 분류하지 못함 (counterexample 발생), 또는 silent resolution 발생.

오늘 적어도 PS, 가능하면 S 를 목표.

---

## §2. Multi-approach (5 mathematically independent routes)

각 접근에 대해 (a) 핵심 idea, (b) 성공 시 산출물, (c) 실패 모드, (d) canonical 와의 상호작용 을 기록.

### A1. Representation-theoretic — Aut(G)-equivariant Hessian decomposition

**(a) Idea.** $u^*$ 의 stabilizer $\text{Stab}_{\text{Aut}(G)}(u^*) =: S$ 는 $\text{Hess}\,\mathcal{E}(u^*)$ 와 commute 한다 (왜냐하면 $\mathcal{E}$ 는 $\text{Aut}(G)$-invariant). 따라서 $T_{u^*}\Sigma_m$ 은 $S$ 의 unitary representation 으로 분해되고, Hessian eigenspaces 는 irreducible 성분의 합으로 표현된다. 각 eigenmode $\phi_k$ 에 대해 그 eigenspace 의 isotypic component decomposition 이 정의되며, dominant irrep $[\rho_k]$ 가 그 mode 의 SCC-intrinsic label 로 사용 가능.

**(b) 성공 시 산출물.** 모든 eigenmode 에 대한 irrep label 함수 $\rho : \text{Spec}(\text{Hess}) \to \widehat{S}$. R23 의 angular multipole power decomposition 이 (large-grid 에서) irrep projection 의 근사임을 보임.

**(c) 실패 모드.**
1. **Stabilizer trivial.** 만약 $u^*$ 가 어떤 graph-symmetry 도 보존하지 않으면 (high-F random-IC 결과 일부) $S = \{e\}$ 이고 모든 irrep 은 trivial — 이 경우 label 이 vacuous.
2. **Eigenvalue 중첩.** 같은 $\lambda_k$ 의 두 mode 가 서로 다른 irrep 에 속할 때 dominant irrep 이 임의 (mixing).
3. **Group action 가 grid 중심점에 정확히 align 되지 않음.** Translation 이 보존되지 않는 free-BC 에서 $u^*$ 가 grid 중심을 벗어나면 효과적 stabilizer 가 떨어진다.

**(d) Canonical 상호작용.** T-Birth-Parametric (D₄ supercritical pitchfork, Cat A) 는 first pitchfork 에서 D₄ irrep 분해를 명시적으로 사용한다. 이것을 nucleation-time 에서 minimizer 에 대한 "post-bifurcation 시점에서의 stabilizer" 로 확장하는 작업. canonical 직접 추가 없음, 정의 보강.

---

### A2. Spectral-combinatorial — Courant nodal domain count

**(a) Idea.** Hessian eigenvector $\phi_k$ 의 **nodal domain count** $\mathcal{N}(\phi_k) :=$ "$\{i : \phi_k(i) > 0\}$ 의 connected component 수 + $\{i : \phi_k(i) < 0\}$ 의 connected component 수" 는 graph-intrinsic 정수 함수. Courant-Fischer 정리에 따라 $\mathcal{N}(\phi_k) \leq k$ ($k$-th eigenvector). 이 nodal count $n_k := \mathcal{N}(\phi_k)$ 를 SCC-intrinsic mode "principal quantum number" 로 정의.

**(b) 성공 시 산출물.** 모든 mode 에 정수 $n_k$ 가 부여된 분류표. R23 의 (mode index → angular label) 을 (mode index → $n_k$) 로 재라벨. atom 의 principal quantum number $n$ 와 **구조적 평행** 을 보이지만, value 는 일반적으로 다름 (atom 은 hydrogenic, SCC 는 shell-Schrödinger).

**(c) 실패 모드.**
1. **Nodal sign 모호.** $\phi_k(i) = 0$ 인 site 가 있을 때 어디에 할당할지 (positive / negative) 임의. 일반적 graph 에서 generic 하게 발생하지 않으나 highly symmetric minimizer 에서 occur 가능.
2. **Courant non-tight.** SCC Hessian = pure Laplacian + cl/sep 보정. 보정 항이 nodal ordering 을 흔들 수 있어 Courant tight (= n_k = k) 가 깨질 수 있음.
3. **Discreteness 의 정보 손실.** 같은 $n_k$ 를 갖는 두 모드가 다른 angular structure 를 가질 때 nodal count 만으로는 구분 불가 (irrep label 이 보완해야 함 → A1+A2 결합 필요).

**(d) Canonical 상호작용.** Prop 1.3a/b 가 mode-counting 을 다루지만 nodal domain count 는 canonical 에 부재. canonical §13 에 corollary 로 추가 가능.

---

### A3. Continuum PDE — shell-potential Schrödinger emergence

**(a) Idea.** $n \to \infty$ (continuum) limit 에서 SCC Hessian 의 leading 항이 $4\alpha(-\Delta) + V(r)$ 형태가 되고, $V(r) = \beta W''(u^*(r))/(4\alpha)$ 는 interface $r = r_0$ 근방에서 attractive shell well 을 형성. Radial-angular separation 에 의해 spectrum 이 $\{(n, \ell)\}$ 로 labeling 됨. $SO(2)$ rotational symmetry 가 continuum 에서 emergent. 유한 grid 에서 $D_4$ correction 이 ℓ=2/ℓ=6 mixing 등을 정량 설명.

**(b) 성공 시 산출물.**
- Continuum effective Hamiltonian closed form
- Spectrum 의 leading-order 값 (closed form 또는 ODE)
- $D_4$ perturbation 에 의한 splitting 의 small-parameter expansion

**(c) 실패 모드.**
1. **Continuum limit 에서 finite-graph 정보 손실.** 32×32 grid 의 lattice 효과가 lowest-order 에서 무시되면 mode ordering 예측 빗나감.
2. **Translation Goldstone 처리.** Continuum 의 $SO(2)$ symmetry 외에 $\mathbb{R}^2$ translation 이 있으면 zero mode 2개 추가; 이를 Σ_m 위 quotient 로 다루는 게 비-trivial.
3. **W''(u*) 의 spinodal 영역.** Interior $u^* > c_+$ 또는 $u^* < c_-$ 영역에서 $W'' < 0$, attractive 가 아니라 repulsive — well 구조가 역전됨.

**(d) Canonical 상호작용.** Cor 2.2 (interface scale, Cat A) 가 $u^*(r) \sim \tfrac{1}{2}(1 - \tanh((r-r_0)/\xi_0))$ 의 ansatz 를 제공하며, 본 접근은 그 ansatz 위 Hessian 의 spectrum 도출. canonical §13 의 새 corollary "Continuum spectral structure" 로 잠재 추가.

---

### A4. Equivariant bifurcation — secondary pitchforks from circular minimizer

**(a) Idea.** β 가 증가함에 따라 disk-like (1s) minimizer 가 secondary bifurcation 을 통해 unstable 해지고, equivariant Crandall-Rabinowitz 에 의해 새 orbital state 들이 분기. 각 bifurcation 의 분기 방향이 $D_4$ irrep 으로 indexed → 분기 tree 가 자동으로 orbital 분류를 생성. R22 의 cubic-coefficient 분석 (axis vs diagonal) 가 first pitchfork 에 대한 prototype 이며, 이를 secondary 로 확장.

**(b) 성공 시 산출물.** Bifurcation tree (β-축 위에 분기점들), 각 branch 에 isotropy subgroup 라벨, 각 critical β 에서의 cubic-coefficient sign.

**(c) 실패 모드.**
1. **분기 점근선이 catalog 를 채우지 못함.** Equivariant CR 은 bifurcation 직후의 local 정보만 줌. Far-from-criticality 에서의 stability 변화는 별도 분석 필요. 56 stable basins 중 다수가 saddle-node 등 non-pitchfork 로 출현했을 가능성.
2. **Disk minimizer 의 unstability 의 trigger 결정 어려움.** Disk → secondary 분기의 critical β 와 mode 가 disk 의 정확한 형태에 의존 (Cor 2.2 의 ansatz 는 leading 만).
3. **Multi-formation channel 의 분기.** Disk → bilobed (Mechanism A) vs disk → K=2 (Mechanism B) 의 분기 분리가 nontrivial.

**(d) Canonical 상호작용.** T-Birth-Parametric 는 uniform → first non-uniform 의 분기. A4 는 그 다음 단계 분기를 다룸. canonical 의 §13 에 "Secondary equivariant bifurcation tree" 항목으로 잠재 추가.

---

### A5. Frustration-theoretic — orbital as compromise of incompatible per-term ideal minimizers

**(a) Idea.** 4 energy term ($\mathcal{E}_\text{cl}, \mathcal{E}_\text{sep}, \mathcal{E}_\text{bd}, \mathcal{E}_\text{tr}$) 의 각각의 ideal minimizer (해당 term 만 활성화 시 최소) 가 서로 incompatible. Joint minimization 의 해는 compromise 이며, compromise 의 "spatial detail" 이 orbital structure. Frustration 양 $\mathcal{F}_\text{trs} := \min \mathcal{E} - \sum_i \lambda_i \min \mathcal{E}_i$ 이 orbital energy gap 의 lower bound 또는 scaling indicator. Closure 의 self-reference 가 single-disk 를 직접 destabilize → A-04 (F=1 removal) 에 대한 mechanism 적 설명.

**(b) 성공 시 산출물.**
- Per-term ideal minimizer 의 명시적 형태 ($u^*_\text{bd} = \chi_A$ for minimal-perimeter $A$; $u^*_\text{cl} = c^* \cdot \mathbf{1}$; $u^*_\text{sep}$ = checkerboard-like).
- $\mathcal{F}_\text{trs}$ 의 정의와 inequalities ($\mathcal{F}_\text{trs} \geq 0$, with equality iff per-term simultaneously minimizable — generally impossible).
- F=1 의 single-disk 가 cl+sep 의 동시 활성화 하에 saddle 임을 보이는 정리 (pre-objective theorem 의 한 형태).

**(c) 실패 모드.**
1. **Per-term 만 활성화 자체가 ill-defined.** $\lambda_i \to 0$ 극한에서 다른 항의 영향을 완전 제거하면 $\mathcal{E}_i$ 만 남지만, Σ_m constraint 와 호환 안 될 수 있음 (e.g. $\mathcal{E}_\text{sep}$ ideal 인 checkerboard 가 mass m 과 호환되지 않음).
2. **Compromise 의 spatial detail 결정 불가.** 일반적인 4-term variational 문제의 minimizer 의 정확한 형태는 closed form 없음.
3. **Quantitative gap 예측 부정확.** $\mathcal{F}_\text{trs}$ 가 orbital gap 의 scaling 을 줄지언정 정확한 값은 못 줌.

**(d) Canonical 상호작용.** CN5 (4-term independence) 가 frustration 개념의 axiomatic 근거. canonical §10 (structural interpretation) 에 frustration 으로서의 해석을 추가.

---

### A6. Axiomatic redraft — define formation identity by signature directly (S1' meta-level)

**(a) Idea.** 위 A1–A5 가 발견·증명할 객체를 어떻게 axiom 안에 짜 넣을지의 메타-접근. Axiom S1' 의 statement 자체를 "$\sigma(u^*)$ 가 formation identity 를 결정한다" 의 형태로 정립. Observable bridge 로 $K_\text{step}$ 등 기존 양과 σ 의 관계 명시.

**(b) 성공 시 산출물.**
- Axiom S1' v1 의 SCC-intrinsic statement
- Observable bridge 의 명시적 inequality 들
- 기존 axiom (A1', A2-A4, B-E, D-Ax) 와의 양립성 audit

**(c) 실패 모드.**
1. **Signature components 의 임의성.** $K$ ("lowest $K$ modes") 의 cutoff 가 자연스러운 spectral-dimension argument 없이 임의이면 S1' 자체가 ill-defined.
2. **Aut(G)-orbit identification 의 strength.** "up to Aut(G)" 가 너무 약하면 (different orbital configurations 이 동일 σ) 또는 너무 강하면 (overspecified) hospital.
3. **Observable bridge 가 inequality 만 (equality 없으면)** practical observable 로 사용 어려움.

**(d) Canonical 상호작용.** A6 가 새 axiom S1' 를 직접 도입. canonical §6 (axiom groups) 에 새 group "S" (Single-Formation Signature) 또는 §11 (fixed commitments) 의 항목 14 로 추가.

---

### A1–A6 의 mathematical independence audit

각 두 접근의 실패 모드와 사용 도구가 다름을 점검:

| 쌍 | 사용 도구 차이 | 실패 모드 차이 | 독립성 |
|---|---|---|---|
| A1 ↔ A2 | rep. theory vs spectral graph | trivial stabilizer (A1) vs nodal sign 모호 (A2) | 독립 |
| A1 ↔ A3 | discrete group rep vs continuum PDE | finite group dim 한계 (A1) vs continuum 근사오차 (A3) | 독립 |
| A1 ↔ A4 | equivariant decomposition (static) vs equivariant bifurcation (dynamic) | non-symmetric minimizer (A1) vs far-from-criticality (A4) | 부분 독립 (둘 다 group rep 이용하나 정적 vs 동적) |
| A2 ↔ A3 | combinatorial vs analytical | nodal degeneracy (A2) vs continuum boundary 처리 (A3) | 독립 |
| A2 ↔ A4 | spectral counting vs bifurcation tree | ordering 변화 (A2) vs 분기 외 minimizer 누락 (A4) | 독립 |
| A3 ↔ A4 | spectral PDE vs bifurcation theory | continuum effect (A3) vs branch tracking (A4) | 부분 독립 (둘 다 분석학 사용; 그러나 prediction target 다름: A3 = spectrum, A4 = catalog) |
| A5 ↔ {A1..A4} | variational decomposition (energy budget) vs spectral 도구 | 주어진 minimizer 의 분류가 아닌, **존재 자체의 mechanism** 설명 | 독립 (다른 prediction 종류) |
| A6 | meta-axiomatic | A1..A5 의 산출물에 의존 | 종속 (A1..A5 의 합성) |

→ A1, A2, A3, A4, A5 는 사실상 5 개 독립 접근. A6 는 메타-합성으로 분리.

---

## §3. Primary selection rationale

### 3.1 후보 비교 매트릭스

각 접근을 (i) Cat A 도달 가능성, (ii) R23 데이터와의 직접 연결, (iii) 새 falsifiable 예측 생성 능력, (iv) canonical 통합 단순성, 4 차원으로 평가.

| 접근 | (i) Cat A 가능성 | (ii) R23 연결 | (iii) 새 예측 | (iv) 통합 | 점수 |
|---|---|---|---|---|---|
| A1 (irrep) | High (group rep theory 는 finite finite case 에서 well-defined) | High (R23 angular multipole 이 irrep proxy) | Medium (translation Goldstone 분리 후 atom-vs-SCC 차이 예측) | Easy (canonical T-Birth-Parametric 와 호환) | **10** |
| A2 (nodal) | High (Courant 정리 사용) | Medium (R23 에는 nodal count 없음 — 새 측정 필요) | High (Courant tight fraction 자체가 예측 + irrep × nodal 의 product 라벨) | Easy (Prop 1.3a 의 corollary) | **9** |
| A3 (continuum) | Medium-Low (continuum 에서 Cat A 가능, 그러나 finite grid 에서는 Cat B/C) | Medium (continuum 예측이 finite grid 과 부합하는지 별도 작업) | High (closed-form spectrum, $D_4$ correction 양적) | Medium (canonical Cor 2.2 와 부합하나 새 §추가 필요) | **7** |
| A4 (bifurcation) | Medium (CR 은 bifurcation 직후 만 Cat A) | Low (R23 data 는 minimizer catalog; 분기 정보 추출에 별도 numerics) | Medium-High (분기 점 예측) | Medium (T-Birth-Parametric 의 자연 후속) | **6** |
| A5 (frustration) | Low-Medium (qualitative 로는 Cat A 가능, quantitative 는 Cat B/C) | High (A-04 F=1 removal 의 mechanism 설명) | Medium (gap scaling 예측만) | Easy (CN5 의 자연 corollary) | **7** |
| A6 (axiomatic) | n/a (정의이므로 Cat 분류 불가; consistency audit 만) | High (R23 의 모든 데이터를 σ 로 재라벨) | n/a (정의는 예측 안 함) | High (canonical 의 새 axiom group) | **(메타)** |

### 3.2 결정

**Primary = A1 + A2 결합 (irrep × nodal product label) + A6 메타-합성으로 σ 정의**.

이유:
- A1+A2 는 둘 다 graph-intrinsic 이고 finite case 에서 Cat A 가능.
- A1 의 한계 (trivial stabilizer 시 vacuous label) 를 A2 가 보완 (nodal count 는 항상 정의됨).
- A2 의 한계 (같은 nodal count 의 두 mode 구분 안 됨) 를 A1 이 보완 (irrep 라벨로 구분).
- 둘 모두 R23 의 Hessian eigenmode 를 동일 데이터에서 추출 가능 → 추가 실험 무필요 (plan.md non-goal 준수).
- A6 가 A1+A2 의 산출을 axiom S1' 의 statement 안에 짜 넣음.

**Supporting = A3 (continuum)**. 단, 오늘은 A1+A2 의 정의가 main; A3 은 motivation 및 "왜 ℓ=2 가 first excited 인가" 에 대한 explanatory account 로만 사용. 정확한 spectrum 도출은 §02 §5 에 sketched 수준.

**Preserved alternatives**:
- **A4 (bifurcation)** — 후속 세션 (e.g. 2026-04-25 또는 W5) 에서 56 stable basin 의 분기 mapping 수행 시 활성화. 오늘 배제 이유: R23 데이터가 분기 정보를 직접 주지 못함 (각 minimizer 의 출현 분기 점은 별도 사다리 numerics 필요).
- **A5 (frustration)** — pre-objective theorem (오늘 §02 §6) 의 backbone 에 부분 사용. 더 정량적 frustration quantification (gap scaling $\sim \mathcal{F}_\text{trs}$) 은 후속.

### 3.3 보존된 대안의 부차성 명시

**왜 A4 가 부차적인가**: R23 의 stable basin catalog 은 정적 (minimizer 단위) 이지 동적 (분기 mapping) 이 아님. A4 는 동적 정보가 필요. 후속 세션에서 β-cascade 실험을 추가로 수행하면 활성화 가치가 큼.

**왜 A5 가 부차적인가**: A5 는 mechanism 설명에 강하나 catalog 분류에는 약함. Catalog 분류는 σ-정의 (A1+A2+A6) 가 일차적으로 처리. A5 는 §02 §6 의 pre-objective theorem 에서 부분 사용되며, 그 이상 깊이 들어가면 quantitative 예측이 Cat B/C 에 머물러 오늘의 Cat A 승급 목표와 맞지 않음.

**왜 A3 가 supporting 인가**: A3 는 closed-form 예측에서 강하나 Cat A 도달이 finite grid 에서 어려움. 따라서 §02 의 Cat A primary 자리에는 A1+A2 가 들어가고, A3 는 "explanatory backbone + 한 corollary" 로 §02 §5 에 등장.

---

## §4. 다음 파일 (`02_development.md`) 의 구조 사전 통지

`02_development.md` 는 다음 순서로 전개:

§1. **Setup**: graph-intrinsic 객체의 명시 (Aut(G), Stab, T_{u}Σ_m, Hessian definition with constraint)
§2. **Definition (Cohesion Signature σ)** — A6 의 axiomatic 정의
§3. **Lemma 1 (Irrep decomposition well-defined)** — A1 의 핵심
§4. **Lemma 2 (Nodal count is graph-intrinsic and Aut(G)-equivariant)** — A2 의 핵심
§5. **Theorem 1 (Mode-0 reinterpretation as translation Goldstone)** — H3 의 처리, A-01 statement 수정 정당화
§6. **Theorem 2 (Pre-objective structure: closure removes F=1 stable minimizer)** — A-04 의 mechanism 적 정리. A5 부분 사용. Cat C scoping (조건 의존).
§7. **Continuum limit corollary (A3 sketch)** — 왜 ℓ=2 가 first excited (조건부, non-translation 한정)
§8. **Falsification attempts** — σ-정의에 대한 명시적 counterexample 시도
§9. **Self-classification** — 각 결과의 Cat A/B/C/conjecture 자기 평가

§02 의 실 추정 길이: 700–900 lines.

---

## §5. 이 파일의 자기 평가

- §4.1 Restatement: target 재진술 + 7 개 암묵 가정 표면화 ✓
- §4.2 Multi-approach: 5 개 mathematically independent approach 생성 (A1–A5), 1 개 메타 (A6); 독립성 audit 표 ✓
- §4.3 Primary selection: 점수 매트릭스 + 결정 + 보존 대안의 부차성 ✓
- 모든 접근의 실패 모드 명시 ✓
- 후속 파일의 구조 통지 ✓

다음 파일에서 이행할 것: definitions, lemmas, proofs, counterexample attempts, self-classification.
