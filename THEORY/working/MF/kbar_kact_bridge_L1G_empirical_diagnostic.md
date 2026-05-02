# L1-G: Empirical L1Hyp Diagnostic

**File:** `THEORY/working/MF/kbar_kact_bridge_L1G_empirical_diagnostic.md`
**Document type:** non-canonical working diagnostic protocol + empirical observation
**Created:** 2026-05-02 (after L1-A through L1-F)
**Status:** working diagnostic; not theorem-grade; not Cat-A; not promotion-ready

---

## 1. Status and Scope

This is a non-canonical working note. It defines a diagnostic protocol and reports empirical observations on the L1Hyp clauses

\[
\mathrm{L1Hyp}(\varepsilon,\ell_{\min},\delta,D_{\mathrm{sep}},h_{\min},\{B_{jk}\},r_{\mathrm{assoc}},r_{\mathrm{birth}},\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\tau_{\mathrm{tie}},r)
\]

introduced by L1-F (`kbar_kact_bridge_L1F_synthesis.md` §5).

L1-G does **not**:

- prove L-1.
- promote L1-F to Cat-A.
- solve OP-0005 or OP-0008.
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) or \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally.
- claim \(\sigma_{\mathrm{rich}}\) sufficiency.
- promote reservoir theory to canonical.
- treat empirical results as a theorem.
- modify any canonical file.

The purpose is to (i) make explicit which L1Hyp clauses are *empirically measurable* on existing WQ-LAT-style outputs, (ii) classify each clause as `EXACTLY_MEASURABLE`, `PROXY_MEASURABLE`, `PARTIALLY_MEASURABLE`, or `NOT_MEASURABLE_FROM_CURRENT_OUTPUTS`, and (iii) execute a smoke-test computation to confirm the diagnostic pipeline is implementable.

---

## 2. Task Checklist

- [x] Read L1-F synthesis and L1-A through L1-E.
- [x] Read proof-status, bridge-lemma, and reservoir grounding.
- [x] Read WQ-LAT-1, WQ-LAT-1.B, ksoft_kact_diag (the available empirical lineage).
- [x] Inspect persistence / diagnostics / multi / graph / k_soft code.
- [x] Inspect existing result JSONs to determine whether per-snapshot \(\mathbf u(t)\) fields are stored.
- [x] Identify diagnostics that are not measurable from existing JSONs.
- [x] Design Level 1 (easy) and Level 2 (graph) diagnostic sets.
- [x] Specify max-min bridge-height computation via threshold scan.
- [x] Implement `CODE/scripts/l1g_l1hyp_diagnostic.py` with both `--mode rerun` and `--mode summary`.
- [x] Smoke-test the script.
- [x] Run `--mode summary` over the existing `ksoft_kact_diag.json`.
- [x] Classify each H1-H10 clause for the smoke configuration.
- [x] Preserve all non-claims.
- [x] Verify file creation.

---

## 3. Motivation from L1-F

L1-F synthesizes the conditional hard-bar / active-count bridge

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^{\varepsilon}(\mathbf u)
\]

under \(\mathrm{L1Hyp}\). The synthesis is theorem-candidate, not theorem-grade, because clauses H5, H8, H10 and the constants compatibility (PO-1..PO-9 in L1-F §9) are open.

Before any theorem-grade upgrade attempt (L1-J), the synthesis must be tested for *empirical viability*: does the WQ-LAT empirical lineage describe a regime in which \(\mathrm{L1Hyp}\) plausibly holds, fails, or is partially obeyed? If the regime is empty, the theorem candidate is vacuous; if many clauses fail, the synthesis is unrealistic.

L1-G performs this stress test. It is evidence-gathering, not proof.

---

## 4. Diagnostic Philosophy

Three principles.

**P1 - Status before pass/fail.** Each clause is first classified by *measurability* (exact / proxy / partial / not-measurable) before any pass/fail status is assigned. A clause that cannot be measured from current artifacts is reported as `UNKNOWN`, not silently treated as passing.

**P2 - Honest separation of empirical and theorem-grade content.** A `pass` status on a measurable clause is empirical evidence in favor of L1Hyp consistency on the tested configuration, not a proof. A `fail` is empirical falsification of L1Hyp on that configuration, not a refutation of the L1-F theorem candidate; L1-F may still be valid in a different regime.

