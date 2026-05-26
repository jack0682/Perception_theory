> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q3_stochastic_dynamics]] · [[pf_tstar_langevin]] · [[pf_a1_lions_sznitman_freidlin_route]]

# broad_survey_B1.md — OP-0021 $T_*$ Registration: Mori-Zwanzig Route A + pf_tstar_langevin 5-Gap Survey

**Type**: W8-Day1 Track B LIGHTER. *Survey + gap identification only* — **no proof attempts**. W9 staging input.
**Date**: 2026-05-18 (W8-Day1, Mon).
**Author**: Claude session, sole producer.
**Canonical refs**: `canonical.md §16 D-ST-4` (Kramers rate / partition function), `§13 T-PF-A1-{AR,SDE,GI,PE} Cat A` (Package I), `theorem_status.md` OP-0021 row.
**Working refs**: `pf_tstar_langevin.md §11 NOP-F + NOP-J + §1b F_0/F_M` (T_* working formalization), `pf_a1_lions_sznitman_freidlin_route.md` (route memo), `CV114_H_MORSE_PACKAGEII/07_Eyring_Kramers_requirements.md`, `CV114_H_MORSE_PACKAGEII/08_candidate_lemma_chain.md`, `n1_kramers_extension.md`.
**Pre-work xref check**: 20+ working file hit; ancestors above. 본 file 의 *novel positioning* = *Mori-Zwanzig Route A literature pointer* + *pf_tstar_langevin §11 의 light gap 5개 정식 표 등록* (W9 sketch 의 직접 입력).

---

## §1. Mission

> **OP-0021 ($T_*$ registration) 의 Mori-Zwanzig Route A 문헌 + `pf_tstar_langevin.md` 의 *light* 5 gap 식별 — W9 의 `op0021_mori_zwanzig_sketch.md` 의 직접 입력**. *증명 시도 없음*. *survey 만*.

W8 strategic plan §11 W9+ Preview 의 Path 1/2/3 공통 항목: "OP-0021 T_* registration 본격 (Mori-Zwanzig Route A or RG Route B; W8 Day 1 Agent B1 survey 가 입력)". 본 file 이 그 *입력*.

---

## §2. 현재 OP-0021 상태 (theorem_status.md 인용)

> **OP-0021** Stochastic Dynamics — Low priority — UNDER INVESTIGATION (exp54–exp59 Kramers rate theory). Dual-naming with `hypothesis_tree.md` $T_*$ row (carried forward to CV-1.17+ per CV-1.16 SEAL §"Pre-existing inconsistency").

`pf_tstar_langevin.md §3` 의 P-F-A1 axiom 후보:
- **Package I (CV-1.8, fully Cat A CV-1.9)**: T-PF-A1-AR + T-PF-A1-SDE + T-PF-A1-GI + T-PF-A1-PE → *for any* $T_* > 0$ 의 well-posedness + Gibbs invariance + Poincaré ergodicity.
- **Package II (W9+)**: Eyring-Kramers Cat B → Cat A, H5 + T_* registration 필요.

**Open**: $T_*$ 자체의 *origin* (어디서 오는 노이즈인가?) — 8 candidate interpretations (§11.1 of pf_tstar_langevin.md).

---

## §3. Mori-Zwanzig Route A (literature pointer, *survey only*)

### §3.1 Mori-Zwanzig formalism — core idea

거시 변수 (slow modes, e.g., K_act, σ-tuples) 의 동역학을 *projection operator* 로 분리:

$$\partial_t A_\mathrm{slow}(t) = \underbrace{i \Omega A_\mathrm{slow}}_{\text{drift}} + \underbrace{\int_0^t K(t - s)\, A_\mathrm{slow}(s)\, ds}_{\text{memory}} + \underbrace{F(t)}_{\text{fluctuation}}$$

with *Mori-Zwanzig identity*: $F(t)$ = projected fluctuation, $K$ = memory kernel, *fluctuation-dissipation* relation links $K$ and $\langle F(t) F(s) \rangle$.

### §3.2 SCC 적용 시 핵심 질문

- **Slow variable 선택**: $K_\mathrm{act}$? σ-tuple? cumulative cross-formation overlap?
- **Fast variable**: per-site $u_t(x)$ 의 short-time fluctuation 가 슈드-thermal noise 의 source 인가?
- **Memory kernel decay**: $K(t)$ exponential ↔ Markovian (Langevin reduction OK); long-tail ↔ non-Markovian (Eyring-Kramers 변형 필요).

### §3.3 외부 reference (필요 시 W9 작업의 도구)

| Reference | 적용 영역 |
|---|---|
| Zwanzig, *Nonequilibrium Statistical Mechanics* (2001), Ch. 8 | Mori-Zwanzig identity derivation 표준 |
| Givon, Kupferman, Stuart, *Extracting macroscopic dynamics: model problems and algorithms*, Nonlinearity 17 (2004) | 수치 효과 + Mori-Zwanzig 의 numerical realization |
| Chorin, Hald, Kupferman, *Optimal prediction with memory*, Physica D 166 (2002) | Memory kernel 의 *optimal projection* |
| Lin, Lu, *Computing committor functions for the study of rare events*, Comm. Math. Sci. 2017 | Committor + projection → barrier identification (Q3-DYN 의 입력) |

