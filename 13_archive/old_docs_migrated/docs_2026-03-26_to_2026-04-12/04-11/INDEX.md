# 04-11 Index

**Date:** 2026-04-11
**Focus:** SCC branch-family threshold audit and post-Exp73 family-matching analysis

---

## 1. Experiment Documents

| File | Description | Status |
|---|---|---|
| `experiment/EXP74-FAMILY-MATCH-PRELIMINARY.md` | Family-matched comparison of global vs within-family frozen crossings on top of Exp73 catalogs | complete |
| `experiment/EXP74-HIGH-BUDGET-ROBUSTNESS.md` | High-budget robustness sweep over catalog budget and family-distance thresholds | complete |
| `experiment/EXP75-TYPEB-SEEDED-CONTINUATION-20x20_c0.6.md` | Targeted seeded continuation showing Type B-like positive-lambda persistence on the hardest sentinel | complete |
| `experiment/EXP76-FINE-SEEDED-CONTINUATION-20x20_c0.6.md` | Fine warm continuation showing Type B label persists through lambda=1.0 | complete |
| `experiment/EXP77-SELECTION-VS-PERSISTENCE-20x20_c0.6.md` | Total-energy comparison between the persistent branch and raw-catalog competitors | complete |
| `experiment/EXP78-SEARCH-PROTOCOL-UPGRADE-20x20_c0.6.md` | Direct optimization with injected continuation seed on representative lambdas | complete |
| `experiment/EXP78-CROSS-CONFIG-15x15_c0.6.md` | Cross-config follow-up showing the same search sensitivity on 15x15:0.6 | complete |
| `experiment/EXP78-CROSS-CONFIG-10x10_c0.6.md` | Third-config follow-up showing the same search sensitivity on 10x10:0.6 | complete |
| `experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md` | First direct diagnostic supporting continuation-accessible valleys | complete |
| `experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md` | Local basin proxy showing 100% return to the continued Type B family | complete |
| `experiment/EXP80-DENSE-BASIN-SCALING-20x20_c0.6.md` | Dense sigma ladder showing 100% return across the tested local basin range | complete |
| `experiment/CONTINUATION-ACCESS-CROSS-CONFIG-15x15_c0.6.md` | Cross-config replication of the hard-to-enter / easy-to-keep pattern | complete |
| `experiment/EXP81-ACTIVE-SET-TRANSITION-PROXY-20x20_c0.6.md` | Raw vs seeded coarse-region transition comparison | complete |
| `experiment/EXP82-ACCESS-PATH-TRAJECTORY-20x20_c0.6.md` | Raw vs seeded energy/overlap corridor comparison | complete |

## 2. Experiment Scripts / Results

| File | Description | Status |
|---|---|---|
| `../experiments/exp74_branch_family_match.py` | Family-matching layer for Exp73 catalog outputs | complete |
| `../experiments/results/exp74_family_match_summary.json` | Exp74 machine-readable summary | complete |
| `../experiments/results/exp74_family_match_summary.csv` | Exp74 tabular summary | complete |
| `../experiments/results/exp73_catalog_hi_*.json/.csv` | High-budget Exp73 sentinel catalogs | complete |
| `../experiments/results/exp74_family_match_hi_t*.json/.csv` | Threshold-swept high-budget Exp74 summaries | complete |
| `../experiments/exp75_typeb_seeded_continuation.py` | Targeted seeded continuation experiment for recovered Type B branches | complete |
| `../experiments/results/exp75_typeb_seeded_continuation_20x20_0.6.json/.csv` | Exp75 seeded continuation outputs | complete |
| `../experiments/exp76_fine_seeded_continuation.py` | Fine-grid warm continuation from the recovered Type B seed | complete |
| `../experiments/results/exp76_fine_seeded_continuation_20x20_0.6.json/.csv` | Exp76 fine continuation outputs | complete |
| `../experiments/exp77_selection_vs_persistence.py` | Matched-lambda total-energy comparison script | complete |
| `../experiments/results/exp77_selection_vs_persistence_20x20_0.6.json/.csv` | Exp77 selection-vs-persistence outputs | complete |
| `../experiments/exp78_search_protocol_upgrade.py` | Search-upgrade comparison script | complete |
| `../experiments/results/exp78_search_protocol_upgrade_20x20_0.6.json/.csv` | Exp78 upgraded-search outputs | complete |
| `../experiments/results/exp78_search_protocol_upgrade_15x15_0.6.json/.csv` | Exp78 cross-config follow-up outputs | complete |
| `../experiments/exp79_continuation_access_diagnostic.py` | Direct continuation-access diagnostic script | complete |
| `../experiments/results/exp79_continuation_access_20x20_0.6_l05.json/.csv` | Exp79 continuation-access outputs | complete |
| `../experiments/exp80_local_basin_proxy.py` | Local basin proxy around the continued branch | complete |
| `../experiments/results/exp80_local_basin_proxy_20x20_0.6_l05.json/.csv` | Exp80 local-basin outputs | complete |
| `../experiments/results/exp80_local_basin_proxy_20x20_0.6_l05_dense.json/.csv` | Dense Exp80 basin-scaling outputs | complete |
| `../experiments/results/exp79_continuation_access_15x15_0.6_l05.json/.csv` | 15x15 continuation-access replication outputs | complete |
| `../experiments/results/exp80_local_basin_proxy_15x15_0.6_l05.json/.csv` | 15x15 local-basin replication outputs | complete |
| `../experiments/exp81_active_set_transition_proxy.py` | Coarse active-set / penalty-region transition proxy | complete |
| `../experiments/results/exp81_active_set_transition_proxy_20x20_0.6_l05.json/.csv` | Exp81 transition-proxy outputs | complete |
| `../experiments/exp82_access_path_trajectory.py` | Raw-vs-seeded trajectory profile experiment | complete |
| `../experiments/results/exp82_access_path_trajectory_20x20_0.6_l05.json/.csv` | Exp82 trajectory-profile outputs | complete |

