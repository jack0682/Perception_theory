---
type: working/sensing_pipeline/reconstruction
version: v0
date: 2026-05-25
status: ACTIVE — Pass 6 Reconstruction
purpose: |
  Pass 3-5 의 21/22 deletion 후 corpus 를 pattern-aware design 으로 재구축.
  10 new TC-SP-R-N candidates (5 MATH-FACT + 5 CONDITIONAL-OBSERVATION).
  Each TC: conditional statement + pattern-avoidance + proof sketch +
  biological framing + predicted survival across 9 patterns.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (with explicit MATH-FACT vs COND-OBS tagging)
parent: 01_framework_master
prev_ledger: 09_verification_pass3
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  retractions_revived: 0
  audit_trail_preservation: complete (all 21 deletions remain documented in 02–07)
  pattern_aware_design: each NTC addresses ≥3 of 9 known patterns
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[09_verification_pass3]] · Plan: `/Users/ojaehong/.claude/plans/sensing-pipeline-full-verify-cleanup.md` (Phase 6 reconstruction extension)

# Pass 6 — Reconstruction: 10 New TC-SP-R Candidates

## 0. 본 문서의 위치

Pass 3-5 adversarial verification 이 21 of 22 TC-SP candidates 를 박탈한 후, 본 문서는 **새 TC 후보 10개** 를 *pattern-aware design* 으로 재구축한다.

설계 원칙 (Pass 5 self-Architect 검토 반영):

1. **Math/biology separation**: 각 new TC 가 **MATH-FACT** (no biological claim; retinal motivation 은 illustration only) 또는 **CONDITIONAL-OBSERVATION** (biological claim with explicit Q-conditions in statement) 로 명시 tagged.
2. **Conditional-by-design**: COND-OBS TCs 의 qualifier (Q1, Q2, ...) 가 statement 의 *integral* 부분; "weakening note" 후처리 아님.
3. **Pattern-survival design**: 각 new TC 가 9 known patterns 중 ≥3 을 *명시적으로* address.
4. **Audit trail preservation**: Pass 3-5 의 21 deletions 본문 그대로 유지; reconstruction 은 *additive*.
5. **No unconditional retinal claim**: "X *implements* Y in retina" 또는 "Y *arises from* X" 형식 금지.

본 문서가 *수행하지 않는 것*:
- TC-SP-N.M 코드 재사용 (deleted TCs 의 코드 부활 시도 없음 — 새 namespace **TC-SP-R-N**)
- Stage docs (02-07) 본문 수정 (cross-reference 만; 추후 별도 plan)
- Pass 7 verification 즉시 실행 (predicted survival 만 문서; verification 은 별도 plan)
- canonical / SCC / PAI / 8 retractions 무수정

---

## 1. 9 attack patterns — survival design 의 기준

| Pattern | Pass | Killer 주제 | Survival 전략 |
|---------|------|------------|--------------|
| #4 | 3 | RH-style specialization (general form proves famous open) | 0 hits in P3 — 표준 정리는 거의 안 fires; design 시 무시 가능 |
| #18 | 3 | Tautology (proof = restatement / definitional fiat) | Proof 가 *non-definitional* 단계 ≥2 step; intermediate identities substituting back 으로 결론 *복원 불가* |
| #40 | 3 | Too-clean general lemma counterexample | Statement 에 *retinal-specific* regularity condition 명시; general form 의 known counterexample 의 *exclusion* 가 statement 안 |
| #5 | 3 | Theorem hypothesis recheck | Invoked external theorem 의 *exact hypothesis* 가 statement Q-condition 으로 명시 |
| #6 | 4 | Divergent regularization (boundary divergence hand-waved) | Integrals 의 endpoint behavior 명시; cutoff / 적분영역 explicit |
| #46 | 4 | Boundary condition unhandled | Endpoint / saturation / 0-limit behavior 명시; operating range bounded |
| #51 | 4 | Independence assumption violated | Conditional-independence 가 statement Q-condition (예: "Cox process structure assumed") 으로 명시 |
| #11 | 5 | **Model misspecification (biological applicability gap)** | **TAG**: MATH-FACT (no biological claim) OR COND-OBS (biological claim with explicit Q's). *어느 경우도* unconditional retinal-applicability 주장 금지 |
| #29 | 5 | Continuity at limits / limit-interchange | Limit-interchanges 의 justification 명시 (DCT, Plancherel, Birkhoff 등 인용) |

---

## 2. MATH-FACT TCs (5개) — Mathematical theorems with retinal motivation only

이 5개 는 *pure mathematics*. Retinal "applicability" 는 *illustration* 으로만; *biological claim 자격 없음*. Pattern #11 의 attack 무력화.

### TC-SP-R-1 — [DELETED 2026-05-25 Pass 9 escalated]

**Status**: **DELETED via Pass 9 escalation** (3 patterns HOLE).

- **#7 implicit regularity smuggle** (Pass 8): Radon-Nikodym 가정 명사구 hidden
- **#15 vacuity at biological boundary** (Pass 9): 자연 광 = *super-Poisson* (Bose-Einstein bunching $g^{(2)}(0) > 1$); 광수용기 state-dependent thinning (bleaching, adaptation); "Poisson photon stream" hypothesis class essentially empty in actual retina outside laboratory stimuli
- **#52 information-theoretic vs operational** (Pass 9): "All finite-dim stats determined by Λ" 은 Kolmogorov-style mathematically exhaustive 이나 operationally inaccessible — 망막 decoder 는 bounded-order summary statistics 만 access; higher-order Janossy 미사용

**Why DELETED**: 본 TC 가 *mathematically valid* 이나 *biologically vacuous*: (a) Poisson hypothesis 가 자연 광에 적용 안 됨 (super-Poisson); (b) "all stats" 가 operationally accessible 아님; (c) Radon-Nikodym hidden assumption. *세 layer 의 mathematical-biological gap* 노출.

---

### TC-SP-R-1-ORIGINAL (Janossy Product Density Composition) — MATH-FACT

**Statement**: For any Poisson point process $N \sim \text{Poisson}(\Lambda)$ on a Polish-Borel space $\mathcal{X}$ with $\sigma$-finite intensity measure $\Lambda$, the $n$-th Janossy density on any compact window $W \subset \mathcal{X}$ takes the product form:

$$j_n^W(x_1, \ldots, x_n) = e^{-\Lambda(W)} \prod_{i=1}^n \lambda(x_i)$$

where $\lambda$ is the density of $\Lambda$ w.r.t. a reference $\sigma$-finite measure.

**Tag**: MATH-FACT (no biological claim).

**Retinal motivation**: Stage 0 photon point process is an instance with $\mathcal{X} = \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda_{\text{wavelength}}$. *This TC does not claim that photon arrival exactly satisfies Poisson assumption* — Mandel-Wolf coherence corrections (OP-SP-001) are separate.

**Proof sketch**: Daley-Vere-Jones Thm 5.4.II + standard Poisson PGF $G^W(h) = \exp(\int (h-1) d\Lambda)$. Termwise expansion gives product Janossy form.

**Pattern-avoidance analysis** (≥3 required):
- **#18 tautology**: Proof uses *non-definitional* step (PGF computation + termwise expansion); intermediate identities (PGF form) substituting back into Janossy do NOT recover the product form trivially — requires the $\exp$ expansion structure.
- **#5 hypothesis**: All hypotheses (Polish-Borel, σ-finite, compact W) explicit in statement.
- **#11 misspec**: TAG = MATH-FACT; biological applicability 의 *claim 없음*. Photon-arrival Poisson 가정의 *biological 정당성* 은 별도 (Mandel-Wolf §2.4 + OP-SP-001).
- **#40 too-clean**: General form (Poisson on Polish-Borel) is the *most general* setting where Janossy form holds; no retinal-specific "specialness" required.

**Predicted Pass 6/7 survival**: HIGH (textbook theorem; rigorous statement; no biological smuggling).

### TC-SP-R-2 — [DELETED 2026-05-25 Pass 9 escalated]

**Status**: **DELETED via Pass 9 escalation** (3 patterns HOLE).

- **#28 subset support** (Pass 8 minor): Scope-vs-motivation mismatch
- **#41 non-constructive set-theoretic dependency** (Pass 9): Banach lattice 가 silently Hahn-Banach (AC-equivalent) pull-in. Biology 는 vector-lattice Hahn-Jordan (pure ZF) 만 필요. *Gratuitous set-theoretic strength*.
- **#15 vacuity at biological boundary** (Pass 9): Retinal signal space 는 *bounded cone*, *bona fide Banach lattice 아님* — (a) firing rates non-negative + refractory upper bound → vector lattice 아님; (b) 실제 neuron 이 ∨, ∧ 정확히 compute 안 함 (only divisive normalization approximation 으로 axioms fail); (c) norm not lattice-compatible

**Why DELETED**: Banach lattice 가 *retinal signal 의 적합 모델 아님* — 단지 *ordered Banach space with cone structure* 정도. Pure-math statement 자체는 sound 이나 *biological instantiation* 가 vacuous.

---

### TC-SP-R-2-ORIGINAL (Riesz Lattice Disjoint Decomposition) — MATH-FACT

