---
type: working/protocols
created: 2026-05-07
stage: OMS-0.6
project: Observer Moduli Space of SCC
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Validation Protocols — OMS-0.6

Computational and empirical protocols for validating OMS claims. Each protocol is tagged with the open problem or hypothesis it addresses.

Classification: **DEFINED** | **COMPUTATIONALLY TESTABLE** | **EMPIRICALLY TESTABLE** | **OPEN**.

---

## §1. Computational Protocol VP-1: P-Resolution Audit

**Addresses:** Proposition R1 (readout_map_audit.md), OP-OMS-009.

**Goal:** Demonstrate that $P_{\min}$ is too coarse — construct two observers with equal diagnostic vector but different topological signature.

**Procedure:**

1. **Scene setup:** Use a path graph $X_t = P_{12}$ (12 nodes, unit weights) with $m = 6$ (mass = half the graph).

2. **Observer A:** $\lambda^A = (0.6, 0.2, 0.2, 0)$, $q^A = q_c(X_t)$.
   - Run `find_formation(g, params_A)` using SCC optimizer.
   - Record $u^{A*}$, diagnostic $d^A$, component count $K^{A*}$.

3. **Observer B:** $\lambda^B = (0.2, 0.6, 0.2, 0)$, $q^B = q_c(X_t)$.
   - Run optimizer.
   - Record $u^{B*}$, diagnostic $d^B$, component count $K^{B*}$.

4. **Check:** If $\lVert d^A - d^B \rVert < \delta$ (small) but $K^{A*} \neq K^{B*}$ (different component counts), Proposition R1 is confirmed.

5. **Parameter scan:** Vary $(\lambda^A, \lambda^B)$ over a grid to find pairs minimizing $\lVert d^A - d^B \rVert$ while maximizing $\lvert K^{A*} - K^{B*} \rvert$.

**Expected result:** For convex-shaped scenes, closure-dominant observers ($\lambda_{cl}$ large) produce compact single-component formations; separation-dominant observers ($\lambda_{sep}$ large) produce dispersed multi-component formations — with similar aggregate diagnostic values due to averaging.

**SCC code entry points:**
```python
# CODE/scc/optimizer.py: find_formation(graph, params)
# CODE/scc/diagnostics.py: DiagnosticVector
# CODE/scc/graph.py: GraphState
```

**Success criterion:** $\lVert d^A - d^B \rVert < 0.05$ AND $K^{A*} \neq K^{B*}$. **COMPUTATIONALLY TESTABLE.**

---

## §2. Computational Protocol VP-2: Basin Discovery

**Addresses:** Prop BS1 (basin_stratification.md), OP-OMS-010.

**Goal:** Demonstrate multiple attractor basins in $\Delta^3$ for a specific observer landscape $V_D^0$.

**Procedure:**

1. **Fix scene $X_t$** (e.g., grid graph $G_{10 \times 10}$, $m = 50$).

2. **Define landscape:** $V_D^0(\lambda) = \lVert d_\lambda - d^* \rVert^2$ with $d^* = (1, 1, 1, 0)$, varying $\lambda \in \Delta^3$ with $q = q_c(X_t)$, $\xi = \xi_0$.

3. **Grid sampling:** Sample $N = 1000$ points $\lambda^{(i)} \sim \mathrm{Uniform}(\Delta^3)$.

4. **Gradient descent:** For each sample:
   - Initialize $\lambda^{(i)}$.
   - Run projected gradient descent on $V_D^0(\lambda)$: $\lambda \leftarrow \Pi_{\Delta^3}(\lambda - \eta \nabla_\lambda V_D^0)$.
   - Terminate at convergence (gradient norm $< 10^{-4}$).
   - Record terminal $\lambda^*$.

5. **Clustering:** Cluster the terminal points $\{\lambda^*\}$ using k-means or DBSCAN. Number of clusters $= $ estimated basin count.

6. **Report:** Number of distinct attractors, their locations in $\Delta^3$, and basin boundaries.

**SCC code entry points:**
```python
# CODE/scc/optimizer.py: find_formation (for computing d_lambda)
# New script: CODE/experiments/exp_oms_basin_discovery.py
```

**Success criterion:** More than 1 cluster with separation $> 0.1$ in $\Delta^3$. **COMPUTATIONALLY TESTABLE.**

---

## §3. Computational Protocol VP-3: Core-Weight Symmetry Test

**Addresses:** OP-OMS-001, Protocols CW-1, CW-2, CW-3 (core_weight_symmetry.md).

**Goal:** Test whether any candidate transformation $g : \Delta^3 \to \Delta^3$ is a perceptual gauge symmetry.

**Procedure A (Closure-Separation Swap):**

