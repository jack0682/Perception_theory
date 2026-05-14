---
type: log/exploration
date: 2026-05-12
target: OP-AFD-003 (Existence of Minimizing Transition Paths — Infimum Attainment)
canonical_version: CV-1.13 (read-only)
session_label: W7-Day3 (single-target deep-dev branch)
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# 01 — Exploration: OP-AFD-003 Infimum Attainment

**Session:** 2026-05-12
**Target (from plan.md Priority 3):** Prove (or disprove) that the infimum in AFD-D7
`C_AFD(F_i, F_j) = inf_{γ ∈ Adm(F_i, F_j)} J_AFD(γ; F_i)`
is **attained** by some admissible path γ_* ∈ Adm(F_i, F_j).

**This file covers:** Restatement + multi-approach + primary selection.

**Depends on reading:**
- `THEORY/working/AFD_0/abstract_formation_dynamics.md` §6 (AFD-D6, AFD-D7, AFD-D8, AFD-D9, AFD-D10), §14 (AFD-T5), §17 (OP-AFD-003).
- `THEORY/working/AFD_0/op_afd_004_proof.md` §5.1 item 4 (relation: OP-AFD-003 does **not** block lower-bound on Bar; it blocks *attainment*).
- `canonical.md` §13 Cat A list: T-PF-A1-AR (Σ_m is a compact convex polytope), T14 (Łojasiewicz analytic gradient-flow convergence), T8-Core, T-Merge(b), Pred-E Bridge, A3 closure, QM3, CSEH 2007.
- `01_pre_brainstorm.md` §3 (pre-session Arzelà-Ascoli sketch).

---

## §1. Note on multi-priority plan and target selection

The user-authored `00_plan.md` for 2026-05-12 lists three priorities:

| Pri | Item | Fits this template? |
|---|---|---|
| 1 | M-A2 numerical verification on 15×15 minimizer | Computational; needs `find_formation` runs. Out of scope for theoretical deep-dev session. |
| 2 | AFD-0 external audit via TeamCreate (3 agents) | **Banned by §10 of session prompt** (no OMC orchestration). |
| 3 | OP-AFD-003 infimum attainment | Theoretical proof attempt; ideal fit. |

**Selected single target:** **Priority 3 (OP-AFD-003).** Priorities 1 and 2 are noted in `99_summary.md` for user-driven handling.

Justification: prompt §1 requires "단일 target open problem" + §13 requires substantive theorem development. Priority 3 is the only item meeting both. Priority 1 (M-A2) is preserved as a parallel computational task for a separate session; we will however contribute a **theoretical prediction** for the M-A2 outcome in `03_integration_and_new_open.md` §4 — using AFD-T9 + canonical commitments about symmetry breaking — as a free byproduct.

---

## §2. Restatement (in primary author's language)

### 2.1 The formal question

Fix:

- `G = (V, E_G)` finite connected graph, `n = |V|`.
- `Σ_m = { u ∈ [0,1]^n : Σ_i u_i = m }` with `m ∈ (0, n)` — a compact convex polytope (T-PF-A1-AR Cat A).
- `E : Σ_m → ℝ`, the SCC energy `λ_cl E_cl + λ_sep E_sep + λ_bd E_bd`, continuous on Σ_m (analytic on its interior). `b_D = 0` (analyticity assumption — A3, used by T14).
- Two formation states `F_i, F_j ∈ V_form` with deterministic basins `B_{F_i}, B_{F_j} ⊂ Σ_m` (AFD-D2).
- `Adm(F_i, F_j) = { γ ∈ C([0,1], Σ_m) : γ(0) ∈ cl(B_{F_i}), γ(1) ∈ cl(B_{F_j}) }`.

Define for any `γ ∈ Adm(F_i, F_j)`:

$$
J_{\mathrm{AFD}}(\gamma; F_i) \;=\; \mathrm{Bar}(\gamma, F_i) \;+\; \lambda_D \,\mathrm{Var}_D(\gamma) \;+\; \lambda_K \, J_K(\gamma),
$$

$$
\mathrm{Bar}(\gamma, F_i) := \max_{s\in [0,1]} \bigl( E(\gamma(s)) - E_{F_i} \bigr).
$$

The infimum-cost is

