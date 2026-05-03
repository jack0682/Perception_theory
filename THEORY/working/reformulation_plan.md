# Reformulation Plan — C+E Cycle Active

**Status:** **Stage 0 locked (2026-04-20)** — Purpose = **C+E (Thermal Framework + Emergent-K)**. Stage 1 이 2026-04-21 진입 예정.
**Location:** `THEORY/working/reformulation_plan.md` (2026-04-19 저녁 이관. 다중 세션 gating 자료이므로 working/ 소관)
**Purpose pin:** `THEORY/working/reformulation_purpose.md` (2026-04-20 작성) — 한 줄 선언문 + rationale 5 + Non-goals 6 + 17-세션 stage 분배.
**Entry context:** `THEORY/working/open_problems_reframing_2026-04-19.md` — F-1/M-1/MO-1을 단일 원천 N-1로 통합 재프레이밍 완료
**User principle:** "이론적 목적이 분명하게 못을 박고 그다음 진행해야함." → Stage 0 = blocking gate. **해소됨 2026-04-20.**

---

## 0. 왜 이 플랜이 존재하는가

2026-04-12 Research OS (v2.0 kinetic, Option C)는 **purpose가 덜 다져진 상태에서 시작**되어 scaffolding에 삼켜져 4월 16일경 붕괴했다. 2026-04-18에 스캐폴드 전부 `_archive/`로. 같은 실패를 반복하지 않으려면:

1. 재공식화의 **이론적 목적(theoretical purpose)** 을 한 줄 선언문으로 먼저 고정.
2. 모든 후속 단계는 이 선언문에 정합해야 하고, 선언문에서 벗어나는 확장은 **별도 working topic**으로 분리.
3. 단방향 승급 파이프라인 유지: `logs/daily/2026-04-19/` → `working/` → `canonical/`. **canonical 직접 수정 금지.**
4. 에이전트 협업은 discrete 단위 호출로, 전체 계획의 오케스트레이션은 사용자가 직접 통제.

---

## Stage 0 — Purpose Declaration (BLOCKING)

본 플랜의 모든 하위 단계가 의존. **선언 전에는 Stage 1 이하 착수 금지.**

### Deliverable
한 줄 선언문 + 3~5개 bullet rationale. `02_purpose.md`로 본 디렉토리에 pinning.

### 후보 (reframing에서 도출된 5개)

#### A. 존재론 순화 — Soft-Hard Switching Asymmetry 해소 (N-1 정면)
- **주 목표:** 이론의 ontology(연속, graded)와 작동(이산 K, threshold, 공리 스위칭) 사이의 비원리적 스위칭 제거.
- **도달 지표:** canonical 내 모든 "정수 K" 등장 지점이 soft count로 대치됨 + threshold 선택이 parametric family로 명시됨.
- **commit:** K-field §12 폐기 또는 전면 재작성. 기존 T-Persist-K-* 정리 3개 전부 재검토.
- **NOT promise:** 계산 효율성 (soft-count는 H_0 persistent bars 등 비용 큼).
- **slogan:** "이론의 ontology와 작동을 같은 층위에 둔다."

#### B. 정직한 scope 제한 — 최소 수정, Honesty 승급
- **주 목표:** X_t, N_t, T, m, 25+개 파라미터가 pre-theoretic임을 명시적 Commitment Note로 승급. 공리계 불변.
- **도달 지표:** canonical §14에 CN15~CN20 추가. §12 주장에 scope-limitation 인라인 erratum.
- **commit:** 새 정리 없음. 기존 주장의 honesty 강화만.
- **NOT promise:** 이론의 실질적 진전. P-A, P-F 등은 그대로 open.
- **slogan:** "현 이론이 무엇에 대한 것이 아닌지를 명시한다."

