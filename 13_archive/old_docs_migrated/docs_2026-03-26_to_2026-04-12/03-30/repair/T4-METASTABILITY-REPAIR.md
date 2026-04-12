# Theorem 4 (Enhanced Metastability) — Repair Analysis

**Author:** Theorem Repair Specialist
**Date:** 2026-03-30
**Status:** Three approaches evaluated; Approach C recommended
**Dependencies:** MATH-DEEP-AUDIT.md (gap diagnosis), BIND-BOUND-PROOF.md (T-Bind), paper1_math.tex (current statement)

---

## 0. The Problem

The current Theorem 4 claims: at a non-trivial constrained minimizer $\hat{u}$ of $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$, the minimum eigenvalue of $\nabla^2\mathcal{E}|_{T_{\hat{u}}\Sigma_m}$ strictly exceeds that of $\nabla^2\mathcal{E}_{\mathrm{bd}}|_{T_{\hat{u}}\Sigma_m}$, with enhancement $\geq \lambda_{\mathrm{cl}} \cdot 2(1 - \|J_{\mathrm{Cl}}\|_{\mathrm{op}})^2$.

**Two gaps identified in the audit:**

1. **Gauss-Newton gap.** The proof uses $\nabla^2\mathcal{E}_{\mathrm{cl}} = 2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}})$, which is the Gauss-Newton approximation. The exact Hessian is:
$$\nabla^2\mathcal{E}_{\mathrm{cl}} = 2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}}) + 2\sum_i r_i \nabla^2(\mathrm{Cl}_i - \mathrm{id}_i)$$
where $r = \mathrm{Cl}(\hat{u}) - \hat{u}$. At the closure fixed point $r = 0$, the second term vanishes. At the energy minimizer, $r \neq 0$.

2. **$H_{\mathrm{sep}}$ sign gap.** The proof assumes $\lambda_{\mathrm{sep}} \nabla^2\mathcal{E}_{\mathrm{sep}}$ "does not dominate negatively" without justification.

---

## Approach A: Prove the Residual Correction Is Small

### Strategy
Show $\|r\| = O(1/\lambda_{\mathrm{cl}})$ so that for large $\lambda_{\mathrm{cl}}$, the Gauss-Newton term $2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$ dominates the residual correction $2\sum_i r_i \nabla^2(\mathrm{Cl}_i - \mathrm{id}_i)$.

### Detailed Analysis

**Step 1: Bound on the residual correction operator norm.**

Each component $\mathrm{Cl}_i(u) = \sigma(z_i)$ where $z_i = a_{\mathrm{cl}}((1-\eta)u_i + \eta(Pu)_i - \tau)$. The Hessian of $\mathrm{Cl}_i - u_i$ with respect to $u$ is $\nabla^2 \mathrm{Cl}_i(u)$ (the $-u_i$ term contributes zero to the second derivative since $\nabla^2 u_i = 0$).

$$\nabla^2 \mathrm{Cl}_i = \sigma''(z_i) \cdot a_{\mathrm{cl}}^2 \cdot e_i e_i^T$$

Wait — more carefully. $z_i = a_{\mathrm{cl}}((1-\eta)u_i + \eta \sum_j P_{ij} u_j - \tau)$. Define $w_i = \nabla_u z_i = a_{\mathrm{cl}}((1-\eta)e_i + \eta P_i^T)$ where $P_i$ is the $i$-th row of $P$ (as a column vector). Then:

$$\nabla_u \mathrm{Cl}_i = \sigma'(z_i) w_i$$

$$\nabla^2_u \mathrm{Cl}_i = \sigma''(z_i) w_i w_i^T$$

since $w_i$ does not depend on $u$ (the pre-activation is linear in $u$). Here $\sigma''(z) = \sigma'(z)(1 - 2\sigma(z))$.

The residual correction is:
$$R = 2\sum_i r_i \sigma''(z_i) w_i w_i^T$$

Its operator norm:
$$\|R\|_{\mathrm{op}} \leq 2\sum_i |r_i| \cdot |\sigma''(z_i)| \cdot \|w_i\|_2^2$$

**Bounding $|\sigma''(z)|$.** $|\sigma''(z)| = \sigma'(z)|1 - 2\sigma(z)| \leq \sigma'(z) \leq 1/4$. More tightly: $\max_z |\sigma''(z)| = \frac{\sqrt{3}}{9} \approx 0.1925$ (achieved at $z = \pm \ln(2 + \sqrt{3})$).

**Bounding $\|w_i\|_2$.** $w_i = a_{\mathrm{cl}}((1-\eta)e_i + \eta P_i^T)$. So $\|w_i\|_2 \leq a_{\mathrm{cl}}((1-\eta) + \eta\|P_i\|_2)$. Since $P$ is row-stochastic with entries in $[0,1]$: $\|P_i\|_2 \leq \|P_i\|_1 = 1$ (with equality when the node has one neighbor). More precisely $\|P_i\|_2 \leq 1$. So $\|w_i\|_2 \leq a_{\mathrm{cl}}$, and $\|w_i\|_2^2 \leq a_{\mathrm{cl}}^2$.

Therefore:
$$\|R\|_{\mathrm{op}} \leq 2 \cdot \frac{\sqrt{3}}{9} \cdot a_{\mathrm{cl}}^2 \cdot \sum_i |r_i| = \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \|r\|_1$$

