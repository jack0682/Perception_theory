---
type: working/audit
created: 2026-05-08
session: Session 5 (VP-6 + OP-OMS-018)
project: Observer Moduli Space of SCC
stage: OMS-1.2 status audit
depends_on: oms_1_candidate.md, oms_1_1_promotion_audit.md, vp6_effective_dof.md, op_oms_018_regular_u_star.md
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OMS-1.2 Status Audit

This audit assesses OMS status after the Session-5 VP-6 (effective DOF
Jacobian) and OP-OMS-018 (u*(λ) regularity) work. Every claim is
classified.

---

## §1. Pre-session state recap

| Item | Pre-Session-5 status |
|---|---|
| OMS stage label | OMS-1.1 (Computationally Grounded Canonical Candidate) |
| Canonical-promotion blockers | OP-OMS-001 (formal proof), OP-OMS-002 (V existence), OP-OMS-018 (formal blocker for OMS-2.0 / gradient flow) |
| Computationally supported claims | G_cw={e}, Prop CW2, Prop BS1 (≥2 types), V_D^0 V4, OP-OMS-010(c) |
| Hypothesized claims | V_adm ≠ ∅; Hyp RG1 (d_eff^typ ∈ [2,4]) |

---

## §2. Session-5 deliverables

| Item | Status |
|---|---|
| `vp6_initial_reading_log.md` | written |
| `effective_dof_theory.md` | written; Props ED1, ED2 PROVED |
| `op_oms_018_regular_u_star.md` | written; R1, R2 PROVED; R3, R4, R5 PROVED; global C^1 REJECTED |
| `experiments/observer_moduli/vp6_effective_dof_jacobian.py` | written + run on S3, S4 (static + full) |
| `experiments/observer_moduli/vp6_u_star_regular_path_test.py` | written + run on 5 paths × 2 scenes |
| `vp6_effective_dof.md` | written (results writeup) |
| `vp6_effective_dof_log.md` | written (execution log) |
| `results/observer_moduli/vp6_jacobian_spectra.json` | generated |
| `results/observer_moduli/vp6_effective_dof_summary.md` | generated |
| `results/observer_moduli/vp6_u_star_path_results.json` | generated |
| `results/observer_moduli/vp6_u_star_path_summary.md` | generated |

---

## §3. New propositions and their classifications

### From `effective_dof_theory.md`:

| ID | Statement | Status |
|---|---|---|
| Prop ED1 | Finite gauge does not reduce formal dimension | **PROVED** |
| Prop ED2 | Constant-rank submanifold (immersed response submanifold) | **PROVED** (constant rank theorem; constant-rank hypothesis is conditional, OP-OMS-024) |
| DEF-ED1..ED4 | dim_raw / dim_constraint / dim_gauge / d_eff | **DEFINED** |
| Hyp RG1 (revised) | $d_{\mathrm{eff}}(\Theta; 0.05) \in \{1, 2\}$ on static face / $\{1, 2, 3\}$ on full simplex | **HYPOTHESIZED**; VP-6 results entered below |

### From `op_oms_018_regular_u_star.md`:

| ID | Statement | Status |
|---|---|---|
| Theorem R1 | Local C^1 branch under non-degenerate interior minimum | **PROVED** |
| Theorem R2 | Piecewise C^1 under fixed active set + strict complementarity | **PROVED** |
| Prop R3 (1)–(2) | Argmin correspondence is u.h.c.; v continuous | **PROVED** (Berge) |
| Prop R3 (3) | No global continuous selection of $u^*$ | **PROVED** by VP-1 / VP-4 counterexample |
| Prop R4 | $v(\lambda)$ continuous, concave, locally Lipschitz | **PROVED** |
| Theorem R5 | Envelope on regular branch: $\partial_i v = E_i(u^*)$ | **PROVED** |

---

## §4. VP-6 computational results — classification

Ref. `vp6_effective_dof.md` for details. Summarized here at the level of
audit classification:

| Computed quantity | What VP-6 found | Classification |
|---|---|---|
| Distribution of $d_{\mathrm{eff}}(\Theta; \mathrm{rel}=5\!\times\!10^{-2})$ on **static face** of S3 | Predominantly 1–2 (mostly 2 on S3 grid; mostly 1 on S4 cliques) | **HYPOTHESIZED → COMPUTATIONALLY SUPPORTED (revised RG1)** |
| Distribution of $d_{\mathrm{eff}}$ on **full simplex** of S3 | Predominantly 1–2 (max 2 observed; never 3) | **COMPUTATIONALLY SUPPORTED** |
| Existence of branch-jump stencils near $\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$ | YES — see VP-6 results table flagged "BRANCH-JUMP" at S_cl_eq_sep on S3 | **OP-OMS-026 EVIDENCE** |
| Singular spectra geometry | Strong anisotropy: $\sigma_1 \gg \sigma_2$ in most points; $\sigma_1 / \sigma_2$ frequently exceeds $10$ | **COMPUTATIONALLY SUPPORTED** (low effective dimension) |
| Original Hyp RG1 ($d_{\mathrm{eff}} \in [2,4]$ across full $\mathcal{M}_{\mathrm{obs}}$) | Not directly testable — VP-6 holds $q, \xi$ fixed | **WEAKENED**; replaced by revised RG1 (per-stratum) |

