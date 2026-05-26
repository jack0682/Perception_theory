---
id: CC-StableK-00
type: working/theory
status: open — CV-1.14 candidate working file
created: 2026-05-12
session: W7 carry-forward (CV-1.13 sealed 2026-05-10)
scope: OP-0012-CC-StableK — stable-K regime에서 temporal correspondence의 compositional consistency
parent_op: OP-0012 (Persistence Composition)
predecessor: THEORY/4_temporal/identity_inheritance/temporal_identity_sharp_form_2026-05-07.md (Lemma 6, Cat B sketch)
---

> [!nav] Linked: [[MOC_temporal_composition]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 00. 목표 및 범위 — OP-0012-CC-StableK

## 핵심 목표

**OP-0012-CC-StableK**: stable-K regime에서 시간적 대응의 합성 일관성(compositional consistency)을
정리화한다.

목표 정리 (한 문장):
> K_t = K_s = K_r = K, birth/death/merge/split 없음, unique matching margin Δ 조건 하에서,
> Δ > 2ε_comp이면 R_{t→r} = R_{s→r} ∘ R_{t→s}가 성립한다.

strict equality가 불가능하면 margin-stable equivalence로 약화:
> R_{t→r} ≡_Δ R_{s→r} ∘ R_{t→s}
>   (양변의 bijection이 Δ - 2ε_comp > 0 margin 이내에서 일치)

---

## 배경 — CV-1.13 현황

CV-1.13 (sealed 2026-05-10)에서 T-Temporal-Identity 전 4파트가 Cat A로 완성됨:

| 파트 | 내용 | 상태 |
|------|------|------|
| (a) 존재성 | R_{t→s} well-defined, 5 event types | Cat A |
| (b) 유일성 | stable-K + margin → bijection | Cat A |
| (c) 커널 독립성 | S-C1 margin 조건부 | Cat A |
| (d) K=1 환원 | persist_transport와 동치 | Cat A |

합성 일관성은 `temporal_identity_sharp_form_2026-05-07.md` Lemma 6으로
Cat B 스케치 수준에서 구성됨:
- "Under stable-K + margin on both intervals + basin-containment: π_{tr} = π_{sr} ∘ π_{ts}"
- 완전 증명 없음; ε_comp explicit bound 없음

OP-0012는 theorem_status.md 기준 **PARTIALLY STRUCTURED** 상태.
OP-0012-CC (stable-K 조건부 합성)가 Cat B path로 정의됨.

---

## 절대 금지 항목

| 금지 | 이유 |
|------|------|
| K-jump 일반 경우 증명 | OP-0012 전체 범위; Cat C 이상 불명; W8+ 별도 작업 |
| MERGE/SPLIT σ_standard 증명 | OP-0008 범위 |
| Wigner projection 진입 | T-σ-Inherit 영역 |
| H-MORSE / Package II 진입 | 완전히 별개 프로그램 |
| canonical.md 직접 수정 | promotion pipeline 준수 필수 |

---

## 범위 제한 (In-Scope)

정확한 범위:

```
주어진 것:
  t < s < r (세 시점)
  K_t = K_s = K_r = K   (stable-K: 세 시점 동일한 component 수)
  [t,s] 구간: no birth / death / merge / split
  [s,r] 구간: no birth / death / merge / split
  Δ := min(Δ_sep(M_{t→s}), Δ_sep(M_{s→r})) > 0  (양 구간 margin)
  ε_comp: OT 정규화 불일치로 인한 합성 오차

증명 목표:
  Δ > 2ε_comp  ⟹  R_{t→r} = R_{s→r} ∘ R_{t→s}
```

---

## 선행 파일 참조

| 파일 | 관련 내용 | 상태 |
|------|----------|------|
| `temporal_identity_sharp_form_2026-05-07.md` | Lemma 6, (A1)-(A9) package | Lemma 6 Cat B |
| `S-B3_kernel_independence.md` | Lemma 9/10/11 chain | Cat A/B |
| `partial_ot_stability.md` | Theorem Partial-H-SINK | Cat A |
| `S-A3_EXISTENCE_AUDIT.md` | R_{t→s} 존재성, 5 event types | Cat A |
| `canonical.md §13` | T-Temporal-Identity Cat A (CV-1.13) | Cat A |

---

## CV-1.14 승격 최소 조건

| 조건 | 설명 |
|------|------|
| Score Composition Lemma | Cat B 이상 (ε_comp 명시적 bound 포함) |
| Argmax Stability Lemma | Cat A (margin algebra, 거의 자명) |
| ε_comp explicit formula | ε_OT, M_tot, Δ의 함수로 명시 |
| 실험 검증 | K=2 stable sequence, ≥10 케이스, pass/fail 기록 |
| promotion pipeline review | working → canonical 일방향 통과 |

---

*작성: 2026-05-12 (W7 carry-forward). OP-0012-CC-StableK 전용 작업 폴더.*
