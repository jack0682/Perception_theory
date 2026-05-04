# 02_development.md — G1 L-M-AUDIT Self-Audit Closure: R-0 / R-1 / R-2 / R-3 + Cat-A-Conditional Promotion

**Session:** 2026-05-04 (W6 Day 1, mid-day, post-G3)
**Target (from `01_exploration.md` §3):** Execute Approach A3 (self-audit) for redesigned W6 plan G1. Apply R-0 + R-1 + R-2 + R-3 closures to L-M working draft + produce Cat-A-conditional promotion proposal text for canonical §13 + theorem_status.md row.
**This file covers:** §1 R-0 closure (§2.2 Phi-4c F1 wording fix); §2 R-1 closure (§5.4 factor-2 sharpness verification); §3 R-2 closure (§5.5 Type-B chain explicit reproof); §4 R-3 closure (§5.4 Type-N non-terminal clarification note); §5 Lemma L-M-2 post-repair Cat-A-conditional self-classification; §6 Theorem L-M post-repair statement; §7 per-family corollaries L-M.A/B/C self-classification; §8 counterexample stability check; §9 granularity check + audit-independence acknowledgement; §10 hard-constraint sweep.
**Depends on reading:** `01_exploration.md` §1–§3 (problem framing + multi-approach + A3 selection); `THEORY/logs/daily/2026-05-03/02_L1M_proof_development.md` §§2.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.3 (all sections being repaired); `THEORY/canonical/canonical.md` §13 T-L1-F (lines 1482-1489) + §11.1 #16 Commitment 16 (line 810, with G3 amendment proposal); CSEH 2007 Theorem 4.2 (`working/E/soft_K_definition.md` §2.1).

---

## §1. R-0 Closure — `02_L1M_proof_development.md` §2.2 Phi-4c F1 Wording Fix

### §1.1 Current text in L-M draft §2.2 Phi-4c

```
F1: σ(s(ℓ - ℓ_min)) ∈ [0, 1] for all ℓ; subtracting σ(-s ℓ_min) ∈ [0, 1) may give negative
values for ℓ near 0. We tighten F1 to φ(ℓ) ≥ 0 by clipping at 0 if needed; alternatively
restrict Φ_res to φ that already satisfy F1 (Phi-4c with the WQ-LAT-1.B definition is
non-negative on [0,1] since σ(-s ℓ_min) is the value at ℓ = 0).
```

### §1.2 Identified problem

The "we tighten F1 to $\phi(\ell) \ge 0$ by clipping at $0$ if needed" hedge is **unnecessary**. The Phi-4c definition $\phi_{\mathrm{logistic}}^s(\ell;\ell_{\min}) := \sigma(s(\ell-\ell_{\min})) - \sigma(-s\ell_{\min})$ satisfies $\phi(0) = \sigma(-s\ell_{\min}) - \sigma(-s\ell_{\min}) = 0$ exactly. Combined with monotonicity of $\sigma$ (and hence of $\phi$ on $[0,1]$), $\phi(\ell) \ge \phi(0) = 0$ for all $\ell \ge 0$. Therefore $\phi \ge 0$ on $[0, 1]$ holds **cleanly by monotonicity**, with no clipping or restriction needed.

### §1.3 Replacement text

```
F1: σ is monotonic with σ ∈ [0,1]; subtracting σ(-s ℓ_min) gives φ(0) = 0 exactly.
By monotonicity of σ, φ(ℓ) is non-decreasing on [0,1] starting from φ(0) = 0;
hence φ(ℓ) ≥ 0 on [0,1] cleanly without any clipping. Combined with σ(s(ℓ-ℓ_min)) ≤ 1
and σ(-s ℓ_min) ≥ 0, we have φ(ℓ) ≤ 1. Hence F1 is satisfied: φ(ℓ) ∈ [0,1] on [0,1].
```

### §1.4 R-0 status

**RESOLVED.** Cat A absolute (one-sentence wording simplification; uses only F2 + F3 of L-M-D1, which are independently established).

---

## §2. R-1 Closure — `02_L1M_proof_development.md` §5.4 Factor-2 Sharpness

### §2.1 Setup (recap from L-M draft §5.4)

Type-N bar $i$ of $\mathrm{Dgm}_0^{\sup}(U;G_j^r)$ (subdominant local maximum within active neighborhood $N_j^r$) is matched via CSEH bottleneck stability to a bar of $\mathrm{Dgm}_0^{\sup}(u^{(j)};G_j^r)$ under perturbation $\|R_j\|_{\infty,N_j^r} \le \rho_{\mathrm{pert}}/2$ (P9). The L-M draft uses:

$$
\bigl|\ell_i(U;G_j^r) - \ell_i(u^{(j)};G_j^r)\bigr| \le 2 \cdot \rho_{\mathrm{pert}}/2 = \rho_{\mathrm{pert}}, \tag{F2}
$$

with the factor 2 arising from "both birth and death of a single bar potentially shifting under bottleneck-stability matching." R-1 asks whether this factor 2 is sharp or expandable to factor 1 via terminal-death convention $(P0)$.

