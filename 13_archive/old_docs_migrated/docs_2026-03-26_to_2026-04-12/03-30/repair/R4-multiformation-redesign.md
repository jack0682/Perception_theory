# R4: Multi-Formation Redesign Decision

**Date:** 2026-03-30
**Author:** Teammate 4 — Multi-Formation Redesign Planner
**Input:** A4 audit, SYNTHESIS, A1 audit, I9-multi-formation.md, scc/multi.py, results_multiformation.md

---

## Recommendation: OPTION B — Minimal Viable Multi-Formation

Keep K=2 as an honest proof-of-concept. Remove all theoretical claims. Focus effort on closing the static and temporal single-formation theory.

---

## 1. Option Analysis

### Option A: Repair Current K-Field — REJECTED

**What it would require:**
1. Replace simplex barrier `max(0, S-1)²` with analytic alternative (log-barrier or smooth exponential)
2. Re-derive T8-Core for K-field Hessian with cross-terms (block matrix eigenvalue analysis)
3. Implement formation-specific operators (available-capacity-modulated closure `ω^k_t`, formation-specific co-belonging `C^k_t`)
4. Implement boundary repulsion term (specified in I9 §3.3 but silently dropped from code)
5. Add formation birth/death mechanism (variable-mass formulation)
6. Run K=1 vs K=2 baseline comparison
7. Address repulsion-quality tradeoff (find a repulsion form that doesn't destroy Inside at strong coupling)

**Effort:** 6-8 weeks realistically (the 3-4 week estimate from the task is optimistic — the K-field Hessian analysis alone is a nontrivial research problem, and the formation-specific operators require new gradient derivations and JVP implementations).

**Why rejected:**
- The static single-formation theory has **8 Tier-1/Tier-2 issues** (SYNTHESIS §F) that must be fixed before any submission. These are more fundamental and more tractable.
- The K-field Hessian analysis (M9 in Missing Math Ledger) may reveal that multi-formation phase separation requires conditions not satisfiable in practice — the repulsion cross-terms *stabilize* the uniform state, and it's unknown whether the instability condition has solutions for interesting parameter ranges.
- The current `multi.py` doesn't implement I9's theoretical contribution (formation-specific operators). Repairing it means essentially rewriting it. At that point it's new work, not repair.
- Risk of 6-8 weeks invested with a negative result (K-field phase separation may be fundamentally harder than I9 assumed).

### Option B: Minimal Viable Multi-Formation — RECOMMENDED

**What it requires:**
1. Demote K=2 from "theoretical result" to "proof-of-concept demonstration" in papers
2. Remove any forward references to K=2 theorems (paper1 conclusion cites K=2 results not in experiments — SYNTHESIS E7)
3. Add K=1 baseline comparison at volume_fraction=0.5 (one experiment, ~30 minutes)
4. Keep `multi.py` as-is (working code, useful for exploration)
5. In I9 document, clearly mark all unimplemented features and open problems
6. In papers, mention multi-formation as "future work with preliminary implementation"

**Effort:** ~1 week (mostly paper edits + one baseline experiment).

**What's preserved:**
- The I9 architecture *decision* (K-field is the right approach — this is well-reasoned and worth keeping)
- The K=2 weak-repulsion result (two spatially separated formations with Bind>0.88, Sep>0.79, Inside>0.74 — genuinely interesting)
- The `multi.py` code (useful for future development)
- The honest acknowledgment that multi-formation is an active research direction

**What's lost:**
- Any claim that multi-formation theory is "done" or "proved"
- K-field theorems in the paper (there are none that are valid anyway)
- The impression that multi-formation is a solved extension

**Publishability impact:** POSITIVE. Removing premature multi-formation claims *strengthens* the papers by focusing on what's actually proved. Reviewers will respect honest "future work" framing far more than overclaimed results with known gaps.

### Option C: Defer Entirely — VIABLE BUT UNNECESSARY

**What it requires:**
1. Remove all multi-formation content from papers
2. Remove K=2 mention from paper1 conclusion
3. State as open problem in future work section

**Effort:** 0 weeks (just cutting).

**What's preserved:** Nothing from I9.

**What's lost:** The proof-of-concept demonstration, the architecture decision record, the preliminary positive results at weak repulsion.

**Why not chosen:** Option B costs only ~1 week more than Option C and preserves genuinely useful preliminary results. The K=2 weak-repulsion demonstration is worth showing if framed honestly. Cutting it entirely would mean I9's work is invisible to reviewers, losing credit for a well-reasoned architecture decision.

---

## 2. Specific Paper Edits Under Option B

### Paper 1 (math paper)

**REMOVE:**
- Any theorem statements about K-field energy minimizers
- Any claim that T8-Core extends to K>1
- Any claim that T14 (Łojasiewicz convergence) extends to K-field
- The K=2 citation in the conclusion (SYNTHESIS E7)

**ADD (future work section, ~1 paragraph):**
> The K-field architecture extends the single-formation theory to K coupled cohesion fields with a simplex participation constraint. Preliminary implementation demonstrates two spatially separated formations on grid graphs at weak repulsion (λ_rep ≈ 1), with diagnostic values comparable to single-formation results. However, the K-field extension introduces open mathematical problems: (1) the simplex barrier used in implementation is C¹ but not analytic, breaking the Łojasiewicz convergence guarantee; (2) the phase transition analysis (Theorem X) has not been re-derived for the K-field Hessian, where repulsion cross-terms stabilize the uniform state; (3) the repulsion-quality tradeoff limits the regime in which high-quality spatially separated formations coexist. Resolving these issues and developing formation-specific operator modifications is ongoing work.

### Paper 2 (cognitive science paper)

**REMOVE:**
- Any claim that multi-formation is a solved capability
- Any implication that the theory handles multiple objects in a scene

**ADD (limitations/future work, ~1 paragraph):**
> The current theory addresses a single cohesive formation. Real perception involves multiple simultaneous formations (objects, groups). We have adopted a K-field architecture (K coupled fields with mutual exclusion) and demonstrated preliminary K=2 results, but the mathematical foundation for multi-formation—particularly phase transition conditions and convergence guarantees—remains open. This is a significant limitation: a complete theory of pre-objective cohesion must ultimately handle the generic multi-formation case.

---

## 3. Required Baseline Experiment

Before finalizing Option B, run ONE experiment:

**K=1 at volume_fraction=0.5 on 20×20 grid** (same total mass as K=2 with 0.25 each).

- If K=1 at m=0.5 produces a single formation with diagnostics comparable to or better than K=2 individual formations → the K=2 result is not demonstrating genuine multi-formation behavior, just splitting one formation. Report this honestly.
- If K=1 at m=0.5 produces a formation that is clearly different (e.g., spanning the whole grid, lower Sep) → the K=2 result is genuinely showing spatial decomposition. This strengthens the proof-of-concept.

Either outcome is publishable if reported honestly.

---

## 4. What Stays in the Codebase

| Item | Action | Reason |
|------|--------|--------|
| `scc/multi.py` | **Keep as-is** | Working code, useful for exploration and future development |
| `I9-multi-formation.md` | **Keep, add status header** | Architecture decision is well-reasoned; mark implementation status clearly |
| `results_multiformation.md` | **Keep, add baseline** | Add K=1 comparison when available |
| K-field tests (if any) | **Keep** | Regression protection for existing functionality |
| Multi-formation in `CLAUDE.md` | **Update** | Change "K-field architecture decided" to "K-field architecture decided; implementation is proof-of-concept, theory gaps remain" |

---

## 5. Roadmap After Option B

Once the static single-formation theory is closed (SYNTHESIS Phase 2, ~2-3 weeks), multi-formation can be revisited with a clear agenda:

1. **K-field Hessian analysis** (M9): Compute full nK×nK Hessian at (c/K,...,c/K), find conditions on λ_rep for instability. This is the gate — if the instability condition is impossible or vacuous, the K-field approach needs fundamental rethinking.
2. **Analytic barrier** (M10): Replace max(0,·)² with log-barrier or smooth exponential. Straightforward.
3. **Formation-specific operators**: Implement ω^k-modulated closure, verify contraction still holds. Medium difficulty.
4. **Boundary repulsion**: Implement the spec'd `λ_bdy · Σ_{xy} N(x,y) u^j(x) u^k(y)` term. Straightforward.

Steps 2-4 are engineering. Step 1 is the research question. Don't invest in 2-4 until 1 has a positive answer.

---

## 6. Honest Assessment of I9

The I9 architecture decision (Option B: K-field) is **correct**. The four-option evaluation is thorough, the rejection of peeling/spectral/localization is well-justified, and K-field is the right framework for multi-formation SCC. The commitment notes (CN15-CN17) are sound.

The problem is entirely in execution and premature claims:
- The implementation (`multi.py`) implements ~30% of the I9 specification (pointwise repulsion only, no formation-specific operators, no boundary repulsion, no formation death)
- The barrier choice breaks a load-bearing mathematical guarantee
- The T8-Core extension was flagged as "open" in I9 §5.5 but this caveat didn't propagate to paper claims
- The K=2 results are presented as if they validate the full theory, when they validate only that "K independent optimizations + weak pointwise repulsion = two blobs"

None of this invalidates the architecture. It means the architecture is a solid plan that needs 6-8 weeks of careful work to execute, and should not be presented as complete until that work is done.

---

## 7. Summary

| Criterion | Option A (Repair) | **Option B (Minimal)** | Option C (Defer) |
|-----------|------------------|----------------------|-----------------|
| Effort | 6-8 weeks | **~1 week** | 0 |
| Risk | High (may get negative result) | **Low** | None |
| I9 value preserved | Full | **Partial (architecture + demo)** | None |
| Paper honesty | Requires completed work | **Honest framing of open work** | Clean but loses credit |
| Publishability | Blocks submission by 2 months | **Unblocks immediately** | Unblocks immediately |
| Single-formation focus | Delayed | **Preserved** | Preserved |

**Bottom line:** The single-formation theory has enough genuine issues to occupy all available effort for the next 4-6 weeks (SYNTHESIS Phases 1-2). Multi-formation is a real and important extension, but it's a Phase 4 item. Option B preserves everything worth preserving from I9 without blocking the critical path. Ship the single-formation theory first, then come back with the mathematical foundation that multi-formation deserves.
