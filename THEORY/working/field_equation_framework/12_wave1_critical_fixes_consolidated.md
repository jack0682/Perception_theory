---
type: working/field_equation_framework/consolidated-fix-specification
date: 2026-05-20
session_origin: W8-Day3, post-Wave-2-critic-review (07_critic_full_review.md)
canonical_version: CV-1.13 SEALED (0 edits — this file is a fix specification only)
status: authoritative fix reference for Wave 1 outputs (files 02-06)
source_critic: 07_critic_full_review.md (Wave 2 adversarial critic; 4 CRITICAL + 17 MAJOR + 23 MINOR)
files_under_review:
  - 02_kramers_prefactor_op_0005_attack.md (551L)
  - 03_modica_mortola_jacobi_cat_b.md (680L)
  - 04_h_morse_spectral_quantification.md (833L)
  - 05_cat_a_direct_catalog_proofs.md (955L)
  - 06_surface_tension_rescaling_cat_a.md (479L)
constraint_compliance:
  canonical_edits: 0
  files_02_to_06_edits: 0 (fix specification only — do NOT edit wave-1 files directly)
  Mori_Zwanzig: 0
  inertia: 0
  new_energy_terms: 0
  CSSL_patterns: 0
purpose: |
  Single reference document consolidating all 4 CRITICAL + 8 priority MAJOR fixes
  from Wave 2 critic review. Provides corrected derivations, exact fix specifications,
  and cross-file consistency mandates. Serves as the Wave 1 → W9+ promotion gate.
---

> [!nav] Linked: [[07_critic_full_review|07 Wave-2 critic review]] · [[02_kramers_prefactor_op_0005_attack|02 Kramers]] · [[03_modica_mortola_jacobi_cat_b|03 Modica-Mortola]] · [[04_h_morse_spectral_quantification|04 H-Morse spectral]] · [[05_cat_a_direct_catalog_proofs|05 Cat A catalog]] · [[06_surface_tension_rescaling_cat_a|06 Surface tension rescaling]] · [[../../canonical/theorem_status|theorem_status.md]] · [[../../canonical/canonical|CV-1.13 canonical]]

# 12 — Wave 1 Critical Fixes Consolidated (W8-Day3 Post-Critic Gate)

**Purpose**: This document is the *authoritative fix specification* for Wave 1 outputs (files 02-06), produced after Wave 2 adversarial critic review (`07_critic_full_review.md`). It consolidates 4 CRITICAL findings + 8 priority MAJOR findings into corrected derivations and exact replacement text. Files 02-06 are NOT edited directly — this document is the *fix gate* that any W9+ session reads before referencing Wave 1 material.

