---
type: working/afd/v_afd
status: V-AFD Draft v0.1 (2026-05-12)
---

# V-AFD Worked Examples

Eight scenarios from `vector_abstract_formation_dynamics.md` §5, worked out in detail. Each scenario specifies setup, expected vector trajectory `z_γ`, what V-AFD captures, what V-AFD loses, and whether additional coordinates beyond baseline `Z = (D, K_act, E, τ)` are needed.

The canonical reference configuration is **15×15 free-BC grid, β = 50, vol_frac = 0.3** (per `CV114_H_MORSE_PACKAGEII/02_H_MORSE_statement_reconstruction.md` setup). Numerical values are plausibility estimates, not exact.

---

## Scenario 1 — Static single formation

### Setup

- Graph: 15×15 grid, free boundary conditions.
- Parameters: β = 50 (well above β_crit ≈ 4λ_2/|W''(c)|), α = 0.5, λ_cl, λ_sep, λ_bd canonical defaults.
- Initial: random multi-start initialization.
- u*: convergent formation from `find_formation`, single localized blob.
- vol_frac = 0.3 ⇒ m = 0.3 · 225 = 67.5.

### Expected Z

| Coord | Value (estimate) | Justification |
|---|---|---|
| Bind | 0.90–0.95 | High β saturates cohesion within core |
| Sep | 0.85–0.92 | Off-center blob has clear separation from boundary |
| Inside | 0.92–0.97 | Single core with high mass concentration |
| Persist (static) | 1.00 | static placeholder |
| K_act | 1 | single connected component above threshold |
| E | E_F^* ≈ minimum on Σ_m for K=1 | global K=1 minimum (T-Merge(b) Cat A) |
| τ | single H_0 bar (b_1, d_1) with d_1 - b_1 large | one persistent component |

### What V-AFD captures

- Pareto dominance: this state Pareto-dominates any state with strictly smaller diagnostic on any component.
- Vector stability: high `ExitCost` (cost to leave basin), high `Q_w` for any reasonable weight choice, low local sensitivity.
- Single-state baseline: `z_γ(s) ≡ Z_F^*` for the constant path γ(s) = u_F^*.

### What V-AFD loses

- **Spatial location** of the blob. Bind/Sep/Inside/τ are translation-invariant up to Aut(G); two blobs at different corners of the 15×15 grid have the same `Z` but different basin labels.
- **Specific blob shape** beyond persistence-diagram statistics. Two different blob shapes with the same `τ` are indistinguishable.

### Additional coordinates?

For Layer-2 ordering (Pareto, ExitCost-based stability): **no**.
For dynamical specificity (which corner does the blob occupy?): **basin label needed**.
For shape detail (which blob morphology?): **PCA of `u_F^* - \bar u`** or **field fingerprint** needed.

---

## Scenario 2 — Weak formation

### Setup

- Same grid.
- β = 5 (below β_crit; T8-Core gives no formation under canonical conditions, but consider an off-uniform local minimizer near a barrier in E if one exists at small β; alternatively a partially-formed state from a `find_formation` run that did not fully converge).

### Expected Z

| Coord | Value (estimate) | Justification |
|---|---|---|
| Bind | 0.45–0.60 | partial cohesion only |
| Sep | 0.25–0.40 | mass not well-separated from background |
| Inside | 0.30–0.50 | core mass fraction moderate |
| Persist (static) | 1.00 | placeholder |
| K_act | 0 or 1 | depending on threshold θ_in |
| E | close to min E (uniform field nearly minimal at low β) | weak gradient |
| τ | small persistence bars, possibly all near d_i = 0 | weak topology |

### What V-AFD captures

- Pareto-dominated by Scenario 1 on Bind, Sep, Inside. Persist tied (static placeholder).
- Low `Q_w` for any weights.
- Low ExitCost (close to basin boundary, weakly defined basin).

### What V-AFD loses

- **Threshold dependence** of K_act: small variations in θ_in toggle K_act between 0 and 1. V-AFD's K_act coordinate is robust only when the persistence diagram has a clear gap.

### Additional coordinates?

For threshold sensitivity analysis: **persistence-gap statistic** (e.g. ratio of top to second bar persistence) beyond `τ`.

---

## Scenario 3 — Merge K=2 → K=1

### Setup

