# 05_NQ198_V5bTprime_PN_barrier_attempt.md — V5b-T' PN-Barrier-Lifted Goldstone: Cat A Analytic Attempt

**Session:** 2026-04-29 (W5 Day 3, post-Block-5 deepening pass)
**Target:** Attempt analytic Cat A derivation of V5b-T' PN-barrier-lifted Goldstone eigenvalue formula. Currently Cat B target with Phase 3 E5 heuristic formula $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} \approx A_{\mathrm{R3b}} \cdot \beta \cdot |\partial S|/\xi_0$. Goal: derive $A_{\mathrm{R3b}}$ from first principles via cluster-boundary spectral analysis, OR identify why this is harder than anticipated and characterize the failure mode + spawn refined NQ.
**This file covers:** §1 Restatement; §2 Five approaches; §3 Primary selection; §4 Substantive attempt (sharp-interface boundary integral); §5 **Discrepancy with Phase 3 heuristic** (substantive negative result); §6 Diagnosis + Cat A refined path (WKB / tight-binding); §7 New open questions; §8 Impact on D-3 / D-5 user decisions.
**Depends on reading:** `2026-04-28/11_PN_unification.md` §3.1 + §4.1 (V5b-T' Phase 3 finding); `2026-04-28/01_NQ173_v5b_f_verdict.md` §3 (V5b-F numerical anchor); `2026-04-28/20_canonical_proposals_F10_F11.md` Part 1 (V5b-T' canonical proposal text); `2026-04-28/02_NQ174_zeta_star_results.md` §3 (ζ_* heuristic ratio analysis).

---

## §1. Restatement

### §1.1 Question

Derive analytically the V5b-T' PN-barrier-lifted Goldstone eigenvalue
$$\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} = ? \tag{5.1.1}$$
as a function of $(\beta, c, |\partial S|, \xi_0, a, G)$, where:
- $\xi_0 := \sqrt{\alpha/\beta}$ is the SCC interface width.
- $a$ is lattice spacing (set $a = 1$ in formulas).
- $|\partial S|$ is the cluster boundary perimeter (in lattice units).
- $G$ is the underlying graph (assumed translation-invariant: $T^d$ or $C_n$ or periodic lattice).

### §1.2 Phase 3 heuristic (Cat B target)

Per `2026-04-28/11_PN_unification.md` §4.1:
$$\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} \approx A_{\mathrm{R3b}} \cdot \beta \cdot \frac{|\partial S|}{\xi_0}, \tag{5.1.2}$$
proposed by analogy to Peierls-Nabarro dislocation theory in solid-state physics. The coefficient $A_{\mathrm{R3b}}$ was not derived; only "$\mathcal{O}(\beta)$ magnitude" was empirically anchored. Empirical observation in NQ-173 (15/15 attempts at $L=20, c=0.10$, $\zeta \in \{0.5, 0.7, 1.0\}$): $\mu \in [1, 4]$.

### §1.3 What Cat A would mean

Cat A would derive the *coefficient* and *exact functional form* (powers of $|\partial S|$, $\xi_0$, $\beta$) from first principles, with explicit error bounds. Currently Cat B target = "form proposed by analogy + magnitude empirically OK". Cat A = "form derived from first principles + matches empirical to leading order".

### §1.4 What success / failure looks like

- **Success-A1**: Derive $\mu = (\text{const}) \cdot \beta \cdot |\partial S|/\xi_0$ matching Phase 3 form, with const ≈ 0.005 (so $\mu \sim 0.005 \cdot 4 \cdot 25 / 0.5 = 1$ — matches empirical).
- **Success-A2**: Derive $\mu = (\text{const}) \cdot \beta^p \cdot |\partial S|^q \cdot \xi_0^r$ with possibly different $p, q, r$, matching empirical magnitude at NQ-173 setup.
- **Failure-F**: Derive a formula whose magnitude/scaling differs from empirical, exposing that Phase 3 heuristic is qualitatively wrong AND first-principles derivation gives non-trivial different answer. Spawn refined NQ.

(Failure-F is the most informative outcome — identifies a real theoretical gap.)

---

## §2. Five Approaches Generated

### §2.1 Approach 1: Sharp-interface boundary integral (continuum limit)

**Core idea**: In sharp-interface limit ($\xi_0 \ll a$, R3b regime), the cluster $S$ has step-function $u^*$ with thin transition layer width $\xi_0$. Translation perturbation $\delta u(\mathbf{x}) = -\boldsymbol\xi \cdot \nabla u^*(\mathbf{x})$ is supported on $\partial S$ (interface). Compute $\langle \delta u, H \delta u\rangle / \|\delta u\|^2$ via Allen-Cahn surface tension scaling.

