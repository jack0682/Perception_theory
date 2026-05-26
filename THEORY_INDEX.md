---
type: MOC
cluster: top-level
id: MOC_00_THEORY_INDEX
last_updated: 2026-05-26
description: Soft Cognitive Cohesion (SCC) 저장소 최상위 진입 인덱스. 2026-05-26 perception-action stack 으로 재편. 중심축 = actional perception (DECL-2.0); substrate = 봉인된 cohesion morphology.
---

# THEORY_INDEX — Actional Perception (perception-action stack)

> [!nav] Theory Navigation
> Parent: (root)
> Center: [[DECLARATION]] (DECL-2.0) · [[CANONICAL_AXIS]] · [[PAI_GLOSSARY]]
> Authority (substrate): [[canonical]] (CV-1.20) · [[sct_manifest]]
> Status: Active (DECL-2.0 / CV-1.20 substrate sealed / HT-3.12)

## 중심축 (DECL-2.0)

> **Perception 은 가능한 로봇 개입(intervention)의 장을 형성하는 것이다.** 장면은 개입 가능성 구조에 대한 등급화된 참여 $u_t : X_t \to [0,1]$ 로 조직되고, 객체·affordance·행동단위·궤적·제어모드는 그 *하나의 장의 사영*이다. 객체성 = 안정화된 affordance 구조.

지능이 세계를 두 번 해석(perception → 다시 action)하는 **이중 번역**을 제거하는 것이 이 이론의 목표다. 상세: [[CANONICAL_AXIS]] · [[AUDIT_perception_action_2026-05-26]].

축의 형식화 (𝒜(u;Θ), Δ_interp, 불변성 기준) 는 **OPEN**: [[perception_action_interpretation_pivot_2026_05_21|PAI Pivot]] · [[PAI_ROADMAP|Roadmap Phase 0–6]] · OP-PAI-001..006 / OP-ACTIONAL-U / OP-PROJECTION / OP-CONTROL-GROUNDING ([[theorem_status]]).

## Substrate (봉인, 불변)

cohesion-field morphology — closure/separation/boundary/transport — 와 102개 봉인 정리(CV-1.20, 71A/20B/6C/5R). 개입 장이 올라타는 *운반층*이지 이론 자체가 아니다. DECL-1.0 의 질문 "어떤 차이의 덩어리가 언제 객체가 되는가" 는 substrate 질문으로 보존.

---

## 0. 가장 먼저 읽을 것 (perception-action stack)

| 순서 | 문서 | 위치 |
|---|---|---|
| 1 | [[DECLARATION]] (DECL-2.0) — 중심축 선언 | `THEORY/0_axis/` |
| 2 | [[CANONICAL_AXIS]] — spine (one field → projections) | `THEORY/0_axis/` |
| 3 | [[PAI_GLOSSARY]] — 통제 어휘 | `THEORY/0_axis/` |
| 4 | [[canonical]] (CV-1.20) — substrate 사실 권위 | `THEORY/2_substrate/canonical/` |
| 5 | [[sct_manifest]] — substrate 구조 권위 (9장) | `THEORY/2_substrate/canonical/structural/` |
| 6 | [[theorem_status]] · [[hypothesis_tree]] — 정리·OP·차단 트리 | `THEORY/2_substrate/canonical/` |
| 7 | [[CHANGELOG]] — 세션 로그 | `THEORY/` |

권위 MOC: [[MOC_canonical_authority]] · [[MOC_SCC_CT_v0.1]] · [[MOC_hypothesis_tree]].

---

## 1. Substrate 의 여섯 질문 (Q1~Q6)

