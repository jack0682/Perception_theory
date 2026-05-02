# Layered Ambient-State Architecture — README

**File:** `THEORY/working/MF/layered_ambient_architecture_README.md`
**Companion docs:**
- `layered_ambient_architecture_candidate.md` — full memo with definitions, status table, migration notes, non-claims.
- `layered_ambient_architecture_agent_notes.md` — guardrails for future agents.
- `layered_ambient_architecture_next_work.md` — concrete task board.

---

## 1. What this document is

A short human-readable guide to the layered ambient-state architecture for SCC / Multi-Formation. It is a non-canonical working frame: it organizes existing canonical and working content into a layered picture; it does not modify canonical files, does not assign a Commitment number, and does not resolve any open problem.

Read this README first. Then read the candidate memo (`..._candidate.md`) for definitions and status, the agent notes (`..._agent_notes.md`) before doing any new work in this line, and the next-work file (`..._next_work.md`) for the immediate task queue.

---

## 2. Why layered ambient states are needed

Three conflations recurred in the SCC / Multi-Formation working corpus before this architecture:

1. **Architectural choice vs. ontology.** I9 (K-field, fixed per-formation masses) and I9' (shared-pool, variable per-formation masses) were sometimes treated as competing architectures, sometimes as nested submanifolds. Without a layered framing, every claim had to specify "in I9" or "in I9'" by hand.

2. **Count-strata vs. labelled active-set cells.** A K-jump is defined by the integer count $K_{\mathrm{act}}$, but a labelled trajectory carries more information than the count: it carries the active *index set* $A \subseteq \{1, \dots, K_{\mathrm{field}}\}$. Mixing the count picture and the labelled picture caused recurring slips.

3. **Unlabelled topological count vs. labelled active count.** A persistence-based soft count derived from $H_0$ of the aggregate field is conceptually distinct from the labelled threshold-gated active count. Using one in place of the other produces wrong statements in the overlap regime.

The architecture isolates these three issues by giving each layer its own ambient, its own intended use, and its own status grade.

---

## 3. The three layers in one diagram

```text
Layer I: Primitive SCC field
    Σ_m(G_t)
        ↑ aggregate projection U
Layer II: Shared-pool lifecycle ambient
    \widetildeΣ^{K_field}_M(G_t)
        ├─ active masses m_j
        ├─ active count K_act^ε
        ├─ ε-active regions S_A^ε, S_r^ε
        └─ K-jump events
Layer III: Smooth local slices
    Σ_M^A(m_A;G_t)
        └─ fixed-mass theorem layer between K-jumps
```

Read the diagram top-down: Layer I is the *primitive* single-field layer where canonical theorem-grade results live. Layer II is the *global lifecycle* multi-formation ambient that hosts trajectories with varying active count. Layer III is the *smooth local slice* layer where fixed-K, fixed-mass theorems are proved; it sits inside Layer II as an occupancy-constrained submanifold.

The aggregate projection $U : \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t) \to \Sigma_M(G_t)$ is the bridge from Layer II to Layer I. The fixed-mass slice $\Sigma_M^A(\mathbf m_A; G_t) \subseteq \widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ is a submanifold of Layer II.

---

## 4. The three K-notions

| Notion | Symbol | Type | Layer | Labelled? | Threshold? | Role |
|---|---|---|---|---|---|---|
| Architectural cap | $K_{\mathrm{field}}$ | integer | (parameter) | n/a | no | external modeling-layer commitment; bounds active count from above |
| Active count | $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ | integer | II | yes | yes ($\varepsilon$) | labelled threshold-gated count; stratum / region index |
| Soft count | $K_{\mathrm{soft}}^\phi(v)$ | real | I (via $U$) | no | envelope-mediated ($\phi$) | unlabelled topological count from $H_0$ persistence of aggregate field |

These are three different objects. They must not be conflated.

- $K_{\mathrm{field}}$ is set externally before instantiating the theory; it is architectural, not dynamical.
- $K_{\mathrm{act}}^\varepsilon$ is computed from a multi-formation state $\mathbf u$ by counting how many formation slots have mass above threshold $\varepsilon$. It depends on $\varepsilon$ and on the labelling.
- $K_{\mathrm{soft}}^\phi$ is computed from any single field $v$ (typically $v = U(\mathbf u)$) by summing a Lipschitz envelope $\phi$ over the bar lengths of the $H_0$ persistence diagram of the superlevel filtration. It depends on $G_t$, the filtration, $\phi$, and the finite graph resolution. It does not depend on a single object-existence threshold.

Per Commitment 16 (CV-1.5.1), $K_{\mathrm{field}}$ is the architectural cap and $K_{\mathrm{act}}$ is the dynamic stratum index. The soft count $K_{\mathrm{soft}}^\phi$ is added by this memo as a third, complementary object.

---

## 5. What this architecture enables

Working frame for the next research sequence:

- **NQ-242c counterexample protocol** — the K-jump event sits inside Layer II; σ-standard / σ-rich are derived diagnostics on Layer II states; the bridge to aggregate $H_0$ topology is available via $U$ and $K_{\mathrm{soft}}^\phi$.
- **K-soft / K-act bridge lemma** — the well-separated regime is well-defined inside Layer II; the bridge is an approximation statement with explicit hypotheses and error term.
- **σ-rich minimal packet analysis** — the trajectory pairs and their σ-tuples live in Layer II; the analysis is well-posed once σ-standard has been demonstrated insufficient by NQ-242c.
- **K-selection three-model comparison** — the candidate mechanisms (free-energy variational, kinetic metastability, symmetry-broken automorphism-stabilizer) are applied to trajectories on Layer II; predictions are compared to R23 dataset behavior.
- **Stratified ambient feasibility check** — the question "do $\{S_A^\varepsilon\}$ or $\{S_r^\varepsilon\}$ verify Whitney stratification?" is sharply posed at Layer II, separately from the already-verified count-only stratification of the same ambient.

The architecture also gives existing canonical content a clean Layer III reading: the I9 K-field architecture and the T-Persist-K-* family operate on Layer III as smooth-segment, fixed-K, fixed-mass theorems. No canonical edit is required to use this reading.

---

## 6. What this architecture does not claim

- It does not claim $K_{\mathrm{soft}}^\phi$ equals $K_{\mathrm{act}}^\varepsilon$. They live at different ontological layers and may diverge in the overlap and corner-saturated regimes.
- It does not claim K-jump σ-inheritance is deterministic. The non-determinism conjecture (`sigma_multi_trajectory.md` Lemma 4.4.1(c), Cat C) is preserved as conjectured, not asserted, and not refuted.
- It does not claim σ-rich is globally sufficient. σ-rich is a candidate augmentation; its sufficiency is a downstream target.
- It does not claim stratified Morse theory is established machinery for the labelled cell refinement. The Goresky-MacPherson framework is named as the natural future setting; it is not applied as a black-box theorem deliverable.
- It does not claim $\{S_A^\varepsilon\}$ or $\{S_r^\varepsilon\}$ are Whitney strata. The Whitney verification of `mathematical_scaffolding_4tools.md` §2.2 is for the count-only stratification; cell-level Whitney verification is a separate downstream check.
- It does not claim K-Selection (OP-0005) is resolved.
- It does not claim Layer II is globally smooth.
- It does not claim any application-layer validation (vision, robotics, control, neural implementation).
- It does not import gauge theory, full category theory, Geometric Langlands, sheaf cohomology beyond elementary $H_0$ persistence, CBF / CLF, neural operators, Koopman operators, or formal verification.
- It does not silently resolve any open problem; F-1, M-1, MO-1 retain their CV-1.5.1 status; OP-0005, OP-0006, OP-0008, OP-0009 sub-items retain their current canonical status.

For the full enumeration of forbidden non-claims, see `layered_ambient_architecture_candidate.md` §12 and `layered_ambient_architecture_agent_notes.md` §2.

---

## 7. Next recommended work packages

In execution order:

1. **NQ-242c counterexample protocol** — demonstrate σ-standard non-determinism at a K-jump on $T^2_{20}$ (equilateral vs. isoceles configurations); evaluate σ-rich determinism on the same construction. Input: `nq242c_explicit_construction.md`, `sigma_rich_augmentation.md`, `sigma_multi_trajectory.md`, `CODE/scc/multi.py`. Output: `nq242c_results.md` + JSON anchor.

2. **K-soft / K-act bridge lemma** — state and prove (or counter) a lemma comparing $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ and $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ in the well-separated regime, with explicit error term. Input: this memo §6, §9; `mathematical_scaffolding_4tools.md` §4. Output: `k_soft_k_act_bridge_lemma.md`.

3. **σ-rich minimal packet analysis** — given NQ-242c results, identify the minimal augmentation beyond σ-standard achieving deterministic Φ_rich on the constructed example. Input: `sigma_rich_augmentation.md`, `sigma_rich_phi_proof.md`, `sigma_rich_wigner_derivation.md`, NQ-242c JSON. Output: `sigma_rich_minimal_packet.md`.

4. **K-selection three-model comparison** — side-by-side comparison of free-energy variational / kinetic metastability / symmetry-broken automorphism-stabilizer mechanisms on R23 data. Input: `k_selection_mechanism.md`, `k_selection_a_free_energy.md`, `k_selection_b_kramers.md`, `k_selection_c_numerical_anchor.md`, `cn15_static_dynamic_separation.md`. Output: `k_selection_three_model_comparison.md`.

5. **Stratified ambient feasibility check** — verify (or refute) Whitney stratification of $\{S_A^\varepsilon\}$ and $\{S_r^\varepsilon\}$; identify minimal coarsening if cell-level fails. Input: `mathematical_scaffolding_4tools.md` §2; this memo §7. Output: `stratified_ambient_feasibility_check.md`.

For full goal / inputs / outputs / success criterion / forbidden claims of each package, see `layered_ambient_architecture_next_work.md`.

---

**End of README.**

**Reading order for new agents:**

```text
1. layered_ambient_architecture_README.md           (this file — orientation)
2. layered_ambient_architecture_agent_notes.md      (guardrails before any work)
3. layered_ambient_architecture_candidate.md        (full memo with definitions and status)
4. layered_ambient_architecture_next_work.md        (immediate task queue)
```
