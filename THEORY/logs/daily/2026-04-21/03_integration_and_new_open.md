# 03 — Integration & New Open: Canonical Impact + canonical_sub Entry + New Open Questions

**Session:** 2026-04-21
**Target (from plan.md):** Stage 1 C+E foundation — integration of session output with canonical commitments; new open questions registry; canonical_sub.md 2026-04-21 entry draft.
**This file covers:** Canonical impact analysis (§1–§5), proposed canonical changes (§6), partial resolutions of existing open problems (§7), new open questions (§8), canonical_sub.md 2026-04-21 entry draft (§9), prompt improvement notes (§10).
**Depends on reading:** all 6 working files (G1–G6), `01_exploration.md`, `02_development.md`, canonical sections referenced inline.

---

## §1. Canonical Theorems Affected

The session's substantive output touches the following canonical Cat A/B/C theorems:

### 1.1 Cat A theorems re-anchored thermally (no statement change)

- **T-Merge (b)** (Energy Ordering Isoperimetric, Cat A): re-stated under soft-K as "single-mode preference" (G5 §2.2). **Statement preserved**, language updated. Per `working/integer_K_dependency_map.md` §2.2 "Re-prove (retain)".
- **T11** (Γ-Convergence, Cat A): unchanged. M-1 dissolution (G5 §2) reuses T11 directly.
- **T-1, T-3, T-6a/b/Stability, T-7, T-8-Core/Full, T-14, T-20, C-Axioms, QM-1/2/3/4, Predicate-Energy Bridge, T-Bind-Proj, Deep Core Dom 2b, T-Persist-1(b)/(e), T-A2** (19~20 single-formation Cat A): unchanged, survive T → 0 limit. F4.b commitment.

### 1.2 Cat A theorems retired (per `working/integer_K_dependency_map.md` §2.1)

| # | Theorem | Why retired | Replacement in session |
|---|---|---|---|
| 1 | T-Merge (a) — K-Formation Local Minimality on Σ²_M | Σ²_M not used in soft-K; per-formation Hessian PD on Σ^K_M is vacuous | Σ_m Hessian at K_soft ≈ 2 critical points (G3 §3.3 sketch) |
| 2 | Topological Lock — Merge Impossible on Σ²_M | `0 ∉ Σ_{m_2}` argument vacuous in soft-K (no per-formation mass) | Mountain Pass on Σ_m connects K=2 ↔ K=1 basins (G5 §5 R-M1-B) |
| 3 | Coupling Bound Lemma — K-Formation Hessian | `(K-1)λ_rep` factor specific to integer K-pair counting | No replacement statement; Hessian of single-field ℱ_{C+E} (G3 §3.3) |
| 4 | Proposition 1.2 — Fiber Dimension of Σ²_M | Σ²_M not used | No replacement (vacuous question in soft-K) |
| 5 | Theorem 3.1(a,b,d) — Landscape at K=2 Symmetric Point | "K=2 symmetric point" specific to integer K | No direct replacement; Hessian at soft-K ≈ 2 critical points (G3 §3.3) |

**Status:** retirement is **proposed** (working file commit, weekly merge to canonical via canonical_sub.md). User decision required for actual canonical edit.

### 1.3 Cat B theorem retired

| # | Result | Why retired | Replacement |
|---|---|---|---|
| 6 | γ_eff ≈ 0.89 (empirical merge barrier) | "K-merge" as integer transition vacuous; barrier scaling is for *Kramers prefactor on K_soft path*, not "K=2 → K=1 integer transition" | Re-interpretation as Kramers prefactor in M1 dissolution (G5 §4.1); precise re-derivation C-S2 |

### 1.4 Cat C theorems re-proved (statement re-write needed)

Per `working/integer_K_dependency_map.md` §2.3 (3 items):

| # | Theorem | Re-statement direction | Status this session |
|---|---|---|---|
| 7 | T-Persist-K-Sep (Well-Separated, Cat C) | "K independent per-formation persistence on Σ^K_M" → "per-mode persistence of K_soft distribution regimes on Σ_m" | sketched (E-S2 carry) |
| 8 | T-Persist-K-Weak (Weakly-Interacting) | `(K-1)λ_rep` factor reinterpreted as soft-K mode-pair count × overlap | sketched (E-S2 carry) |
| 9 | T-Persist-K-Unified | `Λ_coupling = λ_rep ω_{jk} / min(μ_j, μ_k)` rewritten with mode-pair indices | sketched (E-S2 carry) |

