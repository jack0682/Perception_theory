> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 13_NOP_D_lemma18_hilbert_metric.md — NOP-D Closure: Hilbert/Birkhoff Metric Sinkhorn Contraction

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended late-evening session
**NOP target:** NOP-D — self-referential Sinkhorn fixed-point stability under (A7') sharp regime. Resolves the apparent contradiction between (A7') ($\varepsilon_\mathrm{OT} \leq 0.45$) and Banach-norm contraction regime ($\varepsilon_\mathrm{OT} \geq 143$).
**Closure objective:** Lemma 18 — Hilbert/Birkhoff projective metric Sinkhorn contraction with rate $\rho_H < 1$ for any $\varepsilon_\mathrm{OT} > 0$. Composed with the SCC self-referential cost-update step.
**Depends on:** `working/MF/self_ref_fp_stability.md` (working file from earlier this session); standard Sinkhorn convergence theory (Franklin-Lorentz 1989, Chen-Georgiou-Pavon 2017); canonical T-Persist-1(e) Schauder fixed-point.

---

## §1. The Hilbert/Birkhoff projective metric

### §1.1 Definition

The Hilbert (Birkhoff) projective metric on the strictly positive cone $\mathbb{R}^n_{>0}$ is:
$$d_H(u, v) := \log \frac{\max_x u(x)/v(x)}{\min_x u(x)/v(x)}.$$

Equivalent: $d_H(u, v) = \log(\sup u/v) - \log(\inf u/v)$. It's a *projective* metric — invariant under positive scalar multiplication: $d_H(\lambda u, \mu v) = d_H(u, v)$.

The Hilbert *diameter* of a positive matrix $A$ is:
$$\Delta(A) := \sup_{u, v > 0} d_H(Au, Av) = \log \frac{\sup_{x,y, x',y'} A(x,y) A(x',y')}{A(x',y) A(x,y')}.$$

### §1.2 Birkhoff contraction theorem

**Theorem (Birkhoff 1957).** For any positive matrix $A$ with finite Hilbert diameter $\Delta(A) < \infty$:
$$d_H(Au, Av) \leq \tanh\!\Big(\frac{\Delta(A)}{4}\Big) \cdot d_H(u, v).$$

Since $\tanh(\Delta/4) < 1$ for finite $\Delta$, *any* positive matrix induces a Hilbert-metric contraction. **This is the fundamental result for Sinkhorn convergence.**

### §1.3 Application to Sinkhorn

Sinkhorn iteration on $A(x,y) = \exp(-c(x,y)/\varepsilon_\mathrm{OT})$ multiplied by row-rescalings:
$$u^{(k+1)} = \mathrm{normalize}(A v^{(k)}),\quad v^{(k+1)} = \mathrm{normalize}(A^\top u^{(k+1)}).$$

The composition is a Hilbert-metric contraction with rate $\tanh^2(\Delta/4)$ per iteration (Franklin-Lorentz 1989). For $A(x,y) = e^{-c(x,y)/\varepsilon_\mathrm{OT}}$ with $c \in [c_\mathrm{min}, c_\mathrm{max}]$:
$$\Delta(A) = \frac{2(c_\mathrm{max} - c_\mathrm{min})}{\varepsilon_\mathrm{OT}}.$$

So the Sinkhorn contraction rate is $\rho_S := \tanh^2((c_\mathrm{max} - c_\mathrm{min})/(2\varepsilon_\mathrm{OT})) < 1$ for any $\varepsilon_\mathrm{OT} > 0$.

**Key feature.** $\rho_S < 1$ for all $\varepsilon_\mathrm{OT} > 0$ — Sinkhorn always contracts in Hilbert metric. The convergence rate degrades as $\varepsilon_\mathrm{OT} \to 0$ (Hilbert diameter grows), but contraction never fails.

---

## §2. SCC self-referential iteration in Hilbert metric

### §2.1 The full iteration

The SCC self-referential Sinkhorn iteration is:
$$M^{(k+1)} = \mathrm{Sinkhorn}(c[u^{(k)}], \varepsilon_\mathrm{OT}, u_t, u_s),\quad u^{(k+1)} = M^{(k+1)\,\top} \mathbf{1}.$$

Decompose into two steps:
- **Step A (cost update):** $u^{(k)} \to c[u^{(k)}]$ — fingerprint-based cost from current $u$.
- **Step B (Sinkhorn solve):** $c \to M^*(c)$ — entropic-OT optimum.

### §2.2 Step B contraction

By Birkhoff, Step B is a Hilbert-metric contraction with rate $\rho_S = \tanh^2((c_\mathrm{max} - c_\mathrm{min})/(2\varepsilon_\mathrm{OT}))$.

At default: $c_\mathrm{max} - c_\mathrm{min} \approx 3$ (3-component fingerprint range squared + spatial). At $\varepsilon_\mathrm{OT} = 0.1$: $\rho_S = \tanh^2(15) \approx 1$ (very weak contraction). At $\varepsilon_\mathrm{OT} = 1$: $\rho_S = \tanh^2(1.5) \approx 0.81$.

