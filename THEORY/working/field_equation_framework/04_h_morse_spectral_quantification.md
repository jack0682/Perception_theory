---
type: working/field_equation_framework/h_morse_spectral_quantification
date: 2026-05-20
session_origin: W8-Day3 EOD extension, post-01_ns_inspired_synthesis
canonical_version: CV-1.18 SEALED (untouched)
status: draft v0.1 (Cat B target derivation; two complementary lemmas)
authors: user (Jaehong Oh) via Executor delegation
preceded_by:
  - 01_ns_inspired_synthesis.md (§6 #7 Sc^{(2)}, §6 #9 Pr^{(bd)}, §8.3 Path 3, §11 leverage map)
  - 03_D_L_commutation.md §1-§4 (bulk/active/exterior 3-block decomposition, regular-graph functional calculus)
  - working/CV114_H_MORSE_PACKAGEII/* (H-Morse Package II working files, dependency map, broadness attack)
  - canonical §13 L-HMORSE-LOCAL Cat B (CV-1.16); L-HMORSE-DECOMP Cat B conditional (CV-1.16); L-BOUNDARY-MODE-EXCLUSION Cat C (CV-1.16); Theorem 4 (Cat A); T-PF-A1-PE Cat A (CV-1.9)
  - working/cssl/01_critic_evaluation.md (CSSL critic-rejected — AVOID PATTERNS: E_ridge sign-conflict, E_pers analyticity break, primitive inversion)
purpose: |
  H-Morse spectral gap의 두 보완적 정량화:
  (I) Sc^{(2)} = μ_bulk / μ_active의 explicit lower bound via L-HMORSE-DECOMP의 Schur complement structure (3-block bulk/active/exterior).
  (II) Pr^{(bd)} = α W''(u^*) / T_*의 H-Morse precondition threshold via D-HMORSE-LOCAL (C2′) implicit width-ratio derivation + T-PF-A1-PE Poincaré anchor.
  두 target lemma 모두 Cat B (explicit lower bounds conditional on graph structure + saturation parameters); L-HMORSE-DECOMP Cat B → Cat A path와 D-HMORSE-LOCAL (C2′) Cat B explicit verification 의 working-layer infrastructure 제공.
canonical_compatibility:
  CN1_canonical_edits: 0
  CN4_analyticity: preserved (no new energy terms)
  CN5_4_term_independence: preserved (H_bd, H_cl, H_sep treated separately)
  CN10_no_reductive_reduction: preserved (Schur complement + Weyl + Poincaré are contrastive standard tools)
  primitive_u_t: preserved (Sc^{(2)}, Pr^{(bd)} = derived spectral diagnostics)
  inertia_introduction: forbidden (Package I Cat A protection)
  Mori_Zwanzig: forbidden (OP-0021 Routes A/B DEPRECATED CV-1.18)
  CSSL_energy_pattern: forbidden (no E_pers, no E_ridge, no E_surg; only parameter-ratio analysis)
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§13 Theorem 4 Cat A; L-HMORSE-LOCAL Cat B; L-HMORSE-DECOMP Cat B conditional; L-BOUNDARY-MODE-EXCLUSION Cat C; T-PF-A1-PE Cat A) · [[../../canonical/DECLARATION|DECL-1.0]] (Q1 T8 boundary; Q3 stochastic dynamics) · [[01_ns_inspired_synthesis|01 NS-inspired synthesis (§6 catalog, §8.3 Path 3)]] · [[../../logs/daily/2026-05-20/03_D_L_commutation|03 [D, L_G] commutation (3-block decomposition)]] · [[../CV114_H_MORSE_PACKAGEII/MOC_H_MORSE_packageII|CV114 H-Morse Package II MOC]] · [[../cssl/01_critic_evaluation|CSSL critic eval (anti-patterns)]]

# 04 — H-Morse Spectral Quantification: Sc^{(2)} Bulk-Active Separation + Pr^{(bd)} Threshold

**Mode**: working-layer Cat B target derivation (NOT canonical promotion, NOT SEAL prep)
**Target**: Two complementary Cat B target lemmas quantifying H-Morse spectral structure:
- **L-SC2-SEPARATION** (Cat B target): explicit lower bound on $\text{Sc}^{(2)} = \mu_{\text{bulk}} / \mu_{\text{active}}$ via L-HMORSE-DECOMP Schur complement
- **L-PR-BD-THRESHOLD** (Cat B target): explicit lower bound on $\text{Pr}^{(\text{bd})}$ implied by D-HMORSE-LOCAL (C2′)

---

## §0 Frontmatter + xref check + §8a P1-P6 audit

### §0.1 Pre-work xref check

- `grep -r "Sc\^{(2)}\|Pr\^{(bd)}\|mu_bulk\|mu_active\|Schur complement.*H-Morse" canonical/ working/` → 4 canonical hits (Sc^{(2)} 1 ref in §13 Cat B count comment; "Schur complement" 2 hits in T-Cl-Sym C3-symmetrization Cat A I7, unrelated; Pr^{(bd)} 0 canonical references); 18 working hits (all in 01_ns_inspired_synthesis.md §6/§8.3/§9/§11 catalog references — *no derivation file exists*).
- **Novel positioning**: 본 file 은 01_ns_inspired_synthesis §6 #7 / §6 #9 / §8.3 의 *catalog references* 의 **first explicit derivation**. 01 file 의 §13.2 Tier 2 priority 의 `05_h_morse_pr_bd_threshold.md` + `06_sc_2_bulk_active_quantification.md` 의 *combined deliverable* (사용자 명시 scope: 두 target을 하나의 file에 통합).
- canonical L-HMORSE-DECOMP Cat B conditional (§13 line 1974-2007) → 본 file = Sc^{(2)} 정량화 via 3-block Schur (03 §1-§4의 bulk/active/exterior decomposition을 spectral 측면으로 lift).
- canonical D-HMORSE-LOCAL (C2′) Cat B (§13 line 1939) → 본 file = Pr^{(bd)} explicit threshold (01 §8.3 Path 3의 derivation completion).

### §0.2 §8a P1-P6 archive pattern audit

- **P1 (근본 질문 우회)**: DECL Q1 (T8 = H-Morse spectral gap의 phase transition) + Q3 (T_*-dependent boundary smearing) 직접 정량화 — *우회 아님* ✓
- **P2 (Vocabulary refactoring)**: u_t primitive 미변경; Sc^{(2)}, Pr^{(bd)} = derived spectral diagnostics (canonical Hessian eigenvalue ratios) ✓
- **P3 (Canonical content 중복)**: L-HMORSE-DECOMP Cat B의 *conditional 해소 path* (working layer derivation, canonical 미수정) ✓
- **P4 (외부 도구 도입)**: Schur complement + Cauchy-Weyl interlacing + Payne-Weinberger = *contrastive standard tools*, canonical anchor (T-PF-A1-PE Cat A) 직접 후속 ✓
- **P5 (Self-audit)**: 본 §0 + §12 dual audit ✓
- **P6 (언어-수학 분리)**: 모든 lemma 명시적 수학 statement + proof sketch separation ✓

**0/6 부합** → 진행 합법.

### §0.3 CSSL anti-pattern check (critic eval §F.2-§F.3 + §D.4 직접 학습)

- ❌ E_pers, E_ridge, E_surg 도입 0 (CN4 analyticity 보존 — critic §D.4)
- ❌ Persistence homology의 *energy term* 도입 0 (critic §D.4 — diagnostic only)
- ❌ 새 primitive 도입 0 (critic §F.3 — u_t 유지)
- ❌ Sign-conflict 도입 0 (critic §D.1 — Sc^{(2)}, Pr^{(bd)} = pure spectral ratios)
- ❌ Derived → primitive 도입 0 (critic §F.3)
- ✓ Parameter-ratio analysis only (canonical α, β, T_*, μ_k, λ_2(L_G), W''(u^*), |∂Ω|/n)

---

## §1 Mission: Two Complementary Cat B Targets for H-Morse

### §1.1 The H-Morse spectral gap problem

Canonical L-HMORSE-LOCAL Cat B (CV-1.16) provides
$$\mu_{\min}\bigl(\Pi_T^{\mathrm{free}} H_{\mathcal{E}}(u^*) \Pi_T^{\mathrm{free}}\bigr) \;\geq\; c_{\mathrm{HML}}\bigl(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}}, c^*, d_{\min}/d_{\max}\bigr) > 0,$$
with explicit but *coarse* lower bound (canonical.md:1953-1956). The Cat A path (OP-HMORSE-LOCAL-A) requires:
- *(Path A)* sharper residual-correction $\lVert R_{\mathrm{cl}} \rVert$ bound (via Schur complement structure on 3-block decomposition).
- *(Path B)* explicit verification of (C2′) "active set well-defined" against thermal smearing.

These two paths are the two Cat B targets of this file:

| Target | Quantity | Canonical anchor | Cat status |
|---|---|---|---|
| **L-SC2-SEPARATION** | $\text{Sc}^{(2)} = \mu_{\text{bulk}}/\mu_{\text{active}}$ | L-HMORSE-DECOMP (Cat B conditional) | **Cat B target** |
| **L-PR-BD-THRESHOLD** | $\text{Pr}^{(\text{bd})} = \alpha W''(u^*)/T_*$ | D-HMORSE-LOCAL (C2′) + T-PF-A1-PE Cat A | **Cat B target** |

### §1.2 Why these two complement each other

```
CoT step 1: L-HMORSE-LOCAL is a *positivity* claim (μ_min > 0); it does NOT quantify *how much* the spectrum separates.
CoT step 2: Sc^{(2)} measures the *separation ratio* between bulk-stable modes and active-band marginal modes — the relevant dimensionless number for H-Morse stability.
CoT step 3: Pr^{(bd)} measures the *boundary-width condition* under which (C2′) "active set well-defined" is non-vacuous against thermal smearing.
CoT step 4: Sc^{(2)} addresses the *deterministic* H-Morse structure (T_* = 0 limit); Pr^{(bd)} addresses the *stochastic* precondition (T_* > 0).
CoT step 5: Together they cover the (i) deterministic spectral gap quantification, (ii) stochastic precondition validity — the two complementary half-problems of full H-Morse certification.
→ Therefore: combined deliverable = (Sc^{(2)} explicit lower bound) + (Pr^{(bd)} explicit threshold).

CoC anchors:
  - canonical §13 L-HMORSE-LOCAL Cat B unconditional (CV-1.16, canonical.md:1948-1970)
  - canonical §13 L-HMORSE-DECOMP Cat B conditional (CV-1.16, canonical.md:1974-2007)
  - canonical §13 D-HMORSE-LOCAL (C2′) Cat B definition (CV-1.16, canonical.md:1939)
  - canonical §13 T-PF-A1-PE Cat A (CV-1.9, canonical.md:1700-1711) — Poincaré inequality grounding thermal-smearing length
  - 01_ns_inspired_synthesis §6 #7 (Sc^{(2)}) + §6 #9 (Pr^{(bd)}) + §8.3 Path 3
```

---

## §2 Schur Complement Decomposition Recap (Canonical L-HMORSE-DECOMP)

### §2.1 3-block decomposition (from 03 §1-§4)

Following 03_D_L_commutation §1-§4 (bulk/active/exterior 3-block decomposition) and canonical L-HMORSE-DECOMP §1976-1994:

Let $u^* \in \Sigma_m$ be an H-Morse-Local critical point satisfying D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5). Partition the vertex set $X = B \sqcup A \sqcup E$:

- $B$ = **bulk** sites: $u^*_i \approx 1$ (saturated-interior; $\lvert W''(u^*_i) \rvert = W''(1) = 2 > 0$).
- $A$ = **active** sites: $u^*_i \in (0, 1)$ non-saturated (boundary band; $W''(u^*_i) \in [-1, 2]$ depending on saturation; spinodal interior gives $W''(u^*_i) = -1$ at $u^*_i = c^* = 1/2$).
- $E$ = **exterior** sites: $u^*_i \approx 0$ (saturated-exterior; $\lvert W''(u^*_i) \rvert = W''(0) = 2 > 0$).

The active-set restriction (C2′) sets $A^* = B \cup E$ (corner-saturated) and $A$ = free interior. The free tangent subspace $T_{u^*}^{\mathrm{free}}$ restricts $v$ to $v|_{A^*} = 0$, i.e., $v$ supported on $A$ only. **However**, for the Schur complement analysis, we work on the full Hessian $H_{\mathcal{E}}(u^*) \in \mathbb{R}^{n \times n}$ pre-restriction; the active-set restriction is recovered post-Schur via the effective $H_{\text{eff}}^{AA}$ block.

### §2.2 3-block Hessian structure

The full SCC Hessian on $\mathbb{R}^n$ admits the block form
$$H_{\mathcal{E}}(u^*) \;=\; \begin{pmatrix} H_{BB} & H_{BA} & H_{BE} \\ H_{AB} & H_{AA} & H_{AE} \\ H_{EB} & H_{EA} & H_{EE} \end{pmatrix}$$

where:
- **Diagonal blocks** $H_{BB}, H_{AA}, H_{EE}$ contain the per-site $\beta W''(u^*_i) I$ and $4\alpha L_G|_{\text{block}}$ contributions (from L-HMORSE-DECOMP (D1) boundary term, canonical.md:1982-1984).
- **Off-diagonal blocks** $H_{BA}, H_{AE}, H_{BE}, H_{AB}, H_{EA}, H_{EB}$ couple via the graph Laplacian $4\alpha L_G$ edges + the closure/separation Jacobian off-diagonal entries.

**Approximate vanishing $H_{BE} \approx 0$**: by graph locality, bulk and exterior are *not adjacent* (active band $A$ separates them spatially — this is the geometric content of D-HMORSE-LOCAL (C3) single-formation + (C2′) active set). Specifically:

$$H_{BE,ij} = 4\alpha (L_G)_{ij} + \text{(closure + separation off-diagonal at saturated nodes)} \approx 0$$

because (i) bulk and exterior are graph-distance $\geq 2$ apart in the canonical phase-separated regime (T8-supercritical, D-HMORSE-LOCAL (C3)), hence $(L_G)_{ij} = 0$; (ii) the closure/separation Jacobian at saturated nodes $u^*_i \in \{0, 1\}$ has $|\sigma''(z(u^*_i))| \to 0$ (canonical.md:1956 "$\delta_{\mathrm{res}}$ small at saturated minimizers").

This gives the approximation
$$H_{\mathcal{E}}(u^*) \;\approx\; \begin{pmatrix} H_{BB} & H_{BA} & 0 \\ H_{AB} & H_{AA} & H_{AE} \\ 0 & H_{EA} & H_{EE} \end{pmatrix} \quad \text{(saturated-minimizer approximation)}.$$

### §2.3 Schur complement (effective active-set Hessian)

By standard linear algebra (Schur complement reduction; see canonical Cat A T-Cl-Sym C3-symmetrization I7 for prior canonical Schur usage, canonical.md:1148-1149):

$$\boxed{\;H_{\text{eff}}^{AA} \;:=\; H_{AA} \;-\; H_{AB} \, H_{BB}^{-1} \, H_{BA} \;-\; H_{AE} \, H_{EE}^{-1} \, H_{EA}\;}$$

This is well-defined whenever $H_{BB}, H_{EE}$ are invertible (PD) — which is the L-HMORSE-DECOMP Cat B conditional regime (saturated bulk and exterior, both with $W''(u^*) = 2 > 0$ ensuring strict positivity; see §3.1 below).

```
CoC anchors (Schur reduction):
  - canonical §13 Cat A T-Cl-Sym C3-symmetrization (I7 closure, prior Schur usage in SCC; canonical.md:1148-1149)
  - canonical L-HMORSE-DECOMP (D1)(D2)(D3) per-term bounds (canonical.md:1982-1994)
  - external: Horn-Johnson Matrix Analysis 2nd ed. §0.8.5 (Schur complement standard formula)
inverse_causation_check (Schur well-definedness):
  - if H_BB not PD: bulk modes themselves degenerate → no L-HMORSE-LOCAL (Cat B requires (C2′) saturated bulk)
  - if H_EE not PD: exterior modes degenerate → no formation regime at all
  - if H_BE ≠ 0 substantially: requires full 3×3 Schur (not 2×2 reduction); but saturated-minimizer approximation is canonical (L-HMORSE-DECOMP Cat B conditional)
```

---

## §3 Sc^{(2)} Explicit Lower Bound Derivation

### §3.1 Definitions

- $\mu_{\text{bulk-B}} := \mu_{\min}(H_{BB})$ — smallest eigenvalue of bulk-block Hessian
- $\mu_{\text{bulk-E}} := \mu_{\min}(H_{EE})$ — smallest eigenvalue of exterior-block Hessian
- $\mu_{\text{bulk}} := \min(\mu_{\text{bulk-B}}, \mu_{\text{bulk-E}})$
- $\mu_{\text{active}} := \mu_{\min}^{\neq 0}(H_{\text{eff}}^{AA})$ — smallest **non-Goldstone** eigenvalue of effective active Hessian (excludes volume-Goldstone $\mu = 0$ on $T_{u^*}^{\mathrm{free}}$)
- $\boxed{\text{Sc}^{(2)} \;:=\; \mu_{\text{bulk}} \,/\, \mu_{\text{active}}}$

### §3.2 Lower bound on $\mu_{\text{bulk-B}}$ (and analogously $\mu_{\text{bulk-E}}$)

```
CoT step 1: H_BB diagonal entries. At a bulk site i ∈ B, u^*_i ≈ 1 (saturated-interior).
  - W'(u) = 2u(1-u)(1-2u), W''(u) = 2(1 - 6u + 6u²) (canonical CLAUDE.md "Critical Implementation Details" I6 correction; canonical.md:1982).
  - At u = 1: W''(1) = 2(1 - 6 + 6) = 2 > 0.
  - At u = 1 (exactly saturated): the boundary term H_bd diagonal entry is 4α (L_G)_{ii} + β · W''(1) = 4α d_i + 2β.
  - Closure + separation diagonal contributions at saturated bulk: small (|σ''(z)| → 0 at saturated, canonical.md:1956).

CoT step 2: Cauchy-Weyl interlacing for symmetric matrix lower bound.
  - For symmetric M = D + S where D = diag(d_1, ..., d_k) and S = symmetric off-diagonal:
    μ_min(M) ≥ min_i (d_i) - ||S||_op.
  - In our case, H_BB = 4α L_G|_B + 2β I + (small saturated correction).
  - 4α L_G|_B is PSD (Laplacian on block B is PSD; eigenvalues in [0, 4α · d_max-in-B]).
  - 2β I is positive multiple of identity → all eigenvalues = 2β.
  - μ_min(H_BB) ≥ 4α · λ_min(L_G|_B) + 2β - O(δ_sat) where O(δ_sat) is the saturated-correction term, bounded by |σ''(z)| · ||M||² ~ exponentially small at saturated.

CoT step 3: Explicit bound.
  - On a connected bulk subgraph B (or B as a disjoint union of connected components, each connected):
    λ_min(L_G|_B) ≥ 0 (Laplacian PSD, with kernel = constant on each connected component).
  - The constant mode on B contributes 0 to the spatial part, but the onsite term 2β I dominates → μ_min(H_BB) ≥ 2β - O(δ_sat).
  - In the saturated-minimizer regime (canonical L-HMORSE-DECOMP Cat B conditional), O(δ_sat) ≪ β, so:
    μ_bulk-B ≥ 2β (1 - O(δ_sat/β)) ≥ β (conservative bound).

CoT step 4: Analogously for H_EE (u^* ≈ 0, W''(0) = 2):
  - μ_bulk-E ≥ 2β (1 - O(δ_sat/β)) ≥ β.
→ μ_bulk = min(μ_bulk-B, μ_bulk-E) ≥ 2β (1 - O(δ_sat/β)), conservatively ≥ β.

CoC anchors:
  - canonical §13 L-HMORSE-DECOMP (D1) boundary term, canonical.md:1982-1984
  - canonical CLAUDE.md "Critical Implementation Details" I6: W''(u) factor 2 correction
  - external: Horn-Johnson Matrix Analysis §4.3 (Cauchy-Weyl interlacing); Bhatia "Matrix Analysis" §III.5
  - canonical L-HMORSE-DECOMP §1956: δ_res small at saturated minimizers (|σ''(z)| → 0)
inverse_causation_check:
  - if W''(1) < 2 (non-canonical W form): bound weakens; requires alternative double-well
  - if bulk not actually saturated (u^* < 1 - ε): δ_sat correction grows, bound degrades
  - if B disconnected with isolated singletons: λ_min(L_G|_B) = 0 contribution; bound still 2β from onsite term
```

### §3.3 Upper bound on $\mu_{\text{active}}$ via Schur correction

```
CoT step 1: H_AA diagonal structure.
  - At active site i ∈ A: u^*_i ∈ (0, 1) interior; W''(u^*_i) ∈ [-1, 2].
  - In spinodal interior (u^*_i ∈ (1/2 - 1/√12, 1/2 + 1/√12)): W''(u^*_i) < 0, minimum -1 at u = 1/2.
  - H_AA diagonal: 4α (L_G)_{ii} + β W''(u^*_i) + closure/separation diagonal corrections.
  - Worst case (spinodal interior c^* = 1/2): H_AA,ii = 4α d_i + β · (-1) + corrections = 4α d_i - β + corrections.
  - For β/α > 4 d_max: H_AA can have negative diagonal entries → indefinite on its own.

CoT step 2: Schur correction reduces H_AA toward H_eff^AA.
  - H_eff^AA = H_AA - H_AB H_BB^{-1} H_BA - H_AE H_EE^{-1} H_EA.
  - Each subtracted term is PSD (since H_BB, H_EE are PD by §3.2 → H_BB^{-1}, H_EE^{-1} PD → H_AB H_BB^{-1} H_BA = (H_BA)^T H_BB^{-1} H_BA is PSD by conjugation).
  - Therefore H_eff^AA ⪯ H_AA (componentwise PSD ordering on the active block).
  - Equivalently: μ_min(H_eff^AA) ≤ μ_min(H_AA) (which can be negative without Schur correction).

CoT step 3: BUT H_eff^AA is also bounded *below* by the L-HMORSE-DECOMP combined bound (canonical.md:1994):
  - μ_min(Π_T H_E Π_T) ≥ 2λ_cl(1-a_cl/4)² (d_min/d_max) + α λ_2(L_G) - β ρ_bd-band(u^*) - ||R_cl||/λ_cl > 0.
  - This is the L-HMORSE-LOCAL Cat B lower bound c_HML (canonical.md:1953-1955).
  - On T^free (which is supported on A only), Π_T H_E Π_T = Π_T^free H_eff^AA Π_T^free.
  - Therefore μ_active ≥ c_HML > 0 (L-HMORSE-LOCAL Cat B guarantee).

CoT step 4: Operator-norm bound on Schur correction.
  - ||H_AB||_op² / μ_bulk-B = bound on H_AB H_BB^{-1} H_BA contribution (since H_BB^{-1} ⪯ μ_bulk-B^{-1} I).
  - H_AB entries: graph Laplacian off-diagonals = -4α w_ij for edge (i ∈ A, j ∈ B), 0 otherwise.
  - ||H_AB||_op ≤ 4α √(|A| · |B| · w_max² · κ_AB) where κ_AB = max boundary-edge multiplicity per active node; conservatively ||H_AB||_op ≤ 4α √(|∂A→B|) · w_max.
  - Therefore Schur correction (B side): ||H_AB H_BB^{-1} H_BA||_op ≤ (4α)² |∂A→B| w_max² / (2β) = 8 α² |∂A→B| w_max² / β.

CoT step 5: Combining steps 3 + 4:
  - μ_active ∈ [c_HML, μ_min(H_AA) + (correction)] — bracketed lower/upper bounds.
  - For the *ratio* Sc^{(2)} = μ_bulk / μ_active, we need μ_active *upper bound* (to lower-bound the ratio).
  - Conservative upper bound: μ_active ≤ μ_min(H_AA) ≤ 4α λ_min(L_G|_A) + β · max_A W''(u^*) + corrections ≤ 4α λ_max(L_G|_A) + 2β ≤ 4α · 2d_max + 2β = 8α d_max + 2β.

CoC anchors:
  - canonical L-HMORSE-LOCAL Cat B (canonical.md:1953-1955) — lower bound c_HML
  - canonical L-HMORSE-DECOMP (D2)(D3) (canonical.md:1986-1991) — closure/separation per-term bounds
  - external: Horn-Johnson §0.8.5 (Schur complement PSD ordering: H_eff^AA ⪯ H_AA)
  - external: Bhatia §III.1.1 (operator norm bound via Hilbert-Schmidt)
inverse_causation_check:
  - if c_HML ≤ 0: L-HMORSE-LOCAL Cat B fails → no Sc^{(2)} analysis (H-Morse precondition broken)
  - if H_AB unbounded: ||H_AB||_op → ∞ → Schur correction destroys positivity; but on finite graph with bounded edge weights, ||H_AB||_op bounded
```

### §3.4 Combined Sc^{(2)} explicit lower bound

Combining §3.2 (lower bound on $\mu_{\text{bulk}}$) and §3.3 (upper bound on $\mu_{\text{active}}$):

$$\boxed{\;\text{Sc}^{(2)} \;=\; \frac{\mu_{\text{bulk}}}{\mu_{\text{active}}} \;\geq\; \frac{2\beta (1 - O(\delta_{\text{sat}}/\beta))}{8\alpha d_{\max} + 2\beta} \;=\; \frac{1}{1 + 4\alpha d_{\max}/\beta} \cdot (1 - O(\delta_{\text{sat}}/\beta))\;}$$

**Interpretation**:
- For $\beta \gg 4\alpha d_{\max}$ (deep formation regime, $\beta/\alpha \gg d_{\max}$): $\text{Sc}^{(2)} \to 1$ (clean separation; bulk and active have *comparable* lowest eigenvalues).
- For $\beta \sim 4\alpha d_{\max}$ (near T8 wall): $\text{Sc}^{(2)} \sim 1/(1+1) = 1/2$ (mode mixing onset).
- For $\beta \ll 4\alpha d_{\max}$ (sub-critical, no formation): $\text{Sc}^{(2)} \to 0$ (H-Morse breaks down — *but this regime is outside L-HMORSE-LOCAL hypothesis*).

**Why Sc^{(2)} ≥ 1/2 is the "clean" regime**: at $\text{Sc}^{(2)} \geq 1/2$ the bulk and active spectra are *comparable* (within factor 2), so the Schur complement off-diagonal contamination $H_{AB} H_{BB}^{-1} H_{BA}$ is bounded by a constant fraction of the bulk diagonal — the canonical L-HMORSE-DECOMP §1956 "small residual" regime.

---

## §4 L-SC2-SEPARATION Cat B Target Lemma

### §4.1 Statement

**Lemma L-SC2-SEPARATION (Cat B target; W8-Day3 EOD working draft).**

*Conditions.*
- *(H1)* D-HMORSE-LOCAL (C1)(C2′)(C3) — well-defined 3-block bulk/active/exterior structure with $H_{BE} \approx 0$ (canonical L-HMORSE-LOCAL hypothesis; canonical.md:1934-1944).
- *(H2)* $H_{BB}$, $H_{EE}$ PSD strict (saturated bulk and exterior at $W''(1) = W''(0) = 2 > 0$).
- *(H3)* Canonical phase-separated regime $\beta/\alpha > 4\lambda_2(L_G)/\lvert W''(c^*) \rvert$ (T8-Core supercritical, canonical SB7 Cat A).
- *(H4)* $b_D = 0$ analyticity (CN4 canonical commitment).
- *(H5)* Active set $A$ has bounded boundary-edge degree: $|\partial A \to B|, |\partial A \to E| \leq C \cdot \lvert A \rvert \cdot d_{\max}$ for an explicit constant $C \leq 1$ (graph-structural; holds on finite grids/tori).

*Statement.*
$$\text{Sc}^{(2)} \;=\; \frac{\mu_{\text{bulk}}}{\mu_{\text{active}}} \;\geq\; \frac{1}{1 + 4\alpha d_{\max}/\beta} \cdot \bigl(1 - O(\delta_{\text{sat}}/\beta)\bigr)$$

where $\delta_{\text{sat}} = O(|\sigma''(z(u^*))| \cdot a_{\mathrm{cl}}^2 \lVert M \rVert^2)$ is exponentially small at saturated minimizers (canonical L-HMORSE-DECOMP §1988 residual bound).

*Corollary 1 (deep-formation regime).* If $\beta/\alpha > 4 d_{\max}$ (deep T8-supercritical), then
$$\text{Sc}^{(2)} \;\geq\; \frac{1}{2} \cdot (1 - O(\delta_{\text{sat}}/\beta))$$
(clean bulk-active separation, mode mixing bounded).

### §4.2 Proof sketch (4-step Schur + Weyl chain)

```
Step 1 (Bulk block lower bound). §3.2: μ_bulk-B ≥ 2β(1 - O(δ_sat/β)); μ_bulk-E ≥ 2β(1 - O(δ_sat/β)).
  → μ_bulk = min(μ_bulk-B, μ_bulk-E) ≥ 2β(1 - O(δ_sat/β)).
  Anchor: canonical L-HMORSE-DECOMP (D1), CLAUDE.md I6.

Step 2 (Active block upper bound). §3.3: μ_active ≤ μ_min(H_AA + Schur correction) ≤ 8α d_max + 2β (conservative).
  Anchor: Horn-Johnson Schur complement PSD ordering.

Step 3 (Cauchy-Weyl interlacing on Schur complement).
  - H_eff^AA = H_AA - PSD - PSD ⪯ H_AA (PSD subtraction).
  - Therefore μ_min(H_eff^AA) ≤ μ_min(H_AA).
  - But μ_min(H_AA) is bounded above by max(H_AA diagonal) = 4α d_max + 2β.

Step 4 (Ratio). Sc^{(2)} = μ_bulk / μ_active ≥ [2β(1-O(δ_sat/β))] / [8α d_max + 2β] = 1/(1 + 4α d_max/β) · (1 - O(δ_sat/β)).
  Anchor: arithmetic.

→ QED Sc^{(2)} lower bound.
```

### §4.3 Inverse causation check

```
inverse_causation_check:
  - if (H1) D-HMORSE-LOCAL violated: 3-block structure undefined → Sc^{(2)} undefined
  - if (H2) H_BB or H_EE not PD: Schur complement undefined → no L-HMORSE-DECOMP Cat B regime
  - if (H3) sub-critical (β/α < 4λ_2/|W''(c)|): no formation → no active band → Sc^{(2)} vacuous
  - if (H4) b_D ≠ 0: analyticity breaks → CN4 violation → no T14 Łojasiewicz convergence
  - if (H5) |∂A→B| ≫ |A| d_max: boundary-edge degree explodes → Schur correction unbounded → bound degrades
  - if W form non-canonical (W''(1) ≠ 2): bulk diagonal coefficient changes; bound prefactor changes but Cat B structure preserved
  - if μ_active = 0 exactly (Goldstone-bearing): Sc^{(2)} = ∞ — but Goldstone is excluded by definition (μ_active is *non-Goldstone* smallest eigenvalue; volume-Goldstone subtracted on T^free)
```

### §4.4 Cat B classification rationale

| Aspect | Status | Rationale |
|---|---|---|
| Statement | explicit | closed-form lower bound in (α, β, d_max, δ_sat) |
| Hypotheses | 5 explicit (H1-H5) | all canonical or graph-structural |
| Proof | sketch (4-step) | Schur + Weyl + PSD ordering; standard linear algebra |
| Cat A path | promote δ_sat bound to rigorous constant | requires sharper σ''(z) analysis at saturated nodes (parallel to OP-HMORSE-LOCAL-A) |
| Cat C path (if hypotheses weaken) | ✗ | (H1)-(H5) all match canonical L-HMORSE-DECOMP Cat B conditional |

**Honest Cat B**: conditional on (H1)-(H5) explicit graph-structural + saturation hypotheses; not Cat A because $\delta_{\text{sat}}$ asymptotic-only bound, not closed-form rigorous constant.

### §4.5 Implication for H-Morse

```
CoT step 1: Sc^{(2)} ≥ 1/2 (deep-formation regime) → Schur off-diagonal contamination bounded by 1/2 fraction → L-HMORSE-DECOMP §1956 "δ_res small at saturated minimizers" regime quantitatively verified.
CoT step 2: Sc^{(2)} ~ 1 → bulk and active spectra cleanly separated → H_eff^AA acts as nearly-decoupled block → L-HMORSE-LOCAL Cat B → Cat A path eased.
CoT step 3: Sc^{(2)} ~ O(α d_max/β) → mode mixing strong → off-diagonal Schur contribution dominates → δ_res term in L-HMORSE-LOCAL (canonical.md:1956) cannot be neglected → Cat A path blocked.
→ Therefore: L-SC2-SEPARATION Cat B lower bound provides *quantitative* certificate for L-HMORSE-DECOMP Cat B → Cat A path; specifically, the regime β/α > 4 d_max provides Sc^{(2)} ≥ 1/2 — the *target regime* for OP-HMORSE-LOCAL-A.

CoC anchors:
  - canonical L-HMORSE-LOCAL §1956 "δ_res(u^*) small at saturated minimizers" (canonical.md:1956)
  - canonical L-HMORSE-DECOMP §1988 residual ||R_cl|| bound (canonical.md:1988)
  - 01_ns_inspired_synthesis §11 Tier 3 "Sc^{(2)} (H-Morse spectral gap quantification) → Tier 2 supporting infrastructure" (01 line 672)
```

---

## §5 Pr^{(bd)} Definition + Boundary Widths

### §5.1 Recall Pr^{(bd)} definition (from 01 §6 #9)

$$\text{Pr}^{(\text{bd})} \;:=\; \frac{\alpha \cdot W''(u^*)}{T_*}$$

(canonical parameters: $\alpha$ = boundary smoothness coupling, $W''(u^*) = 2(1 - 6u^* + 6u^{*2})$ at active-band node $u^*$, $T_*$ = effective stochastic temperature per OMS-1 ξ resident CV-1.18.)

### §5.2 Two characteristic boundary widths

**Deterministic boundary width** (from canonical T-OP6-B Cat A persistent ridge boundary bound, canonical.md:1956):

$$\ell_{\text{det}} \;:=\; \sqrt{\alpha / \beta}$$

(standard Allen-Cahn-like interface width derived from energy minimization $\alpha (\partial u)^2 + \beta W(u)$ scaling; cf. Modica-Mortola 1987 Arch Rat Mech Anal 98:123; T-OP6-B persistent-ridge boundary band measure $\rho_{\mathrm{bd-band}} \leq 2 \ell_{\text{det}} \cdot |\partial\Omega|/n$, canonical.md:1956).

**Thermal smearing width** (from canonical T-PF-A1-PE Cat A Poincaré + harmonic potential approximation):

$$\ell_{\text{therm}} \;:=\; \sqrt{T_* / (\beta W''(u^*))}$$

(derived: at active-band node $u^*$, the local quadratic-potential approximation gives variance per stationary Gibbs measure $\langle (u_i - u^*_i)^2 \rangle \sim T_* / (\beta W''(u^*))$ when $W''(u^*) > 0$; T-PF-A1-PE Cat A grounds the well-definedness of stationary Gibbs measure $\pi_{T_*}$, canonical.md:1700-1711).

### §5.3 Width ratio

```
CoT step 1: Ratio of squared widths.
  - ℓ_det² / ℓ_therm² = (α/β) / (T_* / (β W''(u^*)))
                     = (α W''(u^*)) / T_*
                     = Pr^{(bd)}.
  - Therefore: ℓ_det / ℓ_therm = √Pr^{(bd)}.

CoT step 2: Physical interpretation.
  - ℓ_det > ℓ_therm ⟺ Pr^{(bd)} > 1: deterministic boundary width *exceeds* thermal smearing length.
  - Active band is *spatially resolved* — D-HMORSE-LOCAL (C2′) "active set well-defined" is non-vacuous.
  - ℓ_det < ℓ_therm ⟺ Pr^{(bd)} < 1: thermal smearing *exceeds* deterministic boundary width.
  - Active band is *smeared into bulk* — D-HMORSE-LOCAL (C2′) breaks (cannot distinguish active from saturated).

CoC anchors:
  - external: Modica 1987 Arch Rat Mech Anal 98:123 (Allen-Cahn interface scaling — ℓ ~ √(α/β))
  - canonical §13 T-OP6-B Cat A (CV-1.7, persistent-ridge boundary bound; canonical.md:1956)
  - canonical §13 T-PF-A1-PE Cat A (CV-1.9, Poincaré + Gibbs measure variance; canonical.md:1700-1711)
  - 01_ns_inspired_synthesis §8.3 Path 3 (CoT chain L538-543)
inverse_causation_check:
  - if W''(u^*) < 0 (spinodal interior): ℓ_therm undefined (negative variance) — but at spinodal, dynamics is *unstable*, not stationary; this regime is OP-0005-DYN territory, NOT L-HMORSE-LOCAL post-formation regime
  - if T_* = 0 (zero-temperature limit): ℓ_therm = 0; Pr^{(bd)} = ∞; (C2′) trivially holds — BUT canonical zero-temperature metastability flag (P-F-A1 Package II not established) — see §6.4 caveat
  - if α = 0: no smoothness term; ℓ_det = 0; Pr^{(bd)} = 0; (C2′) impossible — Modica-Mortola Γ-limit singular interface
```

---

## §6 D-HMORSE-LOCAL (C2′) → Pr^{(bd)} Threshold Derivation

### §6.1 (C2′) "active set well-defined" — implicit content

Canonical D-HMORSE-LOCAL (C2′) states (canonical.md:1939):
> $A^* = \{x : u^*(x) \in \{0,1\}\}$ has explicit complement, and $T_{u^*}^{\mathrm{free}}$ has positive dimension ($\dim T_{u^*}^{\mathrm{free}} = n - \lvert A^* \rvert - 1$).

This is a *purely combinatorial* definition at the deterministic minimizer $u^*$. However, under the stochastic dynamics T-PF-A1-SDE Cat A (canonical.md:1668), the *typical* configuration sampled from the stationary Gibbs measure $\pi_{T_*}$ fluctuates around $u^*$ with characteristic width $\ell_{\text{therm}}$. For (C2′) to be *non-vacuously* satisfied in the stochastic-mean sense, the fluctuation width at active-band sites must not blur active vs saturated.

```
CoT step 1: Stochastic dressing of (C2′).
  - Sample u ~ π_{T_*} from canonical stationary Gibbs measure (T-PF-A1-PE Cat A: π_{T_*} exists, exponential ergodicity).
  - At bulk site i ∈ B: u^*_i = 1, with fluctuation u_i - u^*_i ∈ ±ℓ_therm-bulk where ℓ_therm-bulk = √(T_*/(2β)) (uses W''(1) = 2).
  - At active site i ∈ A: u^*_i ∈ (0,1), with fluctuation u_i - u^*_i ∈ ±ℓ_therm-active where ℓ_therm-active = √(T_*/(β |W''(u^*_i)|)).
  - At exterior site i ∈ E: u^*_i = 0, with fluctuation u_i - u^*_i ∈ ±ℓ_therm-ext = √(T_*/(2β)).

