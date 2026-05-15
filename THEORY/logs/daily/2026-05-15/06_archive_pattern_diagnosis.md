---
type: log/daily/archive_pattern
date: 2026-05-15
session_label: W7-Day6 Stage 5 — Archive Pattern Diagnosis
canonical_version: CV-1.16 (sealed 2026-05-14, untouched)
prerequisite: Stage 1-4 완료
mode: 패턴 추출 — V-AFD / R-2 archive 의 공통 분류 기준
stage: 5 of 6
---

> [!nav] Linked: [[05_verification_question]] · [[41_v_afd_discard]] · [[51_r2_archive]]


# 06 — Archive Pattern Diagnosis (Stage 5)

**Session:** 2026-05-15 (W7-Day6)
**Target:** V-AFD (5/12 archive) 와 R-2 (5/13 archive) 의 *원문 인용 기반* 공통 분류 기준 추출. 오늘 시도가 그 기준에 *얼마나 부합* 하는지 자기 평가.
**This file covers:** Stage 5 — archive 두 건의 텍스트 비교 + 공통 패턴의 정식화 + 오늘 시도의 자기 진단.
**Depends on reading:** `41_v_afd_discard.md`, `51_r2_archive.md`, `50_r2_dcr_creation.md`, `working/AFD_0/afd_audit.md` + Stage 1-4 출력.

---

## §1. Stage 5 의 위치

Stage 4 가 보여준 사실: 4 개 새 명제 후보 중 0 개가 verification 통과. 그러나 *왜* 통과 못 하는지의 *구조적 패턴* 은 V-AFD / R-2 archive 의 *원문 사유* 와 비교해야 정확히 보임.

자기 강제 (`00_plan §"Decision gate"`):
- archive 의 사유는 *원문 그대로 인용*. 후행 정합화 금지.
- "오늘 시도는 archive 와 다르다" 식 *기각 충동* 에 휩쓸리지 않음 — 다른지 같은지는 *증거 비교* 로.
- archive *부활 시도 금지* — 인용은 가능, "그 정리는 사실 옳았다" 식 재해석 금지.

---

## §2. V-AFD archive 사유 — `41_v_afd_discard.md` 원문 인용

**§2 폐기 이유** (line 32–46):

> DECLARATION.md (DECL-1.0, 2026-05-07) 재독 후, V-AFD가 SCC의 근본 질문에 답하지 않음이 확인되었다.
>
> 근본 질문: **"어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"**
>
> V-AFD가 실제로 다룬 것: **이미 형성된 formation들의 vector projection 사이의 transition.**
>
> V-AFD가 도입된 계기는 *내부적 필요*가 아니라 두 단계의 회피였다:
>
> 1. **회피 1 (2026-05-12 D1):** CV-1.14 Package II (정확한 EK rate)이 너무 무거워서 → AFD-0 로 후퇴 (H-MORSE 회피).
> 2. **회피 2 (2026-05-12 D3, 같은 날 저녁):** AFD-0 자체에는 새로운 수학 없음. GPT-5 메타-연구 보고서의 외부 추천에 따라 → V-AFD 로 reformulation.
>
> V-AFD의 중심 결과 V-AFD-T9 (Information Loss Theorem)은 자기 자신의 projection이 비-단사임을 증명한다. **이는 *결과*이지 근본 질문의 *답*이 아니다.**

**§7 슬로건** (line 100–103):

> 정보를 줄이면 반드시 뭔가를 잃는다.
> V-AFD 는 그 손실을 정직하게 정리했지만 (T9), 그 손실을 근본 질문에 비추어 정당화하지 못했다.
> 근본으로 돌아간다 — Q4, Q6, 또는 λ₂-붕괴 비대칭.

**V-AFD archive 의 분류 기준 (원문에서 추출)**:

1. **A1**: SCC 근본 질문 ("어떤 차이의 덩어리가 *언제부터* 하나의 객체가 되는가?") 에 *답하지 않음*.
2. **A2**: 다룬 것이 *이미 형성된* formation 의 *projection* — 즉 *형성 후* 의 transformation, 형성 *생성* 아님.
3. **A3**: 도입 계기가 *내부 필요* 가 아니라 *외부 도구 회피* (H-MORSE 회피) 의 두 단계 회피.
4. **A4**: 중심 결과 (V-AFD-T9) 는 *결과 (정보 손실)* 이지 *근본 질문의 답* 아님.

