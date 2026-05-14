---
id: ACT-08
type: working/theory
status: open — 최종 gap audit + 한국어 보고서
created: 2026-05-12
scope: 닫힌 것 / 열린 것 분리, CV-1.14 연결 요약, 승격 문장
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 08. Gap Audit — CV-1.15 최종 보고서

---

## §1. 닫힌 것 (Cat A, 증명 완결)

| 항목 | 근거 | 파일 | 조건 |
|---|---|---|---|
| Endpoint cost 합성 불가 | 반례: $x=0,z=2$ → $4 \neq 2$ | 01 | $\mathbb{R}^1$, 임의 $x\neq z$ |
| Time-normalized cost 등속 경로 additive | 선형 보간 대수 계산 | 01 | 등속 경로에서만 |
| SCC fingerprint action admissibility | $a_i\geq0$ + additivity 확인 | 02 | 구조적 확인 (fingerprint quality 별도) |
| **T-ACT-DP** Hard-min Bellman DP | 양방향 부등식 (경로 분해 + 이어붙임) | 03 | 유한 site set, additive action |
| $\delta_\mathrm{eff}=0$ under action definition | T-ACT-DP 직접 귀결 | 03 | action direct cost 재정의 전제 |
| **T-ACT-GIBBS** Gibbs kernel semigroup | Chapman-Kolmogorov path-integral 분해 | 04 | 유한 site set, $\varepsilon>0$, additive action |
| Soft-min / hard-min bound $\leq\varepsilon\log N$ | log-sum-exp 표준 부등식 | 04 | 표준 |
| $\delta_\mathrm{eff}^\varepsilon=0$ (soft-min) | T-ACT-GIBBS 직접 귀결 | 04 | $\varepsilon>0$ |

**요약**: Cat A 8건 모두 완결. 핵심 두 결과는 T-ACT-DP와 T-ACT-GIBBS이다.

---

## §2. 조건부 결과 (Cat B)

| 항목 | 조건 | 파일 | 이유 |
|---|---|---|---|
| T-ACT-KERNEL-COMP→REL | (GK): $M:=K_{\mathrm{Gibbs}}$ 재정의 + (stable-K) + (margin) | 05 | canonical §8.5 정의 변경 필요 |
| P-SINKHORN-STABILITY-CONDITIONAL | H-SINK + MARGIN + SMALL-SINK-GAP | 05 | H-SINK 별도 미증명; gap이 작다는 보장 없음 |

---

## §3. 열린 것 (OPEN)

| 항목 | 이유 | 분류 |
|---|---|---|
| **Sinkhorn-scaled plan semigroup** | $b_1\odot a_2\neq c\cdot\mathbf{1}$ generically (대수 반례) | OPEN (proved failure) |
| **OP-0012-SINK** (Sinkhorn $M$ 유지) | scaling gap bound 없음; L-δ_eff-SINK + L-Eff-Sinkhorn 미증명 | OPEN |
| Action kernel을 canonical $M$으로 채택 | canonical.md §8.5 정의 변경 결정 필요 | OPEN (CV-1.16 이후) |
| Fingerprint $\varphi$ 3성분 vs 4성분 | resolvent diagonal 포함 여부 실험 미완 | OPEN |
| Continuous-time limit | Γ-수렴 or viscosity 분석 별도 필요 | OPEN |
| K-jump / MERGE / SPLIT으로 확장 | 이번 작업 금지 영역 | OPEN (별도 OP) |

---

## §4. 전체 판정표

