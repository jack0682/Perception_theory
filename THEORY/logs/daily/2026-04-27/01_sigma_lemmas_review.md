# 01_sigma_lemmas_review.md — G0 Decision Packet (σ Supporting Structures Canonical Merge)

**Session:** 2026-04-27 (W5 Day 1 AGGRESSIVE)
**Target (from plan.md §3 Block 1, 09:00–09:30):** G0 user decision Option α/β/γ on σ-framework supporting lemmas/theorems canonical merge granularity.
**This file covers:** Decision summary + corrected statement scoping (per `pre_brainstorm.md` §1.1/1.2/1.3) + default action.
**Depends on reading:** `THEORY/canonical/canonical.md` §11.1 (Commitment 14), §13 (T-V5b-T entry as insertion anchor); `THEORY/logs/daily/2026-04-24/02_development.md` §3 (Lemma 1), §4 (Lemma 2), §5 (Theorem 1), `04_orbital_proofs.md` §1 (Theorem 3), §2 (Theorem 4), §3 (Lemma 3); `pre_brainstorm.md` §1 (technical hurdles).

---

## §1. Context

W4-04-24 produced 5 supporting structures for the σ-framework that have lived in `working/` since:

| ID | Statement (one-liner) | Cat (W4 self-classification) | Source |
|----|----------------------|-------------------------------|--------|
| Lemma 1 | Hessian commutes with $G_u$-action; eigenspaces decompose into $G_u$-irreps via Maschke | A | `04-24/02_development.md` §3 |
| Lemma 2 (i) | Nodal count is graph-intrinsic (function of $\phi_k$ + adjacency) | A | `04-24/02_development.md` §4 |
| Lemma 2 (ii) | $\mathrm{Aut}(G)$-equivariance: $\mathcal{N}(\pi\cdot\phi_k) = \mathcal{N}(\phi_k)$ | A | same |
| Lemma 2 (iii) | Courant bound $\mathcal{N}(\phi_k) \leq k+1$ | C (signed-Laplacian frustration) | same |
| Lemma 2 (iv) | Sign-flip invariance | A | same |
| Lemma 3 | Goldstone basis $(\delta u_x, \delta u_y)$ saturates ℓ=1 angular sector via IBP identity | A | `04-24/04_orbital_proofs.md` §3 |
| Theorem 3 | $\sigma(c\mathbf{1})$ on $D_4$ free-BC grid: $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ closed form | A | `04-24/04_orbital_proofs.md` §1 |
| Theorem 4 | $\sigma(u^*_\epsilon)$ at first pitchfork: $D_4 \to \mathbb{Z}_2$ symmetry breaking, irrep relabeling | A in $\epsilon$-small regime | `04-24/04_orbital_proofs.md` §2 |

These are referenced from canonical §11.1 Commitment 14 (final sentence: *"supporting Lemma 1/2/3, Theorem 3/4 — T2 deferred, W5+ user decision for §13 entries"*) but are not themselves canonical.

W5 G0 promotes them to §13.

---

## §2. Decision Options (Three Granularities)

### Option α — five separate §13 entries (RECOMMENDED, default)

Insert after T-V5b-T:

1. `T-σ-Lemma-1` — Irrep decomposition well-defined.
2. `T-σ-Lemma-2` — Nodal count graph-intrinsic (sub-statements (i, ii, iv) Cat A; (iii) Cat C separately registered).
3. `T-σ-Lemma-3` — Goldstone–ℓ=1 saturation identity.
4. `T-σ-Theorem-3` — σ closed form at $u \equiv c$ on $D_4$ grid.
5. `T-σ-Theorem-4` — σ leading order at first pitchfork.

**Counts effect:** +5 Cat A → 38A → **43A**, 52 → **57 claims**, 73% → 75.4% ≈ **75%**.
**T1 effect:** 3 → **8** (per W5 strategic plan §0.4 Decision 1 estimate).

**Pros:**
- Mathematical independence of statements is reflected in canonical structure.
- Each entry independently verifiable; future edit (e.g., strengthening Lemma 2 (iii) from C → B) does not entangle other lemmas.
- Paper 1 §4 σ-framework can cite individual entries.

