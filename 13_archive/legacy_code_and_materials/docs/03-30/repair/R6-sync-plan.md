# R6: Publication Synchronization Plan

**Date:** 2026-03-30
**Purpose:** Master edit plan ensuring ONE consistent version of every definition, claim, and value across all files.
**Input:** SYNTHESIS.md (Output E), A2-axiom-operator-audit.md, A6-contradiction-publication-audit.md, plus all 10 source files.

---

## Dependency Order for Edits

Edits must proceed in this order, because later edits depend on earlier decisions:

1. **Canonical Spec v2.0.md** — the authoritative source. All changes here propagate outward.
2. **CLAUDE.md** — project instructions that guide all agents. Must match spec.
3. **Agent Instructions.md** — binding protocol. Minimal changes needed.
4. **papers/paper1_math.tex** — math paper. Must match spec definitions exactly.
5. **papers/paper2_cogsci.tex** — cog-sci paper. Must match spec and paper1.
6. **scc/diagnostics.py** — code comments/docstrings must match spec (logic already correct).
7. **scc/operators.py** — code comments only (logic already correct).
8. **scc/energy.py** — code comments only (logic already correct).
9. **docs/00-overview.md** — development record. Update to reflect corrected status.

---

## FILE: `/home/jack/ex/Canonical Spec v2.0.md`

### EDIT 1: Sep definition — change from C_t-weighted to u-weighted
- **Where:** §7.1 (around line 404-414)
- **Type:** definition
- **What:** Replace the C_t-weighted Sep formula:
  ```
  Sep_t(u_t) = sum_x C_t(x,x) * D_t(x; 1-u_t) / sum_x C_t(x,x)
  ```
  with the u-weighted formula:
  ```
  Sep_t(u_t) = sum_x u_t(x) * D_t(x; 1-u_t) / sum_x u_t(x)
  ```
- **Rationale:** The C_t-weighted version averages ~0.5 regardless of formation quality (A2 Issue 4.1, SYNTHESIS E1). Code, experiments, and the proved Sep-energy bridge (`Sep = 1 - E_sep/m`) all use u-weighted. The spec was never updated after the I8 fix.
- **Also update:** The surrounding prose to say "u-weighted average of distinction over the formation support" instead of "C_t-weighted average."
- **Also update:** The "Change from v1.0" note to explain the further revision from C_t-weighted to u-weighted.
- **Also update:** The note on proved bounds (line 414) — the exact equality `Sep = 1 - E_sep/m` now holds for the PRIMARY definition, not just "the original unweighted Sep."

### EDIT 2: Sep open problem — update
- **Where:** §14 or wherever "Sep theorem for Sep_new" open problem appears (around line 743)
- **Type:** definition
- **What:** Remove or revise the open problem about `Sep_new` vs `E_sep` relationship, since with u-weighting the bridge `Sep = 1 - E_sep/m` is exact. Replace with note that the C_t-weighted variant remains as an open alternative.

### EDIT 3: C_t codomain — fix Group C header
- **Where:** §6, Group C header (line 306)
- **Type:** definition
- **What:** Change `C_t : X_t × X_t → [0,1]` to `C_t : X_t × X_t → [0,∞)`
- **Rationale:** §3.6 (line 115) already says [0,∞). Group C header contradicts it. Flagged as I6 priority fix #1, never applied. (SYNTHESIS E2, A2 Issue 3.1)

### EDIT 4: Sep status note — remove reference to C_t entering Sep
- **Where:** §3.6 (line 120) — "Co-belonging enters the theory's predicates (specifically, the separation predicate Sep)"
- **Type:** wording
- **What:** Update to note that with the revised u-weighted Sep, C_t no longer enters any predicate formula directly. C_t remains a standalone diagnostic for co-belonging assessment. Alternatively, if C_t-weighted Sep is retained as an alternative, note this.

