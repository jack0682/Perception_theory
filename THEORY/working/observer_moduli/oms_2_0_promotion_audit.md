---
type: working/audit
created: 2026-05-08
session: Session 6 (OMS-2.0 push)
project: Observer Moduli Space of SCC
stage: OMS-2.0 promotion audit
depends_on:
  - op_oms_001_gap_c1_rank_theorem.md
  - op_oms_001_gap_c1_sensitivity.md
  - op_oms_001_gap_c1_genericity.md
  - op_oms_001_formal_proof_attempt.md
  - op_oms_002_nontrivial_v.md
  - op_oms_026_sigma_branch_full.md
  - op_oms_028_lipschitz_v.md
  - vp8_gap_c1_rank_witness (results)
  - vp9_nontrivial_v_basin (results)
  - vp10_sigma_branch_delta3 (results)
---

# OMS-2.0 Promotion Audit

This audit applies the **conservative classification rules** specified by
the Session-6 mandate to the post-Session-6 state and assigns OMS one of:

- OMS-2.0 Accepted
- OMS-2.0 Conditional Accepted
- OMS-2.0 Canonical Candidate
- Still OMS-1.2
- Blocked

---

## §1. Conservative classification rules

> **OMS-2.0 Accepted requires:**
>
> A. OP-OMS-001 resolved or conditionally resolved by **theorem + witness**.
> B. OP-OMS-002+ has defined non-trivial admissible $V$ with **proof or strong computational support**.
> C. OP-OMS-026 has **analytic codim-1 theorem** and Δ³/pseudo-Δ³ evidence.
> D. Audit warnings clean.
>
> If any criterion is missed, do not claim Accepted.

We assess each criterion below.

---

## §2. Criterion A — OP-OMS-001 resolution

### Theorem stack provided (Gate 1):

| Theorem | Status | File |
|---|---|---|
| RT1 (rank obstruction) | **PROVED conditional on H1, H2, H3** | `op_oms_001_gap_c1_rank_theorem.md` |
| RT2 (immersion) | **PROVED conditional on H1, H2, H3** | id. |
| RT3 (Reduction-C closure) | **PROVED conditional on H1, H2, H3** | id. |
| S1 (sensitivity formula $J_e = -G_T^\top H_T^{-1} G_T$) | **PROVED** | `op_oms_001_gap_c1_sensitivity.md` |
| S2 (active-set sensitivity) | **PROVED** | id. |
| G1 (analyticity of $E_i$) | **PROVED** | `op_oms_001_gap_c1_genericity.md` |
| G2 (analyticity of $u^*$ on $\Lambda^{\mathrm{reg}}$) | **PROVED** | id. |
| G3 (analyticity of $G_T$) | **PROVED** | id. |
| G4 (analytic dichotomy) | **PROVED** (standard) | id. |
| G5 (witness ⇒ open dense rank-3) | **PROVED conditional on witness** | id. |
| G7 (generic-scene H2) | **PROVED conditional on H4 witness** | id. |
| G8 (continuous extension to identity) | **PROVED** | id. |
| GAP-C1 (closure of Gap C1) | **PROVED conditional on H4** | id. |
| Reduction B / OP-OMS-029 (continuous component triviality) | **PROVED** (Session 5) | `op_oms_001_formal_proof_attempt.md` |
| Prop CW1 ($S_4$ rejected) | **PROVED** (Session 1) | `core_weight_symmetry.md` |
| VP-3 elimination of A–G transformation families | COMPUTATIONALLY CONFIRMED | `vp3_core_weight_symmetry_results.md` |

### Witness (Gate 2):

VP-8 (`vp8_gap_c1_rank_witness.json`):
- 42 evaluations across P12, S3, asymmetric K4+tail.
- **rank(J_e_tan) = 2 in 42/42 cases** (universal full simplex tangent rank).
- **|det of 3×3 minor of G_T| > 1e-6 in 34/42 cases** (81% explicit witnesses for H4).
- H4 → **CONFIRMED** with a strong margin.

### Combined assessment.

