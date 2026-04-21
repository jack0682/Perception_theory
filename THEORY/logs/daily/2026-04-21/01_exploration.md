# 01 — Exploration: Restatement, Multi-Approach, Primary Selection

**Session:** 2026-04-21
**Target (from plan.md):** Stage 1 (Definition Foundation) — C+E 공통 첫 세션. **K_soft 정의 commit + F-group 공리 F1–F2 + 교차 객체 ℱ_C+E[u] = ℰ[u] − T·S[u] + λ_K·K_soft(u) well-definedness 확립 + F-1/M-1/MO-1 세 Critical 의 C+E dissolution mapping pre-draft (1~2 페이지 each).**
**This file covers:** 문제 재진술 (§1), 다중 접근 (§2 — 5 후보), Primary 선택 근거 (§3), 작업 순서 및 dependency (§4), 자기 점검 표 (§5).
**Depends on reading:** `plan.md`, `pre_brainstorm.md` (§A–§J), `canonical.md` §3 / §6 / §8 / §11 / §12 / §13 / §14 (특히 CN5/CN6/CN8/CN10/CN12/CN14), `working/open_problems_reframing_2026-04-19.md` §6 (P-A/P-D/P-F/P-G), `working/integer_K_dependency_map.md` §2, `working/new_open_questions_2026-04-20.md` (NQ-1, NQ-3), `canonical/canonical_sub.md` 2026-04-20 entry, `working/reformulation_purpose.md`.

---

## §1. Restatement of the Plan Target

### 1.1 무엇이 물음인가 (4 layered question)

오늘 세션은 **단일 이론적 질문 4 개를 동시에 토대 수준에서 commit**하는 것을 요구한다. 네 질문은 **선후 관계** 가 있다:

**Q-1 (precondition).** `K_soft : Σ_m → ℝ_{≥0}` 라는 derived 양을 어떻게 정의할 것인가? 정의는 (a) `u`-의 연속함수, (b) 기존 canonical §5.5 의 H₀ persistence 사용 패턴과 호환, (c) Σ_m 위에서 well-defined, (d) `K_hard ∈ ℕ` (canonical 의 integer K) 의 자연스러운 grade를 생산해야 한다.

**Q-2 (foundation).** **온도 T 와 엔트로피 S 를 도입하는 새 공리군 F-group (F1–F4)** 을 어떤 형태로 둘 것인가? F1–F2 는 commit (well-definedness 포함), F3–F4 는 statement 수준만.

**Q-3 (cross-object).** 위 둘을 합친 **자유에너지** 

$$
\mathcal{F}_{\mathrm{C+E}}[u] \;=\; \mathcal{E}[u] \;-\; T\cdot S[u] \;+\; \lambda_K \cdot K_{\mathrm{soft}}(u)
$$

이 (a) Σ_m 위에서 well-defined (Lipschitz, lower semicontinuous, coercive), (b) 최소화 가능 (Weierstrass), (c) 기존 ℰ 의 minimizer 구조와 양립 가능한가? 그리고 λ_K 의 자연 scale 은 무엇인가?

**Q-4 (dissolution).** 위 토대 위에서 1년간 고착된 세 Critical (F-1: K=2 vacuity, M-1: K=1 always preferred, MO-1: smooth Morse inapplicable) 이 어떻게 **dissolve** (사라지는가, 아니면 다른 문제로 변환되는가)? "Dissolve" 는 silent resolution 이 아니라 **재언어화 (re-phrasing) + 잔여물 명시** 를 의미한다.

### 1.2 무엇이 데이터인가 (입력)

세션이 의존하는 사전 자료:

- **canonical.md v1.2** §3 (formal universe), §5.5 (Q_morph 의 H_0 persistence), §6 (Group A–E), §8 (energy on Σ_m), §11 (fixed commitments — 특히 CN5 four-term 독립성, CN12 persistence-based morphology), §12 (multi-formation kinetic narrative), §13 (정리 카탈로그 — 특히 Cat A/B/C 분류, Retracted T-Merge (c)(d)(e)), §14 (CN6/CN8/CN14 — kinetic/metastability 관련 commitments).
- **working/open_problems_reframing_2026-04-19.md** §6 의 P-A/P-D/P-F/P-G, §8 의 N-1 single-source thesis.
- **working/integer_K_dependency_map.md** 의 9+1 정리 목록 (Retire 6 + Re-prove 3 + Re-prove(retain) 1).
- **working/new_open_questions_2026-04-20.md** NQ-1 (soft-K uniqueness), NQ-3 (vineyard 대체).
- **canonical_sub.md 2026-04-20 entry** — 직전 세션의 Clarified/Pending 누적, 본 세션이 append 할 자리.
- **pre_brainstorm.md** 의 104 가설 (특히 §A 10 개, §B 20 개, §C 10 개, §D 8 개, §E 14 개, §F 14 개, §G 7 개, §H 11 개, §I priority mapping).
- **외부 정리:** Cohen-Steiner–Edelsbrunner–Harer (2007) bottleneck stability of persistence diagrams; Modica-Mortola (1977) Γ-convergence; Witten (1982), Simon (1985), Helffer-Sjöstrand (1985) Witten Laplacian semiclassics; Kramers (1940), Eyring (1935) escape rates; Da Prato-Zabczyk (Stochastic Equations in Infinite Dimensions) for projected SDE.

### 1.3 무엇이 성공인가 / 실패인가

**성공:** plan.md §Success criterion. 6 working 파일 (G1–G6) 모두 존재 + canonical_sub.md 2026-04-21 entry append + 3 working 디렉토리 (E/, C/, CE/) 신설. 우선순위 규칙: G1·G2·G3 필수 (Stage 1 토대), G5·G6 필수 (각 Critical 의 묵직한 dissolution), G4 는 시간 부족 시 후순위 carry 가능.

**실패 (dissolution 의 의미 오인):** 세 Critical 중 어느 것이라도 silent resolution. 특히:
- (a) F-1 을 "이제 해결됨" 으로 선언 — 잔여물 (소프트-K distribution 의 volume m 의존성) 명시 안 함.
- (b) M-1 의 isoperimetric ordering 정리 자체를 retract — 이는 proved 정리이며 "문제" 가 아니라 "기존 framing 의 prejudice" 이다 (reframing §9 참조). M-1 의 dissolve 는 정리 자체의 부정이 아니라 **framing 의 부정**.
- (c) MO-1 의 corner 가 Witten Laplacian 으로 "완전 해결" 되었다는 주장 — 실제로는 (i) 코너가 사라지는 부분 (E 측면, soft-K interior smooth 화) 과 (ii) 새 도구 도입 부분 (C 측면, Witten/Fokker-Planck) 두 layer 의 합성이며, **둘 다 완료까지는 Stage 1 + 2 + 3** 이 필요.

**실패 (수학적 엄밀성 부족):**
- K_soft 의 Lipschitz 골격에 외부 정리 (CSEH 2007) 의 진술/적용이 명시 anchor 되지 않음.
- F-group 공리에서 Σ_m 위 Gibbs measure 의 normalizability 가 단순 "compact 이므로 자명" 으로 처리되고 boundary behavior (u_i = 0 또는 1 인 corner) 의 entropy 발산 처리 누락.
- λ_K scaling 논증이 dimensional analysis 없이 hand-waved.

### 1.4 사용자가 plan.md 에서 암묵적으로 둔 가정 (수면 위로 끌어올림)

plan.md §"잠정 직감" 1~5 와 §Q1~Q4 를 검토하면 다음 4 개 가정이 작동:

1. **A1 (Persistence canonical):** Soft-K 의 4 후보 중 (i) persistence weighted sum 이 commit 대상. NQ-1 의 (ii)(iii)(iv) 는 parking. 본 세션은 이 direction 을 **default** 로 받되 §3 에서 alternative direction 을 명시 보존.
2. **A2 (Standard stat mech overlay):** F1–F2 가 standard Bernoulli 엔트로피 + Gibbs measure 라는 가정. 이는 SCC 의 4 에너지 항이 thermal 확장에 well-suited 라는 _기대_ 를 전제. 실제로는 E_sep 의 자가참조성 (§8.3 의 D_t(x; 1−u)) 이 Gibbs 의 standard normalization 과 어떻게 양립하는지가 별도 검증 대상.
3. **A3 (λ_K ~ T natural):** plan.md §3 의 잠정 직감. 본 세션은 이 가정을 **하나의 합리적 선택** 으로 분석하되 alternative scaling (O(1) T-independent, O(β) low-T dominant) 를 §3 (G3) 에서 보존.
4. **A4 (3 Critical = single source):** N-1 single-root thesis (`open_problems_reframing_2026-04-19.md` §8). 본 세션은 이를 **working hypothesis** 로 받되 dissolution 후의 **잔여 비대칭** (residual asymmetry between F-1, M-1, MO-1 dissolutions) 을 §G4–G6 에서 명시.

---

## §2. Multi-Approach (수학적으로 독립인 5 후보)

같은 plan target 에 도달하는 서로 다른 수학적 경로 5 개를 제시한다. **각 후보는 (a) 핵심 아이디어, (b) 성공시 산출물 형태, (c) 실패 모드, (d) 기존 정리/공리와의 상호작용** 을 명시한다. 후보 간 독립성 자기 점검은 §2.6.

### 2.1 Approach P1 — Persistence-Bottleneck (CSEH stability) + Standard Gibbs

**핵심 아이디어.** Soft-K 의 정의에 H₀ persistence 의 weighted bar-length sum 을 commit (`K_pers(u) = Σᵢ φ(ℓᵢ)`, φ monotone Lipschitz). well-definedness 의 핵심은 Cohen-Steiner–Edelsbrunner–Harer (2007) 의 **bottleneck stability theorem**:

$$
W_\infty\!\big(\mathrm{Dgm}(u),\,\mathrm{Dgm}(v)\big) \;\leq\; \|u - v\|_\infty.
$$

φ 의 Lipschitz 성과 결합하여 `K_pers : (Σ_m, ‖·‖_∞) → ℝ_{≥0}` 가 Lipschitz. 이 위에 standard Gibbs `ℙ ∝ exp(−ℱ/T)` 와 standard Bernoulli 엔트로피 `S[u] = −Σ[u log u + (1−u) log(1−u)]` 를 layered overlay 로 추가.

**성공시 산출물.** (a) K_soft 의 closed-form 정의 + Lipschitz constant 의 explicit bound (`L_K ≤ L_φ`). (b) F1–F2 commit + ℱ_C+E 의 Σ_m 위 Lipschitz·coercivity·minimizer 존재. (c) 세 dissolution mapping (G4–G6) 이 표준 stat-mech 도구 (Boltzmann factor, Kramers rate, Witten Laplacian) 로 1~2 페이지 pre-draft.

**실패 모드.** (i) **Vineyard discontinuity:** persistence diagram 은 generic u 에서 stable 하나 bar birth/death 순간에 jump 가능. K_pers 의 Lipschitz 는 generic set 에서만; non-generic codimension-1 set 위에서 jump → integration / variational analysis 시 measure-zero exceptional set 처리 추가 필요. (ii) **Volume constraint 와 K_soft 의 호환성:** Σ_m 위 정의역이 K_pers 의 sublevel set / superlevel set 과 어떻게 교차하는가 — 본 세션 G1 §Volume compatibility 단락에서 예비 검토. (iii) **Gibbs normalizability at corner:** Σ_m 의 corner (u_i ∈ {0, 1}) 에서 Bernoulli 엔트로피 `u log u → 0` 은 finite 하지만 entropy gradient 가 발산 — projected gradient flow (F3 Langevin) 의 well-posedness 가 corner 처리 별도.