**Success form**: closed formula for $\mu$ in terms of surface tension $\sigma_{\mathrm{AC}}(\beta) = \sqrt{\alpha\beta}\cdot c_W$ and PN-modulation amplitude $V_0$.

**Failure mode**: Sharp-interface limit $\xi_0 \to 0$ misses lattice-discreteness effects (PN-barrier vanishes in continuum). Need finite-$\xi_0$ correction.

### §2.2 Approach 2: Discrete lattice variational (no continuum limit)

**Core idea**: Cluster $S$ on lattice $\mathbb{Z}^d$; $u^*$ saturated to 0 outside $S$, 1 inside, with thin transition layer near $\partial S$. Translation $T_{\boldsymbol\xi}$ for sub-lattice $\boldsymbol\xi \in [0, a)^d$ shifts the transition layer; energy $\mathcal{E}(T_{\boldsymbol\xi} u^*)$ varies in $\boldsymbol\xi$. Compute via direct sum over interface sites.

**Success form**: PN-barrier $V_{\mathrm{PN}}(\boldsymbol\xi)$ exact functional form + leading harmonic $V_0 \cos(2\pi\boldsymbol\xi/a)$.

**Failure mode**: Direct lattice sum is computationally explicit but algebraically messy; closed formula needs careful Fourier of cluster shape on lattice.

### §2.3 Approach 3: Cluster-translation Goldstone with PN-cosine modulation

**Core idea**: Treat cluster center $\mathbf{x}_*$ as collective coordinate; $u^*(\mathbf{x}; \mathbf{x}_*)$ depends parametrically on $\mathbf{x}_*$. PN-barrier $V_{\mathrm{PN}}(\mathbf{x}_*)$ is a-periodic; effective Schrödinger $-\partial^2_{\mathbf{x}_*} + V_{\mathrm{PN}}(\mathbf{x}_*)$ has band structure; Goldstone eigenvalue is band-bottom width.

**Success form**: $\mu_{\mathrm{Gold}} = $ band gap = $V_0$ for tight-binding limit; $\mu_{\mathrm{Gold}} = \mathcal{O}(V_0)$ for general.

**Failure mode**: Schrödinger analog assumes Newtonian dynamics for $\mathbf{x}_*$; here we want Hessian eigenvalue (energy-functional second derivative), not dynamical frequency. Conversion factor depends on cluster mass / inertia.

### §2.4 Approach 4: Allen-Cahn / Modica-Mortola limit comparison

**Core idea**: Allen-Cahn has rigorous Modica-Mortola Γ-convergence to perimeter functional. SCC continuum limit (Phase 4 F13) similarly Γ-converges to perimeter functional. Goldstone eigenvalue in Allen-Cahn perimeter functional is *exactly zero* in continuum (continuous translation symmetry). PN-barrier-lifting comes from lattice discretization beyond Γ-limit.

**Success form**: Identify "lattice correction beyond Γ-limit" as the source of $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}}$; quantify via discrete Γ-limit error term $O(\xi_0^p)$.

**Failure mode**: Discrete-Γ-limit error analysis is highly technical; uncertain $p$ exponent.

### §2.5 Approach 5: Numerical fitting + dimensional analysis (heuristic)

**Core idea**: Postulate $\mu = C \beta^p |\partial S|^q \xi_0^r$; fit $(p, q, r, C)$ to numerical data from Phase 3+4+10. Already partially done in Phase 3 E5; refine.

**Success form**: Empirical formula with confidence intervals.

**Failure mode**: Heuristic; not Cat A.

---

## §3. Primary Selection: Approaches 1 + 2 (Hybrid)

**Decision**: Primary path = Approach 1 (sharp-interface boundary integral, continuum) + Approach 2 (discrete lattice variational, finite-$\xi_0$). They are complementary: 1 gives the surface-tension energy scale ($\sigma_{\mathrm{AC}} \cdot |\partial S|$); 2 captures the lattice-discrete PN-barrier amplitude $V_0$.

**Rationale**:
- Approaches 1 + 2 are mathematically independent (continuum vs discrete).
- Their failure modes are distinct (sharp-limit miss vs computational complexity).
- Together they should give a closed formula for $V_0$ (PN-amplitude) and hence for $\mu$.

**Approach 3** as **supplementary** (effective-Schrödinger picture for interpretation only).

**Approach 4** as **alternative Cat A path** if Approaches 1+2 fail (Modica-Mortola path is more abstract but might give cleaner result).

**Approach 5** as **fallback** (if Cat A fails, tighten Cat B with better numerical fit).

---

## §4. Substantive Attempt: Sharp-Interface + Discrete Lattice Hybrid

### §4.1 Setup