### §3.4 Route A 의 *성공 조건*

- (i) SCC 의 slow variable 의 *명시적 후보* 선택 (e.g., $K_\mathrm{act}$ 의 *coarse-grained* projection).
- (ii) Mori-Zwanzig projection 의 *finite-dimensional reduction* 가 SCC 의 finite-graph setting 에서 well-defined (Givon et al. 의 standard recipe 적용 가능).
- (iii) Memory kernel 의 *exponential decay* 가능성 — high-frequency $u_t$ fluctuation 의 *spectral gap* 으로부터 유도 (H-MORSE row Cat A 활용? — OP-HMORSE-LOCAL-A 의 Day 4 SEAL prep 후 가능).

### §3.5 Route A 실패 모드

- *Slow/fast 분리 부재*: SCC 의 $u_t$ 의 다양한 모드 가 *intermediate timescale* 에 *지속적 분포* — projection 의 *cut-off* 임의성.
- *Memory long-tail*: $K(t) \sim t^{-\alpha}$ 가 SCC 의 *vineyard* 또는 *persistence-skeleton* structure 에 의해 강제 — Markovian 환원 실패.
- *Reflection boundary*: $\mathcal{F}_M$ 의 boundary 에서 Mori-Zwanzig 의 *unbounded slow variable* 가정 위배 (pf_tstar_langevin §1b 의 F_0 vs F_M 문제 의 잔향).

→ **본 broad survey 는 §3.4-3.5 만 기록**; *증명/도출 시도 부재*. W9 의 `op0021_mori_zwanzig_sketch.md` 에서 explicit attempt.

---

## §4. `pf_tstar_langevin.md` 의 *light* 5 gap 식별

`pf_tstar_langevin.md` 의 §11 NOP-F (T_* emergence Lemma 20 candidate) + NOP-J (Information geometry Lemma 24 candidate) 영역에서, *W9 effort 1-2 sessions 안에 처리 가능* 한 light gap 5개:

### §4.1 **Gap-1**: NOP-F Lemma 20 의 *coupling structure* 명시

`pf_tstar_langevin.md §11.3`:

> $T_*$ 가 *primary* 가 아니라 *emergent* — combined Fisher metric + RG flow 가 effective $T_*$ 를 *produce* 한다는 Lemma 20 candidate.

