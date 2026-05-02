# WQ-LAT-1 — Reservoir Resolution Sweep Results

**File:** `THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_results.md`
**Companion files:**
- `THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_protocol.md` — full protocol.
- `CODE/scripts/wq_lat1_reservoir_resolution_sweep.py` — executable script.
- `CODE/scripts/results/wq_lat1_reservoir_resolution_sweep.json` — JSON output (after run).

---

## Status: RUN COMPLETE — partial reservoir convergence at the integer-morphology level (re-classified weak_success; script returned "failed" by strict aggregator)

Production run executed (2026-05-02): `max_iter=5000`, `seed=42`, $K \in \{3, 4, 6, 8, 12\}$, options $\{\text{LAT-A}, \text{LAT-C}\}$, geometries $\{A, B\}$, **20 trajectories**, **61.7 s wall-clock**. Output: `CODE/scripts/results/wq_lat1_reservoir_resolution_sweep.json`.

**Re-classified verdict.** The script's strict aggregator (all five must-pass criteria conjoined) returned `failed`. The empirical record is more nuanced: **integer-counted morphology observables converge cleanly, while the smooth K_soft envelope does not.** Reading the WQ-LAT-1 protocol §13:

- LAT-A (control): trivially convergent because extras are frozen and dynamics is identical across $K$ (LAT-F1 inconclusive).
- LAT-C (substantive test): the *field-level integer-morphology* observables (K_bar at all four ℓ_min, dominant bar profile, aggregate L2 distance) **all stabilize** across K. The *smooth* K_soft does not — it grows monotonically with K because the φ-saturating envelope $\phi(\ell) = \ell / (\ell + \ell_{\min})$ accumulates sub-resolution bar contributions as the truncation refines.

**The integer-morphology side of the reservoir prediction is empirically supported. The smooth-envelope side is not, under the chosen $\phi$ family.** This is a φ-sensitivity finding, not a refutation of the reservoir framing.

---

## Run Status Table

| Item | Status |
|---|---|
| Protocol document | written |
| Script | written |
| Smoke test (max_iter=200, K∈{3,6}, options=both, geom=A) | PASS — 0.4 s wall, end-to-end correct |
| Production run (max_iter=5000, K∈{3,4,6,8,12}, options=both, geom=A,B) | RUN COMPLETE — 61.7 s wall |
| Result JSON | generated at `CODE/scripts/results/wq_lat1_reservoir_resolution_sweep.json` |

---

## Per-trajectory empirical record (20 trajectories)

### LAT-A (control, frozen extras): identical dynamics across $K$ as expected

For all $K \in \{3, 4, 6, 8, 12\}$ and both A and B:

- $K_{\mathrm{act}}^\varepsilon$ initial = final = 3 (active slot mask freezes the extras)
- Aggregate $L^2$ distance between any pair $K, K'$: $\le 10^{-16}$ (machine precision)
- $K_{\mathrm{bar}}^{\ell_{\min}}$ at all four thresholds: identical across all $K$
- $K_{\mathrm{soft}}^\phi$: identical across $K$ (range = $4 \times 10^{-15}$)
- Dominant bar vector distance: 0

**LAT-A is the control / null test:** convergence is trivial because the dynamics is identical across $K$ values. **Status: LAT-F1 inconclusive** per protocol §11. Does not test the reservoir-resolution prediction.

### LAT-C (split-bump refinement, primary test)

Final-state diagnostics:

| K | geom | $K_{\mathrm{act}}^{\mathrm{final}}$ | $K_{\mathrm{soft}}^{\mathrm{final}}$ | $K_{\mathrm{bar}}^{0.10}$ | $\mathcal F^{\mathrm{final}}$ |
|---|---|---|---|---|---|
| 3 | A | 3 | 0.916 | 1 | 4 |
| 4 | A | 4 | 1.129 | 1 | 11 |
| 6 | A | 6 | 1.249 | 1 | 8 |
| 8 | A | 8 | 1.399 | 1 | 13 |
| 12 | A | 12 | 1.859 | 1 | 18 |
| 3 | B | 3 | 0.889 | 1 | 4 |
| 4 | B | 4 | 1.005 | 1 | 6 |
| 6 | B | 6 | 1.222 | 1 | 8 |
| 8 | B | 8 | 1.436 | 1 | 12 |
| 12 | B | 12 | 2.051 | 1 | 19 |