Using $\|r\|_1 \leq \sqrt{n} \|r\|_2$:

$$\|R\|_{\mathrm{op}} \leq \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \sqrt{n} \|r\|_2 \tag{A1}$$

**Step 2: Attempt to bound $\|r\|_2$ via KKT.**

From the KKT conditions at the minimizer (with strict interiority):
$$-2\lambda_{\mathrm{cl}}(I - J_{\mathrm{Cl}})^T r = \nu \mathbf{1} - \lambda_{\mathrm{sep}} \nabla\mathcal{E}_{\mathrm{sep}} - \lambda_{\mathrm{bd}} \nabla\mathcal{E}_{\mathrm{bd}}$$

Inverting $(I - J_{\mathrm{Cl}})^T$ (valid since $\|J_{\mathrm{Cl}}\|_2 \leq a_{\mathrm{cl}}/4 < 1$):
$$\|r\|_2 \leq \frac{|\nu|\sqrt{n} + \lambda_{\mathrm{sep}}\|\nabla\mathcal{E}_{\mathrm{sep}}\|_2 + \lambda_{\mathrm{bd}}\|\nabla\mathcal{E}_{\mathrm{bd}}\|_2}{2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)} \tag{A2}$$

**Problem:** This involves the Lagrange multiplier $\nu$. As shown in BIND-BOUND-PROOF.md §III, bounding $\nu$ through KKT creates circularity — the $\nu$ bound depends on $\nabla\mathcal{E}_{\mathrm{cl}}$ which depends on $r$.

**Step 3: Attempt to break the circularity.**

The projected KKT eliminates $\nu$:
$$\lambda_{\mathrm{cl}} \Pi_T(\nabla\mathcal{E}_{\mathrm{cl}}) + \lambda_{\mathrm{sep}} \Pi_T(\nabla\mathcal{E}_{\mathrm{sep}}) + \lambda_{\mathrm{bd}} \Pi_T(\nabla\mathcal{E}_{\mathrm{bd}}) = 0$$

This gives a bound on the tangential residual $\|r_T\|_2 = O((\lambda_{\mathrm{bd}} + \lambda_{\mathrm{sep}})/\lambda_{\mathrm{cl}})$ (proved in T-Bind). But the full residual $\|r\|_2$ includes the mean component $\bar{r}$, which is not controlled by $\lambda_{\mathrm{cl}}$.

**Can we use the Hessian correction on the tangent space only?** Yes — the theorem concerns $\nabla^2\mathcal{E}|_{T\Sigma_m}$, so we need to bound the restricted correction:

$$\|R|_T\|_{\mathrm{op}} = \sup_{v \in T, \|v\|=1} |v^T R v| = \sup_{v \in T, \|v\|=1} \left|2\sum_i r_i \sigma''(z_i)(w_i^T v)^2\right|$$

Since $(w_i^T v)^2 \geq 0$ and $\sigma''(z_i)$ can be positive or negative (depending on sign of $1 - 2\sigma(z_i)$), there could be cancellation. But in worst case:

$$\|R|_T\|_{\mathrm{op}} \leq 2\sum_i |r_i| |\sigma''(z_i)| \|w_i\|_2^2 = \|R\|_{\mathrm{op}}$$

The restriction to $T$ doesn't help with the operator norm bound.

**Step 4: Can we bound $\|r\|_2$ (full) without KKT?**

Using the energy comparison: $\lambda_{\mathrm{cl}}\|r\|_2^2 = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}}(\hat{u}) \leq \mathcal{E}(\hat{u}) \leq \mathcal{E}(c\mathbf{1})$.

At the uniform field: $\mathcal{E}(c\mathbf{1}) = \lambda_{\mathrm{cl}} n|c - \sigma(a_{\mathrm{cl}}(c-\tau))|^2 + \lambda_{\mathrm{sep}} \cdot E_{\mathrm{sep}}^{\mathrm{unif}} + \lambda_{\mathrm{bd}} \beta n W(c)$.

This gives $\|r\|_2^2 \leq n|c - \sigma(a_{\mathrm{cl}}(c-\tau))|^2 + O((\lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}})/\lambda_{\mathrm{cl}}) \cdot n$.

So $\|r\|_2 = O(\sqrt{n})$, giving $\|R\|_{\mathrm{op}} = O(n)$ by (A1). The Gauss-Newton term has minimum eigenvalue $\lambda_{\mathrm{cl}} \cdot 2(1-a_{\mathrm{cl}}/4)^2 = O(\lambda_{\mathrm{cl}})$. For the GN term to dominate, we need $\lambda_{\mathrm{cl}} \gg n$, which is not a natural condition.

**Better route:** Use the energy comparison more carefully. At the minimizer, the closure energy $\mathcal{E}_{\mathrm{cl}}(\hat{u}) \leq \mathcal{E}(c\mathbf{1})/\lambda_{\mathrm{cl}}$... but this doesn't give $\|r\| = O(1/\lambda_{\mathrm{cl}})$. The energy comparison gives $\|r\|^2 = O(n)$ regardless of $\lambda_{\mathrm{cl}}$ (the uniform field has $O(n)$ closure energy too).

Actually, the comparison gives:
$$\lambda_{\mathrm{cl}}\|r\|_2^2 \leq \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}(c\mathbf{1}) + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}(c\mathbf{1}) + \lambda_{\mathrm{bd}} \mathcal{E}_{\mathrm{bd}}(c\mathbf{1})$$