| 항목 | 내용 | 판정 | 다음 조치 |
|---|---|---|---|
| L-ENDPOINT-NONSEMI | endpoint squared cost 비합성성 | **Cat A 후보** | promotion 가능 |
| L-ACTION-NORMALIZATION | time-normalized cost 등속 경로 additive | **Cat A 후보** | promotion 가능 |
| L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action DP/Gibbs 전제 충족 | **Cat A 후보** | promotion 가능 |
| **T-ACT-DP** | hard-min action Bellman DP | **Cat A 후보** | promotion 가능 |
| **T-ACT-GIBBS** | soft-min / Gibbs kernel semigroup | **Cat A 후보** | promotion 가능 |
| L-SOFTMIN-HARDMIN-BOUND | soft-min / hard-min 오차 $\leq\varepsilon\log N$ | **Cat A 후보** | promotion 가능 |
| L-ACTION-DELTA-EFF-ZERO | action direct / effective gap = 0 | **Cat A 후보**, action definition 조건 | promotion 가능 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | soft-min $\delta_\mathrm{eff}^\varepsilon=0$ | **Cat A 후보** | promotion 가능 |
| P-ACTION-PATH-INHERITANCE | action = path inheritance 해석 | Interpretation | motivation 삽입 |
| T-ACT-KERNEL-COMP→REL | action kernel → relation composition | **Cat B 조건부** | CV-1.14 Lemma 6 연결; canonical 정의 변경 대기 |
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | Sinkhorn plan semigroup generically fails | **OPEN (proved failure)** | OP-0012-SINK 별도 유지 |
| P-SINKHORN-STABILITY-CONDITIONAL | H-SINK 조건부 relation 보존 | **Cat B 조건부** | H-SINK lemma 필요 |
| OP-0012-SINK | Sinkhorn plan composition | **OPEN** | L-δ_eff-SINK + L-Eff-Sinkhorn 필요 |

---

## §5. CV-1.14와 CV-1.15의 관계 요약

```
CV-1.14 (T-CC-StableK-Kernel, Cat B):
  "합성된 kernel이면 relation도 합성된다"
  R[M∘M] = R[M]∘R[M]  (stable-K + margin 조건)

CV-1.15 (T-ACT-GIBBS, Cat A):
  "action principle이 자연스럽게 합성되는 kernel을 만든다"
  K_{i→k} = K_{i→j}K_{j→k}  (raw Gibbs kernel, 정확히 성립)

연결 (T-ACT-KERNEL-COMP→REL, Cat B):
  T-ACT-GIBBS (Cat A)  [CV-1.15]
    +
  T-CC-StableK-Kernel (Cat B)  [CV-1.14]
    ↓
  R[K_{t→r}] = R[K_{t→s}]∘R[K_{s→r}]  (stable-K + margin + GK 조건)
```

**핵심 구분**:

| | CV-1.14 | CV-1.15 |
|---|---|---|
| 질문 | "합성이 relation을 보존하는가?" | "action이 자연스럽게 합성 구조를 만드는가?" |
| 핵심 결과 | Cat B (kernel composition 조건부) | Cat A (raw action / Gibbs kernel, 정확히) |
| Sinkhorn plan | "독립 Sinkhorn은 OPEN" (OP-0012-SINK) | "Sinkhorn semigroup is generically false" |

---

## §6. 잔여 블로커 분석

**CV-1.15로 해소된 블로커**:

- OP-0012-SINK의 "$\delta_\mathrm{eff}$ bound 없음" 문제 → action cost로 재정의 시 $\delta_\mathrm{eff}=0$ (Cat A, L-ACTION-DELTA-EFF-ZERO).

**CV-1.15로 해소되지 않은 블로커**:

- Sinkhorn scaling gap: $\|M^{\mathrm{sink}}(K_{t\to r}) - M_1 M_2\|_\infty$의 bound.
- 이것은 cost level 문제가 아니라 **normalization level 문제**이다.

**OP-0012-SINK 해소를 위해 여전히 필요한 것**:

| Lemma | 내용 | 현재 상태 |
|---|---|---|
| L-δ_eff-SINK | Sinkhorn plan gap의 sup norm bound | Cat C / OPEN |
| L-Eff-Sinkhorn | $M^{\mathrm{sink}}(K_{t\to r})\approx M_1 M_2$ 조건 | Cat C / OPEN |

---

## §7. 한국어 최종 보고서

### CV-1.15 완료 보고

**목표**: SCC temporal identity의 cost 구조를 endpoint similarity에서 action-based path inheritance로 전환하고, 이를 바탕으로 temporal composition의 수학적 근거를 확립한다.

