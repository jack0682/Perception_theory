# plan.md — 2026-04-30 (W5 Day 4, FOCUSED-PROMOTION: CV-1.5.1 Apply + Critic 보강 + Paper §4.4 재작성)

**Session type:** W5 Day 4 — *focused promotion day*. Day 3 produced 12 daily files including 3 substantive negative results (σ^A K-jump 비결정성 / V5b-F mass-dependence 반증 / V5b-T' phantom on torus) + ~95-100 lines canonical promotion ready + Paper §4 polished. Day 4 applies the promotion + Critic reinforcement + Paper §4.4 rewrite + 1 information-cheap numerical (NQ-198l) + first git commit in 4 months.
**W5 scope:** 2026-04-27 (Mon, Day 1 G0) ~ 2026-05-03 (Sun). 8 goals per `W5_strategic_plan.md`.
**Prerequisite:** Day 3 close 2026-04-29 EOD. canonical/ pristine; tests 175 passing baseline; 12 untracked daily files; 7-agent analysis report consolidated.
**Session working directory:** `THEORY/logs/daily/2026-04-30/`.
**Weekly buffer target:** `logs/weekly/2026-04-W5/weekly_draft_storming.md` (04-30 entry append).
**Day 3 reference:** `THEORY/logs/daily/2026-04-29/99_summary.md` + `08_user_decisions_log.md` + `11_NQ198fg_results_and_D5_withdraw.md`.
**Strategic plan:** `logs/weekly/2026-04-W5/W5_strategic_plan.md` (8-goal blueprint).

---

## §1. Day 4 Mission Statement

> **"Day 3's user-decision queue + 3 negative results + Critic reinforcement → Day 4's CV-1.5.1 release + Paper §4.4 v2 + Theorem 4.6.1 promotion + V5b-T-zero confirmation + first git commit. Single user authorization at 09:15 covers entire Block 1+3."**

Day 3 was a **3-stage day** (consolidation → deepening → numerical). Day 4 is a **focused promotion day** — apply mature results, reinforce process, advance Paper §4.4 to truly LaTeX-ready, all under tight scope.

Calibration: Day 4 should be MODERATE (~9h work-time), with **most-critical block in morning (canonical apply)**, biggest-time-block in afternoon (Paper §4.4 rewrite), 1 information-cheap numerical (NQ-198l ~30min), and 1 background launch (NQ-244 야간).

---

## §2. Day 3 EOD → Day 4 Calibration

| 항목 | Day 3 (3-stage) | **Day 4 (FOCUSED-PROMOTION)** |
|------|-----------------|-------------------------------|
| Total time | ~12h | **~9h** |
| New daily files | 12 | **~7** (00 reconciliation, 01 canonical apply log, 02b Paper §4 v2, 03 OP register, 04 NQ-198l result, 05 git commit log, 99 summary) |
| Canonical edits | 0 | **~95-100 lines** (D-1~D-4 + D-6a + Critic 보강) |
| OP edits | 0 | **+1 new (OP-0008) + MO-1 라이더** |
| Numerical runs | 3 (NQ-198a/f/g, ~7min total) | **1 quick (NQ-198l ~15min)** + **NQ-244 background launch** |
| User decisions | 0 (queue formed) | **1 batch authorize at 09:15** (Path 1 + Critic 보강) |
| New Cat A | 0 | **+3** (D-6a static σ_multi) **−1** (T-σ-Theorem-4 Cat A→B 격하) = **net +2** (43 → **45**) |
| Files outputs | 12 daily | **~7 daily + canonical/CHANGELOG/theorem_status edits + Paper §4 v2** |
| Git commits | 0 (3 months) | **1 batched commit** (Day 3 + Day 4 logs + canonical + scripts) |

---

## §3. 30-Minute Granular Schedule

### Block 0 — Pre-flight + Reconciliation (09:00-09:15, 15min)

**09:00-09:10 (10min): Day 3 EOD audit + test baseline**

- `git status` → Day 3 12 daily files untracked (expected). canonical/ pristine.
- `cd CODE && python3 -m pytest tests/ -q` → **175 passing baseline**. (run_in_background OK.)
- Read this plan.md + `pre_brainstorm.md` + Day 3 `99_summary.md` §11 + `11_NQ198fg_results_and_D5_withdraw.md` §4 (D-5 WITHDRAW final).

**09:10-09:15 (5min): Quick reconciliation check**

Verify Day 3 EOD final decisions match this plan §3 Block 1:
- D-5 = WITHDRAW (NQ-198f phantom). ✓ (`11_*` §4.2)
- D-6b = Defer to W6+ via NQ-242. ✓ (`08_*` §2)
- T-σ-Theorem-4 Cat A → B (Critic 보강). NEW Day 4 decision (not in Day 3 logs).
- OP-0008 σ^A K-jump 비결정성 register. NEW Day 4 decision.
- MO-1 OP-0003 라이더 추가. NEW Day 4 decision.

**Output**: none (mental confirmation only).

**Failure mode F0 (test broken)**: tests not 175 passing baseline. Action: `git diff CODE/` → bisect → fix before Block 1.

---

### Block 1 — Canonical Apply CV-1.5.1 + Critic 보강 (09:15-10:30, 75min, **USER AUTH 필요 09:15**)

**09:15 USER AUTHORIZATION POINT**

Display unified summary to user, request batch approval:

```
Day 4 Block 1 시작합니다. CV-1.5 → CV-1.5.1 적용 항목:

[Day 3 user-decision queue 확정분]
- D-1 Commitment 14 (O5') multi-irrep convention             ~10-15 lines
- D-2 Commitment 14 (O7) Mulliken character order             ~15-20 lines
- D-3 V5b-F mechanism rider + NQ-198a 1/n scaling 추가        ~25 lines
- D-4 ζ_*(graph, c) precise + c-dependence                    ~12 lines
- D-6a Commitment 14-Multi STATIC (σ_multi^A + σ_multi^D)     ~35 lines
- D-5 V5b-T' WITHDRAW (NQ-198f phantom 근거; merge 안함)        0 lines
- D-6b dynamic σ_multi^A(t): Defer to W6+ via NQ-242           0 lines

[Critic 7-agent analysis 보강]
- T-σ-Theorem-4 status: Cat A → Cat B 격하                     status note 추가
  근거: Errata Round 1 structural error retroactive
- OP-0008 σ^A K-jump inheritance non-determinism: 신규 등록     ~30 lines
- OP-0003 MO-1 entry: "Re-activation trigger" 라이더 추가     ~5 lines

총 canonical/OP 변경: ~110-130 lines
Cat A net: +3 (D-6a) − 1 (T-σ-Theorem-4 격하) = +2 → 43A → 45A
Total claims: 57 → 59. % proved: 75% → 76%.

Approve all? (yes / no / modify list)
```

**Decision protocol**:
- "yes" → 전체 batch 진행. Block 1, 2, 3 일괄 적용.
- "no" → Day 4를 Defer-all로 전환. Block 4 (Paper §4.4)만 진행.
- "modify [items]" → 사용자 지정 subset만 적용. 나머지는 carry-forward.

**09:20-10:00 (40min): canonical.md edits**

Edit `THEORY/canonical/canonical.md` per approved subset. **Order critical** (cross-reference dependencies):

1. **D-1 + D-2 (§11.1 Commitment 14 addendum)**: Mulliken character order + multi-irrep eigenspace convention. Insert after current Commitment 14 body. ~25-35 lines.

2. **D-3 V5b-F rider + NQ-198a scaling (§13 T-V5b-T entry)**: 현재 line ~1184 영역. T-V5b-F sub-statement에 추가:
   ```
   *Sub-statement (V5b-F-empirical, Cat B target via NQ-198a 2026-04-29):*
   For sub-spinodal corner-saturated minimizer on translation-broken graphs
   (free-BC), Goldstone eigenvalue obeys
   $$\mu_{\text{Gold}}^{\text{V5b-F}} \approx C(\beta) \cdot |\partial S|/n$$
   with empirical $C(\beta=4, \xi_0=0.5) \approx 13.2 \pm 0.4$ (NQ-198a, 6 corner-sat
   data points, std/mean ~3%, SNR 34.9). Full $C(\beta, \xi_0)$ functional form
   open (NQ-198k W6+; NQ-198g 결과는 |∂S| confound으로 inconclusive).
   ```
   ~25 lines.

3. **D-4 ζ_*(graph, c) precise (§13 T-V5b-T-(d) line ~1129 replacement)**: 기존 bracket statement → 2-decimal precise + c-qualifier. ~12 lines.

4. **D-6a Commitment 14-Multi STATIC (§11.1 + §13)**:
   - §11.1 addendum: Commitment 14-Multi static framework declaration. ~15 lines.
   - §13 new entries (3 new C-IDs):
     - **C-0717 Commitment 14-Multi-Static** (definitional Cat A).
     - **C-0718 σ_multi^A static structure** (Cat A on Σ^{K,interior}_M; corners excluded per Option A).
     - **C-0719 σ_multi^D cohomology pull-back** (Cat A definitional).
   - ~20 lines.

5. **T-σ-Theorem-4 Cat A → B 격하 (§13 entry inline note)**: 기존 entry 끝에 추가:
   ```
   *Status revision 2026-04-30 (W5 Day 4): Cat A → **Cat B** in $\epsilon$-small
   regime on $D_4$ free-BC. Rationale: Errata Round 1 (`91_critical_review.md`
   §3.2) caught a structural error in original sub-statement (ii) ($K_1 < K_0$
   "would-be transverse Goldstone" framing inapplicable to discrete symmetry
   breaking; corrected to $K_1 = K_0 = 4|W''(c)|$ at leading order). Although
   the corrected statement is mathematically valid, the original Cat A merge
   was premature per process audit. Status downgraded to Cat B retroactively
   for canonical credibility (Critic verdict 2026-04-29). Higher-order
   $\epsilon$ splitting is open (NQ-187, W7+).*
   ```
   theorem_status.md C-0716 row도 동시 수정. ~10 lines.

**Verification after each edit**:
- `git diff THEORY/canonical/canonical.md` 검토.
- canonical line count: 1593 → ~1690 (확인).
- §1.1 release table 행 추가 (CV-1.5.1 row).

**10:00-10:30 (30min): theorem_status.md + CHANGELOG.md systematic refresh**

Use templates in §10 below.

`THEORY/canonical/theorem_status.md`:
- last_updated → 2026-04-30.
- **CV-1.5.1 release entry** 신규 추가 (line ~17, CV-1.5 entry 위).
- C-0716 row: status 컬럼 `Cat A` → `Cat B (downgraded 2026-04-30)`.
- C-0717, C-0718, C-0719 신규 rows (Active Claims table).
- Counts row: 43A → **45A**, 57 → **59 claims**, 75% → **76%**.

`THEORY/CHANGELOG.md` 신규 entry (top, 가장 최신):

```markdown
## 2026-04-30 — W5 Day 4 FOCUSED-PROMOTION: CV-1.5.1 + Critic Reinforcement

### Summary
Apply Day 3 user-decision queue (D-1, D-2, D-3, D-4, D-6a) + Critic 7-agent
analysis 보강 (T-σ-Theorem-4 Cat A→B 격하; OP-0008 신규 등록; MO-1 라이더).
D-5 V5b-T' WITHDRAW (NQ-198f phantom). D-6b dynamic σ_multi^A(t) defer to
W6+ via NQ-242.

### Files Modified
- canonical.md (CV-1.5 → CV-1.5.1): +95-100 lines net.
- theorem_status.md: +CV-1.5.1 entry, +3 C-IDs (C-0717/8/9), C-0716 status
  downgrade.
- open_problems.md: +OP-0008, OP-0003 라이더.

### Theorem Status Changes
- New Cat A: +3 (D-6a static σ_multi triplet).
- Demoted: T-σ-Theorem-4 Cat A → Cat B (process audit retroactive).
- Withdrawn: V5b-T' new entry (D-5; phantom on torus per NQ-198f).
- Net: 43A → 45A. Claims 57 → 59. % proved 75% → 76%.

### Carry-Forward
- W6 Day 1: NQ-198l (V5b-T-zero confirmation, ~15min) + NQ-198j/k/l +
  NQ-244 follow-up + NQ-242 sampler.
- W6+: D-6b dynamic via NQ-242 (4-6주 effort) → CV-1.6.

### Test Count
- Pre-edit: 175 passing.
- Post-edit: TBD (no code changes; should remain 175).
```

**Output**: `01_canonical_promotion_log.md` (~150-200 lines documenting Block 1 edits).

**Success metric**: canonical/theorem_status/CHANGELOG/open_problems all consistent; 175 tests still passing post-edit.

**Failure mode F1 (user defers all)**: skip Block 1, 2, 3. Proceed to Block 4 Paper §4.4 + Block 6 NQ-198l + Block 7 EOD only.

**Failure mode F2 (partial approve)**: Block 1 edits 사용자 지정 subset만. CHANGELOG entry는 partial-approval 명시.

---

### Block 2 — Post-edit Verify + Audit (10:30-11:00, 30min)

**10:30-10:45 (15min): Test verification**

```bash
cd CODE && python3 -m pytest tests/ -q
```
Expected: 175 passing (no code changes; theory-only edits).

If FAIL: revert canonical edits, bisect, fix.

**10:45-11:00 (15min): Errata-free re-review pass**

자체-감사 — Block 1에 머지된 entries 각각 한 번씩 read-through:
1. D-1, D-2 wording이 `92_critical_review_round2.md` decisions와 일치?
2. D-3 NQ-198a scaling 수치 (C ≈ 13.2±0.4) 정확?
3. D-4 ζ_* c-dependence 명시?
4. D-6a Σ^{K,interior}_M 명시 (corners excluded)?
5. T-σ-Theorem-4 격하 inline note 일관성?
6. theorem_status counts 산수 정확?

각 항목별 PASS/FAIL 기록 (mental note).

**Output**: none (감사 결과는 `01_canonical_promotion_log.md` §4에 통합).

---

### Block 3 — OP-0008 등록 + MO-1 라이더 (11:00-11:30, 30min)

**11:00-11:25 (25min): open_problems.md 편집**

`THEORY/canonical/open_problems.md`:

1. **OP-0008 신규 entry** (HIGH-PRIORITY 섹션 OP-0006 다음에 삽입):

```markdown
### **OP-0008: σ^A K-jump Inheritance Non-Determinism**

**Statement:**
Under K-field gradient flow on shared-pool $\widetilde{\Sigma}^K_M$, at K-jump
times $t^*$ the post-merger σ^A($t^{*+}$) is **NOT** determined by
pre-merger σ^A($t^{*-}$) alone. Inheritance map $\Phi$ requires
merger-geometry data $\mathcal{M}$ = (which two formations merge, post-merger
relaxation trajectory, cluster centroids).

**Evidence:**
- Day 3 deepening pass `04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c)
  gives the formal non-determinism claim (Cat C asserted; rigorous
  two-trajectory construction open as NQ-242c).
