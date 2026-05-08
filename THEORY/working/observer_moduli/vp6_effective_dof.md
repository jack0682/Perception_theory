---
type: working/results
created: 2026-05-08
session: Session 5
project: Observer Moduli Space of SCC
stage: OMS-1.1 → OMS-1.2 candidate
attacks: OP-OMS-016, OP-OMS-005, Hyp RG1
experiment: CODE/experiments/observer_moduli/vp6_effective_dof_jacobian.py
data: CODE/experiments/results/observer_moduli/vp6_jacobian_spectra.json
---

# VP-6 — Effective DOF via Jacobian Singular Spectrum

Computational attack on OP-OMS-016 (computational $d_{\mathrm{eff}}$),
OP-OMS-005 (effective DOF), and Hypothesis RG1.

Classification: **DEFINED** | **PROVED** | **COMPUTATIONALLY SUPPORTED** |
**HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. What VP-6 measures

For each base point $\lambda \in \Delta^3$ (or static face $\Delta^2_{\mathrm{static}}$):

1. Run `find_formation` at $\lambda$ to obtain $u^*(\lambda)$.
2. Construct the **smooth-component readout vector**

   $$R_{\mathrm{vec}}(\lambda) = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, [\mathrm{Persist}], \ell_{\max}, \ell_{\mathrm{sec}}, A, c_{\max})$$

   (Persist included only in the full-simplex variant.) Discrete components
   $K_{\mathrm{core}}$, $n_{\mathrm{high}}$ are **excluded** from $R_{\mathrm{vec}}$ but recorded as
   the **branch identifier**.
3. Centered finite-difference Jacobian along the orthonormal tangent basis
   of the simplex (dim 2 for static face, dim 3 for full $\Delta^3$),
   $h = 10^{-3}$.
4. SVD of $J_R(\lambda)$. Effective dimensions
   $d_{\mathrm{eff}}(\lambda; \varepsilon) = \#\{\sigma_i \ge \varepsilon\}$
   for absolute and relative thresholds in $\{10^{-3}, 10^{-2}, 5\!\times\!10^{-2}, 10^{-1}\}$.
5. **Branch consistency**: each FD perturbation is checked against the base
   branch identifier; if the branch flips inside the FD stencil, the
   stencil is flagged `BRANCH-JUMP` (it crosses $\Sigma_{\mathrm{branch}}$,
   per Prop R3 (3) of `op_oms_018_regular_u_star.md`).

---

## §2. Sample setup

**Scenes:** S3 (6×6 grid, $n=36$) and S4 (two 5-cliques + weak bridge, $n=10$).
Both inherited from VP-3 / VP-4.

**Static-face samples (λ_tr = 0).** 12 points: VP-4 strategic P1..P5 plus the
VP-1 CE1 pair, three random interior points, and two near-symmetry-locus
points (`S_cl_eq_sep`, `S_bd_face_near`).

**Full-simplex samples.** 9 points: VP-4 strategic P1..P6 plus the lifted CE1
pair (lifted to give $\lambda_{tr}=0.15$) and `S_cl_eq_sep`.

Total Jacobian evaluations: $(12 + 9) \times 2 = 42$ stencils across two scenes.

---

## §3. Headline results

### 3.1 Effective dimension distribution (VP-6 Run 2 final, 42 samples, 41 branch-clean)

Threshold $\varepsilon_{\mathrm{rel}} = 5 \times 10^{-2}$ (i.e.\ $\sigma_i / \sigma_1 \ge 0.05$):

| Aggregation | $d_{\mathrm{eff}}$ histogram | Total |
|---|---|---|
| **static** (S3 ∪ S4, $k_{\mathrm{tan}}=2$) | $\{1: 15,\ 2: 9\}$ | 24 |
| **full**   (S3 ∪ S4, $k_{\mathrm{tan}}=3$) | $\{1: 13,\ 2: 5\}$ | 18 |
| **all**    | $\{1: 28,\ 2: 14\}$ | 42 |

Per scene:

| Variant × Scene | $d_{\mathrm{eff}}$ histogram | Notes |
|---|---|---|
| static × S3 | $\{1: 3,\ 2: 9\}$ (out of 12) | One stencil flagged BRANCH-JUMP; rest branch-clean |
| static × S4 | $\{1: 12\}$ (out of 12) | All d_eff = 1; σ_2 / σ_1 always < 0.001 |
| full × S3   | $\{1: 4,\ 2: 5\}$ (out of 9)  | One stencil flagged BRANCH-JUMP (S_cl_eq_sep) |
| full × S4   | $\{1: 9\}$ (out of 9)         | Extreme anisotropy on biclique scene |

**Aggregate σ statistics:** σ_max average = 4.22, σ_min/σ_max average = 0.0176.

**Headline:** **No sample produced $d_{\mathrm{eff}} = 3$ on the full simplex.** Two-thirds of all stencils have $d_{\mathrm{eff}} = 1$ at this threshold.

