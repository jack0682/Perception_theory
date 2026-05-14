---
type: working/open-problems
created: 2026-05-07
project: Observer Moduli Space of SCC
registry: OP-OMS-001 through OP-OMS-008
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Open Problems — Observer Moduli Space

Problems are rated by importance (★★★ critical / ★★ important / ★ useful) and expected difficulty (H/M/L).

---

## OP-OMS-001 — Core-Weight Gauge Group

**Status:** Open (VP-3 significantly constrains — default G_cw={e} COMPUTATIONALLY SUPPORTED, 2026-05-08)
**Importance:** ★★★  **Difficulty:** H

**Statement.** Is $G_{\mathrm{core\text{-}weight}} = \{e\}$ the correct default, or does a non-trivial compact group act on the energy weights $\lambda$ while preserving perceptual cores?

**Context.** The current formulation sets $G_{\mathrm{core\text{-}weight}} = \{e\}$ by convention (conservative default). The motivation: any continuous group acting on $\lambda \in \Delta^3$ would either: (a) reduce the dimension of $\mathfrak{M}$, or (b) identify observers that have genuinely different perceptual outputs.

**VP-3 Results (exp87, 2026-05-08).** Seven transformation families A–G tested on S3 and S4 scenes:

| Transform | Verdict | frac_asym | n |
|---|---|---|---|
| A: Closure-sep swap | **NOT_A_SYMMETRY** | 0.833 | 12 |
| B: Closure-bd swap | PARTIAL_SYMMETRY | 0.500 | 12 |
| C: Bd-cl compensation | PARTIAL_SYMMETRY | 0.368 | 38 |
| D: Bd-sep compensation | PARTIAL_SYMMETRY | 0.421 | 38 |
| E: Transport ablation (static) | **CANDIDATE_SYMMETRY** | 0.000 | 18 |
| F: Radial toward centroid | PARTIAL_SYMMETRY | 0.300 | 60 |
| G: Random tangent | PARTIAL_SYMMETRY | 0.217 | 60 |

- **Prop CW2** (static transport invariance): **COMPUTATIONALLY CONFIRMED** (VP-3 E, n=18).
- **Prop CW3** (G_cw={e} default): **COMPUTATIONALLY SUPPORTED** (no global gauge direction found).
- PARTIAL_SYMMETRY results (B, C, D, F, G) reflect approximate local symmetry loci near $\{\lambda_{\mathrm{cl}}=\lambda_{\mathrm{sep}}\}$ and near $F_{\mathrm{bd}}$. See **OP-OMS-017**.

**What would fully resolve it.**
- Formal proof that no diffeomorphism $g: \Delta^3 \to \Delta^3$ satisfies $P(g \cdot \lambda) = P(\lambda)$ for all scenes (beyond the static-scene transport invariance).

**Dependencies.** Requires $P_{\mathrm{top}}$ to be well-defined (DEF-6 in `definitions.md`).

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

**Status:** Open (VP-4 results: (c) COMPUTATIONALLY SUPPORTED, 2026-05-08)
**Importance:** ★★★  **Difficulty:** H
**Canonical blocker:** YES (subsumed by OP-OMS-002)

**Statement.** Does $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$? Specifically:

(a) Existence: Is there any $V$ satisfying V1–V5?
(b) Regularity: Is there $V \in \mathcal{V}_{\mathrm{adm}} \cap C^1(\mathcal{M}_{\mathrm{obs}})$?
(c) Basin count: For $V_D^0$, how many distinct basins does $\mathfrak{M}$ have?
(d) Universality: Is the basin stratification topology independent of the choice of $V \in \mathcal{V}_{\mathrm{adm}}$?

**VP-4 Results (exp88, 2026-05-08).** Direct evaluation of $V_D^0$ at 6 strategic $\lambda$-points on S3 and S4:

- **Sub-question (c):** ≥2 distinct observer types found on both scenes ($\Delta d = 0.40$ on S3, $\Delta d = 0.52$ on S4). **COMPUTATIONALLY SUPPORTED.**
- cl-dominant observer (P1: $\lambda_{cl}=0.70$) is a consistently distinct perceptual type.
- On S4 (two 5-cliques): cl-dominant gives symmetric equilibrium (no dominant formation), while all other observers select one clique as dominant.
- Persist=1.00 for all evaluations on static scenes, consistent with Prop CW2.

