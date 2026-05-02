# WQ-1.C — Layer I H_0 Bar-Death Counterexample Results

**File:** `THEORY/working/MF/wq1c_layerI_h0_bardeath_results.md`
**Companion files:**
- `THEORY/working/MF/wq1c_layerI_h0_bardeath_protocol.md` — full protocol specification.
- `CODE/scripts/wq1c_layerI_h0_bardeath.py` — executable script.
- `CODE/scripts/results/wq1c_layerI_h0_bardeath_results.json` — JSON output (after run).

---

## Status: RUN COMPLETE — failed F-C1 (asymmetric event occurrence)

Production run executed (2026-05-02): `max_iter=5000`, `seed=42`, `--skip_v2`, V0 (saturated_gaussian) + V1 (capped_smooth), 4 trajectories total, 8.5 s wall-clock.

**Top-line result.** `failure_mode = F-C1`, but the underlying empirical observation is more informative than "no event at all". The script reports F-C1 because *cross-trajectory event matching* fails: bar-death events occur consistently in **B_I** (compressed configuration), at every threshold and in both V0 and V1 variants, but **not** in **A_I** (equilateral configuration). With no A_I event to pair against B_I, no σ-standard pre/post comparison is possible.

This is **not** a script bug, **not** a parameter-tuning issue, and **not** an artifact of saturation (V1 capped_smooth reproduces the asymmetry). It is a real finding about Layer I single-field SCC dynamics on $T^2_{20}$: the equilateral configuration is *stable* under SCC single-field flow, while the compressed configuration is *not*.

---

## Per-trajectory empirical record

Snapshot interval = 25 iter, 201 snapshots per trajectory, default $M = 90$, threshold sweep $\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}$.

### V0 — saturated_gaussian

| Trajectory | K_bar(0.05) trajectory | K_bar(0.10) trajectory | K_soft drift | F drift | First bar-death event |
|---|---|---|---|---|---|
| A_I (equilateral) | constant 3 throughout | constant 3 throughout | 2.709 → 2.727 (≈ 0) | 0 → 0 | **none** |
| B_I (compressed) | 3 → 1 at τ=3500 (ℓ=0.05) | 3 → 1 at τ=2775 (ℓ=0.10) | 2.637 → 1.859 | 0 → 14 | yes, at all four ℓ_min |

B_I bar-death event time as a function of threshold:

| ℓ_min | event τ_post | drop |
|---|---|---|
| 0.05 | 3500 | 3 → 1 |
| 0.10 | 2775 | 3 → 1 |
| 0.15 | 2375 | 3 → 1 |
| 0.20 | 2075 | 3 → 1 |

### V1 — capped_smooth ($u_{\max} = 0.7$)

| Trajectory | K_bar(0.05) | K_bar(0.10) | K_soft drift | F drift | First bar-death event |
|---|---|---|---|---|---|
| A_I (equilateral) | constant 3 throughout | constant 3 throughout | 2.581 → 2.727 (≈ 0) | 0 → 0 | **none** |
| B_I (compressed) | 3 → 1 at τ=3475 (ℓ=0.05) | 3 → 2 → 1 at τ=2575, 2625 (ℓ=0.10) | 2.392 → 1.974 | 0 → 16 | yes, at all four ℓ_min; multi-step transition at ℓ=0.10 and ℓ=0.15 |

### Critical observation

**Bar-death events occur only in B_I (compressed). They do not occur in A_I (equilateral) within `max_iter=5000`.** This is true for both V0 (saturated_gaussian) and V1 (capped_smooth) — the asymmetry is *not* an artifact of initial-state saturation.

The dominant bar at the end of A_I is $\{1.0, 1.0, 1.0\}$ in both V0 and V1 — three saturated robust components. The dominant bars in B_I at the end are $\{1.0, 0.04, 0.04\}$ — one dominant component with two near-extinct sub-bars.

### Why the asymmetry

The SCC single-field gradient flow on $T^2_{20}$ with $M = 90$ and the canonical 4-term energy is *stable* on a 3-bump configuration when the bumps are at distance ≈ 10 (A_I, equilateral). It is *unstable* when bumps are at distance ≈ 7.81 (B_I, compressed): two of the three bumps are close enough that one cannot survive the closure-distinction-boundary energy minimum, leading to a bar-death event.