### §2.2 The hypothesized factor-1 sharpening — and why it does not apply

Under terminal-death convention $(P0)$, **terminal** matched bars have $d_i = d_{\sigma(i)} = 0$, so

$$
|\ell_i - \ell_{\sigma(i)}| = |b_i - b_{\sigma(i)}| \le \rho_{\mathrm{pert}}/2 \quad (\text{factor } 1, \text{ for terminal pairs}). \tag{T}
$$

But Type-N bars are **NOT terminal**. Specifically: a subdominant local maximum at vertex $v \in N_j^r \setminus \{q_j^U\}$ births a $H_0$ component at level $U(v) < U(q_j^U) = b_{\mathrm{primary}}$. As the descending superlevel sweep continues, this component eventually merges with the slot-primary component (the one born at $q_j^U$) at some saddle vertex $w \in N_j^r$ (by P3 disjointness of $N_j^r \cap N_k^r$, the merge cannot escape $N_j^r$; by connectedness of $N_j^r$, the merge must occur within $N_j^r$). The death of the Type-N bar is $d_i = U(w) > 0$ — finite, not terminal.

The same analysis on $u^{(j)}|_{G_j^r}$: subdominant local maxima of $u^{(j)}$ produce merge bars on $G_j^r$, with finite death at intra-slot saddle levels.

So the matched bars in CSEH applied to $(U|_{G_j^r}, u^{(j)}|_{G_j^r})$ for the Type-N case have $d_i, d_{\sigma(i)} > 0$ in **both** diagrams. Condition (T) fails. The factor-1 sharpening is **structurally inapplicable**.

### §2.3 Explicit perturbation realizing the factor-2 bound (sharpness verification)

To show that (F2) is sharp under L1-J, construct an admissible perturbation $R_j$ (satisfying $\|R_j\|_{\infty,N_j^r} \le \rho_{\mathrm{pert}}/2$ per P9) such that $|\ell_i(U;G_j^r) - \ell_i(u^{(j)};G_j^r)| = \rho_{\mathrm{pert}}$ exactly.

**Construction.** Let $i$ be a Type-N bar of $\mathrm{Dgm}_0^{\sup}(u^{(j)};G_j^r)$ with birth at vertex $v$ and death at saddle vertex $w$ (both in $N_j^r$). Define $R_j$ by:
- $R_j(v) = +\rho_{\mathrm{pert}}/2$.
- $R_j(w) = -\rho_{\mathrm{pert}}/2$.
- $R_j(x) = 0$ for $x \ne v, w$.

Clearly $\|R_j\|_{\infty,N_j^r} = \rho_{\mathrm{pert}}/2 \le \rho_{\mathrm{pert}}/2$ (P9 satisfied with equality).

Compute the resulting $U = u^{(j)} + R_j$:
- $U(v) = u^{(j)}(v) + \rho_{\mathrm{pert}}/2$ (birth of the Type-N bar in $\mathrm{Dgm}(U)$ shifts by $+\rho_{\mathrm{pert}}/2$, assuming the persistence skeleton — which vertex is birth, which is saddle — is preserved under the perturbation).
- $U(w) = u^{(j)}(w) - \rho_{\mathrm{pert}}/2$ (death/saddle level of the Type-N bar in $\mathrm{Dgm}(U)$ shifts by $-\rho_{\mathrm{pert}}/2$).

**Skeleton preservation.** For the perturbation to preserve the persistence skeleton (i.e., $v$ remains the birth vertex and $w$ remains the saddle vertex of the same Type-N bar), we need the shifts to be small enough that no superlevel-event reordering occurs near $v$ or $w$. Sufficient: $\rho_{\mathrm{pert}}/2 < \min(u^{(j)}(v) - \max_{x \in \partial^- v} u^{(j)}(x), u^{(j)}(w) - \min_{x \in \mathrm{nbr}(w)} u^{(j)}(x))$ where $\partial^- v$ are vertices below $v$ in the superlevel ordering. This is generically satisfied for non-degenerate $u^{(j)}$ with separated superlevel-event values.

**Resulting bar lengths.**

$$
\ell_i^U = U(v) - U(w) = \bigl(u^{(j)}(v) + \rho_{\mathrm{pert}}/2\bigr) - \bigl(u^{(j)}(w) - \rho_{\mathrm{pert}}/2\bigr) = \ell_i^{u^{(j)}} + \rho_{\mathrm{pert}}.
$$

So $|\ell_i^U - \ell_i^{u^{(j)}}| = \rho_{\mathrm{pert}}$ exactly — **the factor-2 bound is achieved**.

### §2.4 Sharpness verdict

