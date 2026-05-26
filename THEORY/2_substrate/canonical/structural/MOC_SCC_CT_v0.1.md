---
type: MOC
cluster: scc-ct-sealed
id: MOC_SCC_CT_v0.1
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: SCC-CT v0.1 — Sealed Theoretical Structure

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]]
> Sibling: [[MOC_canonical_authority]]
> Pairs with: [[canonical]] (사실적 권위)
> Status: SEALED 2026-05-14 (구조적 권위)

## Purpose

`SCC_CANONICAL/` 은 SCC 이론의 **구조적 권위** 층이다. CV-1.x 릴리즈 사다리(`THEORY/2_substrate/canonical/canonical.md`)는 *언제 무엇이 증명되었는가*를 기록하고, 이 디렉토리는 *무엇이 이론적으로 영구한 구조인가*를 기록한다 — 9-Chapter, 4-tier Cat A/B/C/R, 97 claims 의 봉인된 분류표.

두 권위 사이의 갈등 시 `THEORY/2_substrate/canonical/canonical.md` 가 fact authority, 이 폴더가 structure authority. 갈등 발생 → v0.2 재봉인.

## Core Files

- [[sct_manifest]] — 이름·범위·선언·구조 (Ch. 0).
- [[sct_ontology]] — Ch. I Ontological Commitment (pre-objective primitive).
- [[sct_axioms_and_primitives]] — Ch. II + III: Primitive Structure + Operator Triad.
- [[sct_energy_and_diagnostics]] — Ch. IV + V: Diagnostic Vector + 4-term Energy.
- [[sct_theorem_registry]] — Ch. VI + VII: Cat A/B/C 정리 등록부 + computational validation.
- [[sct_open_problems]] — Ch. VIII: 활성 open problems.
- [[sct_forbidden_claims]] — Ch. IX: Cat R + 금지 어휘.
- [[sct_changelog]] — SCC-CT 자체 변경 기록 (CV-1.x 사다리와 분리).

## Reading Order

1. [[sct_manifest]] (구조 개관)
2. [[sct_ontology]] (pre-objective commitment)
3. [[sct_axioms_and_primitives]] (A1'-A4, B1-B4, E1-E4 + operator triad)
4. [[sct_energy_and_diagnostics]] (E_cl, E_sep, E_bd, E_tr + d∈[0,1]^4)
5. [[sct_theorem_registry]] (Cat A/B/C 분류된 97 claims)
6. [[sct_open_problems]] (active OPs)
7. [[sct_forbidden_claims]] (Cat R + 금지 어휘)

## 4-Tier Classification

| Cat | 의미 | 예시 |
| --- | --- | --- |
| A | Fully proved / sealed | T8-Core 위상전이; T-Temporal-Identity (CV-1.13); L-CLOSURE-LIFT (CV-1.16) |
| B | Partial / 명시적 조건 | T-K-Select-PF (T_* axiomatic); L-HMORSE-LOCAL |
| C | Conjectural / architectural | L-BOUNDARY-MODE-EXCLUSION; T-σ-Inherit σ_standard; T-Persist-Full |
| R | Rejected / forbidden 표현 | original A1; mountain pass on Σ_M^K; "temporal theorem proved" |

Count at v0.1 seal: **68 A / 18 B / 6 C / 5 R = 97 claims (~70%)**.

## Forbidden Wording (manifest-level)

[[sct_forbidden_claims]] 의 Cat R 항목과 함께 다음 표현은 모든 SCC-CT 문서에서 **금지**:

- "temporal theorem proved" (T-Temporal-Identity (c) 는 Cat A 조건부; 무조건적이지 않음)
- "transport fixed point fully established"
- "multi-formation solved"
- "Sep term essentiality proved"
- "paper ready as-is"
- "H-MORSE Cat A unconditional" (V5b-T-zero 구조적 반례, CV114)
- "L-CLOSURE-LIFT replaces T7-Enhanced" (broadness 만 replace; T7-Enhanced 보존)
- "Cat A by construction" (V-AFD / R-2 실패 모드)

## Dependencies

- Pairs with: [[canonical]] — fact ↔ structure 페어. 갈등 시 SCC-CT v0.2 재봉인.
- Cross-references: [[DECLARATION]] (DECL-1.0 의 pre-objective 선언을 sanctify).
- 영향받음: 모든 [[MOC_Q1_boundary_T8]]..[[MOC_Q6_sigma_inherit]] 의 Cat 분류 라벨링.

## Related Clusters

- [[MOC_canonical_authority]] — 사실적 권위 페어.
- [[MOC_open_problems_blockers]] — Ch. VIII 의 OP 들이 여기 등록.

## What This Seal Does NOT Do

- `THEORY/2_substrate/canonical/canonical.md` 를 수정하지 않음.
- 새 수학 도입하지 않음.
- DECL-1.0 을 대체하지 않음 — extend & sanctify.

---

*MOC_SCC_CT_v0.1, 2026-05-14. SCC-CT v0.1 SEAL 시점.*