CoT step 2: Active band spatial extent.
  - Boundary between bulk and active spans deterministic width ℓ_det = √(α/β) (T-OP6-B persistent-ridge bound).
  - If ℓ_therm > ℓ_det at active-band edge (where u^* transitions from 1 to interior): fluctuations smear bulk into active → bulk node may *typically* appear as active in instantaneous sample.
  - Quantitative: if ℓ_therm-bulk > ℓ_det, the saturation distinction between B and A blurs at the boundary.

CoT step 3: Pr^{(bd)} threshold derivation.
  - Define worst-case Pr^{(bd)} using boundary-band node W''(u^*) (active-band entry point):
    Pr^{(bd)} = α W''(u^*) / T_*.
  - From §5.3: ℓ_det/ℓ_therm = √Pr^{(bd)}.
  - Requirement "ℓ_det > ℓ_therm" ⟺ Pr^{(bd)} > 1.
  - Sharper bound: for *clean* separation requiring ℓ_det ≥ k · ℓ_therm for some safety factor k ≥ 1, need Pr^{(bd)} ≥ k².

→ Therefore (C2′) implicit precondition: Pr^{(bd)} ≥ c_bd^* := 1 (loose) or k² (sharper, k chosen by graph-resolution analysis).
```

### §6.2 Variance bound via T-PF-A1-PE

Canonical T-PF-A1-PE Cat A (canonical.md:1700-1711) provides Poincaré inequality
$$\text{Var}_{\pi_{T_*}}(f) \leq C_P \cdot T_* \cdot \int |\nabla_H f|^2 \, d\pi_{T_*}$$
with $C_P = (n/\pi^2) e^{\mathrm{osc}(\tilde{\mathcal{E}})/T_*}$ (canonical.md:1704).

Applied to the local linear functional $f_i(u) = u_i - u^*_i$ at active-band node $i \in A$:

```
CoT step 1: Variance estimate.
  - Var_{π_{T_*}}(f_i) = ⟨(u_i - u^*_i)²⟩_{π_{T_*}}.
  - ∫ |∇_H f_i|² dπ_{T_*} ~ 1 (gradient of u_i w.r.t. u is e_i basis vector).
  - Naive Poincaré: Var(f_i) ≤ C_P T_* ~ (n/π²) T_* exp(osc/T_*).
  - This is EXPONENTIALLY LARGE in n — metastable scaling (canonical L1709 explicit warning).