**Statement**: In any Banach lattice $E$, every element $f \in E$ admits a *unique* decomposition

$$f = f^+ - f^-, \quad f^+, f^- \in E_+ \text{ (positive cone)}, \quad f^+ \wedge f^- = 0 \text{ (lattice infimum)}$$

where $f^+ := f \vee 0$, $f^- := (-f) \vee 0$.

**Tag**: MATH-FACT (no biological claim).

**Retinal motivation**: ON/OFF bipolar split in retina *approximates* this decomposition for the *signed* photoreceptor response, but biological ON/OFF channels are *NOT* literal Riesz decomposition (Schiller 1992 documents overlapping operating ranges; tonic baseline firing on both channels; distinct mGluR6/AMPA cascade gains). *This TC does not claim retinal ON/OFF implements Riesz decomposition.*

**Proof sketch**: Aliprantis-Burkinshaw Thm 1.5. Uniqueness via lattice identity $(f \vee 0) + (-f \vee 0) = |f|$ and $(f \vee 0) - (-f \vee 0) = f$, together with $g \wedge h = 0 \Rightarrow g + h = g \vee h$.

**Pattern-avoidance analysis**:
- **#18 tautology**: Proof uses Banach-lattice axioms (associativity, distributivity of $\vee, \wedge$); intermediate $|f| = f^+ + f^-$ does NOT trivially imply uniqueness — requires *disjointness* axiom.
- **#11 misspec**: TAG = MATH-FACT; biological ON/OFF is *not* literal decomposition (referenced as *failure mode*).
- **#5 hypothesis**: Banach lattice structure explicit; no hidden topology assumptions.
- **#40 too-clean**: General Banach-lattice setting is the *unique correct* abstraction; counterexamples (non-lattice ordered vector spaces) lack the axioms.

**Predicted survival**: HIGH (Aliprantis-Burkinshaw is canonical textbook proof).

### TC-SP-R-3 — [DELETED 2026-05-25 Pass 8 escalated]

**Status**: **DELETED via Pass 8 escalation** (4 patterns HOLE — strongest refute of any TC ever).

- **#50 typicality vs guarantee** (Pass 7): "Concentrates on slab" heuristic without $S_V$ distribution specification
- **#37 pointwise vs uniform** (Pass 8): Concentration constant $S_V$-dependent — pure pointwise-in-$S_V$ smuggled as uniform
- **#7 implicit regularity smuggle** (Pass 8 — MAJOR): PSD $S_V$ existence 자체가 WSS / Bochner hypothesis 없이 invoked. 전체 RHS 가 *undefined* without stationarity hypothesis on $V$
- **#28 subset support** (Pass 8): "concentrates on slab of thickness $1/\sigma_t$" reads as uniform geometric containment; proof only delivers Gaussian envelope-weighted moment

**Original statement (preserved for audit trail)**:

> Adelson-Bergen motion energy $E_\theta$ 의 spacetime spectrum 이 velocity slab $\omega = -\xi \cdot v_\theta$ 의 Gaussian-weighted neighborhood 의 energy.

**Why DELETED**: 4 patterns 모두 fire — MATH-FACT 태그도 *input signal model* 의 regularity (WSS, $L^2$, Schwartz) 의 명시화 없으면 vulnerable. 본 TC 가 *MATH-FACT 의 첫 failure pattern* 확립 — *signal-class hypothesis* 의 명시 필요.

---

### TC-SP-R-3-ORIGINAL (Spacetime Fourier Velocity-Slab Identity) — MATH-FACT

**Statement**: For any quadrature pair $(G_\theta^{\sin}, G_\theta^{\cos})$ of spatiotemporal Gabor filters with carrier $(\xi_\theta, \omega_0)$ and Schwartz-class Gaussian envelope $W_{\sigma_x, \sigma_t}(x, t) = e^{-|x|^2/2\sigma_x^2} e^{-t^2/2\sigma_t^2}$, the motion energy

$$E_\theta(x, t) := |G_\theta^{\sin} * V|^2 + |G_\theta^{\cos} * V|^2$$

has expected Fourier-domain energy

$$\mathbb{E}\!\left[\int E_\theta(x, t) \, dx \, dt\right] = \frac{1}{(2\pi)^3} \int |\hat{W}(\xi - \xi_\theta, \omega - \omega_0)|^2 \cdot S_V(\xi, \omega) \, d\xi \, d\omega$$

where $S_V$ is the power spectral density of $V$, and the Gaussian weight $|\hat{W}|^2$ concentrates the integration mass on a *velocity slab* $\omega = -\xi \cdot v_\theta$ (with $v_\theta := \omega_0 / |\xi_\theta|$) of thickness $\sim 1/\sigma_t$ in $\omega$ and $\sim 1/\sigma_x$ in $\xi$.

**Tag**: MATH-FACT (no biological claim).

**Retinal/cortical motivation**: Adelson-Bergen 1985 used this identity to model *V1 complex cells*. **Mammalian retinal DSGCs use a different mechanism** (starburst amacrine cell asymmetric inhibition; Briggman-Helmstaedter-Denk 2011). *This TC does NOT claim retinal DSGC implements Adelson-Bergen energy.*

**Proof sketch**: Parseval + modulation theorem $(G_\theta \cdot e^{i \xi_\theta \cdot x - i \omega_0 t})^\wedge(\xi, \omega) = \hat{G}_{\theta}(\xi - \xi_\theta, \omega - \omega_0)$. Schwartz multiplier ensures integrability.

**Pattern-avoidance analysis**:
- **#11 misspec**: Explicit cortical-V1 scope; DSGC mechanism (starburst amacrine) is acknowledged as *different object*.
- **#29 continuity-at-limits**: Parseval + Schwartz multiplier provides absolute integrability — limit interchanges justified.
- **#6 divergent**: Schwartz envelope $|\hat{W}|^2$ kills any DC blowup in $S_V$ (e.g., $1/|\xi|^2$ natural spectrum); no divergence.
- **#46 boundary**: Spectrum on $\mathbb{R}^3$ has no problematic boundary; envelope-weighted integral converges at infinity.

**Predicted survival**: HIGH (Fourier-domain identity; Schwartz envelope handles boundaries; biology explicitly cortical-not-retinal).

### TC-SP-R-4 — [DELETED 2026-05-25 Pass 9]

**Status**: **DELETED via Pass 9** (2 patterns HOLE — *final true MATH-FACT ironclad falls*).

- **#15 vacuity at biological boundary**: Retinal pipeline *NOT Markov* (다중 prior passes 에서 establish). Horizontal-cell lateral feedback + amacrine feedback + light/dark adaptation history dependence + cone gap-junction coupling 이 Markov property 위반. *"Markov chains in retina" set 이 empty*. *Verifier 본인 명시*: "Should have triggered retraction earlier; process failure to keep DPI active when non-Markov was established."
- **#52 information-theoretic vs operational**: Shannon DPI 는 *joint distribution* 의 statement; *bounded biological decoder* 가 추출 가능한 *task-relevant Fisher information* 과 다른 객체. Sparse coding / efficient coding recompression 이 *downstream task-decodability 를 증가* 가능 — Shannon I 의 monotonic 감소 와 모순.

**Why DELETED**: 본 TC 가 textbook 정리 (Cover-Thomas Thm 2.8.1) 의 *Shannon-correct restatement* 이나 *retinal Markov 가정 자체가 vacuous*; 그리고 *biological decoder operational quantity* 는 Shannon I 가 아님 (Geisler 2008 task-relevant Fisher framework). *Last MATH-FACT 의 fall* 이 본 corpus 의 systematic conclusion 확립.

---

### TC-SP-R-4-ORIGINAL (Data Processing Inequality for Markov Kernel Cascades) — MATH-FACT

**Statement**: For any finite Markov chain $X_0 \to X_1 \to \cdots \to X_n$ of stochastic kernels $\mathcal{K}_i$ between Polish-Borel spaces, mutual information satisfies

$$I(X_0; X_i) \geq I(X_0; X_{i+1}) \quad \text{for all } i \in \{0, 1, \ldots, n-1\}.$$

Equivalently, for any $i < j$: $I(X_0; X_j) \leq I(X_0; X_i)$.

**Tag**: MATH-FACT (no biological claim).

**Retinal motivation**: SSKP $\Phi_{0 \to 4}$ is a 5-stage Markov chain *under the forward-only assumption* (which is *violated* by cortico-fugal feedback, OP-SP-010, and by adaptation, OP-SP-009). *This TC does NOT claim retinal pipeline is strictly Markov.*

**Proof sketch**: Cover-Thomas Thm 2.8.1. Chain rule of MI: $I(X_0; X_i, X_{i+1}) = I(X_0; X_i) + I(X_0; X_{i+1} | X_i)$. Markov property: $X_{i+1}$ conditionally independent of $X_0$ given $X_i$, so $I(X_0; X_{i+1} | X_i) = 0$. Therefore $I(X_0; X_i) = I(X_0; X_i, X_{i+1}) \geq I(X_0; X_{i+1})$.

For Polish-Borel continuous case: Gelfand-Yaglom-Perez sup-of-quantizations representation handles $H(X_0) = \infty$ via finite partitions; DPI preserved.

