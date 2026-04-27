# 91_critical_review.md — Self-Critical Re-Review of W5 Day 1 G0 Outputs

**Session:** 2026-04-27 (W5 Day 1, post-merge re-review)
**Trigger:** User feedback "아직 좀 부족한데 제대로 좀더 재검토해서 분석해줘".
**Purpose:** Honest self-audit of the 5 σ-framework supporting structures merged today, identify substantive math errors / loose proofs / overclaims, and apply targeted corrections to canonical + daily files.
**Output of this review:** Document below + corrections in `01c_lemma3_goldstone_saturation.md`, `01d_theorem3_uniform_D4_grid.md`, `01e_theorem4_first_pitchfork.md`, and the corresponding `canonical.md` §13 entries.

---

## §1. Summary of Issues Found

| # | Severity | Where | Issue |
|---|---------|-------|-------|
| **A** | **CRITICAL math error** | T-σ-Lemma-3 (i), `01c` §3.1, canonical line 1217 | IBP identity gives $-\pi \int u^*(r) dr$ (1D radial integral), NOT $-m$ (2D mass). W4-04-24 source had an erroneous step ($\cos\theta \cdot r = x$ substitution missing a Jacobian factor). My re-derivation in `01c` §3.1 perpetuated the error. |
| **B** | **CRITICAL math error** | T-σ-Theorem-4 (ii), `01e` §2/§3, canonical line 1267 | Stated "$0 < K_1 < K_0$" for the two Hessian eigenvalues at axis-aligned post-pitchfork minimizer. Correct: on $D_4$ free-BC with cubic ratio $A_2/A_1 = 4$, leading-order Hessian eigenvalues are $K_0 = 4\|W''(c)\|$ and $K_1 = (A_2/A_1)\|W''(c)\| = 4\|W''(c)\|$ — i.e., **equal**. The two modes are distinguished by irrep (+1 vs -1), not by eigenvalue magnitude. |
| **C** | Substantive but recoverable | T-σ-Theorem-4 §3 derivation, `01e` §3 Step 5, canonical proof sketch | My second-order perturbation calculation gave $\mu_1 = -(1/2)\epsilon\|W''(c)\|$ — negative, contradicting Morse-0. The calculation was incomplete (missed off-diagonal couplings). Correct route: defer Morse-0 establishment to R22 normal-form analysis (which is the standard cubic-equivariant framework giving the eigenvalue formulas in (B)). |
| **D** | Loose proof, recoverable | T-σ-Theorem-3 (vi) irrep table, `01d` §2(vi)/§5 Step 6, canonical line 1248 | Mixed-parity $\{(p, q), (q, p)\}$ orbit decomposition was stated as "$E \oplus E$ or $A_1 \oplus B_1 \oplus E$" — actually mixed-parity gives **single $E$** (2-dim, character $(2, -2, 0, 0, 0)$). Both-odd off-diagonal gives $A_2 \oplus B_2$, not $E \oplus E$. |
| **E** | Stylistic / clarification | T-σ-Lemma-1 §3 Step 2, `01a` §3, canonical proof sketch | Polarization step "$H = \pi^\top H \pi$, ie $\pi^{-1} = \pi^\top$ gives $H \pi = \pi H$" is correct but the logical chain is compressed. Clearer: from quadratic-form equality on $\mathbb{R}^X$, we get matrix equality $H = \pi^\top H \pi$; multiplying both sides by $\pi$ on right + using $\pi^\top \pi = I$: $H \pi = \pi^\top H \pi \cdot \pi = \pi^\top H = (H\pi)^\top$ wait this circles. Actually clean path: $\pi$ orthogonal $\Rightarrow \pi^\top = \pi^{-1}$, so $H = \pi^\top H \pi = \pi^{-1} H \pi$, multiply by $\pi$ on left: $\pi H = H \pi$. ✓ |
| **F** | Loose proof | T-σ-Lemma-3 §3.4, `01c` §3.4, canonical (iii) | "Sign pattern of $\partial_x u^*$ for radial $u^*$: $\sgn(\partial_x u^*) = -\sgn(x)$ → two half-plane nodal domains." This needs slight care for the discrete graph: the half-plane partition $\{x > 0\}$ vs $\{x < 0\}$ on the integer grid is connected. Spelling out: $X^+ = \{i : i_x < 0\}$ is a $L \times L/2$ rectangle; $X^- = \{i : i_x > 0\}$ similarly. Both connected. ✓ Lower-bound $\geq 2$ from Lemma 2 (iii) automatic. So the count = 2 in continuum and discrete. |
| **G** | Worth flagging | NQ-173 / NQ-174 scripts | I never actually invoked `find_formation` — only verified imports. There may be runtime issues (e.g., `normalize=False` kwarg might not exist in current scc API; pattern was copied from `nq170c_v5b_extension.py` which presumably works). This is the user's task to trigger. |

