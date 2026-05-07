---
type: working/canonical-candidate
created: 2026-05-07
updated: 2026-05-08
stage: OMS-1.1
project: Observer Moduli Space of SCC
version: OMS-1.1
status: COMPUTATIONALLY GROUNDED CANONICAL CANDIDATE — G_cw={e} computationally supported; V existence hypothesized; Prop BS1 computationally confirmed; formally blocked pending OP-OMS-018
---

# SCC Observer Moduli Space — OMS-1.1 Candidate

**Version:** OMS-1.1 (2026-05-08)

> **Status declaration:** This document is a **Computationally Grounded Canonical Candidate** — all core claims are either proved or computationally supported. $G_{\mathrm{cw}}=\{e\}$ is COMPUTATIONALLY SUPPORTED (VP-3); $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ is HYPOTHESIZED (VP-2); Prop BS1 (≥2 observer types) is COMPUTATIONALLY CONFIRMED (VP-4). ~~OP-OMS-009 RESOLVED 2026-05-07 (VP-1).~~ Formally blocked from full canonical promotion pending OP-OMS-018 (optimizer regularity, $C^1$ of $u^*(\lambda)$). See §19 (Canonical Promotion Checklist).

Every statement is classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Abstract

The SCC Observer Moduli Space formalizes the notion of *perceptual equivalence* between observers. Two observers share a perceptual core when they produce the same topological formation signature on a given scene, up to gauge redundancy (formation label permutation and task-spatial symmetry).

The central mathematical object is:
$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} \,/\, G_{\mathrm{SCC}}^{(0)}$$

where $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$ is a compact 8-dimensional manifold-with-corners, $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$ is a finite gauge group, and the quotient has the structure of a compact Hausdorff connected orbifold.

Key results:
1. $\mathfrak{M}$ is compact, Hausdorff, and connected. [PROVED]
2. Finite gauge does not reduce dimension. [PROVED]
3. $\mathfrak{M}$ can support multiple perceptual observer types despite connectedness. [PROVED]
4. Perceptual types are basin strata of an admissible observer landscape. [DEFINED + PROVED (conditional)]
5. Effective DOF is 2–4, below the formal dimension 8. [HYPOTHESIZED]
6. No continuous compact gauge symmetry is established. [ASSUMED (conservative)]

---

## §2. Motivation

The SCC theory answers: *어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?* The answer depends on observer parameters: the phase-transition ratio $q = \beta/\alpha$, energy weights $\lambda$, and auxiliary hyperparameters $\xi$. This generates the second-level question:

> **When two observers see the same scene, under what conditions do they share a perceptual core?**

The Observer Moduli Space is the space of distinct observer configurations, up to perceptual equivalence. It provides:
- A mathematical classification of observer types.
- A topology on the space of perceptual styles.
- A framework for analyzing observer adaptation dynamics.
- The correct setting for studying perceptual universality classes.

---

## §3. Observer Parameter Space

### DEF-1. Observer Parameter Vector [DEFINED]

$$\Theta = (q, \lambda, \xi) \in \mathcal{M}_{\mathrm{obs}}$$

- $q = \beta/\alpha \in [q_{\min}, q_{\max}]$: phase-transition ratio (boundary-separation balance)
- $\lambda = (\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr}) \in \Delta^3$: energy weights (4-simplex, $\sum \lambda_i = 1$)
- $\xi = (a_{cl}, \varepsilon_{OT}, \theta_{core}, \theta_{in}) \in B_\xi$: auxiliary hyperparameters

**Scene-determined (NOT observer parameters):** $m$ (mass), $\lambda_2$ (Fiedler eigenvalue), $c = m/n$, $n$ (graph size), $b_D = 0$ (fixed for analyticity).

### DEF-2. Observer Space [DEFINED]

$$\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$$

**Proposition 1 (Compactness).** [PROVED] $\mathcal{M}_{\mathrm{obs}}$ is compact (finite product of compact sets, Tychonoff).

**Dimension:** $\dim \mathcal{M}_{\mathrm{obs}} = 8$ (manifold-with-corners).

### DEF-3. Critical Observer Space [DEFINED]

