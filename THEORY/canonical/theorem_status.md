---
id: META-0103
type: registry/theorems
status: accepted
last_updated: 2026-05-02
---

# Theorem Registry

**Purpose:** Register all claims (C-xxxx), proofs (P-xxxx), and canonical theorems (T-xxxx, CV-x.y). This is the authoritative index of what has been proved.

**Structure:** Rows are organized by canonical version (CV-1.0 .. CV-1.5.2; current = **CV-1.5.2**) then status (active, challenged, deprecated). *(Updated 2026-05-02 after T-L1-F canonical promotion to CV-1.5.2.)*

---

## Canonical Theorems (Accepted into Canonical Spec)

### Canonical Spec v1.5.2 (2026-05-02) — Current Version (W6: L1-F Hard-Bar / Active-Count Bridge Conditional Cat-A)

**Additions over v1.5.1** (W6, 2026-05-02):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-L1-F** | Hard-Bar / Active-Count Bridge under L1-J Regime | accepted | A (conditional under L1-J package) | C-0721 | P-0721 | (theoretical via L1-A..L1-L chain; numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$; L1-H2 stress tests 5/5; L1-J PO-1 decay-to-cut 6/6; L1-K external audit passed) | Conditional theorem on finite shared-pool multi-formation states under hypothesis package $(P0)$–$(P11)$: $K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)=K_{\mathrm{act}}^{\varepsilon}(\mathbf u)$ AND labeled bijection $\mathcal A_{\mathrm{bar}}:A^\varepsilon\to\mathrm{Bars}_0^{\mathrm{term}}(U;G)$ via primary representative $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$. NOT a global identity; explicit hypothesis package required. P7 decay-to-cut adopted as safe technical regime hypothesis; L1-L provides Combes-Thomas / discrete Agmon backing under strong stationarity (P7_DERIVED_UNDER_STRONG_STATIONARITY) but P7 is not asserted for all SCC states. Does NOT solve OP-0005 (K-Selection) or OP-0008 ($\sigma^A$ K-jump non-determinism). Does NOT establish $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}$ (additionally requires $\phi\in\Phi_{\mathrm{res}}$ per WQ-LAT-1.B). Does NOT claim $\sigma_{\mathrm{rich}}$ sufficiency. Reservoir theory not promoted to canonical. |

**v1.5.1 → v1.5.2 release notes (2026-05-02)**:

- **Added (1 new C-ID)**: 1 Cat A conditional (T-L1-F) synthesizing the L1-A..L1-L chain.
- **Hypothesis package (P0)–(P11)**:
  - P0 terminal-death $H_0$ superlevel persistence convention (code-aligned with `scc.diagnostics._persistence_h0_graph`);
  - P1 deterministic tie convention (fixed total order $\prec$ on $X$; ties in descending-$U$ broken by ascending $\prec$);
  - P2 active mass + connected $\delta$-support;
  - P3 disjoint active neighborhoods $N_j^r\cap N_k^r=\emptyset$;
  - P4 low boundary collar $\max_{\partial N_j^r}U\le b_j-\ell_{\min}-r_{\mathrm{assoc}}$;
  - P5 background suppression $\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}$ (on $U$, not just on $R_{\mathrm{inact}}$);
  - P6 birth height $b_j\ge h_{\min}\ge\ell_{\min}$;
  - P7 decay-to-cut (heterogeneous form): $u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta))$ and $H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}$;
  - P8 tightened H6 on $G_j^r$: $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$;
  - P9 NE-2 perturbation $\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2$;
  - P10 inactive residual suppression $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$;
  - P11 margin ledger $h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}$.
- **L1 chain provenance**: L1-A merge / death / contact level; L1-B cut bound; L1-C slot-to-bar + terminal-death convention; L1-D no-extra-bar / secondary-bar suppression; L1-E inactive suppression; L1-F synthesis; L1-G empirical diagnostic; L1-H local-to-global transfer; L1-H2 boundary-leakage proof (Lemma 1: $\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}$ from graph inclusion); L1-I constants feasibility (439/1920 FEASIBLE_WITH_BUDGET); L1-J Cat-A attempt; L1-K external audit (THEOREM_CANDIDATE_STRONG_AUDIT_PASSED); L1-K-REPAIR (4 proof-hygiene repairs R-1, R-2, R-3, R-4 applied); L1-L P7 status decision.
- **Counts**: 45A → **46A** (+1 conditional Cat A), 60 → **61 claims**, 75% → **75% fully proved** (unchanged %).
- **Non-claims preserved**: no global $K_{\mathrm{bar}}=K_{\mathrm{act}}$; no global $K_{\mathrm{soft}}=K_{\mathrm{act}}$; no OP-0005 or OP-0008 solution; no $\sigma_{\mathrm{rich}}$ sufficiency; reservoir theory not promoted to canonical; P7 not generally derived from all SCC states; no application / vision / robotics claims.
- **Source**: `THEORY/working/MF/kbar_kact_bridge_L1A..L1L_*.md` (full L1 chain — 13 working documents); `CODE/scripts/l1g_l1hyp_diagnostic.py`, `l1h_local_to_global_counterexample.py`, `l1h2_boundary_leakage_counterexample.py`, `l1i_constants_feasibility.py`, `l1j_bridge_cut_decay_diagnostic.py` (5 diagnostic / counterexample scripts); `CODE/scripts/results/l1*.json`.
- **canonical.md growth**: ~25 lines added in §13 Category A (T-L1-F entry).

### Canonical Spec v1.5.1 (2026-04-29) — Previous Version (W5 Day 3 EOD: D-6a Multi-Static + Ontological Depth + Critic 보강)

**Additions over v1.5** (W5 Day 3 EOD, 2026-04-29):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-Commitment-14-Multi-Static** | Multi-Formation σ-Signature on K-field (Static) | accepted | A definitional | C-0717 | P-0717 | (theoretical extension of Commitment 14) | Defined on $\widetilde{\Sigma}^{K_{\mathrm{field}},\circ}_M$ interior (Option A pragmatic; corners deferred to NQ-248 W7+). $\sigma_{\mathrm{multi}} = (\sigma^A, \sigma^D)$ joint invariant under wreath-product $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ |
| **T-σ-multi-A-Static** | Within-Formation σ-Tuple Multi-Set Invariance | accepted | A (well-separated regime) | C-0718 | P-0718 | (theoretical via Coupling Bound Lemma + T-σ-Lemma-1) | Multi-set $\{\sigma_j\}_{j=1}^{K_{\mathrm{act}}}$ under $S_{K_{\mathrm{act}}}$ permutation; reduces to Commitment 14 σ at $K_{\mathrm{act}}=1$. Cat B target in T-Persist-K-Weak overlap regime |
| **T-σ-multi-D-Static** | Between-Formation Cohomology Pull-Back | accepted | A definitional | C-0719 | P-0719 | (wreath-product representation theory, Specht 1935 + James-Kerber 1981) | Conjugacy-class label in $H^1(\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}; \mathrm{Stab}(\mathbf{u}^*))$. Explicit cohomology computation (D_4 × S_2 etc.) Cat B target via NQ-242d W6+ |
| **T-σ-Multi-1** | Multi-Formation Goldstone-Pair Instability (Phase 4 Static) | tentative | B target | C-0720 | (sketch) | (Phase 4 D-6a numerical, Phase 6 Q1 box-clipping) | Goldstone-pair separation $\Delta\lambda \approx O(\lambda_{\mathrm{rep}} e^{-c_0 D_{\mathrm{sep}}})$ under V5b-T per-formation regime. Static instability iff $\lambda_{\mathrm{rep}} > c_{\mathrm{eff}} \mu_{\mathrm{Gold}}^{\mathrm{single}}$. Cat A pending NQ-242 numerical anchor |

