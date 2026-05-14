---
type: working/reading-log
created: 2026-05-08
session: Session 5 (VP-6 + OP-OMS-018)
project: Observer Moduli Space of SCC
stage: OMS-1.1 → OMS-1.2 candidate
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# VP-6 Initial Reading Log — Session 5

Records the OMS state at session start (post-VP-4 / OMS-1.1) and the
information used to design VP-6 and the OP-OMS-018 attack.

---

## §1. Current OMS State (read 2026-05-08, Session-5 start)

### Documents read

| Path | Status snapshot |
|---|---|
| `oms_1_candidate.md` | OMS-1.1 — Computationally Grounded Canonical Candidate; G_cw={e} COMP. SUPPORTED; V_adm ≠ ∅ HYPOTHESIZED; Prop BS1 COMP. CONFIRMED; formal blocker = OP-OMS-018 |
| `oms_1_1_promotion_audit.md` | Two-track: Track 1 (Computationally Grounded Canonical Candidate) ADOPTED |
| `definitions.md` | DEF-1…DEF-22 stable; DEF-19 (d_eff) and DEF-22 (J_P) directly relevant to VP-6 |
| `open_problems.md` | OP-OMS-001 (G_cw): COMP. SUPPORTED, formal proof open. OP-OMS-002 (V): HYP. OP-OMS-009 RESOLVED-NEGATIVE. OP-OMS-010(c) COMP. SUPPORTED. OP-OMS-016 / 018 are the VP-6 / OP-OMS-018 targets. |
| `audit_log.md` | AUDIT-001..AUDIT-022; W11 (continuity of u*) still open |
| `validation_protocols.md` | VP-6 spec: 200 grid points; finite-difference Jacobian; SVD; d_eff(ε) for ε∈{0.01,0.05,0.1} |
| `core_weight_symmetry.md` (read indirectly via VP-3 audit) | Prop CW2 CONFIRMED — λ_tr is gauge on static scenes |
| `basin_stratification.md` (via VP-4 summary) | Prop BS1 COMP. CONFIRMED on S3 (Δd=0.40) and S4 (Δd=0.52); P1 (cl-dominant) is a distinct type |
| `daily_log.md` | Sessions 1–4 logged; Session-5 priority = VP-6 + OP-OMS-018 |
| `checkpoints.md` | All OMS-0.x checkpoints COMPLETE; VP-1/3/2/4 complete; VP-6 next |
| `CODE/experiments/exp86_vp1_p_resolution_audit.py` | reference: P_min coarseness CEs |
| `CODE/experiments/exp87_vp3_core_weight_symmetry.py` | reference: λ-space transformation API (uses ParameterRegistry.w_cl/w_sep/w_bd/w_tr) |
| `CODE/experiments/exp88_vp4_basin_stratification.py` | reference: STRATEGIC_POINTS dict, eval_point pattern |
| `CODE/experiments/results/observer_moduli/vp1_pairs.json` | 4 CEs (CE-1: λ_A=(0.6,0.2,0.2,0), λ_B=(0.5,0.3,0.2,0), Δd=0.071, K_core 2 vs 1) |
| `CODE/experiments/results/observer_moduli/vp3_symmetry_results.json` | 7 transforms; A NOT_A_SYMMETRY; E (transport ablation) CANDIDATE_SYMMETRY |
| `CODE/experiments/results/observer_moduli/vp4_basin_results.json` | S3: 2 types; S4: 2 types; cl-dominant produces n_high=0 on S4 |

### Code architecture noted

- `scc.params.ParameterRegistry`: weights are `w_cl`, `w_sep`, `w_bd`, `w_tr` (NOT `lambda_*`). Mass via `volume_fraction`.
- `scc.optimizer.find_formation(graph, params)`: deterministic given `params` (multi-start uses `seed=r` for `r ∈ range(n_restarts)`); returns `FormationResult(u, energy, energy_terms, diagnostics, converged, n_iter, ...)`.
- `scc.diagnostics`: `_persistence_h0_graph(u, graph) → (l_max, l_second)` is exposed (private but importable). `diagnostic_vector(u, graph, params)` returns the 4-vector.
- On static scenes, `persist = 1.0` always (Persist predicate fall-back when `u_prev=None`), confirming Prop CW2 at the diagnostic level.

---

## §2. Plan for VP-6

### Smooth components for Jacobian

Given the W11 caveat in `audit_log.md` and the OP-OMS-018 obstruction (phase
transitions in $u^*$), the Jacobian is well-defined only on regular branches.
We decline to mix discrete and continuous components. For VP-6 we use:

$$R_{\mathrm{vec}}(\lambda) = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist}, \ell_{\max}, \ell_{\mathrm{sec}}, A, c_{\max}) \in \mathbb{R}^8$$

where:

- $\mathrm{Bind, Sep, Inside, Persist}$ are the standard diagnostic vector entries.
- $\ell_{\max}, \ell_{\mathrm{sec}}$ are the longest / second-longest H0 bars (continuous).
- $A = \ell_{\max} - \ell_{\mathrm{sec}}$ is the articulation gap (continuous; on a regular branch).
- $c_{\max} = \max_i u^*_i$ is the peak amplitude (continuous on regular branches).

