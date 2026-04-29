# sigma_multi_trajectory.md — σ_multi^A(t) Dynamic Trajectory Framework

**Status:** working draft (Cat B target framework; promoted from `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Day 3 W5 deepening pass).
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

**FM1 — Analyticity in corner-saturated regime**: Lemma 4.1 (H4) excludes corner-saturated trajectories. V5b-T'/V5b-F dynamics live precisely in this excluded regime. **Lemma 4.1 may not apply where σ_multi^A(t) is most physically interesting**.

**FM2 — Lemma 4.2(c) non-determinism is asserted, not proved**: explicit two-trajectory construction with same $\sigma^A(t^{*-})$ and different $\sigma^A(t^{*+})$ is open (NQ-242c W6+).

**FM3 — V5b-T' phantom (per `11_*`)**: NQ-198f shows V5b-T' (sub-lattice translation-invariant corner-saturated) has μ ≈ 0 trivially (cluster orbit Goldstone). The "PN-barrier-lifted Goldstone" in V5b-T'/F was a **mis-identified phenomenon**; V5b-T' as a separate regime does not exist. This affects σ_multi^A(t) at corner-saturated configurations: the cluster Goldstone modes are exactly zero on torus, not lifted.

**FM4 — Coefficient $C(\beta, \xi_0)$ in V5b-F regime is non-trivial (per `11_*`)**: NQ-198g $\beta$-scan shows $C/\beta$ varies from 4.0 (β=2) to 2.4 (β=6); not simply $C = \pi\beta$.

---

## §6. Cat A Path (W6+)

### §6.1 NQ-242 (full Hessian σ-tuple time-series + rigorous K-jump theory)

**Effort**: 4-6 weeks.

**Phases**:
1. (W6 Days 1-3) Numerical infrastructure: dense Hessian σ-tuple sampling at 100+ time points per K=8 trajectory.
2. (W6 Days 4-7) K-jump event detection + characterization.
3. (W7) Rich-σ augmentation candidates: σ + cluster centroid, σ + cluster orientation, σ + total mass dispersion.
4. (W8) Cat A target: deterministic σ_rich K-jump map.

**Cat target**: Cat A or strong Cat B.

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
- `2026-04-29/09_session_self_critique.md` §2.2 (analyticity caveat), §2.3 (Lemma 4.4.1c Cat C downgrade).
- `2026-04-29/11_NQ198fg_results_and_D5_withdraw.md` §3 (V5b-T' phantom; affects corner-saturated regime).

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
- u_t primitive — definitions operate on $\mathbf{u}(t)$.
- 4 energy terms not merged.
- K not dual-treated (K_act integer; K-jumps discrete).
- P-F flag inline at corner-saturated discussions.
- Reductive equation 0 — Modica-Mortola, equivariant cohomology cited as **structural correspondence**.
- MO-1 re-engaged explicitly via Approach 2 stratified-space.

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
**Status: working draft — Theorem 4.4 (σ_multi(t) trajectory) Cat B target with explicit failure modes (FM1-FM4). Cat A path via NQ-242 W6+. D-6b deferred to CV-1.6.**
**Promoted from `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` per CLAUDE.md promotion pipeline. Source daily file preserved with full multi-approach exposition; this working file is the topic-organized active development version.**
