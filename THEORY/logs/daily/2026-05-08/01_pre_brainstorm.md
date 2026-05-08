---
type: log/daily
date: 2026-05-08
session: pre-Session-5 brainstorm
---

# Pre-brainstorm — Strategy Notes

## Why $u^*(\lambda)$ regularity is the right next attack

The Session-4 finding (OP-OMS-001 partially constrained, OP-OMS-002 partially supported, OMS-1.1) leaves OP-OMS-018 as the formal pivot:

- The basin / gradient-flow / RG analyses of OMS depend on $u^*(\lambda)$ being smooth somewhere.
- VP-1 / VP-4 already showed that $u^*$ jumps at branch boundaries (different $K_{\mathrm{core}}$), so a **global** $C^1$ statement is wrong.
- A **local** $C^1$ statement should follow from the implicit function theorem applied to the KKT system $\nabla_u E_\lambda(u^*) + \nu \mathbf{1} = 0$, $\mathbf{1}^\top u^* = m$.

## VP-6 design choices

- Build $R_{\mathrm{vec}}(\lambda) \in \mathbb{R}^p$ from the **smooth** components of $P_{\mathrm{top}}$ only — exclude $K_{\mathrm{core}}$, $n_{\mathrm{high}}$ (discrete; jumps at $\Sigma_{\mathrm{branch}}$).
- Tangent basis on $\Delta^3$: orthonormal columns of the 4 → 3 reduction (Gram–Schmidt of $\{e_i - e_4\}$).
- Centered finite-difference Jacobian, $h = 10^{-3}$.
- Flag stencils where the FD pair lands on different branches (branch-id jump).

## Reduction-C strategy for OP-OMS-001

If the energy-decomposition map $e(\lambda) := (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*(\lambda))$ is locally injective on the simplex tangent, then any candidate gauge $g \in G_{\mathrm{cw}}$ with $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ on a regular set must be the identity (envelope theorem).

Local injectivity = full rank of the energy-decomposition Jacobian on the simplex tangent. By the bordered-Hessian argument, this Jacobian has the explicit form

$$J_e = -G_T^\top H_T^{-1} G_T,$$

where $G$ is the matrix of energy gradients, $H$ is the Hessian of $E_\lambda$, and $T$ is the tangent space of $\Sigma_m$.

This is the **structural target** of the Gap C1 chain (later worked out in detail in Session-6 Gate 1).

## Targets for the day

| Topic | Mechanism | Output |
|---|---|---|
| VP-6 effective DOF | FD Jacobian + SVD | json + md per scene |
| $u^*$ regularity | IFT + Berge + envelope | proofs R1–R5 |
| Σ_branch existence | Constructive: K_core flips at saddle | from VP-1/VP-4 |
| Effective DOF theory | DEF-ED1..ED4 + Props ED1, ED2 | effective_dof_theory.md |
| Open problems registered | OP-OMS-024, 025, 026 | open_problems.md update |

## Preview: Gates 1–8 brainstorm (anticipated for Session 6)

If the day unfolds as expected, Session 6 should attack the three hard
OMS-2.0 blockers via **theorem + computational witness**. The cleanest
path:

- OP-OMS-001 → Gap C1 (analytic genericity of energy-gradient rank).
- OP-OMS-002+ → soft-min of two distance functionals: $V_2(\lambda) = \min\{D_1, D_2\}$.
- OP-OMS-026 → branch-energy difference + envelope theorem ⇒ codim-1.

The key insight is that all three reduce to **single-witness analytic
genericity** + **codim-1 surface** arguments, which can be implemented
computationally on small graphs ($P_{12}$, S3, asymmetric K4+tail).

This brainstorm was prophetic — it's exactly what Gates 1–6 implemented.