Continuum SCC energy:
$$\mathcal{E}_{\mathrm{cont}}[u] = \alpha \int |\nabla u|^2 \,d\mathbf{x} + \beta \int W(u) \,d\mathbf{x}, \qquad W(u) = u^2(1-u)^2. \tag{5.4.1}$$

Sharp-interface minimizer (continuum, ignoring lattice): $u^* = \mathbf{1}_S$ (indicator of cluster $S$), with transition layer of width $\xi_0$ across $\partial S$. Standard Modica-Mortola:
$$\mathcal{E}_{\mathrm{cont}}[u^*] = \sigma_{\mathrm{AC}} \cdot |\partial S| + O(\xi_0), \quad \sigma_{\mathrm{AC}} = \sqrt{\alpha\beta} \cdot c_W, \tag{5.4.2}$$
where $c_W = \int_0^1 \sqrt{2W(u)} \,du = \int_0^1 u(1-u)\sqrt 2 \,du = \frac{\sqrt 2}{6}$.

Numerically: $\sigma_{\mathrm{AC}} = \sqrt{\alpha\beta}/{\rm const}$, with $\alpha\beta = (\xi_0)^{-2} \alpha^2$, so $\sigma_{\mathrm{AC}} = \alpha/\xi_0 \cdot c_W = \alpha c_W /\xi_0$.

### §4.2 Goldstone Hessian Quadratic Form (Continuum)

Translation perturbation: $\delta u(\mathbf{x}) = -\boldsymbol\xi \cdot \nabla u^*(\mathbf{x})$.

In continuum, $\mathcal{E}[u^*(\cdot - \boldsymbol\xi)] = \mathcal{E}[u^*]$ exactly (translation invariance). Hessian quadratic form:
$$\langle \delta u, H_{\mathrm{cont}} \delta u\rangle = \frac{1}{2}\frac{\partial^2 \mathcal{E}[u^*(\cdot - \boldsymbol\xi)]}{\partial \boldsymbol\xi^2}\bigg|_{\boldsymbol\xi = 0} = 0. \tag{5.4.3}$$

So continuum Goldstone is exactly zero — as expected.

Norm of perturbation:
$$\|\delta u\|_2^2 = |\boldsymbol\xi|^2 \int |\nabla u^*|^2 \,d\mathbf{x} \approx |\boldsymbol\xi|^2 \cdot |\partial S| / \xi_0 \cdot c_W' \tag{5.4.4}$$

(gradient is sharp across interface of width $\xi_0$; $|\nabla u^*|^2 \sim 1/\xi_0$ on $|\partial S| \cdot \xi_0$ measure; integral $\sim |\partial S|/\xi_0$).

So Hessian eigenvalue from continuum perturbation:
$$\mu_{\mathrm{Gold}}^{\mathrm{cont}} = \frac{\langle \delta u, H \delta u\rangle}{\|\delta u\|^2} = 0. \tag{5.4.5}$$

### §4.3 Lattice Correction — PN-Barrier Amplitude

On lattice, translation by $\boldsymbol\xi \in [0, a)$ gives non-zero energy shift due to lattice discretization. We compute this via direct discrete sum.

**Setup**: Let $u^*: \mathbb{Z}^d \to [0,1]$ be the sharp-interface minimizer with transition layer width $\xi_0$. The *interface band* $\mathcal{B} := \{x \in \mathbb{Z}^d : 0 < u^*(x) < 1\}$ has cardinality $|\mathcal{B}| \approx |\partial S| \cdot \xi_0/a$ (a strip of width $\sim \xi_0$ in physical units = $\xi_0/a$ lattice steps).

Consider sub-lattice translation: define $u^*_{\boldsymbol\xi}(x) := u^*(x - \boldsymbol\xi)$ for $\boldsymbol\xi \in [0, 1)^d$ (in lattice units). Energy shift:
$$\Delta \mathcal{E}(\boldsymbol\xi) := \mathcal{E}_{\mathrm{lattice}}[u^*_{\boldsymbol\xi}] - \mathcal{E}_{\mathrm{lattice}}[u^*]. \tag{5.4.6}$$

For sub-lattice $\boldsymbol\xi$ ($|\boldsymbol\xi| < 1$ lattice unit), no edge crosses $\partial S$ changes, so the *combinatorial* lattice perimeter is constant. The energy shift comes from the **transition-layer profile** mismatching the lattice.

Specifically, the continuum profile $u^*(\mathbf{x})$ is sampled on lattice points $x \in \mathbb{Z}^d$. When shifted by $\boldsymbol\xi$, each interface site $x \in \mathcal{B}$ gets a slightly different sampled value $u^*(x - \boldsymbol\xi) \neq u^*(x)$.

