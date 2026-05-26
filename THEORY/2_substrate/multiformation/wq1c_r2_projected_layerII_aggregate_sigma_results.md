> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]

# WQ-1.C-R2 — Projected Layer-II Aggregate σ Test (Results)

**File:** `THEORY/2_substrate/multiformation/wq1c_r2_projected_layerII_aggregate_sigma_results.md`
**Document type:** Working-grade R2 results / protocol record (non-canonical).
**Created:** 2026-05-02 (WQ-1.C-R2 retry path of WQ-1.C, motivated by the F-C1 / F-C7 outcome of WQ-1.C base).
**Status:** RUN COMPLETE — see §3 outcome.

**Companion artifacts:**
- `CODE/scripts/wq1c_r2_projected_layerII_aggregate_sigma.py` — executable script.
- `CODE/scripts/results/wq1c_r2_projected_layerII_aggregate_sigma.json` — JSON output.

**Predecessor artifacts (read for context):**
- `THEORY/2_substrate/Q4_kselection/ksoft_kact_bridge_lemma.md` — WQ-2 bridge lemma + WQ-2.D-1 production-run outcome ($K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1 for both A and B under Layer II).
- `THEORY/2_substrate/multiformation/wq1c_layerI_h0_bardeath_protocol.md` — WQ-1.C base protocol.
- `THEORY/2_substrate/multiformation/wq1c_layerI_h0_bardeath_results.md` — WQ-1.C F-C1 / F-C7 outcome (asymmetric event occurrence under pure Layer I single-field flow).
- `THEORY/2_substrate/multiformation/nq242c_results.md` — WQ-1 F2 outcome.
- `THEORY/2_substrate/multiformation/layered_ambient_architecture_agent_notes.md` — guardrails and forbidden non-claims.
- `CODE/scripts/results/ksoft_kact_diag.json` — WQ-2.D-1 scalar diagnostics (no per-snapshot field arrays).

---

## 1. Status and Scope

This is the **R2 retry path** of WQ-1.C, selected by the WQ-1.C results decision rule on the basis of WQ-1.C's F-C1 / F-C7 outcome (single-field SCC dynamics did not reproduce the symmetric A/B aggregate-topology transition observed in WQ-2 Layer II).

**Status grade per claim.**

| Claim | Status |
|---|---|
| WQ-2 Layer II trajectories show $K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1 for both A and B | working-definition safe (per `ksoft_kact_bridge_lemma.md` §13 WQ-2.D-1 record) |
| Aggregate $U(\mathbf u(t)) = \sum_j u^{(j)}(t)$ | working-definition safe (per `..._candidate.md` §6.3) |
| σ-standard via `compute_sigma_rich(U, ...)` (1-D input) | working-only Cat B sketch placeholder (per `sigma_rich.py` docstring) |
| σ-standard incompleteness across aggregate H_0 bar-death (under Layer II projection) | **conjectural / downstream — *target of this protocol*** |
| OP-0008 multi-formation σ-standard incompleteness across labelled $K_{\mathrm{act}}^\varepsilon$-jumps | **forbidden non-claim** for this protocol |
| σ-rich sufficiency | forbidden non-claim |

**Scope.** Re-runs the WQ-2 Layer II trajectories (deterministic, seed=42, identical parameters: $K_{\mathrm{field}}=4$, $M=90$, $\lambda_{\mathrm{rep}}=10$, $\lambda_{\mathrm{bar}}=100$, $\sigma_b=2.0$, A=equilateral, B=compressed, $T^2_{20}$). For each snapshot, computes the *aggregate* $U(t)$ and detects $H_0$ superlevel bar-death events on $U$ at the threshold sweep $\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}$. At event-bracketing snapshots, computes σ-standard on the aggregate $U(t^-)$ and post-stabilization $U(t^+_{\mathrm{stab}})$. Compares A vs B σ pre/post under tolerance sweep $\tau_\lambda \in \{10^{-4}, 10^{-3}, 10^{-2}\}$.

**Out of scope.**

