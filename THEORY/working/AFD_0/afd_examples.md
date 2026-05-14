---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

> [!nav] Linked: [[MOC_AFD_0_foundation]] · [[THEORY_INDEX]]


# AFD-0 Worked Examples

Seven concrete examples on small grids illustrating the AFD-0 definitions. All grids use 4-neighbor connectivity unless otherwise stated. Parameter conventions follow `canonical.md` §8 and `CODE/scc/params.py`. Numerical anchors reference `experiments/` results where available.

Examples 1–4 illustrate the formation-state apparatus (AFD-D1..D14). Examples 5–7 illustrate the diagnostic / topological / degenerate-symmetry edge cases.

---

## Example 1 — Single Formation State (K = 1, clean)

**Setup.** Grid `5×5` (n = 25). Parameters β = 30, α = 1.0 (so β/α = 30 > 4 λ_2 ≈ 4 · 0.382 = 1.53 well above β_crit). Mass m = 12. Closure coefficient λ_cl = 1.0, λ_sep = 1.0, λ_bd = 0.5.

**Initial field.** u_0(x, y) = 0.95 if (x, y) is in the central 3×3 block, else 0.05. Mass-projected to m = 12.

**Run.** `find_formation(graph, params)` → converges to u_F^* with single connected high-cohesion region, support roughly the central 3×3.

**Formation state F_1.**

- u_F^* = (the converged minimizer).
- B_F_1 = gradient-flow basin of u_F^*.
- d_F_1 ≈ (Bind 0.92, Sep 0.88, Inside 0.95, Persist 1.0) — all high.
- K_F_1 = K_act(u_F^*) = 1 (single H_0 bar of high persistence).
- τ_F_1 = single long bar (essential, birth at u_max ≈ 0.95).
- E_F_1 ≈ minimal value among local minima of E with mass 12.

**AFD interpretation.** V_form contains F_1 (and any graph-automorphism translates if mass and parameters permit them). G_form has F_1 (and translates) as vertices.

---

## Example 2 — Two Formation States Separated by a Barrier

**Setup.** Grid `5×5`. Parameters as in Example 1 but mass m = 20 (large enough to support two formations on opposite corners). β = 30.

**Initial fields.**

- u_0^A: high in upper-left 2×2.
- u_0^B: high in lower-right 2×2.

**Run.** Two `find_formation` runs from u_0^A and u_0^B with mass m = 20 yield:

- F_A with u_F_A^* concentrated in upper-left.
- F_B with u_F_B^* concentrated in lower-right (graph-symmetric mirror of F_A).

These are two formation states with the same energy: E_F_A = E_F_B.

**Barrier between them.** A nudged-elastic-band (NEB) interpolation between u_F_A^* and u_F_B^* finds a saddle point u_s^* at the midline (3rd row/column). The barrier is

> `Bar(F_A, F_B) = E(u_s^*) − E_F_A` (and by symmetry = `Bar(F_B, F_A)`).

Numerical anchor: exp33 on 12×12 with similar parameters gives Bar ≈ 0.18 in normalized units. For 5×5 the barrier is lower (typically Bar ≈ 0.05–0.10) due to smaller graph distance.

**AFD interpretation.**

- C_AFD(F_A, F_B) = C_AFD(F_B, F_A) = Bar (by graph symmetry, the asymmetric Bar coincides with its reverse here).
- ExitCost(F_A) = ExitCost(F_B) = Bar.
- F_A ≼_bar F_B and F_B ≼_bar F_A (tied — symmetry-paired formations have equal stability).
- K_F_A = K_F_B = 1; both states live in S_1.

---

## Example 3 — K = 1 to K = 2 (Split)

**Setup.** Grid `7×7`. Mass m = 24. Parameters chosen to make a single-formation minimizer thin enough that an artificial split is energetically close.

**Initial field.** Single elongated bump u_0(x, y) ≈ 0.8 along the central row. Mass m = 24.

