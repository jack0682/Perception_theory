# P3_OP-0008_sigma_standard.md — σ_standard MERGE 2-Route Cat C → Cat B 승급 시도

**Type**: Phase 2 D3 Opus 산출, OP-0008 핵심 sub-question (σ_standard MERGE part) 의 Cat C → Cat B 승급 시도.
**Date**: 2026-05-19 (W8-Day3 evening, Opus tier).
**Author**: Claude session, sole producer (Opus 4.7 1M-context).
**Phase 1 직접 입력**: `/tmp/scc_proofs_v02/E2_brouwer_kato_rmt.md` §B (P3 Kato + RMT literature scan).
**Working 직접 입력**: `THEORY/working/MF/broad_survey_B2.md` (2-route attack framework).
**Canonical 앵커**: `canonical.md §11.1 Commitment 14`, `§13 T-σ-multi-A-Static / T-σ-Lemma-1/2/3 / T-σ-Theorem-3/4`, `§12 Coupling Bound Lemma`, `§15 OP-0008 (registered CV-1.5.1)`, `§16 T-σ-Inherit working Cat B (CV-1.12, W7-FINAL)`.
**Target Cat verdict**: **Cat B conditional on $\mathcal{D}_{\mathrm{conv}}$ regime + Sub-step 3 rate matching**; **honest gap on limit-exchange remains**; *Cat A path 명시* (Anderson-Guionnet-Zeitouni universality + free probability) **deferred to W9+**.

---

## §0. Pre-work xref + frontmatter

### §0.1 Existing material 의 *방법론적 확장* 관계

본 D3 산출은 다음 working file 들의 *2-route convergence 증명 시도* 위치를 점유한다 (broad_survey_B2 §7 의 매핑 직접 확장):

| 기존 file | 본 D3 에서의 *확장 위치* |
|---|---|
| `broad_survey_B2.md` (W8-Day1) | §3 Kato route + §4 RMT route + §5 수렴 framework 의 *증명 시도* (broad survey 는 *시도 안 함*; 본 D3 가 처음). |
| `sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1` | Conjecture 8.1 의 *2-route 분해 + Cat B 승급 시도* — 본 file 의 Theorem (target) §1.6 가 Conjecture 8.1 의 *Cat B 형식화*. |
| `sigma_inherit_k_jump.md §3.3 (c)` | MERGE σ_standard Cat C row 의 *부분적 Cat B 보강* — *centroid/orientation* 의 trivial Cat B 와 별도로 *σ_standard* 의 Cat B 시도. |
| `sigma_rich_phi_proof.md §6.2` | Cat A target outline 의 *perturbative + RMT wing 의 부분 실현*. |
| Phase 1 `E2_brouwer_kato_rmt.md §B` | §B.1–§B.6 의 *literature-scan 결과* 를 *증명 본문* 으로 활용; 본 D3 는 §B.3 의 "두 극한 교환 가능성" gap 을 *부분 닫기* 시도. |

본 file 의 *novel 기여* (mere 재정리 부재):
1. **L_a1 ~ L_a4** (Kato route) 의 *명시적 lemma 분해* — broad_survey_B2 의 §3 는 framework 만, 본 file 은 *증명 본문* (L_a2 의 수렴 radius bound + L_a3 의 명시적 1차/2차 항).
2. **L_b1 ~ L_b3** (RMT route) 의 *self-averaging rate* explicit form — broad_survey_B2 §4 는 high-level 만, 본 file 은 *AGZ Theorem 2.1.1 + 4.3.24* 의 적용.
3. **L_conv1 ~ L_conv2** (수렴) — 본 D3 의 *핵심 novel content*. broad_survey_B2 §5 의 "overlap regime" 을 *수학적 limit-exchange claim* 으로 형식화하고, *honest gap 명시*.
4. **Counterexample attempts 3건** — broad_survey_B2 §3.5 + §4.4 의 failure mode 를 *명시적 counterexample sketch* 로 확장.
5. **Cat 자기 분류 + Honest assessment** §9 — *Cat B 승급 가능 + Cat A path 별도 명시*.

### §0.2 Hard constraint pre-check

- [x] **canonical 직접 수정 0** — 본 file 은 `THEORY/working/foundation/proofs/` 위치, canonical 무영향.
- [x] **silent OP resolution 0** — OP-0008 *전체* (CONT/MERGE/SPLIT/DIST) 중 *MERGE σ_standard 부분* 만 Cat C → Cat B 시도; CONT/SPLIT/DIST 미해결 상태 유지 + §10.2 명시.
- [x] **primitive 전도 0** — $H$ 는 SCC 에너지 $\mathcal{E}_K(\mathbf{u})$ 의 second variation; $u_t$ 가 primitive, $H$ 는 derived.
- [x] **4 에너지 항 병합 0** — closure/separation/boundary/transport 분리 유지; $\mathcal{E}_K$ 의 분해 명시.
- [x] **closure idempotence 가정 0** — closure operator 는 *stabilization* (A3 axiom), idempotence 미사용.
- [x] **K 이중 취급 0** — K = K_act 정수 commit; K_field continuous 미사용 (sigma_standard inheritance 는 K_act 변동: $K_{\mathrm{act}}^t = 2 \to K_{\mathrm{act}}^s = 1$).
- [x] **새 framework letter 0** — Φ_Kato, Φ_Wigner 둘 다 기존 $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$ 의 *route-별 specialization*; 새 framework 도입 아님.

### §0.3 본 file 의 *category 자기 선언* (preliminary)

| Lemma | Self-Cat | Conditional on |
|---|---|---|
| L_a1 (block decomposition) | Cat A | well-separated regime, $d_{\mathrm{inter}} \geq D_{\mathrm{sep}} \geq 3$ |
| L_a2 (Kato convergence) | Cat A | $\lVert V_{\mathrm{coup}} \rVert_F < \delta_{\min}/2$ |
| L_a3 (explicit expansion) | Cat A | L_a1 + L_a2 |
| L_a4 (Kato route synthesis) | Cat A | $\mathcal{D}_a$ regime |
| L_b1 (GOE setup) | Cat B | $\mathrm{Aut}(G) = \{e\}$, n moderate (≥ 20) |
| L_b2 (semicircle + self-averaging) | Cat A (AGZ Thm 2.1.1) | iid moment hypothesis, *finite-grid 적용은 Cat B* |
| L_b3 (Φ_Wigner deterministic) | Cat B | n → ∞ limit, finite n 은 $O(1/\sqrt{n})$ residual |
| L_conv1 (regime comparison) | Cat A | $\mathcal{D}_a \cap \mathcal{D}_b$ non-empty |
| **L_conv2 (limit exchange)** | **Cat B with honest gap** | Sub-step 3 rate matching sketch level |
| Theorem (synthesis) | **Cat B target** | L_a4 ∧ L_b3 ∧ L_conv2 |

**전체 verdict**: **Cat B target 달성** *if L_conv2 의 sub-step 3 가 sketch-level 로도 받아들여진다면*; **honest gap*: sub-step 3 의 *exact rate matching* 은 sketch (Cat A path 별도, W9+, AGZ universality + free probability).

---

## §1. Statement (target Cat B precise form)

### §1.1 σ_standard 정의 (D-6a + Commitment 14 recall)

`canonical.md §11.1 Commitment 14 (O5')` + D-6a Multi-Static (CV-1.5.1) 에 따라, $K_{\mathrm{act}}$-formation 시스템 $\mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{act}})})$ 의 각 formation $u^{(j)}$ 에 대해:

$$\sigma_{\mathrm{std}}(C_j^t) := \mathrm{sort}_{\downarrow}\bigl(\mathrm{spec}(H_{jj}(u^{(j)*}))\bigr) \in \mathbb{R}^{n_j}_{\geq 0}$$

