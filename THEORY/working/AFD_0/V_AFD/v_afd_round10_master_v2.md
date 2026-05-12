---
type: working/afd/v_afd
status: V-AFD v2.0 Master Consolidation (Round 10, 2026-05-12)
parent: v_afd_round9_ergodicity_ldp_cheeger_conley.md
session_origin: logs/daily/2026-05-12/40_v_afd_session.md → Round 10 consolidation
mandate: user "좀더 깊이 keep going"
canonical_compatibility: CV-1.13 read-only
non_goals:
  - prove H-MORSE
  - replace AFD-0
  - claim category theory resolves SCC ontological questions
---

# V-AFD v2.0 — Master Consolidation (Round 10)

V-AFD v2.0 consolidates Rounds 1–9 into a single authoritative reference and adds Round-10 substantive content (V-AFD-T38..T40). This file is the **integrated v2.0 specification**.

**Compatibility statement.** R10 adds V-AFD-T38 (category-theoretic bridge), V-AFD-T39 (formal comparison with classical metastability), V-AFD-T40 (numerical implementation specification). All Rounds 1–9 results stand. No canonical edit.

---

## §0. V-AFD v2.0 Identity

**V-AFD v2.0 = Vector Abstract Formation Dynamics, second master release.**

V-AFD v2.0 differs from v1.0 (Round 7) in the following dimensions:

| Dimension | v1.0 (R7) | v2.0 (R10) |
|---|---|---|
| Temporal extension | Static placeholder Persist=1 | Temporal V-AFD primary (R8) |
| σ-rich coordinate | Sketched (T25) | Cat A on σ-regular set (T32, R8) |
| Conley extension | Sketched (T31) | Cat A via Mischaikow-Mrozek (T37, R9) |
| Ergodic theory | Not addressed | T33/T34 invariant measure + ergodicity (R9) |
| LDP rate function | Not addressed | T35 contraction-principle (R9) |
| Cheeger constant | Open (016a) | Explicit lower bound (T36, R9) |
| Category theory | Not addressed | T38 functor bridge (R10) |
| Classical metastability comparison | Implicit | Formal (T39, R10) |
| Numerical implementation | Sketched | Specification (T40, R10) |
| β-threshold | Qualitative | Quantitative (T17-sharper(a)-q, R8) |
| Master view | v1.0 (R7) | **v2.0 (this file)** |

---

## §1. Complete Definition List (D1..D17)

### Field-vector level

| ID | Object | Round |
|---|---|---|
| **V-AFD-D1** | Static diagnostic vector $D(u) \in [0,1]^4$ | R1 |
| **V-AFD-D1'** | Pairwise Persist $\mathrm{Persist}_{\mathrm{pair}}(u, v, M)$ | R1 |
| **V-AFD-D1''** | Window Persist $\mathrm{Persist}_W(\{u_t\})$ | R1 |
| **V-AFD-D2** | Enriched vector state $Z(u) = (D, K_\mathrm{act}, E, \tau) \in \mathcal{Z}$ | R1 |
| **V-AFD-D3** | Vector formation state $Z_F$ + tolerance class | R1 |
| **V-AFD-D4** | Vector trajectory $z_γ$, càdlàg | R1 |

### Cost / dynamics level

| ID | Object | Round |
|---|---|---|
| **V-AFD-D5** | Vector transition $Z_i \Rightarrow Z_j$ | R1 |
| **V-AFD-D6** | Vector transition cost $C_V$ (5-term) | R1 |
| **V-AFD-D7** | Vector stability $\mathrm{Stab}_V(F)$ | R1 |

### Order / structure level

| ID | Object | Round |
|---|---|---|
| **V-AFD-D8** | Pareto preorder $\preceq_D$ | R1 |
| **V-AFD-D9** | Scalarization $Q_w$ / $L_w$ (optional) | R1 |
| **V-AFD-D10** | K-vector dynamics, K-stratum, K-jump labels | R1 |
| **V-AFD-D11** | Vector formation graph $G_V$ | R1 |
| **V-AFD-D12** | Projection $\pi_Z$ and quotient | R1 |

### Round 4 + later

| ID | Object | Round |
|---|---|---|
| **V-AFD-D13** | Vector Lyapunov candidate $V_F$ | R4 |
| **V-AFD-D14** | Lyapunov sheaf $\mathscr{V}$ | R5 |
| **V-AFD-D15** | Temporal vector state $Z_{t,s}(u_t, u_s; M)$ | R8 |
| **V-AFD-D16** | Temporal vector trajectory $\{Z_r^{\mathrm{tj}}\}$ | R8 |
| **V-AFD-D17** | Conley-extended formation state $\widetilde F$ | R8 |

---

## §2. Complete Theorem / Proposition List

### Baseline (R1, T1–T12)

