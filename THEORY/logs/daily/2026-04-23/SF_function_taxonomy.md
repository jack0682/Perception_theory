# SF_function_taxonomy.md — Mathematical Function Taxonomy of SCC Transitions

**Session:** 2026-04-23 (G2 deliverable; intended promotion target: `working/SF/function_taxonomy.md`)
**Target (from plan.md §2 G2):** SCC의 transition 현상들을 수학적 함수 class로 분류. 각 class의 정의·regularity·asymptotic + 현상 매핑.
**This file covers:** 7개 함수 class 정의 (B1 forward catalog) + 주요 SCC 현상 7개의 morphological transition graph (B3 primary) + class-phenomenon 매핑 매트릭스 + 조건부성 명시.
**Depends on reading:** `01_exploration.md` §3 (B3 primary selection), `pre_brainstorm.md` §1 (7 function candidates), `logs/daily/2026-04-22/99_summary.md` §17.2 (R20 decoupling, N_unst saturation 발견), §17.10 (R21 shape regime A/B).

---

## §1. 설계 원리

### 1.1 Morphological transition graph (B3 primary)

Primary approach: **하나의 SCC 현상이 parameter regime에 따라 다른 함수 class로 "형태 변경"한다**는 점을 graph로 구조화. 각 edge는 transition point를 가진 형태 변경, nodes는 함수 class.

B1 (forward class catalog)이 secondary로, 각 class의 수학적 reference를 제공.

### 1.2 분류 축

- **Regularity**: $C^\infty$, $C^0$, discontinuous
- **Boundedness**: bounded, divergent, saturating
- **Asymptotic behavior**: exponential, polynomial, logarithmic, constant
- **Parameter dependence**: continuous smooth, continuous non-smooth, discrete

---

## §2. Function class catalog (B1 secondary)

7개 candidate class를 수학적으로 정의하고 각 class의 key properties를 기록.

### 2.1 Class H — Heaviside step

**Definition**:
$$H_{a}(x) = \begin{cases} 0 & x < a \\ 1 & x > a \end{cases}$$

- **Regularity**: $C^{-1}$ (discontinuous at $x = a$); $C^\infty$ on $\mathbb{R} \setminus \{a\}$.
- **Boundedness**: bounded in $[0, 1]$.
- **Asymptotic**: constant at $\pm \infty$.
- **Parameter**: discrete jump at $a$.
- **Characteristic function**: indicator of half-line.
- **Derivative**: Dirac delta $\delta(x - a)$ (distributional).
- **SCC primary role**: **Layer 1 protocol selector** $s_\pi(\beta)$ in zero-noise / zero-T limit.

### 2.2 Class L — Logistic sigmoid

**Definition**:
$$\sigma_{\kappa, a}(x) = \frac{1}{1 + e^{-\kappa(x - a)}}$$

- **Regularity**: $C^\infty$.
- **Boundedness**: in $[0, 1]$.
- **Asymptotic**: $\sigma \to 0$ as $x \to -\infty$, $\sigma \to 1$ as $x \to +\infty$.
- **Parameter**: smoothly parameterized by $(\kappa, a)$ (sharpness, center).
- **Derivative**: $\sigma'(x) = \kappa\sigma(1-\sigma)$.
- **Limit**: $\sigma_{\kappa, a} \to H_a$ as $\kappa \to \infty$. **Class H is $\lim_{\kappa \to \infty}$ Class L**.
- **SCC primary role**: closure operator $\mathrm{Cl}_t$ itself ($\sigma_{a_{\mathrm{cl}}, \tau_{\mathrm{cl}}}$ from canonical §9.2); **Layer 2 smooth crossover** within single K-sector.

### 2.3 Class T — Tanh soliton

**Definition**:
$$\phi_{\xi, r_0}(x) = \frac{1}{2}\left(1 - \tanh\left(\frac{d(x, x_0) - r_0}{\xi}\right)\right)$$

