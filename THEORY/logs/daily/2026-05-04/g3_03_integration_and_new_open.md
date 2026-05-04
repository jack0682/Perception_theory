# 03_integration_and_new_open.md — G3 ε-Convention Integration + New Open Questions

**Session:** 2026-05-04 (W6 Day 1, mid-day)
**Target (from plan.md / `02_development.md` §5–§10):** Integrate the G3 ε-convention decision (R1 explicit reading of $\bar m = M / K_{\mathrm{field}}$) with the canonical structure; surface what changes / what stays the same; collect new open questions; record prompt v2 notes.
**This file covers:** §1 integration with canonical (Commitment 16 amendment); §2 integration with `theorem_status.md`; §3 integration with `T-L1-F` empirical claim; §4 integration with W6 strategic plan (misframing finding); §5 OP non-impact statement (recap); §6 new open questions surfaced; §7 prompt v2 candidate notes.
**Depends on reading:** `02_development.md` §1–§10 (full diagnostic + decision rule + propagation plan); `01_exploration.md` §1–§3 (problem framing + multi-approach + A4 selection rationale); `THEORY/canonical/canonical.md` line 810 (Commitment 16); `THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md` G3 (lines 49-58).

---

## §1. Integration with Canonical

### §1.1 Where G3 sits in the canonical structure

G3's outcome is a **Cat A definitional precision** to Commitment 16 (canonical.md §11.1 #16, line 810). It does not modify any theorem, axiom, or definition outside of clarifying the existing canonical default for the K_act support threshold ε.

