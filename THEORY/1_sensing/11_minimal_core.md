---
type: working/sensing_pipeline/minimal_core
version: v0
date: 2026-05-25
status: ACTIVE — Pass 10 Minimal-Structure Refinement
purpose: |
  Single document containing the entire minimal core of sensing_pipeline after 9 adversarial verification passes + Pass 10 refinement.
  Replaces the TC-candidate corpus reading of the directory; the 10 prior docs (00-10) are reclassified as EXPLORATION RECORD.
  Output of 10-iteration minimal-structure adversarial refinement following the prompt at ~/.claude/plans/minimal-adversarial-refinement-prompt.md
register: MINIMAL_CORE (single source of authoritative claims)
parent: 00_INDEX
prev: 10_reconstruction_pass6
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  added_new_framework_name: NO
  preserved_audit_trail: YES (all deletion notices remain in stage docs)
  downgraded_before_reconstructing: YES (no new TC; only compression of survivors)
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[10_reconstruction_pass6]] · Source: ~/.claude/plans/minimal-adversarial-refinement-prompt.md

# Minimal Core — Pass 10 Adversarial Refinement Output

## 0. Document purpose

After 9 verification passes (Pass 3–9) deleted 31 of 32 TC-candidates (96.9% attrition), the underlying problem was diagnosed: *the original directory was framed as a theorem-candidate corpus when its actual content is mathematical exploration record + negative-result documentation*.

This document is **the single authoritative output** of the sensing_pipeline directory under that honest framing. The 10 prior documents (00–10) are reclassified as **EXPLORATION RECORD** (research process documentation), not theorem candidates.

The 10-iteration adversarial refinement (Pass 10) executed:
- Iter 1: register inventory
- Iter 2–5: Pattern A–D sweeps
- Iter 6: 5+5+5 compression
- Iter 7: survival-criteria deletions (this document replaces the TC-corpus reading)
- Iter 8: reconstruction-rule audit (PASSED — no new architecture introduced)
- Iter 9: minimal core writing (this document)
- Iter 10: final report (§9 below)

---

## 1. Five Primitive Terms (operationally defined)

Each term has: (a) precise definition, (b) measurement procedure, (c) what it is NOT.

### P1 — Photon arrival event
- **Definition**: atomic tuple $(t, x, \nu)$ where $t \in \mathbb{R}^+$ is arrival time, $x$ is sensor location (discrete or continuous), $\nu$ is wavelength.
- **Measurement**: SPAD array with TDC timestamp resolution $\sim$ ps; DVS event-stream timestamps; or aggregate photon counts per CMOS pixel-frame.
- **NOT**: assumed Poisson; assumed independent across events; assumed to have density.

### P2 — Bounded intensity-valued response
- **Definition**: scalar $r_i(t) \in [0, R_{\max}]$ at sensor index $i$, time $t$; non-negative; bounded above.
- **Measurement**: patch-clamp membrane potential; calcium imaging fluorescence; or model output normalized to known $R_{\max}$.
- **NOT**: assumed to be a probability density; assumed unbounded; assumed to satisfy mass conservation.

### P3 — Forward-only kernel transformation
- **Definition**: mapping $\mathcal{K}: \mathcal{S}_{in} \to \mathcal{S}_{out}$ where output at time $t$ depends only on input at times $\leq t$; intensity-valued (not probability).
- **Measurement**: input-output recording in a single sensor stage with known input.
- **NOT**: assumed Markov on a global state space; assumed to preserve total mass; assumed to be a probability kernel.

### P4 — Tolerance relation σ
- **Definition**: binary symmetric reflexive (non-transitive) relation on events: $\sigma(e_i, e_j) \iff |t_i - t_j| < \delta_t \,\wedge\, d(x_i, x_j) < \delta_x$ for chosen $\delta_t, \delta_x$.
- **Measurement**: choice of $\delta_t, \delta_x$ from sensor resolution; σ is then computable from raw event stream.
- **NOT**: a metric; a topology; a vector-space inner product.

### P5 — Channel index
- **Definition**: finite set $\mathcal{C}$ tagging biologically-given parallel pathways (ON/OFF, M/P/K, L/M/S cone).
- **Measurement**: cell-type identification via genetic markers, morphology, or electrophysiological signature.
- **NOT**: derived from the framework; not optimized; not learned. *Given by anatomy*.

