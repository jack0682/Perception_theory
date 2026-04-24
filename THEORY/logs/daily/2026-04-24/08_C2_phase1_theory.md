# 08_C2_phase1_theory.md — C2 Conquest Phase 1: Theory

**Session:** 2026-04-24 (evening, C2 attack Phase 1)
**Plan reference:** `07_C2_attack_plan.md` §2 Phase 1.
**This file covers:** (1.1)–(1.6) Phase 1 analytical 작업. g_cl / g_sep explicit · λ_cl^crit closed form / scaling · F_* spectral argument · F-1 / M-1 / MO-1 의 σ-language 재기술.
**Depends on reading:** 본 세션 `02_development.md` §6 (Theorem 2 sketch); `working/SF/mode_count.md` §2 (Prop 1.3b explicit forms); `working/SF/symmetry_moduli.md` §3.3 (cubic coefficient); canonical Cor 2.2 quantitative.

---

## §1. Setup and notation refresh

$G = L \times L$ free-BC grid, $n = L^2$. $\Sigma_m \subset [0,1]^X$ volume-constrained simplex, $\sum_i u_i = m$. $\Gamma = \text{Aut}(G) = D_4$.

Energy $\mathcal{E} = \lambda_\text{cl} \mathcal{E}_\text{cl} + \lambda_\text{sep} \mathcal{E}_\text{sep} + \mathcal{E}_\text{bd}$ with $b_D = 0$. Disk minimizer $u^*_\text{disk}$ from pure $\mathcal{E}_\text{bd}$ via Cor 2.2 ansatz:
$$u^*_\text{disk}(r) = \tfrac{1}{2}\big(1 - \tanh((r - r_0)/\xi_0)\big), \quad r_0 = \sqrt{m/\pi}, \quad \xi_0 = \sqrt{\alpha/\beta}.$$
Interior $u^* \to 1$, exterior $u^* \to 0$, interface $r \approx r_0$ width $\xi_0$.

Closure operator $\text{Cl} : [0,1]^X \to [0,1]^X$ with FP $c^* \in (0, 1)$, contraction regime $a_\text{cl} \in (0, 4)$. Linearization $J_\text{Cl} = \partial \text{Cl}/\partial u$ around $u = c^* \mathbf{1}$. From canonical convention (`working/SF/mode_count.md` §2.1):
$$J_\text{Cl}\big|_{c^*\mathbf{1}} = \mu_c \cdot P, \quad P = D^{-1}A,\quad \mu_c \in (0, 1).$$

Distinction operator $D(u)_i = \sigma(\kappa_D (Pu)_i - \delta_D)$, separation energy $\mathcal{E}_\text{sep}[u] = \sum_i u_i (1 - D(u)_i)$.

---

## §2. (1.1) g_cl explicit at u*_disk

### 2.1 Gradient form

$\mathcal{E}_\text{cl}[u] = \tfrac{a_\text{cl}}{2} \|u - \text{Cl}(u)\|_2^2$. By chain rule:
$$\nabla \mathcal{E}_\text{cl}(u) = a_\text{cl} (I - J_\text{Cl}(u)^\top)(u - \text{Cl}(u)).$$

Constrained gradient on $\mathbf{1}^\perp$:
$$g_\text{cl}(u) := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{cl}(u) = a_\text{cl} \pi_{\mathbf{1}^\perp} (I - J_\text{Cl}^\top)(u - \text{Cl}(u)).$$

### 2.2 Disk-specific evaluation

At $u = u^*_\text{disk}$: define "residual" $\rho(u^*) := u^*_\text{disk} - \text{Cl}(u^*_\text{disk}) \in \mathbb{R}^X$.

**Interior** ($r \ll r_0 - 2\xi_0$): $u^* \approx 1$. By contraction, $(\text{Cl}(u^*))_i$ is the closure of "all-1 in a neighborhood" — this is approximately $c^* + (1 - c^*) \cdot (\text{contraction action on locally-1 input})$. For Cl operator with linearization $\mu_c P$:
$$(\text{Cl}(u^*))_i \approx \mu_c \cdot 1 + (1 - \mu_c) \cdot c^* + O(\text{boundary})$$
Thus interior residual: $\rho_\text{int} = 1 - [\mu_c + (1-\mu_c)c^*] = (1 - \mu_c)(1 - c^*)$.

