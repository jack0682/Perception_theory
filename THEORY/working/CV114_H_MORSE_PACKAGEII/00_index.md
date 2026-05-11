# W7-CV114 — H-MORSE / Package II Entry Audit

**Task:** Multi-agent entry audit for H-MORSE, Package II (Eyring-Kramers), and dynamic K-selection prerequisites.
**Date:** 2026-05-11
**Baseline:** CV-1.13 SEALED (2026-05-10). 59A/14B/5C/5R = 83 claims. HT-3.5. T-Temporal-Identity full Cat A. H-SINK FULLY CLOSED Cat A. Package I fully Cat A.
**Status:** ENTRY AUDIT — no canonical promotion intended. Working files only.

---

## Objective

Reconstruct H-MORSE (= the repository's "H5 Morse stability" hypothesis), map Package II / Eyring-Kramers dependencies, identify degeneracies that block unconditional Morse, search for finite-graph counterexamples, and recommend the most realistic CV-1.14 target.

---

## Generated documents

| File | Role | Agent (primary) |
|------|------|------------------|
| `00_index.md` | This index | — |
| `01_canonical_audit.md` | Canonical / theorem_status / hypothesis_tree refs to H-MORSE, H5, Package II, OP-0021 | A — Canonical Auditor |
| `02_H_MORSE_statement_reconstruction.md` | Exact H-MORSE candidates A/B/C/D, classification, recommended form | C — Long-Form Theorem Writer |
| `03_energy_landscape_and_hessian.md` | SCC energy, constrained Hessian on Σ_m, projector, finite-graph checks | B — Mathematical Analyst |
| `04_degeneracy_catalogue.md` | 14 degeneracy classes (volume / symmetry / boundary / saturation / etc.) with repair options | B — Mathematical Analyst |
| `05_counterexample_search.md` | Seven explicit finite-graph counterexamples to unconditional H-MORSE | D — Counterexample Hunter |
| `06_packageII_dependency_map.md` | Package I→Package II dependency graph; missing inputs; entry criterion | E — Package II Mapper |
| `07_Eyring_Kramers_requirements.md` | Six EK variants compared (classical/manifold/reflected/finite-state/discrete/custom); SCC compatibility | E — Package II Mapper |
| `08_candidate_lemma_chain.md` | CV-1.14 paths A–E (Audit/Local/Generic/PreTheorem/Full) with effort and risk | C / E |
| `09_CV114_recommendation.md` | Final recommendation: **Path B — H-MORSE-Local Cat B candidate** | A / E |
| `10_agent_handoff_prompt.md` | Ready-to-run prompt for W7-CV114B | — |

---

## One-line finding (preview)

**Unconditional H-MORSE is impossible.** Canonical Theorem V5b-T-zero (Cat A) already establishes that on translation-invariant graphs (cycle $C_n$, torus $T^d$) under sub-spinodal $c$, every corner-saturated minimizer has an *exact zero* Goldstone eigenvalue from the $\mathbb Z_L^d$ orbit. This is a structural Morse-Bott degeneracy, not numerical noise. H-MORSE must therefore be either **quotient** (mod discrete symmetry), **local** (restricted to symmetry-broken configurations), or **generic** (post small symmetry-breaking perturbation). See `05_counterexample_search.md` for details.

---

## Final recommended CV-1.14 target

**Path B — H-MORSE-Local registration as a Cat B canonical lemma.** Specifically: register a working theorem of the form

> *"Let $u^* \in \Sigma_m^\circ$ be a non-uniform single-formation minimizer of full SCC energy $\mathcal E$ that is in symmetry-broken position (no nontrivial element of $\mathrm{Aut}(G)$ fixes $u^*$). Then the projected Hessian $\Pi_T H_{\mathcal E}(u^*) \Pi_T$ on the tangent space $T_{u^*}\Sigma_m \cap \{\text{symmetry-quotient}\}$ is positive definite, with eigenvalue lower bound $\mu_\mathrm{min} \geq c(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl})$ given by the closure-correction gap of canonical.md §13 line 1139."*

This is closeable Cat B in 2–3 sessions using existing canonical material (T-PreObj-1 + closure-correction gap + V5b-T-b super-lattice exponential bound). Cat A requires either generic-perturbation transversality OR quotient-manifold Morse-Bott extension.

Package II itself should **not** be attempted at CV-1.14 — it sits behind both H-MORSE Cat A and OP-0021 (T_* registration). CV-1.14 should be an audit + Path B promotion only.

---

## Canonical state at entry (snapshot, unchanged by this audit)

- CV-1.13 SEALED 2026-05-10
- 59A / 14B / 5C / 5R = 83 claims
- HT-3.5
- T-Temporal-Identity Cat A (all 4 parts)
- H-SINK FULLY CLOSED Cat A
- P-F-A1 Package I fully Cat A (T-PF-A1-AR/SDE/GI/PE)
- T-P-F-ε0 Cat A; T-P-F-ε0-K Cat B (conditional on H5)
- T-K-Select-PF Cat B (CV-1.10); T-K-Select-OBS Cat B (CV-1.11)
- OP-0005-DYN OPEN; OP-0008 OPEN; OP-0021 OPEN (T_* axiomatic)

**No canonical claim status changed by this audit.**