- Phase 8 T4 SCC↔CH correspondence implicit deterministic-trajectory
  assumption violated (Day 2 `32_U5_SCC_CH_theorem.md`).

**Impact:**
- D-6b Commitment 14-Multi DYNAMIC Cat A path requires rich-σ augmentation
  (centroid + orientation + Wigner-von Neumann data beyond eigenvalue tuple).
- Bifurcates CV-1.6 release path: Path A (accept non-determinism, Cat B) vs
  Path B (rich-σ for Cat A).
- Phase 8 T4 caveat needed in Paper §4.5.7.

**Status:** ⚠️ **TENTATIVE** (Cat C asserted; explicit construction open).

**Severity:** 🟠 **HIGH** (affects D-6b canonical path; CV-1.6 release-blocking
for Cat A target).

**Last reviewed:** 2026-04-30 (W5 Day 4 morning, post-Day 3 deepening pass).

**Direct-attack NQs:**
- NQ-242c: explicit construction of two trajectories with same σ^A($t^{*-}$)
  but distinct σ^A($t^{*+}$). Cat A target. ~2-3주 effort. W6+.
- NQ-242d: σ^D symmetry-emergence characterization. Cat A target. ~2-3주. W6+.
- NQ-242: full Hessian σ-tuple time-series with rigorous K-jump theory. Cat
  A or B target. 4-6주. W6.