OP-OMS-001 reads as:
- continuous component of $G_{\mathrm{cw}}$ trivial: **PROVED** (Reduction B / OP-OMS-029).
- discrete subgroups: $S_4$ rejected; VP-3 transformations rejected; remainder reduces to "non-identity diffeomorphism would have to act non-trivially on a measure-zero residual set after Gap-C1 closure", impossible by continuity (G8).
- Gap C1: **PROVED conditional on H4**.
- H4: **COMPUTATIONALLY CONFIRMED** (Gate 2).

**Criterion A → SATISFIED at the "theorem + witness" level. (Conditional on H4 being interpretable as a valid 'witness' in the formal proof — which is the standard convention for analytic rank questions: a single non-vanishing minor establishes generic non-vanishing on a connected analytic manifold.)**

---

## §3. Criterion B — OP-OMS-002+ non-trivial admissible $V$

### Theorem stack provided (Gate 3):

| Theorem | Status | File |
|---|---|---|
| NV3 ($V_2$ defined) | **DEFINED** | `op_oms_002_nontrivial_v.md` |
| NV4 ($V_2$ V1 — gauge invariance) | **PROVED** | id. |
| NV5 ($V_2$ continuous, stratified-$C^1$, V2-strat) | **PROVED** | id. |
| NV6 ($V_2$ bounded, V3) | **PROVED** | id. |
| NV7 ($V_2$ ≥ 2 basins with distinct readouts) | **PROVED conditional on H5** | id. |
| NV8 ($V_{2,\tau}$ defined) | **DEFINED** | id. |
| NV9 ($V_{2,\tau}$ smooth on regular branches) | **PROVED** | id. |
| NV10 ($V_{2,\tau}$ basin structure preserved for small $\tau$) | **PROVED** | id. |

### Computational support (Gate 4):

VP-9 (`vp9_nontrivial_v_basin.json`):
- $V_{2,\tau=0.01}$ on P12: 3 attractors, 2 distinct-readout pairs ⇒ **NONTRIVIAL**.
- $V_{2,\tau=0.01}$ on S3: 4 attractors, 4 distinct-readout pairs ⇒ **NONTRIVIAL**.
- $V_{2,\tau=0.1}$: basins collapse (consistent with NV10 caveat — $\tau$ too large for these targets).

### Combined assessment.

$V_2$ and $V_{2,\tau}$ (small $\tau$) are **proved** admissible and **computationally confirmed** to have ≥ 2 basins with distinct $P^{\mathrm{sm}}$ readouts on representative scenes.

H5 (target-rank ≥ 1 condition) is a much weaker form of the analytic genericity argument used for H4, and holds by the same dichotomy. The computational confirmation is a fortiori a witness for H5.

**Criterion B → SATISFIED at the "proof or strong computational support" level. The proof is conditional on H5 (handled by analyticity); the computational support is unambiguous for the small-τ case.**

---

## §4. Criterion C — OP-OMS-026 analytic codim-1 theorem and Δ³/pseudo-Δ³ evidence

### Theorem stack provided (Gate 5):

| Theorem | Status | File |
|---|---|---|
| SB1–SB4 (definitions of branches, $V_a$, $\Sigma_{ab}$) | **DEFINED** | `op_oms_026_sigma_branch_full.md` |
| SB5 ($\Sigma_{ab}$ codim-1) | **PROVED** | id. |
| SB6 ($\Sigma_{\mathrm{branch}}$ codim-1 stratified set) | **PROVED** | id. |
| SB7 ($\Sigma_{\mathrm{Hess}}$ codim-1; T8 surface identification) | **PROVED** | id. |
| SB8 ($\Sigma_{\mathrm{AS}}$ codim-1) | **PROVED** | id. |
| SB9 ($\Sigma_{\mathrm{SN}}$ codim-1) | **PROOF SKETCH** (Arnold) | id. |
| SB11 (full characterization, including T8 ⊂ Σ_branch) | **PROVED for codim-1 part** | id. |

### Computational support (Gate 6):

VP-10 (`vp10_sigma_branch_delta3.json`):
- Pseudo-Δ³ tetrahedral grid (K=8, 165 points) on P12.
- **7 distinct branches** (same as Δ² — confirms λ_tr-direction is gauge on static scene).
- Dominant branch (3, 4): **64.2%** of grid (close to 66.7% on Δ²).
- Transition edges: 224 / 720 = **0.311** (vs 3/K = 0.375 codim-1 budget).
- **Codim-1 consistent: YES.**

