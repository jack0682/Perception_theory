# A6: Cross-Document Contradiction and Publication-Readiness Audit

**Author:** Teammate 6 (Cross-Document Auditor) | **Date:** 2026-03-30
**Files audited:** 18 (Canonical Spec v2.0, old Spec, paper1_math.tex, paper2_cogsci.tex, I6-registries, I6-verification-report, I8-code-synthesis, I7-temporal-prover, I7-temporal-audit, I13-temporal-repair, I9-multi-formation, I5-ontological-audit, I5-consistency-audit, R13-final-math-synthesis, operators.py, diagnostics.py, energy.py, results-I8.md)

---

## 1. Contradiction Ledger

### 1.1. Sep Predicate Definition (CRITICAL)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Sep formula** | Spec v2.0 Section 7.1: C_t-weighted average `Sep = sum C_t(x,x)*D_t(x) / sum C_t(x,x)` | Code (diagnostics.py:51-63): u-weighted average `Sep = sum u(x)*D_t(x) / sum u(x)` | **CRITICAL.** The spec and the code are contradictory. |
| **Sep formula (paper1)** | Paper1 Section II-D (line 259-262): C_t-weighted, same as spec | Code: u-weighted | Paper1 matches spec; both contradict code |
| **Sep formula (paper2)** | Paper2 Section II-B (line 184-186): C_t-weighted `Sep = sum C_t(x,x)*D_t(x) / sum C_t(x,x)` | Code: u-weighted | Paper2 matches spec; both contradict code |
| **Sep empirical values** | Paper1 Section V (line 716): reports Sep~0.93 using u-weighted formulation, **openly states** using corrected u-weighted form | Spec: defines C_t-weighted | Paper1 is honest about the discrepancy at line 755; but the formal definition in Section II-D still says C_t-weighted |
| **I8 code synthesis** | I8-code-synthesis: "Sep_new was broken — C_t-weighted average ~0.5 regardless. FIXED: switched to u-weighted" | Spec v2.0 still says C_t-weighted | Spec was NEVER updated after the I8 fix |
| **Experiment results** | results-I8.md: Sep_new (C_t-weighted) stuck at ~0.5 for all configs; Sep_old (u-weighted) gives 0.88-0.94 | All formal documents still define C_t-weighted Sep | **The spec, paper1, and paper2 all formally define a predicate that is demonstrated broken** |

**Resolution:** The spec must be updated to either (a) adopt u-weighted Sep as the primary definition, or (b) explicitly state the C_t-weighted form is theoretical while the u-weighted form is used computationally. Papers must match whichever choice is made. Currently paper1 Section V-A honestly discloses the switch but the formal definition contradicts the implementation. A reviewer will catch this immediately.

### 1.2. Closure Formula (MODERATE)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Closure formula (spec/paper1)** | Spec v2.0 Section 9.2 and paper1 eq (4): `Cl(u)(x) = sigma(a_cl * ((1-eta)*u(x) + eta*(P_t u)(x) - tau_cl))` | Paper2 line 159: `Cl_t(u)(x) = sigma(a_cl/z_x * sum_y N_t(x,y)*u_t(y) - b_cl)` | **Different formula.** Paper2 uses a simplified "pure aggregation" form with no self-retention term. Missing the `(1-eta)*u(x)` component. |
| **Closure formula (code)** | operators.py:57-60: matches spec/paper1 form `a_cl * ((1-eta)*u + eta*Pu - tau_cl)` | Paper2: different form | Paper2 uses a pedagogical simplification that omits self-retention. This is not wrong per se but is a different operator. |

**Resolution:** Paper2 should either (a) present the full operator and note the simplified form is illustrative, or (b) state explicitly that it presents a simplified version and refer to paper1 for the full formula. Currently a reader comparing the two papers would see different closure operators with no explanation.