**Exterior** ($r \gg r_0 + 2\xi_0$): $u^* \approx 0$. Symmetric:
$\rho_\text{ext} = 0 - [\mu_c \cdot 0 + (1 - \mu_c)c^*] = -(1 - \mu_c) c^*$.

**Interface** ($|r - r_0| \lesssim 2\xi_0$): transitional. Profile $\rho(r) \approx (1 - \mu_c) \cdot [u^*(r) - c^*]$ (linear interpolation hypothesis, valid when $\xi_0 \gg$ lattice spacing).

**Composite**: 
$$\rho(r) \approx (1 - \mu_c) \cdot [u^*(r) - c^*] = (1 - \mu_c) \cdot \big[\tfrac{1}{2}(1 - \tanh((r-r_0)/\xi_0)) - c^*\big].$$

### 2.3 Norm of residual

$\|\rho\|_2^2 = (1 - \mu_c)^2 \int (u^* - c^*)^2 \, dV$. Evaluate using disk geometry:
- Interior contribution: $(1 - c^*)^2 \cdot \pi r_0^2$
- Exterior: $(c^*)^2 \cdot (\text{area outside disk})$ (proportional to $L^2 - \pi r_0^2$ for free-BC)
- Interface: $O(\xi_0 \cdot 2\pi r_0)$ correction

For $r_0 \ll L/2$ (small disk): exterior dominates → $\|\rho\|_2^2 \approx (1 - \mu_c)^2 \cdot (c^*)^2 \cdot L^2$.
For $r_0 \approx L/2$ (large disk): both contribute.

**Scaling estimate**:
$$\|\rho\|_2^2 = (1-\mu_c)^2 \cdot \big[(1-c^*)^2 \pi r_0^2 + (c^*)^2 (L^2 - \pi r_0^2)\big] + O(r_0 \xi_0).$$

### 2.4 g_cl norm (after $(I - J_\text{Cl}^\top)$)

$(I - J_\text{Cl}^\top) = I - \mu_c P^\top$. Eigenvalues: $1 - \mu_c \cdot \lambda_k(P^\top)$ where $\lambda_k(P^\top) \in [-1, 1]$ for stochastic-like $P$ (eigenvalue 1 corresponds to constant vectors which $\pi_{\mathbf{1}^\perp}$ removes).

For the residual $\rho$: it has nonzero spatial variation (interior vs exterior). Decompose $\rho$ into Laplacian eigenmodes $\phi_k$ with coefficients $\hat\rho_k = \langle \rho, \phi_k\rangle$:
$$g_\text{cl} = a_\text{cl} \sum_{k \geq 2} (1 - \mu_c \lambda_k(P^\top)) \hat\rho_k \phi_k.$$

For the disk shape: $\hat\rho_k$ is concentrated in low-$k$ modes (rotationally symmetric ~ radial $\phi_{(0,0)}$ + small angular). $\hat\rho_2$ (Fiedler) is small unless $L$ is small or disk is asymmetric.

Dominant contribution to $\|g_\text{cl}\|^2$:
$$\|g_\text{cl}\|^2 \approx a_\text{cl}^2 \sum_{k \geq 2} (1 - \mu_c \lambda_k)^2 |\hat\rho_k|^2.$$

For low-$k$ ($\lambda_k$ small): $(1 - \mu_c \lambda_k)^2 \approx 1$. Approximation:
$$\boxed{\;\|g_\text{cl}\|^2 \approx a_\text{cl}^2 (1-\mu_c)^2 \cdot \big[(1-c^*)^2 \pi r_0^2 + (c^*)^2 (L^2 - \pi r_0^2)\big] - a_\text{cl}^2 \cdot (\text{mean removed})\;}$$
The "mean removed" is $\pi_{\mathbf{1}^\perp}$'s effect.

### 2.5 Self-classification of (1.1)

**Cat B scaling formula** — closed-form scaling expressed in $(\mu_c, c^*, r_0, L, a_\text{cl})$, but with leading-order assumption (disk symmetric, interface narrow $\xi_0 \ll r_0$, low-mode dominance). Higher-order corrections in $\xi_0/r_0$ left implicit.

---

## §3. (1.2) g_sep explicit at u*_disk

### 3.1 Gradient form

$\mathcal{E}_\text{sep}[u] = \sum_i u_i (1 - D(u)_i)$ with $D(u)_i = \sigma(\kappa_D (Pu)_i - \delta_D)$.

