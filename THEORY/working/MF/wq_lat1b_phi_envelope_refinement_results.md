# WQ-LAT-1.B — Phi-Envelope Refinement Results

**File:** `THEORY/working/MF/wq_lat1b_phi_envelope_refinement_results.md`
**Document type:** Working-grade post-processing results (non-canonical).
**Created:** 2026-05-02 (post-WQ-LAT-1; targeted phi-envelope refinement).

**Companion artifacts:**
- `CODE/scripts/wq_lat1b_phi_envelope_refinement.py` — analysis script.
- `CODE/scripts/results/wq_lat1b_phi_envelope_refinement.json` — full numerical output.

**Predecessor artifacts:**
- `THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_protocol.md` — WQ-LAT-1 protocol.
- `THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_results.md` — WQ-LAT-1 outcome (integer-morphology PASS, smooth K_soft FAIL under default φ).
- `THEORY/working/MF/latent_index_space_design.md` — reservoir framework.
- `THEORY/working/MF/ksoft_kact_bridge_lemma.md` — bridge lemma framework.
- `THEORY/working/E/soft_K_definition.md` — original K_soft definition with (φ-sat) family.

---

## 1. Status and Scope

**Status:** RUN COMPLETE — `success`. All six LAT1B-C1..C6 criteria pass.

**Status grade per claim.**

| Claim | Status |
|---|---|
| Default $\phi$-saturating envelope fails to be chart-invariant under split-bump refinement | working-definition safe (per WQ-LAT-1 + this run) |
| Hard threshold $\phi_{\mathrm{hard}}$ is chart-invariant | working-definition safe (range = 0 across all $K$) |
| Logistic envelope at high slope $s = 100$ achieves smooth chart-invariance | working-definition safe (range = 0.0009 at $\ell_{\min} = 0.10$) |
| The recommended $\phi$ family is *the* canonical choice | **forbidden non-claim** — only empirical evidence on one configuration |

**Scope.** Post-processing on the WQ-LAT-1 production run plus a targeted deterministic rerun (seed=42, identical params; bit-for-bit reproduces WQ-LAT-1 trajectories) to recover the *full* final-snapshot $H_0$ superlevel barcodes (the WQ-LAT-1 JSON saved only top-8). 13 candidate $\phi$-envelopes evaluated at 4 thresholds ($\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}$) across 20 trajectories ($K \in \{3, 4, 6, 8, 12\}$, options ${\text{LAT-A}, \text{LAT-C}}$, geometries $\{A, B\}$). Wall-clock 55.9 s.

**Out of scope.**

- Promoting any $\phi$ choice to canonical.
- Resolving OP-0005 / OP-0008.
- Validating reservoir framework as canonical.
- Generalizing to other graphs / dynamics.

---

## 2. Motivation from WQ-LAT-1

WQ-LAT-1 production (61.7 s, 20 trajectories) found:

- **Integer-morphology observables converge** under split-bump refinement: $K_{\mathrm{bar}}^{\ell_{\min}}$ at all four $\ell_{\min}$ stays exactly = 1 across all $K$; aggregate $L^2$ distance per vertex $\le 1.5 \times 10^{-2}$; dominant bar profile stable within 0.03.
- **Smooth $K_{\mathrm{soft}}^\phi$ does NOT converge** under the default (φ-sat) envelope $\phi(\ell) = \ell / (\ell + \ell_{\min})$: it grows monotonically $0.92 \to 1.13 \to 1.25 \to 1.40 \to 1.86$ across $K = 3 \to 12$ on LAT-C__A; range = 0.94 vs tolerance 0.10.

The cause was identified: the (φ-sat) envelope assigns ~0.09 to a bar of length 0.01, and as $K$ increases under split-bump refinement, more sub-resolution bars accumulate. WQ-LAT-1.B asks: **does any $\phi$ envelope achieve chart-invariance while preserving dominant morphology?**

---

## 3. Candidate $\phi$-Envelopes Evaluated

