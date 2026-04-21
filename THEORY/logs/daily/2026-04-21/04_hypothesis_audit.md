# 04 — Hypothesis Survival Audit + Quality Review (Post-Session)

**Session:** 2026-04-21
**Purpose:** `pre_brainstorm.md` 의 104 가설 중 본 세션에서 (a) 채택·정리되어 출력 파일에 들어간 가설 (USED), (b) 보존되었으나 본 세션에 commit 안 된 가설 (PARKED), (c) 명시적으로 기각된 가설 (REJECTED), (d) 본 세션 scope 밖이라 다루지 않은 가설 (UNTOUCHED) 을 분류. 추가로 산출물에서 발견한 정정사항 (Errata) 정리.
**This file covers:** 가설 survival 매트릭스 (§1–§9) + 살아남은 가설의 substantive 소개 (§10) + Errata + Quality Review (§11–§12).
**Depends on reading:** `pre_brainstorm.md` (104 가설), 6 working files, 4 daily core files.

---

## §0. 분류 기준

- **USED** (채택). 본 세션의 working 파일 또는 daily 파일에 명시적으로 인용 / 사용 / commit. 가설의 핵심 내용이 산출물의 일부.
- **PARKED** (보존). 본 세션에 직접 사용 안 했으나 산출물에서 alternative / future-work 로 명시 보존. 후속 세션 활성화 후보.
- **REJECTED** (기각). 본 세션에서 명시적으로 reject 또는 conflict 사유 제시 (CN12 충돌, T8-Core 충돌 등).
- **UNTOUCHED** (미접촉). pre_brainstorm 에 등재되었으나 본 세션 scope 밖. 후속 세션 / Stage 의 자유 후보.

---

## §1. §A K_soft 정의 (17 가설)

| # | 가설 요약 | 분류 | 근거 (산출물 위치) |
|---|---|---|---|
| **A1** | persistence weighted sum `K_soft = Σ φ(ℓ_i)` canonical | **USED** | G1 Def 1 (primary commit) |
| **A2** | Betti integral = (i) under `φ(ℓ)=ℓ` via Fubini | **PARKED** | G1 §5 후보 (ii); 01_exploration P2 |
| **A3** | simplex-valued `K_eff = exp(H(u))` | **REJECTED** | G1 §5 후보 (iii) — CN12 충돌 |
| **A4** | measure-valued | **PARKED** | G1 §5 후보 (iv) |
| **A5** | hybrid `Σ φ(ℓ)·ψ(bar entropy)` | **UNTOUCHED** | (post; complexity) |
| **A6** | ∇K_soft = vineyard, V 에서 discontinuous | **USED** | G1 §3.3 sparse gradient + §2.3 vineyard caveat |
| **A7** | volume `Σu_i = m` 와 K_soft 직교 | **USED** | G1 §3.2 Q1 답변 |
| **A8** | `sup K_soft ~ m/ℓ_min` scaling | **USED** | G1 §3.2 마지막 단락 |
| **A9** | sub-additivity `K_soft(u+v) ≤ K_soft(u) + K_soft(v)` | **UNTOUCHED** | (post) |
| **A10** | `K_hard(θ)` 와 K_soft 의 θ-average 관계 | **USED** | G1 §4 hard-K recovery |
| **A11** | K_soft = order parameter rank (interpretive) | **PARKED** | G1 §4 interpretation |
| **A12** | RG flow block-spin | **PARKED** | NQ-10 (γ_K first-principles) |
| **A13** | Ising cluster count analog | **UNTOUCHED** | (interpretive only) |
| **A14** | Allen-Cahn interfaces, K_soft = component count Γ-conv | **USED** | G5 §2.2 Modica-Mortola |
| **A15** | Neural ensemble interpretation | **UNTOUCHED** | (out of math scope) |
| **A16** | Percolation analog | **UNTOUCHED** | (out of math scope) |
| **A17** | K_soft inherently multiscale, single-scalar lossy | **UNTOUCHED** | (concession; future) |

**§A 합계:** USED 6, PARKED 4, REJECTED 1, UNTOUCHED 6. **K_soft 정의 단계의 11/17 = 65% 가설이 본 세션에 들어옴.**

---

