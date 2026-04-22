# 03 — Integration and New Open Questions

**Session:** 2026-04-22 (SF-S1)
**Target (from plan.md):** Integrate Axis A + Axis B outputs with existing canonical; collect new open questions; document canonical merge proposals.
**This file covers:** §1 Integration with existing canonical. §2 New open questions (NQ-32 re-registered + NQ-33/34/35). §3 Canonical merge proposals (consolidated). §4 Effect on existing open problems (F-1/M-1/MO-1/OP-0004-0013/P-A-H). §5 Prompt improvement suggestions.
**Depends on reading:** `01_exploration.md`, `02_development.md`, all `working/SF/*.md`, `working/MF/from_single.md`, `working/E/{F1,M1,MO1}_dissolution.md` §Round 18 sections, `working/integer_K_dependency_map.md` rewrite, `errata_batch.md`.

---

## §1. Integration with existing canonical

### 1.1 Preserved Cat A theorems

Cat A single-formation theorems **survive unchanged** after Axis A/B reframing:

| Theorem | Session usage | Status |
|---|---|---|
| T1 (Existence) | Reused in `cardinality_open.md` §1 | Preserved |
| T8-Core (Phase Transition) | Corollary of Prop 1.3a at $k=2$ | Preserved; generalized |
| T11 (Γ-convergence Modica-Mortola) | Reused in Cor 2.2 qualitative + quantitative | Preserved |
| T14 (Gradient flow convergence, Łojasiewicz) | Two-timescale picture metastable absorption | Preserved |
| T20 (Axiom consistency, a_cl < 4) | Prop 1.3b (c) closure block | Preserved |
| T-Merge (b) (Isoperimetric energy ordering) | M-1 dissolution §8.1, MF §3.4 long-time K=1 | Preserved; re-cast as long-time limit |
| T-Birth-Parametric (D4 supercritical) | Cor 2.3.a of Prop 1.3a (pitchfork at k=2) | Preserved; Prop 1.3a generalizes |
| T3/T6-Stability (Closure Gram PSD) | Prop 1.3b (c) via Gram reuse | Preserved |
| T-A2 (Closure monotonicity) | Indirect (closure fixed point analysis) | Preserved |
| Coupling Bound Lemma Item 5 | `02_development.md` §7 spacing derivation | Preserved; reinterpreted at single-formation |
| T-Uniform-Stab-T (Round 4, canonical_sub 2026-04-21) | Prop 1.3a thermal extension | Preserved; thermal analog |

**Key observation.** Integer-K retirements (`integer_K_dependency_map.md` §2, 8 theorems) do NOT touch these single-formation Cat A results. The derived view reads integer-K from single-formation invariants; it does not invalidate single-formation analysis.

### 1.2 Modified commitments (CN)

| CN | Original | Modification (proposed) |
|---|---|---|
| **CN5** | "Four-term independence is conceptual, not mathematical" | Augment: Prop 1.3b shows cl_sep and bd Hessians are additive at $u_{\mathrm{uniform}}$; conceptual independence confirmed at Hessian level |
| **CN6** | "$K$ is kinetically determined" | Quantitative addendum (P-2026-04-22-05): $\widehat{K}(t_{\mathrm{emerge}}) = 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$; $\widehat{K}(t_{\mathrm{coarsen}}) = 1$. |
| **CN8** | "Formations are metastable, not globally optimal" | Unchanged in statement; §8 two-timescale gives rigorous backing |
| **CN14** | "Closure expands multi-formation stability by ~30% $d_{\min}^\ast$ reduction" | **Direction correction** (P-2026-04-22-03): CN14's 30% reduction is now an effect on $\xi_0^{\mathrm{eff}}$, not on the raw $d_{\min}^\ast$ formula (which scaled wrongly). |

### 1.3 New commitments (proposed CN18)