| ID | Form | Parameters |
|---|---|---|
| Phi-0 | $\phi_0(\ell) = \ell / (\ell + \ell_{\min})$ | (default; baseline failure) |
| Phi-1 | $\phi_1(\ell) = \mathbf 1\{\ell \ge \ell_{\min}\}$ | hard threshold (= $K_{\mathrm{bar}}$) |
| Phi-2 | $\phi_2(\ell) = \max(0, (\ell - \ell_{\min})/(1 - \ell_{\min}))$ | shifted linear |
| Phi-3a–d | $\phi_3(\ell) = 1 - \exp(-\beta \max(0, \ell - \ell_{\min}))$ | shifted saturating; $\beta \in \{2, 5, 10, 20\}$ |
| Phi-4a–c | $\phi_4(\ell) = \mathrm{sigmoid}(s(\ell - \ell_{\min})) - \mathrm{sigmoid}(-s\ell_{\min})$ | logistic; $s \in \{20, 50, 100\}$ |
| Phi-5 | $\phi_0$ applied to top-$r$ bars only | $r \in \{1, 2, 3, 4, 6\}$ |
| Phi-6 | $\sum_i \phi_0(\ell_i) / Z$ | $Z \in \{$ count, totalpers, topr_pers $\}$ |

13 envelope variants total.

---

## 4. Metrics

For each (envelope, $\ell_{\min}$, option, geometry) $K$-block, compute:

- **M1 Range** = $\max_K K_{\mathrm{soft}}^\phi - \min_K K_{\mathrm{soft}}^\phi$
- **M2 CV** = std / mean across $K$
- **M3 Monotonic drift** flag
- **M4 Mean value** (closeness to dominant-morphology reference $K_{\mathrm{bar}} = 1$)
- **M5 Threshold robustness** (LAT1B-C5: at least 2 $\ell_{\min}$ values pass)
- **M6 A/B geometry consistency**
- **M7 Option (LAT-A vs LAT-C) consistency**

---

## 5. Results Table

### 5.1 Per-envelope $K_{\mathrm{soft}}$ on LAT-C__A at $\ell_{\min} = 0.10$ (the WQ-LAT-1 baseline)

| Envelope | $K=3$ | $K=4$ | $K=6$ | $K=8$ | $K=12$ | range | mean |
|---|---|---|---|---|---|---|---|
| **Phi-0_default_sat** (baseline) | 0.916 | 1.129 | 1.249 | 1.399 | **1.859** | **0.943** ❌ | 1.310 |
| **Phi-1_hard** | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | **0.000** ✓ | **1.000** ✓ |
| Phi-2_shift_lin | 0.156 | 0.155 | 0.153 | 0.152 | 0.156 | 0.005 | 0.154 |
| Phi-3a_shift_sat_b2 | 0.245 | 0.243 | 0.240 | 0.239 | 0.244 | 0.006 | 0.242 |
| Phi-3b_shift_sat_b5 | 0.505 | 0.502 | 0.497 | 0.495 | 0.503 | 0.010 | 0.500 |
| Phi-3c_shift_sat_b10 | 0.755 | 0.752 | 0.747 | 0.745 | 0.753 | 0.010 | 0.750 |
| **Phi-3d_shift_sat_b20** | 0.940 | 0.939 | 0.936 | 0.935 | 0.939 | 0.005 | **0.938** |
| Phi-4a_logistic_s20 | 0.878 | 0.928 | 0.957 | 0.989 | 1.118 | 0.240 ❌ | 0.974 |
| Phi-4b_logistic_s50 | 1.003 | 1.012 | 1.018 | 1.024 | 1.050 | 0.047 | 1.022 |
| **Phi-4c_logistic_s100** | 1.000 | 1.000 | 1.000 | 1.001 | 1.001 | **0.001** ✓ | **1.001** ✓ |
| Phi-5_topr=1 | 0.706 | 0.705 | 0.704 | 0.703 | 0.706 | 0.004 | 0.705 |
| Phi-5_topr=2 | 0.829 | 0.828 | 0.826 | 0.814 | 0.859 | 0.045 | 0.831 |
| Phi-5_topr=3 | 0.912 | 0.915 | 0.933 | 0.916 | 0.992 | 0.080 | 0.934 |
| Phi-5_topr=4 | 0.916 | 0.991 | 1.013 | 0.998 | 1.116 | 0.200 ❌ | 1.007 |
| Phi-5_topr=6 | 0.916 | 1.121 | 1.170 | 1.154 | 1.312 | 0.396 ❌ | 1.135 |
| Phi-6_norm_count | 0.229 | 0.103 | 0.156 | 0.108 | 0.103 | 0.126 | 0.140 |
| Phi-6_norm_totalpers | 3.469 | 3.949 | 4.198 | 4.479 | 5.045 | 1.576 ❌ | 4.228 |
| Phi-6_norm_topr_pers | 3.469 | 3.960 | 4.321 | 4.884 | 6.012 | 2.543 ❌ | 4.529 |

