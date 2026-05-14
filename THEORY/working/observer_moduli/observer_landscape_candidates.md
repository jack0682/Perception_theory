---
type: working/theory
created: 2026-05-07
stage: OMS-0.2
project: Observer Moduli Space of SCC
attacks: OP-OMS-002
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Observer Landscape Candidates — OMS-0.2

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **COMPUTATIONALLY TESTABLE** | **OPEN** | **REJECTED**.

---

## §1. Goal and Strategy

The observer landscape $V : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ (or its pre-quotient version $V_{\mathrm{raw}} : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$) is needed to:

1. Define attractor basins and perceptual observer types (OMS-0.2, basin stratification).
2. Define the effective degrees of freedom via Hessian/Jacobian analysis (OMS-0.4).
3. Generate a canonical discrimination between observer configurations.

**Strategy:** Rather than immediately selecting one $V$, this document develops a family of candidate functions, analyzes each against criteria, and recommends a working placeholder. The class of admissible observer landscapes (rather than a unique $V$) may be the correct OMS-1.0 object.

### Admissibility Criteria for $V$

An observer landscape $V_{\mathrm{raw}} : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ is **admissible** iff it satisfies:

| Criterion | Condition | Label |
|---|---|---|
| V1 | Gauge-invariant: $V_{\mathrm{raw}}(g \cdot \Theta) = V_{\mathrm{raw}}(\Theta)$ for all $g \in G$ | **Gauge** |
| V2 | Continuous: $V_{\mathrm{raw}} \in C^0(\mathcal{M}_{\mathrm{obs}})$ | **Cont** |
| V3 | Readout-compatible: $\nabla V_{\mathrm{raw}}(\Theta) = 0 \Rightarrow P(\Theta)$ is locally stable | **Compat** |
| V4 | Basin-generating: level sets of $V_{\mathrm{raw}}$ decompose $\mathcal{M}_{\mathrm{obs}}$ into attraction regions | **Basin** |
| V5 | Boundary-aware: $V_{\mathrm{raw}}|_{\partial \mathcal{M}_{\mathrm{obs}}} \not\equiv \mathrm{const}$ | **Bdry** |

**Definition (Admissible class).** [DEFINED]
$$\mathcal{V}_{\mathrm{adm}} = \{ V_{\mathrm{raw}} : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0} \mid V_{\mathrm{raw}} \text{ satisfies V1--V5} \}$$

OMS-1.0 may define the observer landscape as a choice of element from $\mathcal{V}_{\mathrm{adm}}$ rather than a unique function.

---

## §2. Candidate V-D: Diagnostic Loss Landscape

### §2.1 Definition

**V-D (Diagnostic loss).** [DEFINED]

Given a target diagnostic vector $d^* = (\mathrm{Bind}^*, \mathrm{Sep}^*, \mathrm{Inside}^*, \mathrm{Persist}^*) \in [0,1]^4$ and a positive weight matrix $W \succ 0$:

$$V_D(\Theta; X_t, d^*, W) = \|d_\Theta - d^*\|_W^2 = (d_\Theta - d^*)^\top W (d_\Theta - d^*)$$

Unweighted version ($W = I$):
$$V_D^0(\Theta; X_t) = \sum_{i \in \{\mathrm{Bind, Sep, In, Pers}\}} (d^i_\Theta - d^{*,i})^2$$

### §2.2 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | PROVED | $d_\Theta$ is $S_K$- and $\mathrm{Aut}_{task}$-invariant (Prop R3, readout_map_audit.md §6). |
| **Cont** (V2) | ASSUMED | Continuous in $\Theta$ iff $d_\Theta$ is continuous in $\Theta$; continuity of SCC optimizer assumed. |
| **Compat** (V3) | OPEN | Whether $\nabla V_D = 0$ implies readout stability is a strong claim; not proved. |
| **Basin** (V4) | HYPOTHESIZED | $V_D$ is a squared-norm; if $d_\Theta$ is injective, unique minimum exists. |
| **Bdry** (V5) | OPEN | Depends on behavior of $d_\Theta$ on $\partial \mathcal{M}_{\mathrm{obs}}$; boundary behavior unknown. |

**Advantages:**
- Directly computable from SCC diagnostics (no topology required).
- Smooth in $\Theta$ wherever $u^*(\Theta)$ is smooth.
- Interpretable: basin attractors are configurations that maximize observed diagnostic fidelity.
- Gauge-invariant by inspection.

