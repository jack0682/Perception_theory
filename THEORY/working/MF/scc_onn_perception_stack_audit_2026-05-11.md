---
id: NOTE-STACK-002
type: working/audit
status: read-only audit; conceptual note; NOT a theorem; NOT a canonical claim
created: 2026-05-11
parent: THEORY/working/MF/scc_relation_onn_ortsf_perception_stack.md
related:
  - THEORY/logs/daily/2026-05-06/99_summary.md  (§A3)
  - THEORY/logs/daily/2026-05-07/01_pre_brainstorm.md  (§3)
  - THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md
  - THEORY/working/INDEX.md
scope: SCC ↔ ONN 연결 — 저장소 내 모든 근거 정리; "SCC / Perception theory / ONN 삼단" 사용자 그루핑에 대한 매핑.
authority: read-only at audit-time HEAD; quotes existing files verbatim
---

# SCC ↔ ONN 연결 — 저장소 내 모든 근거 정리

> **작업 모드.** 읽기 전용. canonical / hypothesis_tree / theorem_status / CHANGELOG / 기존 working source 어떤 파일도 수정하지 않았다. claim 승격/강등 수행하지 않았다. 본 파일은 `scc_relation_onn_ortsf_perception_stack.md`(NOTE-STACK-001, 2026-05-06 EOD stub)의 후속 audit note이며, contamination barrier 안쪽(working layer)에만 존재한다.
>
> **목적.** "SCC / Perception theory / ONN 삼단"이라는 사용자 그루핑에 대해 저장소의 명시적 표현을 점검하고, 4단 pipeline (SCC → RelationWorld → ONN → ORTSF) 안에서 어떻게 떨어지는지 매핑한다.

---

## 0. 한 줄 요약

저장소가 명시한 perceptual pipeline은 **4단**이고, **ONN은 그 안의 의미(ontology) 층**이다. SCC는 그 4단의 **시작점(primitive layer)**이고, ONN은 두 단계 떨어져 있다. 두 단계 사이를 잇는 것이 **RelationWorld**(관계 문법), ONN 뒤를 받는 것이 **ORTSF**(행동/제어).

```
SCC (cohesion-first field)
  ↓ formations: PersComp(u_t), K_act, σ(C_i)
RelationWorld (relation/world grammar over SCC formations)
  ↓ world-state: relational structure between formations
ONN (ontological/semantic placement)
  ↓ ontological commitments: category assignment, constraint satisfaction
ORTSF (action, attention, memory, delay-robust control)
  ↓ action commands, memory updates, attention allocation
```
— `THEORY/working/MF/scc_relation_onn_ortsf_perception_stack.md:17–26` (NOTE-STACK-001, status: **stub, conceptual note only, NOT a theorem, NOT a canonical claim**)

> "Perceptual generation order: cohesion → relation → meaning → action." (같은 파일 line 28)

---

## 1. 일차 자료 (어디에 적혀 있는가)

| 출처 | 파일 | 줄 | 역할 |
|---|---|---|---|
| 핵심 stub | `THEORY/working/MF/scc_relation_onn_ortsf_perception_stack.md` | 9–96 | **유일하게 4단을 명문화한 working note**. id `NOTE-STACK-001`, type `conceptual-note`, status `stub`. |
| Daily EOD | `THEORY/logs/daily/2026-05-06/99_summary.md` | §A3 line 215–230 | "Current Architecture State" 블록 — 동일 4단 다이어그램. |
| Pre-brainstorm | `THEORY/logs/daily/2026-05-07/01_pre_brainstorm.md` | §3 line 77–108 | "Perception Stack — Open Questions" — 각 층을 한 단락씩. |
| Weekly draft | `THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md` | line 32–40 | "Perception stack clarified" — 한 줄 다이어그램 + stub 위치 인용. |
| Index | `THEORY/working/INDEX.md` | 219 | working file 카탈로그 — "SCC/ONN/ORTSF stack". |
| Day plan | `THEORY/logs/daily/2026-05-07/00_plan.md` | 73 | 전날 closeout에서 "SCC → RelationWorld → ONN → ORTSF pipeline documented with inter-layer formal links." |

→ ONN이 **본문 정리 차원으로 등장한 곳은 위 6개로 한정**됨. canonical / hypothesis_tree / theorem_status / CHANGELOG에는 **ONN이 등장하지 않음**. 즉 **현재 canonical theory 안에 ONN의 정식 자리는 없고, working layer의 conceptual note 한 장으로만 존재**한다.

---

## 2. 각 층의 역할 (저장소 표현 그대로)