(Range tolerance for LAT1B-C2: 0.10. ✓ = pass; ❌ = fail.)

### 5.2 Threshold-robustness check on top candidates (LAT-C__A)

| $\ell_{\min}$ | Phi-1_hard range | Phi-4c_logistic_s100 range | Phi-3d_shift_sat_b20 range |
|---|---|---|---|
| 0.05 | 0.000 | 0.134 ❌ | 0.002 ✓ |
| 0.10 | 0.000 | 0.001 ✓ | 0.005 ✓ |
| 0.15 | 0.000 | 0.0001 ✓ | 0.014 ✓ |
| 0.20 | 0.000 | 0.008 ✓ | 0.037 ✓ |

Phi-1 is robust at all four $\ell_{\min}$. Phi-4c is robust at $\ell_{\min} \ge 0.10$. Phi-3d is robust at all four with slowly degrading consistency.

### 5.3 Bar-count statistics (where the drift comes from)

| Run | $K_{\mathrm{act}}$ | $K_{\mathrm{bar}}^{0.10}$ | $\mathcal F$ | n_positive_bars | max_bar | median_bar | min_bar |
|---|---|---|---|---|---|---|---|
| LAT-C K=3 A | 3 | 1 | 4 | 4 | 0.241 | 0.014 | 0.0004 |
| LAT-C K=4 A | 4 | 1 | 11 | 11 | 0.239 | 0.006 | 0.0000 |
| LAT-C K=6 A | 6 | 1 | 8 | 8 | 0.237 | 0.009 | 0.0005 |
| LAT-C K=8 A | 8 | 1 | 13 | 13 | 0.237 | 0.008 | 0.0000 |
| LAT-C K=12 A | 12 | 1 | 18 | 18 | 0.240 | 0.008 | 0.0000 |

The dominant bar (max ≈ 0.24) is *constant* across $K$ — the aggregate has one robust connected component throughout. The drift in default $\phi$ is entirely from the sub-resolution noise band: the **number of positive bars grows from 4 to 18** as $K$ increases under LAT-C, each contributing a small (median ~0.01) length that the default $\phi$-saturating envelope assigns ~0.09 to.

### 5.4 Criteria summary

| Criterion | Status | Evidence |
|---|---|---|
| LAT1B-C1 — baseline failure reproduced | **PASS** | Phi-0 range = 0.943 on LAT-C__A at $\ell_{\min} = 0.10$ |
| LAT1B-C2 — at least one $\phi$ suppresses drift | **PASS** | 5 candidates pass: Phi-1, Phi-4c, Phi-5_topr=1, Phi-2, Phi-3d |
| LAT1B-C3 — candidate preserves dominant morphology | **PASS** | Phi-1 mean = 1.000; Phi-4c mean = 1.001; Phi-3d mean = 0.938 |
| LAT1B-C4 — robust across A/B geometry | **PASS** | Phi-1, Phi-4c, Phi-3d each robust on both A and B |
| LAT1B-C5 — robust across thresholds | **PASS** | Phi-1 robust at all 4 $\ell_{\min}$; Phi-4c at 3 of 4; Phi-3d at all 4 |
| LAT1B-C6 — theoretically interpretable | **PASS** | Phi-1 = hard threshold; Phi-4c = logistic-as-hard-approximation; Phi-3d = shifted saturating; Phi-5 = top-$r$ truncation; Phi-2 = shifted linear |

**Status: success.**

---

