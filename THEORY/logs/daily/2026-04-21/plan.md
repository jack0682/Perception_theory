# Plan — 2026-04-21

## Target

**재공식화 Stage 1 (Definition Foundation) — C+E 공통 첫 세션.** K_soft 정의 commit, F-group 공리 F1–F2 초안, 교차 객체 `ℱ_C+E[u] = ℰ[u] − T · S[u] + λ_K · K_soft(u)` 의 well-definedness 를 생산하고, 그 위에서 **F-1 / M-1 / MO-1 세 Critical 각각의 C+E 강화 dissolution mapping** 을 1~2 페이지씩 pre-draft 한다. 하루의 산출은 reformulation 의 **수학적 toehold** — 이후 Stage 1 나머지 세션 과 Stage 2–3 가 이 위에서 이루어진다.

## Why now

- 2026-04-20 저녁 Stage 0 pin 완료 (Purpose = **C+E**, Decision Tree Q-α YES → Q-β YES). `reformulation_plan.md` 의 blocking gate 해소됨.
- 사용자 의지: 내일은 1 년 고착된 Critical 3건 (F-1, M-1, MO-1) 을 실제로 건드리고 싶다. C+E 는 단일 세션 에 **세 Critical 모두 에 개입 가능** 한 유일 경로 (E-only 는 F-1 vacuity 소멸만 가능, C-only 는 framework 만, C+E 는 dissolution 이중화).
- C+E 의 단일 세션 일감 (약 12~16 h) 이 사용자 "시간 많다" 예상 과 일치.
- 내일 산출물 없이는 Stage 1 나머지 세션 (E-S2, C-S2, CE-S2) 이 진입 불가 — 기반 정의와 교차 객체가 선행되어야.

## Context refs (에이전트가 반드시 읽어야 할 소재)

- **`THEORY/logs/daily/2026-04-21/pre_brainstorm.md`** — 본 plan 과 함께 작성된 **104 가설 풀** (A–J 섹션, 수학·물리 다각도 관점). 각 deliverable G1–G6 작성 전 해당 섹션 review 필수. §I 가 가설 → deliverable priority mapping.
- `THEORY/working/reformulation_purpose.md` — 오늘 저녁 pin 된 C+E purpose 선언문 + rationale + Non-goals.
- `THEORY/working/reformulation_plan.md` — Stage 1 Scope Definition 구조.
- `THEORY/working/open_problems_reframing_2026-04-19.md` §1–§9 — N-1 분해 (P-A, P-D, P-G), P-F 공백, 외부 이론 비교 (Allen-Cahn, stat mech, Witten Laplacian reference).
- `THEORY/working/integer_K_dependency_map.md` — 10 개 integer-K load-bearing 정리 (Retire 5+1, Re-prove 3, Re-prove-retain 1) + single-formation 19~20 survive.
- `THEORY/working/new_open_questions_2026-04-20.md` — NQ-1 (soft-K uniqueness, 4 후보 중 (i) 선택 근거 필요), NQ-3 (vineyard 대체).
- `THEORY/canonical/canonical.md` §3.3 (u codomain), §5.5 (transition diagnostics, persistence stability 이미 사용), §6 (Axiomatic Groups A-E, Group F 추가 대상), §8.1 (energy functional, ℱ_C+E 확장 대상), §12 (K-field 폐기 예고), §14 CN6/CN8/CN14 (thermal 재해석 대상).
- `THEORY/canonical/canonical_sub.md` — 2026-04-20 entry (integer-K dependency map, pending inconsistencies, NQ-1~7). 내일 출력은 본 파일 에 2026-04-21 entry append.
- `THEORY/logs/daily/2026-04-20/03_integration_and_new_open.md` §11 CS-1 (soft-K volume compatibility 우려), §11 CS-2 (thermal framework 필요 근거).
- 외부 정리 reference:
  - Cohen-Steiner, Edelsbrunner, Harer (2007) — persistence stability (bottleneck distance).
  - Simon (1985), Helffer-Sjöstrand (1985) — Witten Laplacian semiclassical analysis.
  - Da Prato & Zabczyk — Stochastic Equations in Infinite Dimensions (F3 Langevin well-posedness).
  - Kramers (1940) · Eyring (1935) — escape rate prefactor.

## Current hypotheses / approaches under consideration

사용자의 잠정 직감 (에이전트는 이 안에만 머물지 않음 — 출발점):