Under the **criticality hypothesis** ($q = q_c(X_t) = 4\lambda_2/|W''(c)|$):

$$\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} \cong \Delta^3 \times B_\xi, \quad \dim = 7$$

**Proposition 2.** [PROVED] $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} \cong \Delta^3 \times B_\xi$ (the criticality condition fixes $q$ as a scene function).

**Note:** The criticality hypothesis is an ASSUMED physical constraint, not an axiom.

---

## §4. Readout Map

### DEF-4. Topological Formation Signature [DEFINED]

Given $u^*(\Theta, X_t) = \arg\min_{u \in \Sigma_m} E_\Theta(u; X_t)$:

$$T_\Theta = (N_0, \mathrm{Bar}_0, \ell_1, \ell_2, A, K^*, C_{bd})$$

where $N_0 = $ component count, $\mathrm{Bar}_0 = $ persistence barcode of superlevel filtration, $\ell_1, \ell_2 = $ dominant bar lengths, $A = \ell_2/\ell_1 = $ articulation ratio, $K^* = $ core count, $C_{bd} = $ boundary band count.

### DEF-5. Readout Map Hierarchy [DEFINED]

$$P_{\min}(\Theta) = d_\Theta \in [0,1]^4 \quad \text{(diagnostic vector only)}$$
$$P_{\mathrm{top}}(\Theta) = (d_\Theta, T_\Theta) \in [0,1]^4 \times \mathcal{T} \quad \text{(recommended)}$$
$$P_{\mathrm{full}}(\Theta) = (d_\Theta, T_\Theta, B_\Theta) \quad \text{(deferred — requires }V\text{)}$$

**Working canonical readout:** $P = P_{\mathrm{top}}$. [ASSUMED — Prop R1 PROVED by VP-1 (exp86, 2026-05-07); continuity of $u^*(\Theta)$ still assumed]

**Audit Warning.** $P_{\min}$ is too coarse: observers with identical diagnostic vectors can produce formations with different topological structure. [**PROVED** by VP-1 (exp86, 2026-05-07; 4 explicit counterexamples; Prop R1 confirmed)]

**Proposition R3 (Quotient descent).** [PROVED (conditional)] $P_{\mathrm{top}}$ is $G$-invariant and descends to a unique map $\bar{P} : \mathfrak{M} \to \mathcal{P}$. Conditional on continuity of $\Theta \mapsto u^*(\Theta)$.

---

## §5. Gauge Group

### DEF-6. SCC Gauge Group [DEFINED]

$$G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}(X_t, \mathcal{N}_t, K, \mathcal{A})$$

with $G_{\mathrm{core\text{-}weight}} = \{e\}$ as default (ASSUMED, pending OP-OMS-001).

**$S_K$:** Permutations of $K$ formation labels. Finite, order $K!$.

**$\mathrm{Aut}_{\mathrm{task}}$:** Task-anchored subgroup of $\mathrm{Aut}(X_t)$. Anchors: task neighborhood $\mathcal{N}_t$, formation count $K$, attention mask $\mathcal{A}$.

**REJECTED:** U(1) on $(\alpha, \beta)$ — exits $\mathbb{R}_{>0}^2$. [REJECTED, AUDIT-001]
**REJECTED:** $S_4$ permutation of energy weights $\lambda$ — energy terms are not interchangeable. [REJECTED, Prop CW1]

---

## §6. Moduli Space

### DEF-7. SCC Observer Moduli Space [DEFINED]

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} \,/\, G_{\mathrm{SCC}}^{(0)}$$

with the quotient topology. Points are orbits $[\Theta] = G \cdot \Theta$.

### DEF-8. Perceptual Core [DEFINED]

The perceptual core of observer $\Theta$ is its orbit $[\Theta] \in \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$.

---

## §7. Topology of the Moduli Space

**Proposition 3 (Compactness).** [PROVED] $\mathfrak{M}$ is compact (continuous image of compact under $\pi$).

**Proposition 4 (Hausdorff).** [PROVED] $\mathfrak{M}$ is Hausdorff (finite group acting on compact Hausdorff space gives Hausdorff quotient).

