# 10_critic_NQ249_review.md — Critic Final Review of NQ-249 (`scc_mass_gap_connection.md`)

**Date:** 2026-04-30
**Reviewer agent:** critic (oh-my-claudecode:critic)
**Target file:** `THEORY/working/MF/scc_mass_gap_connection.md` (414 lines, last edit 2026-04-30)
**Companion files reviewed for cross-consistency:** `formation_birth_string_breaking.md` (NQ-253), `multi_formation_sigma.md` (T-σ-Multi-1 source), `sigma_multi_trajectory.md` (K-jump dynamics), `06_gauge_theory_connections_analysis.md` (Connection enumeration), `08_pm_infinite_develop_batch.md` (origin context).
**Source assignment:** PM batch §X — multi-perspective critic pass on the NQ-249 mass-gap conjecture file before Day 5+ promotion-gate decision.
**Output verdict class:** REVISE.

---

## §1. Aggregate Verdict

**Verdict: REVISE — 3 critical, 6 major, 5 minor findings.**

| Severity | Count | IDs |
|---|---|---|
| **Critical** | 3 | C1, C2, C3 |
| **Major** | 6 | M1, M2, M3, M4, M5, M6 |
| **Minor** | 5 | m1, m2, m3, m4, m5 |
| **Total flagged** | 14 | — |

**Headline summary.** The file successfully frames a graph-theoretic mass-gap analog (BC-249-1) under CN10 contrastive lock and avoids gross category errors (Yang–Mills is parallel, not foundation). However, three critical issues block immediate Day 5+ promotion as written:

1. **(C1)** The conjecture statement BC-249-1 (§3.1) asserts $\Delta_*(G, K)$ "*not* depending on $(\alpha, \beta, c)$" while the failure-mode analysis (§9.1) acknowledges $\Delta_K \to 0$ near bifurcation surfaces ⇒ $\Delta_*$ must depend on bifurcation distance ⇒ internally inconsistent.
2. **(C2)** §10.2 (mass-gap cycling at K-jumps) directly contradicts NQ-253 §4.3 ("formation birth is NOT spontaneous under SCC canonical dynamics; $\Delta K = +1$ is forbidden under noiseless gradient flow") by suggesting $K \to K+1$ cycling without flagging the protocol-conditional nature.
3. **(C3)** §7.1 Cat A claim that pointwise positivity is "Cat A immediate, no new mathematical content beyond canonical Morse-0 + T-σ-Lemma-3" is misleading: it silently inherits the well-separated regime hypothesis ($D_{\mathrm{sep}} \geq 3$) and the multi-formation Goldstone subspace identification (T-σ-Multi-1, currently Cat B target), neither of which is canonical Cat A.

The 6 majors and 5 minors are precision/citation/scope concerns that should be cleaned up before BC-249-1 is presented to the user as a candidate W7+ Cat B target.

**Promotion-gate recommendation:** §16 Path A ("no promotion required") stands as written *only after* the C1+C2+C3+M1 mandatory fixes are applied. §16 Path B (Cat B promotion of BC-249-1) requires the M2–M6 cleanups before the Cat B effort estimate (3–4 weeks W7) is realistic.

---

## §2. Critical Findings

### §2.1 C1 — BC-249-1 internally inconsistent

**Severity:** Critical.
**Location:** §3.1 (lines 67–75), §3.2 (line 79), §9.1 (lines 221–225).
**Type:** Internal contradiction between conjecture statement and failure-mode analysis.

**The contradiction.**

§3.1 states BC-249-1 as:
> "There exists a function $\Delta_*(G, K) > 0$ depending only on $(G, K)$ — *not* on $(\alpha, \beta, c)$ — such that $\Delta_K(G, \alpha, \beta, c) \geq \Delta_*(G, K)$ uniformly for all $(\alpha, \beta, c)$ with $c$ in the spinodal interior and $\beta > \beta_{\mathrm{crit}}^{(2)}(G, \alpha, c)$."

§9.1 then states:
> "$\Delta_K \to 0$ as $(\alpha, \beta, c)$ approaches bifurcation surface where $\beta_{\mathrm{crit}}^{(j)}$ thresholds intersect."

**The problem.** If $\Delta_K \to 0$ as $(\alpha, \beta, c)$ approaches a bifurcation surface contained in (or accumulated by) the post-bifurcation parameter region $\{(\alpha,\beta,c) : c \in \text{spinodal interior}, \beta > \beta_{\mathrm{crit}}^{(2)}\}$, then any uniform lower bound $\Delta_*(G, K) > 0$ over the entire region collapses to $0$. The "fix" §9.1 proposes ("restrict to interior of spinodal × $\{\beta > \beta_{\mathrm{crit}}^{(2)}\}$ minus a neighborhood of bifurcation locus") makes the neighborhood thickness an unavoidable parameter:

$$\Delta_*(G, K) \;=\; \Delta_*(G, K, \delta(\alpha, \beta, c))$$

where $\delta$ is the distance from the bifurcation locus. The "*not* on $(\alpha,\beta,c)$" clause therefore cannot stand as written.

**Severity justification.** This is the conjecture statement itself; an internally inconsistent conjecture cannot be a Cat B target — Cat B requires a stable target predicate to converge on. The current statement either trivially holds with a degenerate $\Delta_*(G,K) = 0$ (defeating the mass-gap claim) or demands a non-trivial dependence on bifurcation distance that §3.1 explicitly forbids.

**Mandatory fix (C1).** Restate BC-249-1 with one of:

- **Variant A (recommended):** $\Delta_*(G, K, \delta) > 0$ depending on $(G, K)$ and the bifurcation-distance scalar $\delta(\alpha,\beta,c) := \mathrm{dist}\big((\alpha,\beta,c),\,\text{bifurcation locus}\big)$. State BC-249-1 as: *for every $\delta_0 > 0$, there exists $\Delta_*(G, K, \delta_0) > 0$ such that $\Delta_K(G,\alpha,\beta,c) \geq \Delta_*(G, K, \delta_0)$ whenever $\delta(\alpha,\beta,c) \geq \delta_0$.*
- **Variant B:** Drop uniformity in $(\alpha,\beta,c)$ entirely; state BC-249-1 as a pointwise + open-set statement (mass gap is positive and locally lower semi-continuous on the parameter-fixed component).

Both variants require explicit edit of §3.1 paragraph, §3.2 inf-statement, and §9.1 resolution language. The current "$\Delta_*(G, K)$ depends only on $(G, K)$" line in §3.1 (line 71) must be deleted or replaced.

**Cross-references.** §4.3 ("operational reading: $\Delta_K > 0 \Leftrightarrow$ σ-tuple is locally rigid under perturbation of $(\alpha, \beta, c)$") is consistent with Variant A but inconsistent with the §3.1 uniform claim — currently §4.3 reads as if $\Delta_K > 0$ persists under perturbation, which contradicts §9.1's near-bifurcation collapse. Operational reading must be restricted to $\delta(\alpha,\beta,c) \geq \delta_0$.

