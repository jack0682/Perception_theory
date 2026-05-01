# 04_cv16_packet_recalibration.md — CV-1.6 Packet READY/PARTIAL/DEFER + CV-1.7 Parking Lot

**Session:** 2026-05-01 (W5 Day 5)
**Block:** 3 (CV-1.6 Packet Recalibration + Wave 3 Implicit Candidates Integration, 14:00-16:00)
**Target (from plan.md):** Reclassify the CV-1.6 11 D-items packet under post-EOD-cluster-aware discipline. Introduce CV-1.7 parking lot as a separate destination so post-EOD content has a home that is not CV-1.6. Prescribe canonical-section addressing for Wave 3 implicit candidates (Schramm / CN15 / N-1 Kramers). Estimate revised count. List working files explicitly **NOT** in CV-1.6 with one-line reason each.
**This file covers:** plan.md §3 Block 3 (14:00-14:30 omc-team OAT collection / 14:30-15:30 reclassify / 15:30-16:00 packet note).
**Depends on reading:** `working/CV-1.6_packet_crosswalk.md` (205 lines, lead-direct), `working/MF/commitments_18_19_drafts.md` (144), `working/MF/commitment_18_sigma_rich_packet.md` (459, post-EOD), `working/MF/commitment_19_k_selection_axiom_packet.md` (376, post-EOD), `working/MF/mathematical_scaffolding_4tools.md` §8.1 (Commitment 17 4-tool), `working/MF/cn15_static_dynamic_separation.md` (146), `working/MF/n1_kramers_extension.md` (121), `working/SF/theorem_2g_schramm_restatement.md` (156), `02_verification_audit.md` §3.4 (critic state).

---

## §1. Reclassification Rule (binding for Day 5)

**Default for un-critic-checked post-EOD content** = PARTIAL → **CV-1.7 parking lot**.

**Default for Wave-3-completed lead-direct content with no outstanding critic verdict** = READY-NEAR (entry into CV-1.6 packet at W6 D6-D7 finalize).

**Default for Wave-3-revised content awaiting critic re-verdict** (NQ-187 pivot 819 lines, NQ-253 revised, NQ-249 M2-M6 residue) = PARTIAL — not blocking CV-1.6 release if release-narrative does not depend on these (caveat-based inclusion only).

**Inheritance rule**: do **not** inherit Day 4 optimism. Quantity of Day 4 working lines does not equal CV-1.6 readiness.

---

## §2. CV-1.6 11 D-Items: READY / PARTIAL / DEFER Table

For each item: status + one-line evidence + responsible owner + W6 dispatch decision.

### §2.1 Ontological D-items

