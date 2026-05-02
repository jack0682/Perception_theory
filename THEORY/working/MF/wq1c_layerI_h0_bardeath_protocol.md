# WQ-1.C — Layer I H_0 Bar-Death Counterexample Protocol

**File:** `THEORY/working/MF/wq1c_layerI_h0_bardeath_protocol.md`
**Document type:** Working-grade executable protocol (non-canonical).
**Created:** 2026-05-02 (WQ-1.C, retry path of WQ-1 selected by WQ-2 decision rule).
**Status:** working draft. Protocol specified; executable script in `CODE/scripts/wq1c_layerI_h0_bardeath.py`.

**Companion artifacts:**
- `THEORY/working/MF/wq1c_layerI_h0_bardeath_results.md` — results placeholder / outcome record.
- `CODE/scripts/wq1c_layerI_h0_bardeath.py` — executable script.
- `CODE/scripts/results/wq1c_layerI_h0_bardeath_results.json` — JSON output (after run).

**Predecessor artifacts:**
- `THEORY/working/MF/layered_ambient_architecture_candidate.md` — Layer I ambient $\Sigma_M(G_t)$, $K_{\mathrm{soft}}^\phi$ (§6.4), regime discipline (§9).
- `THEORY/working/MF/nq242c_counterexample_protocol.md` — WQ-1 protocol on Layer II.
- `THEORY/working/MF/nq242c_results.md` — WQ-1 F2 outcome.
- `THEORY/working/MF/ksoft_kact_bridge_lemma.md` — WQ-2 bridge lemma + WQ-2.D-1 production-run outcome ($K_{\mathrm{bar}}^{0.10}$ : 3 → 1 along F2 trajectory).
- `THEORY/working/E/soft_K_definition.md` — pre-existing $K_{\mathrm{soft}}^\phi$ definition with (φ-sat) and (φ-lin).
- `CODE/scripts/nq242c_counterexample.py`, `CODE/scripts/ksoft_kact_diagnostics.py` — predecessor scripts (torus builder, persistence pipeline, σ extraction reused).

---

## 1. Status and Scope

This is the **WQ-1.C retry path** of WQ-1, selected by the WQ-2 bridge-lemma decision rule (`ksoft_kact_bridge_lemma.md` §9.1) on the basis of the WQ-2.D-1 empirical finding that aggregate-field $H_0$ topology changes ($K_{\mathrm{bar}}^{0.10}$ : 3 → 1) along the WQ-1 F2 trajectory.

**Status grade per claim.**

| Claim | Status |
|---|---|
| Layer I single-field ambient $\Sigma_M(G_t)$ | working-definition safe (`canonical.md` §3 baseline) |
| Single-field SCC gradient flow on $\Sigma_M(G_t)$ | working-definition safe (reuses canonical 4-term energy via `scc/energy.py`) |
| H_0 bar-death event definition | working-definition safe (per `ksoft_kact_bridge_lemma.md` §5.1) |
| σ-standard extracted by `scc/sigma_rich.py::_sigma_standard` | working-only Cat B sketch placeholder; FD-Hessian on single field |
| σ-standard incompleteness across H_0 bar-death | conjectural / downstream — *target of this protocol* |
| Multi-formation σ-standard incompleteness across labelled $K_{\mathrm{act}}$-jumps (OP-0008) | **forbidden non-claim** for this protocol |
| σ-rich sufficiency | forbidden non-claim |

**Scope.** Single executable counterexample construction at Layer I ($\Sigma_M(G)$), two single-field trajectories, one bar-death event per trajectory under a threshold sweep. The protocol is not designed to prove a global theorem; it is designed to determine whether σ-standard is sensitive, incomplete, or ambiguous across an unlabelled aggregate-topology transition on the same graph used in WQ-1 / WQ-2.

**Out of scope.**

- OP-0008 multi-formation σ-standard incompleteness across labelled $K_{\mathrm{act}}$-jumps. WQ-1.C is a Layer I *analogue*, not a proof of OP-0008.
- σ-rich global sufficiency.
- K-Selection mechanism (OP-0005).
- Stratified Morse / Whitney verification on Layer I.
- Vision / robotics / control application.
- Canonical promotion of any object.

---

## 2. Motivation from WQ-1 and WQ-2

### 2.1 WQ-1 outcome (recap)

WQ-1 NQ-242c protocol on Layer II ($\widetilde{\Sigma}^{4}_{90}(T^2_{20})$) ran 14 trajectories (primary + λ_rep sweep + B-compression sweep). All 14 returned `failed F2`: $K_{\mathrm{act}}^\varepsilon$ stayed at 3, minimum slot mass 23.94 (>> ε=0.225). No labelled K-jump occurred.

