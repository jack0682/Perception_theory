---
type: log/daily
date: 2026-05-08
session: Session 5 (morning)
attacks: OP-OMS-016, OP-OMS-005, Hyp RG1
deliverables: vp6_effective_dof_jacobian.py, vp6_effective_dof.md, effective_dof_theory.md
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Session 5 — VP-6 Effective DOF via Jacobian Singular Spectrum

## What was done

Built and ran `vp6_effective_dof_jacobian.py` to compute the FD Jacobian of the
smooth-component readout

$$R_{\mathrm{vec}}(\lambda) = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, [\mathrm{Persist}], \ell_{\max}, \ell_{\mathrm{sec}}, A, c_{\max})$$

at 42 stencils across S3 and S4 (12 static + 9 full per scene).

## Headline numbers

| Quantity | Value |
|---|---|
| Total stencils | 42 |
| Branch-clean stencils | 41 |
| $d_{\mathrm{eff}}(\lambda; \mathrm{rel}=5\!\times\!10^{-2})$ histogram (static) | $\{1: 15,\ 2: 9\}$ |
| $d_{\mathrm{eff}}(\lambda; \mathrm{rel}=5\!\times\!10^{-2})$ histogram (full) | $\{1: 13,\ 2: 5\}$ |
| **No sample produced $d_{\mathrm{eff}} = 3$** | — |
| $\sigma_{\max}$ average | 4.22 |
| $\sigma_{\min}/\sigma_{\max}$ average | 0.0176 |
| Branch-jump stencils | 1 (S3 full at $\lambda_{cl} \approx \lambda_{sep}$) |

Strong rank anisotropy in every sample. Two-thirds of stencils have $d_{\mathrm{eff}} = 1$.

## Theoretical companion: `effective_dof_theory.md`

Three notions of dimension distinguished:

- $\dim_{\mathrm{raw}}$ (formal): 8 for $\mathcal{M}_{\mathrm{obs}}$.
- $\dim_{\mathrm{constraint}}$: 8 minus normalizations / fixed parameters.
- $\dim_{\mathrm{eff}}$ (response): per-point rank of $J_R$.

Two propositions PROVED:

- **Prop ED1:** Finite gauge does not reduce formal dimension; low Jacobian rank is **not** evidence for hidden gauge symmetry. (Audit firewall against W3/W18.)
- **Prop ED2:** If $R$ has constant rank $r$ on $U$, the level sets are $C^1$ submanifolds of codim $r$ — the perceptual indifference leaves.

## Hypothesis RG1 status update

- **Original Hyp RG1** ($d_{\mathrm{eff}} \in [2, 4]$ on full $\mathcal{M}_{\mathrm{obs}}$): WEAKENED — VP-6 holds $q, \xi$ fixed, so the original is untested.
- **Revised RG1** ($d_{\mathrm{eff}} \le k_\mathrm{tan} - 1$ on simplex slice): **COMPUTATIONALLY SUPPORTED** in 42/42 stencils.

## Conceptual takeaway

The OMS observer space, restricted to the simplex slice, has effective
response dimension 1 — typical $\lambda$-perturbations affect only one
strong direction of $P_{\mathrm{top}}$. The discrete components
($K_{\mathrm{core}}$, $n_{\mathrm{high}}$) are excluded from this picture and
provide the orthogonal information that distinguishes branches across
$\Sigma_{\mathrm{branch}}$.

## Files produced

- `THEORY/working/observer_moduli/effective_dof_theory.md`
- `THEORY/working/observer_moduli/vp6_effective_dof.md`
- `THEORY/working/observer_moduli/vp6_effective_dof_log.md`
- `THEORY/working/observer_moduli/vp6_initial_reading_log.md`
- `CODE/experiments/observer_moduli/vp6_effective_dof_jacobian.py`
- `CODE/experiments/results/observer_moduli/vp6_jacobian_spectra.json` (118 KB)
- `CODE/experiments/results/observer_moduli/vp6_effective_dof_summary.md`
