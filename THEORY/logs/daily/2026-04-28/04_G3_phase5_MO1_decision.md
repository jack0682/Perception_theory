# 04_G3_phase5_MO1_decision.md — MO-1 Face Decision (W5 Strategic Plan §0.4 Decision 2)

**Session:** 2026-04-28 (W5 Day 2 MODERATE, Block 3 14:30-15:30)
**Target (from plan.md §3 Block 3 + W5_strategic_plan.md §0.4 Decision 2):** Choose among Options A/B/C for handling MO-1 (Morse theory inapplicability on $\Sigma^K_M$ corners) in multi-formation σ Phase 5 (G3).
**This file covers:** §1 problem statement; §2 Option A (interior-only) detailed; §3 Option B (stratified Morse) detailed; §4 Option C (soft-K detour) detailed; §5 decision criteria + recommendation; §6 W5+ trajectory implications.
**Depends on reading:** `working/MF/multi_formation_sigma.md` (companion file, σ_multi^(A) primary); `canonical.md` §12 OP-0003 MO-1 SIDESTEPPED note (single-formation scope); `open_problems.md` OP-0003 MO-1 entry; `2026-04-27/03_v5b_f_status_update.md` §4 (V5b-F mechanism transfer to multi-formation, conditional on NQ-173 Branch B).
**Status:** decision recorded with explicit rationale; W5+ multi-formation σ trajectory determined.

---

## §1. Problem Statement

### 1.1 What MO-1 is

From `canonical.md` §12 + `open_problems.md` OP-0003:

> **MO-1: Morse Theory Inapplicability on $\Sigma^K_M$.** The K-field manifold $\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$ has corners where one or more $u^{(j)}$ saturates the boundary of $[0,1]^n$. At corners, Morse-theoretic Hessian analysis fails (Hessian is not the usual second-derivative tangent-space operator; gradient flow can hit corners). Standard Morse-theory tools (Hessian index, Morse complex, λ-cobordism) do not directly apply.

**Status (canonical, single-formation scope)**: SIDESTEPPED — single-formation σ-framework operates on $\Sigma_m$ (no corners at $u(x) \in \{0, 1\}$ generically because volume constraint forces $\bar u = c$, and Morse-0 minimizers in spinodal interior keep $u \in (0, 1)$ a.e.).

**Status (multi-formation σ Phase 5)**: **RETURNS active**. On $\Sigma^K_M$, even if each $\Sigma_{m_j}$ alone avoids corners, the *product* manifold has corners when *any* $u^{(j)}$ saturates. Furthermore, the simplex constraint $\sum_k u^{(k)}(x) \leq 1$ creates additional boundary structure (saturation faces) that single-formation σ doesn't encounter.

### 1.2 Why this matters for σ_multi

Per `working/MF/multi_formation_sigma.md` §5.6 forward gap M2:

> σ_j is undefined when $u^{(j)*}$ touches the boundary of $[0,1]^n$. σ_jk inherits this issue. Whether σ_multi^(A) is well-defined on $\Sigma^K_M$ corners is an open question.

For σ_multi to be a useful invariant of K-field minimizers, it must be defined on the **set of minimizers** that the optimization algorithm actually reaches. If the optimizer routinely hits corners (e.g., when $\lambda_{\text{rep}}$ is large enough that one formation pushes another to saturation), σ_multi must handle this.

### 1.3 The decision

**W5 Strategic Plan §0.4 Decision 2** offers three options. This file evaluates each, then commits to one as primary (with the others preserved as alternatives per meta-prompt §4.3 alternative preservation).

---

## §2. Option A — Interior-Only σ_multi (Pragmatic)

### 2.1 Statement

Define σ_multi^(A) (per `working/MF/multi_formation_sigma.md` §5) only on the **interior** $\Sigma^{K,\circ}_M = \{\mathbf{u} \in \Sigma^K_M : 0 < u^{(j)}(x) < 1 \text{ for all } j, x; \sum_k u^{(k)}(x) < 1 \text{ for all } x\}$. At corners, σ_multi is **undefined** by convention; declare so explicitly.

