# Multi-Formation Theory Reassessment

**Date:** 2026-04-02
**Category:** theory / synthesis
**Status:** active — replaces previous multi-formation framework
**Depends on:** exp51 (K*=1 universally), CN6 resolution, Isoperimetric Ordering (Cat A), T7-Enhanced (Cat A), all persistence results

---

## 1. The Paradigm Shift

### 1.1. What We Believed

Multi-formation theory was framed as a **thermodynamic** question:
- "What K minimizes the total energy?"
- Λ_coupling parametrizes the coupling strength
- Regime classification (Sep/Weak/Strong) determines persistence behavior
- Spectral structure predicts optimal K

### 1.2. What We Now Know

**exp51 (10 graph configurations):** K* = 1 universally. On every connected graph — homogeneous grids, barbells with near-zero bridge weight, stochastic block models with clear community structure, random geometric graphs — a single merged formation has strictly lower energy than any K > 1 configuration.

**The isoperimetric wall is absolute.** The boundary cost K^{1/d} scaling cannot be overcome by any topological structure on connected graphs. A single formation always "flows" to fill the optimal shape.

**Conclusion:** Multi-formation is NOT a thermodynamic phenomenon. It is a **kinetic** phenomenon.

### 1.3. The New Framework

Multi-formation theory should be reframed as **metastability theory**:

| Old framing | New framing |
|---|---|
| K is determined by energy minimization | K is determined by initial conditions + dynamics |
| Regime classification (Sep/Weak/Strong) | Barrier classification (how hard to merge) |
| Λ_coupling predicts persist degradation | Barrier height predicts merge timescale |
| Spectral K-selection | Spectral nucleation prediction |
| "How many formations are optimal?" | "How long do K formations survive?" |

---

## 2. What's Proved (Unchanged)

The following results remain valid and important:

| Result | Status | Interpretation in new framework |
|---|---|---|
| K=2 is always local min | Cat A | K>1 formations are metastable, never unstable |
| E(u*_{2m}) < 2E(u*_m) | Cat A | Single formation is always global min (isoperimetric) |
| Merge barrier ~ O(β^{0.89}) | Experimental | Barriers grow with phase separation strength |
| T7-Enhanced metastability | Cat A | SCC barriers > Allen-Cahn barriers (self-referential boost) |
| T-Persist-K-Sep | Cat B | Well-separated formations persist under gentle perturbation |
| T-Persist-K-Weak | Cat C | Weakly-interacting formations persist |
| Coupling Bound Lemma | Cat A | Inter-formation coupling is global but gradient effect is local |
| Spectral-repulsion (SR) | Cat A | Joint spectral gap positive when min μ_k > (K-1)λ_rep |

---

## 3. The Three Pillars of Kinetic Multi-Formation Theory

### Pillar I: Nucleation — Where Do Formations Appear?

**Question:** Given a noisy/random initial field, where do formations nucleate?

**Answer (from spectral theory):** Formations nucleate at locations determined by the dominant eigenvectors of the graph Laplacian. The eigengap identifies natural "basins" in the graph topology.

**Evidence:**
- SBM with 3 communities: K_eigengap = 3 (correct community identification)
- Grid graphs: K_eigengap = 1 (uniform → single formation)
- Barbell: K_eigengap = 2 for low bridge weight

**What's needed:**
- Experiment: random initialization → gradient flow → count formations at convergence
- Theory: connect Fiedler vector level sets to nucleation sites
- Prediction: K_nucleation = K_eigengap for most graph structures

### Pillar II: Metastability — How Long Do They Survive?

**Question:** Given K > 1 formations, what is the timescale before they merge to K-1?

**Answer (from barrier theory):**
- Merge requires crossing an energy barrier ΔE_barrier
- ΔE_barrier ~ O(β^{0.89}) (exp38, on grids)
- SCC enhanced metastability (T7): SCC barrier > Allen-Cahn barrier by factor (1 + Gram boost)
- Kramers-type escape rate: τ_merge ~ exp(ΔE_barrier / kT) in a stochastic setting

