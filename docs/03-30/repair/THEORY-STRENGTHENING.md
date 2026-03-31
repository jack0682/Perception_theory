# Theory Strengthening: Medium-Priority Repairs

**Author:** Theory Strengthener
**Date:** 2026-03-30
**Inputs:** R2 (static repair), R3 (temporal reconstruction), A4 (scaling audit), Canonical Spec v2.0, paper1_math.tex

---

## 1. beta_crit Scaling Analysis

### 1.1. The Problem

The phase transition criterion (T8-Core) states: if beta/alpha > 4*lambda_2/|W''(c)|, then the global minimizer of E_bd on Sigma_m is non-uniform. On a k x k grid graph, lambda_2 = 2(1 - cos(pi/k)) ~ pi^2/k^2 as k grows. This gives:

| Grid | n | lambda_2 | beta_crit (alpha=1) | beta/beta_crit at beta=10 |
|------|---|----------|---------------------|---------------------------|
| 5x5 | 25 | 0.382 | 2.29 | 4.4 |
| 10x10 | 100 | 0.098 | 0.59 | 17 |
| 20x20 | 400 | 0.025 | 0.15 | 67 |
| 50x50 | 2,500 | 0.004 | 0.024 | 417 |
| 100x100 | 10,000 | 0.001 | 0.006 | 1,667 |

At 100x100, *any* positive beta exceeds the threshold. The criterion is vacuous.

### 1.2. Analysis of Options

**Option A (scale-invariant criterion):** No normalization of alpha, beta can fix the fundamental issue. The problem is that lambda_2 -> 0 reflects a *physical fact* about large grids: long-wavelength modulations have vanishing energy cost under the smoothness penalty. Any intensive rescaling (e.g., alpha_hat = alpha * lambda_max(L)) still leaves the ratio lambda_2/lambda_max -> 0 for grids. The spectral gap ratio is an intrinsic property of the graph, not an artifact of parameter scaling.

**VERDICT: Fails. The vanishing spectral gap is geometric, not parametric.**

**Option B (scale alpha with n):** Setting alpha = alpha_0 * n makes beta_crit = 4*alpha_0*n*lambda_2/|W''(c)|. For grids, n*lambda_2 ~ pi^2, giving beta_crit = O(1). But this is a *parameter prescription*, not a theorem. It says: "if you choose alpha proportional to n, then the phase transition is meaningful." This is finite-element-style mesh rescaling (alpha plays the role of the diffusion coefficient, and scaling it with the mesh size keeps the PDE limit well-defined). Technically correct but ad hoc within the current theory, which treats alpha as a fixed physical parameter.

**VERDICT: Correct but ad hoc. Useful as a remark, not as a fix to T8-Core.**

**Option C (restrict claims to spectral-gap graphs):** State the theorem's domain of applicability honestly. On graphs where lambda_2 = Omega(1) — expander graphs, complete graphs, fixed-size graphs, bounded-diameter graphs — the phase transition is a genuine constraint. On graphs where lambda_2 -> 0 (grids, trees, lattices at increasing size), the criterion is trivially satisfied and the *diagnostic vector*, not the phase transition, becomes the meaningful assessment tool.

**VERDICT: Mathematically honest, preserves the theorem's genuine content, correctly identifies the regime boundary.**

**Option D (quality-aware phase transition):** Ask "does a minimizer exist with d > d_0?" instead of "does a non-trivial minimizer exist?" This is the right long-term question but requires quantitative predicate bounds at minimizers (the Bind bound from R2 Item 2), which is a separate proof effort. Not available now.

**VERDICT: Correct but downstream of the Bind bound proof. Long-term goal.**

### 1.3. Recommendation: Option C + Option B as Remark

The strongest honest framing combines:

1. **T8-Core stays as-is** — it is a correct theorem with no mathematical error
2. **Add a scaling caveat** that identifies the regime where the theorem is informative vs. vacuous
3. **Add a remark on finite-element rescaling** (Option B) for practitioners who want a meaningful threshold on large graphs
4. **Add a remark on diagnostic primacy** — on large graphs, the diagnostic vector d = (Bind, Sep, Inside, Persist) replaces the phase transition as the meaningful criterion