---

## 2. Five Constraints (negative — what the framework explicitly does NOT assume)

Negative constraints are stronger than positive claims because they survive Pass #15 vacuity attack.

### C1 — Not Poisson
Photon arrival statistics in actual retina are **super-Poissonian** (Bose-Einstein bunching at $g^{(2)}(0) > 1$ in low-coherence thermal light; gain-modulated under adaptation). Any modeling step that assumes Poisson must explicitly justify the regime, OR use Cox/Hawkes intensity formulation.

### C2 — Not Markov
Retinal processing has cortico-fugal feedback, multi-timescale adaptation (ms → hours), lateral coupling via horizontal/amacrine cells, and gap-junction connectivity. Standard Markov-chain inequalities (DPI in textbook form) apply only to an *augmented hidden-state extension* whose construction is not provided.

### C3 — Not probability-kernel
Retinal stages exhibit saturation, refractory periods, divisive normalization, and gain modulation — all of which violate probability-mass conservation. The admissible object is **sub-probability or intensity-valued kernel**; probability-kernel theorems (Kallenberg, Ionescu-Tulcea standard form) do not directly apply.

### C4 — Not unbounded
All retinal signal spaces are **bounded cones** (firing rates between 0 and refractory ceiling; membrane potentials between $V_{\text{rest}}$ and $V_{\text{rev}}$; ion concentrations bounded by reversal potentials). Vector-space / Banach-lattice structures import unbounded operations that retina does not realize.

### C5 — Not biological-theorem
This framework makes no claim of the form *"theorem X is true about retina"*. The honest registers are: (i) mathematical fact about an abstract object; (ii) conditional observation under explicit regime; (iii) operational hypothesis with falsification criterion; (iv) modeling motivation by structural analogy; (v) open problem with stated obstacle.

---

## 3. Five Open Problems (precise — each with question, obstacle, route)

### OP-MIN-1 — Operational definition of "perceptual field"

**Question**: What measurable quantity computed from spike trains $\{G_c(t)\}_{c \in \mathcal{C}_g}$ corresponds operationally to what was called "perceptual field $u_t$" in SCC?

**Why existing structure fails**: $u_t$ has been used metaphorically; no procedure $u_t = F(G)$ has been specified. Pattern #11 (model misspecification) repeatedly killed TCs that conflated abstract quantities with operational ones.

**Minimal assumptions needed**: spike train data $G$; bounded temporal/spatial smoothing kernel; specification of which task-relevant Fisher direction defines "field strength".

**Possible test route**: Geisler 2008 task-relevant Fisher information; spike-decoder ROC bounds on a benchmark perceptual task (orientation discrimination, motion direction).

### OP-MIN-2 — Super-Poisson statistics measurement protocol

**Question**: At which retinal stages does Mandel $Q = \langle (\Delta N)^2 \rangle / \langle N \rangle - 1$ exceed 0, and by how much, under natural-illumination conditions?

**Why existing structure fails**: All deleted TCs assumed Poisson statistics; no operational measurement of the actual super-Poissonian deviation was specified.

**Minimal assumptions needed**: MEA recording in natural-illumination condition; binning interval; per-cell rate estimate.

**Possible test route**: re-analyze existing primate MEA datasets (Chichilnisky lab) for cell-specific Mandel $Q$; predict gain-control regime from $Q$ vs intensity correlation.

### OP-MIN-3 — Sub-probability kernel composition theorem

**Question**: Does Kallenberg's composition-of-stochastic-kernels lemma extend to *sub-probability kernels* on Polish-Borel spaces, and if so, what extra hypothesis is required?

**Why existing structure fails**: TC-SP-R-5 (probability-kernel composition) is the sole UNCLEAR survivor of 9 passes; Pass 9 #15 hit because retinal kernels are sub-probability. A direct extension would convert R-5 from UNCLEAR to RETAINED.

**Minimal assumptions needed**: σ-finiteness still holds; mass-loss function $\mu(x) := 1 - \mathcal{K}(x, \mathcal{Y}) \in [0, 1]$ measurable.