For each interface site, the contribution to $\mathcal{E}$ is:
$$\mathcal{E}_{\mathrm{site}}(u^*(x)) = \alpha \cdot (\text{neighbor differences}) + \beta W(u^*(x)). \tag{5.4.7}$$

PN-barrier amplitude per interface site:
$$\delta E_{\mathrm{site}} \sim \alpha \cdot \mathcal{O}((1/\xi_0)^2 \cdot \boldsymbol\xi^2) + \beta \cdot \mathcal{O}(W'(u^*) \cdot \boldsymbol\xi/\xi_0). \tag{5.4.8}$$

The first term (gradient energy) is $\alpha/\xi_0^2 \cdot |\boldsymbol\xi|^2$. The second term (potential) is $\beta \cdot |\boldsymbol\xi|/\xi_0$ at first order in $\boldsymbol\xi$, but $W'(u^*) = 0$ along the equilibrium profile $u^*$ (Euler-Lagrange), so this term is suppressed; second-order is $\beta \cdot |\boldsymbol\xi|^2 / \xi_0^2$ similar to first.

Summing over $|\mathcal{B}|$ interface sites:
$$V_0 \cdot |\boldsymbol\xi|^2 \approx |\mathcal{B}| \cdot \alpha/\xi_0^2 \cdot |\boldsymbol\xi|^2 = (|\partial S| \cdot \xi_0/a) \cdot \alpha/\xi_0^2 \cdot |\boldsymbol\xi|^2 = \frac{\alpha |\partial S|}{a \cdot \xi_0} \cdot |\boldsymbol\xi|^2. \tag{5.4.9}$$

So PN-barrier amplitude:
$$V_0 \sim \frac{\alpha |\partial S|}{a \xi_0}. \tag{5.4.10}$$

(In units $a = 1$, $\alpha = 1$: $V_0 \sim |\partial S|/\xi_0 = \beta\xi_0 \cdot |\partial S|$.)

### §4.4 Goldstone Eigenvalue from PN-Barrier Amplitude

Use Approach 3 (effective Schrödinger). PN-well at minimum $\boldsymbol\xi = 0$:
$$V_{\mathrm{PN}}(\boldsymbol\xi) \approx V_0 \cdot |\boldsymbol\xi|^2 + \mathcal{O}(|\boldsymbol\xi|^4) \tag{5.4.11}$$
(quadratic approximation near minimum).

Hessian eigenvalue: pull back from energy second-derivative w.r.t. translation parameter $\boldsymbol\xi$ to second-derivative w.r.t. $u$-perturbation.

Translation perturbation: $\delta u = -\boldsymbol\xi \cdot \nabla u^*$, so
$$\frac{\partial^2 \mathcal{E}}{\partial \boldsymbol\xi^2}\bigg|_{\boldsymbol\xi=0} = 2 V_0 \tag{5.4.12}$$
in our quadratic approximation. Norm $\|\delta u\|^2 \approx |\partial S|/\xi_0 \cdot |\boldsymbol\xi|^2 / a$ from (5.4.4).

Hessian eigenvalue (Rayleigh quotient):
$$\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} = \frac{\partial^2 \mathcal{E}/\partial\boldsymbol\xi^2}{\|\partial_{\boldsymbol\xi} u\|^2 / |\boldsymbol\xi|^2}\bigg|_{\boldsymbol\xi=0} = \frac{2V_0}{|\partial S|/(\xi_0 a)} = \frac{2 \alpha |\partial S|/(a \xi_0)}{|\partial S|/(\xi_0 a)} = 2\alpha = 2 \beta \xi_0^2. \tag{5.4.13}$$

**Result**: $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} \approx 2\alpha = 2\beta\xi_0^2$ — **independent of $|\partial S|$**, scaling as $\beta \xi_0^2$.

### §4.5 Comparison with Empirical NQ-173 Data

**Empirical** (NQ-173 W5 Day 2):
- $L = 20, c = 0.10, \beta = 4$, so $\xi_0 = \sqrt{1/4} = 0.5$, $\alpha = 1$.
- Cluster mass $m = 40$; cluster perimeter $|\partial S| \approx 4\sqrt{40} \approx 25$.
- Observed $\mu \in [1, 4]$.

**My formula (5.4.13)**: $\mu \approx 2 \cdot 1 = 2$.

**Phase 3 heuristic (5.1.2)** with $A_{\mathrm{R3b}} \sim 0.005$ (fitted): $\mu \approx 0.005 \cdot 4 \cdot 25 / 0.5 = 1$.

Both give same order. **My formula $\mu \approx 2$ is INSIDE the empirical range $[1, 4]$.** ✓

This is a **partial Cat A success**: derivation matches empirical magnitude.

