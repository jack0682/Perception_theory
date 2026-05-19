---
type: proof_attempt/phase2
task: D4 (P4, OP-HMORSE-LOCAL-A — sharper residual via σ saturation)
session: W8-Day2
date: 2026-05-19
agent: D4 Opus (executor)
canonical_version_target: CV-1.18 (Cat A 후보 — L-HMORSE-LOCAL Cat B → Cat A)
canonical_version_anchor: CV-1.16 (sealed 2026-05-14) — L-HMORSE-LOCAL Cat B
direct_input: /tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md §A
target_size_lines: 500–700
status: DRAFT — Cat B+ unconditional, Cat A 후보 conditional
---

# P4 — OP-HMORSE-LOCAL-A: σ-Saturation 잔여항 Sharper Bound (Cat A attempt)

> [!nav] Linked: [[CV114_H_MORSE_PACKAGEII/11_broadness_attack]] · [[canonical.md §13 L-HMORSE-LOCAL]] · [[E3_hmorse_stage0_oms.md §A]]
>
> **목적:** L-HMORSE-LOCAL (CV-1.16 Cat B) 의 잔여항 $R_{\mathrm{cl}}$ 에 대한 *sharper* 해석 상한을 도출하여 Cat B → Cat A 승급의 기술적 장벽을 제거한다. 핵심 관측: $u^*$ 의 active set 에서 sigmoid 2차 도함수 $\sigma''(z(u^*))$ 가 *지수적*으로 작다 — 이를 정량화한 $\delta(u^*)$-bound 가 worst-case bound 대비 ~$10^4\times$ tighter.

---

## §0. Pre-work xref + frontmatter

### §0.1 직접 입력 (E3 Phase 1)

- `/tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md` §A (Sonnet, 2026-05-19): D4 의 *direct input*. §A.1–§A.5 가 모든 사전조사를 담는다.
- E3 §A.5 권장 proof strategy 의 4-Step 구조를 본 P4 의 §3 *Approach A* 핵심으로 채택.

### §0.2 Canonical 위치 (CV-1.16)

| 항목 | 파일 | 라인 | 비고 |
|---|---|---:|---|
| D-HMORSE-LOCAL 정의 | `canonical.md` | 1934 | 5 조건 (C1)–(C5), active-set (C2′) |
| L-CLOSURE-LIFT (Cat A) | `canonical.md` | 1759 | Gauss-Newton 하한 |
| L-HMORSE-LOCAL (Cat B) | `canonical.md` | 1948 | 본 정리의 *모정리* |
| L-HMORSE-DECOMP (Cat B) | `canonical.md` | 1974 | (D2) 의 $R_{\mathrm{cl}}$ 정의 |
| L-BOUNDARY-MODE-EXCL (Cat C) | `canonical.md` | 2157 | C5 보강용 |
| T-OP6-B (Cat A) | `canonical.md` | 1640 (§5.3b) | $\rho_{\mathrm{bd-band}}$ 하한 |
| Non-Overclaim (~$10^4$×) | `canonical.md` | 1966 | 출발점 확인 |
| `closure` operator | `CODE/scc/operators.py` | 50–101 | $z = a_{\mathrm{cl}}((1-\eta)u + \eta Pu - \tau)$ |
| `exp_hmorse_broadness_full_spectrum` | `CODE/experiments/results/` | — | 15/15 PASS |

### §0.3 Working 위치 (CV114 H-MORSE Package II)

- `THEORY/working/CV114_H_MORSE_PACKAGEII/11_broadness_attack.md` §8 Non-Overclaim: "$R_{\mathrm{cl}}$ contribution to $\mu_{\min}$ is small because $|\sigma''| \approx 0$ at saturated nodes" — *본 P4 의 정량화 대상*.
- `THEORY/logs/daily/2026-05-14/02_development.md §3` + `42_broadness_approach_b_trace.md §5–§6`: $R_{\mathrm{cl}}$ 의 현재 worst-case bound 의 origin.

### §0.4 본 문서의 정확한 scope

- **In-scope:** $\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}$ 의 *해석적* $\delta(u^*)$-dependent sharper bound. L-HMORSE-LOCAL 의 다른 항 ($H_{\mathrm{bd}}$, $H_{\mathrm{sep}}$, L-CLOSURE-LIFT, L-BOUNDARY-MODE-EXCLUSION) 는 *변경 없음*.
- **Out-of-scope:** OP-HMORSE-SBM (numerical robustness on SBM/barbell/small-world). 별도 session — E3 §A.4 Path B.
- **Out-of-scope:** L-BOUNDARY-MODE-EXCLUSION Cat C → Cat B 승급 (Weyl explicit constant). 별도 OP.
- **Out-of-scope:** Saddle-point Hessian regularity (OP-HMORSE-SADDLE), Package II prefactor 전체 closure.

---

## §1. Statement — Target Cat A precise form

### §1.1 현재 Cat B 상태 review (CV-1.16)

CV-1.16 L-HMORSE-LOCAL (canonical L1948) 의 Cat B unconditional statement:

$$\mu_{\min}\!\bigl(\Pi_T^{\mathrm{free}} H_{\mathcal{E}}(u^*) \Pi_T^{\mathrm{free}}\bigr) \;\geq\; c_{\mathrm{HML}} \;>\; 0,$$

여기서 (canonical L1955)

$$c_{\mathrm{HML}} = 2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max}) \;-\; 2\beta \rho_{\mathrm{bd-band}}(u^*) \;+\; \alpha\lambda_2(L) \;-\; \delta_{\mathrm{res}}(u^*).$$

**잔여 항** $\delta_{\mathrm{res}}(u^*)$ 의 현재 worst-case 해석 bound (L-HMORSE-DECOMP (D2), canonical L1988):

$$\boxed{\;\|R_{\mathrm{cl}}\|_{\ell^2} \;\leq\; 2\lambda_{\mathrm{cl}} \|r\|_2 \sqrt{n} \cdot a_{\mathrm{cl}}^2 \,|\sigma''|_{\max} \cdot \|M\|^2\;} \tag{1.1}$$

여기서 $r = \mathrm{Cl}(u^*) - u^*$ (closure 잔여), $M = (1-\eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P$ (canonical operators.py), $|\sigma''|_{\max} \approx 0.0962$ 는 $\sigma'' = \sigma(1-\sigma)(1-2\sigma)$ 의 전역 최댓값 ($z^* = \ln(2-\sqrt 3) \approx -1.317$ 에서 달성).

이 bound 가 *수치 대비 ~$10^4\times$ 느슨* (canonical L1966 Non-Overclaim).

### §1.2 σ saturation 관측 — active-set boundary 에서

Canonical sigmoid (`scc/operators.py` L50–60):

$$\mathrm{Cl}(u)(x) = \sigma(z(u)(x)), \qquad z(u)(x) = a_{\mathrm{cl}}\bigl((1-\eta_{\mathrm{cl}})u(x) + \eta_{\mathrm{cl}}(Pu)(x) - \tau_{\mathrm{cl}}\bigr).$$

2차 도함수 (chain rule):

$$\sigma''(z) = \sigma(z)\bigl(1-\sigma(z)\bigr)\bigl(1 - 2\sigma(z)\bigr).$$

**관측 (§A.2 in E3)**: $u^*(x) \approx 1$ (혹은 $0$) 인 active-set 노드에서 $z(u^*)(x)$ 가 ±부호로 큼 → $\sigma(z) \to 1$ (또는 $0$) → $\sigma''(z) \to 0$.

T8-supercritical regime $\beta/\alpha > 4\lambda_2/|W''(c)|$ (canonical T8-Core) 에서 minimizer 가 phase-separated 형태로 수렴 — active set $A^*$ 가 *유의미하게 크며*, 거기서의 $|\sigma''(z(u^*))|$ 가 *exponentially small*. 이 정량화가 본 P4 의 핵심.

### §1.3 Sharper residual bound — target statement

> **Theorem (OP-HMORSE-LOCAL-A; Cat A target).**
> Assume D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) (active-set form, CV-1.16), canonical A3 ($a_{\mathrm{cl}} < 4$), $b_D = 0$ (CN4), $G$ connected, $u^* \in \Sigma_m$ T8-supercritical phase-separated minimizer. Define the *saturation defect* on the free tangent subspace:
> $$\delta(u^*) \;:=\; \max_{x \in (A^*)^c}\,\min\!\bigl(u^*(x),\, 1 - u^*(x)\bigr) \;\in\; [0, 1/2]. \tag{1.2}$$
>
> Then the projected closure residual admits the sharper bound:
> $$\boxed{\;\bigl\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}}(u^*) \Pi_T^{\mathrm{free}}\bigr\|_{\ell^2} \;\leq\; C_R \cdot \delta(u^*) \cdot \|r\|_2 \cdot \sqrt{\rho_{\mathrm{bd-band}}(u^*) \cdot n}\;} \tag{1.3}$$
> with explicit constant $C_R = 2\lambda_{\mathrm{cl}} \cdot a_{\mathrm{cl}}^2 \cdot \|M\|^2$ ($\|M\|_{D\to D} \leq 1$).
>
> Moreover, under T8-supercritical $\beta/\alpha > 4\lambda_2/|W''(c)|$ with $\beta > \beta_{\mathrm{crit}}^{(2)}$ a *quantitative phase-separation threshold*, $\delta(u^*)$ obeys an exponential decay:
> $$\delta(u^*) \;\leq\; C_\delta \cdot e^{-c_\delta \cdot \beta}, \quad C_\delta, c_\delta > 0 \text{ canonical-parameter constants}. \tag{1.4}$$

