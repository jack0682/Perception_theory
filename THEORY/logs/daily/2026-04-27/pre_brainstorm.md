# pre_brainstorm.md — 2026-04-27 W5 Day 1 (사전 brainstorm)

**Type:** Pre-session brainstorm. Free-form thinking notes — plan.md의 *strict structure* 옆에 두는 *raw thinking*.
**Status:** Drafted 2026-04-26 evening (W4 extended close 직후) for next-day W5 Day 1 (Mon 04-27).
**Use:** Day 1 morning 09:00 시작 전 빠르게 review. Plan 외의 *예상치 못한 issues + conjectures + memory refresh*.

---

## §0. 마음의 상태 (W4 close → W5 진입 감각)

W4의 8일이 *밀도 높은 마라톤*이었다. 04-19 N-1 reframing → 04-26 V5b-T canonical merge. 매일 12-14h work, 7+ daily artifacts × 8 days = ~60+ daily docs, ~30 scripts, 3 canonical merges (v1.2 → v1.3 04-25 → v1.4 04-26 extended).

W5 진입은 *처음으로 안정된 mathematical body*에서 출발. 더 이상 critical blockers (F-1/M-1/MO-1) 없음, σ-framework canonical에, V5b-T canonical에. 즉 *aggressive 작업이 가능한 평지*.

그러나 W5의 Day 1이 *공격적 marathon kickoff*라는 것은 W4의 *가장 마라톤스러운 day가 W5의 평균 day*가 됨을 의미. 마음 준비 필요.

---

## §1. G0의 *진짜 어려움* (plan에 안 보일 수 있는)

Plan은 G0를 "5 statements canonical-merge"로 단순화. 그러나 현실은 다음 5 sub-issues 존재:

### 1.1 Lemma 1 (irrep decomposition)의 well-posedness 검증

**Plan**: "Hessian commutes with $G_u$-action → eigenspaces decompose into irreps"

**진짜 어려움**: $G_u = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$가 자동으로 finite group 인가? 무한 자동군 (예: $\mathbb{Z}^d$ on infinite lattice)에서 이 statement 적용 안 됨. **Finite graph 가정이 essential** — proof step 1에 명시 필요.

또 *trivial $G_u = \{e\}$ case*: irrep decomposition is trivial (1 irrep, the regular). Statement validity 유지하나 informative 가치 없음. *Generic minimizer (non-trivial $G_u$) 가정* 필요한가? Plan의 statement은 generic case 강조 안 함. 이것이 W5 Day 1 morning의 *first technical hurdle*.

### 1.2 Lemma 2 (nodal count) 의 (iii) sub-statement

**Plan**: "n_k=1 iff $\phi_k$ is constant (volume tangent)"

**진짜 어려움**: 정확히는 $n_k=1$ iff $\phi_k$가 *연결 그래프 위에서 sign-definite (positive 또는 negative throughout)*. Constant function은 trivial sign-definite case. 그러나 *non-constant sign-definite* eigenvector가 있나? Yes — *first non-Goldstone mode*가 sign-definite할 수 있음.

따라서 Plan의 "n_k=1 iff constant"는 **부정확**. 정확한 statement: "n_k=1 iff sign-definite" — 이게 더 generally true. *Volume tangent ($\phi_0 = 1/\sqrt{n} \cdot \mathbf{1}$)은 trivial sign-definite case*.

이 correction이 Day 1 morning의 *second hurdle*.

### 1.3 Lemma 2 (iv) symmetry constraint

**Plan**: "n_k constrained by $G_u$-action (e.g., n_k divisible by minimum orbit size)"

**진짜 어려움**: "Divisible by minimum orbit size"가 항상 sharp constraint? 반례 가능성:
- Eigenvector가 *invariant* under $G_u$ (즉 fixed point of action) → orbit size 1 → divisibility trivial.
- Eigenvector가 non-invariant → orbits of size > 1 → constraint sharp.

따라서 (iv)는 *non-invariant eigenvectors only*. Plan에 명시 안 됨.

### 1.4 Lemma 3 (Goldstone-saturation) 의 정확한 wording

**Plan**: "$(\partial_{x_i} u^*, \delta u_{x_i}^{ref})$ saturate $\ell=1$ angular sector by IBP"

**진짜 어려움**: $\delta u_{x_i}^{ref}$가 정확히 무엇인가? Plan에 정의 없음. Two interpretations:
- (A) $\delta u_{x_i}^{ref} = \partial_{x_i} u^{ref}$ where $u^{ref}$ = some reference disk profile. 이 경우 IBP가 trivial.
- (B) $\delta u_{x_i}^{ref}$ = unit vector in $\ell=1$ angular subspace. 이 경우 IBP가 saturation을 보여줌.