**Do NOT modify canonical/* files.** Do NOT modify files 02-06. This document is the specification only.

---

## §0 — Frontmatter: Fix Count Summary

| Category | Count | Source sections |
|---|---|---|
| **CRITICAL fixes** | **4** | §2-§5 below |
| **MAJOR fixes** | **8** | §6 below |
| Cross-file consistency mandates | 4 | §7 |
| W9+ promotion gate decisions | 5 files | §8 |
| CN1-16 check | 16/16 ✓ | §9 |

**Critic source**: `07_critic_full_review.md` §A-§H (adversarial mode, 4 CRITICAL + 17 MAJOR final count).

**Origin of failures**: Parallel ultrawork generation (5 simultaneous agents) prevented natural cross-checking. The σ-formula divergence between files is the textbook multi-agent consistency failure; the L1967 miscitation repeats the exact CSSL §A.1 failure mode.

---

## §1 — Mission: Consolidate Wave 2 Critic Fixes

The Wave 2 critic found **4 CRITICAL** findings across files 02-06:

1. **σ formula divergence** (files 05, 06 wrong; file 03 correct): factor-√2 error on the defining surface tension constant, propagating through 7+ derived quantities.
2. **File 03 L1967 systematic miscitation** (9 instances): OP-HMORSE-SADDLE cited as "canonical L1967" when the canonical *registration* is `theorem_status.md` L594. This is the exact CSSL §A.1 failure mode repeating.
3. **File 06 §8.1 prefactor invariance claim FALSE** (cross-file): Kramers prefactor claimed invariant under (α,β)→(sα,sβ) rescaling — algebraically wrong; prefactor scales linearly as s.
4. **Files 02/05 Identity 2 algebraic equivalence wrong** (§5.1 of file 02, §4.5 of file 05): `ω_well·ω_saddle·(Pr^{(Kramers)})^{-1/2}` equated to `√(μ_well·|μ_saddle|)` — these are different quantities and must not be equated.

Each CRITICAL finding gets a full section below (§2-§5) with:
- Issue summary
- Corrected derivation (full algebra shown)
- Affected lemmas/locations with corrected forms
- Verification check

---

## §2 — CRITICAL Fix #1: σ Formula Consensus (Files 05, 06 WRONG; File 03 CORRECT)

### §2.1 Issue

The Modica-Mortola surface tension constant `σ` for `W(u) = u²(1-u)²` is stated inconsistently across Wave 1:

| File | σ formula | Numerical (α=β=1) | Status |
|---|---|---|---|
| File 03 §2.2 + §13 | `σ = (√2/6)·√(αβ)` | 0.2357 | **CORRECT** |
| File 05 §2 (L112-114) | `σ = √(αβ)/3` | 0.3333 | **WRONG** (off by factor √2) |
| File 06 §2 (L100) + §3 Proof (c) (L148) | `σ = √(αβ)/3` | 0.3333 | **WRONG** (off by factor √2) |

The discrepancy is 41% on a *defining constant* of the framework. File 05's own derivation is internally inconsistent: it writes `σ = (√(αβ)/3) · ∫₀¹ 2W(u)^{1/2} du` and then claims the integral equals 1 (so that `σ = √(αβ)/3`), but the integral `∫₀¹ 2u(1-u) du = 1/3`, giving `σ = (√(αβ)/3)·(1/3) = √(αβ)/9` — a threefold internal contradiction.

File 06's error is in the numerical prefactor only; the scaling property `σ → s·σ` under (α,β)→(sα,sβ) is correct regardless of which prefactor is used, so file 06's *main theorem* (L-SURFACE-TENSION-RESCALE) is structurally sound. But the numerical reference values in file 06 are wrong by factor √2.

### §2.2 Correct Derivation (full, step by step)

The canonical Modica-Mortola surface tension for the boundary energy `E_bd = α·uᵀLu + β·ΣW(uᵢ)` with `W(u) = u²(1-u)²` is:

```
σ = √(αβ) · ∫₀¹ √(2W(s)) ds

Step 1: Compute √(2W(s)).
  W(s) = s²(1-s)²
  2W(s) = 2s²(1-s)²
  √(2W(s)) = √2 · s(1-s)    [since s(1-s) ≥ 0 for s ∈ [0,1]]

Step 2: Integrate.
  ∫₀¹ √(2W(s)) ds = √2 · ∫₀¹ s(1-s) ds
                   = √2 · ∫₀¹ (s - s²) ds
                   = √2 · [s²/2 - s³/3]₀¹
                   = √2 · (1/2 - 1/3)
                   = √2 · (1/6)
                   = √2/6

Step 3: Multiply by √(αβ).
  σ = √(αβ) · (√2/6) = (√2/6) · √(αβ)

Numerical check:
  √2/6 = 1.41421.../6 = 0.23570...
  At α=β=1: σ = 0.23570
```

**CORRECT VALUE:**

$$\boxed{\sigma = \frac{\sqrt{2}}{6} \cdot \sqrt{\alpha\beta} \approx 0.2357 \cdot \sqrt{\alpha\beta}}$$

**Why file 05 is wrong:** File 05 writes `∫₀¹ 2W^{1/2} du` (note: `2W^{1/2}`, NOT `√(2W)`). These differ:
- `√(2W) = √2 · u(1-u)` → integral = `√2/6 ≈ 0.2357`
- `2W^{1/2} = 2u(1-u)` → integral = `2·(1/6) = 1/3 ≈ 0.333`

The ratio is exactly `√2`. File 05 uses the non-standard `∫ 2W^{1/2}` convention (sometimes seen in `2·∫√W` forms), which gives σ = `(1/3)·√(αβ)`. The standard Modica-Mortola convention is `∫ √(2W)`, giving the correct `(√2/6)·√(αβ)`. File 03 uses the standard convention correctly.

**Python verification** (run by Wave 2 critic):
```python
import numpy as np
from scipy.integrate import quad
def integrand(s): return np.sqrt(2 * s**2 * (1-s)**2)
result, _ = quad(integrand, 0, 1)
# result = 0.23570226039551584
# np.sqrt(2)/6 = 0.23570226039551587 ✓
```

### §2.3 Affected Derivations: Corrected Forms

All downstream quantities in files 05 and 06 that use `σ = √(αβ)/3` must be corrected to use `σ = (√2/6)·√(αβ)`. The scaling relation `σ → s·σ` under (α,β)→(sα,sβ) is unchanged (homogeneity degree 1 in √(αβ) is the same); only the numerical prefactor changes.

**Correction factor**: multiply all σ-derived quantities by `(√2/6)/(1/3) = (√2/6)·3 = √2/2 ≈ 0.707` wherever `√(αβ)/3` was used. Equivalently, divide by √2.

**Affected lemmas in file 05** (use `c_W := √2/6`):

| Lemma | Old form (WRONG) | Corrected form |
|---|---|---|
| **L-CAPILLARY-DEF** (§3.3) | `Ca = |∇E|/σ = 3|∇E|` at α=β=1 | `Ca = |∇E|/σ = (6/√2)|∇E| ≈ 4.243·|∇E|` |
| **L-BOND-DEF** (§3.4) | `Bo = R²|∇E|/σ = 48·|∇E|` at R=4, α=β=1 | `Bo = R²·(6/√2)·|∇E| ≈ 67.88·|∇E|` at R=4 |
| **L-LEWIS-DEF** (Le_SCC) | uses σ in denominator — rescale by √2 | corrected: multiply Le_SCC by √2 wherever σ appears in denominator |
| **T-IDENTITY-LEWIS-ANALOG** (§4.3) | any reference value at α=β=1 using σ=1/3 | replace 1/3 → √2/6 ≈ 0.2357 |
| **Reference table §6** | σ = 1/3 at α=β=1 | σ = √2/6 ≈ 0.2357 at α=β=1 |

**Affected lemma in file 06**:

| Lemma | Old form (WRONG) | Corrected form |
|---|---|---|
| **L-SURFACE-TENSION-RESCALE §2 (c) statement** | `σ(α,β) = √(αβ)/3` | `σ(α,β) = (√2/6)·√(αβ)` |
| **Proof of (c)** (L148) | `σ(sα,sβ) = √((sα)(sβ))/3 = s·√(αβ)/3` | `σ(sα,sβ) = (√2/6)·√((sα)(sβ)) = s·(√2/6)·√(αβ)` |
| **Reference values §7** | σ = √5/3 at α=1,β=5 | σ = (√2/6)·√5 = √10/6 ≈ 0.527 at α=1,β=5 |

**Important**: the *structural conclusion* of file 06 (parts a-f of L-SURFACE-TENSION-RESCALE) is **unaffected** — the scaling law `σ → s·σ` holds for any formula `c·√(αβ)`. Only the numerical prefactor changes. File 06's main theorem survives CRITICAL Fix #1 intact.

**Affected lemma in file 03**: File 03 §8.1 and §9 use the *correct* formula `σ = (√2/6)·√(αβ)` throughout, so the spectral gap bound:

```
μ_min ≥ σ · μ_2(J_Γ) = (√2/6)·√(αβ) · (d+1)/R²
```

is correct as stated in file 03. No change needed to file 03 for CRITICAL Fix #1.

### §2.4 Verification

After applying corrections: all three files (03, 05, 06) must agree that:
- At α=β=1: σ = √2/6 ≈ 0.2357 (NOT 1/3 ≈ 0.333)
- At α=1, β=5: σ = √10/6 ≈ 0.527 (NOT √5/3 ≈ 0.745)
- Ca at α=β=1 with |∇E|=1: Ca = 6/√2 ≈ 4.243 (NOT 3.0)
- Bo at α=β=1, R=4, |∇E|=1: Bo ≈ 67.88 (NOT 48.0)

---

## §3 — CRITICAL Fix #2: File 03 L1967 → theorem_status.md L594 (9 Instances)

### §3.1 Issue

File 03 (`03_modica_mortola_jacobi_cat_b.md`) cites OP-HMORSE-SADDLE as `"(canonical L1967, OPEN)"` or `"OP-HMORSE-SADDLE L1967"` at **9 locations**. This is the same failure mode as CSSL §A.1.

What canonical.md L1967 actually contains (verified):
```
"- Does NOT prove saddle-point Hessian regularity (OP-HMORSE-SADDLE, separate OP)."
```

This is a **non-overclaim caveat** inside the body of `L-HMORSE-LOCAL`, referencing OP-HMORSE-SADDLE. It is NOT the registration of OP-HMORSE-SADDLE. Following "L1967" leads a reader to a parenthetical caveat, not to the OP definition or statement.

**The actual canonical registration** of OP-HMORSE-SADDLE is `theorem_status.md` L594:
```
| OP-HMORSE-SADDLE | Saddle-point Hessian regularity | Medium | OPEN (NEW CV-1.16): required 
  for full Eyring-Kramers prefactor Cat B; independent of OP-HMORSE-LOCAL-A. ETA 2–4 sessions. |
```

Secondary mention: `theorem_status.md` L435 (the "Did NOT close" caveat, a valid cross-reference).
Third mention: `canonical.md` L1967 (the non-overclaim caveat, NOT the registration).

File 02 cites OP-HMORSE-SADDLE correctly (theorem_status.md L435 / L594). File 03 fails to reference theorem_status.md at all for this OP.

### §3.2 Affected Locations in File 03

All 9 instances (verified by critic via grep):

| Line | Current (WRONG) text | Required correction |
|---|---|---|
| 67 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 85 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 91 | `OP-HMORSE-SADDLE L1967` | See replacement text §3.3 |
| 376 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 505 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 541 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 543 | `"OP-HMORSE-SADDLE statement" = L1967 caveat text` | Special — see §3.4 |
| 560 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |
| 614 | `OP-HMORSE-SADDLE (canonical L1967, OPEN)` | See replacement text §3.3 |

### §3.3 Standard Replacement Text (8 of 9 instances)

**WRONG:**
```
OP-HMORSE-SADDLE (canonical L1967, OPEN)
```

**CORRECT (standard form):**
```
OP-HMORSE-SADDLE (theorem_status.md L594, OPEN)
```

**CORRECT (dual-citation form, preferred for clarity):**
```
OP-HMORSE-SADDLE (registration: theorem_status.md L594; cross-ref: canonical.md L1967
  non-overclaim caveat within L-HMORSE-LOCAL body)
```

The dual-citation form is preferred because it explains *why* L1967 appears: it is a non-overclaim caveat that mentions the OP by name, but the OP's actual content and status are at theorem_status.md L594.

### §3.4 Special Case: Line 543

File 03 §10.1 line 543 currently reads something like:
```
OP-HMORSE-SADDLE (OPEN, canonical L-HMORSE-LOCAL caveat L1967): 
"Does NOT prove saddle-point Hessian regularity (OP-HMORSE-SADDLE, separate OP)."
```
and treats this caveat text as the "statement of OP-HMORSE-SADDLE."

**This is a misdescription.** The caveat text is the non-overclaim caveat of L-HMORSE-LOCAL, not the OP statement. The OP statement is at theorem_status.md L594.

**Required correction at line 543:**
```
OP-HMORSE-SADDLE (registration: theorem_status.md L594, OPEN):
"Saddle-point Hessian regularity — required for full Eyring-Kramers prefactor Cat B; 
independent of OP-HMORSE-LOCAL-A. ETA 2–4 sessions."
[Note: canonical.md L1967 contains a non-overclaim caveat within L-HMORSE-LOCAL that 
references this OP by name ("Does NOT prove saddle-point Hessian regularity (OP-HMORSE-
SADDLE, separate OP)"), but that caveat is NOT the OP statement.]
```

### §3.5 Why This Is CRITICAL (Not Just MINOR)

This is the **exact same failure mode** CSSL §A.1 identified: treating a *non-overclaim caveat* that mentions an OP as if it were the OP's registration location. A reader following the L1967 citation cannot find the OP definition, its status, its ETA, or its relationship to other OPs — all of which are at theorem_status.md L594. The failure pattern must not repeat in W9+.

**Mandatory W9+ rule (from §7.3 below):** Every citation of a canonical OPEN problem must cite `theorem_status.md` (the OP registration source), not merely `canonical.md` (which may contain cross-references but not the primary OP record).

---

## §4 — CRITICAL Fix #3: File 06 §8.1 Prefactor Invariance Claim — RETRACTION REQUIRED

### §4.1 Issue

File 06 §8.1 (lines 327-335, approximately) contains:

> "ω_0(s) ~ (s·ω_well·ω_saddle)/(s·√Pr^{(Kramers)}) = ω_well·ω_saddle/√Pr^{(Kramers)} = ω_0(1)"

This claims the Kramers prefactor `ω_0` is **invariant** under (α,β) → (sα,sβ) rescaling.

This claim is **FALSE**. The proof contains an algebraic error: it asserts `Pr^{(Kramers)} = μ_well·μ_saddle → s²·Pr^{(Kramers)}` — treating Pr^{(Kramers)} as a product. But Pr^{(Kramers)} is defined as a **ratio**: `Pr^{(Kramers)} = |μ_well|/|μ_saddle|`. The ratio scales as `(s·|μ_well|)/(s·|μ_saddle|) = |μ_well|/|μ_saddle|` — **invariant under rescaling**, not s²-scaled.

Once the correct scaling of Pr is applied, the prefactor is NOT invariant.

### §4.2 Correct Derivation of Prefactor Scaling

Starting from the correct definitions:
- `ω_well = √|μ_well|` → under rescaling: `ω_well(s) = √(s·|μ_well|) = √s · ω_well(1)`
- `ω_saddle = √|μ_saddle|` → under rescaling: `ω_saddle(s) = √s · ω_saddle(1)`
- `Pr^{(Kramers)} = |μ_well|/|μ_saddle|` → under rescaling: `Pr^{(Kramers)}(s) = (s|μ_well|)/(s|μ_saddle|) = Pr^{(Kramers)}(1)` (**invariant**)

Now compute the prefactor under the structural form `ω_0 ~ ω_well · ω_saddle / √Pr^{(Kramers)}`:

```
ω_0(s) ~ ω_well(s) · ω_saddle(s) / √(Pr^{(Kramers)}(s))
        = (√s · ω_well(1)) · (√s · ω_saddle(1)) / √(Pr^{(Kramers)}(1))
        = s · ω_well(1) · ω_saddle(1) / √(Pr^{(Kramers)}(1))
        = s · ω_0(1)
```

**CORRECT RESULT: `ω_0(s) = s · ω_0(1)`. The Kramers prefactor scales LINEARLY in s.**

Alternative derivation via the 1D-projection form:
```
ω_0^{1D-proj} = (1/2π)·√(μ_well · |μ_saddle|)
Under rescaling: (1/2π)·√(s·μ_well · s·|μ_saddle|) = (s/2π)·√(μ_well·|μ_saddle|) = s·ω_0^{1D-proj}(1)
```
Both derivation paths give `ω_0(s) = s · ω_0(1)`. ✓

### §4.3 Correct Statements for Rescaling Behavior of Kramers Rate

**What IS invariant under (α,β) → (sα,sβ):**
```
Pr^{(Kramers)}(s) = |μ_well(s)| / |μ_saddle(s)|
                  = s·|μ_well(1)| / (s·|μ_saddle(1)|)
                  = Pr^{(Kramers)}(1)           [INVARIANT ✓]
```

The Pr^{(Kramers)} ratio is the useful invariant structural feature — it characterizes the *shape* of the transition (well curvature vs saddle curvature) without reference to the overall energy scale.

**What scales with s:**
```
ω_well(s) = √s · ω_well(1)
ω_saddle(s) = √s · ω_saddle(1)
ω_0(s) = s · ω_0(1)                             [LINEAR in s]
ΔE(s) = s · ΔE(1)                               [barrier scales with s by linearity of E_bd]
```

**Full Kramers rate under rescaling:**
```
Γ(s) = ω_0(s) · exp(-ΔE(s)/T_*)
      = s·ω_0(1) · exp(-s·ΔE(1)/T_*)
```

Both the prefactor and the exponent acquire s-dependence. The rate is NOT simply scaled — the exponential suppression is enhanced as `s → ∞` (deeper wells relative to T_*, which is fixed as OMS-1 ξ resident).

### §4.4 Required Replacement for File 06 §8.1

**RETRACT** the current §8.1 claim "Kramers prefactor invariant under uniform rescaling."

**REPLACE WITH:**
```
§8.1 [CORRECTED] Kramers Rate Behavior Under Surface Tension Rescaling

Under (α,β) → (sα,sβ) with s > 0:
  
  (1) Pr^{(Kramers)} = |μ_well|/|μ_saddle| is INVARIANT (ratio of eigenvalues; 
      both scale by s so the ratio is unchanged). This is the useful structural 
      invariant: the shape ratio of well vs saddle curvature does not change under 
      uniform surface tension rescaling.
  
  (2) Kramers prefactor ω_0 scales LINEARLY: ω_0(s) = s · ω_0(1). 
      (Because ω_well·ω_saddle → s·ω_well·ω_saddle while √Pr is invariant.)
  
  (3) Barrier ΔE scales linearly: ΔE(s) = s · ΔE(1).
      (By linear homogeneity of E_bd in (α,β), part (d) of this lemma.)
  
  (4) Full Kramers rate: Γ(s) = s·ω_0(1) · exp(-s·ΔE(1)/T_*)
      Both prefactor AND exponent acquire s-dependence. The exponential suppression 
      INCREASES under rescaling (deeper barrier relative to fixed T_*).
  
  (5) The Pr^{(Kramers)} invariance (item 1) is the correct structural insight for 
      cross-file comparison. The prefactor itself is NOT invariant.
```

### §4.5 Impact on OP-0005-DYN Cross-File Analysis

The file 02 / file 06 cross-file claim that "Kramers prefactor is invariant under surface tension rescaling" (used as a structural reason to separate prefactor from exponent in OP-0005-DYN analysis) is incorrect. The correct statement for OP-0005-DYN analysis is: **Pr^{(Kramers)} is invariant** (the ratio), **ω_0 is not** (it scales as s). The useful separability is:

```
Γ(s) = s · ω_0(1) · exp(-s · ΔE(1)/T_*)
```

where `ω_0(1)` and `ΔE(1)` are evaluated at the baseline (α₀, β₀), and the full s-dependence is explicit. This is actually a richer structural result than the (false) invariance claim.

---

## §5 — CRITICAL Fix #4: Files 02/05 Identity 2 Algebraic Equivalence — SPLIT REQUIRED

### §5.1 Issue

File 02 §5.1 (boxed formula) and file 05 §4.5 (T-IDENTITY-KRAMERS-PREFACTOR-FORM) both equate two quantities that are algebraically distinct:

**Claimed (WRONG):**
```
ω_well · ω_saddle · (Pr^{(Kramers)})^{-1/2}  =  √(μ_well · |μ_saddle|)
```

**Algebraic check** (critic §A.3, verified):
```
Left side:  ω_well · ω_saddle · (Pr)^{-1/2}
          = √|μ_well| · √|μ_saddle| · √(|μ_saddle|/|μ_well|)     [since Pr = |μ_well|/|μ_saddle|]
          = √|μ_saddle| · √|μ_saddle|
          = |μ_saddle|

Right side: √(μ_well · |μ_saddle|)
          = √|μ_well| · √|μ_saddle|
          = ω_well · ω_saddle

These are DIFFERENT:
  Left  = |μ_saddle|
  Right = √(μ_well · |μ_saddle|) = ω_well · ω_saddle
```

They are equal ONLY when `|μ_well| = |μ_saddle|`, i.e., Pr^{(Kramers)} = 1. In the SCC formation regime these are generically unequal.

Additionally, file 02 §5.1 appends an extra `·ω_well^{1/2}` factor in one version, making the right side `|μ_saddle|·|μ_well|^{1/4}/(2π)` — which is dimensionally inconsistent with the left side `√(μ_well·|μ_saddle|)/(2π)`.

### §5.2 Resolution: Split Into Two Distinct Identities

**Identity 2a — Structural Kramers Prefactor Form** (multi-D leading-order):

$$\boxed{\omega_0 \;\sim\; \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} \cdot (Pr^{(Kramers)})^{-1/2} = |\mu_{\mathrm{saddle}}|}$$

where the equality holds by the algebra above: `√|μ_well|·√|μ_saddle|·√(|μ_saddle|/|μ_well|) = |μ_saddle|`.

**Interpretation of Identity 2a:** The leading-order Kramers prefactor scales as `|μ_saddle|/(2π)` — proportional to the magnitude of the unstable eigenvalue at the saddle. This is the dominant factor in the HTB multi-D formula (file 02 §3.3):
```
ω_0^{multi-D} = (|μ_saddle|/(2π)) · √(|det' Hess(u_well)| / |det' Hess(u_saddle)|)
```
where the det'/det' ratio is the subleading correction.

**Identity 2b — 1D-Projection Geometric Mean Form:**

$$\boxed{\omega_0^{1D-proj} = \frac{1}{2\pi} \cdot \sqrt{\mu_{\mathrm{well}} \cdot |\mu_{\mathrm{saddle}}|} = \frac{1}{2\pi} \cdot \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}}}$$

**Interpretation of Identity 2b:** The 1D-projection (Kramers 1940 §VII, HTB 1990 eq. 4.55a) gives the geometric mean of well and saddle curvatures. This is the direct product `ω_well·ω_saddle = √(μ_well·|μ_saddle|)` with no Pr^{(Kramers)} ratio needed.

**Key difference:**
```
Identity 2a:  ω_0 ~ |μ_saddle|                            (proportional to saddle curvature alone)
Identity 2b:  ω_0 ~ √(μ_well · |μ_saddle|)               (geometric mean of both curvatures)
```

These are different physical quantities. In the SCC reference example (file 02 §6.4, μ_well ~ 10, |μ_saddle| ~ 30):
```
Identity 2a:  ω_0 ~ |μ_saddle| = 30
Identity 2b:  ω_0 = √(10·30)/(2π) = √300/(2π) ≈ 17.3/6.28 ≈ 2.76
```

The file 02 §6.4 numerical calculation uses Identity 2b (`≈ 2.76`) but cites it as "Identity 2" without distinguishing these two forms. This is the source of the confusion.

### §5.3 Required Replacements in Files 02 and 05

**File 02 §5.1 boxed formula**: Replace the single "Identity 2" with the two-identity split:

```
[CORRECTED §5.1]

Identity 2a (Structural / Leading-Order Form):
  ω_0^{multi-D} ~ ω_well · ω_saddle · (Pr^{Kramers})^{-1/2} = |μ_saddle|
  
  This follows from: ω_well·ω_saddle·(Pr)^{-1/2} = √|μ_well|·√|μ_saddle|·√(|μ_saddle|/|μ_well|)
                   = |μ_saddle| (exact algebra).
  It matches the leading factor |μ_saddle|/(2π) in the multi-D HTB formula (§3.3).

Identity 2b (1D-Projection / Geometric-Mean Form):
  ω_0^{1D-proj} = (1/2π) · √(μ_well · |μ_saddle|) = (1/2π) · ω_well · ω_saddle
  
  This is the Kramers 1940 §VII 1D form (also HTB 1990 eq. 4.55a). It does NOT
  involve Pr^{(Kramers)} — the Pr ratio drops out because both ω_well and ω_saddle
  appear directly. The numerical example §6.4 uses this form: √(10·30)/(2π) ≈ 2.76.

THESE ARE DIFFERENT. Identity 2a gives the structural insight (ω_0 ∝ |μ_saddle|);
Identity 2b gives the 1D-projection computation (ω_0 ∝ √(μ_well·|μ_saddle|)).
Do not equate them.
```

**File 05 §4.5 T-IDENTITY-KRAMERS-PREFACTOR-FORM**: Replace the single "Cat A form" with the two-identity split, using the same text above. The Cat A classification remains correct for *both* identities separately (each is direct algebra from the canonical Hessian spectral definitions). The previous single identity was not Cat A because it was wrong.

**File 02 §3.3 det consistency** (secondary MAJOR, now clarified): The multi-D formula at §3.3 uses `det` (full determinant) in the numerator and `det'` (product over non-zero eigenvalues) in the denominator. On translation-invariant graphs (T²₁₆), the well Hessian has Goldstone zeros, so `det Hess(u_well) = 0`. Both numerator and denominator must use `det'` (excluding Goldstone AND the single negative eigenvalue at the saddle). The §5.1 expanded product form `∏_{k ∉ ker_G^well} μ_k(u^well) / ∏_{k ∉ ker_G^saddle, k≠saddle} μ_k(u^saddle)` is correct — §3.3 notation should be updated to match.

---

## §6 — MAJOR Fixes Summary (8 Priority Findings)

The following MAJOR findings from the critic review (07_critic_full_review.md §A-§E) require correction before W9+ reference. They are ranked by cross-file impact.

### §6.1 MAJOR Fix M1: File 03 §3.2 — ε² Convention vs Canonical T-OP6-B (Factor 2)

**Critic reference**: §B.3
**Files affected**: 03, 05, 06 (all use `ε² = α/β`)

**Issue**: Files 03/05/06 use `ε² = α/β` and `ℓ_bd = √(α/β)` for the Allen-Cahn interface width. Canonical `T-OP6-B` (Cat A, canonical.md L385-388) states `ξ = √(2α/β)`, i.e., `ξ² = 2α/β` — differing by factor 2.

**Root cause**: The SCC energy has `E_bd = α·uᵀLu + β·ΣW(u)`. The canonical factor-4 ordered-pair convention (CLAUDE.md "Critical Implementation Details") means the effective diffusion coefficient is `2α` (factor-4 gradient = `4αLu`, so effective diffusion scale `~ 2α`). The interface width from matched asymptotics: `ξ = √(2α/β)`.

**Fix specification**:
```
WRONG: ε² = α/β, ℓ_bd = √(α/β)   [used in files 03/05/06]
CORRECT: ξ² = 2α/β, ℓ_bd = √(2α/β)  [canonical T-OP6-B, Cat A]

Discrepancy: factor √2 ≈ 1.414 on all boundary-width quantities.

Required action: Files 03/05/06 must either:
  (a) Adopt canonical T-OP6-B convention ξ² = 2α/β throughout, OR
  (b) Explicitly flag: "This file uses ε² = α/β (factor-2-rescaled convention); 
      canonical T-OP6-B uses ξ² = 2α/β. All ℓ_bd values here should be 
      multiplied by √2 to match canonical convention."
Option (b) is acceptable for working-layer files; option (a) required for any canonical promotion.
```

### §6.2 MAJOR Fix M2: File 02 §3.3 — `det` vs `det'` Inconsistency

**Critic reference**: §A.2
**Files affected**: 02 (§3.3 vs §5.1 internal inconsistency)

**Issue**: File 02 §3.3 writes `|det Hess(V)(x_well)|` (full determinant) in the HTB formula numerator, but the well on T²₁₆ (translation-invariant graph) has Goldstone zero eigenvalues, making `det Hess(u_well) = 0`. The formula is ill-defined. File 02 §5.1 correctly uses `∏_{k ∉ ker_G^well} μ_k(u_well)` (the `det'` form). §3.3 is internally inconsistent with §5.1.

**Fix specification**:
```
File 02 §3.3: Replace

  ω_0^{multi-D} = (|μ_saddle|/(2π)) · √(|det Hess(V)(x_well)| / |det' Hess(V)(x_saddle)|)

with

  ω_0^{multi-D} = (|μ_saddle|/(2π)) · √(|det' Hess(V)(x_well)| / |det' Hess(V)(x_saddle)|)

where det' at BOTH positions excludes zero eigenvalues (Goldstone modes at the well; 
Goldstone modes + the single negative eigenvalue at the saddle).

Definition (add at §3.3): "det'(H) := product over all nonzero eigenvalues of H 
(excluding Goldstone modes on translation-invariant graphs per V5b-T-zero Cat A, 
and excluding the unstable negative eigenvalue at the saddle per S2 hypothesis)."

§5.1 is already correct (uses the ∏ form with explicit ker_G exclusion). 
No change to §5.1 required.
```

### §6.3 MAJOR Fix M3: File 02 §6.4 — μ_well/μ_saddle Estimates Unsubstantiated (Factor 3-100x)

**Critic reference**: §A.5
**Files affected**: 02 (§6.2-§6.5)

**Issue**: File 02 §6.2 estimates `μ_well ~ 10` and §6.3 estimates `|μ_saddle| ~ 30`. These are unsubstantiated scaling arguments. The canonical anchor `L-HMORSE-LOCAL` numerical anchor (canonical L1960) gives `μ_min ∈ [0.13, 3.49]` on 5×5/10×10/15×15 grids — suggesting `μ_well ~ 1`, not `~ 10`, i.e., an overestimate by 3-100×.

**Fix specification**:
```
File 02 §6.2-§6.3: Strengthen the caveat language:

"μ_well ~ 10 [CONJECTURE: scaling argument only; canonical L-HMORSE-LOCAL numerical 
anchor (canonical.md L1960) gives μ_min ∈ [0.13, 3.49] on smaller grids, suggesting 
μ_well ~ 1 on T²₁₆ at β/α=10. The '~10' estimate may be overestimated by 3-10×. 
True verification requires CODE/scripts/test_kramers_prefactor_torus.py (not yet run).]"

File 02 §6.4: Replace "ω_0 ≈ 2.76" with:
"ω_0 ~ (1/2π)·√(μ_well·|μ_saddle|) ≈ (1/2π)·√(μ_well·|μ_saddle|).
  At μ_well~10, |μ_saddle|~30: ω_0 ≈ 2.76 [per §5.1 conjecture].
  At μ_well~1, |μ_saddle|~3 (canonical anchor range): ω_0 ≈ 0.28.
  Range: ω_0 ∈ [0.28, 2.76] depending on non-uniform Hessian eigenvalues."

File 02 §6.5: Replace "Γ ~ 10^{-337}" with:
"Γ ~ exp(-ΔE/T_*) with ΔE ~ 10·β^{0.89} (exp38). Order of magnitude: 10^{-337}
to 10^{-340} depending on prefactor conjecture. Qualitatively correct; quantitatively
needs CODE/scripts verification."
```

### §6.4 MAJOR Fix M4: File 02 §5.1 — Unit Confusion in 1D-Projection Prefactor

**Critic reference**: §A.4
**Files affected**: 02 (§6.4 unit conversion)

**Issue**: File 02 §6.4 computes `ω_0 ≈ 2.76` "in units of √β/√α · 1/τ_0" with `τ_0 ≈ 33`, then gives `ω_0 ≈ 0.084 per unit time`. The unit conversion double-counts the dimensional content of μ. In natural Langevin units (where the Hessian eigenvalues already have units of 1/time²), `√(μ_well·|μ_saddle|)` directly has units of 1/time, so `ω_0 ≈ 2.76` per unit time WITHOUT any additional τ_0 factor.

**Fix specification**:
```
File 02 §6.4: Choose one unit convention and state it explicitly:

Option A (natural units, recommended):
"At reference (α=β=1, β/α=10, T_*=0.1): μ_well ~ 10, |μ_saddle| ~ 30 
[in natural Langevin time units where E_bd is dimensionless and T_* ~ 0.1 sets the noise].
ω_0^{1D-proj} = √(10·30)/(2π) ≈ 2.76 [per unit time, directly].
No additional τ_0 conversion needed: the μ values ARE the eigenvalues of the Hessian 
in natural units, and √μ has units of 1/time."

Option B (physical units with explicit τ_0):
"ω_0 ≈ 2.76/τ_0 [per second], where τ_0 is the natural time unit.
But then μ_well and μ_saddle must FIRST be rescaled by 1/τ_0² before insertion.
With τ_0 ≈ 33, rescaled eigenvalues: μ_well/τ_0² ~ 0.009, |μ_saddle|/τ_0² ~ 0.027.
ω_0 = √(0.009·0.027)/(2π) ≈ 0.0078/τ_0 [consistent]. 
CAUTION: mixing the two conventions inflates ω_0 by τ_0 ≈ 33."
```

### §6.5 MAJOR Fix M5: File 03 §6.1 — Mesh Refinement Required for Spectral Convergence

**Critic reference**: §B.5
**Files affected**: 03 (L-MODICA-JACOBI-HMORSE statement)

**Issue**: File 03 §6.1 states spectral convergence "as ε → 0" but conflates taking `β/α → ∞` on a **fixed graph** with the genuine continuum limit requiring **joint** `ε → 0` AND `h → 0` (mesh refinement). On a fixed T²₁₆ grid at large β/α, the discrete spectrum converges to an asymptotic regime, NOT to the continuum Jacobi spectrum.

**Fix specification**:
```
File 03 §6.1 hypothesis H3 must be strengthened from:
  "graph → continuum applicability (as ε → 0)"
to:
  "graph → continuum applicability (joint scaling: mesh h_n → 0, 
   ε_n = √(α_n/β_n) → 0, with α_n = α₀/h_n² or equivalent van Gennip-
   Bertozzi 2012 scaling; on a FIXED graph this limit is not achievable)"

Add clarifying note:
  "On T²₁₆ (n=256, fixed), the statement 'converges to Jacobi spectrum as ε → 0' 
   is FALSE — increasing β/α on a fixed graph does NOT refine the mesh. The continuum 
   Jacobi limit is a research direction (H3 conditional), not a numerical claim."
```

### §6.6 MAJOR Fix M6: File 04 §5.2 — ℓ_therm Undefined at Spinodal Interior

**Critic reference**: §C.4
**Files affected**: 04 (§5.2-§6.3, L-PR-BD-THRESHOLD)

**Issue**: File 04 §5.2 defines `ℓ_therm := √(T_*/(β·W''(u*)))`. At spinodal interior `u* = 1/2`, `W''(1/2) = -1 < 0`, making ℓ_therm imaginary. File 04 then silently uses `|W''|` in §6.1, but the local Gaussian approximation underlying ℓ_therm FAILS at spinodal points (the effective local potential is a local maximum, not a minimum, so there is no local Gaussian).

**Fix specification**:
```
File 04 §5.2: Add explicit restriction:
  "ℓ_therm = √(T_*/(β·W''(u*))) is valid ONLY at sites where W''(u*) > 0 
   (stable active-band sites, near-saturated edges u* ≈ 0.9 with W''(0.9) ≈ 0.92 > 0).
   At spinodal interior u* = 1/2: W''(1/2) = -1 < 0, ℓ_therm is imaginary, 
   and the local Gaussian approximation fails. This file's threshold Pr^{(bd)} ≥ 1 
   applies to the saturated-edge active-band regime ONLY, not to spinodal-interior sites."

