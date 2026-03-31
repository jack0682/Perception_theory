# Unified Audit Synthesis — Soft Cognitive Cohesion Theory

**Date:** 2026-03-30
**Based on:** 6 independent audits (A1-A6), ~150KB of analysis

---

## OUTPUT A: Executive Fault Map (ranked most → least fundamental)

### TIER 1 — STRUCTURAL FAILURES (must fix before any submission)

1. **Sep predicate spec-vs-code contradiction.** Spec v2.0 §7 defines C_t-weighted Sep. Code uses u-weighted Sep (because C_t-weighted gives ~0.5 regardless). All experimental values use u-weighted. The spec is wrong. The proved Sep=1-E_sep/m holds for u-weighted ONLY. [A2, A6]

2. **T7 (Enhanced Metastability) — conceptual error.** The proof equates Hessian positive-definiteness with deeper energy basins. These are different quantities. Hessian curvature ≠ barrier height. The "4-17× deeper basins" experimental claim measures perturbation energy, not saddle-point barrier height. [A1]

3. **Transport existence theorem (Brouwer) — continuity gap UNFIXED.** The re-optimization step is discontinuous at bifurcation/Maxwell points. Paper1 presents this as a proved theorem. It is not. [A3, A6]

4. **QM1 (Q_morph vanishes on uniform) — FALSE.** For u≡c>0 on a connected graph, Q_morph = c·1 = c, not 0. The proved-results registry is wrong. [A2]

5. **Autopoiesis claim — fundamentally unsupported.** The system uses fixed operators with fixed parameters on a given graph. This is nonlinear optimization, not self-production. [A5]

6. **"No OT precedent" — false.** Mean-field games (Lasry-Lions 2007) involve transport where costs depend on the distribution. This is a structural precedent. [A3, A5]

### TIER 2 — SIGNIFICANT GAPS (should fix for credible publication)

7. **Phase transition vacuous at scale.** β_crit = 4αλ₂/|W''(c)| → 0 as graph grows (λ₂ ~ 1/k² for k×k grid). On 100×100, β_crit ≈ 0.006. The theory's central prediction is automatically satisfied on any reasonably large graph. [A4]

8. **Proto-cohesion existence — demonstrated, not proved.** The existence backbone (T8-Core) is rigorous, but predicate satisfaction at minimizers lacks quantitative bounds. Should be "supported conjecture," not "theorem." [A1]

9. **Persist code vs theory — completely different quantities.** Code: 1-||u_curr-u_prev||/||u_prev|| (L2 similarity). Theory: core-to-core structural inheritance via M_{t→s}. [A2, A3]

10. **Simplex barrier breaks analyticity for K-field.** max(0, Σu^k-1)² is C¹ not analytic. T14 (Łojasiewicz) does not extend to K-field setting. [A4]

11. **K-field T8-Core not re-derived.** Repulsion cross-terms in Hessian are POSITIVE, stabilizing the uniform state. Phase separation is HARDER with K>1, not the same. [A4]

12. **C3'' resolvent monotonicity gap.** The symmetrization step involves D^{-1/2} which depends on u(x). Monotonicity of diagonal not formally closed. [A1, A2]

13. **A1' θ_support never specified.** T20 claims A1' satisfied without specifying the threshold. Proof-blocking. [A2]

14. **Predicate-energy bridge is one-way only.** Low E → high diagnostics (proved). High diagnostics → low E (fails). The theory's interpretive core has an asymmetry the papers don't adequately address. [A1]

### TIER 3 — MODERATE ISSUES (fix for rigor, not submission-blocking)

15. T11 Γ-convergence: self-referential correction is O(1) perturbation, not Γ-limit modification. Overstated. [A1]
16. T3/T6 non-idempotent advantage: proved at closure FP only, not at energy minimizer. [A1]
17. C_t codomain: spec internally contradicts (§3.6 says [0,∞), Group C says [0,1]). [A2, A6]
18. Closure formula in paper2 differs from paper1/spec/code (missing self-retention term). [A6]
19. "Triple-mode self-reference" overstated: only 2 modes enter energy; C_t is diagnostic-only. [A5]
20. Gestalt mapping shallow in places: Cl_t ≠ contour completion, C_t ≠ co-motion. [A5]
21. PP/GWT/IIT comparison oversimplifies those theories. [A5]
22. Paper1 conclusion cites K=2 and sensitivity results not in experiments section. [A6]
23. Theorem count inflated: CLAUDE.md says "22+" but only 12 are Category A rigorous. [A6]
24. T8-Full IFT step unwritten; λ_sep/λ_bd constraint missing. [A1]
25. b_D=0 expressiveness claim unproved. [A2]

