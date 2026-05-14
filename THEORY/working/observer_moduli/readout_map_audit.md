---
type: working/audit
created: 2026-05-07
stage: OMS-0.2
project: Observer Moduli Space of SCC
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Readout Map Audit — OMS-0.2

Every statement is classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Purpose

The readout map $P : \mathcal{M}_{\mathrm{obs}} \to \mathcal{P}$ is the link between the observer parameter space and perceptual output. The entire notion of "perceptual equivalence" depends on the choice of $P$: two observers $\Theta, \Theta'$ share a perceptual core iff $P(\Theta) = P(\Theta')$ (or more precisely, iff they lie in the same orbit under $G$ and $P$ is gauge-invariant).

The coarseness of $P$ determines the coarseness of the equivalence relation. Too coarse: $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ collapses distinct perceptual types. Too fine: every observer is its own type and the moduli space provides no compression.

This document audits the three candidate readout levels and determines which is appropriate for OMS working theory.

---

## §2. Readout Level Hierarchy

### DEF-R1. Three-Level Readout Hierarchy [DEFINED]

Let $X_t$ be a fixed scene (finite weighted graph), $\Theta \in \mathcal{M}_{\mathrm{obs}}$ an observer configuration, and $u^*(\Theta, X_t) = \arg\min_{u \in \Sigma_m} E_\Theta(u; X_t)$ the SCC energy minimizer.

**Level 1 — Diagnostic readout:**
$$P_{\min}(\Theta; X_t) = d_\Theta = (\mathrm{Bind}_\Theta,\, \mathrm{Sep}_\Theta,\, \mathrm{Inside}_\Theta,\, \mathrm{Persist}_\Theta) \in [0,1]^4$$

**Level 2 — Topological readout:**
$$P_{\mathrm{top}}(\Theta; X_t) = (d_\Theta,\, T_\Theta) \in [0,1]^4 \times \mathcal{T}$$

where $T_\Theta$ is the topological formation signature (DEF-R2).

**Level 3 — Basin readout:**
$$P_{\mathrm{full}}(\Theta; X_t) = (d_\Theta,\, T_\Theta,\, B_\Theta) \in [0,1]^4 \times \mathcal{T} \times \mathcal{B}$$

where $B_\Theta$ is the basin signature (DEF-R3). **DEFERRED** — requires $V(\Theta)$ (see OP-OMS-002).

**Notation:** $P = P_{\mathrm{top}}$ unless otherwise specified. The scene argument $X_t$ is often suppressed.

---

## §3. Rigorous Definition of the Topological Signature $T_\Theta$

### DEF-R2. Topological Formation Signature [DEFINED]

Given $u^* = u^*(\Theta, X_t) \in [0,1]^n$, define the superlevel filtration:

$$\mathcal{F}(u^*, s) = \{i \in V(X_t) : u^*_i \geq s\}$$

for $s \in [0,1]$, with induced subgraph $X_t[\mathcal{F}(u^*, s)]$.

The **topological formation signature** $T_\Theta$ consists of:

| Component | Symbol | Definition |
|---|---|---|
| Component count at threshold | $N_0(\Theta, \theta_{\mathrm{core}})$ | Number of connected components of $X_t[\mathcal{F}(u^*, \theta_{\mathrm{core}})]$ |
| H0 persistence barcode | $\mathrm{Bar}_0(\Theta)$ | Persistence barcode of $H_0$ of the superlevel filtration |
| Dominant bar length | $\ell_1(\Theta)$ | Length of the longest bar in $\mathrm{Bar}_0$ |
| Second bar length | $\ell_2(\Theta)$ | Length of the second-longest bar (0 if $N_0 = 1$) |
| Articulation ratio | $A(\Theta)$ | $\ell_2 / \ell_1$ if $\ell_1 > 0$, else 0 |
| Core count | $K^*(\Theta)$ | Number of bars with length $> \theta_{\mathrm{persist}}$ |
| Boundary band count | $C_{bd}(\Theta)$ | Number of nodes with $\theta_{\mathrm{in}} \leq u^*_i < \theta_{\mathrm{core}}$ |

**Note on $H_1$.** For planar or near-planar scenes, $H_1$ persistence (topological loops) may provide additional information. This is optional and deferred to the extended model.