| D-item | Day 5 status | Evidence | Owner | W6 action |
|---|---|---|---|---|
| **O1 K-status (Commitment 16)** | ✅ DONE CV-1.5.1 | `K_status_commitment.md` 480 lines (OAT-1) → Commitment 16 canonical at CV-1.5.1 | (already canonical) | Verify only at W6 D7 packet finalize |
| **O2 Shared-pool I9'** | 🟡 PARTIAL | `shared_pool_canonical_proposal.md` 402 lines (OAT-4) ready; omc-team worker 3 supplementary refinement TBD; canonical proposal text not yet drafted as canonical insertion | omc-team worker 3 + lead | W6 D3 short integration (~45min per `99_summary.md` Day 4 §4 cuts) |
| **O3 F bridge + λ_rep** | 🟡 PARTIAL | `F_Kstep_K_triple.md` 451 lines (OAT-2; **BC-1 fails generic update applied**) + `lambda_rep_ontology.md` 360 lines (OAT-3; Argument C strict fail honest, Option 3 contrastive recommended) | omc-team workers 1+2 + lead | W6 D1 evening (OAT-2, ~50 lines PH layer) + W6 D2 short (OAT-3, ~30min Option 3 only) |
| **O4 C_t coexistence** | 🔴 DEFER | `cobelonging_vs_sigmaD.md` 392 lines (OAT-5) records *Option C-3 variant* + orthogonality witness, but **no positive claim**; OAT-5 status per `15_wave4_carry_forward.md` §3 = "no claim made; new dispatch needed but defer to W6" | OAT-5 lead pending W6 dispatch | W6 D3 PM new dispatch `oat5-c_t-prover` if still unaddressed |
| **O5 Commitment 17 (4-tool)** | ✅ READY | `mathematical_scaffolding_4tools.md` 613 lines §8.1 has formal Commitment 17 text (Tool A1 stratified §3.10 entry / A2 quotient ontological primacy / A3 σ_multi^A(t) ≅ PH barcode + NQ-242 PH pipeline / A4 contrastive — CN5 amendment). **Tool A4 partial fail honest acknowledgment preserved** | (CV-1.6 lead) | W6 D5-D7 packet finalize ~80-100 canonical lines |
| **(Implicit O6) Schramm-restatement** | ✅ READY-NEAR | `theorem_2g_schramm_restatement.md` 156 lines lead-direct + numerical anchor `sigma_locality_R23_cycle_torus.json` (3 graph classes, `"all_locality_predicates_hold": true`) | team-lead (Wave 3 lead-direct) | W6 D6-D7 packet integrate as T-PreObj-1G addendum subsection §13 |
| **(Implicit O7) CN15 static-dynamic** | ✅ READY-NEAR | `cn15_static_dynamic_separation.md` 146 lines lead-direct; static $K = 1$ on pure $\mathcal{E}_{\mathrm{bd}}$ vs dynamic $K_{\mathrm{act}}$ on full $\mathcal{E}$ separation — explains apparent K=1 vs K>1 conflict cleanly | team-lead (Wave 3 lead-direct) | W6 D6-D7 packet integrate as §11.1 CN15 amendment |
| **(Implicit O8) N-1 Kramers** | ✅ READY-NEAR | `n1_kramers_extension.md` 121 lines lead-direct; **P-F flag preserved**; connects N-1 (Soft-Hard Switching Asymmetry) to K-Selection (b) Kramers candidate without claiming closure | team-lead (Wave 3 lead-direct) | W6 D6-D7 packet integrate as N-1 sub-statement under appropriate §13 entry; **NOT** as standalone Cat A theorem (P-F flag prevents) |

### §2.2 Process D-items

| D-item | Day 5 status | Evidence | Owner | W6 action |
|---|---|---|---|---|
| **P1 V5b-F C(β) (NQ-198k)** | 🔴 DEFER → W6+ | NQ-198k functional form scan not started; ~8h compute budget; not in Day 5 scope | NQ-198k numerical | W6 D4 launch + W6+ analysis |
| **P2 V5b-T-zero (NQ-198l)** | 🔴 DEFER → W6+ | T-V5b-T-zero already Cat A def at CV-1.5.1; universality test (NQ-198l) requires extended graph classes; ~6h compute | NQ-198l numerical | W6+ |
| **P3 3D LSW (NQ-244)** | 🟡 PARTIAL (Day 5 launch only) | Day 5 background launch + metadata only (Block 4a → `05_nq244_launch_note.md`); **no Day 5 interpretation**; result analysis = Day 6+/W6 D4 | NQ-244 background | Day 5 launch metadata; W6 D4 result analysis |
| **P4 G5 SF Round 1-5 merge** | 🟡 PARTIAL | Wave 3 revisions integrated (NQ-187 pivot 819 lines, NQ-188 ACCEPT-WITH-RESERVATIONS, NQ-189 4-fix, NQ-190 ACCEPT, NQ-244 σ-trajectory perturbation Cat A piecewise). **NQ-187 pivot critic re-verdict pending** (`02_verification_audit.md` §3.1) → NQ-187 contributes only as **caveat-based inclusion** at CV-1.6, not Cat A re-promotion | Wave 3 owners + team-lead at W6 D6 close | W6 D6 G5 merge with NQ-187 caveat per `03_t_sigma_theorem4_reconciliation.md` §4.1 provisional text |
| **P5 NQ-242 PH** | 🟡 PARTIAL | working file framework ready (`sigma_multi_trajectory.md` 283 lines + post-EOD `sigma_rich_VR_phase1.md` 336 lines design). PH pipeline infrastructure not yet implemented (PHAT/GUDHI/Ripser library integration) | NQ-242 PH owner | W6 D1-D5 PH pipeline implementation + Phase 1 V-R + Phase 2 zigzag |

### §2.3 Aggregate by status