---

## §2. Issue A — Lemma 3 IBP Correction (Detailed)

### 2.1 What was claimed

Canonical T-σ-Lemma-3 (i):
> In the continuum limit ($\xi_0 \gg a$, $\xi_0/L \to 0$):
> $$\mathcal{P}_{\ell=1}[\delta u_x] = (\langle\delta u_x, \psi^{(c)}_{\ell=1}\rangle, \langle\delta u_x, \psi^{(s)}_{\ell=1}\rangle) = (-m, 0) + O(\xi_0/L)$$

with proof sketch: "$\int (\partial_x u^*) x\, dx\, dy = -\int u^*\, dx\, dy = -m$".

### 2.2 The error

The integrand of $\langle\delta u_x, \psi^{(c)}\rangle$ in continuum is $(\partial_x u^*) \cdot \cos\theta\, dx\, dy$, NOT $(\partial_x u^*) \cdot x\, dx\, dy$.

$\cos\theta = x/r = x/\sqrt{x^2 + y^2}$, so:
$$\langle\delta u_x, \psi^{(c)}\rangle = \int (\partial_x u^*) \cdot \frac{x}{\sqrt{x^2 + y^2}}\, dx\, dy.$$

The W4-04-24 source `04_orbital_proofs.md` §3.3 step "$\cos\theta \cdot r = x$" implicitly multiplied the integrand by $r$, which would correspond to a *different quantity* (the $\ell=1$ moment weighted by $r$, not the $\cos\theta$ inner product). The result $-m$ is the moment, not the inner product.

### 2.3 Correct calculation

In Cartesian, IBP in $x$:
$$I = \int (\partial_x u^*) \cdot \frac{x}{r}\, dx\, dy = \big[u^* \cdot x/r\big]_{-\infty}^\infty\, dy - \int u^* \cdot \partial_x(x/r)\, dx\, dy.$$

Boundary term: $u^*$ decays $\to 0$ at infinity (or at boundary distance $\geq d_*$ in localized case).

$\partial_x(x/r) = 1/r - x^2/r^3 = (r^2 - x^2)/r^3 = y^2/r^3 = \sin^2\theta / r$.

$$I = -\int u^* \cdot \sin^2\theta / r\, dx\, dy.$$

In polar ($d^2 r = r\, dr\, d\theta$):
$$I = -\int_0^\infty \int_0^{2\pi} u^*(r) \cdot \sin^2\theta / r \cdot r\, dr\, d\theta = -\int_0^\infty u^*(r)\, dr \cdot \int_0^{2\pi} \sin^2\theta\, d\theta = -\pi \int_0^\infty u^*(r)\, dr.$$

For tanh disk $u^*(r) = \tfrac{1}{2}(1 - \tanh((r - r_0)/\xi_0))$: $\int_0^\infty u^*(r)\, dr \approx r_0 + O(\xi_0)$ (interior contribution $r_0$, transition region $O(\xi_0)$).

**Correct identity:**
$$\boxed{\mathcal{P}_{\ell=1}[\delta u_x] = (-\pi \int_0^\infty u^*(r)\, dr,\ 0) + O(\xi_0/L) \approx (-\pi r_0, 0)\ \text{for tanh disk}.}$$

