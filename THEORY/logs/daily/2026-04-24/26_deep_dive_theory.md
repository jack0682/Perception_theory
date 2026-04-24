# 26_deep_dive_theory.md — Deep Dive Theoretical Framework

**Session:** 2026-04-24 (final late night, post-falsification deep analysis)
**Purpose:** 이전 dual-regime falsification (`25_*.md`) 후 critical mode 와 Goldstone 의 결정적 구분 + mechanism 정확한 identification.
**Depends on:** `25_dual_regime_falsification.md`, canonical T-Birth-Parametric (Cat A), Frenkel-Kontorova theory.

---

## §1. 정확한 질문 재정립

이전 세션이 **dual-regime (sub vs super lattice)** 를 주장했으나 falsified. 남은 핵심 질문들:

1. **Near-zero mode 가 정확히 뭔가?** — translation Goldstone vs Fiedler-related soft mode vs 제3 mechanism
2. **Critical slowing down 의 exact form** — Landau mean field (ν=1) 확인
3. **Genuine Goldstone 의 existence** — β/β_crit fixed (far from critical) 로 decoupled test
4. **이중 (또는 다중) regime 이 진짜 있다면 어떤 parameter 공간에서?**

이 세 질문의 정확한 답이 SCC 이론의 spectral structure 의 정확한 이해에 필요.

---

## §2. 이론적 prediction framework

### 2.1 Near-zero mode 의 세 가지 가능한 정체

**(A) Translation pseudo-Goldstone** (Goldstone):
- Origin: broken translation symmetry
- 2D torus: 2-fold degenerate doublet (x, y)
- Overlap: 강 overlap with $\delta u_x = u^*(\cdot + e_1) - u^*$ 등
- Scaling: λ_0 ~ exp(-c r_0/ξ_0) (Peierls-Nabarro)
- L-dependence: λ_0 → 0 as L → ∞ (continuum limit)

**(B) Fiedler-like critical soft mode** (Landau):
- Origin: pitchfork bifurcation at β_crit
- Single mode (non-degenerate)
- Overlap: 강 overlap with Fiedler eigenvector $\phi_2$ of Laplacian
- Scaling: λ_0 ~ (β - β_crit)^ν, Landau ν = 1
- L-dependence: β_crit decreases with L → effect tamed at large L

**(C) Other (unknown)**:
- 위 두 가지 모두 not dominant
- 요구: 새로운 mechanism proposal

Phase 1 eigenvector projection 이 결정적 test.

### 2.2 이전 관측이 암시하는 것

`25_*.md` 의 3 evidences:
- Only ONE near-zero mode (not doublet) → (B) 지지
- L 증가 시 λ_0 증가 → (B) 지지
- Smooth monotonic (no transition) → (B) 지지

**Phase 1 eigenvector analysis 가 이를 definitively confirm 할 것**.

---

## §3. Goldstone 의 수학적 criterion

Goldstone 을 mathematically identify 하려면:

### 3.1 Exact Goldstone (continuum torus)

$u^*$ 가 translation orbit 위에 있고 이 orbit 이 연속적이면: $\partial_\alpha u^* =$ translation mode is **exact null direction** of H[u*] projected to constraint.

**Test**: $H(u^*) \cdot \delta u_x \approx 0$ (numerically).

### 3.2 Discrete torus pseudo-Goldstone

Discrete lattice 에서 "translation" 은 permutation (finite group action). 하지만 continuum limit 에서:
- $\delta u_x$ becomes continuum $\partial_x u^*$
- Near-null direction 의 eigenvalue $\approx$ PN barrier

**Test**: $\langle \delta u_x, H \delta u_x\rangle / \|\delta u_x\|^2 \ll \lambda_1$ (first non-tangent eigenvalue).

### 3.3 중요한 distinction

**Eigenvector overlap** with $\delta u_x$ vs **Rayleigh quotient** along $\delta u_x$ 구분:

- **Overlap test**: lowest eigenvector $\phi_0$ 와 $\delta u_x$ 의 inner product. 만약 $|\langle \phi_0, \delta u_x\rangle| > 0.7$, Goldstone character dominant.
- **Rayleigh test**: $\delta u_x$ 를 candidate 방향으로 쓰고 Hessian projection quotient 계산. 만약 작으면 "soft along this direction".