**CN18 (proposed).** "Single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ pre-determine the multi-formation emergence structure $(\widehat{K}, m_k, d_{\min}^\ast)$ up to graph-topology-dependent $O(1)$ constants. Integer $K$ is a derivable statistic, not a primitive."

- $N_{\mathrm{unst}}$ is the unstable Morse index at $u_{\mathrm{uniform}}$ (Prop 1.3a for bd; Prop 1.3b (e) for full).
- $\xi_0 = \sqrt{\alpha/\beta}$ is the interface width.
- $\widehat{K} = 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(G)} + O(1)$ (Conjecture 2.1, `working/MF/from_single.md` §2).
- $m_k \approx m/\widehat{K}$ at emergence; $K^\ast = 1$ at coarsening.
- $d_{\min}^\ast \asymp \xi_0\cdot \log(1/\epsilon_0)$ (§4 of MF file).

**Status.** Proposed; canonical addition awaits Stage 2 axiom audit (per canonical_sub P-2026-04-22-04 recommendation).

### 1.4 Retirements (consolidated with 2026-04-21 P-2026-04-21-02)

Integrated list (this session E-5 applied → 8 retirements total):

**Cat A (5 retirements):** T-Merge (a), Topological Lock, Coupling Bound Lemma (Item 5 reused standalone but the K-field structural items retired), Proposition 1.2, Theorem 3.1(a,b,d).

**Cat B (3 retirements):** γ_eff ≈ 0.89, T-Beyond-Weyl, T-d_min-Formula (with direction correction).

**Retirement reason (updated):** integer-K is derivable from $(N_{\mathrm{unst}}, \xi_0)$; K-field architecture $\Sigma^K_M$ is optional representation, not primitive. See `working/integer_K_dependency_map.md` §1.

### 1.5 Canonical §5, §8, §11 structural updates

**§5 (Transition Diagnostics).** Insert "Single-Formation Geometry" subsection anchoring $\xi_0 = \sqrt{\alpha/\beta}$ as formal subject (P-2026-04-22-02). Include three-scales table (`interface_scale.md` §5).

**§8 (Energy Functional).** Cross-reference to Prop 1.3a/b explaining why T8-Core threshold is first-mode of a sequence.

**§11 (Multi-formation paradigm).** Add paragraph (P-2026-04-22-07): "The observed formation count $\widehat{K}$ at emergence timescale is determined by the single-formation Morse index via graph-class law; coarsening to $K=1$ follows isoperimetric ordering on exponential timescales at $T > 0$."

### 1.6 Canonical §13 new Cat A entries

Four new entries (P-2026-04-22-01):
- **Prop 1.3a** (Morse index at $u_{\mathrm{uniform}}$, pure bd).
- **Prop 1.3b** parts (a)-(c)+(e) (cl_sep structural decomposition).
- **Cor 2.2 qualitative** (interface concentration).
- **Cor 2.2 quantitative (tanh ansatz, 2D square grid)** — explicit constant $C = \pi\ln 9/2 \approx 3.449$.

---

## §2. New Open Questions

### 2.1 NQ-32 (re-registered, originally 2026-04-21) — SCC Profile Perturbation

**Statement.** The SCC full-energy K=1 minimizer interface profile deviates 16–60% from the pure tanh ansatz (Round 18 exp_alpha_scan_v3). What is the explicit profile shape $f_{\mathrm{SCC}}(s/\xi)$? Does Prop 1.3b's $H_{\mathrm{cl,sep}}$ eigenbasis parametrize the deviation?

**Sub-problems.**
- NQ-32.a: Does pure tanh fit SCC radial profile? (Test via G5 exp_profile_fit.py.)
- NQ-32.b: If not, which correction basis $g(r)$ best fits? (C2 candidate: sech² perturbation; C3: generalized exponent.)
- NQ-32.c: Extract effective $\xi_0^{\mathrm{fitted}}$, compare to $\sqrt{\alpha/\beta}$.
- NQ-32.d: Does $\delta_{\mathrm{SCC}} = \xi_0^{\mathrm{fitted}}/\xi_0^{\mathrm{theory}} - 1$ scale with $w_{\mathrm{cl}}, w_{\mathrm{sep}}$ linearly?