**Proposition 5 (Dimension preservation).** [PROVED] At generic points (trivial stabilizer), $\dim \mathfrak{M} = \dim \mathcal{M}_{\mathrm{obs}} = 8$. Finite gauge groups do NOT reduce dimension.

**Proposition 6 (Connectedness).** [PROVED] $\mathfrak{M}$ is connected (continuous image of connected space under $\pi$; resolves OP-OMS-003).

**Proposition 7 (Orbifold structure).** [PROVED] $\mathfrak{M}$ is a compact Hausdorff orbifold. Singular strata indexed by stabilizer conjugacy classes. Generic stratum: smooth 8-manifold.

### Dimension Reduction Sources (MANDATORY DISTINCTION)

| Mechanism | Status | DOF removed |
|---|---|---|
| Normalization ($\sum \lambda_i = 1$) | PROVED (already in $\Delta^3$ definition) | 1 (from 4 to 3 energy weights) |
| Gauge ($S_K, \mathrm{Aut}_{task}$) | PROVED (no dimension reduction by finite gauge) | 0 |
| Criticality hypothesis | ASSUMED | 1 (removes $q$ under criticality) |
| RG relevance (irrelevant directions) | HYPOTHESIZED | 2–4 (estimated, unproved) |

---

## §8. Toy Models

### Model A: Minimal Case ($K=1$, trivial $G$, $\xi$ fixed, strict criticality) [PROVED]

$$\mathfrak{M}_{\min} \cong \Delta^3$$

Properties: compact, convex, contractible, $\pi_k = 0$ for all $k$, $\chi = 1$, $\dim = 3$.

**Vertices** = pure-energy observers: $e_{cl}$ (closure-only), $e_{sep}$ (separation-only), $e_{bd}$ (boundary-only), $e_{tr}$ (transport-only).

**Key implication.** No topological barriers in minimal model. Perceptual discontinuity must arise from $V$ basin structure.

### Model B: Two-Formation ($K=2$, $G = S_2$, $\xi$ fixed, strict criticality) [PROVED]

$$\mathfrak{M}_2 \cong \mathrm{Sym}^2(\Delta^3) = (\Delta^3 \times \Delta^3)/S_2$$

Dimension: 6 (generic); orbifold singularity along diagonal $\{[\theta,\theta]\} \cong \Delta^3$ (dim 3, stabilizer $S_2$). Compact, connected.

---

## §9. Observer Landscapes

### DEF-9. Admissible Observer Landscape [DEFINED]

$V_{\mathrm{raw}} : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ is admissible iff it satisfies:

- **V1 (Gauge-invariant):** $V_{\mathrm{raw}}(g \cdot \Theta) = V_{\mathrm{raw}}(\Theta)$
- **V2 (Continuous):** $V_{\mathrm{raw}} \in C^0$
- **V3 (Readout-compatible):** $\nabla V_{\mathrm{raw}}(\Theta) = 0 \Rightarrow P(\Theta)$ locally stable
- **V4 (Basin-generating):** Level sets decompose $\mathcal{M}_{\mathrm{obs}}$ into attraction regions
- **V5 (Boundary-aware):** $V_{\mathrm{raw}}|_{\partial \mathcal{M}_{\mathrm{obs}}} \not\equiv \mathrm{const}$

**Definition (Admissible class).** $\mathcal{V}_{\mathrm{adm}} = \{V_{\mathrm{raw}} : V_{\mathrm{raw}} \text{ satisfies V1–V5}\}$. [DEFINED]

**OMS position:** OMS-1.0 defines the class $\mathcal{V}_{\mathrm{adm}}$, not a unique $V$. The canonical $V$ is an open problem (OP-OMS-002). [OPEN]

**Computational placeholder:** $V_D^0(\lambda) = \|d_\lambda - d^*\|^2$ with $d^* = (1,1,1,0)$. [DEFINED, COMPUTATIONALLY TESTABLE]

**Recommended representative:** $V_P(\Theta) = D_{\mathcal{P}}(P(\Theta), P^*)$ with $D_{\mathcal{P}} = \alpha\|\cdot\|^2 + \beta D_T$. [DEFINED, V3 PROVED conditional]

---

## §10. Basin Stratification

### DEF-10. Basin of Attraction [DEFINED]

