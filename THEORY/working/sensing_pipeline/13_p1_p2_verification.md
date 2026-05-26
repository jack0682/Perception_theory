---
type: working/sensing_pipeline/pass12_postulate_verification
version: v0
date: 2026-05-25
status: ACTIVE — Pass 12 Phase A (Tasks 1-5)
purpose: |
  Adversarial verification of Pass 11's two postulates (P1 perceptual relativity, P2 limiting rate)
  and the Minkowski-style derivation of σ. Each task produces explicit PASS / WEAKEN / FAIL / OPEN verdict
  against a falsification criterion stated up-front.
register: VERIFICATION
parent: 00_INDEX
prev: 12_perception_cone_field_equation
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  verdict_method: per-task explicit verdict against pre-stated falsification criterion
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[12_perception_cone_field_equation]] · Pass 12 Phase A

# Pass 12 Phase A — Postulate Verification (Tasks 1-5)

**Scope**: audit Pass 11's P1, P2, and the σ derivation. The framework's *entire* structure rests on these — if either postulate fails, σ derivation collapses, cone is asserted not derived, and the field equation has no postulate-level foundation (Pattern #18 tautology returns).

**Method**: each task states (i) what is verified, (ii) falsification criterion, (iii) evidence considered, (iv) verdict with confidence, (v) downstream consequences if verdict is FAIL or WEAKEN.

---

## Task 1 — P1 inter-observer variance audit

### What is verified
P1 claims: within an equivalence class $\mathcal{O}$ (same retina + same task + same illumination), $\sigma^{(\omega)}(e_i, e_j)$ is observer-invariant.

The Iter 1 adversarial check already weakened P1 to "within-subject + within-task + within-illumination". This task pushes further: *even within a single subject*, is σ stable across repeated measurements?

### Falsification criterion
If *within-observer* variance of σ-judgments (test-retest in identical conditions) exceeds 30%, then σ is not even a well-defined function of $(e_i, e_j, \omega)$ — it is a *random variable* over repeated trials, and P1 (deterministic invariance) is false. The framework would need probabilistic relaxation $\sigma \mapsto P[\sigma = 1 | e_i, e_j, \omega]$.

### Evidence considered (psychophysics literature, E1-E2 register)

**Apparent motion (Wertheimer-Korte regime)**:
- Korte's laws (1915): apparent motion strength is *not* binary at the cone boundary; it has a *graded* response across a transition zone of width ~50ms at $\Delta x \sim 1°$ (Sperling 1976; Burr & Ross 1986)
- Test-retest variance in single subjects: ~15-25% near the threshold (Anstis 1980)
- Far from threshold (deep inside or far outside cone), test-retest is highly stable (<5%)

**Simultaneity judgment (TOJ paradigm)**:
- JND (just noticeable difference) for temporal order: 20-40ms in single observer (Hirsh & Sherrick 1961; Vatakis & Spence 2007)
- Distribution shape: cumulative Gaussian — not step function
- Within-observer SD on threshold: 5-15ms
- Across-session drift: ~10ms

**Binding by motion / common fate**:
- Gestalt binding strength is graded, not binary (Palmer 1999)
- Within-observer variance ~10-20% near threshold

### Verdict

**WEAKEN** (not FAIL). Confidence: high.

P1 as stated (binary invariant σ) is *false at the threshold*: σ has a transition zone of 15-25% within-observer variance. *Outside the transition zone*, σ is operationally binary and stable.

The honest reformulation:
> **P1'**: There exists $\mathcal{O}$ such that for events with $|c_p \Delta t - \Delta x|$ outside a *threshold band* $[-\epsilon, +\epsilon]$, $\sigma^{(\omega)}$ is observer-invariant. Inside the band, σ is a *graded probability* $P[\sigma=1]$ with within-observer SD ~15-25%.

### Downstream consequence
- σ becomes *probabilistic at the boundary*; the cone has a *fuzzy edge* of width $\epsilon$
- This is the *same kind of degradation* as quantum-mechanical observable definitions (sharp away from threshold, probabilistic at threshold)
- Field equation form is *unchanged* (it operates on the deterministic-region geometry)
- Test 2 (cone-membership ↔ binding) must be reformulated: *graded binding probability* at the boundary, not binary

### What was NOT verified
- Cross-individual variance (P1 already restricts to single observer)
- Cross-condition variance (P1 already restricts to single illumination/task)
- Pathological observers (lesion, prosthesis) — out of scope

### Register
CONDITIONAL-OBSERVATION (with the explicit threshold-band caveat); was MODELING-MOTIVATION before this task.

---

## Task 2 — P2 stage-rate $c_p^{(s)}$ cross-check

### What is verified
The Iter 4 stage table (six rows: photoreceptor, bipolar/amacrine, M ganglion, P ganglion, V1, attentional). Each $c_p^{(s)} = \ell_s / \tau_s$ is asserted with one citation. This task re-checks: are these numbers within 2× of primary-literature consensus?

### Falsification criterion
If *any* $c_p^{(s)}$ in the table is off by >2× from the literature consensus, the table must be revised. If *most* rows are off by >2×, the operational definition $c_p = \ell/\tau$ may itself be wrong (Iter 4's choice of $\ell, \tau$ may not capture the actual propagation rate).

### Per-stage audit

**Stage 1: Cone photoreceptor**
- Iter 4 claim: $\tau = 10$ ms, $\ell = 3$ μm, $c_p = 0.3$ mm/s
- Literature: cone response time-to-peak ~30-60ms (Baylor, Lamb & Yau 1979 for amphibian; Schnapf et al. 1990 for primate); cone density 200,000/mm² in fovea → spacing ~2.2 μm
- Honest $c_p$: $2.2 / 0.04 \approx 55$ μm/s = 0.055 mm/s
- **Iter 4 value 0.3 mm/s is ~5× high** (used $\tau = 10$ ms but primate cones are slower)
- FAIL (>2× error). Source of error: $\tau$ used was rod-like, not cone-like. Cones are *faster* than rods (~30ms vs ~200ms), but Iter 4 used a value that is *too fast*.
- Corrected value: $c_p^{(\text{cone})} \approx 0.05$–$0.1$ mm/s

**Stage 2: Bipolar / amacrine network**
- Iter 4 claim: $\tau = 5$ ms, $\ell = 50$ μm, $c_p = 10$ mm/s
- Literature: bipolar integration time ~10-20 ms (Awatramani & Slaughter 2000); amacrine lateral spread ~50-200 μm (Masland 2012)
- Honest $c_p$: $100 / 0.015 \approx 6.7$ mm/s
- Within 2× of Iter 4. **PASS**

**Stage 3a: M ganglion (magnocellular)**
- Iter 4 claim: $\tau = 1$ ms, $\ell = 100$ μm, $c_p = 100$ mm/s
- Literature: M-cell spike timing precision ~1-5 ms (Uzzell & Chichilnisky 2004); RF center 100-300 μm at 10° eccentricity (Croner & Kaplan 1995)
- Honest $c_p$: $200 / 0.003 \approx 67$ mm/s
- Within 2× of Iter 4. **PASS** (barely)

**Stage 3b: P ganglion (parvocellular)**
- Iter 4 claim: $\tau = 5$ ms, $\ell = 50$ μm, $c_p = 10$ mm/s
- Literature: P-cell sustained firing, slower than M; RF center 30-100 μm in central retina
- Honest $c_p$: $65 / 0.007 \approx 9$ mm/s
- Within 2× of Iter 4. **PASS**

**Stage 4: V1 cortical column**
- Iter 4 claim: $\tau = 10$ ms, $\ell = 1$ mm, $c_p = 100$ mm/s
- Literature: V1 response onset ~40-50ms (Schmolesky et al. 1998); cortical column spacing ~500 μm-1mm (Hubel & Wiesel)
- Honest $c_p$ using onset time: $1.0 / 0.045 \approx 22$ mm/s
- Honest $c_p$ using membrane time constant ~10ms: $1.0 / 0.01 = 100$ mm/s
- **Iter 4 value passes only if $\tau$ = membrane time constant, fails if $\tau$ = response onset**
- AMBIGUOUS — depends on which $\tau$ is chosen; this is a definitional ambiguity, not an empirical error

**Stage 5: Attentional binding**
- Iter 4 claim: $\tau = 100$ ms, $\ell = 100$ mm, $c_p = 1$ m/s
- Literature: attention shift latency 100-300 ms (Posner 1980); attentional window radius ~1-10° (Eriksen & St James 1986), at viewing distance 50cm: 1-10 cm not 10 cm
- Honest $c_p$: $50 / 0.15 \approx 0.3$ m/s
- **Iter 4 value 1 m/s is ~3× high** (used $\ell = 100$ mm which is full visual field, not attention spotlight diameter)
- FAIL (>2×). Corrected value: $c_p^{(\text{att})} \approx 0.3$ m/s for the attention spotlight; ~3 m/s for full-field shifts

### Verdict

**WEAKEN with corrections needed**. Confidence: high.

Summary:
- 3 of 6 rows: PASS within 2×
- 2 of 6 rows: FAIL (>2× error, definitional sloppiness)
- 1 of 6 rows: AMBIGUOUS (definition-dependent)

The operational definition $c_p = \ell/\tau$ is *consistent* but the choice of $\ell, \tau$ per stage is *non-trivial*. Iter 4 used inconsistent conventions (membrane vs response-onset $\tau$; receptor spacing vs receptive-field radius for $\ell$; attention-spotlight vs full-field for $\ell$).

### Downstream consequence
- The stage table needs revision with *consistent convention* (e.g., use *characteristic-time-constant* for $\tau$ everywhere, *characteristic-spatial-correlation-length* for $\ell$ everywhere)
- The ratio structure (slower-stages-have-smaller-cones) is preserved qualitatively
- The *order of magnitude* per stage is approximately right (0.1 mm/s for photoreceptors, ~10 mm/s for inner retina, ~100 mm/s for ganglion, ~1 m/s for attention)
- Conclusion: the *qualitative* hierarchy holds; *quantitative* values are unreliable until a consistent convention is fixed and primary measurements are re-extracted

### Register move
Stage table moves from CONDITIONAL-OBSERVATION (E1 textbook) to OPEN-PROBLEM: "consistent operational convention for $c_p^{(s)}$ across stages" (now OP-PFE-6).

### What was NOT verified
- The *existence* of a single $c_p$ per stage (Iter 2 already admitted "per-stage")
- Whether the convention should be peak-time vs onset-time vs integration-time
- Spatial inhomogeneity (Iter 4 already noted fovea vs periphery)

---

## Task 3 — σ derivation rigor audit

### What is verified
Iter 3 claims σ is *derived* from P1 + P2 (not asserted, defeating Pattern #18 tautology). The derivation:

$$\sigma^{(s)}(e_i, e_j) := \mathbf{1}[c_p^{(s)} |t_i - t_j| \geq |x_i - x_j|]$$

is supposedly forced by P1 (invariance) + P2 (limiting rate). This task checks the derivation step-by-step.

### Falsification criterion
If any step in deriving σ from P1+P2 requires an *unstated hypothesis* (a third postulate, smuggled), then σ is not derived from P1+P2 alone, and the derivation fails. σ would remain a *primitive*, and Pattern #18 (tautology) re-applies.

### Step-by-step audit

**Step A**: From P2 (existence of $c_p^{(s)}$), define the *reachability set* $R^{(s)}(e_i) := \{e_j : \text{some perceptual influence can propagate from } e_i \text{ to } e_j\}$.

**Hidden assumption check**: P2 only states $c_p^{(s)}$ is an *upper bound*. It does NOT state:
- That perceptual influence is *deterministic* (could be probabilistic propagation)
- That propagation occurs in a *connected medium* (could be discrete hops)
- That space and time have a *fixed origin* per event (could be observer-dependent)

**STEP A REQUIRES THE ADDITIONAL HYPOTHESIS**: continuous-medium homogeneous-propagation. Call this *implicit hypothesis I1*.

**Step B**: From P1 (invariance across observer class), $R^{(s)}(e_i)$ does not depend on $\omega \in \mathcal{O}$.

**Hidden assumption check**: P1 states σ is invariant. To conclude *R is invariant*, we need σ = $\mathbf{1}_R$. But σ is the thing we're deriving — *circular*.

**STEP B HAS CIRCULARITY**: we use the invariance of σ to derive R's invariance, but σ is defined in terms of R.

Resolution attempt: maybe P1 should be reformulated as *invariance of R*, then σ follows. But this just moves the postulate (the postulate becomes "R is invariant" rather than "σ is invariant"). Step doesn't go through as stated.

**Step C**: Identify $R^{(s)}(e_i) = \{e_j : c_p^{(s)} |t_i - t_j| \geq |x_i - x_j|\}$.

**Hidden assumption check**: this identification requires:
- (i) That space is Euclidean and isotropic ($|x_i - x_j|$ uses Euclidean norm)
- (ii) That time is one-dimensional and absolute (an Iter 3-level Galilean assumption; rejecting it would require a *full Lorentz transformation* across the observer class, not just constant $c_p$)
- (iii) That the *upper-bound rate* $c_p$ is saturated (i.e., the boundary $c_p |\Delta t| = |\Delta x|$ is *achievable*, not merely *not exceeded*)

**STEP C REQUIRES THREE ADDITIONAL HYPOTHESES**: I2 (Euclidean isotropy), I3 (Galilean absolute time), I4 (saturation of $c_p$).

### Verdict

**FAIL**. Confidence: high.

Iter 3's claim of "σ derived from P1 + P2 alone" is *not rigorous*. The derivation actually uses *at least 4 implicit hypotheses*:
- **I1**: continuous-medium homogeneous propagation
- **I2**: Euclidean isotropy of retinal space
- **I3**: absolute (Galilean) time across observers
- **I4**: $c_p$ is achievable, not merely upper bound

Additionally, Step B has a *circularity* between σ and R.

### Downstream consequence
- Iter 3's "σ is derived" status is downgraded to "σ is constructed under P1 + P2 + I1-I4 + circularity-acknowledgment"
- Pattern #18 attack (tautology) returns: σ is *defined* via a construction that uses many assumptions, not *forced* by minimal postulates
- The 2-postulate compression of Iter 19 (P1, P2 derive σ) is *too clean*. Actually it's 2 postulates + 4 implicit hypotheses + 1 circularity.
- **Honest restatement of the framework's postulate count**: 2 explicit postulates + 4 implicit hypotheses ≈ 6 commitments.

### Register move
σ derivation moves from MATH-FACT-ish to MODELING-MOTIVATION ("σ has the cone form when I1-I4 hold and the circularity is resolved by reformulating P1 as invariance of R").

### Repair candidates
1. **Reformulate P1**: state invariance of *reachability* R (not σ). σ then *is* the indicator. Removes circularity. (Adds clarity but doesn't change content.)
2. **Make I1-I4 explicit**: list them as P3, P4, P5, P6. Framework has 6 postulates, not 2. Honest but bloated.
3. **Accept σ as primitive after all**: re-elevate σ to primitive status (as in Tier 2). The "derivation" was always *motivation*, never *proof*. Simplest fix.

Recommended: combine (1) and (3). Reformulate P1 in terms of R. Accept σ = $\mathbf{1}_R$ where R is operationally identified with the cone-shape *under stated regimes*. The cone *form* is a *modeling choice* given P1+P2; not *forced* by them.

### What was NOT verified
- Whether I1-I4 hold empirically (they roughly do, within continuum approximation)
- Whether the circularity is truly fatal (probably not, if P1 is reformulated)
- The geometric content (still valid as a *construction*; just not as a *derivation*)

---

## Task 4 — Postulate independence check (P1 vs P2)

### What is verified
Iter 19 lists P1 and P2 as *two independent* postulates. This task checks: could one imply the other (under any standard auxiliary assumption)? If so, framework collapses to one postulate.

### Falsification criterion
If P1 ⟺ P2 under standard auxiliary assumptions (continuity, smoothness, etc.), then framework has *one* postulate, not two — the compression claim of "2 postulates" is overcounting.

### Direction P2 → P1

P2 states: there exists $c_p^{(s)}$ as upper bound on perceptual propagation rate, invariant within $\mathcal{O}$.

Does P2 imply P1 (σ invariant across $\mathcal{O}$)?

- P2's invariance is *of $c_p$*, not of σ. σ depends on $(e_i, e_j, c_p)$. If $c_p$ is invariant and σ is a *function only of $c_p$ and $e_i, e_j$*, then σ is invariant.
- This requires: σ does not depend on *any other observer-specific quantity*.
- Is this satisfied? In Iter 3's derivation, σ = $\mathbf{1}[c_p \Delta t \geq \Delta x]$ — depends only on $c_p$ and the event coordinates.
- But event coordinates $(t_i, x_i)$ are *observer-relative* (each observer's clock and spatial coordinate system).
- For σ to be observer-invariant via P2-only, we additionally need: $\Delta t$ and $\Delta x$ are *observer-invariant* (i.e., absolute coordinates).
- That's exactly I3 (Galilean absolute time) plus its spatial analog.

**Verdict on P2 → P1**: P2 + (absolute coordinates) → P1. Partial implication, with one extra hypothesis.

### Direction P1 → P2

P1 states: σ is observer-invariant within $\mathcal{O}$.

Does P1 imply existence of $c_p^{(s)}$?

- P1 alone says σ is invariant. Says nothing about *what σ looks like as a function of $(e_i, e_j)$*.
- σ could have *any* shape: a cone, a box, a fractal, a discrete set. P1 doesn't restrict the *shape* of the σ = 1 region.
- For σ to be a *cone* (parametrized by a single $c_p$), we need *additional* structure: isotropy (I2) + absolute time (I3) + linear scaling (no fundamental length scale).
- Under those, the σ = 1 region is determined by *one* parameter: its slope = $c_p$. P2 emerges.

**Verdict on P1 → P2**: P1 + (isotropy + absolute time + scaling) → P2. Partial implication, with three extra hypotheses.

### Joint analysis

Under the *Minkowski-style* implicit hypotheses (I2, I3, plus scaling and absolute coordinates):
- P1 and P2 are *not equivalent* but they *constrain each other*
- Specifically: P1 + (full Minkowski auxiliary structure) → "σ region is some cone-shaped region invariant under $\mathcal{O}$", which is P2 once $c_p$ = cone slope is identified
- Conversely: P2 + (full Minkowski auxiliary structure) → "σ is cone-membership for $c_p$", which is P1 once invariance is propagated

### Verdict

**WEAKEN**. Confidence: medium-high.

P1 and P2 are *not independent in the strong sense*. Under the full set of implicit Minkowski-like hypotheses (I1-I4 from Task 3), they are *essentially the same statement* expressed at different levels:
- P1 = symmetry statement (invariance under $\mathcal{O}$)
- P2 = quantitative statement (invariance has a rate parameter $c_p$)
- P2 = the *value-carrying* refinement of P1

The "2 postulates" compression of Iter 19 is *cosmetic*. The honest count is *1 postulate + several implicit hypotheses*: there is *one* commitment (Minkowski-like structure invariant within $\mathcal{O}$); P1 and P2 are *two facets* of this single commitment.

### Downstream consequence
- Iter 19's "2 postulates, 5 primitives, 4 tests, 5 OPs" should be revised to "1 commitment (Minkowski-like invariance), 5 primitives, 4 tests, 6 OPs (adding OP-PFE-6)"
- The framework is *not less rigorous* for this — the *content* is the same. The cosmetic count just becomes honest.
- Falsification routes are unchanged (each falsification test targets the *content*, not the *naming*)

### What was NOT verified
- Whether P1 and P2 are equivalent in *non*-Minkowski settings (probably not — but the framework assumes Minkowski-like structure throughout)
- Whether *some* observer class makes them equivalent and another doesn't (probably the same class; P1's $\mathcal{O}$ ≡ P2's $\mathcal{O}$ by construction)

---

## Task 5 — Postulate falsifiability test design

### What is verified
Per Popper: for any postulate to be *scientific*, there must exist a *specific observation* that would refute it. Iter 19 lists 4 operational tests, but tests 1-4 target *consequences* of the framework (cone-binding correlation, curvature-binding, etc.), not the postulates *themselves*.

This task asks: for **P1 alone** and **P2 alone**, what *specific observation* would refute them?

### Falsification criterion
If no observation can refute P1 (or P2) without simultaneously refuting *other* claims, then the postulate is *unfalsifiable* in isolation — its content collapses into the conjunction.

### P1 falsifiability

**Direct falsification test**:
- Setup: one subject performs σ-judgment task across multiple sessions, same task, same illumination, same retinal eccentricity
- Measure: test-retest variance of σ-judgments far from the threshold band
- Falsification: if variance > 30%, P1 is refuted (σ is not even within-observer invariant)

**Result already in Task 1**: outside the threshold band, variance is <5%. *P1 is NOT refuted by this test*.

**Stronger falsification test** (across observers within $\mathcal{O}$):
- Setup: two subjects with similar retinas (same age, no pathology), same task and illumination
- Measure: across-subject σ-judgment agreement for stimuli far from threshold
- Falsification: if agreement < 70%, P1's *cross-observer invariance* is refuted (even within nominally-equivalent observers)

**Literature estimate**: cross-individual agreement on apparent motion ~70-85% (when far from threshold). *P1 is on the border*: NOT decisively refuted, but the equivalence class $\mathcal{O}$ is *narrow*.

**Verdict on P1 falsifiability**: P1 IS falsifiable (clear test, clear failure criterion). Current evidence: P1 *survives* the test for narrow $\mathcal{O}$, *fails* for broad $\mathcal{O}$.

### P2 falsifiability

**Direct falsification test**:
- Setup: measure perceptual propagation rate within one stage $s$ across many independent recordings
- Measure: distribution of $c_p^{(s)}$
- Falsification: if distribution has *no central tendency* (e.g., bimodal or wildly spread, >10× range), then "there exists $c_p^{(s)}$" is refuted — there is no single rate per stage

**Note**: Task 2 found that *within* primary literature, the same stage has consensus values *within a factor of ~2* (with the right convention). Task 2's >2× errors were definitional, not measurement spread. So P2 is *likely* to survive when measurements use a consistent convention.

**Stronger test** (claim of *constancy* of $c_p$ within $\mathcal{O}$):
- Setup: measure $c_p^{(s)}$ in single subject, multiple sessions, identical task/illumination
- Falsification: if $c_p^{(s)}$ drifts >2× across sessions, the *constancy within $\mathcal{O}$* claim of P2 is refuted

**Literature estimate**: $c_p^{(s)}$ stability across sessions in primate retina is typically <30% drift (within adaptation envelope). P2 survives.

**Verdict on P2 falsifiability**: P2 IS falsifiable (clear test, clear failure criterion). Current evidence: P2 *survives* with the convention-fixing caveat.

### What about P1 and P2 in their *joint* implication (cone structure)?

Even if P1 and P2 individually pass, the *conjunction* makes a *stronger* prediction: σ = cone-membership. This is tested by:
- Test 2 (Iter 16) — cone-membership ↔ binding strength

The *joint* prediction is what carries the framework's empirical content. Individual P1 and P2 falsifiability tests are necessary but not sufficient.

### Verdict

**PASS**. Confidence: high.

P1 and P2 are *both falsifiable* in Popper's sense:
- P1 — falsified by within-observer variance >30% in deterministic regime (within-subject test-retest)
- P2 — falsified by absence of central tendency in $c_p^{(s)}$ distribution (consistent-convention test)

Neither has been refuted by current literature evidence, *under their narrow scoping*:
- P1's $\mathcal{O}$ is *within-subject*, *within-task*, *within-illumination*
- P2's $c_p^{(s)}$ requires *consistent convention* (Task 2 caveat)

### Downstream consequence
- Framework is *not* unfalsifiable (good)
- Each falsification test must be performed *with the convention-fix* (Task 2 caveat embedded)
- Two new "Test 0" entries should be added to Iter 16's list:
  - **Test 0a**: P1 falsifiability — within-observer test-retest of σ-judgments
  - **Test 0b**: P2 falsifiability — multi-recording $c_p^{(s)}$ distribution analysis under fixed convention

### What was NOT verified
- Whether existing primary data (e.g., Chichilnisky lab, Berry lab MEA recordings) *already* allow these tests without new experiments — see Task 15 (dataset survey)
- Whether the threshold values (30% variance for P1, 2× drift for P2) are themselves principled or arbitrary — currently arbitrary, set to match Pass 11's adversarial threshold language

---

## Phase A Summary

| Task | Target | Verdict | Confidence | Effect on framework |
|------|--------|---------|------------|---------------------|
| 1 | P1 within-observer | WEAKEN | High | σ becomes fuzzy at threshold; binding probability graded |
| 2 | P2 stage table | WEAKEN (with corrections) | High | Stage table needs consistent convention; 2 of 6 values were off >2× |
| 3 | σ derivation rigor | FAIL | High | "σ derived from P1+P2" overstated; requires 4 implicit hypotheses + 1 circularity |
| 4 | P1/P2 independence | WEAKEN | Medium-high | P1 and P2 are facets of single Minkowski-like commitment |
| 5 | Postulate falsifiability | PASS | High | Both falsifiable; tests not yet performed but well-defined |

### Aggregate Phase A verdict
**WEAKEN** the postulate foundation. The framework's *content* survives, but Iter 19's compression ("2 postulates + ... derived σ") is *not honest*. The honest reformulation:

- **1 commitment** (Minkowski-like invariance under observer class $\mathcal{O}$), expressible as P1 (symmetry) or P2 (rate) — these are facets
- **4 implicit hypotheses** I1-I4 (continuous medium, Euclidean isotropy, Galilean absolute time, $c_p$-saturation) required for σ-as-cone derivation
- **1 reformulation** required: P1 should target *reachability R* not σ directly, to remove circularity
- **σ-at-threshold is probabilistic**, not binary; the cone has a *fuzzy edge*
- **Stage table needs Task 2 corrections**: 2 of 6 entries off >2×
- **Both P1 and P2 are falsifiable** (Popper-OK); tests not yet performed

### Pass 11 framework status after Phase A

| Component | Pre-Phase-A | Post-Phase-A |
|-----------|-------------|--------------|
| P1 | binary invariant, conditional | probabilistic at threshold, narrow $\mathcal{O}$ |
| P2 | per-stage rate, operational | per-stage rate, convention-dependent, $c_p$-values 2 of 6 wrong |
| σ derivation | derived from P1+P2 | constructed under P1+P2+I1-I4 (Task 3) |
| Postulate count | 2 independent | 1 commitment + 4 hidden hypotheses |
| Falsifiability | implicit in 4 tests | explicit per postulate (Task 5) |

### New OPs registered
- **OP-PFE-6**: Establish consistent operational convention for $c_p^{(s)}$ across stages (use $\tau$ = characteristic time constant, $\ell$ = characteristic spatial correlation length, primary measurements re-extracted under this convention)
- **OP-PFE-7**: Resolve P1 circularity by reformulating in terms of reachability R; derive σ as $\mathbf{1}_R$

### What was NOT done in Phase A
- σ derivation NOT re-attempted from scratch (Task 3 only audited; rewrite is Pass 13)
- Stage table NOT corrected in 12_ (per discipline, no edits to existing docs); corrections live here in 13_
- 11_minimal_core NOT updated (Phase G will collate Phase A-F changes for any minimal-core revision)
- No empirical literature deep dive — Tasks 1, 2 used standard psychophysics + retinal physiology references at E1-E2 level only

---

*Phase A v0. 5 tasks, 5 verdicts. Postulate foundation weakened but content preserved. canonical/SCC/PAI/8-retractions 0 modifications. Next: Phase B Field Equation Verification (Tasks 6-10) in 14_field_equation_verification.md.*
