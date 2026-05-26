---
type: working/sensing_pipeline/pass12_operational_test_protocols
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase C (Tasks 11-15)
purpose: |
  Detailed operational protocols for the 4 falsification tests defined in 12_ Iter 16,
  plus survey of existing datasets that could enable execution without new experiments.
  Each protocol specifies: paradigm, measurement procedure, expected effect, falsification trigger.
register: PROTOCOL (not yet executed)
parent: 00_INDEX
prev: 14_field_equation_verification
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  protocols_specified: 4 + dataset survey
  protocols_executed: 0 (Pass 12 = protocol design only; execution requires separate plan)
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[14_field_equation_verification]] · Pass 12 Phase C

# Pass 12 Phase C — Operational Test Protocols (Tasks 11-15)

**Scope**: convert Iter 16's 4 test definitions from *sketches* into *executable protocols* with explicit parameters, predictions, and falsification triggers. Plus identify existing primary-data sources that could enable execution without new experiments.

**Inherited caveats** (from Phases A-B):
- σ is graded near threshold band (Task 1) — predictions must accommodate probabilistic boundary
- Stage-table $c_p^{(s)}$ values need correction (Task 2) — use Task 2 corrected values
- Linear regime matches DoG conditionally, not motion-energy (Task 9) — Test 3 (curvature ↔ binding variation) is the cleanest test of the *non-trivial* PFE content

---

## Task 11 — Test 1 detailed protocol ($c_p^{(s)}$ stability)

### Hypothesis tested
P2 (existence of single rate per stage) plus convention-fix from Task 2: within consistent definition of $\tau$ (characteristic time constant) and $\ell$ (characteristic spatial correlation length), $c_p^{(s)}$ is *stable* across recording sessions within a single individual.

### Falsification trigger
If measured $c_p^{(s)}$ varies by *more than 10× across recordings* within the same individual + same condition + same stage, P2 is refuted. If variance is 2-10×, P2 is *weakened* but salvageable with explicit error bars.

### Paradigm

**For stage 3 (M ganglion) — most accessible in MEA recordings**:

1. **Recording substrate**: Multielectrode array (MEA) recording from isolated primate or salamander retina, with full-field photographic projection
2. **Stimulus**: White noise checkerboard, refresh rate ≥ 60 Hz, contrast ≥ 50%, duration ≥ 20 min
3. **Extraction of $\tau_s$**:
   - Spike-triggered average (STA) per cell → biphasic temporal kernel
   - $\tau_s := $ peak-to-zero crossing time of STA (a *consistent* convention; avoids the membrane-vs-onset ambiguity of Task 2)
4. **Extraction of $\ell_s$**:
   - Spike-triggered covariance (STC) per cell → spatial receptive field
   - $\ell_s := $ 1σ Gaussian fit radius of RF center (consistent convention)
5. **Compute $c_p^{(s)} := \ell_s / \tau_s$ per cell**
6. **Aggregate**: across cells of the same type (e.g., M parasol), across sessions of the same individual, compute:
   - Cell-to-cell variance
   - Session-to-session variance (same individual)
   - Inter-individual variance (excluded — P2 is within-individual)

### Predicted value (Task 2 corrected)

For M parasol cells in primate retina:
- Expected $\tau_s \approx 5-15$ ms
- Expected $\ell_s \approx 100-300$ μm at 10° eccentricity
- Expected $c_p^{(s)} \approx 7-60$ mm/s (factor of ~8 spread from RF size variation alone)

**This is right at the falsification edge** — a factor of ~8 from RF-size variation alone, before accounting for measurement noise. If actual variation is more, hypothesis fails.

### Mitigation: eccentricity stratification

Stratify cells by eccentricity (e.g., 5°, 10°, 15°, 20° rings). $c_p^{(s)}$ should be *approximately constant within an eccentricity ring*, varying systematically with eccentricity (matching $\ell_s$ scaling).

Refined falsification: within a 5° eccentricity ring, $c_p^{(s)}$ variance >3× refutes "single rate per stage at fixed eccentricity".

### Effort estimate
- MEA data acquisition: ~weeks per session, hundreds of cells
- STA/STC extraction: standard analysis pipeline (Chichilnisky lab, Pillow lab toolboxes)
- Stratification + statistics: ~1 week of analysis given recorded data

### Likely outcome

**Estimated**: WEAKEN (factor 3-5 variation within eccentricity ring is plausible given cell-type heterogeneity). FAIL (>10× variation) is unlikely because RF measurements are robust.

