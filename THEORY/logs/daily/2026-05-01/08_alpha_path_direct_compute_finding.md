# 08_alpha_path_direct_compute_finding.md — α-Path Direct Compute (W5 Day 5 Supplementary)

**Session:** 2026-05-01 (W5 Day 5 EOD — supplementary work after primary 8 outputs delivered)
**Block:** Supplementary (post-Block 5 close, executed at user direction "keep going")
**Target:** Pre-execute the α-path direct compute script (`nq187b_a2_a1_extrapolation.py` per `working/SF/nq187b_L_extrapolation.md` §6.1 spec) so W6 D1 has the α-path numerical anchor available without first-day script-creation overhead. **Validate post-EOD op-0008-architect's §2.6 closed-form table.**
**This file covers:** script creation + validation run + finding (post-EOD table contains a closed-form computational error; the correct ratio is L-independent 2/3 exactly).
**Depends on reading:** `working/SF/nq187b_L_extrapolation.md` §2 + §3 + §6.1, `03_t_sigma_theorem4_reconciliation.md` §3.3 (α-path original assignment).

---

## §1. What was done today

1. Created `CODE/scripts/nq187b_a2_a1_extrapolation.py` per `nq187b_L_extrapolation.md` §6.1 spec.
2. Executed: `cd CODE && python3 scripts/nq187b_a2_a1_extrapolation.py`.
3. Saved output: `CODE/scripts/results/nq187b_a2_a1_extrapolation.json`.
4. Cross-checked numerical output against `nq187b_L_extrapolation.md` §2.6 closed-form table.

**Status**: 🔴 **DISCREPANCY FOUND** — post-EOD `nq187b_L_extrapolation.md` §2.6 table is computationally incorrect.

---

## §2. Numerical Run Result

```
NQ-187b: discrete-grid A_2/A_1 evaluation
Convention: C1 (naive, no L^2-normalization)
L scan: [4, 8, 16, 32, 64, 128]

    L |          A_1^L |          A_2^L |    A_2/A_1
-------------------------------------------------------
    4 |         6.0000 |         4.0000 |   0.666667
    8 |        24.0000 |        16.0000 |   0.666667
   16 |        96.0000 |        64.0000 |   0.666667
   32 |       384.0000 |       256.0000 |   0.666667
   64 |      1536.0000 |      1024.0000 |   0.666667
  128 |      6144.0000 |      4096.0000 |   0.666667

Extrapolation r(L) = a + b/L^2 (linear fit on 1/L^2):
  a (L=infty) = 0.666667
  b (slope)   = 0.000000
  residual L2 = 1.11e-16
```

The ratio is **identically 2/3 at every L ∈ {4, 8, 16, 32, 64, 128}** with machine-precision residual ~10⁻¹⁶. No finite-size correction; no extrapolation needed (b ≈ 0).

---

## §3. Discrepancy with `nq187b_L_extrapolation.md` §2.6

The post-EOD op-0008-architect file claims (§2.5 + §2.6 tabulation):

| L | (claimed) sum cos² | (claimed) sum cos⁴ | (claimed) A_2/A_1 |
|---|---:|---:|---:|
| 4 | 2.0 | **1.25** ❌ | **0.80** ❌ |
| 8 | 4.0 | **2.625** ❌ | **0.762** ❌ |
| 16 | 8.0 | **5.6875** ❌ | **0.703** ❌ |
| 32 | 16.0 | **11.96875** ❌ | **0.668** ❌ |
| 64 | 32.0 | **24.2734375** ❌ | **0.659** ❌ |
| ∞ | — | — | 2/3 ≈ 0.667 (claimed asymptotic) |

The actual closed-form values (verified by direct numpy execution of the eigenmode formulas in §2.1 of the same file) are:

| L | sum cos² | sum cos⁴ | A_2/A_1 |
|---|---:|---:|---:|
| 4 | 2.0 ✓ | **1.5** | **2/3 = 0.6667** |
| 8 | 4.0 ✓ | **3.0** | **2/3** |
| 16 | 8.0 ✓ | **6.0** | **2/3** |
| 32 | 16.0 ✓ | **12.0** | **2/3** |
| 64 | 32.0 ✓ | **24.0** | **2/3** |
| 128 | 64.0 ✓ | **48.0** | **2/3** |

The cos² sums match (the post-EOD §2.5 closed-form $L/2$ identity is correct). The **cos⁴ sums are systematically low by an L-dependent amount** in the post-EOD table.

### §3.1 Closed-form proof of the discrepancy (correct derivation)

Using $\cos^4\theta = (3 + 4\cos 2\theta + \cos 4\theta)/8$:

$$\sum_{i=0}^{L-1} \cos^4\!\left(\frac{(i+1/2)\pi}{L}\right) = \frac{3L}{8} + \frac{1}{2}\sum_i \cos\!\left(\frac{(2i+1)\pi}{L}\right) + \frac{1}{8}\sum_i \cos\!\left(\frac{(4i+2)\pi}{L}\right).$$

Both auxiliary sums are zero for $L \geq 3$ (geometric series argument: $\sum_i e^{i(4i\pi/L)} = (e^{i 4\pi} - 1)/(e^{i 4\pi/L} - 1) = 0/(\cdot) = 0$ when $e^{i 4\pi/L} \neq 1$, which holds for $L \geq 3$ and $L \neq 4$). For the special case $L = 4$, direct computation gives the same $3L/8 = 1.5$ value. So:

$$\sum_i \cos^4 = \frac{3L}{8} \quad \text{exactly for all } L \geq 2.$$

Therefore $A_1^L = L \cdot (3L/8) = 3L^2/8$ and $A_2^L = (L/2)^2 = L^2/4$, giving:

$$\frac{A_2^L}{A_1^L} = \frac{L^2/4}{3L^2/8} = \frac{2}{3} \quad \text{exactly for all } L \geq 2.$$

**No finite-L correction at any L ≥ 2.** The §2.6 table's L-dependent values (0.80, 0.762, 0.703, 0.668, 0.659) are computational artifacts — possibly from a different angle convention used in op-0008-architect's hand-computation, but **not** reproducing the eigenmode formula stated in §2.1 of the same file.

### §3.2 Hand-check at L = 4

Angles $(i + 1/2)\pi/4$ for $i = 0, 1, 2, 3$: $\pi/8, 3\pi/8, 5\pi/8, 7\pi/8$.

- $\cos(\pi/8) \approx 0.9239$, $\cos^4 \approx 0.7286$.
- $\cos(3\pi/8) \approx 0.3827$, $\cos^4 \approx 0.0214$.
- $\cos(5\pi/8) = -\cos(3\pi/8) \approx -0.3827$, $\cos^4 \approx 0.0214$.
- $\cos(7\pi/8) = -\cos(\pi/8) \approx -0.9239$, $\cos^4 \approx 0.7286$.

Sum = $0.7286 + 0.0214 + 0.0214 + 0.7286 = 1.5 = 3 \cdot 4 / 8$. ✓ matches my numerical script.

The post-EOD §2.5 tabulation of "L=4: sum cos⁴ = 1.25" is **arithmetically incorrect**; the correct value is 1.5.

---

## §4. Implications for T-σ-Theorem-4 Reconciliation Triple

### §4.1 α-path verdict updated

The α-path *was* "finite-L vs continuum extrapolation audit" in `03_t_sigma_theorem4_reconciliation.md` §3.3 (third priority, confirmatory rather than causal).

**Updated α-path verdict (Day 5 supplementary)**: under naive convention C1, $A_2/A_1 = 2/3$ **identically at every $L \geq 2$**. There is no extrapolation problem; there is no "finite-L correction" to wait for. α-path is **closed Cat A** at the elementary trigonometric algebra level.

α-path is no longer a "third priority confirmation lane"; it is **Cat A definitive evidence** that R22's claim $A_2/A_1 = 4$ is incompatible with naive convention C1 — *at every finite L*, not just in some asymptotic limit.

### §4.2 β-path priority elevated

`03_*` §3.4 originally placed β-path at second priority because:
> "β-path has more pre-existing evidence than γ-path (the 2/3 closed-form is concrete). However, β-path requires re-deriving the entire R22 cubic-equivariant computation from first principles..."

With α-path now Cat A definitively *L-independent* 2/3 (not just an asymptotic), β-path's *prima facie* evidence against R22 is **even stronger**:

- R22's 4 cannot be a continuum-only feature with finite-L correction (no correction exists).
- R22's 4 must come from a *different convention* (C2/C3/C4 per `nq187b_L_extrapolation.md` §3.2) OR from a derivation error.
- β-path audit (`r22_a2_a1_audit.md` NEW W6 D4-W7) must identify which convention R22 uses, not whether finite-L corrections matter.

**Updated priority ordering** (revised from `03_*` §3.4):
- 🥇 **γ-path** (Σ_m-Hessian convention) — **still first**. Reason: γ explains the $\mu_0$ factor mismatch (canonical $4|W''(c)|\epsilon$ vs numerical $\epsilon|W''(c)|$). α-path closure does not address this.
- 🥈 **β-path** — priority raised to *parallel-with-γ* (vs original conditional-on-γ-inconclusive). The 2/3 ≠ 4 mismatch is *structural*, not asymptotic. β-path can run W6 D2 immediately rather than D4-W7 conditionally.
- 🥉 **α-path** — **closed Cat A today** under naive convention C1; remaining α-path work is alternative conventions C2/C3/C4 evaluation (different question; can be folded into β-path).

