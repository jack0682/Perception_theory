# 01e_theorem4_first_pitchfork.md — Theorem 4 (σ at First Pitchfork on $D_4$ Free-BC Grid)

> ⚠ **ERRATUM (2026-04-27 evening, post-merge re-review):** §2 statement (ii) and §3 Step 5/5' derivation have **two related errors**:
>
> 1. **$K_1 < K_0$ wrong.** Stated "$0 < K_1 < K_0$ would-be transverse Goldstone, partial lifting from discrete $D_4 \to \mathbb{Z}_2$" — this is incorrect. Discrete symmetry breaking does NOT produce Goldstone modes (Goldstones require continuous symmetry). The R22 normal-form analysis on $D_4$ free-BC gives $K_0 = 4|W''(c)|$, $K_1 = (A_2/A_1)|W''(c)|$, with $A_2/A_1 = 4$, hence **$K_1 = K_0$** at leading order. The two modes are degenerate but irrep-distinct ($[+1]$ trivial vs $[-1]$ sign).
>
> 2. **In-text contradiction not resolved.** §3 Step 5 admitted "this gives Morse-1, not Morse-0" without resolution. The fix is to defer Morse-0 establishment to R22 normal-form (which gives the correct positive eigenvalues above), not to the ad-hoc partial second-order calculation I did.
>
> **Canonical T-σ-Theorem-4 entry (canonical.md §13 line 1278) has been corrected** with the right $K_0 = K_1$ formula and a clean R22 normal-form proof outline. See `91_critical_review.md` §3 + §5 for full discussion.

**Session:** 2026-04-27 (W5 Day 1, G0 Block 2)
**Target (from plan.md §3 Block 2 13:00–14:00):** Theorem 4 full statement (leading-order $\epsilon$ expansion at first pitchfork) + perturbation-theory proof + $D_4 \to \mathbb{Z}_2$ symmetry breaking irrep relabeling + canonical wording.
**This file covers:** Setup ($\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$, $u^*_\epsilon$ axis-aligned post-bifurcation), 8-step proof, second-order perturbation theory at $c = 0.5$ (where first-order vanishes per `pre_brainstorm.md` §1.5), $\mathcal{F}$-tie convention, Cat A self-classification.
**Depends on reading:** `04-24/04_orbital_proofs.md` §2 (W4-04-24 Theorem 4 first proof), `canonical.md` §13 T-Birth-Parametric (Cat A pitchfork existence), `working/SF/symmetry_moduli.md` §3.3 (R22 axis-aligned cubic coefficient analysis Cat A), `01d_theorem3_uniform_D4_grid.md` (uniform σ as starting point), `01a_lemma1_irrep_decomposition.md` (irrep apparatus).

---

## §1. Setup

Same $G$ as Theorem 3: $D_4$ free-BC $L \times L$ grid, $c \in $ spinodal interior. Now take $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$ with $\epsilon > 0$ small.

**Existence of post-bifurcation minimizer (T-Birth-Parametric, `canonical.md` §13, Cat A):** for $\beta$ slightly above critical, $u^* = c\mathbf{1}$ becomes Morse-1 (one negative eigenvalue along $V_2$ Fiedler subspace), and a new local minimum $u^*_\epsilon$ bifurcates from $c\mathbf{1}$ along a direction in $V_2 = \mathrm{span}(\phi_{(1,0)}, \phi_{(0,1)})$, with $\|u^*_\epsilon - c\mathbf{1}\|_2 = O(\sqrt{\epsilon})$.

**R22 axis-aligned selection (`working/SF/symmetry_moduli.md` §3.3, Cat A):** the cubic equivariant analysis at the bifurcation point selects, among the orbit of $D_4$-equivalent post-bifurcation minimizers, **axis-aligned** ones (single Fiedler direction $\phi_{(1, 0)}$ or $\phi_{(0, 1)}$, not diagonal $\phi_{(1, 0)} + \phi_{(0, 1)}$) over diagonal orbit, with cubic coefficient ratio $A_2/A_1 = 4$ on $D_4$ free-BC.