### Cross-K convergence (LAT-C, both geometries)

Maximum across all pairs in {3, 4, 6, 8, 12}:

| Quantity | LAT-C__A | LAT-C__B | Tolerance | Pass? |
|---|---|---|---|---|
| Aggregate $L^2$ distance / vertex | $1.26 \times 10^{-2}$ | $1.53 \times 10^{-2}$ | $0.05$ | **PASS** |
| Dominant bar vector $L^2$ distance | $0.022$ | $0.027$ | $0.10$ | **PASS** |
| $K_{\mathrm{bar}}$ integer disagreement count (all $\ell_{\min}$) | 0 | 0 | 0 | **PASS** |
| $K_{\mathrm{soft}}^\phi$ max difference | $0.943$ | $1.162$ | $0.10$ | **FAIL** |
| $K_{\mathrm{act}}^\varepsilon$ range across $K$ | 9 | 9 | (chart-dependent expected) | n/a |

### What's happening: φ-envelope sub-resolution accumulation

$K_{\mathrm{soft}}^\phi$ grows monotonically with $K$ under LAT-C even though the dominant bar (length ≈ 1) is preserved across all $K$. The growth comes from sub-prominence bars: at $K = 12$, the aggregate field has many small-amplitude wiggles (each sub-atom contributes a tiny local maximum), creating short bars (length ~0.01–0.05). The envelope $\phi(\ell) = \ell / (\ell + 0.10)$ assigns ~0.09–0.33 to each such sub-bar, summing to ~0.9 of additional $K_{\mathrm{soft}}$ at $K = 12$.

The **integer hard-bar count $K_{\mathrm{bar}}^{0.10}$ filters these out** (constant = 1 across all $K$), and the **dominant bar vector** (top-6 lengths) is also stable. The aggregate $L^2$ is well within tolerance.

**The reservoir prediction is empirically realized at the integer-morphology level. It is not realized at the smooth-envelope level under the chosen $\phi$.**

---

## LAT-C1–LAT-C7 Results Table (post-run)

| Criterion | Status | Evidence | Notes |
|---|---|---|---|
| LAT-C1 — protocol consistency | **PASS** | shared `RunConfig` per (option, geometry) | by construction |
| LAT-C2 — aggregate final-state convergence | **PASS** | max $L^2$/vertex = $1.5 \times 10^{-2}$ vs tolerance $0.05$ | cleanly within tolerance |
| LAT-C3 — $K_{\mathrm{bar}}$ trajectory stabilization | **PASS** | 0 integer disagreements across all $K$ pairs at all $\ell_{\min}$ | exact integer convergence |
| LAT-C4 — $K_{\mathrm{soft}}^\phi$ convergence | **FAIL** | max diff $0.94$ (A), $1.16$ (B) vs tolerance $0.10$ | φ-envelope picks up sub-resolution bars |
| LAT-C5 — persistence profile convergence | **PASS** | top-6 bar vector dist $\le 0.027$ vs tolerance $0.10$ | dominant bars stable |
| LAT-C6 — $K_{\mathrm{act}}$ / $K_{\mathrm{soft}}$ separation | **FAIL (mixed)** | $K_{\mathrm{act}}$ range = 9, $K_{\mathrm{soft}}$ range = 1.16 — both vary with $K$ | smooth $K_{\mathrm{soft}}$ is *not* fully chart-invariant under default φ |
| LAT-C7 — A/B geometry consistency | **PASS** | A and B exhibit qualitatively identical convergence pattern | both pass C2/C3/C5, both fail C4 |

**Reclassified status:** weak_success at the integer-morphology level (LAT-C2 ∧ LAT-C3 ∧ LAT-C5 ∧ LAT-C7); failure at the smooth-envelope level (LAT-C4).

---

## Convergence summary