### EDIT 5: QM1 — mark as FALSE or redefine
- **Where:** §13, proved results registry (around line 797-798)
- **Type:** theorem-status
- **What:** Mark QM1 as **FALSE** with explanation: for u ≡ c > 0, Q_morph = c ≠ 0 (the surviving component has bar length c, Artic = 1). Either:
  - (a) Redefine Q_morph to subtract baseline: Q_morph = l_max · Artic - c (vanishes on uniform), or
  - (b) Weaken QM1 to "Q_morph is low on near-uniform fields" (with bound), or
  - (c) Mark QM1 as an open problem requiring resolution.
- **Rationale:** SYNTHESIS E6, A2 Issue 4.3.

### EDIT 6: T7 (Enhanced Metastability) — restate correctly
- **Where:** §13, proved results registry
- **Type:** theorem-status
- **What:** Restate T7 as "the full energy Hessian at a minimizer has a strictly larger minimum eigenvalue than the boundary-only Hessian" — which IS what's proved. Remove or correct any language equating Hessian eigenvalue with "deeper energy basin" (barrier height requires saddle-point analysis, not just local curvature). Add note: "The computational observation of 4-17× deeper basins measures perturbation energy, not saddle-point barrier height."
- **Rationale:** SYNTHESIS item #2, A1 audit.

### EDIT 7: Transport existence — mark as conditional
- **Where:** §13, wherever transport FP is referenced
- **Type:** theorem-status
- **What:** Add "under a non-degeneracy hypothesis (the energy minimizer is a smooth function of the transport kernel at the fixed point)" to the transport existence result. Mark the continuity gap as open.
- **Rationale:** SYNTHESIS E3, A6 §1.8.

### EDIT 8: Theorem count in §1
- **Where:** §1 Status Note (line 33): "12 theorems from Iterations 1–2"
- **Type:** wording
- **What:** This is actually accurate for the spec (it only claims I1-I2 theorems). No change needed here. The inflation is in CLAUDE.md.

### EDIT 9: Persist predicate — add implementation note
- **Where:** §7.1, near the Persist definition (around line 440-443)
- **Type:** wording
- **What:** Add note: "The code implementation uses a placeholder (L2 field similarity) rather than the core-inheritance formula, as the transport kernel M_{t→s} has not been implemented. See §14, Open Problems."
- **Rationale:** SYNTHESIS E9, A2 Issue 4.5.

---

## FILE: `/home/jack/ex/CLAUDE.md`

### EDIT 1: Theorem count — fix "22+ proved theorems"
- **Where:** Theory Structure Quick Reference section (line 106)
- **Type:** wording
- **What:** Change `**22+ proved theorems**` to `**12 rigorously proved theorems, 4 with proof gaps, 3 conjectured**`
- **Rationale:** SYNTHESIS E5, A6 §1.5. The "22+" conflates proved, proved-with-gaps, demonstrated, and conjectured.

### EDIT 2: Sep definition note — update
- **Where:** Critical Implementation Details section
- **Type:** wording
- **What:** Update the Sep predicate bullet to reflect that spec NOW uses u-weighted (after the spec edit). Change from "Uses u-weighted average... NOT C_t-weighted" to "Uses u-weighted average (Σ u_i·D_i / Σ u_i), matching spec §7.1 (corrected from original C_t-weighted version in I8)."

### EDIT 3: Persist note — add placeholder warning
- **Where:** Code Architecture section or Critical Implementation Details
- **Type:** wording
- **What:** Add: `**Persist**: Code implements a placeholder (L2 field similarity: 1 - ||u_curr - u_prev|| / ||u_prev||), NOT the spec's core-inheritance formula. Transport kernel M_{t→s} is unimplemented.`

### EDIT 4: T7 status — add caveat
- **Where:** Theory Structure Quick Reference, theorem list
- **Type:** wording
- **What:** In the theorem list, change T7 reference to note it's "restated as Hessian curvature result (not barrier depth)."

### EDIT 5: Transport — mark as conditional
- **Where:** Theory Structure Quick Reference, theorem list
- **Type:** wording
- **What:** Ensure transport existence is listed as "conditional (non-degeneracy hypothesis)."

---

## FILE: `/home/jack/ex/Agent Instructions.md`

### EDIT 1: No changes needed
- **Rationale:** Agent Instructions is an operational protocol, not a statement of definitions. It correctly says "the cohesion field u_t is the primitive" and does not cite specific formulas. No contradictions found.