## §2. §B F-group (20 가설)

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **B1** | F1 Gibbs Z(T) finite via compact + cont | **USED** | G2 Prop F1.1 (Cat A) |
| **B2** | F2 Bernoulli S strictly concave on (ε,1-ε)^n | **USED** | G2 Prop F2.1 (Cat A) |
| **B3** | F3 Langevin via Da Prato-Zabczyk | **USED (statement)** | G2 §3 reference |
| **B4** | F3 alt: logit→unconstrained | **PARKED** | G2 §3.2 alternative noted |
| **B5** | F4 T→0 via Laplace's method | **USED (statement)** | G2 §4 F4.a |
| **B6** | Freidlin-Wentzell instanton | **UNTOUCHED** | (carry C-S2/3) |
| **B7** | KL divergence as F2 alternative | **REJECTED** | (Bernoulli chosen, KL needs reference measure) |
| **B8** | Fisher information / natural gradient | **UNTOUCHED** | (canonical §8.7 Shahshahani 언급만; post) |
| **B9** | Witten Laplacian H-S 1985 | **USED** | G6 §3 + dev §3 (primary spectral tool) |
| **B10** | Hodge decomposition | **UNTOUCHED** | (advanced; post) |
| **B11** | F-group = Ginzburg-Landau + thermal | **PARKED** | (interpretive comparison) |
| **B12** | Kubo linear response | **UNTOUCHED** | (post) |
| **B13** | FDT | **UNTOUCHED** | (post) |
| **B14** | Critical phenomena, β_crit, universality | **UNTOUCHED** | (post; canonical T8-Core 별개) |
| **B15** | Mean-field on fully-connected | **UNTOUCHED** | (post) |
| **B16** | RG flow for `(T, α, β, λ_K)` | **PARKED** | NQ-10 |
| **B17** | Witten SUSY QM ↔ F-group | **UNTOUCHED** | (advanced) |
| **B18** | Path integral Feynman-Kac | **UNTOUCHED** | (advanced) |
| **B19** | Euclidean QFT analog (FP = imaginary-time Schrödinger) | **UNTOUCHED** | (advanced) |
| **B20** | Free energy Legendre = effective action | **UNTOUCHED** | (advanced) |

**§B 합계:** USED 4 (statement-only 2 포함), PARKED 3, REJECTED 1, UNTOUCHED 12. **F-group 4/20 = 20% 만 본 세션 (commit + statement) — 나머지는 의도적 carry.**

---

## §3. §C 교차 객체 ℱ_C+E (10 가설)

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **C1** | `λ_K ~ T` scaling, "effective entropy" | **USED** | G3 §4.3 commit |
| **C2** | `λ_K ~ β` scaling | **REJECTED** | G3 §4.2 — T8-Core/F4 충돌 |
| **C3** | `λ_K ~ O(1)` T-independent | **REJECTED** | G3 §4.2 — F4 recovery 더럽힘 |
| **C4** | `(T, λ_K)` phase diagram 4 corners | **PARKED** | CE-S2 carry |
| **C5** | Modified Gibbs decomposition `exp(-ℰ/T)·exp(S - λ_K K_soft/T)` | **USED** | G3 §4.3 form |
| **C6** | Information decomposition orthogonal axes (Shannon S vs persistence K_soft) | **USED** | G3 §5.1 |
| **C7** | Multiscale variational | **PARKED** | (interpretive) |
| **C8** | Crossover region `γ_K · K_soft ≈ S` | **PARKED** | CE-S2 |
| **C9** | Degenerate lift, K=1 mode choice symmetry breaking | **UNTOUCHED** | (post) |
| **C10** | `∇K_soft` vineyard explicit + bar birth/death discontinuous | **USED** | G1 §3.3 |

**§C 합계:** USED 4, PARKED 3, REJECTED 2, UNTOUCHED 1. **교차 객체 4/10 = 40% — 핵심 (λ_K-T scaling, decomposition, gradient, information axes) 모두 들어옴.**

---

## §4. §D F-1 Dissolution (8 가설) — **전수 활용 시도**

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **D1** | "Vacuity" 는 integer-K category 에서만 정의 | **USED** | G4 §2.1 |
| **D2** | K=2 = distribution regime, K_soft ≈ 2 = 2 dominant bars | **USED** | G4 §2.2 |
| **D3** | K-resolved partition `Z = Σ_K Z_K` | **USED** | G4 §3 + R-F1-D carry |
| **D4** | F_K = E_K - T S_K + λ_K K, S_K(K) compete | **USED** | G4 §3.3 example |
| **D5** | Critical T_c ≈ ΔE / ΔS | **USED** | G4 §3.3 (단, **§11 errata 반영** 후 부호 정정) |
| **D6** | Crossover temperature | **USED** | G4 §3.3 table |
| **D7** | F-1 zero-T artifact | **USED** | G4 §3.4 |
| **D8** | exp62/63 are T=0; thermal redo | **USED** | G4 R-F1-A → Stage 5 |

**§D 합계:** USED 8/8 = 100%. **F-1 dissolution 의 모든 가설이 channel 됨** (가장 직관적이고 단순한 dissolution이라 가설 풀 자체가 작았음).

---