---

### §2.2 C2 — Δ_K cycling at K-jumps contradicts NQ-253 noiseless-flow forbiddance

**Severity:** Critical.
**Location:** §10.2 (lines 251–255).
**Type:** Cross-file contradiction with NQ-253 (`formation_birth_string_breaking.md` §4.3).
**Companion file at fault:** none — the contradicting evidence is in NQ-253; this file is the one that needs to acknowledge the constraint.

**The contradiction.**

This file §10.2 states:
> "*Formation birth ↔ mass-gap closure + reopening.* When $K_{\mathrm{act}}$ jumps $K \to K+1$, the $K$-component mass gap closes (a flat direction opens for the new formation to nucleate); after birth, $(K+1)$-component mass gap re-opens. This *mass-gap cycling* is the SCC analog of QuEra-observed string breaking."

NQ-253 (`formation_birth_string_breaking.md`) §4.3 ("Formation birth is NOT spontaneous under SCC canonical dynamics") states:
> "Under noiseless SCC gradient flow on $\widetilde\Sigma^K_M$ with K-field architecture ($K_{\mathrm{field}} \geq 2$), a formation at $K_{\mathrm{act}} = 1$ will NOT spontaneously birth a second formation. The single-formation energy minimum is a local attractor in $S_1 \subset \widetilde\Sigma^K_M$."

NQ-253 §4.2 enumerates three mechanisms (B1 thermal noise, B2 IC manipulation, B3 stretching protocol) — all of which require *protocol control or external noise*, not noiseless canonical dynamics.

NQ-253 §3.1, line 318 (cascade discussion): "Each upward transition is a birth event requiring a mechanism (B1/B2/B3 from §4.2). Under noiseless flow the cascade is impossible."

**The problem.** §10.2's "mass-gap cycling" presentation strongly implies that $K \to K+1$ jumps are part of generic SCC dynamics — without flagging that they are *exclusively* protocol-conditional. The QuEra analog reading (line 255: "SCC analog of QuEra-observed string breaking") obscures the disanalogy: QuEra string breaking is a *quantum spontaneous process* (vacuum pair creation); SCC has no noiseless analog.

**Severity justification.** This is a foundational dynamics claim. Stating "mass-gap cycling at K-jumps" without the protocol-conditional qualifier propagates a misimpression that BC-249-1's $\Delta_K$ structure naturally exhibits cycling — when in fact the cycling only occurs under externally imposed B2/B3 protocols. NQ-249 inherits this confusion if not addressed.

**Mandatory fix (C2).** Add a reconciliation paragraph to §10.2 (target ~5 lines) explicitly:

1. Acknowledging NQ-253 §4.3 forbids $\Delta K = +1$ under noiseless gradient flow.
2. Clarifying that $\Delta_K$ cycling is *protocol-conditional* via NQ-253 §4.2 mechanisms B1 (noise), B2 (IC), or B3 (stretching).
3. Restricting the QuEra parallel: the SCC parallel is to the *threshold structure* of birth, not to the spontaneous mechanism.
4. Cross-referencing `formation_birth_string_breaking.md` §4 explicitly.

Suggested wording: *"Reconciliation with NQ-253: per `formation_birth_string_breaking.md` §4.3, $\Delta K = +1$ formation birth is forbidden under noiseless gradient flow on $\widetilde\Sigma^K_M$. The mass-gap cycling described above is therefore *protocol-conditional*: it occurs only under one of the NQ-253 §4.2 mechanisms B1 (thermal noise), B2 (initial-condition manipulation), or B3 (stretching protocol). Under generic noiseless SCC dynamics, $\Delta_K$ does not cycle. The QuEra parallel inherits the disanalogy of NQ-253 §3.3: SCC matches QuEra in the *threshold structure* of birth events, not in the spontaneous quantum mechanism."*

---

### §2.3 C3 — §7.1 Cat A claim is misleading (silent hypothesis chain)

**Severity:** Critical.
**Location:** §7.1 (lines 149–157), §16 Path A (lines 407–408).
**Type:** Silent hypothesis inheritance + Cat A category error.

**The claim.**

§7.1 states:
> "**Cat A target (immediate, this file):** $\forall\, \mathbf{u}^* \in \mathcal{L}_K \text{ Morse-0},\quad \min_k \lambda_k\!\big(H(\mathbf{u}^*)\big)\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp} \,>\, 0.$
> **Proof sketch:** Direct from Morse-0 definition: a Morse-0 critical point has positive-definite Hessian on the tangent space modulo zero modes. The Goldstone subspace is exactly the zero-mode subspace per T-σ-Lemma-3 (canonical `canonical.md:1318`); modding it out leaves a positive-definite operator. $\Box$
> **Status:** Cat A immediate, no new mathematical content beyond canonical Morse-0 + T-σ-Lemma-3."

§16 Path A states:
> "Pointwise positivity at non-degenerate Morse-0 minimizers is *already implied* by canonical T-σ-Theorem-3 + T-σ-Lemma-3 + Morse-0 definition; **no new canonical entry needed**. No promotion required at this iteration."

**The problem — silent hypothesis chain.**

The §7.1 proof sketch silently inherits **three non-trivial hypotheses** that do not appear in canonical Cat A items:

1. **(H1) Interior-only Whitney-stratified regime per Option A.** $\mathcal{L}_K$ is defined on $\widetilde{\Sigma}^{K_{\mathrm{field}},\,\circ}_M = \widetilde{\Sigma}^{K_{\mathrm{field}}}_M \setminus \partial\widetilde{\Sigma}$, with corner-saturated boundaries excluded (canonical §13 line 1218 hypothesis). Outside this interior, Morse-0 + Goldstone subspace identification breaks down (Option B stratified Morse, deferred to NQ-248 W7+). This is not "Cat A immediate" — it is conditional on Option A.
2. **(H2) Well-separated regime $D_{\mathrm{sep}} \geq 3$.** §2.1 defines $\mathcal{L}_K$ via canonical T-σ-multi-A-Static which itself assumes the well-separated hypothesis (canonical lines 1232–1235). Without this hypothesis, the multi-formation Hessian splitting argument is not canonical — it is a Cat C conditional result. The R23 generic-state caveat (canonical line 1239) explicitly notes the well-separated regime is non-generic on $32\times32$ $D_4$ free-BC grids.
3. **(H3) Multi-formation Goldstone subspace identification of T-σ-Multi-1.** The Goldstone subspace in the multi-formation regime is the subject of T-σ-Multi-1 (canonical lines 1248–1255), which is currently **Cat B target** (per CV-1.5.1 line 77 update note). T-σ-Lemma-3 alone gives the *single-formation* Goldstone identification; the multi-formation Goldstone-pair structure requires T-σ-Multi-1's still-pending Cat A upgrade.

