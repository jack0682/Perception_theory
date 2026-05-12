---
id: ACT-04
type: working/theory
status: open — T-ACT-GIBBS 증명
created: 2026-05-12
scope: Gibbs kernel 정의, T-ACT-GIBBS, soft-min recursion,
       L-SOFTMIN-HARDMIN-BOUND, L-SOFT-ACTION-DELTA-EFF-ZERO
---

# 04. Soft-Min / Gibbs Kernel Semigroup

---

## §1. Gibbs Kernel 정의

### Local Gibbs Kernel

$$\boxed{K_{\ell,\ell+1}(x,y) = \exp\!\left(-\frac{a_\ell(x,y)}{\varepsilon}\right)}, \quad \varepsilon > 0, \; x\in X_\ell, \; y\in X_{\ell+1}$$

$\varepsilon > 0$: 온도 파라미터 (entropic regularization). $\varepsilon \to 0$에서 soft-min → hard-min.

### Long-Horizon Path-Sum Gibbs Kernel

$$\boxed{K_{i\to k}(x,z) = \sum_{\substack{(x_i,\ldots,x_k):\\ x_i=x,\, x_k=z}} \exp\!\left(-\frac{\mathcal{A}_{i:k}(x_i,\ldots,x_k)}{\varepsilon}\right)}$$

이것은 모든 $x \to z$ 경로에 대해 $e^{-\mathrm{action}/\varepsilon}$ 가중합이다.

**행렬 표기**: $K_{i\to k} \in \mathbb{R}^{|X_i| \times |X_k|}_{\geq 0}$ (nonneg 행렬).

단계별 적용:
$$K_{i\to i+1} = K_{i,i+1} \quad\text{(local Gibbs kernel)}$$
$$K_{i\to i+2}(x,z) = \sum_{y\in X_{i+1}} K_{i,i+1}(x,y)\,K_{i+1,i+2}(y,z)$$

### Soft-Min Action Cost

$$\boxed{c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon\log K_{i\to k}(x,z)}$$

---

## §2. Theorem T-ACT-GIBBS — Gibbs Kernel Semigroup

### 문장

> **T-ACT-GIBBS** (Cat A 후보):
>
> 가정:
> - $X_i, X_j, X_k$: 유한 집합 ($i < j < k$).
> - $\mathcal{A}_{i:k}$: additive path action.
> - $\varepsilon > 0$.
>
> 결론 (행렬 등식):
>
> $$\boxed{K_{i\to k} = K_{i\to j}\, K_{j\to k}}$$
>
> 성분별:
>
> $$K_{i\to k}(x,z) = \sum_{y\in X_j} K_{i\to j}(x,y)\, K_{j\to k}(y,z)$$

---

### 증명

#### 경로 분해

$K_{i\to k}(x,z)$를 경로 합으로 전개한다.

모든 경로 $(x_i,\ldots,x_k)$는 $t_j$에서 유일한 중간점 $y = x_j \in X_j$를 가진다.
따라서 전체 경로 집합은 $y$별로 분리된다:

$$\{(x_i,\ldots,x_k) : x_i=x,\,x_k=z\} = \bigsqcup_{y\in X_j} \{(x_i,\ldots,x_j,\ldots,x_k):x_j=y\}$$

#### 합산 분해

$$K_{i\to k}(x,z) = \sum_{y\in X_j}\;\sum_{\substack{(x_i,\ldots,x_j):\\ x_i=x,\,x_j=y}}\;\sum_{\substack{(x_j,\ldots,x_k):\\ x_j=y,\,x_k=z}} \exp\!\left(-\frac{\mathcal{A}_{i:k}}{\varepsilon}\right)$$

#### Action Additivity 적용

Path action additivity: $\mathcal{A}_{i:k} = \mathcal{A}_{i:j} + \mathcal{A}_{j:k}$이므로:

$$\exp\!\left(-\frac{\mathcal{A}_{i:k}}{\varepsilon}\right) = \exp\!\left(-\frac{\mathcal{A}_{i:j}}{\varepsilon}\right)\cdot\exp\!\left(-\frac{\mathcal{A}_{j:k}}{\varepsilon}\right)$$

이 인수분해로 내부 이중합이 분리된다:

$$K_{i\to k}(x,z) = \sum_{y\in X_j} \underbrace{\left[\sum_{\substack{(x_i,\ldots,x_j):\\ x_i=x,\, x_j=y}} \exp\!\left(-\frac{\mathcal{A}_{i:j}}{\varepsilon}\right)\right]}_{=\,K_{i\to j}(x,y)} \underbrace{\left[\sum_{\substack{(x_j,\ldots,x_k):\\ x_j=y,\, x_k=z}} \exp\!\left(-\frac{\mathcal{A}_{j:k}}{\varepsilon}\right)\right]}_{=\,K_{j\to k}(y,z)}$$

#### 결론

$$K_{i\to k}(x,z) = \sum_{y\in X_j} K_{i\to j}(x,y)\,K_{j\to k}(y,z) = \bigl[K_{i\to j}\,K_{j\to k}\bigr]_{xz}$$

행렬 곱 정의에 의해: $K_{i\to k} = K_{i\to j}\,K_{j\to k}$. $\blacksquare$

---

### Soft-Min Recursion 도출

$K_{i\to j}(x,y) = \exp(-c_{i\to j}^{\varepsilon}(x,y)/\varepsilon)$ (정의)이므로:

$$K_{i\to k}(x,z) = \sum_{y\in X_j} \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y) + c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

