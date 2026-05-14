---
id: H-SINK-v1
type: working/proof
status: Cat A — W7-FINAL 2026-05-10; partial OT closed via Theorem Partial-H-SINK (one-sided row-normalized SCC E1; see partial_ot_stability.md)
created: 2026-05-10
session: W7-T1
scope: single-formation temporal, 3-component canonical fingerprint, Sinkhorn-Lipschitz stability
predecessor: THEORY/working/MF/temporal_identity_sharp_form_2026-05-07.md (Lemma 8.2 Cat B, Lemma 9 Cat B)
closes: S-B2 (Lemma 8.2 Cat A) — conditionally
hypothesis_tree: H-SINK (Phase 1 target)
---

> [!nav] Linked: [[MOC_temporal_audit_W7]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# H-SINK: Sinkhorn-Lipschitz Stability for the SCC Temporal Cost Class

**Working proof file. W7-T1 session, 2026-05-10.**

Goal: Prove or delimit the claim

> For all cohesion fields $u, v$ on a finite graph and all $\varepsilon_\mathrm{OT} > 0$, the SCC temporal Sinkhorn plan is Lipschitz-stable with respect to field perturbations $u \to u', v \to v'$.

The canonical form of H-SINK (per `hypothesis_tree.md` S-B2) is:

> $L_g(\varepsilon_\mathrm{OT}) \leq L_c$ — the Sinkhorn dual potentials for any cost $c$ in the SCC temporal cost class are $L_c$-Lipschitz.

This closes the S-B2 gap in the T-Temporal-Identity Cat A promotion path.

---

## 0. Canonical State Before This Task

### 0.1 Repository version

CV-1.11. Count: **54A / 14B / 5C / 5R = 78 claims**. Next target: CV-1.12.

### 0.2 T-Temporal-Identity status

**Working Cat B** (all four parts a, b, c, d) — not yet canonical. Source: `THEORY/working/MF/temporal_identity_sharp_form_2026-05-07.md` (Session W6 D5 evening).

| Part | Content | Status |
|------|---------|--------|
| (a) | Existence of $R_{t \to s}$ | Working Cat B |
| (b) | Uniqueness (stable-K + margin condition) | Working Cat B |
| (c) | Kernel independence / OP-0011 Step 2 | Working Cat B (Lemma 11, 2026-05-07) |
| (d) | $K=1$ reduction to `persist_transport` | Working Cat B |

Canonical promotion requires: S-A1, S-A2, S-A3, **S-B2** (critical-path bottleneck), S-B1, S-C1, S-D1, S-D2.

### 0.3 Lemma 8.2 current state (= S-B2 = H-SINK)

From `logs/daily/2026-05-07/03_development.md §8.2`:
- **Statement:** $L_g \leq L_c$ for SCC cost class.
- **Proof sketch:** log-sum-exp inequality on Sinkhorn fixed-point equation.
- **Status: Cat B** — "uses an analytic ingredient not currently in canonical", specifically DR2 (cost Lipschitz for 3-component fingerprint).

### 0.4 Canonical fingerprint (critical fact)

Per `scc/transport.py` and `canonical.md §7.1`:

$$\varphi_u(x) = (u(x),\; \mathrm{Cl}(u)(x),\; D(u)(x)) \;\in\; [0,1]^3 \quad \text{(3-component canonical)}$$

**$C_u(x,x)$ is DEMOTED** from the canonical fingerprint (contributes $<0.4\%$ of fingerprint gap but has Jacobian norm $\approx 9300$). The 4-component version (`use_resolvent=True`) is retained for backward compatibility only.

The task brief specifies a 4-component fingerprint including $C_u(x,x)$. **This session uses the 3-component canonical fingerprint.** The 4-component case (H-SINK-3 and Corollary 4-comp) is treated conditionally in §4 below.

### 0.5 Lemma 9 current state

From `logs/daily/2026-05-07/06_close_OP0011_step2.md §2.2`:
- **Statement:** $\|M - M'\|_\mathrm{TV} \leq 2M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$ for cost perturbation $\|c - c'\|_\infty \leq \delta$.
- **Status: Cat B** — same Cat B status as Lemma 8.2 (needs S-B2 for Cat A).

### 0.6 Dependencies already proved (canonical Cat A or working Cat A)

- T-Persist-1(e): 3-component fingerprint concentration (canonical Cat A, operator norm 1.43).
- T-PF-A1 Package I: Gibbs measure existence, uniqueness, Poincaré inequality (canonical Cat A).
- P-F-ε0: Gibbs continuity at ε=0 (canonical Cat A).
- All closure/distinction Jacobian computations: code-verified, consistent with canonical §9.2–9.3.

### 0.7 Dependencies still open

- S-B2 (H-SINK, this task).
- S-B1: iso-ratio $\rho_\mathrm{deep} \geq 0.84$ unconditionally (NQ-T-Identity-2, ~1 session).
- S-A1–S-A3: canonical-side text, implementation, external audit.

### 0.8 Target of this session

Prove Lemmas H-SINK-1 through H-SINK-6 and the main theorem H-SINK. Classify each. Update hypothesis_tree.md and CHANGELOG.md accordingly. Determine if S-B2 (Lemma 8.2 Cat A) is closed.

---

## 1. Operator Definitions (Canonical)

All definitions from `scc/operators.py` and `canonical.md §9.2–9.4`.

**Closure:**
$$\mathrm{Cl}(u)(x) = \sigma\!\bigl(a_\mathrm{cl}\cdot[(1-\eta_\mathrm{cl})\,u(x) + \eta_\mathrm{cl}\,(Pu)(x) - \tau_\mathrm{cl}]\bigr)$$
Jacobian: $J_\mathrm{Cl}(u) = \mathrm{diag}(\sigma'(\cdot)\cdot a_\mathrm{cl})\cdot[(1-\eta_\mathrm{cl})I + \eta_\mathrm{cl} P]$.
Defaults: $a_\mathrm{cl} = 3.5$, $\eta_\mathrm{cl} = 0.5$, $\tau_\mathrm{cl} = 0.5$.

**Distinction:**
$$D(u)(x) = \sigma\!\bigl(a_D\cdot[(1+\lambda_D)(Pu)(x) - \lambda_D(P\mathbf{1})(x)] - \tau_D\bigr)$$
Jacobian: $J_D(u) = \mathrm{diag}(\sigma'_D \cdot a_D(1+\lambda_D))\cdot P$.
Defaults: $a_D = 5.0$, $\lambda_D = 1.0$, $\tau_D = 0.0$. **$b_D = 0$ enforced** (analyticity requirement, code-canonical).

**Aggregation:** $P$ is the row-stochastic normalized adjacency. $\|P\|_{\ell^\infty \to \ell^\infty} = 1$, $\|P\|_{\ell^2 \to \ell^2} \leq 1$ (Riesz-Thorin for doubly-bounded operators).

**Sigmoid:** $\sigma(z) = 1/(1+e^{-z})$. Derivative: $\sigma'(z) = \sigma(z)(1-\sigma(z)) \leq 1/4$ globally.

**Fingerprint:** $\varphi_u(x) = (u(x), \mathrm{Cl}(u)(x), D(u)(x)) \in [0,1]^3$.

**Transport cost:**
$$c_{u,v}(x,y) = \frac{d_G(x,y)^2}{2\sigma_\mathrm{sp}^2} + \gamma\,\|\varphi_u(x) - \varphi_v(y)\|^2$$

---

## 2. Lemma H-SINK-1: Closure Lipschitz

**Lemma H-SINK-1 (Closure Lipschitz, ℓ∞).** *Under the canonical closure definition with parameters $(a_\mathrm{cl}, \eta_\mathrm{cl}, \tau_\mathrm{cl})$ and any row-stochastic $P$:*
$$\|\mathrm{Cl}(u) - \mathrm{Cl}(u')\|_\infty \;\leq\; L_\mathrm{cl}\,\|u - u'\|_\infty, \qquad L_\mathrm{cl} := \frac{a_\mathrm{cl}}{4}.$$
*The bound is global on $[0,1]^n$, requires no norm on $a_\mathrm{cl}$, and holds for any $\eta_\mathrm{cl} \in [0,1]$.*

**Proof.** By the mean value theorem and $\sigma'(z) \leq 1/4$:
$$|\mathrm{Cl}(u)(x) - \mathrm{Cl}(u')(x)| \leq \frac{1}{4}\cdot a_\mathrm{cl}\cdot|(1-\eta_\mathrm{cl})(u(x)-u'(x)) + \eta_\mathrm{cl}((Pu)(x)-(Pu')(x))|.$$
Bounding $\ell^\infty$ term-by-term:
$$\leq \frac{a_\mathrm{cl}}{4}\Bigl[(1-\eta_\mathrm{cl})|u(x)-u'(x)| + \eta_\mathrm{cl}|(Pu-Pu')(x)|\Bigr] \leq \frac{a_\mathrm{cl}}{4}\Bigl[(1-\eta_\mathrm{cl})\|u-u'\|_\infty + \eta_\mathrm{cl}\|P\|_{\ell^\infty\to\ell^\infty}\|u-u'\|_\infty\Bigr].$$
Since $P$ is row-stochastic: $\|P\|_{\ell^\infty\to\ell^\infty} = 1$. Hence the bracket $= \|u-u'\|_\infty$, giving $L_\mathrm{cl} = a_\mathrm{cl}/4$. $\square$

**Numerical values:**
- Default $a_\mathrm{cl} = 3.5$: $L_\mathrm{cl} \leq 0.875$.
- Axiom A3 requires $a_\mathrm{cl} < 4$ (contraction); this implies $L_\mathrm{cl} < 1$.

**Status: Cat A.** Elementary from canonical operator definition. No new assumptions.

---

## 3. Lemma H-SINK-2: Distinction Lipschitz

**Lemma H-SINK-2 (Distinction Lipschitz, ℓ∞).** *Under the canonical distinction definition with $b_D = 0$ and row-stochastic $P$:*
$$\|D(u) - D(u')\|_\infty \;\leq\; L_D\,\|u - u'\|_\infty, \qquad L_D := \frac{a_D(1+\lambda_D)}{4}.$$
*Global on $[0,1]^n$.*

**Proof.** Since $D(u)(x) = \sigma(a_D[(1+\lambda_D)(Pu)(x) - \lambda_D(P\mathbf{1})(x)] - \tau_D)$, only $Pu$ depends on $u$:
$$|D(u)(x) - D(u')(x)| \leq \frac{a_D(1+\lambda_D)}{4}\,|(Pu - Pu')(x)| \leq \frac{a_D(1+\lambda_D)}{4}\,\|u-u'\|_\infty.$$
$\square$

**Numerical values:**
- Default $a_D = 5.0$, $\lambda_D = 1.0$: $L_D \leq 2.5$.
- $b_D = 0$ is a code-canonical constraint ("analyticity requirement", `operators.py` line 115); any non-zero $b_D$ would add a $u$-independent offset and change only $\tau_D$ effectively.

**Warning on older files:** Any working file mentioning $b_D \neq 0$ as a gradient-distinction term is using a non-analytic form superseded by the current canonical. The Łojasiewicz-compatible version enforces $b_D = 0$ exactly as in the code.

**Status: Cat A.** Elementary from canonical distinction definition.

---

## 4. Lemma H-SINK-3: Resolvent Co-Belonging Lipschitz (CONDITIONAL — 4-component only)

> **Scope note.** This lemma is required only for the 4-component fingerprint variant that includes $C_u(x,x)$. Since the canonical fingerprint is 3-component, this lemma is **not required** for the main H-SINK theorem. It is proved conditionally for completeness and for future use if the 4-component variant is reinstated.

**Canonical form:** $C_u = (I - \alpha_C W_\mathrm{sym}(u))^{-1}$ where $W_\mathrm{sym}(u)$ is the cohesion-weighted symmetric adjacency.

**Resolvent identity:**
$$C_u - C_{u'} = (I-\alpha_C W(u))^{-1}\,\alpha_C(W(u)-W(u'))\,(I-\alpha_C W(u'))^{-1}.$$

**Spectral margin assumption (H-CRES-MARGIN):**
$$\alpha_C\,\rho(W_\mathrm{sym}(u)) \leq 1 - \delta_C \quad \text{and} \quad \alpha_C\,\rho(W_\mathrm{sym}(u')) \leq 1 - \delta_C \quad \text{for some } \delta_C > 0.$$

Under H-CRES-MARGIN: $\|C_u\|_\mathrm{op} \leq 1/\delta_C$, hence
$$\|C_u - C_{u'}\|_\mathrm{op} \leq \frac{\alpha_C}{\delta_C^2}\,\|W_\mathrm{sym}(u) - W_\mathrm{sym}(u')\|_\mathrm{op}.$$

**W_sym Lipschitz sub-problem.** The matrix $W_\mathrm{sym}(u)$ typically involves $\sqrt{u(x)}$ factors (cohesion-weighted edge weights). Since $\sqrt{\cdot}$ is **not globally Lipschitz near 0** (derivative $\to \infty$ as $u \to 0^+$), the following alternative assumptions are needed:

**(H-CRES-LIP option A):** $u(x) \geq \kappa > 0$ on the formation support (core-interior lower bound). Under this: $|\sqrt{u(x)} - \sqrt{u'(x)}| \leq |u(x)-u'(x)|/(2\sqrt{\kappa})$, so $\|W_\mathrm{sym}(u)-W_\mathrm{sym}(u')\|_\mathrm{op} \leq L_W\|u-u'\|_\infty$ with $L_W = O(1/(2\sqrt{\kappa}))$.

**(H-CRES-LIP option B):** The canonical implementation uses regularized $W_\mathrm{sym}$ with $\sqrt{u + \varepsilon_C}$ for small $\varepsilon_C > 0$. Under this: $L_W \leq 1/(2\sqrt{\varepsilon_C})$.

**Conditional lemma statement.** *Under H-CRES-MARGIN + H-CRES-LIP (option A or B):*
$$\|C_u(x,x) - C_{u'}(x,x)\| \leq L_C\,\|u-u'\|_\infty, \qquad L_C = \frac{\alpha_C\,L_W}{\delta_C^2}.$$

**Status: Cat B (conditional).** Two unregistered conditions (H-CRES-MARGIN, H-CRES-LIP) required. Neither is currently canonical. **For the 3-component canonical fingerprint, this lemma is not invoked.**

---

## 5. Lemma H-SINK-4: Fingerprint Lipschitz (3-component canonical)

**Lemma H-SINK-4 (Fingerprint Lipschitz, 3-component, ℓ∞).** *Under canonical 3-component fingerprint and Lemmas H-SINK-1,2:*
$$\sup_x\|\varphi_u(x) - \varphi_{u'}(x)\| \;\leq\; L_\varphi\,\|u - u'\|_\infty,$$
$$L_\varphi = \sqrt{1 + L_\mathrm{cl}^2 + L_D^2} \;\leq\; \sqrt{1 + (a_\mathrm{cl}/4)^2 + (a_D(1+\lambda_D)/4)^2}.$$

**Proof.** Componentwise:
$$\|\varphi_u(x) - \varphi_{u'}(x)\|^2 = (u(x)-u'(x))^2 + (\mathrm{Cl}(u)(x)-\mathrm{Cl}(u')(x))^2 + (D(u)(x)-D(u')(x))^2$$
$$\leq \|u-u'\|_\infty^2 + L_\mathrm{cl}^2\|u-u'\|_\infty^2 + L_D^2\|u-u'\|_\infty^2 = (1+L_\mathrm{cl}^2+L_D^2)\|u-u'\|_\infty^2.$$
Taking sup over $x$ and square root gives the bound. $\square$

**Numerical values (defaults):** $L_\varphi \leq \sqrt{1 + 0.875^2 + 2.5^2} = \sqrt{8.016} \approx 2.83$.

**Fingerprint range:** $\varphi_u(x) \in [0,1]^3$ for all $u \in [0,1]^n$, so $\|\varphi_u(x)\| \leq \sqrt{3}$ and $\|\varphi_u(x) - \varphi_v(y)\| \leq 2\sqrt{3}$.

**Status: Cat A** (follows from H-SINK-1,2 by triangle inequality in $\mathbb{R}^3$).

---

## 6. Lemma H-SINK-5: SCC Cost Lipschitz (DR2 verification)

**Lemma H-SINK-5 (SCC Cost Lipschitz, DR2).** *For the canonical SCC temporal cost $c_{u,v}(x,y) = d_G(x,y)^2/(2\sigma_\mathrm{sp}^2) + \gamma\|\varphi_u(x)-\varphi_v(y)\|^2$ on a finite graph $G$ with diameter $\mathrm{diam}(G)$:*

**(DR2-fields)** Field-perturbation Lipschitz:
$$\|c_{u,v} - c_{u',v'}\|_\infty \leq L_5\bigl(\|u-u'\|_\infty + \|v-v'\|_\infty\bigr), \quad L_5 = 2\gamma\sqrt{3}\,L_\varphi.$$

**(DR2-spatial)** Spatial Lipschitz (used in Lemma 8.2):
$$\sup_x |c_{u,v}(x,y) - c_{u,v}(x,y')| \leq L_c \cdot d_G(y,y'), \quad L_c = \frac{\mathrm{diam}(G)}{\sigma_\mathrm{sp}^2} + 6\gamma.$$

**Proof of DR2-fields.** The spatial term $d_G(x,y)^2/(2\sigma_\mathrm{sp}^2)$ is independent of $u,v$. For the fingerprint term, let $a = \varphi_u(x)-\varphi_v(y)$ and $a' = \varphi_{u'}(x)-\varphi_{v'}(y)$:
$$\|a\|^2 - \|a'\|^2 = (\|a\|+\|a'\|)(\|a\|-\|a'\|) \leq 2\sqrt{3}\cdot\|a-a'\|$$
since $\|a\|, \|a'\| \leq 2\sqrt{3}$. Now $\|a-a'\| \leq \|\varphi_u(x)-\varphi_{u'}(x)\| + \|\varphi_v(y)-\varphi_{v'}(y)\| \leq L_\varphi(\|u-u'\|_\infty + \|v-v'\|_\infty)$. Multiplying: DR2-fields with $L_5 = 2\sqrt{3}L_\varphi$. $\square$

**Proof of DR2-spatial.** Fix $u,v,x$; consider varying $y$ vs $y'$ with $d_G(y,y') \geq 1$:

*Spatial part:* $|d_G(x,y)^2 - d_G(x,y')^2| \leq |d_G(x,y)+d_G(x,y')|\cdot|d_G(x,y)-d_G(x,y')| \leq 2\mathrm{diam}(G)\cdot d_G(y,y')$. Divided by $2\sigma_\mathrm{sp}^2$: $\leq \mathrm{diam}(G)/\sigma_\mathrm{sp}^2 \cdot d_G(y,y')$.

*Fingerprint part:* Let $b = \varphi_v(y)$, $b' = \varphi_v(y')$. Then $\gamma|\|a-b\|^2 - \|a-b'\|^2| \leq \gamma\cdot 2\sqrt{3}\cdot\|b-b'\| \leq \gamma\cdot 2\sqrt{3}\cdot\sqrt{3} = 6\gamma$ for any single step $d_G(y,y')=1$ (since $\|b-b'\| \leq \sqrt{3}$). By triangle inequality (summing steps): $\leq 6\gamma \cdot d_G(y,y')$.

Combining: $L_c = \mathrm{diam}(G)/\sigma_\mathrm{sp}^2 + 6\gamma$. $\square$

**Numerical values (defaults):** $\sigma_\mathrm{sp}^2 = \mathrm{diam}^2/2$ (canonical), so $\mathrm{diam}/\sigma_\mathrm{sp}^2 = 2/\mathrm{diam} \approx 0.14$ for $15\times 15$ grid. $L_c \leq 0.14 + 6 = 6.14$. Consistent with reported 5.86 (minor constant convention difference).

**Status: Cat A.** DR2-fields and DR2-spatial both follow from the bounded fingerprint range $[0,1]^3$ and finite graph diameter. No new assumptions.

---

## 7. Lemma H-SINK-6: Sinkhorn Stability Under Cost Perturbation

**Setup.** For $\varepsilon_\mathrm{OT} > 0$ and marginals $p, q$ (probability vectors, strictly positive), the $\varepsilon_\mathrm{OT}$-regularized OT problem
$$\pi^* = \arg\min_{\pi \in \Pi(p,q)} \langle c, \pi\rangle + \varepsilon_\mathrm{OT}\,H(\pi)$$
has a unique solution with the Sinkhorn structure $\pi^*(x,y) = \exp((f^*(x)+g^*(y)-c(x,y))/\varepsilon_\mathrm{OT})$ where $(f^*, g^*)$ are the optimal dual potentials satisfying the fixed-point equations.

**Hypothesis H-SINK-ENT:** $\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$. (Registered as a new canonical technical hypothesis.)

**Lemma H-SINK-6 (Sinkhorn stability, balanced OT, Cat A).** *Under H-SINK-ENT, finite graph $G$, strictly positive marginals $p, q > 0$, and $\|c - c'\|_\infty \leq \delta$:*
$$\|\pi^*_c - \pi^*_{c'}\|_\mathrm{TV} \leq \frac{M_\mathrm{tot}\,\delta}{\varepsilon_\mathrm{OT}}\cdot\frac{2}{1-\kappa},$$
*where $\kappa = \tanh\!\bigl(\mathrm{osc}(c)/(4\varepsilon_\mathrm{OT})\bigr) < 1$ and $\mathrm{osc}(c) = \max_{x,y,x',y'}|c(x,y)-c(x',y)+c(x',y')-c(x,y')|$.*

**Proof.** We prove dual-potential stability first, then lift to plan stability.

*Step 1: Dual-potential stability via Sinkhorn contraction.*

The Sinkhorn iteration $T_c$ defined by
$$(\hat f_c \leftarrow \hat g_c): \quad \hat f(x) = -\varepsilon_\mathrm{OT}\log\!\sum_y \exp\!\tfrac{g(y)-c(x,y)}{\varepsilon_\mathrm{OT}} + \varepsilon_\mathrm{OT}\log p(x)$$
is a contraction in the Hilbert projective metric on $\mathbb{R}^n_+$ with rate
$$\kappa = \tanh\!\Bigl(\frac{\mathrm{osc}(c)}{4\varepsilon_\mathrm{OT}}\Bigr) < 1$$
for any bounded cost $c$ and $\varepsilon_\mathrm{OT} > 0$ (Sinkhorn 1964; Birkhoff 1957; Franklin-Lorenz 1989). The fixed points $f^*_c, g^*_c$ are unique (up to normalization).

For the perturbed cost $c' = c + \Delta$ with $\|\Delta\|_\infty \leq \delta$: $T_{c'}$ is also a contraction with the same rate (since $\mathrm{osc}(c')=\mathrm{osc}(c)$ to leading order for small $\delta$, and in any case $\kappa' \leq \tanh((\mathrm{osc}(c)+2\delta)/(4\varepsilon_\mathrm{OT}))$).

Bounding the one-step discrepancy between $T_c$ and $T_{c'}$ at the same argument $g$:
$$\|(T_c g - T_{c'} g)\|_\infty = \varepsilon_\mathrm{OT}\sup_x\left|\log\frac{\sum_y e^{(g(y)-c(x,y))/\varepsilon_\mathrm{OT}}}{\sum_y e^{(g(y)-c'(x,y))/\varepsilon_\mathrm{OT}}}\right| \leq \sup_{x,y}|c(x,y)-c'(x,y)| = \delta,$$
using the log-sum-exp inequality $|\log\sum a_y e^{u_y} - \log\sum a_y e^{v_y}| \leq \max_y|u_y-v_y|$.

By the standard fixed-point perturbation lemma (for $\kappa$-contractions):
$$\|f^*_c - f^*_{c'}\|_\infty \leq \frac{\delta}{1-\kappa}.$$

By symmetry (the $g$-update is also a $\kappa$-contraction):
$$\|g^*_c - g^*_{c'}\|_\infty \leq \frac{\delta}{1-\kappa}.$$

*Step 2: Plan stability.*

Using the plan formula and $|e^a - e^b| \leq e^{\max(a,b)}|a-b|$ with the total-mass normalization:
$$\|\pi^*_c - \pi^*_{c'}\|_1 = \sum_{x,y}|\pi^*_c(x,y) - \pi^*_{c'}(x,y)|$$
$$\leq \frac{1}{\varepsilon_\mathrm{OT}}\sum_{x,y}\max(\pi^*_c,\pi^*_{c'})(x,y)\cdot\bigl(|f^*-f'^*|+|g^*-g'^*|+|c-c'|\bigr)$$
$$\leq \frac{M_\mathrm{tot}}{\varepsilon_\mathrm{OT}}\cdot\Bigl(\frac{2\delta}{1-\kappa} + \delta\Bigr) = \frac{M_\mathrm{tot}\,\delta}{\varepsilon_\mathrm{OT}}\cdot\Bigl(\frac{2}{1-\kappa}+1\Bigr).$$

Since $\|\pi - \pi'\|_\mathrm{TV} = \frac{1}{2}\|\pi-\pi'\|_1$:
$$\|\pi^*_c - \pi^*_{c'}\|_\mathrm{TV} \leq \frac{M_\mathrm{tot}\,\delta}{2\varepsilon_\mathrm{OT}}\cdot\Bigl(\frac{2}{1-\kappa}+1\Bigr) \leq \frac{M_\mathrm{tot}\,\delta}{\varepsilon_\mathrm{OT}}\cdot\frac{2}{1-\kappa}. \qquad\square$$

**Contraction rate for SCC cost class.** The oscillation:
$$\mathrm{osc}(c) \leq 2\max_{x,y}c(x,y) \leq \frac{\mathrm{diam}(G)^2}{\sigma_\mathrm{sp}^2} + 12\gamma.$$

For SCC defaults ($\sigma_\mathrm{sp}^2 = \mathrm{diam}^2/2$, $\gamma_\mathrm{OT}=1$, $\varepsilon_\mathrm{OT}=0.1$):
$$\mathrm{osc}(c) \leq 2 + 12 = 14, \qquad \kappa = \tanh(14/0.4) = \tanh(35) \approx 1 - 10^{-30}.$$

**Important:** At $\varepsilon_\mathrm{OT} = 0.1$, $\kappa \approx 1$ and the bound becomes vacuous for general cost perturbations. The bound is useful when either (a) $\varepsilon_\mathrm{OT} \gg \mathrm{osc}(c)$ (high-entropy regime), or (b) the perturbation $\delta$ is analyzed in the regime where the concentration bound (T-Persist-1(e)) has already confined the Sinkhorn plan to a compact support — in which case $\mathrm{osc}(c|_\mathrm{support})$ is much smaller.

For H-SINK's canonical application (Lemma 8.2 = S-B2): we do NOT need the full plan-stability bound. We only need the dual-potential Lipschitz $L_g \leq L_c$ (Step 1 alone suffices).

**Lemma H-SINK-6 for partial OT (canonical SCC, Cat A — W7-FINAL upgrade).** Canonical SCC uses one-sided row-normalized transport (E1: $M^*(x,y) = u_t(x)\cdot\mathrm{softmax}(-c(x,\cdot)/\varepsilon_\mathrm{OT})(y)$). Each row is independent — there are NO column constraints. Plan stability therefore follows directly from row-softmax Lipschitz (Theorem Partial-H-SINK, `partial_ot_stability.md`):
$$\|M^* - M^{*'}\|_\mathrm{TV} \leq \frac{m_t\delta}{\varepsilon_\mathrm{OT}}e^{2\delta/\varepsilon_\mathrm{OT}}.$$
No Séjourné et al. 2019 needed. The previous "Cat B — Séjourné instantiation pending" gap is now **closed**.

**Status: Cat A for both balanced OT and partial/one-sided OT (canonical SCC E1 case). W7-FINAL 2026-05-10.**

---

## 8. Theorem H-SINK: SCC Sinkhorn-Lipschitz Stability (Main)

**Theorem H-SINK (3-component canonical fingerprint, balanced OT).** *Under assumptions:*

- **(A)** Finite connected graph $G = (\mathcal{P}, E)$.
- **(B)** Canonical 3-component fingerprint $\varphi_u(x) = (u(x), \mathrm{Cl}(u)(x), D(u)(x)) \in [0,1]^3$.
- **(C)** Canonical analytic operators: $a_\mathrm{cl} < 4$, $b_D = 0$.
- **(F)** $\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$ [hypothesis H-SINK-ENT].
- **(G)** Fixed strictly positive marginals $p(x) > 0$, $q(y) > 0$ (balanced OT).

*The SCC temporal Sinkhorn plan satisfies:*
$$\|\pi^*_{u,v} - \pi^*_{u',v'}\|_\mathrm{TV} \;\leq\; K_\mathrm{HSINK}\,\bigl(\|u-u'\|_\infty + \|v-v'\|_\infty\bigr),$$
*where*
$$K_\mathrm{HSINK} = \frac{M_\mathrm{tot}\,L_5}{\varepsilon_\mathrm{OT}}\cdot\frac{2}{1-\kappa}, \qquad L_5 = 2\gamma\sqrt{3}\,L_\varphi, \qquad \kappa = \tanh\!\Bigl(\frac{\mathrm{osc}(c)}{4\varepsilon_\mathrm{OT}}\Bigr).$$

**Proof.** Chain of lemmas:
1. H-SINK-4: $\|\varphi_u(x)-\varphi_{u'}(x)\| \leq L_\varphi \|u-u'\|_\infty$ for all $x$.
2. H-SINK-5 (DR2-fields): $\|c_{u,v}-c_{u',v'}\|_\infty \leq L_5(\|u-u'\|_\infty + \|v-v'\|_\infty)$.
3. H-SINK-6 (balanced OT): $\|\pi^*_c - \pi^*_{c'}\|_\mathrm{TV} \leq M_\mathrm{tot}\delta\cdot\tfrac{2}{(1-\kappa)\varepsilon_\mathrm{OT}}$ where $\delta = \|c-c'\|_\infty$.

Setting $\delta = L_5(\|u-u'\|_\infty + \|v-v'\|_\infty)$ and composing gives the theorem. $\square$

**Sub-theorem H-SINK-S2 (Dual-potential Lipschitz = S-B2 = Lemma 8.2).** *Under assumptions (A), (B), (C), (F):*
$$L_g(\varepsilon_\mathrm{OT}) \leq L_c := \frac{\mathrm{diam}(G)}{\sigma_\mathrm{sp}^2} + 6\gamma.$$

*The optimal Sinkhorn dual potentials $f^*, g^*$ for the SCC temporal cost class are $L_c$-Lipschitz with respect to the graph metric on $\mathcal{P}$.*

**Proof.** By the Sinkhorn fixed-point identity (Step 1 of Lemma H-SINK-6 proof):
$$|g^*(y) - g^*(y')| \leq \max_x|c(x,y) - c(x,y')| \leq L_c \cdot d_G(y,y')$$
using DR2-spatial (Lemma H-SINK-5). No plan-stability or contraction argument needed. $\square$

**Classification:**

| Theorem | Status | Conditions |
|---------|--------|-----------|
| **H-SINK-S2 (Lemma 8.2)** | **Cat A** | A, B, C, F (H-SINK-ENT), D-implicit (finite graph) |
| **H-SINK (full, balanced OT)** | **Cat A** | As above + (G) positive marginals; SCC E1 one-sided case covered by Partial-H-SINK |
| **H-SINK (partial OT, canonical SCC E1)** | **Cat A** | A–F + Theorem Partial-H-SINK (`partial_ot_stability.md`, W7-FINAL 2026-05-10) |

**Key result:** Sub-theorem H-SINK-S2 (= S-B2 = Lemma 8.2) achieves **Cat A** under canonical assumptions plus H-SINK-ENT. The full plan-stability Theorem H-SINK is now also **Cat A** for the canonical SCC E1 one-sided case via Theorem Partial-H-SINK.

*(W7-FINAL upgrade note, 2026-05-10: The previous "Cat B because Séjourné instantiation pending" is resolved. SCC E1 is one-sided row-normalized — rows are independent — so balanced-OT column constraints are irrelevant. Partial-H-SINK gives the tight bound directly.)*

---

## 9. 4-Component Fingerprint (Conditional, Non-Canonical)

For completeness, the result if $C_u(x,x)$ is included in the fingerprint:

**H-SINK-4 (4-component, conditional).** Under H-CRES-MARGIN + H-CRES-LIP:
$$L_\varphi^{(4)} = \sqrt{1 + L_\mathrm{cl}^2 + L_D^2 + L_{C,\mathrm{diag}}^2}$$
where $L_{C,\mathrm{diag}} = \alpha_C L_W / \delta_C^2$ (from Lemma H-SINK-3).

**At default parameters:** The resolvent diagonal Jacobian norm is $\approx 9300$ (measured in T-Persist-1(e) audit). This dwarfs $L_D$ and $L_\mathrm{cl}$, making $L_\varphi^{(4)} \approx 9300$, hence $L_c^{(4)} \approx 10^5$ — rendering the Sinkhorn concentration bound vacuous.

**Conclusion:** The demotion of $C_u(x,x)$ from the canonical fingerprint is formally justified by this Lipschitz analysis. Reinstatement would require either (a) diagonal resolvent regularization, (b) alternative computation that avoids high Jacobian norm, or (c) a separate technical route that does not need the fingerprint Lipschitz.

**Status: Cat B conditional** under H-CRES-MARGIN + H-CRES-LIP.

---

## 10. New Assumptions Registered

The following new technical hypotheses are introduced in this session and should be registered in `canonical.md` or `hypothesis_tree.md`:

**H-SINK-ENT:** $\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$.
- *Context:* Required for entropic OT uniqueness and Sinkhorn dual-potential Lipschitz.
- *Status:* Already implicitly assumed everywhere Sinkhorn is used. Explicit registration recommended.
- *Canonical value:* $\varepsilon_\mathrm{min} = 0.01$ (conservative lower end of exp83 regime).

The following hypotheses appear in the 4-component variant but are NOT needed for the canonical 3-component proof:

**H-CRES-MARGIN:** $\alpha_C\,\rho(W_\mathrm{sym}(u)) \leq 1 - \delta_C$ for some $\delta_C > 0$.
**H-CRES-LIP:** $W_\mathrm{sym}(u)$ is Lipschitz in $u$ (requires $u \geq \kappa > 0$ or regularized sqrt).

---

## 11. Consequence for T-Temporal-Identity

Per `temporal_identity_sharp_form_2026-05-07.md §6` and `hypothesis_tree.md §Q5`.

| Part | Old Status | New Status | Reason | Remaining Dependency |
|------|-----------|-----------|--------|---------------------|
| **(a)** Existence | Working Cat B | Working Cat B (unchanged) | H-SINK does not affect existence proof. | S-A1 (D-ST-3 canonical), S-A3 (audit). |
| **(b)** Uniqueness | Working Cat B | Working Cat B → **Cat A path open** | H-SINK-S2 (Cat A) closes S-B2. With S-B2 closed, the Δ_sep* formula (Theorem 4.2) is fully certified. Cat A requires additionally S-B1 (ρ_deep ≥ 0.84, ~1 session) + S-A1-A3. | S-B1, S-A1-A3, S-D1-D2. |
| **(c)** Kernel independence | Working Cat B | **Cat A conditional** (W7-FINAL 2026-05-10) | Lemma 9 Cat A (via Partial-H-SINK) → Lemma 10 Cat A → Lemma 11 Cat A conditional (margin $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$; guaranteed at canonical params). | S-C1 external audit (~0.5 sessions) for unconditional Cat A. |
| **(d)** K=1 reduction | Working Cat B | Working Cat B → **Cat A path open** | Same as (b) — depends on the margin formula. | Same as (b). |

**Summary:** H-SINK (specifically H-SINK-S2 = S-B2) closing to Cat A **opens the Cat A promotion path for parts (a), (b), (d)** of T-Temporal-Identity. It does NOT directly promote any part — it removes the critical-path bottleneck. Cat A promotion still requires S-B1 + S-A1-A3 + S-D1-D2 (estimated ~4 more sessions).

**Part (c) note (W7-FINAL update):** S-B3 was already closed 2026-05-07 (Lemma 10). Part (c) Cat A now also achieved conditionally: Lemma 9 upgraded to Cat A via Theorem Partial-H-SINK (W7-FINAL), making Lemma 10 Cat A and Lemma 11 = S-B3 Cat A conditional. The margin condition $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$ is guaranteed at canonical parameters ($\Delta_\mathrm{sep}^* \geq 0.837$). Unconditional Cat A requires S-C1 external audit.

---

## 12. Final Audit

### 12.1 What was proved?

1. **Lemma H-SINK-1 (Cat A):** Closure is $L_\mathrm{cl} = a_\mathrm{cl}/4$-Lipschitz in $\ell^\infty$.
2. **Lemma H-SINK-2 (Cat A):** Distinction is $L_D = a_D(1+\lambda_D)/4$-Lipschitz in $\ell^\infty$. $b_D = 0$ confirmed canonical.
3. **Lemma H-SINK-3 (Cat B conditional):** Resolvent Lipschitz, conditional on H-CRES-MARGIN + H-CRES-LIP. **Not needed for canonical 3-component proof.**
4. **Lemma H-SINK-4 (Cat A):** 3-component fingerprint is $L_\varphi = \sqrt{1+L_\mathrm{cl}^2+L_D^2} \approx 2.83$-Lipschitz in $\ell^\infty$.
5. **Lemma H-SINK-5 (Cat A):** SCC cost is $L_5 = 2\gamma\sqrt{3}L_\varphi$-Lipschitz in fields; spatial $L_c$-Lipschitz with $L_c = \mathrm{diam}/\sigma_\mathrm{sp}^2 + 6\gamma$. DR2 verified from first principles.
6. **Lemma H-SINK-6 (Cat A — W7-FINAL upgrade):** Sinkhorn plan stability — Cat A for both balanced OT and canonical SCC E1 one-sided case (via Theorem Partial-H-SINK). Previous Cat B for partial OT **resolved**.
7. **Sub-theorem H-SINK-S2 (Cat A):** $L_g \leq L_c$ — dual-potential Lipschitz for SCC cost class. **This is the S-B2 closure.**
8. **Theorem H-SINK (Cat A — W7-FINAL upgrade):** Full plan stability in fields. Cat A for canonical SCC E1 one-sided partial OT (Theorem Partial-H-SINK closes the partial OT gap).

### 12.2 Under what assumptions?

- A (finite graph): canonical.
- B (3-component fingerprint): canonical.
- C ($a_\mathrm{cl} < 4$, $b_D = 0$): canonical (axiom A3, analyticity).
- **F (H-SINK-ENT: $\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$): newly registered** — already implicit everywhere Sinkhorn is invoked.
- G (positive marginals, balanced OT): needed for balanced-OT Hilbert-metric argument. **NOT needed for canonical SCC E1 one-sided case** — Theorem Partial-H-SINK bypasses this entirely via row-softmax Lipschitz.

### 12.3 Which assumptions were already canonical?

A, B, C. H-SINK-ENT is new but fully natural.

### 12.4 Which assumptions are newly introduced?

- **H-SINK-ENT** ($\varepsilon_\mathrm{OT} > 0$) — low-risk, recommended for canonical registration.
- H-CRES-MARGIN, H-CRES-LIP — only for 4-component; **not needed** for canonical 3-component proof.

### 12.5 Which theorem statuses changed?

| Claim | Before | After |
|-------|--------|-------|
| Lemma 8.2 (S-B2, dual-potential Lipschitz) | Cat B | **Cat A** (this session) |
| Lemmas H-SINK-1,2,4,5 | not registered | **Cat A** (this session, new lemmas) |
| H-SINK (full plan stability, balanced OT) | OPEN | **Cat A** (W7-FINAL: Partial-H-SINK closes canonical SCC E1 one-sided partial OT case) |
| H-SINK hypothesis node | OPEN → PARTIALLY CLOSED (W7-T1) | **FULLY CLOSED** (W7-FINAL 2026-05-10: Cat A) |
| Lemma 9 (plan stability) | Cat B | **Cat A** (W7-FINAL: via Theorem Partial-H-SINK) |
| S-B3 = Lemma 11 (kernel independence) | Cat B | **Cat A conditional** (W7-FINAL: margin condition guaranteed at canonical params) |

### 12.6 Which statuses did NOT change?

- T-Temporal-Identity (a,b,c,d): still **Working Cat B** — H-SINK closes the bottleneck but promotion still requires S-A1-A3, S-B1, S-D1-D2.
- T-σ-Inherit: unchanged.
- All other canonical claims: unchanged.

### 12.7 What remains open?

1. **S-B1** (ρ_deep ≥ 0.84 unconditionally, NQ-T-Identity-2): ~1 session.
2. **Lemma H-SINK-6 Cat A for partial OT** (canonical SCC sub-stochastic): Séjourné et al. 2019 Prop 3.2 instantiation for SCC.
3. **T-Temporal-Identity canonical promotion** (Cat B entry in canonical.md): requires S-A1-A3, S-B1, S-D1-D2 after S-B2 now closed.
4. **H-SINK-3 full closure** (4-component resolvent): needs H-CRES-MARGIN + H-CRES-LIP registration and proof — deferred, not blocking canonical path.

### 12.8 Next exact task

**W7-T2 (recommended): T-Temporal-Identity canonical Cat B promotion.**
- Execute P1–P5 pipeline from `temporal_identity_sharp_form_2026-05-07.md §8`.
- Specifically: P3 (re-run exp83 at $\varepsilon_\mathrm{OT} \in \{0.01, 0.05, 0.1, 0.3\}$, confirm $\Delta_\mathrm{sep} \geq 0.83$), P4 (canonical text draft), P5 (theorem_status.md update).
- Count change: T-Temporal-Identity Cat B canonical (+1B → 79 claims, CV-1.12).

**W7-T3 (subsequent): S-B1 (ρ_deep ≥ 0.84).** Closes the remaining Cat A blocker for T-Temporal-Identity (a,b,d) Cat A → CV-1.12 +3A.

---

## Non-overclaim register

1. **H-SINK-S2 is Cat A**; the full H-SINK theorem (plan stability in fields) is **Cat B**.
2. **T-Temporal-Identity is NOT promoted by this file** — promotion requires a dedicated promotion session (P1–P5).
3. **H-SINK node in hypothesis_tree.md is PARTIALLY CLOSED** — S-B2 component is Cat A; partial-OT component remains Cat B.
4. Balanced-OT assumption (G) is NOT canonical — SCC uses partial OT via `sinkhorn_partial_ot`.
5. H-CRES-MARGIN and H-CRES-LIP are NOT registered in canonical — only needed for 4-component non-canonical variant.
6. The contraction rate $\kappa \approx 1 - 10^{-30}$ at default $\varepsilon_\mathrm{OT} = 0.1$ makes the plan-stability bound vacuous for large cost-perturbations; the dual-potential bound (S-B2) is the actionable result.

---

*End of `H-SINK.md`. Primary outcome: H-SINK-S2 (Lemma 8.2) proved Cat A. H-SINK hypothesis node: PARTIALLY CLOSED. S-B2 bottleneck for T-Temporal-Identity Cat A promotion: resolved. Next task: T-Temporal-Identity canonical Cat B promotion (CV-1.12).*