**Severity justification.** Calling §7.1 "Cat A immediate" while silently inheriting (H1) Option A interior, (H2) well-separated $D_{\mathrm{sep}} \geq 3$, and (H3) T-σ-Multi-1 Cat B target collapses three distinct hypothesis categories into one misleading "Cat A" label. This propagates into §16 Path A's claim that "no new canonical entry needed" — which is only true *if* one accepts inheriting all three hypotheses, in which case the claim is conditional, not immediate.

**Mandatory fix (C3).** Restructure §7.1 with explicit hypothesis chain and downgrade Cat A status.

Suggested rewrite:

> "**Cat A target (immediate-conditional, this file):**
> Assume:
> - (H1) Interior-only Whitney-stratified regime per Option A (canonical §13 line 1218): $\mathcal{L}_K \subset \widetilde{\Sigma}^{K_{\mathrm{field}},\,\circ}_M$.
> - (H2) Well-separated regime: $D_{\mathrm{sep}}(\mathbf{u}^*) \geq 3$ for all $\mathbf{u}^* \in \mathcal{L}_K$ (canonical §13 T-σ-multi-A-Static hypothesis, lines 1232–1235).
> - (H3) Multi-formation Goldstone subspace identified per T-σ-Multi-1 (canonical lines 1248–1255).
>
> Then: $\forall\, \mathbf{u}^* \in \mathcal{L}_K \text{ Morse-0},\; \min_k \lambda_k\!\big(H(\mathbf{u}^*)\big)\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp} \,>\, 0$ pointwise.
>
> **Status:** Cat A *conditional on T-σ-Multi-1 Cat A upgrade*. Currently (H3) is Cat B target per canonical CV-1.5.1; this conditional Cat A inherits T-σ-Multi-1's Cat B status until the T-σ-Multi-1 promotion is completed (NQ-2xx). Reduces to Cat A immediate only after T-σ-Multi-1 Cat A upgrade."

§16 Path A must be retracted: "no canonical entry needed" cannot stand. Suggested replacement:

> "**Path A (Cat A conditional, §7.1):** Pointwise positivity is conditional on (H1)+(H2)+(H3) as restated. Promotion to canonical §13 deferred until T-σ-Multi-1 Cat A upgrade is achieved. *(Earlier draft asserted "no canonical entry needed" — retracted 2026-04-30 per critic review C3.)*"

---

## §3. Major Findings

### §3.1 M1 — Inaccurate canonical line citations

**Severity:** Major.
**Locations across file:**
- §1.3 (line 34): `canonical.md:1217–1228` for T-Commitment-14-Multi-Static.
- §2.1 (line 44): `canonical.md:1337` for "spinodal interior".
- §2.1 (line 48): `canonical.md:1232–1235` for T-σ-multi-A-Static well-separated regime.
- §3.1 (line 75): `canonical.md:1343` for "Phase-transition theorem".
- §5 table (line 119): `canonical.md:1343` for "Uniform state $c\mathbf{1}$ — but mass gap measured *not* at vacuum, rather at non-trivial K-formation minimizers".
- §6.1 (line 132): `canonical.md:1199` for T-V5b-T-zero.
- §7.3 (line 178): "canonical §13 line 1343, `mode_count.md` Prop 1.3a" — phase-transition reference.
- §8.1 (line 192): `canonical.md:1367` for exp_hessian_uniform_v2.json.
- §9.4 (line 239): `canonical.md:77` for OP-0008.
- §12.2 (line 314): `canonical.md:77` for Commitment 16.
- §14.1 (line 354): "lines 1337–1371" for §3 phase transition.

**Type:** Citation accuracy / promotion-gate evidence.

**The problem — line citations checked against canonical.md (1666 lines total).**

| Citation in NQ-249 | Claimed content | Actual content at that line |
|---|---|---|
| `canonical.md:77` | OP-0008 / Commitment 16 K-status | **CV-1.5.1 row in the version-history table (§1.1)** — meta entry, not Commitment 16 itself. Commitment 16 is at lines 796–812 (§11.1). |
| `canonical.md:1337` | "spinodal interior" / phase-transition | **T-σ-Theorem-3 hypothesis discussion (added 2026-04-27 night)** — inside T-σ-Theorem-3, not the phase-transition theorem proper. Phase-transition theorem T8-Core is at line 1005 with Scaling Caveat at 1009. Admissible spinodal range is at line 572 (canonical §8). |
| `canonical.md:1343` | "Phase-transition theorem" / "Uniform state $c\mathbf{1}$" | **Inside T-σ-Theorem-3 (lines 1334–1409), section discussing Hessian on uniform.** Not the canonical §3 phase transition. |
| `canonical.md:1367` | exp_hessian_uniform_v2.json reference | **Inside T-σ-Theorem-4** (theorem starts ~line 1378). Empirical anchor location may be wrong. |
| `canonical.md:1199` | T-V5b-T-zero | **Correct** — V5b-T-zero sub-statement at line 1199. |
| `canonical.md:1217–1228` | T-Commitment-14-Multi-Static | **Correct** — T-Commitment-14-Multi-Static at line 1218. |
| `canonical.md:1232–1235` | T-σ-multi-A-Static + $D_{\mathrm{sep}} \geq 3$ hypothesis | **Plausible** — T-σ-multi-A-Static block in §13. |
| `canonical.md:1318` | T-σ-Lemma-3 nodal subspace | **Plausible** — T-σ-Lemma-3 at lines 1301–1320. |

**Key errors.**
1. `canonical.md:77` for **Commitment 16** is wrong — line 77 is the version-history table entry for CV-1.5.1, not the §11.1 Commitment 16 block. Commitment 16 is at lines 796–812.
2. `canonical.md:1337` and `canonical.md:1343` for the **phase-transition theorem / spinodal interior** are wrong — these lines are inside T-σ-Theorem-3 (lines 1334–1409), which is a *separate* canonical entry from the T8-Core phase-transition theorem at line 1005. The Scaling Caveat at line 1009 is the correct place to cite for the $\beta_{\mathrm{crit}}$ scaling, and line 572 (canonical §8) is the correct place for the admissible spinodal range $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$.

**Severity justification.** Inaccurate line citations are not catastrophic but they fail the canonical-traceability standard for promotion-gate evidence. A reviewer following `canonical.md:77` to verify Commitment 16 will find the version table, not the Commitment block. This degrades the file's evidentiary value for any Cat B promotion attempt. Additionally, citing the phase-transition theorem via T-σ-Theorem-3 lines obscures the distinction between the foundational existence theorem (T8-Core) and the σ-framework-supporting theorem (T-σ-Theorem-3) — a category-of-canonical confusion.

**Mandatory fix (M1).** Correct each citation by `grep`-verification before the next promotion-gate. Specifically:

| Replace | With |
|---|---|
| `canonical.md:77` (Commitment 16 reference) | `canonical §11.1 Commitment 16, lines 796–812` |
| `canonical.md:77` (OP-0008 reference) | `canonical §1.1 CV-1.5.1 release-notes line 77; see also `THEORY/canonical/open_problems.md` OP-0008` |
| `canonical.md:1337` (phase-transition / spinodal interior) | `canonical §8 admissible range line 572` (for spinodal interval) **or** `canonical §13 T8-Core line 1005 + Scaling Caveat line 1009` (for $\beta_{\mathrm{crit}}$ formula) |
| `canonical.md:1343` (phase-transition + uniform vacuum) | `canonical §13 T-σ-Theorem-3 (lines 1334–1409)` (if context is σ-Theorem-3) **or** `canonical §13 T8-Core line 1005` (if context is phase-transition existence) — disambiguate based on §-by-§ context. |
| `canonical.md:1367` (exp_hessian_uniform_v2.json) | Re-verify; if inside T-σ-Theorem-4, cite `canonical §13 T-σ-Theorem-4 lines 1378–1409`. |

Apply fixes in §1.3, §2.1, §3.1, §5 table, §7.3, §8.1, §9.4, §12.2, §14.1.

---

### §3.2 M2 — Thermodynamic limit collision with T8-Core Scaling Caveat

**Severity:** Major.
**Location:** §3.3 (lines 81–83), §11.2 (lines 286–288).
**Type:** Cross-statement collision with canonical T8-Core Scaling Caveat (line 1009).

**The collision.**

§3.3 states:
> "the analog of the IR limit is the *thermodynamic limit* of $G \to \infty$ via $L \to \infty$ on a $L^d$ lattice, which yields a separate continuum-limit mass-gap statement (NQ-217 interaction, see §11). BC-249-1 is the *finite-graph* statement; the continuum extension is BC-249-2 (deferred)."

§11.2 elaborates BC-249-2 dependence on NQ-217 graph-to-continuum convergence.

**The problem — canonical Scaling Caveat (line 1009).**

T8-Core Scaling Caveat (canonical line 1009):
> "The phase transition threshold $\beta_{\mathrm{crit}} = 4\alpha\lambda_2/|W''(c)|$ depends on the spectral gap $\lambda_2$ of the graph Laplacian. For graph families where $\lambda_2 \to 0$ as $n \to \infty$ (e.g., $k \times k$ grids with $\lambda_2 \sim \pi^2/k^2$), the threshold vanishes and the criterion is trivially satisfied for any fixed $\beta > 0$. In this regime, T8-Core guarantees non-trivial minimizer *existence* but does not provide a meaningful *selection criterion* for parameters."

**Implication for NQ-249.** On $L^d$ grids, $\lambda_2 \sim \pi^2/L^2 \to 0$ as $L \to \infty$, so $\beta_{\mathrm{crit}}^{(2)} \to 0$. The post-bifurcation regime $\{\beta > \beta_{\mathrm{crit}}^{(2)}\}$ degenerates to "$\beta > 0$" trivially — the BC-249-1 hypothesis is satisfied for any fixed $\beta > 0$ in the thermodynamic limit, but the selection criterion is degenerate. The mass-gap statement BC-249-2 inherits this scaling pathology: any "uniform mass gap" claim across $L \to \infty$ must specify how the bifurcation distance $\delta(\alpha,\beta,c)$ from §C1 scales with $L$. If $\delta \to 0$ as $L \to \infty$, BC-249-2 collapses.

**Severity justification.** §3.3 sets up BC-249-2 as the continuum extension via NQ-217 without acknowledging that T8-Core's own scaling caveat already flags the thermodynamic limit as a degenerate selection regime. Any mass-gap claim in this limit must engage with the spectral-gap-vanishing pathology — currently not addressed.

**Recommended fix (M2).** Add a footnote or paragraph in §3.3 acknowledging T8-Core Scaling Caveat (canonical line 1009) and noting that BC-249-2 (continuum extension) inherits the spectral-gap pathology: any uniform mass-gap claim across $L \to \infty$ must specify the bifurcation-distance scaling. Suggested wording:

> "*Caveat (T8-Core Scaling, canonical line 1009)*: On $L^d$ grids, $\beta_{\mathrm{crit}}^{(2)} \sim 4\alpha\pi^2/(L^2 |W''(c)|) \to 0$ as $L \to \infty$, and the T8-Core selection criterion degenerates. BC-249-2 inherits this: any uniform mass-gap statement across $L \to \infty$ must specify how the bifurcation-distance threshold $\delta_0$ (per C1 fix) scales with $L$. If $\delta_0(L) \to 0$ faster than the bifurcation locus accumulates, BC-249-2 collapses. Dependence on NQ-217 thermodynamic-limit machinery is therefore non-trivial."

---

### §3.3 M3 — Goldstone subspace dimension fluctuation

**Severity:** Major.
**Location:** §6 (lines 128–142), §9.2 (lines 227–229).
**Type:** Definitional gap — Gold dimension treated as constant, but varies with $K_{\mathrm{act}}$ and graph symmetry.

**The problem.**

§6.1 states the Goldstone subspace is $\mathrm{Gold} = \mathrm{span}(\delta u_{x_1}, \ldots, \delta u_{x_d})$ — $d$-dimensional from discrete lattice translation. §6.3 then mentions multi-formation Goldstone-pair from T-σ-Multi-1: each formation contributes a per-formation Goldstone, joint Hessian splits the pair.

§9.2 acknowledges Goldstone proliferation but resolves it as "Mass-gap defined relative to the *full* Goldstone subspace $\mathrm{Gold}_{\mathrm{full}}$; uniform bound conditional on $\dim \mathrm{Gold}_{\mathrm{full}}$ being finite (always true on finite graphs)."

**The gap.** $\dim \mathrm{Gold}_{\mathrm{full}}$ depends on $(K_{\mathrm{act}}, \mathrm{Stab}(\mathbf{u}^*), G)$. On a $D_4$-symmetric grid with $K_{\mathrm{act}} = 2$ formations placed symmetrically, the joint stabilizer $\mathrm{Stab}(\mathbf{u}^*) = \mathbb{Z}_2$ (formation-swap) reduces the effective Goldstone dimension by inducing pair-wise correlations among the per-formation Goldstones. The "$d$-dim" count from §6.1 is not $d \times K_{\mathrm{act}}$ — it is some function of $(d, K_{\mathrm{act}}, \mathrm{Stab})$ that the file does not specify.

The mass-gap definition $\Delta_K(G,\alpha,\beta,c) := \inf_{\mathbf{u}^* \in \mathcal{L}_K} \min_k \lambda_k(H(\mathbf{u}^*))\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp}$ then depends on $\dim \mathrm{Gold}$ varying across $\mathcal{L}_K$ — which means the orthogonal complement is a varying-dimension subbundle. The infimum then takes a non-trivial form (over varying-dimensional fibers).