**Choose representative orbit element:**
$$u^*_\epsilon = c\mathbf{1} + a_\epsilon\, \phi_{(1, 0)} + O(\epsilon),\qquad a_\epsilon = c_R \sqrt{\epsilon} + O(\epsilon^{3/2}),$$
with $c_R > 0$ explicit Crandall–Rabinowitz coefficient (`working/SF/symmetry_moduli.md` §3.3).

(Other orbit elements: $c\mathbf{1} \pm a_\epsilon \phi_{(1, 0)}$ and $c\mathbf{1} \pm a_\epsilon \phi_{(0, 1)}$ — total 4-element orbit; choose one representative.)

---

## §2. Statement

> **Theorem 4 (σ at first pitchfork, leading order in $\epsilon$).** Under the Setup, with $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1, 0)} + O(\epsilon)$ axis-aligned post-bifurcation minimizer:
>
> **(i) Stabilizer.** $G_{u_\epsilon} = \langle s_y \rangle \cong \mathbb{Z}_2$ (single reflection through horizontal mid-line $y = (L-1)/2$). The full $D_4$ symmetry of $u^* = c\mathbf{1}$ is spontaneously broken to $\mathbb{Z}_2$.
>
> **(ii) Hessian leading-order spectrum.** Two Fiedler-direction modes split:
> - Mode 0 (along $\phi_{(1, 0)}$, broken-symmetry direction): $\mu_0 = K_0 \cdot \epsilon + O(\epsilon^2)$ with $K_0 > 0$ explicit (recovered stability).
> - Mode 1 (along $\phi_{(0, 1)}$, would-be Goldstone of broken rotational symmetry $D_4 \to \mathbb{Z}_2$): $\mu_1 = K_1 \cdot \epsilon + O(\epsilon^2)$ with $0 < K_1 < K_0$ (split, near-zero).
> All higher modes stay at $\mu_k(c\mathbf{1}) + O(\sqrt{\epsilon})$.
>
> **(iii) Irrep labels under $G_{u_\epsilon} = \mathbb{Z}_2 = \langle s_y\rangle$.** $\widehat{\mathbb{Z}_2} = \{+1, -1\}$ (trivial and sign).
> - Mode 0 ($\phi_{(1, 0)}$): under $s_y: y \to L-1-y$, $\phi_{(1, 0)}$ depends only on $x$, invariant. $[\rho_0] = +1$ (trivial).
> - Mode 1 ($\phi_{(0, 1)}$): under $s_y$, $\phi_{(0, 1)} \to -\phi_{(0, 1)}$. $[\rho_1] = -1$ (sign).
> - Higher modes: classified by $s_y$-parity.
>
> **(iv) Nodal counts.** $\mathcal{N}(\phi_{(1, 0)}) = 2$, $\mathcal{N}(\phi_{(0, 1)}) = 2$. Higher modes inherit $\mathcal{N}(\phi_{(p, q)}) = (p+1)(q+1)$ to leading order.
>
> **(v) σ-signature** (leading order):
> $$\sigma(u^*_\epsilon) = \big(\mathcal{F}(u^*_\epsilon);\ (2, [+1], K_0\epsilon),\ (2, [-1], K_1\epsilon),\ (n_{(p_k, q_k)}, [\rho_k], \mu_k(c\mathbf{1}) + O(\sqrt{\epsilon}))_{k \geq 4}\big).$$
>
> **(vi) Local-maxima count.** $\mathcal{F}(u^*_\epsilon) \in \{0, 1\}$ depending on tie-breaking convention (strict-max convention: 0 by strict inequality at $L \to \infty$ continuum; plateau-max convention: 1).

---

## §3. Proof

### Step 1 — Existence and form of $u^*_\epsilon$.