- Two blobs in K=2 metastable configuration, β slightly above bifurcation threshold (β = 8 say).
- Initial: two-blob configuration u_0 ∈ B_{F_2}.
- Final: single-blob configuration u_1 ∈ B_{F_1}.
- Path γ: continuous interpolation that merges blobs (e.g. shortest path in Σ_m, or NEB-computed minimum-energy path).

### Expected `z_γ`

Plotting each coordinate along s ∈ [0, 1]:

| Coord | s=0 | s=0.4 (pre-merge) | s=0.5 (merge instant) | s=0.6 (post-merge) | s=1 |
|---|---|---|---|---|---|
| Bind | 0.88 | 0.70 (dip) | 0.55 (merge minimum) | 0.75 | 0.92 |
| Sep | 0.85 | 0.50 (decreasing) | 0.05 (separation lost) | 0.10 | 0.88 |
| Inside | 0.85 | 0.70 | 0.60 | 0.80 | 0.95 |
| Persist (static) | 1 | 1 | 1 | 1 | 1 |
| K_act | 2 | 2 | **1** (jump) | 1 | 1 |
| E | E_F_2 | E_F_2 + δ | E_F_2 + Bar | E_F_2 + δ' | E_F_1 < E_F_2 |
| τ | 2 bars | 2 bars (one shortening) | 1 bar (the other dies) | 1 bar | 1 bar |

### What V-AFD captures

- **Energy barrier** `Bar(γ, F_2) = max_s E(γ(s)) - E_{F_2} > 0` (per OP-AFD-004 Cat B: ≥ 0.0221β).
- **K-jump** at s ≈ 0.5: `TV(K_act ∘ γ) = 1` (single merge event).
- **Diagnostic variation** `Var_D(γ) > 0`: Bind and Sep dip and recover; sum of TV gives positive value.
- **Topology variation** `Var_τ(γ) ≈ d_B(τ(γ(0.5^-)), τ(γ(0.5^+)))` includes the death of one bar.
- **Pareto comparison**: F_1 ≼_D F_2 is *false* generically (F_1 may have higher Inside, lower Bind), so they are Pareto-incomparable.

### Compare to AFD-T7 / OP-AFD-004

AFD-T7 Cat B (resolved 2026-05-12): `C_K(K=2, K=1) ≥ 0.0221β`. Setting `λ_E = 1, λ_K = 0` and ignoring D, τ, L:

$$C_V^\mathrm{minimal}(F_2, F_1) = \mathrm{Bar}(F_2, F_1) \geq 0.0221β.$$

V-AFD-T10 + V-AFD-T6' (under Claim B.3) attains this lower bound by a Lipschitz γ_*.

V-AFD adds **K-jump cost**: with `λ_K > 0`, `C_V = Bar + λ_K · 1`. The vector cost reflects both the energy barrier *and* the discrete merge event.

### What V-AFD loses

- **Which** specific blob "wins" the merge (left or right). This is basin-label / pre-merge specific configuration; vector-degenerate at level of `Z`.

### Additional coordinates?

For analyzing the merge geometry: **pre-merge blob centroid coordinates** (e.g. via centroid PCA of u_F_2^*). Not in baseline V-AFD.

---

## Scenario 4 — Split K=1 → K=2

### Setup

- Initial: single blob u_0 ∈ B_{F_1}.
- Final: two-blob u_1 ∈ B_{F_2}.
- Path γ: split trajectory (symmetry-breaking perturbation).

### Expected `z_γ` (mirror of Scenario 3)

| Coord | s=0 | s=0.5 (split instant) | s=1 |
|---|---|---|---|
| Bind | 0.92 | 0.55 (drops, new boundaries) | 0.88 |
| Sep | 0.88 | 0.10 → 0.05 → rising | 0.85 |
| Inside | 0.95 | 0.65 | 0.85 |
| K_act | 1 | **2** | 2 |
| E | E_F_1 | E_F_1 + Bar(F_1, F_2) > Bar(F_2, F_1) | E_F_2 > E_F_1 (T-Merge(b)) |
| τ | 1 bar | 2 bars (one new) | 2 bars |

### What V-AFD captures

- K-jump (split): `TV(K_act ∘ γ) = 1`.
- Topology event: new bar born; `Var_τ` captures this.
- **Asymmetric barrier** `Bar(F_1, F_2) > Bar(F_2, F_1)` (T-Merge(b) Cat A — K=1 is global min, splitting climbs higher).

### Asymmetry

