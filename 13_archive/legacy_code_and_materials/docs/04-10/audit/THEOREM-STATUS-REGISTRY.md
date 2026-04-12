# Theorem Status Registry

**Date:** 2026-04-10
**Session:** Cycle 1 theorem-status registry
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/GAP-REGISTRY.md; Canonical Spec v2.1.md §13

---

## Status Delta for Cycle 1

| Claim | Prior status | Cycle-1 outcome | Canonical Spec change? |
|---|---|---|---|
| R1-P local branch continuation | Implicit / not registered | REFORMULATED AND PROVED under explicit KKT nondegeneracy and fixed active-set hypotheses | No, auxiliary support result only |
| Universal scalar Type A/B classification | Informal research hypothesis | FALSE UNIVERSALIZATION OF BRANCH-SPECIFIC FACT | No, not a Canonical theorem |
| R1-Q quantitative branch threshold | Active research blocker | OPEN-CONDITIONAL; sweep suggests singular zero-repulsion transition for 20x20_c0.6 | No |
| Zero-repulsion degeneracy support lemma | New support lemma | PROVED under automorphism/barrier-feasible hypotheses | No, auxiliary only |
| Positive-repulsion overlap-selection support lemma | New support lemma | PROVED under fixed-candidate or smooth nondegenerate branch hypotheses | No, auxiliary only |
| R1-G overlap-to-centeredness | Next-trigger candidate | DISPROVED in universal form; REFORMULATED as minimum-overlap plus tie-breaker problem | No, support result |
| B1 gamma_eff | Category B | unchanged; requires branch-conditioned constants | No |
| B3 d_min* formula | Category B | unchanged; likely branch-conditioned | No |

## Current Official Counts

| Category | Count |
|---|---:|
| Category A | 35 |
| Category B | 4 |
| Category C | 5 |
| Retracted | 5 |

## Guardrail

No theorem may be upgraded from this cycle alone. The proved result is a local finite-dimensional continuation theorem; it does not determine the global selected branch or numerical threshold.

## B1/R4 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| Branch-local `F_B''(0)` | PROVED well-defined under R1-P branch-continuation hypotheses | No |
| Branch-free `F''(M/2)` | DISPROVED / false universalization | No |
| Universal `gamma_eff ≈ 0.89` | remains Category B empirical and branch/path/manifold conditioned | No |
| Relaxed-manifold merge barrier | still open until valid endpoint/path class is specified | No |

## B3 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| qualitative critical separation | retained as regime-level support concept | No |
| closure lowers observed threshold | numerical support + plausible mechanism | No |
| coefficient formula `4.8 + 0.31sqrt(beta/alpha)-0.018beta/alpha` | remains Category B empirical | No |
| universal branch-free `d_min*` | rejected / false universalization | No |

## B4 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| structured soft-mode overlap perturbation formula | theorem-level under spectral-gap/localization hypotheses | No |
| `33x` improvement | remains Category B empirical/config-specific | No |
| universal 33x window | rejected / false universalization | No |
| replacement quantity | `1 / omega_soft(B, geometry)` | No |

## B2 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| instability threshold / nonuniform existence | retained as proved | No |
| D4/equivariant supercriticality | retained as proved | No |
| simple eigenvalue with spectral-gap condition | proved under explicit condition | No |
| narrow-gap / non-D4 degenerate supercriticality | remains Category B | No |

## C1 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| shifted-threshold preservation | retained as proved | No |
| exact threshold under interior-gap / beta condition | PROVED UNDER EXPLICIT CONDITIONS | No |
| unconditional exact threshold | rejected / structurally false near weak phase or bifurcation | No |
| Category C status | retained | No |

## C2 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| shifted-threshold full persistence | proved composition | No |
| deep-core exact full persistence | proved under C1 conditions | No |
| all-core exact full persistence | rejected / too strong | No |
| Category C status for official T-Persist-Full | retained | No |

## C3-C5 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| T-Persist-K-Sep | proved as Sep-regime theorem; global Category C retained | No |
| T-Persist-K-Weak | conditionally proved as Weak-regime theorem; global Category C retained | No |
| T-Persist-K-Unified | conditionally proved for selected branch + five hypotheses; scalar branch classifier rejected | No |

