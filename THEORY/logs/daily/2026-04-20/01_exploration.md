# 01 — Exploration: Stage 0 Purpose Decision Material (Dual Matrix)

**Session:** 2026-04-20
**Target (from plan.md):** 재공식화 Stage 0 (Purpose Declaration) 확정을 위한 의사결정 재료 생산 — 5 후보 (A/B/C/D/E) + 3 조합 (C+E, B+C, A+C) 에 대한 Matrix-1 (OP coverage) · Matrix-2 (Theorem survival) · 세션 스케치 재료 · Q1~Q4 답변 · 단일 권고 1개. **최종 선택 금지** — 재료만.
**This file covers:** §1 Restatement · §2 Multi-approach (3+) · §3 Primary selection rationale · §4 Matrix-1 · §5 Matrix-2 · §6 Cross-reference between matrices.
**Depends on reading:** `THEORY/logs/daily/2026-04-20/plan.md`; `THEORY/working/reformulation_plan.md` §Stage 0; `THEORY/working/open_problems_reframing_2026-04-19.md` §1–§9; `THEORY/canonical/canonical.md` §3, §6, §8, §11, §12, §13, §14 (CN1–14); `THEORY/canonical/open_problems.md` OP-0001~0007; `THEORY/canonical/theorem_status.md` 전체.

---

## §1. Restatement

### 1.1 본 세션은 이론 작업이 아니라 **메타-결정 작업**이다

이 세션의 산출물은 **정리의 증명**도, **공리의 재작성**도, **새 정의의 well-definedness 증명**도 아니다. 그 모든 작업은 Stage 1~6 에 속한다. 본 세션은 그 전단계 — **Stage 0 Exit Criterion** (한 줄 purpose 선언문 + rationale + Non-goals) 을 사용자가 오늘 저녁 작성할 때 의존할 **정량적 재료** 를 생산한다.

"정량적" 이란:

- 각 후보가 건드리는 **Open Problem 의 개수**와 **방식**을 셀 수 있음 (Matrix-1).
- 각 후보가 **폐기·재증명·강등·생존** 시키는 기존 정리의 수를 셀 수 있음 (Matrix-2).
- 각 후보가 내일 실제 진입 가능한지를 **3개의 첫 세션** 으로 예증 가능함 (02_development.md).

### 1.2 plan.md 의 암묵적 가정 표면화

**가정 1 (단일 원천 N-1):** plan.md 는 "N-1 (Soft-Hard Switching Asymmetry) 이 단일 원천으로 드러난 이후 각 후보가 N-1 을 어떻게 다루는지가 핵심 축" 이라고 선언. 이 축 위에서 5 후보가 정렬됨을 전제. → 본 세션은 이 전제를 수용하되, N-1 의 세 얼굴 (K / threshold / axiom-switching) 각각이 어느 후보에서 어떻게 처리되는지를 분리하여 매트릭스에 반영한다.

**가정 2 (silent scope creep 방지):** plan.md 는 "완전히 새 후보 (F, G, ...) 를 창안 금지" 명시. 5 단일 + 3 조합 = 8 선택지만 평가. → 본 세션은 이를 엄격 준수.

**가정 3 (선택 권한 없음):** 에이전트의 권고는 1개이되 강제력 없음. 사용자는 재료를 보고 독립 결정. → 본 세션은 권고를 최종 섹션(`03_integration_and_new_open.md` §7) 에만 배치하며 매트릭스 · 스케치 자체는 평가적 서술을 최소화.

**가정 4 (성공 기준의 형태):** plan.md §Success criterion 은 "저녁에 사용자가 `reformulation_purpose.md` 를 쓸 때 'Matrix 가 보여주듯 X 는 {OP N개 / Cat A k개 / ~m세션}' 라고 말할 수 있어야" 를 요구. → 본 세션의 매트릭스는 **cell 단위로 근거를 제시**해야 하며, 단순 ✓/✗ 코드만으로는 불충분. 각 셀은 코드 + 1~2문장 정당화.

### 1.3 무엇이 성공인가 / 무엇이 실패인가

**성공:**
- Matrix-1: 16행 × 5열, 각 셀 {완전/부분/방치/악화/생성} + 1~2문장.
- Matrix-2: 49행 × 5열, 각 셀 {생존/재증명/강등/폐기/미지}. Cat A 35행 정밀, Cat B 4행 조건부, Cat C 5행 조건부, Retracted 5행 표시만.
- Q1, Q2, Q3, Q4 명시 답변.
- 권고 1개 + 3 근거.
- 99_summary.md 한 줄 메시지.

**실패:**
- 에이전트가 "이 세션이 E 를 최적으로 결정한다" 식으로 사용자의 선택 권한을 찬탈.
- 후보 1개에만 정밀하고 나머지는 1~2 cell 만 채움.
- N-1 의 세 얼굴 중 K 만 논하고 threshold / axiom-switching 얼굴을 누락.
- 기존 open problem 중 plan target 이 아닌 것을 "해결됨" 으로 silent 주장.

### 1.4 5 후보의 one-line 재진술 (나의 언어로)

