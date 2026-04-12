# Task #6 Theory Validator Checklist

**Prepared by:** Experimenter (Task #5 agent)
**Date:** 2026-04-03
**Purpose:** Pre-integration consistency checks for Task #6 spec update

---

## 1. Cross-Theorem Consistency

- [x] **C-Axioms (C1-C4) all Cat A** — No contradictions with operator theorems.
  - C3'' proof (Task #1) uses conjugation identity for `D^{-1/2} W_u D^{-1/2}` symmetrization.
  - Code (`scc/graph.py:140-145`) confirmed to use geometric-mean symmetrization, matching the proof.
  - Task #4 audit of C3PP-PROOF.md flagged arithmetic-mean discrepancy, but this was the *old scaffold* — Task #1's final proof confirms alignment. **No gap.**

- [x] **MERGE Theorem (parts a-d) — barrier formulation alignment.**
  - MERGE barrier: linear interpolation scales as $\Theta(\beta)$ (Part d).
  - Basin depth (T-Persist-1(b)): $\Delta_{\mathrm{bdy}} \approx 2\mu^3/(3L_3^2)$ — this is the *escape barrier along soft mode*, NOT the merge barrier.
  - These are **distinct barriers** serving different purposes: MERGE = inter-formation merge energy cost; Basin = local escape from single-formation basin.
  - **No contradiction.** The merge barrier > basin escape barrier (confirmed by exp30 curvature +1541 vs exp44 basin containment at $\varepsilon = 0.10$).

- [x] **SINKHORN-Lipschitz (Cat A) — confinement upgrade compatibility.**
  - Sinkhorn-Lipschitz provides basin containment via computable sufficient condition.
  - TC-FORMATION-CONDITIONED (Cat B) provides tighter quantitative bounds but inherits shallow-core condition.
  - Per Task #4 audit recommendation: Sinkhorn-Lipschitz may **subsume** TC entirely. During Task #6, check whether TC is still referenced independently or can be cited as "subsumed by Sinkhorn-Lipschitz."
  - **No contradiction** — Sinkhorn is strictly stronger.

- [x] **T-Persist-1(b) Cat A (unconditional) — Sard/Kupka-Smale argument coherence.**
  - Kupka-Smale removes NB ($\mu > 0$ for generic params) — Section 3.
  - Sard removes GT ($\Delta > 0$ for generic params) — Section 4.
  - "Generic" = full-measure, residual (dense) in parameter space. On finite graphs, semi-algebraically generic (complement is proper algebraic subvariety).
  - The argument correctly chains: Kupka-Smale (Section 3) → Sard (Section 4) → BC' Cat A (cited from F1-BOUND-CATA-UPGRADE.md) → T14 Lojasiewicz (Cat A) → convergence.
  - **Verified coherent.** One subtlety: the "sufficiently gentle" transition condition remains quantitative, not structural — this is correctly noted in Section 5.3.

- [x] **FORMATION-BIRTH (D₄) Cat A — alignment with exp51 findings.**
  - Formation Birth Theorem is about *parametric birth* (β crossing β_crit) — creates a formation from uniform state.
  - exp51 tests *K-selection* (which K is optimal for given graph) — different question.
  - These are compatible: parametric birth creates K=1 formation at β_crit (confirmed by exp37). K>1 requires K-field architecture (exp57).
  - **No contradiction.** Recommend noting in spec that Formation Birth addresses single-formation parametric emergence, not multi-formation K-selection.

## 2. Experiment-to-Theory Alignment

- [x] **exp30/exp37 validate MERGE barrier model.**
  - exp30: K=2 curvature +1541 to +1914 (all positive = local min). Confirms MERGE Part (a).
  - exp37: Zero hysteresis, supercritical pitchfork with two distinct branches. Confirms Formation Birth Thm 1/1a.
  - exp37 β_crit discrepancy (empirical 5.0 vs T8-Core 0.52, ratio 9.5×): Known issue — T8-Core formula uses Fiedler eigenvalue which gives a *sufficient* condition, not tight. **Flag for spec note.**

- [x] **exp40-41/exp44-45 validate T-Persist-1(b)/(e).**
  - exp40: 6/6 bound valid, persistence ≥ 0.9 in all configs.
  - exp41: Naive bound valid (max ratio 0.48). Tighter bounds B1-B4 exceed actual displacement.
  - exp44: 14/14 comprehensive tests pass including T-Persist chain.
  - exp45: 8/8 regime classification agreement.
  - **Full validation for transport and basin theory.**

- [x] **exp38 shows β^1.24 > β^0.89 (conservative bound).**
  - MERGE Theorem Part (d): barrier $= \Theta(\beta)$ (linear in $\beta$).
  - exp38 empirical: barrier $\propto \beta^{1.24}$ (superlinear).
  - **Slight tension:** MERGE says $\Theta(\beta)$ but experiment shows $\beta^{1.24}$. However, $\Theta$ notation means "same order" not "exactly linear." The superlinear growth is *compatible* with an upper bound of $O(\beta \log \beta)$ or similar.
  - **Recommend:** Update MERGE Part (d) to say "barrier $= \Omega(\beta)$" (at least linear, possibly superlinear) and cite exp38 exponent 1.24 as empirical observation.

- [x] **exp39/exp51 expected non-validation under architectural paradigm.**
  - exp39: K=1 always preferred (no spontaneous birth on homogeneous grid).
  - exp51: K*=1 always (spectral K-selection doesn't predict optimizer K).
  - Both consistent with "K is architectural" (exp54-57 paradigm shift from 04-02).
  - **Recommend:** Ensure spec explicitly states K is fixed by K-field architecture, not selected by energy minimization over K.

## 3. Paradigm Shift Consistency

- [ ] **Is K explicitly listed as architectural (not thermodynamic) in updated spec?**
  - Check Canonical Spec §10 (Multi-formation) or wherever K-field architecture is defined.
  - Must state: "K is an architectural parameter set by initialization, not emergent from energy minimization."
  - Cross-reference: MULTI-FORMATION-PARADIGM-SHIFT.md (docs/04-03/).

- [ ] **Do T-Persist theorems reflect this (K fixed by initialization)?**
  - T-Persist-K-Unified should state K is given (not derived).
  - T-Persist-K-Sep/Weak should condition on "K well-separated formations exist" not "K formations emerge."

## 4. Final Edits Review (Task #6 execution)

- [ ] All spec edits syntactically correct and logically coherent?
- [ ] No stale references or dangling citations (e.g., references to retracted K-Saddle conjecture)?
- [ ] Completeness % accurately computed from final category counts?
- [ ] Retracted results (K-Saddle Conjecture, Theorem 3.3) clearly marked?
- [ ] exp38 barrier exponent (1.24 vs 0.89) noted in spec or open-issues register?

## 5. Cross-Check: 4 Proof Files Coherence

### C3-SYMMETRIZATION-COMPLETE.md (Task #1)
- [x] Conjugation identity $\mathbf{C}_t(x,x) = d(x) \cdot [H^{-1}](x,x)$ — verified algebraically correct.
- [x] Schur complement derivative $f'(s) = \mathbf{v}^T G_0 \mathbf{v}$ — exact cancellation verified, FD match to $< 10^{-8}$.
- [x] Code alignment confirmed (`scc/graph.py:140-145` uses `D^{-1/2}`).
- **No issues.**

### T-PERSIST-1B-UNCONDITIONAL.md (Task #3)
- [x] Kupka-Smale argument: Transversality of gradient map verified (Section 7.2).
- [x] Sard's theorem applied correctly to barrier function (Section 6.3).
- [x] BC' Cat A dependency correctly cited (F1-BOUND-CATA-UPGRADE.md).
- [x] Exp44 cross-validation section (Section 8) matches actual exp44 results (14/14 PASS).
- **Minor note:** Section 8.2 quotes "a_cl/4=0.875" but exp44 output shows 0.7762 < 0.8750 (PASS). These are consistent (closure FP rate < a_cl/4). **No issue.**

### CONDITIONAL-PROOFS-AUDIT.md (Task #4)
- [x] 6 files audited with clear category assignments.
- [x] C3PP-PROOF code discrepancy flag is resolved by Task #1 (geometric-mean now in code).
- [x] MERGE Theorem correctly assessed as Cat A (generic params).
- [x] Recommendations are actionable and non-contradictory.
- **One stale item:** Audit §6 says "Block on Task #1 for code alignment" — Task #1 is now complete and code is aligned. This blocker is resolved.

### EXP-VERIFICATION-RESULTS.md (Task #5)
- [x] 12 experiments run, 9/12 PASS.
- [x] 3 failures correctly diagnosed with common root cause.
- [x] Experiment outputs match stored JSON results.
- **No issues.**

---

## Summary: Issues for Task #6 Integration

| # | Issue | Severity | Action |
|---|-------|----------|--------|
| 1 | exp38 barrier exponent (1.24 vs predicted 0.89) | Low | Note in spec as "empirical, exceeding conservative bound" |
| 2 | β_crit empirical/theoretical ratio 9.5× (exp37) | Low | Note T8-Core gives sufficient condition, not tight |
| 3 | K architectural paradigm not yet in spec | Medium | Add explicit statement in multi-formation section |
| 4 | Audit blocker on C3PP code alignment | Resolved | Task #1 completed, code uses D^{-1/2} |
| 5 | TC vs Sinkhorn-Lipschitz subsumption | Low | Clarify relationship in spec; consider TC as "refinement" |

**Overall assessment: GREEN — ready for Task #6 integration.** No blocking contradictions found across the 4 proof files. Two low-severity notes (exp38 exponent, β_crit ratio) and one medium item (architectural K statement) to address during integration.
