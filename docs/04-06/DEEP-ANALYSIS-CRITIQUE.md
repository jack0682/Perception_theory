# Adversarial Critique: Deep Analysis Team Outputs

**Date:** 2026-04-06
**Category:** critique
**Status:** complete
**Role:** Adversarial critic — attacking overlap analysis, M₂ landscape, and Morse theory claims
**Author:** critic-2 (adversarial agent)

---

## PART I: ATTACK ON OVERLAP ANALYSIS

### FLAW O-1: `formation_overlap` Uses Hard Thresholding, Not the Actual Overlap Functional

The overlap functional in the K-field energy is the **continuous inner product**:

$$\Omega(u^1, u^2) = \langle u^1, u^2 \rangle = \sum_x u^1(x) u^2(x)$$

But `scc/multi.py:421-437` implements `formation_overlap` as:

```python
supports = [(f >= theta_supp) for f in fields]  # theta_supp = 0.1
O[j, k] = float(np.sum(supports[j] & supports[k]))  # binary AND
```

This counts the number of nodes where **both** fields exceed 0.1. It is NOT the inner product. A configuration where $u^1(x) = 0.09$ and $u^2(x) = 0.09$ at every node reports **zero** overlap, but the true inner product is $\Omega = n \times 0.0081$. On a 400-node grid, that's $\Omega = 3.24$ — non-negligible.

**Consequence:** Any overlap analysis using `formation_overlap` systematically **underestimates** the true energy-relevant overlap. The "exact disjointness" claims in KFIELD-GLOBAL-STABILITY.md line 71 ($\langle u_1^*, u_2^* \rangle = 0.000000$) should be verified with the continuous inner product, not the binary count.

**Severity: MAJOR.** All overlap scaling conclusions based on `formation_overlap` are about the wrong quantity.

### FLAW O-2: `find_k_formations` Can Place Formations On Top of Each Other

The spatial initialization in `_spatial_init` (multi.py:214-234) uses Fiedler-based separation:

```python
v2 = graph.fiedler_vector()
percentiles = np.linspace(0, 100, K + 1)
lo = np.percentile(v2, percentiles[k])
hi = np.percentile(v2, percentiles[k + 1])
mask = ((v2 >= lo) & (v2 <= hi)).astype(float)
bias = 0.5 * mask + 0.5 * rng.randn(n)
```

The 50% random noise component means the initialization is only **weakly** biased toward spatial separation. On small grids (e.g., 5×5), the noise can dominate and both formations start nearly overlapping. Even if the optimizer eventually separates them, the question is: **does the optimizer always converge to the separated state?**

With only `n_restarts=3` and the adaptive step size scheme (multi.py:192-198), the optimizer could get stuck in a local minimum where formations partially overlap. The convergence criterion `max_gnorm < params.eps_grad` only checks gradient norm — a local minimum with partial overlap satisfies this condition.

**Attack:** Run `find_k_formations` on a 5×5 grid with K=2 and `lambda_rep=0.1`. The repulsion is too weak to overcome the spatial constraint, and the formations may overlap. The overlap analysis would then report non-zero overlap NOT because of tail leakage but because of **optimizer failure**.

**Severity: MODERATE.** Overlap measurements conflate physical overlap with optimization artifacts.

### FLAW O-3: The "Theoretical Minimum Overlap" Bound Is Wrong