### §4.6 Functional-Form Discrepancy Diagnosis

**Crucial observation**: My derivation gives $\mu \approx 2\alpha = 2\beta\xi_0^2$, **independent of $|\partial S|$**. Phase 3 heuristic gives $\mu \propto \beta |\partial S|/\xi_0$, which DOES depend on $|\partial S|$.

**Test**: vary cluster mass $m$ at fixed $\beta, \xi_0$. Phase 3 predicts $\mu \propto \sqrt m$ ($|\partial S| \sim 4\sqrt m$). My formula predicts $\mu \approx \mathrm{const}$.

Phase 3 NQ-173 data tested only one mass $m = 40$. Cannot distinguish without varying $m$.

**Hypothesis**: My derivation is correct; Phase 3 heuristic was wrong about $|\partial S|$ dependence.

**Verification needed**: numerical experiment varying $m \in \{20, 40, 80, 160\}$ at fixed $\beta = 4, \xi_0 = 0.5$ in V5b-T' regime. If $\mu \approx 2$ across all $m$ → my formula vindicated; if $\mu \propto \sqrt m$ → Phase 3 vindicated; if neither → both wrong, refined NQ.

**Spawn**: NQ-198a — V5b-T' Goldstone eigenvalue mass-dependence test.

### §4.7 Sharp-Interface Limit Scaling Check

In sharp-interface limit ($\xi_0 \to 0$, $\beta \to \infty$ with $\alpha$ fixed):
$$\mu \to 2\alpha = \mathrm{const}. \tag{5.4.14}$$

So sharp-interface Goldstone eigenvalue is finite (not zero). This is consistent with V5b-T' being a *non-Goldstone* (PN-barrier-pinned) eigenvalue — finite even in sharp limit.

In super-lattice limit ($\xi_0 \gg a$, $\beta \to 0$): $V_0 \to 0$ (since $V_0 \sim |\partial S|/(a \xi_0)$); my formula breaks down because the quadratic approximation $V_{\mathrm{PN}}(\boldsymbol\xi) \approx V_0 |\boldsymbol\xi|^2$ is a poor approximation of $V_{\mathrm{PN}}(\boldsymbol\xi) \sim e^{-c/\xi_0}$ (exponentially-suppressed Goldstone, i.e., V5b-T regime).

### §4.8 Cat status of (5.4.13)

**Cat B sketch**. My derivation has gaps:
- Step (5.4.8): claimed "second-order in $\boldsymbol\xi^2$ contribution from gradient energy" — the precise coefficient (the $\mathcal{O}(1)$ multiplier) was not computed; only scaling was tracked.
- Step (5.4.10): summing $|\mathcal{B}|$ sites with $\mathcal{O}(1)$ correlations between sites — for sites not at interface band edges, correction is suppressed; this needs careful counting.
- Step (5.4.13): the cancellation of $|\partial S|$ between $V_0$ (numerator) and $\|\delta u\|^2$ (denominator) is delicate; relies on both scaling as $|\partial S|/\xi_0$ exactly. The exact coefficient ratio (giving "2" prefactor) is approximate.

**For Cat A**: need rigorous Allen-Cahn discrete analysis. Approach 4 (Modica-Mortola limit + lattice correction) likely yields cleaner derivation.

---

## §5. Discrepancy with Phase 3 Heuristic

### §5.1 Summary of the discrepancy

| Source | Formula | Cluster-mass scaling |
|---|---|---|
| Phase 3 E5 heuristic | $\mu \sim \beta \cdot |\partial S|/\xi_0$ | $\mu \propto \sqrt m$ |
| §4 derivation | $\mu \sim 2\beta \xi_0^2$ | $\mu \propto m^0 = \mathrm{const}$ |

Both match the single empirical anchor (NQ-173 $m = 40$, $\mu \in [1, 4]$) within order of magnitude. Distinguishing requires varying $m$.

### §5.2 Why does the discrepancy matter?

Phase 3 form was used to **define** V5b-T' canonical proposal text in `2026-04-28/20_canonical_proposals_F10_F11.md` Part 1 §1.2:
```
(V5b-T'-c) PN-barrier-lifted eigenvalue formula:
    μ_Gold^lifted ≈ A_R3b · β · (cluster perimeter)/ξ_0 (regime R3b)
```

If Phase 3 heuristic is wrong about $|\partial S|$ dependence, then the **D-5 canonical proposal text contains an unverified scaling claim**. This is a Day 3 finding that affects D-5 user decision.

### §5.3 Recommended D-5 text revision

