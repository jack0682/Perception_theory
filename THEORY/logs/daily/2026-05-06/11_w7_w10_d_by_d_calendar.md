> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 11_w7_w10_d_by_d_calendar.md — W7-W10 Day-by-Day Calendar

**Session:** 2026-05-06 (W6 Day 3 G3.12, P1).
**Scope:** W7 (May 7-13) through W10 (May 28-June 3), 28 days.
**Source:** Day 3 plan.md §2.12 + G3.6/G3.7/G3.8/G3.9/G3.10 analysis.
**Format:** Each day: primary task, estimated effort, output files, hard constraints.

---

## §0. Legend

- **[NQ]** = Numerical query (experiment)
- **[Sup]** = Supervised canonical edit (requires user presence)
- **[W]** = Working file update only
- **[P]** = Planning/audit document
- **[R]** = Review / retrospective

Hours in () are estimates; "–" = no output file (planning only).

---

## §1. W7 — May 7-13 (Debt Paydown + CV-1.6 Execution)

### W7 D1 (May 7) — NQ-G1-2-ext Execution
**Primary:** Run `exp58_nq_g1_2_ext.py` (NQ-G1-2-ext post-flow residual measurement).
**Secondary:** canonical §0 Table of Contents + anchor tags (G3.5 interim navigability).
**Effort:** 1-2h NQ + 30min canonical §0.
**Output:**
- `CODE/experiments/exp58_nq_g1_2_ext.py` (new experiment)
- `CODE/results/nq_g1_2_ext_results.json` (960-config sweep)
- `CODE/results/nq_g1_2_ext_summary.txt` (distribution + outcome H-A/B/C)
- `THEORY/logs/daily/2026-05-07/01_nq_g1_2_ext_results.md` (analysis)
**Hard constraint:** Do NOT write canonical production reach caveat until results reviewed under supervision.

### W7 D2 (May 8) — NQ-G1-2-ext Analysis + Conditional Erratum
**Primary:** Analyze NQ-G1-2-ext results; determine H-A/B/C outcome.
**If H-B (>50% regime exit):** [Sup] supervised canonical erratum for T-L1-F/M Cat A conditional.
**If H-A:** add positive production reach note to T-L1-F entry.
**Effort:** 30min analysis + (if H-B) 1h supervised erratum.
**Output:**
- `THEORY/logs/daily/2026-05-08/01_nq_g1_2_ext_canonical_action.md`
- (If H-B): canonical.md T-L1-F caveat amendment + CHANGELOG entry [Sup]

### W7 D3 (May 9) — OP-0009-F + OP-0009-C Canonical Promotions
**Primary:** [Sup] Two supervised canonical promotions:
  - OP-0009-F: add F to canonical §5.5 derived diagnostics + CN17 reference.
  - OP-0009-C: add §10.5 $C_t$ multi-formation status note.
**Secondary:** [W] `pre_objective_K_field_tension.md` §7 — record Day 3 G3.2 advance.
**Effort:** 30min each promotion + 1h working file update.
**Output:**
- canonical.md §5.5 + §10.5 amendments [Sup]
- CHANGELOG W7 D3 entry [Sup]
- `working/MF/pre_objective_K_field_tension.md` §7 addition [W]

### W7 D4 (May 10) — OP-0009-λ Amendment + σ-Multi S_K Formalization
**Primary:** [Sup] canonical amendment — λ_rep footnote to CN5 + architectural coupling note §11.
**Secondary:** [W] Formalize $S_K$-equivariance of σ^A in `multi_formation_sigma.md`; check T-σ-Theorem-4 at class level (per `02e` §5.1 W7 D4 plan).
**Effort:** 1h canonical + 1h σ-multi formalization.
**Output:**
- canonical.md CN5 footnote + §11 note [Sup]
- `THEORY/logs/daily/2026-05-10/01_sigma_multi_class_level_formalization.md` [W]

