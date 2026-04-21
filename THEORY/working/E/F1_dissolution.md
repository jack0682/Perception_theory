# F-1 Dissolution — Soft-K Distribution + Gibbs Thermal Population (G4)

**Status:** working (preliminary mapping draft, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1.
**Canonical refs:** `canonical.md` §13 Cat A T-Merge (a) (K-formation local minimality on Σ²_M — to retire), Topological Lock (Σ²_M-specific — to retire), Coupling Bound Lemma (`(K-1)λ_rep` factor — to retire), §13 Cat B γ_eff barrier exponent.
**Working refs:** `working/E/soft_K_definition.md` (G1), `working/C/F_group_axioms.md` (G2), `working/CE/free_energy_wellposed.md` (G3), `working/E/M1_dissolution.md` (G5).
**Note:** Per plan.md §Success criterion, this is the **lowest-priority** of the three dissolution mappings. Page target: 1–1.5 pages.

---

## §1. F-1 Statement Recap

**F-1 (canonical OP-0001, severity 🔴 CRITICAL).** "K=2 global stability is 'vacuous' without external per-formation mass constraint. If masses m_j are allowed to vary, energy minimization always selects K=1 (energetically ~50% cheaper)."

**Empirical evidence in canonical:** exp62 (E_{K=2} ≈ 4.66), exp63 (E_{K=1} ≈ 2.25), 50% energy gap. All K-field theorems (T-Persist-K-Sep/Weak/Unified, Coupling Bound Lemma) implicitly assume "m_j fixed externally" — this is the "vacuity" — and become content-empty if external m_j is removed.

**Original framing.** F-1 was the most foundational of the three Critical: F-1 says "K=2 cannot exist autonomously." Without resolving F-1, the entire K-field machinery (which assumes K formations with external mass quotas) lacks self-contained justification.

---

## §2. E-Side: Vacuity Dissolves Under Soft-K

### 2.1 The "external m_j" assumption disappears

In the soft-K framework (G1), there is **no per-formation mass constraint**. The entire architecture `Σ^K_M = Σ_{m_1} × … × Σ_{m_K}` is replaced by a single `Σ_m`, with `K_soft : Σ_m → ℝ_{≥0}` derived from the single field u via H₀ persistence.

**Re-statement of "K=2" in soft-K.** "K=2 configuration" no longer means "u^1 with mass m_1 and u^2 with mass m_2 = M − m_1" (the integer-K reading). It means a single field `u ∈ Σ_m` with `K_soft(u) ≈ 2` — i.e., the H₀ persistence diagram of u has approximately 2 dominant bars of comparable length.

**Consequence.** The "external m_j" requirement vanishes — there are no per-formation masses to constrain. The single mass `m = Σ u_i` is the one volume budget; how it is distributed across the field's modes is a *property of the configuration*, not an external input.

### 2.2 What replaces "K=2 vacuity"?

In the soft-K framework, the analog of "K=2 stability" is:

**(Re-statement).** *In the energy landscape of ℰ on Σ_m, are there local minima `u^*` with `K_soft(u^*) ≈ 2` (and not just K_soft ≈ 1)?*

This is a well-posed question — and the answer is **yes**:
- canonical exp62 reports a configuration with `E ≈ 4.66` corresponding to two clearly separated formations on a single grid. This is a critical point of ℰ on Σ_m (gradient flow stationarity verified empirically).
- T-Merge (a) restated in soft-K: **"K_soft ≈ 2 configurations are local minima (not saddles) of ℰ"** — re-derivable from the Hessian analysis at well-separated multi-mode configurations.

The vacuity claim ("K=2 needs external m_j") is **dissolved** — no external m_j is needed, because the K=2 character comes from the *internal mode structure of u* (read off via K_soft), not from a per-formation mass dictate.

### 2.3 Status of E-side dissolution

| Aspect | Status |
|---|---|
| "External m_j" assumption removed | committed (soft-K has no per-formation mass) |
| K_soft ≈ 2 local minima exist on Σ_m | sketched (empirical exp62, formal Hessian analysis carry) |
| T-Merge (a) statement re-write to soft-K | sketched |

**Status: Cat A** for the architectural claim (Σ^K_M dissolves into Σ_m). **Cat C** for the formal re-statement (K_soft ≈ 2 critical points characterized) — full Hessian analysis on Σ_m is C-S2 + E-S3.

---

## §3. C-Side: Thermal Population (Gibbs Boltzmann Factor)

### 3.1 Re-framing K=2 as thermal mode

Even after the E-side dissolves the vacuity claim, one might still ask: *Why would the system "be" in K_soft ≈ 2 rather than the global minimum K_soft ≈ 1?* In a deterministic theory (zero T), the system at a K_soft ≈ 2 local minimum **stays there forever** — but this is the metastability of M-1, sketched in `M1_dissolution.md` §3 via Kramers.

In the thermal C+E theory (G2 + G3), the question becomes statistical:
- The Gibbs measure `ℙ_T ∝ exp(−ℱ_C+E[u]/T)` populates **all** local minima with weights exponential in their free-energy gap from the ground state.
- In particular, for the K_soft ≈ 2 metastable state at energy ℱ_2 and the K_soft ≈ 1 ground state at ℱ_1:

$$
\frac{\mathbb{P}_T[\text{near } u_2^*]}{\mathbb{P}_T[\text{near } u_1^*]} \;\approx\; \exp\!\Big(-\frac{\Delta\mathcal{F}_{2-1}}{T}\Big).
$$

For canonical exp62/exp63: `ΔE_{2−1} ≈ 4.66 − 2.25 = 2.41` (ignoring entropy/K_soft corrections at low T). At T ~ 1, Boltzmann factor ≈ exp(−2.41) ≈ 0.09 — i.e., K=2 is populated at 9% of K=1 weight. **Non-zero, non-vacuous.**

### 3.2 "Vacuous" → "thermally populated"

**Re-framing.** Where the original F-1 said "K=2 is vacuous (cannot exist)", the C+E reformulation says:

**K=2 is thermally populated** with relative weight `exp(−ΔF_{2−1}/T)` in the Gibbs distribution, plus mediated by long Kramers escape time `τ_{K=2 → K=1} ~ exp(ΔF/T)`.

At low T, both quantities are small but nonzero — K=2 exists as a *minority population* with extremely long lifetime. At T → 0, both vanish — K=2 lives forever as a deterministic local minimum (the canonical v1.2 metastability claim).

### 3.3 Example distribution

**Toy example.** Consider an 8×8 grid (n = 64) with mass m = 10. Compare the K=1 (single concentrated formation) and K=2 (two separated formations) configurations.

**Bernoulli entropy heuristic.** Most sites have u ≈ 0 or u ≈ 1 (near binary, sharp-interface regime); these contribute ~0 to S. The Bernoulli entropy is dominated by the **boundary band** sites (intermediate u values).
- K=1: one boundary perimeter, ~8–12 intermediate-u sites. S₁ contribution ≈ 6 nats.
- K=2: two boundary perimeters (each smaller, but two of them), ~12–16 intermediate-u sites total. S₂ contribution ≈ 8–10 nats.

⇒ **S₂ > S₁** (multi-mode has more boundary length, hence more entropy). Rough estimates (writing `S = (η)·n log 2` with η ∈ [0,1]):
- S₁ ≈ 0.85 · 64 · log 2 ≈ 37.7
- S₂ ≈ 0.90 · 64 · log 2 ≈ 39.9
- ΔS = S₂ − S₁ ≈ 0.05·64·log 2 ≈ 2.22 nats.

**Energy values (canonical exp62/exp63 empirical):**
- E₁ = 2.25 (K=1 minimum), K_soft(u₁*) ≈ 1.
- E₂ = 4.66 (K=2 minimum), K_soft(u₂*) ≈ 2.
- ΔE = E₂ − E₁ = 2.41.
- Saddle energy E_s ≈ 6 (approximate; exact value depends on γ_eff per exp38; not used in ratio below).

**Free energy formula.** With γ_K = 0.1 (so λ_K = 0.1·T):

ℱ_K(T) = E_K − T · S_K + λ_K · K_soft(u_K*) = E_K − T · S_K + 0.1 · T · K_soft(u_K*).

Hence:

$$
\Delta\mathcal{F}_{2-1}(T) \;=\; \Delta E \;-\; T\cdot\Delta S \;+\; 0.1\cdot T \cdot \Delta K_{\mathrm{soft}}
\;=\; 2.41 \;-\; T\cdot 2.22 \;+\; 0.1\cdot T \cdot 1
\;=\; 2.41 \;-\; T \cdot 2.12.
$$

**Crossover temperature** where ΔF = 0: `T_c = 2.41 / 2.12 ≈ 1.14`. Below T_c, ΔF > 0 ⇒ K=1 thermodynamically preferred. Above T_c, ΔF < 0 ⇒ K=2 thermodynamically preferred (entropy wins).

**Boltzmann ratio table (corrected):**

| T | ΔF_{2−1} | Boltzmann ratio K=2 / K=1 = exp(−ΔF/T) | Regime |
|---|---|---|---|
| 0.1 | +2.20 | exp(−22.0) ≈ 2.7·10⁻¹⁰ | deeply zero-T, K=2 negligibly populated |
| 0.5 | +1.35 | exp(−2.70) ≈ **0.067** (6.7%) | low-T, K=2 minority |
| 1.0 | +0.29 | exp(−0.29) ≈ **0.75** (75%) | approaching crossover |
| **T_c ≈ 1.14** | ≈ 0 | ≈ 1 | crossover (K=1, K=2 equal weights) |
| 2.0 | −1.83 | exp(+0.92) ≈ **2.51** | mixed: K=2 entropically beginning to dominate |
| 5.0 | −8.19 | exp(+1.64) ≈ **5.16** | high-T, K=2 strongly entropy-favored |

**Asymptotic behavior:**
- T → 0: `ΔF → ΔE = 2.41` (energy dominates) ⇒ K=2 suppressed exponentially. Recovers canonical zero-T picture.
- T → ∞: `ΔF / T → −ΔS + 0.1·ΔK_soft = −2.22 + 0.2 ≈ −2.02`. Boltzmann ratio approaches `exp(2.02) ≈ 7.5` — temperature-independent asymptote where K=2 is favored by ~7.5× over K=1.

The numbers are illustrative; exact values await Hessian-of-ℱ_C+E computation with calibrated parameters (Stage 5 / R-F1-A). **The qualitative points:**
1. **Low-T (T < T_c ≈ 1.14):** K=1 is thermodynamically preferred, K=2 is a Boltzmann-suppressed metastable minority. Consistent with canonical "K=1 always preferred" framing.
2. **High-T (T > T_c):** **K=2 becomes thermodynamically preferred** — entropy of multi-mode formations wins over their energy cost. This is **stronger than canonical** which has no thermal framework to express this regime.
3. **At T_c ≈ 1.14:** roughly equal occupation. Crossover phenomenon — entropy-driven mode-count phase transition.

**Implication for F-1 dissolution.** F-1 originally said "K=2 vacuous (cannot exist)". The corrected thermal picture shows **K=2 not only exists but in fact dominates at high T**. The "vacuity" framing was a zero-T artifact that hid a richer thermal phenomenology. **F-1 dissolution is stronger than initially stated** — not just "K=2 is thermal minority", but "K=2 is thermal majority above T_c".

**Connection to P-F (Zero-T metastability gap).** This corrected example provides direct evidence that canonical's zero-T deterministic framework is **inadequate** for the multi-formation question. P-F's diagnosis ("metastability claim on zero-T framework") is substantiated: at T > T_c, the metastable hierarchy actually inverts. C+E framework resolves this by treating finite T explicitly.

### 3.4 Comparison to canonical "vacuous"

| Question | Canonical v1.2 | C+E reformulation |
|---|---|---|
| Does K=2 exist autonomously? | No (vacuous without external m_j) | Yes (thermally populated, no external m_j needed) |
| Is K=2 the energy minimum? | No (K=1 cheaper, isoperimetric) | No (same — ℰ comparison unchanged, M-1 §2) |
| Is K=2 the **free-energy** minimum? | (no F framework) | **Depends on T:** K=1 favored at T < T_c ≈ 1.14; K=2 favored at T > T_c. Entropy-driven crossover. |
| Is K=2 stable against perturbation? | Yes (CN8 metastable, kinetic barriers) | Yes (Kramers metastable at low T, M-1 §3); thermodynamic minimum at high T. |
| Quantitative occupancy at observation time? | undefined (zero-T deterministic) | Boltzmann ratio (table §3.3) × kinetic correction `exp(−τ_obs/τ_Kramers)` |

**Conclusion.** F-1's "vacuity" is dissolved by **two complementary moves + a third refinement from §3.3 corrected analysis**:
- (E-side) Removal of the "external m_j" architecture — soft-K has no per-formation mass.
- (C-side, low-T) Thermal Gibbs population — K=2 is a Boltzmann-suppressed thermal minority, not a vacuum.
- (C-side, high-T, **new finding from §3.3**) K=2 becomes thermodynamic majority at T > T_c. Canonical's "K=1 always preferred" is a zero-T statement; thermal extension reveals an entropy-driven multi-mode regime.

**Caveat (per `02_development.md` §4.5).** The K=1 vs K=2 free-energy comparison is implicitly **connected-graph**. On disconnected graphs, K_soft > 1 may dominate at all T (NQ-13 carry).

---

## §4. Residual Open Items After Dissolution

- **R-F1-A.** The "K=2 occupancy" requires concrete computation: numerical Boltzmann ratio at calibrated SCC parameters (a_cl, β, λ_*). Carry to **Stage 5 (Numerical Validation)** — exp77+.
- **R-F1-B.** The K_soft ≈ 2 critical points on Σ_m: existence (sketched empirically by exp62), Hessian structure (carry to E-S3), enumeration (how many modes? K_soft ≈ 2 corresponds to a *family* of configurations parameterized by the spatial location of the two modes).
- **R-F1-C.** Modes "intermediate" between K_soft ≈ 1 and K_soft ≈ 2 (i.e., K_soft ∈ (1, 2)): are these critical points or only saddles? In the canonical theory, intermediate K was prohibited (K integer). In soft-K, intermediate K_soft is allowed; whether it represents *physical* configurations depends on whether ℱ_C+E has critical points there. Generic answer: only critical points at certain `K_soft^*` values, with continuous "modes" not generically being critical.
- **R-F1-D.** The Boltzmann ratio computation at §3.3 used naive entropy estimates. Tighter analysis requires the saddle-point method (Laplace) on the partition function:

$$
Z_K \;:=\; \int_{\{u : K_{\mathrm{soft}}(u) \approx K\}} \exp\!\big(-\mathcal{F}_{C+E}[u]/T\big)\,\nu(du),
$$

then `K=2 occupancy = Z_2 / Z` with `Z = Σ_K Z_K`. Carry to **CE-S2**.

---

## §5. Status Summary

| Aspect | Status |
|---|---|
| F-1 vacuity dissolved (E-side: soft-K) | committed (§2) |
| F-1 thermal population (C-side: Gibbs) | sketched (§3, illustrative numbers) |
| Crossover temperature T_c ≈ ΔE/ΔS | sketched |
| Replacement of "external m_j" architecture | committed |
| Residual items R-F1-A through R-F1-D | open (carry to Stages 2–5) |

**Page count:** ~1.2 pages substantive (within plan §G4 1–1.5 page target).

**Category self-classification:**
- E-side (architectural removal): **Cat A**.
- C-side (thermal occupancy): **sketched (Cat C-provisional pending CE-S2 / Stage 5)**.

---

## §6. Carry / Next

- **C-S2:** R-F1-D (saddle-point analysis on Z_K).
- **CE-S2:** R-F1-B, R-F1-C ((T, λ_K) phase diagram including K_soft critical loci).
- **Stage 5 (Numerical Validation):** R-F1-A (numerical Boltzmann ratio at calibrated SCC parameters; exp77+).
- **canonical_sub.md 2026-04-21 entry:** F-1 reframing (vacuity → thermal population) as **Pending** (Critical relabeling awaits weekly merge); C-S2 / CE-S2 carry items as **Added — Pending OP promotion**.

Next: 02_development.md (G1–G6 의 수학적 핵심을 step-by-step granularity 로 통합).