W4 04-24 04_orbital_proofs §3에서는 (B). Plan needs to specify.

### 1.5 Theorem 3 (σ at uniform on $D_4$ grid) 의 *closed form*의 정확성

**Plan**: "$\lambda_k = \beta W''(c) + 4\alpha\lambda_k^{Lap}$"

**진짜 어려움**: 부호 confusion. $W''(c) = -1$ at $c=0.5$ (W4-04-24 NQ-128 분석에서 사용). 따라서 $\lambda_k = -\beta + 4\alpha\lambda_k^{Lap}$. 이 식이 negative 가능 (low $k$ at sub-spinodal $\beta$ regime). *Spinodal 정의*에 의존.

또 $\lambda_k^{Lap}$ ordering: $\lambda_0^{Lap} = 0 < \lambda_1^{Lap} \leq ...$. $k$ index in σ vs $k$ index in Laplacian — *consistent indexing*?

이 detail이 Day 1 morning에서 가장 시간 걸릴 것. ~30min 추가 가능성.

---

## §2. G1 V5b-F H1/H2/H3 *진짜* 예측

Plan은 H1 (bulk-localized) most likely. 그러나 brainstorm 시 다른 고려:

### 2.1 H2 (mode mixing)이 사실 가장 깨끗한 가설일 수도

**왜?**: Translation symmetry는 *interior에서만 valid*, boundary 에서 broken. 이는 *exact decomposition*: eigenvector = (translation interior part) + (boundary localized part). Linear superposition.

**Test**: Mode decomposition coefficients α (translation), β (boundary):
- $\alpha^2 + \beta^2 = 1$ (orthogonal basis if 직교)
- α ≈ 0.83 (W4-04-26 NQ-170c에서 측정한 max overlap)

만약 α, β ≈ 0.83, 0.55: H2 strong. $\alpha^2 + \beta^2 = 0.69 + 0.30 = 0.99 ≈ 1$ — 직교 분해 확인.

**가능성**: H1 + H2 둘 다 partial true. *Bulk-localized translation Goldstone이 boundary mode와 mix되는 것*이 자연스런 picture.

### 2.2 H3 (PN barrier modification) — 사실 제일 보수적

**왜?**: H3는 mode가 *fully Goldstone-character*라는 강한 주장. 만약 H3 true → eigenvalue should be "near zero" but boundary-lifted.

**Test**: Eigenvalue ordering. H3 if Goldstone candidate가 *spectrum의 lowest non-tangent* 위치에 있고, λ가 small (say < 0.1).

W4-04-26 NQ-170c: 2D free BC ζ=0.5 Goldstone @ mode 5 with λ=1.749 — *spectrum의 5번째 mode이고 λ가 큼*. 따라서 H3 *unlikely*.

### 2.3 결론: H1 + H2 mixed가 most likely

Plan은 H1 main, but reality may be H1+H2 mixed. Day 1 evening 분석 시 *명시적 mixed verdict 가능성* 인지.

### 2.4 Bulk region 정의의 trickiness

**Plan**: "interior 8 ≤ x,y ≤ 12 in L=20"

**진짜 어려움**: 8 to 12가 5x5 = 25 sites. L=20 grid의 25/400 = 6.25%만 "interior". 이 narrow definition으로 bulk overlap > 0.95 보기 어려울 수 있음 (boundary lifting이 5x5 narrow window 안까지 침투).

**Better defn**: interior 4 ≤ x,y ≤ 16 (12x12 = 144 sites = 36%). 더 넓은 interior.

또는 *radial* definition: distance from boundary > xi_0. ζ=0.5 → ξ_0 = 0.5 → distance > 0.5 means *exclude only edge column*.

Day 1 evening에 multiple bulk definitions 시도 가능.

---

## §3. Cross-Cutting Concerns

### 3.1 σ-framework supporting lemmas의 *paper relevance*

W5 G0가 §13 깊이로 격상되면 Paper 1 (Foundational SCC)에서 *§4 σ-Framework* 핵심 sub-section. Without G0, paper는 "supporting structures are working level" caveat. With G0, paper는 *self-contained mathematical statement*.

이 paper-relevance가 G0를 P0 MUST로 만드는 *진짜 이유*. Plan에서 다소 약한 언급.

### 3.2 V5b-F (G1)와 multi-formation σ (G3)의 interaction

