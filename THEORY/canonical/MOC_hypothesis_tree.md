---
type: MOC
cluster: hypothesis-tree
id: MOC_hypothesis_tree
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: Hypothesis Tree & Blocking Hypotheses (HT-3.7)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]]
> Authority: [[hypothesis_tree]] (HT-3.7)
> Sibling: [[MOC_canonical_authority]] · [[MOC_open_problems_blockers]]
> Status: Active (CV-1.16 baseline)

## Purpose

CV-1.16 시점에서 **무엇이 무엇을 막고 있는가** 를 단일 화면에서 본다. SCC 이론은 14+ Cat B 결과를 가지며, 이 Cat B 들이 Cat A 로 승격되려면 차단 가설(H-가설)들이 닫혀야 한다. 이 MOC 는 [[hypothesis_tree]] 의 의존 그래프를 wikilink 로 풀어서 노출한다.

## Authoritative Source

- [[hypothesis_tree]] — HT-3.7 (2026-05-14 봉인).

## Blocking Hypotheses Summary

| ID | 가설 | 현재 상태 | 차단하는 정리 | 우선순위 | Phase |
| --- | --- | --- | --- | --- | --- |
| **H-SINK** | Sinkhorn-Lipschitz (S-B2) | **FULLY CLOSED** Cat A (CV-1.12) | Q5 Cat A ✓ | 완료 | 1 ✓ |
| **H-T*** | T_* 정규 등록 (OP-0021) | OPEN | Q3/Q4 수치화 | 최상 | 2 |
| **H-MORSE** | Morse 안정성 | **PARTIALLY CLOSED** Local Cat B (CV-1.16) | Package II 진입 | 최상 | 2 |
| **H-SR** | 스펙트럼 반발 호환성 | OPEN | Q2 무조건화 | 중 | 2 |
| **H-WS** | Well-separation 도출 | OPEN | Q2 범위 확장 | 중 | 2 |
| **H-σ4** | T-σ-Theorem-4 Cat A | PARTIALLY OPEN | Q1 σ-framework | 중 | 2 |
| **H-P7** | Decay-to-cut (P7) | PARTIALLY STRUCTURED | Q2 조건 감소 | 중하 | 3 |
| **H-κ** | 곡률 조건 도출 | OPEN | Q1 조건 감소 | 중하 | 3 |
| **H-μ0** | μ₀ > 0 일반 증명 | OPEN | Q1 완전 무조건화 | 낮음 | 3 |

## Critical Path (CV-1.16 → CV-1.17)

```
H-SINK [Phase 1] ─→ Q5 Cat A ✓ → CV-1.12 ✓ (2026-05-10)
                       │
                       ▼
                S-B1-Weak Cat A + S-A1/S-A3/S-C1 ─→ T-Temporal-Identity Cat A ✓ → CV-1.13 ✓
                       │
                       ▼
                  Q6 Cat B (σ-상속) ── OP-0008 MERGE/SPLIT (Phase 2)

H-MORSE ──┐
          ├──→ Package II (Eyring-Kramers)  [CV-1.17 타겟]
H-T*    ──┘
```

## H-가설 ↔ Q-MOC 매핑

- H-T* → [[MOC_Q3_stochastic_dynamics]], [[MOC_Q4_K_selection]]
- H-MORSE → [[MOC_H_MORSE_packageII]], [[MOC_Q3_stochastic_dynamics]]
- H-SINK → [[MOC_Q5_temporal_identity]] (CLOSED)
- H-SR → [[MOC_Q2_multi_formation]]
- H-WS → [[MOC_Q2_multi_formation]]
- H-σ4 → [[MOC_Q1_boundary_T8]], [[MOC_sigma_rich_framework]]
- H-P7, H-κ, H-μ0 → [[MOC_Q1_boundary_T8]], [[MOC_Q2_multi_formation]]

## Dependencies

- Reads: [[hypothesis_tree]] (single source of truth).
- Pairs with: [[theorem_status]] (OP catalog).
- Feeds: [[MOC_open_problems_blockers]] 의 OP × H 매트릭스.

## Modification Governance

가설 트리 수정은 [[hypothesis_tree]] 후미의 "수정 규칙" 을 따른다. 이 MOC 는 *반영* 만 하며 권위는 hypothesis_tree.md 가 가진다.

## Related Clusters

- [[MOC_canonical_authority]]
- [[MOC_open_problems_blockers]]
- 모든 Q-MOC (Q1~Q6)

---

*MOC_hypothesis_tree, 2026-05-14.*