This sidesteps MO-1 by **scope restriction**, not by resolution. Justified by:
- Single-formation σ already operates this way (canonical Lemma 1 hypothesis: $u^* \in \Sigma_m^\circ$ Morse-0 minimizer; corner case excluded).
- For sufficiently small $\lambda_{\text{rep}}$ and well-separated $\mathbf{u}^*$, interior is generic.

### 2.2 Strengths

- **Pragmatic and compatible with single-formation precedent**: extends Commitment 14's interior-only convention to multi-formation. No theory leap required.
- **Allows W5 G3 closure**: σ_multi^(A) interior definition is the deliverable; MO-1 is acknowledged-and-deferred, not resolved-and-claimed.
- **Compatible with V5b-F mechanism transfer**: the V5b-F H1 Branch (bulk-localized Goldstone) operates in interior of free BC graph; analog operates in interior of $\Sigma^K_M$.
- **Time budget**: σ_multi^(A) interior definition + numerical K=2 baseline can complete W6-W7 (within initiation window).

### 2.3 Weaknesses

- **Doesn't address MO-1 directly**: a formation that saturates ($u^{(j)*}(x_0) = 1$ at some $x_0$) is not covered. For "strong" formations (small $m_j$, high $\beta$, narrow interface) this happens.
- **Boundary behavior unanalyzed**: what does σ_multi^(A) do as a minimizer approaches a corner from interior? Continuity? Limit existence? These questions are postponed.
- **Not a closed theory**: future work must either extend Option A to corners (becoming Option B) or accept the gap as permanent.

### 2.4 Required follow-up if A chosen

- Document the interior-restriction convention explicitly in σ_multi^(A) canonical entry text (when promoted W6+).
- Register as forward gap: "σ_multi^(A) at $\Sigma^K_M$ corners — open per MO-1 inheritance".
- Numerically verify that K=2 baseline minimizers stay interior in chosen parameter regime (G3 Day 3 numerical).

### 2.5 Compatibility with V5b-F Branch verdict

- **V5b-F Branch B (~70% a priori)**: bulk-localized Goldstone with mode-mixing near boundary. The "boundary" in V5b-F single-formation case is the *graph* boundary (free BC). The analogous "boundary" in multi-formation σ_multi^(A) interior case is the *inter-formation boundary* — the region where $u^{(j)}$ and $u^{(k)}$ supports approach each other. **Option A handles this naturally** because the inter-formation boundary is in the interior of $\Sigma^K_M$ (not at corners): formations have $u^{(j)} \in (0, 1)$ even at the inter-formation transition.
  - V5b-F Branch B verdict (when produced Day 3+) supports Option A.
- **V5b-F Branch A (H1 alone)**: even cleaner — bulk Goldstone fully resolves; interior assumption suffices.
- **V5b-F Branch C/D (H2/H3)**: still works in interior; mechanism details differ but interior assumption unaffected.

---

## §3. Option B — Stratified Morse on $\Sigma^K_M$ (Theoretically Rigorous)

### 3.1 Statement

Develop **stratified Morse theory** for $\Sigma^K_M$ — analogous to Goresky-MacPherson stratified Morse theory for singular spaces, adapted to the corner structure of products of simplices. Define σ_multi to extend continuously across strata, including corner strata where formations saturate.

Mathematical framework: $\Sigma^K_M$ is a stratified space with strata indexed by saturation patterns:
- Top stratum (K-formations interior): $\Sigma^{K,\circ}_M$.
- Codim-1 strata (one site of one formation saturated): finite collection.
- Codim-d strata (d sites saturated across formations).
- Lowest stratum: full saturation patterns (most degenerate).

Stratified Morse theory provides:
- Local Morse-Bott structure on each stratum.
- Transition operators between strata (the "tangential" vs "transversal" Hessian decomposition).
- Stratum-aware σ-tuple definition.

### 3.2 Strengths

- **Theoretically maximal rigor**: σ_multi defined everywhere on $\Sigma^K_M$, including all corners.
- **Matches existing literature**: stratified Morse theory has 40+ year tradition (Goresky-MacPherson 1988); applying to SCC's specific corner structure is a focused extension.
- **Long-term canonical-ready**: the resulting σ_multi is a complete invariant on $\Sigma^K_M$, not a partial invariant.

