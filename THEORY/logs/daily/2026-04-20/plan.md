# Plan — 2026-04-20

## Target

**재공식화 Stage 0 (Purpose Declaration) 확정을 위한 의사결정 재료 생산.**

구체적으로: A/B/C/D/E 다섯 purpose 후보 각각에 대해 (i) **Open Problem coverage matrix** (기존 OP + 신규 P-A~P-H + 단일 원천 N-1), (ii) **Theorem Survival matrix** (canonical §13 의 49 claims), (iii) **첫 3세션의 구체 산출물 스케치**, (iv) **risk·scope 비교표**, (v) **단일 후보 vs 주요 조합 (C+E / B+C / A+C) 정밀 비교** 를 생산한다. 에이전트는 **최종 선택을 하지 않는다** — 사용자가 저녁에 `THEORY/working/reformulation_purpose.md` 를 작성할 때 참고할 **정량적·구체적 근거** 만 제공한다.

## Why now

- Stage 0 은 `THEORY/working/reformulation_plan.md` 에서 명시된 **blocking gate**. 미확정 상태에서는 Stage 1~6 전부 착수 불가.
- 사용자는 5 후보의 **직관적** tradeoff 는 파악했으나, 각 후보가 실제 작업으로 펼쳐졌을 때 **구체상** — 어떤 파일을 쓰고, 어떤 정리가 생존/소멸하며, 어떤 새 문제가 생기는지 — 이 부족한 상태. 직관만으로 선택하면 2026-04-12 Research OS 식 drift 재발 위험.
- 한 세션으로 purpose 를 **결정** 하는 것이 아니라 **결정 가능하게 만든다** 는 scope 유지. "하루에 너무 많이 풀지 않는다" 원칙 준수.
- N-1 (Soft-Hard Switching Asymmetry) 이 단일 원천으로 드러난 이후 각 후보가 N-1 을 어떻게 다루는지가 핵심 축이 됨. 이 축 아래에서 비교가 정렬되면 선택이 쉬워짐.

## Context refs (에이전트 세션 진입 시 읽어야 할 소재)

- **`THEORY/working/reformulation_plan.md`** §Stage 0 — 5 후보 (A/B/C/D/E) 의 원본 정의, commitment, NOT promise, slogan.
- **`THEORY/working/open_problems_reframing_2026-04-19.md`** — N-1 단일 원천 + P-A~P-H 9개 신 problem 정의 + F/M/MO 교차 대조 표 (§9) + 재명명된 문제 전수 설명.
- **`THEORY/canonical/canonical.md`** — 특히 §3 (formal universe), §6 (axiom groups A-E), §8 (energy), §11 (fixed commitments & open design choices), §12 (open problems), §13 (49 claims registry), §14 (CN1–CN14 commitment notes).
- **`THEORY/canonical/theorem_status.md`** — 49 claims 현재 Category (35 A / 4 B / 5 C / 5 Retracted) 및 각각의 소스 (canonical §13 참조).
- **`THEORY/canonical/open_problems.md`** — 기존 OP-0001 ~ OP-0007. 각 후보가 어떤 OP 를 건드리는지 대응 필요.
- **`THEORY/logs/daily/2026-04-19/00_session_log.md`** — 전 세션 narrative 와 carry-forward.
- **`THEORY/logs/daily/MAIN_PROMPT.md`** 는 에이전트에게 이미 주어진 지시이므로 다시 읽지 말 것 — 중복.

## Current hypotheses / approaches under consideration

사용자의 잠정 직감 (에이전트는 이 안에만 머물지 않음 — 출발점):

1. **후보 E (Emergent-K)** 가 N-1 을 가장 정면으로 다루고 F/M/MO 삼총사를 통합 소멸시킬 잠재력이 크다 — 하지만 T-Persist-K-Sep / K-Weak / K-Unified 3개가 전부 재검토 대상이 되어 Category B/C 상실 위험.
2. **후보 C (Temperature/entropy)** 는 metastability 주장의 framework 공백 (P-F) 을 메운다 — 현 주장의 암묵적 지지대를 공식화.
3. **C+E 조합** 이 폐기된 Option C 의 원래 의도에 가장 가깝고 통합적. 작업량은 최대이나 공통 framework 로 묶임.
4. **후보 B (honest scope)** 는 최소 작업으로 정직성만 확보 — 이론 진전 없음. "보험" 또는 C/E 실패시 fallback. 단독 선택 가치 불명.
5. **후보 A (존재론 순화)** 는 E 보다 광역 — A 가 모(母) 목표이고 E 가 그 하위 구체 경로인가? 아니면 독립 병렬인가?
6. **후보 D (self-generating substrate)** 는 야심 최대이나 다른 후보의 선결조건이 아니며 시간 규모 크다 — 이번 purpose 로는 후순위.

