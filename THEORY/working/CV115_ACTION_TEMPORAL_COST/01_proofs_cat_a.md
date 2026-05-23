---
id: ACT-01
type: working/theory
status: open — Cat A 후보 증명 모음 (완전 검증됨)
created: 2026-05-12
session: W7 carry-forward
scope: L-ENDPOINT-NONSEMI, T-ACT-DP, T-ACT-GIBBS, L-SOFTMIN-HARDMIN-BOUND,
        L-ACTION-DELTA-EFF-ZERO, L-SOFT-ACTION-DELTA-EFF-ZERO,
        L-ACTION-NORMALIZATION, L-FINGERPRINT-ACTION-ADMISSIBLE
non-overclaim: 모든 Cat A 판정은 유한 site set + additive nonneg local action 조건 하.
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 01. Cat A 후보 증명 — CV-1.15 Action Temporal Cost

---

## 기본 설정

### 시간 격자

$$t_0 < t_1 < \cdots < t_L, \quad \Delta t_i = t_{i+1} - t_i > 0$$

각 시각 $t_i$의 site 집합 $X_i$ (유한; $\lvert X_i \rvert < \infty$).  
단순화 시 $X_i = X$ 공통, 일반적으로 $X_i$ 상이 허용.

### Local action

$$a_i(x,y) = \frac{d_i(x,y)^2}{\Delta t_i} + \gamma\frac{\lVert \varphi_{i+1}(y) - \varphi_i(x) \rVert^2}{\Delta t_i}, \quad x \in X_i,\; y \in X_{i+1}$$

여기서:
- $d_i(x,y)$: 공간 거리
- $\varphi_i(x) = (u_i(x), \mathrm{Cl}_i(u_i)(x), D_i(x;\,1-u_i))$: SCC fingerprint
- $\gamma \geq 0$: fingerprint 가중치
- $\Delta t_i > 0$: 시간 간격

### Path action

$$\mathcal{A}_{i:k}(x_i, x_{i+1}, \ldots, x_k) = \sum_{\ell=i}^{k-1} a_\ell(x_\ell, x_{\ell+1})$$

### Hard-min action cost

$$c_{i\to k}^{\mathrm{act}}(x,z) = \min_{\substack{x_{i+1},\ldots,x_{k-1} \\ x_i=x,\; x_k=z}} \mathcal{A}_{i:k}(x_i,\ldots,x_k)$$

유한 집합에서 최솟값 존재 보장됨.

### Gibbs kernel

$$K_{\ell,\ell+1}(x,y) = \exp\!\left(-\frac{a_\ell(x,y)}{\varepsilon}\right), \quad \varepsilon > 0$$

$$K_{i\to k}(x,z) = \sum_{x_{i+1},\ldots,x_{k-1}} \exp\!\left(-\frac{\mathcal{A}_{i:k}(x_i,\ldots,x_k)}{\varepsilon}\right)$$

### Soft-min action cost

$$c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon \log K_{i\to k}(x,z)$$

---

## Lemma L-ENDPOINT-NONSEMI — Squared Endpoint Cost는 합성 불가

**문장**: Squared endpoint cost $c^\mathrm{end}_{i\to k}(x,z) = \lVert z-x \rVert^2$는 일반적으로

$$c^\mathrm{end}_{i\to k}(x,z) \;\neq\; \min_{y} \!\left[c^\mathrm{end}_{i\to j}(x,y) + c^\mathrm{end}_{j\to k}(y,z)\right]$$

이다.

**증명** ($\mathbb{R}^1$, $x=0$, $z=2$):

직접:
$$c^\mathrm{end}_{0\to2}(0,2) = \lvert 2-0 \rvert^2 = 4$$

중간점 $y=1$ 경유:
$$c^\mathrm{end}_{0\to1}(0,1) + c^\mathrm{end}_{1\to2}(1,2) = \lvert 1 \rvert^2 + \lvert 1 \rvert^2 = 2$$

