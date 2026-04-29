# 01_canonical_promotion_queue_review.md — Day 3 User Decision Queue (D-1..D-6b)

**Session:** 2026-04-29 (W5 Day 3, Block 1)
**Target (from plan.md §3 Block 1):** Present 7 canonical-edit decisions to user with per-item summary, line-delta estimate, edit location, and approve/modify/defer options. Hard constraint per plan.md §6: **NO canonical edits without explicit user approval per item.**
**This file covers:** §1 method note, §2 per-item decision packets (D-1..D-6b), §3 combined option matrix, §4 default-conservative-no-action behavior, §5 application instructions if user approves.
**Depends on reading:** `00_phase9_10_reconciliation.md` (Phase 9-10 → proposal text reconciliation), Day 2 source files (`01_NQ173_v5b_f_verdict.md`, `02_NQ174_zeta_star_results.md`, `03_canonical_proposal_v5b_t_update.md`, `20_canonical_proposals_F10_F11.md`), `canonical.md` §11.1 + §13.

---

## §1. Method Note (Important: Read First)

This file does **not edit canonical**. It packages 7 user-decision items into a single decision queue. Each item has:

- **Source**: which Day 2 daily file the proposal text was drafted in.
- **Reconciled status** (per `00_phase9_10_reconciliation.md`): is the proposal FINAL or does it need updating?
- **Canonical edit target**: which canonical file + line area would receive the edit.
- **Estimated line delta**: how many canonical lines added/replaced.
- **Cat status delta**: count of new C-IDs / Cat A entries.
- **Decision options**: APPROVE / MODIFY / DEFER, with subsidiary specifications.

**The user's role**: read each item, decide A/M/D per item, and (if any approved) explicitly authorize Claude to apply the canonical edits in a follow-up message. **Default behavior absent explicit authorization**: defer-all (NO canonical edits Day 3).

**Why explicit per-item authorization is required**:
- meta-prompt §8.1: canonical 직접 수정 금지 without user authorization.
- plan.md §6: "Without explicit user approval per item, NO canonical edits".
- A blanket "approve all" is acceptable but should be stated explicitly (e.g., "approve D-1..D-6a, defer D-6b").

---

## §2. Per-Item Decision Packets

### D-1. Commitment 14 (O5') Multi-Irrep Eigenspace Convention

**Source**: Day 1 W5 Round-2 (`2026-04-27/92_critical_review_round2.md` §4.3); Phase 1+2 review reaffirmed Phase 4 §5.4-5.5.

**Reconciled status** (per `00_*` §2 D-1): **FINAL.** No Phase ≥ 5 changes; proposal text in `2026-04-28/03_canonical_proposal_v5b_t_update.md` §5.2 reflects final substantive content.

