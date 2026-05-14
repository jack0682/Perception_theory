> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 06 — Open Problems and Residuals (Post-CV-1.13)

This file distinguishes **blocking** from **non-blocking** open problems after CV-1.13 seal. The Cat A path for single-formation temporal identity is now complete; what remains is either non-blocking refinement or Phase 2 multi-formation/dynamics work.

---

## 1. Non-blocking Residuals

### OP-SB1-084 — LOW

**Status:** OPEN / LOW priority, **non-blocking** for CV-1.13.

**Statement:** Determine the smallest provable isoperimetric constant $C_\mathrm{iso}$ on canonical 15×15 SCC minimizers such that

$$\rho_\mathrm{sym}(C_\mathrm{iso}, \bar m, \bar\theta_\mathrm{core}) = \bar\theta_\mathrm{core}\!\left(1 - \frac{4 C_\mathrm{iso}}{\sqrt{\bar m}}\right) = 0.84.$$

Equivalently: derive HWF-1 ($\mathrm{iso\_ratio}(\mathrm{Core}) \leq C_\mathrm{iso}$) from (A1)–(A7), or give a tight analytic calibration of $C_\mathrm{iso}$ for canonical compact disk-like minimizers.

**Why it doesn't block CV-1.13:**
- T-Temporal-Identity (b) Cat A requires only $\Delta_\mathrm{sep} > 0$ (positivity), which is handled by **Lemma S-B1-Weak Cat A** ($\rho_\mathrm{deep} \geq 0.7/225 > \rho_* \approx 0.003$).
- The quantitative magnitude $\Delta_\mathrm{sep}^* \approx 0.84$ is given by S-B1-SYM (Cat B) under HWF-1, sufficient for Cat B documentation of the magnitude.
- The remaining gap is only the analytic derivation of HWF-1 from canonical axioms, not any temporal-identity blocker.

**Effect of resolving:** S-B1-SYM would promote Cat B → Cat A (quantitative magnitude bound), and the literal value 0.84 would become a fully analytic theorem constant rather than a numerical evaluation.

**Successor relationship:** OP-SB1-084 supersedes OP-SB1-DEEP (which was registered W7-FINAL, downgraded W7-CV113, superseded W7-CV113A).

---

## 2. Remaining Cat B / Cat C / R Items (from `theorem_status.md`)

Listed below are non-Cat-A claims drawn from the canonical theorem registry as of CV-1.13 (HT-3.5). All items are unchanged from CV-1.12 unless noted.

### Cat B (14 total)

Notable rows (not exhaustive; see `theorem_status.md` for the full registry):

- **D-ST-1, D-ST-2, D-ST-3, D-ST-4, D-ST-5** — Stereo-SCC extension definition rows; canonical bodies in `canonical.md §3.9–§3.11` and §16.
- **T-ST-5b** — Smooth-Depth Barrier Raising. Cat B; narrow claim (full SCC β=10 regime).
- **T-P-F-ε0-K** — Kramers Exponent Stability under Bernoulli regularization. Cat B conditional on H-MORSE / H5 (Morse stability) — Cat A path runs through H-MORSE.
- **T-K-Select-PF** — Equilibrium K-Selection under P-F-A1 Package I. Cat B; Cat A path needs σ_M-null computation + per-instance K_feas characterization.
- **T-K-Select-OBS** — Observation-Conditioned K-Selection. Cat B; Cat A path needs full stereo likelihood canonicalization + temporal extension.
- **Lemma S-B1-SYM** — Symbolic deep-core density identity. Cat B; Cat A path is OP-SB1-084.
- **(OP-OMS-032b, OP-OMS-033b, OP-OMS-034b, OP-OMS-034c)** — OMS Cat B residuals (non-blocking formalities; static / temporal robustness).
- (Several historical Cat B rows from CV-1.8 / CV-1.9 era — see registry.)

### Cat C (5 total)

- **T-σ-Inherit (parts c, d-σ_standard)** — σ_standard inheritance under MERGE/SPLIT. Cat C pending OP-0008 Wigner-projection W9+.
- **T-Persist-1(d)** — Interior Gap Lower Bound. Cat C — β > 7α necessary condition; structural limit.
- (Plus three other historical Cat C rows.)

### Retracted (5 total)