For attractor $A_i \subset \mathfrak{M}$, basin:
$$\mathcal{B}_i = \{[\Theta] \in \mathfrak{M} : \lim_{t\to\infty} d(\Phi_t([\Theta]), A_i) = 0\}$$

### DEF-11. Perceptual Observer Type [DEFINED]

$$\mathrm{Type}_i = (\mathcal{B}_i,\ \bar{P}(A_i))$$

**Proposition BS1 (Multiple types on connected space).** [PROVED]

$\mathfrak{M}$ is connected AND can support $\geq 2$ distinct perceptual types. Construction: $\bar{V}(\lambda) = \|\lambda - \lambda^{(1)}\|^2 \cdot \|\lambda - \lambda^{(2)}\|^2$ on $\Delta^3$ has two minima at $\lambda^{(1)}, \lambda^{(2)}$ with disjoint basins.

> **Mandatory central statement:** Perceptual types are not connected components of the observer moduli space; they are attractor basins of an admissible observer landscape on that space.

**Proposition SD1 (Faces are forward-invariant).** [PROVED] Boundary faces $\partial_I \Delta^3$ are absorbing walls of the projected gradient flow. An observer initialized on the $\lambda_{tr} = 0$ face never develops temporal energy.

---

## §11. Core-Weight Symmetry Status

**Status of OP-OMS-001:** SIGNIFICANTLY CONSTRAINED — $G_{\mathrm{cw}} = \{e\}$ COMPUTATIONALLY SUPPORTED (VP-3, exp87, 2026-05-08).

| Candidate | Status |
|---|---|
| $S_4$ weight permutation | REJECTED (Prop CW1) |
| Closure-separation swap $\mathbb{Z}_2$ | **NOT_A_SYMMETRY** (VP-3 A, frac_asym=0.833, n=12) |
| Closure-boundary swap | PARTIAL_SYMMETRY (VP-3 B, scene-dependent) |
| Boundary-closure compensation | PARTIAL (VP-3 C, near $F_{\mathrm{bd}}$ only — not global) |
| Boundary-separation compensation | PARTIAL (VP-3 D, same) |
| Transport invariance (static scenes) | **COMPUTATIONALLY CONFIRMED** (Prop CW2, VP-3 E, n=18) |
| Radial toward centroid | PARTIAL_SYMMETRY (VP-3 F) |
| Random tangent perturbation | PARTIAL_SYMMETRY (VP-3 G) |
| Any global continuous symmetry on $\Delta^3$ | REJECTED for vertex-preserving actions (Prop LS1) |

**Prop CW2 update:** PROVED (conditional) → **COMPUTATIONALLY CONFIRMED** (VP-3 E, $\Delta P_{\mathrm{top}} = 0$ for all 18 static-scene pairs).

**Prop CW3 update:** ASSUMED → **COMPUTATIONALLY SUPPORTED** (no global gauge direction found on $\Delta^3$ for dynamic scenes).

**Default maintained:** $G_{\mathrm{core\text{-}weight}} = \{e\}$ for dynamic scenes. [COMPUTATIONALLY SUPPORTED]

**Approximate symmetry loci** (OP-OMS-017, NEW): near $\{\lambda_{\mathrm{cl}}=\lambda_{\mathrm{sep}}\}$ and near $F_{\mathrm{bd}}$ face, approximate local symmetries exist. Not global gauge directions.

---

## §12. Latent Symmetry Extension

**Core claim:** Continuous compact gauge symmetry belongs to the **OMS-Gen extension**, not OMS-0.x core. [ASSUMED]

**Justification:** No continuous compact group naturally acts on $\mathcal{M}_{\mathrm{obs}}$ without additional structure (latent generator, equivariant architecture, factorized scene distribution). The SCC axioms do not generate such a group.

**Effective dimension** (without latent gauge):
$$\dim \mathfrak{M}_{\mathrm{eff}} \leq 8 - 1 \text{ (criticality)} - k \text{ (relevance)}$$
where $k \in [2, 4]$ is hypothesized (OP-OMS-005, OP-OMS-016).

---

## §13. RG Relevance Program