**완료 사항**:

1. **Endpoint cost 실패 증명 (Cat A)**  
   $c^\mathrm{end}(x,z)=\|z-x\|^2$는 temporal composition과 호환되지 않는다. 반례: $x=0,z=2$에서 좌변 $4$, 우변 $\leq 2$. Time-normalized cost $\|z-x\|^2/(r-t)$는 등속 경로에서 additive (L-ACTION-NORMALIZATION).

2. **Action cost 정의 및 admissibility (Cat A)**  
   SCC fingerprint action $a_i(x,y)=d^2/\Delta t + \gamma\|\Delta\varphi\|^2/\Delta t$는 $a_i\geq0$ + additive 조건 만족 (L-FINGERPRINT-ACTION-ADMISSIBLE).

3. **T-ACT-DP — Hard-min Bellman DP (Cat A, 핵심)**  
   $c_{i\to k}^{\mathrm{act}}=\min_y[c_{i\to j}^{\mathrm{act}}+c_{j\to k}^{\mathrm{act}}]$. 양방향 부등식 증명 완결. 이 결과로 $\delta_\mathrm{eff}=0$ (action cost 재정의 시).

4. **T-ACT-GIBBS — Gibbs kernel semigroup (Cat A, 핵심)**  
   $K_{i\to k}=K_{i\to j}K_{j\to k}$ (행렬 곱). Chapman-Kolmogorov path-integral 분해. Soft-min recursion 도출. $\delta_\mathrm{eff}^\varepsilon=0$ (L-SOFT-ACTION-DELTA-EFF-ZERO).

5. **Sinkhorn plan semigroup 실패 증명 (OPEN — proved failure)**  
   $M_1 M_2 = \mathrm{diag}(a_1)K_{ts}\mathrm{diag}(b_1\odot a_2)K_{sr}\mathrm{diag}(b_2)$에서 $b_1\odot a_2\neq c\cdot I$ generically → semigroup 붕괴. 이것이 OP-0012-SINK가 OPEN으로 유지되는 근본 이유.

6. **CV-1.14와 연결 (Cat B 조건부)**  
   T-ACT-GIBBS (Cat A) + T-CC-StableK-Kernel (Cat B, CV-1.14) → T-ACT-KERNEL-COMP→REL (Cat B): $M$을 Gibbs kernel로 재정의 시 relation 합성 성립.

**미완 사항**:
- OP-0012-SINK: Sinkhorn scaling gap bound 필요 (Cat C / OPEN).
- exp89 실험 구현: 이론 검증용.
- canonical 정의 변경 결정: action kernel vs Sinkhorn plan 선택 (CV-1.16 이후).

---

## §8. CV-1.15 최소 승격 문장

canonical.md §13 CV-1.15 항목으로 삽입 가능한 최소 문장:

---

> **CV-1.15 (Action-Based Temporal Succession Package, 2026-05-12)**.
> SCC fingerprint action $a_i(x,y)=d_i^2/\Delta t_i+\gamma\|\Delta\varphi\|^2/\Delta t_i$에 대해 두 결과를 증명한다.
>
> **T-ACT-DP** (Cat A): 유한 site set에서 hard-min action cost는 Bellman 원리를 만족한다:
> $c_{i\to k}^{\mathrm{act}}(x,z)=\min_{y}[c_{i\to j}^{\mathrm{act}}(x,y)+c_{j\to k}^{\mathrm{act}}(y,z)]$.
>
> **T-ACT-GIBBS** (Cat A): Gibbs kernel $K_{\ell,\ell+1}=\exp(-a_\ell/\varepsilon)$는 행렬 곱으로 합성된다:
> $K_{i\to k}=K_{i\to j}K_{j\to k}$.
>
> 이 두 결과로 action cost level에서 $\delta_\mathrm{eff}=0$ (정확히)이 성립한다.
> 단, Sinkhorn-scaled plan의 semigroup은 일반적으로 성립하지 않는다 (OP-0012-SINK OPEN 유지).

---

*작성: 2026-05-12.*
