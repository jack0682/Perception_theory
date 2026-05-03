# Non-Canonical Commitment Candidate: Layered Ambient-State Architecture for SCC / Multi-Formation

**Document type:** Non-canonical commitment candidate. Working draft.
**File:** `THEORY/working/MF/layered_ambient_architecture_candidate.md`
**Created:** 2026-05-02 (W6 prep, advanced from prior architecture decision report).
**Status mode:** Non-canonical. No commitment number is assigned. No canonical files are edited by this memo.
**Canonical baseline:** CV-1.5.1 (`THEORY/canonical/canonical.md`, 2026-04-29).
**Related working files:** `K_status_commitment.md` (OAT-1), `shared_pool_canonical_proposal.md` (OAT-4), `mathematical_scaffolding_4tools.md` (OAT-supplementary), `sigma_multi_trajectory.md` (D-6b dynamic), `nq242c_explicit_construction.md` (NQ-242c protocol), `multi_formation_sigma.md` (D-6a static), `sigma_rich_augmentation.md` (Path B), `cn15_static_dynamic_separation.md` (CN15 candidate).
**Companion docs (this package):** `layered_ambient_architecture_README.md`, `layered_ambient_architecture_agent_notes.md`, `layered_ambient_architecture_next_work.md`.

---

## Status labels used in this document

| Label | Meaning |
|---|---|
| **canonical theorem-grade** | Already in `canonical.md` §13 with Cat A / B / C marker; not changed by this memo. |
| **working-definition safe** | Definition is precise, internally consistent, not yet promoted to canonical. Safe to use in working files. |
| **theorem-grade under existing hypotheses** | Proved under stated hypotheses (e.g., interior regime, well-separated regime); typically Cat B or Cat C target. |
| **conjectural / downstream** | Open question or hypothesis under test; resolved only by a downstream work package. |
| **forbidden non-claim** | Identification or inference that this memo and downstream work must avoid. |

---

## 1. Status and Scope

This memo proposes a layered ambient-state architecture for SCC / Multi-Formation analysis. It is a **non-canonical commitment candidate**. It does not modify, supersede, or replace any entry in `THEORY/canonical/`. It does not assign a Commitment number. It does not promote any object to canonical status.

The architecture is restricted to:

- finite graphs $G_t = (X_t, N_t)$ with $|X_t| < \infty$;
- finite total mass $M$;
- finite architectural cap $K_{\mathrm{field}} \in \mathbb{Z}_{\ge 1}$;
- gradient-flow dynamics on the K-field energy $\mathcal{E}_K$ as defined in `canonical.md` §11.

Continuum, infinite-volume, infinite-$K$, and stochastic extensions are out of scope. No application claim (vision, control, robotics, neural implementation) is made.

The memo is theory-only. No code is changed.

---

## 2. Purpose

Three recurring conflations in the current working corpus motivate this memo:

1. **Architectural choice vs. ontology.** I9 K-field and I9' shared-pool are sometimes phrased as competing architectures, sometimes as nested submanifolds, sometimes as different stratum views of the same space.
2. **Count-strata vs. labelled active-set cells.** A K-jump is currently defined by the integer count $K_{\mathrm{act}}$, but a labelled trajectory carries more information than the count: the active index set $A \subseteq \{1, \dots, K_{\mathrm{field}}\}$.
3. **Unlabelled topological count vs. labelled active count.** A persistence-based soft count derived from $H_0$ of the aggregate field is conceptually distinct from the labelled threshold-gated active count; they are sometimes used interchangeably.

The architecture separates these by introducing three explicit layers, each with its own primitive object, ambient, intended use, and status grade.

---

## 3. Primitive Graph Substrate

The primitive substrate is the time-indexed weighted graph

$$
G_t = (X_t, N_t),
$$

where $X_t$ is finite, $N_t : X_t \times X_t \to [0, \infty)$ is symmetric in the minimal SCC setting, and $G_t$ carries a graph Laplacian $L_t$, a row-normalized transition $P_t$, and a cohesion-weighted symmetric form $W_{\mathrm{sym}}$ (`CODE/scc/graph.py`).

Per `canonical.md` §3.2 and §2 (Foundational Orientation), $X_t$ is a domain of relational loci, not a collection of pre-given objects.

$G_t$ is the substrate for closure $\mathrm{Cl}_t$, distinction $D_t$, the four energy functionals $E_{\mathrm{cl}}, E_{\mathrm{sep}}, E_{\mathrm{bd}}, E_{\mathrm{tr}}$, persistence (core-overlap and transport-based variants), cohesion fingerprint, and Sinkhorn OT transport.

