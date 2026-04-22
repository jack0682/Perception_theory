# Integer-K Dependency Map

**Status:** updating (Round 12-18 post-audit rewrite, 2026-04-22).
**Last touched:** 2026-04-22 (SF-S1 session).
**Previous versions:** 2026-04-20 (initial topic consolidation), 2026-04-21 evening Round 2 errata note (E-5/E-6 pending).
**Canonical refs:** `canonical.md` §12 (K-field), §13 Cat A (T-Merge (a), Topological Lock, Coupling Bound Lemma, Prop 1.2, Thm 3.1), §13 Cat B (γ_eff ≈ 0.89, T-Beyond-Weyl, T-d_min-Formula), §13 Cat C (T-Persist-K-Sep/Weak/Unified).
**Working refs:** `working/SF/mode_count.md` (Prop 1.3a/b, integer-K derivability), `working/SF/interface_scale.md` (ξ_0 anchor), `working/MF/from_single.md` (derived multi-formation view, Conjecture 2.1), `working/E/{F1,M1,MO1}_dissolution.md` §Round 18 post-audit sections.
**Origin:** `THEORY/logs/daily/2026-04-20/01_exploration.md` §5.2–§5.3 (3rd audit); 2026-04-22 `logs/daily/2026-04-22/01_exploration.md` §3.2 (Axis B derivation rationale).

---

## §1. Rewrite motivation (2026-04-22)

Previous version (2026-04-20 + 2026-04-21 errata note) identified 10 integer-K load-bearing theorems and called for retirement based on "soft-K hat statement meaning disappears under soft-K reformulation".

**Round 12-18 + Axis B derivation (2026-04-22) provides a stronger reason:** integer $K$ is **derivable** from single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ via `working/MF/from_single.md` §2 Conjecture 2.1. The retirement reason for the 10 integer-K theorems is therefore updated:

- **Old reason** (2026-04-20): "soft-K hat statement meaning disappears."
- **New reason** (2026-04-22): "integer-K is a derivable statistic from $(N_{\mathrm{unst}}, \xi_0)$; the K-field architecture $\Sigma^K_M$ with external $m_j$ is an optional representation, not a primitive requirement."

This is a stronger statement. It says: *integer-K is not wrong, but it is not primitive*. The 10 theorems remain valid within K-field architecture but are not needed in the derived view.

---

## §2. Integer-K Load-Bearing Theorems (9 + 1)

Unchanged from 2026-04-20 enumeration; retirement reasons updated per Round 12-18.

### 2.1 Category A — Retire (5 → 5; count unchanged)

Statements involve per-formation mass $\Sigma^K_M$, per-formation Hessian products, or $(K-1)$ coupling factors that are **integer-K specific**. In derived view, these live within K-field architecture but do not speak to the underlying single-field Σ_m analysis.

| # | Theorem | canonical.md line | Integer-K dependence | Retire reason (2026-04-22) |
|---|---|---|---|---|
| 1 | **T-Merge (a)** — K-Formation Local Minimality | §13, 979 | $\Sigma^K_M$ manifold | Valid within K-field architecture; single-field Σ_m equivalent: $u^\ast$ with $K_{\mathrm{soft}}(u^\ast) \approx K$ is a local minimum (captured by `cardinality_open.md` §2) |
| 2 | **Topological Lock** — Merge Impossible on $\Sigma^K_M$ | §13, 988 | $\Sigma^K_M$-specific | $\Sigma^K_M$ not needed in derived view; Σ_m is connected, merge paths exist (MO1_dissolution §9) |
| 3 | **Coupling Bound Lemma** — K-Formation Hessian | §13, 820 | $(K-1)\lambda_{\mathrm{rep}}$ | Core result (exponential tail decay at distance, Item 5) reusable in single-field context; $(K-1)$ coupling factor is K-field specific |
| 4 | **Proposition 1.2** — Fiber Dimension | §13, 1026 | $\Sigma^2_M$ stratified Morse | $\Sigma^2_M$ not needed; Σ_m is convex polytope (Prop 1.1), smooth Morse on Σ_m^ε \ V (MO1_dissolution §9.2) |
| 5 | **Theorem 3.1(a,b,d)** — Landscape at Symmetric Point | §13, 1031 | $(m_1 = m_2 = M/2)$ symmetric point | "Symmetric point" is Σ²_M-specific; single-field analog: $u^\ast$ with $K_{\mathrm{soft}} \approx 2$, mode centers related by graph automorphism |