**Status:** statement re-writes proposed but not formalized this session (E-S2). Cat C remains Cat C until full re-proof.

### 1.5 Retracted theorems (canonical §13 R2-R5) confirmed

T-Merge (c)(d)(e) (Mountain Pass on Σ²_M) and K-Saddle Conjecture (R2-R5) remain retracted. Soft-K does not revive them — Mountain Pass on Σ_m (single field) is a different statement (G5 §5 R-M1-B) and applies to a different manifold.

---

## §2. Existing Commitment Notes (CN) Affected

### 2.1 CN substantiated thermally (no retraction)

- **CN6** ("K kinetically determined"): substantiated. "Kinetically" = "Kramers-rate-determined" within ℱ_{C+E} thermal framework. G5 §3.4 + §4.1.
- **CN8** ("formations metastable, not globally optimal"): substantiated. Boltzmann population at finite T. G4 §3.
- **CN14** ("closure expands metastability"): substantiated. Closure raises ΔF in Kramers exponent, extending metastable regime. G5 §3.4.
- **CN12** ("Q_morph persistence-based"): preserved. K_soft uses same H₀ persistence (G1 §6).

### 2.2 CN potentially affected

- **CN5** ("four-term independence is conceptual"): unchanged. ℱ_{C+E} adds two new terms (-T·S, +λ_K·K_soft); now "six-term independence" — generalizes naturally. G3 §5.1.
- **CN4** ("Group F architecturally distinct from A–E"): naming conflict. CN4's "Group F" refers to crisp recovery; this session's F-group = thermal. **Proposed:** rename present F-group to "Group F-thermal" in canonical merge to avoid conflict, or rename CN4's reference. (See §6.1 below.)
- **CN7** ("operator pair, not generic self-referentiality"): partially affected. F-group introduces global entropy S and global K_soft as new structural functionals; one could ask whether these constitute a "third self-referential mode" (resurrecting NQ-2 / P-C). This session **does not** commit to such re-elevation; CN7's dual-mode structure preserved.

### 2.3 CN newly proposed (potential additions)

- **CN15-thermal (proposed):** "Free energy ℱ_{C+E} is the C+E framework's variational object; canonical ℰ is recovered as the T → 0, λ_K → 0 limit."
- **CN16-thermal (proposed):** "The metastability claim of CN6/CN8/CN14 is substantiated by Kramers rates and Witten Laplacian small-eigenvalue spectrum, both at finite T."
- **CN17-thermal (proposed):** "Soft-K K_soft : Σ_m → ℝ_{≥0} is the canonical generalization of integer K; the integer reading is recovered in the sharp-interface limit."

**Status:** proposed. Canonical addition awaits user decision and full session-pipeline (Stage 1 → Stage 6).

---

## §3. Existing Open Problems Status

Per `canonical/open_problems.md` and `working/open_problems_reframing_2026-04-19.md`:

### 3.1 Critical (🔴): F-1, M-1, MO-1

| Problem | Status before | Status after this session |
|---|---|---|
| **OP-0001 / F-1** (K=2 vacuity) | unresolved | **partially dissolved** — vacuity claim re-stated in soft-K terms; thermal occupation framework provides quantitative replacement. Full resolution awaits Stage 5 numerical validation (R-F1-A). |
| **OP-0002 / M-1** (K=1 always preferred) | unresolved | **reframed** — proved theorem (T-Merge (b) Cat A) standing, "preference" is feature not bug. Kramers metastability (G5 §3) provides the framework for K>1 coexistence. Full resolution requires C-S2 (Kramers prefactor on Σ_m). |
| **OP-0003 / MO-1** (Morse inapplicability) | unresolved | **partially dissolved** — Σ²_M corner removed (architectural). Smooth Morse on Σ_m^ε \ V applies. Witten Laplacian provides spectral alternative on discrete graph (statement only). Full resolution: post-Stage-1 (discrete-graph Witten Laplacian). |

