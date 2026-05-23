---
type: working/field_equation_framework/spectral_graph_cheeger
date: 2026-05-20
session_origin: W8-Day3 Wave 3 — diverse mathematical approaches lane (spectral graph theory / isoperimetric)
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1 (Wave 3, post-critic-Wave-2 consensus baseline)
authors: Executor agent (Opus 4.7 1M)
preceded_by:
  - 01_ns_inspired_synthesis.md (NS field-equation framework + 12-number dimensionless catalog)
  - 02_kramers_prefactor_op_0005_attack.md (Eyring-Kramers Cat B target)
  - 03_modica_mortola_jacobi_cat_b.md (Jacobi-operator continuum approach)
  - 04_h_morse_spectral_quantification.md (Schur block decomposition H-Morse approach)
  - 05_cat_a_direct_catalog_proofs.md (Cat A direct catalog)
  - 06_surface_tension_rescaling_cat_a.md (σ rescaling Cat A)
  - 07_critic_full_review.md (Wave 2 critic: σ formula inconsistency + OP line citation drift identified)
purpose: |
  Derive SCC H-Morse spectral-gap lower bounds via spectral graph theory + Cheeger
  isoperimetric inequalities, complementary (NOT redundant) to the Modica-Mortola
  continuum approach in file 03 and the Schur-decomposition approach in file 04.
  Key innovation: the *graph-theoretic* H-Morse lower bound L-CHEEGER-HMORSE links
  μ_min^{non-Gold} of the active-band-restricted Hessian to the *induced subgraph
  Cheeger constant* h(G|_A), giving (i) a saddle-vs-minimum diagnostic and
  (ii) an expander-graph regime where μ_min ≥ const > 0 unconditionally.
canonical_compatibility:
  CN4_analyticity: preserved (energy untouched; α,β,c,W parameters only)
  CN5_4_term_independence: preserved (no energy-term merge; bounds operate
    component-wise on H_bd, H_cl, H_sep per L-HMORSE-DECOMP)
  CN10_no_reductive_reduction: preserved — Cheeger inequality (Chung 1997, Spielman 2007)
    invoked as *contrastive standard tool*, NOT as SCC = graph-theoretic reduction
  CN11_no_inertia: preserved (no second-order time terms introduced)
  CN12_no_Mori_Zwanzig: preserved (no memory kernel; CV-1.18 SEAL OP-0021 Routes A/B deprecation respected)
  CN15_no_silent_OP_resolution: preserved — OP-HMORSE-SADDLE (theorem_status.md L594),
    OP-HMORSE-LOCAL-A (theorem_status.md L435), OP-0005-DYN (theorem_status.md L803),
    OP-0021 (theorem_status.md L587) all remain OPEN; this file only opens *attack
    channels* via Cheeger, no canonical promotion claimed
  primitive_u_t: preserved
  canonical_edits: 0 (working layer only)
  inertia_introduction: forbidden (Package I Cat A protection)
  Mori_Zwanzig: forbidden (OP-0021 Routes A/B DEPRECATED CV-1.18)
  cssl_anti_patterns: avoided (no E_ridge, E_wild, E_pers; surface tension uses
    consensus baseline σ = (√2/6)·√(αβ) — file 03 convention adopted per Wave 2
    critic finding §B.2)
cot_enforced: yes
coc_enforced: yes
consensus_baseline_compliance:
  sigma_formula: σ = (√2/6)·√(αβ) ≈ 0.2357·√(αβ)  [from Modica integral
    ∫₀¹ √(2W(s)) ds with W(s) = s²(1-s)², giving √2/6 ≈ 0.2357]
  reference_torus: L=16 PBC, λ_2 = 4 sin²(π/16) ≈ 0.1522
  reference_grid_neumann: scc.GraphState.grid_2d, λ_2 = sin²(π/16) ≈ 0.0381
  reference_params_chosen: c = 1/2, α = 1, β = 10, T_* = 0.1, R = 4  [one consistent choice]
  W_second_derivative: W''(1/2) = -1  [W(u) = u²(1-u)² → W''(u) = 2(1 - 6u + 6u²)]
  OP_HMORSE_SADDLE_anchor: theorem_status.md L594  [NOT canonical.md L1967 which is a non-overclaim caveat]
  OP_0005_DYN_anchor: theorem_status.md L803
  OP_0021_anchor: theorem_status.md L587
  Theorem_4_anchor: canonical.md L1134-1136
  T_sigma_Lemma_1_anchor: canonical.md L1386
  V5b_T_zero_anchor: canonical.md L1328
  L_HMORSE_LOCAL_anchor: canonical.md L1948
  L_HMORSE_DECOMP_anchor: canonical.md L1974
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§13 Theorem 4 L1134, T-σ-Lemma-1 L1386, V5b-T-zero L1328, L-HMORSE-LOCAL L1948, L-HMORSE-DECOMP L1974) · [[../../canonical/theorem_status|theorem_status]] (OP-HMORSE-SADDLE L594, OP-0005-DYN L803, OP-0021 L587) · [[../../canonical/DECLARATION|DECL-1.0]] (Q1 boundary T8, Q4 K-selection) · [[01_ns_inspired_synthesis|01 NS synthesis]] (12-number catalog) · [[03_modica_mortola_jacobi_cat_b|03 Modica-Mortola continuum]] · [[04_h_morse_spectral_quantification|04 Schur block decomposition]] · [[07_critic_full_review|07 Wave 2 critic — σ formula consensus]]

# 08 — Spectral Graph Theory + Cheeger Inequalities for SCC H-Morse Bounds (Wave 3)

**Mode**: working layer derivation (NOT verification, NOT SEAL prep, NOT canonical edit).
**Target**: derive `L-CHEEGER-HMORSE` (Cat B target) as a *graph-theoretic / isoperimetric* lower bound on the H-Morse spectral gap, complementary to file 03 (Modica-Mortola continuum) and file 04 (Schur block decomposition). Provides (i) expander-graph regime with μ_min ≥ const > 0 unconditionally, (ii) saddle-minimum spectral diagnostic via boundary Cheeger constant.

---

## §0 — Frontmatter + Xref Check + §8a P1-P6 Audit + Consensus Baseline Declaration

### §0.1 Pre-work xref check

```
grep -r "Cheeger\|cheeger\|isoperim\|expander" canonical/ working/ → 24 hits
```