| 후보 | 한 줄 요약 (my words) | N-1 취급 방식 |
|---|---|---|
| **A. Ontology purification** | Soft-Hard switching 을 모든 등장 지점에서 제거 — K, threshold, 공리 모두 대상. | N-1 **전체** 대상. E 를 포함하되 더 넓음. |
| **B. Honest scope** | 현 이론이 무엇의 이론이 **아닌지** 를 CN 으로 명시. 공리·정리 불변. | N-1 을 **honesty note 로 승급** — 해결하지 않고 pin. |
| **C. Temperature/entropy** | 유한 T · entropy · noise 를 공리에 편입. Zero-T 결정론 탈출. | N-1 의 **hard 측** (정수 K 선택) 에 thermodynamic 정당성 부여. soft 측은 불변. |
| **D. Self-generating substrate** | X_t · N_t 를 u_t 에서 유도. 외부 관계 입력 제거. | N-1 과 **orthogonal** — substrate 레벨 문제에 집중. |
| **E. Emergent-K** | K 를 외부 정수 파라미터에서 derived soft quantity 로 재정의. 단일 u 에서 K readout. | N-1 의 **K 얼굴만** 정면 — threshold / axiom 얼굴은 out-of-scope. |

이 재진술은 plan.md 의 원문과 일치하되, N-1 의 세 얼굴 (K / threshold / axiom-switching, `open_problems_reframing_2026-04-19.md` §8 참조) 을 기준으로 coverage 를 분류.

---

## §2. Multi-approach

### 2.1 접근 (a) — Coverage-first (gravity method)

**핵심 아이디어:** Matrix-1 (OP coverage) 를 먼저 채우고, 각 후보가 건드리는 OP 의 총량과 분포를 정량화. 그 결과가 각 후보의 "중력" 을 결정. Matrix-2 (theorem survival) 는 coverage 에 의해 induced 되는 비용. 세션 스케치는 coverage 달성의 첫 3 단계로 역산.

**성공 시 결과물:** 사용자는 Matrix-1 을 보고 "가장 많은 OP 를 해결하는 후보 = X" 를 즉시 식별. 이어 Matrix-2 로 그 X 의 비용 (Cat A 상실) 을 확인. 세션 스케치로 실행 가능성 확인.

**실패 모드:** "해결" 의 정의가 후보마다 다를 수 있다. 예: E 는 "OP-0002 M-1 이 well-posed 하지 않게 됨" 을 완전해결 로 코드하지만, 이것이 정말 해결인지 소멸인지 해석 차이. 코딩의 granularity 가 후보 간 불균등하면 매트릭스는 biased.

**기존 정리·공리와의 상호작용:** 직접 없음. Matrix-2 에서 비용이 드러남.

**이 접근의 의의:** 본 세션의 G1 (plan.md §Goals) 가 직접 두 매트릭스를 요구하므로, coverage-first 는 **요구사항과 일치**.

### 2.2 접근 (b) — Commitment-first (axiomatic method)

**핵심 아이디어:** 각 후보가 canonical §6 (Axiomatic Groups) 에 **어떤 공리를 추가·수정·폐기** 하는지를 먼저 명시. 그 공리 변경이 §13 의 49 정리에 induce 하는 survival 을 **연역**. OP coverage 는 공리 변경의 부산물로 간주.

**성공 시 결과물:** 각 후보가 "A1' 유지, A3 유지, E3 재작성, B-group 전면 폐기" 같은 공리-수준 commitment 로 요약됨. 이것이 Matrix-2 의 primary 정당화가 됨.

**실패 모드:** Stage 0 은 공리 수준 선택 전단계다. 공리 변경을 먼저 확정하려 하면 Stage 2 (Axiom Audit) 의 작업을 선행하게 되어 **stage gate 위반**. `reformulation_plan.md` 에 명시된 gate 순서 무시.

**기존 정리·공리와의 상호작용:** 많음. 각 후보의 공리 commitment 가 §6 의 각 Group 에 매핑.

**이 접근의 의의:** 이론적으로 가장 엄밀하나 Stage gate 를 침해. 본 세션에는 primary 로 부적합. 다만 **보조적으로** 각 후보의 공리 영향 요약을 `reformulation_plan.md` §Stage 2 예상 표 로부터 차용 가능 — coverage-first 매트릭스의 각주에 활용.

### 2.3 접근 (c) — Failure-mode-first (risk method)

**핵심 아이디어:** 각 후보가 **실패**할 수 있는 방식을 먼저 상정 — "E 는 soft-K 정의가 H_0 persistence 외에 잘 작동 안 할 때 실패", "C 는 T 의 ontology 가 설명되지 않을 때 실패" 등. 실패 시나리오에서 역산하여 각 후보의 scope 경계를 획정. Matrix 는 실패 경계 내에서의 coverage 만 인정.

**성공 시 결과물:** 매트릭스의 각 cell 이 "성공 시 Y, 실패 시 Z" 의 조건부 형태가 됨. risk-adjusted coverage.

**실패 모드:** 실패 정의 자체가 주관적. 매트릭스가 가설적 조건문들의 집합이 되어 **비교 불가능**. plan.md 의 Success criterion ("X 를 선택한다 — Matrix 가 보여주듯 X 는 ...") 을 만족시키지 못함.

**기존 정리·공리와의 상호작용:** 간접. 각 정리 survival 이 "조건부 생존" 이 됨 — 이미 canonical §13 이 Cat A/B/C 로 구조적 조건부 를 분류하고 있어 중복.