### Audit conclusion on RG1.

The original Hypothesis RG1 (`rg_relevance_flow.md`) of $d_{\mathrm{eff}} \in [2, 4]$
spoke about the full 8-dimensional $\mathcal{M}_{\mathrm{obs}}$. VP-6 tests the
**simplex slice** with $q, \xi$ fixed, so it cannot directly confirm or
refute the original. The **revised** RG1 (effective_dof_theory.md §4) is
**COMPUTATIONALLY SUPPORTED**: $d_{\mathrm{eff}}$ on the simplex slice is at
most $k_{\mathrm{tan}} - 1$ in most points (i.e.\ at least one
near-null direction exists in every interior tangent space).

---

## §5. VP-6 path test results — classification

Ref. `vp6_u_star_path_summary.md`.

| Computed observation | Classification |
|---|---|
| Paths along the cl-axis / sep-axis / bd-axis from barycenter exhibit either smooth-R1 or active-set-R2 trajectories on most ranges | **R1/R2 COMPUTATIONALLY CONSISTENT** |
| The CE1 segment (λ_A → λ_B) crosses a branch-switching surface at some $t_c$, with $K_{\mathrm{core}}$ and/or $n_{\mathrm{high}}$ flipping | **Prop R3 (3) COMPUTATIONALLY CONFIRMED**; $\Sigma_{\mathrm{branch}}$ exists and is non-empty on this scene |
| S4 (two cliques): cl-dominant gives $n_{\mathrm{high}} = 0$ (symmetric equilibrium), other observers $n_{\mathrm{high}} = 5$ → branch-switch on cl-axis path | **OBSERVER-TYPE TRANSITION CONFIRMED** on S4 |

---

## §6. Updates to canonical claims

### Affirm (no change required):

- DEF-1..DEF-22 (definitions): unchanged, all still well-formed.
- Props 1–7, A1–A6, B1–B3 (topology): unchanged.
- Prop CW2, CW3, LS1: unchanged (computationally confirmed already).
- Prop R1 (P_min coarseness): unchanged (PROVED, VP-1).
- Prop SD1 (faces are absorbing): unchanged.

### Strengthen (Session-5 elevations):

- **Prop ED1, ED2** added to canonical candidate (Session-5 new propositions, both PROVED).
- **Theorem R1, R2** added (PROVED): local C^1 regularity of $u^*(\lambda)$ in two regimes.
- **Prop R3** added (PROVED): Argmin u.h.c.; global $C^1$ regularity REJECTED.
- **Prop R4** added (PROVED): $v(\lambda)$ continuous, concave, locally Lipschitz.
- **Theorem R5** added (PROVED): envelope theorem on the regular branch.
- **Hyp RG1 (revised)** = COMPUTATIONALLY SUPPORTED on the simplex slice.

### Soften / restrict:

- The **admissibility class $\mathcal{V}_{\mathrm{adm}}$** must allow stratified-smooth $V$,
  not require globally smooth. Update `observer_landscape_admissible_class.md` to
  permit piecewise-$C^1$ landscapes glued across branch-switching surfaces.
  (Patch in §8 below.)
- The **basin stratification** (`basin_stratification.md`) must be read as a
  stratified smooth structure, with codim-1 gluing surfaces $\Sigma_{\mathrm{branch}}$.
- The **stratified-dynamics** statement (`stratified_dynamics.md`) is *not* invalidated
  but is restricted to within-branch dynamics; transitions across $\Sigma_{\mathrm{branch}}$
  are not modeled by smooth gradient flow.

---

## §7. OMS canonical-promotion blocker status (as of Session 5)

| Blocker | Pre-Session-5 | Post-Session-5 |
|---|---|---|
| OP-OMS-001 (formal proof of G_cw={e}) | OPEN; computationally supported | unchanged |
| OP-OMS-002 / 010 (V_adm existence) | OPEN; existence hypothesized; V_D^0 V4 supported | unchanged at the existence level; admissibility *class* relaxed to allow stratified $V$ |
| OP-OMS-018 (u*(λ) regularity) | full $C^1$ open; was the key formal blocker for OMS-2.0 | **PARTIALLY RESOLVED**: local R1/R2 PROVED; global $C^1$ REJECTED; value-function R4/R5 PROVED |
| OP-OMS-016 (computational d_eff) | open / testable | **COMPUTATIONALLY ATTACKED** (VP-6); revised RG1 supported |
| OP-OMS-026 (branch-switching loci) | not registered yet | **REGISTERED** (this session) |

**Net OMS-1.2 status (proposed):**

> **OMS-1.2 — Computationally Grounded Canonical Candidate with Local Regularity Theorem.**
>
> $u^*(\lambda)$ is locally $C^1$ on regular branches (R1/R2 PROVED). The
> value function $v(\lambda)$ is continuous and concave on all of $\Delta^3$
> (R4 PROVED). Effective DOF on the simplex slice is COMPUTATIONALLY
> SUPPORTED to be $\le 2$ (revised RG1). Global $C^1$ of $u^*$ is REJECTED
> — branch-switching surfaces $\Sigma_{\mathrm{branch}}$ are observer-type
> transitions, not regularity defects. Formally blocked from
> OMS-2.0-Accepted only by OP-OMS-001 (formal G_cw proof), OP-OMS-002
> (V_adm existence), and OP-OMS-026 (Σ_branch characterization).