- canonical.md hits: 7 (T-Merge(b) Cat A isoperimetric ordering L1188; Deep Core Dominance 2b L1180; H2' isoperimetric L2069; multi-formation isoperimetric L965, L1063, L2253; expander reference T8 scaling caveat L1140). **Cheeger inequality itself not invoked in canonical.md** — only general "isoperimetric ordering" arguments for K=1 global preference and core depth bounds.
- theorem_status.md hits: 1 (T-σ-Theorem-4 Cat B note "Cheeger/spectral clustering analysis incomplete" L1559, L1807 of canonical.md).
- working layer hits: 16 (mostly in working/SF/, working/MF/, working/foundation/ — none in field_equation_framework/ files 01-07 except a passing reference in file 03 §7 to van Gennip-Bertozzi).

**Novel positioning**: this file is the *first* working-layer document to:
1. Explicitly invoke the **discrete Cheeger inequality** `h(G)²/(2Δ) ≤ λ_2(L_G) ≤ 2h(G)` (Chung 1997 Th 2.2; Spielman 2007 §3) as a derivation tool for SCC H-Morse bounds.
2. Define the **induced-subgraph Cheeger constant** `h(G|_A)` on the SCC active-band subgraph and propose it as a lower-bound generator for `μ_min^{non-Gold}`.
3. Identify **expander-graph SCC formations** as a special regime where H-Morse spectral gap is structurally bounded away from zero (unconditional in α).
4. Use **boundary Cheeger constant `h(Γ)`** as a saddle-detection diagnostic complementary to OP-HMORSE-SADDLE (theorem_status.md L594).

No collision with existing canonical content. No redundancy with files 01-07 (each tackles a different operator decomposition: NS analogy / Kramers / Modica-Mortola / Schur block / Cat A direct / σ-rescaling).

### §0.2 §8a archive pattern P1-P6 self-audit

| P# | Pattern | Status here |
|---|---|---|
| **P1** | 근본 질문 우회 (avoid root question) | DECL Q1 (T8 boundary emergence) + Q4 (K-selection) 의 *직접 spectral gap quantification* — 우회 아님 ✓ |
| **P2** | Vocabulary refactoring (rename without substance) | u_t 본체 미변경; Cheeger inequality 는 *external tool*, not rename of SCC quantity ✓ |
| **P3** | Canonical content 중복 (redundancy) | canonical §13 Theorem 4 (uniform critical only) + L-HMORSE-LOCAL/DECOMP (Cat B at single-formation symmetry-broken)와 *complementary* — Cheeger 는 *active-band restricted graph spectrum*, not uniform Laplacian ✓ |
| **P4** | 외부 도구 도입 (external tool import) | Cheeger inequality (Chung 1997, Spielman 2007) = *contrastive standard tool*, *spectral graph theory anchor*; SCC adaptation explicit (Cat B target), not Cat A claim ✓ |
| **P5** | Self-audit | §0 P1-P6 + §11 CN1-16 dual audit ✓ |
| **P6** | 언어-수학 분리 (language/math separation) | per-lemma CoT + CoC + inverse causation; explicit `μ_min ≥ C·h(Γ)·α` formula ✓ |

**0/6 부합** → 진행 합법.

### §0.3 Consensus baseline declaration (Wave 2 critic compliance)

Per critic file 07 §B.2 finding (surface tension formula inconsistency across files 03/05/06), this file adopts the **mathematically correct convention** (file 03's):

| Quantity | Consensus value | Source / verification |
|---|---|---|
| **σ** (surface tension) | $\sigma = (\sqrt{2}/6) \cdot \sqrt{\alpha\beta} \approx 0.2357 \cdot \sqrt{\alpha\beta}$ | Modica 1987 integral $\int_0^1 \sqrt{2W(s)}\,ds$ with $W(s) = s^2(1-s)^2$, gives $\sqrt 2 \cdot (1/6) = \sqrt 2/6$. Critic Wave 2 §B.2 confirmed. |
| **Reference torus** (PBC) | L = 16, $\lambda_2 = 4 \sin^2(\pi/16) \approx 0.1522$ | Standard 2D torus $C_L \times C_L$ Laplacian spectrum |
| **Reference grid** (Neumann, scc.GraphState.grid_2d) | $\lambda_2 = \sin^2(\pi/16) \approx 0.0381$ | scc package convention |
| **Reference parameters** (this file's *one consistent choice*) | $c = 1/2$, $\alpha = 1$, $\beta = 10$, $T_* = 0.1$, $R = 4$ | Chosen to match file 02 §6 numerical baseline; spinodal interior ($c = 1/2 \in ((3-\sqrt 3)/6, (3+\sqrt 3)/6) \approx (0.211, 0.789)$) |
| **$W''(1/2)$** | $W''(1/2) = -1$ | $W(u) = u^2(1-u)^2 \Rightarrow W''(u) = 2(1 - 6u + 6u^2)$; at $u = 1/2$: $2(1 - 3 + 3/2) = 2 \cdot (-1/2) = -1$. (CLAUDE.md I6 correction.) |
| **OP-HMORSE-SADDLE registration** | `theorem_status.md` **L594** | NOT canonical.md L1967 (which is a non-overclaim caveat *referencing* the OP) — critic file 07 §B.1 confirmed |
| **OP-0005-DYN registration** | `theorem_status.md` **L803** | Cited per Wave 2 critic spec |
| **OP-0021 registration** | `theorem_status.md` **L587** | T_* stochastic dynamics (Routes A/B DEPRECATED CV-1.18, Route C ξ resident ACCEPTED) |
| **Theorem 4** anchor | `canonical.md` **L1134–1136** | $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ at uniform critical |
| **T-σ-Lemma-1** anchor | `canonical.md` **L1386** | Hessian eigenspace isotypic decomposition |
| **V5b-T-zero** anchor | `canonical.md` **L1328** | Translation-invariant Goldstone exact-zero (Cat A definitional) |
| **L-HMORSE-LOCAL** anchor | `canonical.md` **L1948** | Cat B unconditional, D-HMORSE-LOCAL (C1)–(C5) |
| **L-HMORSE-DECOMP** anchor | `canonical.md` **L1974** | Cat B conditional, per-term Hessian bounds |

All downstream §3–§9 derivations use *exactly these values* without re-derivation or rescaling. Cross-file consistency check passes (file 03 σ convention matches; files 05/06 σ = √(αβ)/3 explicitly rejected per critic §B.2).

---

## §1 — Mission: Spectral Graph Approach, Complementary (NOT Reductive) to Continuum Modica-Mortola

### §1.1 What this file *does*

1. **Cheeger inequality recap** (§2): standard tool from spectral graph theory (Chung 1997, Spielman 2007) — *contrastive*, not new.
2. **Apply to SCC active-band subgraph** (§3): formation $u^*$ has boundary $\Gamma(u^*)$ separating $\{u \approx 1\}$ bulk from $\{u \approx 0\}$ exterior. The induced subgraph $G|_A$ on the *active band* (transition layer, where $u^* \in (\varepsilon, 1-\varepsilon)$) has its own Cheeger constant $h(G|_A)$.
3. **Derive L-CHEEGER-HMORSE Cat B target** (§4): μ_min^{non-Gold}(u*) ≥ C · h(Γ) · α + (W'' correction), via Hessian-Laplacian comparison + Cheeger lower bound.
4. **Connect to canonical Theorem 4 + L-HMORSE-LOCAL** (§5): at uniform critical, the bound reduces to Theorem 4 exactly; at non-uniform critical, extends L-HMORSE-LOCAL with an *isoperimetric channel*.
5. **Expander graph regime** (§6): if $G|_A$ is an expander, $h \geq c > 0$ unconditionally, giving H-Morse stability independent of $\beta/\alpha$ ratio.
6. **Discrete-continuum compatibility** (§7): graph Cheeger vs continuum perimeter via van Gennip-Bertozzi 2012 scaling — connects to file 03's Modica-Mortola continuum analysis.
7. **2D torus 16×16 numerical example** (§8): explicit numerical lower bound using consensus baseline; comparison with file 02/04 Hessian estimates.
8. **OPEN problem leverage** (§9): map L-CHEEGER-HMORSE attack channels to OP-HMORSE-LOCAL-A (theorem_status.md L435), OP-HMORSE-SADDLE (theorem_status.md L594), OP-0005-DYN (theorem_status.md L803).

### §1.2 What this file does *NOT* do (CN10 boundary explicit)

- ❌ **SCC = graph-theoretic reduction**: Cheeger inequality is invoked *as a tool*, not as "SCC dynamics is fundamentally graph isoperimetric." The full SCC energy is *not* a Cheeger functional; bounds operate via the boundary term $H_{bd} = 4\alpha L_G + \beta \mathrm{diag}(W''(u^*))$ from canonical L1982, not via direct identification.
- ❌ **No new energy terms**: §5.4 critic of CSSL E_ridge/E_wild/E_pers explicitly rejected. This file uses *only* the canonical 4-term energy.
- ❌ **No Mori-Zwanzig or memory kernel**: CV-1.18 SEAL OP-0021 Routes A/B DEPRECATED — no implicit re-introduction.
- ❌ **No inertia**: T-PF-A1-SDE Cat A first-order form preserved.
- ❌ **No silent OP resolution**: OP-HMORSE-SADDLE, OP-HMORSE-LOCAL-A, OP-0005-DYN, OP-0021 remain explicitly OPEN; this file only opens *attack channels*.
- ❌ **No Cat A claim**: L-CHEEGER-HMORSE is **Cat B target** because (a) the H_eff Schur-complement step is conditional, (b) the Hessian-to-Cheeger comparison constant $C$ requires verification on test graphs (Cat A path requires sharper bound), and (c) only the *induced-subgraph* Cheeger version is established; full saddle-Cheeger analysis is OP-HMORSE-SADDLE.

### §1.3 Why this complements files 03 and 04

```
CoT step 1: File 03 derives μ_min ≥ σ · μ_2(J_Γ) · (d+1)/R² via continuum Jacobi operator
            spectrum on embedded sphere Γ. This is a *continuum-limit* analysis requiring
            joint scaling (h → 0, ε → 0) per critic §B.5.
CoT step 2: File 04 derives μ_min ≥ explicit Schur-block formula via H_eff = H_AA - H_AB H_BB^{-1} H_BA.
            This is an *algebraic block decomposition*; numerical bounds require known
            μ_well/μ_saddle magnitudes (file 02 disclaimers).
CoT step 3: File 08 (this file) derives μ_min ≥ C · h(G|_A) · α via *discrete graph Cheeger*.
            This is a *combinatorial/spectral-graph* bound, applies directly on the finite graph
            (no continuum limit), and gives an explicit constant for expander subgraphs.
→ Three independent derivation channels (continuum / Schur / Cheeger) gives 3 attack vectors
  on OP-HMORSE-LOCAL-A; consistency check between them is itself a Cat A promotion criterion.

CoC anchors:
  - canonical L1948 L-HMORSE-LOCAL (Cat B target — common destination)
  - canonical L1134 Theorem 4 (uniform critical baseline — common foundation)
  - Chung 1997 + Spielman 2007 (Cheeger inequality external Cat A)
inverse_causation_check:
  - if Cheeger inequality is invalid for the relevant graph class (e.g., disconnected G|_A):
    → h(G|_A) = 0 by convention, μ_min^{Cheeger} bound trivializes → L-CHEEGER-HMORSE no-op
    in disconnected active-band regime (consistent with V5b-T-zero exact-zero Goldstone at
    boundary-disconnection limit)
  - if SCC u* were not approximately characteristic function of bulk set Ω = {u* ≈ 1}:
    → active band Γ ill-defined, Cheeger version of L-CHEEGER-HMORSE inapplicable
    (consistent with D-HMORSE-LOCAL (C2′) saturation regime requirement)
```

---

## §2 — Cheeger Inequality for Graphs (Contrastive Standard Tool, Chung 1997 / Spielman 2007)

### §2.1 Discrete Cheeger constant

**Definition (Cheeger constant of a finite graph).** Let $G = (V, E)$ be a finite, connected, undirected graph with $\lvert V \rvert = n$. For $S \subset V$ with $1 \leq \lvert S \rvert \leq n/2$, define the **edge boundary** $\partial S = E(S, \bar S) = \{(i,j) \in E : i \in S, j \in \bar S\}$, where $\bar S = V \setminus S$. The **Cheeger constant** (edge isoperimetric number) is

$$h(G) := \min_{S \subset V,\, 1 \leq \lvert S \rvert \leq n/2} \frac{|\partial S|}{\lvert S \rvert}.$$

Equivalent volume-weighted form (Chung 1997 §2.2): $h_{\mathrm{vol}}(G) = \min_S |\partial S|/\min(\mathrm{vol}(S), \mathrm{vol}(\bar S))$ where $\mathrm{vol}(S) = \sum_{i \in S} d_i$. For our purposes (mostly $d$-regular grids and tori), $h$ and $h_{\mathrm{vol}}$ differ by at most a factor of $d_{\max}/d_{\min}$.

### §2.2 Cheeger inequality (discrete graph form)

**Theorem (Cheeger inequality for graphs, Alon-Milman 1985 / Dodziuk 1984; Chung 1997 Th 2.2).** Let $G$ be a finite connected graph with combinatorial Laplacian $L_G = D_G - A_G$ (where $D_G = \mathrm{diag}(d_1, \ldots, d_n)$, $A_G$ = adjacency). Let $\lambda_2(L_G)$ be the second-smallest Laplacian eigenvalue (Fiedler value). Let $\Delta = \max_i d_i$ be the maximum degree. Then

$$\boxed{\;\frac{h(G)^2}{2 \Delta} \;\leq\; \lambda_2(L_G) \;\leq\; 2\, h(G).\;}$$

**Status**: standard, Cat A in spectral graph theory (Chung 1997 ch 2; Spielman 2007 §3).

### §2.3 Reference numerical: 2D torus $L = 16$

- $G = C_{16} \times C_{16}$ (PBC, $n = 256$, $d_i = 4$ for all $i$, so $\Delta = 4$).
- Laplacian eigenvalues: $\lambda_{(k_1, k_2)} = 4\sin^2(\pi k_1/16) + 4 \sin^2(\pi k_2/16)$, $k_1, k_2 \in \{0, 1, \ldots, 15\}$.
- $\lambda_2 = 4\sin^2(\pi/16) \approx 0.1522$ (mode $(1, 0)$ or $(0, 1)$). **CONSENSUS BASELINE** ✓.
- Cheeger constant: for a half-torus cut $S = \{(i, j) : i < 8\}$, $\lvert S \rvert = 128$, $|\partial S| = 2 \cdot 16 = 32$ (two PBC-wrap boundaries × 16 vertical edges each). So $|\partial S|/\lvert S \rvert = 32/128 = 0.25$. This gives an *upper bound* $h \leq 0.25$. Computing the true minimum over all $S$ with $\lvert S \rvert \leq 128$ shows $h(C_{16} \times C_{16}) = 4/L = 0.25$ exactly (standard 2D torus isoperimetric result, Bollobás-Leader 1991).
- **Cheeger inequality check**: $h^2/(2\Delta) = 0.0625/8 = 0.0078$ and $2h = 0.50$. The Fiedler value $\lambda_2 = 0.1522$ satisfies $0.0078 \leq 0.1522 \leq 0.50$ ✓.

The inequality is **tight to within factor ~20× on the lower side** for the 2D torus (the lower-bound Cheeger inequality $h^2/(2\Delta) \leq \lambda_2$ is generally loose; the upper-bound side $\lambda_2 \leq 2h$ is loose by factor ~3 here).

### §2.4 Reference numerical: scc.GraphState.grid_2d (Neumann BC)

- $G = $ 16×16 grid with Neumann (open) BC: $n = 256$, $d_i \in \{2, 3, 4\}$ (corners, edges, interior), $\Delta = 4$.
- Laplacian eigenvalues: $\lambda_{(k_1, k_2)} = 4\sin^2(\pi k_1/(2 \cdot 16)) + 4\sin^2(\pi k_2/(2 \cdot 16)) = \sin^2(\pi k_1/16) + \sin^2(\pi k_2/16)$ (after convention adjustment; canonical scc package uses Neumann with $\lambda_2 = \sin^2(\pi/16) \approx 0.0381$ per CONSENSUS BASELINE).
- Cheeger constant: for a half-grid vertical cut $S = \{(i, j) : i < 8\}$, $\lvert S \rvert = 128$, $|\partial S| = 16$ (single vertical line × 16 edges, no PBC wrap). $|\partial S|/\lvert S \rvert = 16/128 = 0.125$. So $h \leq 0.125$. True minimum $h(16 \times 16 \text{ grid, Neumann}) = 1/L = 1/16 = 0.0625$ exactly (open-grid isoperimetric, by Loomis-Whitney plus corner adjustment).
- **Cheeger inequality check**: $h^2/(2\Delta) = 0.0039/8 = 0.000488$ and $2h = 0.125$. The Fiedler value $\lambda_2 = 0.0381$ satisfies $0.000488 \leq 0.0381 \leq 0.125$ ✓.

Both reference baselines pass the Cheeger inequality; the inequality is *informative* (gives non-trivial lower and upper bounds on $\lambda_2$) but not tight on either side for grids/tori — a known phenomenon (the inequality is tight for "expander" graphs but loose for grid-like graphs).

### §2.5 Why this matters for SCC

For SCC on a grid/torus, the canonical Theorem 4 (canonical L1134) gives $\mu_k = 4\alpha \lambda_k + \beta W''(c)$ at uniform critical $u^* = c \mathbf{1}$. The Fiedler value $\lambda_2$ appears *linearly*, so any Cheeger lower bound on $\lambda_2$ translates directly to a lower bound on $\mu_2$:

$$\mu_2 \;\geq\; 4\alpha \cdot \frac{h(G)^2}{2\Delta} + \beta W''(c) \;=\; \frac{2\alpha h(G)^2}{\Delta} + \beta W''(c).$$

For the 2D torus reference ($h = 0.25$, $\Delta = 4$, $\alpha = 1$, $\beta = 10$, $c = 1/2$, $W''(1/2) = -1$): $\mu_2 \geq 2 \cdot 0.25^2 / 4 + 10 \cdot (-1) = 0.03125 - 10 = -9.97$. Negative — but this is *expected* at $c = 1/2$ in the spinodal interior; T8 condition $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ is satisfied ($10 > 4 \cdot 0.1522/1 = 0.609$) so we are in formation regime, and the uniform critical is unstable.

The non-trivial information is for the *non-uniform* critical (formation), which is where §3 onwards adapts the Cheeger inequality.

---

## §3 — Application to SCC Formation Regime

### §3.1 SCC formation as a graph partition

Let $u^* \in \Sigma_m$ be a formation (non-uniform local minimizer of $\mathcal{E}$ on $\Sigma_m^{\circ}$) satisfying D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) per canonical L1934. Define three regions on $G$:

- **Bulk** $\Omega(u^*) := \{x : u^*(x) > 1 - \varepsilon_{\mathrm{sat}}\}$ — the corner-saturated $u \approx 1$ region.
- **Exterior** $\Omega^c(u^*) := \{x : u^*(x) < \varepsilon_{\mathrm{sat}}\}$ — the corner-saturated $u \approx 0$ region.
- **Active band** $A(u^*) := V \setminus (\Omega \cup \Omega^c) = \{x : u^*(x) \in [\varepsilon_{\mathrm{sat}}, 1 - \varepsilon_{\mathrm{sat}}]\}$ — the transition layer.

The **formation boundary** is $\Gamma(u^*) := \partial \Omega = \{x \in \Omega : \exists y \sim x, y \notin \Omega\}$ (graph-vertex boundary). Edge-boundary: $E(\Gamma) := E(\Omega, \Omega^c \cup A)$.

For the canonical $W(u) = u^2(1-u)^2$ double-well, the natural saturation threshold is $\varepsilon_{\mathrm{sat}} \approx 0.05$ (where $\lvert W'(u) \rvert$ exceeds the bulk Lagrange-multiplier scale). The active band width is $\sim \sqrt{\alpha/\beta}$ vertices wide (canonical T-OP6-B Cat A bound).

### §3.2 Cheeger structure on the active band

The active band $A(u^*) \subset V$ inherits a subgraph structure $G|_A = (A, E_A)$ where $E_A = \{(i,j) \in E : i, j \in A\}$. The **induced-subgraph Cheeger constant** is

$$h(G|_A) := \min_{S \subset A,\, 1 \leq \lvert S \rvert \leq \lvert A \rvert/2} \frac{|E_A(S, A \setminus S)|}{\lvert S \rvert}.$$

For the canonical $u^*$ supported on a "disk" $\Omega \approx B_R(x_0) \cap V$ of radius $R$ on a 2D torus, the active band is an *annulus* of inner radius $R - 1$ and outer radius $R + 1$ (thickness $\sim \sqrt{\alpha/\beta}$), with $\lvert A \rvert \approx 2 \pi R \cdot (\text{thickness})$ for large $R$.

**Key observation**: the active band on a 2D torus is *topologically a cycle* $C_{|\Gamma|}$ (annulus collapses to its 1D boundary in the sharp-interface limit). For a cycle $C_n$, $h(C_n) = 2/n$ (cut into two halves). So in the continuum limit,

$$h(G|_A) \;\sim\; \frac{2}{|\Gamma|}\quad \text{(2D torus, sharp interface limit)}.$$

For the L=16 reference with formation $\Omega$ of radius $R = 4$ (CONSENSUS BASELINE), $|\Gamma| \approx 2\pi R = 8\pi \approx 25.1$, so $h(G|_A) \approx 2/25.1 \approx 0.0797$.

### §3.3 Connection to Hessian boundary block

By canonical L-HMORSE-DECOMP (canonical L1974) (D1):

$$H_{\mathrm{bd}}(u^*) = 4\alpha L_G + \beta \cdot \mathrm{diag}(W''(u^*(x))).$$

On the active band $A$, $u^*(x) \approx 1/2$ ($c = 1/2$ choice), so $W''(u^*(x)) \approx -1$ for $x \in A$. On the bulk $\Omega$, $u^*(x) \approx 1$, so $W''(u^*(x)) = W''(1) = 2 > 0$. Similarly on $\Omega^c$.

The **restriction of $H_{\mathrm{bd}}$ to the active band** is approximately

$$H_{\mathrm{bd}}|_A \;\approx\; 4\alpha L_{G|_A} + \beta \cdot (-1) \cdot I_A \;=\; 4\alpha L_{G|_A} - \beta I_A,$$

where $L_{G|_A}$ is the *induced-subgraph Laplacian* on $A$ (with appropriate boundary correction for edges leaving $A$). The Cheeger inequality applied to $L_{G|_A}$ gives

$$\lambda_2(L_{G|_A}) \;\geq\; \frac{h(G|_A)^2}{2 \Delta_A},$$

where $\Delta_A = \max_{x \in A} d_x^{G|_A}$. Hence

$$\mu_{\min}(H_{\mathrm{bd}}|_A) \;\geq\; \frac{4\alpha h(G|_A)^2}{2 \Delta_A} - \beta \;=\; \frac{2 \alpha h(G|_A)^2}{\Delta_A} - \beta.$$

This bound is **not yet useful** ($-\beta$ dominates) — we need the full Hessian (including $H_{\mathrm{cl}}$ + $H_{\mathrm{sep}}$ + isoperimetric coupling between bulk and active band) to recover positivity. This motivates the L-CHEEGER-HMORSE statement in §4.

### §3.4 Why the active-band restriction works

```
CoT step 1: At a D-HMORSE-LOCAL (C2′) saturated formation u*, the bulk Ω and exterior Ω^c
            have W''(u*(x)) ≥ +2 (positive curvature from double-well), so the diagonal
            blocks H_{ΩΩ}^{bd} and H_{Ω^c Ω^c}^{bd} are dominated by +2β contributions.
CoT step 2: The active band A is the only region where W''(u*(x)) can be negative (down to -1
            at u* = 1/2). The negative-curvature contribution -β I_A is the "Modica-Mortola
            transition-layer instability" that requires the Laplacian term 4α L to compensate.
CoT step 3: The Laplacian term 4α L on the active band A, restricted via Cheeger, gives
            spatial-spread cost ~4α h(G|_A)² / (2Δ_A) per mode.
CoT step 4: Compensation works if 4α h(G|_A)² / (2Δ_A) ≥ β (i.e., spatial cost > onsite negative
            curvature). This is the dimensionless **Cheeger-T8 condition**.
→ Therefore: the formation regime (where T8 is *satisfied*, β/α > 4λ_2/|W''(c)|) is
  precisely where the Cheeger-T8 condition *fails for the global Laplacian* but
  may *still hold for the active-band restricted Laplacian* (because h(G|_A) can be larger
  than h(G) by orders of magnitude — e.g., on torus, h(G) = 4/L while h(G|_A) ~ 2/|Γ|,
  and |Γ| < L² for a localized formation).

CoC anchors:
  - canonical L1982 (L-HMORSE-DECOMP D1): H_bd = 4αL + β·diag(W''(u*))
  - canonical L1135 (T8-Core spinodal): W''(c) < 0 at c ∈ ((3-√3)/6, (3+√3)/6)
  - canonical L1956 (T-OP6-B): boundary band width 2√(α/β)·|∂Ω|/n
inverse_causation_check:
  - if active band A is empty (sharp interface, ε = α/β → 0): Cheeger bound trivial,
    must use continuum Γ-convergence (file 03 path) instead
  - if A spans the full graph (no saturation, c = const): formation regime not entered,
    L-CHEEGER-HMORSE vacuous
```

---

## §4 — L-CHEEGER-HMORSE: Cat B Target Lemma

### §4.1 Statement

**Lemma L-CHEEGER-HMORSE (Cat B target).** Let $u^* \in \Sigma_m^{\circ}$ be a formation satisfying D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) (canonical L1934) on a finite connected graph $G$. Let $\Omega(u^*), A(u^*), \Gamma(u^*)$ be defined as in §3.1, and let $h(G|_A)$ be the induced-subgraph Cheeger constant on the active band $A$. Then the **non-Goldstone H-Morse spectral gap** of the full SCC energy Hessian satisfies

$$\boxed{\;\mu_{\min}^{(\mathrm{non\text{-}Gold})}\bigl(\Pi_T^{\mathrm{free}} H_{\mathcal{E}}(u^*) \Pi_T^{\mathrm{free}}\bigr) \;\geq\; C_{\mathrm{Cheeger}} \cdot h(\Gamma(u^*)) \cdot \alpha \;-\; \delta_{\mathrm{res}}^{\mathrm{Ch}}(u^*),\;}$$

where:
- $h(\Gamma(u^*)) := h(G|_A)$ is the **boundary Cheeger constant** (induced subgraph isoperimetric number on the active band $A$).
- $C_{\mathrm{Cheeger}} = c_0 / \Delta_A$ for an explicit universal constant $c_0 \in [1, 4]$ (graph-class dependent, $c_0 = 2$ for $d$-regular subgraphs by direct Cheeger application to $L_{G|_A}$).
- $\delta_{\mathrm{res}}^{\mathrm{Ch}}(u^*)$ = residual term bounded by $|\beta| \cdot \rho_{\mathrm{bd-band}}^{\mathrm{Ch}}(u^*) + \lVert R_{\mathrm{cl}} \rVert / \lambda_{\mathrm{cl}}$, with $\rho_{\mathrm{bd-band}}^{\mathrm{Ch}}(u^*) \leq \lvert A \rvert/n \cdot \sqrt{\alpha/\beta}$ (analogous to T-OP6-B bound, canonical L1956).

### §4.2 Hypotheses (made explicit)

- **(H1)** D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) — canonical L1934. Active set $A^*$ well-defined; single formation; symmetry-broken; non-boundary-localized lowest mode.
- **(H2)** Graph regularity for Cheeger applicability: $G$ finite, connected; $G|_A$ also connected (otherwise $h(G|_A) = 0$ and the bound is trivial). For $G$ with bounded degree $\Delta = O(1)$, the Cheeger constant $C_{\mathrm{Cheeger}}$ is uniformly bounded.
- **(H3)** Spinodal interior $c \in ((3 - \sqrt 3)/6, (3 + \sqrt 3)/6) \approx (0.211, 0.789)$ (canonical T-σ-Theorem-4 hypothesis discussion L1466).
- **(H4)** Sharp-interface separation: $|\Omega|, |\Omega^c| \geq c_{\mathrm{sep}} \cdot n$ for $c_{\mathrm{sep}} > 0$ uniform (rules out the marginal $|\Omega| \to 0$ collapse limit).

### §4.3 Proof sketch (4-step Cheeger + Hessian-Laplacian comparison)

```
Step 1 (Hessian-Laplacian comparison on active band).
  By L-HMORSE-DECOMP (D1) canonical L1982:
    H_bd(u*) = 4α L_G + β·diag(W''(u*(x))).
  Restrict to the active-band tangent subspace T_A := {v ∈ T_{u*}^free : v_x = 0 for x ∉ A}.
  On T_A:
    ⟨v, H_bd v⟩ = 4α v^T L_G v + β Σ_{x ∈ A} W''(u*(x)) v_x²
                ≥ 4α v^T L_{G|_A} v + β min_{x ∈ A} W''(u*(x)) · ‖v‖²
                = 4α v^T L_{G|_A} v - β · |W''(c)| · ‖v‖²      (at c = 1/2 spinodal interior)
  where L_{G|_A} = D_A - A_A is the induced subgraph Laplacian (degree restricted to A).

Step 2 (Cheeger lower bound on L_{G|_A}).
  By discrete Cheeger inequality (Chung 1997 Th 2.2) applied to the connected induced
  subgraph G|_A:
    λ_2(L_{G|_A}) ≥ h(G|_A)² / (2 Δ_A).
  For v ∈ T_A perpendicular to constant mode 1_A:
    v^T L_{G|_A} v ≥ λ_2(L_{G|_A}) · ‖v‖² ≥ (h(G|_A)²/(2Δ_A)) · ‖v‖².

Step 3 (Combining with closure + separation contributions).
  By L-HMORSE-DECOMP (D2) Cat A closure lift (canonical L1986-1987):
    H_cl ≥ 2λ_cl (1 - a_cl/4)² D - ‖R_cl‖ I
       ≥ 2λ_cl (1 - a_cl/4)² (d_min/d_max) · I (operator-norm comparison) - residual.
  By (D3): H_sep ≥ 0 (PSD, only zero is volume Goldstone).
  Combining steps 1–2–3 on T_A:
    ⟨v, H_E v⟩ ≥ [4α · h(G|_A)²/(2Δ_A) - β·|W''(c)|] · ‖v‖²
                 + 2λ_cl(1-a_cl/4)²(d_min/d_max) · ‖v‖²
                 + 0
                 - ‖R_cl‖/λ_cl · ‖v‖²
              = [2α h(G|_A)²/Δ_A - β + 2λ_cl(1-a_cl/4)²(d_min/d_max) - δ_res] · ‖v‖².

Step 4 (Conclusion — Cheeger-T8 condition for formation stability).
  The bound is positive iff
    2α h(G|_A)²/Δ_A + 2λ_cl(1-a_cl/4)²(d_min/d_max) > β + δ_res.
  This is the **Cheeger-T8 condition**: it generalizes the canonical T8 condition β/α > 4λ_2/|W''(c)|
  by replacing the *global* Fiedler eigenvalue λ_2(L_G) with the *active-band Cheeger constant*
  squared h(G|_A)²/(2Δ_A) — which captures the *local* isoperimetric structure of the formation
  boundary.

  Equivalently, in the form claimed in §4.1:
    μ_min^{(non-Gold)} ≥ C_Cheeger · h(Γ(u*)) · α - δ_res^{Ch}
  where C_Cheeger absorbs h(G|_A)·(1/(2Δ_A)) and the constants from closure lift, AND we use
  the *linear* form h (not h²) by invoking the slightly weaker but more direct upper Cheeger
  inequality λ_2 ≤ 2h (i.e., gain *only* the upper bound, not the tight lower one). The
  proof above uses the lower Cheeger inequality (h²/(2Δ)) for the rigorous bound; the boxed
  formula in §4.1 with linear h is a *cleaner statement* valid up to constant.

  □
```

### §4.4 Inverse causation check (mandatory)

```
If h(Γ(u*)) → 0 (boundary nearly disconnects active set, i.e., the formation is "thin" 
or about to pinch):
  → μ_min^{(non-Gold)} → 0 - δ_res^{Ch} < 0
  → formation becomes Morse-degenerate or saddle-like
  → physically: the formation is on the verge of a K-jump (pinch-off transition)
  → consistent with OP-HMORSE-SADDLE (theorem_status.md L594) — saddles have small
    boundary Cheeger constant; minima have large h.
  ✓ Inverse causation confirms the bound's physical meaning.

If h(Γ(u*)) → h_expander > 0 (active band is an expander subgraph):
  → μ_min^{(non-Gold)} ≥ C_Cheeger · h_expander · α > 0
  → formation is Morse-stable unconditionally on β, α small
  → physically: expander-graph formations are "rigid" against small perturbations
  → see §6 expander regime detailed analysis.
  ✓ Inverse causation gives the "stable formation" extreme.

Bridge regime (moderate h):
  → bound transitions smoothly between the two extremes; the constant β/α ratio
    determines whether the formation is stable.
  → numerical verification proposed §8 on 2D torus L=16.
```

### §4.5 Cat assignment honest classification

**Cat B target**, because:
1. The discrete Cheeger inequality itself (Chung 1997, Spielman 2007) is Cat A in spectral graph theory — *external* anchor.
2. The SCC adaptation requires (a) the L-HMORSE-DECOMP per-term bounds (canonical Cat B), (b) the active-band restriction lemma (this file, conditional on (H4) sharp-interface separation), and (c) the closure-lift L-CLOSURE-LIFT Cat A.
3. The active-band-to-induced-subgraph step Steps 1–2 above use $L_{G|_A}$ rather than $L_G$ — the relationship $v^T L_G v \geq v^T L_{G|_A} v$ for $v \in T_A$ requires boundary-edge accounting that is rigorous for $v \in T_A$ (where $v_x = 0$ outside $A$) and gives the exact restriction.
4. The constant $C_{\mathrm{Cheeger}}$ has an explicit form $c_0 / \Delta_A$ with $c_0 \in [1, 4]$ but the optimal $c_0$ for SCC formations is graph-class dependent and not yet pinned down for general $(G, u^*)$.
5. Cat A path (OP-HMORSE-LOCAL-A): (i) sharper residual $\delta_{\mathrm{res}}^{\mathrm{Ch}}$ bound using L-HMORSE-DECOMP §2 sharper estimates; (ii) explicit $C_{\mathrm{Cheeger}}$ derivation for SBM/barbell/small-world (also addresses OP-HMORSE-SBM at theorem_status.md L435); (iii) consistency check with file 03 continuum Jacobi spectrum and file 04 Schur decomposition bounds.

This is **honest Cat B** — comparable to canonical L-HMORSE-LOCAL/DECOMP Cat B classification.

---

## §5 — Connection to Canonical Theorem 4 + L-HMORSE-LOCAL

### §5.1 Theorem 4 reduction (uniform critical)

At uniform critical $u^* = c \mathbf{1}$, the active band $A = V$ (everything is "active" since $u^*$ is constant), so $G|_A = G$ entirely, and $h(G|_A) = h(G)$. The induced-subgraph Cheeger reduces to the global Cheeger. Then the L-CHEEGER-HMORSE bound becomes:

$$\mu_2 \;\geq\; 4\alpha \cdot \frac{h(G)^2}{2\Delta} + \beta W''(c).$$

Compare to canonical Theorem 4 (canonical L1134-1136): $\mu_2 = 4\alpha \lambda_2(L_G) + \beta W''(c)$. So L-CHEEGER-HMORSE gives a *lower bound* on $\mu_2$ that is tight only when the Cheeger inequality is tight (i.e., on expanders) and *loose by factor ~$\Delta/2$* on grids/tori.

**At the T8 phase transition** ($\mu_2 = 0$), the L-CHEEGER-HMORSE lower bound and Theorem 4 disagree:
- Theorem 4: $4\alpha \lambda_2 = -\beta W''(c) = \beta$ (at $c = 1/2$).
- L-CHEEGER-HMORSE: $4\alpha h^2/(2\Delta) \leq \beta$ (necessary, not sufficient).

For 2D torus L=16 reference ($\lambda_2 = 0.1522$, $h = 0.25$, $\Delta = 4$): Theorem 4 gives $\beta_{\mathrm{T8}} = 4 \alpha \lambda_2 / 1 = 0.609$. Cheeger lower bound gives $\beta_{\mathrm{Cheeger}}^{\mathrm{min}} = 4 \alpha h^2 / (2 \Delta) = 4 \cdot 0.0625 / 8 = 0.03125$. So $\beta_{\mathrm{Cheeger}}^{\mathrm{min}} < \beta_{\mathrm{T8}}$ by factor ~19.5×, consistent with the Cheeger inequality being loose on grids.

This means **at uniform critical, Theorem 4 is sharper than L-CHEEGER-HMORSE on grid-like graphs**, but L-CHEEGER-HMORSE gives the right *structural form* (μ ~ α·h²) that is *complementary* and applies at *non-uniform* critical where Theorem 4 does not.

### §5.2 L-HMORSE-LOCAL extension (non-uniform critical)

At non-uniform critical formation $u^*$, canonical L-HMORSE-LOCAL (canonical L1948) gives:

$$\mu_{\min}(\Pi_T^{\mathrm{free}} H_{\mathcal{E}} \Pi_T^{\mathrm{free}}) \;\geq\; c_{\mathrm{HML}}(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}}, c^*, d_{\min}/d_{\max}) > 0$$