**이 접근의 의의:** Primary 로는 부적합. 그러나 **risk 섹션** (`03_integration_and_new_open.md` §Combination Cost 의 subsection) 에서 활용. 각 조합의 실패 모드 1~2개를 섹션 §5 (risk) 로 흡수.

### 2.4 접근의 수학적 독립성 점검

세 접근은:
- **수학 도구 독립** — (a) 는 coverage 집계, (b) 는 공리 변경의 연역, (c) 는 조건부 case analysis. 서로 다른 방법론.
- **실패 모드 독립** — (a) 는 coding granularity, (b) 는 stage gate 위반, (c) 는 비교 불가능. 공통 실패 원인 없음.
- **성공 조건 독립** — (a) 는 플랜 G1 요구와 일치, (b) 는 공리 수준에서 엄밀, (c) 는 risk 측면.

독립성 기준 충족.

---

## §3. Primary Selection + Alternative Preservation

**Primary: 접근 (a) Coverage-first.**

근거:
1. **Plan G1 요구와 직접 일치.** plan.md §Session goals §G1 은 "두 매트릭스를 단일 문서에 나란히 배치" 를 명시. Coverage-first 는 이 요구의 자연스러운 수행.
2. **Stage gate 준수.** 공리 수준 commitment 를 선행하지 않음 — 그 작업은 Stage 2 에 속함. Stage 0 은 purpose-level 결정에 집중.
3. **cell 단위 비교가능성.** 매트릭스의 셀이 모두 {완전/부분/방치/악화/생성} 의 5값 codomain 을 공유. 후보 간 직접 비교 가능.

**보존되는 대안:**
- **(b) Commitment-first** 는 Matrix-2 의 각 셀에 대한 "왜 생존/폐기" 연역 근거로 각주 활용 (다만 본 세션에서 공리 변경을 확정하지 않음 — 예측치일 뿐).
- **(c) Failure-mode-first** 는 `03_integration_and_new_open.md` 의 조합 비용 분석 (Q3) 에서 활용 — 각 조합의 "실패 시 어디로 돌아가야 하는가" 측면.

둘 다 `03_integration_and_new_open.md` 의 섹션 내부에서만 사용 — `01_exploration.md` 의 매트릭스 본체는 순수 coverage-first 로 유지.

---

## §4. Matrix-1 — Open Problem Coverage × Purpose

**행 (16):** OP-0001~0007 (기존 canonical) + P-A~P-H (reframing 2026-04-19) + N-1 (단일 원천).
**열 (5):** A, B, C, D, E.
**셀 code:** `완전` (완전해결), `부분` (부분해결), `방치` (영향 없음), `악화` (문제가 더 나빠짐), `생성` (기존 문제 해결하되 새 하위 문제 발생).
**각 cell:** 코드 + 1~2문장 정당화.

### 4.1 The Matrix