**Status:** Conceptual framework. Not a theorem. [HYPOTHESIZED as program]

**Definitions provided:** Parameter response map $R(\Theta)$, Jacobian $J_P(\Theta)$, relevant/irrelevant directions, local effective dimension $d_{\mathrm{eff}}(\Theta; \varepsilon)$, coarse-graining map $\mathcal{C}_\varepsilon$.

**Predicted effective directions:**
- $q$ (near $q_c$): RELEVANT for phase transition [HYPOTHESIZED]
- $\lambda_{cl} - \lambda_{sep}$ balance: RELEVANT for formation count [HYPOTHESIZED]
- $\lambda_{bd}$: RELEVANT for boundary morphology [HYPOTHESIZED]
- $\lambda_{tr}$ (static scenes): IRRELEVANT [PROVED conditional]
- $a_{cl}$, $\theta_{core}$, $\theta_{in}$: potentially IRRELEVANT [HYPOTHESIZED]

**Mandatory warning.** RG relevance is a program for estimating $d_{\mathrm{eff}}$, not a proved dimension reduction mechanism. Do not cite as a theorem until Protocol VP-6 is executed.

---

## §14. Boundary and Stratified Dynamics

### Faces of $\Delta^3$ [DEFINED]

Four boundary faces: $F_{cl}, F_{sep}, F_{bd}, F_{tr}$ (codimension-1); six edges (codimension-2); four vertices $e_{cl}, e_{sep}, e_{bd}, e_{tr}$ (codimension-3).

Each face corresponds to a degenerate SCC sub-theory (one energy term absent). The $F_{tr}$ face = static SCC sub-theory. [DEFINED]

### Stratified Flow [DEFINED + PROVED (partial)]

The projected gradient flow on $\Delta^3$ (projected gradient descent onto the simplex) is well-posed at interior points and boundary faces. [PROVED for faces (Prop SD1)]. Regularity at corners: OPEN (OP-OMS-013).

### Full Stratification [DEFINED]

$$\mathfrak{M} = \bigsqcup_{I \subseteq \{cl,sep,bd,tr\},\ [H] \leq G} \mathfrak{M}_{I,[H]}$$

---

## §15. Integration with SCC

**OMS does not modify any SCC theorem.** It uses SCC as input and adds a new observer layer.

**Dependencies:**
- OMS K=1 minimal: INDEPENDENT of temporal theory and multi-formation.
- OMS K≥2: DEPENDS on multi-formation theory (currently Cat B).
- OMS temporal: DEPENDS on T-Temporal-Identity (currently Cat B, pending CV-1.12).
- OMS phase transition: uses T8 directly; T8 unchanged.

**New open problems for SCC exposed by OMS:**
- OP-OMS-009: Regularity of $u^*(\Theta)$ (needed for readout continuity).
- OP-OMS-012: Validity of boundary-face (degenerate) observer types.
- OP-OMS-016: Jacobian singular spectrum of $P_{\mathrm{top}}$.

**OMS Q-mapping:** OMS is a Level-2 "Q0" extension: the question behind Q1–Q6. Different Q-results feed different OMS components.

---

## §16. Propositions and Proof Sketches

### Summary of Proved Propositions

| ID | Statement | Status | Key condition |
|---|---|---|---|
| Prop 1 | $\mathcal{M}_{\mathrm{obs}}$ compact | PROVED | Tychonoff |
| Prop 2 | $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} \cong \Delta^3 \times B_\xi$ | PROVED | Criticality removes $q$ |
| Prop 3 | $\mathfrak{M}$ compact | PROVED | Image of compact under $\pi$ |
| Prop 4 | $\mathfrak{M}$ Hausdorff | PROVED | Finite $G$ on Hausdorff space |
| Prop 5 | Dimension preserved | PROVED | Finite gauge, no dim reduction |
| Prop 6 | $\mathfrak{M}$ connected | PROVED | Image of connected under $\pi$ |
| Prop 7 | $\mathfrak{M}$ is orbifold | PROVED | Finite proper action |
| Prop A1–A6 | $\Delta^3$ topology | PROVED | Convexity, compactness, contractibility |
| Prop B1–B3 | $\mathrm{Sym}^2(\Delta^3)$ structure | PROVED | $S_2$ action, diagonal singularity |
| Prop R3 | $P_{\mathrm{top}}$ descends to quotient | PROVED (conditional) | Continuity of $u^*(\Theta)$ |
| Prop BS1 | Multiple types on connected $\mathfrak{M}$ | PROVED | Construction of 2-basin $V$ |
| Prop SD1 | Faces are absorbing walls | PROVED | Projection argument |
| Prop CW1 | $S_4$ rejected | PROVED | Distinct functional forms |
| Prop CW2 | Transport invariant (static) | **COMPUTATIONALLY CONFIRMED** (VP-3 E) | $\Delta P_{\mathrm{top}} = 0$ for n=18 static pairs |
| Prop CW3 | $G_{\mathrm{cw}} = \{e\}$ default | **COMPUTATIONALLY SUPPORTED** (VP-3 A–G) | No global gauge direction found |
| Prop LS1 | No vertex-preserving cont. symmetry | PROVED | Fixed-point argument |