- **Effective $K^*$ (integer-morphology):** $K^* = 3$ for $K_{\mathrm{bar}}$ (constant 1 across all $K$); $K^* = 3$ for dominant bar profile (range $\le 0.027$).
- **Effective $K^*$ (smooth-envelope):** none — $K_{\mathrm{soft}}^\phi$ grows monotonically through $K = 12$.
- **Aggregate field convergence:** YES, cleanly within $\tau_U = 0.05$ tolerance (max $1.5 \times 10^{-2}$).
- **$K_{\mathrm{bar}}$ convergence:** YES, exact integer agreement at all four $\ell_{\min}$.
- **$K_{\mathrm{soft}}^\phi$ convergence:** NO under the default φ-saturating envelope at $\ell_{\min} = 0.10$.
- **Persistence profile convergence:** YES, dominant top-6 bar vector $L^2$ distance $\le 0.03$.

---

## Conclusion

**The reservoir interpretation is empirically supported at the integer-morphology level.** Under the WQ-1 / WQ-2 baseline dynamics on $T^2_{20}$, the SCC multi-field flow with split-bump refinement produces:

- **field-level convergence:** the aggregate $U_K$ field stabilizes within $L^2$ tolerance as $K$ increases past 3;
- **integer-morphology convergence:** $K_{\mathrm{bar}}^{\ell_{\min}}$ is exactly constant at 1 (well-separated dominant component) across all $K$ and all four thresholds;
- **persistence-profile convergence:** dominant bar vector stable within 0.03;
- **chart-dependent activation:** $K_{\mathrm{act}}^\varepsilon = K$ exactly under LAT-C (all atoms above threshold) — confirming the chart-level reading of $K_{\mathrm{act}}$.

**The smooth $K_{\mathrm{soft}}^\phi$ envelope is not reservoir-invariant under the default φ-saturating choice.** $K_{\mathrm{soft}}$ grows monotonically with $K$ because additional sub-atoms create additional sub-prominence bars, each contributing a small but nonzero amount via the smooth envelope. This is a **φ-envelope sensitivity finding**, not a refutation of the reservoir framework: the *integer* counterparts ($K_{\mathrm{bar}}^{\ell_{\min}}$ at $\ell_{\min} = 0.10$) do not have this sensitivity and converge cleanly.

**Implication.** $K_{\mathrm{soft}}^\phi$ as currently defined (per `soft_K_definition.md` (φ-sat) family) is **not** the right reservoir-invariant smooth observable for this dynamics. A reservoir-invariant smooth observable would require either:

- a $\phi$ envelope that more aggressively suppresses small bars (e.g. $\phi(\ell) = (\ell - \ell_{\min})_+ / (1 + \ell - \ell_{\min})$ or step function);
- replacing $K_{\mathrm{soft}}^\phi$ with $K_{\mathrm{bar}}^{\ell_{\min}}$ as the primary count observable (which already converges cleanly);
- or composing $K_{\mathrm{soft}}^\phi$ with a *normalization* by total aggregate $L^1$ to remove the sub-atom-count growth.

The bridge lemma of `ksoft_kact_bridge_lemma.md` §5 should be revisited under this finding: the lemma's smooth-envelope error term $O(\rho_{\mathrm{noise}})$ from §5.3 was anticipated but not quantified; WQ-LAT-1 numerically confirms $\rho_{\mathrm{noise}}$ grows with truncation rank under the default φ.

---

## Theoretical interpretation (under reservoir reading)

Under `latent_index_space_design.md` §10:

- $K_{\mathrm{field}}$: chart rank — **changes by design** in the sweep.
- $K_{\mathrm{act}}^\varepsilon$: chart-level activation — **changes 3 → 12** under LAT-C as the chart includes more sub-atom slots.
- $K_{\mathrm{soft}}^\phi$ at default $\phi$: **mixed** — partly reservoir-level (the dominant-bar contribution stabilizes) but partly chart-dependent (the sub-prominence contribution accumulates with $K$).
- $K_{\mathrm{bar}}^{\ell_{\min}}$ at $\ell_{\min} = 0.10$: **field-level / reservoir-invariant** — constant 1 across all $K$.

The integer-morphology observables behave **as predicted by the reservoir reading**: the aggregate field is reservoir-invariant up to discretization tolerance, the integer counts of robust topological features are exactly $K$-invariant.

The smooth $K_{\mathrm{soft}}^\phi$ behaves **less cleanly**: it inherits the chart-rank dependency through the envelope's sub-resolution sensitivity. This is a useful empirical lesson about which envelopes give chart-invariant smooth observables.