**No silent resolution.** Each is "partially dissolved / reframed / sketched" — explicit residuals carried.

### 3.2 High (🟠): OP-0004 Type A/B (already retracted), OP-0005 K-selection, OP-0006 Boundary

| Problem | Status before | Status after this session |
|---|---|---|
| **OP-0005 / K-selection** | open | **substantively addressed**: in soft-K, K is not "selected" but **distributed** (K_soft is continuous). The original framing ("how is K determined?") becomes ("what determines K_soft distribution?"); answered by Gibbs measure ℙ_T at temperature T (G2 §1) + Kramers rates (G5 §3). Full statement of "K_soft selection mechanism" pending CE-S2 phase diagram. |
| **OP-0006 / Boundary** | tentative | not directly addressed this session (P-D in reframing — Non-goal). |
| **OP-0004 / Type A/B** | retracted | unchanged. |

### 3.3 Medium (🟡), Low (🟢)

| Problem | Status |
|---|---|
| OP-0010, 0011, 0012, 0013 | unchanged |
| OP-0020, 0021, 0022 | unchanged (OP-0021 stochastic dynamics partially addressed via F3 Langevin — statement only). |

### 3.4 Reframing categories (from `working/open_problems_reframing_2026-04-19.md` §6)

| Reframed | Status before | Status after this session |
|---|---|---|
| **P-A** (Integer-K / Continuous-u Mismatch) | reframed | **substantially dissolved** — soft-K resolves the integer-continuous gap. Soft-K is a single-field continuous quantity. (Residual: K_hard recovery / sharp-interface limit precision; G1 Prop 4.1 sketch.) |
| **P-D** (Threshold non-principled) | reframed | not addressed (Non-goal — A-purpose work). |
| **P-F** (Zero-T metastability claim) | reframed | **substantially dissolved** — F-group provides finite-T framework. Metastability is now Kramers-rate-determined at T > 0. (Residual: full F3 well-posedness; F4 recovery proofs.) |
| **P-G** (Axiom-implementation divorce) | reframed | not addressed (Non-goal — A-purpose work). |
| **P-B** (External substrate) | reframed | not addressed (Non-goal — D-purpose work). |
| **P-C** (Missing third mode) | reframed | not addressed (NQ-2 carry). |
| **P-E** (25+ parameters origin) | reframed | not addressed; γ_K added (NQ-10 new). |
| **P-H** (Time pre-theoretic) | reframed | not addressed. |
| **N-1** (Soft-Hard switching, single source) | reframed | **partially dissolved** in K-face only (P-A). Threshold-face (P-D) and axiom-face (P-G) remain. |

---

## §4. integer_K_dependency_map.md Audit

Per `working/integer_K_dependency_map.md` §7 "Next Actions":
- The classification "Retire 6 / Re-prove 3 / Re-prove (retain) 1" is **operationalized this session** in G4–G6:
  - Retire 6: G6 §6 (Prop 1.2, Thm 3.1) + G4 §2 (T-Merge (a), Topological Lock, Coupling Bound) + G5 §1 (γ_eff = 0.89 reinterpreted, not retained).
  - Re-prove (retain) 1: T-Merge (b) — G5 §2 statement re-write, proof core (Γ-conv) preserved.
  - Re-prove 3 (T-Persist-K-Sep/Weak/Unified): sketched (§1.4 above). Full re-proof carry to E-S2.

The integer_K_dependency_map.md should be updated post-merge to reflect:
- Retire 5 (Cat A) + 1 (Cat B) → status moved from "Retire (planned)" to "Retire (architectural removal committed in 2026-04-21 session, awaiting weekly canonical merge)".
- Re-prove (retain) 1 (T-Merge (b)) → status moved to "Re-stated in soft-K language; proof core preserved (G5 §2.2)".
- Re-prove 3 (Cat C) → status: "Sketched re-statement; full re-proof E-S2 carry".

---

## §5. NQ-1 (Soft-K Uniqueness) Partial Resolution

Per `working/new_open_questions_2026-04-20.md` NQ-1: 4 candidates ((i) persistence, (ii) Betti, (iii) simplex, (iv) measure).

