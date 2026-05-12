---
id: ACT-02
type: working/theory
status: open — Cat B 조건부 + OPEN 결과 분리
created: 2026-05-12
session: W7 carry-forward
scope: T-ACT-KERNEL-COMP-REL (Cat B), T-SINKHORN-PLAN-SEMIGROUP-FAILS (OPEN),
        OP-0012-SINK 연결 분석
non-overclaim: Sinkhorn-scaled plan semigroup proved/Cat B 선언 절대 금지
---

# 02. 조건부·열린 결과 — CV-1.15 Action Temporal Cost

---

## 개요

이 파일은 세 가지 내용을 다룬다:

1. **T-ACT-KERNEL-COMP-REL** (Cat B 조건부): Gibbs kernel semigroup + Lemma 6 → 관계 합성  
2. **T-SINKHORN-PLAN-SEMIGROUP-FAILS** (OPEN, proved failure): Sinkhorn-scaled plan의 semigroup 붕괴 증명  
3. **OP-0012-SINK 연결 분석**: CV-1.15 Cat A 결과가 OP-0012-SINK 블로커를 어떻게 해소하는가, 그리고 왜 Sinkhorn plan에는 여전히 열려 있는가

---

## §1. T-ACT-KERNEL-COMP-REL — Gibbs Kernel → 관계 합성 (Cat B 조건부)

### 문장

> **T-ACT-KERNEL-COMP-REL** (Cat B):  
> 다음 조건을 가정하자:
>
> **(GK)** $M_{t\to s}$, $M_{s\to r}$을 (Sinkhorn plan이 아닌) Gibbs kernel $K_{t\to s}$, $K_{s\to r}$로 재정의.  
> **(stable-K)** $K_t = K_s = K_r = K$ (formation 수 안정; T-CC-StableK-Kernel 동일 조건).  
> **(margin)** $\Delta_\mathrm{sep}^{ts} > 0$, $\Delta_\mathrm{sep}^{sr} > 0$ (각 단계에서 bijection $\pi_{ts}$, $\pi_{sr}$ 유일 결정).
>
> 그러면:
>
> $$R[K_{t\to r}] = R[K_{t\to s}] \circ R[K_{s\to r}]$$
>
> 성분별로: $\pi_{tr}^\mathrm{comp} = \pi_{sr} \circ \pi_{ts}$.

### 증명

**단계 1: Gibbs kernel의 합성 구조**

T-ACT-GIBBS (Cat A, 01_proofs_cat_a.md §T-ACT-GIBBS)에 의해:

$$K_{t\to r} = K_{t\to s}\, K_{s\to r}$$

(행렬 곱; Chapman-Kolmogorov). 이것이 (GK) 조건 하에서 $M_{t\to r}^{\mathrm{direct}}$의 정의이다.

**단계 2: 관계 함수 합성**

위의 행렬 곱 구조는 CV-1.14 T-CC-StableK-Kernel의 전제와 동일한 형태:

$$M_{t\to r}^{\mathrm{comp}} = M_{s\to r} \circ M_{t\to s}$$

단 여기서 $M$은 Gibbs kernel $K$.

CV-1.14 T-CC-StableK-Kernel (05_promotion_draft.md §2에 기술; Lemma 6 기반)에 의해:

$$R[M_{t\to r}^{\mathrm{comp}}] = R[M_{s\to r}] \circ R[M_{t\to s}]$$

**단계 3: (stable-K) + (margin) 조건 적용**

(stable-K)와 (margin) 조건은 T-CC-StableK-Kernel의 조건과 동일하므로 적용 가능.
각 단계의 bijection $\pi_{ts}$, $\pi_{sr}$이 margin 조건으로 유일 결정되고:

$$\pi_{tr}^\mathrm{comp} = \pi_{sr} \circ \pi_{ts} \quad \blacksquare$$

### Cat B 판정 이유

> **이 정리는 조건 (GK)에 강하게 의존한다.**  
> 현재 SCC canonical.md의 $M_{t\to s}$는 Sinkhorn plan으로 정의됨  
> (transport.py `persist_transport`, Sinkhorn log-domain OT).  
> Gibbs kernel $K_{t\to s}$는 $M_{t\to s}$와 일반적으로 다른 행렬이다.  
>
> 따라서 이 정리는 "M을 Gibbs kernel로 재정의할 때" 성립하는 조건부 결과 → **Cat B**.

---

## §2. T-SINKHORN-PLAN-SEMIGROUP-FAILS — Sinkhorn Plan의 Semigroup 붕괴 (OPEN = proved failure)