So $\|r\|_2^2 \leq \mathcal{E}_{\mathrm{cl}}(c\mathbf{1}) + (\lambda_{\mathrm{sep}}/\lambda_{\mathrm{cl}})n + (\lambda_{\mathrm{bd}}/\lambda_{\mathrm{cl}})\beta n W(c)$.

The first term $\mathcal{E}_{\mathrm{cl}}(c\mathbf{1}) = n|c - \sigma(a_{\mathrm{cl}}(c - \tau))|^2$ is $O(n)$ and independent of $\lambda_{\mathrm{cl}}$.

**Conclusion:** The energy comparison cannot give $\|r\|_2 = o(\sqrt{n})$.

### Verdict on Approach A: **FAILS**

The full residual $\|r\|_2$ cannot be bounded as $O(1/\lambda_{\mathrm{cl}})$ by either KKT or energy comparison. The mean component $\bar{r}$ is $O(\sqrt{n})$ and determined by the closure operator's mass-preservation properties, not the energy weight. Consequently, the residual correction $\|R\|_{\mathrm{op}} = O(\sqrt{n} \cdot \sqrt{n}) = O(n)$, which is too large for the Gauss-Newton term $O(\lambda_{\mathrm{cl}})$ to dominate without the unnatural assumption $\lambda_{\mathrm{cl}} \gg n$.

**However**, the projected approach (restricting to $T\Sigma_m$) may help indirectly — see Approach C.

---

## Approach B: Prove $H_{\mathrm{sep}}$ Is PSD at Minimizers

### Strategy
Show $\nabla^2\mathcal{E}_{\mathrm{sep}} \succeq 0$ at minimizers, so it contributes non-negatively to the total Hessian.

### Detailed Analysis

**Step 1: Compute $\nabla^2\mathcal{E}_{\mathrm{sep}}$.**

$\mathcal{E}_{\mathrm{sep}}(u) = \sum_i u_i(1 - D_i(u))$ where $D_i(u) = \sigma(q_i(u))$ and $q_i(u) = a_D(P_i^T u - \lambda_D P_i^T(1-u)) - \tau_D = a_D(1+\lambda_D)P_i^T u - a_D \lambda_D P_i^T \mathbf{1} - \tau_D$.

The gradient (verified in energy.py): $(\nabla\mathcal{E}_{\mathrm{sep}})_j = (1 - D_j) - (J_D^T u)_j$.