**Conclusion.** Under Option D-2 (per-slot gradient + uniform total-mass rescale) on the SCC + simplex barrier energy, the dynamics finds a stable 3-formation fixed point. σ-standard incompleteness across labelled $K_{\mathrm{act}}$-jumps cannot be tested without producing a $K_{\mathrm{act}}$-jump.

### 2.2 WQ-2 outcome (recap)

WQ-2 bridge lemma (`ksoft_kact_bridge_lemma.md`) defined the bridge between $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ (labelled count on Layer II) and $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ (unlabelled topological count of aggregate $U$). The diagnostic script (`ksoft_kact_diagnostics.py`) was run on the canonical WQ-1 F2 configuration (max_iter=5000, default parameters):

| Quantity | A | B |
|---|---|---|
| $K_{\mathrm{act}}^\varepsilon$ start → end | 3 → 3 (rigid) | 3 → 3 (rigid) |
| $K_{\mathrm{bar}}^{0.10}(U)$ start → end | **3 → 1 (changed)** | **3 → 1 (changed)** |
| $K_{\mathrm{soft}}^\phi(U)$ range | 1.797 | 1.788 |
| Regime | corner-saturated → overlap | corner-saturated → overlap |

**Conclusion.** Even when labelled $K_{\mathrm{act}}^\varepsilon$ is rigid, the *aggregate field* $U(\mathbf u(t)) = \sum_j u^{(j)}(t)$ undergoes substantial unlabelled topological transitions. F-B6 of the bridge lemma is empirically confirmed.

### 2.3 What WQ-1.C now tests

Reframe the σ-test from labelled $K_{\mathrm{act}}$-jump (Layer II) to unlabelled $H_0$ bar-death (Layer I aggregate or directly on a single field):

> Do there exist two single-field trajectories $u_A(t), u_B(t) \in \Sigma_M(G)$ such that both undergo the same type of $H_0$ bar-count transition, have matching pre-event σ-standard signatures, but have different post-event σ-standard signatures?

This is a **Layer I analogue**, not OP-0008. The connection to OP-0008 requires the WQ-2 bridge lemma plus an additional implication argument linking single-field aggregate dynamics to multi-field labelled dynamics. That implication is *not* part of WQ-1.C.

---

## 3. Formal Target Statement

**WQ-1.C Layer-I H_0 Bar-Death Incompleteness Target.** There exist two single-field trajectories

$$
u_A(t),\; u_B(t) \;\in\; \Sigma_M(T^2_{20})
$$

generated by the same SCC single-field projected gradient-flow rule (same graph, total mass $M$, energy parameters, integrator, projection, snapshot interval, stopping rule, σ extraction, threshold $\ell_{\min}$, tolerance $\tau_\lambda$), such that:

1. Both trajectories undergo an $H_0$ hard-bar-count transition at some times $t_A^*$, $t_B^*$:

   $$
   K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u_A(t_A^-)\big) \;>\; K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u_A(t_A^+)\big), \qquad K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u_B(t_B^-)\big) \;>\; K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u_B(t_B^+)\big).
   $$

2. Pre-event signatures match within tolerance $\tau_\lambda$:

   $$
   \sigma_{\mathrm{standard}}\!\big(u_A(t_A^-)\big) \;=_\tau\; \sigma_{\mathrm{standard}}\!\big(u_B(t_B^-)\big).
   $$

3. Post-event signatures differ beyond tolerance:

   $$
   \sigma_{\mathrm{standard}}\!\big(u_A(t_A^+)\big) \;\ne_\tau\; \sigma_{\mathrm{standard}}\!\big(u_B(t_B^+)\big).
   $$

**Interpretation if validated.** The (working, FD-Hessian, projected) σ-standard implementation is **not complete** for $H_0$ bar-death inheritance under the constructed Layer I conditions on $T^2_{20}$.

**Non-conclusion.** This does **not** prove the multi-formation OP-0008 claim for labelled $K_{\mathrm{act}}^\varepsilon$-jumps. The implication (Layer I aggregate-topology incompleteness ⇒ Layer II labelled-K incompleteness) requires the WQ-2 bridge lemma to be *quantitatively* established (currently sketch only) plus an additional argument about how single-field dynamics relates to multi-field labelled dynamics. That argument is not part of WQ-1.C.

---

## 4. Non-Claims

This protocol does not claim:

- σ-rich is sufficient (no σ-rich sufficiency claim made under any outcome);
- Φ_rich is deterministic;
- σ-standard is *globally* incomplete (only the projected single-field FD-Hessian implementation, on this graph, under these conditions);
- $K_{\mathrm{soft}}^\phi(u) = K_{\mathrm{act}}^\varepsilon$ (no labelled $K_{\mathrm{act}}$ exists at Layer I);
- $\{S_A^\varepsilon\}$ are Whitney strata;
- stratified Morse theory is established machinery;
- $H_0$ bar-death is a labelled K-jump;
- a positive WQ-1.C result implies OP-0008 resolution;
- canonical promotion of any object.

OP-0008 retains 🟠 HIGH severity unconditionally.

---

## 5. Graph and State-Space Setup

### 5.1 Graph

$$
G = T^2_{20}, \qquad X = \mathbb Z_{20} \times \mathbb Z_{20}, \qquad |X| = 400.
$$

4-regular periodic boundary, identical to the WQ-1 / WQ-2 torus construction (`nq242c_counterexample.py::build_torus`). Reused via import.

### 5.2 Layer I single-field ambient

$$
\Sigma_M(G) = \Big\{ u : X \to [0, 1] \;\Big|\; \sum_{x \in X} u(x) = M \Big\}, \qquad M = 90 \text{ (default)}.
$$

This is the **primitive single-field ambient** of `..._candidate.md` Layer I. No labels. No multi-field structure. No simplex barrier (the constraint $u(x) \in [0, 1]$ is a per-coordinate box, not a simplex over $K$ slots).

### 5.3 Activity threshold (not used at Layer I)

The Layer II quantity $\varepsilon$ has no role here — there are no labelled slots to threshold. The relevant threshold is the persistence threshold $\ell_{\min}$ on $H_0$ bars.

### 5.4 Topological count

For $u \in \Sigma_M(G)$:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(u) \;:=\; \#\big\{ i : \ell_i(u) \ge \ell_{\min} \big\},
$$

$$
K_{\mathrm{soft}}^\phi(u) \;:=\; \sum_i \phi(\ell_i(u)),
$$

where $\ell_i(u)$ are the lengths of bars in the $H_0$ superlevel persistence diagram $\mathrm{Dgm}_0^{\sup}(u; G)$, and $\phi(\ell) = \ell / (\ell + \ell_{\min})$ in the (φ-sat) family of `soft_K_definition.md` §1.

### 5.5 Threshold sweep

The default $\ell_{\min} = 0.10$ matches WQ-2.D-1 (which observed 3 → 1 at this threshold). To test threshold robustness, sweep:

$$
\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}.
$$

Bar-death events are detected separately for each $\ell_{\min}$, and the C5 robustness criterion (§10) is evaluated across the sweep.

### 5.6 Event definition

A trajectory $u(t)$ exhibits an **$H_0$ bar-death event at $\ell_{\min}$ at time $t^*$** iff for two consecutive recorded snapshots $\tau_i, \tau_{i+1}$ with $\tau_i < t^* \le \tau_{i+1}$,

$$
K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u(\tau_i)\big) \;>\; K_{\mathrm{bar}}^{\ell_{\min}}\!\big(u(\tau_{i+1})\big).
$$

Define $t^- := \tau_i$, $t^+ := \tau_{i+1}$. If multiple events occur, the *first* event is the protocol's primary target; subsequent events are recorded but not used for the σ pre/post comparison unless explicitly noted.

This is an **event definition only**. It does not assert determinism, single-event genericity, or any inheritance structure.

---

## 6. Initial Configuration Design

Two single-field configurations $u_A(0), u_B(0) \in \Sigma_M(G)$, both 3-bump aggregate fields differing only in geometric arrangement.

### 6.1 Configuration A-I — Equilateral aggregate

Centers (matching WQ-1 Configuration A, used here as bump centers in a single field):

$$
c_1^A = (5, 5), \qquad c_2^A = (15, 5), \qquad c_3^A = (10, 14).
$$

Pairwise torus distances ≈ 10 each (closest integer-grid approximation of an equilateral triangle on $T^2_{20}$).

### 6.2 Configuration B-I — Compressed isosceles aggregate

Centers (matching WQ-1 Configuration B):

$$
c_1^B = (5, 5), \qquad c_2^B = (15, 5), \qquad c_3^B = (10, 11).
$$

Pairwise torus distances: $\{10, \sqrt{61}, \sqrt{61}\} \approx \{10, 7.81, 7.81\}$.

### 6.3 Three initialization variants