$$
C_{\mathrm{AFD}}(F_i, F_j) := \inf_{\gamma \in \mathrm{Adm}(F_i, F_j)} J_{\mathrm{AFD}}(\gamma; F_i).
$$

**Question.** Does there exist `γ_* ∈ Adm(F_i, F_j)` with `J_AFD(γ_*; F_i) = C_AFD(F_i, F_j)`?

### 2.2 Three sub-questions

Resolving "OP-AFD-003" actually decomposes into three logically separable claims:

**(Q-A) Minimal case (`λ_D = λ_K = 0`).** Does `γ ↦ Bar(γ, F_i)` attain its infimum over `Adm(F_i, F_j)`?

**(Q-B) Rectifiable case (`λ_D > 0` or `λ_K > 0`, restricted to rectifiable γ).** Does `J_AFD` attain its infimum on the subclass `Adm_{rect}(F_i, F_j) = Adm ∩ {γ : ‖γ‖_BV ≤ L}` for some chosen `L`?

**(Q-C) Density.** Is `inf_{Adm_{rect}} J_AFD = inf_{Adm} J_AFD` (i.e. is the rectifiable subclass dense for the cost)?

Together, (Q-A)+(Q-B)+(Q-C) give a full attainment statement for the general case. We will treat (Q-A) as the *primary* deep-dev target — it is the case AFD currently uses (per AFD-T5 minimal version), and (Q-B)+(Q-C) propagate from it cleanly.

### 2.3 What is *not* being asked

- **Uniqueness** of `γ_*` (AFD does not claim it; degenerate flat saddle ridges create families).
- **Smoothness** of `γ_*` (we accept Lipschitz / merely continuous answers).
- **MEP / NEB convergence** (numerical questions; orthogonal to existence).
- **Quasipotential identification with FW instanton** (Layer 3; OP-AFD-005).
- **Sharp barrier value** (Layer 3; OP-AFD-004a).

### 2.4 Trivial subcases

- If `F_i = F_j`: γ ≡ u*_{F_i} is admissible and achieves `Bar = 0, Var_D = 0, J_K = 0`. Attained, trivially.
- If `cl(B_{F_i}) ∩ cl(B_{F_j}) ≠ ∅`: γ ≡ const path on the boundary intersection is admissible; cost 0 if `E_{F_i} = E_{F_j}`; otherwise still bounded.

The substantive case is `F_i ≠ F_j` with disjoint basins. Henceforth assumed.

### 2.5 Success criteria

| Verdict | What it means |
|---|---|
| **Theorem (unconditional)** | Infimum attained for every (F_i, F_j) and every (λ_D, λ_K) ≥ 0, with no restriction on path class. |
| **Proposition (conditional)** | Attainment proved under explicit restriction (e.g. rectifiable paths only, or path-length bound, or λ_D = λ_K = 0). |
| **Counterexample** | Explicit (F_i, F_j) on small graph where `Adm` admits a minimizing sequence with no convergent admissible limit. |
| **Conditional with gap** | Sketch with one isolated lemma open. |

### 2.6 Hidden assumptions in the user's formulation

Pre-brainstorm `01_pre_brainstorm.md` §3 sketched an Arzelà-Ascoli argument but contained two implicit assumptions to make explicit:

(IA-1) "Piecewise-linear paths are dense in the uniform topology among admissible paths" — true (uniform-approximation of continuous maps into a convex polytope), but Adm has *boundary conditions* (endpoints in cl(B_{F_i}), cl(B_{F_j})). Piecewise-linear approximation must respect these.

(IA-2) "max_s E(γ(s)) is continuous under uniform convergence" — yes, since E is continuous on compact Σ_m, but **only if** we use the sup-norm. Uniform convergence of γ_k → γ_* gives `‖E∘γ_k − E∘γ_*‖_∞ → 0` hence `sup E∘γ_k → sup E∘γ_*`. Confirmed.

The harder gap is **upper semicontinuity of `cl(B_{F_i})`-membership** under uniform convergence of endpoints — this we will handle by working with the closed condition `γ(0) ∈ cl(B_{F_i})` directly.

---

## §3. Multi-approach generation

Per prompt §4.2 and §5: at least 3 mathematically independent approaches with distinct success conditions and failure modes.

### Approach A — Arzelà-Ascoli on Lipschitz reparametrizations (compact-open)