- OP-0008 multi-formation σ-standard incompleteness across labelled $K_{\mathrm{act}}^\varepsilon$-jumps. R2 is a *projected aggregate analogue*, not OP-0008.
- σ-rich global sufficiency.
- K-Selection mechanism.
- Stratified Morse / Whitney verification.
- Vision / robotics / control application.
- Canonical promotion of any object.

---

## 2. Data Availability and Approach

### 2.1 Data availability check

The WQ-2 output `CODE/scripts/results/ksoft_kact_diag.json` contains scalar diagnostics per snapshot (`K_act`, `K_bar`, `K_soft`, `dominant_bar_lengths` (top 8), `pairwise_overlaps`, `support_distance`, `regime_label`, `m_j_trajectory`) but **does not contain the per-snapshot field arrays** $U(t)$ or $u^{(j)}(t)$.

### 2.2 R2 approach

R2 reruns the WQ-2 Layer II trajectories (deterministic, seed-stable) inside its own script. At each snapshot, R2 computes:

- aggregate $U(t) = \sum_j u^{(j)}(t)$;
- $H_0$ superlevel bar-death events on $U$ at all four $\ell_{\min}$;
- σ-standard via `compute_sigma_rich(U(t), ...)` *only at event-bracketing snapshots* (pre and post-stabilization), to avoid the FD-Hessian cost on every snapshot.

This is **not** a duplicate of WQ-2 — WQ-2 computed σ on the multi-field state $\mathbf u$ (effectively averaging via `u.mean(axis=0)`); R2 computes σ on the aggregate $U = \sum_j u^{(j)}$ (the single-field projection). For consistent multi-field input where slot 4 is empty, these are mathematically equivalent up to a factor of $K_{\mathrm{field}}$ in the FD-Hessian eigenvalue scale, but the R2 framing is conceptually clean: σ is read on the Layer I projection at Layer II event times.

---

## 3. Outcome (RUN COMPLETE — failed R2-F3)

Production run executed (2026-05-02): `max_iter=5000`, `seed=42`, identical parameters to WQ-2.D-1, 5.2 s wall-clock. Output JSON: `CODE/scripts/results/wq1c_r2_projected_layerII_aggregate_sigma.json`.

### 3.1 R2-C1–R2-C6 table (post-run)

| Criterion | Status | Evidence |
|---|---|---|
| R2-C1 — events exist for both A and B | **PASS** | both A and B undergo bar-death events at all four $\ell_{\min}$ |
| R2-C2 — same pre-event σ-standard | **FAIL** | max λ diff at ℓ=0.05 is 1.385; at ℓ=0.10 is 2.823; at ℓ=0.15 is 1.943; at ℓ=0.20 is 0.802 — all far beyond any tested $\tau_\lambda \in \{10^{-4}, 10^{-3}, 10^{-2}\}$ |
| R2-C3 — different post-event σ-standard | **PASS** | max λ diff at ℓ=0.10 is 2.097, etc.; well beyond $10\tau_\lambda$ at all thresholds |
| R2-C4 — same projected protocol | PASS | single shared `RunConfig`, seed=42, identical to WQ-2.D-1 |
| R2-C5 — threshold robustness | NOT EVALUATED | (R2-C2 ∧ R2-C3 must both pass to be evaluated) |
| R2-C6 — tolerance robustness | NOT EVALUATED | same |

**Status overall: `failed`. Failure mode: `R2-F3` (pre-event σ mismatch).**

### 3.2 Per-trajectory event timing (production run)

| Threshold $\ell_{\min}$ | A: τ_pre → τ_post_stab | A: K_bar | B: τ_pre → τ_post_stab | B: K_bar |
|---|---|---|---|---|
| 0.05 | 775 → 900 | 3 → 2 | 675 → 800 | 3 → 2 |
| 0.10 | 600 → 725 | 3 → 2 | 450 → 575 | 3 → 2 |
| 0.15 | 425 → 550 | 3 → 1 | 350 → 475 | 3 → 1 |
| 0.20 | 300 → 425 | 3 → 2 | 275 → 400 | 3 → 1 |

Two notable structural observations:

- **B's bar-death events occur ~100–175 iterations earlier than A's** at every threshold. The compressed B is closer to the unstable transition. This is a substantive feature, not noise.
- **At higher thresholds ($\ell \ge 0.15$) the K-drop is 3 → 1**; at lower thresholds ($\ell \le 0.10$) it's 3 → 2. This is consistent with `ksoft_kact_bridge_lemma.md` §13 WQ-2.D-1: the longest bar settles around prominence ≈ 1.0, the second/third bars below ≈ 0.04. At ℓ=0.10, only 2 bars survive briefly before collapsing further; at ℓ=0.15, both die together.

### 3.3 Critical observation: qualitative cluster structure agrees; eigenvalue magnitudes do not

At every event bracket and every threshold, **both A and B have FD-Hessian σ-standard tuples with 6 multiplicity-1 clusters** — the qualitative *cluster-size pattern* `(1, 1, 1, 1, 1, 1)` is identical between A and B at every snapshot examined.

What differs is the **eigenvalue magnitudes**. For example, at ℓ=0.10 pre-event:

- A_pre eigenvalues (top 6): −6.684, −6.445, −6.070, −4.317, −4.305, −4.158
- B_pre eigenvalues (top 6): −9.507, −9.053, −8.644, −5.929, −5.898, −5.601

These differ by ≈ O(2.8) — a substantial systematic shift, not noise.

**Implication.** The current `_sigma_standard` placeholder implementation in `scc/sigma_rich.py` returns the cluster tuple as `(cluster_size, "mult-{n}", eigenvalue)`. The script's tolerance comparison checks all three components. If a coarser comparison were used — comparing only cluster sizes and multiplicity tags, ignoring eigenvalue magnitudes — **R2-C2 would PASS at all four thresholds** (both A and B are `(1, 1, 1, 1, 1, 1)`).

This matches the **canonical Commitment 14** σ-tuple convention `(n_k, [\rho_k], \lambda_k)` where `[\rho_k]` is the irrep label. In the canonical version, two states would be considered σ-equivalent if their cluster-size + irrep structure agreed, regardless of eigenvalue magnitudes (subject to a separate scale-invariance discussion). Under that coarser convention the WQ-1.C-R2 test changes outcome from R2-F3 to a clean R2-C1 ∧ R2-C2 ∧ R2-C3 = TRUE.

The working `_sigma_standard` placeholder defaults to including eigenvalues in the comparison. The canonical Commitment 14 form does not specify whether eigenvalue magnitudes are part of σ-equivalence; the irrep label `[\rho_k]` is the load-bearing classifier.

**This is a σ-implementation-level finding, recorded as R2-F3-σ-implementation-dependent.** The protocol's R2-F3 failure is conditional on the eigenvalue-magnitude tolerance comparison; under a coarser cluster-structure-only comparison the R2 test would pass cleanly.

---

## 4. Failure-Mode Catalog

| ID | Description |
|---|---|
| R2-F1 | snapshots unavailable (would require rerun — handled by R2 script via direct rerun) |
| R2-F2 | event missing for one trajectory (contradicts WQ-2.D-1 summary or threshold mismatch) |
| R2-F3 | pre-event σ mismatch (not a valid incompleteness test) |
| R2-F4 | post-event σ remains equal (this projected aggregate test does not expose σ-standard incompleteness) |
| R2-F5 | σ extraction limitation (current implementation too aggregate-averaged or insensitive at this scale) |
| R2-F6 | threshold artifact (result depends on a single unstable $\ell_{\min}$) |
| R2-F7 | tolerance artifact (result depends on one σ tolerance only) |

---

## 5. Interpretation Rules

### 5.1 If status = success

> The projected Layer II aggregate σ-standard test on $T^2_{20}$ exposes a Layer I topological-transition analogue of σ-standard incompleteness. The (working FD-Hessian) σ-standard distinguishes A and B post-event but not pre-event, robustly across multiple $\ell_{\min}$ and multiple $\tau_\lambda$.

The conclusion is restricted to:

- the projected FD-Hessian σ implementation;
- the specific Layer II configuration ($T^2_{20}$, $K_{\mathrm{field}}=4$, $M=90$, $\lambda_{\mathrm{rep}}=10$, $\lambda_{\mathrm{bar}}=100$, equilateral / compressed initial geometries);
- the aggregate $H_0$ superlevel bar-death event observed in WQ-2.D-1.

