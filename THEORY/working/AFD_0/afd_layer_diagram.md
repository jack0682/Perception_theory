---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

# AFD-0 — Three-Layer Architecture Diagram

```
================================================================
Layer 1 — SCC Core
================================================================
  Field            u : X_t -> [0,1],  u in Sigma_m = {sum u_i = m}
  Energy           E(u) = lambda_cl E_cl + lambda_sep E_sep + lambda_bd E_bd
  Operators        Cl (closure, A3 contraction), D (distinction), C (co-belonging)
  Diagnostics      D(u) = (Bind, Sep, Inside, Persist) in [0,1]^4
  K-notions        K_field (architectural cap), K_act (active count, Commitment 16, Cat A)
                   K_soft (persistence-weighted soft count, QM3 Cat A)

  Cat A results used by AFD-0:
    T8-Core         non-trivial minimizer exists when beta/alpha > 4 lambda_2 / |W''(c)|
    T14             gradient flow Lojasiewicz convergence
    T-Merge(b)      K=1 is global energy minimum
    T-Persist-1(b)  basin radius r_basin = sqrt(2 Delta_min / lambda_max)
    T7-Enhanced     enhanced metastability gap
    P-F-A1 Pkg I    AR / SDE / GI / PE  (reflected Langevin, Gibbs, Poincare)
    QM3             K_soft Lipschitz on Sigma_m
    Commitment 16   K_act integer-valued, derived diagnostic
    T-Temp-Identity CV-1.13, all 4 parts Cat A
    Pred-E Bridge   Sep = 1 - E_sep / m
================================================================
                              |
                              |  builds on
                              v
================================================================
Layer 2 — Abstract Formation Dynamics (AFD-0)   [NEW, this directory]
================================================================
  Formation State    F = (u_F^*, B_F, d_F, K_F, tau_F, E_F)
                       u_F^* = local minimizer (AFD-D1)
                       B_F   = deterministic basin (AFD-D2)
                       d_F   = D(u_F^*) diagnostic vector
                       K_F   = K_act(u_F^*) integer
                       tau_F = H0 persistence diagram of u_F^*
                       E_F   = E(u_F^*)

  Formation State Graph     G_form = (V_form, E_form, w)   (AFD-D5)
  Abstract Transition Cost  C_AFD(F_i, F_j)                (AFD-D7)
  Barrier (asymmetric)      Bar(F_i, F_j)                  (AFD-D8)
  Diagnostic Variation      Var_D(gamma)                   (AFD-D9)
  K-Jump Cost               J_K(gamma)                     (AFD-D10)
  Topology Signature        tau(u), d_top                  (AFD-D11)
  K-Strata                  S_K = {u : K_act(u) = K}       (AFD-D12)
  K-Jump Events             vineyard crossings             (AFD-D13)
  Barrier Preorder          F_i <=_bar F_j via ExitCost    (AFD-D14)
  EK Compatibility hook     AFD-D15

  Key Layer-2 facts:
    AFD-T1    V_form non-empty
    AFD-T2    D Lipschitz
    AFD-T3    K_act set-theoretic decomposition
    AFD-T4    G_form well-defined
    AFD-T5    C_AFD in [0, +inf) for admissible pairs
    AFD-T6    ExitCost preorder is total preorder
    AFD-T7    K-stratum transition cost
    AFD-T9    AFD does NOT require H-MORSE        <-- key result
================================================================
                              |
                              |  optional refinement
                              v
================================================================
Layer 3 — Refined Stochastic Rate Theory   [H-MORSE required]
================================================================
  H-MORSE-Local   Hessian at each min is nondegenerate on T Sigma_m
  H-MORSE-Saddle  Hessian at each index-1 saddle is nondegenerate on T Sigma_m
  EK prefactor    A_ij = (|lambda^-_saddle| / 2 pi) sqrt(|det H_sad^proj| / det H_min^proj)
  Exact rate      r_ij = A_ij exp(-Bar(F_i,F_j) / T_*) (1 + O(T_*))
  Package II      T-P-F-eps0-K Cat B -> Cat A target, D-ST-4 sector machinery

  Layer-3 status (2026-05-12):
    H-MORSE-Local   Cat B target (CV-1.14)
    H-MORSE-Saddle  not yet registered
    EK formula      literature available, needs reflected-Langevin adaptation
================================================================
```

## What each layer provides

| Quantity | Layer | Need H-MORSE? |
|---|---|---|
| Existence of local minimizer u_F^* | 1 (T8-Core) | No |
| Basin B_F | 2 (AFD-D2) | No |
| Diagnostic vector d_F | 1 + 2 (AFD-T2) | No |
| K_act(u_F^*) | 1 (Commitment 16) | No |
| Persistence diagram tau_F | 1 (QM3) | No |
| Barrier height Bar(F_i, F_j) | 2 (AFD-D8) | No |
| Barrier ordering | 2 (AFD-T6) | No |
| Reflected Langevin well-posedness | 1 (Pkg I) | No |
| Gibbs invariant measure | 1 (T-PF-A1-GI) | No |
| **Exact rate prefactor A_ij** | **3** | **Yes** |
| **Exact mean first-passage time** | **3** | **Yes (+ FW)** |

## Slogan

> **AFD separates transition order from transition rate.**
> EK refines AFD; AFD does not require EK.
> H-MORSE is a Layer-3 regularity hypothesis, not a Layer-2 axiom.
