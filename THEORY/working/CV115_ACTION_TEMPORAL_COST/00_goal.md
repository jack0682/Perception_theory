---
id: ACT-00
type: working/theory
status: open — CV-1.15 working file (재작성 2026-05-12)
created: 2026-05-12
session: W7 carry-forward
scope: Action-Based Temporal Succession Package
predecessor: CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md (OP-0012-SINK 정의)
---

# 00. 목표 — CV-1.15 Action-Based Temporal Succession Package

---

## 핵심 목적

CV-1.15는 SCC temporal identity의 cost 구조를 **endpoint similarity에서 action-based path inheritance로 전환**한다.

질문의 전환:

| 이전 (endpoint 기반) | 이후 (action 기반) |
|---|---|
| "x와 z가 직접 닮았는가?" | "x에서 z로 이어지는 최소 action 역사 경로가 존재하는가?" |
| c_endpoint(x,z) = ‖z−x‖² | c^act_{i→k}(x,z) = min over paths A_{i:k} |
| composition 불가 (반례 존재) | Bellman DP 정확히 성립 |

---

## CV-1.14와의 관계

| 패키지 | 핵심 질문 | 핵심 결과 |
|---|---|---|
| CV-1.14 | 합성된 kernel이면 relation도 합성되는가? | T-CC-StableK-Kernel (Cat B): R[M∘M]=R[M]∘R[M] |
| CV-1.15 | action principle이 자연스럽게 합성되는 kernel을 만드는가? | T-ACT-DP (Cat A): DP 정확 성립; T-ACT-GIBBS (Cat A): K_{i→k}=K_{i→j}K_{j→k} |

CV-1.15의 T-ACT-GIBBS는 CV-1.14 T-CC-StableK-Kernel의 **전제 "M_{t→r}=M_{s→r}∘M_{t→s}"를 action 원리로부터 자연스럽게 유도**한다.

연결 경로:
```
T-ACT-GIBBS (CV-1.15, Cat A)
   → K_{t→r} = K_{t→s}K_{s→r} (raw kernel semigroup)
   → (CV-1.14 T-CC-StableK-Kernel 조건 충족, Cat B 조건부)
   → R[K_{t→r}] = R[K_{t→s}]∘R[K_{s→r}]  (T-ACT-KERNEL-COMP→REL, Cat B)
```

---

## 닫을 수 있는 것 (Cat A 목표)

| Lemma/Theorem | 내용 |
|---|---|
| L-ENDPOINT-NONSEMI | Squared endpoint cost 합성 불가 반례 |
| L-ACTION-NORMALIZATION | Time-normalized cost 등속 경로에서 정합 |
| T-ACT-DP | Hard-min action cost Bellman DP (핵심 1) |
| T-ACT-GIBBS | Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k} (핵심 2) |
| L-SOFTMIN-HARDMIN-BOUND | soft-min / hard-min 오차 ≤ ε log N |
| L-ACTION-DELTA-EFF-ZERO | action direct cost = effective cost → δ_eff=0 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | soft-min action δ_eff^ε=0 (T-ACT-GIBBS 귀결) |
| L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action은 DP/Gibbs 전제 만족 |

## 조건부로 닫을 수 있는 것 (Cat B)

| Theorem | 조건 |
|---|---|
| T-ACT-KERNEL-COMP→REL | M을 Gibbs kernel로 재정의 + stable-K + margin 조건 |
| P-SINKHORN-STABILITY-CONDITIONAL | H-SINK / Sinkhorn Lipschitz lemma 조건부 |

## 열린 것 (OPEN 유지)

| 문제 | 이유 |
|---|---|
| Sinkhorn-scaled plan semigroup | scaling vector 호환성 보장 없음; generically fails |
| OP-0012-SINK (Sinkhorn M 그대로) | Gibbs kernel ≠ Sinkhorn plan 일반적 |
| action kernel을 canonical M으로 채택할지 | canonical 정의 변경 필요 → CV-1.16 이후 |
| fingerprint φ 3성분 vs 4성분 선택 | 별도 실험 필요 |
| continuous-time limit | Γ-수렴 or viscosity 분석 필요 |

---

## 절대 금지

- Sinkhorn-scaled plan semigroup을 proved / Cat B로 선언 금지
- T-CC-StableK-Sinkhorn 독립 Sinkhorn 버전 proved 선언 금지
- ε_comp=0 Route B 사용 금지 (CV-1.14에서 폐기)
- canonical.md / theorem_status.md / hypothesis_tree.md 직접 수정 금지
- H-MORSE, Eyring-Kramers, Wigner projection, K-jump 일반론, MERGE/SPLIT σ_standard 확장 금지
- 독립 Sinkhorn composition 문제를 이번 작업에서 닫으려 시도 금지

---

## 파일 구조

```
CV115_ACTION_TEMPORAL_COST/
├── 00_goal.md                    ← 이 파일
├── 01_endpoint_failure.md        ← endpoint cost 실패 증명
├── 02_action_cost_definition.md  ← action cost 정의
├── 03_dynamic_programming_theorem.md  ← T-ACT-DP
├── 04_softmin_gibbs_semigroup.md ← T-ACT-GIBBS
├── 05_relation_to_sinkhorn.md    ← Sinkhorn 분리 + OPEN 명시
├── 06_experiment_plan.md         ← exp89 계획
├── 07_promotion_draft.md         ← canonical 초안
└── 08_gap_audit.md               ← 최종 감사 + 한국어 보고서
```

---

*작성: 2026-05-12.*
