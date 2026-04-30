# cn15_static_dynamic_separation.md — CN15 Static/Dynamic Separation Canonical Promotion Candidate

**Status:** working draft (W5 Day 4 PM Wave 3, 2026-04-30).
**Type:** CV-1.6 canonical §11.1 amendment proposal.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 CN6 K-determination (existing); §13 T-Merge (b) Cat A; §13 T-PreObj-1 + T-PreObj-1G; OP-0001 F-1 SPLIT-RESOLVED.
**Working refs:** `K_status_commitment.md` (OAT-1, Commitment 16); `formation_birth_string_breaking.md` (NQ-253 §4 noiseless flow constraint); `k_selection_mechanism.md` (in flight).

---

## §1. Mission

W4 (2026-04-19~26) F-1 split-resolution work introduced an implicit principle that distinguishes **static global minimum** of pure $\mathcal{E}_{\mathrm{bd}}$ from **dynamic protocol-endpoint observables** of full $\mathcal{E}$. This principle was used (a) to resolve OP-0001 F-1, (b) to clarify OP-0002 M-1, and (c) to ground Theorem 2 family (T-PreObj-1G).

**The principle has not been canonically registered.** This file proposes its formal registration as **CN15 Static/Dynamic Separation** in canonical §11.1 at CV-1.6 (W6 Day 7 EOD).

---

## §2. CN15 Statement (CV-1.6 candidate)

**CN15. Static/Dynamic Separation.** *(NEW, CV-1.6 candidate, 2026-04-30 W5 Day 4 PM proposal.)*

The static and dynamic readings of multi-formation observables on a finite graph $G$ with full SCC parameters are conceptually independent and may have distinct ground states:

1. **Static reading.** The global minimum of pure $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_M^K$ has $K_{\mathrm{step}} = 1$ (perimeter-minimization on connected graphs by isoperimetric ordering, T-Merge (b) Cat A). At this static reading, $K = 1$ is the energetically preferred multi-formation state.

2. **Dynamic reading.** The protocol-endpoint observables $\widehat{K}_{\mathrm{act}}, \mathcal{F}, \widehat{\sigma}^A_{\mathrm{multi}}(t)$ of full $\mathcal{E}$ under gradient flow on $\widetilde\Sigma^K_M$ need not equal the static minimum. Specifically:
   - Pre-objective default ground state has $\mathcal{F} \geq 2$ (T-PreObj-1 Cat A graph-class independent via T-PreObj-1G).
   - $K_{\mathrm{act}}$ trajectory is monotone non-increasing under noiseless flow (T-Merge (b) Cat A on multi-formation manifold).
   - Birth events ($\Delta K_{\mathrm{act}} = +1$) are forbidden under noiseless flow (NQ-253 §4.3 Claim 4.3 + sigma_rich_augmentation.md §4 protocol-conditional).
   - Equilibrium $K_{\mathrm{act}}$ depends on initial condition + protocol (NQ-253 §4.2 mechanisms B1/B2/B3).

3. **Resolution of apparent K=1 vs K>1 conflict.** The empirical observation that R23 minimizers have $\mathcal{F} \in [5, 63]$ (W4 04-23 enumeration) is *not* in conflict with the static $K=1$ ground state of pure $\mathcal{E}_{\mathrm{bd}}$. The two readings refer to different objects:
   - *Static reading*: minimum of pure $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_M^K$ — a mathematical optimization, not a dynamical claim.
   - *Dynamic reading*: equilibrium of full SCC gradient flow on $\widetilde\Sigma^K_M$ — a protocol-conditional empirical observable.
   - The reframing of OP-0001 F-1 (W4 04-24) recognizes both readings are *correct* in their own scope; the apparent conflict was a misframing.

**Ontological status:** CN15 is a *conceptual constraint* on theoretical reading, not a new theorem. It clarifies the scope of canonical statements (T-Merge (b), T-PreObj-1, NQ-253 Claim 4.3) by demarcating their respective domains of applicability.

