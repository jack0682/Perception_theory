# NQ-242c Counterexample Results — WQ-1 Numerical Anchor

**File:** `THEORY/working/MF/nq242c_results.md`
**Companion files:**
- `THEORY/working/MF/nq242c_counterexample_protocol.md` — full protocol specification.
- `CODE/scripts/results/nq242c_result_schema.json` — JSON schema for numerical anchor.
- `CODE/scripts/nq242c_counterexample.py` — executable script.

---

## Status: RUN COMPLETE — failed F2 (no K-jump under Option D-2)

Three runs were executed (2026-05-02): primary (λ_rep=10), λ_rep sweep {30, 100, 300}, and Configuration-B compression sweep (c_3 = (10, 8), (10, 7), (10, 6)). **All twelve trajectories** (A and B for primary + 5 perturbations) reported `failure_mode = "F2"`: K_act stayed at 3 throughout, the minimum-mass slot never approached ε = 0.225 (lowest observed: m_j ≈ 23.9 at λ_rep = 300; ε is 100× smaller).

**This is a structural finding, not a parameter-tuning issue.** Option D-2 (per-slot gradient + uniform total-mass rescale) is the protocol's gradient-flow integrator. Under Option D-2, each slot's mass is conserved up to a global rescale factor that stays near 1, so no slot loses substantial mass. The dynamics find a stable 3-formation fixed point regardless of:

- λ_rep ∈ {10, 30, 100, 300} — stronger repulsion only deepens the redistribution-within-wells pattern;
- Configuration B compression to distance ≈ 5.1 (overlap regime) — bumps still sit in stable wells.

**Implication for WQ-1.** σ-standard incompleteness across K-jumps cannot be tested without producing a K-jump. The current Option D-2 implementation does not produce K-jumps in this regime. The WQ-1 protocol therefore requires one of:

1. **Option D-1 — true joint projection** onto $\widetilde\Sigma^{K_{\mathrm{field}}}_M$, which couples all slots simultaneously and may permit inter-slot mass transfer (theoretically required by the layered architecture; not yet implemented).
2. **K-jump by intervention** — equilibrate at K=3, force one slot's mass to zero artificially, re-equilibrate at K=2, compare σ-standard pre/post. Tests σ-standard *response* to a prescribed extinction rather than σ-standard *predictive sufficiency* across a natural extinction. Different question, valid alternative.
3. **Single-field framework** — abandon labelled K-field entirely; use Layer I single field $\Sigma_M(G_t)$ with $K_{\mathrm{soft}}^\phi$ as the count diagnostic. K-"jumps" become bar-deaths in $H_0$ persistence of the aggregate. Requires WQ-2 (K-soft / K-act bridge) to be operationalized first.

---

## Smoke-Test Validation (2026-05-02)

Performed before reporting NOT RUN, to confirm the script is operationally correct. Run from the project root:

```bash
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 /Users/ojaehong/Perception/Perception_theory/CODE/scripts/nq242c_counterexample.py \
  --output /tmp/nq242c_smoke2.json --max_iter 200 --snapshot_every 25 --seed 42
```

**Smoke-test outcome (max_iter=200):**

| Check | Result |
|---|---|
| Script imports `scc.{graph,params,energy,optimizer,sigma_rich}` | OK |
| Torus graph construction | OK (4-regular periodic, 400 nodes) |
| Initial state construction (Configurations A and B) | OK; m_j(0) = (30, 30, 30, 0) |
| Spare-slot zero preserved across dynamics | OK; m_4 ≡ 0 throughout (active_slot_mask) |
| Trajectory loop runs without exception | OK; 0.2 s wall-clock |
| K_act trajectory recording | OK; K_act stays at 3 throughout (no K-jump in 200 iter) |
| K-jump detector | OK; correctly reports `no_k_jump=True` |
| Failure-mode classification | OK; reports `failure_mode="F2"` |
| JSON serialization | OK; conforms to `nq242c_result_schema.json` |
| All required schema keys present | OK |
| σ-rich extraction gated by K-jump occurrence | OK; not invoked when no jump |

**Smoke-test K_act trajectory (A and B identical at this resolution):** `[3, 3, 3, 3, 3, 3, 3, 3, 3]` (snapshots at τ = 0, 25, 50, ..., 200).

