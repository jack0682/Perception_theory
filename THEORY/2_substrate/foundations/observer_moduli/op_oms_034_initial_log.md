---
type: working/reading-log
created: 2026-05-08
session: Session 8 (OP-OMS-034 closure)
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OP-OMS-034 — Initial Reading Log

State at session start: **OMS-2.0 Accepted — Static**, Full Temporal Conditional on OP-OMS-034.

## Documents reviewed (mandated order)

1. `oms_2_0_accepted_audit.md` — Session-7 verdict: Static Accepted; Full Temporal Conditional on OP-OMS-034 only.
2. `op_oms_034_temporal_delta3_status.md` — Session-7 separation declaration. Static does not require temporal; full temporal requires non-degenerate $E_{tr}$ on a 2-time-slice scene.
3. `gap_c1_final_theorem_package.md` — Static Theorem C1.5 PROVED. Energy decomposition $e(\lambda) = (E_{cl}, E_{sep}, E_{bd})$ on the static face; rank 2 on the **2D** simplex tangent.
4. `op_oms_001_gap_c1_sensitivity.md` — Theorem S1: $J_e = -G_T^\top H_T^{-1} G_T$. Generalizes to 4-component energy on temporal scene.
5. `op_oms_026_sigma_branch_full.md` — Σ_branch decomposition (codim-1 PROVED for static).
6. `op_oms_033_sigma_sn_arnold.md` — SN3 codim-1 fold theorem (conditional). Same structure applies temporal.
7. `open_problems.md` — OP-OMS-034 SEPARATED at end of Session 7.
8. `audit_log.md` — W21/W24 (static-temporal scope hazards).
9. `canonical.md` Appendix OMS — OMS Static layer canonical; Temporal subsection pending (Gate 7 of this session).

## Code inspection — temporal infrastructure

### Available (`scc/transport.py`).

- `cohesion_fingerprint(u, graph, params)` → φ ∈ R^{n×3}: $(u, \mathrm{Cl}(u), D(u))$.
- `graph_distance_matrix(graph)` → $d_G \in R^{n×n}$ (shortest-path distances).
- `transport_cost(phi_t, phi_s, dist_matrix, sigma, gamma)` → $c \in R^{n×n}$: $d_G^2/(2\sigma^2) + \gamma \lVert \phi_t - \phi_s \rVert^2$.
- `sinkhorn_partial_ot(cost, mu, nu, eps)` → transport plan $M$ + info dict. Log-domain Sinkhorn.
- `transport_field(M, u_s)`, `persist_transport(u_t, u_s, M, theta_core)`, `transport_fixed_point(...)`.

### Available (`scc/multi.py`).

- `transport_k_formations(...)`: K-formation transport between time slices (full temporal scc.multi infrastructure).
- `multi_diagnostic_vector(...)`.

### Issue with `find_formation` for temporal use.

`scc.optimizer.EnergyComputer.gradient(u)` includes static gradients ($cl$, $sep$, $bd$) but **explicitly excludes** the transport gradient:

> "NOTE: E_tr gradient w.r.t. u is not included here. The transport energy is self-referential (u → fingerprint → cost → M → E_tr), so its gradient is handled by the outer fixed-point iteration in transport.py, not by direct differentiation."

Hence to make $\lambda_{tr}$ a non-trivial direction in the per-time-slice optimizer, we cannot reuse `find_formation` directly. Two options:

1. Use the full $K$-formation transport fixed-point loop (`scc.multi.transport_k_formations`) — heavy but principled.
2. **Use a faithful reduced temporal OMS test** (per the user's explicit fallback): a fixed transport kernel $M$ (Gaussian-shift on graph distance) plus an L2 transport-mismatch term $E_{tr}(u_0, u_1) = \tfrac{1}{2}\lVert M u_0 - u_1 \rVert^2$ with closed-form gradient $M^\top(M u_0 - u_1)$.

Option 2 is the right choice for OP-OMS-034: tractable runtime, closed-form gradient, **non-degenerate** $\lambda_{tr}$-direction (the optimizer's $u_0^*$ depends on $\lambda_{tr}$). It is documented as a **faithful reduced temporal OMS test**, not full Sinkhorn OT.

The rank-3 witness and codim-1 branch map are theoretically equivalent for any non-degenerate transport: what matters is that $\lambda_{tr}$ produces an independent response in the energy decomposition.

## Critical correction to prior session notes

Previous session notes (Session 6) referenced a "4×4 minor" requirement for the temporal extension. This is **wrong**:

- $\Delta^3$ has tangent dimension **3** (not 4), because the simplex constraint $\sum \lambda_i = 1$ removes one direction.
- The energy decomposition $e_{\mathrm{temp}}(\lambda) = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*(\lambda)) \in \mathbb{R}^4$ is 4-dimensional in the codomain.
- The Jacobian $J_e^{\mathrm{tan}} = D_\lambda e_{\mathrm{temp}}\bigr\vert _{T_\lambda \Delta^3} \in \mathbb{R}^{4 \times 3}$ is 4×3 in the tangent direction.
- Full rank means **rank 3** (not 4), as $\min(4, 3) = 3$.

This session uses the correct **rank-3 condition** throughout.

## Plan

1. Gate 1: write `op_oms_034_temporal_delta3_resolution.md` with precise rank-3 target.
2. Gate 2: write `vp11_temporal_delta3.py` — minimal 2-time scene, custom temporal optimizer with closed-form $E_{tr}$ gradient.
3. Gate 3: temporal rank witness on 14 λ-points; compute $J_e^{\mathrm{tan}} \in R^{4 \times 3}$; SVD; rank threshold.
4. Gate 4: temporal Δ³ branch map on tetrahedral grid (K=5 → 56 points or K=6 → 84).
5. Gate 5: update resolution file with verdict (Case A / B / C).
6. Gate 6: write `oms_2_0_full_accepted_audit.md` with final classification.
7. Gate 7: add OMS Temporal Extension subsection to `canonical.md` Appendix OMS.
8. Gate 8: bookkeeping.
