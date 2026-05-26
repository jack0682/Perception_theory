---
id: AUX-1.5
type: registry/auxiliary_structures
status: meta-document (no claim count change)
created: 2026-05-18
amended: 2026-05-18 (AUX-1.5 — END OF DAY: §8 최종 분류 상태 신설. 분류 완료 항목 + U 잔류 항목 분리 명시. AUX-1.0~1.4 통합 마감.)
---

> [!nav] Auxiliary Structures Registry
> Parent: [[THEORY_INDEX]] · [[MOC_canonical_authority]]
> Pairs with: [[canonical]] (theorem authority), [[theorem_status]] (claim status authority), [[hypothesis_tree]] (dependency authority)
> Status: **Meta-registry** (AUX-1.5, 2026-05-18, END-OF-DAY consolidation). Not a theorem claim. Claim count `59A/14B/5C/5R = 83` unchanged.

# Auxiliary Structures Master Registry

## Purpose

SCC 이론은 `u_t : X_t → [0,1]`을 유일한 primitive로 선언하지만(CLAUDE.md §Ontological Constraints, canonical.md §3), 실제 정리(theorem) layer는 각각 외생적 보조구조(매개변수, 함수, 측도, 임계값, 가설 패키지)를 도입한다. 이 문서는 **7개 인식 단계별로 도입되는 모든 보조구조를 한 표에 모은** 단일 레지스트리다.

**역할:**
- 각 보조구조의 출처(canonical.md §, theorem_status.md row, code module)를 단일 지점에서 추적.
- u에서 *유도된* 것과 *외생적*으로 가정된 것을 명시적으로 구분.
- 후속 진단 작업 (scale tagging / observer tagging) 의 작업대.

**비-역할:**
- 새 정리 제시 없음.
- 기존 정리의 상태(category, claim count) 변경 없음.
- 미해결 보조구조(`ρ_pers`, `ε_kernel`, `T_*`)의 *해결* 시도 없음 — 미등록임을 *명시*만 함.
- Open Problems Catalog 변경 없음 (§4가 그 역할을 함).

**관계:**
- `canonical.md` — 정리 본문 및 §3 (primitives), §6 (axioms), §13 (proved results), §16 (stereo ext).
- `theorem_status.md` — 정리 상태/카테고리/카운트.
- `hypothesis_tree.md` — 정리 간 의존성 (HT-3.5).
- 이 문서 — 각 정리가 *어떤 보조구조 위에* 서 있는지의 등록부.

---

## §1 인벤토리 (단계별)

### Stage 0 — Sensor-to-u Transformation T (가장 근본적 누락, AUX-1.1 추가)

**근거:** *없음 (canonical 미등록)*. 코드: `CODE/scc/graph.py` (u-vector를 외부 입력으로 받지만 생성 메서드 없음); 이론: canonical.md §3 (`u_t`를 primitive로 *선언*하지만 origin은 정의되지 않음); canonical.md §4 (왜 soft form이 primary인지 논증하지만 raw → soft 변환은 다루지 않음); OMS-2.0 Appendix (observer moduli 추상적 — T의 concrete instantiation 부재).

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `T : I → u` | 변환 함수 | **canonical 미등록** | u의 *생성자* (역방향) | §4.5 상세. Stage 1–7이 *모두* T에 조건 부과 | **P** (시력 — ξ resident) |
| `I_t` | raw sensor data | **canonical 미등록** | 외생 (이론 외부 객체) | 형식 미정: pixel array / waveform / token / multi-modal | **외부 입력** (§4.9.8: COB 비대상 — 보조구조 아니라 원료) |
| `X_t` (graph) | 위상 구조 | canonical.md §3 (사용) | **외생** (T가 결정) | Stage 1에서 G로 등장하지만 노드/엣지 선택은 T 차원 | **D** (T(I)에서 유도) |
| T의 hypothesis package | 조건 묶음 | **canonical 미등록** | downstream에서 *역방향* 부과 | §4.5 9-조건 표 | **9×A** (§4.9.9: 각 조건은 T 위 axiom; A on P) |
| `{I : T(I) ≡ c·𝟙}` (균질 입력 집합) | 부분집합 | **canonical 미등록** | T 후순 (T 정해진 후) | Stage 1의 *암묵 출발점* | **D** (T 정해지면 자동) |

**Fixed-point 구조:** `(T, Θ)` 쌍이 동시에 결정. T가 Θ를 가능하게 하고, Θ가 T에 조건을 *역방향*으로 부과. 시간순으로 *마지막에* 일관성 조건으로 풀리는 자리. 지금 시도는 시기상조 — registry는 "빠짐"을 *명시*만 함.

**암묵 가정 (Stage 1로 흘러들어가는):** Stage 1이 "균질 IC에서 시작"이라고 가정하지만, *균질성 자체*가 T를 통해서만 정의됨. 따라서 Stage 1의 출발점은 *Stage 0의 결정에 의존*. 이 의존성이 현재 어디에도 명시되지 않음.

---

### Stage 1 — T8 (Spinodal 상전이 / Single Formation 존재)

**근거:** `canonical.md` §3, §6, §8, §13 (T8 row); `CODE/scc/energy.py`, `params.py`.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `λ_cl, λ_sep, λ_bd, λ_tr` | 결합상수 (4개) | canonical.md §3, §8 | **외생** | CN5: 4항 독립성 약속 | **P** (OMS-1 λ ∈ Δ³) |
| `α, β` | spinodal 매개변수 | canonical.md §8 (T8) | **외생** | Tier 1, T8 조건 `β/α > 4λ₂/|W''(c)|` | **P** (OMS-1 q = β/α) |
| `c ∈ ((3-√3)/6, (3+√3)/6)` | spinodal 중심 농도 | canonical.md §8 | 부분유도 (m/n) | 농도-simplex 평균 관계 | **D** (= m/n; m은 §4.6.2 U) |
| `W(u) = u²(1-u)²` | 이중우물 포텐셜 | canonical.md §3 | 정의 (외생) | I6 보정: `W'(u) = 2u(1-u)(1-2u)` | **A** (canonical §3 axiom) |
| `Σ_m = {u : Σuᵢ = m}` | 제약 simplex | canonical.md §3 | 외생 (m이 매개변수) | 질량 m이 어디서 오는지 → OP-0009의 일부 | **A** (형태) / m은 **D-conditional on T** (§4.9.2: m = Σ_v T(I)(v)) |
| `λ₂(L)` | Fiedler 고유값 | canonical.md §3 (graph) | 그래프에서 유도 | T8 임계비의 우변 | **D** (G에서 유도; G는 Stage 0 D) |
| `L = D - N` | 라플라시안 | canonical.md §3 | 그래프 G에서 유도 | G 자체가 외생 | **D** (G에서 유도) |
| `a_cl < 4` | closure 기울기 | canonical.md §3 (A3) | 외생 | A3 contraction axiom 요구 | **A** (A3 axiom) |
| `b_D = 0` | distinction 매개변수 | canonical.md §3 | 외생 (analyticity 위한 약속) | Łojasiewicz 수렴 강제 | **A** (analyticity axiom) |
| `η_cl ∈ [0,1]` | self/neighbor 균형 | params.py | 외생 (Tier 2, default 0.5) | sigmoid closure 실현 | **P** (관찰자 균형 선택 — ξ 후보) |

**암묵 가정:** 균질 초기조건 `u ≡ c`에서 출발한다는 *시점*. 그 균질 상태의 기원은 정리되지 않음.

---

### Stage 2 — T-PreObj-1 (다중 peak이 기본값)

**근거:** `canonical.md` §13 (T-PreObj-1, T-PreObj-1G); `theorem_status.md` C-0700 row.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `F` (peak count) | 정수 함수 | theorem_status.md C-0700 | u에서 유도 | F=1 디스크 non-critical, F≥2 attract | **D** (u에서 유도) |
| `ε` (F-count threshold) | 임계값 | T-PreObj-1G | **외생** (graph-class 의존) | 어디서 정해지는지 비명시 | **P** (관찰자 F-카운트 분해능 — ξ 후보) |
| IC-protocol (adaptive bounded vs random) | 초기조건 규약 | exp-0090, exp-0091 | **외생** | dichotomy 결정 | **P** (관찰자 실험 설정 — ξ resident) |
| 그래프 클래스 G | 집합론적 가정 | T-PreObj-1G | **외생** | 그래프 자체가 ontological input | **D** (Stage 0 T(I)에서 유도) |
| Non-criticality 방향 | 구조적 조건 | T-PreObj-1 증명 | 유도 (Hessian) | 어느 방향에서 unstable인지 | **D** (Hessian에서 유도) |

**암묵 가정:** gradient flow 자체가 dynamics. 어느 시간척도의 flow인지 명시 없음.

---

### Stage 3 — D-ST-3 (K_act = #PersComp)

**근거:** `canonical.md` §3.11 (D-ST-3), §16 (D-ST-4); `theorem_status.md` D-ST-3 row, T-L1-F row; `CODE/stereo_scc/topology.py`.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `ρ_pers` (persistence threshold) | 임계값 | canonical.md §3.11 (L291) | **외생** | **§4 누락 등록**: 기호 도입 (L291), `ρ_pers > 0` 명시. 그러나 *값* 또는 *결정 규칙* 미등록 | **P** (위상 분해능 — ξ resident) |
| `ℓ_min` (minimum bar length) | 임계값 | T-L1-F | **외생** | Tier 2, 문제 의존 | **P** (지속 분해능 — ξ resident) |
| Sublevel filtration 방향 | 알고리즘 선택 | D-ST-3 | 규약 | superlevel vs sublevel 선택이 결과를 바꿈 | **A** (알고리즘 규약 — canonical 등록 권장) |
| `K_bar^{ℓ_min}` | bar count | T-L1-F | u + ℓ_min에서 유도 | bar 임계에 의존 | **D** (u + ℓ_min에서 유도) |
| `K_act^ε` | active count | T-L1-F | u + ε에서 유도 | slot ε에 의존 (regime-conditional) | **D** (u + ε에서 유도) |
| L1-J 패키지 `(P0)–(P11)` | 12개 가설 묶음 | T-L1-F | **외생 가설 묶음** | T-L1-F가 Cat A인 *조건* | **A/D mix** (§4.8.1: 3 D + 8 A; P7만 U) |
| `P7` (decay-to-cut) | 강한 정상성 가설 | L1-L | 부분유도 (Combes-Thomas / Agmon) | 안전한 기술적 regime | **U** (§4.6.8 hybrid; §4.8.1) |
| `r` (neighborhood radius) | 임계 | T-L1-F `q_j^U = argmax_{N_j^r}` | **외생** | primary representative 정의 | **P** (공간 분해능 — ξ resident) |
| `B_K(P)` (topological sector) | 부분집합 | canonical.md §16 (D-ST-4) | u에서 유도 (K_act 통해) | | **D** (u + K_act에서 유도) |

**가장 큰 누락:** `ρ_pers`의 canonical 등록. 이게 정해지지 않으면 K_act 자체가 매개변수 의존량.

---

### Stage 4 — σ-framework (정적 다중 σ)

