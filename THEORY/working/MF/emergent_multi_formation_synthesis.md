---
id: MF-synthesis-v1
type: working/synthesis
status: open — conceptual roadmap, no new promotions
created: 2026-05-06
session: Session U (W6 D4, 2026-05-06)
scope: emergent multi-formation from shared soft field; CV-1.10 state
related:
  - canonical.md §§3,5,13,16
  - theorem_status.md (all OP entries)
  - k_select_pf_equilibrium.md
  - k_select_obs_posterior.md
  - op_0009_pre_a_kfield_chart_validity.md
  - pf_a1_lions_sznitman_freidlin_route.md
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# Emergent Multi-Formation from a Shared Soft Field — Synthesis

**Purpose:** This document synthesizes all theorems established through CV-1.10 into a single theory-level narrative, identifies the complete dependency ladder from soft field to multi-formation, and maps the remaining gaps that prevent theoretical completeness. It does not promote new theorems and does not begin Package II.

**Session:** Session U (2026-05-06). State: 54A/13B/5C/5R = 77 claims, ~70% fully proved.

---

## §1. Central Thesis

**Multi-formation is not primitive. It emerges from a shared soft field.**

The core claim of the SCC framework is that multiple coherent formations — what common sense calls "objects" in a scene — are not posited from the outset. They are not a collection of pre-individuated entities whose interactions must then be modeled. They arise as the observable structure of a single continuous soft cohesion field over a shared support space.

Formal statement:

$$u \in \mathcal{F}_M(\mathcal{P}) = \{u \in [0,1]^n : \mu^T u = M\}$$

The multi-formation structure is the derived partition:

$$\mathrm{MF}(u) = \mathrm{PersComp}_{\rho_\mathrm{pers},\tau}(u)$$

The formation count is the derived observable:

$$K_\mathrm{act}(u) = |\mathrm{MF}(u)|$$

**Key interpretive commitments:**

- $K$ is derived from $u$, not assumed. The theory does not know the number of formations before analyzing the field. K_act is an output, not an input.
- $\Sigma_M^K = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$ is a local coordinate chart within an energy basin $\mathcal{B}_K$, not the foundational state space. The foundational object is $\mathcal{F}_M(\mathcal{P})$.
- Formation identity begins as persistent-component identity. A "formation" is not a label, an instance ID, or a bounding box. It is a maximally cohesive connected region of the soft field that persists under threshold perturbation.
- Spatial objecthood (persistent, bounded, cohesive component) is established. Full temporal objecthood (identity across time steps) is not yet established. This is the primary remaining gap.

---

## §2. The Theorem Ladder

The following theorems establish the chain from raw relational support to observation-conditioned multi-formation K-selection.