### 1.4. Why the Theorem Is Still Valuable

The theorem IS genuinely informative in several important settings:

- **Fixed-size graphs** (e.g., sensory scenes with bounded spatial extent): lambda_2 is bounded below, and beta_crit is a meaningful threshold
- **Expander-like graphs** (social networks, random graphs): lambda_2 = Omega(1), giving a non-trivial beta_crit
- **Small-to-moderate grids** (up to ~20x20): beta_crit is O(0.1), which is a real constraint on beta
- **The theorem establishes the mechanism**: even on large graphs where the criterion is trivially satisfied, the *proof* reveals *why* formations emerge (saddle-point instability of the uniform state), which is conceptually important

The scaling issue does NOT mean the theory "breaks" on large graphs. Formations still exist, still have good diagnostics, and the energy functional still provides a meaningful variational target. What breaks is the *phase transition as a selection criterion* — it can no longer distinguish "parameters that favor formation" from "parameters that don't."

### 1.5. Recommended Spec Text for T8-Core

The current T8-Core statement (Spec lines 787-789) should be amended. Add the following **immediately after** the existing T8-Core statement and proof:

```
**Scaling Caveat.** The phase transition threshold $\beta_{\mathrm{crit}} =
4\alpha\lambda_2/|W''(c)|$ depends on the spectral gap $\lambda_2$ of the graph
Laplacian. For graph families where $\lambda_2 \to 0$ as $n \to \infty$ (e.g.,
$k \times k$ grids with $\lambda_2 \sim \pi^2/k^2$), the threshold vanishes and
the criterion is trivially satisfied for any fixed $\beta > 0$. In this regime,
T8-Core guarantees non-trivial minimizer *existence* but does not provide a
meaningful *selection criterion* for parameters.

On graphs with $\lambda_2 = \Omega(1)$ (expander graphs, bounded-diameter graphs,
fixed-size applications), the phase transition is a genuine constraint that
separates formation-supporting from formation-suppressing parameter regimes.

On large grid-like graphs, the proto-cohesion diagnostic vector
$\mathbf{d} = (\mathsf{Bind}, \mathsf{Sep}, \mathsf{Inside}, \mathsf{Persist})$
replaces the phase transition as the primary assessment tool. Formation *quality*,
not formation *existence*, is the meaningful question at scale.
```

Add the following as a **Remark** after the scaling caveat:

```
**Remark (Finite-element rescaling).** In the continuum limit interpretation,
$\alpha$ plays the role of a diffusion coefficient and should scale with the mesh
resolution: $\alpha = \alpha_0 / h^2$ where $h$ is the mesh spacing. For a
$k \times k$ grid with $h = 1/k$, this gives $\alpha = \alpha_0 k^2$, and
$\beta_{\mathrm{crit}} = 4\alpha_0 k^2 \lambda_2 / |W''(c)| \approx
4\alpha_0 \pi^2 / |W''(c)| = O(1)$, recovering a mesh-independent threshold.
This rescaling is standard in numerical PDE but constitutes a parameter
prescription rather than a theorem. It is recommended for computational
implementations on large grids.
```

### 1.6. Recommended Paper Text

For paper1_math.tex, after Theorem 4.1 (phase transition), add a paragraph:

```latex
\begin{remark}[Scaling regime]
\label{rmk:scaling}
The threshold $\beta_{\mathrm{crit}} = 4\alpha\lambda_2/|W''(c)|$ depends on the
Fiedler eigenvalue $\lambda_2$, which vanishes as $O(1/k^2)$ for $k \times k$
grid graphs. On large grids, the criterion is trivially satisfied for any
$\beta > 0$: the uniform state is unstable to long-wavelength perturbations
regardless of the double-well strength. In this regime, formation \emph{existence}
is guaranteed but the phase transition provides no selection among parameters.

The diagnostic vector $\mathbf{d}$ (Section~\ref{sec:diagnostics}) then becomes
the primary quality measure: a non-trivial minimizer exists, but only minimizers
with $\mathbf{d}$ above application-specific thresholds constitute meaningful
formations. For computational implementations on fine meshes, the
finite-element rescaling $\alpha \propto 1/h^2$ recovers a mesh-independent
threshold (see Appendix).

The theorem remains informative on graphs with spectral gap $\lambda_2 = \Omega(1)$
(expander graphs, bounded-diameter networks, fixed-size application domains).
\end{remark}
```

---

## 2. Restructured Temporal Theorem Architecture

### 2.1. Design Principles

Following R3's recommended Option C (restrict to conditional results):

1. **Separate the sound from the broken.** T-Persist-1(a,c) are genuine IFT results that do not depend on the broken Brouwer argument. Present them as the primary temporal contribution.
2. **Upgrade what deserves upgrading.** The weak-regime contraction argument is currently a remark; it deserves Proposition status as the strongest honest existence result.
3. **Downgrade what must be downgraded.** The Brouwer FP existence becomes a Conjecture. T-Persist-1(b) and (d) become explicitly conditional sub-results.
4. **State gaps as open problems.** Don't hide them in proof sketches; give them their own subsection.

### 2.2. Restructured Architecture

```
Section 6: Transport and Persistence
  6.1  Cohesion Fingerprint [unchanged]
  6.2  Self-Referential Transport Cost [unchanged]
  6.3  Fixed-Point Existence
       - Proposition 6.1 (Weak-Regime Existence): contraction -> unique FP [UPGRADE from remark]
       - Conjecture 6.2 (General Existence): Brouwer [DOWNGRADE from theorem]
       - Remark (Kakutani, mean-field game precedent)
  6.4  Temporal Core Inheritance
       - Definition (epsilon-gentle) [unchanged]
       - Theorem 6.3 (a,c): IFT persistence + core inclusion [KEEP, primary result]
       - Proposition 6.4 (b): gradient flow convergence [CONDITIONAL on Gap 4]
       - Remark (d): threshold preservation [CONDITIONAL on Gap 6]
  6.5  Open Problems [NEW]
```

### 2.3. LaTeX-Ready Theorem Statements

#### Proposition 6.1: Weak-Regime Existence and Uniqueness