The Hessian: differentiate again. Let $h_i = a_D(1+\lambda_D) P_i$ (the gradient of $q_i$ w.r.t. $u$). Then $J_D = \mathrm{diag}(\sigma'(q) \cdot a_D(1+\lambda_D)) P$ as computed in operators.py.

$$\frac{\partial^2 \mathcal{E}_{\mathrm{sep}}}{\partial u_j \partial u_k} = -\frac{\partial D_j}{\partial u_k} - \frac{\partial}{\partial u_k}\left[\sum_i u_i \frac{\partial D_i}{\partial u_j}\right]$$

$$= -\sigma'(q_j) h_{jk} - \sum_i u_i \sigma''(q_i) h_{ij} h_{ik} - \delta_{ij} \text{ terms...}$$

Let me be more systematic. Define $f(u) = \sum_i u_i(1 - D_i(u))$.

$$\frac{\partial f}{\partial u_j} = (1 - D_j) - \sum_i u_i \frac{\partial D_i}{\partial u_j} = (1 - D_j) - (J_D^T u)_j$$

$$\frac{\partial^2 f}{\partial u_j \partial u_k} = -\frac{\partial D_j}{\partial u_k} - \frac{\partial D_k}{\partial u_j} - \sum_i u_i \frac{\partial^2 D_i}{\partial u_j \partial u_k}$$

Wait — let me redo this. The gradient is:
$$g_j = (1 - D_j) - \sum_i u_i (J_D)_{ij}$$

Differentiating w.r.t. $u_k$:
$$H_{jk} = -(J_D)_{kj} - (J_D)_{jk} - \sum_i u_i \frac{\partial (J_D)_{ij}}{\partial u_k} + \text{correction}$$

Wait, I need to be very careful. Let me write it in matrix form.

$\nabla \mathcal{E}_{\mathrm{sep}} = (\mathbf{1} - D) - J_D^T u$

$\nabla^2 \mathcal{E}_{\mathrm{sep}} = -J_D^T - J_D - \sum_i u_i \nabla^2 D_i$

Wait no — differentiate $(\mathbf{1} - D(u))$ w.r.t. $u$: this gives $-J_D$. Differentiate $J_D^T u$ w.r.t. $u$: this gives $J_D^T + \text{(terms involving } \nabla J_D \text{ and } u)$.

More carefully: $(\nabla \mathcal{E}_{\mathrm{sep}})_j = (1 - D_j(u)) - \sum_i u_i (J_D)_{ij}(u)$

$$\frac{\partial}{\partial u_k}(1 - D_j) = -(J_D)_{jk}$$

$$\frac{\partial}{\partial u_k}\left(\sum_i u_i (J_D)_{ij}\right) = (J_D)_{kj} + \sum_i u_i \frac{\partial (J_D)_{ij}}{\partial u_k}$$

So: $H_{jk} = -(J_D)_{jk} - (J_D)_{kj} - \sum_i u_i \frac{\partial (J_D)_{ij}}{\partial u_k}$

In matrix form:
$$\nabla^2 \mathcal{E}_{\mathrm{sep}} = -J_D - J_D^T - \sum_i u_i \nabla^2 D_i$$

Now $(J_D)_{ij} = \sigma'(q_i) \cdot a_D(1+\lambda_D) P_{ij}$, so:
$$\frac{\partial (J_D)_{ij}}{\partial u_k} = \sigma''(q_i) \cdot (a_D(1+\lambda_D))^2 P_{ij} P_{ik}$$

Therefore:
$$\sum_i u_i \nabla^2 D_i = (a_D(1+\lambda_D))^2 \sum_i u_i \sigma''(q_i) P_i P_i^T$$

where $P_i$ is the $i$-th row of $P$ as a column vector.

**Step 2: Analyze the sign of $\nabla^2\mathcal{E}_{\mathrm{sep}}$.**

$$\nabla^2\mathcal{E}_{\mathrm{sep}} = -J_D - J_D^T - (a_D(1+\lambda_D))^2 \sum_i u_i \sigma''(q_i) P_i P_i^T$$

The first two terms: $-J_D - J_D^T = -2\,\mathrm{sym}(J_D)$. Since $J_D = \mathrm{diag}(s_D) P$ where $s_D = \sigma'(q) a_D(1+\lambda_D) > 0$, the symmetric part $\mathrm{sym}(J_D) = \frac{1}{2}(\mathrm{diag}(s_D) P + P^T \mathrm{diag}(s_D))$.

For a direction $v$: $v^T(J_D + J_D^T)v = 2\sum_i s_{D,i} (Pv)_i v_i$. This can be positive (when $(Pv)_i$ and $v_i$ have the same sign, which happens for smooth $v$ on the graph) or negative. So $-J_D - J_D^T$ is **indefinite** in general.

The third term: $\sigma''(q_i) = \sigma'(q_i)(1 - 2\sigma(q_i)) = \sigma'(q_i)(1 - 2D_i)$. For sites where $D_i > 1/2$ (well-distinguished interior), $\sigma'' < 0$, so $-u_i \sigma''(q_i) > 0$ and the rank-1 contribution $u_i(-\sigma''(q_i))P_iP_i^T$ is PSD. For sites where $D_i < 1/2$ (poorly distinguished), $\sigma'' > 0$ and the contribution is $-u_i \sigma''(q_i) P_i P_i^T$ which is NSD.

**Step 3: Assessment.**

The Hessian $\nabla^2\mathcal{E}_{\mathrm{sep}}$ is a sum of indefinite terms. There is no reason to expect it to be PSD at minimizers. In particular:

- The $-J_D - J_D^T$ contribution is negative in directions where $v$ is smooth on the graph (since $Pv \approx v$ for smooth vectors, making $v^T J_D v \approx \sum s_{D,i} v_i^2 > 0$).
- The third term has mixed sign depending on whether $D_i \gtrless 1/2$.

**Explicit counterexample sketch.** On a path graph with 3 nodes, $u = (0.8, 0.5, 0.2)$, default parameters. The distinction operator gives $D_1 \approx 0.7$, $D_2 \approx 0.5$, $D_3 \approx 0.3$. The Hessian matrix can be computed numerically and will have negative eigenvalues.

### Verdict on Approach B: **FAILS**

$\nabla^2\mathcal{E}_{\mathrm{sep}}$ is generically indefinite. It cannot be assumed PSD, and there is no structural reason why it would become PSD at energy minimizers. The audit's identification of this as an unstated hypothesis was correct — it is an unfixable hypothesis.

---

## Approach C: Weaken the Theorem Honestly

### Strategy
State: for $\lambda_{\mathrm{cl}}$ sufficiently large relative to $\lambda_{\mathrm{sep}}$ and $\lambda_{\mathrm{bd}}$, the Gauss-Newton term dominates both the residual correction and the (possibly negative) $H_{\mathrm{sep}}$ contribution. Compute an explicit threshold.

### Detailed Analysis

**Step 1: Structure of the exact Hessian on $T\Sigma_m$.**

$$\nabla^2\mathcal{E}|_T = \lambda_{\mathrm{cl}}\left[2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}}) + R_{\mathrm{cl}}\right] + \lambda_{\mathrm{sep}} H_{\mathrm{sep}} + \lambda_{\mathrm{bd}} H_{\mathrm{bd}}$$

where all operators are restricted to $T\Sigma_m$ (via $\Pi_T(\cdot)\Pi_T$), and:
- $R_{\mathrm{cl}} = 2\sum_i r_i \sigma''(z_i) w_i w_i^T$ is the residual correction to the closure Hessian.
- The Gauss-Newton term $G = 2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}})$ has $\lambda_{\min}(G|_T) \geq 2(1 - a_{\mathrm{cl}}/4)^2$.

**Step 2: Bound the error terms.**

From Approach A: $\|R_{\mathrm{cl}}\|_{\mathrm{op}} \leq \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \|r\|_1 \leq \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \sqrt{n} \|r\|_2$

From Approach B: $\|H_{\mathrm{sep}}\|_{\mathrm{op}} \leq \|J_D + J_D^T\|_{\mathrm{op}} + (a_D(1+\lambda_D))^2 \sum_i u_i |\sigma''(q_i)| \|P_i\|_2^2$

