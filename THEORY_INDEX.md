---
type: MOC
cluster: top-level
id: MOC_00_THEORY_INDEX
last_updated: 2026-05-21
description: Soft Cognitive Cohesion (SCC) 이론 저장소의 최상위 진입 인덱스. 2026-05-21 PAI pivot 이후 substrate (SCC) + 새 main axis (PAI) 두 layer 가 공존.
---

# THEORY_INDEX — SCC Substrate + Perception-Action Interpretation (PAI)

> [!nav] Theory Navigation
> Parent: (root)
> Authority: [[DECLARATION]] · [[canonical]] · [[00_manifest]]
> PAI direction: [[canonical/perception_action_interpretation_pivot_2026_05_21|PAI Pivot Doc]] · [[canonical/PAI_ROADMAP|Roadmap]]
> Status: Active (CV-1.20 substrate / HT-3.12 / 2026-05-21 PAI direction)

## 2026-05-21 Canonical Pivot

본 저장소는 두 layer 가 공존합니다.

**Substrate layer** (변경 없음): SCC = soft cohesion field $u_t : X_t \to [0,1]$ 의 phase-field morphology 이론. CV-1.20 SEALED, 102 claims (71A/20B/6C/5R), DECL-1.0 thesis "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?" 모두 **SUBSTRATE-CANONICAL** 로 보존.

**Main research axis** (2026-05-21 등록): **Perception-Action Interpretation (PAI)**.
- Thesis: *Perception must produce the same unit that action can act upon.*
- 정의: Perception = cohesive individuation + interpretation invariance across action.
- 6 DEFINITION-DRAFT vocabulary + 6 OPEN problems (OP-PAI-001..006)
- 증명 0건, mathematical formalization 없음, CANONICAL-DIRECTION

상세: [[canonical/perception_action_interpretation_pivot_2026_05_21|PAI 핀 문서]] · [[canonical/PAI_ROADMAP|Phase 0-6 roadmap]] · `THEORY/logs/daily/2026-05-21/00_pivot_entry.md` · `THEORY/logs/daily/MAIN_PROMPT_v4_PAI_PIVOT.md` (새 agent prompt; v3 는 legacy substrate 작업용으로 보존).

Trigger: `THEORY/working/macro_audit_2026-05-20.md` §11 verdict.

---

이 저장소의 **substrate 질문** (DECL-1.0):
**"어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"** — 변경 없음. Primitive 는 soft 응집장 $u_t : X_t \to [0,1]$ 이며, 객체는 가정되지 않고 준안정 응집장의 안정된 판독으로 사후 출현한다.

이 저장소의 **새 main axis** (PAI pivot, 2026-05-21):
**"Perception 과 action 이 같은 단위를 공유해야 한다."** — 이중 번역 거부. 증명 미완, OPEN.

---

## 0. 가장 먼저 읽을 것 (2분)

1. [[DECLARATION]] — DECL-1.0, 이론 중심축 선언문 (Q1~Q6).
2. [[00_manifest]] — SCC-CT v0.1 (구조적 권위, 9-Chapter, 4-tier Cat A/B/C/R).
3. [[canonical]] — CV-1.20 SEALED (사실적 권위, 102 claims).
4. [[theorem_status]] — 정리·OP 레지스트리.
5. [[hypothesis_tree]] — HT-3.11 차단 가설 의존 트리.
6. [[CV-1.20_SEAL]] — 최신 봉인 기록.
7. [[CHANGELOG]] — 세션 로그.

권위 계층 MOC: [[MOC_canonical_authority]] · [[MOC_SCC_CT_v0.1]] · [[MOC_hypothesis_tree]].

---

## 1. 이론이 답하려는 여섯 가지 질문

| 질문 | MOC | 수학적 구조 | 현재 상태 |
| --- | --- | --- | --- |
| Q1. 경계는 언제 출현하는가? | [[MOC_Q1_boundary_T8]] | T8 위상전이 $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ | 대부분 Cat A |
| Q2. 여럿이 공존할 수 있는가? | [[MOC_Q2_multi_formation]] | Multi-formation, Count bridge (T-L1-F) | Cat A (조건부) |
| Q3. 어떻게 변하는가? | [[MOC_Q3_stochastic_dynamics]] | Langevin / Gibbs / Lions-Sznitman | Package I Cat A |
| Q4. 몇으로 안정화되는가? | [[MOC_Q4_K_selection]] | K-selection (EQ / OBS / DYN) | Cat B |
| Q5. 시간이 지나도 같은 것인가? | [[MOC_Q5_temporal_identity]] | T-Temporal-Identity, OT, Sinkhorn | Cat A (CV-1.13) |
| Q6. 분열·합병 후에도 이어지는가? | [[MOC_Q6_sigma_inherit]] | σ-Inheritance (Wigner-projection) | 진행 중 |

