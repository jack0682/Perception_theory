---
type: MOC
cluster: Q6-sigma-inherit
id: MOC_Q6_sigma_inherit
parent: [[THEORY_INDEX]]
question: Q6. 분열·합병 후에도 이어지는가?
last_updated: 2026-05-14
---

# MOC: Q6 — 분열·합병 후에도 이어지는가? (σ-Inheritance)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[INDEX|working/INDEX.md]]
> Authority: [[canonical]] T-σ-Inherit (Cat C, Wigner-projection deferred); [[theorem_status]]
> Status: 진행 중. OP-0008 MERGE/SPLIT 활성.

## Purpose

응집 구조가 분열(SPLIT) 또는 합병(MERGE) 사건을 겪은 후에도 σ-fingerprint 가 인헤리트되는지를 다룬다. OP-0008-DIST 는 Cat B (Lemma 16) 로 닫혔으나 MERGE/SPLIT 부분은 Phase 2 진행 중. K-jump 케이스가 1차 표적.

## Core Files (Active)

- [[sigma_inherit_k_jump]] ★ — K-jump σ-inheritance (H-σ4 개발)
- [[sigma_multi_trajectory]] — Multi-trajectory σ tracking
- [[cobelonging_vs_sigmaD]] — Co-belonging vs σ_D (cross-cut Q2)

## σ-Rich (cross-cutting) → [[MOC_sigma_rich_framework]]

Q6 의 σ-inheritance 는 σ-Rich fingerprint 의 시간 변화 형태이며, 정적 부분은 [[MOC_sigma_rich_framework]] 가 관리.

## Code Module

- `CODE/scc/sigma_rich.py` — SigmaRich namedtuple (sigma_standard, centroids, orientations, wigner_data). K-jump σ-inheritance (OP-0008 Path B) 의 derived diagnostic.

## Reading Order

1. [[canonical]] §T-σ-Inherit (Cat C 현재)
2. [[sigma_inherit_k_jump]]
3. [[sigma_multi_trajectory]]
4. [[cobelonging_vs_sigmaD]]
5. [[MOC_sigma_rich_framework]] (정적 σ 구조)
6. [[MOC_Q5_temporal_identity]] (시간 동일성 foundation)

## Dependencies

- Requires: [[MOC_Q5_temporal_identity]] (T-Temporal-Identity Cat A), [[MOC_sigma_rich_framework]] (σ-Rich definitions).
- Blocked by: OP-0008 MERGE/SPLIT (Phase 2); H-σ4 (T-σ-Theorem-4 Cat A).

## Current Status (CV-1.16)

- **Canonical:** T-σ-Inherit (Cat C; Wigner-projection deferred); OP-0008-DIST CLOSED Cat B (Lemma 16).
- **Working:** K-jump σ-inheritance, multi-trajectory tracking.
- **Open:** OP-0008 MERGE/SPLIT (Phase 2 target); H-σ4 partial open.

## Related Clusters

- [[MOC_Q5_temporal_identity]]
- [[MOC_sigma_rich_framework]]
- [[MOC_Q2_multi_formation]] (co-belonging cross-cut)
- [[MOC_hypothesis_tree]]

---

*MOC_Q6_sigma_inherit, 2026-05-14.*