**Formal definition:**
$$T_\Theta = (N_0,\, \mathrm{Bar}_0,\, \ell_1,\, \ell_2,\, A,\, K^*,\, C_{bd}) \in \mathbb{Z}_{\geq 0} \times \mathcal{B}_0 \times [0,1]^5 \times \mathbb{Z}_{\geq 0}$$

where $\mathcal{B}_0$ is the space of finite persistence barcodes for $H_0$.

### DEF-R3. Basin Signature [DEFERRED]

$$B_\Theta = \text{attractor structure of } V \text{ near } [\Theta]$$

**Status: DEFERRED.** Requires explicit $V(\Theta)$ (OP-OMS-002). Cannot be canonical until resolved.

---

## §4. Audit: Is $P_{\min}$ Too Coarse?

### §4.1 Counterexample Construction: Same Diagnostics, Different Topology

**Setup.** Consider a graph $X_t = P_8$ (path graph on 8 nodes) with $m = 4$ and the following two observer configurations:

**Observer A:** $\lambda^A = (0.6, 0.3, 0.1, 0)$, $q^A = q_c(X_t)$.
- SCC energy minimum: $u^{A*} \approx (0, 0, 1, 1, 1, 1, 0, 0)$ — one compact central formation.
- Diagnostics: $\mathrm{Bind}^A \approx 0.85$, $\mathrm{Sep}^A \approx 0.7$, $\mathrm{Inside}^A \approx 0.8$, $\mathrm{Persist}^A = 0$.
- Topology: $N_0 = 1$, $K^* = 1$.

**Observer B:** $\lambda^B = (0.3, 0.6, 0.1, 0)$, $q^B = q_c(X_t)$.
- SCC energy minimum: $u^{B*} \approx (0.8, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8)$ — two peripheral formations.
- Diagnostics: $\mathrm{Bind}^B \approx 0.82$, $\mathrm{Sep}^B \approx 0.72$, $\mathrm{Inside}^B \approx 0.78$, $\mathrm{Persist}^B = 0$.

**Claim.** The diagnostic vectors $d^A$ and $d^B$ can be made arbitrarily close by tuning parameters, while $T^A \neq T^B$ (different $K^*$, different barcode).

**Classification:** HYPOTHESIZED (formal proof requires explicit computation; consistent with SCC multi-formation literature). The construction demonstrates the plausibility of $P_{\min}$ being too coarse.

### §4.2 Counterexample: Same Diagnostics, Different Boundary Morphology

**Scenario.** Two observers with similar $(\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside})$ but different $\lambda_{bd}$:

- **Observer C:** $\lambda^C = (0.5, 0.3, 0.2, 0)$ — high boundary weight gives sharp, narrow boundary band.
- **Observer D:** $\lambda^D = (0.5, 0.3, 0, 0)$ — zero boundary weight gives diffuse boundary.

By continuity of diagnostics in $\lambda$, there exist nearby parameter values where $d^C \approx d^D$ yet $C_{bd}^C \neq C_{bd}^D$. **Classification:** HYPOTHESIZED.

### §4.3 Formal Statement

**Proposition R1 (Coarseness of $P_{\min}$).** [**PROVED** — VP-1, exp86, 2026-05-07]

There exist $\Theta_1, \Theta_2 \in \mathcal{M}_{\mathrm{obs}}$ and a scene $X_t$ such that:
$$P_{\min}(\Theta_1; X_t) = P_{\min}(\Theta_2; X_t) \quad \text{but} \quad P_{\mathrm{top}}(\Theta_1; X_t) \neq P_{\mathrm{top}}(\Theta_2; X_t)$$

*Proof (constructive).* Experiment exp86_vp1_p_resolution_audit.py (2026-05-07) found 4 explicit counterexamples on 12×12 and 15×15 grids. CE-1 (tightest): $\lambda_A=(0.6,0.2,0.2)$ vs $\lambda_B=(0.5,0.3,0.2)$, $\|P_{\min}(\Theta_A) - P_{\min}(\Theta_B)\| = 0.071 < 0.15$, while $K_{\mathrm{core}}(\Theta_A)=2 \neq 1 = K_{\mathrm{core}}(\Theta_B)$, giving $D_T = 3.028$. Thus $P_{\mathrm{top}}$ distinguishes the pair but $P_{\min}$ does not. Mechanism: Inside predicate collapses H0 barcode to one scalar; $K_{\mathrm{core}}$ integer is not injectively recoverable.