**Resolution this session (G1 §5):**
- **(i) committed** as canonical choice — minimal disruption to CN12, Lipschitz via CSEH 2007, gradient sparse off vineyard.
- **(ii) parked but related**: reduces to (i) under `φ(ℓ) = ℓ` via Fubini (pre_brainstorm H-A2). Less general.
- **(iii) parked, conflict** with CN12 (loss of spatial info). Activate only if CN12 weakening accepted.
- **(iv) parked**: most general, computationally heavy, integer-output (defeats soft purpose).

**Open part of NQ-1:** are the *theories induced* by (i) vs (ii) vs (iii) the same? E.g., do the same canonical Cat A theorems hold under each? This is **deeper question** beyond the choice of K_soft definition, into the structure of induced theory. Carry as **NQ-1-extended** to post-Stage-1.

---

## §6. Proposed Canonical Changes (for weekly merge consideration)

This session's proposed changes to canonical, organized for user review:

### 6.1 §6 Group F-thermal (new section)

**Proposed:** Add new axiomatic group "Group F-thermal" containing F1 (Gibbs), F2 (Bernoulli entropy), F3 (Langevin — statement), F4 (T-primacy + recovery — statement). Located after Group E (Temporal Transport).

**Rename CN4** to refer to "Group F-crisp" (crisp recovery) to disambiguate from new "Group F-thermal".

**Source:** `working/C/F_group_axioms.md`.

### 6.2 §8.1 Free energy extension

**Proposed:** Add §8.1.5 "Free Energy Functional in C+E Framework" stating ℱ_{C+E} = ℰ - T·S + λ_K·K_soft, with reference to Group F-thermal and λ_K = γ_K · T scaling commitment.

**Source:** `working/CE/free_energy_wellposed.md`.

### 6.3 §5.5 K_soft addition

**Proposed:** Extend §5.5 "Transition Diagnostics" to include K_soft as a derived quantity, alongside g_t, ℓ_max, Q_morph. Include Lemma 1.5 (Lipschitz via CSEH).

**Source:** `working/E/soft_K_definition.md`.

### 6.4 §12 Multi-formation re-narrative

**Proposed (E-S2 carry, not this session):** Rewrite §12 to use soft-K language: "K-field architecture" → "soft-K distribution"; "K formations" → "K_soft modes". Three Pillars (Nucleation, Metastability, Coarsening) preserved but re-anchored thermally.

### 6.5 §13 Theorem registry updates

**Proposed (per `integer_K_dependency_map.md` §7):**
- 5 Cat A theorems retired (Prop 1.2, Thm 3.1, T-Merge (a), Topological Lock, Coupling Bound).
- 1 Cat B retired (γ_eff = 0.89 — reinterpreted as Kramers prefactor, not standalone).
- 3 Cat C re-statement-pending (T-Persist-K-Sep/Weak/Unified).
- New Cat A claims (this session): K_soft Lipschitz, ℱ_{C+E} continuity / Lipschitz / coercivity / minimizer, Łojasiewicz on Σ_m^ε \ V.
- New sketched (Cat C-provisional): F1 / F2 commitments, F3 / F4 statements, Kramers metastability framework, Witten Laplacian framework.

### 6.6 §14 CN additions

**Proposed:** CN15-thermal, CN16-thermal, CN17-thermal (per §2.3 above).

### 6.7 Total scope of canonical changes

- New section: 1 (Group F-thermal).
- Modified sections: 4 (§5.5, §8.1, §12, §13).
- New CNs: 3.
- Retired theorems: 6 (5 Cat A + 1 Cat B).
- New theorems: ~12 (foundation Cat A from this session).

This is a **large canonical update**. Per CLAUDE.md and `working/reformulation_purpose.md` 17-session plan, this update spans Stages 1–6 (6 stages over 17 sessions). The present session contributes **Stage 1 first session** = ~5–10% of total update.

---

## §7. Partial Resolutions of Other Open Problems

### 7.1 P-2026-04-20-01 (T-Persist-K-Sep Category Inconsistency)

`canonical/canonical_sub.md` 2026-04-20 entry P-2026-04-20-01 noted: canonical §13 erratum moved T-Persist-K-Sep to Cat C; theorem_status.md still has it as Cat B.