---

## OUTPUT B: Theorem Status Ledger

| # | Name | Source | Claimed | Actual | Dependencies | Failure Mode | Fix Priority |
|---|------|--------|---------|--------|-------------|-------------|-------------|
| T1 | Minimizer existence | Spec §13 | Proved | **VALID** | Compactness + continuity | — | — |
| T6a | Closure FP existence | Spec §13 | Proved | **VALID** | Brouwer | — | — |
| T6b | Closure contraction | Spec §13 | Proved | **VALID** | Banach, a_cl<4 | — | — |
| T-A2 | Monotonicity | Spec §13 | Proved | **VALID** | Sigmoid monotone | — | — |
| T20 | Axiom consistency | Spec §13 | Proved | **VALID** (A1' underspecified) | θ_support undefined | A1' vacuous | LOW |
| T8-Core | Phase transition | Spec §13 | Proved | **VALID** | Ordered pairs, Fiedler, spinodal | Vacuous at scale | MEDIUM |
| T3/T6 | Non-idempotent advantage | Spec §13 | Proved | **VALID at FP only** | ‖J_Cl‖<1 at FP | Not at minimizer | LOW |
| T7 | Enhanced metastability | Spec §13 | Proved | **CONCEPTUAL ERROR** | Hessian PD ≠ barrier | Wrong claim | **HIGH** |
| T14 | Gradient flow convergence | Spec §13 | Proved | **VALID** | Analyticity (b_D=0) | Unknown exponent | LOW |
| T11 | Γ-convergence | Spec §13 | Proved | **OVERSTATED** | Modica-Mortola base | Correction is perturbation, not Γ-limit | MEDIUM |
| C-Ax | Resolvent co-belonging | Spec §13 | Proved (C3'' gap) | **C3'' OPEN** | Symmetrization calculus | Monotonicity unproved | MEDIUM |
| QM1-4 | Q_morph axioms | Spec §13 | Proved | **QM1 FALSE** | u≡c gives Q_morph=c≠0 | Wrong theorem | **HIGH** |
| Bind bound | Bind ≥ 1-√(E_cl/n) | R13 | Proved | **VALID** | Cauchy-Schwarz | — | — |
| Sep=1-E/m | Sep_old equality | R13 | Proved | **VALID for Sep_old** | Algebraic | NOT for Sep_new | MEDIUM |
| Proto-coh | Existence | R8 | Proved w/caveats | **DEMONSTRATED** | T8-Core + quantitative gaps | Bounds missing | **HIGH** |
| T8-Full | Full-energy phase transition | R13 | Gap | **GAP** | IFT unwritten | λ constraint missing | MEDIUM |
| Sep cov. | Covariance identity | I7 | Proved | **VALID** | Algebraic | — | — |
| T-Persist-1 | Core inheritance | I7 | Proved (conditional) | **3/6 GAPS CLOSED** | ε-gentle, IFT, re-projection | 3 gaps remain | MEDIUM |
| T-Persist-2 | Persist predicate | I7 | Conditional | **UNPROVED** | Requires Gap 5 (transport conc.) | Independent hypothesis | LOW |
| Transport FP | Brouwer existence | I7 | Proved | **GAP** | Continuity at bifurcations | Unfixed | **HIGH** |
| K-form exist. | K-formation minimizer | I9 | Sketch | **CIRCULAR** | T8-Core not re-derived for K | Cross-terms stabilize | MEDIUM |

---

## OUTPUT C: Missing Mathematics Ledger

| # | Missing Item | Needed For | Type | Priority |
|---|-------------|-----------|------|----------|
| M1 | Restatement of T7 as Hessian curvature result, not barrier depth | T7 correctness | Restatement | **CRITICAL** |
| M2 | Fix QM1: either change definition (Q_morph=0 when u uniform) or change theorem | QM axioms | Theorem fix | **CRITICAL** |
| M3 | Spec update: Sep → u-weighted, matching code and proved theorems | Consistency | Spec edit | **CRITICAL** |
| M4 | Continuity of re-optimization map (or Kakutani for upper hemicontinuous) | Transport FP | New lemma | HIGH |
| M5 | Quantitative Bind/Sep/Inside bounds at T8-Core minimizer | Proto-cohesion | New analysis | HIGH |
| M6 | θ_support specification for A1' | Axiom completeness | Parameter bound | MEDIUM |
| M7 | C3'' symmetrization calculus completion | Resolvent axioms | Calculus | MEDIUM |
| M8 | T8-Full IFT argument + λ_sep/λ_bd bound | Full-energy theorem | IFT proof | MEDIUM |
| M9 | K-field Hessian analysis with cross-terms | Multi-formation | New derivation | MEDIUM |
| M10 | Analytic simplex barrier (or Łojasiewicz without analyticity) | K-field convergence | Replace barrier or new convergence | MEDIUM |
| M11 | Scale-dependent β_crit analysis (what replaces it on large graphs?) | Theory scaling | New analysis | MEDIUM |
| M12 | Basin radius persistence (Morse theory on Σ_m) | T-Persist-1 Gap 4 | New theorem | LOW |
| M13 | Transport concentration lemma | T-Persist-2 | New lemma | LOW |
| M14 | Interior gap lower bound | T-Persist-1 Gap 6 | PDE estimate | LOW |
| M15 | b_D=0 expressiveness justification | Operator completeness | Analysis | LOW |

---

## OUTPUT D: Ontological Risk Ledger

| # | Philosophical Claim | Mathematical Support | Risk Level |
|---|-------------------|---------------------|------------|
| D1 | "Formalizes autopoiesis" | None — fixed operators ≠ self-production | **FUNDAMENTALLY UNSUPPORTED** |
| D2 | "No precedent in OT literature" | False — mean-field games are precedent | **FUNDAMENTALLY UNSUPPORTED** |
| D3 | "First variational foundation for Gestalt" | Unverified — no systematic prior art review | OVERSTATED |
| D4 | "Pre-objective" despite discrete substrate | Tension acknowledged but unresolved | OVERSTATED |
| D5 | "Triple-mode self-reference" | Only 2 modes variational; C_t diagnostic | OVERSTATED |
| D6 | "PP/GWT/IIT start too late" | Oversimplifies those theories | OVERSTATED |
| D7 | "Soft ontology" | Hard constraints everywhere (Σu=m, a_cl<4, thresholds) | OVERSTATED |
| D8 | "Closure = Gestalt closure" | Neighborhood averaging ≠ contour completion | OVERSTATED |
| D9 | "10 testable predictions" | Some are model properties, not perceptual predictions | OVERSTATED |
| D10 | Self-referential structure | Genuinely supported by mathematics | ACCEPTABLE |
| D11 | "Objects are derivative" | u_t is optimized, X_t/N_t given — consistent | ACCEPTABLE |
| D12 | "Metastability as perceptual mode" | T8-Core + gradient flow convergence support this | ACCEPTABLE |

---

## OUTPUT E: Contradiction Ledger

| # | Item | File A | File B | Status |
|---|------|--------|--------|--------|
| E1 | Sep definition | Spec §7: C_t-weighted | Code: u-weighted | **CRITICAL — spec wrong** |
| E2 | C_t codomain | Spec §3.6: [0,∞) | Spec Group C: [0,1] | **Internal spec contradiction** |
| E3 | Transport FP | paper1: "proved" | I7-audit: "gap at bifurcations" | **Paper overclaims** |
| E4 | Closure formula | paper2: pure aggregation | paper1/code: self-retention+aggregation | **Paper2 simplified** |
| E5 | Theorem count | CLAUDE.md: "22+" | I6 registry: 12 Cat A | **Inflation** |
| E6 | QM1 | Registry: "proved" | A2 audit: "FALSE" | **Theorem error** |
| E7 | Paper1 conclusion | Cites K=2, sensitivity | Not in paper1 experiments section | **Forward reference to missing content** |
| E8 | T7 status | Papers: "proved" | A1 audit: "conceptual error" | **Hessian ≠ barrier** |
| E9 | Persist code vs theory | Code: L2 field similarity | Theory: core transport inheritance | **Completely different** |
| E10 | Sep "marginal" | Some docs still say marginal | Post-fix: 0.924→0.938 verified | **Stale language** |

---

## OUTPUT F: Hard Recommendations

### 1. MUST FIX BEFORE ANY PAPER SUBMISSION
- [ ] Update spec: Sep → u-weighted (matching code, proved theorems, experiments)
- [ ] Fix T7: restate as "larger minimum Hessian eigenvalue" not "deeper basin"
- [ ] Fix QM1: redefine Q_morph to give 0 on uniform fields (e.g., subtract baseline c)
- [ ] Downgrade transport FP from "theorem" to "conditional result (assuming non-degeneracy)"
- [ ] Remove "formalizes autopoiesis" — replace with "structural analogue"
- [ ] Remove "no OT precedent" — add mean-field games citation
- [ ] Fix C_t codomain internal contradiction in spec
- [ ] Align closure formula in paper2 with paper1/spec

### 2. SHOULD FIX FOR A STRONG STATIC THEORY
- [ ] Address β_crit → 0 at scale (either restrict claims to finite graphs or find scale-invariant criterion)
- [ ] Complete C3'' symmetrization proof
- [ ] Specify θ_support for A1'
- [ ] Write T8-Full IFT argument
- [ ] Distinguish T11 Γ-convergence (standard) from perturbation correction (novel)
- [ ] Downgrade proto-cohesion from "theorem" to "supported conjecture"
- [ ] Prove predicate bounds at T8-Core minimizers

### 3. NEEDED FOR TEMPORAL THEORY
- [ ] Fix transport FP continuity (use Kakutani or restrict to non-degenerate regime)
- [ ] Close Gap 4 (basin radius / Morse persistence)
- [ ] Close Gap 5 (transport concentration) or state as permanent hypothesis
- [ ] Implement theory-consistent Persist in code (core-to-core inheritance, not L2 similarity)
- [ ] Cite mean-field games as precedent; clarify what's genuinely novel (fingerprint structure)

### 4. NEEDED FOR MULTI-FORMATION THEORY
- [ ] Re-derive T8-Core for K-field (account for repulsion cross-terms in Hessian)
- [ ] Replace simplex barrier with analytic alternative (or prove convergence without Łojasiewicz)
- [ ] Implement formation-specific operators (not just K independent optimizers + repulsion)
- [ ] Add formation birth/death mechanism
- [ ] Establish K=1 vs K=2 comparison baseline

### 5. NEEDED FOR HONEST COGNITIVE SCIENCE FRAMING
- [ ] Replace "first" claims with "a" or "to our knowledge, the first"
- [ ] Soften PP/GWT/IIT comparisons — acknowledge their grouping/composition work
- [ ] Distinguish mathematical properties from empirical predictions
- [ ] Acknowledge that Gestalt mapping is "structural correspondence" not "formalization"
- [ ] Add honest section on what the theory CANNOT explain (attention, learning, hierarchy, features)

---

## OUTPUT G: Best Next Mathematical Roadmap

### PHASE 1: Emergency Fixes (1 week)
**No new math needed. Just corrections.**
1. Fix Sep definition in spec (u-weighted)
2. Fix T7 statement (Hessian curvature, not barrier depth)
3. Fix QM1 (redefine or re-prove)
4. Fix transport theorem label (conditional, not proved)
5. Fix all contradictions in E1-E10
6. Update CLAUDE.md theorem count

### PHASE 2: Close Static Theory (2-3 weeks)
**Complete the single-formation core.**
1. Prove quantitative Bind/Sep/Inside bounds at T8-Core minimizers → upgrades proto-cohesion from conjecture to theorem
2. Complete C3'' proof → closes last resolvent gap
3. Write T8-Full IFT argument → extends phase transition to full energy
4. Analyze β_crit scaling → either find scale-invariant criterion or restrict claims
5. Specify A1' θ_support → closes axiom completeness

### PHASE 3: Temporal Theory (4-6 weeks)
**Requires Phase 2 complete.**
1. Fix transport FP continuity via Kakutani or restricted domain
2. Close Gap 4 (Morse persistence on Σ_m)
3. State Gap 5 as permanent hypothesis (transport concentration) — may not be provable without additional structure
4. Implement core-to-core Persist in code
5. Cite MFG precedent properly; clarify SCC novelty = fingerprint + operator triad in cost

### PHASE 4: Multi-Formation (6-8 weeks)
**Requires Phase 2 complete. Can parallel Phase 3.**
1. Re-derive Hessian for K-field energy (with cross-terms)
2. Find critical λ_rep for K>1 formation existence
3. Replace simplex barrier with smooth alternative
4. Implement formation-specific operators
5. Run K=2 vs K=1 comparison on non-trivial graphs

### WHAT TO REMOVE OR DOWNGRADE
- Remove "autopoiesis formalization" claim → "structural analogue"
- Remove "no OT precedent" → cite MFG, clarify novelty
- Remove "22+" theorem count → "12 rigorous, 4 with gaps, 3 conjectured"
- Downgrade "first variational Gestalt foundation" → "a variational framework"
- Downgrade proto-cohesion existence from theorem to supported conjecture

### WHAT NOT TO PURSUE YET
- Continuous-space extension (would require substantial PDE theory)
- RG analysis of separation energy (speculative, low priority)
- Full multi-formation birth/death dynamics (requires Phase 4 complete)
- Empirical validation (requires collaborators with psychophysics labs)