| Row | A (Ontology) | B (Honest scope) | C (Thermal) | D (Substrate) | E (Emergent-K) |
|---|---|---|---|---|---|
| **OP-0001 (F-1, K=2 vacuity)** | `완전` — A 의 declared scope 에 "모든 정수 K 등장 지점이 soft count 로 대치" 포함. K 가 soft 되면 "K=2 stability" 는 문법적으로 재정의됨. vacuity 개념 소멸. E 와 동일 메커니즘. | `부분` — "F-1 은 external m 가정 하 open" 으로 scope-pin. 해결 아님. | `부분` — F=E-TS 의 entropy 항이 K>1 을 thermodynamically 정당화 가능. M-1 의 전제를 흔듦. | `악화` — X_t 동적화 → K-field 정의 자체가 shifting target. F-1 을 재정의할 새 언어 필요. | `완전` — K 가 integer 전제를 포기하면 K=2 라는 개념 자체가 soft distribution 의 한 모드로 축소. vacuity 소멸. |
| **OP-0002 (M-1, K=1 preference)** | `완전` — E 와 동일 메커니즘 (A ⊇ E 의 K-soft 작업). K 가 soft 되면 isoperimetric ordering 은 distribution 수준 비교로 재작성. | `부분` — "isoperimetric 은 정리, K 선택은 external" 명시. | `부분` — entropy 항이 K>1 distribution 을 thermodynamically 선호할 수 있음. | `방치` — substrate 변화와 무관. M-1 은 고정 graph 위 isoperimetric 결과. | `완전` — soft-K 위에서 M-1 은 "single dominant mode" 로 재해석. 정리 내용은 유지되나 문제성 상실. |
| **OP-0003 (MO-1, Morse inapplicable)** | `완전` — soft-K 는 m₂=0 코너를 제거 (K 가 연속). smooth Morse 복원. | `방치` — scope note 만 추가. 기술적 문제 그대로. | `부분` — C 의 thermal framework 는 smooth Morse 대신 Witten Laplacian · Fokker-Planck · Kramers 를 분석 도구로 사용 → 우회. MO-1 해결은 아니나 blocker 제거. | `부분` — Σ²_M 이 의미를 잃으므로 "MO-1 대상 자체 재정의 필요". | `완전` — §4.1 A 와 동일 — K 연속화가 코너 제거. |
| **OP-0004 (Type A/B classification)** | `부분` — A 의 K-soft 가 E 와 동일하게 "분류" 개념을 continuous classifier 로 대체 가능. | `부분` — retraction 을 CN 으로 공식 인정. | `방치` — thermal 과 무관. | `방치` — substrate 와 무관. | `부분` — soft-K 위에서 "분류" 개념 자체를 continuous classifier 로 대체 가능성 (reframing §9). |
| **OP-0005 (K selection mechanism)** | `완전` — K 가 emergent / gradable 이 되면 selection 은 자동 — "선택" 대신 "읽기". | `부분` — "K 는 external assumption" 명시. 메커니즘 부재 honesty. | `완전` — Free energy F 의 최소화가 K-valued distribution 을 선택. BIC 식. | `부분` — K 는 substrate 구조에서 emerge 가능. 메커니즘이 self-generating 에 위임. | `완전` — E 의 정의. K 자체가 derived 이면 selection 은 존재하지 않는 질문. |
| **OP-0006 (Boundary definition precision)** | `부분` — threshold 를 parametric family 로 승급. precision 개선. | `부분` — "θ 들은 free parameter" 명시. 정밀도 개선 없음. | `방치` — boundary 는 spatial, thermal 과 무관. | `부분` — boundary 가 u→N derived 에 의해 재정의됨. 정밀도는 유도 메커니즘에 의존. | `부분` — soft-K 가 H_0 persistence 기반이면 일부 threshold 제거. 전체 해결 아님. |
| **OP-0007 (Dynamic topology)** | `방치` — X_t 고정 유지. | `방치` — out of scope 명시 유지. | `방치` — thermal 과 무관. | `완전` — D 의 정의 중 X_t 도 u 에서 유도되면 dynamic topology 는 자연 포함. | `방치` — K 재정의는 topology 와 orthogonal. |
| **P-A (Integer-K / Continuous-u Mismatch)** | `완전` — A 가 mismatch 전체 (K·threshold·axiom) 를 대상. | `부분` — mismatch 를 N-1 honesty note 로 pin. | `방치` — thermal 은 K 의 층위 문제에 영향 없음. | `방치` — substrate 와 orthogonal. | `완전` — E 의 핵심 — K 를 u 와 같은 층위에서 정의. |
| **P-B (External substrate)** | `방치` — A 는 N-1 축에 집중. substrate 의 pre-theoretic 지위는 건드리지 않음. | `부분` — CN 으로 공식 commitment 로 승급. 해결 아님. | `방치` — thermal 은 substrate 층위와 무관. | `완전` — D 의 정의. | `방치` — K 재정의는 substrate 와 orthogonal. |
| **P-C (Missing third mode — C_t demotion)** | `방치` — A 의 declared scope 는 K + threshold + axiom-switching (reformulation_plan §Stage 0 A). Co-belonging demotion 은 별개의 ontology 문제로 A scope 외. | `부분` — "dual-mode 선택은 수학적 편의" 로 commitment pin. | `부분` — entropy 항이 "self-integration" 의 수학적 대체재가 될 잠재력 (C_t 의 대안). | `방치` — substrate 층위, third mode 와 무관. | `방치` — K 에 집중. C_t 와 무관. |
| **P-D (Threshold non-principled)** | `부분` — threshold 도 N-1 의 한 얼굴이므로 축소 · 제거 시도. | `부분` — threshold 는 free parameter 명시. | `방치` — thermal 은 threshold 선택과 무관. | `부분` — boundary 는 u→N derived 에 귀속될 수 있음. | `부분` — H_0 persistence 기반 K_soft 가 일부 threshold 제거 (그러나 Core/Interior 임계는 잔존). |
| **P-E (Parameter genealogy)** | `부분` — A 의 K-soft 가 E 와 동일하게 K 관련 파라미터 제거 + threshold family 명시로 일부 보조 파라미터도 다룸. 25+ 파라미터 중 일부만. | `부분` — "파라미터 origin 미결" honesty note. | `부분` — T 도 새 파라미터. 단, thermodynamic analysis 는 **일부** 파라미터를 derived 로 만듬 (엔트로피 constant 등). | `부분` — 일부 파라미터가 substrate 동역학에서 emerge 가능. | `부분` — K 관련 파라미터 (K 자체 + K-repulsion λ_rep) 자동 제거. 나머지 20+ 파라미터 잔존. |
| **P-F (Zero-T metastability claim)** | `부분` — A 의 K-soft 가 E 와 동일하게 "무엇이 metastable 인가" 의 대상을 재정의. thermal framework 공백은 그대로 남음. | `부분` — "metastability 는 zero-T local min 언어로 downgrade" CN. | `완전` — C 의 정의. Kramers rate · exp(ΔE/kT) · FDT 가 framework 에 편입. | `방치` — substrate 변화와 metastability 는 orthogonal. | `부분` — soft-K distribution 의 metastability 해석은 여전히 thermal framework 부재 — P-F 의 본질은 남음. E 가 "무엇이 metastable 인가" 의 대상을 재정의하나 framework 공백은 그대로. |
| **P-G (Axiom / implementation divorce)** | `부분` — A1'/b_D=0/E3 reclassification 의 이중표시 를 N-1 의 "공리 얼굴" 로 간주하고 재검토. | `부분` — 각 divorce 지점을 공식 CN 으로 승급. | `방치` — 새 thermal 공리를 추가할 뿐, 기존 divorce 미건드림. | `방치` — substrate 변화는 Group B 에 집중, Group A/D/E 의 divorce 와 무관. | `부분` — K-관련 공리 (A1', E3 reclassification 중 K-field 부분) 재작성. A/D-group divorce 는 잔존. |
| **P-H (Time T pre-theoretic)** | `방치` — A 는 space 축 (K/threshold/axiom), time 축 미건드림. | `부분` — "T 는 주어진 pre-theoretic 순서" CN 승급. | `부분` — thermal 이 dynamic 이므로 T 의 역할 (evolution parameter) 이 명시됨. | `부분` — substrate 에 T 포함 시 time 도 self-generating. 다만 D 의 primary scope 는 X_t/N_t. | `방치` — K 재정의는 time 축과 orthogonal. |
| **N-1 (Soft-Hard Switching Asymmetry, unified)** | `부분` — N-1 의 세 얼굴 (K/threshold/axiom) 모두 대상. 완전해결은 작업 완료 후. | `부분` — N-1 honesty note 로 승급. 해결 아님. | `부분` — N-1 의 hard 측 (정수 K, zero-T 결정론 의 "decision") 에 thermodynamic 정당화 부여. soft 측 불변. | `방치` — D 는 N-1 과 orthogonal (substrate 축). | `부분` — N-1 의 K 얼굴만 정면. threshold · axiom 얼굴은 out-of-scope. |