**This session's input:** the soft-K reformulation **rewrites** T-Persist-K-Sep (per §1.4 above, sketched re-statement). Whether the rewritten statement is Cat B or Cat C in soft-K is a separate question (likely Cat C still — regime conditions WS, SR are non-removable structural hypotheses).

**Recommendation:** sync theorem_status.md to Cat C per canonical §13 erratum (P-2026-04-20-01 (i) recommendation). The soft-K rewrite preserves regime-conditional nature.

### 7.2 P-2026-04-20-02 (Cat C count header)

Same recommendation: header says "(5 theorems)" but section lists 6-7. Update to actual count post-merge.

---

## §8. New Open Questions Surfaced This Session

In addition to NQ-1 partial resolution and NQ-1-extended (§5):

### NQ-8 (new). Vineyard set V measure-theoretic handling

**Question:** Is the Gibbs measure ℙ_T absolutely continuous with respect to Lebesgue on Σ_m so that the codim-1 vineyard set V is null for thermal analysis?

**Why it matters:** F3 Langevin trajectories pass through V; Gibbs probability of being on V is the question of whether V is null. Expected answer yes (continuous ℱ + bounded ⇒ Gibbs equivalent to Lebesgue on compact Σ_m), but formal verification needed.

**Carry:** C-S2.

### NQ-9 (new). Sharper Lipschitz constant L_K via graph spectral structure

**Question:** Cor 2.2 in G1 gives `L_K ≤ 2 L_φ · n`, likely loose by factor related to λ_2(G) or isoperimetric constant of the graph.

**Why it matters:** Tighter `L_K` bound translates directly to tighter Lipschitz of ℱ_{C+E}, hence sharper stability / convergence rates for Langevin and gradient flow. Improves quantitative predictions.

**Carry:** C-S2 / E-S2.

### NQ-10 (new). First-principles determination of γ_K (λ_K = γ_K T scaling)

**Question:** What is the natural numerical value of γ_K? Recommended `γ_K ∈ [0.01, 1]` (G3 §4.3) is heuristic; can it be derived from RG analysis (pre_brainstorm H-B16) or from a dimensional argument on (S, K_soft) information measures?

**Why it matters:** γ_K is the first new free parameter introduced by C+E framework (beyond T). P-E's "25+ parameters" concern grows; γ_K should be derived if possible.

**Carry:** CE-S2 / Stage 3 (Definition & Derivation).

### NQ-11 (new). Variational saddle existence between K_soft basins

**Question:** Mountain Pass on connected Σ_m gives existence of saddle between K_soft ≈ 1 and K_soft ≈ 2 critical points. What is the saddle's K_soft value? Is it a single saddle or a connected manifold of saddles? Energy ℱ at saddle?

**Why it matters:** Saddle ℱ value enters Kramers ΔF directly. Without specifying saddle, Kramers prefactor (G5 §3.2) is incomplete.

**Carry:** C-S2.

### NQ-12 (new). Discrete-graph Witten Laplacian rigorous formulation

**Question:** Witten Laplacian (G6 §3) is classically smooth-manifold construction. SCC's Σ_m has discrete underlying graph + continuous u-values. Two routes: (i) treat Σ_m as smooth manifold, apply Witten directly; (ii) Forman-style discrete (G6 §5) — combinatorial alternative. Which route is canonical?

**Why it matters:** MO-1 dissolution (G6) leans on Witten Laplacian as central spectral tool. Discrete-graph treatment is needed for full applicability to SCC.

**Carry:** post-Stage-1.

### NQ-13 (new). Disconnected graph regime for M-1

Per §4.5 of `02_development.md`: M-1 reframing (isoperimetric feature) is implicitly **connected-graph**. On disconnected graphs, K_soft > 1 is global minimum (one mode per component) — no isoperimetric-monotonicity-toward-K=1.

**Question:** What is the soft-K theory on disconnected graphs? Is there a unified treatment that handles both connected (single-mode preferred) and disconnected (multi-mode preferred) without case-splitting?

**Carry:** E-S3 / canonical scope clarification.

---

## §9. canonical_sub.md 2026-04-21 Entry Draft

The following is the proposed entry to append to `canonical/canonical_sub.md`. Format follows the file's §"사용 규칙" (Append at top, 5 type labels: Added, Modified, Retired, Clarified, Pending).