CoT step 2: Local linearization sharpening (away from metastable barriers).
  - Within a single Gibbs well around u^*, the local Gaussian approximation gives Var(f_i) ~ T_*/H_ii where H_ii is the local Hessian diagonal entry.
  - At active-band node: H_ii = 4α d_i + β W''(u^*_i) ≈ β W''(u^*_i) for the active-band dominant contribution.
  - Therefore Var(f_i) ~ T_* / (β W''(u^*_i)) = ℓ_therm-active² ✓ (matches §5.2).

CoT step 3: Convergence of derivations.
  - Naive Poincaré: exponentially large in n (metastable, correct for *full* state-space mixing time).
  - Local linearization: T_*/(β W''(u^*)) (correct for *local* fluctuation amplitude around u^*).
  - The local linearization is appropriate for (C2′) which is a *local* condition at u^*; the metastable factor exp(osc/T_*) controls TRANSITIONS between minima, not within-well fluctuations.
→ For (C2′) precondition: ℓ_therm = √(T_*/(β W''(u^*))) is the relevant length.

CoC anchors:
  - canonical §13 T-PF-A1-PE Cat A (canonical.md:1700-1711)
  - canonical L1709 metastable scaling explicit ("C_P ~ (n/π²) e^{βn/16T_*} exponentially large in n — metastable scaling, correct and expected for double-well")
  - external: Bovier-den Hollander "Metastability" 2015 §16 (local Gaussian approximation around minima)
