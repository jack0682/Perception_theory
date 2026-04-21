# M-1 Dissolution — Isoperimetric Feature + Kramers Metastability (G5)

**Status:** working (preliminary mapping draft, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1.
**Canonical refs:** `canonical.md` §13 Cat A T-Merge (b) (Energy Ordering Isoperimetric), §13 Cat A T11 (Γ-convergence), §14 CN6 (kinetically determined), CN8 (metastable not globally optimal), CN14 (closure expands metastability — `β^{0.89}`); §13 Cat B "Barrier Exponent γ_eff ≈ 0.89" (empirical from exp38).
**Working refs:** `working/E/soft_K_definition.md` (G1), `working/C/F_group_axioms.md` (G2), `working/CE/free_energy_wellposed.md` (G3), `working/integer_K_dependency_map.md` §2.2 (T-Merge (b) Re-prove retain).
**External refs:** Modica-Mortola (1977), *Un esempio di Γ-convergenza*, Boll. UMI; Kramers (1940), Eyring (1935), Hänggi-Talkner-Borkovec (1990) review for prefactor.

---

## §1. M-1 Statement Recap

**M-1 (canonical OP-0002, severity 🔴 CRITICAL).** "The K=2 energy landscape `E(m_1, m_2)` where `m_1 + m_2 = M` is monotonically decreasing as one formation size decreases (m_2 → 0). Therefore, K=1 with total mass M is always energetically cheaper than any K=2 split."

**Empirical evidence in canonical:** exp62 (E_{K=2} ≈ 4.66, E_{K=1} ≈ 2.25), exp63, exp71–73; T-Merge (b) (Cat A) is the proved theorem statement.

**Original framing as a problem.** Treated as "K=1 is always preferred → K>1 cannot emerge from energy minimization → theory cannot explain multi-formation." The implicit assumption was that emergence of multi-formation must be **thermodynamic** (energy-favored). This assumption is the source of M-1 being a "problem" (cf. `working/open_problems_reframing_2026-04-19.md` §9: M-1 is "not a problem but a proved theorem reframed as a problem by prior framing").

---

## §2. Isoperimetric Feature (E side — soft-K view)

### 2.1 Re-statement under soft-K

In the soft-K framework (G1), "K=1" and "K=2" are not distinct integer states but values of `K_soft(u)`. The relevant variational comparison is no longer "min over K=1 configs vs min over K=2 configs" (this discrete dichotomy dissolves), but rather:

**Re-statement (soft-K):** *On Σ_m, the minimizers of ℰ are concentrated configurations (`K_soft(u^*) ≈ 1`). Configurations with `K_soft(u) > 1` (multi-mode) have strictly higher ℰ.*

This is the **same content** as M-1, expressed without integer-K commitment. The "preference for K=1" becomes "preference for low-K_soft" — a property of ℰ, not a problem.

### 2.2 Mathematical core (Modica-Mortola Γ-convergence)

The mathematical engine is the Modica-Mortola Γ-convergence theorem:

**Theorem (Modica-Mortola 1977; canonical T11, Cat A).** As `ε = α/β → 0`, the energy `ℰ_bd(u) = α Σ_{x,y} N(x,y)(u_x - u_y)² + β Σ u²(1-u)²` Γ-converges (after rescaling by `√(αβ)`) to the perimeter functional:

$$
\mathcal{E}_{\mathrm{bd}}(u) \;\xrightarrow{\Gamma}\; c_W \cdot \mathrm{Per}\!\big(\{u = 1\}\big),
$$

with `c_W = ∫_0^1 √(2 W(s))\, ds` the surface tension constant.

**Consequence (perimeter minimization).** Among configurations with fixed volume `m`, the one minimizing perimeter (under suitable graph regularity) is a **single connected region** of size m — by the discrete isoperimetric inequality. Multi-region configurations have perimeter `≥ K · Per(single region of mass m/K)`, which is generally larger than `Per(single region of mass m)` for any K > 1.

**Soft-K interpretation.** In the soft framework, "single connected region" corresponds to `K_soft(u^*) ≈ 1` (one dominant H₀ bar of long length). "Multi-region" corresponds to `K_soft(u) > 1`. The Modica-Mortola argument shows that single-region (low-K_soft) is energetically preferred by ℰ alone.

### 2.3 Status of the re-stated claim

**Status: Cat A** — same as canonical T11, T-Merge (b). **No re-proof needed; only re-statement.** Per `working/integer_K_dependency_map.md` §2.2, T-Merge (b) is the unique "Re-prove (retain)" item: the proof core (Γ-conv perimeter minimization) survives the soft-K rewrite intact.

### 2.4 Reframing of M-1 as feature, not bug

**Conclusion (feature interpretation).** M-1 is **not a bug** in the SCC theory — it is a **mathematical feature** consistent with Γ-convergence and isoperimetric inequalities. The theory correctly predicts that single-mode is energy-favored. The existence of K_soft > 1 multi-mode configurations as **observed phenomena** (which the canonical theory does need to account for) cannot be explained by ℰ-minimization alone — it requires **kinetic stability** (next section, C side).

This was anticipated implicitly by canonical CN8 ("formations are metastable, not globally optimal") and CN6 ("K is kinetically determined"). The C+E reformulation makes this thermodynamic-vs-kinetic distinction **rigorous** (rather than commitment-noted).

---

## §3. Kinetic Metastability (C side — Kramers)

### 3.1 Setup

In the thermal SCC framework (G2 + G3), the system is governed by Langevin SDE F3 at temperature T > 0, with stationary measure `ℙ_T ∝ exp(-ℱ_{C+E}/T)`. ℱ_{C+E} has multiple critical points (G3 §3.3): the global minimizer at `K_soft ≈ 1` (single-mode), and **higher-energy local minima at K_soft ≈ 2, 3, …** (multi-mode).

**Definition (metastable state).** A local minimum `u_K^*` of ℱ_{C+E} with `K_soft(u_K^*) ≈ K` for K ≥ 2 is **metastable**: thermal noise eventually drives the system to the global minimum (K=1), but the **escape time** is exponentially long in T^{-1}.

### 3.2 Kramers escape rate

**Kramers formula (1940; sharp-interface or weak-noise limit).** For a Langevin process in a potential well `u_a^*` separated from a deeper basin by a saddle `u_s^*`, the mean first-passage time (MFPT) from `u_a^*` to the deeper basin is:

$$
\boxed{\;\;\tau_{a \to b} \;=\; \tau_0(u_a^*, u_s^*) \cdot \exp\!\Big(\frac{\Delta\mathcal{F}}{T}\Big)\;\;}
$$

where:
- `ΔF = ℱ_{C+E}[u_s^*] - ℱ_{C+E}[u_a^*]` is the **barrier height** (free energy of saddle minus that of the metastable minimum);
- `τ_0` is the **prefactor**, depending on Hessian determinants:

$$
\tau_0 \;=\; \frac{2\pi}{|\omega_s|}\cdot \sqrt{\frac{\det H(u_a^*)}{|\det H(u_s^*)|}},
$$

with `|ω_s|` the magnitude of the unique negative-eigenvalue at the saddle, and `H` the constrained Hessian on `T_{u^*} Σ_m`.

### 3.3 Application to K=2 → K=1 in SCC

**Claim (G5 commit).** For SCC's K_soft ≈ 2 metastable state and K_soft ≈ 1 ground state (separated by a saddle K_soft ≈ 1.5):

$$
\tau_{K=2 \to K=1} \;=\; \tau_0 \cdot \exp\!\Big(\frac{\Delta\mathcal{F}_{2\to 1}}{T}\Big),
$$

with `ΔF_{2→1} ≈ ΔE_{2→1} - T·(S_2 - S_s) - λ_K·(K_soft(u_2^*) - K_soft(u_s^*))`. 

For canonical exp62/exp63 evidence: `ΔE_{2→1} ≈ 4.66 - 2.25 = 2.41` (energy difference). At low T (`T ≪ ΔE`), entropic and K_soft corrections to ΔF are subleading, and:

$$
\tau_{K=2 \to K=1} \;\approx\; \tau_0 \cdot \exp\!\Big(\frac{2.41}{T}\Big).
$$

**Numerical scale.** At `T = 0.1`: `exp(2.41/0.1) ≈ exp(24.1) ≈ 3·10^{10}` — astronomical timescale relative to relaxation time. K=2 effectively eternal. At `T = 1.0`: `exp(2.41) ≈ 11` — short timescale, K=2 indistinguishable from equilibrium fluctuation.

**Status of (3.3) claim.** Sketched — full rigor requires:
- Constrained Hessian computation at K_soft ≈ 2 minimizer (G3 §3.3 conditional).
- Identification of saddle u_s^* between K=2 and K=1 basins (a non-trivial transition state — variational saddle point on Σ_m, not on Σ²_M which doesn't exist in soft-K framework).
- Kramers formula on Σ_m (constrained Hessian, projection onto T_u Σ_m) — pre_brainstorm H-H3 risk.

Carry to **C-S2** for full Kramers prefactor derivation (consistency with empirical γ_eff = 0.89 — see §4 below).

### 3.4 Substantiation of CN6, CN8, CN14

**CN6 (K kinetically determined):** Substantiated. K_soft ≈ K for K ≥ 2 is a **metastable** state of ℱ_C+E. Whether the system is observed at K_soft ≈ K depends on initial conditions and the relative magnitudes of `τ_{K→K-1}` and observation timescale `τ_{obs}`:
- `τ_{K→K-1} ≪ τ_{obs}`: thermalized to K = 1 (canonical T-Merge (b) statement realized).
- `τ_{K→K-1} ≫ τ_{obs}`: K_soft > 1 observed as quasi-equilibrium.

This is the **thermodynamic substantiation** of "K is kinetically determined" — kinetic = barrier-rate-determined within the thermal Gibbs framework.

**CN8 (metastable not globally optimal):** Substantiated. Boltzmann population of K=2 basin: `Z_2 / Z = exp(−(ℱ_2 − ℱ_1)/T) · (volume_2 / volume_1) ≈ exp(−ΔF/T) · O(1)`. Non-zero at any `T > 0` — K=2 is *populated* but *suppressed*. Both "exists" (CN8) and "is not globally optimal" (T-Merge (b)) hold simultaneously, without contradiction.

**CN14 (closure expands metastability):** Re-cast. CN14 claims closure increases barrier height (canonical: `β^{0.89}` with closure vs `β^{0.85}` for pure Allen-Cahn, exp38/57). Under Kramers framework: increased barrier ⇒ longer τ ⇒ wider region of (T, observation timescale) space where K>1 appears stable. The 30% reduction in `d_min^*` (canonical CN14) becomes a Kramers-rate consequence: closer formations have lower barrier (smaller ΔF), but closure raises ΔF enough to extend the metastable regime to closer `d_min`.

---

## §4. Empirical Re-interpretation (exp38, exp55)

### 4.1 exp38: barrier exponent γ_eff ≈ 0.89

**Empirical fact (canonical Cat B).** exp38 reports merge barrier ΔE ∝ β^{0.89} with R² = 0.997 over β ∈ [20, 100]. Currently classified as Cat B "empirical fit, not derived" — branch/path-conditioned per 2026-04-10 erratum.

**Kramers-prefactor reinterpretation (sketch).** Under Kramers formula (3.2), the barrier "height" appears in the **exponent** as `ΔF`. The β-dependence of `ΔF` is via:
- ℰ_bd's β-coefficient on the double-well: `β · Σ u²(1-u)²`. At the saddle (transition state where the K=2 → K=1 merge reduces a "neck"), the integral over the neck region scales with β.
- Specifically, in sharp-interface (Modica-Mortola) limit, `ΔE_bd ~ √(αβ) · Per(transition state)` (from T11 Γ-conv normalization).

The empirical exponent 0.89 is **lower than 1 (linear in β) and lower than 0.5 (square-root scaling)**. It sits between, suggestive of a *crossover* between sharp-interface (`√β`) and bulk-dominated (`β`) regimes within the explored β-range. This is consistent with Kramers prefactor analysis: at moderate β, the saddle is not yet sharp-interface, so the simple scaling is corrected by Hessian-related prefactor (which itself is `β`-dependent through ω_s and `det H`, giving an additional fractional power).

**Specifically (sketch).** With `det H ~ β^k` for some `k` (Hessian eigenvalues scale with β through the double-well curvature), `τ_0 ~ β^{(k_a - k_s)/2}`, and total `τ ~ β^{(k_a-k_s)/2} · exp(c·β^{γ}/T)` for some `γ`. Fitting log τ vs log β across β-range gives a single effective exponent that mixes prefactor and exponent contributions. **Numerical claim:** `γ_eff = 0.89` is consistent with `γ = 1` (linear bulk barrier) plus prefactor correction `~ β^{-0.11}`. Detailed derivation deferred to **C-S2**.

**Status of reinterpretation:** *consistent-with*, not *derived-from*. (per H-H5 risk: do not overclaim.) Plan §G5 commitment is "재유도 시도" (attempted re-derivation), not "재유도 완료" (completed). exp77+ would test prefactor predictions against new measurements at varied parameters.

### 4.2 exp55: zero-merge in 5000 iterations at σ ≤ 0.5, β = 30

**Empirical fact (canonical CN14, exp55).** Well-separated K=4 formations on a 10×10 grid show **zero merges** in 5000 gradient-flow iterations under noise σ ≤ 0.5 with β = 30.

**Kramers reinterpretation.** With T identified to noise scale by `T = σ²/2` (standard Langevin-noise dictionary):
- σ = 0.5 ⇒ T = 0.125.
- ΔE_{merge} ≈ 20 (canonical CN14 for SCC at β = 30 with closure).
- `exp(20/0.125) = exp(160) ≈ 10^{69}` — astronomical. Effectively `τ_merge → ∞` in any practical observation window.

**Predicted MFPT (Kramers):** `τ ≈ τ_0 · 10^{69}`. Even with `τ_0 ~ 1`, this is unmeasurably long. Hence **zero merges is not just consistent with Kramers; it is the predicted behavior**.

**Consistency with T → 0 limit (F4.a).** As `T → 0` (i.e., `σ → 0`), `τ → ∞`. exp55 sits at the low-T end where the Kramers limit (zero noise) is well-approached, hence zero merges is the deterministic consequence.

### 4.3 Combined empirical summary

| Experiment | Reported | Kramers re-interpretation | Status |
|---|---|---|---|
| **exp38** | ΔE ∝ β^{0.89} | Mix of bulk-barrier exp (`γ ≈ 1`) + Hessian prefactor (`-0.11`). Crossover regime in tested β-range. | sketched (consistent with) |
| **exp55** | zero merges, σ ≤ 0.5, β = 30 | `τ ≈ 10^{69}` Kramers MFPT — **predicted** zero merges | sketched (predicted by) |
| **exp57** | `d_min^* ≈ 5` (SCC) vs `≈ 7` (AC) | Closure raises barrier ⇒ longer τ ⇒ wider d_min^* — quantitative shift. | sketched (consistent with) |

These are the canonical empirical pillars previously interpreted within the kinetic CN6/CN8/CN14 commitment. Under C+E framework, they become **predictions of a thermodynamically-grounded Kramers analysis** — consistent with prior interpretations but on rigorous footing.

---

## §5. Residual Open Items After Dissolution

The C+E reformulation does **not** completely close the M-1 thread. Residuals:

- **R-M1-A.** Kramers prefactor `τ_0` derivation on **constrained Σ_m manifold** — projected Hessian, rank-deficient (n−1 vs n). Standard Kramers is on ℝ^n. Carry to C-S2.
- **R-M1-B.** Identification of the **transition state** (saddle) between K_soft ≈ 2 and K_soft ≈ 1 minima. On Σ²_M (integer-K manifold) this was the merge corner — vacuous (Topological Lock retraction R2). On Σ_m (single field, soft-K), the saddle is a variational object: a critical point of ℰ + S + λ_K K_soft with one negative Hessian eigenvalue. Existence: by Mountain Pass theorem (now applicable on Σ_m which is connected and where path between K_soft ≈ 2 and K_soft ≈ 1 minima exists). Status: existence by Mountain Pass — sketched. Quantification of saddle ℱ value: open.
- **R-M1-C.** Empirical γ_eff = 0.89 derivation precision: sketched as "consistent with linear bulk + prefactor correction". Full derivation requires Hessian eigenvalue scaling analysis on the transition state — C-S2.
- **R-M1-D.** Connection between `λ_K · K_soft` regularization and barrier height: `ΔF_{2→1}` includes `λ_K · (K_soft(u_2^*) − K_soft(u_s^*))`. With `λ_K = γ_K·T`, this contributes O(γ_K · T) to ΔF — small. But at the saddle where K_soft varies rapidly, this could be non-negligible. Detailed analysis carry.
- **R-M1-E.** Multi-K sequential merging (K=4 → K=3 → K=2 → K=1) involves a cascade of Kramers transitions. Total merger time = sum of MFPTs. At fixed T, the slowest step dominates. Ostwald-ripening-style coarsening (pre_brainstorm H-E8) may apply. Carry to E-S3.

---

## §6. Status Summary

| Aspect | Status |
|---|---|
| M-1 re-framed as feature (E side, isoperimetric) | committed (§2; reuses Cat A T-Merge (b) and T11) |
| M-1 metastability substantiated (C side, Kramers) | sketched (§3; full Kramers prefactor C-S2) |
| Empirical exp38, exp55, exp57 re-interpreted | consistent-with, not derived-from (§4) |
| CN6, CN8, CN14 thermally substantiated | yes (§3.4) |
| Residual open items | R-M1-A through R-M1-E (§5) |

**Page count:** roughly 2 pages of substantive content (within plan §G5 1.5–2 page target).

**Category self-classification:**
- Re-framing of M-1 as feature: **Cat A** (uses Cat A T-Merge (b), T11 directly).
- Kramers metastability quantification: **sketched** (Cat C-provisional pending C-S2).

---

## §7. Carry / Next

- **C-S2:** R-M1-A (Kramers prefactor on constrained Σ_m), R-M1-C (γ_eff=0.89 derivation precision).
- **E-S3:** R-M1-E (multi-K cascade, Ostwald-ripening coarsening).
- **canonical_sub.md 2026-04-21 entry:** M-1 reframing as Clarified (CN6/CN8/CN14 thermal interpretation); Kramers/exp38 reinterpretation as Pending.

Next file: `working/E/MO1_dissolution.md` (G6).