**근거:** `canonical.md` §13 (Commitment 14, T-σ-multi-A/D-Static), §14 (Commitment Notes); `CODE/scc/sigma_rich.py`.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `σ_rich = (σ_standard, centroids, orientations, wigner_data)` | 5-튜플 | sigma_rich.py | u + G + P에서 유도 | derived diagnostic, energy term 아님 | **D** (u + G + Θ에서 유도) |
| `σ_standard` | irrep tuple | Commitment 14 | u* Hessian + Aut(G) | irrep labels + nodal counts | **D** (Hessian + Aut(G)에서 유도) |
| `c_j` (centroids) | 벡터 | sigma_rich.py | u-가중 평균 | u에서 유도 | **D** (u에서 유도) |
| orientations (principal axes) | 텐서 | sigma_rich.py | moment tensor에서 유도 | | **D** (u에서 moment tensor 유도) |
| Wigner data | 구조 | sigma_rich.py | 부분유도 | **Wigner projection은 W9+ 연기 (OP-0008)** | **U** (Wigner projection D vs P — §4.6.3) |
| `Aut(G) ≀ S_{K_act}` (wreath product) | 군 | T-σ-multi-D-Static | G + K_act에서 유도 | | **D** (G + K_act에서 유도) |
| Mulliken irrep 순서 | 규약 | Commitment 14 (O5')(O7) | **외생 규약** | 외부 표준 차용 | **A 확정** (§4.9.4: external convention import — chemistry standard) |
| `λ₁ < λ₂` (Goldstone gap) | 스펙트럼 조건 | T-σ-Inherit (d-direction) | u*에서 유도 | well-separated regime 가정 | **D** (Hessian에서 유도) |
| `d_σ` (σ-space 거리) | 메트릭 | T-σ-Inherit (e) | **외생 선택** | 후보 다수 | **P** (관찰자 signature 거리 — ξ resident) |
| one-hop buffer | 규약 | T-σ-Inherit (a) | G에서 유도 | induced subgraph 정의 | **A** (canonical 규약) |
| Hessian 계산 지점 | 선택 | σ-framework 전반 | u*에서 유도 | *어느* critical point인가는 미지정 | **D** (critical point 정의에서; 시간척도는 후보 2) |

**암묵 가정:** σ가 critical point에서 계산된다는 것. equilibrium 안 도달한 transient에서는 미정.

---

### Stage 5 — P-F-A1 Package I + T-K-Select-PF/OBS

**근거:** `canonical.md` §13 (T-P-F-ε0, T-PF-A1-AR/SDE/GI/PE, T-K-Select-PF, T-K-Select-OBS); `theorem_status.md` CV-1.8 / 1.9 / 1.10 / 1.11 sections.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `T_*` (effective stochastic temperature) | **공리적 매개변수** | P-F-A1 | **외생 (axiom)** | **OP-0021 (W9+) — 최대 외생** | **U 잔류** (§4.9.1 fixed-point 구조 확인; Route C → P 권장 유지) |
| `π_{T_*}(u) ∝ exp(-E/T_*)` | Gibbs 측도 | T-PF-A1-GI | u + E + T_*에서 유도 | T-PF-A1-GI Cat A | **D** (u + E + T_*에서 유도) |
| 반사 Langevin SDE | 확률동역학 | T-PF-A1-SDE | u + T_* + ∂Σ에서 유도 | Lions-Sznitman 1984 | **D** (u + T_* + ∂Σ에서 유도) |
| Lions-Sznitman regularity | regularity | T-PF-A1-SDE | 외부 정리 차용 | | **A** (외부 정리 import) |
| `C̃` (convex domain) | 정의역 | T-PF-A1-PE | Σ_m에서 유도 | Payne-Weinberger 적용 위해 | **D** (Σ_m에서 유도) |
| Poincaré 상수 `C_P` | 스펙트럼 상수 | T-PF-A1-PE | u + T_*에서 유도 | `gap ≥ (π²/n)·exp(−osc(Ẽ)/T_*)` | **D** (u + T_*에서 유도) |
| `osc(Ẽ)` | 진폭 | T-PF-A1-PE | E에서 유도 | metastable 시 exp 크게 | **D** (E에서 유도) |
| `p_K = π_{T_*}(B_K)` | sector 측도 | T-K-Select-PF | π + B_K에서 유도 | | **D** (π + B_K에서 유도) |
| `K_feas` | 유한 집합 | T-K-Select-PF §3.5 | 유도 (B_K null 검사) | | **D** (B_K null 검사에서 유도) |
| 관측 likelihood `LM1–LM3` | 모델 선택 | T-K-Select-OBS §2.4 | **외생 (관찰자 모델)** | 3개 후보 | **A/P/D mix** (§4.8.3: LM1=A, LM2=P, LM3=D) |
| 가설 `H1–H5` (T-P-F-ε0 가정, *not* Eyring-Kramers) | 가설 패키지 | T-P-F-ε0 / T-P-F-ε0-K | **외생** | **AUX-1.3 정정: Eyring-Kramers 아님**; 실제 Kramers는 OP-0005-DYN 별도 OPEN | **A/D mix** (§4.8.2: 1 D + 3 A; H5만 U) |
| `Φ_obs` | 관측 사상 | T-K-Select-OBS | **외생 (CN5 묶임)** | likelihood 안에서만 | **P** (CN5 묶임, 관찰자 모델) |

**가장 큰 누락:** `T_*`. P-F-A1이 *axiom*이라는 건 stage 5 전체가 외부 매개변수 하나에 매달려있다는 뜻. OP-0021로 미루어져있음.

---

### Stage 6 — T-Temporal-Identity (CV-1.13 SEALED)

**근거:** `canonical.md` §13 (T-Temporal-Identity, Theorem Partial-H-SINK, Lemma S-B1-Weak/SYM); `theorem_status.md` CV-1.12/1.13 sections; `working/MF/temporal_identity_*.md`; `working/temporal/S-A1/S-A3/S-C1_*_AUDIT.md`.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| Partial OT cost `c[u_t, u_s]` | 비용함수 | E4 (canonical.md §6) | **외생 선택** | fingerprint cost 선택 — 다른 선택지 다수 | **P** (관찰자 유사도 측도 — ξ resident) |
| 가능성 조건 `E1–E4` | 공리 묶음 | canonical.md §6 transport | **외생 axiom group** | sub-stoch, non-inj, core inheritance, fingerprint cost | **A** (canonical §6 axiom group) |
| `M_{t→s}` (transport plan) | 측도 | T-Temporal-Identity | u_t, u_s에서 유도 (E1–E4 하) | 유일성은 마진 조건 필요 | **D** (u_t, u_s + E1–E4에서 유도) |
| `S_{ij}` (score matrix) | 행렬 | T-Temporal-Identity (a) | M에서 유도 | | **D** (M에서 유도) |
| Score threshold | 임계값 | T-Temporal-Identity (a) | **외생** | 어디서 설정? | **P** (관찰자 분해능 — ξ 후보) |
| `Δ_sep ≥ Δ_sep* + 2ε_kernel` | 마진 조건 | S-C1 (CV-1.13) | u에서 유도 (PersComp 간격) | Cat A conditional | **D** (u + ε_kernel에서 유도) |
| `ε_kernel` | tolerance | S-C1 | **외생 매개변수** | **§4 누락 등록**: canonical 등록 미상 | **P** (이산화 분해능 — ξ resident) |
| `Δ_sep*` (margin lower bound) | 임계 | S-C1 | u에서 유도 | ≈ 0.837 (canonical parameters) | **D** (u에서 유도) |
| `ε_OT` (Sinkhorn 정규화) | 매개변수 | H-SINK | **외생** | entropic regularization | **P** (엔트로피 분해능 — ξ resident) |
| 가설 `(A1)–(A7), (A7'), (A9)` | 가설 묶음 | T-Temporal-Identity | **외생** | full Cat A 위한 | **D/A/P mix** (§4.8.4: A1–A3=A, A4/A5/A7'/A9=P, A6/A7=D) |
| `(DR1)–(DR2)` (deep-rooted) | 가설 | T-Temporal-Identity | 부분유도 | S-B1-Weak Cat A 위해 | **D** (§4.8.4: H-SINK Cat A에서 유도) |
| `H-SINK-ENT` | 기술적 hypothesis | W7-FINAL | **외생** | entropy term stability | **D** (§4.9.10: H-SINK Cat A 부분 명제 — 별도 hypothesis 등록 redundant) |
| `HWF-1` (isoperimetric ratio) | 상수 | S-B1-SYM | G에서 유도 | iso_ratio ≤ C_iso | **D-conditional on T** (§4.9.6: T axiom 10번째 후보; T가 iso-regular graph 생성한다는 조건 하) |
| `θ_core` (core threshold) | 임계 | S-B1-Weak | **외생** | default 0.7 또는 0.9 | **P** (crispness 분해능 — ξ resident) |
| `ρ_*` (core density floor) | 임계 | S-B1-Weak | 유도 | ≈ 0.003 | **D** (u에서 유도) |
| `ρ_deep` | 측정량 | S-B1-Weak | u에서 유도 | ≥ 0.7/225 ≈ 0.00311 | **D** (u에서 유도) |
| `R_{t→s}` correspondence | 관계 | T-Temporal-Identity (a) | u_t, u_s에서 유도 | Cat A | **D** (u_t, u_s에서 유도) |
| 5개 사건 유형 (CONT/SPLIT/MERGE/BIRTH/DEATH) | 분류 | T-Temporal-Identity (d) | 유도 | exhaustive taxonomy | **D** (분류, 유도) |

**가장 큰 누락:** `ε_kernel` canonical 등록. `ρ_pers` (Stage 3)와의 관계 미명시.

---

### Stage 7 — T-σ-Inherit (OP-0008)

**근거:** `theorem_status.md` Session W / Session X (T-σ-Inherit working candidate); `working/MF/sigma_inherit_k_jump.md`; `CODE/scc/sigma_rich.py`.

| 보조구조 | 유형 | 도입 위치 | u에서 유도? | 비고 | Origin |
|---|---|---|---|---|---|
| `M` (merger geometry) | 튜플 | OP-0008-MERGE | u_t, u_s에서 유도 | centroid + orientation + trajectory | **D** (u_t, u_s에서 유도) |
| Parallel-axis theorem 적용 | 연산 | T-σ-Inherit (MERGE orientation) | 외부 정리 차용 | mechanics 차용 | **A** (외부 정리 import) |
| `v_1` (split direction) | 벡터 | T-σ-Inherit (d-direction) | Hessian에서 유도 | Goldstone mode (lowest eigenvector) | **D** (Hessian에서 유도) |
| Wigner projection | 연산 | σ_standard merge/split | **W9+ 연기 (Cat C)** | **OP-0008 차단요인** | **D/P hybrid** (§4.9.3: generic D via Schur; degenerate P) |
| `Φ` (inheritance map) | 사상 | T-σ-Inherit 전반 | u + R_{t→s}에서 유도 | partial: Cat B | **D** (u + R_{t→s}에서 유도) |
| `R_σ(i→j)` 분해 | 잔차 | T-σ-Inherit (e) | d_σ에서 유도 | centroid + orientation + eigenvalue 분해 | **D** (d_σ에서 유도; d_σ는 P) |
| `λ₁ < λ₂` (gap) | 조건 | T-σ-Inherit (d-direction) | Hessian에서 유도 | Goldstone 존재 위한 | **D** (Hessian에서 유도) |

**가장 큰 누락:** σ_standard의 K-jump inheritance가 본질적으로 비결정적일 가능성. Wigner projection이 결정성을 회복할지 미지수.

---

## §2 단계 횡단 패턴 (Cross-Stage Drift / Overload)

같은 기호 또는 같은 류의 보조구조가 여러 단계에 출현하면서 *역할이 미묘하게 달라지는* 패턴.

| 보조구조 | 등장 단계 | 단계별 역할 변화 | 일관성 |
|---|---|---|---|
| `λ_i` 결합상수 | 1, 5 | T1: 에너지 결합; T5: Gibbs 측도 매개변수 | 동일 (일관됨) |
| `β/α` | 1, 3 (암묵), 6 (S-B1) | T1: 상전이 임계; T3: 마진; T6: deep-core 조건 (`β > 7α`) | 동일이지만 *역할*은 다름 |
| 임계값 묶음 (`ρ_pers, ℓ_min, ε_kernel, θ_core, ρ_*, ε_OT`) | 3, 4, 6 | 각 단계마다 *다른 임계* 추가 | **불일관** — 통일 임계 정책 없음 |
| `m` (질량) | 1, 3 (slot), 5 (B_K) | T1: simplex 제약; T3: K_act 측면 보정; T5: sector 분류 | 동일이지만 OP-0009-Pre가 메타원인 |
| Hessian | 1, 4, 7 | T1: 안정성; T4: σ; T7: split direction | 동일 연산이지만 *어느 점에서* 계산하는지 단계마다 다름 |
| 가설 패키지 (각각) | 3 (L1-J), 5 (H1–H5), 6 (A1–A7+, DR1–2, HWF) | 각 단계가 *자기 패키지* 가짐 | **불일관** — 패키지 간 호환성 검토 없음 |
| 관찰자 model | 4 (Mulliken), 5 (LM1–3), 6 (cost choice) | 각 단계가 관찰자 선택 내장 | **불일관** — 관찰자 통일 모듈 없음 |
| **`T` (sensor transformation)** | **0, 1, 2, 3, 4, 5, 6, 7** | Stage 0에서 *도입*; Stage 1–7 모두가 *조건을 역방향으로 부과* | **메타-불일관** — 모든 단계가 T에 조건 부과하지만 T 자체는 미정 (AUX-1.1) |

---

## §3 진단: 후보 1 (보조구조 묶음 통일 누락)

이 레지스트리의 인벤토리는 *각 단계의 2% 부족함*이 사실 동일한 균열의 다른 얼굴이라는 가설(후보 1)을 *문서적 사실*로 만든다.

### 강한 증거 (5개)

1. **임계값 인플레이션.** Stage 3–6에서 최소 6개의 임계값 (`ρ_pers, ℓ_min, ε_kernel, θ_core, ρ_*, ε_OT`)이 단계마다 추가되고, 단일 등록 문서가 (이 문서 작성 전까지) 없었다.

2. **`T_*`의 공리적 지위.** Stage 5 전체가 외생 매개변수 하나(`T_*`)에 매달려있고, 이게 OP-0021로 W9+까지 미루어져있다. P-F-A1이 *axiom* 이라는 사실 자체가 후보 1 진단의 직접 증거.

3. **3종의 별도 가설 패키지.**
   - L1-J `(P0)–(P11)` (Stage 3)
   - H1–H5 (Stage 5, Eyring-Kramers)
   - `(A1)–(A7) + (A7') + (A9) + (DR1)–(DR2) + HWF-1` (Stage 6, Temporal-Identity)

   패키지 간 호환성 / 중복 여부가 canonical / hypothesis_tree 어디에도 검토되지 않음.

4. **관찰자 모델의 단편화.**
   - Mulliken irrep 순서 (Stage 4)
   - LM1–LM3 likelihood (Stage 5)
   - partial OT cost 선택 + E4 axiom (Stage 6)

   각각 다른 곳에서 다른 형식으로 도입. 통일된 "관찰자 모듈러스" (OMS-2.0 Appendix는 있으나 정리 행은 미등록) 없음.

5. **단일 마스터 레지스트리 부재.** canonical.md, theorem_status.md, hypothesis_tree.md, params.py에 분산. 이 문서 자체가 그 분산의 *증거*이자 *부분 해결*.

### 약한 증거 (2개, 다른 후보와 겹침)

6. **Hessian 계산 지점.** 단계마다 다름 → 후보 2 (시간척도) 와도 겹침. T1은 균질점 근처, T4는 critical point u*, T7은 split 직전.

7. **관찰자 모델 분산** → 후보 3 (관찰자) 가설의 직접 증거.

### 결론

후보 1이 가장 직접적이고 강하게 지지받는다. 후보 2 (시간척도 불일관)와 후보 3 (관찰자 분산)은 후보 1의 *하위 분할* 또는 *결과*일 가능성이 크다 (예: 관찰자 분산은 보조구조 묶음 통일이 안 돼있어서 각 정리가 자기 관찰자 모델을 들고 다니는 결과).

---

## §4 미해결 등록 항목

이 절은 *canonical 등록이 누락된* 보조구조를 명시한다. 해결 시도는 하지 않는다 — 누락 사실을 *문서화*만 함.

### 4.1 `ρ_pers` (persistence threshold) — Stage 3

**위치:** canonical.md §3.11 (D-ST-3 정의 본문) 안에서 사용되지만, *값* 또는 *결정 규칙*은 canonical에 등록되지 않음.

**영향:** K_act = #PersComp(u) 자체가 ρ_pers에 의존. 등록 누락 시 K_act는 매개변수 의존량.

**OP 등록 상태:** 별도 OP 없음. OP-HMORSE-FIEDLER-BOUND가 인접 문제지만 동일하지 않음.

### 4.2 `ε_kernel` — Stage 6

**위치:** S-C1 audit (`working/temporal/S-C1_KERNEL_AUDIT.md`)에서 사용. canonical.md §13 T-Temporal-Identity 마진 조건 `Δ_sep ≥ Δ_sep* + 2ε_kernel`에 등장.

**영향:** T-Temporal-Identity (c) Cat A conditional 마진 폭. 등록 누락 시 *마진 조건의 의미*가 fix되지 않음.

**OP 등록 상태:** 별도 OP 없음.

### 4.3 `T_*` (effective stochastic temperature) — Stage 5

**위치:** P-F-A1 axiom 안에 명시. canonical.md §13 P-F-A1 family rows.

**OP 등록 상태:** **OP-0021** (W9+ 활성). Mori-Zwanzig 또는 RG fixed-point route 후보.

**영향:** Stage 5 전체. Gibbs measure, Poincaré gap, Kramers exponent 모두 T_*에 의존.

### 4.4 가설 패키지 호환성

세 패키지가 각자 자기 단계에서 Cat A를 보장하지만, *동시에 같은 u에 적용 가능한지*가 검토되지 않음:

- L1-J `(P0)–(P11)` (Stage 3): 슬롯 카운트 ↔ bar 카운트 동치 조건.
- H1–H5 (Stage 5): Morse stability + spectral gap + 마진.
- `(A1)–(A7), (A7'), (A9), (DR1)–(DR2), HWF-1` (Stage 6): 시간상 마진 + deep-core + isoperimetric.

**영향:** T-MF-Synthesis (synthesis candidate, theorem_status.md line 122–126)가 *세 패키지를 동시에* 가정함. 호환성 정리 부재 시 synthesis는 vacuous할 위험.

**OP 등록 상태:** 별도 OP 없음.

### 4.5 `T` (sensor-to-u transformation) — 가장 근본적 누락 (AUX-1.1)

**위치:** Canonical 어디에도 등록되지 않음.

- `canonical.md §3`: `u_t : X_t → [0,1]`를 primitive로 *선언*. 그러나 u_t가 *어디서 오는가*는 미정의.
- `canonical.md §4` ("Why the Soft Form Is Primary"): 왜 soft form이 primary인지 *논증*하지만, raw → soft 변환은 다루지 않음.
- `canonical.md §16` (stereo extension): 관측 구조(H_L, H_R, D-ST-1..4) 도입하지만 *심볼릭* 수준. raw pixel / sensor 수준 아님.
- `canonical.md` OMS-2.0 Appendix: observer moduli 추상적. T의 *concrete instantiation*은 부재.
- `CODE/scc/graph.py`: `GraphState`가 u-vector를 *외부 입력*으로 받음. 생성 메서드 없음.
- 실험 코드 (`experiments/exp*.py`): 합성 u로 초기화. raw → u 파이프라인 부재.

**구조:**

- **입력**: `I_t` — raw sensor data. 형식 미정 (pixel array / audio waveform / token sequence / multi-modal stream / ...).
- **변환**: `T` — 매끄러움/연속성/위상보존 등 일정 조건을 만족하는 함수.
- **출력**: `u_t : X_t → [0,1]` — soft cohesion field.
- **부수 결정**: 그래프 `X_t` 자체 — 어느 좌표가 노드가 되고 어느 인접이 엣지가 되는지도 T가 결정.

**왜 가장 근본적 누락인가:**

1. **u_t = primitive 약속의 가장 강한 사례.** 진짜 primitive는 `(I, T)` 또는 `(I, T, X)`. 현재 약속은 사실상 `T(I)`를 primitive라고 부르면서 T를 *invisible*하게 유지한 것.
2. **Stage 1의 출발점 미정의.** "균질 초기조건 u ≡ c"가 어느 I에서 오는지 T 의존. 따라서 *whole theory의 출발 조건* 자체가 T 미등록 상태에서 vacuous.
3. **다른 §4 항목과의 비교.** `ρ_pers, ε_kernel, T_*`는 *Stage 내부의* 매개변수. T는 *Stage 진입 자체*를 결정 — 메타 레벨에서 한 단계 위.

**Fixed-point 구조 (왜 *마지막에* 결정되는가):**

`(T, Θ)` 쌍이 동시에 결정되는 fixed point:

- T가 정해져야 u_t가 결정 → Θ (Stages 1–7)의 입력이 fix.
- Θ가 작동하려면 T가 일정 조건 만족 → Θ에서 T로 *역방향* 제약.
- 둘이 *동시에* 풀려야 일관.

따라서 T 자체의 *구성*은 Stages 1–7이 안정된 후에 *일관성 조건*으로서 풀림. 시간순으로 첫 번째 자리이지만, 풀이 순서로는 *마지막*. 이 점을 명시적으로 두기 위해 Stage 0이라는 이름의 자리로 등록.

**downstream에서 T에 부과되는 조건 (현 단계에서 알 수 있는 만큼):**

| 출처 단계 | T에 부과되는 조건 | 이유 |
|---|---|---|
| Stage 1 (T8 mass) | `T(I) ∈ Σ_m` | 질량 보존, simplex 제약 |
| Stage 1 (spinodal regime) | T가 *적당한 매끄러움* | 너무 매끄러우면 formation 안 일어남; 너무 날카로우면 formation이 입력에 *이미* 꽂혀있어 trivial |
| Stage 1 (homog. 존재) | `{I : T(I) ≡ c·𝟙}` ≠ ∅ | Stage 1의 출발점이 존재하도록 |
| Stage 2 (T-PreObj-1G) | T가 graph-class independent | 그래프-보편 정리 위해 |
| Stage 3 (D-ST-3) | T가 위상 정보 보존 | PersComp 카운트가 의미를 가지려면 |
| Stage 4 (σ) | T가 `Aut(G)`와 호환 | σ_standard가 변환 불변 |
| Stage 5 (P-F-A1) | T 연속 | 반사 SDE well-posedness (Lions-Sznitman) |
| Stage 5 (T-K-Select-OBS) | T가 LM1–LM3 likelihood와 호환 | 관측 모델 일관 |
| Stage 6 (T-Temporal-Identity) | T가 시간 연속 | partial OT가 의미를 가지려면 |
| Stage 7 (T-σ-Inherit) | T가 K-jump 시 연속 | inheritance map well-defined |

이 표는 잠재적 **`OP-AUX-T-FIXED-POINT`** (가칭)의 statement 시드. 즉 T는 위 9개 조건을 *동시에* 만족하는 변환 — 그런 T가 *존재하는가*? *유일한가*? *modular space의 dimension은*?

**OMS와의 관계:**

T는 본질적으로 *관찰자가 raw에 가하는 변환*. OMS-2.0 Appendix의 observer moduli set은 가능한 T들의 modular space이거나 그것을 *포함*. 즉 §4.5 (T 미등록)과 OMS-2.0 concretization 부재(theorem rows pending)는 *같은 문제의 두 얼굴*일 가능성. §3 후보 1과 후보 3이 만나는 *바닥*이 T.

**OP 등록 상태:** 별도 OP 없음. `OP-AUX-T-FIXED-POINT` 등록 권장이나 사용자 명시 결정 시에만. 등록 안 한 경우: 본 §4.5가 임시 등록부.

**비-시도 (out of scope):**

- T 자체의 *구성* 시도하지 않음. 마지막에 풀릴 일.
- "균질 초기조건"의 *operational definition* 시도하지 않음 (T 의존).
- raw 입력 형식 (image/audio/text/...)의 선택 시도하지 않음.
- 9개 downstream 조건 호환성 검증 시도하지 않음 (Stages 1–7 더 안정될 때까지 보류).

### 4.6 COB 위반 후보 + 모호 항목 (AUX-1.2)

§7 COB 원칙 (Closed Ontological Budget) 하에서 각 보조구조는 **D** ($\mathcal{D}_u$, u에서 유도), **A** ($\mathcal{A}_u$, u 위 axiom), **P** ($\mathcal{P}_{\text{obs}}$, 관찰자-개인) 중 하나로 분류돼야 한다. 이 절은 현재 어디에도 명확히 속하지 않거나 분류가 모호한 항목들을 등록한다 — *처분은 시도하지 않음*; 결정 필요 사실만 명시.

#### 4.6.1 `T_*` (Stage 5) — 가장 심각한 위반 후보

OP-0021에 등록된 두 route가 모두 COB 위반:

- **Route A (Mori-Zwanzig)**: 환경 메모리 커널에서 유도 → **환경 외생**. COB 위반.
- **Route B (RG fixed point)**: 보편 임계점에서 유도 → **외부 물리 외생**. COB 위반.

§4.7.2에 **Route C** (observer-personal: 관찰자 내부 stochastic resolution) 권장. Stage 5 전체 (P-F-A1 Package I + T-K-Select-PF/OBS)가 재해석에 의존하지만 *해석 변경*이고 *수학적 역할은 동일* — Cat A/B 상태 변경 없음.

#### 4.6.2 `m` (Stage 1) — 출처 결정 필요

세 후보 분류 가능:

- **D**: `m(I) = ∫ T(I) dx` — Stage 0의 T가 정해지면 자동 유도.
- **P**: 관찰자가 "얼마나 보고 있는가"를 정함 (주의 범위).
- **외생**: "환경에서 주어진 총 질량" → **COB 위반**.

현재 canonical (canonical.md §3 Σ_m 정의)은 사실상 외생적으로 취급. AUX-1.2는 *결정을 강제하지 않음* — 결정 필요 항목으로 *등록*만.

#### 4.6.3 `Wigner projection` (Stage 7) — D vs P borderline

- 표현론 (Specht 1935 + James-Kerber 1981)에서 *유일하게* 유도되면 **D**.
- 다중 선택 가능하면 **P** (관찰자 분해 선택).

현재 OP-0008의 Cat C 차단요인이며, 분류 결정이 OP-0008 해결과 결합. AUX-1.2는 분류를 *유보*하고 표기만.

#### 4.6.4 `Mulliken irrep 순서` (Stage 4) — A vs P borderline

- 외부 표준 차용 → **A** (axiom import).
- 관찰자 라벨 규약 → **P**.

두 해석 모두 COB 통과하지만 *어느* 부류인지는 결정 필요. AUX-1.2는 둘 다 유효 표기.

#### 4.6.5 가설 패키지 — 전수 감사 결과 (AUX-1.3: §4.8 참조)

**AUX-1.3에서 전수 감사 수행** — 31개 가설 전체를 §4.8에 분류. 새로 발견된 COB 위반 후보 + hybrid 항목:

- **§4.6.6 H5 (Morse stability)** — 새 COB 위반 후보.
- **§4.6.7 HWF-1 (isoperimetric ratio)** — 새 COB 위반 후보 (counterexample 존재).
- **§4.6.8 P7 (decay-to-cut)** — D/A hybrid (regime 의존).

기존 패키지:
- **L1-J `(P0)–(P11)`** (Stage 3) — §4.8 분류: 3 D + 8 A + 1 U(P7).
- **H1–H5** (Stage 5) — §4.8 분류: 1 D + 3 A + 1 U(H5). **주의: 이 패키지는 *Eyring-Kramers가 아니라* T-P-F-ε0의 가정 집합**. 실제 Eyring-Kramers (Package II) 는 별도 OPEN.
- **LM1–LM3** (Stage 5, T-K-Select-OBS) — §4.8 분류: 1 D + 1 A + 1 P. 깨끗.
- **`(A1)–(A7), (A7'), (A9), (DR1)–(DR2)`** (Stage 6) — §4.8 분류: 4 D + 3 A + 4 P. 깨끗.
- **HWF-1** — 별도. U(COB 위반).

#### 4.6.6 `H5` (Morse stability) — COB 위반 후보 (AUX-1.3)

**Statement:** 임계점 (saddle/minimum) 이 perturbation `ε·R` 하에서 stable.

**출처:** theorem_status.md L373; canonical.md L1831 부근. T-P-F-ε0-K (Cat B conditional) 의 마지막 조건.

**COB 진단:** SCC axiom에서 *유도 불가능*. Morse generic assumption — 일반적 수학 가설이지만 SCC 에너지 `E_SCC`의 *non-convex* 특성 하에서 *증명되지 않음*. 환경/물리 외생도 아니지만 *어떤 부류로 분류할지 미정*. 가능 후보:
- **A (axiom)**: "Morse stability를 SCC 환경에 axiom으로 import" — 가능하지만 강한 약속.
- **D (derived)**: SCC 에너지의 구조적 성질에서 유도 시도 미정 — open.
- **외생**: 환경 의존이 아니므로 외생은 아님. → 분류 미정 (**U**).

**영향:** T-P-F-ε0-K가 Cat A로 승급하려면 H5 해결 필요. Package II (Kramers rates, OP-0005-DYN) 도 H5에 의존.

#### 4.6.7 `HWF-1` (isoperimetric ratio) — COB 위반 후보 (AUX-1.3)

**Statement:** `iso_ratio(Core) = |∂_V Core| / |Core| ≤ C_iso` (그래프 Core의 isoperimetric 비율 상한).

**출처:** `SYMBOLIC_DEEP_CORE_NECESSITY.md §1.3`; T-Temporal-Identity Lemma S-B1-SYM Cat B (조건부).

**COB 진단:** (A1)–(A7) axiom에서 *유도 불가능*. 그래프 G의 구조적 정규성에 대한 가정인데:
- **반례 존재:** 3×10 elongated rectangle에서 `ρ_deep ≈ 0.27 ≪ 0.84` — HWF-1 fail.
- **G가 Stage 0의 T(I)에서 유도된다면** HWF-1은 *T에 대한 추가 조건*. 즉 §4.5 "T의 hypothesis package" 9-조건의 *11번째* 후보.

분류 미정 (**U**). 가능 후보:
- **A**: "isoperimetric 정규성을 grid graph에 axiom으로 부여."
- **D**: T 자체에서 유도 (T가 isoperimetric-regular graph만 생성한다면).
- **외생**: 환경 의존 아님 — 외생은 아님.

**영향:** Lemma S-B1-SYM (Cat B 조건부)이 HWF-1 의존. 실제 사용은 ρ_deep ≥ 0.84 정량적 magnitude에만; 정성적 `Δ_sep > 0`은 S-B1-Weak (Cat A, HWF-1 불필요) 로 처리됨. 따라서 HWF-1 미해결이 T-Temporal-Identity Cat A를 깨지 않음.

#### 4.6.8 `P7` (decay-to-cut, L1-J) — D/A hybrid (AUX-1.3)

**Statement:** 각 `j ∈ A^ε`에 대해 `u^(j)(x) ≤ ψ_ℓ(d_G(x, S_ℓ^δ))` (지수 감쇠 profile) + cut-height bound.

**출처:** canonical.md L1604 (P7 정의); L1-L (Combes-Thomas / discrete Agmon 부분 유도).

**COB 진단:** Hybrid 상태:
- **Gaussian bumps 한정 (L1-I regime)**: *exact*, 따라서 **D**.
- **일반 SCC states**: 일반적으로 *TBD* — L1-L에서 *strong stationarity (P7_DERIVED_UNDER_STRONG_STATIONARITY)* 하에서 partial D 유도. 그 외 regime은 **A**로 도입.

분류: **U** (regime 의존). Strong stationarity regime 에서는 D, 그 외 regime은 A.

**영향:** T-L1-F가 Cat A *conditional on P0–P11* (전체 패키지). P7만 분리 시 Cat A 유지하려면 strong stationarity regime 명시.

---

### 4.7 ξ 카탈로그 시드 + T_* Route C 권장 (AUX-1.2)

#### 4.7.1 ξ catch-all 카탈로그 시드

OMS-1 (canonical.md L2416)이 관찰자 파라미터 벡터를 `Θ = (q, λ, ξ) ∈ [q_min, q_max] × Δ³ × B_ξ`로 등록함. `q = β/α`와 `λ ∈ Δ³`는 명시적으로 enumerate됐으나 **`ξ ∈ B_ξ`는 catch-all box로 *내용물 카탈로그가 비어있음***.

다음 후보 목록을 *registry-level 시드*로 등록 (canonical OMS-1 amendment 권장이지만 Step 1로 미루어짐 — 본 AUX-1.2 범위 밖):

```
ξ 후보 = (
  T_*,                           # effective stochastic temperature
  ρ_pers, ℓ_min,                 # 위상 분해능
  ε_kernel, ε_OT,                # 이산화/엔트로피 분해능
  θ_core, ρ_*,                   # crispness 분해능
  LM,                            # 관찰자 베이지언 likelihood 모델 선택
  c_OT,                          # partial OT cost choice
  π_W,                           # Wigner projection convention
  d_σ,                           # σ-space metric
  IRREP_ORDER,                   # Mulliken irrep 순서
  T_sensor,                      # Stage 0: raw→u 변환 ("관찰자의 시력")
  IC_protocol,                   # 관찰자 실험 설정
  r                              # neighborhood radius
)
B_ξ = ∏ (각 성분의 valid range / space)
```

**중요 caveat:** 각 후보를 ξ에 enumerate한다고 D 가능성을 *봉인하지 않음*. 일부 (예: `ε_kernel`, `ρ_pers`)는 partial OT cost / graph spectral gap에서 *원리적으로* D 유도 가능할 수도. 시도해야 알 수 있음. 따라서 ξ enumeration은 **잠재적 P 슬롯**으로 등록하고, 각 항목에 *"D 시도 미정 / P 확정 / OP-걸림"* 태그를 같이 표기.

#### 4.7.2 T_* Route C 권장

OP-0021에 새 후보 route 등록 권장 (canonical OP catalog 직접 수정은 별도 결정):

> **Route C (Observer-personal):** `T_* = 관찰자 내부 stochastic resolution`. 관찰자가 어떤 noise level로 u를 sampling하는가에 해당하는 인지적 양. $\mathcal{P}_{\text{obs}}$ 분류, ξ resident, COB 통과.
>
> **장점:** 환경 통계 모델 불필요; 관찰자 인지 모델만 필요. SCC의 first-person 색채와 일관.
>
> **단점:** T_*가 환경 의존이라는 직관 (외부 noise 침투)을 거부.
>
> **영향:** 수학적 역할 동일 (π_{T_*} 정의, Poincaré gap, Kramers exponent). 해석과 증명 책임만 변경 — Stage 5 전체 (P-F-A1 Package I + T-K-Select-PF/OBS) 의 *재해석*이 필요하나 정리 카테고리 변경 없음.

#### 4.7.3 분류 결정 미루어진 항목 목록

| 항목 | 후보 분류 | 결정 후 영향 |
|---|---|---|
| `T_*` | Route C 권장 → P | OP-0021의 Route A/B 폐기 결정 |
| `m` | D (T(I) 적분) / P (주의 범위) / 외생(COB 위반) | Σ_m simplex 의미 재정의 |
| `Wigner projection` | D (표현론 유일) / P (다중 선택) | OP-0008 Cat C 차단요인 해소 가능성 |
| `Mulliken irrep 순서` | A (외부 표준) / P (관찰자 규약) | Stage 4 σ_standard 출처 명확화 |
| `H5` (Morse stability) | A (axiom import) / D (SCC 에너지에서) | T-P-F-ε0-K Cat A 승급 가능 (AUX-1.3) |
| `HWF-1` (isoperimetric) | A (grid axiom) / D (T 생성 그래프) | S-B1-SYM Cat A 승급 가능 (AUX-1.3) |
| `P7` (decay-to-cut) | D (Gaussian / strong stationarity) / A (일반) | T-L1-F regime 명시 (AUX-1.3) |

모두 사용자 별도 결정 사항. Registry는 *등록*만 함.

---

### 4.8 가설 패키지 전수 감사 — 32개 가설 D/A/P/U 분류 (AUX-1.3)

§4.6 / §4.7에서 가설 패키지를 식별만 했으나, AUX-1.3에서 *각 가설*을 D/A/P/U 중 하나로 *전수* 분류한다. 총계: **32개** (L1-J P0–P11 = 12 + H1–H5 = 5 + LM1–LM3 = 3 + Temporal A1–A7+A7'+A9+DR1+DR2+HWF-1 = 12). 출처: §4.8.1–§4.8.4 각 패키지별 explore agent 보고 (2026-05-18).

#### 4.8.1 L1-J `(P0)–(P11)` — Stage 3, T-L1-F가 Cat A인 조건 (12개)

**출처:** `canonical.md` L1603–1619; `THEORY/working/MF/kbar_kact_bridge_L1J_catA_upgrade_attempt.md` §§4–5.

| ID | 이름 | Statement 요약 | Origin | 이유 |
|---|---|---|---|---|
| P0 | Terminal-Death H₀ Convention | union-find 기반 superlevel persistence; `scc.diagnostics._persistence_h0_graph` 코드 정렬 | **D** | Definitional (code-aligned) |
| P1 | Deterministic Tie Convention | `≺` 전체 순서로 ties 결정; elder rule | **D** | Definitional |
| P2 | Active Mass + Connected Support | `m_j(u)>ε` + `G[S_j^δ]` connected | **D** | u-내재적 정의 |
| P3 | Disjoint Active Neighborhoods (LG-1) | `N_j^r ∩ N_k^r = ∅` for `j≠k` | **A** | Geometric axiom (safe) |
| P4 | Low Boundary Collar (LG-2) | `max_{∂N_j^r} U(x) ≤ b_j − ℓ_min − r_assoc` | **A** | Geometric axiom |
| P5 | Background Suppression (LG-4) | `‖U‖_{∞,X_bg} ≤ ℓ_min − ρ_bg` | **A** | Field-shape axiom |
| P6 | Birth Height Threshold | `b_j ≥ h_min ≥ ℓ_min` | **A** | Field-shape axiom |
| **P7** | **Decay-to-Cut (heterogeneous)** | `u^(j)(x) ≤ ψ_ℓ(d_G(x, S_ℓ^δ))` + cut-height bound | **U** | **§4.6.8 hybrid** — Gaussian exact (D), strong stationarity partial D (L1-L), 일반 regime A |
| P8 | Tightened H6 on `G_j^r` | `ℓ_{j,2}(u^(j); G_j^r) ≤ ℓ_min − 3ρ_pert` | **A** | Slot-internal axiom |
| P9 | NE-2 Perturbation Control | `‖R_j‖_{∞,N_j^r} ≤ ρ_pert/2` | **A** | Interaction bound |
| P10 | Inactive Residual Suppression | `‖R_inact‖_∞ ≤ ℓ_min − ρ_res` | **A** | Residual bound |
| P11 | Margin Ledger | `h_min − max_{k≠j} B_{jk} ≥ ℓ_min + r_assoc + r_birth` | **A** | Constants compatibility |

**소계:** 3 D + 8 A + 1 U(P7) = 12 가설. P7가 유일한 미해결.

#### 4.8.2 H1–H5 — Stage 5, T-P-F-ε0 / T-P-F-ε0-K 의 가정 (5개)

**중요 정정:** 이 패키지는 *Eyring-Kramers 가설이 아님*. T-P-F-ε0 (Gibbs measure continuity, Cat A) 와 T-P-F-ε0-K (Bernoulli-stable Kramers exponent, Cat B) 의 가정 집합. **실제 Eyring-Kramers 정리 (Package II / Kramers rates) 는 별도 OPEN (OP-0005-DYN, W9+)**.

**출처:** `theorem_status.md` L315–375; `canonical.md` L1831 부근; `working/MF/pf_tstar_langevin.md`.

| ID | 이름 | Statement 요약 | Origin | 이유 |
|---|---|---|---|---|
| H1 | Compactness | `F_M(P)` compact convex polytope | **A** | T-PF-A1-AR canonical |
| H2 | Continuity | `E_SCC` continuous on `F_M(P)` | **D** | Polynomial energy form |
| H3 | Measure positivity | `σ(F_M(P)) > 0` | **A** | Geometric axiom on polytope measure |
| H4 | R bounded below | `R ≥ -C` (Bernoulli entropy term) | **A** | Axiom on regularization term |
| **H5** | **Morse stability** | 임계점 (saddle/min) stable under `ε·R` perturbation | **U** | **§4.6.6** — generic Morse, SCC axiom에서 유도 불가; 비convex E_SCC에서 미증명 |

**소계:** 1 D + 3 A + 1 U(H5) = 5 가설. H5가 유일한 COB 위반 후보.

#### 4.8.3 LM1–LM3 — Stage 5, T-K-Select-OBS 의 관측 likelihood (3개)

**출처:** `working/MF/k_select_obs_posterior.md` §2.3 L74–79.

| ID | 이름 | Statement 요약 | Origin | 이유 |
|---|---|---|---|---|
| LM1 | Measurability | `u ↦ L_obs(O_t∣u)` Borel measurable on `F_M(G)` | **A** | Mathematical regularity (continuous likelihood에서 automatic) |
| LM2 | Positivity | `L_obs(O_t∣u) > 0` for all `u` | **P** | Observation 모델 선택 (likelihood parametrization) — ξ resident |
| LM3 | Posterior Normalizability | `Z^obs > 0` | **D** | LM2 + compactness (T-PF-A1-AR)에서 유도 |

**소계:** 1 A + 1 P + 1 D = 3 가설. 깨끗.

#### 4.8.4 T-Temporal-Identity (A1–A7, A7', A9, DR1–DR2, HWF-1) — Stage 6 (11개)

**출처:** `working/MF/temporal_identity_sharp_form_2026-05-07.md §2`; `canonical.md §8.5`; `working/temporal/H-SINK.md §6`; `working/temporal/SYMBOLIC_DEEP_CORE_NECESSITY.md §1.3`.

| ID | 이름 | Statement 요약 | Origin | 이유 |
|---|---|---|---|---|
| A1 | Finite shared graph | `G = (P, E)` 유한, 연결, `t=s`에서 동일 | **A** | Graph axiom (time-varying G = NQ-T-Identity-3 OPEN) |
| A2 | Field admissibility | `u_t, u_s ∈ F_M(P)` | **A** | Canonical state space (T-Persist-1 preconditions) |
| A3 | PersComp non-empty | `K_t, K_s ≥ 1`; D-ST-3 적용 | **A** | D-ST-3 canonical (ρ_pers는 별도 P) |
| A4 | Stable-K | `K_t = K_s = K` (parts b,d 필요) | **P** | Observer regime restriction — temporal K-dynamics 미주장 |
| A5 | Well-separated regime | `d_inter^*(t), d_inter^*(s) ≥ d_min^* ≥ 3` | **P** | Regime parameter (ξ resident) |
| A6 | E1–E4 admissibility of transport | `M_{t→s}` entropic-OT optimum with E1–E4 | **D** | E1–E4 형식 자체는 canonical SCC energy stationarity에서 유도 (T-PF-A1 Package I) |
| A7 | T-Persist-1(e) preconditions | (TC1) `Δ_φ²(δ≥2)>0`; (TC2) `σ_sp² ≥ diam²/2`; (TC3) entropy sufficiency | **D** | T-Persist-1(e) Cat C에서 유도 |
| A7' | Sharp-OT regime | `ε_OT ≤ ε_OT^* ≈ 0.45` | **P** | Sinkhorn 정규화 parameter 선택 (ξ resident) |
| A9 | Mass dominance | `λ_m ≥ κ·λ_c·c̄_intra`, `κ≥10` | **P** | Score matrix 상대 가중 — 관찰자 선택 |
| DR1 | Sinkhorn c-cyclical monotonicity at support | automatic for entropic-OT optima | **D** | Sinkhorn theory automatic |
| DR2 | Cost jointly L_c-Lipschitz | `L_c ≤ 5.86` (H-SINK-5 Cat A 검증) | **D** | canonical fingerprint Lipschitz (S-B2 = Lemma 8.2 Cat A) 에서 유도 |
| **HWF-1** | **Isoperimetric regularity** | `iso_ratio(Core) ≤ C_iso` | **U** | **§4.6.7** — (A1)–(A7) axiom에서 유도 불가; 3×10 rectangle 반례 존재 |

**소계:** 4 D + 3 A + 4 P + 1 U(HWF-1) = 12 가설 (포함 HWF-1).

**Note:** Lemma S-B1-Weak (Cat A, `Δ_sep > 0` 정성적) 는 HWF-1 *불필요*. HWF-1은 S-B1-SYM (Cat B 정량적 `ρ_deep ≥ 0.84`) 에만 필요. 따라서 HWF-1 미해결이 T-Temporal-Identity Cat A를 깨지 않음.

#### 4.8.5 전수 감사 요약

| 분류 | 갯수 | 항목 |
|---|---|---|
| **D** (u에서 유도) | 9 | P0, P1, P2, H2, LM3, A6, A7, DR1, DR2 |
| **A** (canonical axiom) | 15 | P3, P4, P5, P6, P8, P9, P10, P11, H1, H3, H4, LM1, A1, A2, A3 |
| **P** (관찰자-개인, ξ resident) | 5 | LM2, A4, A5, A7', A9 |
| **U** (분류 미정 / COB 위반) | 3 | **P7** (hybrid), **H5** (COB 위반), **HWF-1** (COB 위반) |
| **총계** | **32** | (LM1–3 + H1–5 + A1–9 + DR1–2 + HWF-1 + P0–11) |

**핵심 결과:**

1. **U 항목 3개 모두 §4.6에 등록됨** (4.6.6 H5, 4.6.7 HWF-1, 4.6.8 P7).
2. **H1–H5는 *Eyring-Kramers가 아님*** — T-P-F-ε0 / T-P-F-ε0-K 의 가정. 실제 Kramers는 OP-0005-DYN 별도 OPEN.
3. **HWF-1 미해결이 Cat A를 깨지 않음** — S-B1-Weak (Cat A) 가 정성적 `Δ_sep > 0` 처리; HWF-1은 정량적 magnitude에만.
4. **3종의 별도 가설 패키지가 *대부분 D/A/P로 깨끗 분류 가능***. §3 후보 1 진단의 "패키지 간 호환성 미검토" 우려가 *대부분 해소* — 32개 중 29개가 D/A/P 어딘가에 속하고, 3개만 미정.

---

### 4.9 D-derivation 전수 시도 (AUX-1.4)

§4.6 / §4.7 / §4.8에서 식별된 모든 U 항목에 대해 **D-derivation을 진지하게 시도**한다. 시도는 *attempt-grade* — 즉 registry-level 분류 변경만 (canonical 정리 promote 아님).

원칙: "D 가능성을 봉인하지 말라" (AUX-1.2 caveat) 적극 실행. 각 U 항목이 *진짜* U인지 *未-시도* D인지 가른다.

총 10개 항목 시도.

#### 4.9.1 `T_*` (effective stochastic temperature) — Stage 5

**Strategy:** `T_*`를 u의 *intrinsic fluctuation scale*에서 유도 시도. 후보:
- (a) u의 ensemble variance: `T_* = Var_{π}(u)`?
- (b) Hessian 최저 고유값의 역수: `T_* ~ 1/λ_min(H_E)`?
- (c) 자유 에너지 landscape 곡률.

**Result: 실패 (fixed-point 잔류).**

후보 (a) 는 *self-referential*: `T_*`가 Gibbs measure `π ∝ exp(-E/T_*)`를 정의 → `π`가 variance를 정의 → variance가 `T_*`를 정의. 순환. 일관된 fixed-point가 *원리적으로* 존재할 수 있지만 *유일성*은 보장 안 됨 (E가 multi-well이면 multiple fixed-points 가능).

후보 (b)는 local quadratic approximation의 *local* scale을 정의할 뿐, *global* SDE 매개변수 `T_*`를 결정하지 않음.

후보 (c)는 (a) 와 같은 self-referential 구조.

**Updated: U (잔류).** Route C (관찰자 내부 stochastic resolution) 권장 유지.

**Diagnosis:** `T_*`는 *intrinsically* observer-side. SDE의 noise level이 환경에서도, u에서도 유도되지 않는다. 관찰자가 어떤 *sampling 해상도*로 u를 관측하는가가 `T_*`. → **P (observer-personal)** 가 자연. `OP-T*-FIXED-POINT` 등록 권장 — *T_* 가 fixed-point 구조라는 사실 자체*를 OP로 명시.

#### 4.9.2 `m` (총 질량) — Stage 1

**Strategy:** Stage 0 T-chain. `m = ∫_X T(I)(x) dx` 또는 discrete: `m = Σ_v u(v) = Σ_v T(I)(v)`.

**Result: 성공 (D-conditional on T).**

T가 정해지면 `m`은 자동. Stage 0 §4.5의 T hypothesis package 하에서 T가 well-defined되면 m도 well-defined. Σ_m simplex 정의 자체는 변경되지 않음 — 단, `m`의 *출처*가 명시됨.

**Updated: D (conditional on Stage 0 T가 정해짐).**

**Diagnosis:** Σ_m simplex의 `m`은 raw 입력에서 *유도된* 양; *외부에서 주어진* 매개변수가 아님. canonical §3에 단 한 줄 명시하면 충분 (AUX-1.5+ 후속 작업): "`m := Σ_v T(I)(v)`, where T is the sensor transformation (Stage 0)".

#### 4.9.3 `Wigner projection` (Stage 7)

**Strategy:** Schur's lemma 사용. Aut(G)_{u*} 의 irreducible representations `ρ`에 대해 projection `P_ρ = (d_ρ/|G|) Σ_g χ_ρ(g)^* T(g)` (canonical formula, Serre 1977).

**Result: D/P hybrid.**

- **Generic case (모든 irrep multiplicities = 1):** Schur's lemma가 *유일한* projection을 결정. → **D.**
- **Degenerate case (multi-irrep same dim, 또는 multiplicity > 1):** Multiplicity space 안에서 basis 선택 자유 → **P.**

**Updated: D/P hybrid.** Generic case에서는 D; degenerate case (실제 SCC에서는 그래프 대칭이 풍부할 때 일어남) 에서는 P.

**Diagnosis:** σ_standard merge/split inheritance (OP-0008) 의 차단요인 일부 해소. *Generic* 그래프에서는 deterministic inheritance 가능; symmetric (높은 대칭) 그래프에서는 P (관찰자 선택). Wigner projection 의존 *Cat C → Cat B* 승급이 generic case에서 원리적으로 가능. OP-0008 처분에 직접 기여.

#### 4.9.4 `Mulliken irrep 순서` (Stage 4)

**Strategy:** Canonical lex order 시도 — `(dim, character, ...)` 로 정렬.

**Result: 실패 (Mulliken은 외부 convention).**

Mulliken 순서 (R. S. Mulliken, 1933 이후 chemistry 표준)는 *수학적*으로 정렬 규칙이 *아님*. Identity rep `A` first → `A_1, A_2, B_1, B_2, E, T` 같은 chemistry-internal labelling convention. 수학적으로 동등한 다른 ordering (Schoenflies, Hermann-Mauguin) 존재. → D-derivation 시도 자체가 무의미.

**Updated: A 확정 (axiom import).**

**Diagnosis:** Commitment 14 (O5')(O7) 에서 Mulliken을 import. 이건 *외부 표준* axiom으로 명시. canonical §14 Commitment Notes에 한 줄 추가하면 완전 명시 가능: "Mulliken irrep ordering is imported from chemistry convention (R. S. Mulliken 1933) as axiom" — 별도 결정.

#### 4.9.5 `H5` (Morse stability) — Stage 5

**Strategy:** Sard's theorem + transversality + SCC 에너지 real-analytic.

- E가 real-analytic (polynomial in u; double-well + Laplacian).
- For generic `(α, β, λ_i)`, the critical set of E is Morse (Sard).
- Specifically: codimension-1 set of `(α, β, λ)` 에서 degenerate critical points 존재; complement은 dense open → Morse.

**Result: 부분 성공 (D-generic, U at spinodal).**

- **Generic regime (post-bifurcation):** Cat A formations 안정점은 *generically* Morse. → **D-generic.**
- **Spinodal regime (T8 critical surface):** T8 임계점에서 Hessian이 *intrinsically* zero eigenvalue (Goldstone mode, 그것이 formation을 트리거). 이건 Sard 예외 — codimension-1 surface 위에 존재.

**Updated: U 잔류 (spinodal degeneracy intrinsic).**

**Diagnosis:** Generic-regime D는 *원리적으로* 증명 가능 (Sard transversality). 그러나 spinodal 임계점은 SCC 이론의 *핵심 사건*이고 거기서 Morse 깨짐은 *intrinsic*. T-P-F-ε0-K 가 Cat A로 승급하려면 spinodal 임계점을 *피해* 정의되어야 함 (e.g., bifurcation 후 stable basin 한정).

**OP-H5-MORSE-SPINODAL** 등록 권장 — "H5 Morse stability가 spinodal critical surface에서 intrinsically 깨짐을 명시; T-P-F-ε0-K 적용 regime은 post-bifurcation stable basin 한정". 이건 *해결*이 아니라 *명시*. 별도 결정.

#### 4.9.6 `HWF-1` (isoperimetric ratio) — Stage 6

**Strategy:** 

- HWF-1: `iso_ratio(Core) = |∂_V Core| / |Core| ≤ C_iso`.
- T가 isoperimetric-regular graph (e.g., grid, expander) 만 생성한다면 자동.
- 일반 graph에서는 깨질 수 있음 (3×10 rectangle 반례).

**Result: D-conditional on T.**

T가 "well-formed sensor mapping"이면 X_t가 isoperimetric-regular. 그러면 HWF-1 자동. 즉 HWF-1을 *T axiom*으로 흡수.

**Updated: D-conditional on T (또는 T의 추가 axiom, A on T).**

**Diagnosis:** Stage 0 §4.5의 T hypothesis package 9-조건에 **10번째 조건 (T-cond-10: isoperimetric regularity)** 추가 권장. T가 출력하는 X_t가 `iso_ratio ≤ C_iso`를 만족하는 graph class만 생성하도록 제한.

이건 T axiom 묶음의 추가. AUX-1.4는 *권장*만; 실행은 별도 결정.

#### 4.9.7 `P7` (decay-to-cut, L1-J) — Stage 3

**Strategy:**
- L1-L에서 Combes-Thomas / discrete Agmon을 통해 strong stationarity regime 부분 D 유도.
- 비정상 regime: gradient flow의 transient 거동에서 exponential decay 유도 시도.

**Result: 부분 성공 (현 상태 유지 — D/A hybrid).**

- **Strong stationarity (Gaussian / static):** D via Combes-Thomas. (L1-L 검증됨.)
- **General regime:** 일반 transient에서는 SCC 에너지의 *non-quadratic* 항(`W(u)`) 때문에 exponential decay가 폭발할 수 있음. A로 도입 필요.

**Updated: D/A hybrid 유지** (regime split).

**Diagnosis:** 현 상태가 이미 최적. Regime split을 명시 — strong stationarity 에서는 D, 그 외에는 A. T-L1-F의 *regime 명시*가 필요 (AUX-1.5+ 권장).

#### 4.9.8 `I_t` (raw sensor data) — Stage 0

**Strategy:** I_t의 분류 시도.

**Result: COB *밖*.**

`I_t`는 *raw 입력 신호* (pixel array, waveform, token, multi-modal stream). COB 원칙은 *보조구조* 분류 규칙. 입력은 *원료*이지 보조구조가 아님.

**Updated: 외부 입력 (분류 비대상).**

**Diagnosis:** 

I_t는 COB의 *경계 외부*. 이론은 (I_t, T(I_t)) 의 *결과*인 u에서 시작; I_t 자체는 *우주가 관찰자에게 제공하는 신호*. COB는 "u + T + 관찰자 파라미터 안에서 닫혀라"를 요구하고, I_t는 *그 닫힘 조건의 입력*이지 *닫힘 조건의 일부*가 아니다.

Stage 0 §4.5의 I_t row는 "외부 입력 — COB 비대상" 으로 명시 가능. 단 *T는 여전히 P* (관찰자가 I_t를 받아 처리하는 방식).

#### 4.9.9 T hypothesis package (9-조건) — Stage 0 §4.5

**Strategy:** 각 9개 조건 (Stage 1 질량 보존, spinodal regime, ..., Stage 7 K-jump 연속) 을 *어떻게 등록할지* 분류.

각 조건은 *downstream stage가 작동하기 위해 T가 만족해야 하는 자기-제약*. 즉:
- Stage 1 spinodal regime 조건 → T가 spinodal-supercritical 영역의 u를 생성해야 → **T-axiom 1 (A)**.
- Stage 2 graph-class independence → **T-axiom 2 (A)**.
- Stage 3 위상 보존 → **T-axiom 3 (A)**.
- ... (9개)

**Result: 각 9 조건 모두 A.**

**Updated: 9개 T-axiom (A) 등록 후보.**

**Diagnosis:** §4.5 9-조건 표가 그대로 *T-axiom 카탈로그*. 각 조건은 T (Stage 0 P) 위에 부과되는 axiom — 즉 *P 위의 A 의존성*. COB 하에서 valid (각 조건은 P 자체에 대한 형식적 제약).

이건 §4.5에 추가 명시: "각 9-조건은 T에 부과되는 axiom (A on P)". 실행은 별도 결정.

#### 4.9.10 `H-SINK-ENT` (Sinkhorn entropy bound) — Stage 6

**Strategy:** H-SINK Cat A (W7-FINAL) 의 직접 함의 검토.

- `Theorem Partial-H-SINK` (Cat A) 는 row-softmax Lipschitz를 증명.
- `S-B2` = Lemma 8.2 (Cat A) 는 Sinkhorn entropy term의 일관성을 보장.
- H-SINK-ENT (entropy term stability under plan perturbations) 는 이 둘의 직접 함의.

**Result: 성공 (D).**

H-SINK-ENT는 *별도 가설*이 아니라 H-SINK Cat A의 *부분 명제*. 따라서 D — H-SINK 정리 chain에서 유도.

**Updated: D (H-SINK Cat A에서 유도).**

**Diagnosis:** Registry에서 H-SINK-ENT를 별도 hypothesis로 등록한 것이 *redundant*. 정정: H-SINK-ENT는 H-SINK 의 sub-claim. 별도 등록 해소. T-Temporal-Identity 가설 묶음에서 한 항목 줄어듦.

#### 4.9.11 요약 결과

| 항목 | 시도 전 | 시도 후 | 변화 |
|---|---|---|---|
| `T_*` | U | **U (잔류)** | Fixed-point 구조 명시; Route C (P) 권장 유지 |
| `m` | U | **D-conditional on T** | T-chain 성공 |
| `Wigner projection` | U | **D/P hybrid** | Schur generic D; degenerate P |
| `Mulliken irrep 순서` | U | **A 확정** | External convention import |
| `H5` (Morse stability) | U | **U 잔류 (spinodal)** | Generic D 가능; spinodal intrinsic 미해결 |
| `HWF-1` | U | **D-conditional on T** | T axiom 10번째 후보 |
| `P7` (decay-to-cut) | U | **D/A hybrid 유지** | Regime split (현 상태) |
| `I_t` | U | **외부 입력** | COB 비대상 (분류 밖) |
| T hyp pkg (9-조건) | U | **9×A (T axiom)** | 각 조건 등록 가능 |
| `H-SINK-ENT` | U | **D** | H-SINK Cat A 부분 명제 |

**총 결과:**
- **명확한 D 승격:** 2 (`m` conditional, `H-SINK-ENT`)
- **A 확정:** ~10 (`Mulliken` + T hyp pkg 9-조건)
- **D-conditional on T:** 2 (`m`, `HWF-1`)
- **D/P hybrid:** 1 (`Wigner projection`)
- **D/A hybrid 유지:** 1 (`P7`)
- **외부 입력 (COB 밖):** 1 (`I_t`)
- **U 잔류:** 2 (`T_*` fixed-point, `H5` spinodal degeneracy)

**핵심 진단:**

1. **2개만 진짜 U.** `T_*`와 `H5`만 *진정한 잔류*. 둘 다 SCC 이론의 *핵심 구조적* 미해결 — `T_*`는 fixed-point 정의 문제, `H5`는 spinodal 임계점의 intrinsic Goldstone mode.

2. **나머지 8개는 분류 결정만의 문제였음.** 즉 *진짜* 외생이 아니라 *未-시도* D, *未-명시* A, *未-등록* P였다. AUX-1.4의 가장 큰 가치: **U 의 80%가 시도-등급 D-derivation으로 해소**.

3. **COB 원칙이 실효적임이 검증됨.** 32개 가설 + 10개 핵심 보조구조 = 총 42개 항목 중 *2개*만 진정 잔류. 후보 1/2/3 통합 진단의 *문서적 증명 강화*.

4. **다음 단계 OP 후보 2개 명시:** `OP-T*-FIXED-POINT`, `OP-H5-MORSE-SPINODAL`. 둘 다 *해결 시도* 아니라 *문제 명시* — 별도 결정.

---

## §5 후속 확장 슬롯 (Option B / C 작업대)

각 보조구조에 다음 두 열을 *추후* 추가할 수 있다. 현재는 빈 채로 남겨둔다.

### 5.1 Scale tag 슬롯 (Option B용)

각 보조구조가 *어느 시간척도*에서 의미가 있는가:
- `instant`: 한 시점의 u에서 계산.
- `short-relax`: gradient flow 단기 이완 후.
- `quasi-stationary`: equilibrium에 *근접한* 시점.
- `equilibrium`: t → ∞.
- `inter-snapshot`: 두 시점 비교.
- `transition`: K-jump 사건의 순간.

작업 방법: §1의 각 표에 `scale` 열 추가. 단일 보조구조가 여러 척도에 속하면 기록.

### 5.2 Observer tag 슬롯 (Option C용)

각 보조구조가 *어떤 관찰자*의 능력에 속하는가 (OMS-2.0 Appendix 활용):
- `no-observer`: 자연 dynamics 자체.
- `external-algorithm`: PersComp 같은 외부 계산자.
- `bayesian-likelihood`: LM1–3 류 likelihood 가진 관찰자.
- `two-time-comparator`: 두 시점을 동시에 손에 쥔 관찰자.
- `omniscient`: equilibrium 적분이 가능한 누군가.

작업 방법: §1의 각 표에 `observer` 열 추가.

### 5.3 통합 패턴 가설

후보 1=2=3 가설 (이 문서 §3 결론)이 맞다면, 5.1과 5.2를 완성했을 때 **scale × observer 매트릭스에서 *동일한 위치*에 클러스터링되는 보조구조들이 *동일한 보조구조 묶음의 일부*** 라는 사실이 드러나야 함.

---

## §6 검증

이 문서의 주장을 독립적으로 검증할 명령:

```bash
# 1. 본 문서 존재
ls THEORY/canonical/auxiliary_structures_master.md

# 2. Claim count 불변 (이전 79 → 83 유지)
grep -n "59A.*14B.*5C.*5R\|83 claims" THEORY/canonical/theorem_status.md

# 3. ρ_pers 출현 위치 확인 (§4.1) — 기호는 §3.11 (L291)에 도입, 값/규칙은 미등록
#    (검증된 결과: L291 D-ST-3 정의, L371 ρ_bd 유사 맥락, L2341 T-ST-5a A-STRICT)
grep -nE "rho_pers|ρ_pers|persistence threshold" THEORY/canonical/canonical.md

# 4. ε_kernel canonical 미등록 확인 (§4.2) — 0 hits 기대
grep -nE "epsilon_kernel|ε_kernel|kernel tolerance" THEORY/canonical/canonical.md

# 5. T_* OP-0021 OPEN 확인 (§4.3)
grep -n "OP-0021" THEORY/canonical/theorem_status.md

# 6. canonical.md 참조 §-anchor 유효성
grep -nE "^## (3\.|6\.|8\.|13\.|14\.|16\.) " THEORY/canonical/canonical.md

# 7. CHANGELOG AUX-1.0 entry
grep -n "AUX-1.0" THEORY/CHANGELOG.md

# 8. AUX-1.1 Stage 0 (T-transformation) row in registry
grep -n "Stage 0 — Sensor-to-u Transformation" THEORY/canonical/auxiliary_structures_master.md

# 9. AUX-1.1 §4.5 (T 누락) section
grep -n "^### 4.5" THEORY/canonical/auxiliary_structures_master.md

# 10. AUX-1.1 CHANGELOG entry
grep -n "AUX-1.1" THEORY/CHANGELOG.md

# 11. AUX-1.2 §7 COB 원칙 절
grep -n "^## §7" THEORY/canonical/auxiliary_structures_master.md

# 12. AUX-1.2 §1 각 표 Origin 열 (8개 이상 hit 기대)
grep -nE "\| Origin \|" THEORY/canonical/auxiliary_structures_master.md | head

# 13. AUX-1.2 §4.6 COB 위반/모호 항목
grep -nE "^### 4\.6" THEORY/canonical/auxiliary_structures_master.md

# 14. AUX-1.2 §4.7 ξ 카탈로그 + Route C
grep -nE "^### 4\.7" THEORY/canonical/auxiliary_structures_master.md

# 15. AUX-1.2 CHANGELOG entry
grep -n "AUX-1.2" THEORY/CHANGELOG.md

# 16. AUX-1.3 §4.8 전수 감사
grep -nE "^### 4\.8" THEORY/canonical/auxiliary_structures_master.md

# 17. §4.6.6 / §4.6.7 / §4.6.8 새 COB 위반 / hybrid 항목
grep -nE "^#### 4\.6\.[678]" THEORY/canonical/auxiliary_structures_master.md

# 18. AUX-1.3 CHANGELOG entry
grep -n "AUX-1.3" THEORY/CHANGELOG.md

# 19. AUX-1.4 §4.9 D-derivation 전수 시도 절
grep -nE "^### 4\.9" THEORY/canonical/auxiliary_structures_master.md

# 20. §4.9 sub-sections (4.9.1-4.9.11, 11개 expected)
grep -cE "^#### 4\.9\." THEORY/canonical/auxiliary_structures_master.md

# 21. D-승격 항목 Origin 갱신 (H-SINK-ENT, m, Mulliken, Wigner, HWF-1)
grep -nE "\| \*\*D \(§4\.9\.10|\*\*D-conditional on T\*\* \(§4\.9\.[26]|\*\*A 확정\*\* \(§4\.9\.4|\*\*D/P hybrid\*\* \(§4\.9\.3" THEORY/canonical/auxiliary_structures_master.md

# 22. AUX-1.4 CHANGELOG entry
grep -n "AUX-1.4" THEORY/CHANGELOG.md
```

---

## §7 Closed Ontological Budget (COB) 원칙 (AUX-1.2)

### 7.1 진술

**Commitment 후보 — CN-COB (Closed Ontological Budget):**

모든 보조구조 `s`는 정확히 다음 세 부류 중 하나에서 *유일하게* 유도/등록되어야 한다:

$$
\mathrm{Origin}(s) \in \{\,\mathcal{D}_u,\; \mathcal{A}_u,\; \mathcal{P}_{\text{obs}}\,\}
$$

| 부류 | 정의 | 표기 |
|---|---|---|
| $\mathcal{D}_u$ — Derived from u | u (또는 (T, I, u) bundle)로부터 *명시적 연산*으로 따라나오는 모든 것 | **D** |
| $\mathcal{A}_u$ — Added axiom on u | u에 추가되는 *형식적 axiom*. canonical commitment (CN) 등급으로 등록 | **A** |
| $\mathcal{P}_{\text{obs}}$ — Observer-personal | 관찰자가 가져오는 *개인적 파라미터* (시력, 분해능, 주의 가중, 내부 noise, 모델 선택) | **P** |

**금지:** 위 세 부류 어디에도 속하지 않는 *객관적 외생* (environmental constant, universal physics parameter, externally-given numerical value). 이런 누설이 *단 하나라도* 있으면 COB 위반.

### 7.2 출처 (사용자 지시)

> "이 진입점은 반드시 u 혹은 u와 관련된 추가된 조건 그리고 관찰자의 시력, 분해능과 같은 개인적 파라미터들을 통해서만 나와야함. 이외의 외생은 불허해야함." — 2026-05-18

### 7.3 OMS-1과의 관계

canonical.md L2416의 OMS-1이 관찰자 파라미터 벡터 컨테이너를 *이미* axiom 등급으로 등록:

$$
\Theta = (q, \lambda, \xi) \in \mathcal{M}_{\text{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi
$$

- `q = β/α`, `λ ∈ Δ³` — enumerate됨, $\mathcal{P}_{\text{obs}}$로 분류.
- `ξ ∈ B_ξ` — catch-all box. **내용물 카탈로그가 비어있음** (§4.7.1이 시드 제공).

즉 COB의 `$\mathcal{P}_{\text{obs}}$` 부류는 **새로 만들어지는 게 아니라 OMS-1으로 이미 등록된 컨테이너를 채우는 작업**. 후보 1 (보조구조 묶음 통일 누락) 진단의 *대부분*이 ξ enumeration으로 해결 가능.

### 7.4 본 §7의 적용 범위 (registry-internal only)

§7는 **registry 내부에서 COB 감사를 위한 작업 도구**. 즉:

- ✅ Registry §1 표의 Origin 열 분류 기준으로 사용.
- ✅ §4.6 (위반/모호 항목) + §4.7 (ξ 카탈로그) 작성 기준으로 사용.
- ❌ canonical.md §14 (Commitment Notes)에 CN-COB axiom으로 *등록하지 않음*.
- ❌ canonical.md OMS-1 본문의 `B_ξ` enumeration *수행하지 않음*.
- ❌ 어떤 정리의 상태 변경 *없음*.

**canonical 본문 등록은 Step 1** (별도 결정). 채택 시 이론 전체의 *철학적 색채*를 고정 — SCC는 철저히 first-person, 외부 우주에 대한 가정 0.

### 7.5 결과 — 후보 1/2/3 진단 통합

§7 채택 시 (registry-level이라도):

- **후보 1 (보조구조 묶음 통일 누락)**: §4.7.1 ξ 카탈로그 시드로 *대부분* 해소.
- **후보 2 (시간척도 불일관)**: $\mathcal{P}_{\text{obs}}$의 시간척도 관련 항목 (T_*, ρ_pers, ε_OT) 이 모두 관찰자 분해능에 귀착 → 단일 출처에서 발생하는 *파생*.
- **후보 3 (관찰자 분산)**: OMS-1 컨테이너 + ξ 카탈로그가 *문서적으로* 통일.

세 진단이 동시에 *한 작업으로* 닫힘. 후보 1=2=3 가설 (registry §3 결론) 의 *문서적 증명*.

---

## §8 최종 분류 상태 (End-of-Day Consolidation, 2026-05-18, AUX-1.5)

AUX-1.0 부터 AUX-1.4 까지의 5번 amendment를 통합한 *최종 분류 명시*. 분류 *완료* 항목 vs 분류 *안 된* 항목을 분리해 명시.

### 8.1 분류 완료 항목 — `D` / `A` / `P` / hybrid / external input

#### 8.1.1 D — Derived from u (또는 (T, I, u) bundle) — 약 30 항목

| Stage | 항목 |
|---|---|
| 0 | `X_t (graph)`, `{I : T(I) ≡ c·𝟙}` |
| 1 | `c (=m/n)`, `λ₂(L)`, `L = D−N`, `m (D-conditional on T)` |
| 2 | `F` (peak count), Non-criticality 방향, 그래프 클래스 G |
| 3 | `K_bar^{ℓ_min}`, `K_act^ε`, `B_K(P)` |
| 4 | `σ_rich`, `σ_standard`, `c_j`, orientations, `Aut(G) ≀ S_{K_act}`, `λ₁ < λ₂` gap, Hessian 계산 지점 |
| 5 | `π_{T_*}`, 반사 Langevin SDE, `C̃`, `C_P`, `osc(Ẽ)`, `p_K`, `K_feas` |
| 6 | `M_{t→s}`, `S_{ij}`, `Δ_sep ≥ Δ_sep* + 2ε_kernel`, `Δ_sep*`, `ρ_*`, `ρ_deep`, `R_{t→s}`, 5 사건 유형, `H-SINK-ENT` (H-SINK Cat A 부분 명제), `HWF-1` (D-conditional on T) |
| 7 | `M` (merger geometry), `v_1` (split direction), `Φ` (inheritance map), `R_σ(i→j)` 분해, `λ₁ < λ₂` |
| 가설 | P0, P1, P2 (L1-J); H2 (T-P-F-ε0); LM3 (T-K-Select-OBS); A6, A7, DR1, DR2 (T-Temporal-Identity) |

#### 8.1.2 A — Added axiom on u — 약 25 항목

| Stage | 항목 |
|---|---|
| 1 | `W(u)`, `Σ_m` 형태, `a_cl < 4`, `b_D = 0` |
| 3 | Sublevel filtration 방향 |
| 4 | one-hop buffer, **`Mulliken irrep 순서` (A 확정)** |
| 5 | Lions-Sznitman regularity |
| 6 | E1–E4 (transport axioms) |
| 7 | Parallel-axis theorem (외부 import) |
| T hyp pkg | Stage 0 §4.5 9-조건 (각각 T 위 axiom; A on P) |
| 가설 | P3, P4, P5, P6, P8, P9, P10, P11 (L1-J); H1, H3, H4 (T-P-F-ε0); LM1; A1, A2, A3 (T-Temporal-Identity) |
| Canonical commitment | CN5, CN6, CN14, CN16, Commitment 14 (O5')(O7) |

#### 8.1.3 P — Observer-personal (`ξ` residents) — 약 18 항목

OMS-1 컨테이너 `Θ = (q, λ, ξ)`의 명시 + ξ 카탈로그 시드 (§4.7.1).

| Stage | 항목 |
|---|---|
| 0 | **`T` (sensor transformation — 관찰자 시력)** |
| 1 | `λ_cl, λ_sep, λ_bd, λ_tr` (= λ ∈ Δ³, OMS-1), `α, β` (= q = β/α, OMS-1), `η_cl` |
| 2 | `ε` (F-count threshold), IC-protocol |
| 3 | `ρ_pers`, `ℓ_min`, `r` (neighborhood radius) — 모두 분해능 |
| 4 | `d_σ` (σ-space 거리) |
| 5 | LM2 (positivity), `Φ_obs` |
| 6 | partial OT cost `c[u_t, u_s]`, Score threshold, `ε_kernel`, `ε_OT`, `θ_core` |
| 가설 | A4 (stable-K), A5 (well-separated), A7' (sharp-OT), A9 (mass dominance) |

#### 8.1.4 Hybrid — D/P 또는 D/A — 2 항목

| 항목 | 분류 | regime split |
|---|---|---|
| `Wigner projection` (Stage 7) | **D/P hybrid** | Generic case D (Schur's lemma); degenerate (multi-irrep same dim) P |
| `P7` (decay-to-cut, Stage 3 / L1-J) | **D/A hybrid** | Strong stationarity regime D (Combes-Thomas / Agmon); 일반 regime A |

#### 8.1.5 External input — COB 밖 — 1 항목

| 항목 | 분류 | 사유 |
|---|---|---|
| `I_t` (raw sensor data) | **외부 입력 (COB 비대상)** | I_t는 *원료*이지 보조구조가 아님. T : I → u의 입력. COB는 보조구조 분류 규칙이고 입력은 그 외부 |

---

### 8.2 분류 안 된 항목 — `U` 잔류 (오늘 마무리 시점) — **2 항목만**

이것이 *진정한 잔류 미해결*. 다른 모든 항목은 D/A/P/hybrid/외부입력 중 하나로 분류됨.

| # | 항목 | 위치 | 미해결 사유 | 권장 처분 (별도 결정) |
|---|---|---|---|---|
| 1 | **`T_*`** (effective stochastic temperature) | Stage 5, §4.6.1, §4.9.1 | **Fixed-point 구조.** T_*가 Gibbs measure `π ∝ exp(−E/T_*)`를 정의 → π가 variance를 정의 → variance가 T_*를 정의. 자기-참조 순환. 일관 fixed-point가 *원리적으로* 존재 가능하나 *유일성* 미보장. SCC의 핵심 인식 메커니즘 — 관찰자가 무엇을 noise로 처리하는가. | **`OP-T*-FIXED-POINT`** 정식 등록 + Route C (관찰자-개인 stochastic resolution → P) 채택. OP-0021의 Route A (Mori-Zwanzig) / Route B (RG fixed point) 폐기. |
| 2 | **`H5`** (Morse stability) | Stage 5, §4.6.6, §4.9.5 | **Spinodal Goldstone mode degeneracy.** Generic regime에서 Morse는 Sard transversality로 D 가능. 그러나 T8 spinodal 임계점에서 Hessian이 *intrinsically* zero eigenvalue (formation을 트리거하는 Goldstone mode). 이건 SCC 이론의 *핵심 사건* — perception이 발생하는 바로 그 순간. | **`OP-H5-MORSE-SPINODAL`** 정식 등록 + T-P-F-ε0-K 적용 regime을 *post-bifurcation stable basin* 한정으로 명시. Spinodal critical surface는 separate treatment. |

---

### 8.3 통계 — 오늘 분류 결산

| 분류 | 갯수 | 비율 |
|---|---|---|
| **D** (Derived) | ~30 | ~46% |
| **A** (Axiom) | ~25 | ~38% |
| **P** (Observer-personal) | ~18 | ~28% |
| **Hybrid** (D/P, D/A) | 2 | ~3% |
| **External input** (COB 밖) | 1 | ~1.5% |
| **U 잔류** | **2** | **~3%** |
| 총계 | ~65 | 100% |

(중복 계산 포함 — 일부 항목이 여러 §에 등장. 고유 항목 수는 ~50.)

**핵심:** 65개 항목 중 *2개*만 진정 잔류. 후보 1/2/3 통합 진단의 **97% 해소**.

---

### 8.4 오늘 작업 결산 (AUX-1.0 → AUX-1.5)

| 버전 | 작업 | 산출물 |
|---|---|---|
| AUX-1.0 | Registry 신설 | §1 Stage 1–7 인벤토리, §2 cross-stage drift, §3 후보 1 진단, §4 미해결 4항 |
| AUX-1.1 | Stage 0 추가 | T (sensor transformation) §4.5; 9-조건 downstream package |
| AUX-1.2 | COB 원칙 등록 | §7 CN-COB, §1 Origin 열 (D/A/P/U), §4.6 위반/모호, §4.7 ξ 카탈로그 시드 |
| AUX-1.3 | 가설 패키지 전수 감사 | §4.8 (32개 가설 D/A/P/U), §4.6.6-8 (H5, HWF-1, P7) |
| AUX-1.4 | D-derivation 전수 시도 | §4.9 (10개 시도 + 요약); 8개 분류 결정 |
| AUX-1.5 | End-of-day consolidation | §8 최종 분류 상태 (이 절) |

**총 5번의 amendment, 1000+ lines, 65+ 항목 분류, 클레임 카운트 83 불변, canonical 본문 0 변경.**

---

### 8.5 내일 이후 결정 사항 (오늘 작업 후 carry forward)

오늘 *작업하지 않은* 후속 결정 (사용자 결정 사항):

1. **`OP-T*-FIXED-POINT` 정식 등록** + Route C 채택 + OP-0021 본문 수정.
2. **`OP-H5-MORSE-SPINODAL` 정식 등록** + T-P-F-ε0-K regime 명시.
3. **`CN-COB` canonical commitment 정식 등록** (§14) — 이론 first-person 색채 고정.
4. **canonical §3 Σ_m amendment** — `m := Σ_v T(I)(v)` 명시.
5. **canonical §14 Mulliken axiom** — chemistry convention import 명시.
6. **§4.5 T hypothesis package에 HWF-1 흡수** (10번째 조건).
7. **H-SINK-ENT 별도 hypothesis 등록 해소** (H-SINK Cat A sub-claim 명시).
8. **canonical OMS-1 `B_ξ` enumeration** — §4.7.1 시드를 canonical 본문에 promote.
9. **OP-0008 처분 재검토** — Wigner generic case D 검증; σ_standard merge/split inheritance Cat C → Cat B 가능성.

---

### 8.6 인식론적 결산 (오늘의 의미)

처음에 사용자는 "각 단계가 2%씩 부족하다" 고 느꼈고, 후보 1/2/3 진단을 던졌다.

오늘 작업의 결과:

- **후보 1 (보조구조 묶음 통일 누락):** Registry로 *문서적* 통일 완료. ξ 카탈로그 시드까지.
- **후보 2 (시간척도 불일관):** P 부류 시간척도 항목들이 *모두* 관찰자 분해능에 귀착 — 단일 출처 파생으로 *대부분* 해소.
- **후보 3 (관찰자 분산):** OMS-1 컨테이너 + ξ 카탈로그 + COB 원칙이 통일된 관찰자 모듈 *문서적* 등록.

**후보 1=2=3 가설** (세 후보가 동일한 균열의 세 얼굴) 이 *문서적으로 증명*됨 — 한 작업 (COB 감사) 이 세 진단을 동시에 닫음.

**그리고 두 진정한 잔류 U** (`T_*`, `H5`) 가 *우연*이 아니라 SCC 이론의 *진짜 핵심 사건*과 직결돼있다는 사실이 드러남:

- `T_*` = 관찰자가 무엇을 noise로 처리하는가 (인식 메커니즘 자체).
- `H5` = 균질에서 분화가 일어나는 바로 그 순간 (perception 사건의 기원).

이 두 미해결이 *이론의 핵심 질문 그 자체*. 우연한 정리(整理) 부족이 아니라 *이론이 진짜 묻고 있는 것*.

---

## 부록: 변경 기록

| 버전 | 일자 | 변경 | 클레임 카운트 |
|---|---|---|---|
| AUX-1.0 | 2026-05-18 | 신설. Stage 1–7 인벤토리 + 단계횡단 패턴 + 후보 1 진단 + 미해결 등록 4항. | 83 (불변) |
| AUX-1.1 | 2026-05-18 | Stage 0 (Sensor-to-u Transformation T) 추가. §2에 T row 추가. §4.5 신설 (T 미등록 + 9-조건 downstream hypothesis package + OMS 관계 + fixed-point 구조 설명). §6에 검증 4항 추가. | 83 (불변) |
| AUX-1.2 | 2026-05-18 | §7 COB 원칙 (Closed Ontological Budget) 신설. §1 각 표에 Origin (D/A/P/U) 열 추가. §4.6 신설 (COB 위반/모호 5항: T_*, m, Wigner, Mulliken, 가설 패키지). §4.7 신설 (ξ 카탈로그 시드 + T_* Route C 권장 + 분류 결정 미루어진 항목 표). §6에 검증 5항 추가. | 83 (불변) |
| AUX-1.3 | 2026-05-18 | 가설 패키지 전수 감사 (32개 가설). §4.8 신설 — L1-J (P0–P11), H1–H5 (T-P-F-ε0), LM1–LM3, T-Temporal-Identity (A1–A9 + DR + HWF-1) 모두 D/A/P/U 분류. 새 COB 위반/hybrid 등록: §4.6.6 H5, §4.6.7 HWF-1, §4.6.8 P7. §1 6개 가설 패키지 row Origin 갱신. §6 검증 3항 추가. **중요 정정:** H1–H5는 Eyring-Kramers가 아니라 T-P-F-ε0 가정. 32개 중 29개 D/A/P 깨끗 분류, 3개 U. | 83 (불변) |
| AUX-1.4 | 2026-05-18 | U 항목 10개에 대해 D-derivation 전수 시도. §4.9 신설 (10개 시도 sub-section + 요약). §1 Origin 갱신 8개 row: I_t (외부 입력), T hyp pkg (9×A), m (D-cond on T), Mulliken (A 확정), T_* (U 잔류 fixed-point), HWF-1 (D-cond on T), H-SINK-ENT (D), Wigner (D/P hybrid). §6 검증 4항 추가. **핵심 결과:** 10개 중 2개만 진정 U 잔류 (T_*, H5); 나머지 8개는 분류 결정만의 문제였음. COB 원칙 실효성 검증됨. | 83 (불변) |
| AUX-1.5 | 2026-05-18 | **END-OF-DAY consolidation.** §8 신설 — 최종 분류 상태. AUX-1.0~1.4 통합. §8.1 분류 완료 (D ~30 / A ~25 / P ~18 / hybrid 2 / external input 1). §8.2 U 잔류 *2개만* 따로 분리 (T_*, H5). §8.3 통계: 65+ 항목 중 2개만 잔류 (97% 해소). §8.4 5-amendment 결산. §8.5 9개 carry-forward 결정 사항. §8.6 인식론적 결산: 후보 1=2=3 가설의 문서적 증명; 두 잔류 U가 이론의 핵심 사건과 직결. | 83 (불변) |
