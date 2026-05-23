---
type: log/daily/plan
date: 2026-05-20
day_of_week: Wed
session_label: W8-Day3 (Wed) — Verification-Light Day (post-SEAL extension carry-forward 정밀 검증)
canonical_version: CV-1.18 (sealed 2026-05-19, untouched)
mode: verification-light + algebraic-numerical (multi-layer adversarial 검증 protocol)
predecessors:
  - 2026-05-18 W8-Day1: 14-tier broad survey + AUX-1.5 §8 D/A/P classification (65/65 items, 2 U-residuals → CV-1.18 후 1)
  - 2026-05-19 W8-Day2 (낮): T_*/H5 deep-attack (02_H5_morse_spinodal.md 298L + 03_T_star_fixed_point.md 336L)
  - 2026-05-19 W8-Day2 (저녁): CV-1.18 SEAL — Stage 0 T axiom + T_* Route C + OP-0021 Routes A/B deprecation
  - 2026-05-19 W8-Day2 (post-SEAL evening): 19-phase Manifold Topology Methodology Program — 3 surviving claims (S1/S2/S3) + 8 retractions catalogued + 4-layer adversarial framework production-grade test
session_artifacts_target:
  - 00_plan.md (this file)
  - 01_pre_brainstorm.md
  - (optional) 02_cg_numerical_verification.md (if Priority 1 deep execution)
  - (optional) 03_D_L_commutation.md (if Priority 2 deep execution)
  - (optional) 04_dynamic_class_investigation.md (if Priority 3 progress)
  - 99_summary.md (EOD mandatory)
core_metrics:
  primary: Priority 1 ($c_G$ √3 discrepancy 해소) — measurable PASS/FAIL
  secondary: Priority 2 ($[D, L_G]$ commute 여부) — measurable YES/NO
  tertiary: Priority 3 (dynamic class investigation) — qualitative progress
decision_gate_target: 10/10 checks PASS
expected_session_time: 3-5 hours (verification-light, not deep-attack)
canonical_impact: 0 edits (working layer only)
agent_telemetry_target:
  numerical_verification_agents: 0-1 (if Priority 1 needs explicit Python REPL)
  algebraic_verification_agents: 0-1 (if Priority 2 needs careful canonical D operator analysis)
  general_purpose_agents: 0-2 (literature/canonical lookup as needed)
---