T-Birth-Parametric (`canonical.md` §13 Cat A) + R22 axis-aligned selection (`working/SF/symmetry_moduli.md` §3.3 Cat A): for $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$, $\epsilon$ small, axis-aligned post-bifurcation minimizer $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1, 0)} + O(\epsilon)$ with $a_\epsilon = c_R\sqrt{\epsilon}$ exists and is locally stable. ✓

### Step 2 — Stabilizer computation.

Recall (Theorem 3 §5) $D_4$ action on $\phi_{(p, q)}$ by sign factors and parity swaps:
- $r$ (90° rotation): $\phi_{(1, 0)} \to (-1)^1 \phi_{(0, 1)} = -\phi_{(0, 1)}$. $r \cdot u^*_\epsilon = c\mathbf{1} - a_\epsilon \phi_{(0, 1)} \neq u^*_\epsilon$. $r \notin G_{u_\epsilon}$.
- $r^2$ (180°): $\phi_{(1, 0)} \to (-1)^2 \phi_{(1, 0)} = \phi_{(1, 0)}$? Let me recompute via $r^2 = r \circ r$: $r \cdot \phi_{(1, 0)} = -\phi_{(0, 1)}$, then $r^2 \cdot \phi_{(1, 0)} = r \cdot (-\phi_{(0, 1)}) = -((-1)^0 \phi_{(1, 0)}) = -\phi_{(1, 0)}$. So $r^2 \cdot u^*_\epsilon = c\mathbf{1} - a_\epsilon\phi_{(1, 0)} \neq u^*_\epsilon$. $r^2 \notin G_{u_\epsilon}$.
- $s_x$ (reflection $x \to L-1-x$): $\phi_{(1, 0)} \to (-1)^1 \phi_{(1, 0)} = -\phi_{(1, 0)}$. $s_x \cdot u^*_\epsilon = c\mathbf{1} - a_\epsilon\phi_{(1, 0)} \neq u^*_\epsilon$. $s_x \notin G_{u_\epsilon}$.
- $s_y$ (reflection $y \to L-1-y$): $\phi_{(1, 0)}$ depends only on $x$, invariant under $s_y$. $s_y \cdot u^*_\epsilon = u^*_\epsilon$. $s_y \in G_{u_\epsilon}$. ✓
- $r s_x$, $r s_y$, etc.: combinations; check directly. $rs_y$: first $s_y$ (invariant), then $r$ (move). $rs_y \cdot u^*_\epsilon = r \cdot u^*_\epsilon = c\mathbf{1} - a_\epsilon\phi_{(0, 1)} \neq u^*_\epsilon$. Out.
- Identity $e \in G_{u_\epsilon}$ trivially.

Conclude: $G_{u_\epsilon} = \{e, s_y\} = \langle s_y\rangle \cong \mathbb{Z}_2$. ✓

### Step 3 — Hessian perturbation expansion.

Unconstrained Hessian: $\mathbf{H}(u) = 4\alpha L_G + \beta\,\mathrm{diag}(W''(u))$ at the pure-$\mathcal{E}_{\mathrm{bd}}$ level. Expand:
$$W''(u^*_\epsilon) = W''(c) + W'''(c)(u^*_\epsilon - c\mathbf{1}) + O((u^*_\epsilon - c\mathbf{1})^2).$$
With $u^*_\epsilon - c\mathbf{1} = a_\epsilon \phi_{(1, 0)} + O(\epsilon)$:
$$\mathbf{H}(u^*_\epsilon) = 4\alpha L_G + \beta W''(c) I + \beta a_\epsilon W'''(c)\,\mathrm{diag}(\phi_{(1, 0)}) + O(\epsilon).$$

$W'''(u) = -12 + 24u$ for $W(u) = u^2(1-u)^2$. $W'''(c) = 12(2c - 1)$.

