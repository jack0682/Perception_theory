# Layered Ambient-State Architecture — Next Work Packages

**File:** `THEORY/working/MF/layered_ambient_architecture_next_work.md`
**Companion docs:** `layered_ambient_architecture_README.md`, `layered_ambient_architecture_candidate.md`, `layered_ambient_architecture_agent_notes.md`.
**Audience:** Future agents executing the next research sequence under the layered ambient-state architecture.

---

## Order of work

The work packages are sequenced. The rationale is in `layered_ambient_architecture_agent_notes.md` §6.

```text
0. Layered ambient documentation         (this package — DONE)
1. NQ-242c counterexample protocol       (WQ-1)
2. K-soft / K-act bridge lemma           (WQ-2)
3. σ-rich minimal packet analysis        (WQ-3, requires WQ-1 results)
4. K-selection three-model comparison    (WQ-4)
5. Stratified ambient feasibility check  (WQ-5)
```

Each package below specifies: **goal**, **input files**, **output artifact**, **success criterion**, **forbidden claims**, **dependency on the layered architecture**.

---

## WQ-1 — NQ-242c Counterexample Protocol

### Goal

Numerically demonstrate σ-standard non-determinism at a K-jump event by explicit construction of two trajectories on $T^2_{20}$ — Configuration A (equilateral disk-triangle) and Configuration B (isoceles disk-triangle, slightly compressed) — sharing σ-standard at $t = 0$ and at $t^{*-}$ but exhibiting distinct σ-standard at $t^{*+}$. Simultaneously evaluate σ-rich determinism (Φ_rich prediction vs. numerical post-jump σ-rich) on the same construction.

### Input files

- `THEORY/working/MF/nq242c_explicit_construction.md` — full setup (§§2–4), script outline (§5), Cat A criteria (§6).
- `THEORY/working/MF/sigma_rich_augmentation.md` — Path B framework, σ-rich definition, Φ_rich definition (§3.3).
- `THEORY/working/MF/sigma_rich_phi_proof.md`, `sigma_rich_wigner_derivation.md`, `sigma_rich_centroid_derivation.md`, `sigma_rich_orientation_derivation.md` — σ-rich component derivations.
- `THEORY/working/MF/sigma_multi_trajectory.md` — Lemma 4.4.1(c) Cat C source; §3.7 PH reformulation; FM1–FM4 known failure modes.
- `THEORY/working/MF/sigma_rich_VR_phase1.md` — Vietoris-Rips / PH V-R Phase 1 plan.
- `CODE/scc/multi.py` — existing `find_k_field_formation`, `gradient_flow_trajectory`.
- `CODE/scc/diagnostics.py` — existing `compute_sigma_tuple_multi`.
- (To be created) `CODE/scc/sigma_rich.py` — σ-rich extraction and Φ_rich application module (per `nq242c_explicit_construction.md` §5.2).
- (To be created) `CODE/scripts/nq242c_construction.py` — main script (per `nq242c_explicit_construction.md` §5.1 outline).

### Output artifact