This is a structural feature of the Layer I dynamics, not a bug. It means the protocol's symmetric A/B test design is flawed: the σ-standard pre/post comparison requires *both* trajectories to undergo bar-death events, so the comparison cannot be evaluated when only one does.

---

## C1–C6 Results Table (post-run)

| Criterion | Status | Evidence | Notes |
|---|---|---|---|
| C1 — bar-death event exists in both | **FAIL** | A_I shows no event at any ℓ_min; B_I shows events at all ℓ_min | asymmetric event occurrence |
| C2 — same pre-event σ-standard | NOT EVALUATED | C1 precondition failed | — |
| C3 — different post-event σ-standard | NOT EVALUATED | C1 precondition failed | — |
| C4 — same protocol | PASS | single shared `WQ1CConfig` | by construction |
| C5 — threshold robustness | NOT EVALUATED | C1 precondition failed | NB: B_I alone is robust across all four ℓ_min |
| C6 — saturation robustness | **PARTIAL PASS for B_I asymmetry** | both V0 and V1 show the same A_I no-event / B_I event pattern | not the full C6 criterion (which requires C2 ∧ C3 to hold first) |

---

## Conclusion

**Status: `failed F-C1`** — protocol precondition (cross-trajectory event matching) not satisfied.

**Empirical finding (informative).** Layer I single-field SCC gradient flow on $T^2_{20}$ with $M=90$ and the constructed equilateral / compressed initial geometries:

- preserves a 3-bump topology indefinitely for the equilateral A_I (no bar-death within 5000 iter under either V0 or V1 initialization);
- drives a clean 3 → 1 bar-death transition for the compressed B_I, robustly across ℓ_min ∈ {0.05, 0.10, 0.15, 0.20} and across V0 / V1 initialization;
- the bar-death event time is monotone in ℓ_min (lower threshold ⇒ later event time, as expected: a bar must shrink further to drop below a lower threshold).

**Implication for σ-standard incompleteness.** The protocol's symmetric A/B test design *cannot* test σ-standard incompleteness across H_0 bar-death events when only one trajectory exhibits the event. The σ-standard test is *undefined* in this run.

**Implication for WQ-2 bridge lemma.** The WQ-2.D-1 finding (multi-field Layer II F2 trajectory shows aggregate K_bar 3 → 1) is **not** automatically reproduced by single-field Layer I dynamics on the same initial geometry. The multi-field flow with simplex barrier and inter-formation repulsion is what drives both A and B to the K_bar 3 → 1 transition observed in WQ-2; under single-field SCC dynamics on Layer I, the same geometric initial state evolves differently between A and B. This is **F-C7** (dynamics mismatch) per protocol §11.

The combined classification: **F-C1 (asymmetric event occurrence) compounded by F-C7 (single-field Layer I dynamics differs from multi-field Layer II aggregate dynamics)**.

---

## Recommended redesign

Two distinct redesign paths:

### Redesign R-1 — both trajectories in the unstable regime

Make both A and B compressed enough to undergo bar-deaths, but with different geometric arrangements so the *post-event* states differ.

Suggested initial configurations:

- **A_I' (slightly compressed isosceles):** centers $\{(5,5), (15,5), (10,11)\}$ — distances $\{10, 7.81, 7.81\}$, current B_I.
- **B_I' (more compressed isosceles):** centers $\{(5,5), (15,5), (10,8)\}$ — distances $\{10, 5.83, 5.83\}$.

Both should undergo bar-deaths; the σ-standard pre/post comparison becomes meaningful.

### Redesign R-2 — match Layer II aggregate dynamics

Use the multi-field aggregate $U(\mathbf u(t))$ from a Layer II flow as the single-field "initial condition" sequence, then test σ-standard at points along that sequence directly. This bypasses the Layer I single-field flow's intrinsic stability difference and uses the Layer II flow's bar-death events directly.

The technical step: take WQ-2's `ksoft_kact_diagnostics.py` output, extract $U(\mathbf u(t))$ at pre/post bar-death snapshots, compute σ-standard on $U$ directly, compare A vs B. This is essentially a post-processing of WQ-2 results, not a new dynamics run.