---

## FILE: `/home/jack/ex/papers/paper1_math.tex`

### EDIT 1: Sep formal definition — change to u-weighted
- **Where:** Section II-D (line 259-262)
- **Type:** definition
- **What:** Replace C_t-weighted Sep formula with u-weighted:
  ```latex
  \Sep(u) = \frac{\sum_{x} u(x)\,\mathbf{D}(x; 1-u)}{\sum_{x} u(x)}
  ```
  Update surrounding text to say "u-weighted average of distinction" and explain: u-weighting naturally restricts to formation support, avoiding the diagnostic failure of C_t-weighting (which averages ~0.5 regardless).
- **Rationale:** SYNTHESIS E1. Currently paper1 defines C_t-weighted (line 261) but experiments use u-weighted (line 716). A reviewer will catch this.

### EDIT 2: Sep covariance identity — update context
- **Where:** Proposition 1 (line 559-566)
- **Type:** wording
- **What:** The covariance identity is for C_t-weighted Sep. After changing the primary definition to u-weighted, this proposition should be reframed as characterizing the *relationship* between the u-weighted (primary) and C_t-weighted (alternative) forms, or moved to a remark. The exact bridge `Sep = 1 - E_sep/m` for the u-weighted form should be stated as a theorem/proposition.

### EDIT 3: Sep open problem — update
- **Where:** Open Problem about Sep_new/Energy Relationship (line 836-838)
- **Type:** wording
- **What:** Update to note that the exact bridge now holds for the primary (u-weighted) Sep. The open problem becomes the relationship of the C_t-weighted *alternative*.

### EDIT 4: T7 (Enhanced Metastability) — restate
- **Where:** Theorem 4 (line 386-389) and proof sketch (line 392-396)
- **Type:** theorem-status
- **What:** Restate theorem as: "the minimum eigenvalue of the restricted Hessian of E on Σ_m at û is strictly larger for the full self-referential energy than for E_bd alone." Remove "energy barrier" language from the theorem statement. In the proof sketch, replace "a larger minimum eigenvalue means a deeper basin" (line 394) with "a larger minimum eigenvalue indicates stronger local stability" or similar. Add a remark distinguishing local curvature (proved) from barrier height (not proved).
- **Rationale:** SYNTHESIS item #2. Hessian PD ≠ barrier height. The "4-17× deeper basins" (line 866) is a computational observation about perturbation energy, not barrier height.

### EDIT 5: Transport existence — add non-degeneracy hypothesis
- **Where:** Theorem 9 (line 610-629)
- **Type:** theorem-status
- **What:** Add explicit hypothesis: "Assume the energy minimizer at time s is a non-degenerate critical point for all M in the domain." Or downgrade from "Theorem" to "Proposition (Conditional)" and note the continuity gap. Update proof sketch to acknowledge the gap explicitly.
- **Rationale:** SYNTHESIS E3, A6 §1.8. The non-degeneracy condition at line 626 is doing essential but unstated work.

### EDIT 6: Conclusion K=2 and 45-config claims — substantiate or remove
- **Where:** Conclusion (line 866)
- **Type:** wording
- **What:** The conclusion claims "Parameter sensitivity analysis across 45 configurations" and "Multi-formation (K=2) experiments confirm spatially separated formations" but neither is described in the experiments section. Either:
  - (a) Add brief experimental descriptions in Section V, or
  - (b) Remove these claims from the conclusion, or
  - (c) Soften to "preliminary experiments (not reported here) suggest..."
- **Rationale:** A6 overclaims O6, O7.

### EDIT 7: "without precedent" — soften
- **Where:** Line 81 and line 649
- **Type:** wording
- **What:** Change "without precedent in the phase-field literature" to "to our knowledge, without direct precedent in the phase-field literature."
- **Rationale:** A6 overclaim O3. Mean-field games are a structural precedent.

### EDIT 8: Γ-convergence abstract claim — soften
- **Where:** Abstract (line 55)
- **Type:** wording
- **What:** Change from claiming Γ-convergence with "modified surface tension" to "Γ-convergence of the leading boundary term with characterized self-referential corrections."
- **Rationale:** A6 overclaim O1. The correction is a perturbation, not a Γ-limit modification.