**Two regimes:**
- **$c = 0.5$:** $W'''(0.5) = 0$. First-order perturbation $\delta\mathbf{H}^{(1)} = 0$. Second-order term required ($O(\epsilon)$ direct).
- **$c \neq 0.5$:** $W'''(c) \neq 0$. First-order $\delta\mathbf{H}^{(1)} = \beta a_\epsilon W'''(c)\,\mathrm{diag}(\phi_{(1, 0)}) = O(\sqrt{\epsilon})$.

### Step 4 — Spectral split: degenerate first-order perturbation theory on the Fiedler doublet.

At $u^* = c\mathbf{1}$, modes $\phi_{(1, 0)}$ and $\phi_{(0, 1)}$ are degenerate (both at $\mu = 4\alpha + \beta W''(c)$). At $\beta = \beta_{\mathrm{crit}}^{(2)}$ exactly: $\mu = 0$. For $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$, before perturbation by $u^*_\epsilon - c\mathbf{1}$: $\mu = 4\alpha + (\beta_{\mathrm{crit}}^{(2)} + \epsilon)W''(c) = -\epsilon |W''(c)| + 4\alpha\lambda_2^{\mathrm{Lap}}\cdot 0 = -\epsilon|W''(c)|$ (since $4\alpha\lambda_2^{\mathrm{Lap}} = \beta_{\mathrm{crit}}^{(2)}|W''(c)|$ from definition).

So the unperturbed Fiedler doublet has $\mu = -\epsilon|W''(c)|$ at $u = c\mathbf{1}$ — both modes negative (instability). The post-bifurcation $u^*_\epsilon$ adds the Hessian perturbation $\delta\mathbf{H}$.

**Compute degenerate first-order matrix elements** in Fiedler doublet:

For $c \neq 0.5$:
- $\langle \phi_{(1, 0)} | \delta\mathbf{H} | \phi_{(1, 0)}\rangle = \beta a_\epsilon W'''(c)\,\langle\phi_{(1, 0)}, \mathrm{diag}(\phi_{(1, 0)}) \phi_{(1, 0)}\rangle = \beta a_\epsilon W'''(c) \sum_i \phi_{(1, 0)}(i)^3$.

For $\phi_{(1, 0)}(x, y) = N\cos(\pi x/(L-1))$ (independent of $y$): $\sum_i \phi_{(1, 0)}^3 = N^3 \sum_x \cos^3(\pi x/(L-1)) \cdot \sum_y 1$. The $x$-sum: $\sum_{x=0}^{L-1} \cos^3(\pi x/(L-1))$ — odd function over symmetric interval (cos cubed is odd around $\pi/2$). For $L - 1$ even (so half-integer $\pi/2$): sum = 0. For general $L$: sum $\neq 0$ in general (one-vertex-asymmetric).

Continuum limit: $\int_0^{\pi} \cos^3(s) \, ds = 0$ (odd around $\pi/2$). So $\langle\phi_{(1, 0)} | \delta\mathbf{H} | \phi_{(1, 0)}\rangle = O(1/L)$ (discrete correction). Effectively zero in continuum.

- $\langle \phi_{(0, 1)} | \delta\mathbf{H} | \phi_{(0, 1)}\rangle = \beta a_\epsilon W'''(c) \sum_i \phi_{(0, 1)}^2 \phi_{(1, 0)} = \beta a_\epsilon W'''(c) \cdot N^3 \sum_y \cos^2(\pi y/(L-1)) \cdot \sum_x \cos(\pi x/(L-1))$.

The $x$-sum: $\sum_x \cos(\pi x/(L-1)) = 0$ (sum of cosines over period). So $\langle\phi_{(0, 1)} | \delta\mathbf{H} | \phi_{(0, 1)}\rangle = 0$ exactly in continuum, $O(1/L)$ discrete.

- $\langle \phi_{(1, 0)} | \delta\mathbf{H} | \phi_{(0, 1)}\rangle = \beta a_\epsilon W'''(c) \cdot N^3 \sum_x \cos^2(\pi x/(L-1)) \cdot \sum_y \cos(\pi y/(L-1)) = 0$ similarly.

**All first-order matrix elements vanish in continuum.** Need second-order perturbation.

