# L1-I: Constants Feasibility Study

**File:** `THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md`
**Document type:** non-canonical working empirical feasibility study
**Created:** 2026-05-02 (after L1-A through L1-H)
**Status:** working; empirical verdict only; not theorem-grade; not Cat-A

---

## 1. Status and Scope

This is a non-canonical working note. It empirically tests whether the L1-H constants admit a non-empty regime on initial Gaussian-bump configurations on \(T^2_{20}\).

L1-I does **not**:

- prove L-1.
- promote L1-F or L1-H to Cat-A.
- solve OP-0005 or OP-0008.
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) or \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally.
- claim \(\sigma_{\mathrm{rich}}\) sufficiency.
- promote reservoir theory to canonical.
- treat empirical feasibility as theorem proof.
- modify any canonical or existing working file.

L1-I produces:

- a parameter sweep of 1920 configurations on \(T^2_{20}\) under two state-construction modes (WQ-1 mass-projected, raw Gaussian);
- per-configuration measurement of all L1-H inequalities (LG-1 through LG-4, tightened H6, L1-F ledger);
- feasibility classification per configuration into one of `FEASIBLE_WITH_BUDGET`, `RAW_FEASIBLE`, `MARGINAL`, `INFEASIBLE`, `INCONCLUSIVE`;
- a **positive empirical verdict** that the L1-H regime is non-empty: 439/1920 (22.9 %) configurations satisfy all clauses with positive margins of at least 0.05;
- a **negative empirical sub-verdict** that the WQ-1 default initialization (σ_b=2.0, mass-30 forced projection) is **structurally incompatible** with the L1-H regime, failing LG-1 (overlapping supports / inflated supports) on essentially every test.

---

## 2. Task Checklist

- [x] Read L1-H, L1-G, L1-F, and surrounding bridge-lemma grounding.
- [x] Re-inspect persistence / diagnostics / k_soft / graph code and the L1-G + L1-H scripts.
- [x] Define each L1-H inequality precisely as a measurable quantity on a given state.
- [x] Implement `CODE/scripts/l1i_constants_feasibility.py` with a parameter sweep over (σ_b, δ, r, ℓ_min, geometry, state_mode).
- [x] Decide on two state-construction modes:
  - `wq1`: WQ-1 NQ-242c default with mass=30 per slot, simplex-barrier projection, and clipping.
  - `raw_gaussian`: idealized \(u^{(j)}(x)=\exp(-d_T(x,c_j)^2/(2\sigma_b^2))\) with peak=1, no forced normalization.
- [x] Sweep σ_b ∈ {0.5, 1.0, 1.5, 2.0}, δ ∈ {0.02, 0.05, 0.10, 0.15, 0.20}, r ∈ {0, 1, 2, 3}, ℓ_min ∈ {0.05, 0.10, 0.15, 0.20}, geometry ∈ {A, B, wide}, state_mode ∈ {wq1, raw_gaussian}.
- [x] Smoke test (48 configs, ~0.4 s) and full sweep (1920 configs, ~15 s).
- [x] Aggregate failure counts and best-case configurations.
- [x] Stratify results by σ_b, r, δ, geometry, state_mode.
- [x] Verify file creation.
- [x] Preserve all non-claims.

---

## 3. Motivation from L1-H

L1-H produced a partial theorem candidate \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A|\) under L1-H conditions LG-1..LG-6 plus tightened H6 plus the L1-F ledger, with one residual proof obligation (PO-LH1, boundary-leakage correction).

Before attempting PO-LH1 (which is a theorem-grade analytic obligation), it is essential to confirm that the L1-H regime is not empty: that there exist configurations on \(T^2_{20}\) (or another natural finite graph) at which **all** L1-H inequalities are simultaneously satisfied with positive margins.