**Pattern-avoidance analysis**:
- **#11 misspec**: Pure mathematical DPI; retinal pipeline Markov assumption acknowledged as *conditional* (OP-SP-010 feedback explicit failure mode).
- **#29 continuity**: Gelfand-Yaglom-Perez explicit for continuous case.
- **#5 hypothesis**: Markov property required; retinal violation acknowledged.
- **#18 tautology**: Proof uses chain rule + Markov; non-trivial because the conditional MI vanishes only under Markov assumption.

**Predicted survival**: HIGH (Cover-Thomas + Gelfand-Yaglom-Perez; conditional acknowledged).

### TC-SP-R-5 (Composition of Stochastic Kernels Preserves Kernel Property) — MATH-FACT — [UNCLEAR Pass 9 #15]

**Pass 9 #15 flag**: Pure mathematical statement (stochastic kernel composition on Polish-Borel) 자체는 ironclad — Pattern #41 + #52 모두 HOLDS (no AC gratuitous, no operational-info smuggle). 그러나 #15 vacuity hit: retinal stages 가 *probability* kernels 가 아님 — photoreceptor saturation/bleaching → *sub-probability* (mass loss); spike generation with refractory → *intensity / measure kernel*; divisive normalization → mass non-conservation. *"Probability kernel on retinal stages" hypothesis class 이 vacuous*.

1 pattern HOLE (biological vacuity); UNCLEAR. *Final sole survivor* of all 9 verification passes.

**Salvage path**: Reformulate as *measure kernel composition* (intensity/sub-probability) — Kallenberg's measure kernel composition theorem (different but related result). 새 TC-SP-R-5' candidate 가능.

---

### TC-SP-R-5-ORIGINAL (Composition of Stochastic Kernels Preserves Kernel Property) — MATH-FACT

**Statement**: For stochastic kernels $\mathcal{K}_1: \mathcal{X} \to \mathcal{Y}$ and $\mathcal{K}_2: \mathcal{Y} \to \mathcal{Z}$ between Polish-Borel spaces, the composition

$$(\mathcal{K}_2 \circ \mathcal{K}_1)(x, C) := \int_\mathcal{Y} \mathcal{K}_2(y, C) \, \mathcal{K}_1(x, dy), \quad C \in \mathcal{B}_\mathcal{Z}$$

is a stochastic kernel $\mathcal{X} \to \mathcal{Z}$. By induction, finite composition $\mathcal{K}_n \circ \cdots \circ \mathcal{K}_1$ is a stochastic kernel.

**Tag**: MATH-FACT (no biological claim).

**Retinal motivation**: SSKP $\Phi_{0 \to 4}$ is the 4-fold composition of stage kernels *assuming* Markov property. *This TC does NOT claim retinal pipeline satisfies the Markov property* (which is violated by adaptation, OP-SP-009 + OP-SP-010).

**Proof sketch**: Kallenberg Lemma 8.5. For each $x \in \mathcal{X}$, $\mathcal{K}_2(\cdot, C)$ is $\mathcal{B}_\mathcal{Y}$-measurable (kernel property of $\mathcal{K}_2$); $\mathcal{K}_1(x, \cdot)$ is a probability measure. Integral is well-defined and a probability measure in $C$ (Tonelli for $C = \mathcal{Z}$); measurability in $x$ by monotone class.

**Pattern-avoidance analysis**:
- **#11 misspec**: Pure measure-theoretic; retinal Markov is *assumption*, not claim.
- **#5 hypothesis**: Polish-Borel + Tonelli; explicit.
- **#18 tautology**: Proof uses Tonelli (non-definitional integration result) + monotone class; not a restatement.
- **#29 continuity**: Tonelli + monotone class extension are standard limit-interchange justifications.

**Predicted survival**: HIGH (Kallenberg canonical; Tonelli + monotone class robust).

---

## 3. CONDITIONAL-OBSERVATION TCs (5개) — Biological claims with explicit Q-conditions

이 5개 는 *retinal phenomenon* 에 대한 claim 을 *includes*, 그러나 *qualifier (Q1, Q2, ...) 가 statement 의 integral 부분*. 각 Q-condition 의 violation 은 *known failure mode* 로 명시.

### TC-SP-R-6 — [DELETED 2026-05-25 Pass 8 escalated]

**Status**: **DELETED via Pass 8 escalation** (3 patterns HOLE).

- **#22 Q-condition compounding** (Pass 7): saccade 3 hz + multi-scale adaptation → Q-conjunction measure-zero in natural viewing
- **#37 pointwise vs uniform** (Pass 8): Taylor remainder constant $\bar I$-dependent — $R''$ varies by orders of magnitude across $\mathcal{R}_{\text{op}}$
- **#28 subset support** (Pass 8): stated $\mathcal{R}_{\text{op}} = [\mu/10, 10\mu]$ (factor 100) 이나 actual Taylor validity range ≈ $[I_{50}/2, 2 I_{50}]$ (factor 4) — *25배 narrower*