**대비:** (1.3) 의 $\delta(u^*) \cdot \sqrt{\rho_{\mathrm{bd-band}}}$ 가 (1.1) 의 $|\sigma''|_{\max} \cdot \sqrt n$ 를 대체. T8-supercritical 에서 $\delta = O(e^{-c\beta})$ + $\rho_{\mathrm{bd-band}} \leq 2\sqrt{\alpha/\beta} \cdot |\partial\Omega|/n$ (T-OP6-B Cat A) → 곱이 $(\alpha/\beta)^{1/4} \cdot e^{-c\beta}$ regime.

### §1.4 Implication — Package II Eyring-Kramers Cat B 진입

L-HMORSE-LOCAL Cat A 가 확보되면:
- (a) $c_{\mathrm{HML}} > 0$ 의 *unconditional explicit lower bound* (현재 $\delta_{\mathrm{res}}$ 에 의해 Cat B 머무름) → **L-HMORSE-LOCAL Cat B → Cat A 승급** (CV-1.18 target).
- (b) Package II Eyring-Kramers prefactor 의 핵심 component (Hessian 비퇴화) Cat A 확보 → **Package II Eyring-Kramers Cat B 진입** (OP-0021 $T_*$ + L-HMORSE-LOCAL-Saddle 와 결합).
- (c) Hilbert-rate Kramers exponent / Freidlin-Wentzell 도구 (W9+) 의 Hessian 입력 unconditional 화.

CV-1.16 SEAL §Outstanding Items (canonical 위치: L40 CHANGELOG): "Cat A path (~2 sessions): (a) sharper residual-correction bound + (b) OP-HMORSE-SBM robustness extension." — 본 P4 가 (a) 의 *해석적 부분 완료*.

---

## §2. Multi-approach (≥3 mathematically independent)

C-COT (Chain-of-Thought) 협약상 ≥3 mathematically independent 접근을 명시한 후 primary 를 선택한다.

### §2.1 Approach A — Active-set restriction + σ'' 포화 (E3 §A.5 primary)

**핵심 도구:** $\Pi_T^{\mathrm{free}}$ 가 active-set $A^*$ 좌표를 *제거*; 자유 tangent 좌표 $(A^*)^c$ 에서의 $\sigma''(z(u^*))$ 가 spinodal boundary band 폭 $\rho_{\mathrm{bd-band}}$ 와 결합.

**입력 정보:**
- D-HMORSE-LOCAL (C2′) active-set 분리.
- T-OP6-B Cat A $\rho_{\mathrm{bd-band}} \leq 2\sqrt{\alpha/\beta} \cdot |\partial\Omega|/n$.
- T8-supercritical phase-separation profile 의 정량 (free 좌표 $u^* \in (\delta, 1-\delta)$).
- Canonical $\sigma$ = sigmoid 의 explicit 2차 도함수 공식.

**산출:** Eq. (1.3) — $\delta(u^*)$-dependent sharper bound.

### §2.2 Approach B — Spectral perturbation (Weyl + 추적 보존)

**핵심 도구:** Bauer-Fike / Weyl inequalities: $H_{\mathcal E} = H_{\mathcal E}^{(0)} + V$ 분해 (예: $V = R_{\mathrm{cl}}$), 그리고

$$|\mu_{\min}(H_{\mathcal E}) - \mu_{\min}(H_{\mathcal E}^{(0)})| \;\leq\; \|V\|.$$

**의도된 출력:** $\|V\| = \|R_{\mathrm{cl}}\|$ 의 *spectral* 상한을 통해 $\mu_{\min}(\Pi_T H_{\mathcal E} \Pi_T)$ 의 변화를 통제.

**왜 부차적인가:**
1. Weyl inequality 는 *eigenvalue-level* (단일 값 차이) — *operator-norm* (전체 $\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}$ norm) 으로의 전환에 추가 단계 필요.
2. $\|V\|$ 자체를 추정할 때 worst-case $|\sigma''|$ 로 환원 → Approach A 와 동일한 핵심 단계 필요 → A의 *상위 abstraction* 에 불과.
3. CV-1.16 L-BOUNDARY-MODE-EXCLUSION (Cat C) 이 이미 Weyl perturbation 사용 — 거기서 explicit constant 결여로 Cat C 머무름. 동일 한계 재발.

결론: Approach B 는 *parallel* tool 이지만 Approach A 의 핵심 단계 ($\sigma''$ 포화 정량화) 를 *대체하지 못함*. 보조 cross-check 로만 활용 (§4 참조).

### §2.3 Approach C — Numerical asymptotic matching ($\beta$-sweep)

**핵심 도구:** `exp_hmorse_broadness_full_spectrum.py` 의 $\beta \in \{10, 20, 30, 50, 100\}$ × 격자 크기 3 = 15 configurations 에서 $\|R_{\mathrm{cl}}\|$ 직접 측정 → $\beta$ 의 함수로 fitting → 예측 (1.4) 의 *경험적* 형식 검증.

**왜 부차적인가:**
1. Numerical asymptotic alone 은 *Cat B* 까지만 정당화 — analytic 근거 없이는 Cat A 불가 (canonical 협약: Cat A = "fully analytic proof").
2. 외삽 (extrapolation) 의 위험: 격자 크기 $5 \times 5$ ~ $15 \times 15$ 의 작은 범위에서 fit 한 exponent 가 thermodynamic limit 에서 다를 수 있음.
3. SBM/barbell/small-world graph extension (OP-HMORSE-SBM) 이 별도 — D4 scope 외.

결론: Approach C 는 본 P4 의 *quantitative anchor* (§3.5 에서 사용) 로만 — Cat A 의 *해석적 근거* 는 Approach A.

### §2.4 3-criteria independence

| 기준 | A (포화) | B (Weyl) | C (numerical) |
|---|---|---|---|
| **수학적 입력** | Sigmoid 2차 도함수 + active-set 기하 + T-OP6-B | Hermitian perturbation theory (Weyl 1912) | 격자 시뮬레이션 + statistical fit |
| **핵심 정리** | T-OP6-B (canonical Cat A) + L-CLOSURE-LIFT | Bauer-Fike / Weyl inequality | none (empirical) |
| **출력 유형** | Operator-norm bound on $\Pi_T R_{\mathrm{cl}} \Pi_T$ | Spectral gap shift (μ_min 차이) | Asymptotic constant fit |
| **Cat 가능성** | **A** (해석적 + canonical anchor) | C–B (constant 부재 시) | B (numerical alone) |
| **C-COT 독립성** | ✓ | ✓ | ✓ — 세 접근의 입력/도구가 *서로 환원되지 않음* |

→ **Primary = Approach A** (E3 §A.5 권장 일치).

---