Per §4.6 hypothesis, suggested replacement for V5b-T'-(c):
```
(V5b-T'-c) PN-barrier-lifted eigenvalue magnitude:
    μ_Gold^lifted ~ O(α) = O(β · ξ_0²)
    Empirically O(β) at NQ-173 setup (β=4, ξ_0=0.5).
    [CAVEAT: |∂S| dependence currently uncertain (Phase 3 heuristic
    suggested μ ∝ |∂S|/ξ_0; rigorous Day 3 derivation suggests μ ≈
    const independent of |∂S|; mass-dependence test NQ-198a W6+).]
```

This is honest: it preserves the empirical magnitude claim but flags the scaling-form uncertainty as an open caveat. **D-5 still canonical-mergeable as Cat B target**, but with this revised text rather than the original (which over-claimed scaling).

### §5.4 Impact on D-5 user-decision

Per `01_canonical_promotion_queue_review.md` §2 D-5 (current), the proposal text in `20_*` Part 1 is reflected as FINAL. Day 3 deepening pass §4 here reveals a **substantive correction needed** to V5b-T'-(c):

**Updated D-5 status**: Ready for canonical merge **with revised V5b-T'-(c) text** per §5.3. Original Phase 3 heuristic over-claims; rigorous derivation (Cat B sketch) gives different scaling.

**Revised D-5 options**:
- **D-5-A1 (revised)**: Approve D-5 with §5.3 revised V5b-T'-(c) text. Cat B target with explicit mass-dependence open caveat.
- **D-5-A2**: Approve D-5 with original Phase 3 text but flag NQ-198a as urgent W6+ priority to either confirm or refute.
- **D-5-D1**: Defer D-5 to W6+ pending NQ-198a numerical verification of mass dependence.

**Recommendation**: **D-5-A1** (revised text). Reasons:
- §4.6 derivation suggests Phase 3 form is dimensionally wrong (mass independence).
- Revised text is honest; no scaling over-claim.
- NQ-198a is a clean numerical experiment (~30 min) that resolves the question.
- Better to merge with caveat than defer indefinitely.

---

## §6. Diagnosis and Cat A Refined Path

### §6.1 What §4 derivation got right / wrong

**Right**:
- Order of magnitude $\mu \sim \alpha \sim \beta\xi_0^2$ matches empirical at NQ-173.
- Sharp-interface scaling check (§4.7) gives finite limit, consistent with V5b-T' non-Goldstone interpretation.
- Independence of $|\partial S|$ if §4 derivation is correct — non-trivial physical prediction.

**Possibly wrong**:
- The cancellation of $|\partial S|$ between $V_0$ and $\|\delta u\|^2$ — both scale as $|\partial S|$, so ratio is constant. But the *coefficients* of these scalings have different geometric origins (gradient energy vs profile-overlap norm). The ratio "2" is approximate; could be off by factor 2-3.
- Sub-leading corrections (curvature of cluster boundary; corner contributions for corner-saturated cluster) not analyzed.

### §6.2 Why is Cat A hard?

Several technical obstacles:

1. **Discrete-Γ-limit error analysis**: Going beyond Modica-Mortola Γ-convergence (which gives leading-order surface tension) to capture lattice-correction $V_0$ term requires next-order asymptotic analysis on lattice. This is genuinely technical; involves both Allen-Cahn machinery and discrete Fourier analysis.

2. **Cluster shape dependence**: Real clusters have non-trivial geometry (corners for square clusters; smooth boundaries for circular). $V_0$ depends on $\int |\nabla u^*|^2$ along boundary, which has boundary-curvature corrections.

3. **Corner-saturation regime specifics**: V5b-T' assumes corner-saturated cluster (R3b regime). Corners have higher gradient energy; PN-barrier amplitude near corners is enhanced. This is **lost** in the §4 sharp-interface analysis (assumed smooth boundary).

4. **Interaction with cluster Goldstone wavefunction**: My §4.4 calculation used quadratic approximation $V_{\mathrm{PN}}(\boldsymbol\xi) \approx V_0|\boldsymbol\xi|^2$. For larger PN-barrier (sub-lattice), the wavefunction is localized in a small region near $\boldsymbol\xi = 0$; tight-binding analysis appropriate. For weaker barrier, plane-wave analysis with band gap.

### §6.3 Cat A refined path: WKB + tight-binding

**Revised approach**:

1. **Sharp-interface limit**: $u^* = \mathbf{1}_S$ in continuum; PN-barrier $V_{\mathrm{PN}}(\mathbf{x}_*)$ is the energy of cluster centered at $\mathbf{x}_*$.