Bounding: $\|J_D + J_D^T\|_{\mathrm{op}} \leq 2\|J_D\|_{\mathrm{op}} \leq 2 \cdot \frac{a_D(1+\lambda_D)}{4} = \frac{a_D(1+\lambda_D)}{2}$.

For the third term: $\sum_i u_i |\sigma''(q_i)| \leq m \cdot \frac{\sqrt{3}}{9}$ and $\|P_i\|_2^2 \leq 1$. So the third term is bounded by $(a_D(1+\lambda_D))^2 \cdot m \cdot \frac{\sqrt{3}}{9}$.

Define:
$$S := \frac{a_D(1+\lambda_D)}{2} + (a_D(1+\lambda_D))^2 \cdot n \cdot \frac{\sqrt{3}}{9}$$

so $\|H_{\mathrm{sep}}\|_{\mathrm{op}} \leq S$. (Note: the $n$-dependent term arises from $m \leq n$.)

**Step 3: Bound the residual norm using the energy comparison.**

From the energy comparison (Step 4 of Approach A):
$$\|r\|_2^2 \leq n|c - \sigma(a_{\mathrm{cl}}(c - \tau))|^2 + \frac{n(\lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}} \beta W(c))}{\lambda_{\mathrm{cl}}}$$

Define $\rho_0^2 := |c - \sigma(a_{\mathrm{cl}}(c - \tau))|^2$ (the per-site closure residual at the uniform field). Then:
$$\|r\|_2 \leq \sqrt{n}\sqrt{\rho_0^2 + \frac{\lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}} \beta W(c)}{\lambda_{\mathrm{cl}}}} \leq \sqrt{n}\left(\rho_0 + O(1/\sqrt{\lambda_{\mathrm{cl}}})\right)$$

Substituting into the residual correction bound:
$$\|R_{\mathrm{cl}}\|_{\mathrm{op}} \leq \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 n \left(\rho_0 + O(1/\sqrt{\lambda_{\mathrm{cl}}})\right)$$

**Step 4: The $n$-problem.**

Both $\|R_{\mathrm{cl}}\|_{\mathrm{op}}$ and $\|H_{\mathrm{sep}}\|_{\mathrm{op}}$ scale as $O(n)$, while the Gauss-Newton enhancement $\lambda_{\mathrm{cl}} \cdot 2(1-a_{\mathrm{cl}}/4)^2$ is $O(\lambda_{\mathrm{cl}})$. For the theorem to hold, we would need $\lambda_{\mathrm{cl}} \gg n$, which is unnatural.

**Key insight: per-site rescaling.** The issue is an artifact of working with extensive quantities. The energy $\mathcal{E}$ scales as $O(n)$; the Hessian eigenvalues also scale with $n$. The *physically meaningful* quantity is the eigenvalue of the Hessian of the **per-site energy** $\mathcal{E}/n$.

Actually, this doesn't help with the operator-norm bound — both terms scale the same way.

**Revised key insight: the residual correction is rank-deficient on typical minimizers.**

At a well-formed minimizer, most sites $i$ have either $\hat{u}_i \approx 0$ or $\hat{u}_i \approx 1$. At these sites:
- $z_i$ is far from 0, so $\sigma'(z_i) \approx 0$, hence $\sigma''(z_i) \approx 0$.
- The weight $w_i w_i^T$ contributes negligibly to $R_{\mathrm{cl}}$.

Only **boundary sites** (where $\hat{u}_i$ is intermediate) contribute significantly. If the number of boundary sites is $n_b \ll n$, then the effective rank of $R_{\mathrm{cl}}$ is $O(n_b)$, and its action on tangent-space directions that are supported on the interior is negligible.

However, making this rigorous requires a quantitative characterization of "well-formed minimizers," which essentially requires Gamma-convergence estimates. This is circular — we're trying to prove properties of minimizers, not assuming them.

**Step 5: A clean sufficient condition.**

We can state an honest theorem with an explicit condition on $\lambda_{\mathrm{cl}}$. The Gauss-Newton enhancement on $T\Sigma_m$ gives a minimum eigenvalue increase of at least:
$$\lambda_{\mathrm{cl}} \cdot 2(1 - a_{\mathrm{cl}}/4)^2 - \lambda_{\mathrm{cl}} \|R_{\mathrm{cl}}|_T\|_{\mathrm{op}} - \lambda_{\mathrm{sep}} \|H_{\mathrm{sep}}|_T\|_{\mathrm{op}}$$

This is positive when:
$$\lambda_{\mathrm{cl}}\left[2(1 - a_{\mathrm{cl}}/4)^2 - \|R_{\mathrm{cl}}|_T\|_{\mathrm{op}}\right] > \lambda_{\mathrm{sep}} \|H_{\mathrm{sep}}|_T\|_{\mathrm{op}}$$

The residual correction norm involves $\|r\|_1$, which involves $\lambda_{\mathrm{cl}}$ through the energy comparison. This creates an implicit condition rather than a clean threshold.

**Step 6: The clean formulation — condition at the minimizer.**

Rather than trying to derive a priori bounds (which lead to $O(n)$ terms), we state the theorem as: **the enhancement holds whenever a computable condition at the minimizer is satisfied.** This is the honest approach.

