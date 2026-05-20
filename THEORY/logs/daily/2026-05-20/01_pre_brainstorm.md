---
type: log/daily/pre_brainstorm
date: 2026-05-20
day_of_week: Wed
session_label: W8-Day3 (Wed) — Pre-Brainstorm: Verification-Light Day Reference
parent_plan: 00_plan.md
purpose: 본 day 의 Priority 1-3 verification task 의 reference 백서 — 어제 post-SEAL extension 산출물 + 검증 시 인용할 정확한 정의/식/canonical anchor
canonical_version: CV-1.18 (sealed 2026-05-19, untouched)
---

> [!nav] Linked: [[00_plan|today's verification plan]] · [[../2026-05-19/99_summary|어제 W8-Day2 99_summary + §POST-SEAL EXTENSION]] · [[../2026-05-19/04_manifold_topology_program_plan|어제 post-SEAL plan]] · [[../2026-05-19/01_pre_brainstorm|어제 pre_brainstorm + §POST-SEAL APPENDIX]] · [[../../../working/foundation/manifold_topology_attempt_v1|v1 master synthesis]]

# 01 Pre-Brainstorm — Verification-Light Day Reference

## §0. Mission of this file

오늘 (2026-05-20, W8-Day3) 의 *Priority 1-3 verification task* 의 *reference 백서*. 새 derivation 시도 *없음*; 단지 어제 post-SEAL extension 의 산출물 + 검증 시 인용할 정확한 정의/식/canonical anchor 를 한 곳에 압축.

산출 절:
- §1 (Priority 1 reference): $c_G$ 공식 + canonical SB7 + Lemma 2.4
- §2 (Priority 2 reference): $D$ operator + $L_G$ Laplacian + canonical §3.7, §9.3
- §3 (Priority 3 reference): Hohenberg-Halperin Model A/B + Cahn-Hilliard vs constrained AC
- §4 (Anti-goal reference): 8 retractions explicit
- §5 (Numerical infrastructure): scc/ 모듈 READ-ONLY 호출 가능 list
- §6 (Cat A/B promotion path)

---

## §1. Priority 1 Reference — $c_G$ Numerical Verification

### §1.1 어제 Phase 5 산출 (Łojasiewicz $c_G$ explicit)

**Statement**: SCC 의 Fiedler eigenvalue 가 distance-controlled bound 만족:
$$\mu_2(\Theta, c) \geq c_G(K) \cdot d, \quad d := \mathrm{dist}(\Theta, \Sigma_{T8})$$

where:
$$c_G(K) = \inf_{\Theta^* \in K \cap \Sigma_{T8}} \sqrt{16 \lambda_2(L_G)^2 + W''(c)^2 + 144\,\beta^2\,(2c-1)^2}$$

**Gradient computation (검증 기준)**:
- $\frac{\partial \mu_2}{\partial \alpha} = 4 \lambda_2(L_G)$
- $\frac{\partial \mu_2}{\partial \beta} = W''(c)$
- $\frac{\partial \mu_2}{\partial c} = \beta \cdot W'''(c) = 12\beta(2c-1)$

**Euclidean gradient norm**:
$$|\nabla_\Theta \mu_2|^2 = 16\lambda_2^2 + W''(c)^2 + 144\beta^2(2c-1)^2$$

### §1.2 2D 토러스 L=16 worked example (검증 input)

**Setup**: $G = \mathbb{Z}_{16} \times \mathbb{Z}_{16}$ (256 nodes), $c = 1/2$, $\beta = 1, \alpha = 1$

**Step-by-step computation**:

1. Laplacian eigenvalue:
$$\lambda_2(L_{16 \times 16}) = 4\sin^2(\pi/16)$$
$$\sin(\pi/16) \approx \sin(0.1963) \approx 0.1951$$
$$\sin^2(\pi/16) \approx 0.03806$$
$$\lambda_2 \approx 4 \cdot 0.03806 \approx 0.1522$$

2. Double-well 2nd derivative at $c = 1/2$:
$$W(u) = u^2(1-u)^2, \quad W''(u) = 2(1 - 6u + 6u^2)$$
$$W''(1/2) = 2(1 - 3 + 1.5) = 2 \cdot (-0.5) = -1$$
$$|W''(1/2)| = 1$$

3. Double-well 3rd derivative at $c = 1/2$:
$$W'''(u) = 12(2u - 1)$$
$$W'''(1/2) = 12 \cdot 0 = 0$$

4. Plug into $c_G$ formula:
$$c_G = \sqrt{16 \cdot (0.1522)^2 + (-1)^2 + 144 \cdot 1^2 \cdot 0^2}$$
$$= \sqrt{16 \cdot 0.02316 + 1 + 0}$$
$$= \sqrt{0.3706 + 1}$$
$$= \sqrt{1.3706}$$
$$\approx 1.171$$

### §1.3 Discrepancy 분석

- Phase 5 agent 보고: $c_G \approx 2.09$
- Math-olympiad 검증: $c_G \approx 1.17$
- Factor 차이: $2.09 / 1.17 \approx 1.786 \approx \sqrt{3.19}$ — 거의 $\sqrt{3}$

**가능한 원인**:
- (a) Phase 5 agent 가 다른 $\lambda_2$ 값 사용 (예: $\lambda_2 = 2\sin^2(\pi/16)$ 일 가능성, factor 2 missing?)
- (b) gradient norm definition 의 dimensionalization 차이
- (c) compact $K$ 의 infimum 처리 차이
- (d) Phase 5 가 다른 graph size 또는 boundary condition 사용

**Resolution approach**: 위 §1.2 step-by-step 계산이 *공식 자체로부터* 산출되었으므로, agent 의 2.09 가 *잘못된 가능성 높음*. 단, agent 가 다른 정의 사용했을 가능성도 명시 검토.

### §1.4 Canonical Anchors

- **SB7** (canonical.md L2495-2510, Cat A): $\Sigma_{T8} = \Sigma_{\mathrm{Hess}}$ codim-1 algebraic
- **Theorem 4** (canonical.md L1466, Cat A): $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ eigenvalue formula
- **CV-1.13 §13** Cat A baselines

### §1.5 검증 도구 (READ-ONLY scc/ 호출)

옵션:
- `from scc.graph import GraphState; g = GraphState.grid_2d(16, 16); g.lambda_2()` — Fiedler eigenvalue 계산
- 수기 계산 (위 §1.2 표시)
- NumPy direct: `np.sin(np.pi/16)**2 * 4`

---

## §2. Priority 2 Reference — $[D, L_G]$ Commutation Check

### §2.1 SCC distinction operator $D$ (canonical §3.7)

Read canonical.md §3.7 "Soft Distinction" for exact definition.

Provisional form (canonical §9.3, Section 9.3 — Distinction candidate):
$$D(x; 1-u) = \text{some functional of } 1-u \text{ via aggregation } P_t(1-u)$$

**Key feature**: $D$ depends on $u$ self-referentially. Whether $D$ as linear operator on $T\Sigma_m$ commutes with $L_G$ is the question.

### §2.2 Graph Laplacian $L_G$

For graph $G = (V, E)$:
$$L_G = D_G - A_G$$
where $D_G$ = degree diagonal matrix, $A_G$ = adjacency matrix. $L_G$ is symmetric PSD.

### §2.3 Commutation test approach

**For specific small graph** (e.g., path $P_3$ or $K_4$):

1. Compute $L_G$ explicitly (small matrix)
2. Compute $D$ at specific $u$ (e.g., $u = c\mathbf{1}$ uniform critical)
3. Check $L_G D = D L_G$ as matrices

**Case analysis**:
- Case A: $D(u) = f(L_G) u$ for some function $f$ → $D$ commutes with $L_G$ automatically
- Case B: $D(u)$ depends on local neighborhoods only → commutes if $D$ is graph-symmetric
- Case C: $D$ depends on $u$ non-trivially → commute on specific subspaces only

### §2.4 Implications for S3 (Kernel-multiplicity identity)

**S3 statement**:
$$\dim \ker(\mathrm{Hess}(E_\Theta)(c\mathbf{1})|_{T\Sigma_m}) = \mathrm{mult}(\lambda_2(L_G)) =: k_0(G)$$

**Minimal model** (just $E_{bd}$): direct algebraic from Theorem 4. Cat A unconditional.

**Full SCC** (with $E_{cl} + E_{sep}$):
$$\mathrm{Hess}(E) = \mathrm{Hess}(E_{bd}) + \lambda_{cl} \mathrm{Hess}(E_{cl}) + \lambda_{sep} \mathrm{Hess}(E_{sep})$$

For S3 to hold for full SCC:
- $\mathrm{Hess}(E_{cl})$ must preserve $\ker(\mathrm{Hess}(E_{bd}))$ as a whole
- $\mathrm{Hess}(E_{sep})$ similar

This is equivalent to *commutation* condition (or weaker — invariant subspace condition).

**Math-olympiad found**: For random non-commuting $D$ with $\lambda_{sep} = 0.5$, kernel destroyed (dim drops 4 → 0 in test case). So *commutation matters*.

### §2.5 Canonical Anchors

- **canonical §3.7**: Distinction operator definition (axiom level)
- **canonical §9.3**: Distinction candidate (specific provisional form)
- **canonical §13**: T-σ-Theorem-3 (Aut(G)-equivariance) — may imply specific commutation properties
- **V5b-T-zero (canonical L1328)**: Goldstone exact zero on translation-invariant graphs

---

## §3. Priority 3 Reference — SCC Dynamic Class Investigation

### §3.1 Hohenberg-Halperin Classification (1977)

| Model | Order parameter | Conservation | Equation | Dynamic exponent |
|---|---|---|---|---|
| **A** | Non-conserved scalar | None | $\partial_t \phi = -\delta H/\delta \phi + \eta$ | $z \approx 2.17$ (2D Ising) |
| **B** | Conserved scalar | $\int \phi$ conserved locally | $\partial_t \phi = \nabla^2 (\delta H/\delta \phi) + \nabla \cdot \eta$ | $z = 4 - \eta \approx 3.75$ (2D) |
| C | Coupled scalar + non-conserved | None | Mixed | varies |
| D | Coupled scalar + conserved | Magnetization | Mixed | varies |
| E-J | Various | Various | Various | Various |

### §3.2 SCC Dynamics Structure

SCC reflected Langevin SDE (T-PF-A1-SDE Cat A):
$$dU_t = -P_{T\Sigma_m} \nabla \mathcal{E}(U_t)\,dt + \sqrt{2T_*}\,P_{T\Sigma_m}\,dB_t + dK_t$$

Where:
- $P_{T\Sigma_m} = I - n^{-1}\mathbf{1}\mathbf{1}^T$ projector onto mean-zero subspace
- $K_t$ Skorokhod boundary local time
- $\sum u_i = m$ conserved (global, NOT local)

### §3.3 Cahn-Hilliard vs SCC 비교

**Continuum Cahn-Hilliard**:
$$\partial_t \phi = -\nabla^2(\varepsilon^2 \nabla^2 \phi - W'(\phi))$$
- Outer $-\nabla^2$ ensures *local mass conservation*
- Dispersion $\omega(q) = q^2 (\varepsilon^2 q^2 - |W''(c)|)$
- Coarsening $L(t) \sim t^{1/3}$

**SCC on graph**:
$$\partial_t u = -P_{T\Sigma_m} \nabla \mathcal{E}(u)$$
- $P_{T\Sigma_m}$ removes constant mode only — *not Laplacian application*
- Equivalent to Allen-Cahn + Lagrange multiplier
- Mass conservation is *global*, NOT *local*

**Key distinction**: SCC's $P$ ≠ Laplacian $L$. So SCC is *constrained Allen-Cahn (Rubinstein-Sternberg 1992)*, not Cahn-Hilliard.

### §3.4 Coarsening Crossover (Bray 1994)

For constrained AC:
- Early time: AC-like motion by mean curvature → $L(t) \sim (\alpha t / \beta)^{1/2}$
- Late time: mass redistribution dominates → LSW-like $L(t) \sim t^{1/3}$
- **Crossover at**: $\xi_{AC}(t_\times) = \xi_{CH}(t_\times)$ → $t_\times \sim \alpha/\beta$ (Bray §3-4 explicit, *Critic Pass 2*)

### §3.5 References (어제 §POST-SEAL APPENDIX 의 직접 인용)

- Hohenberg-Halperin (1977) *Rev. Mod. Phys.* 49:435
- Bray (1994) *Adv. Phys.* 43:357 — phase ordering kinetics
- Rubinstein-Sternberg (1992) *IMA J. Appl. Math.* 48:249 — non-local AC
- Allen-Cahn (1979) *Acta Metall.* 27:1085
- Lifshitz-Slyozov (1961) *J. Phys. Chem. Solids* 19:35

---

## §4. Anti-Goal Reference — 8 Retractions Explicit

본 day 에 *재시도 절대 금지*:

1. ❌ **EW universality**: SCC ≠ Edwards-Wilkinson (double-well + spinodal 불안정 linearization)
2. ❌ **Model A z=2.17**: mass conservation 으로 인해 Model B 가능성 (또는 SCC-specific)
3. ❌ **$t_\times \sim (\beta/\alpha)^{3/2}$**: Bray 1994 explicit → $t_\times \sim \alpha/\beta$
4. ❌ **$D_f^{(k)} = (n-1) - k$**: codim 산수 오류, k=0 시 ambient 전체
5. ❌ **H-int**: formation regime ($u_i \to 0, 1$) 배제, framework 재정식화 필요
6. ❌ **Closure RG-irrelevance**: tree-level only, loop 미증명
7. ❌ **$D_f = 11/8$ theorem**: SLE_3 continuum result, discrete SCC 에 미적용
8. ❌ **k(k+1)/2-1 single-graph stratification**: fixed graph 의 uniform $k_0$, graph moduli 에만 의미

---

## §5. Numerical Infrastructure (READ-ONLY scc/ 호출 가능)

본 day 에 *읽기만 가능* (수정 0):

| 모듈 | 용도 (READ-ONLY) |
|---|---|
| `scc/graph.py::GraphState` | Laplacian eigenvalue, Fiedler vector 추출 |
| `scc/graph.py::GraphState.grid_2d(L, L)` | 2D torus L×L 생성 |
| `scc/energy.py::EnergyComputer` | Hessian 계산 (Priority 2 의 commutation test) |
| `scc/operators.py` | distinction operator $D$ 의 함수 형태 |
| `scc/params.py` | $\alpha, \beta, c$ admissible range |
| `scc/langevin.py` | Reflected Langevin (필요 시 reference only) |

**호출 패턴 예**:
```python
from scc.graph import GraphState
g = GraphState.grid_2d(16, 16)
lambda_2 = g.lambda_2()  # 0.1522 expected
```

**제약**: pytest 재실행 가능 (관찰만, 결과 변경 없음), 코드 수정 금지.

---

## §6. Cat A/B Promotion Path (어제 Phase 14 산출)

| Claim | Current Cat | Path to Cat A |
|---|---|---|
| S1 ($c_G$) | Cat B conditional | (1) numerical verification (Priority 1) → (2) Kato perturbation for degenerate Fiedler |
| S2 (Distance-Poincaré) | Cat B target | S1 Cat A + BGL §4.2 Bakry-Émery |
| S3 (Kernel-mult identity) | Cat A minimal / Cat A conditional full | (1) $[D, L]$ commutation (Priority 2) → (2) full SCC Cat A unconditional 결정 |

**Path 1A**: Priority 1 numerical + analytic verification → S1 → S2 자동 promotion (~1-2 sessions)
**Path 1B**: Priority 2 commutation result → S3 full SCC promotion (1 session)

---

## §7. EOD Update 의 필수 포함 (99_summary 에 들어가야)

본 day 종료 시 99_summary 의 EOD update 에 반드시 들어갈 결과:

1. **$c_G$ 정확한 값** (Priority 1 결과)
2. **$[D, L_G]$ commute 여부** (Priority 2 결과)
3. **Dynamic class investigation** 진행 상태 (Priority 3)
4. **Cat status update**: S1, S3 의 Cat status 변화
5. **다음 세션 (W8-Day4) carry-forward**

---

## §8. EOD 메모 (작성자 → 사용자)

- 본 file 은 2026-05-20 morning 작성, 본 day 의 *verification task reference*
- 사용자 본 day 진입 시: ① Priority 1 ($c_G$) 부터 시작 권장, ② Priority 2 algebraic check 병행 가능, ③ Priority 3 은 시간 허락 시
- 본 file 은 *읽기용* — 본 day 검증 작업 시 *인용 출처*
- canonical / theorem_status / auxiliary_structures_master 어느 것도 *수정 없음*
- 본 day plan §G 의 verification 추가 항목: 본 01_pre_brainstorm.md §1-§3 reference 가 본 day 의 verification 작업에서 *실제 인용* 됐는지

**End of pre-brainstorm. 본 day verification 출발 위치 명확.**