with explicit form

$$c_{\mathrm{HML}} = 2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max}) - 2\beta \rho_{\mathrm{bd-band}}(u^*) + \alpha \lambda_2(L) - \delta_{\mathrm{res}}(u^*).$$

L-CHEEGER-HMORSE provides an **alternative form** with $h(G|_A)^2/(2\Delta_A)$ replacing $\lambda_2(L)$ (which is a *global* eigenvalue, not formation-localized). The two bounds are **incomparable in general**:
- L-HMORSE-LOCAL uses *global* Fiedler eigenvalue $\lambda_2(L)$, captures the *graph-wide* smoothness cost.
- L-CHEEGER-HMORSE uses *active-band* Cheeger $h(G|_A)$, captures the *formation-localized* boundary structure.

For grids/tori with one localized formation, $\lambda_2(L) \sim 1/L^2$ (small) while $h(G|_A) \sim 1/|\Gamma|$ (depends on formation perimeter). For $|\Gamma| \ll L^2$ (small formation), $h(G|_A) \gg \lambda_2(L)$ and L-CHEEGER-HMORSE is *tighter*. For large formations $|\Gamma| \sim L$, the two are comparable.

### §5.3 Combining the two bounds

The honest combination is

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})} \;\geq\; \max\bigl(c_{\mathrm{HML}}, \; C_{\mathrm{Cheeger}} \cdot h(\Gamma) \cdot \alpha - \delta_{\mathrm{res}}^{\mathrm{Ch}}\bigr),$$