**Severity justification.** Without specifying how $\dim \mathrm{Gold}$ varies, the operator $H\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp}$ is ambiguous when $\mathcal{L}_K$ contains minimizers with different stabilizers. This is a definitional gap that affects BC-249-1's well-formedness.

**Recommended fix (M3).** Add §6.4 (or expand §6.3) explicitly stating $\dim \mathrm{Gold}_{\mathrm{full}}(\mathbf{u}^*) = \dim \mathrm{Gold}_{\mathrm{full}}(d, K_{\mathrm{act}}(\mathbf{u}^*), \mathrm{Stab}(\mathbf{u}^*))$ and either:

- (a) restrict $\mathcal{L}_K$ to a stabilizer-fixed component (each $\mathbf{u}^* \in \mathcal{L}_K$ has the same $\mathrm{Stab}$), making $\dim \mathrm{Gold}$ constant; or
- (b) define $\Delta_K$ piecewise across stabilizer strata, with $\Delta_*(G, K, [H_0])$ depending on the conjugacy class $[H_0] = [\mathrm{Stab}]$.

This affects §3.1 conjecture statement: BC-249-1 may need stratum indices.

---

### §3.4 M4 — §9.3 well-separated regime evacuates R23-generic

**Severity:** Major.
**Location:** §9.3 (lines 231–235).
**Type:** Scope collapse — BC-249-1 holds on a non-generic submanifold per canonical R23 caveat.

**The problem.**

§9.3 states:
> "Restrict $\mathcal{L}_K$ to well-separated regime $D_{\mathrm{sep}} \geq 3$ per T-Persist-K-Sep (canonical T-σ-multi-A-Static hypothesis, `canonical.md:1233`). The R23 generic-state caveat (canonical `canonical.md:1239`) shows the well-separated regime is non-generic on $32\times32$ $D_4$ free-BC grids — implying BC-249-1 in its current form holds on a non-generic submanifold. Generalization to overlapping regime requires NQ-242 PH pipeline (canonical `canonical.md:1239`)."

**The implication.** BC-249-1 holds on a non-generic submanifold of $\widetilde{\Sigma}^{K_{\mathrm{field}},\,\circ}_M$. R23 (`single_high_F_equivalence.md`) found that on $32\times32$ $D_4$ free-BC grids, generic minimizers have $\mathcal{F} \geq 5$ peaks with $K_{\mathrm{step}} \geq 1$ — i.e., overlapping rather than well-separated. The well-separated $D_{\mathrm{sep}} \geq 3$ regime is then a **measure-zero or low-density submanifold** of the empirical generic stratum.

**Why this is a Major issue.** A mass-gap conjecture holding on a non-generic submanifold has limited explanatory force: it covers a regime that almost no R23 minimizer occupies. The promotion-gate effort estimate (3–4 weeks W7 for Cat B target) does not currently account for the fact that successful Cat B proof would still leave the empirical generic regime (R23-generic, overlapping) unaddressed — which is the regime that NQ-242 PH pipeline targets.

**Severity justification.** This isn't a contradiction (the file does acknowledge R23-non-generic), but it materially degrades BC-249-1's evidentiary scope. A reader could conclude "BC-249-1 ≅ YM mass-gap" without noticing the regime restriction. The §11 effort estimate should reflect that BC-249-1 in well-separated regime is a *partial* result, not the full SCC mass-gap target.

**Recommended fix (M4).** Add a paragraph or footnote in §3.3 or §9.3 explicitly stating:

> "*Scope caveat*: BC-249-1 in the form presented here holds on the well-separated submanifold $\{\mathbf{u}^* \in \mathcal{L}_K : D_{\mathrm{sep}}(\mathbf{u}^*) \geq 3\}$, which is non-generic relative to R23 empirical observations on $32\times32$ $D_4$ grids ($\mathcal{F} \geq 5$ overlapping minimizers dominate). The generic-stratum extension (BC-249-1-Generic) requires NQ-242 PH pipeline machinery and is deferred to W8+. Effort estimate in §11.1 (3–4 weeks W7) covers only the well-separated case; full-stratum coverage is a separate ~6-8 week effort."

---

### §3.5 M5 — §8 compute scope unrealistic

**Severity:** Major.
**Location:** §8 (lines 184–215).
**Type:** Compute feasibility / experimental design realism.

**The setup.**

§8.1 specifies:
- Graph: $L \in \{4, 8, 16\}$ ⇒ node counts $16, 64, 256$.
- $K_{\mathrm{field}} \in \{1, 2, 3\}$.
- $\beta \in [\beta_{\mathrm{crit}}^{(2)}(L, c), 50]$ with **20 log-spaced points**.
- Multi-start: **10 random initial conditions per parameter point**.
- Procedure: full Hessian via finite-difference + projection to Goldstone complement.

**Compute estimate.** Per parameter point:
- $L=16, K=3$: $u \in \mathbb{R}^{256 \times 3} = \mathbb{R}^{768}$. Full Hessian $H \in \mathbb{R}^{768 \times 768}$. Finite-difference Hessian: $768 \times 2 = 1536$ gradient evaluations, each requiring O($n \log n$) work for the grad. Eigendecomposition O($n^3$) ~ $4.5 \times 10^8$ flops per Hessian.
- 10 ICs × 20 $\beta$-points × 3 $K$ × 3 $L$ = **1800 parameter points**.
- Each parameter point: 1 optimizer run (`find_formation`) + 1 Hessian computation + 1 projection.

**Estimate breakdown.**
- `find_formation` runtime per point: O(seconds) for $L=4,8$; O(minutes) for $L=16, K=3$.
- Hessian + eigendecomp at $L=16, K=3$: ~30 seconds–2 minutes per Hessian on a single CPU core.
- **Total compute estimate**: 10 × 20 × 3 = 600 parameter points per $L$. At $L=16, K=3$: 600 × 3 min ≈ **30 hours single-core**.
- Multiplied across 3 values of $L$: ~5–15 hours minimum, plausibly ≥ 30 hours on the largest grid alone.

§8 currently shows no parallelization plan, no batching strategy, no estimated runtime. The "1 week" effort estimate in §11.1 (NQ-249a) for empirical anchor is **plausible but tight**: it requires non-trivial CODE/ infrastructure work (extending `CODE/scc/diagnostics.py` to multi-formation Hessian — flagged in §14.4 line 385).

**Severity justification.** Major (not critical) because §11.1 already flags this as 1 week effort and §14.4 acknowledges the CODE extension dependency. But the absence of a compute budget estimate, a parallelization plan, and a finite-difference accuracy note (Hessian via FD is noisy at $\epsilon = 10^{-4}$ — see canonical V5b-T-zero anchor at line 1199 noting $|\mu_{\mathrm{Gold}}| \leq 0.028$ within FD noise) means the empirical anchor will likely fail to detect $\Delta_K$ near zero (mass-gap closure) — exactly the regime BC-249-1 is most interesting in.