- **Regularity**: $C^\infty$.
- **Boundedness**: in $[0, 1]$ (inherits from $\tanh$).
- **Asymptotic**: $\phi \to 1$ near center, $\phi \to 0$ at infinity.
- **Parameter**: $(\xi, r_0)$ (interface width, radius).
- **Relation to L**: $\tanh(x) = 2\sigma(2x) - 1$. So T is L up to affine transformation.
- **SCC primary role**: **L3 field profile** (Cor 2.2 Cat A); universal tanh in supra-lattice regime (X2 D1 confirmed).

### 2.4 Class D — Log-divergent (Kramers-type)

**Definition**:
$$f_{\mathrm{log}}(x) = A \log\left(\frac{x - x_0}{x_1 - x_0}\right)\quad (x > x_0)$$

- **Regularity**: $C^\infty$ on $(x_0, \infty)$; diverges at $x_0$.
- **Boundedness**: divergent to $-\infty$ as $x \to x_0^+$.
- **Asymptotic**: logarithmic growth.
- **Key usage**: Kramers escape rate $\log \tau = \Delta\mathcal{F}/T$ — linear in inverse T; equivalently, near critical point $\beta \to \beta_c$, escape rate $\log \tau \sim \log(1/(\beta - \beta_c))$ (divergent).
- **SCC primary role**: **Layer 1 → Layer 0 escape rates** (finite T only); connection to Kramers theory.

### 2.5 Class S — Softmax (Boltzmann weight)

**Definition** (discrete K indexing):
$$P_k(\beta; T) = \frac{e^{-E_k^*(\beta)/T}}{\sum_j e^{-E_j^*(\beta)/T}}$$

- **Regularity**: $C^\infty$ in $\beta$ and $T$ (when $E_k^*$ smooth).
- **Boundedness**: $P_k \in [0, 1]$, $\sum_k P_k = 1$.
- **Asymptotic**:
  - $T \to 0$: $P_k \to \delta_{k, k^*}$ (Heaviside-like; reduces to class H selector).
  - $T \to \infty$: uniform $P_k = 1/|K|$.
- **Parameter**: continuous $T$ controls sharpness.
- **Relation to L**: binary case ($|K| = 2$) reduces exactly to logistic $P_1 = \sigma((E_2-E_1)/T)$.
- **SCC primary role**: **thermal basin selection at finite T**; **REFUTED as universal description** by R22 V7 P1 for SCC (P(K=1)≈0.02 constant across β=8.5-9.5) — see §5.3.

### 2.6 Class R — Rational / algebraic (static)

**Definition**:
$$f_{\mathrm{rat}}(x) = \frac{\sum_{k=0}^n a_k x^k}{\sum_{k=0}^m b_k x^k}$$

- **Regularity**: $C^\infty$ except at denominator zeros.
- **Boundedness**: depends on polynomial degrees.
- **Asymptotic**: polynomial growth or decay.
- **Concrete SCC instance**: $\nu_k(c) = -\gamma_D(c)[2 + c(1 - 2d_0(c))\kappa_D p_k]$ (Prop 1.3b (d) explicit form).
- **SCC primary role**: **L2 static spectral quantities**; c-dependence of Hessian eigenvalues.

### 2.7 Class P — Power law

**Definition**:
$$f_{\mathrm{pow}}(x) = A \cdot (x - x_c)^\gamma, \quad x > x_c$$

- **Regularity**: $C^\infty$ on $(x_c, \infty)$; derivative may diverge at $x_c$ for $\gamma < 1$.
- **Boundedness**: unbounded.
- **Asymptotic**: polynomial.
- **Relation to T/L**: Near critical point of pitchfork, amplitude $\propto (\beta - \beta_c)^{1/2}$ (T-Birth-Parametric Cat A) — power law with $\gamma = 1/2$.
- **SCC primary role**: **L2 amplitude near pitchfork** (T-Birth-Parametric); $\xi_0 = (\beta/\alpha)^{-1/2}$ (power with $\gamma = -1/2$).

---

## §3. SCC transition phenomena (B2 reverse anchors)

SCC의 주요 7개 transition (pre_brainstorm §1.1):

