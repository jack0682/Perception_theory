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

**Status:** L-M draft is at `THEORY/working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` (Cat-B sketched). Three audit items are flagged in §5.7 of that file:
- R-1: bottleneck-stability factor sharpness.
- R-2: Type-B bound LG-7 reuse explicit reproof.
- R-3: Type-N terminal-death convention.

The 2026-05-04 deep audit flagged R-3 as potentially structural (not bookkeeping): the comparison between $U|_{G_j^r}$ and $u^{(j)}|_{G_j^r}$ uses local-graph terminal-death, which is a different convention than global terminal-death; the proof currently invokes L1-H2 Lemma 1 to bridge them, but the invocation itself is conditional on an uncontested reading of L1-H2.

**Deliverable:** L-M-2 Cat-B sketched -> Cat-A conditional via explicit closure of R-1/R-2/R-3, OR a deliberate retention at Cat-B with an explicit failure analysis.

**Estimated effort:** 3-4 days.
**Priority:** P0 (must).

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

**Status:** 17 unaudited working files (~8,145 lines) introduced during W5 Day 4 Wave 3 burst. Plan exists at `THEORY/working/CV-1.7_PARKING_LOT_REVIEW_PLAN.md`. Stage 0 produces an inventory file that lists every parking-lot file with metadata.

**Deliverable:** `THEORY/working/CV-1.7_parking_lot_inventory.md` with all 17 (or actual count) files enumerated. Per-file critic dispatch (Stage 2) is **out of scope for W6** — that is the W7+ workstream.

**Estimated effort:** 1 day.
**Priority:** P1 (should).

## 2. Explicit non-goals for W6

Things deliberately NOT attempted this week:

- **CV-1.6 release.** Previous W6 plan targeted Day 7 EOD release. This redesign treats CV-1.6 as deferred until G1+G2+G3 close. There is no reason to push a release with documented Cat-A miscounts and ε ambiguity.
- **T-σ-Theorem-4 γ-path audit.** Was G3 in old plan. Deferred; per 2026-05-04 user decision, the NQ-187 falsification handling is to be revisited later.
- **L1-M canonical promotion.** L1-M-AUDIT (G1 above) is the prerequisite. Even if G1 closes cleanly to Cat-A conditional, the actual canonical merge is a CV-1.6 release activity, not a W6 commit.
- **OAT-2 / OAT-3 short integration.** Was G7 in old plan. Deferred — not blocking anything this week.
- **NQ-244 3D LSW analysis.** Was G8 in old plan. Background script not confirmed launched (audit found ambiguous launch status). Deferred until launch is verified.
- **Wave 3 parking-lot critic dispatch (Stage 2).** Was G5 in old plan. Per the parking-lot plan, this is W7+ work; W6 only does Stage 0.
- **σ-rich CODE work** (centroid_trajectory.py, vr_persistence.py, k_jump_detector.py mentioned in working files but not in scc/). Out of scope.

## 3. Daily breakdown

The below is a target shape, not a rigid schedule. Substantive work (G1, G2, G3) is sequential because each requires reading the same canonical body and would interfere if parallel.

| Day | Date | Focus | Hours (target) | Deliverable |
|-----|------|-------|----------------|-------------|
| Day 1 | 2026-05-04 (Mon, today) | Audit pass 2 closure (already done; CHANGELOG written) + W6 plan (this file) + start G2 reading | 4 | 2026-05-04 audit-pass-2 entry in CHANGELOG; this plan; G2 audit reading begun |
| Day 2 | 2026-05-05 (Tue) | G2 finish: T-Bind-Proj/Full category decision + canonical/theorem_status sync | 6 | G2 closed. Net Cat A count update (likely +1 or unchanged depending on decision) propagated to §13, §15, theorem_status. |
| Day 3 | 2026-05-06 (Wed) | G3 in full: ε-convention decision + script audit + working file sync | 6 | G3 closed. Single ε convention documented. T-L1-F empirical claim re-anchored to chosen ε. |
| Day 4 | 2026-05-07 (Thu) | G1 part 1: R-1 (bottleneck factor sharpness) closure + R-2 (Type-B LG-7 reuse) explicit reproof | 6 | R-1 closed; R-2 closed. R-3 deferred to Day 5. |
| Day 5 | 2026-05-08 (Fri) | G1 part 2: R-3 (Type-N terminal-death) closure attempt + Cat-A conditional decision | 6 | R-3 either closed (L-M-2 -> Cat-A conditional) or deliberately retained at Cat-B (failure analysis). |
| Day 6 | 2026-05-09 (Sat) | G4: parking-lot inventory file produced | 4 | `CV-1.7_parking_lot_inventory.md` complete with 17 files enumerated and metadata populated. |
| Day 7 | 2026-05-10 (Sun) | W6 close: weekly_summary.md draft + W7 seed | 3 | `THEORY/logs/weekly/2026-05-W1/weekly_summary.md` describing what was closed and what remains. |

**Total target hours: 35** (vs old plan's claimed-62 / actual-75-144).

## 4. Success criteria

- **Bronze (minimum):** G2 closed (T-Bind decision applied); G3 closed (ε convention chosen); audit-pass-2 entry in CHANGELOG (already done). G1 and G4 may slip.
- **Silver (default target):** Bronze + G1 closed (R-1/R-2/R-3 resolved one way or the other); G4 inventory produced.
- **Gold (stretch):** Silver + G4 first-cluster (Reconciliation drafts) critic dispatch completed (carries Stage 1 of parking-lot plan into W6).

## 5. Decision points

These need user input or explicit deferral by W6 close, otherwise they become silent drift.

1. **Day 2 EOD:** T-Bind-Proj / T-Bind-Full category decision (Cat A or Cat B/C). Affects §15 closing-summary count.
2. **Day 3 EOD:** ε convention decision (Commitment 16 default vs script default). Affects T-L1-F empirical regime.
3. **Day 5 EOD:** if R-3 cannot be closed, decide whether L-M is retained at Cat-B sketched (working) or formally moved to Cat C / retracted.
4. **Day 7 EOD (W6 close):** decision on whether CV-1.6 release becomes a W7 target or is deferred indefinitely. Default: deferred until parking lot is at least partially resolved.

## 6. Risks

- **G1 slip into G2/G3 territory.** If R-3 turns out to require substantial rework (likely if L1-H2 Lemma 1 itself is contested), L1-M may need a deeper revision and could slip beyond W6.
- **G3 underestimation.** If the ε decision is "amend Commitment 16 to ε=0.225", the propagation is mechanical. If it's "keep Commitment 16 default and re-run scripts", the script time may be 2-3 days.
- **Parking-lot Stage 0 surprise.** The "17 files / 8,145 lines" cluster count is from W5 Day 5 narrative; the actual inventory may show drift (some files renamed, split, or duplicated). If the count is materially different, a brief plan revision is needed.

## 7. What this plan deliberately does not commit to

- A specific CV-1.6 release date.
- Promotion of L-M to canonical (only audit closure).
- Parking-lot Stages 1-3 (the per-file critic dispatches).
- T-σ-Theorem-4 statement modification (NQ-187 falsification handling deferred).
- W7+ scope.
- Any cross-team / external dispatch this week.

W6 is a closure week, not an expansion week.

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
