---
type: working/open-problems
created: 2026-05-07
project: Observer Moduli Space of SCC
registry: OP-OMS-001 through OP-OMS-008
---

# Open Problems — Observer Moduli Space

Problems are rated by importance (★★★ critical / ★★ important / ★ useful) and expected difficulty (H/M/L).

---

## OP-OMS-001 — Core-Weight Gauge Group

**Status:** Open  
**Importance:** ★★★  **Difficulty:** H

**Statement.** Is $G_{\mathrm{core\text{-}weight}} = \{e\}$ the correct default, or does a non-trivial compact group act on the energy weights $\lambda$ while preserving perceptual cores?

**Context.** The current formulation sets $G_{\mathrm{core\text{-}weight}} = \{e\}$ by convention (conservative default). The motivation: any continuous group acting on $\lambda \in \Delta^3$ would either: (a) reduce the dimension of $\mathfrak{M}$, or (b) identify observers that have genuinely different perceptual outputs.

**What would resolve it.**
- Identify an energy-weight symmetry $g: \Delta^3 \to \Delta^3$ such that $P(g \cdot \lambda) = P(\lambda)$ for all scenes $X_t$
- OR prove that no such symmetry exists for the full readout $P_{\mathrm{top}}$

**Candidate symmetry to test.** Closure-separation swap: $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}) \leftrightarrow (\lambda_{\mathrm{sep}}, \lambda_{\mathrm{cl}})$ (a $\mathbb{Z}_2$ action on $\Delta^3$). Does this preserve the perceptual core? Requires explicit computation on toy scenes.

**Dependencies.** Requires $P_{\mathrm{top}}$ to be well-defined (DEF-6 in `definitions.md`). Requires explicit scene examples.

---

## OP-OMS-002 — Explicit $V(\Theta)$ Construction

**Status:** Open  
**Importance:** ★★★  **Difficulty:** H

**Statement.** Define $V : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ satisfying requirements V1–V5 (DEF-13 in `definitions.md`), and compute its level sets and critical points for at least one family of scenes.

**Requirements (from DEF-13):**
- V1: Gauge-invariant: $V(g \cdot \Theta) = V(\Theta)$
- V2: Continuous: $V \in C^0(\mathcal{M}_{\mathrm{obs}})$
- V3: Compatible with readout: $\nabla V(\Theta) = 0$ iff $P(\Theta)$ is locally stable
- V4: Basin structure: level sets of $V$ decompose $\mathcal{M}_{\mathrm{obs}}$ into attraction basins
- V5: Boundary awareness: $V(\partial \mathcal{M}_{\mathrm{obs}})$ not identically constant

**Candidate forms:**
1. $V(\Theta) = \|P(\Theta) - P_{\mathrm{ref}}\|^2$ (distance from reference perceptual state)
2. $V(\Theta) = H(P(\Theta))$ (entropy of perceptual distribution)
3. $V(\Theta) = E_{\mathrm{min}}(\Theta, X_t)$ (minimal energy at optimum, scene-dependent)

**What would resolve it.** A single explicit function satisfying V1–V5, or a proof that no such function exists without additional structure.

---

## OP-OMS-003 — Connectedness of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$

**Status:** Open (partial)  
**Importance:** ★★  **Difficulty:** M

**Statement.** Is $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ connected for general $(K, \mathrm{Aut}_{task})$?

**Known:**
- Model A ($K=1$, trivial $G$): $\mathfrak{M}_{\min} \cong \Delta^3$, which is connected.
- Model B ($K=2$, $S_2$): $\mathrm{Sym}^2(\Delta^3)$ is connected (quotient of connected by connected).
- General: unknown when $\mathrm{Aut}_{task}$ acts non-trivially with multiple components.

**What could cause disconnectedness.** If $\mathrm{Aut}_{task}$ partitions $\mathcal{M}_{\mathrm{obs}}$ into regions with different orbit structures, the quotient could have multiple connected components. This would require $\mathrm{Aut}_{task}$ to act with disconnected fixed-point loci.

**What would resolve it.** Prove that for any finite $G$ acting on $\mathcal{M}_{\mathrm{obs}}$ (compact, connected), the quotient $\mathcal{M}_{\mathrm{obs}}/G$ is connected. (This is in fact true: continuous image of connected set under quotient map is connected.)