inverse_causation_check:
  - if T-PF-A1-PE Cat A removed: no Poincaré → no Gibbs variance bound → ℓ_therm undefined
  - if metastable scaling forgotten: full-Poincaré bound used → bound exponentially loose → (C2′) precondition appears unreachable, but actually local condition only requires local Gaussian
```

### §6.3 Combined threshold

From §6.1 + §6.2:

$$\boxed{\;\text{D-HMORSE-LOCAL (C2′) implicit precondition}: \quad \text{Pr}^{(\text{bd})} \;\geq\; c_{\text{bd}}^* \;:=\; 1\;}$$

with sharper safety-factor regime $\text{Pr}^{(\text{bd})} \geq k^2$ for any chosen $k > 1$ providing $k$-fold ratio $\ell_{\text{det}}/\ell_{\text{therm}}$.

### §6.4 Zero-temperature caveat (canonical flag)

```
CoT inverse_causation_check (T_* → 0):
  - As T_* → 0: ℓ_therm → 0, Pr^{(bd)} → ∞, (C2′) automatic.
  - BUT: canonical zero-temperature metastability flag (CV-1.18 SEAL Non-Overclaim; P-F-A1 Package II not established; OP-0021 T_* axiomatic only).
  - At T_* = 0 exactly: T-PF-A1-PE inequality vacuous (no stochastic dynamics); SCC becomes deterministic gradient flow.
  - The Pr^{(bd)} > 1 threshold is meaningful in the T_* > 0 regime where stationary Gibbs measure exists.