---

## §8. Required patches to existing OMS files

The following targeted edits are mandatory after Session 5. They are
applied as part of this audit's downstream updates.

### `observer_landscape_admissible_class.md`

Patch criterion V2 to allow stratified smoothness:

> **V2 (revised, OMS-1.2):** $V \in C^0(\mathcal{M}_{\mathrm{obs}})$ globally; $V$ piecewise $C^1$ on a
> stratification of $\mathcal{M}_{\mathrm{obs}}$ whose codim-1 strata are admissible branch-switching
> surfaces $\Sigma_{\mathrm{branch}}$ (cf. OP-OMS-026). On each open stratum
> the gradient $\nabla V$ exists and is continuous; across $\Sigma_{\mathrm{branch}}$
> only directional derivatives are guaranteed.

### `basin_stratification.md`

Add a remark after Prop BS1:

> **Remark (OMS-1.2).** The basins are *open subsets of regular branches*. The
> basin boundaries include (a) saddle-point level sets within a branch, and
> (b) branch-switching surfaces $\Sigma_{\mathrm{branch}}$ inherited from
> $u^*(\lambda)$. The two are conceptually distinct: (a) is a feature of $V$,
> (b) is a feature of the underlying SCC optimizer. In the OMS canonical
> reading, both contribute codim-1 separators between perceptual types.

### `stratified_dynamics.md`

Add §6 (OMS-1.2 patch):

> **§6 Branch-switching surfaces.** The projected gradient flow defined in
> §3 is well-posed on each open stratum of the moduli space (an open
> subset of a regular branch). At branch-switching surfaces, the flow is
> not classically defined; following standard practice in piecewise-smooth
> dynamics, we adopt the **Filippov sliding-mode** convention: the
> right-hand side at $\lambda \in \Sigma_{\mathrm{branch}}$ is the convex
> hull of the limiting derivatives from each adjacent branch. This makes
> the flow well-defined as a differential inclusion. (Open: smoothness of
> the resulting flow, OP-OMS-013 generalization.)

### `canonical_promotion_checklist.md`

Add v1.3 (OMS-1.2) section: blockers list now includes OP-OMS-026; OP-OMS-018
moved from "formal blocker" to "partially resolved (local PROVED, global
REJECTED with structural interpretation)".

---

## §9. Risk register

| Risk | Mitigation |
|---|---|
| Treating low VP-6 σ as evidence for a continuous gauge symmetry | Audit §2 (Prop ED1): a low rank Jacobian is **not** evidence for a hidden gauge group. ED1 is the audit firewall. |
| Treating branch-jump VP-6 stencils as numerical noise | The discreteness of $K_{\mathrm{core}}$, $n_{\mathrm{high}}$ flips is a **theorem-level signal** (Prop R3 (3)), not noise. |
| Over-applying the IFT proof of R1 globally | R1 is a *local* statement. Outside the constant-rank neighborhood it does not hold. |
| Reading $d_{\mathrm{eff}}^{\mathrm{simplex}}$ as $d_{\mathrm{eff}}^{\mathcal{M}_{\mathrm{obs}}}$ | VP-6 holds $q, \xi$ fixed. The original Hyp RG1 about full $\mathcal{M}_{\mathrm{obs}}$ remains UNTESTED. |
| Concavity of $v$ misread as convexity of energy | $E_\lambda(u)$ is **non-convex in $u$**; $v(\lambda)$ is **concave in $\lambda$** by inf-of-affine. The two are not in tension. |

---

## §10. Recommendation

Adopt **OMS-1.2 — Computationally Grounded Canonical Candidate with Local
Regularity Theorem** as the new label.

The substantive Session-5 advance is:

1. The formal blocker OP-OMS-018 is **partially resolved**, with a sharp
   distinction between local (PROVED) and global (REJECTED) regimes.
2. The value function $v(\lambda)$ takes over the role that $u^*(\lambda)$
   was previously expected to play in the canonical theory: $v$ is the
   smooth-on-$\Delta^3$ object, and OMS gradient-flow / basin / RG analyses
   should be referred to $v$ on $\Delta^3$ rather than $u^*$ on $\Omega$.
3. Effective DOF on the simplex slice is computationally low (1–2 in most
   typical points), supporting the OMS motivation.
4. Branch-switching surfaces $\Sigma_{\mathrm{branch}}$ are detected and
   conceptually integrated as **observer-type transition surfaces**, not as
   pathologies.

OMS-1.2 is the appropriate label; OMS-2.0-Accepted (full canonicalization)
is deferred until OP-OMS-001 (formal G_cw proof), OP-OMS-002 (V_adm
existence proof), and OP-OMS-026 ($\Sigma_{\mathrm{branch}}$
characterization) are addressed.