### 4.2 후보별 집계 (2026-04-20 final audit after A-E consistency fix)

| | 완전 | 부분 | 방치 | 악화 | 생성 | 합 |
|---|---|---|---|---|---|---|
| **A** | 5 (OP-0001 F-1, OP-0002 M-1, OP-0003 MO-1, OP-0005, P-A) | 7 | 4 | 0 | 0 | 16 |
| **B** | 0 | 14 | 2 (OP-0003, OP-0007) | 0 | 0 | 16 |
| **C** | 2 (OP-0005, P-F) | 7 | 7 | 0 | 0 | 16 |
| **D** | 2 (OP-0007, P-B) | 6 | 7 | 1 (OP-0001) | 0 | 16 |
| **E** | 5 (OP-0001, OP-0002, OP-0003, OP-0005, P-A) | 7 | 4 | 0 | 0 | 16 |

**읽기:** "완전해결" 수가 가장 많은 단일 후보는 **A 와 E 둘 다 5개** — 2026-04-20 audit 에서 A 의 K-soft 작업이 E 와 동일 메커니즘임을 반영하여 OP-0001/0002/0004/P-E/P-F 에서 A 를 E 와 일치시킨 결과. **B** 는 완전해결 0개이되 "부분" 이 14 rows 로 coverage 폭 최대. **D** 는 OP-0007 (dynamic topology) 을 유일하게 정면 해결.

**A 와 E 의 구분은 Matrix-1 5-level 코딩 resolution 에서는 drop out 됨.** 실질 차이는:
- A 는 threshold (P-D, OP-0006) · axiom (P-G) 까지 **같은 '부분' code 내에서 더 깊이** 대응.
- E 는 K 만 다루고 threshold · axiom 은 surface-level 부분만.
- 차이는 **세션 수 (A 18 vs E 12) · qualitative depth** 에 드러남.

**주의:** 코딩은 단순화된 5값 분류. "완전" 이 같은 방식의 해결을 의미하지 않음 — E 의 완전해결은 "문제 소멸" (reframing), C 의 완전해결은 "메커니즘 도입" (positive). 이 차이는 Matrix-2 로 비용 측면에서 보완.

### 4.3 조합 후보의 집계 (주요 3)

조합은 단일 후보의 OR 결합으로 근사 (각 cell 은 더 강한 결과를 택함: 완전 > 부분 > 방치 > 악화).

| 조합 | 완전 | 부분 | 방치 | 악화 | 해석 |
|---|---|---|---|---|---|
| **C+E** | 6 (OP-0001, OP-0002, OP-0003, OP-0005, P-A, P-F) | 8 | 2 (OP-0007, P-B) | 0 | Coverage 최대. OP-0007 과 P-B 만 방치. |
| **B+C** | 2 (OP-0005, P-F) | 13 | 1 (OP-0007) | 0 | 정직함 + thermal 정당화. 완전해결은 C 기여분만. |
| **A+C** | 6 (OP-0001, OP-0002, OP-0003, OP-0005, P-A, P-F) | 8 | 2 (OP-0007, P-B) | 0 | A-E consistency fix 후 A+C 와 C+E 는 Matrix-1 에서 동일 coverage. 차이는 session 수 (21 vs 17). |

---

## §5. Matrix-2 — Theorem Survival × Purpose

**행 (49):** Cat A 35 + Cat B 4 + Cat C 5 + Retracted 5 (canonical §13 per `theorem_status.md` 집계).
**열 (5):** A, B, C, D, E.
**셀 code:** `생존` (Survive, 무변화), `재증명` (Re-prove, 진술 유지·증명 재작성), `강등` (Downgrade, 카테고리 하향 A→B/B→C), `폐기` (Retire), `미지` (Unknown).
**각 cell:** code 만 (정당화는 표 아래 각주에 묶음 — 49×5 의 cell-level 주석은 과부하).

Retracted 5 개는 이미 폐기이므로 모든 열에 `-` (해당 없음).

**각 후보 열의 끝:** "Category A 상실 수" = {폐기 + 강등 (A→B 이상) + 재증명으로 Cat A 에서 밀려난 것}. 이것이 보수적 **비용 지표**.