File 04 §6.3 boxed Pr^{(bd)} ≥ 1: Restrict explicitly to saturated-edge sites:
  "Under D-HMORSE-LOCAL (C2') with near-saturated active sites (u*_i ≈ 0.9, W''(u*_i) > 0):
   Pr^{(bd)} = T_* / (β·W''(u*_i)·ℓ_therm²) ≥ 1."

Label scope:
  "The spinodal-center case (u*_i = 1/2) requires a separate treatment: 
   the local potential is a maximum, not a well; a Morse-theoretic analysis 
   (not a Gaussian approximation) is needed there."
```

### §6.7 MAJOR Fix M7: File 04 §3.2 — Weyl Mis-Attribution

**Critic reference**: §C.1
**Files affected**: 04 (§3.2)

**Issue**: File 04 §3.2 attributes the bound `μ_min(M) ≥ min_i(d_i) - ||S||_op` (for symmetric M = D+S with D diagonal) to "Cauchy-Weyl interlacing." The correct reference is **Weyl's inequality for Hermitian matrix sums**: `μ_min(A+B) ≥ μ_min(A) + μ_min(B) ≥ μ_min(A) - ||B||_op`.

**Fix specification**:
```
File 04 §3.2: Replace "Cauchy-Weyl interlacing" → "Weyl's inequality (H+S sum of Hermitian):
  μ_min(D+S) ≥ μ_min(D) + μ_min(S) ≥ min_i(d_i) - ||S||_op."

