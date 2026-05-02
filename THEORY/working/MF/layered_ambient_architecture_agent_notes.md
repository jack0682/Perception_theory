# Layered Ambient-State Architecture — Agent Notes

**File:** `THEORY/working/MF/layered_ambient_architecture_agent_notes.md`
**Audience:** Future agents (Claude Code sessions, sub-tasks, downstream work) operating on the SCC / Multi-Formation theory along the layered ambient-state line.
**Purpose:** Guardrails. Read this file before doing any new work in this line. The intent is to prevent overclaim, conflation, and silent canonical drift.

**Companion docs:** `layered_ambient_architecture_README.md`, `layered_ambient_architecture_candidate.md`, `layered_ambient_architecture_next_work.md`.

---

## 1. Mandatory distinctions

Each of these distinctions is load-bearing. Confusing the two sides of any line will produce wrong statements.

### 1.1 Three K-notions are not interchangeable

$$
K_{\mathrm{field}} \;\ne\; K_{\mathrm{act}}^\varepsilon \;\ne\; K_{\mathrm{soft}}^\phi.
$$

- $K_{\mathrm{field}}$ is an integer parameter set externally (architectural cap).
- $K_{\mathrm{act}}^\varepsilon$ is an integer-valued labelled, threshold-gated *count diagnostic* on a Layer II state.
- $K_{\mathrm{soft}}^\phi$ is a real-valued unlabelled *topological soft count* from $H_0$ persistence of a single field.

Inequality is the default. Equality is a *bridge lemma* claim, only available under explicit well-separated hypotheses, with explicit error term, and only computed downstream (work package WQ-2).

### 1.2 Three ambients are not interchangeable

$$
\Sigma_m(G_t) \;\ne\; \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t) \;\ne\; \Sigma_M^A(\mathbf m_A; G_t).
$$

- $\Sigma_m(G_t)$ is the Layer I primitive single-field ambient. Canonical theorem-grade. Single-formation only.
- $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ is the Layer II shared-pool multi-formation ambient. Working-definition safe. Hosts variable active count and K-jump events.
- $\Sigma_M^A(\mathbf m_A; G_t)$ is the Layer III occupancy-constrained fixed-mass slice. Working-definition safe. Subset of Layer II. Smooth-segment, fixed-K, fixed-mass scope.

Statements about Layer III do not automatically lift to Layer II. Statements about $\Sigma_m$ do not automatically lift to multi-formation by replacing $u$ with $\mathbf u$.

### 1.3 Operational ε-active regions are not Whitney strata

$\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$ are operational ε-active regions: working-definition safe as labelled regions, but not yet verified Whitney-stratified. The Whitney verification in `mathematical_scaffolding_4tools.md` §2.2 is for the *intrinsic*-count stratification $\{S_{K_{\mathrm{act}}}\}$, which is a coarser object.

If a future statement requires Whitney structure on the cell refinement, the stratifiability feasibility check (work package WQ-5) must be completed first.

The word "cell" used here is **memo-internal operational** — a labelled region indexed by an active set $A$. It is not a CW-complex cell, not a Morse-Smale cell, not a chamber of a hyperplane arrangement.

### 1.4 Fixed-mass slices are not global lifecycle ambients

$\Sigma_M^A(\mathbf m_A; G_t)$ cannot host a K-jump by definition: the active set $A$ and per-formation masses $\mathbf m_A$ are fixed.

Any "long-time dynamics" or "lifecycle" statement that varies the active count must be made on Layer II, not on a Layer III slice.

### 1.5 σ-standard incompleteness is a precondition for σ-rich sufficiency claims

σ-rich is a candidate *augmentation* of σ-standard. It is meaningful to claim σ-rich is sufficient only after σ-standard has been *demonstrated* insufficient. NQ-242c (work package WQ-1) is the demonstration. Reversing the order — claiming σ-rich is sufficient first, then citing σ-standard non-determinism as motivation — produces an unmotivated and overclaiming sequence.

### 1.6 Fixed-mass slice is not the unconstrained product

$\Sigma_M^A(\mathbf m_A; G_t)$ is an *occupancy-constrained* subset of Layer II. It is **not** the unconstrained product $\prod_{j \in A} \Sigma_{m_j}(G_t)$, which admits configurations violating the simplex constraint $\sum_j u^{(j)}(x) \le 1$. Substituting the unconstrained product silently drops Layer II's defining inequality.

---

## 2. Forbidden overclaims

Each of these is a specific overclaim that prior working sessions have skirted. Do not make any of them.

