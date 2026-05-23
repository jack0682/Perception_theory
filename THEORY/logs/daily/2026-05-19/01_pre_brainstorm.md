---
type: log/daily/pre_brainstorm
date: 2026-05-19
session_label: W8-Day2 — pre_brainstorm reference (외부 학문 백서)
prepared: 2026-05-18 EOD (작성자: agent, 사용자 EOD 검토 가능)
purpose: 내일 T_*/H5 deep work 의 외부 reference. 인식론적 증명 철학 + Perception 이론 + 수학적 도구 통합.
sources_total: 15+ web searches across 8 sub-sections
---

> [!nav] Linked: [[00_plan]] · [[00_index]] · [[../2026-05-18/99_summary|어제 99_summary]] · [[auxiliary_structures_master|AUX-1.5 registry]]

# 01 — Pre-Brainstorm (2026-05-19, W8-Day2)

## 0. Mission of this file

내일 (2026-05-19) 의 T_*/H5 deep work 를 위한 *외부 학문 reference 백서*. SCC 이론의 두 잔류 U:
- `T_*` (effective stochastic temperature; fixed-point 구조)
- `H5` (Morse stability; spinodal Goldstone mode degeneracy)

가 *기존 학문 전통의 어느 자리에* 있는지, 어떤 *수학 도구가* 사용 가능한지, 어떤 *철학 framework이* 자연스러운지 — 한 곳에 압축. **새 SCC 정리 도출 시도 없음**; 외부 reference 인용만.

산출 절: §1 (철학), §2 (perception 이론), §3 (phase transition), §4 (수학 도구), §5 (T_*-specific), §6 (H5-specific), §7 (SCC 연결 진단), §8 (내일 plan 권장).

---

## §1. 인식론적 증명 철학 (Philosophy of Epistemological Proof)

### §1.1 First-person 인식론 — 현상학과 embodied cognition

**핵심 인물:** Merleau-Ponty (현상학), Varela-Thompson-Rosch (enactive cognition).

Merleau-Ponty의 *지각의 현상학* (1945): "Subjectivity는 신체와 세계와 묶여있다 — 의식적 존재는 신체적 존재이자 세계의 존재와 하나이다." Embodied cognition은 이 통찰의 현대적 계승: 인식은 *순수 표상적 신경 과정*에서 오는 게 아니라 *신체와 환경의 pre-reflective 관여*에서 온다.

Varela 등 (1991 *The Embodied Mind*): "Autopoietic enactivism" — cognition은 *생명 시스템의 biodynamics* 그 자체. 4E cognition (embodied / embedded / enacted / extended) framework.

**→ SCC 와의 관계:** CN-COB (Closed Ontological Budget) 의 *first-person 색채* — `Origin(s) ∈ {𝒟_u, 𝒜_u, 𝒫_obs}` 에서 *외부 우주 가정 0* — 이 enactive cognition 의 *수학적 형식화*. SCC u-field는 Merleau-Ponty의 *perceptual horizon* 의 정량 모델.