## §5. §E M-1 Dissolution (14 가설) — **most substantive**

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **E1** | Modica-Mortola perimeter limit | **USED** | G5 §2.2 |
| **E2** | M-1 = feature, not bug | **USED** | G5 §2.4 (with disconnected-graph caveat per dev §4.5) |
| **E3** | Kramers-Eyring formula | **USED** | G5 §3.2 |
| **E4** | exp38 γ_eff=0.89 ~ Hessian scaling, prefactor reinterpretation | **USED** | G5 §4.1 |
| **E5** | Freidlin-Wentzell instanton | **PARKED** | (advanced; alternative escape-rate analysis) |
| **E6** | 3 origin: barrier / topological / entropic | **PARKED** | (G5 mentioned indirectly; not unpacked) |
| **E7** | Becker-Döring nucleation, critical radius | **UNTOUCHED** | (R-M1-E carry) |
| **E8** | Ostwald ripening, Lifshitz-Slyozov | **PARKED** | G5 §5 R-M1-E carry to E-S3 |
| **E9** | Allen-Cahn → mean curvature flow | **UNTOUCHED** | (post; canonical "extension" §12) |
| **E10** | Supercooled liquid analog (K>1 = glass, K=1 = crystal) | **UNTOUCHED** | (interpretive) |
| **E11** | β^{0.89} universality vs Ising classes | **PARKED** | (R-M1-C carry) |
| **E12** | Dynamic quench T(t) | **UNTOUCHED** | (post) |
| **E13** | Eyring transition state, transmission coefficient κ | **PARTIAL USED** | G5 §3.2 Eyring formula |
| **E14** | Lifetime concrete: `τ/τ_0 = (det H ratio)^{1/2} · exp(2.41/T)` | **USED** | G5 §3.3 |

**§E 합계:** USED 5, PARTIAL USED 1, PARKED 4, UNTOUCHED 4. **6/14 = 43% — primary tools (Modica-Mortola + Kramers + reinterpretation + lifetime) 모두 USED. 후속에 Becker-Döring, Ostwald, mean-curvature 등 alternative tools 다수 보존.**

---

## §6. §F MO-1 Dissolution (14 가설) — **dissolution 도구 풍부**

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **F1** | Σ²_M corner removal by soft-K | **USED** | G6 §2.1 |
| **F2** | Smooth Morse on Σ_m^ε interior | **USED** | G6 §2.3 |
| **F3** | Morse-Bott degenerate critical submanifold | **PARKED** | (post; advanced) |
| **F4** | Stratified Morse (Goresky-MacPherson) for boundary | **PARTIAL USED** | G6 §4.4 mentioned |
| **F5** | Witten Laplacian definition | **USED** | G6 §3.1 + dev §3 |
| **F6** | Helffer-Sjöstrand semiclassical | **USED** | G6 §3.2 + dev §3.2 |
| **F7** | Fokker-Planck operator | **USED** | G6 §4 + dev §3 conjugate |
| **F8** | Hodge decomposition on Witten complex | **UNTOUCHED** | (advanced) |
| **F9** | Morse inequalities `c_k ≥ b_k` | **PARTIAL USED** | G6 §5.1 (Forman context) |
| **F10** | Forman discrete Morse | **PARKED** | G6 §5 alternative |
| **F11** | Reeb graph / level set | **UNTOUCHED** | (post) |
| **F12** | Reeb barcode = persistence diagram (theoretical foundation of K_soft) | **PARTIAL USED** | (implicit in G1 K_soft definition) |
| **F13** | Floer homology infinite-dim | **UNTOUCHED** | (advanced; post-Stage-1+) |
| **F14** | Cerf theory (T as bifurcation parameter) | **UNTOUCHED** | (advanced; post-Stage-1+) |

**§F 합계:** USED 4, PARTIAL USED 3, PARKED 2, UNTOUCHED 5. **7/14 = 50% — Witten + FP + Forman alternative + smooth Morse 4 도구 확보. plan §G6 의 "3 alternative tools 동시 획득" 목표 충족.**

---

## §7. §G 교차 구조 (7 가설)

| # | 가설 요약 | 분류 | 근거 |
|---|---|---|---|
| **G1** | 3 Critical = single source N-1 | **USED** | 01_exploration §1.4 A4; cross-cuts all dissolutions |
| **G2** | Residual after dissolution (각 Critical 별 잔여물 listed) | **USED** | 각 dissolution §5 residuals (R-F1-X, R-M1-X) |
| **G3** | 3 dissolution = 재언어화, 새 문제 등장 | **USED** | 01_exploration §1.3 failure 정의 + 각 dissolution residual |
| **G4** | Gauge theory analog (integer K = topological charge) | **UNTOUCHED** | (J series; advanced) |
| **G5** | Disorder-order phase transition (T-driven) | **PARTIAL USED** | G4 §3.3 crossover T_c |
| **G6** | 3 Critical share Hessian structure | **PARTIAL USED** | dev §3 (Witten + Kramers 통합 spectral framework) |
| **G7** | Universality across phase-field theories | **UNTOUCHED** | (post; canonical "extension" §12) |