**Cons:**
- canonical.md grows by ~600 lines in single commit.
- §13 entry count visibly inflates (43 → reads as fast progression; may need narrative balance in §15).

### Option β — one combined §13 entry `T-σ-Supporting`

Single entry containing all 5 statements as labeled sub-results, with consolidated proof. **Counts effect:** +1 Cat A → 39A, +1 claim → 53.

**Pros:** Compact; treats supporting structure as one mathematical object.
**Cons:** Erodes granular tracking; future revision of one sub-statement requires editing the combined entry.

### Option γ — hybrid (Lemmas combined, Theorems separate)

`T-σ-Lemmas-1-3` (combined) + `T-σ-Theorem-3` + `T-σ-Theorem-4`. **Counts effect:** +3 Cat A → 41A, +3 claims → 55.

**Pros:** Lemmas form a logical unit (foundational for σ); theorems are σ instantiations on distinct configurations.
**Cons:** Slightly arbitrary cut; Lemma 3 is conceptually closer to Theorem 1 (Goldstone) than to Lemmas 1/2.

---

## §3. Default (No User Decision by 09:30)

**Per plan.md §3 Block 1 09:00–09:30**: Default is **Option α** (5 separate entries).

Rationale (W5 strategic plan §0.4 Decision 1, recommendation): *"mathematically independent statements deserve individual canonical visibility."* Each lemma has distinct hypotheses, distinct proof tools (Maschke for L1; signed-graph Courant for L2 (iii); IBP identity for L3; closed-form spectral analysis for T3; Crandall–Rabinowitz perturbation for T4) and would be retrieved independently in publications.

This file commits to **Option α** for the remainder of the W5 Day 1 work unless user overrides.

---

## §4. Statement Scoping Corrections (from `pre_brainstorm.md`)

Three corrections to the statements as written in plan.md §10 templates were identified in pre-session brainstorming and are folded into `01a–01e` below.

### 4.1 Lemma 1 — finite-graph hypothesis is essential (`pre_brainstorm.md` §1.1)

**Plan template:** $G_u = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$ acts on $T_{u^*}\Sigma_m$.

**Issue:** $\mathrm{Aut}(G)$ may be infinite for non-finite graphs (e.g., $\mathbb{Z}^d$ on infinite lattice). Maschke's theorem requires finite groups to provide isotypic projectors $P_{[\rho]} = (\dim\rho/|S|)\sum_\pi \overline{\chi_\rho(\pi)} \pi$.

**Correction:** Statement assumes $G$ **finite** (so $\mathrm{Aut}(G)$ finite, hence $G_u$ finite). This matches the canonical scope (canonical §3.1: "X_t is a finite set"; 04-24/02_development.md §1.1 explicitly: "finite simple connected graph").

**Trivial-stabilizer remark:** When $G_u = \{e\}$ (generic asymmetric minimizer), the only irrep is trivial; Lemma 1 holds vacuously but gives no information. Statement remains valid but informative content concentrates in non-trivial-stabilizer cases.

### 4.2 Lemma 2 — sub-statement (iii) wording (`pre_brainstorm.md` §1.2, §1.3)

**Plan template:** "n_k = 1 iff $\phi_k$ constant" + "(iv) symmetry constraint: n_k divisible by minimum orbit size".