두 test 가 다를 수 있다 — e.g., $\delta u_x$ 가 여러 eigenmodes 의 combination 이면 overlap 이 분산되어 작지만 Rayleigh 는 여전히 작음.

**가장 decisive**: **eigenvector overlap**. 만약 $\phi_0$ 가 $\delta u_x$ 와 orthogonal, 그것은 Goldstone 아님 (다른 mechanism).

---

## §4. Landau pitchfork soft mode 의 정확한 form

T-Birth-Parametric (canonical Cat A) 에 의한 pitchfork bifurcation:

### 4.1 Standard Landau analysis

Near critical point $\beta_c$, amplitude $a$ of bifurcating mode satisfies:
$$F(a) = -\frac{1}{2} r(\beta) a^2 + \frac{1}{4} u a^4 + \text{higher order}$$
with $r(\beta) = c_r (\beta - \beta_c)$.

**Above critical** ($\beta > \beta_c$, $r > 0$): minimum at $a^* = \sqrt{r/u}$. Energy $F(a^*) = -r^2/(4u)$.

**Hessian at minimum**: 
$$\partial^2_a F|_{a = a^*} = -r + 3u a^{*2} = 2r = 2c_r(\beta - \beta_c)$$

So soft mode eigenvalue **exactly linear in $(\beta - \beta_c)$** with Landau.

### 4.2 Prediction

$$\lambda_0^\text{soft}(\beta) = 2c_r (\beta - \beta_c) \cdot \text{(prefactor from prefer)}$$

Fit: $\lambda_0 = A (\beta - \beta_c)^\nu$ with $\nu = 1$.

**Mean field (Landau) prediction ν = 1**.

### 4.3 Mode identification

Bifurcation eigenmode at $\beta = \beta_c$: the **lowest Laplacian eigenvector** (Fiedler) above uniform $c\mathbf{1}$. For torus L×L:
- Fiedler eigenspace 4-dim: $\{\cos(2\pi i/L), \sin(2\pi i/L), \cos(2\pi j/L), \sin(2\pi j/L)\}$
- Disk minimizer breaks this — single direction "selected"

**Post-bifurcation**: $u^* \approx c\mathbf{1} + a^* \cdot \phi_\text{chosen}$ with $\phi_\text{chosen}$ = axis-aligned Fiedler component (R22 §3.3 cubic coefficient).

**Soft mode at post-bifurcation**: 동일 방향 Fiedler eigenvector, but now with quadratic curvature $2c_r(\beta - \beta_c)$.

**Test**: eigenvector overlap with Fiedler Laplacian eigenvector should be LARGE (not zero).

---

## §5. Exponential decay 의 정확한 form

Phase B 에서 관측한 smooth exponential decay:
$\log \lambda_0 \sim -c/\zeta^n$ (accelerating).

### 5.1 Landau prediction

$\lambda_0 = 2c_r (\beta - \beta_c)$ where $\beta = 1/\zeta^2$.

In limit $\zeta \to \zeta_\text{crit} = 1/\sqrt{\beta_c}$: 
$\lambda_0 \to 0$ linearly in $(1/\zeta^2 - \beta_c)$ = $(1 - \beta_c \zeta^2)/\zeta^2$

**Near $\zeta_\text{crit}$**: $\lambda_0 \propto (\zeta_\text{crit} - \zeta)/\zeta_\text{crit}$ (linear in $\zeta$).

### 5.2 반증 test

Phase 3 에서 fit $\lambda_0 \sim (\beta - \beta_c)^\nu$:
- $\nu \approx 1$: Landau confirmed
- $\nu \neq 1$: Different universality

만약 $\nu = 1$: near-zero mode 는 definitively critical pitchfork soft mode, Goldstone 아님.

만약 $\nu$ 이상한 값: something else (e.g. 3D Goldstone with 2D lattice crossover?).

---

## §6. Goldstone 의 Decoupled Test

### 6.1 Protocol 설명

Large L (L=40) torus: β_crit ≈ 0.049. β=1 (ζ=1) at L=40: β/β_crit = 20 (far from critical).

만약 이 decoupled regime 에서:
- 여전히 near-zero mode 존재 + overlap with $\delta u_x$ ≈ 0.7+ → **genuine Goldstone exists**
- 모든 eigenvalues ≫ 0 (orbital scale) → **no Goldstone, critical만이 전부였음**