**Re-prove (retain) 1 (unchanged):** T-Merge (b) Cat A (line 984), isoperimetric energy ordering. Γ-convergence proof survives in derived view as "single-mode ($K_{\mathrm{soft}} \approx 1$) has lower energy than multi-mode ($K_{\mathrm{soft}} > 1$) on connected graph" (M1_dissolution §2.2). **This is the only retained theorem among the 10.**

### 2.2 Category B — Retire (1 → 3; **+2 per E-5 applied**)

E-5 (2026-04-21 Round 2 errata, originally pending) identified two additional Cat B theorems for retirement, now applied:

| # | Result | canonical.md line | Integer-K dependence | Retire reason (2026-04-22) |
|---|---|---|---|---|
| 6 | **γ_eff ≈ 0.89** K-merge barrier exponent | §13, 992 (erratum) | "K-merge" barrier | Empirical, protocol/path-conditioned (canonical 2026-04-10 erratum + Round 11 Stage 5 NEB numerics confirming non-reproducibility); in derived view, barrier between $K_{\mathrm{soft}} = K+1$ and $K_{\mathrm{soft}} = K$ basins on single Σ_m is mode-unification barrier; $\beta^{0.89}$ is protocol measurement, NOT universal invariant |
| **7** (new) | **T-Beyond-Weyl** | §13, 1057 (Cat B) | $\omega_{\mathrm{soft}}$ from $\mathcal{P}_{O_{jk}}\psi_k^{\mathrm{soft}}$ — pair-overlap projection | K-formation pair-overlap concept requires Σ²_M; single-field analog via Prop 1.3b cl_sep eigenmode analysis (carry to post-Stage-1) |
| **8** (new) | **T-d_min-Formula** | §13, 1053 (Cat B) | $d_{\min}^\ast = 4.8 + 0.31\sqrt{\beta/\alpha}$ — branch-conditioned regression | Direction fix in `working/MF/from_single.md` §4: $d_{\min}^\ast \asymp \xi_0\cdot \log(1/\epsilon_0)$, NOT $\sqrt{\beta/\alpha}$; prior fit is an artifact of branch-specific protocol (NQ-30) |

**Total Cat B retire: 3** (γ_eff, T-Beyond-Weyl, T-d_min-Formula). This is the E-5 update now applied.

### 2.3 Category C — Re-prove (3, unchanged)

Per-formation index can be reinterpreted as soft-K distribution mode index; persistence results survive but require proof rewrite.

| # | Theorem | canonical.md line | Integer-K dependence | Reinterpretation |
|---|---|---|---|---|
| 9 | **T-Persist-K-Sep** | §13, 1065 | per-formation $j \in \{1,\ldots,K\}$ | "K independent formations" → "K well-separated modes of single field" |
| 10 | **T-Persist-K-Weak** | §13, 1110 | joint Hessian, $(K-1)\lambda_{\mathrm{rep}}$ | Weyl bound on single-field Hessian with pair-mode interaction |
| 11 | **T-Persist-K-Unified** | §13, 1115 | pair index $(j,k)$ in $\Lambda_{\mathrm{coupling}}$ | $\Lambda$ becomes soft-mode overlap measure; Corollaries reorganize |

### 2.4 Total count update (2026-04-22)

- **Retire 8** (5 Cat A + 3 Cat B) — up from 6 in 2026-04-20 original.
- **Re-prove 3** (Cat C) — unchanged.
- **Re-prove (retain) 1** (T-Merge (b) Cat A) — unchanged.
- **Total touched: 12** (was 10 in original count).

---

## §3. Single-Formation Cat A Survival (22 + 4 = 26)

Soft-K reformulation and derived multi-formation view do NOT require retirement of single-formation-only Cat A theorems. These **survive**.

### 3.1 Canonical-original 22 Cat A survivors (Round 2 verified + §3 corrected)