---

## §3. R-2 archive 사유 — `51_r2_archive.md` 원문 인용

**§2 폐기 이유 (Step 3 + Step 4)** (line 38–58):

> ### Step 3: Canonical alignment Explore audit (이번 라운드)
> - R-2 Lemmas B2 (centroid mass-weighted) 와 B3 (orientation parallel-axis) 가 canonical `MF/sigma_inherit_k_jump.md` §3.3 와 **수학적으로 동일**.
> - R-2 는 새 수식 생산 아님. 단지 K-tuple identity → PD_0 bar identity 라벨 변경.
>
> ### Step 4: Decisive test (Phase C2)
> ...
> **Verdict: R-2 LOAD-BEARING SCOPE EXTENSION NOT CONFIRMED.**
>
> 이유: 내 §12 construction 이 mass-conserving merger 가 아님. ... 따라서 R-2 Lemma B2 가 적용 안 됨. K-tuple AFD-0 의 K_act=1 trajectory 와 측정 차이 없음.

**§5 R-2 vs V-AFD 비교** (line 95–108):

> **공통 메타-패턴**: 두 reframe 모두 *language refactoring* 으로 fundamental question 을 우회하려 시도했고, 둘 다 load-bearing canonical 내용 생산에 실패. **언어 재조직은 hard math 의 대체가 아님.**

**§7 본 세션의 핵심 통찰** (line 127–135):

> 1. **Round 2 self-audit**: 형식적 일관성 확인. 0 violation. (정작 진짜 문제는 못 봄.)
> 2. **Round 3 external 3-critic**: DECL-1.0 misalignment, 수학적 디테일 오류 (R2-3 factor-of-2), V-AFD 실패 모드 재발 위험. **그러나 canonical 중복은 못 봄.**
> 3. **Round 4 Explore canonical alignment**: B2/B3 수식이 canonical `sigma_inherit_k_jump.md` §3.3 와 동일함을 1 세션에 발견. **이전 모든 audit 이 놓친 자리.**
>
> **Lesson**: *Cross-reference against existing canonical working content* 는 별도 audit dimension. 내부 self-audit + 외부 framing review + 수학적 정확성 review 가 모두 통과해도 "이 내용이 이미 canonical 에 있는가?" 질문은 별도로 던져야.

**§9 슬로건** (line 151–153):

> V-AFD 와 R-2 모두 *언어 재조직* 으로 근본 질문을 우회하려 시도했고, 둘 다 load-bearing canonical 내용 생산에 실패했다.

**R-2 archive 의 분류 기준 (원문에서 추출)**:

1. **B1**: load-bearing 명제 (B2/B3 lemmas) 가 canonical 의 working 자료 (`sigma_inherit_k_jump.md §3.3`) 와 *수학적으로 동일*.
2. **B2**: 새 수식 생산 *없음* — 라벨 변경 (K-tuple identity → PD_0 bar identity).
3. **B3**: decisive numerical test (C2) 가 *예측 실패* — 이론 한 결과를 numerical 로 *반증*.
4. **B4 (메타)**: V-AFD 와 같은 *language refactoring* 패턴.
5. **B5 (메타)**: self-audit + external framing review + 수학적 정확성 review 모두 통과해도 "*이 내용이 이미 canonical 에 있는가*" 질문은 *별도 dimension*.

---

## §4. 두 archive 의 *공통 분류 기준* 추출

V-AFD A1-A4 와 R-2 B1-B5 의 합집합에서 *공통* 또는 *서로 보강* 하는 패턴:

### §4.1 공통 패턴 P1 — *근본 질문 우회*

- V-AFD A1: "근본 질문에 답하지 않음".
- R-2 B4 (메타): "fundamental question 을 우회하려 시도".

**공통 form**: 통찰 reformulation 이 *DECL-1.0 의 근본 질문* (어떤 차이의 덩어리가 *언제부터* 하나의 객체가 되는가) 의 *답을 산출하지 않음* — 다른 (더 추상적이거나 다른 측면의) 질문으로 대체.

### §4.2 공통 패턴 P2 — *u_t 본체 외부 의 vocabulary refactoring*