### EDIT 9: "4-17× deeper basins" — qualify
- **Where:** Conclusion (line 866)
- **Type:** wording
- **What:** Change "Self-referential energy basins are 4–17× deeper than pure Allen–Cahn basins" to "In our experiments, self-referential formations show 4–17× larger minimum Hessian eigenvalues than pure Allen–Cahn formations."
- **Rationale:** A6 overclaim O5. This is a computational observation, not a proved bound. And it measures Hessian curvature, not barrier height.

### EDIT 10: Diagnostic values — verify consistency
- **Where:** Section V (line 713-719)
- **Type:** wording
- **What:** Verify values are Bind ≈ 0.86, Sep ≈ 0.93, Inside ≈ 0.98, Persist = 1.0. These are already correct in paper1 (line 715-718). No change needed.

---

## FILE: `/home/jack/ex/papers/paper2_cogsci.tex`

### EDIT 1: Closure formula — add self-retention term
- **Where:** Line 159
- **Type:** definition
- **What:** Change from:
  ```latex
  \mathrm{Cl}_t(u)(x) = \sigma\!\left(\frac{a_{\mathrm{cl}}}{z_x} \sum_{y} N_t(x,y)\, u_t(y) - b_{\mathrm{cl}}\right)
  ```
  to the full formula matching spec/paper1/code:
  ```latex
  \mathrm{Cl}_t(u)(x) = \sigma\!\left(a_{\mathrm{cl}}\left[(1-\eta)\,u(x) + \eta\,\frac{\sum_y N_t(x,y)\,u(y)}{z_x}\right] - \tau_{\mathrm{cl}}\right)
  ```
  Or add note: "We present a simplified form; the full operator includes a self-retention term $(1-\eta)\,u(x)$; see the companion paper [ref] for details."
- **Rationale:** SYNTHESIS E4, A6 §1.2.

### EDIT 2: Sep definition — change to u-weighted
- **Where:** Line 183-186
- **Type:** definition
- **What:** Replace C_t-weighted Sep with u-weighted:
  ```latex
  \text{Sep}(u) = \frac{\sum_x u(x) \cdot D_t(x; 1-u)}{\sum_x u(x)}
  ```
  Update surrounding text to match.
- **Rationale:** SYNTHESIS E1. Must match spec and paper1.

### EDIT 3: C_t entering Sep — update prose
- **Where:** Line 243 and wherever C_t is said to enter Sep as an importance weight
- **Type:** wording
- **What:** With u-weighted Sep, C_t no longer enters the Sep formula. Update the prose about C_t's role: it remains a diagnostic for co-belonging assessment but is no longer an importance weight in Sep. (Or retain C_t-weighted as an alternative and note both.)

### EDIT 4: Persist formula — align with spec
- **Where:** Line 219
- **Type:** definition
- **What:** The paper2 Persist formula uses a crisp set-intersection ratio:
  ```
  Persist = |Core_t ∩ M^{-1}(Core_s)| / |Core_t|
  ```
  The spec uses a continuous sum. Either align with the spec formula or add note: "This is a simplified crisp version; see the companion paper for the continuous formulation."
- **Rationale:** A6 overclaim O16.

### EDIT 5: "first variational foundation" — soften
- **Where:** Abstract (line 29)
- **Type:** wording
- **What:** Change "the first variational foundation for the Gestalt laws" to "a variational foundation for the Gestalt laws" or "to our knowledge, the first comprehensive variational foundation."
- **Rationale:** A6 overclaim O9, unsafe statement U1.

### EDIT 6: "formalizes autopoiesis" — soften
- **Where:** Abstract (line 29) and Section VII-B
- **Type:** wording
- **What:** Change "formalizes the autopoietic insight" to "formalizes a structural analogue of the autopoietic principle."
- **Rationale:** SYNTHESIS D1, A6 overclaim O10.