**기존 정리/공리와의 상호작용.**
- canonical §5.5 의 ℓ_max (Q_morph 정의의 최장 bar) 는 K_pers 의 special case (φ(ℓ) = ℓ · 1_{ℓ = ℓ_max}) — 기존 Q_morph 의 Lipschitz (T11 도구) 가 자연스럽게 generalize.
- canonical §13 Cat A 의 QM3 (Q_morph 의 continuity in u via persistence stability) 가 K_pers 의 continuity 와 동일 도구 사용.
- §6 Group F (신설) 가 §6 Group A–E 와 layer 분리 (CN4 의 "Group F architecturally distinct from A–E" 의 자연 일반화 — 단 CN4 는 crisp recovery 의 Group F 이므로 이름 충돌; 본 세션의 F-group (thermal) 은 다른 ontological layer).

### 2.2 Approach P2 — Betti Integral + Modica-Mortola Sharp-Interface

**핵심 아이디어.** Soft-K 를 H₀ persistence 가 아니라 **superlevel Betti integral** 로 정의:

$$
K_{\mathrm{Betti}}(u) \;=\; \int_0^1 \beta_0\!\big(\{x : u(x) \geq \theta\}\big)\, d\theta.
$$

Modica-Mortola (1977) 의 Γ-convergence 에서 ε → 0 극한의 perimeter functional 이 sharp-interface 한계를 제공 — 이 한계에서 superlevel set 의 connected component 수가 자연 정수화. 따라서 K_Betti 는 sharp limit 에서 standard hard count 와 일치, finite ε 에서는 graded.

엔트로피와 Gibbs 는 Approach P1 과 동일한 standard form.

**성공시 산출물.** (a) K_Betti 의 정의 + Lipschitz (Fubini + persistence stability). (b) Modica-Mortola 와의 Γ-conv consistency 증명 sketch — soft-K 가 sharp-K 의 변분적 grade 임을 보이는 단락. (c) M-1 의 isoperimetric 부분 (G5) 이 Modica-Mortola 골격 위에서 자연 — "single-mode preference 는 perimeter minimization 의 귀결" 이 한 줄 인용으로.

**실패 모드.** (i) K_Betti = K_pers 의 동치 여부 (pre_brainstorm H-A2): φ(ℓ) = ℓ 일 때 Fubini-on-filtration 으로 동치. 이 동치가 일반 φ 로 확장 안 됨 → P1 보다 정의 자유도가 좁음. (ii) Sharp-interface limit 은 실제로는 ε = α/β → 0 — 본 세션의 working point (β finite, α finite) 에서 직접 적용 안 됨. Connection 이 **interpretation** 수준으로 격하.

**기존 정리/공리와의 상호작용.** canonical §13 Cat A 의 T11 (Γ-convergence) 와 직접 호환. T-Merge (b) (Energy ordering, isoperimetric) 의 증명 핵심을 그대로 재활용 (working/integer_K_dependency_map.md §2.2 의 "Re-prove (retain)" 1 개).

### 2.3 Approach P3 — Witten Laplacian (Helffer-Sjöstrand) Spectral Approach

**핵심 아이디어.** 정의 layer 자체는 P1 (또는 P2) 와 동일하게 시작하되, **존재론적 무게중심을 Witten Laplacian 의 spectrum 에 둠**. Free energy `ℱ_C+E[u]` 의 Witten 변형:

$$
\Delta_{\mathcal{F}, T} \;=\; -T\,\Delta + \frac{1}{T}\|\nabla \mathcal{F}\|^2 - \Delta \mathcal{F}.
$$

Helffer-Sjöstrand (1985) 의 semiclassical analysis: T → 0 에서 Witten Laplacian 의 small eigenvalues 가 critical points of ℱ 와 1-1 대응 (Morse-theoretic). 이 spectrum 이 Kramers escape rates 를 직접 encode.

세 Critical 의 dissolution 을 **모두 spectral language** 로 수행: F-1 = Z_K partition over critical points, M-1 = Kramers gap = small eigenvalue, MO-1 = Witten Laplacian 자체가 Morse 의 spectral 대안.

