---
id: ACT-02
type: working/theory
status: open — action cost 정의
created: 2026-05-12
scope: 시간 격자, SCC fingerprint, local action, path action, hard-min cost,
       L-FINGERPRINT-ACTION-ADMISSIBLE, P-ACTION-PATH-INHERITANCE
---

# 02. Action Cost 정의

---

## §1. 시간 격자 및 Site Set

$$t_0 < t_1 < \cdots < t_L, \quad \Delta t_i = t_{i+1}-t_i > 0$$

각 시각 $t_i$의 site 집합: $X_i$ (유한; $|X_i| < \infty$).

단순화 시 $X_i = X$ (공통 site set) 사용 가능. 일반적으로 $X_i$ 상이 허용.

---

## §2. SCC Fingerprint

**정의 D-FINGERPRINT**:

각 site $x \in X_i$에 대해 SCC fingerprint $\varphi_i(x)$를 다음과 같이 정의한다:

$$\varphi_i(x) = \bigl(u_i(x),\; \mathrm{Cl}_i(u_i)(x),\; D_i(x;\,1-u_i)\bigr) \in \mathbb{R}^3$$

각 성분:

| 성분 | 기호 | 의미 |
|---|---|---|
| cohesion field 값 | $u_i(x) \in [0,1]$ | site $x$의 cohesion 강도 |
| closure operator 값 | $\mathrm{Cl}_i(u_i)(x) \in [0,1]$ | closure 후 cohesion (canonical §4 정의) |
| distinction 값 | $D_i(x;\,1-u_i) \in \mathbb{R}_{\geq 0}$ | background-weighted distinction |

**비고**:
- Canonical §8.5에서 resolvent diagonal $r_{ii} = (I-\alpha P)^{-1}_{ii}$를 fingerprint에 포함하는 4성분 버전도 고려됨.
  단, resolvent diagonal은 canonical §8.5에서 "기여 <0.4%" demoted 상태이므로 이 패키지에서는 3성분 버전을 기본으로 한다.
- $\varphi_i$의 Lipschitz 상수, well-separation 조건 등은 별도 결과 (이 패키지 범위 외).

---

## §3. Local Action

**정의 D-LOCAL-ACTION**:

$$\boxed{a_i(x,y) = \frac{d_i(x,y)^2}{\Delta t_i} + \gamma\,\frac{\|\varphi_{i+1}(y)-\varphi_i(x)\|^2}{\Delta t_i}}$$

$x \in X_i$, $y \in X_{i+1}$, $\gamma \geq 0$.

각 항의 의미:

| 항 | 의미 | 단위 |
|---|---|---|
| $d_i(x,y)^2/\Delta t_i$ | 공간 이동 비용 (time-normalized) | [거리²/시간] |
| $\gamma\|\Delta\varphi\|^2/\Delta t_i$ | SCC 상태 변화 비용 (time-normalized) | [무차원/시간] |

**Optional term** $V_i(x,y)$:

$$a_i(x,y) = \frac{d_i(x,y)^2}{\Delta t_i} + \gamma\,\frac{\|\varphi_{i+1}(y)-\varphi_i(x)\|^2}{\Delta t_i} + V_i(x,y)$$

이 패키지에서는 $V_i(x,y) = 0$으로 둔다. $V_i \geq 0$ 조건이 추가되면 Admissibility Lemma 결론 그대로 유지.

---

## §4. Path Action

**정의 D-PATH-ACTION**:

경로 $P = (x_i = x, x_{i+1}, \ldots, x_k = z)$에 대해:

$$\mathcal{A}_{i:k}(P) = \sum_{\ell=i}^{k-1} a_\ell(x_\ell,\, x_{\ell+1})$$

핵심 성질 (**additivity**):

임의의 $i < j < k$에 대해, 경로 $P$를 $t_j$에서 두 부분으로 나누면 ($P = P_{i:j} \cup P_{j:k}$):

$$\mathcal{A}_{i:k}(P) = \mathcal{A}_{i:j}(P_{i:j}) + \mathcal{A}_{j:k}(P_{j:k})$$

이것은 합산 정의에서 자동으로 따른다.

---