---

```markdown
## 2026-04-21

**Session type:** Stage 1 (Definition Foundation) — C+E common first session.
**Origin:** `logs/daily/2026-04-21/` (plan.md + pre_brainstorm.md + 01_exploration.md + 02_development.md + 03_integration_and_new_open.md + 99_summary.md) + `working/E/soft_K_definition.md` + `working/C/F_group_axioms.md` + `working/CE/free_energy_wellposed.md` + `working/E/M1_dissolution.md` + `working/E/MO1_dissolution.md` + `working/E/F1_dissolution.md`.
**Canonical-relevant 산출물:** Added 3 (K_soft def, F1-F2 axioms, ℱ_{C+E} cross-object), Clarified 1 (F-1/M-1/MO-1 dissolution mappings — language), Pending 7+ (Group F-thermal section, §12 rewrite, theorem retirements, F3-F4 statements, new CNs, NQ-8/9/10/11/12/13).

---

### Added

#### A-2026-04-21-01. K_soft Soft-K Definition

**출처:** `working/E/soft_K_definition.md`.

**정의:** For `u ∈ Σ_m`, with monotone Lipschitz `φ : [0,∞) → [0,∞)`, `φ(0)=0`:

`K_soft(u) = Σ_{i ∈ B_+(u)} φ(ℓ_i(u))`, B_+(u) = positive-length bars of H₀ persistence diagram of superlevel filtration. Default `φ(ℓ) = ℓ/(1+ℓ)`.

**Well-defined:** Cat A. K_soft ∈ C^0(Σ_m) globally Lipschitz with `L_K ≤ 2 L_φ n` (G1 §2 + 02_development.md §4.1 strengthened).

**Canonical merge target:** §5.5 (Transition Diagnostics). NQ-1 partial resolution (i committed; (ii)(iii)(iv) parked).

#### A-2026-04-21-02. F-group axioms F1, F2

**출처:** `working/C/F_group_axioms.md`.

**F1 (Thermal State):** Gibbs measure ℙ_T ∝ exp(-ℱ/T) on Σ_m for T > 0. Z(T) finite (Cat A, Prop F1.1).

**F2 (Bernoulli Entropy):** S(u) = -Σ[u log u + (1-u)log(1-u)]. Continuous, bounded, strictly concave on (0,1)^n; Lipschitz on [ε, 1-ε]^n (Cat A, Prop F2.1).

**Canonical merge target:** §6 new "Group F-thermal" section.

#### A-2026-04-21-03. ℱ_{C+E} Cross-Object Well-Definedness

**출처:** `working/CE/free_energy_wellposed.md`.

**정의:** ℱ_{C+E}[u; T, λ_K] = ℰ[u] - T·S(u) + λ_K·K_soft(u).

**Well-defined:** Cat A. Continuous on Σ_m (Lemma 1.7); Lipschitz on Σ_m^ε (Lemma 1.8); bounded below ≥ -T n log 2 (Prop 3.1); minimizer exists (Thm 3.3, Weierstrass); real-analytic on Σ_m^ε \ V (Lemma 2.1); Łojasiewicz applies on Σ_m^ε \ V (Cor 2.2).

**λ_K scaling commitment:** λ_K = γ_K · T with γ_K ∈ [0.01, 1] (heuristic; NQ-10).

**Canonical merge target:** §8.1 new sub-section "Free Energy in C+E Framework".

---

### Clarified

#### C-2026-04-21-01. F-1 / M-1 / MO-1 Dissolution Mappings

**출처:** `working/E/F1_dissolution.md`, `working/E/M1_dissolution.md`, `working/E/MO1_dissolution.md`.

**F-1:** vacuity claim dissolved at architectural level (soft-K removes external m_j); thermal occupation provides quantitative replacement. **Status: partially dissolved (E-side Cat A; C-side sketched).**

**M-1:** reframed as feature (isoperimetric Cat A T-Merge (b) preserved); Kramers metastability provides finite-T framework for K>1 coexistence. **Status: reframed (Cat A reused; Kramers sketched).**

**MO-1:** Σ²_M corner removed (architectural); smooth Morse on Σ_m^ε \ V applies; Witten Laplacian provides spectral alternative. **Status: partially dissolved (E-side Cat A; C-side statement only — discrete-graph treatment carry).**

**Variation:** none of the 3 silently resolved; explicit residuals in each working file.

---

### Pending

#### P-2026-04-21-01. Canonical §6 Group F-thermal addition

awaiting weekly merge user decision. Naming conflict with CN4 ("Group F" = crisp recovery): proposed disambiguation rename.

#### P-2026-04-21-02. Canonical §13 retirements

5 Cat A retirements (Prop 1.2, Thm 3.1, T-Merge (a), Topological Lock, Coupling Bound) + 1 Cat B (γ_eff = 0.89). Per `working/integer_K_dependency_map.md` §2.

#### P-2026-04-21-03. Canonical §13 Cat C re-statements

T-Persist-K-Sep/Weak/Unified (3 Cat C) — soft-K language re-write. E-S2 carry.

#### P-2026-04-21-04. F3 Langevin well-posedness

`working/C/F_group_axioms.md` §3 — statement only. Full proof via Da Prato–Zabczyk + Lions–Sznitman + V handling. C-S2 carry.

#### P-2026-04-21-05. F4 T → 0 recovery proofs

`working/C/F_group_axioms.md` §4 — statement only. Case-by-case verification of canonical Cat A theorems' T → 0 survival. C-S3 carry.

#### P-2026-04-21-06. Witten Laplacian discrete-graph treatment

`working/E/MO1_dissolution.md` §3 — statement only. Discrete-graph formulation + V mollification. Post-Stage-1 carry.

#### P-2026-04-21-07. New CNs proposed

CN15-thermal (ℱ_{C+E} variational), CN16-thermal (Kramers/Witten substantiation of CN6/8/14), CN17-thermal (soft-K canonical generalization of integer K). User decision for canonical §14 addition.

---

### Added — Pending OP 승급 (NQ-8 through NQ-13)

#### NQ-8. Vineyard set V measure-theoretic handling

**Q:** Is Gibbs ℙ_T absolutely continuous w.r.t. Lebesgue on Σ_m so V is null?
**Carry:** C-S2.

#### NQ-9. Sharper L_K Lipschitz constant via graph spectrum

**Q:** Refine Cor 2.2's `L_K ≤ 2 L_φ n` using λ_2(G) or isoperimetric constant.
**Carry:** C-S2 / E-S2.

#### NQ-10. First-principles γ_K determination

**Q:** Derive γ_K ∈ [0.01, 1] from RG analysis or dimensional argument.
**Carry:** CE-S2 / Stage 3.

#### NQ-11. Variational saddle existence between K_soft basins

**Q:** Mountain Pass on Σ_m gives existence; what is saddle's K_soft value, ℱ value, structure?
**Carry:** C-S2.

#### NQ-12. Discrete-graph Witten Laplacian formulation

**Q:** Two routes: smooth-Σ_m + Witten direct vs Forman discrete. Canonical choice?
**Carry:** post-Stage-1.

#### NQ-13. Disconnected-graph regime for M-1

**Q:** M-1 reframing (single-mode preferred) is connected-graph; how to unify with disconnected graph multi-mode preference?
**Carry:** E-S3 / canonical scope clarification.

---

### 본 entry 의 canonical 변경 규모 (주간 merge 예상)

주간 merge 시 `canonical.md` 실제 수정 (현재 누적):

- 2026-04-20 entry 이월: §13 inline annotation 10줄 (Q1), Cat C count header 1줄 (Q3), theorem_status.md sync 1줄 (Q2).
- 2026-04-21 entry 신규 (대규모):
  - §6 신설 "Group F-thermal" — 약 80줄 (F1-F4).
  - §8.1 신설 sub-section "Free Energy in C+E Framework" — 약 30줄.
  - §5.5 확장 (K_soft 추가) — 약 15줄.
  - §13 retirements — 6 정리 retire, 새 Cat A 12개 added.
  - §14 새 CN 3개 (CN15-CN17 thermal).
  - 총 ~250줄 추가, ~30줄 retire/modify.

총 변경 ~280줄 (이전 누적 ~12줄에 비해 매우 큰 변경). 새 정리/공리/CN 다수.

**주간 merge 에서 user 가 결정할 추가 사항:**
- Q5. Group F-thermal 명칭 vs CN4 "Group F" 충돌 해결 (rename 어느 쪽?).
- Q6. F3 / F4 statement-only 가 canonical 에 들어갈 자격이 있는가? 아니면 working 단계로 유지?
- Q7. NQ-8 ~ NQ-13 중 OP-xxxx 승급 후보 (권고: 모두 Stage 1 완료까지 대기).
- Q8. 6 retirement 시점 (이번 주 vs Stage 6 통합 merge).
- Q9. CN15-17 thermal 추가 시점 (이번 주 commit vs Stage 2 audit 후).
```