Also add clarification on subspace:
  "The bound μ_bulk ≥ 2β applies to the bulk block H_BB evaluated on the 
   bulk-subspace tangent vectors. The zero mode (constant on B) is globally 
   constrained by Σu_i = m but not zero on B alone; the Schur complement 
   H_eff^AA handles this correctly. The bound 2β is for the bulk block only."
```

### §6.8 MAJOR Fix M8: File 05 §5.1 — T-RESCALE-HESSIAN-LINEAR Proof Incomplete for Non-Uniform u*

**Critic reference**: §D.3
**Files affected**: 05 (§5.1)

**Issue**: File 05 §5.1 proves `μ_k(sα,sβ) = s·μ_k(α,β)` for the UNIFORM case `u* = c·1` only (via Theorem 4). The catalog entry `T-RESCALE-HESSIAN-LINEAR` claims to cover all critical points `u*`. The non-uniform case proof (bilinearity of `E_bd` in (α,β)) is only in file 06 §3 Case 2, not in file 05.

**Fix specification**:
```
File 05 §5.1: After the uniform case proof, add:

"For non-uniform critical u* (general): E_bd(u; α,β) = αu^T L_G u + β Σ W(u_i) is 
linear-homogeneous in (α,β), so E_bd(u; sα,sβ) = s·E_bd(u; α,β). Since differentiation 
is linear: H(u*; sα,sβ) = ∇²E_bd(u*; sα,sβ)|_{TΣ_m} = s·∇²E_bd(u*; α,β)|_{TΣ_m} 
= s·H(u*; α,β). Therefore μ_k(sα,sβ) = s·μ_k(α,β) for all k. □