핵심 미해소 질문 (에이전트 답변 필수):
- **Q1. A 와 E 의 포함관계** — E 는 A 의 구체 경로인가, 병렬 경로인가, 독립 경로인가? 수학적·개념적 근거와 함께.
- **Q2. B 의 단독 가치** — B 를 단독 선택하는 것이 의미 있는 시나리오가 존재하는가? 존재한다면 어떤 조건에서?
- **Q3. 조합 비용의 선형성** — C+E 의 작업량이 C 비용 + E 비용 보다 큰가 작은가? 상호작용 효과 추정.
- **Q4. D 의 deferability** — D 를 이번에 미룰 때, 선택된 purpose 가 D 에 우호적이어야 하는 조건은 무엇인가?

## Session goals (에이전트 핵심 deliverable — 3개)

### G1. Dual Matrix — Open Problem Coverage × Theorem Survival

에이전트가 `01_exploration.md` 에 두 매트릭스를 생성.

**Matrix-1 (Open Problem Coverage)**
- **행:** 기존 OP-0001 ~ OP-0007 + 신규 P-A, P-B, P-C, P-D, P-E, P-F, P-G, P-H + 단일 원천 N-1 (최소 16 행).
- **열:** A, B, C, D, E.
- **셀:** `완전해결` / `부분해결` / `방치` / `악화` / `새 문제 생성` 중 하나 + 1~2문장 정당화.
- 각 후보 열의 하단에 "총 완전해결 / 부분해결 / 방치 수" 집계.

**Matrix-2 (Theorem Survival)**
- **행:** canonical §13 의 49 claims 전체 (35 Category A 는 특히 정밀하게, 4 Category B 와 5 Category C 는 조건부로 판정, 5 Retracted 는 "이미 폐기" 표시).
- **열:** A, B, C, D, E.
- **셀:** `Survive` (무변화) / `Re-prove` (증명 재작성 필요, 결과는 유지) / `Downgrade` (카테고리 하향) / `Retire` (폐기) / `Unknown` (판정 불가) 중 하나.
- 각 후보 열의 하단에 "Category A 상실 수" 집계 — 이것이 보수적 지표.

두 매트릭스는 **단일 문서** 에 나란히 배치. 크로스 참조 (예: "P-A 완전해결 → C-0550 Retire 를 함의") 를 인접 섹션에서 기술.

### G2. 각 후보의 "첫 3세션" 구체 스케치

에이전트가 `02_development.md` 에 작성. 각 후보 A/B/C/D/E 에 대해, 내일 Stage 1 을 시작한다면 Session 1·2·3 이 무엇을 할지.

각 세션 항목은 다음을 포함:
- **Target** (한 문장)
- **생산할 파일명과 내용 요약** (working/ 또는 daily/ 어느 쪽에 어떤 이름으로)
- **수학적 작업의 유형** (정의 / 증명 / 반례 구성 / 공리 조작 / 수치 실험 / 서술)
- **건드리는 canonical 섹션** (예: §3.3, §6 Group E, §8.5, §12)
- **선결조건 / 의존** (이전 세션 산출물, 외부 정리, 관련 정의)

**추상 금지.** "Session 1: 개념 정리" 같은 표현은 실패. "Session 1: `working/soft_K_definition.md` 작성. K 를 H_0 persistence bar length 가중합 $K_{\mathrm{soft}} = \sum_i \ell_i \cdot \phi(\ell_i)$ 로 정의. canonical §5 (derived morphology) 에 추가될 후보. 정의의 well-defined 성 증명 (persistence stability theorem 에 의한 Lipschitz bound). 선결: persistence stability 정리 진술 확정." 식으로 구체.

5 후보 × 3 세션 = 15 세션 스케치. 간결하게, 그러나 충실히.

### G3. 단일 vs 조합 후보 정밀 비교 + A/E 관계 + 최종 권고

에이전트가 `03_integration_and_new_open.md` + `99_summary.md` 에 작성.

구성:
- **A/E 관계 진단** — Q1 에 대한 답. 수학적·개념적 근거. 포함/병렬/독립 중 하나 선택 + 그 근거.
- **조합 비용 분석 (Q3)** — C+E / B+C / A+C 세 조합 각각:
  - 단일 후보 대비 추가로 얻는 것
  - 단일 후보 대비 추가로 잃는 것
  - 작업량 선형·초선형·준선형 추정 (이유 포함)
- **B 단독 가치 진단 (Q2)** — B 단독이 최적인 시나리오가 존재하는지, 존재한다면 조건.
- **D 의 deferability (Q4)** — D 를 후순위로 할 때 현 선택이 D 에 우호적이어야 하는 구조적 조건.
- **최종 권고** — 5 단일 후보 + 3 조합 후보 = 8 선택지 중 하나를 권고. 3개 이유 (각각 Matrix-1/Matrix-2/세션 스케치 중 하나에 근거). 강제력 없음 명시.
- **사용자에게의 한 줄 메시지** (`99_summary.md` 끝) — "오늘 저녁 `reformulation_purpose.md` 작성시 참고할 최단 경로: [권고안 + 주요 근거 1개]".

## Non-goals (오늘 안 할 것)

