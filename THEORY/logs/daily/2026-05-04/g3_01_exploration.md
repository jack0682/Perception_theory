# 01_exploration.md — G3 K_act ε-Convention Decision: Restatement + Multi-Approach + Primary Selection

**Session:** 2026-05-04 (W6 Day 1, Day 1 mid-day acceleration of redesigned Day 3 work)
**Target (from plan.md):** redesigned W6 plan **G3 — K_act ε-convention decision and propagation**. Decide between Commitment 16 default ε = 0.01·m̄ vs production-script default ε = 0.225, and propagate the choice to canonical / working / scripts. Anchor: redesigned `W6_strategic_plan.md` G3 (lines 49-58) + canonical `Commitment 16` (line 810) + script empirical usage.
**This file covers:** §1 problem restatement (what G3 is *actually* asking, with implicit assumptions surfaced); §2 multi-approach (5 mathematically distinct decision rules); §3 primary selection (A4 diagnostic-first) + alternatives preserved.
**Depends on reading:** `THEORY/canonical/canonical.md` line 810 (Commitment 16 K_act definition + ε default); `THEORY/canonical/canonical.md` lines 1482-1489 (T-L1-F entry, "439/1920 FEASIBLE_WITH_BUDGET" empirical claim); `THEORY/working/MF/kbar_kact_bridge_L1I_constants_feasibility.md` (L1-I source, parameter sweep design); `CODE/scripts/nq242c_counterexample.py` lines 78-100 (RunConfig with explicit ε comment); `CODE/scripts/l1i_constants_feasibility.py` lines 605-625 (M_total + ε); `CODE/scripts/wq_lat1_reservoir_resolution_sweep.py` lines 77, 190-200; `THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md` G3 (lines 49-58) — the weekly anchor.

---

## §1. Restatement (what is G3 actually asking?)

### §1.1 The W6 strategic plan's framing

`W6_strategic_plan.md` G3 (verbatim, lines 49-57):

> **Status:** Commitment 16 (canonical) proposes default ε = 0.01·m̄. Production scripts (`l1g_l1hyp_diagnostic.py`, `l1i_constants_feasibility.py`, `wq_lat1_*.py`, `nq242c_*.py`) all use ε = 0.225 (~0.075·m̄ for K_field = 4). T-L1-F's "439/1920 = 22.9% feasible" empirical claim is for ε = 0.225, not Commitment 16's default.
>
> Without unification, the conditional Cat A status of T-L1-F is ambiguous: under which ε does the regime hold non-vacuously?
>
> **Deliverable:** a single canonical ε convention (either confirm Commitment 16 default and re-run the empirical scripts, or amend Commitment 16 to match the script default), applied across canonical / working / scripts.

The framing presupposes that **0.225 ≠ 0.01·m̄** under the canonical reading of m̄. Specifically, "(~0.075·m̄ for K_field = 4)" implies m̄ ≈ 3 in the strategic plan's assumed notation.

### §1.2 What "m̄" actually means in the codebase

`canonical.md` line 810 (Commitment 16):

> $K_{\mathrm{act}}(\mathbf{u}(t)) := \#\{j \in \{1, \ldots, K_{\mathrm{field}}\} : \|u^{(j)}(t)\|_1 > \epsilon\}$
> for support threshold $\epsilon$ (default $\epsilon = 0.01 \cdot \bar{m}$, $\bar{m}$ per-formation expected mass).

The canonical text says "per-formation expected mass" but does **not** uniquely fix what "per-formation expected mass" means. Three readings are syntactically possible:

- **(R1) Architectural per-formation mean:** $\bar m = M / K_{\mathrm{field}}$, where $M$ is the total system mass. Under this reading, for $M = 90$ and $K_{\mathrm{field}} = 4$: $\bar m = 22.5$, and the script default $\epsilon = 0.225 = 0.01 \cdot 22.5 = 0.01 \cdot \bar m$. **No discrepancy.**
- **(R2) Active per-formation mean:** $\bar m = M / K_{\mathrm{act}}$, where $K_{\mathrm{act}}$ is the active count (e.g., 3 in production setup with `initial_masses=(30,30,30,0)`). Under this reading: $\bar m = 30$, and the script $\epsilon = 0.225 = 0.0075 \cdot 30 = 0.0075 \cdot \bar m$. **Real discrepancy by factor 0.75.**
- **(R3) Single-formation reference mass:** $\bar m \approx 3$ (per W6 strategic plan G3's "~0.075·m̄ for K_field = 4" implicit reading). Under this reading: $\bar m = 3$, and the script $\epsilon = 0.225 = 0.075 \cdot \bar m$. **Real discrepancy by factor 7.5.**

Production-script empirical evidence (decisive for which reading is intended in scripts):

`CODE/scripts/nq242c_counterexample.py` line 80:
```python
epsilon: float = 0.225  # 0.01 * (M / K_field) = 0.01 * 22.5
```

This comment **explicitly** shows the script uses reading **R1**: $\epsilon = 0.01 \cdot (M / K_{\mathrm{field}}) = 0.01 \cdot 22.5$.

Cross-confirmed: `l1i_constants_feasibility.py` lines 612-613 (`M_total = 90.0; epsilon = 0.225`) and `wq_lat1_reservoir_resolution_sweep.py` lines 77, 192 (`CLUSTER_MASS = 30.0` "per-cluster mass (3 clusters, total M=90)"; `M=90.0, epsilon=0.225`).

### §1.3 The hidden question

So the actual G3 question is **not "0.01 vs 0.075" formula choice**, but rather:

> **Is the canonical "$\bar m$ per-formation expected mass" in Commitment 16 to be read as (R1) $M/K_{\mathrm{field}}$, (R2) $M/K_{\mathrm{act}}$, or (R3) some external reference mass?**

If R1 is the intended reading, **there is no actual discrepancy** between Commitment 16 and the scripts; the W6 strategic plan G3's framing is misleading. The "fix" is to *clarify Commitment 16* to make R1 explicit — a 1-line wording change.

If R2 or R3 is intended, **there is a real discrepancy**, and either Commitment 16 must be amended or the scripts must be re-run with the canonical ε.

### §1.4 Restatement of the success criterion

A successful G3 deliverable produces:
1. **Diagnostic:** a definitive determination of which reading (R1/R2/R3) the scripts use (already mostly known from §1.2 above — they use R1).
2. **Determination:** which reading the canonical Commitment 16 *intends* (requires reading the W5 D3 EOD OAT-1 source `working/MF/K_status_commitment.md` if needed, plus historical context).
3. **Decision:** if R1 ≡ scripts ≡ canonical-intent → minimal wording clarification of Commitment 16. If reading mismatch → choice between (a) preserve canonical, re-run scripts (~2-3 days), or (b) amend canonical, sync scripts (~1 day).
4. **Propagation plan:** specific files / lines to edit + verification steps.
5. **T-L1-F empirical claim re-anchor:** the "439/1920 = 22.9% feasible" claim's ε regime made explicit.

### §1.5 What G3 is NOT asking (non-claims to preserve)

- G3 does **not** revise T-L1-F's $(P0)$–$(P11)$ regime structure (only ε within (P2)).
- G3 does **not** affect Commitment 16's K_field/K_act two-tier decomposition (only the threshold inside K_act's definition).
- G3 does **not** touch OP-0005 (K-Selection) or OP-0008 (σ^A K-jump non-determinism).
- G3 does **not** modify the $\Phi_{\mathrm{res}}$ envelope class for L-M (deferred per redesigned W6 plan §2).
- G3 is **not** a substantive theory change; it's a notational unification across the canonical / working / script layers.

---

## §2. Multi-Approach (5 mathematically distinct decision rules)

Each approach below is a different decision rule for resolving the ε-convention question. They differ in (a) which layer is taken as authoritative (canonical / scripts / new), (b) what notational reading of $\bar m$ is adopted, (c) what propagation cost is incurred, (d) what failure mode emerges if the underlying premise is wrong.

### §2.1 Approach A1 — Preserve canonical literally; re-run scripts

**Core idea.** Take Commitment 16's "$\epsilon = 0.01 \cdot \bar m$" as authoritative under the strategic plan's R3 reading ($\bar m \approx 3$). Re-run all production scripts with $\epsilon = 0.03$ (= $0.01 \cdot 3$, far smaller than current 0.225). Re-derive T-L1-F's "439/1920 feasible" under the new ε.

**Success outcome.** Commitment 16 unchanged; script defaults updated; T-L1-F empirical claim re-anchored with potentially different fraction (likely smaller — tighter ε = stricter activity threshold).

**Failure mode.** L1-I FEASIBLE_WITH_BUDGET set may shrink dramatically (closer to 0/1920 or vacuous); T-L1-F becomes practically irrelevant. Also: requires script re-runs (~2-3 days compute + analysis).