## §5. Hard-Min Action Cost

**정의 D-HARD-MIN-COST**:

$$\boxed{c_{i\to k}^{\mathrm{act}}(x,z) = \min_{\substack{(x_i,\ldots,x_k):\\x_i=x,\; x_k=z}} \mathcal{A}_{i:k}(x_i,\ldots,x_k)}$$

**존재성**: $X_{i+1},\ldots,X_{k-1}$이 모두 유한이므로 최솟값 달성 경로 존재.

---

## §6. Lemma L-FINGERPRINT-ACTION-ADMISSIBLE

**문장**:

> SCC fingerprint action $a_i(x,y) = d_i(x,y)^2/\Delta t_i + \gamma\|\varphi_{i+1}(y)-\varphi_i(x)\|^2/\Delta t_i$는:
>
> 1. $a_i(x,y) \geq 0$ (nonnegativity)
> 2. $\mathcal{A}_{i:k}(P) = \sum_\ell a_\ell(x_\ell, x_{\ell+1})$ (additivity, by definition)
> 3. 따라서 T-ACT-DP, T-ACT-GIBBS의 전제 조건을 모두 충족한다.

**증명**:

**(1) Nonnegativity**:

$$d_i(x,y)^2 \geq 0 \quad\text{(거리의 제곱)},\quad \|\varphi_{i+1}(y)-\varphi_i(x)\|^2 \geq 0 \quad\text{(norm square)}$$

$\Delta t_i > 0$, $\gamma \geq 0$이므로 각 항 $\geq 0$. 따라서 $a_i(x,y) \geq 0$. $\checkmark$

**(2) Additivity**:

Path action은 정의상 local action의 합산이므로 $i < j < k$에서:

$$\mathcal{A}_{i:k}(P) = \sum_{\ell=i}^{k-1}a_\ell = \sum_{\ell=i}^{j-1}a_\ell + \sum_{\ell=j}^{k-1}a_\ell = \mathcal{A}_{i:j}(P_{i:j}) + \mathcal{A}_{j:k}(P_{j:k}) \quad \checkmark$$

**(3) T-ACT-DP 전제 확인**:

T-ACT-DP는 (a) additive path action, (b) finite site set $X_j$ 조건만 사용.
(a) ✓ (2번), (b) ✓ ($|X_j|<\infty$ 가정). $\checkmark$

**(4) T-ACT-GIBBS 전제 확인**:

T-ACT-GIBBS는 (a) additive path action, (b) finite site set, (c) $\varepsilon>0$ 조건 사용.
(a)(b) ✓, (c)는 $\varepsilon>0$ 선택 시 만족. $\checkmark$ $\blacksquare$

**비고**:

- 이 lemma는 "fingerprint가 좋은가"를 증명하지 않는다. fingerprint gap, well-separation, Lipschitz 조건 등은 별도 결과.
- "action theory의 형식적 전제를 구조적으로 만족한다"는 확인만 한다.
- $V_i \geq 0$ optional term 추가 시 nonnegativity 유지, 나머지 무변.

**판정**: $\boxed{\text{Cat A}}$

---

## §7. P-ACTION-PATH-INHERITANCE (해석 명제, 수학 정리 아님)

**명제 P-ACTION-PATH-INHERITANCE**:

> **(Definition Justification / Interpretation)**
>
> SCC temporal identity는 endpoint similarity보다 low-action path inheritance에 더 잘 부합한다.
>
> 이유:
> - SCC의 핵심 원리는 u_t의 연속적 진화 (axiom A3: stabilization tendency).
> - Stabilization tendency는 "형성이 갑자기 바뀌지 않는다"는 것이며, 이는 경로상 작은 action이다.
> - Endpoint similarity는 중간 경로를 무시하므로, t→s→r 동안의 점진적 진화를 포착하지 못한다.
> - Hard-min action cost는 t→r 간 최소 action 역사 경로를 찾으므로, SCC의 지속성 개념과 정렬된다.

**분류**: 수학 정리가 아닌 **definition justification / interpretation**.
이 명제는 canonical.md의 motivation 섹션에 삽입하기 적합하다.

---

*작성: 2026-05-12.*
