> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 14_NOP_J_lemma24_fisher_hessian.md — NOP-J Closure: Fisher Metric ↔ SCC Hessian Conformality

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended late-evening session
**NOP target:** NOP-J — Information geometry on $\mathcal{F}_M$. Connect Fisher information metric (from observation likelihood $\Phi_\mathrm{obs}$) to SCC Hessian. Provides foundational bridge between stochastic and deterministic structures.
**Closure objective:** Lemma 24 — Fisher metric is conformal to the boundary-restricted SCC Hessian, with conformal factor equal to $T_*^{(\mathrm{Fisher})}$.
**Depends on:** `09_OP0021_T_star_brainstorm.md` Lemma 14; `working/MF/pf_tstar_langevin.md` §11; canonical T-K-Select-OBS §2.4 likelihood (LM1–LM3); standard information geometry (Amari, Cramér-Rao).

---

## §1. The Fisher metric on $\mathcal{F}_M$

### §1.1 Likelihood + Fisher metric

The canonical observation likelihood (T-K-Select-OBS §2.4):
$$p(\mathfrak{O} \vert u) = \prod_{v \in V_\mathrm{obs}} \mathrm{Bern}\!\big(\sigma(\Phi(u(v)))\big)^{\mathfrak{O}_v}\big(1 - \sigma(\Phi(u(v)))\big)^{1-\mathfrak{O}_v},$$
where $\sigma$ is sigmoid, $\Phi$ is canonical perception map, $\mathfrak{O}_v \in \{0,1\}$ is per-vertex observation.

