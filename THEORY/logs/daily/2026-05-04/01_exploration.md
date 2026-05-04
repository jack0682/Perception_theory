# 01_exploration.md — G1 L-M-AUDIT Closure: Restatement + Multi-Approach + Primary Selection

**Session:** 2026-05-04 (W6 Day 1, mid-day, post-G3-deep-dive)
**Target (from `plan.md` v2 §3 G1 row + §4.2):** Close redesigned W6 plan **G1 — L-M-AUDIT (R-1 / R-2 / R-3 closure)** by self-audit. Apply 3 textual repairs (R-1 sharpness verification, R-2 §5.5 Type-B chain, R-3 §5.4 Type-N non-terminal note) + minor §2.2 Phi-4c F1 wording fix to L-M working draft (`logs/daily/2026-05-03/02_L1M_proof_development.md`). Produce Cat-A-conditional promotion text (canonical §13 T-L1-M new entry, immediately after T-L1-F). Originally W6 plan Day 4-5 work; first autonomous session over-delivered Day 1 morning, work was deleted in 10:30 reset; this session re-executes self-audit-mode.
**This file covers:** §1 problem restatement (audit closure under post-reset constraints); §2 multi-approach (5 distinct closure routes); §3 primary selection (A3 self-audit) + alternatives preserved.
**Depends on reading:** `THEORY/logs/daily/2026-05-04/plan.md` v2 (§3 G1 row + §4.2 Day 2 Block 1 prescription); `THEORY/logs/daily/2026-05-03/02_L1M_proof_development.md` (L-M working draft, audit subject); `THEORY/canonical/canonical.md` §13 T-L1-F (lines 1482-1489) + §11.1 #16 Commitment 16 (lines 804-820); `THEORY/logs/daily/2026-05-04/g3_*.md` (G3 deep-dive: shows ε convention is now R1 = $M / K_{\mathrm{field}}$, Cat A definitional precision; impacts L-M's $\epsilon$ usage in Theorem L-M); conversation memory of (a) the deleted G2-OLD-plan CSEH negative finding (factor 2 sharp under L1-J) — pre-resolves R-1; (b) the deleted G1 audit verdict — provides R-2 / R-3 / minor §2.2 Phi-4c F1 specifications.

---

## §1. Restatement

### §1.1 What G1 is asking (post-reset framing)

The redesigned W6 plan G1 (`W6_strategic_plan.md` lines 18-30) targets:

> L-M-2 Cat-B sketched → Cat-A conditional via explicit closure of R-1/R-2/R-3, OR a deliberate retention at Cat-B with an explicit failure analysis.

Three refinements were flagged in `02_L1M_proof_development.md` §5.7 by the L-M working-draft author (W5 Day 7):

- **R-1**: bottleneck-stability factor sharpness in §5.4 Type-N bound (whether the factor 2 in $|\ell_i - \ell_i^{(u^{(j)})}| \le 2 \cdot \rho_{\mathrm{pert}}/2 = \rho_{\mathrm{pert}}$ is sharp or expandable to factor 1 via terminal-death convention).
- **R-2**: Type-B bound LG-7 reuse explicit reproof in §5.5 (whether the §5.5 invocation of "Type-B classification as background" cleanly follows from re-deriving LG-7 within L-M-2's scope, or implicitly assumes T-L1-F's proof structure).
- **R-3**: terminal-death convention Type-N consistency in §5.4 (whether the §5.4 bottleneck-stability comparison correctly handles Type-N bars as finite-death merge bars, not terminal bars).

A fourth, minor refinement was surfaced by the deleted G1 audit verdict (W6 D1 morning autonomous session, conversation-memory only):

- **R-0** (label introduced for clarity; was not flagged in §5.7): L-M-D1 §2.2 Phi-4c F1 wording — the "tighten F1 to $\phi(\ell) \ge 0$ by clipping at $0$ if needed; alternatively restrict $\Phi_{\mathrm{res}}$ to $\phi$ that already satisfy F1" hedge is unnecessary because $\phi_{\mathrm{logistic}}^s$ with the WQ-LAT-1.B definition is non-negative on $[0,1]$ by monotonicity ($\phi(0) = 0$ + monotone non-decreasing ⇒ $\phi(\ell) \ge 0$).

**G1 closure target:** apply R-0 + R-1 + R-2 + R-3 as concrete textual repairs to L-M working draft + produce Cat-A-conditional promotion text for canonical §13 + update `theorem_status.md` row.