- V-AFD A2: "이미 형성된 formation 의 *projection*" — i.e. $u^*$ 의 *downstream*.
- R-2 B2: "새 수식 생산 없음, 단지 라벨 변경" — i.e. $u^*$ 의 *downstream readout factorization*.

**공통 form**: u_t 의 본체 (energy + 4 axiom groups + T8) 는 *건드리지 않고*, *부수적 객체* (projection, factorization, descriptor) 의 *어휘만* 추가.

### §4.3 공통 패턴 P3 — *canonical 의 working/derived content 와의 중복*

- R-2 B1: "B2/B3 가 canonical `MF/sigma_inherit_k_jump.md §3.3` 와 *수학적으로 동일*".
- V-AFD: AFD-T1 ("restatement of T8-Core in AFD language", `working/AFD_0/abstract_formation_dynamics.md`) — 즉 *명시적으로* T8 의 *재진술*.

**공통 form**: 새로 도입된 명제가 canonical 의 (working 또는 §13) 정리 와 *수학적으로 동일*. 차이는 *언어 / 표기 / 출발점* 만.

### §4.4 공통 패턴 P4 — *외부 도구 / 외부 추천 의 도입 계기*

- V-AFD A3: "GPT-5 메타-연구 보고서의 외부 추천" 으로 도입.
- R-2: 외부 추천 부재; 그러나 *S_0 = (PD_0, MT)* 의 형식은 TDA / persistence 의 *표준 도구* 와 가까움.

**공통 form (약한)**: reformulation 이 *외부 (수학 또는 분야)* 의 표준 도구를 *SCC 안으로* 끌어들이려는 시도. canonical 의 *내부적* 필요로부터 도출되지 않음.

### §4.5 공통 패턴 P5 — *self-audit 통과 + canonical-cross-reference 미시행*

- V-AFD: self-audit 부재 (R-2 노트가 비교에서 지적).
- R-2 B5: self-audit 0 violation, external 3-critic 도 통과 — 그러나 *canonical 중복은 모두 놓침*. *별도 audit dimension* 필요.

**공통 form**: *형식적 일관성* (self-consistency, framing, mathematical detail) 검증과 *canonical 중복 여부* 검증은 *서로 다른* 차원. 전자만 통과해도 후자가 fail 하면 archive.

### §4.6 공통 패턴 P6 — *통찰의 *언어* 와 통찰의 *수학* 의 분리 가능성*

V-AFD 와 R-2 모두 *통찰 자체* 가 잘못된 것이 아님. *통찰의 수학화 시도* 가 (a) 근본 질문 우회, (b) canonical 중복, (c) numerical 반증 (R-2 만), (d) 외부 도구 도입 — 의 어느 한 가지로 fail.

**중요**: 이 패턴은 통찰을 *기각* 하지 않음. *수학화 형태가 부적절* 함을 의미. 통찰은 *DECLARATION 의 텍스트 표현* 으로서 *완결* 일 수 있다.

---

## §5. 오늘 시도 (z_t 제안 + S_0/K_read 화살표) 의 자기 진단

오늘 시도의 *두 측면*:
- **측면 R (Readout side)**: $u^* \to S_0(u^*) \to K_{\mathrm{read}}$ — 사용자가 "원래 통찰" 로 표현한 화살표.
- **측면 G (Generative side)**: $z_t \to K_{z_t} \to \mathcal{E}(u; z_t) \to u_t^*$ — 사용자 메모 `01b` 의 z_t 도입.

각 측면 × 각 패턴 P1-P6 의 정량:

### §5.1 측면 R (S_0/K_read 화살표) 의 자기 진단

