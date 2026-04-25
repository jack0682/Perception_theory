# pre_brainstorm.md — 2026-04-25 Session Pre-brainstorm

**Purpose:** Open-ended hypothesis exploration before plan execution.
**Reference state:** 2026-04-24 evening — Theorem 1 V5b confirmed (dual-regime + commensurability splitting discovered), C2 ~100%·C3 sub-lattice ~100% conquered, Axiom S1' v1 canonical-ready, ~40 NQ (NQ-125..171).
**Thinking mode:** Mechanism-first. 어제 발견된 현상의 "왜"를 묻는다. 성급한 claim 금지 — 어제 V4→V5a→V5b의 교훈.

---

## §1. 어제의 발견과 오늘의 질문

### 1.1 발견 요약 (27_deep_dive_results.md §7-8)

Super-lattice regime (ζ = ξ_0/a ≥ 0.5)에서:
- Lowest Hessian eigenmode: **δu_y 와 94-98% overlap** → y-translation Goldstone
- Second lowest mode: **eigenvalue가 orbital-scale** (near-zero 아님)
- L=40 β/β_c=10 decoupled test: **99% Goldstone overlap**, criticality와 독립 확인

**핵심 발견**: Continuum에서 2-fold degenerate Goldstone doublet ($\partial_x u^*, \partial_y u^*$)이 discrete lattice에서 **(λ_near-zero, λ_orbital-scale)** pair로 split. 즉 x-translation과 y-translation이 서로 다른 eigenvalue를 가짐.

### 1.2 오늘의 중심 질문 (NQ-168)

> **왜 x-translation Goldstone와 y-translation Goldstone의 eigenvalue가 다른가?**
> **이 splitting이 disk center position (x_0, y_0)의 어떤 함수인가?**

이 질문에 답하는 것이 오늘의 전부.

### 1.3 알려진 사실 vs 미지

**알려진 것**:
- ζ < 0.3 (sub-lattice): splitting 없음, 둘 다 orbital-scale
- ζ > 0.5 (super-lattice): splitting 있음, 하나 near-zero + 하나 orbital-scale
- β/β_c ≫ 1 decoupled에서도 splitting 유지 → criticality 기원 아님
- L=40 torus에서 발견 → boundary effect 아님 (주기 경계)

**미지**:
- disk center position (x_0, y_0)에 따라 splitting이 어떻게 변하는가?
- splitting의 exact functional form은?
- x vs y 비대칭의 geometric origin은?
- ζ_* 경계(≈0.3-0.4)에서의 smooth transition mechanism은?

---

## §2. Peierls-Nabarro (PN) Framework — 가장 유망한 이론

### 2.1 PN 기본 아이디어

연속체 soliton이 discrete lattice 위에 놓이면, center position $(x_0)$에 따라 에너지가 주기적으로 변화한다. 이 주기적 potential을 **Peierls-Nabarro potential** $V_{\mathrm{PN}}(x_0)$ 라 한다.

SCC 맥락: disk minimizer $u^*(x; x_0, y_0)$ (center at $(x_0, y_0)$)의 에너지 $\mathcal{E}(x_0, y_0)$가 lattice 주기의 주기 함수.

### 2.2 1D PN potential의 표준 결과

Frenkel-Kontorova / sine-Gordon 계열에서:
$$V_{\mathrm{PN}}(x_0) = V_0 \left(1 - \cos\frac{2\pi x_0}{a}\right)$$

여기서 $V_0 \propto \exp\!\left(-\frac{\pi^2 \xi_0}{a}\right)$ (exponentially small in $\xi_0/a$).

→ kink (domain wall, soliton) 의 번 oscillation frequency:
$$\omega_{\mathrm{PN}}^2 = \frac{1}{m_{\mathrm{eff}}} \frac{d^2 V_{\mathrm{PN}}}{dx_0^2} = \frac{(2\pi)^2 V_0}{m_{\mathrm{eff}} a^2} \cos\frac{2\pi x_0}{a}$$

