# 03_integration_and_new_open.md — G1 L-M-AUDIT Closure: Integration + Promotion Proposal + New Open Questions

**Session:** 2026-05-04 (W6 Day 1, mid-day, post-G3)
**Target (from `02_development.md` §10):** Integrate the G1 self-audit closure with the canonical structure; produce concrete T-L1-M canonical promotion proposal text; propose theorem_status.md update; record OP non-impact; collect new open questions; record prompt v2 notes.
**This file covers:** §1 Integration with canonical (T-L1-M new entry text); §2 theorem_status.md update proposal (C-0722 row); §3 Integration with G3 ε-convention amendment + with T-L1-F empirical claim; §4 OP non-impact statement; §5 Integration with W6 strategic plan + CV-1.6 release scheduling; §6 New open questions surfaced; §7 Prompt v2 candidate notes.
**Depends on reading:** `01_exploration.md` §1–§3 (problem framing); `02_development.md` §1–§10 (full self-audit + R-0/R-1/R-2/R-3 closures + Cat-A-conditional self-classification); `THEORY/canonical/canonical.md` §13 T-L1-F entry (lines 1482-1489) — anchor for placement; `THEORY/canonical/theorem_status.md` (existing theorem registry); `THEORY/logs/daily/2026-05-04/g3_03_integration_and_new_open.md` §1 (G3 Commitment 16 amendment proposal — affects Theorem L-M's $\epsilon$ usage).

---

## §1. Integration with Canonical (T-L1-M Promotion Proposal)

### §1.1 Where T-L1-M sits in the canonical structure

T-L1-M (Soft-Count Corollary under $\Phi_{\mathrm{res}}$) is downstream of T-L1-F (CV-1.5.2 Cat A conditional). It does not modify any canonical theorem. It **adds** a new theorem (T-L1-M) to canonical §13 Cat A.

If promoted (per the user's promotion decision; this session does not write to canonical/), T-L1-M would naturally sit in `canonical.md` §13 directly after T-L1-F's entry (line 1489). This keeps the L1 chain together: T-L1-F (hard count bridge) immediately followed by T-L1-M (soft count corollary). Both are conditional Cat A under the same $(P0)$–$(P11)$ regime, with T-L1-M adding the envelope class restriction.

### §1.2 Proposed T-L1-M canonical entry text (NOT yet to be applied — proposal only)

After line 1489 (end of T-L1-F entry), insert:

```markdown
**T-L1-M. Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F.** *(New, 2026-05-04 W6 D1 G1-AUDIT closure; CV-1.6 promotion target after external L-M-K-style audit + user-supervised canonical merge.)*
Let $G,\mathbf u,U,A^\varepsilon,K_{\mathrm{act}}^\varepsilon,K_{\mathrm{soft}}^\phi$ be as in T-L1-F. Let $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ denote the class of envelopes $\phi:[0,1]\to[0,1]$ satisfying axioms F1 (range), F2 ($\phi(0)=0$), F3 (monotonicity), F4 (sub-threshold suppression: $\phi(\ell)\le\varepsilon_{\mathrm{sub}}^\phi$ on $[0,\ell_{\min}-\tau]$), F5 (dominant retention: $1-\phi(\ell)\le\varepsilon_{\mathrm{dom}}^\phi$ on $[\ell_{\min}+\tau,1]$). Set $\tau_*^{\mathrm{post-R2}}:=\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{bg}},r_{\mathrm{birth}})$. Under T-L1-F's $(P0)$–$(P11)$ and $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ with $\tau\in(0,\tau_*^{\mathrm{post-R2}})$,
$$|K_{\mathrm{soft}}^\phi(U(\mathbf u))-K_{\mathrm{act}}^\varepsilon(\mathbf u)|\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau)+\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot K_{\mathrm{act}}^\varepsilon(\mathbf u).$$
*Proof:* L-M-1 (envelope-pure inequality, triangle decomposition over three-region bar partition) + L-M-2 post-repair (edge-band emptiness derived from P5 + P6 + P8 + P9 + P11 + (P0) + L1-H2 Lemma 1 + CSEH 2007 bottleneck stability with factor-2 sharpness verified) + T-L1-F substitution. Per-family corollaries: $\phi=\phi_{\mathrm{hard}}$ EXACT; $\phi=\phi_{\mathrm{logistic}}^s$ ($s\ge 50$) bound $\le 3e^{-s\tau}\cdot K_{\mathrm{act}}^\varepsilon$; $\phi=\phi_{\mathrm{shift\text{-}sat}}^\beta$ ($\beta\ge 20$) bound $\le e^{-\beta\tau}\cdot K_{\mathrm{act}}^\varepsilon$. *(W5 Day 7 logs/daily/2026-05-03/02_L1M_proof_development.md; W6 D1 G1-AUDIT closure logs/daily/2026-05-04/02_development.md; working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md after user promotion.)*
*Status:* **Proved**, Cat A *conditional under the L1-J regime package $(P0)$–$(P11)$ + $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ + $\tau<\tau_*^{\mathrm{post-R2}}$*. NOT a global identity. Does NOT solve OP-0005 (K-Selection) or OP-0008 ($\sigma^A$ K-jump non-determinism). Does NOT promote $\Phi_{\mathrm{res}}$ to a canonical envelope class beyond its working role; reservoir-admissible families restricted to WQ-LAT-1.B-empirically-supported sub-classes (hard, logistic $s\ge 50$, shift-sat $\beta\ge 20$). $\tau_*^{\mathrm{post-R2}}$ uses $\rho_{\mathrm{bg}}$ (per W6 D1 G1-AUDIT R-2 closure: §5.5 Type-B chain replaced with explicit P5-direct derivation; original $\rho_{\mathrm{res}}$ replaced with $\rho_{\mathrm{bg}}$). External L-M-K-style audit recommended before canonical merge (analogous to L1-K external audit that preceded T-L1-F's CV-1.5.2 promotion).
```

### §1.3 Important — this is NOT applied

Per prompt §8.1 hard constraint, `canonical/*.md` writes are forbidden in this session. The above is a *proposal* for the user's promotion decision (analogous to G3 deep-dive's Commitment 16 amendment proposal). Actual canonical merge is a CV-1.6 release activity (which is **deferred** per W6 plan §2 explicit non-goals — release date determined separately).

### §1.4 Pre-promotion: external L-M-K-style audit recommended

Per `02_development.md` §9.2 audit-independence acknowledgement: this G1 closure is a self-audit. Before canonical promotion, an external L-M-K-style audit (general-purpose subagent dispatch, ~7-15 min) is recommended to provide independent verification — analogous to the L1-K external audit + L1-K-REPAIR cycle that preceded T-L1-F's CV-1.5.2 promotion.

This pre-promotion audit can be Day 2-3 work or deferred to the eventual CV-1.6 release packet preparation.

---

## §2. theorem_status.md Update Proposal

### §2.1 New row in Active Claims table (proposal)

Add the following row to the Active Claims / Resolved Claims table in `theorem_status.md` (around line 178-198, after the C-0716 T-σ-Theorem-4 row):

```
| **C-0722** | T-L1-M Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F | (proposed) | A conditional | A | P-0722 | (theoretical via L-M-1 + L-M-2 post-repair + T-L1-F substitution; WQ-LAT-1.B empirical anchor on $T^2_{20}$ with K_field ∈ {3,4,6,8,12} for envelope sub-class verification: φ_hard exact, φ_logistic^{100} ~10^{-3}, φ_shift-sat^{20} ~10^{-2}) | New 2026-05-04 W6 D1 G1-AUDIT closure. Cat-A-conditional under (P0)–(P11) + φ ∈ Φ_res(ℓ_min, τ) + τ < τ_*^{post-R2} = min(2ρ_pert, ρ_bg, r_birth). Per-family corollaries L-M.A (hard) Cat A absolute, L-M.B (logistic s≥50) + L-M.C (shift-sat β≥20) Cat A conditional inheriting Theorem L-M. NOT a global identity. Does NOT solve OP-0005 or OP-0008. Pre-promotion external L-M-K-style audit recommended. |
```

### §2.2 CV-1.6 release-version-history entry (proposal, deferred)

If T-L1-M is promoted at CV-1.6 release (W6 D7 or W7+), add the following to the release history section:

```markdown
### Canonical Spec v1.6 (TBD) — W6+: T-L1-M Soft-Count Corollary

**Additions over v1.5.2** (W6, TBD):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-L1-M** | Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F | accepted | A (conditional under L1-J + $\Phi_{\mathrm{res}}$ + $\tau < \tau_*^{\mathrm{post-R2}}$) | C-0722 | P-0722 | (theoretical; WQ-LAT-1.B empirical anchor) | [...] |

**v1.5.2 → v1.6 release notes (TBD)**: 1 new C-ID (T-L1-M Cat A conditional) + Commitment 16 ε-convention amendment per G3 D1 verdict (R1 reading: $\bar m = M / K_{\mathrm{field}}$). Counts: 46A → **47A**, 61 → **62 claims**, 75% → 75% fully proved.
```

This is a CV-1.6 release activity, **deferred** per W6 plan §2 explicit non-goals.

### §2.3 No status changes to existing entries

T-L1-F (C-0721) status preserved (Cat A conditional, unchanged). All other Cat A / B / C / R entries unaffected.

---

## §3. Integration with G3 ε-Convention + T-L1-F Empirical Claim

### §3.1 G3 deep-dive impact on T-L1-M's $\epsilon$ usage

The G3 deep-dive (`g3_*.md`) proposed a Commitment 16 amendment making the $\bar m = M / K_{\mathrm{field}}$ reading (R1) explicit. T-L1-M's hypothesis package inherits T-L1-F's $(P0)$–$(P11)$, which uses $\epsilon$ via the K_act definition in Commitment 16. Under the post-G3 amendment, $\epsilon$ in T-L1-M's $K_{\mathrm{act}}^\epsilon$ is well-defined as $0.01 \cdot M / K_{\mathrm{field}}$ (e.g., 0.225 for the standard $T^2_{20}$ regime $M=90, K_{\mathrm{field}}=4$).

T-L1-M's empirical anchor (WQ-LAT-1.B reservoir-resolution sweep on $T^2_{20}$) was computed at $\epsilon = 0.225$ (consistent with R1). The G3 amendment makes this explicit upstream; no separate edit to T-L1-M's empirical-anchor parenthetical needed.

### §3.2 G1 Cat-A-conditional inherits T-L1-F's empirical regime

T-L1-F's "439/1920 = 22.9% feasible on $T^2_{20}$" empirical anchor establishes that the L1-J regime $(P0)$–$(P11)$ is non-empty. T-L1-M's Cat-A-conditional status inherits this empirical regime — i.e., for parameter configurations within the L1-I FEASIBLE_WITH_BUDGET set, T-L1-M holds.

The post-R2 $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$ uses $\rho_{\mathrm{bg}}$ (from P5) instead of $\rho_{\mathrm{res}}$ (from P10).

> ***(Erratum, W6 D1 late re-review per `op_resolution.md` §9.7 + §13.6)***: An earlier draft of this paragraph claimed "$\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ in general, so $\tau_*^{\mathrm{post-R2}} \ge \tau_*$ — the post-R2 admissible $\tau$ range is at least as wide as the pre-repair range." **This is incorrect.** The relationship is **configuration-dependent**:
> - $\rho_{\mathrm{bg}}^{\mathrm{actual}} = \ell_{\min} - \|U\|_{\infty, X_{\mathrm{bg}}}$ (P5 form, restricted to $X_{\mathrm{bg}}$).
> - $\rho_{\mathrm{res}}^{\mathrm{actual}} = \ell_{\min} - \|R_{\mathrm{inact}}\|_\infty$ (P10 form, **global** over the full graph, not just $X_{\mathrm{bg}}$).
> - Since $\|U\|_{\infty, X_{\mathrm{bg}}} \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$ (active-slot decay tails add to $U|_{X_{\mathrm{bg}}}$ via P7), and $\|R_{\mathrm{inact}}\|_\infty \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$ (global $\ge$ restricted), neither $\rho_{\mathrm{bg}}^{\mathrm{actual}}$ nor $\rho_{\mathrm{res}}^{\mathrm{actual}}$ generically dominates the other.
>
> **Corrected reading:** the comparison $\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ is **configuration-dependent** (NQ-G1-1, deferred to NQ-G1-1-ext W7+ for empirical anchor via L1-I extension recording $\|R_{\mathrm{inact}}\|_\infty$ separately). The post-R2 derivation gains theoretical clarity (P5 direct on $U$, no implicit T-L1-F LG-7 dependency) at potentially the cost of a slightly tighter or wider $\tau$ range depending on configuration. **Cat A conditional self-classification of Lemma L-M-2 is unaffected**: the lemma states "edge band empty for $\tau \in (0, \tau_*^{\mathrm{post-R2}})$" which holds regardless of which of $\rho_{\mathrm{bg}}, \rho_{\mathrm{res}}$ is the binding constraint. Net trade-off accepted for canonical promotion (post-R2 derivation more honest about regime structure).

### §3.3 Existing canonical theorems: relation to T-L1-M

| Canonical theorem | Cat | Relation to T-L1-M |
|---|---|---|
| **T-L1-F** (CV-1.5.2) | A conditional | **T-L1-M depends directly on T-L1-F** for $K_{\mathrm{bar}}^{\ell_{\min}} = K_{\mathrm{act}}^\varepsilon$ substitution + $\mathcal A_{\mathrm{bar}}$ bijection. T-L1-M extends T-L1-F from integer to real-valued count. |
| **QM3** (Q_morph continuity via persistence stability) | A | **Same CSEH 2007 anchor** as L-M-2's bottleneck-stability use (R-1 closure). |
| **T11** (Γ-convergence) | A | **No direct interaction.** |
| **T-PreObj-1** | A | **No direct interaction.** Single-formation; T-L1-M is multi-formation. |
| **T-Persist-K-Sep / Weak / Unified** | C | **No direct interaction.** Persistence K-formation theorems; T-L1-M is field-level diagnostic. Future interaction: T-L1-M as smooth diagnostic for persistence-K-events. |
| **Commitment 16** (K_field/K_act two-tier) | A | **T-L1-M operates strictly within Layer II** ($K_{\mathrm{act}}^\varepsilon$). T-L1-M does not extend the K-status decomposition; it adds a real-valued sibling to $K_{\mathrm{act}}^\varepsilon$ at the same layer. The G3 amendment (Commitment 16 line 810 R1 reading) is upstream and inherited. |
| **T-Bind-Proj / T-Bind-Full** (Cat A post-evening-G2) | A | **No direct interaction.** Different theorem family. |

T-L1-M does not modify, weaken, or contradict any existing canonical theorem.

---

## §4. OP Non-Impact Statement

This G1 closure:
- Does **not** affect OP-0001 (F-1), OP-0002 (M-1), OP-0003 (MO-1) — orthogonal layer.
- Does **not** affect OP-0005 (K-Selection) — does not address the K mechanism; T-L1-M operates on already-determined K-field state.
- Does **not** affect OP-0008 ($\sigma^A$ K-jump non-determinism) — T-L1-M strictly within $(P0)$–$(P11)$ resolved regime; K-jump events lie outside.
- Does **not** affect OP-0009 (Multi-Formation Ontological Foundations) sub-items — operates within Commitment 16 K-status decomposition. **OP-0009-F partially clarified** (T-L1-M provides smooth real-valued diagnostic at field level; cf. G3 deep-dive's NQ-G3 family).
- Does **not** affect OP-0006, OP-0010, OP-0011, OP-0012, OP-0013 — unrelated layers.
- **N-1 (Soft-Hard Switching Asymmetry):** preserved. T-L1-M honors N-1 by keeping $K_{\mathrm{soft}}^\phi$ (real) vs $K_{\mathrm{act}}^\varepsilon$ (integer) as **distinct objects with explicit relationship**, not identifying them.

**No silent OP resolution.**

---

## §5. Integration with W6 Strategic Plan + CV-1.6 Release Scheduling

### §5.1 W6 strategic plan G1 status update

`W6_strategic_plan.md` G1 (lines 18-30) targets:

> L-M-2 Cat-B sketched → Cat-A conditional via explicit closure of R-1/R-2/R-3, OR a deliberate retention at Cat-B with an explicit failure analysis.

This G1 closure produces the first option: Cat-A-conditional via R-0 + R-1 + R-2 + R-3 closures. Recommended W6 strategic plan §G1 status text revision (proposal):

```markdown
### G1 — L1-M-AUDIT (R-1 / R-2 / R-3 closure)

**Status (post W6 D1 G1-AUDIT closure):** L-M-2 Cat-B sketched → **Cat-A conditional** via explicit closure of R-0 (minor §2.2 wording) + R-1 (factor 2 sharp under L1-J via explicit perturbation) + R-2 (§5.5 Type-B chain explicit reproof using P5 direct) + R-3 (Type-N non-terminal clarification note). Self-audit deliverable at `logs/daily/2026-05-04/02_development.md`. Theorem L-M post-repair Cat A conditional under $(P0)$–$(P11) + \Phi_{\mathrm{res}} + \tau < \tau_*^{\mathrm{post-R2}}$ where $\tau_*^{\mathrm{post-R2}} := \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$ (uses $\rho_{\mathrm{bg}}$ post-R2). Per-family corollaries: L-M.A absolute, L-M.B/L-M.C conditional inheriting.

**Pre-promotion:** external L-M-K-style audit recommended (~7-15 min agent dispatch). Canonical promotion = CV-1.6 release activity (deferred per §2 explicit non-goals).

**Estimated effort:** ✅ closed Day 1 (0 day vs original 3-4 day estimate). Day 4-5 budget freed.

**Priority:** P0 (must) — CLOSED.
```

This is a **proposal for the user's edit** — this session does not write to weekly/.

### §5.2 CV-1.6 release feasibility update

W6 strategic plan §2 declared "CV-1.6 release deferred until G1 + G2 + G3 close." With G1 + G2 + G3 all closed Day 1:
- G1: ✅ this session.
- G2: ✅ Day 1 evening (CHANGELOG).
- G3: ✅ Day 1 mid-day post-reset (g3_* deep-dive proposals; user-supervised promotion ~30 min).

**CV-1.6 release blocker (G1 + G2 + G3 closure) is removed.** CV-1.6 release becomes a candidate for W6 D7 EOD or W7+ scheduling, conditional on:
- User-supervised promotion of G2 canonical edits (already applied per evening session) + G3 Commitment 16 amendment + T-L1-M new entry.
- Pre-promotion external L-M-K-style audit (per §1.4 above).
- W6 D6 G4 parking-lot inventory completion (per W6 strategic plan §3 daily breakdown).
- W6 D7 weekly_summary.md draft.

**Net:** CV-1.6 release goes from "deferred indefinitely" (per W6 plan §2) to "**candidate for W6 D7 EOD release**, pending external audit + G4 + weekly_summary."

### §5.3 Day 2-7 schedule revision (proposal)

Given G1 + G2 + G3 all closed Day 1:

| Day | Original W6 plan §3 | Revised post-Day 1 G1 closure |
|---|---|---|
| Day 2 | G2 finish (already done evening Day 1) | G3 user-supervised promotion (Block 0, ~30 min) + T-L1-M user-supervised promotion (Block 1, ~30 min if no external audit, ~30 min + 15 min agent if external audit) + outstanding decisions cleanup (Block 2) + Day 3 plan |
| Day 3 | G3 ε-convention (already done Day 1 mid-day) | External L-M-K-style audit dispatch + verdict integration + T-L1-M repair if needed |
| Day 4 | G1 R-1 + R-2 (already done Day 1) | G4 parking-lot inventory acceleration (Day 6 task → Day 4) |
| Day 5 | G1 R-3 + Cat-A decision (already done Day 1) | (free / contingency) |
| Day 6 | G4 parking-lot inventory | (already done Day 4 if accelerated; otherwise per schedule) |
| Day 7 | weekly_summary | weekly_summary.md + CV-1.6 release packet preparation + release |

**Net:** 3 days of slack created by Day 1 over-delivery.

---

## §6. New Open Questions Surfaced

These are questions that G1 closure does *not* answer but became visible during execution. Each is 3-5 lines, candidate for future plan.md targets.

### NQ-G1-1. ρ_bg vs ρ_res in L1-I FEASIBLE configurations

**Question.** R-2 closure changed $\tau_*^{\mathrm{post-R2}}$ to use $\rho_{\mathrm{bg}}$ (from P5) instead of $\rho_{\mathrm{res}}$ (from P10). Whether $\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ or vice versa in the L1-I FEASIBLE_WITH_BUDGET set is empirically untested. If $\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ generically, $\tau_*^{\mathrm{post-R2}}$ is at least as wide as $\tau_*$; otherwise the post-R2 may shrink for some configurations.

**Severity.** Medium. Affects T-L1-M's regime characterization; informs CV-1.6 release packet.

**Connection.** Single re-run of `l1i_constants_feasibility.py` with explicit $\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ measurement per config; ~1-2 hours compute. Could be Day 4 work in the revised schedule (§5.3).

### NQ-G1-2. (P9-tight) regime experiment — would tighter perturbation budget recover factor 1?

**Question.** R-1 closure (§2 above) noted that "(P9-tight): $\|R_j\|_{\infty,N_j^r} \le \rho_{\mathrm{pert}}/4$" would tighten the Type-N bar bound to use $\rho_{\mathrm{pert}}/2$ instead of $\rho_{\mathrm{pert}}$, expanding $\tau_*$. Empirically: how often is the tighter bound (P9-tight) satisfied in the L1-I FEASIBLE configurations? If frequently, an L1-J' regime with (P9-tight) replacing P9 would give a tighter T-L1-M with wider $\tau_*$.

**Severity.** Low-Medium. Future regime tightening direction.

**Connection.** Re-run of `l1i_constants_feasibility.py` with $\rho_{\mathrm{pert}}/4$ instead of $\rho_{\mathrm{pert}}/2$ in P9; ~1-2 hours compute. W7+ NQ.

### NQ-G1-3. External L-M-K-style audit pre-promotion verdict

**Question.** This G1 closure is a self-audit (§9.2 acknowledgement). An external `l1m-k-audit-prover` agent dispatch (analogous to L1-K external audit pattern) would provide independent verification of R-0/R-1/R-2/R-3 closures + Cat-A-conditional self-classification. The external audit may identify additional refinements or confirm the self-audit verdict.

**Severity.** High (CV-1.6 promotion blocker if external audit disagrees substantively).

**Connection.** ~7-15 min agent dispatch + 1-2 hours verdict integration. Should be done before CV-1.6 release packet preparation. Day 2 morning Block 1 (per §5.3 revised schedule).

### NQ-G1-4. Per-formation $K_{\mathrm{soft}}^{\phi,(j)}$ vs aggregate $K_{\mathrm{soft}}^\phi(U)$

**Question.** T-L1-M provides $|K_{\mathrm{soft}}^\phi(U) - K_{\mathrm{act}}^\varepsilon(\mathbf u)|$ bound at the **aggregate** field level. Per-formation $K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)})$ may also be of interest (e.g., for per-formation persistence diagnostics). Is there a per-formation analog of T-L1-M? Specifically: under $(P0)$–$(P11)$, is $\sum_j K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)}) \approx K_{\mathrm{soft}}^\phi(U)$ within some bound?