```latex
\begin{proposition}[Weak-Regime Transport Fixed Point]
\label{prop:weak-regime-fp}
Let $\Phi : \Sigma_m \to \Sigma_m$ be the self-referential transport map
(Section~\ref{sec:fp-formulation}). Define the \emph{feedback ratio}:
\begin{equation}
\label{eq:feedback-ratio}
\rho = \frac{\lambda_{\mathrm{tr}} \cdot \gamma \cdot \|\partial\phi/\partial u\|_{\mathrm{op}}}
            {\varepsilon_{\mathrm{OT}} \cdot \mu},
\end{equation}
where $\mu = \lambda_{\min}(H_{\mathrm{static}}|_{T\Sigma_m}) > 0$ is the spectral
gap of the constrained static Hessian at the minimizer, $\gamma$ is the fingerprint
weight in the transport cost~\eqref{eq:transport-cost},
$\|\partial\phi/\partial u\|_{\mathrm{op}}$ is the operator norm of the fingerprint
Jacobian, and $\varepsilon_{\mathrm{OT}}$ is the entropic regularization parameter.

If $\rho < 1$, then:
\begin{enumerate}
\item[(a)] $\Phi$ is a contraction with Lipschitz constant $\leq \rho$ on a
neighborhood of the static minimizer.
\item[(b)] $\Phi$ has a unique fixed point $u_s^* \in \Sigma_m$ in this
neighborhood, and the alternating minimization iteration $u_s^{(k+1)} = \Phi(u_s^{(k)})$
converges geometrically: $\|u_s^{(k)} - u_s^*\|_2 \leq \rho^k \|u_s^{(0)} - u_s^*\|_2$.
\end{enumerate}
\end{proposition}

\begin{proof}[Proof sketch]
The chain rule gives $\|D\Phi(u)\|_{\mathrm{op}} \leq
\|D_u(\text{re-optimize})\|_{\mathrm{op}} \cdot
\|D_M(\text{OT-solve})\|_{\mathrm{op}} \cdot
\|D_c(\text{cost})\|_{\mathrm{op}} \cdot
\|D_u(\text{fingerprint})\|_{\mathrm{op}}$.

The re-optimization Jacobian is bounded by $\lambda_{\mathrm{tr}}/\mu$ (IFT on
the perturbed energy). The entropic OT solution Jacobian with respect to cost is
bounded by $1/\varepsilon_{\mathrm{OT}}$~\cite{Peyre2019}. The cost Jacobian with
respect to fingerprints is $2\gamma$. The fingerprint Jacobian is
$\|\partial\phi/\partial u\|_{\mathrm{op}}$. The product is
$\leq 2\lambda_{\mathrm{tr}} \gamma \|\partial\phi/\partial u\|_{\mathrm{op}} /
(\varepsilon_{\mathrm{OT}} \cdot \mu)$. When $\rho < 1$, Banach's contraction
mapping theorem applies.
\end{proof}

\begin{remark}
The feedback ratio $\rho$ has a transparent interpretation: the numerator measures
the strength of the self-referential loop (transport weight $\times$ fingerprint
sensitivity $\times$ fingerprint responsiveness), while the denominator measures the
restoring forces (entropic smoothing $\times$ energy curvature). Formation tracking
is well-posed when feedback is weaker than restoration. The constants in $\rho$ are
estimable from the energy parameters but are not derived in closed form; they depend
on the specific graph and parameter regime. Tightening these constants is an open
problem.
\end{remark}
```

#### Conjecture 6.2: General Fixed-Point Existence

```latex
\begin{conjecture}[General Transport Fixed-Point Existence]
\label{conj:general-fp}
For any $\lambda_{\mathrm{tr}} > 0$ and $\varepsilon_{\mathrm{OT}} > 0$, the
self-referential transport map $\Phi : \Sigma_m \to \Sigma_m$ has at least one
fixed point.
\end{conjecture}

\begin{remark}
The natural approach via Brouwer's theorem requires continuity of $\Phi$. The
entropic OT solution $M^*$ is $C^\infty$ in the cost matrix, and the fingerprint
is continuous in $u_s$, so the only potential discontinuity is in the
re-optimization step: the energy minimizer as a function of the transport plan.
At non-degenerate minimizers, the implicit function theorem gives continuity.
However, at Maxwell points---parameter values where two local minimizers have
equal energy and the global minimizer jumps---the re-optimization step is
discontinuous. Such points exist generically in the phase-transition regime
($\beta > \beta_{\mathrm{crit}}$), which is precisely the regime of interest.

Alternative approaches include: (i)~Kakutani's fixed-point theorem for set-valued
maps (requires convex-valued correspondences, which the argmin set does not
generally satisfy for non-convex energies); (ii)~restricting to local minimizer
tracking via IFT (Proposition~\ref{prop:weak-regime-fp}), which avoids the
Maxwell-point issue but restricts to the weak regime.

The closest structural precedent in the literature is mean-field game
theory~\cite{LasryLions2007}, where the cost depends on the distribution of
agents. The SCC formulation differs in that the cost depends on \emph{specific
field values} through the operator triad, introducing a richer dependence
structure than the distribution-level coupling in mean-field games.
\end{remark}
```

#### Theorem 6.3: Temporal Core Inheritance (revised)