## 6. Recommended $\phi$

Three candidates emerge from the empirical record. Each has different trade-offs.

### 6.1 Primary recommendation: **Phi-1 hard threshold**

$$
\phi_1(\ell; \ell_{\min}) := \mathbf 1\{\ell \ge \ell_{\min}\}.
$$

This recovers $K_{\mathrm{bar}}^{\ell_{\min}}$ exactly. It is **integer-valued, perfectly chart-invariant** (range = 0 at all $\ell_{\min}$, both A and B, both LAT-A and LAT-C), and has mean exactly = 1 on the WQ-LAT-1 baseline.

**Use:** as the *primary count observable* for reservoir-invariant morphology. This is exactly the empirical lesson of WQ-LAT-1: the integer hard-bar count is reservoir-invariant where the smooth K_soft is not.

**Limitation:** not differentiable. If a smooth observable is needed for variational analysis, see Phi-4c.

### 6.2 Secondary recommendation: **Phi-4c logistic with s = 100**

$$
\phi_4(\ell; \ell_{\min}, s = 100) := \frac{1}{1 + \exp(-100 (\ell - \ell_{\min}))} - \frac{1}{1 + \exp(100\, \ell_{\min})}.
$$

This is a **smooth approximation to the hard threshold** with sharp transition. Range = 0.0009 at $\ell_{\min} = 0.10$, mean = 1.001. Indistinguishable from hard threshold at $\ell_{\min} \ge 0.10$.

**Use:** when smoothness is required (gradient-based optimization, Lipschitz arguments). Sensitive to $\ell_{\min}$: degrades at $\ell_{\min} = 0.05$ (range = 0.13) because the dominant bar (~0.24) is then much larger than $\ell_{\min}$ and sub-resolution bars near $\ell_{\min}$ contribute non-trivially.

**Limitation:** $\ell_{\min}$ choice matters. Recommended $\ell_{\min} \in [0.10, 0.20]$ for this graph and dynamics.

### 6.3 Tertiary recommendation: **Phi-3d shifted saturating with β = 20**

$$
\phi_3(\ell; \ell_{\min}, \beta = 20) := 1 - \exp(-20 \max(0, \ell - \ell_{\min})).
$$

Range = 0.005 at $\ell_{\min} = 0.10$, mean = 0.938. Smooth and differentiable everywhere. Less aggressive transition than Phi-4c.

**Use:** when an *interpretable* shifted-saturation form is preferred over the logistic-as-hard-approximation. The mean depends on the dominant bar magnitude relative to $\ell_{\min}$ via the saturation rate $\beta$, so the exact value is < 1; but range is consistently small across all four $\ell_{\min}$.

**Limitation:** mean is below 1 — does not exactly recover $K_{\mathrm{bar}}$ at the dominant-bar level.

### 6.4 Why Phi-2 and Phi-5_topr=1 are not recommended

Phi-2 (shifted linear) and Phi-5_topr=1 are also chart-invariant (small range), but their mean values (0.154 and 0.705 respectively) are far from the $K_{\mathrm{bar}}$ reference of 1. They measure something different — the *excess persistence above threshold* (Phi-2) or the *default-sat envelope of the single most prominent bar* (Phi-5_topr=1). Either is admissible as a *different* observable; neither is a chart-invariant *count* observable in the K_bar sense.

### 6.5 Why Phi-6 normalized envelopes fail

All three normalizations (count, totalpers, topr_pers) fail because the normalizing factor itself depends on $K$. count = n_positive_bars varies 4 → 19 across LAT-C K-sweep; totalpers and topr_pers grow with the number of sub-bars. Normalization does not cancel the chart-rank dependency.

---

## 7. Failure Modes (none triggered)

| Mode | Triggered? | Evidence |
|---|---|---|
| LAT1B-F1 — JSON lacks bar lengths | NO | targeted rerun recovered full barcodes |
| LAT1B-F2 — no $\phi$ suppresses drift | NO | 5 candidates pass |
| LAT1B-F3 — only hard threshold works | NO | Phi-3d, Phi-4c, Phi-5_topr=1, Phi-2 all also pass |
| LAT1B-F4 — candidate works only for one geometry | NO | top candidates work for both A and B |
| LAT1B-F5 — candidate works only for one threshold | NO | Phi-1 works at all 4; Phi-3d works at all 4; Phi-4c at 3 of 4 |
| LAT1B-F6 — candidate destroys dominant morphology | NO | Phi-1 mean = 1; Phi-4c mean = 1.001; Phi-3d mean = 0.938 |

