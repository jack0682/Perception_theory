# Phase A-B Coordination Map

**Created**: 2026-04-01  
**Team**: scc-generalization (4 agents)  
**Goal**: Generalize Category B proofs → Unify multi-formation regimes

---

## Task Dependency Graph

```
Phase A (Parallel)
├─ Task #1 (conditional-analyst): T-Persist-1(b,d,e) conditions
├─ Task #2 (generalization-strategist): T-Persist-K-Sep/Weak conditions
├─ Task #3 (conditional-analyst): Isoperimetric/Transport necessity
└─ Task #4 (generalization-strategist): λ_coupling design

        ↓ (all Phase A complete)

Phase B (Sequential)
├─ Task #5 (framework-designer): T-Persist-K-Unified theorem
├─ Task #6 (integration-lead): Canonical Spec v2.1
└─ Task #7 (integration-lead): exp45-47 validation
```

---

## Phase A: What We're Looking For

### Task #1: T-Persist-1 Conditions Analysis
**Agent**: conditional-analyst

| Part | Current Status | Questions |
|------|---|---|
| **(a) Core Inheritance** | Likely proved | Is it universal or conditional? |
| **(b) Basin Escape** | r ≥ 0.210 away from bifurcation | What's the μ scaling? Can we extend to near-bifurcation? |
| **(c) Transport Existence** | Likely proved | Unconditional or Brouwer-dependent? |
| **(d) Fixed-Point Uniqueness** | Conditional on μ ≥ 3.4 | Can we remove this bound? Is it fundamental? |
| **(e) Fingerprint Convergence** | 3-component fingerprint | Weak regime proved, strong regime? |

**Output format**:
```markdown
## Part (b): Basin Escape Radius

**Current**: r ≥ 0.210 away from bifurcation (μ >> δ)
**Fundamental?** YES/NO + explanation
**Removal difficulty**: 1-10 (1=trivial, 10=impossible)
**Scaling near bifurcation**: μ → 0 implies r → ? (predict form)
**Evidence**: [cite exp, theoretical argument]
```

---

### Task #2: Regime Conditions Comparative Analysis
**Agent**: generalization-strategist

| Regime | Key Condition | Appears in | Unique to? |
|--------|---|---|---|
| **Sep (WS)** | d_min >> 1 | T-Persist-K-Sep | Sep only |
| | SR: high spectral gap | T-Persist-K-Sep | Sep only |
| **Weak (NB-K)** | NB-K: joint spectral gap | T-Persist-K-Weak | Weak only |
| | WI: small overlap | T-Persist-K-Weak | Weak only |
| **Strong** | Barrier dominance | T-Persist-K-Strong (conj) | Strong only |
| | λ_rep >> λ_self? | ? | ? |

**Looking for**:
1. Which parameters are **universal** (appear in all regimes)?
2. Which **define regime boundaries**?
3. Can one parameter **monotonically order** all three regimes?

**Output format**:
```markdown
## Unified Parameters

| Parameter | Sep | Weak | Strong | Role |
|-----------|-----|------|--------|------|
| d_min | large | medium | small | Separation distance |
| overlap | negligible | small | significant | Interaction strength |
| λ_rep | N/A or small | small-med | critical | Repulsion strength |

## Proposed λ_coupling

**Definition**: λ_coupling := [your formula]

**Properties**:
- Dimensional analysis: [check units]
- Sep limit: λ_coupling → ∞ yields [T-Persist-K-Sep]
- Weak limit: λ_coupling → 1 yields [T-Persist-K-Weak]
- Strong limit: λ_coupling → 0 yields [T-Persist-K-Strong]
- Monotonicity: ∂regime/∂λ_coupling = [decreasing/continuous]
```

---

### Task #3: Isoperimetric & Transport Necessity
**Agent**: conditional-analyst

**Two blocking theorems**:

1. **Isoperimetric Energy Ordering**: E(u*_{2m}) < 2E(u*_m)
   - Currently proved on: homogeneous graphs only
   - Needed for: K=1 always preferred in K-Strong
   - Question: **Is this necessary or technical?**
   - If not universal: characterize failing graph topologies

2. **Transport Confinement**: C_conf√m < r_basin
   - Currently: 25-10000× slack (exp40)
   - Needed for: T-Persist-1(e) fixed-point uniqueness
   - Question: **Can we tighten the bound?**
   - If not: characterize when it fails

**Output format**:
```markdown
## Isoperimetric Ordering Necessity

**Universality**: [Proved everywhere / Proved on subset / Conjectured]
**Failing topologies** (if any): [barbell-type? star? grid?]
**Tightening path**: [proposed approach]
**Consequence if false**: T-Persist-K-Strong becomes [conditional on topology]

## Transport Confinement Tightness

**Current bound**: C_conf = O(σ√(ε_OT log n))
**Empirical slack**: 25-10000× (exp40 data)
**Tightening strategy**: [fingerprint analysis / directional bounds / ???]
**If untightenable**: Why? (proof fundamental?)
```

---

### Task #4: Unified Regime Parametrization
**Agent**: generalization-strategist

**This is the KEY output** for Phase B and experiments.