**Near-resolution.** The quotient of a connected space by a group action is always connected, provided the action is continuous. Since $G$ is finite (hence the action is trivially continuous), $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is connected whenever $\mathcal{M}_{\mathrm{obs}}$ is connected. $\mathcal{M}_{\mathrm{obs}}$ is connected (product of connected sets). So **OP-OMS-003 is likely resolved in the affirmative** — needs only to be written up cleanly.

---

## OP-OMS-004 — Contractibility of $\mathrm{Sym}^K(\Delta^3)$

**Status:** Open  
**Importance:** ★★  **Difficulty:** M

**Statement.** Is $\mathrm{Sym}^K(\Delta^3)$ contractible for all $K \geq 1$?

**Known:**
- $K=1$: $\Delta^3$ is contractible (proved in toy_models.md Proposition A3).
- $K=2$: $\mathrm{Sym}^2(\Delta^3) = (\Delta^3 \times \Delta^3)/S_2$. Need to verify contractibility.

**General principle.** If $X$ is contractible, is $\mathrm{Sym}^K(X)$ contractible? This is a standard result in algebraic topology when $X$ is a CW complex: $\mathrm{Sym}^K(X)$ need not be contractible in general, but for contractible $X$ the answer is yes (Milgram 1967 argument via configuration spaces).

**Perceptual implication.** If $\mathrm{Sym}^K(\Delta^3)$ is contractible for all $K$, then the moduli space has no topological barriers between observer states, and all perceptual discontinuities must arise from $V(\Theta)$ basin structure.

**What would resolve it.** Explicit proof or citation of the general contractibility result for $\mathrm{Sym}^K$ of contractible spaces.

---

## OP-OMS-005 — Effective Degrees of Freedom

**Status:** Open  
**Importance:** ★★★  **Difficulty:** M

**Statement.** What is the effective dimensionality of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ after all constraints, gauge identifications, and relevance flow are applied?

**Theoretical estimate:** 1–3 effective DOF (from conversational analysis 2026-05-07).

**Known dimension-reducing mechanisms:**
1. Normalization $\sum \lambda_i = 1$: removes 1 DOF (from raw 4 to 3)
2. Criticality hypothesis $q = q_c(X_t)$: removes 1 more DOF (from 4+ to 3)
3. Relevance flow (RG-analogy): irrelevant parameter directions flow to fixed values, reducing effective DOF further

**What is unknown.** Which specific directions in $(\lambda, \xi)$ space are irrelevant (in the RG sense) and which are relevant? This requires computing the Hessian of $V(\Theta)$ at critical points — which in turn requires $V$ to be defined (see OP-OMS-002).

**What would resolve it.** Explicit computation of $\partial^2 V / \partial \Theta_i \partial \Theta_j$ at a representative critical point, showing which eigenvalues are large (relevant directions) and which are near-zero (irrelevant).

---

## OP-OMS-006 — Topology of $\mathcal{M}_{\mathrm{obs}} / G$ for Non-Trivial $\mathrm{Aut}_{task}$

**Status:** Open  
**Importance:** ★★  **Difficulty:** H

**Statement.** For a non-trivial $\mathrm{Aut}_{task}(X_t, \mathcal{N}_t, K, \mathcal{A})$, what is the topology of the quotient?

**Context.** $\mathrm{Aut}_{task}$ is task-anchored: it is the subgroup of graph automorphisms of $X_t$ that (a) preserve the task-relevant neighborhood structure $\mathcal{N}_t$, (b) respect the formation count $K$, and (c) fix the attention mask $\mathcal{A}$ setwise.

**Example where $\mathrm{Aut}_{task}$ is non-trivial.** A grid scene $X_t = \mathbb{Z}^2_{n \times n}$ with 4-fold rotational symmetry. If the task has no preferred orientation, $\mathrm{Aut}_{task} \supseteq \mathbb{Z}_4$. The quotient $\mathcal{M}_{\mathrm{obs}} / \mathbb{Z}_4$ introduces additional orbifold singularities at fixed points of the $\mathbb{Z}_4$ action.