```latex
\begin{theorem}[Temporal Core Inheritance---Conditional]
\label{thm:temporal-persistence-revised}
Let $X = X_t = X_s$ with $n = |X|$. Let $\hat{u}_t \in \Sigma_m$ be a local
minimizer of $\mathcal{E}_t$ on $\Sigma_m$ with constrained Hessian spectral gap
$\mu > 0$. Suppose the transition from $t$ to $s$ is $\varepsilon$-gentle
(Definition~\ref{def:gentle}) with $\varepsilon_1 < \mu/2$. Then:
\begin{enumerate}
\item[(a)] \emph{(Minimizer persistence.)} $\mathcal{E}_s$ has a local minimizer
$\hat{u}_s \in \Sigma_m$ with $\|\hat{u}_s - \hat{u}_t\|_2 \leq 2\varepsilon_1/\mu$,
non-degenerate with spectral gap $\geq \mu/2$.
\item[(c)] \emph{(Core inclusion.)} $\Core_t(\hat{u}_t) \subseteq
\Core_s(\hat{u}_s,\, \theta_{\mathrm{core}} - 2\varepsilon_1/\mu)$. That is, every
site in the core at time $t$ remains in the core at time $s$ with a shifted threshold.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
Part (a) is a standard application of the implicit function theorem for constrained
optimization. Define the homotopy $\mathcal{E}_\lambda = (1-\lambda)\mathcal{E}_t +
\lambda\mathcal{E}_s$ on $\Sigma_m$. At $\lambda = 0$, the projected gradient
vanishes at $\hat{u}_t$ and the constrained Hessian $H_\Sigma$ is invertible with
$\|H_\Sigma^{-1}\| \leq 1/\mu$. By the IFT, the critical point persists along the
homotopy with displacement $\leq 2\varepsilon_1/\mu$. Weyl's inequality gives the
spectral gap bound.

Part (c) follows from the $\ell^\infty \leq \ell^2$ bound: for any $x \in \Core_t$,
$\hat{u}_s(x) \geq \hat{u}_t(x) - \|\hat{u}_s - \hat{u}_t\|_\infty \geq
\theta_{\mathrm{core}} - 2\varepsilon_1/\mu$.

\emph{Hypotheses status:} Non-degeneracy ($\mu > 0$) is generically satisfied (the
set of degenerate critical points has measure zero in parameter space by Sard's
theorem). The $\varepsilon$-gentle condition is a smallness hypothesis on the
temporal transition; it is satisfied when the environment changes slowly relative
to the energy landscape curvature.
\end{proof}
```

#### Proposition 6.4: Gradient Flow Convergence (conditional)

```latex
\begin{proposition}[Gradient Flow to Persisted Minimizer---Conditional]
\label{prop:basin-convergence}
Under the hypotheses of Theorem~\ref{thm:temporal-persistence-revised}, let
$\tilde{u} = \mathbf{M}_{t \to s}\hat{u}_t$ be the transported field and
$\pi_\Sigma(\tilde{u})$ its projection onto $\Sigma_m$.

\textbf{If} additionally the basin of attraction of $\hat{u}_s$ under the projected
gradient flow of $\mathcal{E}_s$ has radius $r_{\mathrm{basin}} >
2\varepsilon_2 + 2\varepsilon_1/\mu$ \textbf{(Gap~4, open)}, then the gradient flow
from $\pi_\Sigma(\tilde{u})$ converges exponentially to $\hat{u}_s$.
\end{proposition}

\begin{remark}
The sub-stochasticity axiom (E1) implies $\mathbf{1}^T\tilde{u} \leq m$, so the
projection cost satisfies $\|\pi_\Sigma(\tilde{u}) - \tilde{u}\|_2 \leq
\varepsilon_2$. The projected field lies at distance $\leq 2\varepsilon_2 +
2\varepsilon_1/\mu$ from $\hat{u}_s$. The gap is the basin radius bound: proving
$r_{\mathrm{basin}} \geq f(\mu, \Delta E)$ for a quantitative function $f$
requires Morse-theoretic analysis of the energy landscape's saddle-point structure.
\end{remark}
```

#### Remark on Threshold Preservation

