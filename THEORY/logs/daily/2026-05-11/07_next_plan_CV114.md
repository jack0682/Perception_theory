# 07 — Next Plan: CV-1.14 Candidate

> The recommended next target is **H-MORSE / Package II Entry Audit**.

The CV-1.13 closure made T-Temporal-Identity Cat A and finished single-formation temporal identity. The natural extension is metastable transition rates, which require Morse structure on the constrained energy landscape. H-MORSE is the gating dependency; Package II (Eyring-Kramers) is the immediate payoff.

---

## 1. Recommended Target

**W7-CV114 — H-MORSE and Package II Entry Audit**

This is an **audit / entry session**, not a proof session. Goal: reconstruct H-MORSE exact statement, map dependencies, identify proof routes and blockers, and produce a candidate CV-1.14 promotion plan.

Estimated effort: 1–2 sessions for audit; CV-1.14 seal estimated 3–6 more sessions after audit (depending on Morse-degeneracy resolution).

---

## 2. Why This Target

- **T7-Enhanced metastability exists.** The metastable basin structure on $\Sigma_m$ (volume-constraint polytope) is empirically supported (μ_min ∈ [0.96, 60.2] across configurations) but unproven.
- **H-MORSE is needed for nondegenerate critical points / saddle structure.** Without it, Hessian analysis at critical points cannot be lifted into a Morse decomposition, and the Kramers prefactor is undefined.
- **Package II needs Eyring-Kramers rates.** $\Gamma_K = \frac{1}{2\pi} \sqrt{\frac{|\lambda_-|\det(\nabla^2 E|_*)}{|\det(\nabla^2 E|_s)|}} \exp(-\Delta E / T_*)$ requires:
  - Morse minima (T-PF-A1 Package I gives Gibbs invariance; H-MORSE gives nondegeneracy).
  - Morse saddles (index-1 transition states between minima).
  - $T_*$ registered (OP-0021, currently axiomatic).
- **Dynamic K-selection depends on transition rates.** $\Gamma_{K \to K \pm 1}$ rates determine non-equilibrium K-distribution dynamics; needed for D-ST-4 rate claims.
- **H-SR (spectral repulsion) becomes derivable from H-MORSE.** Critical-point spectral structure gives explicit lower bounds on $\mu_k$ for the K-formation case.

---

## 3. Initial Questions

The entry audit must answer these eight questions before any proof attempt:

1. **What is the exact H-MORSE statement?** Likely form:
> For every critical point $u^* \in \Sigma_m$ of $E$, the Hessian $H(u^*)|_{T_{u^*}\Sigma_m}$ (projected onto the tangent space of the volume-constraint polytope) has $\mu_\mathrm{min}(H|_*) > 0$ modulo symmetry-zero eigenvalues.
   Identify the exact registered form (likely scattered across `working/MF/`); reconcile.

2. **Which energy landscape is used?** $E = \lambda_\mathrm{cl} E_\mathrm{cl} + \lambda_\mathrm{sep} E_\mathrm{sep} + \lambda_\mathrm{bd} E_\mathrm{bd} + \lambda_\mathrm{tr} E_\mathrm{tr}$ on $\Sigma_m$? Or a restricted variant?

3. **Are minimizers nondegenerate?** The K=1 disk-like minimizer empirically has $\mu_\mathrm{min} \approx 0.96$; degeneracy from translation symmetry on a torus is a candidate zero mode.

4. **Are saddles Morse?** Saddles between K and K±1 must have index 1; check whether the energy landscape generically achieves this.

5. **Does the volume constraint create zero modes?** $\Sigma_m$ is a polytope; the constraint $\sum_x u(x) = m$ adds one Lagrange dimension. Projected Hessian should remove this — verify.

6. **Does symmetry / gauge create degeneracy?** Translation on torus, rotation on disk-symmetric configurations — Morse-Bott rather than Morse?

7. **Can generic perturbation make the landscape Morse?** Standard transversality (Smale, Sard) — if so, what is the perturbation class compatible with SCC canonical structure?