### 2.1 SCC — Soft Cognitive Cohesion
(`scc_relation_onn_ortsf_perception_stack.md:34–39`)
- **Primitive**: soft cohesion field $u_t : X_t \to [0,1]$.
- **Output**: formations — cohesion regions detected **before** discrete objecthood.
- **Key theorems in play**: T8 (minimizer existence), T-OP6-B (boundary precision), T-K-Select-PF/OBS (K-selection), T-Temporal-Identity (inter-frame correspondence), T-σ-Inherit (signature inheritance).
- **Ontological stance**: formations are pre-objective. Crisp objects (discrete, labeled) are derivative and emerge only **after RelationWorld assignment**.

→ 이것이 현재 저장소(`Perception_theory`)의 거의 모든 정리·증명이 속하는 층 (CV-1.13 기준 83 claims).

### 2.2 RelationWorld — Relation/World Grammar
(같은 파일 41–45)
- **Input**: SCC formations (graph-structured cohesion regions with σ-signatures).
- **Role**: assigns discrete relational structure between formations (closure, distinction, co-belonging in the relational sense). Produces a "world-state" as a relational configuration.
- **Ontological breadth 메모**: RelationWorld theory **may be stated for any relational primitive** — it is not inherently restricted to SCC-derived formations. **However, in the perceptual generation pipeline, SCC is the entry point and RelationWorld receives SCC output.**

→ 이 층은 별도 연구 프로젝트로 표기됨: "RelationWorld theory is a separate research project (see `theory/` directory in the parent repo)" — line 89.

### 2.3 ONN — Ontology Neural Networks
(같은 파일 47–51)
- **Full name**: **Ontology Neural Networks** (저장소가 공식적으로 풀어 쓴 유일한 약어 — line 47).
- **Input**: RelationWorld relational world-state.
- **Role**: **constraint-based fixed-point solver**. Maps relational structure to **ontological categories** (semantic placement).
- **Output**: ontological commitments — which formations are instances of which categories, under which relational constraints.

→ 별도 프로젝트로 표기됨: "ONN and ORTSF are separate projects (see `ONN/` directory)" — line 90. 본 저장소(`Perception_theory`) 안에는 ONN의 수학적 정의는 없고, **외부 디렉토리에 별도 코드/이론이 있다는 참조만** 존재.

### 2.4 ORTSF — Ontology-based Robust Topological Sequencing Framework
(같은 파일 53–57)
- **Full name**: **Ontology-based Robust Topological Sequencing Framework** (line 53).
- **Input**: ONN outputs + temporal identity (T-Temporal-Identity correspondence $R_{t\to s}$) + σ-signatures.
- **Role**: delay-robust control stabilization, attention allocation, memory formation, action command generation.
- **Output**: action commands, updated attention, memory trace.

---

## 3. "삼단" 해석 — 어디서 어떻게 떨어지는가

사용자가 표현한 **SCC / Perception theory / ONN** 의 3단을 저장소 근거로 매핑하면:

| 사용자의 3단 | 저장소 4단 매핑 | 근거 |
|---|---|---|
| **SCC** | SCC (L1) | 저장소의 일차 작업 단위; CV-1.13까지의 모든 캐논 정리 (`canonical.md` §13). |
| **Perception theory** | **RelationWorld + ORTSF** (L2 + L4) — 즉 SCC와 ONN을 둘러싸는 "지각 이론" 우산. 동시에 저장소 이름이 `Perception_theory`라는 의미 중의성도 있다. | stub line 89 "RelationWorld theory is a separate research project"; 저장소 root `/Perception_theory/` 그 자체가 우산. |
| **ONN** | ONN (L3) | `scc_relation_onn_ortsf_perception_stack.md` §2.3; line 90 "see `ONN/` directory" — 별도 프로젝트. |

또 다른 가능한 해석: 사용자가 "Perception theory"를 **저장소 전체 = 4단 전체의 이름**으로 쓴 것이라면, "SCC ⊂ Perception theory → ONN"이라는 구조가 된다. 즉 SCC가 Perception theory 안의 진입점이고, Perception theory가 끝나는 곳에 ONN이 받는다.

**어느 해석이든 핵심 사실은 동일하다.** SCC ↔ ONN 사이에는 **반드시 RelationWorld라는 중간 번역 층이 존재**한다고 저장소가 명시한다. 직접 결합이 아니다. 이 점은 stub과 pre-brainstorm 양쪽에 모두 기록되어 있다(아래 §4).

---

## 4. 층간 형식 연결 (현재 미해결로 표시된 부분)

`scc_relation_onn_ortsf_perception_stack.md` §4 (line 73–82) + `2026-05-07/01_pre_brainstorm.md` §3.5 (line 104–108)에 **inter-layer formal links의 open question 4개**가 명시되어 있다:

1. **SCC → RelationWorld boundary.** SCC formation boundaries (T-OP6-B: $d_H \le 2(\alpha/\beta)^{1/2}$) 가 RelationWorld node boundaries로 어떻게 매핑되는가? **공식 translation 존재 여부 미정.**
2. **RelationWorld → ONN.** RelationWorld가 만든 relational grammar가 이미 ONN의 constraint form에 있는가, 아니면 **번역 단계가 추가로 필요한가?**
3. **Temporal identity → ORTSF memory.** T-Temporal-Identity ($R_{t\to s}$ correspondence)가 ORTSF memory formation으로 어떻게 들어가는가? σ-inheritance (T-σ-Inherit)가 semantic continuity signal인가?
4. **K-selection as attention.** T-K-Select-OBS (posterior $K^*$ given observation $O_t$)가 attentional selection의 한 형태인가? $K^* = \arg\min F_{\mathrm{obs}}(K)$ 가 perceptually-preferred object count를 고르는가?

→ 모두 **현재 OPEN**. 그러나 (3),(4)는 **SCC 측 출력(T-Temporal-Identity, T-K-Select-OBS)이 이미 캐논 Cat B 이상**이라 ONN/ORTSF 측만 정의되면 곧바로 연결 가능한 상태다(canonical CV-1.11/CV-1.13 기준).

---

## 5. SCC가 ONN을 "필연적으로 요구"한다는 명제의 저장소 근거

"이건 반드시 ONN에 연결돼"라는 입장을 저장소 문장으로 뒷받침하는 근거:

1. **CN10 contrastive lock (canonical §11.1 Commitment 16, line 914).** "The SCC ontological flow is **one-way**: $u_t$ (primitive) → ($K_{\mathrm{field}}$ modeling commit, $K_{\mathrm{act}}(t)$ dynamic diagnostic) → **cog-sci comparisons**." 즉 SCC는 본질적으로 "downstream에서 인지·존재론과 비교될 운명"을 자기 안에 명시.
2. **§11.1 Commitment 3 (non-primitive status of crisp objects, line 866).** "Crisp objects may be recovered from the soft system by thresholding or stabilization, but they are **derivative** constructs, not foundational primitives." → 즉 SCC가 만든 formation을 "객체화 = 의미 부여"하는 단계가 **이론 내부에서 정의되지 않으며, 외부 층(ONN 등)으로 넘긴다**는 commitment.
3. **§10 Structural Interpretation (canonical line 850).** "The theory does not reduce to segmentation, clustering, or tracking… **this theory seeks to explain how anything becomes delineable at all**." → SCC는 "무엇이 객체가 되는가"의 *전 단계*이며, "그 객체가 무엇인가(category, ontology)"는 ONN의 몫.
4. **Stub의 perceptual generation order (`scc_relation_onn_ortsf_perception_stack.md:28`).** "Perceptual generation order: cohesion → relation → **meaning** → action." → meaning = ONN. SCC만으로는 의미가 발생하지 않으며, 의미는 **ONN 층에서 비로소 발생**한다고 stub이 정의한다.
5. **σ-inheritance / temporal identity의 downstream consumer**. `01_pre_brainstorm.md:108` "How does the σ-inheritance (T-σ-Inherit) map to ORTSF memory formation?" → σ-signature가 ONN을 통과해 ORTSF에서 memory로 굳어진다는 그림이 명시.

→ 종합: **저장소는 SCC가 단독으로 완성되지 않으며 의미층(ONN)으로 이어져야 perceptual pipeline이 닫힌다고 본다.** 단 그 이음은 *현재 working level의 stub 한 장*에만 적혀 있고, 캐논 안에는 들어와 있지 않다.

---

## 6. 캐논화되지 않은 이유 (status 진단)

`scc_relation_onn_ortsf_perception_stack.md:85–92` 명문 caveat:

> - This document is a **conceptual note, not a theorem**.
> - No formal proofs are made here.
> - RelationWorld theory is a separate research project.
> - ONN and ORTSF are separate projects.
> - The pipeline description is the author's current working model and may evolve.
> - This document does **NOT promote T-MF-Synthesis** or any working candidate.

**캐논화의 전제조건** (저장소가 자체적으로 열거한 것 — 같은 파일 §4 + `99_summary.md` A3):
- T-Temporal-Identity 캐논 Cat A — **달성됨 CV-1.13 (2026-05-10)** ✓
- T-σ-Inherit 캐논 Cat B — **부분 (a,b,d-dir,e)만 Cat B working**, MERGE/SPLIT은 W9+ deferred (OP-0008).
- T-MF-Synthesis (multi-formation 통합 정리) — future candidate, blocked by σ_standard.