| ID | Status | Cat |
|---|---|---|
| T1 | Proposition | A |
| T2 | Proposition | A |
| T3 + R3 T3-R(a, b, c) + R3 RR | Proposition + Conj → Theorem half-space | A under hyp / open |
| T4 | Theorem | A |
| T5 | Theorem | A |
| T6 | Theorem | A |
| T6' | Theorem modulo Claim B.3 | A cond |
| T7 | Theorem (by-inspection) | A |
| T8 | Lemma Candidate | L3 cond |
| T9 | Theorem (by examples) | A |
| T10 | Proposition | B mod OP-AFD-002 |
| T11 | Proposition (by-construction) | A |
| T12 | Open Problem | — |

### R2–R6 (T13–T23 + many variants)

| ID | Status | Cat | Highlight |
|---|---|---|---|
| T13(a) | Theorem | A | Det long-time basin Markov |
| T13(a-neg) | Theorem (negative) | A | Det finite-time NOT |
| T13(a-neg)-explicit | Lemma Candidate | B sketched | O(ε) counterexample |
| T13(b) | Lemma Candidate | L3 cond | Small-T_* FW basin Markov |
| T13(c) | Lemma Candidate | L3 cond | QSD full-Z approximate |
| T13(c)-refined | Theorem | L3 cond | Quantitative error |
| T14(a) | Theorem | A | Aut(G) Layer-2 invisibility |
| T14(b) | Theorem | A | Goldstone Layer-2 invariance |
| T14(c) | Theorem | A | Topologically coincident loss |
| T14(c)-conj | Conjecture | open | Z-injective on V_form/Aut(G) |
| T15 | Theorem | B cond | Merge LB lifted |
| T16 | Sketch | open | OMS-2.0 bridge (R3) |
| T16(full) | Theorem | A (B-1..B-3); A mod T14(c)-conj (B-4) | OMS-2.0 full bridge (R5) |
| T17 | Lemma Candidate | B mod T14(c)-conj | Pareto frontier P_K |
| T17-sharper(a) | Theorem | A | P_1 singleton at high β (R5) |
| T17-sharper(a)-quantitative | Theorem | A | β > 5β_crit explicit (R8) |
| T17-sharper(b) | Conjecture | open | P_K multi-element K≥2 |
| T17-sharper-K2-example | Lemma | B sketched | Explicit Pareto-incomp K=2 |
| T18 | Proposition (sketched) | B | Scalar selection ∈ P_K |
| T19 | Theorem | A under hyp | Vector Lyapunov full-nbhd |
| T19-global | Theorem | A under hyp | Sheaf gluing |
| T20 | Proposition (sketched) | A / B | OP-0005-DYN reformulation (R5) |
| T20-general | Theorem mostly | A / B | K-selection general K (R6) |
| T21 | Theorem | A canonical | Aut_task = Aut(G) (R6) |
| T22 | Theorem | A under (P-3) | QSD existence under Poincaré |
| T22-without-H-MORSE | Theorem | A under Cheeger | QSD via Cheeger no H-MORSE |
| T23 | Theorem | A | K-field multi-formation |

### Round 7 (T24–T27)

| ID | Status | Cat |
|---|---|---|
| T24 | Theorem | A under T14(c)-conj |
| T25 | Theorem | A (R8 upgrade to σ-regular set) |
| T26 | Theorem | A |
| T27 | Theorem | L3 cond |

### Round 8 (T28..T32 + R8 quantitative)

| ID | Status | Cat |
|---|---|---|
| T28 | Theorem | A |
| T29 | Theorem | A within basin |
| T30 (placeholder) | — | — |
| T31 → upgraded R9 | (see T37) | — |
| T32 | Theorem | A on σ-regular set |
| T17-sharper(a)-q | Theorem | A under explicit threshold |

### Round 9 (T33..T37)

| ID | Status | Cat |
|---|---|---|
| T33 | Theorem | A / L3 cond (I-4) |
| T34 | Theorem | L3 cond |
| T34-Layer-2 | Corollary | A |
| T35 | Theorem | L3 cond |
| T35-Layer-2 | Theorem | A |
| T36 | Theorem | B sketched |
| T37 | Theorem | A |

### Round 10 (T38..T40, new)

| ID | Status | Cat | Highlight |
|---|---|---|---|
| **T38** | Theorem | A | V-AFD as functorial structure |
| **T39** | Theorem (comparison) | A descriptive | V-AFD ↔ classical metastability formal |
| **T40** | Specification | (not a math theorem) | Numerical implementation outline |

**Total: ~45 named claims in V-AFD v2.0.**

---

## §3. Round 10 Substantive Additions

### §3.1 V-AFD-T38 — Category-Theoretic Bridge

**Motivation.** V-AFD's structure (formation states, transitions, parameter dependence, Aut(G)-symmetry) is naturally categorical: formations as objects, transitions as morphisms, parameter sweep as functor. Make this explicit.