| # | Object / Claim | Theorem(s) | Status | Role in ladder |
|---|---|---|---|---|
| 1 | Stereo-visible support $\mathcal{P}_t$ | D-ST-1 (left support), D-ST-2 (right), D-ST-3 (stereo product), D-ST-4 (depth + disparity) | Cat B candidates | Defines the domain $\mathcal{P}_t$ on which $u_t$ lives |
| 2 | Field state space $\mathcal{F}_M(\mathcal{P})$ | T-PF-A1-AR | **Cat A** | F_M(G) is compact convex polytope; $\sigma_M$ well-defined; affine isometry to bounded convex body in $\mathbb{R}^{n-1}$ |
| 3 | Boundary precision $B_\mathrm{PersRidge} \approx \partial\mathrm{PersComp}$ | T-OP6-B | **Cat A conditional** (H1–H5) | Crisp boundary approximation: $d_H(B_\mathrm{PersRidge}, \partial\mathrm{PersComp}) \leq 2(\alpha/\beta)^{1/2}$ in phase-separated regime |
| 4 | Stereo hard-depth topological locking: $G^\mathcal{P} = G_1 \sqcup G_2$ | T-ST-5a | **Cat A** | Hard depth discontinuity implies topological separation → K_act ≥ 2 forced; formation boundary = depth edge |
| 5 | Smooth-depth barrier raising | T-ST-5b | **Cat B** | Smooth depth transition raises SCC barrier → two-formation minimum is stable even without hard disconnection |
| 6 | Reflected stochastic dynamics on $\mathcal{F}_M(\mathcal{P})$ | T-PF-A1-SDE | **Cat A** | Lions-Sznitman 1984 reflected SDE well-posed; strong solution unique |
| 7 | Gibbs equilibrium measure | T-PF-A1-GI | **Cat A** | $\pi_{T_*}(du) = Z^{-1}e^{-E/T_*}d\sigma_M$ is the unique invariant; $\pi_{T_*} \ll \sigma_M$ |
| 8 | Exponential ergodicity | T-PF-A1-PE | **Cat A** | Spectral gap $\lambda_1 > 0$ (Payne-Weinberger for convex polytopes); $L^2 \to TV$ convergence |
| 9 | Equilibrium K-selection | T-K-Select-PF | **Cat B canonical** (CV-1.10) | $p_K = \pi_{T_*}(\mathcal{B}_K)$ is the equilibrium K-distribution; $K^* \in \arg\min_K F(K;\mathcal{P})$ |
| 10 | Observation-conditioned K-selection | T-K-Select-OBS | **working Cat B candidate** (Sessions S/T) | Posterior $p_K(\mathfrak{O}_t) = \pi_t^{obs}(\mathcal{B}_K)$; observation shifts K-distribution toward evidence-consistent K |
| — | Smooth-depth Gibbs continuity | T-P-F-ε0 | **Cat A** | Gibbs measure continuous in $\varepsilon$ (stereo depth perturbation); no phase transition in $\varepsilon$ |
| — | Kramers exponent stability | T-P-F-ε0-K | **Cat B** | Exponent $\Delta\mathcal{E}_\varepsilon = \Delta\mathcal{E}_0 + O(\varepsilon)$; conditional on H5 Morse |
| — | Persistence: two-step | T-Persist-1 | **Cat A** (partial: sub-items a,b,c,e Cat A; d Cat C) | Cohesion fingerprint OT transport; two-step formation tracking |
| — | Active-count bridge | T-L1-F, T-L1-M | **Cat A conditional** (L1-J regime) | Under strong hypothesis package: $K_\mathrm{bar} = K_\mathrm{act}$; useful as persistence diagnostic |

**Summary of coverage:** The ladder is complete from support definition through stochastic dynamics to equilibrium K-selection with and without observation evidence. The primary missing rung is the temporal segment: no theorem yet establishes how a formation at time $t$ is identified with a formation at time $t+1$.

---

## §3. What "Formation" Currently Means

The theory currently supports the following concept of a formation object:

$$\mathfrak{F}_i(u) = (C_i,\; \partial C_i,\; K_i,\; \sigma_i^?)$$

**Components:**

- $C_i \in \mathrm{MF}(u) = \mathrm{PersComp}(u;\rho_\mathrm{pers},\tau)$: the $i$-th persistent connected component of the soft field $u$. Well-defined by D-ST-3 / canonical §3.11.
- $\partial C_i \approx B_\mathrm{PersRidge} \cap \bar{C}_i$: the crisp boundary approximation, established by T-OP6-B (Cat A conditional) within $d_H \leq 2(\alpha/\beta)^{1/2}$. Requires H1–H5 (phase separation, boundary regularity, etc.).
- $K_i$: the count of components; derived from $u$ via $K_\mathrm{act}(u) = |\mathrm{MF}(u)|$.
- $\sigma_i^?$: the σ-signature — a spectral fingerprint of the formation's internal structure. Formally defined (T-Commitment-14-Multi-Static, canonical D-6a), but its dynamics under K-jumps are NOT fully integrated. OP-0008 governs how $\sigma_i$ transforms when two formations merge or split.

**What is established:** Spatial objecthood. A formation is a maximal cohesive persistent region with crisp boundary, characterized by a spectral fingerprint. These properties are graded (not binary), derived from $u$, and stable under bounded perturbation.

**What is NOT yet established:** Full temporal objecthood.

The theory cannot yet answer: if $\mathfrak{F}_i(u_t)$ is a formation at time $t$ and $\mathfrak{F}_j(u_{t+1})$ is a formation at time $t+1$, under what conditions are they "the same formation"? The persistence theorems (T-Persist-1 two-step, T-Persist-K-Unified) use OT-based fingerprint matching as a proxy, but:

1. The transport kernel $M_{t \to s}$ is not uniquely determined (OP-0011).
2. Long-chain persistence composition is Cat C (OP-0012, T-Persist-Full).
3. K-jump events (formation birth, death, merge, split) require a separate K-jump transition theory — not yet established.