**Canonical edit target**: `canonical.md` §11.1 Commitment 14 (current entry near line 768) — append (O5') sub-clause.

**Proposed text to insert** (verbatim from `2026-04-28/03_*` §5.2):
```
(O5') Multi-irrep eigenspace convention. When dim V_k > 1 with
V_k = ⊕_{[ρ]} V_k^{[ρ]} (Lemma 1 (ii)) containing r > 1 distinct irreps,
the σ-tuple entry for eigenvalue λ_k is
({n^{[ρ]}_k}_{[ρ]}, {[ρ]}_{[ρ]}, λ_k) — a multi-set of nodal counts and
irrep labels at this eigenvalue. The lex-ordering of the multi-set follows O7.
```

**Estimated line delta**: ~10-15 lines (sub-clause + brief usage example anchor to T-σ-Theorem-3 (vi)).

**Cat status delta**: 0 new C-IDs (this is a Commitment-level convention, not a theorem). Strengthens existing C-0715 (T-σ-Theorem-3) by removing well-definedness gap.

**Decision options**:
- **A1**: Approve as-is, apply Day 3 PM.
- **A2**: Approve with modification (user specifies edit; Claude updates proposal then applies).
- **D1**: Defer to v1.6 release (W6+).

**Risk note**: Low-risk addition (clarifying convention, not new mathematical content).

---

### D-2. Commitment 14 (O7) Tie-Breaking via Mulliken Character Order

**Source**: Day 1 W5 Round-2 (`2026-04-27/92_critical_review_round2.md` §2.2).

**Reconciled status** (per `00_*` §2 D-2): **FINAL.**

**Canonical edit target**: `canonical.md` §11.1 Commitment 14 — append (O7) sub-clause (after O5' if D-1 also approved).

**Proposed text to insert** (verbatim from `2026-04-28/03_*` §5.3):
```
(O7) Tie-breaking for degenerate eigenvalues. When λ_k = λ_{k+1} but
[ρ_k] ≠ [ρ_{k+1}], order entries by the canonical character-table order
of the residual stabilizer's irreps. For D_4 = {A_1, A_2, B_1, B_2, E}:
order A_1, A_2, B_1, B_2, E (Mulliken convention). For Z_2 = {[+1], [-1]}:
order [+1], [-1] (trivial first). For Z_n cyclic: order [1], [ω], [ω²], ...
by phase. For general finite groups: order by isomorphism-class invariants
(smallest dimension first; within same dimension, order by character of generator).
```

**Estimated line delta**: ~15-20 lines (sub-clause + cross-reference to T-σ-Theorem-4 (v) usage).

**Cat status delta**: 0 new C-IDs. Strengthens existing C-0716 (T-σ-Theorem-4) by promoting locally-stated convention to Commitment level.

**Decision options**:
- **A1**: Approve as-is, apply Day 3 PM.
- **A2**: Approve with modification.
- **D1**: Defer to v1.6.

**Combined D-1+D-2 note**: per `2026-04-28/03_*` §5.6, recommendation is to apply both jointly (they are complementary — O5' covers single-eigenspace multi-irrep; O7 covers distinct-eigenspace degenerate-eigenvalue). Splitting would create an inconsistent intermediate state.

---

### D-3. V5b-F Mechanism Rider in T-V5b-T

**Source**: Phase 2 α (NQ-173 monkey-patch run); refined by Phase 3 (`2026-04-28/01_NQ173_v5b_f_verdict.md` §3.4 + `03_*` §2.2).

**Reconciled status** (per `00_*` §2 D-3): **FINAL** for static mechanism. Optional 2-3 line static-vs-dynamic remark available (Phase 6 R1.2 box-clipping finding) — **user decides whether to include the optional clarifier**.

**Canonical edit target**: `canonical.md` §13 T-V5b-T entry (current line ~1151) — replace existing one-sentence V5b-F note with refined mechanism description.

**Current canonical text (line ~1151)**:
```
*Distinct from non-translation-invariant graphs (V5b-F)*: Free BC, barbell,
SBM exhibit *partial* Goldstone (overlap 0.5–0.85) due to boundary lifting;
this is a separate phenomenon currently sketched as Cat C (NQ-173).
```

**Proposed replacement** (verbatim from `2026-04-28/03_*` §2.2; with optional clarifier marked):
```
*Distinct from non-translation-invariant graphs (V5b-F refined, Cat B target)*:
Free BC, barbell, SBM exhibit *partial* Goldstone (full-space overlap 0.5–0.78,
bulk-only overlap 0.55–0.78) in the **corner sub-lattice regime**
(β > 1/a², c < c_s = (3-√3)/6 ≈ 0.211). Mechanism: the lowest non-tangent
Hessian mode is a hybridization of:
  (a) bulk-localized translation Goldstone of the corner-saturated cluster
      (H1 partial: bulk overlap exceeds full overlap by 0.03–0.10);
  (b) boundary-mode mixing with cluster-boundary spectral modes
      (H2: α²+β² ≈ 0.46–0.65, γ component ≈ 0.35–0.54);
  (c) PN-barrier-lifted eigenvalue μ_Gold^lifted ≈ 1–4 (H3: lattice-translation
      symmetry from "approximate" to "weakly explicit").
All three mechanisms operate jointly. Cat B target; analytic PN-barrier formula
NQ-198 (W6+) is the Cat A path.
Empirical anchor: NQ-173 W5 Day 2, 15/15 attempts at L=20, c=0.10,
ζ ∈ {0.5, 0.7, 1.0}.
[OPTIONAL: This is a static spectral characterization. Whether the analogous
multi-formation Goldstone instability manifests dynamically under volume +
simplex + box constraints is a separate question; see T-σ-Multi-1 / Phase 6
R1.2 dynamic stability finding.]
```

**Estimated line delta**: ~15-20 lines (without optional clarifier) or ~18-23 lines (with).

**Cat status delta**: 1 new entry — V5b-F (C-0711) status change from **Cat C → Cat B target**.

**Decision options**:
- **A1**: Approve without optional clarifier.
- **A2**: Approve with optional clarifier (recommended for clarity).
- **A3**: Approve with user-specified modification.
- **D1**: Defer to v1.6.

---

### D-4. ζ_*(graph, c) Precise Values + c-Dependence

**Source**: Phase 2 α (NQ-174 monkey-patch run); written up in `2026-04-28/02_NQ174_zeta_star_results.md` §6 + `03_*` §3.2.

**Reconciled status** (per `00_*` §2 D-4): **FINAL.**

**Canonical edit target**: `canonical.md` §13 T-V5b-T entry T-V5b-T-(d) sub-statement (current line ~1129).

**Current canonical text (line ~1129)**:
```
- $\zeta_*(2D \text{ torus}) \in [0.2, 0.5]$ (bracketed by $\zeta=0.2$
  overlap 0.49, $\zeta=0.5$ overlap 0.97).
- $\zeta_*(1D \text{ cycle}) < 0.2$ (sub-lattice overlap already 0.76 at $\zeta=0.2$).
- Precise value and dimensionality dependence: NQ-174.
```

**Proposed replacement** (verbatim from `2026-04-28/03_*` §3.2):
```
- $\zeta_*(2D \text{ torus } L=20, c=0.10) \approx 0.40$
  (NQ-174 W5 Day 2; mean overlap 0.920 at ζ=0.40 crosses 0.9 threshold).
- $\zeta_*(1D \text{ cycle } L=40, c=0.10) > 0.15$ (super-lattice transition
  NOT reached in tested ζ ∈ {0.05, 0.10, 0.15} range; mean overlap stays 0.70-0.74.
  Extended sweep NQ-174d W5 Day 3+ at ζ ∈ {0.20, 0.30, 0.50}).
- **NEW c-dependence finding**: ζ_* depends on volume fraction c, not only on graph class.
  Compare NQ-170c (c=0.5) vs NQ-174 (c=0.10):
    2D torus L=20: c=0.5 bracket [0.20, 0.50]; c=0.10 ≈ 0.40.
    1D cycle L=40: c=0.5 has overlap 0.76 at ζ=0.2 (ζ_* < 0.2); c=0.10 has overlap
    0.74 at ζ=0.15 (ζ_* > 0.15). Different c-regimes give different ζ_*.
- **Finite-size**: $L=20$ for 2D, $L=40$ for 1D; thermodynamic-limit ζ_*(∞):
  NQ-174c W6+.
- **Precise functional form** $\zeta_*(d, G, c)$: open (NQ-174b W6+).
- **Anomaly at ζ=0.45 on 2D torus L=20 c=0.10**: overlap drops 0.92 → 0.70
  (mode-crossing at deeper super-lattice; investigate via NQ-174e W6+).
```

**Estimated line delta**: ~12-15 lines (3 lines replaced + ~10 lines added for c-dependence + finite-size + functional form spawn + anomaly).

**Cat status delta**: T-V5b-T-(d) sub-statement changes from "bracketed pending NQ-174" → "**c=0.10 measured Cat A; functional form NQ-174b/c/e W6+**". No standalone new C-ID, but C-0710 (T-V5b-T) sub-statement (d) refined.

**Decision options**:
- **A1**: Approve as-is.
- **A2**: Approve with shorter version (drop the anomaly + W6+ NQ spawn details, retain only c=0.10 measured + c-dependence finding) — would reduce delta to ~8-10 lines.
- **A3**: Approve with user-specified modification.
- **D1**: Defer to v1.6.

---

### D-5. V5b-T' New Canonical Entry

**Source**: Phase 3 E5 + E10 (`2026-04-28/11_PN_unification.md` §3.1 + `16_K2_baseline_and_zeta45_results.md` §2.5); canonical proposal text in `20_canonical_proposals_F10_F11.md` Part 1.

**Reconciled status** (per `00_*` §2 D-5): **FINAL.**

**Canonical edit target**: `canonical.md` §13 — insert AFTER T-V5b-T entry (line ~1167), as sister theorem.

**Proposed text** (verbatim from `2026-04-28/20_*` Part 1 §1.2, lines 18-52): see source file. Begins:
```
**T-V5b-T'. Pre-Objective Goldstone on Translation-Invariant Graphs in
Corner-Saturated Regime.** *(New, 2026-04-28, W5 Day 2 Phase 3.)*

Let G be a finite translation-invariant graph (torus T^d, cycle C_n, or
d-fold lattice with periodic boundary conditions). ...
```
... [full statement V5b-T'-(a)/(b)/(c)/(d), Cat status, numerical confirmation, distinct-from-V5b-T/V5b-F notes, iteration history, references].

**Estimated line delta**: ~50-60 lines.

**Cat status delta**: 1 new C-ID — **C-NEW-V5b-T' (Cat B target)**. Add to Active Claims table in theorem_status.md.

**Decision options**:
- **A1**: Approve as-is, apply Day 3 PM.
- **A2**: Approve with optional shortening — drop "iteration history" subsection (saves ~5 lines).
- **A3**: Approve with user-specified modification.
- **D1**: Defer to v1.6 — keep V5b-T' as carry-forward NQ-206; revisit after analytic PN-barrier proof (NQ-198) or W6+ deeper numerical anchor.

**Risk note**: Largest single addition. Cat B target (not Cat A) — analytic PN-barrier formula remains W6+. If user prefers minimal v1.5.1 release, deferring D-5 is reasonable.

---

### D-6a. Commitment 14-Multi STATIC Extension (σ_multi^A + σ_multi^D)

**Source**: Phase 4 F11 (`2026-04-28/20_canonical_proposals_F10_F11.md` Part 2); supporting Phase 1-7 numerics (NQ-173, NQ-174, e9, e10, f5-f8).

**Reconciled status** (per `00_*` §2 D-6a): **FINAL** for static layer. Phase 5-10 cycles orthogonal. Optional 2-line static-vs-dynamic note available.

**Canonical edit target**: `canonical.md` §11.1 — insert AFTER existing Commitment 14 entry (line ~768).

**Proposed text** (verbatim from `2026-04-28/20_*` Part 2 §2.2, lines 75-103): see source file. Begins:
```
**Commitment 14-Multi (New, 2026-04-28, W5 Day 2 Phase 4).** Extension of
Commitment 14 to multi-formation K-field architecture.

Let u* = (u^(1)*, ..., u^(K)*) ∈ Σ^K_M be a Morse-0 K-formation joint minimizer
of K-field energy E_K under involutive canonical iso ρ ∈ Aut(G) on each pair...

σ_multi(u*) := (σ_multi^A(u*), σ_multi^D(u*)) — combined invariant with two
layers: ...
```
... [Layer A definition, Layer D definition, K=1 reduction, complementarity per Theorem 2.1', T-σ-Multi-1 Goldstone-pair instability with c_eff(L) → 1, numerical anchor, paper exposition note].

**Estimated line delta**: ~30-40 lines (+2 lines if optional static-vs-dynamic note included).

**Cat status delta**: New Commitment-level extension. Up to 3 new C-IDs:
- C-NEW-σ_multi^A (Cat A under involution iso) — combined invariant Layer A formal.
- C-NEW-σ_multi^D (Cat A under wreath-stabilizer iso) — combined invariant Layer D formal.
- C-NEW-T-σ-Multi-1 (Cat A) — Goldstone-pair static instability with c_eff(L) measured.

**Decision options**:
- **A1**: Approve without optional static-vs-dynamic note.
- **A2**: Approve with optional note (recommended — adds 2 lines, prevents future static/dynamic confusion).
- **A3**: Approve with user-specified modification.
- **D1**: Defer to v1.6 — D-6a stays as working-level (`working/MF/multi_formation_sigma.md`); revisit after K=2 baseline canonical anchor strengthens.

**Risk note**: Foundational addition. Establishes multi-formation σ-framework at canonical level. Strong empirical anchor (Phase 1-4 + Phase 5-7 K=2 baseline + Phase 8 T1 K=10 LSW). All Cat status claims have corresponding numerical or theoretical justification per Day 2 work.

---

### D-6b. Commitment 14-Multi DYNAMIC Extension (σ_multi^A(t) Trajectory)

**Source**: Phase 8 T4 (`2026-04-28/30_T4_CH_correspondence_sigma_t.md`) + Phase 9 U4 + Phase 10 V3 (`34_Phase10_findings.md` §3) + V4 (`34_*` §4).

**Reconciled status** (per `00_*` §2 D-6b): **NEEDS UPDATE.** The Phase 4 `20_*` Part 2 proposal text **does not contain** the dynamic σ_multi^A(t) layer. Phase 8-10 added substantive new content: time-trajectory definition, K-jump event characterization, V3 Hessian-based numerical, V4 K-jump statistics Δt ∝ t^1.315.

**Canonical edit target**: would be a sub-section appended to D-6a Commitment 14-Multi, OR a separate new entry "Commitment 14-Multi-Dynamic". Decision pending.

**Required additional drafting** (~20-30 lines if approved):
- Definition: σ_multi^A(t) := σ_multi^A(u(t)) along K-field gradient flow trajectory u(t).
- Smooth-segment + K-jump event structure (per Phase 9 U4).
- Numerical anchor: V3 Hessian σ-tuple at K=8 T²_20 (lowest 4 eigvals) + V4 K-jump statistics.
- Cat status: Cat B sketch (full Hessian σ-tuple time series + rigorous K-jump theory unproved).

**Estimated line delta** (if approved): ~20-30 lines.

**Cat status delta**: 1 new C-ID — C-NEW-σ_multi-trajectory (Cat B sketch).

**Decision options**:
- **A1**: Approve — Claude drafts the additional ~20-30 lines (effort ~30 min within Block 1 budget) and applies.
- **A2**: Approve with user-specified content (user provides specific text constraints).
- **D1 (RECOMMENDED)**: Defer to W6+ — `00_*` §2 D-6b rationale: V3 used simplified σ-tuple (lowest 4 eigvals), not full Hessian σ-tuple per Commitment 14; K-jump theory at canonical level requires resolving "what σ-tuple does the K-1 formation inherit from the merged pair?" — not addressed; full Hessian σ-tuple time-series with rigorous derivation still NQ-242.

**Risk note**: Cat B sketch is below typical canonical Cat-A or Cat-B-target threshold. Including D-6b in CV-1.5.1 carries higher risk of needing retraction in CV-1.6 if Hessian σ-tuple time-series proves more subtle than current V3 sketch suggests.

---

## §3. Combined Option Matrix

Recall pre_brainstorm `2026-04-29` §2 option matrix; here annotated with reconciliation status:

| Option | Items approved | Canonical δ | Cat A delta | Reconciliation status |
|---|---|---|---|---|
| **All-7** | D-1, D-2, D-3, D-4, D-5, D-6a, D-6b | ~300-380 | +5-7 | Requires D-6b drafting (~30 min) |
| **Recommended** | D-1, D-2, D-3, D-4, D-5, D-6a (defer D-6b) | ~130-180 actual ((O5'+O7) ~25 + D-3 ~18 + D-4 ~12 + D-5 ~55 + D-6a ~35 = ~145) | +3 (V5b-F upgrade C→B target; σ_multi^A; σ_multi^D; T-σ-Multi-1 — actually +4 new C-IDs) | All proposal texts FINAL |
| **Conservative** | D-1, D-2, D-3, D-4 (defer D-5, D-6a, D-6b) | ~70-90 ((O5'+O7) ~25 + D-3 ~18 + D-4 ~12 = ~55, plus theorem_status updates ~15-30) | +1 (V5b-F C→B target only) | All proposal texts FINAL |
| **Minimum** | D-1, D-2 (defer rest) | ~25-35 | 0 (Commitment-level convention; no new C-IDs) | All proposal texts FINAL |
| **Defer all** | none | 0 | 0 | No action Day 3 |

(Note: original pre_brainstorm "Recommended" estimate of "~250-310 lines" was high; reconciliation shows actual delta closer to ~145-180 lines after dropping rounding-up.)

**Recommended path**: per `00_*` §3 + plan.md §3 Block 0.5 — **Recommended option** (D-1..D-5 + D-6a, defer D-6b). Reasons:
1. All 6 items have reconciled-FINAL proposal texts.
2. Phase 9-10 dynamic layer (D-6b) not mature enough for canonical-level commitment.
3. Brings σ-framework single-formation + multi-formation static into canonical alignment.
4. ~145-180 line delta is within plan.md §4 estimate (250-310 lines) but on the lower end — reflects Day 2's already-tight proposal drafting.

---

## §4. Default Behavior (No Explicit User Approval)

Per plan.md §6 Hard Constraint + meta-prompt §8.1:

If the user does not explicitly authorize per-item, **default action is DEFER ALL**. Specifically:
- canonical.md unchanged.
- theorem_status.md unchanged.
- CHANGELOG.md unchanged.
- Day 3 99_summary.md will record: "Block 1 user decisions: deferred all (default behavior absent explicit authorization). Day 4+ revisit."
- Block 2 (paper polish) proceeds as planned (does not depend on canonical edits).
- Block 3 (theorem_status / CHANGELOG refresh) becomes trivial documentation-only update (no canonical changes to log).

**Consequence**: CV-1.5 stays current; CV-1.5.1 / CV-1.6 release deferred.

This is a **safe default** — no canonical drift, no premature commitments. User can revisit any time in W5 Days 4-7 or beyond.

---

## §5. Application Instructions (If User Approves)

If user provides explicit authorization (e.g., "approve D-1..D-5 + D-6a, defer D-6b" or "approve Conservative"), Claude executes in this order:

1. **Pre-flight**: `cd CODE && python3 -m pytest tests/ -q --tb=no` (verify 180 passing baseline).
2. **canonical.md edits** (per approved D-* items, in line-order ascending to minimize conflicts):
   - §11.1 Commitment 14 (O5')(O7) (line ~768) — D-1, D-2.
   - §11.1 Commitment 14-Multi (after Commitment 14) — D-6a (and D-6b if approved).
   - §13 T-V5b-T-(d) line ~1129 — D-4.
   - §13 T-V5b-T line ~1151 — D-3.
   - §13 new T-V5b-T' entry after line ~1167 — D-5.
3. **Per-edit verification**: `git diff canonical.md` to inspect; `pytest tests/ -q` to confirm 180 still passing.
4. **theorem_status.md update**: CV-1.5.1 release entry + new C-IDs + Cat A count update.
5. **CHANGELOG.md append**: Phase 1-10 cumulative entry per Block 3 template.
6. **Output `01a_canonical_promotion_log.md`**: ~150-200 lines documenting all edits + verification + git diff.

**Failure mode handling**:
- If pre-flight fails (180 tests not passing): abort; report state; do not edit.
- If post-edit pytest drops below 180: revert specific edit; investigate.
- If `git diff` shows unexpected changes: abort; report; investigate.

**Estimated execution time** (from authorization to logged completion):
- Conservative (D-1..D-4): ~30 min.
- Recommended (D-1..D-5 + D-6a): ~60 min.
- All-7 (with D-6b drafting): ~90 min.

---

## §6. Hard Constraint Verification

- [x] canonical 직접 수정 0 — this file is decision packaging only.
- [x] Silent resolution 0 — all 7 items explicitly listed with source phase + reconciliation status; D-6b explicitly flagged as needing drafting.
- [x] No primitive override, no 4-term merging, no closure idempotence.
- [x] K not dual-treated — K integer throughout; D-6a/b applies to K-field architecture per canonical I9.
- [x] No metastability without P-F flag — D-6b dynamic note flags "K-jump theory at canonical level" as Cat B sketch, not full thermodynamic claim.
- [x] No reductive equation — D-6b mentions LSW + CH correspondence as **correspondence**, not reduction (per CN10).
- [x] OMC pull orchestration not invoked.

---

**End of 01_canonical_promotion_queue_review.md.**
**Status: 7 user-decision items packaged with per-item summary, edit target, line delta, Cat status delta, decision options. Awaits user explicit per-item authorization. Default absent authorization: DEFER ALL.**
**Recommended option per `00_*` reconciliation: Approve D-1..D-5 + D-6a, defer D-6b. ~145-180 canonical lines, +4 new C-IDs, CV-1.5 → CV-1.5.1 release.**