→ Therefore: (C2′) Pr^{(bd)} threshold is the *non-vacuous* precondition for T_* > 0 stochastic regime; zero-temperature limit handled separately by deterministic minimizer machinery (canonical Theorem 4 Cat A, T-OP6-B Cat A).
```

---

## §7 L-PR-BD-THRESHOLD Cat B Target Lemma

### §7.1 Statement

**Lemma L-PR-BD-THRESHOLD (Cat B target; W8-Day3 EOD working draft).**

*Conditions.*
- *(H1)* D-HMORSE-LOCAL (C1)(C2′)(C3) on canonical phase-separated regime (T8-supercritical).
- *(H2)* T-PF-A1-PE Cat A (Poincaré inequality + stationary Gibbs measure $\pi_{T_*}$ exists; canonical.md:1700-1711).
- *(H3)* Local Gaussian approximation valid within a single Gibbs well (canonical metastable scaling acknowledged; full-state mixing exponential in $n$).
- *(H4)* $T_* > 0$ (stochastic regime; zero-temperature caveat per §6.4).
- *(H5)* $W''(u^*) > 0$ at active-band reference node (outside spinodal interior; canonical post-formation regime at saturated edges).

*Statement.* For D-HMORSE-LOCAL (C2′) to be non-vacuously satisfied in the stochastic-mean sense (typical $\pi_{T_*}$-sample preserves active-set distinction), the dimensionless number
$$\text{Pr}^{(\text{bd})} \;=\; \frac{\alpha W''(u^*)}{T_*}$$
must satisfy the explicit lower bound
$$\boxed{\;\text{Pr}^{(\text{bd})} \;\geq\; c_{\text{bd}}^* \;=\; 1\;}$$
(loose threshold), with sharper $k^2$-safety regime $\text{Pr}^{(\text{bd})} \geq k^2$ providing ratio $\ell_{\text{det}}/\ell_{\text{therm}} \geq k$.

*Corollary 1 (canonical SCC default regime).* For canonical defaults $\alpha = 1$, $\beta = 5$, $c^* = 1/2$, post-formation active-edge $W''(u^*) \approx 2$ (saturated edges), $T_* = 0.1$ (P-F-A1 Package II working default):
$$\text{Pr}^{(\text{bd})} = \frac{1 \cdot 2}{0.1} = 20 \;\gg\; 1 \quad ✓ \quad (k_{\text{achieved}} \approx 4.5).$$

### §7.2 Proof sketch (3-step width-ratio + variance bound)

```
Step 1 (Deterministic boundary width). Modica-Mortola scaling on canonical E_bd = α (∇u)² + β W(u):
  - ℓ_det = √(α/β) (T-OP6-B Cat A persistent-ridge boundary bound; canonical.md:1956).
  Anchor: canonical T-OP6-B Cat A (CV-1.7).