| # | Forbidden overclaim | Why forbidden |
|---|---|---|
| 1 | "$K_{\mathrm{soft}} = K_{\mathrm{act}}$" | Different ontological layers; divergence in overlap and corner-saturated regimes; bridge is a lemma with hypotheses, not an identity |
| 2 | "σ-rich solves K-jumps" | σ-rich global sufficiency requires (R1)–(R4) of `nq242c_explicit_construction.md` §6.2; only local numerical anchors exist (and only post-WQ-1) |
| 3 | "K-selection is resolved" | OP-0005 is HIGH severity OPEN; partial via σ-framework + CN15 + Commitment 16 only; full mechanism is a downstream comparison |
| 4 | "Stratified Morse is established" | Goresky-MacPherson framework is named, not applied; SCC energy needs Morse-Bott handling; NQ-248 is W7+ downstream |
| 5 | "Layer II is globally smooth" | Layer II carries at minimum the count stratification; cell refinement is finer-singular |
| 6 | "Active-set cells $\{S_A^\varepsilon\}$ are Whitney strata" | Whitney verification is for intrinsic-count strata only; cell stratifiability is open (WQ-5) |
| 7 | "Vision / robotics implementation is validated" | No application claim is made by the architecture; vision_model_sketch/ remains explicit future work |
| 8 | "I9 is superseded by I9'" | I9 is reread as a Layer III slice; both inhabit the same scaffold; no canonical edit is performed |
| 9 | "K-jump σ-inheritance is deterministic" | Lemma 4.4.1(c) of `sigma_multi_trajectory.md` is Cat C conjectured non-deterministic; explicit counterexample is open (NQ-242c) |
| 10 | "OP-0003 MO-1 is resolved" | MO-1 is SIDESTEPPED at single-formation; multi-formation re-activation rider is preserved; no resolution claim |
| 11 | "$\{S_r^\varepsilon\} = \{S_{K_{\mathrm{act}}}\}$" | $\{S_r^\varepsilon\}$ is the labelled-cell-collapsing union; $\{S_{K_{\mathrm{act}}}\}$ is the intrinsic-count stratification of `mathematical_scaffolding_4tools.md` §2.2; they coincide *as sets* but only the latter is Whitney-verified |
| 12 | "σ-standard is sufficient" | Path B framework asserts (and NQ-242c targets to confirm) σ-standard incompleteness |
| 13 | "Commitment 16 K-status decomposition resolves K-Selection" | Commitment 16 frames *what* K is; OP-0005 asks *what selects* K; these are different questions |
| 14 | "K-jump events are codim-1 transitions" | Codim-1 holds for *single-merger* events on the *count* stratification; multi-merger and cell-level codim are not asserted |

---

## 3. Safe terminology

Use these terms in working files in this line.

| Safe term | Meaning |
|---|---|
| **Layer I / Layer II / Layer III** | The three layers of the architecture |
| **primitive single-field ambient** | $\Sigma_m(G_t)$ |
| **shared-pool multi-formation ambient** | $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ |
| **fixed-mass smooth local slice** | $\Sigma_M^A(\mathbf m_A; G_t)$ |
| **occupancy-constrained subset** | The way the slice sits inside Layer II |
| **architectural cap** | $K_{\mathrm{field}}$ |
| **active count** / **active count diagnostic** | $K_{\mathrm{act}}^\varepsilon$ |
| **soft count** / **persistence-based soft count** | $K_{\mathrm{soft}}^\phi$ |
| **aggregate projection** / **aggregate field** | $U(\mathbf u) \in \Sigma_M(G_t)$ |
| **active-set cell** | $S_A^\varepsilon$, with a note that "cell" is operational |
| **operational ε-active region** | $S_A^\varepsilon$ or $S_r^\varepsilon$ |
| **count-only stratification** | $\{S_{K_{\mathrm{act}}}\}$ of `mathematical_scaffolding_4tools.md` §2.2 (Whitney-verified) |
| **K-jump event** / **K-jump time** | A trajectory time $t^*$ at which $K_{\mathrm{act}}^\varepsilon$ strictly drops |
| **smooth segment** | Maximal open interval on which $K_{\mathrm{act}}^\varepsilon$ is constant |
| **well-separated regime** | $(\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min})$ hypotheses of `..._candidate.md` §9.1 |
| **overlap regime** | Active mass holds; one or more of the well-separation hypotheses fails |
| **corner-saturated regime** | Mass-boundary, field-boundary, or simplex-saturation |
| **bridge lemma** | An approximation statement with explicit hypotheses and explicit error term |
| **non-canonical commitment candidate** | This memo's status; not canonical, no Commitment number |
| **promotion target** | The CV-x.y release at which a working object might be promoted to canonical |
| **status: working-definition safe** | Definition is precise; not promoted to canonical |
| **status: theorem-grade under existing hypotheses** | Proved under stated hypotheses (Cat B / Cat C target) |
| **status: conjectural / downstream** | Open, attacked by a downstream work package |