WQ-2 noted that the WQ-1 default Gaussian bumps with $\sigma_b = 2.0$ and per-slot mass $30$ produce *saturated* peaks ($u(x) \approx 1$ at bump centers), classified as corner-saturated regime at $t = 0$. To distinguish substantive dynamics from initialization-state artifacts, run three variants:

#### V0 — saturated_gaussian (continuity with WQ-1 / WQ-2)

Construct $\tilde u(x) = \sum_{j=1}^{3} \exp(-d_T(x, c_j)^2 / (2 \sigma_b^2))$ with $\sigma_b = 2.0$, then normalize $u(x) = M \cdot \tilde u(x) / \sum_x \tilde u(x)$, then clip to $[0, 1]$ and re-project to $\Sigma_M$. May produce $u(x) \approx 1$ at bump centers.

#### V1 — capped_smooth (non-saturated)

Same construction as V0, but cap $u(x) \le u_{\max} = 0.7$ before re-projection. Iteratively: clip to $[0, u_{\max}]$, redistribute the excess uniformly across remaining capacity, repeat until both constraints hold (or up to 5 iterations). Then $\sum_x u(x) = M$ and $\max_x u(x) \le u_{\max}$ approximately.

If $M / (u_{\max} \cdot |X|) > 1$, the cap is infeasible — V1 is then skipped or run with reduced $M$.

For $M = 90$, $u_{\max} = 0.7$, $|X| = 400$: $M / (u_{\max} \cdot |X|) = 90 / 280 \approx 0.32 < 1$, so V1 is feasible.

#### V2 (optional) — low_mass

Same as V0 but $M = 45$ (half mass; flatter natural peaks). Used as sensitivity probe; not required for primary success.

### 6.4 Mass-preserving projection

After construction, enforce $u \in \Sigma_M$ via `scc.optimizer.project_volume(u, M)` (existing utility). For V1 (capped), iterate clip + project until both constraints hold (similar to `nq242c_counterexample.build_initial_state` simplex-enforcement loop).

---

## 7. Dynamics

### 7.1 Energy

The **canonical SCC single-field 4-term energy** as implemented in `scc/energy.py::EnergyComputer`:

$$
\mathcal{E}(u) \;=\; \mathcal{E}_{\mathrm{cl}}(u) + \mathcal{E}_{\mathrm{sep}}(u) + \mathcal{E}_{\mathrm{bd}}(u) + \mathcal{E}_{\mathrm{tr}}(u),
$$

per canonical §8. No multi-formation repulsion ($\lambda_{\mathrm{rep}}$ does not apply at Layer I). No simplex barrier ($\lambda_{\mathrm{bar}}$ does not apply). Box constraint $u(x) \in [0, 1]$ enforced by clip in `project_volume`.

### 7.2 Numerical integration

Discrete projected gradient descent on $\Sigma_M(G)$:

```
for τ = 1, ..., max_iter:
    g       = ec.gradient(u)
    g_proj  = g − mean(g)              // project onto T(Σ_M) = {v : Σ v_i = 0}
    u       = project_volume(u − dt · g_proj, M)   // mass-preserving box projection
```

`project_volume` is the existing `scc/optimizer.project_volume`: project onto the simplex $\Sigma_M = \{u \in [0, 1]^n : \sum u = M\}$.

### 7.3 Default parameters

| Symbol | Value | Note |
|---|---|---|
| $G$ | $T^2_{20}$ | 4-regular periodic |
| $M$ | 90 (V0, V1), 45 (V2) | total mass |
| $\sigma_b$ | 2.0 | initial bump width |
| $u_{\max}$ | 0.7 (V1 only) | per-vertex cap |
| ParameterRegistry | repo defaults | SCC 4-term parameters |
| $dt$ | $10^{-3}$ | initial time step |
| `max_iter` | 5000 | maximum outer iterations |
| `snapshot_every` | 25 | snapshot interval |
| stopping | $\max \|g\|_\infty < 10^{-5}$ for ≥ 50 iter | gradient stagnation |
| seed | 42 (default; configurable) | not strictly needed at Layer I (no random init) but recorded |

### 7.4 Snapshot recording

Each snapshot stores $u(\tau)$ in memory. From the snapshot, the script computes:

- $K_{\mathrm{bar}}^{\ell_{\min}}(u(\tau))$ for all $\ell_{\min}$ in the sweep;
- $K_{\mathrm{soft}}^\phi(u(\tau))$ at default $\ell_{\min} = 0.10$;
- bar lengths sorted descending;
- $\mathcal{F}(u(\tau))$ (strict local maxima count);
- σ-standard via `compute_sigma_rich` *only at bar-death snapshots*: pre-event $t^- = \tau_i$ and post-event stabilization snapshot $t^{+}_{\mathrm{stab}} = t^+ + n_{\mathrm{stab}} \cdot$ snapshot_every with $n_{\mathrm{stab}} = 4$.