| Status | Count | D-items |
|---|---:|---|
| ✅ READY (CV-1.5.1 done or Day 5 ready) | 2 | O1 + O5 |
| ✅ READY-NEAR (Wave 3 lead-direct, packet integrate at W6 D6-D7) | 3 | Implicit O6 Schramm + O7 CN15 + O8 N-1 Kramers |
| 🟡 PARTIAL (W6 work needed, included with caveat) | 5 | O2 + O3 + P3 + P4 + P5 |
| 🔴 DEFER (W6+ scope) | 3 | O4 + P1 + P2 |
| **Net CV-1.6 candidate items** | **10** (including PARTIAL with caveats) | excludes 3 DEFER |

---

## §3. CV-1.7 Parking Lot (NEW destination category)

The post-EOD op-0008-architect cluster (16 files, ~3848 lines) needs a destination label that is not CV-1.6. **CV-1.7 parking lot** is the safe label.

### §3.1 Cluster contents (parking lot inhabitants)

| Cluster | Files | Lines | Promotion target |
|---|---:|---:|---|
| σ_rich foundation | 8 (sigma_rich_augmentation 533 + centroid 306 + orientation 311 + phi_proof 313 + wigner 333 + vs_standard 444 + VR_phase1 336 + sigma_rich_refinement_theorem 188) | 2764 | CV-1.7 Commitment 18 candidate |
| σ-fingerprint | 2 (sigma_fingerprint_qrcode 195 + sigma_fingerprint_algorithm 344) | 539 | CV-1.7+ (NQ-264 Cat B target via R23 numerical W6+) |
| K-Selection | 4 post-EOD (k_selection_a 306 + b 315 + c 409 + compatibility 365) + 1 upstream (k_selection_mechanism 520 op-0005-architect) | 1915 | CV-1.7+ Commitment 19 candidate |
| Reconciliation drafts | 2 (sigma_theorem4_canonical_revision 338 + nq187b_L_extrapolation 422) | 760 | T-σ-Theorem-4 reconciliation triple γ/β/α inputs (NOT canonical revision today) |
| Commitment packets | 2 (commitment_18_sigma_rich_packet 459 + commitment_19_k_selection_axiom_packet 376) | 835 | CV-1.7+ formal proposal drafts |
| NQ-242c | 1 (nq242c_explicit_construction.md 475) | 475 | W6 D6 input for Lemma 4.2(c) σ^A non-determinism explicit construction |
| Auxiliary categorical | 2 lead-direct (sigma_class_category 185 + sigma_lie_algebra_structure 323) | 508 | CV-1.7+ (Bridge B-3 π_1 + categorical framing extensions) |
| π_1 | 1 (formation_fundamental_group 349, pi1-formation-prover) | 349 | CV-1.7+ (B-3 π_1 formal Cat C) |

**Subtotal in parking lot**: ~17 files / ~8145 lines.

### §3.2 Parking lot rule

- **Working/-only labels with explicit "CV-1.7 candidate" header** to be added at W6 D6 packet finalize (not Day 5; preserves single-modification scope).
- **No Day 5 promotion attempt** for any parking-lot item.
- **Critic re-review at W6+** unblocks promotion path (post-EOD cluster default = PARTIAL → critic verdict needed before any CV-1.7 promotion).
- **CV-1.7 release target**: ~W7-W9 (per `commitments_18_19_drafts.md` §6 net CV roadmap).

### §3.3 Parking lot risk

If the parking lot becomes a "permanent storage" rather than a *transit* destination, post-EOD work degrades silently. **Mitigation**: W6 D6 parking-lot list + critic dispatch checklist must explicitly trigger W6+ critic re-review for each cluster file. Day 5 closes parking-lot definition; W6 owns transit.

---

## §4. Wave 3 Implicit Candidates — Canonical Section Addressing

For each implicit candidate (O6 / O7 / O8), specify **exactly which canonical section** it would enter at CV-1.6 release. **Drafts only — no canonical edit today.**

### §4.1 Implicit O6 — T-PreObj-1G Schramm-restatement addendum

**Target section**: `canonical.md` §13 T-PreObj-1G entry (existing Cat A graph-class independent theorem from CV-1.3 W4 merge), addendum subsection.