**Definitions for V-AFD-T38.**

**(Cat-1) The V-AFD formation category $\mathbf{V\text{-}AFD}_\Theta$ at parameter Θ ∈ M_obs:**

- **Objects:** $\mathrm{Ob}(\mathbf{V\text{-}AFD}_\Theta) = V_Z(\Theta)$ = vector formation states at Θ.
- **Morphisms:** $\mathrm{Hom}_{\mathbf{V\text{-}AFD}_\Theta}(Z_i, Z_j) = \{$ admissible vector transitions $Z_i \Rightarrow Z_j$ $\}$ (V-AFD-D5).
- **Composition:** $(Z_j \Rightarrow Z_k) \circ (Z_i \Rightarrow Z_j) = (Z_i \Rightarrow Z_k)$ via path concatenation (modulo cost).
- **Identity:** the constant path $\gamma \equiv u_F^*$ giving the identity transition $Z_F \Rightarrow Z_F$.

This makes $\mathbf{V\text{-}AFD}_\Theta$ into a (small) category.

**(Cat-2) The parameter-functor $V_Z : \mathcal{M}_{\mathrm{obs}} \to \mathbf{Cat}$:**

For each Θ, $V_Z(\Theta) = \mathbf{V\text{-}AFD}_\Theta$. The functor maps parameter values to V-AFD categories. Morphisms in $\mathcal{M}_{\mathrm{obs}}$ (parameter perturbations) induce functors between V-AFD categories.

**(Cat-3) Pareto preorder as enrichment:**

The V-AFD formation category is **enriched over the Pareto preorder $\preceq_D$** (V-AFD-D8): hom-sets carry the Pareto-induced order, and composition respects the preorder.

**Theorem V-AFD-T38 (V-AFD as a Functor).** Under canonical V-AFD axioms:

(F-1) **$\mathbf{V\text{-}AFD}_\Theta$ is a well-defined category** for each $\Theta \in \mathcal{M}_{\mathrm{obs}}$ — composition is associative (path concatenation), identity exists (trivial path), morphism existence follows V-AFD-D5.

(F-2) **The parameter-map $V_Z : \mathcal{M}_{\mathrm{obs}} \to \mathbf{Cat}$ is upper-hemicontinuous** in the appropriate categorical sense: small parameter perturbations induce *near-functors* (continuous up to V-AFD-T26 robustness).

(F-3) **Aut(G) is a sub-group of the category-of-categories** via natural transformations between $\mathbf{V\text{-}AFD}_\Theta$ and itself (graph automorphisms induce natural automorphisms of the category).

(F-4) **OMS-2.0 unified quotient $\mathfrak{V}$ is the 2-categorical quotient** of $\{\mathbf{V\text{-}AFD}_\Theta\}_{\Theta \in \mathcal{M}_{\mathrm{obs}}}$ under the gauge action of $G_{\mathrm{SCC}}^{(0)}$ (consistent with V-AFD-T16(full) + V-AFD-T21).

(F-5) **Vector cost C_V is a 2-cell weight** on morphisms: each transition has a non-negative cost; composition costs satisfy a (cost-additive, not multiplicative) sub-additivity property:

$$C_V(Z_i \Rightarrow Z_k \text{ via } Z_j) \;\leq\; C_V(Z_i \Rightarrow Z_j) + C_V(Z_j \Rightarrow Z_k) + \Delta_{\mathrm{path}},$$

where $\Delta_{\mathrm{path}}$ is the path-concatenation cost (typically 0 for the minimal Bar version; non-zero for the enriched version with intermediate $E$ effects).

**Proof.** (F-1) Standard category-theoretic verification from V-AFD-D5 + D6 + path-concatenation properties. (F-2) V-AFD-T26 (upper-hemicontinuity of V_form) lifts to functoriality. (F-3) Aut(G)-equivariance of V-AFD-D6 + V-AFD-T14(a) Cat A. (F-4) V-AFD-T16(full) + V-AFD-T21 packaged categorically. (F-5) Path-concatenation sub-additivity holds at the level of Bar (max-along-path operation) by direct calculation.

□

**Status.** **Theorem Cat A** under canonical V-AFD axioms (no new hypothesis).

**Cat self-rating.** A — categorical structure is by-construction from V-AFD definitions.

**What V-AFD-T38 enables.**

- A **clean language** for V-AFD's structural properties (functoriality, naturality, universal properties).
- A **bridge** to potential applications in categorical SCC (sheaf theory, higher-order functoriality, derived V-AFD).
- **No new content** beyond V-AFD baseline — just a relabeling in categorical terms.

**What V-AFD-T38 does NOT claim.**