**Limitations:**
- Depends on $P_{\min}$: inherits the coarseness problem (Proposition R1, readout_map_audit.md). Two observers with different formation topology but similar aggregate diagnostics map to the same $V_D$ basin.
- $d^*$ is a free parameter: the choice of target vector is external to the theory. Different choices yield different landscapes.
- $W$ is a free parameter: the relative weighting of Bind/Sep/Inside/Persist is not canonically determined.
- Does not capture topological differences.

**Classification:** $V_D \in \mathcal{V}_{\mathrm{adm}}$ provisionally for **V1, V2**; **V3, V4, V5** are open or hypothesized.

**Role in OMS:** Suitable as a **minimal computational placeholder** for computational basin-discovery experiments (OMS-0.6). Not suitable as canonical $V$ for OMS-1.0 due to coarseness and free parameters.

---

## §3. Candidate V-T: Topological Readout Loss

### §3.1 Definition

**V-T (Topological readout loss).** [DEFINED]

Let $T_\Theta$ be the topological formation signature (DEF-R2, readout_map_audit.md), and $T^*$ a target signature. Let $D_T$ be a pseudometric on the space of topological signatures $\mathcal{T}$.

$$V_T(\Theta; X_t, T^*, \alpha) = D_T(T_\Theta, T^*) + \alpha \|d_\Theta - d^*\|^2$$

where $\alpha \geq 0$ is a regularization weight.

**Pure topological version** ($\alpha = 0$):
$$V_T^0(\Theta; X_t, T^*) = D_T(T_\Theta, T^*)$$

**Choice of $D_T$.** Two options:

1. **Bottleneck distance** $d_B$: $d_B(\mathrm{Bar}_0, \mathrm{Bar}_0^*) = \inf_{\gamma} \sup_{x} \|x - \gamma(x)\|_\infty$ over bijections $\gamma$ (extended to allow matching with diagonal). Stable, well-studied.

2. **Wasserstein-1 distance on barcodes** $d_W$: $d_W(\mathrm{Bar}_0, \mathrm{Bar}_0^*) = \inf_{\gamma} \sum_x \|x - \gamma(x)\|$. More sensitive than bottleneck.

3. **Component-count difference** (coarser): $D_T^{\mathrm{coarse}} = |K^*_\Theta - K^{*}_*| + |\ell_1 - \ell_1^*|$.

### §3.2 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | PROVED | $T_\Theta$ is $G$-invariant (Prop R3, readout_map_audit.md §6). |
| **Cont** (V2) | OPEN | Bottleneck distance is stable (Stability Theorem of TDA); continuity of $V_T$ in $\Theta$ requires continuity of $\mathrm{Bar}_0(\Theta)$. Barcodes are lower-semicontinuous; $V_T$ may have jump discontinuities. |
| **Compat** (V3) | HYPOTHESIZED | Topological readout is more discriminating than diagnostic; alignment of $\nabla V_T = 0$ with readout stability is plausible. |
| **Basin** (V4) | HYPOTHESIZED | $V_T$ generates basins if $D_T$ generates a basin structure; true for smooth surrogate but unclear for discrete topological distance. |
| **Bdry** (V5) | OPEN | Depends on boundary behavior of $T_\Theta$. |

**Advantages:**
- Captures topology (number of formations, persistence structure).
- More discriminating than $V_D$ (avoids Prop R1 failure mode).
- Stability Theorem of TDA: small perturbations in $u^*$ cause small changes in $\mathrm{Bar}_0$ (in bottleneck distance).

**Limitations:**
- $T_\Theta$ is piecewise constant in $\Theta$ (for discrete graphs): $V_T^0$ has no gradient at most points. Cannot drive smooth gradient flow.
- Needs a smooth surrogate for computational use (e.g., replace hard thresholds with soft filtration).
- $T^*$ is still a free parameter.

**Classification:** $V_T$ satisfies **V1** (proved); **V2** is problematic (piecewise-constant $T$); other criteria hypothesized. Not immediately suitable for smooth gradient flow, but compatible with discrete/stochastic optimization.

**Role in OMS:** Best candidate for **topologically faithful** landscape; requires smoothed surrogate for gradient flow. Recommended for OMS validation experiments (protocol VP-2 in validation_protocols.md).

---

## §4. Candidate V-E: Expected Scene Energy Landscape

### §4.1 Definition

**V-E (Expected minimum energy).** [DEFINED]