**Status:** canonical theorem-grade (`canonical.md` §3).

---

## 4. Layer I — Primitive Single-Field Ambient

### 4.1 Definition

$$
\Sigma_m(G_t)
:=
\left\{
u : X_t \to [0,1]
\;\middle|\;
\sum_{x \in X_t} u(x) = m
\right\},
\qquad m \in (0, |X_t|).
$$

The soft cohesion field $u : X_t \to [0,1]$ is the primitive ontological entity per Commitment 1 of `canonical.md` §11.

### 4.2 Status and use

**Status:** canonical theorem-grade.

The single-formation theorem-grade core lives here:

- existence T-1, interior stability T-3, closure fixed point T-6a/b/Stability, enhanced metastability T-7;
- phase transition T-8-Core / T-8-Full;
- Γ-convergence T-11; gradient flow T-14; consistency T-20;
- pre-objective mechanism T-PreObj-1, graph-class extension T-PreObj-1G;
- pre-objective Goldstone T-V5b-T (with V5b-T-zero, V5b-F-empirical sub-statements);
- σ-framework supporting structures T-σ-Lemma-1/2/3, T-σ-Theorem-3/4 (CV-1.5);
- QM-1..4, C-Axioms, Predicate-Energy Bridge, Deep Core Dom. 2b.

This memo does not modify, reframe, or reinterpret any of these results.

### 4.3 Allowed analytical machinery on Layer I

- Smooth simplex structure on $\Sigma_m(G_t)$.
- Hessian spectrum and full irrep / nodal-count σ-framework (Commitment 14).
- Smooth Morse theory on the interior of $\Sigma_m(G_t)$ (no corners; OP-0003 SIDESTEPPED at single-formation).
- Predicate diagnostics $\mathbf d = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist})$.

### 4.4 Forbidden moves on Layer I

- Treating $\Sigma_m(G_t)$ as a labelled multi-formation space.
- Importing $K_{\mathrm{field}}$ or $K_{\mathrm{act}}$ machinery into single-formation statements.
- Lifting any single-formation theorem to multi-formation without explicit passage through Layer II or Layer III.

---

## 5. Layer II — Shared-Pool Multi-Formation Ambient

### 5.1 Definition

$$
\widetilde{\Sigma}^{K_{\mathrm{field}}}_{M}(G_t)
:=
\left\{
\mathbf u = (u^{(1)}, \dots, u^{(K_{\mathrm{field}})})
\in [0,1]^{K_{\mathrm{field}} \times X_t}
\;\middle|\;
\sum_{j=1}^{K_{\mathrm{field}}} \sum_{x \in X_t} u^{(j)}(x) = M,
\;\;
\sum_{j=1}^{K_{\mathrm{field}}} u^{(j)}(x) \le 1
\;\;\forall x \in X_t
\right\}.
$$

Parameters:

- $K_{\mathrm{field}} \in \mathbb{Z}_{\ge 1}$ — architectural cap, external modeling-layer commitment per Commitment 16 (CV-1.5.1).
- $M \in (0, |X_t|]$ — conserved total mass.

### 5.2 Status and use

**Status:** working-definition safe; promotion target CV-1.6 D-CV1.6-O2 (per `shared_pool_canonical_proposal.md`).

Intended uses:

- Host trajectories whose active formation count varies (K-jump events: merger, extinction).
- Host the σ-multi$^A(t)$ dynamic framework (`sigma_multi_trajectory.md`).
- Host the NQ-242c counterexample protocol.
- Host LSW-style coarsening dynamics in the long-time limit.
- Serve as the globally consistent ambient across K-jumps.

### 5.3 Count-only stratification (working-definition safe)

For $\varepsilon \in (0, M / K_{\mathrm{field}})$ a fixed support-mass threshold, the count-only stratification

$$
S_{K_{\mathrm{act}}}(G_t) := \big\{ \mathbf u \in \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t) : \#\{j : m_j(\mathbf u) > \varepsilon\} = K_{\mathrm{act}} \big\}
$$

partitions $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$. Per `mathematical_scaffolding_4tools.md` §2.2, this *count-only* stratification is verified Whitney-stratified semi-algebraic (working-definition safe; CV-1.6 promotion candidate).

### 5.4 Forbidden moves on Layer II

- Treating Layer II as a smooth manifold globally.
- Importing fixed-mass theorem-grade results (T-Persist-K-Sep / Weak / Unified) directly onto Layer II without smooth-segment scope.
- Asserting deterministic K-jump σ-inheritance.

---

## 6. Derived Count and Projection Objects