**What would resolve it.** For a specific example ($X_t$ = symmetric grid, $K = 1$, $\mathrm{Aut}_{task} = \mathbb{Z}_4$):
1. Identify the fixed-point locus in $\mathcal{M}_{\mathrm{obs}}$
2. Compute local orbifold structure at fixed points
3. Determine the stratification of $\mathcal{M}_{\mathrm{obs}} / \mathbb{Z}_4$

---

## OP-OMS-007 — Observer as Dynamical System (Level-3 Extension)

**Status:** Open (deferred to Level-3 SCC)  
**Importance:** ★★  **Difficulty:** H

**Statement.** Formalize the observer dynamics $\Theta_o(t) = F^t(s_o)$ where $s_o$ is the observer seed, and identify what constraints $F$ must satisfy for $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ to be the correct moduli space for steady-state observer types.

**Current treatment.** This document treats $\Theta_o$ as static. The dynamical question — which $\Theta$ are attractors of $F$, how $s_o$ maps to attractors, and whether the attractor structure is consistent with the moduli space stratification — is deferred.

**Connection to current work.** If $F$ has finitely many attractors $\Theta_1^*, \ldots, \Theta_r^* \in \mathcal{M}_{\mathrm{obs}}$, then the "observer types" are precisely $[\Theta_1^*], \ldots, [\Theta_r^*] \in \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$, and the moduli space topology determines how many distinct observer types exist.

**What would resolve it.** A Level-3 SCC formalism defining $F : \mathcal{M}_{\mathrm{obs}} \to \mathcal{M}_{\mathrm{obs}}$ as a contraction or gradient flow, with explicit attractor analysis.

---

## OP-OMS-008 — Relation to RelationWorld Theory Gauge Structure

**Status:** Open  
**Importance:** ★  **Difficulty:** M

**Statement.** Does $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{task}$ share mathematical structure with the discrete gauge groups appearing in RelationWorld Theory (finite graphs, discrete Yang–Mills)?

**Context.** RelationWorld Theory (in `theory/`) develops discrete gauge structure on finite graphs, including analogues of Yang–Mills gauge groups. The SCC gauge group $G_{\mathrm{SCC}}^{(0)}$ also acts on finite graph structures ($X_t$).

**Specific question.** Is there a functorial relationship between $\mathrm{Aut}(X_t)$ (graph automorphism group, appearing in RelationWorld) and $\mathrm{Aut}_{task}(X_t, \mathcal{N}_t, K, \mathcal{A})$ (task-anchored subgroup, appearing in SCC)?

**What would resolve it.** Identify a common categorical framework (e.g., groupoids on finite graphs) that captures both gauge structures as special cases.

---

## OP-OMS-009 — Readout Resolution Completeness

**Status:** RESOLVED-NEGATIVE (VP-1, 2026-05-07)
**Importance:** ★★★  **Difficulty:** M
**Canonical blocker:** REMOVED (resolved)

**Statement.** Does $P_{\mathrm{top}}$ distinguish all perceptually relevant core differences, and is it continuous in $\Theta$?

**Sub-questions:**
- (a) Is $P_{\min}$ strictly coarser than $P_{\mathrm{top}}$? — **RESOLVED: YES** (VP-1, exp86, 4 explicit counterexamples)
- (b) Is $P_{\mathrm{top}}$ continuous in $\Theta$? (Requires continuity of $u^*(\Theta)$ — still OPEN)
- (c) Is $u^*(\Theta)$ unique for generic $\Theta$? What is the non-unique set? (OPEN)
- (d) What tie-breaking rule should be used when multiple global minima exist? (OPEN)

**Resolution of (a).** Protocol VP-1 (exp86_vp1_p_resolution_audit.py, 2026-05-07) found 4 definitive counterexamples: observer configurations with $\|P_{\min}(\Theta_1) - P_{\min}(\Theta_2)\| < 0.15$ and $K_{\mathrm{core}}(\Theta_1) \neq K_{\mathrm{core}}(\Theta_2)$. Tightest: $\lambda_A=(0.6,0.2,0.2)$ vs $\lambda_B=(0.5,0.3,0.2)$, $\|d\|=0.071$, $D_T=3.028$, $K_{\mathrm{core}}$ 2 vs 1. Prop R1 promoted from HYPOTHESIZED to PROVED.