If applied (per the user's promotion decision; this session does not write to canonical/), the canonical text would change at exactly **one sentence** (line 810). All other canonical content, theorem categories, OP statuses remain unchanged.

### §1.2 Proposed canonical amendment text (recap from `02_development.md` §6.1)

**Current text** (canonical.md line 810):

> for support threshold $\epsilon$ (default $\epsilon = 0.01 \cdot \bar{m}$, $\bar{m}$ per-formation expected mass).

**Proposed amended text:**

> for support threshold $\epsilon$ (default $\epsilon = 0.01 \cdot \bar{m}$, where $\bar{m} := M / K_{\mathrm{field}}$ is the **architectural per-formation mean** with $M$ the total system mass; for the standard $T^2_{20}$ multi-formation regime $M = 90, K_{\mathrm{field}} = 4$ this gives $\bar{m} = 22.5$ and $\epsilon = 0.225$, matching production-script default and L1-I empirical anchor).

**Important:** I am NOT applying this insertion. Per prompt §8.1, `canonical/*.md` writes are forbidden in this session. The above is a *proposal* for the user's promotion decision (analogous to W5 D7 §1.2 path-resolution policy for `02_L1M_proof_development.md`).

### §1.3 Why this placement (line 810, in-place edit)

- **No structural reorganization needed.** The existing Commitment 16 entry already has the "$\epsilon = 0.01 \cdot \bar m$" sentence; only its second clause (defining $\bar m$) is amended.
- **No release-version increment needed.** This is a documentation-precision amendment, not a theorem change. CV-1.5.2 release notes can be retained; an inline footnote or an entry in the next CHANGELOG (per `02_development.md` §7.3) suffices.
- **No theorem_status.md row change needed.** Commitment 16 is not a theorem entry there; only the CV-1.5.1 release notes mention it.

### §1.4 Existing canonical theorems: no relation impact

The §1.2 amendment does not interact with any other canonical theorem. Specifically:

- **T-L1-F** (line 1482-1489): empirical anchor "439/1920 FEASIBLE_WITH_BUDGET" was already implicitly at $\epsilon = 0.225$ via L1-I script default; the §1.2 amendment makes this explicit *upstream* (in Commitment 16) rather than requiring a downstream T-L1-F text edit.
- **All Cat A theorems**: unaffected; Commitment 16's K-status decomposition + threshold default are downstream of all single-field and multi-field theorem statements.

### §1.5 Future canonical interactions

If subsequent work (e.g., W7+ regime extensions to non-standard $M$ or $K_{\mathrm{field}}$, or the deferred γ/β/α reconciliation reactivating the σ-tuple ε-dependence) introduces a *different* $\epsilon$ default, the §1.2 amendment's R1 reading provides a **stable reference point** ($\bar m = M / K_{\mathrm{field}}$ is well-defined across all $M$, $K_{\mathrm{field}}$). Any new convention can be expressed as a perturbation of R1 rather than as a separate convention.

---

## §2. Integration with `theorem_status.md`

### §2.1 No theorem category change

The G3 decision changes no theorem categorization. Specifically:
- Commitment 16 itself is **not** indexed in the Theorem Registry (it is a Commitment Note in §11.1 of canonical.md, not a T-xxxx entry).
- T-L1-F (C-0721) Cat A status preserved.
- No active claim (C-xxxx) is modified.

### §2.2 Optional CV-1.5.1 release-notes footnote

The CV-1.5.1 release-notes section in `theorem_status.md` (around lines 76-83) mentions Commitment 16 as a new addition. An optional footnote can be added there:

> *(Erratum 2026-05-04 W6 D1 G3 audit: Commitment 16 K_act default ε convention clarified — $\bar m = M / K_{\mathrm{field}}$ is the architectural per-formation mean. Standard $T^2_{20}$ regime $M=90, K_{\mathrm{field}}=4 \Rightarrow \bar m = 22.5, \epsilon = 0.225$. See canonical.md line 810 amendment + CHANGELOG 2026-05-04 W6 D1 G3 entry.)*

This is purely cosmetic / for traceability; not required for the substantive G3 outcome.

### §2.3 Open Problems Catalog: no change

OP-0005 (K-Selection), OP-0008 (σ^A K-jump non-determinism), OP-0009 (Multi-Formation Ontological Foundations) all retain their HIGH severity. G3 does not partially or fully resolve any of them. (See `02_development.md` §10.3 for the full OP non-impact statement.)

---

## §3. Integration with T-L1-F Empirical Claim

### §3.1 No T-L1-F entry edit needed

`canonical.md` line 1489 (T-L1-F status):

> ... (numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$ ...

Under the §1.2 Commitment 16 amendment, the L1-I empirical claim is **automatically and consistently anchored** to the canonical ε default (which now explicitly equals 0.225 for the standard regime). No edit to T-L1-F line 1489 is needed.

### §3.2 Optional inline-cosmetic improvement

For maximum reader clarity, the parenthetical could be expanded to:

> ... (numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$ at $\epsilon = 0.01 \cdot M / K_{\mathrm{field}} = 0.225$ per Commitment 16 ...

Cosmetic only.

### §3.3 Stability of the "439/1920" claim under R1 reading

Under R1, the "439/1920 = 22.9% feasible" empirical claim is well-defined and reproducible:
- Inputs: $T^2_{20}$ ground graph, $M = 90$, $K_{\mathrm{field}} = 4$, $\epsilon = 0.225$, plus the L1-I sweep over $(σ_b, δ, r, \ell_{\min}, \text{geometry}, \text{state mode})$.
- Output: 439 of 1920 configurations satisfy LG-1, LG-2, LG-3, LG-4, tightened H6, L1-F ledger with margin ≥ 0.05.

If R3 or some other reading were adopted (which it is not), the empirical claim would need re-derivation under the new ε. R1 preserves the claim.

---

## §4. Integration with W6 Strategic Plan (Misframing Finding)

### §4.1 The W6 strategic plan G3 framing was based on a misreading

`THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md` G3 (lines 49-51) describes the discrepancy as:

> Production scripts (...) all use ε = 0.225 (~0.075·m̄ for K_field = 4). T-L1-F's "439/1920 = 22.9% feasible" empirical claim is for ε = 0.225, not Commitment 16's default.

The "(~0.075·m̄ for K_field = 4)" parenthetical implicitly assumes $\bar m \approx 3$ (since $0.225 / 0.075 = 3$). But under the only documented R1 reading, $\bar m = M / K_{\mathrm{field}} = 22.5$, and the script $\epsilon = 0.225 = 0.01 \cdot 22.5$ matches Commitment 16's "$\epsilon = 0.01 \cdot \bar m$" formula **exactly**. The strategic-plan author's "$\bar m \approx 3$" reading is **not supported by any source** (`02_development.md` §9.3 reverse-engineering check).

### §4.2 Recommended W6 strategic plan G3 update

The strategic plan G3 description should be revised to reflect this Day 1 finding. Proposed amendment to `W6_strategic_plan.md` G3 status text:

**Replace** (lines 49-52):

> **Status:** Commitment 16 (canonical) proposes default ε = 0.01·m̄. Production scripts (`l1g_l1hyp_diagnostic.py`, `l1i_constants_feasibility.py`, `wq_lat1_*.py`, `nq242c_*.py`) all use ε = 0.225 (~0.075·m̄ for K_field = 4). T-L1-F's "439/1920 = 22.9% feasible" empirical claim is for ε = 0.225, not Commitment 16's default.

**With** (R1 explicit framing):

> **Status:** Commitment 16 (canonical) proposes default ε = 0.01·m̄ where m̄ is "per-formation expected mass" (deliberately deferred at CV-1.5.1 per `K_status_commitment.md` line 313 to "NQ-242 W6 Day 1-3 numerical work"). Production scripts (`l1g_l1hyp_diagnostic.py`, `l1i_constants_feasibility.py`, `wq_lat1_*.py`, `nq242c_*.py`) all use ε = 0.225 with `nq242c` line 80 explicit comment `0.01 * (M / K_field) = 0.01 * 22.5` — i.e., scripts adopt R1 reading $\bar m = M / K_{\mathrm{field}}$. T-L1-F's "439/1920 = 22.9% feasible" empirical claim is for ε = 0.225, consistent with R1.
>
> **W6 D1 G3 finding** (`logs/daily/2026-05-04/02_development.md` §1-§10): D1 verdict — canonical intent ≈ scripts use R1; the "discrepancy" framing was based on an unsupported $\bar m \approx 3$ reading. **Resolution: minimal canonical wording amendment** to make R1 explicit; no script re-runs needed.

This is a **proposal for the user's edit** — this session does not write to weekly/ directly. (Note: weekly/ is conceptually similar to working/ in the promotion-pipeline pattern; the autonomous prompt §3 hard constraint applies symmetrically.)

### §4.3 G3 effort revision

Per `02_development.md` §6 and §7, the actual G3 effort is **~30 minutes** (read 4 scripts + 1 working file + 1 OAT-1 source; write 1-sentence canonical amendment + 1 CHANGELOG entry), **not 1-3 days** as the strategic plan §6.3 estimated. The Day 3 budget for G3 (per redesigned plan §3) is now mostly free.

### §4.4 Implication for Day 2-3 schedule

Per `plan.md` (redesigned) §6.2, Day 2 afternoon was scheduled to start G3 reading. Since G3 is now substantively closed by this Day 1 mid-day session:

- **Day 2 morning (Block 1, ~2 hours):** G1 textual repairs (unchanged from `plan.md` §6.1).
- **Day 2 afternoon Block 2 (was G3 reading) is now FREE.** Options:
  - (i) Apply the §1.2 canonical amendment + CHANGELOG entry (user-supervised, ~30 minutes).
  - (ii) Start G4 (parking-lot inventory, originally Day 6) — accelerate.
  - (iii) Catch up on W6 weekly_summary draft.
  - (iv) Optional: revisit deferred-track artifacts (cseh / γ-path / NQ-187b / OAT-2) for promotion candidacy *if* user reactivates any deferred goal. (Default: do not extend, per redesigned plan §5.)
- **Day 3-7 schedule:** unchanged, but with significant slack.

---

## §5. OP Non-Impact Statement (recap from `02_development.md` §10.3)

This G3 decision:
- Does **not** affect OP-0001 (F-1), OP-0002 (M-1), OP-0003 (MO-1) — orthogonal layer.
- Does **not** affect OP-0005 (K-Selection) — does not address the K mechanism; only the threshold for declaring a slot "active."
- Does **not** affect OP-0008 (σ^A K-jump non-determinism) — orthogonal.
- Does **not** affect OP-0009 (Multi-Formation Ontological Foundations) sub-items — Commitment 16 K-status decomposition unchanged; only the ε-default wording is clarified.
- Does **not** affect OP-0006, OP-0010, OP-0011, OP-0012, OP-0013 — unrelated layers.
- Does **not** affect N-1 (Soft-Hard Switching Asymmetry) reframing.

**No silent OP resolution.** All OP-xxxx severities preserved.

---

## §6. New Open Questions Surfaced

These are questions that G3 does *not* answer but became visible during its construction. Each is 3-5 lines, candidate for future plan.md targets.

### NQ-G3-1. Stability of "439/1920" under ε perturbation

**Question.** The L1-I "439/1920 = 22.9% feasible" empirical claim is computed at exactly $\epsilon = 0.225$. How does the FEASIBLE_WITH_BUDGET fraction change under ε perturbations? Specifically: what is the function $f(\epsilon) = |\{c \in \text{1920 configs} : c \in \text{FEASIBLE\_WITH\_BUDGET}(\epsilon)\}| / 1920$ for $\epsilon \in [0.01, 1.0]$?

**Severity.** Low-Medium. Practical informativeness: which ε values make the L1-J regime "robustly large" vs "marginally non-empty" vs "vacuous"?

**Connection.** Single re-run of `l1i_constants_feasibility.py` with a sweep over ε, ~1-2 hours compute. Result feeds into a future regime-tightening discussion.

### NQ-G3-2. Architectural mass conventions for non-standard regimes

**Question.** R1 ($\bar m = M / K_{\mathrm{field}}$) is well-defined for any $(M, K_{\mathrm{field}})$, but the canonical "for the standard $T^2_{20}$ regime $M = 90, K_{\mathrm{field}} = 4$" specifies one particular regime. What is the canonical default ε for **non-standard** regimes (e.g., $T^2_{32}, M = 200, K_{\mathrm{field}} = 8$)? The R1 formula would give $\epsilon = 0.25$ for that regime. Is this consistent with the L1-J regime hypothesis package (which itself is regime-dependent via $\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}}, \ldots$)?

**Severity.** Medium. Future-proofing for any W7+ multi-regime extensions.

**Connection.** Would require re-running L1-I-style feasibility at multiple regimes + analyzing whether the same L1-J hypotheses hold robustly. Could be a W7+ NQ.

### NQ-G3-3. K_act stability under ε perturbation at fixed state

**Question.** For a fixed multi-formation state $\mathbf{u}$, $K_{\mathrm{act}}^\epsilon(\mathbf{u})$ is monotone non-increasing in ε (raising the threshold can only deactivate slots). At what ε perturbation does $K_{\mathrm{act}}$ jump? Is this jump set "structural" (corresponding to genuine slot deactivation) or "noise-driven" (corresponding to slots near the threshold)?

**Severity.** Medium. Connects to OP-0008 (K-jump non-determinism) — if K_act jumps are sensitive to small ε perturbations, then K-jump events themselves may have ε-dependent structure.

**Connection.** A direct numerical experiment: take the L1-I FEASIBLE configurations + sweep ε ± 30% around 0.225 + measure K_act jump points. Could be a W7+ NQ.

### NQ-G3-4. Does the W6 strategic plan G3 misframing pattern indicate a broader documentation drift?

**Question.** The W6 strategic plan G3 was written 2026-05-04 morning by the same author as `K_status_commitment.md` (presumably the user, based on session pattern). The strategic plan adopted a different reading of $\bar m$ than the source. This suggests the original author themselves had drift between writing `K_status_commitment.md` (W5 D3 EOD) and writing `W6_strategic_plan.md` (W6 D1 morning) — about a week apart. Are there other documentation-drift cases like this within the W4-W6 timeframe that haven't been caught?

**Severity.** Medium. Meta-question about audit hygiene; may motivate a broader audit pass.

**Connection.** Would require systematic cross-checking of canonical / working / strategic-plan files for similar provisional-default vs implemented-default mismatches. Could be folded into the W6 G4 parking-lot inventory work.

### NQ-G3-5. Should ε also be a regime parameter in T-L1-F's $(P0)$–$(P11)$?

**Question.** T-L1-F's hypothesis package $(P0)$–$(P11)$ includes regime constants ($\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}}, \ldots$) but does **not** include ε explicitly. ε appears only via the K_act definition in Commitment 16 (used through P2 "active mass + connected $\delta$-support" indirectly). Should ε be added as $(P12)$ to the L1-J regime package, with its own range constraint (e.g., $0 < \epsilon < c \cdot \bar m$ for some safety constant $c$)?

**Severity.** Low. Cosmetic / regime-completeness question.

**Connection.** Would require re-deriving the T-L1-F proof to identify where ε's specific value matters (likely only in P2's "active mass" definition). If ε appears only in one place, it may be cleaner to leave it in Commitment 16 rather than promote to (P12).