**성공시 산출물.** (a) ℱ_C+E 의 Witten Laplacian 정의 (statement only — full spectrum 분석은 post-Stage-1). (b) F-1 / M-1 / MO-1 dissolution 이 단일 도구 (Witten Laplacian) 로 통일. (c) MO-1 dissolution (G6) 이 가장 자연.

**실패 모드.** (i) **Discrete graph 위 Witten Laplacian:** Witten 의 원래 framework 는 smooth manifold 위. Discrete graph 에서는 Forman discrete Morse (Forman 2002) 또는 graph Witten Laplacian (Sunada 등) 의 finite-dim 변형 필요. 이 변형의 H-S 스펙트럼 이론은 standard 하지만 본 세션 1 일에 완전 sketch 불가 — statement only 로 격하. (ii) **Σ_m 의 boundary 처리:** Witten Laplacian 은 closed manifold 또는 boundary condition 명시 필요. Σ_m 의 corner (u_i ∈ {0,1}) 에서 Neumann/Dirichlet 선택이 free energy boundary value 와 정합되어야 함 — 별도 검증.

**기존 정리/공리와의 상호작용.** canonical §13 Cat C 의 T-Persist-K-Sep/Weak/Unified 가 Witten Laplacian 의 small eigenvalue gap 으로 unified statement 가능 — long-term roadmap. 단기적으로 본 세션은 statement only.

### 2.4 Approach P4 — Free-Energy-First (KL Divergence + Effective K via Entropy)

**핵심 아이디어.** Soft-K 의 정의를 persistence 가 아니라 **entropy-based effective number** 로 commit:

$$
K_{\mathrm{eff}}(u) \;=\; \exp\!\big(H(u)\big), \qquad H(u) = -\sum_x p(x)\log p(x), \quad p(x) = u(x)/m.
$$

(이는 Hill 의 Hill number, 또는 ecology 의 effective species number 의 변형). K_eff 는 단일 mode 의 완전 집중 (`u = m·δ_{x_0}` 형) 에서 K_eff = 1, uniform 분포에서 K_eff = n. SCC 의 ontological framing (u 가 distribution-like) 과 가장 호환.

이 정의는 NQ-1 의 후보 (iii) (simplex-valued) 의 변형. F-group 공리 F2 (Bernoulli entropy) 와 K_eff (Shannon entropy of normalized u) 가 동일 수학적 source — F-group + K-soft 가 한 ontological layer 에서 통합.

**성공시 산출물.** (a) K_eff 정의 + Lipschitz (단, u_i = 0 근처에서 entropy 가 발산하지 않도록 ε-regularization 필요). (b) F-group 의 entropy S 와 K_eff 가 같은 layer → ℱ_C+E 의 단순화. (c) 세 dissolution 이 **information-theoretic argument** 로 통일.

**실패 모드.** (i) **K_eff 와 H₀ persistence 의 disconnect:** canonical §5.5 가 이미 H₀ persistence 사용 (CN12 "Q_morph is persistence-based"). K_eff 로의 전환은 CN12 retract → canonical 에 큰 충격. 본 cycle 의 Non-goal (canonical 직접 수정 금지) 와 충돌. (ii) **Spatial structure 손실:** K_eff 는 spatial coordinates 무시 (u 의 공간분포는 entropy 에 안 들어감). SCC 의 핵심인 "공간적 cohesion" 이 K_eff 에 보이지 않음 → 정보 손실.

**기존 정리/공리와의 상호작용.** CN12 (persistence-based morphology commitment) 와 직접 충돌. canonical §13 의 QM 정리들이 K_eff 와 호환되지 않을 가능성. **부적합한 후보** — §3 에서 보존하되 primary 아님.

### 2.5 Approach P5 — Forman Discrete Morse Theory (Combinatorial)

**핵심 아이디어.** smooth Morse / Witten Laplacian 의 **discrete combinatorial 대안**. Forman (1998, 2002) 의 discrete Morse theory 는 finite simplicial complex 위에서 직접 작동. K_soft 정의는 P1 (persistence) 또는 P2 (Betti) 사용하되, MO-1 의 dissolution (G6) 의 **수학적 도구** 를 Witten 대신 Forman 으로 commit.