## R2 Normal-Form Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| quartic normal-form displacement scaling | PROVED | No |
| IFT `f/mu` bound near bifurcation | shown conservative; quartic gives `f^(1/3)` critical scaling | No |
| uniform exact persistence across `mu=0` | still not proved; requires margin condition | No |

## R2 Cubic Normal-Form Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| symmetric quartic near-bif displacement | proved scaling bound | No |
| cubic/asymmetric normal form | shows pitchfork-style persistence is not universal | No |
| uniform near-bifurcation persistence | rejected; only normal-form-specific shrinking windows remain | No |

## R4 Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| constrained endpoint `(u_merged,0)` on fixed per-formation masses | remains invalid/retracted | No |
| relaxed total-mass state space `R_M^2` | defined | No |
| branch/path-conditioned barrier functional | defined | No |
| positive lower bound / MEP | still open | No |

## Relaxed Merge Lower-Bound Cycle Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| finite-image minimax path existence in `R_M^2` | PROVED | No |
| universal positive relaxed merge barrier | rejected / unsupported | No |
| no uniform lower bound over vanishing second-formation mass | PROVED degeneration | No |
| positive barrier under relaxed local stability and path restrictions | OPEN-CONDITIONAL | No |

## Relaxed Local Basin Barrier Delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| local escape barrier from relaxed Hessian gap | PROVED under fixed-stratum / stratified SOSC hypotheses | No |
| global relaxed merge barrier | remains conditional on target/path leaving local basin | No |

## Global relaxed path condition delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| target outside local basin | PROVED only under mass lower bound and basin-radius inequality | No |
| local contribution to global relaxed barrier | PROVED under explicit conditions | No |
| full global MEP lower bound | remains open | No |

## Kramers-rate formulation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| branch-conditioned barrier prerequisite | established | No |
| Kramers exponential rate for SCC constrained dynamics | plausible but unproved | No |
| finite-dimensional stochastic model requirements | specified | No |

## Relaxed MEP after escape delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| post-escape separation criterion | PROVED as conditional theorem | No |
| automatic additional global barrier beyond local escape | rejected / not automatic | No |
| global barrier strictly larger than local barrier | OPEN-CONDITIONAL on sublevel-set separation | No |

## Relaxed sublevel separation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| direct interpolation barrier as MEP lower bound | rejected | No |
| dissolve-spread-transfer path class | obstruction identified | No |
| post-escape additional barrier | OPEN-CONDITIONAL on sublevel separation/path restrictions | No |

## Core-preserving path class delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| `P_core-preserving` path class | defined | No |
| lower-bound theorem in this class | plausible but event bounds pending | No |
| relevance to unrestricted MEP | limited / artificial | No |

## Core dissolution lower bound delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| single-site threshold crossing cost | PROVED: `beta W(theta)` | No |
| mass-scaled core dissolution bound | rejected without synchronization/no-peeling assumptions | No |
| smoothness add-on | geometry/path dependent | No |

## No-peeling condition delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| exact simultaneous all-core crossing | rejected as artificial/nongeneric | No |
| threshold-band lower bound for q sites | PROVED | No |
| mass-scaled core dissolution | conditional on collective/no-peeling path restriction | No |

## Constrained Langevin Kramers schema delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| fixed-stratum Langevin model | defined | No |
| reflected-polytope Langevin model | defined but technically open | No |
| Kramers rate claims without model | invalid | No |
| SCC Kramers theorem | theorem-schema only | No |

## Kramers route decision delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| fixed active stratum route | selected as safer theorem path | No |
| reflected-polytope route | deferred as advanced stochastic-analysis extension | No |
| boundary/corner Kramers claims | not SCC theorems yet | No |

## Fixed-stratum Kramers theorem schema delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| fixed-stratum Eyring-Kramers rate | classical theorem under K1-K7 assumptions | No |
| SCC branch transition rate without model/saddle | invalid | No |
| reflected-polytope rate | deferred | No |

## Saddle vs communication height delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| communication height for branch transition | primary deterministic object | No |
| index-1 saddle representation | conditional/unproved | No |
| Eyring-Kramers prefactor | unavailable until saddle is proved | No |