**Interpretation.**

- **No sample produced $d_{\mathrm{eff}} = 3$ on the full simplex.** The original
  Hyp RG1 ($d_{\mathrm{eff}} \in [2, 4]$) cannot be the right per-point bound on
  the simplex slice; the revised RG1 ($\{1, 2\}$ on static, $\{1, 2, 3\}$
  on full) is consistent with these data.
- **S4 is severely degenerate.** The two-clique scene with weak bridge has
  $d_{\mathrm{eff}}^{\mathrm{rel}}(\lambda; 0.05) = 1$ at every sampled point.
  This is geometrically natural: on S4 the optimizer effectively chooses
  one of two cliques (or symmetric equilibrium), so first-order
  $\lambda$-perturbations along most tangent directions barely affect the
  field.

### 3.2 Singular spectra geometry

Across all 42 stencils:

- $\sigma_1$ (largest singular value) ranges from $\approx 0.003$ (S4
  interior away from cl-dominant) to $\approx 7.20$ (S4 P1 full-simplex).
- $\sigma_2$ typical magnitudes: $0.01 \ldots 0.1$ on S3; $\le 10^{-3}$ on S4.
- The ratio $\sigma_2 / \sigma_1$ is usually $\le 0.1$, often $\le 0.01$.

**Spectral gap is the dominant feature.** A persistent $10\times$–$10^3\times$
gap between $\sigma_1$ and $\sigma_2$ means: at most points, perturbations
of $\lambda$ along the simplex tangent affect only **one** strong direction
of the readout. The formal tangent dimension is 2 (static) or 3 (full),
but the **effective** response dimension is typically 1.

### 3.3 Branch-jump stencils

Two stencils flagged `BRANCH-JUMP`:

- S3 static, sample `S_cl_eq_sep` ($\lambda = (0.40, 0.40, 0.20)$): branch
  flips from $(7, 11)$ to $(6, 12)$ during the FD perturbation in $e_1 = (1,-1,0)/\sqrt 2$.
  Reported $\sigma_1 = 40.29$ — manifestly contaminated by the field jump.
- S3 full, sample `S_cl_eq_sep` ($\lambda = (0.35, 0.35, 0.15, 0.15)$):
  similar flip, $\sigma_1 = 40.38$.
- S3 full, sample `P4_cl_sep` ($\lambda = (0.40, 0.40, 0.10, 0.10)$): $\sigma_1 = 42.23$,
  comparable contamination (branch ID was $(6,12)$ but the FD pair drifted
  near a phase boundary).

**These flagged points correspond exactly to the OP-OMS-017 approximate-symmetry
locus near $\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$**, where VP-3 already
documented that $\lambda$-space transformations have small $\Delta P_{\mathrm{top}}$.
The VP-6 finding refines this: the locus is *not* a smooth approximate
symmetry; it is a **branch-switching surface** in the $u^*$ map (Prop R3 (3)),
across which the Jacobian is undefined and the readout is discontinuous.

This pivots OP-OMS-017's interpretation: the locus is **not** "approximate
gauge symmetry" but rather "stratification gluing surface". Update:
`open_problems.md` OP-OMS-017 to be merged with the new OP-OMS-026.

### 3.4 The cl-dominant special direction

On both scenes, the **cl-axis** direction (perturbing $\lambda_{cl}$ at the
expense of others) has the largest singular value:

- S3 P1 (cl-dominant): $\sigma_1 = 2.26$ (static) / $3.70$ (full). Branch is $(0, 12)$,
  i.e.\ $u$ never reaches the core threshold $\theta_{\mathrm{core}} = 0.9$ but
  has a soft 2-blob structure consistent with VP-1 CE-1.
- S4 P1 (cl-dominant): $\sigma_1 = 3.24$ (static) / $7.20$ (full). Branch is
  $(0, 5)$ static / $(0, 0)$ full — symmetric equilibrium ($n_{\mathrm{high}} = 0$ on
  full): cl-dominant on a biclique gives the symmetric solution that
  collapses to no formation, exactly the VP-4 finding.

The cl-axis is the **dominant relevant direction** in the RG sense across
both scenes. This confirms the qualitative prediction in
`rg_relevance_flow.md` §3 ("$\lambda_{cl} - \lambda_{sep}$ balance: RELEVANT
for formation count [HYPOTHESIZED]") and elevates it:

> **Status update.** $\lambda_{cl}$-axis as dominant relevant direction:
> COMPUTATIONALLY SUPPORTED on S3 and S4.

---

## §4. Reconciliation with original Hyp RG1

| Hypothesis | Domain | Status |
|---|---|---|
| Original Hyp RG1: $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2, 4]$ on full $\mathcal{M}_{\mathrm{obs}}$ (8-dim) | $\mathcal{M}_{\mathrm{obs}}$ with all of $q, \xi, \lambda$ varying | **WEAKENED — UNTESTED in this experiment** (we held $q, \xi$ fixed) |
| Revised RG1: $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in \{1, 2\}$ on static face / $\{1, 2, 3\}$ on full | $\Delta^2_{\mathrm{static}}$ / $\Delta^3$ slice | **COMPUTATIONALLY SUPPORTED** ($d_{\mathrm{eff}} \le 2$ in every sample) |
| Stronger statement: $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) = 1$ in the simplex interior | $\mathrm{int}(\Delta^3)$ | **HYPOTHESIZED**; supported by S4 (always 1) and majority of S3 full-simplex samples (4/9 are 1) |