**Recommended fix (M5).**

1. Add §8.4 "Compute Budget" specifying:
   - Total Hessian evaluations: 1800.
   - Largest Hessian size: $768 \times 768$.
   - Estimated single-core runtime: ~30 CPU-hours.
   - Parallelization: parameter points are embarrassingly parallel ⇒ run on $\geq 8$ cores ⇒ ~4 wall-hours.
2. Add §8.5 "FD Noise Floor" specifying:
   - Hessian via FD with $\epsilon = 10^{-4}$ has noise floor $\sim \epsilon^{1/2} \approx 10^{-2}$ on eigenvalues.
   - $\Delta_K$ values $\lesssim 10^{-2}$ cannot be distinguished from zero ⇒ mass-gap closure regime is empirically inaccessible at this precision.
   - Recommend hybrid: analytic Hessian via `CODE/scc/operators.py` JVP machinery where available; FD only for cross-check.
3. Reduce $L = 16$ scope or use smaller $L \in \{4, 6, 8, 10\}$ first; defer $L=16$ to second-pass.

---

### §3.6 M6 — §7.3 closed-form references uniform not post-bifurcation

**Severity:** Major.
**Location:** §7.3 (lines 170–180).
**Type:** Reference scope mismatch.

**The claim.**

§7.3 states:
> "**Reference:** SF/mode_count.md (`/Users/ojaehong/Perception/Perception_theory/THEORY/working/SF/mode_count.md`) provides the closed-form Hessian on $u_{\mathrm{uniform}}$ basis: $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ (canonical §13 line 1343, `mode_count.md` Prop 1.3a). Multi-formation analog with $K \geq 2$ Goldstone-pair coupling: open."

**The problem.**

The cited closed-form $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ is the Hessian spectrum at the **uniform vacuum** $u^* = c\mathbf{1}$ — *before* the first pitchfork bifurcation at $\beta = \beta_{\mathrm{crit}}^{(2)}$. This is canonical T-σ-Theorem-3 setup (lines 1334–1371): $\beta < \beta_{\mathrm{crit}}^{(2)}$, $u^* = c\mathbf{1}$, sub-critical Morse-0.

But $\Delta_K$ is defined at **non-trivial K-formation minimizers** $\mathbf{u}^* \in \mathcal{L}_K$, which exist only **post-bifurcation** ($\beta > \beta_{\mathrm{crit}}^{(2)}$). At post-bifurcation, $u^* \neq c\mathbf{1}$ and the closed-form $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ does *not* apply.

The post-bifurcation Hessian spectrum requires a **different** closed-form, derived in T-σ-Theorem-4 (canonical lines 1378–1409 approximately). At $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$ with $\epsilon > 0$ small, $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1,0)} + O(\epsilon)$ with $a_\epsilon = c_R\sqrt{\epsilon}$, and the Hessian spectrum has a different form (see canonical line 1378 onward).

**Severity justification.** Citing the uniform-vacuum closed-form as the "Cat C target" closed-form for $\Delta_*(G, K)$ misleads about the actual difficulty. The Cat C target is the post-bifurcation Hessian spectrum, which is non-trivial precisely because the perturbation expansion around $c\mathbf{1}$ breaks down post-bifurcation.

**Recommended fix (M6).**

Replace the §7.3 reference paragraph with:

> "**Reference:** `SF/mode_count.md` Prop 1.3a provides the closed-form Hessian *at the uniform vacuum* $u^* = c\mathbf{1}$ (sub-critical, $\beta < \beta_{\mathrm{crit}}^{(2)}$): $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ (canonical T-σ-Theorem-3, lines 1334–1371). However, $\Delta_K$ is defined at **post-bifurcation** $K$-formation minimizers ($\beta > \beta_{\mathrm{crit}}^{(2)}$, $u^* \neq c\mathbf{1}$), where the uniform-vacuum closed-form does not apply. The post-bifurcation Hessian closed-form requires a separate normal-form expansion derived in T-σ-Theorem-4 (canonical lines 1378–1409); see also `SF/symmetry_moduli.md` for $D_4$-normal-form coefficients $A_1, A_2$. The Cat C target $\Delta_*(G, K)$ closed-form must therefore be derived in the post-bifurcation regime — substantially harder than the uniform-vacuum case, justifying the 6-8 week effort estimate."

---

## §4. Minor Findings

### §4.1 m1 — §2.3(b) ambiguous "Infimum may collapse"

**Location:** §2.3(b) (line 61).

§2.3(b) says: "Whether $\Delta_K > 0$ (uniform) or $\Delta_K = 0$ (collapse) depends on whether $\mathcal{L}_K$ is bounded away from bifurcation surfaces / merger boundaries."

Should be tightened to: "depends on whether $\mathcal{L}_K$ has positive distance to the union of bifurcation locus and merger boundary in the parameter space $\{(\alpha,\beta,c)\}$." Provide a precise distance metric (Euclidean in normalized parameter coordinates is conventional).

### §4.2 m2 — §5 contrastive table conflates BRST vs Goldstone

**Location:** §5 table row "Symmetry-breaking modes" (line 122).

The table aligns "Goldstone bosons in spontaneously broken phases" (YM) with "T-V5b-T-zero exact zero mode" (SCC). This is misleading: YM Goldstone bosons appear in *spontaneously broken* phases (Higgs / chiral symmetry), while T-V5b-T-zero is a *discrete* lattice translation Goldstone — a different mathematical category. The contrastive lock §1.3 emphasizes "structural inspiration, not derivation" — but the table treats the analogy as tighter than that. Add a footnote: "Disanalogy: YM Goldstones are Lie-group-valued continuous; SCC V5b-T-zero is discrete-translation $\mathbb{Z}^d$-valued. The structural parallel is in the *role* (mass-gap requires modding out the symmetry orbit closure), not in the Lie-algebra structure."

### §4.3 m3 — §10.1 NQ-251 Anderson-localization parallel under-developed

**Location:** §10.1 (lines 245–249).

The Anderson-localization mass-gap analog is mentioned but not cited. Suggest adding a reference to the Duke 2026 paper from `06_gauge_theory_connections_analysis.md` Connection G (cited at line 26 there). The NQ-251 candidate registration is implicit; should be explicit in §15 "Open questions registered" table.

### §4.4 m4 — §10.3 Floer "speculative" but not P-F flagged

**Location:** §10.3 (lines 257–261).

§10.3 says the Floer mass-gap analog is "*speculative*; categorical structure not developed" but does not P-F flag (Provisional / Framework). Per `08_pm_infinite_develop_batch.md` conventions, speculative cross-domain analogies should carry a P-F flag in the file metadata. Add P-F flag to §10.3 paragraph header.

### §4.5 m5 — §15 NQ-249g effort estimate inconsistent with §10.2

**Location:** §15 NQ-249g row (line 401), §10.2 mass-gap cycling (line 255).

