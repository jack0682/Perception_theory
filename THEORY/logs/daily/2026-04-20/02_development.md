# 02 — Development: 15 Session Sketches (5 candidates × first 3 sessions)

**Session:** 2026-04-20
**Target (from plan.md):** 각 후보 A/B/C/D/E 에 대해 Stage 1 을 내일 시작한다면 **Session 1·2·3 이 무엇을 하는가** 를 구체적으로 스케치. 추상 금지 — 각 세션은 (Target 한 문장) + (생산 파일명 + 내용 요약) + (수학 작업 유형) + (건드리는 canonical 섹션) + (선결조건 / 의존) 5요소 필수.
**This file covers:** plan.md §G2 — 5 × 3 = 15 세션 스케치.
**Depends on reading:** `01_exploration.md` (특히 Matrix-2 가 보여주는 각 후보의 Cat A 상실 지점); `reformulation_plan.md` §Stage 1~4; `canonical.md` §3, §5, §6, §8, §12, §13.

---

## §0. 작성 원칙

- **구체의 층위:** "Session 1: 개념 정리" 같은 표현 금지. plan.md 예시인 "working/soft_K_definition.md 작성. K 를 H_0 persistence bar length 가중합 K_soft = Σ ℓ_i · φ(ℓ_i) 로 정의" 의 granularity 를 기준.
- **파일 경로:** `THEORY/working/<purpose_tag>/<file>.md` 형식으로 통일. `<purpose_tag>` ∈ {A, B, C, D, E}. 본 세션 작업 자체는 `THEORY/logs/daily/2026-04-20/` 에만 쓰므로 이 스케치 내 제안 경로는 **미래 세션의 산출물 위치**.
- **수학 작업 유형:** {정의, 증명, 반례 구성, 공리 조작, 수치 실험, 서술 (scope note)} 중 하나 이상.
- **선결조건:** 이전 세션 산출물 · 외부 정리 · 관련 정의.
- **Session 0 (Stage 0 자체, 오늘) 은 세지 않음.** Session 1 = Stage 1 첫 세션 = purpose pin 직후.

---

## §A. Candidate A — Ontology Purification (N-1 전면)

**Purpose 한 줄:** 이론의 ontology (연속, graded) 와 작동 (이산 K, threshold, 공리 스위칭) 사이의 비원리적 스위칭을 제거.
**Scope 특성:** N-1 의 세 얼굴 (K / threshold / axiom-switching) 모두 대상. E 를 포함하되 더 광역.

### A-S1. Switching point audit (어디서 스위칭이 발생하는가)

- **Target (1문장):** canonical 전체에서 "정수 K / threshold 값 / 공리의 조건부 on-off" 가 등장하는 모든 지점을 지도화 — rewrite 대상의 범위 확정.
- **파일:** `THEORY/working/A/switching_audit.md`
- **내용 요약:** canonical §3 (formal universe), §5 (derived morphology), §6 (각 Group 의 Layer-crossing note · Reclassification Note), §7 (predicates with threshold), §8.0 (volume m = integer), §12 (K-field), §14 (CN6/CN14) 의 각 등장 지점을 행으로, 종류 (K-integer / θ-threshold / axiom-switch) 를 열로 한 audit table 작성. 각 행에 "현 해결 방식" + "A 이후 예상 변화" + "기존 정리 연결" 를 기록.
- **수학 작업 유형:** 서술 (scope mapping) + 공리 조작 준비.
- **건드리는 canonical 섹션:** §3.3, §5 전체, §6 (5 Group 모두), §7.1, §8.0, §12 K-field, §14 CN6, CN14.
- **선결조건:** `open_problems_reframing_2026-04-19.md` §8 (N-1 정의) 읽기. Matrix-1 의 A 열 (본 파일 §4) 이해.

### A-S2. Soft-K 정의 후보 세트 (not yet committed — options space)

