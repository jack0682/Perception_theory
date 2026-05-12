---
type: working/afd/v_afd
status: V-AFD Draft v0.1 (2026-05-12)
read_time: 5 minutes
---

# V-AFD — Compact Handoff for Next Agent

Read time: 5 minutes.

---

## 1. What was built

A vector-projection refinement of AFD-0:

> **V-AFD = Vector Abstract Formation Dynamics**

V-AFD reformulates AFD-0's formation-state tuple `(u_F^*, B_F, d_F, K_F, τ_F, E_F)` (AFD-D3) into a vector image:

> `Z(u) := (D(u), K_act(u), E(u), τ(u)) ∈ 𝒵 = [0,1]⁴ × {1,…,K_field} × ℝ × PD`

with primary diagnostic component

> `D(u) := (Bind(u), Sep(u), Inside(u), Persist(u)) ∈ [0,1]⁴`.

V-AFD does **not** modify any canonical claim, any AFD-0 definition, any AFD-0 theorem, or any existing OP-AFD. It adds **V-AFD-D1..D12**, **V-AFD-T1..T12**, and **OP-VAFD-001..010** as a new working-layer reformulation.

---

## 2. Definitions added (V-AFD-D1..D12)

| ID | Name | Highlight |
|---|---|---|
| D1 | Diagnostic Vector (static + temporal forms) | Static placeholder Persist = 1; pairwise / window forms via T-Temporal-Identity Cat A |
| D2 | Enriched Vector State Z | Baseline (D, K_act, E, τ); optional Z_+ with basin label / gradient norm |
| D3 | Vector Formation State | Exact `Z_F = Z(u_F^*)` and tolerance class `[F]_Z^ε` |
| D4 | Vector Trajectory `z_γ(s)` | Càdlàg on [0,1]; D∘γ Lipschitz, K_act∘γ piecewise constant, E∘γ continuous, τ∘γ continuous in d_B |
| D5 | Vector Transition `Z_i ⇒ Z_j` | via admissible γ with finite vector cost |
| D6 | Vector Transition Cost `C_V` | `λ_E Bar + λ_D Var_D + λ_K J_K + λ_τ Var_τ + λ_L Len` |
| D7 | Vector Stability | Design quantity `a·ExitCost + b·Q − c·LocalSensitivity` |
| D8 | Pareto Preorder `≼_D` | Componentwise on `[0,1]⁴`; refl, trans, not total, antisym mod equal vector |
| D9 | Scalarization (optional) | `Q_w(D) = Σ w_i D_i`; loses Pareto info |
| D10 | K-Vector Dynamics | K-stratum `S_K^Z`, K-jumps (merge / split / reconfig) |
| D11 | Vector Formation Graph `G_V` | Quotient of `G_form` under `~_Z`; edge collapse with inf-cost aggregation |
| D12 | Projection / Quotient `π_Z` | Surjection `V_form → V_Z` with non-injective fibers (V-AFD-T9) |

---

## 3. Theorems added (V-AFD-T1..T12) — status

| ID | Status | Cat | Highlight |
|---|---|---|---|
| T1 | Proposition | A | D(u) well-defined ∈ [0,1]⁴ |
| T2 | Proposition | A | ≼_D Pareto preorder properties |
| T3 | Proposition + Conjecture | A (well-def) / open (Lyap) | `L_w` Lipschitz; monotonicity along grad flow NOT generally true |
| T4 | Theorem | A | Vector trajectory exists; càdlàg on [0,1] |
| T5 | Theorem | A | BV bounds: Var(D∘γ) ≤ L_D · Len(γ) |
| T6 | Theorem | A | C_V well-defined; minimal version `= Bar = C_AFD^min` finite |
| **T6'** | **Theorem modulo Claim B.3** | A (cond) | **Attainment of C_V minimum, inheriting T-OP-AFD-003-A** |
| **T7** | **Theorem (by-inspection)** | **A** | **V-AFD does not require H-MORSE** |
| T8 | Lemma Candidate (Conditional, L3) | L3 | EK Compatibility (inherited from AFD-T8) |
| T9 | Theorem | A | Vector projection information loss (non-injectivity examples) |
| T10 | Proposition | B (modulo OP-AFD-002 reach) | K-jump detection for transversal γ |
| T11 | Proposition | A | `G_V = G_form / ~_Z` quotient |
| T12 | **Open Problem** | — | Markovianity of vector dynamics (OP-VAFD-003) |

**Central claims.**

- **V-AFD-T7**: by-inspection analog of AFD-T9. V-AFD does not use Hessian-nondegeneracy. EK / H-MORSE remain Layer-3 conditionals.
- **V-AFD-T9**: V-AFD is a genuine coarse-graining; vector-degeneracy is real (symmetric, Goldstone, topologically coincident examples).
- **V-AFD-T6'**: Inherits today's `02_development.md` attainment result; same Claim B.3 dependency.