### W7 D5 (May 11) — OP-0009-A Reconciliation
**Primary:** [W] Reconcile `shared_pool_canonical_proposal.md` §2-§4 with G3.2 quotient formalism ($\widetilde{\widetilde\Sigma}^K_M$). Update I9' description to reference quotient as canonical shared-pool space.
**Secondary:** [W] T-Persist-K induced gradient flow on quotient (per `02e` §5.2 W7 D5 plan).
**Effort:** 1.5h reconciliation + 1h T-Persist-K quotient formalization.
**Output:**
- `working/MF/shared_pool_canonical_proposal.md` §2-§4 update [W]
- `THEORY/logs/daily/2026-05-11/01_t_persist_k_quotient_formalization.md` [W]

### W7 D6 (May 12) — CV-1.6 Release Package Assembly
**Primary:** [Sup] CV-1.6 release: assemble D-O1..O6 items into canonical.md edits.
  - D-CV1.6-O1: shared-pool I9' commitment (CN17+)
  - D-CV1.6-O2: architecture I9/I9' canonical
  - D-CV1.6-O3: F derived diagnostic + λ_rep note
  - D-CV1.6-O4: $C_t$ multi-formation status
  - D-CV1.6-O5: K-bridge chain L1-series promoted items
  - D-CV1.6-O6: NQ-G1-2-ext reach finding (from W7 D1-D2)
**Effort:** 3-4h (full CV-1.6 supervised editing session).
**Output:**
- canonical.md CV-1.6 version bump + all D-O amendments [Sup]
- CHANGELOG W7 D6 entry: CV-1.6 release [Sup]
- `working/CV-1.6_release_packet_skeleton.md` status: DONE

### W7 D7 (May 13) — W7 Weekly Summary
**Primary:** [R] Weekly summary W7 + retrospective.
**Output:**
- `THEORY/logs/weekly/2026-05-W2/weekly_summary_w7.md`

---

## §2. W8 — May 14-20 (Bridge Chain + BC-1 Audit)

### W8 D1 (May 14) — OP-0009-Pre Working File Integration
**Primary:** [W] Integrate G3.2 Day 3 advance into `pre_objective_K_field_tension.md` as new §7 ("Day 3 quotient formalism advance"). Cross-reference 02a-02e files.
**Effort:** ~2h.
**Output:** `working/MF/pre_objective_K_field_tension.md` §7 addition [W]

### W8 D2 (May 15) — OP-0009-Emp BC-1 Analysis + σ-Multi Caveat Audit
**Primary:** [W] Read `single_high_F_equivalence.md` §4 BC-1 failure findings in detail. Determine if caveat needed on T-σ-multi-A/D-Static (analogous to T-σ-Theorem-4 pattern).
**Output:**
- `THEORY/logs/daily/2026-05-15/01_bc1_failure_sigma_multi_audit.md`
- (If caveat needed): [Sup] supervised T-σ-multi-A/D-Static precision remark addition

### W8 D3-D4 (May 16-17) — K-Bridge Chain Canonical Promotions
**Primary:** [Sup] Promote K-bridge chain (L1A through L1L + T-L1-F/M canonical additions).
  - T-L1-F (canonical §13): update with K-bridge chain backing proofs
  - T-L1-M (canonical §13): update with L1M soft count corollary
**Effort:** 2h/day × 2 days.
**Output:**
- canonical.md T-L1-F + T-L1-M proof chain additions [Sup]
- CHANGELOG W8 D3-D4 entry

### W8 D5 (May 18) — K-Bridge Chain Verification + Tests
**Primary:** Run tests to verify K-bridge chain additions don't break existing behavior.
**Output:**
- `CODE/tests/` passing (215+ tests)
- `THEORY/logs/daily/2026-05-18/01_k_bridge_chain_verification.md`

### W8 D6 (May 19) — T-Persist-K Quotient Theorem Draft
**Primary:** [W] Formalize T-Persist-K induced gradient flow on $\widetilde{\widetilde\Sigma}^K_M$ (per `02e` §5.2 W7 D5 carry-forward, if not completed W7 D5).
**Effort:** ~1.5h.
**Output:** `THEORY/logs/daily/2026-05-19/01_t_persist_k_quotient_theorem.md`

### W8 D7 (May 20) — W8 Weekly Summary
**Output:** `THEORY/logs/weekly/2026-05-W3/weekly_summary_w8.md`

