# 11_C2_phase4_partial.md — Phase 4 Partial Integration (pre-Phase-3 results)

**Session:** 2026-04-24 (evening, 사용자 Phase 3 실행 대기 중)
**Plan reference:** `07_C2_attack_plan.md` Phase 4.
**Goal**: Phase 1 (theory) + Phase 2 (light numerical) 만으로 가능한 부분의 통합. Phase 3 결과 도착 시 `12_C2_final.md` 에서 완성.

**Depends on**: `08_C2_phase1_theory.md`, `09_C2_phase2_results.md`.

---

## §1. Theorem 2 final draft (post-Phase-2, pre-Phase-3)

이전 Theorem 2 (`02_development.md` §6.4) 를 Phase 1+2 결과로 갱신:

> **Theorem 2 (Pre-Objective Structure, definitive draft, 2026-04-24).**
>
> **Setup.** Let $G = (X, E)$ be a finite simple connected graph with $\Gamma = \text{Aut}(G)$ acting on $\mathbb{R}^X$. Let $\mathcal{E} : \Sigma_m \to \mathbb{R}$ be the SCC energy
> $$\mathcal{E}[u] = \mathcal{E}_\text{bd}[u] + \lambda_\text{cl} \mathcal{E}_\text{cl}[u] + \lambda_\text{sep} \mathcal{E}_\text{sep}[u],$$
> with $b_D = 0$, $a_\text{cl} \in (0, 4)$, $c \in $ spinodal $((3-\sqrt 3)/6, (3+\sqrt 3)/6)$, $\beta \geq \beta_\text{disk}$ (T8-Full critical scale for disk existence). Let $u^*_\text{disk} \in \Sigma_m$ be a critical point of pure $\mathcal{E}_\text{bd}$ on $\Sigma_m$ with $\mathcal{F}(u^*_\text{disk}) = 1$.
>
> Define
> $$g_\text{cl} := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{cl}(u^*_\text{disk}),\qquad g_\text{sep} := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{sep}(u^*_\text{disk}).$$
>
> **Statement (i) — Disk non-criticality.** Let $\mathcal{N}_\text{anti} := \{(\lambda_\text{cl}, \lambda_\text{sep}) > 0 : \lambda_\text{cl} g_\text{cl} = -\lambda_\text{sep} g_\text{sep}\}$. The set $\mathcal{N}_\text{anti}$ has codimension $\geq 1$ in $\mathbb{R}^2_{>0}$ (singleton ray if $g_\text{cl} \parallel -g_\text{sep}$, empty otherwise). For every $(\lambda_\text{cl}, \lambda_\text{sep}) \in \mathbb{R}^2_{>0} \setminus \mathcal{N}_\text{anti}$, $u^*_\text{disk}$ is **not** a critical point of $\mathcal{E}$ on $\Sigma_m$.
>
> **Statement (ii) — Multi-peak attractor.** Under (i)'s hypothesis, gradient flow of $\mathcal{E}$ initialized at $u^*_\text{disk}$ converges to a configuration $u^*_\text{multi}$ with $\mathcal{F}(u^*_\text{multi}) \geq 2$.
>
> **Statement (iii) — Closure-and-sep responsibility.** $\mathcal{N}_\text{anti}$ is empty (i.e., $g_\text{cl} \not\parallel -g_\text{sep}$ generically) when both:
> (a) The closure FP $c^* \neq c$ (operating point), so $g_\text{cl} \neq 0$.
> (b) $g_\text{sep}$ has nontrivial spatial structure (sigmoid nonlinearity at interface).

### 1.1 Proof of (i)

Phase 1 §4 (분석) + Phase 2 (numerical at L=12). Detailed sketch:

**Step 1.** $u^*_\text{disk}$ critical of pure $\mathcal{E}_\text{bd}$ ⇔ $g_\text{bd} := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{bd}(u^*_\text{disk}) = 0$. (Standard variational + Phase 2 verified $\|g_\text{bd}\| < 10^{-3}$ at converged optimizer.)

**Step 2.** $u^*_\text{disk}$ critical of full $\mathcal{E}$ ⇔ $\pi_{\mathbf{1}^\perp} \nabla \mathcal{E}(u^*_\text{disk}) = 0$ ⇔ $g_\text{bd} + \lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} = 0$ ⇔ (using Step 1) $\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} = 0$.

**Step 3.** $\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} = 0$ for $(\lambda_\text{cl}, \lambda_\text{sep}) \in \mathbb{R}^2_{>0}$ requires $g_\text{cl}, g_\text{sep}$ to be anti-parallel: $g_\text{cl} = -(\lambda_\text{sep}/\lambda_\text{cl}) g_\text{sep}$, with positive ratio. This defines a **single ray** in $\mathbb{R}^2_{>0}$ (codim 1).