**Proposed addendum text** (provisional, ~30 canonical lines):
> *Schramm-locality reframing addendum (CV-1.6, post W5 Day 4 numerical anchor).* The graph-class independence of T-PreObj-1G admits a Schramm-style local restatement: for two finite connected graphs $G_1, G_2$ whose $u$-stabilizer subgroups $\mathrm{Aut}(G_i)_{u_i^*}$ are isomorphic and whose ambient $\mathrm{Aut}(G_i)$ actions on $V_2$ (Fiedler doublet eigenspace) are irrep-compatible, the first-pitchfork σ-tuples $\sigma(u_1^*)$ and $\sigma(u_2^*)$ are identical. Numerical anchor across 3 graph classes (R23 D_4 free-BC L=8 grid, Z_n cycle n=20, Z_n × Z_n torus n=10) confirms the locality predicate via direct verification (`CODE/scripts/results/sigma_locality_R23_cycle_torus.json`, `"all_locality_predicates_hold": true`).
>
> **Cat status**: Cat A definitional refinement (locality predicate is itself a definition; numerical confirmation across 3 graph classes is supporting empirical anchor for the conditional Cat A target). Promotion to Cat A theorem in continuum-limit form requires NQ-262 W7+ proof.

**Net effect** on CV-1.6 counts: +1 Cat A definitional refinement (counting as inline Cat A entry, no new claim line) OR +1 Cat A in continuum-limit form (counting as new claim) — depends on packet finalize style. Conservative count: +0 to +1 Cat A.

### §4.2 Implicit O7 — CN15 static-dynamic separation

**Target section**: `canonical.md` §11.1 CN amendment (CN15 NEW or CN amendment to CN6+).

**Proposed text** (provisional, ~20 canonical lines):
> **CN15. Static / Dynamic Separation.** The K=1 global energy minimum on pure $\mathcal{E}_{\mathrm{bd}}$ (T-Merge (b) Cat A) and the dynamic K-protocol-endpoint observable $K_{\mathrm{act}}$ on full $\mathcal{E}$ are *distinct quantities* — equality is the special case where the gradient flow trajectory converges to the global static minimum, generically false under noise / non-equilibrium initial conditions / finite-time observation. The apparent K=1 vs K>1 conflict (originally OP-0001 F-1 / OP-0002 M-1) is resolved by this separation: pure-static is a *theorem* (T-Merge (b)), dynamic-observable is an *empirical quantity* (K_act per Commitment 16); they live at different conceptual layers and need not agree.

**Net effect**: +1 CN entry (no theorem count change; CN-level commitment).

### §4.3 Implicit O8 — N-1 Kramers extension sub-statement

**Target section**: `canonical.md` §13 — **NOT** a standalone Cat A theorem (P-F flag prevents). Possibilities:
- (a) Sub-statement under K-Selection (b) candidate — but K-Selection is OP-0005 OPEN, not yet a canonical theorem.
- (b) Sub-statement under N-1 (Soft-Hard Switching Asymmetry) — but N-1 is currently a *re-framing* in `THEORY/working/open_problems_reframing_2026-04-19.md`, not a canonical theorem either.
- (c) Inline note in `open_problems.md` OP-0005 K-Selection entry.

**Recommended target**: (c) inline note in `open_problems.md` OP-0005 entry, ~10 lines linking N-1 ↔ K-Selection (b) with explicit P-F flag reminder. **NOT** §13.

**Net effect**: +0 theorem count; +0 Cat A; cross-reference enrichment of OP-0005 only.

---

## §5. Revised CV-1.6 Count Estimate

Per `13_wave3_critical_findings.md` §7 baseline + Day 5 reclassification adjustment:

| Category | CV-1.5.1 | CV-1.6 estimated | Δ |
|---|---:|---:|---|
| Cat A | 45 | **46-49** | +1 (Schramm addendum, conservative) to +4 (Schramm + V5b-F C(β) Cat B → Cat A if NQ-198k closes + V5b-T-zero universality if NQ-198l closes + NQ-244 3D Cat B target if confirms) |
| Cat B | 5 | **6-7** | +1 (Theorem 4.6.1 σ_multi^A(t) PH barcode equivalence if NQ-242 PH Phase 1 closes) to +2 (additional from 3D LSW Cat B target) |
| Cat C | 5 | 5 | 0 |
| Retracted | 5 | 5 | 0 |
| **Total claims** | 60 | **63-65** | +3 to +5 |
| % proved | 75% | **73-76%** | balanced shift (more Cat A but more Cat B too) |

