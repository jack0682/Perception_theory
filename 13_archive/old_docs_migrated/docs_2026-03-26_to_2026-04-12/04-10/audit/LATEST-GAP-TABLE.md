# Latest Gap Table

**Date:** 2026-04-11
**Session:** Latest remaining-gap summary
**Category:** audit
**Status:** active
**Depends on:** Canonical Spec v2.1.md §13 and §15; docs/04-10/audit/REMAINING-GAP-ANALYSIS.md

---

## 0. Current Count

| Bucket | Count | Meaning |
|---|---:|---|
| Category A | 35 | fully proved |
| Category B | 4 | proved/understood qualitatively, but quantitative/general form still has structural or empirical dependence |
| Category C | 5 | conditionally proved under non-removable regime/structural hypotheses |
| Retracted | 5 | no longer active claims |
| Research extensions | 4 | not theorem-status gaps yet, but next research blockers |

---

## 1. Formal Gap Table — Category B

| # | Gap / Item | Current status | What is missing | Next action |
|---:|---|---|---|---|
| B1 | Barrier exponent `gamma_eff ≈ 0.89` | Category B | Positive barrier / `Theta(beta)` picture is solid, but the exact fitted exponent is optimizer/path/range dependent. | Replace scalar exponent claims with branch-conditioned constants or asymptotic `Theta(beta)` statement. |
| B2 | General-graph birth supercriticality | Category B | D4/simple cases are proved; arbitrary non-D4 degenerate eigenspaces lack a general supercriticality proof. | Prove via Cheeger/spectral clustering or equivariant bifurcation for non-D4 eigenspaces. |
| B3 | Quantitative `d_min*` formula | Category B | Regression formula has strong fit, but no analytical derivation of coefficients; exp65 suggests branch dependence. | Convert to branch-conditioned bounds and validate over `lambda_rep`/grid-size sweep. |
| B4 | Beyond-Weyl 33x quantification | Category B | Structured bound is mathematical, but “33x” improvement is grid/config specific. | Report range/interval over wider grid and overlap validation instead of point factor. |

---

## 2. Formal Gap Table — Category C

| # | Gap / Item | Current status | Condition causing the gap | Next action |
|---:|---|---|---|---|
| C1 | T-Persist-1(d), exact threshold preservation | Category C | Requires structural condition `beta > 7 alpha`; condition has not been removed. | Keep condition explicit; optionally split into shifted-threshold theorem + structural exact-threshold corollary. |
| C2 | T-Persist-Full | Category C | Chains through C1, so weakest component remains conditional. | Update only if C1 is reframed or strengthened. |
| C3 | T-Persist-K-Sep | Category C | Requires well-separation WS and spectral-repulsion SR; these are regime definitions, not accidental assumptions. | Treat as a regime theorem rather than trying to erase all conditions. |
| C4 | T-Persist-K-Weak | Category C | Requires WI, SR, NB-K, and per-formation persistence assumptions. | Validate under branch-sensitive initialization and overlap sweeps. |
| C5 | T-Persist-K-Unified | Category C | Requires PS, ND, BC'-K, TC-K, SR-Lambda. | Extend parameterization with branch-selection / history state if exp65 sweep confirms need. |

---

## 3. Active Research Gaps / Next Blockers

| # | Research gap | Latest evidence | Why it matters | Next action |
|---:|---|---|---|---|
| R1 | K=2 branch-selection bifurcation | exp65/71/72/73/74/75/76/77/78 now show branch identity is continuation-sensitive, budget-sensitive, and strongly search-sensitive: on the hardest sentinel `20x20:0.6`, injected-seed direct optimization finds even lower-energy Type B branches than either the raw catalog or the plain continued branch. | `F''` and merge-barrier claims are not single scalar properties unless branch family, initialization/search protocol, and candidate catalog are specified. | Start using the new search-aware branch-selection vocabulary in R1-Q audits and, if desired, replicate one more nontrivial config analytically/numerically; search sensitivity is now observed on `10x10:0.6`, `15x15:0.6`, and `20x20:0.6`. |
| R2 | Near-bifurcation persistence (`mu -> 0`) | Still listed in Canonical Spec §15 as a remaining extension. | Determines branch selection / basin collapse through bifurcation points. | Center-manifold reduction and branch-selection analysis. |
| R3 | Multi-formation kinetic dynamics | Current theory is kinetic/barrier-based, not thermodynamic; exp65 reinforces branch/path dependence. | Needed for coarsening cascades, stochastic birth/death, and noise-driven merge rates. | Build branch-aware kinetic phase diagram. |
| R4 | Merge barrier on relaxed manifold | T-Merge path on constrained `Sigma^K_M` was retracted; relaxed-manifold F'' is branch-conditioned. | Needed to state meaningful merge barrier and transition rates. | Analyze `Sigma_M^relax` with branch-conditioned endpoints. |

---

## 4. One-Line Priority Order

| Priority | Work item | Reason |
|---:|---|---|
| 1 | family-matched catalog / source-0 anchored threshold audit | Directly tests whether the expanded Exp73 threshold variability is physical or a clustering/catalog artifact. |
| 2 | Branch-conditioned `F''(M/2)` / merge barrier statement | Required before any merge-barrier theorem cleanup. |
| 3 | `d_min*` branch-conditioned bounds | Spatial separation is downstream of branch choice. |
| 4 | General-graph birth supercriticality proof | Independent formal Category B gap. |
| 5 | T-Persist exact-threshold condition cleanup | Larger theorem-status cleanup; only worth doing after branch dynamics are clearer. |

---

## 5. Do Not Change Yet

No Canonical Spec theorem category should be changed from the current evidence alone. The latest evidence says the missing structure is **branch selection**, not proof-status reclassification.
