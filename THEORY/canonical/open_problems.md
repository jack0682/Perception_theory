---
id: ROADMAP-0003
type: roadmap/open_problems
status: accepted
last_updated: 2026-04-30
---

<!-- Update history:
  2026-04-25: W4 weekly close (F-1/M-1/MO-1 resolved/clarified/sidestepped, 3 Critical → 0). [last body edit through this date]
  2026-04-30 (W5 Day 4 / CV-1.5.1): OP-0008 σ^A K-jump non-determinism + OP-0009 Multi-Formation Ontological Foundations (7 sub-items) registered HIGH; OP-0003 MO-1 re-activation rider added; OP-0009-K RESOLVED via Commitment 16. [last body edit]
  2026-05-02 (W5 Day 6 / CV-1.5.2): T-L1-F canonical promotion. open_problems.md body NOT modified (T-L1-F is a bridge, not a K-selection mechanism — explicitly does NOT solve OP-0005 or OP-0008). Note (2026-05-04 audit fix): the previous bump of `last_updated` to 2026-05-02 was misleading because no body change accompanied it; reverted to 2026-04-30 (the true date of the last substantive edit) per audit-trail honesty principle.
-->


# Open Problems Registry (OP-xxxx)

**Purpose:** Catalog all unresolved research questions with severity ratings, status, and impact analysis.

**Format:** Organized by severity (critical → high → medium → low) and category.

---

## CRITICAL PROBLEMS 🔴 (Foundational)

### **OP-0001: F-1 — K=2 Vacuity**

**Statement:**  
K=2 global stability is "vacuous" without external per-formation mass constraint. If masses m_j are allowed to vary, energy minimization always selects K=1 (energetically ~50% cheaper).

**Evidence:**
- exp62, exp63: K=2 energy E ≈ 4.66; K=1 energy E ≈ 2.25
- M-1 analysis: M₂ landscape monotonically decreasing toward K=1
- All K-field theorems assume "m_j fixed externally" (axiom A-0013)

**Impact:**
- All K-field theorems (T-Persist-K-Sep, T-Persist-K-Unified, etc.) depend on this external assumption
- K-field theory is not self-contained
- No mechanism yet explaining why K would be fixed in biological/cognitive systems
- Blocks publication as self-contained theory

**Related problems:** M-1 (root cause), MO-1 (Morse variant)

**Proposed resolutions:**
- **Option A:** Accept "fixed K is external constraint" (current v1.2 approach)
- **Option B:** Develop K-selection mechanism (BIC, free energy, birth-death dynamics)
- **Option C:** Reformulate as kinetic/metastability theory (K>1 as local minima)
- **Option D (taken in W4, 2026-04-24):** Premise dissolution via SCC-intrinsic re-framing — neither A/B/C, but a fourth path where the dichotomy "K=1 cheaper vs observed K>1" itself ceases to be framed.

**Status:** ✅ **SPLIT-RESOLVED (2026-04-24)** — both portions Cat A.

**Resolution (2026-04-24, W4 session):**

F-1 decomposes into two layers, each Cat A resolved:

- **Pure $\mathcal{E}_{\mathrm{bd}}$ portion**: Resolved by T-Merge (b) canonical theorem (already proved, isoperimetric ordering on connected graphs). The "K=1 cheaper" statement in pure $\mathcal{E}_{\mathrm{bd}}$ is a *correct theorem*, not an open problem. Original framing as "open problem" was a misclassification — see also OP-0002 M-1 below.

- **Full SCC portion**: Resolved by **Theorem 2 (i)** (Pre-Objective Mechanism, Cat A graph-class independent via Theorem 2-G). Under full SCC parameters, the F=1 single-disk minimizer of pure $\mathcal{E}_{\mathrm{bd}}$ is **not a critical point** of full $\mathcal{E}$. Therefore, the dichotomy "K=1 cheaper vs observed K>1" does not arise — F=1 is non-critical, F ≥ 2 is the default ground state under full SCC. The premise of F-1 collapses.

**Net effect**: The originally-paradoxical comparison ("global static minimum K=1 vs empirical K>1") is dissolved. Pure $\mathcal{E}_{\mathrm{bd}}$ statement is a proved theorem (T-Merge (b)); full SCC statement is reversed (F ≥ 2 default).

**Severity:** 🔴 ~~CRITICAL~~ → ✅ RESOLVED (no longer blocking)
**Last reviewed:** 2026-04-25 (W4 weekly close)
**References:**
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §F-1 resolution
- `THEORY/logs/daily/2026-04-24/11a_C2_generalization.md` (Theorem 2-G)
- `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` (Theorem 2 (i) proof)
- `THEORY/canonical/canonical.md` §13 T-Merge (b) (pure portion) — pre-existing Cat A
- `THEORY/canonical/canonical.md` §13 T-PreObj-1 (full SCC portion) — to be added in W4 merge