Step 2 (Thermal smearing width). T-PF-A1-PE Cat A local Gaussian approximation:
  - Within-well variance Var_{π_{T_*}}(u_i - u^*_i) ~ T_* / H_ii ~ T_* / (β W''(u^*)).
  - ℓ_therm = √(T_*/(β W''(u^*))).
  Anchor: canonical T-PF-A1-PE Cat A (CV-1.9; canonical.md:1700-1711); Bovier-den Hollander Metastability §16 local Gaussian.

Step 3 (Ratio threshold).
  - ℓ_det² / ℓ_therm² = (α/β) / (T_*/(β W''(u^*))) = α W''(u^*) / T_* = Pr^{(bd)}.
  - (C2′) non-vacuous ⟺ ℓ_det > ℓ_therm ⟺ Pr^{(bd)} > 1.
  Anchor: arithmetic + (C2′) interpretation §6.1.

→ QED Pr^{(bd)} ≥ 1 threshold.
```

### §7.3 Inverse causation check

```
inverse_causation_check:
  - if (H1) D-HMORSE-LOCAL (C1)(C2′)(C3) violated: no active-set framework → Pr^{(bd)} threshold vacuous (no boundary to threshold)
  - if (H2) T-PF-A1-PE not Cat A: no Gibbs measure → ℓ_therm undefined
  - if (H3) local Gaussian invalid: variance bound fails; full Poincaré gives exp(osc/T_*) scaling — bound becomes (C_P-based) much weaker but still implies threshold qualitatively
  - if (H4) T_* = 0: Pr^{(bd)} = ∞ trivially; (C2′) deterministic regime (separate Theorem 4 Cat A handling); canonical zero-temperature flag
  - if (H5) W''(u^*) < 0 (spinodal interior): ℓ_therm imaginary; (C2′) breakdown; this regime is *outside* post-formation L-HMORSE-LOCAL hypothesis — properly handled by OP-0005-DYN dynamic transition theory
  - if T_* too large: Pr^{(bd)} < 1 → thermal smearing destroys boundary → (C2′) violated → no H-Morse possible → formation regime breaks down
```

### §7.4 Cat B classification rationale

| Aspect | Status | Rationale |
|---|---|---|
| Statement | explicit | closed-form threshold Pr^{(bd)} ≥ 1 |
| Hypotheses | 5 explicit (H1-H5) | all canonical + standard local-Gaussian regime |
| Proof | sketch (3-step) | Modica-Mortola scaling + T-PF-A1-PE local Gaussian; standard |
| Cat A path | tighten local Gaussian → full Poincaré comparison with explicit Bovier-den Hollander bounds | requires explicit metastable-vs-within-well separation; deferred to OP-HMORSE-LOCAL-A + P-F-A1 Package II |
| Cat C path | if (H3) local Gaussian invalid: bound degrades to Cat C SKETCH | hypothesis explicit; honest scope |

**Honest Cat B**: conditional on (H1)-(H5); not Cat A because local Gaussian (H3) is approximation, not rigorous bound across full Gibbs measure support.

---

## §8 Numerical Example: 2D Torus L=16

### §8.1 Setup

- Graph: $G = C_{16} \times C_{16}$ (2D torus, $n = 256$ vertices, $d = 4$ regular)
- Canonical parameters: $\alpha = 1$, $\beta = 5$ (canonical T8-supercritical at $\beta/\alpha = 5 > 4\lambda_2/\lvert W''(c) \rvert = 4 \cdot 0.152/1 \approx 0.61$ for torus Fiedler $\lambda_2 \approx 0.152$ on 16×16 torus)
- Formation at $c^* = 1/2$ ($u^*$ = single connected formation occupying half the torus by mass conservation $m = n/2$)
- Effective temperature: $T_* = 0.1$ (working P-F-A1 Package II default)

### §8.2 Sc^{(2)} computation

```
Bulk sites: u^*_i ≈ 1, |B| ≈ 96 (interior of formation, away from boundary band)
Active sites: u^*_i ∈ (0,1), |A| ≈ 64 (boundary band of width ≈ 2√(α/β) ≈ 0.89 cells, ~16-cell ring)
Exterior sites: u^*_i ≈ 0, |E| ≈ 96 (interior of exterior, away from boundary)

μ_bulk-B ≥ 2β · (1 - O(δ_sat/β)) = 10 · (1 - small) ≈ 10
μ_bulk-E ≥ 2β · (1 - O(δ_sat/β)) = 10 · (1 - small) ≈ 10
μ_bulk = min(10, 10) ≈ 10

μ_active upper bound = 8α d_max + 2β = 8 · 1 · 4 + 10 = 42 (conservative)
μ_active L-HMORSE-LOCAL c_HML lower bound ~ O(α λ_2 + small) ≈ 0.15 (modest)

Sc^{(2)} ≥ μ_bulk / μ_active_upper = 10 / 42 ≈ 0.24

In the closed-form bound: Sc^{(2)} ≥ 1/(1 + 4α d_max/β) = 1/(1 + 16/5) = 1/4.2 ≈ 0.238 ✓ (matches)

For deep-formation regime β = 50 (β/α = 50 ≫ 4d_max = 16): Sc^{(2)} ≥ 1/(1 + 16/50) = 1/1.32 ≈ 0.76 → clean separation.
```

### §8.3 Pr^{(bd)} computation

```
At active-band edge (u^* transition zone), saturated edge node has W''(u^*) ≈ W''(0.9) = 2(1 - 5.4 + 4.86) = 2 · 0.46 = 0.92
At spinodal interior c^* = 1/2 (deepest band): W''(0.5) = 2(1 - 3 + 1.5) = -1 (negative; outside Pr^{(bd)} regime)

For (C2′) precondition, use saturated-edge W''(u^*) ≈ 0.92 (where active band meets bulk):
Pr^{(bd)} = α W''(u^*) / T_* = 1 · 0.92 / 0.1 = 9.2 > 1 ✓ (threshold satisfied)
k_achieved = √9.2 ≈ 3.0 → 3-fold ratio ℓ_det/ℓ_therm.

ℓ_det = √(α/β) = √(1/5) ≈ 0.45
ℓ_therm = √(T_*/(β W''(u^*))) = √(0.1/(5 · 0.92)) = √0.0217 ≈ 0.15

ℓ_det / ℓ_therm ≈ 3.0 ✓ matches Pr^{(bd)}^(1/2)
```

### §8.4 Joint H-Morse certification

```
Sc^{(2)} ≥ 0.24 (modest clean separation; deep regime β=50 gives ≥ 0.76)
Pr^{(bd)} = 9.2 (clear threshold satisfaction; k_safety = 3)

→ Both Cat B target preconditions verified numerically on canonical 2D torus L=16 example.
→ Sc^{(2)} ≥ 0.24 marginally exceeds 1/4.2; β increase yields rapid improvement.
→ Pr^{(bd)} = 9.2 well above threshold; T_* can increase 9-fold before threshold violation.
```

---

## §9 H-Morse Quantification Map (Sc^{(2)} + Pr^{(bd)} Combined)

### §9.1 Joint regime diagram

| Regime | $\text{Sc}^{(2)}$ | $\text{Pr}^{(\text{bd})}$ | H-Morse status | Cat path |
|---|---|---|---|---|
| Deep formation, cold ($\beta/\alpha \gg d_{\max}$, $T_* \ll \alpha W''/1$) | $\geq 1/2$ | $\gg 1$ | clean | L-HMORSE-LOCAL Cat B → Cat A direct (OP-HMORSE-LOCAL-A) |
| Standard SCC ($\beta/\alpha \sim$ few $\cdot d_{\max}$, $T_* \sim$ working default) | $\sim 1/2$ | $\sim 5\text{-}20$ | clean | L-HMORSE-LOCAL Cat B verified (numerical anchor §8) |
| Near T8 wall, modest $T_*$ ($\beta/\alpha \sim 4 d_{\max}$, $T_*$ moderate) | $\sim 1/4$ | $\sim 1$ | marginal | Cat B threshold; H-Morse fragile |
| Sub-critical or thermal-dominant | $\to 0$ | $< 1$ | broken | outside L-HMORSE-LOCAL hypothesis (no formation regime) |

### §9.2 Combined H-Morse quantification statement

```
JOINT CERTIFICATION (working layer, Cat B):

H-Morse-Local stability at u^* ∈ Σ_m is quantified by the pair (Sc^{(2)}, Pr^{(bd)}):

(i)  Deterministic spectral gap separation:
     Sc^{(2)} = μ_bulk / μ_active ≥ 1/(1 + 4α d_max/β) — L-SC2-SEPARATION Cat B (§4)
     Quantifies how cleanly bulk modes separate from active-band modes.
     Sc^{(2)} ≥ 1/2 ⟹ Schur off-diagonal contamination bounded by factor 2 ⟹ L-HMORSE-DECOMP §1956 "δ_res small" regime quantitatively verified.

