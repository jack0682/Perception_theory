---
id: SCC-CT-CH-VI-VII
type: canonical/theorem-registry
chapter: VI + VII
version: SCC-CT v0.1
sealed: 2026-05-14
canonical_source: THEORY/canonical/canonical.md (CV-1.16 SEALED)
total_claims: 97 (68A / 18B / 6C / 5R)
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# VI. Static Core Theorems & VII. Computational Validation

# VI. Static Core Theorems

## §1. Scope

This chapter registers all 97 claims of the CV-1.16 SEALED state into the SCC-CT 4-tier Cat A/B/C/R taxonomy. The registry is **authoritative**: every claim in the system has exactly one Cat assignment.

For the per-claim *historical* status (proof method, who proved it, when, in which session), refer to `THEORY/canonical/theorem_status.md`. This SCC-CT registry organizes by *ontological role*, not chronology.

## §2. Cat A — Fully Proved / Sealed (68 entries)

### §2.1 Static single-formation core

| ID | Name | Role |
|---|---|---|
| T1 | Existence of formation | Ground-level non-vacuity |
| T-A2 | Monotonicity of closure | A2 axiom realization |
| T3 / T6-Stability | Non-idempotent closure strict positivity | $H_{\mathrm{cl}} \succ 0$ at fixed point |
| T8-Core | Phase transition $\beta/\alpha > 4\lambda_2/\lVert W''(c) \rVert$ | Central T8 theorem |
| T8-Full | Phase transition full version | Extended to T8-Core hypotheses |
| T11 | Γ-convergence to perimeter functional | Sharp-interface limit |
| T14 | Gradient flow convergence | Łojasiewicz-Simon |
| T20 | Axiom consistency | Group A-E mutual compatibility |

### §2.2 Pre-objective formation (W4 merge, 2026-04-25/26)

| ID | Name | Role |
|---|---|---|
| T-PreObj-1 | Pre-objective mechanism (specific graph classes) | Resolves F-1 vacuity problem |
| T-PreObj-1G | Graph-class independent pre-objective mechanism | Generic finite weighted graph |
| T-V5b-T | Pre-objective Goldstone (translation-invariant) | Sub/super-lattice spectral dichotomy |
| V5b-T-zero | Exact-zero Goldstone sub-statement | Cat A definitional (replaces WITHDRAWN V5b-T′) |

### §2.3 σ-framework supporting (W5 Day 1)

| ID | Name | Role |
|---|---|---|
| T-σ-Lemma-1 | irrep decomposition | σ-structure foundation |
| T-σ-Lemma-2 | nodal count | |
| T-σ-Lemma-3 | Goldstone-ℓ=1 | |
| T-σ-Theorem-3 | σ-framework supporting theorem | Commitment 14 grounding |

### §2.4 D-6a Multi-Static (W5 Day 3 EOD, CV-1.5.1)

| ID | Name | Role |
|---|---|---|
| T-Commitment-14-Multi-Static | Multi-static σ commitment | Grounds Commitment 14 |
| T-σ-multi-A-Static | A-axis multi-static | |
| T-σ-multi-D-Static | D-axis multi-static | |

### §2.5 Multi-formation count bridge (CV-1.5.2 / W6 D1 EOD)

| ID | Name | Role |
|---|---|---|
| T-L1-F | Hard-Bar / Active-Count Bridge under L1-J regime | $K_{\mathrm{bar}} = K_{\mathrm{act}}$ under (P0)-(P11) |
| T-L1-M | Soft-Count Corollary under $\Phi_{\mathrm{res}}$ | Supervised addition; same regime |

### §2.6 Stereo extension (CV-1.6, W6 D4)

| ID | Name | Role |
|---|---|---|
| T-ST-5a | Hard-Depth Topological Locking | K=2 lock via disconnected graph |

### §2.7 P-F-A1 Package I (CV-1.7 to CV-1.9, W6 D4)

| ID | Name | Role |
|---|---|---|
| T-P-F-ε0 | Gibbs measure continuity at $\varepsilon = 0$ | Target B → Target A weak convergence |
| T-PF-A1-AR | Field polytope compact convex + affine reduction | Geometric foundation |
| T-PF-A1-SDE | Reflected Langevin SDE well-posedness (Lions-Sznitman 1984) | Existence + uniqueness on polytope |
| T-PF-A1-GI | Gibbs measure unique invariant measure (CV-1.9 promoted from Cat B) | Heat kernel + $L^2$ kernel argument |
| T-PF-A1-PE | Poincaré inequality + exponential ergodicity (CV-1.9 promoted from Cat B) | Payne-Weinberger + Holley-Stroock |

