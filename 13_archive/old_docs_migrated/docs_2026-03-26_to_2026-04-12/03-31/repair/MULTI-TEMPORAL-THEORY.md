# Multi-Formation Temporal Persistence: Theory

**Date:** 2026-03-31
**Status:** Phase C — Strongly-Interacting Regime (Dichotomy Conjectured)

---

## 1. Joint Hessian Spectral Gap

**Proposition (Joint Hessian Perturbation Bound).**

The $K$-field energy $\mathcal{E}_K(u^1,\ldots,u^K) = \sum_k \mathcal{E}_{\text{self}}(u^k) + \sum_{j<k} \lambda_{\text{rep}} \langle u^j, u^k \rangle + \lambda_{\text{bar}} \sum_x \max(0, \sum_k u^k(x) - 1)^2$ has constrained Hessian on the product manifold $\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$:

$$H_{\text{joint}} = \begin{pmatrix} H_1 + R_1 & V_{12} & \cdots \\ V_{21} & H_2 + R_2 & \cdots \\ \vdots & & \ddots \end{pmatrix}$$

where:
- $H_k$ = single-formation constrained Hessian of $u^k$ on $\Sigma_{m_k}$
- Diagonal block $(k,k)$: $H_k + 2\lambda_{\text{bar}} \cdot \text{diag}(\mathbf{1}_{S>1})$ — self-energy Hessian plus barrier at active simplex-violation sites, where $S(x) = \sum_j u^j(x)$
- Off-diagonal block $(j,k)$: $V_{jk} = \lambda_{\text{rep}} \cdot I_n + 2\lambda_{\text{bar}} \cdot \text{diag}(\mathbf{1}_{S>1})$ — repulsion coupling everywhere (full identity) plus barrier at active simplex-violation sites

> **Erratum (2026-03-31):** The previous version incorrectly included a "repulsion diagonal" $R_k = \lambda_{\text{rep}} \cdot \text{diag}(\sum_{j \neq k} u^j)$ on the diagonal blocks. Since $E_{\text{rep}} = \lambda_{\text{rep}} \sum_{j<k} \langle u^j, u^k \rangle$ is bilinear in $(u^j, u^k)$, the same-field second derivative $\partial^2 E_{\text{rep}} / \partial (u^k)^2 = 0$. The cross-Hessian $\partial^2 E_{\text{rep}} / \partial u^j_x \partial u^k_y = \lambda_{\text{rep}} \delta_{xy}$, giving $V_{jk} = \lambda_{\text{rep}} \cdot I_n$ (full identity, not restricted to the overlap set). The off-diagonal coupling $V_{jk}$ was also corrected accordingly.

**Key observation:** Repulsion contributes *only* to the off-diagonal blocks (cross-coupling), not to the diagonal blocks. There is no "repulsion stabilization" of individual formations. The off-diagonal coupling $V_{jk}$ *decreases* the joint spectral gap.

By Weyl's inequality for block matrices:

$$\mu_{\text{joint}} \geq \min_k(\mu_k) - (K-1) \cdot \lambda_{\text{rep}}$$

This bound requires an explicit compatibility condition:

> **Hypothesis (SR) — Spectral-Repulsion Compatibility:** $\min_k(\mu_k) > (K-1) \cdot \lambda_{\text{rep}}$.

With typical values $\mu_k \approx 70$–$130$ and $\lambda_{\text{rep}} = 10$, $K = 2$: $\mu_{\text{joint}} \geq 60$–$120$. Condition (SR) is easily satisfied in practice.

*Status:* **Proved.**

---

## 2. Post-hoc Correction Displacement Bound

**Proposition (Correction Displacement).**

Let $(u^1_s, \ldots, u^K_s)$ be the independently transported fields, and let $(\tilde{u}^1_s, \ldots, \tilde{u}^K_s)$ be the simplex-corrected fields (via gradient descent on the barrier+repulsion energy). The correction displacement satisfies:

The correction displacement has two components:

1. **Barrier relaxation:** $\|\Delta u^k_{\text{barrier}}\|_2 \leq \|v\|_1 / K$ (volume redistribution among $K$ formations at simplex-violation sites), where $v(x) = \max(0, \sum_k u^k_s(x) - 1)$.
2. **Repulsion drift during correction:** $\|\Delta u^k_{\text{rep}}\|_2 \leq O(\lambda_{\text{rep}} / \lambda_{\text{bar}} \cdot \log(v_0 / \varepsilon))$ (repulsion pushes formations apart while barrier drives toward feasibility).

**Total:** $\|\tilde{u}^k_s - u^k_s\|_2 \leq \|v\|_1 / K + O(\lambda_{\text{rep}} / \lambda_{\text{bar}} \cdot \log(v_0 / \varepsilon))$

In the weakly-interacting regime with $\lambda_{\text{bar}} = 100$, $\lambda_{\text{rep}} = 10$, $\|v\|_1 \leq 2$: displacement $\leq 1 + 0.3 \approx 1.3$ (in $L^2$ over $n$ nodes), giving per-node displacement $\sim 1.3/\sqrt{n} \ll r_{\text{basin}} = 0.210$. Still safe.

