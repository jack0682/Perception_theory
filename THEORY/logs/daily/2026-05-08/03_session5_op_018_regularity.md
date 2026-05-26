---
type: log/daily
date: 2026-05-08
session: Session 5 (theoretical)
attacks: OP-OMS-018
deliverables: op_oms_018_regular_u_star.md, vp6_u_star_regular_path_test.py
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Session 5 — OP-OMS-018 Partial Resolution

## Setup

For fixed scene $X_t$:

$$E_\lambda(u) = \sum_{i \in \{cl, sep, bd, tr\}} \lambda_i E_i(u; X_t),$$

affine in $\lambda$, **non-convex in $u$** (double-well boundary term has spinodal directions).
Domain $\Omega = \Sigma_m \cap [0,1]^n$.
Argmin $S(\lambda) = \mathrm{Argmin}_{u \in \Omega} E_\lambda(u)$.
Value function $v(\lambda) = \min_{u \in \Omega} E_\lambda(u)$.

## Six theorems PROVED

| ID | Statement | Method |
|---|---|---|
| **R1** | Local interior $C^1$ branch at non-degenerate min | bordered-Hessian + IFT |
| **R2** | Local boundary $C^1$ on fixed active set | Robinson–Fiacco parametric NLP |
| **R3 (1)–(2)** | $S$ u.h.c.; $v$ continuous | Berge maximum theorem |
| **R3 (3)** | No global continuous selection of $u^*$ | Construction from VP-1 / VP-4 |
| **R4** | $v$ continuous, concave, locally Lipschitz | inf-of-affine |
| **R5** | Envelope: $\partial_i v = E_i(u^*)$ on regular branch | Danskin's theorem |

## Net OP-OMS-018 status

**PARTIALLY RESOLVED.**

- Local regularity PROVED on regular branches.
- **Global $C^1$ regularity REJECTED** — branch-switching surfaces $\Sigma_{\mathrm{branch}}$ exist (codim-1).
- **The value function $v(\lambda)$ takes over** as the canonical smooth-on-Δ³ object: continuous, concave, locally Lipschitz.
- Envelope (R5): $\nabla v = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*)$ — directly readable from the optimizer output.

## VP-6 path test

`vp6_u_star_regular_path_test.py` traversed 5 paths × 2 scenes (11 samples each) and classified per regime:

| Scene | Path | Verdict |
|---|---|---|
| S3 | cl_axis, sep_axis, CE1_pair, random | branch-switch detected (5, 5, 2, 6 jumps) |
| S3 | bd_axis | active-set change (R2 boundary) |
| S4 | cl_axis | branch-switch (1 jump) |
| S4 | bd_axis | smooth branch (R1) |
| S4 | sep_axis, CE1_pair | field jump / kink |
| S4 | random | active-set change (R2) |

All four regimes (R1, R2, kink, branch-switch) realized empirically. Direct
empirical confirmation of Theorems R1, R2, and Prop R3 (3).

## Conceptual reframing for OMS

The branch-switching surfaces $\Sigma_{\mathrm{branch}}$ are **observer-type
transition surfaces**, not regularity defects. They are predicted by the
theory rather than failures of it. The canonical OMS picture becomes a
**stratified smooth structure** on Δ³, with codim-1 gluing surfaces between
regular branches.

## Files produced

- `THEORY/2_substrate/foundations/observer_moduli/op_oms_018_regular_u_star.md` (23 KB; full proofs)
- `CODE/experiments/observer_moduli/vp6_u_star_regular_path_test.py`
- `CODE/experiments/results/observer_moduli/vp6_u_star_path_results.json` (224 KB)
- `CODE/experiments/results/observer_moduli/vp6_u_star_path_summary.md`

## Downstream patches

- `observer_landscape_admissible_class.md` — V2 criterion relaxed to stratified-$C^1$.
- `basin_stratification.md` §11 added — basin boundaries include $\Sigma_{\mathrm{branch}}$.
- `stratified_dynamics.md` §8 added — Filippov sliding-mode at $\Sigma_{\mathrm{branch}}$.
- `oms_1_2_status_audit.md` — stage promoted from OMS-1.1 to **OMS-1.2** ("Computationally Grounded Canonical Candidate with Local Regularity Theorem").