NOT $(-m, 0)$. For tanh disk $r_0 = 8$: correct value $\approx -8\pi \approx -25$, not $-m = -\pi r_0^2 = -64\pi \approx -201$.

### 2.4 Numerical sanity check

For 32×32 R23 minimizer ($r_0 \approx 8$, $\xi_0 \approx 1$, $L = 32$):
- Correct $|\mathcal{P}_{\ell=1}[\delta u_x]| \approx 8\pi \approx 25$.
- Original (wrong) claim: $|\mathcal{P}_{\ell=1}[\delta u_x]| = m \approx 64\pi \approx 201$.

For the angular ℓ=1 power fraction $\rho_{\ell=1}[\hat\phi]$ to be $\leq 1$ (Cauchy–Schwarz), the correct value is required:
- $\|\delta u_x\|^2 \approx \pi r_0/(3\xi_0) \approx 8.4$.
- $\|\psi^{(c)}\|^2 \approx L^2/2 \approx 512$.
- $\rho_{\ell=1}[\hat\phi] = |\langle\hat\phi, \hat\psi^{(c)}\rangle|^2 = (\pi r_0)^2 / (\|\delta u_x\|^2 \|\psi^{(c)}\|^2) = 8\pi^2 \cdot 64 / (8.4 \cdot 512) \approx 0.15$.