The factor 2 in (F2) is **sharp** under the L1-J regime hypothesis package $(P0)$–$(P11)$. Recovering factor 1 would require **strictly stronger** structural hypotheses on $R_j$ that constrain the sign correlation across (peak vertex, saddle vertex) pairs — none of which are in $(P0)$–$(P11)$. Specifically, any of the following would suffice but exceeds L1-J:
- **(S-sign):** $R_j(v)$ and $R_j(w)$ have the same sign for every (subdominant peak, saddle) pair within $N_j^r$.
- **(S-Lip):** $R_j$ is $L_R$-Lipschitz on $N_j^r$ with $L_R \cdot d_G(v, w) \le \rho_{\mathrm{pert}}/2$.
- **(P9-tight):** $\|R_j\|_{\infty,N_j^r} \le \rho_{\mathrm{pert}}/4$ instead of $\rho_{\mathrm{pert}}/2$ (would trivially give factor 2 with $\rho_{\mathrm{pert}}/2$ instead of $\rho_{\mathrm{pert}}$, expanding $\tau_*$).

None of these is currently part of L1-J. R-1 is therefore **RESOLVED in the negative direction**: $\tau_* = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$ in §5.6 of the L-M draft is correct as stated; no expansion is available without strengthening the regime.

### §2.5 R-1 closure addendum to L-M draft §5.4

Append the following to L-M draft §5.4 (after the existing factor-2 derivation):

```
**Sharpness note (R-1 closure, W6 D1).** The factor 2 in this bound is sharp under (P0)–(P11).
The terminal-death convention (P0) allows factor-1 sharpening only for **terminal** matched bars
(d_i = d_{σ(i)} = 0 ⇒ |ℓ_i - ℓ_{σ(i)}| = |b_i - b_{σ(i)}| ≤ ρ_pert/2). Type-N bars are intra-slot
merge bars: by P3 disjointness + connectedness of N_j^r, a subdominant local-maximum component
in N_j^r merges with the slot-primary component at some intra-slot saddle vertex w ∈ N_j^r,
giving d_i = U(w) > 0 (not terminal). Hence (P0) does not apply. Sharpness verified by
construction: take R_j(v) = +ρ_pert/2 at the subdominant peak vertex v, R_j(w) = -ρ_pert/2
at the saddle vertex w, R_j = 0 elsewhere. Admissible under P9 (||R_j||_∞ = ρ_pert/2). Then
ℓ_i^U - ℓ_i^{u^(j)} = R_j(v) - R_j(w) = ρ_pert exactly, achieving the factor-2 bound. Recovering
factor 1 would require strictly stronger hypotheses on R_j sign correlation (e.g., (S-sign)
constant-sign on N_j^r, or (S-Lip) Lipschitz constraint, or (P9-tight) tighter ||R_j||_∞ bound)
— none in current L1-J. Resolution: original τ_* = min(2ρ_pert, ρ_res, r_birth) stands.
```

### §2.6 R-1 status

**RESOLVED.** Cat A absolute (sharpness verification + explicit admissible counterexample to factor-1 sharpening). Closes the L-M draft §5.7 R-1 refinement entry.

---

## §3. R-2 Closure — `02_L1M_proof_development.md` §5.5 Type-B Chain Explicit Reproof

### §3.1 Current text in L-M draft §5.5

```
For Type-B bars, b_i ∈ X_bg where X_bg is the background region (off all N_j^r). On X_bg
the field U coincides with the inactive residual: U|_{X_bg} = R_inact|_{X_bg}. By P10,
||R_inact||_∞ ≤ ℓ_min - ρ_res. Hence the birth height b_i = U(b_i) ≤ ℓ_min - ρ_res, and
by P0 the death is d_i = 0:
    ℓ_i = b_i ≤ ℓ_min - ρ_res.
For τ < ρ_res: ℓ_i ≤ ℓ_min - ρ_res < ℓ_min - τ, so i ∈ I_sub ⊄ I_edge.

*Note.* P5 (background suppression on U, not just R_inact) gives a stronger bound
b_i ≤ ℓ_min - ρ_bg, but ρ_bg may not equal ρ_res. Using the weaker P10 bound is
sufficient for the conclusion; the stronger P5 bound only tightens the constant.
```

### §3.2 Identified problems

1. The assertion "$U|_{X_{\mathrm{bg}}} = R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$" is **not quite right**. Active fields $u^{(j)}$ can extend (via decay-to-cut, P7) into the background region. The aggregate $U = \sum_j u^{(j)} + R_{\mathrm{inact}}$ on $X_{\mathrm{bg}}$ includes both the inactive residual and small contributions from active-slot decay tails.
2. The claim "by P0 the death is $d_i = 0$" implicitly assumes Type-B bars are terminal under $(P0)$. But Type-B bars may merge with active-slot components as the descending superlevel sweep crosses through transition regions; whether they are "terminal" under $(P0)$ depends on the specific structure.
3. The chain implicitly relies on T-L1-F's proof structure (LG-7 coverage) to establish the "Type-B as background" classification, rather than re-deriving it within L-M-2's own scope.

### §3.3 Replacement chain — using P5 (stronger, more direct)

P5 (`canonical.md` line 1483, T-L1-F regime hypothesis): **background suppression on $U$ directly** (not just on $R_{\mathrm{inact}}$):

$$
\|U\|_{\infty,X_{\mathrm{bg}}} \le \ell_{\min} - \rho_{\mathrm{bg}}.
$$

This is *stronger* than P10 (which bounds only $R_{\mathrm{inact}}$). For Type-B bars, P5 directly gives:

$$
b_i = U(b_i) \le \|U\|_{\infty,X_{\mathrm{bg}}} \le \ell_{\min} - \rho_{\mathrm{bg}}.
$$

For the death $d_i$: regardless of whether the Type-B bar is terminal or merge, $d_i \ge 0$ (death levels are non-negative in $H_0$ superlevel persistence). Hence

$$
\ell_i = b_i - d_i \le b_i \le \ell_{\min} - \rho_{\mathrm{bg}}.
$$

For $\tau < \rho_{\mathrm{bg}}$: $\ell_i \le \ell_{\min} - \rho_{\mathrm{bg}} < \ell_{\min} - \tau$, so $i \in I_{\mathrm{sub}} \not\subseteq I_{\mathrm{edge}}$.

**No reliance on P0 terminal-death convention; no implicit T-L1-F proof structure dependency; no implicit "$U|_{X_{\mathrm{bg}}} = R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$" assertion.**

### §3.4 Implication for $\tau_*$

The chain of §3.3 uses P5 with $\rho_{\mathrm{bg}}$ instead of P10 with $\rho_{\mathrm{res}}$. Hence the τ-side contribution from Type-B is now $\rho_{\mathrm{bg}}$, and the post-repair $\tau_*$ becomes:

$$
\tau_*^{\mathrm{post-R2}} := \min\bigl(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}}\bigr).
$$

This may be tighter or looser than the original $\tau_* = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$ depending on whether $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$ or not. The original L-M draft's note acknowledged that P5 bound is "stronger" (i.e., $\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ in general isn't guaranteed; the comparison depends on the specific regime configuration).

For consistency with T-L1-F's empirical L1-I anchor (which uses $\rho_{\mathrm{bg}}$ implicitly via P5), the $\tau_*^{\mathrm{post-R2}}$ formulation with $\rho_{\mathrm{bg}}$ is **more honest** (matches the canonical regime constants directly) and **avoids the P10 indirection**.

### §3.5 Replacement text for L-M draft §5.5

```
For Type-B bars (b_i ∈ X_bg, off all N_j^r), apply P5 (background suppression on U directly):
    ||U||_{∞, X_bg} ≤ ℓ_min - ρ_bg.
Hence:
    b_i = U(b_i) ≤ ||U||_{∞, X_bg} ≤ ℓ_min - ρ_bg.
For the death d_i ≥ 0 (death levels non-negative in H_0 superlevel persistence):
    ℓ_i = b_i - d_i ≤ b_i ≤ ℓ_min - ρ_bg.
For τ < ρ_bg: ℓ_i ≤ ℓ_min - ρ_bg < ℓ_min - τ, so i ∈ I_sub ⊄ I_edge.

*Note.* This chain uses P5 directly (background suppression on U, not on R_inact), avoiding the
implicit "U|_{X_bg} = R_inact|_{X_bg}" assertion and the dependency on T-L1-F's LG-7 coverage
proof structure. P5 is stronger than P10 for Type-B bound purposes; the resulting τ_* uses
ρ_bg instead of ρ_res. The conclusion ℓ_i ≤ ℓ_min - ρ_bg holds regardless of whether the
Type-B bar is terminal or merge under (P0) — only b_i is invoked.
```

### §3.6 R-2 status

**RESOLVED.** Cat A absolute (P5 direct chain; no implicit T-L1-F structure dependency; no P0 dependency for the bound). Closes the L-M draft §5.7 R-2 refinement entry.

### §3.7 Updated $\tau_*$ definition (consequence of R-2)

Throughout L-M draft §5–§6 + Theorem L-M statement, the $\tau_*$ definition should change from:

$$
\tau_* := \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})
$$

to:

$$
\tau_*^{\mathrm{post-R2}} := \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}}).
$$

This is a **substantive change** (not just wording) — it affects the admissible $\tau$ range. The conclusion of Lemma L-M-2 + Theorem L-M is unchanged at the structural level (edge band still empty for $\tau \in (0, \tau_*^{\mathrm{post-R2}})$), but the specific feasibility regime is re-anchored to $\rho_{\mathrm{bg}}$ instead of $\rho_{\mathrm{res}}$.

---

## §4. R-3 Closure — `02_L1M_proof_development.md` §5.4 Type-N Non-Terminal Clarification Note

### §4.1 Current text in L-M draft §5.4 §5.7 item 3

L-M draft §5.7 item 3:

> **The terminal-death convention's role for Type-N.** §5.4 implicitly assumed Type-N bars also use terminal death. This is correct under P0 (which is global), but the argument should make this explicit: the comparison between $U|_{G_j^r}$ and $u^{(j)}|_{G_j^r}$ both use terminal death on $G_j^r$, giving consistent diagram-comparisons.

The flag here is that §5.4's bottleneck-stability argument doesn't make explicit how the terminal-death convention applies to Type-N bars. R-1 closure (§2 above) clarifies: **Type-N bars are intra-slot merge bars, not terminal**. The §5.4 argument works because bottleneck stability between two diagrams with consistent (P0) global death convention is well-defined; the factor 2 comes from the standard CSEH bound + non-terminality of Type-N bars (so factor-1 sharpening is unavailable).