Forman 의 framework: simplicial complex `Σ` 위에 discrete vector field `V` 가 매칭 (matching) 정의. critical cells 가 standard Morse 의 critical points 역할. Morse inequalities 가 그대로 성립: `c_k ≥ b_k(Σ)`.

**성공시 산출물.** (a) Σ_m 의 cell complex 구조 위 discrete Morse 분석. (b) MO-1 dissolution (G6) 이 corner-aware (i.e., 코너 자체를 제거하지 않고 corner cells 를 critical cells 로 처리 가능). (c) Σ_m 의 simplex-edge 에서의 stratification 이 Forman framework 에서 자연.

**실패 모드.** (i) **Continuous u 와 discrete cells 의 호환:** SCC 의 u 는 X_t 위 continuous-valued. Σ_m 자체는 convex polytope (Cat A Proposition 1.1) — manifold with corners. Forman 은 simplicial complex 위 정의 — Σ_m 을 simplicial decomposition 으로 처리해야 함. 가능하나 본 세션 1 일에 sketch 부담. (ii) **Spectral information 손실:** Forman 은 combinatorial — Kramers escape rate 같은 quantitative spectral 정보 직접 회수 안 됨. M-1 dissolution (G5) 의 Kramers 부분이 Forman 으로는 약함.

**기존 정리/공리와의 상호작용.** canonical 과의 직접 충돌 없음 (Forman 은 새 도구 도입). 단 M-1 의 Kramers 부분에서는 Witten 이 더 강력 → P3 와 결합 가능 (P5 = MO-1 도구, P3 = M-1 도구).

### 2.6 후보 간 독립성 자기 점검

수학적 독립성, 실패 모드 차이, 조건부 성공 조건 차이의 3 기준에 따라 5 후보를 매트릭스화한다.

| 후보 | 핵심 도구 | 실패 모드 (가장 결정적) | 조건부 성공 조건 |
|---|---|---|---|
| **P1** Persistence + Gibbs | CSEH 2007 bottleneck + standard Gibbs | Vineyard discontinuity (codim-1 exception set) | φ Lipschitz, ε > 0 (corner reg) |
| **P2** Betti + Modica-Mortola | Fubini + Γ-conv (Modica-Mortola) | ε = α/β → 0 한계 (현 working point 에서 indirect) | β/α large (sharp-interface regime) |
| **P3** Witten Laplacian | H-S 1985 semiclassical | Discrete graph 위 Witten 의 finite-dim 처리 | T → 0 (semiclassical), discrete-vs-smooth bridge |
| **P4** K_eff (entropy) | Shannon H + Hill number | CN12 retract 충돌 (spatial info loss) | ε-regularization (u > 0) |
| **P5** Forman discrete Morse | Combinatorial matching | Spectral info loss (Kramers 약함) | Σ_m simplicial decomposition |

**5 후보 간 독립성 확인:**

- **P1 vs P2:** φ(ℓ) = ℓ 일 때 동치 (H-A2). 일반 φ 에서 P1 ⊋ P2. 부분 독립 (P1 이 더 일반).
- **P1 vs P3:** P1 은 정의 layer, P3 는 spectral layer. 정의는 P1 사용하고 분석을 P3 로 — 가능. **두 layer 가 직교** → 독립.
- **P1 vs P4:** 정의 자체가 다름 (persistence vs entropy). 충돌 (CN12).
- **P3 vs P5:** smooth (Witten) vs discrete (Forman). 같은 ontological 도구의 두 표현 — 부분 동치, 부분 독립 (spectral vs combinatorial). 결합 가능.
- **P4 vs others:** P4 가 가장 outlier. CN12 retract 가 cycle-internal Non-goal.

→ **수학적으로 독립 + 본 세션에 동시 사용 가능:** P1 (정의 + F-group + ℱ_C+E foundation) + P3 (G6 의 Witten 도구) + P5 (G6 의 alternative 도구로 보존) + P2 (G5 의 isoperimetric 부분 reuse). P4 는 §3 에서 alternative direction 으로 명시 보존하되 본 세션 직접 사용 안 함.

