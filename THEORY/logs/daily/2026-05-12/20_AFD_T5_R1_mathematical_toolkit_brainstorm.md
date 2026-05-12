---
type: log/brainstorm
date: 2026-05-12
target: AFD-T5 R1 promotion — mathematical backbone landscape
canonical_version: CV-1.13 (read-only)
session_label: W7-Day3 (extended brainstorming pass)
mode: long-form catalog + comparative analysis + new-direction brainstorm
external_input: GPT-5 meta-research planning report (provided by user)
non_goals:
  - Direct canonical edit
  - Direct working/ edit
  - OMC pool orchestration
status: brainstorm only — no decisions locked
---

# 20 — AFD-T5 R1 Mathematical Backbone Brain-storming

**Session:** 2026-05-12 W7 Day 3 (extended pass after the OP-AFD-003 development cycle and its audit)
**Trigger:** User request — *"AFD-T5 R1과 관련해서 내가 많은 수학적 도구들을 찾아보고 그랬잖아 ... brainstorming이 아주 강하게 필요해 시간은 제한이 없으니 충분한 시간을 써서라도 진행해줘."*
**External meta-input:** GPT-5 meta-research planning report. The report's diagnosis (*topic is specified at domain level, underspecified at decision level; default to comparative framework report + annotated bibliography + theorem-skeleton appendix*) is taken as a planning prior, not as a decision.

**This document covers (informally):**
- Part 0 — why this document exists, and what it is not.
- Part 1 — what exactly is being *locked* when AFD-T5 enters CV-1.14-AFD R1.
- Part 2 — catalog of mathematical backbones, ~30 candidates, grouped by R1 role.
- Part 3 — pairwise compatibility / overlap / conflict matrix.
- Part 4 — minimum essential set for AFD-T5 R1 promotion (audit-honest).
- Part 5 — deferred set for R2/R3 with explicit activation conditions.
- Part 6 — reductive-risk catalog: tools that must *not* be silently absorbed at R1.
- Part 7 — substantive new-direction brainstorming (not in the OP catalog).
- Part 8 — promotion-pipeline implications: what AFD-T5 R1 means for AFD-T6..T11.
- Part 9 — final recommendation + decision points the user must close before promotion.

**Output regulation note.** This document is a *brainstorming log*, not a deliverable promotion proposal. Decisions remain with the user. All "recommendations" are framed as starting points for the next pre-promotion conversation, not as committed positions.

---

## Part 0 — What this document is and is not

### 0.1 What it is

A long-form **catalog + comparative critique** of the mathematical-backbone candidates that bear on AFD-T5 R1 promotion. The catalog is **not exhaustive** (no catalog can be) but aims to cover:

- (i) every tool already cited inside `02_development.md` and `02b_L3_tightening_and_op003c.md`;
- (ii) every tool surfaced in prior SCC working files that bears on AFD;
- (iii) the major adjacent mathematical fields the GPT-5 meta-report identified as overlapping with AFD's scope: dynamical systems, TDA, optimal transport, category theory;
- (iv) a deliberate *speculative bench* of tools whose connection to SCC is plausible but not yet established;
- (v) the **reductive bench** — tools that AFD's canonical commitments (CN10 especially) forbid us from silently merging into.

Each entry has a uniform structure: (a) one-paragraph definition, (b) precise SCC connection, (c) R1 role (essential / leverage / deferred / reductive-risk / speculative), (d) failure modes if invoked at R1.

### 0.2 What it is not

- It is **not** a literature review with citations to specific papers. Where citations matter for R1, they are placeholders ("Bochnak-Coste-Roy", "van den Dries 1998") to be hardened in a separate citation pass.
- It is **not** a decision document. Per the SCC prompt §8 (canonical not directly modified) and §13 (natural stopping at proof completion), promotion decisions are user-driven.
- It is **not** a publication plan. The GPT-5 report's "publication or dissertation packaging" track is acknowledged but explicitly *deferred* — AFD-T5 R1 is a canonical-promotion question, not a paper-submission question.
- It is **not** a parallel-agent task brief. Per §10 of the prompt, OMC orchestration is forbidden.

### 0.3 Why this document is needed now (and not earlier)

Three triggers converge:

(T-1) **AFD-T5's status just changed.** Today's session moved OP-AFD-003 from OPEN(H) to *Cat A modulo Claim B.3* + Cat A unconditional for the K_soft variant. This makes AFD-T5 promotion-ready *conditional on a single citation lookup*. The next session may execute the promotion; we should not promote without first inventorying what AFD-T5 actually *commits* the canonical to.

(T-2) **R1 is a one-way door.** Per SCC promotion-pipeline policy, canonical entries do not flow back to working. Once AFD-T5 is in canonical, the implicit mathematical backbones it depends on are *also* in canonical. We owe a clear-eyed inventory before the door closes.

(T-3) **User has explicitly accumulated tools.** The user's message — *"내가 많은 수학적 도구들을 찾아보고 그랬잖아"* — indicates a private catalog of frameworks examined over the AFD development. The current document is the persistent crystallization of that exploration, not its origination.

### 0.4 The single most important framing

**AFD-T5 R1 is a question about what AFD is, not just what it proves.** A theorem in canonical is not an isolated claim; it is a commitment to the language, the assumptions, and the proof techniques that justify it. AFD-T5's proof (`02_development.md` §5 + audit `02b` §B) commits canonical SCC to:

- (C-1) **Real analyticity of E on Σ_m** as a Cat A standing hypothesis (already implicit via A3 b_D = 0).
- (C-2) **O-minimal geometry of E-sublevel sets** (Claim B.3 if verified; new commitment).
- (C-3) **Compact convex polytope geometry of Σ_m** (already Cat A, T-PF-A1-AR).
- (C-4) **BV-LSC framework for Var_D and J_K** (new operational commitment, follows from Ambrosio-Fusco-Pallara).
- (C-5) **K_act vs K_soft choice** for the J_K cost (currently K_act = primary; K_soft = alternative variant per `02b` §C).

These five commitments are the *load-bearing inputs*; everything else is downstream. Brainstorming should focus on each commitment in turn, asking: "What other tools touch this commitment? Can they replace or strengthen it? What conflicts do they generate?"

---

## Part 1 — What is locked by AFD-T5 R1 promotion

### 1.1 The exact statement under consideration

From `02_development.md` §5.1 (T-OP-AFD-003-A) and `03_integration_and_new_open.md` §1.4 (proposed AFD-T11 wording), AFD-T5 in R1-ready form reads (paraphrased to canonical-style):

> **AFD-T5 (Abstract Transition Cost, Existence and Attainment).** For an SCC universe with canonical Σ_m and analytic energy E (Cat A standing assumptions), for any pair of formation states F_i, F_j ∈ V_form with Adm(F_i, F_j) ≠ ∅, the infimum
> $$C_\mathrm{AFD}(F_i, F_j) = \inf_{\gamma \in \mathrm{Adm}(F_i, F_j)} J_\mathrm{AFD}(\gamma; F_i)$$
> is **attained** by some Lipschitz admissible path γ_* of bounded length L_*. (Cat A modulo Claim B.3; Cat A unconditional in the K_soft variant.)

### 1.2 What this *says* mathematically

(L-1) The functional `J_AFD` has the **direct-method-of-the-calculus-of-variations** structure: a continuous functional, lower-semicontinuous under uniform convergence, on a sequentially compact admissible class.

(L-2) The admissible class `Adm(F_i, F_j)` is **topologically tractable**: closed under uniform limits, with endpoints in closed sets. No measure-theoretic relaxation is required.

(L-3) The minimizer's **regularity** is Lipschitz but no smoother (CK^1 deferred to OP-AFD-003d).

(L-4) The minimizer is **non-unique generically** (saddle ridges allow families).

(L-5) The proof is **constructive in principle** (PL approximation, T-OP-AFD-003-B) but **non-constructive in practice** (no algorithm yields L_* without o-minimal-theory inputs).

### 1.3 What this *commits* the canonical to (deep cuts)

(D-1) **No probabilistic relaxation needed for transition existence.** AFD-T5 lives at Layer 2 (deterministic, gradient-flow + barrier). It does not need Brownian / Langevin / large-deviation machinery. This is the **defining boundary between Layer 2 and Layer 3** of AFD.

(D-2) **The basin-of-attraction concept is canonical for AFD.** B_{F_i} (deterministic basin per AFD-D2) is the input. T-T14 (Łojasiewicz Cat A) guarantees its well-definedness. No alternative formulation (e.g. stochastic quasi-stationary distribution, QSD) is needed at Layer 2.

(D-3) **The cost J_AFD is a normed scalar.** Bar + λ_D Var_D + λ_K J_K is a linear combination with non-negative weights. Vector-valued or partial-order generalizations (Pareto cost) are deferred.

(D-4) **No external symmetry-breaking machinery is invoked.** AFD-T5 proof does not call symmetry, Aut(G), or stabilizer arguments. The M-A2 priority (Priority 1 of plan.md) is *orthogonal* to AFD-T5.

(D-5) **Compact-finite-graph setting is canonical.** Σ_m as compact convex polytope in ℝ^n with `n = |V| < ∞` is load-bearing. Continuum / mean-field / large-n limits are deferred to a hypothetical "AFD-∞" layer.