8. **What does Package II require exactly?** Eyring-Kramers also needs: (a) bounded oscillation of $E$, (b) confining behavior outside basins, (c) Friedlin-Wentzell action functional, (d) Berestycki-Hamel-Roques boundary regularity. Map these against canonical state.

---

## 4. Expected Deliverables (CV-1.14 audit)

- **H-MORSE statement reconstruction.** Definitive registered statement with full assumptions and projection conventions.
- **Package II dependency map.** Directed graph: H-MORSE → T-PF-ε0-K → Package II; cross-links to P-F-A1 Package I (Cat A) and H-T* (OP-0021).
- **Proof route list.** At least three candidate routes, e.g., (a) generic perturbation + transversality, (b) Allen-Cahn-style explicit Morse decomposition under β > 7α, (c) finite-dim Morse on $\Sigma_m$ polytope + boundary-strata analysis.
- **Blocker list.** Concrete items needed to close H-MORSE Cat A: e.g., translation symmetry resolution, boundary critical points, non-analyticity if any old $b_D \neq 0$ term reappears.
- **CV-1.14 candidate plan.** Sequenced sub-tasks: H-MORSE-1 (statement), H-MORSE-2 (Hessian projection), H-MORSE-3 (interior critical points), H-MORSE-4 (boundary), H-MORSE-5 (symmetry resolution), H-MORSE-6 (final Morse decomposition), MERGE INTO Package II audit phases.

---

## 5. Alternative Target

**T-σ-Inherit / OP-0008** — σ-signature inheritance through persistent-component correspondence (Q6 multi-formation identity).

### When to choose it instead

Choose T-σ-Inherit / OP-0008 as the next target if:

- The H-MORSE audit reveals Morse-Bott degeneracy (translation / rotation symmetry) that cannot be resolved by generic perturbation under canonical SCC constraints, or
- The Package II Friedlin-Wentzell route requires P-F-A1 Package I extensions not yet canonical, blocking progress on H-MORSE indefinitely, or
- The user prioritizes multi-formation identity (Q6) over metastability dynamics (Q3-Q4) for thematic reasons.

OP-0008 has four sub-problems:
- **CONT** (continuation) — PARTIALLY STRUCTURED.
- **MERGE** — centroid + orientation Cat B; σ_standard Cat C (Wigner-projection W9+).
- **SPLIT** — direction Cat B; σ_standard Cat C.
- **DIST** (perturbation stability) — Cat B closed 2026-05-07 (Lemma 16).

Closing MERGE σ_standard (Cat C → Cat B) would be the natural CV-1.14 advance for this route, requiring the Wigner-projection apparatus to be canonicalized.

---

## 6. Out-of-scope for CV-1.14

Do **not** attempt in CV-1.14:

- Full Package II proof (Eyring-Kramers prefactor) — multi-session, requires H-MORSE first.
- OP-0021 ($T_*$ canonical registration) — major foundational item; out of scope.
- Multi-formation temporal identity beyond OP-0008 sub-problems.
- Code changes — none planned (theoretical work only).

---

## 7. Notes for the next agent

- **Carry CV-1.13 sealed state as baseline.** T-Temporal-Identity Cat A is the floor.
- **Do not reopen H-SINK, T-Temporal-Identity, or the deep-core density chain.** They are closed.
- **Treat HT-3.5 as authoritative.** (The earlier HT-3.4 leftover label on line 308 of `hypothesis_tree.md` was repaired 2026-05-11; the 변경 이력 table now includes an explicit HT-3.5 row.)
- **Start by reading `THEORY/canonical/DECLARATION.md` and the H-MORSE block in `hypothesis_tree.md` Q3.** Then enumerate every working file that mentions H-MORSE or Morse stability.
- **Default to audit, not proof.** Do not attempt full H-MORSE proof in the entry session.

The handoff prompt in `09_agent_handoff_prompt.md` is ready to run directly.