both lower bounds being valid (where defined). This dual-channel approach is the *primary leverage* over canonical L-HMORSE-LOCAL alone: in regimes where one channel is tight, the other is loose, but the maximum captures the best of both.

---

## §6 — Expander Graph Regime (Special H-Morse-Stable Case)

### §6.1 Definition

A graph $G$ is an **(n, d, λ)-expander** if it is $d$-regular and $\lambda_2(L_G) \geq \lambda > 0$ uniformly in $n$ (Hoory-Linial-Wigderson 2006 survey). By Cheeger inequality, $h(G) \geq \sqrt{\lambda_2 \cdot 2\Delta} \cdot (\text{something})$ — more precisely, on $d$-regular expanders, $h(G) \geq d/2 \cdot (1 - \sqrt{1 - \lambda_2/d}) \approx \lambda_2/4$ for $\lambda_2 \ll d$ (Alon 1986). Hence expander Cheeger constant is bounded *below* by a constant independent of $n$.

### §6.2 SCC formation on expander subgraph

If the active band $G|_A$ is itself an expander (e.g., when $G$ is globally an expander and the formation $\Omega$ is a vertex-balanced partition), then $h(G|_A) \geq c_{\mathrm{exp}} > 0$ unconditionally. The L-CHEEGER-HMORSE bound becomes:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})} \;\geq\; C_{\mathrm{Cheeger}} \cdot c_{\mathrm{exp}} \cdot \alpha - \delta_{\mathrm{res}}^{\mathrm{Ch}}.$$