1. **Ph1 — K-sector selector**: $s_\pi(\beta) \in \mathbb{Z}_+$ protocol selector, steps at basin boundaries.
2. **Ph2 — Within-basin $K_{\mathrm{soft}}$ shift**: smooth continuous variation of soft count within single K-sector.
3. **Ph3 — Energy $E_{\mathrm{branch}}(\beta)$**: scalar energy value along single branch.
4. **Ph4 — Basin escape rate at T>0**: $\tau^{-1}_{k \to k'}$ exponential in inverse T.
5. **Ph5 — Bistable region stochastic**: probabilistic basin choice near protocol transition (V7 P3 observed).
6. **Ph6 — Shape profile $\phi_k^*(r)$**: u-field radial profile (Cor 2.2).
7. **Ph7 — Static mode count $\nu_k(c)$**: Hessian eigenvalues vs c (Prop 1.3b (d)).

### 3.1 Additional phenomena (not in pre_brainstorm)

- **Ph8 — Amplitude at first pitchfork**: $|u - u_{\mathrm{unif}}| \propto (\beta - \beta_c)^{1/2}$ (T-Birth-Parametric).
- **Ph9 — $\xi_0(\beta)$ interface width scaling**: $\xi_0 = \sqrt{\alpha/\beta}$.
- **Ph10 — $d_{\min}^*$ critical separation**: $d_{\min}^* = \sqrt{2}\,\xi_0\ln(1/\epsilon_0) + O(\xi_0)$ (`from_single.md` §4.3b).

---

## §4. Morphological transition graph

각 현상이 **여러 class를 돌아다니는 형태**를 명시. Nodes = class, edges = "regime transition points".

### 4.1 Ph1 (K-sector selector) — morphological trajectory

$$\begin{array}{r}
\text{Class H (T=0, zero noise, deterministic protocol)} \\
\downarrow\ (\text{finite noise } \epsilon \text{ or finite T}) \\
\text{Class L (}\kappa \propto 1/\epsilon\text{ or }\kappa \propto 1/T\text{)} \\
\downarrow\ (\text{ensemble over multiple protocols, or very high T}) \\
\text{Class S (Boltzmann-like, with caveats §5.3)} \\
\end{array}$$

**Transition points**:
- H → L: when single protocol + noise $\epsilon > 0$. Width of crossover $\propto \epsilon$.
- L → S: when ensemble of protocols / stochastic IC. However, **V7 P1 refuted basic thermal Boltzmann** → transition to S is **protocol-theoretic, not thermodynamic**.

**Primary class (canonical regime, deterministic)**: **H**.

### 4.2 Ph2 (Within-basin $K_{\mathrm{soft}}$) — trajectory

$$\text{Class L (smooth logistic in }\beta\text{ within K-sector)}$$

단일 class. Within-basin smoothness is guaranteed by canonical T14 (Łojasiewicz) + analyticity. Transitions 없음 except when K-sector boundary 통과 — then Ph1으로 switch.

**Primary class**: **L**.

### 4.3 Ph3 (Energy $E_{\mathrm{branch}}(\beta)$) — trajectory

$$\begin{array}{c}
\text{Class R (polynomial in }\beta\text{ away from } \beta_{\mathrm{crit}}\text{)} \\
\downarrow\ (\text{near }\beta_{\mathrm{crit}}^{(2)}) \\
\text{Class P (}\propto (\beta - \beta_c)\text{ linear near pitchfork)} \\
\downarrow\ (\text{at bifurcation crossover}) \\
\text{Class R (new branch})
\end{array}$$

**Primary class**: **R** generically, **P** near pitchfork.

### 4.4 Ph4 (Basin escape rate at T>0) — trajectory

$$\begin{array}{r}
\text{Class D (log-divergent, Kramers: } \log \tau \sim 1/T\text{)} \\
\downarrow\ T \to 0 \\
\text{Class H (}\tau \to \infty \text{ step at } T = 0\text{)}
\end{array}$$

**Primary class**: **D** (finite T); undefined at T=0.

### 4.5 Ph5 (Bistable region stochastic) — trajectory

$$\begin{array}{r}
\text{Class L (if protocol ensemble averages give sigmoid)} \\
\downarrow\ (\text{per-seed decomposition}) \\
\text{Mixture of H + H (deterministic per-seed)}
\end{array}$$

**V7 P3 observation**: At β=9 bistable, 200 seeds give **unimodal Gaussian around K=13**, NOT bimodal. So observed distribution is **neither pure L nor pure S** — rather a **Gaussian in K** which is not a class listed. **New class (N)** needed?

### 4.6 Ph6 (Shape profile $\phi_k^*(r)$) — trajectory

$$\begin{array}{c}
\text{Class T (tanh soliton, supra-lattice } \xi_0 \gg a, \alpha \geq 20) \\
\parallel\ (\text{same class, different regime}) \\
\text{Class T with shape exp } p \geq 3 \text{ (Regime A, } \alpha \leq 10) \\
\downarrow\ \beta \to \infty \\
\text{Class H (sharp indicator } \chi_{A_k}\text{)}
\end{array}$$

**Primary class**: **T** (with $p = 1$ in Regime B; $p \geq 3$ in Regime A per R21).
**Transition**: $\beta \to \infty$ gives $\xi_0 \to 0$ → class H step.

### 4.7 Ph7 (Static mode count $\nu_k(c)$) — trajectory

$$\text{Class R (purely algebraic in c, fixed graph)}$$

단일 class. No transitions. 이것은 purely static Layer 2 algebraic quantity (§17.2 R20 decoupling confirmed).

**Primary class**: **R**.

### 4.8 Ph8 (Amplitude at first pitchfork) — trajectory

$$\text{Class P, }\gamma = 1/2\ (\text{Crandall-Rabinowitz)}$$

단일 class. $|u - u_{\mathrm{unif}}| \propto (\beta - \beta_c)^{1/2}$.

### 4.9 Ph9 ($\xi_0(\beta)$) — trajectory

$$\text{Class P, }\gamma = -1/2$$

$\xi_0 = \sqrt{\alpha/\beta}$ — power with exponent $-1/2$. Saturates at lattice spacing $a$ when $\xi_0 \leq a$.

### 4.10 Ph10 ($d_{\min}^*(\beta)$) — trajectory

$$\text{Class P (}\xi_0\text{) } \times \text{ Class }D^{-1}\text{ (log tolerance)}$$

Composite: $d_{\min}^* = \sqrt{2}\xi_0\ln(1/\epsilon_0) + O(\xi_0)$ — product of power ($\xi_0 \propto \beta^{-1/2}$) and logarithm in tolerance.

---

## §5. Class-phenomenon mapping matrix

### 5.1 Matrix (row = phenomenon, column = class, entry = primary/secondary/NA/refuted)

| Phenomenon | H | L | T | D | S | R | P |
|---|---|---|---|---|---|---|---|
| Ph1 K-sector selector (deterministic) | **P** | S | — | — | (refuted) | — | — |
| Ph2 $K_{\mathrm{soft}}$ within basin | — | **P** | — | — | — | — | — |
| Ph3 $E_{\mathrm{branch}}(\beta)$ | — | — | — | — | — | **P** | S (near pitchfork) |
| Ph4 Escape rate (finite T) | S (T=0) | — | — | **P** | — | — | — |
| Ph5 Bistable stochastic | S | (averaged) | — | — | (refuted) | — | — |
| Ph6 Profile $\phi_k^*(r)$ | S ($\beta\to\infty$) | — | **P** | — | — | — | — |
| Ph7 $\nu_k(c)$ | — | — | — | — | — | **P** | — |
| Ph8 First-pitchfork amplitude | — | — | — | — | — | — | **P** |
| Ph9 $\xi_0(\beta)$ | — | — | — | — | — | — | **P** |
| Ph10 $d_{\min}^*(\beta)$ | — | — | — | S | — | — | **P** |

- **P** = primary class (this is the main fit)
- **S** = secondary class (fits in limit regime)
- **(refuted)** = class is NOT empirical fit (R17/R19/R20/V7 P1 falsifications)
- **—** = not applicable

### 5.2 Class usage summary

| Class | Primary count | Secondary count | Refuted count |
|---|---|---|---|
| H (Heaviside) | 1 (Ph1) | 3 (Ph4-T=0, Ph5, Ph6-β→∞) | 0 |
| L (Logistic) | 2 (Ph1-finite ε, Ph2) | 1 (Ph5 avg) | 0 |
| T (Tanh) | 1 (Ph6) | 0 | 0 |
| D (Log-div) | 1 (Ph4) | 1 (Ph10) | 0 |
| S (Softmax) | 0 | 0 | **2 (Ph1, Ph5 — V7 P1 refutation)** |
| R (Rational) | 2 (Ph3, Ph7) | 0 | 0 |
| P (Power) | 3 (Ph8, Ph9, Ph10) | 1 (Ph3) | 0 |

### 5.3 Softmax (Class S) refutation — 중요 결과

**V7 P1 refutation** (logs 2026-04-22 R22): β=9 bistable region에서 P(K=1) ≈ 0.02 constant across β=8.5-9.5, not sigmoid-shaped. Basic thermal Boltzmann softmax에 의해 fit되지 않음.

**V7 P3 observation**: 200 seeds × β=9 gives **Gaussian around K=13**, not Boltzmann $P_k \propto e^{-E_k/T}$.

**Conclusion**: Class S는 SCC의 dynamic observable (K̂)에 대해 **unsuitable**. 현재 framework에서 "basin selection이 Boltzmann"이라는 가정은 **empirically falsified**.

**대안 설명 (tentative)**: Layer 1 protocol-selector가 stochastic initial condition과 독립적으로 분포. Distribution은 **graph-spectral-mode-seeded Gaussian** (R22 V7 P3) — 이는 기존 분류에 없는 **new class (Class N — "spectral Gaussian")**의 후보.

---

## §6. New class candidate — Class N (spectral Gaussian)

### 6.1 Proposed definition

$$P_{\mathrm{spec}}(K | \beta) \approx \mathcal{N}(K; \bar K(\beta, G), \sigma^2_K(\beta, G))$$

where $\bar K$ and $\sigma_K^2$ are graph-spectral functionals determined by the Fiedler-mode distribution at saturation.

### 6.2 Status

- **V7 P3 empirical motivation**: β=9, 1D cycle c=0.7, 200 seeds → Gaussian around K=13 with std ≈ 1.5.
- **Open**: Gaussian parameters의 explicit form — what depends on $\beta, c, G$? Related to NQ-47 (Kramers-like transition rates).

### 6.3 Assign Class N

- **Ph5** (Bistable stochastic): **Class N** as primary (replacing refuted Class S).
- **Other**: Class N appears to be specific to **Layer 1 stochastic basin selection**; not currently applicable to other phenomena.

---

## §7. Morphological transition limits (class convergences)

다음은 class 간 asymptotic 관계:

| From → To | Limit | Mechanism |
|---|---|---|
| L → H | $\kappa \to \infty$ | Sigmoid sharpening |
| T → H | $\xi \to 0$ | Interface width vanishing |
| S → H | $T \to 0$ | Thermal freezing (Boltzmann → max) |
| S → uniform | $T \to \infty$ | Thermal melting |
| P → constant | $\gamma \to 0$ | Exponent vanishing |
| D → constant | $x \to \infty$ far from singularity | Log growth slow |
| N → H | $\sigma_K \to 0$ | Stochastic concentration (deterministic limit) |

**Key observation**: Class H is **attractor** of multiple limit procedures (L, T, S, N). SCC의 **Layer 1 discrete structure는 여러 smooth limits의 공통 limit**이며, 이는 Layer 1의 robustness를 시사.

---

## §8. Regime-dependence of class choice

각 phenomenon의 class는 **특정 regime에서만 고정**. 다음 regime axes 중요:

### 8.1 Parameter regime axes

- **$\beta$ regime**: $\beta < \beta_{\mathrm{crit}}^{(2)}$ (uniform) / $\beta \in [\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{sat}}]$ (bifurcating) / $\beta > \beta_{\mathrm{sat}}$ (saturated multi-formation).
- **$c$ regime**: Regime I ($c < c_{\mathrm{bif}}^-$), Regime II (canonical $c = 1/2$), Regime III ($c > c_{\mathrm{bif}}^+$).
- **α regime**: supra-lattice ($\alpha \geq 20$) vs sub-lattice ($\alpha \leq 10$) — R21 X2 D1 α threshold.
- **T regime**: zero-T deterministic / finite-T Langevin.
- **Protocol regime**: Fiedler-init / random-init / warm-start / hysteresis.