### 3.3 Weaknesses

- **Time-heavy**: stratified Morse theory is a multi-week project even with literature support. W5 G3 budget (~18h) cannot accommodate.
- **Risk of over-engineering**: SCC's actual minimizers (numerically observed) may stay interior most of the time; stratified theory could be machinery without practical use cases.
- **Dependence on corner regularity**: $\Sigma^K_M$ corners under simplex constraint $\sum_k u^{(k)}(x) \leq 1$ are not standard polyhedral cones; they are intersections of $K$ simplices in a complicated way. Stratification structure is non-trivial to define cleanly.
- **W5 deliverable risk**: W5 G3 closure (working file + numerical K=2) becomes infeasible if Option B chosen.

### 3.4 Compatibility with V5b-F Branch verdict

- Independent of V5b-F branch; stratified Morse handles all branches uniformly.

### 3.5 Required follow-up if B chosen

- Multi-week effort: literature review of Goresky-MacPherson + adaptation to product-of-simplices corner structure.
- W5 G3 deliverable scope-cut: only "Option B feasibility study" Day 2; full development W6-W9.
- Re-prioritize W5: G3 yields a study, not a proof; W5 ladder downgrades to Minimal (G0+G1 only).

---

## §4. Option C — Soft-K Detour (Conservative)

### 4.1 Statement

Use the W4-04-21 **K_soft** framework (referenced in `working/SF/from_single.md` §1 derived view) — instead of treating K as an external integer parameter on $\Sigma^K_M$, parameterize the K-formation minimizer state via continuous mode-count statistics on the *single-formation* manifold $\Sigma_m$. Multi-formation structure becomes a *derived* quantity from single-formation $u_t : X \to [0,1]$ + filter rules.

This avoids $\Sigma^K_M$ entirely. σ_multi becomes a discrete invariant on $\Sigma_m$ alone, derived from level-set / mode structure.

### 4.2 Strengths

- **Avoids $\Sigma^K_M$ corners by construction**: no product manifold, no corners.
- **Compatible with W4-04-22 R22 reformulation** (`working/SF/from_single.md` §2 retracted, replacement framework `step_cohesion.md`): conservative continuation of a working line of investigation.
- **Lightest mathematical cost**: σ_multi reuses single-formation Commitment 14 + post-processing.

### 4.3 Weaknesses

- **Trades K-field architecture canonicity** (CN6 K kinetic + CN8 metastable + I9 K-field paradigm): SCC's canonical multi-formation paradigm IS the K-field architecture on $\Sigma^K_M$. Substituting K_soft sidesteps the canonical commitment; this is a "secret retreat" from canonical I9.
- **R22 retraction's caveat applies**: `from_single.md` §2 retracted because the soft-K view's specific quantitative claims were falsified (R17 Weyl scaling, R19 dynamic symmetry, R20 functional form impossibility, V7 P1 softmax probability all failed). The conservative-derived view is **partially retained** as *qualitative* but not *quantitative*. Building σ_multi on soft-K means inheriting the qualitative-only status.
- **Does not actually achieve multi-formation σ**: produces a single-formation invariant that *correlates with* multi-formation structure, not a multi-formation σ-tuple per se. S4 (non-triviality: distinguish K-fields with same per-formation σ_j but different coupling) cannot be achieved without explicit K-field structure.
- **Falls short of G3 deliverable**: G3 P1 explicitly is "multi-formation σ Phase 5 *initiation*". Option C is more like "G3 substitute".

### 4.4 Compatibility with V5b-F Branch verdict

- Independent of V5b-F branch (no inter-formation Hessian analysis to do).

### 4.5 Required follow-up if C chosen

- Re-frame G3 deliverable: "soft-K-derived multi-formation invariant" instead of σ_multi^(A/B).
- W5 G3 closure achievable but at the cost of explicit K-field σ.
- W6+ revisit: when full multi-formation σ becomes urgent (Paper 1 §4), a Cat A/B path through Option A or B will still be needed.

---

## §5. Decision Criteria + Recommendation

### 5.1 Criteria

Per W5 strategic plan §0.4 Decision 2 hint and meta-prompt §4.3:

(D-i) **Continuity with canonical commitments**: I9 K-field architecture, CN5 four-energy-term independence, Commitment 14 σ-framework. Higher = better.

(D-ii) **W5 deliverable feasibility**: Option that lets G3 P1 close within W5 budget (~18h).

(D-iii) **Long-term path to canonical-quality multi-formation σ**: which option leaves a feasible Cat A path for W6+?

(D-iv) **V5b-F Branch B compatibility**: if V5b-F confirms bulk-localized Goldstone (~70% a priori), which option lets the mechanism transfer most cleanly?

(D-v) **No silent resolution of MO-1**: per meta-prompt §8.2 hard constraint, MO-1 must remain explicitly open if not actually resolved.

### 5.2 Scoring

| Criterion | Option A (interior-only) | Option B (stratified Morse) | Option C (soft-K detour) |
|---|---|---|---|
| (D-i) Canonical continuity | **High** (extends Lemma 1 interior convention) | High (full $\Sigma^K_M$ rigor) | Low (sidesteps I9) |
| (D-ii) W5 feasibility | **High** (closeable W5-W6) | Low (multi-week) | High (lightest) |
| (D-iii) Cat A path W6+ | Medium (corner gap remains) | **High** (complete invariant when done) | Low (qualitative only) |
| (D-iv) V5b-F transfer | **High** (inter-formation in interior) | High (uniform) | Low (no Hessian transfer) |
| (D-v) MO-1 honesty | **High** (explicitly defers) | High (resolves) | Medium (sidesteps without admission) |

### 5.3 Recommendation: **Option A (interior-only)** — primary

Option A is selected as the **primary strategy for W5 G3 + W6 W7**. Reasons:

1. **Highest score on criteria (D-i, D-ii, D-iv, D-v)**; tied with B on (D-i) but B fails (D-ii). C fails (D-iii) and (D-iv).

2. **Compatible with V5b-F Branch B mechanism transfer** (~70% a priori): the σ_multi^(A) §5.5 cross-formation Goldstone analog operates entirely in the interior of $\Sigma^K_M$ (formations have $u^{(j)} \in (0, 1)$ at the inter-formation boundary because the simplex constraint is sub-saturated when formations are well-separated).

3. **Honest about MO-1**: explicitly defers MO-1 corner case rather than claiming resolution. Compliant with meta-prompt §8.2 hard constraint.

4. **Time-efficient**: σ_multi^(A) Cat B-target proof feasible in W6 (per `multi_formation_sigma.md` §4.1 effort estimate "2-3 weeks"). Numerical K=2 baseline in Day 3 morning provides empirical confirmation.

5. **Option B kept as W7+ deepening**: when Cat A on full $\Sigma^K_M$ becomes urgent (Paper 1 §4), Option B's stratified Morse approach is the path. **Not abandoned**, just deferred to when needed.

6. **Option C kept as fallback**: if Option A's M3 forward gap (overlapping formations beyond well-separated regime) proves intractable, Option C's soft-K detour can serve as "qualitative reduction" — but this is a fallback, not primary.

### 5.4 Decision (recorded)

**W5 Day 2 W5_strategic_plan.md §0.4 Decision 2: Option A (interior-only σ_multi^(A)).**

### 5.5 Risks of this decision (acknowledged)

- (R1) If V5b-F Branch verdict (Day 3+) turns out NOT to be Branch B (i.e., the bulk-localized hypothesis fails), Option A's clean V5b-F transfer claim weakens. Mitigation: σ_multi^(A) interior definition stands independent of V5b-F transfer; only §5.5 Goldstone analog is conditioned on Branch B.
- (R2) If numerical K=2 baseline (Day 3) shows that even well-separated K=2 minimizers routinely touch corners, Option A's interior-only restriction is empirically too restrictive. Mitigation: expand to Option A+ (interior + first-stratum boundary) as a W6+ refinement.
- (R3) If σ_multi^(A) M1 (tensor-irrep handling) proves more subtle than estimated, Cat B target extends to W8+. Mitigation: A-light fallback (scalar coupling fingerprint without tensor irreps) noted in `multi_formation_sigma.md` §4.2.

---