### 6.1 Active mass

$$
m_j(\mathbf u) := \sum_{x \in X_t} u^{(j)}(x),
\qquad j \in \{1, \dots, K_{\mathrm{field}}\},
\qquad \sum_{j=1}^{K_{\mathrm{field}}} m_j(\mathbf u) = M.
$$

Real-valued, smooth on the interior of Layer II, varies continuously along gradient-flow trajectories. **Status:** working-definition safe.

### 6.2 Active count

For a fixed threshold $\varepsilon \in (0, M / K_{\mathrm{field}})$,

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u)
:=
\#\big\{ j \in \{1, \dots, K_{\mathrm{field}}\} : m_j(\mathbf u) > \varepsilon \big\}.
$$

Properties:

- $K_{\mathrm{act}}^\varepsilon : \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t) \to \{0, 1, \dots, K_{\mathrm{field}}\}$ is integer-valued.
- Threshold-gated and labelled (computation requires distinguishing the $K_{\mathrm{field}}$ slots).
- Stratum / region index, not an unlabelled topological count.

**Status:** working-definition safe via Commitment 16 (CV-1.5.1).

Default convention: $\varepsilon = 0.01 \cdot \bar m$ with $\bar m = M / K_{\mathrm{field}}$ (per `K_status_commitment.md` §6.1). The convention is provisional; sensitivity to $\varepsilon$ is part of the K-soft / K-act bridge work package.

### 6.3 Aggregate field projection

$$
U(\mathbf u)(x) := \sum_{j=1}^{K_{\mathrm{field}}} u^{(j)}(x).
$$

The simplex constraint gives $U(\mathbf u)(x) \in [0, 1]$. Mass conservation gives $\sum_x U(\mathbf u)(x) = M$. Therefore

$$
U : \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t) \;\longrightarrow\; \Sigma_M(G_t).
$$

$U$ is the bridge from Layer II to Layer I. It forgets per-formation labelling and overlap structure; it is not invertible. **Status:** working-definition safe.

### 6.4 H0 persistence-based soft count

For any single-field configuration $v : X_t \to [0,1]$, define the superlevel filtration

$$
G_t^\theta(v) := G_t\big[\{x \in X_t : v(x) \ge \theta\}\big],
\qquad \theta \in [0, 1],
$$

where $G_t[Y]$ denotes the induced subgraph on vertex set $Y$. Let $\mathrm{Dgm}_0(v; G_t)$ be the $H_0$ persistence diagram of this filtration, and let $\{\ell_i(v)\}_i$ be the lengths (persistences) of its positive-length bars.

Let $\phi : [0, 1] \to [0, \infty)$ be **monotone, Lipschitz, with $\phi(0) = 0$**. Define

$$
K_{\mathrm{soft}}^\phi(v) := \sum_i \phi\big(\ell_i(v)\big).
$$

For a Layer II state, $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ is the soft count of the aggregate field.

**Status:** working-definition safe (this memo upgrades the dormant `working/E/soft_K_definition.md` by introducing the $\phi$-envelope form).

Properties:

- Real-valued; not integer-valued in general.
- Unlabelled — depends only on $G_t$ and the field $v$.
- Depends on $G_t$, the choice of $\phi$, and finite graph resolution; this dependence must be made explicit when comparing across configurations.
- By Cohen-Steiner–Edelsbrunner–Harer (2007) bottleneck stability and the Lipschitz hypothesis on $\phi$:

  $$
  \big| K_{\mathrm{soft}}^\phi(v) - K_{\mathrm{soft}}^\phi(v') \big|
  \;\le\;
  C_\phi \cdot \big| \mathrm{Dgm}_0(v) - \mathrm{Dgm}_0(v') \big|_{\mathrm{bot}}
  \;\le\;
  C_\phi \cdot \| v - v' \|_\infty,
  $$

  where $C_\phi$ is the Lipschitz constant of $\phi$ scaled by an upper bound on the number of bars.

**Documentation warning.** $K_{\mathrm{soft}}^\phi$ avoids choosing a single object-existence threshold (which $K_{\mathrm{act}}^\varepsilon$ does require) but it still depends on $G_t$, the superlevel filtration, $\phi$, and the finite graph resolution. It is not threshold-free in any absolute sense.

### 6.5 The four objects collected

| Symbol | Layer | Type | Labelled? | Threshold? | Role |
|---|---|---|---|---|---|
| $m_j(\mathbf u)$ | II | real | yes | no | per-formation mass |
| $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ | II | integer | yes | yes | active count / count-region index |
| $U(\mathbf u)$ | II → I | field | n/a (forgets) | no | aggregate projection to Layer I |
| $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ | I (computed via $U$) | real | no | envelope-mediated | unlabelled topological soft count |

These four objects exhaust the count / projection vocabulary of this memo.

---

## 7. ε-Active Regions and K-Jumps

### 7.1 Active-set cells

For $\varepsilon \in (0, M / K_{\mathrm{field}})$ and $A \subseteq \{1, \dots, K_{\mathrm{field}}\}$, define the **active-set cell**

$$
S_A^\varepsilon(G_t)
:=
\left\{
\mathbf u \in \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)
\;:\;
m_j(\mathbf u) > \varepsilon \text{ for } j \in A,
\;\;
m_j(\mathbf u) \le \varepsilon \text{ for } j \notin A
\right\}.
$$

**Documentation warning.** The word "cell" here is a memo-internal **operational** term denoting a labelled region of Layer II indexed by an active set $A$. It is **not** a CW-complex cell, not a Morse-Smale cell, not a chamber of an arrangement. The naming is for compactness within this memo and the next-work package files.

### 7.2 ε-active-count regions

For $r \in \{0, 1, \dots, K_{\mathrm{field}}\}$,

$$
S_r^\varepsilon(G_t)
:=
\bigsqcup_{
\substack{
A \subseteq \{1, \dots, K_{\mathrm{field}}\} \\
|A| = r
}
}
S_A^\varepsilon(G_t),
$$

and

$$
\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)
=
\bigsqcup_{r = 0}^{K_{\mathrm{field}}}
S_r^\varepsilon(G_t).
$$

### 7.3 Status of cells and regions

- $S_A^\varepsilon$ is a labelled cell; $S_r^\varepsilon$ is the disjoint union of cells of size $r$, count-collapsing.
- $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$ are **operational ε-active-count regions**, not Whitney strata.
- The Whitney verification of `mathematical_scaffolding_4tools.md` §2.2 is for the *count-only* stratification $\{S_{K_{\mathrm{act}}}\}$, *not* for the labelled cell refinement or the ε-thresholded count regions. Stratifiability of $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$ requires a separate analysis (see `layered_ambient_architecture_next_work.md` work package WQ-5).
- **Forbidden non-claim:** $\{S_A^\varepsilon\}$ or $\{S_r^\varepsilon\}$ are Whitney strata.

**Status:** working-definition safe (cells and regions); stratifiability of these refinements is **conjectural / downstream**.

### 7.4 K-jump (event-only definition)

Let $\mathbf u : [0, T] \to \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ be a continuous trajectory. A time $t^* \in (0, T)$ is a **K-jump time** at threshold $\varepsilon$ if

$$
\mathbf u(t^{*-}) \in S_r^\varepsilon(G_t),
\qquad
\mathbf u(t^{*+}) \in S_s^\varepsilon(G_t),
\qquad
s < r,
$$

equivalently

$$
K_{\mathrm{act}}^\varepsilon\big(\mathbf u(t^{*-})\big)
\;>\;
K_{\mathrm{act}}^\varepsilon\big(\mathbf u(t^{*+})\big).
$$

### 7.5 What the K-jump definition does and does not do

The definition is **event-only**. It identifies what counts as a K-jump along a trajectory.

It does **not**:

- assert $\sigma^A(t^{*+})$ is deterministic in $\sigma^A(t^{*-})$ alone;
- assert the labelled active set $A(t^{*+})$ is deterministic in $A(t^{*-})$;
- assert σ-standard is sufficient as a state for post-jump dynamics;
- assert single-merger genericity ($r - s = 1$);
- assert uniqueness of left/right limits in the corner-saturated regime.

These are open questions handled by downstream work packages, principally NQ-242c.

**Status:** working-definition safe.

---

## 8. Layer III — Fixed-Mass Smooth Local Slices

### 8.1 Definition

For $A \subseteq \{1, \dots, K_{\mathrm{field}}\}$, $|A| = r$, and a per-formation mass vector $\mathbf m_A = (m_j)_{j \in A}$ with each $m_j > 0$ and $\sum_{j \in A} m_j = M$, define the **occupancy-constrained fixed-mass slice**

$$
\Sigma_M^A(\mathbf m_A; G_t)
:=
\left\{
\mathbf u \in \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)
\;:\;
m_j(\mathbf u) = m_j \text{ for } j \in A,
\;\;
m_j(\mathbf u) = 0 \text{ for } j \notin A
\right\}.
$$

### 8.2 Containment in Layer II (not an unconstrained product)