---

## §3. Primary Selection + Alternative Preservation

### 3.1 Primary 선택: P1 (정의) + P3 (G6 도구) + P2 (G5 isoperimetric reuse)

**선택 근거 (3 항):**

1. **Canonical 과의 minimal disruption.** P1 (persistence weighted sum) 은 canonical §5.5 의 H_0 persistence 사용 패턴 (CN12 commitment) 의 자연 확장. CN12 retract 불요. QM3 (Q_morph continuity) 의 도구가 K_pers 에 그대로 적용. 9+1 정리 목록 (working/integer_K_dependency_map.md §2) 의 Re-prove 3 / Re-prove(retain) 1 분류를 그대로 inherit.

2. **세 dissolution 의 도구 분배 자연.** 
   - **F-1 (G4):** Standard Gibbs partition Z_K 가 K_pers ≈ K 의 distribution regime 에 직접 적용. 추가 도구 불요. **P1 only**.
   - **M-1 (G5):** Isoperimetric 부분 (single-mode preference) 이 Modica-Mortola Γ-conv 로 자연 (P2 의 도구 reuse, 이는 canonical T-Merge (b) 의 증명 핵심). Kramers 부분은 standard 도구. **P1 + P2 (isoperimetric reuse)**.
   - **MO-1 (G6):** Witten Laplacian 이 가장 강력 (small eigenvalue ↔ critical point). Forman 은 alternative 로 보존. **P1 + P3**.

3. **plan.md 사용자 직감과 정합.** plan.md §"잠정 직감" 1 (persistence canonical), 4 (Kramers 도입), 5 (Witten Laplacian for MO-1) 가 모두 P1 + P3 조합과 일치. 사용자의 의도 오독 risk 최소.

### 3.2 Alternative Preservation (왜 부차적인가, 그리고 언제 활성화될 수 있는가)

다음 alternative 는 본 세션 직접 사용 안 하되 후속 세션의 활성화 후보로 보존:

- **P4 (K_eff entropy-based):** CN12 retract 가 충돌. 단 NQ-1 의 후보 (iii) 의 본질이 P4 → NQ-1 의 사후 비교에서 재등장 예정. 활성화 조건: CN12 의 weakening 에 사용자 동의 시.
- **P5 (Forman discrete Morse):** MO-1 dissolution 의 alternative 도구. Witten Laplacian 의 discrete graph 처리가 어려운 것으로 판명되면 P5 가 fallback. 활성화 조건: G6 의 Witten Laplacian 골격이 finite-dim 호환 안 되면.
- **P2 (Betti integral) 단독:** 본 세션은 P1 의 isoperimetric 부분에 대해 P2 의 도구만 reuse. P2 가 K_soft 정의 자체로 격상되는 경우는 P1 의 vineyard discontinuity 가 critical 한 것으로 판명되면 (Fubini 가 codim-1 exception 을 자동 처리하므로 P2 가 더 robust 한 정의 가능성).

### 3.3 Primary 의 단점에 대한 사전 인정

P1 + P3 + (P2 reuse) 조합에 본질적 약점:

- **Vineyard discontinuity.** P1 의 K_pers 가 codim-1 exception set 위에서 Lipschitz 가 깨짐 — gradient flow 분석시 measure-zero 처리 / smoothing 이 카드. 본 세션 G1 의 Lipschitz 골격은 generic Lipschitz; full statement 는 NQ-3 (vineyard 대체) 에 link.
- **Witten Laplacian 의 finite-dim 처리.** P3 의 Witten 은 본래 smooth setting. Discrete graph 위에서는 graph Witten Laplacian (Forman, Sunada, others) 의 변형 — 본 세션은 statement only 로 처리하고 finite-dim 호환 증명을 C-S2 (Stage 1 둘째 또는 Stage 2) carry.
- **세 dissolution 이 _서로 다른_ 도구 조합.** F-1 = Gibbs only, M-1 = Gibbs + Γ-conv + Kramers, MO-1 = Witten + Forman alternative. 통일된 single tool 부재 — 이는 plan.md 의 "C+E dissolution _이중화_" 에 부합 (E = isoperimetric/soft-K, C = thermal/spectral) 하나, "단일 framework" 이라는 미적 통일성 손실.