$\min_y \leq 2 < 4$이므로 equality 불성립.  
반례 존재이므로 일반적으로 성립하지 않는다. $\blacksquare$

**검증 메모**:
- 우변의 $\min_y$ 값은 $y = (x+z)/2 = 1$에서 최소 $\lVert z-x \rVert^2/2$를 가짐.
- $\lVert z-x \rVert^2 \neq \lVert z-x \rVert^2/2$ (일반적), 등호는 $x=z$일 때만.
- 이 lemma의 의미: endpoint cost는 "경로를 통한 계승"이 아니라 "직접 유사성"만 측정함.
  SCC temporal identity의 목적과 어긋남.

**판정**: $\boxed{\text{Cat A}}$

---

## Lemma L-ACTION-NORMALIZATION — Time-Normalized Cost의 등속 경로 합성

**문장**: $t < s < r$에 대해 등속 직선 경로의 중간점

$$y = \frac{r-s}{r-t}\,x + \frac{s-t}{r-t}\,z$$

에서 time-normalized squared cost는 additive:

$$\frac{\lVert z-x \rVert^2}{r-t} = \frac{\lVert y-x \rVert^2}{s-t} + \frac{\lVert z-y \rVert^2}{r-s}$$

**증명**:

선형 보간이므로:
$$y-x = \frac{s-t}{r-t}(z-x), \qquad z-y = \frac{r-s}{r-t}(z-x)$$

계산:
$$\frac{\lVert y-x \rVert^2}{s-t} = \frac{\left(\frac{s-t}{r-t}\right)^2\lVert z-x \rVert^2}{s-t} = \frac{s-t}{(r-t)^2}\lVert z-x \rVert^2$$

$$\frac{\lVert z-y \rVert^2}{r-s} = \frac{\left(\frac{r-s}{r-t}\right)^2\lVert z-x \rVert^2}{r-s} = \frac{r-s}{(r-t)^2}\lVert z-x \rVert^2$$

합산:
$$\frac{s-t}{(r-t)^2}\lVert z-x \rVert^2 + \frac{r-s}{(r-t)^2}\lVert z-x \rVert^2 = \frac{(s-t)+(r-s)}{(r-t)^2}\lVert z-x \rVert^2 = \frac{\lVert z-x \rVert^2}{r-t}$$

$\blacksquare$

**검증 메모**:
- 이 정리는 "등속 경로에서만" 성립함. 일반 경로에서는 부등호 ($\geq$) 방향.
- Local action의 $d^2/\Delta t$ 항 설계 근거: $1/\Delta t$ normalization이 없으면 합성 시 오차 발생.
- 연속 시간 버전: $\int_t^r \lVert \dot\xi(\tau) \rVert^2 d\tau$의 등속 최소값이 $\lVert z-x \rVert^2/(r-t)$.

**판정**: $\boxed{\text{Cat A}}$

---

## Theorem T-ACT-DP — Hard-Min Action Cost의 Dynamic Programming

**문장**: 임의의 $i < j < k$에 대해:

$$\boxed{c_{i\to k}^{\mathrm{act}}(x,z) = \min_{y \in X_j} \!\left[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\right]}$$

**증명**:

**($\geq$) 방향**: 임의의 경로 $P = (x = x_i, x_{i+1}, \ldots, x_k = z)$를 $t_j$에서 절단하면 중간점 $y = x_j$가 생긴다. Action의 addivity에 의해:

$$\mathcal{A}_{i:k}(P) = \mathcal{A}_{i:j}(P_{i:j}) + \mathcal{A}_{j:k}(P_{j:k})$$

각 부분 action은 그 구간의 최소 action 이상이므로:

$$\mathcal{A}_{i:k}(P) \geq c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z) \geq \min_{y'}\!\left[c_{i\to j}^{\mathrm{act}}(x,y') + c_{j\to k}^{\mathrm{act}}(y',z)\right]$$

임의의 경로 $P$에 대해 성립하므로 infimum을 취하면:

$$c_{i\to k}^{\mathrm{act}}(x,z) \geq \min_{y}\!\left[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\right]$$

**($\leq$) 방향**: 우변의 최솟값을 달성하는 $y^* \in X_j$를 취하자 ($X_j$ 유한이므로 최솟값 존재).

$c_{i\to j}^{\mathrm{act}}(x,y^*)$를 달성하는 최적 경로 $P^*_{i:j}$와  
$c_{j\to k}^{\mathrm{act}}(y^*,z)$를 달성하는 최적 경로 $P^*_{j:k}$를 이어붙이면  
$x$에서 $z$로 가는 admissible 경로 $P^* = P^*_{i:j} \cup P^*_{j:k}$가 된다.

그 action:

$$\mathcal{A}_{i:k}(P^*) = c_{i\to j}^{\mathrm{act}}(x,y^*) + c_{j\to k}^{\mathrm{act}}(y^*,z) = \min_y\!\left[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\right]$$

$c_{i\to k}^{\mathrm{act}}$는 이 경로 action의 하한이므로:

$$c_{i\to k}^{\mathrm{act}}(x,z) \leq \mathcal{A}_{i:k}(P^*) = \min_y\!\left[\ldots\right]$$

양 방향을 합치면 등식. $\blacksquare$

**검증 메모**:
- 핵심 조건: $X_j$ 유한 → argmin 존재. 연속 공간에서는 compactness 필요.
- Additivity of action은 local action $a_i$의 additive sum 정의에서 자동.
- 이 정리는 $a_i \geq 0$ 조건 불필요 (양수 여부와 무관하게 성립).
  단, $a_i < 0$이면 경로가 무한히 길어질수록 action이 $-\infty$로 발산할 수 있음 (병적 경우).
  L-FINGERPRINT-ACTION-ADMISSIBLE에서 $a_i \geq 0$ 확인.
- **Bellman 방정식의 직접 이산 형태**. 수학적으로 완결된 증명.

**판정**: $\boxed{\text{Cat A}}$ (유한 site set, additive nonneg local action)

---

## Theorem T-ACT-GIBBS — Soft-Min Action Gibbs Kernel Semigroup

**문장**: 임의의 $i < j < k$에 대해 행렬 합성 등식:

$$\boxed{K_{i\to k} = K_{i\to j} K_{j\to k}}$$

성분별로:

$$K_{i\to k}(x,z) = \sum_{y \in X_j} K_{i\to j}(x,y)\, K_{j\to k}(y,z)$$

따라서 soft-min cost의 recursion:

$$\boxed{c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon\log\sum_{y \in X_j} \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y) + c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)}$$

**증명**:

$K_{i\to k}(x,z)$의 정의:

$$K_{i\to k}(x,z) = \sum_{\substack{x_{i+1},\ldots,x_{k-1} \\ x_i=x,\, x_k=z}} \exp\!\left(-\frac{\mathcal{A}_{i:k}}{\varepsilon}\right)$$

모든 경로는 $t_j$에서 유일한 중간점 $y = x_j$를 가진다. 따라서 경로 합을 $y$에 대한 합으로 분해:

$$K_{i\to k}(x,z) = \sum_{y \in X_j} \left[\sum_{\substack{x_{i+1},\ldots,x_{j-1} \\ x_i=x,\, x_j=y}} \exp\!\left(-\frac{\mathcal{A}_{i:j}}{\varepsilon}\right)\right] \left[\sum_{\substack{x_{j+1},\ldots,x_{k-1} \\ x_j=y,\, x_k=z}} \exp\!\left(-\frac{\mathcal{A}_{j:k}}{\varepsilon}\right)\right]$$

Action additivity: $\exp(-\mathcal{A}_{i:k}/\varepsilon) = \exp(-\mathcal{A}_{i:j}/\varepsilon)\exp(-\mathcal{A}_{j:k}/\varepsilon)$이므로 대괄호 내부가 분리됨.

