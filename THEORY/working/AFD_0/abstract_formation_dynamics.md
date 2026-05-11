---
type: working/afd
status: AFD-0 Draft (2026-05-12)
version: 0.1
authors: AFD-0 working session
---

# Abstract Formation Dynamics — AFD-0 Foundation

## 0. Executive Summary

This document defines **Abstract Formation Dynamics (AFD-0)**, the Layer-2 abstract dynamics layer of the SCC architecture. AFD-0 introduces the notions of *formation state*, *formation-state graph*, *abstract transition cost*, *K-stratum*, *barrier preorder*, and *EK refinement compatibility*, while explicitly avoiding Morse-nondegeneracy assumptions.

The central architectural commitment, formalized in §13 and proved in §14 as Theorem AFD-T9, is:

> **AFD separates transition order from transition rate.**
> The existence of a formation transition, the comparison of its abstract cost, and the induced K-stratum dynamics do not require Hessian determinant prefactors. Exact Eyring-Kramers theory, when applicable, refines selected AFD edges by assigning asymptotic stochastic rates whose exponential order is governed by the AFD barrier term.

> **H-MORSE is a Layer-3 regularity hypothesis, not a Layer-2 formation-dynamics axiom.**

AFD-0 builds entirely on existing Cat A Layer-1 SCC results (T8-Core, T14, T-Merge(b), T-Persist-1(b), T7-Enhanced, P-F-A1 Package I, QM3, Commitment 16, T-Temporal-Identity, the Predicate-Energy Bridge), with no new analytic hypotheses beyond those.

## 1. Motivation: Why Exact Rates Are Too Low-Level

The CV-1.14 / Package II programme in `CV114_H_MORSE_PACKAGEII/` aims at exact Eyring-Kramers rates for SCC. That programme requires:

- H-MORSE-Local: nondegenerate Hessians at minima of E on the constraint Σ_m (currently Cat B).
- H-MORSE-Saddle: nondegenerate Hessians at index-1 saddles (not yet registered).
- FW quasipotential identification with Bar(F_i, F_j).
- Reflected-Langevin adaptation of the standard EK prefactor (literature gap).
- Small-noise limit T_* → 0 (T_* axiomatic, OP-0021).

These are heavy assumptions, and several SCC regimes (T8-Full bifurcation threshold, D_4-symmetric minimizers on regular grids, Goldstone families on translation-invariant graphs) actively violate nondegeneracy.

Almost every actually-needed downstream claim in SCC, however, is *not* an exact-rate claim. We need:

- Existence of formation states (Cat A via T8-Core).
- Comparison of stability: which formation has higher barrier? (no determinant needed).
- K-stratum decomposition: which configurations live in which K_act class? (Commitment 16, Cat A).
- Diagnostic dynamics: how does D = (Bind, Sep, Inside, Persist) evolve along a path? (QM3 + Predicate-Energy Bridge, Cat A).
- Topological identity: when does u_t = u_s persist as the same formation? (T-Temporal-Identity, CV-1.13 Cat A).

These are all *abstract* (order-level, ordinal, topological) claims. AFD-0 packages them as a coherent Layer-2 theory.

## 2. Three-Layer Architecture

```
Layer 1  SCC Core         u, E, Cl, D, C, K_field, K_act, K_soft, diagnostics, Pkg I
Layer 2  AFD-0            F-state, G_form, C_AFD, K-strata, ≼_bar, vineyard
Layer 3  Exact EK theory  H-MORSE-Local + Saddle, EK prefactor, FW quasipotential
```

Layer 2 depends on Layer 1 (Cat A inputs only). Layer 3 depends on Layer 2 (for barrier ordering) and on extra regularity (H-MORSE). Layer 3 refines Layer 2 but does not replace it.

A complete picture is in `afd_layer_diagram.md`.

## 3. SCC Objects Used by AFD

We fix once and for all the Cat A objects from Layer 1 that AFD-0 builds on:

| Object | Source | Status |
|---|---|---|
| Graph state G = (X_t, E_t) and Laplacian L | `canonical.md` §3.2 | Cat A |
| Field u ∈ Σ_m ⊂ [0,1]^n, m = Σ u_i | §3.3, §3.9 | Cat A |
| Energy E(u) = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd | §8.1 | Cat A |
| Closure operator Cl with A3 (contraction) | §3.4, §6 Group A | Cat A |
| Distinction D, co-belonging C | §3.7, §3.6 | Cat A |
| Diagnostic vector D = (Bind, Sep, Inside, Persist) | §7.2 | Cat A |
| K_field (architectural cap) | Commitment 16 (i) | Cat A |
| K_act (active count, integer) | Commitment 16 (ii), D-ST-3 | Cat A |
| K_soft (persistence-weighted, Lipschitz) | QM3, `working/E/soft_K_definition.md` | Cat A |
| T8-Core: minimizer exists when β/α > 4 λ_2 / |W''(c)| | §13 Cat A | Cat A |
| T14: Łojasiewicz gradient-flow convergence | §13 Cat A | Cat A |
| T-Merge(b): K=1 is global min | §13 Cat A | Cat A |
| T-Persist-1(b): basin radius r_basin = sqrt(2 Δ_min/λ_max) | §13 Cat A | Cat A |
| T7-Enhanced: enhanced metastability gap | §13 Cat A | Cat A |
| P-F-A1 Package I (AR/SDE/GI/PE) | §13 Cat A (CV-1.8–1.9) | Cat A |
| T-Temporal-Identity (4 parts) | §13 Cat A (CV-1.13) | Cat A |
| Predicate-Energy Bridge Sep = 1 − E_sep/m | §13 Cat A | Cat A |
| Bottleneck stability (CSEH 2007) | external | accepted |