### 8.2 Class choice as function of regime (primary class matrix)

| Phenomenon | $\beta$ regime | $c$ regime | α regime | T regime | Protocol | Primary class |
|---|---|---|---|---|---|---|
| Ph1 selector | supra-crit | — | — | T=0 | deterministic | H |
| Ph1 selector | supra-crit | — | — | T=0 | noisy ε | L |
| Ph1 selector | supra-crit | — | — | T>0 | ensemble | N (not S) |
| Ph2 $K_{\mathrm{soft}}$ | supra-crit | any | any | any | fixed | L |
| Ph3 E(β) | any | any | any | T=0 | branch-fixed | R (or P near pitchfork) |
| Ph4 escape | supra-crit | any | any | **T>0** | any | D |
| Ph6 profile | supra-crit | any | **supra-α** | T=0 | any | T |
| Ph6 profile | supra-crit | any | **sub-α** | T=0 | any | T + $p \geq 3$ (modified) |
| Ph7 ν_k(c) | any | any | any | T=0 | — | R |
| Ph8 amplitude | near-crit | any | any | T=0 | branch | P ($\gamma = 1/2$) |

### 8.3 "Regime-dependence" as taxonomy axis

Class choice is **not** a phenomenon-property pair; it's a **(phenomenon, regime) → class** mapping. Taxonomy 정확히 쓰려면 row = (phenomenon × regime), column = class.