---

### **OP-0002: M-1 — K=1 Energetic Preference**

**Statement:**  
The K=2 energy landscape E(m₁, m₂) where m₁ + m₂ = M is monotonically decreasing as one formation size decreases (m₂ → 0). Therefore, K=1 with total mass M is always energetically cheaper than any K=2 split.

**Evidence:**
- Direct calculation: E_K1(M) < E_K2(M/2, M/2) always
- Empirical confirmation: exp62, exp63, exp71–exp73
- Consequence of energy functional form (no K>1 preference mechanism)

**Impact:**
- This is the **root cause of F-1**
- Shows K>1 can never emerge from energy optimization alone
- Requires model selection mechanism (BIC, free energy, etc.) to explain K>1 emergence
- Fundamental limitation of current energy-based framework

**Related problems:** F-1 (consequence), OP-0005 (K selection)

**Status:** ✅ **LAYER-CLARIFIED (2026-04-24)** — proved theorem misframed.

**Clarification (2026-04-24, W4 session):**

M-1 is **not an open problem**; it is the *correct mathematical statement* (T-Merge (b), canonical §13 Cat A) about isoperimetric ordering on the constraint manifold $\Sigma_m$. The original framing as "problem" arose from conflating two distinct quantities:

- **Pure $\mathcal{E}_{\mathrm{bd}}$ layer**: M-1 statement holds — K=1 has lower energy than K=2 by the perimeter minimization (Γ-convergence). This is T-Merge (b), already canonical.

- **Full SCC layer**: The comparison "K=1 cheaper vs K=2" is not even framed, because under full SCC parameters, the F=1 single-disk minimizer is **not a critical point** (Theorem 2 (i)). The "K=1 ground state" of pure $\mathcal{E}_{\mathrm{bd}}$ does not survive into the full SCC landscape.

**Net effect**: M-1 is *proved* (T-Merge (b)); the misframe was treating it as a *problem*. The actual problem (in original framing) was the apparent conflict between this proved theorem and empirically observed K>1 — that conflict is resolved by Static/Dynamic Separation (CN15 candidate, W4 04-23) and Theorem 2 (W4 04-24): static global minimum is K=1 only on pure $\mathcal{E}_{\mathrm{bd}}$, but dynamic protocol-endpoint observables ($\widehat{K}$, $\mathcal{F}$) need not equal it.

**Severity:** 🔴 ~~CRITICAL~~ → ✅ CLARIFIED (proved theorem, not a problem)
**Last reviewed:** 2026-04-25 (W4 weekly close)
**References:**
- `THEORY/canonical/canonical.md` §13 T-Merge (b) (the actual theorem)
- `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` §M-1 layer analysis
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §4
- `THEORY/logs/daily/2026-04-23/MF_multi_quantization.md` §7 (Landau monotone) — the same statement under FQ framework

---

### **OP-0003: MO-1 — Morse Theory Inapplicability**