We will *not* invoke any Cat B or Cat C result below without explicitly labeling it. In particular H-MORSE-Local (CV-1.14 target) is **not used** in AFD-0.

## 4. Formation Representatives

### Definition AFD-D1 (Formation Representative)

A field `u_F^* ∈ Σ_m` is a **formation representative** if it is a local minimizer of `E` on `Σ_m`:

> there exists ρ > 0 with E(u_F^*) ≤ E(v) for all v ∈ Σ_m with ‖v − u_F^*‖ ≤ ρ.

We do **not** require the Hessian to be nondegenerate. Existence of at least one such `u_F^*` (with non-trivial support, i.e. `u_F^* ≢ const`) is guaranteed by **T8-Core (Cat A)** whenever β/α > 4 λ_2/|W''(c)|.

*Notes.*

(a) Degenerate minimizers (zero-eigenvalue Hessian, Goldstone families) are explicitly permitted.

(b) Membership in `∂Σ_m` (where some `u_i = 0` or `u_i = 1`) is permitted; T14 (Łojasiewicz) still applies on the analytic manifold pieces.

(c) A "trivial" critical point — uniform field `u ≡ m/n · 1` — is a representative only when β/α ≤ β_crit; above threshold it is unstable (T8-Core) and is excluded from V_form by convention (non-trivial support requirement).

## 5. Basins and Formation States

### Definition AFD-D2 (Formation Basin — Deterministic)

The **deterministic basin of attraction** of a representative `u_F^*` is

> B_det(F) := { u ∈ Σ_m : the constrained gradient flow `dot u = − P_T ∇E(u)` starting from u converges to u_F^* as t → ∞ }

where P_T is the projection onto T Σ_m. This is well-defined by **T14 (Cat A)**: every gradient-flow trajectory converges to a critical point. The basins partition `Σ_m` modulo the measure-zero stable manifolds of non-minimizer critical points (saddles, maxima, degenerate non-min critical sets), which are precisely the basin boundaries.

### Definition AFD-D2' (Formation Basin — Stochastic, optional)

For small noise `T_* > 0`, the **stochastic basin** `B_stoch(F, T_*)` is the quasi-stationary distribution concentrated near `u_F^*`. Existence of the underlying reflected Langevin dynamics is **Package I (T-PF-A1-SDE Cat A)**; existence of the Gibbs invariant measure is **T-PF-A1-GI Cat A**; exponential return to `B_stoch` is **T-PF-A1-PE Cat A**. AFD-D2' is the stochastic variant of AFD-D2 used only in §11 (FW compatibility) and §13 (EK compatibility). AFD-0 default is **AFD-D2 (deterministic)**.

### Definition AFD-D3 (Formation State)

A **formation state** is a tuple

> `F = (u_F^*, B_F, d_F, K_F, τ_F, E_F)`

where:

- `u_F^*` ∈ Σ_m is a formation representative (AFD-D1).
- `B_F` = `B_det(F)` (AFD-D2 default), or `B_stoch(F, T_*)` in the stochastic variant (AFD-D2').
- `d_F` = `D(u_F^*)` = (Bind, Sep, Inside, Persist) ∈ [0,1]^4.
- `K_F` = `K_act(u_F^*)` ∈ {1, ..., K_field}; well-defined by Commitment 16 (Cat A).
- `τ_F` = `TopSig(u_F^*)` := the H_0 persistence diagram of the superlevel-set filtration of `u_F^*` (the same diagram used in QM3 / `k_soft.py`).
- `E_F` = `E(u_F^*)`.

### Definition AFD-D4 (Formation Equivalence — optional refinement)

Two formation states `F_i ~ F_j` if their representatives `u_{F_i}^*, u_{F_j}^*` lie in the same connected component of the set of local minimizers, share the same K_act, and have τ-diagrams differing only by an ε-perturbation (ε < persistence threshold). This is *not* used in AFD-0; it is reserved for a future refinement.

**Design choice for AFD-0.** Use raw representatives, *not* equivalence classes. This avoids commitments about Aut(G)-symmetry and Goldstone-family identification, which interact with OP-0008 / OP-0009.

## 6. Formation State Graph

### Definition AFD-D5 (Formation State Graph)

The **formation state graph** is the weighted directed graph

> `G_form = (V_form, E_form, w)`

where:

- `V_form = { F : F is a formation state per AFD-D3 }`.
- `(F_i, F_j) ∈ E_form` iff `C_AFD(F_i, F_j) < ∞` (AFD-D7 below).
- `w(F_i, F_j) := C_AFD(F_i, F_j)`.

Well-definedness is AFD-T4.

### Definition AFD-D6 (Admissible Path)

A continuous map `γ : [0,1] → Σ_m` is **admissible** from F_i to F_j (notation γ ∈ Adm(F_i, F_j)) if:

- (P1) γ is continuous as a map [0,1] → Σ_m (compact-open topology).
- (P2) γ(0) ∈ cl(B_{F_i}).
- (P3) γ(1) ∈ cl(B_{F_j}).
- (P4) γ(s) ∈ Ω_m := [0,1]^n ∩ Σ_m for all s ∈ [0,1].

Paths *may* cross K-jump regions and *may* touch ∂Σ_m. Rectifiability (finite length) is not required by (P1)–(P4), but is required for diagnostic-variation cost (AFD-D9) and K-jump cost (AFD-D10) to be finite.

## 7. Abstract Transition Cost

### Definition AFD-D7 (Abstract Transition Cost)

For F_i, F_j ∈ V_form, the **abstract transition cost** is

> `C_AFD(F_i, F_j) := inf_{γ ∈ Adm(F_i, F_j)} J_AFD(γ; F_i)`,
> `J_AFD(γ; F_i) := Bar(γ, F_i) + λ_D · Var_D(γ) + λ_K · J_K(γ)`,

with `λ_D, λ_K ≥ 0` weighting parameters.

**Minimal version (λ_D = λ_K = 0).** `C_AFD(F_i, F_j) = Bar(F_i, F_j)`, the pure energy barrier. This is the version we use for all subsequent comparisons with FW / EK; the additional terms are diagnostic-aware refinements.

### Definition AFD-D8 (Barrier Term)

> `Bar(γ, F_i) := max_{s ∈ [0,1]} ( E(γ(s)) − E_F_i )`,
> `Bar(F_i, F_j) := inf_{γ ∈ Adm(F_i, F_j)} Bar(γ, F_i)`.

This is **asymmetric** in general (`Bar(F_i, F_j) ≠ Bar(F_j, F_i)` when E_F_i ≠ E_F_j). The **symmetric variant** is

> `Bar_sym(F_i, F_j) := inf_{γ ∈ Adm(F_i, F_j)} max_s ( E(γ(s)) − max(E_F_i, E_F_j) )`.

The FW quasipotential identifies most naturally with the asymmetric Bar (AFD-T8 and §11).

### Definition AFD-D9 (Diagnostic Variation)

For Lipschitz γ (when γ is rectifiable and D is Lipschitz, which is AFD-T2):

> `Var_D(γ) := ∫_0^1 ‖D'(γ(s)) γ'(s)‖_2 ds`.

For continuous-only γ:

> `Var_D(γ) := TV(D ∘ γ)`,

the total variation of D∘γ as a map [0,1] → [0,1]^4. Always Var_D(γ) ∈ [0, ∞]; finite when γ is rectifiable.

### Definition AFD-D10 (K-Jump Cost)

`K_act : Σ_m → {1, ..., K_field}` is integer-valued and (by Commitment 16) locally constant on `Σ_m^◦ \ V`, where V ⊂ Σ_m is the **vineyard set** of codimension-1 semi-algebraic configurations at which the H_0 superlevel persistence diagram changes (see `working/E/soft_K_definition.md` §2.3 for the formal definition of V).

> `J_K(γ) := TV(K_act ∘ γ)` = total variation of K_act along γ.

Equivalently when γ crosses V transversally, J_K(γ) = #{vineyard crossings of γ}. J_K(γ) ∈ {0, 1, 2, ...}; bounded above by 2 K_field along any rectifiable γ (each K can be visited and left at most O(1) times along a finite-length path inside Σ_m, see AFD-T5 proof).

### Definition AFD-D11 (Topological Signature Distance)

`τ(u)` denotes the H_0 persistence diagram of the superlevel filtration of u (a finite multiset of bars (b_i, d_i) with b_i ≥ d_i ≥ 0). Distances on diagrams:

> `d_top(τ(u), τ(v))` := `d_B(τ(u), τ(v))` (bottleneck) or `W_2(τ(u), τ(v))` (Wasserstein-2).

**Stability (CSEH 2007, Cohen-Steiner et al.):** `d_B(τ(u), τ(v)) ≤ ‖u − v‖_∞`. Thus τ is 1-Lipschitz from (Σ_m, ‖·‖_∞) to the space of persistence diagrams with the bottleneck distance. The Wasserstein-2 variant is well-defined on finite diagrams; stability constants differ (see CSEH 2010).

## 8. K-Strata and K-Jumps

### Definition AFD-D12 (K-Stratum)

For each K ∈ {1, ..., K_field},

> `S_K := { u ∈ Σ_m : K_act(u) = K }`.

These give a **set-theoretic decomposition**

> `Σ_m = ⨆_{K=1}^{K_field} S_K`.

**Warning.** S_K is in general *not* a smooth manifold and *not* a Whitney stratum. It is only the level set of an integer-valued function. Whitney regularity, definability, transversality, or persistence-regularity hypotheses must be added before "stratum" can be used in its differential-topology sense. The terminology "stratum" here refers exclusively to the set-theoretic decomposition.

### Definition AFD-D13 (K-Jump Event)

Along a continuous γ : [0,1] → Σ_m, a **K-jump event** at s_0 ∈ (0,1) is a discontinuity of `s ↦ K_act(γ(s))`. Types:

- **K-birth.** K_act increases (new connected component nucleates / persistence bar is born long enough to be counted).
- **K-merge.** K_act decreases by one (two formations merge).
- **K-split.** K_act increases by one (one formation splits; rare under pure gradient flow per T-Merge(b)).

K-jumps occur when γ crosses the vineyard set V (see `working/E/soft_K_definition.md` §2.3): V is the locus of birth/death exchanges, i.e. codimension-1 inside Σ_m. Hence under genericity, J_K(γ) counts the number of transversal V-crossings of γ.

**Comment.** A K-jump is a topological event in K_act, not (necessarily) a single Morse saddle crossing. In the EK / Morse picture, certain K-merges correspond to crossing a specific index-1 saddle, but the converse does not hold in general (degenerate saddle families can host multi-K transitions). This independence is what makes AFD's K-jump notion robust under H-MORSE failure.

## 9. Barrier Orders and K-Selection

### Definition AFD-D14 (Barrier Preorder — Exit Cost)

The **exit cost** of F_i is

> `ExitCost(F_i) := inf_{j ≠ i, F_j ∈ V_form} Bar(F_i, F_j) = inf_{γ exiting B_{F_i}} max_s (E(γ(s)) − E_{F_i})`.

The **barrier preorder** is

> `F_i ≼_bar F_j` iff `ExitCost(F_i) ≥ ExitCost(F_j)`.

Interpretation: `F_i ≼_bar F_j` means F_i is at least as stable (higher exit barrier) as F_j.

**Warning on transitivity.** The exit-cost version (above) is a **total preorder** (AFD-T6) because ExitCost : V_form → [0, ∞] is a real-valued scalar and ≥ is a total order on ℝ. However, the *pairwise* comparison `C_AFD(F_i, F_j) vs C_AFD(F_j, F_i)` does **not** define a transitive relation in general; using only the exit-cost version yields a valid preorder.

## 10. EK Refinement Compatibility

### Definition AFD-D15 (EK Refinement Compatibility)

Under the additional **Layer-3 hypotheses**

- (H-MORSE-Local) Hessian of E on T_{u_F^*} Σ_m is nondegenerate at every formation representative;
- (H-MORSE-Saddle) the optimal connecting saddle `u_s^*` exists, has index 1, and has nondegenerate Hessian on T_{u_s^*} Σ_m;
- (P-F-A1) reflected Langevin dynamics (T-PF-A1-SDE, Cat A);
- (Small noise) `T_* > 0` axiomatic per OP-0021, and `T_* → 0`;

the **Eyring-Kramers rate** between F_i and F_j is

> `r_ij = A_ij · exp(−Bar(F_i, F_j) / T_*) · (1 + O(T_*))`

with prefactor

> `A_ij = (|λ^−_saddle| / 2π) · sqrt( |det Π_T H_E(u_s^*) Π_T|_{1^⊥} / det Π_T H_E(u_F_i^*) Π_T|_{1^⊥} )`.

Layer 2 produces only `Bar(F_i, F_j)` (the exponent). Layer 3 produces `A_ij` (the prefactor). Together, Layer 2 + Layer 3 = exact EK rate. Thus

> AFD barrier ordering ≡ EK rate ordering (up to prefactor).
> EK refines AFD; AFD does not require EK.

## 11. Compatibility with Freidlin-Wentzell

The Freidlin-Wentzell (FW) large-deviation theory applied to the reflected Langevin SDE on `Σ_m` (well-posed by T-PF-A1-SDE Cat A) yields a quasipotential

> `V(u_0, u) := inf_{γ : γ(0) = u_0, γ(T) = u, T > 0} I_T(γ)`,

with action `I_T(γ) = (1/4) ∫_0^T ‖γ'(s) + ∇_T E(γ(s))‖^2 ds` (overdamped form). For the gradient SDE, FW gives

> `V(u_F_i^*, u_F_j^*) = inf_{γ} max_s ( E(γ(s)) − E_F_i ) = Bar(F_i, F_j)`.

This is the standard identification of FW quasipotential with the energy barrier for gradient SDEs. **It does not require H-MORSE.** Hence:

- AFD-D8 (Bar) coincides with the FW quasipotential.
- AFD reduces to FW in the small-noise gradient limit (modulo the boundary-reflection correction, which is handled by reflected Langevin per T-PF-A1-SDE).
- AFD-T8 is the small-noise asymptotic statement; its proof reduces to FW + reflected-Langevin theory (OP-AFD-005).

## 12. Compatibility with Conley Dynamics

When critical points are degenerate (Goldstone families, D_4-symmetric minimizers, T8-Full bifurcation threshold), the Morse-decomposition picture fails locally. Conley index theory provides a rigorous replacement: **isolated invariant sets** and **Morse decompositions** in Conley's sense exist even without nondegeneracy.

AFD-0 is designed so that formation representatives `u_F^*` can be replaced or refined by isolated invariant sets when needed:

- AFD-D1 (representative) → isolated invariant set N_F (Conley).
- AFD-D2 (basin) → attractor of N_F in the Conley sense.
- AFD-D5 (G_form) → Conley-Morse digraph.
- AFD-D7 (cost) → continues to be defined via paths and energy.

This is reserved for an AFD-1 / AFD-Conley extension. AFD-0 itself stops at the level of local minimizers and gradient-flow basins.

## 13. Compatibility with Eyring-Kramers (why H-MORSE is Layer 3)

**Slogan statements (canonical for §13, to be cited verbatim).**

1. **"AFD separates transition order from transition rate. The existence of a formation transition, the comparison of its abstract cost, and the induced K-stratum dynamics do not require Hessian determinant prefactors. Exact Eyring-Kramers theory, when applicable, refines selected AFD edges by assigning asymptotic stochastic rates whose exponential order is governed by the AFD barrier term."**

2. **"H-MORSE is a Layer-3 regularity hypothesis, not a Layer-2 formation-dynamics axiom."**

3. **"A K-jump is first an event in the diagnostic-topological coarse dynamics, not necessarily a single Morse saddle crossing."**

4. **"The term *stratum* is used cautiously. Initially S_K is only the level/decomposition set of K_act. Additional definability, transversality, or persistence-regularity assumptions are required before S_K can be treated as a smooth or Whitney stratum."**

5. **"AFD is compatible with Conley theory: formation states may later be replaced or refined by isolated invariant sets and Morse decompositions. This allows degenerate or symmetric formation families to be handled without forcing Morse nondegeneracy."**

The formal H-MORSE reclassification — H-MORSE ∈ Layer 3, H-MORSE ∉ Layer 2 — is in `afd_hmorse_reclassification.md` and is proved by Theorem AFD-T9 below.

## 14. Theorems and Proofs

### AFD-T1 (Existence of Formation States) — Proposition

**Assumptions.** SCC energy E on Σ_m with `β/α > 4 λ_2 / |W''(c)|` (T8-Core condition).

**Statement.** `V_form ≠ ∅`. Concretely, E has at least one local minimizer `u^* ∈ Σ_m` with non-trivial support (i.e. `u^* ≠ (m/n) · 1`).

**Proof.** Direct from T8-Core (Cat A, canonical.md §13). T8-Core proves existence of a non-trivial local minimizer with positive diagnostic margin; that minimizer is a formation representative (AFD-D1). □

---

### AFD-T2 (Diagnostic Map Continuity) — Theorem

**Assumptions.** E satisfies the SCC core assumptions of `canonical.md` §3 and §8. `D = (Bind, Sep, Inside, Persist) : Σ_m → [0,1]^4` is the diagnostic map of §7.2.

**Statement.** D is Lipschitz from (Σ_m, ‖·‖_2) to ([0,1]^4, ‖·‖_∞). Component bounds:

- **Sep.** Lipschitz; constant bounded by L_E_sep / m, where L_E_sep is the Lipschitz constant of E_sep on Σ_m. Justification: the Predicate-Energy Bridge (Cat A) gives `Sep(u) = 1 − E_sep(u)/m` with E_sep Lipschitz by §8.3 and Cat A operator regularity.
- **Bind.** Lipschitz with constant L_Bind ≤ (1 + L_Cl) / sqrt(n), where L_Cl is the Lipschitz constant of the closure operator Cl (finite by A3 contraction, Cat A). Justification: `Bind(u) = max(0, 1 − ‖u − Cl(u)‖_2 / sqrt(n))`, and the inner map `u ↦ u − Cl(u)` is (1 + L_Cl)-Lipschitz.
- **Inside.** Lipschitz with constant bounded by a graph-dependent polynomial in n times the bottleneck stability constant. Justification: Inside is built from the persistence diagram (via `_persistence_h0_graph` in `diagnostics.py`) and from L^∞ statistics of u; QM3 + CSEH 2007 give bottleneck Lipschitz stability of the underlying persistence object.
- **Persist.** 1-Lipschitz; Persist = min over a Lipschitz family in the canonical formulation; equivalently bounded below by Cat A persistence-stability arguments.

**Proof sketch.** Combine the Predicate-Energy Bridge (Cat A, gives Sep Lipschitz), A3 closure contraction (Cat A, gives Bind Lipschitz), QM3 (Cat A, K_soft Lipschitz; same persistence machinery for Inside), and CSEH 2007 bottleneck stability for Persist. Each component is Lipschitz with a graph-dependent (finite-n) constant; the combined map D is Lipschitz with constant L_D ≤ sqrt(L_Sep^2 + L_Bind^2 + L_Inside^2 + L_Persist^2). □

**Status.** Theorem (assembly of Cat A facts). The detailed exact constants for Inside and Persist depend on `_persistence_h0_graph` implementation; the *existence* of finite Lipschitz constants is Cat A from QM3 + CSEH.

---

### AFD-T3 (K-Act Decomposition) — Proposition

**Statement.** `Σ_m = ⨆_{K=1}^{K_field} S_K` is a set-theoretic disjoint decomposition, where `S_K = { u ∈ Σ_m : K_act(u) = K }`.

**Proof.** K_act is a well-defined integer-valued function on Σ_m (Commitment 16, Cat A; K_act(u) ∈ {1, ..., K_field} by construction, with K_act = #PersComp at threshold `ε = 0.01 · m̄` per `canonical.md` §3.11 / D-ST-3). Disjointness and cover are immediate from K_act being a function. □

**Warning.** This is a partition only as sets. S_K is generally not a smooth submanifold and not a Whitney stratum (see Definition AFD-D12 warning).

---

### AFD-T4 (Formation Graph Well-Definedness) — Proposition

**Assumptions.** AFD-T1 holds (V_form ≠ ∅). C_AFD is defined as in AFD-D7.

**Statement.** `G_form = (V_form, E_form, w)` is a well-defined weighted directed graph with V_form ≠ ∅, E_form ⊆ V_form × V_form, and `w : E_form → [0, ∞)`.

**Proof.** V_form ≠ ∅ by AFD-T1. C_AFD : V_form × V_form → [0, ∞] is well-defined by AFD-T5 (next). E_form = {(F_i, F_j) : C_AFD(F_i, F_j) < ∞} is then a well-defined subset of V_form × V_form. w = C_AFD ↾ E_form is a nonneg finite weight. □

---

### AFD-T5 (Abstract Transition Cost Existence) — Theorem

**Assumptions.** Σ_m is compact (Cat A: bounded convex polytope per T-PF-A1-AR). E is continuous on Σ_m. γ is required only to satisfy AFD-D6 (P1)–(P4); rectifiability of γ is *not* assumed.

**Statement.** For any F_i, F_j ∈ V_form with `Adm(F_i, F_j) ≠ ∅`, `C_AFD(F_i, F_j) ∈ [0, +∞)` is well-defined in the minimal version (λ_D = λ_K = 0). For λ_D, λ_K > 0 and rectifiable γ, `J_AFD(γ; F_i) < +∞`.

**Proof sketch.**

(a) E is continuous on compact Σ_m, so E attains finite max and min on Σ_m. Hence `Bar(γ, F_i) ≤ max E − min E < ∞` for any continuous γ.

(b) For the minimal version: `Bar(F_i, F_j) = inf_γ Bar(γ, F_i) ∈ [0, max E − E_F_i] ⊂ [0, ∞)`. Non-negativity follows from `Bar(γ, F_i) ≥ E(γ(0)) − E_F_i ≥ 0` when γ(0) is in cl(B_F_i) (where E ≥ E_F_i locally; for the strict statement at the basin boundary one may take Bar = max(0, ...)). The infimum is over a non-empty admissible class so the value is in [0, +∞).

(c) D is Lipschitz (AFD-T2), so for rectifiable γ, `Var_D(γ) ≤ L_D · length(γ) < ∞`.

(d) K_act takes only finitely many integer values; J_K(γ) = TV(K_act ∘ γ) ≤ 2 K_field for any γ of bounded total variation (since each level can be entered/exited a bounded number of times along a finite-length curve in the semi-algebraic setting; for the formal statement see OP-AFD-002).

(e) Thus J_AFD(γ; F_i) ≤ Bar(γ, F_i) + λ_D L_D length(γ) + 2 λ_K K_field < ∞ for rectifiable admissible γ.

(f) C_AFD ≥ 0 by inspection. □

**Properties (not all are proved here; see audit).**

- C_AFD may be **asymmetric** (Bar is asymmetric).
- `C_AFD(F_i, F_i) = 0` (the constant path γ ≡ u_F_i^* is admissible from F_i to F_i and has J_AFD = 0 in the minimal version).
- C_AFD is **not** in general a metric. Symmetry fails. The **triangle inequality fails** in general because the max-along-path operation in Bar does not concatenate additively. Explicit counterexamples exist on landscapes with three basins arranged so that the direct F_i → F_k path crosses a low ridge but F_i → F_j → F_k must cross two high saddles. The pairwise-min over admissible paths through F_j is therefore not bounded above by C_AFD(F_i, F_j) + C_AFD(F_j, F_k) in general.
- **Infimum attainment** is OPEN (OP-AFD-003); compactness of Σ_m + continuity of E suggests it is attainable via Arzelà-Ascoli on rectifiable curves of bounded length, but for the minimal version (λ_D = λ_K = 0) and continuous (non-rectifiable) admissible class the attainment is non-trivial.

---

### AFD-T6 (Exit-Cost Barrier Preorder) — Proposition

**Statement.** The relation `F_i ≼_bar F_j` ⇔ `ExitCost(F_i) ≥ ExitCost(F_j)` is a **total preorder** on V_form (reflexive, transitive, total). It is **not** antisymmetric: distinct formations may have equal exit cost.

**Proof.** ExitCost : V_form → [0, ∞] is a function with values in a totally-ordered set. Pulling back ≥ yields a total preorder. Reflexivity: ExitCost(F_i) ≥ ExitCost(F_i). Transitivity: ExitCost(F_i) ≥ ExitCost(F_j) ≥ ExitCost(F_k) ⇒ ExitCost(F_i) ≥ ExitCost(F_k). Totality: for any F_i, F_j the real numbers ExitCost(F_i), ExitCost(F_j) are comparable. □

**Warning.** The *pairwise* comparison `C_AFD(F_i, F_j) ⋚ C_AFD(F_j, F_i)` does *not* define a preorder (no transitivity in general). Use only the exit-cost scalar version.

---

### AFD-T7 (K-Stratum Transition Cost) — Proposition

**Definitions.**

> `C_K(K, K') := inf { C_AFD(F_i, F_j) : F_i ∈ S_K ∩ V_form, F_j ∈ S_{K'} ∩ V_form }` (extended-real, ≥ 0).

**Statements.**

- (a) `C_K(K, K') ∈ [0, +∞]`, well-defined.
- (b) `C_K(K, K) = 0` (trivial constant path within a stratum if V_form ∩ S_K is nonempty).
- (c) `C_K(K, K') = +∞` is admissible (no admissible path connecting representatives in the two strata).
- (d) `C_K` is **not symmetric** in general: merge-direction `C_K(K, K−1)` and split-direction `C_K(K−1, K)` differ generically (split barriers are typically higher under gradient flow per T-Merge(b)).

**Lemma Candidate.** For SCC energy with `β/α` sufficiently above β_crit, `C_K(K, K−1) > 0` for all K ≥ 2, with a quantitative lower bound c(β, n, G) > 0. *Status: numerically supported (exp38, exp60 on T^2_{20}); analytic proof OPEN (OP-AFD-004).*

---

### AFD-T8 (EK Compatibility) — Lemma Candidate (Conditional)

**Assumptions.** (Layer-3, all required) H-MORSE-Local + H-MORSE-Saddle + Package I (Cat A) + T_* → 0 small-noise limit (OP-0021).

**Statement.** The mean first-passage time satisfies

> `T_* · log E[τ_{i → j}] → Bar(F_i, F_j)` as T_* → 0,

and therefore the rate ordering matches the barrier ordering:

> `Bar(F_i, F_j) < Bar(F_k, F_l)` ⇔ `E[τ_{i → j}] ≪ E[τ_{k → l}]` (exponential separation as T_* → 0).

**Proof sketch.** Apply FW theory to the gradient reflected SDE on Σ_m (well-posed by T-PF-A1-SDE Cat A). The FW quasipotential `V(u_F_i^*, ·)` along a minimizing instanton equals `E − E_F_i` evaluated at the saddle (gradient SDE identity), which is `Bar(F_i, F_j)`. Then standard Bovier-Eckhoff-Gayrard / Day-Schuss results give the log-scale identification. The reflected-boundary version is in the literature for convex polytopes; full verification for SCC is OP-AFD-005.

**Status.** Lemma Candidate. FW theory itself is standard; the SCC-specific application requires both the H-MORSE inputs (Layer 3) and a reflected-Langevin EK adaptation (literature gap noted in `CV114_H_MORSE_PACKAGEII/06_packageII_dependency_map.md` §2.5).

---

### AFD-T9 (H-MORSE Non-Necessity for AFD) — Theorem

**Statement.** None of the definitions AFD-D1–AFD-D15 and none of the results AFD-T1–AFD-T7 use or require:

- (a) Nondegeneracy of the Hessian at any critical point.
- (b) Existence of an index-1 saddle.
- (c) Hessian determinants.
- (d) Morse-type genericity conditions.

**Proof (by inspection of the definitions and proofs).**

- AFD-D1 requires only "local minimizer". T8-Core (Cat A) gives existence without any nondegeneracy assumption on the Hessian of E.
- AFD-D2 uses constrained gradient-flow convergence; T14 (Łojasiewicz, Cat A) yields convergence to a critical point for *any* analytic E on Σ_m, including degenerate cases.
- AFD-D3 packages the representative, basin, and diagnostics; no Hessian appears.
- AFD-D5 builds a graph from V_form; no Hessian appears.
- AFD-D6–D7 (admissibility, cost) use continuity of E and Lipschitz-ness of D and integer-valued K_act; no Hessian appears.
- AFD-D8 (Bar) is a sup-along-path of E; no Hessian appears.
- AFD-D9–D10 use Var_D (from D Lipschitz, AFD-T2) and J_K (from Commitment 16, Cat A); no Hessian appears.
- AFD-D11 (TopSig) uses CSEH 2007 bottleneck stability; no Hessian appears.
- AFD-D12–D13 (K-strata, K-jumps) use the integer-valued K_act + vineyard set V (from K_soft / persistence machinery); no Hessian appears.
- AFD-D14 (exit-cost preorder) uses Bar only.
- AFD-D15 (EK refinement compatibility) is the *interface* with Layer 3; H-MORSE enters here only to state what *extra* Layer-3 hypotheses are needed for *additional* (prefactor-level) conclusions.
- AFD-T1: uses T8-Core (Cat A, no H-MORSE).
- AFD-T2: uses Predicate-Energy Bridge + A3 + QM3 + CSEH (all Cat A or accepted external; no H-MORSE).
- AFD-T3: uses Commitment 16 (Cat A, no H-MORSE).
- AFD-T4: combinatorial.
- AFD-T5: uses compactness of Σ_m + continuity of E + AFD-T2 + Commitment 16; no H-MORSE.
- AFD-T6: uses real-number order; no H-MORSE.
- AFD-T7: combinatorial from AFD-T5.

Hence (a)–(d) are not used anywhere in AFD-D1..D15, AFD-T1..T7. □

**Corollary.** H-MORSE is a Layer-3 regularity hypothesis, **not** a Layer-2 formation-dynamics axiom.

---

### AFD-T10 (Degeneracy Handling) — Design Principle

**Status.** Design Principle (not a proved theorem). Records the design commitments that allow AFD-0 to gracefully degrade when Layer-3 regularity fails.

**Content.** When critical points are degenerate (zero Hessian eigenvalues, Goldstone modes, D_4-symmetric minimizers, T8-Full bifurcation threshold), AFD-0 can:

- (a) Use deterministic basins `B_det(F)` (AFD-D2); these are well-defined by T14 (Cat A) even at degenerate critical points.
- (b) Replace single representatives by **Conley-style isolated invariant sets** when the critical set is a manifold or a more complicated invariant set (see §12).
- (c) Use **quotient formation states** `[F] = { F' : K_act(F') = K_act(F), τ(F') ≈ τ(F) }`, modding out Aut(G)-orbits when relevant.
- (d) Use **connected components of the set of local minimizers** as formation families (instead of individual representatives).

**Rationale.** T14 guarantees gradient-flow convergence regardless of Hessian rank. The basin AFD-D2 is therefore intrinsically well-defined. Conley index theory rigorously handles the cases where Morse decomposition fails. Persistence machinery (QM3) is stable under bar-length degeneracy (CSEH).

**Note.** Aut(G) quotienting and connected-component-of-minimizers refinements are the natural follow-up; both intersect OP-0008 / OP-0009 and are deferred to AFD-1 / AFD-Conley.

## 15. Examples

See `afd_examples.md` for seven worked examples on small grids (3×3, 4×4, 5×5).

## 16. Limitations

- AFD-0 is **not** a quantitative rate theory. Use Layer 3 (when H-MORSE holds) for actual rates.
- AFD-0 does **not** define dynamics on G_form itself (no jump process specified). Layer 3 (EK / Bovier-Eckhoff-Gayrard) does, asymptotically.
- AFD-0 uses raw representatives, not equivalence classes; D_4-symmetric / Goldstone families currently produce a continuum of formation states which are abstractly distinct but ought to be identified physically. AFD-D4 sketches the equivalence-class refinement; full treatment is deferred.
- AFD-0 does not resolve any open SCC problem (OP-0005, OP-0006-extensions, OP-0008, OP-0009, OP-0021). It is a *language* for stating those problems more crisply at Layer 2.

## 17. Open Problems

See `afd_open_problems.md` for the full list. OP-AFD-001 through OP-AFD-010.

## 18. Summary

AFD-0 provides:

- A precise definition of *formation state* (AFD-D3) built entirely on Cat A Layer-1 inputs.
- A *formation-state graph* `G_form` (AFD-D5) with a well-defined abstract transition cost `C_AFD` (AFD-D7).
- A barrier preorder `≼_bar` (AFD-D14) that is a total preorder (AFD-T6).
- A K-stratum decomposition (AFD-D12) and K-jump event structure (AFD-D13) keyed to the vineyard set V from K_soft / persistence machinery.
- Explicit compatibility hooks with FW (§11), Conley (§12), and Eyring-Kramers (§13, AFD-D15, AFD-T8).
- A proof that AFD-0 does not require H-MORSE (AFD-T9), formalizing the reclassification of H-MORSE as a Layer-3 hypothesis.

This positions AFD-0 as the natural target for canonical promotion once internal review and one round of external audit have completed. Promotion candidates (in order of confidence):

1. AFD-T9 (Theorem, by-inspection; the central claim of AFD-0).
2. AFD-D1, AFD-D2, AFD-D3, AFD-D5 (the formation state and graph apparatus).
3. AFD-T1 (Proposition; restatement of T8-Core in AFD language).
4. AFD-T6 (Proposition; barrier preorder).

AFD-T2, AFD-T5 require assembly of finer Cat A constants and are recommended for second-round promotion. AFD-T8 (EK compatibility) is and remains a Layer-3 conditional and should not be promoted ahead of CV-1.14 / Package II.
