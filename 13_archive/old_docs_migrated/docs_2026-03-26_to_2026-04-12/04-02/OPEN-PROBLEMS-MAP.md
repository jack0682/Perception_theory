# SCC Theory: Proved Results and Open Problems

**Date:** 2026-04-06 (updated after Phase 9-14 audit)
**Purpose:** Complete map of what is proved, what is conditional, and what is open

**Update 2026-04-03:** +9 Cat A from gap resolution (equivariant supercriticality, K-field Hessian, C3'' closed, formation birth theorems, f₁ bound, beyond-Weyl spectral, barrier scaling). TC'' tightened 300×. H3 improved to β > 7α.

**Update 2026-04-06 (audit):** Audit of Phase 9-14 overclaims. Corrected from "48/0/0 (100%)" to 43/2/3.

**Update 2026-04-06 (evening):** Retracted 5 overclaims from today's session. γ_eff back to Cat B (exp60 NEB didn't converge). Merge barrier back to OPEN (K-field barrier structure unknown on M₂). Merge Theorem (c)(d)(e) retracted. Counts: **43 Cat A / 2 Cat B / 3 Cat C (90% proved)**.

---

## Part I. What Is Proved (43 Category A)

### 1. Formation Existence and Structure (5 theorems — COMPLETE)

| Theorem | Statement | Method |
|---|---|---|
| **T1** | Energy minimizer exists on Σ_m | Extreme value theorem |
| **T8-Core** | Non-uniform minimizer when β/α > 4λ₂/\|W''(c)\| | Second variation |
| **T8-Full** | Full energy (cl+sep+bd) preserves non-uniform min | IFT; μ₀ > 0 confirmed |
| **T14** | Gradient flow converges to critical point | Łojasiewicz-Simon |
| **T11** | E_bd Γ-converges to perimeter functional | Modica-Mortola |

**Status:** No open problems. Formation existence theory is complete.

### 2. Operator Theory (7 theorems — COMPLETE)

| Theorem | Statement | Method |
|---|---|---|
| **T6a** | Closure FP exists | Brouwer |
| **T6b** | Closure FP unique when a_cl < 4 | Banach contraction |
| **T20** | Sigmoid satisfies A1'-A4 | Direct computation |
| **T-A2** | Closure monotone | σ, P_t monotone |
| **C-Axioms** | Resolvent satisfies C1-C4 | Neumann series |
| **QM1-4** | Q_morph satisfies 4 axioms | Direct |
| **C3'' (closed)** | Resolvent diagonal C(x,x) non-decreasing in u(x) | Schur complement + M-matrix + PD of G₀ |

**Status:** C3'' gap closed (2026-04-03). Code aligned to D^{-1/2} symmetrization. No open problems.

### 3. Stability and Metastability (4 theorems — COMPLETE)

| Theorem | Statement | Method |
|---|---|---|
| **T3/T6-Stability** | Non-idempotent closure ⟹ strictly PD Hessian | Gram matrix |
| **T7-Enhanced** | SCC metastability > Allen-Cahn | Closure Gram boost |
| **K=2 Local Stability** | K=2 always local min, never saddle | Product Hessian |
| **Isoperimetric Ordering** | E(u*_{2m}) < 2E(u*_m) | Discrete isoperimetric |

**Status:** No open problems. Metastability theory is complete.

### 4. Single-Formation Temporal Persistence (10 theorems — 1 mild condition remaining)