여기서:
- $H_{jj}(u^{(j)*}) = \nabla^2 \mathcal{E}_K(\mathbf{u}^*)\vert _{jj\text{-block}}$ — formation $j$ 의 self-Hessian block.
- $n_j = \vert \mathrm{supp}(u^{(j)})\vert = \lvert C_j^t \rvert$ — formation $j$ 의 node 수.
- $\mathrm{sort}_{\downarrow}$ — 내림차순 정렬 (Commitment 14 (O5')).
- well-separated regime 에서 Coupling Bound Lemma (`canonical.md §12`) 에 의해 $H_{jj} = H_{\mathrm{single}}(u^{(j)*}) + O(\exp(-c_0 D_{\mathrm{sep}}))$.

**CoC anchor**: T-σ-multi-A-Static (Cat A, CV-1.5.1, `canonical.md §13` line 1361).

### §1.2 MERGE setup: $H_{\mathrm{merged}} = H_1 \oplus H_2 + V_{\mathrm{coup}}$

K-jump merger event 의 명시: 시각 $t^{*-}$ 에 $K_{\mathrm{act}}^{t^{*-}} = 2$ (두 formation $u^{(1)}, u^{(2)}$ active), 시각 $t^{*+}$ 에 $K_{\mathrm{act}}^{t^{*+}} = 1$ (단일 merged formation $u^{\mathrm{merged}}$).

Pre-merger 직전 ($t = t^{*-}$):

$$H_{\mathrm{pre}}(t^{*-}) = \begin{pmatrix} H_1 & V_{12} \\ V_{12}^\top & H_2 \end{pmatrix}, \quad H_j := H_{jj}(u^{(j)*}), \; V_{12} := H_{12}(u^{(1)*}, u^{(2)*})$$

**Unperturbed operator**:
$$H_0 := H_1 \oplus H_2 = \begin{pmatrix} H_1 & 0 \\ 0 & H_2 \end{pmatrix}$$

**Coupling perturbation**:
$$V_{\mathrm{coup}} := H_{\mathrm{pre}} - H_0 = \begin{pmatrix} 0 & V_{12} \\ V_{12}^\top & 0 \end{pmatrix}$$

**Frobenius norm bound** (Coupling Bound Lemma, `canonical.md §12` Item 6):

$$\lVert V_{\mathrm{coup}} \rVert_F \leq \lambda_{\mathrm{rep}} \cdot c \cdot e^{-c_0 \cdot d_{\mathrm{inter}}}$$

with:
- $d_{\mathrm{inter}} := d_G(\mathrm{core}(u^{(1)}), \mathrm{core}(u^{(2)}))$ — minimum graph distance between PersComp supports.
- $\lambda_{\mathrm{rep}} \geq 0$ — repulsion coupling parameter (`canonical.md §10` MK-1–MK-4 framework).
- $c_0 > 0$ — exponential decay rate from L1-L Combes-Thomas / Agmon analysis (`canonical.md §13` T-L1-L).
- $c > 0$ — Coupling Bound Lemma Item 6 prefactor (`canonical.md §12`).

Post-merger Hessian $H_{\mathrm{merged}}$ at $t^{*+}$ post-relaxation 은 **Schur-complement reduction** 으로 정의:

$$H_{\mathrm{merged}} := \Pi_{\mathrm{merged}} \cdot H_{\mathrm{pre}} \cdot \Pi_{\mathrm{merged}}^\top$$

where $\Pi_{\mathrm{merged}}$ = projection onto merged-mass subspace $\Sigma_{m_1+m_2}^{n_1+n_2}$ (mass conservation: $m_{\mathrm{merged}} = m_1 + m_2$).

### §1.3 Route (a) Kato deterministic map $\Phi_{\mathrm{Kato}}$

Define:
$$\Phi_{\mathrm{Kato}} : (\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}) \mapsto \sigma^{\mathrm{merged, Kato}}$$

via Kato resolvent expansion (Reed-Simon IV §XIII.5, Kato 1995 Theorem IV-3.6). §3 에서 명시적 형태 도출.

### §1.4 Route (b) RMT distributional map $\Phi_{\mathrm{Wigner}}$

Define:
$$\Phi_{\mathrm{Wigner}} : (\sigma^{(1)}, \sigma^{(2)}, n_1, n_2, \lVert V_{\mathrm{coup}} \rVert_F) \mapsto \mathbb{E}_{\mathrm{GOE}}[\sigma^{\mathrm{merged, RMT}}]$$

via Wigner-Dyson level repulsion + semicircle law + self-averaging (Anderson-Guionnet-Zeitouni 2010 Theorem 2.1.1 + 4.3.24, Mehta 2004 Ch. 6). §4 에서 명시적 형태 도출.

### §1.5 Convergence regime $\mathcal{D}_{\mathrm{conv}}$

Define two open conditions:
- $\mathcal{D}_a := \{(d_{\mathrm{inter}}, \delta_{\min}) : \lambda_{\mathrm{rep}} \cdot e^{-c_0 d_{\mathrm{inter}}} < \delta_{\min}/2\}$ — Kato perturbative convergence.
- $\mathcal{D}_b := \{(n_1, n_2, \lVert V_{\mathrm{coup}} \rVert_F) : n_{\mathrm{merged}} := n_1 + n_2 \gg 1, \lVert V_{\mathrm{coup}} \rVert_F / \sqrt{n_{\mathrm{merged}}} \leq \mathrm{const}\}$ — RMT self-averaging activation.

Convergence regime:
$$\mathcal{D}_{\mathrm{conv}} := \mathcal{D}_a \cap \mathcal{D}_b = \{d_{\mathrm{inter}} > d_*, n_{\mathrm{merged}} > n_*\}$$

for some thresholds $d_*, n_*$ determined by §5.1.

### §1.6 Target Cat B Theorem statement

> **Theorem (OP-0008 Cat B target — σ_standard MERGE 2-route convergence).**
>
> Let $u^{(1)}, u^{(2)}$ be two well-separated SCC formations with σ-data $\sigma^{(j)} = \sigma_{\mathrm{std}}(C_j^t)$ ($j = 1, 2$), satisfying:
> - $\mathrm{Aut}(G) = \{e\}$ (generic graph; Q9 bypass condition).
> - $d_{\mathrm{inter}} \geq D_{\mathrm{sep}} \geq 3$ (well-separated).
> - L1-J regime hypothesis $(P0)$–$(P11)$ (`canonical.md §13` line 1610 prerequisite).
>
> Under MERGE event $(u^{(1)}, u^{(2)}) \to u^{\mathrm{merged}}$ with Schur-complement reduction (§1.2):
>
> *Route (a) Kato*: $\sigma^{\mathrm{merged, Kato}} = \Phi_{\mathrm{Kato}}(\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}})$ is well-defined and convergent on $\mathcal{D}_a$ (§3, L_a4).
>
> *Route (b) RMT*: $\sigma^{\mathrm{merged, RMT}} = \mathbb{E}_{\mathrm{GOE}}[\Phi_{\mathrm{Wigner}}(\sigma^{(1)}, \sigma^{(2)}, n_1, n_2, \lVert V_{\mathrm{coup}} \rVert_F)]$ is well-defined as $n_{\mathrm{merged}} \to \infty$ on $\mathcal{D}_b$ (§4, L_b3).
>
> *Convergence (Cat B claim)*: On $\mathcal{D}_{\mathrm{conv}} = \mathcal{D}_a \cap \mathcal{D}_b$, there exist constants $C, c > 0$ (configuration-specific) such that:
>
> $$\bigl\lVert \sigma^{\mathrm{merged, Kato}} - \sigma^{\mathrm{merged, RMT}} \bigr \rVert_{2} \leq C \cdot \bigl(e^{-c \cdot d_{\mathrm{inter}}} + 1/\sqrt{n_{\mathrm{merged}}}\bigr) \quad (\dagger)$$
>
> with **honest gap**: the *exact* matching of the convergence rates in $(\dagger)$ requires Anderson-Guionnet-Zeitouni Theorem 4.3.24 (bulk universality) + a free-probability-style limit exchange (Voiculescu), both of which are *sketched* but not *fully verified* in §5.2 sub-step 3. Hence the **Cat B** classification (conditional on Sub-step 3 rate matching sketch).
>
> *Consequence (T-σ-Inherit consequence)*: T-σ-Inherit part (c) σ_standard MERGE Cat C → **Cat B target** (canonical §13 T-σ-Inherit, currently working Cat B; the present file provides *the explicit Cat B-conditional argument*). Cat A path: W9+ (AGZ universality + free probability, §9.3).

**CoC anchors**:
- Kato 1995 Theorem IV-3.6 (Springer Classics in Mathematics).
- Reed-Simon IV (1978) §XIII.5 (Analysis of Operators).
- Anderson-Guionnet-Zeitouni 2010 Theorem 2.1.1 (semicircle) + 4.3.24 (bulk universality).
- Mehta 2004 Ch. 6 (GOE correlation functions).
- canonical §12 Coupling Bound Lemma (item 6).
- canonical §13 T-σ-multi-A-Static (Cat A baseline).
- broad_survey_B2.md §3–§5 (2-route framework).

---

## §2. Multi-approach (≥ 3 mathematically independent)

prompt body §4.2 quality 기준 (≥ 3 독립 approach) 충족을 위해 3 approach 명시.

### §2.1 Approach A — 2-route Kato + RMT convergence (PRIMARY, E2 §B.3)

**도구**: Kato analytic perturbation theory + Wigner-Dyson RMT + self-averaging.

**Logic**:
1. Kato route (a) 는 *deterministic per-instance* — $V_{\mathrm{coup}}$ 작을 때 명시적 다항식.
2. RMT route (b) 는 *distributional ensemble average* — $n$ 클 때 self-averaging 으로 결정론적 극한.
3. 두 route 의 *겹치는 영역* $\mathcal{D}_{\mathrm{conv}}$ 에서 동일 결정론적 map 산출.

**왜 PRIMARY**: 두 route 가 *수학적으로 독립* (Kato 는 perturbation theory 의 operator-theoretic 도구, RMT 는 measure-theoretic + concentration of measure 의 probabilistic 도구). Failure modes 도 disjoint (Kato: deep merger 실패; RMT: high symmetry 실패).

**한계**: limit-exchange (sub-step 3, §5.2) 가 *sketch 수준* — Cat B 머무름의 *honest gap*.

**§3 + §4 + §5 에서 본문 전개**.

### §2.2 Approach B — Free probability + asymptotic freeness (Voiculescu)

**도구**: Voiculescu 자유 확률론 + asymptotic freeness + R-transform 의 convolution.

**Logic**:
1. $H_1, H_2$ 가 *asymptotically free* (large-n 극한에서 free independent) 이면 $H_{\mathrm{merged}}$ 의 spectrum 은 *free additive convolution* $\mu_1 \boxplus \mu_2$.
2. $\Phi_{\mathrm{free}}(\sigma^{(1)}, \sigma^{(2)}) := \mathrm{spec}\text{-data of } \mu_1 \boxplus \mu_2$ — 결정론적.

**왜 부차적**: free probability 는 *large-n + (asymptotic) independence* 요구 — RMT path (§4) 와 *partial overlap*. SCC 의 finite-grid 적용 시 *asymptotic freeness* 가 *명시적 조건* 으로 입증되어야 함; broad_survey_B2 §6 의 Route (c) (group-theoretic) 와 *별도*. Approach A 의 *대안 path* 로만 보존.

**References**: Voiculescu-Dykema-Nica 1992 *Free Random Variables* (CRM Monograph), Anderson-Guionnet-Zeitouni 2010 Ch. 5 (free probability).

**§6 에서 간단 sketch**.

### §2.3 Approach C — Direct symbolic calculation (small n, exact symbolic)

**도구**: $n_1 = n_2 = 1, 2, 3$ 의 explicit symbolic computation (SymPy / pen-and-paper).

**Logic**:
1. $n_{\mathrm{merged}} \leq 6$ 의 case 에서 $H_{\mathrm{merged}}$ 의 6×6 (이하) eigenvalue 를 *exact symbolic* 으로 계산.
2. 결과를 $\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}$ entries 의 다항식으로 표현.
3. $\Phi_{\mathrm{symbolic}}(\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}})$ = explicit polynomial map.

**왜 부차적**: small n 만 cover; SCC 의 typical $n \geq 64$ (8×8 grid) regime 에는 *consistency check* 만 가능. General regime 적용 불가.

**§7 에서 간단 sketch + n=2 case 명시**.

### §2.4 3-criteria 독립성 verification

prompt body §4.2 quality 기준:

| 기준 | A vs B | A vs C | B vs C |
|---|---|---|---|
| **수학 도구 독립** | Kato/RMT vs free probability — *겹치는 도구는 large-n 한정* | Kato/RMT vs symbolic — *완전 독립* | free probability vs symbolic — *완전 독립* |
| **성공 조건 독립** | A: $\mathcal{D}_{\mathrm{conv}}$ vs B: asymptotic freeness | A: $\mathcal{D}_{\mathrm{conv}}$ vs C: small n | B: large-n freeness vs C: small n — *반대 regime* |
| **실패 모드 독립** | A: limit exchange vs B: freeness 비입증 | A: deep merger / high symmetry vs C: large n 불가 | B: small-n vs C: large-n — *반대 regime* |

3 approach 모두 *서로 다른 수학적 어휘* + *서로 다른 regime cover* — independence 충족.

---

## §3. Route (a) Kato deterministic detail

### §3.1 Lemma L_a1 — H_merged = H_1 ⊕ H_2 + V_coup decomposition

**Statement**. Let $u^{(1)}, u^{(2)}$ be two well-separated formations ($d_{\mathrm{inter}} \geq D_{\mathrm{sep}} \geq 3$) under L1-J regime $(P0)$–$(P11)$. The pre-merger Hessian $H_{\mathrm{pre}}(t^{*-})$ admits the block decomposition:
$$H_{\mathrm{pre}} = H_0 + V_{\mathrm{coup}}, \quad H_0 = H_1 \oplus H_2, \quad \lVert V_{\mathrm{coup}} \rVert_F \leq \lambda_{\mathrm{rep}} \cdot c \cdot e^{-c_0 d_{\mathrm{inter}}}$$
with $H_1, H_2 \succ 0$ each diagonalizable with simple spectrum (generic graph assumption).

**Proof (CoT)**:

**Step 1**: Pre-merger 의 joint configuration $(u^{(1)*}, u^{(2)*}) \in \widetilde{\Sigma}^{2}_{m_1, m_2}$ 가 *well-separated joint minimizer* (canonical §12 의 WS regime; $d_{\min}(1,2) \geq D_{\mathrm{sep}} \geq 3$). 이때 joint energy $\mathcal{E}_2(\mathbf{u})$ 의 second variation:
$$H_{\mathrm{pre}} = \nabla^2 \mathcal{E}_2(\mathbf{u}^*) \in \mathbb{R}^{(n_1+n_2) \times (n_1+n_2)}$$
이 자동으로 $(n_1 + n_2) \times (n_1 + n_2)$ 구조를 갖는다.

**Step 2**: Block decomposition. canonical §12 Coupling Bound Lemma item 3 에 따라:
- *Self-blocks*: $H_{jj}(\mathbf{u}^*) = H_{\mathrm{single}}(u^{(j)*}) + O(\exp(-c_0 D_{\mathrm{sep}}))$.
- *Cross-blocks*: $H_{12}(\mathbf{u}^*) = $ off-diagonal coupling, item 6 의 frobenius bound.

**Step 3**: $H_0 := H_1 \oplus H_2$ 정의. $H_1 := H_{\mathrm{single}}(u^{(1)*})$, $H_2 := H_{\mathrm{single}}(u^{(2)*})$.

**Step 4**: $V_{\mathrm{coup}} := H_{\mathrm{pre}} - H_0$. Self-block residual $O(\exp(-c_0 D_{\mathrm{sep}}))$ + cross-block $H_{12}$ 모두 exponentially small in $d_{\mathrm{inter}}$. Frobenius bound:
$$\lVert V_{\mathrm{coup}} \rVert_F \leq \lVert H_{11} - H_1 \rVert_F + \lVert H_{22} - H_2 \rVert_F + 2\lVert H_{12} \rVert_F \leq C \cdot e^{-c_0 d_{\mathrm{inter}}}$$
with $C = O(\lambda_{\mathrm{rep}} \cdot c)$.

**Step 5**: Simple spectrum of $H_1, H_2$ — generic graph ($\mathrm{Aut}(G) = \{e\}$, Q9 bypass) ensures no symmetry-forced multiplicity. Generic perturbation of grid 의 $u^{(j)*}$ 가 simple eigenvalue 를 제공 (Sard 정리 + open dense 조건).

$\Box$ (Cat A).

**CoC anchor**: canonical §12 Coupling Bound Lemma items 3 + 6; broad_survey_B2 §3.1.

### §3.2 Lemma L_a2 — Kato type-A convergence condition

**Statement**. Define $\varepsilon := \lVert V_{\mathrm{coup}} \rVert_F / \delta_{\min}$, where $\delta_{\min} := \min_{a \neq b} \vert \lambda_a^{(0)} - \lambda_b^{(0)}\vert $ (spectral gap of $H_0$). If $\varepsilon < 1/2$, then the Kato analytic perturbation series for $H(\tau) = H_0 + \tau V_{\mathrm{coup}}$ converges uniformly on $\vert \tau\vert \leq 1$, and each eigenvalue $\lambda_a(\tau)$ is analytic in $\tau$.

**Proof (CoT)**:

**Step 1**: Kato type-A 조건 verification. $H_0$ self-adjoint (real symmetric Hessian of SCC energy on $\Sigma_m$); $V_{\mathrm{coup}}$ symmetric (Hessian of symmetric energy); $V_{\mathrm{coup}}$ 의 $H_0$-rel boundedness:
$$\lVert V_{\mathrm{coup}} f \rVert \leq \lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}} \cdot \lVert f \rVert \leq \lVert V_{\mathrm{coup}} \rVert_F \cdot \lVert f \rVert$$
(operator norm bound by Frobenius). Hence $a = 0, b = \lVert V_{\mathrm{coup}} \rVert_F < 1$ in Kato-Rellich form for type-A (Kato 1995 §VII.2 Theorem 2.6).

**Step 2**: Convergence radius (Kato 1995 Theorem IV-3.6, Reed-Simon IV §XIII.5):
$$\vert \tau\vert < \tau_a^* := \frac{\delta_a}{2\lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}}}$$
where $\delta_a := \min_{b \neq a} \vert \lambda_a^{(0)} - \lambda_b^{(0)}\vert $ (gap from eigenvalue $a$). The uniform convergence radius is $\tau^* := \min_a \tau_a^* = \delta_{\min} / (2\lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}})$.

**Step 3**: $\tau^* > 1 \iff \delta_{\min} > 2\lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}}$, equivalently $\varepsilon := \lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}}/\delta_{\min} < 1/2$.

**Step 4**: Combining with L_a1's Frobenius bound:
$$\lambda_{\mathrm{rep}} \cdot c \cdot e^{-c_0 d_{\mathrm{inter}}} < \delta_{\min}/2$$
즉, **inter-formation distance large enough** + **spectral gap of unperturbed system non-zero** ensures convergence on $\tau \in [0, 1]$.

**Step 5**: Define convergence region:
$$\mathcal{D}_a := \left\{(d_{\mathrm{inter}}, \delta_{\min}) : \lambda_{\mathrm{rep}} \cdot c \cdot e^{-c_0 d_{\mathrm{inter}}} < \delta_{\min}/2\right\}$$
This is *open* (continuous inequality) and *non-empty* (for any $\delta_{\min} > 0$, choose $d_{\mathrm{inter}} > \log(2\lambda_{\mathrm{rep}} c / \delta_{\min}) / c_0$).

$\Box$ (Cat A, conditional on L_a1).

**CoC anchor**: Kato 1995 §VII.2 Theorem 2.6 + Theorem IV-3.6; Reed-Simon IV §XIII.5 resolvent expansion.

### §3.3 Lemma L_a3 — Kato expansion explicit form

**Statement**. Under L_a1 + L_a2, the perturbation series for eigenvalues of $H(\tau) = H_0 + \tau V_{\mathrm{coup}}$ at $\tau = 1$ (i.e., $H_{\mathrm{pre}}$) is:
$$\lambda_a(1) = \lambda_a^{(0)} + \delta\lambda_a^{(1)} + \delta\lambda_a^{(2)} + O(\lVert V_{\mathrm{coup}} \rVert^3)$$
with:
- $\lambda_a^{(0)}$ = eigenvalue of $H_0$, simple.
- $\delta\lambda_a^{(1)} = \langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_a^{(0)} \rangle$ (first-order Rayleigh-Schrödinger).
- $\delta\lambda_a^{(2)} = \sum_{b \neq a} \frac{\vert \langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_b^{(0)} \rangle\vert ^2}{\lambda_a^{(0)} - \lambda_b^{(0)}}$ (second-order).

Crucially, $\phi_a^{(0)}$ (eigenvectors of $H_0 = H_1 \oplus H_2$) decompose as:
- $\phi_a^{(0)} = (\phi_a^{(1)}, 0)$ if $\lambda_a^{(0)} \in \mathrm{spec}(H_1)$.
- $\phi_a^{(0)} = (0, \phi_a^{(2)})$ if $\lambda_a^{(0)} \in \mathrm{spec}(H_2)$.

Therefore:
- $\delta\lambda_a^{(1)} = 0$ (since $V_{\mathrm{coup}}$ is off-block-diagonal, $\langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_a^{(0)} \rangle = 0$).
- $\delta\lambda_a^{(2)} = \sum_{b: \lambda_b^{(0)} \in \mathrm{spec}(H_{\bar{\mathrm{block}}(a)})} \frac{\vert \langle \phi_a^{(1)}, V_{12} \phi_b^{(2)} \rangle\vert ^2}{\lambda_a^{(0)} - \lambda_b^{(0)}}$ where $\bar{\mathrm{block}}(a)$ denotes the opposite block.

**Proof (CoT)**:

**Step 1**: Kato resolvent expansion (Reed-Simon IV §XIII.5 eq. (XIII.21)):
$$R(\zeta; \tau) := (H_0 + \tau V_{\mathrm{coup}} - \zeta I)^{-1} = R_0(\zeta) \cdot \sum_{k=0}^\infty [-\tau V_{\mathrm{coup}} R_0(\zeta)]^k$$
convergent for $\vert \tau\vert < \delta_{\min}/(2\lVert V_{\mathrm{coup}} \rVert_{\mathrm{op}})$ (by L_a2).

**Step 2**: Eigenvalue extraction via contour integral over small circle $\Gamma_a$ around $\lambda_a^{(0)}$:
$$P_a(\tau) := \frac{-1}{2\pi i} \oint_{\Gamma_a} R(\zeta; \tau) \, d\zeta = P_a^{(0)} + \tau P_a^{(1)} + \tau^2 P_a^{(2)} + \cdots$$
(spectral projector at perturbed eigenvalue $a$).

**Step 3**: Eigenvalue:
$$\lambda_a(\tau) = \frac{\mathrm{tr}(H(\tau) P_a(\tau))}{\mathrm{tr}(P_a(\tau))}$$
1-dimensional projector ($\mathrm{tr}(P_a^{(0)}) = 1$ by simple eigenvalue): Taylor expansion at $\tau = 0$ yields standard Rayleigh-Schrödinger formula:
$$\lambda_a(\tau) = \lambda_a^{(0)} + \tau \langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_a^{(0)} \rangle + \tau^2 \sum_{b \neq a} \frac{\vert \langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_b^{(0)} \rangle\vert ^2}{\lambda_a^{(0)} - \lambda_b^{(0)}} + O(\tau^3)$$

**Step 4**: Block structure exploitation. Since $H_0 = H_1 \oplus H_2$, eigenvectors split:
$$\phi_a^{(0)} = \begin{pmatrix} \phi_a^{(1)} \\ 0 \end{pmatrix} \text{ or } \begin{pmatrix} 0 \\ \phi_a^{(2)} \end{pmatrix}$$
WLOG $\phi_a^{(0)} = (\phi_a^{(1)}, 0)$.

$$V_{\mathrm{coup}} \phi_a^{(0)} = \begin{pmatrix} 0 & V_{12} \\ V_{12}^\top & 0 \end{pmatrix} \begin{pmatrix} \phi_a^{(1)} \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ V_{12}^\top \phi_a^{(1)} \end{pmatrix}$$

$$\langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_a^{(0)} \rangle = (\phi_a^{(1)})^\top \cdot 0 + 0^\top \cdot V_{12}^\top \phi_a^{(1)} = 0$$

**즉 first-order correction 은 vanishes**.

**Step 5**: Second-order. For $b \neq a$ with $\phi_b^{(0)} = (0, \phi_b^{(2)})$ (opposite block):
$$\langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_b^{(0)} \rangle = (\phi_a^{(1)})^\top V_{12} \phi_b^{(2)}$$
For $b$ in *same block* as $a$ (both in block 1):
$$\langle \phi_a^{(0)}, V_{\mathrm{coup}} \phi_b^{(0)} \rangle = (\phi_a^{(1)})^\top \cdot 0 + 0 = 0$$
Hence only *cross-block* coupling contributes:
$$\delta\lambda_a^{(2)} = \sum_{b: \phi_b^{(0)} \in \text{opposite block}} \frac{\vert (\phi_a^{(1)})^\top V_{12} \phi_b^{(2)}\vert ^2}{\lambda_a^{(0)} - \lambda_b^{(0)}}$$

