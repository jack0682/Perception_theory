# Task #3: Isoperimetric & Transport Necessity Analysis

**Date:** 2026-04-02
**Session:** Phase A — necessity and tightness of multi-formation conditions
**Category:** analysis
**Status:** complete
**Depends on:** ISOPERIMETRIC-TRANSPORT-PROOFS.md, TRANSPORT-SELECTION-ANALYSIS.md, exp40

---

## 1. Isoperimetric Energy Ordering

### 1.1. Current Status

**Theorem (ISOPERIMETRIC-TRANSPORT-PROOFS.md §2).** On a connected graph G with n >= 4m, lambda_bd > 0, beta/alpha > beta_crit (sharp-interface regime), and non-increasing isoperimetric profile h(k):

    E(u*_{2m}) < 2 * E(u*_m)

**Proved on:**
- d-dimensional grid graphs Z^d_n (all d >= 1), where h(k) ~ k^{-1/d} is strictly decreasing.
- Expander graphs and regular graphs with non-increasing h(k).
- All 24 topologies tested in exp35, including barbells, stars, and weighted bridges.

**Conditions required:**
1. n >= 4m (room for two disjoint copies of the volume-m minimizer)
2. lambda_bd > 0 (positive interfacial energy)
3. beta/alpha > beta_crit (sharp-interface regime for Gamma-convergence)
4. Non-increasing isoperimetric profile h(k), or the weaker condition h(2m) < 2*h(m) - epsilon

**Quantitative saving on grids:** The isoperimetric saving is delta_iso = 1 - 2^{-1/d}, which gives:
- d=1: delta_iso = 0.50 (50% boundary saving)
- d=2: delta_iso = 0.29 (29% boundary saving)
- d=3: delta_iso = 0.21 (21% boundary saving)

exp30 confirms: E_K1 ~ 7.98 vs E_K2_self ~ 15.58 on 15x15 grid, a ratio of ~1.95 (exceeding the sqrt(2) ~ 1.41 isoperimetric prediction because E_cl and E_sep also favor single formations).

### 1.2. Necessity Analysis

**Question:** Is isoperimetric ordering NECESSARY for T-Persist-K-Strong, or merely sufficient for establishing kinetic stability?

**Answer: It is sufficient but NOT necessary for persistence. It IS necessary for the metastability interpretation.**

The logical chain in the multi-formation theory is:

    Isoperimetric ordering  =>  K>=2 is never the global minimum
                            =>  K>=2 persistence is a KINETIC phenomenon (barrier)
                            =>  Barrier height determines persistence timescale

For T-Persist-K-Strong persistence itself, what is actually needed is:

1. **Local stability of the K-formation state** (positive definite Hessian) — proved by exp30: curvatures +1000 to +1500 in merge direction, independent of overlap.
2. **Basin containment under temporal perturbation** (directional criterion BC' from Task #1).
3. **Transport confinement** (TC condition from Task #1).

None of these three conditions require isoperimetric ordering. A K=2 state could persist even if it were the global minimum (which would make it thermodynamically stable, not just kinetically).

**What would fail if ordering didn't hold?**

If E(u*_{2m}) >= 2*E(u*_m) on some graph:
- The K=2 state would be the **global minimum**, not merely metastable.
- Persistence would actually be **easier** to prove (thermodynamic stability is stronger than kinetic).
- The Corollary (§2.4 of ISOPERIMETRIC-TRANSPORT-PROOFS.md) that "multi-formation persistence is kinetic" would fail — it would be thermodynamic instead.
- The theory's narrative changes (multi-formation as ground state vs metastable state), but persistence guarantees are **unaffected or strengthened**.

**Verdict:** Isoperimetric ordering is **not necessary** for T-Persist-K-Unified persistence. It is necessary only for the **metastability characterization** — i.e., for classifying multi-formation persistence as a barrier phenomenon rather than ground-state stability. The unified theorem can proceed without it as a hypothesis, but should note the metastability interpretation requires it.

### 1.3. Failing Topologies

**Question:** Do any graph topologies violate E(u*_{2m}) < 2*E(u*_m)?

**Analysis of candidates where h(2m) > h(m) might occur:**

#### Barbell graphs

A barbell graph has two dense clusters (|C_1| = |C_2| = n_c) connected by a narrow bridge of width w. The isoperimetric profile is:

    h(k) = |dS| / k  where  |dS| = min_{|S|=k} |boundary edges of S|

For k <= n_c: the optimal set is a subgraph of one cluster, so h(k) ~ h_cluster(k) (the cluster's internal isoperimetric profile, typically decreasing).

For k ~ n_c: the optimal set is an entire cluster. h(n_c) = w/n_c (the bridge contributes w boundary edges).

For k = n_c + delta (slightly more than one cluster): the optimal set must spill across the bridge. h(n_c + delta) >= w/(n_c + delta) but the spilled nodes contribute additional boundary edges within the second cluster.

**Critical regime for ordering failure:** Set m ~ n_c/2 so two formations fit in separate clusters. Then u*_m occupies half a cluster, and:
- Two copies at volume m: one per cluster, total boundary ~ 2*h_cluster(m)*m (internal to each cluster)
- One merged at volume 2m = n_c: could sit entirely in one cluster (boundary ~ h_cluster(n_c)*n_c) OR span the bridge (boundary ~ bridge cost)

If n_c is large and the cluster has good isoperimetric profile, the single formation at 2m within one cluster wins: h_cluster(2m) < h_cluster(m), preserving ordering.

**But if m = n_c** (one formation per cluster): Two formations have boundary 2*w (bridge edges only, since each fills its cluster). A merged formation at volume 2*n_c = n must fill the entire graph, which could have zero boundary (if the graph is the complete vertex set). This gives E(u*_{2m}) ~ 0 < 2*w = 2*E(u*_m), so **ordering still holds**.

**exp35 confirms:** All 24 tested topologies (including barbells at bridge widths 1-8) satisfy the ordering.

#### Star graphs

Star graph S_n: center vertex connected to n-1 leaves, no leaf-leaf edges.

For m = 1: u*_1 concentrates on a single vertex. Boundary = degree of that vertex.
- Center: boundary = n-1
- Leaf: boundary = 1
So u*_1 is a leaf, E_bd(u*_1) proportional to 1.

For m = 2: u*_2 must place mass on two vertices. If on center + leaf: boundary involves the high-degree center.
If on two leaves: no edge between them, so u^T L u = 0 for the Laplacian quadratic, but the double-well term W(u_i) is nonzero at both.

The isoperimetric profile of the star is non-monotone:
- h(1) = 1 (one leaf, boundary = 1)
- h(2) = ? Depends on whether the optimizer picks center+leaf or 2 leaves.
- h(n-1) = (n-1)/(n-1) = 1 (all leaves, boundary = n-1 edges to center)

The lack of leaf-leaf edges makes h(k) behave irregularly for intermediate k. However, for the SCC energy (which includes E_cl and E_sep, not just boundary), the full optimization over Sigma_m may yield different behavior than pure boundary minimization.

**Assessment:** Star graphs could in principle violate monotonicity of h(k), but the SCC energy includes volume-scaling terms (E_cl, E_sep) that provide an additional single-formation advantage beyond isoperimetry. No violation of the energy ordering has been observed experimentally.

#### Highly irregular graphs

The theoretical failure mode requires:
- h(2m) >= h(m), i.e., the optimal set at volume 2m has proportionally MORE boundary per unit volume than at volume m.
- This can happen on graphs where the "efficient" region for volume m is a tight cluster, but doubling the volume forces expansion into a poorly-connected region.

**Concrete construction:** Take two copies of K_{n/2} (complete graphs) connected by a single edge. Set m = n/4. Then u*_m lives compactly in one half-clique (boundary ~ 1 edge to the other half). But u*_{2m} = u*_{n/2} fills one half-clique entirely (boundary = 1 bridge edge). Two copies at volume m could fit in the two half-cliques, with total boundary ~ 2. The merged formation at 2m has boundary ~ 1. So **ordering still holds** (1 < 2).

**Key insight:** For ordering to fail, we need the merged formation to be LESS efficient at using space than two separate ones. This requires the graph to have "anti-isoperimetric" regions — areas where adding volume proportionally increases boundary. Such graphs exist in theory (e.g., long chains of bottlenecks at increasing widths) but are pathological and do not arise in typical applications.

### 1.4. Consequences for Unified Theorem

**If ordering fails on some topology, what changes?**

1. T-Persist-K-Unified does NOT require isoperimetric ordering as a hypothesis. It requires:
   - (SR-lambda): Lambda_coupling < 1/(K-1) (spectral-coupling bound)
   - (TC-K): Transport confinement per formation
   - (BC'): Directional basin containment
   None of these reference the isoperimetric ordering.

2. The **metastability narrative** would need a topology condition:
   - "On graphs with non-increasing h(k), multi-formation persistence is kinetic (barrier phenomenon)."
   - "On graphs where E(u*_{2m}) >= 2*E(u*_m), multi-formation persistence may be thermodynamic (ground state)."

3. The **merge dichotomy** (MERGE-DICHOTOMY-ANALYSIS.md) is unaffected: exp30 shows K=2 is always a local minimum regardless of isoperimetric ordering. The ordering only determines whether K=2 or K=1 is the global minimum.

**Recommendation for T-Persist-K-Unified:** Do NOT include isoperimetric ordering as a hypothesis. State it as a separate theorem that characterizes the thermodynamic landscape, with the consequence that K>=2 persistence is kinetic on graphs satisfying the ordering. The persistence theorem itself works regardless.

---

## 2. Transport Confinement

### 2.1. Current Bound

**Theorem (ISOPERIMETRIC-TRANSPORT-PROOFS.md §3).** For u_t in Sigma_m with eps_OT > 0, sigma > 0, connected G:

    ||transport(u_s) - u_t||_2 <= C_conf * sqrt(m)

where C_conf = O(sigma * sqrt(eps_OT * log n)), independent of u_s.

The u_s-independence follows from K(x,y) <= K_sp(x,y) = exp(-d_G(x,y)^2 / (2*sigma^2*eps_OT)), where the spatial kernel K_sp is u_s-independent and the fingerprint cost term gamma*||phi_t(x) - phi_s(y)||^2 >= 0 only makes the cost larger.

The bound was derived via entropic smoothing width analysis: mass from source site x concentrates within radius O(sigma*sqrt(eps_OT*log n)) of x, with exponential tail beyond this radius.

### 2.2. Empirical Slack

**exp40 Part 3 results (actual displacement vs bound):**

| Config | n | Actual ||u_tilde - u*|| | Bound C_conf*sqrt(m) | Ratio | Slack factor |
|--------|---|------------------------|---------------------|-------|-------------|
| 10x10_b30 | 100 | 3.18e-4 | 11.75 | 2.7e-5 | ~37,000x |
| 10x10_b50 | 100 | 1.13e-5 | 11.75 | 9.6e-7 | ~1,040,000x |
| 15x15_b30 | 225 | 0.588 | 19.12 | 0.031 | ~33x |
| 15x15_b50 | 225 | 2.27e-5 | 19.12 | 1.2e-6 | ~842,000x |
| 15x15_b100 | 225 | 0.754 | 19.12 | 0.040 | ~25x |
| 20x20_b50 | 400 | 1.155 | 26.81 | 0.043 | ~23x |

**The slack ranges from 25x to over 1,000,000x.** The extreme cases (ratio ~ 1e-6) occur when the transport fixed-point iteration converges in 1 step with essentially zero displacement (the formation is already at its fixed point). The more informative cases are when actual displacement is non-trivial:

- 15x15_b30: 33x slack
- 15x15_b100: 25x slack
- 20x20_b50: 23x slack

### 2.3. Tightening Analysis

**Why is the slack so large?** The slack has three distinct sources:

#### Source 1: The sigma*sqrt(eps_OT*log n) entropic blur radius (dominant, ~5-10x)

The bound uses the entropic smoothing width as a uniform upper bound on transport displacement. This width is the maximum distance mass *could* travel under the entropic OT plan. But actual transport displacement depends on the *difference* between source and target marginals, not just the kernel width.

When u_s ~ u_t (which is the case at the fixed point), the transport plan is nearly the identity: M*(x,y) ~ u_t(x)*delta_{xy}. The displacement is then O(||u_s - u_t||), not O(sigma*sqrt(eps_OT*log n)). The bound is tight only when u_s is maximally different from u_t.

**Tightening:** Replace the uniform bound with a perturbative bound:

    ||transport(u_s) - u_t|| <= L_T * ||u_s - u_t|| + O(exp(-R^2/(2*sigma^2*eps_OT)))

where L_T is the Lipschitz constant of the transport map. For u_s in a ball around u_t, this gives a much tighter bound. The L_T factor is related to the Jacobian D(transport) at u_t, which can be estimated from the Sinkhorn sensitivity.

#### Source 2: The sqrt(m) volume factor (~3-5x)

The bound aggregates displacement over all m units of mass: ||u_tilde - u_t||_2 <= (per-site bound) * sqrt(m). But at the fixed point, most mass stays put. Only O(|boundary|) mass units undergo non-trivial displacement. Since |boundary| ~ m^{(d-1)/d} on grids:

    ||u_tilde - u_t||_2 ~ (per-site displacement) * sqrt(|boundary|) ~ (per-site) * m^{(d-1)/(2d)}

The sqrt(m) factor overestimates by m^{1/(2d)} ~ n^{1/(4d)}, which is ~3x for n=225 on a 2D grid.

#### Source 3: Ignoring the fingerprint cost (minor, ~2x)

The bound drops the fingerprint term gamma*||phi_t(x) - phi_s(y)||^2 >= 0, using only the geodesic cost. For sites where phi_t(x) is very different from phi_s(y) — i.e., core sites of the source mapping to exterior sites — the fingerprint cost provides additional exponential suppression. Including it would tighten the bound by a factor related to the fingerprint gap Delta_phi^2.

#### Summary of slack decomposition

| Source | Estimated contribution | Tightenable? |
|--------|----------------------|-------------|
| Uniform blur vs perturbative | ~5-10x | Yes: use Lipschitz bound near fixed point |
| sqrt(m) vs sqrt(|boundary|) | ~3-5x | Yes: use boundary-localized mass |
| Dropping fingerprint cost | ~2x | Yes: include gamma*Delta_phi^2 in kernel |
| **Total** | **~30-100x** | Consistent with observed 25-33x in non-trivial cases |

The extreme slack (>10^5) in near-zero-displacement cases is not a bound looseness issue but a measurement artifact: when the fixed point IS u_t to machine precision, any positive bound has infinite slack.

#### Fundamental lower bound on transport displacement

For transport from u_t to u_s != u_t, the displacement is bounded below by:

    ||transport(u_s) - u_t|| >= inf_{M in Pi(u_t, u_s)} ||M*1 - u_t|| = 0

since the identity-like plan M(x,y) ~ u_t(x)*delta_{xy} achieves zero column-marginal displacement when u_s = u_t. The lower bound is zero at the fixed point, confirming that the actual displacement can be arbitrarily small.

For u_s far from u_t, the lower bound is determined by how much mass must be rearranged:

    ||transport(u_s) - u_t|| >= c * TV(u_s, u_t) / sqrt(n)

where TV is the total variation distance. This provides a non-trivial lower bound only when u_s is substantially different from u_t.

### 2.4. Transport Confinement vs (WR') Banach Contraction

Task #1 (CONDITIONAL-CONDITIONS-ANALYSIS.md) proposes replacing (WR') with (TC).

**Formal comparison:**

**(WR') Banach contraction:**

    rho = lambda_tr * ||d_phi/du||_op * (log n + C) / (Delta_phi^2 * mu) < 1

This guarantees uniqueness AND exponential convergence of the fixed-point iteration. It is a condition on the *derivative* of T at the fixed point (spectral radius < 1).

**(TC) Transport confinement:**

    ||transport(u_s) - u_t|| < r_basin  for all u_s in Sigma_m

This guarantees uniqueness by a different mechanism (T is the constant map u_s -> u*). It is a condition on the *global image* of the transport map.

**Is (TC) strictly weaker than (WR')?**

Yes, and the evidence is clear:

1. **exp40 Part 1:** WR' holds in 3/6 configs (10x10_b50, 15x15_b100, 20x20_b50). Yet persistence is perfect (>=0.999) in ALL 6/6 configs. This means persistence holds even when WR' fails.

2. **Logical relationship:** (WR') implies (TC) under mild conditions (if the Banach contraction maps Sigma_m into B_{r_basin}(u*), then transport confinement holds a fortiori). But (TC) does NOT imply (WR'): transport confinement can hold even when the spectral radius of DT is >= 1, as long as the re-optimization step kills perturbations.

3. **The deep reason (TRANSPORT-SELECTION-ANALYSIS.md, Argument 3):** The composite map T = R o transport has ||DT|| ~ ||DR|| * ||D(transport)||. At a non-degenerate minimizer, ||DR|| ~ exp(-mu*tau) -> 0 for large optimization time tau. This makes T strongly contracting even when ||D(transport)|| > 1/mu (which is when WR' fails). (TC) implicitly exploits this re-optimization contraction; (WR') does not.

4. **Quantitative gap from exp40:**

| Config | WR' value | WR' holds? | Persist | Note |
|--------|-----------|-----------|---------|------|
| 10x10_b30 | 1.22 | NO | 1.000 | WR' fails by 22%, persistence perfect |
| 15x15_b30 | 2.94 | NO | 1.000 | WR' fails by 194%, persistence perfect |
| 15x15_b50 | 1.36 | NO | 1.000 | WR' fails by 36%, persistence perfect |

**Can (TC) be proved analytically (not just numerically)?**

Partially. The ISOPERIMETRIC-TRANSPORT-PROOFS.md §3 proves:

    ||transport(u_s) - u_t|| <= C_conf * sqrt(m)

with C_conf = O(sigma * sqrt(eps_OT * log n)), independent of u_s. This is the analytical part. What remains to close the gap is showing C_conf * sqrt(m) < r_basin, which couples transport parameters to the energy landscape:

    sigma * sqrt(eps_OT * log n) * sqrt(m) < sqrt(2 * Delta_bdy / lambda_max(H))

Rearranging:

    eps_OT < 2 * Delta_bdy / (sigma^2 * m * log(n) * lambda_max(H))

This is **always satisfiable** for small enough eps_OT. The question is whether it holds at *natural* parameter values (eps_OT ~ 1).

From exp40: the bound C_conf*sqrt(m) ranges from 11.75 to 26.81, while r_basin ranges from 0.15 to 0.44. So C_conf*sqrt(m) >> r_basin at natural parameters. **The analytical bound does NOT establish (TC) at natural parameters.**

However, the actual displacement (0 to 1.15) IS within r_basin for smaller grids and within several times r_basin for larger grids. The failure is in the bound's tightness, not in the underlying phenomenon.

**Path to analytical (TC):** The tightened perturbative bound (Section 2.3, Source 1) would give:

    ||transport(u_s) - u_t|| <= L_T * ||u_s - u_t|| + tail

For the fixed point u_s = u*, this gives displacement ~ 0 + tail, which IS within r_basin. For arbitrary u_s, the key is bounding L_T, which requires the Jacobian of the Sinkhorn solution with respect to the target marginal. This is a well-studied problem in computational OT (Cuturi & Doucet, 2014) and should yield L_T = O(1) for eps_OT = O(1).

**Verdict:** (TC) is strictly weaker than (WR'). The existing analytical bound is too loose by ~25-100x to establish (TC) at natural parameters. A tighter perturbative analysis is needed and appears feasible.

---

## 3. Implications for T-Persist-K-Unified

### 3.1. Which conditions are necessary?

| Condition | Necessary for persistence? | Sufficient? | Evidence |
|-----------|--------------------------|-------------|----------|
| **Isoperimetric ordering** | NO | N/A (not a persistence condition) | Persistence holds regardless; ordering characterizes thermodynamic landscape only |
| **Local stability** (mu > 0) | YES | No (needs basin containment) | At mu = 0, bifurcation destroys formation topology (structurally necessary) |
| **(BC') Basin containment** | YES | With (TC), yes | If perturbation escapes basin, gradient flow lands at wrong minimizer (structurally necessary) |
| **(TC) Transport confinement** | For uniqueness, YES* | With (BC'), yes | *In principle, persistence can hold with non-unique fixed points if all fixed points are close. But (TC) or a uniqueness condition is needed for the strong claim "persist to the SAME formation" |
| **(SR-lambda) Spectral coupling** | YES (for IFT approach) | No alone | At Lambda_coupling = 1/(K-1), joint spectral gap vanishes, IFT fails. Structurally necessary for the IFT proof route |

**Strictly necessary conditions (cannot be removed):**
1. mu > 0 (non-degeneracy) — generic by Sard's theorem
2. Perturbation within basin — expressed via (BC') or an equivalent
3. Lambda_coupling < 1/(K-1) — for K >= 2, inter-formation coupling must not destroy joint spectral gap

**Sufficient but replaceable:**
4. (WR') -> replaced by (TC)
5. (H2') -> proved (no longer a condition)
6. (H3) -> absorbed into (PS)
7. (NB) quantitative threshold -> weakened via directional analysis
8. (GT) -> absorbed into (BC')

### 3.2. What conditions does the unified theorem need?

**Minimal condition set for T-Persist-K-Unified:**

**(PS) Phase separation.** beta/alpha > beta_crit. This is the entry condition for the entire theory (sharp-interface regime, Gamma-convergence, meaningful core/boundary structure). Subsumes (H3) and implies (H2') for m >= 25.

**(ND) Non-degeneracy.** mu_F > 0 for each formation. Generic (Sard). Ensures IFT applies.

**(BC') Directional basin containment.** ||delta_u|| < r_eff(mu, mu_2, Delta_bdy, f_1). Unifies (NB) and (GT). Quantitatively 10-100x weaker than (NB) alone.

**(SR-lambda) Spectral coupling bound.** Lambda_coupling < 1/(K-1). Ensures positive joint spectral gap. This IS the regime boundary — beyond it, the theory transitions from persistence to merge.

**(TC-K) Per-formation transport confinement.** ||transport_k(u_s) - u^k_t|| < r_basin^k for each k. Ensures transport uniqueness and core-to-core inheritance. Currently numerically verified; analytical proof requires tighter displacement bound.

**Total: 5 conditions** (down from 7), with (H2') removed (proved), (H3)/(GT) absorbed, (WR') replaced.

**Topology condition (optional, for metastability interpretation only):** Non-increasing isoperimetric profile h(k), or the weaker h(2m) < 2h(m). If included, enables the statement "K>=2 persistence is kinetic (barrier phenomenon)." Not needed for the persistence guarantee itself.

### 3.3. Open problems remaining

1. **Analytical transport confinement bound.** The existing C_conf*sqrt(m) bound is 25-100x too loose at natural parameters. Need either:
   - (a) A perturbative/Lipschitz-based bound near the fixed point, or
   - (b) A tighter entropic OT concentration inequality that includes the fingerprint cost.
   Both approaches are feasible. (a) requires bounding the Sinkhorn Jacobian w.r.t. target marginal; (b) requires extending standard entropic OT concentration to structured costs.

2. **Directional basin radius quantification.** The (BC') criterion from NEARBIF-DIRECTIONAL-EXTENSION.md requires the soft-mode fraction f_1, which depends on the temporal perturbation's alignment with the soft eigenmode. A generic bound f_1 = O(n^{-1/(2d)}) is conjectured but not proved. This would make (BC') automatically satisfied for most formations.

3. **Strong-regime coexistence beyond Weyl.** The condition Lambda_coupling < 1/(K-1) comes from the Weyl bound mu_joint >= min_k(mu_k) - (K-1)*lambda_rep*omega_max. This may be loose — the actual bifurcation could occur at a larger Lambda_coupling if off-diagonal coupling is structured (e.g., only affects boundary modes). A tighter spectral perturbation analysis using the spatial structure of the coupling could extend the coexistence region.

4. **Merge theorem (beyond bifurcation).** What happens at Lambda_coupling > 1/(K-1)? The unified theorem correctly identifies this as the boundary but cannot describe the dynamics beyond it. This requires Morse theory on Sigma^K_M — identifying saddle points and connecting orbits of the gradient flow. The exp30 results (K=2 is always a local minimum, even at high overlap) suggest that the Weyl-based bifurcation boundary may be conservative, and the actual merge transition requires even stronger coupling.

5. **Isoperimetric ordering on general graphs.** While exp35 found no violations in 24 topologies, a theoretical characterization of the graph class where h(2m) < 2h(m) holds would strengthen the metastability interpretation. The conjecture is that it holds on all graphs with sublinear isoperimetric profile (h(k) -> 0 as k -> infinity), which includes all polynomial-growth graphs.

---

## 4. Summary Table

| Component | Status before | Status after this analysis |
|-----------|--------------|---------------------------|
| Isoperimetric ordering | Proved (with conditions) | Proved; NOT necessary for persistence (only for metastability characterization) |
| Transport confinement bound | Proved (C_conf*sqrt(m)) | Proved but 25-100x loose; tightening path identified |
| (TC) vs (WR') | (WR') used as condition | (TC) is strictly weaker; (WR') replaceable; exp40 confirms persistence when WR' fails |
| (TC) analytical proof | Not attempted | Feasible via perturbative approach; existing bound insufficient at natural parameters |
| Minimal conditions for Unified | 7 conditions | 5 conditions (2 removed, 2 absorbed) |
| Isoperimetric ordering for Unified | Assumed needed | Not needed; separate theorem for landscape characterization |