**Connection to existing CNs:**
- **CN6 (K kinetically determined):** CN15 sharpens CN6 by separating "kinetically determined" into static/dynamic readings. CN6's "K is kinetically determined" applies to dynamic reading; the static reading has K=1 by isoperimetric ordering, which is *not* kinetic determination but a global energy fact.
- **CN10 (Contrastive Comparison):** CN15 enforces contrastive reading — gauge-theoretic / stat-mech analogs that suggest static ground state = dynamic ground state are CN10 contrastive only; SCC's static/dynamic separation is a structural feature, not a defect.
- **Commitment 16 (K-status):** CN15 supplies the *interpretive backdrop* for Commitment 16's $K_{\mathrm{field}}$ vs $K_{\mathrm{act}}$ distinction. $K_{\mathrm{field}}$ is architectural (modeling-layer); $K_{\mathrm{act}}$ is dynamic-emergent. CN15 ensures that comparing static-pure-$\mathcal{E}_{\mathrm{bd}}$ K=1 to dynamic-full-$\mathcal{E}$ K_act is a *category error* rather than a paradox.

---

## §3. Canonical merge text

Insert at canonical §11.1 (Conceptual Norms section) after CN14 (existing) and before any new commitments. Estimated ~50 canonical lines.

```markdown
**CN15. Static/Dynamic Separation.** *(CV-1.6 added, 2026-04-30 W5 Day 4 PM W4 retroactive registration.)*

The static and dynamic readings of multi-formation observables are conceptually 
independent. Static global minimum of pure $\mathcal{E}_{\mathrm{bd}}$ on 
$\Sigma_M^K$ has $K_{\mathrm{step}} = 1$ (T-Merge (b) Cat A); dynamic protocol-endpoint 
of full $\mathcal{E}$ has $\mathcal{F} \geq 2$ default (T-PreObj-1 Cat A). The two 
readings refer to different mathematical objects, and the apparent K=1 vs K>1 
conflict (W4 OP-0001 F-1 history) is a misframing rather than a paradox. Sub-clauses:

(i) Static reading: pure $\mathcal{E}_{\mathrm{bd}}$ minimum on $\Sigma_M^K$.
(ii) Dynamic reading: full $\mathcal{E}$ gradient flow protocol-endpoint on 
$\widetilde\Sigma^K_M$.
(iii) Birth events $\Delta K_{\mathrm{act}} = +1$ forbidden under noiseless flow 
(NQ-253 §4.3 Claim 4.3); protocol-conditional via thermal noise / IC manipulation 
/ external stretching (NQ-253 §4.2 mechanisms B1/B2/B3).
(iv) CN15 sharpens CN6 by separating "kinetically determined" into static/dynamic 
readings. Commitment 16 K_field/K_act decomposition is the modeling-layer 
realization of CN15.

References: W4 OP-0001 F-1 SPLIT-RESOLVED (open_problems.md §OP-0001); 
canonical §13 T-Merge (b), T-PreObj-1, T-PreObj-1G; canonical §11.1 Commitment 16; 
working/MF/cn15_static_dynamic_separation.md (this file); 
working/MF/formation_birth_string_breaking.md §4.3 (Claim 4.3 noiseless-flow 
forbidding); working/MF/sigma_rich_augmentation.md §4 (Path B protocol-conditional 
inheritance).
```

---

## §4. Why register as CN, not Commitment or Theorem?

Three options were considered:

| Option | Pro | Con | Decision |
|---|---|---|---|
| (A) New Commitment 17 | Strong canonical anchor | Conflicts with already-proposed Commitment 17 (4-tool scaffolding) | **rejected** |
| (B) New theorem entry §13 | Mathematical content | CN15 is conceptual scope rule, not mathematical theorem | **rejected** |
| (C) New CN15 in §11.1 | Matches existing CN style; conceptual scope rule; ~50 lines | Adds another CN to already-long §11.1 list | **selected** |