### EDIT 7: T_t row in Gestalt table — update
- **Where:** Table I (line 359)
- **Type:** wording
- **What:** For the Good Continuation row, change from "Conceptual alignment (T_t open)" to "Open problem — no formal operator defined (T_t demoted from formal universe in v2.0)."
- **Rationale:** A6 overclaim O12.

### EDIT 8: Diagnostic values — verify consistency
- **Where:** Line 634
- **Type:** wording
- **What:** Verify values are Bind ≈ 0.86, Sep ≈ 0.93, Inside ≈ 0.98, Persist = 1.0. Already correct. No change needed.

### EDIT 9: Ablation table Sep values — verify
- **Where:** Line 640-641 (ablation results)
- **Type:** wording
- **What:** A6 §1.6 flags that paper2 reports BD-only Sep=0.95 but raw data shows Sep_new=0.500 (C_t-weighted, broken). The u-weighted value should be ~0.924. Verify and correct to exact u-weighted value from experiments.

### EDIT 10: Predictions framing — add "none yet tested"
- **Where:** Abstract (line 29) and Section V header
- **Type:** wording
- **What:** Add "none yet empirically tested" to the predictions claim.
- **Rationale:** A6 overclaim O11.

---

## FILE: `/home/jack/ex/scc/diagnostics.py`

### EDIT 1: Sep docstring — update spec reference
- **Where:** Line 52 (sep_predicate docstring)
- **Type:** wording
- **What:** Change `(Spec Section 7.1, corrected I8)` to `(Spec Section 7.1)` once the spec is updated. The "corrected I8" note will be unnecessary when spec matches.

### EDIT 2: Persist docstring — add placeholder warning
- **Where:** Line 143 (persist_predicate docstring)
- **Type:** wording
- **What:** Change `"""Persist in [0,1]: temporal inheritance. 1.0 for static optimization."""` to `"""Persist placeholder (L2 field similarity, NOT spec formula). The spec defines core-to-core inheritance via M_{t→s}, which is unimplemented. Returns 1.0 for static optimization."""`
- **Rationale:** SYNTHESIS E9, A2 Issue 4.5.

### EDIT 3: No logic changes needed
- **Rationale:** The code logic is correct. Sep uses u-weighted (correct), Bind uses √n (correct), Inside uses H0 persistence (correct). Only docstrings need updating.

---

## FILE: `/home/jack/ex/scc/operators.py`

### EDIT 1: No changes needed
- **Rationale:** Operator implementations match spec/paper1. All formulas correct. No contradictions found in code logic. Comments reference "Spec §9" correctly.

---

## FILE: `/home/jack/ex/scc/energy.py`