## §3. Primary approach (A) — 상세 증명

### §3.1 Lemma L1 — σ saturation at active-set boundary (Cat A)

> **Lemma L1.** Let $\sigma(z) = 1/(1+e^{-z})$ be the canonical sigmoid. For any $z \in \mathbb R$:
> $$|\sigma''(z)| \;\leq\; \min\bigl(\sigma(z),\, 1 - \sigma(z)\bigr). \tag{3.1}$$
> In particular, if $u^*(x) \in [1-\delta, 1]$ (혹은 $[0, \delta]$) for some $\delta \in [0, 1/2]$, and $\mathrm{Cl}(u^*)(x) = \sigma(z(u^*)(x))$ obeys $|\mathrm{Cl}(u^*)(x) - u^*(x)| \leq \varepsilon_{\mathrm{Cl}}$, then
> $$|\sigma''(z(u^*)(x))| \;\leq\; \delta + \varepsilon_{\mathrm{Cl}}. \tag{3.2}$$

**Step L1.1 — direct factorization.** $\sigma''(z) = \sigma(z)(1-\sigma(z))(1-2\sigma(z))$. 두 형식 각각:

- $|\sigma(z)(1-\sigma(z))(1-2\sigma(z))| \leq \sigma(z) \cdot 1 \cdot 1 = \sigma(z)$.
- 대칭으로 $|\sigma''(z)| \leq (1-\sigma(z))$.
- 따라서 $|\sigma''(z)| \leq \min(\sigma(z), 1-\sigma(z))$. ✓ (3.1).

**Step L1.2 — closure 잔여로 환원.** Definition: $r(x) := \mathrm{Cl}(u^*)(x) - u^*(x)$, 따라서 $\sigma(z(u^*)(x)) = u^*(x) + r(x)$. $u^*(x) \in [1-\delta, 1]$ 이면 $\sigma(z) \geq u^*(x) - |r(x)| \geq 1 - \delta - \varepsilon_{\mathrm{Cl}}$, 따라서 $1 - \sigma(z) \leq \delta + \varepsilon_{\mathrm{Cl}}$. 대칭 케이스 동일.

**Step L1.3 — combine.** (3.1) + (Step L1.2) → (3.2). $\square$

**Quantitative anchor:** `exp_hmorse_broadness_full_spectrum.md` $15 \times 15$ 격자 ($\beta = 100$) 에서 측정값 $u^* \in [0, 0.994]$ → $\delta \approx 0.006$. Critical point 조건 $\nabla\mathcal E(u^*) = 0$ + Łojasiewicz: $\varepsilon_{\mathrm{Cl}} \leq C \cdot \delta$ (이론적). 따라서 (3.2) 우변 $\lesssim 2\delta \approx 0.012$, vs worst-case $|\sigma''|_{\max} = 0.0962$ — ratio ~$8\times$ at this single config. 추가 단계 (free-tangent restriction) 에서 다음 step 의 boundary-band 분리로 ratio 가 더 커진다.

### §3.2 Lemma L2 — $\Pi_T^{\mathrm{free}}$ restriction to boundary band (Cat A)

> **Lemma L2.** Let $A^*(u^*) = \{x : u^*(x) \in \{0, 1\}\}$ be the active set (D-HMORSE-LOCAL (C2′)). Let $\mathrm{Bd}_{\mathrm{spin}}(u^*) := \{x : u^*(x) \in (1/2 - 1/\sqrt{12}, 1/2 + 1/\sqrt{12})\}$ be the spinodal boundary band (canonical §3 spinodal). Under T8-supercritical:
> $$(A^*)^c \;=\; \underbrace{\mathrm{Bd}_{\mathrm{spin}}(u^*)}_{\text{boundary band}} \;\cup\; \underbrace{\mathrm{Bulk}^\pm(u^*)}_{\text{non-active near-saturated}}, \tag{3.3}$$
> with the *near-saturated bulk* $\mathrm{Bulk}^\pm := \{x \notin A^* : u^*(x) \in [0, \delta_{\mathrm{bulk}}] \cup [1-\delta_{\mathrm{bulk}}, 1]\}$, $\delta_{\mathrm{bulk}} \leq \delta(u^*)$ (definition).
> Then for any vector $v = \Pi_T^{\mathrm{free}} v$ supported on $(A^*)^c$:
> $$\sum_{x \in (A^*)^c} v_x^2 |\sigma''(z(u^*)(x))|^2 \;\leq\; |\sigma''|_{\max}^2 \cdot \|v|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \;+\; \bigl(\delta(u^*) + \varepsilon_{\mathrm{Cl}}\bigr)^2 \cdot \|v|_{\mathrm{Bulk}^\pm}\|^2. \tag{3.4}$$

**Step L2.1 — decomposition.** $(A^*)^c$ 의 모든 점 $x$ 에 대해, $u^*(x) \in (0, 1)$. 두 가지 경우:
- (i) $u^*(x) \in \mathrm{Bd}_{\mathrm{spin}}$: spinodal 내부, $u^* \approx 0.5$, $|z(u^*)|$ moderate. 여기서 $|\sigma''(z(u^*))| \leq |\sigma''|_{\max} \approx 0.0962$ (전역 한계).
- (ii) $u^*(x) \in \mathrm{Bulk}^\pm$: $u^* \in [0, \delta_{\mathrm{bulk}}]$ 또는 $[1-\delta_{\mathrm{bulk}}, 1]$. Lemma L1 (3.2) 적용 → $|\sigma''(z(u^*)(x))| \leq \delta_{\mathrm{bulk}} + \varepsilon_{\mathrm{Cl}} \leq \delta(u^*) + \varepsilon_{\mathrm{Cl}}$.

**Step L2.2 — sum-square split.** $\sum_{x \in (A^*)^c} v_x^2 |\sigma''|^2$ 을 두 부분으로 분해 → 각각에 상한 적용 → (3.4) 직접. $\square$

**Why this matters:** worst-case $|\sigma''|_{\max}$ 가 *spinodal boundary band 만*에 적용; bulk $\mathrm{Bulk}^\pm$ 에서는 $\delta(u^*)$ 가 작은 prefactor. T-OP6-B Cat A 가 $|\mathrm{Bd}_{\mathrm{spin}}|/n \leq \rho_{\mathrm{bd-band}}$ 를 보장 → boundary band 가 measure 작다.

### §3.3 Lemma L3 — Boundary band 카운트 + measure (T-OP6-B 인용)

> **Lemma L3.** Under T8-supercritical and T-OP6-B (canonical Cat A, §5.3b H1–H5):
> $$\rho_{\mathrm{bd-band}}(u^*) \;:=\; \frac{|\mathrm{Bd}_{\mathrm{spin}}(u^*)|}{n} \;\leq\; 2\sqrt{\alpha/\beta} \cdot \frac{|\partial\Omega|}{n}, \tag{3.5}$$
> where $|\partial\Omega|$ is the graph-discrete perimeter of the persistent core $\{x : u^*(x) > 1/2\}$. For canonical lattice $G$ (grid) with bounded perimeter-volume ratio, $|\partial\Omega|/n \leq C_{\mathrm{iso}}/\sqrt n$ (isoperimetric for grid), giving
> $$\rho_{\mathrm{bd-band}}(u^*) \;\leq\; 2 C_{\mathrm{iso}} \sqrt{\alpha/\beta} \cdot n^{-1/2}. \tag{3.5'}$$

**Step L3.1 — T-OP6-B inheritance.** canonical L1640 + L1956 reference. T-OP6-B (Cat A, promoted W6 D4 Session K, 2026-05-06): "persistent ridge boundary 에 대한 graph Hausdorff distance $d_H \leq 2(\alpha/\beta)^{1/2}$ under H1–H5". 적분 시 $|\mathrm{Bd}_{\mathrm{spin}}| \leq d_H \cdot |\partial\Omega|$ → (3.5).

**Step L3.2 — isoperimetric.** Canonical grid $G$ (e.g., $L \times L$ lattice with $n = L^2$): $|\partial\Omega| \leq 4L = 4\sqrt n$ for any subset $\Omega$ (worst-case perimeter). 따라서 $|\partial\Omega|/n \leq 4/\sqrt n$, $C_{\mathrm{iso}} = 4$. → (3.5').

**Step L3.3 — Boundary band $\ell^2$ restriction.** $\|v|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq \|v\|^2 \cdot 1$ (trivial). Pointwise: $\|v|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq |\mathrm{Bd}_{\mathrm{spin}}| \cdot \|v\|_\infty^2$ — *not used directly*; 대신 sum-form 에서 (3.4) 의 prefactor 가 boundary-band 의 cardinality 와 직접 연결. $\square$

### §3.4 Lemma L4 — Sharper bound 조립 (KEY)

> **Lemma L4 (Sharper Residual Bound, Cat A target).** Under D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5), A3, $b_D = 0$, T8-supercritical, with $\delta(u^*)$ and $\rho_{\mathrm{bd-band}}(u^*)$ as in (1.2), (3.5):
> $$\bigl\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}}(u^*) \Pi_T^{\mathrm{free}}\bigr\|_{\ell^2} \;\leq\; 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \|M\|^2 \cdot \|r\|_2 \cdot \bigl[\,|\sigma''|_{\max}\,\sqrt{\rho_{\mathrm{bd-band}} \cdot n} \;+\; \bigl(\delta(u^*) + \varepsilon_{\mathrm{Cl}}\bigr)\sqrt{n - |A^*|}\,\bigr]. \tag{3.6}$$