$\Sigma_M^A(\mathbf m_A; G_t) \subseteq \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ by construction.

The unconstrained product $\prod_{j \in A} \Sigma_{m_j}(G_t)$ is **not** naturally a subset of Layer II, because the simplex constraint $\sum_j u^{(j)}(x) \le 1$ is enforced on Layer II but not on the product. The correct view is

$$
\Sigma_M^A(\mathbf m_A; G_t)
\;\subseteq\;
\Big\{
(u^{(j)})_{j \in A} \in \prod_{j \in A} \Sigma_{m_j}(G_t)
\;:\;
\sum_{j \in A} u^{(j)}(x) \le 1 \;\forall x
\Big\}
\;\subseteq\;
\prod_{j \in A} \Sigma_{m_j}(G_t).
$$

The simplex constraint is generically active in the overlap regime and generically slack in the well-separated regime; Layer III does not erase it.

**Documentation warning.** Treating $\Sigma_M^A(\mathbf m_A; G_t)$ as the unconstrained product $\prod_{j \in A} \Sigma_{m_j}(G_t)$ silently drops the simplex constraint and admits configurations that are not in Layer II. This is a recurring error mode and is forbidden.

### 8.3 Status and use

**Status:** working-definition safe; the canonical I9 K-field architecture $\Sigma_M^K = \prod_j \Sigma_{m_j}$ is reread within this memo as a Layer III object (interpretation only, no canonical edit).

Layer III hosts:

- T-Persist-K-Sep (Cat B), T-Persist-K-Weak (Cat C), T-Persist-K-Unified (Cat B), with the smooth-segment scope clause proposed in `shared_pool_canonical_proposal.md` §5.2;
- the static D-6a Multi-σ framework (T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static, T-σ-Multi-1) per CV-1.5.1, on the interior of Layer III (Option A pragmatic).

### 8.4 Forbidden moves on Layer III

- Treating $\Sigma_M^A(\mathbf m_A; G_t)$ as the global lifecycle ambient. It cannot host K-jumps by definition.
- Substituting the unconstrained product (simplex constraint lost).
- Lifting fixed-mass results to variable-mass dynamics without smooth-segment scope and explicit handling of stratum-boundary events.

---

## 9. Regime Discipline

The interaction between $K_{\mathrm{soft}}^\phi$ and $K_{\mathrm{act}}^\varepsilon$ — and the analytical safety of layer crossings — depends on which regime the state inhabits.

### 9.1 Well-separated regime

A state $\mathbf u \in S_A^\varepsilon(G_t)$ is **$(\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min})$-well-separated** if all four conditions hold:

1. $m_j(\mathbf u) > \varepsilon$ for all $j \in A$.
2. The $\delta$-supports

   $$
   \mathrm{Supp}_\delta(u^{(j)}) := \{x \in X_t : u^{(j)}(x) > \delta\}, \qquad \delta \in (0, 1),
   $$

   are pairwise disjoint:
   $\mathrm{Supp}_\delta(u^{(j)}) \cap \mathrm{Supp}_\delta(u^{(k)}) = \emptyset$ for $j \ne k$ in $A$.

3. Graph distance between $\delta$-supports satisfies
   $d_{G_t}\!\big(\mathrm{Supp}_\delta(u^{(j)}), \mathrm{Supp}_\delta(u^{(k)})\big) \ge D_{\mathrm{sep}}$
   for all $j \ne k$ in $A$.

4. The aggregate $H_0$ persistence diagram $\mathrm{Dgm}_0(U(\mathbf u); G_t)$ contains exactly $|A|$ bars of length $\ge \ell_{\min}$, and at most $|A|$ bars of any length above an auxiliary robustness threshold.

Under these hypotheses, $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ and $K_{\mathrm{act}}^\varepsilon(\mathbf u) = |A|$ become comparable as an approximation statement with explicit error term. The exact form of this approximation is the content of the **K-soft / K-act bridge lemma** (work package WQ-2).

**Status:** working-definition safe (the hypotheses); bridge identity is **conjectural / downstream**.

### 9.2 Overlap regime

A state $\mathbf u \in S_A^\varepsilon(G_t)$ is in the **overlap regime** if it satisfies (1) but fails one or more of (2), (3), (4).

In the overlap regime, $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ and $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ may genuinely diverge. T-Persist-K-Weak (Cat C) is the relevant smooth-segment persistence regime.

The R23 fullscale dataset analysis of `single_high_F_equivalence.md` (OAT-7) finds the overlap regime is *generic* in the high-$\mathcal{F}$ ground-state regime: all 56 R23 minimizers have $\mathcal{F} > K_{\mathrm{step}}$, so the well-separated bijection between per-formation peaks and aggregate $H_0$ features fails generically.

