# Expected Outputs: Phase A-B Unification Project

**Created**: 2026-04-01  
**Status**: interrupted after Task #1 completion; Phase A/B not integrated

---

## Stop Point (2026-04-02)

This project stopped after **Task #1** was completed and before the rest of the Phase A outputs were fully materialized and integrated.

**What is actually done:**
- Task #1 is complete in [CONDITIONAL-CONDITIONS-ANALYSIS.md](/Users/ojaehong/ex_2/docs/04-02/analysis/CONDITIONAL-CONDITIONS-ANALYSIS.md).
- A provisional Task #4 output exists in [UNIFIED-REGIME-PARAMETRIZATION.md](/Users/ojaehong/ex_2/docs/04-02/theory/UNIFIED-REGIME-PARAMETRIZATION.md), but it still needs reconciliation with the missing Task #2 and Task #3 outputs.
- A provisional Task #5 draft exists in [T-PERSIST-K-UNIFIED.md](/Users/ojaehong/ex_2/docs/04-02/theory/T-PERSIST-K-UNIFIED.md), but it still contains placeholders awaiting Phase A findings.

**What is not done:**
- Task #2 does not yet exist as a completed standalone output.
- Task #3 does not yet exist as a completed standalone output.
- Phase A findings have not been integrated into [PHASE-AB-SYNTHESIS.md](/Users/ojaehong/ex_2/docs/04-02/integration/PHASE-AB-SYNTHESIS.md).
- Canonical Spec v2.1 was not started.
- exp45-47 were scaffolded but not brought to runnable state.

**Resume tomorrow from here:**
1. Write the missing Task #2 deliverable: regime-condition comparison across Sep / Weak / Strong.
2. Write the missing Task #3 deliverable: isoperimetric-ordering necessity + transport-confinement necessity/tightness.
3. Reconcile Task #4 (`lambda_coupling`) with Tasks #2-3 and revise thresholds if needed.
4. Replace placeholders in Task #5 and then update [PHASE-AB-SYNTHESIS.md](/Users/ojaehong/ex_2/docs/04-02/integration/PHASE-AB-SYNTHESIS.md).
5. Only after that, repair and run `exp45`-`exp47`, then decide whether Canonical Spec v2.1 is justified.

## Phase A Expected Outputs (In Progress)

### Task #1: T-Persist-1(b,d,e) Conditions Analysis
**Agent**: conditional-analyst  
**Status**: 🟢 In progress (40+ min)  
**Expected by**: ~30-45 min total

**Output Format**:
- Document: `CONDITIONAL-CONDITIONS-ANALYSIS.md`
- Summary table: Part (a)-(e) | Current condition | Fundamental? (Y/N) | Difficulty (1-10) | Scaling near μ→0 | Evidence

**Key Information to Extract**:
```
(a) Core inheritance:
    - Current: [read from T-PERSIST-FULL-PROOF.md]
    - Structural necessity: [Y/N, explain]
    
(b) Basin escape radius:
    - Current: r ≥ 0.210 away from bifurcation
    - μ scaling: extract exact threshold μ_0 or δ
    - Near-bif behavior: r(μ) → ? as μ → 0
    - Evidence: exp31, exp32, exp33
    
(d) Fixed-point uniqueness:
    - Current: Conditional on μ ≥ 3.4 (or similar)
    - Fundamental? Weyl bound tightness / Brouwer gap?
    - Removal difficulty: numerical (1000 init) / theoretical (IFT)
    
(e) Fingerprint convergence:
    - Current: 3-component φ = (u, Cl(u), D)
    - Weak regime: μ ≥ 3.4
    - Strong regime: [open question]
```

**Downstream Use**: 
- Framework-designer will know if T-Persist-1 conditions are ready for unification
- Integration-lead will know what to put in Spec v2.1 (full proof or conditional)

---

### Task #2: T-Persist-K-Sep/Weak Conditions Comparative Analysis
**Agent**: generalization-strategist  
**Status**: 🟢 In progress (40+ min)  
**Expected by**: ~30-45 min total

**Output Format**:
- Document: `REGIME-CONDITIONS-COMPARATIVE.md`
- Conditions table: Regime | Condition | Parameter | Role

**Expected Findings**:
```
Sep (WS):
  - WS: d_min > d_threshold
  - SR: spectral repulsion (high μ despite coupling)
  - Why: large separation prevents overlap

Weak (NB-K):
  - NB-K: joint spectral gap μ_K ≥ μ_threshold
  - WI: overlap integral σ < σ_threshold
  - Why: weak coupling allows independent evolution

Strong (T-Persist-K-Strong):
  - Barrier dominance (height scales as O(β^0.89))
  - K=2 always local minimum (from exp30)
  - Why: energy landscape has merge barrier

Common parameters:
  - All depend on μ (spectral gap)
  - All depend on K (number of formations)
  - All depend on λ_rep (repulsion strength)
  - All sensitive to overlap structure
```