*Status:* **Proved** (modulo explicit constant tracking).

---

## 3. T-Persist-K-Weak Theorem

**Theorem (T-Persist-K-Weak: Multi-Formation Temporal Persistence, Weakly-Interacting Regime).**

Let $(u^1_t, \ldots, u^K_t)$ be a joint minimizer of $\mathcal{E}_{K,t}$ on $\Sigma^K_M$. Suppose:

- **(H1-K)** Each formation $u^k_t$ satisfies the single-formation hypotheses (H1)–(H4) of T-Persist-1.
- **(WI)** Weakly-interacting: for all $j \neq k$, the overlap satisfies $|O_{jk}| \leq \eta \cdot \min(|\text{Core}_j|, |\text{Core}_k|)$ with $\eta < 0.2$.
- **(NB-K)** Joint non-bifurcation: $\mu_{\text{joint}} > \mu_0$ (spectral gap of the joint Hessian on $\Sigma^K_M$).
- **(SR)** Spectral-repulsion compatibility: $\min_k(\mu_k) > (K-1) \cdot \lambda_{\text{rep}}$ (ensures $\mu_{\text{joint}} > 0$ despite repulsion coupling; see §1 erratum).

Under an $\varepsilon$-gentle transition from $t$ to $s$:

**(a) Joint minimizer persistence.** $\mathcal{E}_{K,s}$ has a joint minimizer $(u^1_s,\ldots,u^K_s)$ with $\|u^k_s - u^k_t\| \leq 2\varepsilon_1/\mu_{\text{joint}}$ for each $k$.

**(b) Deep core preservation.** For each formation $k$, deep core sites ($\delta(x) \geq 2$ within $\text{Core}_k$) are unaffected by the coupling: the single-formation T-Persist-1(c,d) applies with unchanged bounds.

**(c) Boundary overlap: shifted threshold.** At overlap sites $x \in O_{jk}$, only the shifted-threshold guarantee applies: $u^k_s(x) \geq \theta_{\text{core}} - 2\varepsilon_1/\mu_{\text{joint}}$. Transport concentration is not guaranteed at these sites (consistent with the two-tier structure).

**(d) Post-hoc correction containment.** The simplex correction displacement is bounded by $C_{\text{corr}} \cdot |O_{jk}| \cdot \theta_{\text{supp}} < r_{\text{basin}} = 0.210$, ensuring corrected fields remain in the joint basin of attraction.

**(e) Per-formation transport concentration (deep core).** Deep core transport concentration is unaffected by coupling: fingerprint gap $\Delta_\varphi^2 \geq 2.87 - O(\exp(-c_0))$ at depth $\delta \geq 2$, where $c_0 = \text{arccosh}(1 + \kappa^2/d_{\min})$ and the correction accounts for the negligible cross-formation influence on the distinction operator.

*Proof sketch.* (a) IFT on the product manifold $\Sigma^K_M$ using the joint Hessian spectral gap (Proposition 1). Under (SR), $\mu_{\text{joint}} \geq \min_k(\mu_k) - (K-1)\lambda_{\text{rep}} > 0$, so the off-diagonal repulsion coupling is controlled by the single-formation spectral gaps. (b) At deep core sites of formation $k$, all other formations' fields are exponentially small by the Interior Gap Proposition applied to the complementary fields ($u^j(x) \leq 2\exp(-c_0 \cdot \delta)$ for $\delta \geq 2$, so coupling terms in the Hessian and fingerprint vanish). (c) At boundary overlap sites, the coupling is $O(1)$ but affects only $O(|\partial\text{Core}|)$ sites; the IFT displacement bound still applies but transport concentration fails (fingerprint gap $\Delta_\varphi^2 \approx 0.05$ at depth $< 2$, consistent with single-formation two-tier structure). (d) Direct from Proposition 2 and the exp14 E1 observation that simplex violations in the weakly-interacting regime are $< 0.01$. (e) The fingerprint at deep core sites depends only on the formation's own field (since other fields are negligible there), so the single-formation concentration bound of T-Persist-1(e) applies directly.

*Status:* **Conditionally proved** under (H1-K), (WI), (NB-K), (SR), plus per-formation T-Persist-1 conditions.

---

## 4. Experimental Predictions

From the theory:

1. **P1-K:** Deep core Persist is independent of the number of formations $K$ (decoupling at depth $\geq 2$).
2. **P2-K:** Simplex violation in the weakly-interacting regime is $O(|\partial\text{Core}|)$, not $O(|\text{Core}|)$.
3. **P3-K:** Joint re-optimization (Phase 2 reoptimize) should improve Persist at boundary sites but not at deep core sites.
4. **P4-K (revised):** $\mu_{\text{joint}} \approx \min_k(\mu_k) - (K-1)\lambda_{\text{rep}}$; the joint spectral gap is *reduced* by repulsion coupling but remains positive under (SR). The original P4-K ("repulsion increases effective spectral gap") was retracted — the bilinear repulsion energy has zero same-field Hessian, so there is no diagonal stabilization.

---

## 5. Connection to Phase C