### EDIT 1: No changes needed
- **Rationale:** Energy implementations correct. Factor conventions (4αL, 2βW') documented and implemented correctly. No contradictions.

---

## FILE: `/home/jack/ex/docs/00-overview.md`

### EDIT 1: I8 summary — update Sep note
- **Where:** Line 302-303 (I8 summary)
- **Type:** wording
- **What:** The note "Sep predicate bug found and fixed (C_t-weighted → u-weighted)" is accurate history. No change needed. The diagnostic values (Bind=0.86, Sep=0.93, Inside=0.98, Persist=1.0) are correct.

### EDIT 2: No other changes needed
- **Rationale:** 00-overview.md is a development record, not a normative document. Historical accuracy should be preserved.

---

## Specific Synchronization Items — Resolution Summary

### 1. Sep definition: u-weighted EVERYWHERE
| File | Current | Target | Edit |
|------|---------|--------|------|
| Spec §7.1 | C_t-weighted | **u-weighted** | Spec EDIT 1 |
| paper1 §II-D | C_t-weighted | **u-weighted** | Paper1 EDIT 1 |
| paper2 §II-B | C_t-weighted | **u-weighted** | Paper2 EDIT 2 |
| diagnostics.py | u-weighted ✓ | u-weighted ✓ | Docstring only (EDIT 1) |
| CLAUDE.md | Notes u-weighted ✓ | Update note | CLAUDE EDIT 2 |

### 2. C_t codomain: [0,∞) EVERYWHERE
| File | Current | Target | Edit |
|------|---------|--------|------|
| Spec §3.6 | [0,∞) ✓ | [0,∞) ✓ | — |
| Spec §6 Group C | **[0,1] ✗** | **[0,∞)** | Spec EDIT 3 |
| paper2 line 229 | [0,∞) ✓ | [0,∞) ✓ | — |
| paper1 | Ambiguous | Leave as-is (acceptable) | — |
| operators.py | Returns raw resolvent ≥1 ✓ | ✓ | — |

### 3. Closure formula: align paper2 with paper1/spec/code
| File | Current | Target | Edit |
|------|---------|--------|------|
| Spec §9.2 | Full formula ✓ | ✓ | — |
| paper1 eq (4) | Full formula ✓ | ✓ | — |
| paper2 line 159 | **Simplified (no self-retention)** | **Full formula or noted simplification** | Paper2 EDIT 1 |
| operators.py | Full formula ✓ | ✓ | — |

### 4. Bind formula: √n denominator EVERYWHERE
| File | Current | Target | Edit |
|------|---------|--------|------|
| Spec §7.1 | √n ✓ | ✓ | — |
| paper1 | √n ✓ | ✓ | — |
| paper2 line 165 | √n ✓ | ✓ | — |
| diagnostics.py | √n ✓ | ✓ | — |
| **Status: CONSISTENT. No changes needed.** |

### 5. Factor conventions: 4αL and 2βW'(u) EVERYWHERE
| File | Current | Target | Edit |
|------|---------|--------|------|
| Spec §0, §8.4 | 4αL ✓ | ✓ | — |
| paper1 line 244, 344 | 4αL ✓ | ✓ | — |
| energy.py line 9-12 | 4αL ✓, 2βW' ✓ | ✓ | — |
| **Status: CONSISTENT. No changes needed.** |

### 6. Theorem count: fix CLAUDE.md
| File | Current | Target | Edit |
|------|---------|--------|------|
| CLAUDE.md | "22+ proved theorems" | "12 rigorous, 4 with gaps, 3 conjectured" | CLAUDE EDIT 1 |
| Spec §13 | "12 theorems from I1-I2" ✓ | ✓ | — |

### 7. Theorem labels: T7, transport, QM1
| Item | Current Status | Target | Edits |
|------|---------------|--------|-------|
| T7 | "deeper basins" (wrong) | "larger Hessian eigenvalue" (correct) | Spec EDIT 6, Paper1 EDIT 4, CLAUDE EDIT 4 |
| Transport | "proved" (gap) | "conditional (non-degeneracy)" | Spec EDIT 7, Paper1 EDIT 5, CLAUDE EDIT 5 |
| QM1 | "proved" (FALSE) | "FALSE — requires fix" | Spec EDIT 5 |

### 8. Persist: label as placeholder
| File | Current | Target | Edit |
|------|---------|--------|------|
| diagnostics.py | Minimal docstring | "placeholder (L2 similarity)" | Diagnostics EDIT 2 |
| CLAUDE.md | Not mentioned | Add placeholder note | CLAUDE EDIT 3 |
| Spec §7.1 | Formula only | Add implementation note | Spec EDIT 9 |

### 9. K=2 claims: align with audit findings
- **Decision needed:** Either add K=2 experiment description to paper1 Section V, or remove from conclusion.
- Paper1 EDIT 6 handles this.
- Paper2 lines 774-775 mention K=2 with appropriate hedging ("has been implemented and validated") — acceptable if paper1 is fixed.

### 10. Diagnostic values: Bind=0.86, Sep=0.93, Inside=0.98
| File | Values | Status | Edit |
|------|--------|--------|------|
| paper1 line 715-718 | 0.86, 0.93, 0.98, 1.0 | ✓ | — |
| paper2 line 634 | 0.86, 0.93, 0.98, 1.0 | ✓ | — |
| docs/00-overview line 303 | 0.86, 0.93, 0.98, 1.0 | ✓ | — |
| paper2 ablation (line 640-641) | BD-only Sep=0.95 | **Verify** | Paper2 EDIT 9 |
| **Status: Consistent except paper2 ablation table needs verification.** |

---

## Verification Checklist

After all edits are applied, verify the following:

### Definitions (grep across all files)
- [ ] `Sep` formula: every occurrence uses `sum u(x)*D(x) / sum u(x)` (u-weighted)
- [ ] `C_t` codomain: every occurrence says `[0,∞)` (no `[0,1]` for C_t)
- [ ] `Cl_t` formula: paper2 either matches full formula or explicitly notes simplification
- [ ] `Bind` formula: every occurrence has `√n` denominator
- [ ] `Persist` formula: every code reference notes "placeholder"

### Factor conventions
- [ ] Smoothness gradient: `4αLu` everywhere (not `2αLu`)
- [ ] Double-well derivative: `2u(1-u)(1-2u)` everywhere
- [ ] Critical ratio: `β/α > 4λ₂/|W''(c)|` everywhere

### Theorem status
- [ ] T7: "larger Hessian eigenvalue" (not "deeper basin" / "larger barrier")
- [ ] Transport existence: "conditional" or includes non-degeneracy hypothesis
- [ ] QM1: marked FALSE or redefined
- [ ] Theorem count: no document says "22+ proved"
- [ ] T-Persist-1: "conditional" with 3/6 gaps

### Claims
- [ ] No "first variational foundation" without qualifier
- [ ] No "formalizes autopoiesis" — use "structural analogue"
- [ ] No "without precedent" without "to our knowledge"
- [ ] K=2 in conclusion either substantiated or removed
- [ ] 45-config sensitivity either described or removed
- [ ] "4-17× deeper basins" qualified as computational observation about Hessian eigenvalues

### Diagnostic values
- [ ] All files report Bind ≈ 0.86, Sep ≈ 0.93, Inside ≈ 0.98, Persist = 1.0
- [ ] Paper2 ablation values verified against u-weighted recomputation

### Code-spec alignment
- [ ] `sep_predicate` docstring references Spec §7.1 (no "corrected" caveat needed post-fix)
- [ ] `persist_predicate` docstring warns about placeholder status
- [ ] No code logic changes needed (all implementations are correct)

---

## Total Edit Count by File

| File | Edits | Complexity |
|------|-------|-----------|
| Canonical Spec v2.0.md | 9 | HIGH — definition changes propagate everywhere |
| CLAUDE.md | 5 | LOW — wording updates |
| Agent Instructions.md | 0 | — |
| paper1_math.tex | 10 | HIGH — theorem restatements, definition changes |
| paper2_cogsci.tex | 10 | MEDIUM — definition alignment, claim softening |
| diagnostics.py | 2 | LOW — docstring only |
| operators.py | 0 | — |
| energy.py | 0 | — |
| docs/00-overview.md | 0 | — |
| **TOTAL** | **36 edits** | |

---

## Priority Tiers

### MUST DO (blocks submission)
1. Sep → u-weighted in spec, paper1, paper2 (Spec EDIT 1, Paper1 EDIT 1, Paper2 EDIT 2)
2. C_t codomain fix (Spec EDIT 3)
3. T7 restatement (Spec EDIT 6, Paper1 EDIT 4)
4. Transport non-degeneracy (Paper1 EDIT 5)
5. QM1 fix (Spec EDIT 5)
6. Closure formula in paper2 (Paper2 EDIT 1)
7. CLAUDE.md theorem count (CLAUDE EDIT 1)

### SHOULD DO (strengthens papers)
8. Persist placeholder labeling (Diagnostics EDIT 2, CLAUDE EDIT 3, Spec EDIT 9)
9. K=2/45-config claims (Paper1 EDIT 6)
10. "First"/"precedent" softening (Paper1 EDIT 7, Paper2 EDIT 5, EDIT 6)
11. Sep open problem updates (Spec EDIT 2, Paper1 EDITS 2-3)
12. Γ-convergence and "deeper basins" softening (Paper1 EDITS 8-9)

### NICE TO HAVE (improves consistency)
13. All remaining paper2 softening (EDITS 7, 9, 10)
14. CLAUDE.md remaining updates (EDITS 2, 4, 5)
15. Diagnostics.py docstring cleanup (EDIT 1)