---

## 4. Unsafe terminology

Avoid these terms — they invite the conflations of §1 or smuggle the overclaims of §2.

| Unsafe term | Why unsafe | Use instead |
|---|---|---|
| "K" (bare) | Ambiguous between $K_{\mathrm{field}}$, $K_{\mathrm{act}}^\varepsilon$, $K_{\mathrm{soft}}^\phi$ | Specify which |
| "the K manifold" / "the K-field manifold" without scope | Ambiguous between Layer II, Layer III, intrinsic stratum | Specify the layer / stratum |
| "stratum" applied to $S_A^\varepsilon$ or $S_r^\varepsilon$ | Suggests Whitney-verified | "operational ε-active region" or "cell" with operational caveat |
| "Whitney" applied to cell refinement | Verification is for count-only stratification | "Whitney-verified count stratification" only |
| "global smoothness" / "global manifold structure" of Layer II | False | "smooth on the interior of $S_{K_{\mathrm{act}}}$" |
| "transient K-field" / "K-field is transient" | Misleading shorthand for stratum traversal | "trajectory crosses cell / stratum boundaries; K-field as Layer III slice does not capture inter-stratum transitions" |
| "σ resolves multi-formation" | Vague; conflates static σ-multi-A (Cat A def) and dynamic σ-multi-A(t) (Cat B target) | Distinguish static / dynamic; specify Cat |
| "the architecture is canonical" | This memo is non-canonical | "non-canonical commitment candidate" |
| "Commitment 17" / "Commitment 18" without "candidate" qualifier | Implies canonical assignment that has not happened | "candidate Commitment text in OAT-supplementary §8.1" |
| "rich-σ proves determinism" | Determinism is conjectural / downstream | "rich-σ predicts determinism on the NQ-242c construction; global determinism is open" |
| "stratified Morse applies" without verification context | Goresky-MacPherson framework named, not applied | "Goresky-MacPherson stratified Morse is the natural future framework (NQ-248 W7+)" |
| "K-selection mechanism" without Cat-marker | OP-0005 is open; mechanisms are Cat C candidates | "K-selection candidate (a) / (b) / (c) per `k_selection_mechanism.md`" |
| "vision-ready" / "control-ready" / "engineering-ready" | No application claim is made | "theory-side discipline; application bridges remain future work" |
| "soft K = active K" | Forbidden non-claim | "bridge lemma under well-separated hypotheses with error term" |
| "fixed-K slice" without smooth-segment scope | Leaks Layer III result onto Layer II dynamics | "Layer III, smooth-segment scope" |
| "shared-pool replaces K-field" | Wrong; both inhabit the scaffold | "K-field is a Layer III reading; shared-pool is the Layer II ambient" |

---

## 5. Files to inspect before modifying this line of work

Inspect in this order. Highest-priority files are read fully; the rest are reference.

### 5.1 Mandatory before any new work

1. `THEORY/canonical/canonical.md` (CV-1.5.1) — current canonical baseline; especially §3 (formal universe), §11 (Commitments and Open Design Choices), §13 (theorem catalog including T-Persist-K-* and D-6a entries), §14 (CN list).
2. `THEORY/canonical/open_problems.md` — current OP register, especially OP-0001..0003 (resolved/clarified/sidestepped status), OP-0005 (K-Selection HIGH), OP-0008 (σ^A K-jump non-determinism), OP-0009 (Multi-Formation Ontological Foundations, 7 sub-items).
3. `THEORY/canonical/theorem_status.md` — current Cat A / B / C registry, version history.
4. `THEORY/working/MF/layered_ambient_architecture_candidate.md` — full architecture definitions and status table.
5. `THEORY/working/MF/layered_ambient_architecture_README.md` — architecture orientation.
6. `THEORY/working/MF/K_status_commitment.md` (OAT-1) — Commitment 16 K-status decomposition (CV-1.5.1).
7. `THEORY/working/MF/shared_pool_canonical_proposal.md` (OAT-4) — I9' shared-pool proposal; Whitney verification reference.
8. `THEORY/working/MF/mathematical_scaffolding_4tools.md` (OAT-supplementary) — Tool A1 / A2 / A3 / A4 verification, with Tool A4 partial fail honest acknowledgment.

### 5.2 For dynamic σ-multi work

9. `THEORY/working/MF/sigma_multi_trajectory.md` — D-6b dynamic framework, Lemma 4.4.1(c) Cat C non-determinism, FM1–FM4 known failure modes.
10. `THEORY/working/MF/multi_formation_sigma.md` — D-6a static framework.
11. `THEORY/working/MF/sigma_rich_augmentation.md` — Path B framework, σ-rich definition, Φ_rich.
12. `THEORY/working/MF/sigma_rich_phi_proof.md`, `sigma_rich_wigner_derivation.md`, `sigma_rich_centroid_derivation.md`, `sigma_rich_orientation_derivation.md` — σ-rich component derivations.