1. `CODE/scripts/nq242c_construction.py` — numerical script.
2. `CODE/scc/sigma_rich.py` — σ-rich module.
3. `CODE/scripts/results/nq242c_construction.json` — JSON results, schema in `nq242c_explicit_construction.md` §5.3.
4. `THEORY/working/MF/nq242c_results.md` — results write-up:
   - Cat-status updates against (C1) σ-standard non-determinism, (C2) σ-rich distinguishability at $t^{*-}$, (C3) Φ_rich determinism, (C4) generality probe;
   - identified regime of each trajectory (well-separated / overlap / corner-saturated) at sampled time points;
   - identified K-jump times and active-set transitions (which $A \to A'$).
5. Update entries in `THEORY/working/MF/sigma_multi_trajectory.md` §6.2 and in this file's status table referencing WQ-1 outcome.

### Success criterion

All of the following are met:

- (C1) $\sigma_{\mathrm{standard}}^A(t^{*+}) \ne \sigma_{\mathrm{standard}}^B(t^{*+})$ at qualitative-tuple precision $10^{-3}$, while $\sigma_{\mathrm{standard}}^A(t^{*-}) = \sigma_{\mathrm{standard}}^B(t^{*-})$ and $\sigma_{\mathrm{standard}}^A(0) = \sigma_{\mathrm{standard}}^B(0)$.
- (C2) $\sigma_{\mathrm{rich}}^A(t^{*-}) \ne \sigma_{\mathrm{rich}}^B(t^{*-})$ via at least one of $\{c, \Theta, W\}$ components.
- (C3) Φ_rich applied to $\sigma_{\mathrm{rich}}^A(t^{*-})$ predicts $\sigma_{\mathrm{rich}}^A(t^{*+})$ within tolerance: centroid $10^{-2}$ graph units; orientation $1°$; Wigner-data post-merger Goldstone gap < $10^{-3}$. Same for B.
- (C4) Conclusions hold under small perturbations of Configuration B (~3 additional runs).

If (C1) fails on $T^2_{20}$ with the default parameters of `nq242c_explicit_construction.md` §2, fall back per §3.4: try higher-anisotropy graphs (rectangular torus $T^2_{20 \times 30}$, hexagonal lattice) or larger geometric difference in B.

### Forbidden claims

- Promoting σ-rich to canonical on the basis of (C3) holding for A and B alone — that requires (R1)–(R4) of `nq242c_explicit_construction.md` §6.2.
- Promoting the layered architecture to canonical because NQ-242c succeeded.
- Claiming OP-0008 is resolved; at most claim it is *partially attacked* with a numerical anchor for Path B.
- Claiming the result on $T^2_{20}$ generalizes globally.
- Re-interpreting any single-formation theorem as the multi-formation analogue.

### Dependency on the layered architecture

- The two trajectories live in $\widetilde{\Sigma}^{K_{\mathrm{field}} = 4}_{M = 90}(T^2_{20})$ — Layer II.
- The active-set cell at $t = 0$ is $S_A^\varepsilon$ with $A = \{1, 2, 3\}$, $K_{\mathrm{act}}^\varepsilon = 3$.
- The K-jump is an event-only transition $S_A^\varepsilon \to S_{A'}^\varepsilon$ with $|A'| < |A|$.
- σ-standard / σ-rich are derived diagnostics on Layer II states; their bridge to aggregate $H_0$ topology uses $U(\mathbf u)$ and $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ from Layer II → Layer I.
- WQ-1 is the empirical anchor that makes WQ-3 well-posed.

---

## WQ-2 — K-soft / K-act Bridge Lemma

### Goal

State and either prove (or refute by counterexample) a bridge lemma of the form:

> **Lemma (target).** Under the well-separated regime hypotheses $(\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min})$ of `..._candidate.md` §9.1, for any monotone Lipschitz $\phi : [0,1] \to [0, \infty)$ with $\phi(0) = 0$,
>
> $$
> K_{\mathrm{soft}}^\phi\big(U(\mathbf u)\big) \;=\; |A| \cdot \phi(\ell_*(\mathbf u)) \;+\; e(\phi, \varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min}, G_t),
> $$
>
> with $K_{\mathrm{act}}^\varepsilon(\mathbf u) = |A|$, where $\ell_*(\mathbf u)$ is a typical bar length and $e$ is an explicit error term that vanishes as $D_{\mathrm{sep}} \to \infty$, $\delta \to 0^+$, $\ell_{\min} \to \ell_*$, with explicit dependence on $G_t$ through graph diameter / spectral gap.

The output is the lemma in *its actual provable form* — which may differ from the target form above; precise statement, hypotheses, and error term are part of the deliverable.

### Input files