| 질문 | MOC | 수학 구조 | 상태 |
| --- | --- | --- | --- |
| Q1. 경계는 언제 출현? | [[MOC_Q1_boundary_T8]] | T8 위상전이 $\beta/\alpha > 4\lambda_2/\lvert W''(c)\rvert$ | 대부분 Cat A |
| Q2. 여럿이 공존? | [[MOC_Q2_multi_formation]] | Multi-formation, Count bridge | Cat A (조건부) |
| Q3. 어떻게 변하나? | [[MOC_Q3_stochastic_dynamics]] | Langevin / Gibbs / Lions-Sznitman | Package I Cat A |
| Q4. 몇으로 안정화? | [[MOC_Q4_K_selection]] | K-selection (EQ/OBS/DYN) | Cat B |
| Q5. 시간 동일성? | [[MOC_Q5_temporal_identity]] | T-Temporal-Identity, OT, Sinkhorn | Cat A (CV-1.13) |
| Q6. 분열·합병 계승? | [[MOC_Q6_sigma_inherit]] | σ-Inheritance | 진행 중 |

Cross-cutting: [[MOC_sigma_rich_framework]] (σ-Rich fingerprint).

---

## 2. 수직 확장 패키지

| 패키지 | MOC | 위치 |
| --- | --- | --- |
| H-MORSE / Eyring-Kramers (Package II) | [[MOC_H_MORSE_packageII]] | `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/` |
| CV-1.15 Action 기반 시간 비용 | [[MOC_action_temporal_cost]] | `THEORY/4_temporal/action_cost/` |
| CV-1.14 Temporal Composition | [[MOC_temporal_composition]] | `THEORY/4_temporal/composition/` |
| W7 Temporal Audit | [[MOC_temporal_audit_W7]] | `THEORY/4_temporal/temporal_audit/` |
| Level-2 Observer Moduli (OMS) | [[MOC_observer_moduli_OMS]] | `THEORY/2_substrate/foundations/observer_moduli/` |
| Abstract Formation Dynamics (AFD-0) | [[MOC_AFD_0_foundation]] | `THEORY/2_substrate/foundations/AFD/` |

---

## 3. Open Problems

[[MOC_open_problems_blockers]] — substrate OP-0001~0022 + H-* 차단 그래프; **축 OP**: OP-PAI-001..006, OP-ACTIONAL-U, OP-PROJECTION, OP-CONTROL-GROUNDING.

---

## 4. 검증 · 기록

실험↔정리 매핑 [[MOC_experiments_validation]] · 연구 일지 [[MOC_research_journal]].
CV SEAL 체인 (`THEORY/2_substrate/canonical/seals/`): [[CV-1.13_SEAL]] → [[CV-1.15_SEAL]] → [[CV-1.16_SEAL]] → [[CV-1.17_SEAL]] → [[CV-1.18_SEAL]] → [[CV-1.19_SEAL]] → [[CV-1.20_SEAL]].

---

## 5. 저장소 구조 (perception-action stack)

```
Perception_theory/
├── THEORY_INDEX.md             ← 이 문서 (최상위 MOC)
├── CLAUDE.md / README.md / CONVENTIONS.md
├── THEORY/
│   ├── 0_axis/                 중심축: DECLARATION(2.0), CANONICAL_AXIS, PAI_GLOSSARY, audit, roadmap, pivot
│   ├── 1_sensing/              raw → field
│   ├── 2_substrate/            cohesion morphology + canonical/ (사실+구조 권위) + Q1~Q4 + foundations
│   ├── 3_projections/          PAI 사영 (prolegomena, object/affordance/action/control)
│   ├── 4_temporal/             identity / transport / succession
│   └── logs/                   daily / weekly / monthly
├── CODE/                       Python 구현 / 실험
└── _archive/, private_brainstorm/
```

---

## 6. 봉인 상태 (2026-05-20 substrate / 2026-05-26 reorg)

- **사실 권위:** CV-1.20 SEALED ([[canonical]]). **구조 권위:** SCC-CT v0.1 ([[sct_manifest]]).
- **Counts:** 71 Cat A / 20 Cat B / 6 Cat C / 5 Cat R = **102 claims** (~70% proved). 축(PAI) 작업으로 불변.
- **2026-05-26 reorg:** perception-action stack 재편; SCC_CANONICAL → `2_substrate/canonical/structural/` 통합; DECL-2.0 승격. 링크 무결성 검증 통과 (`scripts/migration/verify_links.py`).

---

*MOC_00_THEORY_INDEX, 2026-05-26. 방향·봉인 버전 갱신 시에만 수정. [[CHANGELOG]] 기록.*