양변에 $-\varepsilon\log$를 취하면:

$$\boxed{c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon\log\sum_{y\in X_j}\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y) + c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)}$$

이것이 soft-min recursion이다. $\varepsilon\to 0$ 극한에서:

$$c_{i\to k}^{\varepsilon}(x,z) \;\xrightarrow{\;\varepsilon\to0\;}\; \min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr] = c_{i\to k}^{\mathrm{act}}(x,z) \quad\text{(T-ACT-DP)}$$

---

### 검증 메모

| 항목 | 확인 |
|---|---|
| Chapman-Kolmogorov | T-ACT-GIBBS는 Chapman-Kolmogorov 방정식의 path-integral (이산) 버전 |
| Transfer matrix | 물리에서 transfer matrix method와 동일한 수학 구조 |
| $\varepsilon>0$ 필요 | $\log$ 정의 위해 $K_{i\to k}>0$ 필요; $a_\ell \geq 0$ → $K_{\ell,\ell+1}>0$ → $K_{i\to k}>0$ |
| Raw vs Sinkhorn | **$K_{i\to k}$는 비정규화 (raw) kernel.** Sinkhorn scaling 이전 상태. Sinkhorn scaling 후에는 semigroup 깨짐 (05 파일 §2 참조). |

**판정**: $\boxed{\text{Cat A}}$ (유한 site set, $\varepsilon>0$, additive action)

---

## §3. Lemma L-SOFTMIN-HARDMIN-BOUND

### 문장

> 실수열 $a_1,\ldots,a_N \in \mathbb{R}$에 대해 soft-min
>
> $$\operatorname{smin}_\varepsilon(a) = -\varepsilon\log\sum_{i=1}^N e^{-a_i/\varepsilon}$$
>
> 는:
>
> $$\boxed{\min_i a_i \;-\; \varepsilon\log N \;\leq\; \operatorname{smin}_\varepsilon(a) \;\leq\; \min_i a_i}$$

### 증명

$m = \min_i a_i$로 놓는다.

**상한** ($\operatorname{smin}_\varepsilon \leq m$):

$$\sum_{i=1}^N e^{-a_i/\varepsilon} \geq e^{-m/\varepsilon}$$

(최솟값 항이 포함되므로.)

$$\Rightarrow \quad -\varepsilon\log\!\sum_i e^{-a_i/\varepsilon} \leq -\varepsilon\log e^{-m/\varepsilon} = m \quad \checkmark$$

**하한** ($\operatorname{smin}_\varepsilon \geq m - \varepsilon\log N$):

$$\sum_{i=1}^N e^{-a_i/\varepsilon} \leq N \cdot e^{-m/\varepsilon}$$

(모든 항이 $e^{-m/\varepsilon}$ 이하.)

$$\Rightarrow \quad -\varepsilon\log\!\sum_i e^{-a_i/\varepsilon} \geq -\varepsilon\log(N\,e^{-m/\varepsilon}) = m - \varepsilon\log N \quad \checkmark$$

$\blacksquare$

**Tightness**:
- 상한: $a_i$가 모두 $m$이면 $\operatorname{smin}_\varepsilon = m$.
- 하한: $a_i$가 균등분포이면 $\operatorname{smin}_\varepsilon \to m - \varepsilon\log N$.

**Action cost 적용**:

$N = |X_j|$로 하면:

$$\left|c_{i\to k}^{\varepsilon}(x,z) - c_{i\to k}^{\mathrm{act}}(x,z)\right| \leq \varepsilon\log|X_j|$$

$\varepsilon \to 0$ 시 수렴: $c_{i\to k}^{\varepsilon} \to c_{i\to k}^{\mathrm{act}}$.

**판정**: $\boxed{\text{Cat A}}$

---

## §4. Lemma L-SOFT-ACTION-DELTA-EFF-ZERO

### 문장

> Soft-min direct cost $c_{i\to k}^{\varepsilon} = -\varepsilon\log K_{i\to k}$와 soft effective cost
>
> $$c_{i\to k}^{\mathrm{eff},\varepsilon}(x,z) = -\varepsilon\log\!\sum_{y\in X_j}\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$
>
> 에 대해:
>
> $$\boxed{c_{i\to k}^{\varepsilon} = c_{i\to k}^{\mathrm{eff},\varepsilon}, \quad \delta_\mathrm{eff}^{\varepsilon} = 0}$$

### 증명

T-ACT-GIBBS에 의해:

$$K_{i\to k}(x,z) = \sum_{y\in X_j} K_{i\to j}(x,y)\,K_{j\to k}(y,z)$$

$K_{i\to j}(x,y) = e^{-c_{i\to j}^{\varepsilon}(x,y)/\varepsilon}$로 대입:

$$K_{i\to k}(x,z) = \sum_{y}\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

양변 $-\varepsilon\log$:

$$c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon\log\!\sum_y\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}+c_{j\to k}^{\varepsilon}}{\varepsilon}\right) = c_{i\to k}^{\mathrm{eff},\varepsilon}(x,z)$$

모든 $x,z$에서 등식 → $\delta_\mathrm{eff}^{\varepsilon} = 0$. $\blacksquare$

**요약**:

| | Hard-min ($\varepsilon\to0$) | Soft-min (임의 $\varepsilon>0$) |
|---|---|---|
| 근거 | T-ACT-DP | T-ACT-GIBBS |
| $\delta_\mathrm{eff}$ | $0$ (exact) | $0$ (exact) |

**판정**: $\boxed{\text{Cat A}}$

---

*작성: 2026-05-12.*
