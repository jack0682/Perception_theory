---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

# AFD-0 Theorem Registry

Tabular index of AFD-0 results. Cross-references to Layer-1 (Cat A) dependencies and open gaps.

## AFD Theorems

| ID | Name | Statement (brief) | Status | Dependencies (Layer 1, Cat A) | Gaps / Open | File |
|---|---|---|---|---|---|---|
| **AFD-T1** | Existence of Formation States | V_form ≠ ∅ when β/α > 4 λ_2 / \|W''(c)\| | Proposition (proved from Cat A) | T8-Core | none | `abstract_formation_dynamics.md` §14 |
| **AFD-T2** | Diagnostic Map Continuity | D = (Bind, Sep, Inside, Persist) is Lipschitz on Σ_m | Theorem (assembly of Cat A) | Pred-E Bridge, A3 closure, QM3, CSEH 2007 | exact Lipschitz constants for Inside, Persist need bookkeeping | §14 |
| **AFD-T3** | K-Act Decomposition | Σ_m = ⊔ S_K is a set-theoretic disjoint partition | Proposition (proved from Cat A) | Commitment 16, D-ST-3 | S_K is NOT proved a smooth/Whitney stratum (warning) | §14 |
| **AFD-T4** | Formation Graph Well-Definedness | G_form = (V_form, E_form, w) is a well-defined weighted directed graph | Proposition | AFD-T1, AFD-T5 | none | §14 |
| **AFD-T5** | Abstract Transition Cost Existence | C_AFD(F_i, F_j) ∈ [0, +∞) for admissible pairs | Theorem | Σ_m compact (T-PF-A1-AR), E continuous, AFD-T2, Commitment 16 | infimum attainment (OP-AFD-003); J_K bound proof | §14 |
| **AFD-T6** | Exit-Cost Barrier Preorder | ≼_bar via ExitCost is a total preorder | Proposition | ℝ total order | warning: pairwise C_AFD does NOT yield a preorder | §14 |
| **AFD-T7** | K-Stratum Transition Cost | C_K(K, K') is well-defined; not symmetric; **C_K(K,K−1) ≥ 0.0221β > 0** (Cat B, cond.) | Proposition + **Cat B Proposition** | AFD-T5, T-Persist-1(b) Cat A, T8-Core Cat A, T-Merge(b) Cat A | Cat B cond. on H1-H4+WS+SR; tight exponent open (OP-AFD-004a, Layer 3) | §14 + `op_afd_004_proof.md` |
| **AFD-T8** | EK Compatibility | T_* log E[τ_{i→j}] → Bar(F_i, F_j) under H-MORSE + small noise | Lemma Candidate (Conditional, Layer 3) | T-PF-A1-SDE/GI/PE, H-MORSE-Local + Saddle (Layer 3), T_* axiom | full proof = OP-AFD-005; H-MORSE Cat B / unregistered (Layer 3) | §14 |
| **AFD-T9** | H-MORSE Non-Necessity | AFD-D1..D15 and AFD-T1..T7 do not use H-MORSE | **Theorem** (proved by inspection) | (inspection of definitions and proofs) | none | §14 |
| **AFD-T10** | Degeneracy Handling | Strategies for degenerate critical sets | Design Principle | T14 Lojasiewicz, Conley (external) | full Conley-AFD layer = AFD-1 follow-up | §14 |

## Layer-1 (Cat A) inputs used by AFD-0

| Layer-1 result | AFD-0 use | Source |
|---|---|---|
| T8-Core | AFD-T1 existence | `canonical.md` §13 Cat A |
| T14 Lojasiewicz | AFD-D2 basin well-definedness; AFD-T10 | §13 Cat A |
| T-Merge(b) | K=1 global min, AFD-T7 split-barrier asymmetry | §13 Cat A |
| T-Persist-1(b) | basin-radius lower bound for AFD-D2; relates to OP-AFD-004 | §13 Cat A |
| T7-Enhanced | enhanced metastability gap; used in OP-AFD-004 conjecture | §13 Cat A |
| P-F-A1 Pkg I (AR/SDE/GI/PE) | Σ_m polytope, stochastic basin AFD-D2', §11 FW reduction | §13 Cat A (CV-1.8–1.9) |
| QM3 (K_soft Lipschitz) | AFD-T2 (Inside), AFD-D11 (τ stability via CSEH) | §13 Cat A |
| Commitment 16 (K_field / K_act) | AFD-D3, AFD-D10, AFD-D12, AFD-T3, AFD-T7 | §11.1 |
| T-Temporal-Identity | AFD-D3 τ tracking under transport (compatibility with R_{t→s}) | §13 Cat A (CV-1.13) |
| Predicate-Energy Bridge | AFD-T2 (Sep Lipschitz) | §13 Cat A |
| CSEH 2007 bottleneck stability | AFD-D11, AFD-T2 (Inside, Persist) | external |

## Layer-3 (NOT used in AFD-0) — for reference

| Layer-3 hypothesis | Status | Where it is needed (NOT in AFD-0) |
|---|---|---|
| H-MORSE-Local | Cat B target (CV-1.14) | EK prefactor det(H_min); AFD-T8 |
| H-MORSE-Saddle | not registered | EK prefactor det(H_sad); AFD-T8 |
| EK adapted to reflected Langevin | literature gap | exact rate; AFD-T8 prefactor |
| FW quasipotential identification | OP-AFD-005 | log-rate identification; AFD-T8 |
| T_* small-noise axiom | OP-0021 | AFD-T8 |

## Status-label legend

- **Definition**: notational commitment.
- **Proposition**: short proof from Cat A inputs or by inspection.
- **Theorem**: substantive claim with full proof from Cat A inputs.
- **Lemma Candidate**: plausible, sketched, full proof OPEN.
- **Conjecture**: stated, no proof attempted.
- **Design Principle**: architectural commitment, not a proved theorem.
- **Open Problem**: explicit gap, to be addressed in future work.
- **Warning**: clarification preventing overclaim.

## Promotion recommendation (suggested order, see main doc §18)

1. AFD-T9 — central, by-inspection, no gaps.
2. AFD-D1, AFD-D2, AFD-D3, AFD-D5 — definitions, used by everything.
3. AFD-T1 — restatement of T8-Core in AFD language.
4. AFD-T6 — barrier preorder.
5. AFD-T3 — K-stratum decomposition.

Hold for second round:
- AFD-T2 (need explicit Lipschitz constants).
- AFD-T5 (need OP-AFD-003 resolved or restated as conditional).
- AFD-T7 **Cat B Proposition now resolved** (OP-AFD-004 Cat B, 2026-05-12) — promote in R2 conditional on H1-H4+WS+SR.

Do **not** promote AFD-T8 ahead of CV-1.14 (H-MORSE-Local Cat B) — it is and remains Layer-3 conditional.
