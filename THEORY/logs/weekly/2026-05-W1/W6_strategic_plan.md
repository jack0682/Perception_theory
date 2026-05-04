# W6 Strategic Plan (2026-05-04 ~ 2026-05-10) — Audit-Anchored Redesign

**Created:** 2026-05-04 (replacing the deleted W6_strategic_plan.md ~1,691-line draft).
**Anchor:** the 2026-05-04 audit pass (CHANGELOG entry of the same date) catalogued ~50 critical and ~200 high-severity inconsistencies across canonical, working, code, and meta layers. This W6 plan is built around closing the highest-leverage subset of those, not around growing the surface.

**Discipline:** the previous W6 plan promised 8 goals across 3 pillars in 7 days at "62 hours" (actual sums were 75 and 144). It also silently downgraded the CV-1.7 parking-lot dispatch from "audit" to "checklist preparation" in §6.6. This redesign avoids both failures: it commits to fewer items, with explicit hour budgets that sum honestly, and treats the parking-lot review as a first-class deliverable.

---

## 0. Theme

**"Close the four documented inconsistencies; promote L-M; surface the parking lot."**

W5 ended with CV-1.5.2 (T-L1-F canonical) plus a working draft for L-M (Cat-B sketched). The 2026-05-04 audit found that on top of those substantive results sit a measurable amount of documentation drift. W6 prioritises closing that drift and getting L-M to a state where its CV-1.6 promotion candidacy is honest, rather than chasing more theorems.

## 1. Goals (4 items, prioritised)

### G1 — L1-M-AUDIT (R-1 / R-2 / R-3 closure)

**Status (post W6 D1 EOD closure + canonical promotion):** ✅ **FULLY CLOSED + CANONICALLY PROMOTED.** L-M-2 Cat-B sketched → **Cat-A conditional** via explicit closure of R-0 (§2.2 Phi-4c F1 wording simplification) + R-1 (factor-2 sharpness verified by explicit admissible perturbation $R_j(v)=+\rho_{\mathrm{pert}}/2$, $R_j(w)=-\rho_{\mathrm{pert}}/2$; (P0) factor-1 sharpening structurally inapplicable since Type-N bars are intra-slot merge bars, not terminal) + R-2 (§5.5 Type-B chain replaced with explicit P5-direct derivation; no T-L1-F LG-7 dependency) + R-3 (Type-N non-terminal clarification consistent with R-1). Theorem L-M post-repair Cat A conditional under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau) + \tau < \tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$ (uses $\rho_{\mathrm{bg}}$ post-R2; NQ-G1-1 self-correction integrated: $\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ configuration-dependent, NQ-G1-1-ext W7+ for empirical anchor). Per-family corollaries: L-M.A (hard) Cat A absolute, L-M.B (logistic $s\ge 50$) + L-M.C (shift-sat $\beta\ge 20$) Cat A conditional inheriting.

**External L-M-K-style audit (NQ-G1-3):** ✅ PASS (W6 D1 EOD, ~7 min cold-review general-purpose agent dispatch). All 4 closures + Theorem L-M composition verified rigorous; persistence-skeleton preservation disclosure added per auditor recommendation.

**Canonical promotion:** ✅ APPLIED (W6 D1 EOD second addendum, supervised user authorization). T-L1-M new entry in `canonical.md` §13 line 1491 immediately after T-L1-F; C-0722 row in `theorem_status.md` line 197 (accepted Cat A conditional). L-M draft promoted from `logs/daily/2026-05-03/02_L1M_proof_development.md` to `working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` with full R-0/R-1/R-2/R-3 closures + NQ-G1-1 self-correction.

**Deliverables (substantively exceeded):** L-M-2 Cat-A conditional ✅ + canonical promotion ✅ + external audit PASS ✅ + working draft updated ✅. Per W6 plan §2 explicit non-goals, "L-M canonical promotion" was originally deferred until CV-1.6 release prep; user "promotion 정리" directive triggered same-day exception based on external audit PASS providing third-party verification rigor.

**Actual effort:** Day 1 mid-day self-audit (~3h) + Day 1 EOD external audit (~7 min agent + ~30 min integration) + Day 1 EOD supervised canonical promotion (~30 min) — **vs. original 3-4 day estimate**. Day 4-5 budget freed for deferred numerical NQ-G1-2 (P9-tight regime experiment) + NQ-G3-1 ε stability + W7+ seed work.