> [!nav] Linked: [[../2026-05-19/99_summary|어제 W8-Day2 99_summary + §POST-SEAL EXTENSION]] · [[../2026-05-19/04_manifold_topology_program_plan|어제 04 manifold_topology program plan]] · [[../2026-05-19/01_pre_brainstorm|어제 01 pre_brainstorm + §POST-SEAL APPENDIX]] · [[01_pre_brainstorm|today's pre_brainstorm reference]] · [[../../../working/foundation/manifold_topology_attempt_v1|v1 master synthesis]] · [[../../../working/foundation/foundation_reset_v0|foundation_reset_v0]] · [[../../../working/foundation/W8_Day2_evening_manifold_topology_report|W8_Day2 evening report]] · [[../../../canonical/canonical|CV-1.18 canonical.md]] · [[../../../canonical/CV-1.18_SEAL|CV-1.18 SEAL]]

# 2026-05-20 (W8-Day3, Wed) Plan — Verification-Light Day (정밀 검증)

## §0. Mission Statement (확장 버전)

### §0.1 본 day 의 *진짜 목적*

본 day = **verification-light + algebraic-numerical day**. 어제 (2026-05-19 evening, post-CV-1.18 SEAL) 의 *19-phase Manifold Topology Methodology Program* 에서 catch 한 **3 surviving claims (S1, S2, S3)** 의 *정밀 numerical + algebraic 검증*.

본 day 가 *답해야 할 3 질문*:
1. **$c_G$ 의 정확한 값은?** Phase 5 agent 가 보고한 $2.09$ vs Math-olympiad 가 재계산한 $1.17$ (factor $\sqrt{3}$ 차이) 의 *진짜 답*
2. **SCC 의 distinction operator $D$ 와 graph Laplacian $L_G$ 가 commute 하는가?** S3 의 *full SCC* (not just minimal model) 의 Cat A unconditional 여부 결정
3. **SCC 의 dynamic universality class 는 정확히 무엇인가?** Model A (Allen-Cahn 비보존) vs Model B (Cahn-Hilliard 보존) vs SCC-specific class

### §0.2 Mode Rationale (왜 verification-light 인가)

어제 19-phase program 이 *4-layer adversarial framework production-grade test* 를 통해 **naive import 8 systematic biases** 를 catch:
- Critic Pass 1: 4 critical findings (Bakry-Émery sign, codim arithmetic, L-theory vs K_0, basin equivalence)
- Critic Pass 2: 4 추가 critical (universality EW→AC→Model B, coarsening $t_\times$, H-int formation incompatibility, closure RG loop)
- Math-Olympiad: 3 numerical/hypothesis discrepancies + 1 commutation assumption

**살아남은 3 claims** (S1 Łojasiewicz $c_G$, S2 distance-Poincaré gap, S3 kernel-multiplicity identity) 은 *Cat B/C target* 상태. 이들의 *Cat A 또는 Cat B 승급* 을 위해서는 **numerical + algebraic verification** 필요.

**Mode 분류**:
- Verification-light: 새 derivation 시도 *없음* (어제 deep-attack 과 대조)
- Algebraic-numerical: 수학적 정밀 계산 + canonical 문서 정독
- Multi-layer adversarial: 어제 검증된 4-layer framework 적용 (specialist → critic → math-olympiad → cross-reconciliation)

### §0.3 Today is NOT (anti-modes)

본 day 는 다음 *aren't*:
- ❌ Deep-attack day (어제가 그 역할; 19 phases 완료)
- ❌ SEAL day (canonical 0 edits 유지)
- ❌ New OP catalog day (어제 OP-NEW-1~8 draft 완료)
- ❌ Survey day (W8-Day1 가 그 역할; 14-tier broad survey 완료)
- ❌ Theory deep-derivation day (어제 18 phases 가 그 역할)
- ❌ Canonical promotion day (numerical verification 후 별도 SEAL session)

### §0.4 Today IS (positive identification)

본 day 는 다음 *is*:
- ✅ **Verification-light day** (numerical + algebraic checks)
- ✅ **Carry-forward execution** (어제 post-SEAL extension Priority 1-3 의 직접 실행)
- ✅ **Cat status calibration** (S1, S2, S3 의 정확한 Cat 등급 결정)
- ✅ **Canonical 보호 barrier 유지** (CV-1.18 untouched throughout)
- ✅ **Production-grade adversarial protocol 의 second day** (어제 first day 였음 — 18 phases 산출 + critic + math-olympiad)
- ✅ **W8 의 4번째 day** (W8-Day1 survey + W8-Day2 deep-attack + post-SEAL extension + W8-Day3 verification)

### §0.5 Strategic Importance

본 day 가 *왜 중요한가*:

1. **S1, S2, S3 의 Cat B/A 승급 candidate 결정** — 향후 CV-1.19 SEAL 의 main content 후보
2. **8 retractions 의 정직한 *영구 보존* + 동일 함정 회피** — production canonical 보호의 second layer (working layer 첫 layer + day-level catalog)
3. **4-layer adversarial framework 의 second-day validation** — 첫째 day 가 *naive import catch*, 둘째 day 가 *survival claim verification* — 두 단계 모두 production-grade 검증
4. **W8 mission 의 *방법론적 마무리*** — 14-tier palette → 8 biases catch → 3 surviving content → Cat 승급 candidate 의 4-step pipeline 완성

---

## §A. 입력 — 어제 post-SEAL extension Carry-Forward

본 §A 는 어제 산출의 *완전한 inventory* + 본 day 가 검증해야 할 정확한 statement.

### §A.1 살아남은 3 Claims (검증 대상, 상세)

#### §A.1.1 Claim S1 — Łojasiewicz $c_G$ explicit (Cat B conditional)

**Statement (Phase 5 산출)**:
For SCC at uniform critical point $u = c\mathbf{1}$, parameter $\Theta = (\alpha, \beta, c)$:
$$\mu_2(\Theta) \geq c_G(K) \cdot d, \quad d := \mathrm{dist}(\Theta, \Sigma_{T8})$$

where $\mu_2(\Theta) = 4\alpha\lambda_2(L_G) + \beta W''(c)$ is the Fiedler-mode Hessian eigenvalue, and:
$$c_G(K) = \inf_{\Theta^* \in K \cap \Sigma_{T8}} \sqrt{16 \lambda_2(L_G)^2 + W''(c)^2 + 144\,\beta^2\,(2c-1)^2}$$

**Validity radius**: $d \leq d_{\max}(K) \approx 0.08$ (Lipschitz remainder bound).

**Numerical Example** (2D torus L=16, c=1/2, β=1):
- Phase 5 agent stated: $c_G \approx 2.09$, $d_{\max} \approx 0.08$
- Math-olympiad recomputed: $c_G \approx 1.17$, $d_{\max} \approx 0.04$
- **Both numerical values disagree by factor $\sqrt{3}$**

**Pre-brainstorm step-by-step computation**:
1. $\lambda_2(L_{16 \times 16}) = 4 \sin^2(\pi/16) \approx 0.1522$
2. $W''(1/2) = 2(1 - 6 \cdot 0.5 + 6 \cdot 0.25) = -1$
3. $W'''(1/2) = 12(2 \cdot 0.5 - 1) = 0$
4. $c_G = \sqrt{16 \cdot 0.0232 + 1 + 0} = \sqrt{1.371} \approx 1.171$

**Implication**: 만약 $c_G = 1.17$ correct → Phase 5 agent 의 2.09 가 잘못 → v1 file 정정 필요. 만약 $c_G = 2.09$ correct → math-olympiad 가 다른 정의 사용 → 정의 명시 필요.

**Cat status**: Cat B *conditional on* (a) 3 hypotheses (off-kernel, c off spinodal boundary, mult($\lambda_2$)=1), (b) numerical reconciliation, (c) compact $K$ uniformity.

#### §A.1.2 Claim S2 — Distance-Controlled Poincaré Gap (Cat B target)

**Statement (Cor 7.1 어제 산출)**:
$$\lambda_1(\Sigma_m, E_\Theta, T_*) \geq c_G(K) \cdot d$$

where $\lambda_1$ is the spectral gap of the SCC Langevin generator on $L^2(\pi_{T_*})$.

**Derivation**: Direct from S1 + Bakry-Émery (BGL 2014 §4.2):
- $\mu_2(\Theta) = $ smallest Hessian eigenvalue on $T\Sigma_m$ (away from kernel)
- Bakry-Émery $CD(\mu_2, \infty)$ condition: $\mathrm{Hess}(E) \geq \mu_2 \cdot I$ on $T\Sigma_m$
- Implies Poincaré inequality $\lambda_1 \geq \mu_2 \cdot c_{BGL}$ for some constant from BGL
- Combined with S1: $\lambda_1 \geq c_G \cdot d$

**Sharpening**: For canonical T-PF-A1-PE (Cat A) bound $\lambda_1 \geq (\pi^2/n) e^{-\mathrm{osc}(E)/T_*}$:
- T-PF-A1-PE: exponentially small in $T_*$ for large $\beta n$
- S2 bound: linearly $\propto c_G d$, independent of $T_*$
- **S2 sharper than T-PF-A1-PE** when $c_G d > (\pi^2/n) e^{-\beta n/T_*}$, i.e., in formation regime $\beta \gg T_*$

**Cat status**: Cat B target *conditional on S1 Cat B promotion*.

#### §A.1.3 Claim S3 — Kernel-Multiplicity Identity (Cat A minimal / Cat A conditional full)

**Statement (Phase 3 산출)**:
For fixed connected graph $G$, every $\Theta \in \Sigma_{T8}$ has:
$$\dim \ker(\mathrm{Hess}(E_\Theta)(c\mathbf{1})\vert _{T\Sigma_m}) = \mathrm{mult}(\lambda_2(L_G)) =: k_0(G)$$

**Direct algebraic proof (minimal model, $E_{bd}$ only)**:
- $\mu_k(\Theta, c) = 4\alpha\lambda_k(L_G) + \beta W''(c)$ for eigenvalue index $k$
- $\mu_k = 0 \iff \beta/\alpha = -4\lambda_k(L_G)/W''(c) = 4\lambda_k/\lvert W''(c) \rvert$ (since $W''(c) < 0$)
- Multiple $k$ vanish simultaneously $\iff \lambda_k(L_G) = \lambda_2(L_G)$
- Count: $k_0(G) = \mathrm{mult}(\lambda_2(L_G))$

**Full SCC** (with $E_{cl} + E_{sep}$):
$$\mathrm{Hess}(E) = \mathrm{Hess}(E_{bd}) + \lambda_{cl} \mathrm{Hess}(E_{cl}) + \lambda_{sep} \mathrm{Hess}(E_{sep})$$

For S3 to hold for full SCC, additional terms must preserve $\ker(\mathrm{Hess}(E_{bd}))$.

**Math-olympiad finding**: For random non-commuting $D$ with $\lambda_{sep} = 0.5$, kernel destroyed (test on 2D torus L=8: dim drops 4 → 0). So **commutation condition $[D, L_G] = 0$ matters**.

**Cat status**:
- Minimal model: Cat A direct (canonical Theorem 4 algebraic)
- Full SCC: Cat A *conditional on $[D, L_G] = 0$* (or weaker invariant-subspace condition)

### §A.2 8 Retractions (회피 대상, 상세 명시)

본 day 에 *재시도 절대 금지*. 어제 catalog 의 완전한 형식:

| # | Retracted Claim | Why Wrong | Correct Replacement |
|---|---|---|---|
| 1 | SCC = Edwards-Wilkinson universality | Double-well $W''(c) < 0$ spinodal interior, unstable linearization | Non-local constrained Allen-Cahn (Rubinstein-Sternberg 1992) |
| 2 | Dynamic exponent $z = 2.17$ (Model A 2D Ising) | Mass conservation via $P$ projector → Model B (conserved) | $z = 4 - \eta \approx 3.75$ (Model B 2D Ising) — but P ≠ Laplacian, SCC-specific class possible |
| 3 | Coarsening crossover $t_\times \sim (\beta/\alpha)^{3/2}$ | Bray 1994 §3-4 explicit derivation gives $t_\times \sim \alpha/\beta$ | $t_\times \sim \alpha/\beta$ from $\xi_{AC}(t_\times) = \xi_{CH}(t_\times)$ matching |
| 4 | $D_f^{(k)} = (n-1) - k$ static fractal dim | $k=0$ gives $n-1$ = whole ambient (absurd); confused parameter-stratum with field-level-set | $D_f$ depends on continuum $d$ AND regime: bulk $d-1$, coarsening $(d-1)+\delta(t)$, critical $(d-1)+\eta_\partial(d)$ |
| 5 | H-int interior regime hypothesis | Formations saturate $u_i \to 0, 1$ — H-int excludes them | Need Tanaka formula with $K_t$ explicit, or formation-compatible regime (boundary-inclusive) |
| 6 | Closure $E_{cl}$ RG-irrelevance | Tree-level PSD shift verified, but loop-level RG missing | Cat D until 1-loop $\beta$-function for closure-induced quartic computed |
| 7 | $D_f = 11/8$ as theorem | SLE_3 limit for continuum 2D Ising (Smirnov 2010); discrete SCC continuum limit OPEN | Cat C conjecture, requires continuum scaling limit + conformal invariance |
| 8 | k(k+1)/2-1 stratification on single graph | For fixed $G$, uniform $k_0 = $ mult($\lambda_2(L_G)$); Phi map only 2-eff-param in Sym$^{n-1}$ | Stratification lives in graph moduli $W_n$ (Phase 8) |

**메타-lesson** (어제 §C.2): Naive import 시 *반드시 verify*:
- (i) Importing framework 의 defining structural features 가 SCC 와 *matching* 하는지
- (ii) Literature explicit formula vs heuristic dimensional analysis 의 차이
- (iii) Tree-level vs loop-level argument 의 차이
- (iv) Continuum vs discrete 의 차이
- (v) Hypothesis 가 regime of interest 를 *포함* 하는지 (배제 아님)

### §A.3 어제 산출 Files (Reference)

본 day verification 시 직접 참조할 파일:

| 파일 | 위치 | 본 day 사용 |
|---|---|---|
| `2026-05-19/04_manifold_topology_program_plan.md` | daily logs | post-SEAL plan §A-§S 전체 |
| `2026-05-19/01_pre_brainstorm.md` (§POST-SEAL APPENDIX) | daily logs | 위상수학 reference base |
| `2026-05-19/99_summary.md` (§POST-SEAL EXTENSION) | daily logs | extension overview |
| `THEORY/working/foundation/manifold_topology_attempt_v1.md` | working | v1 master synthesis (§8 math-olympiad) |
| `THEORY/working/foundation/foundation_reset_v0.md` | working | Phase 0 honest inventory |
| `THEORY/working/foundation/W8_Day2_evening_manifold_topology_report.md` | working | Phase 18 final report (timeline) |
| `THEORY/working/foundation/manifold_topology_attempt_v0.md` | working (superseded) | archive of initial attempt |
| `THEORY/working/foundation/fractal_dynamic_dim_v0.md` | working (superseded) | archive of Type F attempt |
| `~/.claude/plans/eager-splashing-dream.md` | plans | 14-tier palette + Phase 1 entry |

---

## §B. Today's Work Plan (시간 배분 + 정밀 sub-task)

### §B.1 Priority 1 — $c_G$ Numerical Verification (1-1.5 hours, HIGHEST priority)

#### §B.1.1 Sub-task 1.1: Manual Step-by-Step Computation (~15 min)

**Tool**: 수기 계산 (가장 빠름) + Python REPL 또는 calculator 확인

**Steps**:
1. Compute $\lambda_2(L_{16 \times 16})$:
   - 2D torus L×L Laplacian eigenvalues: $\lambda_{(j,k)} = 4 \sin^2(\pi j/L) + 4 \sin^2(\pi k/L)$ for $(j, k) \neq (0,0)$
   - Smallest non-zero: $\lambda_2 = 4 \sin^2(\pi/L)$ for $L = 16$
   - $\sin(\pi/16) \approx 0.1951$
   - $\sin^2(\pi/16) \approx 0.03806$
   - $\lambda_2 \approx 0.1522$
   
2. Compute $W''(c)$ and $W'''(c)$ at $c = 1/2$:
   - $W(u) = u^2(1-u)^2$
   - $W'(u) = 2u(1-u)(1-2u)$
   - $W''(u) = 2(1 - 6u + 6u^2)$
   - $W''(1/2) = 2(1 - 3 + 1.5) = -1$
   - $W'''(u) = 12(2u - 1)$
   - $W'''(1/2) = 0$

3. Plug into $c_G$ formula:
   $$c_G = \sqrt{16 \cdot (0.1522)^2 + (-1)^2 + 144 \cdot 1^2 \cdot 0^2}$$
   $$= \sqrt{16 \cdot 0.02316 + 1 + 0}$$
   $$= \sqrt{0.3706 + 1}$$
   $$= \sqrt{1.3706}$$
   $$\approx 1.171$$

4. Decision:
   - If computed = 1.171 → confirms Math-olympiad
   - If computed = 2.09 → confirms Phase 5 agent
   - If different → re-derive formula

#### §B.1.2 Sub-task 1.2: Independent Verification via scc/ Module (~15 min)

**Tool**: Python REPL (READ-ONLY)
```python
from scc.graph import GraphState
import numpy as np

# Generate 2D torus 16x16
g = GraphState.grid_2d(16, 16)

# Get Laplacian
L = g.laplacian()

# Compute eigenvalues
eigvals = np.linalg.eigvalsh(L)
lambda_2 = eigvals[1]  # smallest non-zero

print(f"λ_2(L_16x16) = {lambda_2:.6f}")
# Expected: 0.1522

# Compute c_G
c = 0.5; beta = 1
W_pp = 2*(1 - 6*c + 6*c*c)  # = -1
W_ppp = 12*(2*c - 1)  # = 0

c_G_squared = 16*lambda_2**2 + W_pp**2 + 144*beta**2*(2*c-1)**2
c_G = np.sqrt(c_G_squared)
print(f"c_G = {c_G:.6f}")
# Expected: 1.171
```

**Expected outcome**: c_G ≈ 1.171 (confirms Math-olympiad).

#### §B.1.3 Sub-task 1.3: Phase 5 Agent Output Investigation (~15 min)

**Question**: Why did Phase 5 agent state $c_G \approx 2.09$?

**Possible causes** (search Phase 5 output for clue):
- (a) Phase 5 used $\lambda_2(L_G) \neq 0.1522$ (e.g., used $\lambda_2 = 2\sin^2(\pi/L)$ without factor 4)
- (b) Phase 5 used different gradient norm definition (e.g., extra factor for compact $K$ infimum)
- (c) Phase 5 included additional term (e.g., from parameter dimensionalization)
- (d) Phase 5 used different formula altogether

**Action**: Read `manifold_topology_attempt_v1.md §1.1` for Phase 5 agent's exact derivation. Cross-check formula.

#### §B.1.4 Sub-task 1.4: Validity Radius $d_{\max}$ Recomputation (~15 min)

**Phase 5 stated**: $d_{\max} \approx 0.08$
**Math-olympiad stated**: $d_{\max} \approx 0.04$ (factor 2 off)

**Formula** (from Phase 5):
$$d_{\max}(K) = c_G(K) / \vert H_\mu\vert _{op}$$

where $\vert H_\mu\vert _{op} \leq \sqrt{576\beta^2 + 144}$ is the Hessian-of-$\mu_2$ operator norm.

**For $\beta = 1$**:
$$\vert H_\mu\vert _{op} \leq \sqrt{576 + 144} = \sqrt{720} \approx 26.83$$
$$d_{\max} = c_G / 26.83$$

- If $c_G = 1.17$: $d_{\max} \approx 0.0436$
- If $c_G = 2.09$: $d_{\max} \approx 0.0779$

**Verdict**: Both estimates internally consistent (factor 2 in $d_{\max}$ ≈ factor √3 in $c_G$ × bound). Not independent verification of $c_G$.

#### §B.1.5 Sub-task 1.5: Multiple Graph Cross-Check (~15 min)

Verify $c_G$ formula on additional graphs:

**Path $P_5$** (5 nodes in a line):
- $\lambda_2(L_{P_5}) = 2(1 - \cos(\pi/5)) \approx 0.382$
- $c_G = \sqrt{16 \cdot 0.146 + 1 + 0} = \sqrt{3.336} \approx 1.826$

**Complete graph $K_4$**:
- $\lambda_2(L_{K_4}) = 4$ (multiplicity 3)
- $c_G = \sqrt{16 \cdot 16 + 1 + 0} = \sqrt{257} \approx 16.03$

**Complete graph $K_8$**:
- $\lambda_2(L_{K_8}) = 8$ (mult 7)
- $c_G = \sqrt{16 \cdot 64 + 1 + 0} = \sqrt{1025} \approx 32.02$

**Verdict**: $c_G$ grows linearly with $\lambda_2$ for spectrally large graphs. K_8 ~ 32 matches Math-olympiad estimate from §A.1.1.

#### §B.1.6 Priority 1 Deliverable

**Required outputs**:
1. **Definitive $c_G(L=16, c=1/2, \beta=1)$ value** with verification trail
2. **Reason for Phase 5 vs Math-olympiad discrepancy** identified
3. **Updated v1 file §1.1** with corrected $c_G$ formula (if needed)
4. **Cat status update**: S1 promoted from "Cat B conditional with discrepancy" to "Cat B with verified $c_G$"

**Optional deliverable**: `02_cg_numerical_verification.md` if extensive analysis needed.

#### §B.1.7 Priority 1 Decision Tree

```
START: Run Sub-task 1.1 (manual computation)
   ↓
   c_G computed = ?
   ↓ 1.17 ─────→ Sub-task 1.2 (verify with scc/)
   ↓                 ↓ confirm 1.17 → S1 verified, update v1 with c_G=1.17
   ↓                 ↓ different → debug formula / Python
   ↓ 2.09 ─────→ Sub-task 1.3 (investigate Phase 5)
   ↓                 ↓ find Phase 5 mistake → fix v1
   ↓                 ↓ find different definition → document both
   ↓ other ─────→ Re-derive formula from scratch
                     ↓ resolve discrepancy → update v1
```

### §B.2 Priority 2 — $[D, L_G]$ Commutation Algebraic Check (1-2 hours, HIGHEST priority)

#### §B.2.1 Sub-task 2.1: Read Canonical D Definition (~20 min)

**Files to read**:
- `canonical.md §3.7` "Soft Distinction" — axiomatic definition
- `canonical.md §9.3` "Distinction candidate" — specific provisional form

**Information to extract**:
- Exact functional form of $D(x; v)$ where $v$ is the "complement" field
- Linear? Non-linear in $u$?
- Self-referential? (i.e., $D$ depends on $u$ through which it's evaluated)
- Graph-local? (depends only on neighborhoods of $x$)

**Expected**: $D$ is some functional of $1 - u$ via aggregation operator (e.g., $P_t(1-u)$ row-normalized adjacency application).

#### §B.2.2 Sub-task 2.2: Linearize $D$ at $u = c\mathbf{1}$ (~20 min)

At critical point $u = c\mathbf{1}$:
- $D(x; 1-u) = D(x; (1-c)\mathbf{1})$ at critical
- Linearize: $D(x; 1-u^* - \delta) = D_0 + J_D \delta + O(\delta^2)$
- $J_D$ = Jacobian, typically a matrix on $T\Sigma_m$

**Test**: Is $J_D$ a function of $L_G$ alone? (i.e., $J_D = f(L_G)$ for some smooth $f$)
- If yes → $[J_D, L_G] = 0$ automatic
- If no → check structure

#### §B.2.3 Sub-task 2.3: Compute $[J_D, L_G]$ on Small Graph (~30 min)

**Tool**: Python with explicit matrix computation.

**Test graph 1: Path $P_3$** (3 nodes in line: 1-2-3):
- $L_{P_3} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$
- Compute $J_D$ for SCC's distinction operator at $u = c\mathbf{1}$
- Check $L J_D = J_D L$ as matrices

**Test graph 2: $K_4$** (complete graph, 4 nodes):
- $L_{K_4} = 4I - \mathbf{1}\mathbf{1}^T$ (after normalization)
- Symmetric — likely $[D, L] = 0$ if $D$ respects $K_4$ symmetry

**Test graph 3: 2D torus $C_4 \times C_4$**:
- Translation-invariant
- $[D, L] = 0$ if $D$ respects translation symmetry
- More relevant to V5b-T-zero (Cat A canonical)

#### §B.2.4 Sub-task 2.4: Theoretical Analysis (~30 min)

**Question 1**: Is $D$ functional calculus of $L_G$?

If $D(x; v) = (f(L_G) v)(x)$ for some smooth $f$, then $[D, L_G] = 0$ automatically (any function of $L_G$ commutes with $L_G$).

If $D(x; v)$ involves $v$ at $x$'s neighbors (not all of $v$), then $D$ is "graph-local" but possibly not functional calculus.

**Question 2**: Does $D$ respect $\mathrm{Aut}(G)$-symmetry?

By construction (canonical §3.7), $D$ should be $\mathrm{Aut}(G)$-equivariant (no preferred vertex labeling). This implies $D$ commutes with $L_G$ in the sense of *block-diagonal in Aut(G)-isotypic decomposition*.

**Question 3**: On Fiedler eigenspace specifically, does $[D, L_G] = 0$?

Even if $[D, L_G] \neq 0$ on all of $\mathbb{R}^n$, the *restriction to Fiedler eigenspace* ($\lambda_2$-eigenspace of $L_G$) may commute. This is the *invariant-subspace condition* that suffices for S3 full SCC.

#### §B.2.5 Sub-task 2.5: Cat Status Update for S3 (~10 min)

**After verification**:
- Case A: $[D, L_G] = 0$ globally → S3 full SCC = **Cat A unconditional**
- Case B: $[D, L_G] = 0$ on Fiedler eigenspace only → S3 full SCC = **Cat A on $\Sigma_{T8}$**
- Case C: $[D, L_G] \neq 0$ generically → S3 full SCC = **Cat A *conditional* on commutation hypothesis explicit**

#### §B.2.6 Priority 2 Deliverable

**Required outputs**:
1. **Definitive $[D, L_G]$ status** (commute or not, on which subspace)
2. **S3 full SCC Cat status** (A unconditional / A on Σ_T8 / A conditional)
3. **Updated v1 file §1.3** with verified S3 statement

**Optional deliverable**: `03_D_L_commutation.md` for detailed algebraic analysis.

#### §B.2.7 Priority 2 Decision Tree

```
START: Sub-task 2.1 (read canonical §3.7, §9.3)
   ↓
   D operator form identified?
   ↓ Yes → Sub-task 2.2 (linearize at u = c·1)
   ↓ Unclear → Read canonical §9 broader context
   ↓
   J_D Jacobian form?
   ↓ Functional of L_G → [D, L] = 0 automatic → Cat A unconditional
   ↓ Graph-local non-functional → Sub-task 2.3 (compute on P_3, K_4, C_4×C_4)
   ↓
   Computation result?
   ↓ All commute → Cat A on all graphs verified
   ↓ Some commute → Cat A conditional on Aut(G) structure
   ↓ None commute → Cat A conditional on specific subspace
```

### §B.3 Priority 3 — SCC Dynamic Class Investigation (if time, MED priority)

#### §B.3.1 Sub-task 3.1: Re-read Canonical SDE Formulation (~30 min)

**Files**:
- `canonical.md` T-PF-A1-SDE Cat A statement
- `canonical.md §13` for full P-F Package I (4 Cat A theorems)

**Information to extract**:
- Exact SDE form: $dU_t = ?$
- Projection $P_{T\Sigma_m}$ definition (NOT Laplacian)
- Reflection $K_t$ (Skorokhod) form

#### §B.3.2 Sub-task 3.2: Compare with Hohenberg-Halperin Model Classification (~30 min)

**Read Hohenberg-Halperin 1977 RMP 49:435** (or summary).

| Aspect | Model A | Model B | SCC |
|---|---|---|---|
| Order parameter | Non-conserved scalar | Conserved scalar | $u$ on $\Sigma_m$ |
| Conservation | None | Local ($\int \phi$ conserved) | Global ($\sum u_i = m$) |
| Equation | $\partial_t \phi = -\delta H/\delta \phi + \eta$ | $\partial_t \phi = \nabla^2 \delta H/\delta \phi + \nabla \eta$ | $\partial_t u = -P \nabla E + \sqrt{2T_*} P dB$ |
| $z$ exponent | $\approx 2.17$ (2D Ising) | $\approx 3.75$ (2D Ising) | ? |

**Question**: Is SCC's $P$ equivalent to Model B's $\nabla^2$?
- Mathematically: $P = I - n^{-1}\mathbf{1}\mathbf{1}^T$, removes constant mode only
- Cahn-Hilliard's $\nabla^2$ acts on each mode by eigenvalue $-q^2$ (in Fourier)
- These are *very different operators* — SCC is NOT Cahn-Hilliard

**Conclusion**: SCC is *constrained Allen-Cahn (Rubinstein-Sternberg)*, has GLOBAL but not LOCAL conservation. Dynamic class may be:
- *Effective Model A* (local dynamics) with *global Lagrange multiplier correction*
- Or *SCC-specific class* with novel exponent

#### §B.3.3 Sub-task 3.3: Literature Search for Constrained AC Dynamic Exponent (~30 min)

**Search**: Rubinstein-Sternberg 1992, Bray 1994, Funaki-Spohn 1997 for explicit dynamic exponent of constrained AC.

**Expected findings**:
- AC universality early time: $z \approx 2.17$ (Model A)
- LSW late time: $L(t) \sim t^{1/3}$, but $z = 3$ effective dynamic exponent? (or different formalism)
- Crossover at $t_\times \sim \alpha/\beta$ (Bray 1994 §3-4)

**Question**: Is there a *single $z$* for SCC, or *regime-dependent* $z$ (Model A early, Model B-like late)?

#### §B.3.4 Sub-task 3.4: Investigation Outline (NOT full derivation)

**Goal for Priority 3**: Outline *the question* + *initial framework*, not full answer.

**Outline**:
1. SCC SDE form (T-PF-A1-SDE Cat A)
2. Model A vs Model B comparison
3. Why SCC's $P$ ≠ Laplacian $L$ → SCC ≠ Cahn-Hilliard
4. Constrained AC literature (Rubinstein-Sternberg)
5. Open question: SCC dynamic exponent — Model A, Model B, or hybrid?

**Deliverable**: `04_dynamic_class_investigation.md` (outline only, ~200 lines)

### §B.4 Detailed Time Allocation

| Time slot | Task | Sub-tasks | Output |
|---|---|---|---|
| 09:00-09:30 | Setup + read 00_plan + 01_pre_brainstorm | — | Ready to start |
| 09:30-10:00 | Priority 1.1 (manual computation) | 1.1 | $c_G$ value pinned |
| 10:00-10:30 | Priority 1.2 (Python verify) | 1.2 | Verification confirmed |
| 10:30-10:45 | Priority 1.3 (Phase 5 investigation) | 1.3 | Discrepancy reason |
| 10:45-11:00 | Priority 1.6 (deliverable write) | 1.6 | Section in 99 or 02 |
| 11:00-11:20 | Priority 2.1 (read canonical D) | 2.1 | D operator form |
| 11:20-11:40 | Priority 2.2 (linearize) | 2.2 | $J_D$ Jacobian |
| 11:40-12:10 | Priority 2.3 (matrix computation) | 2.3 | Commute or not |
| (lunch) | | | |
| 13:30-14:00 | Priority 2.4 (theoretical analysis) | 2.4 | Subspace conditions |
| 14:00-14:15 | Priority 2.5+2.6 (deliverable) | 2.5, 2.6 | S3 full SCC status |
| 14:15-15:45 | Priority 3 (dynamic class investigation) | 3.1-3.4 | Outline file |
| 15:45-16:30 | EOD 99_summary 작성 | — | Mandatory summary |
| 16:30 | Session end | — | — |

**Total**: ~5-6 hours of focused work.

### §B.5 Adaptive Time Management

If Priority 1 takes < 1 hour:
- Extend Priority 2 with more graph examples
- Start Priority 3 earlier

If Priority 1 takes > 2 hours (unexpected discrepancy):
- Drop Priority 3 entirely
- Focus on completing Priority 1 + 2

If Priority 2 takes > 2 hours (D operator complex):
- Drop Priority 3
- Document Priority 2 as "investigation in progress"

---

## §C. Decision Gate (10 checks, expanded from 8)

| 검사 | 기준 | 검증 방법 | 결과 (EOD) |
|---|---|---|---|
| 1 | canonical 0 edits | `git status THEORY/canonical/` clean | TBD |
| 2 | DECLARATION 0 edits | `git status THEORY/canonical/DECLARATION.md` | TBD |
| 3 | scc/ 0 edits (READ-ONLY) | `git status CODE/scc/` clean | TBD |
| 4 | pytest baseline 유지 | optional 재실행 225+1xf | TBD |
| 5 | 8 retractions 재시도 0 | §A.2 anti-goal 준수 check | TBD |
| 6 | Silent OP resolution 0 | new OP 등록 0 | TBD |
| 7 | Priority 1 ($c_G$) 완료 | Definitive value + reason for discrepancy | TBD |
| 8 | Priority 2 ($[D, L_G]$) 완료 | commute status + S3 full SCC Cat update | TBD |
| 9 | EOD 99_summary 작성 | mandatory | TBD |
| 10 | Hard-constraint 16/16 PASS | §F self-check | TBD |

**Target**: 10/10 PASS.

**Conditional pass** (Priority 3 incomplete): 9/10 PASS acceptable if Priority 1 + 2 + 9 + 10 all green.

---

## §D. Risk Register (Detailed, 8 risks)

### §D.1 R1 — $c_G$ Discrepancy 둘 다 잘못

**Risk**: Both Phase 5 (2.09) and Math-olympiad (1.17) wrong; formula itself has missing factor.

**Severity**: MED (delays S1 Cat B promotion)

**Likelihood**: LOW (formula is straightforward from IFT + gradient computation)

**Mitigation**: 
- Priority 1.5 manual sanity check on multiple graphs (path P_5, K_4, K_8)
- If all 3 disagree with both estimates → re-derive from canonical Lemma 2.4
- Worst case: spend additional 1 hour on §B.1.4 validity radius double-check

### §D.2 R2 — $[D, L_G]$ Result Graph-Dependent

**Risk**: $[D, L_G] = 0$ for some graphs but not others; can't make uniform statement.

**Severity**: LOW (still Cat A conditional)

**Likelihood**: MED ($D$ may respect specific graph symmetries)

**Mitigation**:
- Test on 3 graphs (P_3, K_4, torus) in Sub-task 2.3
- If graph-dependent → document explicit invariant subspace condition
- Cat A conditional is acceptable status

### §D.3 R3 — Dynamic Class 확정 못함

**Risk**: Priority 3 investigation cannot definitively classify SCC dynamics.

**Severity**: LOW (Priority 3 deliverable is "outline only")

**Likelihood**: HIGH (this is multi-session work, not single-day)

**Mitigation**:
- Priority 3 deliverable is *outline*, not *classification*
- Outline file describes *question + framework + literature* — sufficient

### §D.4 R4 — 시간 초과 (5+ hours)

**Risk**: Session extends beyond planned 5-6 hours.

**Severity**: LOW

**Likelihood**: MED

**Mitigation**:
- §B.5 adaptive time management
- Drop Priority 3 if needed
- Priority 1 + 2 + 99_summary = mandatory minimum (3 hours)

### §D.5 R5 — scc/ 수정 충동

**Risk**: During Python verification (Sub-task 1.2), urge to fix scc/ bug or add feature.

**Severity**: HIGH if happens (canonical impact)

**Likelihood**: LOW (Priority 1.2 is straightforward READ-ONLY)

**Mitigation**:
- §F.3 hard constraint explicit
- All Python calls READ-ONLY
- No `Write` or `Edit` on scc/ files

### §D.6 R6 — Canonical 직접 수정 충동

**Risk**: While reading canonical §3.7, §9.3, urge to clarify or fix.

**Severity**: CRITICAL (canonical impact)

**Likelihood**: LOW

**Mitigation**:
- §F.1 hard constraint explicit
- All canonical reading READ-ONLY
- Suggestions noted in working files, NOT in canonical

### §D.7 R7 — Silent OP Resolution

**Risk**: Priority 1-3 results may *implicitly* resolve canonical OP without explicit registration.

**Severity**: HIGH (silent resolution violates §15.4)

**Likelihood**: LOW

**Mitigation**:
- All results recorded in 99_summary EOD
- Any implication for OP-NEW-1~8 or canonical OPs explicit
- No claim of "OP-X resolved" without §J anti-goal check

### §D.8 R8 — 4-Layer Adversarial Architecture 비활성화

**Risk**: Verification-light day, agent calls minimal — adversarial layers not activated.

**Severity**: LOW (verification-light doesn't require full 4-layer)

**Likelihood**: MED

**Mitigation**:
- Priority 1, 2 results subject to internal self-check (math-olympiad style)
- If any result unexpected → fire critic agent for verification
- 4-layer for *unexpected results*, not for *expected verification*

---

## §E. Anti-Goals (Expanded, 16 items)

본 day 에 **반드시 회피**:

### §E.1 Naive Import 재시도 (8 retractions 각각)

1. ❌ Edwards-Wilkinson universality 재시도
2. ❌ Dynamic exponent $z = 2.17$ (Model A) 사용
3. ❌ Coarsening crossover $t_\times \sim (\beta/\alpha)^{3/2}$ 사용
4. ❌ $D_f^{(k)} = (n-1) - k$ codim 공식 사용
5. ❌ H-int 가설 formation regime 에 적용
6. ❌ Closure RG-irrelevance loop-level 미증명 채로 주장
7. ❌ $D_f = 11/8$ as theorem 주장
8. ❌ k(k+1)/2-1 single-graph stratification 사용

### §E.2 Canonical 보호 위반

9. ❌ canonical/*.md 직접 수정
10. ❌ DECLARATION.md 수정
11. ❌ scc/*.py 수정 (READ-ONLY only)
12. ❌ auxiliary_structures_master.md 수정 (Priority 1-3 결과는 working file 에만)

### §E.3 Methodological 위반

13. ❌ Silent OP resolution (어떤 OP 도 silent 하게 resolve 처리 금지)
14. ❌ New framework letter 도입
15. ❌ Single-agent consensus 신뢰 (Priority 1-2 결과 의문 시 cross-check)
16. ❌ Anti-pattern: "이건 obvious 하므로 verification 생략" (verification day 의 본질 위반)

---

## §F. Hard Constraint Self-Check (Pre-Execution)

| 제약 | 본 day status | 검증 시점 |
|---|---|---|
| F.1 canonical 0 edits | 약속됨 | EOD git status |
| F.2 DECLARATION 0 edits | 약속됨 | 동 |
| F.3 `_archive/` 부활 0 | 약속됨 | 동 |
| F.4 scc/ 0 edits (READ-ONLY 허용) | 약속됨 | 동 |
| F.5 새 framework letter 0 | 약속됨 | working file 검토 |
| F.6 silent OP resolution 0 | 약속됨 | 99_summary 명시 |
| F.7 Research OS 재도입 0 | 약속됨 | structure check |
| F.8 Reductive 환원 0 | 약속됨 | CN10 disclosure 준수 |
| F.9 Primitive 전도 0 | 약속됨 | u_t primitive 유지 |
| F.10 4 에너지 항 병합 0 | 약속됨 | working file 검토 |
| F.11 Closure idempotence 가정 0 | 약속됨 | Priority 2 analysis 점검 |
| F.12 K 이중 취급 0 | 약속됨 | scope outside Priority 1-3 |
| F.13 Zero-temp metastability 인지 | 약속됨 | applicable to Priority 3 |
| F.14 OMC 풀 오케스트레이션 0 | (사용 가능, 단 verification-light 에 필요 시만) | agent telemetry |
| F.15 pytest baseline 유지 | 약속됨 | optional 재실행 |
| F.16 Engineering proxy 도입 0 | 약속됨 | working file 검토 |

**16/16 PASS target** at EOD.

---

## §G. EOD 99_summary 필수 포함 사항 (확장 체크리스트)

본 day 종료 시 99_summary.md 에 *반드시* 포함:

### §G.1 Priority 결과 (정량적)

- [ ] **G.1.1** Priority 1 결과: $c_G(L=16, c=1/2, \beta=1)$ = ? (정확한 값)
- [ ] **G.1.2** Phase 5 vs Math-olympiad discrepancy 해소 reason
- [ ] **G.1.3** $d_{\max}(L=16, c=1/2, \beta=1)$ = ? (정확한 값)
- [ ] **G.1.4** Multiple graph cross-check 결과 (P_5, K_4, K_8)
- [ ] **G.1.5** Priority 2 결과: $[D, L_G]$ commute 여부 (commute / not / subspace-only)
- [ ] **G.1.6** S3 full SCC Cat status (A unconditional / A conditional / Cat lower)
- [ ] **G.1.7** Priority 3 결과: dynamic class investigation 진행 상태 (outline progress)

### §G.2 Cat Status Update Table

| Claim | 어제 EOD Cat | 본 day EOD Cat | Reason |
|---|---|---|---|
| S1 ($c_G$) | Cat B conditional | TBD | Priority 1 verification |
| S2 (Distance-Poincaré) | Cat B target | TBD | S1 conditional |
| S3 minimal model | Cat A | Cat A (unchanged) | direct algebraic |
| S3 full SCC | Cat A conditional | TBD | Priority 2 commutation |
| S4 (Σ_T8 codim-1) | Cat A canonical | Cat A (unchanged) | canonical SB7 |

### §G.3 Decision Gate Verification

- [ ] 10/10 checks PASS (§C)
- [ ] 16/16 hard constraints PASS (§F)
- [ ] 16 anti-goals 준수 (§E)

### §G.4 Files Produced 확인

- [ ] 00_plan.md (this file)
- [ ] 01_pre_brainstorm.md
- [ ] 99_summary.md (EOD mandatory)
- [ ] (optional) 02_cg_numerical_verification.md
- [ ] (optional) 03_D_L_commutation.md
- [ ] (optional) 04_dynamic_class_investigation.md

### §G.5 Carry-Forward to W8-Day4 (Thu 2026-05-21)

- [ ] **G.5.1** S1 status → CV-1.19 SEAL preparation possible?
- [ ] **G.5.2** S3 status → CV-1.19 SEAL preparation possible?
- [ ] **G.5.3** Dynamic class → multi-session work plan
- [ ] **G.5.4** New OP-NEW-X catalog entries (if any verification result requires)

### §G.6 Adversarial Self-Check

- [ ] If Priority 1 result unexpected → did I verify with cross-check?
- [ ] If Priority 2 commute → did I check on multiple graphs?
- [ ] If Priority 3 conclusion drawn → did I avoid retraction #2 (z exponent)?
- [ ] 8 retractions 재시도 absolute 0?

---

## §H. References (Comprehensive Cross-Reference)

### §H.1 어제 (2026-05-19) post-SEAL extension Files

| Reference | Content | 본 day 사용 |
|---|---|---|
| `04_manifold_topology_program_plan.md` (§A 19-phase catalogue) | 19 phases 작업 목록 | §A.3 file index |
| `04_manifold_topology_program_plan.md` (§B 4 claims) | S1-S4 statements | §A.1 직접 인용 |
| `04_manifold_topology_program_plan.md` (§C 8 retractions) | retraction catalog | §A.2 + §E.1 |
| `04_manifold_topology_program_plan.md` (§F numerical tasks) | Priority 1-4 detail | §B 직접 carry-forward |
| `04_manifold_topology_program_plan.md` (§I risk register) | 5 risks | §D 확장 |
| `04_manifold_topology_program_plan.md` (§S verification execution order) | W8-Day4-5 roadmap | §G.5 carry-forward |
| `01_pre_brainstorm.md §POST-SEAL APPENDIX` | 위상수학 reference base | 01_pre_brainstorm (today) |
| `99_summary.md §POST-SEAL EXTENSION` | extension overview | §0 mission context |

### §H.2 Working Files

| File | Content | Section reference |
|---|---|---|
| `manifold_topology_attempt_v1.md §1.1` | S1 statement + $c_G$ formula | §A.1.1 |
| `manifold_topology_attempt_v1.md §1.2` | S2 statement + Cor 7.1 | §A.1.2 |
| `manifold_topology_attempt_v1.md §1.3` | S3 statement + kernel mult identity | §A.1.3 |
| `manifold_topology_attempt_v1.md §1.4` | S4 statement (canonical SB7) | §A.1 |
| `manifold_topology_attempt_v1.md §2` | 8 retraction catalogue | §A.2 + §E.1 |
| `manifold_topology_attempt_v1.md §8` | Math-olympiad verification (S1, S2, S3) | §A.1.1 (discrepancy) |
| `foundation_reset_v0.md §1` | Valid results inventory | §A.1 cross-check |
| `foundation_reset_v0.md §2` | Invalidated claims | §A.2 cross-check |
| `foundation_reset_v0.md §3` | Critic findings re-evaluated | §D mitigation |
| `W8_Day2_evening_manifold_topology_report.md §3` | Cat A path per claim | §B.2.5 + §G.2 |

### §H.3 Canonical SCC Cat A Baselines (CV-1.18)

| Theorem | Location | Used in |
|---|---|---|
| T8-Core (phase transition) | canonical.md L1135 | §A.1.3 (μ_k formula) |
| SB7 (Σ_T8 codim-1) | canonical.md L2495 | §A.1.3 (S3 minimal Cat A) |
| Theorem 4 (Hessian eigenvalue) | canonical.md L1466 | §A.1.3 + §B.1.1 |
| T-V5b-T-zero (Goldstone exact) | canonical.md L1328 | §A.1.3 + §B.2.4 (Aut(G) equivariance) |
| T-σ-Theorem-3 (Aut(G) decomposition) | canonical.md L1466 | §B.2.4 |
| T-PF-A1-AR (field polytope) | canonical.md L1668 | §B.3.1 |
| T-PF-A1-SDE (reflected Langevin) | canonical.md L1670+ | §B.3.1 |
| T-PF-A1-GI (Gibbs invariance) | canonical.md L1688 | §B.3.1 |
| T-PF-A1-PE (Poincaré ergodicity) | canonical.md L1700 | §A.1.2 (S2 comparison) |
| T-PERSIST-1B-UNCONDITIONAL | canonical.md L2063 | §B.2.4 (Kupka-Smale + Sard precedent) |
| T-Temporal-Identity (CV-1.13) | canonical §13 | §B.3.1 (4-part Cat A) |
| Distinction operator | canonical §3.7 | §B.2.1 (D definition) |
| Distinction candidate (provisional) | canonical §9.3 | §B.2.1 |
| Appendix OMS §N (CV-1.18) | canonical Appendix OMS | §B.3.1 (T_* ξ resident) |
| AUX-1.5 §8 (D/A/P classification) | auxiliary_structures_master.md | §A.1 context |
| CV-1.18 SEAL | THEORY/canonical/CV-1.18_SEAL.md | §0 context |

### §H.4 External Literature (어제 §POST-SEAL APPENDIX 의 직접 인용)

**Statistical physics / dynamic universality**:
- Hohenberg-Halperin (1977) *RMP* 49:435 — Model A/B classification (§B.3.2 직접)
- Edwards-Wilkinson (1982), KPZ (1986)
- Allen-Cahn (1979), Lifshitz-Slyozov (1961)
- Bray (1994) *Adv Phys* 43:357 — phase ordering (§B.3.3 + retraction #3)
- Bray-Rutenberg (1994), Funaki-Spohn (1997)
- Rubinstein-Sternberg (1992) *IMA J Appl Math* 48:249 — non-local AC (§B.3.2 직접)

**Critical phenomena / RG**:
- Onsager (1944), Wilson-Fisher (1972)
- Wansleben-Landau (1991), Kamieniarz-Blöte (1993), Pelissetto-Vicari (2002)

**Probability / SDEs**:
- Bakry-Gentil-Ledoux (2014) — Γ_2 + BGL convention (§A.1.2)
- Otto-Villani (2000), Lions-Sznitman (1984)
- Tanaka (1979), Freidlin-Wentzell (1998)
- Markowich-Villani (1999)

**Random fields / fractals**:
- Adler-Taylor (2007), Sheffield (2007), Falconer (2003)
- Schramm (2000), Smirnov (2010), Chelkak-Smirnov (2012) — retraction #7
- Boissonnat-Pritam (2021)

**Algebraic topology / assembly**:
- Browder (1972), Wall (1970), Ranicki (2002), Davis-Lück (1998)
- Hairer (2014) — regularity structures (retraction #6 Cat A path)

---

## §I. Working File Output Schemas

본 day 에 생성 가능한 working files 의 *예상 구조*:

### §I.1 02_cg_numerical_verification.md (optional)

```markdown
# 02 — $c_G$ Numerical Verification (W8-Day3, 2026-05-20)

## §1. Manual Step-by-Step Computation
[verbatim from Sub-task 1.1]

## §2. Python Verification via scc/ Module  
[code + output]

## §3. Phase 5 Agent Investigation
[reason for discrepancy]

## §4. Multiple Graph Cross-Check
[P_5, K_4, K_8 verification]

## §5. Verdict
[c_G definitive value + Cat status update]

## §6. References
[canonical anchors + Phase 5 source]
```

### §I.2 03_D_L_commutation.md (optional)

```markdown
# 03 — $[D, L_G]$ Commutation Analysis (W8-Day3, 2026-05-20)

## §1. Canonical D Definition
[from canonical §3.7, §9.3]

## §2. Linearization at u = c·1
[J_D Jacobian explicit]

## §3. Commutation Test
[P_3, K_4, C_4×C_4 matrix computations]

## §4. Theoretical Analysis
[functional calculus? Aut(G)-equivariance?]

## §5. Verdict
[commute status + S3 Cat status]

## §6. References
```

### §I.3 04_dynamic_class_investigation.md (optional, outline only)

```markdown
# 04 — SCC Dynamic Class Investigation (W8-Day3 outline)

## §1. SCC SDE Form (canonical T-PF-A1-SDE)
## §2. Hohenberg-Halperin Comparison
## §3. Why SCC's P ≠ Laplacian L
## §4. Constrained AC Literature
## §5. Open Question + Framework
## §6. References

(NOT a derivation — outline + question framing only)
```

### §I.4 99_summary.md (mandatory EOD)

Structure consistent with previous days (00_plan §G.1-§G.6 체크리스트 따름).

---

## §J. Verification Architecture (4-Layer Adversarial)

어제 검증된 production-grade 4-layer framework 의 *본 day version*:

### §J.1 Layer 1 — Specialist Computation

- Sub-task 1.1, 1.2: Direct computation (manual + Python)
- Sub-task 2.1, 2.2, 2.3: Direct algebraic verification
- Sub-task 3.1: Direct canonical reading

**Risk**: Single-source computation bias.

**Mitigation**: Multiple cross-checks (manual + Python + multiple graphs).

### §J.2 Layer 2 — Self-Critic (Internal)

After each Priority completion:
- "Did I verify this correctly?"
- "Are there hidden assumptions?"
- "Does this contradict canonical Cat A?"

**Risk**: Confirmation bias.

**Mitigation**: Explicit checklist (§G).

### §J.3 Layer 3 — Cross-Reference (Canonical + Working Files)

After each Priority completion:
- Cross-check with canonical Cat A baselines (§H.3)
- Cross-check with v1 master synthesis §8 math-olympiad findings (§A.1)
- Cross-check with W8_Day2_evening_manifold_topology_report Cat A path (§G.2)

**Risk**: Stale references.

**Mitigation**: Read references at start of each Priority, not just plan.

### §J.4 Layer 4 — External Adversarial (if needed)

If any Priority result *unexpected*:
- Fire critic agent for adversarial review
- Or fire math-olympiad agent for counterexample search

**Risk**: Over-reliance on agent (cost + slowness).

**Mitigation**: Only fire if result *contradicts* expected (e.g., $c_G \neq 1.17$ and $\neq 2.09$).

---

## §K. Cat Status Update Tracking (Real-Time)

본 day 진행 중 Cat status 변화 실시간 기록:

### §K.1 S1 ($c_G$) Cat status timeline

| 시점 | Cat status | 이유 |
|---|---|---|
| W8-Day2 entry | Cat C target | First derivation |
| W8-Day2 evening Phase 5 | Cat B target (with discrepancy) | Explicit formula |
| W8-Day2 evening Critic 1 | Cat B conditional (Critic C2 overreach 거부됨) | linear scaling verified |
| W8-Day2 evening Math-olympiad | Cat B *conditional with 3 hypotheses + discrepancy* | numerical issue |
| W8-Day3 morning (now) | Cat B conditional (pending verification) | this day's work |
| W8-Day3 EOD target | Cat B verified, ready for CV-1.19 SEAL | Priority 1 resolution |

### §K.2 S3 ($\dim\ker = \mathrm{mult}\lambda_2$) Cat status timeline

| 시점 | Cat status | 이유 |
|---|---|---|
| W8-Day2 evening Phase 3 | Cat A minimal model | Direct algebraic |
| W8-Day2 evening Critic 2 | Cat A *conditional on $[D, L_G] = 0$* | Math-olympiad finding |
| W8-Day3 morning (now) | Cat A conditional (pending Priority 2) | this day's work |
| W8-Day3 EOD target | Cat A unconditional OR Cat A on Σ_T8 | Priority 2 resolution |

### §K.3 New OP catalog entries (from Priority 1-2 results)

If verification reveals new open issues:
- OP-NEW-9: (if applicable) — specific to today's findings
- ...

---

## §L. Pre-Execution Final Check

### §L.1 Required reading before start

1. **00_plan.md** (this file) — 전체 한 번
2. **01_pre_brainstorm.md** — verification reference
3. **2026-05-19/04_manifold_topology_program_plan.md §B (4 claims)** — S1-S4 statements
4. **2026-05-19/01_pre_brainstorm.md §POST-SEAL APPENDIX** — 위상수학 reference base
5. **manifold_topology_attempt_v1.md §1 (claims) + §8 (math-olympiad)** — v1 synthesis + verification

### §L.2 Required tools

- Pencil + paper (manual computation)
- Python REPL (Sub-task 1.2 — optional but recommended)
- canonical.md reader (Sub-task 2.1, §H.3 references)
- v1 + working files reader (cross-references)

### §L.3 Required mental state

- Verification mode (not derivation mode)
- Skeptical of all "obvious" claims
- Layer 4 adversarial ready (fire critic agent if unexpected)
- Hard constraint discipline (§F)
- Anti-goal vigilance (§E)

---

## §M. Closing Plan Slogan (Expanded)

> **W8-Day3 = *verification-light day*. 어제 post-SEAL extension 의 3 surviving claims (S1 Łojasiewicz $c_G$, S2 distance-Poincaré gap, S3 kernel-multiplicity identity) 의 *정밀 numerical/algebraic verification*. 새 derivation 0, naive import retry 0, canonical edits 0.**
>
> **Priority 1**: $c_G$ √3 discrepancy 해소 (1-1.5 hours) → S1 Cat B promoted ready for CV-1.19 SEAL.
>
> **Priority 2**: $[D, L_G]$ commutation algebraic check (1-2 hours) → S3 full SCC Cat A status finalized.
>
> **Priority 3**: SCC dynamic class investigation (remaining time) → outline + framework only.
>
> **Decision gate**: 10/10 PASS target (canonical 0 edits, 8 retractions absent, Priority 1+2 complete, 99_summary mandatory).
>
> **Hard constraints**: 16/16 PASS target.
>
> **Adversarial framework**: 4-layer (specialist + self-critic + cross-reference + external if needed) — *verification day version* of yesterday's production-grade test.
>
> **Carry-forward to W8-Day4 (Thu 2026-05-21)**: depending on Priority 1+2 results, candidate for CV-1.19 SEAL preparation (S1 + S3 unconditional) or extended verification (if results require).

---

## §N. Appendix — Quick Reference Cards

### §N.1 $c_G$ Formula Quick Reference

```
c_G(K) = inf_{Θ* ∈ K ∩ Σ_T8} √(16λ_2² + W''(c)² + 144β²(2c-1)²)
       = √(16·0.0232 + 1 + 0)   [at L=16, c=1/2, β=1]
       = √1.371
       ≈ 1.171   [Math-olympiad value]
```

### §N.2 8 Retractions Quick Reference

```
1. ❌ Edwards-Wilkinson universality
2. ❌ z = 2.17 (Model A)
3. ❌ t_× ~ (β/α)^(3/2)
4. ❌ D_f^(k) = (n-1) - k
5. ❌ H-int for formations
6. ❌ Closure RG-irrelevance (loop)
7. ❌ D_f = 11/8 theorem
8. ❌ k(k+1)/2-1 single-graph stratification
```

### §N.3 Decision Gate Quick Reference

```
1.  canonical 0 edits ✓
2.  DECLARATION 0 edits ✓
3.  scc/ 0 edits ✓
4.  pytest baseline ✓
5.  8 retractions 재시도 0 ✓
6.  Silent OP resolution 0 ✓
7.  Priority 1 ($c_G$) 완료 ✓
8.  Priority 2 ($[D, L]$) 완료 ✓
9.  EOD 99_summary 작성 ✓
10. Hard constraint 16/16 PASS ✓
```

---

*Plan 작성 완료 2026-05-20 morning. 총 ~1500 lines. 다음: 01_pre_brainstorm 검토 → Priority 1.1 시작.*