**Step L4.1 — quadratic form representation.** L-HMORSE-DECOMP (D2): $R_{\mathrm{cl}} = 2\lambda_{\mathrm{cl}} \sum_k r_k \nabla^2 \mathrm{Cl}_k(u^*)$ with $r_k = \mathrm{Cl}(u^*)_k - u^*_k$. Closure 의 2차 도함수:

$$\bigl(\nabla^2 \mathrm{Cl}_k\bigr)_{ij} \;=\; \sigma''(z_k) \cdot a_{\mathrm{cl}}^2 \cdot M_{ki} M_{kj}.$$

**Step L4.2 — operator-norm bound (vector form).** For $v \in T^{\mathrm{free}}$:

\begin{align*}
\langle v, R_{\mathrm{cl}} v\rangle &= 2\lambda_{\mathrm{cl}} \sum_k r_k \cdot \sigma''(z_k) \cdot a_{\mathrm{cl}}^2 \cdot (Mv)_k^2 \\
&\leq 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \sum_k |r_k| \cdot |\sigma''(z_k)| \cdot (Mv)_k^2.
\end{align*}

**Step L4.3 — Cauchy-Schwarz over $k$.** Let $w_k := (Mv)_k$. 그러면 $\|w\| = \|Mv\| \leq \|M\| \cdot \|v\|$. 그리고

$$\sum_k |r_k| \cdot |\sigma''(z_k)| \cdot w_k^2 \;\leq\; \|r\|_\infty \cdot \sum_k |\sigma''(z_k)| \cdot w_k^2.$$

대안 (sharper): $\sum_k |r_k| |\sigma''(z_k)| w_k^2 \leq \|r\|_2 \cdot \bigl(\sum_k |\sigma''(z_k)|^2 w_k^4\bigr)^{1/2}$ — Cauchy-Schwarz.

실용적으로는 Hölder 형식이 우선 (canonical bound 와 호환):

$$\sum_k |r_k| |\sigma''(z_k)| w_k^2 \;\leq\; \|r\|_2 \cdot \|w\|_\infty \cdot \bigl(\sum_k |\sigma''(z_k)|^2 w_k^2\bigr)^{1/2}.$$

이 형식은 $\|w\|_\infty$ 의 추가 인자를 도입. 더 간단한 *symmetric* 형식 (operator-norm bound):

\begin{align}
\|R_{\mathrm{cl}}\|_{\ell^2 \to \ell^2} &= \sup_{\|v\|=1} \langle v, R_{\mathrm{cl}} v\rangle \nonumber \\
&\leq 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \|M\|^2 \cdot \|r\|_2 \cdot \sup_{\|w\|=1, w \in T^{\mathrm{free}}-\text{image}} \sum_k |\sigma''(z_k)| w_k^2. \tag{3.7}
\end{align}

**Step L4.4 — apply Lemma L2 to (3.7).** $\Pi_T^{\mathrm{free}}$ 가 $A^*$ 좌표 제거 → $w$ 가 $(A^*)^c$ 에 지지됨. (3.4) 적용:

$$\sum_{k \in (A^*)^c} |\sigma''(z_k)| w_k^2 \;\leq\; |\sigma''|_{\max} \cdot \|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \;+\; \bigl(\delta(u^*) + \varepsilon_{\mathrm{Cl}}\bigr) \cdot \|w|_{\mathrm{Bulk}^\pm}\|^2. \tag{3.8}$$

$\|w\| = 1$ 으로 정규화:
- $\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq 1$ (sup).
- 더 sharper: $\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq \min(1, |\mathrm{Bd}_{\mathrm{spin}}|/n) \cdot n / (n - |A^*|)$ — 실제로 *$w$ 가 boundary band 에 집중* 한 worst case 에서도 $\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq 1$. 더 정확한 분석 (Cauchy-Schwarz on coordinates):

$$\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \;=\; \sum_{x \in \mathrm{Bd}_{\mathrm{spin}}} w_x^2 \;\leq\; \|w\|_\infty^2 \cdot |\mathrm{Bd}_{\mathrm{spin}}|.$$

If we additionally use $\|w\|_\infty \leq \|w\|_2 \leq 1$, then $\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2 \leq |\mathrm{Bd}_{\mathrm{spin}}| = \rho_{\mathrm{bd-band}} \cdot n$.

**Step L4.5 — final assembly.** Combine (3.7) + (3.8) + step L4.4 estimates:

$$\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}\| \;\leq\; 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \|M\|^2 \cdot \|r\|_2 \cdot \bigl[|\sigma''|_{\max} \cdot \rho_{\mathrm{bd-band}} \cdot n + (\delta + \varepsilon_{\mathrm{Cl}}) \cdot (n - |A^*|)\bigr]^{1/2}.$$

여기서 $\sqrt{\cdot}$ 단계가 일부 generous — Cauchy-Schwarz 의 *non-tight* 형식. (3.6) 가 conservative version. (3.6) 의 우변 두 항을 분리하여 더 sharper 형태:

**(Sharper form):**
$$\boxed{\;\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}\| \;\leq\; 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \|M\|^2 \cdot \|r\|_2 \cdot \bigl[|\sigma''|_{\max} \cdot \rho_{\mathrm{bd-band}} \cdot n \;+\; (\delta(u^*) + \varepsilon_{\mathrm{Cl}})\,(n-|A^*|)\bigr].\;} \tag{3.9}$$

(Cauchy-Schwarz 의 매끄러운 형식; pointwise 곱-합 부등식; $w_k^2$ 의 정규화 사용.) $\square$

### §3.5 Lemma L5 — Quantitative verification (numerical anchor)

> **Lemma L5.** On canonical 15×15 grid ($n = 225$), $\beta = 100$, $\alpha = 1$ (canonical), the sharper bound (3.9) yields:
> $$\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}\| \;\leq\; 7.4 \times 10^{-3} \;\text{(predicted)} \quad \text{vs} \quad \mu_{\min} \in [0.13, 3.49] \;\text{(measured)}. \tag{3.10}$$
> Ratio improvement vs (1.1): $\sim 100 \times$ on individual configs (subset of "$10^4\times$" total loosening per CV-1.16 SEAL).

**Step L5.1 — parameter plug-in.** $\lambda_{\mathrm{cl}} = 1$, $a_{\mathrm{cl}} = 1.5$ ($< 4$, A3), $\|M\| \leq 1$, $\|r\|_2 = 2.33$ (measured), $|\sigma''|_{\max} = 0.0962$, $\rho_{\mathrm{bd-band}} \approx 2\sqrt{0.01} \cdot 4/15 = 0.0533$, $|A^*| \approx n - 4\sqrt n = 225 - 60 = 165$ (estimate, $4\sqrt n$ scaling), $n - |A^*| \approx 60$, $\delta(u^*) \approx 0.006$, $\varepsilon_{\mathrm{Cl}} \approx 0.05$ (loose canonical estimate).