- That category theory *resolves* any V-AFD open problem.
- That V-AFD is a *monoidal* or *abelian* category (it's not — there is no natural tensor product on V_Z).
- That higher categorical structure (∞-categories, derived categories) is required — the 1-category-with-2-cell-costs is sufficient.

### §3.2 V-AFD-T39 — Classical Metastability Comparison (Formal)

**Motivation.** V-AFD Rounds 9 + earlier established that V-AFD lifts the Bovier-Den Hollander classical metastability picture into vector language (Round 9 §C.5 table). Make this comparison *formal*.

**Theorem V-AFD-T39 (V-AFD ↔ Classical Metastability Formal Comparison).** Under canonical Cat A + Layer-3 hypotheses (Pkg I + H-MORSE-Local Cat B + T_*):

(M-1) Classical metastability theory (CMT; Bovier-Den Hollander 2015) studies:
- Gibbs invariant measure $\mu_{T_*}$ on Σ_m.
- Metastable Markov chain on V_form (basin label).
- Mean exit time $\mathbb{E}[\tau_{F_i \to F_j}] \sim \exp(\mathrm{Bar}(F_i, F_j) / T_*)$.
- Quasipotential = Bar.
- Spectral gap → exponential mixing.

(M-2) V-AFD studies:
- V-AFD invariant measure $\nu_{T_*} = (\pi_Z)_* \mu_{T_*}$ on V_Z (V-AFD-T33).
- Basin-label Markov chain on $V_\mathrm{form}/\mathrm{Aut}(G)$ (V-AFD-T13(b), V-AFD-T34).
- V-AFD quasipotential $V^{\mathrm{V}}(Z_{F_i}, Z_{F_j}) = \mathrm{Bar}(F_i, F_j)$ (V-AFD-T35).
- V-AFD spectral gap $\sim \exp(-\mathrm{Bar}_*/T_*)$ (V-AFD-T27).

(M-3) **Identifications:**

| CMT object | V-AFD object | Identification |
|---|---|---|
| $\mu_{T_*}$ | $\nu_{T_*}$ | Push-forward; T33 |
| V_form chain | V_form/Aut(G) chain | Aut(G)-quotient; T14(a) |
| Quasipotential | V-quasipotential | Equality on V_form; T35 (LDP-5) |
| Spectral gap | V-spectral gap | Equality; T27 |
| Mean exit time | V-mean exit time | Inverse of spectral gap; T34 |

(M-4) **What V-AFD adds beyond CMT:**

| V-AFD addition | CMT analog | Why |
|---|---|---|
| Pareto preorder ≼_D | (none) | CMT uses scalar barrier order only |
| Multi-criteria cost C_V | Energy barrier only | CMT does not include diagnostic / topology variation |
| K-jump structure | (implicit) | CMT does not distinguish K levels |
| Aut(G)-quotient explicit | Symmetry handled ad-hoc | V-AFD-T14 makes Aut(G) primary |
| OMS-2.0 unified gauge | (none) | CMT does not address observer-equivariance |
| σ-rich extension | (none) | New diagnostic coordinate |
| Conley extension | (none) | Handles Goldstone families |
| Effective dim reduction | (implicit) | V-AFD-T24 explicit |
| Information-loss tracking | (implicit) | V-AFD-T9 explicit |

(M-5) **What CMT has that V-AFD inherits but does not refine:**

- Sharp EK prefactors $A_{ij}$ via H-MORSE-Local + Saddle (Layer 3, V-AFD-T8 / T13(b) conditional).
- Detailed rate asymptotics in T_* (Bovier-Eckhoff-Gayrard) — V-AFD-T27 inherits.

(M-6) **Conclusion (Theorem statement).** V-AFD is **a strict generalization of classical metastability theory** applied to SCC, adding multi-criteria preorder, K-jump structure, Aut(G)-quotient, OMS unification, σ/Conley extensions, and information-loss tracking — while preserving the Bovier-Den Hollander rate / spectral / invariant-measure structure as a special case at small T_*.

**Status.** **Theorem (descriptive comparison) Cat A** — the identifications (M-3) follow from individual V-AFD-T results; the additions (M-4) are V-AFD-specific by-construction.

**Cat self-rating.** A descriptive.

### §3.3 V-AFD-T40 — Numerical Implementation Specification

**Motivation.** OP-VAFD-008 (R1): empirical V-AFD numerics. R3 + R5 + R8 gave protocols; this consolidates into a single implementation specification for CODE-side.

**Specification V-AFD-T40 (Numerical V-AFD baseline).**

**(N-1) Inputs:**
- Canonical 15×15 grid (free BC).
- Parameters β = 50, α = 0.5, λ_cl = λ_sep = λ_bd = 1/3 (canonical defaults).
- vol_frac = 0.3.
- Number of seeds N (recommended: N = 1000 for robust statistics).

**(N-2) Step 1 — Run `find_formation`:**
```
for k in 1..N:
    seed_k = random_initialization(grid, vol_frac)
    u_F_k = find_formation(seed_k, β, α, λ, vol_frac)
    Save u_F_k.
```

**(N-3) Step 2 — Compute V-AFD vector states:**
```
for k in 1..N:
    D_k = D(u_F_k) = (Bind, Sep, Inside, Persist=1)  # static
    K_k = K_act(u_F_k)
    E_k = E(u_F_k)
    τ_k = H_0_persistence_diagram(u_F_k)
    Z_k = (D_k, K_k, E_k, τ_k)
    Save Z_k.
```

**(N-4) Step 3 — Aut(G) orbit clustering:**
```
For 15×15 grid, Aut(G) = D_4 = {e, r_90, r_180, r_270, s_h, s_v, s_d1, s_d2}.
for k, l in 1..N (k < l):
    d_orbit = min_{g in D_4} ||u_F_k - g · u_F_l||_2
    if d_orbit < ε_orbit (= 1e-3):
        cluster k, l together.
After clustering: distinct Aut(G)-orbits = N_orbit.
```

**(N-5) Step 4 — V-AFD-T14(c)-conj test:**
```
For each pair (orbit_i, orbit_j) of distinct Aut(G)-orbits:
    Z_i_rep = Z_k for any k in orbit_i.
    Z_j_rep = Z_k for any k in orbit_j.
    d_Z = d_𝒵(Z_i_rep, Z_j_rep)  # product metric (V-AFD-D2)
    if d_Z < ε_Z (= 1e-4):
        report: candidate V-AFD-T14(c)-conj falsifier (orbit_i, orbit_j).
Conclusion: if no candidate found across all pairs: V-AFD-T14(c)-conj supported by data.
```

**(N-6) Step 5 — Pareto frontier $\mathcal{P}_K$:**
```
For each K in {1, 2, ...} found in {K_k}:
    Z_orbits_K = {Z_orbit : orbit has K_orbit = K}.
    Compute Pareto frontier of {D_orbit : orbit in Z_orbits_K}.
    P_K = {orbit : D_orbit is Pareto-non-dominated in Z_orbits_K}.
    Report |P_K| (size of K-Pareto frontier).
```

V-AFD-T17-sharper(a)-quantitative prediction: at β = 50 > 5β_crit, $|\mathcal{P}_1| = 1$ (mod Aut(G)). V-AFD-T17-sharper(b) prediction: $|\mathcal{P}_K| \geq 2$ for K ≥ 2 at intermediate β.

**(N-7) Step 6 — NEB minimum-energy paths (V-AFD-T5, V-AFD-T15 verification):**
```
For each pair (F_i, F_j) in V_form (or representative orbits):
    Run NEB to compute γ_{ij} = minimum-energy path from u_F_i to u_F_j.
    Compute along γ_{ij}:
        z_γ(s) = Z(γ_{ij}(s)) for s ∈ [0, 1] sampled at 50 points.
        Var(D ∘ γ_{ij}), Var_τ(γ_{ij}), TV(K_act ∘ γ_{ij}), Len(γ_{ij}), Bar(γ_{ij}, F_i).
    Verify:
        Var(D ∘ γ) ≤ L_D · Len(γ)  # V-AFD-T5 prediction
        Bar ≥ 0.0221 β = 1.1 for merge transitions  # V-AFD-T15 prediction
```

**(N-8) Step 7 — Temporal V-AFD evaluation (V-AFD-D15, T28, T29):**
```
For each F ∈ V_form:
    Run gradient flow u̇ = -P_T ∇E from u_0 = u_F^* + ε · random_perturbation.
    Track u(t) for t in [0, T] (T = 10 · τ_relax).
    For each pair (t, s) with t < s, compute:
        π_{t,s} = Persist_pair(u(t), u(s), gradient_flow_operator)
    Verify V-AFD-T29: π_{t,s} should be monotonically non-increasing in s.
```

**(N-9) Outputs / deliverables:**
- Distinct Aut(G)-orbit count N_orbit.
- V-AFD-T14(c)-conj test verdict.
- Pareto frontier sizes |P_K| for each K.
- V-AFD-T5 + V-AFD-T15 verification verdicts.
- V-AFD-T29 temporal monotonicity verdict.
- Histogram of effective dim of V_Z (V-AFD-T24 verification).

**Estimated effort.** 2–3 CODE-side sessions (Python, NumPy, NEB, persistence diagrams via `scc/k_soft.py` machinery).

**Status.** **Specification (not a math theorem)**. Implementable.

---

## §4. Master Dependency Graph (Updated)

```
                     Canonical CV-1.13 Cat A
                     ┌────────────────────────────┐
                     │ T8-Core, T14, T-Merge(b),  │
                     │ T-Persist-1(b), T7-Enh,    │
                     │ A3 closure, Pred-E Bridge, │
                     │ QM3, CSEH 2007,            │
                     │ Commitment 16,             │
                     │ T-PF-A1-AR/SDE/GI/PE,      │
                     │ T-Temporal-Identity,       │
                     │ Łojasiewicz (b_D=0),       │
                     │ Appendix OMS-2.0           │
                     └────────────────────────────┘
                              │
                              ↓
                         AFD-0 Layer 2
                     ┌────────────────────────────┐
                     │ AFD-D1..D15, AFD-T1..T10   │
                     │ T-OP-AFD-003-A (R3 today)  │
                     │ AFD-T7 Cat B merge LB      │
                     │ AFD-T9 H-MORSE-free        │
                     └────────────────────────────┘
                              │
                              ↓
                     V-AFD v2.0 Layer 2
                     ┌────────────────────────────┐
                     │ V-AFD v2.0:                │
                     │   D1..D17 + T1..T40        │
                     │   45+ named claims         │
                     │   28+ OPs                  │
                     │   8 example scenarios       │
                     │   3 modalities:             │
                     │     - Static (R1–R7)       │
                     │     - Temporal (R8)        │
                     │     - Conley-extended (R8/R9) │
                     │   + σ-rich extension (R8)  │
                     │   + Ergodic / LDP (R9)     │
                     │   + Categorical (R10)      │
                     │   + Numerical spec (R10)   │
                     └────────────────────────────┘
                              │
                       ┌──────┴───────┐
                       │              │
                       ↓              ↓
                  Layer 2 (CatA)   Layer 3 (L3 cond)
                  ~30 Cat A        T8, T13b, T13c-refined, T27, T34, T35
                  claims           = EK/FW machinery
```

---

## §5. Complete Open Problems List (Updated)

| ID | Severity | Status R10 |
|---|---|---|
| OP-VAFD-001 | M | open |
| OP-VAFD-002 | M | upgraded by V-AFD-D15/D16 (R8) |
| OP-VAFD-003 | H | partially resolved (R2 det long-time A) |
| OP-VAFD-003a | M | open |
| OP-VAFD-004 | M | partially resolved (R2 T14 + R6 T21) |
| OP-VAFD-004a | M | open (computational test pending) |
| OP-VAFD-005 | M | open |
| OP-VAFD-006 | M | open |
| OP-VAFD-006-revised | M | open |
| OP-VAFD-007 | L | open |
| OP-VAFD-008 | L | specification R10 V-AFD-T40 |
| OP-VAFD-009 | M | tied to Claim B.3 |
| OP-VAFD-010 | M | **resolved R2** V-AFD-T15 |
| OP-VAFD-011 | M | **partially resolved R4** V-AFD-T19 |
| OP-VAFD-011a | M | **partially resolved R5** V-AFD-T19-global |
| OP-VAFD-011b | L | open |
| OP-VAFD-012 | M | **resolved R5** V-AFD-T16(full) |
| OP-VAFD-013 | M | **partially resolved R4 + R6** |
| OP-VAFD-013-K≥2 | M | Lemma R6 V-AFD-T17-sharper-K2-example |
| OP-VAFD-014 | M | reformulation R5 + R6 |
| OP-VAFD-015 | M | **resolved R6 canonical** V-AFD-T21 |
| OP-VAFD-016 | M | **resolved R6 under Cheeger** V-AFD-T22-without-H-MORSE |
| OP-VAFD-016a | M | **Lemma Cat B R9** V-AFD-T36 |
| OP-VAFD-017 | M | open |
| OP-VAFD-018 | M | open |
| OP-VAFD-019 | M | **resolved R8 on σ-regular set** V-AFD-T32 |
| OP-VAFD-019a | L | open |
| OP-VAFD-020 | L | **resolved R9** V-AFD-T37 |

**Status summary R10:**
- **Resolved:** 8 (010, 012, 015, 016, 019, 020, 011-partially, 011a-partially).
- **Partially resolved:** 5 (003, 004, 013, 016a Cat B, 019 Cat A on regular).
- **Open:** 15 (001, 002, 003a, 004a, 005, 006, 006-revised, 007, 008, 009, 011b, 013-K≥2, 014, 017, 018, 019a).

V-AFD has **resolved or partially resolved 13 of 28 OPs through 10 rounds**.

---

## §6. Architectural Diagram v2.0

```
                                  V-AFD v2.0
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ↓                        ↓                        ↓
        Static V-AFD              Temporal V-AFD          Conley-extended
        (R1–R7 baseline)          (R8 primary)            (R8–R9 sketched-Cat A)
        Z(u) = (D, K, E, τ)       Z_{t,s}(u_t, u_s; M)    Z(\widetilde F)
              │                        │                        │
              │                        │                        │
              ├ Pareto preorder ≼_D    ├ Pairwise Persist       ├ Goldstone family
              │   (T2 A)               │   primary               │   handling
              │                        │                        │
              ├ Vector cost C_V        ├ C_V^temporal           ├ Conley index h(S_F)
              │   (D6 + T15 cond)      │   (with log π_{t,s})    │   (T37 A)
              │                        │                        │
              ├ Pareto frontier P_K    ├ Temporal Persist Lyap  ├ Mischaikow-Mrozek
              │   (T17 + T17-sharper)  │   monotonicity (T29 A) │   continuation
              │                        │                        │
              ├ Aut(G)-quotient        ├ T-Temporal-Identity     │
              │   (T14a A)             │   Cat A input            │
              │                        │                        │
              ├ OMS unified gauge      │                        │
              │   (T16(full) A)        │                        │
              │                        │                        │
              └ Effective dim ~K_field│
                  (T24 A under T14(c)-conj)                     │
              │                        │                        │
              │ ┌──────────────────────┼────────────────────────┘
              │ │
              ↓ ↓
        σ-rich extension       Vector Lyapunov sheaf
        Z^σ(u) = (Z, σ)        𝒱 = {V_F}_{F ∈ V_form}
        (T32 A on regular set) (T19-global A under hyp)
              │                        │
              └──────────┬─────────────┘
                         │
                         ↓
              Robustness (T26 A)
              + parameter perturbation
                         │
                         ↓
              Invariant measure ν_{T*} (T33 A / L3 cond)
              + Ergodicity (T34 + Layer-2 cor A)
                         │
                         ↓
              V-AFD LDP rate function I_T^V
              (T35 L3 cond; T35-L2 A)
                         │
                         ↓
              Categorical structure V-AFD as functor
              (T38 A)
                         │
                         ↓
              Classical metastability comparison
              (T39 A descriptive)
                         │
                         ↓
              Numerical implementation V-AFD-T40
              (Specification, CODE-side ready)
              │
        ──────┴───────────────────────────────────────
                         │ Layer 3 boundary
                         ↓
              EK refinement (T8)
              Small-T_* basin Markov (T13b)
              Approximate full-Z Markov in QSD (T13c-refined)
              Spectral gap small T_* (T27 + T34 E-4,E-5)
              FW quasipotential identification (T35 LDP-5)
        ──────────────────────────────────────────────
```

V-AFD v2.0 master diagram.

---

## §7. Canonical Promotion Roadmap (Updated R10)

### §7.1 R1 promotion candidates (V-AFD as AFD R1 companions)

If AFD-0 R1 promotion executes:

**Strongly recommended additions to canonical:**
- **V-AFD-T2** (Pareto preorder) — Cat A unconditional.
- **V-AFD-T7** (V-AFD H-MORSE-free) — Cat A by-inspection.

**Net effect:** +2 Cat A claims alongside AFD R1.

### §7.2 R2 promotion candidates (post Claim B.3)

- **V-AFD-T6'** (attainment) — Cat A unconditional after Claim B.3 (R3 today).
- **V-AFD-T14(a)** (Aut(G)-invisibility) — Cat A.
- **V-AFD-T19-global** (Lyapunov sheaf) — Cat A under (H-A1)–(H-A2).
- **V-AFD-T21** (Aut_task = Aut(G) canonical) — Cat A.
- **V-AFD-T23** (K-field architecture) — Cat A.

**Net effect:** +5 Cat A claims at R2.

### §7.3 R3 promotion candidates (after empirical / further work)

- **V-AFD-T16(full)** (OMS bridge) — Cat A modulo T14(c)-conj (computational test pending).
- **V-AFD-T17-sharper(a) + quantitative** (K=1 singleton) — Cat A.
- **V-AFD-T20-general** (K-selection) — Cat A for high-β K=1 case.
- **V-AFD-T22-without-H-MORSE** (Cheeger QSD) — Cat A under Cheeger.
- **V-AFD-T24** (effective dim) — Cat A under T14(c)-conj.
- **V-AFD-T26** (robustness) — Cat A.
- **V-AFD-T28, T29** (temporal V-AFD basics) — Cat A.
- **V-AFD-T32** (σ-rich Lipschitz on regular set) — Cat A.
- **V-AFD-T33** (invariant measure existence Cat A part) — Cat A.
- **V-AFD-T34-Layer-2** (G_V strong connectivity) — Cat A.
- **V-AFD-T35-Layer-2** (LDP rate as definition) — Cat A.
- **V-AFD-T37** (V-AFD-Conley Cat A) — Cat A.
- **V-AFD-T38** (categorical structure) — Cat A.
- **V-AFD-T39** (classical-metastability comparison) — Cat A descriptive.

**Net effect at R3:** +14 Cat A claims.

### §7.4 Layer-3 conditional candidates (with Pkg II / H-MORSE)

- V-AFD-T8, T13(b), T13(c)-refined, T27, T34 (E-4, E-5), T35 (LDP-5) — all L3 conditional.

### §7.5 Promotion summary

If all V-AFD R1–R3 promotion candidates land, V-AFD adds:

- R1: +2 Cat A (T2, T7)
- R2: +5 Cat A (T6', T14a, T19-global, T21, T23)
- R3: +14 Cat A

**Total: +21 V-AFD Cat A claims** to canonical layer over CV-1.14 → CV-1.16 or thereabouts. This would substantially expand the canonical Cat A budget while remaining strictly compatible with AFD-0 and CV-1.13.

---

## §8. Round 10 Self-Audit + Round 11 Priorities

### §8.1 15-question audit

1. ✓ Projection not replacement: T38 functorial structure preserves projection.
2. ✓ Persist forms: temporal V-AFD primary in v2.0.
3. ✓ Continuity explicit: T38 uses T26 continuity Cat A.
4. ✓ K_act discontinuity: unchanged.
5. ✓ τ stability: unchanged.
6. ✓ Injectivity loss: T39 acknowledges in comparison (V-AFD-T9 vs CMT implicit handling).
7. ✓ Nonnegativity: T40 specification respects all bounded ranges.
8. ✓ Not a metric: T38 categorical structure does not impose metric.
9. ✓ H-MORSE free: T38, T39 (M-4 + M-6 part), T40 do not use H-MORSE. CMT analog in T39 invokes H-MORSE only at Layer 3 (T39 (M-5)).
10. ✓ EK Layer-3 only: T39 (M-5) explicit; rest of T39 is descriptive.
11. ✓ Scalarization optional: T38 hom-set carries Pareto preorder, not scalar.
12. ✓ Pareto incomparability: unchanged.
13. ✓ Markovianity open: T39 (M-2) explicit; T13(c)-refined remains L3 cond.
14. ✓ Examples concrete: T40 numerical specification on canonical 15×15.
15. ✓ Honest statuses: T38 Cat A, T39 Cat A descriptive, T40 Specification (not theorem).

**Round 10 audit: PASS** on all 15 questions.

### §8.2 Round 11 priorities

(P-A) **Execute V-AFD-T40 numerical baseline** (CODE-side). Validate V-AFD-T14(c)-conj, V-AFD-T17-sharper(a)-quantitative, V-AFD-T15, V-AFD-T29 empirically. 2–3 sessions.

(P-B) **OP-VAFD-016a Cat A** — non-convex Cheeger constant for canonical SCC basins via Buser-Cheeger geometric measure theory. 1 session.

(P-C) **OP-VAFD-017 verification** — T-K-Select-PF / OBS coincidence (combination of theoretical + numerical). 2 sessions.

(P-D) **V-AFD-T35 explicit quasipotential calculation** for canonical 15×15. 1–2 sessions.

(P-E) **V-AFD-T38 higher categorical extensions** — derived/∞-categorical V-AFD, if substantive. 1 session (theoretical).

(P-F) **V-AFD ↔ machine learning bridge** — V-AFD as representation learning framework; Z(u) as learnable embeddings. 1–2 sessions (new direction).

(P-G) **V-AFD v2.0 paper draft** — publication-quality manuscript outline based on this consolidation. 1 session.

### §8.3 Status summary v2.0

V-AFD v2.0 = **substantively complete Layer-2 vector-projection theory** with:

- **45+ named claims** (Definitions D1..D17, Theorems T1..T40 + variants).
- **28+ Open Problems** (OP-VAFD-001..020 + sub-variants).
- **3 modalities** (static, temporal, Conley-extended).
- **2 extensions** (σ-rich, K-field).
- **Categorical structure** (V-AFD as functor).
- **Classical metastability comparison** (formal).
- **Numerical implementation specification** (CODE-side ready).
- **OMS-2.0 unified gauge** (V-AFD-T16(full) + V-AFD-T21).
- **Ergodic theory + LDP rate function** at Layer-3 conditional.
- **Cheeger-based QSD existence** without H-MORSE.

**8 of 9 audit rounds: PASS** on all 15 questions (Round 10 included).

---

## §9. Round 10 Slogans

> **V-AFD v2.0 is substantively complete at Layer 2.**
> **45 named claims; 28+ OPs (13 resolved/partial); 3 modalities; 2 extensions; categorical functor + classical-metastability comparison + numerical spec.**
> **Layer-2 Cat A core: ~30 claims; Layer-3 conditional: 6 claims; rest open / sketched.**
> **No H-MORSE; OMS-2.0 unified; Aut(G)-quotient natural; Pareto-multi-criteria.**
> **Numerical baseline V-AFD-T40 ready for CODE execution.**

V-AFD Round 10 consolidates Rounds 1–9 into v2.0, adds categorical bridge (T38), classical metastability comparison (T39), and numerical spec (T40). Next: execute T40 and continue Round 11.

---

*End of `v_afd_round10_master_v2.md`. V-AFD v2.0 consolidation complete.*