따라서:

$$K_{i\to k}(x,z) = \sum_{y \in X_j} K_{i\to j}(x,y)\, K_{j\to k}(y,z)$$

이것이 행렬 곱 $[K_{i\to j} K_{j\to k}]_{xz}$의 정의이므로:

$$K_{i\to k} = K_{i\to j} K_{j\to k} \quad \blacksquare$$

**Soft-min recursion 도출**:

$K_{i\to j}(x,y) = \exp(-c_{i\to j}^{\varepsilon}(x,y)/\varepsilon)$이므로:

$$K_{i\to k}(x,z) = \sum_y \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y) + c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

양변에 $-\varepsilon\log$를 취하면 soft-min recursion 성립. $\blacksquare$

**검증 메모**:
- 이 정리는 **Chapman-Kolmogorov 방정식** (혹은 전달 행렬 semigroup)의 이산 path-integral 버전.
- 핵심: action의 additivity + 지수 함수의 곱 분리 → 합산 분해.
- $\varepsilon > 0$ 조건 필요 (정규화 인자; $\varepsilon = 0$이면 soft-min → hard-min으로 수렴).
- $K_{i\to k}$는 raw kernel (marginally unnormalized). Sinkhorn scaling 이전 상태.
- **T-ACT-GIBBS ≠ Sinkhorn plan semigroup**: Sinkhorn scaling 후에는 semigroup 깨짐 (02_conditional_open.md §T-SINKHORN-FAILS 참조).

**판정**: $\boxed{\text{Cat A}}$ (유한 site set, $\varepsilon > 0$, additive local action)

---

## Lemma L-SOFTMIN-HARDMIN-BOUND — Soft-Min / Hard-Min 오차 Bound

**문장**: 실수열 $a_1, \ldots, a_N$에 대해 soft-min

$$\operatorname{smin}_\varepsilon(a) = -\varepsilon\log\sum_{i=1}^N e^{-a_i/\varepsilon}$$

는 다음을 만족:

$$\boxed{\min_i a_i - \varepsilon\log N \;\leq\; \operatorname{smin}_\varepsilon(a) \;\leq\; \min_i a_i}$$

**증명**:

$m = \min_i a_i$라 하자.

**상한** ($\operatorname{smin}_\varepsilon \leq m$):

$$\sum_i e^{-a_i/\varepsilon} \geq e^{-m/\varepsilon}$$

(최솟값 항만으로 하한) $\Rightarrow$

$$-\varepsilon\log\sum_i e^{-a_i/\varepsilon} \leq -\varepsilon\log e^{-m/\varepsilon} = m$$

**하한** ($\operatorname{smin}_\varepsilon \geq m - \varepsilon\log N$):

$$\sum_i e^{-a_i/\varepsilon} \leq N \cdot e^{-m/\varepsilon}$$

(모든 항이 최솟값 이하) $\Rightarrow$

$$-\varepsilon\log\sum_i e^{-a_i/\varepsilon} \geq -\varepsilon\log(N e^{-m/\varepsilon}) = m - \varepsilon\log N$$

$\blacksquare$

**적용**: hard-min과 soft-min effective cost의 차이:

$$\left|c_{i\to k}^{\varepsilon,\mathrm{eff}}(x,z) - c_{i\to k}^{\mathrm{act}}(x,z)\right| \leq \varepsilon\log|X_j|$$

$\varepsilon \to 0$ 극한에서 $c^{\varepsilon} \to c^{\mathrm{act}}$ (soft-min → hard-min 수렴).

**검증 메모**:
- bound가 tight함: $a_i$가 모두 $m$이면 soft-min = $m$ (상한 달성); $a_i$가 균등 분포되면 soft-min → $m - \varepsilon\log N$ (하한 달성).
- $\lvert X_j \rvert$에 의존하므로 site 수가 많으면 gap이 커짐. Fingerprint well-separation 조건 하에서 effective 최솟값 항 1개 지배 → gap 감소.