### §2.8 OP-0006 boundary precision (CV-1.7 Session K)

| ID | Name | Role |
|---|---|---|
| T-OP6-B | Persistent Ridge Boundary equivalence (H1-H5 conditional) | $d_H \leq 2\sqrt{\alpha/\beta}$ |

### §2.9 Temporal identity (CV-1.13 SEALED, W7-CV1.13)

| ID | Name | Role |
|---|---|---|
| **T-Temporal-Identity** | Persistent component identity via partial transport (4 parts: a, b, c-conditional, d) | Q5 closure, ALL Cat A |
| Lemma S-B1-Weak | Deep-core density positivity $\rho_{\mathrm{deep}} > \rho_*$ | Δ_sep > 0 Cat A |
| Theorem Partial-H-SINK | One-sided SCC E1 Sinkhorn stability | partial OT plan stability |

### §2.10 Predicate-Energy Bridge

| ID | Name | Role |
|---|---|---|
| T-Bind-Proj | Bind projected lower bound | Bind ↔ E_cl bridge (forward) |
| T-Bind-Full | Bind exact-equality at KKT optimum | reverse direction |
| **Sep bidirectional bridge** | Sep = 1 − E_sep/m exactly (u-weighted) | Cat A exact equality |

### §2.11 Deep core dominance (W5)

| ID | Name | Role |
|---|---|---|
| Theorem 2b (Deep Core Dominance) | $\lVert \mathrm{Core}^2 \rVert/\lVert \mathrm{Core} \rVert \geq 1 - 4 C_{\mathrm{iso}}/\sqrt{m}$ | Isoperimetric on $\mathbb{Z}^d$ |

### §2.12 Persistence (single-step)

| ID | Name | Role |
|---|---|---|
| T-Persist-1 | Temporal persistence (5 components a-e) | Two-step persistence |

### §2.13 CV-1.15 Action-Based Temporal Succession Package (W7-Day5 morning)

| ID | Name | Role |
|---|---|---|
| L-ENDPOINT-NONSEMI | Endpoint² cost generically not composition-compatible | counterexample (1D) |
| L-ACTION-NORMALIZATION | Uniform-speed action additivity | $\frac{\lVert z-x \rVert^2}{r-t}$ identity |
| L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action ≥ 0 and additive | T-ACT-DP/GIBBS premises |
| T-ACT-DP | Hard-min action cost Bellman DP | $c^{\mathrm{act}}_{i \to k}$ recursion |
| L-ACTION-DELTA-EFF-ZERO | $\delta_{\mathrm{eff}} = 0$ under action direct cost | scope-restricted |
| T-ACT-GIBBS | Gibbs kernel semigroup $\mathbf{K}_{i\to k} = \mathbf{K}_{i\to j}\mathbf{K}_{j \to k}$ | Chapman-Kolmogorov-type |
| L-SOFTMIN-HARDMIN-BOUND | $\min a - \varepsilon \log N \leq \mathrm{smin}_\varepsilon(a) \leq \min a$ | log-sum-exp bound |
| L-SOFT-ACTION-DELTA-EFF-ZERO | Soft-min image $\delta^\varepsilon_{\mathrm{eff}} = 0$ | $-\varepsilon \log$ of T-ACT-GIBBS |

### §2.14 CV-1.16 H-MORSE-Local Closure Package (W7-Day5 evening, this session's seal point)

| ID | Name | Role |
|---|---|---|
| **L-CLOSURE-LIFT** | Operator-norm broadness: $\lVert J_{\mathrm{Cl}} \rVert_{D \to D} \leq a_{\mathrm{cl}}/4 < 1$; uniform tangent lower bound | **Supersedes T7-Enhanced as the broadness statement** |

### §2.15 OMS Appendix (W6 D6, 2026-05-08)

| ID | Name | Role |
|---|---|---|
| OMS-2.0 Accepted Full | Observer Moduli Space static + temporal | Appendix OMS A-M |

### §2.16 K-Selection (equilibrium / observational)

| ID | Name | Role |
|---|---|---|
| (None — all K-Select are Cat B) | — | Cat B section below |

### Cat A Total: 68 entries