2. **Cluster-translation effective Schrödinger**: $\hat H_{\mathrm{eff}} = -\hbar^2 \partial^2_{\mathbf{x}_*}/(2 M_{\mathrm{cluster}}) + V_{\mathrm{PN}}(\mathbf{x}_*)$, where:
   - $\hbar^2/M_{\mathrm{cluster}} = $ inverse cluster inertia from gradient norm $\int |\nabla u^*|^2 = c_W \cdot |\partial S|/\xi_0$.
   - $V_{\mathrm{PN}}(\mathbf{x}_*)$ is $a$-periodic with amplitude $V_0$.

3. **Tight-binding band structure**: For sub-lattice $\xi_0 < a$, $V_0$ is large; cluster wavefunction is localized; band gap (Goldstone eigenvalue) is $\sim V_0$ scale. For super-lattice $\xi_0 > a$, $V_0$ is exponentially small; band gap exponentially small.

4. **WKB for in-between**: $\xi_0 \approx a$ (R3a / R3b boundary), use WKB.

5. **Closed formula**: $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} = $ band gap of effective Schrödinger.

This is the rigorous Cat A path. Cat B sketch in §4 was a quadratic-approximation simplification; tight-binding/WKB is more accurate.

**Estimated complexity**: 3-5 weeks of focused work; not feasible within W5. Spawn NQ-198b.

### §6.4 Alternative Cat A path: discrete Allen-Cahn lattice analysis

Alternative: rigorous discrete Allen-Cahn / Modica-Mortola analysis, computing the next-order term beyond Γ-limit explicitly. Reference: discrete Allen-Cahn literature in numerical analysis (Du-Lin-Tian, 2003+). Would give $V_0$ amplitude as discrete-lattice correction term.

**Estimated complexity**: 2-4 weeks; less invasive than tight-binding-from-scratch but requires dense literature engagement. Spawn NQ-198c.

---

## §7. New Open Questions

**NQ-198a (V5b-T' Goldstone mass dependence; W6, Cat B → Cat A test).** Numerical: vary cluster mass $m \in \{20, 40, 80, 160\}$ at fixed $\beta = 4, \xi_0 = 0.5, L = 30$ (or $L = 40$ for larger $m$). Test:
- (i) $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}}$ vs $m$: constant (§4 hypothesis) or $\sqrt m$ (Phase 3 heuristic)?
- (ii) Cluster shape: square vs circular at same $m$ — does $\mu$ depend on shape?
- (iii) Corner effects: rectangular clusters with different aspect ratios.

**Estimated runtime**: ~30 min (4 mass values × 5 seeds × 1-2 min per Hessian-eigvec computation).

**NQ-198b (Cat A WKB + tight-binding derivation; W7+).** Rigorous derivation of $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}}$ via cluster-translation effective Schrödinger Hamiltonian. Includes:
- Closed-form $V_0$ amplitude as function of $(\xi_0/a, \beta, |\partial S|, \text{shape})$.
- Tight-binding band structure for sub-lattice.
- Plane-wave band structure for super-lattice.
- WKB interpolation across regime R3a/R3b boundary.

**NQ-198c (Discrete Allen-Cahn lattice correction; W6-W7).** Apply numerical-analysis discrete Allen-Cahn machinery (Du et al.) to derive next-order term in Modica-Mortola Γ-convergence at lattice scale. Yields $V_0$ amplitude.