**Key non-changes (do NOT inflate)**:
- T-σ-Theorem-4 stays Cat B (Cat A re-promotion blocked by 3-way A_2/A_1 discrepancy → CV-1.7+ post-reconciliation; per `03_t_sigma_theorem4_reconciliation.md` §4-§5).
- Commitment 17 4-tool entry adds Commitment-level content, not theorem count.
- σ_rich Commitment 18 + K-Selection Commitment 19 are CV-1.7+ parking lot, not CV-1.6.
- π_1 (formation_fundamental_group.md 349 lines) + Lie algebra (sigma_lie_algebra_structure.md 323) + σ-class category (185) are CV-1.7+ parking lot.

**Net CV-1.6 release narrative** (per Day 5 reclassification): smaller but cleaner picture than Day 4's inflated 11-D-items + 3-implicit count. **Effective inclusion: 7 D-items + 3 implicit candidates = 10 CV-1.6 packet items**, with 3 deferred (O4 + P1 + P2) and 6 in parking lot.

---

## §6. Working Files NOT in CV-1.6 (with one-line reason)

Files persisted in working/ at Day 4 EOD that are *explicitly excluded* from CV-1.6 release packet:

| File | Lines | Reason |
|---|---:|---|
| `working/MF/sigma_rich_augmentation.md` | 533 | post-EOD; CV-1.7 Commitment 18 parking lot |
| `working/MF/sigma_rich_centroid_derivation.md` | 306 | post-EOD un-audited |
| `working/MF/sigma_rich_orientation_derivation.md` | 311 | post-EOD un-audited |
| `working/MF/sigma_rich_phi_proof.md` | 313 | post-EOD un-audited; OP-0008 Path B Cat A target ≠ CV-1.6 promotion |
| `working/MF/sigma_rich_wigner_derivation.md` | 333 | post-EOD un-audited |
| `working/MF/sigma_rich_vs_standard_R23.md` | 444 | post-EOD; CV-1.7+ via NQ-264 Cat B target |
| `working/MF/sigma_rich_VR_phase1.md` | 336 | post-EOD; W6+ NQ-242 PH Phase 1 input |
| `working/SF/sigma_rich_refinement_theorem.md` | 188 | post-EOD; CV-1.7+ |
| `working/SF/sigma_fingerprint_qrcode.md` | 195 | CV-1.7+ NQ-264 R23 verification |
| `working/SF/sigma_fingerprint_algorithm.md` | 344 | post-EOD; CV-1.7+ |
| `working/MF/k_selection_mechanism.md` | 520 | OP-0005 OPEN; CV-1.7+ Commitment 19 |
| `working/MF/k_selection_a_free_energy.md` | 306 | post-EOD candidate (a); P-F flagged at finite T |
| `working/MF/k_selection_b_kramers.md` | 315 | post-EOD candidate (b); P-F flagged metastability |
| `working/MF/k_selection_c_numerical_anchor.md` | 409 | post-EOD candidate (c); CV-1.7+ via NQ-302/303 numerical |
| `working/MF/k_selection_compatibility_proof.md` | 365 | post-EOD; compatibility with Commitment 16 (already canonical) |
| `working/MF/commitment_18_sigma_rich_packet.md` | 459 | post-EOD draft; CV-1.7 release target |
| `working/MF/commitment_19_k_selection_axiom_packet.md` | 376 | post-EOD draft; CV-1.7+ release target |
| `working/MF/nq242c_explicit_construction.md` | 475 | post-EOD; W6 D6 input, not CV-1.6 |
| `working/SF/sigma_class_category.md` | 185 | CV-1.7+ Bridge B-3 categorical framing |
| `working/SF/sigma_lie_algebra_structure.md` | 323 | NQ-258 McKay-spirit; CV-1.7+ Lie algebra reading |
| `working/SF/formation_fundamental_group.md` | 349 | B-3 π_1 formal Cat C; CV-1.7+ |
| `working/SF/sigma_theorem4_higher_order.md` | 819 | NQ-187 pivot; T-σ-Theorem-4 caveat-only inclusion via reconciliation note (`03_*`); not standalone canonical |
| `working/SF/sigma_theorem4_canonical_revision.md` | 338 | reconciliation triple input; not Day 5 canonical |
| `working/SF/nq187b_L_extrapolation.md` | 422 | α-path numerical input; not Day 5 canonical |
| `working/MF/scc_mass_gap_connection.md` | 445 | NQ-249 M2-M6 W6 residue; CV-1.7+ |
| `working/MF/formation_birth_string_breaking.md` | 520 | NQ-253 revised; W6 critic re-review needed; QuEra 2025 citation hard-blocker |
| `working/MF/r24_dataset_design.md` | 146 | numerical infrastructure spec; not canonical |
| `working/MF/op003_mo1_status_review.md` | 140 | sidestep preservation review; canonical OP-0003 already records sidestep + re-activation rider |

