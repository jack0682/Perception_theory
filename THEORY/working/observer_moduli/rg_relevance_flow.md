---
type: working/theory
created: 2026-05-07
stage: OMS-0.4
project: Observer Moduli Space of SCC
attacks: OP-OMS-005, OP-OMS-016
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# RG-Style Relevance / Irrelevance Flow — OMS-0.4

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **COMPUTATIONALLY TESTABLE** | **OPEN** | **REJECTED**.

---

## §1. Mandatory Distinction

> **Three separate mechanisms reduce the effective observer dimension. They must not be conflated.**

| Mechanism | What it does | Dimension reduction |
|---|---|---|
| **Normalization constraints** | $\sum \lambda_i = 1$, $\alpha + \beta = 1$ | Removes redundant DOF from the raw parameter count |
| **Gauge identification** | $G = S_K \times \mathrm{Aut}_{task}$ quotienting | Removes representation redundancy (finite gauge: no dimension reduction) |
| **RG relevance** | Irrelevant directions have $D_\Theta P \approx 0$ | Reduces effective perceptual dimension (not formal manifold dimension) |

Only the third mechanism is the subject of this document.

---

## §2. Parameter Response Map

### §2.1 Definition

**Definition RG1 (Parameter response map).** [DEFINED]

For a fixed scene $X_t$ and readout $P = P_{\mathrm{top}}$, define:

$$R(\Theta; X_t) = P_{\mathrm{top}}(\Theta; X_t) \in \mathcal{P}$$

This is a map from observer space to perceptual output space.

**Scene-averaged version:**
$$R_{\mathcal{D}}(\Theta) = \mathbb{E}_{X \sim \mathcal{D}}[P_{\mathrm{top}}(\Theta; X)]$$

For the analysis below, we use the scene-averaged version to avoid scene-specific artifacts.

### §2.2 Jacobian of the Response Map

**Definition RG2 (Perceptual Jacobian).** [DEFINED]

At a point $\Theta \in \mathrm{int}(\mathcal{M}_{\mathrm{obs}})$ where $R_{\mathcal{D}}$ is differentiable:

$$J_P(\Theta) = D_\Theta R_{\mathcal{D}} : T_\Theta \mathcal{M}_{\mathrm{obs}} \to T_{R_{\mathcal{D}}(\Theta)} \mathcal{P}$$

This is a linear map from the tangent space of $\mathcal{M}_{\mathrm{obs}}$ (dimension 8) to the tangent space of $\mathcal{P}$.

**Matrix form.** In local coordinates $(\Theta^1, \ldots, \Theta^8)$ on $\mathcal{M}_{\mathrm{obs}}$ and coordinates $(P^1, \ldots, P^{d_{\mathcal{P}}})$ on $\mathcal{P}$:

$$[J_P(\Theta)]_{ij} = \frac{\partial R_{\mathcal{D}}^i}{\partial \Theta^j}(\Theta)$$

**Dimension:** $J_P(\Theta) \in \mathbb{R}^{d_{\mathcal{P}} \times 8}$.

**Note on differentiability:** $R_{\mathcal{D}}$ may not be differentiable everywhere (topological components of $T_\Theta$ are piecewise constant). The Jacobian is defined only on the complement of the topological transition locus. **Classification:** DEFINED generically; OPEN at topological transition points.

---

## §3. Relevant and Irrelevant Directions

### §3.1 Singular Value Decomposition of $J_P$

The SVD of $J_P(\Theta)$ gives:
$$J_P(\Theta) = U \Sigma V^\top$$

where:
- $V = [v_1, \ldots, v_8]$ are the right singular vectors in $T_\Theta \mathcal{M}_{\mathrm{obs}}$
- $\Sigma = \mathrm{diag}(\sigma_1 \geq \sigma_2 \geq \ldots \geq \sigma_8 \geq 0)$ are singular values
- $U$ are left singular vectors in $\mathcal{P}$

**Definition RG3 (Relevant direction).** [DEFINED]

A tangent direction $v \in T_\Theta \mathcal{M}_{\mathrm{obs}}$ is **$\varepsilon$-relevant** if:
$$\lVert J_P(\Theta) v \rVert \geq \varepsilon \lVert v \rVert$$

Equivalently: $v$ has significant singular value components above $\varepsilon$.

**Definition RG4 (Irrelevant direction).** [DEFINED]

A tangent direction $v$ is **$\varepsilon$-irrelevant** if:
$$\lVert J_P(\Theta) v \rVert < \varepsilon \lVert v \rVert$$

These are directions in $\mathcal{M}_{\mathrm{obs}}$ along which moving the observer causes negligible change in perceptual output.

### §3.2 Local Effective Dimension

**Definition RG5 (Local effective dimension).** [DEFINED]

$$d_{\mathrm{eff}}(\Theta; \varepsilon) = \#\{i : \sigma_i(J_P(\Theta)) \geq \varepsilon\}$$

This counts the number of singular values of $J_P(\Theta)$ above threshold $\varepsilon$.