**Interaction with existing structure.** Heavy. Canonical preserved; scripts and `kbar_kact_bridge_L1I_constants_feasibility.md` empirical claims need re-anchoring; `T-L1-F` canonical entry's empirical-anchor parenthetical needs revision; downstream `nq242c` / `wq_lat1_*` analyses need re-execution.

### §2.2 Approach A2 — Amend canonical to match scripts

**Core idea.** Take production-script $\epsilon = 0.225$ as authoritative. Amend Commitment 16 to either: (a) replace "$\bar m$ per-formation expected mass" with the explicit formula "$\bar m = M / K_{\mathrm{field}}$" (i.e., adopt R1 as the canonical reading); or (b) drop the formulaic default and just say "$\epsilon$ is a configuration-dependent threshold; production default $\epsilon = 0.225$ on $T^2_{20}$ with $M = 90$, $K_{\mathrm{field}} = 4$."

**Success outcome.** Scripts unchanged; canonical-text amendment ~1 day; T-L1-F empirical claim already valid under amended convention.

**Failure mode.** If the original canonical author intended R3 (or some other strict reading), this amendment silently weakens the canonical commitment. Risk: hidden semantic drift.

**Interaction with existing structure.** Light. canonical.md line 810 amended; `theorem_status.md` updated to reflect; scripts unchanged; `T-L1-F` canonical entry's empirical claim remains valid.

### §2.3 Approach A3 — Dual-convention regime

**Core idea.** Register both ε conventions in Commitment 16 as alternative regime parameters: (i) **theoretical-default** $\epsilon_{\mathrm{theo}} = 0.01 \cdot M / K_{\mathrm{field}}$ (R1 explicit), (ii) **strict-default** $\epsilon_{\mathrm{strict}} = 0.01$ (or smaller absolute, if R3 ever needed). T-L1-F's empirical claim is tagged with which ε is used.

**Success outcome.** No script changes; canonical gains explicit dual-convention note; future regime decisions can choose between conventions.

**Failure mode.** Adds complexity without resolving the underlying ambiguity; future readers must navigate two conventions; possible silent drift if scripts and canonical diverge on which convention is "default."

**Interaction with existing structure.** Medium. Commitment 16 expanded by ~10 lines; `T-L1-F` entry needs to specify which ε; future canonical / working files inherit the dual-convention burden.

### §2.4 Approach A4 — Diagnostic-first (verify R1/R2/R3 by reading sources)

**Core idea.** Before choosing A1/A2/A3, **diagnose the actual nature of the discrepancy** by reading:
1. The W5 D3 EOD OAT-1 source `working/MF/K_status_commitment.md` to determine what reading of $\bar m$ the original author of Commitment 16 intended.
2. The four production scripts' explicit comments / variable derivations to confirm they all use R1.
3. The `kbar_kact_bridge_L1I_constants_feasibility.md` document and any other references to ε to check for additional readings.