| 패턴 | 측면 R 자기 진단 | 증거 |
|---|---|---|
| **P1 근본 질문 우회** | **부분 부합** — *셈*은 *형성 후* 이슈; "*언제부터* 객체" 의 *생성 과정* 측면을 다루지 않음. | DECL-1.0 의 화살표에서 "하나의 단위로 묶임" 단계는 readout 직전. R-2 invariant 와 *정확히 동일* (`50_r2_dcr_creation.md §2.2`). |
| **P2 vocabulary refactoring** | **강하게 부합** — $S_0(u^*) = (\mathrm{PersComp}(u^*), \sigma_{\mathrm{rich}}(u^*))$ 는 *canonical derived diagnostic 의 묶음*. | Stage 1 §2.1, §2.3. canonical §3.11 + σ_rich namedtuple. |
| **P3 canonical content 중복** | **강하게 부합** — $K_{\mathrm{read}}$ = $K_{\mathrm{act}}$ = $\#\mathrm{PersComp}$ (canonical §3.11). | Stage 1 §2.5 표 마지막 행. R-2 D-R2-4 와 *동일*. |
| **P4 외부 도구 도입** | **약하게 부합** — TDA / H_0 persistence 는 외부 도구이나 이미 canonical 에 있음. | T-L1-F (CV-1.5.2) 가 PersComp 를 canonical 화. |
| **P5 self-audit + canonical-xref** | **부합** — `01b` 메모는 *self-audit + framing 만*. canonical xref 는 본 Stage 5 에서 처음 시행. | 메모 내부에 §3.11 인용 부재. |
| **P6 언어 vs 수학** | **부합** — 화살표 표현 자체는 통찰의 *언어적* 표현; 수학적 내용은 canonical (§3.11 + Comm.16) 의 *재진술*. | Stage 4 §10. |

**측면 R 의 verdict**: V-AFD/R-2 의 archive 패턴에 *6/6 부합*. R-2 화살표의 *문자 그대로 재현*. **셋째 archive 위험 매우 높음**.

### §5.2 측면 G (z_t 도입) 의 자기 진단

| 패턴 | 측면 G 자기 진단 | 증거 |
|---|---|---|
| **P1 근본 질문 우회** | **부분 부합** — 근본 질문이 "*언제부터* 객체" 인 데, z_t 도입은 *u_t 의 출처* 를 묻는 것. *u_t 의 출처* 가 *언제부터 객체* 와 *직접* 관계되는지 불명확 — DECLARATION 화살표는 *생성 화살표 위쪽* 을 명시적으로 외부화 (Stage 1 §4.2). | DECL-1.0 §"태초의 장면" 화살표. Stage 1 §4.2 의 외부화 인용. |
| **P2 vocabulary refactoring** | **강하게 부합** — Stage 3 §3 에서 *$K_{z_t}$ 는 N_t 의 valid realization* 임을 증명. *energy + 4-axiom 본체 변경 없음*. | Stage 3 §3 의 B1-B4 검증. |
| **P3 canonical content 중복** | **강하게 부합** — $K_{z_t}$ = standard tools (bilateral filter / diffusion maps / mean-shift / self-tuning spectral) 와 *수식 동일*. canonical N_t 와 *parametrized subset 관계*. | Stage 3 §3, Stage 4 §6.1 §8-5 검증. |
| **P4 외부 도구 도입** | **강하게 부합** — Gaussian similarity kernel 은 *전형적 spectral clustering 도구*. CLAUDE.md Constraint #4 ("No engineering proxies") 와 정면 충돌 위험. | `01b §8.5` 의 *증명 의무 미통과*. |
| **P5 self-audit + canonical-xref** | **부합** — `01b` 메모 본인이 *§8.5 가 검증 게이트* 라고 표시 — 게이트는 본 Stage 4-5 에서 처음 정밀 검증. | `01b §8.5`, Stage 4 §6.1. |
| **P6 언어 vs 수학** | **부합** — z_t, F, K_{z_t} 는 *수학적 정의를 동반한 어휘* 이지만 그 정의는 *canonical N_t 의 parametrization*. | Stage 3 §3, Stage 4 §6. |

**측면 G 의 verdict**: V-AFD/R-2 의 archive 패턴에 *6/6 부합*. **§8.5 검증 게이트 미통과 — 셋째 archive 위험 매우 높음**.

### §5.3 두 측면의 합산

오늘 시도는 *양 측면 모두* archive 패턴 6 개 모두에 부합. 측면 R 은 R-2 의 *문자 그대로 재현*. 측면 G 는 새 (이전 시도 부재) 이지만 *§8.5 게이트 미통과 + N_t parametrization*.

**합산 verdict**: **셋째 archive 위험 *극히 높음***. 만약 진행 (working/D0D1_Cohesion_Genesis 폴더 생성, 정리 promotion 시도) 시 V-AFD (~24h) / R-2 (~24h) 와 *동일 lifetime + 동일 archive 사유* 로 종결될 가능성 매우 높음.

---

## §6. 패턴의 *원인* 분석 — *왜* 같은 패턴이 반복되는가