σ extraction is restricted to event-bracketing snapshots because FD-Hessian is $O(n^2) = O(400^2)$ gradient calls per snapshot ≈ 1 minute. Restricting to ~4 sigma evaluations per trajectory keeps the run under ~10 minutes.

---

## 8. H_0 Bar-Death Detection

### 8.1 H_0 superlevel persistence

At each snapshot, compute the $H_0$ superlevel persistence diagram $\mathrm{Dgm}_0^{\sup}(u(\tau); G)$ via the existing pipeline:

- `scc/diagnostics.py::_persistence_h0_graph(u, graph)` returns $(\ell_{\max}, \ell_{\mathrm{second}})$ — useful for some diagnostics but does not return the full barcode;
- a graph-agnostic full-barcode reimplementation, identical to `ksoft_kact_diagnostics.py::h0_barcode`, returns the full list of $(\text{birth}, \text{death})$ pairs sorted by length descending. Reused in this protocol.

### 8.2 Bar-death event flag

For each $\ell_{\min}$ in the sweep, compute $K_{\mathrm{bar}}^{\ell_{\min}}(u(\tau))$ at every snapshot. A bar-death event at $\ell_{\min}$ is flagged when consecutive snapshots give:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(u(\tau_i)) \;>\; K_{\mathrm{bar}}^{\ell_{\min}}(u(\tau_{i+1})).
$$

Define $t^- := \tau_i$, $t^+ := \tau_{i+1}$, $\Delta K := K^-_{\mathrm{bar}} - K^+_{\mathrm{bar}}$ (the drop magnitude).

### 8.3 Multi-event handling

If a trajectory exhibits multiple bar-death events at the same $\ell_{\min}$, the *first* event is the protocol's primary target. Subsequent events are recorded in the diagnostics but not used for the σ pre/post comparison unless first-event analysis fails.

If a bar-death event has $\Delta K \ge 2$ (e.g. 3 → 1 directly without intermediate 3 → 2 snapshot), it is recorded as a *multi-bar-death* event. The σ pre/post comparison still applies, but the event is flagged as multi-event for downstream interpretation.

### 8.4 Cross-trajectory event matching

For the C2 / C3 σ comparison, the events on A-I and B-I are matched by *event ordering*: the first bar-death event on A-I is compared to the first bar-death event on B-I (regardless of absolute time). If the events differ in $\Delta K$ (e.g. A is 3 → 2, B is 3 → 1), this is flagged but the σ pre/post comparison still proceeds.

---

## 9. σ-Standard Extraction

### 9.1 Implementation used

`scc/sigma_rich.py::compute_sigma_rich(u, graph_state, params, positions=positions, n_eig=6)`. The returned namedtuple's `.sigma_standard` field is a tuple of `(cluster_size, "mult-{cluster_size}", eigenvalue)` triples sorted by ascending eigenvalue.

For single-field input `u` of shape `(n,)`, `_normalize_field` reshapes to `(1, n)`, then `_hessian_eigenpairs` computes `u_mean = u.mean(axis=0) = u`, then builds the FD-Hessian on this single field. **For Layer I, this is exactly the FD-Hessian of the single field $u$ at the snapshot.** No projection or aggregate-averaging is needed.

### 9.2 Scope and limitations of this σ-standard

The σ implementation is documented as "working-only Cat B sketch (W5 Day 4, 2026-04-30)" in the `sigma_rich.py` module docstring. The irrep labels are multiplicity placeholders (`mult-{n}`) pending Aut(G)$_{u^*}$ character data. **WQ-1.C's σ-standard is therefore the cluster-tuple representation of the FD-Hessian eigenvalue spectrum, not the full irrep-decomposed σ-tuple of canonical Commitment 14.**

This is an explicit limitation. A positive WQ-1.C result is restricted to this σ implementation; future joint character-data integration may agree or disagree.

### 9.3 Equality criterion

Two σ-standard tuples agree iff:

1. Same number of clusters.
2. For each cluster, same cluster size.
3. For each cluster, eigenvalue agreement within $\tau_\lambda = 10^{-3}$.

Mismatch is recorded with the offending cluster index and $|\lambda^A - \lambda^B|$ value.

For C3 (post-event differ), require additionally that the maximum eigenvalue difference exceeds $10 \tau_\lambda = 10^{-2}$ (margin to rule out marginal numerical noise — same convention as WQ-1 protocol §7.3).