Given a scene distribution $\mathcal{D}$ over scenes $X_t$:

$$V_E(\Theta; \mathcal{D}) = \mathbb{E}_{X \sim \mathcal{D}}\left[\min_{u \in \Sigma_m} E_\Theta(u; X)\right]$$

Single-scene version:
$$V_E^1(\Theta; X_t) = \min_{u \in \Sigma_m} E_\Theta(u; X_t) = E_\Theta(u^*(\Theta, X_t); X_t)$$

### §4.2 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | PROVED | $E_\Theta(u; X_t)$ is $G$-invariant (same argument as readout invariance). |
| **Cont** (V2) | HYPOTHESIZED | $\min_u E_\Theta(u; X)$ is continuous in $\Theta$ if the minimum is achieved and varies continuously; follows from envelope theorem under mild regularity. |
| **Compat** (V3) | OPEN | Minimum energy need not align with readout stability: a configuration with very low energy may have poor formation topology (e.g., trivial uniform field). |
| **Basin** (V4) | OPEN | $V_E^1$ may have multiple local minima in $\Theta$ if $\Theta \mapsto \min_u E_\Theta(u)$ is non-convex. Basin structure unclear. |
| **Bdry** (V5) | OPEN | Behavior at $\partial \mathcal{M}_{\mathrm{obs}}$ (e.g., $\lambda_{\mathrm{cl}} = 0$) requires analysis. |

**Advantages:**
- Directly grounded in SCC variational structure: low $V_E^1$ means the observer finds a low-energy configuration.
- No free target $d^*$ or $T^*$ parameter.
- Differentiable in $\lambda$ (by envelope theorem) when the minimizer is non-degenerate.

**Limitations:**
- Low energy $\neq$ good perception: the global energy minimum may be a trivially uniform field ($u^* \equiv m/n$) if the observer weights closure too weakly. $V_E^1$ is not monotone in perceptual quality.
- Scene distribution $\mathcal{D}$ is a free parameter.
- For single-scene $V_E^1$: minimizing over $\Theta$ directly to minimize scene energy could push the observer to degenerate configurations (e.g., $\lambda_{sep} \to 0$ reduces $E_{sep}$, allowing cheaper uniform fields).

**Compatibility warning:** $V_E$ minimization conflicts with perceptual maximization in general. An observer that minimizes the SCC scene energy may be a "lazy" observer, not a perceptually accurate one.

**Classification:** $V_E$ satisfies **V1** (proved), **V2** (hypothesized). **V3** is problematic (energy minimization $\neq$ readout stability). Not recommended as canonical $V$ without additional readout constraint.

**Role in OMS:** Useful as a **scene-energy diagnostic** — to identify degenerate observer configurations (those for which even the optimal field has high energy). Not recommended as standalone observer landscape.

---

## §5. Candidate V-P: Readout-Induced Potential

### §5.1 Definition

**V-P (Readout-induced potential).** [DEFINED]

Let $\mathcal{P}$ be the readout space with a metric or divergence $D_{\mathcal{P}}$. Fix a target perception state $P^*$:

$$V_P(\Theta; X_t, P^*, D_{\mathcal{P}}) = D_{\mathcal{P}}(P(\Theta; X_t), P^*)$$

where $P = P_{\mathrm{top}}$ (or $P_{\mathrm{full}}$).

**Generalized version.** Fix a reference observer $\Theta_0$ and measure distance to its readout:
$$V_P^{\mathrm{rel}}(\Theta; X_t, \Theta_0) = D_{\mathcal{P}}(P(\Theta), P(\Theta_0))$$

### §5.2 Choice of $D_{\mathcal{P}}$

For $P = P_{\mathrm{top}} = (d, T) \in [0,1]^4 \times \mathcal{T}$:

$$D_{\mathcal{P}}((d, T), (d^*, T^*)) = \alpha \|d - d^*\|^2 + \beta D_T(T, T^*)$$

This combines V-D and V-T into a unified readout-induced potential.