[Cross-reference: file 06 §3 Case 2 contains the same argument with fuller details. 
The two files together provide the complete proof for all u*.]"
```

---

## §7 — Cross-File Consistency Mandate (For Future Ultrawork)

Per critic §H.3 final recommendation, any future parallel-ultrawork session producing multiple files on shared mathematical content MUST satisfy these mandates before critic review:

### §7.1 Single-Source Constants

All shared mathematical constants must be declared in a **single source block** at the start of any new framework file. Copy-paste this block verbatim:

```
## §CONST — Shared Constants (Single Source of Truth)

σ-FORMULA (canonical Modica-Mortola):
  σ = (√2/6) · √(αβ) ≈ 0.2357 · √(αβ)        [NOT √(αβ)/3]
  
  Derivation: σ = √(αβ) · ∫₀¹ √(2W(s)) ds = √(αβ) · √2·∫₀¹ s(1-s) ds 
                = √(αβ) · √2/6. Verified: √2/6 ≈ 0.2357.
  
  At α=β=1: σ = √2/6 ≈ 0.2357   [NOT 1/3 ≈ 0.333]
  At α=1, β=5: σ = √10/6 ≈ 0.527   [NOT √5/3 ≈ 0.745]

ε-CONVENTION:
  Files may use either ε² = α/β or the canonical ξ² = 2α/β (T-OP6-B).
  Any file using ε² = α/β MUST state: "ε² = α/β convention (differs from 
  canonical T-OP6-B ξ² = 2α/β by factor 2)."