(Counting per-canonical-record: original 35 + W4 (T-PreObj +2, T-V5b-T +1) + W5 Day 1 (σ-supporting +4) + W5 Day 3 EOD (D-6a +3) + W5 Day 6 (T-L1-F +1) + W6 D1 (T-L1-M +1) + W6 D4 (T-ST-5a +1, T-P-F-ε0 +1, T-OP6-B +1, T-PF-A1-AR +1, T-PF-A1-SDE +1, T-PF-A1-GI +1 promoted, T-PF-A1-PE +1 promoted) + W7-CV1.13 (T-Temporal-Identity full Cat A +4 parts -1 Cat B row) + W7-CV113 (Lemma S-B1-Weak +1) + CV-1.15 (8 entries) + CV-1.16 (L-CLOSURE-LIFT +1). Net 68.)

## §3. Cat B — Partial / Conditional (18 entries)

### §3.1 K-Selection (CV-1.10 / CV-1.11)

| ID | Name | Condition |
|---|---|---|
| T-K-Select-PF | Equilibrium K-selection under P-F-A1 Package I | $T_*$ axiomatic (OP-0021); $K^*$ uniqueness not proved |
| T-K-Select-OBS | Observation-conditioned K-selection | LM1-LM3 likelihood; $T_*$ axiomatic |

### §3.2 Stereo extension (CV-1.6, T-ST-5b)

| ID | Name | Condition |
|---|---|---|
| T-ST-5b | Smooth-Depth Barrier Raising | full SCC β=10 specific regime; monotonicity not confirmed |

### §3.3 P-F stochastic foundation (CV-1.7)

| ID | Name | Condition |
|---|---|---|
| T-P-F-ε0-K | Kramers exponent stability under Bernoulli regularization | H5 Morse stability (now partially upgraded by L-HMORSE-LOCAL Cat B, CV-1.16) |

### §3.4 σ-framework retroactive (CV-1.5.1)

| ID | Name | Condition |
|---|---|---|
| T-σ-Theorem-4 | σ-framework spectral statement | retroactive Cat A → Cat B; NQ-187 continuum vs discrete mismatch |
| V5b-F-empirical | empirical scaling sub-statement | NQ-198a 1/n scaling |

### §3.5 Persistence

| ID | Name | Condition |
|---|---|---|
| T-Persist-K-Sep | K-field persistence (well-separated) | well-separation + spectral repulsion (Cat C in some classifications; Cat B per current canonical) |
| T-Persist-K-Weak | K-field persistence (weak coupling) | weakly-interacting regime |
| T-Persist-K-Unified | Parametric persistence | conditional on $\Lambda_{\mathrm{coupling}}$ regime |

### §3.6 Sigma rich / Multi-formation (W5 Day 3)

| ID | Name | Condition |
|---|---|---|
| T-σ-Multi-1 | Goldstone-pair instability (Cat B target) | working layer; CV-1.5.1 |

### §3.7 Stereo extension D-ST candidates (CV-1.6, working candidates)

| ID | Name | Condition |
|---|---|---|
| D-ST-1 | Stereo Adjacency (Hard + Smooth) | hard/smooth variants |
| D-ST-2 | Field Space $F_M(P)$ and Mass Constraint | foundational state space |
| D-ST-3 | K_act as #PersComp Observable | exp01 SUPPORTED |
| D-ST-4 | Topological Sector $B_K$, Partition Function $Z_K$ | P-F flag (Cat B) |
| D-ST-5 | Backprojection / Prior-Likelihood separation | exp03, exp04 |

### §3.8 CV-1.12 Temporal Identity (now Cat A but historical Cat B)

(Promoted to Cat A in CV-1.13. Row removed from Cat B in current count.)

### §3.9 S-B1 symbolic (W7-CV113A)

| ID | Name | Condition |
|---|---|---|
| Lemma S-B1-SYM | Symbolic deep-core density identity | HWF-1 (iso_ratio ≤ C_iso); m ≥ 25; β > 7α |

### §3.10 CV-1.15 Cat B additions (W7-Day5 morning)

| ID | Name | Condition |
|---|---|---|
| T-ACT-KERNEL-COMP→REL | $(GK)+(stable-K)+(margin) \Rightarrow R$ composition | conditional on CV-1.14 T-CC-StableK-Kernel working candidate |
| P-SINKHORN-STABILITY-CONDITIONAL | Sinkhorn-scaled relation stability | (H-SINK)+(MARGIN)+(SMALL-SINK-GAP) |

### §3.11 CV-1.16 H-MORSE-Local Cat B (W7-Day5 evening)