**Core idea.** Reparametrize every admissible path by constant-speed (arc-length-equivalent) parametrization on `[0,1]`. Show every minimizing sequence is uniformly equicontinuous after reparametrization. Apply Arzelà-Ascoli on `C([0,1], Σ_m)`. Use continuity of `max ∘ E ∘ ·` under uniform convergence to identify the limit's cost as the infimum.

**Mathematical ingredients.**
- Arzelà-Ascoli theorem (uniform-norm compactness in `C([0,1], Σ_m)` with Σ_m compact).
- Uniform continuity of `E` on the compact polytope Σ_m.
- Property: every continuous γ : [0,1] → Σ_m can be *approximated* by Lipschitz γ' with the same Bar-cost to within ε (since Σ_m is convex and E is uniformly continuous).
- Closedness of `cl(B_{F_i}), cl(B_{F_j})` (they are closed by definition).

**Success form.** If γ_k → γ_* uniformly and each γ_k is Lipschitz-L, then γ_* is Lipschitz-L; γ_* ∈ Adm(F_i, F_j) by closed endpoint conditions; `Bar(γ_*, F_i) = lim Bar(γ_k, F_i) = Bar(F_i, F_j)`. Done.

**Failure modes.**
- (FM-A1) Minimizing sequence cannot be uniformly bounded in length — e.g. if `inf` requires γ to "go to infinity in time" through narrow flat regions. *Mitigation:* Σ_m is compact and Bar depends only on image; reparametrize by image, finite Hausdorff content gives finite length.
- (FM-A2) `Var_D(γ)` is lower-semicontinuous under uniform convergence but not continuous; a minimizing sequence may "lose Var_D in the limit". *Mitigation:* lower-semicontinuity is *what we need* for `J_AFD(γ_*) ≤ liminf J_AFD(γ_k) = inf`. Works.
- (FM-A3) `J_K(γ) = TV(K_act ∘ γ)` is lower-semicontinuous (TV always is) but K_act is discontinuous on the vineyard set V. *Mitigation:* TV lower-semicontinuity gives the inequality we want; OP-AFD-001/002 reserved for refined regularity.

**Yields:** Theorem (unconditional) for Q-A (minimal case); Proposition (conditional on uniform-equicontinuity of minimizers) for Q-B / Q-C.

### Approach B — Direct construction via finite-dimensional reduction on PL paths

**Core idea.** Approximate every admissible path by piecewise-linear interpolation through a finite point set in Σ_m. The space of N-vertex PL paths from any `u_0 ∈ cl(B_{F_i})` to any `u_1 ∈ cl(B_{F_j})` is a finite-dimensional compact subset of `(Σ_m)^N`. `Bar` restricted to this set is continuous (max of finitely many continuous functions). Take limit N → ∞.

**Mathematical ingredients.**
- Polytope structure of Σ_m → PL paths exist between any two interior points without leaving Σ_m.
- E continuous on compact Σ_m → Bar of PL path is continuous in vertex positions.
- Density of PL paths in `C([0,1], Σ_m)` under uniform norm.
- `cl(B_{F_i}), cl(B_{F_j})` compact (closed subsets of compact Σ_m).