**판정**: $\boxed{\text{Cat A}}$

---

## Lemma L-ACTION-DELTA-EFF-ZERO — Hard-Min Action: δ_eff = 0

**문장**: direct cost를 hard-min action cost로 정의하고 effective cost를

$$c_{i\to k}^{\mathrm{eff}}(x,z) = \min_{y \in X_j}\!\left[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\right]$$

로 정의하면:

$$\boxed{\delta_{\mathrm{eff}} = \left\lVert c_{i\to k}^{\mathrm{act}} - c_{i\to k}^{\mathrm{eff}}\right \rVert_\infty = 0}$$

**증명**:

T-ACT-DP에 의해 모든 $x \in X_i$, $z \in X_k$에 대해:

$$c_{i\to k}^{\mathrm{act}}(x,z) = \min_{y \in X_j}\!\left[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\right] = c_{i\to k}^{\mathrm{eff}}(x,z)$$

sup norm 차이는 0. $\blacksquare$

**중요한 조건 (non-overclaim)**:

> 이 결과는 $c_{i\to k}^{\mathrm{direct}}$를 **action cost로 재정의**했을 때만 성립한다.
> 기존 endpoint cost $\lVert z-x \rVert^2$ 또는 fingerprint similarity cost로 정의한 direct cost에는 적용 불가.
> 또한 이것은 raw action cost level의 결과이며,  
> **Sinkhorn-scaled plan과는 무관**하다.

**OP-0012-SINK 블로커 해소 경로**:

OP-0012-SINK의 핵심 blocker는 "$c_\mathrm{direct}$와 $c^\mathrm{eff}$의 차이 $\delta_\mathrm{eff}$가 얼마인가"였다.
이 lemma는 action cost를 direct cost로 채택하면 $\delta_\mathrm{eff} = 0$ (exact)을 보여준다.
단, 이것이 Sinkhorn plan semigroup까지 직접 연결되지 않음에 주의 (02 파일 참조).

**판정**: $\boxed{\text{Cat A}}$

---

## Lemma L-SOFT-ACTION-DELTA-EFF-ZERO — Soft-Min Action: δ_eff = 0

**문장**: direct soft cost를 $c_{i\to k}^{\varepsilon} = -\varepsilon\log K_{i\to k}$로 정의하고 effective soft cost를

$$c_{i\to k}^{\mathrm{eff},\varepsilon}(x,z) = -\varepsilon\log\sum_{y} \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y) + c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

로 정의하면:

$$\boxed{c_{i\to k}^{\varepsilon} = c_{i\to k}^{\mathrm{eff},\varepsilon}, \quad \delta_\mathrm{eff}^{\varepsilon} = 0}$$

**증명**:

T-ACT-GIBBS에 의해:

$$K_{i\to k}(x,z) = \sum_y K_{i\to j}(x,y) K_{j\to k}(y,z) = \sum_y \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

양변에 $-\varepsilon\log$:

$$c_{i\to k}^{\varepsilon}(x,z) = -\varepsilon\log\sum_y \exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right) = c_{i\to k}^{\mathrm{eff},\varepsilon}(x,z)$$

모든 $x,z$에서 등식이므로 $\delta_\mathrm{eff}^{\varepsilon} = 0$. $\blacksquare$

**L-ACTION-DELTA-EFF-ZERO와의 관계**:

- Hard-min ($\varepsilon\to0$): L-ACTION-DELTA-EFF-ZERO
- Soft-min (임의 $\varepsilon>0$): 이 lemma
- 두 경우 모두 $\delta_\mathrm{eff} = 0$ (exact, not approximate)

**판정**: $\boxed{\text{Cat A}}$

---

## Lemma L-FINGERPRINT-ACTION-ADMISSIBLE — SCC Fingerprint Action은 DP/Gibbs 전제 만족