### 9.4 Sampling times

For each trajectory, given the first bar-death event at $\tau^* = \tau_{i+1}$ (so $t^- = \tau_i$, $t^+ = \tau_{i+1}$), σ-standard is extracted at:

- $t^-$ — pre-event snapshot;
- $t^{+}_{\mathrm{stab}} = \tau_{i + 1 + n_{\mathrm{stab}}}$ with $n_{\mathrm{stab}} = 4$ — post-event stabilization snapshot.

If the trajectory ends before $t^{+}_{\mathrm{stab}}$, use the last available snapshot.

If no bar-death event occurs, σ extraction is skipped (failure mode F-C1).

---

## 10. C1–C6 Criteria

### C1 — Bar-death event exists in both trajectories

For at least one $\ell_{\min}$ in the sweep, both A-I and B-I exhibit at least one bar-death event.

### C2 — Same pre-event σ-standard

$$
\sigma_{\mathrm{standard}}\!\big(u_A(t_A^-)\big) \;=_\tau\; \sigma_{\mathrm{standard}}\!\big(u_B(t_B^-)\big)
$$

within $\tau_\lambda = 10^{-3}$ (per §9.3).

### C3 — Different post-event σ-standard

$$
\sigma_{\mathrm{standard}}\!\big(u_A(t_A^+)\big) \;\ne_\tau\; \sigma_{\mathrm{standard}}\!\big(u_B(t_B^+)\big)
$$

with maximum eigenvalue difference $> 10 \tau_\lambda$ (per §9.3).

### C4 — Same protocol

Both runs use:

- same graph $G = T^2_{20}$;
- same total mass $M$;
- same energy parameters (`ParameterRegistry` defaults);
- same integrator, $dt$, `max_iter`, snapshot_every, stopping rule;
- same σ extraction implementation;
- same threshold $\ell_{\min}$ used to define the matched event;
- same initialization variant (V0, V1, or V2).

### C5 — Threshold robustness

At least one of:

- C2 ∧ C3 holds for **multiple** $\ell_{\min}$ values in the sweep $\{0.05, 0.10, 0.15, 0.20\}$ — preferred;
- the bar-death event ordering (A and B both jump in the same range of trajectory time) is stable across the threshold sweep — acceptable;
- failure is documented as explicitly threshold-dependent — acceptable as honest negative.

### C6 — Saturation robustness

At least one **non-saturated initialization variant (V1 or V2)** reproduces the C2 ∧ C3 outcome, demonstrating that the result is not an artifact of the saturated-Gaussian V0 initial state.

If only V0 succeeds and V1 / V2 fail, the result is flagged as saturation-dependent.

### Status outcomes

| Outcome | Criteria met | Reported as |
|---|---|---|
| **success** | C1 ∧ C2 ∧ C3 ∧ C4 ∧ C5 ∧ C6 | Layer I H_0 bar-death σ-standard incompleteness for FD-Hessian σ on $T^2_{20}$ |
| **weak_success** | C1 ∧ C2 ∧ C3 ∧ C4, with C5 or C6 failing | Candidate evidence only; threshold or saturation artifact |
| **failed** | C1 fails OR C2 fails OR C3 fails OR C4 fails | Classify per failure modes §11 |

---

## 11. Failure Modes

Documented for honest reporting; each is a *valid scientific outcome*.

### F-C1 — No bar-death event

Neither trajectory exhibits a $K_{\mathrm{bar}}^{\ell_{\min}}$ drop within `max_iter` at any $\ell_{\min}$ in the sweep.
*Adjust:* increase `max_iter`, reduce `snapshot_every`, lower $\ell_{\min}$, change initialization.

### F-C2 — Pre-event σ mismatch

C1 holds, but $\sigma_{\mathrm{standard}}(u_A(t_A^-)) \ne_\tau \sigma_{\mathrm{standard}}(u_B(t_B^-))$.
*Adjust:* relax tolerance (with caveat) or redesign A-I / B-I to share more spectral structure pre-event.

### F-C3 — Post-event σ still equal

C1 ∧ C2 hold, but $\sigma_{\mathrm{standard}}(u_A(t_A^+)) =_\tau \sigma_{\mathrm{standard}}(u_B(t_B^+))$.
*Implication:* the construction does not falsify σ-standard incompleteness. Either redesign with stronger geometric difference, or accept that the projected σ-standard is too coarse and a richer σ implementation is required.

### F-C4 — Threshold artifact

Result holds only at one unstable $\ell_{\min}$.
*Mark as:* weak_success or weak_failure depending on direction.

### F-C5 — Saturation artifact

