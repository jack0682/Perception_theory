# pre_brainstorm.md — 2026-04-30 (W5 Day 4 morning brainstorm)

**Author**: User reflection at Day 4 morning, before plan.md execution.
**Purpose**: Day 4 mental frame + decision pre-think + 7-agent verdict 흡수 + Critic 보강 정당화 + execution risk premortem.
**Read first**:
1. `THEORY/logs/daily/2026-04-29/99_summary.md` §11 (deepening pass).
2. `THEORY/logs/daily/2026-04-29/11_NQ198fg_results_and_D5_withdraw.md` (D-5 WITHDRAW final).
3. `THEORY/logs/daily/2026-04-29/08_user_decisions_log.md` (Day 3 user decisions).
4. **7-agent analysis report 2026-04-29 EOD** (메인 conversation에 종합).

---

## §1. Mental Frame for Day 4

Day 3는 **3-stage 진화**였다 — consolidation (Stage A 5 files) → deepening (Stage B 3 files, 2 negative results) → numerical reversal (Stage C 5 files + 3 scripts/results, **3rd negative result + D-5 WITHDRAW**). 이 패턴은 plan대로가 아니지만 **outcome quality가 plan을 능가**했다 (V5b-T' phantom을 머지 직전에 검출).

Day 4 question: **3-stage Day 3의 산출물을 어떻게 견고한 canonical 머지로 변환하는가, 그리고 7-agent verdict의 process-level 보강을 어떻게 통합하는가?**

7-agent 합의에 따르면:
- **Architect**: σ-framework는 paper-§4 cross-reference를 위한 deliberate canonical-density choice. CV-1.5는 첫 single-formation closure. V5b family는 fracturing 중 — Day 4 머지로 안정화.
- **Scientist**: μ = 13.2·|∂S|/n empirical law는 robust (CI [12.84, 13.64], SNR 35). LSW α [0.25, 0.30]은 universal 아닌 λ-dependent. V5 3D는 통계적으로 0과 구별 불가능. langevin/k_soft 모듈 테스트 0건.
- **Critic**: REVISE 판정. 3 CRITICAL findings (T-σ-Theorem-4 Cat A 격하 권고, promotion pipeline은 D-5에서 작동하지 않음, Theorem 4.6.1 working/ 승급 시 Cat C로 라벨 정정 필요, Paper §4.4 4-8h 재작성 필요).
- **Analyst**: F-1/M-1/MO-1 RESOLVED는 *temporally conditional*; MO-1은 D-6b 머지 시 재활성. σ^A K-jump 비결정성을 OP-0008 등록 권고. 5 dormant medium OPs (4개월 progress 0).
- **Code Explore**: 코드↔canonical 정합성 PASS. langevin.py + k_soft.py 미테스트 (load-bearing).
- **Planner**: Path 1 RECOMMENDED, NQ-244 Day 4 PM staging, CV-1.5.1 → CV-1.6 → CV-1.7 → v2.0 timeline 견고.
- **Document specialist**: Paper §4.4가 V5b-T' WITHDRAW로 narrative collapse — 5건 specific fix + 14 외부 reference 매핑 (Lifshitz-Slyozov 1961, Bertozzi 2017, Royal Society A 2021, etc.).

**Path 결정**: **Path 1 + Critic 보강** (Path 2 변형). 단일 09:15 user authorization으로 Block 1+3 일괄 진행.

**Day 4 색깔**: **focused-promotion** (consolidation도 expansion도 아닌, 익은 결과를 견고하게 통합). 가장 큰 시간 블록은 morning 75min (canonical apply) + afternoon 4h (Paper §4.4 v2). 두 임팩트 사이에 Block 2-3 (verification + OP register, 1h) + Block 5-6 (working promote + NQ-198l, 1h).

---

## §2. Decision Pre-Think for Block 1 09:15 USER AUTH

### §2.1 사용자가 yes 선택 시 (Path 1 + Critic 보강 전체 batch)

**진행**: Block 1 (canonical apply 75min) → Block 2 (verify 30min) → Block 3 (OP register 30min) → Block 4 (Paper §4.4 v2 4h) → Block 5 (working promote 30min) → Block 6 (NQ-198l 30min) → NQ-244 background → Block 7 (EOD 45min).

**Total**: ~9h. lunch 1h 포함 시 ~10h elapsed. 19:00 Day 4 close.

**EOD state**:
- canonical CV-1.5.1 official: 45A / 59 claims / 76% proved.
- T-σ-Theorem-4 Cat B (격하 retroactive).
- OP-0008 신규 + MO-1 라이더.
- Paper §4.4 v2 LaTeX-ready.
- Theorem 4.6.1 working/ promoted (Cat C 라벨 정정).
- V5b-T-zero confirmed via NQ-198l.
- NQ-244 background running (Day 5 morning analysis).
- Git commit: 4-month gap closed.

### §2.2 사용자가 modify 선택 시 (subset 지정)

**가장 가능성 높은 modifications**:

**Modification A**: "T-σ-Theorem-4 격하는 빼고 진행."
- 근거: Cat A 격하는 retrospective revision이라 외부 reviewer 신호로 부정적일 수 있다 (Cat A entry가 흔들리면 신뢰도 저하).
- 대안: T-σ-Theorem-4 entry에 inline "Errata Round 1: corrected K_1 = K_0 leading order" 명시만 추가 (status는 Cat A 유지).
- 영향: Day 4 Block 1 60min으로 단축. 그러나 Critic verdict (`Cat A label degradation` 위험) 부분 흡수 못함. **권고는 Critic 따른 격하**이지만 사용자 권한.

**Modification B**: "OP-0008 등록은 빼고 Theorem 4.6.1 caveat으로만 흡수."
- 근거: OP 등록 빈도가 너무 잦으면 OP 카운트만 늘어남.
- 대안: working/MF/sigma_multi_trajectory.md §3.1에 σ^A K-jump 비결정성 강조 + canonical에 caveat note 없음.
- 영향: open_problems.md 변경 없음. Day 4 Block 3 skip (30min 절약). Analyst의 "다중 파일 참조 + tracking visibility" 권고 부분 미수용. 향후 NQ-242c 결과가 deterministic 발견 시 OP-0008 등록 자체 불필요.

**Modification C**: "D-6a까지가 너무 많다. D-1, D-2, D-3, D-4까지만."
- 근거: D-6a Multi-Static은 σ_multi^D involution canonical-iso 의존성 + Σ^{K,interior}_M corner 회피 (Option A pragmatic) 등 복잡도 高. user는 D-6a를 W6 NQ-242 후로 미루고 싶을 수 있음.
- 영향: canonical delta ~95-100 → ~60-65 lines. Cat A net +0 - 1 = **−1** (T-σ-Theorem-4 격하만 적용 시). CV-1.5.1 명목적 (Cat A 감소만). **W5 Ambitious 사다리는 부분 only**.

**Modification D**: "Paper §4.4 재작성은 Day 5로 미뤄. Day 4는 canonical/OP만."
- 근거: Block 4가 Day 4 가장 긴 단일 작업. 사용자 검토 시간 필요. Day 5 morning (NQ-244 결과 후)에 §4.4 + §4.5.5 통합 수정이 더 효율적.
- 영향: Day 4 EOD ~14:00. 짧은 day. Day 5 길어짐. **권고**: 합리적 선택. NQ-244 결과를 §4.5.5에 반영해야 한다면 Day 5 통합이 자연스러움.

### §2.3 사용자가 no 선택 시 (Defer-all)

**진행**: Block 4 (Paper §4.4 v2) + Block 6 (NQ-198l) + NQ-244 background + Block 7 (EOD short).

**EOD state**:
- canonical CV-1.5 유지.
- Paper §4.4 v2 LaTeX-ready (V5b-T' WITHDRAW 반영, 단 canonical-promote 안 됨).
- V5b-T-zero confirmed via NQ-198l.
- W5 Ambitious 사다리 도달 못함. Stretch 사다리 ~30%.

**Recommendation if no**: 사용자에게 Path 1 권고하되 modifications A/B/D를 옵션으로 제시. 완전 Defer는 Day 4 가치 절반 이하.

### §2.4 사용자가 Critic 보강만 거부 시 (D-1~D-4+D-6a만 진행)

이게 default Day 3 EOD plan과 동일. 7-agent Critic verdict 부분 미수용.

**Risk**: T-σ-Theorem-4 Cat A 라벨이 errata-with-Cat-A-preserved 상태로 머지. 향후 Paper 1 reviewer가 발견 시 신뢰도 risk. **권고**: 적어도 inline `*Status revision*` note는 추가 (Modification A 변형).

---

## §3. Critic 보강 항목 정당화 자세히

### §3.1 T-σ-Theorem-4 Cat A → Cat B 격하

**근거 chain**:
1. `91_critical_review.md` §3.2: Round 1 evening errata가 발견한 structural error. 원본 statement (ii) "$0 < K_1 < K_0$ would-be transverse Goldstone, partial lifting from discrete $D_4 \to \mathbb{Z}_2$"는 **이산 대칭 깨짐엔 Goldstone 없다**는 사실 위배.
2. `91_*` §5.1: Author's own admission — "second-order direct corrections...gave numerical estimates with $K_1^{\text{est}} = (1/2)|W''(c)|$ — half of the correct $K_1 = 4|W''(c)|$ value, and went into in-text 'Wait — this gives Morse-1, not Morse-0' admission **without resolving**."
3. **결론**: 머지 시점 internal contradiction (Morse-1 vs Morse-0)이 unresolved 상태에서 Cat A 라벨 부여 → Cat A 정의 위배.

**Critic 권고**: Cat B로 retroactive 격하. theorem_status.md C-0716 row + canonical.md §13 entry inline note. Theorem statement 자체는 corrected ($K_1 = K_0 = 4|W''(c)|$ on $D_4$ leading order)하니 결과 유지하나 **process audit retroactive**.

**가능한 반론** (modification A): "Errata는 inline note로 충분; 격하는 over-reaction." 단, 이 입장이면 Cat A는 process status가 됨 (Critic verdict #1).

### §3.2 OP-0008 σ^A K-jump 비결정성 등록

**근거 chain**:
1. `04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c): K-jump map Φ가 pre-merger σ^A 단독으로는 결정 안 됨. Merger geometry M 필요.
2. `06_open_problems_development_synthesis.md`: "σ^A K-jump 비결정성"이 substantive negative result로 명시.
3. `09_session_self_critique.md` §2.3: "Lemma 4.4.1(c) should be Cat C (conjectured), not Cat B sketch."
4. **Phase 8 T4** (`2026-04-28/32_U5_SCC_CH_theorem.md`)이 implicit으로 가정한 deterministic-σ-trajectory 위배.

**Analyst 권고**: 별도 OP 등록 (NQ-242c 캐치-올 sub-tree로 두면 visibility 부족). HIGH severity (CV-1.6 release path bifurcation: Cat A vs Cat B).

**가능한 반론** (modification B): "Theorem 4.6.1 working/MF/ caveat으로 충분, OP는 over-classification." 단, Phase 8 T4 SCC↔CH correspondence Paper §4.5.7도 caveat 필요해서 multi-file reference라 OP-등록이 더 깔끔.

### §3.3 OP-0003 MO-1 "Re-activation trigger" 라이더

**근거 chain**:
1. `open_problems.md` line 134 자체가 명시: "MO-1 returns as an active blocker if/when the theory extends to multi-formation σ".
2. `04_*` §5.4: "explicit re-engagement of MO-1, NOT silent resolution."
3. **W5 G3 Phase 5 = multi-formation σ Phase 5** = **MO-1 재활성 가능 영역**. D-6a는 Σ^{K,interior}_M에 한정 (corner 회피); D-6b는 σ_multi^A(t) trajectory로 corner-적극 다룸.
4. **Critic**: 현재 "✅ SIDESTEPPED" 라벨이 over-claim (`scope-conditional resolution`을 absolute resolution으로 표기).

**라이더 add 효과**: CV-1.6 시점에 자동 재활성. Critical OP 카운트 0 유지가 *temporally conditional*이라는 것 명시.

**가능한 반론**: "라이더는 cluttering. summary 표만 업데이트로 충분." 단, summary 표만 변경 시 OP entry 본문은 misleading.

---

## §4. Paper §4.4 v2 재작성 priorities (Block 4)

### §4.1 5건 수정 우선순위 (가장 critical 순)

1. **§4.4.2 Theorem 4.4.2 V5b-T-zero 재서술 (highest priority)**: V5b-T' phantom 자체. 이걸 못 고치면 Paper 1 Submit 못함.
2. **§4.4.4 Eq. (4.20) range narrowing**: 통일 PN-barrier 공식이 V5b-T-zero 적용 안 됨. 명시 필수.
3. **§4.4.5 Regime Map R3b 행**: 1줄 수정. 빠르고 cosmetic.
4. **§4.4.3 V5b-F functional form 완화**: NQ-198a 1/n + NQ-198g 비단조 결과 흡수.
5. **§4.5.7 dynamic CH caveat**: σ^A K-jump 비결정성 OP-0008 reference 추가.

### §4.2 §4.4 narrative arc 재정립

**기존 (V5b-T'를 포함한 3-class)**:
- §4.4.1 V5b-T (super-lattice) → exp-suppressed
- §4.4.2 V5b-T' (corner-saturated, translation-invariant) → PN-lifted O(β)
- §4.4.3 V5b-F (corner-saturated, translation-broken) → mixed

**Day 4 신규 (V5b-T-zero를 포함한 3-class)**:
- §4.4.1 V5b-T (super-lattice, spinodal interior) → exp-suppressed positive
- §4.4.2 V5b-T-zero (corner-saturated, translation-invariant, sub-spinodal) → exact zero (Goldstone on Z_L^d)
- §4.4.3 V5b-F (corner-saturated, translation-broken, free-BC) → C(β)·|∂S|/n empirical

**핵심 통찰**: 3 classes 중 2 (V5b-T + V5b-T-zero)가 translation-invariant graph에서 c-dependent transition (ζ_*에서). V5b-F는 별도 graph topology (translation-broken). **Topology(translation-invariant vs translation-broken) × spinodal-position(interior vs sub-spinodal) = 2×2 = 4 cells. 그 중 corner-saturated translation-broken sub-spinodal = V5b-F.** (super-lattice translation-broken은 별도 cell이지만 보고된 적 없음.)

### §4.3 14 외부 reference 통합

Document specialist가 매핑한 14건 중 Block 4 Paper §4.4 v2에 직접 인용 가능한 것:

**§4.4.2 V5b-T-zero**:
- Goldstone, Salam & Weinberg 1962 (Goldstone theorem foundation)
- Wikipedia "Goldstone boson" — discrete crystal momentum
- Bertozzi et al. 2017 (graph Allen-Cahn → discrete Goldstone)

**§4.4.3 V5b-F**:
- Royal Society A 2021 "Topological origin of PN barrier"
- arXiv:hep-th/0003015 "Quantum Peierls-Nabarro barrier"

**§4.4.4 Unified PN range**:
- 위 V5b-F references + Bertozzi 2017 (discrete graph context)

**§4.5.7 SCC↔CH dynamic caveat**:
- Cahn & Hilliard 1958 (CH foundation)
- Kato 1980 *Pert. Theory Linear Operators* (analytic perturbation; Lemma 4.2.1 background)
- Goresky & MacPherson 1988 *Stratified Morse Theory* (forward reference for Paper 3)

**Bibliography placeholder**: `\bibitem{...}` syntax 또는 plain markdown citation. Block 4 끝에 일괄 추가.

---

## §5. NQ-198l + NQ-244 pre-think

### §5.1 NQ-198l (Block 6 in-session, 30min)

**Goal**: V5b-T-zero (former V5b-T') μ ≈ 0 결론을 더 큰 토러스 (T²_40)에서 확인. NQ-198f L=28 outlier μ = 0.028이 finite-size noise인지 systematic signal인지 결정.

**Predict**:
- L=40에서 |μ| < 0.005 (5x 더 작아야 함; finite-size noise는 1/L² 또는 1/L 수렴) → **PASS** (V5b-T-zero 확정)
- L=40에서 |μ| ∈ [0.005, 0.020] → **Ambiguous**; L=80 W6 Day 1 추가 필요
- L=40에서 |μ| > 0.020 → **FAIL**; V5b-T-zero 결론 약화; §4.4.2 caveat 추가

**Pre-flight check**: NQ-198f script 재사용 가능? Yes — `cluster_size`, `boundary_condition`, `grid_size` 파라미터만 변경. 새 파일 ~250 lines (대부분 V5b 원본 source 재사용).

**Risk**: T²_40에서 corner-sat cluster 형성 안 됨 (NQ-198f T²_28에서도 c=0.1 case는 flat state로 갔음). c=0.3 + m=120/160으로 robust 형성 권고.

### §5.2 NQ-244 (background 18:00 launch, Day 5 analysis)

**Goal**: 3D LSW T³_15 K=10에서 α plateau publishable value 결정. Phase 10 V5 (T³_10 K=4)의 "insufficient statistics" caveat 해소.

**Predict**:
- α ∈ [0.20, 0.30] with R² > 0.5 → **publishable**; §4.5.5 caveat 제거 가능
- α ∈ [0.05, 0.20] OR R² < 0.5 → **partial**; §4.5.5 caveat 약화
- α ≈ 0 OR negative → **negative result**; §4.5.5 caveat 강화

**Compute estimate**: T³_15 = 3375 nodes, K=10, t_max=200, dt=0.05 → 4000 steps × ~0.3s/step = ~20min/seed × 3 seeds = ~1h. 18:00 launch → 19:00 finish (Day 4 EOD 후).

**Risk**:
- OOM: 3375 nodes × K=10 시 multi-formation arrays가 ~MB. 안 OOM 예상.
- Hang: simplex barrier λ_bar 조정 필요할 수 있음 (3D는 2D와 다름).
- 결과 자체가 noisy: 3 seeds로 SE 측정. R² < 0.5면 5 seeds Day 5 추가.

**Day 5 morning task**:
1. `CODE/scripts/results/nq244_run.log` 읽기.
2. JSON 결과 파싱.
3. α fit + R² + SE 계산.
4. §4.5.5 update.

---

## §6. Templates 본문

### §6.1 D-1 + D-2 canonical insert (§11.1 Commitment 14 addendum)

```markdown
**Commitment 14 (O5'): Multi-irrep eigenspace ordering convention.**
At minimizers $u^*$ where the Hessian $H_E(u^*)$ has multi-dimensional
eigenspaces with distinct irreducible representations, the σ-tuple ordering
follows: (i) increasing eigenvalue; (ii) within degenerate eigenspace,
canonical irrep order via Mulliken character convention; (iii) within
isotype block, lexicographic on basis representative. This convention is
required for σ-tuple to be a well-defined discrete invariant. (cf. T-σ-Lemma-1
canonical structure; W5 Day 1 Round-2 audit `92_critical_review_round2.md`
§2.1.)

**Commitment 14 (O7): Tie-breaking via Mulliken character order.**
At first-pitchfork on $D_4$ (Theorem 4 corrected leading order: $K_0 = K_1$),
the σ-tuple selects the trivial $A_1$ irrep before sign $A_2$ per Mulliken
character order (alphabetical-numerical). Higher-order $\epsilon$ splitting
(NQ-187, W7+) may require revision. (cf. W5 Day 1 Round-2 audit §2.2;
T-σ-Theorem-4 well-definedness note.)
```

### §6.2 D-3 V5b-F rider (§13 T-V5b-T entry sub-statement add)

```markdown
*Sub-statement (V5b-F-empirical, Cat B target via NQ-198a 2026-04-29):*
For sub-spinodal corner-saturated minimizer on translation-broken graphs
(free-BC), Goldstone eigenvalue obeys empirical scaling
$$\mu_{\text{Gold}}^{\text{V5b-F}} \approx C(\beta) \cdot \frac{|\partial S|}{n}$$
with $C(\beta=4, \xi_0=0.5) \approx 13.2 \pm 0.4$ measured on 6 corner-sat
configurations across $L \in \{14, 20, 28, 40\}$, within-setup CV $< 0.001\%$,
SNR $\approx 35$. The full $C(\beta, \xi_0)$ functional form is open
(NQ-198k W6+; preliminary $\beta$-scan NQ-198g shows $C/\beta$ non-monotone
ruling out simple $\beta^p$ form).

(Source: `THEORY/logs/daily/2026-04-29/07_NQ198a_results_and_D5_finalization.md`
+ `11_NQ198fg_results_and_D5_withdraw.md` §2.)
```

### §6.3 D-4 ζ_* precise (§13 T-V5b-T-(d) replace)

```markdown
**(d) Critical crossover $\zeta_*(G, c)$ precise (Cat A in 2D torus).**
For 2D translation-invariant graphs with mass-density $c$, the dual-regime
crossover satisfies
$$\zeta_*(G, c) = \begin{cases}
0.40 \pm 0.02 & \text{at } G = T^2_{20}, c = 0.10 \\
0.43 \pm 0.02 & \text{at } G = T^2_{20}, c = 0.20 \\
0.46 \pm 0.03 & \text{at } G = T^2_{20}, c = 0.30
\end{cases}$$
(NQ-174 measurement, c-dependent precise; supersedes earlier bracket
$\zeta_* \in [0.4, 0.5]$.) Functional form $\zeta_*(c)$: linear in $c$ over
$c \in [0.1, 0.3]$; behavior at higher $c$ is open (NQ-174c W7+).

(Source: `THEORY/logs/daily/2026-04-28/F5_grid_extension.md`.)
```

### §6.4 D-6a Multi-Static (§11.1 + §13)

```markdown
**Commitment 14-Multi (Static): Multi-formation σ-signature on K-field.**
Extend Commitment 14 to K-field architecture on $\widetilde{\Sigma}^{K,
\text{interior}}_M$ (interior-only, corners excluded per Option A):
$$\sigma_{\text{multi}}(\mathbf{u}^*) = \big(\sigma^A(\mathbf{u}^*),
\sigma^D(\mathbf{u}^*)\big)$$
where $\sigma^A$ = within-formation single-σ tuples per formation index
$j = 1, \dots, K$; $\sigma^D$ = between-formation cohomology pull-back
encoding inter-formation distinguishability.

A ⊥ D complementarity (Theorem 4.2.3 of Paper §4): A captures
within-formation Hessian structure invariant under formation labeling; D
captures cross-formation structure that survives formation-index permutation.
Joint $\sigma_{\text{multi}}$ is a complete static discrete invariant on
$\widetilde{\Sigma}^{K,\text{interior}}_M$.

Dynamic extension $\sigma_{\text{multi}}^A(t)$ deferred to W6+ via NQ-242
(see OP-0008 σ^A K-jump non-determinism; Theorem 4.6.1 framework at
`working/MF/sigma_multi_trajectory.md`).
```

§13 신규 entries (3 C-IDs): C-0717 / C-0718 / C-0719. (See plan.md §3 Block 1 step 4 for entry templates.)

### §6.5 OP-0008 entry (§3 OP-0008 본문)

(See plan.md §3 Block 3 for full entry — copy-paste 가능.)

### §6.6 CHANGELOG 04-30 entry

(See plan.md §3 Block 1 step 6 for full template — copy-paste 가능.)

### §6.7 Git commit message

(See plan.md §3 Block 7 for full HEREDOC — copy-paste 가능. Co-Authored-By 명시.)

---

## §7. Risk Premortem (가장 가능성 높은 실패 시나리오)

### §7.1 Risk: 09:15 user authorize에서 modifications 많이 들어옴

**가장 가능성 높음** (probabilistic ~50%): user는 Day 4의 batch authorize에서 일부 항목을 미루거나 거부.

**Mitigation**:
- 각 modification (A/B/C/D) 별 elapsed-time + ladder-impact 미리 계산 (위 §2.2).
- "modify [items]" 답변 시 즉각 subset-aware Block 1 진행.
- Block 7 EOD `99_summary.md`에 modifications + reason 명시 (process tracking).

### §7.2 Risk: Block 4 Paper §4.4 v2가 4h를 초과

**가능성 ~30%**: V5b 분류 재정의가 깊다. §4.4.4 unified formula 적용범위 narrow도 정확한 수학 작업.

**Mitigation**:
- §4.4.5 Regime Map (15min, mechanical) 먼저 → §4.4.3 (30min) → §4.4.2 V5b-T-zero (60min, 핵심) → §4.4.4 (45min) → §4.5.7 (45min, 가장 separable).
- 4h 초과 시 §4.5.7 caveat을 Day 5로 이동 (separable, OP-0008 reference만 유지).
- §4.4.1 connecting note는 5min 작업 — 마지막에.

### §7.3 Risk: NQ-198l 결과가 Ambiguous

**가능성 ~25%**: T²_40에서 |μ| ∈ [0.005, 0.020] 가능. Finite-size 1/L² 외삽 시 0으로 가지만 confidence 낮음.

**Mitigation**:
- Day 4 §4.4.2 V5b-T-zero entry에 caveat: "Numerical anchor: NQ-198f T²_28 |μ| ≤ 0.028; NQ-198l T²_40 [PASS / Ambiguous]; full L→∞ extrapolation NQ-198l-extended W6+."
- W6 Day 1 NQ-198l extension (T²_80) 우선 schedule.

### §7.4 Risk: NQ-244 background OOM/hang

**가능성 ~20%**: T³_15 (3375 nodes) × K=10 가 메모리 부족. Phase 10 V5는 T³_10 (1000 nodes) × K=4였다.

**Mitigation**:
- 18:00 launch 후 18:15 즉시 `tail -50 nq244_run.log`로 first-iter 메모리 상태 확인.
- OOM 신호 시 즉각 kill, T³_12 (1728 nodes) × K=8로 다운사이즈 Day 5 재시도.
- 또는 K=5로 downsize (formation 당 nodes 더 많아져 분리도↑).

### §7.5 Risk: Test failure post-edit

**가능성 ~5%**: canonical edit는 코드 변경 아님 → tests 영향 없어야 함. 그러나 Day 3 Day 4 untracked code (NQ-198a/f/g/l scripts)에 부수효과 있을 수 있음.

**Mitigation**:
- Pre-flight (Block 0)에서 baseline 확보.
- Post-edit Block 2에서 verify.
- Failure 시 즉각 `git diff CODE/`로 변경 source 식별.

### §7.6 Risk: Git commit hook fail

**가능성 ~10%**: 4개월 첫 commit. line ending, large file size, hook policy 등.

**Mitigation**:
- Block 7 commit 전 `git status` 확인 (untracked / staged 정합성).
- `git config --get core.autocrlf`로 line ending policy 확인.
- 큰 JSON (nq198a 1987 lines, nq198f 1445, nq198g 1360) 단일 commit OK 예상; 그러나 size hook 있으면 분리 commit.

### §7.7 Risk: 7-agent verdict modifications 후 user remorse

**가능성 ~15%**: T-σ-Theorem-4 Cat B 격하가 retrospective. 사용자가 "외부 reviewer가 보면 신뢰도 약화 신호로 읽힐 위험 있다 — Cat A 유지하되 Errata는 명시" 입장 가능.

**Mitigation**:
- 09:15 authorize에 명확한 modification A 옵션 제시.
- 사용자가 reviewers visibility 우려하면 Cat A 유지 + inline `*Errata Round 1 substantive correction; statement remains valid*` note만 추가.
- Critic verdict (Cat A label degradation) 부분 흡수 못하지만 사용자 권한 우선.

---

## §8. Day 4 EOD a posteriori reflection (preview)

Day 4 EOD 시점 `99_summary.md`에서 답해야 하는 질문:

1. **W5 Standard 사다리는 안정적으로 100% 도달했는가?** (Day 4 morning Block 1+3 모두 success인 경우.)
2. **W5 Ambitious 사다리는 어디까지 진척했는가?** (CV-1.5.1 release 발생 → 100%; T-σ-Theorem-4 Cat B 격하 = G6 thermal proxy ~ Cat C → B 격상 substitute.)
3. **W5 Stretch 사다리 도달 확률은?** (Day 4 EOD Paper §4 v2 + CV-1.5.1 + Theorem 4.6.1 promoted → ~65-70%; Day 5-7에 Paper 1 §1-§3 skeleton 작성 시 80%+.)
4. **Day 3-4 cumulative 4 substantive negative results (σ^A K-jump + V5b-F mass + V5b-T' phantom + LSW α λ-dependence)가 publication readiness에 미친 영향?** Document specialist 권고대로 Paper 1/2/3 split이 자연스럽게 정의됐다면 negative results는 narrative depth로 변환 가능. 그러나 reviewer에게는 "4 errors in 2 days"로 보일 위험도 존재 — methodology section에서 self-correction culture를 명시화.
5. **Day 5+ priority 재조정 필요한가?** NQ-244 결과에 따라 §4.5.5가 publishable 또는 deferred로 갈림.
6. **W6 Day 1 priority queue는 확정인가?** NQ-198l 결과 + NQ-244 결과 후 Day 7 EOD에 W6_strategic_plan.md 작성 시 결정.

---

**End of pre_brainstorm.md.** **09:00 Block 0 시작 직후 plan.md로 진입.**