---

## §3. W9 — May 21-27 (P-F Framework + K-Selection)

### W9 D1 (May 21) — OP-0014 P-F Axiom Set v1
**Primary:** [W] Upgrade `03a_pf_framework_axiom_proposal_v0.md` → `working/MF/pf_stochastic_framework_v1.md`.
  - P-F-A1 existence proof sketch (compact SDE on $\Sigma_M$)
  - P-F-A3 convergence (spectral gap argument sketch)
  - P-F-A7 $T_*$ calibration from `scc/optimizer.py` BB step
**Formal:** Register OP-0014 in `theorem_status.md` HIGH (supervised, ID assignment).
**Effort:** ~3h.
**Output:**
- `working/MF/pf_stochastic_framework_v1.md` (new)
- `theorem_status.md` OP-0014 registration [Sup]

### W9 D2 (May 22) — OP-0005 Layer B Kramers Under P-F
**Primary:** [W] Formalize Layer B Kramers rates under P-F-A4/A5.
  - Eyring-Kramers prefactor on $\Sigma_M$ (constraint geometry treatment)
  - Saddle existence attempt (or conditional statement)
  - NQ-ST-1: compute $\det H_{\min,K}$ at representative R23 minimizers (empirical Hessian non-degeneracy check)
**Effort:** ~3h.
**Output:**
- `working/MF/k_selection_b_kramers.md` §new section [W]
- `THEORY/logs/daily/2026-05-22/01_nq_st1_hessian_verification.md` [NQ]

### W9 D3 (May 23) — OP-0008 Path B + σ^A K-Jump Under P-F
**Primary:** [W] OP-0008 Path B formulation: $P(\sigma^A_\mathrm{new} \vert \text{K-jump from } [\hat{\mathbf{u}}])$ as Gibbs-weighted saddle average.
**Secondary:** σ-rich + Φ-rich combined formalism start.
**Effort:** ~3h.
**Output:**
- `working/MF/pf_op_0008_path_b.md` (new) [W]
- `working/MF/sigma_rich_augmentation.md` §new section [W]

### W9 D4 (May 24) — σ-Rich + Φ-Rich Combined + OP-0009-Pre §1 Draft Start
**Primary:** [W] σ-rich + Φ-rich combined formalism (`sigma_rich_augmentation.md` extend).
**Secondary:** [W] OP-0009-Pre §1 amendment draft start (`pre_objective_K_field_tension.md` §8).
**Effort:** ~2h + ~2h.
**Output:**
- `working/MF/sigma_rich_augmentation.md` extended [W]
- `pre_objective_K_field_tension.md` §8 start [W]

### W9 D5 (May 25) — OP-0009-Pre §1 Draft + σ-Rich Cat B Target
**Primary:** [W] OP-0009-Pre v2.0 §1 amendment draft complete.
  - CN10 refined statement
  - 5-layer ontological table (from `02d`)
  - Commitment 1 auto-satisfaction proof sketch
**Secondary:** σ-rich augmentation Cat B target.
**Effort:** ~3h + ~1.5h.
**Output:**
- `pre_objective_K_field_tension.md` §8 complete [W]
- `sigma_rich_augmentation.md` Cat B target draft [W]

### W9 D6 (May 26) — P-F Framework Canonical Promotion Proposal
**Primary:** [W] Draft canonical promotion proposal for P-F framework (new §16 candidate).
**Secondary:** T-K-Select Cat B candidate write-up.
**Output:**
- `THEORY/logs/daily/2026-05-26/01_pf_canonical_promotion_proposal.md`
- `THEORY/logs/daily/2026-05-26/02_t_k_select_catB_draft.md`

### W9 D7 (May 27) — W9 Weekly Summary + CV-1.7 Prep
**Output:** `THEORY/logs/weekly/2026-05-W4/weekly_summary_w9.md`

---

## §4. W10 — May 28-June 3 (CV-1.7 + v2.0 Kickoff)