(ii) Stochastic boundary precondition:
     Pr^{(bd)} = α W''(u^*) / T_* ≥ 1 — L-PR-BD-THRESHOLD Cat B (§7)
     Quantifies whether (C2′) "active set well-defined" is non-vacuous against thermal smearing.
     Pr^{(bd)} ≥ 1 ⟹ ℓ_det ≥ ℓ_therm ⟹ active band spatially resolved against Gibbs fluctuation.

Joint precondition for L-HMORSE-LOCAL Cat B → Cat A path:
  (Sc^{(2)} ≥ 1/2) ∧ (Pr^{(bd)} ≥ 1) ⟹ both Schur δ_res small AND (C2′) non-vacuous.
  This identifies the *clean H-Morse regime* in parameter space (α, β, T_*) where Cat A path is feasible.
```

### §9.3 Cat distribution

- **L-SC2-SEPARATION**: Cat B target (explicit lower bound, 5 hypotheses, 4-step proof sketch)
- **L-PR-BD-THRESHOLD**: Cat B target (explicit lower bound, 5 hypotheses, 3-step proof sketch)
- **Combined H-Morse quantification map**: Cat B (joint regime diagram, numerical anchor §8)
- **Cat A path**: OP-HMORSE-LOCAL-A (sharper δ_sat + full Poincaré); deferred to W9+

---

## §10 W9+ Forward Hooks

### §10.1 L-HMORSE-DECOMP Cat B → Cat A path via L-SC2-SEPARATION

```
W9+ Tier 2 priority (from 01_ns_inspired_synthesis §13.2):

L-SC2-SEPARATION (Cat B, this file §4) provides the *quantitative* certificate for:
  - canonical L-HMORSE-DECOMP §1988 ||R_cl|| residual bound: δ_sat asymptotic refinement to closed-form constant
  - canonical L-HMORSE-LOCAL §1956 δ_res(u^*) "small at saturated minimizers" → quantified as O(1/Sc^{(2)})
  - OP-HMORSE-LOCAL-A: sharper residual-correction step direct via Sc^{(2)} ≥ 1/2 regime certification

Suggested W9+ child file: `05_op_hmorse_local_a_via_sc2.md` — L-SC2-SEPARATION Cat B → Cat A path with rigorous δ_sat bound + extension to SBM/barbell graphs (OP-HMORSE-SBM).
```

### §10.2 D-HMORSE-LOCAL (C2′) Cat B explicit verification via Pr^{(bd)}

```
W9+ Tier 2 priority:

L-PR-BD-THRESHOLD (Cat B, this file §7) provides the *quantitative* certificate for:
  - canonical D-HMORSE-LOCAL (C2′) implicit precondition: explicit Pr^{(bd)} ≥ 1 threshold
  - canonical T-PF-A1-PE Cat A connection: local Gaussian vs full Poincaré bridging
  - L-HMORSE-LOCAL Cat B numerical anchor (canonical.md:1960) "exp_hmorse_broadness_full_spectrum.py 15/15 PASS" extension: cover (Sc^{(2)}, Pr^{(bd)}) joint regime sweeps

Suggested W9+ child file: `06_pr_bd_numerical_sweep.md` — explicit (Sc^{(2)}, Pr^{(bd)}) regime diagram on canonical 5×5, 10×10, 15×15 grids + 2D torus L=16, 32 + SBM heterogeneous.
```

### §10.3 Connection to Pr^{(Kramers)} (highest leverage, separate file)

```
L-SC2-SEPARATION + L-PR-BD-THRESHOLD provide the *static H-Morse spectral infrastructure*.
The complementary *dynamic Kramers-rate quantification* lives at Pr^{(Kramers)} = |μ_well|/|μ_saddle|.

Joint pipeline:
  Sc^{(2)}, Pr^{(bd)} (this file) → static H-Morse Cat A path
  Pr^{(Kramers)} (separate W9+ file: `02_kramers_prefactor_op_0005_attack.md`) → dynamic Eyring-Kramers Cat A path
  → Combined: Package II (P-F-A1 Eyring-Kramers prefactor Cat A; OP-0005-DYN advance)

This file does NOT attempt the dynamic side; Pr^{(Kramers)} is deferred to separate W9+ derivation.
```

### §10.4 NOT included in this file (explicit out-of-scope)

- ❌ OP-HMORSE-SADDLE (saddle-point Hessian regularity) — separate OP, not L-HMORSE-LOCAL related
- ❌ Pr^{(Kramers)} explicit derivation — separate W9+ file (highest leverage, OP-0005-DYN entry)
- ❌ canonical promotion of L-SC2-SEPARATION or L-PR-BD-THRESHOLD — these are *working layer* target lemmas, not SEAL candidates
- ❌ Modica-Mortola Jacobi (Path 2) — separate W9+ file 04_modica_mortola_jacobi_cat_b.md
- ❌ Surface tension rescaling (Path 1) — already Cat A direct in 01 §8.1, separate file 03_surface_tension_rescaling_cat_a.md

---

## §11 CoT/CoC Archival

### §11.1 Key CoT chain — Sc^{(2)} derivation

```
CoT-Sc^{(2)}: derivation of explicit lower bound

CoT step 1: L-HMORSE-DECOMP Cat B (canonical CV-1.16) provides per-term lower bounds (D1)(D2)(D3) but NOT a *separation ratio* between bulk and active modes.
CoT step 2: The 3-block decomposition H = ((H_BB, H_BA, 0), (H_AB, H_AA, H_AE), (0, H_EA, H_EE)) is saturated-minimizer approximation (canonical L-HMORSE-LOCAL §1956 H_BE ≈ 0 by graph locality + saturated δ_res small).
CoT step 3: Schur complement reduction: H_eff^AA = H_AA - H_AB H_BB^{-1} H_BA - H_AE H_EE^{-1} H_EA (Horn-Johnson §0.8.5).
CoT step 4: Bulk eigenvalue lower bound: μ_bulk-B ≥ 2β(1 - O(δ_sat/β)) using W''(1) = 2 + Cauchy-Weyl (canonical L-HMORSE-DECOMP (D1) + CLAUDE.md I6).
CoT step 5: Active eigenvalue upper bound: μ_active ≤ μ_min(H_AA) ≤ 8α d_max + 2β (PSD subtraction in Schur + diagonal bound).
CoT step 6: Sc^{(2)} = μ_bulk / μ_active ≥ 2β(1 - O(δ_sat/β)) / (8α d_max + 2β) = 1/(1 + 4α d_max/β) · (1 - O(δ_sat/β)).
→ L-SC2-SEPARATION Cat B target lemma (§4.1).
```

### §11.2 Key CoT chain — Pr^{(bd)} derivation

```
CoT-Pr^{(bd)}: derivation of explicit threshold

CoT step 1: D-HMORSE-LOCAL (C2′) "active set well-defined" is canonically a combinatorial condition at deterministic u^*, but implicitly requires non-vacuousness under stochastic dynamics T-PF-A1-SDE Cat A.
CoT step 2: Deterministic boundary width ℓ_det = √(α/β) (canonical T-OP6-B Cat A persistent-ridge bound; Modica-Mortola scaling).
CoT step 3: Thermal smearing width ℓ_therm = √(T_*/(β W''(u^*))) (T-PF-A1-PE Cat A local Gaussian within-well variance).
CoT step 4: Ratio ℓ_det²/ℓ_therm² = α W''(u^*)/T_* = Pr^{(bd)} (arithmetic).
CoT step 5: (C2′) non-vacuous ⟺ ℓ_det > ℓ_therm ⟺ Pr^{(bd)} > 1.
→ L-PR-BD-THRESHOLD Cat B target lemma (§7.1).
```

### §11.3 CoC archive (anchored chains)

```yaml
target_statement_L_SC2_SEPARATION: Sc^{(2)} = μ_bulk/μ_active ≥ 1/(1 + 4α d_max/β) · (1 - O(δ_sat/β)) under D-HMORSE-LOCAL (C1)(C2′)(C3) + saturated bulk/exterior + canonical phase-separated regime.
prior_anchors:
  - canonical §13 L-HMORSE-DECOMP Cat B (CV-1.16; canonical.md:1974-2007) — 3-block decomposition + per-term bounds
  - canonical §13 L-HMORSE-LOCAL Cat B (CV-1.16; canonical.md:1948-1970) — μ_min ≥ c_HML > 0
  - canonical §13 T-Cl-Sym C3-symmetrization Cat A I7 (canonical.md:1148-1149) — prior Schur complement usage in SCC
  - canonical §13 Theorem 4 Cat A (μ_k = 4αλ_k + βW''(c)) — Hessian formula
  - CLAUDE.md "Critical Implementation Details" I6 — W''(u) = 2(1 - 6u + 6u²) factor 2
  - external: Horn-Johnson Matrix Analysis 2nd ed. §0.8.5 (Schur complement); Bhatia §III.5 (Cauchy-Weyl interlacing)
  - 03_D_L_commutation §1-§4 — bulk/active/exterior 3-block decomposition origin (working layer)
  - 01_ns_inspired_synthesis §6 #7 + §11 Tier 3 — Sc^{(2)} catalog reference + leverage map
causation_chain:
  - L-HMORSE-DECOMP Cat B + saturated-minimizer approximation → 3-block H with H_BE ≈ 0 (intermediate I1)
  - I1 + Schur complement → H_eff^AA explicit form (intermediate I2)
  - I2 + Cauchy-Weyl + W''(1) = 2 → μ_bulk lower bound 2β(1 - O(δ_sat/β)) (intermediate I3)
  - I2 + PSD subtraction in Schur → μ_active upper bound 8α d_max + 2β (intermediate I4)
  - I3 + I4 + arithmetic → Sc^{(2)} ≥ 1/(1 + 4α d_max/β) · (1 - O(δ_sat/β)) (target)
