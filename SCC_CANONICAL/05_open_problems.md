---
id: SCC-CT-CH-VIII
type: canonical/open-problems
chapter: VIII
version: SCC-CT v0.1
sealed: 2026-05-14
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# VIII. Open Problems

## §1. Scope and discipline

This chapter registers all genuinely open problems in SCC-CT, organized by ontological role rather than ID number. Per the manifest forbidden-wording list (`06_forbidden_claims.md`), no open problem here may be casually claimed as "essentially resolved" or "partial proof exists" — each must carry an honest status label:

| Label | Meaning |
|---|---|
| **OPEN** | No proof attempt has produced a viable strategy. |
| **PARTIALLY STRUCTURED** | A proof strategy exists; some structural lemmas proved; full proof not yet assembled. |
| **PARTIALLY RESOLVED** | A *sub-problem* is closed; remainder remains. |
| **CLOSED Cat X** | Resolved at Cat X level; included here for historical traceability only. |

## §2. Open by ontological domain

### §2.1 Temporal persistence (Q5 closure refinement)

**T-Temporal-Identity is Cat A (CV-1.13 SEALED, all 4 parts).** What remains:

#### OP-0012: Persistence Composition (PARTIALLY STRUCTURED, refined CV-1.15)
- **OP-0012-CC** (Cat B path): under stable-K + margin, $R_{t \to r} = R_{s \to r} \circ R_{t \to s}$. Cat B via Lemma 6 (W6 D5).
- **OP-0012-SINK** (NEW SUB-LABEL, CV-1.15 OPEN): Sinkhorn temporal scaling compatibility. Cost-level $\delta_{\mathrm{eff}}$ blocker closed under action redefinition (L-ACTION-DELTA-EFF-ZERO Cat A). Plan-level scaling-gap blocker OPEN. Required: L-δ_eff-SINK (Cat C target), L-Eff-Sinkhorn (Cat C target).
- **OP-0012-Kjump** (Cat C): K-jump general case. Depends on OP-0008 + OP-0021.
- **OP-0012-Markov** (deferred): probabilistic / Markov-kernel formulation.

**Status:** Single-formation 3+-step composition is OPEN under stable-K. Multi-formation is OPEN.

#### OP-0011: Transport Kernel Uniqueness (PARTIALLY RESOLVED, CV-1.12)
- Resolved at the level of Sinkhorn-based partial OT plans (Lemma 10 / S-B3 Cat A).
- Remaining: do *other* admissible E1-E4 transport kernels coincide with the canonical Sinkhorn realization?

#### OP-HMORSE-FIEDLER-BOUND (NEW 2026-05-14, MEDIUM)
- Quantitative $\lambda_2^{\min}(\beta, n, c)$ such that (C3) single-formation holds on graphs with Fiedler $\geq \lambda_2^{\min}$.
- ETA 1-2 sessions. Builds on `exp_hmorse_sbm_robustness.py` infrastructure.
- *Source:* `THEORY/logs/daily/2026-05-14/50_hmorse_sbm_results.md §5`.

### §2.2 Self-referential Optimal Transport

#### Self-referential OT uniqueness / fixed point (PARTIALLY RESOLVED)

- **Fixed point existence:** Schauder, any $\varepsilon_{\mathrm{OT}} > 0$. (Cat A historical.)
- **Confinement bound:** $C_{\mathrm{conf}} = O(\sigma \sqrt{\varepsilon_{\mathrm{OT}} \log n})$ proved, independent of $u_s$. (Cat A.)
- **H-SINK (Sinkhorn-Lipschitz stability):** FULLY CLOSED Cat A (W7-FINAL, 2026-05-10). One-sided partial OT case via Theorem Partial-H-SINK.
- **Remaining:** Tight confinement constants (current bound 25-10000× conservative, exp40/41). True self-referential uniqueness (cost depending on $u_t, u_s$ AND $u_t, u_s$ depending on cost) — fixed-point existence does NOT imply uniqueness.

### §2.3 Multi-formation rigorous theory

#### OP-0009: Multi-formation Ontological Foundations (PARTIALLY RESOLVED, 1/7 closed)

Seven ontological sub-problems registered W5 Day 3 EOD:
- (OP-0009-pre-A) K-field chart validity — PARTIALLY STRUCTURED.
- (OP-0009-V) Field-space $F_M(P)$ vs slot-based $\Sigma_M^K$ unification — PARTIALLY STRUCTURED (D-ST-2 helps).
- (OP-0009-λ_rep) $\lambda_{\mathrm{rep}}$ ontology — PARTIALLY STRUCTURED.
- (OP-0009-C_t-multi) Co-belonging on multi-formation — OPEN.
- (OP-0009-merger) Merger ontology — partially via OP-0008-MERGE structure.
- (OP-0009-split) Split ontology — partially via OP-0008-SPLIT structure.
- (OP-0009-K-field/shared-pool) Architecture unification — OPEN.

T-L1-F (Cat A conditional) closes the *count bridge* under (P0)-(P11) regime. Does NOT solve OP-0009 ontology.