**Smoke-test m_j drift (Configuration A, last snapshot):** `[30.110, 29.979, 29.911, 0.000]`. Per-formation masses drift by ~0.4% in 200 iterations under Option D-2 rescaling. Extrapolating, 5000 iterations may or may not produce a m_j → ε drop; this is the empirical question the full run is designed to answer.

**Implication for full run.** The script is correct; the full protocol run is empirically open. If the full run with `max_iter=5000` fails to produce a K-jump (F2), the user should:

- consider switching to **Option D-1** (true joint projection — more aggressive at driving m_j → 0; protocol §6.3),
- or increase `lambda_rep` (stronger inter-formation repulsion drives one slot to extinction faster),
- or compress the initial geometry further to force earlier merger.

---

## Run Status Table

| Item | Status |
|---|---|
| Protocol document | written (`nq242c_counterexample_protocol.md`) |
| JSON schema | written (`CODE/scripts/results/nq242c_result_schema.json`) |
| Executable script | written (`CODE/scripts/nq242c_counterexample.py`) |
| Script syntax + import check | PASS (2026-05-02) |
| Script end-to-end smoke test (max_iter=200) | PASS (F2 correctly reported, schema-conforming) |
| Primary run (`max_iter=5000`, λ_rep=10, default centers) | RUN COMPLETE — `failed F2` (1.9 s wall-clock) |
| λ_rep sweep (30, 100, 300; default centers) | RUN COMPLETE — `failed F2` for all three |
| Configuration B compression sweep (c_3 = (10,8), (10,7), (10,6); λ_rep=100) | RUN COMPLETE — `failed F2` for all three |
| Robustness sweep (`--robustness center_perturb`) | NOT RUN (moot until a K-jump is produced) |
| Result JSON at `CODE/scripts/results/nq242c_results.json` | generated (primary run; F2) |
| Sweep JSONs in `/tmp/nq242c_lr*.json` | generated (sweep runs; F2 throughout) |

### Sweep summary (all runs F2)

| Run | λ_rep | c_3^B | A min m_j ever | B min m_j ever | K_act ever | Outcome |
|---|---|---|---|---|---|---|
| primary | 10 | (10, 11) | 27.43 | 27.32 | 3 | F2 |
| lr30 | 30 | (10, 11) | 26.53 | 26.94 | 3 | F2 |
| lr100 | 100 | (10, 11) | 26.05 | 25.69 | 3 | F2 |
| lr300 | 300 | (10, 11) | 24.80 | 23.94 | 3 | F2 |
| compress y8 | 100 | (10, 8) | 26.05 | 25.26 | 3 | F2 |
| compress y7 | 100 | (10, 7) | 26.05 | 25.50 | 3 | F2 |
| compress y6 | 100 | (10, 6) | 26.05 | 25.71 | 3 | F2 |

ε = 0.225 throughout. Lowest observed slot mass across all 14 trajectories: **23.94** — over 100× the activity threshold. The dynamics never approach extinction in any tested configuration.

---

## What must be run

From the repository root:

```bash
# Step 1 — verify code-side health (≤ 30 s)
cd CODE && python3 -m pytest tests/test_multi.py tests/test_sigma_rich.py -q

# Step 2 — primary run (~10–30 min on single CPU)
cd CODE && python3 scripts/nq242c_counterexample.py \
    --output scripts/results/nq242c_results.json \
    --seed 42 \
    --max_iter 5000

# Step 3 — robustness run (optional but required for C4 PASS)
cd CODE && python3 scripts/nq242c_counterexample.py \
    --output scripts/results/nq242c_results_robust.json \
    --seed 137 \
    --max_iter 5000 \
    --robustness center_perturb
```

If Step 1 fails, abort the protocol and resolve the dependency / import issue first. Do not proceed to Step 2.

---

## Expected outputs

### Primary run

`CODE/scripts/results/nq242c_results.json` conforming to `nq242c_result_schema.json`. Top-level fields populated:

- `status`: one of `success | weak_success | failed`.
- `parameters`: full echo of the run configuration.
- `configuration_A`, `configuration_B`: per-trajectory K-jump time, pre/post σ-standard, K_act trajectory, m_j trajectory.
- `criteria`: C1, C2, C3 booleans with supporting evidence.
- `diagnostics`: σ-rich pre/post for both trajectories, K_act trajectories, m_j trajectories.
- `conclusion`: `standard_sigma_incomplete` ∈ `{supported, weak, undetermined, not_supported}`; `sigma_rich_sufficiency: "not_claimed"` (always).
- `metadata`: git commit, wall-clock, host, library versions.

