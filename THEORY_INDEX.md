---
type: MOC
cluster: top-level
id: MOC_00_THEORY_INDEX
last_updated: 2026-05-14
description: Soft Cognitive Cohesion (SCC) 이론 저장소의 최상위 진입 인덱스. 모든 MOC 와 권위 문서로의 진입점.
---

# THEORY_INDEX — Soft Cognitive Cohesion (SCC) 이론

> [!nav] Theory Navigation
> Parent: (root)
> Authority: [[DECLARATION]] · [[canonical]] · [[00_manifest]]
> Status: Active (CV-1.16 SEALED / SCC-CT v0.1)

이 저장소는 **"어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"** 라는 단일 질문에 수학적으로 답하려는 살아 있는 이론 시스템이다. Primitive 는 soft 응집장 $u_t : X_t \to [0,1]$ 이며, 객체는 가정되지 않고 준안정 응집장의 안정된 판독으로 사후 출현한다.

---

## 0. 가장 먼저 읽을 것 (2분)

1. [[DECLARATION]] — DECL-1.0, 이론 중심축 선언문 (Q1~Q6).
2. [[00_manifest]] — SCC-CT v0.1 (구조적 권위, 9-Chapter, 4-tier Cat A/B/C/R).
3. [[canonical]] — CV-1.16 SEALED (사실적 권위, 97 claims).
4. [[theorem_status]] — 정리·OP 레지스트리.
5. [[hypothesis_tree]] — HT-3.7 차단 가설 의존 트리.
6. [[CV-1.16_SEAL]] — 최신 봉인 기록.
7. [[CHANGELOG]] — 세션 로그.

권위 계층 MOC: [[MOC_canonical_authority]] · [[MOC_SCC_CT_v0.1]] · [[MOC_hypothesis_tree]].

---

## 1. 이론이 답하려는 여섯 가지 질문

| 질문 | MOC | 수학적 구조 | 현재 상태 |
| --- | --- | --- | --- |
| Q1. 경계는 언제 출현하는가? | [[MOC_Q1_boundary_T8]] | T8 위상전이 $\beta/\alpha > 4\lambda_2/|W''(c)|$ | 대부분 Cat A |
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

CV-1.17 타겟: **Package II Eyring-Kramers prefactor Cat B** ([[hypothesis_tree]] HT-3.7).

---

## 4. 검증 · 감사 · 기록

| 자산 | MOC |
| --- | --- |
| 실험 (exp1~exp88 + VP1~VP11) ↔ 정리 매핑 | [[MOC_experiments_validation]] |
| 일·주·월간 연구 일지 | [[MOC_research_journal]] |
| 폐기·계승된 산출물 (parking, 구 SEAL) | [[MOC_parked_superseded]] |

CV SEAL 체인: [[CV-1.13_SEAL]] → [[CV-1.15_SEAL]] → [[CV-1.16_SEAL]].

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

## 6. 현재 봉인 상태 (2026-05-14)

- **구조적 권위:** SCC-CT v0.1 SEALED ([[00_manifest]]).
- **사실적 권위:** CV-1.16 SEALED ([[canonical]]).
- **Counts:** 68 Cat A / 18 Cat B / 6 Cat C / 5 Cat R = **97 claims**, ~70% fully proved.
- **CV-1.16 주 성과:** H-MORSE-Local Closure Package — L-CLOSURE-LIFT Cat A, L-HMORSE-LOCAL Cat B, OP-HMORSE-BROADNESS CLOSED.

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

*MOC_00_THEORY_INDEX, 2026-05-14. 이론의 방향 또는 봉인 버전이 갱신될 때만 수정. 수정 시 [[CHANGELOG]] 에 기록.*
