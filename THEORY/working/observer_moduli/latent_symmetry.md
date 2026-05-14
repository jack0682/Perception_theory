---
type: working/theory
created: 2026-05-07
stage: OMS-0.3
project: Observer Moduli Space of SCC
attacks: OP-OMS-005
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Latent Continuous Symmetry — OMS-0.3

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Problem Statement

**OP-OMS-005.** Can a continuous compact Lie group $H$ act on the observer space to reduce the effective dimension of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$?

**Context from OMS-0.1:** Finite gauge groups ($S_K$, $\mathrm{Aut}_{task}$) do not reduce the dimension of $\mathfrak{M}$. Dimension reduction requires continuous compact groups.

**The question:** Does a continuous compact group naturally arise in the SCC observer framework, either:
(a) directly on $\mathcal{M}_{\mathrm{obs}}$, or
(b) through a latent generator structure?

---

## §2. Why Direct Continuous Symmetry on $\mathcal{M}_{\mathrm{obs}}$ Is Unlikely

### §2.1 Direct Action on $\Delta^3$

A continuous group $H$ acting on $\Delta^3 = \{\lambda \geq 0, \sum \lambda_i = 1\}$ would need to:
1. Map $\Delta^3$ to itself (preserve the simplex).
2. Preserve the perceptual readout $P_{\mathrm{top}}$.

**Proposition LS1 (No continuous symmetry on $\Delta^3$ without perceptual justification).** [PROVED]

Any continuous group $H$ acting on $\Delta^3$ while preserving all vertices $e_i$ (the pure-energy observers) must be trivial.

**Proof.** The vertices $e_1 = (1,0,0,0)$, $e_2 = (0,1,0,0)$, $e_3 = (0,0,1,0)$, $e_4 = (0,0,0,1)$ are fixed points of any symmetry of the simplex that respects its combinatorial structure. A continuous group action that fixes all 4 vertices of a 3-simplex must fix the entire simplex (by convexity and continuity). Hence any continuous $H$ preserving the vertex set acts trivially. $\square$

**Consequence.** If a continuous group acts on $\Delta^3$, it must permute some vertices — which requires $S_4$ elements (already rejected as gauge). Therefore no continuous compact group acts non-trivially on $\Delta^3$ while preserving the perceptual readout for all four pure-energy observer types.

**Classification of Prop LS1:** PROVED for vertex-preserving actions. For actions that do not preserve vertices (e.g., rotations of the embedded simplex): require separate analysis.

### §2.2 Direct Action on $[q_{\min}, q_{\max}]$

A continuous group acting on the $q$-interval could reduce it to a quotient. However:
- $[q_{\min}, q_{\max}] \subset \mathbb{R}$ is 1-dimensional.
- A continuous compact group acting on an interval that preserves order is trivial (only the trivial group acts freely on an interval).
- A $\mathbb{Z}_2$ reflection ($q \mapsto q_{\min} + q_{\max} - q$) is possible in principle.

**Question:** Is there $q^* \in (q_{\min}, q_{\max})$ such that $P(\Theta; X_t)$ is invariant under $q \mapsto 2q^* - q$? This would require a very specific symmetry of the phase transition condition that seems unlikely generically. **Classification:** OPEN (not yet tested).

---

## §3. Latent Generator Framework

### §3.1 Latent Observer Generator

**Definition LS1 (Latent observer generator).** [DEFINED]

A **latent observer generator** is a pair $(Z, \Gamma)$ where:
- $Z$ is a **latent space** (compact manifold or polytope), $z \in Z$.
- $\Gamma : Z \to \mathcal{M}_{\mathrm{obs}}$ is a smooth map (the generator).

The observer is parameterized by $z$: $\Theta = \Gamma(z)$.

**If $\Gamma$ is not surjective:** The image $\Gamma(Z) \subset \mathcal{M}_{\mathrm{obs}}$ is a proper submanifold — the **constrained observer manifold**.

**If $\Gamma$ is surjective and bijective:** The latent generator is just a reparameterization; no new structure.

**The interesting case:** $\Gamma$ is not injective — multiple latent points map to the same observer, defining an equivalence relation on $Z$.