### §4.3 γ-path interpretation unchanged

γ-path scope (Σ_m-Hessian convention, factor 4 in $\mu_0$) is *separate* from the A_2/A_1 ratio question. γ-path explains the $\mu_0$ value; β-path explains the $A_2/A_1$ ratio. They are two independent audit lanes that happen to both bear on T-σ-Theorem-4.

If γ-path finds canonical $\mu_0 = 4|W''(c)|\epsilon$ is correct under one convention but $\mu_0 = \epsilon|W''(c)|$ under another → γ closes; T-σ-Theorem-4 (ii) factor of 4 in the $\mu_0$ formula explained.

If β-path finds R22's $A_2/A_1 = 4$ derivation actually uses convention C3 (mass-conservation simplex projection) where the ratio is genuinely 4 → β closes; T-σ-Theorem-4 (ii) factor in the $\mu_1$ formula explained as convention-specific.

Both audits can close *independently*; their findings combine to determine T-σ-Theorem-4 (ii) final canonical statement.

---

## §5. Errata Recommendation for `working/SF/nq187b_L_extrapolation.md`

Recommended W6 D1 morning errata (NOT applied today; preserves Day 5 anti-drift "no edits to working/ files outside the daily/2026-05-01/ scope"):

### §5.1 §2.5 closed-form table correction

Replace:
> "For $L \in \{4, 8, 16, 32, 64\}$: explicit computation gives:
>
> | L | sum cos² | sum cos⁴ |
> | 4 | 2.0 | 1.25 |
> | 8 | 4.0 | 2.625 |
> | 16 | 8.0 | 5.6875 |
> | 32 | 16.0 | 11.96875 |
> | 64 | 32.0 | 24.2734375 |"

With:
> "For $L \geq 2$: by trigonometric identity $\cos^4\theta = (3 + 4\cos 2\theta + \cos 4\theta)/8$ + geometric-series argument for shifted-half phase $(i+1/2)\pi/L$, both auxiliary sums vanish at $L \geq 3$ (and $L = 4$ special case computes to the same value). Therefore:
> $$\sum_i \cos^2\!\big((i+1/2)\pi/L\big) = L/2, \qquad \sum_i \cos^4\!\big((i+1/2)\pi/L\big) = 3L/8 \quad \text{exactly}.$$
> Numerical confirmation across $L \in \{4, 8, 16, 32, 64, 128\}$ via `CODE/scripts/nq187b_a2_a1_extrapolation.py` (`results/nq187b_a2_a1_extrapolation.json`)."

### §5.2 §2.6 discrete ratio table correction

Replace L-dependent table with:
> $A_2^L / A_1^L = (L^2/4)/(3L^2/8) = 2/3$ **identically** at every $L \geq 2$. No finite-L correction. (Verified numerically `CODE/scripts/results/nq187b_a2_a1_extrapolation.json`: $a = 0.666667$, $b = 0.000000$, residual L² = $1.1 \times 10^{-16}$.)"

### §5.3 §5 prediction table correction

The "α-naive: $\mu_1/\mu_0 \to 1/6$ as $L \to \infty$" prediction in §5.1 was based on the assumption of L-dependent extrapolation. With L-independent ratio, the prediction simplifies:
- α-naive: $\mu_1/\mu_0 = (A_2/A_1)/4 = (2/3)/4 = 1/6$ at *every* L (under canonical $\mu_0 = 4|W''(c)|\epsilon$ formula + naive A_2/A_1 = 2/3).
- NQ-187 numerical $\mu_1/\mu_0 = 2$ at L=16 → **incompatible** with α-naive at *any* L.

So if α-naive C1 convention is the correct convention, NQ-187 numerical extension to L=32, L=64 should *still* show $\mu_1/\mu_0 = 1/6$, not converge from 2 toward something else. If NQ-187 numerical at L=32, 64 stays at 2, then naive C1 convention is **rejected** as the operative convention — β-path must identify which convention NQ-187 numerical actually used.

### §5.4 §6.1 + §6.2 numerical script update

Note that `nq187b_a2_a1_extrapolation.py` (Day 5 supplementary) already executes correctly. The §6.2 NQ-187 extension to L=32, 64 (Lanczos eigenvalue extraction) remains W6 D4-W7 work — the script for *that* (`nq187b_mu_extrapolation.py`) does not yet exist.

