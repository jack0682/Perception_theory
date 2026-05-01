# 03_t_sigma_theorem4_reconciliation.md — T-σ-Theorem-4 Red Lane Reconciliation Note

**Session:** 2026-05-01 (W5 Day 5)
**Block:** 2 (T-σ-Theorem-4 Red Lane, 11:00-13:00)
**Target (from plan.md):** Convert the T-σ-Theorem-4 3-way A_2/A_1 ambiguity (2/3 vs 4 vs 8) into a cleanly bounded audit lane with γ/β/α paths owned and assigned to W6 D1-D3 working files. **No canonical edits today. No new ε-expansion attempts. No "saving" Cat A re-promotion.**
**This file covers:** plan.md §3 Block 2 (11:00-11:45 read three red-source packets; 11:45-12:30 separate audit paths; 12:30-13:00 reconciliation note).
**Depends on reading:** `working/SF/sigma_theorem4_higher_order.md` (819 lines, revised pivot), `working/SF/sigma_theorem4_canonical_revision.md` (338 lines, post-EOD Task #63), `working/SF/nq187b_L_extrapolation.md` (422 lines, post-EOD α-path), `2026-04-30/11_nq187_scaling_test_results.md` (numerical), `2026-04-30/13_wave3_critical_findings.md` §1 + §10, canonical.md §13 T-σ-Theorem-4 (lines 1377-1413, current Cat B).

---

## §1. Precise Statement of the Discrepancy

### §1.1 What canonical T-σ-Theorem-4 currently claims

Per CV-1.5.1 frozen text (`canonical.md` §13 lines 1377-1413), T-σ-Theorem-4 is **Cat B retroactive** with the following load-bearing claim at leading order:

$$\mu_0 = 4|W''(c)|\,\epsilon + O(\epsilon^{3/2}), \qquad \mu_1 = (A_2/A_1)\,|W''(c)|\,\epsilon + O(\epsilon^{3/2}),$$

with **continuum claim** $A_2/A_1 = 4$ (sourced to `working/SF/symmetry_moduli.md` §3.3, R22 working file) ⇒ leading-order degeneracy $\mu_0 = \mu_1 = 4|W''(c)|\,\epsilon$. The σ-tuple at first pitchfork on $D_4$ free-BC inherits this degeneracy and is broken only by Commitment 14 (O7) Mulliken tie-break on irrep label (trivial $A_1$ before sign $A_2$).

### §1.2 The three sources of disagreement

| Source | Reported $A_2/A_1$ | Convention | File / artifact |
|---|---:|---|---|
| **Continuum naive integral** (post-EOD op-0008-architect closed-form) | **2/3 ≈ 0.667** | Standard $L^2$-normalized continuum eigenmodes; ratio of $A_2 = \int \phi_{(1,0)}^2 \phi_{(0,1)}^2$ over $A_1 = \int \phi_{(1,0)}^4$ | `working/SF/nq187b_L_extrapolation.md` §2.5 + §2.6 closed-form trigonometric identity |
| **R22 working-file claim** | **4** | Asserted (un-derived) on $D_4$ free-BC grid | `working/SF/symmetry_moduli.md` §3.3 |
| **NQ-187 numerical *implied*** | **≈ 8** | Derived from observed $\mu_1/\mu_0 \to 2$ asymptotically + assumed canonical $\mu_0 = 4|W''(c)|\epsilon$ → effective $A_2/A_1 = 4 \cdot (\mu_1/\mu_0) = 8$ | `CODE/scripts/test_sigma_theorem4_scaling.py` + `results/sigma_theorem4_scaling.json` ($L \in \{4, 8, 16\}$, $p_{16} = 1.03$) |

This is **three sources, not one**. The observed gaps:
- naive vs R22: factor **6** (2/3 vs 4).
- naive vs numerical-implied: factor **12** (2/3 vs 8).
- R22 vs numerical-implied: factor **2** (4 vs 8).

### §1.3 Adjacent numerical content

Direct power-law fits per L (`11_nq187_scaling_test_results.md` §2.3):
- $L = 4$: $p = 0.925 \pm 0.031$ (small-L regime).
- $L = 8$: $p = 0.970 \pm 0.022$ (clean).
- $L = 16$: $p = 1.028 \pm 0.014$ (clean).

→ exponent **converges to $p = 1$** as $L$ grows; rejects both §3.2 polynomial-equivariant ($p = 2$) and §5 alternative ($p = 3/2$) hypotheses. Confirms **leading-order non-degeneracy** at finite L.

Discrete-grid $A_2/A_1$ ratio direct closed-form (`nq187b_L_extrapolation.md` §2.6 table):

| L | $A_2^L/A_1^L$ |
|---|---:|
| 4 | 0.80 |
| 8 | 0.762 |
| 16 | 0.703 |
| 32 | 0.668 |
| 64 | 0.659 |
| **L → ∞ extrapolation** (1/L² fit) | **≈ 0.667 = 2/3** |

→ Naive convention C1 (eigenmodes $\phi_{(p,q)} = \cos((p)(i+1/2)\pi/L) \cos((q)(j+1/2)\pi/L)$, no L²-normalization or with normalization that cancels) gives convergent value **≠ R22's claimed 4**.

---

## §2. What Stays Safe Today (preserved)

The following **do not change** as a result of the 3-way mismatch:

1. **T-σ-Theorem-4 Cat B retained** (already retroactive at CV-1.5.1 per Critic 7-agent verdict 2026-04-29). Wave 3 audit *augments* the caveat without further downgrade.
2. **σ-tuple definition (Commitment 14)** unchanged. The σ-tuple is well-defined regardless of $A_2/A_1$ value; only the *plateau* (degenerate vs non-degenerate first two entries) depends on the ratio.
3. **Commitment 14 (O7) tie-break convention** vacuously satisfied at finite L (no degeneracy → no tie to break). Tie-break necessity emerges only in continuum limit *if* $A_2/A_1 = 4$ holds.
4. **σ-locality (Bridge B-2 Schramm reframing)** independently verified on 3 graph classes (R23 D_4 free-BC L=8 / Z_n cycle n=20 / Z_n × Z_n torus n=10) per `CODE/scripts/results/sigma_locality_R23_cycle_torus.json`. T-σ-Theorem-4 caveat does **not** propagate to T-PreObj-1G Schramm-restatement.
5. **Numerical anchors for sibling theorems** (T-σ-Theorem-3 closed-form on uniform, T-σ-Lemma-1/2/3) all unaffected — these operate on uniform $u = c\mathbf{1}$ or general structural facts, not on the first-pitchfork plateau.

→ Cluster of σ-framework Cat A entries (T-σ-Lemma-1/2/3 + T-σ-Theorem-3) at CV-1.5.1 is **not destabilized** by the T-σ-Theorem-4 finding.

---

## §3. Three Audit Paths (γ / β / α)

Day 5 confirms the partition introduced in `sigma_theorem4_canonical_revision.md` §4 and `pre_brainstorm.md` §3, with explicit owners and W6 handoff dates.

### §3.1 γ path — Σ_m-Hessian convention audit

**Question**: Is the conversion from ambient $\mathbb{R}^n$ Hessian to the Σ_m-tangent Hessian (the "absorption derivation" in NQ-187 §2.1) using the right normalization?

**Specifically**: two common conventions in the simplex-projected Hessian literature:
- *Convention I (centered)*: project gradient + Hessian onto tangent simplex; eigenvalues are intrinsic to Σ_m geometry.
- *Convention II (Lagrange)*: extrinsic reduction via Lagrange multipliers; eigenvalues include constraint-multiplier contributions.

These differ by factors of order unity in some cases — exactly the kind of factor that could explain the 4× gap between canonical $\mu_0 = 4|W''(c)|\epsilon$ and numerical $\mu_0 = \epsilon|W''(c)|$.

**Why first priority**: if the comparison quantities ($\mu_0$ canonical vs $\mu_0$ numerical) are mismapped at the convention level, then the apparent disagreement is *partially artificial*. Day 5 should remove artificial disagreement before studying genuine disagreement.

**Owner (W6 handoff)**: NEW W6 D1-D3 working file `working/SF/sigma_m_hessian_convention_audit.md` (3-5 days effort per `sigma_theorem4_canonical_revision.md` §4.3).

**W6 D1 immediate action**: compute $\mu_0, \mu_1$ via both conventions on $L = 4$ small grid (16 sites; exact symbolic via SageMath or numpy + analytic formulas); compare ratio. If conventions disagree by exactly factor 4, γ-path explanation holds.

**Cat target**: Cat A (elementary symbolic algebra; either reproduces canonical with one convention or identifies the convention error).

### §3.2 β path — R22 cubic-equivariant derivation audit

**Question**: Is R22's claim $A_2/A_1 = 4$ on $D_4$ free-BC grid correct?

**Already-found evidence (must not be over-claimed today)**: post-EOD direct discrete-grid computation (`nq187b_L_extrapolation.md` §2.5 closed-form + §2.6 table) under naive convention C1 gives $A_2/A_1 \to 2/3$ as $L \to \infty$ — which is *prima facie* incompatible with R22's 4. **However**, this is provisional: R22 may use a different convention (C3 mass-conservation simplex projection or C4 W-potential expansion coefficients per `nq187b_L_extrapolation.md` §3.2) that produces a different value. Until R22's exact convention is pinned down by audit, the R22 claim cannot be rejected on this evidence alone.

**Why second priority**: β-path has *more pre-existing evidence* than γ-path (the 2/3 closed-form is concrete). However, β-path requires *re-deriving* the entire R22 cubic-equivariant computation from first principles to identify which convention R22 invoked — a 1-2 week task, not a 3-5 day audit. Higher cost, more pre-evidence.

**Owner (W6 handoff)**: NEW W6 D4-W7 working file `working/SF/r22_a2_a1_audit.md` (1-2 weeks effort).

**Required audit steps** (per `sigma_theorem4_canonical_revision.md` §4.2):
- Cubic-invariant computation $A_1 = \int \phi_{(1,0)}^4$, $A_2 = \int \phi_{(1,0)}^2 \phi_{(0,1)}^2$ — symbolic algebra check under each candidate convention C1/C2/C3/C4.
- Discrete vs continuum: free-BC grid eigenmodes are discrete cosines $\cos((2k-1)\pi/(2L))$; products / integrals discretize differently from continuum.
- Cross-check: does R22's 4 follow from any of C1/C2/C3/C4? If yes, β-path identifies the convention; if no, R22 contains an error.

**Cat target**: Cat A or strong Cat B (symbolic + numerical cross-check; identifies error if present).

### §3.3 α path — finite-L vs continuum extrapolation audit

**Question**: Does $\mu_1/\mu_0$ from NQ-187 numerical (currently 2 at $L = 16$) trend toward a limit at $L \to \infty$, and which?

**Already-found evidence (post-EOD `nq187b_L_extrapolation.md` §5)**: three competing predictions for the L → ∞ limit:
- α-naive: $\mu_1/\mu_0 \to 1/6$ (if naive 2/3 convention applies and canonical formula μ_0 = 4|W''(c)|ε is right ⇒ ratio = (A_2/A_1)/4 = 1/6).
- R22-continuum: $\mu_1/\mu_0 \to 1$ (degenerate; canonical claim).
- saturation: $\mu_1/\mu_0$ stays at 2 for all L (no continuum limit recovers canonical value).

The current $L = 16$ value is 2; the *finite-L extrapolation only*, without convention disambiguation, cannot discriminate between R22-continuum (which predicts decreasing trend toward 1) and saturation (constant 2). Any of the three predictions is consistent with measurements at $L \leq 16$.

**Why third priority (lowest)**: α-path is *confirmatory* rather than *causal*. Without γ + β closing first, α extrapolation alone produces ambiguous values. Furthermore, NQ-187 extension to $L = 32, 64$ requires substantial Lanczos compute (~10-30 hours) — expensive *and* indirect.

**Owner (W6 handoff)**: existing post-EOD `working/SF/nq187b_L_extrapolation.md` (already drafted at 422 lines) + NEW companion `CODE/scripts/nq187b_a2_a1_extrapolation.py` (per the file's §6.1 outline) + W6 D4-W7 NQ-187 extension via `CODE/scripts/nq187b_mu_extrapolation.py` (§6.2).

**W6 D3 immediate action**: execute `nq187b_a2_a1_extrapolation.py` (< 1 hour compute) to formalize the discrete $A_2/A_1$ extrapolation under naive convention C1. Compare against γ-path convention finding from W6 D1.

**Cat target**: Cat A for closed-form (already drafted); Cat B target for extension to $L = 32, 64$.

### §3.4 Priority ordering and rationale

| Path | Priority | W6 handoff | Effort | Cat target |
|---|---|---|---|---|
| γ Σ_m-Hessian convention | 🥇 first | W6 D1-D3 (`sigma_m_hessian_convention_audit.md` NEW) | 3-5 days | Cat A |
| β R22 derivation | 🥈 second | W6 D4-W7 (`r22_a2_a1_audit.md` NEW) | 1-2 weeks | Cat A or strong Cat B |
| α L → ∞ extrapolation | 🥉 third | W6 D3 direct (existing `nq187b_L_extrapolation.md` + script) + W6 D4-W7 numerical extension | 1 hour direct + 10-30 hours extension | Cat A direct + Cat B target extension |

**Why γ first** (per `pre_brainstorm.md` §3.3): the γ-path question has the smallest scope (one convention check), the highest probability of resolving the apparent factor-4 discrepancy in $\mu_0$ alone, and removes the risk of conducting α + β under a mis-specified comparison. **Day 5 is not for γ-path execution**; only for owner assignment.

**Combined convergence target**: if γ + β + α all close to consistent values, T-σ-Theorem-4 Cat A re-promotion candidate at **CV-1.7+** (per `sigma_theorem4_canonical_revision.md` §8.4); not CV-1.6.

---

## §4. CV-1.6 Caveat Wording (provisional, no canonical edit today)

The CV-1.6 release narrative (W6 D7 EOD) needs one sentence about T-σ-Theorem-4. **Default expectation: caveat addition, NOT Cat A re-promotion.**

### §4.1 Provisional caveat text (do NOT apply to canonical today)

For consideration at W6 D6-D7 packet finalize (after γ-path audit at minimum closes):

> **T-σ-Theorem-4 (ii) finite-L caveat (CV-1.6 candidate — text proposal only).** Numerical scaling test on $L \in \{4, 8, 16\}$ (`CODE/scripts/test_sigma_theorem4_scaling.py`, W5 Day 4) measures $\mu_0 = \epsilon|W''(c)|$, $\mu_1 = 2\epsilon|W''(c)|$ asymptotically with power-law $p = 1.03 \pm 0.014$ at $L = 16$, contradicting the leading-order degeneracy $\mu_0 = \mu_1 = 4|W''(c)|\epsilon$ predicted by the canonical formula with $A_2/A_1 = 4$. Three reconciliation paths registered: (γ) Σ_m-Hessian convention audit (highest priority, W6 D1-D3), (β) R22 cubic-equivariant ratio derivation audit (W6 D4-W7), (α) finite-L vs continuum extrapolation (W6 D3 direct + W6 D4-W7 numerical extension). **Cat A re-promotion deferred to CV-1.7+**, conditional on γ + β + α closing to a consistent value.

### §4.2 Conditional decision rule for CV-1.6 release

- **If γ-path closes by W6 D5** with a clean convention error explanation → caveat text adopts γ-finding inline; T-σ-Theorem-4 Cat B retained with augmented caveat; CV-1.6 release on schedule.
- **If γ-path is inconclusive by W6 D5** → caveat text uses §4.1 provisional wording above; T-σ-Theorem-4 Cat B retained with three-path uncertainty caveat; CV-1.6 release on schedule.
- **If γ-path identifies a deeper structural problem requiring T-σ-Theorem-4 Cat C downgrade** → CV-1.6 release narrative re-thinks the SF Round 1-5 P4 packet item; possible CV-1.6 deferred 1 week; user decision required.

→ **Default expectation**: scenario (b) — caveat addition, no canonical Cat A re-promotion attempt; release on schedule.

---

## §5. What Day 5 Can Promote (and What Can't)

### §5.1 Can promote today

**Nothing** to canonical. Day 5 canonical edit count target = 0 per plan.md §5 + Day 4 anti-drift discipline.

The following may move forward at the *working-file* level (not canonical):
- This reconciliation note is itself a working artifact (in `logs/daily/2026-05-01/`); no canonical edit.
- W6 D1-D3 working file *targets* (`sigma_m_hessian_convention_audit.md`, `r22_a2_a1_audit.md`) are *named* but not *created* today. Owner assignment is the deliverable.

### §5.2 Cannot attempt today (hard list)

- **Canonical edits to T-σ-Theorem-4**: forbidden per plan.md §5 + §9.
- **New ε-expansion derivation attempts**: explicitly forbidden per plan.md §3 Block 2 §12:30-13:00 list item 6.
- **"Saving" Cat A re-promotion via a fresh Day 5 derivation**: forbidden per same.
- **Treating NQ-187b L-extrapolation finding (post-EOD, 422 lines) as resolution rather than as α-path input**: forbidden per `pre_brainstorm.md` §3.4.
- **Modifying Commitment 14 (O7) tie-break convention text in canonical**: forbidden (already correctly states tie-break is *vacuously satisfied* at finite L; no edit needed today).
- **Cross-cluster propagation**: σ_rich (Commitment 18 candidate, CV-1.7 parking lot) + K-Selection (Commitment 19 candidate, CV-1.7 parking lot) are **not affected** by T-σ-Theorem-4 finding per `sigma_theorem4_canonical_revision.md` §6.1-§6.2. No Day 5 propagation of T-σ-Theorem-4 caveat into these clusters.

---

## §6. Risk Watch (preserved into W6)

### §6.1 Risk — γ-path "fixes" the convention but produces an even worse-looking T-σ-Theorem-4

If γ-path discovers that the canonical convention was correct but R22's $A_2/A_1 = 4$ is still wrong, then Day 4's apparent disagreement structure changes: the issue moves from "convention map" (artificial) to "derivation error" (real). This shifts T-σ-Theorem-4 from Cat B with finite-L caveat → Cat C requiring substantive rework.

**Mitigation**: γ-path execution must compute *both* canonical $\mu_0 = 4|W''(c)|\epsilon$ derivation (under the canonical convention) and the corresponding consistent $\mu_1$ formula on the same convention. If both come out to numerical-matching values, γ-path closes T-σ-Theorem-4. If only $\mu_0$ matches and $\mu_1$ doesn't, β-path is the necessary follow-on.

### §6.2 Risk — Two of three audit paths agree, one disagrees

Most likely outcome: γ-path resolves $\mu_0$ convention; α-path direct compute confirms naive ratio 2/3; β-path discovers R22's 4 came from a non-naive convention (C3 or C4) that was internally consistent but mis-cited as continuum. Then there are *two* canonical values (continuum 2/3 vs alternative R22 convention 4) and the canonical statement requires **explicit convention specification**.

**Mitigation**: CV-1.6 caveat text should include "subject to convention specification" language; CV-1.7+ post-reconciliation has the chance to pick the canonical convention deliberately rather than inherit R22's choice.

### §6.3 Risk — γ-path takes longer than 3 days

Likelihood: medium. Symbolic computation on simplex-projected Hessians at $L = 4$ is mechanical but error-prone; 3 days is the optimistic estimate.

**Mitigation**: W6 plan preview (Block 6) reserves D1-D3 for γ; if γ slips into D4, β starts in parallel anyway and α direct compute (1 hour) executes regardless. Parallel-track structure protects against single-path delay.

---

## §7. W6 D1-D3 Reconciliation Triple Handoff (operational)

**W6 D1 Mon 5/4 morning**:
- Read this file (`03_t_sigma_theorem4_reconciliation.md`) + canonical_revision packet (338 lines) + nq187b_L_extrapolation.md (422 lines) as a single state packet.
- Spawn / claim `working/SF/sigma_m_hessian_convention_audit.md` ownership.
- γ-path symbolic computation on $L = 4$ via SageMath or numpy + analytic.
- Run `nq187b_a2_a1_extrapolation.py` (α direct compute, < 1 hour).
- OAT-2 F bridge (omc-team output integration if collected) — independent track.

**W6 D2 Tue 5/5**:
- γ-path continued; if $L = 4$ symbolic confirms canonical or identifies convention issue, extend to $L = 8$.
- If γ-path findings → β-path needed: claim `working/SF/r22_a2_a1_audit.md` ownership.
- NQ-242 PH Phase 1 setup (Vietoris-Rips infrastructure via PHAT/GUDHI/Ripser) — independent track.
- OAT-3 λ_rep short integration — independent.

**W6 D3 Wed 5/6**:
- α-path direct compute output formalized into `nq187b_L_extrapolation.md` §6 results extension (or new appendix).
- γ-path final output: convention pinned down, OR escalation to β.
- NQ-242 PH Phase 1 dense runs (K=2/3) — independent track.
- OAT-4 shared-pool short integration — independent.

**W6 D4-D7**: γ closed (or escalated); β starts; CV-1.6 packet finalize; release.

→ **Day 5 deliverable**: this note + ownership assignment. **W6 D1 deliverable**: γ-path execution + α direct compute. **W6 D3 deliverable**: γ verdict + α formalized result. **W6 D4-D7 deliverable**: β execution + CV-1.6 caveat finalize + release.

---

## §8. Day 5 Hard Constraint Compliance (this file)

- [x] **canonical 직접 수정 0** — this is a working/log file in `logs/daily/2026-05-01/`; canonical.md untouched.
- [x] **No silent OP resolution** — T-σ-Theorem-4 Cat B status preserved; no claim of resolution. F-1 / M-1 / MO-1 / OP-0005 / OP-0008 / OP-0009 untouched.
- [x] **u_t primitive maintained** — T-σ-Theorem-4 operates on $u^*_\epsilon$ first-pitchfork minimizer (single-formation); σ-tuple is derived diagnostic.
- [x] **CN5 4-energy not merged** — N/A (single-formation σ-supporting structure).
- [x] **K not dual-treated** — N/A (single-formation context).
- [x] **CN10 contrastive** — numerical evidence (NQ-187 lanczos-engineer) used as constraint on theory; no reductive identification with external framework.
- [x] **No Research OS resurrection** — single-topic working note.
- [x] **No metastability claim without P-F flag** — N/A (static σ-extraction at first pitchfork).
- [x] **No new ε-expansion attempt today** — γ/β/α paths assigned, no derivation work.
- [x] **No Cat A re-promotion attempt today** — Cat B preserved with augmented caveat.

---

**End of 03_t_sigma_theorem4_reconciliation.md.**
**Status:** T-σ-Theorem-4 red lane no longer "confusing"; it is now "clearly unresolved in three specific dependent sub-paths γ (Σ_m-Hessian convention) + β (R22 cubic-equivariant) + α (finite-L vs continuum) with named owners and W6 D1-D7 handoff dates". Cat B retained; Cat A re-promotion deferred to CV-1.7+. CV-1.6 caveat wording drafted as proposal (not applied today). Hard constraint sweep clean.