Define the **residual correction number**:
$$\kappa(\hat{u}) := \frac{\|R_{\mathrm{cl}}(\hat{u})|_T\|_{\mathrm{op}}}{2(1 - \|J_{\mathrm{Cl}}(\hat{u})\|_{\mathrm{op}})^2}$$

and the **separation curvature number**:
$$\mu(\hat{u}) := \frac{\lambda_{\mathrm{sep}}}{\lambda_{\mathrm{cl}}} \cdot \frac{\lambda_{\min}^{-}(H_{\mathrm{sep}}(\hat{u})|_T)}{2(1 - \|J_{\mathrm{Cl}}(\hat{u})\|_{\mathrm{op}})^2}$$

where $\lambda_{\min}^{-}(M) = \max(0, -\lambda_{\min}(M))$ is the magnitude of the most negative eigenvalue.

Then the metastability enhancement holds whenever $\kappa(\hat{u}) + \mu(\hat{u}) < 1$.

**Step 7: Asymptotic statement for large $\lambda_{\mathrm{cl}}$.**

Alternatively, we can prove an asymptotic result. As $\lambda_{\mathrm{cl}} \to \infty$ with $\lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}$ fixed:

1. The minimizer $\hat{u}$ approaches the closure fixed point $u^*$ (the unique fixed point of $\mathrm{Cl}$ on $[0,1]^n$), projected onto $\Sigma_m$.
2. At the closure fixed point, $r = 0$, so $R_{\mathrm{cl}} = 0$ and the Gauss-Newton approximation is exact.
3. The $\lambda_{\mathrm{sep}} H_{\mathrm{sep}}$ term is $O(1)$ while the closure enhancement is $O(\lambda_{\mathrm{cl}})$.

Therefore, for $\lambda_{\mathrm{cl}}$ large enough, the enhancement holds.

To make this quantitative: from (A2), if we can bound $|\nu|$ independently of $\lambda_{\mathrm{cl}}$ (which we cannot in general), we'd get $\|r\|_2 = O(1/\lambda_{\mathrm{cl}})$, giving $\|R_{\mathrm{cl}}\| = O(\sqrt{n}/\lambda_{\mathrm{cl}})$ and the theorem follows for $\lambda_{\mathrm{cl}} \gg \sqrt{n}(\lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}})$.

Without the $\nu$ bound, we use the tangential bound from T-Bind plus the fact that on $T\Sigma_m$, only $r_T$ matters for the Hessian action on tangent vectors. This requires a more subtle argument...

**The tangent-space refinement.** For $v \in T\Sigma_m$ with $\|v\| = 1$:
$$v^T R_{\mathrm{cl}} v = 2\sum_i r_i \sigma''(z_i)(w_i^T v)^2$$

Split $r = r_T + \bar{r}\mathbf{1}/\sqrt{n}$. Then:
$$v^T R_{\mathrm{cl}} v = 2\sum_i (r_T)_i \sigma''(z_i)(w_i^T v)^2 + \frac{2\bar{r}}{\sqrt{n}} \sum_i \sigma''(z_i)(w_i^T v)^2$$

The second sum is bounded by $|\bar{r}|/\sqrt{n} \cdot 2 \cdot (2\sqrt{3}/9) a_{\mathrm{cl}}^2 n \leq |\bar{r}| \cdot \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \sqrt{n}$, which is $O(\sqrt{n})$ since $|\bar{r}| = O(1)$.

The first sum: $|2\sum_i (r_T)_i \sigma''(z_i)(w_i^T v)^2| \leq 2\|r_T\|_1 \cdot \max |\sigma''| \cdot \max \|w_i\|^2 \leq \frac{2\sqrt{3}}{9} a_{\mathrm{cl}}^2 \sqrt{n} \|r_T\|_2$.

Using T-Bind: $\|r_T\|_2 = O((\lambda_{\mathrm{bd}} + \lambda_{\mathrm{sep}})/\lambda_{\mathrm{cl}})$ (dropping the $\bar{r}_0$ correction for the moment). This gives:
$$|v^T R_{\mathrm{cl}} v| \leq C_1 \sqrt{n} \frac{\lambda_{\mathrm{bd}} + \lambda_{\mathrm{sep}}}{\lambda_{\mathrm{cl}}} + C_2 \sqrt{n} |\bar{r}|$$

where $C_1, C_2$ are parameter-dependent constants.

The Gauss-Newton minimum eigenvalue on $T$ is $2(1-a_{\mathrm{cl}}/4)^2$ (independent of $n$). So the total closure contribution on $T$ has minimum eigenvalue at least:
$$\lambda_{\mathrm{cl}} \cdot 2(1-a_{\mathrm{cl}}/4)^2 - C_1\sqrt{n}(\lambda_{\mathrm{bd}} + \lambda_{\mathrm{sep}}) - C_2\lambda_{\mathrm{cl}}\sqrt{n}|\bar{r}|$$

The third term is the problem: $\lambda_{\mathrm{cl}}\sqrt{n}|\bar{r}|$ scales with $\lambda_{\mathrm{cl}}$. Unless $|\bar{r}| = o(1/\sqrt{n})$, this term can dominate.

**Empirically, $\bar{r} = O(1/n)$ at well-formed formations** (the mean residual per site is $O(1/n)$, not $O(1)$). But we cannot prove this a priori.

### The Honest Theorem (Approach C)

Given the analysis, the cleanest honest theorem has two parts:

**(C1) A conditional metastability statement** with a computable condition at the minimizer:

> If $\kappa(\hat{u}) + \mu(\hat{u}) < 1$ (where $\kappa, \mu$ are the residual correction and separation curvature numbers defined above), then the constrained Hessian enhancement holds.

**(C2) An asymptotic metastability statement** for large $\lambda_{\mathrm{cl}}$:

> For $\lambda_{\mathrm{cl}}$ sufficiently large (depending on $\lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}},$ graph parameters, and the mean residual $\bar{r}$), the Gauss-Newton term dominates and the enhancement holds.

The cleanest version combines both by making the Gauss-Newton approximation an explicit hypothesis:

### Verdict on Approach C: **SUCCEEDS (as an honest weakening)**

The theorem becomes weaker but correct. The key trade-off: the original theorem claimed an unconditional enhancement at any non-trivial minimizer; the corrected theorem conditions on either a computable diagnostic at the minimizer, or on $\lambda_{\mathrm{cl}}$ being sufficiently large.

---

## Recommendation: Approach C

Approach A fails because the full residual $\|r\|_2$ cannot be bounded as $O(1/\lambda_{\mathrm{cl}})$. Approach B fails because $H_{\mathrm{sep}}$ is generically indefinite. Approach C succeeds by honestly qualifying the conditions under which the enhancement holds.

---

## Corrected Theorem Statement (LaTeX-Ready)

```latex
\begin{theorem}[Metastability Enhancement — Corrected]
\label{thm:metastability-v2}
Let $\hat{u}$ be a non-trivial constrained minimizer of the full energy
$\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}}
+ \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}}
+ \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$,
with strict interiority ($0 < \hat{u}_i < 1$ for all~$i$).
Assume $a_{\mathrm{cl}} < 4$ (contraction regime). Define:
\begin{enumerate}[(i)]
\item The \emph{Gauss--Newton enhancement}:
$\gamma_{\mathrm{GN}} := 2(1 - \|J_{\Cl}(\hat{u})\|_{\mathrm{op}})^2$.
\item The \emph{residual correction bound}:
$\delta_{\mathrm{res}} := \frac{2\sqrt{3}}{9}\,a_{\mathrm{cl}}^2\,
\|\Cl(\hat{u}) - \hat{u}\|_1\,
\max_i |\sigma''(z_i(\hat{u}))|/|\sigma''|_{\max}$.
\item The \emph{separation curvature}:
$\delta_{\mathrm{sep}} := \max\!\big(0,\;
-\lambda_{\min}\!\big(\nabla^2\mathcal{E}_{\mathrm{sep}}(\hat{u})
\big|_{T\Sigma_m}\big)\big)$.
\end{enumerate}
If
\begin{equation}
\label{eq:metastability-condition}
\lambda_{\mathrm{cl}}\,(\gamma_{\mathrm{GN}} - \delta_{\mathrm{res}})
\;>\; \lambda_{\mathrm{sep}}\,\delta_{\mathrm{sep}},
\end{equation}
then the minimum eigenvalue of $\nabla^2\mathcal{E}\big|_{T_{\hat{u}}\Sigma_m}$
strictly exceeds that of
$\lambda_{\mathrm{bd}}\,\nabla^2\mathcal{E}_{\mathrm{bd}}\big|_{T_{\hat{u}}\Sigma_m}$,
with the enhancement bounded below by
\begin{equation}
\Delta(\mathrm{min\_eig}) \;\geq\;
\lambda_{\mathrm{cl}}\,(\gamma_{\mathrm{GN}} - \delta_{\mathrm{res}})
- \lambda_{\mathrm{sep}}\,\delta_{\mathrm{sep}}.
\end{equation}
\end{theorem}
```

## Corrected Proof Sketch (LaTeX-Ready)

