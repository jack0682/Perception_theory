---
type: working/afd/v_afd
status: V-AFD Draft v0.1 (2026-05-12)
---

# V-AFD Theorem Registry

Tabular index of V-AFD results. Cross-references to Layer-1 (Cat A) dependencies, AFD-0 dependencies, and open gaps.

## V-AFD Definitions

| ID | Name | Object | File anchor |
|---|---|---|---|
| V-AFD-D1 | Diagnostic Vector | `D(u) = (Bind, Sep, Inside, Persist) ∈ [0,1]⁴` (static + temporal forms) | main §3 |
| V-AFD-D1' | Persist (pairwise) | `Persist_pair(u, v, M)` via core-overlap under transition operator | main §3 |
| V-AFD-D1'' | Persist (window) | `Persist_W({u_t})` infimum over window | main §3 |
| V-AFD-D2 | Enriched Vector State | `Z(u) = (D, K_act, E, τ) ∈ 𝒵` | main §3 |
| V-AFD-D3 | Vector Formation State | `Z_F = Z(u_F^*)` and tolerance class `[F]_Z^ε` | main §3 |
| V-AFD-D4 | Vector Trajectory | `z_γ(s) = Z(γ(s))` along admissible γ | main §3 |
| V-AFD-D5 | Vector Transition | `Z_i ⇒ Z_j` via admissible γ with finite `C_V` | main §3 |
| V-AFD-D6 | Vector Transition Cost | `C_V = λ_E Bar + λ_D Var_D + λ_K J_K + λ_τ Var_τ + λ_L Len` | main §3 |
| V-AFD-D7 | Vector Stability | `Stab_V(F) = a·ExitCost + b·Q − c·LocalSensitivity` | main §3 |
| V-AFD-D8 | Pareto Preorder | `≼_D` componentwise on diagnostic vectors | main §3 |
| V-AFD-D9 | Scalarization (optional) | `Q_w(D)`, `L_w(D) = 1 − Q_w(D)` | main §3 |
| V-AFD-D10 | K-Vector Dynamics | K-stratum `S_K^Z`, K-jump events, merge/split labels | main §3 |
| V-AFD-D11 | Vector Formation Graph | `G_V = (V_Z, E_Z, w_Z)` | main §3 |
| V-AFD-D12 | Projection / Quotient | `π_Z : V_form → V_Z` surjection; fibers | main §3 |

## V-AFD Theorems and Propositions