```latex
\begin{remark}[Exact threshold preservation]
\label{rmk:threshold}
If, in addition to the hypotheses of Theorem~\ref{thm:temporal-persistence-revised},
the formation-structured minimizer $\hat{u}_t$ satisfies an \emph{interior gap}
condition---$\min_{x \in \Core_t}(\hat{u}_t(x) - \theta_{\mathrm{core}}) \geq \eta$
for some $\eta > 2\varepsilon_1/\mu$---then core inclusion holds with the original
threshold:
\[
\Core_t(\hat{u}_t) \subseteq \Core_s(\hat{u}_s, \theta_{\mathrm{core}}).
\]
A quantitative interior gap bound $\eta \geq \eta_0 > 0$ at formation-structured
minimizers, deriving from the double-well structure of $\mathcal{E}_{\mathrm{bd}}$,
is an open problem (Gap~6).
\end{remark}
```

#### Open Problems Subsection

```latex
\subsection{Open Problems in Temporal Theory}

The following problems remain open in the temporal theory. They are ordered by
estimated difficulty and impact.

\begin{enumerate}
\item \textbf{General transport fixed-point existence (Conjecture~\ref{conj:general-fp}).}
Prove (or disprove) that $\Phi$ has a fixed point for all $\lambda_{\mathrm{tr}},
\varepsilon_{\mathrm{OT}} > 0$. The key obstacle is continuity of the re-optimization
step at Maxwell points. Approaches: Kakutani-type theorems for non-convex-valued
correspondences; degree theory; or constructive iteration schemes beyond alternating
minimization.

\item \textbf{Basin radius (Gap~4).} Prove a quantitative lower bound
$r_{\mathrm{basin}} \geq f(\mu, \Delta E, n)$ for the basin of attraction of
non-degenerate energy minimizers on $\Sigma_m$. The natural approach uses Morse
persistence of saddle points under perturbation and the quantitative Morse lemma.
This would upgrade Proposition~\ref{prop:basin-convergence} to an unconditional
result.

\item \textbf{Transport concentration (Gap~5).} Prove that the self-referential
transport kernel maps core to core:
$\sum_{y \in \Core_s} M^*(x,y) \geq 1 - \delta_{\mathrm{core}}$ for
$x \in \Core_t$. This is the key missing step for a quantitative Persist predicate
bound (T-Persist-2). It requires concentration inequalities for entropic optimal
transport under the fingerprint cost.

\item \textbf{Interior gap (Gap~6).} Prove that at formation-structured minimizers
of $\mathcal{E}_{\mathrm{bd}}$, the field values in the core satisfy
$\hat{u}(x) \geq \theta_{\mathrm{core}} + \eta_0$ for a quantitative $\eta_0 > 0$
depending on the double-well parameters. The $\Gamma$-convergence result (T11)
implies this in the sharp-interface limit ($\varepsilon \to 0$); finite-parameter
bounds are needed.
\end{enumerate}
```

### 2.4. Strongest Honest Temporal Claim

The strongest honest claim about temporal persistence is:

> **Under epsilon-gentle transitions with fixed support space and non-degenerate minimizers, formations persist in the following precise sense: the energy landscape at time s has a local minimizer quantitatively close to the minimizer at time t (distance bounded by 2*epsilon_1/mu), and the cohesive core is preserved with a shifted threshold (shifted by at most 2*epsilon_1/mu). In the weak-transport regime (feedback ratio rho < 1), the self-referential transport fixed point exists uniquely and alternating minimization converges geometrically. General fixed-point existence beyond the weak regime is an open problem.**

This is a genuine contribution: the first quantitative persistence result for SCC, with explicit dependence on the spectral gap mu and the gentleness parameters. The epsilon-gentle framework is well-designed and publishable in its own right.

---

## 3. Updated Proto-Cohesion Status

### 3.1. Status After Emergency Fixes

The emergency fixes addressed three critical issues:
- **T7 restated** as Hessian curvature result (not barrier height)
- **QM1 fixed** with normalized Q_morph = (l_max - c)/(1 - c) * Artic
- **Transport existence** made conditional (Brouwer -> Conjecture)