### 5.3 For NQ-242c work

13. `THEORY/working/MF/nq242c_explicit_construction.md` — full NQ-242c protocol, Cat A criteria (C1)–(C4) and (R1)–(R4).
14. `THEORY/working/MF/sigma_rich_VR_phase1.md` — Vietoris-Rips / persistent homology V-R Phase 1 plan.
15. `CODE/scc/multi.py`, `CODE/scc/diagnostics.py` — existing K-field implementation and σ-standard computation.
16. `CODE/scc/transport.py`, `CODE/scc/persistence.py` — persistence pipeline.

### 5.4 For K-selection work

17. `THEORY/working/MF/k_selection_mechanism.md` — three Cat C candidates.
18. `THEORY/working/MF/k_selection_a_free_energy.md`, `k_selection_b_kramers.md`, `k_selection_c_numerical_anchor.md` — per-candidate development.
19. `THEORY/working/MF/k_selection_compatibility_proof.md`, `commitment_19_k_selection_axiom_packet.md` — compatibility scaffolding.
20. `THEORY/working/MF/cn15_static_dynamic_separation.md` — CN15 Static/Dynamic Separation candidate (relevant to why energy minimization does not force $K_{\mathrm{act}} = 1$).

### 5.5 For stratified ambient feasibility check

21. `THEORY/working/MF/mathematical_scaffolding_4tools.md` §2 (already in §5.1 above) — count-only Whitney verification.
22. `THEORY/working/MF/op003_mo1_status_review.md` — MO-1 status, single-formation sidestep, multi-formation re-activation rider.

### 5.6 For empirical and bridge-lemma work

23. `THEORY/working/MF/single_high_F_equivalence.md` (OAT-7) — R23 fullscale dataset analysis, overlap regime as generic.
24. `THEORY/working/MF/F_Kstep_K_triple.md` (OAT-2) — F / $K_{\mathrm{step}}$ / $K_{\mathrm{act}}$ / $K_{\mathrm{field}}$ triple.

### 5.7 Do not edit

- `THEORY/canonical/canonical.md`
- `THEORY/canonical/theorem_status.md`
- `THEORY/canonical/open_problems.md`
- `THEORY/CHANGELOG.md`
- `_archive/**` (frozen)
- Any vision_model_sketch/ file (application-side, out of scope for this line)

If a canonical edit is genuinely needed, it must go through the promotion pipeline and be staged in a new working file, not done directly in canonical/.

---

## 6. Next work package order

The work packages must be attempted in this order. Each depends on the previous having a definite outcome (success or documented failure).

```text
0. Layered ambient documentation
   (this package: README + candidate + agent notes + next work)
   ↓
1. NQ-242c counterexample protocol
   (WQ-1: σ-standard non-determinism numerical anchor;
    σ-rich determinism evaluation)
   ↓
2. K-soft / K-act bridge lemma
   (WQ-2: well-separated regime approximation
    statement with explicit error term)
   ↓
3. σ-rich minimal packet analysis
   (WQ-3: identify minimal augmentation for Φ_rich
    determinism on NQ-242c construction)
   ↓
4. K-selection three-model comparison
   (WQ-4: free-energy / kinetic / symmetry-broken
    candidates side-by-side on R23)
   ↓
5. Stratified ambient feasibility check
   (WQ-5: Whitney verification on labelled cell
    refinement; minimal coarsening if needed)
```

For full goal / inputs / outputs / success criterion / forbidden claims of each, see `layered_ambient_architecture_next_work.md`.

**Order rationale:**

- WQ-1 first, because everything else depends on whether σ-standard is actually insufficient. If WQ-1 fails (σ-standard non-determinism does not manifest in the NQ-242c construction), σ-rich Path B is not motivated, and the order shifts.
- WQ-2 depends only on definitions (already in `..._candidate.md`); independent of WQ-1 outcome but most useful once WQ-1's empirical anchor is available.
- WQ-3 strictly requires WQ-1 results.
- WQ-4 is independent of WQ-1–WQ-3 but more naturally sequenced after them, because the K-selection mechanisms are sharper-stated under the layered architecture.
- WQ-5 is the most theoretically self-contained but largest in effort; placing it last avoids blocking earlier packages.

---

**End of agent notes.**

**If you read only one section, read §1 (Mandatory distinctions) and §2 (Forbidden overclaims).**

**If you are about to write a working file in this line, also read §3 (Safe terminology) and §4 (Unsafe terminology).**