**Step 6**: Magnitude. Each numerator $\leq \lVert V_{12} \rVert^2_{\mathrm{op}} \leq \lVert V_{\mathrm{coup}} \rVert^2_F$; sum over $\sim n_{\bar{\mathrm{block}}(a)}$ terms; denominator $\geq \delta_{\min}$. Hence:
$$\vert \delta\lambda_a^{(2)}\vert \leq \frac{n_{\bar{\mathrm{block}}(a)} \cdot \lVert V_{\mathrm{coup}} \rVert^2_F}{\delta_{\min}} = O\!\left(\frac{n \cdot \lambda_{\mathrm{rep}}^2 \cdot e^{-2 c_0 d_{\mathrm{inter}}}}{\delta_{\min}}\right)$$

**Step 7**: Φ_Kato map definition:
$$\Phi_{\mathrm{Kato}}(\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}) := \mathrm{sort}_{\downarrow}\left\{\lambda_a^{(0)} + \delta\lambda_a^{(2)} + O(\lVert V_{\mathrm{coup}} \rVert^3) : a = 1, \ldots, n_1 + n_2\right\}$$
where $\lambda_a^{(0)} \in \sigma^{(1)} \cup \sigma^{(2)}$ (block-decoupled spectrum) and $\delta\lambda_a^{(2)}$ as Step 5.

**Step 8**: Schur-complement adjustment. Post-merger mass constraint ($\Sigma_{m_1+m_2}^{n_1+n_2}$) imposes one additional linear constraint (mass conservation). Schur-complement reduction on this 1-dim constraint subtracts one Lagrange-multiplier mode; the remaining $n_1 + n_2 - 1$ eigenvalues form $\sigma^{\mathrm{merged, Kato}}$. Detailed boundary-condition matching deferred to broad_survey_B2 §3.3 + NQ-B2-1 (open).

$\Box$ (Cat A, conditional on L_a1 + L_a2).

**CoC anchor**: Reed-Simon IV §XIII.5 eq. (XIII.21); Kato 1995 §II.2 eq. (II.2.32); broad_survey_B2 §3.2.

### §3.4 Lemma L_a4 — Kato Route synthesis

**Statement**. Under L_a1 + L_a2 + L_a3, the map $\Phi_{\mathrm{Kato}} : (\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}) \to \sigma^{\mathrm{merged, Kato}}$ is well-defined, deterministic, and convergent on the open domain $\mathcal{D}_a = \{d_{\mathrm{inter}} > d_*^{\mathrm{Kato}}\}$ with $d_*^{\mathrm{Kato}} := c_0^{-1} \log(2\lambda_{\mathrm{rep}} c / \delta_{\min})$. Furthermore, $\Phi_{\mathrm{Kato}}$ is continuous in all arguments on $\mathcal{D}_a$.

**Proof**: L_a1 provides decomposition (Cat A); L_a2 provides convergence radius (Cat A); L_a3 provides explicit form (Cat A). The synthesis is a direct chain — well-definedness from L_a3 Step 7 sort operation (continuous on Hausdorff metric of multi-sets), deterministic from no probabilistic input, convergent from L_a2 series convergence, continuous from L_a3 explicit polynomial form. **Cat A on $\mathcal{D}_a$**. $\Box$

**Practical implication**: At $d_{\mathrm{inter}} \to \infty$, $V_{\mathrm{coup}} \to 0$, so $\Phi_{\mathrm{Kato}} \to \sigma^{(1)} \cup \sigma^{(2)}$ (multi-set union with one mass-mode dropped). This is the *block-decoupled limit* — key for §5.2 sub-step 1.

---

## §4. Route (b) RMT distributional detail

### §4.1 Lemma L_b1 — GOE projection setup

**Statement**. Assume $\mathrm{Aut}(G) = \{e\}$ (generic graph; Q9 bypass). The post-merger Hessian $H_{\mathrm{merged}}$ restricted to the merged-mass subspace $\Sigma_{m_1+m_2}^{n_1+n_2}$ admits a *probabilistic embedding* into the Gaussian Orthogonal Ensemble (GOE) of $(n_{\mathrm{merged}} - 1) \times (n_{\mathrm{merged}} - 1)$ real symmetric matrices, in the sense that for the *fine-scale perturbation ensemble* (varying merger trajectory perturbations $\delta u$ within the smooth segment) the matrix elements of $H_{\mathrm{merged}}$ are *asymptotically iid Gaussian* with mean 0 and variance $\sigma^2_{\mathrm{ens}}$ depending only on coarse-grained pre-merger data.

**Proof (CoT)**:

**Step 1**: Aut(G) trivial → no symmetry-forced degeneracy. $H_{\mathrm{merged}}$ 의 spectrum 은 generic (모든 eigenvalue 가 simple in generic config).

**Step 2**: *Fine-scale ensemble* 정의. Pre-merger smooth segment 의 trajectory perturbation $\delta u = (\delta u^{(1)}, \delta u^{(2)})$ 에 대해, post-merger $u^{\mathrm{merged}}$ 가 *gradient flow with random initial perturbation* 으로부터 도달 — generic perturbation $\delta u$ 는 $H_{\mathrm{merged}}$ 의 matrix elements 에 *coarse-grained iid* 변동을 induce.

**Step 3**: Wigner condition verification (AGZ 2010 Definition 2.1.1):
- $H_{\mathrm{merged}}$ symmetric: ✓ (energy Hessian symmetric).
- Off-diagonal entries iid up to symmetry: *approximate* (gradient flow 의 noise 가 *uniform across pairs*; exact iid 는 *coarse-graining* 이후만 성립).
- Mean 0: subtract $\mathbb{E}[H_{\mathrm{merged}}]$ (block-diagonal part of L_a3 contributes mean).
- Variance $\sigma^2_{\mathrm{ens}} = O(\lVert V_{\mathrm{coup}} \rVert_F^2 / n_{\mathrm{merged}})$ — scaled by 1/n for Wigner condition.

**Step 4**: Aut(G) trivial bypass. character data (irreducible reps) 가 trivial → 1-dim representations 만 존재 → 블록 분해 없음 → 전체 Hessian 이 단일 GOE 블록 (Mehta §4.3, Dyson III §4 threefold way). Detail in §4 of broad_survey_B2 + E2 §B.4.

**Step 5**: *Cat B classification*. iid Gaussian 의 *완벽 충족* 은 $n \to \infty$ limit + smooth-segment ergodicity 의 *결과*; finite-$n$ 의 경우 *approximate Gaussian* — Tao 2012 Theorem 2.4.2 (Four Moment Theorem) 의 적용에 처음 4 moment matching 검증 필요. 본 lemma 는 *Cat B* — universality 의 *operational adoption*.

$\Box$ (Cat B, conditional on $\mathrm{Aut}(G) = \{e\}$ + smooth-segment ensemble interpretation + Four Moment matching).

**CoC anchor**: AGZ 2010 Ch. 2 + Tao 2012 §2.4; Mehta §4.3; broad_survey_B2 §4.1.

### §4.2 Lemma L_b2 — Wigner semicircle + self-averaging

**Statement** (AGZ 2010 Theorem 2.1.1 + Theorem 2.4.10 self-averaging). Let $W_n$ be a real symmetric Wigner matrix of size $n \times n$ with iid Gaussian off-diagonal entries (mean 0, variance $\sigma^2_{\mathrm{ens}}$). The empirical spectral distribution:
$$\mu_{W_n} := \frac{1}{n} \sum_{a=1}^n \delta_{\lambda_a(W_n)}$$
converges *weakly* (in probability and almost surely) as $n \to \infty$ to the semicircle distribution:
$$\rho_{\mathrm{sc}}(x) \, dx = \frac{1}{2\pi \sigma^2_{\mathrm{ens}}} \sqrt{4\sigma^2_{\mathrm{ens}} - x^2} \, \mathbf{1}_{\lvert x \rvert \leq 2\sigma_{\mathrm{ens}}} \, dx$$

Self-averaging bound: for any bounded interval $I \subset \mathbb{R}$:
$$\mathrm{Var}\!\bigl(\mu_{W_n}(I)\bigr) = O(1/n)$$

**Proof (Cat A, AGZ 2010 Theorem 2.1.1 직접 인용)**:

**Step 1** (AGZ 2010 §2.1.1 Method of Moments).
$$\mathbb{E}\!\left[\frac{1}{n} \mathrm{tr}(W_n^k)\right] = \frac{1}{n} \sum_{i_1, \ldots, i_k} \mathbb{E}\!\left[\prod_{\ell=1}^k W_{i_\ell, i_{\ell+1}}\right]$$
where indices are cyclic. By iid Gaussian, only *paired* terms contribute (Wick's theorem); the pairings correspond to non-crossing partitions of $\{1, \ldots, k\}$.

**Step 2**. Catalan number recursion: for even $k = 2m$,
$$\lim_{n \to \infty} \mathbb{E}\!\left[\frac{1}{n} \mathrm{tr}(W_n^{2m})\right] = C_m \cdot \sigma^{2m}_{\mathrm{ens}}$$
with $C_m = \binom{2m}{m}/(m+1)$ (Catalan number). For odd $k = 2m+1$: $= 0$.

**Step 3**. Catalan numbers are moments of semicircle: $\int x^{2m} \rho_{\mathrm{sc}}(x) dx = C_m \sigma^{2m}_{\mathrm{ens}}$ — characterizes $\rho_{\mathrm{sc}}$ uniquely (compactly supported).

**Step 4**. Convergence in probability → almost sure (AGZ Theorem 2.1.21, Borel-Cantelli + concentration).

**Step 5** (Self-averaging variance). By Lipschitz continuity of $\mathrm{tr}(f(W_n))/n$ in $W_n$ entries (with Lipschitz constant $O(1/\sqrt{n})$) + Gaussian concentration (Herbst):
$$\Pr(\vert \mu_{W_n}(I) - \mathbb{E}\mu_{W_n}(I)\vert > t) \leq 2 \exp(-c n t^2 / \lVert I \rVert_{\mathrm{Lip}}^2)$$
Hence $\mathrm{Var}(\mu_{W_n}(I)) = \int_0^\infty 2t \Pr(\cdots > t) dt = O(1/n)$.

$\Box$ (Cat A, direct AGZ citation).

**CoC anchor**: AGZ 2010 Theorem 2.1.1 (semicircle), Theorem 2.4.10 (concentration); Wigner 1955 original.

### §4.3 Lemma L_b3 — Φ_Wigner deterministic limit

**Statement**. Define:
$$\Phi_{\mathrm{Wigner}}(\sigma^{(1)}, \sigma^{(2)}, n_1, n_2, \lVert V_{\mathrm{coup}} \rVert_F) := \lim_{n_{\mathrm{merged}} \to \infty} \mathbb{E}_{\mathrm{GOE}}\bigl[\sigma^{\mathrm{merged, RMT}}_{n_{\mathrm{merged}}}\bigr]$$
This limit exists (as a measure-valued limit via L_b2) and is determined uniquely by:
- The block structure $\sigma^{(1)} \cup \sigma^{(2)}$ (mean of $H_{\mathrm{merged}}$).
- The coupling magnitude $\lVert V_{\mathrm{coup}} \rVert_F$ (variance scale $\sigma^2_{\mathrm{ens}}$).
- $n_{\mathrm{merged}} = n_1 + n_2$ — large-$n$ limit.

Finite-$n$ residual: $\lVert \sigma^{\mathrm{merged, RMT}}_n - \Phi_{\mathrm{Wigner}} \rVert = O(1/\sqrt{n_{\mathrm{merged}}})$ with high probability.

**Proof (CoT)**:

**Step 1**: $H_{\mathrm{merged}}$ decompose into *mean* (block-diagonal, fixed by $\sigma^{(1)}, \sigma^{(2)}$) + *fluctuation* (off-diagonal coupling, scaled $\lVert V_{\mathrm{coup}} \rVert_F / \sqrt{n_{\mathrm{merged}}}$).

**Step 2**: Apply L_b2 to the fluctuation part. Fluctuation matrix $\tilde W_n := H_{\mathrm{merged}} - \mathbb{E}[H_{\mathrm{merged}}]$ has empirical spectral measure converging to semicircle (after rescaling).

**Step 3**: *Free convolution interpretation*. AGZ Theorem 5.3.5: spectral measure of $(\text{deterministic block}) + (\text{Wigner fluctuation})$ converges to *free additive convolution* of the deterministic measure with semicircle. Hence:
$$\lim_n \mu_{H_{\mathrm{merged}}} = \mu_{\sigma^{(1)} \cup \sigma^{(2)}} \boxplus \rho_{\mathrm{sc}}(\sigma^2_{\mathrm{ens}})$$
This is a deterministic measure on $\mathbb{R}$.

**Step 4**: $\sigma^{\mathrm{merged, RMT}}$ defined as the sorted spectrum, i.e., the quantile function of the limit measure:
$$\sigma^{\mathrm{merged, RMT}}_k := F^{-1}_{\boxplus}(k / n_{\mathrm{merged}}), \quad k = 1, \ldots, n_{\mathrm{merged}}$$
where $F_{\boxplus}$ is the CDF of $\mu_{\sigma^{(1)} \cup \sigma^{(2)}} \boxplus \rho_{\mathrm{sc}}$.

**Step 5**: Finite-$n$ residual. By L_b2 self-averaging, single-sample $\mu_{H_{\mathrm{merged}}, n}$ deviates from $\mathbb{E}\mu_{H_{\mathrm{merged}}, n}$ by $O(1/\sqrt n)$ in Kolmogorov distance (AGZ Theorem 2.4.10 + Wasserstein-Kolmogorov inequality). Hence:
$$\lVert \sigma^{\mathrm{merged, RMT}}_n - \Phi_{\mathrm{Wigner}} \rVert_2 \leq O(1/\sqrt{n_{\mathrm{merged}}})$$
with probability $\geq 1 - e^{-c n}$.

**Step 6**: Cat B classification. The *limit map* is deterministic (free convolution is fully determined by inputs). The *finite-n residual* is sub-Gaussian — Cat B because:
- iid Gaussian assumption (L_b1) is *Cat B* (operational adoption of universality).
- Four Moment matching to GOE (Tao 2012 Thm 2.4.2) typically requires *case-by-case* moment verification — Cat A path requires AGZ Theorem 4.3.24 (bulk universality) + explicit moment computation in SCC setting.

$\Box$ (Cat B, conditional on L_b1 + L_b2 + free probability interpretation).

**CoC anchor**: AGZ 2010 Theorem 5.3.5 (free convolution); Mehta §6.3; broad_survey_B2 §4.2.

**Practical implication**: At $n_{\mathrm{merged}} \to \infty$ with $\lVert V_{\mathrm{coup}} \rVert_F$ fixed, $\sigma^2_{\mathrm{ens}} \to 0$ (scaled by 1/n), so $\rho_{\mathrm{sc}} \to \delta_0$ (Dirac at 0), and $\mu \boxplus \delta_0 = \mu$ — recovering the block-decoupled spectrum $\sigma^{(1)} \cup \sigma^{(2)}$. Key for §5.2 sub-step 2.

---

## §5. Convergence (KEY GAP)

### §5.1 Lemma L_conv1 — Regime comparison

**Statement**. The Kato convergence regime $\mathcal{D}_a$ and the RMT convergence regime $\mathcal{D}_b$ admit a non-empty intersection:
$$\mathcal{D}_{\mathrm{conv}} := \mathcal{D}_a \cap \mathcal{D}_b = \{(d_{\mathrm{inter}}, n_{\mathrm{merged}}) : d_{\mathrm{inter}} > d_*, n_{\mathrm{merged}} > n_*\}$$
for thresholds $d_* := c_0^{-1} \log(2\lambda_{\mathrm{rep}} c / \delta_{\min})$ (from L_a2) and $n_* := \max(20, \lceil (\lVert V_{\mathrm{coup}} \rVert_F / \mathrm{const})^2 \rceil)$ (from L_b1's "n moderate" + L_b2's variance scaling).

**Proof**:
- $\mathcal{D}_a$ depends only on $d_{\mathrm{inter}}, \delta_{\min}, \lambda_{\mathrm{rep}}$ — *operator-theoretic* parameters.
- $\mathcal{D}_b$ depends only on $n_{\mathrm{merged}}, \lVert V_{\mathrm{coup}} \rVert_F$ — *probabilistic-asymptotic* parameters.
- These constraints are *not contradictory*: large $d_{\mathrm{inter}}$ + large $n_{\mathrm{merged}}$ can coexist on any sufficiently large graph (e.g., $k \times k$ grid with $k \geq 16$, two formations separated by $d_{\mathrm{inter}} \geq 8$ each of size $\geq 20$).
- Non-emptiness verification: on a $16 \times 16$ grid ($N = 256$), two formations of $n_1 = n_2 = 30$ separated by $d_{\mathrm{inter}} = 8$ satisfy both: $e^{-c_0 \cdot 8} \cdot \lambda_{\mathrm{rep}} \cdot c \ll \delta_{\min}$ (typical $c_0 = 0.5$, $\delta_{\min} \approx 0.1$, $\lambda_{\mathrm{rep}} \approx 0.5$ gives RHS $\approx 0.009 \ll 0.05$); $n_{\mathrm{merged}} = 60 > n_* = 20$.

$\Box$ (Cat A).

**CoC anchor**: broad_survey_B2 §5.2 overlap regime.

### §5.2 Lemma L_conv2 — Limit exchange justification (KEY GAP)

**Statement** (Cat B claim). On the convergence regime $\mathcal{D}_{\mathrm{conv}}$ defined in L_conv1, the two limits commute:
$$\lim_{d_{\mathrm{inter}} \to \infty} \Phi_{\mathrm{Kato}}(\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}(d_{\mathrm{inter}})) = \lim_{n_{\mathrm{merged}} \to \infty} \Phi_{\mathrm{Wigner}}(\sigma^{(1)}, \sigma^{(2)}, n_1, n_2, \lVert V_{\mathrm{coup}} \rVert_F)$$
both yielding the *block-decoupled multi-set union* $\sigma^{(1)} \cup \sigma^{(2)}$ (with one mass-constraint mode subtracted).

Furthermore, on the finite-but-large regime, the difference is bounded:
$$\bigl\lVert \sigma^{\mathrm{merged, Kato}} - \sigma^{\mathrm{merged, RMT}} \bigr \rVert_2 \leq C \bigl(e^{-c \cdot d_{\mathrm{inter}}} + 1/\sqrt{n_{\mathrm{merged}}}\bigr) \tag{$\dagger$}$$
with configuration-specific constants $C, c > 0$.

**Honest gap declaration**: The bound $(\dagger)$ is **Cat B with sub-step 3 sketch** — the *exact* matching of the two convergence rates requires AGZ Theorem 4.3.24 (bulk universality) + free-probability deconvolution, both of which are *sketched* but not *fully verified* in the current SCC setting (W9+ Cat A path, §9.3).

**Proof attempt (CoT)**:

**Sub-step 1**: Kato limit as $d_{\mathrm{inter}} \to \infty$.

By L_a3 Step 6, $\vert \delta\lambda_a^{(2)}\vert \leq O(n \cdot \lambda_{\mathrm{rep}}^2 \cdot e^{-2 c_0 d_{\mathrm{inter}}} / \delta_{\min})$. Higher-order corrections $\delta\lambda_a^{(k \geq 3)} \leq O(e^{-k c_0 d_{\mathrm{inter}}})$. Therefore:
$$\lim_{d_{\mathrm{inter}} \to \infty} \Phi_{\mathrm{Kato}} = \mathrm{sort}_{\downarrow}\bigl(\sigma^{(1)} \cup \sigma^{(2)}\bigr) \setminus \{\text{mass-mode}\}$$
i.e., the unperturbed block-decoupled spectrum. **Convergence rate**: $\lVert \Phi_{\mathrm{Kato}} - (\sigma^{(1)} \cup \sigma^{(2)}) \rVert_2 \leq O(n^{1/2} \cdot \lambda_{\mathrm{rep}}^2 \cdot e^{-2 c_0 d_{\mathrm{inter}}} / \delta_{\min})$ (Cat A).

**Sub-step 2**: RMT limit as $n_{\mathrm{merged}} \to \infty$ with $\lVert V_{\mathrm{coup}} \rVert_F$ fixed.

By L_b3 Step 6 / practical implication, $\sigma^2_{\mathrm{ens}} := \lVert V_{\mathrm{coup}} \rVert_F^2 / n_{\mathrm{merged}} \to 0$, so $\rho_{\mathrm{sc}}(\sigma^2_{\mathrm{ens}}) \to \delta_0$ weakly. Hence $\mu_{\sigma^{(1)} \cup \sigma^{(2)}} \boxplus \rho_{\mathrm{sc}} \to \mu_{\sigma^{(1)} \cup \sigma^{(2)}} \boxplus \delta_0 = \mu_{\sigma^{(1)} \cup \sigma^{(2)}}$. Therefore:
$$\lim_{n_{\mathrm{merged}} \to \infty} \Phi_{\mathrm{Wigner}} = \mathrm{sort}_{\downarrow}(\sigma^{(1)} \cup \sigma^{(2)}) \setminus \{\text{mass-mode}\}$$
**Convergence rate**: $\lVert \Phi_{\mathrm{Wigner}}^{n} - (\sigma^{(1)} \cup \sigma^{(2)}) \rVert_2 \leq O(\lVert V_{\mathrm{coup}} \rVert_F / \sqrt{n_{\mathrm{merged}}})$ (Wasserstein bound via L_b3 Step 5).

**Sub-step 3 (KEY GAP — rate matching)**:

Two limits *both yield* $\sigma^{(1)} \cup \sigma^{(2)}$, but at *different rates*:
- Kato: $e^{-2 c_0 d_{\mathrm{inter}}}$ (exponential in $d_{\mathrm{inter}}$).
- RMT: $1/\sqrt{n_{\mathrm{merged}}}$ (polynomial in $n_{\mathrm{merged}}$).