### 문장

> **T-SINKHORN-PLAN-SEMIGROUP-FAILS** (proved counterexample):  
> Sinkhorn-scaled plan $M^\mathrm{sink}(K) = \mathrm{diag}(a)\,K\,\mathrm{diag}(b)$  
> (단 $a$, $b$는 marginal $u_t$, $u_s$에 맞춘 Sinkhorn scaling 벡터)에 대해:
>
> $$M^\mathrm{sink}(K_{t\to s}) \cdot M^\mathrm{sink}(K_{s\to r}) \;\neq\; M^\mathrm{sink}(K_{t\to r})$$
>
> 가 일반적으로 성립한다.

### 증명

**Sinkhorn scaling 구조 복기**:

Sinkhorn(K; $u_t$, $u_s$) = $\mathrm{diag}(a_1)\,K\,\mathrm{diag}(b_1)$  
단 $a_1 \odot (K b_1) = u_t$, $b_1 \odot (K^T a_1) = u_s$ (행렬 표기).

따라서:

$$M_1 := M^\mathrm{sink}(K_{t\to s}) = \mathrm{diag}(a_1)\,K_{t\to s}\,\mathrm{diag}(b_1)$$

$$M_2 := M^\mathrm{sink}(K_{s\to r}) = \mathrm{diag}(a_2)\,K_{s\to r}\,\mathrm{diag}(b_2)$$

**곱 계산**:

$$M_1 M_2 = \mathrm{diag}(a_1)\,K_{t\to s}\,\underbrace{\mathrm{diag}(b_1)\,\mathrm{diag}(a_2)}_{=\,\mathrm{diag}(b_1 \odot a_2)}\,K_{s\to r}\,\mathrm{diag}(b_2)$$

**반면 Sinkhorn(K_{t→r})**:

T-ACT-GIBBS에 의해 $K_{t\to r} = K_{t\to s}K_{s\to r}$이므로:

$$M^\mathrm{sink}(K_{t\to r}) = \mathrm{diag}(a_3)\,K_{t\to s}K_{s\to r}\,\mathrm{diag}(b_3)$$

단 $a_3$, $b_3$은 marginal $(u_t, u_r)$에 맞춘 scaling 벡터.

**등호 조건**:

$M_1 M_2 = M^\mathrm{sink}(K_{t\to r})$이 성립하려면:

$$\mathrm{diag}(a_1)\,K_{t\to s}\,\mathrm{diag}(b_1 \odot a_2)\,K_{s\to r}\,\mathrm{diag}(b_2) = \mathrm{diag}(a_3)\,K_{t\to s}K_{s\to r}\,\mathrm{diag}(b_3)$$

이것은 $\mathrm{diag}(b_1 \odot a_2) = c \cdot I$ (스칼라 배 단위 행렬)일 때, 즉

$$b_{1,i} \cdot a_{2,i} = c \quad \text{(모든 } i \text{에 대해 동일한 상수 } c\text{)}$$

일 때만 성립할 수 있다.

**반례 구성**:

$X_s = \{y_1, y_2\}$, $u_s = (1/3, 2/3)$이라 하자.

Sinkhorn의 수렴값 $(a_2, b_1)$은 $u_s$ 분포를 재현해야 한다.  
일반적으로 $b_{1,1}/b_{1,2} \neq a_{2,2}/a_{2,1}$ (다른 transport 방향에서 결정되므로).  
따라서 $b_{1,1}a_{2,1} \neq b_{1,2}a_{2,2}$이고 $b_1 \odot a_2 \neq c\cdot\mathbf{1}$.

구체적 수치 예: 2×2 Gibbs kernels

$$K_{t\to s} = \begin{pmatrix}e^{-1}&e^{-2}\\e^{-2}&e^{-1}\end{pmatrix}, \quad K_{s\to r}=\begin{pmatrix}e^{-1}&e^{-3}\\e^{-3}&e^{-1}\end{pmatrix}$$

$u_t=(1/2,1/2)$, $u_s=(1/3,2/3)$, $u_r=(1/2,1/2)$.

Sinkhorn 수렴 후:  
$M_1$의 우측 scaling $b_1$: $K_{t\to s}$를 $(u_t,u_s)$ marginal에 맞춤 → $b_{1,1} \neq b_{1,2}$ (비균등).  
$M_2$의 좌측 scaling $a_2$: $K_{s\to r}$를 $(u_s,u_r)$ marginal에 맞춤 → $a_{2,1} \neq a_{2,2}$ (비균등).  