---

## 4. Open problems added (OP-VAFD-001..010)

| ID | Severity | Topic |
|---|---|---|
| OP-VAFD-001 | M | Continuity / Lipschitz status of D under vineyard crossings |
| OP-VAFD-002 | M | Persist coordinate for static vs temporal states |
| **OP-VAFD-003** | **H** | **Markovianity / lumpability of vector dynamics** |
| OP-VAFD-004 | M | Injectivity loss of Z — *when* does it matter dynamically? |
| OP-VAFD-005 | M | Topology signature stability beyond d_B Lipschitz |
| OP-VAFD-006 | M | Vector transition cost attainment in enriched form |
| OP-VAFD-007 | L | K-jump regularity for non-transversal paths |
| OP-VAFD-008 | L | Empirical estimation of vector dynamics (numerical) |
| OP-VAFD-009 | M | Relation to OP-AFD-003 (attainment) — Claim B.3 dependence |
| OP-VAFD-010 | M | Relation to OP-AFD-004 (merge barrier) — V-AFD merge LB |

**Headline.** OP-VAFD-003 (Markovianity) is the single H-severity new OP — fundamental open question about whether vector dynamics is a Markov chain.

---

## 5. What is proven, what is open

| Item | Status |
|---|---|
| V-AFD baseline is well-defined | proved (V-AFD-T1, T4 Cat A) |
| Pareto preorder on diagnostics | proved (V-AFD-T2 Cat A) |
| Vector trajectory càdlàg with explicit regularity | proved (V-AFD-T4 Cat A) |
| BV bounds along rectifiable γ | proved (V-AFD-T5 Cat A) |
| C_V minimal version finite | proved (V-AFD-T6 Cat A) |
| C_V attainment | proved modulo Claim B.3 (V-AFD-T6') |
| V-AFD H-MORSE-free | proved by-inspection (V-AFD-T7) |
| EK compatibility at Layer 3 | conditional (V-AFD-T8 Lemma Candidate) |
| Information loss exists | proved by examples (V-AFD-T9) |
| K-jump piecewise-constant for transversal γ | proved modulo OP-AFD-002 reach (V-AFD-T10) |
| G_V = G_form / ~_Z quotient | proved by-construction (V-AFD-T11) |
| **Markovianity of vector dynamics** | **OPEN (V-AFD-T12 / OP-VAFD-003)** |
| Quantitative information loss characterization | open (OP-VAFD-004) |
| Vector cost lower bounds match AFD-T7 merge LB | open (OP-VAFD-010) |

---

## 6. Was H-MORSE avoided?

**Yes.** V-AFD-T7 (Theorem by-inspection) explicitly establishes: V-AFD-D1..D12 + V-AFD-T1..T11 do not use:
- Hessian nondegeneracy at any critical point,
- Existence of index-1 saddles,
- Hessian determinants,
- Morse-type genericity conditions.

The only V-AFD result that interfaces with H-MORSE is V-AFD-T8 (EK Compatibility), which is a Layer-3 conditional Lemma Candidate inherited from AFD-T8. V-AFD baseline statements (T1..T7, T9..T11) are fully H-MORSE-free.

---

## 7. Was EK correctly deferred to Layer 3?

**Yes.** Section 1.2 ("Why not exact Eyring-Kramers as foundation") and V-AFD-T8 explicitly defer:
- Hessian-determinant prefactor (Layer 3 only).
- Reflected-Langevin EK adaptation (OP-AFD-005 literature gap).
- T_* small-noise axiom (OP-0021).

V-AFD-T8 gives exponential-order compatibility only: `T_* log E[τ] → Bar`. Prefactors are not claimed in V-AFD.

---

## 8. Main risks

| Risk | Mitigation |
|---|---|
| Vector-degeneracy makes V-AFD insufficient for dynamical specificity | Acknowledged (V-AFD-T9, OP-VAFD-004); baseline + basin label augmentation possible |
| Markovianity assumption silently introduced elsewhere | OP-VAFD-003 explicitly open; no V-AFD theorem assumes it |
| Sorted-bar τ-coordinate discontinuity | Acknowledged (V-AFD-T4 caveat); use d_B-bottleneck for stability claims |
| Persist confusion (static vs temporal) | Three forms distinguished (V-AFD-D1, D1', D1''); protocol-question open (OP-VAFD-002) |
| Scalarization adoption silently | Marked optional and lossy (V-AFD-D9, §6.6); Pareto preorder preserved |
| Claim B.3 unverified | Inherited from `logs/daily/2026-05-12/02b`; status tracked at OP-AFD-003a-revised |
| K_act non-transversal γ | OP-VAFD-007; baseline restricted to transversal γ |

---

## 9. Recommended next task

**Three viable paths (in priority order).**

### Option A (Recommended): OP-VAFD-003 — Markovianity Characterization

The H-severity gap in V-AFD. Specific sub-tasks:

1. **Deterministic case (T_* = 0):** Prove formally that `Z_+ = (Z, basin\_label)` makes the dynamics Markov on `V_Z × V_form` (singleton-per-basin). Conjecture: yes, by determinism of gradient flow. Sketch:
   - Field state in basin B_{F_i} flows deterministically to u_{F_i}^*.
   - Z_+ at any time uniquely identifies the basin (basin label coordinate).
   - Subsequent dynamics depends only on the basin, hence only on Z_+.
   - Markovianity holds (trivially, deterministically).

2. **Stochastic case (T_* > 0):** Lumpability via Bovier-style metastability. Requires Layer-3 inputs (H-MORSE-Local Cat B + Pkg I). Defer until CV-1.14.

3. **Approximate Markovianity:** Asymptotic regime T_* → 0; rigorous version of "vector dynamics is approximately Markov for small noise". Standard FW + EK techniques, but for V-AFD requires specifying the basin-label coordinate.

Output: `THEORY/working/AFD_0/V_AFD/op_vafd_003_markovianity.md`. Estimated 1–2 sessions.

### Option B: OP-VAFD-004 — Injectivity Loss Characterization

The architecturally significant M-severity gap. Specific sub-tasks:

1. Prove that vector-degenerate fibers (V-AFD-T9 examples) are **dynamically equivalent** under SCC operators (Aut(G)-equivariance argument).
2. Therefore Layer-2 transition-ordering questions are *insensitive* to the loss.
3. Layer-3 specifications (which specific basin) require basin label.

Output: theorem of form "V-AFD-T9 information loss does not affect Layer-2 transition ordering; it affects only Layer-3 specifics." Estimated 1 session.

### Option C: V-AFD-T3 — Lyapunov Refinement (Conjecture → Theorem)

Identify conditions on weights `w` and on E under which `L_w(D(u(t)))` is monotonically decreasing along gradient flow. Connection to dual-mode SCC operators (closure + distinction). Estimated 1–2 sessions.

### Option D (long-tail): V-AFD numerical baseline (OP-VAFD-008)

Implement V-AFD numerics on canonical 15×15 grid. Compute `Z(u)` for `find_formation` outputs; track `z_γ(s)` along NEB-computed paths; verify V-AFD-T5 BV bounds empirically. Estimated 2–3 sessions involving `CODE/`.

---

## 10. Slogan

> **V-AFD lifts AFD-0 to vector language.**
> **The diagnostic vector is the primary observable.**
> **The vector graph is a quotient of the formation graph.**
> **H-MORSE is Layer 3; V-AFD is Layer 2.**

---

## 11. File reference

| File | Read priority |
|---|---|
| `README.md` | First (1 min). |
| `vector_abstract_formation_dynamics.md` | Main (20 min). |
| `v_afd_theorem_registry.md` | Tabular (3 min). |
| `v_afd_open_problems.md` | OP-VAFD-001..010 (3 min). |
| `v_afd_examples.md` | 8 stress-test scenarios (10 min). |
| `v_afd_audit.md` | 15-question audit (5 min). |
| `v_afd_summary_for_next_agent.md` | This file (5 min). |

---

## 12. Cross-references

- **AFD-0 parent**: `../abstract_formation_dynamics.md` (15 min skim).
- **Today's OP-AFD-003 / T5-Strong proof**: `logs/daily/2026-05-12/02_development.md` §5 (T-OP-AFD-003-A), `02b_L3_tightening_and_op003c.md` (audit + Claim B.3).
- **Today's mathematical-toolkit brainstorm**: `logs/daily/2026-05-12/20_AFD_T5_R1_mathematical_toolkit_brainstorm.md`.
- **Remote-ultraplan AFD-T5 framing correction**: `logs/daily/2026-05-12/30_remote_verification_and_T5_statement_correction.md`.
- **AFD-0 reclassification of H-MORSE**: `../afd_hmorse_reclassification.md`.
- **CV-1.14 H-MORSE-Local programme**: `THEORY/working/CV114_H_MORSE_PACKAGEII/`.

---

## 13. Canonical compatibility

V-AFD does **not** require any canonical edit. CV-1.13 stays sealed. No new canonical claim is introduced. V-AFD is a working-layer reformulation only.

If AFD-0 R1 promotion executes (per `99_summary.md` Options 1 of today's session), V-AFD-T2 (Pareto preorder) and V-AFD-T7 (H-MORSE Non-Necessity in vector language) could optionally enter as companion canonical propositions, but neither is a blocker or a required addition.

---

*End of `v_afd_summary_for_next_agent.md`. Session 2026-05-12 W7 Day 3 V-AFD branch closed.*