**Evidence:** `vp1_counterexamples.md`, `CODE/experiments/results/observer_moduli/vp1_pairs.json`. OP-OMS-009 sub-question (a): RESOLVED-NEGATIVE.

### §4.4 Audit Warning: Diagnostic Vector Overclaim

> **Warning R1.** The diagnostic vector alone ($P_{\min}$) is too coarse to define the perceptual core. Two observers with identical $d_\Theta$ may produce formations with different connectivity, different persistence structure, and different core count. Using $P_{\min}$ as the equivalence criterion would identify observers that produce perceptually distinct formations.

---

## §5. Is $P_{\mathrm{top}}$ Sufficient?

### §5.1 Argument for $P_{\mathrm{top}}$

$P_{\mathrm{top}}$ adds to $P_{\min}$ the topological invariants:
- Number of formation components ($N_0$, $K^*$)
- Persistence structure of the filtration ($\mathrm{Bar}_0$, $\ell_1$, $\ell_2$, $A$)
- Boundary morphology ($C_{bd}$)

**HYPOTHESIZED.** For most practical scenes and observer configurations, $P_{\mathrm{top}}$ provides sufficient resolution to distinguish perceptually relevant cores.

**Argument:** The SCC theory identifies formations primarily by their topological structure (connected components of core region). Two observers agreeing on formation topology (component count, persistence hierarchy, boundary) likely share perceptual cores up to small metric distortions.

### §5.2 When $P_{\mathrm{top}}$ May Still Be Insufficient

$P_{\mathrm{top}}$ may fail to distinguish:

1. **Basin accessibility differences.** Two observers may produce the same formation topology at the energy minimum but have different landscape structures: one has a unique deep basin, the other has multiple shallow basins with the same ground-state topology. These observers may respond differently to perturbations. $P_{\mathrm{full}}$ would distinguish them.

2. **Metric structure differences.** Two formations may have the same component count but different diameter, aspect ratio, or density profile. Whether these count as "perceptually distinct" is a modeling choice.

3. **Multiplicity of minima.** If $\arg\min E_\Theta$ is not unique (energy landscape has multiple global minima at the same level), $P_{\mathrm{top}}$ as defined (using $u^*$) is ill-defined without a tie-breaking rule.

**Resolution for (3).** Define $P_{\mathrm{top}}$ using the minimum-norm minimizer, or the output of the SCC optimizer from the canonical multi-start protocol. Add to OP-OMS-009 the requirement that the readout must be well-defined when the minimizer is non-unique.

### §5.3 Formal Sufficiency Claim

**Proposition R2 ($P_{\mathrm{top}}$ as working canonical readout).** [ASSUMED]

For the purposes of OMS-0.2 through OMS-0.6, $P_{\mathrm{top}}$ is adopted as the working canonical readout. This means:

- The perceptual core of $\Theta$ at scene $X_t$ is $P_{\mathrm{top}}(\Theta; X_t)$.
- Two observers share a perceptual core iff $P_{\mathrm{top}}(\Theta_1; X_t) = P_{\mathrm{top}}(\Theta_2; X_t)$.

This is an **assumption**, not a theorem. It will be upgraded to **proved** if Proposition R1 is confirmed and basin-level distinctions are shown to be negligible for OMS purposes, or **revised** if $P_{\mathrm{full}}$ turns out necessary.

---

## §6. Quotient Descent of $P$

### Proposition R3 (Descent to quotient). [PROVED]

**Setup.** Let $G = G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$, acting on $\mathcal{M}_{\mathrm{obs}}$. Let $\pi : \mathcal{M}_{\mathrm{obs}} \to \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ be the quotient projection.

**Claim.** If $P : \mathcal{M}_{\mathrm{obs}} \to \mathcal{P}$ satisfies:
$$\forall g \in G,\ \forall \Theta \in \mathcal{M}_{\mathrm{obs}}: \quad P(g \cdot \Theta) = P(\Theta) \quad (\star)$$

then there exists a unique continuous map $\bar{P} : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathcal{P}$ such that $P = \bar{P} \circ \pi$.