### Summary of Assumed/Hypothesized Claims

| ID | Statement | Status |
|---|---|---|
| Prop R2 | $P_{\mathrm{top}}$ as working canonical | ASSUMED |
| Hyp RG1 | $d_{\mathrm{eff}}^{\mathrm{typical}} \approx 2$–$4$ | HYPOTHESIZED |
| Hyp SD1 | $F_{tr}$ as static observer basin | HYPOTHESIZED |
| Hyp LS3 | Latent symmetry is Gen extension | ASSUMED |

---

## §17. Open Problems

### Critical Blockers (prevent canonical promotion)

| ID | Title | Status |
|---|---|---|
| OP-OMS-001 | Core-weight gauge group | OPEN (formal proof); **G_cw={e} COMPUTATIONALLY SUPPORTED** (VP-3, exp87, 2026-05-08) |
| OP-OMS-002 | Explicit admissible $V$ | OPEN ($\mathcal{V}_{\mathrm{adm}}$ defined; no explicit element proved admissible) |
| OP-OMS-009 | Readout resolution + continuity | **RESOLVED-NEGATIVE** (VP-1, 2026-05-07; $P_{\min}$ coarseness PROVED; continuity sub-question still open but not a blocker) |

### Important (do not block promotion)

| ID | Title | Status |
|---|---|---|
| OP-OMS-003 | Connectedness | RESOLVED (affirmative, Prop 6) |
| OP-OMS-004 | Contractibility of $\mathrm{Sym}^K(\Delta^3)$ | OPEN |
| OP-OMS-005 | Effective DOF / continuous gauge | OPEN (latent symmetry framework defined) |
| OP-OMS-006 | Topology for non-trivial $\mathrm{Aut}_{task}$ | OPEN |
| OP-OMS-007 | Observer dynamics (Level-3) | DEFERRED |
| OP-OMS-008 | Relation to RelationWorld | OPEN |
| OP-OMS-010 | $V$ existence and regularity | OPEN |
| OP-OMS-011 | Basin stability under scene perturbation | OPEN |
| OP-OMS-012 | Boundary face interpretation | OPEN |
| OP-OMS-013 | Stratified flow at corners | OPEN |
| OP-OMS-014 | Empirical identifiability | OPEN |
| OP-OMS-015 | OMS ↔ perceptual styles | OPEN |
| OP-OMS-016 | Computational $d_{\mathrm{eff}}$ | COMPUTATIONALLY TESTABLE |

---

## §18. Canonical Promotion Checklist

See `canonical_promotion_checklist.md` for the full checklist. Summary:

- **Definitions:** Complete. [✓]
- **Proofs:** Complete for topology, quotient structure, toy models, basin multiplicity. Incomplete for readout continuity, $V$ existence. [✓ partial]
- **Audits:** Complete. All mandatory warnings documented. [✓]
- **Open problems:** Classified. OP-OMS-001, OP-OMS-002 are canonical blockers. OP-OMS-009 RESOLVED-NEGATIVE (VP-1, 2026-05-07). [✓ classified]
- **Integration:** Complete. INDEX.md and CHANGELOG.md updated. [✓]

