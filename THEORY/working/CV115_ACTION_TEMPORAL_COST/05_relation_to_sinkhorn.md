---
id: ACT-05
type: working/theory
status: open — Sinkhorn 분리 + OPEN 명시
created: 2026-05-12
scope: raw Gibbs kernel vs Sinkhorn-scaled plan 구분,
       T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY,
       P-SINKHORN-STABILITY-CONDITIONAL
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 05. Raw Gibbs Kernel과 Sinkhorn Plan의 관계

---

## §1. 두 수준의 엄격한 구분

| 수준 | 대상 | 성질 | 판정 |
|---|---|---|---|
| **Raw action cost** | $c_{i\to k}^{\mathrm{act}}(x,z)$ | Bellman DP 정확 성립 (T-ACT-DP) | **Cat A** |
| **Raw Gibbs kernel** | $K_{i\to k}(x,z)$ | $K_{i\to k}=K_{i\to j}K_{j\to k}$ 정확 성립 (T-ACT-GIBBS) | **Cat A** |
| **Sinkhorn-scaled plan** | $M_{i\to k}^{\mathrm{sink}} = \mathrm{diag}(a)\,K_{i\to k}\,\mathrm{diag}(b)$ | semigroup generically **fails** | **OPEN** |

SCC canonical.md §8.5의 현재 정의:

$$M_{t\to s} = \mathrm{Sinkhorn}(u_t,\, u_s,\, c[u_t,u_s])$$

즉 SCC에서 $M_{t\to s}$는 raw Gibbs kernel이 아니라 **Sinkhorn-scaled plan**이다.

---

## §2. T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY

### 문장

> **T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY** (proved failure):
>
> Sinkhorn-scaled plan
>
> $$M^{\mathrm{sink}}(K;\,u,v) = \mathrm{diag}(a)\,K\,\mathrm{diag}(b)$$
>
> (단 $(a,b)$는 marginal $(u,v)$에 맞춘 Sinkhorn scaling 벡터)에 대해:
>
> $$M^{\mathrm{sink}}(K_{t\to s};\,u_t,u_s)\;\cdot\;M^{\mathrm{sink}}(K_{s\to r};\,u_s,u_r) \;\;\neq\;\; M^{\mathrm{sink}}(K_{t\to r};\,u_t,u_r)$$
>
> 가 일반적으로 성립한다.

### Algebraic Argument

**표기**:

$$M_1 = \mathrm{diag}(a_1)\,K_{t\to s}\,\mathrm{diag}(b_1), \quad M_2 = \mathrm{diag}(a_2)\,K_{s\to r}\,\mathrm{diag}(b_2)$$

**곱 전개**:

$$M_1 M_2 = \mathrm{diag}(a_1)\,K_{t\to s}\,\underbrace{\mathrm{diag}(b_1)\,\mathrm{diag}(a_2)}_{=\,\mathrm{diag}(b_1\odot a_2)}\,K_{s\to r}\,\mathrm{diag}(b_2)$$

T-ACT-GIBBS에 의해 $K_{t\to r} = K_{t\to s}K_{s\to r}$이므로:

$$M^{\mathrm{sink}}(K_{t\to r}) = \mathrm{diag}(a_3)\,K_{t\to s}K_{s\to r}\,\mathrm{diag}(b_3)$$

**등호 조건**:

$M_1 M_2 = M^{\mathrm{sink}}(K_{t\to r})$이 성립하려면:

$$\mathrm{diag}(a_1)\,K_{t\to s}\,\mathrm{diag}(b_1\odot a_2)\,K_{s\to r}\,\mathrm{diag}(b_2)
= \mathrm{diag}(a_3)\,K_{t\to s}\,K_{s\to r}\,\mathrm{diag}(b_3)$$

이것이 일반 $K$에 대해 성립하려면 $\mathrm{diag}(b_1\odot a_2) = c\cdot I$, 즉:

$$b_{1,i}\cdot a_{2,i} = c \quad\text{(모든 } i \text{에 대해 동일한 상수)}$$

**왜 이것이 일반적으로 실패하는가**:

- $b_1$은 $K_{t\to s}$와 marginal $(u_t, u_s)$에 의해 결정된다.
- $a_2$는 $K_{s\to r}$와 marginal $(u_s, u_r)$에 의해 결정된다.
- 두 벡터는 **서로 다른 transport 문제**에서 독립적으로 결정된다.
- 일반적으로 $b_{1,i}\cdot a_{2,i}$는 $i$에 따라 다르다.

**반례 구성** ($|X_s| = 2$):

$X_s = \{y_1, y_2\}$, $u_s = (1/3, 2/3)$ (비균등 분포).

$$K_{t\to s} = \begin{pmatrix}e^{-1}&e^{-2}\\e^{-2}&e^{-1}\end{pmatrix}, \quad K_{s\to r} = \begin{pmatrix}e^{-1}&e^{-3}\\e^{-3}&e^{-1}\end{pmatrix}$$

$u_t=u_r=(1/2,1/2)$, $u_s=(1/3,2/3)$.

Sinkhorn 수렴 후 $b_1 = (b_{1,1}, b_{1,2})$는 $K_{t\to s}$를 row-sum $(u_t)$, col-sum $(u_s)$에 맞춤.
$a_2 = (a_{2,1}, a_{2,2})$는 $K_{s\to r}$를 row-sum $(u_s)$, col-sum $(u_r)$에 맞춤.