#### C. 온도/엔트로피/노이즈 도입 (P-F 정면)
- **주 목표:** Metastability 주장이 정당화되도록 유한 온도 프레임워크 도입. `F = E - TS`, Langevin noise, Kramers rate 통합.
- **도달 지표:** canonical §8에 ε10 (stochastic gradient flow) 또는 §8B (thermal) 추가. §12 kinetic 주장이 framework 내에서 성립.
- **commit:** 새 공리 (F-group: thermal). Option C(폐기)의 원래 의도 부활하되 더 넓게.
- **NOT promise:** 온도 embedding의 유일성 (여러 가능).
- **slogan:** "Zero-temperature 주장을 유한 온도 위에 다시 놓는다."

#### D. Self-generating substrate (P-B 정면)
- **주 목표:** X_t 또는 N_t를 u_t로부터 유도. 외부 관계 구조 의존 제거.
- **도달 지표:** canonical §3에 derived adjacency (u → N) 매핑 도입. B-group 공리 재작성.
- **commit:** 유한 차원성 재검토, 기술적 난이도 최상.
- **NOT promise:** 유한 계산 가능성 보장. 수십 년 단위 프로젝트일 가능성.
- **slogan:** "관계 자체를 u에서 emerge시킨다."

#### E. Emergent-K framework (N-1 통합, A의 구체 경로)
- **주 목표:** K를 외부 정수 파라미터에서 derived soft quantity로 재정의. 단일 u를 더 부유한 공간(simplex-valued, measure-valued 등)에 정의.
- **도달 지표:** §12 multi-formation 전면 재작성. K-field `scc/multi.py` 재설계.
- **commit:** F-1/M-1/MO-1/OP-0004/OP-0005/OP-0006이 **단일 재공식화로 소멸 예상**.
- **NOT promise:** T-Persist-K-Sep/Weak/Unified 생존.
- **slogan:** "K를 세는 대신 K를 파생시킨다."

### 조합 가능성
- **C+E**: finite-T + emergent-K. 폐기된 Option C의 원래 의도에 가장 가까움. 가장 통합적 + 가장 큰 작업.
- **B+C**: 정직한 scope + 온도 도입. "진전하되 야심 제한"의 중간 경로.
- **A+C**: 존재론 순화 + 온도. A가 자체 완결이 어려우면 C가 P-F를 메우면서 N-1 해소 지원.

### 선택 기준 (사용자 판단 원칙)
다음 한 질문에 답하면 후보가 좁혀짐:

> **"내가 재공식화로 얻고자 하는 일등 결과물은 무엇인가?"**

- "수학적 일관성" → A 또는 E
- "현 주장의 정직함 복구" → B
- "metastability 주장의 framework 완성" → C
- "가장 야심찬 존재론" → D
- "F-1/M-1/MO-1 통합 소멸" → E (또는 C+E)

### Stage 0 Exit Criterion
`02_purpose.md` 파일에 다음이 기록됨:
1. 한 줄 선언문 (예: "재공식화의 목적은 K를 연속량으로 재정의하여 Soft-Hard Switching Asymmetry를 제거하는 것이다.")
2. 선택된 후보 (A/B/C/D/E 또는 조합).
3. 3~5개 rationale bullet (왜 이 purpose를, 왜 이 시점에).
4. **Non-goals** 3개 이상 (명시적으로 이번 reformulation에서 다루지 않을 것 — scope creep 방지).

---

## Stage 1 — Scope Definition

**Purpose가 fixed된 뒤 진입 가능.**

### 공통 deliverable
`03_scope.md`:

- **In scope:** 본 재공식화가 수정할 canonical 섹션 / 공리 / 정리 / 정의
- **Out of scope:** 언급은 되어도 이번에 손대지 않을 것 (명시하지 않으면 scope creep 매우 빠름)
- **Interfaces:** 본 재공식화가 건드리지 않는 근처 구조와의 경계

### Purpose별 스코프 특성