#### OP-0005: K-Selection (3-way split, PARTIALLY RESOLVED)
- **OP-0005-EQ** (equilibrium): partially resolved by T-K-Select-PF Cat B (CV-1.10).
- **OP-0005-OBS** (observation-conditioned): partially resolved by T-K-Select-OBS Cat B (CV-1.11).
- **OP-0005-DYN** (dynamic Kramers rates): **OPEN.** Requires Package II + H-MORSE-Local + OP-0021. Major missing piece.

#### OP-0008: σ-Inheritance (PARTIALLY STRUCTURED, 4 sub-problems)
- **OP-0008-CONT** (continuation): PARTIALLY STRUCTURED.
- **OP-0008-MERGE** (K-jump merge): centroid + orientation Cat B (mass-weighted average; parallel-axis theorem); σ_standard **Cat C** (Wigner-projection W9+ required).
- **OP-0008-SPLIT** (K-jump split): direction Cat B (Goldstone $v_1$); σ_standard **Cat C**.
- **OP-0008-DIST** (perturbation stability): CLOSED Cat B (Lemma 16, 2026-05-07).

Major OPEN piece: σ_standard inheritance via Wigner-projection.

### §2.4 Energy and dynamics

#### Sep energy scale relevance (OPEN)

- The relative importance of $\mathcal{E}_{\mathrm{sep}}$ in the four-term sum is **conceptually** independent (CN5) but the **quantitative** scale at which Sep dominates is not analytically determined.
- Numerical evidence: full SCC vs BD-only show different attraction basin geometries (exp57), but the *threshold* at which Sep contribution becomes dominant has not been characterized.
- Required: R10 separation-dominance regime determination.

#### Full-energy phase transition (OPEN)

- T8-Core / T8-Full give phase transition for $\mathcal{E}_{\mathrm{bd}}$ alone.
- The corresponding phase-transition condition for the *full* four-term energy (with closure correction + separation) is not closed-form derived.
- Numerical: closure shifts the transition (T7-Enhanced; CN14 stability expansion). Exact analytical form OPEN.

#### Parameter regime theory (OPEN)

- Canonical parameters ($a_{\mathrm{cl}} = 3.5$, $\beta = 30$, $c = 0.3$, $\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}} = 1.0$, etc.) work in tested grids.
- The *regime boundaries* — which parameter combinations break which Cat A theorem — are not systematically characterized.
- Required: regime classifier for each Cat A theorem's applicability domain.

### §2.5 Morse-stability follow-ups (CV-1.16 derivatives)

#### OP-HMORSE-LOCAL-A (Cat A path for L-HMORSE-LOCAL, MEDIUM-HIGH severity)
- Requires: (a) sharper residual-correction bound using $|\sigma''(z(u^*))| \to 0$ at saturated nodes; (b) OP-HMORSE-SBM robustness extension; (c) (C2′) → strict-interior (C2) generalization OR generic-Morse (γ).
- ETA: 2 sessions.

#### OP-HMORSE-SBM (PARTIALLY RESOLVED 2026-05-14)
- `exp_hmorse_sbm_robustness.py` confirms L-CLOSURE-LIFT Cat A robustness 11/11 valid runs.
- L-HMORSE-LOCAL Cat B robust on SBM + small-world; barbell shows (C3)-violation analyzed as OP-HMORSE-FIEDLER-BOUND.
- Remaining: numerical confirmation across SBM with varying $p_{\mathrm{intra}}/p_{\mathrm{inter}}$ ratios.

#### OP-HMORSE-SADDLE (MEDIUM severity)
- Saddle-point Hessian regularity required for full Eyring-Kramers prefactor Cat B.
- Independent of minimum-Hessian L-HMORSE-LOCAL.
- ETA: 2-4 sessions.

#### OP-HMORSE-GENERIC-PATH (MEDIUM)
- Alternative Cat A path via Smale-Sard transversality + Allen-Cahn Morse transition (Bates-Fife-Wang 1997; Fei-Wang-Zhou 2019).
- Generic-measure-theoretic Cat A, not pointwise.
- Lower priority since L-CLOSURE-LIFT direct (Approach b) is Cat A already.

#### OP-HMORSE-ACTIVE-SET-EXTENSION (NEW 2026-05-14, LOW-MEDIUM)
- Extend (C2′) active set to include near-zero eigenmodes (e.g., Fiedler-direction bottleneck modes).
- Allows L-HMORSE-LOCAL to apply to near-disconnected graphs.

#### OP-HMORSE-EXCLUSION-VOLUME (LOW, downgraded)
- Operationally resolved: $\Pi_T = I - (1/n)\mathbf{1}\mathbf{1}^\top$ produces exactly one ~0 eigenvalue numerically.

### §2.6 Package II and stochastic dynamics

#### OP-0021: T_* registration (MAJOR OPEN, Phase 2)

- **Status:** OPEN. T_* is currently axiomatic in canonical SCC (not derived).
- **Route A — Mori-Zwanzig (NOP-F):** memory kernel decay → effective temperature. 5 identified gaps, sketch-level.
- **Route B — RG fixed point (NOP-J):** $T_*^{\mathrm{Fisher}} = T_*^{\mathrm{RG}}$ equivalence sketched.
- **Naming inconsistency** (carried from CV-1.15 SEAL): `theorem_status.md` line ~837 has separate OP-0021 "Stochastic Dynamics" entry. Reconciliation deferred to CV-1.17+.