V5b-F mechanism이 *boundary lifting*. Multi-formation σ에서 K-field의 *inter-formation boundary*도 비슷한 partial Goldstone? K=2 inter-formation gap 영역이 V5b-F의 free BC boundary와 mathematical analog?

만약 yes → V5b-F characterization (G1)이 multi-formation σ (G3) MO-1 face에 **method 제공**. 이것이 *unexpected synergy*.

Day 1 evening 분석 시 *V5b-F mechanism 이 multi-formation에 어떻게 generalize 되는지 sketch* 시도 가능.

### 3.3 G0 + G1이 모두 W5 Day 1에서 substantive complete가 *너무 야심찬가?*

**Skeptic check**: 
- G0 takes ~7h (plan estimate). 12h day의 60%.
- G1 takes ~5h (plan estimate). 12h day의 40%.
- 합 ~12h, fits.

But cross-cutting overhead (transitions, breaks, decision points) ~1-2h 추가. Total 13-14h. Marginal.

**Risk**: Day 1 evening 23:00까지 work 가능성. Day 2 morning fatigue.

**Mitigation**: Day 1 hard cutoff 22:30. G2 setup이 22:00-22:30 narrow → 사실 23:00까지 갈 수도. Sleep loss avoidance.

---

## §4. Conjectures Spawned During Brainstorm

Day 1 brainstorm 동안 떠오른 *new conjectures*:

### CJ1 (W5 spawn): G0 Lemma 1의 functoriality

Lemma 1 statement이 *graph automorphism action invariance*에 의존. 이는 *category-theoretic functoriality* 시사. SCC 자체가 *graph-functor*인가?

즉 graph homomorphism $f: G \to G'$이 induce $f_*: \mathrm{Form}(G) \to \mathrm{Form}(G')$ formation map? σ-framework의 *naturality*?

**개념적 implication**: σ-framework가 *graph categorically* well-defined. W6+ research candidate (NQ-191).

### CJ2 (W5 spawn): V5b-F mechanism의 universal lifting formula

V5b-F가 H1+H2 mixed일 가능성 (§2 brainstorm)이 시사: boundary lifting이 *generic* mechanism — 모든 non-translation-invariant graphs에 universal.

**Conjecture**: $\lambda_{Goldstone}^{partial}(G) = \lambda_{Goldstone}^{bulk}(G) + \delta\lambda_{boundary}(G)$ where $\delta\lambda_{boundary}$ scales with *boundary surface area / volume ratio*.

W6 NQ candidate (NQ-192).

### CJ3 (W5 spawn): Lemma 3 generalization to higher ℓ

Lemma 3는 $\ell=1$ Goldstone-saturation. 확장 가능?
- $\ell=2$ orbital이 *quadrupole tensor*와 saturate?
- $\ell=k$ orbital이 *rank-k spherical tensor*와 saturate?

W4-04-23 R23 ℓ↔irrep table (NQ-146 Cat A)와 결합하면 σ-framework의 *full angular structure* derivation 가능.

W6+ NQ candidate (NQ-193).

### CJ4 (W5 spawn): Multi-formation σ → V5b의 Goldstone proliferation

K=2 well-separated minimizer에서 각 formation이 자체 translation Goldstone → 4-fold Goldstone (2 formations × 2D translation). K=3 → 6-fold. K-fold formations → 2K-fold Goldstone (in 2D).

**Conjecture**: Multi-formation V5b-T가 *2dK-fold Goldstone with K-formation commensurability splitting* (d=lattice dim).

W6+ research direction (NQ-194).

---

## §5. Memory / Context Refresh from W4

Day 1 morning 빠르게 reload할 W4 핵심 facts:

### 5.1 σ-framework definition (Commitment 14, 04-25)

$$\sigma(u^*) = \big(\mathcal{F}(u^*); \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^{K}\big)$$

- $\mathcal{F}$ = local-maxima count (threshold-independent)
- $n_k$ = $k$-th Hessian eigenvector's nodal-domain count (Courant)
- $[\rho_k]$ = irrep label under $G_u = \mathrm{Stab}_G(u^*)$
- $\lambda_k$ = $k$-th Hessian eigenvalue
- Cutoff $K$ = spectral-gap multiple $c=10$ (provisional)

### 5.2 V5b-T statement (T-V5b-T canonical 04-26 extended)

Translation-invariant graphs (torus T^d, cycle C_n):
- Sub-lattice ($\zeta < \zeta_*(G)$): orbital only, no Goldstone
- Super-lattice ($\zeta > \zeta_*(G)$): d-fold pseudo-Goldstone, possibly split by commensurability
- 2D torus: 2-fold doublet split
- 1D cycle: 1-fold single Goldstone
- $\zeta_*(2D \text{ torus}) \in [0.2, 0.5]$, $\zeta_*(1D \text{ cycle}) < 0.2$
- Goldstone nodal=2 universal