→ 이것이 Goldstone mode의 eigenvalue: **$\lambda_{\mathrm{Gold}}(x_0) = \omega_{\mathrm{PN}}^2(x_0)$**

### 2.3 2D PN potential (SCC)

2D square lattice에서 disk center $(x_0, y_0)$:
$$V_{\mathrm{PN}}(x_0, y_0) = V_0 \left[\cos\frac{2\pi x_0}{a} + \cos\frac{2\pi y_0}{a}\right] + V_1 \cos\frac{2\pi x_0}{a}\cos\frac{2\pi y_0}{a} + \ldots$$

Leading order: separable x + y contributions.

**x-Goldstone eigenvalue** (response to x-translation):
$$\lambda_x(x_0, y_0) = \frac{(2\pi)^2 V_0}{m_{\mathrm{eff}} a^2} \cos\frac{2\pi x_0}{a} + O(V_1)$$

**y-Goldstone eigenvalue** (response to y-translation):
$$\lambda_y(x_0, y_0) = \frac{(2\pi)^2 V_0}{m_{\mathrm{eff}} a^2} \cos\frac{2\pi y_0}{a} + O(V_1)$$

**Splitting**:
$$\Delta\lambda(x_0, y_0) = \lambda_x - \lambda_y \propto \cos\frac{2\pi x_0}{a} - \cos\frac{2\pi y_0}{a}$$

### 2.4 PN 예측의 핵심 결론

- **대칭점** $(x_0, y_0) = (0, 0)$ (lattice site): $\Delta\lambda = 0$ (degenerate Goldstone doublet)
- **Edge point** $(x_0, y_0) = (a/2, 0)$: $\cos(2\pi x_0/a) = -1$, $\cos(2\pi y_0/a) = +1$ → $\Delta\lambda$ 최대
- **Diagonal** $(x_0, y_0) = (a/2, a/2)$ (saddle point): $\Delta\lambda = 0$ 다시

→ **PN 예측**: splitting은 $(x_0, y_0)$ 위치에 따라 사인파 패턴으로 변화. Disk center가 lattice site 또는 saddle point에 있을 때 degenerate, edge에 있을 때 최대 split.

### 2.5 어제 관측과의 비교

어제 test config가 정확히 어디 (x_0, y_0)에 있었는가?

- L=40 torus에서 Fiedler IC → disk center가 특정 위치에 수렴
- 만약 center가 edge (a/2, 0) 근처에 있었다면 → 최대 splitting (관측과 consistent)
- 만약 center가 site (0, 0)에 있었다면 → zero splitting이어야 함 (관측된 splitting이 있었으므로 off-site 가능성)

이것이 **G1 수치 실험으로 검증 가능한 핵심 prediction**.

---

## §3. Irrep Splitting (σ-framework) — 대안 메커니즘

### 3.1 아이디어

어제 σ-framework에서 Hessian eigenmode는 $\mathrm{Stab}_G(u^*)$의 irrep으로 분류된다. Continuum에서 translation Goldstone doublet $(\partial_x u^*, \partial_y u^*)$는 2D irrep $E$ (x, y 함께)에 속한다.

**그런데**: discrete torus에서 $\mathrm{Stab}_G(u^*)$는 정확히 어떤 group인가?

- Torus는 전역적으로 $\mathbb{Z}_L \times \mathbb{Z}_L$ translation symmetry를 가짐
- Disk center가 $(0, 0)$ (lattice site)에 있을 때: x-translation $T_x$와 y-translation $T_y$ 동등 → $E$-irrep 2D degenerate
- Disk center가 $(a/2, 0)$ (edge)에 있을 때: x-translation이 다른 half-lattice site로 가고, y-translation은 같은 y-offset 유지 → **symmetry breaking** → $E$ splits into $A \oplus B$ (1D + 1D irreps)

### 3.2 Symmetry breaking pattern

