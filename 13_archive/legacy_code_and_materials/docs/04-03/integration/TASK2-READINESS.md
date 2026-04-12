# Task #2 Cross-Validation: Transport Confinement Tight Bound

**Date:** 2026-04-03
**Validator:** basin-mathematician
**Purpose:** Checklist for validating Task #2 deliverables when transport-mathematician reports

---

## Expected Deliverables

- [ ] `docs/04-03/proof/TIGHT-CONFINEMENT-FINAL.md` (5-6 pages, formation-aware cost decomposition)
- [ ] `experiments/exp45_refined.py` or equivalent (optional, refined confinement on higher-res grid)

---

## Validation Checks

### 1. Decomposition Formula Alignment

- [ ] Does formation-aware decomposition $C_{\mathrm{tr}} = C_{\mathrm{core}} + C_{\mathrm{boundary}}$ logically fit with the conjugation identity from Task #1 (C3'' symmetrization)?
- [ ] Are the bounds $C_{\mathrm{boundary}} \leq |\mathrm{Bdy}_k| \cdot \max(u_{\mathrm{bdy}}) \cdot (\text{Sinkhorn log-domain rate})$ consistent with exp45 data?
- [ ] Does the decomposition respect the ordered-pair summation convention (Canonical Spec v2.1 Section 0)?

### 2. Sinkhorn-Lipschitz Backing

- [ ] Does Task #2 reference `SINKHORN-LIPSCHITZ.md` (from docs/04-02/proof/, Task #4's Cat A upgrade)?
- [ ] Does confinement bound $L_{\mathrm{sink}} \approx 1.1$ appear in safety factor justification?
- [ ] Is the Sinkhorn convergence rate correctly stated (log-domain, entropy-regularized)?

### 3. Exp45 Experimental Match

- [ ] Does refined confinement on higher-res grid show $\pm 5\%$ agreement with theoretical bound?
- [ ] Are violation instances explained (e.g., near-bifurcation formation geometry, small grid effects)?
- [ ] Is the 1.02x violation from exp41 (referenced in PLAN_0403.md) addressed or explained?

### 4. Spectrum-to-Basin Bridge

- [ ] Does transport parametrization from confinement connect to basin depth?
  - Basin depth: $\Delta_{\mathrm{bdy}}$ via soft-mode energy probe (Task #3: $\Delta = 0.593$ at default params)
  - Transport displacement: $\|\tilde{u} - \hat{u}_s\| \leq C_{\mathrm{conf}} \sqrt{m}$ must be $< r_{\mathrm{eff}}$
- [ ] Is the formation-conditioned bound from TC-FORMATION-CONDITIONED.md (04-02) incorporated or superseded?
- [ ] Any logical gaps or tension points between confinement and basin containment?

### 5. Category Assessment

- [ ] Does Task #2 claim Cat A or Cat B for T-Persist-1(e)?
- [ ] What conditions (if any) remain for Cat A upgrade?
- [ ] Is the shallow-core limitation ($\delta = 1$) addressed?
  - Deep core ($\delta \geq 2$): exponential concentration expected
  - Shallow core ($\delta = 1$): weak concentration only; shifted-threshold fallback (T-Persist-1(c)) applies

### 6. Consistency with Task #3 Results

- [ ] Does the confinement bound $C_{\mathrm{conf}} \sqrt{m}$ at default params yield displacement $< r_{\mathrm{eff}} \approx 0.18$ (from EXP44-VERIFICATION.md)?
- [ ] Is the gentleness condition $\varepsilon < \varepsilon_{\max}$ from T-PERSIST-1B-UNCONDITIONAL.md compatible with the transport bound?
- [ ] Do the two proofs (Task #2 confinement + Task #3 basin) compose cleanly for T-Persist-Full?

---

## Outcome

| Check | Status | Notes |
|-------|--------|-------|
| 1. Decomposition alignment | | |
| 2. Sinkhorn-Lipschitz | | |
| 3. Exp45 match | | |
| 4. Spectrum-basin bridge | | |
| 5. Category assessment | | |
| 6. Task #3 consistency | | |

**Verdict:** ___ (Green: all checks pass / Yellow: minor issues for Task #6 / Red: blocking issues)

---

## Reference Files

- Task #3 output: `docs/04-03/proof/T-PERSIST-1B-UNCONDITIONAL.md`
- Task #3 verification: `docs/04-03/integration/EXP44-VERIFICATION.md`
- Prior confinement: `docs/04-02/proof/TC-FORMATION-CONDITIONED.md`
- Sinkhorn-Lipschitz: `docs/04-02/proof/SINKHORN-LIPSCHITZ.md`
- Basin escape: `docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md`
- BC' theorem: `docs/04-02/proof/BC-PRIME-THEOREM.md`
- F1 upgrade: `docs/04-02/proof/F1-BOUND-CATA-UPGRADE.md`