**Severity.** Low-Medium. Connects to OP-0009-F (per-formation F vs aggregate F bridge).

**Connection.** Theoretical extension of L-M-2; would require analyzing the bar-type partition of $\mathrm{Dgm}_0^{\sup}(u^{(j)};G_j^r)$ vs $\mathrm{Dgm}_0^{\sup}(U;G)$ and bottleneck stability between them. W7+ extension.

### NQ-G1-5. $\Phi_{\mathrm{res}}$ axiomatic compactness

**Question.** Definition L-M-D1 has 5 axioms F1–F5. Are they all independent, or can some be collapsed? Specifically:
- F1 + F3 (with $\phi(0) = 0$ from F2) imply $\phi \le 1$ on $[0,1]$ if $\phi(1) \le 1$. Can F1's "$\phi \le 1$" upper bound be derived rather than postulated?
- F4 + F5 imply $\phi$ has a "soft step" near $\ell_{\min}$. Is there a 3-axiom reformulation $\{F2, F4, F5\}$ from which F1 and F3 follow under additional regularity?

**Severity.** Low. Cosmetic axiomatization.

**Connection.** Pure axiom-arithmetic exercise. Was NQ-L1M-4 in W5 D7's `03_L1M_canonical_integration_and_NQ.md`; preserved here.