Result holds only in V0 (saturated_gaussian); V1 (capped_smooth) and V2 (low_mass) do not reproduce.
*Mark as:* weak_success; flag explicitly that the conclusion is conditional on initial-state saturation.

### F-C6 — σ implementation limitation

Pre-event σ matches, post-event σ matches, but other diagnostics ($\mathcal{F}$, dominant bar lengths, regime label, persistence centroid) clearly distinguish A and B.
*Implication:* the projected FD-Hessian σ implementation is insensitive at this scale; the geometry is distinguishable but not by σ-standard. A richer σ implementation or a different invariant is needed.

### F-C7 — Dynamics mismatch

The single-field SCC dynamics (no multi-field repulsion / simplex barrier) does not produce the aggregate-topology transition observed in WQ-2 (where the multi-field flow with Option D-2 + λ_rep + λ_bar drove $K_{\mathrm{bar}}$ : 3 → 1).
*Implication:* WQ-2's aggregate-topology transition was driven by the *multi-field* energy structure (the simplex barrier squashing peaks together); single-field dynamics may have different trajectory topology and may not reproduce it.

---

## 12. JSON Result Schema

Output JSON conforming to:

```json
{
  "protocol_id": "WQ-1.C",
  "protocol_version": "1.0",
  "status": "not_run | weak_success | success | failed",
  "graph": {"type": "torus_grid", "n": 20},
  "state_space": "Sigma_M(G)",
  "parameters": {
    "M": 90,
    "sigma_b": 2.0,
    "u_max": 0.7,
    "dt": 0.001,
    "max_iter": 5000,
    "snapshot_every": 25,
    "tau_lambda": 0.001,
    "ell_min_values": [0.05, 0.10, 0.15, 0.20],
    "ell_min_default": 0.10,
    "n_eig_sigma": 6,
    "n_stab_post": 4,
    "seed": 42,
    "initialization_variants": ["V0_saturated_gaussian", "V1_capped_smooth", "V2_low_mass"]
  },
  "configurations": {
    "A_I": {"name": "equilateral_aggregate", "centers": [[5,5],[15,5],[10,14]]},
    "B_I": {"name": "compressed_aggregate", "centers": [[5,5],[15,5],[10,11]]}
  },
  "runs": {
    "V0_A_I": {<run record>}, "V0_B_I": {...},
    "V1_A_I": {...}, "V1_B_I": {...},
    "V2_A_I": {...} (optional), "V2_B_I": {...} (optional)
  },
  "comparisons": {
    "<l_min>_<variant>": {
      "ell_min": 0.10, "variant": "V0",
      "A_event_time": null, "B_event_time": null,
      "A_K_bar_pre": null, "A_K_bar_post": null,
      "B_K_bar_pre": null, "B_K_bar_post": null,
      "A_sigma_pre": null, "A_sigma_post": null,
      "B_sigma_pre": null, "B_sigma_post": null,
      "C1": null, "C2": null, "C3": null,
      "C2_max_lambda_diff": null, "C3_max_lambda_diff": null,
      "C3_offending_cluster": null
    }
  },
  "criteria_summary": {
    "C1_bar_death_exists": null,
    "C2_same_pre_sigma": null,
    "C3_different_post_sigma": null,
    "C4_same_protocol": true,
    "C5_threshold_robustness": null,
    "C5_threshold_robustness_notes": [],
    "C6_saturation_robustness": null,
    "C6_saturation_robustness_notes": []
  },
  "failure_mode": "F-C1 | F-C2 | F-C3 | F-C4 | F-C5 | F-C6 | F-C7 | null",
  "conclusion": {
    "layerI_h0_sigma_incompleteness": "supported | weak | undetermined | not_supported",
    "multi_formation_OP0008": "not_claimed",
    "sigma_rich_sufficiency": "not_claimed",
    "scope_caveat": "Restricted to projected FD-Hessian σ-standard of scc/sigma_rich.py::_sigma_standard on T^2_20 single-field Layer I; not multi-formation; not a proof of OP-0008.",
    "notes": []
  },
  "metadata": {
    "git_commit": null, "wall_clock_seconds": null,
    "host": null, "python_version": null, "numpy_version": null,
    "scipy_version": null, "scc_module_path": null,
    "run_timestamp_utc": null
  }
}
```

A `<run record>` per trajectory contains snapshot times, $K_{\mathrm{bar}}^{\ell_{\min}}$ trajectory per $\ell_{\min}$, $K_{\mathrm{soft}}^\phi$ trajectory, dominant bar lengths per snapshot, $\mathcal{F}(u(t))$ trajectory, σ-standard at event-bracketing snapshots, event times per $\ell_{\min}$.