**Subtotal NOT in CV-1.6**: ~28 files / ~10,150 lines. → CV-1.6 packet is intentionally a *small slice* of Day 4's working output.

---

## §7. Risk Watch (CV-1.6 release narrative)

### §7.1 Risk: OP-0009 over-claim (per Critic MAJOR-3)

**Mitigation**: CV-1.6 release narrative must use the verbatim wording **"OP-0009 framework + 1/7 sub-items resolved (K via Commitment 16) + 6/7 sub-items partially addressed"** per `05_critic_final_review.md` MAJOR-3. Do **not** claim "OP-0009 framework-level resolved" or "Theory Deepening Stretch 100%". This wording is binding for `99_summary.md` (Day 5 close), W5 weekly_summary.md, and CV-1.6 release CHANGELOG entry.

### §7.2 Risk: post-EOD cluster lobbies for CV-1.6 inclusion via volume

**Mitigation**: explicit CV-1.7 parking lot label on every cluster file at W6 D6 packet finalize; this file (`04_cv16_packet_recalibration.md`) §6 is the binding "NOT in CV-1.6" list.

### §7.3 Risk: T-σ-Theorem-4 caveat appears as 9th-hour add-on at release

**Mitigation**: `03_t_sigma_theorem4_reconciliation.md` §4.1 provides provisional caveat text drafted today; W6 D5 γ-path verdict updates it; W6 D7 release adopts final form. Two weeks lead time.

### §7.4 Risk: CV-1.6 drift to "small + clean" → user expectation mismatch with prior 11-D-item promise

**Mitigation**: `99_summary.md` (Day 5 close) §5 + W5 weekly_draft_storming.md 05-01 entry explicitly note that Day 5 reclassification reduced CV-1.6 inclusion count from naive 11 to effective 10 (with 3 PARTIAL caveat-based + 7 READY/READY-NEAR + 3 DEFER + 6 parking lot). Reduction is *honesty*, not failure.

---

## §8. Day 5 Hard Constraint Compliance (this file)

- [x] **canonical 직접 수정 0** — log file only; no canonical edits proposed for application today.
- [x] **No silent OP resolution** — OP-0009 wording binding per Critic MAJOR-3; OP-0005/0008 explicitly NOT resolved (CV-1.7+ parking lot).
- [x] **u_t primitive maintained** — all candidates respect.
- [x] **CN5 4-energy not merged** — Commitment 17 Tool A4 preserves 4-energy independence; λ_rep architectural-layer separate per Option 3 contrastive.
- [x] **K not dual-treated** — Commitment 16 K_field/K_act consistent across all D-items.
- [x] **CN10 contrastive** — Tool A4 partial fail honest; Bridge B-2 / B-7 explicitly contrastive not reductive.
- [x] **No metastability claim without P-F flag** — Implicit O8 N-1 Kramers preserves P-F flag; K-Selection (b) candidate parking lot also P-F flagged.
- [x] **CV-1.7 parking lot is a transit destination, not silent abandonment** — W6+ critic dispatch checklist enforced.

---

**End of 04_cv16_packet_recalibration.md.**
**Status:** CV-1.6 packet recalibrated under post-EOD-aware discipline. 10 effective inclusion items (2 ✅ READY + 3 ✅ READY-NEAR Wave 3 implicit + 5 🟡 PARTIAL with caveats); 3 🔴 DEFER (O4 + P1 + P2); 6 CV-1.7 parking lot post-EOD cluster files. Wave 3 implicit candidates (Schramm / CN15 / N-1 Kramers) addressed to specific canonical sections (§13 T-PreObj-1G addendum / §11.1 CN15 amendment / open_problems.md OP-0005 inline). Revised count estimate: 46-49A / 6-7B / 5C / 5R / 63-65 claims / 73-76% proved. ~28 files / ~10,150 lines explicitly NOT in CV-1.6 with reasons. OP-0009 wording binding per MAJOR-3.