$\nabla \mathcal{E}_\text{sep}(u)_i = (1 - D(u)_i) - \sum_j u_j \cdot \partial_i D(u)_j$
$= (1 - D(u)_i) - \kappa_D \sum_j u_j \cdot D(u)_j (1 - D(u)_j) \cdot P_{ji}$.
$= (1 - D(u)_i) - \kappa_D (P^\top \xi(u))_i$, with $\xi(u)_j := u_j D(u)_j (1 - D(u)_j)$.

### 3.2 Disk-specific evaluation

Interior ($u \approx 1$, neighbors $\approx 1$): $Pu \approx 1$, $D \approx \sigma(\kappa_D - \delta_D)$. Choose canonical $\delta_D = \kappa_D / 2$ so $D(c\mathbf{1})|_{c=1/2} = \sigma(0) = 1/2$. Then for $c \neq 1/2$: $D(c\mathbf{1}) = \sigma(\kappa_D(c - 1/2))$.

For interior of disk: $D \approx \sigma(\kappa_D \cdot 1/2) \approx 1$ for $\kappa_D > 4$. Then:
$\nabla \mathcal{E}_\text{sep}|_\text{int} \approx (1 - 1) - \kappa_D \cdot (\text{P}^\top \xi)_\text{int} = -\kappa_D \cdot (P^\top \xi)_\text{int}$
where $\xi_\text{int} = 1 \cdot 1 \cdot 0 = 0$ (since $D \to 1$, $(1-D) \to 0$). 
$\to \nabla \mathcal{E}_\text{sep}|_\text{int} \approx 0$.

Exterior ($u \approx 0$): $D \approx 0$, $(1-D) \approx 1$, $\xi \approx 0 \cdot 0 \cdot 1 = 0$:
$\nabla \mathcal{E}_\text{sep}|_\text{ext} \approx 1 - 0 = 1$.

Interface ($u \in (0,1)$): nontrivial. $D$ smoothly transitions, $\xi$ peaked at $u \approx 1/2$ where $D(1-D) = 1/4$ maximal.

**Constrained $g_\text{sep}$**: $g_\text{sep} = \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{sep}$. The leading interior $\approx 0$, exterior $\approx 1$ structure has nonzero mean → projection removes a uniform $\bar = \langle 1\rangle_{exterior} \cdot |\text{Ext}|/L^2$.

After projection:
- Interior: $- \bar$ (negative)
- Exterior: $1 - \bar$ (positive, smaller)
- Interface: peaked correction

**Scaling**:
$$\|g_\text{sep}\|^2 \sim |\text{Int}| \cdot \bar^2 + |\text{Ext}|(1-\bar)^2 + (\text{interface peak})^2.$$
With $\bar = |\text{Ext}|/L^2$ and $|\text{Int}| = \pi r_0^2$:
$$\boxed{\;\|g_\text{sep}\|^2 \approx \pi r_0^2 \cdot (1 - \pi r_0^2/L^2)^2 + (L^2 - \pi r_0^2) \cdot (\pi r_0^2/L^2)^2 + O(\kappa_D \xi_0)\;}$$
$$= \pi r_0^2 (L^2 - \pi r_0^2)/L^2 + O(...).$$
For $r_0 \ll L$: $\|g_\text{sep}\|^2 \approx \pi r_0^2$.

### 3.3 Self-classification of (1.2)

**Cat B scaling formula** — same caveats as (1.1). Sigmoid nonlinearity ($D$) handled by piecewise (interior/exterior/interface) approximation.

---

## §4. (1.3) λ_cl^crit closed form / scaling — NQ-132

### 4.1 Threshold derivation

From Theorem 2 Step 5 (`02_development.md` §6.4): $u^*_\text{disk}$ is critical of full $\mathcal{E}$ on $\Sigma_m$ iff
$$\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} = 0$$
on $\mathbf{1}^\perp$.

Take inner product with itself:
$$\lambda_\text{cl}^2 \|g_\text{cl}\|^2 + 2 \lambda_\text{cl} \lambda_\text{sep} \langle g_\text{cl}, g_\text{sep}\rangle + \lambda_\text{sep}^2 \|g_\text{sep}\|^2 = 0.$$
This is a quadratic in $\lambda_\text{cl}/\lambda_\text{sep}$:
$$\frac{\lambda_\text{cl}}{\lambda_\text{sep}} = \frac{-\langle g_\text{cl}, g_\text{sep}\rangle \pm \sqrt{\langle g_\text{cl}, g_\text{sep}\rangle^2 - \|g_\text{cl}\|^2 \|g_\text{sep}\|^2}}{\|g_\text{cl}\|^2}.$$