### §3.2 Latent Field Generator

**Definition LS2 (Latent field generator).** [DEFINED]

A **latent field generator** is a pair $(Z, \mathcal{G})$ where:
- $Z$ is a latent space.
- $\mathcal{G}_\theta : Z \to [0,1]^n$ maps latent code $z$ to a formation field $u = \mathcal{G}_\theta(z)$.
- $\theta \in \mathcal{M}_{\mathrm{obs}}$ are the model parameters.

The SCC energy is evaluated at $u = \mathcal{G}_\theta(z)$:
$$E_\Theta(\mathcal{G}_\theta(z); X_t)$$

**Role:** This framework generalizes the SCC optimizer: instead of optimizing $u$ over $\Sigma_m$, one optimizes over $z \in Z$ through $\mathcal{G}_\theta$.

**Latent symmetry in this framework:** A group $H$ acts on $Z$ and satisfies:
$$P(\mathcal{G}_\theta(h \cdot z); X_t) = P(\mathcal{G}_\theta(z); X_t) \quad \forall h \in H, z \in Z$$

---

## §4. Compact Lie Group Latent Symmetry

### §4.1 General Framework

**Definition LS3 (Latent gauge symmetry).** [DEFINED]

Let $H$ be a compact Lie group acting on $Z$. $H$ is a **latent gauge symmetry** for generator $(Z, \Gamma)$ and readout $P$ if:

$$P(\Gamma(h \cdot z); X_t) = P(\Gamma(z); X_t) \quad \forall h \in H, z \in Z, X_t$$

**Effective dimension formula.** If $H$ acts freely on $Z$:
$$\dim(Z/H) = \dim Z - \dim H$$

If the action is not free (has stabilizers $H_z \neq \{e\}$ for some $z$):
$$\dim(Z/H) = \dim Z - \dim H \quad (\text{at generic points})$$

with orbifold singularities at fixed points.

### §4.2 Candidate Latent Groups

**Candidate H1: $O(r)$ — orthogonal rotations on $\mathbb{R}^r$**

Arises when the latent space $Z = \mathbb{R}^r$ and the generator $\Gamma$ is equivariant:
$$\Gamma(R z) = \Gamma(z) \quad \forall R \in O(r)$$

Example: $\Gamma(z) = f(\|z\|^2)$ (depends only on norm). Then $O(r)$ is a latent gauge symmetry. Effective dimension reduction: $r \to 1$ (only the norm matters).

**Realistic in SCC?** HYPOTHESIZED if the field generator $\mathcal{G}_\theta$ depends only on the norm of a latent feature vector. Not justified by current SCC structure.

**Candidate H2: $SO(2)$ on formation orientation**

If formations have a rotational degree of freedom and the readout $P_{\mathrm{top}}$ is rotation-invariant:
$$P_{\mathrm{top}}(R_\phi \cdot u; X_t) = P_{\mathrm{top}}(u; X_t) \quad \forall \phi$$

then $SO(2)$ is a latent symmetry. This requires the graph $X_t$ and the energy to be rotationally symmetric.

**Status:** HYPOTHESIZED for symmetric scenes (e.g., circular graph). For generic scenes, $X_t$ breaks rotational symmetry. Hence $SO(2)$ is a symmetry only in special scene classes. **Scene-conditional latent symmetry**, not a universal gauge.

**Candidate H3: $T^r$ (torus symmetry)**

Arises in factorized latent spaces: $Z = Z_1 \times \cdots \times Z_r$ with independent $U(1)$ phases on each factor. **Status:** OPEN — no obvious connection to SCC structure.

**Candidate H4: Finite reflection groups**

$\mathbb{Z}_2^r$ acting on $\mathbb{R}^r$ by sign flips. Could arise in the SCC context through symmetry of the double-well potential $W(u) = u^2(1-u)^2$ (which is symmetric under $u \mapsto 1-u$, a $\mathbb{Z}_2$ action).

**Proposition LS2 ($\mathbb{Z}_2$ field symmetry).** [HYPOTHESIZED]