- **Target:** K 를 정수에서 연속으로 격상하는 정의 후보 3~4개를 제시. 각 후보의 well-definedness · Lipschitz · canonical 연결성을 비교.
- **파일:** `THEORY/working/A/soft_K_candidates.md`
- **내용 요약:** 후보 정의 나열:
  (i) $K_{\mathrm{pers}}(u) = \sum_i \phi(\ell_i)$ — H_0 persistence bar 길이 가중합, $\phi$ monotone Lipschitz.
  (ii) $K_{\mathrm{Betti}}(u) = \int_0^1 \beta_0(\{x: u(x) \geq \theta\}) \, d\theta$ — superlevel set 의 zeroth Betti number 를 threshold 에 대해 적분.
  (iii) $u: X_t \to \Delta^{K_{\max}}$ — u 를 simplex-valued 로 격상, $K_{\mathrm{eff}} = $ effective number of components via entropy $H(u)$.
  (iv) $u: X_t \to \mathcal{P}(\mathbb{R}_{\geq 0})$ — u 를 measure-valued 로 격상, K = support size.
  각 후보에 대해 (a) Lipschitz 증명 spec, (b) canonical §3.3 codomain 에 미치는 영향, (c) 기존 T-Persist-1(e) fingerprint 구조와의 호환, (d) 단점.
- **수학 작업 유형:** 정의 + well-definedness 증명 spec + 비교.
- **건드리는 canonical 섹션:** §3.3 (u 의 codomain), §5.5 (transition diagnostics, persistence stability 이미 사용), §7.1 (Q_morph 의 ℓ_max), §12 K-field (폐기 예고).
- **선결조건:** A-S1 의 audit table. persistence stability theorem 진술 확정 (Cohen-Steiner-Edelsbrunner-Harer).

### A-S3. Threshold-parametrized family 의 공식화 (N-1 의 threshold 얼굴)

- **Target:** `θ_core, θ_in, θ_1, θ_2, θ_ext` 를 개별 자유 파라미터에서 parametrized family 로 격상. integral-over-θ diagnostic 의 형식 도출.
- **파일:** `THEORY/working/A/threshold_family.md`
- **내용 요약:** 현 canonical §5 의 5 threshold 를 하나의 sweep parameter $\theta \in [0, 1]$ 의 family 로 재정의. threshold-free diagnostic 후보: $\tilde{d}_k(u) = \int_0^1 d_k(u; \theta) \, d\theta$ for k ∈ {Bind, Sep, Inside, Persist}. Persist 의 Core 참조 부분은 $\int_\theta \text{Core}_\theta$ 로 재작성. 현 Q_morph 가 이미 superlevel filtration 을 sweep 하므로 부분적 구현 가능. 잔존하는 threshold (Core/Interior 경계) 의 Lipschitz sensitivity 분석.
- **수학 작업 유형:** 정의 + Lipschitz 분석 + 기존 diagnostic 과의 consistency.
- **건드리는 canonical 섹션:** §5 (derived morphology 전체 재작성), §7.1 (proto-cohesion 정의에서 θ 제거).
- **선결조건:** A-S1. A-S2 와 parallel 가능하나 일관성을 위해 A-S2 먼저 권장.

**A 의 초기 3세션 총괄:** S1 = scope 획정, S2 = K 재정의 후보, S3 = threshold 재정의. 3세션 후 A 의 실제 commitment 확정 가능. axiom 얼굴 (P-G) 은 S4+ 에서 진입.

---

## §B. Candidate B — Honest Scope (최소 수정)

**Purpose 한 줄:** 현 이론이 무엇의 이론이 **아닌지** 를 §14 CN 으로 공식화. 공리·정리 불변.
**Scope 특성:** 이론 진전 없음. 정직성 확보만.

### B-S1. CN15~CN20 초안 (6 신규 commitment notes)

- **Target:** P-B, P-D, P-E, P-F, P-H, 그리고 dual-mode 선택에 대한 6개 신규 Commitment Note 의 문장 작성.
- **파일:** `THEORY/working/B/commitment_notes_draft.md`
- **내용 요약:** 6개 CN 의 초안:
  (CN15) External substrate commitment — X_t · N_t 는 pre-theoretic input.
  (CN16) Parameter genealogy commitment — 25+ 파라미터의 origin 은 이론 외부.
  (CN17) Threshold commitment — θ_core/θ_in/θ_1/θ_2/θ_ext 는 free parametrization.
  (CN18) Zero-T commitment — metastability 주장은 zero-T local-minimum 언어로만 해석.
  (CN19) Time pre-theoretic commitment — T 는 given linear order.
  (CN20) Dual-mode choice commitment — Closure + Distinction 만 energy 진입; Co-belonging demotion 의 근거는 수학적 편의, 원리적 증명 아님.
  각 CN 은 (a) 2~3문장 본문, (b) "why here, why now" 1문장, (c) 관련 기존 CN (CN5-CN7 등) 과의 관계.