### 5.1 행 정의 (49 claims)

**Category A (35):**
- T1 (Energy Minimizer Existence), T3/T6-Stability, T6a, T6b, T7-Enhanced, T8-Core, T8-Full, T11 (Γ-Conv), T14 (Grad Flow), T20 (Axiom Consistency), T-A2 (Monotonicity), C-Axioms (C1-C4 satisfaction), QM1, QM2, QM3, QM4, Predicate-Energy Bridge, Deep Core Dominance 2b, T-Merge (a), T-Merge (b), Topological Lock, T-Birth-Parametric (D₄), T-Bind-Proj, T-Bind-Full, Proposition 1.1 (Constraint Manifold), Proposition 1.2 (Fiber Dimension), Theorem 3.1(a), Theorem 3.1(b), Theorem 3.1(d), Persistence Threshold Equation, T-Persist-1(a), T-Persist-1(b), T-Persist-1(c), T-Persist-1(e), Coupling Bound Lemma.

**Category B (4):** Barrier Exponent γ_eff≈0.89, T-Birth-Parametric (general non-D₄), T-d_min-Formula, T-Beyond-Weyl.

**Category C (5):** T-Persist-1(d), T-Persist-Full, T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified.

**Retracted (5):** R1 (Theorem 3.3 general τ), R2 (T-Merge (c)), R3 (T-Merge (d)), R4 (T-Merge (e)), R5 (K-Saddle Conjecture).

### 5.2 The Matrix

| # | Claim | A | B | C | D | E |
|---|---|---|---|---|---|---|
| A1 | T1 | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A2 | T3/T6-Stability | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A3 | T6a | 생존 | 생존 | 생존 | 재증명 | 생존 |
| A4 | T6b | 생존 | 생존 | 생존 | 재증명 | 생존 |
| A5 | T7-Enhanced | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| A6 | T8-Core | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A7 | T8-Full | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A8 | T11 (Γ-Conv) | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A9 | T14 (Grad Flow) | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A10 | T20 (Axiom Consistency) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| A11 | T-A2 | 생존 | 생존 | 생존 | 재증명 | 생존 |
| A12 | C-Axioms (C1-C4) | 생존 | 생존 | 생존 | 재증명 | 생존 |
| A13 | QM1 | 재증명 | 생존 | 생존 | 생존 | 재증명 |
| A14 | QM2 | 재증명 | 생존 | 생존 | 생존 | 재증명 |
| A15 | QM3 | 생존 | 생존 | 생존 | 생존 | 생존 |
| A16 | QM4 | 재증명 | 생존 | 생존 | 생존 | 재증명 |
| A17 | Predicate-Energy Bridge | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A18 | Deep Core Dominance 2b | 생존 | 생존 | 생존 | 재증명 | 생존 |
| A19 | T-Merge (a) | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| A20 | T-Merge (b) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| A21 | Topological Lock | 폐기 | 생존 | 생존 | 재증명 | 폐기 |
| A22 | T-Birth-Parametric (D₄) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| A23 | T-Bind-Proj | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A24 | T-Bind-Full | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A25 | Proposition 1.1 (Constraint Manifold) | 재증명 | 생존 | 생존 | 생존 | 재증명 |
| A26 | Proposition 1.2 (Fiber Dimension) | 폐기 | 생존 | 생존 | 생존 | 폐기 |
| A27 | Theorem 3.1(a) | 재증명 | 생존 | 생존 | 생존 | 재증명 |
| A28 | Theorem 3.1(b) | 미지* | 생존 | 생존 | 미지* | 미지* |
| A29 | Theorem 3.1(d) | 폐기 | 생존 | 생존 | 생존 | 폐기 |
| A30 | Persistence Threshold Equation | 재증명 | 생존 | 재증명 | 재증명 | 생존 |
| A31 | T-Persist-1(a) | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A32 | T-Persist-1(b) | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A33 | T-Persist-1(c) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| A34 | T-Persist-1(e) | 생존 | 생존 | 재증명 | 재증명 | 생존 |
| A35 | Coupling Bound Lemma | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| B1 | Barrier Exponent γ_eff | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| B2 | T-Birth-Parametric (non-D₄) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| B3 | T-d_min-Formula | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| B4 | T-Beyond-Weyl | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| C1 | T-Persist-1(d) | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| C2 | T-Persist-Full | 재증명 | 생존 | 재증명 | 재증명 | 재증명 |
| C3 | T-Persist-K-Sep | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| C4 | T-Persist-K-Weak | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| C5 | T-Persist-K-Unified | 폐기 | 생존 | 재증명 | 재증명 | 폐기 |
| R1–R5 | Retracted (5) | — | — | — | — | — |

### 5.3 각 후보 열 집계 (2026-04-20 final audit: 전체 cell 재계산)

Category A 상실 = {폐기 Cat A} + {강등 A→B/C}; 미지 는 상실 range 의 upper end 에 포함. Cat B/C 폐기는 별도 집계 (Cat A 상실 계 에는 포함 안 됨).

**Cat A rows (35):**