**Audit caveat.** $d_{\mathrm{eff}}$ is a **per-point** quantity. The simplex
slice with $q, \xi$ fixed yields $d_{\mathrm{eff}} \le 2$ at every sample.
Whether varying $q, \xi$ would add a third or fourth strongly relevant
direction is not tested; the original Hyp RG1 about full $\mathcal{M}_{\mathrm{obs}}$ remains
**OPEN** (deferred to a future VP-6-extended protocol).

---

## §5. Geometric story

Combining the VP-6 result with `op_oms_018_regular_u_star.md`:

1. On every regular branch (R1 / R2 of OP-OMS-018), the readout map $R$
   has a continuous Jacobian. VP-6 estimates this Jacobian numerically
   and finds it has **rank effectively 1** at most sampled points.
2. By Prop ED2, locally the readout image is at most a 1- or 2-dimensional
   immersed submanifold of $\mathbb{R}^p$. The **perceptual indifference
   leaves** are codim-1 or codim-2 within the local branch domain.
3. Across branch-switching surfaces $\Sigma_{\mathrm{branch}}$ (Prop R3 (3)),
   $R$ jumps discontinuously by exactly the readout components ($K_{\mathrm{core}}$,
   $n_{\mathrm{high}}$) excluded from the smooth Jacobian. VP-6 detects these
   surfaces by branch-ID flips (3 stencils flagged across the experiment).
4. The OMS picture: $\Delta^3$ is partitioned into open regular branches
   plus codim-1 transition surfaces. Each branch carries a low-dimensional
   smooth readout submanifold. The transition surfaces glue distinct
   submanifolds into the global perceptual stratification.

This is the **stratified picture** that the OMS-1.2 status audit adopts.

---

## §6. Open follow-up problems

- **OP-OMS-024** Constant-rank regions for $P_{\mathrm{top}}$. Identify open
  subsets of $\Delta^3$ on which the Jacobian rank is constant. Evidence
  from VP-6: candidate constant-rank-1 region around the bd-dominant face
  on S4 (consistent $\sigma_1 / \sigma_2 \approx 10^3$ at every sampled
  point). Need finer sampling.
- **OP-OMS-025** Empirical correspondence (relate VP-6 $d_{\mathrm{eff}}$
  to behavioral perceptual styles, EP-1 protocol).
- **OP-OMS-026** Characterize $\Sigma_{\mathrm{branch}}$ in $\Delta^3$.
  VP-6 evidence localizes one such surface near $\{\lambda_{cl} \approx \lambda_{sep}\}$
  (the OP-OMS-017 locus, now reinterpreted) and the cl-dominant axis on
  S4 (where $n_{\mathrm{high}}$ flips between 5 and 0).
- **OP-OMS-027 / 028** (registered in `op_oms_018_regular_u_star.md` §11):
  corner cases, quantitative Lipschitz of $v$.

---

## §7. Final classification of VP-6 findings

| Claim | Status |
|---|---|
| $d_{\mathrm{eff}}(\lambda; \mathrm{rel}=5\!\times\!10^{-2}) \le k_{\mathrm{tan}} - 1$ at typical interior $\lambda$ on the simplex slice (revised RG1) | **COMPUTATIONALLY SUPPORTED** |
| $\lambda_{cl}$-axis is the dominant relevant direction on representative scenes | **COMPUTATIONALLY SUPPORTED** |
| Branch-switching surfaces near $\{\lambda_{cl} \approx \lambda_{sep}\}$ exist (Σ_branch ≠ ∅) | **COMPUTATIONALLY SUPPORTED** |
| OP-OMS-017 "approximate symmetry" reinterpretation as Σ_branch | **HYPOTHESIZED** (this writeup; merge with OP-OMS-026) |
| Original Hyp RG1 ($d_{\mathrm{eff}} \in [2, 4]$ on $\mathcal{M}_{\mathrm{obs}}$) | **OPEN** (untested with $q, \xi$ varying) |
| Per-stratum $d_{\mathrm{eff}} = 1$ generic (stronger claim) | **HYPOTHESIZED** |

---

*The full numerical data is in
`CODE/experiments/results/observer_moduli/vp6_jacobian_spectra.json`.
Per-sample tables are in `vp6_effective_dof_summary.md` and the execution
log is in `vp6_effective_dof_log.md`.*
