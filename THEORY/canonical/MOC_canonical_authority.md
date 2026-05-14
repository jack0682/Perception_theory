---
type: MOC
cluster: canonical-authority
id: MOC_canonical_authority
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: Canonical Authority Layer

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]]
> Sibling: [[MOC_SCC_CT_v0.1]] · [[MOC_hypothesis_tree]]
> Status: Canonical (authoritative, CV-1.16 SEALED)

## Purpose

`THEORY/canonical/` 의 5개 권위 문서를 단일 진입점으로 모은다. 이 폴더는 **승급된 컨텐츠만** 받아들이며 본문은 erratum/retraction 마커 외에 손대지 않는다. 사실적 권위(facts-as-of-now)는 여기, 구조적 권위(ontological role)는 [[MOC_SCC_CT_v0.1]] 에 있다.

## Core Files

- [[DECLARATION]] — DECL-1.0 이론 선언문 (먼저 읽기, 2분).
- [[canonical]] — CV-1.16 SEALED, 97 claims authoritative spec.
- [[theorem_status]] — 정리 인덱스 + Open Problems Catalog (OP-0001..OP-0022).
- [[hypothesis_tree]] — HT-3.7 차단 가설 의존 트리.
- [[CV-1.16_SEAL]] — 최신 봉인 기록.
- [[CV-1.15_SEAL]] — Action 기반 시간성 봉인.
- [[CV-1.13_SEAL]] — T-Temporal-Identity Cat A 봉인.
- [[CHANGELOG]] — 세션 단위 변경 기록 (THEORY 측).

## Reading Order

1. [[DECLARATION]]
2. [[canonical]] §2 (Foundational Orientation)
3. [[hypothesis_tree]] (세션 시작 타겟 절)
4. [[theorem_status]] (해당 정리 행)
5. [[CV-1.16_SEAL]] (최근 변경 이유)
6. [[CHANGELOG]] (전체 흐름)

## Dependencies

- Promotes from: [[INDEX|working/INDEX.md]] → working files (3-stage pipeline).
- Cross-links: [[00_manifest]] (SCC-CT v0.1 구조적 권위).
- Feeds into: [[MOC_Q1_boundary_T8]]..[[MOC_Q6_sigma_inherit]] 의 "Current Status" 절.

## Promotion Pipeline (요약)

```
THEORY/logs/daily/YYYY-MM-DD/  (raw)
        ↓ reorganize
THEORY/working/<topic>.md       (active)
        ↓ proof + review + tests + user merge
THEORY/canonical/canonical.md   (one-way)
THEORY/canonical/theorem_status.md
THEORY/CHANGELOG.md
```

자세히는 [[README|canonical/README.md]] 의 promotion criteria 5조항.

## Current Status (CV-1.16)

- **Sealed version:** CV-1.16 (2026-05-14, W7-Day5 ext).
- **Count:** 68 A / 18 B / 6 C / 5 R = 97 claims.
- **Next target:** CV-1.17 Package II Eyring-Kramers prefactor Cat B.
- **Most recent additions:** L-CLOSURE-LIFT (Cat A), L-HMORSE-LOCAL (Cat B), L-HMORSE-DECOMP (Cat B), L-BOUNDARY-MODE-EXCLUSION (Cat C). OP-HMORSE-BROADNESS CLOSED.

## SEAL Chain (Superseded-by)

[[CV-1.13_SEAL]] → [[CV-1.15_SEAL]] → [[CV-1.16_SEAL]] (현재).

이전 CV-1.0~1.12 봉인 기록은 [[CHANGELOG]] 에 흡수.

## Related Clusters

- [[MOC_SCC_CT_v0.1]] — 구조적 권위 (9-Chapter, Cat A/B/C/R).
- [[MOC_hypothesis_tree]] — 차단 가설 그래프.
- [[MOC_open_problems_blockers]] — OP × H 매트릭스.
- [[MOC_research_journal]] — daily/weekly/monthly 로그.

---

*MOC_canonical_authority, 2026-05-14.*