§15 NQ-249g estimates "4 weeks" for "mass-gap cycling at formation birth (Connection H to QuEra 2025 string break)". But per C2 fix, this depends on NQ-253 Phase 1 completion (4–6 weeks W7). The 4-week estimate for NQ-249g should be **after** NQ-253 Phase 1 completes, not in parallel — making total wall-clock ~10 weeks (W7 NQ-253 Phase 1 + W8+ NQ-249g). Update §15 effort estimate or add dependency note.

---

## §5. Cross-File Consistency with NQ-253

| Aspect | NQ-249 (this file) | NQ-253 (`formation_birth_string_breaking.md`) | Consistent? |
|---|---|---|---|
| **Noiseless gradient flow K-monotonicity** | §10.2 implies cycling $K \to K+1$ | §4.1 monotone $K_{\mathrm{act}}$ decrease (T-Merge (b) Cat A) | **❌ Contradiction (C2)** |
| **$\Delta K = +1$ mechanism** | §10.2 ("formation birth") not flagged | §4.2 Mechanisms B1/B2/B3 explicitly required (protocol or noise) | **❌ Missing protocol qualifier (C2)** |
| **QuEra string-breaking analog** | §10.2 SCC analog of QuEra | §3.3 QuEra parallel + §4 disanalogy (CN10) | **⚠ Partial — disanalogy not echoed in NQ-249** |
| **Mass-gap closure mechanism** | §9.3 multi-formation merger ($D_{\mathrm{sep}} \to D_{\mathrm{merge}}^*$) | §3.1 string breaking at $L_{\mathrm{crit}}$ | ✅ Independent — both consistent with bifurcation closure |
| **R23 generic regime** | §9.3 R23-non-generic well-separated submanifold | §3.2 R23 absence consistent with $L_{\mathrm{crit}} \to 0$ at $\beta = 30$ | ✅ Both flag R23 generic-state caveat |
| **Cat B target effort** | §11.1 BC-249-1: 3–4 weeks W7 | §12.1 NQ-253 Phase 1: 4–6 weeks W7 | ⚠ Parallel slot — possible scheduling collision |
| **NQ-200 entry point** | Not mentioned | §1.1 explicit ($K \geq 3$ wreath product) | ⚠ NQ-249 should reference NQ-200 dependency on NQ-253 cascade |
| **CN10 disanalogy** | §1.3, §5, §11.4 — multiple invocations | §1.2, §3.3, §4.3 — CN10 disanalogy explicit | ✅ Both invoke CN10 properly |
| **Multi-formation Goldstone** | §6.3 invokes T-σ-Multi-1 (Cat B target) | §5.5 V5b-F mass scaling | ✅ Both leverage same Cat B canonical lemma |
| **Stretching protocol B3** | Not mentioned | §4.2 B3 explicit, §6 experimental design | ⚠ NQ-249's "K-jump cycling" should reference B3 as the protocol |

**Top consistency issue:** Row 1 (noiseless flow K-monotonicity) — Critical, mapped to C2 above.

**Mandatory cross-file alignment:** After C2 fix, NQ-249 §10.2 must explicitly cite `formation_birth_string_breaking.md` §4.2 (mechanisms) and §4.3 (noiseless forbiddance) by section number and file name.

---

## §6. CN10 Contrastive Integrity Audit

NQ-249 invokes CN10 (canonical-non-reductive contrastive lock) in §1.3, §5, §11.4. This audit checks whether the file passes the "Yang–Mills is parallel, not foundation" standard.

### §6.1 Language passes

- ✅ §1.3: "SCC mass-gap candidate inherits *structural inspiration* (a positive lower bound on the spectral gap excluding zero modes), not derivation. We never write 'SCC mass gap = YM mass gap'; we write 'SCC mass-gap analog $\Delta_K$ on $(G, \alpha, \beta, c)$'."
- ✅ §5 closing paragraph: "**The analog is not reduction.** SCC does not reduce to Yang–Mills; the parallel is structural — both ask whether the spectrum of a quadratic form on the perturbation space about a non-trivial minimizer admits a uniform positive lower bound. The mathematical content of SCC's BC-249-1 is purely graph-spectral + double-well + symmetry-breaking, with **no quantum-field, BRST, or gauge-theoretic content**."
- ✅ §11.4 V5b reuse note acknowledges canonical inheritance, not derivation.

### §6.2 Partial concerns — ↔ vs → directionality

In §10.1, §10.2, §10.3 connection-summary tables, the column "Direction" reads e.g. "Inspires BC-249-1" / "Localization metric" / "Formation birth". This is correct (one-way SCC → use of structural ideas from gauge theory). But the prose in §10.2 line 254 ("$\Delta_K$ closes... after birth, $(K+1)$-component mass gap re-opens") reads as a **bidirectional ↔** claim about SCC mirroring QuEra observations — which crosses CN10's one-way constraint.

**Concern:** "Mass-gap cycling is the SCC analog of QuEra-observed string breaking" — the word *analog* is fine, but the implicit direction-of-evidence reading suggests QuEra observation **validates** SCC behavior. Per CN10, QuEra is *downstream comparison*; it cannot validate SCC structure. Suggested fix (combined with C2 fix above): "Under protocol B3 stretching, $\Delta_K$ exhibits cycling at $K$-jumps that *structurally parallels* QuEra-observed string breaking — but the validation direction is one-way (SCC dynamics is independent of QuEra evidence)."

### §6.3 Weak on §10.2 K → K+1 cycling

Per C2 above, §10.2's framing risks treating QuEra's observed spontaneous string breaking as evidence for SCC's mass-gap cycling — which would invert CN10's contrastive lock (cog-sci/empirical observation as ontological input). Mandatory C2 fix addresses this; §10.2 must read as protocol-conditional structural parallel, not as cross-domain evidence flow.

### §6.4 CN10 verdict

**Verdict: Passes language test; partial concerns on §10.2 directionality (mapped to C2 fix); weak on K → K+1 cycling presentation (also C2).**

---

## §7. Carry-Forward to Day 5+

### §7.1 Mandatory fixes (must complete before any promotion-gate decision)

1. **C1**: Restate BC-249-1 with explicit $\delta(\alpha,\beta,c)$ bifurcation-distance dependence. Drop the "*not* on $(\alpha,\beta,c)$" claim. Edit §3.1, §3.2, §9.1.
2. **C2**: Add reconciliation paragraph to §10.2 acknowledging NQ-253 §4.3 forbids $\Delta K = +1$ under noiseless flow; cycling is protocol-conditional via NQ-253 §4.2 mechanisms B1/B2/B3.
3. **C3**: Restructure §7.1 with explicit (H1)+(H2)+(H3) hypothesis chain. Downgrade Cat A claim to Cat A *conditional on T-σ-Multi-1 Cat A upgrade*. Retract §16 Path A "no canonical entry needed" claim.
4. **M1**: Correct canonical line citations. Specifically:
   - `canonical.md:77` → `canonical §11.1 Commitment 16 lines 796–812` (for Commitment 16) or `canonical §1.1 CV-1.5.1 line 77 + open_problems.md OP-0008` (for OP-0008).
   - `canonical.md:1337` / `canonical.md:1343` → context-disambiguate: `canonical §13 T-σ-Theorem-3 lines 1334–1409` for σ-theory, or `canonical §13 T8-Core line 1005 + Scaling Caveat line 1009` for phase-transition existence, or `canonical §8 line 572` for admissible spinodal range.
   - Verify each citation by `grep -n` before applying.