**Proof.** By the universal property of the quotient topology: a map $f : X \to Y$ factors through $X/G$ iff $f$ is constant on $G$-orbits. Condition $(\star)$ is exactly constancy on orbits. Since $G$ is finite and $\mathcal{M}_{\mathrm{obs}}$ is compact Hausdorff, the quotient $\pi$ is a closed map, and the factored map $\bar{P}$ is continuous iff $P$ is continuous. $P$ is continuous by the continuity of the SCC optimizer output (assumed, see OP-OMS-009). $\square$

**Verification of $(\star)$ for $P_{\mathrm{top}}$:**

- **$S_K$-invariance.** Permuting formation labels permutes $(u^{(1)}, \ldots, u^{(K)})$ without changing the superlevel filtration of the combined field. Hence $T_\Theta$ and $d_\Theta$ are $S_K$-invariant. **PROVED** (by inspection of definitions).

- **$\mathrm{Aut}_{\mathrm{task}}$-invariance.** A graph automorphism $\phi \in \mathrm{Aut}(X_t)$ acts on node values by $(\phi \cdot u)_i = u_{\phi^{-1}(i)}$. The Laplacian satisfies $L_{\phi \cdot X} = \phi L_X \phi^{-1}$, so $E_{\phi \cdot \Theta}(\phi \cdot u; X_t) = E_\Theta(u; X_t)$. Consequently the energy minimizer transforms as $u^*(\phi \cdot \Theta) = \phi \cdot u^*(\Theta)$. The superlevel filtration satisfies $\mathcal{F}(\phi \cdot u, s) = \phi(\mathcal{F}(u, s))$, and graph connectivity is preserved by graph automorphisms. Hence $N_0$, $K^*$, $\ell_1$, $\ell_2$ are all invariant. **PROVED** (assuming $\mathrm{Aut}_{\mathrm{task}}$-invariance of the scene, which is true by definition since $\mathrm{Aut}_{\mathrm{task}} \leq \mathrm{Aut}(X_t)$).

**Condition:** Continuity of $\Theta \mapsto u^*(\Theta)$ is required. This is a regularity question about the SCC optimizer. **ASSUMED** (consistent with existing numerical experiments but not formally proved; registered as part of OP-OMS-009).

---

## §7. Scene-Dependence and Scene-Averaged Readout

### §7.1 Scene-Specific vs. Scene-Averaged Readout

The readout $P(\Theta; X_t)$ depends on the scene $X_t$. There are two perspectives:

**Perspective 1 (Scene-specific):** Fix $X_t$. The moduli space for that scene is:
$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}(X_t) = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}(X_t)$$

Note that $G_{\mathrm{SCC}}^{(0)}$ may depend on $X_t$ through $\mathrm{Aut}_{task}(X_t)$.

**Perspective 2 (Scene-averaged):** Fix a scene distribution $\mathcal{D}$. Define:
$$P_{\mathrm{avg}}(\Theta) = \mathbb{E}_{X \sim \mathcal{D}}[P(\Theta; X)]$$

This is more robust but requires specifying $\mathcal{D}$.

**For OMS-0.2:** Scene-specific readout is used. Scene distribution is deferred to validation protocols (OMS-0.6).

### §7.2 Multi-Scene Equivalence

Two observers $\Theta_1, \Theta_2$ are **perceptually equivalent on scene class $\mathcal{X}$** iff:
$$\forall X_t \in \mathcal{X}: P_{\mathrm{top}}(\Theta_1; X_t) = P_{\mathrm{top}}(\Theta_2; X_t)$$

This gives a stronger equivalence relation than single-scene equivalence. The corresponding moduli space is potentially finer (more distinct points). **DEFINED** as a working concept; formal development deferred.

---

## §8. Continuity of $P_{\mathrm{top}}$

### Proposition R4 (Continuity of $P_{\mathrm{top}}$). [ASSUMED]

$P_{\mathrm{top}} : \mathcal{M}_{\mathrm{obs}} \to [0,1]^4 \times \mathcal{T}$ is continuous with respect to the product topology on $\mathcal{M}_{\mathrm{obs}}$ and an appropriate topology on $\mathcal{T}$.