**Gap**: Fisher metric + RG flow 의 *coupling* 구조 (어느 scale 에서 RG, 어느 metric 으로 Fisher) 가 informal level. **W9 task**: explicit *2-line coupling* formula 작성 (e.g., $T_*(\ell) = T_0 \cdot \exp(\int_0^\ell \beta_\mathrm{RG}(\ell') d\ell')$ 같은 form).

**External tool**: Cardy, *Scaling and Renormalization in Statistical Physics* (1996), §5.4 (RG flow 와 effective temperature).

**Effort estimate**: 1 session sketch + 1 session Cat C 형식.

### §4.2 **Gap-2**: NOP-J Information geometry Lemma 24 의 *finite-dim Fisher* 명시

`pf_tstar_langevin.md §11.4`:

> $\mathcal{F}_M$ 위의 Fisher 정보 metric — Lemma 24 candidate.

**Gap**: Fisher metric 의 *finite-graph* 표현 (continuous Fisher metric $g_{ij}(\theta) = \mathbb{E}[\partial_i \log p \cdot \partial_j \log p]$ 의 discrete analogue 가 graph Laplacian 과 *어떻게 관계*).

**External tool**: Amari, *Information Geometry and Its Applications* (2016), Ch. 2 (discrete Fisher).

**Effort estimate**: 1 session (formal definition + 1 example on $T^2_5$ toy).

### §4.3 **Gap-3**: $T_*$ candidate 2c (phenomenological inverse commitment) 의 *vanishing limit*

`pf_tstar_langevin.md §2c`:

> $T_* \propto 1/\beta_\mathrm{commit}$ 의 phenomenological 후보 — $\beta_\mathrm{commit} \to \infty$ (strong commitment) 시 $T_* \to 0$ (zero-noise limit).

**Gap**: zero-noise limit 의 *Freidlin-Wentzell large-deviation* 결과 와의 *호환성* (현재 정성적 진술).

**External tool**: Freidlin-Wentzell, *Random Perturbations of Dynamical Systems* (3rd ed., 2012), Ch. 4.

**Effort estimate**: 0.5 session (citation + 1-paragraph compatibility statement).

### §4.4 **Gap-4**: F_M vs F_0 의 reflection boundary 의 *T_* sensitivity*

`pf_tstar_langevin.md §1b`:

> $\mathcal{F}_M$ 의 boundary 에서 reflection 이 *projection step* 으로 implement (`optimizer.py:find_formation`).

**Gap**: reflection 의 *noise amplitude scaling* 가 $T_*$ 추정에 *어떻게 들어가는지* 미명시. Naive iid Gaussian noise + projection 의 *effective T* 가 $T_\mathrm{raw}$ 와 차이날 수 있음 (boundary correction).

**External tool**: Lions-Sznitman 의 *Stochastic differential equations with reflecting boundary conditions* (CPAM 1984, T-PF-A1-SDE 의 출처) — *boundary correction formula*.

**Effort estimate**: 1 session (단일 site Brownian motion on $[0, 1]$ 의 effective $T_*$ vs $T_\mathrm{raw}$ 명시 + 일반화 sketch).

### §4.5 **Gap-5**: Package II Eyring-Kramers prefactor 의 *T_* dependency* 분해

`canonical.md §13 T-PF-A1-PE` 의 spectral gap explicit form:

$$\lambda_1(\pi_{T_*}) \geq \frac{\pi^2}{n} \exp\!\left(-\frac{\mathrm{osc}(\tilde E)}{T_*}\right)$$

→ Eyring-Kramers prefactor $A_\mathrm{EK}$ 가 *어떤 식으로 $T_*$ 에 polynomial* (Reed-Simon volume) vs *어떤 식으로 exponential* (gap suppression) 인지 분리.

**Gap**: prefactor $A_\mathrm{EK}$ 의 *closed form* 미명시 (CV114_H_MORSE_PACKAGEII/07,08 에서 *후보* 식 보유; *T_* dependency* 의 *명시적 separation* 부재).

**External tool**: Bovier-Eckhoff-Gayrard-Klein, *Metastability in reversible diffusion processes I/II* (J. Eur. Math. Soc. 2004), prefactor formula.

**Effort estimate**: 2 sessions (Bovier et al. citation + SCC 의 saddle 의 Hessian 의 *T_* free* part 분리).

---

## §5. 5 gap 의 *unlock chain*

| Gap | Unlocks | Effort |
|---|---|---|
| Gap-1 (Lemma 20 RG-Fisher coupling) | NOP-F Cat C ready | 2 sessions |
| Gap-2 (Lemma 24 finite-Fisher) | NOP-J Cat C ready | 1 session |
| Gap-3 (zero-noise compatibility) | Candidate 2c 의 *narrow Cat C* | 0.5 session |
| Gap-4 (reflection $T_*$ correction) | Numerical $T_*$ estimation (exp54-59) 의 *correction factor* | 1 session |
| Gap-5 (Eyring-Kramers prefactor separation) | Package II Cat B → Cat A 의 *partial* (prefactor 만) | 2 sessions |

총 effort: **~6.5 sessions** (W9 의 약 1.5 주). Gap-3 + Gap-4 가 가장 가벼움 (W9 Day 1-2 후보).

---

## §6. 기존 working 과의 관계

본 broad_survey_B1 = `pf_tstar_langevin.md §11` 의 *light gap 5개* + `CV114_H_MORSE_PACKAGEII/07,08` 의 *effort estimate 첨가*. *재정리 아님* — *W9 staging 의 단위 분해*.

- **Silent resolution 회피**: OP-0021 *전체* 미해결 유지. 5 gap 모두 *Cat C ready* 만; *Cat B 승급 주장 없음*.
- **dual-naming inconsistency**: `theorem_status.md` line 587 OP-0021 (Stochastic Dynamics) vs `hypothesis_tree.md` HT-3.7 의 $T_*$ row — CV-1.17+ reconciliation deferred; 본 broad survey 는 *현재 dual-naming 상태 그대로* 인용.

---

## §7. Hard constraint verification

- [x] canonical 직접 수정 0
- [x] silent OP resolution 0 — OP-0021 OPEN 유지, 5 gap *Cat C ready* 만
- [x] Research OS 재도입 0
- [x] reductive 환원 0 — Mori-Zwanzig / Fisher metric / Freidlin-Wentzell 모두 *contrastive* tool
- [x] primitive 전도 0
- [x] 4 에너지 항 병합 0
- [x] K 이중 취급 0
- [x] zero-temp metastability flag — §4.3 zero-noise limit 명시 (Freidlin-Wentzell 별도)
- [x] OMC 풀 오케스트레이션 0

---

## §8. Status

**Type**: working broad survey LIGHTER, P1 baseline.
**Effort to-date**: 1 session (본 W8 Day 1 Track B1).
**Next session**: W9 `op0021_mori_zwanzig_sketch.md` (Gap-1 + Gap-2 attack), W9 `op0021_tstar_emergence.md` (Gap-3 + Gap-4 attack).
**Promotion path**: W9 EOD 의 *Cat C* register → W10+ 의 *Cat B* promotion.

---

*broad_survey_B1.md 종료. OP-0021 W9 staging input — 5 light gap 식별 완료. canonical 0 edits. 증명 시도 0.*