**What's proved:**
- K=2 local stability: merge-direction curvature μ₁ + μ₂ > 0 (Cat A)
- Barrier existence: local min → barrier exists (topological necessity)
- Enhanced curvature: Hessian boost from closure Gram matrix (T7-Enhanced, Cat A)

**What's needed:**
- Analytical barrier height formula (not just O(β^{0.89}) exponent)
- SCC vs Allen-Cahn barrier ratio (quantify the "enhancement factor")
- Coarsening experiment: start with K=4, observe merge events over time
- Connection to Kramers theory for stochastic transition rates

### Pillar III: Coarsening — What's the Long-Term Dynamics?

**Question:** Starting from K_initial formations, how does K(t) evolve over time?

**Classical answer (Allen-Cahn/Lifshitz-Slyozov):**
- Coarsening law: characteristic domain size L(t) ~ t^{1/2} (curvature-driven)
- K(t) ~ K_0 / (1 + t/τ) for uniform coarsening
- Smaller domains shrink, larger domains grow (Ostwald ripening)

**SCC prediction (conjectured):**
- Coarsening is SLOWER due to enhanced metastability (T7)
- The closure self-referential structure creates "self-supporting" formations that resist dissolution
- Predicted: L(t) ~ t^α with α < 1/2 (sub-diffusive coarsening)
- Or: exponentially long metastable plateaus between merge events

**What's needed:**
- Long-time gradient flow simulation: K_initial = 4..8, track K(t)
- Measure coarsening exponent α and compare with Allen-Cahn (α = 1/2)
- Theory: derive coarsening law from barrier heights + landscape structure

---

## 4. Revised Open Problem List

### Tractable (this week)

| Problem | Approach | Difficulty |
|---|---|---|
| **Nucleation from random IC** | exp52: random init → gradient flow → count K(converged) on SBM/barbell | 2/5 |
| **SCC vs AC coarsening** | exp53: K=4 init → long gradient flow → measure K(t) for SCC and pure Allen-Cahn | 3/5 |
| **Barrier height formula** | Analytical: saddle point between K=2 → K=1 via NEB-like interpolation | 3/5 |

### Medium-term

| Problem | Approach | Difficulty |
|---|---|---|
| Enhanced metastability ratio | Compare SCC and AC Hessian eigenvalues at K=2 saddle | 3/5 |
| Kramers rate for stochastic merge | Derive τ_merge from barrier height + prefactor | 4/5 |
| Coarsening exponent derivation | From Kramers rates + landscape statistics | 4/5 |

### Hard (open problem level)

| Problem | Approach | Difficulty |
|---|---|---|
| Formation birth theorem | Quantitative nucleation theory: when does K → K+1? | 4/5 |
| Merge dynamics (MS1-MS4) | Morse theory on Σ^K_M: transition state characterization | 5/5 |
| Near-bif branch selection | Center manifold + stochastic bifurcation (Kramers theory) | 5/5 |

---

## 5. What Changes in Canonical Spec v2.1

### §12 Open Problems: Multi-Formation Architecture

The binding decision (I9, K-field) remains correct but its interpretation changes:

**Before:** "K is an external parameter; the theory seeks the optimal K."

**After:** "K is kinetically determined. The K-field architecture models metastable multi-formation states. The optimal K is always 1 on connected graphs (isoperimetric ordering), but K > 1 formations are metastable with enhanced barriers (T7). The theory's predictions concern persistence timescales, not equilibrium K values."

### §12 Open Problems: K Must Be Emergent (CN6)

**Resolved.** K emerges from:
1. Graph spectral structure (eigengap → nucleation sites)
2. Initial conditions (noisy initialization → K_initial ≈ K_eigengap)  
3. Barrier heights (T7-enhanced metastability → slow coarsening)
4. Time (K(t) decreases monotonically toward K=1)

### New Commitment Note: CN14 (proposed)

**CN14. K Is Kinetic, Not Thermodynamic.** The number of coexisting formations K is not determined by energy minimization (K=1 is always globally optimal on connected graphs). K is a kinetic quantity determined by initial conditions and barrier heights. The theory's multi-formation predictions concern the timescale and mechanism of formation merge/death, not the equilibrium number of formations. This is analogous to the distinction between the equilibrium crystal structure (single crystal) and the kinetically determined polycrystalline microstructure in materials science.