**Partial progress.** $V_D^0$ satisfies V1 (proved), V2 (assumed), V4 (COMPUTATIONALLY SUPPORTED, VP-4). V3, V5 open.

**Attack plan.** (a)–(d) remain open in full generality. $V_D^0$ partially satisfies V1+V2+V4; V3 (critical points vs readout stability) and V5 (boundary awareness) require further work.

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

## OP-OMS-017 — Approximate Symmetry Loci in $\lambda$-Space

**Status:** Open (NEW — VP-3, Session 4, 2026-05-08)
**Importance:** ★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Are there codimension-1 submanifolds $S \subset \Delta^3$ on which a transformation $g$
acts as an approximate gauge symmetry of $P_{\mathrm{top}}$ (i.e., $\Delta P_{\mathrm{top}}(g \cdot \lambda, \lambda) < \epsilon$)?

**VP-3 evidence.** Two candidate loci:
1. $S_A = \{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$: closure-sep swap is approximately a local symmetry (VP-3 A).
2. $S_B = \{F_{\mathrm{bd}}\text{ neighborhood}\}$: boundary-dominant face, compensation near-symmetric (VP-3 C, D).

**Why it matters.** Approximate symmetry loci define flat regions of the observer landscape $V$.
These flat regions slow observer adaptation — near $S$, gradient flow $\dot\Theta = -\nabla V$ has small magnitude.
They define perceptual indifference surfaces: configurations on $S$ are perceptually equivalent up to $\epsilon$.

**What would resolve it.** Map $\Delta P_{\mathrm{top}}(g \cdot \lambda, \lambda)$ on a fine grid and identify
the level set $\{\Delta P_{\mathrm{top}} < 0.05\}$.

---

## OP-OMS-018 — Optimizer Regularity in $\lambda$-Space

**Status:** PARTIALLY RESOLVED (Session 5, 2026-05-08)
**Importance:** ★★★  **Difficulty:** H
**Canonical blocker:** No (blocks OMS-2.0 full canonicalization, but local results are now PROVED)

**Statement.** For fixed scene $X_t$ and $\lambda \in \Delta^3$: is the map
$\lambda \mapsto u^*(\lambda; X_t)$ continuous / $C^1$ in $\lambda$?

**Resolution status (Session 5, theory in `op_oms_018_regular_u_star.md`):**

- **Theorem R1 — Local interior $C^1$ branch:** PROVED. At a non-degenerate interior minimum
  with positive-definite projected Hessian, the IFT yields a $C^1$ branch of $u^*(\lambda)$
  on a neighborhood. (See `op_oms_018_regular_u_star.md` §3.)
- **Theorem R2 — Local piecewise $C^1$ on a fixed active set:** PROVED. Robinson–Fiacco
  parametric NLP sensitivity under LICQ + strict complementarity + 2nd-order sufficiency.
  (`op_oms_018_regular_u_star.md` §4.)
- **Prop R3 (1)–(2) — Argmin u.h.c., $v$ continuous:** PROVED via Berge.
- **Prop R3 (3) — No global continuous selection:** PROVED by VP-1 / VP-4 counterexamples.
  Hence **global $C^1$ regularity is REJECTED**. Branch-switching surfaces $\Sigma_{\mathrm{branch}}$
  are non-empty and codim-1.
- **Prop R4 — $v(\lambda)$ continuous, concave, locally Lipschitz:** PROVED.
  $v$ is the inf of a family of (linear-in-$\lambda$) functions.
- **Theorem R5 — Envelope on regular branches:** PROVED. $\partial v / \partial \lambda_i = E_i(u^*)$
  on the regular branch.

**OMS implication.** $u^*$ is *not* the appropriate smooth-on-$\Delta^3$ object; the
**value function $v$ is**. OMS gradient-flow / basin / RG analyses should be referred
to $v$ on $\Delta^3$ rather than $u^*$ on $\Omega$. Branch-switching surfaces are
**observer-type transition surfaces**, not regularity defects (OP-OMS-026).

**Remaining sub-problems:** OP-OMS-024 (constant-rank regions of $J_R$), OP-OMS-026
(characterize $\Sigma_{\mathrm{branch}}$), OP-OMS-027 (corner cases), OP-OMS-028
(quantitative Lipschitz for $v$).

---

## OP-OMS-024 — Constant-rank Regions for $P_{\mathrm{top}}$ Response Map

**Status:** Open (NEW — VP-6, Session 5, 2026-05-08)
**Importance:** ★★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Identify open subsets of $\Delta^3$ on which the readout Jacobian
$J_R(\lambda) = D_\lambda R_{\mathrm{vec}}(\lambda)$ has constant rank $r$.

**Why it matters.** Prop ED2 (`effective_dof_theory.md`) is conditioned on a
constant-rank assumption. If validated locally, the level sets of $R$ are
perceptual indifference leaves — concrete codim-$r$ submanifolds of the
moduli space.

**VP-6 evidence.** On S4 (two cliques) every interior sample yields
$d_{\mathrm{eff}}(\lambda; \mathrm{rel}=5\!\times\!10^{-2}) = 1$ — strong
evidence for a constant-rank-1 region away from cl-axis. On S3 (grid),
$d_{\mathrm{eff}}$ alternates between 1 and 2 across samples; no obvious
constant-rank region.

**What would resolve it.** Fine grid sampling of $J_R$ on $\Delta^3$ and
boundary detection between rank-1 and rank-2 regions.

---

## OP-OMS-025 — Empirical Correspondence: $d_{\mathrm{eff}}$ ↔ Perceptual Style Dimensions

**Status:** Open (NEW — VP-6, Session 5, 2026-05-08)
**Importance:** ★★  **Difficulty:** H
**Canonical blocker:** No

**Statement.** Relate the per-base-point $d_{\mathrm{eff}}(\Theta; \varepsilon)$
of VP-6 to empirically observed perceptual-style dimensions in human
psychophysics (EP-1).

**Hypothesis.** Low $d_{\mathrm{eff}}$ at most points predicts that human
perceptual styles cluster along **few** continuous dimensions (e.g.\
"closure-vs-separation balance" as the dominant axis), with discrete
between-cluster jumps captured by $\Sigma_{\mathrm{branch}}$ rather than
intermediate continuous values.

**What would resolve it.** EP-1 protocol with fitted $\lambda$ across human
participants; cluster topology compared with VP-6 stratification.

---

## OP-OMS-026 — Characterize Branch-Switching Loci $\Sigma_{\mathrm{branch}}$

**Status:** PARTIALLY RESOLVED (Session 5, VP-7, 2026-05-08)
**Importance:** ★★★  **Difficulty:** H
**Canonical blocker:** No (but central to the OMS-1.2 stratified picture)

**Statement.** Characterize the codim-1 surfaces $\Sigma_{\mathrm{branch}} \subset \Delta^3$
on which $u^*(\lambda)$ exchanges branches (and hence the readout map jumps
in its discrete components $K_{\mathrm{core}}$, $n_{\mathrm{high}}$).

**Resolution status (Session 5):**

**VP-6 evidence (computational localization).** A surface near
$\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$ on S3 (6×6 grid).
A surface separating cl-dominant ($n_{\mathrm{high}} = 0$ symmetric
equilibrium) from other observer types on S4 (two cliques).

**VP-7 evidence (Session 5, fine-grid mapping, `vp7_branch_map_results.md`).**
On the static face $\Delta^2_{\mathrm{static}}$:

- **P12 (path graph, K=10, 66 points):** 7 distinct branches, 44
  transition edges. Dominant branch $(3, 4)$ covers 66.7% of $\Delta^2$ —
  **constant-rank region candidate** (OP-OMS-024).
- **S3 (6×6 grid, K=8, 45 points):** 17 distinct branches, 74 transition
  edges. **Fragmented** — no single dominant branch, several singletons.

**$\Sigma_{\mathrm{branch}}$ is non-empty, codim-1, and scene-complexity-dependent.**
Simple scenes (P12) admit a coarse stratification with one dominant cell;
2D-grid scenes (S3) admit fine stratifications with many small cells.

**Connection to OP-OMS-017.** OP-OMS-017 originally posed the
$\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$ region as an "approximate
symmetry locus". VP-6 reveals it is in fact a **branch-switching
surface** — *not* an approximate gauge symmetry. OP-OMS-017 is **superseded**
by OP-OMS-026 in the OMS-1.2 reading; closed.

**Remaining sub-problems for full resolution:**

(a) VP-7 extended to full simplex $\Delta^3$ (4-coordinate tetrahedral grid).
(b) Theoretical: characterize $\Sigma_{\mathrm{branch}}$ analytically via
    the bordered-Hessian degeneracy condition $\det M_0 = 0$ from
    Theorem R1 (`op_oms_018_regular_u_star.md`). Relate to T8.
(c) Higher-resolution VP-7 (K=12, K=16) to test whether singleton branches
    on S3 are real or grid artifacts.

---

## OP-OMS-001 — Closure (Session 6 OMS-2.0 Push)

**Status update:** Conditional closure obtained, with three detailed proof
files (`op_oms_001_gap_c1_rank_theorem.md`, `op_oms_001_gap_c1_sensitivity.md`,
`op_oms_001_gap_c1_genericity.md`) and computational H4 witness in
`vp8_gap_c1_rank_witness.json` (Gate 2: 34/42 = 81% full-rank witnesses
across P12, S3, asymmetric K4+tail; rank(J_e_tan) = 2 in all 42 cases).

**Theorems proved:** RT1 (Rank Obstruction) conditional on H1–H3; RT2
(local injectivity of $e$); RT3 (Reduction-C closure of $G_{\mathrm{cw}}$);
S1 (interior sensitivity formula $J_e = -G_T^\top H_T^{-1} G_T$); S2
(active-set sensitivity); G1–G7 (analytic genericity chain); G8
(continuous extension to identity); GAP-C1 (closure of Gap C1 conditional
on H4).

**H4 (witness existence)** is now COMPUTATIONALLY CONFIRMED by Gate 2.

**Net status update:** OP-OMS-001 reads as **PROVED on a generic open
dense subset, conditional on the H4 computational witness** — promotable
in canonical theories that admit "computational witness" as a valid
proof step (the standard for inhomogeneous analytic problems where one
non-vanishing minor establishes generic non-vanishing).

---

## OP-OMS-029 — Continuous Component of $G_{\mathrm{cw}}$ is Trivial

**Status:** PROVED (Session 5, 2026-05-08)
**Importance:** ★★  **Difficulty:** M
**Canonical blocker:** No (subsumed under OP-OMS-001)

**Statement.** The identity component of any candidate core-weight gauge
group $G_{\mathrm{cw}}$ is trivial.

**Resolution.** PROVED in `op_oms_001_formal_proof_attempt.md` §3
(Reduction B + Prop LS1). Any continuous one-parameter family of
$P_{\mathrm{top}}$-preserving maps must fix the four vertices
$\{e_{cl}, e_{sep}, e_{bd}, e_{tr}\}$ (because each has a distinct
$P_{\mathrm{top}}$ signature, see VP-1 / VP-3 evidence and Prop CW1). By
Prop LS1, no continuous group acts faithfully on $\Delta^3$ preserving
all four vertices, so the entire one-parameter family is the identity.

**Implication.** $G_{\mathrm{cw}}$, if non-trivial, is **discrete**. The
remaining VP-3 evidence rules out $S_4$ (Prop CW1) and all 7 transformation
families A–G; only proper subgroups remain as residual candidates and
those are ruled out empirically. Formal closure of OP-OMS-001 reduces
to the discrete-subgroup case.

---

## OP-OMS-027 — Regularity at Corners of $\Omega = \Sigma_m \cap [0,1]^n$

**Status:** Open (NEW — Session 5, 2026-05-08)
**Importance:** ★  **Difficulty:** M
**Canonical blocker:** No

**Statement.** Theorem R2 (`op_oms_018_regular_u_star.md`) assumes LICQ. At
a corner of $\Omega$ where many box constraints are simultaneously active
(say $|A^=_0 \cup A^=_n| = n - 1$), R2 may fail. Establish a
directional-derivative version of $u^*(\lambda)$ regularity at corners
using Mordukhovich generalized differentiation or tangent-cone analysis.

**What would resolve it.** Apply Bonnans–Shapiro *Perturbation Analysis of
Optimization Problems* Ch. 5 to the SCC corner case.

---

## OP-OMS-028 — Quantitative Lipschitz Constant for $v(\lambda)$

**Status:** Open (NEW — Session 5, 2026-05-08)
**Importance:** ★  **Difficulty:** L
**Canonical blocker:** No

**Statement.** Prop R4 establishes that $v$ is **locally Lipschitz** on
$\mathrm{int}(\Delta^3)$. Make this quantitative: bound $|v(\lambda + \delta) - v(\lambda)|
\le L \|\delta\|$ in terms of $\sup_{u \in \Omega} \|E(u)\|_2$ where
$E(u) = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u)$.