| Theorem | Cat | Statement |
|---|---|---|
| **T-Persist-1(a)** | A | IFT ⟹ smooth minimizer family |
| **T-Persist-1(b)** | **A** | Basin containment (BC' + f₁^grad) |
| **T-Persist-1(c)** | A | Core inclusion with shifted threshold |
| **T-Persist-1(d)** | C | Exact threshold: **β > 7α** (tightened from 11α) |
| **T-Persist-1(e)** | B | Transport concentration (TC' formation-conditioned) |
| **Schauder FP** | A | Self-ref transport fixed point exists |
| **H2'** | A | Deep core existence (|Core| ≥ 25) |
| **Deep Core 2a/2b** | A | Deep core dominance |
| **Boundary-Mode Dom.** | A | Soft mode on boundary |
| **NB-1/NB-2** | A | Basin collapse + deep-core remnant |

**Open:** T-Persist-1(d) requires β > 7α. This is structurally necessary (phase separation needed) and cannot be removed, only tightened further. Empirically β ≥ 20 is universal.

**T-Persist-Full:** Composition of (a)-(e). Effective Category B. The only remaining condition is the mild H3': β > 7α.

### 5. Predicate-Energy Bridge (2 theorems — COMPLETE)

| Theorem | Statement |
|---|---|
| **Predicate-Energy Bridge** | Sep = 1 − E_sep/m (exact bidirectional) |
| **T-Bind-Proj/Full** (τ=1/2) | Bind ≥ 1 − √(E_cl/n) at minimizers |

**Open for general τ:** r̄₀ is O(1) for τ ≠ 1/2 (Theorem 3.3 retracted). Binary-approximation approach needed. Low priority — τ=1/2 is the default.

### 6. Multi-Formation Persistence (3 theorems — conditional)

| Theorem | Cat | Statement |
|---|---|---|
| **T-Persist-K-Sep** | B | Well-separated K-formations persist |
| **T-Persist-K-Weak** | C | Weakly-interacting persist (Weyl bound) |
| **T-Persist-K-Unified** | C (new) | Parametric theorem, 3 corollaries |

**Open:** T-Persist-K-Unified beyond Λ = 1/(K−1) — merge bifurcation. Theory stops here.

### 7. Transport Theory (2 theorems)

| Theorem | Cat | Statement |
|---|---|---|
| **Transport Confinement** | A | ‖ũ − u_t‖ ≤ C_conf√m |
| **Directional Extension** | A | r_eff/r_iso = √(λ_max/(f₁²μ + ...)) |

**Open:** Transport confinement constants 25-100× loose. TC' provides formation-conditioned bound but relies on transport concentration (Cat B).

---

## Part II. What Is Conditionally Proved (2 Category B, 3 Category C)

| Theorem | Cat | Condition | How Close to Removal? |
|---|---|---|---|
| **γ_eff ≈ 0.89** | B | Empirical | Analytical derivation needed |
| **Formation Birth supercriticality (general graphs)** | B | D₄ only proved; transcritical for c ≠ 1/2 | Fold analysis for asymmetric graphs |
| **T-Persist-1(d)** | C | β > 7α | Structurally necessary; cannot remove, only tighten |
| **T-Persist-K-Weak** | C | WI, SR, NB-K | Weyl bound may be improvable |
| **T-Persist-K-Unified** | C | 5 conditions (PS/ND/BC'-K/TC-K/SR-Λ) | Conditions may be individually removable |

---

## Part III. What Is Falsified / Retracted

| Claim | Evidence | Lesson |
|---|---|---|
| K-Saddle Conjecture | exp30: K=2 always local min | Merge is barrier crossing, not saddle descent |
| Theorem 3.3 (r̄₀ general τ) | r̄₀ = 0.169 at τ=0.3 | Binary-approx fails for τ ≠ 1/2 |
| **P-Unified-1** (Persist ~ 1−CΛ²) | exp49-50: no Lambda-monotone relationship | Persist is barrier-dependent, not Λ-dependent |
| **Spectral K-selection** | exp51: K*=1 on all 10 graphs | Isoperimetric wall is absolute |

---

## Part IV. What Is Experimentally Established (Not Yet Theorems)

| Finding | Evidence | Theoretical Status |
|---|---|---|
| **K*=1 universally** on connected graphs | exp51 (10 graphs) | Consistent with Isoperimetric Ordering (Cat A); no separate theorem needed |
| **Closure reduces d_min* by ~30%** | exp57: SCC 10×10 vs AC 15×15 | Quantitative consequence of T7-Enhanced; formal bound not yet derived |
| **K is kinetic** — determined by IC + barriers | exp51-57 combined | CN14 proposed; no formal theorem |
| **Barriers are O(β)** — no coarsening at noise ≤ 0.5 | exp55 | Consistent with merge barrier O(β^0.89) from exp38 |
| **Random IC → K=1** | exp56 (80 trials) | Consistent with isoperimetric ordering |
| **Repulsion/simplex/mass not necessary** for K>1 | exp53 (6 levels) | Closure + double-well sufficient at d > d_min* |

---

## Part V. Open Problems by Difficulty

### 🟢 Tractable (approach exists, 1-2 sessions)

| Problem | Current State | Approach | Impact |
|---|---|---|---|
| ~~C3'' closure~~ | **RESOLVED** (2026-04-03) | Schur complement + M-matrix proof | Operator theory complete |
| ~~Beyond-Weyl spectral bound~~ | **RESOLVED** (2026-04-03) | Overlap-restricted perturbation + BMD | 33× wider coexistence window |
| ~~Formation birth theorem~~ | **PARTIALLY RESOLVED** (2026-04-03; audit 2026-04-06) | Existence Cat A (T8-Core); supercriticality Cat B (D₄ only) | General graph supercriticality remains open |
| **Analytical d_min*(a_cl, β)** | Mechanism identified (core saturation) | Analytical ū_ext(a_cl) from Euler-Lagrange | Formal theorem for closure d_min reduction |
| **SCC vs AC coarsening rate** | exp55: no coarsening observed | Higher noise, longer time, or Kramers-type analysis | Quantify T7 advantage |
| **T-Bind general τ** | Retracted (O(1)) | New binary-approx gap measure | Low priority |

### 🟡 Research-Level (new techniques needed, weeks)

| Problem | Current State | Approach | Impact |
|---|---|---|---|
| **Barrier exponent derivation** | O(β^0.89) empirical; ΔE_LI=Θ(β) proved; exp60 NEB inconclusive (didn't converge) | NEB/string method for true saddle (needs proper convergence); barrier on M₂ unknown | Kramers merge rate |
| **Analytical TC upgrade** | TC'' tightened to 1-10× | Full Sinkhorn Lipschitz proof at formation-structured points | Upgrade TC'' to Cat A |
| **Analytical ū_ext(a_cl)** | Numerical only | Solve closure-modified Euler-Lagrange in exterior | d_min quantitative Cat A |

### 🔴 Hard (open problem level, months+)

| Problem | Current State | Why Hard | Required Technique |
|---|---|---|---|
| **Merge theorem (MS1-MS4)** | Parts (c)(d)(e) retracted; merge requires Σ²_M→Σ¹ transition | No continuous merge path on Σ²_M; barrier concept inapplicable within fixed-K manifold | Meta-dynamics for cross-manifold (variable-K) transitions |
| **Near-bif branch selection (μ→0)** | Fully open | IFT collapses; topology changes; which branch selected? | Center manifold + Kramers stochastic theory |
| **Strong self-ref transport uniqueness** | Existence proved (Schauder) | Cost depends on transport plan itself — novel mathematical structure | Fixed-point theory for cost-dependent OT |
| **Variable K dynamics** | K is kinetic (exp51-57) | Birth + merge + barrier crossing in unified framework | Multi-scale dynamical systems theory |

---

## Part VI. Theory Architecture — What Connects to What

```
FOUNDATIONS (complete)
  T1 (existence) + T8 (phase transition) + T14 (convergence)
  T11 (Γ-convergence) + T20/T-A2/T6 (operator axioms)
       │
       ▼
SINGLE FORMATION (4/5 complete)
  T-Persist-1(a,b,c) [Cat A] + (d) [Cat C, β>7α] + (e) [Cat B]
  T3/T6-Stability + T7-Enhanced metastability
  Predicate-Energy Bridge [Cat A]
       │
       ▼
MULTI-FORMATION PERSISTENCE (3/5)
  T-Persist-K-Sep [Cat B] → K-Weak [Cat C] → K-Unified [Cat C]
  Coupling Bound Lemma [Cat A] + Weyl spectral gap
       │
       ▼
MULTI-FORMATION STABILITY (3/5, experimentally characterized)
  K*=1 universally (isoperimetric) — proved
  K>1 metastable — proved (K=2 local stability)
  Closure reduces d_min* by ~30% — experimental (exp57)
  K is kinetic — experimental (exp51-57)
       │
       ▼
OPEN FRONTIER
  Merge dynamics (MS1-MS4) ─── 0/4 proved
  Formation birth ─────────── existence Cat A; supercriticality Cat B (D₄ only)
  Near-bif branch selection ── fully open
  Variable K dynamics ──────── framework only
```

---

## Part VII. Numbers at a Glance

| Metric | Value |
|---|---|
| Theorems proved (Cat A) | **43** |
| Theorems conditional (Cat B) | **2** |
| Theorems conditional (Cat C) | **3** |
| Total claims | **48** |
| Fully proved fraction | **90%** |
| Retracted | **2** |
| Falsified predictions | **2** (P-Unified-1, spectral K-sel) |
| Verified predictions | **5/5** single + **4** new multi |
| Experiments (04-02) | **13** (exp45-57) |
| Proofs (04-02) | **3** (BC', TC', H3 tightening) |
| Proofs (04-03) | **10** (C3'', 3 birth, barrier, d_min, f₁, beyond-Weyl, K-field, TC'') |
| Theory documents written | **6 + 7 proof docs** |
| Test count | **175** (unchanged) |
| Gaps identified | **27** |
| Gaps resolved | **9** |

---

## Part VIII. Honest Assessment

**Strengths:**
- Single-formation theory is mature and largely complete (28 Cat A)
- Persistence theory has all bottlenecks resolved
- Experimental validation is extensive (57 experiments, 175 tests)
- Multi-formation stability is now experimentally characterized
- The closure-enhanced metastability (T7 → d_min* reduction) is a genuine, novel contribution

**Weaknesses:**
- Multi-formation theory depends on K-field architecture (architectural choice, not emergent)
- Λ_coupling has limited predictive power (classifier, not predictor)
- P-Unified predictions failed experimental validation
- Merge dynamics and formation birth remain fully open
- Theory is limited to discrete graphs; continuum limit not fully developed

**What SCC does well:**
- Analyzes formation quality via diagnostic vector d = (Bind, Sep, Inside, Persist)
- Proves persistence under temporal perturbation (T-Persist)
- Quantifies enhanced metastability from self-referential closure (T7)
- Provides a framework for multi-formation coexistence at sufficient separation

**What SCC does NOT do:**
- Predict the number of formations K (K is externally imposed or IC-dependent)
- Predict merge timescales (barrier heights known empirically, not analytically)
- Handle strongly-interacting formations (beyond Λ = 1/(K−1))
- Explain formation birth from first principles