- `THEORY/working/MF/layered_ambient_architecture_candidate.md` §6, §9 — definitions and regime discipline.
- `THEORY/working/E/soft_K_definition.md` (dormant) — pre-architecture $K_{\mathrm{soft}}$ proposal; this package upgrades to the $\phi$-envelope form.
- `THEORY/working/MF/mathematical_scaffolding_4tools.md` §4 — Tool A3 PH foundation; Cohen-Steiner stability citation.
- `THEORY/working/MF/single_high_F_equivalence.md` (OAT-7) — R23 dataset analysis showing overlap regime is *generic* in the high-$\mathcal{F}$ regime; the bridge lemma is *not* expected to apply generically on R23.
- `CODE/scc/persistence.py`, `CODE/scc/transport.py` — existing persistence pipeline (cohesion fingerprint, transport-based persist).
- (Optional probe) `CODE/scripts/k_soft_k_act_bridge_probe.py` — synthetic well-separated multi-disk configurations for $e(\cdot)$ estimation.

### Output artifact

1. `THEORY/working/MF/k_soft_k_act_bridge_lemma.md` (~300–500 lines):
   - precise lemma statement (or counterexample);
   - hypotheses (well-separation parameters, $\phi$ family);
   - proof sketch (or counterexample construction);
   - error-term form with explicit graph-dependence;
   - sensitivity analysis: what happens if $\phi$ is sub-linear vs. linear vs. concave near 0; what happens as $D_{\mathrm{sep}} \to D_{\mathrm{crit}}^+$; what happens as $\ell_{\min} \to 0^+$;
   - failure modes: explicit examples of overlap-regime configurations where $K_{\mathrm{soft}}^\phi$ and $K_{\mathrm{act}}^\varepsilon$ diverge.
2. Update `..._candidate.md` status table row 12 with the actual proven status (working-definition safe → theorem-grade under existing hypotheses, if the proof goes through).
3. (Optional) `CODE/scripts/results/k_soft_k_act_bridge_probe.json` — synthetic estimates of $e(\cdot)$.

### Success criterion

A precise lemma statement with explicit hypotheses and explicit error term is reached. *Either* a proof sketch is provided, *or* a counterexample is constructed showing that the lemma in its proposed form fails. In the latter case, a reformulated lemma is proposed and the cycle is iterated within the same file (no second working file).

A *negative* result (counterexample to the target form, with reformulation in a strictly weaker form) counts as success.

### Forbidden claims

- Global identity $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$.
- Bridge holding in the overlap regime.
- Bridge holding in the corner-saturated regime.
- Importing the bridge into canonical without separate user decision and CV-1.6+ packet integration.
- Claiming the bridge resolves the K-Selection mechanism question (it does not; the bridge is a comparison statement, not a selection statement).

### Dependency on the layered architecture

- $K_{\mathrm{soft}}^\phi$ is defined on Layer I via the $H_0$ persistence diagram of the aggregate field.
- $K_{\mathrm{act}}^\varepsilon$ is defined on Layer II as a count diagnostic.
- The bridge sits at the Layer II → Layer I boundary, mediated by $U$.
- The well-separated regime is defined precisely within the architecture's regime discipline (§9.1 of `..._candidate.md`).

---

## WQ-3 — σ-rich Minimal Packet Analysis

### Goal

Determine the minimal set of augmentation data beyond plain σ-standard that achieves deterministic Φ_rich on the WQ-1 numerical anchor under simple-merger genericity. Compare candidate packets:

- (a) centroid only;
- (b) centroid + inertia tensor (per `sigma_rich_centroid_derivation.md`, `sigma_rich_orientation_derivation.md`);
- (c) centroid + inertia tensor + Wigner data (per `sigma_rich_wigner_derivation.md`);
- (d) centroid + $H_1$ barcode of $U(\mathbf u)$ (Tool A3 alternative);
- (e) hybrid combinations.

### Input files