---

## 13. Execution Commands

### 13.1 Pre-run

```bash
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 -c "from scc import *; print('scc imports OK')"
```

### 13.2 Primary run

```bash
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 /Users/ojaehong/Perception/Perception_theory/CODE/scripts/wq1c_layerI_h0_bardeath.py \
    --output /Users/ojaehong/Perception/Perception_theory/CODE/scripts/results/wq1c_layerI_h0_bardeath_results.json \
    --max_iter 5000 --seed 42
```

Estimated wall-clock: ~5–15 min (3 variants × 2 trajectories × 5000 iter + ~6 σ-standard FD-Hessian evaluations).

### 13.3 Quick smoke

```bash
PYTHONPATH=/Users/ojaehong/Perception/Perception_theory/CODE \
  python3 /Users/ojaehong/Perception/Perception_theory/CODE/scripts/wq1c_layerI_h0_bardeath.py \
    --output /tmp/wq1c_smoke.json --max_iter 200 --snapshot_every 25 --skip_v2
```

### 13.4 Inspecting results

```bash
python3 -c "
import json
r = json.load(open('CODE/scripts/results/wq1c_layerI_h0_bardeath_results.json'))
print('status:', r['status'])
for k, v in r['criteria_summary'].items():
    print(f'  {k}: {v}')
print('failure_mode:', r['failure_mode'])
print('conclusion:', r['conclusion']['layerI_h0_sigma_incompleteness'])
"
```

---

## 14. Interpretation Rules

### 14.1 If status = success

Record:

> WQ-1.C supports σ-standard incompleteness for the projected FD-Hessian σ implementation on Layer I aggregate $H_0$ bar-death events on $T^2_{20}$ under the constructed conditions. Robustness across $\ell_{\min}$ sweep and saturation variants is documented.

The conclusion is restricted to:

- the projected FD-Hessian σ implementation of `scc/sigma_rich.py::_sigma_standard`;
- the specific graph $T^2_{20}$;
- the constructed A-I / B-I geometric configurations;
- the H_0 superlevel persistence framework;
- *unlabelled* aggregate topology, not labelled $K_{\mathrm{act}}$ jumps.

It does **not** imply OP-0008 resolution.

### 14.2 If status = weak_success

Record:

> WQ-1.C provides candidate evidence; either threshold (F-C4) or saturation (F-C5) robustness fails. Flag explicitly which axis is unstable. Schedule the failed robustness sweep before proceeding to WQ-1.A or WQ-1.B retry paths.

### 14.3 If status = failed

Record per the failure mode (F-C1 through F-C7). Do not retry until the cause is identified. Do not weaken non-claims.

### 14.4 What is *never* concluded

- σ-rich sufficiency.
- OP-0008 resolution.
- σ-standard incompleteness across labelled $K_{\mathrm{act}}$-jumps.
- $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ identification.
- Stratified Morse application.
- Application-domain validation.

---

## 15. Next Steps

| Outcome | Next package |
|---|---|
| `success` | (i) document Layer I result; (ii) update `ksoft_kact_bridge_lemma.md` §13 cross-reference; (iii) consider WQ-1.A (joint projection) as orthogonal Layer II retry; (iv) only after both, revisit σ-rich (WQ-3) |
| `weak_success` | run failed robustness axis; if upgraded to success, proceed as above |
| `failed F-C1` | tune parameters or reframe (e.g. use a different graph that admits clearer bar-death) |
| `failed F-C2` | redesign A-I / B-I with shared per-bump shape but different geometry |
| `failed F-C3` | construction does not falsify σ-standard at this scale; document; consider σ-rich diagnostic on the same configurations |
| `failed F-C6` | σ implementation insufficient; either upgrade FD-Hessian to joint multi-formation Hessian (deferred to future work) or use different invariant |
| `failed F-C7` | single-field dynamics is qualitatively different from multi-field aggregate; document and consider WQ-1.A as the Layer II retry |

Independent of WQ-1.C outcome:
- WQ-2.A (bridge-lemma proof sketch upgrade) remains valuable.
- WQ-2.C (R23 dataset diagnostic) remains valuable.
- WQ-1.A (joint projection) and WQ-1.B (intervention) remain alternative retries.

---

**End of WQ-1.C protocol.**

**Status: working draft, executable specification. Numerical run pending execution; companion artifacts ready: `wq1c_layerI_h0_bardeath_results.md` (placeholder), `CODE/scripts/wq1c_layerI_h0_bardeath.py` (script).**