### 3.2. Current Status by Component

#### What Is Proved (Category A)

| Result | Statement | Proof Method |
|--------|-----------|-------------|
| T1 | Energy minimizer exists on Sigma_m | Extreme value theorem on compact set |
| T8-Core | Global minimizer of E_bd is non-uniform when beta/alpha > 4*lambda_2/\|W''(c)\| | Hessian negative eigenvalue at uniform state |
| T14 | Gradient flow converges to critical point (exponentially for analytic energy) | Lojasiewicz inequality |
| Sep = 1 - E_sep/m | Exact algebraic identity for u-weighted Sep | Direct computation |
| Bind >= 1 - sqrt(E_cl/n) | Cauchy-Schwarz bound | Direct computation |
| Sep_new covariance | Sep_new = E[D] + Cov(C/S, D) / E[C/S] | Exact algebraic identity |
| T7 (restated) | Closure adds strictly positive Hessian curvature at formation-structured minimizers | Gram matrix analysis |
| QM1-4 (fixed) | Normalized Q_morph satisfies vanishing, monotonicity, continuity, discrimination | Direct construction |

#### What Is Proved Conditionally (Category B)

| Result | Statement | Condition |
|--------|-----------|-----------|
| T8-Full | Full energy has non-uniform local minimizer | Non-degeneracy of E_bd minimizer + lambda_cl, lambda_sep small |
| Bind quantitative | Bind(u*) >= 1 - C * lambda_bd/lambda_cl | KKT gradient balance at minimizer; proof route clear (R2 Item 2) |
| T-Persist-1(a) | Minimizer persists under epsilon-gentle transition | Non-degeneracy (mu > 0), epsilon_1 < mu/2 |
| T-Persist-1(c) | Core inclusion with shifted threshold | Same as (a) |
| Weak-regime FP | Self-referential transport has unique FP | Feedback ratio rho < 1 |

#### What Is Demonstrated Computationally

| Result | Evidence | Analytical Support |
|--------|----------|-------------------|
| Sep >= 0.87 at minimizers | All tested parameter regimes (15x15 grid) | Forward bridge (low E_sep -> high Sep) proved directionally |
| Inside >= 0.88 at minimizers | All tested parameter regimes | Gamma-convergence gives qualitative support in sharp-interface limit |
| Bind >= 0.85 at minimizers | All tested parameter regimes | Cauchy-Schwarz + KKT argument (proof route clear) |
| Formation quality stable across grid sizes | 5x5 to 20x20 grids | No analytical scaling theory |

#### What Is Conditional/Open

| Result | Status | Gap |
|--------|--------|-----|
| Persist | Zero proved results | Requires transport kernel, core-to-core concentration (Gap 5) |
| General transport FP | Conjecture | Brouwer continuity fails at Maxwell points |
| Basin radius | Open | Gap 4: Morse persistence of saddle points |
| Interior gap | Open | Gap 6: quantitative lower bound from double-well |
| Sep >= D_bar | Unproved | Requires Cov(C,D) >= 0 at minimizers |

### 3.3. Strongest Honest Proto-Cohesion Theorem