- WQ-1 results: `CODE/scripts/results/nq242c_construction.json`, `THEORY/working/MF/nq242c_results.md`.
- `THEORY/working/MF/sigma_rich_augmentation.md` — current σ-rich definition; Path B framework.
- `THEORY/working/MF/sigma_rich_phi_proof.md` — Φ_rich proof scaffolding.
- `THEORY/working/MF/sigma_rich_wigner_derivation.md` — Wigner-data derivation.
- `THEORY/working/MF/sigma_rich_centroid_derivation.md` — centroid derivation.
- `THEORY/working/MF/sigma_rich_orientation_derivation.md` — orientation / inertia tensor derivation.
- `THEORY/working/MF/sigma_rich_vs_standard_R23.md` — empirical σ-rich vs. σ-standard comparison.
- `THEORY/working/MF/multi_formation_sigma.md` §5.5 — cross-formation Goldstone observation.
- `THEORY/working/MF/commitment_18_sigma_rich_packet.md` — Commitment 18 candidate packet.
- `THEORY/working/MF/layered_ambient_architecture_candidate.md` §11.5 — σ-rich precondition note.

### Output artifact

`THEORY/working/MF/sigma_rich_minimal_packet.md`:

- enumeration of candidate packets (a)–(e) with clear scope;
- per-packet Φ_rich determinism status on the WQ-1 anchor;
- redundancy analysis: which components in (b) or (c) are necessary, which are redundant;
- minimal-packet recommendation;
- failure-mode documentation if no packet in the candidate list works (with proposed enriched candidate list);
- explicit non-claim: minimal packet on WQ-1 anchor is *not* the minimal packet globally.

### Success criterion

The minimal augmentation that achieves Φ_rich determinism on the WQ-1 numerical anchor is identified, with explicit redundancy analysis. Where no candidate works, the failure is documented and an enriched candidate list is proposed for a follow-up iteration.

If WQ-1 (C1) failed (σ-standard non-determinism does not manifest), WQ-3 is **not executed**: σ-rich Path B is not motivated. Document this in the WQ-3 file as a "not-executed" entry pointing to WQ-1's negative result, and propose alternative paths (Path A retention; richer counterexample search).

### Forbidden claims

- Minimal packet on WQ-1 anchor = minimal packet globally.
- σ-rich resolves OP-0008.
- σ-rich is the unique augmentation; alternatives (e.g., $H_1$ persistent homology augmentation) remain admissible.
- Promoting σ-rich into canonical.
- Asserting that any augmentation is sufficient under the corner-saturated regime (the regime where smooth-segment piecewise-constancy of σ-multi-A is open).

### Dependency on the layered architecture

- σ-standard and σ-rich are derived diagnostics on Layer II states.
- The minimal-packet question is sharpened by the layered architecture: candidates that mix labelled and unlabelled data are admissible, and the bridge to aggregate $H_0$ topology (Layer II → Layer I via $U$) is one source of augmentation candidates.
- The σ-rich precondition (`..._candidate.md` §11.5) makes WQ-3 strictly downstream of WQ-1.

---

## WQ-4 — K-selection Three-Model Comparison

### Goal

Side-by-side analysis of three candidate K-selection mechanisms applied to R23 dataset trajectories, with explicit failure-mode characterization for each.

The three candidates per `k_selection_mechanism.md`:

- **(a) free-energy variational** — K_act emerges from free-energy minimization including entropy of cluster configuration.
- **(b) kinetic metastability (Kramers)** — K_act emerges from inter-formation barrier rates, with metastability $\propto \exp(c \beta)$.
- **(c) symmetry-broken automorphism-stabilizer dimension** — K_act fixed by the dimension of the residual stabilizer subgroup of $\mathrm{Aut}(G)$ at the symmetry-broken minimizer.

### Input files