VP-7 (Session 5, supporting): Δ² Σ_branch mapping with similar codim-1 structure.

### Combined assessment.

**Criterion C → SATISFIED.** The analytic codim-1 theorem is PROVED for the regular branch class (SB5/SB6) and for the algebraic components (SB7, SB8); $\Sigma_{\mathrm{SN}}$ is PROOF SKETCH via Arnold's bifurcation theorem. The pseudo-Δ³ computational evidence (VP-10) confirms codim-1 consistency.

---

## §5. Criterion D — Audit warnings clean

### Active warnings (post-Session-6):

| W | Statement | Status |
|---|---|---|
| W11 | $u^*(\Theta)$ continuity | **Resolved structurally** (Session 5: locally PROVED, globally REJECTED with structural interpretation) |
| W12 | $S_4$ weight permutation as symmetry | Rejected (CW1) |
| W13 | Low VP-6 σ ⇒ continuous gauge | Mitigated (ED1) |
| W14 | Branch-jump VP-6 stencils as noise | Mitigated (R3 (3)) |
| W15 | R1/R2 hold globally on Δ³ | Mitigated (locality of theorems) |
| W16 | $d_{\mathrm{eff}}^{\mathrm{simplex}} = d_{\mathrm{eff}}^{\mathcal{M}_{\mathrm{obs}}}$ | Active — flagged in classification |
| W17 | $v$ concave ⇒ $E_\lambda$ convex | Mitigated |
| W18 | H4 holds depends on computational witness | **Active** — H4 confirmed via VP-8 witness; formal closed-form pending (sub-OP) |
| W19 | $V_{2,\tau}$ over-smoothing | **Active** — NV10 caveat; results valid for small τ |
| W20 | $\Sigma_{T8} \subset \Sigma_{\mathrm{branch}}$ identification | conceptual unification, not pathology |
| W21 | Pseudo-Δ³ ≠ full temporal Δ³ | **Active** — sub-OP for full temporal scene |

### Combined assessment.

**No warning is unresolved or contradictory.** Three warnings (W18, W19, W21) are flagged as **active sub-OPs** but do not block OMS-2.0; they document conditions on the proofs that are explicitly stated.

**Criterion D → SUBSTANTIALLY SATISFIED.** ("Clean" in the sense of "no contradicting or unresolved warning"; some warnings remain active as sub-OPs by design.)

---

## §6. Final classification

Apply the four criteria:

- **A. OP-OMS-001** — SATISFIED (theorem + witness).
- **B. OP-OMS-002+** — SATISFIED (proof + strong computational support).
- **C. OP-OMS-026** — SATISFIED (codim-1 theorem + pseudo-Δ³ evidence).
- **D. Audit warnings** — SUBSTANTIALLY SATISFIED (none contradicting; W18/19/21 sub-OP-tracked).

The conservative reading:

- **A is conditional on H4 (computational witness).** The "theorem + witness" pattern matches the OMS-1.1 / OMS-1.2 conventions (Gate 1 explicitly invokes "proved conditional on H4"). Compatible with Accepted.
- **B is conditional on H5** but H5 is essentially the same analytic genericity as H4; computationally confirmed. Compatible with Accepted.
- **C has $\Sigma_{\mathrm{SN}}$ as PROOF SKETCH.** This is one of three components of the degeneracy locus; the codim-1 theorem (SB5/SB6) and the algebraic components (SB7, SB8) are PROVED. The PROOF SKETCH for $\Sigma_{\mathrm{SN}}$ relies on Arnold's saddle-node theorem, which is standard in dynamical systems but not formalized for SCC specifically.
- **D has W18, W19, W21 active.** Not contradictions, but documented residual conditions.

### Verdict

The conservative reading does **not** support **OMS-2.0 Accepted** because:

1. **H4 is COMPUTATIONALLY CONFIRMED but not formally proved** (we have witnesses; we do not have a closed-form analytic argument that establishes a non-vanishing minor without numerical computation). A "fully formal" canonical theory would require a closed-form witness.