**Sub-statement additions to T-V5b-T**:

| Sub-ID | Name | Status | Category | Notes |
|--------|------|--------|----------|-------|
| **(V5b-F-empirical)** | V5b-F Goldstone Mass Scaling | accepted | B target | $\mu_{\mathrm{Gold}}^{\mathrm{V5b-F}} \approx C(\beta) \cdot \|\partial S\|/n$, $C(\beta=4, \xi_0=0.5) \approx 13.2 \pm 0.4$ (NQ-198a 6 corner-sat, SNR 35). Refutes Phase 3 heuristic + Day 3 §4 derivation. Full $C(\beta, \xi_0)$ open via NQ-198k W6+ |
| **(V5b-T-zero)** | Sub-Spinodal Translation-Invariant Regime | accepted | A definitional | $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T-zero}} = 0$ exactly (discrete translation orbit on $\mathbb{Z}_L^d$). Replaces V5b-T' WITHDRAWN. Empirical anchor NQ-198f $T^2_{20}/T^2_{28}$ $|\mu| \leq 0.028$ within FD numerical noise |

**Status changes to existing entries**:

| C-ID | Name | Old Status | New Status | Reason |
|------|------|-----------|-----------|--------|
| **C-0716** | T-σ-Theorem-4 σ at First Pitchfork | Cat A in $\epsilon$-small regime | **Cat B in $\epsilon$-small regime** | Retroactive Critic 7-agent verdict 2026-04-29: Errata Round 1 caught structural error in original (ii) ("would-be transverse Goldstone" inapplicable to discrete sym breaking); original Cat A merge had unresolved Morse-index contradiction. Higher-order $\epsilon$ splitting NQ-187 W7+ may re-promote. |
| **D-5 (V5b-T' new entry candidate)** | V5b-T' Pre-Objective Goldstone (Phase 3 proposal) | Cat B target proposal | **WITHDRAWN** | NQ-198f phantom on torus (μ ≈ 0 exact, not PN-barrier-lifted O(β)). Replaced by V5b-T-zero sub-statement. |

**v1.5 → v1.5.1 release notes (2026-04-29)**:

- **Added (4 new C-IDs)**: 3 Cat A definitional (Multi-Static + multi-A-Static + multi-D-Static) + 1 Cat B target (Multi-1).
- **Added (sub-statements)**: V5b-T-zero (Cat A def, replaces V5b-T' phantom) + V5b-F-empirical (Cat B target) within T-V5b-T entry.
- **Status revision**: T-σ-Theorem-4 Cat A → Cat B retroactive (Critic 보강).
- **Withdrawn**: D-5 V5b-T' new entry candidate (NQ-198f phantom finding).
- **Counts**: 43A → **45A** (net +2: +3 D-6a Cat A − 1 Theorem-4 격하), 4B → **5B** (+1 Theorem-4 + 1 Multi-1 vs −1 hypothetical), 57 → **60 claims**, 75% → **75% fully proved** (unchanged % due to balanced category shift).
- **Commitment 16 K-status** added to §11.1 (K_field architectural cap / K_act dynamic stratum index two-tier decomposition; resolves 4-month K ontological ambiguity per OP-0009).
- **Commitment 14 (O5')(O7) sub-conventions** added (multi-irrep ordering + tie-breaking via Mulliken character order).
- **CN6 refined** (line 1603): "K kinetically determined" now refers specifically to K_act per Commitment 16.
- **Open problems**: OP-0008 σ^A K-jump non-determinism + OP-0009 Multi-Formation Ontological Foundations registered; OP-0003 MO-1 re-activation rider added.
- **canonical.md growth**: 1593 → 1664 lines (~71 lines added).
- **Source**: `THEORY/logs/daily/2026-04-29/04..11_*` (Day 3 deepening + numerical + 7-agent + 4-agent ontological depth analysis); `THEORY/working/MF/K_status_commitment.md` (OAT-1 Commitment 16 audit); `THEORY/CHANGELOG.md` 2026-04-29 entry.

### Canonical Spec v1.5 (2026-04-27) — Previous Version (W5 Day 1: σ-Framework Supporting Structures)

**Additions over v1.4** (W5 Day 1 G0, 2026-04-27):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-σ-Lemma-1** | σ-Framework Irrep Decomposition Well-Defined | accepted | A | C-0712 | P-0712 | (theoretical, finite-group rep theory) | Hessian commutes with $G_u$-action; isotypic decomposition via Maschke + Schur; finite-graph hypothesis essential; trivial-stabilizer case vacuous |
| **T-σ-Lemma-2** | σ-Framework Nodal Count Properties | accepted | A (i,ii,iii,iv) + C (v,vi conditional) | C-0713 | P-0713 | (theoretical + W4-04-25 NQ-141 32×32 numerical) | Graph-intrinsic + Aut(G)-equivariance + lower bound $\geq 2$ + sign-flip Cat A; Courant upper bound + $G_u$-orbit divisibility Cat C |
| **T-σ-Lemma-3** | Goldstone–ℓ=1 Angular Saturation | accepted | A (continuum) | C-0714 | P-0714 | W4-04-26 NQ-170c 2D torus L=20 ζ=0.5 (overlap 0.97) | IBP identity $\mathcal{P}_{\ell=1}[\delta u_x] = (-c_d \int u^*(r)\, dr, 0)$ *(corrected per canonical.md Errata Round 1, 2026-04-27 evening; original brief stated $(-m, 0)$ which was a Jacobian error)*; Goldstone basis automatically ℓ=1; nodal count = 2 universal (anchors T-V5b-T-(e)) |
| **T-σ-Theorem-3** | σ at Uniform on $D_4$ Free-BC Grid (Closed Form) | accepted | A | C-0715 | P-0715 | exp_hessian_uniform_v2 (NQ-141 W4-04-25, $L = 4$ to $32$, $< 10^{-9}$ precision) | $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$; full $D_4$ irrep table on cosine basis; $\mathcal{N}(\phi_{(p,q)}) = (p+1)(q+1)$. *(Erratum 2026-04-27 Round 1: §13 worked example originally listed irrep label A_1 for the $(1,1)$ singlet; corrected to B_2.)* |
| **T-σ-Theorem-4** | σ at First Pitchfork on $D_4$ Free-BC Grid (Leading Order, **continuum-limit claim**) | Cat A at CV-1.5; **Cat A → Cat B retroactive at CV-1.5.1 (2026-04-29)** per Critic 7-agent verdict (Errata Round 1 Morse-index inconsistency at merge time). **Continuum vs discrete grid caveat added 2026-05-04 W6 NQ-187 audit** (canonical.md §13 T-σ-Theorem-4 entry now contains explicit continuum-vs-discrete note): canonical statement (ii) — leading-order degeneracy $\mu_0 = \mu_1 = 4\|W''(c)\|\epsilon$ from $A_2/A_1 = 4$ — is a continuum-limit prediction (R22 §3.3 Lebesgue integral on unit square) **not realized on finite discrete grids** $L \le 16$. NQ-187 numerical (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`, script `CODE/scripts/test_sigma_theorem4_scaling.py`, $L \in \{4, 8, 16\}$, $\epsilon \in \{0.001..0.1\}$, analytic sparse $\Sigma_m$-Hessian + shift-invert Lanczos): measured $\mu_0/\epsilon \approx 1$, $\mu_1/\epsilon \approx 2$, ratio $\mu_1/\mu_0 \approx 2$ (not $1$ degeneracy) and exponent $p \approx 1.03$ (not $p = 2$ predicted, not $p = 3/2$ alternative). Three reconciliation hypotheses (α continuum extrapolation $L \to \infty$, β R22 derivation re-audit, γ $\Sigma_m$-Hessian convention) under audit. Cat A re-promotion deferred to CV-1.7+ post-γ/β/α path closure. | B (was A in $\epsilon$-small regime at CV-1.5) | C-0716 | P-0716 | (theoretical via T-Birth-Parametric + R22 axis-aligned, continuum-limit; numerical NQ-187 on discrete grid) | $D_4 \to \mathbb{Z}_2$ symmetry breaking; continuum prediction Mode 0 trivial irrep / Mode 1 sign irrep both with eigenvalue $4\|W''(c)\|\epsilon$ (degenerate at continuum leading order); on discrete $L \le 16$ grid measured $\mu_1/\mu_0 \approx 2$ and effective coefficient $\approx 1$ (not $4$). $\mathcal{F}$ tie-break NQ-143/NQ-184. Statement now read as **continuum-limit claim** until γ/β/α audit closes. |

**v1.4 → v1.5 release notes (2026-04-27)**:
- Added: 5 Cat A entries (T-σ-Lemma-1 + T-σ-Lemma-2 + T-σ-Lemma-3 + T-σ-Theorem-3 + T-σ-Theorem-4) — σ-framework supporting structures grounding Commitment 14.
- Decision: Option α (5 separate entries) per W5 strategic plan §0.4 Decision 1 default; rationale "mathematically independent statements deserve individual canonical visibility".
- Counts: 38A → **43A**, 52 claims → **57 claims**, 73% → **75% fully proved**.
- T classification update: T1 = 3 → **8** (Lemma 1, 2, 3, Theorem 3, 4 each individually T1 per Option α). T2 reduced (σ supporting structures moved out of T2).
- Sub-statement caveats canonically registered: T-σ-Lemma-2 internal Cat A/C split (sub-statements (v) Courant + (vi) orbit divisibility are Cat C riders within the Cat A entry); T-σ-Theorem-4 explicit "in $\epsilon$-small regime" qualifier; T-σ-Lemma-3 explicit "in continuum limit" qualifier.
- Pre-brainstorm corrections folded in: Lemma 1 finite-graph hypothesis explicit; Lemma 2 sub-statement (iii) reframed as lower-bound-from-$\mathbf{1}^\perp$ (was incorrectly stated as "$n_k = 1$ iff constant" in plan templates); Lemma 3 IBP interpretation B (δu^ref = unit vector in ℓ=1 angular subspace) adopted.
- σ-framework now fully canonical-grounded: definitional Commitment 14 + irrep apparatus (T-σ-Lemma-1) + nodal count (T-σ-Lemma-2) + Goldstone–ℓ=1 saturation (T-σ-Lemma-3) + worked examples on uniform (T-σ-Theorem-3) and post-bifurcation (T-σ-Theorem-4) configurations.
- **Source:** `THEORY/logs/daily/2026-04-27/01_sigma_lemmas_review.md` (decision packet) + `01a-01e` (per-statement files); `THEORY/canonical/canonical.md` §13 (T-σ-Lemma-1 ~ T-σ-Theorem-4 entries inserted after T-V5b-T at lines 1169-1283); `THEORY/CHANGELOG.md` 2026-04-27 entry.

### Canonical Spec v1.4 (2026-04-26) — Previous Version (W4 Extended Close)

**Additions over v1.3** (W4 extended close, 2026-04-26):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-V5b-T** | Pre-Objective Goldstone on Translation-Invariant Graphs | accepted | A | C-0710 | P-0710 | E-0095 (NQ-170b ζ-scan) + E-0096 (NQ-170c graph-class extension + nodal count) + E-0097 (NQ-172 reproducibility) | Sub/super-lattice dichotomy on translation-invariant graphs (torus T^d, cycle C_n); 2D 2-fold doublet with commensurability split; 1D 1-fold Goldstone; ζ_*(G) graph-class dependent; Goldstone nodal count = 2 universal |

**v1.3 → v1.4 release notes (2026-04-26)**:
- Added: 1 Cat A theorem (T-V5b-T) — V5b verification cycle (8 iterations) result.
- Counts: 37A → **38A**, 51 claims → **52 claims**, 73% → **73% fully proved**.
- T classification update (W4 weekly_summary §3): T1 = 2 → **3** (added V5b-T); T2 = 5 → 4 (V5b moved to T1); T3 = 3 → **4** (added V5b-F new finding).
- New finding registered: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — Cat C, NQ-173 carry.
- Reproducibility crisis identified+resolved: NQ-172 (mode-indexing artifact in NQ-170 analysis script).
- W4 scope extended: 2026-04-19 ~ **2026-04-26** (8 days). Per user direction "아직 내용은 전부 W4로 간주해" — 04-26 work is W4 final-day continuation.

### Canonical Spec v1.3 (2026-04-25) — Previous Version (Frozen)

**Additions over v1.2** (W4 merge, 2026-04-19 ~ 2026-04-25):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-PreObj-1** | Pre-Objective Multi-Peak Formation Mechanism | accepted | A | C-0700 | P-0700 | E-0090 (L=12 numerical, 3-digit agreement) + E-0091 (L=32 dichotomy) | F=1 single-disk minimizer non-critical under full SCC; gradient flow attracts to multi-peak F≥2; IC-protocol dichotomy (adaptive bounded vs random ~ L^2.8) |
| **T-PreObj-1G** | Pre-Objective Mechanism Graph-Class Independent | accepted | A | C-0701 | P-0701 | (theoretical, qualitative empirical) | Conclusions (i),(ii) of T-PreObj-1 hold on **any finite connected graph** under (G1)–(G4) hypotheses |
| **Lemma 4** | Quadratic Form Positive Definite (M matrix) | accepted | A | C-0702 | P-0702 | E-0090 | M ∈ R^{2x2} of (g_cl, g_sep) gradients, PD under linear independence; destabilization magnitude Lambda^T M Lambda > 0 |
| **F-1 Resolution Corollary** | F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 | accepted | A | (corollary) | (corollary) | — | Pure E_bd portion via T-Merge(b); full SCC portion via T-PreObj-1 (i); see open_problems.md OP-0001 |

**v1.2 → v1.3 release notes (2026-04-25):**
- Added: 2 Cat A theorems (T-PreObj-1, T-PreObj-1G), 1 Cat A lemma (Lemma 4), 1 Cat A corollary (F-1 split-resolution).
- Status changes: C-0550 (F-1), C-0551 (M-1), C-0552 (MO-1) — challenged → resolved/clarified/sidestepped (see Active Claims table below).
- Counts: 35A → **37A**, 49 claims → **51 claims**, 71% → **73% fully proved**.
- Critical blockers: 3 (F-1, M-1, MO-1) → **0** (all resolved/clarified/sidestepped).
- Pending W4 merge (user decision required, deferred): T2 candidates including σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1, CN15/16/17, Commitment 14/15 v2.

### Canonical Spec v1.2 (2026-04-12) — Previous Version (Frozen)

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-1** | Existence of Minimizers | accepted | A | C-0001 | P-0001 | E-0001, E-0002 | SCC minimizer always exists on Σ_m |
| **T-3** | Stability of Interior Minimizers | accepted | A | C-0003 | P-0003 | E-0003 | Hessian positive on interior; local stability |
| **T-6a** | Closure Fixed Point (Existence) | accepted | A | C-0006a | P-0006a | E-0005 | u* = Cl_t(u*) ∃ for all parameters |
| **T-6b** | Closure Fixed Point (Stability) | accepted | A | C-0006b | P-0006b | E-0006 | Closure FP is attracting in stability metric |
| **T-6-Stability** | Stability of Closure FP | accepted | A | C-0006c | P-0006c | E-0007 | Full spectral analysis |
| **T-7** | Enhanced Metastability | accepted | A | C-0007 | P-0007 | E-0008, E-0009 | Residence time > expected near saddle |
| **T-8-Core** | Phase Transition (Core Dominance) | accepted | A | C-0008 | P-0008 | E-0010, E-0011 | Binuclear → mononuclear at critical β |
| **T-8-Full** | Phase Transition (Global) | accepted | A | C-0009 | P-0009 | E-0012, E-0013 | Full energy landscape bifurcation |
| **T-11** | Γ-Convergence | accepted | A | C-0011 | P-0011 | E-0014 | Variational convergence under scaling |
| **T-14** | Gradient Flow | accepted | A | C-0014 | P-0014 | E-0020:E-0022 | Gradient descent converges to minimizer |
| **T-20** | Axiom Consistency | accepted | A | C-0020 | P-0020 | E-0025 | Axioms A1–E mutually consistent |
| **C-Axioms** | Cohomology-Resolvent Alignment | accepted | A | C-0101 | P-0101 | E-0030:E-0032 | C3'' symmetrization complete (upgraded 04-03) |
| **QM-1** | Quantum Mechanical Analogy (Eigenvalue) | accepted | A | C-0110 | P-0110 | E-0040 | Fiedler eigenvalue is binding edge |
| **QM-2** | QM-2 (Spectral Gap) | accepted | A | C-0111 | P-0111 | E-0041 | Spectral gap related to phase transition |
| **QM-3** | QM-3 (Perturbation) | accepted | A | C-0112 | P-0112 | E-0042 | Perturbations stay confined |
| **QM-4** | QM-4 (Commutation) | accepted | A | C-0113 | P-0113 | E-0043 | Operator commutation holds generically |
| **T-Bind-Proj** | Tangential Residual Bound at Constrained Minimizers | accepted | A (for all τ_cl ∈ (0,1)) | C-0200 | P-0200 | E-0050:E-0052 | Phase 13 upgrade applied 2026-04-07 (Erratum, see canonical.md §13 line 1440 and Cat B section erratum line 1481): T-Bind-Proj/Full moved to Category A. Bound: $\|r_T\|_2 \le (\lambda_{\mathrm{sep}} G_{\mathrm{sep}} + \lambda_{\mathrm{bd}} G_{\mathrm{bd}}) / (2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)) + (1+a_{\mathrm{cl}}/4)\sqrt{n}\,\bar r_0/(1-a_{\mathrm{cl}}/4)$. Proof: KKT projection + Banach inversion of restricted operator with $\sigma_{\min} \ge 1-a_{\mathrm{cl}}/4$; general τ via binary mass-balance formula $\Phi(\tau; a_{\mathrm{cl}}, c)$. *(Brief corrected 2026-05-04 W6 G2 audit; previously listed Cat B with τ=1/2 restriction, which contradicted canonical and was the result of the Phase 13 upgrade not being propagated to this index.)* |
| **T-Bind-Full** | Bind Lower Bound at Constrained Minimizers | accepted | A | C-0201 | P-0201 | E-0053 | Phase 13 upgrade applied 2026-04-07 (Erratum, see canonical.md §13 line 1445 and Cat B section erratum line 1481): T-Bind-Full moved to Category A. Statement: $\mathsf{Bind}(\hat u) \ge 1 - f(\text{params})$, $n$-independent when parameters are $O(1)$. Proof: follows from T-Bind-Proj + universal gradient bounds. *(Brief corrected 2026-05-04 W6 G2 audit; previously listed Cat C "very conditional, full τ dependence unclear", which contradicted canonical.)* |
| **Predicate-Energy Bridge** | Energy ↔ Diagnostic Alignment | accepted | A | C-0300 | P-0300 | E-0060:E-0063 | Energy minimization ↔ diagonal optimization (upgraded 04-03) |
| **Deep Core Dom. 2b** | Deep Core Dominance | accepted | A | C-0301 | P-0301 | E-0064, E-0065 | Core is always dominant in asymmetric regime (upgraded 04-03) |
| **T-Persist-1(a)** | Transport Persistence (base) | accepted | C | C-0400 | P-0400 | E-0070 | Conditional: assumes generic parameters |
| **T-Persist-1(b)** | Transport Persistence (basin unconditional) | accepted | A | C-0401 | P-0401 | E-0071, E-0072 | Unconditional: genericity automatic (upgraded 04-03) |
| **T-Persist-1(d)** | Transport Persistence (fixed stratum) | accepted | C | C-0402 | P-0402 | E-0073 | Conditional: on fixed active stratum |
| **T-Persist-1(e)** | Transport Persistence (confinement) | accepted | A | C-0403 | P-0403 | E-0074 | Tight confinement bound (upgraded 04-03) |
| **T-Persist-Full** | Transport Persistence (full composition) | accepted | C | C-0404 | P-0404 | E-0075 | Conditional on multiple regime conditions |
| **T-Persist-K-Sep** | K-field Persistence (well-separated) | accepted | B | C-0500 | P-0500 | E-0076, E-0077 | Conditional: on well-separated regime + per-formation persist |
| **T-Persist-K-Weak** | K-field Persistence (weak coupling) | accepted | C | C-0501 | P-0501 | E-0078 | Conditional: on weakly-interacting regime |
| **T-Persist-K-Unified** | K-field Persistence (parametric) | accepted | B | C-0502 | P-0502 | E-0046, E-0047 | Parametric family (Sep/Weak/Strong); 100% validation (new v1.2) |

---

## Active Claims (Not Yet Canonical) / Resolved Claims

| C-ID | Name | Status | Category (Intended) | Proof (P-ID) | Experiments | Notes |
|------|------|--------|---------|----------|-------------|-------|
| **C-0550** | F-1: K=2 Vacuity Problem | ✅ **SPLIT-RESOLVED (2026-04-24)** | A | P-0700 + T-Merge(b) | E-0090, E-0091 | Pure E_bd portion: T-Merge(b) Cat A pre-existing. Full SCC portion: T-PreObj-1 (i) Cat A. See open_problems.md OP-0001. |
| **C-0551** | M-1: K=1 Always Preferred | ✅ **LAYER-CLARIFIED (2026-04-24)** | A | T-Merge(b) | none | Proved theorem (T-Merge(b)) misframed as problem. Pure E_bd: theorem holds. Full SCC: comparison not framed (Theorem 2 makes F=1 non-critical). |
| **C-0552** | MO-1: Morse Theory Invalid | ⚪ **SIDESTEPPED (2026-04-24)** | A (single-formation) | (sidestep) | none | Single-formation σ-framework operates on Σ_m (no corners). Multi-formation extension to Σ^K_M still open (Phase 5). |
| **C-0553** | Type A/B Classification | challenged | OP | exp65 | E-0065 | exp65 invalidates; Type B never observed (unchanged from v1.2). |
| **C-0600** | K-field Model Selection | tentative (partially addressed) | pending | none | exp66:exp73 | W4 σ-framework + Static/Dynamic Separation (CN15 candidate) provides partial answer; full mechanism still open. |
| **C-0700** | T-PreObj-1 Pre-Objective Mechanism | ✅ **accepted Cat A** | A | P-0700 | E-0090, E-0091 | New 2026-04-24. F=1 disk non-criticality + multi-peak attractor + IC-protocol dichotomy. |
| **C-0701** | T-PreObj-1G Graph-Class Independent | ✅ **accepted Cat A** | A | P-0701 | (theoretical) | New 2026-04-24. Conclusions (i),(ii) hold on any finite connected graph under (G1)–(G4). |
| **C-0702** | Lemma 4 Quadratic Form PD | ✅ **accepted Cat A** | A | P-0702 | E-0090 | New 2026-04-24. M positive definite under g_cl, g_sep linear independence. |
| **C-0710** | T-V5b-T Pre-Objective Goldstone on Translation-Invariant Graphs | ✅ **accepted Cat A** | A | P-0710 | E-0095, E-0096, E-0097 | New 2026-04-26 (W4 extended). Sub/super-lattice spectral dichotomy on torus T^d / cycle C_n; 2D commensurability split; 1D Goldstone; nodal count = 2 universal. After 8 V5b iterations (V1 → V5b''). |
| **C-0711** | V5b-F Partial Goldstone on Boundary-Modified Graphs | tentative | C | P-0711 | E-0096 (free BC partial) | New 2026-04-26 (W4 extended). Cat C new finding. NQ-173 quantification carry. |
| **C-0712** | T-σ-Lemma-1 σ-Framework Irrep Decomposition Well-Defined | ✅ **accepted Cat A** | A | P-0712 | (theoretical, Maschke + Schur orthogonality) | New 2026-04-27 (W5 Day 1 G0). Hessian-$G_u$ commutation + canonical isotypic projector. Finite-graph hypothesis essential. |
| **C-0713** | T-σ-Lemma-2 σ-Framework Nodal Count Properties | ✅ **accepted Cat A** (i,ii,iii,iv) + Cat C riders (v,vi) | A/C-split | P-0713 | NQ-141 (W4-04-25 R23 32×32 empirical) | New 2026-04-27 (W5 Day 1 G0). Lower bound $\mathcal{N} \geq 2$ corrected from "constant" template; orbit divisibility restricted to non-invariant case. |
| **C-0714** | T-σ-Lemma-3 Goldstone–ℓ=1 Angular Saturation | accepted Cat A in continuum | A | P-0714 | NQ-170c (W4-04-26 2D torus ζ=0.5 overlap 0.97) | New 2026-04-27 (W5 Day 1 G0). IBP saturation identity $\mathcal{P}_{\ell=1}[\delta u_x] = (-c_d \int u^*(r)\, dr, 0)$ *(Erratum 2026-04-27 Round 1: original brief stated $(-m, 0)$ which was a Jacobian error)*. Anchors T-V5b-T-(e) Goldstone nodal=2 universal. |
| **C-0715** | T-σ-Theorem-3 σ at Uniform on $D_4$ Grid (Closed Form) | accepted Cat A | A | P-0715 | exp_hessian_uniform_v2 (NQ-141, $L = 4$ to $32$, $< 10^{-9}$ precision) | New 2026-04-27 (W5 Day 1 G0). $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ closed form. *(Erratum 2026-04-27 Round 1: §13 worked example originally listed irrep label A_1 for the $(1,1)$ singlet; corrected to B_2.)* |
| **C-0716** | T-σ-Theorem-4 σ at First Pitchfork (Leading Order, continuum-limit claim) | Cat A → Cat B retroactive (CV-1.5.1, 2026-04-29) per Critic 7-agent verdict + Errata Round 1 (Morse-index inconsistency at original merge time). **Continuum vs discrete grid caveat added 2026-05-04 W6 NQ-187 audit:** canonical statement (ii) is now explicitly a continuum-limit claim; NQ-187 measured $\mu_1/\mu_0 \approx 2$ and effective $A_2/A_1 \approx 2$ on discrete $L \le 16$ free-BC grids (continuum prediction is degeneracy with $A_2/A_1 = 4$). Cat A re-promotion deferred to CV-1.7+ post-γ/β/α path closure. | B (was A) | P-0716 | (theoretical via T-Birth-Parametric + R22 axis-aligned, continuum-limit; numerical NQ-187 on discrete grid) | New 2026-04-27 (W5 Day 1 G0); retroactively downgraded 2026-04-29; continuum-vs-discrete caveat added 2026-05-04. $D_4 \to \mathbb{Z}_2$ symmetry breaking. Continuum-limit Mode 0 = Mode 1 = $4\|W''(c)\|\epsilon$ degenerate; discrete-grid measured $\mu_1/\mu_0 \approx 2$. $\mathcal{F}$ tie-break NQ-143/NQ-184. |

---

## Counterexamples & Challenges (X-xxxx)

| X-ID | Refutes | Status | Description | Impact |
|------|---------|--------|-------------|--------|
| **X-0001** | ~~C-0550 (F-1 Validity)~~ — **superseded 2026-04-24** | superseded | Originally: K=2 energy 4.66 vs K=1 energy 2.25. **W4 reframing**: this evidence is the *correct* T-Merge(b) statement, not a refutation. F-1 was misframed as problem. | F-1 SPLIT-RESOLVED via Option D (premise dissolution); see C-0550 entry. |
| **X-0002** | Type A/B Classification | validated | exp65: all configs Type A (0 Type B observed); breaks 04-07 interpretation | Type classification rejected as non-real phenomenon |

---

## Canonical Spec Version History

### CV-1.5 (2026-04-27) — W5 Day 1 G0: σ-Framework Supporting Structures Canonical Merge

- **Added Cat A**: T-σ-Lemma-1 (Irrep Decomposition Well-Defined), T-σ-Lemma-2 (Nodal Count Properties — sub-statements (i,ii,iii,iv) Cat A; (v) Courant + (vi) orbit-divisibility Cat C riders), T-σ-Lemma-3 (Goldstone–ℓ=1 Angular Saturation, Cat A in continuum), T-σ-Theorem-3 (σ at uniform on $D_4$ free-BC grid closed form), T-σ-Theorem-4 (σ at first pitchfork leading order, Cat A in $\epsilon$-small regime).
- **σ-framework status change**: Commitment 14 (W4 04-25) supporting structures (Lemma 1/2/3, Theorem 3/4) — T2 (deferred) → **T1 (canonical-merged)**.
- **Decision**: Option α (5 separate §13 entries) — per W5 strategic plan §0.4 Decision 1 default; chosen because mathematically independent statements deserve individual canonical visibility for paper §4 σ-framework reference.
- **Pre-brainstorm corrections folded in** (`logs/daily/2026-04-27/pre_brainstorm.md` §1.1/1.2/1.3/1.4):
  - T-σ-Lemma-1: finite-graph hypothesis essential (Maschke fails on infinite groups without compact-Lie or amenable extension); trivial-stabilizer case vacuous remark added.
  - T-σ-Lemma-2 (iii): plan-template wording "$n_k = 1$ iff $\phi_k$ constant" was incorrect for $\phi_k \in \mathbf{1}^\perp$ (constant in $\mathbf{1}^\perp$ requires $\phi_k = 0$). Replaced with lower bound $\mathcal{N}(\phi_k) \geq 2$ from $\sum \phi_k = 0$ constraint. **Cat A** (was "Cat A" but with wrong content).
  - T-σ-Lemma-2 (vi): orbit divisibility restricted to non-invariant $\phi_k$ (vacuous for $G_u$-invariant case).
  - T-σ-Lemma-3: IBP interpretation B adopted ($\delta u^{\mathrm{ref}} = $ unit vector in ℓ=1 angular subspace) per W4-04-24 §3.3 actual proof structure; sat. identity is between Goldstone basis and ℓ=1 angular basis.
- **Counts**: 38 + 5 = **43** Category A; 52 + 5 = **57 claims**; 73% → **75% fully proved**.
- **T1 explosion**: 3 → **8** (Option α: each of Lemma 1, 2, 3, Theorem 3, 4 individually T1).
- **canonical.md growth**: 1420 → 1537 lines (~117 lines added; entries are concise per W4 §13 style).
- **Source**: `THEORY/logs/daily/2026-04-27/01_sigma_lemmas_review.md` (decision packet); `01a_lemma1_irrep_decomposition.md`, `01b_lemma2_nodal_count.md`, `01c_lemma3_goldstone_saturation.md`, `01d_theorem3_uniform_D4_grid.md`, `01e_theorem4_first_pitchfork.md` (per-statement files); `THEORY/canonical/canonical.md` §13 lines 1169-1306 (new entries between T-V5b-T and T-Birth-Parametric).

**Errata Round 1 (2026-04-27 evening, post-merge re-review)**: User-requested re-audit caught 3 substantive math errors in this morning's canonical merge. All errors fixed in canonical entries (with embedded `*Erratum 2026-04-27 evening:*` notes). **Theorem status NOT changed**: all 5 σ structures remain Cat A. See `THEORY/logs/daily/2026-04-27/91_critical_review.md`.

- T-σ-Lemma-3 (i): IBP identity value $-m \to -c_d \int u^*(r) dr$ (factor-$r_0$ correction inherited from W4-04-24 source; $c_d$ dimension-dependent).
- T-σ-Theorem-4 (ii): $K_1 < K_0$ → $K_1 = K_0$ on $D_4$ ($A_2/A_1 = 4$); "would-be Goldstone" framing removed.
- T-σ-Theorem-3 (vi): irrep-table speculative entries replaced with rigorous Schur-orthogonality character calculation.

**Round 2 refinements (2026-04-27 night, second re-review)**: User-requested second re-audit caught structural issues beyond Round-1 value errors. 7 issues fixed in canonical (with `*Refinement 2026-04-27 night*` markers); 2 commitment-level changes deferred to user decision; 4 NQs spawned (NQ-187..NQ-190). **Theorem status still NOT changed**. See `THEORY/logs/daily/2026-04-27/92_critical_review_round2.md`.

- T-σ-Lemma-3: (i) reframed to lead with rank/injectivity (IBP value as corollary); statement extended to general dimension $d$ (1D cycle, 2D/3D bulk and torus); (iii) nodal=2 made explicit for all dimensions. **Fully anchors T-V5b-T-(e) "universal on translation-invariant graphs"** (previously only 2D-localized).
- T-σ-Lemma-3: anchoring footer added — registers which T-V5b-T sub-statements σ supports structures anchor (only (e)) vs leave canonical-empirical ((a)/(b)/(c)/(d)).
- T-σ-Theorem-3: spinodal hypothesis discussion added — clarifies role of $W''(c) < 0$ vs outside-spinodal vs spinodal-boundary cases.
- T-σ-Theorem-4: (i') orbit-representative remark added — clarifies σ-tuple is for chosen representative; conjugate stabilizers across orbit give σ-equivalence.
- T-σ-Theorem-4: well-definedness note added — flags $K_0 = K_1$ degeneracy requires Commitment 14 (O7) tie-breaking convention (deferred to user decision).
- 04_nq174_setup.md: PRE-RUN sanity test snippet added (Round-1 §6.G follow-through).

**Deferred to W5 Day 2+ user decision (Commitment-level changes)**:
- Commitment 14 (O5') multi-irrep eigenspace convention.
- Commitment 14 (O7) tie-breaking convention by canonical irrep order.

### CV-1.4 (2026-04-26) — W4 Extended Close: V5b-T Verification + Partial Goldstone Discovery

- **Added Cat A**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice spectral dichotomy with commensurability splitting on 2D torus, 1-fold Goldstone on 1D cycle, universal nodal count.
- **New Cat C finding**: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — boundary lifting mechanism qualitative observation. NQ-173 carry.
- **V5b 8 iterations resolved**: V1 (W4-04-24 morning) → V5b'' (W4-extended 04-26 evening). Healthy iterative refinement pattern.
- **Reproducibility crisis identified+resolved**: NQ-172 (mode-indexing artifact in NQ-170 analysis script). Mode-agnostic detection adopted.
- **σ-framework strengthening**: NQ-141 single-graph empirical → multi-graph (3 classes) empirical Cat A.
- **Count**: 37 + 1 = **38** Category A; 51 + 1 = **52 claims**; 73% fully proved.
- **W4 extended scope**: 2026-04-19 ~ 2026-04-26 (8 days). Per user direction "아직 내용은 전부 W4로 간주해".
- **Source**: `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (extended close, post-2026-04-26 update); `logs/daily/2026-04-26/04_NQ170c_graph_extension_nodal.md`.

### CV-1.3 (2026-04-25) — W4 Merge: Pre-Objective Mechanism + F-1/M-1/MO-1 Resolution

- **Added Cat A:** T-PreObj-1 (Pre-Objective Multi-Peak Formation Mechanism), T-PreObj-1G (graph-class independent), Lemma 4 (Quadratic form PD).
- **Added Cat A corollary:** F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 (i).
- **Critical blocker resolution:** F-1 (OP-0001) split-resolved, M-1 (OP-0002) layer-clarified, MO-1 (OP-0003) sidestepped. **3 → 0** Critical blockers.
- **Status changes:** C-0550, C-0551, C-0552 (challenged → resolved/clarified/sidestepped).
- **Count:** 35 + 2 = **37** Category A; 49 + 2 = **51 claims**; 71% → **73% fully proved**.
- **Pending user decision (T2 candidates, deferred):** σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1 placement, CN15/16/17 (Static/Dynamic Separation, Protocol-Parameterized observables, σ-labeled FQ), Commitment 14/15 v2.
- **Source:** `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (W4 closing summary, ~25 pages).

### CV-1.2 (2026-04-12) — Frozen, with Audit Clarifications

- **Added:** T-Persist-K-Unified (Category B; parametric coverage of Sep/Weak/Strong regimes)
- **Explicit Assumptions:** All K-field theorems now state "fixed K, fixed m" constraint
- **Status Clarifications:**
  - F-1, M-1, MO-1 documented as unresolved (not silently ignored) — *resolved in CV-1.3*
  - Type A/B classification retracted (exp65 invalidated)
  - Morse theory MO-1 vulnerability flagged (mitigation: use existing results, defer full Morse) — *sidestepped in CV-1.3*
- **Count:** 38 + 1 (T-Persist-K-Unified) = 39 theorems (per CV-1.2 release accounting; honest recount 04-07 → 35A/4B/5C/5R)

### CV-1.1 (2026-04-03) — PLAN_0403 Tier 1 Complete

- **Upgraded to Category A:**
  - C-Axioms (C3'' symmetrization gap closed)
  - Predicate-Energy Bridge (formalized)
  - Deep Core Dominance 2b (strengthened)
- **New Unconditional Results:**
  - T-Persist-1(b): Basin unconditional via genericity argument
  - T-Persist-1(e): Confinement tight bounds (2.4-3.5×)
- **New:** T-Bind-Full (Category A, τ=1/2 only)
- **Count:** 35 → 38 Category A (3 upgraded)

### CV-1.0 (2026-04-01) — Initial Comprehensive Spec

- **Theorems:** T-1, T-3, T-6a, T-6b, T-6-Stability, T-7, T-8-Core, T-8-Full, T-11, T-14, T-20
- **QM Results:** QM-1, QM-2, QM-3, QM-4 (11 Category A)
- **Provisional:** Predicate-Energy Bridge, Deep Core Dom. 2b (Category B at the time)
- **K-field:** T-Persist-K-Sep (Category B), T-Persist-K-Weak (Category C)
- **Notes:** Initial comprehensive spec; 35+ theorems claimed
- **Retracted:** K-Saddle Conjecture, r̄₀ general τ (kept in archive)

---

## Open Problems (OP-xxxx) — Updated 2026-05-04 (audit pass; OP-ID system unified per `open_problems.md` as master)

> Note (2026-05-04 audit): the OP-ID system in this file previously used a different numbering than `open_problems.md` (the authoritative registry). The table below has been re-synced to use `open_problems.md` IDs. Severity flags are kept in plain-text form per project documentation policy (Critical / High / Medium / Low) instead of color emojis.

| OP-ID | Problem | Severity | Status | Blocker For |
|-------|---------|----------|--------|-------------|
| **OP-0001** | F-1: K=2 vacuous | (was Critical) Resolved | SPLIT-RESOLVED (2026-04-24) via T-PreObj-1 (i) + T-Merge (b) | (no longer blocking) |
| **OP-0002** | M-1: K=1 preferred | (was Critical) Resolved | LAYER-CLARIFIED (2026-04-24) — proved theorem misframed | (no longer blocking) |
| **OP-0003** | MO-1: Morse fails | (was High) Sidestepped | SIDESTEPPED (2026-04-24) for single-formation σ scope; re-activation rider on D-6b approval or NQ-248 multi-formation Morse work | Multi-formation σ Phase 5 (re-engages) |
| **OP-0004** | Type A/B Classification Invalidation | High | RETRACTED (empirically invalidated; exp65 0/4 Type B observed) | Branch selection narrative |
| **OP-0005** | K Selection Mechanism (Missing) | High | OPEN; partial via 4-layer composite (free-energy / Kramers / numerical anchor / Commitment 16); CV-1.7+ Commitment 19 candidate | Multi-formation completeness |
| **OP-0006** | Boundary Definition Precision | High | TENTATIVE (D-0013 in development) | Morphology formalization, Q_morph |
| **OP-0008** | σ^A K-jump Inheritance Non-Determinism | High | OPEN (CV-1.5.1, W5 Day 4); Path B σ-rich + Φ-rich Cat B target; CV-1.7 Commitment 18 candidate | Dynamic σ-framework |
| **OP-0009** | Multi-Formation Ontological Foundations | High | OPEN (CV-1.5.1, W5 Day 4; 7 sub-items); 1/7 RESOLVED via Commitment 16 (OP-0009-K), 6/7 PARTIALLY (per body of `open_problems.md`; the post-OAT table marks some as "RESOLVED" but the conservative reading is PARTIALLY) | Multi-formation σ + reservoir architecture |
| **OP-0010** | Bind Generalization | Medium | OPEN | Bind diagnostic completeness |
| **OP-0011** | Transport kernel exact form | Medium | TENTATIVE | Full persist theorem |
| **OP-0012** | Persistence composition | Medium | OPEN | Persist diagnostic completeness |
| **OP-0013** | Closure operator convergence rate | Medium | OPEN | A3 sharpness |
| **OP-0020** | Dynamic Topology (Out of Scope) | Low | seed (formerly listed as OP-0007 in this file) | Future multi-scale extension |
| **OP-0021** | (see `open_problems.md`) | Low | seed | — |
| **OP-0022** | (see `open_problems.md`) | Low | seed | — |

**W4 changes (2026-04-25):** Critical blockers 3 → 0. F-1 / M-1 / MO-1 all resolved / clarified / sidestepped via T-PreObj-1 family + T-Merge(b) + σ-framework single-formation scope.

**W5 changes (2026-04-29 CV-1.5.1 + 2026-04-30 W5 Day 4):** OP-0008 σ^A K-jump non-determinism + OP-0009 Multi-Formation Ontological Foundations registered High. OP-0009-K resolved via Commitment 16. OP-0003 MO-1 re-activation rider added.

See `open_problems.md` for detailed body-level entries.

---

## Proof Status Summary (Updated 2026-05-02, post-CV-1.5.2 T-L1-F canonical promotion)

| Status | Count | Examples |
|--------|-------|----------|
| **Category A (Fully Proved)** | **46** (was 43 post-v1.5, 38 post-v1.4, 37 post-v1.3, 35 pre-W4) | T-1, T-20, QM-1:4, C-Axioms, Predicate-Energy Bridge, T-PreObj-1, T-PreObj-1G, Lemma 4 (W4), T-V5b-T (W4 extended), T-σ-Lemma-1, T-σ-Lemma-2, T-σ-Lemma-3, T-σ-Theorem-3 (W5 Day 1 G0; T-σ-Theorem-4 retroactively격하 to Cat B at CV-1.5.1), **T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static (W5 Day 4 D-6a multi-formation σ static)**, **T-L1-F (W5 Day 6 CV-1.5.2 hard-bar / active-count bridge under L1-J regime, conditional)**, etc. |
| **Category B (Conditional)** | **5** (canonical §13 hard Cat B = 4: γ_eff, T-Birth-Parametric General, T-d_min-Formula, T-Beyond-Weyl; plus T-σ-Theorem-4 retroactive Cat A → Cat B at CV-1.5.1; plus T-σ-Multi-1 Cat B target. T-Persist-K-Sep / T-Persist-K-Unified previously listed here have actually been Cat C since 2026-04-07 per canonical Erratum.) | γ_eff ≈ 0.89 (empirical, branch-conditioned); T-Birth-Parametric General (non-D₄ graphs); T-d_min-Formula (regression fit); T-Beyond-Weyl (grid-specific quantification); **T-σ-Theorem-4 (Cat A → Cat B retroactive at CV-1.5.1, NQ-187 finding + Critic 7-agent verdict; Cat A re-promotion deferred to CV-1.7+ post-γ/β/α audit)**; **T-σ-Multi-1 (Cat B target, Goldstone-pair instability under V5b-T per-formation regime)**. *(Corrected 2026-05-04 W6 G2 audit: removed T-Bind-Proj per Phase 13 Cat A upgrade; the resulting count is 6 entries — pending §15 / §13 Cat B header reconciliation, see CHANGELOG W6 G2 entry. The "5" headline kept for now to match canonical §15 wording until the next canonical-merge cycle resolves the count.)* |
| **Category C (Very Conditional)** | 5 + 1 (new finding) + 2 (W5 Day 1 sub-statements within T-σ-Lemma-2) | T-Persist-1(a/d), T-Persist-Full, T-Persist-K-Sep (per canonical Erratum 2026-04-07), T-Persist-K-Weak, T-Persist-K-Unified; V5b-F (new finding 2026-04-26, NQ-173 carry); T-σ-Lemma-2 (v) Courant upper bound + (vi) $G_u$-orbit divisibility (W5 Day 1 sub-statements bundled in single Cat A parent entry). *(Corrected 2026-05-04 W6 G2 audit: removed T-Bind-Full per Phase 13 Cat A upgrade.)* |
| **Resolved/Clarified/Sidestepped (W4)** | 3 | C-0550 (F-1 split-resolved), C-0551 (M-1 layer-clarified), C-0552 (MO-1 sidestepped) |
| **Challenged** | 1 | C-0553 (Type A/B) |
| **Retracted** | 5 | K-Saddle Conjecture; r̄₀ general τ (Theorem 3.3); T-Merge (c); T-Merge (d); T-Merge (e). *(Corrected 2026-05-04 audit: prior "2" entry was inconsistent with `canonical.md` §13 Retracted block which catalogues 5 distinct retractions.)* |
| **Open (active)** | **High: 4 (OP-0005 K-Selection, OP-0006 Boundary, OP-0008 σ^A K-jump, OP-0009 Multi-Formation Foundations); Medium: 4 (OP-0010..OP-0013); Low: 3 (OP-0020..OP-0022)** — total 11. OP-0001/0002 resolved (W4); OP-0003 sidestepped with re-activation rider; OP-0004 retracted (Type A/B). | OP-0005 K-Selection partial via 4-layer composite (CV-1.7+ candidate); OP-0008 σ^A K-jump (Path B σ-rich + Φ-rich Cat B target, CV-1.7 Commitment 18 candidate); OP-0009 7 sub-items (1/7 RESOLVED via Commitment 16, 6/7 PARTIALLY per `open_problems.md` body). |
| **Reproducibility crises identified+resolved** | 1 | NQ-172 (mode-indexing artifact, 2026-04-26 resolved) |
| **W4-extended carry NQ** | 3 (G1/G2/G4) | NQ-173 (V5b-F partial Goldstone — G1 W5 Day 1), NQ-174 (ζ_* graph-dependence — G2 W5 Day 2-3), NQ-175 (3D extension — G4 W5 Day 5) |
| **W5 Day 1 G0 spawn NQ** | 11 (NQ-176..NQ-186) | NQ-176/177 (functoriality, multi-irrep ordering — Lemma 1); NQ-178/179 (frustration bound, orbit sharpening — Lemma 2); NQ-180/181 (discrete correction, higher-ℓ analog — Lemma 3); NQ-182/183 (discrete nodal count, periodic-BC analog — Theorem 3); NQ-184/185/186 (tie-break, higher pitchforks, cascade — Theorem 4) |
| **W5 Day 1 Round-2 spawn NQ** | 4 (NQ-187..NQ-190) | NQ-187 (higher-order $\epsilon$-splitting of $K_0 = K_1$ on $D_4$ — Theorem 4); NQ-188 (σ-uniqueness theorem — # distinct σ-classes per graph/parameter regime); NQ-189 (σ → crisp object recovery — Commitment 11 derivative-objecthood); NQ-190 (σ topological invariance under graph homeomorphism). See `THEORY/logs/daily/2026-04-27/92_critical_review_round2.md` §10, §12. |

---

## Cross-Reference by Topic

### Single-Formation Theory
- **Existence:** T-1
- **Stability:** T-3, T-6-Stability, T-7
- **Phase Transition:** T-8-Core, T-8-Full
- **Convergence:** T-11, T-14
- **Diagnostics:** T-Bind-Proj/Full, Predicate-Energy Bridge

### Multi-Formation (K-field / Shared-pool $\widetilde\Sigma_M^{K_{\mathrm{field}}}$)
- **Temporal Persistence:** T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified
- **Global Stability:** Deep Core Dominance 2b (conditional)
- **σ-framework Multi (W5 Day 4 D-6a static, CV-1.5.1):** T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static, T-σ-Multi-1 (Cat B target)
- **Hard-Bar / Active-Count Bridge (W5 Day 6, CV-1.5.2):** **T-L1-F** (Cat A conditional under L1-J regime $(P0)$–$(P11)$)
- **K-status (CV-1.5.1):** Commitment 16 K_field/K_act Two-Tier Decomposition
- **Open:** F-1 / M-1 (W4 resolved), OP-0006, **OP-0008 σ^A K-jump non-determinism (HIGH)**, **OP-0009 Multi-Formation Ontological Foundations (HIGH, 7 sub-items, 1/7 RESOLVED + 6/7 PARTIALLY)**

### Foundational
- **Consistency:** T-20, C-Axioms
- **Quantum Analogy:** QM-1:4

---

## Maintenance

- **Owned by:** Lead + Archivist
- **Updated:** When new C-xxxx promoted to canonical or P-xxxx completed
- **Validation:** build_dependency_graph.py checks for consistency

---

**Last updated:** 2026-05-04 (audit pass; OP-ID system unified, working content moved out per CLAUDE.md contamination barrier)
**Total canonical theorems:** **56** = **46 Cat A** + 5 Cat B + 5 Cat C — 5 retracted (**61 claims, 75% fully proved**)
**Open problems:** see Open Problems table above (4 High + 4 Medium + 3 Low active; 3 Critical resolved in W4; 1 retracted)

**Note (2026-05-04 audit):** prior versions of this section listed forward-looking content ("W5 Day 7 working draft", "Pending W6+", "Future-stale items pending CV-1.6 release") that belong in `THEORY/CHANGELOG.md` (chronological session log) and `THEORY/logs/weekly/...strategic_plan.md` (forward planning). Per CLAUDE.md contamination barrier ("canonical/ accepts only promoted content"), those forward-looking lines were moved out of this canonical-layer file. The W5 Day 7 L1-M soft-count working draft, the pending W6+ promotion targets, and the future-stale list are recorded in CHANGELOG.md (2026-05-04 audit-pass entry).

**Recent W4 additions (2026-04-25)**: T-PreObj-1, T-PreObj-1G, Lemma 4 (Pre-Objective Mechanism graph-class independent), Commitment 14/15, CN15/16/17.
**W4 extended addition (2026-04-26)**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice dichotomy on torus T^d, cycle C_n; 2D doublet commensurability split; 1D Goldstone; nodal count = 2 universal. V5b 8-iteration cycle resolved.
**W5 Day 1 G0 addition (2026-04-27, CV-1.5)**: T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4 — σ-framework supporting structures grounding Commitment 14 in §13 directly. Option α (5 separate entries). Pre-brainstorm corrections folded in (finite-graph hypothesis explicit, Lemma 2 (iii) reframed as lower bound, Lemma 3 IBP interpretation B adopted). Round-1 (3 numerical errors) + Round-2 (11 structural issues) audit applied same session.
**W5 Day 4 addition (2026-04-30, CV-1.5.1)**: D-6a multi-formation σ static (3 Cat A: T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static) + 1 Cat B target (T-σ-Multi-1 Goldstone-pair instability) + Commitment 16 K-status Two-Tier Decomposition (K_field/K_act; resolves OP-0009-K). T-σ-Theorem-4 Cat A → Cat B retroactive (NQ-187 RED finding + Critic 7-agent verdict). OP-0008 + OP-0009 registered High; OP-0003 MO-1 re-activation rider added.
**W5 Day 6 addition (2026-05-02, CV-1.5.2 — current)**: T-L1-F (Hard-Bar / Active-Count Bridge under L1-J Regime) Cat A conditional under hypothesis package $(P0)$–$(P11)$. First multi-formation canonical Cat A theorem. L1-A through L1-L 13-step working chain + L1-K external audit + L1-K-REPAIR cycle (R-1..R-4) completed. open_problems.md unchanged (T-L1-F is a bridge, not a K-selection mechanism).
**See also:** `weekly_summary.md` (W4 extended close), `open_problems.md` (active OPs), `canonical.md` §13 (theorem catalog), `THEORY/logs/daily/2026-04-27/` (W5 Day 1 artifacts), `THEORY/logs/weekly/2026-04-W5/W5_strategic_plan.md` (8-goal blueprint), `THEORY/CHANGELOG.md` 2026-04-27 entry.