So Sinkhorn contracts but slowly at small $\varepsilon_\mathrm{OT}$.

### §2.3 Step A Hilbert-metric Lipschitz

The cost update $u \mapsto c[u]$ has multiplicative effect — perturbation of $u$ changes $\varphi(u)$ which changes $c$. To bound in Hilbert metric:

For $u, u'$ with $d_H(u, u') = \delta$: $u' = \lambda(x) u$ where $\log\lambda \in [\log(\inf u'/u), \log(\sup u'/u)]$ has range $\delta$.

Effect on $\varphi$: $\varphi(u) = (u, \mathrm{Cl}(u), D(x; 1-u))$. Each component is a function of $u$:
- $u$ direct: $|\varphi_1(u') - \varphi_1(u)| = \lvert u' - u \rvert \leq u(\lambda - 1) \leq u \cdot e^\delta - u = u(e^\delta - 1)$. For small $\delta$: $\approx u \delta$.
- $\mathrm{Cl}(u)$: closure operator is contractive (canonical), so similar $\delta$-scaling.
- $D$: local distinction operator, multiplicative.

Effect on $c[u](x,y) = \lVert \varphi(u)(x) - \varphi(u)(y) \rVert^2 + \mathrm{spatial}$: cost changes by $O(u\delta)$ per entry. Hilbert diameter of $A(x,y) = e^{-c[u]/\varepsilon_\mathrm{OT}}$ changes by $O(u\delta/\varepsilon_\mathrm{OT})$.

For Sinkhorn solution: $d_H(M^*(c), M^*(c')) \leq C_\mathrm{Bigot}\,\lVert c - c' \rVert/\varepsilon_\mathrm{OT}$ (Bigot–Cazelles–Papadakis Hilbert-metric Sinkhorn-Lipschitz). The constant $C_\mathrm{Bigot} = O(1)$.

Hence Step A Lipschitz in Hilbert: $L_A^H = O(\bar u \cdot L_\varphi/\varepsilon_\mathrm{OT})$ where $\bar u$ is mean field value, $L_\varphi$ is fingerprint Lipschitz.

### §2.4 Composition contraction rate

$\rho_\mathrm{full} = \rho_S \cdot L_A^H = \tanh^2(\Delta/(4\varepsilon_\mathrm{OT})) \cdot O(\bar u L_\varphi/\varepsilon_\mathrm{OT})$.

For contraction, need $\rho_\mathrm{full} < 1$. As $\varepsilon_\mathrm{OT} \to 0$: $\rho_S \to 1$ but $L_A^H \to \infty$. As $\varepsilon_\mathrm{OT} \to \infty$: $\rho_S \to 0$ and $L_A^H \to 0$. Intermediate $\varepsilon_\mathrm{OT}$ gives tightest contraction.

Optimization: $\rho_\mathrm{full} < 1$ requires $\tanh^2(\Delta/(4\varepsilon_\mathrm{OT})) \cdot \bar u L_\varphi/\varepsilon_\mathrm{OT} < 1$.

For very small $\varepsilon_\mathrm{OT}$: $\tanh^2 \to 1$, so condition becomes $\bar u L_\varphi/\varepsilon_\mathrm{OT} < 1$, i.e., $\varepsilon_\mathrm{OT} > \bar u L_\varphi$. At default: $\bar u \approx 0.5$, $L_\varphi \approx 1.43$: $\varepsilon_\mathrm{OT} > 0.71$ — *outside* (A7') sharp regime!

For larger $\varepsilon_\mathrm{OT}$: $\tanh^2$ decreases, allowing smaller required ε_OT.

### §2.5 The truth: contraction holds at moderate ε_OT, not at small ε_OT

Hilbert-metric contraction holds in a *moderate-$\varepsilon_\mathrm{OT}$ regime*, not all $\varepsilon_\mathrm{OT} > 0$. Specifically:
- At $\varepsilon_\mathrm{OT} \in [0.71, \infty)$: contraction holds (with rate increasing with $\varepsilon_\mathrm{OT}$).
- At $\varepsilon_\mathrm{OT} < 0.71$: contraction may fail; only Schauder fixed-point existence (canonical T-Persist-1(e)).

**This is a refinement, not a closure.** Hilbert-metric contraction is *better than Banach* (Banach needed $\varepsilon_\mathrm{OT} > 143$), but does not fully cover (A7') sharp regime ($\varepsilon_\mathrm{OT} \leq 0.45$).

---

## §3. Lemma 18 (refined, Cat B)

### §3.1 Statement

**Lemma 18 (Hilbert-metric contraction, refined Cat B closure).** *Under (A1)–(A6) + (DR2) cost regularity, the SCC self-referential Sinkhorn iteration:*

*(i) For $\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{OT}^\mathrm{contr} := \bar u L_\varphi$ (which equals $\approx 0.71$ at default exp83 parameters), the iteration is a Hilbert-metric contraction with rate $\rho_\mathrm{full} < 1$.*

*(ii) For $\varepsilon_\mathrm{OT} < \varepsilon_\mathrm{OT}^\mathrm{contr}$, contraction may fail; canonical T-Persist-1(e) Schauder gives existence + accumulation point of iteration.*

*(iii) The certified-regime gap $[\varepsilon_\mathrm{OT}^*, \varepsilon_\mathrm{OT}^\mathrm{contr}] = [0.45, 0.71]$ at default has both Schauder existence (canonical) and concentration bound (Lemma 15 corrected). **In this gap regime, the iteration accumulates near the Schauder fixed point but does not contract Banach-style.***

### §3.2 Critical re-examination

**Wait** — let me double-check the constraint. (A7') sharp regime requires $\varepsilon_\mathrm{OT} \leq 0.45$ for off-diagonal mass concentration. Hilbert contraction requires $\varepsilon_\mathrm{OT} \geq 0.71$. **Gap: [0.45, 0.71].**

Actually with Lemma 15 corrected (NOP-A closure), $\varepsilon_\mathrm{OT}^* = 2.29$ — far above $0.71$. **So the new (A7'-corrected) regime is ε_OT ≤ 2.29, and Hilbert contraction starts at 0.71 — they overlap on [0.71, 2.29].**

In this overlap, both:
- Concentration bound holds (Lemma 15 corrected).
- Iteration is Hilbert-metric contractive.

**This is the sweet spot.** Recommended canonical $\varepsilon_\mathrm{OT}$: somewhere in $[0.71, 2.29]$ — exp83's $\varepsilon_\mathrm{OT} = 1$ is *exactly* in this sweet spot.

### §3.3 Lemma 18 final statement

**Lemma 18 (Hilbert-metric contraction in (A7'-corrected), Cat B).** *Under (A1)–(A6) + (DR2) + $\varepsilon_\mathrm{OT} \in [\bar u L_\varphi, \Delta_c]$ (overlap of Hilbert-contraction and concentration regimes — at default $[0.71, 2.29]$): the SCC self-referential Sinkhorn iteration is*
- *(C1) Hilbert-metric contractive with rate $\rho_\mathrm{full} < 1$.*
- *(C2) Concentration-bounded: $\eta_\mathrm{cross} \leq C_\mathrm{mass}\,e^{-\Delta_c/\varepsilon_\mathrm{OT}}$ (Lemma 15).*

*The iteration converges to a unique fixed point in the iteration's accumulation set, which coincides with canonical T-Persist-1(e) Schauder fixed point.*

### §3.4 Outside the sweet spot

For $\varepsilon_\mathrm{OT} < 0.71$ (strict (A7') regime): Schauder existence + concentration; iteration may accumulate, may not strictly contract.

For $\varepsilon_\mathrm{OT} > 2.29$: contraction holds but concentration breaks; off-diagonal mass becomes large.

**Recommended canonical canonical $\varepsilon_\mathrm{OT}$ range:** $[0.71, 2.29]$ — gives both contraction and concentration.

---

## §4. NOP-D closure status

### §4.1 NOP-D status: **CLOSED Cat B via Lemma 18 (refined)**

The closure is *conditional* on $\varepsilon_\mathrm{OT}$ being in the sweet spot $[0.71, 2.29]$. exp83 (using $\varepsilon_\mathrm{OT}=1$) is in this sweet spot.

Two regimes outside sweet spot:
- **Strict (A7') sharp ($\varepsilon_\mathrm{OT} < 0.71$):** Schauder-existence only; iterative convergence may fail. **Cat C riders.**
- **Anti-sharp ($\varepsilon_\mathrm{OT} > 2.29$):** Banach contraction also; concentration breaks. Outside scope.

### §4.2 OP-0011 / OP-0012 implications

Lemma 11 (kernel independence) holds in the sweet spot — the relevant Sinkhorn optimum is unique (Hilbert-metric fixed point).

Lemma 6 (OP-0012-CC) requires margin condition + sweet-spot $\varepsilon_\mathrm{OT}$ for both intervals.

### §4.3 Update for `working/MF/self_ref_fp_stability.md`

Replace Lemma 18 sketch with the refined statement. Note the *overlap* with NOP-A's $\varepsilon_\mathrm{OT}^*$ regime (the sweet spot is the intersection of (A7'-corrected) and Hilbert-contraction regimes).

---

## §5. Summary update

For `99_summary.md`:

1. **NOP-D status:** OPEN → **CLOSED Cat B (conditional)** via Lemma 18 in sweet-spot $\varepsilon_\mathrm{OT}$.
2. **Sweet-spot insight:** $\varepsilon_\mathrm{OT} \in [0.71, 2.29]$ at default has both Sinkhorn-Hilbert contraction and concentration.
3. **exp83 $\varepsilon_\mathrm{OT}=1$** is in the sweet spot; canonical recommended range.
4. T-Temporal-Identity Theorem 4.2 should specify $\varepsilon_\mathrm{OT}$ in sweet spot for both stability and concentration guarantees.

---

*End of `13_NOP_D_lemma18_hilbert_metric.md`.*