V-AFD inherits AFD-D8 asymmetry: `C_V(F_1 → F_2) ≠ C_V(F_2 → F_1)` generically (forward / backward Bar differ when energies differ).

### Additional coordinates?

Same as Scenario 3 (symmetry-breaking direction is basin-label).

---

## Scenario 5 — Same K, diagnostic change (reconfiguration)

### Setup

- K=1 formation. Path γ moves the blob continuously across the grid (translation if Aut(G) allows, or smooth deformation).
- All endpoints have K_act = 1, same τ topology (single bar).
- Diagnostic vector changes due to position dependence: Bind/Sep/Inside vary as the blob's spatial relationship to the grid boundary changes.

### Expected `z_γ`

| Coord | s=0 | s=0.5 | s=1 |
|---|---|---|---|
| Bind | 0.92 (corner) | 0.94 (center) | 0.91 (other corner) |
| Sep | 0.85 (close to boundary on one side) | 0.92 (boundary equidistant) | 0.85 (other side) |
| Inside | 0.93 | 0.95 | 0.92 |
| K_act | 1 (constant) | 1 | 1 |
| E | E_corner | E_center (possibly lower) | E_corner |
| τ | 1 bar, persistence varies | 1 bar | 1 bar |

### What V-AFD captures

- **Reconfiguration via `Var_D(γ) > 0`**: K is constant but D changes continuously.
- **τ-variation** is small (same number of bars throughout); reordering events are absent.
- **E-variation**: E may have a small barrier or be monotone.

### Take-away

V-AFD can detect **continuous reconfiguration** without K-jumps via the D and τ coordinates alone. This is qualitatively new content beyond AFD-D5's edge structure (which only registers transitions between *distinct* formation states).

### Additional coordinates?

If position itself matters (e.g. for downstream tasks where blob location is observable): **field centroid coordinates** outside V-AFD baseline.

---

## Scenario 6 — Same D, different basin (vector degeneracy)

### Setup

- Two formation states F_a, F_b in different basins of the 15×15 grid.
- F_a: blob in upper-left corner.
- F_b: blob in lower-right corner.
- By Aut(G)-symmetry (D4 reflection or rotation), `D(u_a^*) = D(u_b^*)`, `K_act = K_act`, `E_a = E_b`, `τ_a = τ_b`.
- Hence `Z_{F_a} = Z_{F_b}` exactly.

### Expected Z

`Z_{F_a} = Z_{F_b}`. Vector-indistinguishable.

### What V-AFD captures

Nothing distinguishes F_a from F_b at the vector level. V-AFD-D11 collapses them into the **same vertex** of `G_V`.

### What V-AFD loses

- **Basin identity.** F_a and F_b are dynamically distinct (a gradient flow from u_0 ∈ B_{F_a} reaches u_a^*, not u_b^*).
- **Edge structure.** If F_a has an outgoing edge to F_c but F_b has an outgoing edge to F_d ≠ F_c, the vector graph `G_V` collapses both into a single edge from the shared `Z_{F_a}=Z_{F_b}` vector state, with cost = inf.

### V-AFD-T9 realized

This scenario explicitly realizes V-AFD-T9 information loss. It is the **central limitation** of V-AFD.

### Additional coordinates needed

To distinguish F_a from F_b, V-AFD must augment to `Z_+ = (Z, basin\_label)`. Basin label is locally constant but jumps at basin boundaries — non-Lipschitz.

Alternative: quotient by Aut(G). Then F_a ~ F_b are *identified* as a single Aut(G)-class. This may be the *desired* behavior in some contexts (the system has D4 symmetry, so symmetric configurations are physically equivalent).

### Connection to M-A2

This scenario is the V-AFD analog of the M-A2 question (Priority 1 of plan.md):

> "Is `Stab_{Aut(G)}(u^*) = {e}`?"

If yes, F_a and F_b are distinct formation states with vector-degeneracy. If no (u* is fixed by some symmetry), F_a = F_b literally — no degeneracy, just a single formation state.

---

## Scenario 7 — Symmetric / degenerate family (Goldstone)

### Setup

- Translation-invariant graph (e.g. discrete torus T^2_{20}).
- Goldstone family: u_θ for θ ∈ S^1 (continuous translation orbit).
- All members have identical `Z(u_θ) = Z(u_0)` by translational equivariance of D, K_act, E, τ.

### Expected Z

Continuum of formation states {F_θ : θ ∈ S^1} all share the same `Z`.