$u_s$가 비균등이면 $b_1$과 $a_2$가 서로 다른 방향으로 비대칭화되며
$b_{1,1}a_{2,1} \neq b_{1,2}a_{2,2}$ (수치 확인: exp89_endpoint_vs_action_temporal_cost.py).

$\Rightarrow$ $b_1 \odot a_2 \neq c\cdot\mathbf{1}$ $\Rightarrow$ $M_1 M_2 \neq M^{\mathrm{sink}}(K_{t\to r})$. $\blacksquare$

### 결론

> Sinkhorn-scaled plan은 **일반적으로 semigroup 구조를 만족하지 않는다**.  
> 이것이 OP-0012-SINK가 OPEN으로 유지되는 근본적인 algebraic 이유이다.
>
> 단, $u_s$가 균등 분포인 특수 경우 ($b_1 = a_2 = \mathbf{1}/|X_s|$) 에는 근사적으로 복원 가능할 수 있다.

**판정**: $\boxed{\text{OPEN (proved failure; generically false)}}$

---

## §3. P-SINKHORN-STABILITY-CONDITIONAL (Cat B 조건부)

### 문장

> **P-SINKHORN-STABILITY-CONDITIONAL** (Cat B, 조건부):
>
> 다음 조건을 가정하자:
>
> **(H-SINK)**: $M^{\mathrm{sink}}(K;\,u,v)$의 Lipschitz 안정성 — cost perturbation $\delta c$ 아래 induced relation $R[M^{\mathrm{sink}}]$의 변화가 margin $\Delta_\mathrm{sep}$에 의해 bound된다 (H-SINK / Sinkhorn Lipschitz lemma, 별도 결과).
>
> **(MARGIN)**: 각 단계 $\Delta_\mathrm{sep}^{ts} > \eta_{ts}$, $\Delta_\mathrm{sep}^{sr} > \eta_{sr}$ (충분한 margin).
>
> **(SMALL-SINK-GAP)**: $\|M_1 M_2 - M^{\mathrm{sink}}(K_{t\to r})\|_\infty \leq \delta_\mathrm{gap}$ (semigroup gap이 작음; 충분히 작은 $u_s$ 비균등성 등 추가 조건 필요).
>
> 결론:
>
> $$R[M^{\mathrm{sink}}(K_{t\to r})] \approx R[M^{\mathrm{sink}}(K_{t\to s})]\circ R[M^{\mathrm{sink}}(K_{s\to r})]$$
>
> 더 정확히, $\delta_\mathrm{gap} < (\Delta_\mathrm{sep} - \eta)/C$이면 induced relation이 보존된다.

### Cat B 판정 이유

- **(H-SINK)** 조건이 아직 CV에서 명시적으로 증명되지 않았다.
- **(SMALL-SINK-GAP)** 조건은 $u_s$의 균등성, site 수, $\varepsilon$ 등에 의존하며 일반 bound가 없다.
- §2에서 semigroup failure를 대수적으로 증명했으므로, 이 조건부 결과는 **예외적 상황에서의 approximate 결과**이다.

**판정**: $\boxed{\text{Cat B (조건부)}}$ — H-SINK + MARGIN + SMALL-SINK-GAP 조건 하에서

---

## §4. 문제 구조 재정리

### OP-0012-SINK blocker 분석

OP-0012-SINK의 핵심: "독립 Sinkhorn $M_{t\to r} = \mathrm{Sinkhorn}(u_t,u_r,c[u_t,u_r])$와 composed relation이 같은가?"

이번 CV-1.15 분석이 보여주는 것:

```
Level 1 — Action cost:
  c^act_{i→k} = min_y[c^act_{i→j} + c^act_{j→k}]
  (T-ACT-DP, Cat A, 정확히 성립)

Level 2 — Raw Gibbs kernel:
  K_{i→k} = K_{i→j} K_{j→k}
  (T-ACT-GIBBS, Cat A, 정확히 성립)

Gap ↓  (diag(b₁⊙a₂) ≠ c·I, generically)

Level 3 — Sinkhorn-scaled plan:
  M^sink(K_{i→k}) ≠? M^sink(K_{i→j}) M^sink(K_{j→k})
  (T-SINKHORN-PLAN-SEMIGROUP-FAILS, OPEN)
```

**결론**:

> 문제는 더 이상 cost-level $\delta_\mathrm{eff}$가 아니다.
> **cost level과 raw kernel level에서는 정확히 닫혀 있다** (CV-1.15 Cat A).
> 남은 열린 문제는 **Sinkhorn scaling gap** — $M^{\mathrm{sink}}$의 곱이 $M^{\mathrm{sink}}(K_{t\to r})$과 얼마나 다른가이다.

---

## §5. Gibbs Kernel 재정의 경로 (T-ACT-KERNEL-COMP→REL, Cat B)

만약 SCC에서 $M_{t\to s}$를 Sinkhorn plan 대신 raw Gibbs kernel $K_{t\to s}$로 재정의한다면:

- T-ACT-GIBBS (Cat A) → $K_{t\to r} = K_{t\to s}K_{s\to r}$ 정확 성립
- CV-1.14 T-CC-StableK-Kernel (Cat B) 조건 충족
- **T-ACT-KERNEL-COMP→REL** (Cat B): $R[K_{t\to r}] = R[K_{t\to s}]\circ R[K_{s\to r}]$ (stable-K + margin 조건 하)

이 경로는 이론적으로 닫혀 있으나 canonical.md §8.5의 $M_{t\to s}$ 정의 변경이 전제된다.
이 결정은 CV-1.16 이후 canonical revision으로 처리해야 한다.

---

*작성: 2026-05-12.*