| ID | Name | Statement (brief) | Status | Dependencies (Layer 1 + AFD-0 Cat A) | Gaps / Open | File anchor |
|---|---|---|---|---|---|---|
| **V-AFD-T1** | Diagnostic Vector Well-Definedness | `D(u) ∈ [0,1]⁴` is well-defined for all `u ∈ Σ_m` (static placeholder + pairwise forms) | **Proposition** (Cat A by inspection) | canonical §7.2: Bind/Sep/Inside; T-Temporal-Identity Cat A: Persist forms | none | main §4 |
| **V-AFD-T2** | Diagnostic Pareto Preorder | `≼_D` is reflexive, transitive, not total, antisymmetric mod equal vector | **Proposition** (Cat A) | componentwise order on `[0,1]⁴` | none | main §4 |
| **V-AFD-T3** | Scalar Diagnostic Lyapunov Candidate | `L_w(D(u))` is well-defined Lipschitz; monotonic decrease along gradient flow is **not** generally true | **Proposition** (well-def Cat A) + **Conjecture** (monotonicity) | AFD-T2 D Lipschitz | conditions for monotonicity (OP-VAFD-006 refinement) | main §4 |
| **V-AFD-T4** | Vector Trajectory Existence by Projection | `z_γ` is càdlàg on `[0,1]`; D∘γ Lipschitz, K_act∘γ piecewise constant, E∘γ continuous, τ∘γ continuous in d_B | **Theorem** (Cat A) | AFD-T2 Cat A, Commitment 16 Cat A, CSEH 2007 | sorted-bar reordering discontinuity is càdlàg only | main §4 |
| **V-AFD-T5** | BV Under Lipschitz Diagnostic | For rectifiable γ: `Var(D∘γ) ≤ L_D · Len(γ)`; analogous bounds for τ, E, K | **Theorem** (Cat A) | AFD-T2 Cat A, CSEH 2007 Cat A, E continuous, Commitment 16 | L_D, L_E numerical bookkeeping per AFD-T2 caveat | main §4 |
| **V-AFD-T6** | Vector Transition Cost Well-Definedness | `C_V(F_i, F_j) ∈ [0, +∞]`; in minimal version `C_V = Bar = C_AFD^min` is finite | **Theorem** (Cat A) | AFD-T5 (finiteness) Cat A, T-PF-A1-AR Cat A, AFD-T2 Cat A | attainment is V-AFD-T6' | main §4 |
| **V-AFD-T6'** | Vector Transition Cost Attainment (Conditional) | `C_V` infimum attained by Lipschitz γ_* of bounded length | **Theorem modulo Claim B.3** (Cat A pending o-minimal citation) | T-OP-AFD-003-A this session, Claim B.3 (uniform o-minimal diameter) | Claim B.3 verification (OP-AFD-003a-revised) | main §4 |
| **V-AFD-T7** | V-AFD Does Not Require H-MORSE | V-AFD-D1..D12 + V-AFD-T1..T11 do not use H-MORSE-Local, H-MORSE-Saddle, Hessian det, Morse genericity | **Theorem** (by-inspection) | (inspection of definitions and proofs) | none | main §4 |
| **V-AFD-T8** | EK Compatibility as Refinement | Under Layer-3 hypotheses (H-MORSE + Pkg I + T_*), `T_* log E[τ_{i→j}] → λ_E^{-1} · C_V^min` | **Lemma Candidate** (Conditional, Layer 3 — inherited from AFD-T8) | AFD-T8 conditions; OP-AFD-005 reflected-Langevin EK | full proof = OP-AFD-005; H-MORSE Cat B / unregistered | main §4 |
| **V-AFD-T9** | Vector Projection Information Loss | `π_Z` is non-injective; symmetric / Goldstone / topologically-coincident examples | **Theorem** (existence of CE by construction) | Aut(G)-equivariance of SCC operators (canonical §3 Cat A) | characterization of *when* loss matters (OP-VAFD-004) | main §4 |
| **V-AFD-T10** | K-Jump Detection in Vector Dynamics | For transversal rectifiable γ: K_act∘γ piecewise constant with finite jump count | **Proposition** (Cat B modulo OP-AFD-002 reach lower bound) | Commitment 16 Cat A, vineyard codim-1 | OP-AFD-002 (reach of V); non-transversal γ (OP-VAFD-007) | main §4 |
| **V-AFD-T11** | Vector Graph as Quotient of Formation Graph | `G_V = G_form / ~_Z`; edges collapse with inf-cost aggregation | **Proposition** (by-construction Cat A) | AFD-D5 G_form; AFD-T4 well-definedness | aggregation-choice variants (OP-VAFD-010) | main §4 |
| **V-AFD-T12** | Markovianity of Vector Dynamics | When is `t ↦ z(t)` Markov or lumpable? | **Open Problem** (OP-VAFD-003) | — | full characterization open | main §4 |

## Layer-1 (Cat A) inputs used by V-AFD

| Layer-1 result | V-AFD use | Source |
|---|---|---|
| Predicate-Energy Bridge | V-AFD-D1 Sep, V-AFD-T5 Lipschitz | canonical §13 Cat A |
| A3 (closure contraction) | V-AFD-D1 Bind, V-AFD-T5 Lipschitz | canonical §13 Cat A |
| QM3 (K_soft Lipschitz) | V-AFD-D1 Inside, V-AFD-D2 τ via persistence | canonical §13 Cat A |
| CSEH 2007 (bottleneck stability) | V-AFD-D2 τ-coordinate, V-AFD-T4 d_B-continuity, V-AFD-T5 L_τ ≤ 1 | external accepted |
| Commitment 16 (K_field / K_act) | V-AFD-D2 K-coord, V-AFD-D10 K-stratum, V-AFD-T10 jumps | canonical §11.1 Cat A |
| T8-Core | V-AFD inherits V_form ≠ ∅ via AFD-T1 | canonical §13 Cat A |
| T14 Łojasiewicz | V-AFD inherits basin def via AFD-D2 | canonical §13 Cat A |
| T-Temporal-Identity (4 parts) | V-AFD-D1' pairwise Persist, V-AFD-D1'' window | canonical §13 CV-1.13 Cat A |
| T-Persist-1(b) | V-AFD inherits AFD-T7 Cat B basin radius bounds | canonical §13 Cat A |
| T-PF-A1-AR (Σ_m compact polytope) | V-AFD-T6 finiteness, V-AFD-T6' compactness | canonical §13 Cat A (CV-1.8) |
| T-PF-A1-SDE/GI/PE | V-AFD-T8 reflected Langevin (Layer 3 only) | canonical §13 Cat A (CV-1.9) |