### §5.3 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | PROVED | $P(\Theta)$ is $G$-invariant; $V_P = D_{\mathcal{P}}(P(\Theta), P^*)$ is hence $G$-invariant. |
| **Cont** (V2) | ASSUMED | Continuous if $P$ and $D_{\mathcal{P}}$ are both continuous. Same caveat as V-T for topological component. |
| **Compat** (V3) | PROVED (conditional) | By construction: $V_P(\Theta) = 0$ iff $P(\Theta) = P^*$; critical points of $V_P$ align with readout stability by definition. |
| **Basin** (V4) | HYPOTHESIZED | If $P$ is injective (or nearly so), $V_P$ has unique minimum at $P^{-1}(P^*)$. Multiple basins possible if $P$ is many-to-one. |
| **Bdry** (V5) | OPEN | Boundary behavior depends on $P$ at $\partial \mathcal{M}_{\mathrm{obs}}$. |

**Advantages:**
- Directly compatible with readout by design (V3 satisfied conditionally).
- Generalizes both V-D and V-T.
- No external target except $P^*$; if $P^*$ is defined as population mean, becomes empirically grounded.

**Limitations:**
- $P^*$ (target readout) is a free parameter.
- Requires $D_{\mathcal{P}}$ to be defined on the full readout space including topological component.
- If $\alpha = 0$: reduces to $V_T$ (inherits its gradient problem).
- If $\beta = 0$: reduces to $V_D$ (inherits its coarseness problem).

**Classification:** Best balance of criteria. $V_P$ with $\alpha, \beta > 0$ satisfies **V1** (proved), **V2** (assumed), **V3** (by construction), **V4** (hypothesized), **V5** (open). Most suitable general candidate.

---

## §6. Candidate V-task: Perception-Action Task Landscape

### §6.1 Definition

**V-task (Task performance loss).** [DEFINED]

Fix a perception-action task (e.g., object manipulation, navigation, categorization) with loss function $\mathcal{L}(\pi, \Theta, X_t)$ where $\pi$ is the agent policy:

$$V_{\mathrm{task}}(\Theta) = \mathbb{E}_{\mathrm{episodes}}[\mathcal{L}(\pi^*(\Theta), \Theta, X_t)]$$

where $\pi^*(\Theta) = \arg\min_\pi \mathcal{L}(\pi, \Theta, X_t)$.

### §6.2 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | OPEN | Depends on whether task loss is permutation-invariant and automorphism-invariant. Task-specific. |
| **Cont** (V2) | OPEN | Task performance loss may be non-smooth (discrete actions, reward cliffs). |
| **Compat** (V3) | HYPOTHESIZED | If task success requires accurate perception, low task loss aligns with stable readout. |
| **Basin** (V4) | HYPOTHESIZED | Evolutionary / RL landscapes typically have multiple attractors. |
| **Bdry** (V5) | OPEN | Boundary behavior task-specific. |

**Advantages:**
- Empirically interpretable: observer configurations are ranked by task performance.
- Naturally justifies $\mathrm{Aut}_{task}$: task symmetries define which observer configurations are equivalent.
- Connects OMS to active perception, robotics, and cognitive science.

**Limitations:**
- Not purely mathematical: requires task specification.
- Different tasks give different landscapes.
- Computational cost is high (requires episode evaluation).
- Not suitable for a purely theoretical OMS.

**Classification:** Not admissible as canonical mathematical $V$ for OMS-1.0 core. Appropriate for empirical validation (OMS-0.6) and task-dependent observer type analysis. Registered as OP-OMS-014.

---

## §7. Candidate V-pop: Population Perceptual Style Potential

### §7.1 Definition

**V-pop (Population log-likelihood).** [DEFINED]

Given empirical data on observer configurations $\{\Theta^{(1)}, \ldots, \Theta^{(N)}\}$ from a population, fit a density $p_{\mathrm{pop}}(\Theta)$ (e.g., Gaussian mixture on $\mathcal{M}_{\mathrm{obs}}$):

$$V_{\mathrm{pop}}(\Theta) = -\log p_{\mathrm{pop}}(\Theta)$$

### §7.2 Analysis

| Criterion | Status | Notes |
|---|---|---|
| **Gauge** (V1) | OPEN | Requires $p_{\mathrm{pop}}$ to be $G$-invariant. |
| **Cont** (V2) | ASSUMED | Smooth density models give smooth $V_{\mathrm{pop}}$. |
| **Compat** (V3) | HYPOTHESIZED | Modes of $p_{\mathrm{pop}}$ correspond to typical observer types; if these align with readout-stable configurations, V3 is satisfied. |
| **Basin** (V4) | HYPOTHESIZED | Mixture density has multiple modes = multiple basins. |
| **Bdry** (V5) | OPEN | Depends on empirical distribution near $\partial \mathcal{M}_{\mathrm{obs}}$. |