- **실제 공리 재작성, 정리 재증명, 새 정의의 수학적 성립 증명** — 전부 Stage 1 이후. 오늘은 "어떤 작업이 있을 것이다"의 나열만.
- **canonical.md 의 구체 patch-level 수정안** — "어떤 섹션이 영향받는다" 수준의 high-level 만.
- **사용자 대신 purpose 최종 결정** — 에이전트의 권고는 재료일 뿐. 강제력·최종성 없음.
- **N-1 자체의 해결 시도** — "각 후보가 N-1 을 어떻게 다루는가" 만 논의. N-1 을 풀지 않음.
- **새 experiment 설계 / 기존 실험 결과 재해석** — Stage 4 까지 밀어둠.
- **CODE/ 쪽 코드 변경 제안** — Stage 5 이후.
- **완전히 새 후보 (F, G, ...) 를 창안** — 이미 5 후보 + 3 조합 = 8 선택지면 충분. 제6 후보 창안은 silent scope creep 이 될 수 있음.

## Carry-forward (2026-04-19 로부터)

- **Stage 0 blocking gate 미해소** — 오늘의 최우선 과제.
- `reformulation_plan.md` 는 Stage 0 외 Stage 1~6 의 **구조** 만 제공. Stage 0 내부의 후보 비교는 아직 얕다 (각 후보 4~6줄 요약 수준). 오늘 이 깊이를 채운다.
- `open_problems_reframing_2026-04-19.md` 의 **N-1 이 공통 축** — 오늘 에이전트는 N-1 언어로 각 후보를 평가한다. F/M/MO 용어가 필요하면 "N-1 의 특정 얼굴" 이라 언급하는 방식으로만.
- 어제 세션 산출물 (reframing + reformulation_plan + MAIN_PROMPT + 새 workflow) 은 **인프라**. 오늘은 이 인프라 위에서 **실제 이론적 판단** 이 처음 시도되는 날.
- 기존 canonical v1.2 의 발표 메타 `id: CV-1.2, released: 2026-04-12` 는 **역사적 날짜** 로 불변 — 이번 재공식화가 canonical 교체를 낳더라도 v1.2 릴리즈 날짜는 2026-04-12 로 남음.

## Success criterion for today

**저녁 시점에 사용자가 `THEORY/working/reformulation_purpose.md` 를 작성하려 할 때, 에이전트가 생산한 Matrix-1 (coverage) 또는 Matrix-2 (survival) 를 참조하면서 "이 근거로 X 를 선택한다 — Matrix 가 보여주듯 X 는 {OP 해결 N개 / Category A 상실 k개 / 작업량 ~m세션} 이기 때문" 이라고 말할 수 있어야 한다.**

단계별 체크:
- [ ] Matrix-1 이 16+ 행 × 5 열 완성 (각 셀에 판정 + 1~2문장 정당화)
- [ ] Matrix-2 가 49 행 × 5 열 완성 (최소 Category A 35 행은 정밀 판정)
- [ ] 각 후보에 대한 3세션 스케치가 "파일명 + 수학 작업 유형 + 건드리는 canonical 섹션" 3요소 포함
- [ ] Q1, Q2, Q3, Q4 에 대한 명시적 답변
- [ ] 에이전트 권고 (1개) + 3 근거
- [ ] `99_summary.md` 에 사용자용 한 줄 메시지

하나라도 미달이면 성공 기준 미충족. 후속 "검증하고 보완하라" 요청 필요.

---

## 작성 메타 (사용자 → 에이전트에게 직접 지시는 아님)

- 본 plan 은 **2026-04-19 저녁** (약 자정 이후 새벽 포함) 에 사용자가 작성. PLAN_TEMPLATE.md 의 구조를 따름.
- 다음 단계: **2026-04-20 아침** 에 사용자가 `THEORY/logs/daily/MAIN_PROMPT.md` 의 `{DATE}` 를 `2026-04-20` 로 치환하여 Agent tool 에 투입. 에이전트는 이 `plan.md` 를 세션 진입시 가장 먼저 읽게 됨.
- 에이전트 출력 위치: **같은 폴더** (`THEORY/logs/daily/2026-04-20/`) 내 `01_exploration.md` / `02_development.md` / `03_integration_and_new_open.md` / `99_summary.md`.
- **저녁 후속 (사용자 할 일):**
  1. 산출물 검토 (필요시 "검증하고 보완하라" 추가 요청)
  2. `THEORY/working/reformulation_purpose.md` 작성 — 한 줄 선언문 + rationale 3~5 bullet + Non-goals 3+ 개
  3. Stage 0 완료 표시 (`reformulation_plan.md` 상단의 "Stage 0 pending" → "Stage 0 locked: <선택>")
  4. 내일 (`2026-04-21`) plan.md 작성 — Stage 1 (Scope Definition) 첫 sub-task

- **본 plan 의 scope 는 의도적으로 meta.** 이론 자체를 건드리지 않고 **이론에 대한 결정의 토대** 만 만드는 세션. 내일 이후부터 실제 이론 작업으로 진입. 이 구분이 무너지면 scope creep.