**핵심 reference:**
- Merleau-Ponty, *Phenomenology of Perception* (1945).
- Varela, Thompson, Rosch, *The Embodied Mind* (1991).
- Stanford Encyclopedia: [Embodied Cognition](https://plato.stanford.edu/entries/embodied-cognition/).

### §1.2 Constructive 수학 / Intuitionism (Brouwer ↔ T_*)

**핵심 인물:** L.E.J. Brouwer (직관주의 창시자), Per Martin-Löf (intuitionistic type theory).

Brouwer의 직관주의 (1907~): *배중률 (excluded middle)* 거부. "P 또는 ¬P" 는 *constructive proof* 없이 주장 불가. Brouwer는 동시에 *Brouwer fixed-point theorem* (1911) 의 창시자 — **T_* 의 핵심 도구**.

Martin-Löf 의 intuitionistic type theory (1972): Brouwer constructivism 의 형식화. Coq, Agda, NuPRL 같은 proof assistant 의 기반. 4-Color Theorem, Feit-Thompson Theorem 같은 대형 정리가 이 framework 안에서 formalize 됨. HoTT (Univalent Foundations, Voevodsky) 가 현대 후속.

**Constructivism의 핵심 원칙:** Existence 증명은 *witness* 를 포함해야 한다. "fixed-point 가 존재" 라는 statement만으로는 부족; *어떻게* 그 fixed-point를 *구성하는지* 보여야 함.

**→ SCC 와의 관계:** T_* fixed-point (`T_* = ψ(T_*)`) 의 *constructive* 처리 시 Brouwer fixed-point 의 *non-constructive* 본성이 문제 — 존재는 증명되나 *어떻게 찾는지* 알려주지 않음. 이게 §5.1 self-consistency 의 *iterative* 접근이 자연스러운 이유 (각 iteration이 constructive).

**핵심 reference:**
- Brouwer, *Über Abbildung von Mannigfaltigkeiten* (1911) — fixed-point theorem.
- Martin-Löf, *Intuitionistic Type Theory* (1984).
- Stanford Encyclopedia: [Intuitionistic Type Theory](https://plato.stanford.edu/entries/type-theory-intuitionistic/).

### §1.3 Observer-dependent 이론들

**핵심 인물:** Niels Bohr (complementarity), Carlo Rovelli (relational QM), Edwin Jaynes (Bayesian/MaxEnt), Wheeler ("It from Bit").

Bohr의 complementarity (1927~): 양자 측정에서 *관찰자의 측정 선택*이 결과에 본질적으로 들어감. Rovelli의 relational QM (1996): 모든 물리량은 *관찰자에 상대적* — "절대 상태"는 무의미.

Jaynes (1957~): MaxEnt principle — 통계역학을 *information-theoretic* 으로 재해석. 확률은 *관찰자의 무지* 측정; entropy는 *관찰자가 모르는 만큼*. 이는 §5.3 T_* information-theoretic 해석의 직접 기초.

Wheeler의 "It from Bit" (1989): 물리적 실재는 *관찰자-참여* 의 산물.

**→ SCC 와의 관계:** OMS-1 의 `Θ = (q, λ, ξ)` 관찰자 파라미터 컨테이너가 *이미* relational 형식 — SCC 의 모든 정리는 *Θ 에 상대적*. AUX-1.5 §7 COB 원칙은 *Jaynes-style* 정보론적 해석을 ξ 카탈로그로 가능하게 함.

### §1.4 Self-referential / Fixed-point 구조 — Lawvere

**핵심 인물:** Bill Lawvere (1969 fixed-point theorem), Kurt Gödel (1931 incompleteness).

**Lawvere's fixed-point theorem** (1969): Cantor diagonal, Russell paradox, Gödel incompleteness, Turing halting, Tarski undefinability 의 *모두* 의 categorical 일반화. *Cartesian closed category* 안에서 어떤 surjective map 도 fixed-point 함수를 induce.

Gödel diagonal: "이 문장은 증명 불가능하다" 류 self-referential statement 의 구성. 이게 *모든 self-application 가능 시스템* 의 본질 (Hofstadter *GEB*, Yanofsky).

**→ SCC 와의 관계:** T_* 의 self-referential 구조 `T_* → π_{T_*} → Var → T_*` 가 Lawvere fixed-point 의 *구체적 사례*. 즉 T_*의 fixed-point 구조는 SCC 의 *우연한* feature 가 아니라 *self-application 가능 인식 시스템* 의 *불가피한* 구조 — Lawvere가 말한 "self-reference 는 어떤 자기-해석 가능 시스템에서도 피할 수 없다" 의 SCC 사례.

**핵심 reference:**
- Lawvere, "Diagonal arguments and Cartesian closed categories" (1969).
- Wikipedia: [Lawvere's fixed-point theorem](https://en.wikipedia.org/wiki/Lawvere's_fixed-point_theorem).
- arXiv [2503.13536](https://arxiv.org/abs/2503.13536) — Survey on Lawvere's fixed-point theorem (2025).
- Yanofsky, "A universal approach to self-referential paradoxes" (2003).

---

## §2. Perception 이론 (Computational + Cognitive)

### §2.1 Bayesian Brain / Predictive Processing / Active Inference

**핵심 인물:** Helmholtz (unconscious inference, 1860s), Knill & Pouget (Bayesian brain, 2004), Rao & Ballard (predictive coding, 1999), Friston (FEP / Active Inference, 2005~).

**Helmholtz** (1860s): 지각은 *unconscious inference* — 망막 자극에서 *원인의 추론*. 이게 현대 Bayesian brain 의 모태.

**Rao-Ballard predictive coding** (1999): 시각 cortex가 hierarchical Bayesian inference 를 수행. Higher-level → lower-level *predictions* 전송; lower-level → higher-level *prediction errors* 전송. End-stopping 같은 extra-classical receptive field effects 가 이 모델로 설명됨.

**Friston Free Energy Principle (FEP)** (2005~): 자기-조직 시스템의 *유일한* imperative — surprise (negative log evidence) 최소화. **Active Inference**: 지각 = inbound sensory information에 대한 free energy 최소화; 행동 = outbound action information 에 대한 free energy 최소화.

**Markov blanket**: 시스템의 *통계적 경계* — internal states ↔ blanket (sensory + active) ↔ external. 자기-조직 시스템은 *nested Markov blankets* 의 self-assembling 계층.

**→ SCC 와의 관계:** SCC 의 reflected Langevin SDE (Stage 5 P-F-A1) 는 FEP 의 *수학적 instance*. T_* 는 *관찰자의 generative model* 의 noise level. K_act = #PersComp 는 active inference의 *posterior dimensionality*. **이게 T_* Route C (관찰자-개인 noise scale) 의 자연스러운 frame**. SCC 전체가 FEP 의 *특수 형태* 일 가능성 — §7.3 에서 더.

**핵심 reference:**
- Rao & Ballard, "Predictive coding in the visual cortex" (*Nature Neuroscience*, 1999).
- Friston, "The free-energy principle: a unified brain theory?" (*Nature Reviews Neuroscience*, 2010).
- Friston et al., "The Markov blankets of life" (*J. R. Soc. Interface*, 2018).
- Friston, "A free energy principle for a particular physics" (arXiv [1906.10184](https://arxiv.org/abs/1906.10184)).

### §2.2 Gestalt Psychology — Formation의 직관적 기초

**핵심 원리:** Figure-ground separation, grouping principles (proximity, similarity, continuation, closure), Prägnanz law.

Gestalt 심리학 (Wertheimer, Köhler, Koffka, 1910s~): "전체는 부분의 합 이상이다." 지각은 *조각의 조합*이 아니라 *전체 패턴의 즉각 인식*. SCC 의 *formation* 개념 (K_act = 한 덩어리) 의 가장 직접적인 정신적 조상.

**→ SCC 와의 관계:** SCC formation = *mathematical Gestalt*. soft cohesion field u가 spinodal 임계 위에서 응집할 때 — 이게 figure-ground separation 의 수학적 모델. Grouping principles 가 SCC 의 closure / cohesion 연산자의 *경험적 기원*.

### §2.3 Ecological psychology (Gibson) — Direct perception

Gibson (1979 *The Ecological Approach*): *Affordances* — 환경이 행위자에게 *직접* 제공하는 행동 가능성. "Perception" 은 표상의 *구성*이 아니라 invariants 의 *직접 pickup*.

**→ SCC 와의 관계:** SCC u-field가 affordance-like 인가? 부분적으로 — u는 *raw input I* 에서 *T(I)* 로 변환된 직접 표상이며, K_act 같은 위상학적 invariant 가 ecological invariants 와 유사. 단 SCC는 *constructive* 측면 (energy gradient flow) 도 가지므로 *pure Gibsonian* 은 아님.

### §2.4 Marr's three levels — SCC의 위치

Marr (1982 *Vision*): 세 분석 수준 — (1) **Computational** ("무엇을 하는가, 왜"), (2) **Algorithmic** ("어떤 표상과 알고리즘으로"), (3) **Implementational** ("어떻게 신경물질에서 실현").

**→ SCC 의 위치:** SCC 는 *computational level* (왜 우리는 객체를 보는가 + 그것의 수학적 형식). canonical.md §13 의 모든 정리는 computational. Algorithmic level (구체적 알고리즘) 은 `CODE/scc/*` 가 *예시* 구현. Implementational (뉴런 수준) 은 미정 — 신경과학과의 연결이 §3.5 neural field 를 거쳐 가능.

### §2.5 Multistable Perception + Phase Transitions — H5 ↔ perceptual bistability

**핵심 인물:** Hermann Haken (synergetics), J.A.S. Kelso (HKB model).

**Haken's synergetics** (1977~): 비평형 시스템의 *자기-조직* — order parameters + control parameters + instabilities. *통일적 framework* for pattern formation across physics, chemistry, biology.

**Kelso의 HKB (Haken-Kelso-Bunz) model** (1985): 인간 양손 협응 (bimanual coordination) 의 *phase transition* 모델. *Multistability + phase transitions + hysteresis* 가 자기-조직의 fundamental features. Critical frequency 에서 spontaneous transition.

**Multistability in perception** (Kelso 1995, etc.): Necker cube, binocular rivalry — perceptual reversion이 *nonlinear phase transition* 의 character. Self-organizing networks + synergetic modeling 으로 high-fidelity simulation.

**→ SCC H5 와의 직접 관계:** SCC의 spinodal 임계점에서 Goldstone mode 가 zero eigenvalue 를 갖는 것 = HKB 의 critical frequency 에서 order parameter 가 degenerate 가는 것 = *perceptual phase transition*. **H5 spinodal Goldstone mode degeneracy ↔ perceptual bistability**. 이게 H5가 단순한 수학 가설이 아니라 *perception 자체의 특징* 인 이유.

**핵심 reference:**
- Haken, *Synergetics: An Introduction* (1977).
- Haken, Kelso, Bunz, "A theoretical model of phase transitions in human hand movements" (*Biological Cybernetics*, 1985).
- Kelso, *Dynamic Patterns* (1995).
- Scholarpedia: [HKB model](http://www.scholarpedia.org/article/Haken-Kelso-Bunz_model).

### §2.6 Binding Problem + Object Permanence

**Binding problem:** 시각 features (color, motion, shape) 가 *어떻게* 통합된 object 로 묶이는가? 후보 답: *temporal binding* (Singer 1999 — 40 Hz 동기화), *gamma oscillations*, *neural assemblies*.

**Object permanence** (Spelke, Piaget): 영아 발달에서 *불연속적 사건* — 6-8개월에 객체 영속성 인지. SCC 의 K_act = #PersComp 은 이 능력의 *수학적 형식화*.

**→ SCC 와의 관계:** SCC 의 PersComp + persistent homology stability theorem (§4.5) 이 binding 의 *위상학적* 해결책. T-Temporal-Identity (CV-1.13 SEALED) 가 object permanence 의 수학적 정형화.

---

## §3. Phase Transition / Pattern Formation (수학적 도구)

### §3.1 Cahn-Hilliard Spinodal Decomposition — T8의 *표준 이론*

**Cahn-Hilliard equation** (Cahn & Hilliard, 1958): 4차 parabolic PDE; binary mixture 의 phase separation 표준 모델. SCC의 T8 spinodal 의 *직접* 수학적 조상.

**Linear stability analysis:** 균질 평형 `u ≡ c` 가 spinodal regime 안에 있으면 *unstable manifold* 가 dominant. *Characteristic wavenumber* 가 가장 빠르게 자라남.

**Maier-Wanke (1990s, *Communications in Mathematical Physics*):** Spinodal decomposition 의 *rigorous* 수학적 증명 — `near homogeneous equilibrium in spinodal region` 에서 *most solutions* exhibit spinodal decomposition behavior. *Geometric + measure-theoretic* techniques.

**Coarsening fronts:** Spinodal decomposition + coarsening 의 *spatio-temporal dynamics* — multi-stage invasion fronts. First front invades unstable equilibrium → spatially periodic pattern; secondary fronts invade → coarser pattern.

**→ SCC H5 와의 직접 관계:** SCC E_λ + Σ_m 시스템이 Cahn-Hilliard 의 *graph 버전* (continuous PDE → graph operator). T8 spinodal 임계점이 *정확히* Cahn-Hilliard 의 spinodal 임계점. H5의 generic Morse 시도는 Cahn-Hilliard 에 대한 기존 Morse-style 분석 (Maier-Stelzer-Wanke 1990s) 의 SCC 적용.

**핵심 reference:**
- Cahn & Hilliard, "Free energy of a nonuniform system" (*J. Chem. Phys.*, 1958).
- Maier-Paape & Wanke, "Spinodal decomposition for the Cahn-Hilliard equation in higher dimensions" (*Commun. Math. Phys.*, 1998).
- Scheel et al., "Spinodal decomposition and coarsening fronts" — [PDF](https://www-users.cse.umn.edu/~scheel/preprints/ch-front.pdf).

### §3.2 Symmetry Breaking + Goldstone Modes — H5 의 *왜* zero eigenvalue?

**Goldstone's theorem** (1961): *Spontaneous symmetry breaking* 마다 *각 깨진 generator 에 대해 하나의 massless bosonic excitation* (Nambu-Goldstone mode) — order parameter 의 long-wavelength fluctuation.

**Mermin-Wagner theorem:** 유한 온도에서 1D / 2D 시스템에서는 *thermal fluctuations of NG modes 가 long-range order 를 파괴* — spontaneous symmetry breaking 불가. 이게 finite lattice 에서의 caveat.

**Finite-system entanglement scaling:** Recent work (arXiv [2503.22468](https://arxiv.org/html/2503.22468)) — type-B Goldstone modes 의 entanglement entropy 가 *logarithmic* in block size.

**Lattice examples:** Hexagonal InMnO₃ — Higgs-like + Goldstone-like phonon modes from symmetry-broken lattice potential.

**→ SCC H5 와의 직접 관계:** SCC formation은 *Z₂* (또는 *그래프 대칭군*) symmetry breaking 으로 해석 가능. spinodal 임계점에서 Hessian의 zero eigenvalue 는 *Goldstone mode* — 깨진 대칭의 orbit tangent direction. 이게 H5의 "intrinsic degeneracy" 의 *물리적 원인*. SCC에서 graph가 작은 Aut(G) 를 가지면 Mermin-Wagner caveat 가 약화됨.

**핵심 reference:**
- Goldstone, "Field theories with «Superconductor» solutions" (*Il Nuovo Cimento*, 1961).
- Mermin & Wagner, "Absence of ferromagnetism..." (1966).
- MIT 8.334 lecture: [SSB and Goldstone Modes](https://ocw.mit.edu/courses/8-334-statistical-mechanics-ii-statistical-physics-of-fields-spring-2014/).

### §3.3 Pattern Formation — Turing + Reaction-Diffusion

**Turing's 1952 paper** "The chemical basis of morphogenesis": Linear stability analysis of reaction-diffusion → patterns emerge from instabilities. 줄무늬, 점, 미로 패턴 등 — 모두 *symmetry breaking + characteristic wavelength*.

**Phase field models:** Cahn-Hilliard 가 가장 prototypical. *Order parameter* φ가 두 phase 사이의 *smooth interpolation*.

**→ SCC 와의 관계:** SCC u-field는 *phase field* 의 직접 instance. T8 spinodal regime 에서 SCC 가 Turing-like patterns 를 형성 — 이게 SCC formation 의 본질.

### §3.4 Catastrophe Theory (Thom-Mather) — H5 의 unifying framework?

**Thom의 catastrophe theory** (1960s, *Stabilité structurelle et morphogenèse*, 1972): Smooth potential의 *discontinuous* behavior 분류. 4-parameter 까지의 elementary catastrophes 7개: **fold, cusp, swallowtail, butterfly**, wave, hair, fountain.

**Zeeman의 popularization** (1970s): "Zeeman catastrophe machine" — cusp catastrophe 의 mechanical visualization. *Fight-or-flight* model in dogs (anger × fear → bistable behavior).

**Singularity:** Maxima/minima/inflection points coalesce → singularity → value jump.

**→ SCC H5 와의 관계:** SCC T8 spinodal 임계점이 *어떤* catastrophe 인가? *Saddle-node (fold)*? *Cusp*? Generic Morse 깨지는 방식이 catastrophe theory 분류로 *정확히* 명명 가능. Option F3 (catastrophe theory) 의 유효성 평가 — *cusp* 일 가능성이 높음 (m 과 β/α 두 parameter).

**핵심 reference:**
- Thom, *Structural Stability and Morphogenesis* (1972).
- Zeeman, *Catastrophe Theory: Selected Papers 1972-1977* (1977).
- Wikipedia: [Catastrophe theory](https://en.wikipedia.org/wiki/Catastrophe_theory).
- Robbins talk: [Thom's Catastrophe Theory + Zeeman's perception model](https://people.math.wisc.edu/~jwrobbin/catastrophe/catastrophe_talk.pdf).

### §3.5 Neural Field Theory — Amari-Wilson-Cowan

**Amari** (1977), **Wilson-Cowan** (1972, 1973): Continuous neural population dynamics. *Bump attractors*, *traveling waves*, *pattern formation in neural fields*.

**→ SCC 와의 관계:** SCC u-field 가 neural field 의 *형식 parallel*. Bump attractor = SCC formation (K_act = 1). Traveling wave = SCC dynamic transition. *implementational level* (Marr §2.4) 의 가교.

---

## §4. 위상학적 / 대수적 도구

### §4.1 Morse Theory — H5의 핵심 도구

**Classical Morse theory** (Milnor 1963 *Morse Theory*): Smooth manifold M 위의 Morse function f 의 critical points 가 *비특이* (non-degenerate Hessian) → M의 *위상* 정보 (Betti numbers, etc.) 추출 가능.

**Morse density:** Morse functions 는 C∞(M, R) 안에서 *C∞-dense* 이며 C² topology 에서 *open* — 따라서 *generic*. 이건 Sard's theorem 의 직접 함의.

**Morse-Bott:** Critical points 가 *degenerate critical manifolds* (이아니라 isolated points) 인 일반화. Goldstone modes 처리 가능.

**Equivariant Morse** (Bott 1954, Atiyah-Bott 1984): Symmetry group G 작용 시 *equivariant* version. Critical points 가 G-orbit; Goldstone modes 가 orbit tangent.

**Stratified Morse** (Goresky-MacPherson 1988): Singular space 의 *stratification* + 각 stratum 위의 Morse. Whitney stratification 의 일반화.

**→ SCC H5 와의 관계:** Option F1 (generic Morse + spinodal stratum split) 의 직접 framework. **post-bifurcation stable basin** 위에서 generic Morse → T-P-F-ε0-K Cat A 가능. spinodal critical surface 는 *separate stratum*. 만약 더 깊이 가려면 Morse-Bott 또는 equivariant Morse — Goldstone modes 명시적으로 처리.

**핵심 reference:**
- Milnor, *Morse Theory* (1963).
- Bott, "Nondegenerate critical manifolds" (*Annals of Math*, 1954).
- Atiyah & Bott, "The Yang-Mills equations over Riemann surfaces" (1984) — equivariant.
- Goresky & MacPherson, *Stratified Morse Theory* (1988).
- Lecture notes: [Toronto Morse 1.3 Genericity](https://www.math.toronto.edu/mgualt/Morse%20Theory/Notes5-8.pdf).

### §4.2 Sard's Theorem + Transversality — H5 Cat A 후보

**Sard 1942:** Smooth function f: M → N 의 critical values set 은 *Lebesgue measure 0*. 따라서 *generic* values 는 regular.

**Federer (geometric measure theory, 1969):** Sard 의 *finite-codimensional* version + analytic / polynomial maps 의 확장.

**Smale transversality** (1958~): Maps + submanifolds 간의 transverse intersection 이 *generic*. 이게 Morse density 의 직접 함의.

**Parametric transversality:** 1-parameter family of maps 에서 *대부분* element 가 transversal — 우리의 *parameter space* (λ, α, β, m) 에 대한 SCC 분석의 직접 도구.

**→ SCC H5 와의 관계:** **A.2.1 Generic Morse statement의 핵심 도구**. SCC E_λ(u) 가 real-analytic in u (polynomial) → ∇²E_λ(u*(λ)) 가 smooth in λ → Sard → critical values of `det H_T` 의 set이 measure zero in λ-space → open dense set of λ 에서 H_T non-degenerate. **단** Sard 가정의 *정밀 확인* 필요 (polynomial maps 의 algebraic structure).

**핵심 reference:**
- Sard, "The measure of the critical values of differentiable maps" (*Bull. AMS*, 1942).
- Hirsch, *Differential Topology* (1976).
- Wikipedia: [Sard's theorem](https://en.wikipedia.org/wiki/Sard's_theorem).

### §4.3 Bifurcation Theory — Crandall-Rabinowitz + Saddle-Node

**Saddle-node (fold) bifurcation:** Two fixed points (equilibria) collide and annihilate. *Critical equilibrium* 의 *one zero eigenvalue*. **Generic codim-1 bifurcation**. 또한 fold or limit point bifurcation.

**Crandall-Rabinowitz 1971:** Linearized eigenvalue problem 의 *simple zero eigenvalue* + transversality condition → *curve of nontrivial solutions* emanates from bifurcation point. 표준 도구 for *local bifurcation from simple eigenvalue*.

**Saddle-node + Hopf:** *Only* generic codim-1 bifurcations.

**→ SCC H5 와의 관계:** SCC T8 spinodal critical surface = saddle-node bifurcation locus. Crandall-Rabinowitz 가 (SN-iii) + (SN-iv) genericity 하에서 적용 — OP-OMS-033b OPEN (canonical.md L2502 SN3, SN4). H5 P3 (Crandall-Rabinowitz) 경로의 직접 적용.

**핵심 reference:**
- Crandall & Rabinowitz, "Bifurcation from simple eigenvalues" (*J. Functional Analysis*, 1971).
- Scholarpedia: [Saddle-node bifurcation](http://www.scholarpedia.org/article/Saddle-node_bifurcation).

### §4.4 Brouwer Fixed-Point Theorem — T_*의 핵심 도구

**Brouwer 1911:** Every continuous map of the *d-dimensional closed unit ball* to itself has a fixed point.

**Schauder extension** (1930): Infinite-dimensional version — *compact convex* subset of Banach space.

**Kakutani** (1941): Multi-valued (set-valued) version — *upper hemicontinuous* set-valued maps.

**Banach contraction principle** (1922): *Stronger* — contraction map → *unique* fixed point + constructive iteration. (Banach 가 *constructive*, Brouwer 가 *non-constructive*.)

**Self-consistency in mean-field theory:** 통계역학의 mean-field equation 은 *fixed-point equation* — input ↔ output 의 self-consistency 가 fixed-point.

**→ SCC T_* 와의 관계:** **B.2.2 (Brouwer existence) sketch 의 직접 도구**. ψ(T) = ⟨(u−⟨u⟩)²⟩_{π_T} 가 [T_min, T_max] 의 self-map + continuous → Brouwer → fixed-point exists. **Uniqueness 는 미보장** — multi-well E 에서 multiple fixed-points 가능 (Banach 처럼 contraction property 부족).

**핵심 reference:**
- Brouwer, "Über Abbildung von Mannigfaltigkeiten" (*Math. Ann.*, 1911).
- Schauder, "Der Fixpunktsatz in Funktionalräumen" (*Studia Math.*, 1930).
- Wikipedia: [Brouwer fixed-point theorem](https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem).
- Edinburgh slides: [Brouwer Theorem + Degree](https://webhomes.maths.ed.ac.uk/~v1ranick/slides/brouwer.pdf).

### §4.5 Persistent Homology — registry §1 D 분류 도구

**Edelsbrunner-Letscher-Zomorodian** (2002): *Persistent homology* — homology 가 filtration parameter 따라 *지속하는* features 추적. *Persistence diagram* 또는 barcode 로 표현.

**Stability theorem** (Cohen-Steiner, Edelsbrunner, Harer 2007): Persistence diagrams 사이의 *bottleneck distance* ≤ input data 사이의 *sup-norm* distance. 즉 **persistent homology 가 small perturbations 에 stable**. TDA 의 기초 정리.

**→ SCC 와의 관계:** **K_act = #PersComp** (Stage 3, D-ST-3) 의 직접 도구. Stability theorem 이 K_act 의 *robustness* 를 보장. ρ_pers (Stage 3 P, 분해능) 가 persistence threshold — bar length 가 *길어야* 해당 component를 count.

**핵심 reference:**
- Edelsbrunner, Letscher, Zomorodian, "Topological persistence and simplification" (*Discrete & Comput. Geom.*, 2002).
- Cohen-Steiner, Edelsbrunner, Harer, "Stability of persistence diagrams" (*Discrete & Comput. Geom.*, 2007).
- Edelsbrunner & Harer, *Computational Topology: An Introduction* (2010).

---

## §5. T_* 관련 specific

### §5.1 Self-Consistency Equations — T_* P1 (Brouwer route 보완)

**Mean-field self-consistency:** 통계역학의 mean-field 처리에서 *self-consistency equation* — 평균 자장이 *결과* 와 일치하도록 *반복적으로* 결정. Hartree-Fock 방법 (양자역학) 이 직접 사례.

**Iterative fixed-point methods:** Picard iteration, fixed-point iteration. *Contraction* 일 때 unique; *non-contraction* 일 때 multiple fixed-points 가능.

**Free energy variational principle:** $F(T) = -T \log Z(T)$ 의 *self-consistent* 조건이 fixed-point 와 동치.

**→ SCC T_* 와의 관계:** B.2.1 의 ψ(T) = variance map 이 *self-consistency* 의 직접 instance. Iterative computation 가능: T_0 → ψ(T_0) → ψ(ψ(T_0)) → ... → 수렴 시 fixed-point. *Convergence guarantee* 는 contraction property — SCC 의 multi-well E 에서는 *not guaranteed* (Brouwer existence 만).

### §5.2 Effective Temperature in Non-equilibrium — Cugliandolo의 review

**Cugliandolo 2011** (*J. Phys. A* 44, 483001; arXiv [1104.4901](https://arxiv.org/abs/1104.4901)): "The effective temperature" — *deviations from equilibrium FDT* 에서 정의되는 effective T 의 종합 review.

**Out-of-equilibrium 시스템:** Kinetic temperature 가 *time-scale-dependent effective T* 로 대체. *Slow dynamics* (aging glass, granular media, active matter) 에서 중요.

**Multiple notions of T_eff:** Cugliandolo 가 *여러* effective T 정의를 비교 — FDT 기반, granular, active matter 등. **모두 환경 외생적**.

**→ SCC T_* 와의 관계:** OP-0021 Route A (Mori-Zwanzig) 의 직접 학문적 위치. Cugliandolo 의 어떤 effective T notion 도 *환경 statistics* 를 요구 → **COB 위반**. 이게 Route C (관찰자-개인 noise scale, §5.4 JND) 가 SCC 에서 자연스러운 *유일한* 옵션인 이유.

**핵심 reference:**
- Cugliandolo, "The effective temperature" (*J. Phys. A*, 2011) — [arXiv 1104.4901](https://arxiv.org/abs/1104.4901).

### §5.3 Information-Theoretic Temperature — Jaynes MaxEnt

**Jaynes 1957** (*Phys. Rev.*): MaxEnt principle — 알려진 constraints 하에서 *최대 entropy* 분포 선택. Temperature 가 *Lagrange multiplier* — *관찰자의 무지* 측정.

**Shannon entropy, Cover-Thomas information theory:** Entropy 가 *관찰자의 정보 부족* 의 정량 측정. Temperature 가 *어느 정도 자세히 보는가* 의 dual.

**→ SCC T_* 와의 관계:** T_* 를 *관찰자의 information capacity* 또는 *resolution scale* 로 해석. Route C 의 자연스러운 형식화. T (Stage 0 sensor transformation) 의 *channel capacity* 가 T_* 를 결정 → Route C + Route 3 (Information-theoretic) hybrid.

**핵심 reference:**
- Jaynes, "Information theory and statistical mechanics" (*Phys. Rev.*, 1957).
- Cover & Thomas, *Elements of Information Theory* (1991).

### §5.4 Weber-Fechner Law + JND — Route C 정식화의 *직접* framework

**Ernst Weber 1834:** *Just noticeable difference (JND)* 가 stimulus magnitude 에 *비례*. (100g → 105g 구별 가능 시 JND = 5g; 200g → 210g 구별, JND 비례.)

**Gustav Fechner 1860** *Elemente der Psychophysik*: Sensation intensity = *logarithm* of stimulus intensity. Weber 법칙의 *적분*.

**→ SCC T_* 와의 직접 관계:** **Route C 의 가장 자연스러운 formalization**. T_* 는 *관찰자의 JND* — 관찰자가 *구별 가능한* u 의 최소 차이. Weber-Fechner 의 *logarithmic* dependence가 T_* 의 자연스러운 scale.

구체적으로:
- T_* = α · ⟨u⟩ (Weber 비례성) — *intensity-dependent* threshold.
- 또는 T_* = constant ξ_* 의 free parameter ∈ B_ξ (관찰자가 선택, OMS-1 ξ resident).

이 두 후보 중 **constant T_* ∈ B_ξ** 가 *가장 가벼움* — Route C 의 G1 (axiomatically free P).

**핵심 reference:**
- Weber, *De Tactu* (1834).
- Fechner, *Elemente der Psychophysik* (1860).
- Wikipedia: [Weber-Fechner law](https://en.wikipedia.org/wiki/Weber%E2%80%93Fechner_law), [Just-noticeable difference](https://en.wikipedia.org/wiki/Just-noticeable_difference).

---

## §6. H5 관련 specific

### §6.1 Spinodal Critical Phenomena — universality + RG

**Mean-field critical exponents:** Spinodal critical point 에서 *order parameter* ψ 가 (β/α − β/α_c)^β 로 scale. Mean-field exponent β = 1/2.

**Universality classes:** Renormalization group (RG) 가 *microscopic detail-independent* universal exponents 추출. SCC T8 가 어느 universality class? — graph Laplacian + double-well → Ising-like Z₂ universality?

**Renormalization group:** Wilson 1971~. *Scale invariance* at critical point.

**→ SCC H5 와의 관계:** SCC T8 spinodal universality class 식별이 H5 의 *meta-context*. 만약 Z₂ Ising-like 면 H5 Goldstone mode 가 *Z₂ symmetry breaking* 의 *order parameter direction*. 정확한 식별은 별도 작업이지만 H5 working file에 한 줄 명시 가능.

### §6.2 Goldstone Modes in Lattice Systems

**Anderson-Higgs mechanism** (1962~): Gauged symmetry breaking 에서 Goldstone modes 가 *massive* Higgs bosons 와 mix. SCC 에는 직접 적용 안 됨 (no gauge), 단 *analog* — graph 구조가 effective gauge 역할.

**Magnetic spin systems:** Heisenberg ferromagnet → Goldstone = magnon (spin wave). Z₂ Ising → *no* continuous Goldstone (discrete symmetry).

**Finite systems:** Mermin-Wagner 가 1D/2D 에서 continuous symmetry breaking 차단. SCC 가 어느 lattice dimension? — 2D grid 가 표준. *Finite size* 효과가 Mermin-Wagner 를 약화.

**→ SCC H5 와의 관계:** SCC formation 의 symmetry breaking 이 *discrete* (Z₂, formation 위치 선택) 인지 *continuous* (rotational, translation) 인지 graph 구조에 의존. Generic graph 에서는 *discrete* — Mermin-Wagner 불적용. **H5 Goldstone mode 는 discrete spinodal critical mode** — H5 P1 (Sard) 적용 가능.

### §6.3 Generic Morse via Sard (refined for polynomial maps)

**Polynomial maps:** SCC E_λ(u) 가 *polynomial in u* (degree 4 from double-well + degree 2 from Laplacian). 따라서 *algebraic geometry* 도구 사용 가능.

**Hironaka resolution** (1964): Algebraic singularities 의 *resolution* — polynomial maps 의 singular set 의 *desingularization*.

**Generic property in algebraic geometry:** *Open dense* set in parameter space — measure-theoretic 보다 *Zariski-open* 이 algebraic version. Sard 의 algebraic analog.

**→ SCC H5 와의 관계:** **A.2.1 Generic Morse 의 정밀한 statement 도구**. SCC E_λ 의 polynomial form 이 Sard 정리의 *strong* version (algebraic) 을 적용 가능하게 함. 즉 *measure zero* 대신 *Zariski-codimension ≥ 1* 인 set 위에서만 H_T degenerate.

**핵심 reference:**
- Hironaka, "Resolution of singularities" (*Annals of Math*, 1964).
- Hartshorne, *Algebraic Geometry* (1977).

---

## §7. SCC 이론과의 연결 — 두 잔류 U가 어디에 위치하는가 (synthesis)

### §7.1 T_* in big picture

**가장 자연스러운 framework:** §5.4 (Weber-Fechner / JND) — *관찰자의 분해능*.

**이유:**
1. COB 원칙 하에서 외부 환경 가정 0 → §5.2 (Cugliandolo effective T) 거부.
2. Self-consistency (§5.1) 은 *기술적* 도구 (Brouwer existence) 이지만 *해석* 미제공.
3. Information-theoretic (§5.3) 는 §5.4 의 더 일반적 form.
4. §5.4 가 *직접* observer-personal — Route C 의 G1 (axiomatically free P) 와 정확히 일치.

**보완:** §5.1 (Brouwer existence) 는 T_* 의 *수학적 well-posedness* 확인 도구로 사용. §5.4 는 *해석* 제공. 둘이 *상보적*.

**잠재 정리 (내일 draft):**
> **OP-T*-FIXED-POINT (Statement Draft):** T_* ∈ B_{T_*} ⊆ B_ξ 는 관찰자의 stochastic resolution 으로 정의되는 자유 매개변수 (P). Brouwer fixed-point 가 ψ(T) = ⟨(u−⟨u⟩)²⟩_{π_T} 의 self-map property 하에서 보장하는 fixed-point 의 *집합* B_{T_*}^{FP} ⊆ B_{T_*}. 관찰자가 어느 fixed-point 를 *선택*하는가는 추가 결정 (JND 또는 information-theoretic criterion).

### §7.2 H5 in big picture

**가장 자연스러운 framework:** §3.1 (Cahn-Hilliard) + §3.2 (Goldstone) + §4.1 (Morse) + §4.2 (Sard) 의 **합성**.

**이유:**
1. SCC = Cahn-Hilliard graph version → spinodal critical surface 가 *intrinsic* feature.
2. Spinodal 임계점에서 Hessian zero eigenvalue = *Goldstone mode* (symmetry breaking).
3. Generic regime 에서 Sard's theorem + Morse density → H5 Cat A 가능.
4. Spinodal critical surface = codim-1 stratum → *stratified Morse* (§4.1 Goresky-MacPherson) 또는 generic + stratum split (Option F1).

**§3.4 Catastrophe theory 의 역할:** SCC T8 임계점이 *cusp catastrophe* (2-parameter) 또는 *fold catastrophe* (1-parameter) 로 *분류 가능* — H5 의 *systematic* 처리에 도움. 단 *unifying* framework은 아니고 *분류 도구*.

**잠재 정리 (내일 draft):**
> **OP-H5-MORSE-SPINODAL (Statement Draft):** SCC E_λ(u) 는 (λ, α, β, m) parameter space 의 *Zariski-open dense* subset 에서 Morse functions in u (Sard + algebraic geometry). T8 spinodal critical surface `Σ_T8 ⊆ Σ_Hess` 는 *intrinsic codim-1 stratum* — 거기서 Hessian 이 *Goldstone mode* 에 의해 degenerate. T-P-F-ε0-K Cat A regime = post-bifurcation stable basin (codim-0 open) 한정. Spinodal stratum 은 separate treatment.

### §7.3 두 U 의 *공통* 구조 — Free Energy Principle 통합?

**관찰:** 두 잔류 U 가 *우연히* SCC 의 핵심 사건과 직결되지 않음. *체계적* 이유:

1. **T_***: 관찰자의 sampling resolution = FEP 의 *generative model 의 noise level*.
2. **H5**: spinodal Goldstone mode = FEP 의 *symmetry-breaking moment* (objects 가 emerge 하는 순간).

**Free Energy Principle (Friston) 안에서 통합:**
- SCC u-field = FEP 의 *internal states*.
- T_* = generative model 의 *precision* (inverse variance).
- H5 spinodal = active inference 의 *belief crystallization* moment.
- K_act = posterior dimensionality.

**잠재 메타-결론:** SCC 전체가 FEP 의 *수학적 specialization* — *graph-based generative model + spinodal phase transition + persistent homology readout*. 두 잔류 U 는 FEP의 *두 핵심 사건* (model 의 noise level + symmetry breaking) 의 SCC 표현.

이 메타-결론은 *내일 작업의 직접 결과* 가 아니라 *향후 작업* 의 leading hypothesis. 단 §7.1 / §7.2 의 reference 인용 시 FEP 를 인용할 수 있음.

---

## §8. 내일 plan을 위한 권장 (1-paragraph each)

### §8.1 H5 working file 작성 시

**우선 인용 reference:**
- **§4.2 Sard's theorem** (Sard 1942, Hirsch 1976) — A.2.1 Generic Morse statement 의 기초.
- **§3.1 Cahn-Hilliard** (Maier-Paape & Wanke 1998) — SCC E_λ 의 spinodal 분석 표준.
- **§4.1 Morse density** (Milnor 1963, Toronto notes) — Morse functions 의 genericity.
- **§6.3 polynomial maps** (Hironaka 1964) — Sard 의 algebraic strengthening.

**Auxiliary inspiration:**
- **§3.2 Goldstone modes** (Goldstone 1961, MIT 8.334) — *왜* spinodal 에서 zero eigenvalue.
- **§2.5 HKB model** (Haken-Kelso-Bunz 1985) — H5 ↔ *perceptual phase transition* 의 직접 parallel.
- **§3.4 Catastrophe theory** (Thom 1972, Zeeman 1977) — T8 spinodal 의 *cusp vs fold* 분류 가능성.

### §8.2 T_* working file 작성 시

**우선 인용 reference:**
- **§4.4 Brouwer 1911** — B.2.2 (existence) sketch 기초.
- **§5.4 Weber-Fechner / JND** (Weber 1834, Fechner 1860) — Route C 의 직접 framework.
- **§1.2 Brouwer intuitionism** — constructive vs non-constructive 처리의 깊이.
- **§1.4 Lawvere fixed-point** (1969) — T_* self-reference 의 *universal* 구조.

**Auxiliary inspiration:**
- **§5.2 Cugliandolo 2011** — effective T 의 학문 위치 + Route A/B 폐기 사유.
- **§5.3 Jaynes 1957 MaxEnt** — information-theoretic 해석 (Route C + G3).

### §8.3 §7.3 FEP 통합 가설

**Hypothesis to test (별도 작업):** SCC = FEP 의 graph-based specialization.

**인용 시:**
- Friston 2010 (*Nat. Rev. Neuro.*) — FEP introduction.
- Friston 2019 ([arXiv 1906.10184](https://arxiv.org/abs/1906.10184)) — FEP for particular physics.
- Friston et al. 2018 — Markov blankets.

만약 내일 작업이 충분히 진행되면 §7.3 hypothesis 를 99_summary 에 *leading question for W9+* 으로 등록.

---

## 사용된 검색 (15+ web search queries, 2026-05-18 EOD)

### Mathematical tools
- "Sard's theorem generic Morse functions transversality polynomial maps"
- "Cahn-Hilliard spinodal decomposition mathematical analysis critical point"
- "Goldstone modes spontaneous symmetry breaking lattice finite systems"
- "Crandall-Rabinowitz bifurcation theory saddle-node fold critical point"
- "Brouwer fixed-point theorem self-consistency mean-field statistical mechanics"
- "persistent homology topological data analysis Edelsbrunner stability theorem"
- "Lawvere fixed-point theorem Gödel self-reference categorical foundations"

### Perception + non-equilibrium physics
- "effective temperature non-equilibrium fluctuation-dissipation Cugliandolo review"
- "Weber-Fechner law just noticeable difference psychophysics perceptual threshold"
- "Free Energy Principle Friston active inference Markov blanket perception"
- "multistable perception phase transition Kelso synergetics Haken self-organization"
- "predictive coding Rao Ballard hierarchical perception cortex Bayesian inference"
- "catastrophe theory Thom Zeeman perception bistability cusp fold singularity"

### Philosophy
- "Brouwer intuitionism constructive mathematics type theory Martin-Löf"
- "embodied cognition phenomenology Merleau-Ponty Varela enactive perception"

---

## 부록: 핵심 references (compressed list)

| Author | Year | Work | Section |
|---|---|---|---|
| Brouwer | 1911 | Fixed-point theorem | §1.2, §4.4 |
| Goldstone | 1961 | SSB theorem | §3.2 |
| Hironaka | 1964 | Resolution of singularities | §6.3 |
| Cohen-Steiner et al. | 2007 | Persistence stability | §4.5 |
| Crandall & Rabinowitz | 1971 | Bifurcation from simple eigenvalue | §4.3 |
| Cahn & Hilliard | 1958 | Free energy of nonuniform system | §3.1 |
| Maier-Paape & Wanke | 1998 | Spinodal decomposition rigorous | §3.1 |
| Sard | 1942 | Critical values measure zero | §4.2 |
| Lawvere | 1969 | Categorical fixed-point | §1.4 |
| Milnor | 1963 | Morse theory | §4.1 |
| Bott | 1954 | Nondegenerate critical manifolds | §4.1 |
| Atiyah & Bott | 1984 | Equivariant Morse | §4.1 |
| Goresky & MacPherson | 1988 | Stratified Morse | §4.1 |
| Cugliandolo | 2011 | Effective temperature review | §5.2 |
| Jaynes | 1957 | MaxEnt | §5.3 |
| Weber | 1834 | JND | §5.4 |
| Fechner | 1860 | Elemente der Psychophysik | §5.4 |
| Haken, Kelso, Bunz | 1985 | HKB phase transition | §2.5 |
| Thom | 1972 | Structural Stability and Morphogenesis | §3.4 |
| Zeeman | 1977 | Catastrophe Theory selected papers | §3.4 |
| Rao & Ballard | 1999 | Predictive coding visual cortex | §2.1 |
| Friston | 2010 | FEP unified brain theory | §2.1, §7.3 |
| Friston et al. | 2018 | Markov blankets of life | §2.1, §7.3 |
| Helmholtz | 1860s | Unconscious inference | §2.1 |
| Merleau-Ponty | 1945 | Phenomenology of Perception | §1.1 |
| Varela, Thompson, Rosch | 1991 | The Embodied Mind | §1.1 |
| Martin-Löf | 1972~ | Intuitionistic type theory | §1.2 |
| Edelsbrunner et al. | 2002 | Topological persistence | §4.5 |

---

## EOD 메모 (작성자 → 사용자)

- 본 file은 **2026-05-18 EOD에 agent 작성**, 내일 작업의 *reference 백서* 용도.
- 사용자가 EOD 검토 시 ① 추가 reference 보완, ② §7.3 FEP 통합 가설 평가, ③ §8 권장 우선순위 조정 가능.
- 본 file은 *읽기용* — 내일 작업 시 02_H5/03_T_star working file 작성 시 *인용 출처*.
- canonical / theorem_status / auxiliary_structures_master 어느 것도 *수정 없음*. 본 file은 *외부 학문 백서* 만.
- 내일 plan §11 verification 의 추가 항목: 본 01_pre_brainstorm.md 의 §1–§6 reference 가 02_H5 / 03_T_star 에서 *실제 인용* 됐는지.

**End of pre-brainstorm. 내일 출발 위치 명확.**

---

## §POST-SEAL APPENDIX (2026-05-19 evening) — Topological Mathematics Reference Base

본 day 의 CV-1.18 SEAL 종료 후 evening session 의 *19-phase Manifold Topology Methodology Program* 의 reference base. 사용자가 사전 제공한 *두 개의 위상수학 종합 보고서* 가 informant 였음:

1. **Report A** — 푸앵카레 추측 증명 (Hamilton-Perelman 1982-2003)
2. **Report B** — 다양체 위상수학 종합 (3D + 4D + ≥5D)

### A.1 Perelman 7-Tool 정리 (Report A 표)

| 도구 | 분야 | 수식/정의 | 증명 역할 |
|---|---|---|---|
| Ricci flow + DeTurck gauge | 미분기하학, PDE | $\partial_t g_{ij} = -2 R_{ij}$ | 전체 program 의 동역학적 뼈대 |
| Hamilton-Ivey pinching | 기하학적 해석학 | $\mathrm{Rm} \geq -\phi(R) R$ | 고곡률 영역을 "거의 비음 아닌 곡률"로 정리 |
| $\mathcal{F}, \lambda, \mathcal{W}, \mu, \nu$ entropy | 기하학적 해석학 | 엔트로피/에너지 + 단조성 | breathers 배제, 솔리톤 식별, 비붕괴성 기반 |
| $\mathcal{L}$-길이, 축약거리, 축약부피 | 비교기하 | $L, l, \tilde{V}$ | blow-up limit 비붕괴성 + 축소기하 제어 |
| 켤레 열방정식, Harnack, log-Sobolev, pseudolocality | 해석학, PDE | $\Box^* u = 0$, $v$-quantity | 곡률 폭주 억제 + 엔트로피 국소화 |
| 콤팩트성 + blow-up + 고대 $\kappa$-해 | 기하학적 해석학 | rescaling + smooth convergence | 특이점 모델 추출 + 정준 이웃 도출 |
| 정준 이웃 + Ricci flow with surgery | 미분기하, 3-다양체 | $\varepsilon$-neck, $\varepsilon$-cap, $\delta$-cutoff | neck 절단 + 흐름 재시작 + 위상 추적 |
| 최소원판 + 곡선단축 + 유한시간 소멸 | 대수적 위상 | $dA_t/dt \leq -2\pi - \frac{1}{2} R_{\min} A_t$ | 푸앵카레 특수경로 마지막 단계 |

### A.2 Perelman 핵심 단조성 공식

$$\mathcal{W}(g, f, \tau) = \int_M [\tau (\vert \nabla f\vert ^2 + R) + f - n] (4\pi\tau)^{-n/2} e^{-f}\,dV$$

$$\frac{d}{dt} \mathcal{W} = \int_M 2\tau \left\vert \mathrm{Ric} + \nabla^2 f - \frac{1}{2\tau} g\right\vert ^2 (4\pi\tau)^{-n/2} e^{-f}\,dV \geq 0$$

**SCC Tier 1 매핑 결과** (post-SEAL Phase 1A): Bakry-Émery $W_{SCC}$ framework 시도 → universality misclassification (EW → Allen-Cahn → Model B) 으로 부분 retract.

### B.1 11-Method Category 표 (Report B)

| 방법 범주 | 대표 도구 | 전형적 쓰임 |
|---|---|---|
| 대수적 | 교차형식, Whitehead torsion, characteristic classes, assembly map | Freedman, Donaldson, Novikov/Borel/Farrell-Jones |
| 기하적 | 쌍곡기하, Mostow rigidity, Dehn filling | JSJ → atoroidal hyperbolic 판정 |
| 해석적/PDE | Ricci flow, 최대원리, 엔트로피, reduced volume | Hamilton-Perelman, no local collapsing |
| 위상적 절단 | prime decomposition, 비압축 곡면, JSJ, cobordism | Kneser-Milnor, Haken/Waldhausen |
| Morse + handle | Morse 함수, handle attachment, Cerf 변형 | h-cobordism, surgery, Kirby calculus |
| 게이지 이론 | ASD Yang-Mills, Seiberg-Witten, moduli | 4D smooth 비가환/가환 불변량 |
| 수술 이론 | normal map, structure set, surgery exact sequence, $L_n(\mathbb{Z}\pi)$ | ≥5D manifold 분류 표준 |
| $K/L$-이론 | Whitehead group, $K_*$, quadratic forms | s-cobordism, Novikov/Borel/FJ 대수적 핵심 |
| 제어 위상수학 | controlled h-cobordism, bounded surgery, ends | 비콤팩트/끝단, Quinn, Farrell-Jones |
| 기하군론 | hyperbolic groups, CAT(0), cube complexes | Virtual Haken, Agol-Wise |
| 계산/알고리즘 | normal surface, Regina, SnapPy | 3-sphere recognition, Thurston norm |

### B.2 3-다양체 11 핵심 정리

Kneser-Milnor 소분해 (1929-1962) → Haken/Waldhausen (1968) → JSJ 분해 (Jaco-Shalen-Johannson) → Mostow-Prasad 강직성 (1968-73) → Thurston hyperbolization (Haken) → Hyperbolic Dehn surgery → Thurston geometrization 추측 → Hamilton-Perelman Ricci flow (1982-2003) → Agol-Wise Virtual Haken (2012) → Schoen-Yau minimal surfaces.

### B.3 4D + ≥5D 14 핵심 결과

Morse + handle (Milnor) → Smale h-cobordism (1961, ≥5D Poincaré) → s-cobordism (Whitehead torsion) → BNW Surgery Theory → Novikov conjecture → Borel conjecture → Farrell-Jones conjecture → Controlled topology (Quinn) → Freedman topological 4D (1982) → Donaldson gauge (1983) → Seiberg-Witten (Witten 1994) → Kirby calculus → **Smooth 4D Poincaré (OPEN)**.

### B.4 차원별 *불변량* 분기 (메타-패턴)

> "방법론의 진짜 분기점은 *"무엇을 불변량으로 삼는가"*에 있음."

| 차원 | 불변량 종류 | SCC 유비 시도 |
|---|---|---|
| 3D | 기하 그 자체 (Mostow rigidity) | Tier 3 — **DROPPED** (hyperbolicity 부재) |
| ≥5D | simple homotopy, structure set, $L$-군 | Tier 4 — Phase 4 $R_K^{SCC}$ (L-theory ≠ K_0 정정) |
| 4D | ASD instanton, monopole moduli | Tier 10 — 추측 only |

### C.1 14-Tier Mapping (post-SEAL Phase 0-18)

| Tier | Report 출처 | post-SEAL 결과 |
|---|---|---|
| 1 Ricci Flow (Perelman) | Report A 전체 | ⚠️ Phase 1A universality 잘못 → 4 retractions |
| 2 Decomposition (JSJ) | Report B §2.1-2.3 | ✓ Phase 3 정정 → graph moduli stratification |
| 3 Mostow Rigidity | Report B §2.4 | ❌ DROPPED (hyperbolicity 부재) |
| 4 Surgery Theory | Report B §3.4 | ⚠️ Phase 4 representation ring $R_K^{SCC}$ |
| 5 h-/s-Cobordism | Report B §3.2-3.3 | 추측, 작업 안 됨 |
| 6 Novikov/Borel/FJ | Report B §3.5-3.7 | Tier 8 에 subsumed |
| 7 Controlled Topology | Report B §3.8 | ✓ T11 Γ-convergence Cat A 이미 작동 |
| 8 Assembly Maps | Report B §3.7 | ✓ Phase 8 CN-COB Assembly Map |
| 9 Topological 4-Manifold | Report B §3.9 | 추측, 작업 안 됨 |
| 10 Gauge Theory | Report B §3.10-3.11 | 추측, 작업 안 됨 |
| 11 Cubulation | Report B §2.9 | 추측, 작업 안 됨 |
| 12 Minimal Surface | Report B §2.10 | 추측, 작업 안 됨 |
| 13 Morse + Handle | Report B §3.1 | ✓ 이미 작동 중 |
| 14 Computational | Report B §"계산" | ✓ scc/ 이미 작동 |

### C.2 *Naive Import 의 8 Systematic Biases* (post-SEAL catch)

1. EW universality (실제: 비국소 Allen-Cahn / Model B)
2. Model A $z = 2.17$ (실제: Model B $z \approx 3.75$, mass-conserved)
3. Coarsening $t_\times \sim (\beta/\alpha)^{3/2}$ (실제 Bray 1994: $t_\times \sim \alpha/\beta$)
4. $D_f^{(k)} = (n-1) - k$ codim 산수 오류
5. H-int formation 배제
6. Closure RG-irrelevance tree-level only
7. $D_f = 11/8$ as theorem (실제: SLE_3 conjecture)
8. k(k+1)/2-1 single-graph stratification 잘못

### D. References (post-SEAL 추가)

**Hamilton-Perelman 원전**:
- Hamilton (1982) *J Diff Geom* 17:255; Perelman (2002, 2003 ×2) arXiv:math/0211159, 0303109, 0307245
- Kleiner-Lott (2008), Morgan-Tian (2007), Cao-Zhu (2006) — 표준 전개

**Statistical physics / dynamic universality**:
- Hohenberg-Halperin (1977) *RMP* 49:435 — Model A/B classification
- Edwards-Wilkinson (1982), Kardar-Parisi-Zhang (1986)
- Allen-Cahn (1979), Lifshitz-Slyozov (1961)
- Bray (1994) *Adv Phys* 43:357 — phase ordering kinetics
- Bray-Rutenberg (1994), Funaki-Spohn (1997), Rubinstein-Sternberg (1992)

**Critical phenomena / RG**:
- Onsager (1944), Wilson-Fisher (1972), Wansleben-Landau (1991), Kamieniarz-Blöte (1993), Pelissetto-Vicari (2002)

**Probability / SDEs**:
- Bakry-Gentil-Ledoux (2014), Otto-Villani (2000), Lions-Sznitman (1984), Tanaka (1979), Freidlin-Wentzell (1998)

**Random fields / fractals**:
- Adler-Taylor (2007), Sheffield (2007), Falconer (2003), Schramm (2000), Smirnov (2010), Chelkak-Smirnov (2012), Boissonnat-Pritam (2021)

**Algebraic topology / assembly**:
- Browder (1972), Wall (1970), Ranicki (2002), Davis-Lück (1998), Hairer (2014)

**3-manifold + 4-manifold**:
- Kneser, Milnor, Haken, Waldhausen, Jaco-Shalen, Johannson, Thurston, Mostow, Schoen-Yau, Agol-Wise
- Freedman (1982), Donaldson (1983), Witten (1994), Kirby (1989)

### E. 본 Appendix 의 *의미*

> **Manifold topology 80년 역사 (1904 Poincaré → 2003 Perelman → 2012 Agol) 의 *전체 도구상자* 가 SCC 에 *naive import* 시 *systematic bias 8개* 만들었음을 정직하게 기록. 이게 *learning resource* 로서의 영구 보존 — 향후 작업 시 *동일 함정 회피* 의 reference. Working layer (foundation_reset + v1 + W8_Day2_evening_manifold_topology_report + v0 archives) 가 canonical 보호 + 학습 자료 archive 의 이중 역할.**

본 appendix 가 *내일 작업의 reference 백서* (위 EOD 메모 정신의 *직접 확장*) — `04_manifold_topology_program_plan.md` 의 §B-§J + §R 와 cross-referenced, `99_summary.md §POST-SEAL EXTENSION` 와 *3-file post-SEAL extension reference triangle* 형성.

---

*End of post-SEAL appendix. Topological mathematics reference base 통합 완료.*