| 후보 | 폐기 | 재증명 | 생존 | 미지 | 합 | **Cat A 상실 계** |
|---|---|---|---|---|---|---|
| **A** | 5 (T-Merge a, Topological Lock, Prop 1.2, Thm 3.1(d), Coupling Bound Lemma) | 11 | 18 | 1 (Thm 3.1(b)) | 35 | **5~6** |
| **B** | 0 | 0 | 35 | 0 | 35 | **0** |
| **C** | 0 | 20 | 15 | 0 | 35 | **0** (모든 Cat A 재증명으로 생존 — thermal limit 회수) |
| **D** | 0 | 26 | 8 | 1 (Thm 3.1(b)) | 35 | **0~1** (T11 / D 재증명 반영) |
| **E** | 5 (T-Merge a, Topological Lock, Prop 1.2, Thm 3.1(d), Coupling Bound Lemma) | 10 | 19 | 1 (Thm 3.1(b)) | 35 | **5~6** |

**Cat B rows (4):**

| 후보 | 폐기 | 재증명 | 생존 | 합 |
|---|---|---|---|---|
| **A** | 3 (B1 γ_eff, B3 d_min, B4 Beyond-Weyl) | 1 (B2) | 0 | 4 |
| **B** | 0 | 0 | 4 | 4 |
| **C** | 0 | 4 | 0 | 4 |
| **D** | 0 | 4 | 0 | 4 |
| **E** | 3 (B1, B3, B4) | 1 (B2) | 0 | 4 |

**Cat C rows (5):**

| 후보 | 폐기 | 재증명 | 합 |
|---|---|---|---|
| **A** | 3 (C3 T-Persist-K-Sep, C4 K-Weak, C5 K-Unified) | 2 (C1 T-Persist-1(d), C2 T-Persist-Full) | 5 |
| **B** | 0 | 0 | 5 (all 생존) |
| **C** | 0 | 5 | 5 |
| **D** | 0 | 5 | 5 |
| **E** | 3 | 2 | 5 |

**Retracted (5):** 이미 폐기. 모든 후보에 해당 없음.

**A/E 동일 폐기 총계:** Cat A 5 + Cat B 3 + Cat C 3 = **11 폐기** (of 44 active claims).
**A/E 재증명 총계:** Cat A 11(A)/10(E) + Cat B 1 + Cat C 2 = **14(A) / 13(E) 재증명**.
**A/E 생존 총계:** Cat A 18(A)/19(E) = **18(A) / 19(E) 생존**.

(A 와 E 의 유일 Cat A 차이: A30 Persistence Threshold Equation 에서 A=재증명, E=생존 — A 가 threshold family 를 건드리므로.)

**주석 (D 의 "실질 불확실"):** D 의 26 Cat A 재증명은 **낙관적 추정**. 실제로는 B-group 공리 전면 재작성에서 많은 정리가 Unknown 이 될 수 있음 — 예: T8-Core 는 "finite connected graph with Fiedler eigenvalue λ_2 > 0" 을 가정하나 그래프 자체가 u 에서 유도되면 λ_2 는 시간가변 · 구성가변. 이 가변성 하에서의 phase transition 정리는 **미지** 가 정확한 코드일 수 있음. 보수적 coding 을 유지하되 이 fragility 는 risk 로 기록.

**Cat B/C 폐기 종합:**
- A: Cat A 폐기 5 + Cat B 폐기 3 (B1 γ_eff, B3 d_min, B4 Beyond-Weyl) + Cat C 폐기 3 (C3/C4/C5) = **총 11 폐기** (of 44 active claims).
- E: 동일 — **총 11 폐기**.
- A 와 E 의 폐기 리스트는 동일 (K-field 전면 재작성 공통).
- A vs E 의 유일한 Cat A 차이: A30 Persistence Threshold Equation (A=재증명 threshold family 로, E=생존 threshold 불변).

### 5.3.1 Honesty margin — Thm 3.1(b) 의 미지 표시 근거

Thm 3.1(b) 진술: "Intra-formation Hessian positive definite" on the K=2 constrained manifold $\Sigma_M^{\mathrm{relax}}$. "Intra-formation" 개념이 per-formation 언어를 전제. A / E / D 에서 per-formation 언어가 사라지면:

- **재증명 쪽 주장:** "intra-formation PD" 가 "단일 field 의 formation-preserving tangent subspace 에서의 PD" 로 일반화 가능 — 추상적 linear algebra 결과. 재증명 가능.
- **폐기 쪽 주장:** "intra" vs "transfer" distinction 이 본질적으로 K 개 필드 간 구분이므로 단일 필드에서는 무의미. 폐기.

두 주장의 결정은 해당 후보의 Stage 3 (Definition & Derivation) 까지 진행해야 확정. **현재는 미지 (Unknown)** 가 honest coding. Cat A 상실 계를 "5~6" 식 range 로 표시.

### 5.4 후보별 Cat A 상실의 지도

- **A · E 공통 Cat A 폐기 (5):** T-Merge (a) [K-formation local minimality], Topological Lock [K-field 구성], Prop 1.2 [Σ²_M 코너], Thm 3.1(d) [symmetric point on Σ²_M], Coupling Bound Lemma [K-field product manifold]. 모두 K-field 전제 정리.
  - T-Merge (b) 는 재증명 유지 (isoperimetric 은 K 와 무관).
- **B:** 0 폐기. 공리 불변.
- **C:** 0 폐기. Zero-T 극한으로 기존 정리 전부 회수 (재증명).
- **D:** 0 폐기 (낙관적 — T11 / D 반영 후 재증명 26, 생존 8, 미지 1). Group B 공리 재작성이 induce 하는 재증명 부담 최대 — 실질 Unknown 가능성.