**Preliminary λ_coupling Hypotheses**:
```
Hypothesis 1: λ_coupling = d_min / √(overlap ratio)
Hypothesis 2: λ_coupling = μ · d_min · (1 - overlap_integral)
Hypothesis 3: λ_coupling = exp(-overlap_integral) · (d_min / √n)
Hypothesis 4: [generalization-strategist's own idea]
```

**Downstream Use**:
- Integration-lead needs λ_coupling to design exp45-47
- Framework-designer needs to know if regimes share structure

---

### Task #3: Isoperimetric & Transport Confinement Necessity
**Agent**: conditional-analyst  
**Status**: ⏳ Blocked by Task #1 (15-30 min after #1 done)

**Expected by**: ~60-75 min total

**Output Format**:
- Appended to `CONDITIONAL-CONDITIONS-ANALYSIS.md`
- Necessity table: Theorem | Universal? | Slack | Tightening path | Failure modes

**Isoperimetric Ordering** E(u*_{2m}) < 2E(u*_m):
```
Current status: Proved on homogeneous graphs
Question: Necessary for T-Persist-K-Strong?
Expected findings:
  - Works on: regular lattices, homogeneous connectivity
  - Fails on: [specific topologies, if any]
  - Why: [fundamental isoperimetric inequality vs graph structure]
  - If fails: T-Persist-K-Strong becomes [conditional on topology]
```

**Transport Confinement** C_conf√m < r_basin:
```
Current status: Proved with 25-10000× slack (exp40)
Question: Can we tighten the bound?
Expected findings:
  - Current bound: O(σ√(ε_OT log n))
  - Empirical ratio: actual transport displacement / bound
  - Tightening: fingerprint analysis / directional bounds
  - If untightenable: why? (fundamental limitation)
```

---

### Task #4: Unified Regime Parametrization (λ_coupling Design)
**Agent**: generalization-strategist  
**Status**: ⏳ Blocked by Task #2 (15-30 min after #2 done)

**Expected by**: ~60-75 min total

**Output Format**:
- Document: `UNIFIED-REGIME-PARAMETRIZATION.md`
- Explicit formula for λ_coupling
- Phase diagram: λ_coupling vs regime class

**Expected Deliverable**:
```
Definition:
  λ_coupling := [explicit function of d_min, overlap, λ_rep, β, μ]
  
Examples (likely candidates):
  λ_coupling := d_min / max(1, overlap_ratio)
  λ_coupling := d_min · exp(-overlap_integral) · (μ/μ_critical)
  λ_coupling := [information-theoretic measure of formation independence]

Properties:
  - Dimensional: [check units]
  - Limits:
    * d_min → ∞: λ_coupling → ∞ ⟹ Sep regime
    * overlap → 1: λ_coupling → 0 ⟹ Strong regime
    * overlap → 0: λ_coupling → ∞ ⟹ Sep/Weak regime
  - Monotonicity: ∂regime/∂λ_coupling = [decreasing/smooth]

Thresholds:
  Λ_sep: λ_coupling > Λ_sep ⟹ T-Persist-K-Sep applies
  Λ_weak: Λ_weak < λ_coupling < Λ_sep ⟹ T-Persist-K-Weak applies
  Λ_strong: λ_coupling < Λ_weak ⟹ T-Persist-K-Strong applies
```

**Downstream Use**:
- Framework-designer plugs this into unified theorem
- Integration-lead uses to compute exp45-47 regime boundaries
- Paper uses to show "unified regime family"

---

## Phase B Expected Outputs (After Phase A)

### Task #5: T-Persist-K-Unified Theorem
**Agent**: framework-designer  
**Status**: ⏳ Blocked by Tasks #1-4  
**Expected by**: ~90-120 min total

**Output Format**:
- Document: `T-PERSIST-K-UNIFIED.md`
- Formal theorem statement (1-2 pages)
- Proof sketch (3-4 pages)

**Expected Structure**:
```
Theorem (T-Persist-K-Unified):

Given:
  - K formations u^1,...,u^K on product manifold Σ^K_M
  - Coupling measure λ_coupling [from Task #4]
  - Spectral gap μ ≥ μ_min [from Task #1]
  
Then:
  [Case 1: Sep regime (λ >> Λ_sep)]
    Persistence holds with rate exp(μ · d_min)
    Mechanism: Spectral-gap repulsion maintains separation
    Proof structure: [T-Persist-K-Sep recipe]
    
  [Case 2: Weak regime (Λ_weak ≲ λ ≲ Λ_sep)]
    Persistence holds with rate exp(weak-coupling parameter)
    Mechanism: Weak transport + coupling decay
    Proof structure: [T-Persist-K-Weak recipe]
    
  [Case 3: Strong regime (λ << Λ_weak)]
    Persistence holds with rate exp(-barrier height / temperature)
    Mechanism: K=2 local min + barrier crossing
    Proof structure: [T-Persist-K-Strong coexistence branch]

Moreover:
  (i) Regime transitions are continuous in λ_coupling
  (ii) All three existing theorems are special cases
  (iii) Bifurcation (μ → 0): persistence budget → 0 in all regimes
  
Conditional on:
  [remaining structural assumptions, if any]
```