### §1.2 Post-reset constraints

The 10:30 reset deleted three artifacts that affect this G1 closure:

1. **`01a_l1m_audit_verdict.md`** — the audit verdict (REPAIR-NEEDED) with explicit replacement-text blocks for R-1, R-2, R-3, R-0. **Conversation memory has the high-level summary; specific replacement wording must be re-derived.**
2. **`cseh_factor_sharpness_analysis.md`** — the Cat A negative finding that pre-resolved R-1 (factor 2 sharp under L1-J because Type-N bars are intra-slot merge bars, not terminal). **Conversation memory has the structural argument; re-derivation is straightforward but lengthy.**
3. **`01_l1m_audit_dispatch.md`** — the dispatch record. Procedural; not load-bearing for the closure itself.

These deletions mean G1 closure must either (a) re-spawn the audit (recovers all 3), (b) memory-base the closure (less rigorous), or (c) self-audit (this session derives R-0/R-1/R-2/R-3 closures from first principles + conversation memory + canonical access).

### §1.3 Success criterion

A successful G1 closure produces:

1. **R-1 closure**: factor-2 sharpness verification with explicit perturbation construction (or alternative tightening proposal). Cat A absolute.
2. **R-2 closure**: §5.5 Type-B bound rewritten with explicit P5-or-P10 chain (no implicit T-L1-F dependency). Cat A absolute.
3. **R-3 closure**: §5.4 Type-N non-terminal status appended as a clarification block; consistency with §5.4 bottleneck-stability bound verified. Cat A absolute.
4. **R-0 closure**: §2.2 Phi-4c F1 wording simplified (drop the unnecessary clipping hedge). Cat A absolute.
5. **L-M-2 Cat-A-conditional self-classification**: post-repair, Lemma L-M-2 upgrades from "Cat B sketched" to "Cat A conditional under $(P0)$–$(P11)$".
6. **Theorem L-M Cat-A-conditional**: post-repair, Theorem L-M upgrades from "Cat B sketched" to "Cat A conditional under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}} + \tau < \tau_*$".
7. **Per-family corollaries**: L-M.A Cat A absolute (trivial substitution); L-M.B / L-M.C Cat A conditional inheriting Lemma L-M-2.
8. **Canonical promotion proposal**: text for new T-L1-M entry in §13, immediately after T-L1-F (line 1489), formatted to match T-L1-F's entry style.
9. **theorem_status.md update proposal**: new C-0722 row; CV-1.6 release-version-history entry (proposal only — actual CV-1.6 release deferred per W6 plan §2 explicit non-goals).
10. **OP non-impact statement**: G1 does not silently resolve OP-0005 / OP-0008 / OP-0009 / etc.

### §1.4 Non-claims to preserve

- G1 closure does **not** automatically promote L-M to canonical (per W6 plan §2: "L-M canonical promotion is a CV-1.6 release activity, not a W6 commit"). G1 closes the *audit*; the *promotion* is a separate user-supervised step.
- G1 closure does **not** resolve the L-M perturbation analysis (was OLD G6, deferred per W6 plan §2 explicit non-goals).
- G1 closure does **not** address the T-σ-Theorem-4 γ/β/α reconciliation (deferred).
- G1 closure does **not** modify Commitment 16 (the G3 deep-dive proposed an amendment; G1 inherits the amended ε convention but does not propose further changes to Commitment 16).
- G1 closure does **not** affect `Φ_res` definitional axioms F1-F5 (only R-0 minor wording on the F1 verification of φ_logistic; F1 itself unchanged).

### §1.5 Hidden assumption surfaced

The plan's "$\tau < \tau_*$" condition (where $\tau_* = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$) hides the fact that $\tau_*$ depends on the L1-J regime constants $\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}}$, which themselves require the L1-I FEASIBLE_WITH_BUDGET set to be non-empty (which is empirically established at "439/1920 = 22.9%" per L1-I + T-L1-F). G1 closure therefore implicitly inherits T-L1-F's regime feasibility caveats. Made explicit in the post-closure Theorem L-M statement (§5 below in `02_development.md`).

---

## §2. Multi-Approach (5 distinct G1 closure routes)

Each approach below is a different rule for closing G1 under the post-reset constraints (§1.2). They differ in (a) the source of R-0/R-1/R-2/R-3 closure derivations, (b) the rigor level of the resulting closure, (c) the time cost, (d) the failure mode if the source is unreliable.