---

## §9. Summary: morphological transition graph (consolidated)

전체 SCC 함수 classes와 primary SCC usage:

```
         [Class H] ← T→0 ← [Class L] ← κ→∞ ← [Class L]
              |                  |               |
              |                  | (within-basin Ph2)
              ↑                  ↑
          (selector Ph1)      (ε>0 smoothing)
              ↑                  
          [T=0 limit, Ph1, Ph6-β→∞]
              
         [Class T] ← ξ→0 ← [shape profile Ph6]
              |                   
         (L3 field profile)
              
         [Class D] ← finite-T Ph4 escape rate
              |
         (log-divergent, Kramers)
              
         [Class S] ← [REFUTED by V7 P1]
              
         [Class N] (empirical, Ph5 stochastic bistable; new class proposal)
              
         [Class R] ← ν_k(c) Ph7, E-branch Ph3 smooth
         
         [Class P] ← Ph8 amplitude √(β-β_c), Ph9 ξ_0, Ph10 d_min
```

**Central insight**: SCC의 transition morphology는 **class H at Layer 1, class T/L at Layer 3, class R/P at Layer 2** — 각 layer가 primary function class family를 가짐. Layer 1의 "H-attractor" 성질 (§7)은 Layer 1 robustness의 수학적 표현.

---