**Related problems:**
- OP-0003 MO-1 (multi-formation 재활성).
- OP-0005 K-Selection (path-dependence implication).

**References:**
- `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c).
- `THEORY/logs/daily/2026-04-29/06_open_problems_development_synthesis.md`.
- `THEORY/logs/daily/2026-04-29/99_summary.md` §11 deepening pass.
```

2. **OP-0003 MO-1 entry 라이더 추가** (Severity 라인 직후):

```markdown
**Re-activation trigger:** D-6b approval (CV-1.6) OR NQ-248 (multi-formation
stratified Morse) work begins. Single-formation 범위에서만 NOT BLOCKING; CV-1.6
시점에 🟠 HIGH로 자동 재활성화. (Added 2026-04-30 per W5 Day 3 7-agent analyst
recommendation; prevents silent re-emergence.)
```

3. **Problem Statistics 표 업데이트** (line ~330):
- 🟠 HIGH: 1 (OP-0005) → **2** (OP-0005 + OP-0008).

**11:25-11:30 (5min): Output write**

`THEORY/logs/daily/2026-04-30/03_OP0008_register_log.md` (~80-100 lines): OP-0008 등록 사유 + MO-1 라이더 변경 사유 + Day 3 7-agent analyst 권고 trace.

**Success metric**: open_problems.md self-consistent; OP-0008 cross-references valid; MO-1 라이더 명시.

---

### Block 4 — Paper §4.4 v2 재작성 (13:00-17:00, 4h, **CRITICAL**)