**Priority:** P0 (must) — ✅ CLOSED.

**Open follow-ons (not blockers):**
- NQ-G1-1-ext (W7+): empirical $\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ comparison via L1-I script extension to record $\|R_{\mathrm{inact}}\|_\infty$ separately.
- NQ-G1-2: ✅ **EXECUTED** (W6 D1 EOD thirteenth addendum). Post-processing wrapper `CODE/scripts/op_resolution_nq_g1_2_p9_tight.py` re-classified all 1920 baseline configurations under 5 budget regimes without re-computation. Verdict: R0 = R1 = 439/1920 (faithful (P9-tight) interpretation); H6' is **non-binding** in L1-I FEASIBLE set; (P9-tight) is CANDIDATE for L1-J' regime promotion enabling factor-1 sharpening **without empirical penalty** (R0 ⊆ R1 with |R1\R0| = 0). Cat A conditional status of T-L1-M unchanged.
- NQ-G1-2-ext (W7+): direct $\|R_j\|_\infty$ measurement under shared-pool gradient-flow dynamics (whether physical perturbations actually satisfy $(P9$-$\mathrm{tight}): \|R_j\|_\infty \le \rho_{\mathrm{pert}}/4$). Required for canonical adoption of (P9-tight) → L1-J'. Estimated ~1-2h.

### G2 — Resolve the T-Bind-Proj / T-Bind-Full categorical disagreement

**Status:** the 2026-05-04 audit found three different category designations for T-Bind-Full across the canonical layer:
- `canonical.md:1448` — Cat A.
- `theorem_status.md:163-164` — Cat C (very conditional).
- `theorem_status.md:285` (CV-1.1 release row) — Cat A (τ=1/2 only).

T-Bind-Proj similarly disagrees: `canonical.md:1440-1448` says Cat A for all τ_cl ∈ (0,1); `theorem_status.md:163-164` says Cat B (τ=1/2 only).

