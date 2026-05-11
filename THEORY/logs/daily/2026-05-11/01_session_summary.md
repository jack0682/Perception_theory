# 01 — Session Summary

## 1. Starting State (entering W7 arc, 2026-05-10 morning)

- **Canonical version:** CV-1.11 (sealed 2026-05-06 W6 D4 Session Y).
- **Claim count:** 54A / 14B / 5C / 5R = 78 claims.
- **Hypothesis tree:** HT-3.0 (the Q1–Q6 epistemic restructuring, 2026-05-07).
- **T-Temporal-Identity:** working Cat B candidate only — not yet canonical. Source: `working/MF/temporal_identity_sharp_form_2026-05-07.md`.
- **H-SINK:** OPEN (Q5 Phase 1 critical-path bottleneck).
- **Deep-core density `S-B1`:** open; literal threshold "ρ_deep ≥ 0.84" suspicious — its provenance was unclear; W7-FINAL working text incorrectly labelled it the positivity threshold.
- **Final S-A1 / S-A3 / S-C1 audit blockers:** all open. None were yet documented as certified.
- **Active high-priority OPs (per `theorem_status.md`):** OP-0005, OP-0008, OP-0009, OP-0021, OP-0011, OP-0012.

The CV-1.12 work and the CV-1.13 work both happened on 2026-05-10. This log captures the full arc as it was sealed; the actual canonical timestamps are 2026-05-10 throughout.

---

## 2. Main Work Performed (chronological)

The W7 arc proceeded as five sessions on 2026-05-10:

### 1. W7-T1 — H-SINK / S-B2 result
- Wrote `THEORY/working/temporal/H-SINK.md` (462 lines): six lemmas H-SINK-1 through H-SINK-6 + main theorem + audit.
- **H-SINK-S2 = Lemma 8.2 = S-B2 promoted Cat A**: $L_g(\varepsilon_\mathrm{OT}) \leq L_c$ — dual-potential Lipschitz for SCC temporal cost class.
- Newly registered hypothesis **H-SINK-ENT** ($\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$).
- Critical finding: canonical fingerprint is 3-component, not 4-component (the 4-component version was demoted because $C_u(x,x)$ has Jacobian norm ≈ 9300 making the Lipschitz bound vacuous).
- H-SINK status: OPEN → PARTIALLY CLOSED. HT-3.0 → HT-3.1. No canonical promotion this session.