**Properties:**
- $0 \leq d_{\mathrm{eff}}(\Theta; \varepsilon) \leq \min(8, d_{\mathcal{P}})$
- $d_{\mathrm{eff}}$ is monotone decreasing in $\varepsilon$
- $d_{\mathrm{eff}}(\Theta; 0) = \mathrm{rank}(J_P(\Theta)) \leq 8$
- $d_{\mathrm{eff}}$ depends on $\Theta$: relevance is local

**Classification:** DEFINED. Computationally estimable: COMPUTATIONALLY TESTABLE via numerical differentiation of $P_{\mathrm{top}}$ w.r.t. $\Theta$.

### §3.3 Global Effective Dimension

**Definition RG6 (Global effective dimension).** [DEFINED]

$$d_{\mathrm{eff}}^{\mathrm{glob}}(\varepsilon) = \max_{\Theta \in \mathcal{M}_{\mathrm{obs}}} d_{\mathrm{eff}}(\Theta; \varepsilon)$$

or alternatively the typical value:

$$d_{\mathrm{eff}}^{\mathrm{typical}}(\varepsilon) = \mathrm{median}_{\Theta \sim \mu} \, d_{\mathrm{eff}}(\Theta; \varepsilon)$$

where $\mu$ is the uniform measure on $\mathcal{M}_{\mathrm{obs}}$.

**Estimation:** Compute $J_P(\Theta)$ at a grid of sample points in $\Delta^3$ and report the distribution of $d_{\mathrm{eff}}(\Theta; \varepsilon)$. See validation_protocols.md Protocol VP-6.

---

## §4. RG-Analogy: Relevance Flow

### §4.1 Informal Analogy

In the renormalization group (RG) for physical systems:
- Relevant operators: grow under coarse-graining.
- Irrelevant operators: shrink under coarse-graining; the system flows to a fixed point where they vanish.

**OMS analogy:**
- **Relevant observer directions:** Changing the observer along these directions significantly changes perceptual output.
- **Irrelevant observer directions:** Moving the observer along these directions has negligible effect; the observer "flows" (under adaptation) to a fixed point where these DOF are locked.

**Classification of analogy:** HYPOTHESIZED as a conceptual framework. The analogy is suggestive but the SCC theory does not (yet) provide an explicit coarse-graining operation.

### §4.2 Formal RG-Like Flow

**Definition RG7 (Irrelevance projection flow).** [DEFINED]

Given $J_P(\Theta)$ with SVD, define the irrelevant subspace at $\Theta$:

$$\mathcal{I}(\Theta; \varepsilon) = \mathrm{span}\{v_i : \sigma_i < \varepsilon\}$$

The **irrelevance projection flow** is:

$$\frac{d\Theta}{ds} = -\Pi_{\mathcal{I}(\Theta;\varepsilon)} v(\Theta)$$

for some drift vector $v(\Theta)$ (e.g., Brownian noise, observer adaptation pressure). This flow drives the observer along irrelevant directions toward "natural" values, effectively freezing those degrees of freedom.

**Classification:** DEFINED formally. Whether this flow converges to a lower-dimensional attractor: OPEN (OP-OMS-016).

### §4.3 Coarse-Graining Map

**Definition RG8 (Observer coarse-graining map).** [DEFINED]

$$\mathcal{C}_\varepsilon : \mathcal{M}_{\mathrm{obs}} \to \mathcal{M}_{\mathrm{eff}}(\varepsilon)$$

maps each observer $\Theta$ to its image under projection onto the relevant subspace:

$$\mathcal{C}_\varepsilon(\Theta) = \Pi_{\mathcal{R}(\Theta;\varepsilon)} \Theta$$

where $\mathcal{R}(\Theta; \varepsilon) = \ker(\mathcal{I}(\Theta; \varepsilon))$ is the relevant subspace.

**The effective observer space:**
$$\mathcal{M}_{\mathrm{eff}}(\varepsilon) = \mathrm{image}(\mathcal{C}_\varepsilon) \subset \mathcal{M}_{\mathrm{obs}}$$

**Dimension:**
$$\dim \mathcal{M}_{\mathrm{eff}}(\varepsilon) = d_{\mathrm{eff}}^{\mathrm{glob}}(\varepsilon)$$

**Classification:** DEFINED. Whether $\mathcal{M}_{\mathrm{eff}}$ is a submanifold, a stratified space, or an irregular set: OPEN.

---

## §5. Hessian-Based Relevance (With $V$)

If an admissible observer landscape $V \in \mathcal{V}_{\mathrm{adm}}$ is available, an alternative definition of relevant/irrelevant directions uses the Hessian of $V$:

**Definition RG9 (Hessian-based relevance).** [DEFINED]

At a critical point $\Theta^* \in \mathcal{M}_{\mathrm{obs}}$ with $\nabla V(\Theta^*) = 0$:

$$\mathrm{Hess}[V]_{\Theta^*} = D^2_\Theta V \in \mathbb{R}^{8 \times 8}$$

