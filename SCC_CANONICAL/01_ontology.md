---
id: SCC-CT-CH-I
type: canonical/ontology
chapter: I
version: SCC-CT v0.1
sealed: 2026-05-14
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# I. Ontological Commitment

## §1. Two formal statements

The ontological commitment of SCC-CT is given by exactly two formal statements, in this order:

$$\boxed{\text{Object} \;\neq\; \text{primitive}}$$

$$\boxed{\text{Object} \;=\; \text{stable reading of a cohesion field}}$$

The first denies what most prior frameworks (object detection, segmentation, Bayesian object priors, Gestalt result patterns) implicitly assume. The second positions objecthood as an *output* of the formation process, not an input.

## §2. Ordering of pre-objective process

The ontological ordering of perceptual emergence in SCC-CT is:

```
sensory field
  → difference / contrast
  → boundary candidate
  → cohesive formation     ← THIS is the SCC-CT primitive domain
  → object candidate
  → label / class           ← outside SCC-CT scope
```

SCC-CT covers the arrow from *"difference"* through *"cohesive formation."* The transition from *"object candidate"* to *"label"* belongs to higher-level classification and is **out of scope**. This restriction is the canonical-level ontological choice; it is not a self-imposed limitation but a positive theoretical commitment.

## §3. The relational support

The pre-objective field is defined over a **relational support space**, not a pre-given object set.

A relational support $(X_t, R_t)$ at time $t$ is:
- $X_t$: a set of *relational loci* (graph vertices, sensory sites, abstract relational positions).
- $R_t$: relations defined on $X_t$ — primarily adjacency $\mathbf{N}_t$ and, derivatively, co-belonging $\mathbf{C}_t$ and distinction $\mathbf{D}_t$.

The individuation of $X_t$ is a *modeling choice at the implementation layer*, not an ontological commitment. The sites of $X_t$ are the substrate over which cohesion is defined — analogous to pixel grids in image analysis, with no commitment to pre-given visual objects.

Cf. `canonical.md §3.2` "Sensory or Relational Support" and §2 "Foundational Orientation."

## §4. The cohesion field

The cohesion field at time $t$ is:

$$u_t \;:\; X_t \to [0, 1]$$

$u_t(x)$ is the **degree of cohesive participation** at site $x$. This is:

- **Not** a posterior probability.
- **Not** a class membership score.
- **Not** a segmentation mask.
- **Not** a Bayesian object prior.

It is the **primary ontological entity** of SCC-CT. All further structure — closure, distinction, boundary, persistence — is *derived from* $u_t$, not from sets, labels, or pre-categorical objects.

The graded nature ($u_t \in [0, 1]$) is essential. Intermediate values (e.g., $u_t = 0.7$) are not "uncertain" — they represent the actual partial participation of a site in a forming cohesion. The graded field cannot be reduced to a Boolean partition; doing so would destroy the regime where most of the formation dynamics live (the boundary band $u \in (\theta_1, \theta_2)$).

## §5. Pre-objective formation

A **pre-objective formation** is a metastable structured solution of the four-term energy

$$\mathcal{E}(u) \;=\; \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}} \mathcal{E}_{\mathrm{bd}} + \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}$$

on the volume-constrained simplex $\Sigma_m = \{u \in [0, 1]^n : \mathbf{1}^\top u = m\}$, subject to the self-referential structure of the operator triad $(\mathrm{Cl}_t, \mathbf{D}_t, \mathbf{C}_t)$.

A *pre-objective* formation is one whose four diagnostic conditions (Bind, Sep, Inside, Persist) are jointly satisfied at a level robust to small perturbations — but *not yet labeled, classified, or named*.

## §6. Why "object" appears later

In SCC-CT, an **object** is not a primitive but a **stable reading** of a pre-objective formation. A formation $u^*$ admits an object reading when:

1. Its core $\{x : u^*(x) \geq \theta_{\mathrm{core}}\}$ is non-empty.
2. Its boundary band is a thin transition layer (per T-OP6-B Cat A: $d_H \leq 2\sqrt{\alpha/\beta}$).
3. Its temporal inheritance is verified (per T-Temporal-Identity Cat A).
4. The diagnostic vector $\mathbf{d}(u^*) \in [0,1]^4$ is high in all four components.

Even when these conditions hold, SCC-CT does not "produce an object" — it only certifies that a formation is *readable as one* under canonical thresholding. The label / class is supplied by an outer (non-SCC) classification process.

## §7. Comparison to prior frameworks

