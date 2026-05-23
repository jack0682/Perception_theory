---
type: working/foundation
status: draft Cat C SKETCH (consolidation reference)
date: 2026-05-19 (evening, post-unified-derivation EOD)
session_label: SCC U-excluded + Problematic Consolidation
predecessor:
  - 2026-05-19 SCC_unified_derivation_v0.1.md (4633 lines, 18 sections, ~278 derived definitions)
  - 2026-05-19 W8-Day2 EOD (T_*/H5 deep work)
  - 2026-05-19 conversation chain (4-class taxonomy → root extraction → MG → L3 → unified derivation)
canonical_version: CV-1.17 (sealed 2026-05-15, untouched)
prompt_body: THEORY/logs/daily/MAIN_PROMPT_v3.md
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[SCC_unified_derivation_v0.1|Unified Derivation v0.1]] · [[../../canonical/auxiliary_structures_master|AUX-1.5 (U-residue source)]] · [[../../canonical/theorem_status|theorem registry]] · [[../../canonical/hypothesis_tree|HT-3.8]] · [[../../logs/daily/2026-05-19/02_H5_morse_spinodal|02_H5]] · [[../../logs/daily/2026-05-19/03_T_star_fixed_point|03_T_star]]

# SCC U-Excluded + Problematic Items — Consolidation v0.1

**Mission**: 2026-05-19 unified derivation 의 *모든 U-excluded* (axiomatic-free / canonical 외부 잔류 항목) + *모든 problematic* (조건부, Cat C SKETCH, OPEN, conditional regime, sketch level, lacunae, proved failure) 의 *분리된 consolidation*. 사용자 instruction: *"문제된 부분과 U로 제외된 부분들은 이제따로 모아서 정리 U제외는 가장 상단에"*.

**Organization principle**:
- **§A U-excluded** (가장 상단) — *intentionally outside* the formal SCC mathematical content (axiomatic-free, observer-personal, canonical 외부 commitment).
- **§B Problematic** — *within* the derivation but with caveats (Cat C SKETCH, conditional regimes, OPEN OPs, lacunae, sketch-level proofs, proved failures).

**Status**: Cat C SKETCH consolidation reference (not canonical, not promotion candidate).

---

# §A. U-Excluded Items — *축출된, 의도적으로 형식화 외부*

본 §A 는 *AUX-1.5 의 U-residue classification* 의 직접 carry-forward + 본 unified derivation 의 *intentional exclusions* 모음. *각 항목은 canonical 의 mathematical content 외부* 에 위치 — *axiomatic-free*, *observer-personal*, 또는 *Class 4 idio (seed-derived)*.

## §A.1 — T_* (Effective Stochastic Temperature)

**Status**: U-residue (AUX-1.5 §4.9.1 + L1057). OP-0021 OPEN.

**Position**: *Observer-personal axiomatic free parameter* (Route C, P classification under OMS-1 ξ resident).

**왜 U-excluded**:
- *Fixed-point 구조*: $T_*$ → π_{T_*} → variance → $T_*$ (자기-참조 순환)
- *Brouwer existence*: 03_T_star §2 Cat A 후보 sketch (3-lemma chain)
- *Multiplicity*: multi-well $\mathcal{E}$ → multiple fixed-points possible (OPEN, 03_T_star §1.3)
- *Cugliandolo effective T review* (pre_brainstorm §5.2): *모든* notion (FDT/kinetic/granular/active matter) → 환경 statistics 요구 → **CN-COB 위반**
- ∴ Route A (Mori-Zwanzig) + Route B (RG fixed point) **폐기 *제안*** (03_T_star §5.2)
- ∴ Route C (observer-personal free) = COB-통과 유일 path

**Mathematical form**:
$$T_* \in B_{T_*}^{\mathrm{FP}}(\Theta) \cap B_\xi^{\mathrm{OMS-1}}, \quad T_* = \mathrm{argmin}_{T \in \mathcal{B}_{T_*}^{\mathrm{FP}}} \rho_{\mathrm{JND}}(\Theta, T)$$

- Brouwer guarantees non-empty $B_{T_*}^{\mathrm{FP}}$
- 관찰자가 *선택* — Weber-Fechner JND criterion (G1+G3 hybrid)

**위치 in unified derivation**: §6.4 Gibbs π_{T_*} + §6.7 dynamics + §14.2 OP-0021 reference. 본 framework 에서 *axiomatic input* — derived NOT.

**Operational consequence**:
- *L3 hyperparam 의 $\tau = T_*/\alpha$ 가 user-controlled* (theoretical study) OR seed-decoded (observer simulation)
- 모든 stochastic regime 의 *기본 입력*

**Forward hook**: OP-T*-FIXED-POINT draft (03_T_star §4) + OMS-1 ξ catalog amendment 권장 (W10+ 후속 결정).

---

## §A.2 — H5 Spinodal Goldstone Mode Degeneracy

**Status**: U-residue (AUX-1.5 §4.9.5 + L1058). OP-H5-MORSE-SPINODAL OPEN (오늘 02_H5 draft).

**Position**: *Intrinsic codim-1 stratum* — *not* axiomatic-free; *mathematical event* 자체가 *intrinsic degeneracy*.

**왜 U-excluded**:
- Generic regime: Morse via Sard transversality → Cat A 후보 (02_H5 §2 P1 Sard sketch)
- Spinodal critical surface: $\Sigma_{T8} = \Sigma_{\mathrm{Hess}}$ (canonical SB7 Cat A, L2495)
- *Intrinsically zero Hessian eigenvalue* on $\Sigma_{T8}$ — *Goldstone mode* (symmetry-breaking 의 자연 후속)
- 본 degeneracy 가 *formation 을 트리거* (perception 의 발생 순간 자체)
- ∴ generic *Morse stability 가정 (H5)* 가 *codim-1 stratum 에서 fails by design* — *intrinsic*, *not derivable*

**Mathematical form**:
- *Outside* $\Sigma_{T8}$ (post-bifurcation $\mathcal{R}_{\mathrm{post}} \cap \mathcal{B}_{\mathrm{stable}}$): Morse Cat A 후보 (Zariski-open dense)
- *On* $\Sigma_{T8}$ (codim-1 stratum): Hessian Goldstone zero (canonical V5b-T-zero Cat A definitional, L1328)