Cross-cutting: [[MOC_sigma_rich_framework]] — σ-Rich fingerprint (Q1/Q2/Q4 횡단).

---

## 2. 수직 확장 — 큰 패키지 단위

| 패키지 | MOC | 위치 |
| --- | --- | --- |
| H-MORSE / Eyring-Kramers (Package II) | [[MOC_H_MORSE_packageII]] | `THEORY/working/CV114_H_MORSE_PACKAGEII/` |
| CV-1.15 Action 기반 시간 비용 | [[MOC_action_temporal_cost]] | `THEORY/working/CV115_ACTION_TEMPORAL_COST/` |
| CV-1.14 Temporal Composition 후보 | [[MOC_temporal_composition]] | `THEORY/working/CV114_TEMPORAL_COMPOSITION/` |
| W7 Temporal Audit (S-A1/S-A3/S-B1/S-C1) | [[MOC_temporal_audit_W7]] | `THEORY/working/temporal/` |
| Level-2 Observer Moduli Space (OMS) | [[MOC_observer_moduli_OMS]] | `THEORY/working/observer_moduli/` |
| Abstract Formation Dynamics (AFD-0 v0.1) | [[MOC_AFD_0_foundation]] | `THEORY/working/AFD_0/` |

---

## 3. 차단 가설 · Open Problems

[[MOC_open_problems_blockers]] — OP-0001~0022 + H-T*, H-MORSE, H-SINK, H-SR, H-WS, H-σ4, H-P7, H-κ, H-μ0 차단 그래프.

현재 W9+ 타겟: **macro ledger / objecthood theorem 정리**, **L-LOJASIEWICZ-CG Cat A path**, **non-uniform H-MORSE / Package II Eyring-Kramers 진입**, **T-σ-Inherit MERGE/SPLIT** ([[hypothesis_tree]] HT-3.11).

---

## 4. 검증 · 감사 · 기록

| 자산 | MOC |
| --- | --- |
| 실험 (exp1~exp88 + VP1~VP11) ↔ 정리 매핑 | [[MOC_experiments_validation]] |
| 일·주·월간 연구 일지 | [[MOC_research_journal]] |
| 폐기·계승된 산출물 (parking, 구 SEAL) | [[MOC_parked_superseded]] |

CV SEAL 체인: [[CV-1.13_SEAL]] → [[CV-1.15_SEAL]] → [[CV-1.16_SEAL]] → [[CV-1.17_SEAL]] → [[CV-1.18_SEAL]] → [[CV-1.19_SEAL]] → [[CV-1.20_SEAL]].

---

## 5. 권장 reading path (신규 협력자)

1. [[DECLARATION]] (2 분)
2. [[THEORY_INDEX|이 파일]]
3. [[00_manifest]] — 구조적 권위 개관
4. [[canonical]] §2 Foundational Orientation
5. [[hypothesis_tree]] §"세션 시작 / 즉시 타겟"
6. 관심 Q 의 MOC 한 개 — 예: [[MOC_Q4_K_selection]]
7. MOC 안의 ACTIVE ★ 파일 한 개
8. [[theorem_status]] 에서 그 정리의 Cat 상태 확인
9. [[CHANGELOG]] 최신 항목으로 현재 상태 확인

---

## 6. 현재 봉인 상태 (2026-05-20)

- **구조적 권위:** SCC-CT v0.1 SEALED ([[00_manifest]]).
- **사실적 권위:** CV-1.20 SEALED ([[canonical]]).
- **Counts:** 71 Cat A / 20 Cat B / 6 Cat C / 5 Cat R = **102 claims**, ~70% fully proved.
- **CV-1.20 주 성과:** L-UNI-ZMODE Cat A, L-SURFACE-TENSION-RESCALE Cat A. H-MORSE uniform-critical zero-mode branch strengthened; H-RESCALE closed Cat A.
- **Macro audit:** [[macro_audit_2026-05-20]] — 새 증명 없이 origin / grounded / conditional / intuition / overreach / macro gap 을 분리한 정지 감사.

---

## 7. 저장소 구조

```
Perception_theory/
├── THEORY_INDEX.md           ← 지금 이 문서 (최상위 MOC)
├── DECLARATION 등 권위 문서 ← THEORY/canonical/
├── SCC-CT v0.1 봉인 구조    ← SCC_CANONICAL/
├── 진행 중 작업 (Q1~Q6)      ← THEORY/working/  ([[INDEX|working/INDEX.md]])
├── 일·주·월 로그            ← THEORY/logs/
├── Python 구현 / 실험        ← CODE/
└── _archive/, private_brainstorm/ (이 인덱스에서 다루지 않음)
```

---

*MOC_00_THEORY_INDEX, 2026-05-20. 이론의 방향 또는 봉인 버전이 갱신될 때만 수정. 수정 시 [[CHANGELOG]] 에 기록.*