**Why DELETED**: Compound scope inflation — natural viewing 에서 fail (P7 #22) + lab regime 안에서도 stated R_op 의 *25배 좁은 subset* 에서만 valid (P8 #28). Weber-Fechner 의 *practical relevance* 가 사실상 *narrow neighborhood of $I_{50}$* 만으로 collapse.

---

### TC-SP-R-6-ORIGINAL (Naka-Rushton Weber-Fechner Operating-Range) — COND-OBS

**Statement (CONDITIONAL)**: Suppose:
- **(Q1)** Photoreceptor input intensity $I$ follows *log-normal stationary* distribution with geometric mean $\mu$ (verified empirically for natural light, Frazor-Geisler 2006);
- **(Q2)** Adaptation time scale separates from membrane time scale: $\tau_a \gg \tau_V$;
- **(Q3)** Slow adaptation tracks geometric mean: $d I_{50}/dt = -(I_{50} - \mu)/\tau_a$;
- **(Q4)** Operating point is within bounded range $\mathcal{R}_{\text{op}} := [\mu/10, 10\mu]$ — saturation and sub-threshold excluded;
- **(Q5)** Pavliotis-Stuart §16 ergodicity holds for the slow-fast SDE pair (uniformly ergodic fast SDE given fixed slow parameter).

**Then** the Hill function $R(I) = R_{\max} I^n / (I^n + I_{50}^n)$ with $n \in [0.7, 1.3]$ satisfies Weber-Fechner *within* $\mathcal{R}_{\text{op}}$:

$$\frac{\Delta R}{R_{\max}} = C(\kappa, n) \cdot \frac{\Delta I}{I} \cdot \left(1 + O(\Delta I / I)\right)$$

with $C(\kappa, n) = n \kappa^n / (1 + \kappa^n)^2$ and $\kappa = I_{50}/\mu$.

**Tag**: COND-OBS (biological claim about photoreceptor; conditions Q1-Q5 explicit).

**Proof sketch**: Taylor expansion of Hill function around $I_{50}$ (Q4 ensures we are in the linear regime). $I_{50}$ tracking $\mu$ (Q3) substitutes to give $\Delta R/R_{\max} \propto \Delta I/\mu$. Q1 ensures $\mu$ is well-defined and $\Delta I/\mu$ is the natural contrast variable. Q5 justifies treating $I_{50}$ as adiabatically constant on fast time scale (Pavliotis-Stuart averaging).

**Pattern-avoidance analysis**:
- **#40 too-clean**: $n \to \infty$ step function counterexample EXCLUDED by $n \in [0.7, 1.3]$. Fixed $I_{50}$ counterexample EXCLUDED by Q3 (sliding).
- **#5 hypothesis**: Pavliotis-Stuart §16 ergodicity required (Q5 explicit). Hill exponent range (Q empirical from Schnapf 1990, Baylor 1979).
- **#46 boundary**: Saturation ($I \gg I_{50}$) and sub-threshold ($I \ll I_{50}$) EXCLUDED by Q4 ($\mathcal{R}_{\text{op}}$ bounded).
- **#11 misspec**: COND-OBS tag; *under Q1-Q5* the Hill function describes photoreceptor steady-state — *not* a claim that all photoreceptor behavior reduces to Hill.
- **#51 independence**: Q1's stationarity + Q5's ergodicity provide the conditional independence structure needed; cross-photoreceptor correlations (NOT addressed) remain a known failure mode.

**Known failure modes** (acknowledged):
- Q1 violation in flash/transient stimuli (non-stationary).
- Q3 violation across multiple adaptation time scales (OP-SP-009).
- Q5 violation for jump-diffusion if Poisson photon driving introduces non-ergodicity.
- Cross-photoreceptor noise correlations (gap junctions, shared bipolar input) — not addressed.

**Predicted survival**: MODERATE-HIGH. Q-conditions explicit; failure modes acknowledged; key patterns addressed.

### TC-SP-R-7 — [DELETED 2026-05-25 Pass 7]

**Status**: **DELETED via Pass 7** (3 patterns HOLE — strongest refute in reconstruction).

- **#22 Q-condition compounding**: Q1 (C² with bounded ∂²V) excludes natural-scene edges precisely where DoG biologically targets — Mumford-Shah / Geman: natural images have discontinuities; ∂²V unbounded at edges. Conjunction Q1∧Q2∧Q3 has empty support over the very stimuli that motivate the claim.
- **#3 assumption-by-citation**: Lindeberg-Koenderink remainder $O(\sigma_c^4 \|\partial^4 V\|_\infty)$ requires *C⁴* with bounded 4th derivatives; TC's Q1 only specifies *C²* with bounded 2nd derivatives. Citation hypothesis NOT verified by TC's own Q-condition.
- **#50 typicality vs guarantee**: Bound vacuous (RHS = ∞) on stated hypothesis class. "$\alpha$ near 1" qualifier silently migrates from proof sketch into formal leading coefficient (drops $(1-\alpha)V$ zero-order term).

**Original statement (preserved for audit trail)**:

> Under Q1 (V ∈ C²(Ω) with bounded ∂²V), Q2 (margin > 3σ_s from boundary), Q3 (σ_s/σ_c ∈ [2,5], σ_c ≪ L_V): $B(x) = (\sigma_s^2 - \sigma_c^2) \cdot (1-\alpha)/2 \cdot \Delta V(x) + O(\sigma_c^4 \|\partial^4 V\|_\infty)$ on interior Ω.

**Why DELETED**: Multi-layered failure — citation hypothesis mismatch + bound vacuous + Q-condition empty support at biologically relevant edges. Cannot be salvaged without (i) strengthening Q1 to C⁴ AND (ii) restricting scope to smoothly-shaded interior (excluding edges), AND (iii) explicit α-near-1 condition. Such fix yields a TC describing *boring smooth gradients* — biologically uninteresting.

**Replacement**: Lindeberg-Koenderink scale-space identity (under C⁴) 본문 §4.5b 의 generic mathematical reference 로 유지. *Retinal DoG* 의 edge detection 정당화는 efficient coding (Atick-Redlich) 으로 별도 — *operator-derivation* 정리 자격 박탈.

### TC-SP-R-7-DEPRECATED (DoG Center-Surround as Laplacian Approximation on Interior) — COND-OBS

**Statement (CONDITIONAL)**: Suppose:
- **(Q1)** Input $V \in C^2(\Sigma_{\text{ret}}, \mathbb{R})$ with bounded second derivatives on the sensor interior $\Omega \subset \Sigma_{\text{ret}}$;
- **(Q2)** Restricted to $\Omega$ with margin $> 3 \sigma_s$ from sensor boundary $\partial \Sigma_{\text{ret}}$ (effective compact support of DoG kernel);
- **(Q3)** Scale ratio $\sigma_s / \sigma_c \in [2, 5]$ with $\sigma_c \ll L_V$ where $L_V$ is the characteristic length of $V$'s gradient.

**Then** the DoG convolution $B = K_{\text{DoG}}^{\sigma_c, \sigma_s, \alpha} * V$ approximates a scale-normalized Laplacian:

$$B(x) = (\sigma_s^2 - \sigma_c^2) \cdot \frac{1 - \alpha}{2} \cdot \Delta V(x) + O(\sigma_c^4 \cdot \|\partial^4 V\|_\infty)$$

within the restricted interior $\Omega$.

**Tag**: COND-OBS (biological motivation: bipolar cell center-surround; conditions explicit).

**Proof sketch**: Lindeberg-Koenderink scale-space: $G_\sigma * V = V + \sigma^2 / 2 \cdot \Delta V + O(\sigma^4 \cdot \|\partial^4 V\|_\infty)$ (Taylor expansion of Gaussian convolution). $K_{\text{DoG}} = G_{\sigma_c} - \alpha G_{\sigma_s}$. Subtract:

$$B = (1 - \alpha) V + \frac{1}{2}(\sigma_c^2 - \alpha \sigma_s^2) \Delta V + O(\sigma_c^4, \sigma_s^4)$$

For $\alpha$ near 1 (typical bipolar surround balance), the constant term $\approx 0$, leaving $B \propto (\sigma_s^2 - \sigma_c^2) \Delta V / 2$ as the leading term. Margin $> 3 \sigma_s$ (Q2) ensures effective support of $K_{\text{DoG}}$ stays inside $\Omega$.

**Pattern-avoidance analysis**:
- **#46 boundary**: Sensor edge EXPLICIT EXCLUSION via margin $> 3 \sigma_s$ (Q2). $\sigma \to 0$ (delta) and $\sigma \to \infty$ (constant) EXCLUDED by Q3 ($\sigma_c \ll L_V$ and finite $\sigma_s$).
- **#40 too-clean**: General DoG counterexamples (curved edges, T-junctions, textures) acknowledged as *outside Q1's C² regularity*. Q1 explicitly requires bounded second derivatives.
- **#11 misspec**: Statement is about *DoG operator* (mathematical), not "bipolar cells implement Laplacian". Bipolar cells *approximate* DoG; their *actual* mechanism (mGluR6/AMPA cascade) is acknowledged as different object.
- **#51 independence**: NO Gaussian-iid noise assumption — DoG approximation is *deterministic* (about the operator). Biological pixel noise correlations are SEPARATE concern, not in this TC's scope.

**Known failure modes**:
- Q1 violation at sharp edges (jump discontinuities) — DoG response becomes ill-defined at the discontinuity.
- Q2 violation near sensor boundary — convolution undefined.
- Q3 violation for very large structures ($L_V \lesssim \sigma_c$) or very small ($\sigma_c \gtrsim L_V$).
- *Biological correlated noise* in actual retina (gap junctions) — not addressed.

**Predicted survival**: MODERATE-HIGH. Q2 directly addresses prior #46 hole; Q1 addresses #40; #11 avoided by deterministic-operator framing.

### TC-SP-R-8 — [DELETED 2026-05-25 Pass 7]

**Status**: **DELETED via Pass 7** (2 patterns HOLE).

- **#22 Q-condition compounding**: 5 Q-conditions multiplicatively → conjunction has near-empty support in real parvocellular data. Berry-Meister 1998 (Fano 0.3-0.7, not 0.9-1.1 → Q4 violated); Mastronarde 1989 + Shlens 2006 (~80% pairs have $|r^{\text{noise}}| > 0.05$ → Q5 violated). Joint Q1∧Q2∧Q4∧Q5 < 1% support in actual recordings.
- **#50 typicality vs guarantee**: $O(W/\bar\lambda \log(\bar\lambda/W))$ correction presented as *uniform* at fixed $\bar\lambda/W \geq 4$, but Bialek-Rieke produces it as *asymptotic* leading term as $\bar\lambda/W \to \infty$. At Q3 boundary ($\bar\lambda/W = 4$), implicit constant unbounded; "leading-order" wording is asymptotic, not uniform.

**Original statement (preserved for audit trail)**:

> Under Q1 (Cox process structure), Q2 (Gaussian WSS bandlimited), Q3 ($\bar\lambda \geq 4W$ Nyquist), Q4 (Fano ≈ 1), Q5 (|r^noise| < 0.05): $I(s; G) = I(s; \lambda) + O((W/\bar\lambda) \log(\bar\lambda/W))$.

**Why DELETED**: Same fundamental Cox issue as deleted TC-SP-3.1 (now repeated at new level). Q-condition conjunction excludes most actual parvocellular regimes (Berry-Meister + Pillow GLM literature explicit). The "parvocellular high-rate stationary regime" 의 *real-world support* 는 *measure-zero*. Reconstruction 의 *systematic 약점* 노출 — biology 가 *Cox* 와 *Markov-conditional-independence* 의 가정에 systematically 어긋남.

**Replacement**: Cox/Hawkes process modeling 본문 (05 §2-3) 은 *modeling tools* 로 유지 (specific regime 에서 valid). Rate sufficiency 의 *biological theorem* 자격 박탈.

### TC-SP-R-8-DEPRECATED (Cox Process Rate Sufficiency in High-Rate Bandlimited Regime) — COND-OBS

**Statement (CONDITIONAL)**: Suppose:
- **(Q1)** Spike train $G$ is doubly-stochastic Poisson (Cox process) with stochastic rate $\lambda(t)$ — i.e., conditional on $\lambda$, spike inter-arrival times are independent exponential with rate $\lambda(t)$;
- **(Q2)** Stimulus $s(t)$ is wide-sense stationary Gaussian with bandwidth $W$ (Fourier support $\subseteq [-W, W]$);
- **(Q3)** Average rate $\bar{\lambda} \geq 4W$ (Nyquist with safety factor 2);
- **(Q4)** Refractory effects negligible: empirical Fano factor $\in [0.9, 1.1]$ over windows $\geq 1/W$;
- **(Q5)** Population correlation is negligible: $|r^{\text{noise}}| < 0.05$ between any pair of channels considered.

**Then** the mutual information satisfies, to leading order:

$$I(s; G) = I(s; \lambda) + O\!\left( \frac{W}{\bar{\lambda}} \log \frac{\bar{\lambda}}{W} \right)$$

— i.e., the spike rate $\bar{\lambda}_c(t) := |\{t_i : t_i \in [t - \delta, t]\}|/\delta$ (suitably smoothed) carries $I(s; \lambda)$ up to small correction; precise spike timing adds $O$ correction.

**Tag**: COND-OBS (biological claim about parvocellular high-rate stationary regime; Q5 explicitly excludes magnocellular bursting and population-correlated regimes).

**Proof sketch**: Bialek-Rieke 1996 derivation. Cox structure (Q1) gives $G | \lambda \sim \text{Poisson}$ with $\lambda$ as sufficient statistic. Stein 1967 lower bound + Bialek-Rieke upper bound coincide at $O(W/\bar{\lambda} \log(\bar{\lambda}/W))$ under Q2-Q4. Q5 ensures channel-conditional independence so the per-channel bound is not contaminated by population effects.

**Pattern-avoidance analysis**:
- **#51 independence**: Q1 (Cox conditional independence) and Q5 (low noise correlation) EXPLICIT. Magnocellular bursting (which violates Q1) and parasol-population correlations (which violate Q5) ACKNOWLEDGED as out-of-scope.
- **#5 hypothesis**: All four standard hypotheses (Cox + bandlimited + Nyquist + Fano $\approx 1$) listed as Q1-Q4.
- **#11 misspec**: Statement explicitly conditional on Q1-Q5; does NOT claim "all retinal ganglion cells implement rate code" — restricted to *parvocellular high-rate stationary regime where Q1-Q5 hold*.
- **#46 boundary**: $\bar{\lambda} \to 0$ (sub-Nyquist) EXCLUDED by Q3. $\bar{\lambda} \to \infty$ trivially OK (Gaussian limit).

**Known failure modes**:
- Q1 violation in bursting magnocellular cells (Berry-Meister 1998).
- Q5 violation in population coding with shared noise (Pillow 2008).
- Q3 violation in transient sub-threshold regimes.
- Q4 violation in cells with strong refractory (CV $\ll 1$).

**Predicted survival**: MODERATE. Q5 is strong condition that empirically isn't always met; statement remains conditional on this hypothesis being checked per data set.

### TC-SP-R-9 — [DELETED 2026-05-25 Pass 8]

**Status**: **DELETED via Pass 8** (2 patterns HOLE — second MATH-FACT failure after R-3).

- **#37 pointwise vs uniform** (Pass 8): "Take $\sup_{\mu_0}$ of both sides" 는 *admissibility-pushforward compatibility* (즉 $\mathcal{K}_{i-1} \circ \cdots \circ \mathcal{K}_1 \mu_0 \in \mathcal{P}_i$) 가 *pointwise-in-$\mu_0$* 검증 필요. Statement 의 "uniform across cascades" 가 sup-interchange-without-uniform-convergence smuggle (Pattern #37 textbook form)
- **#28 subset support** (Pass 8): Stated "all admissibility-compatible cascades" 이나 actual proof support 는 *compatible-pushforward 가 모든 stage 에서 성립* 하는 *sparse subset*. Independent per-stage capacity constraint (biologically relevant case) 가 D' 밖

**Original statement (preserved for audit trail)**:

> $C(\Phi) := \sup_{\mu_0 \in \mathcal{P}_0} I(\mathcal{S}_0; \Phi \mu_0) \leq \min_{i \in \{1, \ldots, n\}} C(\mathcal{K}_i)$

**Why DELETED**: 본 TC 가 Pass 7 까지 RETAINED MATH-FACT 였으나 Pass 8 의 *uniformity / scope* attacks 에서 *admissibility-pushforward compatibility* 의 silent assumption 노출. *Sup interchange* 가 textbook pattern #37 smuggle. R-3 와 함께 *MATH-FACT 의 systematic uniformity vulnerability* 확립.

**Replacement**: Cover-Thomas Ch.7 의 channel capacity 본문 reference 유지. *Retinal applicability* (Geisler 2008 framework alternative) 의 별도 정리 필요. TC-SP-R-9 자격 박탈.

**Statement**: For any Markov chain of stochastic kernels $\Phi = \mathcal{K}_n \circ \cdots \circ \mathcal{K}_1$ between Polish-Borel spaces, the Shannon channel capacity (under any fixed admissibility constraint $\mathcal{P}_0 \subseteq \mathcal{P}(\mathcal{S}_0)$) satisfies

$$C(\Phi) := \sup_{\mu_0 \in \mathcal{P}_0} I(\mathcal{S}_0; \Phi \mu_0) \leq \min_{i \in \{1, \ldots, n\}} C(\mathcal{K}_i)$$

where $C(\mathcal{K}_i) := \sup_{\mu \in \mathcal{P}_i} I(\mathcal{S}; \mathcal{K}_i \mathcal{S})$ for $\mathcal{S} \sim \mu$ and admissibility $\mathcal{P}_i$ on $\mathcal{K}_i$'s input.

**Tag**: MATH-FACT (no biological claim).

**Retinal motivation**: SSKP composition with $n = 4$. **Retina is NOT a Shannon channel** in any operational sense (Geisler 2008): no encoder freely choosing messages, no decoder optimizing for capacity, biological information is task-relevant Fisher information about scene parameters rather than Shannon source bits. *This TC does NOT bound "retinal capacity"* — it bounds an abstract Shannon-channel quantity that does not directly describe retinal perception.

**Proof sketch**: TC-SP-R-4 (DPI) applied pointwise in $\mu_0$: for each $\mu_0 \in \mathcal{P}_0$ and each intermediate $i$, $I(\mathcal{S}_0; \mathcal{S}_n) \leq I(\mathcal{S}_0; \mathcal{S}_i)$. Take $\sup_{\mu_0 \in \mathcal{P}_0}$ of both sides; sup respects $\leq$. RHS $\leq \sup_{\mu \in \mathcal{P}_i} I(\mathcal{S}; \mathcal{K}_i \mathcal{S}) = C(\mathcal{K}_i)$ provided $\mathcal{K}_{i-1} \circ \cdots \circ \mathcal{K}_1 \mu_0 \in \mathcal{P}_i$ (compatible admissibility). Min over $i$ gives the stated bound.

**Pattern-avoidance analysis**:
- **#11 misspec**: Retinal non-applicability EXPLICIT via Geisler 2008 reference; task-relevant Fisher info framework noted as the more appropriate biological framework.
- **#29 continuity**: Sup-of-monotone-inequalities preserves ordering; sup over single admissibility set, no interchange issue.
- **#5 hypothesis**: Admissibility compatibility EXPLICIT ($\mathcal{P}_{i-1}$ pushforward under $\mathcal{K}_{i-1}$ should be in $\mathcal{P}_i$).
- **#18 tautology**: Uses TC-SP-R-4 (DPI) as a non-trivial step; not a self-restatement.

**Predicted survival**: HIGH (textbook Shannon; explicit biological non-applicability).

### TC-SP-R-10 — [DELETED 2026-05-25 Pass 8 escalated]

**Status**: **DELETED via Pass 8 escalation** (4 patterns HOLE — equal-strongest refute with R-3).

- **#50 typicality vs guarantee** (Pass 7): "Resembling V1" empirical-as-guarantee
- **#37 pointwise vs uniform** (Pass 8): Per-patch / per-initialization / per-$M/N$ pointwise observation dressed as uniform
- **#7 implicit regularity smuggle** (Pass 8): $\arg\min$ uniqueness (L1 not strictly convex), dictionary-learning convergence (nonconvex joint problem, no convergence theorem)
- **#28 subset support** (Pass 8): Stated "natural-scene patches" 이나 actual demonstration 은 *Olshausen-Field 1996 corpus + specific hyperparameters* 만 — generalization 미확립

**Why DELETED**: 본 TC 가 *empirical observation* 을 *theorem-statement form* 으로 framed 한 systematic failure. 4 patterns 모두 fire — sparse coding 의 *robust observation* 자체는 valid 이나 *TC-candidate* 자격 아님 (empirical result, not theorem).

---

### TC-SP-R-10-ORIGINAL (Sparse Coding L1-Regularized MAP as V1 Substrate Model) — COND-OBS

**Statement (CONDITIONAL)**: Suppose:
- **(Q1)** Natural-scene patches $V \in \mathbb{R}^N$ are modeled with sparse prior $p(V | D, \beta) \propto \exp(-\beta \|D^{-1} V\|_1)$ on a learned overcomplete basis dictionary $D \in \mathbb{R}^{N \times M}$ ($M \geq N$);
- **(Q2)** Photoreceptor observation noise is Gaussian: $y = V + \eta$, $\eta \sim \mathcal{N}(0, \sigma_n^2 I)$;
- **(Q3)** Dictionary $D$ is *learned* (not assumed) from a corpus of natural patches via Olshausen-Field 1996 minimization $\min_{V, D} \sum_t \|y_t - D V_t\|_2^2 + \beta \sum_t \|V_t\|_1$ with normalization $\|D_k\| = 1$ per column.

**Then** the MAP reconstruction

$$\hat{V} = \arg\min_V \|y - D V\|_2^2 + \beta \|V\|_1$$

has solution exhibiting *spatially-localized, oriented, bandpass* basis functions resembling V1 simple cells (Olshausen-Field 1996 empirical result). *The TC does NOT claim retinal bipolar cells implement this sparse coding* — biological substrate is V1 cortical simple cells; retina may perform partial whitening (Atick-Redlich 1990) that *prepares* input for downstream sparse coding.

**Tag**: COND-OBS (biological claim about V1; conditions Q1-Q3 explicit; retina explicitly NOT the claim's target).

**Proof sketch**: Olshausen-Field 1996. The L1 prior promotes sparse activation; the dictionary learning forces $D$ to capture statistical regularities of natural patches. Convergence to V1-like basis is empirical (replicated by many subsequent works: Lewicki-Olshausen 1999, etc.). No closed-form proof; convergence is via gradient descent on the joint $\{V, D\}$ optimization.

**Pattern-avoidance analysis**:
- **#11 misspec**: Statement TARGETS V1 cortical cells, NOT retinal bipolars. Retinal pre-processing (Atick-Redlich whitening) is noted as separate operation that *prepares* input.
- **#51 independence**: Sparse prior is NON-Gaussian, NON-iid (basis activations have heavy-tailed distribution); this is the explicit replacement for the failed Gaussian-iid assumption in the deleted TC-SP-2.3.
- **#5 hypothesis**: Q3 (dictionary learning protocol) explicit; Olshausen-Field's specific objective function cited.
- **#40 too-clean**: Result is *empirical* (numerical optimization), not a closed-form general lemma; no counterexample-from-generality concern.

**Known failure modes**:
- Q1 violation if natural-scene patches are *not* sparse in any basis (e.g., textures with no localized structure).
- Q3 violation: alternative dictionary learning protocols (ICA, NMF) give different bases.
- Cortical V1 simple cells have receptive fields that are *approximately* Gabor-like; Olshausen-Field bases are *similar but not identical*.

**Predicted survival**: MODERATE. Empirical claim with explicit scope; relies on Olshausen-Field's empirical convergence; no closed-form rigor.

---

## 4. Pattern-survival 통합 표

| NTC | Tag | Patterns Addressed | Predicted Survival |
|-----|-----|--------------------|--------------------|
| **R-1** Janossy product | MATH-FACT | #18, #5, #11, #40 | HIGH |
| **R-2** Riesz decomp | MATH-FACT | #18, #11, #5, #40 | HIGH |
| **R-3** Spacetime slab | MATH-FACT | #11, #29, #6, #46 | HIGH |
| **R-4** DPI cascade | MATH-FACT | #11, #29, #5, #18 | HIGH |
| **R-5** Kernel composition | MATH-FACT | #11, #5, #18, #29 | HIGH |
| **R-6** Naka-Rushton Weber | COND-OBS | #40, #5, #46, #11, #51 | MOD-HIGH |
| **R-7** DoG ≈ Laplacian on interior | COND-OBS | #46, #40, #11, #51 | MOD-HIGH |
| **R-8** Cox rate sufficiency | COND-OBS | #51, #5, #11, #46 | MODERATE |
| **R-9** Min-capacity bound | MATH-FACT | #11, #29, #5, #18 | HIGH |
| **R-10** Sparse coding | COND-OBS | #11, #51, #5, #40 | MODERATE |

**Aggregate prediction**: HIGH 6, MOD-HIGH 2, MODERATE 2. Estimated Pass 7 survival rate: ≥70% (vs. Pass 5 collapse rate of 95.5%).

---

## 5. Cross-reference to deleted predecessors

각 새 TC 가 어느 deleted TC 의 *salvaged mathematical core* 인지:

| New TC | Replaces (was deleted because) | Salvaged content |
|--------|-------------------------------|------------------|
| R-1 | TC-SP-0.1 (factorization Λ tautology, Stiles-Crawford) | First clause: stats = Λ functional (now general Poisson, no biology) |
| R-2 | TC-SP-2.1 (ON/OFF channels overlap, baseline firing) | Pure Banach lattice fact; biological non-implementation explicit |
| R-3 | TC-SP-2.4 (Adelson-Bergen vs DSGC starburst) | Fourier-slab identity for V1, NOT retina |
| R-4 | TC-SP-1.2 (centrifugal feedback, lateral coupling) | DPI for abstract Markov chain, retinal Markov as conditional |
| R-5 | TC-SP-1.1 (Markov property breaks under adaptation) | Pure composition lemma, no retinal claim |
| R-6 | TC-SP-1.4 (averaging hypothesis, sub-threshold/saturation) | Hill Weber-Fechner *within bounded operating range* with explicit slow-fast (Q5) |
| R-7 | TC-SP-2.2 (Marr-Hildreth counterexamples + sensor edge) | DoG Laplacian approximation *on interior C² inputs* with margin |
| R-8 | TC-SP-3.1 (Cox violated by population correlations) | Cox conditional on Q5 ($|r^{\text{noise}}| < 0.05$) — parvocellular regime only |
| R-9 | TC-SP-4.1 (Shannon capacity ≠ retinal task-relevant info) | Pure Shannon min-bound; Geisler 2008 framing for biological alternative |
| R-10 | TC-SP-2.3 (Gaussian prior empirically wrong for natural images) | Sparse-coding L1 prior (correct framework); V1 target (not retinal bipolar) |

---

## 6. Pre-mortem (3 scenarios)

### Scenario 1: All 10 new TCs fall to Pass 7
**Probability**: Low (~10%). Math-FACT TCs are textbook results; their failure would imply a foundational issue with Cover-Thomas, Aliprantis-Burkinshaw, Parseval, or Kallenberg — *very* unlikely.

**Action if happens**: Declare reconstruction failure; pivot to archival framing.

### Scenario 2: 4-5 new TCs survive, but Pattern #11 still hits 3-5 (mostly COND-OBS)
**Probability**: Moderate (~30%). COND-OBS TCs are most exposed; even with Q-conditions, the biological framing slips back.

**Action if happens**: Tighten COND-OBS to MATH-FACT with stronger non-biological framing; OR accept partial reconstruction with explicit "COND-OBS frequently fails biological applicability — under explicit Q-conditions only" caveat.

### Scenario 3: New TCs survive 9 patterns but Pass 7 with new patterns kills them
**Probability**: Moderate (~30%). Verification arms race: more patterns = more attacks.

**Action if happens**: Accept that "stable" is conditional on chosen pattern set; document Pass 6 pattern set explicitly; future passes may add patterns and force further deletions.

---

## 7. Expanded test plan (deliberate mode)

**Unit**: Each NTC standalone verification:
- Statement is syntactically well-formed (parseable LaTeX)
- Q-conditions explicit (if COND-OBS)
- Pattern-avoidance list specific (not vague)
- Predicted survival assigned (HIGH/MOD/MOD-HIGH)

**Integration**: Cross-NTC consistency:
- NTC-R-4 (DPI) uses NTC-R-5 (composition) as premise — chain valid
- NTC-R-9 (capacity) uses NTC-R-4 (DPI) — chain valid
- NTC-R-6, R-7, R-8 (COND-OBS) all reference distinct biological substrates (rod, bipolar, ganglion) — no overlap

**E2E**: Pass 6 verification:
- Run subset of 9 attack patterns (#11 + #51 + #5 — most lethal in P3-P5) on 10 NTCs
- Each NTC: predicted survival vs actual verdict
- Discrepancy analysis: if predicted HIGH but verdict HOLE, why?

**Observability**:
- Grep `### TC-SP-R-` in stage docs → count new TCs (should be 0 — NTCs live only in this 10_ document for Pass 6)
- Grep `### TC-SP-R-` in 10_reconstruction_pass6.md → 10
- 09 ledger §15 cross-reference

---

## 8. Implementation checklist (집행 완료)

- [x] 10 new TCs designed (5 MATH-FACT + 5 COND-OBS)
- [x] Pattern-avoidance analysis per TC (≥3 of 9 patterns)
- [x] Predicted survival assigned
- [x] Cross-reference to deleted predecessors
- [x] Pre-mortem (3 scenarios)
- [x] Expanded test plan (unit/integration/e2e/observability)
- [x] 본 10_reconstruction_pass6.md 작성
- [x] Constraint compliance: canonical / SCC / PAI / 8-retractions 무수정

---

## 9. ADR (Architecture Decision Record)

**Decision**: Pass 6 Reconstruction via Option A (10 new TCs, 5 MATH-FACT + 5 COND-OBS, pattern-aware design).

**Drivers**:
1. Verification ground truth — Pass 3-5 results dictated what avoiding patterns means
2. User's "계속 진행해 아주 자세하게 정밀하게" directive
3. Constraint discipline (canonical/SCC/PAI/8-retractions unchanged)

**Alternatives considered**:
- **Option B (minimal 5 TCs)**: Rejected — insufficient for "아주 자세하게"
- **Option C (PAI bridge work, advance OP-SP-006)**: Rejected for *this* plan — higher-leverage but requires SCC re-engagement; deferred to separate plan
- **Option D (archival + register reframing)**: Rejected — does not match "계속 진행해"
- **Option E (pure mathematical-only reconstruction, no COND-OBS)**: Rejected — too narrow; loses connection to biological motivation entirely

**Why chosen**: Best matches user directive ("very long, very detailed, very precise") while honoring verification ground truth (math/biology separation) and staying within constraints (canonical/SCC/PAI unchanged).

**Consequences**:
- New TC namespace `TC-SP-R-N` separate from deleted `TC-SP-N.M`
- 10_reconstruction_pass6.md adds ~1000 lines to directory
- Predicted survival rate ≥70% in Pass 7 (vs. 4.5% post Pass 5)
- New attack surface for Pass 7 verification
- Reconstruction demonstrates *resilience strategy* — useful pattern for future cleanup-reconstruct cycles

**Follow-ups**:
1. Pass 7 verification of new TCs (separate plan)
2. PAI bridge work (OP-SP-006 advancement, separate plan)
3. Possible Stage 6/7 expansion (LGN, V1)
4. Stage docs (02-07) cross-reference updates to link to new TCs (separate plan)

---

## 10. 한 줄 요약

> Pass 6 Reconstruction 으로 21/22 deletion 의 corpus 를 *pattern-aware design* 으로 재구축: **10 new TCs** (5 MATH-FACT + 5 COND-OBS), 각 TC 가 ≥3 of 9 known attack patterns 를 explicitly address, predicted survival 6 HIGH + 2 MOD-HIGH + 2 MODERATE. Math/biology separation 가 핵심 design principle. canonical/SCC/PAI 무수정.

---

*Pass 6 Reconstruction v0. 10 new TC-SP-R candidates. Predicted Pass 7 survival ≥70%. 다음 단계: Pass 7 verification (별도 plan) 또는 PAI bridge work.*

---

## 11. Pass 7 Verification Results (2026-05-25 late evening)

사용자 directive "더 깎아보자 정밀하게" — 3 new attack patterns 적용:
- **#22 Q-condition compounding** (conjunction empty support in real data)
- **#3 Assumption-by-citation** (rhetorical authority vs verified hypothesis)
- **#50 Typicality vs guarantee** (approximate ≠ uniform bound)

### 11.1 Pass 7 verdict matrix (10 NTCs × 3 patterns)

| TC-SP-R | #22 | #3 | #50 | Cumulative HOLE | **Pass 7 Verdict** |
|---------|-----|----|-----|------------------|---------------------|
| R-1 Janossy | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| R-2 Riesz | HOLDS | HOLDS-edition | HOLDS | 0 | **RETAINED** |
| R-3 Slab | HOLDS | HOLDS | **HOLE** | 1 | **UNCLEAR** ("concentrates" heuristic without distribution) |
| R-4 DPI | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| R-5 Composition | HOLDS | UNCLEAR-lemma# | HOLDS | 0 | **RETAINED** (content sound) |
| R-6 Naka-Rushton | **HOLE** | HOLDS | HOLDS-marginal | 1 | **UNCLEAR** (saccade 위반; lab-only scope 필요) |
| R-7 DoG≈Laplacian | **HOLE** | **HOLE** | **HOLE** | **3** | **DELETED (strongest refute in Pass 7)** |
| R-8 Cox rate | **HOLE** | HOLDS | **HOLE** | **2** | **DELETED** |
| R-9 Min-capacity | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| R-10 Sparse coding | HOLDS | HOLDS | **HOLE** | 1 | **UNCLEAR** ("resembling V1" empirical-as-guarantee) |

### 11.2 Pass 7 통계 + 집행

- **RETAINED (0 HOLE across 3 P7 patterns)**: 5 (R-1, R-2, R-4, R-5, R-9) — 모두 MATH-FACT
- **DELETED (≥2 HOLE)**: 2 (R-7, R-8)
- **UNCLEAR (1 HOLE)**: 3 (R-3, R-6, R-10) — substantive but not yet 2+ threshold

### 11.3 결정적 발견 — Pass 7 의 systematic 진단

1. **MATH-FACT TCs 가 모두 survive** — pattern-aware design 의 성공 측면. Pure mathematics + biological non-claim 가 verification 에 robust.
2. **COND-OBS TCs 가 systematically vulnerable** — 5 of 5 COND-OBS (R-6, R-7, R-8, R-10 hit; R-3 도 model-statement 측면) — *Q-condition multiplicative compounding* (#22) 이 가장 lethal: 각 Q 가 individually OK 여도 conjunction 이 real data 에서 vanishing support.
3. **R-7 의 3-pattern failure** 가 특히 의미 — Lindeberg-Koenderink remainder 인용의 *hypothesis mismatch* (C²→C⁴) + bound vacuous at edges + α-typicality smuggle. *Mathematical citation 자체가 hypothesis-check 가 필요* — Pass 6 의 pattern-survival design 이 충분하지 않았음.
4. **R-3 의 #50 HOLE 은 MATH-FACT 의 first failure** — exact Parseval identity 자체는 sound 이나, "concentrates on slab" 의 *interpretive layer* 가 typical-case smuggle. Math-fact 도 *interpretation* 의 sneakiness 노출.

### 11.4 Final state after Pass 7

| Status | Count | Codes |
|--------|-------|-------|
| RETAINED (0 cumulative HOLE across applicable patterns) | 5 | R-1, R-2, R-4, R-5, R-9 |
| Original survivor (Pass 3-5 sole survivor) | 1 | TC-SP-0.1a |
| UNCLEAR (1 HOLE in Pass 7; pending Pass 8) | 3 | R-3, R-6, R-10 |
| DELETED (Pass 7) | 2 | R-7, R-8 |
| **Total active candidates** | **9** | (1 + 5 + 3 = 9) |
| Total Pass 7 deletions | 2 | |

### 11.5 Pass 6 design lesson 재평가

Pass 6 의 *predicted survival* vs *Pass 7 actual*:
- Predicted HIGH (6): R-1, R-2, R-3, R-4, R-5, R-9 → **actual: 5 HIGH + 1 UNCLEAR** (R-3 의 #50 typicality 가 예상 외)
- Predicted MOD-HIGH (2): R-6, R-7 → **actual: 1 UNCLEAR + 1 DELETED** (R-7 의 3-pattern failure 가 강하게 underestimated)
- Predicted MODERATE (2): R-8, R-10 → **actual: 1 DELETED + 1 UNCLEAR**

**Calibration**: prediction 7 of 10 correct. 3 mis-predictions all *too optimistic*. 본 lesson — pattern-aware design 의 *self-prediction* 도 confirmation bias 위험. Future passes 의 prediction 은 *external adversarial verification* 필요.

### 11.6 Constraint 재확인 (Pass 7 cleanup 후)

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| Stage docs 01-09 본문 수정 | **0** ✓ (모든 Pass 7 cleanup 은 10_reconstruction_pass6.md 내부에만) |
| 새 TC-SP-R 코드 | **0** (기존 R-1..R-10 namespace 내에서 deletion / unclear marking 만) |
| 8 SCC retractions 부활 | **0** ✓ |

---

*Pass 6 v1 (Pass 7 verification + cleanup 통합). Active TCs after 4 verification passes (P3-P7): **9** (= TC-SP-0.1a + 5 RETAINED + 3 UNCLEAR). 다음 단계: Pass 8 으로 UNCLEAR 3개 검증, 또는 stable-state 선언 + PAI bridge work.*

---

## 12. Pass 8 Verification Results (2026-05-25 deepest cut)

사용자 directive "더 깎아보자 정밀하게" — 3 추가 patterns:
- **#7 implicit regularity smuggle**
- **#37 pointwise vs uniform conflation**
- **#28 subset support (actual scope < stated)**

### 12.1 Pass 8 verdict matrix (9 active TCs × 3 patterns) + cumulative

| TC | P7 holes | P8 #7 | P8 #37 | P8 #28 | Cumulative HOLE (P7+P8) | **Pass 8 Decision** |
|----|---------|-------|--------|--------|--------------------------|---------------------|
| TC-SP-0.1a | (n/a) | **HOLE** | HOLDS | **HOLE**(mild) | **2** | **DELETED** ⚠️ (9-pattern survivor falls) |
| R-1 Janossy | 0 | **HOLE**(minor) | HOLDS | HOLDS | 1 | **UNCLEAR** |
| R-2 Riesz | 0 | HOLDS | HOLDS | **HOLE**(minor) | 1 | **UNCLEAR** |
| R-3 Slab | 1 (#50) | **HOLE**(MAJOR) | **HOLE** | **HOLE** | **4** | **DELETED (strongest)** |
| R-4 DPI | 0 | HOLDS | HOLDS | HOLDS | **0** | **RETAINED** (clean across 6 patterns) |
| R-5 Composition | 0 | HOLDS | HOLDS | HOLDS | **0** | **RETAINED** (clean across 6 patterns) |
| R-6 Naka-Rushton | 1 (#22) | HOLDS | **HOLE** | **HOLE** | **3** | **DELETED (strong)** |
| R-9 Min-capacity | 0 | HOLDS | **HOLE** | **HOLE** | **2** | **DELETED** ⚠️ (second MATH-FACT failure) |
| R-10 Sparse coding | 1 (#50) | **HOLE** | **HOLE** | **HOLE** | **4** | **DELETED (strongest)** |

### 12.2 Pass 8 통계

- **RETAINED (0 cumulative HOLE across 6 P7+P8 patterns)**: **2** (R-4 DPI, R-5 Composition) — the *truly ironclad core*
- **UNCLEAR (1 minor HOLE)**: 2 (R-1, R-2) — fixable with single explicit-hypothesis addition
- **DELETED (Pass 8)**: 5 (TC-SP-0.1a, R-3, R-6, R-9, R-10)

### 12.3 결정적 발견 — Pass 8 의 systematic 진단

1. **TC-SP-0.1a 도 fallen** — Pass 3-5 의 21/22 deletion 후 *lone survivor* 이었던 0.1a 가 *meta-mathematical attacks* (#7 + #28) 에서 *load-bearing 가정이 statement 밖에 hidden* 임이 노출. **Radon-Nikodym a.c. + simple-process** 가 statement 의 명시적 hypothesis 아니라 명사구 안 ("density of Λ", "Poisson") 에 hidden — *systematic verbal smuggle pattern* 확인.

2. **R-3, R-9 두 MATH-FACT failure** — pre-Pass-8 까지 MATH-FACT TCs 가 모두 robust 였으나 *uniformity / scope / signal-class regularity* attacks 에서 fall:
   - R-3: PSD $S_V$ 자체가 WSS hypothesis 없이 invoked
   - R-9: sup-interchange 의 admissibility-pushforward compatibility 가 silent
   
   둘 모두 *textbook citation 자체* 의 hypothesis 가 TC 의 stated Q-conditions 으로 verify 안 됨. **MATH-FACT 의 *signal-model regularity* 가 새 vulnerability** 확립.

3. **R-3, R-10 4-pattern failure** — 본 corpus 의 *strongest refute*. R-3 는 *MATH-FACT*, R-10 은 *COND-OBS* — 양쪽 모두 4 patterns 통과 못 함. *interpretive smuggle* 가 가장 lethal 패턴.

4. **남은 2 RETAINED (R-4 DPI + R-5 Composition) 의 공통점**:
   - 둘 다 *pure measure-theoretic existence/closure* claims
   - 둘 다 *외부 signal/distribution 가정 없음* (R-4 는 입력 distribution μ_0 의 *any choice* 에 robust; R-5 는 *any pair of stochastic kernels*)
   - 둘 다 *non-trivial inequality / construction* 이 아니라 *generic well-definedness*
   - → **본 corpus 에서 살아남는 TC 의 *공통 형식*: "generic existence/closure on Polish-Borel" — *signal-class / data-class hypothesis 0*

### 12.4 Final state after Pass 8

| Status | Count | Codes |
|--------|-------|-------|
| **RETAINED (truly ironclad — 0 HOLE across 6 P7+P8 patterns)** | **2** | R-4, R-5 |
| **UNCLEAR (1 minor HOLE; fixable)** | 2 | R-1, R-2 |
| **DELETED (Pass 8)** | 5 | TC-SP-0.1a, R-3, R-6, R-9, R-10 |
| **Total active candidates** | **4** | (was 9 pre-P8; now 2 RETAINED + 2 UNCLEAR) |
| Cumulative DELETED across all verification passes | **28** | of 32 ever-created TCs |
| **Overall survival rate** | **12.5%** | 4 / 32 |

### 12.5 Pass 8 의 *meta-lesson*

본 corpus 의 가장 깊은 진단:

> **수학적으로 trivially 참인 TC** (R-4 DPI, R-5 Composition) 만 다중-pass adversarial verification 에 survives.

이 *trivially-true core* 는 *intellectually 가치 작음* — 모두 standard textbook results 의 단순 재진술. **본 corpus 의 *진정한 value*** 는 TCs 가 아니라 *11,000+ 라인의 mathematical exploration* 그 자체 — *retinal phenomena 의 mathematical 형식화 시도와 그 시도가 어디서 부서지는가* 의 documented record.

이는 *연구 자료* 로서는 가치 있으나 *theorem-candidate corpus* 로서는 4 TCs 만 활용 가능.

### 12.6 Constraint 재확인 (Pass 8 cleanup 후)

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| Stage docs 01, 03-09 본문 수정 | **0** ✓ (Pass 8 cleanup 은 02 의 0.1a + 10_ 내부에만) |
| 8 SCC retractions 부활 | **0** ✓ |

---

*Pass 6 v2 (Pass 8 cleanup 통합). Active TCs after 5 verification passes (P3-P8): **4** (= 2 RETAINED ironclad + 2 UNCLEAR-minor). 28 deletions cumulative. Stable state 도달 — further passes 의 marginal value 극히 낮음 (R-4, R-5 는 textbook generic existence/closure; UNCLEAR R-1, R-2 의 hole 은 fix 가능한 명시화 차원). 다음 단계: stable-state 선언 + PAI bridge pivot.*

---

## 13. Pass 9 Verification Results (2026-05-25 absolute final) — Corpus Collapse

사용자 directive (재차): "더 깎아보자 정밀하게". 3 추가 patterns:
- **#41 non-constructive set-theoretic dependency**
- **#15 vacuity at biological boundary**
- **#52 information-theoretic vs operational quantity mismatch**

### 13.1 Pass 9 verdict matrix (4 active TCs × 3 patterns) + cumulative across all passes

| TC | P7+P8 holes | P9 #41 | P9 #15 | P9 #52 | Cumulative HOLE (P7-P9) | **Pass 9 Decision** |
|----|------------|--------|--------|--------|--------------------------|---------------------|
| R-1 Janossy | 1 (#7) | HOLDS-caveat | **HOLE** | **HOLE** | **3** | **DELETED (strong)** |
| R-2 Riesz | 1 (#28 minor) | **HOLE** | **HOLE** | HOLDS | **3** | **DELETED (strong)** |
| R-4 DPI | 0 | HOLDS | **HOLE** | **HOLE** | **2** | **DELETED** ⚠️ (last MATH-FACT ironclad falls) |
| R-5 Composition | 0 | HOLDS | **HOLE** | HOLDS | **1** | **UNCLEAR** (sole survivor) |

### 13.2 Pass 9 통계

- **RETAINED**: **0** (final true MATH-FACT ironclad R-4 falls; sole RETAINED R-5 reduced to UNCLEAR)
- **UNCLEAR (1 hole)**: 1 (R-5 — probability vs sub-probability kernel)
- **DELETED (Pass 9)**: 3 (R-1, R-2, R-4)

### 13.3 *최종* 통계 (Pass 3-9 통합)

| Status | Count |
|--------|-------|
| Original TCs ever-created | **32** (22 P1+P3 split 0.1a + 10 P6 reconstruction) |
| Total DELETED | **31** (21 P3-P5 + 2 P7 + 5 P8 + 3 P9) |
| **Final active (UNCLEAR with salvage path)** | **1** (R-5) |
| **Final survival rate** | **3.1%** (1/32) |

### 13.4 Pass 9 의 systematic 발견

**Pattern #15 (vacuity) 가 모든 active TC 에 hit (4/4)**. Verifier 의 결정적 진단:

> "Every active TC's universal hypothesis class is empty/measure-zero in actual retina."

구체:
- R-1 (Poisson): 자연 광 super-Poisson (Bose-Einstein bunching $g^{(2)}(0) > 1$)
- R-2 (Banach lattice): retinal signal space 는 bounded cone, vector lattice 아님
- R-4 (Markov): retinal pipeline NOT Markov (다중 prior passes establish; 본 패턴 fire 가 retraction trigger 였어야 함)
- R-5 (probability kernel): retinal stages 는 sub-probability / intensity, probability 아님

**원인 분석**: 본 corpus 의 *모든* TC 가 *textbook mathematical structure* (Poisson, Banach lattice, Markov chain, probability kernel) 의 retinal 응용 주장 — 그러나 *실제 retina 는 그 textbook structures 의 instance 아님*. 본 sensing pipeline 의 *총체적* misframing.

### 13.5 Pass 9 의 *meta-meta-lesson*

본 corpus 가 *adversarial verification 의 limit 까지* 깎였을 때 *0 RETAINED + 1 UNCLEAR* 가 남음. 이는:

1. **수학 자체는 sound** — 모든 deleted TC 의 underlying math (Cover-Thomas DPI, Kallenberg composition, Hahn-Jordan, Daley-Vere-Jones Janossy) 는 textbook 진리
2. **그러나 retinal applicability 는 systematically vacuous** — 망막의 *실제 구조* 가 textbook 가정과 *체계적으로 다름*
3. **본 corpus 의 *진정한 contribution*** 은 *negative result* — *"다음 시도하지 마라"* 의 documented record:
   - Poisson 가정 → super-Poisson 현실 (R-1 #15)
   - Banach lattice 가정 → bounded cone 현실 (R-2 #15)
   - Markov 가정 → feedback + adaptation 현실 (R-4 #15)
   - Probability kernel 가정 → sub-probability + intensity 현실 (R-5 #15)
4. **다음 framework 의 *출발점***: super-Poisson + bounded cone + non-Markov + sub-probability/intensity 가 *실제 retinal 구조*. 새 framework 가 이들 위에 build 되어야.

### 13.6 Final Constraint 재확인

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| Stage docs 01-08 본문 수정 (Pass 9) | **0** ✓ (Pass 9 cleanup 은 10_ 내부에만) |
| 8 SCC retractions 부활 | **0** ✓ |

---

*Pass 6 v3 (Pass 9 cleanup 통합). Active TCs after 6 verification passes (P3-P9): **1** (R-5 UNCLEAR). 31 deletions cumulative; 96.9% attrition. 모든 RETAINED MATH-FACT fall. **Corpus 의 final state 가 documented research process record** — TC corpus value 가 *negative result* 와 *exploration documentation* 임을 honest acknowledge.*