**위치 in unified derivation**: §3.5 ($\Sigma_{T8} = \Sigma_{\mathrm{Hess}}$, SB7 anchor) + §4 Stage 2 의 (H5) 가정 + §13 axiom verification + §14.1 OP-H5-MORSE-SPINODAL reference.

**Proposed (H5') regime restriction** (02_H5 §5.2):
> Replace canonical T-P-F-ε0-K (H5) with $(\mathrm{H5'})$ Morse stability *on $\mathcal{R}_{\mathrm{post}} \cap \mathcal{B}_{\mathrm{stable}}$ regime only* — *spinodal stratum separate treatment*.

**Operational consequence**: *Eyring-Kramers Package II Cat B* 진입의 *prerequisite identification* — (H5') + Route C T_* 결합 (02_H5 §5.3 + 03_T_star §5.3).

**Forward hook**: OP-H5-MORSE-SPINODAL draft (02_H5 §4) + 3 sub-OPs (α/β/γ) — OP-H5-α (Hironaka detail W9+), OP-H5-β (Aut(G) trivial fallback), OP-H5-γ ((SN-iii)(SN-iv) genericity + OP-OMS-033b).

---

## §A.3 — Class 4 Idio Entries (Seed-Derived, Axiomatic Free)

**Status**: *Axiomatic free under OMS-1 ξ resident* (CN-COB unique path). Decode from 256-bit seed $s$.

**Position**: *Not derivable from foundation* — *axiomatic input* (observer's cognitive style identity).

**왜 U-excluded**:
- Class 1-3 (구조적 + 해부학적 + 지각적) = *measurable individual values*
- Class 4 = *irreducibly individual cognitive style* — *전수 정의 불가능* (사용자 instruction: "개인의 특성을 정의하는것과 같기땜문에 사실 불가능함")
- 사용자 *pragmatic bypass*: 256-bit SHA256 seed 가 *operational compression* (2²⁵⁶ ≈ 10⁷⁷ distinct observers)
- *Ontological question 의 *bypass*, NOT *resolution***: True Class 4 residue 가 *empty* 인지 *non-empty* 인지 결정 부재 (epistemic frontier)

**Decoded entries (~10)**:

| Idio entry | Range | Decode distribution | Role in SCC |
|---|---|---|---|
| $r_1 = \lambda_{\mathrm{cl}}/\lambda_{\mathrm{bd}}$ | $\mathbb{R}_+$ | log-uniform | Closure-vs-boundary balance |
| $r_2 = \lambda_{\mathrm{sep}}/\lambda_{\mathrm{bd}}$ | $\mathbb{R}_+$ | log-uniform | Separation-vs-boundary balance |
| $r_3 = \beta/\alpha$ | $\mathbb{R}_+$ | log-uniform | T8 phase ratio |
| $a_{\mathrm{cl}}$ | $(0,4)$ | uniform | Closure parameter |
| $\tau = T_*/\alpha$ | $\mathbb{R}_{\geq 0}$ | log-uniform | Noise level (→ §A.1 T_*) |
| $r_{\mathrm{Gestalt}}$ | $[0,1]$ | beta(2,2) | Closure-vs-separation cognitive bias |
| $p_{\mathrm{FG}}$ | $[0,1]$ | beta(1,1) | Figure-ground basin selection prior |
| $m_{\mathrm{attn}}$ | $\Delta^{K-1}$ | Dirichlet uniform | Attention strategy distribution |
| $c_{\mathrm{const}}$ | $[0,1]$ | beta(2,2) | Color constancy strength |
| $g_{\mathrm{bias}}$ | small distortion | $\mathcal{N}(0, \sigma_g^2)$ | Geometric perception bias |

**위치 in unified derivation**: §1.2 (Θ_idio decoded from s) + §6 (cognitive style modulation) + Appendix C (decode catalog).

**Reduction caveat (사용자 critique)**:
- *진짜 Class 4 인가 *epistemic gap* 인가* 결정 불가능
- 시간이 흐르며 Class 2/3 정밀화 (시력 측정 + attention modulation 신경학적 mapping) 가 Class 4 entries → Class 3/2 migrate 가능성
- 본 day 의 *operational decision*: 256-bit seed 으로 *pragmatic bypass*, *ontological resolution 부재*

---

## §A.4 — Stage 0 Sensor Transformation T (Canonical 미등록 Lacuna)

**Status**: *Canonical 외부* — pre_brainstorm §5.3 의 9-조건 hypothesis package OPEN. 본 unified derivation 의 §2 가 *first operational sketch* (Full Cat C SKETCH).

**Position**: SCC 의 *입력 단계* (Stage 0) — canonical 미등록, 따라서 *전체 framework 의 가장 근본적 lacuna*.

**왜 U-excluded**:
- Stage 0 T 가 $I_t \to \tilde{I}_t$ (LMS-channel retinal signal)
- 6-부 composition (PSF + sampling + LMS + adaptive gain + spatial CSF + temporal kernel)
- 각 sub-T 가 *observer-anatomical/neural parameter dependent* (~14 entries from MG-1 + MG-4 + R-nn-1,2 등)
- canonical 9-조건 등록 시도 — *현재 OPEN* (pre_brainstorm §5.3 명시)
- 따라서 *모든 derivation 의 입력* 이 *canonical 외부 sketch level*

**Mathematical form (본 file §2 Cat C SKETCH)**:
$$T_{\mathrm{sensor}} = T_{\mathrm{temp}} \circ T_{\mathrm{CSF}} \circ T_{\mathrm{gain}} \circ T_{\mathrm{LMS}} \circ T_{\mathrm{sample}} \circ T_{\mathrm{PSF}}$$

**위치 in unified derivation**: §2 (Full Cat C SKETCH, 383 lines).

**Lacuna 영향**:
- Stage 1 ($u_0 = \pi_G(\tilde{I}_t)$) 의 *입력* 이 canonical 외부 sketch
- T_* (§A.1) 의 *information-theoretic Route C 보강* (Jaynes MaxEnt) 가 Stage 0 T 의 channel capacity 의존 — 본 lacuna 영향
- *모든* SCC simulation 의 *입력 형식* 가 *configuration-specific* (구체적 값 canonical 부재)

**Forward hook**: Stage 0 9-조건 canonical 등록 prerequisite work (W10+ priority).

---

## §A.5 — Configuration-Specific Parameters (불-uniqueness 명시 항목)

**Status**: *Configuration-specific* (prompt body §12.6 carry-forward). *Parameter uniqueness 주장 0*.

**Position**: *Operational decision per study* — *axiomatic-free in the *uniqueness* sense* (값 자체 는 fixed per simulation, 단 *canonical default 부재*).

**왜 U-excluded**:
- 25+ external parameters (~30 root entries + thresholds + decode distributions)
- canonical *각 값의 unique 선택 주장 0* (prompt body §12.6)
- *예외* (값 명시): $a_{\mathrm{cl}} \in (0, 4)$ contraction range; $c$ spinodal interior $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$; $\beta/\alpha$ critical inequality (T8); $W(u) = u^2(1-u)^2$ canonical double-well
- *예외 아닌* (값 미고정): $\rho_{\mathrm{pers}}, \tau_{\mathrm{pers}}, \theta_{\mathrm{core}}, \theta_{\mathrm{in}}, \theta_{\mathrm{supp}}$ thresholds; energy weight ratios; mass $M$; etc.

**Configuration-specific entries**:

| Parameter | Range | Default form | 위치 |
|---|---|---|---|
| $\rho_{\mathrm{pers}}, \tau_{\mathrm{pers}}$ | $[0,1] \times \mathbb{R}_+$ | eccentricity-dependent (R-an-13) | §5.2 |
| $\theta_{\mathrm{core}}, \theta_{\mathrm{in}}, \theta_{\mathrm{supp}}$ | $[0,1]^3$ | ~(0.7, 0.5, 0.05) | §5.5-5.8 |
| Mass $M$ | $(0,1)$ | per-trial structural choice | §1.1 |
| $\delta_{\mathrm{stereo}}$ (D-ST-1 bandwidth) | $\mathbb{R}_+$ | IPD + binocular fusion-derived | §12.2 |
| $T_{\min}, T_{\max}$ (T_* bounds) | $\mathbb{R}_+^2$ | study-fixed | §A.1 ref |
| FOV cardinality $\lvert V \rvert$ | $\mathbb{Z}_+$ | R-an-11 derived | §1.2 |
| K_field cap | $\mathbb{Z}_+$ | R-nn-11 (cognitive capacity) | §A.7 |
| $\Lambda_{\mathrm{coupling}}$ functional form | varies | configuration-specific | §11.4 |
| $\Psi_{\mathrm{LMS}\to \mathrm{scalar}}$ | function | achromatic vs chromatic balance | §3.8 |
| $\mathrm{Norm}_{\Sigma_M}$ method | linear vs iterative | study-fixed | §3.8 |

**위치 in unified derivation**: §1 throughout, §5.2 (eccentricity thresholds), §11.4 (Λ_coupling), §3.8 (LMS-scalar collapse).

**Forward hook**: 각 entry 별 *Cat B promotion candidate* — canonical *uniqueness 주장 부재* 의 operational decision; case-by-case canonical amendment 후보.

---

## §A.6 — K_field Architectural Cap (R-nn-11 Individual Cognitive Capacity)

**Status**: *Observer-fixed* modeling commitment (Commitment 16). *Not derivable*; observer-specific.

**Position**: *Modeling commitment* — integer-valued, *NOT* optimization variable.

**왜 U-excluded**:
- $K_{\mathrm{field}}^{\mathrm{cap}} \in \mathbb{Z}_+$ = observer's architectural cap on number of formations
- Empirical anchor: R-nn-11 $K_{\mathrm{ind}}$ (VSTM F3 / MOT F7 measurement) $\approx 3-7$ (Cowan 2001)
- *Observer-fixed* — 변경 시 다른 observer
- *NOT* derived from $u_t$ — 본 *primitive non-inversion* 의 commitment
- **Commitment 16 explicit triple separation**: $K_{\mathrm{field}}^{\mathrm{cap}}$ (modeling) ≠ $K_{\mathrm{act}}$ (dynamical count) ≠ $K_{\mathrm{soft}}$ (φ-weighted bar sum)

**위치 in unified derivation**: §10.1 + §10.5 K-triple separation table.

**Forward hook**: F3/F7 measurement-grounded K_field empirical anchor (Cat B promotion candidate, §17.1).

---

## §A.7 — CN-COB (Closed Ontological Budget) — *외부 우주 statistics 가정 부재*

**Status**: *Foundational commitment* (AUX-1.5 §7). *모든 derivation 의 prerequisite*.

**Position**: SCC 의 *근본적 ontological commitment* — *외부 우주의 statistics 가정* 차단.

**왜 U-excluded**:
- Standard 통계역학 / 통계학 의 *환경 statistics* (natural image statistics, sensor noise distributions from "real world", etc.) 가정 모두 *부재*
- $I_t$ = *관찰자-mediated raw input*, not derived from external world statistics
- ∴ Mori-Zwanzig (OP-0021 Route A) / RG fixed point (Route B) / mean-field self-consistency (Cugliandolo 2011 등) *모두 위반*
- ∴ Route C (observer-personal free P) = *유일* 통과 path (§A.1)

**위치 in unified derivation**: §1.4 + §1.6 + §13.6 + §16.5 commitment sweep.

**Operational consequence**: 모든 *외부 dataset, training data, prior distribution from environment* 도입 금지.

---

# §B. Problematic Items — *내부 derivation 의 조건부 / Cat C SKETCH / OPEN / Lacunae*

본 §B 는 *형식화 시도된* 항목 중 *완결성 부족 / 조건부 / sketch level / proved failure* 의 모음. 각 항목 별 *현재 status* + *Cat A path* + *forward hook*.

## §B.1 — Open Problems (현재 active OPEN)

### §B.1.1 OP-0005-DYN (Dynamical K-Selection, Kramers Escape Rate)

- **Status**: OPEN, W9+ staging
- **Cat target**: Cat B (Eyring-Kramers prefactor)
- **Conditional on**: H5 (Morse stability — §A.2) + OP-0021 (T_* registration — §A.1)
- **Current path (오늘 작업 부분 진척)**: 02_H5 §5 (H5' regime restriction) + 03_T_star §5 (Route C) → combined T-P-F-ε0-K Cat A path proposal (02_H5 §5.3 + 03_T_star §5.3)
- **Required work**: Eyring-Kramers prefactor canonical proof under (H5') + Route C
- **Priority**: HIGH (Q3 closure path)

### §B.1.2 OP-0008 (σ_standard MERGE/SPLIT Wigner-Projection)

- **Status**: Cat C OPEN, W9+ committed
- **Cat target**: Cat C → Cat B 승급
- **2-approach framework** (W8-Day1 broad survey B2):
  - Route (a) Kato perturbation expansion (Reed-Simon IV §XIII.5, low-coupling deterministic)
  - Route (b) RMT Wigner-Dyson level repulsion (Aut(G) trivial distributional)
- **Gate A (50% prob)**: 2-route convergence → Cat B 승급
- **Gate B (fallback ~85%)**: T-σ-Inherit 4 parts (a, b, d-direction, e) partial canonical promotion (audit-only)
- **위치**: §7.8 (T-σ-Inherit parts c, d-σ_standard Cat C) + §7.9 + §14.3
- **Priority**: HIGH (distinctive layer secure)

### §B.1.3 OP-0009 (Multi-Formation Ontological Foundations)

- **Status**: OPEN
- **Priority**: MED (long-term)
- **위치**: §11 multi-formation architecture + §14.1 OP catalog
- **Forward hook**: OMS-2.0 framework consolidation + Λ_coupling explicit form

### §B.1.4 OP-0012-SINK (Sinkhorn Temporal Composition)

- **Status**: **PROVED FAILURE** (T-SINKHORN-PLAN-SEMIGROUP-FAILS canonical warning) + scaling-gap OPEN
- **Cost-level blocker**: closed under action redefinition (CV-1.15)
- **Scaling-gap blocker**: remains OPEN
- **Alternative path**: T-CC-StableK-Kernel Cat B (CV-1.17) — kernel-composed (not plan-composed)
- **위치**: §7.4 + §7.6 + §14.1
- **Priority**: MED

### §B.1.5 OP-0021 (T_* Registration)

- **Status**: OPEN (Route C 03_T_star §5 proposed — Cat C SKETCH only)
- **Routes A/B (Mori-Zwanzig / RG)**: *폐기 제안* (COB 위반)
- **Route C (observer-personal)**: COB-통과 유일 path, OMS-1 ξ resident
- **Required work**: OMS-1 ξ catalog amendment + Brouwer existence Cat A 승급
- **위치**: §A.1 (U-excluded) + §6.4 + §14.2
- **Priority**: HIGH (Q3 closure prereq)

### §B.1.6 OP-HMORSE-LOCAL-A (L-HMORSE-LOCAL Cat B → Cat A)

- **Status**: OPEN (W7 Day 4 target)
- **Cat target**: Cat A (sharper residual via $|\sigma''(z(u^*))|$ saturation)
- **Sub-tasks**: A (analytic primary), B (numerical robustness OP-HMORSE-SBM)
- **위치**: §14.1 OP catalog
- **Priority**: HIGH (Package II Eyring-Kramers prereq)

### §B.1.7 OP-H5-MORSE-SPINODAL (NEW today)

- **Status**: OPEN, 오늘 02_H5 §4 draft
- **3 sub-OPs (a/b/c)**:
  - OP-H5-α: Hironaka algebraic strengthening (W9+ priority)
  - OP-H5-β: Equivariant Morse (Aut(G) trivial fallback)
  - OP-H5-γ: Crandall-Rabinowitz (SN-iii)(SN-iv) genericity + OP-OMS-033b unification
- **위치**: §A.2 (U-excluded) + §3.5 + §14.1
- **Priority**: HIGH

### §B.1.8 OP-T*-FIXED-POINT (NEW today)

- **Status**: OPEN, 오늘 03_T_star §4 draft
- **3 sub-OPs (α/β/γ)**:
  - OP-T*-α: Multi-well multiplicity quantification
  - OP-T*-β: Route C + Stage 0 T-channel hybrid
  - OP-T*-γ: Lawvere universality (meta-foundational)
- **위치**: §A.1 (U-excluded) + §14.1
- **Priority**: HIGH

### §B.1.9 OP-OMS-033b (Sub-OP: (SN-iii)(SN-iv) Genericity)

- **Status**: OPEN sub-OP, LOW priority
- **Cat target**: Cat B (under genericity)
- **위치**: §3.5 SN3 reference + §14.1
- **Forward hook**: Unification with OP-H5-γ

### §B.1.10 N-1 (K Conflation Prevention)

- **Status**: OPEN canonical commitment (Commitment 16 prerequisite)
- **Issue**: K 의 "counting 용 정수, 최적화 용 연속" *동시 취급* 위반 방지
- **3-quantity separation enforcement**: K_field (modeling) / K_act (dynamical) / K_soft (smooth)
- **위치**: §10.5 + §10.8

---

## §B.2 — Cat C SKETCH Items (Sketch-Level, Cat A Path Identified)

### §B.2.1 Stage 0 Sensor T (Full 6-부 Composition)

- **위치**: §2 (383L, Wave 1 A1 output)
- **Cat**: Cat C SKETCH (canonical 미등록)
- **Sketch components**: $T_{\mathrm{PSF}}$ (Zernike) + $T_{\mathrm{sample}}$ (Poisson on retinal mesh) + $T_{\mathrm{LMS}}$ (LMS channel separation) + $T_{\mathrm{gain}}$ (adaptive log-luminance) + $T_{\mathrm{CSF}}$ (spatial CSF filter) + $T_{\mathrm{temp}}$ (temporal kernel)
- **Cat A path**: canonical 9-조건 등록 (pre_brainstorm §5.3, W10+)
- **Cross-ref**: §A.4 (U-excluded canonical lacuna)

### §B.2.2 OP-H5-α — Hironaka Algebraic Strengthening

- **위치**: 02_H5 §2.3 (L3 lemma sketch level)
- **Cat**: Cat A 후보 sketch
- **Sketch**: $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \subset \mathbb{R}^4_{>0}$ codimension ≥ 1 via Hironaka resolution
- **Required work**: Full algebraic geometry proof (Tarski-Seidenberg + Hironaka 1964 detail)
- **Priority**: HIGH (H5 Cat A path completion)

### §B.2.3 OP-T*-α — Multi-Well Multiplicity Quantification

- **위치**: 03_T_star §1.3 + §6 multiplicity OPEN
- **Cat**: Cat B 후보 sketch (existence Cat A 후보 separate)
- **Sketch**: $|\mathcal{B}_{T_*}^{\mathrm{FP}}|$ as function of $\Theta \in \mathcal{R}_{\mathrm{post}}$
- **Required work**: $\beta/\alpha$ scan with explicit fixed-point counting

### §B.2.4 Brouwer L1 Quantitative TV Bound (T_*)

- **위치**: 03_T_star §2.1 L1 (qualitative continuity)
- **Cat**: Cat A 후보 sketch (quantitative refinement)
- **Sketch**: $\lVert \pi_T - \pi_{T_0} \rVert_{\mathrm{TV}} \leq C \lvert T - T_0 \rvert^\gamma$ for some explicit $C, \gamma$
- **Required work**: Holley-Stroock perturbation 의 quantitative form

### §B.2.5 T-σ-Inherit (c) σ_standard MERGE Explicit

- **위치**: §7.8 part (c) Cat C
- **Cat**: Cat C (OP-0008 target)
- **Sketch**: $\sigma_{\mathrm{merged}}$ as Wigner-projection of $(\sigma_1, \sigma_2)$
- **Required work**: 2-approach (Kato + RMT) convergence proof (W9+, see §B.1.2)

### §B.2.6 T-σ-Inherit (d-σ_standard) SPLIT Explicit

- **위치**: §7.8 part (d-σ_standard) Cat C
- **Cat**: Cat C
- **Sketch**: σ_standard decomposition formula
- **Required work**: Coupled with OP-0008 attack

### §B.2.7 $\Psi_{\mathrm{LMS}\to\mathrm{scalar}}$ Canonical Form

- **위치**: §3.8 Stage 1 initial field projection
- **Cat**: Operational (canonical 부분 정의)
- **Sketch**: $\Psi(\tilde{I}_t) = w_L \tilde{I}_t^L + w_M \tilde{I}_t^M + w_S \tilde{I}_t^S$ with weights from R-an-9
- **Required work**: Canonical achromatic vs chromatic balance fixing (Cat B promotion)

### §B.2.8 $\mathrm{Norm}_{\Sigma_M}$ Method Selection

- **위치**: §3.8 projection method
- **Cat**: Operational
- **Sketch**: Linear projection vs iterative redistribution
- **Required work**: Method 선택의 canonical form

### §B.2.9 Q_morph Morphological Descriptor

- **위치**: §5.10
- **Cat**: Cat C SKETCH (canonical 부분 정의)
- **Sketch**: $(\lvert C \rvert, |\partial C|, \chi(C), \ldots)$ per-PersComp
- **Required work**: Canonical normalization + invariant detection

---

## §B.3 — Cat B Conditional Items (Conditional Cat B Status)

### §B.3.1 T-P-F-ε0-K (Cat B Under H5)

- **위치**: canonical L1818-1833 + §4 본 file reference + 02_H5 §5
- **Status**: Cat B (conditional on H5 Morse stability — §A.2)
- **Cat A path**: (H5') regime restriction (02_H5 §5.2 proposal)
- **Combined**: (H5') + Route C T_* → Cat A path proposal (02_H5 §5.3 + 03_T_star §5.3)

### §B.3.2 T-K-Select-PF (Cat B, CV-1.10)

- **위치**: §10.7 B_K sectors + §14.1 OP-0005-EQ partially resolved
- **Status**: Cat B canonical (equilibrium K-selection under P-F-A1 Package I)
- **Cat A path**: Conditional on Q4 K-selection unified framework
- **Forward hook**: OP-0005-DYN unification

### §B.3.3 T-K-Select-OBS (Cat B, CV-1.11)

- **위치**: §10.7 + §14.1 OP-0005-OBS partially resolved
- **Status**: Cat B canonical (observed K-selection)
- **Cat A path**: Conditional on observer-extension

### §B.3.4 T-CC-StableK-Kernel (Cat B, CV-1.17)

- **위치**: §7.4 + §14.1 (T-ACT-KERNEL-COMP→REL activation)
- **Status**: Cat B canonical (kernel-composed compositional consistency under (I_{ts})+(I_{sr}))
- **Cat A path**: Conditional on Q5 temporal composition complete

### §B.3.5 T-σ-Inherit Parts (a, b, d-direction, e) Cat B

- **위치**: §7.8
- **Status**: Cat B canonical (multi-part)
- **Cat A path**: Parts (c) + (d-σ_standard) Cat C → Cat B 승급 후 전체 unified

### §B.3.6 L-HMORSE-LOCAL (Cat B, CV-1.16)

- **위치**: §14.1 OP-HMORSE-LOCAL-A target
- **Status**: Cat B unconditional under D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) active-set form
- **Cat A path**: Sharper residual bound (OP-HMORSE-LOCAL-A)

### §B.3.7 L-HMORSE-DECOMP (Cat B Conditional, CV-1.16)

- **위치**: §14.1 reference
- **Status**: Cat B conditional on $b_D = 0$ + canonical A3 (closure stabilization tendency)

### §B.3.8 T-OP6-B (Cat A Conditional Under H1-H5)

- **위치**: §5.9 + §8.13 + §12.8
- **Status**: Cat A conditional under H1-H5 (phase separation + well-formed formation + canonical $\rho_{\mathrm{bd}}$ + bounded curvature + hard-cut stereo D-ST-1)
- **Cat A absolute**: Unconditional Cat A 부재 — H1-H5 condition 명시

### §B.3.9 L-BOUNDARY-MODE-EXCLUSION (Cat C, CV-1.16)

- **위치**: §14.1 reference (sub-OP)
- **Status**: Cat C SKETCH-level (Weyl-perturbation)
- **Forward hook**: Cat C → Cat B 승급 시도 (canonical exp25 anchor)

### §B.3.10 V5b-F-empirical (Cat B Target, CV-1.5.1)

- **위치**: §11 multi-formation reference + §A.2 V5b-T-zero anchor
- **Status**: Cat B target via NQ-198a 1/n scaling
- **Cat A path**: Conditional on Goldstone mass scaling formal proof

### §B.3.11 T-σ-Multi-1 (Cat B Target, CV-1.5.1)

- **위치**: §11.7
- **Status**: Cat B target (Goldstone-pair instability)

### §B.3.12 P-SINKHORN-STABILITY-CONDITIONAL (Cat B, CV-1.15)

- **위치**: §7.5 Action package
- **Status**: Cat B under H-SINK + MARGIN + SMALL-SINK-GAP

### §B.3.13 T-ACT-KERNEL-COMP→REL (Cat B Conditional, CV-1.17 활성화)

- **위치**: §7.4 + §7.5
- **Status**: Cat B conditional (activated by CV-1.17 T-CC-StableK-Kernel)

---

## §B.4 — Canonical Lacunae (Canonical 외부 또는 부분 정의)

### §B.4.1 Stage 0 Sensor T 9-Condition Hypothesis Package

- **Source**: pre_brainstorm §5.3
- **Status**: 9 conditions OPEN, canonical 미등록
- **위치**: §A.4 (U-excluded) + §B.2.1
- **Forward hook**: W10+ canonical promotion

### §B.4.2 OMS-1 ξ Catalog T_* Entry Amendment

- **Source**: 03_T_star §5.1 G1+G3 hybrid formalization
- **Status**: 미수행 (후속 결정 plan §E item 3)
- **위치**: §14.5 OMS-2.0 framework

### §B.4.3 AUX-1.6 Amendment (H5/T_* Status Update)

- **Source**: 99_summary plan §E item 1
- **Status**: 본 day 의 선택 산출 — 생략 (시간 분배 trade-off)
- **위치**: 99_summary Day 3 입력 매핑

### §B.4.4 Theorem_status.md Working Candidate Registration

- **Source**: 99_summary plan §E item 2
- **Candidates**: T-H5-MORSE-GENERIC (Cat A 후보), T-T*-EXIST-FP (Cat B 후보)
- **Status**: 미수행

### §B.4.5 OP-0021 본문 Amendment (Route A/B 폐기 + Route C 추가)

- **Source**: 03_T_star §5.2 silent OP resolution 회피 3-part 제안
- **Status**: *제안 only*, canonical 본문 미수정 (후속 결정 plan §E item 4)

### §B.4.6 OP-H5-MORSE-SPINODAL 정식 등록

- **Source**: 02_H5 §4 draft
- **Status**: Draft only, canonical Open Problems Catalog 미수정 (후속 결정 plan §E item 5)

### §B.4.7 OP-T*-FIXED-POINT 정식 등록

- **Source**: 03_T_star §4 draft
- **Status**: Draft only

### §B.4.8 OMS-2.0 Appendix Temporal Extension Sub-OP

- **Source**: canonical Appendix OMS temporal $\Sigma_{\mathrm{SN}}^{\mathrm{temp}}$
- **Status**: Conditional on (SN-iii)+(SN-iv) genericity (OP-OMS-033b)

### §B.4.9 Wigner Irrep Classification for Aut(G) Trivial Generic Graph

- **위치**: §6.1 σ_standard + §6.8 open issues
- **Status**: Generic graph Aut(G) trivial → equivariant Morse environment 부재
- **Implication**: σ-framework 의 *trivial group action degeneration* — canonical missing piece

### §B.4.10 K_field Individual Measurement Protocol

- **Source**: §10.1 R-nn-11 K_ind
- **Status**: Empirical anchor (F3 VSTM / F7 MOT) suggested, canonical anchor 부재
- **Cat B promotion candidate** (§17.2 forward hook)

### §B.4.11 Λ_coupling Explicit Functional Form

- **Source**: §11.4 inter-formation overlap
- **Status**: Configuration-specific only (scc/multi.py operational)
- **Cat B promotion candidate**

---

## §B.5 — Proved Failures + Warnings (Canonical Warnings)

### §B.5.1 T-SINKHORN-PLAN-SEMIGROUP-FAILS

- **위치**: §7.6
- **Status**: OPEN warning (canonical §12 warning, proved failure)
- **Implication**: Sinkhorn plan composition does NOT preserve semigroup property
- **Alternative**: T-CC-StableK-Kernel Cat B (CV-1.17) kernel-composed (§B.3.4)

### §B.5.2 Aut(G) Trivial Equivariant Morse Degeneration

- **위치**: §6.1 + §B.4.9
- **Status**: Generic graph (R-an-13 cortical magnification typical) → Aut(G) trivial → equivariant Morse → standard Morse (degenerate)
- **Implication**: Equivariant Morse (H5-b) approach 가 *generic graph 에서 *trivial environment* — H5-a Sard primary

### §B.5.3 D-5 V5b-T' Withdrawal (2026-04-29 W5-D3)

- **Source**: NQ-198f phantom — V5b-T' canonical entry candidate WITHDRAWN at CV-1.5.1
- **Implication**: Sub-spinodal translation-invariant regime has Goldstone $\mu = 0$ exact, NOT PN-barrier-lifted $O(\beta)$ Goldstone
- **위치**: canonical L1328 V5b-T-zero (Cat A definitional replacement)

### §B.5.4 V-AFD / R-2 / z_t Archive Pattern (Carry-Forward)

- **Source**: 5/15 결정 C 의 6-stage framework
- **Pattern**: *언어 재배치를 새 수학으로 잘못 인식한 것*
- **Implication**: 본 unified derivation 이 *동일 archive pattern* 위반 0 (§16.1 §8a P1-P6 = 0/6 PASS)
- **Forward hook**: 본 day 의 모든 작업이 *registry → theory* 격상 — *재포장* 부재

### §B.5.5 Cugliandolo Effective T (All Notions COB-Violating)

- **Source**: pre_brainstorm §5.2 effective T review
- **Status**: 모든 *out-of-equilibrium* effective T notion (FDT / kinetic / granular / active matter) → 환경 statistics 요구 → **CN-COB 위반**
- **Implication**: Route A/B 폐기 의 *근거* — §A.1 + §B.1.5

---

## §B.6 — Sketch-Level Proof Items (각 Wave 1-3 Agent's Sketch Sub-Items)

### §B.6.1 §2 Stage 0 — Sub-T Sketch Levels

- $T_{\mathrm{PSF}}$ Zernike convention 미고정
- $T_{\mathrm{sample}}$ Poisson stochasticity 의 deterministic interpretation
- $T_{\mathrm{LMS}}$ 의 phenotype-specific projection matrix
- $T_{\mathrm{gain}}$ adaptive baseline 결정
- $T_{\mathrm{CSF}}$ vs Stage 1 boundary (commit needed)
- $T_{\mathrm{temp}}$ 의 explicit gamma-shaped kernel parameters

### §B.6.2 §3 Stage 1 — Boundary Conditions

- $\Psi_{\mathrm{LMS}\to\mathrm{scalar}}$ canonical form (§B.2.7)
- $\mathrm{Norm}_{\Sigma_M}$ method (§B.2.8)
- $\beta_{\mathrm{crit}}^{(2)}$ graph-dependent variability (small-world vs lattice)

### §B.6.3 §4 Stage 2 — Conditional Items

- T-PF-A1-PE Cat A의 $C_P \sim e^{\mathrm{osc}/T_*}$ exponential scaling (metastable, large $n$)
- Reflected Langevin SDE의 stochastic regime 정확한 form (canonical Lions-Sznitman)
- $E$ Morse property 의존 (H5, §A.2)

### §B.6.4 §5 Stage 3 — Threshold Configurations

- $\rho_{\mathrm{pers}}(\theta)$ eccentricity profile parameteric form (configuration-specific, §A.5)
- Threshold $\theta_{\mathrm{core}}, \theta_{\mathrm{in}}, \theta_{\mathrm{supp}}$ canonical default 부재 (§A.5)
- Per-PersComp morphology $Q_{\mathrm{morph}}$ normalization (§B.2.9)

### §B.6.5 §6 Stage 4-5 — σ-Framework Lacunae

- Wigner irrep classification Aut(G) trivial (§B.4.9)
- σ orbital framework 의 generic graph application
- Reflected Langevin 의 sampling efficiency in metastable regime

### §B.6.6 §7 Stage 6-7 — σ-Inheritance Lacunae

- T-σ-Inherit parts (c)/(d-σ_standard) Cat C (§B.1.2, §B.2.5-6)
- EVENT_TYPES (smooth/merge/split/birth/death) discrimination canonical form
- Multi-time temporal energy $E_{\mathrm{tr}}$ 의 SCC 안 explicit form

### §B.6.7 §8 Operators — Auxiliary Operators

- Aggregation operator의 canonical form
- σ-readout operator의 explicit form (generic graph case)
- Stage operators의 type signature 완전한 specification

### §B.6.8 §9 Predicates — Threshold Sensitivity

- Bind / Sep / Inside / Persist 모두 thresholds 의존 — *meaningful comparison* only at fixed thresholds

### §B.6.9 §11 Multi-Formation — Coupling Forms

- Mass split $(M_1, \ldots, M_K)$ 의 attention strategy $m_{\mathrm{attn}}$ canonical form (§A.3, seed-decoded)
- Inter-formation transport (transport_k_formations modes) 의 mode 선택 (canonical default 부재)

### §B.6.10 §12 Stereo — Backprojection

- Backprojection의 explicit form (canonical 부분 정의)
- Stereo σ-inheritance (D-ST-4 extension of Stage 7)

---

## §B.7 — Open Questions (Meta-Level, 본 day 의 NEW)

### §B.7.1 True Class 4 Residue Empty 가능성

- *Class 4 (idio seed) entries* 가 *원리적 환원불가* 인가 *epistemic gap dumping* 인가 결정 부재
- Class 2/3 정밀화 진전 시 Class 4 → Class 2/3 migration 가능성
- 본 *meta-ontological question* — SCC 의 가장 깊은 question
- 본 day 의 *bypass* (256-bit seed): *operational form*, *ontological resolution 부재*

### §B.7.2 Seed Cardinality 충분성

- $\lvert s \rvert = 256$ bits, $2^{256} \approx 10^{77}$ distinct observers
- *Physical universe 의 모든 개인* 표현 충분 — 단 *higher-resolution* regime 존재?
- Cryptographic hash function (SHA256) 의 *computational indistinguishability* 가정 의 한계

### §B.7.3 FEP (Free Energy Principle) Integration

- Pre_brainstorm §7.3 leading question
- SCC = FEP graph-based specialization 가설
- 본 day 채택 부재, W9+ leading question
- 본 가설 의 *증명 또는 반증* meta-task

### §B.7.4 Stage 0/Stage 1 Boundary Commitment

- Spatial CSF (R-nn-5) 의 Stage 0 마지막 부 vs Stage 1 의 일부 commitment
- Canonical commit 부재
- 본 unified derivation 의 *Stage 0 마지막 부* 선택 (§2.6)

### §B.7.5 CV-1.13 T-Temporal-Identity 의 본 Framework Operational Form Match

- §7.3 4 parts (a/b/c/d) 의 본 unified derivation interface 와 *정확히 match* 검증 부재
- T-CC-StableK-Kernel (CV-1.17) 의 활성화 조건 추가 verification

### §B.7.6 Distinctive vs Secured Layer Boundary

- Distinctive layer (σ-inheritance + OMS-2.0 quotient): §6 + §7 + §11 + §14
- Secured layer (T8 + T-L1-F + T-Temporal-Identity + T-σ-supporting): §3 + §5 + §10
- 본 file 의 *both layers' unified operational form*
- Cat A advance 의 priority asymmetry

### §B.7.7 Conversation-Derived Promotion Candidates Canonical Path

- L3 hyperparam compression, 4-class taxonomy, 30 root extraction, 5 MG grouping, seed-based pseudorandom observer identity — 모두 *informal conversation outcome*
- Canonical promotion path 부재 (working file 작성 only)
- 본 file 자체가 *informal-to-formal bridge*

---

# §C. Summary — Meta-Organization

본 file 의 *역할*: 2026-05-19 unified derivation 의 *모든 caveats / lacunae / OPEN items / U-residue* 의 *single-file index*. 후속 사용 (W8-Day3, W9 planning, canonical promotion priority) 의 *direct reference*.

## §C.1 Coverage Statistics

| Category | Count |
|---|---|
| §A U-excluded items (axiomatic-free / canonical 외부) | **7** (T_*, H5, Class 4, Stage 0, configuration-specific, K_field, CN-COB) |
| §B.1 Open Problems (현재 OPEN) | **10** (OP-0005-DYN, 0008, 0009, 0012-SINK, 0021, HMORSE-LOCAL-A, H5-MORSE-SPINODAL, T*-FIXED-POINT, OMS-033b, N-1) |
| §B.2 Cat C SKETCH items | **9** (Stage 0, H5-α, T*-α, Brouwer L1, T-σ-Inherit (c)/(d), Ψ_LMS, Norm_Σ, Q_morph) |
| §B.3 Cat B conditional items | **13** (T-P-F-ε0-K, T-K-Select-PF/OBS, T-CC-StableK-Kernel, T-σ-Inherit parts, L-HMORSE-LOCAL/DECOMP, T-OP6-B, L-BOUNDARY-MODE-EXCLUSION, V5b-F-empirical, T-σ-Multi-1, P-SINKHORN-STAB, T-ACT-KERNEL-COMP) |
| §B.4 Canonical lacunae | **11** (Stage 0 9-조건, OMS-1 ξ amendment, AUX-1.6, theorem_status registration, OP-0021/H5/T* 본문, Appendix temporal, Wigner Aut(G), K_field measurement, Λ_coupling form) |
| §B.5 Proved failures + warnings | **5** (T-SINKHORN-FAILS, Aut(G) trivial, V5b-T' withdrawal, V-AFD/R-2 carry-forward, Cugliandolo COB violation) |
| §B.6 Sketch-level proof items | **10 groups** (각 Stage/section 별 sub-items) |
| §B.7 Open meta-questions | **7** (Class 4 residue, seed cardinality, FEP integration, Stage 0/1 boundary, CV-1.13 match, layer boundary, promotion path) |
| **Total** | **72 distinct entries** |

## §C.2 Cross-Reference Map

| §A U-excluded item | §B problematic counterparts |
|---|---|
| §A.1 T_* | §B.1.5 OP-0021 + §B.4.2 OMS-1 ξ amendment + §B.4.5 OP-0021 본문 |
| §A.2 H5 | §B.1.7 OP-H5-MORSE-SPINODAL + §B.2.2 OP-H5-α + §B.3.1 T-P-F-ε0-K + §B.4.6 정식 등록 |
| §A.3 Class 4 | §B.7.1 residue empty 가능성 + §B.7.2 seed cardinality |
| §A.4 Stage 0 lacuna | §B.2.1 Stage 0 sketch + §B.4.1 9-조건 + §B.6.1 sub-T sketches |
| §A.5 Configuration-specific | §B.6 throughout sub-items |
| §A.6 K_field cap | §B.4.10 measurement protocol |
| §A.7 CN-COB | §B.5.5 Cugliandolo COB violation |

## §C.3 Priority Sort (Cat A Promotion Candidates)

**HIGH priority (W9+ priority)**:
1. OP-H5-α (Hironaka detail) — §B.2.2
2. OP-T*-α (multiplicity quantification) — §B.2.3
3. OP-0008 σ_standard Cat C → Cat B — §B.1.2
4. OP-HMORSE-LOCAL-A Cat B → Cat A — §B.1.6
5. Stage 0 sensor T 9-조건 canonical 등록 — §A.4 + §B.4.1
6. canonical OMS-1 ξ T_* amendment — §B.4.2

**MED priority**:
7. OP-0009 (multi-formation ontological) — §B.1.3
8. OP-0012-SINK (Sinkhorn scaling) — §B.1.4
9. AUX-1.6 amendment — §B.4.3
10. theorem_status.md working candidate registration — §B.4.4
11. K_field individual measurement protocol — §B.4.10
12. Λ_coupling explicit form — §B.4.11

**LOW priority**:
13. OP-OMS-033b (sub-OP) — §B.1.9
14. Q_morph normalization — §B.2.9
15. Aut(G) trivial Wigner Irrep classification — §B.4.9

**Meta (long-term)**:
16. §B.7.1 True Class 4 residue empty 가능성 — *philosophical-mathematical* meta-question
17. §B.7.3 FEP integration — W9+ leading hypothesis
18. §B.7.7 Conversation-derived promotion canonical path — *bridge* problem

## §C.4 Forward Hooks Summary

본 file 의 *후속 작업 의 primary reference*:

- **W8-Day3 candidate priority**: §C.3 HIGH 의 1-2 항목 (Hironaka detail 또는 Stage 0 prerequisite work)
- **W9 entry**: Distinctive layer Cat A push (OP-0008 + Route C unification, §B.1.2 + §B.1.5)
- **W10+**: Stage 0 canonical 등록 + OMS-1 ξ amendment 동반 (§A.4 + §B.4.2)
- **Long-term**: Class 4 residue empty/non-empty determination + FEP integration evaluation (§B.7.1 + §B.7.3)

---

## §D. Self-Audit

| 검사 | 결과 |
|---|---|
| canonical 0 edits | ✓ (본 file = working/ 산출, canonical untouched) |
| 새 어휘 생성 0 | ✓ (모든 어휘 canonical 또는 본 day conversation 표준 form) |
| Silent OP resolution 0 | ✓ (모든 OPs *명시* OPEN status 표기; Route A/B *폐기 제안* 만, *해결* 주장 부재) |
| §8a archive pattern P1-P6 | 0/6 부합 (본 file = *consolidation reference*, *재포장* 부재 — 모든 entries 가 canonical/SCC_unified_derivation 의 *cross-reference*) |
| §8b 5 self-discipline | 5/5 PASS |
| Cross-reference precision | 본 file 의 각 entry 가 *unified derivation §X* + *canonical anchor* 명시 |

**Verdict**: Cat C SKETCH consolidation reference. *Working file*, not canonical promotion. *Primary use*: W8-Day3 onwards priority routing + W9+ canonical promotion roadmap.

---

*End of SCC_U_excluded_and_problems_v0.1.md.*

**File**: `/home/jack/Perception_theory/THEORY/working/foundation/SCC_U_excluded_and_problems_v0.1.md`
**Lines**: ~700 expected
**Predecessor**: `SCC_unified_derivation_v0.1.md` (4633 lines, 18 sections, ~278 derived definitions)
**Status**: Cat C SKETCH consolidation reference. Canonical 0 edits.