## §10. Taxonomy's relation to canonical

### 10.1 Each class's location in canonical

- **Class L (logistic)**: canonical §9.2 closure operator $\mathrm{Cl}_t = \sigma(a_{\mathrm{cl}}(P_t u - \tau_{\mathrm{cl}}))$. 이것은 **canonical의 primitive**.
- **Class T (tanh)**: canonical §13 Cor 2.2, T11 Γ-convergence.
- **Class P (power)**: canonical T-Birth-Parametric (power $\gamma = 1/2$); $\xi_0$ definition.
- **Class R (rational)**: Prop 1.3b (d) explicit.
- **Class H (Heaviside)**: canonical T11 Γ-limit; R22 C-X1V5 Protocol Selection; **step_cohesion.md** §5.1 $K_{\mathrm{step}}$ operator.
- **Class D (log-divergent)**: canonical §12 "Three Pillars" Pillar III (coarsening barrier $\propto \beta^{0.89}$, 현재 Cat B); Kramers 현재 canonical 외부.
- **Class S (softmax)**: canonical 외부. V7 P1 refuted.
- **Class N (spectral Gaussian)**: new proposal; canonical 외부.

### 10.2 Class as candidate new canonical lemma

각 class에 대해 canonical lemma 형태로 쓰면:

- **L-Lemma**: $\mathrm{Cl}_t$ is class L with $\kappa = a_{\mathrm{cl}}/4 \cdot n$, center $\tau_{\mathrm{cl}}$.
- **T-Lemma**: Cor 2.2 states single-formation profile is class T with $\xi_0 = \sqrt{\alpha/\beta}$ in supra-lattice regime.
- **P-Lemma**: T-Birth-Parametric gives Class P with $\gamma = 1/2$ for first pitchfork amplitude.
- **R-Lemma**: Prop 1.3b (d) gives Class R for $\nu_k(c)$.
- **H-Lemma (new)**: Step_cohesion.md §5.1 K_step operator produces Class H selector; protocol selection (C-X1V5) gives Class H transitions.
- **D-Lemma (new, conditional)**: Kramers escape rate, contingent on P-F (thermal framework open).