### 9.3 Corner-saturated regime

A state $\mathbf u \in \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ is **corner-saturated** if at least one holds:

- $m_j(\mathbf u) \downarrow \varepsilon$ for some $j$ (extinction-imminent / cell-boundary).
- $u^{(j)}(x) \in \{0, 1\}$ for some $(j, x)$ (field-boundary saturation).
- $\sum_j u^{(j)}(x) = 1$ for some $x$ (simplex constraint active).

In this regime, smooth-manifold structure of fixed-mass slices fails (mass-boundary case), the interior smoothness hypothesis (H4) of `sigma_multi_trajectory.md` Lemma 4.1 fails, and finite-difference Hessian computations and analytic perturbation theory become unreliable. V5b-T-zero / V5b-F sub-statements of T-V5b-T live precisely in this regime; their handling is single-formation.

This regime must be flagged explicitly whenever invoked.

### 9.4 Regime-aware analysis discipline

A correctly disciplined analysis on Layer II:

1. Identify the candidate regime (well-separated / overlap / corner-saturated).
2. Apply only the bridge lemmas / theorems / definitions valid in that regime.
3. At regime transitions (K-jumps, well-separation breakdowns, corner entries), treat each as a separate analytical event.
4. Do not import bridge identities, fixed-mass slice arguments, or smooth-segment piecewise-constancy across regime transitions without an explicit transition lemma.

---

## 10. Theorem-Grade / Conjectural Status Table

| # | Object / claim | Status | Why | Allowed use | Forbidden overclaim |
|---|---|---|---|---|---|
| 1 | $G_t = (X_t, N_t)$ | canonical theorem-grade | `canonical.md` §3 | Substrate for all SCC machinery | Pre-given object identity; smuggling object labels via $X_t$ |
| 2 | $\Sigma_m(G_t)$ | canonical theorem-grade | `canonical.md` §3, §11 | All Cat A single-formation theorems | Importing $K_{\mathrm{field}} / K_{\mathrm{act}}$ machinery |
| 3 | $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ | working-definition safe | `shared_pool_canonical_proposal.md` (CV-1.6 target) | Multi-formation lifecycle host | Treating as smooth manifold globally; treating I9 as a competing architecture |
| 4 | $m_j(\mathbf u)$ | working-definition safe | derived from definition | Continuous diagnostic on Layer II | Promoting to primitive parameter |
| 5 | $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ | working-definition safe via Commitment 16 | Threshold-gated labelled count | Stratum / region index on Layer II | Treating as unlabelled topological count; ignoring threshold dependence |
| 6 | $U(\mathbf u)$ | working-definition safe | Simplex constraint forces $U \in \Sigma_M(G_t)$ | Bridge from Layer II to Layer I | Treating as faithful inverse |
| 7 | $K_{\mathrm{soft}}^\phi(v) = \sum_i \phi(\ell_i(v))$ | working-definition safe | Cohen-Steiner stability + Lipschitz $\phi$ + $\phi(0)=0$ | Unlabelled soft count of aggregate field | Suppressing $\phi$, $G_t$, or filtration dependence; threshold-free framing |
| 8 | $S_A^\varepsilon$ active-set cell | working-definition safe | Labelled refinement of count stratum | Region notation; precondition for NQ-242c labelled trajectory analysis | Calling a Whitney stratum or a CW cell |
| 9 | $S_r^\varepsilon = \bigsqcup_{|A|=r} S_A^\varepsilon$ | working-definition safe | Disjoint union; count-collapsing | Operational ε-active-count region | Identifying with intrinsic-count strata $S_{K_{\mathrm{act}}}$ of `mathematical_scaffolding_4tools.md` §2.2 |
| 10 | $\Sigma_M^A(\mathbf m_A; G_t)$ | working-definition safe (Layer III scope) | Occupancy-constrained subset of Layer II | Smooth-segment fixed-K fixed-mass theorems (T-Persist-K-Sep / Weak / Unified, D-6a static σ-multi) | Substituting unconstrained product $\prod_{j\in A}\Sigma_{m_j}(G_t)$; treating as global lifecycle ambient |
| 11 | K-jump event definition | working-definition safe (event-only) | Direct from continuity + $K_{\mathrm{act}}^\varepsilon$ drop | Identifying jump times; staging NQ-242c | Asserting deterministic σ-inheritance, deterministic $A$-inheritance, single-merger genericity, unique right-limit |
| 12 | $K_{\mathrm{soft}} \leftrightarrow K_{\mathrm{act}}$ bridge | conjectural / downstream | Requires (well-separated, $\delta$, $D_{\mathrm{sep}}$, $\ell_{\min}$) hypotheses | Approximation statement with explicit hypotheses and error term (work package WQ-2) | Global identity; identity in overlap or corner-saturated regimes |
| 13 | Whitney stratification of $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$ | conjectural / downstream | Verification in `mathematical_scaffolding_4tools.md` §2.2 is for intrinsic-count strata only; ε-thresholds add new singular loci | None until separate feasibility check (work package WQ-5) | Invoking stratified Morse on labelled cells without verification |
| 14 | Stratified Morse theory on Layer II | conjectural / downstream | Goresky-MacPherson framework named, not applied; SCC energy needs Morse-Bott handling | Named as natural framework only | Asserting as established machinery; promoting OP-0003 MO-1 from SIDESTEPPED to RESOLVED |
| 15 | Deterministic σ-standard inheritance across K-jump | forbidden non-claim (currently conjectured non-deterministic / Cat C) | `sigma_multi_trajectory.md` Lemma 4.4.1(c); PH non-lift fact | State non-determinism as conjectured; attack via NQ-242c | Asserting determinism; asserting σ-standard sufficiency |
| 16 | σ-rich global sufficiency | conjectural / downstream | `sigma_rich_augmentation.md` Path B framework; no global proof | State as candidate; pursue via NQ-242c-Rich | Asserting deterministic Φ_rich globally; promoting to canonical without (C1)–(C4) numerical and (R1)–(R4) theoretical criteria |
| 17 | K-Selection mechanism (OP-0005) | conjectural / downstream | No mechanism for $K_{\mathrm{act}}(0)$ or $K_{\mathrm{act}}(\infty)$ selection | Three-model comparison framework (work package WQ-4) | Asserting any single mechanism resolves OP-0005; substituting Commitment 16 K-status decomposition for a selection mechanism |
| 18 | Global identity $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ | forbidden non-claim | Different ontological layers; divergence in overlap and corner-saturated regimes | None | All forms of identification |
| 19 | $\{S_A^\varepsilon\}$ = Whitney strata | forbidden non-claim | ε-threshold loci differ from intrinsic stratum boundaries | None | Treating cells as strata |
| 20 | Application bridges (vision, robotics, control) | forbidden non-claim within this memo | No application claim is made by this memo | None within this memo | Citing the architecture as application-ready |