| Disk center | $\mathrm{Stab}_{D_4}(u^*)$ | Goldstone irrep | Splitting |
|---|---|---|---|
| $(0, 0)$ (site) | $D_4$ | $E$ (2D) | $\Delta\lambda = 0$ |
| $(a/2, a/2)$ (saddle) | $D_4$ (rotated) | $E$ (2D) | $\Delta\lambda = 0$ |
| $(a/2, 0)$ (edge) | $D_2$ (sub-group) | $A_1 \oplus B_1$ | $\Delta\lambda \neq 0$ |
| general | $C_1$ (trivial) | $A \oplus A$ | $\Delta\lambda$ generic |

**핵심**: $D_4$가 보존되는 위치 (site, saddle)에서만 $E$-irrep 2D degeneracy 유지. 그 외에서는 자연스럽게 split.

### 3.3 PN과 irrep splitting의 관계

두 접근법이 사실 **같은 현상을 다른 언어로 기술**할 가능성:
- PN: 에너지 곡면의 curvature 비대칭 → eigenvalue 분리
- Irrep splitting: symmetry 저하 → degenerate multiplet 분리

이 두 language가 consistent하면 (즉 splitting functional form이 동일하면), 우리는 두 개의 독립적 이론이 아니라 하나의 phenomenon을 두 관점에서 보는 것.

검증 방법: PN이 예측하는 $\cos(2\pi x_0/a) - \cos(2\pi y_0/a)$ 의존성이 irrep-split 구조의 matrix element로도 유도되는가?

### 3.4 σ-framework에 대한 함의

만약 Goldstone splitting이 irrep-based라면:
- σ에서 Goldstone mode를 어떻게 표현할지 자명해짐: $[\rho_0] = E$ (degenerate) at high-symmetry positions, $A_1 \oplus B_1$ (split) at generic positions
- Axiom S1' v1의 "(post-Goldstone)" 한정자가 position-dependent가 됨 → S1' 수정 필요할 수 있음

이것이 오늘 세션이 σ-framework에 **가장 직접적으로 연결되는 지점**.

---

## §4. Fourier Decomposition — 수학적 완전성 검토

### 4.1 General lattice potential

어떤 함수 $f(x_0, y_0)$이 $a$-주기적이라면 Fourier로:
$$f(x_0, y_0) = \sum_{m,n \in \mathbb{Z}} c_{mn} e^{i 2\pi(m x_0 + n y_0)/a}$$

에너지 $\mathcal{E}(x_0, y_0) = \mathcal{E}_0 + V_{\mathrm{PN}}(x_0, y_0)$에서:

$$V_{\mathrm{PN}}(x_0, y_0) = 2V_{10}\cos\frac{2\pi x_0}{a} + 2V_{01}\cos\frac{2\pi y_0}{a} + 4V_{11}\cos\frac{2\pi x_0}{a}\cos\frac{2\pi y_0}{a} + \ldots$$

Square lattice의 $D_4$ symmetry: $V_{10} = V_{01}$ (same coefficient in x, y at lowest order).

### 4.2 Why splitting occurs despite $V_{10} = V_{01}$

만약 $V_{10} = V_{01}$이면 $\partial^2 V/\partial x_0^2 = \partial^2 V/\partial y_0^2$ at $(0,0)$. 그러면 splitting이 0?

**아니다.** x-Goldstone는 $\partial^2 V_{\mathrm{PN}}/\partial x_0^2$에 의존하고, y-Goldstone는 $\partial^2 V_{\mathrm{PN}}/\partial y_0^2$에 의존하는데, 이 두 partial derivatives는 *일반 위치 $(x_0, y_0)$에서* 서로 달라진다:

$$\frac{\partial^2 V}{\partial x_0^2} = -\frac{(2\pi)^2}{a^2}\left[V_{10}\cos\frac{2\pi x_0}{a} + V_{11}\cos\frac{2\pi x_0}{a}\cos\frac{2\pi y_0}{a} + \ldots\right]$$