## AFD-0 inputs used by V-AFD

| AFD-0 input | V-AFD use |
|---|---|
| AFD-D1 (Formation Representative) | V-AFD inherits unchanged |
| AFD-D2 (Basin, deterministic) | V-AFD inherits unchanged |
| AFD-D3 (Formation State tuple) | V-AFD-D3 reformulation |
| AFD-D5 (G_form) | V-AFD-D11 quotient base |
| AFD-D6 (Admissible Path) | V-AFD inherits unchanged |
| AFD-D7 (C_AFD) | V-AFD-D6 extends |
| AFD-D8 (Bar) | V-AFD inherits unchanged |
| AFD-D9 (Var_D) | V-AFD-D6 includes |
| AFD-D10 (J_K) | V-AFD-D6 includes |
| AFD-D11 (TopSig distance) | V-AFD-D2 τ-coordinate |
| AFD-D14 (≼_bar) | V-AFD-D8 refines (Pareto) |
| AFD-T2 (D Lipschitz) | V-AFD-T5 trajectory-level BV |
| AFD-T5 (finiteness) | V-AFD-T6 inherits |
| T5-Strong / AFD-T11 (attainment) | V-AFD-T6' inherits |
| AFD-T6 (≼_bar preorder) | V-AFD-T2 alternate / finer |
| AFD-T7 (C_K positivity Cat B) | V-AFD inherits, applies to vector merge cost |
| AFD-T8 (EK Compatibility) | V-AFD-T8 reformulation |
| AFD-T9 (H-MORSE Non-Necessity) | V-AFD-T7 (lifted to vector language) |

## Layer-3 (NOT used in V-AFD) — for reference

Same list as AFD-0: H-MORSE-Local Cat B, H-MORSE-Saddle unregistered, reflected-Langevin EK literature gap, FW quasipotential identification (OP-AFD-005), T_* axiom (OP-0021). V-AFD-T8 *interfaces* with these as a Layer-3 conditional; V-AFD-T1..T7 + V-AFD-T9..T11 do **not** use any of them.

## Status-label legend

- **Definition**: notational commitment, no proof obligation.
- **Proposition**: short proof from Cat A inputs or by inspection.
- **Theorem**: substantive claim with full proof from Cat A inputs.
- **Lemma Candidate**: plausible, sketched, full proof OPEN.
- **Conjecture**: stated, no proof attempted.
- **Open Problem**: explicit gap, registered in `v_afd_open_problems.md`.
- **Conditional**: holds only under named hypotheses (e.g. Layer-3 H-MORSE).
- **modulo Claim X**: Cat A pending verification of a specific cited fact.

## Promotion (none recommended at this stage)

V-AFD is a **working-layer reformulation** of AFD-0 in vector language. No V-AFD result is recommended for direct canonical promotion at this round. Promotion candidates that piggyback on AFD-0 promotion:

- V-AFD-T2 (Pareto preorder) — could enter canonical as a companion to AFD-T6 (≼_bar).
- V-AFD-T7 (H-MORSE Non-Necessity, vector version) — companion to AFD-T9.

These would be optional additions to AFD R1 promotion, not blockers.

## Cross-link to OPs

See `v_afd_open_problems.md` for OP-VAFD-001..010 and their relations to OP-AFD-001..010.