**Relevant directions:** eigenvectors of $\mathrm{Hess}[V]_{\Theta^*}$ with eigenvalue $|\mu_i| \geq \varepsilon_H$.

**Irrelevant directions:** eigenvectors with $|\mu_i| < \varepsilon_H$ (flat directions of $V$).

**Relation to Jacobian-based relevance:** In general, Jacobian-based relevance (via $J_P$) and Hessian-based relevance (via $\mathrm{Hess}[V]$) need not agree. They agree if $V = D_{\mathcal{P}}(P(\Theta), P^*)^2$ (readout-induced potential), in which case $\mathrm{Hess}[V] \approx J_P^\top J_P$ near $P^{-1}(P^*)$.

**Classification:** DEFINED. Requires $V$ to be available. Currently OPEN (OP-OMS-002 not resolved).

---

## §6. Expected Values from SCC Physics

### §6.1 Predicted Relevant Directions

Based on the SCC phase transition theory (T8), the most relevant observer directions are:

1. **$q = \beta/\alpha$ direction (1 DOF):** The phase transition condition $q > q_c(X_t)$ is the primary driver of formation/dissolution. Near $q_c$, the system is maximally sensitive to $q$. $\Rightarrow$ $q$ is a **relevant** direction for $P_{\min}$ (Bind diagnostic).

2. **$\lambda_{\mathrm{cl}} - \lambda_{\mathrm{sep}}$ axis (1 DOF):** Closure vs. separation balance determines the number of formations. $\Rightarrow$ HYPOTHESIZED as relevant for $K^*$ (core count).

3. **$\lambda_{\mathrm{bd}}$ direction (1 DOF):** Boundary morphology determines the boundary band width $C_{bd}$. $\Rightarrow$ HYPOTHESIZED as relevant for $P_{\mathrm{top}}$ boundary components.

### §6.2 Predicted Irrelevant Directions

Based on SCC physics:

1. **$\lambda_{\mathrm{tr}}$ on static scenes:** Transport weight is irrelevant for static scene readout (Prop CW2). $d_{\mathrm{eff}}$ decreases by 1 for static scenes.

2. **$a_{\mathrm{cl}}$ near the interior of spinodal zone:** The closure gain $a_{\mathrm{cl}}$ primarily sets the speed of convergence, not the formation topology. May be approximately irrelevant for $P_{\mathrm{top}}$. **HYPOTHESIZED.**

3. **$\theta_{\mathrm{core}}, \theta_{\mathrm{in}}$ near typical $u^*$ values:** These thresholds convert the continuous field $u^*$ into discrete topological counts. Near their typical operational values, small changes may not change $K^*$ or $C_{bd}$. **HYPOTHESIZED.**

### §6.3 Effective DOF Estimate

**Hypothesis RG1 (Effective DOF estimate).** [HYPOTHESIZED]

For typical scenes and observer configurations in the interior of $\mathcal{M}_{\mathrm{obs}}$:
$$d_{\mathrm{eff}}^{\mathrm{typical}}(\varepsilon) \approx 2\text{--}4$$

with the following breakdown:
- 1 DOF from $q$ (or 0 if criticality imposed)
- 1 DOF from $\lambda_{\mathrm{cl}} - \lambda_{\mathrm{sep}}$ balance
- 1 DOF from $\lambda_{\mathrm{bd}}$
- 0--1 DOF from remaining $\xi$ parameters

**Classification:** HYPOTHESIZED. Requires numerical validation via Protocol VP-6.

---

## §7. Mandatory Warnings

> **Warning RG1.** The RG relevance program is currently a **conceptual framework and program**, not a proved theorem. The Jacobian $J_P(\Theta)$ can be computed numerically but no rigorous proof of its spectral properties has been given.

> **Warning RG2.** "Effective dimension" $d_{\mathrm{eff}}(\Theta; \varepsilon)$ is $\varepsilon$-dependent. It does not give a canonical dimension for $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$; it gives a threshold-dependent approximation of the number of perceptually active degrees of freedom.

> **Warning RG3.** The estimate of 1--3 effective DOF from initial analysis is a **hypothesis**, not a proved theorem. It must be upgraded to COMPUTATIONALLY TESTABLE (Protocol VP-6) before being cited as a result.

---

## §8. Open Problems

**OP-OMS-016 — Computational Estimation of $d_{\mathrm{eff}}$** [OPEN]

Compute $J_P(\Theta)$ numerically over a grid on $\Delta^3 \times [q_{\min}, q_{\max}]$ and determine the distribution of $d_{\mathrm{eff}}(\Theta; \varepsilon)$.

**What would resolve it.** Implementation of numerical differentiation of $P_{\mathrm{top}}(\Theta; X_t)$ with respect to $\Theta$ using the existing SCC code. This is COMPUTATIONALLY TESTABLE.

**OP-OMS-005 (updated).** The question of continuous compact gauge symmetry reducing formal dimension is separate from RG relevance reducing effective perceptual dimension. Both are unresolved, but through distinct mechanisms.