## Communication-height large-deviation schema delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| communication height controls log-scale transition time | theorem-schema under fixed-stratum Freidlin-Wentzell assumptions | No |
| saddle-free prefactor | unavailable | No |
| SCC stochastic rate without LD assumptions | invalid | No |

## Relaxed communication-height scaffold delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| exp67 direct-vs-shortcut scaffold | implemented | No |
| naive diffuse shortcut lower than direct path | falsified in smoke config | No |
| true MEP / communication height | still requires path optimization | No |

## NEB-lite scaffold delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| exp68 projected path-relaxation scaffold | implemented | No |
| direct interpolation locally optimal | falsified in smoke setup | No |
| true MEP convergence | not proved | No |

## NEB-lite hardening delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| exp68 constraint diagnostics | implemented | No |
| smoke improvement with no simplex/mass violation | observed | No |
| communication height estimator | improved but still numerical scaffold | No |

## NEB-lite multi-config smoke delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| NEB-lite lowers direct path proxy across smoke configs | supported numerically | No |
| improvements due constraint violation | not supported by diagnostics | No |
| true MEP found | not proved | No |

## NEB sweep scaffold delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| exp69 sweep aggregator | implemented | No |
| exp69 smoke improves direct path proxy | supported numerically | No |
| communication height theorem | still requires deterministic/path-class proof | No |

## lambda-rep NEB-lite sweep delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| lambda_rep=0 relaxed merge proxy collapse | numerical support | No |
| positive lambda_rep increases communication proxy | numerical support | No |
| exact communication height | still unproved | No |

## lambda/grid NEB-lite sweep delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| lambda_rep=0 proxy collapse across smoke configs | repeated numerical support | No |
| positive lambda_rep creates/increases proxy | repeated numerical support | No |
| exact zero-rep theorem under endpoint convention | next proof target | No |

## zero-repulsion relaxed merge zero-barrier delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| lambda_rep=0 removes interaction barrier | PROVED | No |
| zero barrier iff connected within source sublevel set | PROVED as criterion, with infimum/attainment caveat | No |
| lambda_rep=0 alone implies zero barrier | rejected | No |

## zero-repulsion sampled sublevel diagnostics delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| sampled lambda_rep=0 paths stay in source sublevel | verified numerically | No |
| zero clipped barrier for sampled convention | supported numerically via sufficient condition | No |
| universal zero-repulsion zero barrier | still false/conditional | No |

## positive-repulsion first-order merge delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| first-order repulsion term equals overlap functional | established | No |
| positive first-order lower bound | conditional on unavoidable overlap `Omega_0>0` | No |
| universal positive first-order coefficient | rejected | No |

## Omega0 overlap diagnostics delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| sampled zero-excess lambda_rep=0 path has nonzero overlap | verified numerically | No |
| sampled path positive first-order repulsion cost | follows from decomposition | No |
| unavoidable overlap Omega_0>0 | remains open | No |

## Omega0 overlap-excess diagnostics delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| raw max overlap is enough for first-order barrier | corrected/rejected | No |
| sampled zero-repulsion overlap excess | measured as 0 | No |
| positive first-order bound | must use unavoidable overlap excess and fixed branch | No |

## fixed-branch repulsion perturbation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| fixed zero-repulsion path gains first-order barrier from lambda | falsified in smoke path set | No |
| overlap-excess, not raw overlap, controls fixed-branch first-order term | supported | No |
| positive-lambda barrier source | branch re-selection likely dominant | No |

## positive-repulsion branch reselection delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| equal-self-energy lower-overlap branch selected by positive lambda | PROVED | No |
| unequal self-energy threshold | PROVED: lambda > DeltaE_0/DeltaR | No |
| universal branch selection without candidate set | not proved | No |

## branch-reselection threshold estimate delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| threshold estimate from independent optimized exp69 rows | rejected | No |
| branch identity matching required | established | No |
| branch continuation needed | next target | No |

## Exp71 branch continuation smoke delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| branch continuation needed for threshold estimates | confirmed | No |
| up/down branches distinct in smoke | confirmed | No |
| robust threshold theorem | still open; needs jump detection | No |