### 1.3. C_t Codomain (MODERATE)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **C_t codomain (spec §3.6)** | Spec v2.0 Section 3.6: `C_t : X_t x X_t -> [0,infinity)` with explicit explanation that resolvent produces diagonal values >= 1 | I6-verification-report: "C_t codomain: §3.6 says [0,1] but resolvent has entries >= 1" | **Already fixed in spec v2.0.** The verification report flagged the issue and the spec was updated. |
| **C_t codomain (Group C header)** | Spec v2.0 Section 6, Group C header line 306: `C_t : X_t x X_t -> [0,1]` | Spec v2.0 Section 3.6: `C_t : ... -> [0,infinity)` | **INTERNAL CONTRADICTION in the spec itself.** Section 3.6 was updated to [0,infinity) but Section 6 Group C still says [0,1]. |
| **Papers** | Paper1 line 198-204: W_sym definition, no explicit codomain stated for C_t | Paper2 line 229-233: `C_t : X_t x X_t -> [0,infinity)`, correct | Paper2 is correct; paper1 is ambiguous (acceptable). Spec Group C header needs fix. |

### 1.4. Factor Conventions (LOW — well-handled)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Critical ratio** | Spec v2.0, paper1 eq (8): `beta/alpha > 4*lambda_2/|W''(c)|` | Code (energy.py:8-10): "E_bd smoothness = 2*alpha * u^T L u, Gradient = 4*alpha*L*u" | **CONSISTENT.** All sources use factor 4. |
| **W'(u)** | Spec: `W'(u) = 2u(1-u)(1-2u)` implied by standard derivative of u^2(1-u)^2 | Code (energy.py:36): `return 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)` | **CONSISTENT.** Factor of 2 present everywhere. |
| **Hessian** | Paper1 line 244, 344: "Hessian contribution of 4*alpha*L" | Code (energy.py:10): "Hessian of smoothness = 4*alpha*L" | **CONSISTENT.** |
| **Historical issue** | I5-consistency-audit: "2*lambda_2 vs 4*lambda_2 STILL UNRESOLVED" | R13-final-math-synthesis: corrected to 4*lambda_2; Spec v2.0 updated | **RESOLVED.** The old inconsistency was fixed. I5 report is stale. |

### 1.5. Theorem Count (MODERATE)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Theorem count** | Spec v2.0 Section 13: "12 theorems from Iterations 1-2" | CLAUDE.md: "22+ proved theorems" | **Different counts.** The 12 are from I1-I2. The 22+ includes I7 temporal results and other later additions. |
| **I6 registries** | I6-registries: "12 rigorous, 4 proved with gaps, 1 proved with caveats" = 17 entries | R13-final-math-synthesis: 12 Cat A + 4 Cat B + 3 Cat C + 3 Cat D = 22 entries | The 22+ count includes conjectures and preliminary results. Calling all of these "proved" is an overclaim. |
| **Honest count** | 12 rigorous (Cat A) + 4 with gaps (Cat B) | Papers claim ~8-9 theorems formally stated | Papers are conservative; docs are not. |

**Resolution:** CLAUDE.md should say "12 rigorously proved theorems, ~10 additional results at various stages" rather than "22+ proved theorems." The "22+" conflates proved, proved-with-gaps, demonstrated, and conjectured.

### 1.6. Diagnostic Values (LOW)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Post-fix diagnostics** | I8-code-synthesis: "(Bind=0.86, Sep=0.93, Inside=0.98, Persist=1.0)" | Paper1 line 716-721: "Bind~0.86, Sep~0.93, Inside~0.98, Persist=1.0" | **CONSISTENT.** |
| **Pre-fix Sep** | results-I8.md Exp1: Sep_new ~ 0.5 for all configs | No document cites these as final | Pre-fix values are properly contextualized as broken; no stale citation found. |
| **Paper2 ablation** | Paper2 line 640-641: "BD-only: Bind=0.85, Sep=0.95, Inside=1.0" | Results-I8.md Exp3: "BD-only: Bind=0.850, Sep_new=0.500, Inside=1.000" | **DISCREPANCY.** Paper2 reports Sep=0.95 for BD-only but the raw experiment data shows Sep_new=0.500. Paper2 must be using the corrected u-weighted Sep (which gives ~0.924 per the post-fix table), but reports 0.95 — a rounding-up or different run. Minor but should be exact. |

### 1.7. Vulnerability Count (LOW)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Vulnerability count** | I5-ontological-audit: "2 critical, 5 high, 8 moderate" = 15 total | CLAUDE.md: "17 vulnerabilities found" | Minor discrepancy (15 vs 17). May include additional items from the consistency audit. Low priority. |
| **Resolution count** | I8-code-synthesis: "V12 (Parameter inconsistency): RESOLVED. V13 (Four-term independence): RESOLVED." | No comprehensive resolution tracking exists across all 15-17 vulnerabilities. | Unclear how many of the 15-17 are actually resolved. |

### 1.8. Transport Existence Proof (HIGH)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Transport existence** | Paper1 Theorem 9 (line 610-629): States fixed-point existence via Brouwer, presents as a theorem with proof sketch | I7-temporal-audit: "Transport Designer's Brouwer argument is a SKETCH, not a proof, with a fundamental continuity gap" | Paper1 presents this as a proved theorem. The audit says it has a fundamental gap (continuity of the energy minimization step in the Phi map). |
| **Continuity gap** | Paper1 proof sketch line 626: "The energy minimizer at time s is continuous in M* at non-degenerate points (by the implicit function theorem)" | I7-temporal-audit: This step requires non-degeneracy at EVERY point along the iteration, which is not verified | The qualifier "at non-degenerate points" in the proof sketch is doing enormous work. If the minimizer is degenerate at any point, Phi is discontinuous and Brouwer fails. |

**Resolution:** Paper1 should either (a) add an explicit non-degeneracy hypothesis to Theorem 9, or (b) downgrade to "proof strategy" or "conditional theorem." Currently it reads as if the proof is complete when the audit identifies a fundamental gap.

### 1.9. T-Persist-1 Status (HIGH)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **T-Persist-1 status** | I7-temporal-prover: "T-Persist-1 — PROVED" | I7-temporal-audit: "NOT 'PROVED' — it is 'PROOF STRATEGY IDENTIFIED WITH MAJOR GAPS'" | I13-temporal-repair closes 3 of 6 gaps; 3 remain. |
| **Paper1 presentation** | Paper1 Theorem 8 (line 665-687): "Temporal Core Inheritance — Conditional", honestly lists open gaps | I7 audit conclusions | Paper1 handles this well — labels it "Conditional" and lists open gaps in the proof sketch. |

### 1.10. Spec v1.0 Stale References (LOW)

| Item | File A says | File B says | Resolution needed |
|------|-------------|-------------|-------------------|
| **Old spec** | Canonical Spec (v1.0): contains original A1 (not A1'), no volume constraint, etc. | Spec v2.0: supersedes all of v1.0 | The old spec still exists in the repo. No document references it as authoritative, and the CLAUDE.md correctly says v2.0 supersedes it. Low risk. |

---

## 2. Overclaim List

### Paper 1 (paper1_math.tex)

| # | Statement | Location | What's actually proved | Fix |
|---|-----------|----------|----------------------|-----|
| O1 | Abstract: "We prove... (vii) $\Gamma$-convergence to a perimeter functional with modified surface tension in the sharp-interface limit" | Abstract, line 55 | T11 proves Gamma-convergence for the leading-order E_bd term. The "modified surface tension" from E_cl and E_sep is described as a "lower-order perturbation" — it's characterized, not fully proved. | Soften: "We prove Gamma-convergence of the leading term and characterize the self-referential corrections to the surface tension." |
| O2 | Abstract: "propose a self-referential optimal transport formulation... whose existence we establish via Brouwer's theorem" | Abstract, line 55 | Existence proof has a continuity gap at the energy minimization step (I7-temporal-audit). The non-degeneracy condition is unstated. | Add: "under a non-degeneracy hypothesis" or soften to "sketch a proof of existence." |
| O3 | "This creates a mathematically distinctive structure... without precedent in the phase-field literature" | Line 81 | This is a novelty claim that no reviewer can verify. It may be true but is unprovable. | Soften: "which, to our knowledge, has no direct precedent..." |
| O4 | Theorem 4 (Metastability): "has a strictly larger energy barrier than any corresponding minimizer of E_bd alone" | Line 386-389 | Proof requires minimizer to be close to closure fixed point. Remark at line 406-408 acknowledges this but the theorem statement does not carry this hypothesis. | Add hypothesis: "If additionally the minimizer satisfies ||u - Cl(u)|| = O(1/lambda_cl)..." |
| O5 | "Self-referential energy basins are 4-17x deeper than pure Allen-Cahn basins" | Line 866 (conclusion) | This is computational observation from specific parameters, not a proved bound. | Add: "In our experiments, self-referential energy basins were 4-17x deeper..." |
| O6 | "Multi-formation (K=2) experiments confirm spatially separated formations" | Line 866 (conclusion) | This appears in the conclusion but no multi-formation experiments are described in the experiments section. Where did these results come from? | Either add the K=2 experiment description or remove the claim. |
| O7 | "Parameter sensitivity analysis across 45 configurations shows formation quality is structurally robust" | Line 866 (conclusion) | This claim also appears without corresponding experimental description in Section V. | Either add the sensitivity analysis description or remove the claim. |
| O8 | Sep covariance identity (Proposition 1, line 559-566) | Section III | This is proved — no issue with the result. But it is presented immediately after stating Sep with C_t-weighting, while all experiments use u-weighting. The reader may assume the experiments validate C_t-weighted Sep. | Clarify which Sep definition is used in experiments vs. which is in the proposition. |

### Paper 2 (paper2_cogsci.tex)

| # | Statement | Location | What's actually proved | Fix |
|---|-----------|----------|----------------------|-----|
| O9 | "SCC provides the first variational foundation for the Gestalt laws" | Abstract, line 29 | This is a strong priority claim. While SCC does formalize several Gestalt laws, "first" is hard to verify. There is related work (e.g., variational approaches to perceptual grouping by Mumford-Shah, region competition models). | Soften: "SCC provides a variational foundation for the Gestalt laws" (drop "first") or add "to our knowledge, the first comprehensive variational foundation..." |
| O10 | "formalizes the autopoietic insight that cognitive systems maintain themselves through self-production" | Abstract, line 29 | The self-referential operator structure does formalize operational closure. But "formalizes autopoiesis" is a very strong claim — autopoiesis involves physical self-production of components, not just mathematical self-reference. | Soften: "formalizes a structural analogue of the autopoietic principle" |
| O11 | "We derive 10 empirical predictions... several of which are testable with current psychophysical and neuroimaging methods" | Abstract, line 29 | The predictions are derived from the theory but NONE have been tested. "Testable" is accurate; the risk is that readers infer some have been tested. | Add: "none yet tested" or "all awaiting empirical validation" |
| O12 | Good continuation mapped to T_t in Table I | Line 359 | T_t was DEMOTED from the formal universe in spec v2.0 (zero realizations, zero theorems). Table says "Conceptual alignment (T_t open)" but this undersells the problem — T_t doesn't exist as a formal operator. | Revise: "Open problem — no formal operator defined" |
| O13 | "Proved (Theorems 3, 4)" for Pragnanz row in Table I | Line 361 | These theorems are from the companion paper. Paper2 readers cannot verify them. The claim is legitimate but should note they are proved in the companion paper, not here. | Add: "(proved in companion paper)" |
| O14 | Paper2 closure formula (line 159) differs from paper1/spec/code | Line 159 | Paper2 uses a simplified form without the self-retention term (1-eta)*u(x). This is a different operator. | Either present the full formula or note the simplification explicitly. |
| O15 | "SCC predicts that figure-ground segregation... should precede top-down categorical effects (N2/P300)" | Line 448 | This is a prediction, not a proved result. The word "predicts" is used correctly. But the prediction depends on SCC being correct — which is circular as a "testable difference." | Clarify: this is what SCC would predict IF its account is correct — it distinguishes the theory, not the evidence. |
| O16 | Persist formula (line 219): `Persist = |Core_t ∩ M^{-1}(Core_s)| / |Core_t|` | Line 219 | This is a DIFFERENT formula than spec v2.0 Section 7.1 and paper1. Spec/paper1 use a continuous sum involving u_s(y) values. Paper2 uses a crisp set-intersection ratio. | Must use the same Persist definition as spec and paper1, or note the simplification. |
| O17 | "If the preliminary computational finding that the separation energy drives formation instability is confirmed, this has a specific enactivist implication" | Line 702 | The R13 synthesis marks the separation dominance claim as PRELIMINARY with methodological caveats (arbitrary normalization, unverified volume constraint, potential sign errors). CN13 in spec says "quantitative claim requires verification." | The hedge "if... is confirmed" is appropriate but should note the specific methodological concerns. |

---

## 3. Unsafe Statements (Hostile Reviewer Targets)

| # | Statement | Location | Risk Level | Recommended Fix |
|---|-----------|----------|------------|-----------------|
| U1 | "first variational foundation for the Gestalt laws" | Paper2 abstract | **HIGH** | Any reviewer familiar with variational segmentation (Mumford-Shah, Chan-Vese, region competition) will challenge this. Remove "first" or add extensive justification for why these don't count. |
| U2 | Sep predicate: paper defines C_t-weighted, experiments use u-weighted | Paper1 Sec II-D vs V-A; Paper2 Sec II-B | **HIGH** | A careful reviewer will note the formal definition differs from the implementation. This looks like moving goalposts. Resolve by updating the formal definition. |
| U3 | "formalizes autopoiesis" | Paper2 abstract, Sec VII-B | **MEDIUM-HIGH** | Autopoiesis scholars (Thompson, Di Paolo) will object that mathematical self-reference is not autopoiesis. Self-referential operators are not "self-producing components." Soften the claim. |
| U4 | "no precedent in the OT literature" / "without precedent in the phase-field literature" | Paper1 lines 81, 649 | **MEDIUM** | Negative existential claims invite counterexamples. Add "to our knowledge" qualifiers. |
| U5 | Allen-Cahn dominance acknowledged but then downplayed | Paper1 Sec V-B, Paper2 Sec VI | **MEDIUM** | A hostile reviewer will note: "The double-well does all the work; the novel terms are corrections. Why not just use Allen-Cahn?" The papers acknowledge this honestly but the framing should emphasize the stability advantage (proved) rather than the quantitative refinement (marginal). |
| U6 | Transport existence theorem with continuity gap | Paper1 Theorem 9 | **MEDIUM-HIGH** | A reviewer who checks the Brouwer argument carefully will find the non-degeneracy assumption is doing essential but unstated work. Either add the assumption or weaken the claim. |
| U7 | 10 empirical predictions, none tested | Paper2 Sec V | **MEDIUM** | Predictions without any empirical validation are speculative, however carefully derived. The paper is honest about this (Sec VIII-C), but a reviewer may see 10 predictions as overpromising. Consider presenting 4-5 with high testability and relegating the rest to supplementary material. |
| U8 | T8-Core proves phase transition for E_bd only, but papers discuss formations under full energy | Paper1 throughout | **LOW-MEDIUM** | The gap between T8-Core (E_bd only) and experimental formation existence (full energy) is explicitly noted (paper1 Sec V-A issue #2). But a reviewer may ask: "Do you have a phase transition theorem for your actual theory, or only for Allen-Cahn?" |
| U9 | The discrete substrate problem | Paper2 Sec VII-D | **LOW** | Paper2 handles this honestly (Sec VII-D, "not fully satisfying"). But it's a structural tension that a philosophically inclined reviewer will press. |
| U10 | Temporal theory: 3 of 6 gaps open, presented as conditional theorem | Paper1 Theorem 8 | **MEDIUM** | Honest presentation but a reviewer may question publishing a "theorem" with 3 open gaps. Consider presenting as "Proposition (conditional)" instead. |

---

## 4. Publication-Ready vs Not-Ready Assessment

### Paper 1 (paper1_math.tex) — "Self-Referential Phase Fields on Graphs"

**OVERALL: NEARLY READY, contingent on 4 fixes.**

| Section | Status | Issues |
|---------|--------|--------|
| Abstract | Needs revision | O2 (transport existence qualifier), O3 (precedent claim) |
| Introduction (Sec I) | **Ready** | Well-written, honest positioning. "No precedent" claim (line 81) needs "to our knowledge." |
| Framework (Sec II) | Needs minor fix | Sep formal definition (line 259-262) contradicts experimental implementation. Must resolve. |
| Static Theory (Sec III) | **Ready** | 8 theorems well-presented. C3'' gap honestly noted (Remark after Thm 7). T8-Core correct with ordered-pair convention. Metastability theorem needs hypothesis clarification (O4). |
| Transport (Sec IV) | Needs revision | Theorem 9 continuity gap (O2/U6). Temporal persistence (Theorem 8) is honestly conditional — acceptable. |
| Experiments (Sec V) | Needs minor fixes | Honest and thorough. Sep discrepancy well-disclosed. Missing: K=2 experiments and 45-config sensitivity analysis referenced in conclusion (O6, O7). |
| Discussion (Sec VI) | **Ready** | Honest limitations. Well-structured open problems. |
| Conclusion | Needs minor fixes | O5 (computational observation stated as general), O6/O7 (unsubstantiated claims). |

**Required fixes before submission:**
1. **Resolve Sep definition** — either update the formal definition to u-weighted or add explicit transition from formal (C_t-weighted) to computational (u-weighted) with justification.
2. **Transport existence** — add non-degeneracy hypothesis to Theorem 9 or downgrade to conditional.
3. **Remove or substantiate** K=2 and 45-config claims in conclusion.
4. **Soften** "without precedent" to "to our knowledge, without precedent."

### Paper 2 (paper2_cogsci.tex) — "Before Objects"

**OVERALL: NEEDS MODERATE REVISION.**

| Section | Status | Issues |
|---------|--------|--------|
| Abstract | Needs revision | O9 ("first variational foundation"), O10 ("formalizes autopoiesis"), O11 (predictions not tested) |
| Introduction (Sec I) | **Ready** | Excellent motivational writing. Fair characterization of existing theories. |
| Framework (Sec II) | Needs fixes | O14 (closure formula differs from paper1/spec/code), Sep definition contradicts code (same as paper1), O16 (Persist formula differs from spec/paper1). |
| Gestalt Connection (Sec III) | Needs minor fix | O12 (T_t row in Table I), O13 (cross-reference to companion paper). Otherwise excellent. |
| Theory Comparison (Sec IV) | **Ready** | Careful, honest, well-structured. |
| Predictions (Sec V) | Needs softening | O15. Consider reducing from 10 to top 5 in main text. |
| Experiments (Sec VI) | **Ready** | Honest "what experiments do not show" section is exemplary. |
| Philosophy (Sec VII) | Needs revision | O10/U3 (autopoiesis claim), O17 (enactivist implication based on preliminary finding). |
| Limitations (Sec VIII) | **Ready** | Extremely honest. Best section in the paper. |
| Conclusion | **Ready** | Appropriately measured claims. |

**Required fixes before submission:**
1. **Soften or drop "first"** in "first variational foundation for Gestalt laws."
2. **Resolve closure formula** — align with paper1/spec or note simplification.
3. **Resolve Sep definition** — same issue as paper1.
4. **Resolve Persist formula** — align with spec (continuous form, not crisp intersection).
5. **Soften autopoiesis claim** — "structural analogue" not "formalization."
6. **Update T_t row** in Gestalt table to reflect demotion.

### What Needs New Results Before Submission

Neither paper strictly needs new results — the static theory is solid and the honest framing of gaps is appropriate. However:

1. **Sep definition resolution** is a MUST-FIX that requires a decision (no new math, just a choice and consistency).
2. **K=2 experiments** referenced in paper1 conclusion either need to be included or the claim removed.
3. **45-config sensitivity analysis** referenced in paper1 conclusion either needs inclusion or removal.
4. The temporal theory is honestly presented as conditional in both papers — this is acceptable for submission.

---

## Appendix: Theorem Status Cross-Reference

| Theorem | Spec v2.0 status | I6-registries status | Paper1 presentation | Honest status |
|---------|------------------|---------------------|---------------------|---------------|
| T1 (Minimizer existence) | Cat A, proved | Rigorous | Implicit (not stated as separate theorem) | **PROVED** |
| T6a/b (Closure contraction) | Cat A, proved | Rigorous | Theorem 1 | **PROVED** |
| T8-Core (Phase transition) | Cat A, proved | Rigorous | Theorem 3 | **PROVED** |
| T8-Full (Full energy PT) | Cat B, gap | Proved with gap | Open Problem 5 | **PROVED WITH GAP** — paper1 honest |
| T3/T6 (Non-idempotent advantage) | Cat A, proved | Rigorous | Theorem 2 | **PROVED** |
| T7 (Enhanced metastability) | Cat A, proved | Rigorous | Theorem 4 | **PROVED** (with unstated hypothesis about minimizer proximity to closure fixed point) |
| T14 (Gradient flow) | Cat A, proved | Rigorous | Theorem 5 | **PROVED** |
| T20 (Axiom consistency) | Cat A, proved | Rigorous | Theorem 6 | **PROVED** |
| T11 (Gamma-convergence) | Cat A, proved | Rigorous | Theorem 7 | **PROVED** (leading order; self-referential correction characterized, not fully proved) |
| C-Axioms (Resolvent) | Cat A, but C3'' has gap | Rigorous w/ gap | Theorem 7.5 (Remark notes gap) | **PROVED WITH GAP** — paper1 honest |
| Transport existence (Brouwer) | Not in spec registry | N/A (I7 era) | Theorem 9 | **PROOF SKETCH WITH GAP** — paper1 presents as theorem |
| T-Persist-1 (Temporal) | Not in spec registry | N/A (I7 era) | Theorem 8, labeled "Conditional" | **CONDITIONAL** — paper1 honest, 3/6 gaps open |
| Sep covariance identity | Not in spec registry | N/A (I7 era) | Proposition 1 | **PROVED** |

**Summary:** Paper1 presents 9 numbered theorems + 1 proposition. Of these: 7 are rigorously proved, 1 has an honest C3'' gap noted, 1 is explicitly conditional (T-Persist-1), and 1 has an unstated continuity gap (transport existence). The paper is generally honest about status, with the transport existence theorem being the main concern.

---

## Appendix: Open Problem Framing Assessment

| Open Problem | Honest framing? | Assessment |
|-------------|----------------|------------|
| Sep marginality/refinement | **YES** — paper1 Sec V-A and Sec VI-A are remarkably honest about the marginal quantitative contribution (0.924->0.938). | Sep is an honest weakness, not a hidden failure. The theoretical role (self-referential distinction) is clear; the quantitative impact is small in current experiments. |
| Temporal theory gaps | **YES** — paper1 Theorem 8 labeled "Conditional", proof sketch lists closed and open gaps explicitly. Paper2 Sec VIII-B is honest. | Temporal theory is the biggest gap, honestly disclosed. |
| Multi-formation limitation | **YES** — paper1 Open Problem 3 and Sec VI-B. Paper2 Sec VIII-D. | Honestly framed as an architectural limitation. |
| Allen-Cahn dominance | **MOSTLY** — acknowledged but could be more prominent. The framing emphasizes the stability advantage (proved) over the quantitative refinement (marginal). | A hostile reviewer might say the novel contributions are perturbations of Allen-Cahn. The stability advantage (Theorem 2, Theorem 4) is the real mathematical contribution and should be emphasized more. |
| Transport existence continuity gap | **NO** — paper1 Theorem 9 presents this as proved. The gap is in the I7-temporal-audit but not reflected in the paper. | This is the most significant honesty gap in the papers. |