**§G 합계:** USED 3, PARTIAL USED 2, UNTOUCHED 2. **5/7 = 71% — 3 Critical 의 통합 framing 이 본 세션의 핵심 narrative 였으므로 높음.**

---

## §8. §H Risk / Counter-Hypothesis (11 가설) — **모두 검토**

각 risk 가 본 세션에서 어떻게 다뤄졌는지:

| # | Risk | 처리 |
|---|---|---|
| **H1** | K_soft non-Lipschitz at vineyard | **STRENGTHENED**. 02_dev §4.1 counter-example attempt — 실은 K_soft 가 multiset-stable 이라 globally Lipschitz 임을 보임 (G1 Cor 4.1 신규). 강화. |
| **H2** | F-group ↔ A3 hidden conflict (e.g., σ T-dependent) | **CHECKED**. G2 §5.1 — A3 는 T-independent 이므로 conflict 없음. |
| **H3** | Kramers on constrained Σ_m, rank-deficient Hessian | **ACKNOWLEDGED**. G5 §5 R-M1-A carry to C-S2; dev §3.2 step 5 명시. |
| **H4** | Witten semiclassical T small assumption | **ACKNOWLEDGED**. G6 §3.2 limit 명시 (T → 0 semiclassical); finite-T 는 별도. |
| **H5** | β^{0.89} overfit risk | **ADDRESSED**. G5 §4.1 explicit "consistent-with, not derived-from"; Plan §H-H5 risk reminder 직접 적용. |
| **H6** | (T, λ_K) degeneracy in observation | **UNTOUCHED**. (post; CE-S2 phase diagram 다룰 때 검토.) |
| **H7** | K_soft physical motivation 약함 (mathematical convenience) | **UNTOUCHED but flagged**. (philosophical concession; canonical §11.2 open design choices 와 맥락 일치.) |
| **H8** | Scope creep (각 dissolution 1-2 페이지 상한) | **HONORED**. F1 1.2p, M1 2p, MO1 2p — 모두 상한 내. dev/integration 은 별도 (메타). |
| **H9** | 1년 stuck → C+E 후 새 stuck (P-F completion) | **ACKNOWLEDGED**. 03_integration §3.4 P-F partially dissolved; full P-F resolution 은 Stage 2-3 carry. |
| **H10** | Witten infinite-dim 주의 | **ADDRESSED**. G6 §3.4 finite-dim 처리만; infinite-dim continuum limit 는 post-Stage-1. |
| **H11** | T = 0 추출 정정성 (λ_K → 0 처리) | **ADDRESSED**. G3 §4.3 (λ_K-T) 선택이 정확히 이를 위함 — T → 0 ⇒ λ_K → 0 자동, 깨끗한 F4 recovery. |

**§H 합계:** STRENGTHENED 1, ADDRESSED/HONORED 5, ACKNOWLEDGED 3, UNTOUCHED 2. **9/11 = 82% — 거의 모든 risk 가 인지·처리됨.** 가장 가치 있었던 결과: H1 의 "non-Lipschitz risk" 가 사실은 false alarm 이고 실제로 K_soft 는 강한 Lipschitz 임을 02_dev §4.1 에서 확인 (Cor 4.1).

---

## §9. §J Out-of-the-box (10 가설)

본 세션 scope 외이나 후속 영감으로 보존:

| # | 가설 | 후속 활성화 시점 |
|---|---|---|
| **J1** | Categorical: SCC as sheaf on poset of thresholds | 후속 P-D (threshold) 작업 시 |
| **J2** | Information geometry: Fisher-Rao on u-space | NQ-10 / CE-S2 |
| **J3** | Quantum-inspired: ψ = √u, C_t = interference | NQ-2 (CN7 third mode) |
| **J4** | Symplectic T*Σ_m Hamiltonian | post-Stage-1+ |
| **J5** | Random matrix: Hessian spectrum GOE/GUE | NQ-9 (sharper L_K) |
| **J6** | Turing pattern reaction-diffusion | extension §12 future |
| **J7** | Cellular automata Wolfram | (out of SCC scope) |
| **J8** | Neural field theory analogy | (out of mathematical scope) |
| **J9** | Noncommutative geometry / graph Dirac | post-Stage-1+ |
| **J10** | RG flow with K_soft as relevant operator | NQ-10 / Stage 3 |

**§J 합계:** USED 0, PARKED-as-inspiration 10. **모두 명시적으로 미래 후보로 보존.**