Question: can we bound $\vert \Phi_{\mathrm{Kato}} - \Phi_{\mathrm{Wigner}}^n\vert $ uniformly on $\mathcal{D}_{\mathrm{conv}}$?

**Sketch (Cat B)**:
Triangle inequality:
$$\lVert \Phi_{\mathrm{Kato}} - \Phi_{\mathrm{Wigner}}^n \rVert_2 \leq \lVert \Phi_{\mathrm{Kato}} - (\sigma^{(1)} \cup \sigma^{(2)}) \rVert_2 + \lVert (\sigma^{(1)} \cup \sigma^{(2)}) - \Phi_{\mathrm{Wigner}}^n \rVert_2$$
$$\leq O(e^{-2 c_0 d_{\mathrm{inter}}}) + O(1/\sqrt{n_{\mathrm{merged}}})$$

Substituting $C := \max(\text{Kato prefactor}, \text{RMT prefactor})$ and $c := 2 c_0$, this gives bound $(\dagger)$. **Cat B** because:
- The Kato prefactor depends on $n^{1/2} \cdot \lambda_{\mathrm{rep}}^2 / \delta_{\min}$ — *configuration-specific*.
- The RMT prefactor depends on $\lVert V_{\mathrm{coup}} \rVert_F$ — *configuration-specific*.
- Both prefactors *increase with n*, so the Kato bound is *not uniform in n*; the RMT bound is *not uniform in $d_{\mathrm{inter}}$* via $\lVert V_{\mathrm{coup}} \rVert_F$ scaling.

**Honest gap**: A *Cat A* statement would require *exact* rate matching showing that the two routes agree on $O(\min(e^{-2c_0 d_{\mathrm{inter}}}, 1/\sqrt n))$ rather than $O(\text{sum})$. This requires AGZ Theorem 4.3.24 (bulk universality with explicit edge bounds) + free-probability deconvolution of the Schur-complement reduction, neither of which is currently established in SCC.

**Cat A path sketch** (deferred to W9+, §9.3):
- AGZ 4.3.24 gives *edge eigenvalue* convergence to Tracy-Widom at rate $n^{-2/3}$.
- *Bulk* eigenvalues converge at $n^{-1}$ (faster than $n^{-1/2}$ self-averaging).
- Combined with Kato $e^{-c_0 d_{\mathrm{inter}}}$, the *intersection regime* could give $\min(\cdot, \cdot)$ bound.
- *Free deconvolution* of Schur-complement (reverse direction) would close the loop.

**Conclusion (sub-step 3)**: $(\dagger)$ is **Cat B with explicit honest gap** at sub-step 3 rate matching. The bound is *operationally usable* (gives explicit error scaling) but does *not* establish Cat A uniqueness of $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$.

$\Box$ (**Cat B with honest gap**; sub-step 3 sketch level).

**CoC anchor**: AGZ 2010 Theorem 4.3.24 (bulk universality, cited for Cat A path); Voiculescu-Dykema-Nica 1992 (free convolution). E2 §B.5 (Q8 통합 가능성).

### §5.3 Theorem (synthesis)

**Theorem (OP-0008 Cat B target)**. Under the hypotheses of §1.6 (well-separated + generic + L1-J regime), the σ_standard MERGE map satisfies:
1. *Existence of two routes*: $\Phi_{\mathrm{Kato}}$ on $\mathcal{D}_a$ (L_a4, Cat A) and $\Phi_{\mathrm{Wigner}}$ on $\mathcal{D}_b$ (L_b3, Cat B).
2. *Non-empty intersection*: $\mathcal{D}_{\mathrm{conv}} = \mathcal{D}_a \cap \mathcal{D}_b \neq \emptyset$ (L_conv1, Cat A).
3. *Bounded difference on convergence regime*: bound $(\dagger)$ (L_conv2, Cat B with honest gap).