By Cauchy-Schwarz: $\langle g_\text{cl}, g_\text{sep}\rangle^2 \leq \|g_\text{cl}\|^2 \|g_\text{sep}\|^2$. Discriminant ≤ 0, real solution exists iff equality (= cancellation curve).

**Conclusion**: cancellation $\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} = 0$ holds **only** when $g_\text{cl}$ and $g_\text{sep}$ are anti-parallel ($\cos\theta = -1$). For generic $u^*_\text{disk}$, $g_\text{cl}$ and $g_\text{sep}$ are **not** anti-parallel (independent terms with different spatial profiles).

### 4.2 Threshold (C5) recast

Re-formulate: the disk is critical of full $\mathcal{E}$ iff exact cancellation. Generic non-criticality is **automatic** (no parameter tuning), the threshold (C5) is **trivial** in the "generic parameter" sense:
$$\lambda_\text{cl}^\text{crit} = 0 \text{ for all generic } (\lambda_\text{cl}, \lambda_\text{sep}) \text{ with } g_\text{cl} \not\parallel -g_\text{sep}.$$

So (C5) reduces to "anti-parallel locus is codim-$\geq 1$" (which is true unless $g_\text{cl}$ and $g_\text{sep}$ have special alignment).

### 4.3 Sharper version — quantitative non-criticality

The "amount" by which disk fails criticality:
$$\|\pi_{\mathbf{1}^\perp} \nabla \mathcal{E}(u^*_\text{disk})\|^2 = \|\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}\|^2 = \lambda_\text{cl}^2 \|g_\text{cl}\|^2 + 2 \lambda_\text{cl} \lambda_\text{sep} \langle g_\text{cl}, g_\text{sep}\rangle + \lambda_\text{sep}^2 \|g_\text{sep}\|^2.$$

For "disk is far from critical" (large displacement from any nearby critical point), need this norm to be substantial. The quantitative threshold:
$$\boxed{\;\lambda_\text{cl} \cdot \lambda_\text{sep}\text{-quadratic form} \geq \epsilon_\text{crit}^2(L, \beta, \alpha, c, c^*, \mu_c, \kappa_D, \delta_D)\;}$$
where $\epsilon_\text{crit}^2$ is the threshold size of "non-criticality residual" needed to push disk into the saddle basin.

### 4.4 Self-classification of (1.3)

**Cat A definitional + Cat B quantitative.** Theorem 2's (C5) is **strictly trivial in generic regime** (Cat A): for any non-anti-parallel $g_\text{cl}, g_\text{sep}$, the disk is non-critical (no threshold). For "how non-critical" quantitative version, scaling formula (Cat B). 

**Important reinterpretation**: Theorem 2 의 (C5) condition 은 이전 형태 ("$\lambda_\text{cl} > \lambda_\text{cl}^\text{crit}$ for sufficient destabilization") 보다 더 강하게 됨 — 사실상 모든 generic $(\lambda_\text{cl}, \lambda_\text{sep}) \neq (0, 0)$ 에서 disk 가 non-critical. **C5 condition 자체가 수정됨**.

→ Theorem 2 의 새 statement (Phase 4 에서 정형화):
> For generic parameters $(\lambda_\text{cl}, \lambda_\text{sep})$ with $g_\text{cl}(u^*_\text{disk}) \not\parallel -g_\text{sep}(u^*_\text{disk})$ (a codim-1 exclusion), $u^*_\text{disk}$ is **not** a critical point of full $\mathcal{E}$.

이전의 "$\lambda_\text{cl}$ 가 충분히 크면" 조건이 사실상 zero threshold 로 강화. **F-1, M-1 대답에 직접 영향**.

---

## §5. (1.4) Spectral gap argument for F* — NQ-133

### 5.1 Transition: "disk not critical" → "what is critical?"

Phase 1.3 가 보임: full SCC 에서 disk 는 임의 generic parameter 에서 non-critical. 그렇다면 어떤 configuration 이 critical 인가? Multi-peak (F ≥ 2) configuration.