---

## §6. Cross-reference — Matrix-1 × Matrix-2

매트릭스 간 상호함의 기록. 형식: "OP X 의 Y 해결 → 정리 Z 의 W 영향".

1. **P-A 완전해결 (E, A)** → T-Persist-K-Sep/Weak/Unified 폐기 (C3/C4/C5) + T-Merge (a) / Topological Lock / Prop 1.2 / Thm 3.1(d) / Coupling Bound Lemma 폐기; T-Merge (b) 는 isoperimetric 재증명.
2. **OP-0005 K selection 완전해결 (C)** → 기존 CN6 ("K 는 kinetically determined") 의 재작성. C 에서 K 는 thermodynamically selected 가 됨. CN6 는 **현 canonical 과 새 C-canonical 에서 다른 내용을 주장**.
3. **MO-1 완전해결 (A, E)** → Prop 1.2 (Fiber Dimension: 코너 singularity) 폐기. 코너가 소멸하면 fiber dimension 의 singular 분석 대상이 없음.
4. **P-F 완전해결 (C)** → CN6/CN8/CN14 의 metastability 언어 전면 재작성. 기존 zero-T 주장들은 T → 0 극한으로 재증명.
5. **P-B 완전해결 (D)** → B-group 공리 (B1-B4) 재작성. Group B 가 derived 되므로 B1-B4 는 정리가 되거나 폐기. T8-Core 의 "finite connected graph" 가정 재검토.
6. **B 의 모든 cell 이 "부분" 이하** ↔ Matrix-2 의 B 열이 전부 생존. **trade-off 의 교과서적 표현**: B 는 아무 것도 폐기하지 않는 대신 아무 것도 완전해결하지 않는다.
7. **D 가 유일 완전해결 OP-0007** ↔ D 의 Matrix-2 에서 대량 재증명 (Cat A 26). Dynamic topology 를 얻는 대신 거의 모든 정리가 "어떤 그래프에서" 질문을 새로 답해야 함.
8. **P-F 는 E 에서 부분 (완전 아님)** ↔ E 가 K-field 폐기에 성공해도 thermal framework 공백은 남음. → **C+E 조합이 두 방향 모두 완전해결** (Matrix-1 §4.3).

### 6.1 권고에 영향을 주는 핵심 크로스

**Cross #1.** E 가 단독으로 "완전해결 5 + Cat A 상실 5" — 1:1 ratio. 즉 **해결 1개당 평균 Cat A 1개 상실**. 비용-편익 이 명확.

**Cross #2.** C+E 조합은 "완전해결 6 + Cat A 상실 5~6" — 비용은 E 와 같은데 해결 1개 추가. 그러나 C 의 재증명 부담 20개 이 E 의 11 개와 일부 중복 제외하고 합쳐 **25~30 재증명** 이 됨 — 세션 수 대폭 증가 (02 §Z 기준 12 → 17 세션, +40%).

**Cross #3.** A-E consistency fix 후 A 와 E 는 Matrix-1/2 5-level aggregate 에서 동일 — 완전해결 5 · Cat A 상실 5~6 · 재증명 11(A) vs 10(E) · 생존 18(A) vs 19(E). 유일 structural 차이는 A30 (A=재증명 / E=생존). 따라서 E 는 A 를 **weak Pareto-dominate (세션 12 < 18)**. A 는 E 의 작업 + threshold/axiom 확장이되 coverage 는 coarse 매트릭스에서 같음.

이는 Q1 (A 와 E 의 관계) 답변에 직결 — `03_integration_and_new_open.md` §1 에서 상세.

**Cross #4.** B 는 `(0, 0)` Pareto-dominated 되는 것이 아니라 **Pareto 축과 orthogonal** — "진전 없이 정직함" 은 다른 축의 가치. fallback 으로서의 역할은 Q2 답변.

**Cross #5.** A+C 와 C+E 도 Matrix-1 aggregate 동일 (6, 8, 2) · Cat A 상실 동일 (5~6). 유일 차이는 세션 (A+C=21 vs C+E=17). C+E 가 A+C 를 **weakly Pareto-dominate** (세션 감소).

---

## §7. 이 파일의 출력 해석 지침 (사용자를 위한)

- Matrix-1 의 cell 은 **방향성 지표**. 실제 완전해결은 Stage 1~6 수행 후 확인.
- Matrix-2 의 Cat A 상실 수는 **보수적 lower bound**. 재증명 중 실질적 증명 실패가 나오면 상실 수는 증가.
- 조합 (C+E, B+C, A+C) 집계는 단일 후보의 OR 결합으로 **상호작용 무시** 한 근사치. 상호작용 분석은 `03_integration_and_new_open.md` §Q3.
- 본 세션은 **5 단일 + 3 조합 = 8 선택지** 밖의 후보를 창안하지 않음 (plan.md Non-goals 준수).
- Matrix 의 "완전해결" 이 "수학적 증명 완료" 를 뜻하지 않음. "문제 언어 소멸" 까지 포함하는 broader interpretation. 후속 검증시 각 cell 의 정당화 문장을 재독.

**Next file:** `02_development.md` — 각 후보의 첫 3 세션 구체 스케치 (5 × 3 = 15).