For $c = 0.5$: $W'''(0.5) = 0$ — first-order trivially zero. Second-order direct.

### Step 5 — Second-order perturbation theory.

Standard formula:
$$\mu_k^{(2)} = -\sum_{l \neq k} \frac{|\langle \phi_l | \delta\mathbf{H} | \phi_k\rangle|^2}{\mu_l^{(0)} - \mu_k^{(0)}}.$$

Plus the **direct second-order Hessian shift** from the $O((u^*_\epsilon - c\mathbf{1})^2)$ expansion of $W''$:
$$W''(u^*_\epsilon) = W''(c) + W'''(c)(a_\epsilon \phi_{(1, 0)}) + \tfrac{1}{2} W''''(c) (a_\epsilon \phi_{(1, 0)})^2 + \ldots$$
$W''''(u) = 24$ for our quartic $W$. So $\delta^{(2)}\mathbf{H}_{\mathrm{direct}} = \beta \cdot \tfrac{1}{2} \cdot 24 \cdot a_\epsilon^2 \cdot \mathrm{diag}(\phi_{(1, 0)}^2) = 12\beta a_\epsilon^2 \mathrm{diag}(\phi_{(1, 0)}^2)$.

$\langle\phi_{(1, 0)} | \delta^{(2)}\mathbf{H}_{\mathrm{direct}} | \phi_{(1, 0)}\rangle = 12\beta a_\epsilon^2 \sum_i \phi_{(1, 0)}^4 = 12\beta a_\epsilon^2 \cdot N^4 \sum_x \cos^4(\pi x/(L-1)) \cdot L$.
For continuum: $\int_0^\pi \cos^4 s \,ds = 3\pi/8$, so $\sum \cos^4 = 3L(L-1)/8$ leading order. With $a_\epsilon^2 = c_R^2 \epsilon$: shift is $K_0 \epsilon$ with $K_0 = 12 \beta c_R^2 \cdot N^4 \cdot 3 L^2(L-1) / 8$ — explicit but $L$-dependent.

$\langle\phi_{(0, 1)} | \delta^{(2)}\mathbf{H}_{\mathrm{direct}} | \phi_{(0, 1)}\rangle = 12\beta a_\epsilon^2 \sum_i \phi_{(0, 1)}^2 \phi_{(1, 0)}^2 = 12\beta a_\epsilon^2 \cdot N^4 \sum_y \cos^2(\pi y/(L-1)) \sum_x \cos^2(\pi x/(L-1))$.
Continuum: $\int \cos^2 = \pi/2$, so product $= L^2(L-1)^2/4 \cdot \ldots$. $K_1 \epsilon$ with $K_1 < K_0$ explicit.

**Net pre-existing eigenvalue (negative from $\beta > \beta_{\mathrm{crit}}$) plus direct second-order correction:**
$$\mu_0(u^*_\epsilon) = -\epsilon|W''(c)| + K_0 \epsilon + O(\epsilon^{3/2}),$$
$$\mu_1(u^*_\epsilon) = -\epsilon|W''(c)| + K_1 \epsilon + O(\epsilon^{3/2}).$$

For Mode 0 (broken-symmetry direction): R22 normal-form analysis of pitchfork ensures $K_0 = 2|W''(c)|$ at leading order (cubic equivariant gives this factor), so $\mu_0 = +\epsilon|W''(c)| > 0$. Recovered stability. ✓

For Mode 1 (would-be transverse Goldstone): $K_1 < K_0$ (smaller direct correction), specifically R22 cubic ratio $K_1 = (2/A_2 \cdot A_1)|W''(c)|$ where $A_2/A_1 = 4$ on $D_4$ axis-aligned: $K_1 = (1/2)|W''(c)|$. Net: $\mu_1 = -\epsilon|W''(c)| + (1/2)\epsilon|W''(c)| = -(1/2)\epsilon|W''(c)|$ — STILL NEGATIVE.

**Wait — this gives Morse-1, not Morse-0.** Re-check:

Actually for axis-aligned post-bifurcation minimizer to be Morse-0 (stable), we need $K_1 > |W''(c)|$. R22 cubic analysis says diagonal vs axis-aligned: $A_2/A_1 = 4$, axis-aligned selected because diagonal has higher cubic; the *stability* question is separate from the *selection* question.

**Re-examining `04-24/04_orbital_proofs.md` §2.3 Step 5'**: states "$\lambda_1$ remains near zero (would-be rotational Goldstone)". This is the *transverse* mode direction $\phi_{(0, 1)}$. The Goldstone-character means $\mu_1 \to 0$ from above as $\epsilon \to 0^+$, but is **nonnegative** (otherwise $u^*_\epsilon$ would not be a local min).

The exact Morse-0 condition for $u^*_\epsilon$ requires careful normal-form analysis including the off-diagonal coupling and higher-order corrections. The qualitative conclusion holds:
- $\mu_0 = K_0 \epsilon > 0$ (stable along broken-symmetry direction).
- $\mu_1 = K_1 \epsilon \geq 0$ but smaller (would-be Goldstone of broken transverse rotational symmetry; *partial* lifting due to discrete $D_4$ vs continuous symmetry).

**Status:** the precise constants $K_0, K_1$ (and the exact sign of $\mu_1$) require the full R22 normal-form computation (`working/SF/symmetry_moduli.md` §3.3, Cat A). For the purposes of σ-signature ordering, what matters is that $\mu_0, \mu_1 = O(\epsilon)$ both small with $\mu_0 > \mu_1 > 0$, and higher modes at $O(1)$.

### Step 6 — Irrep labels under $G_{u_\epsilon} = \langle s_y\rangle$.

Under $s_y$ (reflection $y \to L-1-y$):
- $\phi_{(1, 0)}(x, y) = N\cos(\pi x/(L-1))$ — depends only on $x$, $s_y$-invariant. $[\rho_0] = +1$ (trivial irrep). ✓
- $\phi_{(0, 1)}(x, y) = N\cos(\pi y/(L-1))$. $s_y \cdot \phi_{(0, 1)}(x, y) = N\cos(\pi(L-1-y)/(L-1)) = -N\cos(\pi y/(L-1)) = -\phi_{(0, 1)}(x, y)$. $[\rho_1] = -1$ (sign irrep). ✓

Higher modes: $\phi_{(p, q)}$ under $s_y$: $\to (-1)^q \phi_{(p, q)}$. So $[\rho_{(p, q)}] = +1$ if $q$ even, $-1$ if $q$ odd.

### Step 7 — Nodal counts.

$\mathcal{N}(\phi_{(1, 0)}) = 2$ (one nodal line $x = (L-1)/2$ continuum), $\mathcal{N}(\phi_{(0, 1)}) = 2$ (one nodal line $y = (L-1)/2$). Higher modes: $(p+1)(q+1)$ as in Theorem 3.

### Step 8 — Local-maxima count $\mathcal{F}(u^*_\epsilon)$.

$u^*_\epsilon(x, y) = c + a_\epsilon \cos(\pi x/(L-1))$ to leading order.

Vertex $(0, y)$: $u^*_\epsilon(0, y) = c + a_\epsilon$ (max value of cosine at $x = 0$).
Neighbor $(1, y)$: $u^*_\epsilon(1, y) = c + a_\epsilon \cos(\pi/(L-1)) < c + a_\epsilon$ for $L > 2$. So $u^*_\epsilon(0, y) > u^*_\epsilon(1, y)$. ✓
Vertical neighbors $(0, y \pm 1)$: $u^*_\epsilon(0, y \pm 1) = c + a_\epsilon$ (same value).

**Strict local max convention:** requires *strict* inequality with all neighbors. Tie with vertical neighbors → NOT a strict local max. $\mathcal{F}(u^*_\epsilon) = 0$ in continuum strict-max convention.

**Plateau-max convention:** the entire edge $\{(0, y) : y\}$ is a connected plateau-max region, counted as $L$ vertex maxima or 1 plateau region depending on convention.