#### Package II Eyring-Kramers (MAJOR OPEN)

- **Prerequisite chain:** H-MORSE-Local Cat B ✓ (CV-1.16) → H-MORSE-Saddle (OP-HMORSE-SADDLE) → OP-0021 $T_*$ → full prefactor.
- **CV-1.17 target.** Cat B prefactor formula combining L-HMORSE-LOCAL + OP-HMORSE-SADDLE + $T_*$.

### §2.7 Other open items

#### OP-0013: Closure Operator Convergence Rate (UNDER INVESTIGATION)
- T6 proves closure has fixed point with contraction; exact rate as function of parameters unknown.
- Low practical impact.

#### OP-0020: Dynamic Topology (Out of Scope)
- $X_t$ changing over time. Currently assumed fixed.

#### OP-0022: Continuous-Time Limit (UNDER INVESTIGATION)
- Discrete graph → continuous limit. Sub-aspect: continuous-time *action* limit (CV-1.15 candidate, deferred CV-1.16+).

#### OP-SB1-084: Tightest analytic $C_{\mathrm{iso}}$ (LOW)
- On canonical 15×15 SCC minimizers, determine smallest provable $C_{\mathrm{iso}}$ such that $\rho_{\mathrm{sym}}(C_{\mathrm{iso}}, 25, 1.0) = 0.84$.
- Non-blocking; quantitative refinement only.

## §3. Open problems by priority (CV-1.17 onward)

| Priority | OP | ETA | Why |
|---|---|---|---|
| Highest | **Package II Eyring-Kramers Cat B** | 3-5 sessions | Q3 closure path; uses L-HMORSE-LOCAL |
| High | **OP-HMORSE-LOCAL-A** Cat A path | 2 sessions | Upgrades L-HMORSE-LOCAL Cat B → Cat A |
| High | **OP-0021** $T_*$ registration | ? sessions | Independent track, parallel to H-MORSE |
| Medium | **OP-HMORSE-FIEDLER-BOUND** | 1-2 sessions | Refines D-HMORSE-LOCAL applicability |
| Medium | **OP-0008-MERGE-σ** Wigner-projection | 3+ sessions | Q6 closure path |
| Medium | **OP-HMORSE-SADDLE** | 2-4 sessions | Eyring-Kramers second factor |
| Medium | **OP-0012-SINK lemmas** | 2-4 sessions | CV-1.15 follow-up |
| Low | **§F Step 2 housekeeping** | 0.5 session | CV-1.15 working file rewrite |
| Low | **OP-0021 dual-naming reconciliation** | 0.5 session | Hygiene |
| Low | **OP-HMORSE-ACTIVE-SET-EXTENSION** | 1 session | Refines (C2′) |
| Low | **OP-HMORSE-EXCLUSION-VOLUME** | (resolved) | downgrade marker |

## §4. The DECL-1.0 Q1-Q6 closure status

Per `THEORY/canonical/DECLARATION.md` DECL-1.0, the central question set:

| Q | Question | Status at SCC-CT v0.1 |
|---|---|---|
| Q1 | When does boundary emerge? | T8 phase transition — **Cat A mostly** |
| Q2 | Can multiple formations coexist? | Multi-formation count bridge — Cat A conditional (T-L1-F); ontology — PARTIALLY RESOLVED |
| Q3 | How does it change? | Package I — **Cat A complete**; Package II — OPEN (now partially enabled by L-HMORSE-LOCAL Cat B) |
| Q4 | How many stabilize? | T-K-Select-EQ/OBS — Cat B; DYN — OPEN (Kramers rates, OP-0005-DYN) |
| Q5 | Same across time? | T-Temporal-Identity — **Cat A** (CV-1.13 SEALED, all 4 parts) |
| Q6 | After split / merge? | σ-Inheritance — Cat B (centroid+orientation), Cat C (σ_standard); OP-0008 OPEN |

**Two major OPEN: Q3-DYN (Kramers) and Q6-σ_standard (Wigner-projection).**

## §5. What is *not* registered as OPEN

The following are out of scope of SCC-CT v0.1 OPEN registry — they are *categorically outside* the theory's commitments:

- Object detection / classification accuracy (post-formation; outside SCC scope).
- Specific perceptual phenomena (apparent motion, illusions) — predictions, not theory questions.
- Application-specific optimization (parameter tuning for specific datasets).
- Comparison to specific competing frameworks (Bayesian, predictive processing, etc.) — these are research-program questions, not theory-internal OPEN problems.

---

*Chapter VIII sealed within SCC-CT v0.1. References: `THEORY/canonical/theorem_status.md §Open Problems Catalog`; `THEORY/canonical/hypothesis_tree.md §가설 상태 요약`; `THEORY/canonical/CV-1.16_SEAL.md §Outstanding Items`; `THEORY/logs/daily/2026-05-14/50_hmorse_sbm_results.md`. Next: `06_forbidden_claims.md` (Ch. IX).*
