# 01_T_L1_F_canonical_promotion_closure.md — 2026-05-02 (W5 Day 6)

**Date:** 2026-05-02
**Session title:** SCC Multi-Formation L1 Bridge Closure — T-L1-F Cat-A Conditional Promotion
**Type:** Canonical promotion + research-session closure documentation.
**Working directory:** `THEORY/logs/daily/2026-05-02/`.
**Canonical version after closure:** **CV-1.5.2** (incremented from CV-1.5.1, 2026-04-29).
**Closure status:** **CLOSED**. Today's research session is closed at CV-1.5.2 with T-L1-F canonically registered as a Cat-A conditional theorem.

---

## §1. Core Result

**T-L1-F — Hard-Bar / Active-Count Bridge under the L1-J Regime** was promoted to canonical status as a **Cat-A conditional theorem** under the L1-J regime hypothesis package $(P0)$–$(P11)$.

**Theorem statement.** Let $G=(X,E)$ be a finite graph and $\mathbf u\in\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)$ a shared-pool multi-formation state. Under the L1-J package $(P0)$–$(P11)$,

\[
\boxed{
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
}
\]

and the map

\[
\mathcal A_{\mathrm{bar}}:\,A^\varepsilon(\mathbf u)\;\longrightarrow\;\mathrm{Bars}_0^{\mathrm{term}}(U;G),
\qquad
\mathcal A_{\mathrm{bar}}(j):=\text{the unique dominant bar with birth in }N_j^r,
\]

equivalently $\mathcal A_{\mathrm{bar}}(j)=$ the bar born at $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$, is a bijection from active slots to dominant terminal $H_0$ bars.

**Status:** **PROMOTED_AS_CAT_A_CONDITIONAL.** Canonical version CV-1.5.2 (2026-05-02).

---

## §2. Hypothesis Package $(P0)$–$(P11)$

- **P0** terminal-death $H_0$ superlevel persistence convention.
- **P1** deterministic tie convention (fixed total order $\prec$ on $X$; ties broken by ascending $\prec$).
- **P2** active mass $m_j>\varepsilon$ + connected $\delta$-support $G[S_j^\delta]$.
- **P3** disjoint active neighborhoods $N_j^r\cap N_k^r=\emptyset$ (LG-1).
- **P4** low boundary collar $\max_{\partial N_j^r}U\le b_j-\ell_{\min}-r_{\mathrm{assoc}}$ (LG-2).
- **P5** background suppression on $U$: $\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}$ (LG-4 — on $U$, not just $R_{\mathrm{inact}}$).
- **P6** birth height $b_j\ge h_{\min}\ge\ell_{\min}$.
- **P7** decay-to-cut (heterogeneous form): $u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta))$ and $H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}$.
- **P8** tightened H6 on $G_j^r$: $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$.
- **P9** local perturbation control $\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2$.
- **P10** inactive residual suppression $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$.
- **P11** margin ledger $h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}$.

---

## §3. Files Updated Today

### Canonical files modified

- **`THEORY/canonical/theorem_status.md`** — added new section "Canonical Spec v1.5.2 (2026-05-02) — Current Version (W6: L1-F Hard-Bar / Active-Count Bridge Conditional Cat-A)" with the T-L1-F entry; reflagged CV-1.5.1 from "Current Version" to "Previous Version". +30 lines (338→368).
- **`THEORY/canonical/canonical.md`** — inserted T-L1-F entry at the end of §13 Category A (just before Category B header). +9 lines (1666→1675).

### Canonical files NOT modified

- **`THEORY/canonical/open_problems.md`** — left unchanged. Rationale: no existing OP entry maps directly to L1-F; OP-0005 / OP-0008 are not solved by T-L1-F (T-L1-F is a bridge, not a K-selection mechanism or σ-inheritance result); minimal-edits principle.

### L1 chain documents (provenance, working/MF — already in repo)

- `THEORY/working/MF/kbar_kact_bridge_L1_formalization.md`
- `THEORY/working/MF/kbar_kact_bridge_L1A_merge_level.md`
- `THEORY/working/MF/kbar_kact_bridge_L1B_bridge_bound.md`
- `THEORY/working/MF/kbar_kact_bridge_L1C_slot_to_bar.md`
- `THEORY/working/MF/kbar_kact_bridge_L1D_no_extra_bar.md`
- `THEORY/working/MF/kbar_kact_bridge_L1E_inactive_suppression.md`
- `THEORY/working/MF/kbar_kact_bridge_L1F_synthesis.md`
- `THEORY/working/MF/kbar_kact_bridge_L1G_empirical_diagnostic.md`
- `THEORY/working/MF/kbar_kact_bridge_L1H_local_to_global_transfer.md`
- `THEORY/working/MF/kbar_kact_bridge_L1H2_boundary_leakage.md` (post-L1-K-REPAIR R-1 contradiction proof + R-3 plateau)
- `THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md`
- `THEORY/working/MF/kbar_kact_bridge_L1J_catA_upgrade_attempt.md` (post-L1-K-REPAIR R-2 $q_j^U$ + R-4 heterogeneous-$\psi$)
- `THEORY/working/MF/kbar_kact_bridge_L1K_external_audit.md`
- `THEORY/working/MF/kbar_kact_bridge_L1L_scc_decay_theorem.md`

### Diagnostic / counterexample scripts (provenance)

- `CODE/scripts/l1g_l1hyp_diagnostic.py`
- `CODE/scripts/l1h_local_to_global_counterexample.py`
- `CODE/scripts/l1h2_boundary_leakage_counterexample.py`
- `CODE/scripts/l1i_constants_feasibility.py`
- `CODE/scripts/l1j_bridge_cut_decay_diagnostic.py`