It does **not** imply OP-0008 resolution. The connection requires the WQ-2 bridge lemma (currently sketch-only at the smooth level) plus an additional argument linking projected aggregate-topology transitions to labelled $K_{\mathrm{act}}^\varepsilon$-jumps. That argument is not part of WQ-1.C-R2.

### 5.2 If status = weak_success

> Partial evidence: C5 (threshold robustness) or C6 (tolerance robustness) failed. Result holds only under restricted parameter window. Document and decide whether to upgrade via further sweep or move to WQ-1.A / WQ-1.B retry.

### 5.3 If status = failed

Classify per the failure mode (R2-F2 through R2-F7). Do not weaken any forbidden non-claim. Specifically:

- R2-F4 (post-event σ equal) means the *projected* aggregate test does not falsify σ-standard incompleteness; this is *neutral* to the multi-formation OP-0008 question, which involves labelled extinctions and is a different test.
- R2-F5 (σ extraction limitation) is a known caveat of the current `_sigma_standard` placeholder; the result restricts to that implementation.
- R2-F3 (pre-event σ mismatch) — *as encountered in this run* — has a σ-implementation-conditional reading: under the eigenvalue-magnitude comparison the test fails; under a cluster-structure-only comparison (matching canonical Commitment 14 irrep convention) the test would pass. This is a substantive structural observation about the σ-standard implementation, not a defect of the WQ-2 dynamics or the bridge-lemma framing.

### 5.4 Dual reading of the R2-F3 outcome (this run)

