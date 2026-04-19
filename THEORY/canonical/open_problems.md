---
id: ROADMAP-0003
type: roadmap/open_problems
status: accepted
last_updated: 2026-04-12
---

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

**Status:** ❌ UNRESOLVED  
**Severity:** 🔴 CRITICAL (blocks K-field theory foundation)  
**Last reviewed:** 2026-04-12 audit  
**References:** THEORY_STATUS_2026-04-12.md, assumption_registry.md (A-0012)

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

**Proposed resolutions:**
- **Option A:** Introduce free energy term F = E - TS (entropy penalty)
- **Option B:** Use BIC or other model selection criterion
- **Option C:** Shift from thermodynamic to kinetic framework (metastability + barriers)

**Status:** ❌ UNRESOLVED  
**Severity:** 🔴 CRITICAL (explains why F-1 exists)  
**Last reviewed:** 2026-04-12 audit  
**References:** THEORY_STATUS_2026-04-12.md

---

### **OP-0003: MO-1 — Morse Theory Inapplicability**

**Statement:**  
The K=2 constrained manifold Σ²_M = {(u¹, u²) : m_1 = m_2 = M/2} is not a smooth manifold; it has corners (at boundary where one formation's mass → 0). Smooth Morse theory requires manifolds without boundary and thus is inapplicable.

**Evidence:**
- Manifold geometry: Σ²_M is the product Σ_m × Σ_m restricted to constraint surface; this is a manifold **with corners**
- Standard Morse theory: Only works on smooth manifolds without boundary
- Implication: Theorems T-8-Core, T-14, etc. may need re-proof using stratified framework

**Impact:**
- Full global analysis of K=2 energy landscape incomplete
- Smooth bifurcation theory not applicable to M₂
- Workaround: Use existing stable results (don't claim global optimality without proof)
- Alternative: Develop stratified Morse theory analysis (significant effort)

**Related problems:** F-1, M-1 (both related to M₂ properties)

**Proposed resolutions:**
- **Option A:** Accept current stable results; no claim of global analysis (current v1.2 approach)
- **Option B:** Develop stratified Morse theory framework (more complex analysis)
- **Option C:** Reformulate analysis using alternative topology (avoid Morse theory entirely)

**Status:** ❌ UNRESOLVED  
**Severity:** 🟠 HIGH (affects global optimality claims)  
**Last reviewed:** 2026-04-12 audit  
**References:** THEORY_STATUS_2026-04-12.md

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

| Severity | Count | Blocked By | Status |
|----------|-------|-----------|--------|
| 🔴 **CRITICAL** | 3 | None | UNRESOLVED |
| 🟠 **HIGH** | 3 | F-1, M-1 | Mixed |
| 🟡 **MEDIUM** | 5 | Mostly orthogonal | Mixed |
| 🟢 **LOW** | 4+ | None | Out of scope |
| **Total** | 15+ | — | — |

### Distribution

```
Critical (blocking publication): F-1, M-1, MO-1
High (affects core theory):     Type A/B invalid, K-selection, Boundary
Medium (extensions):             Bind τ, Transport uniqueness, Persist composition
Low (future):                    Dynamic topology, Stochastic, Continuous limit
```

---

## Critical Path to Resolution

**Immediate (next 4 weeks):**
1. Choose resolution strategy for F-1/M-1 (A, B, or C)
2. If B: Begin K-selection mechanism development
3. If C: Begin kinetic theory reformulation

**Short-term (1–2 months):**
1. If B: Complete K-selection + upgrade K-field theorems
2. If C: Complete kinetic axiomatics + re-derive results
3. Address OP-0004 (Type A/B retraction): Update all references

**Medium-term (3+ months):**
1. Resolve MO-1 if pursuing Option B above
2. Address OP-0005 through OP-0013 (secondary problems)
3. Prepare v2.0 for publication

---

## Problem Lifecycle Example: F-1

**Discovery:** 04-06 audit identified K=2 energy paradox  
**Formalization:** 04-12 THEORY_STATUS_2026-04-12.md documented as critical  
**Current status:** OP-0001 in roadmap (CRITICAL, UNRESOLVED)  
**Options:** Three proposed resolutions (A, B, C)  
**Timeline:** 4–6 weeks to choose + execute  
**Expected outcome:** v2.0 released with foundation clarified

---

**Last updated:** 2026-04-12  
**Total problems:** 15+ registered  
**Critical blockers:** 3 (F-1, M-1, MO-1)  
**Time to resolution:** 6–13 weeks (if pursuing Option B or C)

---

See also: **master_problem_map.md**, **dependency_graph.md**, **milestones/** (this folder)