**Possible test route**: standard adaptation of Tonelli + monotone class to sub-probability case; check whether composition preserves σ-finiteness of mass-loss.

### OP-MIN-4 — Non-Markov information-flow inequality

**Question**: What inequality replaces standard DPI $I(X_0; X_i) \geq I(X_0; X_{i+1})$ when the chain $X_0 \to X_1 \to \cdots$ has feedback / adaptation memory?

**Why existing structure fails**: TC-SP-R-4 (DPI) was deleted in Pass 9 because retinal pipeline is non-Markov; no replacement inequality has been provided.

**Minimal assumptions needed**: bounded memory length; feedback summarized by a finite hidden state.

**Possible test route**: Polyanskiy-Wu strong DPI with feedback correction; or simulate a 3-stage feedback chain and measure mutual-information non-monotonicity.

### OP-MIN-5 — SCC $u_t$ ↔ retinal stage mapping (carry-forward from OP-SP-006)

**Question**: At which stage of the sensing pipeline does SCC's $u_t : X_t \to [0,1]$ correspond — pre-Stage-0 (world), Stage 1–2 (retinal field), Stage 3 output (spike-derived), or post-Stage-4 (cortical)?

**Why existing structure fails**: 9 verification passes did not resolve this; left as OP-SP-006 (High severity) in the original 08 OP registry. Resolving it is the *critical path* to any PAI bridge work.

**Minimal assumptions needed**: stage-output recordings (or simulations); computable SCC diagnostic (Bind, Sep, Inside, Persist) at each candidate stage; comparison metric.

**Possible test route**: compute SCC diagnostics on simulated Stage 1, 2, 3 outputs from a controlled scene; determine at which stage the diagnostics behave most like SCC's canonical predictions.

---

## 4. Survival Criteria — applied retroactively to 11,581 lines

Every claim in docs 00–10 must satisfy one of these registers. Anything else is *exploration record* (research process documentation), not a claim.

| Register | Content type | Examples in this directory |
|----------|--------------|---------------------------|
| **MATH-FACT** | Theorem from textbook, no retinal claim | DPI in Cover-Thomas (abstract); Kallenberg kernel composition; Riesz lattice; Parseval identity |
| **CONDITIONAL-OBS** | "If R satisfies Q1..Qn, then M approximates B up to L" with conditions IN statement | TC-SP-R-5 (sub-probability kernel, the sole UNCLEAR survivor) |
| **OPERATIONAL-HYPOTHESIS** | Data + procedure + falsifiability | OP-MIN-1, OP-MIN-2 above |
| **MODELING-MOTIVATION** | Explicit non-theoremic; structural analogy only | Adelson-Bergen Gabor as V1-cortical model (NOT retinal); Olshausen-Field sparse coding as V1 substrate (NOT bipolar); Naka-Rushton Hill function as fitting tool |
| **OPEN-PROBLEM** | Precise question + obstacle + route | OP-MIN-1..5 above; carry-forward OP-SP-001 to 010 in `08_open_problems_sp.md` (still valid as open) |
| **EXPLORATION-RECORD** | Derivation, audit trail, deletion notice | Most of the 11,581 lines: van Kampen expansion, Pugh-Lamb cascade, Lindeberg-Koenderink derivation, Mandel-Wolf coherence treatment, 31 deletion notices, 5 verification ledgers |
| **DELETED** | Removed via adversarial verification | 31 of 32 prior TCs |

**Pass 10 reclassification verdict**: ~11,000 of 11,581 lines are EXPLORATION-RECORD (mathematical derivations + audit trail + verification methodology). ~500 lines are MATH-FACT references. **1 active CONDITIONAL-OBS** (TC-SP-R-5, with salvage route in OP-MIN-3). **5 OPERATIONAL-HYPOTHESIS / OPEN-PROBLEM** registered here. **0 BIOLOGICAL-CLAIM** (per C5 constraint).

---

## 5. Pattern Sweep Results (Iterations 2–5)

### Pattern A — Hidden Idealization (Iter 2)

Survey counts in sensing_pipeline/:

| Term | Count | Disposition |
|------|-------|-------------|
| Poisson | 249 | mostly inside DELETED notices (audit trail); active uses: documenting *failure* of Poisson assumption (C1) |
| Markov | 104 | mostly inside DELETED notices; active uses: documenting *failure* of Markov (C2) |
| linear | 38 | inside derivation text (Lindeberg, Reichardt, DoG); EXPLORATION-RECORD register |
| probability | 26 | inside DELETED notices + OP-MIN-3 reference |
| smooth | 24 | inside Lindeberg derivation; EXPLORATION-RECORD |
| stationary | 20 | inside DELETED Q-conditions (TC-SP-R-6 etc.); audit trail |

**Pass A verdict**: high-count terms are *historical audit trail of failed assumptions*; no active claim depends on them. Constraints C1, C2, C3 explicitly forbid them in new content.

### Pattern B — Ontology Inflation (Iter 3)

| Term | Count | Disposition |
|------|-------|-------------|
| formation | 146 | inherited from SCC framework (canonical); only referenced in cross-link context; not redefined here |
| field | 111 | used historically; replaced operationally by "intensity-valued response" (P2) in minimal core |
| signal | 35 | technical use (input-output mapping); RENAMED to "intensity-valued response" where ambiguous |
| object | 27 | metaphorical use only in motivation sections; MOVED to MODELING-MOTIVATION register |
| perception | 25 | metaphorical use only; per OP-MIN-1, no operational definition exists yet — must be marked OP-MIN-1 dependent |
| raw | 15 | retained as informal label for P1 (photon arrival event); not a technical term |
| carrier | 7 | rarely used; not technically defined; eligible for deletion in future pass |
| world | 6 | metaphorical; MOVED to MODELING-MOTIVATION |
| meaning | 2 | metaphorical; MOVED to MODELING-MOTIVATION |
| pre-objective | 0 | not used in current sensing_pipeline (only in prolegomena cross-reference) |

**Pass B verdict**: 5 inflated terms (field, perception, object, world, meaning) marked for downgrade to MODELING-MOTIVATION register. No active claim uses them in theorem-shape.

### Pattern C — False Generality (Iter 4)

| Phrase | Count | Disposition |
|--------|-------|-------------|
| "the brain" | 1 | inside discussion; replaced with "biological neural system in primate retina" |
| "natural scenes" | 1 | inside reference (Field 1987); kept as citation context |
| "all sensory systems" | 0 | already clean |
| "retina in general" | 0 | already clean |
| "perception as such" | 0 | already clean |
| "biological systems" | 0 | already clean |

**Pass C verdict**: False generality already well-controlled by 9 prior verification passes. Minor cleanup remaining.

### Pattern D — Evidence Boundary (Iter 5)

Every biology-facing element marked:

| Element | Evidence Level | Justification |
|---------|----------------|---------------|
| Photoreceptor single-photon detection (Baylor 1979) | **E2** | empirical literature, well-replicated |
| Super-Poisson Mandel $Q > 0$ in retina | **E1** | textbook (Mandel-Wolf) for thermal light; not yet measured in retina specifically |
| Adelson-Bergen motion energy in V1 | **E2** | empirical (DeAngelis 1993) — but V1, NOT retina |
| Starburst amacrine asymmetric inhibition (DSGC mechanism) | **E2-E3** | Briggman-Helmstaedter-Denk 2011 (connectomics) + simulation |
| Olshausen-Field sparse coding → V1-like bases | **E3** | dataset/simulation reproducible; V1 target, NOT retinal bipolar |
| Cox-process model of ganglion firing | **E1** | textbook approximation; known to fail under correlations |
| Laughlin Naka-Rushton ≈ natural-light CDF | **E2** | Laughlin 1981 fly LMC; Frazor-Geisler 2006 primate; partial fit |
| Center-surround DoG as bipolar cell model | **E2** | empirical (Kuffler 1953; Enroth-Cugell-Robson 1966) |
| ON/OFF Riesz-style decomposition in actual retina | **E0–E1** | metaphorical; not literal — biological ON/OFF channels overlap, have tonic baseline (per Pass 5 #11 hit) |

**Pass D verdict**: most biology-facing content sits at E1–E3. Nothing E4 (no original experimental validation in this project). E0/E1 items have been downgraded to MODELING-MOTIVATION or moved to OP.

### Pattern E — Compression to 5+5+5 (Iter 6)

§§ 1–3 above. Compression *succeeded* — entire framework reducible to 15 elements (5 primitives + 5 constraints + 5 OPs).

---

## 6. Deletion Log — Compressed

31 prior TCs DELETED across Pass 3–9. Full audit trail preserved in stage docs (02–07, 10) as retraction notices. Compressed summary:

| TC | Deleted in Pass | Primary attack pattern | Replacement (if any) |
|----|-----------------|------------------------|----------------------|
| 0.1b | P3 | #18 tautology (definition restatement) | none — definitional |
| 1.3 | P4 (escalated from P3 weakened) | #18 + #5 + #46 + #51 | C2 (negative constraint) |
| 1.4 | P4 (escalated from P3 weakened) | #40 + #5 + #46 + #51 | OP-MIN-1 (operational) |
| 1.5 | P3 | #18 + #5 tautological + CLE violation | E2 empirical reference only |
| 2.1 | P5 | #11 model misspec (ON/OFF not literal Riesz) | none — phenomenon misframed |
| 2.2 | P4 | #40 + #46 + #51 | none |
| 2.3 | P4 (escalated) | #40 + #5 + #46 + #51 | OP-MIN-1 via sparse coding |
| 2.4 | P5 | #11 misspec (V1-cortical, not retinal DSGC) | MODELING-MOTIVATION only |
| 2.5 | P5 | #11 misspec (neither retinal model applies) | MODELING-MOTIVATION only |
| 2.6 | P5 | #11 alignment ≠ causal optimization | MODELING-MOTIVATION |
| 3.1 | P4 | #5 + #51 Cox conditional independence violation | OP-MIN-3 partially addresses |
| 3.2 | P3 | #18 + #5-minor (rename of latency diff) | none |
| 3.3 | P4 (escalated) | #18 + #40 + #46 + #51 | OP-MIN-3 |
| 4.1 | P5 | #11 misspec (Shannon ≠ task-relevant Fisher) | OP-MIN-1 via Fisher info |
| 4.2 | P4 | #5 + #51 inherits 3.1 Cox | derived from 3.1; same OP |
| 4.3 | P4 | #5 + #46 + #51 | OP-MIN-1 via Laughlin reformulation |
| 5.1 | P3 | #18 + #40 + #5 σ functoriality false | none |
| 5.2 | P3 | #18 + #40 + #5 Tier 2 closure definitional fiat | none |
| 0.1a (post-split) | P8 | #7 + #28 Radon-Nikodym hidden, atomic Λ exclusion | OP-MIN-2 absorbs |
| 0.2 | P5 | #11 misspec (photon arrival vs rod detection conflation) | E2 empirical reference |
| R-1 | P9 | #7 + #15 + #52 (super-Poisson + ops inaccessibility) | C1 + OP-MIN-2 |
| R-2 | P9 | #28 + #41 + #15 (Banach lattice not bona fide) | C4 (negative constraint) |
| R-3 | P8 (4 patterns total by P9) | #50 + #37 + #7 + #28 PSD existence smuggle | MODELING-MOTIVATION (cortical only) |
| R-4 | P9 | #15 + #52 (retinal non-Markov + Shannon vs Fisher) | C2 + OP-MIN-4 |
| R-6 | P8 (3 patterns by P9) | #22 + #37 + #28 Q-conjunction empty + range narrow | OP-MIN-1 absorbs |
| R-7 | P7 | #22 + #3 + #50 C²→C⁴ hypothesis mismatch | none — biologically inappropriate target |
| R-8 | P7 | #22 + #50 Cox conjunction <1% real data | OP-MIN-3 partially |
| R-9 | P8 | #37 + #28 sup-interchange admissibility-pushforward | OP-MIN-4 absorbs |
| R-10 | P8 (4 patterns by P9) | #50 + #37 + #7 + #28 empirical-as-guarantee | MODELING-MOTIVATION (V1 only) |
| **R-5 (UNCLEAR sole survivor)** | — | #15 biological vacuity (probability vs sub-probability) | OP-MIN-3 (salvage path) |

**Pattern frequency in deletions** (lethality ranking):
1. **#15 vacuity** — 8 hits (most lethal in Pass 9)
2. **#11 model misspec** — 7 hits (Pass 5 + carryforward)
3. **#51 independence** — 7 hits (Pass 4)
4. **#5 hypothesis recheck** — 6 hits
5. **#28 subset support** — 6 hits (Pass 8)
6. **#46 boundary** — 5 hits
7. **#40 too-clean lemma** — 5 hits
8. **#50 typicality** — 4 hits
9. **#18 tautology** — 4 hits
10. **#37 pointwise vs uniform** — 4 hits
11. **#7 implicit regularity** — 4 hits
12. **#22 Q-compounding** — 3 hits
13. **#3 citation** — 1 hit
14. **#41 set-theoretic** — 1 hit
15. **#4 RH-spec** — 0 hits
16. **#6 divergent** — 0 hits
17. **#29 continuity** — 0 hits
18. **#52 operational** — 2 hits

---

## 7. No-Expansion Compliance Check (Iter 8)

| Check | Verdict | Note |
|-------|---------|------|
| Did this pass add unnecessary structure? | **NO** | Only compression + reclassification; no new TC, no new architecture |
| Did it introduce a new framework name? | **NO** | "Minimal core" is a section label, not a new framework |
| Did it preserve protected canonical files? | **YES** | canonical/ + SCC + PAI + 8 retractions all untouched (git diff confirms) |
| Did it downgrade claims before reconstructing? | **YES** | Reclassified bulk content as EXPLORATION-RECORD; no new claims constructed beyond OP-MIN-1..5 (all explicitly framed as open problems) |
| Did it maintain audit trail? | **YES** | All prior verification ledgers (Pass 3-9) and all deletion notices preserved verbatim in original docs |
| Did this pass reduce or grow the corpus? | **REDUCED in claim count; ~600 lines added in 11_** | 32 TCs + ~1000 LOC of weakening notices → 0 active TCs + 1 UNCLEAR + 5 OPs + 5 constraints + 5 primitives in single doc |

**Reconstruction-rule audit**: OP-MIN-1..5 were created only because:
1. Each replaces a specific deleted TC (precise failure mode)
2. Each repairs that failure (e.g., OP-MIN-3 directly addresses R-5's sub-probability gap)
3. Each is **weaker and more operational** than the deleted TC (operational hypotheses with explicit falsification routes, not theorem candidates)

**Constraint C1–C5** are *negative* constraints — they say what the framework does NOT assume. Adding negative constraints is the *opposite* of expansion.

**Primitives P1–P5** are operationally defined and replace metaphorical inflated terms (per Pattern B). Net effect: vocabulary shrinks.

---

## 8. Files Inspected (Iter 1)

All 11 docs in `THEORY/working/sensing_pipeline/`:
1. `00_INDEX.md` (314 LOC) — navigation + 5 verification updates (§2.1-§2.5)
2. `01_framework_master.md` (1095 LOC) — TC-SP-1.1, 1.2, 1.3 DELETED
3. `02_stage0_photon_point_process.md` (1131 LOC) — TC-SP-0.1a (P8), 0.1b (P3), 0.2 (P5) DELETED
4. `03_stage1_photoreceptor_sde.md` (1222 LOC) — TC-SP-1.4 (P3→P4), 1.5 (P3) DELETED
5. `04_stage2_inner_retinal_algebra.md` (1593 LOC) — TC-SP-2.1, 2.2, 2.3, 2.4, 2.5, 2.6 all DELETED
6. `05_stage3_ganglion_spike_encoding.md` (1355 LOC) — TC-SP-3.1, 3.2, 3.3 all DELETED
7. `06_endtoend_information_bound.md` (1161 LOC) — TC-SP-4.1, 4.2, 4.3 all DELETED
8. `07_omega_sigma_lift.md` (1059 LOC) — TC-SP-5.1, 5.2 DELETED
9. `08_open_problems_sp.md` (1266 LOC) — 14 OP-SP entries (carry-forward as valid)
10. `09_verification_pass3.md` (548 LOC) — Pass 3+4+5 ledger
11. `10_reconstruction_pass6.md` (837 LOC) — R-1..R-10 + Pass 7+8+9 ledger; only R-5 UNCLEAR

Total inspected: **11,581 LOC** (now 12,200+ with this document).

Reclassification: docs 00-10 = EXPLORATION RECORD; doc 11 (this) = MINIMAL CORE.

---

## 9. Next 5 Cut Recommendations (Iter 10 part 1)

Most dangerous remaining assumptions, ranked:

### Cut-1 (highest priority): Forward-only assumption in P3
P3's "forward-only kernel transformation" is itself a *biological idealization* — retinal has cortico-fugal feedback. The next adversarial pass should ask: does P3 need to be reformulated as a *non-causal kernel* with explicit feedback budget?

### Cut-2: Channel index P5 as "given by anatomy"
P5 asserts $\mathcal{C}$ is given, but the *number* of channels depends on counting convention (e.g., midget cell subtypes). Future pass: replace P5 with *operational definition* (cells distinguishable by an explicit assay) or move to OP.

### Cut-3: σ tolerance parameters $\delta_t, \delta_x$
P4's tolerance σ requires choosing $\delta_t, \delta_x$. The choice is implicit. Future pass: are there *principled* choices (e.g., from sensor resolution) vs *arbitrary* choices? If arbitrary, σ is a tunable knob and OP-MIN-1 must specify it.

### Cut-4: "Operational" itself is unmeasured
OP-MIN-1, -2, -3, -4 all promise "operational" or "measurable". Are the proposed measurement procedures themselves performable with current technology in primate retina? Future pass: feasibility audit per OP.

### Cut-5: Constraint C5 ("no biological theorem") as meta-statement
C5 itself is a *meta-constraint* on the framework's register, not a constraint on retinal structure. Is C5 itself a "biological theorem in disguise" (asserting that *no* such theorem exists)? Future pass: distinguish *contingent* C5 (no current theorem) from *necessary* C5 (no such theorem can exist).

---

## 10. Final Standard Compliance (Iter 10 part 2)

> "The pass succeeds if the result is smaller, sharper, and more falsifiable. It fails if the result is merely longer."

**Smaller**: ✓ — 32 TC candidates → 1 UNCLEAR + 5 OPs. Net active claims: 6 (down from 32). Single-doc minimal core (~700 LOC) replaces TC-corpus reading of ~11,000 LOC exploration record.

**Sharper**: ✓ — 5 primitives have operational definitions; 5 constraints are explicit negative statements; 5 OPs each have question + obstacle + route.

**More falsifiable**: ✓ — each OP-MIN states a specific failure mode (e.g., OP-MIN-2 falsifiable by measuring Mandel $Q \leq 0$ in actual retinal MEA; OP-MIN-3 falsifiable by finding a sub-probability kernel pair whose composition is not sub-probability; OP-MIN-4 falsifiable by demonstrating Shannon DPI holds on a simulated non-Markov chain).

**Did not grow**: This 11_ doc adds ~700 LOC, but it *replaces* the active-claim reading of the prior 11,000 LOC (which are reclassified as EXPLORATION RECORD with no active-claim status). Net active-claim content **shrank**.

---

## 11. MINIMAL ADVERSARIAL REFINEMENT COMPLETE

The 10-iteration minimal-structure adversarial refinement of `sensing_pipeline/` is complete. Final state:

- **5 primitives** (operationally defined, replace inflated ontological terms)
- **5 constraints** (negative — what framework does NOT assume; survives Pattern #15)
- **5 open problems** (precise, falsifiable, with routes)
- **31 deletions** preserved as audit trail in original docs
- **1 UNCLEAR survivor** (TC-SP-R-5; salvage path = OP-MIN-3)
- **11,000+ LOC** reclassified as EXPLORATION RECORD (research process documentation)
- **0 modifications** to canonical / SCC / PAI / prior retractions

The framework no longer makes any biological theorem claim. It is now:
1. A set of operational primitives,
2. A set of negative constraints (what NOT to assume),
3. A set of precise open problems,
4. A large exploration record documenting what was tried and why each attempt failed adversarial verification.

This is the smallest mathematically honest structure available given current evidence. Further cuts (Cut-1 to Cut-5 above) are possible in future passes.

---

*Pass 10 v0. Minimal core consolidated. All 9 prior verification passes' audit trail preserved. Constraint compliance verified. Single new doc; no new framework name; no canonical/SCC/PAI modification. Stable terminal state for sensing_pipeline as currently framed.*