### W10 D1-D2 (May 28-29) — CV-1.7 Supervised Promotions
**Primary:** [Sup] CV-1.7 canonical additions:
  - T-K-Select Cat B → canonical §13 (conditional on OP-0014)
  - P-F axiom set v1 → canonical new §16 (stochastic extension framework)
  - OP-0009-Pre §1 amendment → canonical §1 CN10 revised + commitment CN18
**Effort:** ~4h total (2h/day).
**Output:**
- canonical.md CV-1.7 amendments [Sup]
- `theorem_status.md` T-K-Select + P-F-A entries [Sup]
- CHANGELOG W10 D1-D2 entry

### W10 D3 (May 30) — OP-0009-Pre §1 Amendment Review
**Primary:** [Sup] Review §1 revised universe definition. Check consistency with §2-§12.
**Output:**
- `THEORY/logs/daily/2026-05-30/01_section1_review.md`
- canonical.md §1 final edit [Sup]

### W10 D4-D5 (May 31-June 1) — v2.0 New §§ Outline
**Primary:** [W] v2.0 structure planning:
  - §0 philosophical introduction (pre-objecthood primacy)
  - §17 K-selection mechanism (T-K-Select + Kramers + N-1 recovery)
  - Stereo SCC integration decision (Cat B by W10? → include in v2.0; else defer)
**Output:**
- `THEORY/logs/daily/2026-05-31/01_v20_structure_outline.md`
- `working/CV-1.7_parking_lot_inventory.md` update (v2.0 parking lot)

### W10 D6 (June 1) — canonical.md Split Preparation
**Primary:** [W] Prepare canonical split (per G3.5 recommendation):
  - Cross-reference audit (all §N→§M links enumerated)
  - Anchor tag insertion at each §N header
  - Promotion pipeline routing decision document
**Output:**
- `THEORY/logs/daily/2026-06-01/01_canonical_split_preparation.md`

### W10 D7 (June 2) — W10 Weekly Summary + v2.0 Kickoff
**Output:**
- `THEORY/logs/weekly/2026-06-W1/weekly_summary_w10.md`
- `THEORY/logs/daily/2026-06-02/01_v20_kickoff.md`

---

## §5. Calendar Summary Table

| Week | Theme | Primary deliverables | Supervised sessions |
|---|---|---|---|
| W7 | Debt paydown + CV-1.6 | exp58 results; OP-0009-F/C/λ/A promotions; CV-1.6 release | D2 (caveat), D3, D4, D6 |
| W8 | Bridge chain + BC-1 | K-bridge promotions; OP-0009-Pre integration; BC-1 audit | D2 (caveat?), D3-D4 |
| W9 | P-F + K-Selection | OP-0014 v1; Layer B formalized; OP-0008 Path B; σ-rich Cat B | D1 (OP-0014 register) |
| W10 | CV-1.7 + v2.0 kickoff | T-K-Select Cat B; P-F §16; §1 amendment; split prep | D1-D3 |

**Total supervised sessions:** ~8 sessions, ~14-16h of supervised editing across W7-W10.
**Total output files (projected):** ~45 new working/daily files across W7-W10.

---

## §6. Carry-Forward Hard Constraints from Day 3

These constraints from plan.md §3 apply to all W7-W10 work:

1. No un-supervised canonical edits (all §13 theorem changes require user presence).
2. OP-0009-Pre canonical §1 amendment not before W9 D5 (working file must be complete first).
3. NQ-G1-2-ext caveat (if H-B): staged review before canonical erratum — do not rush.
4. P-F framework (OP-0014): working-file-only status until W9 D6 promotion proposal.
5. BC-1 failure finding: confirm scope before adding T-σ-multi-A/D-Static caveat.
6. No G3.2 quotient formalism claims in canonical until W8 D1 working file integration + W10 D3 review.
7. σ-rich augmentation: Cat C → Cat B only after W9 D4-D5 combined formalism complete.
8. v2.0 new §§: outline only at W10; no canonical §§ added before W10 D1-D2 supervised session.

---

**End of `11_w7_w10_d_by_d_calendar.md`. 28-day W7-W10 calendar complete. 8 supervised sessions; ~45 projected output files; critical path: W9 OP-0014 → W10 CV-1.7 → W11-W12 v2.0. G3.12 complete.**