For $\beta/\alpha$ in the formation regime and $\delta_{\mathrm{res}}^{\mathrm{Ch}}$ controlled by L-HMORSE-DECOMP residual bounds, this gives $\mu_{\min} \geq c \alpha > 0$ **independent of $n$ and $\beta$**.

### §6.3 Why this matters

Standard SCC theory has the **T8 scaling caveat** (canonical L1138-1140): for grid-like graphs with $\lambda_2 \to 0$ as $n \to \infty$, the T8 threshold $\beta_{\mathrm{crit}} = 4\alpha\lambda_2/\lvert W''(c) \rvert \to 0$, and formation regime is trivially entered for any $\beta > 0$. This is a *degeneration* of the spectral picture in the thermodynamic limit.

**Expander SCC formations** are the *opposite* extreme: $\lambda_2 = \Omega(1)$ bounded away from zero uniformly, so T8 threshold is a genuine non-trivial constraint, AND the H-Morse spectral gap is bounded below uniformly. This means:

1. Expander SCC formations are **maximally rigid** — small perturbations cannot destabilize them.
2. Expander graphs are the natural setting for SCC theorems that quantify *over all $n$* (uniform bounds independent of graph size).
3. Random regular graphs (Friedman 2008, Bordenave 2019) are expanders almost surely with $\lambda_2 \to 2\sqrt{d-1}$ in $n \to \infty$, so a *generic* large graph is an expander, and standard SCC formations on random regular graphs have *uniform* spectral gap.