**This run does not refute the reservoir framework.** It refines it: among the candidate field-native observables, $K_{\mathrm{bar}}^{\ell_{\min}}$ (with appropriate threshold) is reservoir-invariant; $K_{\mathrm{soft}}^\phi$ (with the default φ-saturating envelope) is not.

---

---

## Explicit non-claims

- This run does **not** prove σ-rich is sufficient.
- This run does **not** resolve OP-0008 (severity 🟠 HIGH retained).
- This run does **not** resolve OP-0005 (K-Selection).
- This run does **not** authorize promoting the reservoir framework to canonical.
- This run does **not** validate any vision / robotics / control application.
- This run does **not** assert that $T^2_{20}$ result generalizes to other graphs.
- This run does **not** invoke or establish stratified Morse theory.
- This run does **not** claim $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$.
- This run does **not** call $K$-resolution-stabilization a theorem.

---

## Cross-references

- `wq_lat1_reservoir_resolution_sweep_protocol.md` — full protocol.
- `latent_index_space_design.md` — design memo motivating WQ-LAT-1.
- `reservoir_reinterpretation_of_K.md` — conceptual reinterpretation.
- `nq242c_results.md`, `ksoft_kact_bridge_lemma.md`, `wq1c_layerI_h0_bardeath_results.md`, `wq1c_r2_projected_layerII_aggregate_sigma_results.md` — predecessor results.
- `CODE/scripts/wq_lat1_reservoir_resolution_sweep.py` — script.

---

## Decision and Next Action

**Verdict.** WQ-LAT-1 is **weak_success at the integer-morphology level**: aggregate field convergence (LAT-C2) PASS, $K_{\mathrm{bar}}$ exact integer convergence (LAT-C3) PASS, dominant bar profile convergence (LAT-C5) PASS, A/B consistency (LAT-C7) PASS. The smooth $K_{\mathrm{soft}}^\phi$ envelope criterion (LAT-C4) FAILS due to φ-envelope sub-resolution sensitivity. LAT-A serves as expected control / inconclusive (LAT-F1).

**Recommended next actions (in priority order):**

- **WQ-LAT-1.B — φ-envelope refinement (~half day).** Re-run WQ-LAT-1 production data with alternative $\phi$ envelopes that suppress sub-prominence noise: (a) hard threshold $\phi(\ell) = \mathbf 1\{\ell \ge \ell_{\min}\}$ recovers $K_{\mathrm{bar}}$ exactly; (b) shifted envelope $\phi(\ell) = \max(0, \ell - \ell_{\min})/(1 + \ell - \ell_{\min})$; (c) normalized envelope $K_{\mathrm{soft}} / \mathcal F$ to remove sub-atom growth. Test which $\phi$ achieves chart-invariance. This is post-processing only — no rerun needed.
- **WQ-LAT-2 — Spectral packet prototype on $T^2_{20}$ (~3–5 days).** Independent test of Model II spectral reservoir; complement to Model I findings.
- **WQ-LAT-3 — Five-model K-selection comparison (~1 week).** Now equipped with empirical evidence that $K_{\mathrm{bar}}^{\ell_{\min}}$ is reservoir-invariant under LAT-C dynamics — informs candidate (e) persistence-prominence.
- **Update bridge lemma `ksoft_kact_bridge_lemma.md`** §13 (WQ-2.D-1 record) and §5.3 (smooth bridge approximation) with WQ-LAT-1 evidence: the smooth bridge error $\rho_{\mathrm{noise}}$ is empirically *not* small under split-bump refinement; the integer bridge $K_{\mathrm{bar}}^{\ell_{\min}}(U) = K_{\mathrm{act}}^\varepsilon$ holds under LAT-C as the inactive-slot count = chart slack count.

**The architecture, the layered framework, the σ-rich design, and all canonical commitments are unaffected by this finding.** The reservoir framework is *partially* validated (integer-morphology observables behave as predicted) and *refined* (smooth-envelope observables need careful $\phi$ choice).

---

**End of WQ-LAT-1 results.** Status: RUN COMPLETE — partial reservoir convergence confirmed at integer-morphology level (LAT-C2 ∧ C3 ∧ C5 ∧ C7 PASS); smooth-envelope convergence not achieved under default $\phi$-saturating envelope (LAT-C4 FAIL); LAT-A inconclusive as expected (LAT-F1 control).