1. Fix $q = q_c(X_t)$, $\xi = \xi_0$.
2. Sample 100 values of $\lambda = (\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, 0)$ with $\lambda_{cl} \neq \lambda_{sep}$.
3. For each $\lambda$: compute $P_{\mathrm{top}}(\lambda)$ and $P_{\mathrm{top}}(g_1(\lambda))$ where $g_1 = (\lambda_{sep}, \lambda_{cl}, \lambda_{bd}, 0)$.
4. Compute symmetry deviation: $\Delta_1 = \lVert P_{\mathrm{top}}(\lambda) - P_{\mathrm{top}}(g_1(\lambda)) \rVert$.
5. Report: mean and max $\Delta_1$ over samples.

**Success criterion for symmetry:** $\Delta_1 < 0.01$ for all samples. (Symmetry confirmed.)
**Success criterion for asymmetry:** $\Delta_1 > 0.05$ for most samples. (Symmetry rejected.)

**Procedure B (Transport Weight Ablation):**

1. Fix static scene ($X_{t+1} = X_t$).
2. Fix $(\lambda_{cl}, \lambda_{sep}, \lambda_{bd}) = (0.4, 0.3, 0.3)$ and vary $\lambda_{tr} \in [0, 0.3]$, rescaling others proportionally.
3. Compute $P_{\mathrm{min}}(\lambda_{tr})$ for each value.
4. Report: is $P_{\mathrm{min}}$ constant in $\lambda_{tr}$ (Prop CW2)?

**Expected result A:** $\Delta_1 > 0.05$ (swap is not a symmetry, $S_4$ rejected confirmed).
**Expected result B:** $P_{\mathrm{min}}$ is constant (Prop CW2 confirmed). **COMPUTATIONALLY TESTABLE.**

---

## §4. Computational Protocol VP-4: Boundary-Face Ablation

**Addresses:** OP-OMS-012, stratified_dynamics.md §6.

**Goal:** Characterize observer behavior on each face of $\Delta^3$.

**Procedure:**

For each face $F_i$ ($i \in \{cl, sep, bd, tr\}$):

1. Set $\lambda_i = 0$, sample 50 points on the face.
2. Run SCC optimizer for each.
3. Record: diagnostic vector, component count $K^*$, formation quality metrics.
4. Compare to interior points with same normalized remaining weights.

**Specific face tests:**

- $F_{tr}$ ablation: Does SCC produce the same result as the static-only theory? (Should be yes — validates the static sub-theory.)
- $F_{cl}$ ablation: Does formation quality degrade (diffuse interior)? (Validates closure necessity.)
- $F_{sep}$ ablation: Does figure-ground separation fail? (Validates separation necessity.)
- $F_{bd}$ ablation: Do boundaries become irregular? (Validates boundary term.)

**SCC code entry points:**
```python
# Existing ablation framework in CODE/experiments/
# New: exp_oms_face_ablation.py
```

**Success criterion:** Consistent degradation on each face (each term is non-redundant). **COMPUTATIONALLY TESTABLE.**

---

## §5. Computational Protocol VP-5: Latent Symmetry Simulation

**Addresses:** OP-OMS-005, latent_symmetry.md §4.

**Goal:** Construct a toy example where a continuous compact group $H$ acts on a latent space and verify dimension reduction.

**Procedure:**

1. **Toy latent model:** Define $Z = \mathbb{R}^2$ (2D latent space). Define generator $\Gamma : Z \to \Delta^3$ by:
   $$\Gamma(z_1, z_2) = \mathrm{softmax}(z_1^2 + z_2^2,\ \lvert z_1 - z_2 \rvert,\ \lvert z_1 + z_2 \rvert,\ 0)$$
   (depends only on $r^2 = z_1^2 + z_2^2$ and $|z_1 \pm z_2|$).

2. **$SO(2)$ symmetry check:** Compute $\Gamma(R_\phi z)$ for various $\phi$. If $\Gamma(R_\phi z) = \Gamma(z)$ for all $\phi$, $SO(2)$ is a latent symmetry of $\Gamma$.

3. **Effective dimension:** Compute $P_{\mathrm{top}}(\Gamma(z))$ for $z$ on the unit circle (orbit). If constant: dimension reduced from 2 to 1 (norm only).

4. **Vary $\Gamma$:** Test other generators to find ones with and without latent symmetry.

**Success criterion:** Identify at least one generator with non-trivial latent symmetry and verify the effective dimension formula. **COMPUTATIONALLY TESTABLE (toy).**

---

## §6. Computational Protocol VP-6: RG Relevance — Jacobian Singular Spectrum

**Addresses:** OP-OMS-016, rg_relevance_flow.md §3.

**Goal:** Numerically estimate the local effective dimension $d_{\mathrm{eff}}(\Theta; \varepsilon)$ over a grid of $\Theta$ values.