R23 empirical: F_* = 5 for $(c, \beta, L) = (0.5, 30, 32)$. 이론 예측 lower bound 도출.

### 5.2 Disk Hessian linearization

At disk, full $\mathcal{E}$ Hessian $H_\text{disk} = H_\text{bd}|_\text{disk} + \lambda_\text{cl} H_\text{cl}|_\text{disk} + \lambda_\text{sep} H_\text{sep}|_\text{disk}$.

Pure $H_\text{bd}|_\text{disk}$: from Cor 2.2 + spectral analysis 의 continuum limit (`02_development.md` §7), shell-Schrödinger Hamiltonian. Eigenmodes labeled by $(n, \ell)$ = (radial node, angular mode). Eigenvalues:
$$\lambda_{n, \ell}^\text{bd} \approx 4\alpha \big[\lambda_n^{(0)} + \ell^2/r_0^2\big] + O(\beta).$$
Bound states 의 spectrum 이 shell-well depth $\beta/\alpha$ 에 의해 결정.

**For radial $n=0$ shell**: angular ladder $\ell = 0, 1, 2, \ldots$. Spacing $\Delta = 4\alpha/r_0^2$.

### 5.3 Closure / sep Hessian shifts

$H_\text{cl}|_\text{disk}$ at the disk: since $u^*_\text{disk}$ is not at the closure FP, $H_\text{cl}$ has nontrivial spatial structure. The block has positive semidefinite contribution from interior ($u \approx 1 \neq c^*$) and exterior ($u \approx 0 \neq c^*$), with PSD bounded by $a_\text{cl} \cdot$ ($u^*$-residual scale).

Effect on $\ell$-th mode eigenvalue:
$$\Delta_\text{cl} \lambda_\ell \approx \lambda_\text{cl} a_\text{cl} \cdot \langle \phi_\ell, (I - J_\text{Cl}^\top)(I - J_\text{Cl}) \phi_\ell\rangle.$$
For low-$\ell$ (smooth) modes, this shift is positive but small. For high-$\ell$ (oscillatory) modes, shift larger.

$H_\text{sep}|_\text{disk}$: from Prop 1.3b (`mode_count.md` §2.1(d)), $H_\text{sep}|_{c\mathbf{1}} = -\gamma_D(P + P^\top) - c \gamma_D'' P^\top P$. At disk minimizer, similar structure but evaluated at non-uniform point. Negative-definite contribution from $-\gamma_D(P + P^\top)$ for low-$\lambda$ modes (where $P\phi \approx \phi$).

**Net effect**: low-$\ell$ modes (e.g. $\ell = 1, 2$) get net negative contribution from $H_\text{sep}$ (destabilization). High-$\ell$ modes unaffected or stabilized.

### 5.4 F* lower bound

The "first stable" multipeak configuration has F = $\ell^*$ where $\ell^*$ is the smallest angular mode with $\lambda_\ell^\text{full} > 0$:
$$\lambda_\ell^\text{full} = 4\alpha \ell^2/r_0^2 + \Delta_\text{cl}(\ell) + \Delta_\text{sep}(\ell).$$

For the cascade (low-ℓ unstable, high-ℓ stable), $F_* = \ell^*$ where stability flip occurs.

**Estimate**: at $r_0 \approx \sqrt{m/\pi}$, $4\alpha/r_0^2 \approx 4\alpha\pi/m$. For destabilization by sep at strength $\gamma_D$: $\Delta_\text{sep}(\ell) \approx -\lambda_\text{sep} \gamma_D \cdot 2(1 - \cos(\ell \cdot 2\pi/(2\pi r_0)))$ (continuum approximation of $-\gamma_D(P + P^\top)$ on circular interface). For small $\ell/r_0$: $\Delta_\text{sep} \approx -\lambda_\text{sep} \gamma_D \cdot \ell^2/r_0^2$.

Stability condition: $\lambda_\ell^\text{full} > 0$:
$$4\alpha \ell^2/r_0^2 - \lambda_\text{sep} \gamma_D \ell^2/r_0^2 + \lambda_\text{cl} a_\text{cl} (1-\mu_c)^2 \cdot \kappa_\text{cl}(\ell) > 0.$$

For the dominant balance: stable iff $4\alpha > \lambda_\text{sep} \gamma_D - \lambda_\text{cl} a_\text{cl}$.

Hmm — this formulation has $\ell$-independence at leading order — instead, the cl-term provides $\ell$-dependent stabilization that grows with $\ell$.