(Round 2 verification in `logs/daily/2026-04-21/05_deepening_and_verification.md` §4 enumerated exactly these 22.)

**T-1** (Existence), **T-3** / **T-6a/b/Stability** (Closure FP), **T-7** (Enhanced Metastability), **T-8-Core/Full** (Phase Transition), **T-11** (Γ-Convergence), **T-14** (Gradient Flow), **T-20** (Axiom Consistency), **C-Axioms**, **QM-1/2/3/4**, **Predicate-Energy Bridge**, **T-Bind-Proj** (all τ), **Deep Core Dominance 2b**, **T-Persist-1(b)/(e)**, **T-A2**, **Prop 1.1** (Σ_m convex polytope), **T-Birth-Parametric** (D4 supercritical), **Persistence Threshold Equation**.

(Round 2 §4: original `integer_K_dependency_map.md` §3 claimed 19; Round 2 re-enumerated to 22, applying E-6 to this file is the action of §2.4.)

### 3.2 Round 12-18 new Cat A survivors (+4)

**Prop 1.3a** (pure $\mathcal{E}_{\mathrm{bd}}$ Morse index) — `working/SF/mode_count.md` §1.
**Prop 1.3b** (cl_sep structural decomposition, (a)-(c)+(e)) — `working/SF/mode_count.md` §2.
**Cor 2.2 qualitative** (interface concentration) — `working/SF/interface_scale.md` §2.
**Cor 2.2 quantitative (tanh ansatz)** — `working/SF/interface_scale.md` §3.

**Total single-formation Cat A post-Round 18: 22 + 4 = 26.**

### 3.3 Cat B/C single-formation survivors

- **Cat B (survive):** T-Bind-Full (τ=1/2 single formation variant was Cat A in Round 2; general τ remains Cat B per canonical §13).
- **Cat C (survive):** T-Persist-1(a)/(d)/Full — all single-formation applicable, `β > 7α` condition retained.

---

## §4. Candidate A vs E coverage equivalence (context, unchanged)

(Retained from 2026-04-20.) Both candidates cover the same 9+1 theorems listed in §2; A adds threshold-level and axiom-switching work beyond this list. Matrix-2 coarse coding renders them indistinguishable at theorem-level; only session depth (A 18 vs E 12) and qualitative reach differ.

---

## §5. Retire vs Re-prove criterion (updated)

- **Retire:** Statement uses K-field architecture primitives ($\Sigma^K_M$, per-formation mass, $(K-1)$ coupling factor) as load-bearing. In derived view, the architecture is not required; the theorem's information content is either (a) reproducible via single-field analysis with different language, or (b) branch-conditioned and better served by NQ-30 remeasurement.
- **Re-prove:** Statement's mathematical content survives under single-field reinterpretation but requires rewriting proof.
- **Re-prove (retain):** Proof core (e.g., Γ-convergence in T-Merge (b)) survives nearly intact; only statement language updates.

---

## §6. Previously Identified Inconsistencies (still open)

### 6.1 T-Persist-K-Sep Category (unchanged from 2026-04-20)

- `canonical.md` §13 line 1043 erratum (2026-04-07): T-Persist-K-Sep moved to Cat C.
- `theorem_status.md` (2026-04-12): still Cat B.

**Resolution (proposed):** sync `theorem_status.md` to Cat C per canonical §13 authority (`CLAUDE.md` principle: canonical is THE spec). Affects `theorem_status.md` line 47.

### 6.2 Cat C Count Header (unchanged from 2026-04-20)

- `canonical.md` §13 line 1061 header: "(5 theorems)".
- Actually listed: 6 or 7 (T-Bind-Full + T-Persist-1(a)/(d)/Full + T-Persist-K-Sep + T-Persist-K-Weak + T-Persist-K-Unified).

**Resolution (proposed):** update header count.

### 6.3 NEW (2026-04-22): T-d_min-Formula direction error