$$\frac{\partial^2 V}{\partial y_0^2} = -\frac{(2\pi)^2}{a^2}\left[V_{01}\cos\frac{2\pi y_0}{a} + V_{11}\cos\frac{2\pi x_0}{a}\cos\frac{2\pi y_0}{a} + \ldots\right]$$

**Leading difference** (ignoring $V_{11}$):
$$\frac{\partial^2 V}{\partial x_0^2} - \frac{\partial^2 V}{\partial y_0^2} \approx -\frac{(2\pi)^2 V_{10}}{a^2}\left[\cos\frac{2\pi x_0}{a} - \cos\frac{2\pi y_0}{a}\right]$$

→ PN §2.3의 결론과 동일. Fourier decomposition이 PN 공식을 재현. 두 접근법은 consistent.

### 4.3 Higher-order corrections

$V_{11}$ term (diagonal coupling):
$$\Delta\lambda_{\mathrm{corr}} \propto V_{11}\cos\frac{2\pi x_0}{a}\cos\frac{2\pi y_0}{a}\left[\ldots\right]$$

이 항은 $(0, a/2)$ 등의 edge point에서도 보정을 준다. 수치 결과와 leading-order PN 예측의 차이가 이 항으로 설명되는지 확인 가능.

---

## §5. 수치 실험 설계 (G1) — 메커니즘 판별 전략

### 5.1 핵심 실험: position scan

**Setup**:
- L=40 torus, ζ ≈ 0.7 (super-lattice 중간)
- IC: Gaussian disk at known center $(x_0, y_0)$ (다양한 위치)
- Optimizer: semi-implicit projected gradient (standard SCC)
- Measurement: lowest 4 Hessian eigenvalues + eigenvector overlap with $(\partial_x u^*, \partial_y u^*)$

**Position grid**: $(x_0, y_0) \in \{0, a/4, a/2, 3a/4\} \times \{0, a/4, a/2, 3a/4\}$ (16 positions)

**Expected result under PN** (§2.3):
| $(x_0, y_0)$ | $\Delta\lambda$ | Splitting |
|---|---|---|
| $(0, 0)$ | 0 | Degenerate doublet |
| $(a/2, 0)$ | maximal | Large x-y asymmetry |
| $(a/2, a/2)$ | 0 | Degenerate (saddle) |
| $(a/4, 0)$ | intermediate | Partial split |

### 5.2 PN 예측 falsification test

**Falsification condition**: 만약 $(0, 0)$에서 splitting이 0이 아닌 substantial value이면 → PN leading-order 공식 incorrect.

**Potential causes of failure**:
- disk가 실제로 정확히 site에 수렴하지 않음 (positional noise)
- 더 높은 Fourier harmonics ($V_{20}$, $V_{02}$)의 기여가 comparable
- ζ-regime에서 "effective lattice constant"가 달라질 수 있음

### 5.3 Phase map 해석

16-point scan의 결과를 $\Delta\lambda(x_0, y_0)$ 열지도(heat map)로 시각화. 이론 예측 $\cos(2\pi x_0/a) - \cos(2\pi y_0/a)$와 비교:
- 정성적 agreement: Cat B candidate
- 정량적 agreement (residual < 10%): Cat A candidate

---

## §6. NQ-169 예비 탐색 — β-scaling ν=5.8의 이론적 분해

### 6.1 어제 관측

27_deep_dive_results.md에서 Goldstone eigenvalue의 β-scaling:
$$\lambda_{\mathrm{Gold}}(\beta) \propto \beta^{\nu}, \quad \nu \approx 5.8 \quad (\text{Cat B empirical})$$

이 ν=5.8은 어디서 오는가?

### 6.2 두 기여의 분해

**기여 1 — PN barrier** ($V_0$의 β-dependence):
$$V_0 \propto \exp\!\left(-\frac{\pi^2 \xi_0}{a}\right)$$

여기서 $\xi_0 = \xi_0(\beta)$. Interface width는 $\beta$ 증가하면 감소:
$$\xi_0 \sim \frac{1}{\sqrt{\beta}} \quad \text{(Allen-Cahn scaling)}$$

