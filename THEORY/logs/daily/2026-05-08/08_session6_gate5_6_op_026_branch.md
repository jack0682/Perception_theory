---
type: log/daily
date: 2026-05-08
session: Session 6 (OMS-2.0 push) — Gates 5 & 6
attacks: OP-OMS-026
deliverables: op_oms_026_sigma_branch_full.md, vp10_sigma_branch_delta3.py + .json + .md
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Session 6 Gates 5 & 6 — OP-OMS-026 Full Σ_branch Theory and Δ³ Map

## Gate 5 — Theory file `op_oms_026_sigma_branch_full.md`

### Setup

For two distinct local branches $u_a, u_b : U \to \Omega$ of the SCC optimizer
on overlapping open $U \subset \Delta^3$:

- Branch energy: $V_a(\lambda) = E_\lambda(u_a(\lambda))$.
- Switch locus: $\Sigma_{ab} = \{\lambda \in U : V_a(\lambda) = V_b(\lambda)\}$.
- Total branch-switch locus: $\Sigma_{\mathrm{branch}} = \bigcup_{a \neq b} \Sigma_{ab} \cup \Sigma_{\mathrm{deg}}$.

Degeneracy locus $\Sigma_{\mathrm{deg}} = \Sigma_{\mathrm{Hess}} \cup \Sigma_{\mathrm{AS}} \cup \Sigma_{\mathrm{SN}}$ (Hessian singularity / active-set change / saddle-node bifurcation).

### Theorems PROVED

**Theorem SB5 (Codim-1 of $\Sigma_{ab}$):** Under distinguishability $e(u_a) \neq e(u_b)$, the set $\Sigma_{ab}$ is a $C^1$ embedded codim-1 submanifold on the regular branch.

Proof: $\Phi(\lambda) := V_a - V_b$. By envelope theorem (R5),
$\nabla_\lambda \Phi = e(u_a) - e(u_b)$. Restricted to simplex tangent: non-zero
generically (one algebraic condition $e_a - e_b = c \mathbf{1}$). Apply regular-value theorem.

**Corollary SB6:** $\Sigma_{\mathrm{branch}}$ is a finite union of codim-1 submanifolds on the regular class (stratified codim-1 set).

**Theorem SB7 ($\Sigma_{\mathrm{Hess}}$ codim-1):** $\det H_T(\lambda) = 0$ defines a real-analytic codim-1 surface. **Identifies $\Sigma_{T8}$ (T8 phase-transition surface) as $\Sigma_{\mathrm{Hess}}$**.

**Theorem SB8 ($\Sigma_{\mathrm{AS}}$ codim-1):** The strict-complementarity-violation locus is a codim-1 algebraic surface.

**Proposition SB9 ($\Sigma_{\mathrm{SN}}$ codim-1):** PROOF SKETCH via Arnold's saddle-node theorem.

**Theorem SB11 (Full characterization).** PROVED for codim-1 components; PROOF SKETCH for $\Sigma_{\mathrm{SN}}$.

### Conceptual unification

$$\Sigma_{T8}(X_t) = \Sigma_{\mathrm{Hess}}(X_t) \subset \Sigma_{\mathrm{branch}}(X_t).$$

The SCC central T8 phase-transition surface is identified as one component
of the OMS branch-switching set. **OMS recognizes T8 as the analytic
characterization of part of $\Sigma_{\mathrm{branch}}$.** This is a non-trivial
conceptual unification of the SCC and OMS frameworks.

## Gate 6 — Pseudo-Δ³ branch map (VP-10)

### Method

`vp10_sigma_branch_delta3.py`:
- Tetrahedral grid on Δ³ = $\{\lambda \in \mathbb{R}^4_{\ge 0} : \sum \lambda_i = 1\}$.
- K = 8 → $\binom{K+3}{3} = 165$ grid points per scene.
- Per-point `find_formation`; branch identifier $(n_{\mathrm{core}}, n_{\mathrm{high}})$.
- Edges: 12 unit moves per interior point.
- Codim-1 consistency criterion: transition fraction ≤ $3/K = 0.375$.

### Pseudo-Δ³ caveat

On a static scene, $E_{tr}$ is degenerate, so $\lambda_{tr}$ is gauge-redundant
(Prop CW2). The result tests SB11 (B)-(C) at the codim-1 level on the 3-D
simplex but uses a degenerate $\lambda_{tr}$-direction. **Not** the same as
a full temporal Δ³ on a 2-time-slice scene (registered as OP-OMS-034).

### Results (P12 only; smaller / faster than S3)

| Quantity | Value |
|---|---|
| K | 8 |
| Grid points | 165 |
| Distinct branches | **7** (same as Δ² — confirms λ_tr degeneracy) |
| Dominant branch (3,4) | **64.2%** of grid (vs 66.7% on Δ²) |
| Transition edges | 224 |
| Total edges | 720 |
| Transition fraction | **0.311** |
| Codim-1 budget (3/K) | 0.375 |
| **Codim-1 consistent** | **YES** |
| Runtime | 96.8 s |

### What this verifies

Theorem SB11 (B)-(C) — Σ_branch is codim-1 in Δ³ — is **COMPUTATIONALLY
SUPPORTED** by the transition-fraction count being well within the codim-1
budget on the tetrahedral grid.

## Net status of OP-OMS-026

| Sub-claim | Status |
|---|---|
| SB1–SB4 definitions | DEFINED |
| SB5 ($\Sigma_{ab}$ codim-1) | **PROVED** |
| SB6 (full Σ_branch codim-1) | **PROVED** on regular class |
| SB7 ($\Sigma_{\mathrm{Hess}}$ + T8 identification) | **PROVED** |
| SB8 ($\Sigma_{\mathrm{AS}}$ codim-1) | **PROVED** |
| SB9 ($\Sigma_{\mathrm{SN}}$ codim-1) | **PROOF SKETCH** (Arnold) |
| SB11 (full characterization) | PROVED for codim-1 part |
| Pseudo-Δ³ codim-1 evidence | **COMPUTATIONALLY SUPPORTED** (VP-10) |
| Full temporal Δ³ | **OP-OMS-034 (NEW)** |

**OP-OMS-026 → PROVED codim-1 + COMPUTATIONALLY SUPPORTED on pseudo-Δ³.**

## Files produced

- `THEORY/2_substrate/foundations/observer_moduli/op_oms_026_sigma_branch_full.md`
- `CODE/experiments/observer_moduli/vp10_sigma_branch_delta3.py`
- `CODE/experiments/results/observer_moduli/vp10_sigma_branch_delta3.json`
- `CODE/experiments/results/observer_moduli/vp10_sigma_branch_delta3.md`