### §2.1 Approach A1 — Re-spawn `l1m-audit-prover` agent

**Core idea.** Dispatch a fresh general-purpose subagent with the same prompt as the deleted W6 D1 morning dispatch (`01_l1m_audit_dispatch.md` recoverable from conversation memory). Pass conversation-memory R-1 closure summary as additional input so the agent does not need to re-derive CSEH analysis. Background dispatch (`run_in_background: true`); verdict file at `01a_l1m_audit_verdict.md`.

**Success outcome.** Authoritative external audit verdict (REPAIR-NEEDED with closeable repairs); explicit replacement-text blocks for each refinement.

**Failure mode.** Agent may produce different verdict than the deleted one (audit non-determinism); agent may take longer than expected (~7-15 min); agent's repair specifications may differ subtly from the deleted verdict.

**Interaction with existing structure.** Heavy. Agent dispatch + verdict integration + Day 2 morning workflow (per `plan.md` v2 §4.2 (a-ii) recommendation).

### §2.2 Approach A2 — Memory-only textual repair

**Core idea.** Apply the conversation-memory summary of R-0/R-1/R-2/R-3 directly to L-M working draft. No re-spawn; no self-derivation.

**Success outcome.** Fastest path (~30 min); preserves the previously-achieved Cat-A-conditional verdict.

**Failure mode.** Conversation memory is high-level summary; specific replacement wording may be misremembered; downstream audit (e.g., CV-1.6 release packet review) may catch discrepancies. Lower rigor.

**Interaction with existing structure.** Light. Direct edits to L-M working draft (per `plan.md` v2 §4.2 (b)).

### §2.3 Approach A3 — Self-audit (this session as audit teammate)

**Core idea.** This Claude session **is** the audit teammate for G1 closure. Derive R-0/R-1/R-2/R-3 closures from first principles + conversation memory + canonical access (without spawning an external agent). For each refinement:
- Read the relevant L-M draft section.
- Identify the gap.
- Construct the explicit closure (proof / replacement wording).
- Verify Cat A absolute classification.

This produces the same end-state as A1's verdict but written by this session, with full traceability in `02_development.md`.

**Success outcome.** Cat-A-grade closure with full proof rigor; explicit replacement text + canonical promotion proposal text; identical end-state to A1's authoritative verdict.

**Failure mode.** This session may make subtly different judgment calls than an external auditor would (audit non-independence). Mitigation: explicit acknowledgement in §10 of `02_development.md` that the audit is internal; conversation memory of the deleted external audit's verdict serves as a cross-check.

**Interaction with existing structure.** Medium. Self-audit produces 02_development.md content directly; no agent dispatch overhead; user-supervised promotion remains a separate step (§8.1 hard constraint preserved).

### §2.4 Approach A4 — Schedule per Day 4-5 original

**Core idea.** Treat the 10:30 reset as a deliberate revert to the original W6 plan Day 4-5 schedule for G1. Do nothing on G1 today; postpone to Day 4 (R-1 + R-2) and Day 5 (R-3 + Cat-A decision). Day 1 ends with G2 done + G3 done + G1 not started.

**Success outcome.** Aligns with original W6 plan §3 daily breakdown literally; no Day 1 over-delivery on G1.

**Failure mode.** Loses the previously-achieved Cat-A-conditional verdict (must be re-derived Day 4-5 from scratch); under-utilizes Day 1 substantive capacity (G3 done; remaining hours could close G1).

**Interaction with existing structure.** None today; Day 4-5 unchanged from W6 plan.

### §2.5 Approach A5 — Hybrid (self-audit + post-hoc external verification)

**Core idea.** Self-audit (A3) for the textual repair specifications + Cat-A-conditional closure today. After this session, optionally re-spawn `l1m-audit-prover` (A1) as a post-hoc external verification of the self-audit's repair specifications. If the external audit agrees, full closure with maximum rigor; if disagrees, repair the self-audit.

**Success outcome.** Self-audit produces immediate Cat-A-conditional closure; external verification adds independent-audit rigor.

**Failure mode.** Doubled effort if the external audit confirms self-audit (no value-added beyond rigor); external audit dispatch consumes additional compute.

**Interaction with existing structure.** Medium-heavy. Self-audit + agent dispatch.

### §2.6 Approach independence check