**Dependency Graph**:
```
Task #5 depends on all of Task #1-4:
  - Task #1 provides: μ scaling, basin bounds, fingerprint conditions
  - Task #2 provides: regime condition comparison
  - Task #3 provides: necessity analysis (which conditions to keep)
  - Task #4 provides: λ_coupling definition + thresholds
```

---

### Task #6: Canonical Spec v2.1 Integration
**Agent**: integration-lead  
**Status**: ⏳ Blocked by Task #5 (will start ~120 min)  
**Expected by**: ~150-180 min total

**Output Format**:
- File: `Canonical Spec v2.1.md` (revised)
- File: `SPEC-V2-TO-V21-TRANSITION.md` (errata + changelog)

**Expected Changes**:
```
Section §13 (Proved Results Registry):

OLD:
  - T-Persist-1: [Category C: conditional on 5 parts]
  - T-Persist-K-Sep: [conditional on WS, SR]
  - T-Persist-K-Weak: [conditional on NB-K, WI]
  - T-Persist-K-Strong: [conjectured, theorem ladder]

NEW:
  - T-Persist-1: [upgraded with μ scaling info from Task #1]
  - T-Persist-K-Unified: [new unified theorem incorporating all three]
  - Necessity Analysis: [isoperimetric/transport from Task #3]
  
NEW SECTION: "Regime Classification"
  - Definition of λ_coupling
  - Phase diagram in (λ_coupling, μ) space
  - Predicted regime boundaries
  - Experimental validation predictions (exp45-47)
```

**Errata to Record**:
```
*(Erratum 2026-04-01): Multi-formation persistence theorems unified*
- Previous approach: three separate theorems (Sep, Weak, Strong)
- New approach: single theorem parametrized by λ_coupling
- Consequence: condition removal/clarification in T-Persist-1(b,d,e)
- References: Phase A-B synthesis, Tasks #1-5
```

---

### Task #7: Experimental Validation (exp45-exp47)
**Agent**: integration-lead  
**Status**: ⏳ Blocked by Task #4 (can start ~75 min)  
**Expected by**: ~180-240 min total (including exp runtime)

**Output Format**:
- File: `exp45_sep_boundary.py`, `exp46_weak_strong.py`, `exp47_full_diagram.py`
- File: `exp45-47_results.json` (collected results)
- Visualization: phase diagrams

**Expected Data**:
```
exp45: Sep regime boundary
  - Vary d_min on 15×15, 20×20 grids
  - Compute λ_coupling for each configuration
  - Measure: persistence, spectral gap, regime class
  - Output: scatter plot (d_min vs λ_coupling, colored by regime)
  - Question: does λ_coupling_threshold match prediction?

exp46: Weak-to-Strong transition
  - Vary overlap ratio (adjust K=2 position)
  - Compute λ_coupling
  - Measure: transport convergence, barrier height, diagnostics
  - Output: boundary signature (where does mechanism change?)
  
exp47: Full phase diagram
  - 2D sweep: (d_min, overlap) or (d_min, μ)
  - Compute λ_coupling for all configs
  - Classify regime (Sep/Weak/Strong)
  - Output: unified phase diagram showing all three regimes
  - Compare: experimental boundaries vs λ_coupling predictions
```

---

## Summary Timeline

```
Time    | Task | Agent | Status
--------|------|-------|--------
T+0     | #1,#2 | conditional, strategist | 🟢 Start
T+40min | Check-in | all | Progress check
T+50min | #1 | conditional-analyst | ✅ Complete
T+50min | #3 | conditional-analyst | 🟢 Unblock, start
T+50min | #2 | strategist | ✅ Complete
T+50min | #4 | strategist | 🟢 Unblock, start
T+75min | #3,#4 | both | ✅ Complete
T+75min | #5 | framework-designer | 🟢 Start synthesis
T+75min | #7 | integration-lead | 🟢 Start exp skeleton → full code
T+120min| #5 | framework-designer | ✅ Complete
T+120min| #6 | integration-lead | 🟢 Start Spec v2.1
T+180min| #6,#7 | integration-lead | ✅ Complete
```

**Total expected**: ~3 hours for full Phase A-B completion

---

## Success Metrics

### Phase A Success ✅
- [ ] T-Persist-1(b,d,e) conditions analyzed (removable vs structural)
- [ ] λ_coupling designed and dimensionally checked
- [ ] Isoperimetric/transport necessity analyzed
- [ ] Regime conditions unified in comparative table

### Phase B Success ✅
- [ ] T-Persist-K-Unified formally stated
- [ ] Proof sketch connects all three regimes
- [ ] Canonical Spec v2.1 updated and consistent
- [ ] exp45-47 designed and ready to run

### Publication Success ✅
- [ ] Can now describe "unified multi-formation persistence as single family"
- [ ] Paper narrative: "Three regimes unified by coupling parameter λ_coupling"
- [ ] New theorems + revised §13 ready for publication update