### NQ-G3-6. Cross-ε consistency between K_act and $K_{\mathrm{soft}}^\phi$ (for L-M)

**Question.** L-M corollary (per `logs/daily/2026-05-03/02_L1M_proof_development.md`) bounds $|K_{\mathrm{soft}}^\phi(U) - K_{\mathrm{act}}^\epsilon(\mathbf{u})|$ for $\phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau)$. The bound depends on $\ell_{\min}$ (envelope threshold) and $\epsilon$ (K_act threshold). Are these two thresholds independently tunable, or is there a natural coupling (e.g., $\ell_{\min} = c_1 \cdot \epsilon$)?

**Severity.** Low-Medium. Connects to L-M's working-file structure; not blocking.

**Connection.** Would require reading `working/MF/ksoft_kact_bridge_lemma.md` and the L-M working draft for any explicit $\ell_{\min}$ vs $\epsilon$ relationship. Could be a W7+ NQ when L-M canonical promotion is pursued.

---

## §7. Prompt v2 Candidate Notes (per prompt §14)

The autonomous-execution prompt is intended as a reusable template. The following observations from this session may inform a future v2:

### §7.1 Plan-vs-strategic-plan misalignment detection

This session encountered a structural misalignment between `plan.md` (daily, original 8-goal version) and `W6_strategic_plan.md` (weekly, redesigned 4-goal version), and earlier also between `W6_strategic_plan.md` G3 framing and the actual canonical / script convention. A future v2 might add: "Before executing plan.md, verify alignment with the most recent weekly strategic plan; flag any goals in plan.md that do not appear in the strategic plan, and any goals in the strategic plan that appear absent from plan.md."