- **수학 작업 유형:** 서술 (scope declaration).
- **건드리는 canonical 섹션:** §14 (CN append 위치).
- **선결조건:** `open_problems_reframing_2026-04-19.md` §1-§7 전체 통독. 기존 CN1-CN14 재독.

### B-S2. §12 Inline erratum 삽입안

- **Target:** §12 의 주요 주장 (K-field architecture, multi-formation kinetic, self-referential transport) 각각에 scope-limitation erratum 삽입.
- **파일:** `THEORY/working/B/section12_erratum.md`
- **내용 요약:** §12 현 상태의 10+ 개 주요 단락 각각에 inline erratum 후보:
  - K-field 단락: "*(Scope note 2026-??-??: 본 architecture 는 external integer K 가정 하. Soft-K 일반화는 out of scope — N-1 참조.)*"
  - Metastability 단락: "*(Scope note: 'metastable' 은 Hessian 양정부호의 정적 의미로만 사용. 유한 T escape rate 는 framework 부재 — P-F 참조.)*"
  - Self-referential transport 단락: "*(Scope note: '자가참조' 는 within-time only. Temporal transport 는 여전히 external Ψ·φ 의존 — §9.5 Honesty Note 참조.)*"
  10 개 각각의 정확한 삽입 위치 (줄 번호) 와 1~2문장 erratum 본문.
- **수학 작업 유형:** 서술 (inline scope-limitation).
- **건드리는 canonical 섹션:** §12 전체.
- **선결조건:** B-S1 의 CN 초안 (erratum 은 CN 을 cross-ref).

### B-S3. Canonical §1/§2 서문 단락 — "what this theory is NOT"

- **Target:** §1 Status Note 또는 §2 Foundational Orientation 끝에 추가될 한 단락 (10~15줄) 초안.
- **파일:** `THEORY/working/B/scope_declaration.md`
- **내용 요약:** 아래 형식의 단락:
  > "이 이론은 다음을 주장하지 않는다: (i) substrate 의 self-generation (X_t 는 given); (ii) 파라미터 값의 원리적 선택 ((a_cl, β, ...) 은 free); (iii) 유한 온도 framework 의 완성 (metastability 는 zero-T 해석); (iv) 시간 T 의 emergence (T 는 given); (v) threshold 의 원리적 fixing (θ_core 등은 parametrized family); (vi) dual-mode 의 uniqueness (third mode C_t 는 demotion 의 수학적 편의)."
  추가로 이 Non-goal 선언의 "이론적 위상" 을 기술 — Non-goal 은 inability 가 아니라 **conscious scope limit**.
- **수학 작업 유형:** 서술.
- **건드리는 canonical 섹션:** §1 또는 §2.
- **선결조건:** B-S1, B-S2. 이 단락은 CN 과 erratum 의 summary 역할.

**B 의 초기 3세션 총괄:** S1 = CN 초안, S2 = inline erratum, S3 = 서문 단락. 3세션 후 B 의 핵심 deliverable 거의 완성. 이후는 주로 wording polish + 승급 작업. **B 는 본질적으로 3세션 프로젝트** — 이것이 "B 는 가장 작은 purpose" 의 정량적 표현.

---

## §C. Candidate C — Temperature / Entropy / Noise

**Purpose 한 줄:** 유한 T · entropy · Langevin noise 를 공리에 편입. metastability 주장의 framework 완성.
**Scope 특성:** 새 공리 그룹 F (thermal) 추가. Zero-T limit 으로 기존 정리 회수.

### C-S1. F-group (thermal) 공리 F1~F4 초안

- **Target:** 유한 온도 T > 0 하에서의 이론의 공리 구조를 F1~F4 로 형식화.
- **파일:** `THEORY/working/C/F_group_axioms.md`
- **내용 요약:** 공리 후보:
  (F1) **Thermal state**: $u$ 의 상태 공간이 확률분포 $\mathbb{P}[u] \propto \exp(-\mathcal{F}[u]/T)$. Free energy $\mathcal{F}[u] = \mathcal{E}[u] - T \cdot S[u]$.
  (F2) **Entropy**: $S[u] = -\sum_x [u(x) \log u(x) + (1-u(x)) \log(1-u(x))]$ (Bernoulli entropy per site). Lipschitz on $[\varepsilon, 1-\varepsilon]$.
  (F3) **Thermal gradient flow (Langevin)**: $\dot{u} = -\Pi_{\Sigma_m}(\nabla \mathcal{E} - T\nabla S) + \sqrt{2T}\, \xi$, $\xi$ = white noise.
  (F4) **Temperature primacy**: T > 0. T = 0 극한에서 기존 canonical 회수.
  각 공리의 well-definedness (확률분포 normalizability, Langevin well-posedness on compact manifold) 1문단씩.