### 1.4 What this *does not* commit the canonical to

(N-1) AFD-T5 says nothing about **K-stratum dynamics**. K-state graph (AFD-D5) and barrier-order K-selection (AFD-T7) are separate.

(N-2) AFD-T5 says nothing about **temperature, noise, or stochasticity**. Layer-3 axiomatics (P-F-A1 Package II, OP-0021 T_*) are unaffected.

(N-3) AFD-T5 says nothing about the **value** of `C_AFD(F_i, F_j)`. The "tight exponent β^0.89" question is OP-AFD-004a (Layer 3).

(N-4) AFD-T5 says nothing about **multi-formation coupling**. K-field structure (AFD-T2 extension) and σ-inheritance (OP-0008) are separate.

(N-5) AFD-T5 says nothing about the **observer / observer-moduli** layer (OMS-2.0). Observer-dependent costs are a CV-1.15+ topic.

### 1.5 R1 promotion in promotion-pipeline terms

Per `THEORY/canonical/canonical.md` §1.1 and `theorem_status.md` §Canonical Spec Version History, the next canonical bump is **CV-1.14**. The current targeting (per `00_index.md` of 2026-05-12) is **CV-1.14 = H-MORSE-Local Cat B + Package II Pre-Theorem Cat B**, yielding 59A/16B/5C/5R = 85 claims.

If AFD-R1 promotion happens instead (an alternative track per `afd_theorem_registry.md` and 99_summary.md Option 1), CV-1.14-AFD adds:
- AFD-T9 (Cat A, by-inspection)
- AFD-D1..D5 (Definitions)
- AFD-T1 (Cat A, restatement of T8-Core)
- AFD-T5 (Cat A modulo Claim B.3)
- AFD-T6 (Cat A, barrier preorder)
- (optional) AFD-T11 = OP-AFD-003 attainment

If AFD-T5 enters at Cat A modulo Claim B.3, the canonical must either (a) wait for Claim B.3 verification before promotion, or (b) admit AFD-T5 as Cat B with explicit "modulo" qualifier in `theorem_status.md`. **The brainstorming question:** which of these is healthier for the canonical?

Tentative position (revisitable): admit AFD-T5 as **Cat A on the standing assumption that E is analytic + o-minimal sublevel-set theory applies**. This is structurally analogous to other Cat A claims that depend on Łojasiewicz inequality (e.g. T14). The "modulo Claim B.3" is then read as "modulo a standard fact in o-minimal geometry that this codebase has not yet explicitly cited." This phrasing is honest and does not require waiting for the citation pass to promote.

---

## Part 2 — Catalog of mathematical backbones, grouped by R1 role

The catalog is organized into five groups by R1 role:

- **Group A (Essential):** load-bearing for AFD-T5 R1. Cannot be removed without invalidating the proof.
- **Group B (Future leverage):** not needed for R1, but plausible R2/R3 entries; AFD-T6, AFD-T7, AFD-T8, future AFD-1 may activate them.
- **Group C (Layer-3 deferred):** stochastic / large-deviation / kinetic-theory machinery; not for R1.
- **Group D (Reductive risk):** tools that AFD must compare against but never reduce to (CN10 violation risk).
- **Group E (Speculative):** brainstorming bench; tentative connections, no commitment.

Each entry has: **(α)** one-paragraph definition; **(β)** SCC connection; **(γ)** R1 role; **(δ)** failure modes if invoked at R1 (or, for deferred items, conditions for future activation).

### Group A — Essential R1 inputs

#### A1. Real analytic geometry / o-minimal structures

(α) An **o-minimal structure** on ℝ is a collection of subsets of ℝ^n (n = 1, 2, ...) closed under Boolean operations, projection, and Cartesian product, in which definable subsets of ℝ are exactly the finite unions of points and open intervals. Standard examples: semi-algebraic sets (Tarski-Seidenberg), globally subanalytic sets (Wilkie 1996 for ℝ_{an,exp}). Key theorem (van den Dries 1998, §3.2): every definable set has finitely many connected components, each definable and locally path-connected with finite intrinsic diameter.

(β) **Direct SCC connection.** Sublevel sets `M(c) = {u ∈ Σ_m : E(u) ≤ E_{F_i} + c}` for analytic E are definable in the o-minimal structure ℝ_{an} (real-analytic functions on compact analytic manifolds), per Łojasiewicz 1959. Path-components of M(c) are definable subsets of Σ_m and inherit the o-minimal finiteness + finite-intrinsic-diameter properties.

(γ) **R1 essential** — load-bearing for Lemma L3 (uniform Lipschitz bound on minimizing sub-sequence) which feeds T-OP-AFD-003-A. Without o-minimal-theory commitment, AFD-T5 lacks Cat A backbone.

(δ) **Failure mode.** If E is *merely continuous* (e.g. SCC variants with non-polynomial double-well), o-minimal theory does not apply. AFD-T5 would downgrade to Cat B in such variants. Mitigation: canonical CV-1.13 assumes A3 b_D = 0 (analyticity), so the o-minimal hypothesis is consistent with what is already canonical.

#### A2. Łojasiewicz-Kurdyka inequality / KL gradient flow

(α) The **Łojasiewicz inequality**: for E real-analytic and `u_0` a critical point, there exist θ ∈ (0, 1/2], C > 0, ε > 0 such that `‖∇E(u)‖ ≥ C · |E(u) - E(u_0)|^{1-θ}` for `‖u - u_0‖ < ε`. **Kurdyka-Łojasiewicz (KL)** generalizes to o-minimal C^1 functions. Consequence: gradient flow of E starting near `u_0` either converges to a critical point or escapes the neighborhood. No oscillation.

(β) **Direct SCC connection.** T14 (canonical Cat A): the gradient flow `u̇ = -∇E(u)` on Σ_m converges to a critical point from any initial condition. Basins B_{F_i} = {u : gradient flow from u limits to a representative of F_i} are well-defined.

(γ) **R1 essential** — AFD-D2 (deterministic basin) requires T14, which requires KL. Already integrated.

(δ) **Failure mode.** If E is C^1 but not analytic and KL fails, basin definitions break down. Mitigation: canonical analyticity assumption.

#### A3. Compact convex polytope geometry of Σ_m

(α) **Σ_m = {u ∈ [0,1]^n : Σu_i = m}** is a compact convex polytope: bounded, closed, convex, finitely many extreme points. Diameter `√2 · √n` in Euclidean norm. Linear segments between any two points of Σ_m lie in Σ_m.

(β) **Direct SCC connection.** Σ_m is canonical (T-PF-A1-AR Cat A). Polytope structure underlies Lemma L1 (constant-speed reparametrization), Lemma L2 (PL approximation), and the entire Approach B (T-OP-AFD-003-B PL finite-dimensional reduction).

(γ) **R1 essential.** Already deeply integrated; nothing new needed for R1.

(δ) **Failure mode.** None on R1. Future extension to non-polytope state spaces (continuum, non-convex, non-Euclidean) would require replacement.

#### A4. Arzelà-Ascoli compactness

(α) A family of continuous functions from `[0,1]` to a compact metric space is **relatively compact** under the uniform topology iff it is **equicontinuous**. Sub-sequence extraction is the workhorse of direct-method existence proofs.

(β) **Direct SCC connection.** T-OP-AFD-003-A Step 3 uses Arzelà-Ascoli to extract a uniformly convergent sub-sequence of equi-Lipschitz minimizing paths. T-OP-AFD-003-B Step 3 reuses it.

(γ) **R1 essential** — load-bearing standard tool.

(δ) **Failure mode.** None as long as Lemma L3 supplies a uniformly Lipschitz minimizing sequence. If L3 fails (Claim B.3 unprovable), Arzelà-Ascoli is unavailable in the needed form. *This is the same fragility as A1.*

#### A5. BV lower-semicontinuity (Ambrosio-Fusco-Pallara 2000)

(α) For `f_l → f` pointwise (or in L^1), if `TV(f_l)` is bounded, then `f ∈ BV` with `TV(f) ≤ liminf TV(f_l)`. Total variation is lower-semicontinuous under pointwise convergence.

(β) **Direct SCC connection.** T-OP-AFD-003-C uses BV-LSC for Var_D and J_K under uniform limits. AFD-D9 (Var_D) and AFD-D10 (J_K) are defined as TV of compositions.

(γ) **R1 essential** for the general (λ_D, λ_K > 0) version of AFD-T5. The minimal (λ_D = λ_K = 0) version uses only Bar continuity.

(δ) **Failure mode.** BV-LSC requires L^1 convergence of compositions. For D ∘ γ this works (D Lipschitz, AFD-T2 Cat A). For K_act ∘ γ this requires vineyard transversality — the Cat B caveat in `02_development.md` §7.2.

#### A6. Spectral graph theory (Chung 1997)

(α) The graph Laplacian `L = D - A` (D = degree matrix, A = adjacency) has eigenvalues `0 = λ_1 ≤ λ_2 ≤ ... ≤ λ_n`. The **Fiedler value λ_2** controls Cheeger constants, mixing times, and bottleneck behavior.