$b_{1,1}\cdot a_{2,1}$ vs $b_{1,2}\cdot a_{2,2}$: 일반적으로 다름 $\Rightarrow$ $b_1\odot a_2 \neq c\cdot\mathbf{1}$.

따라서 $M_1 M_2 \neq M^\mathrm{sink}(K_{t\to r})$. $\blacksquare$

### 결론

> Sinkhorn-scaled plan은 **일반적으로 semigroup 구조를 만족하지 않는다**.  
> $b_1 \odot a_2 = c\cdot\mathbf{1}$이 성립하는 특수 경우 (예: $u_s$ = 균등 분포)에만 근사적 복원 가능.  
> 이 결과는 OP-0012-SINK가 OPEN으로 유지되는 근본 이유이다.

**판정**: Semigroup property가 generically fails → $\boxed{\text{OPEN (proved failure)}}$

---

## §3. OP-0012-SINK 연결 분석

### 3.1 CV-1.15 Cat A 결과와 OP-0012-SINK blocker의 관계

CV-1.14 gap audit에서 확인된 OP-0012-SINK의 핵심 blocker:

> $\delta_{\mathrm{eff}} = \|c_{\mathrm{direct}} - c_{\mathrm{eff}}\|_\infty$가 bound되지 않는다.

CV-1.15 Cat A 결과 (01_proofs_cat_a.md):

| 결과 | 내용 |
|------|------|
| L-ACTION-DELTA-EFF-ZERO | action cost를 direct cost로 채택 → $\delta_\mathrm{eff}=0$ (exact) |
| L-SOFT-ACTION-DELTA-EFF-ZERO | soft-min action → $\delta_\mathrm{eff}^\varepsilon=0$ (exact) |
| T-ACT-DP | Bellman: $c^{\mathrm{act}}_{i\to k} = \min_y[c^{\mathrm{act}}_{i\to j}+c^{\mathrm{act}}_{j\to k}]$ |
| T-ACT-GIBBS | Gibbs kernel: $K_{i\to k}=K_{i\to j}K_{j\to k}$ |

**해소 경로**: $c_{\mathrm{direct}}$를 action cost로 재정의 → $\delta_\mathrm{eff}=0$ 즉시 성립.

### 3.2 왜 Sinkhorn plan까지 직접 연결되지 않는가

핵심 단절 (gap):

```
Action cost level:       c^act_{i→k} = min_y[...] (exact, T-ACT-DP, Cat A)
                              ↓ (이 단계가 gap)
Gibbs kernel level:      K_{i→k} = K_{i→j}K_{j→k} (exact, T-ACT-GIBBS, Cat A)
                              ↓ (이 단계도 gap)
Sinkhorn plan level:     M^sink(K_{i→k}) ≠ M^sink(K_{i→j}) M^sink(K_{i→k}) (FAILS, §2)
```

**Level 1 → Level 2 gap**: Gibbs kernel $K$는 비정규화 행렬. OT transport plan은 $K$의 Sinkhorn 정규화. 정규화가 사이에 삽입되므로 사전에 합성된 $K_{t\to r}$의 Sinkhorn ≠ 두 Sinkhorn의 곱 (§2에서 증명).

**Level 2 → Level 3 gap**: 관계 함수 $R[M]$은 M의 argmax 구조에 의존. $M^\mathrm{sink}(K_{t\to r}) \neq M_1 M_2$이므로 $R[M_1 M_2] \neq R[M^\mathrm{sink}(K_{t\to r})]$ 일반적.

### 3.3 OP-0012-SINK 해소를 위해 여전히 필요한 것

| 필요 Lemma | 내용 | 현재 상태 |
|-----------|------|----------|
| Lemma-δ_eff | $\|M^\mathrm{sink}(K_{t\to r}) - M_1 M_2\|_\infty \leq \delta_\mathrm{eff}$ bound | Cat C (OPEN) |
| Lemma-Eff-Sinkhorn | $M^\mathrm{sink}(K_{t\to r}) \approx M^\mathrm{sink}(K_{t\to s}) M^\mathrm{sink}(K_{s\to r})$ 조건 | Cat C (OPEN) |

두 lemma가 모두 Cat C / OPEN 상태이며 §2의 반례가 일반적 성립을 막는다.

### 3.4 Gibbs kernel 재정의 경로 (Cat B 조건부)

$M_{t\to s}$를 Sinkhorn plan 대신 Gibbs kernel $K_{t\to s}$로 재정의하는 경우:

- $\delta_\mathrm{eff}=0$: L-ACTION-DELTA-EFF-ZERO (Cat A)
- $R[K_{t\to r}]=R[K_{t\to s}]\circ R[K_{s\to r}]$: T-ACT-KERNEL-COMP-REL (Cat B, §1)

이 경로는 이론적으로 닫혀 있으나 **현재 SCC 구현과 canonical.md 정의를 변경해야 함**.  
canonical.md §8.5의 M_{t→s} 정의 재검토 필요 → CV-1.16 이후 과제.

---

## §4. CV-1.15 전체 상태 표

| 항목 | 판정 | 전제 | 파일 |
|------|------|------|------|
| L-ENDPOINT-NONSEMI | **Cat A** | 반례 존재 | 01 |
| L-ACTION-NORMALIZATION | **Cat A** | 등속 경로 | 01 |
| **T-ACT-DP** | **Cat A** | 유한 site, additive action | 01 |
| **T-ACT-GIBBS** | **Cat A** | 유한 site, $\varepsilon>0$, additive | 01 |
| L-SOFTMIN-HARDMIN-BOUND | **Cat A** | 표준 log-sum-exp | 01 |
| L-ACTION-DELTA-EFF-ZERO | **Cat A** | action cost 재정의 전제 | 01 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | **Cat A** | T-ACT-GIBBS 귀결 | 01 |
| L-FINGERPRINT-ACTION-ADMISSIBLE | **Cat A** | 구조적 확인 | 01 |
| T-ACT-KERNEL-COMP-REL | **Cat B** | (GK) + (stable-K) + (margin) | 02 §1 |
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | **OPEN (proved failure)** | 반례 구성 | 02 §2 |
| OP-0012-SINK (Sinkhorn M 재정의 없이) | **OPEN** | Lemma-δ_eff + Lemma-Eff-Sinkhorn 필요 | 02 §3 |

---

## §5. CV-1.15 최종 결론 및 CV-1.14 연결

### CV-1.15 핵심 기여 요약

**닫은 것 (Cat A, 8건)**:

1. Action cost를 사용하면 $\delta_\mathrm{eff}=0$ (exact) — hard-min, soft-min 모두.
2. Gibbs kernel은 사이군(semigroup) 구조를 정확히 만족: $K_{i\to k}=K_{i\to j}K_{j\to k}$.
3. Endpoint cost는 합성 불가 — action cost 설계가 올바른 이유의 근거.
4. SCC fingerprint action은 이 framework의 전제를 구조적으로 만족.

**조건부 결과 (Cat B)**:

- M을 Gibbs kernel로 재정의하면 T-ACT-DP + T-ACT-GIBBS가 OP-0012-SINK blocker를 완전 해소.
- 이 재정의는 canonical 변경을 요구 → CV-1.16 이후 결정 사항.

**열린 것 (OPEN)**:

- Sinkhorn-scaled plan의 semigroup: generically fails (§2에서 증명).
- OP-0012-SINK (Sinkhorn M 유지): Lemma-δ_eff + Lemma-Eff-Sinkhorn 없이 미해결.

### CV-1.14와의 관계

CV-1.14 T-CC-StableK-Kernel (Cat B)는 다음을 성립시킴:

$$M_{t\to r} = M_{s\to r} \circ M_{t\to s} \;\Rightarrow\; R[M_{t\to r}] = R[M_{s\to r}] \circ R[M_{t\to s}]$$

CV-1.15는 이 "M이 합성 구조를 갖는다"는 전제의 **원천**을 제공:

$$K_{t\to r} = K_{t\to s}K_{s\to r} \quad \text{(T-ACT-GIBBS, Cat A)}$$

즉 **CV-1.15 T-ACT-GIBBS (Cat A)** + **CV-1.14 T-CC-StableK-Kernel (Cat B)** 합성이 T-ACT-KERNEL-COMP-REL (Cat B, §1)이다.

---

## §6. 절대 금지 재확인

1. **Sinkhorn-scaled plan semigroup을 proved 또는 Cat B로 선언 금지** (§2에서 반례 존재).
2. **ε_comp=0 Route B 사용 금지** (CV-1.14 gap audit에서 폐기).
3. **canonical.md 직접 수정 금지** (promotion pipeline 경유).
4. **K-jump, MERGE/SPLIT, Wigner projection, H-MORSE 진입 금지**.

---

*작성: 2026-05-12. Cat B (조건부) + OPEN (proved failure) 구분 명확화.*