→ $V_0 \propto \exp(-\pi^2/\sqrt{\beta} \cdot 1/a) \approx 1 - \pi^2/(\sqrt{\beta} a) + \ldots$ (weak β-dependence for large β)

이 기여만으로는 β^5.8 설명 어려움.

**기여 2 — Effective mass** ($m_{\mathrm{eff}}$의 β-dependence):

x-translation mode의 effective mass:
$$m_{\mathrm{eff}} = \int |\nabla u^*|^2 \, dx \sim r_0 \int_0^\infty \left(\frac{du^*}{dr}\right)^2 dr$$

$du^*/dr \sim (1/\xi_0)\,\mathrm{sech}^2((r-r_0)/\xi_0)$이므로:
$$m_{\mathrm{eff}} \sim \frac{r_0}{\xi_0} \propto r_0 \sqrt{\beta}$$

그리고 $r_0 \propto \sqrt{m/(\pi)} = \text{const}$ (mass constraint에서 고정).

→ $\lambda_{\mathrm{Gold}} = V_0 / m_{\mathrm{eff}} \propto V_0 / \sqrt{\beta}$. 여전히 ν=5.8과 gap.

### 6.3 Near-critical enhancement

$\beta$가 $\beta_{\mathrm{crit}}$에 근접할 때 additional contribution:

Phase transition threshold에서 Hessian의 lowest eigenvalue는 soft mode를 가짐. Goldstone와 near-critical soft mode가 **coupled** 할 경우:
$$\lambda_{\mathrm{Gold,eff}}(\beta) = \lambda_{\mathrm{Gold,bare}}(\beta) \cdot f\!\left(\frac{\beta}{\beta_{\mathrm{crit}}}\right)$$

$f$ = enhancement factor from coupling. 어제 decoupled test (β/β_c=10)에서 splitting이 유지됐으므로, 이 coupling은 magnitude는 바꿀 수 있어도 splitting existence는 결정하지 않음.

### 6.4 Combined formula (tentative)

$$\lambda_{\mathrm{Gold}}(\beta) = A \cdot \frac{\exp(-B/\sqrt{\beta})}{C \cdot \sqrt{\beta}} \cdot \left(\frac{\beta}{\beta_{\mathrm{crit}}}\right)^\gamma$$

각 factor:
- $\exp(-B/\sqrt{\beta})$: PN barrier (exponentially suppressed at small β)
- $1/\sqrt{\beta}$: effective mass denominator
- $(\beta/\beta_{\mathrm{crit}})^\gamma$: near-critical enhancement

전체 power: $\exp(-B/\sqrt{\beta}) \cdot \beta^{-1/2} \cdot \beta^\gamma$. Large β에서 dominant term = $\beta^{\gamma - 1/2}$.

→ **$\nu \approx 5.8$을 설명하려면** $\gamma \approx 6.3$. 이 $\gamma$의 이론적 기원은?

이것이 NQ-169의 core — 오늘 G3에서 이 분해의 합리성을 검토하는 것이 목표.

---

## §7. PN의 SCC 적용 시 주의 — 차이점과 잠재적 실패

### 7.1 Standard PN vs SCC PN

| 특성 | Standard kink (FK model) | SCC disk |
|---|---|---|
| Object shape | 1D kink $\tanh(x/\xi_0)$ | 2D disk, radial $\tanh$ |
| Translational modes | 1개 (x) | 2개 (x, y) |
| Effective mass | $\int (\partial_x u)^2 dx$ (1D) | $\int \|\nabla u\|^2 d^2x$ (2D) |
| PN potential symmetry | 1D periodic | 2D periodic (square) |
| Closure effect | 없음 | **있음** — $E_{\mathrm{cl}}$이 potential 수정 |
| Separation effect | 없음 | **있음** — $E_{\mathrm{sep}}$이 potential 수정 |

