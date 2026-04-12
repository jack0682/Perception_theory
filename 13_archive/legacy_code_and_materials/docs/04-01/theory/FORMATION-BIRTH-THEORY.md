# Formation Birth Theory

**Date:** 2026-04-01
**Session:** Phase 7 — formation birth mechanisms, topological splitting, parametric nucleation
**Category:** theory
**Status:** complete
**Depends on:** experiments/results/exp39_formation_birth.json, experiments/results/exp37_bifurcation_crossing.json, docs/03-31/theory/NEAR-BIFURCATION-LOCAL-THEORY.md, Canonical Spec v2.0.md

---

## 1. Definition of Formation Birth

**Formation birth** is the event where the number of distinct formations increases across a temporal or parametric transition:

> K_t < K_s: the system at time s supports more formations than at time t.

Two sub-types:

1. **Nucleation** (0 → 1): The uniform (formationless) state gives way to a structured minimizer. This is a symmetry-breaking event tied to the pitchfork bifurcation at β_crit.

2. **Splitting** (K → K+1): An existing formation's core becomes disconnected, producing two or more spatially separated sub-formations within what may remain a single energy minimum.

Formation birth is the temporal reverse of formation death (merging/dissolution). It violates the K_t = K_s assumption underlying T-Persist.

---

## 2. Three Birth Mechanisms

### Mechanism A: Parametric Nucleation (β Increase)

The classical symmetry-breaking birth. On a connected graph G with n nodes, the uniform field u₀ = c·**1** (with c = m/n) is a critical point of E on Σ_m. The Hessian at u₀ has eigenvalues controlled by the competition between the double-well potential (β) and the boundary smoothing (α).

**Proposition (Parametric Birth — T8-Core).**
The uniform field u₀ undergoes a supercritical pitchfork bifurcation at

    β_crit = 4λ₂(L) · α / |W''(c)|

where λ₂(L) is the Fiedler eigenvalue and W''(c) = 2(1 - 6c + 6c²) is the double-well curvature at the uniform concentration. For β < β_crit, u₀ is a local minimizer (no formation). For β > β_crit, u₀ becomes unstable and two formation-structured branches emerge in the ±Fiedler direction.

**Experimental evidence (exp37):**
- Grid: 12×12 (n=144), volume fraction 0.3
- Empirical β_crit = 5.0
- Two distinct branches at β=7: correlation = −0.50, COM distance = 7.61 (opposite corners)
- Energy degenerate: E_+ = E_- = 2.865 (pitchfork symmetry)
- No hysteresis: forward and backward β_crit coincide (gap = 0.0)
- Verdict: **continuous supercritical pitchfork**, consistent with T8-Core

**Branch selection:**
At the pitchfork, the Fiedler eigenvector determines the spatial template. Any infinitesimal perturbation aligned with ±v₂ selects one of the two branches. On finite graphs, numerical noise or spatial inhomogeneity acts as the selection mechanism. This is not a deficiency — it reflects the genuine Z₂ symmetry breaking inherent in the double-well potential on symmetric graphs.

### Mechanism B: Topological Splitting

A qualitatively different birth mechanism where the graph structure — not the energy parameters — drives the transition. When a bottleneck develops within the formation core, the core disconnects into spatially separated components while the energy minimum remains K=1.

**Key distinction:** This is NOT an energetic phase transition. The optimizer returns K=1, but the formation's core topology has changed.

**Proposition (Topological Birth Criterion).**
Let u* be a K=1 formation on graph G with core Core(θ) = {x : u*(x) ≥ θ}. Let G_Core = G[Core(θ)] be the subgraph induced on the core. If the algebraic connectivity (Fiedler eigenvalue) of G_Core satisfies

    λ₂(G_Core) < ε_split

then Core(θ) decomposes into 2+ connected components: Core = C₁ ∪ C₂ ∪ ... with C_i connected and d_G(C_i, C_j) ≥ 1 for all i ≠ j.

**Experimental evidence (exp39, Scenario 3 — crack):**
The crack scenario weakens a column of edges in a 15×15 grid by reducing their weight. Results:

| Crack weight | Fiedler(G) | K1 components | K1 core size | K=1 preferred? |
|:-------------|:-----------|:--------------|:-------------|:---------------|
| 1.0 (none)   | 0.0437     | 1             | 68           | Yes (ΔE=−8.3)  |
| 0.5          | 0.0385     | 1             | 70           | Yes (ΔE=−8.7)  |
| 0.2          | 0.0277     | **2**         | 69           | Yes (ΔE=−8.2)  |
| 0.1          | 0.0186     | 1             | 68           | Yes (ΔE=−14.0) |
| 0.05         | 0.0110     | 1             | 68           | Yes (ΔE=−8.0)  |
| 0.02         | 0.0049     | **2**         | 67           | Yes (ΔE=−7.3)  |
| 0.01         | 0.0026     | **2**         | 67           | Yes (ΔE=−7.5)  |
| 0.005        | 0.0013     | **2**         | 67           | Yes (ΔE=−5.9)  |
| 0.002        | 0.0005     | **2**         | 67           | Yes (ΔE=−6.6)  |
| 0.001        | 0.0003     | **2**         | 67           | Yes (ΔE=−8.3)  |

Observations:
- K=1 is **always** energetically preferred (ΔE strongly negative throughout)
- Core disconnection appears at crack_weight ≤ 0.2, with consistent 2-component structure for crack_weight ≤ 0.02
- The Fiedler eigenvalue of the full graph drops monotonically with crack weight
- The anomaly at crack_weight = 0.1 (1 component) likely reflects optimizer sensitivity — the core just barely avoids spanning the crack

**Interpretation:** Topological birth is a "hidden" birth. The energy landscape has a single K=1 minimum, but the formation's internal structure has bifurcated. This is invisible to the K-field framework (which counts energy minima) but visible to core connectivity analysis.

### Mechanism C: Volume-Driven Splitting (Not Observed)

**Hypothesis:** Increasing volume fraction forces the formation to elongate, eventually pinching off into two.

**Experimental evidence (exp39, Scenario 1):**
Volume fraction swept from 0.25 to 0.75 on a 15×15 homogeneous grid with β=50:

- K=1 preferred at **every** volume fraction
- **All** K=1 formations had exactly 1 connected core component
- Aspect ratio peaked at 2.33 (vf=0.3) then dropped to 1.0 (vf≥0.7) — the formation becomes rounder, not more elongated
- Core size grows monotonically (56→176) but stays connected

**Conclusion:** Pure volume increase does NOT cause birth on homogeneous grids. The formation accommodates additional volume by expanding isotropically rather than elongating. Volume-driven splitting may require anisotropic graph structure (elongated domains, preferential connectivity directions).

**Non-evidence (exp39, Scenario 2 — β decrease):**
β swept from 50 down to 5. Formation persists with K=1 and 1 component throughout. The formation weakens (strength drops from 1.0 to 0.96) but does not split. This confirms that β decrease causes dissolution (approaching the bifurcation from above), not splitting.

---

## 3. Formal Propositions

### Proposition 1 (Parametric Birth — restated from T8-Core)

On a connected graph G with n nodes, the uniform field u₀ = (m/n)·**1** undergoes a supercritical pitchfork bifurcation at β_crit = 4αλ₂(L)/|W''(m/n)|. For β > β_crit, the bifurcating branch u*(β) satisfies:

    ‖u*(β) − u₀‖ = O(√(β − β_crit))

with branch direction aligned to the Fiedler eigenvector v₂.

**Status:** Proved (T8-Core, Category A). The supercritical character (no hysteresis) is confirmed by exp37.

### Proposition 2 (Topological Birth Criterion)

Let u* be a formation on G with core Core(θ). Define the core connectivity function:

    κ(θ) = number of connected components of G[Core(θ)]

If the edge weights within the core satisfy w_e < w_crit for all edges e crossing a cut S, then there exists θ* such that κ(θ*) ≥ 2 while u* remains a local minimizer of the K=1 energy.

**Status:** Empirically verified (exp39 scenario 3). Not yet proved — requires analysis of how the optimizer distributes mass across a bottleneck. The key difficulty is characterizing when the core "avoids" vs. "spans" the weak region.

### Proposition 3 (Volume Does Not Cause Birth on Homogeneous Graphs)

On a homogeneous grid graph G with uniform edge weights, increasing the volume fraction m/n does not cause K=1 → K=2 splitting. The K=1 minimizer accommodates additional volume by isotropic expansion.