REFERENCE BASELINE (shared across all field-equation-framework files):
  Graph: 2D torus C₁₆ × C₁₆, n=256 nodes, degree-4 regular.
  Parameters: α=1, β=5, T_*=0.1, c=1/2, R=4.   [NOTE: β=5, not β=1 or β=10]
  λ₂ = 4sin²(π/16) = 0.152241
  Sc_{T8} = 4α·λ₂/(β·|W''(c)|) = 4·0.152241/5 = 0.122 (super-critical for β=5)
  σ at reference: (√2/6)·√5 ≈ 0.527
  
  [Individual files may use other parameters internally, but any cross-file 
  numerical claim must specify which baseline it uses.]
```

### §7.2 Canonical OP Citation Protocol

**Mandatory rule** (repeat of CSSL lesson, re-stated for W9+):

Every citation of a canonical OPEN problem MUST cite `theorem_status.md` as the primary source (it contains the OP registration table). Citing only `canonical.md` for an OP is insufficient — canonical.md contains cross-references and non-overclaim caveats, but the OP's definition, status, ETA, and inter-OP relationships are in `theorem_status.md`.

**Required citation form:**
```
MINIMUM: OP-HMORSE-SADDLE (theorem_status.md L594, OPEN)

PREFERRED (dual-citation):
  OP-HMORSE-SADDLE (registration: theorem_status.md L594; 
                   cross-ref: canonical.md L1967 non-overclaim caveat)