- Historical retraction rows preserved in `theorem_status.md` with `*(Retracted YYYY-MM-DD: reason)*` markers, per the canonical contamination policy.
- Note: legacy S-B1 Strong (literal $\rho_\mathrm{deep} \geq 0.84$ unconditional) is **superseded, not retracted as Cat R** — it remains as a Cat B conditional row in the registry, with the standalone interpretation supersession.

**Do not invent counts.** The registry's official counts at CV-1.13 are:

$$59\text{A} \;+\; 14\text{B} \;+\; 5\text{C} \;+\; 5\text{R} \;=\; 83 \text{ claims}.$$

---

## 3. Critical Path After CV-1.13

The critical path now moves to Phase 2 multi-formation / dynamics work.

### Primary recommendation

**H-MORSE / Package II.** Reasoning:
- H-MORSE (Morse stability of constrained energy critical points) is the gating dependency for T-PF-ε0-K Cat A and for Package II (Eyring-Kramers / metastable transition rates).
- Closing H-MORSE unlocks transition-rate formulas $\Gamma_K$ and the Kramers prefactor, which are needed for D-ST-4 rate claims and dynamic K-selection.
- It also feeds H-SR (spectral repulsion) — Morse critical-point structure gives explicit $\mu_k$ lower bounds.

Status: OPEN, major. Numerically: $\mu_\mathrm{min} \in [0.96, 60.2]$ across configurations (from prior experiments) — provides strong evidence but not proof. Symmetry / volume-constraint zero modes are the main risk.

### Alternative

**T-σ-Inherit / OP-0008.** Reasoning:
- T-Temporal-Identity Cat B is the registered prerequisite for T-σ-Inherit; now that CV-1.13 makes it Cat A, T-σ-Inherit can proceed.
- OP-0008 has four sub-problems: CONT, MERGE, SPLIT, DIST. MERGE centroid + orientation are Cat B; σ_standard Cat C requires Wigner-projection (W9+).
- Closing OP-0008 advances multi-formation identity (Q6) — the natural successor to single-formation identity (Q5).

This is a parallel option, not a substitute. Both paths are independent — they do not block each other.

### Tertiary

- **H-T*** (OP-0021) — T_* canonical registration. Still axiomatic. Currently the limiting factor for any rate-prediction claim.
- **OP-SB1-084** (LOW) — Tight analytic $C_\mathrm{iso}$ for S-B1-SYM.

---

## 4. What Not To Reopen

Explicit non-reopen list. These are now closed at Cat A and should not be re-examined under standard work; only under explicit theoretical re-foundation:

- **H-SINK is closed Cat A.** Full plan stability for canonical SCC E1 (one-sided sub-stochastic OT) is proved via Theorem Partial-H-SINK + the H-SINK lemma chain. Do not re-open the partial-OT gap.
- **T-Temporal-Identity is Cat A.** All four parts (a/b/c/d) certified via S-A1 / S-A3 / S-C1. Do not re-open under the existing single-formation scope.
- **The literal 0.84 should not be restored as a universal theorem constant.** It is `ρ_sym(0.2, 25, 1.0)` — a sharp-interface evaluation of the symbolic identity S-B1-SYM (Cat B), not a free-standing analytic bound. Treat 0.84 as **symbolic evaluation** or **legacy/provisional**, never as a universal theorem constant.
- **S-B1-Weak is sufficient for temporal positivity.** $\Delta_\mathrm{sep} > 0$ is fully established Cat A; one does not need the stronger 0.84 magnitude bound to claim Cat A for T-Temporal-Identity (b).
- **OP-SB1-DEEP is superseded.** Do not reopen as a blocking item. Use OP-SB1-084 as the active successor (LOW priority).
- **The S-C1 margin correction is canonical.** $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}$ (factor 2). Do not restore the original $+\epsilon_\mathrm{kernel}$ — that form does not algebraically close the proof.

---

## 5. Carry-forward for next agent

- Carry the **CV-1.13 sealed state** as the baseline.
- T-Temporal-Identity Cat A is **the new floor**; do not weaken it.
- Treat H-MORSE / Package II as the primary CV-1.14 candidate, T-σ-Inherit / OP-0008 as the secondary candidate.
- Treat the existing 215+1xfailed pytest baseline as authoritative for code-level validation; no code changes in W7.

Pre-brainstorm exploration of CV-1.14 routes is in `08_pre_brainstorm_CV114.md`. The handoff prompt is in `09_agent_handoff_prompt.md`.