1. **K_soft 정의 (i) persistence weighted sum 이 canonical choice.** 이유: 기존 canonical §5.5 (transition diagnostics) 가 이미 H_0 persistence 를 사용. codomain 최소 변경. NQ-1 의 후보 (ii) Betti, (iii) simplex, (iv) measure 는 parking.
2. **F1 Thermal state + F2 Entropy 는 standard stat mech.** F3 Langevin · F4 T-primacy 는 statement + reference 만, 완전 well-posedness 는 C-S2 carry.
3. **ℱ_C+E[u] 의 λ_K scaling 이 자연스럽게 O(T).** entropy 와 K_soft 둘 다 information-theoretic 축 — dimensional 관점에서 동일 T scale.
4. **M-1 dissolution 이 C+E 의 가장 강한 강점.** isoperimetric feature (E) + Kramers rate (C) 이중 소멸. exp38 β^{0.89} 를 Kramers prefactor 로 재해석 가능.
5. **MO-1 dissolution 에서 Witten Laplacian 이 핵심 도구.** smooth Morse 복원만으로는 약함 — Witten 의 semiclassical expansion 이 low-T 극한에서 critical point 분석을 회복.

핵심 미해소 질문 (에이전트 답변 필수):

- **Q1. K_soft 와 volume constraint `Σuᵢ = m` 의 compatibility.** K_soft 최소화가 `Σuᵢ = m` 과 상충하는가? projected gradient flow 가 well-defined 한가?
- **Q2. λ_K scaling.** λ_K 의 자연 범위 — O(T)? O(1)? O(β)? 각 경우의 limiting behavior.
- **Q3. F-group 공리와 Group E (Transport) 의 compatibility.** F3 Langevin 이 E4 transport kernel 와 어떻게 공존? 두 동역학이 서로 다른 시간 척도?
- **Q4. Kramers prefactor 의 정확한 유도 경로.** Hessian eigenvalue dependence 가 exp38 의 β^{0.89} 와 일치 가능한가?

## Session goals (에이전트 핵심 deliverable — 6개)

### G1. `working/E/soft_K_definition.md` — K_soft 정의 commit

- 정의: `K_soft(u) = Σᵢ ℓᵢ · φ(ℓᵢ)`, H_0 persistence bar length weighted sum. φ: ℝ_≥0 → ℝ_≥0, monotone Lipschitz (예: `φ(ℓ) = ℓ / (1 + ℓ)` 또는 truncated linear).
- Well-definedness: persistence diagram Dgm(u) 의 stability (CSEH 2007 Theorem 4.2) + φ Lipschitz → `|K_soft(u) − K_soft(v)| ≤ L_φ · W_∞(Dgm(u), Dgm(v)) ≤ L_φ · ‖u − v‖_∞`.
- Lipschitz 증명 **골격** (완전 증명 아님): bottleneck stability lemma 진술 + φ composition 의 Lipschitz 전파 + Σ_m 에서의 bound 는 별도.
- 4 후보 (persistence / Betti / simplex / measure) 비교 1 페이지 + (i) 선택 근거.
- Volume constraint compatibility 예비 검토 (Q1) 1 단락.

### G2. `working/C/F_group_axioms.md` — F-group 공리 F1–F2 commit, F3–F4 draft