---

## §10. 살아남은 (USED) 가설의 substantive 소개 — Top 12

본 세션의 산출물에 핵심적으로 들어간 가설 중 **이 세션의 mathematical content 를 만들어낸** 12 개를 상세 소개:

### S1. A1 (Persistence-Weighted K_soft) — Definition Foundation

`K_soft(u) = Σ_i φ(ℓ_i)` 가 본 세션의 가장 중요한 정의 commit. canonical §5.5 의 H₀ persistence 사용 패턴 (CN12 commitment) 을 자연 확장. φ-saturating `φ(ℓ) = ℓ/(1+ℓ)` 가 default. **Cat A** Lipschitz via CSEH 2007 bottleneck stability. **이 commit 이 없었다면 G2/G3/G4/G5/G6 모두 시작 불가.**

### S2. A14 (Modica-Mortola Γ-conv → K_soft hard-K limit)

`K_soft(u_ε) → K · φ(1)` as `ε → 0` — sharp-interface limit 에서 K_soft 가 hard-K 의 `φ(1)`-rescaled version. 이는 (a) M-1 dissolution 의 isoperimetric reframing 의 수학적 핵심 (G5 §2), (b) K_soft 가 hard-K 의 graded relaxation 임의 보증.

### S3. B1 + B2 (Gibbs Z(T) finite + Bernoulli S 성질)

F-group 의 Cat A 핵심. Gibbs measure ℙ_T 가 finite normalizing constant 갖고, 엔트로피가 strictly concave on (0,1)^n. 이 둘이 **F-group 전체의 mathematical foundation**. Lemma 1.6, 1.7 of dev.

### S4. B5 (F4 T → 0 via Laplace)

`λ_K = γ_K T → 0` 와 결합하면 ℙ_T 가 ℰ minimizer 에 집중. Canonical v1.2 theory recovery 의 mechanism. (statement-only 이지만 framework 의 자기일관성 기둥.)

### S5. B9 (Witten Laplacian Helffer-Sjöstrand)

MO-1 dissolution 의 primary spectral 도구. `Δ_{ℱ, T}` 의 small eigenvalues 가 critical points 와 1-1 대응. `λ_1 ~ τ_0^{-1} exp(-ΔF/T)` 가 inverse Kramers — **G5 (Kramers) 와 G6 (Witten) 을 단일 spectral story 로 통합** (dev §3).

### S6. C1 (λ_K = γ_K · T scaling)

세 candidate (`λ_K ~ T`, `~ O(1)`, `~ β`) 중 첫 번째 채택. Clean F4 recovery + dimensional consistency (S, K_soft 모두 information-measure log-units). G3 §4.3 의 "**effective entropy** `S - γ_K K_soft`" 해석은 본 세션의 가장 elegant 한 conceptual move.

### S7. C5 + C6 (Modified Gibbs decomposition + information orthogonality)

`exp(-ℱ_C+E/T) = exp(-ℰ/T) · exp(S - γ_K K_soft)` — energy weight × complexity weight. CN5 의 "four-term independence" 를 자연스럽게 "six-term independence" 로 확장. C+E framework 이 canonical 과 conflict 없이 layer 추가됨을 보여주는 architectural 결과.

### S8. D1–D8 (F-1 dissolution 전체)

F-1 = "K=2 vacuous" 가 (a) 소프트-K 에서 architectural 으로 vacuous 개념 자체가 사라짐 (D1, D2), (b) thermal Gibbs 에서 K=2 가 Boltzmann factor 로 populated (D3-D7), (c) exp62/63 은 T=0 측정 (D8) — **8 가설 전수 활용**으로 F-1 의 "vacuity → thermal population" 재해석 완성.

### S9. E1 + E2 (M-1 = isoperimetric feature)

Modica-Mortola Γ-conv 가 single-mode 를 perimeter minimization 결과로 보장. M-1 은 **proved theorem** (T-Merge (b) Cat A) 이며 "feature, not bug" — 1 년 stuck 의 핵심 framing 오류 정정. canonical Cat A 보존 (no statement change).

### S10. E3 + E14 (Kramers MFPT τ ~ τ_0 exp(ΔE/T))

M-1 의 metastability 를 finite-T 정량 framework 로 격상. CN6 ("kinetically determined") 의 thermodynamic substantiation. Specific 예: T=1 에서 τ ≈ 11·prefactor (관측 가능), T=0.1 에서 τ ≈ 3·10^10 (eternal). exp55 zero-merge 도 Kramers 예측.

### S11. F1 + F2 + F5 (MO-1 architectural dissolution + Witten)