**Current state of temporal objecthood:** Approximately correct for short time windows with stable K. Formally incomplete.

---

## §4. What Is Still Missing — Gap Table

| Missing layer | Related OP | Why it matters | Current status |
|---|---|---|---|
| **Temporal identity** | OP-0011 (transport kernel), OP-0012 (persistence composition) | Without it, formations cannot be tracked across time; the "same formation" concept is informal | TENTATIVE (OP-0011) / OPEN (OP-0012); T-Persist-1 covers two-step but not multi-step |
| **σ-signature inheritance at K-jumps** | OP-0008 | When K_act changes (merge/split), how does $\sigma_i$ transform? Current static theory is silent on this; dynamic formation description incomplete | OPEN; Path B (σ-rich + Φ-rich) Cat B target; Commitment 18 candidate |
| **Dynamic K-transition (Kramers)** | OP-0005-DYN | What is the rate at which the system transitions from K-sector to (K±1)-sector? Eyring-Kramers formula requires H5 Morse stability + T_* registration | OPEN; Package II conditional on OP-0021 + H5; W9+ |
| **Observation likelihood canonicalization** | OP-0005-OBS | T-K-Select-OBS is complete given LM1–LM3, but which specific likelihood model (photometric, depth, flow) is canonical? | STRUCTURED (Cat B candidate); exp54 validation needed; Cat A path: canonicalize Phi_obs |
| **K-field architecture migration** | OP-0009 | Full formal migration from K-field Σ_M^K to F_M(G) primary + K-field chart secondary; v2.0 §1 amendment; 7 sub-items | PARTIALLY ADDRESSED; 1/7 resolved (OP-0009-K via Commitment 16); full resolution W11–W12 |
| **Semantic / affordance formation structure** | (not yet an OP) | Formations in the current theory are purely spatial-cohesive; no affordance (graspable, walkable), no categorical label, no semantic embedding. What is the relation between SCC formation and semantic scene understanding? | Not yet registered; beyond current theory scope |
| **Code migration: K-field → shared-field** | OP-0009 | Current `multi.py` uses K-field initialization; foundational compute should use F_M(G) projected dynamics with K_act measurement post-hoc | OPEN; V1–V4 validity conditions formalized (op_0009_pre_a); experimental comparison exp02d documents V3 failure |
| **T_* registration** | OP-0021 | T_* appears in every stochastic claim (SDE, Gibbs, Kramers) but is axiomatic; no derivation from SCC parameters or physical quantities | OPEN; W9+; needed before Package II |
| **Non-convex topology** | (not yet registered) | All P-F-A1 theorems assume convex domain F_M(G); non-convex topologies (mesh, partial observability) require separate treatment | Not registered; long-term |
| **Continuous-space limit** | (not yet registered) | SCC is defined on finite graphs; the infinite-graph or continuum limit is not established | Not registered; very long-term |

---

## §5. Formation Life-Cycle Proposal

The following life-cycle is a conceptual roadmap, not a proved theorem. It maps each phase to the mathematical objects available in the current theory.