**Advantages:**
- Empirically grounded: reflects actual human/animal perceptual style distribution.
- Basin count and location data-driven.
- Connects OMS to perceptual psychology and individual differences.

**Limitations:**
- Requires large-scale empirical data.
- Not derivable from SCC theory alone.
- Model selection ($p_{\mathrm{pop}}$ form) introduces degrees of freedom.

**Classification:** Not suitable for theoretical OMS-1.0 core. Valuable for OMS-0.6 empirical validation and OP-OMS-015.

---

## §8. Comparative Analysis

### §8.1 Comparison Table

| Candidate | V1 Gauge | V2 Cont | V3 Compat | V4 Basin | V5 Bdry | Free params | Role |
|---|---|---|---|---|---|---|---|
| V-D | PROVED | ASSUMED | OPEN | HYPO | OPEN | $d^*$, $W$ | Minimal placeholder |
| V-T | PROVED | OPEN | HYPO | HYPO | OPEN | $T^*$ | Topological option |
| V-E | PROVED | HYPO | OPEN (conflict) | OPEN | OPEN | $\mathcal{D}$ | Energy diagnostic |
| V-P | PROVED | ASSUMED | PROVED (cond.) | HYPO | OPEN | $P^*$, $D_{\mathcal{P}}$ | **Best general** |
| V-task | OPEN | OPEN | HYPO | HYPO | OPEN | Task | Empirical |
| V-pop | OPEN | ASSUMED | HYPO | HYPO | OPEN | $p_{\mathrm{pop}}$ | Empirical |

### §8.2 Recommendation

**For OMS-0.2 computational work (basin discovery):** Use $V_D^0$ with $d^* = (1,1,1,0)$ (full perception target, no temporal persistence) as the minimal placeholder. **Justification:** Directly computable from SCC output; gauge-invariant; smooth enough for gradient descent.

**For OMS-0.5 topological analysis:** Use $V_T$ with bottleneck distance and a smooth surrogate. **Justification:** Captures topology; compatible with TDA stability theory.

**For OMS-1.0 candidate definition:** Define the **class $\mathcal{V}_{\mathrm{adm}}$** of admissible observer landscapes, and prove that any $V \in \mathcal{V}_{\mathrm{adm}}$ induces a valid basin stratification. The specific element $V_P$ (readout-induced potential) is the recommended representative. **Justification:** V3 is satisfied by construction; V1 is proved; V2 and V4 are the principal open questions (OP-OMS-010).

### §8.3 OMS-1.0 Position Statement

**Position (DEFINED):** OMS-1.0 does not uniquely specify $V$. Instead, it defines:
1. The admissible class $\mathcal{V}_{\mathrm{adm}}$ (criteria V1–V5).
2. The recommended representative: $V_P$ with $D_{\mathcal{P}} = \alpha \|\cdot\|^2 + \beta D_T$.
3. The computational placeholder: $V_D^0$ with $d^* = (1,1,1,0)$.

Any $V \in \mathcal{V}_{\mathrm{adm}}$ is a valid observer landscape for OMS purposes. The specific choice is scene-distribution-dependent and observer-adaptation-context-dependent.

---

## §9. New Open Problem

### OP-OMS-010 — Existence and Regularity of Admissible Observer Landscape

**Status:** Open  
**Importance:** ★★★  **Difficulty:** H

**Statement.** Does there exist $V \in \mathcal{V}_{\mathrm{adm}}$? Specifically:

(a) *Existence:* Is $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$?

(b) *Regularity:* Does there exist $V \in \mathcal{V}_{\mathrm{adm}} \cap C^1(\mathcal{M}_{\mathrm{obs}})$? (Smooth landscape.)

(c) *Basin count:* For the recommended $V_P$, how many distinct attractors/basins does $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ have?

(d) *Uniqueness:* Is the basin stratification independent of the choice $V \in \mathcal{V}_{\mathrm{adm}}$ (up to topological equivalence)?

**Partial progress:**
- $V_D^0 \in \mathcal{V}_{\mathrm{adm}}$ up to V1, V2 (provisionally): existence is plausible.
- $C^1$ regularity: follows if $u^*(\Theta)$ is $C^1$ in $\Theta$ (unknown).

**What would resolve it.** Explicit $C^1$ proof of the SCC optimizer regularity; computation of attractor count for $V_D^0$ on $\Delta^3$.