### NQ-G1-6. T-L1-M extension to perturbation analysis (NQ-L1M-5 carry-over)

**Question.** T-L1-M states a *static* bound. For two states $\mathbf u_1, \mathbf u_2$ in the same regime, is there a quantitative bound on $|K_{\mathrm{soft}}^\phi(U_1) - K_{\mathrm{soft}}^\phi(U_2)|$ in terms of $\|\mathbf u_1 - \mathbf u_2\|$? This extends T-L1-M to perturbation analysis. (Was NQ-L1M-5 in W5 D7; preserved.)

**Severity.** Medium. Useful for future dynamics analysis.

**Connection.** `working/E/soft_K_definition.md` §2.2 Cor 2.2 gives $L_{K_{\mathrm{soft}}} \le 4 L_\phi n$ via CSEH bottleneck stability. Combined with T-L1-M's static bound, a triangle-inequality argument gives a perturbation bound on $|K_{\mathrm{act}}^\varepsilon(\mathbf u_1) - K_{\mathrm{act}}^\varepsilon(\mathbf u_2)|$ — non-vacuous only when right side $< 1$.

---

## §7. Prompt v2 Candidate Notes (per prompt §14)

The autonomous-execution prompt is intended as a reusable template. The following observations from this G1 closure session may inform a future v2:

### §7.1 Self-audit as a closure pattern

This session demonstrated a "self-audit" closure pattern (Approach A3 in `01_exploration.md` §2.3): the same Claude session that has been working in the directory acts as the audit teammate for its own (or earlier) work. This is faster than external dispatch and produces equivalent end-state when conversation memory + canonical access provide sufficient evidence. A future v2 might explicitly recognize this pattern and add: "If conversation memory + canonical access provide sufficient evidence for an audit-grade closure, consider self-audit (no external dispatch needed). Acknowledge audit non-independence in §9 of `02_development.md`."

### §7.2 File-naming for multi-deep-dive sessions

This session is the third deep-dive in one Day 1 (G3 first → G1 now). The G3 outputs were renamed `g3_*.md` to free 01/02/03/99 slots for G1. A future v2 might offer guidance: "If a Day session contains multiple deep-dives, use `<targetname>_NN_*.md` prefixed naming to preserve all deep-dives. The 01/02/03/99 slots without prefix represent the latest / primary deep-dive."

### §7.3 Pre-existing deferred-track work as input

This G1 self-audit drew on conversation-memory recall of (a) the deleted G2-OLD-plan CSEH analysis (R-1 pre-resolution), (b) the deleted G1 audit verdict (R-2/R-3/R-0 specifications). A future v2 might note: "Conversation memory of deleted-but-substantive work can be re-derived by self-audit. Flag the re-derivation explicitly in §9 audit-independence acknowledgement."