---

## §6. Day 5 Reconciliation Discipline Compliance

This Day 5 supplementary work was authorized by user "keep going" directive after primary 8 daily outputs were complete.

- [x] **canonical 직접 수정 0** — `08_*` is daily log; canonical.md untouched.
- [x] **No silent OP resolution** — α-path Cat A finding does NOT resolve T-σ-Theorem-4 (Cat B retained per `03_*` §2); does NOT close OP-0009 sub-items; does NOT close OP-0008/0005.
- [x] **Errata recommendation, not edit** — `nq187b_L_extrapolation.md` corrections drafted in §5 of this file as W6 D1 morning errata, not applied today.
- [x] **u_t primitive maintained** — N/A (closed-form algebra on eigenmodes).
- [x] **CN5 4-energy not merged** — N/A.
- [x] **K not dual-treated** — N/A.
- [x] **CN10 contrastive** — closed-form trigonometric algebra is standard; numerical confirmation via numpy is internal verification, not external reduction.
- [x] **No Research OS resurrection** — single-topic note.
- [x] **No metastability claim without P-F flag** — N/A.
- [x] **Anti-drift preserved** — α-path direct compute was named in `03_*` §3.3 + `07_*` §2.1 W6 D1 PM action item; Day 5 supplementary execution accelerates W6 D1 by 1 hour, does not introduce new scope. Identifying the post-EOD §2.6 error is honest reconciliation work, not "expansion".

---

## §7. Updated W6 D1 Morning Sequence (per Day 5 Supplementary Finding)

Revised from `07_w6_plan_preview.md` §2.1 + `TASK_LEDGER.md` "W6 D1 morning immediate actions":

1. ✅ **α-path direct compute script + run** — DONE Day 5 supplementary (this file).
2. **Apply errata** to `working/SF/nq187b_L_extrapolation.md` per §5 above (~15min). — NEW W6 D1 morning task.
3. **Spawn `gamma-path-prover` teammate** — unchanged; γ-path is independent of α-path closure.
4. **β-path priority elevated**: spawn `r22-audit-prover` teammate **W6 D1-D2** (was conditional on γ inconclusive D1-D3; now unconditional given α evidence is structural). NEW priority.
5. NQ-242 PH Phase 1 setup — unchanged.
6. omc-team window 1:1 capture — unchanged.
7. OAT-2 F bridge integration — unchanged.

Net W6 D1 entry: γ + β both unconditional; α closed; T-σ-Theorem-4 reconciliation triple becomes a *parallel γ + β* with α as supporting evidence.

---

## §8. Files Changed Today (Day 5 Supplementary)

- ✅ NEW: `CODE/scripts/nq187b_a2_a1_extrapolation.py` (124 lines).
- ✅ NEW: `CODE/scripts/results/nq187b_a2_a1_extrapolation.json` (machine-readable result; ~2KB).
- ✅ NEW: `THEORY/logs/daily/2026-05-01/08_alpha_path_direct_compute_finding.md` (this file).
- ⚪ Existing `working/SF/nq187b_L_extrapolation.md` (422 lines) — errata recommended in §5; **NOT applied today** (W6 D1 morning task).
- ⚪ Existing `THEORY/logs/daily/2026-05-01/03_t_sigma_theorem4_reconciliation.md` — §3.3/§3.4 priority ordering recommendation in §4 of this file; **NOT applied** (the original is preserved as Day 5 reconciliation note; revisions go in this `08_*` file).
- ⚪ Existing `THEORY/logs/daily/2026-05-01/07_w6_plan_preview.md` — W6 D1 morning sequence revised in §7 of this file; **NOT applied** (the plan preview is preserved; W6 D1 morning lead applies revisions).

---

**End of 08_alpha_path_direct_compute_finding.md.**

**Status:** α-path direct compute executed successfully. Closed-form result $A_2/A_1 = 2/3$ identically at every $L \geq 2$ (no finite-size correction). Post-EOD `nq187b_L_extrapolation.md` §2.6 table is computationally incorrect (correct values: sum cos⁴ = $3L/8$ exactly, ratio = 2/3 exactly at every L). β-path priority elevated from conditional to unconditional W6 D1-D2 dispatch. T-σ-Theorem-4 reconciliation triple becomes parallel γ + β with α closed Cat A as supporting evidence. No canonical edits today; no working file edits outside `daily/2026-05-01/` scope; errata recommendations drafted as W6 D1 morning task. Honest reconciliation finding — exactly the kind of cross-check that justifies Day 5 supplementary work.