## 3. Theory Notes

| File | Description | Status |
|---|---|---|
| `theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md` | Search-aware vocabulary separating discovered, persistent, and protocol-selected branches | active |
| `theory/BASIN-ACCESS-ASYMMETRY-MECHANISM-NOTE.md` | Analytic mechanism note for continuation access and search failure | complete |
| `theory/BASIN-ACCESS-GEOMETRY-STATEMENT.md` | Compact non-theorem geometry statement summarizing the current picture | complete |
| `theory/BASIN-ACCESS-CONJECTURE-SUPPORT-LADDER.md` | Formal status ladder from geometry statement to open theorem target | complete |

## 4. Proof Notes

| File | Description | Status |
|---|---|---|
| `proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md` | Compact numerical-support proposition for protocol-dependent selected-branch inference | complete |
| `proof/SEL-UPGRADE-BRANCH-SELECTION-SUPPORT-PROPOSITION.md` | Compact numerical-support proposition for protocol-dependent selected-branch inference | complete |

## 4. Proof Notes

| File | Description | Status |
|---|---|---|
| `proof/CONTINUATION-ACCESS-SUPPORT-PROPOSITION.md` | Cross-config support proposition for continuation access | complete |
| `proof/RUNG-4-BASIN-ACCESS-THEOREM-OUTLINE.md` | Explicit hypothesis outline for the search-neutral rung-4 basin-access theorem target | active |
| `proof/RUNG-4-BASIN-ACCESS-THEOREM-CANDIDATE.md` | Named theorem-candidate statement with H1-H6 evidence-status table | active |

## 5. Audit Notes

| File | Description | Status |
|---|---|---|
| `audit/R1-Q-PROTOCOL-TAGGED-REFORMULATION.md` | Protocol-tagged split of R1-Q into persistence, selection, and search-reliability questions | complete |
| `audit/R1-Q-STATUS-NOTE-PROTOCOL-TAGGED.md` | Compact canonical R1-Q status note using protocol tags | complete |
| `audit/R1-Q-LANE-DECISION.md` | Chooses protocol-fixed branch-selection support as the next lane | complete |
| `audit/ANALYTIC-SEARCH-FAILURE-HYPOTHESES.md` | Records the main analytic hypotheses for why raw search misses lower-energy Type B branches | complete |
| `audit/R1-Q3-DIAGNOSTIC-DESIGN-DECISION.md` | Selects continuation-accessible valleys as the first instrumented mechanism | complete |
| `audit/R1-Q3-ANALYTIC-LANE-COMPARISON.md` | Chooses continuation-access/basin-access as the stronger explanatory line | complete |
| `audit/CONTINUATION-ACCESS-CONJECTURE-REGISTER.md` | Conjecture register for the leading analytic R1-Q3 hypothesis | complete |
| `audit/CONTINUATION-ACCESS-FOLLOWUP-DECISION.md` | Chooses cross-config replication before local scaling refinement | complete |
| `audit/CONTINUATION-ACCESS-POST-PROP-LANE-DECISION.md` | Chooses analytic mechanism work over a third replication | complete |
| `audit/BASIN-ACCESS-QUANTITATIVE-FOLLOWUP-DECISION.md` | Chooses basin-size proxy scaling as the next quantitative step | complete |
| `audit/ACCESS-PATH-DIAGNOSTIC-DESIGN.md` | Designs the next raw-vs-seeded trajectory comparison using energy and overlap profiles | complete |
| `audit/CONTINUATION-ACCESS-EVIDENCE-CHAIN.md` | Compact analytic evidence chain linking Exp79, Exp80, and Exp82 | complete |
| `audit/POST-EVIDENCE-CHAIN-LANE-DECISION.md` | Chooses basin-access geometry abstraction over another replication | complete |
| `audit/POST-GEOMETRY-LANE-DECISION.md` | Chooses formal ladder construction over more near-term diagnostics | complete |
| `audit/NEXT-RUNG-CHOICE.md` | Compares strengthening rung 3 versus outlining explicit rung-4 hypotheses and chooses the theorem-target outline first | complete |
| `audit/H4-VS-FIXED-PROTOCOL-LANE-DECISION.md` | Chooses the fixed-protocol theorem lane before the deeper H4 analytic-access blocker | complete |

## 4. Audit Notes

| File | Description | Status |
|---|---|---|
| `audit/R1-Q-LANE-DECISION.md` | Chooses protocol-fixed branch-selection support as the next lane | complete |