### §7.4 Diagnostic-first → self-audit pipeline

The G3 deep-dive used diagnostic-first (A4); this G1 closure uses self-audit (A3). Both are diagnostic-style approaches that surface assumptions before committing to a decision rule. A future v2 might generalize: "Diagnostic-style approaches (A4 diagnostic-first; A3 self-audit) are often appropriate when the question's *premise* is itself uncertain or the work is a closure/verification rather than open exploration."

### §7.5 Multi-deep-dive Day 1 pattern

This session is the third deep-dive on Day 1 (G3 → G1 sequential, both substantive). The user's invocation pattern (re-invoke autonomous prompt after each deep-dive completes) suggests a "multi-target Day 1" workflow that the original template did not anticipate. A future v2 might offer two modes:
- **Single-deep-dive mode** (current template): one target per Day, files 01/02/03/99 fixed.
- **Sequential-deep-dive mode**: multiple targets per Day, prefixed files (e.g., `g3_*`, `g1_*`) with the unprefixed 01/02/03/99 representing the latest. `99_summary.md` rolls up the day's full work across all deep-dives.

---

**End of `03_integration_and_new_open.md`. Cat-A-conditional T-L1-M canonical promotion proposal documented; theorem_status.md C-0722 row drafted; CV-1.6 release feasibility upgraded from "deferred indefinitely" to "candidate for W6 D7 EOD"; 6 new open questions; 5 prompt v2 notes.**

**Next file:** `99_summary.md` — Day 1 EOD overall (across G3 + G1 deep-dives + evening G2 + morning audit) + Day 2 seed.