After diagnosis, branch:
- **(D1) If canonical intent = R1 = scripts:** the discrepancy is only a notational lacuna (Commitment 16's "$\bar m$ per-formation expected mass" is too vague). **Apply A2 in minimal form**: clarify Commitment 16 to make R1 explicit. ~30 minutes.
- **(D2) If canonical intent ≠ scripts:** the discrepancy is real. Apply A1 or A2 in full form. ~1-3 days.
- **(D3) If canonical intent is genuinely ambiguous:** apply A3 (dual-convention). ~1 day.

**Success outcome.** Targeted decision based on actual evidence; minimal wasted work.

**Failure mode.** Diagnostic step itself may be inconclusive (e.g., source author's intent unrecoverable). Mitigation: in (D3) fallback, dual-convention is always safe.

**Interaction with existing structure.** Adaptive. Cost depends on diagnosis outcome (best case ~30 min for D1; worst case ~3 days for D2 with re-runs).

### §2.5 Approach A5 — Reframe ε as a configuration-derived parameter (no canonical default)

**Core idea.** Drop the canonical default entirely. Commitment 16 becomes: "$\epsilon$ is a regime parameter (a configuration choice); SCC ontology does not commit to a specific value. Production studies report ε explicitly with each measurement." T-L1-F's "439/1920 feasible" is tagged "for $\epsilon = 0.225$ on $T^2_{20}$, $M = 90$, $K_{\mathrm{field}} = 4$."

**Success outcome.** Removes the default ambiguity by removing the default. Production studies become more honest about regime parameters.

**Failure mode.** Canonical becomes silent on a load-bearing parameter; future readers may not know what ε to start with for new studies; "reasonable default" intuition is lost.

**Interaction with existing structure.** Medium. Commitment 16 amendment (~5 lines); existing references to "default ε" need to be tagged with explicit values; `T-L1-F` entry empirical claim explicit.

### §2.6 Approach independence check

The five approaches differ in:
- **Authoritative layer:** A1 = canonical wins; A2 = scripts win; A3 = both registered; A4 = diagnose first; A5 = neither (configuration-derived).
- **Outcome on Commitment 16:** A1 unchanged; A2 amended (1 line); A3 expanded (10 lines); A4 conditional (depends on D1/D2/D3); A5 reframed (5 lines, default dropped).
- **Outcome on scripts:** A1 re-run with new ε (heavy); A2/A3/A4-D1/A4-D2(with R1)/A5 unchanged; A4-D2(with non-R1) re-run.
- **Failure modes:** A1 (regime vacuous), A2 (semantic drift), A3 (complexity), A4 (diagnostic inconclusive), A5 (silent default loss).

These are mathematically independent decision rules with different outcomes under different premises. ✓

---

## §3. Primary Selection: A4 (Diagnostic-First)

### §3.1 Selection rationale

**A4 is primary** because:

1. **Asymmetric cost.** A4's diagnostic step is cheap (~30 minutes of reading 2-3 files); the *decision* it informs is what would otherwise be expensive (A1: 2-3 days; A2: 1 day). Diagnose first, decide cheap.
2. **Risk of hidden assumption.** Any of A1/A2/A3/A5 chosen *without* diagnostic risks committing to a reading (R1 vs R2 vs R3) that doesn't match the original canonical intent. A4 surfaces the assumption.
3. **The §1.2 evidence already strongly suggests D1** (canonical intent = R1 = scripts). Production-script comment in `nq242c_counterexample.py` line 80 is explicit: `0.225 = 0.01 * (M / K_field) = 0.01 * 22.5`. This nearly closes the diagnostic; A4 just needs one more confirmation (read `K_status_commitment.md`).
4. **Best-case path is essentially A2-minimal** (clarify Commitment 16 to make R1 explicit; ~30-minute edit), but with a much stronger justification trail than launching A2 blind.
5. **Worst-case fallback is A3** (dual-convention) which is always semantically safe, even if not aesthetically minimal.

### §3.2 Why the alternatives are NOT primary

- **A1** would discard the production-script empirical evidence (4 scripts × ε=0.225) as "incorrect"; without diagnostic, this is overconfident.
- **A2 (blind)** would silently commit to a reading without verifying canonical intent — the very semantic-drift risk the W6 audit Pass 2 is supposed to catch.
- **A3 (blind)** adds complexity without resolving the question; should only be the fallback if diagnostic is inconclusive.
- **A5** is over-radical for a notational unification problem; appropriate for a deeper "is ε a parameter at all?" question, but G3 is more modest.

### §3.3 Alternatives preserved

All four alternatives (A1, A2, A3, A5) are preserved as branch options conditional on the diagnostic outcome (§2.4 D1/D2/D3 branches). If A4 diagnostic surfaces an unexpected R-reading, A1/A3/A5 are activated.

---

## §4. Plan for `02_development.md` (primary approach deep-dive)

The 02 file will execute A4's diagnostic phase + apply the resulting decision rule. Concretely:

- §1 Diagnostic source #1: production-script comment + variable trace (already strongly evidenced for R1).
- §2 Diagnostic source #2: W5 D3 EOD OAT-1 source `working/MF/K_status_commitment.md` reading for canonical intent.
- §3 Diagnostic source #3: `kbar_kact_bridge_L1I_constants_feasibility.md` for any additional ε-reading evidence.
- §4 Cross-check: `T-L1-F` canonical entry (line 1489: "L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$") implicitly tagged with which ε?
- §5 Diagnostic verdict: D1 / D2 / D3.
- §6 Decision rule applied: minimal Commitment 16 amendment text proposal (Cat A definitional precision).
- §7 Propagation plan: which canonical lines, which working files, which script comments need updating + verification.
- §8 T-L1-F empirical claim re-anchor wording.
- §9 Counterexample attempts: any scripts that *don't* use ε = 0.01 · (M / K_field)? Any working files with conflicting ε convention?
- §10 Cat classification: Cat A definitional precision (no theorem change).

**End of `01_exploration.md`.**

**Next file:** `02_development.md` — A4 diagnostic execution + decision rule + propagation plan.