**Reading I — eigenvalue-quantitative σ (script's default).** R2-F3 fails. The aggregate FD-Hessian eigenvalue spectra of A and B are systematically distinct from $t = 0$ onward (the geometric difference of equilateral vs compressed imprints on the eigenvalue magnitudes). σ-standard sees A and B as different at every snapshot, so the protocol's premise (matching pre-event σ ⇒ test post-event σ inheritance) is unfulfilled.

**Reading II — cluster-structure σ (canonical-aligned).** All snapshots examined have cluster pattern $(1, 1, 1, 1, 1, 1)$ — six multiplicity-1 clusters, identical between A and B. Under a comparison restricted to cluster sizes and multiplicity tags (ignoring eigenvalue magnitudes), R2-C2 PASS, R2-C3 PASS (the irrep / multiplicity structure does *not* change at the post-event snapshot for either A or B in this construction; the *shape* of the cluster pattern is preserved through the bar-death event).

If Reading II is the intended sense of σ-standard agreement, then **R2-C3 also fails under that reading** — both A and B keep the same cluster pattern $(1, 1, 1, 1, 1, 1)$ before and after the bar-death event. The bar-death is a *bar-count* transition (visible to $K_{\mathrm{bar}}$) but not a *Hessian-multiplicity* transition (invisible to a cluster-structure σ).

**Combined reading.** The aggregate $H_0$ bar-death event observed in WQ-2 is a *count* transition that is **not registered by either form of σ-standard at the cluster-structure level, and only registered as O(1) eigenvalue drift at the magnitude level**. The σ-standard test as designed cannot distinguish the bar-death event from ordinary smooth-segment evolution at the structural level.

This is informative about the σ-standard's relationship to aggregate $H_0$ transitions: σ-standard (in either reading) is essentially **insensitive to the type of topological transition that the bar-death event represents**. To detect aggregate-topology transitions through σ, the σ would need to incorporate $H_0$-barcode data directly — which is exactly what σ-rich centroid + Wigner-data extension proposes (per `sigma_rich_augmentation.md`), though this protocol does not test σ-rich.

### 5.5 What is *never* concluded

- OP-0008 resolution.
- σ-rich sufficiency.
- $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ identification.
- Stratified Morse application.
- Vision / robotics / control validation.
- $H_0$ aggregate bar-death is a labelled $K_{\mathrm{act}}^\varepsilon$-jump (it is not).

---

## 6. Execution Commands

```bash
# Smoke test (~2 s)
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 /Users/ojaehong/Perception/Perception_theory/CODE/scripts/wq1c_r2_projected_layerII_aggregate_sigma.py \
    --output /tmp/wq1c_r2_smoke.json --max_iter 200 --snapshot_every 25

# Production run (~10–30 s)
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 /Users/ojaehong/Perception/Perception_theory/CODE/scripts/wq1c_r2_projected_layerII_aggregate_sigma.py \
    --output /Users/ojaehong/Perception/Perception_theory/CODE/scripts/results/wq1c_r2_projected_layerII_aggregate_sigma.json \
    --max_iter 5000 --seed 42

# Inspect
python3 -c "
import json
r = json.load(open('CODE/scripts/results/wq1c_r2_projected_layerII_aggregate_sigma.json'))
print('status:', r['status'])
print('failure_mode:', r['failure_mode'])
for k, v in r['criteria_summary'].items():
    print(f'  {k}: {v}')
"
```

---

## 7. Explicit non-claims (apply regardless of outcome)

- This run does **not** prove σ-rich is sufficient.
- This run does **not** resolve OP-0008 (severity 🟠 HIGH retained).
- This run does **not** resolve OP-0005 (K-Selection).
- This run does **not** authorize promoting any object to canonical.
- This run does **not** validate any vision / robotics / control application.
- This run does **not** assert that $T^2_{20}$ result generalizes to other graphs.
- This run does **not** invoke or establish stratified Morse theory.
- This run does **not** claim $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$.
- This run does **not** call an aggregate H_0 bar-death a labelled $K_{\mathrm{act}}^\varepsilon$-jump.
- A positive R2 result is a **projected Layer II aggregate-topology analogue** of σ-standard incompleteness, not a proof of multi-formation OP-0008.

---

## 8. Cross-references

- `wq1c_layerI_h0_bardeath_protocol.md` — WQ-1.C base protocol (sets the σ-standard implementation, threshold sweep, tolerance, event-bracketing convention reused here).
- `wq1c_layerI_h0_bardeath_results.md` — WQ-1.C base outcome (F-C1 / F-C7) that motivated R2.
- `ksoft_kact_bridge_lemma.md` §13 — WQ-2.D-1 production-run outcome that this protocol revisits at the σ level.
- `nq242c_counterexample_protocol.md` — WQ-1 protocol (Layer II baseline configuration).
- `nq242c_counterexample.py` — script reused by R2 for trajectory rerun.
- `ksoft_kact_diagnostics.py` — script reused by R2 for `h0_barcode` / `bar_lengths`.
- `scc/sigma_rich.py::compute_sigma_rich` — σ-standard extraction.

---

**End of WQ-1.C-R2 results.** Status: RUN COMPLETE — `failed R2-F3` (eigenvalue-magnitude reading) / equivalent to `failed R2-F4` (cluster-structure reading). Empirical finding: aggregate $H_0$ bar-death event is essentially invisible to σ-standard at the cluster-structure level and registers only as O(1) eigenvalue magnitude drift at the quantitative level. Under either σ-equivalence convention, the WQ-1.C-R2 test cannot evaluate σ-standard incompleteness as designed: under the eigenvalue convention pre-event σ already differs (R2-F3); under the cluster-structure convention post-event σ is identical to pre-event σ for both A and B (R2-F4). σ-standard is structurally insensitive to aggregate $H_0$ bar-death transitions.

**Recommended next action:** WQ-1.A (Layer II Option D-1 joint projection — produces real labelled $K_{\mathrm{act}}$-jumps under different dynamics) or WQ-1.B (forced extinction intervention — tests σ-standard *response* rather than *predictive sufficiency*). The WQ-1.C family is exhausted: both pure Layer I (F-C1) and projected Layer II (R2-F3 / R2-F4) showed that σ-standard cannot meaningfully test inheritance across the aggregate-topology transitions accessible from the current setup. WQ-2 bridge lemma is unaffected; the bridge between $K_{\mathrm{soft}}$ / $K_{\mathrm{act}}$ is still well-defined and the F-B6 manifestation is still confirmed.
