# 02 — Temporal Closure Timeline (W7 Arc)

All five sessions occurred on 2026-05-10. This file structures the work as a milestone timeline.

---

## W7-T1 — H-SINK / S-B2 Cat A

**Trigger:** Long-horizon proof audit of H-SINK (Sinkhorn-Lipschitz stability for SCC temporal cost class). Goal: close S-B2 bottleneck for T-Temporal-Identity Cat A promotion path.

**Outputs:**
- S-B2 = H-SINK-S2 = Lemma 8.2 → **Cat A** (proof: log-sum-exp inequality on Sinkhorn fixed-point + DR2 verification from first principles).
- Lemmas H-SINK-1, H-SINK-2, H-SINK-4, H-SINK-5 → **Cat A** (new).
- Lemma H-SINK-3 (resolvent / 4-component) → **Cat B conditional** (not needed for canonical 3-component fingerprint).
- Lemma H-SINK-6 (Sinkhorn plan stability) → **Cat A balanced / Cat B partial OT** (partial OT gap remains).
- Theorem H-SINK (full plan stability) → **Cat B** due to partial OT gap.
- New hypothesis: **H-SINK-ENT** ($\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$).
- Demotion finding: canonical fingerprint is 3-component; the 4-component $C_u(x,x)$ variant has Jacobian norm ≈ 9300 (Lipschitz bound vacuous).

**Status changes:**
- H-SINK hypothesis node: OPEN → **PARTIALLY CLOSED**.
- T-Temporal-Identity Cat A promotion path **unblocked** from the S-B2 side.
- Count unchanged (S-B2 was working, not yet canonical).
- Hypothesis tree: HT-3.0 → HT-3.1.

---

## W7-FINAL — H-SINK Full Closure → CV-1.12 Sealed

**Trigger:** Complete single-formation temporal closure chain. Bridge: H-SINK → partial OT → S-B1 → S-B3 → T-Temporal-Identity canonical → CV-1.12.

