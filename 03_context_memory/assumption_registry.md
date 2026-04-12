---
id: META-0104
type: registry/assumptions
status: accepted
last_updated: 2026-04-12
---

# Assumption Registry (A-xxxx)

**Purpose:** Catalog all assumptions, constraints, and hidden dependencies in SCC theory. Prevents silent assumptions from hiding critical limitations.

**Critical principle:** Every claim (C-xxxx) must list its A-xxxx assumptions in the depends_on field.

---

## Core Axioms (Foundation)

| A-ID | Name | Statement | Status | Necessity | Notes |
|------|------|-----------|--------|-----------|-------|
| **A-0001** | Non-negativity (A1) | u_t : X_t → [0, 1]; always non-negative | axiom | fundamental | Cohesion is positive; never negative |
| **A-0002** | Boundedness (A2) | u_t(x) ∈ [0,1] for all x ∈ X_t | axiom | fundamental | Field stays in unit interval |
| **A-0003** | Closure Tendency (A3') | Conditional extensivity: u_t → Cl_t(u_t) + [corrections] | axiom | fundamental | Closure operator promotes field stabilization |
| **A-0004** | Adjacency Structure (B) | X_t = (V_t, E_t); finite graph with weighted edges | axiom | fundamental | Relational support is a graph |
| **A-0005** | Distinction Operator (D) | D_t : [0,1]^n → [0,1]; boundary contrast via (1 - u_t) | axiom | fundamental | Distinction quantifies boundary richness |
| **A-0006** | Transport Kernel (E) | M_{t→s} entropy-regularized OT; temporal correspondence | axiom | fundamental | Temporal evolution via transport |
| **A-0007** | Resolvent Integration (C) | C_t = L^{-1}[u_t]; co-belonging from graph integration | axiom | derived | Resolvent is functional of u_t and X_t |
| **A-0008** | b_D = 0 Constraint | Boundary energy coefficient must be zero | constraint | critical | Required for energy analyticity (Łojasiewicz) |

---

## Constraint Assumptions (Limits)

| A-ID | Name | Statement | Status | Applied In | Severity | Rationale |
|------|------|-----------|--------|----------|---------|-----------|
| **A-0010** | Fixed Relational Structure | X_t does not change (no dynamic topology) | constraint | all theorems | fundamental | Single-field model assumes fixed graph |
| **A-0011** | Single-Field Scope | All single-formation results (T-1–T-14) assume K=1 implicitly | constraint | T-1:T-14 | high | K-field is extension; not in base theory |
| **A-0012** | Fixed K (K-field) | K = number of formations is externally imposed, not optimized | constraint | T-Persist-K-Sep, T-Persist-K-Unified | 🔴 **CRITICAL** | F-1 issue: K not determined by energy |
| **A-0013** | Fixed Per-Formation Mass | m_j = const for each formation j (or Σ m_j = M fixed) | constraint | K-field theorems | 🔴 **CRITICAL** | F-1 issue: if m_j allowed → vary, K decreases |
| **A-0014** | Volume Constraint | ∫ u^j_t dx = m_j exactly (no tolerance) | constraint | optimization | high | Simplification; allows projection onto Σ_m |
| **A-0015** | Σ_m is Smooth Manifold | Volume-constrained set is diff'able manifold | constraint | T-8, T-14 | high | Enables gradient flow; breaks if boundary interaction |
| **A-0016** | Finite Graph | |V| = n is finite and fixed | constraint | all theorems | fundamental | No infinite dimensions; no scaling limit |
| **A-0017** | No Dynamic Boundary Flux | Mass entering/leaving X_t is zero (closed system) | constraint | all theorems | high | Prevents mass imbalance; simplifies transport |

---

## Parametric Assumptions (Ranges)

| A-ID | Name | Statement | Status | Applied In | Notes |
|------|------|-----------|--------|-----------|-------|
| **A-0020** | Spinodal Condition (Phase Transition) | β ∈ spinodal = ((3-√3)/6, (3+√3)/6) ≈ (0.089, 0.911) | condition | T-8-Full | Phase transition only in this range |
| **A-0021** | Critical β | β_crit = 4λ₂ / \|W''(c)\| where c is spinodal point | condition | T-8-Full | Exact bifurcation threshold |
| **A-0022** | Generic Parameters | λ_cl, λ_sep, λ_bd, λ_tr, λ_rep in "generic" set (residual in parameter space) | condition | several theorems | Measure-theoretic regularity (Sard) |
| **A-0023** | Non-degeneracy (NB) | Hessian/resolvent non-degenerate at minimizer | condition | T-Persist-1(b), T-3 | Genericity ensures this |
| **A-0024** | Generic Transversality (GT) | Solutions cross critical surfaces transversely | condition | T-Persist-1(b) | Kupka-Smale genericity |
| **A-0025** | Tau Normalization | τ = 1/2 in Bind definition (or general τ ∈ (0,1)) | condition | T-Bind-Proj (Cat B), T-Bind-Full (Cat C) | T-Bind-Proj proved for τ=1/2; full τ hard |

---

## Operational Assumptions (Implementation)

| A-ID | Name | Statement | Status | Applied In | Notes |
|------|------|-----------|--------|-----------|-------|
| **A-0030** | Numerical Precision (FD) | Finite difference gradient checks to 1e-9 relative error | tolerance | scc/energy.py | Verification standard for energy gradients |
| **A-0031** | Well-Separation Regime | K-field formations far apart: Sep > threshold_sep | condition | T-Persist-K-Sep | Conditional; not always satisfied |
| **A-0032** | Weakly-Interacting Regime | K-field formations weakly coupled: λ_rep small relative to within-formation energy | condition | T-Persist-K-Weak | Orthogonal regime to Sep |
| **A-0033** | Fixed Active Stratum | Active set (K-field strata) remains constant during evolution | condition | T-Persist-1(d), Kramers theory | Simplification; may break at phase transitions |
| **A-0034** | Gaussian Approximation (Hessian) | Local basin modeled as quadratic (Hessian dominates) | condition | relaxed merge analysis | Valid near minimizer |
| **A-0035** | Sinkhorn Entropy Regularization | ε_OT = 1.0 (mild entropy reg); not ε_OT → 0 | condition | Transport experiments | Affects confinement bounds |

---

## Hidden/Problematic Assumptions (Audit 2026-04-12)

| A-ID | Name | Problem | Status | Impact | Resolution Path |
|------|------|---------|--------|--------|---|
| **F-1** | K=2 Global Stability Vacuity | K must be fixed externally; but energy prefers K=1 | 🔴 **CRITICAL UNRESOLVED** | K-field theory foundation breaks if K unconstrained | Option A: explicit "external K constraint"; Option B: introduce K-selection mechanism; Option C: abandon K > 1 |
| **M-1** | M₂ Energy Landscape | K=1 always energetically preferred; K=2 requires scaffolding | 🔴 **CRITICAL UNRESOLVED** | All K=2 theorems (T-Persist-K-Sep, etc.) are conditional on vacuous foundation | Requires K-selection theory (BIC? free energy?) |
| **MO-1** | Morse Theory Inadequacy | Σ²_M is manifold with corners, not smooth manifold | 🟠 **HIGH UNRESOLVED** | T-8, T-14 may need stratified Morse theory | Option A: use existing results (sufficient); Option B: develop stratified Morse analysis |
| **Implicit K-m** | Canonical Spec doesn't state "fixed K, fixed m" | All K-field theorems assume external constraints without saying so | 🟠 **HIGH UNRESOLVED** | Theory appears self-contained but isn't | Canonical Spec v1.2 to add explicit disclaimers |
| **Type A/B** | Classification was empirically invalid | exp65 showed no Type B; exp62/exp63 divergence attributed to optimizer strategy, not K-field type | 🟠 **HIGH UNRESOLVED** | 04-07 interpretation of F'' divergence rejected | Type classification to be removed from theory; research redirect to actual cause |

---

## Assumption Dependency Graph

```
Foundational Axioms (A-0001:A-0008)
    ↓
Core Constraints (A-0010:A-0017)
    ├→ Single-Formation Theory (T-1:T-14)
    │      ↓
    │  Parametric Ranges (A-0020:A-0025)
    │      ↓
    │  (Generally safe; assumptions explicit)
    │
    └→ K-Field Theory (T-Persist-K-*, etc.)
           ├→ A-0012: Fixed K (external) 🔴 CRITICAL
           ├→ A-0013: Fixed m_j 🔴 CRITICAL
           └→ Operational Assumptions (A-0030:A-0035)
                  ↓
           (Risky; assumes K, m scaffolding exists)
```

---

## Assumption Validation Checklist

Before claiming a theorem is proved:

- [ ] **Foundational axioms (A-0001:A-0008):** Are they all justified? (Answer: yes, they define SCC)
- [ ] **Core constraints (A-0010:A-0017):** Are they acceptable? (Answer: mostly yes; A-0012, A-0013 are problematic for K > 1)
- [ ] **Parametric conditions (A-0020:A-0025):** Are specific ranges required? (If yes, document clearly)
- [ ] **Operational assumptions (A-0030:A-0035):** Do implementation details affect validity? (If yes, discuss caveats)
- [ ] **Hidden assumptions (F-1, M-1, MO-1):** Have critical vulnerabilities been acknowledged? (Answer: not yet in Canonical Spec v1.1; addressed in v1.2)

---

## Assumption Update Protocol

When a new theorem is claimed:

1. **Author lists all A-xxxx** in claim (C-xxxx) depends_on field
2. **Critic Agent checks:**
   - Are all assumptions documented?
   - Are there "hidden" assumptions (circularity, undefined terms)?
3. **Lead decides:**
   - Is this theorem's assumption set acceptable?
   - Does it depend on F-1, M-1, or MO-1? (If yes, note as conditional)
4. **Canonical Spec categorizes:**
   - Category A: depends only on foundational axioms + basic constraints
   - Category B: depends on additional parametric or operational assumptions
   - Category C: depends on very restrictive regime or unresolved open problems

---

## Open Assumption Issues

**The following assumptions lack full justification:**

1. **A-0012 (Fixed K):** Why is K fixed? Cannot it be optimized? (Answer: See F-1, unresolved)
2. **A-0013 (Fixed m_j):** Why fix mass per formation? (Answer: Simplifies optimization; violates it → K collapses, see M-1)
3. **MO-1:** Is Σ²_M really smooth? (Answer: No, it's manifold with corners; Morse theory may be invalid)

These are the three critical open problems noted in THEORY_STATUS_2026-04-12.md.

---

## Maintenance

- **Updated by:** Lead + Critic Agent
- **Reviewed:** Before every promotion to canonical
- **Validated:** All C-xxxx theorems must list assumptions; find_unregistered_assumptions.py checks

---

**Last updated:** 2026-04-12  
**Total assumptions:** 35 (8 foundational, 8 constraint, 6 parametric, 6 operational, 5 problematic)  
**Critical unresolved:** 3 (F-1, M-1, MO-1)  
**See also:** concept_registry.md, theorem_registry.md, THEORY_STATUS_2026-04-12.md
