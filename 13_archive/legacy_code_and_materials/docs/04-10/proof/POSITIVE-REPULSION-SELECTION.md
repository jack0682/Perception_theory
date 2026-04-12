# Positive-Repulsion First-Order Branch Selection Lemma

**Date:** 2026-04-10
**Session:** R1 branch-selection proof cycle
**Category:** proof
**Status:** active
**Depends on:** ZERO-REPULSION-BRANCH-DEGENERACY.md; docs/04-10/audit/theorem-closing/SWEEP-ANALYSIS-R1.md

---

## 1. Purpose

The lambda-rep sweep showed a sharp empirical distinction between `lambda_rep=0` and every tested positive value for `20x20_c0.6`. This lemma isolates the mathematical mechanism available at theorem level: positive repulsion perturbs zero-repulsion branch degeneracy by the overlap functional.

---

## 2. Fixed-Candidate Selection Lemma

Let `A` be a finite or compact family of K=2 candidate pairs `(u_1,u_2)` satisfying:

1. each pair lies in `Sigma_{m_1} x Sigma_{m_2}`;
2. all pairs have the same self-energy sum

```text
E_self(u_1)+E_self(u_2)=E_0;
```

3. all pairs have zero simplex-barrier violation

```text
||(u_1+u_2-1)_+||_2^2 = 0.
```

For fixed fields in `A`, the K=2 energy with repulsion is

```text
E_2^lambda(u_1,u_2)=E_0 + lambda_rep <u_1,u_2>.
```

Therefore, for every `lambda_rep>0`, minimizers of `E_2^lambda` over the candidate family `A` are exactly minimizers of the overlap functional `<u_1,u_2>` over `A`.

### Proof

The common self-energy and common zero barrier are constant on `A`. Thus the only term depending on the candidate pair is `lambda_rep <u_1,u_2>`. Since `lambda_rep>0`, minimizing `E_2^lambda` is equivalent to minimizing `<u_1,u_2>`. ∎

---

## 3. Smooth-Branch Envelope Lemma

Let `z(lambda)=(u_1(lambda),u_2(lambda))` be a differentiable local minimizer branch of the constrained K=2 problem on a fixed active stratum, with Lagrange multipliers enforcing the two mass constraints. Let

```text
F(lambda)=E_2(z(lambda); lambda).
```

Then, at any non-degenerate smooth branch point,

```text
F'(lambda) = <u_1(lambda), u_2(lambda)>.
```

In particular, at `lambda=0`, the first-order branch energy slope is the branch overlap:

```text
F'(0)=<u_1(0),u_2(0)>.
```

### Proof

Differentiate

```text
E_2(u_1,u_2;lambda)
  = E_self(u_1)+E_self(u_2)
    + lambda <u_1,u_2>
    + lambda_bar ||(u_1+u_2-1)_+||_2^2.
```

Along a constrained local minimizer branch, the derivative contributions through `u_1'(lambda),u_2'(lambda)` vanish against feasible tangent directions by the KKT stationarity equations on the fixed active stratum. The remaining explicit parameter derivative is

```text
partial_lambda E_2 = <u_1(lambda),u_2(lambda)>.
```

This is the standard envelope theorem / constrained KKT differentiation argument. ∎

---

## 4. Consequence for R1

The zero-repulsion degeneracy lemma says branch selection can be underdetermined at `lambda_rep=0`. This positive-repulsion lemma says that the first branch-ordering term for small positive `lambda_rep` is overlap.

Thus a mathematically honest branch theorem has the form:

> Positive repulsion selects minimum-overlap branches among zero-repulsion degenerate candidates, up to higher-order branch deformation and active-set changes.

This does **not** prove centeredness by itself. To infer Type A/centered selection, one still needs a graph-geometric lemma showing that minimum-overlap feasible pairs correspond to centered/well-separated placements under the relevant symmetry and volume assumptions.

---

## 5. Remaining Obstruction

Overlap minimization and centeredness are not equivalent on arbitrary graphs. In asymmetric or irregular graphs, minimum-overlap placements may be off-center. Therefore any theorem claiming Type A centered selection must include graph symmetry/geometric hypotheses, or be restricted to the operational branch descriptor measured by exp65.