We also record the **discrete** quantities $K_{\mathrm{core}}$, $n_{\mathrm{high}} = |\{i : u_i > 0.5\}|$
as **diagnostics for branch identification** but exclude them from $R_{\mathrm{vec}}$ used in the Jacobian.

### Tangent basis on the simplex

#### Static face $\Delta^2 = \{\lambda_{cl} + \lambda_{sep} + \lambda_{bd} = 1, \lambda_{tr} = 0\}$ (recommended primary):

Orthonormal basis of $T_\lambda \Delta^2 = \{v \in \mathbb{R}^3 : \sum v_i = 0\}$:

$$e_1 = \frac{1}{\sqrt{2}}(1, -1, 0), \quad e_2 = \frac{1}{\sqrt{6}}(1, 1, -2)$$

#### Full simplex $\Delta^3$ (4-weights):

$$e_1 = \tfrac{1}{\sqrt{2}}(1,-1,0,0), \quad e_2 = \tfrac{1}{\sqrt{6}}(1,1,-2,0), \quad e_3 = \tfrac{1}{\sqrt{12}}(1,1,1,-3)$$

These are orthonormal in $\mathbb{R}^k$, and span the tangent space (kernel of
$\mathbf{1}^\top$). We perturb $\lambda \to \lambda \pm h \cdot e_i$ with $h=10^{-3}$,
project back if any coordinate becomes negative, and compute centered finite
differences.

### Sample points

Inherit the strategic 6 from VP-4 (P1..P6) plus the VP-1 CE pair and a small
random sample. Concretely $\sim 12$ points per scene on $\{S3, S4\}$, in both
the static-face and full-simplex variants.

### Effective dimension thresholds

$\varepsilon \in \{10^{-3}, 10^{-2}, 5\cdot 10^{-2}, 10^{-1}\}$, both absolute
and relative to $\sigma_1$.

### Branch-aware reporting

For each $\lambda$ we record $K_{\mathrm{core}}$, $n_{\mathrm{high}}$, and energy. If a perturbation
$\lambda \pm h e_i$ flips $K_{\mathrm{core}}$ or $n_{\mathrm{high}}$, the centered FD is contaminated
across a branch — we flag it as `branch_jump` and SVD only the FDs that
remain on the same branch.

---

## §3. Plan for OP-OMS-018 attack

### Setup

$$\Omega = \Sigma_m \cap [0,1]^n, \quad \Sigma_m = \{u \in \mathbb{R}^n : \mathbf{1}^\top u = m\}.$$

For fixed scene $X_t$, the SCC energy on $\Omega$ as a function of observer weights $\lambda$:

$$E_\lambda(u) = \sum_i \lambda_i \, E_i(u; X_t), \quad i \in \{cl, sep, bd, tr\}.$$

This is **affine** in $\lambda$, and **non-convex** in $u$ (closure resolvent is nonlinear, double-well boundary term is non-convex).

### Theorem targets

- **R1 (interior IFT branch):** Local $C^1$ regularity of $\lambda \mapsto u^*(\lambda)$ at a non-degenerate interior critical point.
- **R2 (boundary IFT branch):** Piecewise $C^1$ under fixed active set + strict complementarity.
- **R3 (Berge upper hemicontinuity):** Global Argmin correspondence is u.h.c. (no Lipschitz expected).
- **R4 (value function regularity):** $v(\lambda) = \min_u E_\lambda(u)$ is **continuous and concave** (infimum of affine functions).
- **R5 (envelope):** Where unique and regular, $\partial v/\partial \lambda_i = E_i(u^*(\lambda))$.

### Status forecast

OP-OMS-018 will end the session as **PARTIALLY RESOLVED**: local regularity
proved on regular branches; global uniqueness/$C^1$ rejected because of
branch switching surfaces (= observer-type transitions, by VP-4 and VP-1
evidence).

---

## §4. Files I will create/update

- `vp6_effective_dof.md` — VP-6 results writeup
- `vp6_effective_dof_log.md` — execution log
- `effective_dof_theory.md` — definitional / propositional foundation
- `op_oms_018_regular_u_star.md` — regularity proofs / sketches
- `oms_1_2_status_audit.md` — OMS status after VP-6 + OP-OMS-018
- `experiments/observer_moduli/vp6_effective_dof_jacobian.py` — main FD-Jacobian script
- `experiments/observer_moduli/vp6_u_star_regular_path_test.py` — path regularity test
- `results/observer_moduli/vp6_jacobian_spectra.json`, `vp6_effective_dof_summary.md`
- `results/observer_moduli/vp6_u_star_path_results.json`, `vp6_u_star_path_summary.md`
- updates: `open_problems.md`, `audit_log.md`, `daily_log.md`, `checkpoints.md`,
  `THEORY/CHANGELOG.md`, `THEORY/working/INDEX.md`,
  `observer_landscape_admissible_class.md`, `basin_stratification.md`,
  `stratified_dynamics.md`, `canonical_promotion_checklist.md`.

(Note: there is no `experiments/observer_moduli/` directory yet — the existing
experiments live under `CODE/experiments/`. To stay consistent with the
repository convention used by exp86–exp88, the VP-6 scripts will be placed
under `CODE/experiments/observer_moduli/` (new sub-dir) and the result files
under `CODE/experiments/results/observer_moduli/`.)
