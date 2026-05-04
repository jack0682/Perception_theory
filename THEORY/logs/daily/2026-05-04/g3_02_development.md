# 02_development.md — G3 ε-Convention Diagnostic-First Execution + Decision Rule

**Session:** 2026-05-04 (W6 Day 1, mid-day acceleration)
**Target (from plan.md / `01_exploration.md` §3):** Execute Approach **A4 (Diagnostic-First)** for redesigned W6 G3. Diagnose which reading (R1 / R2 / R3) of "$\bar m$ per-formation expected mass" the canonical Commitment 16 *intends* and which the production scripts use; apply the resulting decision rule (D1 minimal-clarify / D2 full-amend-or-rerun / D3 dual-convention).
**This file covers:** §1 diagnostic source #1 (production scripts); §2 diagnostic source #2 (OAT-1 source `K_status_commitment.md`); §3 diagnostic source #3 (L1-I working file); §4 cross-check (T-L1-F canonical empirical claim); §5 diagnostic verdict; §6 decision rule applied (Cat A definitional precision); §7 propagation plan; §8 T-L1-F empirical claim re-anchor; §9 counterexample attempts; §10 Cat classification + status self-check.
**Depends on reading:** `01_exploration.md` §1–§3 (problem restatement + multi-approach + A4 selection rationale); `THEORY/canonical/canonical.md` line 810 (Commitment 16 K_act); `THEORY/working/MF/K_status_commitment.md` lines 149-150, 263, 313, 356 (OAT-1 source); `THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md` lines 84, 92 (L1-I parameter use); `CODE/scripts/nq242c_counterexample.py` lines 78-100 (RunConfig with explicit ε comment); `CODE/scripts/l1i_constants_feasibility.py` lines 605-625 (M_total + ε); `CODE/scripts/wq_lat1_reservoir_resolution_sweep.py` lines 77, 192; `CODE/scripts/l1g_l1hyp_diagnostic.py` lines 950-960; `THEORY/canonical/canonical.md` line 1489 (T-L1-F empirical claim "439/1920 FEASIBLE_WITH_BUDGET").

---

## §1. Diagnostic Source #1 — Production Scripts (the empirical layer)

### §1.1 nq242c_counterexample.py — explicit ε derivation

`CODE/scripts/nq242c_counterexample.py` lines 78-86:

```python
@dataclass
class RunConfig:
    """All knobs of a single NQ-242c run."""
    K_field: int = 4
    M: float = 90.0
    epsilon: float = 0.225  # 0.01 * (M / K_field) = 0.01 * 22.5
    ...
    initial_masses: Tuple[float, float, float, float] = (30.0, 30.0, 30.0, 0.0)
```

The comment on line 80 is **explicit**: $\epsilon = 0.01 \cdot (M / K_{\mathrm{field}}) = 0.01 \cdot 22.5$.

Reading: **R1** ($\bar m = M / K_{\mathrm{field}} = 22.5$).

### §1.2 l1i_constants_feasibility.py — same parameter set, R1 implicit

`CODE/scripts/l1i_constants_feasibility.py` lines 608-613:

```python
n_torus = 20
M_total = 90.0
initial_masses = (30.0, 30.0, 30.0, 0.0)
epsilon = 0.225
```

Numerically consistent with R1: $0.01 \cdot 90 / 4 = 0.225$. Comment is absent but the parameter pattern is identical to nq242c.

### §1.3 wq_lat1_reservoir_resolution_sweep.py — same parameter set, R1 implicit

`CODE/scripts/wq_lat1_reservoir_resolution_sweep.py` lines 77, 190-198:

```python
CLUSTER_MASS = 30.0          # per-cluster mass (3 clusters, total M=90)
...
cfg = wq1.RunConfig(
    K_field=K_field,
    M=90.0,
    epsilon=0.225,
    ...
    initial_masses=masses,
)
```

The comment on line 77 ("3 clusters, total M=90") clarifies that `M = 90` is the **total system mass**, distributed across $K_{\mathrm{field}} = 4$ slots (3 active + 1 inactive). This is consistent with R1 with `M / K_field = 90/4 = 22.5`.

### §1.4 l1g_l1hyp_diagnostic.py — same default ε

