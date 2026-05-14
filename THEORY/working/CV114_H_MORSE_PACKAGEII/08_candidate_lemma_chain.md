> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 08 — Candidate Lemma Chain (CV-1.14)

Five candidate paths for CV-1.14. For each: required lemmas, difficulty, expected status, risk, output files, seal feasibility.

---

## Path A — Conservative Audit Only

**Scope:** Complete this audit; register working OP entry; no theorem promotion.

**Required lemmas:** None proved; existing working files only.

**Difficulty:** Trivial (this audit already does most of it).

**Expected status:** No claim count change.

**Risk:** Very low.

**Output files (already created in this audit):**
- `THEORY/working/CV114_H_MORSE_PACKAGEII/00..10*.md` (10 files in this folder)

**Additional CV-1.14 output proposed:**
- Register **OP-MORSE** in `theorem_status.md` Open Problems Catalog as the formal canonical analogue of the hypothesis-tree H-MORSE node, citing this audit folder.

**Can seal CV-1.14?** Technically yes — CV-1.14 = audit + OP registration. But this is a thin seal; no theorem advance.

**Verdict:** Acceptable fallback if no proof emerges. Not the recommended primary path.

---

## Path B — Local H-MORSE Cat B (recommended primary)

**Scope:** Prove **H-MORSE-Local Cat B** as a working theorem; canonical promotion candidate.

**Statement (target):** As in `02_H_MORSE_statement_reconstruction.md §8 Path A`. The non-uniform single-formation minimizer $u^* \in \Sigma_m^\circ$ of full SCC energy, satisfying (M-A1) parameter window, (M-A2) trivial stabilizer, (M-A3) strict interiority, has positive-definite projected Hessian with explicit closure-correction-gap lower bound.

**Required lemmas:**

| Lemma | Status | Source |
|-------|--------|--------|
| **L1.** Tangent projector $\Pi_T = I - n^{-1}\mathbf 1\mathbf 1^T$ is well-defined and orthogonal | Trivial | Linear algebra |
| **L2.** SCC energy $\mathcal E$ is $C^\omega$ on $\Sigma_m^\circ$ | Cat A | canonical.md §9.2 + $b_D = 0$ |
| **L3.** Closure-correction Hessian gap | **Cat A** | canonical.md line 1139 (use directly) |
| **L4.** Symmetry quotient: under $G_u = \{e\}$, orbital decomposition is trivial (no enforced eigenvalue degeneracy) | Cat A | Theorem 1 canonical.md line 1362 |
| **L5.** T8-Full bifurcation locus is codim-1; canonical $\beta/\alpha$ strictly above threshold | Cat A | T8-Full |
| **L6.** Boundary stratum exclusion: M-A3 strict interiority prevents boundary critical points | Trivial | Definition |
| **L7.** Closure operator's $J_\mathrm{Cl}$ has spectral norm $< 1$ under $a_\mathrm{cl} < 4$ | Cat A | H-SINK-1 |
| **L8.** Combine L3 + L4 + L5 + L7 → projected Hessian is positive definite with explicit lower bound $\mu_0$ | NEW | this proof |

**Difficulty:** Moderate. L1–L7 are all existing Cat A; L8 is the composition. Estimated 2–3 sessions.

**Expected status:** **Cat B** at first promotion (Cat A conditional on M-A2 + M-A3 + canonical 15×15 / free-BC scope).

**Risk:** Low-to-moderate. The main risk is that M-A2 + M-A3 together exclude the canonical exp83 minimizer — verify they hold on existing experimental anchors before proving.

**Output files:**
- `THEORY/working/morse/H_MORSE_LOCAL.md` (main proof file)
- `THEORY/working/morse/M_A1_parameter_window.md` (M-A1 definition + Cat A bound)
- `THEORY/working/morse/M_A2_stabilizer_audit.md` (M-A2 stabilizer check on canonical 15×15 minimizer)
- `THEORY/working/morse/M_A3_interiority_audit.md` (M-A3 strict interiority check)
- Canonical edits: add H-MORSE-Local row to `theorem_status.md` Cat B; add §13 entry to `canonical.md`.

**Can seal CV-1.14?** **Yes** — +1B to count (84 claims total), HT-3.6. Hypothesis tree H-MORSE node downgraded from OPEN to PARTIALLY CLOSED.

**Verdict:** **Recommended primary path.** Moderate effort, clear deliverable, opens Package II prerequisite stack.

---

## Path C — Generic H-MORSE Cat B

**Scope:** Prove generic-perturbation Morse property: for an open dense subset of small symmetry-breaking perturbations, $\mathcal E + \rho \cdot u$ is Morse on $\Sigma_m^\circ$.

**Required lemmas:**

| Lemma | Status |
|-------|--------|
| Smale-Sard transversality on smooth manifolds | Standard reference (not canonical) |
| Perturbation class preserving SCC ontology ($b_D = 0$, $a_\mathrm{cl} < 4$, etc.) | NEW |
| Density / openness in canonical parameter space | NEW |

