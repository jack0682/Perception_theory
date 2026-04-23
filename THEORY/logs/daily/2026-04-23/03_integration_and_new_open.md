# 03 — Integration and New Open Questions

**Session:** 2026-04-23
**Target:** Stage 2 Axiom Audit follow-up, 6-goal synthesis. Prepare canonical merge proposals + collect new open questions + explicit silent-resolution audit.
**This file covers:** (§2) Integration proposals to canonical by section; (§3) impact on existing open problems (F-1/M-1/MO-1/OP-0001..0022/N-1/P-A..P-H); (§4) silent-resolution audit; (§5) new open questions consolidated; (§6) retraction list update; (§7) prompt template improvement suggestions.
**Depends on:** `01_exploration.md` (methodology), all deliverables (`SF_layer_classification.md`, `SF_function_taxonomy.md`, `MF_multi_quantization.md`, `T_time_evolution.md`, `T_thermal_softmax.md`, `A_application_scoping.md`), `canonical.md` §11–§14.

---

## §1. Session output inventory

Produced today (`THEORY/logs/daily/2026-04-23/`):

1. `plan.md` (user) — 6-goal plan.
2. `pre_brainstorm.md` (user) — hypothesis exploration.
3. **`01_exploration.md`** — restatement + multi-approach + primary selection for G1-G6.
4. **`SF_layer_classification.md`** — G1: 77 Cat A × Three-Layer table + axiom-dependency summary.
5. **`SF_function_taxonomy.md`** — G2: 7 classes + 1 new candidate (Class N) × 10 phenomena matrix + morphological transition graph.
6. **`MF_multi_quantization.md`** — G3: basin stratification + Landau $F(K)$ + Formation Quantization Uniqueness (Thm 3.2) + naturality audit.
7. **`T_time_evolution.md`** — G4: 4 hypotheses (H-T1 to H-T4) scoping.
8. **`T_thermal_softmax.md`** — G5: 4 hypotheses (H-Th1 to H-Th4) + P-F framework scoping.
9. **`A_application_scoping.md`** — G6: 4 experiment designs (EX-Seg-1/2, EX-SBM-1/2) + contrastive positioning.
10. **`03_integration_and_new_open.md`** — this file.
11. **`99_summary.md`** — (to be written next).

---

## §2. Canonical integration proposals

Note: **canonical §13.x references use v1.2 (2026-04-12) numbering**. All modifications below are **proposals** for Stage 3/Stage 6 merge; this session does NOT edit canonical directly.

### 2.1 §2 (Foundational Orientation) — new lens

**Add subsection 2.4 (proposed)**:
> **Three-Layer Hierarchy** (F1-SSU-v5, `step_cohesion.md` §3). SCC theory decomposes observationally into Layer 1 (topological $K$, basin structure), Layer 2 (geometric $r_0, \xi_0, d_{\min}, \mu$), Layer 3 (continuous field $u$). Each layer has its own primitive quantities and its own proof techniques; bridges across layers are claim-specific.