## Exp71 branch-continuity diagnostics delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| branch-distance / jump diagnostics | implemented | No |
| lambda=0.1 threshold row reliable | rejected due jump | No |
| robust threshold estimate | still unavailable | No |

## Exp71 fine continuation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| fine lambda grid removes branch jumps | falsified | No |
| robust threshold estimate | still unavailable | No |
| branch identity controls needed | reinforced | No |

## Exp71 hardened continuation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| label-swap-aware diagnostics remove jumps | falsified | No |
| robust threshold estimate from Exp71 | still unavailable | No |
| frozen-branch energy evaluation | recommended next | No |

## Exp72 frozen branch threshold delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| frozen-candidate energy-line evaluation | implemented | No |
| positive threshold in smoke | not found; Type A candidate dominates for all lambda>=0 | No |
| candidate discovery problem | identified | No |


## Exp73 branch catalog smoke delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| multi-start branch catalog / frozen lower-envelope comparison | implemented | No |
| positive frozen crossing in smoke catalog | NUMERICAL SUPPORT ONLY: `lambda_cross ≈ 9.09e-4` between discovered representatives | No |
| candidate discovery bottleneck from Exp72 | reduced but not eliminated | No |
| universal/global branch threshold | still not proved | No |


## Exp73 catalog grid preliminary delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| tiny-positive `lambda_cross ≈ 9e-4` summary | rejected as stable summary after expanded catalog | No |
| source-0 anchored first crossing scale | varies widely across configs (`0.092` to `4.605`) | No |
| finite-catalog branch replacement | repeated numerical support | No |
| universal threshold law | still not proved | No |


## Exp74 family-match delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| early global crossings reflect smooth within-family continuation by default | rejected | No |
| family-switch explanation for early/moderate crossings | numerical support | No |
| matched-family threshold | larger or absent in current catalog | No |
| universal family-matched threshold law | still not proved | No |


## Exp74 high-budget robustness delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| family-switch explanation universal across sentinel configs | rejected | No |
| 10x10:0.6 family-switch diagnosis | reversed after higher-budget catalog; same-family crossing now matches global crossing | No |
| 15x15:0.6 and 20x20:0.6 family-switch diagnosis | remains numerically supported | No |
| threshold sweep 2.0-4.0 changes qualitative diagnosis | not supported | No |


## Exp75 seeded continuation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| no positive-lambda Type B-like family on `20x20:0.6` | rejected by seeded continuation | No |
| catalog absence implies physical absence | rejected | No |
| targeted seeded continuation preserves Type B label up to `lambda=0.2` | numerical support | No |
| family-switch diagnosis for hardest sentinel | weakened substantially | No |


## Exp76 fine seeded continuation delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| seeded Type B branch loses its Type B label before `lambda=1.0` on `20x20:0.6` | rejected on current grid | No |
| branch-type drift in Exp75 proves family loss | rejected | No |
| warm continuation of recovered Type B branch to `lambda=1.0` | numerical support | No |
| selection vs persistence divergence | now the active R1-Q subgap | No |


## Exp77 selection-vs-persistence delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| persistent Type B branch is dominated by best discovered competitors on `20x20:0.6` | rejected on tested grid | No |
| raw catalog resolves selected branch structure reliably | rejected | No |
| search/discovery quality is the main bottleneck | numerically supported | No |
| true global selected branch | still not proved | No |


## Exp78 search-protocol-upgrade delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| raw multistart catalog search is adequate for selected-branch inference on `20x20:0.6` | rejected | No |
| injected-seed upgraded optimization still returns Type B at tested lambdas | numerical support | No |
| persistent continuation branch is already locally search-optimal | rejected | No |
| search protocol is the dominant active bottleneck | strongly supported numerically | No |


## Search-protocol dependence support proposition delta

| Claim | Outcome | Canonical Spec change? |
|---|---|---|
| there exist tested configs where `Sel_raw` and `Sel_upgrade` differ by family and energy | NUMERICAL SUPPORT ONLY | No |
| protocol-neutral selected-branch theorem | still open | No |
| protocol tag required in branch-selection statements | adopted as guardrail | No |