**Severity.** MEDIUM — direct numerical investigation required for Cor 2.2 Tier 3 (SCC minimizer) to reach Cat A. Affects Cor 2.2 quantitative's canonical qualifier.

**Carry.** post-Stage-1 (requires exp_profile_fit.py execution).

**Origin.** `logs/daily/2026-04-21/14_single_formation_audit.md` §9.5.

### 2.2 NQ-33 (new) — $d_{\mathrm{eff}}(G)$ Precise Definition

**Statement.** The "effective spectral dimension" in Conjecture 2.1 of `working/MF/from_single.md` §2 is specified loosely (2 for 2D grid, 0 for barbell/SBM). General-graph definition?

**Candidate definition.** $d_{\mathrm{eff}}(G) := \lim_{\lambda \to 0^+} \log N(\lambda) / \log \lambda$ where $N(\lambda) = \#\{\lambda_k(G) \leq \lambda\}$ is the eigenvalue counting function. On 2D lattice: $d_{\mathrm{eff}} = 2$ asymptotically. On expander: $d_{\mathrm{eff}} \to \infty$ (or $d_{\mathrm{eff}} = $ undefined since $\lambda_2$ is $O(1)$).

**Why critical.** Precise $d_{\mathrm{eff}}$ is needed for the $\widehat{K} = 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$ formula to extend beyond 2D grids.

**Severity.** MEDIUM — formula's scope depends on clarifying this definition.

**Carry.** Stage 2 Axiom Audit (definition candidate + robustness testing).

**Origin.** `working/MF/from_single.md` §9.

### 2.3 NQ-34 (new) — Coarsening Exponent with SCC Self-Referentiality

**Statement.** LSW coarsening exponent in 2D Allen-Cahn is $K(t) \sim t^{-1/2}$. With SCC closure raising barrier height to $O(\beta^{0.89})$ (CN14, exp38), is the coarsening exponent modified?

**Why critical.** Mixing CN14 (raised barrier) with LSW (standard coarsening) without verifying the interaction gives inconsistent predictions for $t_{\mathrm{coarsen}}$ in `working/MF/from_single.md` §5.3.

**Severity.** HIGH — affects $t_{\mathrm{coarsen}}$ estimates critical for M-1 dissolution §8.1 quantitative claim.

**Carry.** E-S3 (long Langevin runs required; several hours).

**Origin.** `working/MF/from_single.md` §9; `working/E/M1_dissolution.md` §8 (integrates with R-M1-G).

### 2.4 NQ-35 (new) — Saturating $\widehat{K}$ on Cluster-Graphs

**Statement.** On barbell and SBM graphs, $\widehat{K} = 2$ or $K_{\mathrm{block}}$ (saturating) rather than $\sqrt{N_{\mathrm{unst}}}$. Unified formula covering both lattice scaling and cluster saturation?

**Candidate unified law.**
$$\widehat{K}(G) = \min\!\big(K_{\mathrm{cluster}}(G),\; 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(G)}\big),$$
where $K_{\mathrm{cluster}}(G)$ is the graph's Cheeger-based cluster count (≤ 2 for barbell; ≤ K for K-block SBM).

**Why critical.** Without unification, Conjecture 2.1 of MF §2 fails to classify non-lattice graphs.

**Severity.** MEDIUM.

**Carry.** post-Stage-1.

**Origin.** `working/MF/from_single.md` §2.3 graph-class table.

---

## §3. Effect on existing open problems

### 3.1 F-1 (OP-0001 CRITICAL)

**Session effect.** Dissolved via derived view: K=2 emerges automatically when $N_{\mathrm{unst}} \geq 1$ (`working/E/F1_dissolution.md` §7 Round 18 post-audit). Integer-K "vacuity" framing is an artifact of choosing K-field architecture.