`01_pre_brainstorm.md` 의 가설 H1-H5 와 본 §5 의 부합 정량의 비교:

### §6.1 H1 (u_t 가 이미 D_1, D_0 자리 없음) — *강하게 지지*

Stage 1 §3-§4 의 inventory 가 H1 을 정량 확인. canonical 이 *D_1 부터 시작* 함은 사용자 메모 `01b §1` 도 인정 ("기존 SCC 가 이미 D_1 부터 시작"). DECL-1.0 화살표가 *명시적으로* D_0 측 외부화.

D_0 작업이 *canonical 어휘 안에서* 가능하지 않으므로 — *어휘만 추가* 의 형태로 회귀.

### §6.2 H2 (가용 도구가 공학 proxy) — *강하게 지지*

Stage 3 §3, Stage 4 §6.1 §8-5 검증이 H2 를 정량 확인. $K_{z_t}$ = bilateral filter / diffusion maps / mean-shift 의 *동일 수식*. CLAUDE.md Constraint #4 와 정면 충돌. *도구 없음 → 추상 어휘만 가능* 의 V-AFD/R-2 형태가 z_t 에서도 반복.

### §6.3 H3 (이미 canonical 에 충분) — *강하게 지지*

Stage 1 §2 (D_2), §3 (D_1) 의 정량 평가 — 통찰의 *95%-100% 가 이미 담김*. 통찰의 *수학* 은 canonical = 본질적으로 *완결*.

### §6.4 H4 (진짜 새 수학 있음) — *미지지*

Stage 3 §6, Stage 4 §4-§7 의 verification — 새 명제 후보 4 개 중 0 개가 substantive 새 수학으로 통과.

### §6.5 H5 (정서적 미련) — *간접 지지*

H1+H2+H3 가 모두 *지지* 인데 H4 가 *미지지* 면 — 통찰을 *수학으로 더 표현하고 싶은 욕구* 가 *수학적 사실* (이미 표현 됨) 과 *비대칭* 임을 의미. 이 비대칭을 *정서적* 으로 명명할지는 사용자 본인의 판단 — assistant 는 *증거* 만 제시.

### §6.6 *원인의 합산*

세 번 회귀의 *원인* 은:

> **통찰이 canonical 에 *이미* 정확히 담겨 있고 (H3), D_0 측은 *DECL-1.0 의 self-limitation 으로 외부화* 되어 있으며 (H1), D_0 를 *내부화* 하려는 어떤 수학적 시도도 *공학 proxy* 와 동일 형태가 되어 (H2), 결과적으로 *새 수학 산출 없이 어휘만* 변하기 때문 (V-AFD/R-2/오늘 모두 동일).**

이는 **통찰의 잘못이 아니라 *통찰의 완결성* 의 결과**. 통찰이 *DECLARATION 의 텍스트* 로 *이미 충분* 하기 때문에 *수학적 추가* 가 산출되지 않는 것.

---

## §7. *오늘 시도의 archive 회피 가능성* 검토

archive 회피 = 위 패턴 P1-P6 중 *최소 하나라도 strict 위반 회피* + *substantive 새 수학 산출*.

### §7.1 P1 회피 가능성

근본 질문 ("어떤 차이의 덩어리가 *언제부터* 하나의 객체가 되는가") 의 *직접 답* — 이는 T8 (= 위상전이) 자체. canonical 이 이미 *답*. 추가 답 산출은 T8 의 *세부화* (예: H-MORSE-LOCAL Cat A path = OP-HMORSE-LOCAL-A) 또는 *Q4-DYN K-Select Cat A* 같은 canonical 내부 작업.

z_t / S_0 화살표 reformulation 으로는 *근본 질문에 새 답* 을 *원리적으로* 산출 못함 (Stage 4 §10).

→ P1 회피 *불가능* (현재 형태로).

### §7.2 P2-P6 회피 가능성