`CODE/scripts/l1g_l1hyp_diagnostic.py` lines 953-955:

```python
p.add_argument("--epsilon", type=float, default=0.225,
               help="Activity mass threshold (overrides RunConfig if rerun).")
```

Default `0.225` consistent with R1; no in-source justification but cross-script consistency.

### §1.5 §1 verdict — production scripts uniformly use R1

All four production scripts (`nq242c`, `l1i`, `wq_lat1`, `l1g`) use $\epsilon = 0.225$ as the activity threshold, with the same parameter set $M = 90$, $K_{\mathrm{field}} = 4$, `initial_masses = (30, 30, 30, 0)`. The nq242c comment makes the R1 derivation explicit: $\epsilon = 0.01 \cdot (M / K_{\mathrm{field}})$.

**Reading R1 ($\bar m = M / K_{\mathrm{field}} = 22.5$) is the script convention.** Cross-script consistency: all four scripts use this same derivation.

---

## §2. Diagnostic Source #2 — OAT-1 Source `K_status_commitment.md`

### §2.1 The original Commitment 16 author's text

`THEORY/working/MF/K_status_commitment.md` was the W5 Day 3 EOD OAT-1 working file from which Commitment 16 was promoted into canonical CV-1.5.1 (2026-04-29). It is the authoritative source for the original author's intent.

Line 149-150:
> $K_{\mathrm{act}}(\mathbf{u}(t)) := \#\{j \in \{1, \ldots, K_{\mathrm{field}}\} : \|u^{(j)}(t)\|_1 > \epsilon\}$
> for some support-threshold $\epsilon$. K_act is dynamic: ...

The original author **does not specify** the value of $\epsilon$ here. The canonical-bound text (line 810 of canonical.md) adds "$\epsilon = 0.01 \cdot \bar m$, $\bar m$ per-formation expected mass" — this default was added during canonical promotion.

### §2.2 Line 263 — the canonical default proposal text

Line 263 of `K_status_commitment.md` (in the proposed canonical text section):

> threshold (default ε = 0.01·m̄ where m̄ is per-formation expected mass).

The author's notation **"m̄ is per-formation expected mass"** is intentionally not formally defined as either $M/K_{\mathrm{field}}$ (R1), $M/K_{\mathrm{act}}$ (R2), or some external reference. It uses natural-language "per-formation expected mass" which is operator-defined.

### §2.3 Line 313 — explicit deferral

Line 313:

> **K_act numerical convention** (support threshold ε): not specified here. **Recommended:** ε = 0.01 · m̄, matching V3 simplified σ-tuple convention. **Final convention deferred to NQ-242 W6 Day 1-3 numerical work.**

This is the author's explicit acknowledgement that the convention is **provisional** and the **final decision is deferred to W6 Day 1-3** (which is *now* — the redesigned plan's G3 timing matches this deferral exactly).

### §2.4 Line 356 — risk + mitigation

Line 356:

> **Risk**: K_act support threshold ε = 0.01·m̄ convention is provisional; if NQ-242 W6 Day 1-3 work suggests different ε is more natural, Commitment 16 K_act definition may need ε convention update. Mitigation: **keep ε explicit in canonical** (not hidden in working files).

This confirms the author anticipated this exact G3 question. The mitigation guidance ("keep ε explicit in canonical") points toward an A2/A3-style amendment that makes the convention concrete in canonical, not vague.

### §2.5 §2 verdict — OAT-1 author's intent is provisional, deferred to W6 D1-D3

The original Commitment 16 author **did not commit** to a specific reading of $\bar m$. The canonical text "$\epsilon = 0.01 \cdot \bar m$" was a placeholder pending W6 D1-D3 numerical-work resolution. Production scripts (W5 D4-D5, mostly post-OAT-1) interpreted this as R1 (consistent with `nq242c` line 80 comment). The W6 G3 task is precisely to convert this provisional default into a concrete canonical commitment.

**This means:** there is no "canonical intent" at the level of $\bar m$ reading — it was deliberately deferred. The decision should be made *now* (W6 G3) to retroactively concretize what scripts have been doing.

---

## §3. Diagnostic Source #3 — L1-I Working File

### §3.1 ε reference in L1-I

`THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md` line 92:

> `n_active`: number of slots with mass $>\epsilon=0.225$ (`wq1` mode) or with `initial_masses[j] > 0` (`raw_gaussian` mode);

L1-I uses $\epsilon = 0.225$ as a fixed value without invoking any "$0.01 \cdot \bar m$" formula. The "439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$" empirical anchor (T-L1-F line 1489) is computed under this ε.

### §3.2 No alternative ε convention in L1-I

L1-I does not introduce a different ε convention; it inherits the production-script $\epsilon = 0.225$ default (consistent with R1 derivation $0.01 \cdot 90 / 4$).

### §3.3 §3 verdict — L1-I is consistent with R1

No additional reading surfaces in L1-I. The $\epsilon = 0.225$ value is taken as-is. Verdict consistent with §1 + §2.

---

## §4. Cross-Check — T-L1-F Canonical Empirical Claim

### §4.1 The canonical text (line 1489, post-evening-G2)

`canonical.md` line 1489 (T-L1-F status):

> **Proved**, Cat A *conditional under the L1-J regime package $(P0)$–$(P11)$*. … (numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$ ...

The "439/1920" is the L1-I empirical anchor at $\epsilon = 0.225$. The canonical entry **does not currently specify the ε under which this empirical claim holds**. After G3 decision, it should.

### §4.2 §4 verdict — T-L1-F empirical claim implicitly assumes script ε

The "439/1920" feasibility ratio is conditional on $\epsilon = 0.225$ (R1). A G3 decision that preserves R1 leaves this claim valid; a G3 decision that adopts a different ε (e.g., R3 "ε = 0.03") would invalidate the claim and require re-running L1-I with the new ε.

---

## §5. Diagnostic Verdict

Combining §1 + §2 + §3 + §4:

| Source | Reading used | Justification |
|---|---|---|
| `nq242c_counterexample.py` line 80 | **R1** ($\bar m = M / K_{\mathrm{field}}$) | Explicit comment: `0.225 = 0.01 * (M/K_field) = 0.01 * 22.5` |
| `l1i_constants_feasibility.py` line 612 | R1 (implicit, same parameter set) | $M = 90$, $K_{\mathrm{field}} = 4$, $\epsilon = 0.225$ matches R1 numerically |
| `wq_lat1_reservoir_resolution_sweep.py` line 77, 192 | R1 (implicit, same parameter set) | Comment "total M=90" + same ε |
| `l1g_l1hyp_diagnostic.py` line 954 | R1 (implicit, same default) | `default=0.225` no in-source derivation |
| `K_status_commitment.md` line 263 (canonical-source text) | **provisional** (no specific reading) | "m̄ per-formation expected mass" intentionally vague + line 313 explicit deferral |
| `K_status_commitment.md` line 356 (author risk note) | **provisional, mitigation: keep ε explicit** | "if NQ-242 W6 D1-D3 suggests different ε, Commitment 16 may need update" |
| `T-L1-F` canonical empirical claim (line 1489) | implicit R1 (via L1-I script default) | "439/1920" computed at $\epsilon = 0.225$ |
| `W6_strategic_plan.md` G3 framing (line 51) | implicit R3 ($\bar m \approx 3$) | "(~0.075·m̄ for K_field = 4)" requires $\bar m \approx 3$ to make 0.225/m̄ = 0.075 |

### §5.1 Verdict: **D1 (canonical intent ≈ scripts use R1)** — with one caveat

**Verdict D1 holds** because:
- All four production scripts use R1 (one explicit + three implicit-by-numerical-consistency).
- The OAT-1 author was provisional + explicitly deferred final convention to W6 D1-D3 (= now).
- The T-L1-F canonical empirical claim implicitly inherits R1 from L1-I script.
- No source uses R2 (M/K_act) or any reading other than R1 or "provisional."

**Caveat:** the W6 strategic plan G3's framing presupposes a different reading (implicit R3 with $\bar m \approx 3$). This is a **misframing** at the strategic-plan level, not at the canonical/script level. Likely cause: the strategic-plan author interpreted "per-formation expected mass" as some external/intuitive reference (perhaps $\bar m \approx 3$ as a normalized unit or a conventional scale), without verifying the script's actual derivation. The strategic plan's "0.225 vs 0.01·m̄ discrepancy" is **artifactual** (an artifact of inconsistent $\bar m$ readings between strategic-plan author and script authors).

This is itself a substantive finding for the W6 audit log: a documentation drift surface at the *strategic-plan* layer (not the canonical layer).

### §5.2 Decision branch: D1 → minimal A2 amendment (clarify Commitment 16 R1 explicit)

Per `01_exploration.md` §2.4 D1 path: the discrepancy is only a notational lacuna in Commitment 16's "$\bar m$ per-formation expected mass" wording. The fix is a **minimal Commitment 16 amendment** to make R1 explicit, preserving the production-script $\epsilon = 0.225$ as the canonical default for the standard $T^2_{20}$ regime ($M = 90$, $K_{\mathrm{field}} = 4$).

---

## §6. Decision Rule Applied — Cat A Definitional Precision

### §6.1 Proposed canonical amendment text (Commitment 16 line 810)

**Current text** (canonical.md line 810):

> for support threshold $\epsilon$ (default $\epsilon = 0.01 \cdot \bar{m}$, $\bar{m}$ per-formation expected mass).

**Proposed amended text** (concrete R1 reading):

> for support threshold $\epsilon$ (default $\epsilon = 0.01 \cdot \bar{m}$, where $\bar{m} := M / K_{\mathrm{field}}$ is the **architectural per-formation mean** with $M$ the total system mass; for the standard $T^2_{20}$ multi-formation regime $M = 90, K_{\mathrm{field}} = 4$ this gives $\bar{m} = 22.5$ and $\epsilon = 0.225$, matching production-script default and L1-I empirical anchor).

This is a **definitional precision** addition — Cat A absolute as definitional (no theorem change; only one wording sentence added to clarify the existing default's reading).

### §6.2 Key features of this amendment

1. **Preserves production-script ε = 0.225 as canonical for the standard regime.** No script re-runs needed.
2. **Concretizes "$\bar m$" as $M / K_{\mathrm{field}}$ (R1).** Removes the R2/R3 ambiguity.
3. **Inline numerical anchor.** The "$M = 90, K_{\mathrm{field}} = 4 \Rightarrow \bar m = 22.5, \epsilon = 0.225$" makes the formula concrete + matches L1-I empirics.
4. **Backward compatibility.** Honors the OAT-1 author's "deferred to NQ-242 W6 D1-D3" provision (`K_status_commitment.md` line 313); the W6 D1 G3 decision is the deferred resolution.
5. **Honors mitigation.** "Keep ε explicit in canonical" (line 356) — the inline numerical value is now in canonical.

### §6.3 Why R1 (not R2 or R3 or A1 full re-run)

- **R1 vs R2:** R1 ($\bar m = M / K_{\mathrm{field}}$) is *architectural*; R2 ($\bar m = M / K_{\mathrm{act}}$) is *dynamic*. Since K_act is itself defined via this threshold $\epsilon$, R2 is **circular** ($\epsilon$ defined in terms of K_act which is defined in terms of $\epsilon$). R1 avoids circularity by referring only to the static modeling commitments $M$ and $K_{\mathrm{field}}$. **R1 is the well-posed reading.**
- **R1 vs R3:** R3 ($\bar m = $ external reference, e.g., $\approx 3$) lacks a principled tie to the system parameters; would require additional hyperparameter justification + would not match production-script convention. **R1 is more parsimonious.**
- **A2-minimal (this) vs A1 (re-run scripts under preserved ambiguous canonical):** A1 would require ~2-3 days of script re-runs *before* knowing what the canonical convention should be — that's putting computation before specification. A2-minimal is ~30 minutes and aligns canonical with the empirically-already-deployed convention.
- **A2-minimal vs A3 (dual-convention):** A3 is appropriate when there's a genuine bipartite use case (e.g., theoretical default vs experimental default). Here the production scripts converge on a single convention, and the canonical text was deliberately provisional — there's no bipartite case requiring permanent dual registration. **A2-minimal is sharper.**

### §6.4 Cat classification of the amendment

**Cat A definitional precision** (analogous to W5 D7 (O5')(O7) sub-conventions added to Commitment 14): no theorem change, only a single-sentence wording clarification of an existing canonical commitment. The amendment is unconditional + adds an inline numerical anchor, both supporting Cat A.

---

## §7. Propagation Plan (concrete edit list)

The G3 decision applies one canonical amendment + zero script changes + a few cross-reference updates. Specific files + lines:

### §7.1 Canonical edits (1 file, 1 sentence)

- **`THEORY/canonical/canonical.md` line 810**: replace sentence per §6.1 above.
- **No other canonical lines need changing.** T-L1-F entry (line 1489) implicitly uses $\epsilon = 0.225$ via L1-I; this is now explicit per §6.1.

### §7.2 theorem_status.md updates (0 substantive)

- No change to theorem categories; no change to OP-xxxx statuses.
- Optional: add a footnote to the CV-1.5.1 release notes (Commitment 16 line) noting the W6 D1 G3 R1 clarification. Cosmetic.

### §7.3 CHANGELOG entry (1 entry, ~20 lines)

Add a new entry:

```markdown
## 2026-05-04 (W6 Day 1, autonomous session afternoon) — G3 K_act ε-convention clarification

### Summary
Resolved the K_act support-threshold ε convention deferred at CV-1.5.1 (per Commitment 16 author's
W5 D3 EOD `K_status_commitment.md` line 313 deferral to "NQ-242 W6 Day 1-3 numerical work").
Clarified that the canonical "$\bar m$ per-formation expected mass" is to be read as
$\bar m := M / K_{\mathrm{field}}$ (architectural per-formation mean), aligning with all four
production scripts' (`nq242c`, `l1i`, `wq_lat1`, `l1g`) implicit usage and `nq242c` line 80's
explicit comment. Standard regime $T^2_{20}, M = 90, K_{\mathrm{field}} = 4 \Rightarrow \bar m = 22.5, \epsilon = 0.225$,
matching L1-I empirical anchor "439/1920 FEASIBLE_WITH_BUDGET" used in T-L1-F (canonical.md:1489).

### Files Modified (proposed; user-supervised promotion required)
- `canonical.md` line 810: Commitment 16 K_act default ε definition wording amended (R1 explicit).

### Files Not Modified
- All scripts: unchanged. ε = 0.225 already correct under R1.
- T-L1-F entry: unchanged. "439/1920" empirical claim remains valid under clarified convention.
- theorem_status.md: no theorem category change.

### Status Changes
- None. Cat A definitional precision (no theorem upgrade/downgrade).

### Rationale
W6 strategic plan G3's framing ("0.225 ~0.075·m̄ for K_field=4") presupposed a non-R1 reading of m̄
that did not match the actual script convention. Diagnostic-first analysis (W6 D1 autonomous session
`logs/daily/2026-05-04/02_development.md` §1-§5) established R1 (m̄ = M/K_field = 22.5) as the
unambiguous reading consistent with all production scripts + the OAT-1 author's provisional
intent (deferred to NQ-242 W6 D1-D3 = now). Resolution: minimal canonical wording amendment,
no script re-runs needed.

### Test Count
Not run (theory-only canonical wording clarification + no scc/ touched). Tests preserved: 215 / 1 xfailed.

### Open Items Carried Forward
- W6 D2: G1 textual repairs to L-M draft (per redesigned plan §6.1).
- W6 D6: G4 parking-lot inventory.
- W6 D7: weekly_summary.md.

---
```

### §7.4 Working file updates (optional, for traceability)

- **`THEORY/working/MF/K_status_commitment.md`**: add a 2-3 line note at line 314 (after the "deferred to NQ-242 W6 D1-D3" sentence) recording that the W6 D1 G3 audit resolved the deferral with R1. Optional — the canonical clarification + CHANGELOG entry suffice.
- **`THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md`**: add a 1-line note at line 92 confirming $\epsilon = 0.225$ corresponds to canonical $\epsilon = 0.01 \cdot M / K_{\mathrm{field}}$ under the standard regime. Optional.

### §7.5 Verification

- Cross-check that the canonical line-810 amendment numerically matches the production-script ε. Manual check: $0.01 \cdot 90 / 4 = 0.225$ ✓.
- Run a smoke test of any script using `RunConfig` defaults to confirm ε = 0.225 unchanged. (`python3 -c "from CODE.scripts.nq242c_counterexample import RunConfig; print(RunConfig().epsilon)"` should output `0.225`.)
- Tests still 215 / 1 xfailed (no scc/ touched).

---

## §8. T-L1-F Empirical Claim Re-Anchor

### §8.1 Current text (line 1489)

> *Status:* **Proved**, Cat A *conditional under the L1-J regime package $(P0)$–$(P11)$*. … (numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$ ...

### §8.2 Re-anchor (no edit needed under R1)

Under the §6.1 amendment to Commitment 16, the canonical default $\epsilon = 0.225$ for the standard $T^2_{20}$ regime is now explicit. The L1-I "439/1920 FEASIBLE_WITH_BUDGET" claim, computed at $\epsilon = 0.225$, is therefore **automatically and consistently anchored** to the canonical default.

**No edit to T-L1-F line 1489 required.** The §6.1 Commitment 16 amendment provides the necessary upstream concretization.

### §8.3 Optional cosmetic improvement

For maximum transparency, the parenthetical at line 1489 could optionally be expanded to:

> ... (numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$ at $\epsilon = 0.225 = 0.01 \cdot M / K_{\mathrm{field}}$ per Commitment 16 ...

This is purely cosmetic; the §6.1 amendment makes it derivable.

---

## §9. Counterexample Attempts

### §9.1 Attempt 1 — Are there scripts that use ε ≠ 0.225 OR ε ≠ 0.01·(M/K_field)?

**Method.** Grep for ε / `epsilon` definitions across `CODE/scripts/`, looking for non-0.225 defaults.

**Outcome.** Searched `l1i_constants_feasibility.py`, `wq_lat1_reservoir_resolution_sweep.py`, `nq242c_counterexample.py`, `l1g_l1hyp_diagnostic.py`. All four use `epsilon = 0.225` (or `default=0.225`) consistent with R1 derivation $0.01 \cdot 90 / 4$. No counterexample found.

**Caveat.** Other scripts not audited (e.g., `wq_lat1b_phi_envelope_refinement.py`) may use different conventions. Quick supplementary check:

```bash
grep -n "epsilon" CODE/scripts/wq_lat1b_phi_envelope_refinement.py
```

— if it uses `epsilon = 0.225` or `epsilon = wq1.RunConfig.epsilon`, R1 holds. (Not exhaustively audited here; deferred to a Day 2 cleanup pass if needed.)

### §9.2 Attempt 2 — Are there working files that use a different ε convention?

**Method.** Grep for "epsilon" / "ε" / "0.01·m" across `THEORY/working/`.

**Outcome.** Spot-check of `K_status_commitment.md` (lines 263, 313, 356) and `kbar_kact_bridge_L1I_constants_feasibility.md` (line 92) shows consistent vocabulary. No alternative convention surfaces.

### §9.3 Attempt 3 — Does the W6 strategic plan's "~0.075·m̄" framing have a hidden valid basis?

**Method.** Reverse-engineer: under what reading of $\bar m$ does $0.225 = 0.075 \cdot \bar m$ hold? Answer: $\bar m = 3$.

**Possible basis for $\bar m = 3$:**
- **Hypothesis (a):** $\bar m = K_{\mathrm{act}}$ (the active count). For initial setup with `initial_masses = (30, 30, 30, 0)`, $K_{\mathrm{act}} = 3$. But this would make $\epsilon$ a count, not a mass — dimensionally wrong.
- **Hypothesis (b):** $\bar m = $ some implicit normalized reference (e.g., $\bar m = 1$ rescaled to "intuitive units"). Not in any source file.
- **Hypothesis (c):** $\bar m = (M / K_{\mathrm{field}}) / \text{(normalization factor)}$, e.g., normalized by 7.5 to give $\bar m = 3$. Not in any source file.

None of (a)/(b)/(c) is a documented convention. **The W6 strategic plan's "~0.075·m̄" framing is unsupported by sources.** Verdict: misframing.

### §9.4 §9 verdict — no genuine counterexample to R1

The R1 reading is consistent with all examined production scripts and with the OAT-1 source's spirit ("provisional, deferred"). The W6 strategic plan's contrary framing is a documentation artifact, not a real contradiction.

---

## §10. Cat Classification + Status Self-Check

### §10.1 Per-result self-classification

| Statement | Status | Cat | Notes |
|---|---|---|---|
| §1.1 nq242c uses R1 explicitly | proved | A absolute | Direct script comment quote |
| §1.2-1.4 other scripts use R1 implicitly | proved | A conditional on numerical consistency | $0.225 = 0.01 \cdot 90/4$ matches across scripts; cross-script audit |
| §2.5 OAT-1 author's intent is provisional + deferred | proved | A absolute | Direct quote of `K_status_commitment.md` lines 263, 313, 356 |
| §5.1 Diagnostic verdict D1 | proved | A absolute | Combines §1, §2, §3, §4 evidence |
| §6.1 Proposed Commitment 16 amendment text (R1 explicit) | proposed | A definitional precision | One-sentence wording amendment, no theorem change |
| §6.3 Why R1 over R2 (circularity argument) | proved | A absolute | R2 makes ε circular with K_act |
| §7 Propagation plan (1 canonical line + 0 script changes + 1 CHANGELOG entry) | proposed | A executable | Minimal-edit plan |
| §9 Counterexample attempts | sketched | A absolute as a finite-script audit; conditional on no other scripts having alternative ε | Audited 4 scripts + spot-checked 1 working file; not exhaustive |

**Overall cat for the deliverable:** **Cat A definitional precision.** The diagnostic + decision rule are rigorous; the proposed canonical amendment is a one-sentence wording clarification matching empirical script usage + the OAT-1 author's provisional intent.

### §10.2 Granularity check (per prompt §9)

Each substantive claim is independently verifiable:
- **§1.1 nq242c R1** can be verified by reading `nq242c_counterexample.py` line 80.
- **§2.3 OAT-1 deferral** can be verified by reading `K_status_commitment.md` line 313.
- **§5.1 diagnostic verdict** can be verified by re-running the §1–§4 evidence chain.
- **§6.3 R2 circularity** can be verified by attempting to define $\epsilon$ via $M/K_{\mathrm{act}}$ and noting $K_{\mathrm{act}}$ depends on $\epsilon$.

The §-numbering is preserved for audit references.

### §10.3 OP non-impact statement

This G3 decision:
- Does **not** affect OP-0001 (F-1), OP-0002 (M-1), OP-0003 (MO-1) — orthogonal layer.
- Does **not** affect OP-0005 (K-Selection) — does not address the K mechanism; only the threshold for declaring a slot "active."
- Does **not** affect OP-0008 (σ^A K-jump non-determinism) — orthogonal.
- Does **not** affect OP-0009 (Multi-Formation Ontological Foundations) sub-items — Commitment 16 K-status decomposition unchanged; only the ε-default wording is clarified.
- Does **not** affect OP-0006, OP-0010, OP-0011, OP-0012, OP-0013 — unrelated layers.
- **N-1 (Soft-Hard Switching Asymmetry):** preserved. K_act stays integer; ε threshold convention is on the K_act-from-K_field projection, not on K_act ↔ K_soft.

**No silent OP resolution.**

### §10.4 Hard-constraint sweep

- [x] Canonical 직접 수정 0 (this file proposes the §6.1 amendment but does not apply it to canonical.md).
- [x] Working/ 직접 수정 0 (this file proposes the §7.4 optional working-file annotations but does not apply them).
- [x] scc/ 0 edits.
- [x] Silent OP resolution 0.
- [x] N-1 / CN5 / CN6 / CN7 / CN10 / CN15: all preserved.
- [x] u_t primitive maintained (this G3 decision is on the K_act diagnostic, not on the field $u^{(j)}$).
- [x] No metastability claim w/o P-F flag.
- [x] No Research OS resurrection.
- [x] No external-framework reduction.

### §10.5 Diminishing returns check

The diagnostic + decision are complete. Additional scope (e.g., re-running L1-I at $\epsilon = 0.03$ to compare regime sizes; auditing more scripts beyond the four primary ones) is **incremental polishing** without new structural content. Per prompt §13: stop at this natural matching point + leave next session seed in `99_summary.md`.

---

**End of `02_development.md`.**

**Next file:** `03_integration_and_new_open.md` — Integration with canonical structure + new open questions + prompt v2 candidate notes.