- **수학 작업 유형:** 공리 조작 (공리 추가) + 정의 + 기존 공리와의 compatibility 예비 검토.
- **건드리는 canonical 섹션:** 신규 §8B (thermal energy principle) 또는 §6 신 Group F. §8.1 (energy functional) 에서 $\mathcal{F}$ 로 교체 가능성.
- **선결조건:** `open_problems_reframing_2026-04-19.md` §4 (Allen-Cahn, stat mech 비교), P-F 재검토. Stochastic PDE 표준 정리 (Da Prato-Zabczyk 계).

### C-S2. Kramers rate integration with existing metastability claims

- **Target:** 기존 exp38 의 barrier exponent β^{0.89} 와 exp55 의 zero-merge 결과를 Kramers 식 $\tau_{\mathrm{escape}} \sim \exp(\Delta E / T)$ 의 유한 T 언어로 재접합.
- **파일:** `THEORY/working/C/kramers_integration.md`
- **내용 요약:** 세 블록:
  (1) Barrier identification — canonical §12 "K-merge barrier height $\propto \beta^{0.89}$" (Cat B empirical) 을 C-framework 에서 재해석. T 와 β 의 관계 명확화.
  (2) Kramers prefactor 추정 — Hessian eigenvalue 에서 pre-exponential factor 유도.
  (3) CN6/CN8/CN14 업데이트 제안 — "kinetically determined" 를 "thermodynamically metastable with Kramers rate $\tau \sim \exp(\Delta E/T)$" 로 교체.
- **수학 작업 유형:** 정의 + 기존 empirical result 의 재해석 + 서술 (CN 업데이트).
- **건드리는 canonical 섹션:** §12 (K-merge barrier), CN6, CN8, CN14, §13 (γ_eff Cat B).
- **선결조건:** C-S1. Kramers rate 유도 (standard textbook).

### C-S3. Zero-T limit — 기존 35 Cat A 정리가 T → 0 에서 회수됨

- **Target:** 단일 formation 정리 (T1, T8-Core, T14, T-Bind-Proj 등) 가 T → 0 극한에서 기존 statement 를 얻는 formal derivation 목록.
- **파일:** `THEORY/working/C/zeroT_limit.md`
- **내용 요약:** 35 Cat A 정리 중 24~26개 에 대해 (T → 0 회수 가능 / 재증명 불필요) 분류. 각 정리마다 한 줄로 "T → 0 에서 $\mathcal{F} \to \mathcal{E}$, $\mathbb{P}[u] \to \delta_{u^*}$ 이므로 기존 statement 회수" 식의 argument. 예외 (metastability-수반 주장: T7-Enhanced, T-Persist-Full) 는 별도 표시 — 이들은 C 에서 **강화** (유한 T 에서도 성립) 될 수 있음.
- **수학 작업 유형:** 증명 (극한 회수) + 서술.
- **건드리는 canonical 섹션:** §13 전체.
- **선결조건:** C-S1. 극한 회수 lemma (exponential concentration of Gibbs measure).

**C 의 초기 3세션 총괄:** S1 = thermal 공리 추가, S2 = 기존 주장과 통합, S3 = 기존 정리 보존 확인. 3세션 후 C 의 framework 기본 골격 완성. 이후는 thermal 정리 (Eyring-Kramers, FDT) 신규 증명.

---

## §D. Candidate D — Self-Generating Substrate

**Purpose 한 줄:** X_t · N_t 를 u_t 에서 유도. 외부 관계 입력 제거.
**Scope 특성:** 기술적 난이도 최상. B-group 공리 전면 재작성.

### D-S1. N_t 를 u_t 에서 유도하는 메커니즘 후보