| Phase | Description | Mathematical object | Theory coverage | Status |
|---|---|---|---|---|
| 1. **Latent fluctuation** | Field $u_t$ explores $\mathcal{F}_M(\mathcal{P})$ ergodically without cohering into persistent components | Langevin SDE on $\mathcal{F}_M(\mathcal{P})$; $U_t$ not in any $\mathcal{B}_K$ with $K > 0$, or in $\mathcal{B}_0$ | T-PF-A1-SDE + T-PF-A1-GI | Stochastic dynamics established; $\mathcal{B}_0$ characterization not explicitly proved |
| 2. **Nucleation** | Field crosses into $\mathcal{B}_K$ for some $K \geq 1$; first formation appears | K-sector crossing: $K_\mathrm{act}(U_t) = 0 \to 1$ | T-K-Select-PF gives equilibrium probability; crossing rate = Package II (OP-0005-DYN) | Rate OPEN; existence established |
| 3. **Component persistence** | $K_\mathrm{act}$ stable; field resides in $\mathcal{B}_K$; formation coheres | $U_t$ trajectory within $\mathcal{B}_K$; V1 (K-stability) satisfied | T-K-Select-PF (equilibrium stay probability); T-Persist-1 (two-step tracking) | Two-step established; multi-step Cat C |
| 4. **Boundary sharpening** | Transition zone between core and exterior narrows; $d_H(B_\mathrm{PersRidge}, \partial C_i) \leq 2(\alpha/\beta)^{1/2}$ | T-OP6-B: PersRidge boundary coincides with component boundary | **Cat A conditional** (H1–H5) | Established |
| 5. **Depth-stabilization** | Hard depth discontinuity locks topological separation: $G^\mathcal{P} = G_1 \sqcup G_2$ | T-ST-5a: depth edge forces $K_\mathrm{act} \geq 2$ | **Cat A** | Established |
| 6. **Smooth barrier stabilization** | Smooth depth gradient raises barrier between K-sectors | T-ST-5b: barrier height increases monotone in $\Delta z / \lambda_z$ | **Cat B** (monotonicity not yet proved) | Narrow claim established |
| 7. **Equilibrium K-selection** | System settles to equilibrium K-count distribution $\{p_K\}$ | T-K-Select-PF: $p_K = \pi_{T_*}(\mathcal{B}_K)$; $K^* = \arg\min_K F(K;\mathcal{P})$ | **Cat B canonical** | Established |
| 8. **Observation-conditioned selection** | Scene observation $\mathfrak{O}_t$ shifts K-distribution to posterior $\{p_K(\mathfrak{O}_t)\}$ | T-K-Select-OBS: posterior Gibbs re-weighting | **Working Cat B candidate** | Mathematical structure complete; needs exp54 + likelihood canonicalization |
| 9. **Formation interaction** | Two formations interact: boundary overlap, mass sharing | Binding/separation energy in $E_\mathrm{SCC}$; $E_\mathrm{sep}$ quantifies separation | Covered by energy functional; no interaction theorem | Not formalized as theorem |
| 10. **Merge / split (K-jump)** | Formation count changes: $K_\mathrm{act}(t) \to K_\mathrm{act}(t+1) = K \pm 1$ | Sector crossing $\mathcal{B}_K \to \mathcal{B}_{K\pm 1}$; Kramers rate OP-0005-DYN | Crossing rate OPEN (Package II); σ-transformation OPEN (OP-0008) | Both OPEN |
| 11. **σ-update** | After merge/split, spectral signature $\sigma_i$ must be updated for new K | σ-inheritance at K-jump: OP-0008 | OPEN; Path B Cat B target | OPEN |
| 12. **Temporal identity** | Formation identity assigned across time: $\mathfrak{F}_i(u_t) \equiv \mathfrak{F}_j(u_{t+1})$ | Transport-based fingerprint matching (T-Persist-1 two-step); but uniqueness gap (OP-0011) | Two-step Cat A (partial); multi-step Cat C (OP-0012) | Partial |
| 13. **Death** | Formation mass → 0; component vanishes from $\mathrm{PersComp}$ | $m_i \to 0$; $C_i$ leaves $\mathrm{MF}(u)$; $K_\mathrm{act}$ decreases | T-K-Select-PF implies equilibrium probability of $K < K_\mathrm{act}$; actual death event = K-jump | Existence established; dynamics OPEN |

---

## §6. Future Synthesis Theorem Candidate

**T-MF-Synthesis — Emergent Multi-Formation from Shared Soft Field**

*(Conceptual candidate. Not promoted. Dependencies not all established. Cat B/A target after listed dependencies are all canonical.)*

**Informal statement:** Under standard finite graph support, four-term SCC energy, P-F-A1 Package I, PersComp extraction, and boundary precision assumptions, a soft field $u \in \mathcal{F}_M(\mathcal{P})$ induces a well-defined finite multi-formation object $\mathrm{MF}(u)$ with the following jointly established properties:

(i) **Field grounding.** $u \in \mathcal{F}_M(\mathcal{P})$ is a compact convex polytope (T-PF-A1-AR Cat A).
(ii) **Boundary precision.** Each component $C_i \in \mathrm{MF}(u)$ has crisp boundary: $d_H(B_\mathrm{PersRidge}(C_i), \partial C_i) \leq 2(\alpha/\beta)^{1/2}$ (T-OP6-B Cat A conditional).
(iii) **Hard-depth topological locking.** If $\mathcal{P}$ has depth discontinuity, $G^\mathcal{P} = G_1 \sqcup G_2$ and $K_\mathrm{act} \geq 2$ (T-ST-5a Cat A).
(iv) **Stochastic dynamics grounded.** Reflected Langevin SDE on $\mathcal{F}_M(\mathcal{P})$ is well-posed and ergodic (T-PF-A1-SDE, T-PF-A1-GI, T-PF-A1-PE all Cat A).
(v) **Equilibrium K-selection.** Equilibrium K-distribution $\{p_K\}$ is the Gibbs sector mass (T-K-Select-PF Cat B canonical).
(vi) **Observation-conditioned K-selection.** Bayesian posterior $\{p_K(\mathfrak{O}_t)\}$ updates K-distribution given scene evidence (T-K-Select-OBS working Cat B).