---

## §10. Prompt Improvement Notes (per Final §14 of session prompt)

The session prompt is a reusable template for daily research sessions. Following items observed during this session that may warrant updating:

1. **§4 (다중 접근 ≥3) 의 운영 정의:** "수학적으로 독립" 의 자기 점검 매트릭스 (§2.6 of 01_exploration.md) 는 본 세션에서 5 후보의 독립성을 명시하는 데 도움이 되었음. 향후 세션 prompt 의 §5 ("다중 접근의 품질 기준") 에 "독립성 매트릭스 작성 권장" 추가 가능.

2. **§6 (출력 규약) 의 working file 와 logs/daily 분리:** 본 세션은 6 개 working file (G1-G6) 과 4 개 daily core file (01-03 + 99) 을 동시 생산. 의존 관계 (working file 가 logs/daily 의 02_development.md 에 통합되는 흐름) 가 명시되지 않아 작업 순서 결정시 모호함이 있었음. **개선 제안:** §6 에 "working file 과 logs/daily core file 의 의존 관계 / 작성 순서" 를 명시.

3. **§8 (절대 금기) item 9 (zero-T metastability flag):** 본 세션이 정확히 zero-T → finite-T 전환을 다룸. "metastable" 단어 사용시 P-F flag 의무 — 대신 본 세션은 "P-F dissolution in progress" 라는 메타 표기로 처리. 향후 세션이 thermal framework 가 정착된 이후에는 이 flag 를 "P-F resolved (post-2026-04-21 sessions)" 로 자동 완화 가능.

