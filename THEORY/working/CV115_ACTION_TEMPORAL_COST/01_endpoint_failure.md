---
id: ACT-01
type: working/theory
status: open — endpoint cost 실패 증명
created: 2026-05-12
scope: L-ENDPOINT-NONSEMI, L-ACTION-NORMALIZATION
---

# 01. Endpoint Cost 실패 증명

---

## 배경

SCC temporal identity에서 $t$-시각 site $x \in X_t$와 $r$-시각 site $z \in X_r$의
"시간적 대응"을 어떤 cost로 정의할 것인가?

**자연스러운 첫 시도**: squared endpoint similarity cost

$$c^\mathrm{end}_{t\to r}(x,z) = \|z - x\|^2$$

이 cost는 두 site 간의 직접 거리 제곱이다.
간단하고 직관적이지만, **시간 합성과 호환되지 않는다**.

---

## Lemma L-ENDPOINT-NONSEMI — Squared Endpoint Cost 합성 불가

**문장**:

> Squared endpoint cost $c^\mathrm{end}(x,z) = \|z-x\|^2$는 일반적으로
>
> $$c^\mathrm{end}_{t\to r}(x,z) \;\neq\; \min_{y}\!\bigl[c^\mathrm{end}_{t\to s}(x,y) + c^\mathrm{end}_{s\to r}(y,z)\bigr]$$
>
> 이다.

**증명** ($\mathbb{R}^1$, $x=0$, $z=2$, 중간점 $y=1$):

좌변 (직접):

$$c^\mathrm{end}_{t\to r}(0,2) = |2-0|^2 = 4$$

우변 (중간점 $y=1$을 통한 합성):

$$c^\mathrm{end}_{t\to s}(0,1) + c^\mathrm{end}_{s\to r}(1,2) = |1-0|^2 + |2-1|^2 = 1 + 1 = 2$$

$y=1$을 경유하는 경로의 합이 $2$이므로:

$$\min_y\bigl[c^\mathrm{end}_{t\to s}(x,y)+c^\mathrm{end}_{s\to r}(y,z)\bigr] \;\leq\; 2 \;<\; 4$$

등식이 성립하지 않는다. 반례 존재이므로 일반적으로 성립하지 않는다. $\blacksquare$

**추가 분석**:

$\mathbb{R}^d$에서 임의의 $x,z$에 대해 중간점 $y=(x+z)/2$로 하면:

$$\min_y\bigl[\|y-x\|^2+\|z-y\|^2\bigr] = 2\left\|\frac{z-x}{2}\right\|^2 = \frac{\|z-x\|^2}{2}$$

따라서:

$$c^\mathrm{end}(x,z) = \|z-x\|^2, \qquad \min_y[\ldots] = \frac{\|z-x\|^2}{2}$$

차이 $= \|z-x\|^2/2 \neq 0$ (일반적). 등호는 $x=z$일 때만 성립.

**결론**:

> Endpoint similarity cost는 **temporal composition-compatible하지 않다**.
> "$x$와 $z$가 직접 닮았는가"를 측정하는 것은 경로를 통한 시간적 계승을 반영하지 못한다.

**판정**: $\boxed{\text{Cat A}}$ (반례 구성 완결)

---

## Lemma L-ACTION-NORMALIZATION — Time-Normalized Cost 합성 정합

**문장**:

> $t < s < r$에 대해, 선형 보간 중간점
>
> $$y^* = \frac{r-s}{r-t}\,x + \frac{s-t}{r-t}\,z$$
>
> 에서 time-normalized squared cost는 additive:
>
> $$\frac{\|z-x\|^2}{r-t} = \frac{\|y^*-x\|^2}{s-t} + \frac{\|z-y^*\|^2}{r-s}$$

**증명**:

선형 보간 정의에서:

$$y^* - x = \frac{s-t}{r-t}(z-x), \qquad z - y^* = \frac{r-s}{r-t}(z-x)$$

각 항:

$$\frac{\|y^*-x\|^2}{s-t}
= \frac{\left(\dfrac{s-t}{r-t}\right)^2\|z-x\|^2}{s-t}
= \frac{s-t}{(r-t)^2}\|z-x\|^2$$

$$\frac{\|z-y^*\|^2}{r-s}
= \frac{\left(\dfrac{r-s}{r-t}\right)^2\|z-x\|^2}{r-s}
= \frac{r-s}{(r-t)^2}\|z-x\|^2$$

합산:

$$\frac{s-t}{(r-t)^2}\|z-x\|^2 + \frac{r-s}{(r-t)^2}\|z-x\|^2
= \frac{(s-t)+(r-s)}{(r-t)^2}\|z-x\|^2
= \frac{\|z-x\|^2}{r-t} \quad \blacksquare$$

**해석**:

이 결과가 보여주는 것:

1. **$1/\Delta t$ normalization이 핵심이다.** raw $\|z-x\|^2$는 합성 불가이지만, $\|z-x\|^2/(r-t)$는 등속 경로에서 정합.

2. **연속 시간 analogy**: $\int_t^r \|\dot\xi(\tau)\|^2\,d\tau$의 등속 경로 최솟값이 $\|z-x\|^2/(r-t)$.

3. **local action의 $d^2/\Delta t$ 항 설계 근거**: normalization 없이는 합성 시 오차 발생.

**단, 이 정합은 등속 경로에서만 성립한다.** 임의 경로에서는

$$\frac{\|z-x\|^2}{r-t} \;\leq\; \min_y\!\left[\frac{\|y-x\|^2}{s-t} + \frac{\|z-y\|^2}{r-s}\right]$$

즉 등속 경로 이외에서는 우변 ≥ 좌변, 합성값이 더 크거나 같다.

**판정**: $\boxed{\text{Cat A}}$

---

## L-ENDPOINT-NONSEMI와 L-ACTION-NORMALIZATION 연결

| 비교 | 결과 | 의미 |
|---|---|---|
| $c^\mathrm{end}(x,z) = \|z-x\|^2$ | $\min_y[\ldots] = \|z-x\|^2/2 \neq \|z-x\|^2$ | 합성 불가 |
| $c^\mathrm{norm}(x,z) = \|z-x\|^2/(r-t)$ | 등속 중간점에서 additive | 부분적 정합 |
| $c^\mathrm{act}_{i\to k}(x,z)$ (action) | Bellman DP 정확 성립 (T-ACT-DP) | **완전 정합** |

Endpoint cost의 실패 → normalization 필요 → local action의 $d^2/\Delta t$ 구조 → Bellman DP 성립.

---

*작성: 2026-05-12.*