### §7.2 Diagnostic-first as a meta-pattern

Approach **A4 (Diagnostic-First)** in `01_exploration.md` §2.4 is a useful meta-pattern for any session where the question's *premise* is itself uncertain (e.g., "what does this term mean?" before "which value should it have?"). A future v2 might explicitly suggest A4 when the multi-approach generation reveals that all alternatives (A1, A2, A3, ...) presuppose a particular reading of a key term.

### §7.3 Misframing flags

This session caught a "documentation drift" — the W6 strategic plan G3's "$\bar m \approx 3$" framing was unsupported by sources. A future v2 might recommend that diagnostic sessions explicitly check the strategic-plan / plan.md framing against source-of-truth files, and flag any unsupported implicit assumptions.

### §7.4 Effort estimate validation

The strategic plan G3 estimated 1-3 days; the actual diagnostic-first execution took ~30 minutes of read + ~2 hours of write. A future v2 might suggest: "When executing a planned goal, if the actual effort is dramatically lower than the planned estimate, flag this in `99_summary.md` so the user can recalibrate future estimates."

### §7.5 Single-topic deep-dive vs multi-thread coordination tension

The autonomous prompt template is structured for "single open problem deep-dive" with `01_exploration.md` (multi-approach) → `02_development.md` (primary deep-dive) → `03_integration_and_new_open.md` (integration + NQs). This session fits the template well because G3 is genuinely a single open question with multiple decision rules. But the redesigned W6 plan has 4 parallel goals (G1-G4), and earlier sessions on multi-goal plans (e.g., W5 D7 with 5 goals) struggled to fit the template. A future v2 might offer two modes:
- **Single-goal deep-dive mode** (current template): produces 01/02/03/99.
- **Multi-goal coordination mode**: produces N goal-specific files + 99_summary.

---

**End of `03_integration_and_new_open.md`.**

**Next file:** `99_summary.md` — session summary + tomorrow seed.