---

## Task 12 — Test 2 detailed protocol (cone ↔ binding)

### Hypothesis tested
σ-as-cone (Iter 3, weakened to fuzzy edge by Task 1): for events with $|c_p \Delta t| - |\Delta x|$ far from zero, perceptual binding is *binary* (strong inside cone, none outside). Near the boundary, binding is *graded*.

### Falsification trigger
If perceived binding strength is *uncorrelated* with cone membership at any cone-membership value (not just at threshold), the σ-as-cone hypothesis fails. Specifically: if perfectly inside-cone stimuli show *less* binding than outside-cone stimuli for some configuration, the hypothesis is refuted.

### Paradigm: Apparent motion psychophysics

1. **Stimulus**: Two-flash apparent motion. Flash 1 at position $(t_1, x_1)$, flash 2 at $(t_2, x_2)$.
2. **Parameters to vary**:
   - $\Delta t := t_2 - t_1$: 20, 50, 100, 200, 500 ms (5 values)
   - $\Delta x := |x_2 - x_1|$: 0.5°, 1°, 2°, 5°, 10° (5 values)
   - Grid: 25 stimulus pairs
3. **Stage-specific cone**: Choose the *attentional* stage (Stage 5, $c_p \approx 0.3$ m/s after Task 2 correction)
   - At viewing distance 50 cm, 1° ≈ 0.87 cm on retina
   - Cone boundary $c_p \Delta t = \Delta x$ at attention: $\Delta x = 0.3 \cdot \Delta t$ in m·s units
4. **Binding measure**:
   - 2AFC: "did you see one moving object or two flashes?"
   - Subjective rating (1-5): "how strong is the motion sensation?"
   - Both measures, average across 50 trials per condition

### Expected result