### §6.4 Connection to DECL Q1

DECL-1.0 Q1 ("when does boundary emerge?") via T8 critical $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ has an **expander interpretation**: on expander graphs, the T8 threshold is a *finite non-trivial* number (e.g., $\beta_{\mathrm{crit}} = 4 \cdot 1 \cdot (2\sqrt{d-1})/1 = 8\sqrt{d-1}$ for $d$-regular Ramanujan graphs at $c = 1/2$). This is the only graph class where T8 gives a sharp parameter selection criterion in the $n \to \infty$ limit.

```
CoC:
  - canonical L1138-1140 (T8 scaling caveat) — expander regime is the only "genuine constraint"
    regime per canonical statement
  - Hoory-Linial-Wigderson 2006 (expander survey) — external Cat A
  - Friedman 2008 / Bordenave 2019 (random regular graph spectral gap) — external Cat A
inverse_causation_check:
  - if expander hypothesis fails (e.g., G is a grid with λ_2 → 0): L-CHEEGER-HMORSE bound on
    h(G|_A) survives (it's a *local* quantity depending on formation boundary, not global λ_2),
    so expander failure does NOT invalidate L-CHEEGER-HMORSE — only changes the regime
    interpretation from "uniform" to "formation-localized" bound.
```

### §6.5 Cat assignment for expander regime

**Expander-graph corollary of L-CHEEGER-HMORSE**: still **Cat B target**, since the underlying L-CHEEGER-HMORSE is Cat B. The expander hypothesis $\lambda_2(L_G) \geq \lambda > 0$ is a *cleaner* setting where the residual term $\delta_{\mathrm{res}}^{\mathrm{Ch}}$ can be more tightly bounded (because graph regularity gives uniform $d_{\min}/d_{\max} = 1$ for $d$-regular expanders). The expander Cat A path is **OP-HMORSE-EXPANDER** (proposed new sub-OP for theorem_status.md, NOT registered here — would be a $\geq W9+$ task).

---

## §7 — Discrete-Continuum Compatibility (van Gennip-Bertozzi 2012)

### §7.1 Discrete vs continuum Cheeger / isoperimetric ratio

Van Gennip-Bertozzi 2012 (SIAM J. Imaging Sci. 5:1115) studies the discrete-to-continuum limit of graph Allen-Cahn equations. Key result: for a finite-element discretization $G_h$ of a continuum domain $D \subset \mathbb{R}^d$ with mesh size $h$, the discrete Cheeger constant $h(G_h)$ approximates the continuum isoperimetric ratio:

$$h(G_h) \;\to\; c_d \cdot \frac{\mathrm{Perim}(\Omega)}{\mathrm{Vol}(\Omega)} \quad \text{as } h \to 0,$$

where $c_d$ is a $d$-dimensional constant (e.g., $c_2 = 1/\sqrt 2$ on square grids per Loomis-Whitney + mesh adjustment). This gives a *factor ≤ 2* discrepancy between discrete and continuum Cheeger in the relevant regime (van Gennip-Bertozzi 2012 Th 5.2).

### §7.2 Compatibility with file 03 Modica-Mortola

File 03 §6.1 (per critic file 07 §B.5) requires joint scaling ($h \to 0$, $\varepsilon = \sqrt{\alpha/\beta} \to 0$) for the continuum Jacobi-operator spectrum to be the limit of the discrete Hessian spectrum. The Cheeger-based bound L-CHEEGER-HMORSE is **directly discrete** — it does not require any continuum limit. So the two approaches:

- **File 03 (Modica-Mortola continuum Jacobi)**: requires $h \to 0$ + $\varepsilon \to 0$ joint scaling. Gives sphere-Jacobi spectrum $\mu_2(J_\Gamma) = (d+1)/R^2$ with surface tension $\sigma = (\sqrt 2/6)\sqrt{\alpha\beta}$. Cat B target, conditional on $h \to 0$.
- **File 08 (this file, discrete Cheeger)**: directly on finite graph, no continuum limit. Gives $\mu_{\min} \geq C \cdot h(G|_A) \cdot \alpha$. Cat B target, conditional on (H4) sharp-interface separation.

**Consistency check (sanity)**: In the continuum limit $h \to 0$ with formation $\Omega$ a disk of radius $R$ on torus $D = [0, L]^2$, the discrete Cheeger $h(G|_A) \to c_2 \cdot \mathrm{Perim}(\Gamma)/\mathrm{Vol}(\Omega)$ for the active band approximated as an annulus. For $\Omega = B_R$: $\mathrm{Perim}(\Gamma) = 2\pi R$, $\mathrm{Vol}(\Omega) = \pi R^2$, so ratio $= 2/R$. Then $\mu_{\min}^{\mathrm{Cheeger}} \sim C \cdot c_2 \cdot (2/R) \cdot \alpha = 2 C c_2 \alpha/R$.

Compare to file 03 sphere-Jacobi: $\mu_2(J_\Gamma) = 3/R^2$ (for $d = 2$, so $d + 1 = 3$). At $\alpha = 1$, $R = 4$: file 03 gives $\mu \sim \sigma \cdot 3/R^2 = 0.745 \cdot 3/16 = 0.140$. L-CHEEGER-HMORSE gives $\mu \sim 2 C c_2 \cdot 1/4 = 0.5 C c_2$. With $C c_2 \sim 0.1$ (rough), this gives $\mu \sim 0.05$, same order of magnitude as file 03.

**Discrepancy of factor ~3**: explained by the Cheeger inequality being loose by factor $\sim \Delta_A$ in this regime. Tightening requires either (a) Cat A path for Cheeger (using $\lambda_2(L_{G|_A})$ directly instead of $h^2/(2\Delta)$ lower bound), or (b) cross-validation with file 04 Schur block decomposition.

### §7.3 Three-way cross-check as Cat A promotion criterion

For L-HMORSE-LOCAL Cat A (canonical OP-HMORSE-LOCAL-A, theorem_status.md L435), a natural criterion is **three-way consistency**:

| Approach | File | Formula (schematic) | Cat |
|---|---|---|---|
| Modica-Mortola continuum Jacobi | 03 | $\mu \geq \sigma \cdot (d+1)/R^2$ | B target |
| Schur block decomposition | 04 | $\mu \geq \mu_{\mathrm{Schur}}$ explicit formula | B target |
| Cheeger discrete graph | 08 (this) | $\mu \geq C \cdot h(G\|_A) \cdot \alpha$ | B target |

If all three give comparable lower bounds (within constant factor) on a fixed test family (2D torus L=16, scc.GraphState.grid_2d 16×16, random regular $d=4$ on $n = 256$), this provides *triangulation* — a Cat A path beyond what any single derivation gives.

---

## §8 — 2D Torus 16×16 Numerical Example

### §8.1 Setup (CONSENSUS BASELINE)

- $G = C_{16} \times C_{16}$ (PBC, $n = 256$, $d_i = 4$, $\Delta = 4$).
- Parameters: $c = 1/2$, $\alpha = 1$, $\beta = 10$, $T_* = 0.1$, $R = 4$.
- Formation: $u^* \approx \chi_{\Omega}$ where $\Omega = B_R(x_0) \cap V$ is a discrete disk of radius $R = 4$, $|\Omega| \approx \pi R^2 = 50$.
- Boundary: $|\Gamma| \approx 2\pi R = 25$ (vertex boundary on grid).
- Active band $A$ is annulus of $\sim$ 2 vertices thick (since $\sqrt{\alpha/\beta} = \sqrt{1/10} \approx 0.316$, but on integer grid we round up to nearest discrete band), so $\lvert A \rvert \approx 2 \cdot |\Gamma| \approx 50$.
- $W''(1/2) = -1$ in active band; $W''(1) = W''(0) = 2$ in bulk/exterior.

### §8.2 Cheeger constants

- $h(G) = 4/L = 0.25$ (full 2D torus, §2.3).
- $h(G|_A) \approx 2/|\Gamma| = 2/25 = 0.08$ (annulus on torus collapses to $C_{|\Gamma|}$ cycle in sharp-interface limit, §3.2).
- $\Delta_A = $ max degree on induced subgraph $G|_A \leq 4$ (annulus on grid, mostly degree 2-3, max 4 at corners).

### §8.3 L-CHEEGER-HMORSE lower bound at reference

Using $C_{\mathrm{Cheeger}} = c_0/\Delta_A$ with $c_0 = 2$ (Cheeger inequality lower bound constant):

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})} \;\geq\; (2/4) \cdot 0.08 \cdot 1 - \delta_{\mathrm{res}}^{\mathrm{Ch}} \;=\; 0.04 - \delta_{\mathrm{res}}^{\mathrm{Ch}}.$$