The double-well potential satisfies $W(u) = W(1-u)$. If the energy functional $E_\Theta(u; X_t)$ satisfies $E_\Theta(1-u; X_t) = E_\Theta(u; X_t)$ under complementation $u \mapsto \mathbf{1} - u$, then $\mathbb{Z}_2$ is a field-level symmetry.

**Analysis:** $E_{\mathrm{cl}}(1-u)$ is the closure energy of the complement. $E_{\mathrm{sep}}(1-u) = E_{\mathrm{sep}}(u)$ iff the distinction measure is complement-symmetric. This requires scene-specific analysis. **Status:** OPEN. Complement symmetry is NOT generically true (the background is not the same as the foreground in SCC).

---

## §5. Classification of Latent Symmetry in OMS

### §5.1 Core vs. Generator Extension

**Proposition LS3 (Latent symmetry belongs to OMS-Gen, not OMS core).** [ASSUMED]

Continuous compact latent gauge symmetries, if they exist, belong to a generator-level extension (OMS-Gen) rather than the OMS-0.x core theory. They require:
1. A specific latent generator model $(Z, \Gamma)$ or $(Z, \mathcal{G}_\theta)$.
2. A specific group action on $Z$.
3. Verification that the action preserves $P$ universally.

None of these are determined by the current SCC axioms alone. The OMS core theory should not presuppose a latent symmetry group.

**Justification:**
- The SCC energy functional is defined directly on $\Sigma_m$ (no latent space).
- The observer parameters $\Theta = (q, \lambda, \xi)$ are global scalars, not latent codes.
- The gauge group $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{task}$ is determined by the scene and formation structure, not by a latent generator.

### §5.2 When Latent Symmetry Would Arise

Latent continuous symmetry would arise in:
1. **Neural generator models:** If a neural network $\mathcal{G}_\theta : Z \to \Sigma_m$ is used as a generative model for formations, with a group-equivariant architecture.
2. **Functional data analysis:** If the observer parameter space is modeled as a functional space with continuous symmetry.
3. **Population models:** If the scene distribution $\mathcal{D}$ has a symmetry group $H$ that the observer exploits.

These are all Level-3 SCC extensions (or higher), not part of the static Level-2 OMS framework.

### §5.3 Effective Dimension Without Continuous Gauge

Without continuous latent symmetry, the effective dimension reduction in $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ comes from:

1. Normalization constraints: $\sum \lambda_i = 1$ → $-1$ DOF from raw space.
2. Criticality hypothesis (if applied): $-1$ DOF.
3. RG relevance (irrelevant directions): $-k$ DOF where $k$ is scene/task-specific (see rg_relevance_flow.md).
4. **No continuous gauge reduction** (unless latent symmetry is established).

**PROVED:** Effective dimension without latent symmetry = $8 - 1 (criticality) - k (relevance)$ where $k$ is unknown (OP-OMS-005, OP-OMS-016).

---

## §6. Summary

| Candidate | Type | Status | Dimension reduction |
|---|---|---|---|
| $O(r)$ on latent $\mathbb{R}^r$ | Latent gauge | HYPOTHESIZED | $r \to 1$ (if free) |
| $SO(2)$ on orientation | Scene-conditional | HYPOTHESIZED | $-1$ DOF on symmetric scenes |
| $T^r$ torus | Latent gauge | OPEN | $-r$ DOF if free |
| $\mathbb{Z}_2$ complement | Field-level | OPEN | $-1$ DOF if exact |
| $S_4$ weight permutation | Direct on $\Delta^3$ | REJECTED (Prop CW1) | 0 |
| $O(r)$ vertex-preserving | Direct on $\Delta^3$ | REJECTED (Prop LS1) | 0 |

**Conservative conclusion (ASSUMED):**

> No continuous compact latent gauge symmetry is included in OMS-0.x core. The OMS-Gen extension framework is reserved for generator-level models. The effective dimension of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is currently $\leq 8 - 1 = 7$ (under criticality), with further reduction possible through RG relevance but not through gauge.

**OP-OMS-005** remains OPEN. The question of continuous compact symmetry in SCC observer space requires either:
(a) A specific generative model with verified latent symmetry, or
(b) A proof that no such symmetry exists for $P_{\mathrm{top}}$.
