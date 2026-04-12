# T-Persist-Full: Unified Temporal Persistence --- Complete Proof Synthesis

**Date:** 2026-04-01
**Session:** Final proof synthesis
**Category:** synthesis
**Status:** complete
**Depends on:** Canonical Spec v2.0.md (T-Persist-1, T-Persist-Full, T-Persist-K-Sep/Weak), docs/03-31/proof/CORE-DEPTH-ISOPERIMETRIC.md (Gap 6), docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md (Gap 4), docs/03-31/proof/TRANSPORT-CONCENTRATION-STRENGTHENED.md (Gap 5), docs/03-31/repair/PERSIST-SYNTHESIS.md, docs/03-31/repair/PERSIST-PDE-ANALYSIS.md (interior gap), docs/03-31/theory/NEAR-BIFURCATION-LOCAL-THEORY.md, docs/03-31/theory/THREE-REGIME-SYNTHESIS.md

---

## 1. Theorem Statement

### T-Persist-Full (Unified Temporal Persistence)

Let $\hat{u}_t$ be a formation-structured minimizer of the SCC energy $\mathcal{E}$ on the volume-constrained simplex $\Sigma_m$, and let $\hat{u}_s$ be the minimizer at time $s$ with $|t - s|$ small. Under the following hypotheses:

**(WR') Fixed-point selection.** $\lambda_{\mathrm{tr}} \cdot \gamma \cdot \|\partial\varphi/\partial u\|_{\mathrm{op}} / (\varepsilon_{\mathrm{OT}} \cdot \mu_{\mathcal{F}}) < 1$ (Banach contraction for uniqueness near $\hat{u}_t$; existence guaranteed unconditionally by Schauder for any $\varepsilon_{\mathrm{OT}} > 0$). With 3-component fingerprint: $\|\partial\varphi/\partial u\|_{\mathrm{op}} \leq 1.43$ (measured), $\leq 2.83$ (analytical bound).

**(PS) Phase separation.** $\beta/\alpha > 4\lambda_2/|W''(c)|$ with $c$ in the spinodal region $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$.

**(ND) Non-degeneracy.** $\mu_{\mathcal{F}} > 0$ (generic by Sard's theorem).

**(NB) Non-bifurcation.** $\mu_{\mathcal{F}} \geq \mu_0 > 0$ where $\mu_0 \gtrsim 4.1$ (formation-conditional bound using measured Jacobian norm 1.43); conservative analytical bound $\mu_0 \gtrsim 6.7$ (using analytical Jacobian norm 2.83).

**(H2') Deep core existence.** $\mathrm{Core}^2(\hat{u}_t) \neq \emptyset$ --- **proved** for $|\mathrm{Core}| \geq 25$ and $\beta \geq 58\alpha$ (conservative) via $\Gamma$-convergence isoperimetric analysis.

**(H3) Phase separation strength.** $\beta > 11\alpha$ (for $d_{\min} = 4$; ensures positive interior gap).

**(GT) Gentle transition.** $\varepsilon_1 < \Delta_t/4$ and $2\varepsilon_2 + 2\varepsilon_1/\mu < r_{\mathrm{basin}}/2$, where $r_{\mathrm{basin}} = \sqrt{2\Delta_{\min}/\lambda_{\max}}$ with $\Delta_{\min}$ the minimum energy barrier (boundary-mode dominated).

**Then:**

1. **Self-referential OT fixed point** exists (Schauder) and is unique near $\hat{u}_t$ (Banach under WR').
2. **Deep core transport concentration:** for $\delta(x) \geq 2$, $\sum_{y \in \mathrm{Core}_s} M^*(x,y) / \sum_y M^*(x,y) \geq 1 - (n/\theta_{\mathrm{core}})\exp(-\gamma\Delta_\varphi^2/\varepsilon_{\mathrm{OT}})$.
3. **Gradient flow** from the transported field converges to $\hat{u}_s$.
4. **Persist predicate** $\geq 1 - \varepsilon_{\mathrm{persist}}$.

### Three-Tier Persistence Ladder

| Tier | Regime | $\mu_{\mathcal{F}}$ | What holds | What fails |
|------|--------|---------------------|------------|------------|
| **Full** | Away from bifurcation | $\mu \geq \mu_0 \gtrsim 4.1$ | All of (a)-(e): IFT continuation, basin containment, core inclusion, exact threshold, transport concentration | --- |
| **Deep-core remnant** | Near bifurcation | $0 < \mu < \mu_{\mathrm{bif}}$ | (a) IFT continuation, (c) shifted-threshold, deep-core pointwise bound $\hat{u}_s(x) \geq \theta - 2\varepsilon_1/\mu$ | (b) full basin containment, (d) exact threshold on whole core |
| **Bifurcation** | At bifurcation | $\mu = 0$ | Nothing; formation undergoes shape transition | All persistence guarantees |

---

## 2. Dependency Chain

```
                    T-Persist-Full
                    /     |      \
                   /      |       \
        Part (a)   Part (b,d)    Part (e)
        IFT        Basin/Gap     Transport
          |          /    \          |
          |    Gap 4       Gap 6    Gap 5
          |    Basin      Core     Transport
          |    Escape     Depth    Concentration
          |      |          |         |
          |  Prop BMD    Thm 1     Schauder
          |  boundary    isoper.   fixed-pt
          |  dominance   + Thm 2   + Fingerprint
          |      |       identity  Amplification
          |      |          |         |
          |  BASIN-      CORE-     TRANSPORT-
          |  ESCAPE-     DEPTH-    CONC-
          |  ANALYSIS    ISOPER.   STRENGTH.
          |
      Canonical Spec
      T-Persist-1(a)
      (I7, proved)

    Cross-dependencies:
    Gap 6 (core depth) --feeds--> Gap 5 (fingerprint gap requires interior gap)
    Gap 5 (concentration) --feeds--> Gap 4 (transport displacement feeds basin analysis)
    Gap 4 (basin) --requires--> (NB) non-bifurcation hypothesis
    (H2') deep core --proved via--> Gap 6 (Theorem 1, isoperimetric)
    (H3) phase separation --ensures--> positive interior gap (Gap 6 corollary)
```

**Reading order:** Gap 6 (core depth + interior gap) $\to$ Gap 5 (transport concentration) $\to$ Gap 4 (basin containment) $\to$ T-Persist-Full synthesis.

---

## 3. Part-by-Part Proof

### Part (a): Minimizer Persistence via IFT --- **Proved**

The Implicit Function Theorem guarantees a smooth family of minimizers $\hat{u}_s(\delta)$ with $\|\hat{u}_s - \hat{u}_t\| = O(\delta)$ whenever the constrained Hessian $H_\Sigma$ at $\hat{u}_t$ is non-degenerate ($\mu_{\mathcal{F}} > 0$). The energy $\mathcal{E}$ is analytic on $\Sigma_m$ (polynomial in $u$), so the IFT applies directly to the KKT system with box constraints handled via the active-set decomposition.

The perturbation from time $t$ to time $s$ enters through changes in the adjacency structure $N_s \neq N_t$ and the transport cost, producing a smooth parameter dependence. The IFT yields $\hat{u}_s = \hat{u}_t + H_\Sigma^{-1} \nabla_\delta \mathcal{E} \cdot \delta + O(\delta^2)$, giving $\|\hat{u}_s - \hat{u}_t\| \leq 2\varepsilon_1/\mu$ where $\varepsilon_1$ bounds the energy gradient perturbation.

**Status:** Proved (I7, GAP-CLOSURES.md section G2). No conditions beyond (ND).

**See:** Canonical Spec v2.0.md:946--947.

### Part (b): Gradient Flow Convergence to New Minimizer --- **Conditionally Proved**

The gradient flow at time $s$, initialized from the transported time-$t$ data, must converge to the *correct* minimizer $\hat{u}_s$ (not a different critical point). This requires the initial point to lie within the basin of attraction of $\hat{u}_s$.

**Basin radius.** The basin is characterized by the energy sublevel set $\{u : \mathcal{E}(u) < \mathcal{E}(\hat{u}) + \Delta_{\min}\}$ where $\Delta_{\min} = \min(\Delta_{\mathrm{core}}, \Delta_{\mathrm{ext}}, \Delta_{\mathrm{bdy}})$ is the minimum escape barrier across all directions. The isotropic basin radius is $r_{\mathrm{basin}} = \sqrt{2\Delta_{\min}/\lambda_{\max}}$.

Three escape barrier regimes are established:
- **Core escape:** $\Delta_{\mathrm{core}} \geq 0.0441\beta$ (energy cost of pushing a core node through the double-well spinodal; $W(0.3) = 0.0441$). Gives $\beta$-independent $r_{\mathrm{core}} \approx 0.210$ after cancellation with $\lambda_{\max} \propto \beta$.
- **Exterior escape:** $\Delta_{\mathrm{ext}} \geq 0.0441\beta$ per node (Proposition E1, proved). Exterior reorganization is not a cheap bypass.
- **Boundary escape:** $\Delta_{\mathrm{bdy}}$ is formation-shape-dependent and controls the actual basin radius. Boundary-mode dominance is analytically proved (Proposition BMD): the minimum Hessian eigenvector concentrates on boundary nodes with core fraction $O(1/\beta)$, because the Hessian diagonal at core sites is $\geq 4\alpha + 0.92\beta$ while boundary/spinodal sites can be as low as $4\alpha d_{\max} - \beta$.

**Barrier stability under gentle transition:** $\Delta_s \geq \Delta_t - 2\varepsilon_1$ (Proposition 4). Basin containment holds when $\varepsilon_1 < \Delta_t/4$ and $2\varepsilon_2 + 2\varepsilon_1/\mu < r_{\mathrm{basin}}$ (Proposition 5).

**Quantitative $\Delta_{\mathrm{bdy}}$ formula (Taylor normal form):** $\Delta_{\mathrm{bdy}} = \mu/2 \cdot (t^*)^2 + L_3/6 \cdot (t^*)^3 + L_4/24 \cdot (t^*)^4$ where $t^*$ solves the cubic $\mu + L_3 t/2 + L_4 t^2/6 = 0$. Near generic saddle-node: $\Delta_{\mathrm{bdy}} = \mu^3/(3a_3^2)$. Near pitchfork: $\Delta_{\mathrm{bdy}} = 3\mu^2/(2a_4)$. Verified $<1\%$ error at 2 of 5 test configurations. Empirical basins are 3--12$\times$ larger than the sublevel-set estimate (exp24).

**Status:** Conditionally proved under (GT) + (ND) + (NB). Fails near bifurcation when $\mu \to 0$ and $\Delta_{\mathrm{bdy}} \to 0$.

**See:** BASIN-ESCAPE-ANALYSIS.md (full proof), Canonical Spec v2.0.md:949--950.

### Part (c): Core Inclusion with Shifted Threshold --- **Proved**

The core of the transported formation $\{x : \hat{u}_s(x) \geq \theta - \epsilon\}$ contains the transported core $\{x : (\mathbf{M}_{t \to s} \hat{u}_t)(x) \geq \theta\}$ for perturbations of size $\epsilon$. This follows directly from the IFT bound $\|\hat{u}_s - \hat{u}_t\|_\infty \leq 2\varepsilon_1/\mu$ applied to transported core sites.

**Status:** Proved (I7). No conditions beyond (ND).

**See:** Canonical Spec v2.0.md:952--953.

### Part (d): Exact Threshold Preservation --- **Conditionally Proved under (H2') + (H3)**

Exact threshold preservation requires the interior gap $\gamma_{\mathrm{int}} := \min_{x \in \mathrm{Core}^2} (\hat{u}(x) - \theta_{\mathrm{core}})$ to exceed the perturbation displacement $2\varepsilon_1/\mu$.

**Interior gap bound (screened Poisson).** For core sites at graph distance $\delta(x) \geq 2$ from $\partial\mathrm{Core}$:

$$\hat{u}(x) - \theta_{\mathrm{core}} \geq (1 - \theta_{\mathrm{core}}) - C_1\exp(-c_0\,\delta(x)) - C_2/\beta$$

where $c_0 = \mathrm{arccosh}(1 + \beta/(2\alpha d_{\min}))$ is the per-hop screening decay rate and $C_2 \leq 2(1 + a_{\mathrm{cl}}/4) \cdot R$ with $R = (\lambda_{\mathrm{cl}} + \lambda_{\mathrm{sep}})/\lambda_{\mathrm{bd}}$. At default parameters: $C_2 \leq 2.875$ (conservative analytical), $C_2 \approx 0.7$ (formation-structured).

**Deep core existence (Theorem 1, CORE-DEPTH-ISOPERIMETRIC.md).** Proved for $|\mathrm{Core}| \geq 25$ and $\beta/\alpha$ sufficiently large via a 4-step argument:
1. $\Gamma$-convergence (T11): minimizers converge to characteristic functions of perimeter-minimizing sets $S^*$.
2. Edge-isoperimetric inequality (Bollobas--Leader): $|\partial_E S^*| \leq 4\sqrt{m} + O(1)$.
3. Inradius: a $k \times k$ square has interior $(k-2)^2$ sites at $\delta \geq 2$; non-empty for $m \geq 25$.
4. Transfer to finite $\beta$: Markov inequality gives $|\mathcal{C}_\beta| = 0$ for $\beta \geq \beta_1$; Euler-Lagrange bootstrap upgrades to $\hat{u}_\beta(x) \geq \theta_{\mathrm{core}}$ at deep core sites.

**Deep core dominance (Theorem 2a/2b).** $|\mathrm{Core}^2| = |\mathrm{Core}| - |\partial_V\mathrm{Core}|$ (unconditional identity). Under isoperimetric ratio $\leq C$: $|\mathrm{Core}^2|/|\mathrm{Core}| \geq 1 - 4C/\sqrt{m}$.

**Status:** Conditionally proved under (H2') + (H3). (H2') is now proved (Theorem 1). Requires $\beta > 11\alpha$ for $d_{\min} = 4$.

**See:** CORE-DEPTH-ISOPERIMETRIC.md (Theorems 1, 2a, 2b), PERSIST-PDE-ANALYSIS.md (interior gap).

### Part (e): Two-Tier Transport Concentration --- **Conditionally Proved**

Entropy-regularized OT with self-referential cost concentrates transport mass on core-to-core mappings.

**Fixed-point existence (Schauder, unconditional for $\varepsilon_{\mathrm{OT}} > 0$).** The self-referential transport map $T : \Sigma_m \to \Sigma_m$ has a fixed point. Proof chain: entropic regularization $\Rightarrow$ strict convexity of inner OT $\Rightarrow$ unique $M^*(c)$ continuous in $c$ (Berge) $\Rightarrow$ define $T_\tau$ via finite-time projected gradient flow $\Phi_\tau$ (continuous by Picard-Lindelof on compact $\Sigma_m$) $\Rightarrow$ $T_\tau : \Sigma_m \to \Sigma_m$ continuous $\Rightarrow$ Schauder gives fixed point for each $\tau$ $\Rightarrow$ compactness + Lojasiewicz gives accumulation point that is both transport fixed point and energy critical point. The finite-time flow truncation (Step 7, erratum 2026-04-01) avoids the $\mu > 0$ requirement entirely, bypassing the Maxwell-point discontinuity problem.

**Uniqueness near $\hat{u}_t$** requires (WR') for Banach contraction.

**Canonical fingerprint:** $\varphi = (u, \mathrm{Cl}(u), D(x;1-u)) \in [0,1]^3$ (3 components; resolvent $C(x,x)$ demoted --- contributes $<0.4\%$ of fingerprint gap but $\|\partial C/\partial u\| \approx 9300$ dominates the Jacobian). With 3-component fingerprint: $\|\partial\varphi/\partial u\|_{\mathrm{op}} \leq 2.83$ (analytical), $\leq 1.75$ (formation-conditional), measured $\approx 1.43$.

**Two-tier concentration result:**
- **Deep core** ($\delta \geq 2$): $\Delta_\varphi^2 \approx 2.38$. Concentration ratio $\geq 1 - n\exp(-\gamma\Delta_\varphi^2/\varepsilon_{\mathrm{OT}})$. At $\gamma/\varepsilon_{\mathrm{OT}} > 5$: core-to-core transport $> 99.99\%$.
- **Shallow core** ($\delta = 1$): $\Delta_\varphi^2 \approx 0.05$. Weak concentration only; shifted-threshold fallback (part (c)) applies.
- **Boundary thinness:** $\mathrm{Core} \setminus \mathrm{Core}^{\delta \geq 2} = \partial\mathrm{Core}$ (set-theoretic identity, no $\Gamma$-convergence needed).

**Contraction-concentration compatibility:** both regimes simultaneously satisfiable iff $\mu \cdot \Delta_\varphi^2 > (\log n + C) \cdot \lambda_{\mathrm{tr}} \cdot \|\partial\varphi/\partial u\|_{\mathrm{op}}$. Deep core ($\Delta_\varphi^2 \approx 2.38$): $\mu_0 \approx 3.4$ (at $n = 100$), satisfied at non-bifurcation parameters ($\mu \approx 70$--$130$). Boundary core ($\Delta_\varphi^2 \approx 0.05$): requires $\mu > 170$, never observed --- hence the two-tier structure.

**Status:** Conditionally proved. Fixed-point existence is unconditional (Schauder). Concentration is conditional on interior gap (Gap 6) and (NB).

**See:** TRANSPORT-CONCENTRATION-STRENGTHENED.md (full proof of all three tasks), Canonical Spec v2.0.md:958--980.

---

## 4. Quantitative Parameter Table

All values for **default parameters** ($\alpha = 1$, $\beta = 50$, $a_{\mathrm{cl}} = 3.5$, $\lambda_{\mathrm{cl}} = 1$, $\lambda_{\mathrm{sep}} = 1$, $\lambda_{\mathrm{bd}} = 1$, $\lambda_{\mathrm{tr}} = 1$, $\gamma = 1$, $\varepsilon_{\mathrm{OT}} = 0.1$, $\sigma^2 = 50$, $\theta_{\mathrm{core}} = 0.9$) on **10x10 grid** ($n = 100$, $m \approx 30$):

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Spectral gap (constrained Hessian) | $\mu_{\mathcal{F}}$ | ~14.2 (at $\beta=50$); ~74 (typical) | exp19, BASIN-ESCAPE |
| $\mu_0$ threshold (formation-conditional) | $\mu_0$ | 3.4 ($n=100$), 4.2 ($n=400$) | TRANSPORT-CONC, Eq. in section 3.4 |
| Interior gap ($\delta \geq 2$) | $\gamma_{\mathrm{int}}$ | $\geq 0.017$ ($\beta=50$); $\geq 0.057$ ($\beta=100$) | PERSIST-PDE-ANALYSIS Table section 3.1 |
| Per-hop screening decay rate | $c_0$ | $\mathrm{arccosh}(7.25) \approx 2.67$ (at $\beta=50$) | PERSIST-PDE-ANALYSIS |
| Deep core existence threshold | $\beta/\alpha$ | $\geq 58$ (conservative), $\geq 7$ (formation-structured) | CORE-DEPTH-ISOPER. Thm 1 Remark |
| Core escape barrier | $\Delta_{\mathrm{core}}$ | $\geq 0.0441 \times 50 = 2.2$ | BASIN-ESCAPE Prop. E2 |
| Exterior escape barrier | $\Delta_{\mathrm{ext}}$ | $\geq 0.0441\beta = 2.2$ per node | BASIN-ESCAPE Prop. E1 |
| Boundary escape barrier | $\Delta_{\mathrm{bdy}}$ | 0.640 ($\beta=50$, 10x10); 0.038 ($\beta=200$) | BASIN-ESCAPE Table section 2 |
| Basin radius (isotropic) | $r_{\mathrm{basin}}$ | 0.46 (10x10, $\beta=50$); 0.12 ($\beta=200$) | BASIN-ESCAPE Table section 3 |
| Basin radius ($\beta$-independent core) | $r_{\mathrm{core}}$ | $\geq 0.210$ | PERSIST-SYNTHESIS section 1.3 |
| Fingerprint gap (deep core, 3-comp) | $\Delta_\varphi^2$ | 2.38 (measured), 2.87 (theory) | TRANSPORT-CONC, exp10/20 |
| Fingerprint gap (boundary core) | $\Delta_\varphi^2$ | ~0.05 (worst case) | PERSIST-SYNTHESIS section 1.2 |
| Fingerprint Jacobian norm (measured) | $\|\partial\varphi/\partial u\|_{\mathrm{op}}$ | 1.43 | exp20, TRANSPORT-CONC section 3.3 |
| Fingerprint Jacobian norm (analytical) | $\|\partial\varphi/\partial u\|_{\mathrm{op}}$ | $\leq 2.83$ | TRANSPORT-CONC section 3.3 |
| Perturbation budget (typical $\varepsilon_1 = 1$) | $2\varepsilon_2 + 2\varepsilon_1/\mu$ | ~$0.04 + 0.027 \approx 0.07$ (at $\mu=74$) | PERSIST-SYNTHESIS section 1.3 |
| Core-to-core transport fraction | | $> 99.99\%$ at $\gamma/\varepsilon_{\mathrm{OT}} > 5$ | exp10-11 |
| Transport-based Persist value | | 0.90--0.97 | exp9-11 |
| Empirical basin / sublevel estimate ratio | | 3--12$\times$ | exp24 |
| $C_2$ (operator correction constant) | $C_2$ | $\leq 2.875$ (analytical), $\approx 0.7$ (at formation) | CORE-DEPTH-ISOPER. Prop. 3 |
| Soft mode boundary participation | | $\geq 88\%$ (4 of 5 configs) | exp19, BASIN-ESCAPE Table section 2 |

---

## 5. Near-Bifurcation Theory

### 5.1. Theorem NB-1 (Basin Collapse Near Bifurcation)

**Statement.** Near a generic saddle-node or pitchfork bifurcation on the constrained manifold $\Sigma_m$:

**(a) Barrier scaling:** $\Delta_{\mathrm{bdy}} = \mu^3/(3a_3^2)$ (saddle-node) or $\Delta_{\mathrm{bdy}} = 3\mu^2/(2a_4)$ (pitchfork), where $a_3, a_4$ are third/fourth-order Taylor coefficients of $\mathcal{E}$ along the soft mode.

**(b) Basin radius collapse:** $r_{\mathrm{basin}} = O(\mu^{3/2})$ (saddle-node) or $O(\mu)$ (pitchfork).

**(c) Basin containment failure:** occurs when $\varepsilon_1 > C' \cdot \mu^{5/2}$ (saddle-node) or $\varepsilon_1 > C'' \cdot \mu^{3}$ (pitchfork). Equivalently, $\mu < \mu_{\mathrm{bif}}(\varepsilon_1) := (\varepsilon_1/C')^{2/5}$.

**Numerical verification:**

| Grid | $\beta$ | $\mu_{\mathcal{F}}$ | $\Delta_{\mathrm{bdy}}$ | $r_{\mathrm{basin}}$ | $2\varepsilon_1/\mu$ ($\varepsilon_1=0.1$) | Contained? |
|------|---------|---------------------|-------------------------|----------------------|-------------------------------------------|-----------|
| 10x10 | 50 | 14.2 | 0.640 | 0.46 | 0.014 | YES |
| 10x10 | 200 | 1.74 | 0.038 | 0.12 | 0.115 | MARGINAL |
| 12x12 | 50 | 0.94 | 0.008 | 0.05 | 0.213 | **NO** |

**See:** NEAR-BIFURCATION-LOCAL-THEORY.md section 8.

### 5.2. Theorem NB-2 (Deep-Core Remnant Persistence)

Even when full basin containment fails, deep-core sites retain restricted persistence:

**(a) Pointwise bound:** For $x \in \mathrm{Core}_t^{\delta \geq 2}$: $\hat{u}_s(x) \geq \theta_{\mathrm{core}} - 2\varepsilon_1/\mu$. This follows from the IFT (part (a)), which does *not* require basin containment.

**(b) Exact threshold preservation:** holds on the deep core whenever $\gamma_{\mathrm{int}} > 2\varepsilon_1/\mu$.

**(c) Interior gap estimate:** $\gamma_{\mathrm{int}} \geq (1 - \theta_{\mathrm{core}}) - C_1 e^{-2c_0} - C_2/\beta$. For $\beta = 50$, $\alpha = 1$: $\gamma_{\mathrm{int}} \geq 0.017$.

The physical interpretation: instability is boundary-dominated (Proposition BMD, $\geq 88\%$ of the soft mode weight on boundary nodes), so the deep core is structurally protected even when the full basin-containment argument fails.

**See:** NEAR-BIFURCATION-LOCAL-THEORY.md section 8.3.

---

## 6. Multi-Formation Extension

### 6.1. T-Persist-K-Sep (Well-Separated) --- **Proved**

Under per-formation hypotheses (H1-K), well-separation (WS: $d_{\min}(j,k) \geq 3$ for all $j \neq k$), and spectral-repulsion compatibility (SR: $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$):

- Per-formation minimizer persistence inherited from T-Persist-1.
- Inter-formation separation preserved.
- Deep-core transport concentration preserved per-formation.
- Negligible simplex violation.

**Key mechanism:** Geometric decoupling --- core/boundary transport estimates are essentially per-formation, with coupling entering only as exponentially small correction at depth.

**Status:** Proved, conditional on per-formation T-Persist-1 + (WS) + (SR). Spectral gap via Weyl bound: $\mu_{\mathrm{joint}} \geq \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}}$.

**See:** Canonical Spec v2.0.md:935--939, THREE-REGIME-SYNTHESIS.md section 3.

### 6.2. T-Persist-K-Weak (Weakly-Interacting) --- **Conditional**

Under (H1-K), weak interaction (WI: $|O_{jk}| \leq 0.2 \cdot \min(|\mathrm{Core}_j|, |\mathrm{Core}_k|)$), spectral-repulsion compatibility (SR), and joint non-bifurcation (NB-K: $\mu_{\mathrm{joint}} > \mu_0$):

- Joint minimizer persistence.
- Deep core unaffected by coupling (overlap corrections exponentially small away from boundary).
- Boundary overlap sites have shifted-threshold fallback only.
- Post-hoc simplex correction within basin radius.

**Status:** Conditionally proved under (H1-K) + (WI) + (SR) + (NB-K) plus per-formation T-Persist-1 conditions.

**See:** Canonical Spec v2.0.md:982--985, THREE-REGIME-SYNTHESIS.md section 4.

### 6.3. T-Persist-K-Strong (Strongly-Interacting) --- **Partially Conjectural**

Two branches with different epistemic status:

- **(A) Coexistence branch:** Conditionally defensible. Under joint non-degeneracy + positive overlap-block spectral gap + positive barrier separating the $K$-formation branch from lower-$K$ competitors + gentle transition. This is a local continuation theorem.
- **(B) Merge branch:** Still conjectural. Negative overlap gap ($\mu_{\mathrm{overlap}} \leq 0$) gives instability, but full merge conclusion (gradient flow landing in $(K-1)$-formation) requires Morse-theoretic inputs not yet available.

**See:** THREE-REGIME-SYNTHESIS.md section 5, T-PERSIST-K-STRONG-MORSE-ATTEMPT.md.

---

## 7. Experimental Validation

| Experiment | What it validates | Key finding |
|-----------|-------------------|-------------|
| exp9 | Temporal transport pipeline | Transport-based Persist = 0.90--0.97 |
| exp10 | Fingerprint gap verification | $\Delta_\varphi^2(\text{deep core}) = 2.44$ (theory: 2.87) |
| exp11 | Transport concentration | Core-to-core fraction $> 99.99\%$ at $\gamma/\varepsilon_{\mathrm{OT}} > 5$ |
| exp13 | Core depth verification | Deep core non-empty at $\beta \geq 20\alpha$ for grids up to 20x20 |
| exp18 | Core depth isoperimetric | Thm 1 holds 100% for $\beta \geq 20\alpha$; iso\_ratio > 1.5 causes Thm 2b violations (15%) |
| exp19 | Saddle-point / soft mode | Soft mode boundary-dominated ($\geq 88\%$) in 4/5 configs |
| exp20 | Fingerprint Jacobian norm | Full 4-component $\|\partial\varphi/\partial u\| \approx 9271$ (resolvent); 3-component $\approx 1.43$ |
| exp21 | Gap structural analysis | Spectral gap structure at various parameters |
| exp22 | Escape barrier | Barrier verification along escape paths |
| exp23 | Barrier vs $\mu$ | $\Delta_{\mathrm{bdy}} \to 0$ as $\mu \to 0$ confirmed |
| exp24 | Basin flow test | Empirical basins 3--12$\times$ larger than sublevel-set estimate |
| exp25 | Hessian diagonal | Diagonal gap between core and boundary sites confirmed |
| exp26 | Full chain end-to-end | Parts (a)(c)(e) pass universally; (b)(d) require warm-start (basin identity) |

**Key end-to-end result (exp26):** The complete T-Persist chain is verified when using warm-start initialization (gradient flow from transported field). Multi-start may find a different minimizer, causing (b)/(d) to fail --- this is expected behavior (the basin containment hypothesis is about the specific initialization path).

---

## 8. Remaining Open Problems

### 8.1. Genuinely Open

1. **Strong-regime uniqueness/selection.** Outside the weak regime (WR'), Schauder gives existence of *some* self-referential fixed point, but not nearness to $\hat{u}_t$. The question: does the self-referential iteration converge in the strong-transport regime ($\lambda_{\mathrm{tr}}$ large, $\varepsilon_{\mathrm{OT}}$ small)?

2. **Generic non-alignment of perturbation with soft mode.** The temporal perturbation $\delta u$ comes from $N_s \neq N_t$, which generically does not align with the boundary soft mode. This is argued heuristically but not proved. A proof would upgrade (GT) from a quantitative hypothesis to a generic condition.

3. **Quantitative $\Delta_{\mathrm{bdy}}$ as function of formation geometry.** The Taylor normal form gives $\Delta_{\mathrm{bdy}} = O(\mu^k)$ with explicit constants, but the constants ($a_3$, $a_4$) are formation-dependent. A universal lower bound on $\Delta_{\mathrm{bdy}}$ in terms of computable graph invariants remains open.

### 8.2. Closed Since Original Formulation

- ~~H2 (deep core existence)~~: **Closed** by Theorem 1 (CORE-DEPTH-ISOPERIMETRIC.md). Now (H2').
- ~~Fixed-point existence~~: **Closed** by Schauder (TRANSPORT-CONCENTRATION-STRENGTHENED.md section 4).
- ~~Resolvent Jacobian blowup~~: **Resolved** by dropping resolvent from fingerprint (3-component).
- ~~WR vs. WR'~~: **Resolved** by relaxing WR to a selection condition (existence by Schauder, uniqueness by Banach).
- ~~Boundary thinness~~: **Resolved** as set-theoretic identity (TRANSPORT-CONCENTRATION-STRENGTHENED.md section 2).
- ~~Boundary-mode dominance~~: **Proved** analytically (Proposition BMD, BASIN-ESCAPE-ANALYSIS.md section 8).

---

## 9. Errata Record

### 2026-03-31

1. **Basin radius corrected.** Original claim $r \geq 0.076$ used incorrect barrier $W(0.9) - W(0.95) = 0.00584$. Corrected to $r \geq 0.210$ using correct barrier $W(0.3) = 0.0441$. (PERSIST-SYNTHESIS.md)

2. **H2 upgraded to H2'.** Original (H2) required $\delta_{\min} \geq 2$ as a hypothesis. Deep core existence now proved (Theorem 1) for $|\mathrm{Core}| \geq 25$, $\beta \geq 58\alpha$. (CORE-DEPTH-ISOPERIMETRIC.md)

3. **Fixed-point existence upgraded.** Previously conditional on weak regime ($\rho < 1$). Now proved unconditionally for $\varepsilon_{\mathrm{OT}} > 0$ via Schauder. (TRANSPORT-CONCENTRATION-STRENGTHENED.md)

4. **WR relaxed to WR'.** Original WR required Banach contraction for existence. Now: existence by Schauder (unconditional), WR' needed only for uniqueness/selection. (Canonical Spec v2.0.md)

5. **Fingerprint tightened.** Reduced from 4-component to 3-component (resolvent dropped). $\|\partial\varphi/\partial u\|_{\mathrm{op}}$: 9271 $\to$ 1.43. $\mu_0$: 7.0 $\to$ 3.4. (TRANSPORT-CONCENTRATION-STRENGTHENED.md)

### 2026-04-01

6. **Step 4 of Theorem 1 (Gamma-to-finite-beta transfer) rigorized.** Original hand-waved "Core differs by O(1) sites" from L1 convergence. Replaced with Markov inequality + Euler-Lagrange bootstrap. (CORE-DEPTH-ISOPERIMETRIC.md)

7. **Step 7 of Schauder proof replaced.** Original used IFT-based minimizer continuity (fails at $\mu = 0$). Replaced with finite-time gradient flow truncation $\Phi_\tau$, avoiding $\mu > 0$ requirement. Maxwell-point discontinuity fully bypassed. (TRANSPORT-CONCENTRATION-STRENGTHENED.md)

8. **Boundary-mode dominance analytically proved.** Proposition BMD with diagonal gap argument: core Hessian diagonal $\geq 4\alpha + 0.92\beta$, boundary can be $4\alpha d_{\max} - \beta$. Core fraction of soft eigenvector is $O(1/\beta)$. (BASIN-ESCAPE-ANALYSIS.md section 8)

9. **Theorem 2 split into 2a (unconditional identity) + 2b (conditional quantitative bound).** Experiment exp18 found 15% violations of the original quantitative claim at high $\beta$ with crystallographic faceting ($\mathrm{iso\_ratio}$ up to 2.14). (CORE-DEPTH-ISOPERIMETRIC.md)

10. **$\|\partial\varphi/\partial u\|_{\mathrm{op}}$ derivation justified.** Added explicit proof that $\|P\|_2 = 1$ (requires doubly stochastic $P$, valid on regular/grid graphs). Vertical-stack operator norm derivation added. (TRANSPORT-CONCENTRATION-STRENGTHENED.md)

11. **Quantitative $\Delta_{\mathrm{bdy}}$ formula derived.** Taylor normal form along soft mode: $\Delta_{\mathrm{bdy}} = \mu/2 \cdot (t^*)^2 + L_3/6 \cdot (t^*)^3 + L_4/24 \cdot (t^*)^4$. Verified $<1\%$ at 2/5 configurations. (BASIN-ESCAPE-ANALYSIS.md section 9)

12. **Empirical basin conservatism quantified.** Flow-based basins are 3--12$\times$ larger than sublevel-set lower bounds. (exp24, BASIN-ESCAPE-ANALYSIS.md section 9.5)