**SCC-specific modification**: PN potential이 $\mathcal{E}_{\mathrm{bd}}$ 기여만이 아니라 $\mathcal{E}_{\mathrm{cl}}$ + $\mathcal{E}_{\mathrm{sep}}$의 기여도 포함.

### 7.2 Closure 효과

$\mathcal{E}_{\mathrm{cl}}$는 disk interior가 FP $c^*$와 mismatch할 때 penalty. 이 penalty는 disk center position에 **의존하지 않는다** (interior 전체의 평균 property) — 따라서 PN potential에 기여 X. → Closure는 $V_{\mathrm{PN}}$에 leading order 기여 없음.

(단, closure가 minimizer shape를 변형하면 간접 기여 있음 — higher order.)

### 7.3 Separation 효과

$\mathcal{E}_{\mathrm{sep}}$는 boundary gradient에 sensitive. Boundary가 lattice와 commensurability를 갖는 방식이 달라질 때 변화. → **sep이 PN potential에 기여할 수 있음**.

Specifically: disk edge가 dense lattice edge를 교차하는 pattern이 $(x_0, y_0)$에 따라 달라짐 → additional periodic potential.

이것이 pure Allen-Cahn PN과 SCC PN의 **차이** — 어제 `26b_FK_analogy.md`에서 다룬 내용.

### 7.4 Regime condition for PN validity

PN theory가 유효하려면 $\xi_0 \ll a$ (sharp soliton on coarse lattice, FK regime) 또는 $\xi_0 \gg a$ (continuum limit)이어야 잘 작동한다.

ζ = ξ_0/a에서:
- ζ ≪ 1 (sub-lattice, $\xi_0 \ll a$): PN barrier $V_0 \propto \exp(-\pi^2 \xi_0/a) \approx \exp(-\pi^2 \zeta)$ — exponentially small. → **PN nearly irrelevant, Goldstone near-zero**
- ζ ≫ 1 (super-lattice, $\xi_0 \gg a$): PN barrier large → **Goldstone lifted**

이것이 dual-regime의 이론적 기원 (PN-based). ζ_* ≈ 0.3-0.4 transition은 $V_0 \sim$ eigenvalue gap 조건에서 결정.

---

## §8. 위험 요인과 잠재적 실패 모드

### 8.1 Disk가 lattice site에 정확히 수렴하지 않을 수 있음

SCC optimizer의 gradient flow가 $u^*$를 정확히 lattice site center에 수렴시키는 보장이 없다. "Center" 개념이 continuous relaxation에서는 약간 off이다.

→ Consequence: $(0, 0)$ 실험이 실제로는 $(ε, δ)$ 에서 수행됨. 이 경우 이론 예측을 검증하려면 **center 측정이 선행**되어야.

**해결**: 각 minimizer의 center of mass $(x_c, y_c) = \frac{\sum_i x_i u^*(i)}{\sum_i u^*(i)}$ 계산 후 $V_{\mathrm{PN}}(x_c, y_c)$와 비교.

### 8.2 ζ scan이 β, m에 동시 dependent

ζ = ξ_0/a를 변화시키려면 β나 그리드 간격 a를 바꿔야. 어제는 disk radius를 변경해서 ζ를 조절했는데, radius 변경이 mass constraint를 바꿀 수 있음.

→ 오늘 G1에서는 ζ를 fix하고 position만 scan. ζ는 어제 super-lattice case 그대로 (0.7-1.0).

### 8.3 V5b의 "99% overlap"은 averaged이거나 single-seed

어제 test가 single IC에서의 단일 result였다면, splitting이 다른 IC에서도 consistent한지 확인 필요.

→ G1에서 multiple seeds로 검증.

### 8.4 Split이 numerical artifact일 가능성

Hessian eigenvalue 계산의 수치 정밀도 이슈 (double-precision, finite-difference Hessian vs exact Hessian). Near-degenerate eigenvalue pair는 numerical splitting에 취약.

→ 어제 `CODE/scc/energy.py` exact gradient가 FD 검증 (1e-9)되어 있으므로 이 가능성 낮음. 그러나 super-lattice에서의 near-degenerate case에서 추가 확인 권장.

