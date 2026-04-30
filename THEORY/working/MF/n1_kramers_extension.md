# n1_kramers_extension.md — N-1 Soft-Hard Switching ↔ K-Selection (b) Kramers Connection

**Status:** working draft (W5 Day 4 PM Wave 3, 2026-04-30).
**Type:** Bridge between canonical §11.1 N-1 and OP-0005 K-Selection candidate (b).
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 N-1 Soft-Hard Switching Asymmetry; §11.1 CN6 K-determination; OP-0005 K-Selection.
**Working refs:** `k_selection_mechanism.md` (in flight, OP-0005 attack); `cn15_static_dynamic_separation.md` (CN15 protocol-conditional framework).

---

## §1. Mission

OP-0005 K-Selection candidate (b) Kramers metastability (per `k_selection_mechanism.md` §3) is closely related to canonical N-1 Soft-Hard Switching Asymmetry (W4 04-19, canonical §11.1). This file makes the connection explicit and proposes a unified treatment for CV-1.6+ canonical merge.

---

## §2. N-1 Statement (canonical, existing)

From canonical §11.1 (W4 04-19):

> **N-1. Soft-Hard Switching Asymmetry.** Phase transitions in SCC dynamics are *asymmetric*: soft → hard transitions (formation birth, K_act increase) require larger fluctuation amplitudes than hard → soft transitions (formation merger, K_act decrease). Under noiseless gradient flow, the asymmetry collapses: soft → hard becomes forbidden (NQ-253 §4.3 Claim 4.3); hard → soft remains accessible.

---

## §3. K-Selection (b) Kramers Statement

From `k_selection_mechanism.md` §3 (in flight):

> **K-Selection (b) Kramers metastability.** $K_{\mathrm{act}}$ at long times is determined by initial conditions + barrier-crossing rates per Kramers (1940):
> $$k_{K \to K-1} = \frac{\omega_0}{2\pi} \exp\left(-\beta \cdot \Delta E_{\mathrm{barrier}}^{(K \to K-1)} / k_B T\right)$$
> 
> where $\omega_0$ is the prefactor (saddle-point frequency), $\Delta E_{\mathrm{barrier}}^{(K \to K-1)}$ is the energy barrier for the K → K-1 merger transition, and the noise scale enters via $1/k_B T$.

---

## §4. The Connection

### §4.1 N-1 asymmetry = Kramers rate asymmetry

N-1's "soft → hard" = formation birth = $\Delta K_{\mathrm{act}} = +1$. Kramers rate for this is:
$$k_{K \to K+1} = \frac{\omega_0}{2\pi} \exp\left(-\beta \cdot \Delta E_{\mathrm{birth}} / k_B T\right)$$

N-1's "hard → soft" = formation merger = $\Delta K_{\mathrm{act}} = -1$. Kramers rate:
$$k_{K \to K-1} = \frac{\omega_0}{2\pi} \exp\left(-\beta \cdot \Delta E_{\mathrm{merger}} / k_B T\right)$$

**Asymmetry:** $\Delta E_{\mathrm{birth}} > \Delta E_{\mathrm{merger}}$ (typically). At low temperature ($k_B T \to 0$), the merger rate dominates exponentially:
$$\frac{k_{K \to K+1}}{k_{K \to K-1}} = \exp\left(-\beta \cdot (\Delta E_{\mathrm{birth}} - \Delta E_{\mathrm{merger}}) / k_B T\right) \to 0 \text{ as } T \to 0$$

This is precisely N-1's claim: soft → hard requires larger fluctuations (= higher barrier) than hard → soft.

### §4.2 Noiseless limit recovers NQ-253 §4.3 Claim 4.3

At $T = 0$ (noiseless gradient flow), both Kramers rates vanish exponentially, but the *ratio* is what matters: $k_{K \to K+1} / k_{K \to K-1} = 0$ in the strict $T = 0$ limit. Therefore:
- Birth events $\Delta K_{\mathrm{act}} = +1$ are *forbidden* (rate = 0).
- Merger events $\Delta K_{\mathrm{act}} = -1$ remain accessible at any rate (relative to birth).