Σ²_M corner 가 soft-K 에서 사라짐 (F1). Σ_m^ε \ V 가 smooth manifold ⇒ standard Morse 적용 (F2). Witten Laplacian 이 spectral 대안 (F5). plan §G6 의 "3 alternative tools" 목표 달성: smooth Morse + Witten + (Forman 보존).

### S12. H1 (vineyard non-Lipschitz risk → false alarm)

가장 valuable 한 발견. `02_development.md` §4.1 counter-example attempt 에서 K_soft 가 vineyard 위에서도 **multiset-stable** 임을 보임 — 따라서 globally Lipschitz on Σ_m. G1 Cor 4.1 으로 강화. **risk 가 actually false** 였다는 결론은 본 세션 이전에는 모름.

---

## §11. Errata — G4 §3.3 Entropy 부호 정정

### 11.1 발견된 오류

`working/E/F1_dissolution.md` §3.3 Toy example 에서 다음 문장:

> *K=2 minimum: E_2 = 4.66, S_2 ≈ S_uniform · 0.85 (lower mode count → slightly lower S), K_soft(u_2^*) ≈ 2.*

**문제:**
1. 괄호 안 "lower mode count → slightly lower S" 가 부정확. K=2 는 K=1 보다 **mode 수가 더 많다** (2 vs 1). 따라서 "lower mode count" 표현 자체가 자기모순.
2. **S_2 < S_1 의 추정도 부정확.** Bernoulli 엔트로피는 사이트별 u-값의 intermediate-ness 를 잰다. K=2 는 두 개의 boundary band 를 가져 intermediate-u 사이트가 더 많다 ⇒ **S_2 > S_1** 가 옳다 (대략 boundary length 비율로).
3. 이로 인해 §3.3 의 모든 ℱ_1, ℱ_2, ΔF, Boltzmann ratio 수치 표가 잘못된 부호로 계산됨.

### 11.2 정정

S_1, S_2 의 추정치를 swap. 그리고 표를 다시 계산.

**올바른 estimates (n = 64, m = 10):**
- K=1 단일 응집체: 약 8-12 boundary 사이트가 intermediate u → S_1 contribution ~6 nats. S_1 ≈ 0.85 · n log 2 ≈ 37.7.
- K=2 두 응집체 (각 5 사이트): 두 boundary band 합 ~12-16 사이트 → S_2 contribution ~10 nats. S_2 ≈ 0.90 · n log 2 ≈ 39.9.
- 차이 ΔS = S_2 − S_1 ≈ 0.05 · 64 · log 2 ≈ +2.22 nats.

**올바른 ΔF_{2-1} 계산 (γ_K = 0.1, λ_K = 0.1·T):**

| T | ℱ_1 | ℱ_2 | ΔF_{2-1} | Boltzmann (K=2/K=1) | Regime |
|---|---|---|---|---|---|
| 0.1 | 2.25 - 3.77 = -1.52 | 4.66 - 3.99 + 0.02 = 0.69 | +2.21 | exp(-22.1) ≈ 2.5×10⁻¹⁰ | deeply zero-T, K=2 negligible |
| 0.5 | 2.25 - 18.86 = -16.61 | 4.66 - 19.95 + 0.10 = -15.19 | +1.42 | exp(-2.84) ≈ **0.058** | low-T, K=2 minority |
| 1.09 ≈ T_c | 2.25 - 41.10 = -38.85 | 4.66 - 43.51 + 0.22 = -38.63 | +0.22 | exp(-0.20) ≈ **0.82** | crossover |
| 2.0 | 2.25 - 75.40 = -73.15 | 4.66 - 79.85 + 0.40 = -74.79 | **−1.64** | exp(+0.82) ≈ **2.27** | mixed, K=2 entropically beginning to dominate |
| 5.0 | 2.25 - 188.51 = -186.26 | 4.66 - 199.71 + 1.00 = -194.05 | **−7.79** | exp(+1.56) ≈ **4.76** | high-T, K=2 strongly entropy-favored |

**T_c 계산:** `T_c = ΔE / ΔS ≈ 2.41 / 2.22 ≈ 1.09`.

### 11.3 정정의 함의 (qualitative)

올바른 부호 하에서 **새로운 정성적 결론**:

1. **저온 (T < T_c):** ΔF > 0 ⇒ K=2 minority. canonical "K=1 always preferred" 와 일관. Kramers metastable.
2. **임계온도 T_c ≈ 1.1:** K=1 과 K=2 가 거의 동등 weight (Boltzmann ratio ≈ 1).
3. **고온 (T > T_c):** **ΔF 가 음수가 됨** — 즉 entropy 가 energy gap 을 이김. K=2 가 thermodynamically preferred. 이는 canonical CN8 ("metastable, not globally optimal") 의 새로운 해석: 고온에서는 K=2 가 *오히려* 글로벌 optimal 일 수 있다.