---

## 6. Λ_coupling Reassessment

The Λ_coupling parametrization from the unified regime theory remains **descriptively useful** for classifying the interaction strength between formations. But its **predictive role** changes:

**Before:** Λ predicts persist degradation (P-Unified-1: Persist ~ 1 - C·Λ²)
**After:** Λ describes the interaction regime but does NOT predict persist degradation (exp49-50 falsified P-Unified-1)

**What Λ_coupling IS good for:**
- Classifying interaction regime (100% geometric-Lambda agreement, exp46-47)
- Upper bound on coupling effect: spectral gap μ_joint ≥ μ_min - (K-1)λ_rep (Weyl)
- Identifying the merge bifurcation threshold Λ = 1/(K-1)

**What Λ_coupling is NOT good for:**
- Predicting persist degradation (no monotone relationship observed)
- Determining optimal K (K=1 always optimal)
- Quantifying coarsening timescale (barrier height is the relevant quantity)

**Revised role:** Λ_coupling is a **structural classifier**, not a **dynamical predictor**. The dynamical prediction requires barrier heights, which depend on the full energy landscape, not just the linear coupling measure.

---

## 7. P-Unified Predictions: Revised Status

| Prediction | Original | Status | Revised |
|---|---|---|---|
| P-Unified-1 | Persist ~ 1 - C·Λ² | **FALSIFIED** (exp49-50) | Persist is barrier-dependent, not Λ-dependent |
| P-Unified-2 | δ_min ∝ Λ | **INCONCLUSIVE** | Depth is formation-quality-dependent |
| P-Unified-3 | Bifurcation at Λ = 1/(K-1) | **PARTIALLY VERIFIED** (exp37,44) | Merge threshold exists but Λ is not the right coordinate |

**New predictions (from kinetic framework):**

| ID | Prediction | Testable? |
|---|---|---|
| MK-1 | K_nucleation from random IC = K_eigengap | Yes (exp52) |
| MK-2 | SCC coarsening exponent α < 1/2 (slower than AC) | Yes (exp53) |
| MK-3 | Merge barrier ΔE ∝ β^γ with γ ≈ 0.89 (from exp38) | Partially |
| MK-4 | Enhanced metastability factor = 1 + (Gram boost) / (AC curvature) | Yes |

---

## 8. Summary: The Multi-Formation Picture

```
                    MULTI-FORMATION IN SCC
                    ━━━━━━━━━━━━━━━━━━━━━

    Thermodynamic layer:         Kinetic layer:
    ┌─────────────────┐         ┌─────────────────────────┐
    │ K=1 is always    │         │ K>1 via nucleation      │
    │ global minimum   │         │ (spectral → IC → K_init)│
    │ (isoperimetric)  │         │                         │
    │                  │         │ Metastable persistence  │
    │ PROVED (Cat A)   │         │ (T-Persist, barriers)   │
    └─────────────────┘         │                         │
                                │ Slow coarsening         │
                                │ (T7 enhanced barriers)  │
                                │                         │
                                │ K(t) → 1 eventually     │
                                │ (thermodynamic limit)   │
                                └─────────────────────────┘

    WHAT WE KNOW:                WHAT WE NEED:
    ✅ K=1 optimal               ❓ Nucleation → K_init
    ✅ K>1 metastable            ❓ Barrier heights
    ✅ Barriers exist            ❓ Coarsening timescale
    ✅ Enhanced vs AC            ❓ SCC coarsening exponent
    ✅ Persistence (Sep/Weak)    ❓ Merge dynamics
```

The multi-formation theory shifts from **"what K is optimal"** to **"how does K evolve"** — from equilibrium to dynamics, from thermodynamics to kinetics.

---

## 9. Constraint Relaxation Experiment (exp53)

### 9.1. Setup
Progressive removal of constraints on 10×10 grid, K=4 initial formations:

| Level | Mass | Repulsion | Simplex | Description |
|---|---|---|---|---|
| L0 | Fixed per-formation | λ_rep=5 | λ_bar=50 | Standard SCC |
| L1 | Shared total | λ_rep=5 | λ_bar=50 | Mass transfer allowed |
| L2 | Shared total | λ_rep=1 | λ_bar=50 | Weak repulsion |
| L3 | Shared total | λ_rep=0 | λ_bar=50 | No repulsion |
| L4 | Shared total | λ_rep=0 | λ_bar=0 | No repulsion, no simplex |
| L5 | Free (no constraint) | λ_rep=0 | λ_bar=0 | Fully unconstrained |

### 9.2. Results

| Level | K_final | Mass redistribution (CV) | Key observation |
|---|---|---|---|
| L0 | **4** | 0.000 | All survive, equal mass (baseline) |
| L1 | **0** | 0.000 | ALL DIE — repulsion + shared mass flattens all peaks below 0.5 |
| L2 | **4** | 0.000 | Recover after transient death — weak repulsion allows re-formation |
| L3 | **4** | 0.000 | Recover — simplex alone maintains separation |
| L4 | **4** | 0.095 | Survive + mild redistribution (22-28 range) |
| L5 | **4** | 0.092 | Survive + mass expansion (25→55) — formations grow but don't merge |

### 9.3. Key Findings

**Finding 1: Self-referential closure is the primary stabilizing mechanism.**
At L4-L5 (no repulsion, no simplex, free mass), all 4 formations survive 3000 iterations. The only thing holding them together is the closure self-energy E_cl = ||u - Cl(u)||² and the double-well E_bd. Closure creates self-supporting formations that are independently metastable.

**Finding 2: Strong repulsion + mass sharing is DESTABILIZING (L1).**
Counterintuitively, strong repulsion with shared mass is the MOST destructive combination. Repulsion pushes formations apart but the shared mass constraint redistributes mass uniformly, flattening all peaks. This creates a uniform field with no structure — the worst outcome.

**Finding 3: Mass redistribution is weak even without constraints.**
At L4 (shared mass, no other constraints), the coefficient of variation is only 0.095 (masses 22-28 from initial 25). No Ostwald ripening observed in 3000 iterations. The barriers between formations prevent significant mass transfer.

**Finding 4: On SBM graphs, formations are even MORE stable.**
L5 on SBM 3×20: CV=0.004, essentially perfect equal mass. The community structure creates natural "niches" that stabilize formations independently of constraints.

### 9.4. Theoretical Implications

1. **Closure is the load-bearing wall.** Remove repulsion, simplex, and volume constraint — formations survive. Remove closure — they collapse (trivially: E_cl=0 removes the self-referential binding force).

2. **Repulsion is NOT necessary for multi-formation.** It helps with spatial separation but is not required for formation survival. Formations self-separate through the closure operator's self-completion.

3. **The real coarsening mechanism is NOT gradient descent.** Gradient descent preserves K because each formation is a local minimum. Coarsening requires **stochastic perturbation** (noise) to escape local minima — barrier crossing.

4. **SCC > Allen-Cahn for multi-formation stability.** In Allen-Cahn, the only stabilizing mechanism is the double-well. In SCC, closure adds a self-referential stabilizer. This is the enhanced metastability (T7) applied to multi-formation.

### 9.5. Revised CN14 (Updated after exp54-56)

~~**CN14 (original). Self-Referential Closure Is the Primary Multi-Formation Stabilizer.**~~ — **REVISED** based on exp54.

**CN14 (revised). Double-Well Phase Separation Is the Primary Multi-Formation Stabilizer; Closure Enhances Formation Quality.**

exp54 shows: at a_cl=0 (no closure at all), K=4 formations still survive with peaks 0.85. Closure improves peaks to 1.00 but is NOT necessary for metastability. The load-bearing mechanism is the **double-well potential** E_bd = α·smoothness + β·W(u), which creates phase-separated domains that are local energy minima.