---

## §11. Class hierarchy & limits (§7 consolidated with canonical)

Morphological transition의 limits을 canonical contexts로:

- **Finite-$\beta$**: Class T/L/R dominate.
- **$\beta \to \infty$ limit**: Class T → Class H (T11 Γ-convergence); canonical statement.
- **Protocol-free deterministic**: Class H dominates Ph1.
- **Protocol + noise $\epsilon$**: Class L replaces Class H for Ph1 (width $\propto \epsilon$).
- **Finite T (new, pending P-F)**: Class D enters Ph4; Class N replaces Class S for Ph5.

---

## §12. Limits per class (B1 back-reference)

| Class | Lower limit | Upper limit |
|---|---|---|
| H | 0 | 1 |
| L | 0 ($x \to -\infty$) | 1 ($x \to +\infty$) |
| T | 0 (outside formation) | 1 (inside formation center) |
| D | $-\infty$ (at singularity) | slow growth to $+\infty$ |
| S | 0 (each $P_k$) | 1 ($\sum P_k = 1$) |
| R | depends on polynomial | depends on polynomial |
| P | 0 at $x_c$ | unbounded as $x \to \infty$ |
| N | — Gaussian characterized by mean/variance | — |

---

## §13. Open residual (G2 carry-forward)

- **NQ-52 (new)**: Class N (spectral Gaussian) parameters — $\bar K(\beta, G)$ and $\sigma_K^2(\beta, G)$의 closed form.
- **NQ-53 (new)**: Class D in SCC without P-F — Kramers rate의 엄밀한 justification가 thermal framework P-F를 요구. 현재 sketched only.
- **NQ-54 (new)**: Class R의 graph-class universality — Prop 1.3b(d)은 D_4에서 explicit, general graph에서 Class R 형태 유지?
- **NQ-55 (new)**: Regime-dependent class transition points의 explicit formulas — α=10 (R21 shape Regime boundary), β_sat (R20 N_unst saturation) 등.

---

## §14. File status

- **Primary deliverable**: 7 classes (H, L, T, D, S, R, P) + 1 new candidate (N) × 10 phenomena matrix.
- **Class S refutation** (V7 P1) documented explicitly.
- **Morphological transition graph**: §9.
- **Regime-dependence**: §8.
- **Canonical integration**: §10 (existing classes in canonical); new lemma proposals (§10.2).
- **Intended promotion**: `working/SF/function_taxonomy.md` (신규).

**End of SF_function_taxonomy.md.**