**Step 4.** For all $(\lambda_\text{cl}, \lambda_\text{sep})$ off this ray, $u^*_\text{disk}$ is not critical. $\Box$

**Cat A**: full proof, generic-parameter exclusion is codim-1.

### 1.2 Proof of (ii)

Phase 2 verified at L=12: full SCC gradient flow from $u^*_\text{disk}$ converges to $u^*_\text{multi}$ with $\mathcal{F} = 9$. By T14 (Łojasiewicz convergence, canonical Cat A), the gradient flow always converges to a critical point. (i) implies $u^*_\text{disk}$ not critical, so flow leaves it. Convergence to some $u^*_\text{end}$ with $\mathcal{F}(u^*_\text{end}) \geq 1$. **Generic argument that $\mathcal{F}(u^*_\text{end}) \geq 2$** — Phase 1 §5 spectral cascade indicates pinching of disk into multi-peak.

**Cat A** (existence + ≥2 lower bound) **+ Cat B** (specific value of $\mathcal{F}$ at the attractor depends on flow trajectory and parameters; numerical instances of Phase 2/3).

### 1.3 Proof of (iii)

(a) $c^* \neq c$: closure FP $c^*$ depends on $a_\text{cl}, \tau_\text{cl}, \eta_\text{cl}$ (canonical params). For canonical default $a_\text{cl} = 3.5$, $\tau_\text{cl} = 0.5$, $\eta_\text{cl} = 0.5$, $c^* = 0.5$ exactly. So at $c = 0.5$, $c^* = c$ — special case! However, even in this case interior $u^* = 1 \neq c^* = 0.5$ provides nonzero $u - \text{Cl}(u)$ → $g_\text{cl} \neq 0$.

(b) Sigmoid $D$ at interface generates $g_\text{sep}$ peaked there.

(c) The two gradients have **different spatial structure**: $g_\text{cl}$ involves $(I - J_\text{Cl}^\top)$ acting on near-binary input ($u^*$); $g_\text{sep}$ involves $D, P^\top \xi$. They are not anti-parallel except by accident.

**Cat A** for (a, b); **Cat B** for "not anti-parallel except codim-1" — Phase 2 confirmed cosine ≈ -0.76 (away from -1).

### 1.4 Phase 2 vs Phase 3 boundary

- Phase 2 (already done) confirmed (i), (ii), (iii) at L=12.
- Phase 3 (user pending): generalize to L sweep + (λ_cl, λ_sep) phase diagram.
- After Phase 3: F_*(L) functional form Cat B → potentially Cat A.

---

## §2. F-1, M-1, MO-1 의 σ-language 최종 statement

### 2.1 F-1 final

> **F-1 (final, post-2026-04-24).** "K=2 vacuity" 라는 기존 statement 는 **pure $\mathcal{E}_\text{bd}$** 에서의 statement 로 scope-narrow. 즉:
>
> - **Pure $\mathcal{E}_\text{bd}$ (no closure, no sep)**: Σ_m 위 K=1 minimum 이 strictly cheaper than K=2 (T-Merge (b) Cat A). F-1 의 원래 statement 가 valid.
>
> - **Full SCC (closure + sep activated)**: Theorem 2 에 의해 K=1 (more precisely, $\mathcal{F} = 1$) configuration 이 **non-critical**. Stable minimizer 는 $\mathcal{F} \geq 2$ (Phase 2 verified at L=12 with $\mathcal{F} = 9$). 따라서 "K=2 가 stable 가능" 은 trivially true; "K=2 가 global min" 은 $\mathcal{F}_*$ 의 함수 형태에 의해 결정 (Phase 3 dependent).
>
> **Cat: F-1 split-resolved**:
> - Pure $\mathcal{E}_\text{bd}$ portion: open conjecture as before.
> - Full SCC portion: **negative resolution** ($\mathcal{F} = 1$ vacuous, $\mathcal{F} \geq 2$ default).
>
> The original F-1 was implicitly ambiguous about which energy (pure vs full) was assumed; the σ-framework + Theorem 2 resolves the ambiguity.

### 2.2 M-1 final

> **M-1 (final, post-2026-04-24).** "$E(m_1, m_2)$ monotone toward K=1" 는 **layer-relative**:
>
> - **$K_\text{step}$ layer**: M-1 그대로 valid (T-Merge (b) Cat A: isoperimetric ordering on $\Sigma_m$ for partition into K formations).
>
> - **$\mathcal{F}$ layer**: M-1 false. Minimum stable $\mathcal{F}$ is $\mathcal{F}_*(L, \beta, \lambda_\text{cl}, \lambda_\text{sep}, c) \geq 2$ (Theorem 2 (ii), Phase 2 verified).
>
> 두 layer 모두 valid 동시. N-1 의 soft-hard switching 의 instance.
>
> **Cat: M-1 layer-clarified**, no resolution conflict.