- **Target:** "adjacency from cohesion" 의 3~4 수학적 후보 제시. 각각의 well-definedness 예비 검토.
- **파일:** `THEORY/working/D/derived_adjacency.md`
- **내용 요약:** 후보:
  (i) **Correlation-based:** $\mathbf{N}_t[u](x,y) = f(u(x), u(y), \text{similar context})$ for some kernel $f$.
  (ii) **Cohesion-weighted distance:** 기존 graph 위에서 adjacency 를 u 로 reweight — $\mathbf{N}_t[u](x,y) = \mathbf{N}_t^{\mathrm{base}}(x,y) \cdot g(u(x), u(y))$. (이것은 "partial D" — site 는 고정, edge weight 만 u-derived.)
  (iii) **Gradient-based:** $\mathbf{N}_t[u](x,y) \propto \exp(-|u(x) - u(y)|/\sigma)$ — feature-space adjacency.
  (iv) **Persistence-based:** 0-dim persistence 의 merge tree 에서 adjacency 유도.
  각 후보: well-definedness, circular dependency (N 이 u 에 영향 → u 가 N 에 영향), canonical §6 Group B B1-B4 와의 compatibility, 계산 비용.
- **수학 작업 유형:** 정의 + 예비 분석.
- **건드리는 canonical 섹션:** §3.5 (N_t 정의), §6 Group B (B1-B4), §9.1 (aggregation operator P_t).
- **선결조건:** 기존 B-group 전수 재독. `open_problems_reframing_2026-04-19.md` §1 Group B 부분.

### D-S2. Partial derivation — sites 고정, adjacency 만 derived

- **Target:** X_t 는 유지하되 N_t 만 u 에서 유도하는 minimal D-variant 의 spec. Full D (X_t 까지 derived) 는 deferred.
- **파일:** `THEORY/working/D/partial_derivation.md`
- **내용 요약:** D-S1 의 후보 (ii) cohesion-weighted 를 채택한 partial variant:
  - B1-B4 의 각 조건이 derived N_t 에서 자동 성립하는지 점검.
  - Closure 연쇄 (Cl uses P_t uses N) 에서 N 이 u-dependent 이 되면 Cl 의 Lipschitz 재검토 (기존 Lipschitz bound $a_{\mathrm{cl}}/4$ 가 파괴되는지).
  - Fixed-point iteration: $u \to \mathbf{N}[u] \to P_t \to \mathrm{Cl}(u)$ 의 self-consistent 해 존재.
- **수학 작업 유형:** 공리 조작 (Group B 수정) + 증명 준비 (fixed-point).
- **건드리는 canonical 섹션:** §3.5, §6 Group B, §9.1, §9.2 (closure candidate).
- **선결조건:** D-S1. Banach / Schauder fixed-point 복습.

### D-S3. u → N → u 순환 의존성의 well-posedness

- **Target:** Partial D 에서 정의된 recursion 의 fixed point 존재 증명 골격.
- **파일:** `THEORY/working/D/fixpoint_obstruction.md`
- **내용 요약:** $\Phi: u \mapsto \mathrm{Cl}(u; \mathbf{N}[u])$ 의 fixed point 증명 시도:
  - Step 1: $\Phi$ 가 $[0,1]^n$ 에서 자신에게 매핑됨.
  - Step 2: $\Phi$ 가 continuous (에너지 closure + N[u] 두 층의 composition).
  - Step 3: Brouwer fixed-point → 존재.
  - Step 4 (unique?): Banach 시도 — Lipschitz constant 가 $a_{\mathrm{cl}}/4 \cdot L_N$ with $L_N$ = Lipschitz of N[u] map. 유니크성 조건 정리.
  - Step 5 (실패 분석): $L_N$ 이 크면 기존 contraction 규제 ($a_{\mathrm{cl}} < 4$) 가 강화되어야 함 — 이것이 D 의 비용.
- **수학 작업 유형:** 증명 (fixed-point existence) + 조건 도출.
- **건드리는 canonical 섹션:** §6 Group A (A3 contraction with new Lipschitz analysis), §9.2.
- **선결조건:** D-S1, D-S2. 기존 T6a/T6b 의 증명 기법 활용.

**D 의 초기 3세션 총괄:** S1 = 후보 탐색, S2 = minimal variant 선택, S3 = well-posedness 골격. 3세션 후에도 D 는 초반 단계 — partial D 만 진입, full D (X_t까지 derived) 는 S10+. 이것이 "D 는 수십 년 단위" 의 정량적 예시.