**Statement:**  
The K=2 constrained manifold Σ²_M = {(u¹, u²) : m_1 = m_2 = M/2} is not a smooth manifold; it has corners (at boundary where one formation's mass → 0). Smooth Morse theory requires manifolds without boundary and thus is inapplicable.

**Evidence:**
- Manifold geometry: Σ²_M is the product Σ_m × Σ_m restricted to constraint surface; this is a manifold **with corners**
- Standard Morse theory: Only works on smooth manifolds without boundary
- Implication: Theorems T-8-Core, T-14, etc. may need re-proof using stratified framework

**Impact (original framing):**
- Full global analysis of K=2 energy landscape incomplete
- Smooth bifurcation theory not applicable to M₂
- Workaround: Use existing stable results (don't claim global optimality without proof)
- Alternative: Develop stratified Morse theory analysis (significant effort)

**Related problems:** F-1, M-1 (both related to M₂ properties)

**Status:** ⚪ **SIDESTEPPED (2026-04-24)** — single-formation σ-framework operates on $\Sigma_m$ (no corners). Multi-formation extension to $\Sigma^K_M$ remains open.

**Sidestep mechanism (2026-04-24, W4 session):**

MO-1 was a blocker for global landscape analysis on the multi-formation manifold $\Sigma^K_M$ (corners). The W4 work introduced:

- **σ-framework** (canonical-ready, Cat A definitional): operates on **single-formation** $\Sigma_m$ (smooth simplex, no corners). Hessian eigenvalue/irrep/nodal-count signature $\sigma(u^*) = (\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\})$ is well-posed.
- **Theorem 2 family** (Cat A graph-class independent): operates on **single-formation** $\Sigma_m$. Pre-objective formation mechanism (F ≥ 2 default under full SCC) does not require multi-formation Morse analysis.

Therefore, the principal results of W4 (Theorem 2 family + σ-framework + F-1 split-resolution) **do not require Morse theory on $\Sigma^K_M$**. MO-1 is not a blocker for current scope.

**Multi-formation extension still open**: Stratified Morse on $\Sigma^K_M$ (multi-formation σ, Phase 5) remains genuine open work. MO-1 returns as an active blocker if/when the theory extends to multi-formation σ.

**Severity:** 🟠 HIGH (within multi-formation scope) → ⚪ NOT BLOCKING (within single-formation scope)

**Re-activation trigger (W5 added 2026-04-29 CV-1.5.1):** D-6b dynamic σ_multi^A(t) approval at CV-1.6 OR NQ-248 multi-formation stratified Morse work begins → 🟠 HIGH automatic re-activation. Single-formation σ-framework (CV-1.5+) operates on $\Sigma_m$ corner-free; multi-formation σ Phase 5 (D-6a CV-1.5.1, D-6b CV-1.6+) operates on $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M$ corner-saturated regime — MO-1 stratified Morse on $\widetilde{\Sigma}^K_M$ becomes relevant. Current Day 3 EOD CV-1.5.1 D-6a uses Option A pragmatic (interior only, corners excluded) which preserves SIDESTEPPED status. Critical-blocker count "0" at CV-1.5.1 is **temporally conditional** on architecture choice (per Commitment 16 K-status + OAT-4 Shared-pool architecture decision pending CV-1.6).

**Last reviewed:** 2026-04-29 (W5 Day 3 EOD CV-1.5.1; rider added per 4-agent ontological depth analyst recommendation)
**References:**
- `THEORY/logs/daily/2026-04-24/02_development.md` §2, §5 (σ on Σ_m, single-formation)
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §7 (MO-1 sidestep note)
- `THEORY/logs/daily/2026-04-24/99_summary.md` §8 (sidestep vs resolution distinction)
- `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` §5.4 (explicit re-engagement of MO-1 at multi-formation level)
- Multi-formation σ Phase 5: D-6a static merged at CV-1.5.1; D-6b dynamic deferred to W6+ via NQ-242

---

### **OP-0008: σ^A K-jump Inheritance Non-Determinism**

**Statement:**
Under K-field gradient flow on shared-pool $\widetilde{\Sigma}^K_M$ (Phase 7 R1.3 architecture), at K-jump times $t^*$ (where $K_{\mathrm{act}}(t^{*-}) > K_{\mathrm{act}}(t^{*+})$, formation merger event), the post-merger σ^A($t^{*+}$) is **NOT deterministic** in pre-merger σ^A($t^{*-}$) alone. Inheritance map $\Phi : \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ requires merger-geometry data $\mathcal{M}$ = (which two formation indices $j, k$ merge; cluster centroids; post-merger relaxation trajectory; orientation alignment).

**Evidence:**
- Day 3 deepening pass `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c): formal non-determinism claim, Cat C asserted.
- Self-critique `THEORY/logs/daily/2026-04-29/09_session_self_critique.md` §2.3: Lemma 4.4.1(c) downgraded "Cat B sketch" → "Cat C (conjectured)".
- Phase 8 T4 SCC↔CH correspondence (`2026-04-28/32_U5_SCC_CH_theorem.md` Cat B target): implicit assumption of deterministic σ-trajectory under CH-correspondence flow — violated by Lemma 4.4.1(c).
- Working file `THEORY/working/MF/sigma_multi_trajectory.md` §4.2 Lemma 4.2(c) Cat status: conjectured (Cat C).

**Impact:**
- D-6b Commitment 14-Multi DYNAMIC Cat A path (CV-1.6+) requires **rich-σ augmentation**: σ-tuple expanded to include cluster centroid, orientation, and Wigner-von Neumann data beyond eigenvalue tuple.
- **Bifurcates CV-1.6 release path**:
  - Path A: accept non-determinism, register Cat B target with explicit non-deterministic K-jump map.
  - Path B (Cat A target): rich-σ augmentation (NQ-242c explicit construction + NQ-242d σ^D symmetry-emergence).
- Phase 8 T4 caveat needed in Paper §4.5.7 SCC↔CH correspondence section: "static correspondence intact; dynamic σ_multi^A(t) ↔ CH flow correspondence requires σ_rich".

**Status:** ⚠️ **TENTATIVE** (Cat C asserted; explicit construction NQ-242c open).

**Severity:** 🟠 **HIGH** — affects D-6b canonical path; CV-1.6 release-blocking for Cat A target if Path B chosen.

**Last reviewed:** 2026-04-29 (W5 Day 3 EOD, registered at CV-1.5.1).

**Direct-attack NQs:**
- **NQ-242c**: explicit construction of two trajectories with same σ^A($t^{*-}$) but distinct σ^A($t^{*+}$). Cat A target. ~2-3 weeks. W6+ priority.
- **NQ-242d**: σ^D symmetry-emergence characterization (post-merger stabilizer $\supseteq$ pull-back image). Cat A target. ~2-3 weeks. W6+.
- **NQ-242**: full Hessian σ-tuple time-series with rigorous K-jump theory. Cat A or B target. 4-6 weeks. W6 Day 1-7 priority.

**Related problems:** OP-0003 MO-1 (re-activation at multi-formation level via D-6b path), OP-0005 K-Selection (K-jump-event path-dependence implication), OP-0009 Multi-Formation Ontological Foundations (OP-0008 ⊂ OP-0009).

**References:**
- Day 3 deepening: `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` §4.4.1(c)
- Self-critique: `THEORY/logs/daily/2026-04-29/09_session_self_critique.md` §2.3
- Working file: `THEORY/working/MF/sigma_multi_trajectory.md` §4.2
- Phase 8 T4 implicit assumption: `THEORY/logs/daily/2026-04-28/32_U5_SCC_CH_theorem.md`

---

### **OP-0009: Multi-Formation Ontological Foundations**

**Statement:**
Multi-formation σ-framework (D-6a static at CV-1.5.1 + D-6b dynamic at CV-1.6+) implicitly relies on 7 ontological commitments that are NOT all canonically registered as of CV-1.5.1. The implicit foundation is:

1. **OP-0009-K (K-status)**: K (formation count) ontological position. **PARTIALLY RESOLVED** by Commitment 16 (CV-1.5.1) — K_field/K_act two-tier decomposition. *(OAT-1 done; working file `working/MF/K_status_commitment.md`.)*
2. **OP-0009-F (F as derived diagnostic)**: F (peak count, threshold-free upper semi-continuous) canonical registration. Currently inline in T-PreObj-1 + CN17 only; not in §5 derived diagnostics. **OPEN** (OAT-2 W6 Day 1).
3. **OP-0009-λ (λ_rep ontology)**: λ_rep $\langle u^j, u^k \rangle$ as 5th energy term vs 4-term coupling realization vs simplex-enforcement Lagrange. CN5 (4-term independence) is single-formation 약속 — multi-formation extension status undecided. **OPEN** (OAT-3 W6 Day 2).
4. **OP-0009-A (Architecture choice)**: K-field architecture I9 ($\Sigma^K_M$, fixed K) vs Shared-pool architecture I9' ($\widetilde{\Sigma}^K_M$, K_act variable). Currently I9 canonical, I9' working only. **OPEN** (OAT-4 W6 Day 2).
5. **OP-0009-C (C_t multi-formation)**: Co-belonging C_t demoted single-formation; multi-formation status (subsumed by σ_multi^D vs revived primitive). **OPEN** (OAT-5 W6 Day 3).
6. **OP-0009-Pre (Pre-objective + K-field)**: K-field architecture imports object-like K parameter; potential CN10 violation. Resolution path via "modeling-layer commitment" framing. **OPEN** (OAT-6 W6 Day 4).
7. **OP-0009-Emp (R23 F=9 σ verification)**: σ-framework Cat A claims (CV-1.5) anchored at F=1 uniform / F=2 first-pitchfork; F=9 default ground state σ behavior empirical only (NQ-141). **OPEN** (OAT-7 W6 Day 5+6).

**Evidence:**
- 4-agent ontological depth analysis 2026-04-29 EOD (architect / critic / analyst / planner): convergent identification of 5 implicit commitments + 2 supplementary as multi-formation initiation foundations.
- Critic 7-agent verdict 2026-04-29: REVISE — D-6a should not merge without ontological audit; 5 CRITICAL findings.
- W4-W5 working trajectory: 5 conflicting K-status uses (External I9 / Kinetic CN6 / Derivative R22 / K_soft / Integer per N-1) coexisted in canonical/working without explicit reconciliation.

**Impact:**
- CV-1.5.1 D-6a merge proceeded with **partial ontological foundation** (Commitment 16 K-status added; other 6 sub-items deferred to OAT-2..7 W6 working files).
- CV-1.6 (W6 close) target: 4 ontological D-items (D-CV1.6-O1 K-status if not already in CV-1.5.1 + O2 Shared-pool I9' + O3 F bridge + O4 λ_rep) + 7 process D-items.
- v2.0 (W11-W12) target: full OP-0009 resolution + Paper 4 NEW (Pre-Objective Multi-Architecture, planner權告).
- Paper 1 §6 multi-formation forward-reference depends on OP-0009 sub-items partially resolved before W9 submit.

**Status:** ⚠️ **PARTIALLY ADDRESSED** at CV-1.5.1 + Day 4 morning OAT batch session (2026-04-30). 1 of 7 sub-items RESOLVED (OP-0009-K via Commitment 16 CV-1.5.1); 6 of 7 PARTIALLY RESOLVED at CV-1.6 candidate level via OAT-2..7 working files (W5 Day 4 advance from W6).

**Sub-item Status Table (W5 Day 4 EOD post-Critic verdict propagation):**

| Sub-item | Pre-Day 4 | Post-Day 4 OAT batch | Resolution mechanism | Working file | Promotion target |
|---|---|---|---|---|---|
| **OP-0009-K** (K-status) | OPEN | ✅ **RESOLVED** | Commitment 16 K_field/K_act two-tier decomposition | `K_status_commitment.md` (480 lines) | CV-1.5.1 (DONE) |
| **OP-0009-F** (F derived diagnostic) | OPEN | ⚪ **PARTIALLY RESOLVED** | F as derived diagnostic register §5.5 + CN17+ amendment + 4-quantity bridge | `F_Kstep_K_triple.md` (359 lines) | CV-1.6 D-CV1.6-O3 |
| **OP-0009-λ** (λ_rep ontology) | OPEN | ⚪ **PARTIALLY RESOLVED** | Argument B (architectural-layer coupling) + Option 3 (CN10 contrastive); strict KKT identification verification fail | `lambda_rep_ontology.md` (242 lines) | CV-1.6 D-CV1.6-O3 |
| **OP-0009-A** (Architecture: K-field vs Shared-pool) | OPEN | ⚪ **PARTIALLY RESOLVED** | I9 + I9' complementary modeling-layer commitments via Tool A1 stratified space | `shared_pool_canonical_proposal.md` (335 lines) | CV-1.6 D-CV1.6-O2 |
| **OP-0009-C** (C_t multi-formation) | OPEN | ⚪ **PARTIALLY RESOLVED** | Option C-3 variant: $C_t$ demoted maintained + σ_multi^D orthogonal (not subsumes); architecture-conditional (K-field 4a primary) | `cobelonging_vs_sigmaD.md` (392 lines) | CV-1.6 D-CV1.6-O4 |
| **OP-0009-Pre** (Pre-objective + K-field tension) | OPEN | ⚪ **PARTIALLY RESOLVED** | Path A+C+Tool A2 quotient hybrid; unordered configuration ontologically primary | `pre_objective_K_field_tension.md` (534 lines) | v2.0 §1 amendment |
| **OP-0009-Emp** (R23 empirical verification) | OPEN | ⚪ **PARTIALLY RESOLVED** | R23 fullscale dataset numerical analysis: F=63 max, all 56 minimizers F > K_step, σ-irrep CONFIRMED 0 exceptions; **BC-1 fails generic** (R23 generic = overlapping regime) | `single_high_F_equivalence.md` (511 lines) | CV-1.6 partial; full v2.0 |

**Net OP-0009 status post-Day 4 OAT batch**: **PARTIALLY ADDRESSED** (1 RESOLVED + 6 PARTIALLY RESOLVED). Full RESOLVED status not achieved at CV-1.6; v2.0 (W11-W12) deferred for Pre-objective + K-field tension full canonical §1 amendment.

**Important caveat (W5 Day 4 EOD post-Critic, 2026-04-30):** Per Critic 7-agent verdict (`daily/2026-04-30/05_critic_final_review.md`) MAJOR-3 finding, OP-0009 should be framed as "framework + 1/7 sub-items closed (K via Commitment 16) + 6/7 sub-items partially addressed", **not** as "OP-0009 framework-level resolved" or "Theory Deepening Stretch 100%". Future canonical/CHANGELOG/paper claims should reflect this calibrated status to avoid inflated-resolution mis-citations.

**Severity:** 🟠 **HIGH** — release-blocking for Cat A multi-formation σ-framework completeness; not blocking for CV-1.5.1 D-6a static (Cat A definitional only).

**Last reviewed:** 2026-04-29 (W5 Day 3 EOD, registered at CV-1.5.1).

**Direct-attack NQs and OAT working files**:
- OAT-1 (DONE): `working/MF/K_status_commitment.md` — Commitment 16 K-status proposal.
- OAT-2 (W6 Day 1 evening): F/K_step/K_act/K_field bridge — `working/MF/F_Kstep_K_triple.md` planned.
- OAT-3 (W6 Day 2 evening): λ_rep ontological status — `working/MF/lambda_rep_ontology.md` planned.
- OAT-4 (W6 Day 2 evening): Shared-pool architecture I9' — `working/MF/shared_pool_canonical_proposal.md` planned.
- OAT-5 (W6 Day 3 PM): C_t vs σ_multi^D coexistence — `working/MF/cobelonging_vs_sigmaD.md` planned.
- OAT-6 (W6 Day 4 PM): Pre-objective + K-field tension — `working/MF/pre_objective_K_field_tension.md` planned.
- OAT-7 (W6 Day 5+6): R23 F=9 ↔ K=9 K-field empirical equivalence — `working/MF/single_high_F_equivalence.md` planned.

Total OAT effort: ~8 hours theory work spread W6 Day 1-7, parallel to NQ-242 numerical lane.

**Related problems:** OP-0003 MO-1 (sub-item OP-0009-A architecture decision triggers MO-1 re-activation); OP-0005 K-Selection (sub-item OP-0009-K addresses what K is, not what selects K_act); OP-0008 σ^A K-jump non-determinism (OP-0008 ⊂ OP-0009 sub-item dynamic-σ-trajectory aspect).

**References:**
- 4-agent ontological depth analysis: inline conversation 2026-04-29 EOD (architect/critic/analyst/planner).
- OAT-1 working file: `THEORY/working/MF/K_status_commitment.md`.
- D-6a static merge: `THEORY/canonical/canonical.md` §13 T-Commitment-14-Multi-Static (CV-1.5.1).
- D-6b dynamic deferred: `THEORY/working/MF/sigma_multi_trajectory.md` Theorem 4.6.1 Cat C/B target.
- Critic 7-agent verdict 2026-04-29 EOD (escalated to ADVERSARIAL mode at Phase 2).

---

## HIGH-PRIORITY PROBLEMS 🟠

### **OP-0004: Type A/B Classification Invalidation**

**Statement:**  
04-07 proposed "Type A vs Type B" classification of K=2 configurations:
- Type A: Centered, stable, no valley-hopping
- Type B: Off-center, swap-prone, valley-hopping

exp65 conducted validation; **Type B was never observed** (0/4 configurations).

**Evidence:**
- exp65_formation_tracking.json: All 4 configs clustered at Type A
- max_center_offset = 0.01–0.08 (all < Type B threshold 0.12)
- swap_count = 0 everywhere (Type B marker absent)

**Impact:**
- Classification framework is **retracted** (unvalidated hypothesis)
- 04-07 interpretation of exp62/exp63 divergence is **rejected**
- exp62/exp63 difference attributed to optimizer strategy, not K-field type
- Branch selection work (exp66–exp73) continues but unrelated to Type A/B

**Status:** ❌ RETRACTED (empirically invalidated)  
**Severity:** 🟠 HIGH (affects theoretical narrative)  
**Last reviewed:** 2026-04-12 audit  
**References:** exp65 data, AUDIT_REPORT_2026-04-12.md

---

### **OP-0005: K Selection Mechanism (Missing)**

**Statement:**  
Theory provides no mechanism for how K (number of formations) is determined. Is it:
- Fixed externally (current assumption A-0012, unresolved F-1)?
- Emerged from energy minimization (contradicted by M-1)?
- Determined by model selection (BIC, free energy)?
- Kinetically determined (metastability barriers)?

**Impact:**
- Cannot predict K from initial conditions alone
- Theory cannot explain K emergence in biological/cognitive systems
- Required for moving from v1.2 to v2.0

**Status:** ❌ OPEN (no proposal yet)  
**Severity:** 🟠 HIGH (foundational question)  
**Related:** F-1, M-1

**2026-04-17 integration note (Phase 4):**
- Current audited `E-0082` surface provides only **weak, proxy-level support** for a persistence-scope reading, not observed-`K` selection closure.
- Current runnable/artifact evidence still lacks `tau`/`T`/`B`/cross-`K` observables and locked reruns remain blocked by `No Type B base found`.
- This is an evidence-boundary alignment note only; it does not change `OP-0005` status or severity.
- OP-0005 therefore remains OPEN; selection-mechanism status is unchanged pending a runnable `E-0082` path plus explicit selection-grade outputs.

---

### **OP-0006: Boundary Definition Precision**

**Statement:**  
Boundary B_t is currently defined via D_t (distinction operator) threshold:
- B_t = {x : D_t(u_t) > threshold}

But this is:
- Not morphologically precise (what is "boundary" exactly?)
- Lacks gradient/articulation measure
- Graded, not crisp

**Impact:**
- Affects articulation diagnostic (part of proto-cohesion d)
- Needed for precise morphological quality measure Q_morph
- Currently incomplete

**Status:** ⚠️ TENTATIVE (D-0013 in development)  
**Severity:** 🟠 HIGH (affects diagnostics)  
**Related:** D-0004 (distinction operator)

---

## MEDIUM-PRIORITY PROBLEMS 🟡

### **OP-0010: Bind Generalization**

**Statement:**  
T-Bind-Proj proved for τ=1/2 only (Category B). General τ ∈ (0,1) case (T-Bind-Full) is Category C (very conditional).

**Question:** Does projection property hold for all τ, or only τ=1/2?

**Impact:**
- Limits use of binding predicate (normalization dependent)
- Affects multi-scale analysis
- Low priority (doesn't block main theory)

**Status:** ⚠️ PARTIAL (τ=1/2 case solved)  
**Severity:** 🟡 MEDIUM (specialty case)  
**References:** theorem_registry.md (T-Bind-Proj, T-Bind-Full)

---

### **OP-0011: Transport Kernel Uniqueness**

**Statement:**  
Current transport kernel M_{t→s} form (entropy-regularized OT) is *one* realization satisfying axioms E1–E5. Is it unique? Are there other realizations?

**Impact:**
- Theoretical completeness
- Robustness of persistence results
- May affect characterization of formation inheritance

**Status:** 🔄 UNDER INVESTIGATION (exp30–exp35)  
**Severity:** 🟡 MEDIUM (impacts formalism)  
**Related:** T-Persist-1(a–e)

---

### **OP-0012: Persistence Composition**

**Statement:**  
T-Persist-Full (composition of persistence across 3+ time steps) is Category C (very conditional). Can general composition formula be proved?

**Impact:**
- Affects long-timescale predictions
- Currently only T-Persist-1 (two-step) fully proved
- Limits temporal theory

**Status:** ❌ UNRESOLVED (Category C conditional)  
**Severity:** 🟡 MEDIUM (temporal extension)  
**References:** theorem_registry.md (T-Persist-Full)

---

### **OP-0013: Closure Operator Convergence Rate**

**Statement:**  
T-6 proves closure operator has fixed point with contraction; exact rate unknown.

**Question:** What is the convergence rate as function of parameters?

**Impact:**
- Affects efficiency of closure-based algorithms
- Currently only asymptotic guarantee known
- Low practical impact

**Status:** 🔄 UNDER INVESTIGATION  
**Severity:** 🟡 MEDIUM (implementation detail)

---

## LOW-PRIORITY PROBLEMS 🟢

### **OP-0020: Dynamic Topology (Out of Scope)**

**Statement:**  
Current theory assumes X_t is fixed. What if graph topology changes over time?

**Status:** Not in current scope  
**Severity:** 🟢 LOW (future extension)

---

### **OP-0021: Stochastic Dynamics**

**Statement:**  
Theory focuses on deterministic gradient descent. How do thermal fluctuations affect dynamics?

**Related:** Kramers rate theory (exp54–exp59); under active investigation

**Status:** 🔄 UNDER INVESTIGATION (exp54–exp59)  
**Severity:** 🟢 LOW (extension work)

---

### **OP-0022: Continuous-Time Limit**

**Statement:**  
Theory on discrete graphs; what is continuous limit?

**Status:** Not addressed  
**Severity:** 🟢 LOW (theoretical extension)

---

## Problem Statistics

**Updated 2026-04-25 (W4 weekly close)**:

| Severity | Count | Blocked By | Status |
|----------|-------|-----------|--------|
| 🔴 ~~CRITICAL~~ | ~~3~~ → **0** | — | **All 3 resolved/clarified/sidestepped in W4 (2026-04-24)** |
| 🟠 **HIGH** | **3 (was 1)** | OP-0009 release-blocking for CV-1.6 Cat A | OP-0005 K-Selection (partial: σ-framework + CN15 + Commitment 16 K_field/K_act); OP-0008 σ^A K-jump non-determinism (W5 Day 3 EOD); OP-0009 Multi-Formation Ontological Foundations (W5 Day 3 EOD; sub-item OP-0009-K resolved by Commitment 16; sub-items 2-7 OAT-2~7 W6+) |
| 🟡 **MEDIUM** | 4 (was 5) | Mostly orthogonal | unchanged |
| 🟢 **LOW** | 4+ | None | Out of scope |
| **Total active open** | **5+** | — | — |
| Resolved/clarified/sidestepped (W4) | 3 | F-1, M-1, MO-1 | new (2026-04-24) |

### Distribution (post-W4, 2026-04-25)

```
Critical blockers (post-W4): NONE — all 3 (F-1, M-1, MO-1) addressed in 2026-04-24 session
                              via Theorem 2 family + T-Merge (b) + σ-framework single-formation scope.

High (affects core theory):  K-Selection (partially addressed via σ-framework, Static/Dynamic
                              Separation CN15 candidate; full mechanism still open)
Medium (extensions):          Boundary precision, Bind τ, Transport uniqueness,
                              Persist composition, Closure convergence rate
Low (future):                 Dynamic topology, Stochastic, Continuous limit
```

**Net effect**: 1년간 publication을 블록하던 Critical 3건이 모두 해소됨. v2.0 release path 가 unblocked. 단, K-Selection (OP-0005) 의 *full* mechanism 은 여전히 active research 대상 (W5+ NQ-148 cluster).

---

## Critical Path to Resolution

### ✅ Completed in W4 (2026-04-19 ~ 2026-04-25)

1. **F-1 SPLIT-RESOLVED** (OP-0001) — Both portions Cat A.
   - Pure $\mathcal{E}_{\mathrm{bd}}$ portion: T-Merge (b) canonical (already proved).
   - Full SCC portion: Theorem 2 (i) Cat A graph-class independent (T-PreObj-1 family, W4 04-24).

2. **M-1 LAYER-CLARIFIED** (OP-0002) — Proved theorem (T-Merge (b)) misframed as problem. Static/Dynamic Separation (CN15 candidate) explains apparent K=1 vs K>1 conflict.

3. **MO-1 SIDESTEPPED** (OP-0003) — Single-formation σ-framework operates on $\Sigma_m$ (no corners); current scope does not require Morse on $\Sigma^K_M$.

4. **Resolution path: Option D (premise dissolution)** — neither original A/B/C, but a fourth path discovered via SCC-intrinsic re-framing.

### Next priorities (W5+, 2026-04-26 onward)

**Immediate (next 1-2 weeks)**:
1. Canonical merge of W4 T1 results (Theorem 2 family → §13; F-1/M-1/MO-1 status updates → this file).
2. NQ-170: ζ_* crossover boundary quantification (Theorem 1 V5b verification).
3. Axiom S1' v1 user decision (canonical §6 vs §11 vs §13).

**Short-term (1–2 months)**:
1. Multi-formation σ extension (Phase 5) — would re-activate MO-1 as blocker.
2. NQ-148 (σ-jump formalization, N-1.A connection) — addresses OP-0005 K-selection partially.
3. Theorem 1 V5b ζ-scan + graph-class extension → V5b Cat A canonical promotion candidate.

**Medium-term (3+ months)**:
1. v2.0 release (path now unblocked by W4 Critical resolution).
2. Address remaining Medium-priority open problems (OP-0010..0013).
3. Multi-formation σ stratified Morse (would re-engage OP-0003).

---

## Problem Lifecycle Example: F-1

**Discovery:** 04-06 audit identified K=2 energy paradox
**Formalization:** 04-12 THEORY_STATUS_2026-04-12.md documented as critical
**Reframing:** 04-19 N-1 (Soft-Hard Switching Asymmetry) discovered as single source of F-1/M-1/MO-1 (W4 reframing)
**Foundation work:** 04-21 K_soft + ℱ_{C+E} framework — F/M/MO architectural dissolution candidate
**Empirical pivot:** 04-23 R23 Orbital Discovery + 56 stable minimizers + closure-eliminates-F=1
**Resolution:** 04-24 Theorem 2 family Cat A (graph-class independent via Theorem 2-G) + T-Merge (b) canonical → SPLIT-RESOLVED
**Current status:** OP-0001 RESOLVED (no longer blocking)
**Resolution path:** Option D (premise dissolution via SCC-intrinsic re-framing)
**Timeline actual:** Reframing-to-resolution: 6 days (04-19 to 04-24)
**Outcome:** v2.0 release path unblocked

---

**Last updated:** 2026-04-25 (W4 weekly close, post-resolution)
**Total problems:** 15+ registered
**Active blockers:** 0 critical (was 3 pre-W4; MO-1 OP-0003 re-activation trigger registered W5 Day 3 EOD CV-1.5.1 — temporally conditional on D-6b approval at CV-1.6); 3 high (OP-0005 K-Selection partial; OP-0008 σ^A K-jump non-determinism W5 Day 3 EOD; OP-0009 Multi-Formation Ontological Foundations W5 Day 3 EOD with sub-item OP-0009-K resolved by Commitment 16)
**W4 changes:** F-1 split-resolved, M-1 layer-clarified, MO-1 sidestepped (3 Critical → 0)
**Time to resolution (F-1):** 6 days from N-1 reframing (04-19) to SPLIT-RESOLVED (04-24)

---

See also: **master_problem_map.md**, **dependency_graph.md**, **milestones/** (this folder)
