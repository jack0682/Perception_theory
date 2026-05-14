> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 09 — CV-1.14 Recommendation

Final recommendation distilled from all preceding documents.

---

## 1. Recommended next target

**W7-CV114 = Path B (H-MORSE-Local Cat B) + Path D (Package II Pre-Theorem Cat B conditional).**

CV-1.14 deliverable: **+2B → 59A / 16B / 5C / 5R = 85 claims**, HT-3.6.

CV-1.14 should **NOT** attempt full Package II immediately. It should:
1. Reconstruct the exact H-MORSE statement (done — `02_H_MORSE_statement_reconstruction.md`).
2. Prove or disprove unconditional Morse (done — disproved; see `05_counterexample_search.md`).
3. Formulate corrected conditional/local H-MORSE (done — Path B statement).
4. Map Package II dependencies (done — `06_packageII_dependency_map.md`).
5. **Prove H-MORSE-Local Cat B** (Path B proof, the new CV-1.14 work).
6. **Register Package II Pre-Theorem Cat B conditional** (Path D, bibliographic + notation).

Estimated total effort: 3–5 sessions.

---

## 2. Why this target

### 2.1 Maximally aligned with existing canonical state

The closure-correction Hessian gap (canonical.md line 1139, **Cat A**) is the single most directly relevant piece of canonical material. It already states that non-trivial constrained minimizers of SCC energy have strictly larger minimum Hessian eigenvalue than corresponding Allen-Cahn minimizers. **H-MORSE-Local Cat B is essentially the formalization of this Cat A result as a registered Morse theorem.**

### 2.2 Avoids the structural impossibilities

Unconditional H-MORSE is **provably false** (see `05_counterexample_search.md`): V5b-T-zero on cycles/tori, $D_4$-fixed center minimizers, T8-Full bifurcation threshold, boundary strata. Any CV-1.14 target attempting unconditional Morse will fail.

Path B's three assumptions (M-A1, M-A2, M-A3) exactly excise all four structural counterexample classes.

### 2.3 Unlocks Package II prerequisite stack

H-MORSE-Local Cat B is the **first of three gates** to Package II (the others being H-MORSE-Saddle and OP-0021). Closing it converts the hypothesis-tree H-MORSE node from OPEN to PARTIALLY CLOSED, and immediately upgrades T-P-F-ε0-K's H5 status from "unproved global hypothesis" to "Cat B canonical lemma".

### 2.4 Path D is essentially free

Path D (Package II Pre-Theorem) is bibliographic + notation work — no new mathematics. Once Path B closes, registering the Bouchet-Reygner / Bovier-Den Hollander reflected EK formula as a **conditional** Cat B theorem in SCC notation costs at most one session and adds substantial value (bibliographic integration into canonical SCC + explicit "what's left for Package II" registry).

---

## 3. What NOT to attempt yet

- **Full Eyring-Kramers Cat A (Path E).** Multi-session blocker; cannot close at CV-1.14.
- **H-MORSE-Saddle.** Parallel to H-MORSE-Local; can be tackled at CV-1.15 after CV-1.14 closes Path B.
- **OP-0021 ($T_*$ canonical registration).** Independent track; W9+ scope per existing canonical notes.
- **Freidlin-Wentzell quasipotential** for reflected Langevin. Open derivation, W8+ scope.
- **Multi-formation Morse on $\widetilde\Sigma_M^{K_\mathrm{field}}$.** NQ-248 / W11–W12 scope per canonical.md line 1322.
- **Stratified Morse on $\partial\Sigma_m$.** Option B per canonical.md §11.1; deferred to W7+.
- **OP-0008 σ-inheritance / Wigner-projection.** Separate Q6 track; can run in parallel with H-MORSE work.

---

## 4. Exact first theorem to attack

