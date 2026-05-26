> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 04_integration_and_new_open.md — Integration with Canonical, OP Impact, New Open Questions

**Session:** 2026-05-07 (Thu, W6 Day 5)
**Target (from `00_plan.md` Option A):** Tighten T-Temporal-Identity to a narrow Cat B theorem; today's product is a Cat-B-ready working draft (not promoted).
**This file covers:** §4.5 of MAIN_PROMPT (Integration with existing system) + §4.6 (New open questions) + §14 (Prompt meta).
**Depends on reading:** `02_exploration.md`, `03_development.md` (this session); `canonical.md` §§3, 7.1, 8.5, 11, 13; `theorem_status.md` (Sessions V, X, Y notes; OP-0011, OP-0012); `working/MF/temporal_identity_perscomp_transport.md` §10.

---

## §1. Integration with canonical

### §1.1 Where Theorem T-Temporal-Identity attaches

When promoted to canonical (future session), the natural insertion point is:

- **`canonical.md` §13 Category B** as a new entry. Specifically, insert *after* the T-K-Select-OBS Cat B entry (Session Y, CV-1.11). The actual canonical-file location depends on whether §13's Category B section is ordered chronologically (current convention) or topically. Recommended: chronological, immediately after T-K-Select-OBS.

  *Suggested canonical-side text (≤ 80 lines, DO NOT INSERT NOW):*
  ```
  **T-Temporal-Identity. Persistent component identity via unbalanced transport (parts a, b, d narrowed; sharp form).**
  *(New in CV-1.12, Session ?, 2026-05-?? — promoted from Session V working candidate via 2026-05-07 sharp-form refinement.)*

  Let $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$ be soft cohesion fields on a finite shared graph $G$ (A1, A2). Let $\mathrm{PersComp}(u_t), \mathrm{PersComp}(u_s)$ be the D-ST-3 persistent-component sets, with $K_t \geq 1, K_s \geq 1$ (A3). Let $M_{t \to s}$ be an admissible transport plan satisfying (E1–E4) with entropic regularization $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^*$, where $\varepsilon_\mathrm{OT}^* = (\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff})/2$ is the sharp-OT certified regime (A7').

  Define the component score matrix $\tilde{\mathbf{S}} \in \mathbb{R}^{K_t \times K_s}$ via §4 of `THEORY/4_temporal/identity_inheritance/temporal_identity_perscomp_transport.md`. Then:

  **(a) Existence.** A relation $R_{t \to s} \subseteq \mathrm{PersComp}(u_t) \times \mathrm{PersComp}(u_s)$ exists (constructive, via thresholded $\tilde{\mathbf{S}}$) and exhaustively classifies every pair into one of five mutually-exclusive event types (continuation, split, merge, birth, death).

  **(b) Uniqueness under stable-K + margin.** Additionally assume $K_t = K_s = K$ (A4), the well-separated regime $d_\mathrm{inter}^* \geq d_\mathrm{min}^* \geq 3$ (A5), the dual-potential regularity (DR1)–(DR2) of `03_development.md` §8.1, the diagonal magnitude condition $\min_i \tilde S_{i, j^*(i)}^0 \geq \theta_\mathrm{diag}$ (MA1), and the **margin condition**:
  $$\Delta_\mathrm{sep}(M_{t\to s}) := \min(\Delta_\mathrm{sep}^\mathrm{row}, \Delta_\mathrm{sep}^\mathrm{col}) \geq \Delta_\mathrm{sep}^*$$
  where (sharp closed form):
  $$\Delta_\mathrm{sep}^* \geq \lambda_m\big[\rho_\mathrm{deep}(1 - \eta_\mathrm{self}^{\,K}) - \eta_\mathrm{cross}^\mathrm{sharp}\big] - \lambda_c \bar c_\mathrm{intra},\quad \eta_\mathrm{cross}^\mathrm{sharp} = \exp\!\big(-(\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff})/\varepsilon_\mathrm{OT}\big).$$
  Then $R_{t\to s}$ is a unique bijection $\pi: \{1,\ldots,K\} \to \{1,\ldots,K\}$ given by the row-argmax. The induced pairing satisfies (A8a)' (mass-positivity) and (A8a)'' (fingerprint-gap positivity) — see Lemma 7.

  **(c) Kernel independence.** *Cat C, pending OP-0011 Step 2 (component confinement bound on $|\gamma_M - \gamma_{M'}|$).*

  **(d) K=1 reduction.** When $K_t = K_s = 1$, $R_{t\to s}$ is non-empty $\iff$ $\mathsf{persist\_transport}(u_t,u_s,M_{t\to s},\theta_\mathrm{core}) \geq \tau_\mathrm{id}'$ where $\tau_\mathrm{id}' = (\tau_\mathrm{id} + \lambda_c \bar c_\mathrm{intra})/(\lambda_m \rho_\mathrm{deep,core}(1-\eta_\mathrm{self}))$.

  *Proof:* Lemmas 1–7 + Theorem 4.2 (sharp form) of `THEORY/logs/daily/2026-05-07/03_development.md`; chains T-Persist-1(e) Cat A + Sinkhorn-Lipschitz Lemma 8.2 (sharp form) + finite-matrix bijection Lemma 4.

  *Status:* **Category B** — conditional on (A1)–(A8)+(A7')+(MA1) + (DR1)–(DR2). Cat A path: (i) absorb D-ST-3 into canonical state-space (S-A1, S-A2); (ii) tighten iso-ratio dependence (S-B1); (iii) promote Lemma 8.2 to Cat A (S-B2); (iv) resolve OP-0011 Step 2 (S-B3, also unblocks part (c)); (v) eliminate (MA1) (S-B4, NQ-T-Identity-5 full). Aggregate Cat A timeline: ~7 sessions for parts (a,b,d), ~9 sessions including (c). Composition theorem **OP-0012-CC partially resolved** via Lemma 6 (`03_development.md` §10) under stable-K + margin on both intervals.

  *Numerical anchor:* exp83 ALL PASSED (Session X, 2026-05-06) at $\varepsilon_\mathrm{OT} = 1$ (outside certified regime; observed $\Delta_\mathrm{sep} = 0.726$ in Scenario A consistent in order of magnitude with theoretical $\geq 0.837$ at $\varepsilon_\mathrm{OT} = 0.1$). Recommended canonical-side anchor (P3): exp83-variant at $\varepsilon_\mathrm{OT} \in [0.01, 0.1]$ inside the certified regime.

  *Implementation:* `CODE/scc/transport.py` (sinkhorn_partial_ot, persist_transport); component-score-matrix to be added to `scc/temporal_identity.py` (new module, deferred). exp83 implementation: `CODE/experiments/exp83_temporal_identity_transport.py` (Session X).
  ```

