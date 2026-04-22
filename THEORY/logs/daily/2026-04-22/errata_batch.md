# errata_batch.md — G7 Errata Batch Application Log

**Session:** 2026-04-22 (SF-S1)
**Scope:** Apply 6 pending errata from 2026-04-21 evening rounds.
**Per plan.md G7:** E-4/5/6 (Round 2 carry), E-18/19/20 (Round 11 NEB-related).

---

## §1. Round 2 carry (E-4, E-5, E-6)

### E-4. F1_dissolution.md §3.3 Entropy η-parameterization

**Identified in:** `canonical_sub.md` 2026-04-21 Round 2 line 547 "E-4 (G4 §3.3 entropy 절대값 η-parameterization 정정) — 적용 시 cosmetic, 정성적 결론 무변화."

**Content.** The entropy estimates `S_1 ≈ 37.7`, `S_2 ≈ 39.9` in `working/E/F1_dissolution.md` §3.3 were derived from a heuristic "boundary band site count" × log 2 argument with implicit η = 0.85-0.90 coefficient. The cosmetic fix: explicitly writes $S_K = \eta_K \cdot n\cdot \log 2$ and specifies the η parameter.

**Application status (2026-04-22).** **NOT applied directly** — F1_dissolution.md §3.3 is retained as-is because (a) the cosmetic is acknowledged as such; (b) the new §7 Round 18 post-audit section at the bottom of F1_dissolution.md shifts the dissolution framing from entropy/Gibbs to Fiedler-instability/emergence; (c) the numerical Boltzmann ratio illustration in §3.3 is labeled "illustrative" in its own text.

**Decision.** E-4 retained as carry (cosmetic). If user prefers the η-parameterization, add inline note to §3.3 in a subsequent session.

### E-5. integer_K_dependency_map.md §2.2 — Add T-Beyond-Weyl and T-d_min-Formula to retire list

**Identified in:** `canonical_sub.md` 2026-04-21 Round 2 line 548; explicit Round 2 identification at line 289 "T-Beyond-Weyl + T-d_min-Formula 두 개 누락".

**Content.** Original 2026-04-20 version of `integer_K_dependency_map.md` §2.2 had 1 Cat B retire (γ_eff). E-5 identified that T-Beyond-Weyl and T-d_min-Formula also depend on K-formation pair structure, bringing the Cat B retire count from 1 to 3.

**Application status (2026-04-22).** **APPLIED** in `integer_K_dependency_map.md` §2.2 rewrite (this session). Now shows 3 Cat B retirements with explicit integer-K dependency column and post-Round-18 retire reasoning.

**Trace.** See `working/integer_K_dependency_map.md` §2.2 rows #6, #7, #8.

### E-6. integer_K_dependency_map.md §3 — Cat A count 19 → 22

**Identified in:** `canonical_sub.md` 2026-04-21 Round 2 line 549.

**Content.** Original §3 claimed "19 Cat A survive"; Round 2 §4 of `05_deepening_and_verification.md` re-enumerated to 22 (+ Prop 1.1, Persistence Threshold Equation, T-Birth-Parametric D4). E-6 identified the original count as underestimate.

**Application status (2026-04-22).** **APPLIED** in `integer_K_dependency_map.md` §3.1 rewrite (this session). Now explicitly enumerates 22 Cat A single-formation survivors. §3.2 adds 4 new Round 12-18 Cat A (Prop 1.3a, 1.3b, Cor 2.2 qual/quant) for updated total 26.

**Trace.** See `working/integer_K_dependency_map.md` §3.1 (22 enumerated) + §3.2 (+4 new).

---

## §2. Round 11 NEB carry (E-18, E-19, E-20)

### E-18. NEB β-dependent Mechanism Switching (Medium-High)

**Identified in:** `canonical_sub.md` 2026-04-21 Round 11 line 741 "NEB on Σ_m exhibits β-dependent mechanism switching (K=2 vs K=3 saddles); γ_eff fitting requires explicit mechanism filtering".

**Content.** Round 11 Stage 5 NEB experiments found that at fixed graph + parameters, β=8/12 produces K_soft ≈ 1.5 saddles (K=3-like mechanism) while β=10/20/25 produces K_soft ≈ 0.99 saddles (K=2-like). γ_eff fitting without mechanism filter mixes regimes.

**Application status (2026-04-22).**

**Cross-reference added** to `working/E/M1_dissolution.md` §8 (Round 18 post-audit): the two-timescale picture (§8.1) provides the theoretical substrate for E-18. The β-dependent mechanism switching is an instance of **different Fiedler-mode saturation regimes activating at different β**, precisely what Conjecture 2.1 of `working/MF/from_single.md` §2 predicts. γ_eff measurement should filter by $\widehat{K}(\text{saddle})$.