```latex
\begin{theorem}[Proto-Cohesion at Energy Minimizers---Current Status]
\label{thm:proto-cohesion-status}
Let $X_t$ be a finite connected graph with Fiedler eigenvalue $\lambda_2 > 0$, and
let $\hat{u} \in \Sigma_m$ be a local minimizer of $\mathcal{E} = \lambda_{\mathrm{cl}}
\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} +
\lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$. Then:

\begin{enumerate}
\item \emph{(Existence.)} If $\beta/\alpha > 4\lambda_2/|W''(c)|$ with $c = m/n$ in
the spinodal range, a non-trivial minimizer exists (T8-Core). Under non-degeneracy
of the $\mathcal{E}_{\mathrm{bd}}$ minimizer, this extends to the full energy for
$\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}$ sufficiently small (T8-Full,
conditional).

\item \emph{(Convergence.)} The projected gradient flow on $\Sigma_m$ converges to a
critical point; for analytic energy ($b_D = 0$), convergence is exponential (T14).

\item \emph{(Binding.)} $\mathsf{Bind}(\hat{u}) \geq 1 - \sqrt{\mathcal{E}_{\mathrm{cl}}
(\hat{u})/n}$. At the minimizer, KKT gradient balance gives
$\mathcal{E}_{\mathrm{cl}}(\hat{u}) = O(\lambda_{\mathrm{bd}}^2/\lambda_{\mathrm{cl}}^2)$,
yielding $\mathsf{Bind} \geq 1 - O(\lambda_{\mathrm{bd}}/(\lambda_{\mathrm{cl}} \sqrt{n}))$
(proof route established; see Section~\ref{sec:bind-bound}).

\item \emph{(Separation.)} $\mathsf{Sep}(\hat{u}) = 1 - \mathcal{E}_{\mathrm{sep}}
(\hat{u})/m$ (exact). Quantitative lower bounds on Sep at minimizers are supported
by computation ($\mathsf{Sep} > 0.87$ across all tested regimes) and by asymptotic
analysis ($\Gamma$-convergence implies Sep $\to 1$ in the sharp-interface limit),
but lack finite-parameter analytical proof.

\item \emph{(Morphological quality.)} $\mathsf{Inside}(\hat{u})$ is demonstrated
computationally ($\mathsf{Inside} > 0.88$ across all tested regimes) and supported
by $\Gamma$-convergence asymptotics, but lacks finite-parameter analytical bounds.

\item \emph{(Persistence.)} No analytical results. The persistence predicate requires
a transport kernel $\mathbf{M}_{t \to s}$ and core-to-core concentration (Gap~5).
Under $\varepsilon$-gentle transitions, core inclusion with shifted threshold is
proved (Theorem~\ref{thm:temporal-persistence-revised}).
\end{enumerate}
\end{theorem}
```

### 3.4. Summary Assessment

**The honest status of proto-cohesion is:**

The SCC theory proves that non-trivial energy minimizers exist (T8-Core), that gradient flow converges to them (T14), and that these minimizers satisfy the Bind predicate quantitatively (Cauchy-Schwarz bound, with a tighter KKT-based bound on a clear proof route). Sep and Inside satisfaction at minimizers is demonstrated computationally across all tested parameter regimes and supported by asymptotic (Gamma-convergence) analysis, but finite-parameter analytical bounds are not yet proved. Persist has zero analytical results and depends on the unresolved transport theory.

**In one sentence:** The static theory has a proved variational backbone (existence + convergence + Bind bound) with strong computational evidence for Sep and Inside, while Persist remains the theory's largest gap.

---

## 4. Summary of Recommendations

### For the Canonical Spec

1. **T8-Core:** Add scaling caveat and finite-element rescaling remark (Section 1.5 above). No change to the theorem statement itself.
2. **Temporal section:** Restructure per Section 2.2 architecture. This requires a new spec section on temporal results (currently the spec has no temporal theorem registry).

### For paper1_math.tex

1. **After Theorem 4.1:** Add Remark on scaling regime (Section 1.6 above).
2. **Section 6:** Replace current Theorem 6.1 (Brouwer) with Proposition 6.1 (weak-regime) + Conjecture 6.2 (general). Replace Remark on OT precedent with honest MFG contextualization. Revise Theorem on temporal persistence to Theorem 6.3 (a,c only) + Proposition 6.4 (b, conditional) + Remark (d). Add Open Problems subsection (Section 6.5).
3. **Proto-cohesion discussion:** Update to reflect the status assessment in Section 3.3.

### Priority for New Mathematics

1. **Bind quantitative bound** (KKT gradient balance) — highest-value new proof, converts the central claim's weakest link into a theorem
2. **T8-Full IFT argument** — routine but important; completes the phase transition story
3. **Weak-regime contraction constants** — tighten the estimates in Proposition 6.1