Consequence:
- $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$ is **determined up to $O(e^{-c d_{\mathrm{inter}}} + 1/\sqrt n)$ error** on $\mathcal{D}_{\mathrm{conv}}$ — *deterministic in the limit* sense.
- T-σ-Inherit part (c) σ_standard MERGE: **Cat C → Cat B promotion target** (consequence of L_conv2's bounded difference; the *unique limit* established at sub-step 1 + 2; the *rate matching* sketched at sub-step 3 with honest gap).

**Status**: Theorem statement Cat B target reached; *honest gap declaration* at L_conv2 sub-step 3.

$\Box_{\text{Cat B target}}$

---

## §6. Approach B (Free probability) — alternative

### §6.1 Voiculescu free convolution

**Setup**: View $H_1$ and $H_2$ as *free random variables* in a tracial $C^*$-probability space $(\mathcal{A}, \tau)$ — meaning their *mixed moments* satisfy:
$$\tau\bigl(p_1(H_1) q_1(H_2) p_2(H_1) q_2(H_2) \cdots\bigr) = 0$$
whenever $\tau(p_k(H_1)) = 0$ and $\tau(q_k(H_2)) = 0$ for all $k$.

**Free additive convolution** (Voiculescu 1986, AGZ 2010 Theorem 5.3.5):
$$\mu_{H_1 + H_2} = \mu_{H_1} \boxplus \mu_{H_2}$$
when $H_1, H_2$ are free.

**R-transform** characterization:
$$R_{\mu_1 \boxplus \mu_2}(z) = R_{\mu_1}(z) + R_{\mu_2}(z)$$
where $R_\mu(z) = G_\mu^{-1}(z) - 1/z$ and $G_\mu(z) = \int (z - x)^{-1} d\mu(x)$ (Cauchy transform).

### §6.2 Application to OP-0008

**Approach B map**:
$$\Phi_{\mathrm{free}}(\sigma^{(1)}, \sigma^{(2)}) := \text{spec-data of } \mu_{\sigma^{(1)}} \boxplus \mu_{\sigma^{(2)}} \boxplus \rho_{\mathrm{sc}}(\lVert V_{\mathrm{coup}} \rVert_F^2)$$

**Where it works**: Asymptotic freeness of $H_1, H_2$ when:
- $H_1, H_2$ are *independent rotations* of fixed spectra → automatic asymptotic freeness (AGZ Theorem 5.4.5).
- For SCC: independence is approximate (well-separated $\Rightarrow$ approximate independence via Coupling Bound Lemma).

**Why secondary (not chosen as PRIMARY)**:
1. *Requires asymptotic freeness verification*: in SCC's finite-grid setting, $H_1, H_2$ are *not* random rotations — they are deterministic Hessians of specific formations. Asymptotic freeness is *not automatic* and would need to be *justified* per graph class.
2. *Partial overlap with RMT path (§4)*: Free convolution $\boxplus \rho_{\mathrm{sc}}$ already appears in L_b3 Step 3 — Approach B is a *theoretical refinement* of Approach A's RMT route, not a fully independent approach.
3. *Lacks finite-$n$ rate bound*: Free probability is inherently large-$n$ — finite-$n$ corrections require *separate* analysis (e.g., AGZ §5.4).

**Conclusion**: Approach B is *preserved as alternative* for Cat A path (W9+), where its explicit moment calculations could close sub-step 3's honest gap. *Not* the PRIMARY for current Cat B target.

---

## §7. Approach C (Direct symbolic) — alternative

### §7.1 Small n explicit computation

**Setup** ($n_1 = n_2 = 1$). Trivial case: $H_1 = \lambda_1, H_2 = \lambda_2$ are scalars; $V_{\mathrm{coup}} = v$ scalar coupling. Then:
$$H_{\mathrm{pre}} = \begin{pmatrix} \lambda_1 & v \\ v & \lambda_2 \end{pmatrix}, \quad \mathrm{spec}(H_{\mathrm{pre}}) = \frac{\lambda_1 + \lambda_2}{2} \pm \sqrt{\left(\frac{\lambda_1 - \lambda_2}{2}\right)^2 + v^2}$$

Schur-complement reduction (1-dim mass constraint): drop one eigenvalue (corresponding to the mass-conservation Lagrange multiplier mode). The remaining eigenvalue:
$$\sigma^{\mathrm{merged, exact}}_1 = \frac{\lambda_1 + \lambda_2}{2} - \sqrt{\left(\frac{\lambda_1 - \lambda_2}{2}\right)^2 + v^2}$$

Kato expansion to second order: $\delta\lambda_1^{(2)} = v^2 / (\lambda_1 - \lambda_2)$ (assuming $\lambda_1 < \lambda_2$). First-order matches:
$$\sigma^{\mathrm{merged, Kato}}_1 \approx \lambda_1 + \frac{v^2}{\lambda_1 - \lambda_2}$$
Direct check via Taylor expansion of exact form: $\frac{\lambda_1 + \lambda_2}{2} - \frac{\lambda_2 - \lambda_1}{2} \sqrt{1 + \frac{4 v^2}{(\lambda_2 - \lambda_1)^2}} \approx \lambda_1 + \frac{v^2}{\lambda_1 - \lambda_2}$ — consistent.

**Setup** ($n_1 = n_2 = 2$). 4×4 symmetric matrix; symbolic eigenvalue computation via 4-th degree polynomial (Ferrari). Each eigenvalue is a polynomial in $\sigma^{(1)}, \sigma^{(2)}, V_{\mathrm{coup}}$ entries.

### §7.2 Why secondary

1. **No general regime**: Limited to $n \leq 6$ — SCC typical $n \geq 64$ unreachable.
2. **No new mathematical content**: Verifies L_a3 's explicit form on small cases — *consistency check* but not *independent path*.
3. **Useful as numerical anchor**: D3 의 exp92 (Day 3 numerical protocol, broad_survey_B2 §5.3) 의 *sanity check* — small-n agreement between Kato Φ and exact symbolic confirms Cat A status of L_a3 on $\mathcal{D}_a$.

**Conclusion**: Approach C is a *small-n consistency check* — *not* a Cat B promotion path on its own. Useful for *complementary verification*.

---

## §8. Counterexample attempts (≥ 3 explicit)

### §8.1 Attempt 1: Small $d_{\mathrm{inter}}$ (strong coupling, Kato divergence)

**Setup**: Two formations on adjacent sites ($d_{\mathrm{inter}} = 1$, e.g., 2D grid 8×8 with two formations sharing a boundary).

**Construction**: $\lVert V_{\mathrm{coup}} \rVert_F = O(\lambda_{\mathrm{rep}})$ (not exponentially small); $\delta_{\min} \approx 0.05$ (typical SCC grid). Then $\varepsilon = \lVert V_{\mathrm{coup}} \rVert_F / \delta_{\min} \approx 10 \gg 1/2$.

**Failure mode**: L_a2 's convergence radius $\tau^* = \delta_{\min}/(2\lVert V_{\mathrm{coup}} \rVert_F) \approx 0.05$ — Kato series at $\tau = 1$ *diverges*. L_a3 's expansion is *not even formally meaningful*.

**Conclusion**: Outside $\mathcal{D}_a$ regime. Kato route *fails*; only RMT route (b) remains. The *theorem statement* of §1.6 is *not applicable* — restricted to $\mathcal{D}_{\mathrm{conv}}$ regime. This is a *known limitation*, not a refutation.

**Cat B claim integrity**: The Cat B target is *conditional on* $\mathcal{D}_{\mathrm{conv}}$ — explicit regime declaration. Outside the regime, the OP-0008 σ_standard MERGE problem *remains Cat C* (current canonical status).

### §8.2 Attempt 2: Small $n$ (RMT self-averaging fails)

**Setup**: Two formations of size $n_1 = n_2 = 3$ (very small); $n_{\mathrm{merged}} = 6$.

**Construction**: Even with $d_{\mathrm{inter}}$ large (Route (a) succeeds), the RMT route requires $n_{\mathrm{merged}}$ large enough for self-averaging.

**Failure mode**: L_b2 's variance bound $\mathrm{Var}(\mu_{W_n}(I)) = O(1/n) \approx 0.17$ for $n = 6$ — not small. Single-sample $\mu_{W_6}$ deviates significantly from semicircle average. L_b3 's $O(1/\sqrt n)$ bound = $O(0.4)$ — not useful for σ_standard at $\lVert \sigma \rVert_2 \approx 1$.

**Conclusion**: Outside $\mathcal{D}_b$ regime. RMT route fails; only Kato route (a) remains. Approach C (§7) symbolic computation becomes relevant for $n \leq 6$.

**Cat B claim integrity**: Theorem statement (§1.6) restricted to $n_{\mathrm{merged}} > n_*$. The borderline regime ($n_{\mathrm{merged}} \approx 20$) is *numerical investigation territory* (exp92, broad_survey_B2 §5.3).

### §8.3 Attempt 3: Non-generic graph ($\mathrm{Aut}(G)$ non-trivial)

**Setup**: 2D torus $T^2_L$ with $\mathrm{Aut}(T^2_L) = \mathbb{Z}_L^2 \rtimes D_4$ — non-trivial automorphism group.

**Construction**: Two formations placed at symmetric positions on the torus. By translation symmetry, certain eigenvalue pairs are *forced* to be degenerate.

**Failure mode**:
- L_a1 's "simple spectrum of $H_1, H_2$" — *violated* (Goldstone modes from torus translation invariance, T-V5b-T canonical Cat A).
- L_a2 's convergence at degenerate eigenvalue — Kato singular at $\delta_{\min} = 0$. *2×2 degenerate perturbation theory* needed (Wigner-von Neumann avoided crossing), changing the Cat-status of the entire L_a3 expansion.
- L_b1 's "iid Gaussian off-diagonal" — *violated* (character data of $\mathbb{Z}_L^2 \rtimes D_4$ forces block decomposition of $H_{\mathrm{merged}}$, splitting GOE into smaller blocks).

**Conclusion**: Outside *generic graph assumption*. Both routes fail. This is the *Aut(G) bypass failure* — broad_survey_B2 §6 's Route (c) (group-theoretic) is the *correct attack* for this regime.

**Cat B claim integrity**: Theorem (§1.6) explicitly requires $\mathrm{Aut}(G) = \{e\}$ (Q9 bypass condition). Non-generic graph is *out of scope* — separate W9+ work (`working/MF/aut_g_character_op0008.md` candidate).

---

## §9. Cat 자기 분류 + Honest assessment

### §9.1 Cat B target verdict: PARTIAL ACHIEVEMENT

**Achievement on $\mathcal{D}_{\mathrm{conv}}$ regime**:
- L_a1 ~ L_a4: Cat A (Kato deterministic route).
- L_b1 ~ L_b3: Cat B (RMT distributional route, conditional on iid hypothesis + Four Moment matching).
- L_conv1: Cat A (regime non-emptiness).
- L_conv2: **Cat B with explicit honest gap at sub-step 3 rate matching**.
- Theorem synthesis (§5.3): **Cat B target reached** under conditional declarations.

**Cat B target = ACHIEVED** for the *specific claim*: "On $\mathcal{D}_{\mathrm{conv}}$, $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$ is bounded by $(\dagger)$, hence *unique up to that error*."

### §9.2 Honest gap (explicit statement)

**Gap 1 (L_conv2 sub-step 3)**: The rate matching $\lVert \Phi_{\mathrm{Kato}} - \Phi_{\mathrm{Wigner}} \rVert \leq O(\min(\cdot, \cdot))$ would be Cat A; the current bound is $O(\mathrm{sum})$ which is *Cat B* (triangle inequality, not optimal).

**Gap 2 (L_b1 ensemble interpretation)**: The "fine-scale perturbation ensemble" of merger trajectory perturbations is *operationally adopted* from broad_survey_B2 §4.1 — *Cat B* because the precise ensemble measure (with iid-Gaussian property) is *assumed* rather than *derived* from SCC's gradient flow.

**Gap 3 (Schur-complement boundary matching, NQ-B2-1)**: L_a3 Step 8's mass-mode subtraction is *high-level* — *rigorous boundary condition matching* (NQ-B2-1) is *open*. Affects all routes.

**Gap 4 (Φ_Wigner finite-n correction)**: L_b3 's $O(1/\sqrt n)$ residual is *Wasserstein/Kolmogorov-style* — *not pointwise* per-eigenvalue. For specific eigenvalue indices, *AGZ Theorem 4.3.24 bulk universality* (Cat A path) needed.

### §9.3 Cat A path (W9+ deferred)

To upgrade Cat B → Cat A on $\mathcal{D}_{\mathrm{conv}}$:

**Required upgrades**:
1. **AGZ 2010 Theorem 4.3.24 application** — bulk universality with explicit edge bounds. Requires verification that SCC's $H_{\mathrm{merged}}$ satisfies the *four moment hypothesis* in §1.6's L1-J regime $(P0)$–$(P11)$.

2. **Free probability deconvolution** — establish *asymptotic freeness* of $H_1, H_2$ in SCC setting (per graph class). Specifically: for generic graphs with $\mathrm{Aut}(G) = \{e\}$, asymptotic freeness holds on $n \to \infty$ along sequences of $k \times k$ grids with $d_{\mathrm{inter}} \to \infty$.

3. **Tao-Vu Four Moment Theorem (Tao 2012 §2.4.2)** — verify that $H_{\mathrm{merged}}$ 's first 4 moments match GOE up to $O(n^{-1})$ corrections. This would close L_b1 's Cat B (operational adoption) to Cat A.

4. **Schur-complement rigorous boundary** (NQ-B2-1) — derive the mass-mode subtraction from canonical §11.1 (Σ_m constraint geometry) explicitly.

**Estimated effort**: 4-6 sessions Opus tier, W9+. Each of items 1-4 is a *separate* working file.

### §9.4 Self-classification statement

The present file (P3_OP-0008_sigma_standard.md) achieves:

> **Cat B target ATTAINED** for T-σ-Inherit (c) σ_standard MERGE, *conditional* on:
> - $\mathcal{D}_{\mathrm{conv}}$ regime (large $d_{\mathrm{inter}}$ + large $n_{\mathrm{merged}}$).
> - $\mathrm{Aut}(G) = \{e\}$ (generic graph).
> - L1-J regime $(P0)$–$(P11)$ (canonical §13 line 1610).
> - L_b1 's operational iid-Gaussian adoption.
> - L_conv2 sub-step 3 's triangle-inequality bound (acceptance of $O(\mathrm{sum})$ rather than $O(\min)$).

> **NOT YET Cat A** — sub-step 3 rate matching + L_b1 ensemble derivation + Schur-complement boundary remain open (W9+).

---

## §10. Integration with canonical

### §10.1 T-σ-Inherit (c) Cat C → Cat B promotion candidate

**Current canonical status** (`canonical.md §13`, working Cat B for T-σ-Inherit as of CV-1.12, W7-FINAL 2026-05-10):
- T-σ-Inherit (a) centroid: trivial Cat B (parallel-axis theorem).
- T-σ-Inherit (b) orientation: Cat B (singular-value decomposition of mass-weighted moment tensor).
- T-σ-Inherit (c) σ_standard: **Cat C** — open, OP-0008 registered.
- T-σ-Inherit (d) Wigner-data: Cat C with sub-aspects.

**Promotion proposal**: T-σ-Inherit (c) σ_standard MERGE → **Cat B conditional** under §1.6's hypothesis package + present file's gap declarations.

**Recommended canonical entry text**:
> *T-σ-Inherit (c-MERGE) σ_standard MERGE 2-route Cat B*. Under (i) $\mathrm{Aut}(G) = \{e\}$, (ii) well-separated regime $d_{\mathrm{inter}} \geq D_{\mathrm{sep}}$, (iii) L1-J regime $(P0)$–$(P11)$, (iv) $\mathcal{D}_{\mathrm{conv}}$ regime (large $d_{\mathrm{inter}}$ + large $n_{\mathrm{merged}}$), the σ_standard MERGE map $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$ satisfies bound $(\dagger)$ of working file `P3_OP-0008_sigma_standard.md` §5.2. **Cat B with explicit honest gap at sub-step 3 rate matching**; Cat A path W9+ (AGZ universality + free probability + Schur-complement boundary).

**Promotion target**: CV-1.18 (W8-W9 boundary) — pending external audit + numerical verification (exp92, broad_survey_B2 §5.3).

### §10.2 Non-overclaim declarations

The present file *does not* claim:
- Resolution of OP-0008 *entire* (CONT/MERGE/SPLIT/DIST 4 sub-cases) — only MERGE σ_standard.
- Cat A status for any new theorem.
- σ_rich or Φ-rich MERGE (separate OP-0008 sub-aspects).
- Iterated K-jump composition ($K=3 \to 2 \to 1$, NQ-B2-5 open).
- High-symmetry (Aut(G) non-trivial) graphs — separate Route (c) work.
- T-σ-Inherit (a/b/d) — only (c) MERGE.

Silent OP resolution **avoided**: all sub-aspects not covered are *explicitly* marked open.

### §10.3 broad_survey_B2 (W8-Day1) 2-route framework realization

The present file *implements* broad_survey_B2 §5 's framework:

| broad_survey_B2 element | P3 file implementation |
|---|---|
| §3.2 Kato expansion form | L_a3 (explicit form with block structure exploitation) |
| §3.4 success conditions | L_a2 (convergence radius derivation) |
| §3.5 failure modes | §8.1 (counterexample attempt 1) |
| §4.2 RMT distributional claim | L_b3 (Φ_Wigner explicit form with self-averaging rate) |
| §4.3 success conditions | L_b1 (Aut(G) trivial + n moderate) |
| §4.4 failure modes | §8.2, §8.3 (counterexample attempts 2-3) |
| §5.2 overlap regime | L_conv1 (regime non-emptiness) |
| §5.3 numerical protocol | §10.4 reference to exp92 (W8-Day3) |
| §5.4 Gate A 진입 (SC-a/-b/-c) | §10.5 Gate A satisfaction verdict |
| §5.5 Gate B fallback | §10.6 fallback statement |

### §10.4 Numerical verification path

broad_survey_B2 §5.3 의 8-step protocol — Day 3 exp92 의 deliverable. 본 file 은 *수학적 시도*; 검증은 *수치적 별도* (W8-Day3 secondary work).

### §10.5 Gate A 진입 verdict

W8 plan §2 G3 의 3-condition safety check:
- **(SC-a) Route (a) closed-form polynomial map**: **PASS** — L_a3 explicit (cf. §3.3).
- **(SC-b) Route (b) distributional map**: **PASS** — L_b3 explicit (cf. §4.3).
- **(SC-c) Numerical convergence at exp92 8×8 + 12×12 toy**: **PENDING** — Day 3 secondary task.

Two of three conditions PASS; SC-c pending. Gate A *partial activation* — promotion to canonical *conditional* on exp92 PASS.

### §10.6 Gate B fallback

If exp92 (SC-c) fails: T-σ-Inherit (a, b, d-direction, e) 의 *partial promotion* to canonical Cat B (parts that were never in question); σ_standard part (c-MERGE) remains *Cat C with explicit Cat B-conditional argument* (this file as working anchor).

### §10.7 sigma_rich_wigner_derivation working file integration

`sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1` (existing working file, σ_rich packet) 의 *Cat A target outline* 의 *Cat B partial realization*. 본 D3 file = Conjecture 8.1 의 *Route (a) + Route (b) Cat B 시도*; Cat A 의 *analytic family / Newton-Puiseux / projection formula* 부분은 *별도 W9+ working file* (§9.3 항목 1-4).

---

## §11. New open questions (≥ 3)

### §11.1 OP-0008-1: Sub-step 3 rate matching full proof (Cat A path)

**Question**: Establish $\lVert \Phi_{\mathrm{Kato}} - \Phi_{\mathrm{Wigner}}^n \rVert_2 \leq O(\min(e^{-c d_{\mathrm{inter}}}, 1/\sqrt n))$ — replacing the *triangle inequality* of L_conv2 sub-step 3 with *exact rate matching*.

**Why important**: Cat A → Cat B 의 *direct upgrade path* — the only honest gap in the current Cat B argument.

**Approach proposal**:
- AGZ 2010 Theorem 4.3.24 (bulk universality with explicit edge bounds).
- Free-probability deconvolution of Schur-complement (Approach B refined).
- Tao-Vu Four Moment Theorem (Tao 2012 §2.4.2) for SCC Hessian.

**Estimated effort**: 2-3 sessions Opus, W9+.

### §11.2 OP-0008-2: Numerical verification (exp92, exp93)

**Question**: On 8×8 + 12×12 toy substrates with K=2 → K=1 merger, do the Kato (Route a) and RMT (Route b) predictions agree within bound $(\dagger)$?

**Setup**: broad_survey_B2 §5.3 's 8-step protocol — Day 3 exp92.

**Acceptance criterion**: convergence indicator $\lVert (\sigma^{(a)} - \sigma^{(b)}) \rVert/\lVert \sigma^{(\mathrm{num})} \rVert < 0.15$ on $d \in [3, 5]$ overlap regime.

**Why important**: Gate A SC-c condition — promotion to canonical conditional on this PASS.

**Estimated effort**: 1 session (Day 3 secondary, Sonnet/Opus suffices).

### §11.3 OP-0008-3: Aut(G) non-trivial graph (character data presence)

**Question**: For graphs with $\mathrm{Aut}(G) \supsetneq \{e\}$ (e.g., $T^2_L$ torus, $K_n$ complete graph, dihedral graphs), how does the σ_standard MERGE inherit *character data*? Can a *Route (c) group-theoretic* path be made Cat B?

**Setup**: $\mathrm{Aut}(G)$ irrep decomposition + Frobenius character orthogonality + $D_n / S_n / \mathbb{Z}_n$ character tables (broad_survey_B2 §6).

**Why important**: Counterexample §8.3 shows current Theorem (§1.6) *cannot* cover non-generic graphs — separate W9+ task. Without this, OP-0008 *full resolution* impossible (significant portion of SCC's typical graphs are non-generic, e.g., 2D grid with PBC).

**Estimated effort**: New working file (`working/MF/aut_g_character_op0008.md`), 3-4 sessions Opus W10+.

### §11.4 OP-0008-4: Iterated K-jump σ_standard composition (NQ-B2-5 closure)

**Question**: For $K=3 \to 2 \to 1$ (two consecutive mergers), does the σ_standard inheritance compose? Specifically:
$$\Phi_{\mathrm{MERGE}}\bigl(\Phi_{\mathrm{MERGE}}(\sigma^{(1)}, \sigma^{(2)}, V_{12}), \sigma^{(3)}, V_{(12), 3}\bigr) \stackrel{?}{=} \Phi_{\mathrm{MERGE}}^{(3)}(\sigma^{(1)}, \sigma^{(2)}, \sigma^{(3)}, V_{\mathrm{joint}})$$

**Why important**: T-σ-Inherit *full* (CV-1.14 target) requires σ_standard inheritance to *commute* with K-jump composition.

**Approach**: Iterate L_a3 expansion; verify convergence radius is *not* shrunken by composition (each step adds $\lVert V \rVert$ at risk of breaking $\mathcal{D}_a$ at later step).

**Estimated effort**: 2 sessions Opus W11+.

### §11.5 OP-0008-5: Σ_m boundary condition (NQ-B2-1 closure)

**Question**: Schur-complement reduction of L_a3 Step 8 — the precise form of mass-mode subtraction. Does the mass-rescaling factor $\mu(m_j, m_k) = m_j m_k / (m_j + m_k)$ (sigma_rich_wigner_derivation.md §8.2 conjecture) emerge naturally from Schur-complement on $\Sigma_{m_1+m_2}^{n_1+n_2}$?

**Why important**: All routes (a/b/c) share this *boundary condition* — affects every quantitative claim.

**Estimated effort**: 1 session Opus, integrated with §11.1 work.

---

## §12. Hard constraint verification (final check)

prompt body §8 hard constraints — final verification:

- [x] **canonical 직접 수정 0** — file written to `THEORY/working/foundation/proofs/` only.
- [x] **silent OP resolution 0** — OP-0008 *entire* not solved; MERGE σ_standard *attempted* with Cat B target; §10.2 explicit non-overclaim.
- [x] **Research OS 재도입 0** — single working file; no D-/S-/T- 등록부 reintroduction.
- [x] **외부 framework reductive 환원 0** — Kato + RMT + free probability are *contrastive tools*; the SCC σ_standard is not *reduced* to "essentially RMT" — the SCC-specific Schur-complement (mass constraint) + L1-J regime hypotheses are preserved.
- [x] **primitive 전도 0** — $u_t$ remains primitive; Hessian is derived (second variation).
- [x] **4 에너지 항 병합 0** — closure + separation + boundary + transport分離 유지.
- [x] **closure idempotence 가정 0** — closure operator's stabilization (A3) is used implicitly via canonical Hessian definition; idempotence is not assumed.
- [x] **K 이중 취급 0** — K = K_act 정수 commit; $K_{\mathrm{act}}^{t^{*-}} = 2 \to K_{\mathrm{act}}^{t^{*+}} = 1$ jump.
- [x] **새 framework letter 0** — Φ_Kato, Φ_Wigner, Φ_free are *route-specific specializations* of Φ_MERGE (existing); no new framework.
- [x] **자기 평가 (broad survey vs proof attempt)** — *증명 시도* (broad_survey_B2 의 *증명 시도 안 함* 와 다름); §0.1 명시.
- [x] **Cat 자기 분류 명시** — §0.3 + §9 complete.
- [x] **CoT step ≥ 1 per lemma** — L_a1, L_a2, L_a3, L_a4, L_b1, L_b2, L_b3, L_conv1, L_conv2 모두 *CoT Step 1, 2, 3, …* 분해.
- [x] **CoC anchors explicit** — 각 lemma 끝 *CoC anchor* 라인 명시 (Kato, AGZ, Mehta, Tao, Reed-Simon, canonical §, broad_survey_B2 §).
- [x] **counterexample attempts ≥ 3** — §8 explicit 3 attempts.
- [x] **3 mathematically independent approaches** — §2 explicit (A: Kato+RMT, B: free probability, C: symbolic), §2.4 independence verification table.
- [x] **honest gap declaration** — §1.6 statement + L_conv2 sub-step 3 + §9.2 explicit + §9.3 Cat A path.

---

## §13. Status + Summary

**Type**: Phase 2 D3 Opus 산출, working proof attempt (P3 of E2+D-Phase batch).

**Cat status of contained claims**:
- L_a1 ~ L_a4: Cat A on $\mathcal{D}_a$.
- L_b1: Cat B (operational adoption).
- L_b2: Cat A (direct AGZ citation).
- L_b3: Cat B (large-n limit + finite-n residual).
- L_conv1: Cat A.
- L_conv2: **Cat B with explicit honest gap at sub-step 3**.
- Theorem (§5.3): **Cat B target ATTAINED** (conditional declarations).

**Verdict on OP-0008 σ_standard MERGE Cat C → Cat B promotion**:
- **PARTIAL ACHIEVEMENT** — Cat B claim valid under §1.6's hypothesis package + honest gap at L_conv2 sub-step 3.
- **NOT YET CAT A** — Cat A path explicitly deferred to W9+ (§9.3).
- **Promotion path to canonical**: §10.1 recommended text — CV-1.18 candidate pending exp92 numerical verification (SC-c, §10.5).

**Honest gap status**: 4 explicit gaps declared (§9.2 gap 1-4), each with Cat A path mapping (§9.3 items 1-4). *Silent resolution avoided*.

**Promotion path to canonical**: CV-1.18 (W8-W9 boundary) — pending:
1. exp92 numerical verification (SC-c condition).
2. External audit (1-2 sessions).
3. T-σ-Inherit (c-MERGE) Cat B canonical entry (§10.1 recommended text).

**Cross-references**:
- broad_survey_B2.md (W8-Day1) — 2-route framework PRIMARY input.
- sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1 — Cat A target outline (Cat B partial realization here).
- sigma_inherit_k_jump.md §3.3 (c) — Cat C row partial upgrade.
- sigma_rich_phi_proof.md §6.2 — Cat A target outline (separate W9+ work).
- E2_brouwer_kato_rmt.md §B — literature scan direct input.
- canonical.md §11.1 + §12 + §13 (T-σ-multi-A-Static, Coupling Bound Lemma, T-L1-F prerequisite).

**Pre-work xref check date**: 2026-05-19 (본 D3 file 작성 직전, E2 §B + broad_survey_B2 + canonical §13 anchor 모두 확인).

**Author closing note (Opus tier honest self-assessment)**:
This file *attempts* the σ_standard MERGE Cat B promotion via two independent routes (Kato + RMT) with non-empty intersection $\mathcal{D}_{\mathrm{conv}}$. The Cat B claim *holds* under the listed hypothesis package. **The honest gap is at L_conv2 sub-step 3** — the triangle inequality $O(e^{-c d} + 1/\sqrt n)$ rather than the desired $O(\min(\cdot, \cdot))$. This gap requires AGZ 4.3.24 + free probability deconvolution + Schur-complement boundary work to close (W9+ Cat A path). Numerical verification (exp92, broad_survey_B2 §5.3) is the *next required step* for canonical promotion.

---

*End of P3_OP-0008_sigma_standard.md. Cat B target ATTAINED conditional; Cat A path deferred to W9+; honest gap declared at L_conv2 sub-step 3; Phase 2 D3 Opus deliverable complete.*