**Current classification:** CANONICAL CANDIDATE — not yet CANONICAL ACCEPTED.

---

## §19. Audit Statement

This document has been developed under the following audit commitments:

1. No U(1) gauge on $(\alpha, \beta)$ is claimed. [AUDIT-001]
2. Finite gauge groups do not reduce dimension. [AUDIT-002]
3. $G_{\mathrm{core\text{-}weight}} = \{e\}$ is a default, not a theorem. [AUDIT-003]
4. Criticality hypothesis is a physical assumption, not an axiom. [AUDIT-004]
5. $\mathrm{Aut}_{task}$ is task-anchored, not the full graph automorphism group. [AUDIT-005]
6. $\mathcal{M}_{\mathrm{obs}}$ compactness is proved. [AUDIT-006]
7. $P_{\mathrm{top}}$ descent to quotient is proved conditional on optimizer continuity. [AUDIT-007]
8. $\Delta^3$ is the correct minimal moduli space. [AUDIT-008]
9. $b_D = 0$ is fixed, not an observer parameter. [AUDIT-009]
10. $m$ is scene-determined, not observer-controlled. [AUDIT-010]

**New mandatory warnings (OMS-0.2 through OMS-1.0):**

11. $V$ is not unique. OMS-1.0 defines the admissible class, not a canonical single $V$.
12. Basin count depends on $V \in \mathcal{V}_{\mathrm{adm}}$. It is not a canonical invariant of $\mathfrak{M}$ alone.
13. Connectedness of $\mathfrak{M}$ does not imply a single perceptual type. Multiple types arise through basin stratification.
14. RG relevance is a program. Effective DOF estimate is hypothesized, not proved.
15. Latent continuous symmetry is not a core OMS claim. It belongs to OMS-Gen.
16. $P_{\min}$ is too coarse as a canonical readout — **PROVED** (VP-1, exp86, 2026-05-07; Prop R1 confirmed). $P_{\mathrm{top}}$ is the working canonical, itself subject to continuity uncertainty (u*(Θ) assumed continuous, not proved).
17. Orbifold singularities do not automatically correspond to species-typical perceptual styles.
18. Boundary face observers ($\lambda_i = 0$ faces) may represent degenerate limiting theories; their perceptual validity is open.

---

## §20. OMS-1.0 Classification

$$\boxed{\textbf{OMS-1.0-candidate: CANONICAL CANDIDATE — Blocked by OP-OMS-001, OP-OMS-002}}$$

*(OP-OMS-009 RESOLVED 2026-05-07 by VP-1. 2 blockers remain.)*

**Blocked by:**
1. **OP-OMS-001** (core-weight gauge): Until explicitly resolved, $G_{\mathrm{core\text{-}weight}} = \{e\}$ is an assumption, not a theorem.
2. **OP-OMS-002** (admissible $V$): Until an explicit $V \in \mathcal{V}_{\mathrm{adm}}$ is exhibited and proved admissible, the basin stratification is conditional on an unverified existence claim.
~~3. **OP-OMS-009** (readout resolution): RESOLVED-NEGATIVE by VP-1 (2026-05-07). Prop R1 PROVED; continuity of $u^*(\Theta)$ remains open but is not a blocker for the resolution finding.~~

**Ready for canonical promotion once:**
- ~~VP-1 confirms Prop R1 ($P_{\min}$ coarseness).~~ **DONE** (exp86, 2026-05-07)
- VP-3A confirms $g_1 \notin G_{\mathrm{cw}}$ (closure-separation swap not a symmetry). **NEXT**
- VP-2 demonstrates a multi-basin landscape for explicit $V_D^0$.
- Continuity of $u^*(\Theta)$ is established (either by proof or by citing existing regularity results).

**Non-blocked components** (may be promoted independently):
- The topological results (Props 1–7, A1–A6, B1–B3) are canonical-ready.
- The boundary face analysis (Prop SD1, stratified dynamics) is canonical-ready.
- The gauge rejection results (CW1, LS1, AUDIT-001) are canonical-ready.

---

*OMS-1.0-candidate, 2026-05-07. See `canonical_promotion_checklist.md` for detailed criteria. See `checkpoints.md` for session progress.*