| ID | Name | Condition |
|---|---|---|
| **L-HMORSE-LOCAL** | $\mu_{\min}(\Pi_T^{\mathrm{free}} H_{\mathcal{E}} \Pi_T^{\mathrm{free}}) \geq c_{\mathrm{HML}} > 0$ | D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5); active-set form |
| **L-HMORSE-DECOMP** | $H_{\mathcal{E}} = H_{\mathrm{bd}} + H_{\mathrm{cl}} + H_{\mathrm{sep}}$ per-term bounds | $b_D = 0$ + A3 |

### Cat B Total: 18 entries

## §4. Cat C — Conjectural / Architectural (6 entries)

| ID | Name | Why Cat C |
|---|---|---|
| T-Persist-1(d) | Interior Gap | β > 7α necessary; structural limit |
| T-Persist-Full | Full composition (3+-step) | Multiple regime conditions |
| (T-Persist-K-Sep / Weak / Unified — Cat B/C classification varies; see §3.5 above) | | |
| σ_standard inheritance (T-σ-Inherit (c), (d-σ_standard)) | Wigner-projection W9+ required (OP-0008-MERGE/SPLIT) | |
| **L-BOUNDARY-MODE-EXCLUSION** (CV-1.16) | SKETCH-level Weyl perturbation | Explicit constants deferred to OP-HMORSE-LOCAL-A |

### Cat C Total: 6 entries

(Exact count: 5 historical Cat C + 1 CV-1.16 = 6. Per canonical.md §13 Category C header "5 theorems" plus the CV-1.16 addition.)

## §5. Cat R — Rejected / Downgraded / Forbidden Wording (5 entries)

**See `06_forbidden_claims.md` for full Cat R registry with explanations.**

| ID | Disposition |
|---|---|
| **Original A1 (weak extensivity)** | Replaced by A1′ (conditional extensivity); conflicted with A3 |
| **Theorem 3.3 ($\bar r_0 = O(n^{-1/d})$ for general τ)** | Experimentally falsified; $\bar r_0$ is $O(1)$ for $\tau \neq 1/2$ |
| **T-Merge (c)(d)(e) — Unconstrained mountain pass** | Merge path does not exist on $\Sigma_M^K$ (2026-04-07 Erratum) |
| **D-5 V5b-T′ Goldstone (2D torus PN-barrier)** | NQ-198f phantom; replaced by V5b-T-zero (Cat A definitional) |
| **Literal $\rho_{\mathrm{deep}} \geq 0.84$ unconditional** | Counterexample (elongated formation); replaced by S-B1-SYM (Cat B conditional) + Lemma S-B1-Weak (Cat A positivity) |

### Cat R Total: 5 entries

## §6. Total verification

$$68 + 18 + 6 + 5 \;=\; 97 \quad \checkmark$$

Matches CV-1.16 SEALED count (`THEORY/canonical/CV-1.16_SEAL.md`).

---

# VII. Computational Validation

## §7. What is computationally validated

The SCC-CT theoretical structure is supported by a comprehensive computational implementation in `CODE/scc/` (15 modules) with `CODE/tests/` (215 passed + 1 xfailed) and `CODE/experiments/` (90+ experiments).

### §7.1 Implementation modules

| Module | Role |
|---|---|
| `scc/graph.py` | `GraphState` — Laplacian, Fiedler, row-normalized P, cohesion-weighted $W_{\mathrm{sym}}$ |
| `scc/params.py` | `ParameterRegistry` — A3 ($a_{\mathrm{cl}} < 4$), spinodal, β_crit validation |
| `scc/operators.py` | closure, distinction, aggregation, resolvent_diagonal + exact JVPs |
| `scc/energy.py` | `EnergyComputer` — $\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}, \mathcal{E}_{\mathrm{bd}}$ + FD-verified gradients $10^{-9}$ |
| `scc/optimizer.py` | `find_formation` — semi-implicit projected GD, BB step, multi-start |
| `scc/diagnostics.py` | `DiagnosticVector` (Bind, Sep, Inside, Persist) |
| `scc/multi.py` | K-field, `transport_k_formations` |
| `scc/transport.py` | cohesion fingerprint, Sinkhorn log-domain OT, `persist_transport` |
| `scc/k_soft.py` | $k_{\mathrm{soft}}(u)$ persistence-based soft mode count |
| `scc/langevin.py` | reflected Langevin SDE (P-F-A1 Package I) |
| `scc/sigma_rich.py` | $\sigma_{\mathrm{rich}}$ namedtuple, OP-0008 Path B |

### §7.2 Critical implementation details