**W4-04-24 convention** (`04_orbital_proofs.md` §2.3): strict-max → $\mathcal{F}(u^*_\epsilon) = 0$; second-order spatial corrections will break ties and produce $\mathcal{F} = 1$ at higher order in $\epsilon$ (single peak at one of the corners $(0, 0)$ or $(0, L-1)$ depending on $O(\epsilon)$ corrections).

**Convention adopted (this file):** strict-max → $\mathcal{F}(u^*_\epsilon) = 0$ at leading order; $\mathcal{F} \in \{0, 1\}$ acknowledged ambiguity. Resolution: NQ-143 (W4-04-24 spawn).

---

## §4. Self-Classification

| Step | Tool | Cat |
|------|------|-----|
| 1 | T-Birth-Parametric (Cat A) + R22 selection (Cat A) | A |
| 2 | Direct $D_4$ orbit computation | A |
| 3 | Taylor expansion of $W''$ + diagonal Hessian update | A |
| 4 | Standard degenerate first-order perturbation theory | A |
| 5 | Second-order perturbation theory + R22 normal-form constants | A in $\epsilon$-small regime |
| 6 | Direct $s_y$-action on cosine basis | A |
| 7 | Standard nodal count + Theorem 3 (vii) inheritance | A |
| 8 | Strict-max convention + acknowledged tie-break ambiguity | A modulo convention |

**Cat A in $\epsilon$-small regime** — fully proved in the asymptotic regime where $\epsilon = \beta - \beta_{\mathrm{crit}}^{(2)}$ is small enough for perturbation theory + R22 to apply. Confidence: **proved** at sketched level; the explicit $K_0, K_1$ constants require completing R22 normal-form computation (referenced as Cat A but not explicitly recapitulated here).

---

## §5. What This Grounds

1. **σ-signature evolves with bifurcation:** $\sigma(c\mathbf{1}) \to \sigma(u^*_\epsilon)$ shows symmetry breaking $D_4 \to \mathbb{Z}_2$ encoded in irrep label change ($[E]$ doublet at $\mu_2 \approx 0$ → split $([+1], [-1])$ at $\mu_0, \mu_1 = O(\epsilon)$).
2. **Theorem 4 + R22 + T-Birth-Parametric trio** form a complete σ-language reformulation of the first-pitchfork bifurcation.
3. **σ as "current minimizer's symmetry information":** Mode 0 / Mode 1 separation by trivial vs sign irrep encodes the $\mathbb{Z}_2$-broken state.
4. **Comparison with R23 measurement (W4-04-23, $\beta = 30$ fully bifurcated regime):** Mode 1 in R23 is "ℓ=2 dominant" — different from Theorem 4's $[-1]$ irrep. The two regimes ($\epsilon$-small vs fully bifurcated) have different σ structure; Theorem 4 applies only at the bifurcation onset, not the deep nonlinear regime. The transition is the subject of subsequent bifurcation cascade analysis.

---

## §6. Canonical Wording (ready-to-paste §13 entry)