If an overlap analysis claims the theoretical minimum overlap decays exponentially with distance (from the closure operator's diffusion kernel), this ignores a critical fact: **closure MODIFIES the tail**.

The closure operator is $\text{Cl}(u) = \sigma(a_{\text{Cl}}(Pu) + b_{\text{Cl}})$ where $P$ is the row-normalized adjacency and $\sigma$ is the logistic sigmoid. On a grid graph, $P$ is the random walk matrix. The field $u$ propagates via $P$, creating a "halo" around the formation core. The halo's spatial extent depends on $a_{\text{Cl}}$.

The key issue: the closure fixed point $u^* = \text{Cl}(u^*)$ satisfies:

$$u^*(x) = \sigma\Big(a_{\text{Cl}} \sum_y P(x,y) u^*(y) + b_{\text{Cl}}\Big)$$

For nodes far from the formation core, $\sum_y P(x,y) u^*(y) \approx 0$, so $u^*(x) \approx \sigma(b_{\text{Cl}})$. With default parameters $b_{\text{Cl}} = -5$, this gives $u^*(x) \approx \sigma(-5) \approx 0.0067$.

This means **every** node has $u^* \geq 0.0067$, regardless of distance from the core. Two formations on opposite ends of the grid have:

$$\langle u_1^*, u_2^* \rangle \geq n \times (0.0067)^2 = n \times 4.5 \times 10^{-5}$$

On a 400-node grid: $\Omega \geq 0.018$. **Not** zero, and **not** exponentially decaying — the tail is bounded below by a constant.

The tail doesn't decay exponentially; it **floors** at $\sigma(b_{\text{Cl}})$. Any overlap bound that assumes exponential decay is incorrect.

**Severity: MAJOR.** The "exact disjointness $\langle u_1^*, u_2^* \rangle = 0.000000$" reported in KFIELD-GLOBAL-STABILITY.md is numerically suspicious. Either (a) the formations are NOT closure fixed points, or (b) the inner product is nonzero at the level of $10^{-5}$ and was rounded to display as zero. Either way, the claim of exact disjointness is wrong.

### FLAW O-4: Numerical Precision of Overlap Measurement

Even if the true overlap is $\sim 10^{-5}$, the **energy** contribution is $\lambda_{\text{rep}} \times \Omega = 10 \times 10^{-5} = 10^{-4}$. This is negligible for optimization purposes. But the theoretical claim in KFIELD-GLOBAL-STABILITY.md Part (a) is that the lower bound $\sum_k E_{\text{self}}(u_k^*)$ is **achieved** when $\Omega = 0$. If $\Omega > 0$ always, then:

$$\mathcal{E}_K(u_1^*, u_2^*) = \sum_k E_{\text{self}}(u_k^*) + \lambda_{\text{rep}} \Omega > \sum_k E_{\text{self}}(u_k^*)$$

The lower bound is **not achieved**. The proof's "Achievability" step (line 35-39) is wrong. The K=2 state is NOT the global minimum — it is merely a local minimum with energy slightly above the lower bound.

This is a **logical** error, not a numerical one. The lower bound decomposition assumes $\Omega = 0$ is achievable, but the sigmoid floor makes this impossible on any finite connected graph.

**Severity: CRITICAL for Part (a) of KFIELD-GLOBAL-STABILITY.md.** The global minimality proof has a gap.

---

## PART II: ATTACK ON M₂ ENERGY LANDSCAPE

### FLAW M-1: Re-Optimization with 500 Gradient Steps May Not Converge

The M₂ landscape analysis (if implemented as described in the task) requires computing the optimal K=2 state at each mass split $(m_1, m_2)$. If using `find_k_formations` with `max_iter=500` (as in the `phase2_mode='reoptimize'` path, multi.py:363-370), convergence is not guaranteed.

The default optimizer uses `eps_grad` as convergence criterion (multi.py:202). For a 15×15 grid ($n = 225$), 500 iterations may be insufficient — the standard `find_formation` uses `max_iter=2000` and even that sometimes doesn't converge for extreme parameters.

**Attack:** If the M₂ landscape shows a smooth energy surface, check whether the gradient norm at each point is below `eps_grad`. If not, the "energies" are just snapshots of partially-optimized states, not true minima.

**Severity: MAJOR if convergence wasn't verified.**

### FLAW M-2: The "K=1 Limit" Comparison Is Wrong

The natural comparison for evaluating K=2 vs K=1 is $(m_1 = M, m_2 = 0)$ vs $(m_1 = m_1^*, m_2 = m_2^*)$. But $m_2 = 0$ is NOT on $\Sigma_{m_2}$ for any $m_2 > 0$ (this is the foundational point from MERGE-CRITIQUE.md Flaw #1).

A more informative comparison would be along the **constant-total-mass line**: $(m_1 = M - \epsilon, m_2 = \epsilon)$ as $\epsilon \to 0$. What happens to the energy in this limit?

Three scenarios:
1. **Energy diverges** as $\epsilon \to 0$ (formation at mass $\epsilon$ cannot form on the grid — too dilute). This would mean the M₂ landscape has a barrier near the boundary.
2. **Energy converges** to $E_{\text{self}}(u^*_{M})$ (the single-formation energy). This would mean K=2 continuously degenerates to K=1.
3. **Energy converges** to $E_{\text{self}}(u^*_{M}) + E_{\text{uniform}}(\epsilon)$ (single formation plus uniform background). This is the most likely scenario.

**Critical check:** For scenario 3, the energy at $(m_1 = M - 1, m_2 = 1)$ on a 225-node grid has $c_2 = 1/225 = 0.0044$. This is FAR outside the spinodal range $((3-\sqrt{3})/6, (3+\sqrt{3})/6) \approx (0.211, 0.789)$. The parameter validation in `params.py:122-132` would flag this as **FATAL**. The double-well has no phase separation at this volume fraction — the uniform state IS the global minimum for formation 2.

Therefore: **the M₂ landscape at extreme mass splits is computing the energy of a "formation" that cannot exist**. The self-energy of a field with $c = 0.004$ is dominated by the double-well term at the uniform state $W(c) = c^2(1-c)^2 \approx c^2$, not by a localized formation.

**Severity: CRITICAL.** The M₂ landscape near $(m_1 \approx M, m_2 \approx 0)$ is physically meaningless.

### FLAW M-3: EnergyComputer Uses Wrong `c` Parameter for Different Masses

This is the most insidious bug. In `find_k_formations` (multi.py:65-67):

```python
ec = EnergyComputer(graph, params)
ec.normalize_weights()  # Uses params.volume_fraction = 0.3
```

The `normalize_weights` method (energy.py:186-206) computes Hessian spectral norms at $u_0 = c \cdot \mathbf{1}$ where $c = 0.3$. These norms determine the effective weights $\lambda_i = w_i / (\sigma_i + \epsilon)$.

But for a formation at mass $m_2 = 5$ on a 225-node grid ($c_2 = 0.022$), the double-well curvature is:
$$W''(0.022) = 2(1 - 6 \times 0.022 + 6 \times 0.022^2) \approx 1.74$$

vs the normalization point:
$$W''(0.3) = 2(1 - 1.8 + 0.54) = -0.52$$

**The curvature flips sign!** At $c = 0.3$, the double-well is concave (favoring phase separation). At $c = 0.022$, it's convex (favoring uniformity). The Hessian normalization at $c = 0.3$ dramatically overweights the boundary term for low-mass formations, producing incorrect energy values.

**Consequence:** All energy comparisons between formations at different masses use incorrectly normalized weights. The M₂ landscape is computed with the wrong energy functional for non-equal mass splits.

**Severity: CRITICAL.** The shared EnergyComputer invalidates the entire M₂ landscape analysis.

### FLAW M-4: Mass Transfer Assumes Independent Fields — But They Share a Graph

The M₂ landscape analysis implicitly assumes that $u^1$ at mass $m_1$ and $u^2$ at mass $m_2$ can be independently optimized (aside from repulsion). But they live on the **same graph** and share the **same adjacency structure**.

On a 15×15 grid, a formation at $c = 0.3$ occupies roughly $0.3 \times 225 \approx 68$ nodes of the core. Two such formations need $\sim 136$ nodes. The grid has 225 nodes. This leaves only $\sim 89$ nodes as "background" — enough room.

But at extreme splits $(m_1 = 65, m_2 = 3)$, formation 1 wants $\sim 65$ core nodes and formation 2 wants $\sim 3$ core nodes. Formation 2 is so small it's essentially a single-node perturbation. The closure operator $\text{Cl}(u^2)$ at 3 nodes is just diffusion into neighbors — there's no self-reinforcing formation structure at this scale.

**Attack:** Does `find_k_formations` at $(m_1 = 65, m_2 = 3)$ actually find a localized formation for field 2, or does it return a diffuse smear? If it's a smear, the "formation energy" is meaningless — it's computing $E_{\text{cl}}$ of something that isn't a closure fixed point.

**Severity: MAJOR.** Small-mass formations may not be genuine formations.

### FLAW M-5: The Simplex Constraint $\Sigma u^k \leq 1$ Is NEVER Checked

The M₂ landscape analysis should verify that the optimal K=2 state at each mass split satisfies $u^1(x) + u^2(x) \leq 1$ for all $x$. The simplex barrier in the energy (multi.py:258-261) is a SOFT penalty:

```python
S = sum(fields)
violation = np.maximum(0.0, S - 1.0)
E += lambda_bar * float(violation @ violation)  # lambda_bar = 100
```

With $\lambda_{\text{bar}} = 100$, the penalty is quadratic. A violation of $\delta = 0.1$ at a single node costs $100 \times 0.01 = 1.0$ in energy. This is comparable to the self-energy terms, so the optimizer may tolerate small violations.

**Attack:** After the M₂ landscape optimization, compute $\max_x [u^1(x) + u^2(x)]$ at each mass split. If this exceeds 1.0, the "optimal" formations violate the theoretical simplex constraint. The energies are then not comparable to the theoretical energy on the constrained manifold $\{(u^1, u^2) : u^k \geq 0, \sum_k u^k \leq 1\}$.

**Severity: MODERATE.** Soft constraint violation may invalidate energy comparisons.

---

## PART III: ATTACK ON MORSE THEORY ANALYSIS

### FLAW MO-1: M₂ Is NOT a Smooth Manifold

The constraint manifold for K=2 with per-formation mass constraints is:

$$\Sigma^2_M = \Sigma_{m_1} \times \Sigma_{m_2} = \{u^k \in [0,1]^n : \sum u^k_i = m_k\}$$

Each $\Sigma_{m_k}$ is the intersection of a hyperplane ($\sum u_i = m$) with the unit cube $[0,1]^n$. This is a **convex polytope** — a manifold with corners, not a smooth manifold.

**Smooth Morse theory does not apply to manifolds with corners.** The standard Morse lemma requires a smooth chart around each critical point. At corner points (where multiple coordinates hit 0 or 1), the tangent space degenerates to a tangent cone. The Hessian is not well-defined on the boundary — KKT multipliers replace gradient conditions.

**What is needed instead:** Stratified Morse theory (Goresky-MacPherson) or Morse theory on manifolds with corners (Handron 2002). These theories exist but have different index counting rules and different connecting manifold structures. In particular:

- The Morse inequalities on manifolds with corners involve **boundary Morse indices** that differ from interior indices.
- The connecting manifolds (stable/unstable manifolds of gradient flow) may hit the boundary and bifurcate.
- The CW structure induced by a Morse function on a manifold with corners is more complex than the smooth case.

**Severity: MAJOR.** Any Morse-theoretic counting of critical points or index analysis must use the stratified version.

### FLAW MO-2: The Fibration $\pi : M_2 \to [0, M]$ Is NOT a Fiber Bundle

If the Morse analysis defines $\pi : M_2 \to [0, M]$ by $\pi(u^1, u^2) = m_2 = \sum u^2_i$, this is NOT a fiber bundle because:

1. **The fiber changes topology.** At $m_2 = 0$, the fiber $\pi^{-1}(0) = \Sigma_M \times \{0\}$ is a single copy of $\Sigma_M$ (the K=1 manifold). At $m_2 = \epsilon > 0$, the fiber $\pi^{-1}(\epsilon) = \Sigma_{M-\epsilon} \times \Sigma_\epsilon$ is a product of two polytopes of different dimensions if $\epsilon$ is so small that $\Sigma_\epsilon$ degenerates.

   Actually, $\Sigma_\epsilon$ for $0 < \epsilon < 1$ on $n$ nodes is diffeomorphic to the $(n-2)$-simplex times... no, $\Sigma_\epsilon = \{u \in [0,1]^n : \sum u_i = \epsilon\}$. For $\epsilon < 1$, the constraint $u_i \leq 1$ is automatically satisfied (since $\sum u_i = \epsilon < 1$ and $u_i \geq 0$). So $\Sigma_\epsilon \cong \Delta^{n-1}_\epsilon$ (the standard simplex scaled by $\epsilon$), which is diffeomorphic to $\Delta^{n-1}$ for all $\epsilon > 0$.

   At $\epsilon = 0$: the fiber is a single point $\{0\}$, which is 0-dimensional. At $\epsilon > 0$: the fiber is $(n-2)$-dimensional.

   **The fiber dimension jumps at $\epsilon = 0$.** This is a topological obstruction to being a fiber bundle.

2. **Ehresmann's theorem requires a submersion.** The map $\pi$ is a submersion at $(u^1, u^2)$ iff $d\pi$ is surjective. Since $\pi(u^1, u^2) = \sum u^2_i$, we have $d\pi = (0, \mathbf{1}^T)$. This is surjective whenever $u^2$ has a tangent direction that changes $\sum u^2_i$ — which it always does EXCEPT at the boundary of $\Sigma^2_M$. At boundary points where all coordinates of $u^2$ are at their constraints, $d\pi$ may fail to be surjective in the tangent cone.

**Severity: CRITICAL for the fibration argument.** Ehresmann's theorem is inapplicable at $m_2 = 0$.

### FLAW MO-3: The Blow-Up at $m_2 = 0$ Does Not Resolve the Singularity

If the Morse analysis proposes blowing up $\Sigma^2_M$ at $m_2 = 0$ by replacing $\{m_2 = 0\}$ with the exceptional divisor $\Sigma_1 = \{(u^1, v) : v \in \Sigma_1, u^1 \in \Sigma_{M}\}$ (the "directions" along which $u^2$ approaches zero), this construction has problems:

1. **$\Sigma_1$ is the simplex $\Delta^{n-1}$**, which parametrizes the shape of $u^2$ as its mass shrinks to zero: $u^2 = \epsilon \cdot v$ with $v \in \Sigma_1$. In projective terms, this is the projectivization of $\Sigma_\epsilon$ as $\epsilon \to 0$.

2. **The energy is singular on the blow-up.** As $\epsilon \to 0$, $\mathcal{E}_{\text{self}}(u^2) = \mathcal{E}_{\text{self}}(\epsilon v)$. The closure energy $E_{\text{cl}} = \|\text{Cl}(\epsilon v) - \epsilon v\|^2$. Since $\text{Cl}(\epsilon v) = \sigma(a \cdot P(\epsilon v) + b) \approx \sigma(b) + \sigma'(b) a \epsilon Pv + O(\epsilon^2)$, we get:

   $$\text{Cl}(\epsilon v) - \epsilon v \approx \sigma(b) + [\sigma'(b) a Pv - v] \epsilon + O(\epsilon^2)$$

   So $E_{\text{cl}} \approx n \sigma(b)^2 + O(\epsilon)$ — it converges to a constant (the closure energy of the zero field). The blow-up doesn't remove the energy singularity; it just parametrizes how you approach the singular fiber.

3. **The resolved space is not a smooth manifold.** The blow-up introduces a boundary component $\{0\} \times \Sigma_1$ that is a new face of the polytope. The "resolved" space is again a manifold with corners, and Morse theory still needs the stratified version.

**Severity: MAJOR.** The blow-up is a reasonable geometric idea but doesn't actually resolve the analytical difficulties.

### FLAW MO-4: Morse Index Counting on the Polytope Interior

If the Morse analysis computes critical point indices in the **interior** of $\Sigma^2_M$ (where $0 < u^k_i < 1$ for all $i, k$), then standard smooth Morse theory applies. The question is: **are the critical points of $\mathcal{E}_K$ actually in the interior?**

For the K=2 formations with moderate mass ($c \sim 0.3$), the optimal formation has a clear core-periphery structure: $u^*(x) \approx 1$ in the core and $u^*(x) \approx 0$ outside. The closure floor $\sigma(b_{\text{Cl}}) \approx 0.0067$ keeps the field strictly above 0, but the field may hit $u = 1$ in the core.

If $u^*(x) = 1$ for any node $x$, the critical point is on the **boundary** of $\Sigma_{m_k}$. The Morse index at boundary critical points involves the tangent cone, not the tangent space. Standard Morse theory gives incorrect index values.

**Attack:** Check whether the optimal formation field satisfies $u^*(x) < 1$ for all $x$. If any coordinate saturates at 1, the critical point is on the boundary and the Morse analysis of the interior is incomplete.

**Severity: MODERATE.** Depends on whether saturation actually occurs for typical parameters.

---

## PART IV: FUNDAMENTAL CHALLENGES

### FLAW F-1: "K=2 Is Global Min on $\Sigma^2_M$" — The Flip-Flop

The claim history:
1. **KFIELD-GLOBAL-STABILITY.md** (this session): "K=2 is the GLOBAL MINIMUM on $\Sigma^2_M$" (line 13, Part (a)).
2. **MERGE-BARRIER-KFIELD.md** (this session): "$(u_1^*, u_2^*)$ is a strict local minimum" (Theorem 2 Step 1) — NOT global.
3. **MERGE-CRITIQUE.md** (this session): "K=2 is metastable" — also NOT global.

**Which is it?** Let me resolve this:

- On **$\Sigma_{m_1} \times \Sigma_{m_2}$** (per-formation mass): K=2 with disjoint supports achieves $\mathcal{E}_K = \sum E_{\text{self}}(u_k^*)$. This IS the global minimum on this manifold, since the repulsion term $\geq 0$ and $E_{\text{self}}(u_k) \geq E_{\text{self}}(u_k^*)$ for each $k$. **CORRECT — but trivially so**, because the per-formation mass constraints eliminate all "merge-like" competitors.

- On **$\Sigma_M^{\text{relax}}$** (total mass only): K=2 competes with states like $(u_{\text{merged}}, u_{\text{uniform}})$ where $u_{\text{merged}}$ has mass $\sim M$ and $u_{\text{uniform}}$ has mass $\sim 0$. The self-energy $E_{\text{self}}(u_{\text{merged}})$ at mass $M$ can be **lower** than $E_{\text{self}}(u_1^*) + E_{\text{self}}(u_2^*)$ (isoperimetric ordering). So K=2 is NOT the global minimum on $\Sigma_M^{\text{relax}}$ — it is at best a local minimum.

**The KFIELD-GLOBAL-STABILITY proof is correct on $\Sigma_{m_1} \times \Sigma_{m_2}$ but the claim is misleadingly phrased.** It's "global minimum" on a manifold that was specifically designed to prevent merge. This is like proving "I can't lose a race if my competitors are banned from running."

**Severity: MAJOR (misleading claim).** The statement should be: "K=2 is the global minimum on $\Sigma_{m_1} \times \Sigma_{m_2}$, which is the constraint surface used in the implementation. On the larger space $\Sigma_M^{\text{relax}}$, it is a local minimum."

### FLAW F-2: Energy Comparisons Mix Different EnergyComputer Instances

Consider the energy comparison in KFIELD-GLOBAL-STABILITY.md (lines 65-71):

| State | E_self | E_rep | E_total |
|-------|--------|-------|---------|
| K=2 formations | 39.4 | 0.0 | 39.4 |
| u₁ form + u₂ uniform | 89.5 | 90.0 | 179.5 |

The "u₂ uniform" state at mass $m_2$ has $u^2 = m_2/n \cdot \mathbf{1}$. The self-energy $E_{\text{self}}(m_2/n \cdot \mathbf{1})$ is computed using the **same** EnergyComputer (with normalization at $c = 0.3$).

But the normalization weights $\lambda_{\text{cl}}, \lambda_{\text{sep}}, \lambda_{\text{bd}}$ were computed for the Hessian at $u = 0.3 \cdot \mathbf{1}$, NOT at $u = m_2/n \cdot \mathbf{1}$. If $m_2 = 0.15 \times 225 = 33.75$ (for a 15×15 grid with equal split), $c_2 = 0.15$. The normalization at $c = 0.3$ assigns different effective weights than normalization at $c = 0.15$ would.

For the extreme case $m_2 = 1$ (single-node mass), $c_2 = 0.004$. The normalization weights at $c = 0.3$ are completely wrong for this regime — the energy is meaningless.

**But does this actually matter?** The `normalize_weights` call happens once. The energy computation itself (energy_bd, energy_cl, energy_sep) uses the raw field $u$, not the normalization point. The normalization only affects the **weighting** of the three terms. So the individual $E_{\text{bd}}, E_{\text{cl}}, E_{\text{sep}}$ values are correct — it's only their relative weighting that's calibrated for $c = 0.3$.

**Severity: MODERATE.** The energy values are computed correctly for each field, but the relative weighting is calibrated for a different regime. This doesn't invalidate the ordering (E_total(K=2) < E_total(merged)) but does make the quantitative gap unreliable.

### FLAW F-3: The Simplex Constraint Is Never Checked in KFIELD-GLOBAL-STABILITY

The proof in KFIELD-GLOBAL-STABILITY.md claims $\langle u_1^*, u_2^* \rangle = 0$ (disjoint supports). But it never checks whether $u_1^*(x) + u_2^*(x) \leq 1$ everywhere. Even with disjoint supports (under the binary threshold), the closure floor means:

$$u_1^*(x) + u_2^*(x) \geq 2\sigma(b_{\text{Cl}}) \approx 0.013 \quad \forall x$$

This is trivially below 1, so the simplex constraint is satisfied. But for formations with large cores approaching $u = 1$, if the cores overlap at ALL, we could have $u^1 + u^2 > 1$ at some nodes.

More importantly: the M₂ landscape analysis at non-equal mass splits may produce states where $u^1 + u^2 > 1$ in the overlap region. The soft penalty $\lambda_{\text{bar}} = 100$ allows small violations. If the M₂ landscape doesn't report $\max(u^1 + u^2)$, the "optimal" energies may include simplex violation penalties that make the energy comparison with the hard-constrained theory invalid.

**Severity: MODERATE.** Mainly affects M₂ landscape comparisons, not the stability proof itself.

### FLAW F-4: The Double-Well Energy at the Closure Floor

The closure floor $\sigma(b_{\text{Cl}}) \approx 0.0067$ means the "zero" regions of the field are not actually at $u = 0$ (the double-well minimum) but at $u \approx 0.0067$. The double-well energy at this floor is:

$$W(0.0067) = (0.0067)^2 \times (1 - 0.0067)^2 \approx 4.4 \times 10^{-5}$$

For $n$ nodes in the "zero" region ($\sim n - m$ nodes), the total contribution is:

$$\beta \times (n - m) \times 4.4 \times 10^{-5}$$

With $\beta = 50$ and $n - m = 160$: $\Delta E \approx 0.35$. Small but nonzero.

This energy contribution is **identical** for both formations, so it cancels in energy comparisons. But it contributes to the **absolute** energy value reported in the tables. More importantly, it means the "global minimum" on $\Sigma^2_M$ is NOT exactly $\sum E_{\text{self}}(u_k^*)$ — there's a correction from the closure floor.

**Severity: MINOR.** Quantitative correction, doesn't affect qualitative conclusions.

---

## PART V: META-CRITIQUE — WHAT'S ACTUALLY TRUE

Despite the flaws above, the core narrative is correct:

1. **K=2 formations are stable on $\Sigma_{m_1} \times \Sigma_{m_2}$.** This is trivially true because merge is topologically impossible. Theorem 1 of MERGE-BARRIER-KFIELD.md gets this right.

2. **K=2 formations are locally stable on $\Sigma_M^{\text{relax}}$.** This requires proving positive-definite Hessian on the LARGER tangent space (Flaw #9 from MERGE-CRITIQUE.md), but is almost certainly true for typical parameters.

3. **The merge barrier on $\Sigma_M^{\text{relax}}$ is positive.** Theorem 2 of MERGE-BARRIER-KFIELD.md is correct in principle, but the quantitative bounds are unreliable (Flaw M-3: wrong `c` parameter).

4. **The M₂ landscape analysis is unreliable** at extreme mass splits due to the wrong normalization and the impossibility of forming genuine formations at very low volume fractions.

5. **Morse theory on $\Sigma^2_M$ requires the stratified version.** Standard smooth Morse theory is insufficient for manifolds with corners.

---

## Summary of Flaws by Severity

| # | Flaw | Severity | Target |
|---|------|----------|--------|
| O-1 | `formation_overlap` uses wrong metric (binary vs L²) | **MAJOR** | Overlap analysis |
| O-3 | Closure floor prevents true disjointness | **MAJOR** | Overlap analysis |
| O-4 | Global min proof gap: $\Omega = 0$ not achievable | **CRITICAL** | KFIELD-GLOBAL-STABILITY Part (a) |
| M-2 | K=1 limit exits spinodal range | **CRITICAL** | M₂ landscape |
| M-3 | Wrong `c` in EnergyComputer normalization | **CRITICAL** | M₂ landscape |
| M-1 | 500-step convergence not guaranteed | **MAJOR** | M₂ landscape |
| M-4 | Small-mass "formations" aren't formations | **MAJOR** | M₂ landscape |
| MO-1 | Smooth Morse theory on polytope | **MAJOR** | Morse analysis |
| MO-2 | Fibration fails at $m_2 = 0$ (dimension jump) | **CRITICAL** | Morse analysis |
| MO-3 | Blow-up doesn't resolve singularity | **MAJOR** | Morse analysis |
| F-1 | "Global min" claim is misleading | **MAJOR** | Cross-cutting |
| O-2 | Optimizer may fail to separate formations | **MODERATE** | Overlap analysis |
| M-5 | Simplex constraint violations unchecked | **MODERATE** | M₂ landscape |
| MO-4 | Critical points may be on boundary | **MODERATE** | Morse analysis |
| F-2 | Energy normalization regime mismatch | **MODERATE** | Cross-cutting |
| F-3 | Simplex constraint not verified | **MODERATE** | Cross-cutting |
| F-4 | Closure floor energy correction | **MINOR** | Cross-cutting |

**4 CRITICAL, 7 MAJOR, 5 MODERATE, 1 MINOR.**
