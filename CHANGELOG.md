# CHANGELOG — Session Log

---


## 2026-04-01 — Status Refresh & Plan Realignment

### Summary
Consolidated the current mathematical state after the strong-regime / near-bifurcation documentation pass, verified what has actually been established, and rewrote `plan/Plan_0401.md` around the next real frontier: product-manifold basin theory, merge competitors, selection, and `exp24` integration.

### Files Created
None

### Files Modified
- `plan/Plan_0401.md` — Rewritten from a forward-looking placeholder into a status-aware live plan with completed items, current frontier, and prioritized next theorems
- `CHANGELOG.md` — Added this status-refresh session entry

### Theorem Status Changes
None

### Test Count
Last recorded: 174 tests passing (unchanged; no `scc/` code modified and no fresh re-run in this planning/documentation session)

### Open Items Carried Forward
- Product-manifold basin/sublevel theorem on `Σ_M^K`
- Explicit `(K-1)` merge competitor branch construction
- Strong-regime selection theorem / branch-choice hypothesis
- `exp24` completion and interpretation against the near-bifurcation local theory
- Canonical Spec update only after a genuine theorem-status upgrade is justified

---

## 2026-03-31 — Strong-Regime Theorem Ladder & Near-Bifurcation Local Theory

### Summary
Executed the mathematical-priority part of `plan/Plan_0331.md` without touching code: formalized a theorem ladder for the strongly-interacting regime, unified the three multi-formation temporal regimes, and isolated near-bifurcation persistence as a shrinking-window local theory rather than a full persistence theorem.

### Files Created
- `docs/03-31/proof/T-PERSIST-K-STRONG-MORSE-ATTEMPT.md` — Strong-regime proof-attempt document with explicit theorem ladder: conditional coexistence theorem, local instability proposition, conditional merge proposition, full dichotomy left conjectural
- `docs/03-31/theory/THREE-REGIME-SYNTHESIS.md` — Unified theorem-status map for well-separated, weakly-interacting, and strongly-interacting regimes
- `docs/03-31/theory/NEAR-BIFURCATION-LOCAL-THEORY.md` — Local theory showing uniform persistence failure near bifurcation and the surviving shrinking-window / shifted-threshold statements
- `plan/Plan_0401.md` — Next-step mathematical work plan continuing the strong-regime / near-bifurcation program

### Files Modified
- `docs/03-31/INDEX.md` — Added theorem-ladder proof/theory entries for the new strong-regime and near-bifurcation documents
- `docs/00-overview.md` — Updated top-level project-state header from stale I11/149-tests status to current I12/174-tests status

### Theorem Status Changes
- `T-Persist-K-Strong`: retained as **conjectured** at canonical level; clarified internally into a theorem ladder
- Strong-regime coexistence branch: sharpened to a **conditional local persistence theorem**
- Strong-regime merge branch: sharpened to a **conditional merge proposition** requiring explicit Morse/selection hypotheses
- Near-bifurcation persistence: sharpened to a **negative/local theory** — no uniform persistence theorem, only shrinking-window continuation and shifted-threshold survival

### Test Count
Last recorded: 174 tests passing (unchanged; no `scc/` code modified and no fresh re-run in this document-only session)

### Open Items Carried Forward
- Product-manifold basin/sublevel theorem on `Σ_M^K`
- Explicit construction of a nearby `(K-1)`-formation merge competitor branch
- Strong-regime transport/reoptimization selection theorem
- `exp24` completion and interpretation against the new near-bifurcation local theory
- Canonical Spec update only after a status-changing mathematical upgrade is justified by the new ladder

---

## 2026-03-31 — T-Persist-1 Gap 4/5/6 Strengthening (Session 2)

### Summary
Major advances on T-Persist-1 temporal persistence theorem: closed 3 of 4 remaining open conditions. Gap 6 (core depth) fully closed via isoperimetric proof. Gap 5 (transport concentration) upgraded: Schauder fixed-point existence proved, 3-component fingerprint tightened, boundary thinness shown to be definitional identity. Gap 4 (basin radius) corrected: r≥0.210 holds away from bifurcation but boundary-mode escape can be cheaper near shape transitions.