```

**Prohibited:** citing only `canonical.md LXXX` for an OP registration.

### §7.3 Kramers Identity Protocol

Following CRITICAL Fix #4, any future use of Kramers prefactor identities must distinguish:

```
Identity 2a (structural): ω_0 ~ ω_well·ω_saddle/√Pr = |μ_saddle|  [leading order]
Identity 2b (1D-proj):    ω_0 = ω_well·ω_saddle/(2π)               [1D geometric mean]
Multi-D:  ω_0 = (|μ_saddle|/(2π))·√(det'_well/det'_saddle)         [full HTB form]
```

Never conflate 2a and 2b. Always specify which form is being used. The multi-D form is the correct one for SCC on T²₁₆.

### §7.4 Prefactor Rescaling Protocol

Following CRITICAL Fix #3, any future claim about Kramers prefactor behavior under (α,β)→(sα,sβ) must use the correct scaling:

```
Invariant under rescaling:   Pr^{(Kramers)} = |μ_well|/|μ_saddle|
Scales linearly with s:       ω_0(s) = s·ω_0(1)
Scales linearly with s:       ΔE(s) = s·ΔE(1)
Full rate: Γ(s) = s·ω_0(1)·exp(-s·ΔE(1)/T_*)  [BOTH prefactor and exponent s-dependent]
```

---

## §8 — W9+ Promotion Gate Status Per File

Based on `07_critic_full_review.md` §G (per-file verdicts) and §H.3 (recommendations), the promotion gate for each Wave 1 file is:

### §8.1 File 02 — `02_kramers_prefactor_op_0005_attack.md`

**Critic verdict**: ACCEPT WITH MAJOR REVISIONS

**W9+ gate**: **CONDITIONAL PASS** after 4 targeted fixes:
- [Fix required] §3.3: replace `det` → `det'` at well (CRITICAL Fix #4 related, §A.2)
- [Fix required] §5.1: split Identity 2 into 2a + 2b (CRITICAL Fix #4, §5.2-§5.3 above)
- [Fix required] §6.2-§6.3: mark μ_well/μ_saddle estimates as conjectural with canonical anchor range (§6.3 above)
- [Fix required] §6.4: clarify unit convention (natural units vs τ_0 conversion) (§6.4 above)

Cat B target classification: HONEST. Canonical anchors: HIGH accuracy. CN10/CN12/CN15: COMPLIANT.

**Usable for W9+ reference after fixes**: Yes. The L-KRAMERS-PR-SCC lemma structure and Cat B classification survive all fixes intact.

### §8.2 File 03 — `03_modica_mortola_jacobi_cat_b.md`

**Critic verdict**: SUBSTANTIAL REVISE (2 CRITICAL)

**W9+ gate**: **BLOCKED** until:
- [CRITICAL] 9 L1967 citations fixed → theorem_status.md L594 (CRITICAL Fix #2, §3 above)
- [CRITICAL] σ-formula: file 03 ALREADY HAS the correct value (√2/6) so no σ change needed, but the file must explicitly flag that files 05/06 use the WRONG value and cross-references must use file 03's value
- [MAJOR] §6.1 mesh-refinement requirement added to H3 (§6.5 above)
- [MAJOR] §5.4 rotation Goldstone scope restriction added (pedagogical sphere model ≠ SCC Goldstone structure)
- [MAJOR] §10.2 saddle Jacobi analysis restricted to catenoid-like (isolated-neck) saddles

Estimated fix effort: Substantial. File 03 is the most affected by CRITICAL Fix #2 (9-instance correction).

**Usable for W9+ reference after fixes**: Yes. The σ derivation in file 03 is actually the CORRECT one and can serve as the σ reference for all other files.

### §8.3 File 04 — `04_h_morse_spectral_quantification.md`

**Critic verdict**: SUBSTANTIAL REVISE (5 MAJOR rigor issues)

**W9+ gate**: **BLOCKED** until:
- [MAJOR] §3.2 Weyl mis-attribution corrected + subspace clarification added (§6.7 above)
- [MAJOR] §5.2-§6.3 ℓ_therm restricted to W''>0 regime; spinodal-interior case flagged (§6.6 above)
- [MAJOR] §3.3-§3.4 Schur bound derivation tightened (explicit subspace statements)
- [MAJOR] §6 ε² convention flagged relative to canonical T-OP6-B (§6.1 above)
- [MINOR→MAJOR] cross-file numerical baseline: adopt α=1, β=5 reference or explicitly flag file's own baseline

Estimated fix effort: Substantial. Rigor issues throughout §3-§6 require careful rewriting.

**Usable for W9+ reference after fixes**: Yes. The Sc^{(2)} and Pr^{(bd)} target structure is sound; the derivation paths need tightening.

### §8.4 File 05 — `05_cat_a_direct_catalog_proofs.md`

**Critic verdict**: SUBSTANTIAL REVISE (1 CRITICAL: σ)

**W9+ gate**: **BLOCKED** until:
- [CRITICAL] σ formula corrected to (√2/6)·√(αβ) throughout; Ca, Bo, Le_SCC, reference table all recomputed (CRITICAL Fix #1, §2 above)
- [MAJOR] T-RESCALE-HESSIAN-LINEAR §5.1 proof extended to non-uniform u* (§6.8 above)
- [MAJOR] T-IDENTITY-KRAMERS-PREFACTOR-FORM §4.5 split into Identity 2a + 2b (CRITICAL Fix #4, §5.2-§5.3 above)
- [MINOR] Pr^{(spatial)} = αλ_2/T_* convention: add prominent flag that this differs from the Hessian spatial contribution by factor 4 (file 05 §D.2)

Estimated fix effort: Moderate. The σ fix propagates through ~4 lemmas but is arithmetic correction only. The Identity 2 split requires rewriting §4.5.

**Usable for W9+ reference after fixes**: Yes. The dimensionless number definitions (§3) and most identities (§4) survive; the σ-contaminated lemmas need numerical correction.

### §8.5 File 06 — `06_surface_tension_rescaling_cat_a.md`

**Critic verdict**: ACCEPT WITH MAJOR REVISIONS (1 CRITICAL: σ shared; 2 MAJOR)

**W9+ gate**: **CONDITIONAL PASS** after 3 targeted fixes:
- [CRITICAL] σ formula in §2 and §3 Proof (c) corrected to (√2/6)·√(αβ) (CRITICAL Fix #1, §2.3 above); numerical reference values in §7 recomputed
- [CRITICAL] §8.1 Kramers prefactor invariance claim RETRACTED and replaced with correct s-scaling statement (CRITICAL Fix #3, §4.3-§4.4 above)
- [MAJOR] §3 restructured: Case 2 (bilinearity) promoted to main proof; Case 1 (uniform) demoted to sanity check (§E.2)

Cat A direct classification (parts a-f): **SURVIVES ALL FIXES INTACT.** The rescaling lemma core is mathematically correct; only the σ numerical value and the §8.1 cross-file claim require correction.

**Usable for W9+ reference after fixes**: Yes. File 06 is the highest-quality Wave 1 output — 3 targeted fixes restore it to full W9+ readiness.

---

## §9 — Hard Constraint CN1-16 Check (16/16 ✓)

This fix document itself is checked against the 16 hard constraints:

| CN | Description | Status |
|---|---|---|
| CN1 | 0 canonical/* edits | ✓ 0 edits (fix spec only) |
| CN2 | No silent OP resolution | ✓ No OP closed; all remain OPEN |
| CN3 | No Research OS structure | ✓ No numbered 00-99 dirs or 5-role logs |
| CN4 | Analyticity preserved (no new energy terms) | ✓ No energy terms introduced |
| CN5 | 4-term independence preserved | ✓ No merging of E_cl, E_sep, E_bd, E_tr |
| CN6 | u_t primitive preserved | ✓ u_t remains primitive; fixes are on derived quantities |
| CN7 | No per-item registry files | ✓ This is a single consolidated spec file |
| CN8 | Experiment numbering stable | ✓ No experiments referenced or renumbered |
| CN9 | Promotion pipeline one-way | ✓ No reverse flow from canonical; fixes stay in working/ |
| CN10 | No reductive reduction (SCC ≠ fluid/particle/AC) | ✓ Kramers is contrastive; no SCC = X claim |
| CN11 | No Mori-Zwanzig / inertia | ✓ 0 references |
| CN12 | No CSSL E_ridge/E_wild/E_pers | ✓ 0 references |
| CN13 | No second-order temporal (∂²u terms) | ✓ 0 references |
| CN14 | Primitive u_t ontologically prior | ✓ All objects derived from u_t |
| CN15 | Open problems remain explicit | ✓ All 4 critical fixes leave OPs OPEN; no resolution claimed |
| CN16 | DECLARATION consistency | ✓ Q1-Q6 structure untouched; SCC identity preserved |

**16/16 ✓ — Full constraint compliance.**

---

## §10 — One-Paragraph Summary

The Wave 2 adversarial critic review of Wave 1 outputs (files 02-06) identified 4 CRITICAL and 17 MAJOR findings resulting from parallel-generation cross-file inconsistency. This document specifies exact corrections for all 4 CRITICAL findings: (1) the surface tension constant `σ = (√2/6)·√(αβ)` — files 05 and 06 used the wrong value `√(αβ)/3` by factor √2; (2) file 03's systematic 9-instance miscitation of OP-HMORSE-SADDLE as `canonical.md L1967` when the canonical registration is `theorem_status.md L594`; (3) file 06 §8.1's false claim that the Kramers prefactor is invariant under (α,β)→(sα,sβ) rescaling — the correct result is `ω_0(s) = s·ω_0(1)` (linear scaling), while only `Pr^{(Kramers)}` is invariant; and (4) files 02/05's equation of `ω_well·ω_saddle·(Pr)^{-1/2} = |μ_saddle|` with `√(μ_well·|μ_saddle|)` — these are different quantities that must be split into Identity 2a (structural leading-order `∝ |μ_saddle|`) and Identity 2b (1D-projection geometric mean `∝ √(μ_well·|μ_saddle|)`). After applying these fixes, files 02 and 06 are conditionally cleared for W9+ reference; files 03, 04, and 05 require substantial rework before W9+ reference. This document is the Wave 1 → W9+ promotion gate.