4. **§11 (언어 / 스타일):** 본 세션의 working file 길이 (각 4-7 페이지) 가 plan §G4-G6 의 "1-2 페이지 상한" 을 다소 초과. plan 의 페이지 상한은 _substantive content_ 기준이며 status table / status summary / carry-forward 메타 섹션은 별도라는 운영 합의 필요. **개선 제안:** plan template 에 "페이지 상한 기준: substantive sections only" 명시.

5. **§13 (세션 종료 지점) 의 stop condition:** 본 세션은 §13 의 두 번째 조건 ("Primary 접근이 명시적 실패 조건에 도달") 에 일부 해당하는 항목 (vineyard 처리, 프리팩터 정확 derivation, 등) 이 있으나, 모두 carry 로 처리하여 substantive 산출물을 생산. **개선 제안:** "carry-OK 한 미해결 항목" 의 비율 기준 추가 (예: 총 산출물 중 carry 가 50% 이하 권장).

이 개선 제안은 plan 의 v2 분기 결정에 사용자 참고용. 본 prompt 자체 수정은 별도 결정.

---

## §11. Status Summary

**Session 산출:** 6 working files (G1-G6) + 4 logs/daily core files (01, 02, 03, 99) + canonical_sub.md 2026-04-21 entry draft (above). 3 working sub-directories (E/, C/, CE/) created.

**Canonical 직접 수정:** 0 (per Non-goal). All proposed changes via canonical_sub.md weekly merge process.

**Cat A 추가 (sketched-rigorous):** 12 (foundation chain).

**Sketched (Cat C-provisional):** 7.

**Statement-only (carry):** 3.

**Existing OPs:** F-1, M-1, MO-1, OP-0005 partially dissolved. P-A, P-F partially dissolved. Others unchanged.

**New NQs:** NQ-8 through NQ-13 (6 new), NQ-1-extended (1).

**CN affected:** CN4 (rename proposed), CN5/6/7/8/12/14 (substantiated, no retraction).

Next file: `99_summary.md`.