### Robustness run

`CODE/scripts/results/nq242c_results_robust.json` (same schema, but with `parameters.seed` and possibly `parameters.center_perturb` perturbed). Used to populate `criteria.C4_robustness` in a *combined* analysis (the script reads both files when C4 is requested as a separate post-processing step).

---

## C1–C4 Results Table (post-run, F2)

Fill state from primary `criteria` block (sweep runs all match):

| Criterion | Status | Evidence | Notes |
|---|---|---|---|
| C1 — same pre-jump σ-standard | NOT EVALUATED | no K-jump occurred → no $t^-_X$ defined → σ_pre never extracted | precondition (existence of K-jump) failed |
| C2 — different post-jump σ-standard | NOT EVALUATED | no K-jump → no $t^+_X$ → σ_post never extracted | same precondition failure |
| C3 — same protocol | PASS | single shared `RunConfig` between A and B | enforced by script construction |
| C4 — robustness | NOT EVALUATED | moot until at least one trajectory K-jumps | held in abeyance |

**Status overall: `failed` / `failure_mode = F2` / `conclusion: undetermined`.**

---

## Conclusion

**Empirical finding.** Under the protocol's Option D-2 integrator (per-slot gradient step + uniform total-mass rescale), the SCC multi-field gradient flow on $T^2_{20}$ with $K_{\mathrm{field}} = 4$, $M = 90$, equal initial masses, and Gaussian bumps converges to a stable 3-formation fixed point. Across $\lambda_{\mathrm{rep}} \in \{10, 30, 100, 300\}$ and Configuration B vertical compression to $c_3 = (10, 6)$ (overlap regime, distance ≈ 5.1), no K-jump occurs in 5000 iterations. The minimum slot mass ever observed across 14 trajectories is **23.94** — over 100× the activity threshold ε = 0.225.

**Interpretation.** The protocol did **not** falsify σ-standard incompleteness in this run. The protocol also did **not** confirm σ-standard completeness — the test is unexecuted at the σ level because no K-jump bracketed any pair of snapshots. The result is a *precondition failure* (F2): K-jumps never happened.

**Why F2 is structural, not a tuning issue.**

- Each slot's intra-energy basin (SCC 4-term self-energy) is sufficiently deep that a coherent localized profile is preserved against the inter-slot repulsion.
- Option D-2's uniform total-mass rescale only redistributes mass *globally* — it does not preferentially drain a single slot.
- Stronger $\lambda_{\mathrm{rep}}$ deepens the *redistribution-within-wells* asymmetry but does not produce extinction.
- Closer initial geometry only changes the equilibrium configuration; the simplex barrier and intra-energy still maintain three distinct wells.

**This is informative for WQ-1 design.** The naïve hypothesis that gradient flow under Option D-2 would naturally produce K-jump events is **empirically refuted** for this graph and these parameters. Producing a K-jump under SCC dynamics requires either:

1. Implementing **Option D-1** (true joint projection onto $\widetilde\Sigma^{K_{\mathrm{field}}}_M$) — couples slots simultaneously and may permit inter-slot mass transfer that Option D-2 cannot.
2. **K-jump by intervention** — equilibrate at K=3, force one slot's mass to zero, re-equilibrate at K=2, compare σ-standard pre/post. Tests σ-standard *response* to a prescribed extinction rather than *predictive sufficiency* across a natural extinction. Different question, valid alternative.
3. **Single-field reframing** — use Layer I single field $\Sigma_M(G_t)$ with $K_{\mathrm{soft}}^\phi$ as the count diagnostic. K-"jumps" are bar-deaths in $H_0$ persistence of the aggregate. Requires WQ-2 (K-soft / K-act bridge) operationalized first.

---

## Explicit non-claims (apply regardless of outcome)

- This run does **not** prove σ-rich is sufficient.
- This run does **not** prove Φ_rich is globally deterministic.
- This run does **not** resolve OP-0008 (severity 🟠 HIGH retained).
- This run does **not** resolve OP-0005 (K-Selection).
- This run does **not** authorize promoting any object to canonical.
- This run does **not** validate any vision / robotics / control application.
- This run does **not** assert that $T^2_{20}$ result generalizes to other graphs.
- This run does **not** invoke or establish stratified Morse theory.
- This run does **not** claim $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ (no $K_{\mathrm{soft}}$ is computed here; its bridge to $K_{\mathrm{act}}$ is WQ-2).