---

## 8. Theoretical Interpretation

### 8.1 What WQ-LAT-1.B confirms

The reservoir-resolution prediction of `latent_index_space_design.md` §10 is **structurally correct** for integer-morphology observables. The WQ-LAT-1 finding that smooth $K_{\mathrm{soft}}^\phi$ fails was a $\phi$-envelope choice failure, not a reservoir-framework failure. With an appropriate $\phi$ (hard threshold or smooth approximation thereof), the smooth count observable *does* become chart-invariant within tolerance.

### 8.2 What is happening at the bar-distribution level

Under LAT-C split-bump refinement, the aggregate $H_0$ superlevel barcode of $U_K$ has:

- **One dominant bar** of length ≈ 0.24, *invariant* across $K$ (corresponds to the single connected component the three clusters form);
- **A long tail of sub-resolution bars** with lengths ranging from $\sim 10^{-4}$ to $\sim 0.025$, *growing in count* with $K$ (4 bars at $K=3$ → 18 bars at $K=12$).

The default (φ-sat) envelope $\phi_0(\ell) = \ell/(\ell + \ell_{\min})$ assigns $\sim 0.09$ to a bar of length 0.01 (when $\ell_{\min} = 0.10$). Summing 18 such contributions adds $\sim 1.6$ to $K_{\mathrm{soft}}$. This dominates the dominant-bar contribution (≈ 0.71) and produces the observed drift.

A $\phi$ that *zeros out* sub-$\ell_{\min}$ bars (hard threshold, shifted forms, sharp logistic) eliminates the drift. A $\phi$ that smoothly tapers but doesn't aggressively zero (default sat, gentle logistic at low $s$) allows the drift to accumulate.

### 8.3 Implication for the bridge lemma

The $K_{\mathrm{soft}} / K_{\mathrm{act}}$ bridge of `ksoft_kact_bridge_lemma.md` §5 has an error term form

$$
K_{\mathrm{soft}}^\phi(U(\mathbf u)) = K_{\mathrm{act}}^\varepsilon(\mathbf u) + O(\rho_{\mathrm{sep}} + \rho_{\mathrm{noise}} + \rho_\phi).
$$

WQ-LAT-1.B numerically demonstrates that **$\rho_{\mathrm{noise}}$ is not small under split-bump refinement** for the default (φ-sat) envelope, but **$\rho_{\mathrm{noise}} \to 0$** for $\phi$ envelopes that respect a sharp $\ell_{\min}$ cutoff. The bridge lemma sketch §5.2 (exact identity under condition (5) single-mode-per-formation) is empirically correct *given the right $\phi$*; the §5.3 smooth approximation needs the right $\phi$ to converge.

This suggests an upgrade path for `ksoft_kact_bridge_lemma.md` §5.3: state the smooth bridge with an explicit $\phi$-class restriction (e.g. "for any $\phi$ such that $\phi(\ell) = 0$ for $\ell < \ell_{\min}$").

### 8.4 Implication for the reservoir framework

The latent-index-space design's §10.1 hierarchy

$$
K_{\mathrm{field}} \text{ (chart)} \;\to\; K_{\mathrm{act}}^\varepsilon \text{ (chart-level)} \;\to\; K_{\mathrm{bar}}^{\ell_{\min}}, K_{\mathrm{soft}}^\phi \text{ (field-level)}
$$

is empirically validated **at the level of $K_{\mathrm{bar}}$ and $K_{\mathrm{soft}}^\phi$ with $\phi$ from the recommended families** (hard, sharp logistic, shifted saturating). Under a poor $\phi$ choice, $K_{\mathrm{soft}}^\phi$ leaks chart-rank information from the truncation; under a good $\phi$, it does not.