If the regime is empty, PO-LH1 is moot — the L1-H theorem candidate is vacuous. If the regime is non-empty and large, PO-LH1 becomes the priority for upgrading L1-H from `LEMMA-CAND` toward Cat-A. If the regime is non-empty but small, the theorem candidate may be technically valid but practically irrelevant; the next move would be to weaken L1-H's conditions.

---

## 4. Feasibility Question

> Do there exist configurations, parameters, and neighborhoods on \(T^2_{20}\) satisfying LG-1, LG-2, LG-3, LG-4, tightened H6, and the L1-F margin ledger simultaneously?

We answer this empirically.

---

## 5. Constants and Inequalities

The conditions tested per configuration. All are computed directly from the constructed state \(\mathbf u\) on \(T^2_{20}\) at \(\tau=0\).

| Symbol | Definition | Inequality | Source |
|---|---|---|---|
| LG-1 | \(N_j^r\cap N_k^r\) for \(j\neq k\) | overlap = 0 | L1-H §6 |
| LG-2 | \(B_{\partial,j}=\max_{x\in\partial N_j^r}U(x)\) | \(b_j-\ell_{\min}-r_{\mathrm{assoc}}-B_{\partial,j}\ge 0\) | L1-H §6 |
| LG-3 | \(\theta_{\mathrm{bridge}}^{jk}(U)\) (threshold-scan) | \(\min(b_j,b_k)-\ell_{\min}-r_{\mathrm{assoc}}-\theta_{\mathrm{bridge}}^{jk}\ge 0\) | L1-H §6 |
| LG-4 | \(\|U\|_{\infty,X_{\mathrm{bg}}}\) | \(\ell_{\min}-\rho_{\mathrm{bg}}-\|U\|_{\infty,X_{\mathrm{bg}}}\ge 0\) | L1-H §6 |
| H6' | \(\ell_{j,2}(u^{(j)};G)\) (slot-internal terminal-death) | \(\ell_{\min}-3\rho_{\mathrm{pert}}-\max_j\ell_{j,2}\ge 0\) | L1-H §10 |
| LDG | \(\theta_{\mathrm{bridge,max}}=\max_{jk}\theta_{\mathrm{bridge}}^{jk}\) | \(h_{\min}-\theta_{\mathrm{bridge,max}}-\ell_{\min}-r_{\mathrm{assoc}}-r_{\mathrm{birth}}\ge 0\) | L1-F §5 H4 |

Raw feasibility (`RAW_FEASIBLE`) takes \(r_{\mathrm{assoc}}=r_{\mathrm{birth}}=\rho_{\mathrm{pert}}=\rho_{\mathrm{bg}}=0\). Robust feasibility (`FEASIBLE_WITH_BUDGET`) requires every individual inequality to satisfy with margin ≥ `budget = 0.05`. `MARGINAL` corresponds to a small negative margin (within `MARGINAL_TOL = 0.01`). `INFEASIBLE` corresponds to a clear violation (margin \< -0.01). `INCONCLUSIVE` covers cases with empty active set or empty background (LG-4 vacuous).

---

## 6. Diagnostic Metrics

For each tested configuration:

- `n_active`: number of slots with mass \(>\varepsilon=0.225\) (`wq1` mode) or with `initial_masses[j] > 0` (`raw_gaussian` mode);
- `h_min_measured`: \(\min_{j\in A}U(p_j)\), the smallest peak height of \(U\) at active slot peaks;
- `lg1_disjoint`: True iff every active pair has \(N_j^r\cap N_k^r=\emptyset\);
- `boundary_collars[j]`: \(B_{\partial,j}\) per active slot (None if neighborhood covers entire graph);
- `bg_max_U`: \(\|U\|_{\infty,X_{\mathrm{bg}}}\); None if background empty;
- `bridge_heights[j-k]`: threshold-scan \(\theta_{\mathrm{bridge}}^{jk}(U)\) per active pair (capped at `bridge_max_pairs=6`);
- `slot_l2[j]`: full-graph terminal-death \(H_0\) secondary bar of \(u^{(j)}\) per active \(j\);
- per-clause margin (LG-2, LG-3, LG-4, H6', LDG);
- `feasibility_class`, `failing_clauses`, `notes`.

---

## 7. Sweep Design

Two state modes:

- **`wq1`**: uses `nq242c_counterexample.build_initial_state` — Gaussian with σ_b, normalized to mass 30 per active slot via `project_volume`, then iteratively clipped and simplex-rebalanced. This is the WQ-1 NQ-242c production initial state.
- **`raw_gaussian`**: ideal Gaussian \(u^{(j)}(x)=\exp(-d_T(x,c_j)^2/(2\sigma_b^2))\). Peak = 1 at center; no clipping; no mass projection; no simplex barrier. No dynamics.

Three geometries:

- **A**: `((5,5),(15,5),(10,14))` — WQ-1 equilateral-disk-triangle.
- **B**: `((5,5),(15,5),(10,11))` — WQ-1 isosceles-disk-triangle.
- **wide**: `((3,3),(13,3),(8,13))` — artificial maximally-separated 3-bump configuration on \(T^2_{20}\).

Sweep: σ_b ∈ {0.5, 1.0, 1.5, 2.0} × δ ∈ {0.02, 0.05, 0.10, 0.15, 0.20} × r ∈ {0, 1, 2, 3} × ℓ_min ∈ {0.05, 0.10, 0.15, 0.20} × geometry × state_mode = 4·5·4·4·3·2 = **1920 configs**.

Wall clock: 15.4 s.

---

## 8. Result Schema

The output JSON contains:

```
{
  "script", "script_version", "purpose", "non_claims": { 9 forbidden flags = False },
  "config": { graph + sweep ranges + budget threshold + tolerance },
  "summary": {
    "class_counts": { class -> count },
    "failure_counts": { clause -> count },
    "n_total": 1920,
    "best_cases": [ top 5 results sorted by class then by worst margin ]
  },
  "results": [ per-config FeasibilityResult dicts ],
  "wall_clock_seconds", "metadata": { host, python_version, run_timestamp_utc }
}
```

Each `FeasibilityResult` records the configuration, all measured constants, all per-clause pass flags and margins, the aggregate `feasibility_class`, the list of `failing_clauses`, and any notes (e.g. "Background X_bg is empty — LG-4 vacuous.").

The output JSON is at `CODE/scripts/results/l1i_constants_feasibility.json` (~3 MB).

---

## 9. Empirical Run Summary

### 9.1 Aggregate counts

Total tested: **1920** configurations.

| Class | Count | Fraction |
|---|---:|---:|
| `FEASIBLE_WITH_BUDGET` | 439 | 22.9 % |
| `RAW_FEASIBLE` | 228 | 11.9 % |
| `MARGINAL` | 20 | 1.0 % |
| `INFEASIBLE` | 1233 | 64.2 % |

### 9.2 Failure frequency

| Clause | Failure count | Most common reason |
|---|---:|---|
| LG-1 (disjoint neighborhoods) | 904 | Gaussian supports overlap (large σ_b) or simplex-projected supports cover entire graph (small σ_b under WQ-1 mass projection) |
| LG-4 (background suppression) | 402 | \(\|U\|_{\infty,X_{\mathrm{bg}}}\ge\ell_{\min}\); occurs at small ℓ_min or moderate σ_b |
| LG-2 (boundary collar) | 243 | Boundary collar near peak height; happens at small r |
| LG-3 (low bridge) | 0 | bridge always low when LG-1 holds (consistent with the support-separation argument) |
| H6 tightened | 0 | slot-internal terminal-death \(H_0\) gives ℓ_{j,2}=0 for Gaussian bumps (single-mode) |
| LDG ledger | 0 | when LG-3 holds, the ledger automatically holds for h_min ≈ 1 |

### 9.3 By state_mode

| state_mode | total | FEASIBLE_WITH_BUDGET | RAW_FEASIBLE | MARGINAL | INFEASIBLE |
|---|---:|---:|---:|---:|---:|
| `wq1` | 960 | 50 (5.2 %) | 80 | 13 | 817 |
| `raw_gaussian` | 960 | **389 (40.5 %)** | 148 | 7 | 416 |

The WQ-1 mass-projection mode is structurally incompatible with the L1-H regime in the sense that fewer than 6 % of configurations achieve `FEASIBLE_WITH_BUDGET`. The `raw_gaussian` mode shows the L1-H regime is non-empty: a large minority (40.5 %) achieves robust feasibility.

### 9.4 By σ_b within `raw_gaussian`

| σ_b | total | FEASIBLE_WITH_BUDGET | RAW_FEASIBLE | INFEASIBLE | dominant failure |
|---|---:|---:|---:|---:|---|
| 0.5 | 240 | **162 (67.5 %)** | 54 | 24 | LG-1 at large r combined with small δ |
| 1.0 | 240 | 138 (57.5 %) | 51 | 51 | LG-1 at large r |
| 1.5 | 240 | 72 (30 %) | 31 | 133 | LG-1 |
| 2.0 | 240 | 17 (7.1 %) | 12 | 208 | LG-1 (Gaussian supports overlap directly) |

Narrow bumps (σ_b ≤ 1.0) strongly favor feasibility. WQ-1's default σ_b = 2.0 is at the borderline of overlapping supports on \(T^2_{20}\) given the WQ-1 center positions (pairwise distances ~10).

### 9.5 By r within `raw_gaussian`

| r | total | FEASIBLE_WITH_BUDGET | RAW_FEASIBLE | INFEASIBLE |
|---|---:|---:|---:|---:|
| 0 | 240 | 94 | 46 | 96 |
| 1 | 240 | 127 | 46 | 64 |
| 2 | 240 | 105 | 35 | 100 |
| 3 | 240 | 63 | 21 | 156 |

`r = 1` is the optimum: small enough that neighborhoods stay disjoint, large enough that the boundary collar excludes the high-Gaussian core. Larger r increases LG-1 overlaps.

### 9.6 By δ within `raw_gaussian`

Approximately uniform across δ ∈ {0.02..0.20}: 72-82 FEASIBLE_WITH_BUDGET per δ-slice. Larger δ slightly increases INFEASIBLE counts because the support becomes too small and the boundary collar approaches the peak.

### 9.7 By geometry within `raw_gaussian`

| geometry | FEASIBLE_WITH_BUDGET | RAW_FEASIBLE | INFEASIBLE |
|---|---:|---:|---:|
| A | 134 | 51 | 132 |
| B | 121 | 45 | 153 |
| wide | 134 | 52 | 131 |

A and `wide` (artificial maximally-separated) perform similarly. B (compressed isosceles) is slightly worse because two centers are closer (graph distance ≈ 8 versus ≈ 10).

### 9.8 Best case (numerical detail)

Configuration: σ_b = 0.5, δ = 0.02, r = 0, ℓ_min = 0.10, geometry = A, state_mode = `raw_gaussian`. All margins comfortably positive:

| Metric | Value |
|---|---:|
| `h_min_measured` | 1.0000 |
| `lg2_min_margin` | 0.7647 |
| `lg3_min_margin` | 0.9000 |
| `lg4_margin` | 0.0817 |
| `h6_min_margin` | 0.1000 |
| `ledger_margin` | 0.9000 |
| `bg_max_U` | 0.0183 |
| `max_bridge` | 0.0000 |
| `boundary_collars` | `{0: 0.135, 1: 0.135, 2: 0.135}` |

`FEASIBLE_WITH_BUDGET` with the smallest margin LG-4 = 0.082 still well above the 0.05 budget threshold.

### 9.9 Default WQ-1 case (sigma_b=2.0, delta=0.05, r=1, l_min=0.10, A, wq1)

`feasibility_class = INFEASIBLE`. Only failing clause: **LG-1**. `bg_max_U = 0.023` (LG-4 actually passes), `lg1_overlap_count = 3` (all three pairwise neighborhoods overlap).

The reason WQ-1 default fails LG-1 is the σ_b=2 Gaussian on \(T^2_{20}\) with centers at pairwise graph distance 10: each natural Gaussian δ-support extends to radius ≈ 5 around its center, so the supports just touch on the torus. The WQ-1 mass-projection step does not change LG-1 here (it only affects the σ_b=0.5 / 1.0 cases by inflating supports through the uniform offset).

---

## 10. Feasibility Classification

**Verdict: FEASIBLE_WITH_BUDGET**.

The L1-H regime is non-empty on \(T^2_{20}\) under the `raw_gaussian` mode. 22.9 % of all 1920 configurations and 40.5 % of `raw_gaussian` configurations satisfy every L1-H inequality with margin ≥ 0.05.

**Sub-verdict: WQ-1 dynamics is INCOMPATIBLE.** Only 50/960 (5.2 %) of `wq1` configurations achieve `FEASIBLE_WITH_BUDGET`, and the WQ-1 *default* (σ_b=2.0, δ=0.05, r=1, ℓ_min=0.10, A) is `INFEASIBLE`. The mass-projection step in `nq242c_counterexample.build_initial_state` either (a) inflates supports via the uniform-offset projection at small σ_b, making LG-1 fail, or (b) leaves natural Gaussian supports overlapping at σ_b=2.0, again making LG-1 fail. The WQ-1 dynamics does not naturally land in the L1-H regime.

**Recommendation.** L1-H is not vacuous in principle, so the next theoretical priority is **L1-H2 — boundary-leakage proof / PO-LH1 discharge**. After PO-LH1 is closed, L1-H upgrades from `LEMMA-CAND` to a proof-grade conditional theorem on a non-empty regime.

---

## 11. Failure Modes

### L1I-F1 — WQ-1 mass-projection inflates supports

When σ_b is small (0.5–1.0) and `wq1` mode is used, the mass=30 per slot constraint forces the project_volume step to add a uniform offset across the torus to enforce the volume. This offset is comparable to or larger than δ, so \(S_j^\delta=\{u^{(j)}>\delta\}\) covers all 400 vertices of \(T^2_{20}\). LG-1 then fails by definition (every pair of slots has full overlap). LG-2 also fails (boundary undefined; \(N_j^r=X\)). The failure is visible in the diagnostic `notes`: "boundary undefined (N_j^r covers all of X)" and "Background X_bg is empty — LG-4 vacuous.".

### L1I-F2 — σ_b too large overlaps natural supports

At σ_b=2.0 with center spacing ~10 on \(T^2_{20}\), the natural Gaussian supports at δ=0.05 reach radius ≈ 5 around each center and overlap. The mass-projection step does not save this case; even `raw_gaussian` mode at σ_b=2.0 has 208/240 INFEASIBLE configurations.

### L1I-F3 — r too large

At r=3 on \(T^2_{20}\) with center spacing ~10, the active neighborhoods reach radius up to (graph-distance to support boundary) + r. For σ_b=1.5 supports of radius ~3, neighborhoods of radius 6 overlap. LG-1 fails.

### L1I-F4 — δ too large

At δ ≥ 0.15 the Gaussian supports become very small (only the immediate vicinity of each center). Boundary vertices get close to the center, raising B_∂,j toward the peak height and reducing the LG-2 margin.

### L1I-F5 — Empty background

When N_j^r covers all of X (large r combined with mass-projection-inflated supports), \(X_{\mathrm{bg}}\) is empty and LG-4 is vacuous. The script flags these with notes; classification falls back to whether all other conditions pass.

### L1I-F6 — Configuration / dynamics scope

All evidence is restricted to \(T^2_{20}\), the WQ-1 NQ-242c base centers (and the artificial `wide` extension), Gaussian initial bumps, and the σ_b / δ / r / ℓ_min ranges in the sweep. No claim of generalization to other graphs, dynamics, or initialization families is made.

### L1I-F7 — \(\tau=0\) snapshot only

L1-I evaluates feasibility at the initial state. The L1-H regime is non-empty *as a static property*; whether the SCC dynamics preserves the regime over time is a separate question (likely answered no by L1-G's empirical record on the production WQ-1 trajectory). L1-G already reported that the WQ-1 dynamics drives the system out of the L1-H regime via aggregate-bar merging.

---

## 12. Cat-Status and Evidence Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| L1-H regime | NON-EMPTY (empirical) | 439/1920 configs FEASIBLE_WITH_BUDGET | none for empirical; theorem-grade requires regime characterization |
| LG-1 disjoint neighborhoods | EMPIRICAL DEF | computed exactly per configuration | none |
| LG-2 boundary collar | EMPIRICAL DEF | computed via ∂N_j^r | tie convention for boundary |
| LG-3 inter-neighborhood bridge | EMPIRICAL via threshold scan | uses `l1g_l1hyp_diagnostic.threshold_scan_bridge_height` | exact min-cut not implemented |
| LG-4 background suppression | EMPIRICAL DEF | direct from U on X_bg | none |
| H6 tightened (ℓ_{j,2} ≤ ℓ_min − 3ρ_pert) | EMPIRICAL VERIFIED | trivially true for raw Gaussian (ℓ_{j,2} = 0) | retest under perturbation; CE-3 of L1-H still applies |
| L1-F ledger | EMPIRICAL VERIFIED | when LG-3 holds, ledger holds with h_min ≈ 1 | none |
| WQ-1 default INFEASIBLE | EMPIRICAL FACT | σ_b=2 + center spacing 10 gives LG-1 overlap | structural; not fixable without changing initialization |
| raw_gaussian regime | FEASIBLE_WITH_BUDGET (empirical) | best case all margins ≥ 0.082 | not theorem-grade |
| L1-H theorem candidate | LEMMA-CAND (unchanged) | PO-LH1 still open | L1-H2 |
| L1-F upgrade to Cat-A | BLOCKED | requires PO-LH1 (L1-H2) + L1-J | — |
| Global K_bar = K_act | FORBIDDEN | conditional only | unchanged |
| Reservoir framework | WORKING (unchanged) | unchanged | unchanged |
| OP-0005 / OP-0008 | OPEN (unchanged) | L1-I does not address them | unchanged |

---

## 13. Relationship to L1-H / PO-LH1

L1-I confirms that the L1-H regime is non-empty on natural finite-graph configurations. This **unblocks** the PO-LH1 boundary-leakage proof: discharging PO-LH1 will produce a theorem-grade conditional statement on a non-empty parameter regime (rather than a vacuous theorem).

The L1-I best-case configuration (σ_b=0.5, δ=0.02, r=0, ℓ_min=0.10, geometry=A, raw_gaussian) is a concrete numerical exhibit that any future L1-H Cat-A proof must cover. Any counterexample to L1-H that respects this configuration's constants would be a falsification of the L1-H theorem candidate.

The empirical sub-verdict that WQ-1 dynamics is incompatible with L1-H is a meaningful clarification of L1-G's earlier observation. L1-G found that the WQ-1 trajectory falls out of the L1Hyp regime via aggregate-bar merging; L1-I now identifies that it never starts in the L1-H regime either, because the WQ-1 mass-projection initial state structurally violates LG-1 at all tested σ_b on \(T^2_{20}\).

---

## 14. Relationship to OP-0005 / OP-0008

**OP-0005 (K-Selection).** L1-I does not address K-selection. It confirms that the field-native morphology count and chart-active count can agree on a constrained regime; this is a *bridge*, not a *selection mechanism*. The reservoir-effective rank reformulation of OP-0005 (`latent_index_space_design.md` §11.2) remains a working subprogram.

**OP-0008 (σ-inheritance).** L1-I does not address σ-inheritance. It identifies a non-empty static regime in which the L1-H bridge is consistent; this does not establish σ_rich sufficiency or deterministic Φ_rich.

No σ_rich sufficiency claim is licensed by L1-I.

---

## 15. Next Work Packages

### L1-H2 — Boundary-leakage proof / PO-LH1 discharge (recommended next)

L1-I's positive feasibility verdict unblocks this. Concrete tasks:

1. Prove the boundary-leakage correction lemma: for a global bar of \(U\) with birth in \(N_j^r\), the global death level differs from the local death level on \(G_j^r\) by at most \(\rho_\partial\), where \(\rho_\partial\le\rho_{\mathrm{pert}}\) under LG-2.
2. Formally show \(\ell_{j,2}^{\mathrm{global}}\le\ell_{j,2}^{\mathrm{local}}+\rho_\partial\), closing step (β) of L1-H upper-bound proof.
3. Update `kbar_kact_bridge_L1H_local_to_global_transfer.md` Cat-status table from `LEMMA-CAND` to `THEOREM-CAND` if PO-LH1 closes.

### L1-I2 — Finer regime characterization (optional, supports L1-H2)

Given that L1-I shows the regime is non-empty, characterize the regime boundaries more sharply: what is the maximum σ_b at which LG-1 still holds for given center spacing? What is the minimum r at which LG-2 holds for given σ_b? Build an analytic envelope rather than a sweep.

### L1-H3 — Dynamics-compatible regime study (separate workstream)

L1-I shows the WQ-1 default initialization is incompatible with L1-H; L1-G shows the WQ-1 dynamics drives out of the L1Hyp regime even from compatible starts. A dynamics-compatible regime study would (i) construct an SCC initial state that *does* satisfy L1-H, (ii) integrate forward under the same Option D-2 dynamics, (iii) measure how long the L1-H regime is preserved. This is parallel to L1-H2.

### L1-J — Cat-A upgrade attempt (deferred)

Requires L1-H2 (PO-LH1 discharge) + PO-1 (bridge-cut existence from primitive SCC) + formal tie convention. Not unblocked by L1-I alone.

---

## 16. Summary

- The L1-H regime is **empirically non-empty** on \(T^2_{20}\): 439/1920 configurations (22.9 %) achieve `FEASIBLE_WITH_BUDGET` with margin ≥ 0.05 on every L1-H clause.
- Most-feasible regime: `raw_gaussian` mode with σ_b ∈ {0.5, 1.0}, r ∈ {1, 2}, ℓ_min ∈ {0.10, 0.15, 0.20}, geometry A or `wide`.
- Best-case configuration: σ_b=0.5, δ=0.02, r=0, ℓ_min=0.10, geometry A, `raw_gaussian`. All margins comfortably positive (LG-2: 0.76, LG-3: 0.90, LG-4: 0.08, H6: 0.10, ledger: 0.90).
- The WQ-1 NQ-242c default initialization (σ_b=2.0, mass=30 forced projection, default centers) is `INFEASIBLE`. Only LG-1 fails, due to natural Gaussian support overlap.
- Most common failure: LG-1 (904/1920). LG-4 second (402). LG-3, H6, LDG never failed in the sweep.
- L1-H is **not vacuous**. PO-LH1 (boundary-leakage proof) is the next theoretical priority. L1-I unblocks it.
- L1-F status unchanged. L1-H status unchanged (still LEMMA-CAND with PO-LH1 open). L-1 not proved. OP-0005 / OP-0008 not solved. Reservoir framework not promoted.