- `THEORY/working/MF/k_selection_mechanism.md` — three Cat C candidates.
- `THEORY/working/MF/k_selection_a_free_energy.md` — candidate (a) development.
- `THEORY/working/MF/k_selection_b_kramers.md` — candidate (b) development.
- `THEORY/working/MF/k_selection_c_numerical_anchor.md` — candidate (c) numerical anchor design.
- `THEORY/working/MF/k_selection_compatibility_proof.md` — compatibility scaffolding.
- `THEORY/working/MF/commitment_19_k_selection_axiom_packet.md` — Commitment 19 axiom packet.
- `THEORY/working/MF/cn15_static_dynamic_separation.md` — CN15 candidate (why energy minimization $\ne$ $K_{\mathrm{act}} = 1$ at protocol endpoint).
- `THEORY/working/CE/free_energy_wellposed.md` — free-energy variational well-posedness.
- `CODE/experiments/exp51_k_selection.py` — existing K-selection empirical test on 10 graph configurations.
- `CODE/experiments/exp39_formation_birth.py` — formation birth kinetics for candidate (b).
- R23 dataset (90 runs) — already analysed in `THEORY/working/MF/single_high_F_equivalence.md` (OAT-7).

### Output artifact

`THEORY/working/MF/k_selection_three_model_comparison.md`:

- per-candidate model statement (clear functional form, hypotheses, free parameters);
- per-candidate prediction on R23 dataset;
- per-candidate observed agreement / disagreement (table form);
- residual error vector per candidate;
- implied refinement step per candidate (how to strengthen a partial-success candidate);
- a falsification register (which candidates are falsified by R23, and on what specific configurations);
- update to `THEORY/canonical/open_problems.md` OP-0005 entry — *as a candidate text in this working file, not a direct canonical edit* — noting which candidates survived and what is the next refinement step.

### Success criterion

For each candidate (a), (b), (c):

- explicit prediction-vs-data comparison is made;
- falsification or partial confirmation is documented;
- surviving candidate(s) are scoped to a follow-up package.

OP-0005 is **not** resolved by WQ-4. Resolution is not a success criterion; documented falsification or partial-confirmation is.

### Forbidden claims

- OP-0005 is resolved.
- Any single mechanism is uniquely correct.
- Any K-selection mechanism is promoted into canonical.
- Substituting Commitment 16 K-status decomposition for a selection mechanism.
- The architecture has been validated by surviving K-selection candidates.
- Claiming WQ-4 results lift from R23 to all graphs.
- Claiming all three candidates are mutually exclusive (they may be compatible at different scales).

### Dependency on the layered architecture

- All three candidate mechanisms are statements about $K_{\mathrm{act}}^\varepsilon$ (the dynamic active count), not $K_{\mathrm{field}}$ (the architectural cap).
- Trajectories are on Layer II; the steady-state question "what $K_{\mathrm{act}}$ does the dynamics select?" is well-posed only on Layer II, not on a Layer III fixed-mass slice.
- The CN15 Static/Dynamic Separation argument lives at the Layer II level; it explains why static energy minimization on Layer III does not force $K_{\mathrm{act}} = 1$ at the dynamic protocol endpoint.

---

## WQ-5 — Stratified Ambient Feasibility Check

### Goal

Determine whether the labelled cell refinement $\{S_A^\varepsilon\}$ and the ε-thresholded count regions $\{S_r^\varepsilon\}$ of Layer II carry a Whitney-stratified semi-algebraic structure (or a coarser regularity sufficient to invoke stratified Morse theory). Where Whitney verification fails, identify the failure loci and propose a minimal coarsening of the cell refinement that does verify.

### Input files

- `THEORY/working/MF/mathematical_scaffolding_4tools.md` §2 — current Whitney verification for the *intrinsic*-count stratification.
- `THEORY/working/MF/shared_pool_canonical_proposal.md` §3 — Goresky-MacPherson stratified Morse framework citation.
- `THEORY/working/MF/layered_ambient_architecture_candidate.md` §7 — active-set cells, ε-active-count regions, status §7.3 (stratifiability open).
- `THEORY/working/MF/op003_mo1_status_review.md` — MO-1 status: SIDESTEPPED at single-formation; multi-formation re-activation rider preserved.
- External references on Whitney stratification of semi-algebraic sets (Hironaka 1973, Mather 2012, Goresky-MacPherson 1988, per `mathematical_scaffolding_4tools.md` §9.1).