### §7.2 Recommended fixes (improve quality before W7 BC-249-1 effort begins)

5. **M2**: Add T8-Core Scaling Caveat acknowledgment in §3.3.
6. **M3**: Specify $\dim \mathrm{Gold}(\mathbf{u}^*)$ stratification across $\mathcal{L}_K$.
7. **M4**: Add R23-non-generic scope caveat in §3.3 or §9.3.
8. **M5**: Add §8.4 compute budget + §8.5 FD noise floor analysis.
9. **M6**: Correct §7.3 reference: distinguish uniform-vacuum (T-σ-Theorem-3) from post-bifurcation (T-σ-Theorem-4) closed-forms.
10. **m1**: Tighten §2.3(b) "infimum may collapse" with precise distance metric.
11. **m2**: Footnote on §5 table BRST vs Goldstone disanalogy.
12. **m3**: Cite Duke 2026 in §10.1; register NQ-251 explicitly in §15.
13. **m4**: P-F flag §10.3 Floer paragraph.
14. **m5**: Update §15 NQ-249g effort dependency on NQ-253 Phase 1.

### §7.3 Promotion-gate guidance

- **Path A (§16, Cat A immediate):** Currently asserts "no canonical entry needed" — must be retracted per C3. Replace with "Cat A conditional, deferred until T-σ-Multi-1 Cat A upgrade."
- **Path B (§16, Cat B target BC-249-1):** Cannot proceed until C1 + M3 are addressed. Effort estimate (3–4 weeks W7) realistic only after C1 reformulation. M4 scope caveat means BC-249-1 covers a non-generic submanifold — full coverage is a separate W8+ ~6-8 week effort.
- **Path C (§16, Cat C closed form):** Currently mis-references uniform-vacuum closed-form (M6). After M6 fix, Path C is correctly identified as post-bifurcation closed-form derivation, ~6-8 weeks W8+.

**Promotion timeline (revised after critic review):**
- Day 5+ (immediate): apply C1+C2+C3+M1 fixes. No promotion this iteration.
- W6 Day 5+: NQ-249a empirical anchor (M5-revised compute plan, smaller-$L$ first-pass).
- W7: NQ-253 Phase 1 (precondition for NQ-249g) + BC-249-1 well-separated proof attempt (post-C1 reformulation).
- W8+: NQ-249b Cat C closed-form (post-bifurcation) + NQ-249f localization (Connection G + NQ-251).

### §7.4 Hard-constraint compliance after fixes

| Constraint | Pre-fix | Post-C1+C2+C3+M1 |
|---|---|---|
| 0 canonical edits | ✅ | ✅ |
| CN10 contrastive | ⚠ (§10.2 weak) | ✅ |
| F-1 not silently resolved | ✅ | ✅ |
| M-1 not silently resolved | ✅ | ✅ |
| MO-1 not silently resolved | ✅ | ✅ |
| Cat A/B/C distinctions explicit | ❌ (§7.1 misleading) | ✅ |
| Multi-formation default | ✅ | ✅ |

---

## §8. Verdict Justification + Realist Check

### §8.1 Verdict justification

**REVISE** is the correct verdict (not REJECT, not ACCEPT) because:

- **Not REJECT**: The file's framing (CN10 contrastive lock, BC-249-1 as Cat B target with Cat A subset) is structurally sound. The mass-gap parallel is a legitimate research direction that adds SCC-internal value (σ-tuple stability, R23 verification) independent of any YM aspirations. The empirical anchor (§8) and Cat C closed-form pathway (§7.3) are tractable W6-W8 efforts. CN10 language is mostly correct.
- **Not ACCEPT**: Three critical issues (C1 internal inconsistency in conjecture statement, C2 cross-file contradiction with NQ-253, C3 silent hypothesis chain in Cat A claim) block immediate Day 5+ promotion. Plus six majors (citations, scaling caveat, Goldstone dimension, R23 scope, compute budget, closed-form scope) that materially affect promotion-gate evidence quality.
- **REVISE**: With C1+C2+C3+M1 mandatory fixes (~4-6 hours of working-only edits, no canonical changes), the file becomes Day 5+ promotion-ready as a Cat B target with Cat A conditional subset. The M2-M6 + m1-m5 cleanups can be completed during W6 in parallel with NQ-249a empirical anchor.

### §8.2 Realist check — would a third-party SCC reader accept BC-249-1?

**Test:** Would a domain expert (graph spectral theory + symmetry-breaking + variational analysis) accept BC-249-1 as a meaningful, well-posed mass-gap analog?

**Pre-fix verdict:** **No.** The expert would object:
- "Conjecture statement has $\Delta_*$ depending on $(G,K)$ alone, but failure analysis acknowledges bifurcation collapse — pick one." (C1)
- "Pointwise positivity claimed Cat A but with Morse-0 + well-separated + multi-formation Goldstone hypotheses chained — those are not all Cat A." (C3)
- "Cycling at $K \to K+1$ presented without flagging that noiseless flow forbids it — presents an artifact as generic phenomenon." (C2)

**Post-fix verdict:** **Yes, with caveats.** With C1 reformulation (Variant A or B), C3 explicit hypothesis chain, C2 protocol-conditional cycling, and M1 corrected citations, BC-249-1 becomes a well-posed Cat B target. The expert would still flag M2 (thermodynamic limit scaling) and M4 (non-generic submanifold) as scope limitations — but these are honest scope caveats, not internal contradictions. Acceptance threshold met for "candidate Cat B target, well-separated regime, finite graph, post-C1 reformulation."

### §8.3 Final aggregate

**Verdict: REVISE.** Apply mandatory C1+C2+C3+M1 fixes before Day 5+ promotion-gate. Recommended M2-M6 + m1-m5 cleanups before W7 BC-249-1 Cat B effort begins. Path A (Cat A immediate) retracted; replaced with Cat A conditional. Path B (Cat B target) realistic at 3–4 weeks W7 in well-separated regime only — full-stratum extension a separate W8+ effort. Path C (Cat C closed-form) correctly placed at W8+ ~6-8 weeks once M6 reference correction is applied.

---

**Critic review log persisted: 2026-04-30 EOD.**
**Next action:** apply C1+C2+C3+M1 fixes to `THEORY/working/MF/scc_mass_gap_connection.md` (working-only, no canonical edits).