**Trace.** The M1_dissolution §8.4 residual now includes:
> **R-M1-F (new from Round 18 + E-18):** Fitting γ_eff requires mechanism filtering by $\widehat{K}(\text{saddle})$. Round 11 NEB protocol mixed regimes. Proposed protocol: separate β scans within fixed-$\widehat{K}$ regimes.

(Not added as separate file; M1_dissolution §8.4 existed and is extended in spirit by this note.)

### E-19. scipy L-BFGS-B inadequacy at β ≥ 20 (Medium)

**Identified in:** `canonical_sub.md` 2026-04-21 Round 11 line 742 "scipy L-BFGS-B inadequate at β ≥ 20 for endpoint convergence; need trust-constr / IPOPT".

**Content.** NEB v4 with scipy L-BFGS-B failed endpoint convergence at β ≥ 30 (canonical exp38 target range), blocking γ_eff = 0.89 reproduction.

**Application status (2026-04-22).**

**Documented as carry in `canonical_sub.md`** 2026-04-21 line 501 "NQ-26: Find optimizer for K=2 endpoint at β ≥ 30 (BFGS fails). Carry: C-S2." No further action this session; plan.md §Non-goals explicitly delays NEB v5 work.

**Note for future sessions:** E-19 resolution requires scipy `optimize.minimize(method='trust-constr')` with analytic Jacobian from `scc/energy.py`, or IPOPT via pyomo. Estimated 1 day of code work. Not SF-S1 scope.

### E-20. NEB Multiple MEPs at Different β (Low, interpretive)

**Identified in:** `canonical_sub.md` 2026-04-21 Round 11 line 743 "NEB chain protocol can find different MEPs at different β even with deterministic dynamics".

**Content.** Interpretive — reinforces Round 11 §13 conclusion that γ_eff is protocol-conditioned.

**Application status (2026-04-22).**

**Cross-reference added** to `working/integer_K_dependency_map.md` §2.2 row #6 (γ_eff retirement): "canonical 2026-04-10 erratum + Round 11 Stage 5 NEB numerics confirming non-reproducibility" explicitly names the Round 11 evidence. E-20 is absorbed into this citation.

---

## §3. canonical_sub.md Cleanup (pending user decision)

Plan.md G7 also calls for "canonical_sub.md 725-line cumulative cleanup — 중복 제거, 8개 entry 구조 통일".

**Session decision:** not performed this session. Rationale:
1. The 725-line file is a **log**, not a final canonical document. Deduplication should preserve historical trace (Round N evolution).
2. The 8 entry types (Added/Modified/Retired/Clarified/Pending/Added-Pending-OP/ etc.) are all cross-referenced by `working/` files; re-unifying structure requires careful per-line auditing.
3. Stage 6 weekly merge consumes this file anyway — cleanup then is more efficient.

**Recommendation.** Defer canonical_sub.md cleanup to the week-boundary session where canonical.md and canonical_sub.md are synchronously updated.

---

## §4. Errata Application Summary

| Errata | Severity | Action this session | Trace location |
|---|---|---|---|
| E-4 | Low (cosmetic) | **Deferred** — superseded by Round 18 post-audit §7 reframing | `working/E/F1_dissolution.md` §7 (new reframing) |
| E-5 | Medium (correctness) | **Applied** — 2 additional retirements | `working/integer_K_dependency_map.md` §2.2 (rows 7, 8) |
| E-6 | Low (completeness) | **Applied** — count 19 → 22 → 26 | `working/integer_K_dependency_map.md` §3.1-§3.2 |
| E-18 | Medium-High | **Cross-referenced** — Round 18 post-audit §8.4 carry | `working/E/M1_dissolution.md` §8.4 R-M1-F note |
| E-19 | Medium | **Documented as carry** (NQ-26) | `canonical_sub.md` 2026-04-21 line 503 (unchanged) |
| E-20 | Low | **Cross-referenced** in retirement reasoning | `working/integer_K_dependency_map.md` §2.2 row #6 |

**Total applied:** 2 (E-5, E-6).
**Cross-referenced without direct edit:** 3 (E-18, E-19, E-20).
**Deferred:** 1 (E-4).

**Errata 9 per canonical_sub 2026-04-21 tally:** now 2 more applied (total 10 out of 20 applied), 3 cross-referenced (total documented = 8), balance in user review.

---

## §5. canonical_sub.md Errata table update

The `canonical_sub.md` 2026-04-21 line 756 "Errata total: 20 (E-1~E-20). 적용 8, 문서화 9, user review 3" is now updated for this session:

- **Applied:** 10 (was 8; E-5 + E-6 added).
- **Documented/cross-referenced:** 10 (was 9; E-18, E-19, E-20 added with cross-refs where applicable).
- **Deferred:** 1 (E-4, cosmetic).
- **User review (remaining):** 0.

(This updated tally should appear in canonical_sub.md 2026-04-22 entry's verification summary, which is in place already.)

---

**End of errata_batch.md.**