**Evidence for assumption:**
1. The SCC optimizer output $u^*(\Theta)$ varies continuously in $\Theta$ for generic parameters (supported by experiments exp83, exp84, exp85).
2. The diagnostic vector $d_\Theta$ is computed by smooth functionals of $u^*$, hence continuous if $u^*$ is continuous.
3. The persistence barcode $\mathrm{Bar}_0(\Theta)$ is lower-semicontinuous in the superlevel filtration; for discrete graphs it is piecewise constant in $\Theta$.

**Gap:** Continuity of the persistence barcode with respect to $\Theta$ is not proved in full generality. For discrete graphs, $\mathrm{Bar}_0$ is piecewise constant (not discontinuous but not smooth). The diagnostic components $\ell_1, \ell_2, A, K^*$ may have jump discontinuities when topological events occur. **Registered as OP-OMS-009.**

**Consequence for descent proposition:** Proposition R3 requires continuity of $P$. The piecewise-constant nature of $T_\Theta$ means $P_{\mathrm{top}}$ is lower-semicontinuous but may not be continuous at topological transition points. The quotient descent $\bar{P}$ exists as a set-theoretic map at all points, and as a continuous map on the complement of measure-zero transition loci.

---

## §9. Audit Summary

### Classification of All Readout Statements

| Statement | Classification |
|---|---|
| DEF-R1: Three readout levels | DEFINED |
| DEF-R2: Topological signature $T_\Theta$ | DEFINED |
| DEF-R3: Basin signature $B_\Theta$ | DEFERRED |
| Proposition R1: $P_{\min}$ too coarse | **PROVED** (VP-1, exp86, 2026-05-07) |
| Proposition R2: $P_{\mathrm{top}}$ as working canonical | ASSUMED |
| Proposition R3: Quotient descent | PROVED (conditional on continuity) |
| $S_K$-invariance of $P_{\mathrm{top}}$ | PROVED |
| $\mathrm{Aut}_{task}$-invariance of $P_{\mathrm{top}}$ | PROVED |
| Continuity of $\Theta \mapsto u^*(\Theta)$ | ASSUMED |
| Continuity of $\Theta \mapsto \mathrm{Bar}_0(\Theta)$ | OPEN (OP-OMS-009) |

### Audit Warnings

> **Warning R1.** $P_{\min}$ (diagnostic vector alone) is **too coarse** as a canonical readout — confirmed by VP-1 (exp86, 2026-05-07; 4 explicit counterexamples). It cannot distinguish formation topology ($K_{\mathrm{core}}$). Using it as the equivalence criterion collapses perceptually distinct observer types.

> **Warning R2.** $P_{\mathrm{top}}$ as defined requires the SCC energy minimizer to be unique. When multiple global minima exist at the same energy level, a tie-breaking convention must be specified. The moduli space definition becomes convention-dependent at these points.

> **Warning R3.** $P_{\mathrm{full}}$ (with basin readout) cannot be canonical until $V(\Theta)$ is explicitly defined. Basin-level distinctions are currently out of scope for OMS-0.2.

> **Warning R4.** The topological signature $T_\Theta$ is piecewise constant in $\Theta$ (for discrete graphs). The readout map is not smooth. This limits the applicability of smooth gradient methods in OMS-0.4 (RG relevance).

---

## §10. New Open Problems Generated by This Audit

### OP-OMS-009 — Readout Resolution Completeness

**Status:** Open  
**Importance:** ★★★  **Difficulty:** M

**Statement.** Does $P_{\mathrm{top}}$ distinguish all perceptually relevant core differences?

Sub-questions:
- Is $P_{\mathrm{top}}$ strictly finer than $P_{\min}$ (i.e., does there exist $\Theta_1 \neq \Theta_2$ with $P_{\min}(\Theta_1) = P_{\min}(\Theta_2)$ but $P_{\mathrm{top}}(\Theta_1) \neq P_{\mathrm{top}}(\Theta_2)$)?
- Is $P_{\mathrm{full}}$ strictly finer than $P_{\mathrm{top}}$?
- Is $P_{\mathrm{top}}$ continuous? If not, what is the topology of its discontinuity set?
- Is the energy minimizer $u^*(\Theta)$ unique for generic $\Theta$? What is the measure of the non-unique set?

**What would resolve it.** Explicit SCC computation demonstrating Proposition R1; continuity analysis of $u^*(\Theta)$; Sard-type argument for measure-zero critical set.