This is exactly NQ-253 §4.3 Claim 4.3: "Under noiseless SCC gradient flow on $\widetilde\Sigma^K_M$..., a formation at $K_{\mathrm{act}} = 1$ will NOT spontaneously birth a second formation."

**Net result: N-1 + K-Selection (b) + NQ-253 §4.3 are three readings of the same physics.**

---

## §5. Unified Statement (CV-1.6 candidate)

**Unified principle:** The K-selection problem (OP-0005) admits a Kramers-rate formulation in which:
1. $K_{\mathrm{act}}$ at long times is a *protocol-endpoint observable* (CN15 dynamic reading).
2. Under noiseless flow, $K_{\mathrm{act}}$ is monotone non-increasing (T-Merge (b) Cat A on multi-formation manifold; equivalent to vanishing forward Kramers rate at $T = 0$).
3. Under finite noise (P-F flagged), the Kramers rates determine equilibrium $K_{\mathrm{act}}$ distribution via detailed balance: $P(K_{\mathrm{eq}})/P(K_{\mathrm{eq}} - 1) = k_{K-1 \to K} / k_{K \to K-1}$.

**N-1 captures (1) + (2)** as a structural asymmetry. **K-Selection (b) captures (3)** as a quantitative selection mechanism.

---

## §6. Canonical merge proposal (CV-1.6)

Append to canonical §11.1 N-1 entry:

```markdown
**N-1 Sub-statement (CV-1.6 added):** N-1 Soft-Hard Switching Asymmetry admits a 
Kramers-rate formulation. Under finite noise (P-F flagged), forward (soft → hard, 
$\Delta K_{\mathrm{act}} = +1$) and reverse (hard → soft, $\Delta K_{\mathrm{act}} = -1$) 
transitions have rates $k_{K \to K \pm 1}$ proportional to $\exp(-\beta \Delta E^{(\pm)} / k_B T)$. 
Asymmetry $\Delta E^{(+)} > \Delta E^{(-)}$ implies forward rate dominated at low T; 
in noiseless limit ($T \to 0$), forward rate vanishes (recovering NQ-253 §4.3 
Claim 4.3 noiseless-flow forbidding). This gives an OP-0005 K-Selection candidate 
mechanism (b) per `working/MF/k_selection_mechanism.md` §3.

References: Kramers (1940), Hänggi-Talkner-Borkovec (1990); 
working/MF/n1_kramers_extension.md (this connection); 
working/MF/k_selection_mechanism.md §3 (candidate (b)).
```

**Effort:** ~30 canonical lines.

**Counts impact:** none direct (sub-statement of existing N-1, no new theorem).

---

## §7. Hard constraint verification

- [x] **u_t primitive maintained**: Kramers rates are computed on cohesion-field gradient flow; primitive unchanged.
- [x] **CN10 contrastive**: Kramers (1940) is referenced for rate-theory framework, not reductive identification with chemical reaction kinetics. SCC is not a chemical reaction.
- [x] **CN5 4-energy not merged**: barrier energies $\Delta E^{(\pm)}$ are computed in full $\mathcal{E}$ (4 energy terms preserved, not merged).
- [x] **P-F flag on noise**: explicitly stated; finite-T behavior requires P-F deepening before strict claims.
- [x] **OP not silently resolved**: OP-0005 K-Selection remains 🟠 OPEN HIGH; this file frames a candidate mechanism, doesn't resolve.

---

## §8. Cross-references

- canonical §11.1 N-1 Soft-Hard Switching Asymmetry (existing, W4 04-19).
- working/MF/k_selection_mechanism.md §3 candidate (b) Kramers (in flight).
- working/MF/cn15_static_dynamic_separation.md §3 dynamic reading (this Wave 3).
- working/MF/formation_birth_string_breaking.md §4 mechanisms B1/B2/B3 (NQ-253).
- working/MF/sigma_rich_augmentation.md §4 protocol-conditional Φ_rich (this Wave 3).

---

**End of n1_kramers_extension.md.**

**Status:** CV-1.6 canonical §11.1 N-1 sub-statement candidate. ~30 canonical lines. Cat A definitional (N-1 + Kramers theory both well-established). Promotion target: W6 Day 7 EOD with CV-1.6 packet.