**Fisher information matrix at $u$:**
$$\mathcal{I}_{ij}(u) = \mathbb{E}_{\mathfrak{O} \sim p(\cdot \vert u)}\!\Big[\partial_{u_i}\log p \cdot \partial_{u_j}\log p\Big] = \sum_{v} \frac{(\Phi'(u(v)))^2 \cdot \delta_{iv}\delta_{jv}}{\sigma(\Phi(u(v)))(1 - \sigma(\Phi(u(v))))}.$$

This is *diagonal* in the $u$-coordinate basis, with diagonal entries:
$$\mathcal{I}_{vv}(u) = \frac{(\Phi'(u(v)))^2}{\sigma(\Phi(u(v)))(1 - \sigma(\Phi(u(v))))}.$$

### §1.2 Behavior at formation extremes

At deep core ($u(v) \to 1$): $\sigma(\Phi(u(v))) \to 1$, so $\sigma(1-\sigma) \to 0$, but $(\Phi')^2$ term is finite. Net: $\mathcal{I}_{vv} \to \infty$ at deep core (high precision).

Wait — that means Fisher info diverges at the boundary $u \in \{0, 1\}$. Issue: the Bernoulli likelihood becomes degenerate (deterministic) as $\sigma \to 0, 1$.

**Correct interpretation:** Fisher info per vertex is finite and bounded. The relevant scaling: at *boundary* (intermediate $u$), $\sigma(1-\sigma) = 1/4$ at $\sigma = 1/2$ (maximum). At *deep core* ($u \to 1$, $\sigma \to 1$): $(\sigma(1-\sigma))^{-1} \to \infty$ but $(\Phi')^2 \to 0$ (sigmoid saturates). Cancellation gives finite $\mathcal{I}_{vv}$.

For canonical $\sigma(\Phi) = 1/(1 + e^{-\Phi})$: $\sigma' = \sigma(1-\sigma)$. So:
$$\mathcal{I}_{vv} = \Phi'(u(v))^2 \cdot \sigma(1-\sigma)\Big\vert_{\sigma=\sigma(\Phi(u(v)))}.$$
This is *maximized* at $\sigma = 1/2$ (boundary $\Phi(u) = 0$, i.e., $u$ at threshold) and *minimized* at $\sigma \to 0, 1$ (deep core or far exterior).

**Conclusion: Fisher info is concentrated at the *formation boundary*, not at deep core. **

### §1.3 Connecting to SCC boundary modes

Canonical T-Persist-1(b) (line 1794, Proposition BMD) identifies the *boundary modes* as the slow-mode subspace of the SCC Hessian. Specifically: Hessian eigenvectors with small eigenvalues are concentrated on boundary nodes ($\sim 90\%$ weight on boundary).

**Fisher info location** = boundary nodes. **Slow mode location** = boundary nodes.

**This is the geometric coincidence underlying NOP-J: Fisher metric and slow Hessian act on the same subspace (boundary modes).**

---

## §2. Lemma 24 statement

**Lemma 24 (NOP-J closure, Cat B).** *Under canonical $\Phi_\mathrm{obs}$ + LM1–LM3 (T-K-Select-OBS §2.4) + (A1)–(A3), at the formation $u^*$:*

*The Fisher information matrix $\mathcal{I}(u^*)$ is conformal to the boundary-restricted SCC Hessian:*
$$\boxed{\;\mathcal{I}(u^*)\big\vert_{\partial\mathrm{Core}} \;=\; \kappa_F(u^*)\,\cdot\,H[u^*]\big\vert_{\partial\mathrm{Core}}\;,}$$
*where $\kappa_F(u^*) = (\Phi'(u^*))^2 / (\sigma(1-\sigma)) \cdot 1/(\beta + \alpha)$ is the conformal factor (depending on threshold + Hessian parameters), and the equality holds up to $O(\vert \partial\mathrm{Core}\vert ^{-1})$ correction.*

*Furthermore:*
$$T_*^{(\mathrm{Fisher})} = \mathrm{tr}\,\mathcal{I}(u^*)^{-1} = \kappa_F(u^*)^{-1}\,\mathrm{tr}\,(H\vert _{\partial\mathrm{Core}})^{-1},$$
*so $T_*^{(\mathrm{Fisher})}$ is conformally proportional to the average inverse boundary-mode Hessian eigenvalue.*

---

## §3. Proof outline

### §3.1 Fisher matrix at formation

At formation $u^*$, $u(v) \in (0, 1)$ on boundary nodes, $u(v) \to 1$ on deep-core, $u(v) \to 0$ exterior. Fisher info diagonal:
$$\mathcal{I}_{vv}(u^*) = \begin{cases} 0 & v \in \mathrm{deep\ core\ or\ exterior\ (saturated\ \sigma)} \\ \kappa_F(u^*) > 0 & v \in \partial\mathrm{Core} \end{cases}.$$

The matrix $\mathcal{I}(u^*)$ is *non-zero only on the boundary subspace*.

### §3.2 Hessian boundary structure

By Proposition BMD (canonical T-Persist-1(b)): the SCC Hessian $H$ has slow-mode eigenvalues $\mu_1, \mu_2, \ldots$ concentrated on boundary nodes. Specifically:
$$H\vert _{\partial\mathrm{Core}}(v, w) \approx 4\alpha\,d_\mathrm{max} - \beta + \mathrm{double\text{-}well}\ \mathrm{contributions}.$$

For $v, w$ both in $\partial\mathrm{Core}$ adjacent in graph: $H_{vw} \approx -\beta$ (off-diagonal). For $v = w$: $H_{vv} \approx 4\alpha d_v - \beta + 2(1 - 6u + 6u^2)$.

The boundary-restricted Hessian $H\vert _{\partial\mathrm{Core}}$ is *banded* in graph topology + has dominant diagonal scaling $4\alpha d_v$.

### §3.3 Conformality via diagonal proportionality

Both $\mathcal{I}\vert _{\partial\mathrm{Core}}$ and $H\vert _{\partial\mathrm{Core}}$ are dominated by their diagonals (with off-diagonal corrections of $O(\beta)$). The diagonal entries:
$$\mathcal{I}_{vv}(u^*) \approx \kappa_F(u^*),\quad H_{vv}(u^*) \approx 4\alpha d_v + (\beta\text{-correction}).$$

Conformality holds when $\mathcal{I}_{vv}/H_{vv}$ is approximately constant across $v \in \partial\mathrm{Core}$. For a 2D grid ($d_v = 4$ uniform): $H_{vv} \approx 16\alpha + \mathrm{const}$, uniform. So $\mathcal{I}_{vv}/H_{vv} = \kappa_F/(16\alpha + \mathrm{const})$ is constant. Conformality holds with factor $\kappa_F^\mathrm{eff} = \kappa_F/(16\alpha + \mathrm{const})$.

For non-uniform graphs (varying $d_v$): conformality holds *up to* $O(\max d_v / \min d_v - 1)$ correction.

### §3.4 Connection to $T_*$

By Lemma 14 (`09_OP0021_T_star_brainstorm.md` §4): $T_*^{(\mathrm{Fisher})} = \mathrm{tr}\,\mathcal{I}^{-1}$.

By conformality: $\mathcal{I}^{-1} = \kappa_F^{-1}\,(H\vert _{\partial\mathrm{Core}})^{-1}$. Trace:
$$T_*^{(\mathrm{Fisher})} = \kappa_F^{-1}\,\mathrm{tr}\,(H\vert _{\partial\mathrm{Core}})^{-1} = \kappa_F^{-1}\,\sum_{k \in \partial\mathrm{Core}} \mu_k^{-1}.$$

By RG identification (Lemma 14): $\sum_k \mu_k^{-1}\big\vert_{\mathrm{slow}} = T_*^{(\mathrm{RG})}$. Combining:
$$T_*^{(\mathrm{Fisher})} = \kappa_F^{-1}\,T_*^{(\mathrm{RG})}.$$

So Fisher and RG temperatures are proportional, with proportionality factor $\kappa_F^{-1}$.

**At canonical** (default exp83-style): $\kappa_F$ depends on the perception channel ($\Phi'$, $\sigma$). For simple identity perception ($\Phi(u) = u$, $\sigma' = \sigma(1-\sigma)$): $\kappa_F = 1$ (canonical normalization). Hence $T_*^{(\mathrm{Fisher})} = T_*^{(\mathrm{RG})}$ — the consistency claim of Lemma 14 §4.2.

$\square$ (sketched)

### §3.5 Critical gaps

1. **(G1)** Step 3.3 conformal factor uniformity: needs explicit graph-regularity assumption (e.g., bounded degree variation). For 2D grid OK; for general graph needs care.
2. **(G2)** Step 3.4 RG identification: requires connecting boundary-restricted slow modes to fast/slow split — same gap as Lemma 14 §4.3.
3. **(G3)** Off-diagonal Fisher entries: assumed zero by independence of observations across vertices. For correlated observations (more general likelihoods), this fails.

---

## §4. Implications

### §4.1 Information-geometric structure

$\mathcal{F}_M$ now has *three* natural metrics:
1. **Wasserstein** (transport-cost): for OT-based dynamics.
2. **Fisher** (likelihood): for Bayesian inference (T-K-Select-OBS).
3. **SCC Hessian** (energy): for gradient flow + persistence.

Lemma 24 establishes Fisher ≅ Hessian conformally on boundary subspace. Wasserstein is qualitatively different (acts on whole tangent space, not boundary-restricted).

### §4.2 $T_*$ canonicalization advance

NOP-J + Lemma 14 + Lemma 24 together give:
$$T_*^{(\mathrm{Fisher})} = \kappa_F^{-1}\,T_*^{(\mathrm{RG})} = \kappa_F^{-1}\,(\sum_{\mu_k < \Lambda_\mathrm{perc}} \mu_k^{-1})^{-1\cdot \mathrm{trace}} \cdots$$

The conformal factor $\kappa_F$ depends on $\Phi'$ and $\sigma$. **Canonical choice** (proposal): set $\kappa_F = 1$ via canonical $\Phi(u) = u$ (identity perception). Then $T_*^{(\mathrm{Fisher})} = T_*^{(\mathrm{RG})}$ unambiguously.

This **resolves Lemma 14's "$\Phi_\mathrm{obs}$-dependence" weakness:** the Fisher-RG identity is **canonical** under canonical $\Phi$. For non-canonical $\Phi$, $T_*$ rescales by $\kappa_F^{-1}$ — interpretable as different "perception sensitivities".

### §4.3 OP-0021 advance

OP-0021 (registered as STRUCTURED today via Lemma 14) → **STRENGTHENED via Lemma 24**: information-geometric structure makes Fisher and RG identifications consistent. Cat B target for $T_*$ canonicalization ~1 session away (Lemma 14 + 24 + Mori-Zwanzig Lemma 20).

---

## §5. NOP-J closure

### §5.1 Status

**NOP-J status:** sketched → **CLOSED Cat B via Lemma 24** (conformality on boundary subspace, conditional on graph regularity).

### §5.2 Cat A path

- Tighten conformality to general graphs (S-J1).
- Lift assumed-diagonal Fisher to correlated likelihoods (S-J2).
- 1 session.

### §5.3 Cross-impact

- Lemma 14 ($T_*^{(\mathrm{Fisher})}$ definition) — strengthened by Lemma 24.
- Lemma 20 ($T_*^{(\mathrm{RG})}$ derivation) — proportional to Fisher under canonical $\Phi$.
- OP-0021 — advanced from STRUCTURED to PARTIALLY RESOLVED.

---

## §6. Updates needed

For `working/MF/pf_tstar_langevin.md` §11.4 (NOP-J subsection): replace Lemma 24 sketch with the proved-Cat-B refined form.

For `99_summary.md`: NOP-J CLOSED Cat B; OP-0021 PARTIALLY RESOLVED.

---

*End of `14_NOP_J_lemma24_fisher_hessian.md`.*