**Deliverable**: A single function λ_coupling(d_min, overlap, λ_rep, μ, ...) such that:
- λ_coupling >> Λ_sep ⟹ Sep regime
- Λ_weak ≲ λ_coupling ≲ Λ_sep ⟹ Weak regime
- λ_coupling ≲ Λ_weak ⟹ Strong regime

**Must include**:
1. Explicit formula (e.g., λ_coupling = f(d_min)/g(overlap) or whatever)
2. Dimensional analysis
3. Limiting behaviors verified
4. Proposed threshold values (Λ_sep, Λ_weak)
5. Monotonicity and smoothness properties

**Integration-lead will use this for exp45-47, so precision matters.**

---

## Phase B: What We're Synthesizing

### Task #5: Unified K-Formation Persistence Theorem
**Agent**: framework-designer

**After Tasks 1-4 complete**, synthesize into single statement:

```
Theorem (T-Persist-K-Unified):
Given K formations u^1,...,u^K on Σ^K_M with coupling measure λ_coupling,
then temporal persistence of all K formations holds with mechanism:

• If λ_coupling > Λ_sep(μ):
    Mechanism = Spectral-gap repulsion (WS)
    Rate: exponential in μ
    
• If Λ_weak ≲ λ_coupling ≲ Λ_sep:
    Mechanism = Weak-coupling transport (NB-K)
    Rate: exponential in weak-coupling parameter
    
• If λ_coupling < Λ_weak:
    Mechanism = Barrier-crossing + Kramers rate (Strong)
    Rate: exponential(-ΔE/T) [temperature-dependent]
    
Moreover:
- T-Persist-K-Sep is special case (λ_coupling → ∞)
- T-Persist-K-Weak is special case (λ_coupling ~ Λ_weak)
- T-Persist-K-Strong is special case (λ_coupling → 0)

Conditional on: [remaining structural assumptions, if any]
```

**Questions to resolve**:
- Does unified theorem work without new assumptions?
- Where do μ bounds enter (all regimes or regime-specific)?
- What about bifurcation (μ → 0)? Open or closed?
- Birth/death (variable K)? In or out of scope?

---

### Task #6: Canonical Spec v2.1 Integration
**Agent**: integration-lead

**Scope**: Update Spec §13 (Proved Results Registry)

**What to change**:
1. T-Persist-1 → **with μ bounds and removal analysis**
2. T-Persist-K-Sep, T-Persist-K-Weak → **remove or clarify conditions**
3. T-Persist-K-Unified → **new unified theorem** (if successful)
4. Isoperimetric, Transport → **necessity analysis results**
5. NEW SECTION: "Regime Classification" with λ_coupling diagram

**Output**:
- Canonical Spec v2.1 (.md)
- Transition document (old→new)
- Theorem dependency graph (optional visual)
- Errata register (what changed, why)

---

### Task #7: Experimental Validation
**Agent**: integration-lead

**Three experiments** (exp45, exp46, exp47):

1. **exp45: Sep Regime Boundary**
   - Vary d_min on 15×15, 20×20 grids
   - Predict regime transition point from λ_coupling
   - Measure: persistence, spectral gap, Hessian structure
   - Output: boundary map in (d_min, λ_coupling) space

2. **exp46: Weak-to-Strong Transition**
   - Vary overlap ratio systematically
   - Predict mechanism change from λ_coupling
   - Measure: transport convergence rate, barrier height, Hessian eigenvalues
   - Output: transition signature verification

3. **exp47: Full Phase Diagram**
   - 2D or 3D sweep: (d_min, μ) or (d_min, overlap, μ)
   - Color by inferred regime (Sep/Weak/Strong)
   - Compare to λ_coupling predictions
   - Output: unified phase diagram, quantitative agreement measure

**Deliverable**: exp45-exp47_results.json + visualization

---

## Communication Plan

**When agents complete tasks**:

1. **conditional-analyst** → SendMessage to team-lead when Task #1 done
   - Subject: "Task #1 findings: T-Persist-1(b,d,e) conditions"
2. **generalization-strategist** → SendMessage when Task #2 done (and Task #4)
   - Subject: "Task #2 findings: regime conditions + λ_coupling proposal"
3. **framework-designer** → SendMessage when Task #5 done
   - Subject: "Task #5: T-Persist-K-Unified statement"
4. **integration-lead** → Implements and coordinates tasks #6-7

**Team-lead** will:
- Receive all outputs
- Route between agents if needed
- Ask clarifying questions
- Synthesize final CHANGELOG entry

---

## Success Criteria

✅ **Phase A Success**:
- Conditions on T-Persist-1 identified as removable vs structural
- λ_coupling defined and verified to unify regime conditions
- Isoperimetric/Transport necessity analyzed

✅ **Phase B Success**:
- T-Persist-K-Unified theorem formally stated
- Canonical Spec v2.1 complete and consistent
- exp45-47 show regime boundaries match theory within <20% error

✅ **Publication Impact**:
- Paper can now describe "unified multi-formation persistence" story
- No longer three separate regimes — one family with parameter
- Ready for publication draft update