**Difficulty:** Moderate-to-high. Transversality is standard, but proving the SCC-compatible perturbation class is open dense is non-trivial.

**Expected status:** **Cat B** for generic statement.

**Risk:** Moderate. May produce a vacuous theorem if the perturbation class is too restrictive.

**Output files:** `THEORY/working/morse/H_MORSE_GENERIC.md` + supporting lemmas.

**Can seal CV-1.14?** Yes, +1B.

**Verdict:** Useful alternative if Path B encounters M-A2 issues. Less directly useful for Package II (Path B gives explicit lower bounds; Path C gives only generic existence).

---

## Path D — Package II Pre-Theorem (Bovier-Eckhoff reflected EK adaptation)

**Scope:** Adapt Bouchet-Reygner 2016 / Bovier-Den Hollander 2015 reflected Langevin EK to SCC notation; register as conditional theorem awaiting H-MORSE + OP-0021.

**Required lemmas:**

| Lemma | Status |
|-------|--------|
| Bouchet-Reygner / Bovier-Den Hollander EK on convex polytope | External literature (Cat A in literature) |
| SCC notation translation: $\tilde C \cong \Sigma_m$ via T-PF-A1-AR | Cat A |
| Conditional EK formula for SCC minima/saddles, contingent on H-MORSE + ΔE + $T_*$ | NEW |

**Difficulty:** Moderate. Mostly bibliographic + notation translation; no new mathematics.

**Expected status:** **Cat B conditional** (on H-MORSE + ΔE Cat A + OP-0021).

**Risk:** Low — the theorem is fully conditional; correctness follows from cited literature.

**Output files:** `THEORY/working/morse/PACKAGE_II_ENTRY.md` with conditional EK statement + bibliography.

**Can seal CV-1.14?** Yes — register as Cat B with explicit list of conditions.

**Verdict:** Useful **as a companion to Path B**, not as a substitute. Best done after Path B closes.

---

## Path E — Full Package II (Eyring-Kramers Cat A)

**Scope:** Full proof of Eyring-Kramers rates for SCC at canonical 15×15.

**Required lemmas:**

| Lemma | Status |
|-------|--------|
| H-MORSE-Local Cat A | OPEN |
| H-MORSE-Saddle Cat A | OPEN |
| ΔE Cat A | currently Cat B (T-P-F-ε0-K) |
| $T_*$ canonical registration (OP-0021) | OPEN |
| Freidlin-Wentzell action for reflected Langevin on $\tilde C$ | OPEN |
| Bouchet-Reygner / Bovier-Den Hollander reflected EK + SCC adaptation | requires above |
| Numerical anchor experiment | needs new experiment design |

**Difficulty:** **Very high.** Each of H-MORSE-Local Cat A, H-MORSE-Saddle Cat A, and OP-0021 alone is multi-session work; combined ≥ 6–10 sessions.

**Expected status:** **Cat A** if all gates close; **Cat B at best** without OP-0021.

**Risk:** **Very high.** Any one of the gates failing leaves the EK theorem stuck.

**Output files:** `THEORY/working/morse/EK_FULL.md` (multi-section file) + many supporting working files.

**Can seal CV-1.14?** Almost certainly **no** within a single CV.

**Verdict:** **Do not attempt at CV-1.14.** Reserve for CV-1.15+ after H-MORSE and OP-0021 individually close.

---

## Path comparison summary

| Path | Effort (sessions) | Cat target | Risk | Seal CV-1.14? | Recommended? |
|------|---------------------|------------|------|-----------------|----------------|
| A — Audit only | 0 (this audit) | (none) | very low | thin yes | fallback |
| **B — H-MORSE-Local Cat B** | **2–3** | **Cat B** | **low-mod** | **yes (+1B)** | **PRIMARY** |
| C — H-MORSE-Generic Cat B | 2–4 | Cat B | moderate | yes (+1B) | alternative |
| D — Package II Pre-Theorem | 1–2 | Cat B conditional | low | yes (+1B) | companion to B |
| E — Full EK Cat A | 6–10+ | Cat A | very high | no | defer |

---

## Recommended CV-1.14 plan

**Primary:** Path B (H-MORSE-Local Cat B). 2–3 sessions.

**Companion:** Path D (Package II Pre-Theorem) after Path B closes — adds Cat B-conditional EK entry, +1B. Total CV-1.14 deliverable: +2B → 59A/16B/5C/5R = 85 claims, HT-3.6.

**Deferred (CV-1.15+):**
- H-MORSE-Saddle (parallel to H-MORSE-Local but for index-1 saddles)
- OP-0021 (T_* registration; independent track)
- Full Eyring-Kramers Cat A (after both)

**Alternative if Path B blocked by M-A2 audit failure:** Path C (Generic). +1B.

**Fallback if no proof:** Path A only. Register OP-MORSE; no count change.

See `09_CV114_recommendation.md` for the final recommendation and `10_agent_handoff_prompt.md` for the executable handoff.