(β) **Direct SCC connection.** T8-Core (Cat A) uses λ_2 in the phase-transition criterion β/α > 4λ_2/|W''(c)|. AFD-T1 (Cat A) is a restatement. Spectral identity of canonical 15×15 grid is computed in `CODE/scc/graph.py`.

(γ) **R1 essential — already deeply integrated.**

(δ) **Failure mode.** None for R1. Multi-graph, weighted, or signed-Laplacian extensions are deferred.

#### A7. Convex analysis of energy on simplex

(α) Continuous functions on compact convex polytopes attain their extrema. The simplex Σ_m is the standard ground for convex optimization on probability vectors (Boyd-Vandenberghe).

(β) **Direct SCC connection.** Used implicitly throughout — every "min over Σ_m" calculation uses compactness + continuity.

(γ) **R1 essential** — already integrated.

(δ) **Failure mode.** None.

### Group B — Future leverage (R2/R3 candidates)

#### B1. Conley index theory

(α) **Conley index** (Conley 1978; Mischaikow-Mrozek 1995, 2002) assigns to each isolated invariant set N of a flow a homotopy class `h(N)` invariant under continuation. Basins, attractors, repellers, and saddle sets all have Conley indices. The **Conley-Morse graph** is a directed graph whose nodes are isolated invariant sets and whose edges are connecting orbits.

(β) **SCC connection.** AFD-D2 (deterministic basin) is a Conley-style attractor (`h(B_{F_i})` is the homotopy class of a point — trivially attracting). AFD-D5 (K-state graph) is a Conley-Morse-flavored graph of formation states. AFD-D8 (transition cost between states) is a quantitative refinement of Conley connecting-orbit existence.

(γ) **R2 leverage** — not needed for R1 but **natural fit for AFD-1** (next AFD layer). The Conley index framework provides a *qualitative* invariant for AFD-D2 / AFD-D5 that is preserved under continuation (parameter sweeps), giving a topological-robustness statement that AFD currently lacks.

(δ) **Activation conditions for R2.** Conley index theory requires careful treatment of *isolating neighborhoods* — these must be constructible for SCC basins. The technical work: define an isolating neighborhood `U(F_i)` for each basin and prove `B_{F_i}` is its maximal invariant set. Once established, AFD inherits all Conley machinery (homological continuation, computational Conley index by Mrozek). Plausible CV-1.15 entry.

#### B2. Stratified Morse theory (Goresky-MacPherson 1988)

(α) **Stratified Morse theory** extends classical Morse theory to manifolds with corners or singular spaces. Energy E is *stratified Morse* if its restriction to each stratum is Morse and the gradient transversally crosses strata. Critical points include classical interior critical points + critical points on strata + critical points on stratum boundaries.

(β) **SCC connection.** Σ_m is a polytope with **strata** = faces of all dimensions (interior, codim-1 faces u_i = 0 or u_i = 1, ..., vertices). E restricted to each face is a polynomial. The **vineyard set V** (locus where K_act jumps) is itself stratified.

