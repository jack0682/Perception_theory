# sigma_multi_trajectory.md — σ_multi^A(t) Dynamic Trajectory Framework

**Status:** working draft (Cat B target in non-corner-saturated regime; Cat C corner-saturated regime; per Critic 7-agent verdict 2026-04-29 EOD + self-critique `09_session_self_critique.md`; promoted from `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Day 3 W5 deepening pass).
**Created:** 2026-04-29 (W5 Day 3 EOD).
**Author origin:** `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` (full multi-approach framework); revised in light of `11_NQ198fg_results_and_D5_withdraw.md` (NQ-198f V5b-T' on torus → μ ≈ 0; Theorem 4.6.1 setup notes torus ≠ free-BC).
**Canonical refs:** §11.1 Commitment 14 (single-formation σ; Day 4 morning Block 1 if approved adds (O5')(O7) per D-1+D-2); §11.1 Commitment 14-Multi (D-6a static σ_multi^A + σ_multi^D, Day 4 morning Block 1 if approved); §13 T-σ-Multi-1 (D-6a Goldstone-pair instability, Day 4 morning).
**Working refs:** `working/MF/multi_formation_sigma.md` (D-6a static framework; this file extends to dynamic).
**Predecessor**: `2026-04-28/30_T4_CH_correspondence_sigma_t.md` (Phase 8 T4); `33_Phase9_findings_integration.md` §3 (Phase 9 U4 simplified σ trajectory); `34_Phase10_findings.md` §3-§4 (Phase 10 V3 Hessian + V4 K-jump statistics).
**Open problems referenced:** MO-1 re-engaged at multi-formation level via stratified-space approach (§3.2); NQ-242 (W6+ Cat A path).

---

## §1. Question and Scope

### §1.1 Target

Define and characterize $\sigma^A_{\mathrm{multi}}(t)$ along a K-field gradient flow trajectory $\mathbf{u}(t) : [0, T] \to \widetilde\Sigma^K_M$ (shared-pool architecture per Phase 7 R1.3; per-formation pool is dynamically static per Theorem 4.5.1).

### §1.2 Why now (W6 priority post-CV-1.5.1)

D-6a static σ_multi^A + σ_multi^D framework (Commitment 14-Multi) is canonical-ready (Day 4 morning if approved). D-6b dynamic σ_multi^A(t) is defer-to-W6+; this working file is the **W6+ research seed** providing the framework for NQ-242 numerical anchoring + Cat A refinement.

### §1.3 Day 2-3 numerical anchors

- **V3 (Phase 10)**: Hessian-based σ-tuple at 10 sparse snapshots over $t = 100$. Lowest 4 eigenvalues only (simplified σ-tuple).
- **V4 (Phase 10)**: K-jump statistics from U2 long-time data: $\Delta t \propto t^{1.315}$, ΔK distribution dominated by single mergers.
- **U4 (Phase 9)**: Simplified σ-trajectory implementation; ~6 K-jump events over $t = 200$.

These provide operational $\sigma^A(t)$ but **no rigorous theory**. NQ-242 (W6+) full Hessian σ-tuple time-series + rigorous K-jump theory.

### §1.4 Out of scope (this working file)

- Cat A construction of deterministic K-jump σ-inheritance map (Path B in §4.6); requires rich-σ augmentation NQ-242 W6+.
- 3D K-field σ_multi^A(t) (NQ-244 connection; W6+).
- Full Whitney-stratified Morse on $\widetilde\Sigma^K_M$ (NQ-248 W7+).

---

## §2. Definitions

### §2.1 Smooth segment

**Definition 2.1**: Let $\mathbf{u}(t) \in \widetilde\Sigma^K_M$ be a K-field gradient flow trajectory under shared-pool architecture (Definition 4.5.2 in `2026-04-29/02_*` Paper §4). A **smooth segment** is a maximal open interval $(t_n^*, t_{n+1}^*) \subset [0, T]$ on which $K_{\mathrm{act}}(\mathbf{u}(t))$ is constant.

### §2.2 K-jump time

**Definition 2.2**: A time $t^* \in (0, T)$ is a **K-jump time** if $K_{\mathrm{act}}(\mathbf{u}(t^{*-})) > K_{\mathrm{act}}(\mathbf{u}(t^{*+}))$.

### §2.3 σ_multi^A(t) trajectory

**Definition 2.3**: On a smooth segment $(t_n^*, t_{n+1}^*)$ with $K_{\mathrm{act}} = K'$,
$$\sigma^A_{\mathrm{multi}}(t) := \sigma^A(\mathbf{u}(t)) = \big(\mathcal{F}_{\mathrm{total}}(\mathbf{u}(t));\ \{\sigma_j(u^{(j)}(t))\}_{j=1}^{K'};\ \{\sigma_{jk}(t)\}\big),$$
where $\sigma_j$ is the per-formation σ-tuple (Commitment 14) and $\sigma_{jk}$ is the cross-formation σ-tuple (Commitment 14-Multi if D-6a approved).

---

## §3. Five Approaches Framework

(Reproduced from `2026-04-29/04_*` §2 with primary selection rationale.)

### §3.1 Approach 1: Spectral perturbation theory (Kato-Rellich)

Smooth-segment continuity via analytic perturbation theorem. Eigenvalues admit real-analytic parameterization away from crossing manifolds; avoided crossings codim-1 generic in 1-parameter families.

### §3.2 Approach 2: Stratified-space approach (re-engages MO-1 multi-formation)

$\widetilde\Sigma^K_M$ stratified by $K_{\mathrm{act}}$. K-jump = stratum transition. **Explicit re-engagement of MO-1 at multi-formation level**.

### §3.3 Approach 3: Topological inheritance via cohomology

$\sigma^D$ inheritance via restriction-and-collapse map on conjugacy classes of wreath product.

### §3.4 Approach 4: Right-and-left limit definition (operational fallback)

Define $\sigma^A(t)$ as càdlàg via separate limits.

### §3.5 Approach 5: Spectral-measure functional limit

Spectral measure $\mu_t$ on $\mathbb{R} \times \mathrm{Irr}(\mathrm{Stab}) \times \mathbb{N}$.

### §3.6 Primary selection

**Approach 1 + 2 hybrid** (smooth-segment + K-jump). Approach 3 supplements σ^D layer. Approaches 4, 5 fallback.

### §3.7 Tool A3 PH Reformulation (W6+ integration)

**Reformulation of σ_multi^A(t) via centroid Vietoris-Rips persistent homology.**

Let $c^{(j)}(t) = \sum_i u^{(j)}_i(t) \cdot x_i / \sum_i u^{(j)}_i(t)$ be the centroid of formation $j$ at time $t$ (defined on smooth segments where $\sum_i u^{(j)}_i > 0$).

**Definition (PH reformulation):** The active formation count is recoverable as
$$K_{\mathrm{act}}(t) = \dim H_0\!\left(R_r\!\left(\{c^{(j)}(t)\}_{j=1}^K\right)\right) \quad \text{as } r \to \infty,$$
where $R_r(\cdot)$ denotes the Vietoris-Rips complex at scale $r$.

**K-jump events** = births/deaths in the $H_0$ barcode of $\{c^{(j)}(t)\}$ over time $t$: a merger $K \to K-1$ corresponds to a $H_0$ bar-death (two connected components merging).

**σ^A K-jump non-determinism** = standard PH fact: the $H_0$ (0th) barcode of centroids does **not** determine the $H_1$ (1st) barcode of the full cohesion field. Equivalently, the cluster-level topology (which formations exist and when they merge) does not determine the within-cluster topology (shape, holes, internal structure). This is the content of Lemma 4.2(c) Cat C — there exist configurations with identical $H_0$ barcode (same K-jump sequence) but distinct $\sigma^A(t^{*+})$. This fact is a corollary of Cohen-Steiner–Edelsbrunner–Harer 2007 stability (barcode stability under perturbation does not lift between homological degrees) and is operationalized via Carlsson–de Silva–Morozov 2009 zigzag persistence over K-jump events.

**Cross-ref:** `working/MF/mathematical_scaffolding_4tools.md` §4 Tool A3 (Persistent Homology) verification.

---

## §4. Substantive Lemmas

### §4.1 Lemma 4.1 (smooth-segment piecewise constancy)

**Hypotheses (working version):**
- (H1) $\mathbf{u}(t)$ is the gradient flow of $\mathcal{E}_K$ on shared-pool $\widetilde\Sigma^K_M$, smooth in $t$ on a smooth segment $(t_n^*, t_{n+1}^*)$.
- (H2) $\mathcal{E}_K$ is real-analytic on $\widetilde\Sigma^K_M$ (true for explicit form with $W$ polynomial).
- (H3) On the segment, $H_{\mathrm{joint}}(\mathbf{u}(t))$ has dimension $N := K' \cdot |X|$ constant.
- **(H4) [ADDED post `09_*` self-critique]** Trajectory $\mathbf{u}(t)$ remains in interior of $\widetilde\Sigma^K_M$ — bounded away from $u_i^{(j)} \in \{0, 1\}$ for all $i, j$, and $\sum_k u^{(k)}(x) < 1$ for all $x$. Excludes corner-saturated regime (V5b-T'/V5b-F).

**Claim:** $\sigma^A_{\mathrm{multi}}(t)$ is piecewise constant in $t$ on the segment, with discrete jump times at avoided crossings of $H_{\mathrm{joint}}$ eigenvalues.

**Proof sketch**: see `2026-04-29/04_*` §4.2 (4-step Kato-Rellich + Wigner-von Neumann argument).

**Cat status (revised W6+)**: Cat B target in interior regime; **OPEN in corner-saturated regime** (where (H4) fails). Per `09_*` §2.2 self-critique.

### §4.2 Lemma 4.2 (K-jump left/right limits + σ^A non-determinism)

**Hypotheses:**
- Same as Lemma 4.1.
- (H2k) $t^* \in (0, T)$ K-jump time with simple merger ΔK = 1.
- (H3k) Soft merger: $m_j(\mathbf{u}(t)) \to 0$ continuously as $t \nearrow t^*$.

**Claim (a) Left limit exists**: Cat A under Lemma 4.1 (smooth-segment piecewise-constant ⇒ single-side limits exist).

**Claim (b) Right limit exists**: Cat A under Lemma 4.1.

**Claim (c) σ^A inheritance non-determinism**: $\Phi: \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ is **conjectured** to be non-deterministic in $\sigma^A(t^{*-})$ alone; requires merger-geometry data $\mathcal{M}$.

**Cat status (revised W6+ post `09_*` §2.3)**: 
- (a), (b): Cat A (assuming Lemma 4.1 applies).
- (c): **conjectured (Cat C)** — explicit counterexample construction NQ-242c W6+. Status DOWNGRADE from earlier "Cat B sketch" labeling.

### §4.3 Proposition 4.3 (σ^D restriction at K-jump)

**Statement**: Under Lemma 4.2 hypotheses, $\sigma^D$ inheritance is given by conjugacy-class restriction map $\Psi$ induced by $S_{K'-1} \hookrightarrow S_{K'}$ followed by wreath-product projection.

**Caveat**: post-merger stabilizer may be **larger** than pull-back image (symmetry emergence; NQ-242d W6+).

**Cat status**: Cat B sketch.

### §4.4 Theorem 4.4 (σ_multi(t) trajectory; synthesis)

**Hypotheses:** Lemmas 4.1 + 4.2 + Proposition 4.3.

**Claim:** $\sigma_{\mathrm{multi}}(t) = (\sigma^A(t), \sigma^D(t))$ is càdlàg with:
- (i) Smooth-segment piecewise constancy (Cat B target in interior; open in corner regime).
- (ii) K-jump left/right limits (Cat A).
- (iii) σ^A inheritance non-determinism (conjectured Cat C).
- (iv) σ^D inheritance partial determinism (Cat B sketch).

**Cat status**: Cat B target overall, with caveat for corner-saturated regime.

---

## §5. Known Failure Modes (Self-Identified)

(Per `09_*` §2 + `11_*` §3.)

**FM1 — Analyticity in corner-saturated regime**: Lemma 4.1 (H4) excludes corner-saturated trajectories. V5b-T'/V5b-F dynamics live precisely in this excluded regime. **Lemma 4.1 may not apply where σ_multi^A(t) is most physically interesting**. Tool A3 PH note: finite-difference Hessian computation (NQ-242 Phase 1) also becomes unreliable in corner-saturated regime where $u_i^{(j)} \in \{0,1\}$ — PH barcodes are computable but the σ-tuple they encode has no rigorous analytic grounding. PH does not rescue the analyticity gap; it merely provides an alternative computational observable.

**FM2 — Lemma 4.2(c) non-determinism is asserted, not proved**: explicit two-trajectory construction with same $\sigma^A(t^{*-})$ and different $\sigma^A(t^{*+})$ is open (NQ-242c W6+). PH reframe: this is precisely the statement that the $H_0$ barcode (K-jump sequence) does not determine the $H_1+$ barcodes (within-cluster topology / σ-tuple) — a standard fact in persistent homology. The PH reframe converts FM2 from an ad hoc assertion into a corollary of a known theorem; the explicit counterexample (NQ-242c) provides the SCC-specific instantiation.

**FM3 — V5b-T' phantom (per `11_*`)**: NQ-198f shows V5b-T' (sub-lattice translation-invariant corner-saturated) has μ ≈ 0 trivially (cluster orbit Goldstone). The "PN-barrier-lifted Goldstone" in V5b-T'/F was a **mis-identified phenomenon**; V5b-T' as a separate regime does not exist. This affects σ_multi^A(t) at corner-saturated configurations: the cluster Goldstone modes are exactly zero on torus, not lifted. PH note: in the Vietoris-Rips framework, V5b-T-zero configurations correspond to a degenerate $H_0$ barcode where all bars are born at $r = 0$ and no bar dies at finite $r$ before $r \to \infty$ — PH naturally classifies this trivial-topology regime without requiring a separate V5b-T'/V5b-T-zero distinction.

**FM4 — Coefficient $C(\beta, \xi_0)$ in V5b-F regime is non-trivial (per `11_*`)**: NQ-198g $\beta$-scan shows $C/\beta$ varies from 4.0 (β=2) to 2.4 (β=6); not simply $C = \pi\beta$. PH note: NQ-198k W6+ PH classification quantifies cluster-level topology variation as a function of $\beta$; the $H_1$ barcode total persistence (loop content) is a proxy for $C(\beta, \xi_0)$ variation, giving a topological handle on the non-trivial coefficient.

---

## §6. Cat A Path (W6+)

### §6.1 NQ-242 (full Hessian σ-tuple time-series + rigorous K-jump theory; PH-augmented pipeline)

**Effort**: ~~4-6 weeks~~ **3-4 weeks** via PHAT/GUDHI/Ripser persistent homology library integration (reduces Phase 1-2 from manual implementation to library calls; Phase 3 σ-integration dominates remaining effort).

**Phases (PH-reframed)**:

**Phase 1 (W6 Days 1-3) — Centroid trajectory extraction + Vietoris-Rips PH:**
- Extract centroid sequence $\{c^{(j)}(t)\}_{j=1}^K$ from K=8 trajectory at 100+ time points.
- Compute $H_0$ Vietoris-Rips PH barcode via GUDHI/Ripser; identify K-jump events as $H_0$ bar-deaths.
- Compute full Hessian σ-tuple at 100+ time points (existing NQ-242 infrastructure, now anchored by PH K-jump timestamps).

**Phase 2 (W6 Days 4-7) — Zigzag persistence over K-jump events:**
- Apply Carlsson–de Silva–Morozov 2009 zigzag persistence to $H_0$ barcode across K-jump times.
- Characterize merger geometry $\mathcal{M}$ (centroid distance, approach angle, relative mass) at each K-jump.
- Verify that $H_0$ barcode is insufficient to determine $\sigma^A(t^{*+})$ (numerical pre-confirmation of FM2 / Lemma 4.2(c) Cat C).

**Phase 3 (W7 Days 1-5) — σ-tuple integration with PH barcodes (rich-σ):**
- Rich-σ augmentation candidates: σ-tuple + $H_1$ barcode persistence + cluster centroid geometry + total mass dispersion.
- Test whether rich-σ = (plain σ^A, $H_1$ barcode) gives deterministic K-jump inheritance map.
- Identify minimal augmentation achieving determinism (Cat A target).

**Phase 4 (W7 Day 6 – W8 Day 3) — NQ-242c explicit non-determinism counterexample:**
- Construct two explicit trajectories with identical $H_0$ barcode (same K-jump sequence) and identical plain $\sigma^A(t^{*-})$ but different $\sigma^A(t^{*+})$.
- This is the SCC-specific instantiation of the standard PH non-lift fact (FM2 reframe).
- Confirms Lemma 4.2(c) Cat C status; provides counterexample for CV-1.6 canonical text.

**Cat target**: Cat A or strong Cat B (for rich-σ); Cat C confirmed (for plain σ^A).

### §6.2 NQ-242c (σ^A non-determinism explicit construction)

**Effort**: 2-3 weeks.

If NQ-242 succeeds with rich-σ augmentation: NQ-242c demonstrates that **plain σ^A** (without augmentation) is genuinely non-deterministic by exhibiting two trajectories.

### §6.3 NQ-242d (σ^D symmetry emergence)

**Effort**: 2-3 weeks.

Characterize when post-merger stabilizer is strictly larger than pull-back image (symmetry gain).

### §6.4 NQ-248 (multi-formation Morse stratification)

**Effort**: 6-10 weeks (W7+).

Full Whitney-stratified Morse theory on $\widetilde\Sigma^K_M$ — generalize Goresky-MacPherson stratified Morse to SCC. Resolves MO-1 at multi-formation level.

---

## §7. Cross-References

### §7.1 Day 3 daily files

- `2026-04-29/04_D6b_sigma_trajectory_development.md` — full multi-approach framework (origin).
- `2026-04-29/06_open_problems_development_synthesis.md` §4.3 D-6b options.
- `2026-04-29/09_session_self_critique.md` §2.2 (analyticity caveat), §2.3 (Lemma 4.4.1c Cat C downgrade — source of all Cat C corrections in this file).
- `2026-04-29/11_NQ198fg_results_and_D5_withdraw.md` §3 (V5b-T' phantom; affects corner-saturated regime).

### §7.1bis Tool A3 and 4-tool mapping files

- `working/MF/mathematical_scaffolding_4tools.md` §4 Tool A3 (Persistent Homology) — verification framework for PH reformulation in §3.7 of this file.
- `THEORY/logs/daily/2026-04-30/02_4tool_mapping_summary.md` §3.3 — critical insights on PH non-determinism as standard mathematical fact (source of FM2 PH reframe).
- `THEORY/logs/daily/2026-04-30/01_canonical_promotion_log.md` CV-1.5.1 D-6a Multi-Static merge — canonical context for D-6b deferral to CV-1.6.

### §7.2 Day 2 source files

- `2026-04-28/30_T4_CH_correspondence_sigma_t.md` (Phase 8 T4).
- `2026-04-28/33_Phase9_findings_integration.md` §3 (Phase 9 U4 simplified σ trajectory).
- `2026-04-28/34_Phase10_findings.md` §3-§4 (V3 Hessian + V4 K-jump statistics).

### §7.3 Canonical (after Day 4 morning Block 1 if approved)

- §11.1 Commitment 14 (O5')(O7) — D-1, D-2.
- §11.1 Commitment 14-Multi static — D-6a (provides $\sigma_{\mathrm{multi}}$ definition).
- §13 T-σ-Multi-1 — D-6a (provides static instability theorem).

D-6b (this dynamic extension) is **deferred to CV-1.6** post-NQ-242.

---

## §8. Hard Constraint Compliance

- canonical 직접 수정 0 — this working file does not edit canonical.
- Silent resolution 0 — Lemma 4.1 corner-regime gap explicit (FM1); Lemma 4.2(c) Cat C explicit; V5b-T' phantom referenced (FM3).
- u_t primitive — definitions operate on $\mathbf{u}(t)$; PH centroids are derived from $u^{(j)}(t)$, not independent primitives.
- 4 energy terms not merged.
- K not dual-treated (K_act integer; K-jumps discrete).
- P-F flag inline at corner-saturated discussions.
- Reductive equation 0 — Modica-Mortola, equivariant cohomology cited as **structural correspondence**. PH is a *standard mathematical reformulation* of K-jump topology, not an external reduction or engineering proxy; it does not replace the SCC energy framework.
- MO-1 re-engaged explicitly via Approach 2 stratified-space.
- CN10 contrastive preserved — PH non-determinism fact (FM2 reframe) is cited as a standard result (Cohen-Steiner 2007, Carlsson 2009), not a novel SCC claim; contrastive structure with existing literature maintained.
- PH does not resolve open problems F-1, M-1, MO-1 — these remain open per `THEORY/canonical/open_problems.md`.

---

## §9. W6+ Roadmap (this file's evolution)

| W | Target |
|---|---|
| W6 Day 1-3 | NQ-242 numerical infrastructure (dense Hessian sampler, K-jump detector). |
| W6 Day 4-5 | NQ-242 first dataset analysis. |
| W6 Day 6-7 | NQ-242c explicit two-trajectory construction (if numerical anchor stable). |
| W7 | Rich-σ augmentation prototyping; Theorem 4.4 corner-regime extension via Approach 4 fallback. |
| W8 | Cat A draft; canonical proposal text for CV-1.6. |
| W9 | CV-1.6 release prep with D-6b mature. |

---

**End of sigma_multi_trajectory.md.**
**Status: working draft — Theorem 4.4 (σ_multi(t) trajectory) Cat B target in non-corner-saturated regime; Cat C in V5b-T-zero/V5b-F corner-saturated regime (per Critic 7-agent verdict 2026-04-29 EOD + self-critique `09_*`). Lemma 4.2(c) σ^A K-jump non-determinism: Cat C (conjectured; downgraded from "Cat B sketch" per `09_*` §2.3). Cat A path via NQ-242 W6+ PH-augmented pipeline (3-4 weeks via PHAT/GUDHI/Ripser). D-6b deferred to CV-1.6.**
**Promoted from `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` per CLAUDE.md promotion pipeline. Source daily file preserved with full multi-approach exposition; this working file is the topic-organized active development version. PH reformulation (§3.7) + FM1-FM4 PH context + NQ-242 Phase 1-4 breakdown added 2026-04-29 per Critic C3 recommendations.**
