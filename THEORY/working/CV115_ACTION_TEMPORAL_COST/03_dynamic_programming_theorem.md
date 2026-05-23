---
id: ACT-03
type: working/theory
status: open — T-ACT-DP 증명
created: 2026-05-12
scope: T-ACT-DP, L-ACTION-DELTA-EFF-ZERO
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 03. Dynamic Programming Theorem

---

## Theorem T-ACT-DP — Hard-Min Action Cost Bellman Principle

### 문장

> **T-ACT-DP** (Cat A 후보):
>
> 가정:
> - $X_i$, $X_j$, $X_k$는 유한 집합 ($i < j < k$).
> - 경로 집합 $\mathrm{Path}(x \to z; i,k) = \{(x_i,\ldots,x_k) : x_i=x, x_k=z, x_\ell\in X_\ell\}$.
> - $\mathcal{A}_{i:k}(P) = \sum_{\ell=i}^{k-1}a_\ell(x_\ell,x_{\ell+1})$ (additive, $a_\ell \geq 0$).
>
> 결론:
>
> $$\boxed{c_{i\to k}^{\mathrm{act}}(x,z) = \min_{y \in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr]}$$

---

### 증명

#### 보조 정의

**$c_{i\to k}^{\mathrm{act}}(x,z)$**: $\mathrm{Path}(x\to z; i,k)$ 위에서 $\mathcal{A}_{i:k}$의 최솟값. $X_j$ 유한이므로 argmin 존재.

**우변** (Bellman value):

$$\mathrm{BV}(x,z) = \min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr]$$

등식 $c_{i\to k}^{\mathrm{act}} = \mathrm{BV}$를 양방향 부등식으로 보인다.

---

#### ($\geq$) 방향: $c_{i\to k}^{\mathrm{act}}(x,z) \geq \mathrm{BV}(x,z)$

임의의 경로 $P \in \mathrm{Path}(x\to z; i,k)$를 취한다.

$P$를 $t_j$에서 절단하자:

$$P = P_{i:j} \cup P_{j:k}, \quad x_j \in X_j$$

여기서 $P_{i:j} = (x_i,\ldots,x_j)$, $P_{j:k}=(x_j,\ldots,x_k)$.

Path action의 additivity:

$$\mathcal{A}_{i:k}(P) = \mathcal{A}_{i:j}(P_{i:j}) + \mathcal{A}_{j:k}(P_{j:k})$$

각 부분 action은 해당 구간의 최솟값 이상:

$$\mathcal{A}_{i:j}(P_{i:j}) \geq c_{i\to j}^{\mathrm{act}}(x, x_j)$$

$$\mathcal{A}_{j:k}(P_{j:k}) \geq c_{j\to k}^{\mathrm{act}}(x_j, z)$$

합산:

$$\mathcal{A}_{i:k}(P) \geq c_{i\to j}^{\mathrm{act}}(x, x_j) + c_{j\to k}^{\mathrm{act}}(x_j, z) \geq \min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr] = \mathrm{BV}(x,z)$$

위 부등식은 임의의 경로 $P$에 대해 성립하므로, $P$에 대해 infimum을 취하면:

$$c_{i\to k}^{\mathrm{act}}(x,z) = \inf_P \mathcal{A}_{i:k}(P) \geq \mathrm{BV}(x,z) \quad \checkmark$$

---

#### ($\leq$) 방향: $c_{i\to k}^{\mathrm{act}}(x,z) \leq \mathrm{BV}(x,z)$

$X_j$가 유한이므로 argmin이 존재한다:

$$y^* = \operatorname*{argmin}_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr]$$

$c_{i\to j}^{\mathrm{act}}(x,y^*)$를 달성하는 최적 경로 $P^*_{i:j} \in \mathrm{Path}(x\to y^*; i,j)$가 존재한다.
($X_{i+1},\ldots,X_{j-1}$ 유한이므로 argmin 존재.)

마찬가지로 $c_{j\to k}^{\mathrm{act}}(y^*,z)$를 달성하는 최적 경로 $P^*_{j:k} \in \mathrm{Path}(y^*\to z; j,k)$가 존재한다.

두 경로를 이어붙인다:

$$P^* = P^*_{i:j} \cup P^*_{j:k} \in \mathrm{Path}(x\to z; i,k)$$

이 경로의 action:

$$\mathcal{A}_{i:k}(P^*) = \mathcal{A}_{i:j}(P^*_{i:j}) + \mathcal{A}_{j:k}(P^*_{j:k}) = c_{i\to j}^{\mathrm{act}}(x,y^*) + c_{j\to k}^{\mathrm{act}}(y^*,z) = \mathrm{BV}(x,z)$$

$c_{i\to k}^{\mathrm{act}}$는 모든 admissible 경로의 최솟값이므로:

$$c_{i\to k}^{\mathrm{act}}(x,z) \leq \mathcal{A}_{i:k}(P^*) = \mathrm{BV}(x,z) \quad \checkmark$$

---

#### 결론

양 방향을 합치면:

$$c_{i\to k}^{\mathrm{act}}(x,z) = \mathrm{BV}(x,z) = \min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr] \quad \blacksquare$$

---

### 검증 메모

| 항목 | 확인 |
|---|---|
| $a_\ell \geq 0$ 필요 여부 | 불필요. 증명은 $a_\ell$의 부호에 무관하게 작동함. 단, $a_\ell < 0$이면 경로가 길어질수록 action이 $-\infty$로 발산할 수 있으므로 병적 경우 발생. L-FINGERPRINT-ACTION-ADMISSIBLE에서 $a_\ell \geq 0$ 별도 확인. |
| 유한 site set 필요 여부 | 필요. argmin 존재 보장을 위해 $X_j$ 유한 사용. 연속 공간에서는 compactness + lower semi-continuity 필요. |
| 선형 DP (induction) | 임의의 $i < j_1 < j_2 < \cdots < k$에서 induction 적용 가능. 증명 구조 반복 적용. |
| 수학적 특성 | **Bellman optimality principle** (이산 버전). 강화학습 Bellman 방정식과 동일한 구조. |

---

## Lemma L-ACTION-DELTA-EFF-ZERO

**문장**:

> Direct cost를 $c_{i\to k}^{\mathrm{act}}$, effective cost를
>
> $$c_{i\to k}^{\mathrm{eff}}(x,z) = \min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y) + c_{j\to k}^{\mathrm{act}}(y,z)\bigr]$$
>
> 로 정의하면:
>
> $$\delta_{\mathrm{eff}} = \left\lVert c_{i\to k}^{\mathrm{act}} - c_{i\to k}^{\mathrm{eff}}\right \rVert_\infty = 0$$

**증명**: T-ACT-DP에 의해 $c_{i\to k}^{\mathrm{act}}(x,z) = c_{i\to k}^{\mathrm{eff}}(x,z)$ 모든 $x,z$에서. $\blacksquare$

**Non-overclaim (중요)**:

> 이 결과는 $c_{i\to k}^{\mathrm{direct}}$를 **action cost로 재정의**했을 때만 성립한다.
>
> - Endpoint cost $\lVert z-x \rVert^2$: $\delta_\mathrm{eff} = \lVert z-x \rVert^2/2 \neq 0$ (L-ENDPOINT-NONSEMI).
> - Fingerprint similarity cost: 일반적으로 $\delta_\mathrm{eff} \neq 0$.
> - Sinkhorn plan: cost level이 아닌 plan level 이슈 (05_relation_to_sinkhorn.md §2 참조).

**판정**: $\boxed{\text{Cat A}}$ (action direct cost 정의 하에서)

---

*작성: 2026-05-12.*