---

## §4. What Was Proved / Established

- **Conditional theorem under L1-J regime** $(P0)$–$(P11)$.
- **Resolved Multi-Formation count bridge.** Terminal hard-bar count $K_{\mathrm{bar}}^{\ell_{\min}}$ agrees with active slot count $K_{\mathrm{act}}^\varepsilon$ in the resolved regime.
- **Labeled association** between active slots and dominant bars established under conditions: $\mathcal A_{\mathrm{bar}}(j)=$ the unique dominant bar born at $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$.
- **Boundary-leakage gap closed (PO-LH1).** L1-H2 Lemma 1 (graph-inclusion: $\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}$) + Lemma 2 (contradiction-based bottleneck-stability under tightened H6) close the H10 transfer.
- **External audit passed** (L1-K, THEOREM_CANDIDATE_STRONG_AUDIT_PASSED) with 4 proof-hygiene repairs (R-1 contradiction proof, R-2 $q_j^U$ clarification, R-3 plateau handling, R-4 heterogeneous $\psi$) all applied (L1-K-REPAIR).
- **P7 status decision** (L1-L): P7 adopted as **safe technical regime hypothesis**; L1-L Combes-Thomas / discrete Agmon analysis provides theorem-grade backing under strong stationarity (P7_DERIVED_UNDER_STRONG_STATIONARITY) but P7 is not asserted for all SCC states.
- **Empirical regime non-vacuous** (L1-I): 439/1920 (22.9%) configurations on $T^2_{20}$ are FEASIBLE_WITH_BUDGET; best case $\sigma_b=0.5,\delta=0.02,r=0,\ell_{\min}=0.10$ raw_gaussian.
- **Numerical verification** (L1-H2 stress 5/5 + L1-J PO-1 6/6).

---

## §5. What Was NOT Claimed

- **No global $K_{\mathrm{bar}}=K_{\mathrm{act}}$.** The equality holds only under $(P0)$–$(P11)$.
- **No global $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}$.** Additionally requires $\phi\in\Phi_{\mathrm{res}}$ per WQ-LAT-1.B.
- **OP-0005 (K-Selection) not solved.** T-L1-F is a bridge, not a K-selection mechanism.
- **OP-0008 ($\sigma^A$ K-jump non-determinism) not solved.** T-L1-F does not address $\sigma$-inheritance.
- **$\sigma_{\mathrm{rich}}$ sufficiency not claimed.**
- **Reservoir theory not promoted to canonical.** Reservoir framework remains working-grade.
- **P7 not generally derived for all SCC states.** L1-L provides Route C derivation under strong stationarity only.
- **No application / robotics / vision claims.**
- **No new Commitment number assigned.** T-L1-F uses C-0721 / P-0721 in the existing C-/P- numbering.

---

## §6. Interpretation

T-L1-F gives the **resolved-regime baseline**. It tells us when chart-level active count $K_{\mathrm{act}}^\varepsilon$ and aggregate topological count $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ agree. This baseline is necessary before studying:

- **overlap regime** where $K_{\mathrm{bar}}\neq K_{\mathrm{act}}$ (e.g., R23 generic states with multimodal aggregate);
- **K-jump events** where $K_{\mathrm{act}}$ changes under dynamics (OP-0008 territory);
- **soft-count regime** where smooth $\phi$-envelopes are used (Φ_res restriction needed);
- **σ-rich non-determinism** at K-jumps under aggregate merging.

By establishing the canonical baseline first, future work can measure precisely when and how the count bridge breaks. T-L1-F is a *resolved-regime baseline*, not a global identity — its main value is delineating the boundary between the resolved regime (where standard counting works) and the more interesting unresolved regimes (where overlap, σ-jumps, and soft-count drift become the substantive phenomena).

---

## §7. Next Work Queue

1. **L1-M — Soft-Count Corollary under $\Phi_{\mathrm{res}}$.** Combine T-L1-F count equality with WQ-LAT-1.B $\Phi_{\mathrm{res}}$ envelope class to derive $K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi)$ for $\phi\in\Phi_{\mathrm{res}}$ as a Cat-A corollary. Estimated effort: 1–2 weeks.
2. **L1-L-FORMALIZE — full Combes-Thomas / Agmon derivation of P7 from primitive SCC dynamics.** Removes P7 from T-L1-F's hypothesis package; upgrades T-L1-F from CONDITIONAL to UNCONDITIONAL Cat A under primitive SCC. Substantive theorem-grade workstream. Not blocking for L1-M.
3. **L1-N — dynamics-compatible regime study.** Find an SCC initial state in the L1-J regime, integrate forward, measure how long the regime is preserved. Bridges static feasibility (L1-I) to dynamic applicability.
4. **OP-0008 return path.** Use the resolved-regime baseline T-L1-F to re-enter $\sigma$-rich / K-jump non-determinism analysis. The open question: when the L1-J regime is violated (e.g., aggregate merging via F-B6), what σ-rich invariants distinguish pre-event vs post-event states?
5. **WQ / LAT follow-up.** WQ-LAT-1 / WQ-LAT-1.B are anchored by T-L1-F's conditional bridge. Re-examination of WQ-LAT trajectories with the L1-K-REPAIR-tightened L1-J hypothesis package would clarify regime-membership trajectories.

---

## §8. Closure Note

Today's research is closed at **CV-1.5.2** with **T-L1-F** canonically registered as a **Cat-A conditional theorem** under the **L1-J regime package $(P0)$–$(P11)$**. The L1 chain (L1-A through L1-L, including L1-K external audit + L1-K-REPAIR + L1-L P7 status decision) is the definitive proof provenance. Open problems unchanged. No global identity claimed. Next session: L1-M soft-count corollary.