(γ) **R2 leverage** — provides the language for OP-AFD-003c-K_act vineyard transversality. The Cat A path for K_act requires showing that generic admissible γ meets V transversally; this is precisely a stratified-transversality statement (analog of Sard's theorem for stratified spaces).

(δ) **Activation condition.** Needed for OP-AFD-003c-K_act. The actual proof of vineyard transversality requires: (a) V is a Whitney-stratified codim-1 subset of Σ_m; (b) Adm(F_i, F_j) acts transversally to V except on a meager subset. Both are plausible but not yet established. Plausible R2 / OP-AFD-003c.

#### B3. Persistent homology / TDA (Edelsbrunner-Harer 2010)

(α) **Persistent homology** tracks topological features (connected components H_0, holes H_1, ...) as a filtration parameter varies. Each feature has a birth-death pair, summarized in a persistence diagram or barcode.

(β) **SCC connection.** Already integrated as `scc/k_soft.py`: `K_soft(u) = Σ φ(ℓ_i)` over H_0 persistence bars of the level-set filtration of u. K_act = integer count of components above threshold = H_0 Betti number at threshold. K-state graph (AFD-D5) is morally the discrete summary of H_0 persistence trajectories.

(γ) **R1 leverage if K_soft variant chosen.** Per `02b` §C.2, AFD-T11-soft (J_K via K_soft) is Cat A unconditional. This **is** R1-relevant: AFD-T5 in K_soft form is the cleanest Cat A statement.

(δ) **Failure mode.** Adopting K_soft changes the meaning of AFD-D10 (J_K becomes a soft-aggregated cost, not an integer-jump cost). Conceptual cost (see `02b` §C.3). If user prefers K_act primary, this stays at Cat B worst-case and the leverage activates only for OP-AFD-003c resolution.

#### B4. Coarse-graining / projection methods (Givon-Karniadakis 2004; Gyongy-Krylov 1996)

(α) **Coarse-graining** projects a high-dimensional dynamical system onto a lower-dimensional macro-state space. The projected dynamics may be Markov (if a *projection-Markov property* holds) or non-Markov (memory kernels). In SCC: u ∈ Σ_m (high-dim) → formation state F ∈ V_form (low-dim discrete).

(β) **SCC connection.** AFD itself is a coarse-graining: u_field → (F_i, K_act, σ). AFD-D3 (representative selection u*_{F_i}) is a deterministic section of the projection map.

(γ) **R2 leverage** — natural framework for OP-AFD-006 (Markov / lumpability). If the projected dynamics F_t = π(u_t) is Markov, AFD inherits a clean transition-kernel structure. If not Markov, memory effects appear. AFD currently sidesteps this question; Conley-index continuation gives a non-stochastic alternative.

(δ) **Activation condition.** Markov-projection criteria (Schütte-Sarich 2013 "molecular dynamics" treatment) require timescale separation. SCC at zero temperature is deterministic, so the question is about *Conley-Morse* coarse-graining, not Markov. Plausible R3.

#### B5. Symbolic dynamics / Markov partitions / lumpability

(α) **Symbolic dynamics** codes orbits of a continuous dynamical system as infinite sequences over a finite alphabet via a **Markov partition** of state space. Compatible with topological entropy, mixing rates, periodic-orbit counting.

(β) **SCC connection.** K-state graph (AFD-D5) is a symbolic alphabet. Trajectories in u-space project to walks on the K-state graph. Lumpability = the projection's Markov property.

(γ) **R3 leverage** — beyond AFD-T5; activated when AFD couples to Layer-3 stochasticity.

(δ) **Activation condition.** Requires Layer-3 + a temperature scale.

#### B6. Discrete Morse theory (Forman 1998)

(α) **Discrete Morse theory** assigns a Morse function on a CW or simplicial complex such that each simplex is either critical or paired with a neighbor in a discrete gradient. Compatibly captures Morse-theoretic features of polytope-like spaces.

(β) **SCC connection.** Σ_m is a polytope = simplicial complex. E restricted to face barycenters or vertex values defines a discrete Morse function. Critical cells = local minima / saddles / maxima.

(γ) **R2 leverage** — useful for OP-AFD-010 (finiteness of V_form). Discrete Morse on the canonical 15×15 simplicial decomposition of Σ_m gives a *finite* count of formation states by Morse inequalities.

(δ) **Activation condition.** Choice of discrete Morse function on Σ_m's natural simplicial structure (triangulation). Discrete-Morse rigor needs Forman 1998 framework explicitly. Plausible R2.

#### B7. Variational analysis / epi-convergence (Rockafellar-Wets 1998)

(α) **Epi-convergence** is the convergence notion appropriate for variational problems. Functionals epi-converge iff their epigraphs converge in the Painlevé-Kuratowski sense. Equivalent to Γ-convergence for proper l.s.c. functionals on metric spaces.

(β) **SCC connection.** Γ-convergence framing (Approach C in `01_exploration.md`) is the natural language for relaxation arguments on J_AFD. Currently AFD-T5 uses direct method (Approach A) instead of Γ-convergence (Approach C); the latter is a backup.

(γ) **R2 leverage** — Approach C in `01_exploration.md` §3 reserved. Activates if Approach A fails (it didn't) or as a complementary route for sensitivity analysis (OP-AFD-003e).

(δ) **Activation condition.** Requires choosing the right topology on Adm(F_i, F_j); uniform is standard but other choices possible (BV, W^{1,p}).

#### B8. Lyapunov stability / LaSalle invariance

(α) **Lyapunov stability**: a critical point u_* is stable if every neighborhood admits an invariant sub-neighborhood. **LaSalle invariance principle**: trajectories of a gradient flow on a compact set converge to the largest invariant subset of the zero-set of E-derivative.

(β) **SCC connection.** AFD-D1 (strict local minimizer) implies Lyapunov stability. T14 (gradient-flow convergence) is the LaSalle conclusion. Both already canonical.

(γ) **R1 essential, already integrated.** No new work needed.

(δ) **Failure mode.** None.

#### B9. Metric geometry / intrinsic distances (Burago-Burago-Ivanov 2001)

(α) **Intrinsic metric** on a path-connected metric space X: `d_int(x, y) = inf{L(γ) : γ path from x to y in X}`. **Length space**: X with intrinsic metric where d_int agrees with the metric on small neighborhoods. **Compactness + length space** ⇒ closed bounded sets have rectifiable connecting curves.

(β) **SCC connection.** Path-components of M(c) (sub-level sets of E) are length spaces under the induced Euclidean metric. Claim B.3 is exactly an intrinsic-diameter statement.

(γ) **R1 leverage** — provides the language for Claim B.3 even if its proof relies on o-minimal theory (A1).

(δ) **Failure mode.** None as a language tool. The substantive question is whether intrinsic diameter is *uniform* across thresholds, which is the o-minimal continuity question.

### Group C — Layer-3 deferred

#### C1. Freidlin-Wentzell large deviations (Freidlin-Wentzell 1998)

(α) For SDE `du = -∇E(u) dt + √(2T) dW`, the **quasipotential** `V(u_0, u_1) = inf_γ ∫(|u̇ + ∇E|²/4) ds` over paths γ: [0,T] → ℝ^n governs the small-T behavior of exit times and transitions. **AFD-T8** (EK Compatibility) ultimately rests on this.

(β) **SCC connection.** Layer-3. AFD-T5 attainment is the *deterministic* analog: γ_* exists at zero noise. The FW instanton at small noise is the **scaling limit** of γ_*, but the identification is non-trivial (OP-AFD-005).

(γ) **Deferred to R3 / OP-AFD-005.** AFD-T5 R1 does not invoke FW. AFD-T8 R2/R3 will.

(δ) **Activation condition.** Requires axiomatizing T_* (OP-0021) + reflected Brownian motion on Σ_m (Lions-Sznitman, already cited in canonical for langevin.py via F3 axiom).

#### C2. Eyring-Kramers / Bovier-Den Hollander metastability

(α) **Sharp Kramers formula**: for Brownian motion in a double-well potential at low temperature, the mean exit time from the metastable well is `τ ∼ (2π/|λ_{saddle}^-|) · √(|det Hess E(u_{saddle})| / det Hess E(u_*)) · exp(ΔE/T)`. Bovier-Den Hollander reformulates as eigenvalue + capacity.

(β) **SCC connection.** Package II of canonical CV-1.14 program. AFD-T8 (Cat C currently) aims to ground EK in SCC notation.

(γ) **Deferred** — Layer-3, requires H-MORSE-Saddle, OP-0021 T_*, and reflected-Langevin EK adaptation (literature gap per `CV114_H_MORSE_PACKAGEII/06_packageII_dependency_map.md`).

(δ) **Activation condition.** Requires AFD-T5 R1 (existence of minimizing path = FW instanton) + H-MORSE-Saddle (saddle nondegeneracy). Multi-session work.

#### C3. Hamilton-Jacobi-Bellman / viscosity solutions (Crandall-Ishii-Lions)

(α) The **quasipotential** V(u_*) solves a Hamilton-Jacobi equation `(|∇V|² - 2∇E · ∇V) = 0` with boundary condition V(u_*) = 0. **Viscosity solutions** are the appropriate weak-solution concept for HJB on compact sets with non-smooth data.

(β) **SCC connection.** Quasipotential identification (OP-AFD-005) ultimately reduces to viscosity-solution uniqueness on Σ_m. Layer-3.

(γ) **Deferred** — appears at OP-AFD-005 promotion.

(δ) **Activation condition.** Needs FW (C1) first.

#### C4. Onsager-Machlup path integration

(α) **Onsager-Machlup functional** `S[γ] = ∫(|γ̇ + ∇E|²/2 + (1/2) Δ E ) ds` gives the *most probable path* of the SDE in the sense of maximizing the path-density. Refinement of FW quasipotential.

(β) **SCC connection.** Layer-3+; relates γ_* to small-noise *typical* path. Not needed for AFD-T5.

(γ) **Deferred** — speculative R3.

(δ) **Activation condition.** Needs FW (C1) + finite-noise refinement.

#### C5. Reflected stochastic processes (Lions-Sznitman 1984)

(α) **Reflected Brownian motion** on a compact convex set Σ_m: SDE with normal-reflection boundary condition. Generator is `-Δ` with Neumann BC. Existence + uniqueness theory.

(β) **SCC connection.** F3 axiom in canonical; underlies `scc/langevin.py`. Needed for Layer-3 + Package II.

(γ) **Deferred** — already axiomatized in canonical, but Cat C / pending T_* registration.

(δ) **Activation condition.** Needs T_* (OP-0021).

### Group D — Reductive risk (compare, do not absorb)

#### D1. Optimal transport / Wasserstein (Villani 2009)

(α) **Wasserstein-2 metric**: `W_2(μ, ν)² = inf_{π} ∫ |x - y|² dπ` over couplings π of measures μ, ν. **Otto's calculus**: gradient flows in W_2 of relative-entropy functionals give Fokker-Planck / heat equations.

(β) **SCC connection.** Σ_m as a probability simplex (m=1 case literally) embeds into a Wasserstein space. The transport term `E_tr` of canonical SCC is OT-flavored.

(γ) **Reductive risk.** CN10 forbids reductive claims of form "SCC is OT". Comparative use only. **Useful as a structural analog**, never as a definitional reduction.

(δ) **Risk if mis-applied.** Adopting W_2 metric on Σ_m for AFD admissible class would silently lose the *predicate-level* distinctions that SCC operators (closure, distinction, transport) encode separately. The four energy terms (CN5) would conflate.

#### D2. Allen-Cahn / Cahn-Hilliard equations

(α) **Allen-Cahn**: `u_t = Δu - W'(u)` on continuum domain with W double-well. Gradient flow of `∫ (|∇u|²/2 + W(u)) dx` in L². Sharp-interface limit (Modica-Mortola) gives minimal-surface evolution.

(β) **SCC connection.** SCC's W(u) = u²(1-u)² is the Allen-Cahn double-well. E_cl ∼ ∫|∇u|² + λ W(u) on a graph is the discrete Allen-Cahn energy. Barrier scaling exponents (β^{0.89} numerical) resemble Modica-Mortola sharp-interface asymptotics.

(γ) **Reductive risk.** CN10 explicitly forbids "this is just Allen-Cahn". Allen-Cahn is on continuum; SCC is on graphs. Allen-Cahn has a single primitive (u); SCC has dual primitives (closure / distinction). Comparative use allowed, reduction forbidden.

(δ) **Risk if mis-applied.** Adopting Allen-Cahn's continuum limit silently for SCC at large n would erase graph-Laplacian dependence (λ_2) that drives T8-Core. Numerical evidence for β^{0.89} is consistent with Modica-Mortola but does not imply identity.

#### D3. Mountain Pass / linking theorems

(α) **Ambrosetti-Rabinowitz mountain pass**: under (PS) compactness condition, if E has a "mountain pass geometry" (two basins separated by a higher region), there exists a critical point with critical value equal to the inf-max over paths.

(β) **SCC connection.** Tempting analog for AFD's barrier-cost setup. *But* AFD explicitly **rejects** mountain pass (Approach E in `01_exploration.md` §3) because mountain pass invokes Hessian-based linking arguments that conflict with AFD-T9 (H-MORSE Non-Necessity).

(γ) **Reductive risk + explicitly rejected.** Mountain pass is a *critical-point theorem*, not an *attainment theorem*. AFD-T5 is about path-attainment, not critical-value attainment. Different mathematical content.

(δ) **Risk if mis-applied.** Confusing "γ_* attains the barrier" with "saddle point attains the mountain-pass critical value" silently introduces saddle nondegeneracy (Morse hypothesis) that AFD-T9 explicitly avoids.

#### D4. Γ-convergence (De Giorgi)

(α) Sequence of functionals `F_l : X → ℝ` **Γ-converges** to `F : X → ℝ` if: (i) for every `x_l → x`, `F(x) ≤ liminf F_l(x_l)`; (ii) for every x, exists `x_l → x` with `F(x) ≥ limsup F_l(x_l)`. Standard convergence for variational problems with scale.

(β) **SCC connection.** Approach C of `01_exploration.md` §3. Re-frames Bar as a Γ-limit of regularized functionals. Useful for sensitivity (OP-AFD-003e) and for the Allen-Cahn ↔ sharp-interface analog (but reductive risk per D2).

(γ) **Comparative tool**, not reductive. Allowed at R2 for sensitivity work.

(δ) **Risk if mis-applied.** Γ-limit identification *across* scales could silently merge layers of AFD. Stay within a fixed scale.

#### D5. Mean curvature flow (Brakke 1978; Huisken)

(α) Geometric evolution: hypersurface `Σ_t` moves with velocity proportional to mean curvature. Singular at finite time generically; weak solutions via Brakke flow / level-set method.

(β) **SCC connection.** Sharp-interface limit of Allen-Cahn (D2). Boundary `∂{u > 1/2}` evolves under mean curvature in the limit. SCC's `E_bd = α |∂{u > 1/2}|²` is the discrete-graph analog of `|Hessian of interface|²`.

(γ) **Reductive risk.** Comparative use only.

(δ) **Risk.** Same as D2.

#### D6. Reaction-diffusion bifurcation (Crandall-Rabinowitz 1971)

(α) For a family of nonlinear operators `F(u, λ) = 0`, **bifurcation theorems** describe the branching of solutions at parameter values λ where the Frechét derivative is singular. Classical: simple-eigenvalue bifurcation, Hopf, transcritical.

(β) **SCC connection.** β-driven phase transitions in SCC (T8-Core) are bifurcations: critical β_c determined by spectral gap λ_2. **OP-0006 (multi-formation foundations)** asks about bifurcations in K. **OP-AFD-002** asks about K-stratum regularity at bifurcation points.

(γ) **R2 leverage** — useful for OP-AFD-002, OP-0006 refinement.

(δ) **Risk if mis-applied.** Treating SCC as "just reaction-diffusion bifurcation" silently merges the dual-mode operators (closure + distinction) into a single nonlinearity. Avoid.

### Group E — Speculative / brainstorm bench

#### E1. Categorical structure / basin-graph functors

(α) **Category theory** describes mathematical structures via objects + morphisms + composition + identity. Functors are structure-preserving maps between categories.

(β) **SCC connection.** AFD-D5's K-state graph is a *categorified* object: nodes = K-strata, edges = barrier-bounded transitions. Composition = path concatenation. Identity = constant path. **Functor candidates:** parameter sweep `β ↦ (V_form_β, transitions_β)` is functorial if appropriately defined.

(γ) **Speculative R3.** Could provide a clean language for OP-AFD-009 (Conley extension to multi-parameter family).

(δ) **Risk.** Categorical formalism is *cheap* to write down but *expensive* to make load-bearing. Avoid adopting unless a specific theorem (functoriality, naturality, universal property) clarifies a previously murky statement.

#### E2. Information geometry (Amari)

(α) Statistical manifolds carry a Riemannian metric (Fisher information), a dual pair of affine connections (e^-connection, m^-connection), and divergences (KL, α-divergences).

(β) **SCC connection.** Σ_m as a probability simplex carries Fisher information. **Tempting reduction**: Bar(γ, F_i) looks like a KL-flavored divergence; the SCC energy E looks like negative log-likelihood.

(γ) **Reductive risk + speculative.** Information-geometric framing would *implicitly reduce* SCC to a statistical-manifold model, conflicting with CN10. Allowed only in a strictly comparative role.

(δ) **Risk.** Same as D1 (OT).

#### E3. Sub-Riemannian geometry

(α) **Sub-Riemannian manifold**: a Riemannian manifold with a non-integrable distribution. Geodesics are restricted to be tangent to the distribution. Examples: Heisenberg group, Carnot groups.

(β) **SCC connection.** **Speculative**: if K-strata define a *foliation* of Σ_m with codimension 1, paths in AFD's admissible class restricted to a single K-stratum follow a "horizontal" distribution. Vertical = K-jump direction. Sub-Riemannian geometry could quantify the K-jump cost in geometric terms.

(γ) **Speculative R3.** Provides language for J_K as a sub-Riemannian distance.

(δ) **Risk.** Highly speculative. Requires proving K-strata are a foliation (codim-1 smooth distribution), which is currently OP-AFD-002.

#### E4. Differential inclusions (Filippov 1988)

(α) **Differential inclusion** `u̇ ∈ F(u)` where F is a set-valued map. Generalizes ODE to non-smooth dynamics with multiple branches at each point.

(β) **SCC connection.** Gradient flow of E on Σ_m at the polytope boundary `∂Σ_m` requires projection; this can be formalized as a differential inclusion with reflection. Smoothness of γ_* (OP-AFD-003d) likely involves Filippov-style analysis at boundary points.

(γ) **R2/R3 leverage** for smoothness questions.

(δ) **Risk.** None as a tool. Activation depends on OP-AFD-003d engagement.

#### E5. Sard's theorem / generic transversality

(α) **Sard's theorem**: critical values of a smooth map ℝ^n → ℝ^m have measure zero. **Thom-Smale transversality**: generic maps are transversal to a given submanifold.

(β) **SCC connection.** Vineyard transversality for OP-AFD-003c-K_act (sketched `02b` §C.5) invokes a Sard-type argument.

(γ) **R2 leverage** for closing OP-AFD-003c-K_act.

(δ) **Risk.** None.

#### E6. Ricci flow / heat kernel intuition

(α) **Ricci flow**: `∂g/∂t = -2 Ric(g)` evolves a Riemannian metric. **Graph Ricci flow** (Ollivier-Ricci, Lin-Lu-Yau) on weighted graphs. **Heat kernel**: short-time asymptotics encode geometric information.

(β) **SCC connection.** **Speculative**: SCC's `E_cl` involves a quadratic form on u_i u_j with weights depending on edge presence. Could be viewed as a "discrete Ricci form". β-sweep ↔ time in Ricci flow?

(γ) **Speculative R3.** Could give a *single-parameter* family of SCC theories parameterized by Ricci-flow time, with phase transitions at curvature-collapse times.

(δ) **Risk.** Highly speculative. Provides intuition only.

#### E7. Topological complexity (Farber 2003)

(α) **Topological complexity** `TC(X)` = minimum number of continuous "motion planning" sections required to define a path between any two points in X. Connected to LS category.

(β) **SCC connection.** Adm(F_i, F_j) viewed as a function space; TC of Σ_m gives an a-priori complexity bound for the admissible class.

(γ) **Speculative R3.** Of academic interest; no obvious immediate AFD application.

(δ) **Risk.** None — purely theoretical.

#### E8. Mean field games / mean field control (Lasry-Lions 2007)

(α) **MFG**: many-agent stochastic-control problems where each agent reacts to the *distribution* of all agents. Solution is a coupled Hamilton-Jacobi-Bellman + Fokker-Planck system.

(β) **SCC connection.** Multi-formation extension of AFD (OP-AFD-009 multi-K_field graph): each formation can be viewed as an agent in a mean-field interaction.

(γ) **R3 speculative** — interesting Layer-3 framing.

(δ) **Risk.** None as speculation; requires careful sidesteps of reductive claim (CN10).

#### E9. Random projections / Johnson-Lindenstrauss

(α) **JL lemma**: random linear maps `ℝ^n → ℝ^k` for `k ∼ log n / ε²` preserve pairwise distances up to factor (1±ε) with high probability.

(β) **SCC connection.** K_soft computation involves H_0 persistence on a graph; large-n scaling could exploit JL projections to reduce computational complexity.

(γ) **Speculative R3** — for `scc/k_soft.py` implementation scaling, not for canonical theory.

(δ) **Risk.** None — engineering tool.

#### E10. Tropical geometry / amoebas

(α) **Tropical semiring**: max + plus. **Amoeba** of a polynomial: log-image of its zero set. Tropicalization gives piecewise-linear limits.

(β) **SCC connection.** PL approximation in Approach B (T-OP-AFD-003-B) has tropical-flavor. Could be made rigorous via tropicalization.

(γ) **Speculative R3** — academic interest.

(δ) **Risk.** None.

#### E11. Spectral sequences in algebraic topology

(α) Spectral sequences compute homology by successive approximation. Examples: Leray-Serre, Mayer-Vietoris.

(β) **SCC connection.** **Speculative**: K-state graph (AFD-D5) has H_1 (cycles), H_2 (higher cells if defined). A spectral sequence on the K-state graph could decode multi-formation cooperativity.

(γ) **Speculative R3+** — academic interest only.

(δ) **Risk.** None.

#### E12. Renormalization group (Wilson, Kadanoff)

(α) **RG**: iterated coarse-graining of statistical-mechanical systems. Fixed points = critical phenomena. Universality classes.

(β) **SCC connection.** β-driven transition in SCC (T8-Core) is a critical phenomenon; β_c is the critical coupling. RG perspective could explain why the barrier exponent β^{0.89} is universal (or not) across different SCC variants.

(γ) **Speculative R3+** — could resolve the β^{0.89} vs β^{1.2} numerical discrepancy noted in `10_afd0_and_op004_session.md`.

(δ) **Risk.** Reductive — "SCC is a critical phenomenon" silently merges Layer-2 deterministic theory into Layer-3 statistical physics. Stay comparative.

#### E13. Computational complexity / oracle bounds

(α) **Complexity**: P, NP, #P, BQP. **Oracle model**: cost of access to a function as black box.

(β) **SCC connection.** "Compute γ_*" given E as an oracle is a *concrete computational problem*. Complexity-theoretic bounds could quantify how hard AFD-T5 is to use in practice.

(γ) **R3+ academic** — interesting from a "computational AFD" viewpoint.

(δ) **Risk.** None — separate question from canonical theory.

---

## Part 3 — Pairwise compatibility matrix

The 30+ tools above interact. Some reinforce (use of one strengthens use of another), some conflict (using both creates contradiction), some are independent.

### 3.1 Reinforcement clusters

**Cluster R-1: o-minimal / KL / Łojasiewicz / spectral-graph / convex.**
A1, A2, A3, A6, A7. All Group A. Mutually reinforcing — they share the analyticity hypothesis and constitute the "load-bearing R1 stack" for AFD-T5. Each tool fills a gap the others leave: A1 (sublevel-set topology), A2 (gradient-flow convergence), A3 (state space), A6 (phase transition), A7 (extremum on simplex).

**Cluster R-2: Conley / stratified Morse / discrete Morse / persistent-homology.**
B1, B2, B3, B6. The "topological qualitative" cluster. Mutually reinforcing — Conley index uses Morse-theoretic data, stratified Morse refines on singular spaces, persistence quantifies, discrete Morse provides combinatorial reduction. AFD's R2/R3 extension naturally lives in this cluster.

**Cluster R-3: BV / VL / Γ-convergence / variational analysis.**
A5, B7, D4. The "variational" cluster. BV-LSC is the workhorse, Γ-convergence is the relaxation language, variational analysis (epi-convergence) is the unifying framework. Currently AFD uses A5 directly; B7/D4 are reserve languages.

**Cluster R-4: FW / EK / HJB / Onsager-Machlup / reflected SDE.**
C1, C2, C3, C4, C5. The "Layer-3 stochastic" cluster. Mutually reinforcing: FW provides quasipotential, EK provides sharp rate, HJB is the PDE characterization, OM is the path-density refinement, reflected SDE is the canonical state-space embedding. R1 deferred; activated together at Package II.

**Cluster R-5: AC / MCF / RD-bifurcation / RG.**
D2, D5, D6, E12. The "continuum statistical-physics" comparative cluster. Mutually reinforcing in the comparative sense — they share continuum / scaling / universality intuitions. **Reductive risk if any one is silently absorbed.**

### 3.2 Conflict pairs (silently incompatible)

**Conflict P-1: o-minimal (A1) vs. continuous-only E.**
If we drop A3 b_D = 0 (analyticity), A1 fails and AFD-T5 downgrades. SCC variants that allow non-polynomial double-well violate this.

**Conflict P-2: K_act primary (B3 partial) vs. AFD-T5 Cat A unconditional.**
K_act has vineyard discontinuity → BV-LSC for J_K is only Cat A generic. K_soft (B3 full) removes the conflict. Choosing K_act keeps the conflict; choosing K_soft resolves it.

**Conflict P-3: Mountain pass (D3) vs. AFD-T9 (H-MORSE Non-Necessity).**
Mountain pass uses Hessian linking; AFD-T9 says we don't need it. Don't invoke mountain pass at R1.

**Conflict P-4: OT reduction (D1) vs. four-energy-term independence (CN5).**
Wasserstein structure merges transport-cost intuitions; SCC keeps four separate energies. Don't reduce.

**Conflict P-5: AC/Modica-Mortola limit (D2) vs. graph-Laplacian dependence (T8-Core).**
AC continuum limit erases λ_2 dependence; T8-Core needs λ_2. Don't take continuum limit silently.

### 3.3 Independent pairs (no interaction)

Many tools are simply independent: A4 (Arzelà-Ascoli) and E1 (categorical) have no direct interaction. B5 (symbolic dynamics) and B7 (variational analysis) are independent in AFD-T5 scope.

---

## Part 4 — R1 minimum essential set (honest)

After the audit and the catalog, the R1-essential mathematical-backbone set is exactly:

| Tool | Role |
|---|---|
| **A1** (o-minimal / real analytic geometry) | Sublevel-set finiteness + intrinsic-diameter (Claim B.3) |
| **A2** (KL / Łojasiewicz) | T14 gradient-flow convergence → AFD-D2 basin definition |
| **A3** (compact convex polytope) | Σ_m structure (T-PF-A1-AR Cat A) |
| **A4** (Arzelà-Ascoli) | Minimizing-sequence sub-sequence extraction |
| **A5** (BV-LSC, Ambrosio-Fusco-Pallara) | TV lower-semicontinuity for Var_D and J_K |
| **A6** (spectral graph theory) | λ_2 in T8-Core (used by AFD-T1) |
| **A7** (convex analysis on simplex) | Continuous-on-compact attainment of extrema |

Plus, depending on K_act vs K_soft decision:

| Conditional tool | If K_act | If K_soft |
|---|---|---|
| **B3** (persistent homology) | partial (K_act = H_0 count, no Lipschitz) | full (K_soft = Σ φ(ℓ_i), Lipschitz) |

**Total R1 essential: 7 tools (8 with persistent homology).** No others are load-bearing at R1.

**Implicit assumption.** The proof of AFD-T5 *requires* analyticity of E. This is canonical (A3 b_D = 0) but rarely explicitly cited as load-bearing for AFD. R1 promotion makes this dependency *visible* in canonical, which is healthy.

---

## Part 5 — R2/R3 deferred set with activation conditions

The deferred set has 20+ tools. Each has a specific activation condition.

| Tool | R-Level | Activation condition |
|---|---|---|
| B1 (Conley index) | R2 | AFD-1 isolating-neighborhood construction |
| B2 (stratified Morse) | R2 | OP-AFD-003c-K_act vineyard transversality |
| B4 (coarse-graining / projection) | R3 | Markov-projection question for AFD ↔ u_field |
| B5 (symbolic dynamics) | R3 | Layer-3 + temperature scale |
| B6 (discrete Morse) | R2 | OP-AFD-010 finiteness of V_form |
| B7 (variational analysis / epi-convergence) | R2 | OP-AFD-003e sensitivity |
| B8 (Lyapunov / LaSalle) | R1 already | Used implicitly via T14 |
| B9 (metric geometry / intrinsic distance) | R1 language | Already used in L3 |
| C1 (Freidlin-Wentzell) | R3 | OP-0021 T_* registration |
| C2 (Eyring-Kramers) | R3 | H-MORSE-Saddle + Package II |
| C3 (HJB / viscosity) | R3 | After FW |
| C4 (Onsager-Machlup) | R3+ | After FW + small-noise corrections |
| C5 (reflected SDE) | R3 | Already axiomatized via F3 |
| E1 (categorical) | R3+ | When functoriality of `β ↦ V_form_β` becomes load-bearing |
| E2 (information geometry) | speculative | Allowed only comparatively |
| E3 (sub-Riemannian) | R3+ | After K-stratum foliation proved (OP-AFD-002) |
| E4 (differential inclusions) | R2 | OP-AFD-003d (smoothness) |
| E5 (Sard) | R2 | OP-AFD-003c-K_act |
| E6 (Ricci flow / heat kernel) | speculative | Intuition only |
| E7 (topological complexity) | speculative | None foreseen |
| E8 (mean field games) | R3+ | Multi-formation extension |
| E9 (JL random projections) | engineering | K_soft scaling |
| E10 (tropical) | speculative | None foreseen |
| E11 (spectral sequences) | speculative | None foreseen |
| E12 (RG) | speculative | Reductive risk |
| E13 (complexity theory) | engineering | Practical AFD usage |

**Highest-priority R2 candidates (post-R1):**
1. **B2 + E5 (stratified Morse + Sard)** for OP-AFD-003c-K_act Cat A path.
2. **B1 (Conley index)** for AFD-1 layering and topological robustness.
3. **C1 (FW)** for Layer-3 quasipotential.
4. **B6 (discrete Morse)** for OP-AFD-010 finiteness of V_form.

---

## Part 6 — Reductive-risk catalog (what NOT to do at R1)

R1 promotion is a one-way door. The following silent absorptions would *contaminate* canonical irreversibly:

### 6.1 The five forbidden silent absorptions

(F-1) **"AFD is the variational analysis of Allen-Cahn on a graph."** (D2 absorption.) **No.** SCC has dual-mode primitives (closure + distinction) that Allen-Cahn lacks. AC is a single-field gradient flow; SCC has four energy terms (CN5).

(F-2) **"Adm(F_i, F_j) is the path space of an OT problem on Σ_m."** (D1 absorption.) **No.** SCC's transport-energy E_tr is one of four energies, not the defining structure. Wasserstein structure merges what SCC keeps separate.

(F-3) **"γ_* is a Mountain Pass critical point."** (D3 absorption.) **No.** AFD-T9 says we don't need H-MORSE / Hessian linking. γ_* is a path-minimizer, not a critical point of E.

(F-4) **"Bar(γ, F_i) is an information-geometric divergence."** (E2 absorption.) **No.** Σ_m is the volume-constrained simplex; SCC's E is not a Kullback-Leibler functional.

(F-5) **"SCC is the renormalization-group fixed point of some statistical-mechanical model."** (E12 absorption.) **No.** R1 deterministic theory has no temperature; RG language is Layer-3 at best.

### 6.2 The three allowed comparative invocations

(A-1) **AC ↔ SCC discrete Allen-Cahn analog.** Allowed as motivation; never as reduction. Useful for explaining the barrier-exponent β^{0.89} numerical observation without claiming it follows from Modica-Mortola.

(A-2) **OT ↔ SCC E_tr resemblance.** Allowed as motivation for the transport-cost term; never as substitution for the four-energy structure.

(A-3) **FW instanton ↔ AFD γ_***. Allowed as Layer-3 identification *to be proved* (OP-AFD-005). Not silently assumed.

### 6.3 The audit principle

For each comparative invocation of a Group D tool: write a one-sentence statement of the form

> "Tool X resembles SCC in feature Y, but **differs in feature Z** which is load-bearing for SCC. Therefore the resemblance is structural, not definitional."

Failure to write Z is a CN10 violation flag.

---

## Part 7 — Substantive new-direction brainstorming

This is the brainstorming core. New directions not on the OP catalog, ranked by speculative-but-plausible.

### 7.1 Direction N-1: AFD on a moduli space

**Statement.** Instead of fixing a graph G and varying u, fix a "graph-type" (e.g. all 15×15 grids with boundary conditions varied) and vary the *graph*. The space of admissible graphs is a moduli space; SCC theory should be a sheaf on this moduli space.

**Connection to existing OPs.** OP-AFD-009 (multi-K_field graph). OMS-2.0 (observer-moduli, already in canonical Appendix).

**R-level.** R3+; OMS framework already partially exists. Could be a "post-AFD-1" project.

**Required tools.** B1 (Conley continuation under parameter sweep), B7 (epi-convergence), E1 (functorial language).

**Value.** Would make M-A2 (Aut(G) stabilizer question, Priority 1 of today's plan) a *structural* property rather than a configuration-specific check.

### 7.2 Direction N-2: Floer-theoretic AFD

**Statement.** AFD's minimizing path γ_* is morally a *Floer trajectory* for the Morse-Floer complex of E on Σ_m. The K-state graph is the Floer complex's underlying chain complex.

**Connection.** B1 (Conley homology can be reformulated as Floer-style). B6 (discrete Morse refinement).

**R-level.** R3+ speculative.

**Required tools.** Floer-style analysis on bordered manifolds (Σ_m is bordered: ∂Σ_m faces of the polytope).

**Value.** Provides a *categorified* AFD where K-state graph nodes are objects, edges are 1-morphisms, paths are 2-morphisms. Could unify AFD-T5, AFD-T6, AFD-T7 under a single Floer-complex language.

**Risk.** Floer theory in the bordered case is technically demanding; activation depends on whether the categorification simplifies or merely repackages existing AFD content.

### 7.3 Direction N-3: AFD as a stratified topological field theory

**Statement.** Generalize: SCC is a *functor* from a category of "perception input data" to a category of "formation states". AFD describes the action of this functor on morphisms (perception transitions).

**Connection.** E1 (categorical) + OMS-2.0 framework.

**R-level.** R3+ very speculative.

**Required tools.** E1 + extensive categorical machinery (operads, ∞-categories?).

**Value.** Long-term: a clean axiomatic re-presentation of SCC where all current "commitments" become functorial data. Short-term: probably distracting.

### 7.4 Direction N-4: Spectral-flow refinement of AFD-T5

**Statement.** As γ_* traverses from F_i to F_j, the Hessian eigenvalues of E along γ_* may cross zero — *spectral flow*. The spectral flow is a topological invariant (integer-valued under transversality). Conjecture: spectral flow along γ_* is related to the K-jump count.

**Connection.** B1 (Conley index includes spectral data), B2 (stratified Morse).

**R-level.** R3 speculative.

**Required tools.** Atiyah-Patodi-Singer-style spectral-flow theory adapted to E on Σ_m.

**Value.** Could give a *topological* explanation for K-selection (OP-0005) — K is selected such that spectral flow vanishes / takes a specified value.

**Risk.** Spectral flow conventionally requires unbounded self-adjoint operators on a Hilbert space; SCC's finite-dim Hessian doesn't naturally fit. Adaptation non-trivial.

### 7.5 Direction N-5: Persistent Conley index

**Statement.** Combine B1 (Conley) + B3 (persistence): as β varies, the Conley index of each F_i evolves; track birth-death of formation states via a *Conley persistence diagram*.

**Connection.** Directly addresses OP-AFD-009 (Conley extension) and OP-0005 (K-selection at varying β).

**R-level.** R2-R3 plausible.

**Required tools.** B1 + B3 + computational Conley (Mrozek et al.).

**Value.** Would give a *parameter-sensitive* canonical statement of "when does a formation state appear or disappear under β-sweep". Plausibly resolves OP-0005-DYN.

**Why now?** Persistent Conley index is a mature research area (Mrozek, Edelsbrunner et al. 2010s). Adapting to SCC is "technology transfer", not original theory development.

### 7.6 Direction N-6: Geometric measure theory for J_K

**Statement.** Treat K_act as a function on Σ_m with **finite perimeter** discontinuity locus V (codim-1). Apply Federer-Volpert theory of BV functions: K_act has a well-defined *jump set* with a normal-trace formulation.

**Connection.** A5 (BV-LSC) + B2 (stratified Morse).

**R-level.** R2 — directly addresses OP-AFD-003c-K_act Cat A path.

**Required tools.** Ambrosio-Fusco-Pallara Chapter 3 (BV theory) + jump-set theory.

**Value.** Could close OP-AFD-003c-K_act at Cat A unconditional via "K_act ∈ BV(Σ_m) with finite-perimeter jump set V" → standard BV trace + LSC suffices.

**Why this is concrete.** Unlike most speculative directions, this has a *named theorem to invoke* and a *finite paper-distance* from the current proof. **Strong R2 candidate.**

### 7.7 Direction N-7: Tropical / piecewise-linear AFD

**Statement.** Replace E by its PL approximation E^{PL}_N (per Approach B). The PL energy on Σ_m's natural simplicial decomposition has *combinatorial* structure: each cell has a linear E, gradient is constant per cell, basins are PL polytopes.

**Connection.** B6 (discrete Morse) + E10 (tropical) + A3 (polytope).

**R-level.** R2-R3.

**Required tools.** Discrete Morse + PL gradient flow + tropical geometry of E.

**Value.** Computable AFD: for a PL E, basins, transitions, and γ_* are exact combinatorial objects. This would *bridge canonical theory to numerical experiments* — currently exp38, exp60 numerical results lack a formal correspondence.

**Risk.** PL approximation may miss curvature-sensitive features of analytic E. Need careful Γ-limit (D4) argument.

### 7.8 Direction N-8: KAM / averaging principle for AFD

**Statement.** When E is *nearly integrable* (small perturbation of a separable structure), AFD trajectories should be approximated by *quasi-periodic* motions with a small drift to formation. **KAM theorem** or **Nekhoroshev averaging** could give sharp bounds on the drift rate.

**Connection.** Layer-3 candidate for "slow" trajectories that linger in basins.

**R-level.** R3 speculative.

**Required tools.** Hamiltonian-mechanics KAM (Pöschel) adapted to gradient + small Hamiltonian perturbation.

**Value.** Could resolve OP-AFD-005 partially by characterizing "near-attracting" trajectories as KAM tori in a perturbative regime.

**Risk.** SCC is gradient (not Hamiltonian); KAM machinery doesn't transfer directly. Speculative.

### 7.9 Direction N-9: Synthetic AFD via simplicial sets

**Statement.** Replace continuous Adm(F_i, F_j) by its *simplicial-set* model. Each n-simplex is an "AFD n-cell": a continuous map Δ^n → Adm(F_i, F_j). Higher cells encode homotopies of paths.

**Connection.** E1 (categorical) + B3 (persistence).

**R-level.** R3+ speculative.

**Required tools.** ∞-category theory (Lurie).

**Value.** Long-term: AFD as a homotopy-coherent structure. Short-term: probably overkill.

### 7.10 Direction N-10: AFD over the spectrum of Σ_m's symmetry group

**Statement.** Σ_m has a natural action by S_n (permutations preserving the simplex). AFD restricted to S_n-equivariant paths gives a "symmetric AFD". Conversely, the full AFD breaks S_n; the breaking pattern encodes formation state identity.

**Connection.** Symmetry-breaking is implicit in M-A2 (Priority 1 of plan.md). The *theoretical* analog is here.

**R-level.** R2.

**Required tools.** Representation theory of S_n on Σ_m (or its sub-tableau when G has Aut(G) ⊂ S_n).

**Value.** Provides the *theoretical complement* to M-A2 numerical verification (Priority 1). Could give an a-priori reason why generic minimizers are stabilizer-trivial.

### 7.11 Direction N-11: Quantum AFD

**Statement.** Replace u by a quantum state |u⟩ (vector in a Hilbert space, normalized), E by a Hamiltonian H acting on |u⟩. Quantum AFD = transition amplitudes between quantum formation states.

**Connection.** None to current SCC; entirely speculative.

**R-level.** R∞.

**Risk.** This is **not** what SCC is about. Listing here only to acknowledge and *explicitly reject*.

### 7.12 Direction N-12: AFD with explicit time horizon

**Statement.** Current AFD has time-parametrized paths but no *time horizon* (paths run from s=0 to s=1, but s is not physical time). Introduce a horizon T: minimize over paths of *true time-length* T.

**Connection.** Layer-3 — gives FW its time scale.

**R-level.** R3.

**Value.** Would make the FW identification (OP-AFD-005) concrete by fixing the time-rescaling between AFD's parameter s and the SDE's physical time t.

### 7.13 Direction N-13: AFD with explicit observer

**Statement.** AFD currently is observer-free. Introduce an observer (OMS-2.0): each formation is observed by a state |obs⟩ in observer moduli space. Transitions are *observer-relative*.

**Connection.** OMS-2.0 already in canonical Appendix.

**R-level.** R2 — could be the next major canonical extension.

**Value.** Bridges AFD to the observer-moduli OMS layer. Could give a clean observer-AFD foliation of canonical theory.

### 7.14 Direction N-14: Constructive AFD via fixed-point iteration

**Statement.** Define γ_* as a fixed point of a contraction map on Adm. Iteration converges in polynomial steps.

**Connection.** Approach B's PL refinement is morally an iterative algorithm.

**R-level.** R3 (engineering / numerical).

**Value.** Would give an algorithmic version of AFD-T5 — currently the proof is non-constructive (Arzelà-Ascoli is non-constructive).

**Risk.** Non-trivial; the natural contraction might not exist for J_AFD.

### 7.15 Direction N-15: AFD as a thermodynamic limit

**Statement.** Take n → ∞ (graph size) with appropriate scaling of (β, m). Conjecture: AFD-T5 has a sharp thermodynamic limit; the barrier becomes O(n^{something}).

**Connection.** OP-AFD-007 (multi-K_field), E12 (RG).

**R-level.** R3 speculative.

**Risk.** SCC is canonically finite-graph; "thermodynamic limit" is a comparative concept (CN10 caution).

---

## Part 8 — Promotion-pipeline implications

### 8.1 R1 sequencing

If AFD-R1 is the next promotion:

**Sub-step R1.0 (pre-promotion verification, ~1 day):**
- Verify Claim B.3 via van den Dries 1998 §3.2 + §4.1 citation hunt.
- Audit `02_development.md` for any other unmentioned implicit assumption.
- Run AFD-T5 statement past 1–2 external readers (or self-audit pass).

**Sub-step R1.1 (canonical edit, ~1 day):**
- Add AFD-T5 to canonical.md §13 with "Cat A modulo Claim B.3" qualifier *or* "Cat A on the standing assumption of o-minimal sublevel-set theory".
- Update `theorem_status.md` (move OP-AFD-003 from active to resolved).
- Append CHANGELOG entry for CV-1.14-AFD.

**Sub-step R1.2 (working-layer carry):**
- Update `afd_open_problems.md`: OP-AFD-003 → RESOLVED.
- Update `afd_theorem_registry.md`: AFD-T5 → Cat A.
- Append session log.

### 8.2 What happens to the other AFD-R1 candidates

| AFD candidate | Status pre-R1 | Status post-R1 | Notes |
|---|---|---|---|
| AFD-T9 | Cat A by-inspection | promoted | unchanged |
| AFD-D1..D5 | Definitions | promoted | unchanged |
| AFD-T1 | Cat A (restatement) | promoted | unchanged |
| AFD-T6 | Cat A | promoted | unchanged |
| **AFD-T5** | **Cat A modulo B.3** | **promoted (with caveat)** | needs B.3 verification or explicit caveat |
| AFD-T7 | Cat B | not promoted yet | (separate R2 question) |
| AFD-T8 | Cat C | not promoted | Layer-3 |
| AFD-T11 (optional) | Cat A modulo B.3 (= absorbed into T5) | absorb into T5 | recommendation: not separate |

### 8.3 What R1 promotion does to outstanding OPs

| OP | Pre-R1 | Post-R1 |
|---|---|---|
| OP-AFD-001 (TopSig V continuity) | open | open |
| OP-AFD-002 (K_act stratification) | open | open |
| OP-AFD-003 | "Cat A modulo B.3" | promoted (Q-A); B/B variants remain open |
| OP-AFD-003a-revised | M severity | M severity, blocking elegant Cat A |
| OP-AFD-003c-K_act | M | M |
| OP-AFD-003c-K_soft | closed | closed (in K_soft variant) |
| OP-AFD-004 | Cat B (W7-Day2) | unchanged |
| OP-AFD-005 | open | partially fed (existence side) |
| OP-AFD-006..010 | open | open |

R1 propagation is **clean** — no silent resolution of any OP except OP-AFD-003 (the deliberate one).

### 8.4 What R2 looks like

After R1, the next AFD-track session targets:

- **Priority A:** OP-AFD-003a-revised (Claim B.3 verification). 30–60 min citation hunt.
- **Priority B:** OP-AFD-003c-K_act Cat A via direction N-6 (BV geometric measure theory).
- **Priority C:** AFD-T7 (positivity) + AFD-T8 (FW compatibility) refinement.
- **Priority D:** AFD-1 layer scaffolding (Conley index extension, direction N-5 persistent Conley).

---

## Part 9 — Final recommendation + decision points

### 9.1 Position on R1 timing

**Recommendation (revisitable):** Execute AFD-R1 promotion in **two stages**.

- **Stage R1-α (immediate next session):** verify Claim B.3 (Priority A above), then promote AFD-T5 as Cat A unconditional.
- **Stage R1-β (after R1-α):** if Claim B.3 verification reveals additional gaps, downgrade AFD-T5 to "Cat A under explicit standing assumption" with the gap registered as a new OP.

If the user prefers, R1-α and R1-β can collapse into a single session.

### 9.2 Position on K_act vs K_soft

**Recommendation (revisitable):** Keep K_act as the **primary** AFD-D10 (consistent with integer-K interpretation); register K_soft as an **alternative variant** (AFD-D10-soft) with its Cat A result (T-OP-AFD-003-C-soft). This:

- Honors the original K_act intent (integer counting of objects).
- Preserves a clean Cat A escape hatch via K_soft if K_act vineyard work proves intractable.
- Avoids over-committing canonical to either variant.

### 9.3 Position on R2 priorities

**Recommendation (revisitable):** R2 should focus on **two threads simultaneously**:

1. **Vineyard transversality (B2 + E5 + N-6)** for OP-AFD-003c-K_act Cat A path. Medium severity, high payoff.
2. **AFD-T7 Cat A** (positivity Cat B → Cat A by removing the WS+SR side conditions). Connected to OP-AFD-004 family.

R3 should target FW compatibility (OP-AFD-005) and Layer-3 stochastic embedding.

### 9.4 Position on new directions (Part 7)

**Strong R2 candidates:**
- **N-5 (Persistent Conley index):** mature external technology, direct OP-0005-DYN fit. Worth 3–5 sessions.
- **N-6 (BV geometric measure theory for J_K):** directly closes OP-AFD-003c-K_act. Single paper-distance.
- **N-10 (S_n-equivariant AFD):** theoretical complement to M-A2 numerics. Single session for sketch.

**Speculative but worth keeping on radar:**
- **N-1 (AFD on moduli space):** bridges OMS-2.0 to AFD; multi-session.
- **N-4 (spectral-flow refinement):** could unify K-selection. Multi-session.

**Reject for now (despite intellectual appeal):**
- N-2 (Floer), N-3 (TQFT), N-9 (simplicial sets), N-11 (quantum). Too speculative; reductive risk; insufficient AFD payoff.

### 9.5 Decision points the user must close

Before R1 promotion, the user should decide:

(D-1) **K_act vs K_soft as canonical primary.** (Recommendation: K_act primary, K_soft secondary variant.)

(D-2) **Claim B.3 verification: do it as a session or absorb as standing assumption.** (Recommendation: do it as a session — cheap and decisive.)

(D-3) **AFD-T11 as separate row or absorbed into AFD-T5.** (Recommendation: absorbed into T5 — less proliferation.)

(D-4) **R1 sequencing with H-MORSE-Local.** (Recommendation: AFD-R1 first because it's strictly closer to closed-form completion; H-MORSE-Local Cat B is parallel.)

(D-5) **Whether to invoke any of Part 7's new directions in R1.** (Recommendation: no — keep R1 strictly to AFD-T5+T6+T9+T1+D1..D5. New directions are R2+.)

If the user defers all five decisions, the default is the conservative R1 package described in §8.

---

## Appendix — Side commentary on the GPT-5 meta-research report

The GPT-5 report's main suggestion — *"comparative framework report + annotated bibliography + theorem-skeleton appendix"* — is **partially implemented** here:

- **Comparative framework report:** ✓ (Parts 2 + 3 + 4)
- **Annotated bibliography:** ✗ (deferred — Parts 2 entries cite tools but not specific papers in BibTeX form)
- **Theorem-skeleton appendix:** ~ (Parts 7 contains new-direction skeletons; existing AFD theorem skeletons already in `02_development.md` and `02b`)

The GPT-5 report's *"highest-priority clarifying question"* — what decision must this research support — is implicitly answered here: **the decision is whether and how to execute AFD-R1 promotion**. This is a single concrete decision, not a broad publication-strategy question.

The report's *"single-bundle deliverable"* (comparative report + bibliography + theorem skeleton, 20–30 hours) is partially this document (catalog + comparison + new-direction skeleton, ~6 hours of writing). A 20+ hour expansion would add:

- Full citation pass for each tool in Part 2.
- Annotated bibliography (per-paper, ~50 entries).
- Theorem-skeleton drafts for the top 3 new directions (N-5, N-6, N-10).
- Risk-register for the five reductive-risk tools (D1-D6).

These are deferred to future sessions if the user wants the full bundle.

---

## Closing note

This brainstorming document inventories the mathematical-backbone landscape around AFD-T5 R1. It is intended as a **navigation aid for the next 5–15 sessions** of AFD development, not as a decisional document. All "recommendations" are provisional positions to be revised when the user's actual decisions land.

**Single-line conclusion.** AFD-T5 R1 promotion is technically ready; the only standing question is whether to verify Claim B.3 first (recommended) or admit AFD-T5 with an explicit "modulo o-minimal sublevel-set continuity" qualifier (alternative). All other backbone choices are either already canonical (Group A) or deferred (Groups B-E).

---

*End of `20_AFD_T5_R1_mathematical_toolkit_brainstorm.md`. Brain-storming pass complete.*