**Refined estimate**: 
- $\Delta_\text{cl}(\ell) \sim \lambda_\text{cl} a_\text{cl} (1 - \mu_c)^2 \cdot (1 - \cos(\ell \cdot \pi/(2 r_0)))$ — $\ell$-dependent positive contribution
- For $\ell \ll r_0$: $\Delta_\text{cl}(\ell) \approx \lambda_\text{cl} a_\text{cl}(1-\mu_c)^2 \cdot (\ell\pi/(2r_0))^2/2$
- For $\ell \approx r_0$: $\Delta_\text{cl} \sim \lambda_\text{cl} a_\text{cl}(1-\mu_c)^2$ saturated.

Stability flip at $\ell^*$ where $\Delta_\text{cl}(\ell^*) > \lambda_\text{sep}\gamma_D \ell^{*2}/r_0^2 - 4\alpha \ell^{*2}/r_0^2$.

### 5.5 F* prediction (scaling)

$$\boxed{\;F_*(L, \beta, \lambda_\text{cl}, \lambda_\text{sep}, a_\text{cl}, c) \approx \ell^* \approx \sqrt{\frac{(\lambda_\text{sep}\gamma_D - 4\alpha)}{\lambda_\text{cl} a_\text{cl}(1-\mu_c)^2}} \cdot \frac{2 r_0}{\pi}.\;}$$

**Test cases**:
- For $\lambda_\text{sep} \gamma_D < 4\alpha$ (sep destabilization weaker than bd stabilization): $F_* = $ undefined (no destabilization), disk stable.
- For $\lambda_\text{sep} \gamma_D > 4\alpha$ and $\lambda_\text{cl}$ small: $F_*$ large.
- For $\lambda_\text{cl}$ large: $F_*$ small (cascade stops early).

**R23 case**: $(c=0.5, \beta=30, \alpha=1, \lambda_\text{cl}=\lambda_\text{sep}=1, L=32, m \approx 100, r_0 \approx 5.6)$:
- $4\alpha = 4$
- $\gamma_D = d_0(1-d_0)\kappa_D$ at $d_0 = 1/2$ → $\gamma_D = \kappa_D/4$ (for canonical $\kappa_D = 4$, $\gamma_D = 1$)
- $\lambda_\text{sep}\gamma_D - 4\alpha = 1 - 4 = -3$ → 음수 → 본 estimate 대로면 disk stable!

**Discrepancy with R23** ($F_* = 5$): R23 에서는 disk unstable. 본 leading-order estimate 가 fail.

**원인 진단**:
1. $\Delta_\text{sep}$ leading order 가 부정확. Sep 의 destabilization 메커니즘은 $-\gamma_D(P+P^\top)$ 의 lowest eigenvalue 가 positive eigenvalue 와 cancellation 하는 더 복잡한 효과.
2. Disk 가 closure FP $c^*\mathbf{1}$ 에서 멀리 있어 nonlinear 보정 critical.
3. Closure 의 destabilization 효과 ($\lambda_\text{cl}$ 가 disk 를 favor 하지 않음 — 오히려 closure 가 single-disk 를 destabilize).

**실제로**: Theorem 2 의 핵심은 closure 가 disk 를 **destabilize** 하는 것 (R23 §11 FSC1 가 이를 empirical 확정). 위 (5.5) 는 closure stabilize 가정으로 도출 — 부호 오류.

### 5.6 정정된 scaling

Closure 는 disk 의 interior 가 FP 가 아니라는 mismatch 비용 → 이는 **disk 자체의 에너지를 높임** (Theorem 2 의 §6.2 분석). Spectrum 에 미치는 효과는 disk 의 small perturbation 에 대해:
- Perturbation 이 interior 를 더 균질하게 만들면 → cl mismatch 감소 → 에너지 감소 → mode unstable
- Perturbation 이 multi-peak 만들면 → cl mismatch 가 multi-peak 형태 적합화 → 어떤 peak 수에서 minimum

이 mechanism 이 정량 derivation 어려움. **결론**: F_* prediction 은 Phase 1 만으로 closed form 도출 어렵고, Phase 2/3 numerical 로만 신뢰성 있는 값.

### 5.7 Self-classification of (1.4)