---

## §E. Candidate E — Emergent-K (N-1 의 K 얼굴 정면)

**Purpose 한 줄:** K 를 외부 정수 파라미터에서 derived soft quantity 로 재정의. 단일 u 위에서 K readout.
**Scope 특성:** §12 K-field 전면 재작성. 단일 formation 이론은 최대한 보존.

### E-S1. K_soft 정의 확정 — H_0 persistence 기반

- **Target:** K 를 soft quantity 로 재정의하는 **단일** 정의 채택 (A-S2 의 후보 중 하나 commit) + well-definedness 증명 골격.
- **파일:** `THEORY/working/E/soft_K_definition.md`
- **내용 요약:**
  **정의:** $K_{\mathrm{soft}}(u) = \sum_{i \in \mathrm{H_0 bars}} \phi(\ell_i)$ where $\ell_i$ = persistence bar length (death − birth) in the superlevel-set filtration of $u$, $\phi: \mathbb{R}_{\geq 0} \to [0,1]$ monotone with $\phi(0) = 0$, $\phi(\ell) \to 1$ as $\ell \to \infty$ (예: $\phi(\ell) = 1 - \exp(-\ell / \ell_{\mathrm{scale}})$).
  **Well-definedness:** $K_{\mathrm{soft}}$ 는 persistence stability theorem 에 의해 $\|u - v\|_\infty$ 에 Lipschitz. 즉 $|K_{\mathrm{soft}}(u) - K_{\mathrm{soft}}(v)| \leq L_\phi \cdot n \cdot \|u - v\|_\infty$ (n = |X_t|).
  **기존 이론 연결:** Q_morph 의 $\ell_{\max}$ 는 이미 같은 filtration 의 longest bar. $K_{\mathrm{soft}}$ 는 동일 filtration 의 total bar count weighted by length. 즉 **기존 Q_morph 인프라 재활용 가능**.
  **한계:** $\phi$ 선택의 자유 — 이는 새 free parameter. 최소화는 $\phi = \mathrm{id}$ 근사 사용.
- **수학 작업 유형:** 정의 + Lipschitz 증명.
- **건드리는 canonical 섹션:** §5 (derived morphology 에 $K_{\mathrm{soft}}$ 추가), §7.1 (Q_morph 와의 관계 명시), §12 (K-field 대체 예고).
- **선결조건:** persistence stability theorem (Cohen-Steiner-Edelsbrunner-Harer 2007) 진술.

### E-S2. §12 K-field architecture 전면 재작성

- **Target:** 기존 §12 의 K 개 coupled fields $u^1, ..., u^K$ 를 **단일 u 위의 emergent K** 로 대체하는 새 §12 골격.
- **파일:** `THEORY/working/E/section12_rewrite.md`
- **내용 요약:**
  - 기존 §12 의 3 Pillars (Nucleation, Metastability, Coarsening) 를 단일 u 관점에서 재작성:
    * **Nucleation** — 스펙트럼 분석은 유지 (u 위의 Fiedler eigenvector decomposition). K>1 은 다수의 persistence bars 로 readout.
    * **Metastability** — 단일 formation 이 multi-modal distribution 의 local min 일 때. H_0 persistence 에서 long bars = stable modes.
    * **Coarsening** — $K_{\mathrm{soft}}$ 의 시간 감소 (merging bars).
  - Coupling Bound Lemma · T-Persist-K-* 삼총사 · T-Merge (a) · Topological Lock · Prop 1.2 · Thm 3.1(d) 를 폐기 (T-Merge (b) 는 isoperimetric 으로 재증명 유지; fate 는 E-S3).
  - 대체 정리 후보: "$K_{\mathrm{soft}}(u_t)$ 의 temporal evolution 은 persistence diagram flow 로 기술됨" — vineyard stability 문헌 활용.
  - `scc/multi.py` 재설계 개요: K-loop 제거, 단일 u 에서 persistence 계산 추가.
- **수학 작업 유형:** 공리 조작 (§12 재작성) + 서술 + 코드 영향 예고.
- **건드리는 canonical 섹션:** §12 전체 (대폭), §3.5, §5.5, §11.2 item 8 (multi-formation architecture).
- **선결조건:** E-S1. persistence vineyards 문헌 (Cohen-Steiner-Edelsbrunner-Morozov 2006).