**Residual.** NQ-32 (SCC profile deviation) affects $N_{\mathrm{unst}}^{\mathrm{full}}$ precise count.

**Status update.** Reframed, not completely dissolved. Partial dissolution: "K=2 is not vacuous in derived view."

### 3.2 M-1 (OP-0002 CRITICAL)

**Session effect.** Dissolved via two-timescale picture: "K=1 always preferred" is a long-time statement; short-time emergence has $\widehat{K} \geq 2$ (`working/E/M1_dissolution.md` §8 Round 18 post-audit).

**Residual.** NQ-34 (coarsening exponent) affects $t_{\mathrm{coarsen}}$ quantitative; Kramers prefactor at Σ_m (R-M1-A) unchanged.

**Status update.** Reframed, not completely dissolved. Partial dissolution: "M-1 is two-timescale conflation."

### 3.3 MO-1 (OP-0003 CRITICAL)

**Session effect.** Dissolved via single-Σ_m analysis: $\Sigma^2_M$ is not needed; Prop 1.3a/b counts Morse index on single Σ_m directly (`working/E/MO1_dissolution.md` §9 Round 18 post-audit).

**Residual.** Morse inequality sharp form on Σ_m^ε \ V (cardinality_open.md §2); V transversality (generic Sard).

**Status update.** Reframed, substantially dissolved. MO-1's core claim ("smooth Morse inapplicable") is refuted at the single-field level.

### 3.4 OP-0004 (Type A/B classification) — unchanged (retracted earlier)

### 3.5 OP-0005 (K Selection Mechanism)

**Session effect.** Partial resolution: $\widehat{K}(N_{\mathrm{unst}})$ formula specifies how K is set kinetically. CN6 quantitative addendum (P-2026-04-22-05) makes this explicit.

**Residual.** Formula is conjectural; extensions to non-2D graphs needed (NQ-33, NQ-35).

**Status update.** Partial resolution; remains OPEN pending validation.

### 3.6 OP-0006 (Boundary Definition Precision) — untouched

### 3.7 OP-0010 (Bind Generalization) — untouched

### 3.8 OP-0011 (Transport Kernel Uniqueness) — untouched

### 3.9 OP-0012 (Persistence Composition) — untouched

### 3.10 OP-0013 (Closure Operator Convergence Rate) — untouched

### 3.11 P-A (Integer K) through P-H

These "P-X" problems originate from `open_problems_reframing_2026-04-19.md`. Session effects:

- **P-A (Integer K):** Dissolved — integer K is derivable from $(N_{\mathrm{unst}}, \xi_0)$, a derived statistic not a primitive.
- **P-D (Threshold choices):** Untouched this session.
- **P-F (Zero-T metastability gap):** Reinforced by §8 two-timescale picture — at $T=0$ the framework is complete (instant absorption into local min), at $T>0$ requires external kinetic framework.
- **P-G (Axiom switching):** Unchanged.
- **P-H (25+ parameters):** Unchanged; Prop 1.3b's $H_{\mathrm{cl,sep}}$ depends on many parameters but $\beta$-invariance isolates $\beta$.

---

## §4. Canonical merge proposals (consolidated)

From this session's `canonical_sub.md` 2026-04-22 entry:

| Proposal ID | Target | Action | Canonical lines |
|---|---|---|---|
| P-2026-04-22-01 | §13 Cat A | Add 4 entries | ~60 |
| P-2026-04-22-02 | §5 or §8 | New "Single-Formation Geometry" subsection | ~25 |
| P-2026-04-22-03 | §13 T-d_min-Formula | Direction correction (Cat B correction inline) | ~5 |
| P-2026-04-22-04 | §14 | New CN18 | ~10 |
| P-2026-04-22-05 | §14 CN6 | Quantitative addendum | ~8 |
| P-2026-04-22-06 | §13 | 8 retirements (E-5 consolidated) | ~30 annotation |
| P-2026-04-22-07 | §11 | Multi-formation paradigm paragraph | ~8 |