**Why distinct from A.** Approach A works in *infinite-dimensional* path space and uses Arzelà-Ascoli compactness. Approach B works in *finite-dimensional* (Σ_m)^N and uses straight compactness; the limit N → ∞ is the only infinite-dimensional step. Different failure mode: B requires showing N → ∞ refinement is monotone (it isn't immediately).

**Success form.** For each N, the N-PL minimum `m_N := min_{u_1,...,u_N ∈ Σ_m} max_k E(linear-interp(u_k))` attains (continuous on compact). Show `m_N → C_AFD(F_i, F_j)` as N → ∞. Extract diagonal sub-sequence and verify it converges uniformly to an admissible limit.

**Failure modes.**
- (FM-B1) `m_N` may not be monotone in N (refinement can hurt PL approximation of curved minimizers temporarily). *Mitigation:* prove `m_N` non-increasing by inserting midpoints (PL with N+1 ≥ PL with N as long as the inserted vertex is on the existing segment; energy doesn't change).
- (FM-B2) Diagonal sub-sequence may not have a uniformly convergent sub-subsequence. *Mitigation:* same Arzelà-Ascoli argument as Approach A — equicontinuity by Lipschitz-bound, equiboundedness by Σ_m compact.

**Yields:** Constructive proof; gives a more explicit algorithmic approximation but ultimately leans on the same compactness. Useful for numerical NEB/string-method justification.

### Approach C — Γ-convergence / lower-semicontinuity envelope (relaxation)

**Core idea.** Re-cast `Bar(·, F_i) : C([0,1], Σ_m) → ℝ` as a *non-quadratic* functional and check whether its *relaxation* `Bar^{**}` (Γ-limit of any minimizing sequence) coincides with `Bar`. If the functional is already lower-semicontinuous under the chosen topology, attainment follows from direct method.

**Mathematical ingredients.**
- Topology choice: uniform-norm (sup) on `C([0,1], Σ_m)`.
- Lower-semicontinuity check: `γ ↦ max_s E(γ(s))` under uniform convergence.
- Compactness of sub-level sets `{γ : Bar(γ, F_i) ≤ M}` for `M < ∞`. This needs paths in Adm of bounded barrier to be uniformly equicontinuous — *false* without further restriction (a path can be arbitrarily wiggly while staying near `u*_{F_i}`).
- Restrict to **Lipschitz paths of bounded Lipschitz constant L** to recover compactness.
- Show `inf_{Adm_L} = inf_{Adm}` for L sufficiently large (this is Q-C and is the substantive density question).

**Why distinct from A and B.** Approach C is **topology-driven**: identify the right topology making Bar lower-semicontinuous and Adm compact, then attainment is mechanical. A is **direct compactness extraction** of a specific minimizing sequence. B is **constructive finite-N refinement**. The conceptual failure points differ:
- A fails if you cannot find a Lipschitz-bounded minimizing sub-sequence.
- B fails if PL approximation does not converge to Bar value (it might if E has very narrow saddles).
- C fails if you cannot prove density `inf_{Adm_L} = inf_{Adm}`.

**Failure modes.**
- (FM-C1) No single L works for all (F_i, F_j) pairs. *Mitigation:* allow `L = L(F_i, F_j)` chosen after seeing the pair (diagonal trick).
- (FM-C2) Energy E has *flat* regions where minimizing sequences wander indefinitely. *Mitigation:* on any flat plateau of E, Bar is locally constant, so wandering is "free" — but the *image* of γ stays in a compact set, so by Hausdorff compactness the image-set has a convergent subsequence in the Hausdorff metric. Reparametrize by arc-length on the image; reparametrized paths are Lipschitz with constant = total length of image-curve, which is finite for any image-curve of bounded perimeter in compact Σ_m.

**Yields:** Theorem (unconditional) for the minimal case via standard direct-method machinery, *provided* the density step `inf_{Adm_L} = inf_{Adm}` is established (this is the Q-C question).

### Approach D — Negative-direction approach: search for explicit counterexample

**Core idea.** Construct a small graph and parameter choice where Adm contains a minimizing sequence γ_k with no convergent admissible sub-sequence.

**Candidates.**
- **2-cycle / dumbbell**: two K=1 basins connected only through a narrow neck. The infimum is attained at the neck-passage path. Likely attained.
- **3-island T-junction**: three basins F_1, F_2, F_3 where the optimal F_1→F_2 path is via F_3 (high-cost ridge avoidance). Still attained.
- **Saddle-on-the-boundary ∂Σ_m**: γ_k must approach a saddle point lying on `{u_i = 0}` corner of Σ_m. Limit path touches the boundary; admissibility (γ(s) ∈ [0,1]^n ∩ Σ_m) is preserved by closed convex set. Still attained.
- **Pathological flat saddle**: E has a flat *line* of saddle points connecting two basins. Bar is constant along the entire line. Minimizing sequence indecisive about which saddle to cross. *Mitigation:* sequence has uniform Lipschitz bound; Arzelà-Ascoli extracts limit. Limit *does* sit on the saddle line. Attained.

**Conclusion (provisional).** No obvious counterexample emerges from standard candidates. The compact-convex-polytope-with-continuous-E setting is too tame. This supports the conjecture that **attainment holds unconditionally** for the minimal version (Q-A).

**Use.** Approach D is preserved as a *consistency check*. We attempt counterexample construction in `02_development.md` §6 before declaring victory. If a counterexample is found, it overturns Approaches A/B/C and reduces the result to a conditional one.

### Approach E (rejected) — Mountain Pass theorem

**Why rejected.** Mountain Pass (Ambrosetti-Rabinowitz) gives existence of a *critical point* of `Bar`-type functional under (PS) conditions. It does *not* directly give attainment of `Bar(F_i, F_j) = inf_γ max_s E∘γ`. The classical MP attainment requires `E - E_F_i` to have a strict mountain-pass geometry; our setting may or may not have it (degenerate saddle ridges per AFD-T10). Also MP brings H-MORSE-flavor regularity in through the back door (linking arguments use Hessian information), conflicting with AFD's H-MORSE-Non-Necessity (AFD-T9). **Excluded.**

---

## §4. Primary approach selection

### 4.1 Comparison matrix

| Approach | Independence | Strongest yield | Worst failure | Tool from canonical |
|---|---|---|---|---|
| A: Arzelà-Ascoli + reparametrization | Infinite-dim compactness | Theorem (Q-A unconditional) | Equicontinuity bound unclear without length cap | T-PF-A1-AR (Σ_m compact), E continuous |
| B: PL finite-dim reduction | Finite-dim compactness + limit | Constructive theorem + algorithm | Refinement-monotonicity needs proof | T-PF-A1-AR, E continuous |
| C: Γ-convergence relaxation | Topology engineering | Theorem if topology right | Density Q-C is the hard step | Same as A |
| D: Counterexample search | Disproof | Counter-example | None found in candidates | — |

### 4.2 Selected primary

**Primary = Approach A.** Reasons:

1. **Most direct payoff.** Q-A is the question AFD uses (per AFD-T5 minimal version, AFD-T8 FW instanton). Approach A delivers Q-A as a clean theorem.
2. **Cleanest dependency footprint.** Uses only T-PF-A1-AR (Σ_m compact polytope, Cat A) + E continuous on Σ_m (Cat A) + Arzelà-Ascoli (standard real analysis). No H-MORSE; no Łojasiewicz invoked (T14 enters only in defining cl(B_{F_i}), which is already done).
3. **Robust to E-degeneracy.** Approach A does not need E analytic — only continuous. Flat saddle ridges (per AFD-T10) cause no issue; minimizing sequence still has uniformly convergent sub-sequence.
4. **Extension path is clear.** Approach C is essentially Approach A in Γ-convergence language; reusing A's compactness step gives C for free as a bonus framing.

**Secondary preserved = Approach B.** It gives a *constructive* finite-N route. Useful for numerical justification (NEB / string method results in AFD numerics). Will be written up briefly in `02_development.md` §5 as a *parallel proof*.

**Tertiary = Approach D.** Counterexample search retained as a sanity check in `02_development.md` §6.

### 4.3 What Approach A does **not** deliver (and what we should not silently claim)

- Approach A does not solve Q-B (rectifiable case with λ_D, λ_K > 0) without additional density argument.
- Approach A does not give uniqueness of γ_*.
- Approach A does not prove smoothness of γ_*.
- Approach A does not identify γ_* with an FW instanton or an NEB minimum-energy path (Layer 3 questions).
- Approach A does not bound the *value* `C_AFD(F_i, F_j)` (that is OP-AFD-004 territory, partly resolved 2026-05-12 to Cat B).

These limits will be re-listed explicitly in `03_integration_and_new_open.md`.

---

## §5. Plan for `02_development.md`

Section plan:

- **§1** Setup (compact polytope Σ_m, continuous E, closed endpoint sets, admissible class).
- **§2** Lemma L1: Image-length reparametrization (every admissible path has a constant-speed reparametrization with Lipschitz constant ≤ image arc-length).
- **§3** Lemma L2: Uniform image-arc-length bound for minimizing sequences in the minimal case.
- **§4** Theorem T-OP-AFD-003-A (Primary: Q-A attainment via Arzelà-Ascoli).
- **§5** Parallel proof T-OP-AFD-003-B (Approach B: PL finite-dimensional construction).
- **§6** Counterexample search (Approach D); negative.
- **§7** Extension: Q-B/Q-C attainment with λ_D ≥ 0, λ_K ≥ 0 under bounded-length restriction.
- **§8** Category self-classification: Cat A (Q-A unconditional) / Cat B (Q-B+Q-C conditional on bounded length).
- **§9** Granularity check: each step's dependency (Cat A input or standard real analysis).

---

*End of `01_exploration.md`. Continue to `02_development.md`.*