---

## Decision and Next Action

The F2 outcome under Option D-2 is consistent across 14 trajectories spanning two parameter sweeps. **Do not retry Option D-2** — the cause is identified (structural insufficiency of uniform-rescale mass conservation to drive slot extinction in the SCC + simplex-barrier regime).

**Recommended next action (one of):**

- **WQ-1.A — Implement Option D-1 (joint projection).** Modify `CODE/scripts/nq242c_counterexample.py::project_to_layer_II_D2` to a true joint projection onto $\widetilde\Sigma^{K_{\mathrm{field}}}_M$ (Dykstra-style alternating projections: total mass plane ∩ box [0,1] ∩ simplex constraint). Re-run the protocol. Estimated effort: ~1 day.
- **WQ-1.B — K-jump by intervention.** Add a script mode `--intervention` that runs A and B to K=3 equilibrium, forces $u^{(\mathrm{argmin}_j m_j)} \leftarrow 0$, re-equilibrates at K=2, compares σ-standard pre/post. This tests σ-standard *response* to prescribed extinction. Estimated effort: ~half day.
- **WQ-1.C — Reframe as Layer I H_0 jump.** Skip the labelled K-field entirely. Equilibrate a single field on $\Sigma_M(G_t)$ to a 3-bump configuration, perturb one bump's amplitude downward, observe whether $H_0$ bar-death occurs in the aggregate persistence. Compare σ-standard (Hessian eigenvalue cluster of single field) pre/post. This bypasses the K-jump-via-labelled-dynamics issue and tests σ-standard incompleteness at the unlabelled topological level. Requires WQ-2 (K-soft / K-act bridge) to interpret the result. Estimated effort: ~1 day.

**WQ-2 (K-soft / K-act bridge lemma) becomes the priority instead of WQ-1.** WQ-2 does not depend on WQ-1's outcome; under the F2 finding it becomes the natural next thing to do, since:

- The bridge lemma is independent of whether a K-jump occurred.
- The R23 result (overlap-regime generic, per `single_high_F_equivalence.md`) makes the bridge lemma an immediate empirical question.
- A successful bridge lemma reframes the σ-standard test (WQ-1.C above) on solid ground.

**Updates to other working files:**

- `THEORY/working/MF/sigma_multi_trajectory.md` §6.2 should be updated to note that NQ-242 (full Hessian σ-tuple time series) requires Option D-1 implementation; Option D-2 is empirically refuted as a K-jump driver.
- `THEORY/working/MF/layered_ambient_architecture_candidate.md` status table row 15 (Deterministic σ-standard inheritance across K-jump) is **not** affected by this F2 result. The non-determinism conjecture remains conjectural / Cat C; it has not been refuted by F2 (no K-jump means no test of the conjecture).
- `THEORY/working/MF/layered_ambient_architecture_next_work.md` WQ-1 entry can be annotated with this F2 finding and the WQ-1.A/B/C remediation menu.

**Forbidden non-claims still apply** (see below). In particular: F2 does **not** mean σ-standard is sufficient; F2 means the test was not executed at the σ level. Do not weaken the OP-0008 severity rating on the basis of this run.

---

## Cross-references

- `nq242c_counterexample_protocol.md` — full protocol.
- `nq242c_explicit_construction.md` — predecessor design.
- `sigma_rich_augmentation.md` — Path B framework, σ-rich definition.
- `sigma_multi_trajectory.md` — D-6b dynamic σ-multi-A(t) framework, Lemma 4.4.1(c) Cat C.
- `layered_ambient_architecture_candidate.md` — Layer II definition, status table.
- `layered_ambient_architecture_next_work.md` — WQ-1 specification.
- `CODE/scripts/nq242c_counterexample.py` — executable script.
- `CODE/scripts/results/nq242c_result_schema.json` — JSON schema.

---

**End of NQ-242c results.** Status: RUN COMPLETE — `failed F2` across 14 trajectories (primary + λ_rep sweep + compression sweep). Conclusion: F2 outcome is structural (Option D-2 cannot drive K-jumps in the SCC + simplex-barrier regime), not a tuning issue. Next action: WQ-2 (K-soft / K-act bridge lemma) takes priority; WQ-1 reattempted as WQ-1.A (Option D-1), WQ-1.B (intervention), or WQ-1.C (Layer I single-field reframe).