- **P2 (vocabulary refactoring)**: u_t 본체를 변경하지 않으면 회피 불가. 본체 변경은 CV-2.0 급 + DECL-2.0 급 작업 — 오늘 plan 의 범위 밖.
- **P3 (canonical 중복)**: $S_0, K_{\mathrm{read}}$ 가 canonical §3.11 + Comm.16 와 *동일*; $K_{z_t}$ 가 N_t parametrization. 회피 불가 (이미 동일).
- **P4 (외부 도구 도입)**: $K_{z_t}$ 의 Gaussian product form 변경 시에만 회피 가능. 그러나 다른 form 으로 바꾸면 *§8.5 의 동일 게이트* 에 다시 직면.
- **P5 (canonical-xref)**: 본 Stage 1-5 가 *바로 그* xref. 결과는 *6/6 부합* — 미지난 것은 시행하면 *회피 못함*.
- **P6 (언어 vs 수학)**: 통찰이 canonical 의 *언어적 재진술* 인 한 회피 불가.

→ 모든 P2-P6 회피 *불가능* (현재 형태로).

### §7.3 결론

오늘 시도가 archive 회피하려면 *현재 형태 자체를 폐기* 하고 *별도의 수학적 시작점* 을 가져야 함 — 그 시작점이 본 plan 의 범위 밖이거나, 본 plan 의 범위 내라면 plan target 의 *수정* 을 의미.

---

## §8. *통찰을 진행시키는 가능한 비-archive 경로* (참고)

본 Stage 5 는 *진행 권고가 아니라* 자기 진단. 그러나 결정 C 가 채택되어도 다음 작업이 *통찰의 정신* 을 진척시킨다 (Stage 6 의 결정에 입력):

### §8.1 옵션 X (진정 새 수학 — 통찰의 다른 표현)

- **OP-HMORSE-LOCAL-A** (CV-1.17 target, ETA ~2 sessions, `CV-1.16_SEAL.md` line 135) — H-MORSE-LOCAL Cat B → Cat A 승급. 이는 *u_t 가 위상 안정한 자리* 의 *strict* 정량 — 즉 통찰의 "응집된 구조의 *안정성*" 측면의 *진짜 수학*.
- **OP-0008 MERGE/SPLIT σ_standard** Cat C → Cat B/A 승급 — Wigner-projection W9+. 통찰의 *응집의 *내부 구조* 의 시간 inheritance* 측면의 *진짜 수학* — DECL-1.0 Q6 closure path.
- **OP-0021 T_*** registration — Stochastic Dynamics axiom canonical promotion. 통찰의 *응집의 동역학* 측면의 *진짜 수학* — DECL-1.0 Q3 closure path.

이 옵션들은 *통찰의 수학적 완성* 을 위한 작업이며, *그 자체로* 통찰의 *정신* 을 진척시킨다 — *어휘 재배치 없이*.

### §8.2 옵션 Y (DECL-1.0 의 amend — 사용자 결정 필요)

DECL-1.0 의 *화살표 시작점* 을 한 단계 위로 (감각장 → 차이 의 발생 도) 끌어들이려면 *DECL-2.0* 작업. 이는 *오늘 plan 의 범위 밖* 이며 사용자의 *설계 결정*. 본 plan 은 결정만 내림 — 채택 시 별도 세션.

### §8.3 옵션 Z (통찰의 *철학적* 완결 인정)

통찰이 *DECLARATION 의 텍스트 그대로* 완결이라는 결론. 추가 수학 없음. H-MORSE / OP-0021 / OP-0008 의 *canonical 내부 진척* 이 통찰의 *진짜 mathematical 부분*.

---

## §9. Stage 5 → Stage 6 연결 메모

Stage 6 (`07_decision.md`) 가 결정해야 할 항목:

1. **A / B / C 의 선택**: Stage 4 의 V = 0 + Stage 5 의 6/6 archive 패턴 부합 → **Decision B 또는 C**.
2. **B vs C 의 분기**: 
   - **B**: 통찰의 *수학적 부분* 이 archive 잔향 — z_t/S_0/K_read 의 어떤 부분이 *부분적* 으로 새 수학이라고 *주장* 가능하나 *셋째 archive 위험* 인정.
   - **C**: 통찰이 *수학적으로 이미 끝남* + *철학으로 완결*. canonical 내부 진척 (옵션 X) 으로 이동.
3. **z_t 작업의 진행 여부**: 진행 시 archive 위험 6/6, 미진행 시 옵션 X/Y/Z 중 선택.
4. **DECL-1.0 amend 가능성**: 옵션 Y 가 사용자 결정 — Stage 6 에서는 *유보* 권장 (별도 세션).

---

*Stage 5 종료. Stage 6 (`07_decision.md`) 진입.*