이 정정은 **F-1 dissolution 의 narrative 를 강화**함:
- 저온: K=2 thermal minority (canonical 그림 유지) — F-1 의 vacuity 가 "Boltzmann 압축" 으로 dissolve.
- 고온: K=2 thermal majority — **canonical 의 zero-T 그림이 자체적으로 부적절** 임을 보여줌. P-F (zero-T metastability gap) 의 강력한 dissolution 증거.

### 11.4 정정 적용 위치

- `working/E/F1_dissolution.md` §3.3 — 표 + 본문 수치 + 부호 modify.
- 본 파일 §11 의 정정 기록 (위) — 변경 history.

---

## §12. 추가 Quality Review 발견사항

### 12.1 Minor — `working/E/M1_dissolution.md` §4.1 의 γ_eff 해석

원문: "0.89 = 2 × 0.445 → eigenvalue exponent 0.445 ~ ½ (naive)" — pre_brainstorm H-E4 에서 옮겨옴.

**검토:** 이는 pre_brainstorm 의 임시 가설이며 본 세션 산출물 G5 §4.1 에서는 "consistent-with-not-derived-from" 으로 약화 표현. 정확한 derivation 은 R-M1-C carry 에 명시. **No correction needed** — 이미 honest.

### 12.2 Minor — `working/CE/free_energy_wellposed.md` §1.2 의 "transport term 처리"

원문: "단일-시간-슬라이스 분석을 위해 ℰ_tr = 0 을 (i) 으로 처리". 

**검토:** 이는 명시적 commitment 이고 plan.md 의 "single-time slice" 흐름과 일치. carry-forward 는 §1.2 마지막에 명시. **No correction needed.**

### 12.3 Minor — `working/E/MO1_dissolution.md` §2.4 의 "Σ_m's hypercube corners (u_i ∈ {0,1}) remain"

이는 정확히 canonical Cat A Prop 1.1 (Σ_m convex polytope, manifold with corners) 에 명시된 내용. 본 세션의 dissolution 은 **Σ²_M corner 만 제거**, Σ_m corner 는 유지. 표현 "remain" 은 맞음. **No correction needed.**

### 12.4 Minor — `02_development.md` §3.2 Step 4 prefactor convention

`λ_1 = (1/2π)·|ω_s|·√(|det H_s|/det H_a) · exp(-ΔF/T)` 와 G5 §3.2 의 `τ = (2π/|ω_s|)·√(det H_a/|det H_s|) · exp(ΔF/T)` 가 정확히 inverse 관계 (각각 H_s 와 H_a 의 위치가 반전). 산출 일관. **No correction needed.**

### 12.5 Minor — F1 의 reflection condition (F3 statement)

`working/C/F_group_axioms.md` §3.1 statement 에서 "additional reflection condition at `∂[0,1]^n ∩ Σ_m` corners" 명시. canonical Σ_m 은 hypercube `[0,1]^n` 와 hyperplane `Σu_i = m` 의 교집합 ⇒ corners 는 hypercube boundary 와 hyperplane 의 교차에서 발생. 표현 정확. **No correction needed.**

### 12.6 Major potential issue — Ø detected.

전체 6 working files + 4 daily files 검토 결과, §11 의 G4 §3.3 entropy 부호 외 다른 substantive error 발견 안 됨. 일관성 통과.

---

## §13. Summary Statistics

### 13.1 By section (가설 풀의 channel rate)

| Section | Total | USED | PARTIAL USED | PARKED | REJECTED | UNTOUCHED | Channel rate (USED + PARTIAL) |
|---|---|---|---|---|---|---|---|
| **§A K_soft 정의** | 17 | 6 | 0 | 4 | 1 | 6 | 35% |
| **§B F-group** | 20 | 4 | 0 | 3 | 1 | 12 | 20% |
| **§C 교차 객체** | 10 | 4 | 0 | 3 | 2 | 1 | 40% |
| **§D F-1 dissolution** | 8 | 8 | 0 | 0 | 0 | 0 | **100%** |
| **§E M-1 dissolution** | 14 | 5 | 1 | 4 | 0 | 4 | 43% |
| **§F MO-1 dissolution** | 14 | 4 | 3 | 2 | 0 | 5 | 50% |
| **§G 교차 구조** | 7 | 3 | 2 | 0 | 0 | 2 | 71% |
| **§H Risk** | 11 | (different scheme — see §8) | | | | | 9/11 addressed |
| **§J Out-of-scope** | 10 | 0 | 0 | 10 | 0 | 0 | 0% (intentional) |
| **TOTAL (excl. H, J)** | 90 | 34 | 6 | 16 | 4 | 30 | **44%** USED+PARTIAL |
| Including J | 100 | 34 | 6 | 26 | 4 | 30 | (same) |