**Run.** Two stable endpoints:

- F_1: single elongated formation (K_act = 1, long bar in τ).
- F_2: two side-by-side formations (K_act = 2, two bars of comparable length).

These coexist as separate basins for parameters near the K = 1 / K = 2 metastability threshold.

**K-jump along a transition path.** Path γ : F_1 → F_2 must cross the vineyard set V at the moment the second persistence bar is "born long enough" to count toward K_act (i.e. its length crosses the threshold ε = 0.225 in the standard regime).

**AFD interpretation.**

- C_AFD(F_1, F_2) = Bar(F_1, F_2) + λ_K · 1 (one K-jump event: K_act 1 → 2).
- F_1 ∈ S_1, F_2 ∈ S_2 (different K-strata).
- T-Merge(b) says F_1 is the global energy minimum (K = 1 globally preferred), so under pure gradient flow the F_2 → F_1 path is energetically downhill at large scale, though it must traverse a K-merge barrier (Example 4).

---

## Example 4 — K = 2 to K = 1 (Merge): the K-Jump Event

**Setup.** Same as Example 3 but starting from F_2 (two formations).

**Transition path.** Optimal merge path γ : F_2 → F_1:

- s = 0: u_F_2^* (two bumps separated by a low valley).
- s ∈ (0, s_*): the two bumps move toward each other; the valley fills.
- s = s_*: vineyard crossing — the second bar in the persistence diagram drops below ε, so K_act(γ(s)) jumps from 2 to 1. **This is the K-jump event** (AFD-D13, K-merge type).
- s ∈ (s_*, 1): a single elongated bump relaxes to u_F_1^*.

**Barrier.** The barrier height is governed by Δ_min along the valley between the two formations at s ∈ (0, s_*).

**AFD interpretation.**

- C_AFD(F_2, F_1) = Bar(F_2, F_1) + λ_K · 1.
- J_K(γ) = 1 (exactly one K-jump, at s = s_*).
- γ crosses V transversally (codim-1 in Σ_m).
- C_AFD(F_2, F_1) < C_AFD(F_1, F_2) in general (downhill in energy after the K-jump), so the cost is asymmetric.

**Numerical anchor.** exp38, exp60 on T^2_{20} document positive merge barriers c(β, n, G) > 0 for K ≥ 2; this is the empirical support for OP-AFD-004.

---

## Example 5 — Diagnostic Vector Change Without K Change

**Setup.** Same grid as Example 1. A continuous deformation u_0 → u_1 within S_1 (K_act = 1 throughout) that changes the diagnostic vector.

**Path.** Parametrize u_s = (1 − s) u_F_1^* + s u_F_1^{**}, mass-projected, where u_F_1^* is a tight 3×3 formation and u_F_1^{**} is a looser 4×4 formation, both K_act = 1.

**Diagnostic changes.** Along γ:

- Sep typically increases (looser formation → less u-weighted boundary distinction *until* the formation becomes too diffuse).
- Bind decreases (residual ‖u − Cl(u)‖ grows).
- Inside changes (the persistence top-bar gets shorter as the formation becomes diffuse).
- Persist stays ~1.
- K_act stays = 1.

**AFD interpretation.**

- γ stays in S_1 (no K-jump). J_K(γ) = 0.
- Var_D(γ) > 0 (the diagnostic moves through [0,1]^4).
- This example shows AFD-D9 (diagnostic variation) is a non-trivial finer cost; without it, two states in the same K-stratum with different shapes would be costed equally.

---

## Example 6 — Topological Change Without Large Energy Change

**Setup.** A path γ between two K_act = 1 states whose persistence diagrams τ are bottleneck-far but whose energies are close (within numerical tolerance).

**Construction.** Two single-formation minimizers u_F_a^*, u_F_b^* in graph-isomorphic positions on a *non-symmetric* graph (e.g. a path graph of length 7 with mass concentrated near one endpoint vs the other). Energies differ by < 1% but the *position* of the persistence bar (essential bar location in the diagram) differs by Δ along the energy axis.