**The role hierarchy:**
1. **Double-well (E_bd)** — creates phase separation → metastable domains → NECESSARY
2. **Closure (E_cl)** — enhances formation quality (peaks, sharpness) → NOT necessary for existence, but improves it
3. **Repulsion** — spatial separation → NOT necessary
4. **Simplex** — overlap prevention → NOT necessary
5. **Volume constraint** — mass conservation → NOT necessary for metastability

exp55 confirms: barriers are extremely high — noise up to 0.5 fails to cause any merge in 5000 iterations, for BOTH SCC and Allen-Cahn.

exp56 confirms: random IC → gradient flow → K=1 (single formation) in almost all cases. Multi-formation requires structured initialization.

---

## 11. Thorough Closure Investigation (exp57)

### 11.1. Methodological Fix

exp54 had a hidden bias: `g - mean(g)` gradient projection implicitly conserved per-formation mass, preventing genuine mass transfer. exp57 fixes this with:
- **Mode A:** Raw gradient (no projection, no mass conservation)
- **Mode B:** Single field with K initial bumps (most honest test)

### 11.2. Definitive Results

| Mode | Closure (a_cl=3.0) | No closure (a_cl=0.0) | Meaning |
|---|---|---|---|
| A: K independent fields | K=4 survives | K=4 survives | Independent optimization; no coupling |
| **B: Single field, K bumps** | **K=1 (merge)** | **K=1 (merge)** | **Always merge regardless of closure** |

### 11.3. The Definitive Answer

**On a single field, multiple formations ALWAYS merge to K=1 under gradient flow, regardless of closure.** This is true on all tested grids (8×8, 10×10, 15×15) and all closure strengths (a_cl = 0 to 3.0).

**The K-field architecture is what enables multi-formation, not closure.** By giving each formation its own field u^k, the K-field architecture artificially prevents mass transfer between formations. This is the binding decision I9 — it's not a mathematical consequence of the theory but an architectural choice.

### 11.4. Revised Understanding

```
Multi-formation stability hierarchy:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. K-FIELD ARCHITECTURE (I9) — NECESSARY for K > 1
   Without separate fields, formations merge to K=1 (isoperimetric)

2. PHASE SEPARATION (double-well) — NECESSARY for formation existence
   Without E_bd, no coherent structure at all

3. VOLUME CONSTRAINT — HELPFUL for mass balance
   Without it, mass grows unboundedly but formations survive

4. CLOSURE (E_cl) — QUALITY ENHANCER only
   Improves peaks (0.85 → 1.00) but does not determine K
   Does NOT prevent merge in single-field mode

5. REPULSION — SPATIAL SEPARATOR only
   Helps spatial arrangement but not required for existence
```

### 11.5. Implications for the Theory

1. **CN6 (K must be emergent):** K is determined by the K-field architecture (how many fields are initialized), not by any intrinsic property of the energy landscape on a single field. On a single field, K*=1 always.

2. **The K-field architecture is a modeling choice, not a consequence.** SCC does not explain WHERE K comes from — it provides a framework for analyzing K-formation dynamics GIVEN K.

3. **Closure's role is narrower than previously thought.** It enhances formation quality (T7-Enhanced, BC' basin improvement) but does not create or maintain multi-formation structure.

4. **This is honest and important.** Acknowledging that K is architecturally imposed (not emergent) is more scientifically honest than claiming spectral or energetic K-selection. The theory's strength is in analyzing GIVEN formations, not predicting their count.

---

## 12. Correction: Single-Field Multi-Formation IS Possible (well-separated bumps)

### 12.1. The Methodological Error in exp57 Mode B

exp57 Mode B initialized K=4 bumps that **overlapped heavily** on small grids (width ~ side/K, bumps touching). This forced merge. The correct test: **well-separated narrow bumps** (width=2, centers at grid quadrants).

### 12.2. Definitive Result: Closure Lowers the Multi-Formation Threshold