### E-S3. T-Persist-K-* 삼총사의 fate 판정

- **Target:** T-Persist-K-Sep / K-Weak / K-Unified 각각에 대해 Retire / Re-prove / Reinterpret 중 하나를 선택 + 근거.
- **파일:** `THEORY/working/E/theorem_fate_K.md`
- **내용 요약:**
  - **T-Persist-K-Sep (Cat C):** 현 진술은 per-formation $u^k$ 언어. E 에서 per-formation 은 소멸. **Retire**. 대체: "단일 u 의 H_0 persistence bars 가 gentle transition 하에 individually stable" — vineyard stability 정리로 대체.
  - **T-Persist-K-Weak (Cat C):** per-formation + 경계 overlap. 동일하게 per-formation 언어 소멸. **Retire**. 대체 없음 (weak interaction 이 soft-K 에서 자연스럽게 표현).
  - **T-Persist-K-Unified (Cat C):** $\Lambda_{\mathrm{coupling}}$ parametrization 은 per-formation spectral gap 기반. **Retire**. 대체: "$K_{\mathrm{soft}}$ 변화율의 단일 parametrization" — 새 정리 (Stage 3 에서).
  - **관련 Cat A 정리:** T-Merge (a), Topological Lock, Prop 1.2, Thm 3.1(d), Coupling Bound Lemma — 전부 per-formation 또는 K=2 manifold 언어. **Retire**. T-Merge (b) 는 isoperimetric 이므로 **Re-prove** (K 무관).
  - **T-Beyond-Weyl (Cat B), T-d_min-Formula (Cat B):** K-field 상의 Hessian / distance 결과. **Retire**.
  - 각 Retire 에 대해 "대체 정리 후보" 를 한 줄로 명시 — canonical §13 의 새 entries 후보.
- **수학 작업 유형:** 서술 (survival 판정) + 대체 정리 제안.
- **건드리는 canonical 섹션:** §12, §13.
- **선결조건:** E-S1, E-S2. Matrix-2 (본 세션 §5) 의 E 열 정합성 유지.

**E 의 초기 3세션 총괄:** S1 = K 재정의, S2 = §12 재작성 골격, S3 = 폐기 정리 목록. 3세션 후 E 의 전체 scope 가 확정되고 Stage 2~4 에 진입 가능. **E 는 11~14세션으로 완료 가능** (reformulation_plan.md Timeline 과 일치).

---

## §Z. 전체 세션 수 추정 (각 후보, 3세션 이후 예상)

| 후보 | Stage 1 세션 | Stage 2 세션 | Stage 3 세션 | Stage 4 세션 | Stage 5 세션 | Stage 6 | **총 추정** |
|---|---|---|---|---|---|---|---|
| A | 3 (위) + 2 | 3 | 4 | 3 | 2 | 1 | **18** |
| B | 3 (위) | 0 (공리 불변) | 0 | 0 (정리 불변) | 0 | 1 | **4** |
| C | 3 (위) + 1 | 3 | 3 | 3 | 2 | 1 | **16** |
| D | 3 (위) + 3 | 3 | 4 | 3 | 3 | 1 | **20** |
| E | 3 (위) | 2 | 3 | 2 | 1 | 1 | **12** |
| C+E | (공통 3) + 4 | 4 | 4 | 3 | 2 | 1 | **17** |
| B+C | (공통 3) + 3 | 3 | 3 | 3 | 2 | 1 | **15** |
| A+C | (공통 3) + 4 | 4 | 5 | 4 | 3 | 1 | **21** |

- **B 의 4세션** 추정이 최저 — B 본질적 작업량 자체가 작음. 이것이 Q2 답변의 반대 측면 (B 의 cost 도 최저).
- **E 의 12세션** 이 단일 후보 중 최단. C+E 의 17세션도 조합 중 최단.
- **D 20세션, A+C 21세션** 이 가장 큼.

숫자는 reformulation_plan.md §Timeline 의 "B 하한, D/E 상한" 을 (E 대신 D 를 상한 두어) 재현. 정밀한 추정은 각 Stage 내 진행을 실제 해 봐야 확정.

**Next file:** `03_integration_and_new_open.md` — Q1~Q4 답변 + 조합 비용 분석 + 권고.