### What V-AFD captures

The Goldstone family is collapsed to a single vector vertex in `G_V`. Movement along the family (Goldstone mode) is invisible at vector level.

### What V-AFD loses

- The Goldstone phase θ.
- Dynamics restricted to the family (Goldstone flat direction).

### Connection to H-MORSE-Local

H-MORSE-Local fails on Goldstone families (zero Hessian eigenvalue along the family direction). V-AFD-T7 says: V-AFD doesn't care. The Goldstone family is *vector-degenerate*, hence treated as a single vector state. EK theory cannot apply (Hessian determinant undefined), but V-AFD Layer-2 statements still hold.

### Additional coordinates?

For Goldstone-aware analysis: **family-parameter coordinate** (θ). This is the V-AFD analog of OMS-2.0 / observer moduli (canonical Appendix OMS).

---

## Scenario 8 — Topological event with small energy change

### Setup

- Continuous path γ in Σ_m that crosses the vineyard set V at a "low-energy" crossing.
- Setup: a small ε-perturbation flips the order of two persistence bars in `τ` without changing E by much.
- Specifically: τ(u_-) has bars sorted (b_1, d_1) > (b_2, d_2) by persistence d_1 - b_1; τ(u_+) has them flipped.

### Expected `z_γ`

| Coord | s=0 | s=0.5 (V crossing) | s=1 |
|---|---|---|---|
| Bind | 0.85 | 0.85 (nearly constant) | 0.85 |
| Sep | 0.82 | 0.82 | 0.82 |
| Inside | 0.84 | 0.84 (continuous in d_B) | 0.84 |
| K_act | 2 | 2 → **possibly 2 still** | 2 |
| E | E_0 | E_0 + small ε | E_0 |
| τ | sorted (a, b) | (a, b) → (b, a) | sorted (b, a) |
| Var_τ ((sorted-bar)) | — | **discrete jump** | — |

### What V-AFD captures

- **`Var_τ(γ)`** (in d_B, the bottleneck distance): captures the bar-swap event as a finite contribution.
- `Bar(γ, F_i)` is small.
- `Var_D` is small (D is bottleneck-Lipschitz; bar swap is small in d_B).
- `TV(K_act ∘ γ)` may be 0 if the swap does not change the integer count of bars above threshold.

### What V-AFD loses

- Sorted-bar reordering specifics. The bottleneck metric is *aware* of the swap (CSEH stability) but flattens its directional structure.

### Take-away

The **topology coordinate τ is non-redundant**. A path with small `Bar`, small `Var_D`, zero `TV(K_act)` can still have nontrivial `Var_τ` if it crosses the vineyard. V-AFD's choice to include τ in `Z` is *necessary* for detecting such events.

Alternatively: if τ were *not* in `Z` and only D + K_act were tracked, this scenario would be invisible at vector level.

---

## Summary table

| Scenario | What V-AFD captures | What V-AFD loses | Additional coords needed? |
|---|---|---|---|
| 1 Static single | Pareto dominance, stability | Spatial location | Basin label (if dynamical specificity needed) |
| 2 Weak formation | Pareto-dominated; low Q | Threshold sensitivity | Persistence-gap statistic |
| 3 Merge K=2→1 | Bar, K-jump, τ event, D variation | Which blob wins | Pre-merge centroid (if geometry matters) |
| 4 Split K=1→2 | K-jump, τ event, asymmetric barrier | Split direction | Symmetry-breaking direction (basin-label) |
| 5 Reconfiguration (same K) | Var_D > 0 even with K, τ constant | Position | Field centroid (if location matters) |
| 6 Same D different basin | nothing distinguishes | Basin identity | **Basin label essential** |
| 7 Goldstone family | family collapsed to single vertex | Goldstone phase θ | Family parameter (OMS-2.0 analog) |
| 8 Topology event small E | Var_τ captures bar swap | Sorted-bar order details | — (τ is sufficient at d_B level) |

**Headline.** V-AFD baseline `Z = (D, K_act, E, τ)` is **sufficient** for ordering, stability, and Pareto reasoning at Layer 2. It is **insufficient** for: (a) dynamical specificity (Scenarios 1, 6, 7 — basin label needed), (b) full geometric reconstruction (Scenarios 3, 4, 5 — centroid / field PCA needed). Each insufficiency is a vector-degeneracy and is the content of V-AFD-T9 + OP-VAFD-004.