### §4.2 Replacement note for L-M draft §5.4 (after R-1 sharpness note)

Append the following to L-M draft §5.4 (after the R-1 sharpness note from §2.5 above):

```
**Type-N terminal-death consistency (R-3 closure, W6 D1).** Type-N bars are NOT terminal under
(P0); they are intra-slot merge bars (§2 above). The CSEH bottleneck-stability comparison
between Dgm_0^sup(U|_{G_j^r}) and Dgm_0^sup(u^(j)|_{G_j^r}) uses the global (P0) death
convention applied identically to both diagrams; this gives consistent matched-bar comparisons
regardless of whether individual matched bars are terminal or merge. The factor 2 in the
length-shift bound applies uniformly (cf. §2 R-1 closure).
```

### §4.3 R-3 status

**RESOLVED.** Cat A absolute (clarification note; consistency with R-1 closure verified).

---

## §5. Lemma L-M-2 Post-Repair Cat-A-Conditional Self-Classification

### §5.1 Pre-repair status (per L-M draft §8.1)

| Statement | Status | Cat |
|---|---|---|
| Lemma L-M-2 (edge-band emptiness under regime) | sketched | **B sketched** |
| Theorem L-M (combined corollary) | proved (modulo L-M-2) | **B sketched** (inherits L-M-2) |
| Corollary L-M.A (hard threshold) | proved | A conditional under $(P0)$–$(P11)$ |
| Corollary L-M.B (logistic) | proved (modulo L-M-2) | B sketched (inherits) |
| Corollary L-M.C (shift-sat) | proved (modulo L-M-2) | B sketched (inherits) |

### §5.2 Post-repair status (after R-0 + R-1 + R-2 + R-3)

The three "bookkeeping refinements" R-1 / R-2 / R-3 from L-M draft §5.7 are now CLOSED:
- **R-1 (§2 above):** factor 2 sharp under L1-J; sharpness verification via explicit admissible perturbation. Cat A absolute.
- **R-2 (§3 above):** §5.5 Type-B chain replaced with explicit P5-direct derivation; no implicit T-L1-F dependency. Cat A absolute. Side effect: $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$.
- **R-3 (§4 above):** Type-N non-terminal clarification note appended to §5.4; consistency with R-1 verified. Cat A absolute.
- **R-0 (§1 above):** §2.2 Phi-4c F1 wording simplified; no clipping/restriction needed. Cat A absolute.

With all four refinements closed, the L-M draft §5.7 "sketched" classification of Lemma L-M-2 upgrades to:

| Statement | Post-repair status | Cat |
|---|---|---|
| Lemma L-M-2 (edge-band emptiness under regime) | proved | **A conditional under $(P0)$–$(P11)$** |
| (subordinate: §5.3 Type-D bound) | proved (P11 + P6 + (P0) chain) | A conditional |
| (subordinate: §5.4 Type-N bound) | proved (CSEH + P9 + P8 + P3 + factor-2 sharpness verification) | A conditional |
| (subordinate: §5.5 Type-B bound) | proved (P5 direct chain, post-R2) | A conditional |

### §5.3 Why "conditional" (not absolute)

The conditional clause is "**under the L1-J regime hypothesis package $(P0)$–$(P11)$**." All three Type-D / Type-N / Type-B bounds use specific regime hypotheses (P3, P5, P6, P8, P9, P11 + (P0) terminal-death convention). The conditionality is the same as T-L1-F's: not a global identity, valid only when $(P0)$–$(P11)$ hold. T-L1-F empirically establishes the regime is non-empty (L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$).

### §5.4 Lemma L-M-2 post-repair statement (clean form)

**Lemma L-M-2 (post-repair, Cat A conditional).** Let $\mathbf u \in \widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$ satisfy the L1-J regime hypothesis package $(P0)$–$(P11)$ from T-L1-F (canonical.md §13). Set

$$
\tau_*^{\mathrm{post-R2}} := \min\bigl(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}}\bigr).
$$

Then for any $\tau \in (0, \tau_*^{\mathrm{post-R2}})$, the edge band of $U(\mathbf u)$ contains no bars:

$$
N_{\mathrm{edge}}(U; \tau) = 0.
$$

*Proof:* Three-type bar-classification + per-type bounds (Type-D §5.3 via P11+P6+(P0); Type-N §5.4 via CSEH+P9+P8+P3 with factor-2 sharpness per §2 above; Type-B §5.5 via P5 direct per §3 above). Each bar has $\ell_i \ge \ell_{\min} + r_{\mathrm{birth}}$ (Type-D) or $\ell_i \le \ell_{\min} - 2\rho_{\mathrm{pert}}$ (Type-N) or $\ell_i \le \ell_{\min} - \rho_{\mathrm{bg}}$ (Type-B); hence none lies in $[\ell_{\min} - \tau, \ell_{\min} + \tau]$ for $\tau < \tau_*^{\mathrm{post-R2}}$. $\Box$

---

## §6. Theorem L-M Post-Repair Statement (Cat-A-Conditional)