The five approaches differ in:
- **Source of repair specs:** A1 = external agent; A2 = conversation memory; A3 = self-derivation + memory cross-check; A4 = none today (deferred); A5 = self-derivation + external verification.
- **Rigor level:** A1 ≥ A5 > A3 > A2 > A4 (no closure today).
- **Time cost:** A4 (0 today) < A2 (~30 min) < A3 (~1.5-2 hours) < A1 (~7-15 min agent + integration) < A5 (A3 + A1 sequential).
- **Failure modes:** A1 (non-determinism), A2 (memory error), A3 (audit non-independence), A4 (under-use), A5 (doubled effort).

These are mathematically and procedurally independent. ✓

---

## §3. Primary Selection: A3 Self-Audit

### §3.1 Selection rationale

**A3 is primary** because:

1. **Persistent autonomous mode + "if next step is known and safe, do it."** A3 is the only approach where the session itself produces the closure deliverable (no waiting on agents). Aligned with `plan.md` v2 §4.2 spirit + persistent-mode prompt instruction.

2. **Conversation memory is sufficient for direction; canonical + L-M draft access provides the rigor.** R-0 (Phi-4c F1 wording) and R-3 (Type-N non-terminal note) have clear conversation-memory specifications. R-1 (factor 2 sharpness) and R-2 (Type-B chain) require deeper derivation, which can be done from first principles using the L-M draft + canonical T-L1-F + standard CSEH 2007.

3. **A1 (re-spawn) is wasteful given the substantive content is already known.** The deleted external audit verdict was REPAIR-NEEDED with closeable repairs. Re-spawning would re-derive what's already known + risk audit non-determinism producing different specifications.

4. **A2 (memory-only) is too fragile.** Specific replacement wording for R-2 / R-3 must be precise; high-level memory may produce subtle errors that manifest only at CV-1.6 release packet review.

5. **A4 (defer) discards Day 1 substantive capacity.** Day 1 has G2 done + G3 done; closing G1 today completes 3 of 4 W6 goals on Day 1, freeing Day 2-7 for G4 + slack work.

6. **A5 (self-audit + external verification) doubles effort without clear value-added.** The self-audit's rigor + canonical access makes the external verification redundant unless an independent reviewer is genuinely needed (which the W5 D6 L1-K audit pattern provides for canonical promotion, NOT for working-grade audit closure).

### §3.2 Why the alternatives are NOT primary

- **A1**: redundant given conversation memory + canonical access; non-determinism risk.
- **A2**: too low-rigor for Cat-A-conditional closure that will feed into CV-1.6 release.
- **A4**: deliberate under-use; no rationale to wait until Day 4-5 when closure is achievable today.
- **A5**: see §3.1 #6.

### §3.3 Alternatives preserved

A1 / A2 / A4 / A5 all preserved as branch options if A3 self-audit encounters a refinement that genuinely requires external review (none expected based on conversation memory). If A3 produces a "REPAIR-NEEDED-DEEPER" verdict (rather than the expected "PASS or REPAIR-NEEDED-CLOSEABLE"), A1 (re-spawn) becomes the natural fallback.

### §3.4 A3 execution outline (preview of `02_development.md`)

The A3 self-audit will execute in this order:

- **§1 R-0 closure** (§2.2 Phi-4c F1 wording fix, ~5 min, trivial).
- **§2 R-1 closure** (§5.4 factor-2 sharpness verification, ~30 min, CSEH-style derivation).
- **§3 R-2 closure** (§5.5 Type-B chain explicit reproof, ~30 min, P5-or-P10 derivation).
- **§4 R-3 closure** (§5.4 Type-N non-terminal note, ~15 min, R-1 follow-on).
- **§5 Lemma L-M-2 post-repair Cat-A-conditional self-classification**.
- **§6 Theorem L-M post-repair Cat-A-conditional statement**.
- **§7 Per-family corollaries L-M.A/B/C self-classification**.
- **§8 Counterexample stability check** (the §7 four counterexample attempts in L-M draft remain non-counterexamples after R-0/R-1/R-2/R-3).
- **§9 Granularity check** (per prompt §9).
- **§10 Hard-constraint sweep + audit-independence acknowledgement**.

---

## §4. Plan for `02_development.md`

The 02 file will execute A3's self-audit + produce the Cat-A-conditional closure deliverable + propose canonical promotion text. The 03 file will integrate with T-L1-F + propose `theorem_status.md` updates + collect new open questions.

**End of `01_exploration.md`.**

**Next file:** `02_development.md` — A3 self-audit execution + R-0/R-1/R-2/R-3 closures + Cat-A-conditional promotion proposal.