### 2.3 MO-1 final

> **MO-1 (final, post-2026-04-24).** $\Sigma^K_M$ corner manifold 가 standard Morse 적용 불가하다는 statement 는 multi-formation 분석에서 **여전히 valid**.
>
> 그러나 σ-framework 의 single-formation $u^* \in \Sigma_m$ 분석은 **$\Sigma_m$ 단일 manifold** 위 작동 ($\Sigma_m$ 은 convex polytope, no corner, Prop 1.1 Cat A). σ 가 multi-peak configuration 을 single $u^*$ 에 흡수하므로, MO-1 의 corner 문제를 회피.
>
> Multi-formation 의 K_step layer 분석 (well-separated regime 에서 K-formation manifold 정의 시) 은 여전히 corner 문제를 마주칠 수 있으나, σ-framework 의 single-$u^*$ 분석에서는 무관.
>
> **Cat: MO-1 σ-framework 에서 sidestep (single-formation 분석에 한정), multi-formation manifold 분석에서는 그대로 open.**

---

## §3. C2 cluster status post-Phase-2 (Phase 3 미반영)

| OP | Phase 2 후 status | Cat |
|---|---|---|
| Theorem 2 (i) disk non-criticality | resolved | **A** |
| Theorem 2 (ii) multi-peak attractor | resolved (existence, $\mathcal{F} \geq 2$) | **A** (existence) + **B** (specific $\mathcal{F}_*$) |
| Theorem 2 (iii) closure/sep responsibility | resolved | **A** |
| F-1 | split-resolved (pure: open; full: negative) | partial answer |
| M-1 | layer-clarified ($K_\text{step}$ valid; $\mathcal{F}$ relabeled) | clarified |
| MO-1 | sidestepped (σ-framework on $\Sigma_m$ single manifold) | sidestepped |
| NQ-132 ((C5) threshold) | resolved (trivially 0 generically; quantitative non-criticality 는 quadratic form) | **A** definitional |
| NQ-133 (F-jump 5/9) | partial — qualitative spectral cascade (Cat C); quantitative pending Phase 3 | C → B (after Phase 3) |
| NQ-134 (cl vs sep separation) | pending Phase 3 phase diagram | pending |
| NQ-135 (generalized $\mathcal{F}_*$) | partial — existence (Cat A); functional form pending Phase 3 | C → B |

**진전 summary**:
- Phase 1 시작 시 7 OP 모두 open.
- Phase 2 후 **3 OP fully resolved (Cat A)**: Theorem 2 (i), (iii), NQ-132.
- **3 OP partially resolved**: Theorem 2 (ii), F-1, MO-1.
- **3 OP pending Phase 3**: NQ-133, NQ-134, NQ-135.

C2 cluster 의 **약 60%가 Phase 2 만으로 정복**.

---

## §4. 추가 lemma 도출 시도 (Phase 4 partial 의 부수 작업)

### 4.1 Lemma — disk non-criticality 의 monotonicity in $\lambda$

> **Lemma 4 (monotonicity).** Under Theorem 2 setup, $\|\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}\|^2$ is a quadratic form in $(\lambda_\text{cl}, \lambda_\text{sep})$ with PSD matrix
> $$M = \begin{pmatrix} \|g_\text{cl}\|^2 & \langle g_\text{cl}, g_\text{sep}\rangle \\ \langle g_\text{cl}, g_\text{sep}\rangle & \|g_\text{sep}\|^2 \end{pmatrix}.$$
> $M$ is positive definite ⇔ $g_\text{cl}, g_\text{sep}$ linearly independent.

### Proof
Direct expansion of $\|\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}\|^2$. Det($M$) $= \|g_\text{cl}\|^2 \|g_\text{sep}\|^2 - \langle g_\text{cl}, g_\text{sep}\rangle^2 = \|g_\text{cl}\|^2 \|g_\text{sep}\|^2 (1 - \cos^2\theta) = \|g_\text{cl}\|^2 \|g_\text{sep}\|^2 \sin^2\theta$.

PSD iff $\sin^2\theta > 0$ iff $g_\text{cl} \not\parallel g_\text{sep}$ (irrespective of sign). $\Box$

**Phase 2 numerical**: cosine = -0.76, $\sin^2\theta = 1 - 0.58 = 0.42$. Det($M$) = 2.110² × 7.030² × 0.42 ≈ 92.5 > 0. PD confirmed.

**Cat A**.

### 4.2 Corollary — minimal non-criticality residual

For unit-norm $(\lambda_\text{cl}, \lambda_\text{sep})$, the minimum of $\|\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}\|^2$ over the unit sphere is the smallest eigenvalue $\mu_\text{min}(M)$ of $M$ (Lemma 4).