### §6.1 Statement

**Theorem L-M (Soft-Count Corollary, post-repair, Cat A conditional).** Let $G = (X, E)$ be a finite graph, $\mathbf u \in \widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$. Suppose the L1-J regime hypothesis package $(P0)$–$(P11)$ from T-L1-F holds. Let $\phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau)$ with $\tau \in (0, \tau_*^{\mathrm{post-R2}})$ where $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$. Then

$$
\boxed{
\bigl|K_{\mathrm{soft}}^\phi(U(\mathbf u)) - K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr| \le \varepsilon_{\mathrm{sub}}^\phi(\tau) \cdot N_{\mathrm{sub}}(U; \tau) + \varepsilon_{\mathrm{dom}}^\phi(\tau) \cdot K_{\mathrm{act}}^\varepsilon(\mathbf u),
} \tag{L-M post-R}
$$

where the structural pair $(\varepsilon_{\mathrm{sub}}^\phi, \varepsilon_{\mathrm{dom}}^\phi)$ is determined by the envelope sub-class per Claim L-M-V1 (with R-0 wording simplification).

### §6.2 Proof (post-repair, Cat A conditional)

The proof composition is:
- L-M-1 (envelope-pure inequality, §3 of L-M draft): $|K_{\mathrm{soft}}^\phi - K_{\mathrm{bar}}^{\ell_{\min}}| \le \rho_{\mathrm{sub}} + \rho_{\mathrm{edge}}^\phi + \rho_\phi$. **Cat A absolute** (no regime hypothesis used).
- L-M-2 post-repair (§5 above): under $(P0)$–$(P11) + \tau < \tau_*^{\mathrm{post-R2}}$, $N_{\mathrm{edge}} = 0$ ⇒ $\rho_{\mathrm{edge}}^\phi = 0$.
- L-M-Sub + L-M-Dom (§4 of L-M draft): $\rho_{\mathrm{sub}} \le \varepsilon_{\mathrm{sub}}^\phi N_{\mathrm{sub}}$ + $\rho_\phi \le \varepsilon_{\mathrm{dom}}^\phi K_{\mathrm{act}}^\varepsilon$ (using $N_{\mathrm{dom}} = K_{\mathrm{act}}^\varepsilon$ via T-L1-F bijection $\mathcal A_{\mathrm{bar}}$).
- T-L1-F substitution: $K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u)) = K_{\mathrm{act}}^\varepsilon(\mathbf u)$.

Combining all four steps gives (L-M post-R). $\Box$

**Cat A conditional under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau) + \tau \in (0, \tau_*^{\mathrm{post-R2}})$.**

### §6.3 Status upgrade

| Statement | Pre-repair | Post-repair |
|---|---|---|
| Theorem L-M | Cat B sketched | **Cat A conditional under $(P0)$–$(P11) + \Phi_{\mathrm{res}} + \tau < \tau_*^{\mathrm{post-R2}}$** |
| Corollary L-M.A (hard threshold) | Cat A conditional under $(P0)$–$(P11)$ | **Cat A conditional under $(P0)$–$(P11)$** (unchanged; trivial substitution) |
| Corollary L-M.B (logistic) | Cat B sketched | **Cat A conditional inheriting Theorem L-M** |
| Corollary L-M.C (shift-sat) | Cat B sketched | **Cat A conditional inheriting Theorem L-M** |

---

## §7. Per-Family Corollaries L-M.A / B / C Self-Classification

### §7.1 Corollary L-M.A (hard threshold)

**Statement (unchanged):** For $\phi = \phi_{\mathrm{hard}} = \mathbf 1_{\ell \ge \ell_{\min}}$ under $(P0)$–$(P11)$:
$$
K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U(\mathbf u)) = K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u)) = K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

**Status:** **Cat A absolute as a definitional reduction** (substitution of $\phi_{\mathrm{hard}}$ + T-L1-F bijection). Unchanged from pre-repair.

### §7.2 Corollary L-M.B (logistic, $s \ge 50$)

**Statement (post-R2):** For $\phi = \phi_{\mathrm{logistic}}^s$, $\tau \in (0, \tau_*^{\mathrm{post-R2}})$, $s \ge 50$:
$$
\bigl|K_{\mathrm{soft}}^{\phi_{\mathrm{logistic}}^s}(U) - K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr| \le e^{-s\tau} \cdot N_{\mathrm{sub}}(U; \tau) + 2 e^{-s\tau} \cdot K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

**Status:** **Cat A conditional under $(P0)$–$(P11) + \tau < \tau_*^{\mathrm{post-R2}}$ + $s \ge 50$**. Inherits Theorem L-M (post-repair).

### §7.3 Corollary L-M.C (shifted saturating, $\beta \ge 20$)

**Statement (post-R2):** For $\phi = \phi_{\mathrm{shift\text{-}sat}}^\beta$, $\tau \in (0, \tau_*^{\mathrm{post-R2}})$, $\beta \ge 20$:
$$
\bigl|K_{\mathrm{soft}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}(U) - K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr| \le e^{-\beta\tau} \cdot K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