Until this is resolved, the project does not know which Cat A count is true (and the §15 closing summary's "46 Cat A" rests on the canonical reading; if the theorem_status reading wins, the count is lower).

**Deliverable:** a single decision on T-Bind-Proj and T-Bind-Full's category, applied to both `canonical.md` and `theorem_status.md`, with the affected counts updated in §15 and §13.

**Estimated effort:** 1 day (mostly reading the proofs to decide which category is right).
**Priority:** P0 (must).

### G3 — K_act ε-convention decision and propagation

**Status:** Commitment 16 (canonical) proposes default ε = 0.01·m̄. Production scripts (`l1g_l1hyp_diagnostic.py`, `l1i_constants_feasibility.py`, `wq_lat1_*.py`, `nq242c_*.py`) all use ε = 0.225 (~0.075·m̄ for K_field = 4). T-L1-F's "439/1920 = 22.9% feasible" empirical claim is for ε = 0.225, not Commitment 16's default.

Without unification, the conditional Cat A status of T-L1-F is ambiguous: under which ε does the regime hold non-vacuously?

**Deliverable:** a single canonical ε convention (either confirm Commitment 16 default and re-run the empirical scripts, or amend Commitment 16 to match the script default), applied across canonical / working / scripts.

**Estimated effort:** 1 day if the decision is to amend Commitment 16 (no re-run needed); 2-3 days if the decision is to re-run scripts with ε = 0.01·m̄.
**Priority:** P0 (must) — this directly affects the load-bearing T-L1-F empirical claim.

### G4 — Parking-lot review Stage 0 (Inventory)

**Status (post W6 D1 EOD):** ✅ **STAGE 0 COMPLETED 4–5 days early.** Original W5 narrative claimed "17 unaudited working files (~8,145 lines)"; W6 D1 EOD Stage 0 inventory found actual count **49 files / 17,269 lines** (~2.9× / 2.1× drift). Inventory file `THEORY/working/CV-1.7_parking_lot_inventory.md` (~430 lines) produced with per-file Cat-status / cluster / cross-reference metadata. Issue #1–#5 series subsequently resolved (CHANGELOG addendums #4–#12) with chain-verification audit pattern documented. Plan at `THEORY/working/CV-1.7_PARKING_LOT_REVIEW_PLAN.md` (Stage 1 per-file Cat-header drafting + Stage 2 cluster critic dispatch remain W7+ scope).

**Deliverable:** `THEORY/working/CV-1.7_parking_lot_inventory.md` with all 17 (or actual count) files enumerated. Per-file critic dispatch (Stage 2) is **out of scope for W6** — that is the W7+ workstream.

**Estimated effort:** 1 day.
**Priority:** P1 (should).

## 2. Explicit non-goals for W6

Things deliberately NOT attempted this week (status updated post W6 D1 EOD):

- ~~**CV-1.6 release.** Previous W6 plan targeted Day 7 EOD release. This redesign treats CV-1.6 as deferred until G1+G2+G3 close.~~ **REVISED post W6 D1 EOD:** all G1+G2+G3 closure blockers removed (G2 evening canonical, G3 D1 verdict + Commitment 16 amendment applied, G1 audit + canonical promotion). CV-1.6 release feasibility upgraded from "deferred indefinitely" to **"W6 D7 EOD CANDIDATE"**. User decision pending per Decision Point 4.
- **T-σ-Theorem-4 γ-path audit.** Was G3 in old plan. Deferred; per 2026-05-04 user decision, the NQ-187 falsification handling is to be revisited later. *(Status unchanged W6 D1 EOD: NQ-187 continuum-vs-discrete caveat applied to canonical T-σ-Theorem-4 entry per evening G2 commit; γ/β/α reconciliation still W7+.)*
- ~~**L1-M canonical promotion.** L1-M-AUDIT (G1 above) is the prerequisite. Even if G1 closes cleanly to Cat-A conditional, the actual canonical merge is a CV-1.6 release activity, not a W6 commit.~~ **REVISED post W6 D1 EOD:** L-M canonical promotion **applied W6 D1 EOD** as supervised special-case authorization (CHANGELOG second addendum) after external L-M-K-style audit PASS. T-L1-M now in `canonical.md` §13 line 1491; C-0722 row in `theorem_status.md` line 197.
- **OAT-2 / OAT-3 short integration.** Was G7 in old plan. Deferred — not blocking anything this week. *(Status unchanged: still deferred to W7+.)*
- **NQ-244 3D LSW analysis.** Was G8 in old plan. Background script not confirmed launched (audit found ambiguous launch status). Deferred until launch is verified. *(Status unchanged.)*
- **Wave 3 parking-lot critic dispatch (Stage 2).** Was G5 in old plan. Per the parking-lot plan, this is W7+ work; W6 only does Stage 0. *(Status unchanged: Stage 0 ✅ done W6 D1 EOD; Stages 1–3 remain W7+.)*
- **σ-rich CODE work** (centroid_trajectory.py, vr_persistence.py, k_jump_detector.py mentioned in working files but not in scc/). Out of scope. *(Status unchanged.)*

## 3. Daily breakdown

The below is a target shape, not a rigid schedule. Substantive work (G1, G2, G3) is sequential because each requires reading the same canonical body and would interfere if parallel.

| Day | Date | Original focus | Hours (target) | Original deliverable | Actual W6 D1 EOD status |
|-----|------|----------------|----------------|----------------------|--------------------------|
| Day 1 | 2026-05-04 (Mon, today) | Audit pass 2 closure + W6 plan + start G2 reading | 4 | Pass-2 entry; this plan; G2 reading begun | ✅ **DONE + G2 closed (evening canonical) + G3 D1 verdict applied (mid-day) + G1 audit + canonical promotion + external audit PASS (EOD) + G4 Stage 0 inventory (EOD) + Issue #1–#5 series resolved (EOD) + 12 NQ batch (op_resolution.md) + NQ-G1-2 EXECUTED (post-EOD wrap-up: post-processing + fresh-full-run 5/5 match)** |
| Day 2 | 2026-05-05 (Tue) | G2 finish | 6 | G2 closed | 🟢 **G2 ALREADY CLOSED Day 1 evening.** Day 2 free for: deferred numerical NQ-G3-1, G4 Stage 1 acceleration, W7+ seed, or CV-1.6 release packet prep |
| Day 3 | 2026-05-06 (Wed) | G3 in full | 6 | G3 closed | 🟢 **G3 ALREADY CLOSED Day 1 mid-day** (D1 verdict R1 reading $\bar m = M/K_{\mathrm{field}}$; Commitment 16 line 810 amendment applied per CHANGELOG late re-review). Day 3 free |
| Day 4 | 2026-05-07 (Thu) | G1 part 1 | 6 | R-1 closed; R-2 closed | 🟢 **R-1 + R-2 ALREADY CLOSED Day 1 mid-day** (self-audit Cat A absolute) |
| Day 5 | 2026-05-08 (Fri) | G1 part 2 | 6 | R-3 closed | 🟢 **R-3 + R-0 ALREADY CLOSED Day 1 mid-day** + Theorem L-M Cat A conditional + canonical promotion + external audit PASS |
| Day 6 | 2026-05-09 (Sat) | G4 inventory | 4 | Inventory of 17 files | 🟢 **G4 ALREADY CLOSED Day 1 EOD** with 49 files / 17,269 lines (audit-trail correction over W5 narrative "17 / 8,145"). Day 6 free |
| Day 7 | 2026-05-10 (Sun) | W6 close: weekly_summary + W7 seed | 3 | `weekly_summary.md` | ⏳ Day 7 unchanged in spirit; possible scope: weekly_summary + CV-1.6 release packet prep (since release feasibility upgraded to W6 D7 EOD candidate) |

**Total target hours: 35** (vs old plan's claimed-62 / actual-75-144). **Actual Day 1 hours used: ~10–12h (across morning/mid-day/evening/EOD/post-EOD wrap-up).** Net W6 D2–D7 schedule has ~3-day slack relative to original plan.

## 4. Success criteria

- **Bronze (minimum):** G2 closed (T-Bind decision applied); G3 closed (ε convention chosen); audit-pass-2 entry in CHANGELOG (already done). G1 and G4 may slip. → ✅ **MET Day 1 evening** (G2 + audit-pass-2) + ✅ **G3 closed Day 1 mid-day**.
- **Silver (default target):** Bronze + G1 closed (R-1/R-2/R-3 resolved one way or the other); G4 inventory produced. → ✅ **MET Day 1 EOD** (G1 fully closed at every layer including canonical promotion + external audit PASS; G4 Stage 0 inventory produced).
- **Gold (stretch):** Silver + G4 first-cluster (Reconciliation drafts) critic dispatch completed (carries Stage 1 of parking-lot plan into W6). → 🟡 **PARTIALLY MET Day 1 EOD** via Issue #1–#5 series (CHANGELOG addendums #4–#12) acting as quasi-Stage-1 critic dispatches for Cluster F audit; full Stage 1 per-file Cat-header drafting remains W7+ scope.

**Net post W6 D1 EOD:** **Silver target met; Gold partially met. Day 2–7 unused.** Possible Day 2-7 scope upgrade options: (a) finish Stage 1 per-file headers (49 files), (b) execute deferred NQ-G3-1, (c) CV-1.6 release packet prep (release feasibility upgraded to W6 D7 EOD candidate), (d) W7+ seed work.

## 5. Decision points

These need user input or explicit deferral by W6 close, otherwise they become silent drift. (Status updated post W6 D1 EOD.)

1. ~~**Day 2 EOD:** T-Bind-Proj / T-Bind-Full category decision (Cat A or Cat B/C). Affects §15 closing-summary count.~~ ✅ **CLOSED Day 1 evening**: both Cat A confirmed; canonical edits applied at `canonical.md:1452, 1457` + `theorem_status.md:163-164, 285`.
2. ~~**Day 3 EOD:** ε convention decision (Commitment 16 default vs script default). Affects T-L1-F empirical regime.~~ ✅ **CLOSED Day 1 mid-day**: R1 reading $\bar m = M/K_{\mathrm{field}}$; Commitment 16 line 810 amendment applied per CHANGELOG late re-review.
3. ~~**Day 5 EOD:** if R-3 cannot be closed, decide whether L-M is retained at Cat-B sketched (working) or formally moved to Cat C / retracted.~~ ✅ **CLOSED Day 1 mid-day**: R-3 closed (Type-N non-terminal clarification, Cat A absolute follow-on of R-1); Theorem L-M post-repair Cat A conditional.
4. **Day 7 EOD (W6 close):** decision on whether CV-1.6 release becomes a W7 target or is deferred indefinitely. ~~Default: deferred until parking lot is at least partially resolved.~~ **REVISED post W6 D1 EOD:** parking-lot Stage 0 done + G1+G2+G3 closure blockers all removed → CV-1.6 release feasibility = **W6 D7 EOD CANDIDATE**. New options: (a) push CV-1.6 release Day 7 EOD with Stage 0 sufficient, (b) defer to W7 alongside Stage 1, (c) defer further. **OPEN — user decision required.**

## 6. Risks (status updated post W6 D1 EOD)

- ~~**G1 slip into G2/G3 territory.** If R-3 turns out to require substantial rework (likely if L1-H2 Lemma 1 itself is contested), L1-M may need a deeper revision and could slip beyond W6.~~ ✅ **NOT REALIZED** — R-3 closed cleanly Day 1 as a clarification (not structural rework). G1 closed in Day 1 (not Day 4-5).
- ~~**G3 underestimation.** If the ε decision is "amend Commitment 16 to ε=0.225", the propagation is mechanical. If it's "keep Commitment 16 default and re-run scripts", the script time may be 2-3 days.~~ ✅ **NOT REALIZED** — D1 verdict was the diagnostic-first outcome (canonical intent = scripts use R1; ~30 min wording amendment).
- ~~**Parking-lot Stage 0 surprise.** The "17 files / 8,145 lines" cluster count is from W5 Day 5 narrative; the actual inventory may show drift (some files renamed, split, or duplicated).~~ ⚠️ **REALIZED** — actual count was **49 files / 17,269 lines** (~2.9× / 2.1× drift). Brief plan revision applied: §1 G4 status text updated; CV-1.7_PARKING_LOT_REVIEW_PLAN.md §2 cluster table audit-trail update added. Issue #1–#5 series caught additional drift (cluster F mis-classification of OAT-5/OAT-6 → re-examined).

## 7. What this plan deliberately does not commit to (status updated post W6 D1 EOD)

- ~~A specific CV-1.6 release date.~~ **REVISED:** W6 D7 EOD now active candidate per Decision Point 4 above; user decision required.
- ~~Promotion of L-M to canonical (only audit closure).~~ **REVISED:** L-M canonically promoted as supervised special-case W6 D1 EOD second addendum after external audit PASS; T-L1-M now in canonical.md §13 line 1491 + C-0722 row in theorem_status.md.
- **Parking-lot Stages 1-3** (the per-file critic dispatches). *(Status unchanged: Stage 1+ remains W7+ scope; Issue #1–#5 series acted as quasi-Stage-1 audits but full per-file Cat-header drafting deferred.)*
- **T-σ-Theorem-4 statement modification** (NQ-187 falsification handling deferred). *(Status: continuum-vs-discrete caveat applied W6 D1 evening per G2 commit; γ/β/α reconciliation still W7+ — no statement-level modification beyond the caveat.)*
- **W7+ scope.** *(Status unchanged.)*
- **Any cross-team / external dispatch this week.** *(Note: NQ-G1-3 external L-M-K-style audit was a single ~7-min general-purpose subagent dispatch, not a "cross-team" engagement; treated as part of G1 closure.)*

W6 is a closure week, not an expansion week. **Day 1 substantively absorbed Days 1–6 of the original plan; Day 2–7 has ~3-day slack for either consolidation, deferred numerical NQs, CV-1.6 release packet prep, or W7+ seed work.**

## 8. Comparison with the deleted W6 plan

| Item | Old W6 plan | This redesign |
|---|---|---|
| Goals | 8 (G1 L1-M-AUDIT, G2 NQ-L1M-2, G3 γ-path, G4 CV-1.6 release, G5 parking-lot dispatch, G6 L-M perturbation, G7 OAT-2/3, G8 NQ-244) | 4 (G1 L1-M-AUDIT, G2 T-Bind decision, G3 ε convention, G4 parking-lot inventory only) |
| Hours claimed | 62 (actual sums 75-144) | 35 (sums honestly) |
| Pillars | 3 (Multi-formation closure, σ-framework cleanup, Empirical anchoring) | 1 (Inconsistency closure for CV-1.5.2 baseline) |
| CV-1.6 release | Day 7 EOD target | Deferred |
| Parking lot | Day 6 Block 3 prompt skeletons only ("Full dispatch is optional") | Stage 0 inventory committed; Stages 1-3 explicitly W7+ |
| L-M promotion to canonical | Default Option A (L-M Cat A in CV-1.6) | Audit only; canonical merge separately scheduled |
| Decision points | 5 | 4 (sharper) |

End of plan.
