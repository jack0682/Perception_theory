# pre_brainstorm.md — 2026-04-29 (W5 Day 3 morning brainstorm)

**Author**: User reflection at Day 3 morning, before plan.md execution.
**Purpose**: morning mental frame, decision-pre-think, calibration.
**Read first**: `THEORY/logs/daily/2026-04-28/99_summary.md` Phase 1-10 cumulative.

---

## §1. Mental Frame for Day 3

Day 2 was a **massive expansion** — 10 elevation cycles in single day, 246 numerical attempts, 38 daily files. The σ-framework now spans:

- Static σ-framework (Commitment 14, σ_multi^A and σ_multi^D, T-σ-Multi-1).
- Dynamic regime classification (per-formation, hybrid γ, shared pool).
- LSW correspondence (shared pool ↔ CH; α plateau 0.25-0.30).
- V5b family (V5b-T, V5b-T', V5b-F).
- Paper §4 fully drafted.

Day 3 question: **how to convert this work into canonical / paper output without losing momentum?**

Two paths:
A. **Consolidation-first**: process user-decision queue, apply canonical edits, polish paper. Convergent.
B. **Continue expansion**: Phase 11 with NQ-244 3D, NQ-245 variable-K, etc. Divergent.

Recommend **Path A** (consolidation) for Day 3, with Path B optional in Block 4. Reason: 10 expansion cycles without canonical anchoring risks drift; need at least one consolidation day before continuing expansion.

---

## §2. Decision Pre-Think for Block 1 User Decision Queue (NON-BINDING)

The 6 (or 7 with D-6 split) canonical-edit decisions. Notes below are NON-BINDING context, not recommendations — user decides per item.

### D-1, D-2: Commitment 14 (O5')(O7) (Day 1 carry)

Day 1 Round-2 review (`92_critical_review_round2.md`) findings about σ-tuple well-definedness. Phase 4 §5.4-5.5 verified consistency.

**Context**: Clarifying conventions (multi-irrep + tie-breaking) for σ-tuple discrete invariant. Without them, σ-tuple ordering at degenerate eigenvalues is ambiguous. Canonical δ ~30-50 lines combined.

**Considerations**:
- PRO: removes ambiguity; widely-used Mulliken convention is standard.
- PRO: low canonical-line cost.
- CON: increases Commitment 14 entry length.
- DEFER COND: if user wants to first see Day 3 polished §4 paper text using these conventions.

### D-3: V5b-F mechanism rider (Phase 3 Branch B refined)

`01_NQ173_v5b_f_verdict.md` §3.4 refined V5b-F: H1+H2+H3 mixed in regime R3b. Phase 4 numerical anchored on free BC L=20 c=0.10.

**Context**: Promotes V5b-F from Cat C to Cat B target. Mechanism explicitly characterized. Canonical δ ~15-20 lines.

**Considerations**:
- PRO: empirically anchored (NQ-173 15/15 attempts).
- PRO: Cat status promotion (C→B target).
- CON: Phase 6 finding "static-vs-dynamic distinction" doesn't change this STATIC structural claim, but might be flagged inline for clarity.

### D-4: ζ_*(graph, c) precise + c-dependence

NQ-174 measured ζ_*(2D torus L=20, c=0.10) ≈ 0.40. NEW finding: ζ_* is c-dependent (not just graph-class-dependent).

**Context**: c-qualifier rephrasing of T-V5b-T-(d). Canonical δ ~10-15 lines.

**Considerations**:
- PRO: empirically grounded.
- PRO: clarifies canonical statement that was bracketed before.
- CON: makes statement more verbose.

### D-5: V5b-T' new entry (Phase 3 finding)

V5b-T' = corner-saturated F=1 minimizer on translation-invariant graphs (regime R3b). NEW phenomenon. Phase 4 F5 numerical confirmed.

**Context**: New canonical §13 entry ~50-60 lines. Cat B target (numerical anchor; analytical proof W6+).

**Considerations**:
- PRO: significant new finding from Phase 3.
- CON: large addition (~50-60 lines).
- DEFER COND: if user prefers V5b-T' to mature further before canonical (e.g., wait for analytical proof of PN-barrier formula).

### D-6a: Commitment 14-Multi static (σ_multi^A + σ_multi^D Phase 4)

Phase 4 proposal `20_*` Part 2: combined invariant σ_multi = (σ^A, σ^D) for K-formation. Static framework only (no time-trajectory).

**Context**: Substantial new Commitment Note ~30-40 lines. Cat B under involution canonical-iso hypothesis.

**Considerations**:
- PRO: foundational for multi-formation σ-framework.
- PRO: well-anchored Phase 1-7 numerics.
- CON: requires Frobenius reciprocity + group cohomology background (heavier reading).

### D-6b: Commitment 14-Multi dynamic (σ_multi^A(t) trajectory Phase 9-10)

Phase 9-10 σ_multi^A(t) trajectory framework + K-jump statistics + Hessian σ-tuple over time.

**Context**: Adds time-evolution layer to D-6a. Canonical δ ~20-30 lines.

**Considerations**:
- PRO: extends Cat A static to dynamic regime.
- CON: STILL Cat B sketch only; numerical anchor is Phase 9-10 simplified σ-tuple, not full Hessian.
- DEFER COND: probably WORTH DEFERRING — recommend W6+ after rigorous Hessian-based σ-tuple time-series analysis.

### Combined option matrix

User can pick from:

| Option | Items approved | Canonical δ | Cat A delta |
|---|---|---|---|
| **All-7** | D-1,D-2,D-3,D-4,D-5,D-6a,D-6b | ~300-380 lines | +5-7 |
| **Recommended** | D-1,D-2,D-3,D-4,D-5,D-6a (defer D-6b) | ~250-310 lines | +4-5 |
| **Conservative** | D-1,D-2,D-3,D-4 (defer D-5,D-6a,D-6b) | ~80-100 lines | +1-2 |
| **Minimum** | D-1,D-2 (defer rest) | ~30-50 lines | 0 |
| **Defer all** | none | 0 | 0 |

Each option corresponds to different W5 ladder achievability levels. User decides based on confidence in Phase 1-10 work + W5 release timing.

---

## §3. Paper §4 Polish Priorities

After Phase 4 F12 + Phase 6 Q4 + Phase 7 R1.5-R1.8, §4 prose covers all 7 sub-sections. Polish targets:

### §3.1 Notation cleanup

- σ vs σ_multi vs σ_multi^A/^D — consolidate per `22_*` glossary.
- λ_rep vs λ_{rep} typesetting.
- Formula numbering across sub-sections.

### §3.2 Theorem cards

Consistent format:
```
\begin{theorem}[NAME]
    Statement.
\end{theorem}
\begin{proof}[Sketch]
    Proof points.
\end{proof}
```

Currently mixed: some have full proofs sketched, some just statements.

### §3.3 Cross-references

Phase 1-10 internal references like `01_*`, `09_*` etc. need to be replaced with paper-internal equation/theorem labels.

### §3.4 Figure placeholders

5 figures noted in skeleton; need actual figure-generation script (deferred to W6+ as `papers/generate_figures.py` extension).

---

## §4. Phase 11 Pre-Think (optional Block 4)

If Phase 11 happens in Block 4, candidate priority order:

1. **NQ-244 (3D proper LSW)**: most useful for paper §4.5 LSW d=3 verification. Computational cost ~1-2h. **Recommend**.

2. **NQ-245 (variable-K architecture)**: novel finding potential but exploratory. Defer to Day 4-5.

3. **NQ-246 (K-jump scaling precise)**: refinement of Phase 10 V4 result. Less urgent.

4. **σ_multi^A(t) Hessian autocorrelation**: numerical analysis of Phase 10 V3 data. Lighter computational cost.

If only one Phase 11 task, **NQ-244 3D LSW** has highest value-per-time.

---

## §5. Day 4-7 Outlook

Day 3 outcome determines Day 4-7:

### Scenario A (canonical approved + paper polished)

- Day 4: G4 (V5b 3D extension full), G5 (SF Round 1-5 merge).
- Day 5-6: G6, G7, G8.
- Day 7: W5 close + weekly_summary.

### Scenario B (canonical deferred)

- Day 4-5: continue Phase 11 expansion (NQ-244, NQ-245, etc.).
- Day 6: re-attempt canonical promotion.
- Day 7: weekly close.

### Scenario C (canonical partial)

- Day 4: complete remaining canonical items.
- Day 5-6: G4-G8 work.
- Day 7: weekly close.

---

## §6. Risk Assessment for Day 3

### Risk-1: User opts to defer all canonical edits

**Likelihood**: Medium. User may want more time to review 6 items.
**Mitigation**: Block 1 outputs proposal package even on defer. Day 4 morning re-attempt.

### Risk-2: Canonical edit applies but tests break

**Likelihood**: Low (canonical edits are documentation, not code).
**Mitigation**: Test before/after each block. If breaks: revert + investigate.

### Risk-3: Day 3 Phase 11 explodes scope

**Likelihood**: Medium if user enthusiastic.
**Mitigation**: plan.md §6 hard constraint "no Phase 11 numerical exceeding 2h". Day 3 is consolidation day.

### Risk-4: Paper §4 polish reveals errors in Phase 1-10 prose

**Likelihood**: Medium. Phase 4 F12 and Phase 6 Q4 prose written quickly under pressure.
**Mitigation**: Polish is supposed to catch these. Document errors found in `02_*` polish output.

---

## §7. Personal Calibration Notes

After Day 2's 10-cycle marathon, remember:
- Day 3 SHOULD be slower (consolidation, not expansion).
- Don't be tempted into Phase 11 expansion as default — let consolidation work.
- Quality over quantity for Day 3 outputs.
- User decisions are the bottleneck — process them carefully.

If by 14:30 Block 1-3 not complete, SKIP Block 4 (Phase 11) without regret.

---

## §8. Suggested Reading Order at Session Start

1. `99_summary.md` Phase 1-10 cumulative.
2. `03_canonical_proposal_v5b_t_update.md` (5 user-decision items details).
3. `20_canonical_proposals_F10_F11.md` (V5b-T' + Commitment 14-Multi).
4. `26_paper_section4_prose.md` + `29_paper_section4_full_prose.md` (Paper §4 to polish).
5. `weekly_draft_storming.md` 04-28 entry (W5 progress).

---

**End of pre_brainstorm.md.**
**Mental frame: Day 3 = consolidation. Process user decisions, anchor Phase 1-10, polish paper. Optional Phase 11 only if Block 1-3 close on schedule.**