| Purpose | 주 스코프 | 주 경계 |
|---|---|---|
| A | §3, §5, §6, §7, §12, §14 commitment notes 다수 | §4 철학 부분은 불변 |
| B | §14 + 인라인 erratum | 공리·정의 전부 불변 |
| C | §8 (에너지), §6 Group E, §12 kinetic | §3 (formal universe) 원칙 불변 |
| D | §3 (formal universe), §6 Group B, §2 방어 섹션 | §7 predicate level 건드리지 않음 |
| E | §3 (u의 codomain), §12 전체, §7 Persist | §4~§11 단일 formation 부분 최대한 불변 |

---

## Stage 2 — Axiom Audit

기존 공리계 (A, B, C, D, E + A1', b_D=0, E3 demotion + 11 auxiliary constraints)를 Purpose에 대조하여 분류:

### 공통 산출: `04_axiom_audit.md`
각 공리에 대해:
- **Retain**: 수정 없이 유지
- **Modify**: 본문 변경 또는 조건 완화/강화
- **Retire**: 폐기
- **Add**: 신규 (특히 C, D, E purpose에서 예상)

### Purpose별 변화 양상 (예상, 실행 전 추정)

| | A | B | C | D | E |
|---|---|---|---|---|---|
| A1' | Retain | Retain | Retain | Retain | Modify (K 감안) |
| A3 contraction | Retain | Retain | Retain | Retain | Modify |
| B1-B4 | Retain | Retain | Retain | **Retire or Modify** | Retain |
| C1-C4 | **Modify** (세 모드 복원 후보) | Retain | Retain | Retain | Retain |
| D-Ax3 (`b_D=0`) | **Modify** | Retain (honesty note) | Retain | Retain | Retain |
| E1-E4 | Retain | **Modify** (E3 복원?) | Retain | Retain | Modify |
| Volume constraint (§8.0) | **Modify** (m genealogy) | Retain (CN 추가) | Retain | Retain | **Modify** |
| (신규) F-group thermal | — | — | **Add** | — | Optional Add |
| (신규) Soft-K axiom | — | — | — | — | **Add** |

이 표는 **예상치**. 실제 audit은 Stage 2에서 행별로 수행.

---

## Stage 3 — Definition & Derivation Pass

Stage 2가 확정한 공리 변화에 맞춰, canonical §3~§7의 정의를 재도출.

### 공통 산출: `05_definitions.md`
- 변경된 공리에서 출발하여 operators, predicates, energy terms 재도출
- 기존 derivations 중 깨지는 것 식별
- 신규 정의 (purpose가 새 개념 요구하면)

### Risks
- **Silent resolution.** 재도출 과정에서 기존 open problem(예: self-referential transport uniqueness)이 `암묵적으로` 새 공리에 의해 해결된 것처럼 보이면 — **명시적 증명 없이 해결 주장 금지**. erratum이 아닌 open note로 유지.
- **Cohomology drift.** 개념 재정의가 원래 의도(pre-objective)에서 이탈하면 감지하기 어려움. 단계별로 §2~§4 철학 섹션과의 정합성 체크.

---

## Stage 4 — Theorem Survival Audit

기존 canonical §13: 35 Category A + 4 Cat B + 5 Cat C + 5 Retracted = 49 claims.

### 공통 산출: `06_theorem_survival.md`

각 정리에 대해 Purpose 적용 후 상태:
- **Survive**: 증명 변화 없음
- **Re-prove**: 공리 변화로 증명 필요 재작성
- **Downgrade**: Category 강등 (A→B, B→C)
- **Retire**: 폐기 (Retracted)
- **Unknown**: 미결 (후속 분석 필요)

### Purpose E 예상 (가장 큰 변화)
- T-Persist-K-Sep / K-Weak / K-Unified: **대부분 Retire** (K-field 아키텍처 폐기시)
- T-Persist-1(a,b,c,d,e): 단일 formation 정리 — Survive 기대
- T8-Core, T8-Full (phase transition): Survive 기대 (scalar field 이론)
- T-Merge (a), (b), Topological Lock: K-field 가정에 의존 → Re-prove 또는 Retire

### Purpose C 예상 (온도 도입)
- 대부분 Retain (기존 정리는 zero-T 극한으로 살아있음)
- 추가 thermal 정리 (Kramers, escape time, FDT 등) 새로 증명

---

## Stage 5 — Code & Test Alignment

`CODE/scc/` 및 `CODE/tests/` (175 passing) 에 대한 영향 감사.

### 공통 산출: `07_code_impact.md`
- `scc/*.py` 각 모듈에 대해: Retain / Modify / Rewrite / Retire
- `tests/*.py` 각 테스트: Survive / Need-update / Obsolete
- 신규 모듈/테스트 필요성

### Purpose별 주요 영향

| Purpose | 가장 큰 코드 영향 |
|---|---|
| A | `scc/multi.py` 재설계, predicates threshold parameterization |
| B | 없음 (docstring만 업데이트) |
| C | 신규 `scc/thermal.py`, noise injection into optimizer |
| D | `scc/graph.py` 재설계 (u → N 파이프라인) |
| E | `scc/multi.py` 폐기 + 신규 `scc/soft_k.py` |

175 test 중 **생존 수**가 재공식화 성공 지표 중 하나. Purpose E에서는 50~100개까지 줄어들 가능성 현실적.

---

## Stage 6 — Publication & Canonical Promotion

### 공통 산출
- `08_canonical_diff.md` — 재공식화된 canonical 전문 vs 기존 v1.2 차분
- `THEORY/canonical/canonical.md` 교체 (승급 단계)
- `THEORY/canonical/theorem_status.md` 갱신
- `THEORY/canonical/theorem_status.md` 재작성 (N-1 등 신규 문제 포함)
- `THEORY/CHANGELOG.md` 주요 항목
- `CODE/papers/` 관련 섹션 업데이트 (해당 시)

### 승급 체크리스트 (canonical 교체 전)
- [ ] Stage 0 purpose 선언문이 canonical 서문에 반영됨
- [ ] Stage 2 axiom audit의 각 결정이 canonical 본문에 대응됨
- [ ] Stage 4 theorem survival이 theorem_status.md에 반영됨
- [ ] Non-goals 섹션이 canonical §11 "Open Design Choices"에 추가됨
- [ ] 새 open problem(예: N-1 잔여)이 theorem_status.md에 registered
- [ ] Test suite 통과 (CODE/tests/ 실행 결과 첨부)
- [ ] 사용자 최종 승인

---

## 에이전트 협업 프로토콜

### 사용 원칙
- **OMC 풀 오케스트레이션 금지** (autopilot / ralph / team / ultrawork) — 사용자 철학 중심 유지.
- **개별 Agent tool** (Explore, Plan, scientist, critic, debugger 등) 은 discrete task 단위로 호출.
- 각 에이전트 호출은 **명확한 single-deliverable**를 명시해야 함.
- 에이전트 산출물은 본 디렉토리 `2026-04-19/` 또는 이후 날짜의 `2026-MM-DD/`에 저장 후 사용자 검토 → working 승급.

### 단계별 에이전트 활용 예시 (사용자 결정시)
- **Stage 0 purpose 선택 전**: Agent 호출 금지. 사용자 판단.
- **Stage 1 scope**: Explore 1개 → canonical 섹션별 영향 범위 매핑.
- **Stage 2 axiom audit**: Plan 또는 critic 2개 병렬 → 독립 audit → 교차 검증.
- **Stage 3 definitions**: scientist 1개 → 수학적 정합성 체크.
- **Stage 4 theorem survival**: critic 2~3개 병렬 → Category별 독립 감사.
- **Stage 5 code impact**: general-purpose 1개 → import/signature scan.
- **Stage 6 promotion**: 에이전트 없이 사용자 직접 승급.

### 에이전트 output 규약
본 디렉토리에 저장되는 에이전트 산출물은 파일명 prefix로 출처 표시:
- `agent_<type>_<topic>_<idx>.md` (예: `agent_critic_axiom_audit_01.md`)
- 에이전트 호출 prompt 원문을 해당 파일 끝에 `## Original prompt` 섹션으로 첨부 → 재현 가능성 보장.

---

## 성공 기준

재공식화 **완료**의 정의:

1. **Purpose 완전 반영**: Stage 0 선언문의 모든 주장이 canonical 본문에 대응됨.
2. **No silent resolution**: 명시적으로 다루지 않은 기존 open problem은 재공식화 후에도 여전히 open으로 남아있음.
3. **Consistency**: canonical v(next) 내부에서 공리 → 정의 → 정리 → 예측의 파이프라인이 검증 가능.
4. **Test alignment**: `CODE/tests/` 가 새 canonical에 맞춰 조정되고 재실행시 알려진 failure만 남음.
5. **Changelog transparency**: `THEORY/CHANGELOG.md` 에 변경 전 / 변경 후 비교 명료.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Scope creep (purpose 외 영역까지 건드림) | Stage 0 Non-goals를 강제, Stage 1 scope doc에 반복 참조 |
| Silent resolution (open problem이 공리 재편에 의해 암묵적 해결 주장) | Stage 3/4에서 explicit check, 모든 "이제 해결됨" 주장에 증명 요구 |
| Research OS 재현 (scaffolding 팽창) | 본 디렉토리 외 구조 생성 금지, logs→working→canonical 파이프라인만 사용 |
| Category A 다수 상실 | Stage 4 audit에서 "잃어도 좋은 것"과 "반드시 보존할 것" 을 Purpose에 비추어 사전 분류 |
| 파라미터 유일성 주장 혼입 | 본 재공식화는 파라미터 origin (P-E) 을 다루지 않는 한 "수치 유일성" 주장 금지 |
| 에이전트 출력의 일관성 실패 (독립 호출간 용어 충돌) | 각 에이전트 prompt에 "현재 용어 사전: 01_reformulation_plan.md 참조" 명시 |

---

## Timeline (유연, daily-scale)

Daily progression. 하드 데드라인 없음. 단, Stage gate 순서는 준수.

- **Stage 0**: 1 session (purpose 선택 + 선언문 작성)
- **Stage 1**: 1-2 sessions
- **Stage 2**: 2-3 sessions (에이전트 활용시 병렬 가능)
- **Stage 3**: 3-5 sessions (Purpose 난이도에 따라)
- **Stage 4**: 2-4 sessions (정리 수 다수 × Category 감사)
- **Stage 5**: 1-2 sessions
- **Stage 6**: 1 session (승급 + 승인)

**총 예상**: 11~18 sessions. Purpose B는 하한, Purpose D/E는 상한.

---

## 다음 Action

**오직 Stage 0**. 사용자가 다음 중 하나를 선택:

1. 후보 하나를 pin: "A로 간다" / "B로 간다" / ...
2. 조합 선택: "C+E로 간다" / "B+C로 간다"
3. 후보 간 차이를 더 탐사하고 싶음: "각 후보의 Stage 1 scope를 더 구체화해서 보여달라"
4. 5 후보에 없는 6번째 purpose 제안: "실은 다른 목적이 있다..."

선택 후: `02_purpose.md` 작성 → Stage 1 착수 권한 열림.

---

## 본 플랜 자체의 메타

- **작성**: 2026-04-19
- **위치**: `THEORY/logs/daily/2026-04-19/01_reformulation_plan.md` (logs/daily 단계, 날것)
- **승급 경로**: 메타-플랜이 안정화되면 → `THEORY/working/reformulation_plan.md` (주제별 working)
- **플랜의 플랜**: 본 문서 자체를 재공식화 시작 전에 완결할 필요는 없음 — Stage 0 선택 후 Stage 1 진입 전까지 수정 자유.