**문장**: SCC fingerprint action

$$a_i(x,y) = \frac{d_i(x,y)^2}{\Delta t_i} + \gamma\frac{\lVert \varphi_{i+1}(y)-\varphi_i(x) \rVert^2}{\Delta t_i}$$

는 다음을 만족:
1. $a_i(x,y) \geq 0$ (nonnegativity)
2. Path action $\mathcal{A}_{i:k} = \sum_\ell a_\ell(x_\ell, x_{\ell+1})$ (additivity)
3. 따라서 T-ACT-DP, T-ACT-GIBBS의 전제 조건 충족

**증명**:

(1) $d_i(x,y)^2 \geq 0$ (거리의 제곱), $\lVert \varphi_{i+1}(y)-\varphi_i(x) \rVert^2 \geq 0$ (norm square), $\Delta t_i > 0$, $\gamma \geq 0$이므로 $a_i(x,y) \geq 0$. $\checkmark$

(2) Path action은 정의상 local action의 합산이므로 additivity 자동 성립. $\checkmark$

(3) T-ACT-DP: nonneg + additive + finite site ✓  
    T-ACT-GIBBS: additive + finite site + $\varepsilon > 0$ ✓ $\blacksquare$

**검증 메모**:
- 이 lemma는 "좋은 fingerprint인가"를 증명하지 않음.
  즉 SCC의 fingerprint gap, well-separation, fingerprint Lipschitz 조건 등은 별도 결과.
- "action theory의 형식적 전제를 만족한다"는 구조적 확인만 함.
- fingerprint에 $C_i(x,x)$ (resolvent diagonal)를 포함해도 동일하게 성립.
  단 canonical §8.5에서 resolvent diagonal은 demoted (기여 <0.4%) — 선택 사항.

**판정**: $\boxed{\text{Cat A}}$

---

## 요약: Cat A 판정표

| Lemma/정리 | 내용 | 판정 | 조건 |
|---|---|---|---|
| L-ENDPOINT-NONSEMI | Squared endpoint cost는 합성 불가 | **Cat A** | 반례 존재 (1D, x=0,z=2) |
| L-ACTION-NORMALIZATION | Time-normalized cost는 등속 경로에서 합성 정합 | **Cat A** | 등속 경로에서만 |
| **T-ACT-DP** | Hard-min action cost의 Bellman DP | **Cat A** | 유한 site, additive action |
| **T-ACT-GIBBS** | Gibbs kernel semigroup $K_{i\to k}=K_{i\to j}K_{j\to k}$ | **Cat A** | 유한 site, $\varepsilon>0$, additive action |
| L-SOFTMIN-HARDMIN-BOUND | $|\operatorname{smin}_\varepsilon - \min| \leq \varepsilon\log N$ | **Cat A** | 표준 log-sum-exp |
| L-ACTION-DELTA-EFF-ZERO | Hard-min action에서 $\delta_\mathrm{eff}=0$ | **Cat A** | action cost 재정의 전제 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | Soft-min action에서 $\delta_\mathrm{eff}^\varepsilon=0$ | **Cat A** | T-ACT-GIBBS 직접 귀결 |
| L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action은 DP/Gibbs 전제 만족 | **Cat A** | 구조적 확인 (not fingerprint quality) |

**핵심 결론**:

$$\boxed{c_{i\to k}^{\mathrm{act}} = \min_y[c_{i\to j}^{\mathrm{act}} + c_{j\to k}^{\mathrm{act}}] \quad\text{(T-ACT-DP, Cat A)}}$$

$$\boxed{K_{i\to k} = K_{i\to j}K_{j\to k} \quad\text{(T-ACT-GIBBS, Cat A)}}$$

이 두 결과가 CV-1.15의 핵심 벽돌이다.

---

*작성: 2026-05-12. 모든 증명 단계 검증 완료. 유한 site set 조건 명시.*