**Residual (b)–(d).** The continuity of $u^*(\Theta)$ (needed for Prop R3 / $P_{\mathrm{top}}$ descent to quotient) remains open but is no longer a blocker for the resolution question. Sub-questions (b)–(d) are tracked as open concerns within OP-OMS-009.

**Evidence.** `vp1_p_resolution_audit.md`, `vp1_counterexamples.md`, `CODE/experiments/results/observer_moduli/vp1_pairs.json`.

---

## OP-OMS-010 — Existence and Regularity of Admissible Observer Landscape

**Status:** Open
**Importance:** ★★★  **Difficulty:** H
**Canonical blocker:** YES (subsumed by OP-OMS-002)

**Statement.** Does $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$? Specifically:

(a) Existence: Is there any $V$ satisfying V1–V5?
(b) Regularity: Is there $V \in \mathcal{V}_{\mathrm{adm}} \cap C^1(\mathcal{M}_{\mathrm{obs}})$?
(c) Basin count: For the recommended $V_P$, how many distinct basins does $\mathfrak{M}$ have?
(d) Universality: Is the basin stratification topology independent of the choice of $V \in \mathcal{V}_{\mathrm{adm}}$?

**Partial progress.** $V_D^0$ satisfies V1 (proved), V2 (assumed). V3–V5 open.

**Attack plan.** Protocol VP-2 for (c). Prove $V_D^0 \in \mathcal{V}_{\mathrm{adm}}$ to resolve (a).

---

## OP-OMS-011 — Basin Stability Under Scene Distribution Perturbation

**Status:** Open
**Importance:** ★★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Is the basin stratification of $\mathfrak{M}$ stable under small perturbations of the scene distribution $\mathcal{D}$?

**Precise form.** Let $\mathcal{D}_\epsilon$ be a family of scene distributions with $\mathcal{D}_0 = \mathcal{D}$. If $V_{\mathcal{D}_\epsilon}$ changes continuously in $\epsilon$ (in $C^1$ norm), does the basin count and topological type of basins remain constant for small $\epsilon$?

**Expected answer (HYPOTHESIZED).** Yes, by structural stability of Morse functions. Basin transitions (bifurcations) occur at isolated values of $\epsilon$.

**What would resolve it.** Application of Palis-Smale structural stability theorem to $\bar{V}_\epsilon$ on $\mathfrak{M}$.

---

## OP-OMS-012 — Boundary-Face Interpretation of $\Delta^3$

**Status:** Open
**Importance:** ★★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Are the boundary faces of $\Delta^3$ (degenerate observers with $\lambda_i = 0$) valid limiting perceptual theories, or do they represent ill-posed configurations?

**Sub-questions:**
- Is $E_{\mathrm{cl}}$ alone (vertex $e_{cl}$) a well-posed energy producing non-trivial formations?
- What does the SCC optimizer output at the $F_{sep}$ face (no separation energy)?
- Do face observers correspond to identifiable perceptual strategies in human perception?

**Attack plan.** Protocol VP-4 (boundary face ablation). Run SCC optimizer with each energy term individually zeroed.

---

## OP-OMS-013 — Stratified Gradient Flow at Corners

**Status:** Open
**Importance:** ★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Is the projected gradient flow on $\Delta^3$ (manifold-with-corners) well-posed and convergent at corner strata (codimension $\geq 2$ faces)?

**Context.** At interior points and codimension-1 faces, the projected gradient flow is standard (well-known convergence theory). At corners (vertices and higher-codimension faces), the tangent cone is strictly smaller and convergence is less clear.

**What would resolve it.** Application of variational convergence theory for gradient flows on convex polytopes (e.g., Rockafellar, convex analysis).

---

## OP-OMS-014 — Empirical Identifiability of Observer Moduli Coordinates

**Status:** Open
**Importance:** ★★  **Difficulty:** H
**Canonical blocker:** No

**Statement.** Can the observer parameters $\Theta = (q, \lambda, \xi)$ be identified from behavioral or neural data?

**Sub-questions:**
- Given a subject's perceptual responses on a battery of scenes, can $\lambda$ be estimated?
- Is the estimation problem well-identified (no degeneracy)?
- What is the minimum scene battery size for reliable $\lambda$ estimation?