**Rationale**: Provides organizational framework for §13's 40+ theorems that isn't currently present. Layer classification (this session's G1 deliverable) demonstrates feasibility.

### 2.2 §11 (Fixed Commitments) — new commitments

**Add CN15 (proposed)**: Static/Dynamic Separation Principle (R22 §17.6).
> "Static invariants of the energy functional $\mathcal{E}$ (Hessian eigenvalues, Morse indices, isoperimetric bounds, algebraic symmetries) do not automatically transfer to dynamic observables (gradient-flow endpoint, $\widehat K$, metastable count). Static → dynamic transfer requires separate justification via protocol specification."

**Add CN16 (proposed)**: Protocol-Parameterized Observable (S3 from `step_cohesion.md` §10.1).
> "Dynamic observables $O(\beta, c, G, \pi)$ are functions of 4 arguments including protocol $\pi$. A statement 'K̂ = f(β, c, G)' without $\pi$ is ill-defined."

**Add CN17 (proposed)**: Formation Quantization (F1-SSU-v5 §1, this session §MF §3.6).
> "Every well-separated local minimizer $u^*$ admits unique step decomposition $u^* = \sum_{k=1}^K \phi_k^* + r$ with $K \in \mathbb{Z}_{\geq 0}$ topological invariant within basin."

### 2.3 §11.2 (Open Design Choices) — resolutions

**Item 4 (Dynamic update laws) and Item 7 (Self-referential transport)**: partially resolved by H-Th1 Langevin (this session §T_thermal §2) IF P-F framework committed. Propose:
> "Thermal extension: Langevin SDE $du = -\Pi_{\Sigma_m}\nabla\mathcal{E}(u)\,dt + \sqrt{2T}\Pi_{\Sigma_m}\,dW_t$ with reflected BM boundary treatment (NQ-67). Reduces to T14 gradient flow at $T=0$."

### 2.4 §12 (Open Problems) — status updates

**F-1 (OP-0001)**: This session does **not** resolve but **expands the dissolution mechanism** via §MF_multi §3.6 (Formation Quantization Uniqueness). F-1's "K=2 vacuity without external constraint" is **replaced** by F1-SSU-v5 framework where K is topological invariant within basin, not requiring external mass constraint.

**M-1 (OP-0002)**: §T_time §2.7 (well-separated zero-T freezing) + §T_thermal H-Th4 (Kramers merger $\sim e^{A\beta^{0.89}/T}$) quantify M-1 dissolution's "two-timescale" claim.

**MO-1 (OP-0003)**: §MF_multi §4 (moduli $\mathcal{M}_K$) provides alternative to $\Sigma^K_M$; Morse theory on $\Sigma_m$ (not corners-manifold) applies via Prop 1.1 / Thm 3.1. MO-1 framework-level dissolved; residual in NQ-57 basin boundary smoothness.

**OP-0004 (Type A/B)**: unchanged — still retracted.

**OP-0005 (K selection)**: Partially addressed by C-X1V5 (Protocol Selection) but not fully resolved — **K selection has NO thermodynamic mechanism** (from §MF §3.4 Landau F(K) monotonicity). K is dynamically selected via protocol, not landscape. This is a **negative result**: OP-0005 may not have a Yes answer.

**OP-0006, 0010, 0011, 0012, 0013**: unchanged.

**OP-0020, 0021, 0022**: Related to this session's G4/G5 scoping but not resolved.

### 2.5 §13 (Proved Results Registry) — additions

**Cat A new proposals** (from this session + R22 preserved):

1. **Formation Quantization Uniqueness (Thm 3.2, this session §MF §3.6)**: Well-separated $u^*$ admits unique step decomposition. Cat A structural.
2. **Three-Layer Hierarchy organizational**: Cat A organizational (confirmed by classification table G1).
3. **Static/Dynamic Separation Principle**: Cat A empirical (4 falsifications confirm). Should appear as §2 commitment (CN15) AND as §13 theorem.
4. **Protocol Selection (C-X1V5)**: Cat A empirical, R22.
5. **E3 Cubic Mechanism (C-X3)**: Cat A, R22.
6. **D1 α-Absolute Threshold (C-X2)**: Cat A empirical, R22.

**Cat B demotions to formalize** (from R21-R22):
- Round 9 §11 Supra-Lattice Theorem: Cat A → Cat B regime-restricted.

**Retractions to formalize**:
- Conjecture 2.1 (v1-v5): full retraction.
- Conjecture 2.1-Bott: full retraction.
- Round 6 §2.3e dynamic extension: partial (dynamic retracted, static preserved).

### 2.6 §14 (Commitment Notes) — Additions/modifications

Above proposals CN15-CN17. Plus:

**CN6 modification**: Currently says "K is kinetically determined." Refine to:
> "K is determined by **protocol-driven basin selection**, not by energy minimization. Landscape global min is K=1 (T-Merge (b) Cat A) but observed $\widehat K$ is protocol-dependent and typically $\geq 1$. Finite-time dynamics fixes an **apparent K-sector** that deviates from global min."

**CN14 modification**: Currently "closure expands metastability." Add:
> "Quantitative: closure raises merger barrier from $\propto \beta^{1/2}$ (Allen-Cahn) to empirically $\propto \beta^{0.89}$ (exp38 fit; Cat B), extending coarsening timescale exponentially in $\beta/T$."

---

## §3. Impact on existing open problems

### 3.1 Summary table

| Problem | Pre-session status | Session impact | Post-session status |
|---|---|---|---|
| **F-1** (K=2 vacuity) | OP-0001 (canonical); R16 dissolved | §MF Formation Quantization provides basin-level structure | Dissolution **framework-level complete** (still NQ-46 protocol dependence open) |
| **M-1** (K=1 preferred) | OP-0002; R16 dissolved via 2-timescale | §T_time + §T_thermal quantify timescales | Dissolution **quantitative** (exponent 0.89 Cat B canonical) |
| **MO-1** (Morse inapplicable) | OP-0003; R16 dissolved via $\Sigma_m$ not $\Sigma^K_M$ | §MF_multi moduli $\mathcal{M}_K$ on $\Sigma_m$ extends | Dissolution **extended to K≥2** |
| **OP-0004** (Type A/B) | Retracted (exp65) | No change | Retracted |
| **OP-0005** (K selection) | Open | §MF §3.4 + §MF §6 reframes as "no thermodynamic mechanism; protocol-dynamic only" | **Reframed**, not resolved; now in CN15 / CN16 language |
| **OP-0006** (Boundary precision) | Tentative D-0004 | No change | Tentative |
| **OP-0010** (Bind τ) | Partial (τ=1/2) | No change | Partial |
| **OP-0011** (Transport unique) | Under investigation | No change | Under investigation |
| **OP-0013** (Closure conv rate) | Under investigation | No change | Under investigation |
| **OP-0021** (Stochastic) | Under investigation | §T_thermal H-Th1 framework proposed | **Framework proposed** (needs P-F commit) |
| **OP-0022** (Continuous limit) | Not addressed | §T_time §6.2 continuum limit sketched | Still open; direction clarified |
| **N-1** (Soft-Hard Switching) | R18 reframing | Three-Layer classification (G1) clarifies static/dynamic split | **Structurally addressed**: N-1 is about K integer/continuous toggle; Layer 1 K is **integer always**, no toggle |
| **P-F** (Thermal framework) | Open | §T_thermal §6 scoping | **Scoped**; not committed |
| **P-A..P-H** (from R22) | Various | Carry-forward by layer | Tracked in §5 |

### 3.2 OP-0001 (F-1) detailed status update

Pre-session: "K=2 vacuity without external per-formation mass constraint."

Session contribution (§MF §3.6 Thm 3.2):
- Well-separated K-formation minimizer $u^* \in \mathcal{B}_K \subset \Sigma_m$ (single simplex, no product $\Sigma^K_M$).
- $K(u^*) \in \mathbb{Z}_+$ topological invariant (Formation Quantization).
- No external mass constraint needed; $\sum_k |A_k^*| = m$ is **internal consequence** of single $\Sigma_m$ constraint.

**New residual**: NQ-46 protocol-selection rules (which basins do various protocols land in?). Not silent-resolved. Explicitly carried.

---

## §4. Silent-resolution audit

### 4.1 Checked problems (Hard Constraint #2)

- **F-1**: ✅ Addressed via Formation Quantization (framework-level); residuals (protocol dependence) explicit.
- **M-1**: ✅ Quantitative timescale (§T_thermal §5.3).
- **MO-1**: ✅ $\mathcal{M}_K$ moduli addresses directly.
- **OP-0001..0007**: ✅ Impact table §3.1.
- **OP-0010..0022**: ✅ Impact table.
- **N-1** (Soft-Hard Switching from `open_problems_reframing_2026-04-19.md`): Three-Layer clarifies. K at Layer 1 is **always integer** (CN17 proposed); no "soft/hard toggle" within single layer. Toggle occurs at **protocol** level (Layer 1 ↔ Layer 2 bridge). Silent-resolution check: addressed structurally, but "does integer-K toggle to continuous K in any regime" remains conceptually open — this session does not silent-claim otherwise.
- **P-A..P-H** (physicality properties): tracked by layer. Not silent-resolved.

### 4.2 Status of silent resolutions

**No silent resolutions detected.** Each claim's impact on existing OPs is explicit in §3.

**Partial resolutions (to be distinguished from silent)**:
- F-1, M-1, MO-1: dissolution expanded but not "closed". Residuals explicit.
- OP-0005: reframed (K is protocol-dynamic, no thermodynamic mechanism). This is arguably a **negative resolution** (says "no" to the question), which should be elevated explicitly.

**Danger zone**: In §MF §3.4, "$F(K)$ has no non-trivial K > 1 minimum, predicting K=1 global" could be read as resolving M-1 trivially (K=1 is always preferred). **But** this reinforces M-1 rather than closes it; observed $\widehat K > 1$ is NOT from thermodynamic preference but from kinetic / protocol. Explicitly **not** silent-resolving M-1.

---

## §5. New open questions consolidated

Accumulated from all deliverables. Numbered continuously from NQ-51 (previous session stopped at NQ-50; R22 extended to ~NQ-55, this session adds NQ-56 onward).

### 5.1 G1 layer classification

- **NQ-51**: 3-layer vs 4-layer (adding Bridge Layer) decision. 27% "mixed" is high (§SF_layer §10).

### 5.2 G2 function taxonomy

- **NQ-52**: Class N (spectral Gaussian) parameters — $\bar K(\beta, G)$ and $\sigma_K^2(\beta, G)$의 closed form.
- **NQ-53**: Class D in SCC without P-F — Kramers rate의 엄밀한 justification가 thermal framework P-F를 요구.
- **NQ-54**: Class R의 graph-class universality — Prop 1.3b(d)은 D_4에서 explicit, general graph에서 Class R 형태 유지?
- **NQ-55**: Regime-dependent class transition points의 explicit formulas.

### 5.3 G3 multi-formation

- **NQ-56**: $\mathcal{B}_K$ connectedness (C1-2 Claim §MF §2.2). Path-connected in $\Sigma_m$?
- **NQ-57**: Basin boundary structure $\partial\mathcal{B}_K$ codim-1 smooth?
- **NQ-58**: Landau $F(K)$ empirical fit experiment.
- **NQ-59**: Multi-K with $K \geq 3$ saddle count (extends Round 10 Tree).
- **NQ-60**: Triple-body coupling beyond well-separated.
- **NQ-61**: Protocol-independent invariants of landscape.

### 5.4 G4 time evolution

- **NQ-62**: $t_{\mathrm{coarsen}}$ at zero T: finite or infinite?
- **NQ-63**: Nonuniform coarsening rate across K-sectors.
- **NQ-64**: Protocol changes mid-flow (warm-start) — K non-monotonic?
- **NQ-65**: Continuous limit existence (related to OP-0022).
- **NQ-66**: Noise-assisted nucleation rate scaling with noise amplitude.

### 5.5 G5 thermal

- **NQ-67**: Langevin boundary treatment on $[0,1]^n \cap \Sigma_m$.
- **NQ-68**: Basin volume $V_K(T)$ for SCC — definition + computability.
- **NQ-69**: $T_{\mathrm{eff}}$ from protocol noise — quantitative relation.
- **NQ-70**: Kramers prefactor $\tau_0$ for SCC.
- **NQ-71**: Class N parameter laws (generalize V7 P3 single data point).

### 5.6 G6 application

- **NQ-72**: Data-term augmentation without breaking CN5.
- **NQ-73**: Graph construction from image (k-NN? ε-ball? superpixel?).
- **NQ-74**: Ensemble-averaged metrics for protocol-dependent results.
- **NQ-75**: Scalability to large graphs.

### 5.7 Total new NQ this session: 25 (NQ-51 through NQ-75)

Combined with R22's NQ-50, cumulative: NQ-1..NQ-75. Stage 3/Stage 6 merge will need to triage which become canonical Open Problems.

---

## §6. Retraction / clarification inventory (accumulated)

Following R22 §17.15 + this session's additions:

| # | Target | Action | Origin |
|---|---|---|---|
| R1 | `working/MF/from_single.md` §2 Conjecture 2.1 (v1-v5) | **Full retraction** | R17/R19/R20/V7 P1 (R22) |
| R2 | `working/SF/mode_count.md` §2.3e | **Partial retraction** (dynamic retracted, static preserved) | R19 + R22 §18.6 |
| R3 | `working/SF/symmetry_moduli.md` §3.7.5 Conj 2.1-Bott | **Full retraction** | R17/R19 (R22) |
| R4 | `working/SF/profile_deviation.md` §11 Round 9 Cat A | **Cat A → Cat B demotion** | R21 |
| C1 | `canonical_sub.md` line 145 "exp_profile_fit not executed" | **Correction** | R22 §15.2 |
| Cl1 | `working/SF/cardinality_open.md` §4.2 | **Clarification** (static vs dynamic) | R22 |
| Cl2 | `working/SF/profile_deviation.md` §10.5 "25% shape modulation" | **Nuance** — R21 shows Regime A에서 400%+ | R21 |
| **A1 (this session)** | `canonical.md` §13 Cat A registry | **Additions** (FQ Uniqueness, Three-Layer, Static/Dynamic, Protocol Selection, E3 Cubic, D1 α) | Today §MF, §SF_layer |
| **A2 (this session)** | `canonical.md` §11 CN | **Add CN15, CN16, CN17** | Today §2.2 above |
| **A3 (this session)** | `canonical.md` §11.2 Open Design Item 4/7 | **Partially resolve** via H-Th1 Langevin | Today §T_thermal |
| **A4 (this session)** | `canonical.md` §12 "Multi-formation is kinetic" paragraph | **Refine** with Formation Quantization + Static/Dynamic Separation | Today §MF §3 |

---

## §7. Prompt template improvement suggestions

### 7.1 Template assumption violations today

The prompt template (`THEORY/logs/daily/MAIN_PROMPT.md`, referenced by this session's initial instructions) assumed **"단일 target open problem"** but plan.md had 6 goals. Required on-the-fly reconciliation (01_exploration.md §0).

**Suggestion (for future prompt template v2)**:
- Add explicit branch: "If plan.md has multi-goal structure (>1 deliverable), use extended file naming: `01_exploration.md` covers all goals' exploration; per-goal body files `<domain>_<goal>.md` (e.g., `SF_layer.md`, `MF_multi.md`); standard `03_integration_and_new_open.md` + `99_summary.md` still apply."
- This session effectively did this. Template should document it.

### 7.2 Directory write restriction conflict

Template §2 says "working/ 과 canonical/ 에는 직접 쓰지 않습니다" but plan.md §2 requested new working/ files. Resolution: **file names mirror promotion target, stored in logs/daily/**.

**Suggestion**: Template should explicitly note "plan.md may request working/ file creation; interpret as 'produce content in logs/daily/ named to mirror target, for user-promotion'."

### 7.3 "77 Cat A" counting mismatch

Plan.md said 77 (72 preserved + 5 new). Actual counting in canonical §13 = 35; R1-R22 count 84 new (many bundled). This session treated as ~76 distinct logical statements.

**Suggestion**: Future plan.md should specify **counting convention** explicitly when claiming specific numbers. "77" was ambiguous.

### 7.4 Silent-resolution check discipline

This session actively checked §4 silent-resolution. Template §8 Hard Constraint #2 is strong and worked. No change needed.

### 7.5 Layer organization scaling

Three-Layer Hierarchy was proposed mid-2026-04 and already produces 27% "mixed" category. 4-layer or continuous-layer refinement may be needed (NQ-51).

**Suggestion for future prompts**: If "Mixed" > 25% after classification, automatically trigger framework-refinement sub-task.

---

## §8. Integration verdict

**This session's contribution to canonical framework (Stage 2 Axiom Audit)**:

1. **Layer classification operational** — 77 claims now have assignable layer; framework tested.
2. **Function taxonomy** — 7 classes + 1 new (Class N); V7 P1 refutation of Class S formalized.
3. **Formation Quantization extended** — Well-separated K≥2 well-posed; uniqueness proof (Cat A structural).
4. **Time + thermal scoping** — 8 hypotheses at Cat B-C level; readiness for Stage 3 axiom commits.
5. **Applications contrastive framing** — 4 experiments ready for execution.

**Quality**:
- No silent resolutions.
- No canonical direct edits.
- No Research OS structure.
- All 4-term energy, closure non-idempotence, primitive u-field respected.
- Protocol dependence and static/dynamic separation maintained throughout.

**Limits**:
- `theorem_status.md` and `open_problems.md` in `THEORY/canonical/` are **stale** (as of 2026-04-12) relative to session logs. This session did **not** update canonical files; user's Stage 6 weekly merge needed.
- NQ count (75 total cumulative) is high; triage needed for Stage 3/6.

---

## §9. Next session recommendations

### 9.1 P0 candidates for 2026-04-24

Choose one:

- **(N1) Canonical merge rehearsal**: Apply §2, §6 proposals to canonical draft; verify self-consistency. High-value but user-decision heavy.
- **(N2) Numerical validation**: Execute EX-SBM-1 (simpler, controlled). Validates Formation Quantization dynamical claim on SBM.
- **(N3) Class N parameter study**: Run V7-like experiments across $(\beta, c, G)$ grid to fit $\bar K, \sigma_K$ empirical laws (NQ-71).
- **(N4) $F(K)$ Landau empirical fit**: Measure energy across K-sectors; compare to $K \cdot F_{\mathrm{single}} + \binom{K}{2}F_{\mathrm{pair}}$ (NQ-58).
- **(N5) Stage 2 Axiom Audit finalization**: With layer-classification done, audit each axiom's role per layer.

**Recommended**: **(N5) Stage 2 Axiom Audit** — most aligned with plan.md's Stage 2 trajectory and leverages today's layer framework.

### 9.2 P1 candidates

- Single-formation NQ-43 NQ-44 (R21 profile fit bound expansion).
- Multi-formation NQ-56 basin connectedness (theoretical follow-up).
- Applications **execution** of EX-SBM-1.

---

## §10. File status

- **Primary deliverable**: Integration proposals for canonical §2, §11 (3 new CNs), §12, §13, §14; silent-resolution audit cleared; 25 new NQ consolidated; prompt template improvement suggestions.
- **No canonical direct edits**.
- **No silent resolutions**.

**End of 03_integration_and_new_open.md.**