**Outputs:**
- **Theorem Partial-H-SINK (Cat A NEW):** Direct row-softmax Lipschitz proof for canonical SCC E1 one-sided sub-stochastic OT. No Séjourné et al. 2019 needed. Bound: $\|M^* - M^{*'}\|_\mathrm{TV} \leq (m_t\delta/\varepsilon_\mathrm{OT})e^{2\delta/\varepsilon_\mathrm{OT}}$.
- Cascade: Lemma 9 (plan stability) Cat B → **Cat A**; Lemma 10 (component confinement) Cat B → **Cat A**; Lemma 11 (kernel independence, = S-B3) Cat B → **Cat A conditional** (margin condition).
- H-SINK full theorem (canonical SCC E1) → **Cat A**.
- **S-B3 (Lemma 11) Cat A conditional** under margin $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$ (later corrected to $+2\epsilon_\mathrm{kernel}$ by S-C1).
- S-B1 (literal $\rho_\mathrm{deep} \geq 0.84$): **Cat B conditional** under HWF-1–3. Unconditional Cat A impossible — counterexample: $3 \times 10$ rectangle, $\rho_\mathrm{deep} \approx 0.27$. **OP-SB1-DEEP registered.**
- T-Temporal-Identity: working Cat B → **canonical Cat B** (CV-1.12 promotion). All four parts (a,b,c,d) canonicalized.

**Status changes:**
- H-SINK: PARTIALLY CLOSED → **FULLY CLOSED (Cat A)**.
- T-Temporal-Identity Cat B canonicalized (parts a,b,c,d).
- **CV-1.12 SEALED.** Count: +1B → **54A / 15B / 5C / 5R = 79 claims (~68%)**.
- Hypothesis tree: HT-3.1 → HT-3.2.
- OP-0011: STRUCTURED → PARTIALLY RESOLVED (Steps 2–3 Cat A).

---

## TRACE_084_ORIGIN — Provenance Audit of Literal 0.84 (interleaved with W7-CV113)

**Trigger:** Suspicion that "ρ_deep ≥ 0.84" was being used inconsistently — sometimes as a derived bound, sometimes as a positivity threshold, sometimes as an empirical observation. Need to determine its first-principles status.

**Findings:**
- **Earliest appearance:** `exp49_unified_predictions.json` — empirical `deep_core_frac` ≈ 0.81 mean, 0.84 mode, range 0.664–0.865. Empirical, not theoretical.
- **Later use as plug-in:** `temporal_identity_sharp_form_2026-05-07.md §5` — substituted as observed ρ_deep into Δ_sep* formula yielding $\Delta_\mathrm{sep}^* \approx 0.837$.
- **W7-FINAL error:** `S-B1_deep_core_density.md §0.2` (W7-FINAL) wrote "at default parameters, this threshold is approximately 0.84" — wrongly identifying 0.84 as the positivity threshold for $\Delta_\mathrm{sep} > 0$. **The actual threshold is $\rho_* \approx 0.00282$**, three orders of magnitude smaller.
- **Determination:** 0.84 is **not** a standalone analytic theorem constant. It is an empirical / numerical value, later shown to equal $\rho_\mathrm{sym}(0.2, 25, 1.0)$ from the symbolic identity.

The trace audit established that any claim of the form "ρ_deep ≥ 0.84 as a universal theorem constant" is false; only "ρ_deep ≥ ρ_sym(C_iso, m, θ_core) under HWF-1" is provable, with 0.84 being its sharp-interface evaluation.

---

## W7-CV113 — S-B1-Weak Cat A (Positivity Path Opened)

**Trigger:** Attack OP-SB1-DEEP (the literal 0.84 unconditional bound) and determine T-Temporal-Identity (a,b,d) Cat A path. Eight proof routes were tried.

**Key insight:** The blocking condition was based on misidentifying the positivity threshold. Only $\rho_\mathrm{deep} > 0$ is needed for $\Delta_\mathrm{sep} > 0$; explicitly only $\rho_\mathrm{deep} > \rho_* \approx 0.00282$.

**Outputs:**
- **Lemma S-B1-Weak (Cat A NEW):** $\rho_\mathrm{deep} \geq \theta_\mathrm{core}/n = 0.7/225 \approx 0.00311 > \rho_* \approx 0.00282$. Proof: H2' (Γ-convergence + DMP, Theorem 1 of CORE-DEPTH-ISOPERIMETRIC.md) gives $|\mathrm{Core}^2| \geq 1$, hence $m^\mathrm{deep} \geq 0.7$, and $m \leq 225$.
- **Corollary (Cat A):** $\Delta_\mathrm{sep} > 0$ under canonical assumptions — logical uniqueness condition for T-Temporal-Identity (b) satisfied Cat A.
- **OP-SB1-DEEP downgraded** from HIGH-BLOCKING to NON-BLOCKING. The Cat A path for T-Temporal-Identity (b,d) is unblocked at the density side.
- S-B1 Strong (literal $\rho_\mathrm{deep} \geq 0.84$ unconditional): remains **Cat B conditional** with explicit counterexample.

**Status changes:**
- T-Temporal-Identity (b,d) Cat A path now requires only S-A1-A3 (~1–2 sessions).
- Preliminary count: **55A / 15B / 5C / 5R = 80 claims** (+1A).
- CV-1.13 path unblocked, but **CV-1.13 not yet sealed**.
- Hypothesis tree: HT-3.2 → HT-3.3.

---

## W7-CV113A — Symbolic Reframing of Legacy 0.84 (S-B1-SYM)

**Trigger:** Convert the literal numerical constant $\rho_\mathrm{deep} \geq 0.84$ from a standalone empirical claim into an analytically derived symbolic identity proved from canonical Theorem 2b.

**Outputs:**
- **Theorem S-B1-SYM (Cat B NEW):**
$$\rho_\mathrm{deep} \geq \theta_\mathrm{core}\!\left(1 - \frac{4\,C_\mathrm{iso}}{\sqrt{m}}\right) =: \rho_\mathrm{sym}(C_\mathrm{iso}, m, \theta_\mathrm{core})$$
  under HWF-1 ($\mathrm{iso\_ratio} \leq C_\mathrm{iso}$), $m \geq 25$, $\beta > 7\alpha$. Proof: canonical Theorem 2b (Deep Core Dominance, Cat A) + pointwise core lower bound + trivial mass upper bound.
- Three canonical evaluations:
  | Regime | $C_\mathrm{iso}$ | $m$ | $\theta_\mathrm{core}$ | $\rho_\mathrm{sym}$ |
  |--------|------|-----|---------|---------|
  | Default canonical | 0.155 | 25 | 0.7 | **0.613** |
  | HWF-2' tight interior | 0.155 | 25 | 0.99 | **0.867** |
  | Sharp interface | 0.2 | 25 | ~1.0 | **0.840** ← recovers literal |
- **Literal 0.84 retracted as standalone claim**, retained as numerical evaluation $\rho_\mathrm{sym}(0.2, 25, 1.0) = 0.84$ (sharp-interface regime).
- **OP-SB1-DEEP superseded** by **OP-SB1-084 (LOW):** determine the smallest provable $C_\mathrm{iso}$ on canonical 15×15 such that $\rho_\mathrm{sym}(C_\mathrm{iso}, \bar m, \bar\theta_\mathrm{core}) = 0.84$ analytically.

**Status changes:**
- Net count change: **0**. S-B1-SYM Cat B replaces legacy S-B1 Strong Cat B. Preliminary count: 55A / 15B / 5C / 5R = 80 claims (unchanged).
- Hypothesis tree: HT-3.3 → HT-3.4.
- **CV-1.13 NOT yet sealed.** S-B1-SYM is a provenance / quality upgrade, not a Cat-A-path unblocker.

---

## W7-CV1.13 — Final Certifications and CV-1.13 Seal

**Trigger:** Three audit tasks (S-A1, S-A3, S-C1) needed for T-Temporal-Identity full Cat A. Continuation from W7-CV113A.

**Outputs:**

- **S-A1 CERTIFIED** (`S-A1_PERSCOMP_INTEGRATION.md`): D-ST-3 PersComp integration into canonical §3.11 verified across five checkpoints — definition present, T-Temporal-Identity cites §3.11 explicitly, K=1 (part d) consistent, no circular dependency, code matches.
- **S-A3 CERTIFIED → T-Temporal-Identity (a) Cat A** (`S-A3_EXISTENCE_AUDIT.md`): Lemma 1 (existence) verified — score matrix $S^0_{ij}$ finiteness trivially holds on finite graph; five event types mutually exclusive and exhaustive; $R_{t\to s}$ well-defined.
- **S-C1 CERTIFIED with margin correction** (`S-C1_KERNEL_AUDIT.md`):
  - Audit identified a **margin factor gap** in the Lemma 11 (S-B3) proof: original margin $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$ algebraically yields only $\geq \Delta_\mathrm{sep}^* - \epsilon_\mathrm{kernel}$.
  - **Correction:** strengthen to $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}$. Then $(\Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}) - 2\epsilon_\mathrm{kernel} = \Delta_\mathrm{sep}^* > 0$ ✓.
  - Numerical impact: minor. At canonical parameters $\Delta_\mathrm{sep}^* \approx 0.837 \gg 2\epsilon_\mathrm{kernel}$ for any reasonable cost perturbation.