**Connection to OMS.** Empirical identifiability is required to test the OMS framework against human data (Protocol EP-1).

---

## OP-OMS-015 — Relation Between OMS Basin Types and Psychological Perceptual Styles

**Status:** Open
**Importance:** ★★  **Difficulty:** H
**Canonical blocker:** No

**Statement.** Do the attractor basins of $\mathfrak{M}$ (under an admissible $V$) correspond to recognized clusters of perceptual style in human or animal perception?

**Prediction (HYPOTHESIZED).** Different perceptual style clusters (e.g., "figure-dominant" vs. "ground-dominant" perceivers, or "closure-seekers" vs. "separation-seekers") correspond to different basins in $\mathfrak{M}$.

**What would resolve it.** Protocol EP-1 (psychophysical perceptual style clustering): fit $\lambda$ from behavioral data, cluster in $\Delta^3$, compare with OMS basin predictions from VP-2.

---

## OP-OMS-016 — Computational Estimation of $d_{\mathrm{eff}}$ Through Jacobian Singular Spectrum

**Status:** COMPUTATIONALLY TESTABLE
**Importance:** ★★  **Difficulty:** L
**Canonical blocker:** No

**Statement.** What is the distribution of local effective dimension $d_{\mathrm{eff}}(\Theta; \varepsilon)$ over $\mathcal{M}_{\mathrm{obs}}$?

**Method.** Numerical finite-difference Jacobian $J_P(\Theta)$ at a grid of sample points; SVD; count singular values above threshold $\varepsilon$.

**Expected result (Hypothesis RG1).** $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2, 4]$.

**Attack plan.** Protocol VP-6 using existing SCC code. Straightforward to implement.

---

## Summary Table

*Updated 2026-05-07 (OMS-0.2 through OMS-1.0)*

| ID | Title | Importance | Difficulty | Status | Blocker? |
|---|---|---|---|---|---|
| OP-OMS-001 | Core-Weight Gauge Group | ★★★ | H | Open (constrained) | YES |
| OP-OMS-002 | Admissible $V$ Existence | ★★★ | H | Open | YES |
| OP-OMS-003 | Connectedness | ★★ | M | **RESOLVED** (Prop 6) | No |
| OP-OMS-004 | Contractibility of $\mathrm{Sym}^K(\Delta^3)$ | ★★ | M | Open | No |
| OP-OMS-005 | Effective DOF / Latent Gauge | ★★★ | M | Open | No |
| OP-OMS-006 | Topology for Non-Trivial $\mathrm{Aut}_{task}$ | ★★ | H | Open | No |
| OP-OMS-007 | Observer Dynamics (Level-3) | ★★ | H | Deferred | No |
| OP-OMS-008 | Relation to RelationWorld | ★ | M | Open | No |
| OP-OMS-009 | Readout Resolution + Continuity | ★★★ | M | **RESOLVED-NEGATIVE** (VP-1) | REMOVED |
| OP-OMS-010 | $V$ Existence and Regularity | ★★★ | H | Open | YES (via OP-002) |
| OP-OMS-011 | Basin Stability | ★★ | M | Open | No |
| OP-OMS-012 | Boundary Face Interpretation | ★★ | M | Open | No |
| OP-OMS-013 | Stratified Flow at Corners | ★ | M | Open | No |
| OP-OMS-014 | Empirical Identifiability | ★★ | H | Open | No |
| OP-OMS-015 | OMS ↔ Perceptual Styles | ★★ | H | Open | No |
| OP-OMS-016 | Computational $d_{\mathrm{eff}}$ | ★★ | L | Computationally testable | No |

**Canonical promotion blockers:** OP-OMS-001, OP-OMS-002 (= OP-OMS-010). ~~OP-OMS-009 RESOLVED 2026-05-07 (VP-1).~~

**Immediate computational attacks:** VP-3 (→ 001), VP-2 (→ 002/010), VP-6 (→ 016). ~~VP-1 (→ 009): COMPLETE.~~

**OP-OMS-003 resolved:** Connectedness proved by Prop 6 (observer_moduli_space.md). No longer open.