**Total 2026-04-22 canonical addition: ~146 lines.** Combined with 2026-04-21 pending (225 lines): ~370 lines for Stage 6 weekly merge.

**Recommendation.** Defer all to Stage 6 consolidated merge (consistent with canonical_sub principles + P-2026-04-21-02 deferral decision).

---

## §5. Prompt Improvement Suggestions

Per §14 of MAIN_PROMPT.md (meta section), I collect issues observed in this session:

### 5.1 Output scope vs plan.md tension

**Issue.** The prompt's §6 specifies "all output to daily/" but plan.md G1-G7 explicitly require writes to `working/SF/`, `working/MF/`, `working/E/`, `CODE/experiments/`, and `canonical/canonical_sub.md`. The former is the default, but plan.md legitimately overrides.

**Suggestion.** Update MAIN_PROMPT §6 to clarify: "Numbered daily files are mandatory; plan.md's G-deliverables may legitimately require writes to `working/` or `CODE/`. `canonical/canonical.md` remains read-only."

### 5.2 "Silent resolution" criterion for partial dissolution

**Issue.** Prompt §8 Hard Constraint 2 says "silent resolution 금지". Today's session partially dissolved F-1/M-1/MO-1 (reframed, some residuals). The prompt does not specify where the "partial dissolution" vs "silent resolution" line lies.

**Suggestion.** Clarify: "Partial dissolution is permitted when (a) the mechanism of dissolution is explicitly stated, (b) residuals are enumerated (R-F1-A, R-M1-A, etc.), (c) the status update in canonical_sub.md marks the problem as 'reframed, partially dissolved' — not 'closed'."

### 5.3 Multi-axis session protocol

**Issue.** plan.md's two-axis structure (Axis A + Axis B) was supported by the prompt's multi-approach requirement but required unusual interleaving of Approach selection (A1+A2 for Axis A, B1+B3 for Axis B). The prompt's "one primary approach" reading is ambiguous when a session has multiple sub-goals.

**Suggestion.** For multi-target sessions, the prompt could allow "primary approach per axis, with explicit selection rationale per axis". Observed as natural in this session.

### 5.4 File size / granularity

**Issue.** Today's `02_development.md` is ~9 substantive sections + 11 category self-assessment rows. Already near the "diminishing returns" termination criterion specified in §13. Could benefit from earlier guidance on target density.

**Suggestion.** Add to §6 output convention: "Primary deliverables should target 200-400 lines per file; beyond 500 lines, split (e.g., 02a, 02b)." This session's `02_development.md` is 370-ish lines — near the upper edge but coherent.

---

## §6. Cross-reference index

For future sessions looking back:

| Topic | Primary file | Secondary |
|---|---|---|
| Prop 1.3a, 1.3b | `working/SF/mode_count.md` | `02_development.md` §2, §3 |
| Cor 2.2 qual, quant | `working/SF/interface_scale.md` | `02_development.md` §4 |
| G-C cardinality | `working/SF/cardinality_open.md` | - |
| NQ-32 profile | `working/SF/profile_deviation.md`, `CODE/experiments/exp_profile_fit.py` | - |
| Multi-formation derivation | `working/MF/from_single.md` | `02_development.md` §5-§9 |
| F-1 derived-view dissolution | `working/E/F1_dissolution.md` §7 | - |
| M-1 two-timescale | `working/E/M1_dissolution.md` §8 | - |
| MO-1 single-Σ_m resolution | `working/E/MO1_dissolution.md` §9 | - |
| Integer-K retirement | `working/integer_K_dependency_map.md` §2 | `02_development.md` rationale via §9 |
| Errata application | `logs/daily/2026-04-22/errata_batch.md` | - |
| Canonical merge proposals | `canonical_sub.md` 2026-04-22 entry | - |

---

**End of 03_integration_and_new_open.md.**
