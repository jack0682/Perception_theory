---
type: working/log
created: 2026-05-08
session: Session 5
project: Observer Moduli Space of SCC
script: CODE/experiments/observer_moduli/vp6_effective_dof_jacobian.py
---

# VP-6 Execution Log

Chronological record of the VP-6 Jacobian experiment runs and the
adjustments that were made.

---

## Run 1 (2026-05-08, ~09:00 local)

- Command: `cd CODE && python3 experiments/observer_moduli/vp6_effective_dof_jacobian.py`
- Status: per-sample evaluation completed for both scenes and both variants;
  script crashed at the final aggregation stage with
  `KeyError: 'abs_5e-02'` — the bug was that `aggregate_d_eff(per_scene, key="abs_5e-02")`
  routed through `row["d_eff_rel"]` instead of `row["d_eff_abs"]`.
- Per-sample stdout was captured and used to seed the writeup
  (`vp6_effective_dof.md`). Numerical Jacobians were computed correctly
  (the bug was downstream of the per-sample work); the numbers stayed valid.

### Key per-sample numbers (Run 1, S3 static):

| label | branch (n_core, n_high) | σ_1 | σ_2 | d_eff(rel,5e-2) | flagged |
|---|---|---|---|---|---|
| P1_cl_dominant     | (0, 12) | 2.2596 | 0.1257 | 2 | clean |
| P2_sep_dominant    | (10, 12) | 0.4658 | 0.0081 | 1 | clean |
| P3_balanced        | (6, 12) | 0.6043 | 0.0564 | 2 | clean |
| P4_cl_sep          | (6, 12) | 0.4190 | 0.0029 | 1 | clean |
| P5_bd_dominant     | (6, 12) | 0.4443 | 0.0258 | 2 | clean |
| CE1_lambda_A       | (2, 12) | 1.2584 | 0.0900 | 2 | clean |
| CE1_lambda_B       | (6, 12) | 0.7296 | 0.0824 | 2 | clean |
| R1_random          | (6, 12) | 0.7328 | 0.0770 | 2 | clean |
| R2_random          | (6, 12) | 0.1138 | 0.0083 | 2 | clean |
| R3_random          | (6, 12) | 0.5293 | 0.0381 | 2 | clean |
| S_cl_eq_sep        | (7, 11) | 40.2858 | 0.1942 | 1 | **BRANCH-JUMP** |
| S_bd_face_near     | (6, 12) | 0.4178 | 0.0214 | 2 | clean |

### Key per-sample numbers (Run 1, S3 full):

| label | branch | σ_1 | σ_2 | σ_3 | d_eff(rel,5e-2) | flagged |
|---|---|---|---|---|---|---|
| P1_cl_dominant     | (0, 8)  | 3.7031  | 0.0262 | 0.0080 | 1 | clean |
| P2_sep_dominant    | (10, 12) | 1.0677  | 0.0106 | 0.0000 | 1 | clean |
| P3_balanced        | (6, 12) | 0.8146  | 0.0773 | 0.0000 | 2 | clean |
| P4_cl_sep          | (6, 12) | 42.2327 | 0.3406 | 0.0009 | 1 | (large σ_1; near-symmetry locus) |
| P5_bd_dominant     | (6, 12) | 0.4715  | 0.0273 | 0.0000 | 2 | clean |
| P6_tr_dominant     | (6, 12) | 2.0308  | 0.2076 | 0.0048 | 2 | clean |
| CE1_lambda_A       | (0, 12) | 2.2252  | 0.1442 | 0.0004 | 2 | clean |
| CE1_lambda_B       | (6, 12) | 0.8963  | 0.0957 | 0.0001 | 2 | clean |
| S_cl_eq_sep        | (6, 12) | 40.3787 | 0.2712 | 0.0052 | 1 | **BRANCH-JUMP** |

### Key per-sample numbers (Run 1, S4 static):

All but cl-dominant land in the regime $\sigma_1 \approx 0.003$, $\sigma_2 \approx 10^{-5}$ — extreme rank-1 anisotropy:

| label | branch | σ_1 | σ_2 | d_eff |
|---|---|---|---|---|
| P1_cl_dominant     | (0, 5) | 3.2410 | 0.0009 | 1 |
| P2_sep_dominant    | (0, 5) | 0.0050 | 0.0000 | 1 |
| P3_balanced        | (0, 5) | 0.0029 | 0.0000 | 1 |
| P4_cl_sep          | (0, 5) | 0.0029 | 0.0000 | 1 |
| P5_bd_dominant     | (0, 5) | 0.0029 | 0.0000 | 1 |
| CE1_lambda_A       | (0, 5) | 2.1257 | 0.0010 | 1 |
| CE1_lambda_B       | (0, 5) | 0.0024 | 0.0000 | 1 |
| R1..R3_random      | (0, 5) | 0.0024..0.0040 | 0.0000 | 1 |
| S_cl_eq_sep        | (0, 5) | 0.0027 | 0.0000 | 1 |
| S_bd_face_near     | (0, 5) | 0.0029 | 0.0000 | 1 |

### Key per-sample numbers (Run 1, S4 full):

| label | branch | σ_1 | σ_2 | σ_3 | d_eff |
|---|---|---|---|---|---|
| P1_cl_dominant     | (0, 0) | 7.2031 | 0.0007 | 0.0000 | 1 |
| P2_sep_dominant    | (0, 5) | 0.0066 | 0.0000 | 0.0000 | 1 |
| P3_balanced        | (0, 5) | 0.0038 | 0.0000 | 0.0000 | 1 |
| P4_cl_sep          | (0, 5) | 0.0029 | 0.0000 | 0.0000 | 1 |
| P5_bd_dominant     | (0, 5) | 0.0033 | 0.0000 | 0.0000 | 1 |
| P6_tr_dominant     | (0, 5) | 0.0092 | 0.0000 | 0.0000 | 1 |
| CE1_lambda_A       | (0, 5) | 3.0742 | 0.0012 | 0.0000 | 1 |
| CE1_lambda_B       | (0, 5) | 0.0031 | 0.0000 | 0.0000 | 1 |
| S_cl_eq_sep        | (0, 5) | 0.0033 | 0.0000 | 0.0000 | 1 |

---

## Run 2 (2026-05-08, post-fix)

- Bug fix applied to `aggregate_d_eff`: route through `d_eff_rel`/`d_eff_abs`
  based on the key prefix.
- Re-ran the experiment to obtain the JSON / markdown outputs.
- Numerical results match Run 1 (deterministic optimizer; multi-start uses
  fixed seeds, see `scc/optimizer.py: _optimize_single(..., seed=r)`).
- Total elapsed: ~10 min on the development machine.

JSON output: `CODE/experiments/results/observer_moduli/vp6_jacobian_spectra.json`.
Markdown summary: `CODE/experiments/results/observer_moduli/vp6_effective_dof_summary.md`.

---

## Notes on numerical robustness

1. **Determinism.** `find_formation` is deterministic given the same
   `ParameterRegistry` (multi-start uses `seed=r` for $r \in \{0, \ldots, n_{\mathrm{restarts}}-1\}$).
   Therefore the FD Jacobian is reproducible.
2. **FD step.** $h = 10^{-3}$ in the orthonormal tangent basis. We did not
   sweep $h$; future work should verify Jacobian stability under $h \in \{10^{-4}, 10^{-3}, 10^{-2}\}$.
3. **Tangent basis orthonormality.** Confirmed via `np.linalg.norm` per row;
   the basis vectors $T_3 \in \mathbb{R}^{2 \times 3}$ and $T_4 \in \mathbb{R}^{3 \times 4}$
   are unit-norm and pairwise orthogonal.
4. **Branch-jump filter.** When the FD pair lands on different branches, the
   reported Jacobian column is contaminated. We *do not* exclude the
   contaminated column from the SVD; we only **flag** the stencil. Reading
   the data: ignore $\sigma$-values from flagged stencils when estimating
   $d_{\mathrm{eff}}$ — they reflect a discrete jump rather than a
   smooth-direction sensitivity.
5. **Persist degeneracy.** On static scenes (with $\lambda_{tr} = 0$ in the
   static variant, or the optimizer ignoring temporal terms in the full
   variant on a single time-slice graph), `Persist = 1.0` is fixed. Hence
   the Persist column of the Jacobian contributes zero by construction.
   This is a known consequence of Prop CW2.