**Issue (iii):** $n_k = 1$ does not require constancy — it requires *sign-definiteness on the connected graph*. Volume tangent $\phi_0 = (1/\sqrt{n})\mathbf{1}$ is the trivial sign-definite case but other sign-definite eigenvectors can occur (e.g., the trivial irrep direction in the Hessian's $\mathbf{1}^\perp$ restriction in some symmetric configurations).

Actually for $\phi_k \in \mathbf{1}^\perp$ with $\phi_k \neq 0$: $\sum_i \phi_k(i) = 0$ forces sign change unless $\phi_k = 0$. Hence on $\mathbf{1}^\perp$, **strict sign-definiteness is impossible**. The correct statement is therefore: $\mathcal{N}(\phi_k) \geq 2$ for all $\phi_k \in \mathbf{1}^\perp \setminus \{0\}$ (lower-bound version) — this is what we register.

**Issue (iv):** "Divisible by minimum orbit size" is sharp only for *non-invariant* eigenvectors. Eigenvectors that are themselves $G_u$-invariant (sit in trivial irrep) have orbit size 1 and the divisibility is vacuous.

**Correction:** restrict (iv) to non-invariant eigenvectors and state as conditional.

### 4.3 Lemma 3 — δu^ref interpretation (`pre_brainstorm.md` §1.4)

**Plan template:** "$(\partial_{x_i} u^*, \delta u_{x_i}^{\mathrm{ref}})$ saturate ℓ=1 angular sector by IBP."

**Issue:** $\delta u_{x_i}^{\mathrm{ref}}$ underspecified. Two readings:
- (A) $\delta u_{x_i}^{\mathrm{ref}} = \partial_{x_i} u^{\mathrm{ref}}$ (reference disk profile derivative). IBP trivial.
- (B) $\delta u_{x_i}^{\mathrm{ref}}$ = unit vector in ℓ=1 angular subspace (i.e., $\psi^{(c)}_{\ell=1}(i) = \cos\theta_i$, $\psi^{(s)}_{\ell=1}(i) = \sin\theta_i$).

**Correction:** the W4-04-24 proof (`04_orbital_proofs.md` §3.3 Step 2) actually computes
$$\mathcal{P}_{\ell=1}[\delta u_x] = \sum_i \delta u_x(i) \cdot (\cos\theta_i, \sin\theta_i) \approx (-m, 0)$$
via IBP $\int (\partial_x u^*) \cos\theta \cdot r\,dr\,d\theta = -\int u^* \partial_x(r\cos\theta)\,dr\,d\theta = -\int u^*\,dx\,dy = -m$.

So the saturation is between the **translation derivative** (Goldstone basis) and the **ℓ=1 angular basis** — interpretation (B) is correct. Lemma 3 statement adopts (B) explicitly with the IBP identity as its proof core.

---

## §5. Hard Constraints Verification

Per MAIN_PROMPT §8 + plan.md §6:

- [x] Five entries Cat A claims rest on either (a) standard finite-group rep theory + Maschke (Lemma 1), (b) standard graph theory + signed-graph Courant qualifier (Lemma 2 (i,ii,iv) Cat A; (iii) Cat C explicit), (c) IBP identity (Lemma 3), (d) Hessian closed form Prop 1.3a (Theorem 3), (e) Crandall–Rabinowitz (Theorem 4).
- [x] No silent resolution of OP-0001..OP-0007 — these supporting structures concern σ-framework well-definedness, not the open problems.
- [x] Pre-objectivity primitive ordering preserved (u_t primitive; σ is *measurement* of Hessian at minimizer, not a primitive override).
- [x] No four-energy-term merging.
- [x] No closure-idempotence assumption.
- [x] No K integer/continuous double-treatment (these supporting structures are single-formation only on $\Sigma_m$).
- [x] No metastability claim (Hessian sign analysis is static, not zero-T metastability).

---

## §6. Decision

**Committed: Option α — 5 separate §13 entries.**

Default trigger reason: no user decision recorded by 09:30. Per plan.md §7 contingency F1.

Action plan (next files):
- `01a_lemma1_irrep_decomposition.md` — full statement + 4-step proof + finite-graph hypothesis flagged + canonical wording draft.
- `01b_lemma2_nodal_count.md` — 4 sub-statements with corrections from §4.2; Cat split A/A/A/C.
- `01c_lemma3_goldstone_saturation.md` — IBP identity (interpretation B) + ℓ=1 saturation + canonical wording.
- `01d_theorem3_uniform_D4_grid.md` — closed form + sign analysis at $c=0.5$ + 4×4 worked example.
- `01e_theorem4_first_pitchfork.md` — leading-order σ at $u^*_\epsilon$ + $D_4 \to \mathbb{Z}_2$ irrep relabeling.

After: canonical/theorem_status/CHANGELOG edits per Block 3.