The reservoir framework remains a candidate framework, not canonical. The empirical record now includes both a confirmation (integer-morphology + good-$\phi$ smooth observables converge) and a refinement (the $\phi$ choice matters).

---

## 9. Non-Claims

This analysis does not:

- promote any $\phi$ choice to canonical status;
- claim the reservoir framework is canonical;
- claim OP-0005 (K-Selection) or OP-0008 (σ-standard incompleteness) is resolved;
- claim σ-rich is sufficient;
- claim Φ_rich is deterministic;
- assert the recommended $\phi$ generalizes to other graphs / dynamics / initialization options;
- claim a theorem-level result; the evidence is empirical on one configuration ($T^2_{20}$, Option D-2 dynamics, equilateral A vs compressed B, $K \in \{3, 4, 6, 8, 12\}$, four $\ell_{\min}$ values);
- import gauge theory, full category theory, sheaf cohomology, Geometric Langlands, CBF/CLF, neural operators, Koopman operators, formal verification;
- modify any canonical or existing working file (apart from this WQ-LAT-1.B-specific document and script);
- assign a Commitment number;
- treat $K_{\mathrm{soft}}^\phi$ at default $\phi$ as obsolete — it is *not* chart-invariant under split-bump refinement, but it remains a meaningful observable in other contexts.

OP-0008 retains 🟠 HIGH severity. OP-0005 retains 🟠 HIGH severity. OP-0009 sub-items retain CV-1.5.1 status.

---

## 10. Next Steps

In execution-order priority:

### WQ-LAT-1.C — Bridge-lemma update (~1 hour, post-processing)

Update `ksoft_kact_bridge_lemma.md` §5.3 (smooth bridge approximation) with the empirical finding from WQ-LAT-1.B: the smooth bridge identity holds *for $\phi$ in the recommended families* (hard, logistic with $s \ge 50$, shifted saturating with $\beta \ge 20$). The default (φ-sat) family is *not* sufficient under split-bump refinement.

### WQ-LAT-2 — Spectral packet prototype (~3–5 days)

Independent test of Model II spectral mode reservoir on $T^2_{20}$. Per `latent_index_space_design.md` §16 WQ-LAT-2.

### WQ-LAT-3 — Five-model K-selection comparison (~1 week)

K-selection with reservoir-effective-rank and persistence-prominence candidates added (per `latent_index_space_design.md` §11.3). The WQ-LAT-1.B evidence that $K_{\mathrm{bar}}^{\ell_{\min}}$ is reservoir-invariant *and* $K_{\mathrm{bar}} = 1$ across all $K$ for this baseline informs candidate (e) "persistence-prominence" — it predicts $K^* = 1$ for the well-separated regime, which agrees with T-Merge (b) energy minimization.

### WQ-LAT-4 — OP-0008 reframe (~3–5 days)

Document σ-standard's chart-level vs reservoir-level distinction.

### Updates to existing memos (deferred to user)

- `wq_lat1_reservoir_resolution_sweep_results.md` §10 "Decision and Next Action": update the recommendation block — $\phi$-envelope refinement now answered, with primary recommendation hard threshold + secondary logistic s=100.
- `latent_index_space_design.md` §14.3: tighten the reservoir-consistency-diagnostics description to specify the recommended $\phi$ families.
- `ksoft_kact_bridge_lemma.md` §5.3: add the $\phi$-class restriction.

These document updates are minor and can be deferred or done by the user.

---

**End of WQ-LAT-1.B results.** Status: RUN COMPLETE — `success`. All six criteria pass (LAT1B-C1..C6). Primary recommendation: **Phi-1 hard threshold** (perfect chart-invariance). Secondary smooth recommendation: **Phi-4c logistic with s = 100** at $\ell_{\min} \in [0.10, 0.20]$ (range = 0.001, mean = 1.001 — indistinguishable from hard threshold while smooth). Tertiary differentiable recommendation: **Phi-3d shifted saturating with β = 20** (range = 0.005, mean = 0.938 — smooth everywhere, robust at all four $\ell_{\min}$). Default (φ-sat) envelope confirmed unsuitable for chart-invariant smooth count under split-bump refinement.