CN15 is appropriately a **Conceptual Norm**: it constrains how theorems are interpreted, not what they say. The mathematical content (T-Merge (b), T-PreObj-1, NQ-253 Claim 4.3) is already canonical; CN15 only fixes the reading.

---

## §5. Hard constraint verification

- [x] **u_t primitive maintained**: CN15 is about reading multi-formation observables on $u_t$ field; primitive unchanged.
- [x] **CN10 contrastive throughout**: gauge-theoretic / stat-mech analogs that suggest static = dynamic are CN10 contrastive only.
- [x] **CN5 4-energy not merged**: CN15 distinguishes pure $\mathcal{E}_{\mathrm{bd}}$ from full $\mathcal{E}$, preserving 4-energy structure.
- [x] **K not abused**: $K_{\mathrm{step}}$ static, $K_{\mathrm{act}}$ dynamic, $K_{\mathrm{field}}$ architectural — Commitment 16 distinction preserved.
- [x] **OP not silently resolved**: OP-0001 F-1 SPLIT-RESOLVED status (W4) preserved; OP-0008 σ^A K-jump non-determinism preserved (CN15 does not resolve, only frames).
- [x] **No metastability claim without P-F flag**: CN15 references NQ-253 §4.2 mechanisms B1 (thermal, P-F flagged), B2 (IC), B3 (protocol) without making P-F claims.

---

## §6. CV-1.6 promotion path

**Promotion target:** canonical §11.1 (Conceptual Norms section) after CN14 (existing).

**Effort:** ~50 canonical lines + 3 cross-reference updates (CN6, Commitment 16, theorem_status.md).

**Counts impact:** none direct. CN15 is conceptual; theorem counts unchanged.

**Net effect at CV-1.6:**
- W4 OP-0001 F-1 SPLIT-RESOLVED gets formal canonical interpretive backdrop.
- W4 OP-0002 M-1 LAYER-CLARIFIED gets formal canonical interpretive backdrop.
- W4 Theorem 2-G (T-PreObj-1G) gets formal canonical interpretive backdrop.
- NQ-253 §4.3 Claim 4.3 gets formal canonical referent.
- sigma_rich_augmentation.md §4 protocol-conditional Path B gets formal canonical referent.

**Owner:** team-lead@scc-wave3-deep-research (this file). Final canonical merge at W6 Day 7 by CV-1.6 lead.

---

## §7. Cross-references

### §7.1 Canonical theorems referenced
- §13 T-Merge (b) Cat A — static $K_{\mathrm{step}} = 1$ on pure $\mathcal{E}_{\mathrm{bd}}$.
- §13 T-PreObj-1 + T-PreObj-1G — dynamic $\mathcal{F} \geq 2$ default on full $\mathcal{E}$.

### §7.2 Working files referenced
- `K_status_commitment.md` (OAT-1, Commitment 16 K-status K_field/K_act).
- `formation_birth_string_breaking.md` (NQ-253 §4.3 noiseless-flow forbidding).
- `sigma_rich_augmentation.md` (Path B protocol-conditional Φ_rich).
- `k_selection_mechanism.md` (in flight, OP-0005 K-Selection candidates respect CN15).

### §7.3 Open problems referenced
- OP-0001 F-1 SPLIT-RESOLVED (W4) — CN15 codifies the resolution principle.
- OP-0002 M-1 LAYER-CLARIFIED (W4) — CN15 codifies the clarification principle.
- OP-0008 σ^A K-jump non-determinism — CN15 establishes the framework for protocol-conditional K-jump dynamics.

---

**End of cn15_static_dynamic_separation.md.**

**Status:** CV-1.6 canonical §11.1 amendment proposal candidate. Cat A definitional. ~50 canonical lines. Promotion target: W6 Day 7 EOD with CV-1.6 packet. Net theorem-status counts: unchanged (CN, not theorem).