> **Theorem H-MORSE-Local (Cat B candidate).** Let $G$ be a finite connected graph on $n$ vertices (canonical: 15×15 grid, free BC, $n = 225$). Let $u^* \in \Sigma_m^\circ$ be a non-uniform single-formation local minimizer of the full SCC energy $\mathcal E = \lambda_\mathrm{cl}\mathcal E_\mathrm{cl} + \lambda_\mathrm{sep}\mathcal E_\mathrm{sep} + \lambda_\mathrm{bd}\mathcal E_\mathrm{bd}$, satisfying:
>
> **(M-A1)** Canonical parameter window: $a_\mathrm{cl} \in (0, 4)$ (axiom A3), $b_D = 0$ (canonical), $\beta / \alpha > 4\lambda_2 / |W''(c)| + \eta$ for some $\eta > 0$ (strictly above T8-Full threshold).
>
> **(M-A2)** Trivial stabilizer: $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*) = \{e\}$.
>
> **(M-A3)** Strict interiority: $0 < \delta_0 \leq u^*_i \leq 1 - \delta_0$ for some $\delta_0 > 0$.
>
> Then the projected Hessian $H^\mathrm{proj}_\mathcal E(u^*) = \Pi_T H_\mathcal E(u^*) \Pi_T$ on $T_{u^*}\Sigma_m = \mathbf 1^\perp$ is positive definite, with explicit lower bound
>
> $$\mu_\mathrm{min}(H^\mathrm{proj}_\mathcal E(u^*)) \geq \mu_0(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl}, \delta_0, \eta) > 0,$$
>
> where $\mu_0$ is derived from the closure-correction Hessian gap (canonical.md line 1139, Cat A) plus the T8-Full sub-bifurcation margin $\eta$ plus the closure spectral gap $(1 - a_\mathrm{cl}/4)^2$ (canonical $L_\mathrm{cl} = a_\mathrm{cl}/4 < 1$).
>
> **Status:** Cat B (conditional on M-A1 + M-A2 + M-A3). Cat A path: derive M-A2 + M-A3 from canonical T8-Core for the specific canonical 15×15 minimizer.

---

## 5. Expected outcome

| Deliverable | Status |
|-------------|--------|
| H-MORSE-Local Cat B registered in `canonical.md §13 Category B` | +1B |
| Package II Pre-Theorem Cat B conditional registered | +1B |
| Hypothesis tree H-MORSE node | OPEN → PARTIALLY CLOSED |
| HT version | HT-3.5 → HT-3.6 |
| Claim count | 59A/14B/5C/5R = 83 → 59A/16B/5C/5R = **85** |
| T-P-F-ε0-K H5 dependency | "global hypothesis" → "Cat B lemma cited" |
| CV-1.14 seal | YES |

Cat A promotion of H-MORSE-Local awaits CV-1.15 (deriving M-A2/M-A3 from canonical axioms for the specific canonical 15×15 / exp83 minimizer).

---

## 6. Estimated blockers

| Blocker | Severity | Detected at |
|---------|----------|-------------|
| M-A2 audit on canonical 15×15 minimizer might fail (some minimizers may have nontrivial $D_4$ stabilizer) | Moderate | Verify in `M_A2_stabilizer_audit.md` |
| M-A3 audit: canonical 15×15 minimizer may have $u^*_i$ very close to 0 or 1 at some sites | Low | Use existing exp01 / exp83 data to set $\delta_0$ |
| Explicit closure-correction-gap formula $\mu_0$ may require tightening | Moderate | Extract from canonical.md line 1139 proof |
| Bouchet-Reygner / Bovier-Den Hollander citations may not be available in the working environment | Low | Bibliographic, can be deferred |
| Multi-irrep symmetry quotient if M-A2 fails | Moderate | Use canonical Theorem 1 orbital decomposition |

None of these are showstoppers. The blocker structure is "verify M-A2/M-A3 on canonical minimizers" → "extract explicit $\mu_0$" → "compose with orbital Theorem 1" → "write canonical entry".

---

## 7. Proposed next agent prompt

See `10_agent_handoff_prompt.md` for the full executable prompt.

Summary of the recommended next-agent task:

> **W7-CV114B — H-MORSE-Local Cat B proof attempt + Package II Pre-Theorem registration.**
>
> Inputs: this audit folder (`THEORY/working/CV114_H_MORSE_PACKAGEII/`); canonical.md line 1139 (closure-correction gap Cat A); canonical.md Theorem 1 (orbital Cat A); canonical.md V5b-T-zero / V5b-T-b (Cat A); T-PF-A1 Package I (Cat A all 4); T-P-F-ε0-K Cat B with H5.
>
> Output: H-MORSE-Local Cat B registered; Package II Pre-Theorem Cat B-conditional registered; canonical files updated; CV-1.14 sealed.
>
> Effort estimate: 3–5 sessions.
>
> Stop conditions: H-MORSE-Local Cat B proven OR M-A2/M-A3 audit fails (then switch to Path C Generic OR Path A fallback OP-MORSE registration).

---

## 8. Canonical update policy at CV-1.14 close

When CV-1.14 closes:
- Add `H-MORSE-Local` row to `theorem_status.md` Cat B.
- Add §13 Category B entry to `canonical.md` for `H-MORSE-Local`.
- Add `Package II Pre-Theorem` row to `theorem_status.md` Cat B conditional.
- Update `hypothesis_tree.md` HT-3.5 → HT-3.6: H-MORSE OPEN → PARTIALLY CLOSED.
- Append entry to `CHANGELOG.md`.
- Create seal document `THEORY/canonical/CV-1.14_SEAL.md`.

These canonical edits should **only** happen after the H-MORSE-Local proof and Package II Pre-Theorem registration are complete; **this audit folder does not change canonical state.**