**Procedure:**

1. **Grid:** Sample $N = 200$ points $\Theta^{(i)} = (\lambda^{(i)}, q^{(i)}, \xi_0)$ uniformly from $\Delta^3 \times [q_{\min}, q_{\max}]$.

2. **Numerical Jacobian:** For each $\Theta^{(i)}$, compute the Jacobian $J_P(\Theta^{(i)})$ numerically:
   $$J_P^{jk} \approx \frac{P_{\mathrm{top},j}(\Theta^{(i)} + \varepsilon_k e_k) - P_{\mathrm{top},j}(\Theta^{(i)} - \varepsilon_k e_k)}{2\varepsilon_k}$$
   where $\varepsilon_k = 10^{-3}$ (finite difference step).

3. **SVD:** Compute $\sigma_1 \geq \ldots \geq \sigma_8$ of $J_P(\Theta^{(i)})$.

4. **Effective dimension:** $d_{\mathrm{eff}}(\Theta^{(i)}; \varepsilon) = \#\{\sigma_j \geq \varepsilon\}$ for $\varepsilon \in \{0.01, 0.05, 0.1\}$.

5. **Report:** Distribution of $d_{\mathrm{eff}}$ over the sample, as a histogram.

**Expected result:** $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2, 4]$ (confirming Hypothesis RG1 or not). **COMPUTATIONALLY TESTABLE.**

**Note on $P_{\mathrm{top}}$:** For numerical differentiation, use the smooth components of $P_{\mathrm{top}}$ (diagnostic vector $d$ and continuous topological summaries $\ell_1, \ell_2, A$). The discrete component $K^*$ is piecewise constant and not differentiable; exclude from the Jacobian or use a soft approximation.

---

## §7. Empirical Protocol EP-1: Psychophysical Perceptual Style Clustering

**Addresses:** OP-OMS-015, observer_landscape_candidates.md §7.

**Goal:** Estimate the number and location of human observer types in $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$.

**Design:**

1. **Stimuli:** Present a battery of ambiguous/parametric visual scenes varying figure-ground contrast, closure, and temporal continuity.

2. **Observer task:** Participants report: (a) number of objects seen, (b) object/background judgment for each region, (c) tracking confidence across frames.

3. **Fitting:** Fit SCC parameters $\lambda$ to match each participant's responses using maximum likelihood or Bayesian inference.

4. **Analysis:** Cluster the fitted $\lambda$ values in $\Delta^3$. Report number of clusters and cluster centroids.

**Success criterion:** More than 1 well-separated cluster (> 0.1 separation in $\Delta^3$). **EMPIRICALLY TESTABLE (requires human participants).**

**Note:** This protocol tests whether human perceptual styles cluster in the OMS, validating the basin stratification hypothesis.

---

## §8. Empirical Protocol EP-2: Ambiguous Figure Dwell Times

**Addresses:** Basin boundary proximity hypothesis (basin_stratification.md §5).

**Design:**

1. **Stimuli:** Necker cube, Rubin vase, or other ambiguous figures with known bistable perception.

2. **Prediction:** Observers near a basin boundary (saddle point of $V$) should show shorter dwell times in each percept and more frequent switching. Observers deep in a basin should show longer dwell times.

3. **Fitting:** Fit $\lambda$ from pre-exposure tasks. Predict: $d_{\mathrm{eff}}$ (proximity to basin boundary) correlates with switching frequency.

**Success criterion:** Significant correlation between estimated $\lambda$-space basin proximity and dwell time. **EMPIRICALLY TESTABLE.**

---

## §9. Protocol Priority and Dependency

| Protocol | Type | Dependencies | Priority |
|---|---|---|---|
| VP-1: P-resolution | Computational | SCC code | ★★★ (resolves OP-OMS-009) |
| VP-2: Basin discovery | Computational | VP-1 + $V_D$ | ★★★ (resolves OP-OMS-010 partially) |
| VP-3: Core-weight symmetry | Computational | SCC code | ★★★ (resolves OP-OMS-001 partially) |
| VP-4: Boundary ablation | Computational | SCC code | ★★ (resolves OP-OMS-012) |
| VP-5: Latent symmetry | Computational (toy) | None | ★ (resolves OP-OMS-005 partially) |
| VP-6: RG Jacobian | Computational | SCC code + $P_{\mathrm{top}}$ | ★★ (resolves OP-OMS-016) |
| EP-1: Perceptual clustering | Empirical | VP-2 first | ★★ (resolves OP-OMS-014,015) |
| EP-2: Dwell times | Empirical | VP-2 first | ★★ (tests basin boundary proximity) |

**Recommended execution order:** VP-1 → VP-3 → VP-4 → VP-2 → VP-6 → VP-5 → EP-1 → EP-2.
