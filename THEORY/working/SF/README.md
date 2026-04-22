# working/SF/ — Single-Formation Foundation Audit Results

**Status:** created 2026-04-22 (SF-S1 session).
**Purpose:** Consolidate the 4 Cat A candidates identified by the Round 12-18 single-formation audit (2026-04-21 evening), produce Cat-A-grade working statements with step-granularity proofs, and register canonical merge targets.
**Parent session log:** `THEORY/logs/daily/2026-04-21/14_single_formation_audit.md` (650 lines, Round 12-18 integrated).

## Directory Contents

| File | Covers | Category target |
|---|---|---|
| `README.md` | This overview | — |
| `mode_count.md` | Prop 1.3a (pure $\mathcal{E}_{\mathrm{bd}}$ Morse index) + Prop 1.3b (cl_sep structural operator) | Cat A (1.3a full) + Cat A structural / Cat C explicit form (1.3b) |
| `interface_scale.md` | Cor 2.2 qualitative + quantitative (tanh ansatz) | Cat A qualitative + Cat A ansatz + Cat B SCC-minimizer |
| `cardinality_open.md` | G-C gap: $|\{\text{local minima}\}|$ on $\Sigma_m$ (NQ-31) | Open |
| `profile_deviation.md` | NQ-32: SCC full minimizer profile vs tanh ansatz | Open |

## Naming Convention

- `mode_count`: spectral count of unstable directions at $u_{\mathrm{uniform}}$.
- `interface_scale`: the $\xi_0 = \sqrt{\alpha/\beta}$ geometry.
- `cardinality`: number of critical points on the constrained simplex.
- `profile`: spatial shape of the soft cohesion field at the minimizer.

## Relation to Other Directories

- **`working/C/`**: F-group axioms (F1 Gibbs, F2 entropy, F3 Langevin, F4 T → 0).
- **`working/CE/`**: ℱ_C+E (free energy on Σ_m at T > 0, with K_soft regularizer).
- **`working/E/`**: soft K_soft definition (G1) and dissolution files for F-1/M-1/MO-1.
- **`working/MF/`** (created 2026-04-22): multi-formation structure derived from SF invariants.

**Architectural distinction.** `E/`, `C/`, `CE/` extended the theory along the **thermal axis** (T, S, K_soft). `SF/` strengthens the theory along the **spatial / spectral axis** (N_unst, ξ_0 as single-formation invariants). The two layers are independent and mutually reinforcing; the canonical merge (Stage 6) combines both.

## Integration Targets for Canonical (Pending, awaiting Stage 6 weekly merge)

1. **§13 Cat A** four new entries (Prop 1.3a, Prop 1.3b (a)-(c)+(e), Cor 2.2 qualitative, Cor 2.2 quantitative tanh).
2. **§5 or §8 new subsection** "Single-Formation Geometry" anchoring $\xi_0 = \sqrt{\alpha/\beta}$ as a formal subject (currently implicit in five places, Round 13 §2.1).
3. **§14 new CN18** (proposed): "Single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ pre-determine the multi-formation emergence structure $(\widehat{K}, \text{size}, \text{spacing})$."
4. **§13 T-d_min-Formula** (Cat B): direction correction to $d_{\min}^\ast \asymp \xi_0$, NOT $\sqrt{\beta/\alpha}$; ties to §7 of `02_development.md` today.

## Session Carry

- **Cat A commit target:** 4 new entries for canonical_sub.md 2026-04-22.
- **Pending verification:** Full `H_{\mathrm{cl,sep}}$ explicit form (Prop 1.3b (d)) — carry to C-S2.
- **NQ-31 (G-C cardinality):** open, multi-init Morse survey postponed.
- **NQ-32 (profile):** `cardinality_open.md` documents G-C; `profile_deviation.md` documents NQ-32; `CODE/experiments/exp_profile_fit.py` (G5) is the probe script.

**End of README.**