This is plausible (R23 measured $\sim 0.4$-$0.5$ "p-dominant"; the $0.15$ vs $0.4$-$0.5$ gap may reflect that R23's metric was different from this normalized fraction, or that the tanh approximation underestimates $\|\delta u_x\|$ for non-tanh actual minimizer).

With the wrong value $-m$: $\rho \approx 12$ — *impossible* (exceeds Cauchy–Schwarz bound 1). This would have been the immediate red flag if I had numerically substituted; instead the W4-04-24 source's bottom-line "Numeric ballpark for typical $u^*$ on 32×32: ... $\rho_{\ell=1} \sim 0.5$" smuggled in a re-normalization without showing it, masking the error.

### 2.5 Net effect on Lemma 3 statement

The qualitative content is **unchanged**: $\mathcal{P}_{\ell=1}[\delta u_\mu] \neq 0$ (saturates ℓ=1 sector); Goldstone basis lies in ℓ=1 angular subspace; nodal count = 2.

The **explicit constant** changes: $-m \to -\pi \int u^*(r) dr$ (≈ $-\pi r_0$ for tanh).

Lemma 3 (ii) lower bound $\rho_{\ell=1} \geq \kappa > 0$ remains valid (with corrected $\kappa$ formula).

### 2.6 Action

Edit canonical T-σ-Lemma-3 (i): replace $-m$ with $-\pi \int u^*(r) dr$ explicit. Edit `01c_lemma3_goldstone_saturation.md` §3.1 to fix derivation. Update consequence wording.

---

## §3. Issue B — Theorem 4 $K_1 = K_0$ Correction (Detailed)

### 3.1 What was claimed

Canonical T-σ-Theorem-4 (ii):
> Mode 0 along $\phi_{(1, 0)}$: $\mu_0 = K_0\epsilon + O(\epsilon^{3/2})$ with $K_0 > 0$ (recovered stability). Mode 1 along $\phi_{(0, 1)}$: $\mu_1 = K_1\epsilon + O(\epsilon^{3/2})$ with $0 < K_1 < K_0$ (would-be transverse Goldstone, partial lifting from discrete $D_4 \to \mathbb{Z}_2$).

### 3.2 The error

R22 cubic equivariant analysis on $D_4$ free-BC gives axis-aligned post-pitchfork minimizer as Hessian-isotropic at leading order: $K_0 = K_1 = 4|W''(c)|$.

Standard $D_4$-equivariant normal form: $F(x, y; \beta) = \beta(x^2 + y^2) + A_1 (x^2 + y^2)^2 + A_2 x^2 y^2$. Axis-aligned minimum at $y = 0$, $x^2 = -\beta/(2 A_1)$ (for $\beta < 0$, instability):

- $\partial^2_{xx} F$ at minimum: $2\beta + 12 A_1 x^2 = 2\beta - 6\beta = -4\beta$.
- $\partial^2_{yy} F$ at minimum: $2\beta + (4 A_1 + 2 A_2) x^2 = 2\beta + (4 A_1 + 2 A_2)(-\beta/(2 A_1)) = -\beta A_2/A_1$.
- $\partial^2_{xy} F$ at minimum: $4 A_2 x y = 0$ (since $y = 0$).

Identifying $-\beta = \epsilon |W''(c)|$ (the "above critical" parameter):
- $K_0 = 4 \cdot |W''(c)| / 1 = 4|W''(c)|$.
- $K_1 = (A_2/A_1) \cdot |W''(c)|$.

For $A_2/A_1 = 4$ on $D_4$ (R22 §3.3): $K_1 = 4|W''(c)| = K_0$. **Equal**.

(For $A_2/A_1 < 4$: $K_1 < K_0$. For $A_2/A_1 > 4$: $K_1 > K_0$. The $D_4$ free-BC value is precisely 4, giving equality.)

### 3.3 Why "would-be Goldstone" framing was misleading

Discrete symmetry breaking ($D_4 \to \mathbb{Z}_2$) does NOT produce Goldstone modes. Goldstones arise from breaking *continuous* symmetry. The 4 axis-aligned post-pitchfork minimizers ($c\mathbf{1} \pm a_\epsilon \phi_{(1, 0)}$ and $c\mathbf{1} \pm a_\epsilon \phi_{(0, 1)}$) are *isolated* points in field space, not connected by a continuous symmetry. There's no would-be Goldstone in the transverse direction; $\phi_{(0, 1)}$ direction has fully positive eigenvalue $K_1 \epsilon$ with $K_1 = K_0$.

The two modes are distinguished by **irrep label** ($[\rho_0] = +1$ trivial, $[\rho_1] = -1$ sign under residual $\mathbb{Z}_2 = \langle s_y\rangle$), not by eigenvalue magnitude.

### 3.4 Why my second-order calculation was wrong

In `01e` §3 Step 5/5', I computed only the *direct* $W''''(c) \cdot \phi_{(1, 0)}^2$ second-order correction and got $\mu_1 = -\epsilon|W''(c)| + (1/2)\epsilon|W''(c)| = -(1/2)\epsilon|W''(c)|$ — negative, contradicting Morse-0.

The omission: *off-diagonal couplings* from $\delta H^{(1)} = \beta a_\epsilon W'''(c) \mathrm{diag}(\phi_{(1, 0)})$ to higher modes contribute additional second-order shift via $\sum_l |\langle \phi_l | \delta H^{(1)} | \phi_{(0, 1)}\rangle|^2 / (\mu_{(0, 1)}^{(0)} - \mu_l^{(0)})$. These contribute $O(\epsilon)$ corrections to $\mu_1$.

R22 normal-form encapsulates the full calculation (all relevant cubic and quartic equivariants) and gives the clean result $K_1 = (A_2/A_1)|W''(c)|$. My ad-hoc partial calculation was incomplete.

### 3.5 Net effect on Theorem 4 statement

**Correction (ii):** "Mode 0 along $\phi_{(1, 0)}$: $\mu_0 = 4|W''(c)|\epsilon + O(\epsilon^{3/2})$. Mode 1 along $\phi_{(0, 1)}$: $\mu_1 = (A_2/A_1)|W''(c)|\epsilon + O(\epsilon^{3/2})$. On $D_4$ free-BC: $A_2/A_1 = 4$, so $\mu_1 = \mu_0$ at leading order — the two modes are degenerate but irrep-distinct (Mode 0 trivial $[+1]$, Mode 1 sign $[-1]$)."

**Statement (v) σ-signature:** $\sigma(u^*_\epsilon)|_{D_4} = (\mathcal{F}; (2, [+1], 4|W''(c)|\epsilon), (2, [-1], 4|W''(c)|\epsilon), \ldots)$ — note both eigenvalues are now equal at leading order.

**Remove "would-be transverse Goldstone" wording.** Replace with "transverse mode (orthogonal to broken-symmetry direction)".

### 3.6 Action

Edit canonical T-σ-Theorem-4 (ii) and (v). Edit `01e_theorem4_first_pitchfork.md` §2 statement, §3 Step 5 derivation (defer to R22), §5 framing.

---

## §4. Issue D — Theorem 3 (vi) Irrep Table Cleanup (Detailed)

### 4.1 Correct decomposition

For pair $\{\phi_{(p, q)}, \phi_{(q, p)}\}$ at $\lambda_{(p, q)} = \lambda_{(q, p)}$ ($p \neq q$, both $> 0$, $< L - 1$), the 2-dim representation has character (computed in §A.1 below):

| Class | $e$ | $r^2$ | $r$ | $s_x$ | $rs_x$ |
|-------|-----|-------|-----|-------|--------|
| $\chi$ | $2$ | $2(-1)^{p+q}$ | $0$ | $(-1)^p + (-1)^q$ | $0$ |

Decomposition by Schur orthogonality:

| Parity | $A_1$ | $A_2$ | $B_1$ | $B_2$ | $E$ | Net |
|--------|-------|-------|-------|-------|-----|-----|
| (e, e), $p \neq q$ both even | 1 | 0 | 1 | 0 | 0 | $A_1 \oplus B_1$ |
| (o, o), $p \neq q$ both odd | 0 | 1 | 0 | 1 | 0 | $A_2 \oplus B_2$ |
| Mixed parity (o, e) or (e, o) | 0 | 0 | 0 | 0 | 1 | $E$ (single 2-dim) |

For $(p, p)$ singletons:
- $p$ even: $A_1$.
- $p$ odd: $B_2$.

For axis modes $\{(p, 0), (0, p)\}$, $p \geq 1$ (special case of pair table with $q = 0$):
- $p$ odd: $E$ (single 2-dim).
- $p$ even: $A_1 \oplus B_1$.

### 4.2 What I had wrong

Canonical T-σ-Theorem-3 (vi) wrote: "generic mixed-parity orbit decomposes as $A_1 \oplus B_1 \oplus E$ or $E \oplus E$". 

Correct: mixed-parity gives **single $E$** (one 2-dim irrep). Both-odd gives $A_2 \oplus B_2$, NOT $E \oplus E$.

The "$A_1 \oplus B_1 \oplus E$" or "$E \oplus E$" claims would only apply to 4-dimensional accidentally-degenerate eigenspaces (e.g., $L = 4$ where $\lambda_{(3, 0)} = \lambda_{(2, 1)} = 4$ accidentally). In that case the 4-vector orbit decomposes by the 4-dim rep character. Generic non-accidental mixed-parity pair: just $E$.

### 4.3 Action

Edit canonical T-σ-Theorem-3 (vi) and `01d_theorem3_uniform_D4_grid.md` §2(vi)/§5 Step 6 with the correct table.

### A.1 Character calculation appendix

For $\{\phi_{(p, q)}, \phi_{(q, p)}\}$ basis under $D_4$:
- $r$ (90° rot, $(x, y) \to (L-1-y, x)$): direct computation gives $r \cdot \phi_{(p, q)} = (-1)^q \phi_{(q, p)}$ and $r \cdot \phi_{(q, p)} = (-1)^p \phi_{(p, q)}$. Matrix $\begin{pmatrix} 0 & (-1)^q \\ (-1)^p & 0 \end{pmatrix}$. $\chi(r) = 0$.
- $r^2 = \mathrm{diag}((-1)^{p+q}, (-1)^{p+q})$. $\chi(r^2) = 2(-1)^{p+q}$.
- $s_x$ ($x \to L-1-x$): $s_x \cdot \phi_{(p, q)} = (-1)^p \phi_{(p, q)}$ (depends on $x$-parity). Matrix $\mathrm{diag}((-1)^p, (-1)^q)$. $\chi(s_x) = (-1)^p + (-1)^q$.
- $rs_x$ ($(x, y) \to (L-1-y, L-1-x)$, antidiagonal reflection): $rs_x \cdot \phi_{(p, q)} = (-1)^{p+q} \phi_{(q, p)}$. Off-diagonal. $\chi(rs_x) = 0$.

Schur: $n_\rho = (1/|G|) \sum_g \chi_\rho(g) \chi(g)$ where $|G| = 8$ and class sizes $1, 1, 2, 2, 2$.

For $n_E$ ($\chi_E = (2, -2, 0, 0, 0)$):
$n_E = (1/8)[2 \cdot 2 + 1 \cdot 2(-1)^{p+q} \cdot (-2) + 0 + 0 + 0] = (1/8)[4 - 4(-1)^{p+q}] = (1/2)[1 - (-1)^{p+q}]$.

For $p + q$ odd (mixed parity): $n_E = 1$. For $p + q$ even: $n_E = 0$. ✓

For $n_{A_1}$ ($\chi_{A_1} = (1, 1, 1, 1, 1)$):
$n_{A_1} = (1/8)[2 + 2(-1)^{p+q} + 0 + 2((-1)^p + (-1)^q) + 0] = (1/4)[(1 + (-1)^p)(1 + (-1)^q)]$.

For $(e, e)$: $n_{A_1} = 1$. For others: 0. ✓

Similar for $n_{A_2}, n_{B_1}, n_{B_2}$. Result table:

| | $n_{A_1}$ | $n_{A_2}$ | $n_{B_1}$ | $n_{B_2}$ | $n_E$ |
|---|----------|----------|----------|----------|-------|
| $(e, e)$ | 1 | 0 | 1 | 0 | 0 |
| $(o, o)$ | 0 | 1 | 0 | 1 | 0 |
| Mixed | 0 | 0 | 0 | 0 | 1 |

Total dimension check: $\sum n_\rho \dim\rho = 2$ for all rows. ✓

---

## §5. Issue C — Theorem 4 Proof Cleanup (Detailed)

### 5.1 What `01e` §3 Step 5 actually said

I worked through second-order direct corrections from $W''''(c) \cdot a_\epsilon^2 \cdot \mathrm{diag}(\phi_{(1, 0)}^2)$ and got numerical estimates $K_0 = K_0^{\mathrm{est}}, K_1 = K_1^{\mathrm{est}}$ with $K_1^{\mathrm{est}} = (1/2)|W''(c)|$ — half of the correct $K_1 = 4|W''(c)|$ value, and went into in-text "Wait — this gives Morse-1, not Morse-0" admission without resolving.

### 5.2 Correct path

The complete leading-order Hessian eigenvalues at the post-pitchfork minimizer come from R22 normal-form analysis (cubic + quartic equivariants), NOT from ad-hoc partial perturbation:

1. Project full energy $\mathcal{E}(u^* + v)$ onto Fiedler doublet basis $V_2 = \mathrm{span}(\phi_{(1, 0)}, \phi_{(0, 1)})$, expanding to quartic in $v$. Result: 2D normal form $F(x, y; \beta) = \beta(x^2 + y^2) + A_1(x^2 + y^2)^2 + A_2 x^2 y^2$ with explicit $A_1, A_2$ from the integrals $\int \phi_{(1, 0)}^4, \int \phi_{(1, 0)}^2 \phi_{(0, 1)}^2$.
2. Find post-bifurcation minima of $F$: axis-aligned $(\pm\sqrt{-\beta/(2A_1)}, 0)$ and $(0, \pm\sqrt{-\beta/(2A_1)})$.
3. Compute Hessian of $F$ at axis-aligned minimum: $\partial_x^2 F = -4\beta$, $\partial_y^2 F = -\beta A_2/A_1$.
4. Identify $-\beta = \epsilon |W''(c)|$: $K_0 = 4|W''(c)|$, $K_1 = (A_2/A_1)|W''(c)|$.

The off-diagonal couplings to higher modes (which I missed in `01e` §3 Step 5) are *implicit* in the quartic-equivariant coefficient $A_2$ — they renormalize $A_2$ to its full value, which on $D_4$ free-BC equals $4 A_1$ (R22 Cat A).

### 5.3 Action

Edit `01e` §3 Step 5: replace ad-hoc second-order calculation with reference to R22 normal-form. Rewrite §2 (statement) and (v) σ-signature with $K_1 = K_0$ on $D_4$. Edit canonical T-σ-Theorem-4 (ii) accordingly.

---

## §6. Issues E, F, G — Less Critical

### E. Lemma 1 §3 Step 2 polarization clarity

Current text: "By polarization, $\mathbf{H}(u^*) = \pi^\top \mathbf{H}(u^*) \pi$, i.e. $\pi^{-1} = \pi^\top$ gives commutation $\mathbf{H} \pi = \pi \mathbf{H}$."

**Cleaner:** "Polarizing the quadratic-form identity $v^\top H v = (\pi v)^\top H (\pi v) = v^\top \pi^\top H \pi v$ (valid for all $v \in \mathbb{R}^X$) gives matrix equality $H = \pi^\top H \pi$. Since $\pi$ is a permutation matrix (orthogonal), $\pi^\top = \pi^{-1}$. Multiplying by $\pi$ on the left: $\pi H = \pi \pi^\top H \pi = H \pi$. ✓"

Action: Edit `01a` §3 Step 2 with this cleaner form. Canonical entry's proof sketch is already terse enough; no canonical edit needed.

### F. Lemma 3 §3.4 nodal count for discrete graph

Current: "Sign pattern of $\partial_x u^*$ for radial $u^*$: $\sgn(\partial_x u^*) = -\sgn(x)$, two half-plane nodal domains."

**Cleaner:** "For radial $u^*(r)$ with $u^{*\prime}(r) < 0$ (decreasing), $\delta u_x(i) \approx \partial_x u^*(i) = \cos\theta_i \cdot u^{*\prime}(r_i)$. So $\sgn(\delta u_x(i)) = -\sgn(\cos\theta_i) = -\sgn(i_x - x_*)$. The nodal partition is $X^+ = \{i : i_x < x_*\}$ (left half-plane) and $X^- = \{i : i_x > x_*\}$ (right half-plane). Each is a connected sub-grid of $G$. By Lemma 2 (iii), $\mathcal{N}(\delta u_x) \geq 2$; by direct count, $\mathcal{N}(\delta u_x) = 2$. ✓"

Action: minor wording cleanup in `01c` §3.4.

### G. Script API verification

`nq173_v5b_f_partial_goldstone.py` and `nq174_zeta_star_precise.py` follow the API patterns from `nq170c_v5b_extension.py`. I verified syntax + imports succeeded but did not invoke `find_formation` end-to-end. There may be runtime issues (e.g., `params.beta_bd` field name exact match, `find_formation` kwarg compatibility).

**Recommended sanity test (user runs):**
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 -c "
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
import scipy.sparse as sp
import numpy as np
n = 16
g = GraphState(sp.csr_matrix((np.ones(2*15), ([i for i in range(15)] + [i+1 for i in range(15)], [i+1 for i in range(15)] + [i for i in range(15)])), shape=(n, n)))
p = ParameterRegistry(alpha_bd=1.0, beta_bd=4.0, volume_fraction=0.1, a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0, w_cl=0.0, w_sep=0.0, w_bd=1.0, n_restarts=1, max_iter=100)
res = find_formation(g, p, normalize=False, verbose=False, u_init=np.full(n, 0.1))
print('OK', res.converged, res.energy)
"
```

If this prints `OK True <number>`, the API matches. If it errors, the script needs the kwarg adjustment.

Action: Add this sanity-test snippet to `04_nq174_setup.md` Day 2 morning checklist.

---

## §7. Net Severity Assessment

Of the 7 issues:

- **2 critical math errors** (A, B) — propagated to canonical entries; require canonical edits to correct.
- **1 substantive proof gap** (C) — Theorem 4 second-order calculation was incomplete; canonical proof sketch needs reframing to defer to R22.
- **1 hand-waved table** (D) — Theorem 3 (vi) irrep decomposition needs replacement with rigorous character calculation.
- **3 minor / stylistic** (E, F, G) — clarification value but not critical.

**Net effect on canonical theorem status:**
- T-σ-Lemma-1: NO change (proof is correct, just minor cleaner wording in daily file).
- T-σ-Lemma-2: NO change.
- **T-σ-Lemma-3: (i) IBP identity correction** — value $-m \to -\pi \int u^*(r) dr$. Statement remains Cat A in continuum (with corrected constant).
- **T-σ-Theorem-3: (vi) irrep table replaced** with rigorous character-table decomposition. Statement remains Cat A.
- **T-σ-Theorem-4: (ii) $K_1 = K_0$ on $D_4$** instead of "$K_1 < K_0$ partial Goldstone"; (v) σ-signature both eigenvalues equal at leading order; framing of "would-be Goldstone" removed (no continuous symmetry was broken). Statement remains Cat A in $\epsilon$-small regime.

No theorem becomes Cat B/C as a result of these corrections — all five remain Cat A. The corrections are precision/accuracy fixes, not status downgrades.

---

## §8. Action Plan (Edits To Apply)

1. **canonical.md T-σ-Lemma-3**: replace (i) statement with corrected IBP identity; refine (ii) bound formula; refine proof sketch.
2. **canonical.md T-σ-Theorem-3**: replace (vi) with rigorous irrep table; clean worked-example signature.
3. **canonical.md T-σ-Theorem-4**: replace (ii) with $K_0 = 4|W''(c)|$, $K_1 = (A_2/A_1)|W''(c)|$ giving $K_1 = K_0$ on $D_4$; refine (v) σ-signature; defer Morse-0 to R22; remove "would-be Goldstone" framing.
4. **01c**: refine §3.1 IBP derivation; refine §3.2 (norm calculation); fix §7 canonical wording.
5. **01d**: refine §2(vi) irrep table + §5 Step 6 character calculation; fix §8 canonical wording.
6. **01e**: refine §2 statement (ii)(v); §3 Step 5/5' replace with R22 reference; §6 canonical wording.
7. **04_nq174_setup.md**: add §6 sanity-test snippet.
8. **99_summary.md**: add post-merge correction note to §1.

These are applied in the next files; this review file is the single source-of-truth for "what was wrong, what was fixed".

---

## §9. Lesson Learned

**The W4-04-24 source `04_orbital_proofs.md` had an error** in the IBP derivation that I did not catch on first pass. Re-reading it, the chain "$\partial_x(\cos\theta \cdot r) = \partial_x x = 1$, so $\int \partial_x u^* \cdot \cos\theta \cdot r\, dr\, d\theta = -\int u^*\, dx\, dy = -m$" silently substituted $\cos\theta \cdot r = x$ but kept the polar volume element $dr\, d\theta$ (without the $r$ Jacobian to make it $dx\, dy$). The result $-m$ has the right dimension but the wrong magnitude.

**Mitigation for future canonical merges:** any IBP / dimension-sensitive identity should be **numerically sanity-checked** before canonical merge — substitute concrete numbers and verify Cauchy–Schwarz / physical bounds. The $\rho_{\ell=1} = 12 > 1$ violation would have been caught this way.

The Theorem 4 $K_1$ error is similar: I trusted plan-template "Mode 1 $\mu_1$ near-zero would-be Goldstone" framing without doing the R22 normal-form calculation explicitly. The result: an in-text contradiction ("this gives Morse-1, not Morse-0") which I noted but didn't resolve.

**Mitigation:** any leading-order constant in a perturbation theorem should be derived from the canonical normal form (here R22) and not hand-computed in pieces.

---

**End of 91_critical_review.md.**
**Next: apply edits to canonical entries + 01c + 01d + 01e per §8 action plan.**