**관찰:**
- 본 세션의 "channel rate" (USED + PARTIAL ≈ 44% of non-Risk/non-J hypotheses) 는 plan.md 의 "Stage 1 first session 6 deliverables" scope 와 일치 — 1 일에 가설 풀의 절반 가까이 substantive 산출물에 들어옴.
- F-1 dissolution (§D) 가 100% 채택 — 가장 단순한 dissolution이라 가설 풀이 작고 모두 직접 사용.
- F-group (§B) 가 20% — 의도적 carry (F3 / F4 statement only, B6-B20 advanced 도구는 후속).
- §J 0% — 의도적 (out-of-scope).

### 13.2 살아남은 가설의 distribution by USE level

| USE level | Count |
|---|---|
| Foundation (commit / Cat A) | 9 (S1-S3, B1, B2, F1, F2 architectural, ℱ_C+E well-defined, λ_K = γ_K T) |
| Working tool (sketched / used in proof) | 13 (Modica-Mortola, Kramers, Witten, etc.) |
| Interpretation (cited but not central) | 5 (information geometry analogy, etc.) |
| Future activation (PARKED) | 16 |
| Out-of-scope inspiration (J series) | 10 |

---

## §14. Survival 의 의미

본 세션은 plan.md 의 6 deliverables 라는 **defined scope** 안에서 작동. 가설 채택 / 거부의 판단은:
1. **CN12 같은 canonical commitment 와의 호환성** — A3 reject 의 핵심 사유.
2. **수학적 도구의 가용성** — Witten Laplacian (B9) 가 Helffer-Sjöstrand 1985 라는 well-established theorem 으로 anchor 가능 → USED.
3. **Plan target 과의 직접 관련성** — out-of-scope (§J) 는 intentionally untouched.
4. **Risk reminder (§H) 의 직접 적용** — H5 (overfit) 에 따라 γ_eff 해석 weakening, H8 (scope creep) 에 따라 페이지 상한 유지.

**살아남은 가설의 ontological pattern:** 본 세션에서 USED 된 가설들은 **mathematical commit 가능한 것** + **canonical 과 minimal conflict** + **plan.md scope 내** 의 3 조건을 동시 만족. 거부된 가설들은 한 조건이라도 위반.

이 audit 자체가 **hypothesis-driven research** 의 자기 점검: pre_brainstorm 에서 광범위한 가설 풀을 생성한 뒤, session 중 어느 가설이 살아남는지를 explicit 하게 추적하는 메타 작업. 향후 세션 시작시 같은 audit 을 회고적으로 적용하면 "가설 채택률" 이라는 메타 지표 확보 가능.

---

## §15. 후속 세션을 위한 hypothesis-aware recommendation

### 15.1 PARKED 16 개 중 다음 세션에 활성화 가능 후보:

- **C-S2 / Stage 2:** B6 (Freidlin-Wentzell), C8 (crossover region), E5 (instanton), E11 (universality classes), F3 (Morse-Bott), F4 (stratified Morse).
- **CE-S2 / Stage 3:** A12 (RG block-spin), B16 (RG flow), C4 (4-corner phase diagram).
- **E-S3:** E8 (Ostwald ripening), E14 (lifetime concrete numerics), F10 (Forman alternative full).
- **Stage 5 (Numerical):** D8 (exp62/63 thermal redo), E11 (independent prediction test).

### 15.2 UNTOUCHED 30 개 중 후속 cycle 후보:

- A 시리즈 의 A5 (hybrid), A9 (sub-additivity), A13/15-17 (interpretive) — A-purpose follow-up.
- B 시리즈 의 B7-B20 (KL, Fisher, RG, SUSY 등) — Stage 2-3 axiom audit.
- C9 (degenerate lift) — CE-S2.
- E7/E9/E10/E12 (nucleation, mean curvature, glass, dynamic quench) — extension §12.
- F8/F11/F13/F14 (Hodge, Reeb, Floer, Cerf) — post-Stage-1+.

### 15.3 REJECTED 4 개의 재활성화 가능성:

- **A3 (simplex K_eff):** 활성화 조건 = CN12 weakening 사용자 동의.
- **B7 (KL divergence):** 활성화 조건 = "reference measure" 자연 선택 합의.
- **C2 (λ_K ~ β):** 활성화 조건 = T8-Core 와 호환되는 alternative scaling 발견 — 재고 없음.
- **C3 (λ_K ~ O(1)):** 활성화 조건 = F4 recovery 를 포기 (즉 canonical 과 다른 deterministic limit 수용) — 큰 commitment.

이 4 개는 **rejection 사유가 명시**되어 있으므로 향후 활성화 시 사유 reversal 이 명백해야 함.

---

**End of Hypothesis Audit.**