**P3 - No fabrication.** Diagnostics that require per-vertex \(u^{(j)}(x)\) fields and cannot be reconstructed from a stored JSON are flagged `NOT_MEASURABLE_FROM_CURRENT_OUTPUTS` rather than estimated.

---

## 5. L1Hyp Clauses and Measurable Proxies

For convenience, the L1Hyp clauses (L1-F §5) are repeated:

- H1 active mass and \(\delta\)-support, support separation \(d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}}\);
- H2 birth/peak height \(b_j^U=U(p_j)\ge h_{\min}\);
- H3 low pairwise bridge height \(\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}\) via separating cut;
- H4 persistence-margin compatibility \(h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}\);
- H5 injective slot-to-bar association map \(\mathcal A_{\mathrm{bar}}\);
- H6 active secondary-bar suppression \(\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}\) and local perturbation \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\);
- H7 inactive residual suppression \(\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}\) plus background no-birth;
- H8 coverage \(\{B:\ell(B)\ge\ell_{\min}\}\subseteq\mathrm{Image}(\mathcal A_{\mathrm{bar}})\);
- H9 tie / plateau stability \(\tau_{\mathrm{tie}}>0\);
- H10 local-to-global barcode compatibility.

Each clause is mapped to a measurable proxy if one exists, otherwise to `NOT_MEASURABLE`.

---

## 6. Exact vs Proxy Diagnostic Levels

### Level 1 — easy measurable proxies (implemented)