The weakly-interacting theorem breaks down when:
- $|O_{jk}|$ becomes comparable to $|\text{Core}|$ (strongly-interacting → merge)
- $\mu_{\text{joint}} \to 0$ (joint bifurcation → formation split or merge)

These failure modes naturally lead to the **Dichotomy Theorem** (Phase C): in the strongly-interacting regime, either formations persist or merge, depending on the spectral structure of the joint Hessian restricted to the overlap subspace.

---

## 6. Phase C: Strongly-Interacting Regime — Dichotomy

### 6.1 The Merge Criterion

**Definition (Formation Compatibility).** Two formations $u^j, u^k$ with overlap $O_{jk}$ are *compatible* if the joint Hessian restricted to the overlap subspace has positive spectral gap:

$$\mu_{\text{overlap}}(j,k) := \lambda_{\min}\left(H_{\text{joint}}|_{O_{jk}}\right) > 0$$

They are *incompatible* (merge-prone) if $\mu_{\text{overlap}}(j,k) \leq 0$.

**Physical interpretation:** Compatible overlap means the joint energy landscape (self-energy + barrier) maintains a local minimum separating the formations even in the overlap region. Incompatible overlap means the joint energy has a descent direction that merges the two formations.

### 6.2 Dichotomy Theorem

**Theorem (T-Persist-K-Strong: Multi-Formation Dichotomy).**
Let $(u^1_t, \ldots, u^K_t)$ be a joint minimizer of $\mathcal{E}_{K,t}$ on $\Sigma^K_M$ with $|O_{jk}| > \eta \cdot \min(|\text{Core}_j|, |\text{Core}_k|)$ for some pair $(j,k)$ (strongly-interacting). Under $\varepsilon$-gentle transition:

**Case 1 (Compatible overlap, $\mu_{\text{overlap}} > 0$):** The joint minimizer $(u^1_s,\ldots,u^K_s)$ persists with $K_s = K_t$ formations. The joint re-optimization (Phase 2 reoptimize) recovers the formation structure with Persist comparable to the weakly-interacting regime.

**Case 2 (Incompatible overlap, $\mu_{\text{overlap}} \leq 0$):** The joint minimizer at time $s$ has $K_s < K_t$ active formations — the incompatible pair merges. The post-hoc correction (Phase 2 correction) destroys formation identity (Persist drops significantly), confirming that separation is energetically unfavorable.

*Proof sketch.*
Case 1: When $\mu_{\text{overlap}} > 0$, the joint Hessian is positive definite on the entire product manifold (including the overlap subspace). The IFT applies as in T-Persist-K-Weak, but the coupling perturbation is $O(|O_{jk}|)$ rather than $O(|\partial\text{Core}|)$. The stronger condition $\mu_{\text{overlap}} > 0$ absorbs this larger perturbation.

Case 2: When $\mu_{\text{overlap}} \leq 0$, the joint Hessian has a zero or negative eigenvalue in the overlap direction. This means the $K$-formation minimizer is a saddle point (or near-saddle) of the constrained energy when projected onto the merge direction $v_{\text{merge}} \propto u^j - u^k$. Under gentle perturbation, the minimizer bifurcates: the $K$-formation critical point becomes a saddle, and the gradient flow descends to a $(K{-}1)$-formation minimizer where formations $j$ and $k$ have merged.

*Status:* **Conjectured** with experimental support. The merge criterion ($\mu_{\text{overlap}} \leq 0$) is well-defined but proving that bifurcation leads to a $(K{-}1)$-formation minimizer requires Morse-theoretic analysis on $\Sigma^K_M$ (analogous to the single-formation basin escape problem).

### 6.3 Experimental Evidence

From exp14 E2 (10×10 grid, $K=2$, volume_fraction=0.5):

| $\lambda_{\text{rep}}$ | overlap | regime | correction Persist | reoptimize Persist | interpretation |
|-------|---------|--------|-------------------|-------------------|----------------|
| 0.1 | 33 | strongly | 0.47/0.42 | 0.30/0.19 | incompatible: merge is correct |
| 0.5 | 36 | strongly | 0.93/0.93 | 0.96/0.98 | compatible: coexistence works |
| 1.0 | 33 | strongly | 0.51/0.50 | 0.35/0.39 | incompatible: merge is correct |
| 5.0 | 0 | weakly | 0.66/0.65 | 0.70/0.94 | T-Persist-K-Weak applies |

The bimodal pattern (some strongly-interacting cases have high Persist, others have low Persist) is consistent with the dichotomy: it depends on whether the specific overlap configuration is compatible or incompatible.

### 6.4 Connection to Formation Birth/Death

The merge case (Case 2) is the first example of **formation death** in the temporal theory: $K_t$ formations at time $t$ become $K_s < K_t$ at time $s$. The reverse process (formation birth, $K_s > K_t$) would require a split bifurcation where a single formation's energy landscape develops a new saddle, creating two basins from one. Both processes are controlled by the spectral structure of the joint Hessian at bifurcation points.

**Open:** Formalizing birth/death as bifurcation theory on $\Sigma^K_M$ with varying $K$. This connects to the broader question of dynamic $K$ selection.