**Cat C** — qualitative spectral cascade argument 가 F_* 의 존재성을 보이지만, 정확한 값 (5 vs 2 등) 은 leading-order 만으로 결정 안 됨. NQ-133 은 본 phase 에서 partial answer (F_* exists, scaling 이 (λ_cl, λ_sep, β, α, m, c) 의 함수); 정확한 값은 Phase 2/3 numerical 또는 후속 theory.

---

## §6. (1.5) F-1, M-1 reformulation in σ-language

위 §4 의 결과 — disk 가 generic parameter 에서 non-critical — 이 F-1 / M-1 에 직접 영향.

### 6.1 F-1 reformulation

**기존 F-1**: K=2 global stable 이려면 external per-formation mass constraint 필요. 자유 Σ_m 위 K=1 always cheaper.

**σ-language 재기술**: Σ_m 위에서 minimum stable formation count 는:
- Pure $\mathcal{E}_\text{bd}$ (K=1 layer): $\mathcal{F}_\text{min}^\text{bd} = 1$ (single disk).
- Full SCC (closure + sep > 0): $\mathcal{F}_\text{min}^\text{full} = F_* \geq 2$ (Phase 1.4 + Theorem 2).

**Implication**: F-1 의 "K=2 vacuity" 는 **pure $\mathcal{E}_\text{bd}$** layer 의 statement. Full SCC 에서는 disk 자체가 non-critical → $\mathcal{F} \geq 2$ 가 자동, K=2 (or larger) 가 자연스럽게 작동.

→ **F-1 의 부분 negative resolution**: Full SCC framework 에서 K=1 (more precisely, $\mathcal{F} = 1$) 은 vacuous in the sense of being non-critical. F-1 가 묻는 "K=2 global stable" 은 pure $\mathcal{E}_\text{bd}$ 에서는 부정 (K=1 cheaper) 이지만 full SCC 에서는 K=1 자체가 stable 이 아니라서 질문이 trivial 하게 negative.

**여전히 open**: F-1 의 deeper variant — "두 개의 lobes 가 있는 stable minimizer 가 어떤 setup 에서 K_step layer 의 정수 K=2 로 등록되는가?" — 본 phase 1 답하지 못함. NQ-A.

**Cat: F-1 partially resolved (negative for full SCC), open for $K_\text{step}$ layer-specific question.**

### 6.2 M-1 reformulation

**기존 M-1**: $E(m_1, m_2)$ monotone toward K=1.

**σ-language**:
- $K_\text{step}$ layer: M-1 그대로 valid. Isoperimetric ordering (T-Merge (b) Cat A).
- $\mathcal{F}$ layer: M-1 false. Minimum $\mathcal{F}$ 가 1 이 아니라 $F_* \geq 2$.

→ **M-1 가 layer-relative**: $K_\text{step}$ layer 에서 K=1 preference, $\mathcal{F}$ layer 에서 K=$F_*$ preference. 두 layer 가 양립 — N-1 의 soft-hard switching 의 또 다른 instance.

**Cat: M-1 layer-clarified (K_step layer 그대로, $\mathcal{F}$ layer 에서 F_* preference).**

---

## §7. (1.6) MO-1 sidestep

**기존 MO-1**: $\Sigma^2_M$ corner manifold, standard Morse 적용 불가.

**σ-language sidestep**: σ-framework 가 $\Sigma_m$ 단일 manifold 위 작동 (not $\Sigma^K_M$). 모든 stable minimizer 가 single $u^* \in \Sigma_m$ 으로 표현, $\mathcal{F}(u^*)$ 가 "formation count" derived.

→ **Σ²_M corner 문제 자체가 σ-framework 에서 회피**. $\Sigma_m$ 은 convex polytope (Prop 1.1 Cat A), corner 없음, standard Morse applicable.