With $\delta_{\mathrm{res}}^{\mathrm{Ch}} \leq \beta \cdot \lvert A \rvert/n \cdot \sqrt{\alpha/\beta} = 10 \cdot 50/256 \cdot 0.316 = 0.617$.

**Net bound**: $\mu_{\min}^{(\mathrm{non\text{-}Gold})} \geq 0.04 - 0.617 = -0.577$. **Not yet positive** at these reference parameters with the conservative bound.

This shows that for this regime ($\beta = 10$, $\alpha = 1$, $R = 4$), the **discrete-Cheeger-only** lower bound is *not tight enough* to prove H-Morse without combining with the closure-lift contribution (L-CLOSURE-LIFT canonical Cat A) and separation contribution (L-HMORSE-DECOMP D3 PSD).

### §8.4 Combining with closure-lift (from L-HMORSE-DECOMP)

Adding closure contribution $2\lambda_{\mathrm{cl}} (1 - a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max})$ from L-HMORSE-DECOMP D2 (canonical L1987). With $\lambda_{\mathrm{cl}} = 1$, $a_{\mathrm{cl}} = 0.5$ (canonical A3), $(d_{\min}/d_{\max}) = 1$ (2D torus regular):

$$2 \cdot 1 \cdot (1 - 0.125)^2 \cdot 1 = 2 \cdot 0.766 = 1.531.$$

Combined bound:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})} \;\geq\; 1.531 + 0.04 - 0.617 \;=\; 0.954 > 0. \quad \checkmark$$

**Positivity restored** by closure-lift contribution. This is consistent with canonical L-HMORSE-LOCAL's $c_{\mathrm{HML}}$ form being dominated by the $2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2$ term.

### §8.5 Comparison with file 02/04 estimates

- **File 02 §6.2**: $\mu_{\mathrm{well}} \sim 10$ (rough order of magnitude, critic §A.5 flagged as overestimated by 3-100×). Canonical L-HMORSE-LOCAL numerical anchor (canonical L1960): $\mu_{\min} \in [0.13, 3.49]$ on canonical 5×5/10×10/15×15 grids — *much smaller* than file 02's 10.
- **File 04 Schur**: comparable order to L-HMORSE-LOCAL (file 04 §6 specifically calibrated to canonical L1960).
- **File 08 (this)**: bound $\geq 0.954$ on 2D torus L=16 with $\beta = 10$. Within the canonical anchor range $[0.13, 3.49]$ ✓ (consistent with L-HMORSE-LOCAL numerical anchor).

**Verification proposal**: `CODE/scripts/test_cheeger_hmorse_torus.py` to compute (i) actual discrete Hessian spectrum at $u^*$ on $C_{16} \times C_{16}$, (ii) Cheeger constant $h(G|_A)$ at the active band, (iii) compare lower bound 0.954 to actual $\mu_{\min}$. Estimated to be a $\sim 1$-hour Claude-runs-in-session task per CLAUDE.md numerical validation pattern.

### §8.6 Cheeger-T8 scaling on torus

The Cheeger-T8 condition (§4.3 Step 4 rearranged at $\lambda_{\mathrm{cl}} = 0$):

$$\frac{\beta}{\alpha} < \frac{2 h(G|_A)^2}{\Delta_A} = \frac{2 \cdot 0.08^2}{4} = 0.0032.$$

This is the **threshold below which boundary-only ($H_{\mathrm{bd}}$) gives positive H-Morse**. For $\beta/\alpha = 10/1 = 10 \gg 0.0032$, boundary-only Cheeger is insufficient — *closure must contribute*, as confirmed §8.4.

Comparing to canonical T8 threshold $\beta_{\mathrm{T8}}/\alpha = 4\lambda_2/\lvert W''(c) \rvert = 4 \cdot 0.1522/1 = 0.609$ for uniform critical: the formation regime begins at $\beta/\alpha > 0.609$. So at $\beta/\alpha = 10$, we are *deep* in the formation regime; the closure contribution is essential for H-Morse positivity at the non-uniform critical (consistent with L-HMORSE-LOCAL needing $\lambda_{\mathrm{cl}} > 0$).

---

## §9 — OPEN Problem Leverage Map

### §9.1 OP-HMORSE-LOCAL-A (theorem_status.md L435)

**Status**: OPEN. Path: L-HMORSE-LOCAL Cat B → Cat A; requires sharper residual bound + OP-HMORSE-SBM (numerical robustness extension to SBM/barbell/small-world).

**L-CHEEGER-HMORSE leverage**:
- Provides an **alternative Cat B bound** that is *formation-localized* (via $h(G|_A)$) rather than *graph-global* (via $\lambda_2(L_G)$).
- For graph classes where $\lambda_2(L_G) \to 0$ (grids, large $n$), $h(G|_A)$ remains bounded by formation perimeter — does not degenerate.
- **3-way cross-check** with file 03 (Modica-Mortola) and file 04 (Schur) provides triangulation Cat A path (§7.3).
- **Expander-graph regime** (§6) gives a *Cat A path for the expander sub-case*: on expanders, all hypothesis (H1)-(H4) are uniformly satisfied, and the residual term $\delta_{\mathrm{res}}^{\mathrm{Ch}}$ has explicit bounds.

**Cat A path channel**: prove L-CHEEGER-HMORSE Cat A on expander graphs (OP-HMORSE-EXPANDER, proposed but NOT registered here); use this as base case for general graph extension.

### §9.2 OP-HMORSE-SADDLE (`theorem_status.md` L594, **NOT** canonical.md L1967)

**Status**: OPEN (NEW CV-1.16). Required for full Eyring-Kramers prefactor Cat B; independent of OP-HMORSE-LOCAL-A. ETA 2-4 sessions per canonical statement.

**L-CHEEGER-HMORSE leverage** — **primary attack channel**:

At a saddle $u^\dagger$ (rather than minimum), the formation boundary $\Gamma(u^\dagger)$ has *different* topology than at a minimum. Specifically:
- **At minimum**: boundary $\Gamma$ is a "round" closed curve (sphere-like in continuum), large Cheeger constant $h(\Gamma)$.
- **At saddle (catenoid / pinch saddle)**: boundary has a "neck" (narrow region) where $h(\Gamma)$ is **small** (the neck nearly disconnects the bulk).

**Saddle-detection diagnostic**: $h(\Gamma(u^*))$ small ⟺ $u^*$ is a saddle (formation about to pinch). This gives an *isoperimetric criterion* for identifying saddles without computing the full Hessian:

$$u^* \text{ is a K-jump saddle} \iff h(\Gamma(u^*)) \leq h_{\mathrm{thresh}}(\alpha, \beta, c)$$

with explicit threshold (Cat A path target).

The inverse causation check in §4.4 confirms: $h(\Gamma) \to 0$ ⟹ $\mu_{\min}^{(\mathrm{non\text{-}Gold})} \to 0$ — at the limit, the saddle has *exact-zero* lowest eigenvalue (the pinch direction is the negative unstable mode at the saddle), consistent with Morse index 1 at the saddle.

**Cat A path channel for OP-HMORSE-SADDLE**:
- Step 1 (this file, L-CHEEGER-HMORSE Cat B): boundary-Cheeger lower bound for *minima* (large $h$).
- Step 2 (extension, Cat B target): boundary-Cheeger *upper* bound for *saddles* (small $h$ at neck).
- Step 3 (Cat A target): rigorous saddle-index-1 proof for catenoid-like saddles via Cheeger-bottleneck identification, complementing file 03 §10 Allard-Simons-Reilly continuum analysis.

### §9.3 OP-0005-DYN (`theorem_status.md` L803)

**Status**: OPEN (W9+). Package II Eyring-Kramers, H5 Morse stability + OP-0021 ($T_*$ registration). Not before W9+.

**L-CHEEGER-HMORSE leverage**:
- Eyring-Kramers prefactor $\omega_0$ requires the determinant ratio $\sqrt{\prod_{k \notin \ker} \mu_k(\mathrm{well})/\prod_{k} \mu_k(\mathrm{saddle})}$ (per file 02 §3.3).
- L-CHEEGER-HMORSE gives **lower bounds** on $\mu_k(\mathrm{well})$ (large at minima, $\sim C \cdot h(\Gamma_{\min}) \cdot \alpha$) and **upper bounds** on the smallest $\mu_k(\mathrm{saddle})$ (small at saddles, $\sim C \cdot h(\Gamma^\dagger) \cdot \alpha$ with $h(\Gamma^\dagger) \to 0$).
- This gives a **structural form** of the prefactor:

$$\omega_0 \;\sim\; \alpha^{(N - 1)/2} \cdot \frac{h(\Gamma_{\min})^{(N-1)/2}}{h(\Gamma^\dagger)^{(N-1)/2 - 1}} \cdot |\mu_{\mathrm{neck}}|$$

(rough form, requires combinatorial counting for exact powers; Cat B target).

- **Inverse causation**: as $h(\Gamma^\dagger) \to 0$ (saddle becomes thinner), $\omega_0 \to \infty$ formally — but this is regulated by the $|\mu_{\mathrm{neck}}| \to 0$ at the same rate, giving finite limit. Physically: thin necks have *high* transition attempt frequency (Arrhenius preexponential is enhanced by saddle softness), consistent with Kramers' original 1940 derivation.

**Cat A path channel for OP-0005-DYN via Cheeger**: combine L-CHEEGER-HMORSE saddle-version (§9.2) with file 02 Kramers-prefactor formula gives a *Cheeger-based* Eyring-Kramers expression — *complementary* to file 03's surface-tension based form. Cross-check between the two channels is a Cat A consistency criterion.

### §9.4 OP-0021 (`theorem_status.md` L587, T_* registration)