**Diagnostic.** τ_F_a vs τ_F_b: same number of bars but bottleneck-distant.

**AFD interpretation.**

- Bar(F_a, F_b) is small (energies close, optimal interpolating path stays low).
- d_top(τ_F_a, τ_F_b) is large.
- The minimal cost C_AFD (with λ_D = λ_K = 0) is small, but a diagnostic-aware cost with λ_D > 0 reflects the topological change.
- This example argues for the *option* to include Var_D in AFD-D7 even when the energy barrier is negligible.

---

## Example 7 — Degenerate / Symmetric Formation Family (D_4 symmetry)

**Setup.** Grid `4×4` (n = 16). Mass m = 10. Parameters β = 25, α = 1.0. Graph has Aut(G) = D_4 (rotations and reflections of the square).

**Minimizers.** Under D_4 symmetry, generic minimizers come in orbits of size 4 or 8. A typical minimizer u_F_*^*:

- Concentrates mass near one corner (orbit of 4 under rotation) or near one edge (orbit of 4 under rotation × reflection ≅ D_4 / Z_2 of size 4).
- Has degenerate Hessian along the orbit direction in the configuration space (Goldstone-like).

**AFD-0 treatment (raw representatives).** V_form contains four distinct formation states F_1, F_2, F_3, F_4, one per orbit element. They have identical energy, identical diagnostic, identical K_act = 1, identical τ.

**ExitCost.** Each F_i has the same exit cost (barrier to any of the other three via the corresponding edge-saddle). So ExitCost(F_1) = ... = ExitCost(F_4) — all tied in ≼_bar.

**H-MORSE failure.** Hessian at u_F_1^* is degenerate (zero eigenvalue along the Aut(G) orbit direction). H-MORSE-Local fails here.

**AFD-T9 in action.** AFD-0 results all hold:

- AFD-T1: V_form ≠ ∅ (four formation states exist).
- AFD-T2: D is Lipschitz (no Hessian needed).
- AFD-T3: all four lie in S_1.
- AFD-T5: C_AFD(F_i, F_j) < ∞ (barrier paths exist; specifically the rotation-induced interpolation).
- AFD-T6: ≼_bar is a total preorder with all four tied.

**EK / Layer 3.** Exact EK rate at u_F_i^* is *not defined* (degenerate Hessian → det H = 0 → A_ij undefined). AFD-T10 (Design Principle) recommends using:

- (a) Equivalence classes [F] = Aut(G)-orbit (AFD-D4 refinement) — combines the four into one quotient state.
- (b) Conley index treatment of the orbit as an isolated invariant set (AFD-T10 (b)).
- (c) Quotient state graph G_form / Aut(G) — promotes to a single-vertex graph with self-loops representing intra-orbit rotations.

This example demonstrates how AFD-0 "fails gracefully" where Layer 3 fails outright: the abstract formation-state apparatus continues to function and to assign costs (or recognize tied states), while exact-rate computation becomes unavailable. The AFD-T10 strategies offer principled ways to repackage the degenerate orbit when needed.

---

## Cross-example summary

| Example | Illustrates | AFD-D / T used |
|---|---|---|
| 1 | Single formation state with high diagnostic | AFD-D1, D2, D3, T1 |
| 2 | Symmetric two-state pair, basic barrier | AFD-D5, D7, D8, T6 |
| 3 | K_act stratum change (1 → 2) | AFD-D10, D12, D13 |
| 4 | K-merge K-jump event with positive barrier | AFD-D13, T7, OP-AFD-004 |
| 5 | Diagnostic motion within a K-stratum | AFD-D9, AFD-T2 |
| 6 | Topology change with small ΔE | AFD-D11, T2, motivation for λ_D > 0 |
| 7 | Degenerate Goldstone-like orbit; H-MORSE failure | AFD-T9, T10, OP-AFD-009, OP-AFD-010 |