- per-slot mass \(m_j(\mathbf u)\) and active set \(A^\varepsilon\);
- aggregate \(U(\mathbf u)\);
- hard-bar count \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) via terminal-death \(H_0\) superlevel persistence (`scc.diagnostics._persistence_h0_graph` + the script's `h0_barcode`);
- dominant bar lengths;
- peak heights \(b_j^U=U(\mathrm{argmax}_x u^{(j)}(x))\);
- residual height \(\|R_{\mathrm{inact}}\|_\infty\) and \(K_{\mathrm{bar}}^{\ell_{\min}}(R_{\mathrm{inact}})\);
- secondary slot bar lengths \(\ell_{j,2}\) (full-graph slot-internal terminal-death \(H_0\) barcode of \(u^{(j)}\));
- support connectedness of \(S_j^\delta\) (DFS on induced subgraph);
- pairwise support graph distances \(d_G(S_j^\delta,S_k^\delta)\) (multi-source BFS);
- raw margin \(h_{\min}^{\mathrm{measured}}-\max_{k\neq j}\theta_{\mathrm{bridge}}^{jk}-\ell_{\min}\); the L1Hyp constants \(r_{\mathrm{assoc}},r_{\mathrm{birth}}\) cannot be estimated from data alone, so the raw margin is reported without those error budgets.

### Level 2 — harder graph diagnostics (partially implemented)

- max-min bridge height \(\theta_{\mathrm{bridge}}^{jk}(U)\) via the **descending threshold scan** (Option B of the L1-G guidance):
  - sort vertices by \(U\) descending;
  - union-find merge as each vertex is added with already-active neighbors;
  - the bridge height is the value of the most-recently added vertex when both peaks \(p_j,p_k\) first lie in the same component.
- exact best-cut height \(H_{\mathrm{cut}}^{jk}(U)\) — not implemented; future work.
- slot-to-bar association map \(\mathcal A_{\mathrm{bar}}\) — not implemented; would require birth-vertex tracking through the union-find merges and a tie convention.
- local-to-global barcode mismatch indicator — inherently theorem-shaped, not directly measurable.
- explicit residual-created bar detection — proxy via `K_bar(R_inact) > 0` only.

The threshold-scan bridge is robust on finite graphs and uses only adjacency. It is theoretically equivalent to the widest-path interpretation in Option A.

---

## 7. Diagnostic Metrics

For each per-snapshot multi-formation state \(\mathbf u\), the script computes:

| Symbol | Formula | Source |
|---|---|---|
| \(m_j\) | \(\sum_x u^{(j)}(x)\) | `per_snapshot_diagnostic.masses[j]` |
| \(A^\varepsilon\) | \(\{j: m_j>\varepsilon\}\) | `per_snapshot_diagnostic.active_set` |
| \(U\) | \(\sum_j u^{(j)}\) | aggregate |
| \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) | \(\#\{i:\ell_i\ge\ell_{\min}\}\), terminal-death | `h0_barcode(U)` + `k_bar` |
| \(b_j^U\) | \(U(\mathrm{argmax}_x u^{(j)}(x))\) | per-active-slot |
| \(\ell_{j,1},\ell_{j,2}\) | top two bars of \(\mathrm{Bars}_0^{\mathrm{term}}(u^{(j)};G)\) | `h0_barcode(u_j)` |
| \(S_j^\delta\) | \(\{x:u^{(j)}(x)>\delta\}\) | `support_delta` |
| \(d_G(S_j^\delta,S_k^\delta)\) | multi-source BFS distance | `support_distance` |
| \(\theta_{\mathrm{bridge}}^{jk}(U)\) | descending threshold scan max-min | `threshold_scan_bridge_height` |
| \(R_{\mathrm{inact}}\) | \(\sum_{j\notin A^\varepsilon}u^{(j)}\) | `R_inact` |
| \(\|R_{\mathrm{inact}}\|_\infty\) | infinity norm | summary |
| \(K_{\mathrm{bar}}^{\ell_{\min}}(R_{\mathrm{inact}})\) | residual barcode count | `h0_barcode(R_inact)` |
| coverage excess | \(K_{\mathrm{bar}}-K_{\mathrm{act}}\) | summary |

The threshold-scan bridge is capped at a configurable number of pairs per snapshot (default 6) to bound runtime.

---

## 8. Expected Input Data

### 8.1 Existing artifacts

| File | What it contains | What it lacks |
|---|---|---|
| `CODE/scripts/results/ksoft_kact_diag.json` | per-snapshot \(K_{\mathrm{act}},K_{\mathrm{bar}},K_{\mathrm{soft}},\mathcal F,\) per-slot masses \(m_j\), pairwise overlaps, `min_support_distance`, dominant bar lengths (top-8), regime label, for both A and B trajectories | per-vertex fields \(u^{(j)}(x)\), full barcode, support masks, full pairwise distance matrices, \(U\) field, residual field |
| `CODE/scripts/results/wq_lat1_reservoir_resolution_sweep.json` | per-trajectory \(K_{\mathrm{act}}\), \(K_{\mathrm{bar}}\) at four thresholds, \(K_{\mathrm{soft}}\), \(\mathcal F\), `dominant_bars_initial/final`, `final_aggregate` (the aggregate \(U\) at final snapshot only) | per-snapshot fields, per-slot fields, support masks, intermediate \(U\) snapshots |
| `CODE/scripts/results/wq_lat1b_phi_envelope_refinement.json` | bars per run for envelope sweep | per-snapshot trajectories |
| `CODE/scripts/results/nq242c_results.json` | sigma_pre / sigma_post, criteria, trajectory-level stats | per-snapshot fields |

### 8.2 Confirmed inspection (run 2026-05-02)

`ksoft_kact_diag.json::trajectory_A` keys:
```
['name','centers','snapshot_times','K_act','K_bar','K_soft',
 'F_aggregate','F_per_formation','dominant_bar_lengths',
 'subdominant_bar_count','pairwise_overlaps',
 'min_support_distance','max_overlap','regime_label',
 'm_j_trajectory','jump_time','no_k_jump']
```

The keys do not include any per-vertex `fields` array. **Therefore most L1Hyp diagnostics (H2 birth heights, H3 bridge heights, H4 raw margin, H6 \(\ell_{j,2}\), H7 residual height, full H1 connectedness) cannot be computed from `ksoft_kact_diag.json` alone and require `--mode rerun`.**

`wq_lat1_reservoir_resolution_sweep.json` likewise omits per-snapshot fields.

This is reported to the user explicitly. No diagnostic is silently estimated.

---

## 9. Script Design

### 9.1 Files

- `CODE/scripts/l1g_l1hyp_diagnostic.py` — single-file diagnostic.
- `CODE/scripts/results/l1g_l1hyp_diagnostic_smoke.json` — smoke-test output.
- `CODE/scripts/results/l1g_l1hyp_diagnostic_summary.json` — summary-mode output (over existing `ksoft_kact_diag.json`).

### 9.2 Modes

- `--mode rerun` (default): regenerates the WQ-1 (NQ-242c) configuration-A and configuration-B trajectories deterministically, accesses full per-snapshot multi-formation fields, and computes the full Level 1 diagnostic + the threshold-scan bridge height for at most `--bridge_max_pairs` pairs.
- `--mode summary`: reads an existing diagnostic JSON (designed for `ksoft_kact_diag.json` schema), computes the partial diagnostic that depends only on stored summary statistics, and explicitly flags unavailable diagnostics.

### 9.3 CLI surface

```
--mode {rerun,summary}    default rerun
--input PATH              required for summary mode
--output PATH             always required
--l_min FLOAT             default 0.10
--epsilon FLOAT           default 0.225
--delta FLOAT             default 0.05
--seed INT                default 42
--max_iter INT            default 5000
--snapshot_every INT      default 25
--lambda_rep FLOAT        default 10.0
--max_snapshots INT       optional subsampling for fast smoke tests
--bridge_max_pairs INT    cap on pairwise bridge computations (default 6)
--compress_B INT          override centers_B[2] = (10, compress_B)
```

### 9.4 Reuse, not reimplementation

- terminal-death \(H_0\) barcode reuses the same union-find recipe as `scc.diagnostics._persistence_h0_graph` (the canonical-aligned convention; see L1-C §3 code check), with the surviving component appended as `(max(u), 0.0)`.
- `nq242c_counterexample.run_trajectory` is reused verbatim for trajectory regeneration; no dynamics is re-implemented.
- `ParameterRegistry` is reused.

### 9.5 Forbidden non-claims (preserved by the script)

The output JSON includes a `non_claims` block listing every forbidden claim of L1-G as `False`. Future readers should not interpret a `STRONG_SUPPORT` outcome as a theorem.

---

## 10. Result Schema

Top-level JSON keys:

```
script, script_version, purpose, non_claims, result, metadata
```

`result` (rerun mode):

```
{
  "mode": "rerun",
  "trajectory_A": {
    "name", "centers", "n_snapshots",
    "snapshots": [
      {
        "tau", "diagnostic": { ... per_snapshot_diagnostic ... },
        "clauses": { "H1": {...}, ..., "H10": {...} },
        "outcome": "STRONG_SUPPORT|WEAK_SUPPORT|MIXED|FAIL|INCONCLUSIVE",
        "counts": {"pass", "fail", "unknown"}
      },
      ...
    ],
    "trajectory_outcome", "no_k_jump", "jump_time"
  },
  "trajectory_B": { ... },
  "config": { ... },
  "wall_clock_seconds": float
}
```

`result` (summary mode):

```
{
  "mode": "summary",
  "source_input", "trajectories": { ... },
  "unavailable_diagnostics": [...]
}
```

Each clause record carries `{status, value, threshold, pass, note}` where `status` is one of the four measurability tags, `pass` is `True / False / None`, and `note` includes any caveats.

---

## 11. Empirical Run Summary

Two runs were executed on 2026-05-02.

### 11.1 Smoke test (`--mode rerun --max_iter 200 --max_snapshots 4 --bridge_max_pairs 3`)

- 4 snapshots per trajectory at `tau ∈ {0, 67, 133, 200}` (subsampled from a 200-iter run on `T^2_{20}`, seed 42, default WQ-1 configuration).
- Both trajectories: `no_k_jump = True`.
- Trajectory outcomes: `FAIL` (driven by H1 at \(\tau=0\)).

Per-snapshot detail (trajectory A):

| \(\tau\) | \(K_{\mathrm{act}}\) | \(K_{\mathrm{bar}}\) | H1 | H2 | H3 | H4 | H6 | H7 | H8 | H9 | outcome |
|---:|---:|---:|---|---|---|---|---|---|---|---|---|
| 0 | 3 | 3 | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| 67 | 3 | 3 | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| 133 | 3 | 3 | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| 200 | 3 | 3 | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |

Concrete numerical evidence at \(\tau=0\):
- `pair_distances = {0-1: 0.0, 0-2: 1.0, 1-2: 1.0}`. The 0-1 distance is exactly 0 because the Gaussian initial bumps with \(\sigma_b=2\) overlap above \(\delta=0.05\); supports are not graph-disjoint. **H1 fails on support separation, not on connectedness or activity.**
- `pair_bridge_heights = {0-1: 0.108, 0-2: 0.088, 1-2: 0.088}`.
- `b_j^U = (1.0005, 1.0005, 1.0004)`, `h_min_measured = 1.0004`.
- `raw_margin = h_min - max_bridge - l_min = 1.0004 - 0.108 - 0.10 = 0.792` (positive).
- `R_inact_inf = 0`, `K_bar(R_inact) = 0`.
- `slot_l2 = (0, 0, 0)` (clean unimodal slots in this corner-saturated regime).

So the only failing critical clause throughout the smoke test is **H1 (support separation \(d_G(S_j^\delta,S_k^\delta) > 0\) for all active pairs)**. Its failure is an artifact of the Gaussian-bump initialization at \(\sigma_b=2\), which makes \(S_j^\delta\) overlap above \(\delta=0.05\). All other measurable clauses are consistent with L1Hyp at this stage.

### 11.2 Summary mode over `ksoft_kact_diag.json` (full 5000-iter trajectory, 201 snapshots)

- 201 snapshots per trajectory (A and B).
- The summary-mode diagnostic has access only to `K_act, K_bar, dominant_bar_lengths, m_j, min_support_distance` (per-vertex fields not stored).
- H2, H3, H4, H6, H7 all marked `NOT_MEASURABLE_FROM_CURRENT_OUTPUTS`.
- H1 marked `PARTIALLY_MEASURABLE` (we have `min_support_distance` but not connectedness).
- H8 (coverage excess) is `EXACTLY_MEASURABLE` from the stored \(K_{\mathrm{act}},K_{\mathrm{bar}}\) sequences.

| Trajectory | Initial \((K_{\mathrm{act}},K_{\mathrm{bar}})\) | Final \((K_{\mathrm{act}},K_{\mathrm{bar}})\) | H8 final coverage_excess | First snapshot outcome | Last snapshot outcome |
|---|---|---|---|---|---|
| A | (3, 3) | (3, 1) | \(-2\) | MIXED | FAIL |
| B | (3, 3) | (3, 1) | \(-2\) | MIXED | FAIL |

**Result.** Across the 201-snapshot WQ-1 trajectory, both A and B exhibit the WQ-2 F-B6 phenomenon: \(K_{\mathrm{act}}\) is rigid at 3 while \(K_{\mathrm{bar}}^{0.10}(U)\) drops from 3 to 1. **H8 fails by undercount of 2** at the end of every trajectory. The L1Hyp coverage clause (and therefore the L1-F equality \(K_{\mathrm{bar}}=K_{\mathrm{act}}\)) does not hold along the WQ-1 F2 trajectories beyond the initial corner-saturated stage.

This is empirical falsification of L1Hyp on the tested configuration. It is **not** a refutation of L1-F. L1-F is a theorem candidate stated *under* L1Hyp; the present finding is that the WQ-1 trajectories do not lie in the L1Hyp regime, not that the conditional implication fails.

---

## 12. Clause-by-Clause Diagnostic Table

Compact summary of the implementation status, evidence, and limitations per clause. Status column is the *measurability* status (capacity to evaluate empirically), independent of whether the clause currently passes.

| Clause | Metric | Status | Evidence (smoke / summary mode) | Limitation |
|---|---|---|---|---|
| H1 | \(m_j\), \(A^\varepsilon\), \(\mathrm{conn}(G[S_j^\delta])\), \(d_G(S_j^\delta,S_k^\delta)\) | EXACTLY_MEASURABLE (rerun); PARTIALLY_MEASURABLE (summary) | smoke: H1 FAIL because \(d_G(S_0^\delta,S_1^\delta)=0\) with Gaussian \(\sigma_b=2\), \(\delta=0.05\) | summary mode lacks support masks |
| H2 | \(b_j^U=U(p_j)\) | EXACTLY_MEASURABLE (rerun) | smoke: \(b_j^U\approx 1.0\), \(h_{\min}\approx 1.0\); H2 PASS | requires per-vertex \(U\) |
| H3 | threshold-scan \(\theta_{\mathrm{bridge}}^{jk}(U)\) | PROXY_MEASURABLE (rerun) | smoke: max bridge \(\approx 0.108\); H3 PASS at \(\ell_{\min}=0.10\) | exact min-cut height not implemented |
| H4 | \(h_{\min}-\max_{k\neq j}B_{jk}-\ell_{\min}\) | PARTIALLY_MEASURABLE (rerun) | smoke: raw margin \(\approx 0.79\); H4 PASS, but \(r_{\mathrm{assoc}},r_{\mathrm{birth}}\) absent | error budgets cannot be estimated empirically |
| H5 | injective \(\mathcal A_{\mathrm{bar}}\) | NOT_MEASURABLE_FROM_CURRENT_OUTPUTS | UNKNOWN | requires birth-vertex tracking through filtration |
| H6 | \(\ell_{j,2}\) (slot-internal full-graph \(H_0\) terminal-death) | PROXY_MEASURABLE (rerun) | smoke: \(\ell_{j,2}=0\) for all active \(j\); H6 PASS | local-graph version not implemented |
| H7 | \(\|R_{\mathrm{inact}}\|_\infty\), \(K_{\mathrm{bar}}(R_{\mathrm{inact}})\) | PROXY_MEASURABLE (rerun) | smoke: residual height 0, residual count 0; H7 PASS | aggregate corridor-reinforcement not separately measured |
| H8 | \(K_{\mathrm{bar}}^{\ell_{\min}}(U)-K_{\mathrm{act}}^{\varepsilon}(\mathbf u)\) | EXACTLY_MEASURABLE (both modes) | smoke: \(0\) (PASS); summary: \(-2\) at end (FAIL) | none; this is the most informative clause |
| H9 | min gap among dominant bars and \(\ell_{\min}\) | PROXY_MEASURABLE | smoke: nontrivial gap; PASS | true \(\tau_{\mathrm{tie}}\) requires plateau detection |
| H10 | local-to-global barcode transfer | NOT_MEASURABLE_FROM_CURRENT_OUTPUTS | UNKNOWN | theorem-grade gap by design |

Aggregate outcome rules used by the script:

- `FAIL` if H1 / H2 / H3 / H6 / H7 / H8 has explicit `pass=False`.
- `STRONG_SUPPORT` if H1, H2, H3, H4, H6, H7, H8 all pass (H5, H9, H10 may be unknown).
- `WEAK_SUPPORT` if H1 and H8 pass and no critical clause fails.
- `MIXED` if there is at least one pass and one explicit fail outside the FAIL set.
- `INCONCLUSIVE` otherwise.

---

## 13. Failure Modes

### L1G-F1 - Unavailable per-vertex fields

`ksoft_kact_diag.json` and `wq_lat1_reservoir_resolution_sweep.json` do not store per-snapshot multi-formation fields. Diagnostics that require \(u^{(j)}(x)\) are unavailable in summary mode. The script flags them explicitly.

### L1G-F2 - Initialization-driven H1 failure

Gaussian initial bumps at \(\sigma_b=2\) on \(T^2_{20}\) overlap above \(\delta=0.05\), forcing `pair_distance = 0` and H1 fail at \(\tau=0\). This is a property of the WQ-1 initialization, not of the dynamics. A diagnostic over a different graph or initialization may not exhibit this failure.

### L1G-F3 - Aggregate-bar collapse without slot extinction (the WQ-2 F-B6 mode)

\(K_{\mathrm{act}}=3\), \(K_{\mathrm{bar}}=1\) → coverage excess \(-2\). H8 fails by undercount, not overcount. Per L1F-F1 (terminal-death convention) and L1F-F3 (association failure), this is a slot-to-bar association breakdown induced by aggregate merging in the corner-saturated → overlap regime transition.

### L1G-F4 - Threshold-scan determinism

The `np.argsort(-U, kind="stable")` ordering breaks ties deterministically by index. This matches the persistence union-find but does **not** match a tie-stable mathematical definition. The H9 plateau-stability proxy reports a positive gap in the smoke test, but at exact ties the threshold-scan bridge can flip vertex by vertex with arbitrarily small perturbations.

### L1G-F5 - Bridge-pair cap

Default `--bridge_max_pairs = 6` caps the number of pairwise bridge computations per snapshot. For \(K_{\mathrm{field}}\le 12\) and \(K_{\mathrm{act}}\le 6\) the cap is non-binding; for larger \(K\) the cap should be raised.

### L1G-F6 - L1Hyp constant gap

\(r_{\mathrm{assoc}}\), \(r_{\mathrm{birth}}\), \(\rho_{\mathrm{pert}}\), \(\rho_{\mathrm{res}}\), \(\tau_{\mathrm{tie}}\) are L1Hyp budget constants whose values are not derivable from the data alone. The diagnostic reports raw margins and slot bar lengths; a future feasibility study (L1-I) must check whether non-empty constant assignments exist.

### L1G-F7 - Local-to-global gap

H10 is theorem-shaped, not empirical. The diagnostic returns `UNKNOWN` for H10 by design. No amount of L1-G data alone can fill PO-6.

### L1G-F8 - Configuration / dynamics scope

All evidence in this note is restricted to \(T^2_{20}\), Option D-2 dynamics, WQ-1 default parameters. No claim of generalization is made to other graphs, dynamics, or initializations.

---

## 14. Cat-Status and Evidence Table

| Item | Cat-status | Evidence | Limitation |
|---|---|---|---|
| Script `l1g_l1hyp_diagnostic.py` | WORKING-DEF | smoke test PASS; both modes execute; deterministic seed | not unit-tested; subsampling may hide intermediate behavior |
| Threshold-scan bridge | CAT-A local finite-graph fact (Option B equivalent to widest path) | implemented; tested on smoke configuration | tie convention is index-based, not field-natural |
| H1 measurability | EXACTLY_MEASURABLE (rerun) | passes/fails reflect actual graph distances | summary mode is partial |
| H8 measurability | EXACTLY_MEASURABLE | both summary and rerun verify; matches WQ-2 F-B6 | none |
| H5 / H10 | NOT_MEASURABLE | unaffected by script | theorem-grade, not empirical |
| L1Hyp WQ-1 verdict (F2 trajectory, A and B) | EMPIRICAL | summary mode shows H8 undercount = -2 at end of both trajectories | only one configuration; \(T^2_{20}\), Option D-2 |
| L1-F theorem candidate | LEMMA-CAND (unchanged) | L1-G does not affect L1-F's status | not promoted; not refuted |
| L-1 hard-bar bridge | LEMMA-CAND (unchanged) | L1-G is evidence about regime existence, not bridge proof | not promoted |
| OP-0005, OP-0008 | OPEN (unchanged) | L1-G does not address them | not solved |
| Reservoir framework | WORKING (unchanged) | L1-G does not affect canonical status | not promoted |

---

## 15. Relationship to L1-F

L1-G is the empirical companion to L1-F.

L1-F asserts a conditional theorem candidate: \(\mathrm{L1Hyp}\Rightarrow K_{\mathrm{bar}}=K_{\mathrm{act}}\). It does not claim that the antecedent is non-vacuous, nor that any observed configuration satisfies it.

L1-G measures, on the available WQ-1 / WQ-LAT empirical lineage:

- which clauses are *exactly verifiable* (H1 active mass / support, H8 coverage at the integer level);
- which are verifiable only as *proxies* (H3 threshold-scan bridge instead of exact min-cut, H6 slot-internal full-graph \(\ell_{j,2}\) instead of local-graph variant, H7 residual height + barcode count);
- which are *partially verifiable* with un-estimable error budgets (H4 raw margin minus unknown \(r_{\mathrm{assoc}}\), \(r_{\mathrm{birth}}\));
- which are *not measurable* (H5 association map, H10 local-to-global transfer).

The 2026-05-02 empirical run finds that the WQ-1 F2 trajectories on \(T^2_{20}\) **do not** satisfy the H8 coverage clause beyond the initial corner-saturated stage: aggregate \(K_{\mathrm{bar}}\) drops from 3 to 1 while \(K_{\mathrm{act}}\) remains at 3. This is the WQ-2 F-B6 failure mode reread under the L1Hyp lens.

**Interpretation.** The L1-F implication is conditional. The empirical record shows that the implication's antecedent does not hold along the WQ-1 trajectory. Therefore L1-F does not assert anything about this trajectory, and the trajectory neither supports nor falsifies L1-F as a conditional theorem.

What the empirical record *does* show:

- \(\mathrm{L1Hyp}\) describes a *regime* — the high-margin, well-separated, fully-supported, corner-clear regime — that is **not** generic on \(T^2_{20}\) under Option D-2 dynamics from Gaussian-bump initial states.
- L1-F is therefore **not vacuous in principle** (the smoke-test initial-state stage shows H2-H9 all pass simultaneously, so a non-empty regime exists in the graph state space), but it is **not realized along the production WQ-1 dynamics**.
- A theorem-grade upgrade to L1-F should also produce a regime characterization clause: not only must \(\mathrm{L1Hyp}\) be sufficient, it must be empirically achievable for some natural class of states.

L1-G does not change L1-F's Cat-status. It clarifies the boundary of L1-F's applicability and motivates L1-I (constants feasibility) as an explicit precondition for any Cat-A upgrade attempt (L1-J).

---

## 16. Next Work Packages

### L1-H — Local-to-global barcode transfer theorem

H10 is the central theorem-grade gap. Empirical diagnostics cannot close it. A theorem proving (or counterexampling) that local active-slot and residual barcode controls transfer to the global aggregate \(U\) barcode is the next theoretical priority.

### L1-I — Constants feasibility study

Verify that the L1Hyp constant inequalities

\[
h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}},
\quad
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}},
\quad
\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}
\]