**Status:** Empirically verified (exp39 scenario 1, 11 volume fractions). Not proved — would require showing that the K=1 minimizer on a symmetric graph inherits the symmetry (up to the single Fiedler-direction break).

---

## 4. Connection to Persistence Theory

### 4.1. Birth as Temporal Reverse of Persistence

Formation birth is the temporal complement of T-Persist. At time t there are K_t formations; at time s > t there are K_s > K_t. The transport kernel M_{t→s} maps K_t source formations to K_s target formations, meaning at least one target formation has no source antecedent (nucleation) or one source maps to two targets (splitting).

### 4.2. T-Persist Assumes No Birth

T-Persist (and T-Persist-K-Sep, T-Persist-K-Weak) assume K_t = K_s. When birth occurs:
- The K-field framework at time s has K_s > K_t fields
- The transport map cannot be one-to-one from targets to sources
- The "inheritance" predicate (core-to-core mass transfer) is undefined for the newborn formation

### 4.3. Three-Tier Persistence and Bifurcation Crossing

The near-bifurcation local theory (NEAR-BIFURCATION-LOCAL-THEORY.md) identifies three regimes:

1. **Away from bifurcation:** Full basin containment; T-Persist holds
2. **Near bifurcation:** Restricted persistence (RP-NB); only deep-core remnant persists
3. **At bifurcation:** No finite basin; birth/death events occur

Birth (Mechanism A) occurs at the transition from regime 3 to regime 1 as β increases. The near-bifurcation regime acts as the "incubation zone" where the formation is emerging but not yet robust.

### 4.4. Topological Birth and Multi-Formation Persistence

Topological birth (Mechanism B) poses a subtler challenge. Since the energy minimum remains K=1, the T-Persist framework sees no transition. However, the formation's internal structure has changed in a way that:
- The Bind diagnostic may decrease (core is less cohesive across the crack)
- The Sep diagnostic is unaffected (still measured against complement)
- A future graph change could promote the hidden birth to an energetic one (K=1 → K=2 becomes preferred)

This suggests a **pre-birth** diagnostic: monitoring λ₂(G_Core) as an early warning for imminent splitting.

---

## 5. Open Questions

1. **Can birth occur on homogeneous graphs without parameter or topology change?** Exp39 says no for volume-driven mechanisms. But other energy term variations (λ_sep, λ_bd) have not been tested.

2. **Role of noise in branch selection at the pitchfork.** The Z₂ symmetry at β_crit means the branch is selected by infinitesimal perturbation. In the temporal transport setting, the transported field from t provides a natural perturbation — does this always select the "correct" branch (closest to the source formation)?

3. **Multi-birth: can K → K+2 or higher occur?** This requires either (a) multiple eigenvalues crossing zero simultaneously (codimension-2 bifurcation, non-generic) or (b) sequential rapid births. On highly symmetric graphs (torus, complete bipartite), simultaneous crossings are possible.

4. **Topological birth threshold.** What is the critical crack weight w_crit at which the core disconnects? The exp39 data shows a non-monotone pattern (2 components at 0.2, 1 at 0.1, 2 again at 0.02), suggesting sensitivity to optimizer initialization. A clean characterization requires understanding the competition between boundary energy (favoring spanning the crack) and separation energy (favoring avoiding it).

5. **Birth-death asymmetry.** Is birth the exact time-reversal of death, or are there asymmetries? The pitchfork is symmetric (no hysteresis), but topological splitting/merging may exhibit hysteresis if the crack weight changes direction.

---

## 6. Summary

| Mechanism | Trigger | Energy transition? | Observed? | Status |
|:----------|:--------|:-------------------|:----------|:-------|
| A: Parametric nucleation | β crosses β_crit | Yes (pitchfork) | exp37 | Proved (T8-Core) |
| B: Topological splitting | Graph bottleneck in core | No (K=1 persists) | exp39-S3 | Empirically verified |
| C: Volume-driven splitting | Volume increase | Would be energetic | exp39-S1: **not observed** | Ruled out on homogeneous grids |

The main theoretical contribution is the distinction between energetic birth (Mechanism A, visible to the K-field framework) and topological birth (Mechanism B, hidden within a single energy minimum). Topological birth requires a new diagnostic — core connectivity — that is not captured by the existing proto-cohesion diagnostic vector d = (Bind, Sep, Inside, Persist).