| Grid | SCC (a_cl=3.0) | Allen-Cahn (a_cl=0.0) |
|---|---|---|
| 8×8 | K=1 (grid too small) | K=1 |
| **10×10** | **K=4 ✅** | **K=1 ❌ (merge)** |
| **12×12** | **K=4 ✅** | **K=3 (partial merge)** |
| 15×15 | K=4 ✅ | K=4 ✅ |
| 20×20 | K=4 ✅ | K=4 ✅ |
| 25×25 | K=4 ✅ | K=4 ✅ |

### 12.3. The Real Role of Closure

**Closure does NOT determine whether multi-formation is possible.** On sufficiently large grids (15×15+), both SCC and Allen-Cahn maintain K=4.

**Closure DOES expand the stability region.** It lowers the minimum grid size (equivalently, minimum inter-formation distance) needed for K>1 stability:
- Allen-Cahn: needs ~15×15 (formations ~7 nodes apart)
- SCC: needs ~10×10 (formations ~5 nodes apart)

**This is the multi-formation manifestation of T7-Enhanced metastability:** closure's self-referential structure creates larger basins of attraction, allowing formations to coexist at closer distances.

### 12.4. Revised CN14 (Final)

**CN14. Closure Expands Multi-Formation Stability.** On a single soft field, K > 1 well-separated formations are metastable local minima when the inter-formation distance exceeds a critical threshold d_min*. The self-referential closure operator reduces d_min* compared to pure Allen-Cahn (phase separation alone), extending multi-formation stability to smaller domains. Specifically:
- Without closure (Allen-Cahn): d_min* ≈ 7 on 2D grids (β=30)
- With closure (SCC, a_cl=3.0): d_min* ≈ 5 on 2D grids (β=30)
This is the multi-formation realization of the enhanced metastability theorem (T7).

### 12.5. Revised Stability Hierarchy (Final)

```
Multi-formation stability:
━━━━━━━━━━━━━━━━━━━━━━━━━

NECESSARY:
  1. Phase separation (double-well, E_bd) — creates formations
  2. Sufficient spatial separation (d > d_min*) — prevents merge

ENHANCING:
  3. Closure (E_cl) — reduces d_min* by ~30% (T7 applied to multi-formation)
  4. K-field architecture — guarantees separation by construction
  5. Repulsion — enforces spatial separation actively
  6. Volume constraint — prevents mass drain

NOT NECESSARY:
  - Simplex barrier (formations naturally don't overlap if separated)
  - Fixed per-formation mass (shared mass works if separated)
```

**Revised closure role:** Closure is not the load-bearing wall but the **quality amplifier**. It makes formations more cohesive (higher peaks, sharper boundaries, stronger self-referential identity), which in turn enhances metastability (T7-Enhanced). But the fundamental multi-formation metastability comes from phase separation itself.

---

## 10. Experiment 54-56 Results

### exp54: Closure Strength Sweep (a_cl = 3.5 → 0)

| a_cl | K_final | Peak range | Formation quality |
|---|---|---|---|
| 3.5 | 4 | 0.98-1.00 | Excellent |
| 3.0 | 4 | 0.97-1.00 | Excellent |
| 2.0 | 4 | 0.95-0.97 | Good |
| 1.0 | 4 | 0.92-0.93 | Moderate |
| 0.0 | 4 | 0.85-0.86 | Weak but alive |

**No critical threshold.** Closure removal degrades quality smoothly but never kills formations.

### exp55: Stochastic Coarsening

| Noise | SCC K_final | AC K_final | Any merge? |
|---|---|---|---|
| 0.01 | 4 | 4 | No |
| 0.05 | 4 | 4 | No |
| 0.10 | 4 | 4 | No |
| 0.20 | 4 | 4 | No |
| 0.50 | 4 | 4 | No |

**No coarsening at any noise level.** Barriers are O(β) ~ 20, far above noise scale.

### exp56: Nucleation from Random IC

| Graph | K_eigengap | K_nucleated (mode) |
|---|---|---|
| grid 10×10 | 8 | 1 |
| grid 15×15 | 8 | 2 |
| SBM 3×20 | 3 | 1 |
| SBM 4×15 | 4 | 1 |

**Almost always K=1.** Gradient flow from random IC converges to single formation. Eigengap prediction is uncorrelated with nucleated K.