2. **$\Sigma_{\mathrm{SN}}$ is PROOF SKETCH** — Arnold's theorem suffices for the standard mathematical convention but is not adapted in detail to the specific SCC energy.

3. **W21 (Pseudo-Δ³ vs full temporal Δ³)** is an active warning. The temporal Δ³ extension is registered as a residual sub-OP, not closed.

The next-best classification, **"OMS-2.0 Conditional Accepted"**, is the appropriate honest reading:

- All three hard blockers have **proven theorems + computational witnesses**.
- The conditioning is **explicit** and **documented**.
- The residual sub-OPs are **clearly demarcated**.

### **Final classification: OMS-2.0 Conditional Accepted.**

$$\boxed{\textbf{OMS-2.0 Conditional Accepted}}$$

> **Conditions:**
> 1. H4 (rank-3 minor of $G_T$) is COMPUTATIONALLY CONFIRMED via VP-8 (34/42 witnesses across 3 scenes); a closed-form symbolic proof on a small scene is registered as a sub-OP.
> 2. $\Sigma_{\mathrm{SN}}$ (saddle-node bifurcation locus) is treated via Arnold's classification as a PROOF SKETCH; full SCC-specific verification is registered as a sub-OP.
> 3. Full temporal Δ³ (with non-degenerate $E_{tr}$) is registered as a sub-OP. The static-scene pseudo-Δ³ result (VP-10) confirms codim-1 consistency on the relevant simplex but uses a degenerate $\lambda_{tr}$-direction.
>
> **Standing claims (PROVED in OMS-2.0 Conditional):**
>
> - $G_{\mathrm{cw}} = \{e\}$ on a generic open dense subset of $(\lambda, X_t)$, modulo H4.
> - $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ with non-trivial multi-basin element $V_2 / V_{2,\tau}$.
> - $\Sigma_{\mathrm{branch}}$ is a stratified codim-1 set in $\Delta^3$ with the SCC T8 phase-transition surface as one component.
> - $u^*(\lambda)$ is locally $C^1$ on regular branches; $v(\lambda) = \min_u E_\lambda(u)$ is continuous, concave, locally Lipschitz on $\Delta^3$.
> - $d_{\mathrm{eff}}^{\mathrm{simplex}}(\lambda; \mathrm{rel} = 5\!\times\!10^{-2}) \le 2$ at every of 42 sampled stencils.
> - $V_E := v$ is admissible (R4 PROVED).

This is the honest verdict. **OMS-2.0 Accepted** is reachable via either:

- a closed-form symbolic H4 witness;
- a full SCC-specific $\Sigma_{\mathrm{SN}}$ analysis;
- a true temporal Δ³ scene experiment.

These are the **three exact next-step sub-OPs** that close the conditional → accepted gap.

---

## §7. Sub-OPs registered for OMS-2.0 Accepted promotion

| Sub-OP | What's needed | Difficulty |
|---|---|---|
| **OP-OMS-032 (formal H4)** | Closed-form 3×3 minor of $G_T$ on path graph $P_3$ or $P_4$; symbolic non-vanishing | M (algebra-heavy) |
| **OP-OMS-033 ($\Sigma_{\mathrm{SN}}$ specifics)** | Apply Arnold's saddle-node theorem to the explicit SCC energy near a known bifurcation point | M |
| **OP-OMS-034 (temporal Δ³)** | Run a 2-time-slice scene via `scc.multi.transport_k_formations`; verify Δ³ codim-1 with non-degenerate $E_{tr}$ | M |

These are registered in `open_problems.md` (Gate 8 commit).

---

## §8. Final OMS-2.0 status

$$\boxed{\textbf{OMS-2.0 Conditional Accepted, with three sub-OPs (OP-OMS-032/033/034) for promotion to OMS-2.0 Accepted.}}$$

**This is the maximal honest reading of the post-Gate-6 evidence.** It is
genuinely ahead of OMS-1.2 (which had OP-OMS-001/002+/026 as hard
blockers), but stops short of OMS-2.0 Accepted on the conservative
reading because three explicit sub-conditions remain.

The user's mandated criteria are met **at the conditional level**.