**Expected canonical status:** Cat B after all dependencies are canonical. Cat A after temporal identity + σ-inheritance are proved.

**Dependencies:**
- T-OP6-B Cat A conditional (H1–H5)
- T-ST-5a Cat A
- T-ST-5b Cat B (barrier raising; Cat A requires monotonicity)
- T-PF-A1-AR / SDE / GI / PE all Cat A (P-F-A1 Package I)
- T-K-Select-PF Cat B canonical
- T-K-Select-OBS (Cat B working → needs canonicalization)
- *Future: T-Temporal-Identity Cat A (temporal objecthood; currently OPEN)*
- *Future: T-σ-Inherit Cat B/A (σ at K-jump; OP-0008)*

**What T-MF-Synthesis would unify:** The claim that all these individually proved theorems together constitute a rigorous theory of emergent multi-formation. The synthesis theorem is itself a statement that the parts cohere into a whole — not a new mathematical result but a formal joint statement.

---

## §7. Relation to K-Field Architecture

The K-field product space $\Sigma_M^K = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$ is a useful and computationally valuable object. It is NOT, however, the foundational state space of the theory.

**Correct architectural picture:**

$$\text{Foundational: } \mathcal{F}_M(\mathcal{P}) \supset \mathcal{B}_K \approx \text{chart via } \Sigma_M^K$$

The K-field chart is a local coordinate system on the energy basin $\mathcal{A}_{K,\alpha}(\mathcal{P}) \subset \mathcal{B}_K$. It is valid as long as four conditions hold (V1–V4 from `op_0009_pre_a_kfield_chart_validity.md`):

| Condition | Statement | Failure mode |
|---|---|---|
| **V1 (K-Stability)** | $K_\mathrm{act}(U_t) = K$ throughout time interval | Near K-jump: chart degenerates; switch to (K±1)-field chart required |
| **V2 (Basin Localization)** | Trajectory stays in single basin $\mathcal{A}_{K,\alpha}$ | Inter-basin transition: formation labeling must update |
| **V3 (Formation Separation)** | Formations well-separated: no significant overlap $\langle u^{(j)}, u^{(k)}\rangle \approx 0$ | High overlap: participation constraint binds; product structure lost; chart non-invertible |
| **V4 (Mass Budget)** | Each $m_j > 0$ bounded away from 0 | Formation death: $m_j \to 0$; chart dimension degenerates |

**Empirical evidence for V3 failure:** exp02d (12×12 grid, $\beta=20$, $\lambda_\mathrm{rep}=10$) documented K-field endpoint inconsistency with F_M(G) local minima. The K-field energy minimum $\tilde{u}_A$ (with repulsion term) is NOT an F_M(G) local minimum under pure SCC energy. This is a concrete case of V3 violation.

**Recommended practice:** Compute K-field fields as initialization only. Validate final endpoint via single-field gradient descent on $\mathcal{F}_M(\mathcal{P})$. Use K-field chart for K_act statistics and σ-signature computation (where V1–V4 are typically satisfied in the stable-K regime), but not for barrier heights or endpoint claims.

**Architecture migration status:** OPEN (OP-0009). Full canonical migration of §1 "formal universe" paragraph (which uses K-field as I9 architectural commitment) requires v2.0 amendment. Computational code (`multi.py`) uses K-field initialization — migration to single-field projected dynamics with K_act post-measurement is the target state.

---

## §8. Next Theory Priorities

The following sequence is recommended based on dependency analysis and impact on theoretical completeness.

### Priority 1: Temporal Identity / PersComp Transport

**Why first:** It is the largest single gap in the theory. The life-cycle phases 10–13 (K-jump, σ-update, temporal identity, death) all depend on a rigorous temporal identity theorem. Without it, multi-formation is a static spatial concept only.