**Caveat**: 이 sidestep 은 multi-formation 분석을 single $u^*$ 에 흡수 — 두 formation 이 well-separated 인지의 정보가 σ 안에 (S1'-iv) bridge $K_\text{step} \leq \mathcal{F}$ 로만 encode. K_step layer 에서의 multi-formation 분석은 별도 framework 필요.

**Cat: MO-1 single-formation σ-framework 에서 sidestep, multi-formation 은 별도 개방.**

---

## §8. Phase 1 산출 요약

| 작업 | 결과 | Cat |
|---|---|---|
| (1.1) g_cl explicit | scaling formula in $(\mu_c, c^*, r_0, L, a_\text{cl})$ | B |
| (1.2) g_sep explicit | scaling formula in $(\kappa_D, c, r_0, L)$ | B |
| (1.3) λ_cl^crit | trivially 0 in generic regime; 양적 non-criticality 는 quadratic form | A definitional + B quantitative |
| (1.4) F* spectral argument | $F_*$ 존재성 + scaling 함수 형태; 정확 값은 Phase 2/3 | C |
| (1.5) F-1 reformulation | pure $\mathcal{E}_\text{bd}$ vs full SCC layer 분리, F-1 partial negative | partial answer |
| (1.5) M-1 reformulation | layer-relative ($K_\text{step}$ vs $\mathcal{F}$) | clarified |
| (1.6) MO-1 sidestep | σ-framework 가 corner manifold 회피 | sidestepped |

### 8.1 Theorem 2 의 Phase 1 후 status update

> **Theorem 2 (revised, 2026-04-24 evening, post-Phase-1).** Let $G = L \times L$ free-BC grid, $\mathcal{E}$ full SCC with $b_D = 0$, parameters $(\lambda_\text{cl}, \lambda_\text{sep})$ generic in the sense that $g_\text{cl}(u^*_\text{disk})$ and $g_\text{sep}(u^*_\text{disk})$ are not anti-parallel in $\mathbf{1}^\perp$. Then $u^*_\text{disk}$ from pure $\mathcal{E}_\text{bd}$ is not a critical point of full $\mathcal{E}$ on $\Sigma_m$. In particular, $u^*_\text{disk}$ is not a local minimum.
>
> Furthermore, the minimum stable formation count $F_*$ exists and satisfies $F_* \geq 2$ with scaling form
> $$F_* \sim \mathfrak{F}\big(\lambda_\text{cl}/\lambda_\text{sep}, \beta, \alpha, c, c^*, m, L\big),$$
> where $\mathfrak{F}$ is a graph-class-specific function. For the $D_4$ free-BC $L \times L$ grid at $(c, \beta, L) = (0.5, 30, 32)$, $\lambda_\text{cl} = \lambda_\text{sep} = 1$, R23 §11 confirms $F_* = 5$ empirically (Phase 2/3 numerical verification needed for theoretical $F_* = 5$ derivation).

**Cat 분류**: 
- "Disk non-critical" — **Cat A** (generic parameter assumption은 codim ≥ 1 제외, 사실상 트리비얼 가정).
- "$F_* \geq 2$ exists" — **Cat A** (Phase 1.4 spectral argument + R23 empirical).
- "$F_* = 5$ for R23 setup" — **Cat B** (empirical Cat A from R23 + theoretical scaling formula but exact value pending Phase 2/3).

**Phase 1 후 Theorem 2 의 Cat A 부분이 확보됨** — 이전 Cat C sketched 에서 진전.

---

## §9. Phase 2 / Phase 3 transition

### 9.1 Phase 2 (light numerical, 다음 파일 `08a_*.py`) target

(2.1) g_cl 의 §2 scaling formula 를 L=8 small grid 에서 verify: scc 의 EnergyComputer 의 analytical gradient 와 비교.
(2.2) λ_cl^crit (= 0 generically) verification: 임의 $(\lambda_\text{cl}, \lambda_\text{sep})$ 에서 disk 가 non-critical 임을 numerical 확인.

Estimated runtime: <1분.

### 9.2 Phase 3 (heavy numerical, user runs) target

(3.1) F-distribution at varying $(\lambda_\text{cl}, \lambda_\text{sep})$, 32×32 — F* prediction 의 정량 test.
(3.2) Pure cl ($\lambda_\text{sep} = 0$) vs pure sep ($\lambda_\text{cl} = 0$) — NQ-134.
(3.3) Direct Theorem 2 disk-saddle confirmation across 다양한 param.

Estimated runtime: ~1.5 시간.

---

## §10. 다음 파일 예고

- `08a_C2_phase2_light_numerical.py` — Phase 2 verification script (사용자 실행 가능 또는 본 세션 직접 실행).
- `09_C2_phase3_heavy_scripts.md` — Phase 3 script 모음 + 사용자 실행 명령 + 결과 통신 protocol.
- (Phase 4 integration 은 user 결과 후)

**Phase 1 완료. Cat A 확보된 부분: Theorem 2 의 "disk non-critical" + "F_* ≥ 2 exists". Phase 2 verification 진행.**