### 5.3 V5b-F new finding (04-26 extended, Cat C)

Free BC graphs:
- ζ=0.5: max overlap = 0.83 (intermediate)
- ζ=1.0: max overlap = 0.75 (intermediate)
- Mechanism: bulk approximate translation Goldstone + boundary lifting
- Cat C, NQ-173 quantification carry

### 5.4 NQ-172 mode-indexing lesson

NQ-170 hardcoded `mode_overlaps[1]` → 04-26 NQ-170 reproducibility crisis. NQ-172 resolution: mode-agnostic detection.

**Day 1 G1 implication**: V5b-F script도 mode-agnostic으로 작성 — `mode_overlaps[1]` hardcode 금지.

### 5.5 W4 V5b 8 iterations

V1 → V2 → V3 → V4 → V5a → V5b → V5b' → V5b'' (W4-04-24 to 04-26).

W5 inherits this iterative refinement model.

---

## §6. Day 1 후 W6+에 미치는 영향 (forward thinking)

### 6.1 G0 successful → W6 paper 1 outline 가능

If Day 1 G0 fully merged → Day 7 (W5 close) v1.5 release ready → W6 P1 *Paper 1 Foundational §1-§3 first draft*.

이는 *publication horizon*의 *first concrete step*. SCC project 시작 7개월 만에 첫 paper 작성 시도.

### 6.2 G1 H1 supported → V5b-F → V5b family completion

If Day 1 G1 H1 supported → V5b-F Cat C → Cat B path. W5 Day 5+ G4 (V5b 3D) + G2 (ζ_*) 합쳐 *V5b family complete spectrum*.

이는 *Paper 2 (V5b Family) outline ready*. W7 first draft 시작 가능.

### 6.3 G1 H1 reject → V5b-F Cat C 유지 → W6 deeper 작업

If Day 1 H1 reject → V5b-F mechanism unclear → W6에 *deeper analysis*. 그러나 V5b family completion은 *2D + 3D + 1D translation-invariant only* (V5b-F omitted) 가능 — Paper 2 가능.

### 6.4 G0 partial (Option β) → W5 Day 2 morning continuation

If Option β chosen (1 combined entry) → W6+에 *granular separation 재고려*. Paper 1 §4에서는 5 statements를 *paper의 sub-subsections*로 표현 가능.

### 6.5 Day 1 cumulative time > 14h → Day 2 fatigue

If Day 1 23:00까지 work → Day 2 morning fatigue → Day 2 G2 numerical 정확도 저하. Mitigation: 22:30 hard cutoff 준수. G2 setup이 *완벽하지 않아도 OK*.

---

## §7. Free-Form "What If" Scenarios

### What if 1: G0 user decision = Option γ (hybrid)?

Plan default Option α. But user picks γ (Lemmas combined, Theorems separate)?

Then:
- Lemma 1 + 2 + 3 → *single combined entry* T-σ-Lemmas-1-3
- Theorem 3 + 4 → *2 separate entries* T-σ-Theorem-3, T-σ-Theorem-4
- Total: 38 + 1 + 2 = 41A (vs 43A in Option α, vs 39A in Option β)

Counts update revised: 38→41, 52→55, 73%→74.5%→75%. Not too different.

### What if 2: G1 numerical takes 30+ min (NOT 15min)?

Plan estimates 15min for 10 minimizers. But L=20 with multi-IC × 5 seeds × 2 ζ values = 30 minimizer attempts. Each attempt = 1-2s minimizer + 5s Hessian × 6 modes = ~10s.

30 attempts × 10s = 300s = 5min. Plan accurate.

But numerical could hang if `find_formation` non-converged loops → up to several minutes. Mitigation: max_iter=15000 already set.

### What if 3: H1 supported but bulk overlap = 0.85 (not > 0.95)?

Then *partial H1*. V5b-F mechanism = "mostly bulk-localized, some boundary lifting". Cat C → Cat C/B boundary.

Decision: Cat B with caveat (partial bulk-local, ratio quantified).

### What if 4: User rejects Option α at 09:30, asks for Option β?

Then Day 1 schedule shifts: *only 1 §13 entry* (T-σ-Supporting). 1 hour saved on canonical edits.

**Use saved time on**: G3 multi-formation σ definition draft start (Day 3-4 작업)? Or G1 ζ=0.5 추가 numerical?