### Output artifact

`THEORY/working/MF/stratified_ambient_feasibility_check.md` (~400–600 lines):

- enumeration of cell-boundary loci of $\{S_A^\varepsilon\}$ (mass-threshold loci, simplex-saturation loci, field-boundary loci);
- frontier-condition test on $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$;
- Whitney-(A) test (tangent regularity);
- Whitney-(B) test (secant regularity);
- identification of failure modes per regime (well-separated / overlap / corner-saturated);
- minimal coarsening recommendation if any cell-level test fails (likely candidate: coarsen back to count-only $\{S_{K_{\mathrm{act}}}\}$);
- update to `..._candidate.md` status table row 13 with concrete feasibility verdict.

### Success criterion

A definitive verdict is reached:

- either "cell refinement $\{S_A^\varepsilon\}$ verifies Whitney; $\{S_r^\varepsilon\}$ verifies as quotient";
- or "cell refinement fails Whitney at locus $L$; minimal coarsening to $\{S_r^\varepsilon\}$ (or to intrinsic $\{S_{K_{\mathrm{act}}}\}$) is required for Goresky-MacPherson applicability";
- or "verification is stronger than required; weaker conical-stratification structure is sufficient and verified".

A *negative* verdict (cell refinement fails Whitney) is success: it tells downstream NQ-248 work to operate on the count-only stratification.

### Forbidden claims

- Stratified Morse is established machinery for the cell refinement.
- NQ-248 results are anticipated or invoked before WQ-5 is complete.
- OP-0003 MO-1 is resolved.
- The cell refinement is canonical-target.
- The count-only stratification is sufficient for *labelled* trajectory analysis (it is sufficient for *count* analysis only).
- Whitney-(B) holds automatically because Whitney-(A) holds (it does not in general).

### Dependency on the layered architecture

- Layer II is the ambient. The Whitney verification of `mathematical_scaffolding_4tools.md` §2.2 is *for Layer II's count-only stratification*, not for the labelled cell refinement of `..._candidate.md` §7.
- WQ-5's outcome decides what flavor of stratified Morse (cell-level or count-level) is available for any future MO-1 multi-formation re-activation.
- The architecture's regime discipline (well-separated / overlap / corner-saturated) maps onto cell-boundary structure in WQ-5: corner-saturation corresponds to simplex-saturation loci; well-separation corresponds to interior-of-cell behavior.

---

## Summary Table

| Pkg | Goal (one-line) | Output file | Critical dependency | Forbidden top claim |
|---|---|---|---|---|
| WQ-1 | NQ-242c numerical anchor | `nq242c_results.md` + JSON | Layer II + cell + K-jump definitions | "OP-0008 is resolved" |
| WQ-2 | K-soft / K-act bridge lemma | `k_soft_k_act_bridge_lemma.md` | Layer II → Layer I projection $U$ + well-separated regime | "$K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$" |
| WQ-3 | σ-rich minimal packet | `sigma_rich_minimal_packet.md` | WQ-1 results; σ-rich precondition | "σ-rich is globally sufficient" |
| WQ-4 | K-selection three-model comparison | `k_selection_three_model_comparison.md` | Layer II dynamics; CN15 | "OP-0005 is resolved" |
| WQ-5 | Stratified ambient feasibility check | `stratified_ambient_feasibility_check.md` | Layer II count vs. cell stratification | "Cell refinement is Whitney-verified" |

---

**End of next-work file.**

**Status: working draft, task board for the layered ambient-state architecture line. WQ-1 through WQ-5 to be executed in order.**

**Reading order for new agents:**

```text
1. layered_ambient_architecture_README.md           (orientation)
2. layered_ambient_architecture_agent_notes.md      (guardrails)
3. layered_ambient_architecture_candidate.md        (definitions, status)
4. layered_ambient_architecture_next_work.md        (this file — what to do next)
```