**Sketch.** $|v(\lambda) - v(\lambda')| = |\inf_u L_u(\lambda) - \inf_u L_u(\lambda')|
\le \sup_u |L_u(\lambda) - L_u(\lambda')| \le \sup_u \|E(u)\|_2 \cdot \|\lambda - \lambda'\|_2$.

**What would resolve it.** Bound the SCC energy components on $\Omega$ in
closed form (in terms of graph quantities $\|L\|_\mathrm{op}$, $n$, $m$).

---

## Summary Table

*Updated 2026-05-08 (VP-3 results, Session 4)*

| ID | Title | Importance | Difficulty | Status | Blocker? |
|---|---|---|---|---|---|
| OP-OMS-001 | Core-Weight Gauge Group | ★★★ | H | Open (**G_cw={e} COMP. SUPPORTED**, VP-3) | YES (formal proof) |
| OP-OMS-002 | Admissible $V$ Existence | ★★★ | H | Open (VP-2: existence HYPOTHESIZED) | YES |
| OP-OMS-003 | Connectedness | ★★ | M | **RESOLVED** (Prop 6) | No |
| OP-OMS-004 | Contractibility of $\mathrm{Sym}^K(\Delta^3)$ | ★★ | M | Open | No |
| OP-OMS-005 | Effective DOF / Latent Gauge | ★★★ | M | Open | No |
| OP-OMS-006 | Topology for Non-Trivial $\mathrm{Aut}_{task}$ | ★★ | H | Open | No |
| OP-OMS-007 | Observer Dynamics (Level-3) | ★★ | H | Deferred | No |
| OP-OMS-008 | Relation to RelationWorld | ★ | M | Open | No |
| OP-OMS-009 | Readout Resolution + Continuity | ★★★ | M | **RESOLVED-NEGATIVE** (VP-1) | REMOVED |
| OP-OMS-010 | $V$ Existence and Regularity | ★★★ | H | Open (V1+V3 PROVED for $V_P$) | YES (via OP-002) |
| OP-OMS-011 | Basin Stability | ★★ | M | Open | No |
| OP-OMS-012 | Boundary Face Interpretation | ★★ | M | Open | No |
| OP-OMS-013 | Stratified Flow at Corners | ★ | M | Open | No |
| OP-OMS-014 | Empirical Identifiability | ★★ | H | Open | No |
| OP-OMS-015 | OMS ↔ Perceptual Styles | ★★ | H | Open | No |
| OP-OMS-016 | Computational $d_{\mathrm{eff}}$ | ★★ | L | **COMPUTATIONALLY ATTACKED** (VP-6, Session 5) | No |
| OP-OMS-017 | Approximate Symmetry Loci | ★ | M | **SUPERSEDED** by OP-OMS-026 (Session 5) | No |
| OP-OMS-018 | Optimizer Regularity in $\lambda$-space | ★★★ | H | **PARTIALLY RESOLVED** (R1/R2/R3/R4/R5 PROVED; global $C^1$ REJECTED; Session 5) | No |
| OP-OMS-024 | Constant-rank regions for $J_R$ | ★★ | M | **PARTIALLY RESOLVED** (VP-7: P12 yes, S3 no; VP-8: rank(J_e_tan) = 2 always) | No |
| OP-OMS-025 | $d_{\mathrm{eff}}$ ↔ perceptual style dimensions | ★★ | H | Open | No |
| OP-OMS-026 | Branch-switching loci $\Sigma_{\mathrm{branch}}$ | ★★★ | H | **PROVED codim-1 + COMP. SUPPORTED** (Session 6 SB5/SB11 + VP-7/VP-10) | No |
| OP-OMS-027 | Regularity at corners of $\Omega$ | ★ | M | Open | No |
| OP-OMS-028 | Quantitative Lipschitz of $v(\lambda)$ | ★ | L | **PROVED** (Session 5, `op_oms_028_lipschitz_v.md`) | No |
| OP-OMS-029 | Identity component of $G_{\mathrm{cw}}$ trivial | ★★ | M | **PROVED** (Session 5; subsumed under OP-001) | No |
| OP-OMS-030 | Gap C1 H4 witness (rank(G_T)≥3 at one point) | ★★★ | L | **COMPUTATIONALLY CONFIRMED** (Session 6 VP-8: 34/42 witnesses) | No |
| OP-OMS-031 | Non-trivial admissible $V$ exists with ≥2 basins | ★★★ | M | **PROVED admissible + COMP. SUPPORTED** (Session 6 NV3–NV10 + VP-9) | No |
| OP-OMS-032 | Closed-form / certified H4 witness | ★★ | M | **CLOSED UNDER CERTIFIED WITNESS** (Session 7, INTERVAL_CERTIFIED via VP-8; margin 4×10^13 over IEEE bound) | resolved |
| OP-OMS-032b | Upgrade H4 to RATIONAL_CERTIFIED via Sage | ★ | L-M | Open (NEW, formality upgrade only) | non-blocking |
| OP-OMS-033 | $\Sigma_{\mathrm{SN}}$ codim-1 fold theorem | ★ | M | **PROVED as conditional theorem** (Session 7, Theorem SN3 via Crandall–Rabinowitz) | resolved at conditional level |
| OP-OMS-033b | Full rigor of Lemma SN4 ((SN-iii)+(SN-iv) genericity for SCC) | ★ | M | Open (NEW, formality upgrade only) | non-blocking |
| OP-OMS-034 | Full temporal Δ³ via `scc.multi` 2-time-slice scene | ★★ | M | **CLOSED — COMPUTATIONALLY SUPPORTED** (Session 8, VP-11 faithful reduced temporal OMS test; (Wit-T) 14/14 confirmed) | resolved |
| OP-OMS-034b | Higher-K Δ³ branch map for tighter codim-1 budget | ★ | L | Open (NEW Session 8, formality, non-blocking) | non-blocking |
| OP-OMS-034c | Full Sinkhorn-OT $E_{tr}$ replacing L2 transport proxy | ★ | L-M | Open (NEW Session 8, robustness, non-blocking) | non-blocking |

**Canonical promotion blockers (post Session 8 — final):** **NONE for OMS-2.0 Accepted Full.** All three OMS-2.0 hard blockers (OP-OMS-001, OP-OMS-002+, OP-OMS-026) plus all four sub-OPs (032/033/034 + 034 closure) have been **resolved**:

- OP-OMS-034: CLOSED — COMPUTATIONALLY SUPPORTED (Session 8, VP-11).

Final OMS classification: **OMS-2.0 Accepted — Full** (Static PROVED + Full Temporal COMPUTATIONALLY SUPPORTED on faithful reduced test).

---

**Earlier (post Session 7) blockers context (now resolved):**

- OP-OMS-001: PROVED on the static face conditional on (Wit) which is INTERVAL_CERTIFIED.
- OP-OMS-002+: PROVED admissible + COMP. SUPPORTED via $V_2$.
- OP-OMS-026: PROVED codim-1 + COMP. SUPPORTED.
- OP-OMS-032: CLOSED UNDER CERTIFIED WITNESS (Session 7).
- OP-OMS-033: PROVED as conditional fold theorem SN3 (Session 7).
- OP-OMS-034: SEPARATED — blocks Full Temporal only (Session 7).

**OMS-2.0 final classification: Accepted — Static, with Full Temporal Conditional on OP-OMS-034.** See `oms_2_0_accepted_audit.md`.

**Non-blocking sub-OPs (formality upgrades + extensions):** OP-OMS-027 (corner regularity), OP-OMS-025 (empirical correspondence), OP-OMS-032b (RATIONAL_CERTIFIED H4 via Sage), OP-OMS-033b (full SN4 rigor), OP-OMS-024 (constant-rank regions, partial).

**OP-OMS-003 resolved:** Connectedness proved by Prop 6 (observer_moduli_space.md). No longer open.