## §6. W5+ Multi-Formation σ Trajectory

Per Decision: **Option A primary, B as W7+ deepening, C as fallback only.**

### 6.1 W5 (current week, Day 2-7)

- **Day 2 (today)**: σ_multi^(A) initiation (`working/MF/multi_formation_sigma.md`); MO-1 Decision (this file); K=2 baseline script skeleton (`g3_baseline_k2_sigma.py`).
- **Day 3 morning**: scc validation patch (per NQ-191 P2 option, `01_NQ173_v5b_f_verdict.md` §5); re-launch NQ-173 + NQ-174 numerical; G3 K=2 baseline numerical run.
- **Day 3 PM**: σ_multi^(A) refinement based on numerical observations; canonical proposal text completion (per `03_canonical_proposal_v5b_t_update.md`).
- **Day 4-5**: σ_multi^(A) Cat B-target proof attempt (Lemma 5.1 step 3 tensor-irrep handling); numerical K=2 with $\lambda_{\text{rep}}$ sweep.
- **Day 6-7**: W5 close work (G5 SF Round 1-5 merge, possibly G7 NQ-148 σ-jump).

### 6.2 W6

- σ_multi^(A) Cat B → A path (full proof of well-definedness in well-separated regime).
- OQ-A1 (pair-stabilizer tensor-irrep decomposition) → publication-ready proof.
- σ_multi^(A) canonical proposal package → user review for canonical merge.
- NQ-173 → V5b-F Cat B target promotion (if Branch B) or refinement.

### 6.3 W7-W8

- Begin Option B foundations (stratified Morse on $\Sigma^K_M$ corners).
- σ_multi^(A) M3 (overlapping formations) → A-extended version.
- NQ-179 V5b-F mechanism transfer to multi-formation Goldstone — quantitative formula.

### 6.4 W9+

- Approach C (interaction graph) as paper §4 exposition layer.
- Option B mature (full $\Sigma^K_M$ stratified σ_multi).
- Multi-formation σ-framework completion → Paper 1 §4 first draft.

### 6.5 Branching contingency

If R1 (V5b-F Branch B falsified): σ_multi^(A) §5.5 Goldstone analog needs revision but core σ_multi^(A) (Lemma 5.1 well-definedness) unaffected.
If R2 (corners reached frequently in numerics): re-evaluate Option B priority, possibly accelerate to W6.
If R3 (tensor-irrep too subtle): A-light fallback; defer full A to W7-W8.

---

## §7. Hard Constraint Verification

- [x] **No silent resolution of MO-1** — Option A explicitly defers MO-1 to corner case as forward gap; Option B's resolution is registered as W7+ work; Option C's sidestepping is acknowledged as scope cut.
- [x] **canonical 직접 수정 0** — this file is `logs/daily/`; no edit to canonical/.
- [x] **No Research OS** — no numbered subdirs; no D-/S-/T- registries.
- [x] **u_t primitive** — all decisions operate on $u^{(j)}$ field primitivity; no object-first treatment.
- [x] **K not dual-treated** — K is integer throughout; soft-K detour (Option C) is acknowledged as departure from canonical I9 commitment, not silent K continuation.
- [x] **Not reductive to external framework** — Goresky-MacPherson stratified Morse (Option B) cited as comparative tool, not reductive equation.

---

## §8. Cross-References

- σ_multi^(A) primary definition: `working/MF/multi_formation_sigma.md` §5.
- MO-1 canonical status: `canonical.md` §12 + `open_problems.md` OP-0003.
- V5b-F Branch verdict (deferred): `01_NQ173_v5b_f_verdict.md`.
- W4-04-22 R22 retraction (relevant to Option C): `working/SF/from_single.md` §2 retracted; `working/SF/step_cohesion.md` replacement.
- K-field architecture I9: `canonical.md` §11 line 829.
- W5 strategic plan Decision 2: `THEORY/logs/weekly/2026-04-W5/W5_strategic_plan.md` §0.4.

---

**End of 04_G3_phase5_MO1_decision.md.**
**Decision: Option A (interior-only σ_multi^(A)). B preserved for W7+ deepening; C preserved as fallback. W5+ trajectory recorded.**