- **`canonical.md` §3 (formal universe)** does NOT need modification: the relation $R_{t\to s}$ is defined on top of existing primitives ($\mathcal{F}_M(\mathcal{P})$, PersComp, $M_{t\to s}$). No new primitive is introduced.

- **`canonical.md` §11 (commitments)** does NOT need modification.

- **`canonical.md` §8.5 (E1–E4)** does NOT need modification, but a *cross-reference* entry would help: "T-Temporal-Identity Cat B uses (E1–E4) admissibility."

- **`theorem_status.md`**: a new row in the Cat B table after T-K-Select-OBS, plus the OP-0011 status note moved from "STRUCTURED" to "STRUCTURED — component confinement is the sole remaining step for part (c)". OP-0012 unchanged.

### §1.2 Strengthens / weakens / retires no canonical theorem

- **Strengthens:** None (additive).
- **Weakens:** None.
- **Retires:** None.
- **Modifies:** None directly. `theorem_status.md` reclassifies OP-0011 sub-status (Step 2 isolated as the sole remaining step for part (c)).

### §1.3 Tension with existing canonical statements

The following are checked for consistency with the proposed Cat B claim:

1. **T-Persist-1(e) Cat A** (canonical §13 lines 1802–1824): consistent. Theorem 4.2 inherits T-Persist-1(e) as a black box. The conditional regime (A7'): $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^*$ matches T-Persist-1(e)'s sharp-concentration regime.

2. **T-Persist-K-Sep Cat C** (canonical §13 lines 1781–1784): consistent. (A5) well-separated is *exactly* the WS regime defined here.

3. **T-Persist-1(d) Cat C ($\beta > 7\alpha$)** (canonical §13 line 1799): we use H2' (deep-core existence) but NOT H3 (interior gap requiring $\beta > 7\alpha$). Lemma 2's $\rho_\mathrm{deep}$ uses Theorem 2b (Deep Core Dominance, conditional on iso-ratio $\leq C$) — this is conditional but does not require $\beta > 7\alpha$. Hence Theorem 4.2 stays Cat B (does not propagate Cat C from T-Persist-1(d)).

4. **CN5 (4 energy terms conceptually independent)**: consistent. The score $S_{ij}$ uses transport mass and fingerprint cost — both transport-energy (E_tr-related) artifacts; not a new merging of energy terms.

5. **CN10 (no reductive equivalence to external frameworks)**: consistent. We do not equate $R_{t\to s}$ with PH bottleneck matching, with Hungarian assignment, or with Markov chains. Approaches 2, 3, 5 are *internal* lemmas / alternative paths, not reductive identifications.

6. **Primitive ordering (u_t primitive, objects derivative)**: consistent. $R_{t\to s}$ is a *derivative* relation on persistent components, which themselves are derivative (D-ST-3). Components are not primitives.

7. **K is integer** (canonical commitments): consistent. $K_t, K_s$ are integer counts; (A4) treats them as integers and the bijection is on integer index sets. No "K ∈ continuous" smuggling.

### §1.4 Section header impact

If promoted, the canonical version increment is **CV-1.12** (one Cat B addition):

- CV-1.11 (current, Session Y): 54A / 14B / 5C / 5R = 78 claims.
- CV-1.12 (post-promotion): 54A / **15B** / 5C / 5R = 79 claims.

This is consistent with `00_plan.md`'s expected delta (14B → 15B).

---

## §2. Open Problem impact

### §2.1 OP-0011 — Transport kernel uniqueness

**Pre-session status (Session V, 2026-05-06):** STRUCTURED — component confinement path identified (3-step plan; Step 1 site-level, Step 2 component-level [OPEN], Step 3 identity-level conditional on Δ_sep > ε_kernel).

**Today's impact:** No new resolution. Today's session **isolates** OP-0011 Step 2 as the *sole* remaining sub-step for part (c) of T-Temporal-Identity to be promoted from Cat C to Cat B. Specifically:

- Step 1 (site-level): T-Persist-1(e) Cat A bound — already canonical.
- Step 2 (component-level): bound $\vert \gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)\vert \leq \epsilon_\mathrm{kernel}(C_i^t, C_j^s)$ for two E1–E4-admissible plans $M, M'$. **OPEN**. The candidate approach is a covering argument: $\vert \gamma_M - \gamma_{M'}\vert \leq \lvert C_i^t \rvert \cdot \lVert M - M' \rVert_{\infty,C_i^t \times C_j^s}$, but a Cat B-grade bound requires connecting to the site-level confinement bound $C_\mathrm{conf}\sqrt{m}$ properly.
- Step 3 (identity-level): once Step 2 closes, $\Delta_\mathrm{sep} > \epsilon_\mathrm{kernel}$ implies $R_{t\to s}[M] = R_{t\to s}[M']$. This is now expressible via Theorem 4.2's closed-form $\Delta_\mathrm{sep}^*$.

**Refined OP-0011 sub-status entry (suggestion for `theorem_status.md`):**

> **OP-0011** Status: STRUCTURED — Step 1 (T-Persist-1(e) Cat A, canonical); Step 2 (OPEN, component confinement bound: $\vert \gamma_M - \gamma_{M'}\vert \leq \epsilon_\mathrm{kernel} \cdot \min(m_i^t, m_j^s)$, candidate via covering argument over $C_i^t \times C_j^s$ blocks of the site-level bound $C_\mathrm{conf}\sqrt{m}$); Step 3 (CONDITIONAL: $\Delta_\mathrm{sep} > \epsilon_\mathrm{kernel} \Rightarrow R[M] = R[M']$, closed-form via T-Temporal-Identity Theorem 4.2 (working draft 2026-05-07)). Feeds into T-Temporal-Identity part (c) Cat C → Cat B promotion.

### §2.2 OP-0012 — Persistence composition

**Pre-session status (Session V, 2026-05-06):** PARTIALLY STRUCTURED — OP-0012-CC compositional consistency Cat B path identified; full general composition Cat C.

**Today's impact (refined sophistication layer):** **PARTIALLY RESOLVED via Lemma 6** (`03_development.md` §10). Under hypothesis package (I_{ts})+(I_{sr}) — stable-K + margin condition on both intervals + basin-containment intermediate — bijection composition holds exactly:
$$R_{t \to r}[M_{s\to r} \circ M_{t\to s}] = R_{s \to r}[M_{s\to r}] \circ R_{t \to s}[M_{t\to s}].$$

The proof is a direct application of Theorem 4.2 on each interval + Lemma 4 (bijection composition is a bijection). Critical sub-step: showing E1–E4 admissibility is preserved under transport-plan composition (Lemma 6 §10.2 verifies this).

**Refined OP-0012 status (suggestion for `theorem_status.md`):**

> **OP-0012** Status: PARTIALLY RESOLVED (Lemma 6, `03_development.md` §10, 2026-05-07) — OP-0012-CC Cat B holds under stable-K + margin on both intervals + basin-containment intermediate. Full general composition (K-jumps between $t,s,r$; intermediate without basin-containment) remains Cat C. Markov-kernel formulation deferred to post-OP-0021. *Cat A path:* eliminate basin-containment intermediate hypothesis (= S-B3 OP-0011 Step 2 + S-B4 NQ-T-Identity-5).

**OP-0012 remains OPEN for:**
- (i) general K-jumps (split/merge between $t, s, r$);
- (ii) intermediate $u_s$ that does not satisfy basin-containment;
- (iii) Markov-kernel / Chapman–Kolmogorov composition under stochastic (Package II) transport.

### §2.3 OP-0008 — σ^A K-jump inheritance

**Pre-session status (Session W, 2026-05-06):** PARTIALLY STRUCTURED — OP-0008-CONT/MERGE/SPLIT/DIST sub-problems registered.

**Today's impact:** No direct change. Today's Theorem T-Temporal-Identity Cat B is **prerequisite** for T-σ-Inherit Cat B (which uses $R_{t\to s}$ as input). Specifically, T-σ-Inherit's Cat B path becomes more concrete once T-Temporal-Identity (a, b, d) is canonical: σ-inheritance via $\Phi(C_i^t \to C_{\pi(i)}^s)$ uses the bijection $\pi$ from Theorem 4.2.

**Cross-OP relationship:** OP-0008 ⊃ T-σ-Inherit which depends on T-Temporal-Identity which uses T-Persist-1(e). This dependency chain is now explicit.

### §2.4 OP-0009 — Multi-formation ontological foundations

**Pre-session status:** Active. OP-0009-A (architecture decision); OP-0009-K (resolved via Commitment 16).

**Today's impact:** No direct change. Today's session uses K-field language only insofar as integer $K_t, K_s$ are observable counts (D-ST-3) — does not use K-field slot-indexing as a primitive. Compatible with K-field quotient formalism (W6 D3 G3.2).

### §2.5 OP-0021 — Stochastic dynamics ($T_*$)

**Pre-session status:** UNDER INVESTIGATION (W9+ priority).

**Today's impact:** No dependency. Theorem T-Temporal-Identity Cat B (a, b, d) is *deterministic-transport-conditional* — uses any E1–E4 admissible plan $M_{t\to s}$, including but not requiring stochastic / Langevin plans. $T_*$ does not appear.

**Future link:** When OP-0021 closes and Package II provides stochastic transport plans, these can be plugged into Theorem 4.2 — provided the plan satisfies E1–E4 in expectation. This is a Cat B extension (stochastic-T-Temporal-Identity), deferrable to W9+.

### §2.6 OP-0005 — K-Selection (EQ / DYN / OBS)

**Pre-session status:** OP-0005-EQ partially resolved (T-K-Select-PF Cat B); OP-0005-DYN OPEN; OP-0005-OBS partially resolved (T-K-Select-OBS Cat B).

**Today's impact:** No direct change. Today's Theorem assumes $K_t, K_s$ are *given* (computed from $u_t, u_s$ via D-ST-3). The *selection* of $K^*$ is OP-0005, separate.

**Cross-link:** T-K-Select-PF gives $\{p_K\}$ (Gibbs sector mass) and T-K-Select-OBS gives $\{p_K(\mathfrak{O}_t)\}$ (posterior). Today's Theorem provides the *temporal correspondence* layer once $K_t$ and $K_s$ are individually selected. The full SCC pipeline (selection at $t$ → correspondence to $s$ → selection at $s$ → ...) is a multi-step composition addressed by future T-MF-Synthesis Cat A (out of scope today).

### §2.7 OP impact summary table (post evening-session closures)

| OP | Pre-session | Post-session (today, **post-closure**) | Change |
|----|-------------|----------------------|--------|
| OP-0005-EQ | partially resolved (T-K-Select-PF) | unchanged | no change |
| OP-0005-DYN | OPEN | unchanged | no change |
| OP-0005-OBS | partially resolved (T-K-Select-OBS) | unchanged | no change |
| OP-0008 | PARTIALLY STRUCTURED | unchanged (T-Temporal-Identity is prerequisite for T-σ-Inherit Cat B) | dependency clarified |
| OP-0009 | Active | unchanged | no change |
| **OP-0011** | STRUCTURED | **PARTIALLY RESOLVED via Lemma 10 (`06_close_OP0011_step2.md`)** — explicit closed-form $\epsilon_\mathrm{kernel} = 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$; trivially zero in self-referential cost regime ($\delta=0$). Definitional refinement of E3 (Route B) further trivializes uniqueness. **Step 2 CLOSED.** | **CLOSURE UPGRADE** |
| **OP-0012** | PARTIALLY STRUCTURED | **PARTIALLY RESOLVED via Lemma 6** under stable-K + margin on both intervals | resolution upgraded |
| OP-0021 | UNDER INVESTIGATION | unchanged (no dependency) | no change |

### §2.8 NQ-T-Identity closure summary

| NQ | Pre-evening-session | Post-evening-session | Closure file |
|----|---------------------|----------------------|--------------|
| NQ-T-Identity-1 (OP-0011 Step 2) | OPEN | **CLOSED** (Cat B via Lemma 10; Route A) | `06_close_OP0011_step2.md` |
| NQ-T-Identity-2 (iso-ratio non-grid) | OPEN | unchanged (S-B1, deferred) | — |
| NQ-T-Identity-3 (time-varying topology) | OPEN | unchanged (W9+ priority) | — |
| NQ-T-Identity-4 (large $\varepsilon_\mathrm{OT}$ robustness) | OPEN | **PARTIALLY CLOSED** — 4a closed via sharp form §8 + Theorem ER Cat C; 4b open low priority | `07_close_NQ4_robust.md` |
| NQ-T-Identity-5 (margin-alone implies pairing) | partial via Lemma 7 | **CLOSED** (Cat B via Lemma 8) | `05_close_NQ5_full.md` |
| NQ-T-Identity-6 (spectral-gap Cat A path) | sketched (§12) | **PARTIALLY ADVANCED** — Lemma 13 sketched with 4 critical gaps identified | `08_NQ6_spectral_gap_advance.md` |

**Aggregate today's NQ closures:** 2 fully closed (NQ-1, NQ-5), 1 partially closed (NQ-4), 1 advanced (NQ-6), 2 unchanged (NQ-2, NQ-3).

### §2.9 T-Temporal-Identity status post-closure: all-Cat-B

After today's evening-session closures:
- Part (a) — Cat B (unchanged).
- Part (b) — Cat B (cleaner hypothesis package after Lemma 8: margin-only).
- Part (c) — **Cat C → Cat B** via Lemma 11 (today's closure).
- Part (d) — Cat B (unchanged).

**Theorem T-Temporal-Identity is now all-Cat-B, ready for promotion-session review.** Promotion target: CV-1.12 (one Cat B addition, +1B → 54A/15B/5C/5R = 79 claims).

---

## §3. New open questions

Six open questions surfaced during today's development. Numbered NQ-T-Identity-1 through NQ-T-Identity-6. Each is a candidate for a future `plan.md`.

### §3.1 NQ-T-Identity-1 — Component confinement bound (OP-0011 Step 2)

**Question.** Find an explicit, instance-computable upper bound on $\vert \gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)\vert $ for two E1–E4-admissible plans $M, M'$ on the same fields and cost.

**Why it matters.** This is the sole remaining sub-step to promote T-Temporal-Identity part (c) from Cat C to Cat B (kernel independence under margin condition).

**Candidate approach.** Covering argument: site-level bound $\lVert \tilde u - \hat u_t \rVert \leq C_\mathrm{conf}\sqrt{m}$ (T-Persist-1(e)) → component-level bound by summing over $C_i^t \times C_j^s$ block. Complication: $C_\mathrm{conf}$ depends on $\sigma, \varepsilon_\mathrm{OT}$ and the bound's tightness depends on iso-ratio of $C_i^t \times C_j^s$.

**Estimated difficulty.** 1–2 sessions. Mid difficulty.

### §3.2 NQ-T-Identity-2 — Iso-ratio dependency on non-grid graphs

**Question.** Theorem 4.2 uses Deep Core Dominance Theorem 2b conditional on iso-ratio $\leq C$. For non-grid graphs (random graphs, expanders, hyperbolic graphs), iso-ratio can be unbounded. Does Theorem 4.2 fail in that regime, and if so, what is the natural replacement bound?

**Why it matters.** Robustness of T-Temporal-Identity to graph topology beyond 2D grids; affects perceptual-stack applicability to non-Euclidean substrates.

**Candidate approach.** For high iso-ratio, the deep-core mass fraction $\rho_\mathrm{deep}$ may be small. Replace with a *direct* T-Persist-1(e) site-level bound and avoid the deep-core-dominance step. Yields a weaker $\Delta_\mathrm{sep}^*$ but iso-ratio independent.

**Estimated difficulty.** 1 session. Mid difficulty.

### §3.3 NQ-T-Identity-3 — Time-varying graph topology

**Question.** Today's (A1) restricts to $\mathcal{P}_t = \mathcal{P}_s$. Real perceptual streams have changing graph topology (occlusion = vertex deletion; new objects = vertex addition). Extend T-Temporal-Identity to $\mathcal{P}_t \neq \mathcal{P}_s$ via a graph-correspondence morphism.

**Why it matters.** Required for the SCC → RelationWorld pipeline (perception-stack §3.5.1).

**Candidate approach.** Embed both graphs in a *common ambient* graph $\bar G$ (union of vertices + epsilon-extended edges) and lift the transport plan to $\bar G$. Persist-Comp and core sets defined on $\bar G$. Theorem 4.2 applies in $\bar G$.

**Estimated difficulty.** 2–3 sessions. Higher difficulty (requires architecture commitment in OP-0009-A).

### §3.4 NQ-T-Identity-4 — Robustness outside (A7') (large $\varepsilon_\mathrm{OT}$)

**Question.** exp83 PASS at $\varepsilon_\mathrm{OT} = 1.0$ is empirical evidence that Theorem T-Temporal-Identity holds *outside* the certified regime (A7'): $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^* \approx 0.05$ at default parameters. Find a tighter bound that certifies the theorem at $\varepsilon_\mathrm{OT}$ up to $O(1)$.

**Why it matters.** Practical applicability: exp implementations often use $\varepsilon_\mathrm{OT} = 0.5$–$1.0$ for numerical stability. Current theorem says nothing in that range.

**Candidate approach.** (i) Direct Sinkhorn-Lipschitz bound at moderate $\varepsilon_\mathrm{OT}$ — replacing the union bound (factor $n$) with a tighter row-wise bound. (ii) Empirical robustness theorem: a Cat C result that says "if observed $\Delta_\mathrm{sep}$ is large, the bijection holds" without explicit closed-form lower bound.

**Estimated difficulty.** 2 sessions. Mid difficulty.

### §3.5 NQ-T-Identity-5 — Margin condition without explicit pairing-existence

**Question.** Today's (A8) postulates the *existence* of a pairing $\pi$ with positive inter-component fingerprint gap. Can the margin condition $\Delta_\mathrm{sep}(M_{t\to s}) > 0$ alone (without (A8)) imply existence + uniqueness of bijection?

**Why it matters.** (A8) is *structural* — instance-checkable but not instance-derivable from $u_t, u_s, M$. A theorem with margin alone would be more elegant.

**Candidate approach.** Show that $\Delta_\mathrm{sep}^\mathrm{row} > 0$ AND $\Delta_\mathrm{sep}^\mathrm{col} > 0$ (combined margin condition) is equivalent to (A8) under (A1)–(A7). Lemma 4 already gives the bijection from row+column margins; the "(A8) ⇒ margin > 0" direction is Theorem 4.2; the converse "margin > 0 ⇒ (A8)" is an open implication.

**Estimated difficulty.** 1 session. Low-mid difficulty.

### §3.6 NQ-T-Identity-6 — Spectral-gap-based Cat A path

**Question.** Proposition 12.1 (`03_development.md` §12) sketches a Cat A promotion path for T-Temporal-Identity that bypasses Sinkhorn dual-potential machinery (Lemma 8.2, currently Cat B) and instead uses the joint Hessian spectral gap $\mu_\mathrm{joint}$ (T-Persist-K-Sep). Formalize this path.

**Why it matters.** The current Cat A path bottleneck (S-B2: promote Lemma 8.2 to Cat A) requires importing a non-canonical analytic ingredient (Bigot–Cazelles–Papadakis Lipschitz bound). A spectral-gap-based proof would bypass this entirely, using only canonical Hessian-analysis machinery already present in T-Persist-K-Sep / T-Persist-K-Weak.

**Candidate approach.** Linearized transport-Hessian analysis around the formation manifold $\Sigma_M^K$. Show that the entropic-OT optimum $M^*$ is a Boltzmann-distributed perturbation around the deterministic core-to-core map, with effective "temperature" $\varepsilon_\mathrm{OT}$ and "energy" controlled by $\mu_\mathrm{joint}$. The off-diagonal mass bound becomes $\eta_\mathrm{cross} \leq \exp(-\mu_\mathrm{joint} d_\mathrm{inter}^{*\,2}/\varepsilon_\mathrm{OT})$.

**Estimated difficulty.** 1–2 sessions. Mid-high difficulty (linearized-transport-Hessian formalization is non-trivial but well-precedented in Allen-Cahn / gradient-flow literature; CN10 contrast-not-reduce constraint must be respected).

**Connection to other NQs.** NQ-6 → eliminates dependency on NQ-1 via S-B3 OP-0011 Step 2 (since spectral-gap analysis gives kernel independence as a direct corollary of Hessian uniqueness — provided the optimal plan is Hessian-unique). May also subsume NQ-5 (margin-alone) by providing a structural reason for margin positivity.

### §3.7 NQ priority ranking (post-closure, final)

For tomorrow's `plan.md` (W6 D6 / W7 D1 — 2026-05-08):

| Rank | NQ | Status today | Reason |
|------|----|--------------|---|
| ~~1~~ | ~~NQ-T-Identity-5~~ | **CLOSED** (Lemma 8) | — |
| ~~2~~ | ~~NQ-T-Identity-1~~ | **CLOSED** (Lemma 10) | — |
| **1** | **NQ-T-Identity-6** | PARTIALLY ADVANCED | Lemma 13 sketched with 4 gaps; full closure 1–2 sessions; ~50–60% probability of success; if closes, collapses Cat A timeline 5 → ~3 sessions and removes $\varepsilon_\mathrm{OT}^*$ ceiling. **High-reward.** |
| **2** | **T-σ-Inherit Cat B Review** (Option B from `00_plan.md`) | now feasible | T-Temporal-Identity Lemma 8 form (margin-only) gives clean input to T-σ-Inherit; exp84 ALL PASSED provides anchor; 1 session estimated. **Lower-risk path forward.** |
| 3 | NQ-T-Identity-2 (iso-ratio non-grid, S-B1) | OPEN | Required for S-B1 in part (b) Cat A path. 1 session, low-mid difficulty. |
| 4 | NQ-T-Identity-4b (large-$\varepsilon_\mathrm{OT}$ analytical) | OPEN low priority | Subsumed if NQ-6 closes. |
| 5 | NQ-T-Identity-3 (time-varying topology) | OPEN | W9+ priority; defer to OP-0009-A architecture maturation. |

**Tomorrow's seed (recommended, refined after sophistication layer).** Three candidates:
- (Option A') NQ-T-Identity-5 full (MA1-free, building on today's Lemma 7): close the cleanest margin-only version of T-Temporal-Identity Cat B before promotion. **Estimated:** 1 session, low-mid difficulty.
- (Option A'') NQ-T-Identity-6 (spectral-gap Cat A path, building on §12.3): potentially collapses Cat A timeline. **Estimated:** 1–2 sessions, mid-high difficulty. **Higher reward / higher risk.**
- (Option B') T-σ-Inherit Cat B Review (Option B from today's plan, postponed): now natural since T-Temporal-Identity has a tightened Cat B draft for $R_{t\to s}$. **Estimated:** 1 session.

**Suggested seed:** Option A' (NQ-5 full) **then** Option B' (T-σ-Inherit) sequentially. NQ-6 is ambitious; logged but not recommended for immediate next session unless user has high risk tolerance.

---

## §4. Prompt improvement notes (MAIN_PROMPT v2 candidates)

Per MAIN_PROMPT §14 (meta), I record items where the prompt was actionable / unclear / over-specified.

### §4.1 Actionable as-is

- **§3 (entry procedure):** the explicit reading-order instruction worked well. Reading `plan.md` first, then canonical, theorem_status, working files in sequence prevented misreading the target.
- **§4 (multi-approach + primary selection):** the requirement to enumerate ≥3 mathematically independent approaches forced honest comparison and prevented anchoring on the obvious analytical path. The independence audit table (§2.6 of `02_exploration.md`) is a useful artifact.
- **§6 (output convention):** the 3-core-files-plus-99 structure is clear and matches the granularity of the work.
- **§7 (rigor standard):** Cat self-classification and explicit assumption-list discipline kept the development from drifting to Cat C silently.
- **§8 (hard constraints):** all 10 prohibitions held without conflict.

### §4.2 Slight ambiguity

- **§6 file naming.** The prompt prescribes `01_exploration.md`, `02_development.md`, `03_integration_and_new_open.md`. But the daily directory already had `00_plan.md` and `01_pre_brainstorm.md` (created EOD 2026-05-06 by the user). Today I used `02_exploration.md`, `03_development.md`, `04_integration_and_new_open.md` to avoid filename collision. **Suggestion for v2:** prefix output files with `out_` (e.g., `out_01_exploration.md`) OR explicitly state "if 01-numbering is taken, increment by 1". The current ambiguity required a judgment call.
- **§4.5 "successful 3 ≥ approaches" criterion.** "Mathematically independent" was clear; the independence-audit table format is my own — would benefit from a recommended structure. **Suggestion:** prescribe a small audit table in the prompt.
- **§13 (when to stop).** "10 substantive subsections in 02_development.md" is a useful target but the optimal session product is task-dependent. Today's `03_development.md` has 7 numbered top-level sections (§1–§7) but each contains substantive sub-parts. The 10-subsection rule should be measured at the appropriate granularity.

### §4.3 Over-specified

- **§4.6 (≥3 new open questions).** I generated 5 today; the prompt says "collect" without minimum. Today's count met the spirit. No over-specification.
- **§9 (follow-up Q&A granularity).** The prompt requests "each claim independently verifiable". Today's Lemmas 1–5 + Theorem 4.2 + counterexample audit have natural granularity but are individually quite long (Lemma 2 proof has 6 steps). For follow-up "verify Lemma 2 step 4", granular is fine. **No over-specification.**

### §4.4 Genuine missing item

- **No explicit prompt section on numerical-anchor handling.** Today exp83 (Session X anchor) was *outside* the certified regime (A7'). The prompt's §12.2 ("Treating toy experiments as proofs") covers the negative case but not the *robustness gap* case where empirical PASS extends beyond theory. Would benefit from a prompt addition: "When empirical anchors extend beyond theoretical regime, register as robustness observation, not as proof, and flag the regime gap explicitly."
- **No explicit guidance on Cat A vs Cat B promotion path within a Cat B claim.** Today's theorem self-classified Cat B; the path to Cat A (per part) was articulated in §6.3. Would benefit from a prompt addition: "For each Cat B claim, sketch the Cat A path explicitly (what additional work / sub-step / OP closure is required)."

### §4.5 Recommended v2 prompt patches

For `THEORY/logs/daily/MAIN_PROMPT.md` (next session candidate edits):

1. **§6 (output naming):** Add: "If filename `0N_<role>.md` is already taken, prefix outputs with `out_` (e.g., `out_01_exploration.md`) to disambiguate."
2. **§4.2 (multi-approach):** Add: "Conclude §4.2 with a pairwise independence audit table (rows = approach pairs, columns = same-idea / same-failure-mode / same-conditional / independent verdict)."
3. **§7 (rigor):** Add to item 5 (uncertainty levels): "For each Cat B claim, identify the explicit Cat A promotion path (sub-steps, blockers, expected difficulty)."
4. **§12 (error patterns):** Add: "Error 7. Conflating empirical robustness with theoretical certification. When experiments PASS outside the theoretical regime of certification (e.g., entropic regularization larger than the sharp-OT bound), register as 'robustness observation' and flag the regime gap; do not silently extend the theorem to the empirical regime."
5. **§13 (stopping):** Restate granularity: "10+ substantive subsections" → "approximately 7–10 numbered top-level sections in `0X_development.md`, each with multiple verifiable claims/lemmas/sub-steps."

---

## §5. Output handover to `99_summary.md`

`99_summary.md` shall produce: 3–5 sentence summary + tomorrow's seed (NQ-T-Identity-5 OR Option B from `00_plan.md`).

Key facts to surface:
1. Theorem T-Temporal-Identity Cat B (parts a, b, d) tightened with assumption package (A1)–(A8)+(A7') and explicit closed-form $\Delta_\mathrm{sep}^*$.
2. Counterexample audit: no refutation in scope; three regime-checks (Stress 1, 2, 4) confirm theorem boundary.
3. OP-0011 Step 2 isolated as sole remaining sub-step for part (c) Cat B.
4. exp83 numerical anchor confirmed in *order of magnitude*; certified regime tighter than empirical (A7' demands $\varepsilon_\mathrm{OT} \leq 0.05$ at default params, exp83 used $\varepsilon_\mathrm{OT}=1$).
5. No canonical promotion today; product is Cat-B-ready *working draft*.
6. Tomorrow's seed: NQ-T-Identity-5 (margin alone implies pairing) OR T-σ-Inherit Cat B Review.

---

*End of `04_integration_and_new_open.md`.*