**Recommendation**: G1 추가 numerical (V5b-F characterization 더 깊이).

### What if 5: Completely unexpected — V5b-T canonical entry에 bug 발견?

W4-04-26 V5b-T entry (line 1117 in canonical.md)에 statement error 발견 가능성. (예: ζ_* bracket이 잘못된 값, nodal count statement 잘못됨)

Day 1 morning에 발견 시: *immediate fix* (entry edit) + W5 weekly_draft에 erratum 등록.

Probability: <5%. But monitoring during 14:00-15:00 canonical edits 시 alert.

---

## §8. Day 1 Mental Frame

### 8.1 Marathon mode

W4 Day 1 (04-19 reframing day) was *infrastructure-only*. W5 Day 1 is *substantive aggressive*. Different mental load.

W4 04-24 Day was "all substantive 4 arcs" — *most similar precedent*. 14h work day + 28 daily files.

W5 Day 1 expected ~12h + 8 daily files. *Lighter than W4-04-24 마라톤*.

### 8.2 Verification > discovery 정신 유지

G0 = *verification* (W4 statements를 §13으로 이동). G1 = *characterization* (W4 V5b-F finding의 mechanism quantification). 

**둘 다 verification**, not discovery. W5 Day 1은 *마라톤이지만 risk가 낮은 마라톤*.

진짜 discovery moments (G3 multi-formation σ, G1 V5b-F mechanism)는 Day 2-4. Day 1은 *마라톤 launch*.

### 8.3 Decision fatigue mitigation

Day 1에 5 user decisions (or proxy decisions):
- 09:30 G0 Option α/β/γ
- 12:30 Lemma 2 (iii) Cat A vs Cat C
- 16:00 Counts update consistency check
- 19:30 H1/H2/H3 verdict
- 22:00 G2 setup 진행 vs Day 2 morning carry

**Mitigation**: Pre-decided defaults (in plan §7 contingency). Day 1 morning에 미리 commit.

### 8.4 Boundary cases — 가장 신경 쓸 부분

- canonical.md line numbering이 다음 entry 추가 시 shift. *Specific line references in plan may be outdated*. Use grep for line locations.
- G1 mode-agnostic detection 누락 가능성 — V5b-F script가 NQ-172 lesson (no `mode_overlaps[1]` hardcode) 따르도록 explicit check.

---

## §9. Day 1 후 Sleep Plan

22:30 hard cutoff. 23:00-23:30 wind-down (no canonical edits, only journal review). 24:00 sleep target.

Day 2 06:00-07:00 wake. Day 2 morning ~3h prep before 09:00 G2 numerical run.

Day 1 후 Day 2 07:30-09:00에 *fresh review of Day 1 results*. 잘못된 verdict 가능성 catch.

---

## §10. 마지막 sanity check

Day 1 plan을 *간단히 한 문장으로*:

> **G0 (σ supporting lemmas Day 1 fully merged with proofs) + G1 (V5b-F H1/H2/H3 verdict Day 1 EOD) + G2 (NQ-174 script ready Day 1 EOD).**

이 한 문장이 명확하면 plan은 deliverable. *Yes*.

W4의 8-iteration journey가 W5의 *집중적 verification*으로 transition. Day 1이 *그 transition의 첫 표현*.

---

## §11. 미래의 나에게 메모 (Day 1 morning self)

내가 09:00에 이 brainstorm을 다시 읽을 때 기억할 것:

1. **§1.1, §1.2, §1.3** 의 wording corrections를 즉시 plan §3에 반영. Lemma 1 "finite graph", Lemma 2 (iii) "sign-definite", Lemma 2 (iv) "non-invariant only".

2. **§2.3** 에서 H1+H2 mixed가 most likely라는 점. Day 1 evening 분석 시 명시적 mixed verdict 가능성 열어둘 것.

3. **§3.2** V5b-F → multi-formation synergy. Day 1 evening에 sketch 시도.

4. **CJ1-CJ4** 4 conjectures 새 NQ로 등록. Day 1 99_summary §6에 명시.

5. **§7 What if** — Plan을 *literal하게* 따르기보다 reality에 adapt. Plan은 *guidance*, not *script*.

6. **§8.3** Decision fatigue mitigation — pre-commit to defaults.

7. **§8.4** Mode-agnostic 누락 알림 — V5b-F script writing 시 explicit check.

8. **22:30 hard cutoff**.

---

**End of pre_brainstorm.md.**
**Tone: free-form, more questions than answers, anticipatory anxiety + excitement.**
**Use: Day 1 morning 09:00 fast review 후 plan §3 Block 1 시작.**