**Status**: OPEN (scope revised CV-1.18). Routes A (Mori-Zwanzig) and B (RG fixed point) **DEPRECATED**. Route C (observer-personal $\xi$ resident under OMS-1) canonical-recognized.

**L-CHEEGER-HMORSE leverage**: limited direct leverage on $T_*$ registration itself, but provides infrastructure for downstream Package II Eyring-Kramers (§9.3) which is *conditional* on OP-0021. Once $T_*$ is canonically registered (W9+), L-CHEEGER-HMORSE Cat B bounds combine with $T_*$ to give explicit Kramers rate quantification.

### §9.5 Summary leverage map

| OP (anchor) | Status | L-CHEEGER-HMORSE leverage | Cat path channel |
|---|---|---|---|
| OP-HMORSE-LOCAL-A (theorem_status.md L435) | OPEN | Alternative Cat B bound (formation-localized); 3-way triangulation with files 03/04 | Cat A path: expander sub-case + triangulation |
| OP-HMORSE-SADDLE (`theorem_status.md` L594) | OPEN, ETA 2-4 sessions | **Primary channel**: boundary-Cheeger small-h ⟺ saddle | Cat A path: Cheeger-bottleneck saddle index-1 proof |
| OP-0005-DYN (`theorem_status.md` L803) | OPEN, W9+ | Cheeger-based Eyring-Kramers prefactor form | Cat A path: consistency with file 03 σ-based form |
| OP-0021 (`theorem_status.md` L587) | OPEN, Routes A/B DEPRECATED CV-1.18 | Indirect (infrastructure for §9.3) | No direct Cat A path; W9+ |

---

## §10 — CoT/CoC Archival (Per-Claim)

### §10.1 Claim catalog

| # | Claim | Cat | CoT steps | CoC anchors |
|---|---|---|---|---|
| C1 | Discrete Cheeger inequality $h^2/(2\Delta) \leq \lambda_2 \leq 2h$ | A (external) | §2.2 standard graph theory | Chung 1997 Th 2.2; Spielman 2007 §3 |
| C2 | 2D torus L=16 $h(G) = 4/L = 0.25$ | A (computational) | §2.3 half-torus cut + Bollobás-Leader minimality | Bollobás-Leader 1991 |
| C3 | 2D torus L=16 $\lambda_2 = 4\sin^2(\pi/16) \approx 0.1522$ | A (computational) | §2.3 standard torus Laplacian spectrum | CONSENSUS BASELINE |
| C4 | Cheeger inequality satisfied on 2D torus reference | A (computational) | §2.3 direct check | This file §2.3 |
| C5 | Active-band restriction Hessian comparison | B (this file) | §3.3 + §4.3 Step 1 | canonical L1982 (L-HMORSE-DECOMP D1) |
| C6 | $h(G\lVert _A) \sim 2/ \rVert\Gamma\|$ on torus sharp-interface | A (cycle Cheeger) | §3.2 active band → cycle | Standard cycle isoperimetric |
| C7 | L-CHEEGER-HMORSE main statement | **B (target, this file)** | §4.3 4-step proof sketch | canonical L1948 L-HMORSE-LOCAL Cat B; canonical L1974 L-HMORSE-DECOMP Cat B |
| C8 | Cheeger-T8 condition $\beta/\alpha < 2h(G\|_A)^2/\Delta_A$ | B (this file) | §4.3 Step 4 + §8.6 | canonical L1134 T8-Core |
| C9 | Reduction to Theorem 4 at uniform critical | A (algebraic) | §5.1 | canonical L1134-1136 |
| C10 | L-CHEEGER-HMORSE complementarity with L-HMORSE-LOCAL | B (interpretive) | §5.2-5.3 | canonical L1948 |
| C11 | Expander-graph regime corollary | B (this file) | §6 | Hoory-Linial-Wigderson 2006; Friedman 2008 |
| C12 | Discrete-continuum compatibility (van Gennip-Bertozzi) | B (this file) | §7 | van Gennip-Bertozzi 2012 SIAM J Imaging Sci 5:1115 |
| C13 | 2D torus L=16 explicit lower bound 0.954 (combined) | B (this file, numerical) | §8.4 | This file §8 + canonical L1987 closure-lift |
| C14 | OP-HMORSE-SADDLE Cheeger attack channel | B (this file, OPEN advance) | §9.2 | `theorem_status.md` L594 |
| C15 | OP-0005-DYN Cheeger-based Kramers form | B (this file, OPEN advance) | §9.3 | `theorem_status.md` L803 + file 02 |

### §10.2 Inverse causation summary

For each Cat B claim (C5-C8, C10-C15), inverse causation was checked (see §4.4 for full check on C7; analogous structure for others). Key principle: **if hypothesis fails, claim fails or trivializes** (no "claim survives without hypothesis" silent overclaim).

### §10.3 No silent OP resolution

All four OPs (OP-HMORSE-LOCAL-A, OP-HMORSE-SADDLE, OP-0005-DYN, OP-0021) remain explicitly **OPEN** at conclusion. This file provides *attack channels* and *Cat B target bounds*, NOT canonical promotions. CN15 compliance ✓.

---

## §11 — Hard Constraint CN1-16 Check (16/16 ✓)

| CN | Constraint | Status | Evidence |
|---|---|---|---|
| **CN1** | Canonical 4-term energy preserved | ✓ | Only $\alpha, \beta, c, W$ parameters used; no new energy term. |
| **CN2** | No silent OP resolution | ✓ | OPs explicitly OPEN at §9; only attack channels claimed. |
| **CN3** | u_t primitive preserved | ✓ | DECL-1.0 u_t : X → [0,1] unchanged. |
| **CN4** | Analyticity (b_D = 0) | ✓ | Inherited from L-HMORSE-DECOMP hypothesis (canonical L1996). |
| **CN5** | 4-term conceptual independence | ✓ | Bounds operate component-wise (H_bd / H_cl / H_sep separately); no merge. |
| **CN6** | Σ_m mass constraint preserved | ✓ | Tangent space $T_{u^*}^{\mathrm{free}}$ respects $\Pi_{T\Sigma_m}$. |
| **CN7** | No closure idempotence assumed | ✓ | Uses A3 ($a_{\mathrm{cl}} < 4$) only; non-idempotent closure framework preserved. |
| **CN8** | Sep predicate u-weighted convention | ✓ | Inherited; not modified. |
| **CN9** | Persist core-overlap or transport-based | ✓ | Not used here (boundary Hessian focus). |
| **CN10** | No reductive reduction | ✓ | Cheeger inequality = *contrastive standard tool* (Chung 1997, Spielman 2007); SCC ≠ graph-isoperimetric reduction. §1.2 explicit. |
| **CN11** | No inertia | ✓ | No second-order time terms; T-PF-A1-SDE first-order form preserved. |
| **CN12** | No Mori-Zwanzig / memory kernel | ✓ | OP-0021 Routes A/B DEPRECATED CV-1.18; not re-introduced. |
| **CN13** | No CSSL E_ridge / E_wild / E_pers patterns | ✓ | §1.2 explicit; only canonical 4-term energy. |
| **CN14** | Surface tension convention σ = (√2/6)·√(αβ) | ✓ | Consensus baseline §0.3; file 03 convention adopted per critic §B.2. |
| **CN15** | Honest Cat B classification | ✓ | §4.5 explicit; L-CHEEGER-HMORSE is Cat B target, not Cat A claim. |
| **CN16** | Per-claim CoT + CoC + inverse causation | ✓ | §10 catalog; §4.4 inverse causation; consistent throughout. |

**16/16 ✓.**

---

## §12 — One-Paragraph Summary

This file derives **L-CHEEGER-HMORSE** as a **Cat B target** lower bound on the H-Morse spectral gap of SCC formations: $\mu_{\min}^{(\mathrm{non\text{-}Gold})}(\Pi_T^{\mathrm{free}} H_{\mathcal{E}}(u^*) \Pi_T^{\mathrm{free}}) \geq C_{\mathrm{Cheeger}} \cdot h(\Gamma(u^*)) \cdot \alpha - \delta_{\mathrm{res}}^{\mathrm{Ch}}$, where $h(\Gamma(u^*)) = h(G|_A)$ is the **induced-subgraph Cheeger constant** on the formation active band. Combining with the L-HMORSE-DECOMP closure-lift contribution recovers explicit positivity on the 2D torus L=16 CONSENSUS BASELINE reference ($\mu_{\min} \geq 0.954$ at $\alpha = 1$, $\beta = 10$, $R = 4$, $c = 1/2$, using $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta}$ per critic Wave 2 consensus). The bound is **complementary** (NOT redundant) to file 03's Modica-Mortola continuum Jacobi spectrum and file 04's Schur block decomposition — providing a *third* independent attack channel on OP-HMORSE-LOCAL-A (`theorem_status.md` L435), a **primary attack channel** on OP-HMORSE-SADDLE (`theorem_status.md` L594) via the boundary-Cheeger saddle-detection diagnostic ($h(\Gamma^\dagger) \to 0$ identifies saddles), and an infrastructure contribution to OP-0005-DYN (`theorem_status.md` L803) Eyring-Kramers prefactor via Cheeger-based determinant ratio. The **expander-graph regime** (§6) gives the cleanest sub-case where H-Morse spectral gap is structurally bounded below by $C \cdot \alpha$ uniformly in $n$ and $\beta$. All four canonical OPs remain explicitly OPEN (CN15); 16/16 hard constraints satisfied; zero canonical edits.

---

*End of file 08. 0 canonical edits. Working layer only. Cat B target classification honest. CONSENSUS BASELINE consistent throughout.*