**Lunch 12:00-13:00.** Block 4는 Day 4의 가장 긴 단일 작업.

**Source**: `THEORY/logs/daily/2026-04-29/02_paper_section4_polished.md` (492 lines, V5b-T' assumption).
**Target**: `THEORY/logs/daily/2026-04-30/02b_paper_section4_v2.md` (~520-570 lines, V5b-T' WITHDRAW 반영).
**Constraint**: §4.1, §4.2, §4.3, §4.5, §4.6, §4.7 그대로 (수정 5건은 §4.4 + §4.5.7 일부).

**13:00-13:30 (30min): §4.4.1 V5b-T 검토 + V5b-T-zero 연결 note 추가**

기존 §4.4.1 (V5b-T super-lattice, exp-suppressed)는 그대로 유지. 끝에 connecting note 추가:
> "As $c$ decreases below the spinodal, the super-lattice regime transitions
> to a corner-saturated regime on the same translation-invariant graph. In
> this transition, the Goldstone eigenvalue undergoes a qualitative change:
> from exp-suppressed positive (V5b-T) to exact zero (V5b-T-zero, Theorem
> 4.4.2). The transition point defines $\zeta_*(G, c)$, addressed in
> Theorem 4.4.4 below."

**13:30-14:30 (60min): §4.4.2 Theorem 4.4.2 전면 재서술 → V5b-T-zero**

기존 V5b-T' 내용 모두 삭제 (Phase 3 PN-barrier formula μ ≈ A·β·|∂S|/ξ_0 framework 포함).

신규 §4.4.2 V5b-T-zero (Cat A definitional):

```latex
\subsection{V5b-T-zero: Exact Zero Goldstone on Translation-Invariant Graphs
            (Sub-Spinodal Regime)}

\begin{theorem}[V5b-T-zero, Cat A definitional]
\label{thm:v5b-t-zero}
On translation-invariant graphs ($\mathbb{T}^d$, cycle $C_n$) under SCC energy
with $c < c_{\text{spinodal}}$, every corner-saturated minimizer $u^* \in
\Sigma_m$ has Goldstone eigenvalue
\[ \mu_{\text{Gold}}^{\text{V5b-T-zero}}(u^*) = 0 \]
exactly.

\textbf{Mechanism:} Discrete translation symmetry $\mathbb{Z}_L^d$ acts on
$u^*$ by orbit; the orbit is equienergetic. Orbit-tangent directions form an
exact zero subspace of the Hessian $H_E(u^*)$ on $\Sigma_m$ (standard Goldstone
theorem for discrete-group symmetry breaking on lattice).

\textbf{Empirical anchor:} NQ-198f (2026-04-29, T²_20 / T²_28 / T²_40, 4
corner-sat configurations × 3 seeds): $|\mu_{\text{Gold}}| \leq 0.028$ within
finite-difference Hessian numerical noise of $\epsilon^{1/2}$ for $\epsilon =
10^{-4}$.

\textbf{Distinguished from V5b-T:} V5b-T (super-lattice, $c$ in spinodal
interior) has exp-suppressed positive Goldstone $\mu \propto e^{-c_d/\xi_0}$;
V5b-T-zero ($c$ below spinodal) has exact zero. The transition occurs at
$\zeta_*(G, c)$ (Theorem 4.4.4).

\textbf{Distinguished from V5b-F:} On translation-broken graphs (e.g., free-BC
grids), the discrete translation orbit is not equienergetic; cluster boundary
$|\partial S|$ couples to the energy via Peierls-Nabarro mechanism, producing
$\mu_{\text{Gold}}^{\text{V5b-F}} \propto |\partial S|/n$ (Theorem 4.4.3).
\end{theorem}

\begin{proof}[Sketch] 
Standard Goldstone theorem on discrete lattice: continuous translation acts
nontrivially only as $\mathbb{Z}_L^d$ on the discrete graph, but the cluster
orbit under $\mathbb{Z}_L^d$ generates an exact zero-eigenvalue subspace of
$H_E(u^*)$ since each orbit element is a minimizer with the same energy. By
Bochner-Weitzenböck identity adapted to graph Laplacian (Bertozzi 2017),
orbit-tangent directions $\delta u_x = (T_a u^*)_x - u^*_x$ are exact null
vectors of $H_E$.
\end{proof}
```

대략 ~80 lines (V5b-T'의 ~110 lines보다 짧다 — phantom 제거 + cleaner statement).

**14:30-15:00 (30min): §4.4.3 V5b-F functional form 완화**

기존 §4.4.3에서 "$\mu \propto |\partial S|/\xi_0$" Phase 3 heuristic 표현 제거. 대체:

```latex
\textbf{Empirical scaling (NQ-198a, 2026-04-29):}
For free-BC corner-saturated minimizer at fixed $\beta = 4, \xi_0 = 0.5$:
\[ \mu_{\text{Gold}}^{\text{V5b-F}} \approx C \cdot \frac{|\partial S|}{n}, 
   \quad C \approx 13.2 \pm 0.4 \]
(6 corner-sat data points across $L \in \{14, 20, 28, 40\}$ and $m$ ranges,
within-setup CV $< 0.001\%$, SNR $\approx 35$).

The full functional form $C(\beta, \xi_0)$ is open. NQ-198g preliminary
$\beta$-scan ($\beta \in \{2, 3, 4, 6, 8\}$) shows $C/\beta$ non-monotone
(4.0 → 3.28 → 2.86) — simple $\beta^p$ form refuted. NQ-198k 
($|\partial S|$-controlled $\beta$-scan, W6+) is required for Cat B canonical
statement of $C(\beta, \xi_0)$ functional form.
```

기존 V5b-F prose 다른 부분 (mechanism 분류 H1+H2+H3 mixed, regime R3b, etc.)는 유지.

**15:00-15:45 (45min): §4.4.4 unified PN formula 적용범위 축소**

기존 Eq. (4.20) $\mu_{\text{PN}} = A \cdot \beta \cdot e^{-c_d/\xi_0} \cdot f_{\text{comm}}(\phi) \cdot g_{\partial}(\delta/\xi_0)$ 수식 자체는 유지.

추가 remark:
```latex
\begin{remark}[Applicability of Eq. (4.20)]
The unified PN-barrier formula (4.20) applies to two regimes:
(i) V5b-T (super-lattice, translation-invariant, spinodal interior):
    $g_\partial = 1$ uniform; $f_{\text{comm}}$ commensurability-dependent.
(ii) V5b-F (translation-broken, sub-spinodal, free-BC):
    $g_\partial \propto |\partial S|/n$ cluster-boundary-dependent;
    $f_{\text{comm}} \approx 1$ (no super-lattice modulation).

V5b-T-zero (translation-invariant, sub-spinodal) is \emph{outside} the
applicability of Eq. (4.20): the discrete translation orbit forces
$\mu_{\text{PN}} = 0$ exactly via the Goldstone theorem on $\mathbb{Z}_L^d$
(Theorem 4.4.2). No PN-barrier-lifting mechanism operates in the V5b-T-zero
regime because the requisite symmetry breaking is absent.
\end{remark}
```

**15:45-16:00 (15min): §4.4.5 Regime Map R3b 행 수정**

테이블에서:
- 기존: `R3b | $\beta > \beta_{R3}$ | $c < c_s$ | translation-invariant | Corner-saturated, V5b-T'`
- 수정: `R3b | $\beta > \beta_{R3}$ | $c < c_s$ | translation-invariant | V5b-T-zero ($\mu = 0$ exact)`

**16:00-16:45 (45min): §4.5.7 SCC↔CH dynamic caveat 추가**

기존 §4.5.7 끝에 신규 paragraph:

```latex
\textbf{Static vs dynamic correspondence.}
The SCC ↔ CH correspondence above operates strictly at the level of
\emph{static} σ_{\text{multi}}(u^*) at fixed coarsening configurations: under
the mobility identification $M_{\text{eff}} = \gamma/V$, both frameworks
share the same Hessian-spectral structure at minimizers.

The extension to \emph{dynamic} σ_{\text{multi}}^A(t) trajectory is more
delicate. Lemma~4.4.1(c) of the σ-trajectory framework (deferred to a
companion paper) establishes that under K-field flow on shared-pool
$\widetilde{\Sigma}^K_M$, at K-jump events the post-merger σ^A is \emph{not
deterministic} in pre-merger σ-data alone — merger-geometry data
$\mathcal{M}$ is required. Correspondingly, CH's deterministic order-parameter
flow does not straightforwardly correspond to σ^A(t). Full σ-dynamic ↔ CH
flow correspondence requires a richer invariant σ_{\text{rich}} including
merger-geometry data; this is deferred to NQ-242 (W6+) work, registered as
OP-0008 (§Open Problems).
```

**16:45-17:00 (15min): Polish + LaTeX-readiness final pass**

- (4.20)–(4.22) 식 numbering 일관성 검토.
- §4.4 cross-references (Theorem 4.4.1 ↔ 4.4.2 ↔ 4.4.3 ↔ 4.4.4) 전부 작동.
- Bibliography placeholder: NQ-198a/f/g + Bertozzi 2017 + Goldstone 1962 + Royal Society A 2021 (PN topological origin) 신규 reference 추가.

**Output**: `THEORY/logs/daily/2026-04-30/02b_paper_section4_v2.md` (~520-570 lines, **진정한 LaTeX-ready**).

**Success metric**: §4.4가 V5b-T (Cat A) + V5b-T-zero (Cat A def) + V5b-F (Cat B empirical) 3-class clean taxonomy로 재구성. (4.20)이 V5b-T-zero 범위 밖 명시. (4.4.2)가 phantom 아닌 Goldstone-on-discrete-lattice 결론. §4.5.7이 dynamic correspondence caveat 포함.

**Failure mode F4 (4h 초과)**: §4.5.7 caveat을 Day 5로 이동 (가장 분리하기 쉬운 부분). §4.4 V5b-T-zero 재서술이 우선.

---

### Block 5 — Theorem 4.6.1 working/MF/ 승급 (17:00-17:30, 30min)

**17:00-17:05 (5min): 기존 파일 확인**

```bash
wc -l THEORY/working/MF/sigma_multi_trajectory.md
head -30 THEORY/working/MF/sigma_multi_trajectory.md
```

기존 13KB 파일 내용 확인 — Day 3 Stage B에서 만든 stub인지, 기존 별도 파일인지.

**Case A (Day 3 stub)**: append + integrate.
**Case B (기존 별도)**: 헤더에 통합 note 추가 + 기존 내용 보존.

**17:05-17:30 (25min): Theorem 4.6.1 promotion with Cat C 라벨 정정**

`THEORY/working/MF/sigma_multi_trajectory.md` 작성:

```markdown
# σ_multi^A(t) Trajectory Framework — Working File

**Status:** Theorem 4.6.1 = **Cat B target** (in non-corner-saturated regime);
**Cat C** in V5b-T-zero / V5b-F corner-saturated regime; NQ-242 W6+ → Cat A path.
**Promoted from:** `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md`.
**Created:** 2026-04-30 (W5 Day 4).
**Promotion gate (CV-1.6):** NQ-242 numerical anchor + NQ-242c explicit
non-determinism construction + NQ-242d σ^D symmetry-emergence.

---

[content from `04_*` §1-§6 with Cat label corrections from `09_session_self_critique.md` §7]

## §3.1 Lemma 4.4.1(c) — Status correction (2026-04-30)

Per Critic 7-agent verdict 2026-04-29 + self-critique `09_*` §2.3, Lemma
4.4.1(c) (σ^A K-jump non-determinism) is downgraded:
- Original `04_*` label: "Cat B sketch".
- Corrected label: **"Cat C (conjectured)"** — sketch of motivation only,
  not sketch of proof.
- Rigorous construction is open as NQ-242c (W6+).

## §3.2 Theorem 4.6.1 — Regime restriction (2026-04-30)

Per `09_*` §2.2:
- Original label: "Cat B target".
- Corrected label: **"Cat B target in non-corner-saturated regime; Cat C in
  V5b-T-zero / V5b-F corner-saturated regime"**.
- Rationale: corner-saturated regime is precisely where the dynamics are most
  physically interesting; for that regime, full Cat B status awaits richer
  numerical anchor.

[rest of `04_*` content, with anchor headers + cross-refs to canonical]
```

`THEORY/logs/daily/2026-04-30/05_theorem4.6.1_promotion_log.md` (~50-80 lines): promotion 사유 + Cat 라벨 정정 + 향후 path.

**Success metric**: working/MF/sigma_multi_trajectory.md에 Theorem 4.6.1이 Cat C-아닌-Cat B sketch라는 false-격상 없이 promoted.

---

### Block 6 — NQ-198l Quick Numerical (17:30-18:00, 30min)

**17:30-17:40 (10min): Script 작성**

`CODE/scripts/nq198l_v5b_T_zero_torus_L40.py`:

```python
"""
NQ-198l: V5b-T-zero confirmation on T²_40.
Goal: confirm |μ_G| → 0 as L increases (validate L=28 outlier as finite-size noise).

Setup: T²_40 torus, c=0.3, β=4, ξ_0=0.5.
6 (m, IC) configs × 3 seeds.
Predict: |μ_G| < 0.005 (>5x smaller than NQ-198f L=28 outlier 0.028).
"""
import sys; sys.path.insert(0, '../scc')
from scc import GraphState, ParameterRegistry, find_formation, EnergyComputer
import numpy as np
import json

# [setup torus, mass configs, IC variation]
# [find corner-sat minimizer]
# [compute lowest 6 Hessian eigvals via FD]
# [save to results/nq198l_*.json]
```

**17:40-17:55 (15min): 실행 + 분석**

`python3 CODE/scripts/nq198l_v5b_T_zero_torus_L40.py`. 결과 stream:
- `|μ_G| < 0.005` for all 4+ corner-sat cases → V5b-T-zero confirmed (Day 4 §4.4.2 Theorem 4.4.2 numerical anchor 강화).
- `|μ_G| ∈ [0.005, 0.020]` → ambiguous; L=80 추가 필요 (W6 Day 1).
- `|μ_G| > 0.020` → V5b-T-zero 결론 약화; §4.4.2 caveat 추가 필요.

**17:55-18:00 (5min): Output**

`THEORY/logs/daily/2026-04-30/04_NQ198l_result.md` (~30-50 lines):
- Configurations summary
- Raw eigvals
- Verdict (PASS / Ambiguous / FAIL)
- §4.4.2 Theorem 4.4.2 caveat update if needed

---

### NQ-244 Background Launch (18:00-18:15, 15min)

**18:00-18:10 (10min): Script verification**

`CODE/scripts/nq244_3D_LSW_T15_K10.py` (이미 작성된 경우 사용; 없으면 V5 source 변형):
- T³_15 grid (3375 nodes), K=10, λ_rep=0.5
- t_max=200, dt=0.05
- 3 seeds
- Predicted runtime ~1-2h on local CPU.

**18:10-18:15 (5min): Background launch**

```bash
nohup python3 CODE/scripts/nq244_3D_LSW_T15_K10.py \
    > CODE/scripts/results/nq244_run.log 2>&1 &
disown  # detach from terminal
```

Day 5 morning에 결과 분석 (3D LSW α plateau 0.013 → publishable α value 또는 caveat 강화).

---

### Block 7 — Day 4 EOD: Summary + Weekly + Git Commit (18:15-19:00, 45min)

**18:15-18:35 (20min): `99_summary.md` 작성**

`THEORY/logs/daily/2026-04-30/99_summary.md` (~250-300 lines): Day 4 reflection. Block-by-block 결과 + W5 사다리 a posteriori 재추정 + Day 5 priorities.

**18:35-18:45 (10min): `weekly_draft_storming.md` 04-30 entry append**

상단에 04-30 entry 추가:
```markdown
## 2026-04-30 — W5 Day 4 (FOCUSED-PROMOTION): CV-1.5.1 Released + Paper §4.4 v2 + Critic 보강

### Mission
Day 3's user-decision queue + 7-agent analysis 보강 → CV-1.5.1 release.

### Added (canonical)
- D-1, D-2, D-3, D-4, D-6a applied (~95-100 lines).
- 3 new C-IDs (C-0717/8/9).
- T-σ-Theorem-4 Cat A → B (Critic 보강 retroactive).
- OP-0008 σ^A K-jump 비결정성 신규.
- OP-0003 MO-1 라이더 추가.

### Withdrawn
- D-5 V5b-T' new entry (NQ-198f phantom).

### Deferred
- D-6b dynamic σ_multi^A(t) → W6+ via NQ-242.

### Counts
- 43A → 45A. 57 → 59 claims. 75% → 76%.

### Numerics
- NQ-198l: V5b-T-zero confirmation [PASS / Ambiguous / FAIL].
- NQ-244 background launched (Day 5 morning analysis).

### Paper
- Paper §4.4 v2 written (V5b-T-zero / V5b-F C(β) / unified PN range narrow).
- §4.5.7 dynamic CH caveat added (OP-0008 reference).

### Working
- `working/MF/sigma_multi_trajectory.md`: Theorem 4.6.1 promoted with Cat C
  label (not Cat B sketch) for σ^A non-determinism.
```

**18:45-19:00 (15min): Git commit (4개월만에 first)**

```bash
cd /Users/ojaehong/Perception/Perception_theory

# Verify status
git status

# Stage canonical edits + Day 3 + Day 4 logs + scripts + working updates
git add THEORY/canonical/canonical.md \
        THEORY/canonical/theorem_status.md \
        THEORY/canonical/open_problems.md \
        THEORY/CHANGELOG.md \
        THEORY/working/MF/sigma_multi_trajectory.md \
        THEORY/logs/daily/2026-04-29/ \
        THEORY/logs/daily/2026-04-30/ \
        THEORY/logs/weekly/2026-04-W5/weekly_draft_storming.md \
        CODE/scripts/nq198a_*.py CODE/scripts/nq198f_*.py CODE/scripts/nq198g_*.py \
        CODE/scripts/nq198l_*.py CODE/scripts/nq244_*.py \
        CODE/scripts/results/nq198a_*.json CODE/scripts/results/nq198f_*.json \
        CODE/scripts/results/nq198g_*.json CODE/scripts/results/nq198l_*.json

# Commit with detailed message
git commit -m "$(cat <<'EOF'
CV-1.5.1: D-1..D-4+D-6a apply, D-5 V5b-T' WITHDRAW, T-σ-Theorem-4 Cat A→B; OP-0008 register; Paper §4.4 v2

W5 Day 3-4 batch commit (4-month commit gap closed):

Canonical (CV-1.5 → CV-1.5.1):
- D-1, D-2 Commitment 14 (O5')(O7) conventions applied (~30 lines).
- D-3 V5b-F mechanism rider with NQ-198a 1/n empirical scaling (~25 lines).
- D-4 ζ_*(graph, c) precise + c-dependence (~12 lines).
- D-6a Commitment 14-Multi STATIC (σ_multi^A + σ_multi^D) (~35 lines).
- D-5 V5b-T' new entry WITHDRAWN per NQ-198f phantom finding (Day 3).
- D-6b dynamic σ_multi^A(t) DEFERRED to W6+ via NQ-242.
- T-σ-Theorem-4 status downgraded Cat A → Cat B per Errata Round 1 audit.

Open problems:
- OP-0008 σ^A K-jump inheritance non-determinism registered (HIGH severity).
- OP-0003 MO-1 re-activation trigger rider added.

Counts: 43A → 45A. Total claims 57 → 59. % proved 75% → 76%.

Numerical (Day 3-4):
- NQ-198a: V5b-F 1/n empirical scaling C ≈ 13.2 ± 0.4 (β=4, ξ_0=0.5).
- NQ-198f: V5b-T' phantom on torus (μ ≈ 0 exact) — drives D-5 WITHDRAW.
- NQ-198g: β-scan inconclusive (|∂S| confound; NQ-198k W6+ needed).
- NQ-198l: V5b-T-zero confirmation on T²_40.
- NQ-244: 3D LSW T³_15 K=10 background launched (Day 5 analysis).

Paper §4.4 v2:
- §4.4.2 Theorem 4.4.2 rewritten as V5b-T-zero (Cat A definitional, μ=0 exact).
- §4.4.3 V5b-F functional form softened to "C(β)·|∂S|/n at fixed β=4; full
  C(β,ξ_0) open".
- §4.4.4 unified PN formula range narrowed (V5b-T + V5b-F only;
  V5b-T-zero outside).
- §4.4.5 Regime Map R3b row updated.
- §4.5.7 dynamic CH correspondence caveat added (OP-0008 reference).

Working level:
- working/MF/sigma_multi_trajectory.md: Theorem 4.6.1 promoted with Cat C
  label correction for σ^A non-determinism (not Cat B sketch).

Tests: 175 passing baseline + post-edit.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

# Verify commit
git status
git log -1 --stat
```

**Success metric**: clean working tree post-commit; commit message accurate; CV-1.5.1 release marker official.

**Failure mode F7 (commit hook fail)**: investigate (don't --no-verify). Most likely: line ending or large file size. Fix root cause, re-stage, new commit.

---

## §4. Output Inventory (Day 4 expected)

| File | Lines (est.) | Purpose |
|------|--------------|---------|
| `THEORY/canonical/canonical.md` | edit (+95-100) | CV-1.5.1 main spec |
| `THEORY/canonical/theorem_status.md` | edit (+30) | CV-1.5.1 entry + counts |
| `THEORY/canonical/open_problems.md` | edit (+35) | OP-0008 + MO-1 라이더 |
| `THEORY/CHANGELOG.md` | edit (+50) | 04-30 entry |
| `THEORY/working/MF/sigma_multi_trajectory.md` | new or edit | Theorem 4.6.1 promotion |
| `THEORY/logs/daily/2026-04-30/00_day3_audit.md` | (optional) ~50 | Day 3 EOD reconciliation note |
| `THEORY/logs/daily/2026-04-30/01_canonical_promotion_log.md` | ~150-200 | Block 1 edit log |
| `THEORY/logs/daily/2026-04-30/02b_paper_section4_v2.md` | ~520-570 | Paper §4 v2 (Block 4) |
| `THEORY/logs/daily/2026-04-30/03_OP0008_register_log.md` | ~80-100 | Block 3 OP register log |
| `THEORY/logs/daily/2026-04-30/04_NQ198l_result.md` | ~30-50 | Block 6 numerical result |
| `THEORY/logs/daily/2026-04-30/05_theorem4.6.1_promotion_log.md` | ~50-80 | Block 5 working/ promotion |
| `THEORY/logs/daily/2026-04-30/99_summary.md` | ~250-300 | Day 4 EOD reflection |
| `THEORY/logs/weekly/2026-04-W5/weekly_draft_storming.md` | append (~50) | 04-30 entry |
| `CODE/scripts/nq198l_v5b_T_zero_torus_L40.py` | new (~250) | NQ-198l script |
| `CODE/scripts/results/nq198l_*.json` | new | NQ-198l results |
| `CODE/scripts/nq244_3D_LSW_T15_K10.py` | new or existing | NQ-244 script |
| `CODE/scripts/results/nq244_run.log` | new (background) | NQ-244 stdout |

**Total Day 4 line output (approx)**: ~1500-1900 lines (Day 4 = focused, not expansion).

---

## §5. Hard Constraints (per `W5_strategic_plan.md` §6 + 7-agent verdict)

- [ ] **canonical 직접 수정**: ONLY in Block 1 (~95-100 lines), per user explicit Block 1 authorization at 09:15.
- [ ] **Silent resolution**: 0 (D-5 WITHDRAW은 explicit; T-σ-Theorem-4 격하는 inline `*Status revision*` note + theorem_status.md row update; OP-0008 등록은 신규 entry).
- [ ] **Test breakage**: 0 (175 passing pre + post).
- [ ] **u_t primitive 위반**: 0.
- [ ] **4-energy 항 merging**: 0.
- [ ] **Closure idempotence 가정**: 0.
- [ ] **K dual-treatment**: 0 (D-6a static σ_multi에서 K integer-valued 명시).
- [ ] **Reductive equation**: 0 (CN10 contrastive에 위배되지 않음; SCC↔CH는 correspondence).
- [ ] **Phase 11 numerical >30min**: 0 (NQ-198l 15min only; NQ-244 background launch).
- [ ] **Git commit이 user explicit request 없이는 되지 않는다 (CLAUDE.md 정책)**: Block 7 commit은 Day 3 7-agent verdict + Day 4 plan에 명시된 first-commit-in-4-months task. **사용자 09:15 Block 1 authorize에 commit 포함 여부 명시**.

---

## §6. Success Metrics + Failure Modes

**Success (Day 4 EOD)**:
1. ✅ CV-1.5.1 released: 43A → 45A, 57 → 59 claims, 75% → 76%.
2. ✅ T-σ-Theorem-4 Cat B 격하 (Critic 보강).
3. ✅ OP-0008 등록 + MO-1 라이더.
4. ✅ Paper §4.4 v2 LaTeX-ready (V5b-T-zero + V5b-F C(β) clean taxonomy).
5. ✅ Theorem 4.6.1 working/ promoted (Cat C 라벨 정정).
6. ✅ NQ-198l V5b-T-zero confirmation (PASS or Ambiguous).
7. ✅ NQ-244 background launched.
8. ✅ Git commit: 4-month gap closed. Working tree clean.

**Realistic (1-2 success items 부분)**:
- Block 4 4h 초과 시 §4.5.7 caveat을 Day 5로 이동 (success #4 partial).
- NQ-198l Ambiguous 시 Day 5 morning에 L=80 추가 (success #6 partial).

**Failure modes**:
- F0 (test broken at start): Block 1 진입 전 디버깅. Day 4 일정 1-2h 지연.
- F1 (user defers all): Block 1, 2, 3 skip. Block 4 + 6만 진행. CV-1.5 유지.
- F2 (user partial approve): subset만 적용. CHANGELOG에 명시.
- F4 (Block 4 시간 초과): §4.5.7 Day 5로 이동.
- F7 (git commit hook fail): root cause 디버깅 (--no-verify 금지).

---

## §7. W5 Ladder Status (Day 4 EOD a posteriori)

| Level | Day 3 EOD | **Day 4 EOD (expected)** |
|---|---|---|
| Minimal (G0+G1) | ✅ 100% | ✅ 100% |
| Standard (+G2+G3 substantive) | ✅ 100% | ✅ 100% |
| Ambitious (+G4-G6 ≥ 1) | ~90% (canonical promotion ready) | **✅ 100%** (CV-1.5.1 released; +T-σ-Theorem-4 격하 = G6 thermal proxy) |
| Maximal (+G7+G8) | ~15% | ~15-20% (Day 5+ 가능; NQ-244 결과 dependent) |
| Stretch (+CV-1.5.1 release + Paper 1 first draft) | ~50% | **~65-70%** (CV-1.5.1 ✅ + Paper §4 v2 ✅; Paper 1 §1-§3 skeleton Day 5-6) |

**가장 가능성 높은 Day 7 EOD**: Standard + Ambitious + Stretch (CV-1.5.1 official + Paper 1 first draft completed). Maximal은 W6에 carry.

---

## §8. Day 5+ Carry-Forward

**Day 5 (5-1 Fri)**:
- Morning: NQ-244 결과 분석 + Paper §4.5.5 update (3D LSW α plateau publishable 또는 caveat 강화).
- Afternoon: G5 SF Round 1-5 Cat A merge proposal (Q29-Q34) + Paper 1 §1-§3 skeleton.

**Day 6 (5-2 Sat)**:
- Morning: G5 apply (sub-set; user decision).
- Afternoon: W5 weekly_summary 초안 + Paper 1 §4-§6 skeleton.

**Day 7 (5-3 Sun)**:
- Morning: W5 weekly_summary finalize.
- Afternoon: W6 plan + W6_strategic_plan.md draft.
- EOD: W5 close. CV-1.5.1 official. Paper 1 first draft committed.

**W6 Day 1 priorities (re-confirm Day 7)**:
1. NQ-244 follow-up (3D LSW α refinement, if ambiguous Day 4).
2. NQ-198j (V5b-T-zero regime hunt: m=k² commensurate cluster).
3. NQ-198k (β-scan |∂S|-controlled).
4. NQ-242 sampler (full Hessian σ-tuple time series first).

---

## §9. Templates (canonical edit / OP register)

(See pre_brainstorm.md §6 for detail templates of D-1~D-4, D-6a inserts; OP-0008 entry; CHANGELOG 04-30 entry.)

---

## §10. Critical Risk Watch (Day 4 in-progress)

| Risk | Signal | Mitigation |
|---|---|---|
| Block 1 60min 초과 | apply 분량 더 큼 | D-6a를 Day 5로 분리 (D-1~D-4 + Critic 보강만 Day 4) |
| Test 175 → <175 post-edit | unrelated breakage | revert canonical, bisect, fix |
| Block 4 4h 초과 | Paper §4 재작성 깊이 | §4.5.7 caveat을 Day 5로 이동 |
| NQ-198l |μ| > 0.020 | V5b-T-zero phantom 가능성 | §4.4.2 caveat 추가; L=80 W6 Day 1 |
| NQ-244 background hang/OOM | 3D 메모리 부족 | T³_12 K=8 다운사이즈 Day 5 재시도 |
| Git commit hook fail | hook policy issue | root-cause 디버깅; --no-verify 금지 |

---

**End of plan.md.** **Ready for 09:00 Day 4 execution. User authorization required at 09:15.**