- `S-B3_kernel_independence.md` updated (§0.1, §1.3) with corrected margin.
- T-Temporal-Identity promoted Cat B → **full Cat A** across parts (a), (b), (c), (d).
- Wrote `CV-1.13_SEAL.md` (official seal document).
- Updated `canonical.md`, `theorem_status.md`, `hypothesis_tree.md`, `CHANGELOG.md`.

**Status changes:**
- **CV-1.13 SEALED.**
- T-Temporal-Identity: Cat B → **Cat A**.
- Net count: **+4A, −1B → 59A / 14B / 5C / 5R = 83 claims (~71%).**
- Hypothesis tree: HT-3.4 → HT-3.5.

---

## Cumulative arc summary

| Phase | Session | HT | Count change | Key result |
|-------|---------|-----|--------------|------------|
| Entry | (pre-W7) | HT-3.0 | 54A/14B/5C/5R = 78 | CV-1.11 sealed |
| W7-T1 | 2026-05-10 | HT-3.1 | 0 | S-B2 Cat A; H-SINK PARTIALLY CLOSED |
| W7-FINAL | 2026-05-10 | HT-3.2 | +1B → 79 | CV-1.12 sealed; H-SINK FULLY CLOSED |
| W7-CV113 | 2026-05-10 | HT-3.3 | +1A → 80 (prelim) | S-B1-Weak Cat A; OP-SB1-DEEP downgraded |
| W7-CV113A | 2026-05-10 | HT-3.4 | 0 | S-B1-SYM Cat B; literal 0.84 retracted |
| **W7-CV1.13** | 2026-05-10 | **HT-3.5** | **+4A, −1B → 83** | **CV-1.13 sealed; T-Temporal-Identity full Cat A** |