| Framework | Where it starts | Where SCC-CT differs |
|---|---|---|
| Object detection / segmentation | Discrete objects already given (as input data, ground truth, or prior). | SCC-CT operates *before* discreteness. Objects are output, not input. |
| Gestalt psychology | Describes *result patterns* (proximity, similarity, continuity, closure) of perceptual grouping. | SCC-CT provides the *mechanism* (closure operator + 4-term energy) that produces such patterns. Gestalt phenomena are predictions of SCC-CT, not its axioms. |
| Bayesian object inference | Object posteriors over pre-defined object hypotheses. | SCC-CT denies the pre-defined hypothesis space. The "object hypothesis" itself emerges from formation dynamics. |
| Predictive processing | Hierarchical prediction error minimization on pre-categorical features. | SCC-CT shares the prediction-error spirit (self-referential closure correction is analogous) but rejects pre-categorical feature dictionaries as primitives. |
| Allen-Cahn / Cahn-Hilliard PDE | Order parameter field; phase separation. | SCC-CT's Allen-Cahn-like $\mathcal{E}_{\mathrm{bd}}$ is *one of four* energy components. The other three (closure, separation, transport) are *self-referential* in ways pure phase-field models are not. |

## §8. Ontological consequences

From the ontological commitment, three consequences follow that constrain all further mathematical development of SCC-CT:

### §8.1 Self-referentiality is essential

The cohesion field $u_t$ does not have a fixed "ground truth" against which it is compared. It is evaluated by *its own induced structures*: the closure $\mathrm{Cl}(u)$ (self-completion), the distinction $\mathbf{D}(\cdot; 1-u)$ (self-contrast against self-induced exterior), and the co-belonging $\mathbf{C}_t$ (self-integration). This **self-referential evaluation** is not a methodological convenience — it is what makes the field "stand on its own" without external object labels.

### §8.2 The four-term energy cannot be merged

The four energy components $\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}, \mathcal{E}_{\mathrm{bd}}, \mathcal{E}_{\mathrm{tr}}$ are *conceptually independent*. They correspond to four distinct ontological requirements:

| Term | Ontological role |
|---|---|
| $\mathcal{E}_{\mathrm{cl}}$ | Self-support (the formation supports itself under closure). |
| $\mathcal{E}_{\mathrm{sep}}$ | Self-contrast (the formation is distinguishable from its exterior). |
| $\mathcal{E}_{\mathrm{bd}}$ | Self-articulation (the formation has a core-boundary-exterior morphology). |
| $\mathcal{E}_{\mathrm{tr}}$ | Self-continuation (the formation persists across time). |

Merging any two terms into one would collapse the corresponding ontological distinction. This is the **commitment note CN5** (canonical `canonical.md §14`), enforced as a structural rule.

### §8.3 Crisp recovery is one-way

Discrete (crisp) descriptions can be recovered from soft fields by thresholding:

$$A^\theta_t \;:=\; \{x \in X_t \;:\; u_t(x) \geq \theta\}.$$

The reverse — reconstructing $u_t$ from any crisp $A_t$ — is **not possible** without additional ontological commitment (i.e., assuming what $u_t$ might have been). Hence:

- *Forward direction (soft → crisp):* admitted, well-defined for any $\theta \in (0, 1)$.
- *Reverse direction (crisp → soft):* **not** part of SCC-CT.

This one-way relationship is what makes the soft field genuinely primitive: it carries *more information* than any crisp partition.

## §9. Cat A statements from CV-1.16 supporting this chapter

The ontological commitment of SCC-CT is supported by the following Cat A statements (registered in `THEORY/canonical/canonical.md` §13 Category A):

- **T-PreObj-1G** (graph-class independent Pre-Objective Mechanism, W4): the four-term energy admits formations on *generic* finite weighted graphs without requiring graph-symmetry assumptions. Hence pre-objective formation is graph-class robust.
- **T-Birth-Parametric** (D₄-symmetric case Cat A): explicit construction of formations on canonical graph families.
- **σ-framework supporting theorems (T-σ-Lemma-1/2/3, T-σ-Theorem-3)**: foundational σ-structure for formation-internal organization, decoupled from explicit object labels.

## §10. What is *not* committed in this chapter

The following are NOT canonical ontological commitments of SCC-CT, and remain *open* or *outside scope*:

- **Multi-formation ontology** (how multiple coexisting formations interact) — partially structured by Commitment 16 K-status, but the full multi-formation ontology is not sealed. See `05_open_problems.md` §OP-0009.
- **Continuous-time limit** of SCC dynamics — Γ-convergence to perimeter functional is Cat A (T11) but continuous-time *action* limit is open.
- **Observer / measurement** ontology — partially developed in `THEORY/canonical/canonical.md` Appendix OMS (Observer Moduli Space, OMS-2.0 Accepted Full), but its integration with the central cohesion-field commitment is structural, not deeply unified.
- **Cognitive vs. visual scope** — SCC-CT operates at the perceptual-formation level. Higher cognition (concept formation, language, reasoning) is outside scope.

---

*Chapter I sealed within SCC-CT v0.1. References: `THEORY/canonical/DECLARATION.md` (DECL-1.0, central axis); `THEORY/canonical/canonical.md` §2 (Foundational Orientation), §3.3 (soft cohesion field), §14 (CN1, CN4, CN5). Next: `02_axioms_and_primitives.md` (Ch. II Primitive Structure + Ch. III Operator Triad).*