### 2. W7-FINAL — Partial-H-SINK closure → CV-1.12 sealed
- Wrote `partial_ot_stability.md`: **Theorem Partial-H-SINK (Cat A)** for canonical SCC E1 one-sided sub-stochastic OT. Direct row-softmax Lipschitz proof — no Séjourné et al. 2019 needed.
- Bound: $\|M^* - M^{*'}\|_\mathrm{TV} \leq (m_t\delta/\varepsilon_\mathrm{OT}) e^{2\delta/\varepsilon_\mathrm{OT}}$; linear regime $\leq 2m_t\delta/\varepsilon_\mathrm{OT}$ for $\delta \leq \varepsilon_\mathrm{OT}/4$.
- Cascade: Lemma 9 (plan stability) Cat B → **Cat A**; Lemma 10 (component confinement) → **Cat A**; Lemma 11 (kernel independence) = S-B3 → **Cat A conditional** (margin condition).
- H-SINK full theorem → **Cat A** for canonical SCC E1.
- **T-Temporal-Identity promoted canonical Cat B** (all four parts a/b/c/d).
- Wrote `S-B1_deep_core_density.md` and `S-B3_kernel_independence.md`.
- **CV-1.12 sealed (+1B → 79 claims).** HT-3.1 → HT-3.2. Registered OP-SB1-DEEP.

### 3. W7-CV113 — S-B1 / 0.84 provenance trace and S-B1-Weak Cat A
- Wrote `CV113_S-B1_DEEP_CORE_CLOSURE.md`: eight-route attack on OP-SB1-DEEP.
- **Critical mathematical correction:** the literal "positivity threshold ≈ 0.84" was an error in the W7-FINAL working text. The actual positivity threshold for $\Delta_\mathrm{sep} > 0$ is $\rho_* \approx 0.00282$, computed as
$$\rho_* = \frac{\eta_\mathrm{cross}^\mathrm{sharp} + (\lambda_c/\lambda_m)\bar c_\mathrm{intra}}{1 - \eta_\mathrm{self}^K}.$$
- **Lemma S-B1-Weak (Cat A NEW):** $\rho_\mathrm{deep} \geq \theta_\mathrm{core}/n = 0.7/225 \approx 0.00311 > \rho_*$, hence $\Delta_\mathrm{sep} > 0$ Cat A. Proof uses H2' (deep core non-emptiness, Γ-convergence + DMP, Theorem 1 CORE-DEPTH-ISOPERIMETRIC).
- **OP-SB1-DEEP downgraded** from HIGH-BLOCKING to NON-BLOCKING quantitative refinement.
- T-Temporal-Identity (b,d) Cat A path: blocker reduced to S-A1-A3 only.
- Preliminary count: **55A/15B/5C/5R = 80 claims** (+1A). CV-1.13 NOT yet sealed. HT-3.2 → HT-3.3.

### 4. W7-CV113A — Symbolic deep-core necessity (S-B1-SYM)
- Wrote `TRACE_084_ORIGIN.md` (forensic provenance audit of literal 0.84): every appearance traced to one of (E) empirical observation, (D) derived bound, or (R) historical retraction.
- Wrote `SYMBOLIC_DEEP_CORE_NECESSITY.md`: **Theorem S-B1-SYM (Cat B NEW)** —
$$\rho_\mathrm{deep} \geq \theta_\mathrm{core}\!\left(1 - \frac{4\,C_\mathrm{iso}}{\sqrt{m}}\right) =: \rho_\mathrm{sym}(C_\mathrm{iso}, m, \theta_\mathrm{core})$$
under HWF-1 ($\mathrm{iso\_ratio} \leq C_\mathrm{iso}$), $m \geq 25$, $\beta > 7\alpha$. Proof from canonical Theorem 2b (Deep Core Dominance, Cat A) + pointwise core bound.
- Three canonical evaluations: default (0.155, 25, 0.7) → 0.613; HWF-2' tight (0.155, 25, 0.99) → 0.867; **sharp interface (0.2, 25, 1.0) → 0.840** ← recovers literal.
- **Literal 0.84 retracted as standalone**, preserved as `ρ_sym(0.2, 25, 1.0)`.
- **OP-SB1-DEEP superseded** by **OP-SB1-084 (LOW)**.
- Net count change: 0. Preliminary count: 55A/15B/5C/5R = 80 claims unchanged. HT-3.3 → HT-3.4. CV-1.13 NOT yet sealed.

### 5. W7-CV1.13 — Final certifications and CV-1.13 seal
- Wrote `S-A1_PERSCOMP_INTEGRATION.md`: **S-A1 CERTIFIED**. Five-checkpoint audit of D-ST-3 integration into canonical §3.11 — definition present (CV-1.6), T-Temporal-Identity cites §3.11, K=1 (part d) consistent, no circular dependency, code matches.
- Wrote `S-A3_EXISTENCE_AUDIT.md`: **S-A3 CERTIFIED → T-Temporal-Identity (a) Cat A**. Lemma 1 existence proof verified: score matrix $S^0_{ij}$ finiteness trivially holds on finite graph with bounded cost; five event types (continuation/split/merge/birth/death) are mutually exclusive and exhaust all cases; $R_{t \to s}$ well-defined by construction.
- Wrote `S-C1_KERNEL_AUDIT.md`: **S-C1 CERTIFIED with correction**.
  - Audit found a **margin factor gap** in Lemma 11 (S-B3): original margin $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$ algebraically only yields $\geq \Delta_\mathrm{sep}^* - \epsilon_\mathrm{kernel}$, not $\geq \Delta_\mathrm{sep}^*$.
  - Repair: change to $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}$. Then $(\Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}) - 2\epsilon_\mathrm{kernel} = \Delta_\mathrm{sep}^* > 0$. ✓
  - Numerical impact: negligible at canonical parameters ($\Delta_\mathrm{sep}^* \approx 0.837 \gg 2\epsilon_\mathrm{kernel}$).
- Updated `S-B3_kernel_independence.md` (§0.1, §1.3) with the corrected margin.
- Promoted T-Temporal-Identity Cat B → **full Cat A** in `theorem_status.md` and `canonical.md`.
- Updated `hypothesis_tree.md`: HT-3.4 → HT-3.5; CV-1.13 SEALED block.
- Wrote `CV-1.13_SEAL.md`.
- **CV-1.13 SEALED. Net: +4A, −1B → 59A/14B/5C/5R = 83 claims.**

---

## 3. Final Result

```
T-Temporal-Identity: Cat A
CV-1.13: SEALED
Count: 59A / 14B / 5C / 5R = 83 claims
```

**T-Temporal-Identity part-by-part:**

| Part | Status at seal | Basis |
|------|----------------|-------|
| (a) Existence | Cat A | S-A3 certified |
| (b) Uniqueness (stable-K + $\Delta_\mathrm{sep} > 0$) | Cat A | S-A1 + Lemma S-B1-Weak (Cat A) |
| (c) Kernel independence | Cat A conditional | S-C1 + corrected $2\epsilon_\mathrm{kernel}$ margin (satisfied at canonical parameters) |
| (d) K=1 reduction | Cat A | S-A1 (D-ST-3 consistency) + routine algebra |

---

## 4. Meaning

SCC single-formation theory is now closed from static formation existence through temporal identity.

A single pre-objective cohesion field can form, possess a stable core, and persist as itself through time.

Mathematically: the soft cohesion field $u_t : X_t \to [0,1]$ — the primitive — supports a well-defined temporal correspondence relation $R_{t \to s}$ between persistent components, which is unique, kernel-independent, and reduces correctly to the scalar `persist_transport` in the $K=1$ case. The five event types (continuation, split, merge, birth, death) exhaust all temporal transitions of a single formation.

Conceptually: identity is no longer a primitive assumed about objects — it is a derivable property of the cohesion field over time, conditional only on stable-$K$ and a positive separation margin.

What is **not** yet proved (deliberately, see `06_open_problems_and_residuals.md`):
- Multi-formation temporal identity (T-σ-Inherit, OP-0008).
- Metastable transition rates between $K$-sectors (H-MORSE / Package II).
- Dynamic $K$-selection through time.
- $T_*$ canonical registration (OP-0021, still axiomatic).