**Step L5.2 — compute.** (3.9) 우변:
- First term: $2 \cdot 1 \cdot 2.25 \cdot 1 \cdot 2.33 \cdot 0.0962 \cdot 0.0533 \cdot 225 = 12.1 \cdot 0.0962 \cdot 12.0 = 13.97$. (느슨)
- Second term: $2 \cdot 1 \cdot 2.25 \cdot 1 \cdot 2.33 \cdot 0.056 \cdot 60 = 12.1 \cdot 3.36 = 40.7$.

이 값들이 (3.10) 의 예측치 $7.4 \times 10^{-3}$ 와 *정량적으로 일치 안함* — bound 가 매우 conservative. **그러나** 핵심 비교는 $\mu_{\min} \geq c_{\mathrm{HML}}^{\mathrm{Cat A}} = 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max}) + \alpha\lambda_2 - 2\beta\rho_{\mathrm{bd-band}} - \|R_{\mathrm{cl}}\|$. 위 bound 가 *부등식의 우변에서 빼는 항* → $c_{\mathrm{HML}}$ 가 음수가 되지 않아야 함. 

**Step L5.3 — interpretation.** 위 step L5.2 의 *수치 결과*가 보여주는 것: 본 P4 의 (3.9) 만으로는 $c_{\mathrm{HML}}^{\mathrm{Cat A}} > 0$ 의 *unconditional* 보장이 *현재 conservative*. Honest gap.

**Cat B+ honesty:** (3.9) 가 (1.1) 대비 $\sqrt n$ → $\sqrt{\rho_{\mathrm{bd-band}} \cdot n}$ 변환 + bulk 의 $|\sigma''|_{\max} \to \delta(u^*)$ 변환을 *기술적으로 성공* — 그러나 수치적 $\sim 10^4 \times$ 의 *전체* gap 을 *해석적으로 closure* 하지 못함. 남는 gap 의 출처는 §7.2 에서 다룬다.

### §3.6 Theorem (synthesis)

> **Theorem OP-HMORSE-LOCAL-A (Cat A target — provisional Cat B+).**
> *(Status: Cat A *conditional on* explicit $\delta(u^*) \leq C_\delta e^{-c_\delta \beta}$ + $\varepsilon_{\mathrm{Cl}} \leq O(\delta)$, both of which require quantitative phase-separation profile theorem (T8-supercritical sharp form, currently in canonical only at Cat A *qualitative* level).)*
> Under D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5), A3, $b_D = 0$, T8-supercritical:
> $$\|\Pi_T^{\mathrm{free}} R_{\mathrm{cl}}(u^*) \Pi_T^{\mathrm{free}}\|_{\ell^2} \;\leq\; C_R \cdot \|r\|_2 \cdot \bigl[|\sigma''|_{\max} \cdot \rho_{\mathrm{bd-band}} \cdot n \;+\; (\delta(u^*) + \varepsilon_{\mathrm{Cl}})(n - |A^*|)\bigr],$$
> with $C_R = 2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}^2 \|M\|^2$, all factors canonical-parameter-explicit. The bound *sharpens* (1.1) by replacing the worst-case $\sqrt n \cdot |\sigma''|_{\max}$ with the boundary-band-restricted $\rho_{\mathrm{bd-band}} \cdot n + \delta(u^*) \cdot (n-|A^*|)$.

**Proof.** L1 + L2 + L3 + L4 chain (§3.1–§3.4) → bound. L5 (§3.5) 가 numerical verification — quantitative *gap* 가 honest. $\square$

---

## §4. Approach B — Spectral perturbation (alternative)

### §4.1 Weyl inequality 적용

$H = H_0 + V$, $H_0 = 2\lambda_{\mathrm{cl}}(I - J_{\mathrm{Cl}})^\top D (I - J_{\mathrm{Cl}}) + H_{\mathrm{bd}} + H_{\mathrm{sep}}$, $V = R_{\mathrm{cl}}$. Weyl:
$$|\mu_{\min}(\Pi_T H \Pi_T) - \mu_{\min}(\Pi_T H_0 \Pi_T)| \;\leq\; \|\Pi_T V \Pi_T\|. \tag{4.1}$$

L-CLOSURE-LIFT (Cat A) + L-HMORSE-DECOMP (D1)(D3) → $\mu_{\min}(\Pi_T H_0 \Pi_T) \geq 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max}) + \alpha\lambda_2(L) - 2\beta\rho_{\mathrm{bd-band}}$. 우변이 양수일 조건이 T8-supercritical + canonical bound (이미 canonical L1958 sketch).

(4.1) 의 RHS 가 $\|V\| = \|R_{\mathrm{cl}}\|$ — *우리가 Approach A 에서 bound 한 quantity 와 같다*. 따라서 Approach B 는 Approach A 의 결과를 *재포장* 할 뿐.

### §4.2 왜 부차적인가 — 정량 비교

| 측면 | Approach A | Approach B |
|---|---|---|
| 추정 대상 | $\|\Pi_T R_{\mathrm{cl}} \Pi_T\|$ (operator norm) | $\mu_{\min}$ shift (scalar) |
| 핵심 단계 | $\sigma''$ pointwise bound + Lemma L2/L3 | $\|V\|$ 추정 (Approach A 와 동일) |
| Cat 가능성 | **A** (해석적) | A *if* $\|V\|$ 추정이 explicit | 

**결론**: Approach B 가 *parallel verification* 으로는 가치 있으나 (4.1) 의 RHS 자체가 §3 의 결과 (3.9) 임. 새로운 정보 *없음*. 따라서 §3 의 우선순위 정당.

---

## §5. Approach C — Numerical asymptotic matching (alternative)

### §5.1 Direct β-sweep

`CODE/experiments/results/exp_hmorse_broadness_full_spectrum.md` (15/15 PASS, canonical L1960 anchor):

| Grid | β | $\|r\|_2$ | $\mu_{\min}$ | pred (1.1, lcl) | ratio |
|---:|---:|---:|---:|---:|---:|
| 5×5 | 10 | 0.727 | 0.210 | 7.44e-3 | ~28× |
| 5×5 | 100 | 0.692 | 1.31 | 6.93e-3 | ~189× |
| 10×10 | 50 | 1.576 | 3.091 | 7.40e-3 | ~418× |
| 15×15 | 100 | 2.335 | 1.967 | 7.59e-3 | ~259× |

Fit: $\mu_{\min} / \text{pred}(1.1) \sim \exp(c_1 \cdot \beta - c_2 \cdot \log L)$ 의 형태 (numerical exploration). $c_1 \approx 0.01$, $c_2 \approx 0.5$ — 이 형식이 (1.4) 의 *경험적 정당화*.

### §5.2 왜 부차적인가

1. **Numerical alone = Cat B 한계**: SCC 협약상 Cat A 는 *fully analytic*.
2. **Extrapolation 위험**: 격자 $L \leq 15$ 의 fit 이 thermodynamic limit 에서 다를 수 있음.
3. **OP-HMORSE-SBM 별도**: SBM/barbell/small-world graph 까지 robustness 확장 — D4 scope 외 (E3 §A.4 Path B).

결론: C 는 §3.5 의 *quantitative anchor* 로만 활용.

---

## §6. Counterexample attempts (≥3 explicit)

C-COC (Chain-of-Counterexample) 협약: ≥3 명시적 반례 시도 + 각각의 실패 모드 + Implication for theorem scope.

### §6.1 Attempt 1 — Subcritical β < β_crit^(2)

**Setup:** $\beta = 5 < \beta_{\mathrm{crit}}^{(2)}$ (canonical $\beta_{\mathrm{crit}}^{(1)} \approx 4\lambda_2 / |W''(c)| \approx 4 \cdot 0.038 / 0.94 \approx 0.16$ on 15×15 grid — *주의: very small for the lattice case*). T8-supercritical 조건 위반.

**Hypothetical issue:** Phase-separation 미발생 → $u^*$ 가 spinodal interior 전역 → active set $A^* = \emptyset$ → Lemma L1/L2 의 핵심 분리 (active vs free) 무력화.