Define normalized cone-distance $d := (c_p \Delta t - \Delta x) / \sigma_{\text{boundary}}$ where $\sigma_{\text{boundary}}$ is the width of the threshold band (~ Task 1's 15-25% variance scale).

- $d \gg 1$: deeply inside cone → binding ≈ 1 (strong motion)
- $d \approx 0$: at boundary → binding ≈ 0.5 (graded)
- $d \ll -1$: deeply outside cone → binding ≈ 0 (no motion)

Plot expected: sigmoidal binding probability vs $d$.

### Falsification trigger (precise)

Fit logistic regression $P[\text{bind}] = \sigma(\alpha + \beta d)$. Hypothesis predicts $\beta > 0$ and the *zero-crossing of $\alpha + \beta d$ aligns with $d = 0$* (i.e., cone boundary).

- If $\beta < 0$ (binding *anti-correlates* with cone), hypothesis refuted
- If $\beta > 0$ but zero-crossing is at $d > 0.5$ or $d < -0.5$ (boundary shifted by >50% of band width), hypothesis weakened (cone boundary location wrong; $c_p^{(s)}$ value needs revision)
- If $\beta > 0$ and zero-crossing within ±0.5 of $d = 0$, PASS

### Effort estimate
- Standard psychophysics protocol
- ~5 subjects × 25 conditions × 50 trials = 6,250 trials total
- ~10 hours per subject
- Standard apparatus (CRT or OLED display, button-box)

### Likely outcome
**Estimated**: PASS likely for Korte-regime stimuli (well-studied; binding does correlate with motion-perception cone). The novelty is computing the *quantitative* cone boundary via Task 2 corrected $c_p$ values. If the corrected $c_p$ value gives the right zero-crossing, PFE gets *quantitative* support.

---

## Task 13 — Test 3 detailed protocol (curvature ↔ binding variation)

### Hypothesis tested
PFE Iter 7's curvature-as-binding-strength-variation hypothesis: in regions where $c_p^{(s)}(x)$ varies (e.g., across foveal-to-peripheral transition), Ricci scalar $R^{(s)}(x)$ should *predict* the spatial variation in binding strength.

### Falsification trigger
If binding strength is *uniform* across regions of different computed curvature (i.e., uncorrelated with $R^{(s)}$), hypothesis refuted. Specifically: linear regression of binding strength on $R^{(s)}$ has |slope coefficient| < 0.1 standard-error units (no signal).

### Paradigm: Eccentricity-dependent psychophysics

1. **Map $c_p^{(s)}(x)$ across eccentricity**:
   - Use Test 1 data (if available) to extract $c_p^{(s)}$ at multiple eccentricities (0°, 5°, 10°, 20°, 40°)
   - For human subjects: use published M-cell RF + temporal kernel data
2. **Compute curvature**:
   - Approximate metric: $g_{\mu\nu}(x) = \text{diag}(-c_p^{(s)}(x)^2, 1, 1)$ (position-dependent rate, otherwise flat)
   - Christoffel symbols depend on $\partial c_p / \partial x$
   - Ricci scalar $R^{(s)}(x) \sim (\partial_x c_p)^2 / c_p^2$ + similar terms
   - Compute numerically at each eccentricity sampling point
3. **Measure binding strength at each eccentricity**:
   - Apparent motion 2AFC paradigm (same as Test 2)
   - Fixed $\Delta t = 50$ ms (within cone at all stages)
   - $\Delta x$ scaled with eccentricity (preserve angular size)
   - Binding strength = P[bind] per eccentricity
4. **Compute "binding variation"**:
   - $\Delta \text{Bind} := |P[\text{bind}](e_2) - P[\text{bind}](e_1)|$ for adjacent eccentricities $e_1, e_2$
   - Compare to $|R^{(s)}(e_1)|$ averaged over the interval

### Expected result

Curvature is *highest* at the fovea-periphery transition (~5-10° eccentricity, where $c_p^{(s)}$ changes most rapidly). Binding-strength change should be *largest* there.

Predicted correlation: $\rho(\Delta \text{Bind}, |R^{(s)}|) > 0.5$ across eccentricity samples.

### Falsification trigger (precise)
- $\rho < 0.2$: weak/no signal — hypothesis weakened
- $\rho < 0$: hypothesis refuted (anti-correlation means binding is *smoothest* at high curvature, opposite of prediction)
- $\rho > 0.5$: PASS

### Caveats
- $c_p^{(s)}$ also varies systematically with eccentricity for non-PFE reasons (RF size grows ~linearly with eccentricity, known retinal anatomy). So *trivially* binding varies with eccentricity. The *novel* PFE prediction is that *binding-variation* tracks *curvature*, not just $c_p$ or RF size.
- Need to control for raw RF-size effect: fit binding ~ RF-size as baseline, then check if residual binding correlates with curvature.

### Effort estimate
- Test 1 data: months if new MEA, days if existing dataset (Task 15)
- Psychophysics: same as Test 2, but with eccentricity manipulation
- Total: 2-4 weeks given Test 1 data

### Likely outcome
**Estimated**: WEAKEN or PASS. The eccentricity-binding gradient is known empirically. Whether it tracks Ricci scalar specifically (vs just RF size) is unknown. This is the *cleanest novel* PFE test — distinguishes PFE from naive RF-based theories.

---

## Task 14 — Test 4 detailed protocol (multi-stage intersection ↔ unification)

### Hypothesis tested
Multi-stage cone framework (Iter 5): events $\{e_1, \ldots, e_n\}$ are perceived as a *unified object* iff they lie in $\bigcap_s \mathcal{C}^{(s)}$ (intersection of all stage cones).

### Falsification trigger
- If multi-event stimuli that *fail* the intersection-cone connectivity are *still* perceived as unified, hypothesis refuted (too restrictive)
- If multi-event stimuli that *pass* intersection-cone connectivity are *not* perceived as unified, hypothesis refuted (insufficient)

### Paradigm: Object segmentation with controlled spatiotemporal structure

1. **Stimulus**: Configurations of 4-8 brief flashes at controlled $(t_i, x_i)$
2. **Two configuration classes**:
   - **Cone-connected**: every flash pair $(e_i, e_j)$ lies in $\bigcap_s \mathcal{C}^{(s)}$ — i.e., within the *most restrictive* (slowest-stage) cone
   - **Cone-disconnected**: at least one pair lies outside the *most restrictive* cone but inside some other cone
3. **For each configuration, 2AFC task**: "did you perceive one object moving / one unified event, or multiple separate events?"
4. **Stage-most-restrictive choice**:
   - From Task 2 corrected values, Stage 1 (photoreceptor) has smallest $c_p \approx 0.05$ mm/s → most restrictive cone
   - Test stimuli at retinal sizes 5-50 μm at 50 cm viewing (use magnified display or high-resolution adaptive optics)
   - For human subject without adaptive optics: scale up to Stage 2 (~10 mm/s) most-restrictive — still operational

### Predicted result

P[unified | cone-connected] ≫ P[unified | cone-disconnected]

Specifically: predicted contrast index $\Delta := P[\text{unif}|\text{conn}] - P[\text{unif}|\text{disc}]$ should be > 0.3 (large effect).

### Falsification trigger (precise)
- $\Delta < 0.1$: hypothesis weakened (intersection-cone is not a strong determinant)
- $\Delta < 0$: hypothesis refuted (disconnected stimuli unify *more* than connected — backwards)
- $\Delta > 0.3$: PASS

### Caveats
- Multi-stage intersection is the *strictest* hypothesis. A weaker version: union of cones predicts unification — but this is *not* what PFE predicts. PFE predicts *all* stages must agree (intersection).
- Empirically: Gestalt grouping (common fate, proximity) is known to produce unification even without strict cone-membership. PFE-test must control for these confounds.

### Effort estimate
- Custom stimulus generation (carefully controlled $(t_i, x_i)$ configurations)
- ~5 subjects × 50 configurations × 30 trials = 7,500 trials
- ~15 hours per subject
- Analysis: 2 weeks

### Likely outcome
**Estimated**: WEAKEN. Gestalt confounds are strong; pure cone-intersection unlikely to be the dominant signal. Likely $\Delta \approx 0.1-0.2$ — significant but weak. Hypothesis survives but with caveat that *intersection-cone is one of several unification cues*.

---

## Task 15 — Existing dataset identification + accessibility

### Goal
Survey published datasets that could *enable Tests 1-4 without new experiments*. Tag each dataset by which test(s) it supports.

### Falsification trigger
If no public datasets exist for any test, all 4 tests require new experiments — substantially increasing cost (years of work + ethics + funding). If at least 2 tests have ready datasets, the framework is *practically testable* without major new investment.

### Survey

**Test 1 ($c_p^{(s)}$ stability) — MEA datasets**

1. **Chichilnisky Lab dataset (Stanford / Salk)**
   - Public release: partial via CRCNS (Collaborative Research in Computational Neuroscience)
   - Primate (macaque) retina, 60-channel MEA, white noise stimuli
   - Hundreds of identified cell types per recording
   - **Fit for Test 1**: YES — STA/STC standard pipeline; $c_p$ extraction is straightforward
   - URL: crcns.org/data-sets/retina/

2. **Berry Lab dataset (Princeton)**
   - Salamander retina (smaller cells, simpler stimuli)
   - Public via Berry lab website
   - **Fit for Test 1**: PARTIAL — different species; useful for sanity check but not human-relevant

3. **Pillow Lab simulations + recordings**
   - GLM-fit retinal neurons
   - Useful for model comparison; recordings on CRCNS
   - **Fit for Test 1**: YES — same as Chichilnisky

**Verdict for Test 1**: Multiple high-quality public datasets exist; Test 1 is *executable today* without new recordings.

**Test 2 (cone ↔ binding) — Psychophysics**

1. **Anstis apparent motion archive (1980s)**
   - Published parameters, not always raw data
   - Useful for *validating* the predicted boundary, not for primary fitting

2. **Burr & Ross motion energy datasets**
   - Some publications include trial-level data
   - **Fit for Test 2**: PARTIAL — useful for validation against the cone boundary, but the *quantitative* Test 2 protocol requires new psychophysics

3. **Open Psychophysics Database (various aggregators)**
   - Heterogeneous; quality varies
   - **Fit for Test 2**: PARTIAL — case-by-case

**Verdict for Test 2**: Partial dataset availability; new psychophysics likely needed for clean test but published data supports validation.

**Test 3 (curvature ↔ binding variation) — Eccentricity psychophysics**

1. **Levi & Klein crowding datasets (1980s-2000s)**
   - Eccentricity-dependent visual function
   - Available via Wertheim's compilations
   - **Fit for Test 3**: PARTIAL — measures different binding-like quantities; useful for cross-validation

2. **Robson & Graham (1981) contrast sensitivity vs eccentricity**
   - Standard eccentricity curves
   - **Fit for Test 3**: WEAK — different quantity (contrast sensitivity, not binding)

**Verdict for Test 3**: Limited dataset availability; needs new experiments tailored to motion-binding-vs-eccentricity question.

**Test 4 (multi-stage intersection ↔ unification) — Object segmentation psychophysics**

1. **Lee & Blake biological motion (point-light walker) datasets**
   - Multi-event unification (point-light figure perception)
   - Published parameters; some trial-level data
   - **Fit for Test 4**: WEAK — point-light walkers test biological-motion-specific unification, not generic cone-intersection

2. **Spelke object-formation infant studies**
   - Different paradigm (infants); not Test 4
   - **Fit for Test 4**: NO

**Verdict for Test 4**: Minimal dataset availability; will require dedicated new experiments.

### Summary table

| Test | Public dataset adequacy | New experiments needed? |
|------|--------------------------|--------------------------|
| Test 1 ($c_p^{(s)}$ stability) | HIGH (Chichilnisky CRCNS) | NO — executable today |
| Test 2 (cone ↔ binding) | PARTIAL | Likely YES for clean test |
| Test 3 (curvature ↔ binding variation) | LOW | YES — eccentricity-specific motion-binding |
| Test 4 (multi-stage intersection) | LOW | YES — dedicated paradigm |

### Verdict

**PASS** the data-availability gate for Test 1. **WEAKEN** for Tests 2-4 — partial dataset support; clean execution requires new experiments.

### Downstream consequence
- **Immediate Pass 13 priority**: Execute Test 1 on Chichilnisky CRCNS data. This is the *one* test with no new-experiment barrier. Provides immediate quantitative validation (or refutation) of $c_p^{(s)}$ stability.
- **Medium-term**: Design and pre-register Tests 2-4 psychophysics protocols. Estimated cost: $50K-100K + 1-2 years.
- **Long-term**: If Tests 1-4 collectively support PFE, the *attentional capture* prediction (Task 10, OP-PFE-10) becomes the next operational target.

### Effort distribution for full empirical program

| Test | Pass 13 cost | Years to results |
|------|--------------|------------------|
| 1 | Low (data exists) | 0.5 |
| 2 | Medium (subjects + apparatus) | 1 |
| 3 | Medium-High (custom paradigm) | 1.5 |
| 4 | High (custom paradigm + many subjects) | 2 |

---

## Phase C Summary

| Task | Target | Verdict | Confidence | Effect on framework |
|------|--------|---------|------------|---------------------|
| 11 | Test 1 protocol | PASS (protocol clear) | High | Executable with existing CRCNS data |
| 12 | Test 2 protocol | PASS (protocol clear) | High | Standard psychophysics; new subjects needed |
| 13 | Test 3 protocol | PASS (protocol clear) | Medium-high | Novel; cleanest test of curvature-specific PFE prediction |
| 14 | Test 4 protocol | PASS (protocol clear) | Medium | Vulnerable to Gestalt confounds; needs careful design |
| 15 | Dataset survey | PARTIAL | High | Only Test 1 immediately executable |

### Aggregate Phase C verdict

**PASS the protocol-readiness gate**. All 4 tests have *specific, executable protocols* with explicit falsification triggers. The framework is now *operationally testable in principle* — not merely *operationally framed* as in Pass 11.

**Empirical bottleneck**: Tests 2-4 require new experiments (months-years + funding). Test 1 alone is executable today.

### New OPs registered
- **OP-PFE-11**: Execute Test 1 on Chichilnisky CRCNS dataset; report $c_p^{(s)}$ distribution within stratified eccentricity rings. Highest immediate priority.

### Pass 11 framework status after Phase C

| Component | Pre-Phase-C | Post-Phase-C |
|-----------|-------------|--------------|
| Test 1 protocol | sketch (~3 lines) | full protocol with parameters, predictions, falsification triggers |
| Test 2 protocol | sketch | full 2AFC psychophysics protocol; 25-condition grid |
| Test 3 protocol | sketch | full eccentricity-stratified curvature-binding correlation protocol |
| Test 4 protocol | sketch | full 4-8-event configuration protocol; 50 configurations |
| Dataset path | not addressed | Test 1 via CRCNS today; Tests 2-4 need new experiments |
| Empirical priority | undefined | Test 1 first (zero-cost barrier) |

### What was NOT done in Phase C
- Tests 1-4 NOT executed (per discipline: Pass 12 = protocols only)
- No statistical power analysis (sample sizes are placeholders)
- No IRB / ethics consideration for new-experiment tests
- No pilot data collected
- No actual Chichilnisky-data download or pipeline run (defers to Pass 13)

---

*Phase C v0. 5 tasks, 5 verdicts. 4 operational test protocols specified, 1 dataset survey. Test 1 executable immediately via CRCNS. canonical/SCC/PAI/8-retractions 0 modifications. Next: Phase D OP-PFE Advancement (Tasks 16-20).*