---

## §4. 작업 순서 및 Dependency

### 4.1 작업 단위 (G1–G6 + 4 코어 파일) 의 의존 그래프

```
                          [01_exploration.md] (본 파일)
                                    │
                                    ▼
  ┌──────────────────────────────────────────────────────┐
  │  G1 working/E/soft_K_definition.md  (K_pers 정의 + Lipschitz) │
  │  G2 working/C/F_group_axioms.md     (F1–F2 commit, F3–F4 draft) │
  └──────────────────────────────────────────────────────┘
                         │             │
                         ▼             ▼
            G3 working/CE/free_energy_wellposed.md
            (ℱ_C+E Lipschitz · coercivity · minimizer)
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
  G5 M1_dissolution  G6 MO1_dissolution  G4 F1_dissolution
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
              [02_development.md] (수학적 본체)
                           │
                           ▼
       [03_integration_and_new_open.md] + canonical_sub.md entry
                           │
                           ▼
                   [99_summary.md]
```

**핵심 의존:**
- G1 + G2 → G3 (G3 는 G1 의 K_soft 정의와 G2 의 F1–F2 가 모두 필요).
- G3 → G4–G6 (각 dissolution 이 ℱ_C+E 위에서 작성).
- G4–G6 → 02_development.md (수학적 본체는 G1–G6 의 증명/sketch 를 통합 정리).
- 02 → 03 (integration 은 substantive 산출이 있은 후에만 의미).
- 03 → 99 (summary 는 전체 산출이 끝난 후).

**본 세션의 직렬화 (시간 순):**
1. (완료) `01_exploration.md` 본 파일.
2. G1 → G2 → G3 (foundation, 약 4–5h 추정).
3. G5 → G6 → G4 (priority order — G4 가 가장 후순위 per plan §Success criterion).
4. `02_development.md` (G1–G6 의 수학적 핵심을 step-by-step granularity 로 통합).
5. `03_integration_and_new_open.md` + canonical_sub.md 2026-04-21 entry.
6. `99_summary.md`.

### 4.2 Risk Reminders (pre_brainstorm §H 에서 본 세션 적용)

- **H-H1 (K_pers 의 vineyard non-Lipschitz):** G1 의 Lipschitz statement 를 "generic Lipschitz with measure-zero exception" 으로 honest 작성.
- **H-H3 (Kramers 가 Σ_m 위 constraint 로 Hessian rank-deficient):** G5 의 Kramers prefactor 는 unconstrained Hessian 으로 sketch, constrained 보정은 C-S2 carry.
- **H-H5 (β^{0.89} overfit risk):** G5 의 exp38 재해석은 "consistent with Kramers prefactor" 까지만, "derived" 주장 안 함.
- **H-H8 (scope creep):** G4–G6 각각 1~2 페이지 상한 엄수. 완전 증명 유혹 시 plan.md §Non-goals 재확인.
- **H-H10 (Witten 의 infinite-dim):** G6 의 Witten 은 finite-dim 변형으로 처리, infinite-dim 은 post-Stage-1.

---

## §5. Self-Check (세션 종료시 재확인할 항목)

| 항목 | 검사 |
|---|---|
| plan.md target 재진술 | §1.1–1.4 |
| 다중 접근 (≥3 독립) | §2 (5 후보), §2.6 (독립성 매트릭스) |
| Primary + alternative 보존 | §3.1, §3.2 |
| Primary 의 단점 사전 인정 | §3.3 |
| 작업 의존 그래프 | §4.1 |
| Risk reminders | §4.2 |
| Silent resolution 금지 인지 | §1.3 (실패 정의) |
| Granularity 후속 검증 가능 | 본 파일 §1~§5 의 sub-numbering |

다음 산출물: `working/E/soft_K_definition.md` (G1).