### Files Created
- `docs/03-31/proof/CORE-DEPTH-ISOPERIMETRIC.md` — Gap 6 closure: deep core existence via Γ-convergence + isoperimetric, H2→H2', C₂≤2.875
- `docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md` — Gap 4: escape path analysis, boundary-mode soft modes, directional basin bounds
- `docs/03-31/proof/TRANSPORT-CONCENTRATION-STRENGTHENED.md` — Gap 5: boundary thinness identity, 3-component fingerprint, Schauder fixed-point
- `docs/03-31/proof/H2-CLOSURE.md` — Intermediate core depth proof
- `experiments/exp18_core_depth_isoperimetric.py` — Core depth verification (62/62 existence)
- `experiments/exp19_saddle_point_analysis.py` — Saddle-point structure (boundary-mode dominance)
- `experiments/exp20_fingerprint_jacobian.py` — Fingerprint Jacobian norms (||∂φ/∂u|| = 1.43)
- `experiments/exp21_gap_structural_analysis.py` — Structural analysis across 9 configs
- `experiments/exp22_escape_barrier.py` — Actual escape barriers vs theoretical
- `experiments/exp23_barrier_vs_mu.py` — Barrier scaling (Δ ~ 0.037·μ^0.32, NOT μ²)
- `experiments/exp24_basin_flow_test.py` — Basin flow test (unfinished)

### Files Modified
- `Canonical Spec v2.0.md` — T-Persist-1(b,d,e) status updated, T-Persist-Full upgraded with errata
- `docs/03-31/INDEX.md` — Added proof/ section entries
- `CLAUDE.md` — Added run_all.py to experiment commands

### Theorem Status Changes
- T-Persist-1(d): H2 (hypothesis) → H2' (proved for |Core|≥25, β/α≫1)
- T-Persist-1(e): fixed-point existence: conditional → proved (Schauder)
- T-Persist-1(e): fingerprint: 4-component → 3-component (C(x,x) demoted)
- T-Persist-1(e): μ₀ threshold: 6.3 → 3.4 (tightened contraction constants)
- T-Persist-1(b): r≥0.210 universal → r≥0.210 away from bifurcation (corrected)
- T-Persist-Full: (WR) → (WR') relaxed; (H2) → (H2') proved

### Test Count
174 tests passing (unchanged — no scc/ code modified)

### Open Items Carried Forward
- Near-bifurcation persistence: μ→0 at shape transitions, basin radius→0, T-Persist-1(b) fails
- Strong-regime fixed-point selection/uniqueness (Schauder gives existence, not uniqueness beyond weak regime)
- Barrier scaling Δ_soft ~ 0.037·μ^0.32 — no clean theoretical explanation for the exponent
- exp24 (basin flow test) unfinished — would test whether gradient flow basin exceeds sublevel-set estimate

---

## 2026-03-31 — Docs Reorganization & Convention Setup

### Summary
Reorganized 148 docs/ files from flat structure into date/category hierarchy (03-26, 03-27, 03-30, 03-31). Established file management conventions (CONVENTIONS.md) and this changelog.

### Files Created
- `CONVENTIONS.md` — File & log management rules (must be read every session)
- `CHANGELOG.md` — This session log
- `docs/03-26/INDEX.md` — Day 1 index
- `docs/03-27/INDEX.md` — Day 2 index
- `docs/03-30/INDEX.md` — Day 3 index
- `docs/03-31/INDEX.md` — Day 4 index

### Files Modified
- `docs/00-overview.md` — All file path references updated to new structure
- `CLAUDE.md` — Updated docs/generalization path reference
- `Canonical Spec v2.0.md` — Updated 2 docs/repair path references

### Theorem Status Changes
None

### Test Count
174 tests passing (unchanged)

### Open Items Carried Forward
- Multi-formation temporal evolution: T-Persist-K-Strong (conjectured), strongly-interacting regime open
- Core depth δ_min ≥ 2: isoperimetric proof Step 1 done, Steps 2-3 conditional. depth-proof agent result never received (session crashed)
- T-Persist-1 Gap 4 (basin escape), Gap 5 (transport concentration), Gap 6 (interior gap) — all conditional
- Strong regime transport — open (Brouwer continuity gap)
- Near-bifurcation persistence — open
