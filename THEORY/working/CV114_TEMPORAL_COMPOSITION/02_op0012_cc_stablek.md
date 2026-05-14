---
id: CC-StableK-02
type: working/theory
status: open — 증명 구조 v2 (2026-05-12, §10 독해 반영)
created: 2026-05-12
updated: 2026-05-12 (Lemma 6 범위 재분류, 두 수준 분리, Route B 폐기)
session: W7 carry-forward
scope: OP-0012-CC-StableK 주 정리 + 필요 lemma 구조
non-overclaim: 아래 정리들은 Cat A/B/C 표시 기준으로만 작성. 미증명 항목에 "proved" 사용 금지.
---

> [!nav] Linked: [[MOC_temporal_composition]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 02. 주 정리 및 Lemma 구조 — OP-0012-CC-StableK (v2)

---

## 가정 패키지

### (I_{ts}): [t,s] 구간 가정

**(A1)** 유한 연결 그래프 $G = (\mathcal{P}, E)$, 모든 시점 공유  
**(A2)** 장 허용성: $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$  
**(A3)** PersComp 비공: $K_t, K_s \geq 1$  
**(A4)** Stable-K: $K_t = K_s = K$, no birth/death/merge/split  
**(A5)** Well-separated regime: $d_\mathrm{inter}^*(t), d_\mathrm{inter}^*(s) \geq d_\mathrm{min}^* \geq 3$  
**(A6)** $M_{t \to s}$: E1–E4 허용 OT 계획, $\varepsilon_\mathrm{OT}$ 정규화  
**(A7')** Sharp-OT regime: $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^* \approx 0.45$  
**(A9)** Mass dominance: $\lambda_m \geq \kappa\,\lambda_c\,\bar c_\mathrm{intra}$, $\kappa \geq 10$  
**(DR1–2)** Sinkhorn dual-potential regularity  
**Margin**: $\Delta_\mathrm{sep}(M_{t \to s}) \geq \Delta > 0$  

### (I_{sr}): [s,r] 구간 가정

(I_{ts})와 동일 조건을 $u_s, u_r, M_{s \to r}$에 적용.  
추가로 basin containment: $u_s$가 K-성분 분지 안 **(CC-3)**.

### (I_{tr}): [t,r] 직접 구간 가정

**(A6-tr)** $M_{t \to r}$: 별도로 계산된 E1–E4 허용 OT 계획 ($t$에서 $r$로 직접).  
**주의**: $M_{t \to r} \neq M_{s \to r} \circ M_{t \to s}$ 일반적으로 성립하지 않음.

---

## 주 정리 구조: 두 수준 분리 (v2)

### 2026-05-12 업데이트: Lemma 6 범위 재분류

`03_development.md §10` 정밀 독해 결과:

> Lemma 6의 증명은 $M_{t\to r}^\mathrm{direct} := M_{s\to r} \circ M_{t\to s}$를
> **행렬 합성으로 정의**하여 사용함. 독립 Sinkhorn$(u_t, u_r)$과 비교하지 않음.

이 발견으로 정리를 두 수준으로 분리함:

---

### 수준 1: T-CC-StableK-Kernel (Cat B — 완전 증명됨)

**정리 T-CC-StableK-Kernel** (Cat B, Lemma 6의 직접 귀결).

*가정: (I_{ts}), (I_{sr}).*

*$M_{t\to r}$을 행렬 합성 $M_{s\to r} \circ M_{t\to s}$로 **정의**할 때:*

$$R_{t \to r}\!\left[M_{s\to r} \circ M_{t\to s}\right] = R_{s \to r}[M_{s\to r}] \;\circ\; R_{t \to s}[M_{t\to s}]$$

*동치: $\pi_{tr} = \pi_{sr} \circ \pi_{ts}$.*

**현재 상태**: **Cat B** — `03_development.md §10` Lemma 6으로 완전 증명됨.  
오차 항 없음 ($M_{t\to r}$이 합성으로 정의되므로 ε_comp = 0).  
**추가 작업 없음. canonical promotion 대상.**

---

### 수준 2: T-CC-StableK-Sinkhorn (Cat C → B 목표)

**정리 T-CC-StableK-Sinkhorn** (Cat C, 미해결).

*가정: (I_{ts}), (I_{sr}), (I_{tr}) 및 error dominance: $\Delta > 2\varepsilon_\mathrm{comp}$.*

*$M_{t\to r}$을 $u_t$, $u_r$에 대한 **독립적 Sinkhorn**으로 계산할 때:*

$$R_{t \to r}^\mathrm{Sinkhorn}[M_{t\to r}] = R_{s \to r}[M_{s\to r}] \;\circ\; R_{t \to s}[M_{t\to s}]$$

**현재 상태**: **Cat C** — CC-2, CC-4 미해결.  
핵심 gap: $\|M_{t\to r}^\mathrm{Sinkhorn} - M_{s\to r} \circ M_{t\to s}\|_\mathrm{TV} \leq \varepsilon_\mathrm{comp}$ bound 없음.

---

## 필요 Lemma 구조

### Lemma CC-1. Stable-K No-Event Bijection (Cat A)

**문장**: (I_{ts}) 가정 하에서 $R_{t \to s}$는 유일한 bijection $\pi_{ts}: [K] \to [K]$를 정의한다.

**증명 경로**: T-Temporal-Identity (b) Cat A (CV-1.13, canonical §13).
이미 완전 증명됨. 이 lemma는 새 증명 불필요.

**상태**: **Cat A** (T-Temporal-Identity (b)의 직접 귀결)

**의존**: T-Temporal-Identity (b) Cat A, Lemmas 4+5+8 (sharp form §3)

---

### Lemma CC-2. Sinkhorn vs Kernel-Composition TV Bound (Cat C) [v2 재명명]

**문장** (수준 2 T-CC-StableK-Sinkhorn에만 필요):

$$\left\|M_{t\to r}^\mathrm{Sinkhorn} - M_{s\to r} \circ M_{t\to s}\right\|_\mathrm{TV} \leq \varepsilon_\mathrm{comp}$$

**증명 전략 (Route A, 미완성)**:

**단계 1** [NEW NEEDED]: kernel-comp의 effective cost 계산:
$$c^\mathrm{eff}(x,z) = -\varepsilon_\mathrm{OT} \log \sum_y \frac{M_{t\to s}(x,y)\,M_{s\to r}(y,z)}{u_t(x)}$$

**단계 2** [NEW NEEDED]: $\delta_\mathrm{eff} = \|c_\mathrm{direct}(x,z) - c^\mathrm{eff}(x,z)\|_\infty$ bound.  
이것이 핵심 블로커. Stable-K + well-separated 하에서 두 cost의 차이를 bound하는 명시적 계산 없음.

**단계 3** [Cat A, Partial-H-SINK 적용가능]:  
$$\|M^\mathrm{Sinkhorn}(c_\mathrm{direct}) - M^\mathrm{Sinkhorn}(c^\mathrm{eff})\|_\mathrm{TV} \leq 2m_t \cdot \delta_\mathrm{eff}/\varepsilon_\mathrm{OT}$$

**단계 4** [NEW NEEDED]: $M^\mathrm{Sinkhorn}(c^\mathrm{eff}) \approx M_{s\to r} \circ M_{t\to s}$ 확인  
(entropic regularization과 marginal constraints의 차이 처리 필요)

**단계 5** [Cat B, Lemma 10]: TV → 성분 질량 차이:
$$|\gamma_{M^\mathrm{Sinkhorn}} - \gamma_{M^\mathrm{kernel-comp}}| \leq \varepsilon_\mathrm{comp}$$

**현재 상태**: **Cat C** — 단계 1, 2, 4 미완성.  

**수준 1 (T-CC-StableK-Kernel)에는 CC-2 불필요**: kernel-comp = 직접 사용하므로.

**의존**: Partial-H-SINK Cat A, Lemma 10 Cat B, Lemma 3-sharp Cat B

---

### Lemma CC-3. Argmax Stability under Composition (Cat A 후보)

**문장**: (I_{ts}), (I_{sr}), Lemma CC-2 결론 하에서 $\Delta > 2\varepsilon_\mathrm{comp}$이면:

$$\forall i \in [K]: \quad \arg\max_{k} \tilde{S}_{ik}^0(t \to r) = \pi_{sr}(\pi_{ts}(i))$$

**증명**: (거의 자명, 일단 Lemma CC-2가 성립하면)

가정: $\tilde{S}_{i, \pi_{sr}(\pi_{ts}(i))}^0(t \to r) \geq A - \varepsilon_\mathrm{comp}$ (Lemma CC-2)

임의의 $k \neq \pi_{sr}(\pi_{ts}(i))$에 대해:
$$\tilde{S}_{ik}^0(t \to r) \leq A - \Delta + \varepsilon_\mathrm{comp}$$
(margin 조건에서 비-최적 경로의 점수 상한)

$\Delta > 2\varepsilon_\mathrm{comp}$이면:
$$\tilde{S}_{i,\pi_{sr}(\pi_{ts}(i))}^0 - \tilde{S}_{ik}^0 \geq \Delta - 2\varepsilon_\mathrm{comp} > 0$$

따라서 argmax는 $\pi_{sr}(\pi_{ts}(i))$. $\square$

**현재 상태**: **Cat A 후보** — Lemma CC-2에 조건부. Lemma CC-2가 Cat B이므로 이 lemma도 현재 Cat B에 제한.

**의존**: Lemma CC-2 (Cat B), margin algebra (자명)

---

### Lemma CC-4. Composition Error Bound (Cat C → Cat B 경로) [핵심 NEW lemma]

**문장**: (I_{ts}), (I_{sr}) 가정 하에서 합성 오차 ε_comp가 다음으로 bound됨:

$$\varepsilon_\mathrm{comp} \leq \frac{2 M_\mathrm{tot} \cdot \delta_\mathrm{comp}}{\varepsilon_\mathrm{OT} \cdot \min_i m_i^s}$$

여기서 $\delta_\mathrm{comp}$는 두 단계 cost function의 등가 perturbation 크기.

**증명 전략 (후보, 미검증)**:

Route A (TV bound 경유):
1. Lemma 9 (Partial-H-SINK, Cat A): $\|M^* - M^{*'}\|_\mathrm{TV} \leq M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$
2. 합성 OT 계획 $\hat{M}_{t \to r}$ (marginal composition 근사)와  
   실제 계획 $M_{t \to r}$ 사이의 TV distance를 Lemma 9로 bound
3. Lemma 10 (Component confinement, Cat B): 성분 질량 차이로 전환
4. 최종 정규화 점수 오차로 변환

~~Route B (self-referential cost)~~: **폐기 (2026-05-12)**

canonical.md §8.5 명시:
> "A fully self-referential transport realization is an open problem.
> The semigroup/composition property is NOT proved."

self-referential cost $c(x,y; u_t, u_s)$와 $c(x,z; u_t, u_r)$는 동일하지 않음.  
$c(x,z; u_t, u_r) \neq c(x,y;u_t,u_s) + c(y,z;u_s,u_r)$.  
따라서 self-referential regime에서도 $\varepsilon_\mathrm{comp} \neq 0$ 일반적.  
"$\varepsilon_\mathrm{comp} = 0$" 주장 완전 폐기.

**현재 상태**: **Cat C** — Route A만 유효, 단계 1/2/4 미완성.

**의존**: Lemma 9 (Cat A), Lemma 10 (Cat B), D-CC-8 (ε_comp 정의)

---

## 정리 증명 개요 (v2)

### 수준 1 (Cat B, 완전)

```
CC-1 (Cat A)         Lemma 6 (Cat B)
    ↓                      ↓
  π_{ts}, π_{sr}    R[M_{s→r}∘M_{t→s}] = R[M_{s→r}]∘R[M_{t→s}]
    ↓                      ↓
         T-CC-StableK-Kernel (Cat B)
              M_{t→r} := M_{s→r}∘M_{t→s} 기준
```

### 수준 2 (Cat C, 미해결)

```
CC-1 (Cat A)     CC-4 (Cat C: δ_eff bound)
    ↓                   ↓
  π_{ts}, π_{sr}   ε_comp bound
    ↓                   ↓
         CC-2 (Cat C: Sinkhorn vs kernel-comp TV)
                    ↓
         CC-3 (Cat B: argmax stability, CC-2 조건부)
                    ↓
     T-CC-StableK-Sinkhorn: R[Sinkhorn(u_t,u_r)] = R[M_{s→r}]∘R[M_{t→s}]
```

---

## Lemma별 Cat 판정 요약 (v2)

| Lemma / 정리 | 내용 | 현재 상태 | 블로커 |
|---|---|---|---|
| CC-1 | Stable-K bijection 존재 (단일 구간) | **Cat A** | 없음 |
| Lemma 6 | $R[M_{s\to r}\circ M_{t\to s}] = R[M_{s\to r}]\circ R[M_{t\to s}]$ | **Cat B (완전)** | 없음 |
| **T-CC-StableK-Kernel** | Kernel-comp 기준 합성 등식 | **Cat B** | 없음 (Lemma 6 귀결) |
| CC-2 | Sinkhorn vs kernel-comp TV bound | **Cat C** | δ_eff 계산 (단계 1,2,4) |
| CC-3 | Argmax stability | **Cat B** (CC-2 조건부) | CC-2 |
| CC-4 | ε_comp Route A (Route B 폐기) | **Cat C** | δ_eff bound |
| **T-CC-StableK-Sinkhorn** | 독립 Sinkhorn 기준 합성 등식 | **Cat C** | CC-2 + CC-4 |

---

## 약화 버전: Margin-Stable Equivalence

strict equality ($R_{t→r} = R_{s→r} \circ R_{t→s}$)가 불가능한 경우,  
다음 약화 버전으로 후퇴:

**Margin-stable equivalence** $\equiv_\delta$:

$$R_{t \to r}^\mathrm{direct} \equiv_\delta R_{s \to r} \circ R_{t \to s}$$

의미: 양변의 bijection이 margin $\delta = \Delta - 2\varepsilon_\mathrm{comp} > 0$ 이내에서 일치.

이 버전은 Lemma CC-3의 argmax gap ($\Delta - 2\varepsilon_\mathrm{comp}$)으로 직접 표현됨.  
strict equality보다 약하지만 Cat B 달성이 더 용이.

---

## 비과대 주장 등록 (Non-Overclaim, v2)

1. **T-CC-StableK-Kernel**: Cat B (Lemma 6 귀결). 단, $M_{t\to r} := M_{s\to r}\circ M_{t\to s}$로 **정의**할 때만 성립. 독립 Sinkhorn에는 적용 불가.
2. **T-CC-StableK-Sinkhorn**: Cat C — 증명되지 않았음. CC-2, CC-4 미완성.
3. **Route B "ε_comp=0"**: 폐기. canonical §12에서 semigroup property가 open problem으로 명시됨.
4. **CC-4 ε_comp formula**: Route A의 δ_eff 계산이 핵심 미결. ε_comp formula는 추측.
5. K-jump 경우는 완전히 제외됨.
6. σ-inheritance, Wigner, Package II와 무관.
7. canonical 수정 없음.

---

*작성: 2026-05-12. 모든 "Cat B 후보" 항목은 완전 증명 없음을 명시.*