---

## 11. Migration Notes

### 11.1 Preserved exactly

- The single-field formal universe $\mathfrak{C}^{\mathrm{soft}}$ of `canonical.md` §3.
- The Layer I ambient $\Sigma_m(G_t)$.
- All canonical Cat A / B / C single-formation theorems.
- Commitment 1 ($u_t$ primitive), Commitment 11 (crisp objects derivative), Commitment 14 (σ-signature single-formation), CN5 (4-term independence at single-formation), CN10 (contrastive vs. reductive), CN17 (σ-Labeled Formation Quantization).
- Commitment 16 (K-status two-tier decomposition, CV-1.5.1).
- The CV-1.5.1 D-6a Multi-Static merge (T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static, T-σ-Multi-1) on the interior of Layer III.

### 11.2 Reclassified (interpretation only, no canonical edit)

- The current canonical I9 K-field architecture $\Sigma_M^K = \prod_j \Sigma_{m_j}$ is reread as a Layer III fixed-mass smooth local slice.
- T-Persist-K-Sep / Weak / Unified is reread as Layer III, smooth-segment results; the smooth-segment scope clause already proposed in `shared_pool_canonical_proposal.md` §5.2 is the corresponding canonical-edit candidate.
- CN6 ("K is kinetically determined") is reread as a statement about $K_{\mathrm{act}}$, per the Commitment 16 amendment proposal in `K_status_commitment.md` §5.5.

### 11.3 Newly staged

- Layer II $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ as the global lifecycle ambient (the *layered framing* is new; the object is not).
- Cell refinement $\{S_A^\varepsilon\}$ and labelled count region $\{S_r^\varepsilon\}$.
- Aggregate projection $U$ and persistence-based soft count $K_{\mathrm{soft}}^\phi$ (with $\phi$ envelope, upgrading dormant `working/E/soft_K_definition.md`).
- K-jump event-only definition on Layer II.
- Regime discipline (well-separated / overlap / corner-saturated) consolidated.

### 11.4 NQ-242c framing under the architecture

NQ-242c is now framed as a trajectory-pair construction inside Layer II:

- Both trajectories live in $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ with $K_{\mathrm{field}} = 4$, $M = 90$, $G_t = T^2_{20}$.
- Both start in the same active-set cell $S_A^\varepsilon$ with $A = \{1, 2, 3\}$, $K_{\mathrm{act}}^\varepsilon = 3$.
- Both undergo a K-jump at some $t^*$ where $K_{\mathrm{act}}^\varepsilon$ drops.
- σ-standard at $t^{*-}$ is identical (qualitative-tuple convention at $10^{-3}$).
- σ-standard at $t^{*+}$ is conjectured to differ (NQ-242c-Standard).
- σ-rich at $t^{*-}$ differs (NQ-242c-Rich); Φ_rich is conjectured deterministic at $t^{*+}$.

### 11.5 σ-rich precondition

σ-rich work should not begin in earnest until σ-standard has been *demonstrated* insufficient. NQ-242c provides this demonstration. Until (C1) of `nq242c_explicit_construction.md` §6 is numerically confirmed, σ-rich is a candidate augmentation, not a required one.

### 11.6 No change to canonical files

This memo does not edit `canonical.md`, `theorem_status.md`, `theorem_status.md` (Open Problems Catalog), or `CHANGELOG.md`. Should the architecture be promoted, the canonical-edit candidates already drafted in `mathematical_scaffolding_4tools.md` §8 and `shared_pool_canonical_proposal.md` §5 are the relevant text proposals.

---

## 12. Explicit Non-Claims

1. Not a final architecture.
2. Not a resolution of K-Selection (OP-0005).
3. Not a proof of σ-rich sufficiency.
4. Not a proof of deterministic K-jump σ-inheritance.
5. No global σ-rich sufficiency on the basis of any local numerical anchor.
6. No global identification $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$.
7. No identification of $\{S_A^\varepsilon\}$ or $\{S_r^\varepsilon\}$ with Whitney strata.
8. No import of advanced mathematical machinery: gauge theory, full category theory, Geometric Langlands, sheaf cohomology beyond elementary $H_0$ persistence, CBF / CLF, neural operators, Koopman operators, formal verification.
9. No import of stratified Morse theory as established machinery.
10. No application claim (vision, robotics, control, real-time perception, attention, neural implementation, embodied AI).
11. No silent resolution of any open problem; F-1, M-1, MO-1, OP-0005, OP-0006, OP-0008, OP-0009 sub-items remain in their current canonical status.
12. No claim of canonical priority between I9 (K-field) and I9' (shared-pool); both inhabit the same triple-layer scaffold.
13. No commitment to specific $\varepsilon$ or $\phi$; default conventions are provisional.

---

## 13. Final Recommendation

**Recommendation:** Adopt the layered ambient-state architecture **as a non-canonical working frame**. Use it to organize the next round of multi-formation work — NQ-242c, σ-rich minimal packet, K-soft / K-act bridge lemma, K-selection three-model comparison, stratified ambient feasibility check — without promoting it to canonical status until those downstream results are in.

The architecture introduces no new theorems. It organizes the existing working corpus, prevents the recurring conflations of §2, and prepares the formal stage for the downstream work packages.

**Promotion path** (deferred to user decision):

1. Execute NQ-242c; evaluate (C1)–(C4) of `nq242c_explicit_construction.md` §6.
2. Draft K-soft / K-act bridge lemma with explicit hypotheses and error term.
3. Perform stratified ambient feasibility check on $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$.
4. If 1–3 succeed, promote Layer II to canonical via Commitment 17 + §3.10 candidate texts.
5. If any of 1–3 fails, retain the architecture as a working-frame notation; only Layer I remains canonical-grade.

**What this memo authorizes the user to do:**

- Use the layered language in working files.
- Stage NQ-242c, the bridge lemma, σ-rich minimal packet, K-selection comparison, and stratified ambient feasibility check using the three-layer vocabulary.
- Cross-reference this memo from new working files in the same package.

**What this memo does not authorize:**

- Editing canonical files.
- Assigning a Commitment number.
- Claiming K-Selection, σ-rich sufficiency, or stratified Morse as resolved.
- Treating $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ as identity.
- Citing the architecture in a vision / robotics / control context.

---

**End of `layered_ambient_architecture_candidate.md`.**

**Status: working draft (non-canonical commitment candidate).**
**Companion docs:** `layered_ambient_architecture_README.md`, `layered_ambient_architecture_agent_notes.md`, `layered_ambient_architecture_next_work.md`.
**Promotion target:** CV-1.6+ pending downstream work packages WQ-1 through WQ-5.