### 6.2 Theoretical expectation

Goldstone 은 translation symmetry breaking 의 natural consequence. Physical systems (continuum SCC):
- Smooth interface 에서 translation mode 는 **exact null direction** (conservation law)
- Discrete lattice: PN barrier 로 near-zero (not exact)
- L → ∞ + continuum limit: exact zero

If SCC has true Goldstone in super-lattice continuum limit, it should emerge at large L + large ξ_0. Phase 2 testing this.

### 6.3 Critical insight

Even if **no near-zero mode** 가 Phase 2 에서 나오면:
- 이전 "dual-regime" 완전 반증
- SCC 는 single-regime spectrum structure — all modes orbital scale
- 이전 관측된 near-zero 는 모두 critical artifact

**가장 honest 한 결과**: L=40 decoupled에서 **모든 mode 가 O(β) 이면** SCC Goldstone physics 는 없음을 확정.

---

## §7. Session narrative 의 evolution

Theorem 1 의 iterations:
- **V1 (morning)**: Goldstone universal — falsified
- **V2 (G1)**: 3-geometry (T/T_off/O) — replaced
- **V3 (C3-T)**: regime-based (sub/super) — falsified
- **V4 (25_*.md)**: 2D parameter space (ζ, ρ) — hypothesis
- **V5 (this deep dive)**: pending Phase 1+2+3 결과

각 iteration 이 **더 세밀한 test** 후 refine 됨. Deep dive 의 결과:
- If Goldstone confirmed at decoupled regime → V5 = (ζ, ρ) 2D parameter space with super-lattice Goldstone at large β/β_crit 
- If no Goldstone in decoupled regime → V5 = "critical slowing down everywhere, no true Goldstone"

---

## §8. 이론적 stakes

이 deep dive 가 결정할 것:

### 8.1 Super-lattice Goldstone 존재 여부

존재 확인 시:
- 이전 dual-regime claim partial 복구
- Large L continuum limit 에서 genuine Goldstone physics
- PN barrier theory 적용 가능

Non-존재 확인 시:
- SCC 는 bounded-λ spectrum 만 보유 (unless at critical)
- Super-lattice limit 에서 특이 physics 없음
- 이전 dual-regime claim 완전 폐기

### 8.2 Critical universality

Landau ν = 1 confirmed 시:
- T-Birth-Parametric 의 standard pitchfork nature 재확인
- SCC 는 standard symmetry-breaking bifurcation

Landau 위반 시:
- Non-mean-field critical physics
- Novel SCC feature

### 8.3 σ-framework 의 validity

σ-framework 는 regime-independent definition. 하지만 **interpretation** 이 regime 에 의존. Deep dive 결과가:

σ 의 interpretation 을 어떻게 refine 할지 결정:
- If super-lattice Goldstone exists: σ 에 translation-soft modes (Goldstone) 과 orbital modes 구분
- If no Goldstone: σ 의 modes 모두 orbital 또는 critical soft; 더 simple 한 taxonomy

---

## §9. 실험 완료 후 예상 action

### 9.1 If Phase 1 shows Fiedler-dominant lowest mode

- Phase 2 large L 에서도 같은 pattern 이면: critical slowing only
- Phase 3 exponent ν ≈ 1 이면: Landau mean field 확인
- Theorem 1 V5: "bifurcation soft mode (ν=1), no Goldstone"

### 9.2 If Phase 1 shows translation-dominant lowest mode

- Reconsider: Goldstone 부분적 존재 가능
- Phase 2 large L 에서 decoupled Goldstone 확인 필요
- Theorem 1 V5: "dual-regime with genuine Goldstone at super-lattice + far from critical"

### 9.3 If mixed result

- Phase 2 + Phase 3 결과로 정제
- Theorem 1 V5: 복잡한 3-regime 또는 nuanced picture

---

## §10. 결과 대기 중

Monitor 실행 중. 결과 도착 시 즉시:
1. Phase 1 eigenvector overlap 값 해석
2. Phase 2 decoupled test L=40 결과 check
3. Phase 3 critical exponent ν 추출

다음 파일: `27_deep_dive_results.md` (결과 + interpretation + Theorem 1 V5).

**End of 26_deep_dive_theory.md.**