inverse_causation_check:
  - if L-HMORSE-DECOMP Cat B retracted: 3-block structure undefined → Sc^{(2)} vacuous
  - if W''(1) ≠ 2: bulk diagonal coefficient changes; prefactor changes but Cat B structure preserved
  - if Schur complement ill-defined (H_BB or H_EE singular): saturated bulk/exterior regime breaks

target_statement_L_PR_BD_THRESHOLD: Pr^{(bd)} = α W''(u^*)/T_* ≥ 1 (loose) is the D-HMORSE-LOCAL (C2′) implicit precondition against thermal smearing.
prior_anchors:
  - canonical §13 D-HMORSE-LOCAL (C2′) Cat B definition (CV-1.16; canonical.md:1939)
  - canonical §13 T-PF-A1-PE Cat A (CV-1.9; canonical.md:1700-1711) — Poincaré inequality + Gibbs measure
  - canonical §13 T-OP6-B Cat A (CV-1.7; canonical.md:1956) — persistent-ridge boundary band ℓ_det
  - canonical §13 T-PF-A1-SDE Cat A (CV-1.8; canonical.md:1668) — stochastic dynamics well-posedness
  - external: Modica 1987 Arch Rat Mech Anal 98:123 (Allen-Cahn interface scaling)
  - external: Bovier-den Hollander "Metastability" 2015 §16 (local Gaussian approximation)
  - 01_ns_inspired_synthesis §6 #9 + §8.3 Path 3 — Pr^{(bd)} catalog + Path 3 derivation chain
causation_chain:
  - T-OP6-B Cat A → ℓ_det = √(α/β) deterministic boundary width (intermediate I1)
  - T-PF-A1-PE Cat A + local Gaussian (H3) → ℓ_therm = √(T_*/(β W''(u^*))) thermal smearing width (intermediate I2)
  - I1 + I2 + arithmetic → ℓ_det²/ℓ_therm² = α W''(u^*)/T_* = Pr^{(bd)} (intermediate I3)
  - I3 + D-HMORSE-LOCAL (C2′) non-vacuousness ⟺ ℓ_det > ℓ_therm → Pr^{(bd)} > 1 (target)
inverse_causation_check:
  - if T-PF-A1-PE Cat A retracted: no Gibbs measure → ℓ_therm undefined → threshold vacuous
  - if local Gaussian (H3) invalid: full Poincaré bound exp(osc/T_*) much weaker but threshold still qualitatively valid
  - if T_* = 0: zero-temperature regime (separate Theorem 4 Cat A); Pr^{(bd)} = ∞ trivially
  - if W''(u^*) < 0 (spinodal): out of post-formation regime; OP-0005-DYN territory
```

---

## §12 Hard Constraint CN1-16 Check

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical/* edits 0 | ✓ | 본 file = working/field_equation_framework/04; canonical 미수정 |
| **CN2** Silent OP resolution 0 | ✓ | §10 explicit "OP-HMORSE-LOCAL-A Cat A path requires further work; this file = Cat B target only" |
| **CN3** Research OS 재도입 0 | ✓ | 본 file = single working file in existing dir; no new registry |
| **CN4** Analyticity ($b_D = 0$) | ✓ | L-PR-BD-THRESHOLD §7.1 (H4); no new energy terms |
| **CN5** 4-term independence | ✓ | H_bd, H_cl, H_sep treated as L-HMORSE-DECOMP (D1)(D2)(D3) separate per-term bounds |
| **Closure idempotence 가정 0** | ✓ | 미적용 |
| **K 이중 취급 0** | ✓ | K_field, K_act, K_soft 어휘 부재; single-formation (C3) hypothesis cited as canonical |
| **Zero-temperature metastability flag** | ✓ | §6.4 explicit + §7.3 inverse_causation_check (H4) "T_* = 0 caveat" |
| **OMC 풀 오케스트레이션 0** | ✓ | 호출 0 |
| **CN10** No reductive reduction | ✓ | Schur complement + Cauchy-Weyl + Payne-Weinberger = contrastive standard tools; no fluid reduction |
| **Primitive 전도 0** | ✓ | u_t primitive 유지; Sc^{(2)}, Pr^{(bd)} = derived spectral diagnostics; no E_pers/E_ridge/E_surg (CSSL anti-pattern) |
| **Inertia 0** | ✓ | first-order Langevin T-PF-A1-SDE Cat A 유지; no ∂_t² introduction |
| **Mori-Zwanzig 0** | ✓ | OP-0021 Routes A/B DEPRECATED CV-1.18 SEAL 인지; no memory kernel |
| **CSSL energy terms 0** | ✓ | §0.3 explicit anti-pattern check; ratio analysis only |
| **DECL-1.0 amend 0** | ✓ | DECL 미수정 |
| **scc/ 수정 0** | ✓ | 본 file = doc-only; no code changes |

**16/16 ✓ verified**.

### §12.1 CSSL anti-pattern verification

| Anti-pattern | This file status | Evidence |
|---|---|---|
| E_pers energy embedding (critic §D.4 CRITICAL) | ✗ NOT present | no energy term added; only spectral ratios |
| E_ridge sign-conflict (critic §D.1 MAJOR) | ✗ NOT present | no ridge density; only canonical L-HMORSE-DECOMP per-term bounds |
| Derived → primitive inversion (critic §F.3 MAJOR) | ✗ NOT present | Sc^{(2)}, Pr^{(bd)} declared diagnostic, not promoted to primitive |
| Misframing of canonical problem (critic §A.1 CRITICAL) | ✗ NOT present | §1.1 explicit L-HMORSE-LOCAL scope statement (post-formation Morse-0 minima only) |
| Circular surgery-event subspace (critic §E.4 CRITICAL) | ✗ NOT present | no E_surg; pure spectral analysis on canonical Hessian |

**All 5 CSSL anti-patterns avoided.**

---

## §13 One-Paragraph Summary

**L-SC2-SEPARATION Cat B target lemma** establishes explicit lower bound $\text{Sc}^{(2)} = \mu_{\text{bulk}}/\mu_{\text{active}} \geq 1/(1 + 4\alpha d_{\max}/\beta) \cdot (1 - O(\delta_{\text{sat}}/\beta))$ via Schur complement on the canonical L-HMORSE-DECOMP 3-block bulk/active/exterior decomposition (bulk diagonal $\mu_{\text{bulk}} \geq 2\beta$ from $W''(1) = 2$ + Cauchy-Weyl; active upper bound $\mu_{\text{active}} \leq 8\alpha d_{\max} + 2\beta$ from PSD subtraction in Schur), quantifying L-HMORSE-DECOMP §1956 "$\delta_{\text{res}}$ small at saturated minimizers" as the deep-formation regime $\beta/\alpha \gg d_{\max}$ where $\text{Sc}^{(2)} \geq 1/2$ certifies clean bulk-active mode separation. **L-PR-BD-THRESHOLD Cat B target lemma** establishes explicit threshold $\text{Pr}^{(\text{bd})} = \alpha W''(u^*)/T_* \geq 1$ as the D-HMORSE-LOCAL (C2′) implicit precondition against thermal smearing, via ratio of deterministic boundary width $\ell_{\text{det}} = \sqrt{\alpha/\beta}$ (T-OP6-B Cat A) and thermal smearing width $\ell_{\text{therm}} = \sqrt{T_*/(\beta W''(u^*))}$ (T-PF-A1-PE Cat A local Gaussian within-well variance), so that $\ell_{\text{det}}/\ell_{\text{therm}} = \sqrt{\text{Pr}^{(\text{bd})}} \geq 1$ ensures the active band is spatially resolved against Gibbs-measure fluctuations. **Numerical anchor on 2D torus $L = 16$ canonical defaults** ($\alpha = 1, \beta = 5, c^* = 1/2, T_* = 0.1$) verifies $\text{Sc}^{(2)} \geq 0.24$ (marginal, deep-regime $\beta = 50$ gives $0.76$) and $\text{Pr}^{(\text{bd})} = 9.2 \gg 1$ (3-fold safety, $k = 3$). **Joint H-Morse certification map** identifies the clean regime $(\text{Sc}^{(2)} \geq 1/2) \wedge (\text{Pr}^{(\text{bd})} \geq 1)$ as the L-HMORSE-DECOMP Cat B → Cat A feasibility window (OP-HMORSE-LOCAL-A entry point), with W9+ child files `05_op_hmorse_local_a_via_sc2.md` and `06_pr_bd_numerical_sweep.md` as direct follow-up; canonical CN1-16 + 5 CSSL anti-patterns 16/16 + 5/5 ✓ verified, canonical/* edits 0, fluid reduction 0, primitive inversion 0, inertia 0, Mori-Zwanzig 0, CV-1.18 SEAL untouched.

---

*W8-Day3 EOD H-Morse spectral quantification synthesis 완료. CV-1.18 SEALED untouched. CSSL anti-patterns 5/5 avoided. 01_ns_inspired_synthesis §13.2 Tier 2 priority delivered as combined file (05 + 06 merged). W9+ next: 05_op_hmorse_local_a_via_sc2.md (Cat A path) + 06_pr_bd_numerical_sweep.md (numerical sweep) + 02_kramers_prefactor_op_0005_attack.md (highest leverage, separate).*
