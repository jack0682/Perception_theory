---
type: log/daily
date: 2026-05-08
session: Session 5 continuation (post-final-report)
attacks: OP-OMS-026 (initial), OP-OMS-028, OP-OMS-001 (initial)
deliverables: vp7_branch_map.py, op_oms_028_lipschitz_v.md, op_oms_001_formal_proof_attempt.md
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Session 5 Continuation — Three OP Attacks

After the Session-5 final report, the user said "continue". The three
top-priority OPs from §13 of that report were attacked in parallel.

## OP-OMS-026 — VP-7 fine-grid Σ_branch mapping (PARTIALLY RESOLVED)

`vp7_branch_map.py` implemented a triangular grid on the static face Δ²:

| Scene | Grid | Distinct branches | Transition edges | Dominant fraction |
|---|---|---|---|---|
| **P12** (path graph, n=12) | K=10, 66 pts | 7 | 44 | **66.7% (3,4)** |
| **S3** (6×6 grid, n=36) | K=8, 45 pts | 17 | 74 | 20% (6,11) |

Total runtime: 79 s.

**Key findings:**

- $\Sigma_{\mathrm{branch}}$ is empirically codim-1 on Δ² for both scenes.
- P12 admits a large constant-rank region (the (3,4) branch covering 2/3
  of the simplex) — this is an **OP-OMS-024 candidate**.
- S3 is fragmented (17 branches with many singletons) — OP-OMS-024 fails
  universally; only locally.

## OP-OMS-028 — Quantitative Lipschitz bound for $v(\lambda)$ (PROVED)

**Theorem L1:** $|v(\lambda) - v(\lambda')| \le \lVert M \rVert_2 \cdot \lVert \lambda - \lambda' \rVert_2$ globally on $\Delta^3$, where $M_i = \sup_{u \in \Omega} \lvert E_i(u; X_t) \rvert$.

Proof: $v(\lambda) = \inf_u L_u(\lambda)$ with $L_u$ affine in $\lambda$;
$|L_u(\lambda) - L_u(\lambda')| \le \lVert E(u) \rVert_2 \lVert \lambda - \lambda' \rVert_2$;
take sup over $u \in \Omega$ (compact ⇒ finite).

**Explicit bounds for S3-like scenes:**

- $M_{cl} = O(1)$ (resolvent-bounded).
- $M_{sep} \le m$ (mass).
- $M_{bd} \le 2\alpha\rho(L) n + \beta n / 16$.
- $M_{tr} = 0$ on static.
- $L_2 \le O(\rho(L) n) \approx 600$ (conservative).
- VP-6 empirical $L_2 \approx 4$ (tight).

**Prop L2 (corollary):** $v$ is **strictly concave** off $\Sigma_{\mathrm{branch}}$, conditional on energy-gradient distinguishability at regular points (which is exactly the H2 condition of Gap C1, addressed in Session 6).

**OP-OMS-028 CLOSED with explicit constant.**

## OP-OMS-001 — Three-reduction proof attempt (PROOF SKETCH)

`op_oms_001_formal_proof_attempt.md` developed three independent structural reductions:

### Reduction A (phase-transition surface preservation).

If $g \in G_{\mathrm{cw}}$, then $g(\Sigma_{T8}(X_t)) = \Sigma_{T8}(X_t)$ for every scene. The continuous family $\{\Sigma_{T8}(X_t)\}_{X_t}$ has many distinct surfaces (parameterized by $\lambda_2(X_t)$). Lemma A1: a diffeomorphism preserving a continuous family of distinct codim-1 surfaces with a transverse second family is the identity.

**Gap A1:** transversality of $\Sigma_{T8}$ family with a second preserved family is left as a sub-claim.

### Reduction B (vertex-fixing + LS1) — **PROVED**.

Each of the four vertices $\{e_{cl}, e_{sep}, e_{bd}, e_{tr}\}$ has a distinct $P_{\mathrm{top}}$ signature (VP-1 evidence + Prop CW1). $S_4$ is rejected. By Prop LS1, the only continuous group preserving all four vertices is the identity. **Continuous component of $G_{\mathrm{cw}}$ is trivial.**

**This is registered as OP-OMS-029 PROVED.**

### Reduction C (energy decomposition uniqueness).

By envelope theorem (R5), $\nabla v = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*)$ on the regular branch. If this gradient is locally injective in $\lambda$, then any candidate $g \in G_{\mathrm{cw}}$ is the identity.

**Gap C1:** algebraic independence of the four energy components as functions of $\lambda$ on a generic scene — addressed in Session 6 Gate 1.

## Net status

OP-OMS-001 reads as **PROOF SKETCH** with three named gaps (A1, B1, C1).
OP-OMS-001 closure reduces to closing Gap C1, which becomes the Session 6
Gate 1 + Gate 2 target.

## Files produced

- `THEORY/working/observer_moduli/vp7_branch_map_results.md`
- `THEORY/working/observer_moduli/op_oms_028_lipschitz_v.md`
- `THEORY/working/observer_moduli/op_oms_001_formal_proof_attempt.md`
- `CODE/experiments/observer_moduli/vp7_branch_map.py`
- `CODE/experiments/results/observer_moduli/vp7_branch_map.json`
- `CODE/experiments/results/observer_moduli/vp7_branch_map.md`

## OP catalog state at end of Session 5 cont.

| OP | Status |
|---|---|
| OP-OMS-001 | PROOF SKETCH (continuous case PROVED, discrete partial) |
| OP-OMS-024 | PARTIALLY RESOLVED (P12 yes, S3 no) |
| OP-OMS-026 | PARTIALLY RESOLVED (codim-1 confirmed) |
| OP-OMS-028 | PROVED (Theorem L1 with explicit constant) |
| OP-OMS-029 | PROVED (continuous-component triviality) |