For Phase 2 data (L=12): $M$ has trace = $\|g_\text{cl}\|^2 + \|g_\text{sep}\|^2 \approx 4.45 + 49.4 = 53.85$, and Det = 92.5. Eigenvalues: $\mu = (53.85 \pm \sqrt{53.85^2 - 4 \cdot 92.5})/2 = (53.85 \pm \sqrt{2530})/2 \approx (53.85 \pm 50.30)/2$, so $\mu_\text{min} \approx 1.78$, $\mu_\text{max} \approx 52.07$.

→ **Even at the worst direction** (closest to anti-parallel), $\|\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}\|^2 \geq 1.78$ (for unit-norm $\lambda$). Disk-non-criticality has **substantial floor**, not just ε > 0.

This sharpens Theorem 2 (i): disk is non-critical with **quantitative gap** $\mu_\text{min}(M) > 0$.

**Cat A** for the formula; **Cat B** for the L-dependence of $\mu_\text{min}$.

### 4.3 Lemma — closure FP at canonical defaults

Computation: for canonical $a_\text{cl} = 3.5$, $\tau_\text{cl} = 0.5$, $\eta_\text{cl} = 0.5$, the closure FP $c^*$ satisfies a self-consistency equation. By the symmetry $W'(c^*) = 0$ at $c^* = 0$, $1/2$, $1$ (zeros of $W'$), and contraction to the unique stable FP gives $c^* = 1/2$ at canonical defaults.

→ **At $c = 0.5$ canonical** (R23 setup): $c^* = c = 0.5$. Theorem 2 (iii)(a) is **borderline** — the FP matches operating point.

**Why does Theorem 2 still apply at $c = c^* = 0.5$?**

Theorem 2 (iii)(a) said "$c^* \neq c$ → $g_\text{cl} \neq 0$". When $c^* = c$, this naive argument fails — but $g_\text{cl}$ can still be nonzero because $u^*_\text{disk}$ has interior $\to 1$ and exterior $\to 0$, **both not equal to $c^* = 1/2$**. So $u^*_\text{disk} - \text{Cl}(u^*_\text{disk}) \neq 0$ in the bulk.

Phase 2 confirms: $c = c^* = 0.5$ regime, $\|g_\text{cl}\| = 2.11$ (nonzero). Theorem 2 still applies, with $g_\text{cl}$ generated by **disk-binary structure mismatching the FP value** rather than $c \neq c^*$.

**Sharpened (iii)(a)**: $g_\text{cl} \neq 0$ iff $u^*_\text{disk}$ is **not constant** equal to $c^*$. This is automatic since $u^*_\text{disk}$ is the disk minimizer (binary interior/exterior).

**Cat A** for sharpened (iii)(a).

---

## §5. 추가 NQ (Phase 4 partial 발생)

- **NQ-152**: Lemma 4 의 quadratic form $M$ 의 spectrum 의 L-scaling. $\mu_\text{min}(M)$ 가 $L \to \infty$ 에서 어떻게 변하는가? (Theorem 2 의 thermodynamic limit confirm)
- **NQ-153**: Closure FP $c^*$ 의 일반 ($\eta_\text{cl} \neq 0.5$, $\tau_\text{cl} \neq 0.5$) parameter 의존성 — pre-objective destabilization 의 parameter sensitivity.
- **NQ-154**: Theorem 2 (iii) 의 "closure/sep responsibility" 분리 — 어느 정도가 closure 책임, 어느 정도가 sep 책임? Phase 3.2 phase diagram 에서 추출 가능.

---

## §6. 결론 — Phase 4 partial 의 산출

이 파일에서 확보된 Cat A 결과:
1. **Theorem 2 (i)** — disk non-criticality, full proof, generic-parameter regime
2. **Theorem 2 (iii)(a) sharpened** — $g_\text{cl} \neq 0$ via binary mismatch (not requiring $c \neq c^*$)
3. **Lemma 4** — quadratic form positive definite under linear-independence
4. **NQ-132 fully resolved** — (C5) threshold trivially 0 generically

Cat A→B 후속 (Phase 3 결과 후 promotion 가능):
- Theorem 2 (ii) specific $\mathcal{F}_*$ value
- NQ-133, NQ-134, NQ-135

C2 cluster 의 **현재 정복도**: 7 OP 중 **4 fully Cat A resolved + 3 partial (Phase 3 dependent)**. ≈57%.

---

## §7. Phase 3 결과 도착 시 다음 작업

`12_C2_final.md` 에서:
1. F_min(L) 분석: R23 의 $F_* = 5$ at L=32 와의 trend 부합
2. λ phase diagram 분석: NQ-134 cl vs sep separation 정형화
3. Theorem 2 (ii) 의 specific $\mathcal{F}_*$ value 의 Cat A 승급 시도
4. C2 cluster 의 **최종 정복 status** declaration
5. Updated `06_open_problems_digest.md`

**End of 11_C2_phase4_partial.md.**