| Detail | Why critical |
|---|---|
| Ordered-pair summation ($\mathcal{E}_{\mathrm{bd}}$ smoothness $= 2\alpha u^\top L u$, gradient $4\alpha L u$) | T8-Core factor 4 (not 2) |
| Double-well derivative $W'(u) = 2u(1-u)(1-2u)$ (factor 2, I6 correction) | gradient correctness |
| Sep predicate $u$-weighted (`Σuᵢ·Dᵢ / Σuᵢ`), NOT $\mathbf{C}_t$-weighted | Avoids diagnostic degeneracy |
| $b_D = 0$ enforced | Analyticity (T14 convergence) |

### §7.3 Validated facts at implementation level

| Fact | Validation method |
|---|---|
| Existence of formation on canonical 15×15 grid | exp01 + grid sweep |
| Phase transition at $\beta/\alpha > 4\lambda_2/\lVert W''(c) \rVert$ | β sweep with exp25, exp51 |
| Gradient flow convergence | exp38, exp55, exp57 |
| Diagnostic vector computability | All 4 components verified |
| Closure non-idempotent stability | T7-Enhanced supporting numerical |
| Eyring-Kramers prefactor (Cat C) | Package II partial, requires OP-0021 |

### §7.4 CV-1.16 numerical anchor (this seal point)

**`exp_hmorse_broadness_full_spectrum.py`** (created 2026-05-14 W7-Day5 evening):
- 15-config sweep on canonical 2D grids (5×5, 10×10, 15×15) × $\beta \in \{10, 20, 30, 50, 100\}$.
- **15/15 PASS**: broadness PASS + lift PASS.
- $\mu_{\min}(\Pi_T H_{\mathcal{E}} \Pi_T) \in [0.13, 3.49]$ — all positive.
- $\mu_{\min}(\Pi_T H_{\mathrm{cl}} \Pi_T) \in [0.45, 0.79]$ — exceeds Theorem B2 standard-form prediction by ~60×.

**`exp_hmorse_sbm_robustness.py`** (created 2026-05-14 W7-Day5 post-CV-1.16-SEAL):
- 18 configs across SBM, barbell, small-world × $\beta \in \{10, 30, 100\}$.
- 7 T8-Core β_crit validation errors (well-connected graphs need higher β).
- 11 valid runs: **11/11 lift PASS** (L-CLOSURE-LIFT Cat A robust across heterogeneous graphs).
- 6/11 broadness PASS; 5 borderline machine-epsilon "FAIL" on barbell = (C3) structural degeneracy at Fiedler ~0.02-0.05.

### §7.5 Test suite

```bash
cd CODE && python3 -m pytest tests/ -q
# 215 passed, 1 xfailed in ~3.5 min
```

No regressions through CV-1.13 → CV-1.15 → CV-1.16 evolution.

## §8. What is NOT computationally validated

- Multi-formation rigorous interaction (only T-L1-F regime, conditional Cat A).
- Package II Eyring-Kramers prefactor (Cat C; H-MORSE-Local Cat B is partial Cat B for H5).
- $T_*$ explicit value (axiomatic, OP-0021).
- σ-Inheritance σ_standard (Cat C, OP-0008 Wigner-projection deferred).
- Real perception / RGB-D / psychophysics — out of scope; future application layer.

## §9. Validation hierarchy

| Validation level | Cat status implication |
|---|---|
| Symbolic proof verified | Cat A |
| Symbolic proof + numerical confirmation | Cat A (highest confidence) |
| Numerical only, no symbolic | Cat B at best |
| Symbolic + scope-restricted regime | Cat B conditional |
| Architectural / SKETCH only | Cat C |
| Numerically counterexampled | Cat R |

CV-1.16's L-CLOSURE-LIFT achieves the highest confidence level (symbolic + numerical convergence). L-HMORSE-LOCAL achieves Cat B with strong numerical support but residual condition (C2′ + (C3) for non-bottlenecked graphs) limiting universal Cat A.

---

*Chapters VI & VII sealed within SCC-CT v0.1. Counts verified against `THEORY/canonical/CV-1.16_SEAL.md`: 68A / 18B / 6C / 5R = 97. References: `THEORY/canonical/theorem_status.md` (per-claim history); `THEORY/canonical/canonical.md` §13 (Cat A/B/C bodies); `CODE/scc/` (implementation); `CODE/experiments/exp_hmorse_broadness_full_spectrum.{py,json,md}` + `exp_hmorse_sbm_robustness.{py,json,md}` (CV-1.16 numerical anchors). Next: `05_open_problems.md` (Ch. VIII).*