are simultaneously satisfiable in some non-empty regime. The smoke-test record at \(\tau=0\) (excluding H1) is consistent with positive feasibility, but a systematic parameter sweep is needed.

### L1-G+ extensions (optional)

- generalize the diagnostic to `wq_lat1_reservoir_resolution_sweep` runs with field-saving enabled in a refactored script (small change to that script's `run_one_trajectory`);
- add Level 2 exact min-cut height computation on small graphs;
- add a slot-to-bar association proxy via union-find merge tracking;
- add a tie-stable \(\tau_{\mathrm{tie}}\) plateau detector;
- run the diagnostic on R23 minimizers (overlap regime, expected H1 / H8 failure) for contrast.

### L1-G empirical extensions

- repeat on initialization variants with greater spatial separation (e.g. non-overlapping Gaussian supports, \(\sigma_b\le 1\)) to find natural states that satisfy H1;
- repeat across `compress_B` settings to cover the full ksoft_kact `--sweep` lineage;
- repeat across LAT-A / LAT-C options of the WQ-LAT-1 sweep to confirm the H8 phenomenon is not a single-configuration artifact.

### L1-J — Cat-A upgrade attempt

Defer until L1-H, L1-I, and L1-G+ produce positive evidence or constructive feasibility. L1-G alone does not motivate a Cat-A upgrade.

---

## 17. Summary

L1-G defines a diagnostic protocol for the L1Hyp clauses introduced by L1-F and reports an empirical observation on the available WQ-LAT empirical lineage.

The protocol classifies each H1-H10 clause into one of `EXACTLY_MEASURABLE`, `PROXY_MEASURABLE`, `PARTIALLY_MEASURABLE`, `NOT_MEASURABLE_FROM_CURRENT_OUTPUTS`. The script `CODE/scripts/l1g_l1hyp_diagnostic.py` implements both `--mode rerun` (regenerates trajectories with field access) and `--mode summary` (reads existing summary JSON and reports partial diagnostics with explicit unavailability flags).

Smoke test (max_iter=200, 4 snapshots): trajectory outcome `FAIL` driven entirely by H1 support-separation failure caused by \(\sigma_b=2\) Gaussian initial-state overlap above \(\delta=0.05\). H2-H9 measurable clauses all PASS at all sampled snapshots.

Summary mode over the production `ksoft_kact_diag.json` (201 snapshots): trajectory outcome `FAIL` driven by H8 coverage excess of \(-2\) at the end of both A and B trajectories. \(K_{\mathrm{act}}\) is rigid at 3, \(K_{\mathrm{bar}}^{0.10}(U)\) collapses to 1. This is the WQ-2 F-B6 phenomenon reread as L1Hyp falsification.

L1-G does **not** prove L-1, does **not** promote L1-F, does **not** solve OP-0005 or OP-0008, and does **not** treat empirical data as a theorem. It clarifies that the L1-F theorem candidate is conditional, that the antecedent is not generic on the WQ-1 production trajectory, and that the next theoretical priorities are L1-H (local-to-global) and L1-I (constants feasibility).