- **F1 Thermal state:** `u` 상태공간이 `Σ_m` 위의 확률분포 `ℙ[u] ∝ exp(−ℱ[u] / T)`. Free energy `ℱ[u] = ℰ[u] − T · S[u]`. Gibbs distribution 의 normalizability 1 단락.
- **F2 Entropy:** `S[u] = − Σ_x [u(x) log u(x) + (1 − u(x)) log(1 − u(x))]` (Bernoulli per-site). Lipschitz on `[ε, 1−ε]` 증명 골격. `S[u] ≥ 0` · `S[u] = 0` iff u ∈ {0,1}^n.
- **F3 Thermal gradient flow (Langevin) — statement + reference only:** `u̇ = −Π_{Σ_m}(∇ℰ − T∇S) + √(2T) · ξ`, ξ white noise. Da Prato–Zabczyk reference. 완전 well-posedness carry.
- **F4 Temperature primacy + T → 0 recovery — statement only:** T > 0. T → 0 에서 기존 canonical v1.2 gradient flow 회수 (Laplace's method). 증명 C-S3 carry.

### G3. `working/CE/free_energy_wellposed.md` — 교차 객체 well-definedness

- 객체: `ℱ_C+E[u] = ℰ[u] − T · S[u] + λ_K · K_soft(u)`.
- 4 항 각각의 Lipschitz 합산 → ℱ_C+E Lipschitz.
- Coercivity on Σ_m: E_cl, E_sep, E_bd 기존 coercive; −TS bounded; K_soft ≥ 0 → 합산 coercive.
- Minimizer 존재: compact Σ_m + continuous ℱ_C+E → Weierstrass. (Gibbs distribution normalizability 는 F1 에서.)
- K_soft 와 entropy S 의 상호작용 예비: 서로 다른 information-theoretic 축, 충돌 없음 예상.
- λ_K scaling 1 단락 (Q2) — `λ_K ~ O(T)` 자연성 논증 + 극한 거동 (λ_K → 0, λ_K → ∞).

### G4. `working/E/F1_dissolution.md` — F-1 소멸 C+E 버전

- F-1 statement 복기 + Evidence (exp62/63).
- **E 부분:** "K=2" 는 integer 가 아니라 K_soft ≈ 2 의 distribution regime. 외부 m_j 불필요 — vacuity 전제 소멸.
- **C 부분:** Gibbs 에서 K>1 mode 는 `exp(−ΔE/T)` weight 로 존재. "vacuous" 가 아니라 **thermally populated**. exp62/63 의 K=2 energy 4.66 는 `exp(−4.66/T)` Boltzmann factor.
- 1~1.5 페이지. 예제 distribution 1 개 포함.

### G5. `working/E/M1_dissolution.md` — M-1 feature 화 + Kramers (가장 묵직)

- M-1 statement 복기.
- **Isoperimetric feature (E 부분):** Γ-conv 재활용 sketch. single-mode preference 는 perimeter minimization 귀결 — bug 아님.
- **Kinetic metastability (C 부분, 신규):**
  - Kramers rate `τ_{K=2→K=1} ~ τ_0 · exp(ΔE/T)`, ΔE = E_K2 − E_K1 ≈ 2.41 (exp62/63).
  - T 적절 시 τ 가 관측 timescale 초과 → K=2 metastable.
  - CN6 "kinetically determined" 의 thermodynamic substantiation.
- **기존 empirical 재해석 (2 단락):**
  - exp38 β^{0.89} → Kramers prefactor 의 Hessian eigenvalue 의존으로 재유도 시도 (Q4).
  - exp55 zero-merge → T → 0 극한 τ → ∞ consistent.
- 2 페이지.

### G6. `working/E/MO1_dissolution.md` — MO-1 Witten Laplacian 편입

- MO-1 statement 복기 (Σ²_M corner, smooth Morse inapplicable).
- **코너 소멸 (E 부분):** soft-K 에서 state space 는 Σ_m interior, smooth manifold without boundary.
- **Witten Laplacian (C 부분, 신규):** 
  - `Δ_ℱ = Δ + ‖∇ℱ‖²/T − (Δℱ)/T` 의 low-T spectrum 이 critical point encode (Simon 1985).
  - semiclassical expansion statement only, 전체 분석 carry.
- **Fokker-Planck:** `∂_t ℙ = div(ℙ ∇ℱ) + T · Δℙ`. critical point 분석을 FP 연산자 spectrum 으로.
- 3 가지 alternative tool (smooth Morse via soft-K / Witten Laplacian / Fokker-Planck) 확보.
- 1.5~2 페이지.

## Non-goals (오늘 안 할 것)

- F3 Langevin 의 **완전 well-posedness 증명** (Da Prato–Zabczyk 스타일) — C-S2.
- F4 T → 0 **회수 증명** (35 Cat A 중 survive 분류 전수) — C-S3.
- Kramers **prefactor 정확 유도** (Hessian eigenvalue 의존) — C-S2.
- Witten Laplacian **spectrum semiclassical 완전 분석** — post-Stage-1.
- T-Merge (b) Γ-conv **증명 완전 rewrite** — E-S2.
- **§12 Multi-formation 전면 재작성** — Stage 1 나머지 세션.
- **T-Persist-K-Sep/Weak/Unified 재증명** — E-S3.
- **CN15–20 초안** (B 작업) — C+E scope 외.
- **threshold 얼굴 (P-D) · axiom-switching 얼굴 (P-G)** — 본 cycle Non-goals.
- **γ_eff prefactor 재측정 실험** — exp77+ 별도.
- **canonical.md 직접 수정** — working/ 만, canonical_sub.md 2026-04-21 entry append 로 기록.
- **Kramers 의 complete derivation** — sketch 수준 유지.
- **Q_morph threshold-free 화 (NQ-4)** — A 작업.
- **D partial variant well-posedness (NQ-6)** — D 작업.

## Carry-forward (2026-04-20 로부터)

- **Stage 0 pin 완료** → Stage 1 진입 가능.
- **9+1 integer-K load-bearing 정리 목록** (working/integer_K_dependency_map.md) — 내일 dissolution mapping 에서 명시 reference. Retire 5 중 **Topological Lock** 과 **Proposition 1.2** · **Theorem 3.1** 이 MO-1 dissolution 과 직결.
- **NQ-1 (soft-K 정의 uniqueness)** — G1 에서 (i) 선택 근거 1 단락 으로 부분 해소.
- **NQ-3 (vineyard T-Persist-K 대체)** — 본 세션 Non-goal, E-S2 carry.
- **Pending P-2026-04-20-01 (T-Persist-K-Sep category inconsistency) · P-02 (Cat C count)** — 본 세션에서 보수 안 함, 주간 merge 에서 별도.
- **canonical §12 soft-K 언어 삽입 candidate** (canonical_sub.md 2026-04-20 기록) — 본 세션 산출물이 주간 merge 의 근거.
- **exp38 (β^{0.89}) · exp55 (zero-merge) 재해석** — G5 M-1 dissolution 에서 직접 다룸.

## Success criterion for today

**저녁 시점에 6 개 working 파일이 모두 존재하고, 각 파일이 해당 Session goal (G1–G6) 의 최소 요구사항 을 만족하며, canonical_sub.md 2026-04-21 entry 가 Added 3 + Clarified 1 + Pending 7+ 로 작성 완료되어 있어야 한다.** 특히:

- G1: K_soft 정의 statement 확정 + Lipschitz 골격 + 4 후보 비교 1 페이지.
- G2: F1–F2 commit (well-definedness 포함) + F3–F4 statement draft.
- G3: ℱ_C+E well-definedness (Lipschitz + coercivity + minimizer 존재) 확보.
- G4–G6: 각 Critical dissolution preliminary mapping 1~2 페이지.

**최소 priority (시간 부족 시 뒤로 carry):** G4 (F-1 dissolution) 이 가장 뒤. G1 · G2 · G3 는 반드시 완료 — 이것이 Stage 1 기반.

단계별 체크:

- [ ] G1 soft_K_definition.md — 정의 + Lipschitz 골격 + 후보 비교 + volume compatibility 예비.
- [ ] G2 F_group_axioms.md — F1 F2 commit + F3 F4 draft.
- [ ] G3 free_energy_wellposed.md — 4 항 well-defined + minimizer 존재 + λ_K scaling 논증.
- [ ] G4 F1_dissolution.md — vacuity 소멸 + Gibbs thermal weight.
- [ ] G5 M1_dissolution.md — isoperimetric feature + Kramers + empirical 재해석.
- [ ] G6 MO1_dissolution.md — 코너 소멸 + Witten Laplacian + Fokker-Planck.
- [ ] canonical_sub.md 2026-04-21 entry append (Added 3 + Clarified 1 + Pending 7+).
- [ ] `working/CE/` · `working/E/` · `working/C/` 3 디렉토리 신설 완료.
- [ ] NQ-1 후보 (i) 선택 근거 확보 (working 에 기록).

하나라도 미달이면 성공 기준 미충족. 단, 우선순위 규칙 상 G4 미완은 허용 가능 (G1–G3 + G5 + G6 완료 시).

---

## 메모

- 본 plan 은 **2026-04-20 저녁** 에 사용자가 작성. 전날 밤 세션 (`logs/daily/2026-04-20/`) 의 8 선택지 분석 + Decision Tree + Sensitivity 결과 **C+E** 로 purpose pin.
- 에이전트 출력 위치: 본 디렉토리 내 `01_exploration.md` / `02_development.md` / `03_integration_and_new_open.md` / `99_summary.md`. 또한 `working/E/`, `working/C/`, `working/CE/` 에 6 개 실제 theoretical 산출물. canonical_sub.md 에 2026-04-21 entry append.
- **저녁 후속 (사용자 할 일):**
  1. 6 working 파일 검토 (필요시 "검증하고 보완하라" 추가 요청).
  2. canonical_sub.md 2026-04-21 entry 검토 + 필요 시 수정.
  3. 2026-04-22 plan.md 작성 — Stage 1 둘째 세션 (E-S2 §12 재작성 골격 또는 C-S2 Kramers prefactor 유도 중 선택).
- 본 plan 의 scope 는 **Stage 1 Definition Foundation** 의 공통 첫 세션. 6 deliverable 이 많아 보이지만 각각이 작은 단위 (1~4 h). 총 12~16 h 일감. 사용자 "시간 많음" 전제 하 충족 가능.
- **scope creep 주의점:** G4–G6 dissolution mapping 은 **preliminary mapping** 이지 complete proof 아님. 각 1~2 페이지 상한 엄수. 완전 증명 유혹 시 Non-goals 재확인.