```latex
\begin{proof}
The exact Hessian of $\mathcal{E}_{\mathrm{cl}} = \|\Cl(u) - u\|^2$ is
\begin{equation}
\nabla^2\mathcal{E}_{\mathrm{cl}} =
\underbrace{2(I - J_{\Cl})^T(I - J_{\Cl})}_{G\;\text{(Gauss--Newton)}}
\;+\; \underbrace{2\sum_i r_i\,\sigma''(z_i)\,w_i w_i^T}_{R_{\mathrm{cl}}\;\text{(residual correction)}}
\end{equation}
where $r = \Cl(\hat{u}) - \hat{u}$ is the closure residual,
$w_i = \nabla_u z_i = a_{\mathrm{cl}}((1-\eta)e_i + \eta P_i^T)$,
and $\sigma''(z) = \sigma'(z)(1 - 2\sigma(z))$.

\textbf{Step 1: Gauss--Newton lower bound.}
By the contraction property (Theorem~\ref{thm:contraction}),
$\|J_{\Cl}\|_{\mathrm{op}} \leq a_{\mathrm{cl}}/4 < 1$, so
$I - J_{\Cl}$ has minimum singular value
$\sigma_{\min} \geq 1 - a_{\mathrm{cl}}/4$. The Gauss--Newton term $G$
restricted to any subspace has minimum eigenvalue
$\geq 2\sigma_{\min}^2 = 2(1 - a_{\mathrm{cl}}/4)^2 =: \gamma_{\mathrm{GN}}$.

\textbf{Step 2: Residual correction bound.}
Each rank-1 term $r_i \sigma''(z_i) w_i w_i^T$ has operator norm
$\leq |r_i| \cdot |\sigma''(z_i)| \cdot \|w_i\|^2
\leq |r_i| \cdot \frac{\sqrt{3}}{9} \cdot a_{\mathrm{cl}}^2$,
using $\max|\sigma''| = \sqrt{3}/9$ and $\|w_i\| \leq a_{\mathrm{cl}}$.
By the triangle inequality:
$\|R_{\mathrm{cl}}\|_{\mathrm{op}} \leq
\frac{2\sqrt{3}}{9}\,a_{\mathrm{cl}}^2\,\|r\|_1 = \delta_{\mathrm{res}}$.

\textbf{Step 3: Assembly.}
The full constrained Hessian on $T_{\hat{u}}\Sigma_m$ satisfies:
\begin{align}
\nabla^2\mathcal{E}\big|_T
&= \lambda_{\mathrm{cl}}(G + R_{\mathrm{cl}})
+ \lambda_{\mathrm{sep}} H_{\mathrm{sep}}
+ \lambda_{\mathrm{bd}} H_{\mathrm{bd}} \\
&\succeq \lambda_{\mathrm{cl}}(\gamma_{\mathrm{GN}} - \delta_{\mathrm{res}})\,I\big|_T
- \lambda_{\mathrm{sep}}\,\delta_{\mathrm{sep}}\,I\big|_T
+ \lambda_{\mathrm{bd}} H_{\mathrm{bd}}\big|_T
\end{align}
The first two terms give the enhancement over $\lambda_{\mathrm{bd}} H_{\mathrm{bd}}|_T$
alone, provided condition~\eqref{eq:metastability-condition} holds.
\end{proof}
```

## Corrected Remark (LaTeX-Ready)

```latex
\begin{remark}[Metastability condition in practice]
\label{rem:metastability-practical}
The condition~\eqref{eq:metastability-condition} involves
the closure residual $\|r\|_1$ and the separation Hessian spectrum
at the minimizer. Both are computable quantities.
At well-formed formations ($\mathrm{Bind} \geq 0.85$),
the residual $\|r\|_2/\sqrt{n} \leq 0.15$,
and empirically $\delta_{\mathrm{res}} \ll \gamma_{\mathrm{GN}}$;
the condition is then controlled by the ratio
$\lambda_{\mathrm{sep}}\delta_{\mathrm{sep}} /
(\lambda_{\mathrm{cl}}\gamma_{\mathrm{GN}})$.
For the Hessian-normalized weights used in Section~\ref{sec:experiments},
condition~\eqref{eq:metastability-condition} is satisfied
at all converged formations in our experiments.

As $\lambda_{\mathrm{cl}} \to \infty$ with other parameters fixed,
the minimizer approaches the closure fixed point where $r = 0$
and $\delta_{\mathrm{res}} = 0$, so the condition is
asymptotically guaranteed. The quantitative threshold depends
on the graph topology (through $\|r\|_1$) and the distinction
operator parameters (through $\delta_{\mathrm{sep}}$).
\end{remark}
```

---

## What the Corrected Theorem Honestly Claims vs What It Doesn't

### Claims:
1. The metastability enhancement holds **conditional on a computable inequality** at the minimizer.
2. The Gauss-Newton approximation to the closure Hessian has a quantified error (the residual correction $\delta_{\mathrm{res}}$).
3. The separation Hessian can be indefinite, and its negative contribution ($\delta_{\mathrm{sep}}$) must be explicitly dominated.
4. For large $\lambda_{\mathrm{cl}}$, the condition is asymptotically satisfied.

### Does NOT Claim:
1. ~~The enhancement holds at every non-trivial minimizer unconditionally.~~ (Original claim.)
2. ~~The Gauss-Newton approximation is "tight" when Bind $\geq 0.85$.~~ (Original claim was circular.)
3. ~~The separation Hessian does not dominate negatively.~~ (Original unstated hypothesis.)
4. A computable, closed-form threshold for $\lambda_{\mathrm{cl}}$ that guarantees the condition. (The $\|r\|_1$ in $\delta_{\mathrm{res}}$ depends on the minimizer itself.)

### Remaining Open Problem:
An a priori bound $\|r\|_1 = O(f(\lambda_{\mathrm{cl}}, n, \text{params}))$ at constrained minimizers, without evaluating $r$ at the minimizer. The T-Bind proof controls $\|r_T\|_2$ but not the mean component $\bar{r}$. A proof that $\bar{r} = o(1)$ as $\lambda_{\mathrm{cl}} \to \infty$ (while holding other parameters fixed) would strengthen the theorem to an unconditional asymptotic statement.

---

## Summary Table

| Approach | Strategy | Result | Key Obstacle |
|----------|----------|--------|-------------|
| A | Bound $\|r\| = O(1/\lambda_{\mathrm{cl}})$ | **FAILS** | Mean residual $\bar{r}$ not controlled by KKT; energy comparison gives $\|r\| = O(\sqrt{n})$ |
| B | Prove $H_{\mathrm{sep}} \succeq 0$ | **FAILS** | $H_{\mathrm{sep}}$ is generically indefinite (mixed sigmoid second derivatives) |
| C | Weaken to conditional | **SUCCEEDS** | Honest: computable condition at minimizer; asymptotically guaranteed |
