> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 04_nq_g1_2_ext_design.md — NQ-G1-2-ext: Production Reach Measurement Design

**Session:** 2026-05-06 (W6 Day 3 G3.4, P1).
**Debt addressed:** W2 Production reach — T-L1-F/T-L1-M 의 production WQ-1 trajectories reach.
**Background:** NQ-G3-1 sweep (W6 D2) revealed baseline 439 = 50 wq1 + 389 raw_gaussian. Production-load-bearing reach = 50/960 = 5.2%, not 22.9% headline.
**Execution:** W7 D1 (~1-2h); this file is the design spec.
**Sub-files:** `04a_l1i_extension_script_outline.md` + `04b_post_flow_R_j_measurement_protocol.md`.

---

## §1. Measurement Quantity

**Target:** Post-flow residual $\lVert R_j \rVert_\infty$ under shared-pool gradient-flow dynamics.

**Definition:** For a K-formation configuration starting at initial state $\mathbf{u}_0 \in \Sigma^K_M$ (wq1 build_initial_state), after $N_{\mathrm{steps}}$ gradient steps, define:
$$R_j(t) = u^{(j)}(t) - u^{(j),\mathrm{ideal}}(t)$$
where:
- $u^{(j)}(t)$ = the $j$-th slot cohesion field at step $t$.
- $u^{(j),\mathrm{ideal}}(t)$ = the "ideal" Gaussian-shaped formation centered at the centroid of the active support of $u^{(j)}(0)$, with the same mass (i.e., a reference shape that would satisfy T-L1-F's L1-J regime hypothesis).

**Measurement:** $\lVert R_j \rVert_\infty = \max_{i \in V} \lvert R_j(t)_i \rvert$ at each snapshot step $t$.

**Primary metric:** $\lVert R_j \rVert_{\infty,\mathrm{max}} = \max_{t \in \{100, 200, \ldots, N_{\mathrm{steps}}\}} \lVert R_j(t) \rVert_\infty$ (worst-case residual over the trajectory).

---

## §2. Theoretical Motivation

**T-L1-F hypothesis P9:** $\lVert R_j \rVert_{\infty, N_j^r} \leq \rho_{\mathrm{pert}}/2$ where $N_j^r$ is the restricted neighborhood of formation $j$ and $\rho_{\mathrm{pert}}$ is the perturbation radius from the L1-J regime conditions.

**NQ-G1-2 finding (W6 D1):** Initial-state $\lVert R_j \rVert_\infty$ satisfies H6' (non-binding) in the initial configuration. But *dynamic-state* $\lVert R_j \rVert_\infty$ has not been measured (post-gradient-flow snapshots).

**The W2 debt:** If post-flow $\lVert R_j \rVert_\infty > \rho_{\mathrm{pert}}/2$ frequently in WQ-1 trajectories, T-L1-F Cat A conditional's regime condition (P9) is not met in production, and the theorem's reach is narrower than the headline 22.9% suggests.

**Key question:** Does the gradient flow *maintain* the L1-J regime conditions (P0-P11), or does it *exit* the regime as the formations evolve?

---

## §3. Test Configuration

| Parameter | Value | Rationale |
|---|---|---|
| Graph | $T^2_{20}$ (20×20 torus, $n=400$ nodes) | Production-representative (matches exp55+ experiments) |
| $K_{\mathrm{field}}$ | 4 | Standard multi-formation setup |
| Initial masses | $(30, 30, 30, 0)$ | 3 active slots + 1 empty; matches wq1 build_initial_state canonical setup |
| $\varepsilon$ | 0.225 (Commitment 16 default) | Canonical ε convention |
| Number of gradient steps $N_{\mathrm{steps}}$ | 1000 | Sufficient for near-convergence (exp55 baseline: 5000; use 1000 for efficiency) |
| Measurement interval | Every 50 steps (20 snapshots) | Balance between resolution and wall-clock |
| Number of configs | 960 (wq1 state_mode only) | From NQ-G3-1 baseline; exclude raw_gaussian (ε-independent testing artifact) |
| $\rho_{\mathrm{pert}}$ | canonical value per T-L1-F P9 | From `l1i_constants_feasibility.py` parameter setup |

---

## §4. Hypothesis Branches

**H-G1-2-ext-A (optimistic):** Post-flow $\lVert R_j \rVert_{\infty,\mathrm{max}} \leq \rho_{\mathrm{pert}}/4$ for the majority (>50%) of wq1 configs.

→ *Interpretation:* (P9-tight) condition met in production. T-L1-J' regime is production-representative. T-L1-F/M reach substantial. **Action:** Add production reach note to canonical T-L1-F entry; consider T-L1-J' regime as new canonical Cat A regime.

**H-G1-2-ext-B (pessimistic):** Post-flow $\lVert R_j \rVert_{\infty,\mathrm{max}} > \rho_{\mathrm{pert}}/2$ for the majority (>50%) of wq1 configs.

→ *Interpretation:* Regime exit is common. L1-J regime is transient. T-L1-F Cat A conditional's reach is narrow in production. **Action:** Add retroactive caveat to T-L1-F/M (similar to T-σ-Theorem-4 pattern: continuum-vs-discrete caveat). Cat A conditional demoted to "narrow regime" status. Alert for W8 canonical correction.

**H-G1-2-ext-C (intermediate):** Mixed distribution — some configs satisfy (P9-tight), others exceed $\rho_{\mathrm{pert}}/2$, with regime-dependent clustering.

→ *Interpretation:* T-L1-F reach is regime-dependent; extended regime characterization needed. **Action:** NQ-G1-2-ext-2 follow-up: characterize which initial configs (by $\lVert R_j \rVert_\infty\vert _{t=0}$ or by formation separation) predict post-flow reach.

---

## §5. Wall-Clock Estimation

| Step | Estimate |
|---|---|
| Config loading (960 wq1 configs from baseline JSON) | ~5 min |
| Gradient flow: 960 configs × 1000 steps × `scc/multi.py` forward | ~45-90 min (depends on multi-formation step cost; exp55 baseline ~5000 steps/100 configs in ~10 min → 960 × 1000 ≈ 35-70 min) |
| $R_j$ computation at 20 snapshots | ~5-10 min |
| Statistical aggregation + output JSON | ~2-5 min |
| **Total** | **~1-2h** |

This fits within W7 D1 morning budget (~1-2h for NQ-G1-2-ext execution).

---

## §6. Implications for Canonical Claims

| Outcome | Canonical implication | Urgency |
|---|---|---|
| H-G1-2-ext-A | T-L1-F/M reach confirmed production-representative; add positive note | Low (strengthens existing claims) |
| H-G1-2-ext-B | T-L1-F/M Cat A conditional requires retroactive caveat; potential Cat A → Cat A conditional (narrower) | **HIGH** — W7 D2 supervised canonical erratum |
| H-G1-2-ext-C | Extended regime characterization; deferred to NQ-G1-2-ext-2 | MEDIUM — W8 D1 |

The W2 debt (5.2% wq1 production reach implicit) suggests H-G1-2-ext-B or H-G1-2-ext-C is more likely. The NQ-G1-2-ext sweep will settle this empirically.

---

**End of `04_nq_g1_2_ext_design.md`. G3.4 main design complete. See `04a_l1i_extension_script_outline.md` + `04b_post_flow_R_j_measurement_protocol.md` for implementation details. Ready for W7 D1 cold-start execution.**