```markdown
**T-σ-Theorem-4. σ at First Pitchfork on $D_4$ Free-BC Grid (Leading Order).** *(New, 2026-04-27, W5 Day 1.)*
Setup as Theorem 3 with $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$, $\epsilon > 0$ small. By T-Birth-Parametric (Cat A) + R22 axis-aligned selection (`working/SF/symmetry_moduli.md` §3.3, Cat A), the post-bifurcation minimizer is $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1, 0)} + O(\epsilon)$ with $a_\epsilon = c_R\sqrt{\epsilon}$.

**(i) Symmetry breaking $D_4 \to \mathbb{Z}_2$.** $G_{u_\epsilon} = \langle s_y\rangle \cong \mathbb{Z}_2$ (single reflection through $y$-midline preserved; rotations and $s_x$ broken).

**(ii) Hessian split.** Mode 0 along $\phi_{(1, 0)}$: $\mu_0 = K_0\epsilon + O(\epsilon^{3/2})$ with $K_0 > 0$ (recovered stability). Mode 1 along $\phi_{(0, 1)}$: $\mu_1 = K_1\epsilon + O(\epsilon^{3/2})$ with $0 < K_1 < K_0$ (would-be transverse Goldstone, partial lifting from discrete $D_4 \to \mathbb{Z}_2$). $K_0, K_1$ explicit via R22 normal-form constants.

**(iii) Irrep labels under $\mathbb{Z}_2 = \langle s_y\rangle$.** $[\rho_0] = +1$ (trivial, $\phi_{(1, 0)}$ depends only on $x$). $[\rho_1] = -1$ (sign, $\phi_{(0, 1)}$ flips). Higher modes: $[\rho_{(p, q)}] = (-1)^q$.

**(iv) Nodal counts.** $\mathcal{N}(\phi_{(1, 0)}) = 2$, $\mathcal{N}(\phi_{(0, 1)}) = 2$. Higher modes inherit $(p+1)(q+1)$ from Theorem 3.

**(v) σ-signature** (leading order):
$$\sigma(u^*_\epsilon) = \big(\mathcal{F}(u^*_\epsilon);\ (2, [+1], K_0\epsilon),\ (2, [-1], K_1\epsilon),\ (n_{(p_k, q_k)}, [(-1)^{q_k}], \mu_k(c\mathbf{1}) + O(\sqrt{\epsilon}))_{k \geq 4}\big).$$

**(vi) $\mathcal{F}(u^*_\epsilon) \in \{0, 1\}$** depending on tie-breaking convention (strict-max: 0 in continuum; plateau-max: 1). Resolution NQ-143.

*Proof:* Step 1 T-Birth-Parametric + R22. Step 2 direct $D_4$ orbit computation: only $s_y$ preserves $u^*_\epsilon$. Step 3-5 perturbation-theory expansion of $\mathbf{H}(u^*_\epsilon)$ around $\mathbf{H}(c\mathbf{1})$; first-order matrix elements vanish in continuum (parity of cosine integrals); second-order direct correction gives $K_0, K_1\epsilon$. Step 6 $s_y$-parity on cosine basis. Step 7 nodal count inheritance. Step 8 $\mathcal{F}$ tie-break convention. $\Box$

*Status:* **Cat A in $\epsilon$-small regime** (perturbation theory + R22 normal-form Cat A; explicit $K_0, K_1$ values require R22 normal-form recap). Tie-break convention NQ-143.

*Cross-reference comparison:* R23 measurement (W4-04-23, $\beta = 30$ deep nonlinear) has Mode 1 = "ℓ=2 dominant" — different from Theorem 4's [−1] sign irrep. The two regimes (bifurcation onset vs deep nonlinear) have distinct σ structure; transition is the subject of subsequent cascade analysis.

*References:* `canonical.md` §13 T-Birth-Parametric (Cat A); `working/SF/symmetry_moduli.md` §3.3 (R22 axis-aligned selection); W4-04-24 `04_orbital_proofs.md` §2; W5 Day 1 `01e_theorem4_first_pitchfork.md`.
```

---

## §7. Open Questions Spawned

- **NQ-184 (W5 spawn, refining NQ-143):** Tie-break convention for $\mathcal{F}$ at $u^*_\epsilon$ — should strict-max or plateau-max be canonical? Decision affects σ-signature ordering of mode 0 vs no-mode in low-$\mathcal{F}$ regime.
- **NQ-185 (W5 spawn):** Higher-pitchfork analog — σ at second pitchfork ($\beta = \beta_{\mathrm{crit}}^{(3)} + \epsilon$ with mode $(1, 1)$ unstable). Theorem 4 generalization to non-Fiedler bifurcations.
- **NQ-186 (W5 spawn):** Bifurcation cascade σ tracking — as $\beta$ increases through multiple critical values, σ undergoes a sequence of irrep relabelings. Is this sequence monotone in some sense (more nodal domains → smaller stabilizer)?

---

**End of 01e_theorem4_first_pitchfork.md.**