→ 즉 **SCC 쪽의 인접 정리 두 개(Temporal-Identity, σ-Inherit)가 완전히 닫히면 stub을 정식 working theorem(T-MF-Synthesis 후보)으로 승격할 수 있는 상태**이며, 이는 hypothesis_tree HT-3.5의 **Q5/Q6** 경로와 정확히 일치한다.

---

## 7. 평생연구 관점에서의 위치 (저장소가 함의하는 로드맵)

저장소 자체의 표현으로 정리:

| 단계 | 현재 상태 | 다음 게이트 |
|---|---|---|
| **SCC** 내부 닫기 | CV-1.13 sealed, 83 claims (~71% fully proved); H-MORSE / Package II / T_* registration이 Phase 2 OPEN | H-MORSE-Local Cat B (CV-1.14 권장안, `CV114/09`) |
| **SCC → RelationWorld** 형식화 | OPEN; question 1 in §4 of stub | T-OP6-B boundary → RelationWorld node boundary translation |
| **RelationWorld → ONN** | OPEN; question 2 in §4 of stub | relational grammar의 constraint form 정합성 |
| **ONN → ORTSF** | working level, ORTSF input spec만 명시 | OP-0011/0012 (temporal composition consistency)에 의존 |

→ "SCC가 평생 연구"라는 입장과 저장소의 기록은 정확히 정합한다. 저장소가 명문화한 perceptual pipeline에서 **SCC는 출발 primitive (그리고 가장 수학적 부담이 큰 부분)** 이며, ONN은 두 단계 떨어진 의미층이고, 그 사이는 **RelationWorld라는 별도 프로젝트가 매개**한다. **SCC가 캐논으로 닫힐수록 ONN으로의 합류 경로가 자동으로 더 좁아진다** — 이것이 stub이 함의하는 구조다.

---

## 부록 A. 검색 grep 명세 (재현 가능)

| 키워드 | 결과 |
|---|---|
| `grep -rwn "ONN"` (word boundary) | 위 §1 표의 6개 파일에만 hit. canonical/CHANGELOG/hypothesis_tree에는 0건. |
| `grep -rn "RelationWorld"` | 동일 파일 군 + 일부 weekly draft. |
| `grep -rn "ORTSF"` | 동일 파일 군. |
| `grep -rn "삼단\|3단\|triad\|three-tier\|3-tier"` | 4단 perception stack에 직접 매칭되는 항은 **없음**. "삼단" 표현은 readout map(3단계 $P_{\min}/P_{\mathrm{top}}/P_{\mathrm{full}}$, OMS), 3-tier persistence ladder(near-bifurcation), Cor 2.2 3-tier status 등 별개 맥락에서만 등장. → "삼단"은 저장소의 명시적 표현이 아니라 SCC/Perception theory/ONN 그루핑에 대한 외부 표현으로 보임. |

---

## 부록 B. 후속 작업 후보 (제안일 뿐, 본 audit이 결정하지 않음)

본 audit이 직접 수행하지 않은, 그러나 자연스럽게 이어지는 후보 작업들:

1. **NOTE-STACK-001 stub의 inter-layer formal links §4 (question 1–4)** 각각에 대한 sub-working-file 분리. 특히 question 2 (RelationWorld → ONN translation step)는 ONN 측 외부 디렉토리 정의가 필요해 본 저장소 단독으로 닫을 수 없음.
2. **CV114 H-MORSE 작업이 Path B로 닫혀** Package II 진입 + H-T* registration이 진척되면, T-K-Select-OBS의 "attention" 해석(question 4)이 ORTSF input으로 옮겨갈 형식적 가능성이 열림.
3. **T-σ-Inherit MERGE/SPLIT (OP-0008, W9+)** 닫히면 σ-signature가 ONN ontological category에 어떻게 사상되는지의 첫 형식 진술이 가능 (현재 stub은 σ-signature를 RelationWorld의 입력으로만 사용).
4. **T-MF-Synthesis future candidate** — 저장소가 이미 13-phase formation life-cycle을 정의해 둠 (`99_summary.md` line 201). 이 정리가 stub을 working theorem으로 격상하는 가장 직접적 경로.

이상 후보는 *제안*이며, 본 audit note는 어떤 후속 작업도 결정하거나 승격하지 않는다.

---

**감사 종료 메모.** 본 working note는 read-only audit의 산출물이다. canonical / hypothesis_tree / theorem_status / CHANGELOG / 기존 working source 어떤 파일도 수정하지 않았으며, claim 승격/강등을 수행하지 않았다. `NOTE-STACK-001` stub의 후속 audit note (`NOTE-STACK-002`)로 격납되어 contamination barrier를 준수한다. 본 보고서의 모든 진술은 인용된 파일과 줄 번호로 추적 가능하다.