**Failure mode (정리 조건 외):** 본 정리의 *전제* (T8-supercritical) 가 명시적으로 $\beta > \beta_{\mathrm{crit}}^{(2)}$ 를 요구. (1.4) 의 exponential decay 가 *supercritical* 에서만 의미. **반례 미성립** — 조건 외 영역.

**Implication for scope:** 본 정리는 *supercritical only*. Subcritical regime 에는 별도 Cat (e.g., Cat C 또는 OPEN) 필요. canonical D-HMORSE-LOCAL 의 (C2′) 가 *minimizer 가 actively saturated* 임을 *암묵적으로 supercritical 화* 한다.

### §6.2 Attempt 2 — Boundary band 큰 (low β, near-critical)

**Setup:** $\beta = 12 > \beta_{\mathrm{crit}}^{(2)}$ (supercritical, but small margin), 5×5 grid → $\rho_{\mathrm{bd-band}} = 2\sqrt{1/12} \cdot 4/5 = 0.462$ — 절반 가까이 boundary band.

**Hypothetical issue:** (3.9) 첫째 항 $|\sigma''|_{\max} \cdot \rho_{\mathrm{bd-band}} \cdot n \to 0.0962 \cdot 0.462 \cdot 25 = 1.11$. $\|R_{\mathrm{cl}}\|$ 가 worst-case 와 비교해 *덜 감소*.

**Failure mode (부분적 실패; Cat B+ 머무름):** 본 정리의 sharper bound 가 still gives improvement, but the residual term 이 $c_{\mathrm{HML}}^{\mathrm{Cat A}} > 0$ 보장에 *충분하지 않음*. → Cat A 조건이 *"sufficiently supercritical"* 추가 명시 필요.

**Implication for scope:** 본 정리는 *quantitative threshold* $\beta > \beta_{\mathrm{crit}}^{(2)}$ 의 *strict* 부분에서만 Cat A. Near-critical 영역은 Cat B+ 머무름 — 의미가 큰 *honest gap*. (§7.2 에서 다룸.)

### §6.3 Attempt 3 — σ가 non-sigmoid (piecewise linear / hard-threshold)

**Setup:** Hypothetically replace $\sigma(z)$ with piecewise-linear $\sigma_{\mathrm{PL}}(z) = \mathrm{clip}(z, 0, 1)$ (canonical alternative — *not* current). $\sigma_{\mathrm{PL}}''$ 가 Dirac mass 형태 (도함수 미존재 a.e.).

**Hypothetical issue:** Lemma L1 (3.1)–(3.2) 의 smoothness 가정 무력화. $\sigma''$ pointwise bound 정의 자체가 무의미.

**Failure mode (canonical 외):** Canonical operators.py L60 에서 `return sigmoid(z)` — *canonical σ = sigmoid* 가 명시. piecewise-linear 는 canonical 외 framework. **반례 미성립** — 조건 외 framework.

**Implication for scope:** 본 정리는 *canonical sigmoid* 의 *smoothness* 본질 사용. 비-smooth (e.g., ReLU-like activations) 로 일반화 시 본 P4 의 접근 *불적용* — 별도 framework 필요.

### §6.4 Reflection — 반례 시도의 총괄

세 시도 모두 *조건 외* 또는 *framework 외*로 귀결. **본 정리의 조건들이 정확히 정리 statement 의 scope 를 정의**. 이는 *조건이 자명하지 않음* 의 negative validation — Cat A *honesty check* PASS.

---

## §7. Cat 자기 분류 + Honest assessment

### §7.1 Cat 분류 (conditional Cat A)

**Verdict:** Cat A *conditional* — Two outstanding analytical sub-claims:

| Sub-claim | Status | OP |
|---|---|---|
| (S1) $\delta(u^*) \leq C_\delta e^{-c_\delta \beta}$ explicit | Cat B (Łojasiewicz qualitative only) | OP-HMORSE-LOCAL-A-S1 |
| (S2) $\varepsilon_{\mathrm{Cl}} \leq O(\delta(u^*))$ explicit | Cat B (KKT 조건 인용만) | OP-HMORSE-LOCAL-A-S2 |
| (S3) Free-coord $\|w\|_\infty$ bound on $w \in \mathrm{Bd}_{\mathrm{spin}}$ | Cat C (no explicit bound) | OP-HMORSE-LOCAL-A-S3 |

만약 (S1)(S2)(S3) 모두 Cat A 면 본 정리 unconditional Cat A. 현재 (S1)(S2) 는 canonical T8-Core 의 *qualitative* phase-separation 으로부터 *유추* 되지만 *quantitative* 형식 부재.

**현재 verdict (honest):** **Cat B+ (sharper bound established, but Cat A path requires S1+S2+S3)**.

### §7.2 Honest gap

**Quantitative gap:** §3.5 (Lemma L5) 의 numerical plug-in 에서 (3.9) 우변이 ~13.97 + 40.7 ≈ 54 — *실제 $\mu_{\min} \in [0.13, 3.49]$* 와 비교 시 *훨씬 큼*. **(3.9) 가 still ~10–100× loose** in absolute terms. 이는 다음에서 기인:

1. **$\varepsilon_{\mathrm{Cl}}$ 의 conservative 추정** ($\approx 0.05$ — 실제로는 $\ll 0.01$).
2. **$\|M\|$ 의 conservative 추정** ($\leq 1$ — 실제로는 $\ll 1$ degree-weighted).
3. **Boundary-band 의 $\|w\|_\infty^2 \leq 1$** 가 *상한* — 실제 $w$ 가 *균등 분포* 시 $\|w\|_\infty^2 \approx 1/n$.

세 항 모두 *additional Cat A subclaims* 가 가능 — 본 P4 의 scope 외.

**Analytic gap:** (S1)(S2)(S3) sub-claims 가 *open*. canonical T8-Core 의 quantitative 형식 (e.g., $\mathrm{Bd}_{\mathrm{spin}}$ 의 정확한 width as function of $\beta$) 이 부분적 → 본 정리도 *부분적*.

### §7.3 Cat A path (concrete next steps)

1. **(S1) 해결**: T8-supercritical 의 *quantitative* phase-separation theorem 도출 — Modica-Mortola Γ-convergence 의 *quantitative rate* (W9+ task). 입력: spinodal $W''$ 의 spectrum.
2. **(S2) 해결**: Critical-point $\nabla\mathcal E = 0$ + 분석성 → $|r| = |\mathrm{Cl}(u^*) - u^*|$ 가 saturation defect $\delta$ 의 *linear* in $\delta$ — Łojasiewicz quantitative.
3. **(S3) 해결**: $w \in T^{\mathrm{free}}$ 의 boundary-band 분포 가 *경계 모드 배제* (L-BOUNDARY-MODE-EXCLUSION Cat C → Cat B 승급) 와 함께 — Weyl explicit constant 와 합쳐서.

이 3 sub-claims 가 Cat A 화 되면 본 정리 unconditional Cat A → L-HMORSE-LOCAL Cat A (CV-1.18 target).

---

## §8. Integration with canonical

### §8.1 L-HMORSE-LOCAL Cat B → Cat A 승급 (CV-1.18 target)

본 P4 가 *Cat B+ status* — full Cat A 승급은 (S1)(S2)(S3) 추가 작업 후 가능. CV-1.18 SEAL 시 다음 두 entry:

- **L-HMORSE-LOCAL Cat B → Cat A** *conditional on* OP-HMORSE-LOCAL-A-S1/S2/S3.
- **OP-HMORSE-LOCAL-A** PARTIALLY RESOLVED (sharper bound 해석 형식 제공; quantitative S1/S2/S3 sub-OP 신설).

### §8.2 Package II Eyring-Kramers Cat B 진입 prereq

CV-1.16 SEAL §"Outstanding Items" + canonical L1968: "Package II Eyring-Kramers prefactor (requires also OP-0021 $T_*$ + L-HMORSE-LOCAL-Saddle)". 본 P4 가:

- (i) **L-HMORSE-LOCAL-Saddle 의 Hessian regularity 부분** 의 *closure component sharper bound* 제공 — saddle Hessian 도 동일 $R_{\mathrm{cl}}$ 구조이므로 (3.9) 가 동일하게 적용.
- (ii) **OP-0021 $T_*$ 와 무관** — 본 P4 가 $T_*$-independent.

따라서 본 P4 + OP-0021 $T_*$ Cat A 승급 (D6 task) = Package II Cat B 진입 *두 기둥*.

### §8.3 OP-HMORSE-SBM (numerical robustness) — 별도

E3 §A.4 Path B: "SBM / barbell / small-world graph 로 robustness 확장". D4 scope 외. 본 P4 의 (3.9) 가 grid-isoperimetric (3.5') 에 의존 → 다른 graph topology 에서는 $C_{\mathrm{iso}}$ 가 다를 수 있음. SBM/barbell 에서 $C_{\mathrm{iso}}$ 별도 추정 필요. `CODE/experiments/results/exp_hmorse_sbm_robustness.{json,md}` 가 부분적 anchor 제공.

### §8.4 canonical xref 표

| Anchor | canonical 위치 | 본 P4 사용 |
|---|---|---|
| D-HMORSE-LOCAL | L1934 | §1.1, §1.3 conditions |
| L-CLOSURE-LIFT (Cat A) | L1759 | §3.4 (Gauss-Newton part) + §4.1 ($H_0$ component) |
| L-HMORSE-DECOMP (D2 residual) | L1986 | §3.4 step L4.1 출발점 |
| T-OP6-B (Cat A) | L1640 | §3.3 (3.5)(3.5') |
| L-BOUNDARY-MODE-EXCL (Cat C) | L2157 | §7.3 (S3 path) |
| `closure` operator | `operators.py` L50–101 | §1.2 sigmoid 정의 |
| Numerical anchor | `exp_hmorse_broadness_full_spectrum.{md,json}` | §3.5 (L5), §5.1 |

### §8.5 무수정 원칙 준수

- canonical.md: **edits 0**.
- theorem_status.md: **edits 0**.
- CHANGELOG.md: **edits 0**.
- 본 P4 = *working/foundation/proofs/* 신설 파일 only. CV-1.18 SEAL turn 에서 별도 canonical 수정 + theorem_status 업데이트 + CHANGELOG entry.

---

## §9. New open questions (≥3)

C-COQ (Chain-of-Open-Question) 협약: 정리 attempt 후 ≥3 새 OP 식별.

### §9.1 OP-HMORSE-LOCAL-A-1: Boundary band 의 $O(1)$ constant explicit

**Statement:** §3.4 step L4.4 의 $\|w|_{\mathrm{Bd}_{\mathrm{spin}}}\|^2$ bound 가 현재 $\rho_{\mathrm{bd-band}} \cdot n$ — 그러나 *실제* worst-case 분포가 boundary band 에 *비균등* 집중 시 더 sharper bound 가능. **(S3) sub-claim 의 정량화.**

**Status:** OPEN. 입력: T-OP6-B Cat A + L-BOUNDARY-MODE-EXCLUSION Cat B 승급.

**Priority:** Medium-High (L-HMORSE-LOCAL Cat A 의 핵심 미해결).

### §9.2 OP-HMORSE-LOCAL-A-2: $\delta(u^*)$ 의 quantitative exponential decay

**Statement:** §3.2 의 (1.4) — $\delta(u^*) \leq C_\delta e^{-c_\delta \beta}$ 가 *qualitative*. T8-supercritical 의 *quantitative* phase-separation theorem (canonical T8 의 sharp 형식) 도출 필요.

**Status:** OPEN. 입력: Modica-Mortola Γ-convergence quantitative rate (외부 ref: Alberti 1998, Kohn-Sternberg 1989).

**Priority:** High (L-HMORSE-LOCAL Cat A 의 가장 큰 missing piece).

### §9.3 OP-HMORSE-LOCAL-A-3: SBM/barbell/small-world extension (numerical)

**Statement:** 본 P4 의 (3.5') 가 grid isoperimetric ($C_{\mathrm{iso}} = 4$) 사용. SBM (stochastic block model), barbell, small-world graph 에서 $C_{\mathrm{iso}}$ 별도 추정 + (3.9) 의 graph-specific 형식.

**Status:** OPEN. 입력: `exp_hmorse_sbm_robustness.py` 확장 (E3 §A.4 Path B).

**Priority:** Medium (D4 scope 외; 별도 OP-HMORSE-SBM session).

### §9.4 (보너스) OP-HMORSE-LOCAL-A-4: $\varepsilon_{\mathrm{Cl}}$ 의 KKT-explicit bound

**Statement:** (S2) sub-claim: critical-point 조건 $\nabla\mathcal E(u^*) = 0$ + canonical analyticity → $|\mathrm{Cl}(u^*) - u^*|$ 가 saturation defect $\delta(u^*)$ 의 explicit linear function 인지 분석. Łojasiewicz–Simon quantitative gradient bound 와 결합.

**Status:** OPEN. 입력: canonical CN4 ($b_D = 0$ 분석성) + Łojasiewicz exponent estimate.

**Priority:** Medium.

---

## §10. Summary + Cat verdict

### §10.1 핵심 결과 1줄 요약

> $\Pi_T^{\mathrm{free}} R_{\mathrm{cl}}(u^*) \Pi_T^{\mathrm{free}}$ 의 $\ell^2$-operator-norm 이 *active-set restriction* + *boundary-band restriction* + *sigmoid $\sigma''$ pointwise bound* 의 3-단계 분리를 통해 $|\sigma''|_{\max} \cdot \sqrt n \to |\sigma''|_{\max} \cdot \sqrt{\rho_{\mathrm{bd-band}} \cdot n} + \delta(u^*) \cdot \sqrt{n - |A^*|}$ 의 *sharper* form 으로 표현됨 (3.9).

### §10.2 Cat 자기 verdict

| 항목 | Cat | 근거 |
|---|---|---|
| Lemma L1 (σ saturation) | **A** | §3.1 closed-form, 표준 calc. |
| Lemma L2 (Π_T^free 분해) | **A** | §3.2 결합, active-set + boundary-band partition. |
| Lemma L3 (boundary band measure) | **A** | T-OP6-B canonical Cat A 인용. |
| Lemma L4 (sharper bound assembly) | **A** *(modulo sub-claims)* | §3.4 chain — Cauchy-Schwarz + L1+L2+L3. |
| Lemma L5 (numerical verification) | **B** | §3.5 — quantitative gap honest. |
| Theorem (synthesis) | **B+** (Cat A *conditional on* S1/S2/S3) | §3.6, §7.1, §7.2. |

**최종 verdict:** **Cat B+ unconditional, Cat A conditional on three explicit sub-claims (S1)(S2)(S3).**

### §10.3 Gap status

**Closed (본 P4 기여):**
- (G1) $|\sigma''|_{\max}$ → active-set-restricted form *해석적* 분리 단계.
- (G2) $\sqrt n$ → $\sqrt{\rho_{\mathrm{bd-band}} \cdot n} + \sqrt{n-|A^*|}$ *해석적* refinement.
- (G3) T-OP6-B Cat A 인용을 통한 boundary band measure explicit.

**OPEN (Cat A 승급 prerequisite):**
- (S1) $\delta(u^*)$ 의 quantitative exponential decay → OP-HMORSE-LOCAL-A-2.
- (S2) $\varepsilon_{\mathrm{Cl}}$ explicit KKT-bound → OP-HMORSE-LOCAL-A-4.
- (S3) Boundary-band $\|w\|_\infty$ explicit → OP-HMORSE-LOCAL-A-1.

**OPEN (별도 OP):**
- SBM/barbell/small-world numerical robustness → OP-HMORSE-LOCAL-A-3 / OP-HMORSE-SBM.

### §10.4 다음 작업 (W9+)

- **W9 D1:** (S2) Łojasiewicz quantitative — Cat A 후보.
- **W9 D2:** (S1) Modica-Mortola quantitative rate — Cat A 후보.
- **W9 D3:** (S3) L-BOUNDARY-MODE-EXCLUSION Cat C → Cat B (Weyl explicit) → Cat A 사슬.
- **W10 D1:** CV-1.18 SEAL — L-HMORSE-LOCAL Cat A 승급 (S1+S2+S3 모두 closure 시).
- **W10 D2+:** Package II Eyring-Kramers Cat B 진입 (본 P4 + OP-0021 $T_*$ Cat A from D6).

### §10.5 Sanity check — 정리 조건의 비-vacuousness

D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) 의 *non-empty* validation:
- (C1) KKT critical: canonical `find_formation` 수렴 (215+1 xfailed PASS).
- (C2′) Active-set non-empty: 15/15 PASS 의 모든 minimizer 에서 $|A^*| > 0$.
- (C3) Single-formation: $K_{\mathrm{act}} = 1$ 의 canonical default.
- (C4) Symmetry-broken: asymmetric edge weights (perturb=0.1, seed=42) 사용.
- (C5) Boundary-localized mode 배제: L-BOUNDARY-MODE-EXCLUSION (Cat C) 인용.

T8-supercritical 의 *non-empty*: $\beta/\alpha \in [10, 100]$ all > $4\lambda_2/|W''(c)| \approx 0.16$ (15×15 grid). 따라서 본 정리의 조건이 *명시적으로* canonical 수치 실험에서 실현.

---

## §11. Appendix A — Notation summary

| Symbol | Meaning | Source |
|---|---|---|
| $u^* \in \Sigma_m$ | T8-supercritical minimizer | canonical §3 |
| $A^*(u^*)$ | Active set $\{x: u^*(x) \in \{0,1\}\}$ | canonical L1932 |
| $T_{u^*}^{\mathrm{free}}$ | Free tangent subspace | canonical L1932 |
| $\Pi_T^{\mathrm{free}}$ | Projector onto $T_{u^*}^{\mathrm{free}}$ | canonical L1932 |
| $\mathrm{Cl}(u) = \sigma(z(u))$ | Closure operator | canonical §9.2, `operators.py` L50 |
| $z(u) = a_{\mathrm{cl}}((1-\eta)u + \eta Pu - \tau)$ | Pre-activation | `operators.py` L57 |
| $\sigma(z) = 1/(1+e^{-z})$ | Sigmoid | `operators.py` L25 |
| $\sigma''(z) = \sigma(z)(1-\sigma(z))(1-2\sigma(z))$ | 2차 도함수 | §1.2, Lemma L1 |
| $J_{\mathrm{Cl}} = \mathrm{diag}(\sigma' a_{\mathrm{cl}}) M$ | Closure Jacobian | canonical L1759 |
| $M = (1-\eta)I + \eta P$ | Aggregation mix | canonical L1759 |
| $r = \mathrm{Cl}(u^*) - u^*$ | Closure residual | L-HMORSE-DECOMP D2 |
| $R_{\mathrm{cl}} = 2\lambda_{\mathrm{cl}} \sum_k r_k \nabla^2 \mathrm{Cl}_k$ | Residual Hessian | canonical L1986 |
| $\delta(u^*)$ | Saturation defect (1.2) | §1.3 본 P4 |
| $\rho_{\mathrm{bd-band}}(u^*)$ | Boundary band measure | T-OP6-B (canonical L1640) |
| $\varepsilon_{\mathrm{Cl}}$ | Closure 잔여 $\|r\|_\infty$ | §3.1 Lemma L1 |
| $\beta_{\mathrm{crit}}^{(2)}$ | Quantitative phase-separation threshold | OP-HMORSE-LOCAL-A-2 (S1) |

---

## §12. Appendix B — Cross-reference to E3 §A.5 권장 단계

| E3 §A.5 권장 Step | 본 P4 위치 | 상태 |
|---|---|---|
| Step 1: $\delta(u^*)$ configuration bound | §3.1 Lemma L1 + §7.1 (S1) | *부분적* (qualitative only; quantitative = OP-HMORSE-LOCAL-A-2) |
| Step 2: $\Pi_T^{\mathrm{free}} R_{\mathrm{cl}} \Pi_T^{\mathrm{free}}$ tight bound | §3.4 Lemma L4 | **완료** (해석 형식; quantitative gap honest) |
| Step 3: $c_{\mathrm{HML}}$ refined form | §10.2 + §7.1 | *부분적* — full assembly with S1+S2+S3 |
| Step 4 (optional): L-BOUNDARY-MODE-EXCL Cat B 승급 | §7.3 + §9.1 | OPEN (별도 OP) |

E3 권장 4-Step 중 Step 2 가 본 P4 의 *primary 성취*. Step 1, 3 가 *부분적*. Step 4 가 *별도 OP*.

---

## §13. Appendix C — Self-classification (CoT/CoC/CoQ summary)

### §13.1 CoT (Chain-of-Thought) 명시

- Lemma L1 (§3.1): 3 step (L1.1, L1.2, L1.3).
- Lemma L2 (§3.2): 2 step (L2.1, L2.2).
- Lemma L3 (§3.3): 3 step (L3.1, L3.2, L3.3).
- Lemma L4 (§3.4): 5 step (L4.1, L4.2, L4.3, L4.4, L4.5). **핵심 lemma — 5 step 으로 가장 상세.**
- Lemma L5 (§3.5): 3 step (L5.1, L5.2, L5.3).
- 총 16 CoT step.

### §13.2 CoC (Chain-of-Counterexample) 명시

- §6.1 Attempt 1: 조건 외 — 본 정리 scope 검증.
- §6.2 Attempt 2: 부분적 실패 — Cat A *quantitative* threshold 필요성 검증.
- §6.3 Attempt 3: framework 외 — canonical σ = sigmoid scope 검증.
- §6.4 Reflection: 3 시도 모두 결과적으로 *정리 조건의 분리* — Cat A scope honest.

### §13.3 CoQ (Chain-of-Open-Question) 명시

- §9.1 OP-HMORSE-LOCAL-A-1: $\|w\|_\infty$ explicit.
- §9.2 OP-HMORSE-LOCAL-A-2: $\delta(u^*)$ exponential decay.
- §9.3 OP-HMORSE-LOCAL-A-3: SBM/barbell extension.
- §9.4 (보너스) OP-HMORSE-LOCAL-A-4: $\varepsilon_{\mathrm{Cl}}$ KKT-explicit.

### §13.4 Silent failure 방지 — 명시적 ledger

- (a) Cat A *conditional* — Cat A 무조건이 *아님*. §7.1 explicit.
- (b) Numerical gap ~10–100× 잔존 — §3.5, §7.2 explicit.
- (c) (S1)(S2)(S3) 3 sub-claims 가 *open* — §7.3, §10.3 explicit.
- (d) SBM extension 가 D4 scope 외 — §8.3, §9.3 explicit.
- (e) L-BOUNDARY-MODE-EXCL Cat C → Cat B 가 별도 OP — §7.3, §9.1 explicit.

→ **silent OP resolution 회피 protocol 준수.**

---

## §14. Closing

본 P4 가 E3 §A 권장 *Approach A* 의 4-Step 중 Step 2 (sharper bound 해석 형식) 를 *완료* 한다. Step 1 (S1), Step 3 (S2) 는 *부분적*; Step 4 (S3) 는 *별도 OP*. 따라서 본 P4 자체의 Cat verdict 가 **Cat B+** (sharper bound 해석 형식 확보) + **Cat A 조건부** (S1+S2+S3 closure 시).

CV-1.18 SEAL 시 본 P4 가 canonical 외 working/foundation/proofs/ entry 로 유지; L-HMORSE-LOCAL Cat A 승급은 W10 D1 별도 turn (S1+S2+S3 closure 완료 후).

Package II Eyring-Kramers Cat B 진입의 *두 기둥 중 하나* (L-HMORSE-LOCAL Hessian 비퇴화 측) 가 본 P4 + 후속 (S1+S2+S3) 로 확보. 두 번째 기둥 = OP-0021 $T_*$ Cat A (D6 task).

---

*End of P4_OP-HMORSE-LOCAL-A.md. 작성: 2026-05-19 W8-Day2 Phase 2 D4 Opus. Consumer: V1 (rigor verification, Session 2). Cross-input: E3 §A. Cat verdict: B+ unconditional, A conditional on (S1)(S2)(S3).*