R-2 is faster to execute and more directly comparable to WQ-2. R-1 is theoretically cleaner.

### Recommendation

**Run R-2 first** (post-process WQ-2 snapshots; ~half day). If it produces interpretable σ-standard differences, the Layer I framing is partially salvageable. If not, run R-1 (1 day).

Independent of WQ-1.C outcome:
- WQ-2.A (bridge lemma proof sketch upgrade) remains valuable.
- WQ-2.C (R23 dataset diagnostic) remains valuable.
- WQ-1.A (Option D-1 joint projection) and WQ-1.B (forced extinction intervention) remain alternative Layer II retries.

---

## Explicit non-claims (apply regardless of outcome)

- This run does **not** prove σ-rich is sufficient.
- This run does **not** resolve OP-0008 (severity 🟠 HIGH retained).
- This run does **not** resolve OP-0005 (K-Selection).
- This run does **not** authorize promoting any object to canonical.
- This run does **not** validate any vision / robotics / control application.
- This run does **not** assert that $T^2_{20}$ result generalizes to other graphs.
- This run does **not** invoke or establish stratified Morse theory.
- This run does **not** claim $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$.
- This run does **not** call an H_0 bar-death a labelled K-jump.
- A positive result would be a **Layer I analogue** of σ-standard incompleteness, not a proof of multi-formation OP-0008.

---

## Decision and Next Action

The F-C1 / F-C7 outcome is consistent across V0 and V1 variants and across the full ℓ_min sweep. **Do not retry WQ-1.C with the current symmetric A/B initial geometry** — the cause is identified (single-field SCC dynamics is stable on equilateral 3-bump and unstable on compressed 3-bump; the protocol cannot test σ-standard incompleteness when only one trajectory undergoes the event).

**Recommended next action (one of):**

- **WQ-1.C-R2 — post-process WQ-2 snapshots.** Use existing `ksoft_kact_diagnostics.py` outputs; extract aggregate field $U(\mathbf u(t))$ at WQ-2 bar-death snapshots; compute σ-standard on $U$ for both A and B; compare. ~half day. Risk: σ-standard implementation operates on FD-Hessian which may not see the geometric distinction at the aggregate-field level.
- **WQ-1.C-R1 — both-compressed redesign.** Run with $c_3^A = (10, 11)$ and $c_3^B = (10, 8)$ both in the unstable regime. ~1 day. Most theoretically clean.
- **WQ-1.A — Layer II Option D-1 joint projection.** Independent of WQ-1.C; produces real K_act jumps. ~1 day.
- **WQ-1.B — Layer II forced extinction intervention.** Tests σ-standard *response* to prescribed extinction. ~half day.

The architecture and the bridge lemma are unaffected by the F-C1 / F-C7 result. The non-claims of `..._candidate.md` §12 and `ksoft_kact_bridge_lemma.md` §10 are unchanged.

---

## Cross-references

- `wq1c_layerI_h0_bardeath_protocol.md` — full protocol.
- `ksoft_kact_bridge_lemma.md` — WQ-2 bridge lemma + decision rule that selected WQ-1.C.
- `nq242c_results.md` — WQ-1 F2 outcome.
- `nq242c_counterexample_protocol.md` — WQ-1 protocol (Layer II).
- `layered_ambient_architecture_candidate.md` — Layer I definition, status table.
- `CODE/scripts/wq1c_layerI_h0_bardeath.py` — executable script.

---

**End of WQ-1.C results.** Status: RUN COMPLETE — `failed F-C1` compounded by F-C7. Empirical finding: single-field SCC Layer I dynamics on $T^2_{20}$ produces an asymmetric event pattern (B_I undergoes K_bar 3 → 1 robustly across ℓ_min ∈ {0.05, 0.10, 0.15, 0.20} and across V0 / V1 variants; A_I undergoes no event). The σ-standard incompleteness test is undefined under this asymmetric pattern. Recommended next action: WQ-1.C-R2 (post-process WQ-2 snapshots) or WQ-1.C-R1 (both-compressed redesign).