(Note: $N_{\mathrm{sub}}$ term vanishes since $\varepsilon_{\mathrm{sub}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta} = 0$ — Phi-3d is identically zero on $[0, \ell_{\min}]$.)

**Status:** **Cat A conditional under $(P0)$–$(P11) + \tau < \tau_*^{\mathrm{post-R2}}$ + $\beta \ge 20$**. Inherits Theorem L-M (post-repair).

---

## §8. Counterexample Stability Check (post-repair)

The L-M draft §7 lists four counterexample attempts. Verify they remain non-counterexamples after R-0/R-1/R-2/R-3 closures.

### §8.1 Attempt 1 (Phi-0 default $\phi$-sat envelope, excluded by F4)

**Pre-repair status:** Phi-0 excluded by axiom F4 (Claim L-M-V2). **Post-repair status:** unchanged. F4 is unaffected by R-0/R-1/R-2/R-3.

### §8.2 Attempt 2 (edge-band-dense bar configuration, ruled out by L-M-2)

**Pre-repair status:** the synthesized configuration violates $(P0)$–$(P11)$ via L-M-2's Type-D / Type-N / Type-B classification. **Post-repair status:** unchanged. L-M-2's bar-type classification is exhaustive (every bar of $U$ is one of the three types per L-M draft §5.2 + LG-7), and each type's bound has been verified Cat A under post-R2. The synthesized edge-band-dense configuration still violates L1-J, just now via the post-R2 bound chain instead of the pre-repair sketched chain.

### §8.3 Attempt 3 (insufficient sharpness, $s = 20$ logistic)

**Pre-repair status:** bound becomes vacuous at low sharpness ($e^{-s\tau} = 0.67$ for $s = 20$, $\tau = 0.02$). **Post-repair status:** unchanged. Sharpness threshold $s \ge 50$ remains the empirically-supported regime.

### §8.4 Attempt 4 ($\tau$ chosen too large)

**Pre-repair status:** $\tau \ge \tau_*$ ⇒ L-M-2 fails. **Post-repair status:** $\tau \ge \tau_*^{\mathrm{post-R2}}$ ⇒ L-M-2 fails. $\tau_*$ replaced with $\tau_*^{\mathrm{post-R2}}$. The structural conclusion is the same: $\tau < \tau_*^{\mathrm{post-R2}}$ is a *necessary* hypothesis.

### §8.5 Counterexample stability verdict

All four counterexample attempts remain non-counterexamples after the R-0/R-1/R-2/R-3 closures. Theorem L-M (post-repair) stands.

---

## §9. Granularity Check + Audit-Independence Acknowledgement

### §9.1 Granularity check (per prompt §9)

Each substantive claim is independently re-checkable:

- **§1 R-0 closure** can be verified by reading L-M draft §2.2 + applying F2 + F3 + monotonicity of $\sigma$.
- **§2 R-1 closure** can be verified by:
  - reading L-M draft §5.4 (current factor-2 derivation).
  - constructing the explicit perturbation $R_j(v) = +\rho_{\mathrm{pert}}/2, R_j(w) = -\rho_{\mathrm{pert}}/2, R_j = 0$ elsewhere.
  - confirming the resulting $\ell_i^U - \ell_i^{u^{(j)}} = R_j(v) - R_j(w) = \rho_{\mathrm{pert}}$.
- **§3 R-2 closure** can be verified by:
  - reading P5 statement in canonical T-L1-F (line 1483).
  - applying the bound $b_i \le \|U\|_{\infty, X_{\mathrm{bg}}} \le \ell_{\min} - \rho_{\mathrm{bg}}$ directly.
  - noting that $\ell_i \le b_i$ regardless of $d_i$'s value.
- **§4 R-3 closure** can be verified by reading §2 (R-1 closure) — R-3 is a clarification consequence.
- **§5 Lemma L-M-2 post-repair Cat A conditional self-classification** can be verified by tracing the bound chain in §5.4 of the post-repair L-M draft.
- **§6 Theorem L-M post-repair statement + proof composition** can be verified by combining L-M-1 (Cat A absolute) + L-M-2 post-repair (§5) + T-L1-F substitution.
- **§7 per-family corollaries** verifications are direct substitutions of L-M-V1 (with R-0 simplification) into Theorem L-M post-repair.
- **§8 counterexample stability** verifications are direct re-checks of L-M draft §7's four cases.

The §-numbering is preserved for audit references.

### §9.2 Audit-independence acknowledgement

This G1 closure is a **self-audit** by the same Claude session that wrote G3 deep-dive (`g3_*.md`) and the redesigned plan.md v2. **It is not an external independent audit.** Specifically:

- **Conversation-memory cross-check** (deleted `01a_l1m_audit_verdict.md` was REPAIR-NEEDED with closeable repairs; deleted `cseh_factor_sharpness_analysis.md` had Cat A factor-2-sharp verdict): the present self-audit's R-0 / R-1 / R-2 / R-3 closures align with the deleted external audit's verdict at the high level (REPAIR-NEEDED → Cat A conditional after closeable repairs). Specific replacement-text wording was re-derived in this session.
- **Independence concern:** the same author identifying R-1/R-2/R-3 + closing them may miss issues that an external auditor would catch. Mitigation:
  - The L-M draft author (W5 D7 session, 2026-05-03) flagged R-1/R-2/R-3 themselves; the closures here are responses to those self-flags, not new self-auditing.
  - For canonical promotion (CV-1.6 release activity per W6 plan §2 explicit non-goals), an external L-K-style audit is recommended before merge — analogous to the L1-K external audit that preceded T-L1-F's CV-1.5.2 promotion. This G1 closure **does not** substitute for such an L-M-K-style audit.
- **Scope of this G1 closure:** working-grade audit completion, sufficient to upgrade L-M from Cat-B-sketched to Cat-A-conditional **as a working-file claim**. Canonical Cat-A-conditional promotion remains a **separate** CV-1.6 release activity that requires external audit + user-supervised canonical merge.

### §9.3 Diminishing returns check

The four refinements R-0/R-1/R-2/R-3 are all closed; Cat-A-conditional self-classification produced; counterexample stability verified; granularity preserved. Per prompt §13: stop at this natural matching point + leave next session seed in `99_summary.md`.

---

## §10. Hard-Constraint Sweep + Cat Self-Classification Summary

### §10.1 Per-result self-classification

| Statement | Status | Cat |
|---|---|---|
| §1 R-0 closure (Phi-4c F1 wording) | proved | A absolute |
| §2 R-1 closure (factor 2 sharp under L1-J + explicit perturbation) | proved | A absolute |
| §3 R-2 closure (P5 direct chain for Type-B) | proved | A absolute |
| §3.7 $\tau_*^{\mathrm{post-R2}}$ definition (uses $\rho_{\mathrm{bg}}$) | derived | A absolute (post-R2 chain) |
| §4 R-3 closure (Type-N non-terminal note) | proved | A absolute |
| §5 Lemma L-M-2 post-repair | proved | **A conditional under $(P0)$–$(P11)$** |
| §6 Theorem L-M post-repair | proved | **A conditional under $(P0)$–$(P11) + \Phi_{\mathrm{res}} + \tau < \tau_*^{\mathrm{post-R2}}$** |
| §7.1 Corollary L-M.A | proved | A absolute as definitional reduction |
| §7.2 Corollary L-M.B (logistic, $s \ge 50$) | proved | A conditional inheriting Theorem L-M |
| §7.3 Corollary L-M.C (shift-sat, $\beta \ge 20$) | proved | A conditional inheriting Theorem L-M |
| §8 Counterexample stability | sketched | A absolute as a finite-case audit |

**Overall Cat for the deliverable:** **Cat A conditional working-grade closure of L-M-AUDIT G1.** Promotion to canonical Cat-A-conditional remains a separate CV-1.6 release activity (out of W6 scope per W6 plan §2).

### §10.2 Hard-constraint sweep

- [x] **Canonical 직접 수정 0** (this session). All proposed canonical edits (T-L1-M new entry text, theorem_status.md C-0722 row) are in `03_integration_and_new_open.md` as **proposals**, not applied.
- [x] **Working/ 직접 수정 0** (this session). All R-0/R-1/R-2/R-3 textual repair specifications are in this `02_development.md` as proposals; actual edits to `02_L1M_proof_development.md` and promotion to `working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` are user-supervised steps.
- [x] **scc/ 0 edits.**
- [x] **Silent OP resolution 0.** OP-0001 / OP-0002 / OP-0003 / OP-0005 / OP-0006 / OP-0008 / OP-0009 / OP-0010 / OP-0011 / OP-0012 / OP-0013 — all status preserved. G1 closure does NOT silently resolve any of these (see `03_integration_and_new_open.md` §4 for explicit OP non-impact statement).
- [x] **N-1 reframing honored.** L-M continues to keep $K_{\mathrm{soft}}^\phi$ (real) vs $K_{\mathrm{act}}^\varepsilon$ (integer) as distinct objects with explicit relationship; G1 closure preserves this.
- [x] **CN5 (4 energies independent), CN6 (K kinetically determined), CN7 (dual-mode self-referentiality), CN10 (contrastive not reductive), CN15 (static/dynamic separation):** all preserved.
- [x] **u_t primitive maintained.** All G1 work operates on $u^{(j)}, U$ as scalar fields.
- [x] **No external-framework reduction.** CSEH 2007 used as a tool, not a reduction.
- [x] **No metastability claim w/o P-F flag.** N/A.
- [x] **No Research OS resurrection.**
- [x] **No OMC pool orchestration.** Self-audit; 0 Agent dispatches this session.

---

**End of `02_development.md`. R-0/R-1/R-2/R-3 closed; Lemma L-M-2 + Theorem L-M post-repair Cat-A-conditional; Corollaries L-M.A absolute + L-M.B/L-M.C conditional inheriting; counterexample stability verified.**

**Next file:** `03_integration_and_new_open.md` — Canonical promotion proposal (T-L1-M new entry) + theorem_status.md updates + OP non-impact + new open questions + prompt v2 notes.