---

## §9. 세션 우선순위와 approach 선택

### 9.1 primary approach 선택 (G2)

**PN-based analytical approach를 primary로**:

이유:
1. 가장 explicit한 functional form 예측 (falsifiable)
2. 1D FK model에서 잘 확립된 analogy
3. 어제 `26b_FK_analogy.md`에서 이미 framework 준비됨
4. Fourier decomposition이 동일 결론 지지 (§4)

대안 (irrep splitting)은 **supporting 언어**로 병용 — 두 접근이 consistent하면 더 강한 claim 가능.

### 9.2 세션 구조 권고

**아침 (이론 먼저)**:
- PN potential의 2D 수식 정리 (`02_development.md` §1-§3)
- Effective mass 계산 (`02_development.md` §4)
- Leading-order splitting formula 도출 (`02_development.md` §5)
- Position-dependent 예측 열지도 작성 (analytical) (`02_development.md` §6)

**오후 (수치 검증)**:
- G1: L=40 position scan 실험 (`CODE/scripts/splitting_position_scan.py`)
- 이론 vs 수치 비교 (`03_integration_and_new_open.md`)

**저녁**:
- NQ-169 이론 분해 스케치 (`02_development.md` §7)
- σ-framework 연결 (`03_integration_and_new_open.md`)
- weekly_draft_storming에 entry

### 9.3 성공 기준 재확인

최소 합격선: **splitting이 position scan에서 사인파 패턴을 보이고, PN leading-order formula의 정성적 agreement 확인** (Cat B candidate).

이상적: 정량적 agreement + effective mass 계산 + Cat A elevation 경로 명확.

---

## §10. 핵심 deep questions (세션 중 돌아볼)

- **Q-D9**: splitting mechanism이 PN이라면, SCC는 "soliton on lattice"의 한 instance. 그런데 SCC의 closure + separation 효과가 PN potential을 **질적으로** 수정하는가, 아니면 단지 coefficient $V_0$를 바꾸는가? 전자라면 SCC-specific PN이론이 필요.

- **Q-D10**: Goldstone doublet의 splitting이 σ-signature에 어떻게 포함되는가? "Post-Goldstone eigenvectors"로 시작하는 Axiom S1' v1이 super-lattice에서 σ를 제대로 정의하는가? 혹시 σ가 regime-dependent하게 정의되어야 하는가?

- **Q-D11**: 오늘 발견되는 splitting mechanism이 **ζ_* 경계**(≈0.3-0.4)의 이론적 기원을 설명하는가? $V_0 \sim \lambda_{\mathrm{gap}}$ 조건으로부터 ζ_*의 closed form 도출 가능한가?

- **Q-D12**: PN potential이 존재한다면, disk가 lattice에서 **pinned** 되는 조건이 있는가? 즉 특정 $(x_0, y_0)$에서 equilibrium이 고정되고 perturbation에 의해 이동하지 않는 상황. 이것이 SCC formation의 "positional stability"와 어떤 관계인가?

---

## §11. 오늘 세션의 narrative

어제 V5b가 "Goldstone exists + splitting discovered"를 확립했다. 오늘은 이 splitting의 **왜**를 답한다. 어제의 교훈 (3번의 skeptical 반복이 올바른 picture를 강제)을 오늘도 적용: 수치 결과가 이론 예측을 지지하지 않으면 지지하지 않는다고 명시하고 이론 수정.

성공 시 Theorem 1의 remaining Cat C (super-lattice splitting mechanism)가 Cat B → Cat A로 승급 가능. 실패 시 다음 세션의 실험 설계가 더 구체화된다.

**어느 쪽이든 오늘은 V5b를 V6으로 발전시키는 작업.**

---

**End of pre_brainstorm.md for 2026-04-25.**
**Theme: "Observed splitting" → "Explained splitting". Peierls-Nabarro as primary theoretical vehicle. σ-framework Goldstone treatment as structural goal.**