**Mathematical target:** Define a temporal identity relation $\sim_{t \to s}$ on $\mathrm{PersComp}$ such that:
1. $C_i(u_t) \sim_{t \to s} C_j(u_s)$ iff the formation at time $t$ is identified with formation $j$ at time $s$.
2. $\sim_{t \to s}$ is derived from the transport kernel $M_{t \to s}$ (entropy-regularized OT).
3. Composition: $\sim_{t \to s} \circ \sim_{s \to r} \approx \sim_{t \to r}$ (currently Cat C, OP-0012).

**Blocker:** OP-0011 (transport kernel uniqueness). Until the correct transport kernel is specified, the identity relation is not unique. Path: prove that any kernel satisfying axioms E1–E5 gives the same coarse-grained identity → uniqueness up to relabeling.

**Deliverable:** T-Temporal-Identity Cat B candidate in `working/MF/temporal_identity.md`.

### Priority 2: σ-Inheritance at K-Jumps (OP-0008)

**Why second:** σ-signature is the formation's spectral fingerprint. For a complete formation description $\mathfrak{F}_i = (C_i, \partial C_i, K_i, \sigma_i)$, we need to know how $\sigma_i$ transforms at merge/split events. This is Path B of OP-0008 (σ-rich + Φ-rich Cat B target).

**Mathematical target:** Given $K_\mathrm{act}(u_t) = 2 \to K_\mathrm{act}(u_{t+\delta}) = 1$ (merge event), define $\sigma_\mathrm{merged}$ from $(\sigma_1, \sigma_2)$. Prove continuity/measurability of the inheritance map.

**Deliverable:** T-σ-Inherit Cat B candidate.

### Priority 3: T-K-Select-OBS → Cat B Canonical

**Why third:** The mathematical structure is complete (Sessions S/T). The remaining step is:
1. Canonicalize a specific likelihood model $\mathcal{L}_\mathrm{obs}$ (photometric or operator form).
2. Run exp54 (Method A MCMC + Method B sector MAP) to validate.
3. Promote T-K-Select-OBS to canonical Cat B.

This is the most immediately achievable milestone.

**Deliverable:** exp54 implementation; T-K-Select-OBS → canonical Cat B in CV-1.11.

### Priority 4: Package II Conditional Start

**After OP-0021:** P-F-A1 Package II (Eyring-Kramers, Freidlin-Wentzell quasipotential) requires:
- H5 Morse stability (saddle structure of $E_\mathrm{SCC}$ between basins)
- T_* registration (OP-0021)

Do not start Package II until T_* is canonically defined. Once OP-0021 is resolved, Package II enables OP-0005-DYN (dynamical K-transition rates) and completes the stochastic formation dynamics ladder.

**Deliverable:** T_* registration working file; Package II proof sketch conditional on H5 + registered T_*.

### Priority 5: OP-0009 v2.0 Migration

**Long-term:** Full canonical migration of multi-formation architecture from I9 (K-field as primary) to F_M(G)-primary + K-field-as-chart. This is a §1 formal universe amendment at v2.0 (W11–W12). Requires resolving all 7 OP-0009 sub-items.

Current state: 1/7 resolved (OP-0009-K); 7/7 partially addressed.

---

## §9. Consolidated State Assessment

**What the theory has achieved through CV-1.10:**

The SCC framework now has a complete stochastic grounding for the soft cohesion field. The field lives on a compact convex polytope, evolves according to a well-posed reflected Langevin SDE, reaches a unique Gibbs equilibrium, and that equilibrium assigns each K-value a well-defined probability. With scene observations, the Gibbs measure can be conditioned into a posterior. Spatial formation boundaries are crisp to within $2(\alpha/\beta)^{1/2}$ in phase-separated regimes. Hard depth discontinuities force topological separation. Smooth depth transitions stabilize multi-formation configurations.

**What the theory has not achieved:**

The temporal dimension is fragile. Two-step persistence is Cat A (partial). Multi-step composition is Cat C. K-jump dynamics have no rate theorem. σ-signatures are static (K-stable regime only). Semantic structure is entirely outside scope.

**Summary:** The theory has a rigorous, self-consistent static + equilibrium multi-formation theory. The dynamic, temporal, and semantic layers are the remaining frontier.

---

**End of emergent_multi_formation_synthesis.md.**

**Status:** Working document. No new theorems promoted. Gap table is definitive as of CV-1.10. Synthesis theorem T-MF-Synthesis is a future candidate only.