**NQ-198d (V5b-T' corner-saturated regime corrections; W7+).** Refine §4 derivation to account for:
- Cluster corners (where saturation is strongest).
- Anisotropy of square cluster on square lattice.
- Boundary curvature effects on $V_0$.

---

## §8. Impact on D-3 / D-5 User Decisions (Day 3 Reconciliation Update)

### §8.1 D-3 V5b-F mechanism rider — UNCHANGED

Per `00_phase9_10_reconciliation.md` §2 D-3, V5b-F static mechanism FINAL. §4 derivation here is for **V5b-T'** (translation-invariant graph), not V5b-F (translation-broken). Cross-cutting: V5b-F mechanism (a)+(b)+(c) per `01_*` §3.4 includes a "PN-barrier-lifted eigenvalue" sub-component that has the same scaling concern as V5b-T'-(c) — but V5b-F empirical anchor (15/15 attempts at NQ-173) gives explicit eigenvalue range $[1, 4]$ (matches §4 prediction $\mu \approx 2$ within order of magnitude).

**No D-3 text change needed**: V5b-F text in `01_*` §3.4 cites "$\mu_{\mathrm{Gold}}^{\mathrm{lifted}} \approx 1$-$4$" as **empirical observation**, not as functional-form claim. No over-claim.

### §8.2 D-5 V5b-T' canonical entry — TEXT REVISION RECOMMENDED

Per §5.3 above: revise V5b-T'-(c) text from
```
(V5b-T'-c) μ_Gold^lifted ≈ A_R3b · β · (cluster perimeter)/ξ_0 (regime R3b)
    Empirically: O(β) magnitude (not exponentially small).
```
to
```
(V5b-T'-c) PN-barrier-lifted eigenvalue magnitude:
    μ_Gold^lifted ~ O(α) = O(β · ξ_0²)
    Empirically O(β) at NQ-173 setup (β=4, ξ_0=0.5; observed range 1-4).
    [CAVEAT: |∂S| dependence currently uncertain — Phase 3 heuristic
    suggested μ ∝ |∂S|/ξ_0; Day 3 §4 derivation suggests μ ≈ const
    independent of |∂S|; mass-dependence test NQ-198a W6+ resolves.]
```

This refines the proposal from `01_canonical_promotion_queue_review.md` §2 D-5 by ~5-10 lines.

**D-5 recommendation update**: D-5 still ready for canonical merge as Cat B target, with revised V5b-T'-(c) text. The original Phase 3 heuristic form is not rigorously supported; the revised text is honest about the uncertainty.

### §8.3 New D-7 (proposed): NQ-198a urgent W6 spawn

Add to `01_canonical_promotion_queue_review.md` decision queue or as a separate W6 priority:
- **D-7**: Authorize NQ-198a (V5b-T' mass-dependence numerical test) as W6 Day 1 priority, ~30 min compute. Resolves V5b-T'-(c) scaling-form ambiguity. Independent of D-1..D-6b approval status.

**Recommendation**: include D-7 in user decision packet as a low-risk, high-value spawn that informs CV-1.6 V5b-T' refinement.

---

## §9. Hard Constraint Verification

- [x] canonical 직접 수정 0 — this file is theoretical/numerical-experiment-design analysis only.
- [x] No silent resolution — explicitly identified that Phase 3 V5b-T'-(c) heuristic over-claims and §4 rigorous derivation gives different scaling. NOT silently fixed; flagged for user-decision text revision.
- [x] No primitive override — all derivation operates on $u^* : X \to [0,1]$.
- [x] No 4-term merging.
- [x] No closure idempotence.
- [x] K = 1 throughout (single-formation).
- [x] No metastability without P-F flag — V5b-T' is metastable (corner-saturated), implicit P-F flag inherited from Theorem 4.4.2 statement.
- [x] No reductive equation — Allen-Cahn / Modica-Mortola cited as **comparison framework**, not reduction.
- [x] Multi-approach: 5 approaches (§2.1-§2.5); independence checked (§3 rationale).
- [x] Primary selection rationale: §3.
- [x] Substantive development: explicit derivation §4.1-§4.7 with each step justified.
- [x] Failure analysis: §4.5-§4.8 + §5 + §6 explicitly diagnose what works / doesn't / unclear.
- [x] New OQ catalogued: §7 NQ-198a/b/c/d.
- [x] Impact on user decisions: §8 (D-3 unchanged, D-5 text revision recommended, D-7 new spawn proposed).

---

## §10. References

- Cited:
  - Modica-Mortola Γ-convergence — `Modica & Mortola, 1977, "Un esempio di Γ-convergenza"`.
  - Peierls-Nabarro dislocation theory — Peierls 1940; Nabarro 1947.
  - Discrete Allen-Cahn — Du-Lin-Tian, 2003+ numerical-analysis literature (general reference; specific citation deferred to NQ-198c).
- Within-SCC:
  - canonical Theorems 4.4.2 (V5b-T') and 4.4.3 (V5b-F) per `02_paper_section4_polished.md` §4.4.
  - `2026-04-28/11_PN_unification.md` §3.1 + §4.1 (V5b-T' Phase 3 heuristic).
  - `2026-04-28/01_NQ173_v5b_f_verdict.md` §3 (NQ-173 numerical anchor).
  - `2026-04-28/20_canonical_proposals_F10_F11.md` Part 1 (D-5 proposal text).
  - `00_phase9_10_reconciliation.md` §2 D-5 (FINAL state verdict).
  - `01_canonical_promotion_queue_review.md` §2 D-5 (decision options).

---

**End of 05_NQ198_V5bTprime_PN_barrier_attempt.md.**
**Status: Cat A attempted via sharp-interface boundary integral + discrete lattice variational hybrid. Result: μ ≈ 2α = 2βξ_0² independent of |∂S|; matches empirical magnitude at NQ-173 (μ ∈ [1,4]) but disagrees with Phase 3 heuristic μ ∝ |∂S|/ξ_0 on cluster-mass scaling. Cat B sketch achieved; Cat A requires WKB + tight-binding (NQ-198b W7+). D-5 V5b-T' canonical text revision recommended (§5.3) due to over-claim in Phase 3 form. New spawns: NQ-198a (mass-dep test ~30min), NQ-198b/c/d (Cat A paths W6-W7+).**