- canonical line 1007 (old) / §13 Cat B: $d_{\min}^\ast = 4.8 + 0.31\sqrt{\beta/\alpha}$.
- **Direction is wrong**: $\sqrt{\beta/\alpha} = 1/\xi_0$; correct scaling is $d_{\min}^\ast \asymp \xi_0\cdot \log(1/\epsilon_0)$ from Coupling Bound Lemma Item 5 (proof in `working/MF/from_single.md` §4 / `02_development.md` §7).
- Round 13 §2.5 flagged "dimensionally suspicious" — now analytically corrected.
- **Resolution:** NQ-30 remeasurement in ξ_0-axis rather than $\sqrt{\beta/\alpha}$-axis; canonical T-d_min-Formula Cat B downgrades further (wrong direction, not just Cat B fit).

---

## §7. Next Actions (updated 2026-04-22)

### 7.1 Immediate (pending user review this week)

- [ ] User review of §2.1–2.3 updated retire classification (8 total, +2 from E-5).
- [ ] User review of §3.2 +4 new Cat A survivors (Prop 1.3a, 1.3b (a)-(c)+(e), Cor 2.2 qual, Cor 2.2 quant tanh).
- [ ] Decision on §6.3 T-d_min-Formula direction correction: accept as canonical Cat B correction inline, or NQ-30 to re-measure?

### 7.2 Stage 2 (Axiom Audit) pre-deliverable

- [ ] Cross-check §2.4 "8 retire + 3 re-prove + 1 retain" against candidate E's soft-K completeness (is there a 11th theorem missed?).
- [ ] Cross-check §3 26 Cat A survivors against candidate E's axiom-switching (are additional ones threshold-sensitive?).

### 7.3 Stage 6 (Canonical merge)

- [ ] Apply retirements on canonical.md §13 (move 8 entries to Retracted or mark as "Valid within K-field architecture; single-field equivalents in working/SF/ + working/MF/").
- [ ] §13 T-Persist-K-Sep category resolve (6.1).
- [ ] §13 Cat C count header fix (6.2).
- [ ] §13 T-d_min-Formula direction correction (6.3).
- [ ] §13 add 4 new Cat A (Prop 1.3a/b, Cor 2.2 qual/quant).
- [ ] §11/§12 reshape: derived multi-formation view inserts a paragraph crediting working/MF/from_single.md §2 Conjecture 2.1; "K is kinetically determined" of CN6 acquires quantitative content (§6.2 of MF file).

### 7.4 Post-Stage-1 (future)

- [ ] G-D ($\mathrm{Aut}(G)$ orbit symmetry $\mathcal{M}_1$): scoped out, deep analysis.
- [ ] $\widehat{K}(N_{\mathrm{unst}})$ graph-class formula validation on non-2D graphs (exp_mode_emergence.py carry).
- [ ] NQ-32 (SCC profile deviation) resolution via exp_profile_fit.py execution.
- [ ] NQ-33 ($d_{\mathrm{eff}}(G)$ precise definition for non-lattice graphs).
- [ ] NQ-34 (coarsening exponent with SCC self-referentiality, LSW extension).

---

## §8. Relationship to other working files

- **`working/SF/mode_count.md`** produces Cat A substitutes for integer-K-retired claims via Prop 1.3a/b.
- **`working/SF/interface_scale.md`** produces the $\xi_0$-based single-formation geometry that replaces the $\sqrt{\beta/\alpha}$ fit.
- **`working/MF/from_single.md`** produces the derived multi-formation view.
- **`working/E/{F1,M1,MO1}_dissolution.md`** Round 18 post-audit sections provide the reframing of each Critical using the derived view.

**Canonical merge readiness:** all 8 retirements documented, 4 new Cat A ready for §13 insertion, direction correction for T-d_min-Formula staged. Pending Stage 6 weekly merge.

---

## §9. Session trace (updated)

- 2026-04-20: initial topic consolidation (9+1 theorems, 6 retire).
- 2026-04-21 (Round 2): E-5 identified (+2 retire candidates: T-Beyond-Weyl, T-d_min-Formula), pending.
- 2026-04-21 (Round 2): E-6 identified (§3 Cat A count 19 → 22), pending.
- **2026-04-22 (this session):** E-5, E-6 applied; §2.4 updated (8 retire total); §3.2 added (+4 Round 12-18 Cat A, total 26); §6.3 new inconsistency (T-d_min-Formula direction); retirement reason updated to derived-view framing.

**End of integer_K_dependency_map.md.**
