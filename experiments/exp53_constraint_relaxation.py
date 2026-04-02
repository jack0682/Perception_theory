#!/usr/bin/env python3
"""Experiment 53: Progressive Constraint Relaxation.

Systematically relaxes constraints to find which ones are load-bearing
for multi-formation stability:

  Level 0: Fixed per-formation mass (current SCC) — baseline
  Level 1: Shared total mass, soft per-formation mass (mass transfer allowed)
  Level 2: Level 1 + reduced repulsion
  Level 3: Level 1 + no repulsion (only simplex barrier)
  Level 4: No repulsion, no simplex barrier (pure energy + shared mass)

For each level, tracks K(t) evolution and identifies:
  - When does the first merge/death happen?
  - What's the coarsening timescale?
  - Which formation dies first? (fitness selection)
"""
import sys, os, json, time
import numpy as np
from scipy import sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume
from scc.multi import formation_overlap


def evolve_relaxed(graph, params, K, total_mass, lambda_rep, lambda_bar,
                   mass_mode, max_iter, record_interval=10, rng=None):
    """Run K-field evolution with various constraint relaxation levels.

    mass_mode:
      'fixed': per-formation mass fixed (standard SCC)
      'shared': total mass fixed, per-formation mass free (soft redistribution)
      'free': no mass constraint (formations can grow/shrink freely)
    """
    if rng is None:
        rng = np.random.RandomState(42)

    n = graph.n
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    m_k = total_mass / K  # initial per-formation mass

    # Initialize K fields with spatial separation
    fields = []
    side = int(np.sqrt(n))
    for k in range(K):
        u = np.zeros(n)
        cx = side * (k + 0.5) / K
        cy = side / 2
        for i in range(side):
            for j in range(side):
                idx = i * side + j
                if idx < n:
                    d2 = (i - cx)**2 + (j - cy)**2
                    u[idx] = np.exp(-d2 / max((side / K)**2, 1.0))
        u = project_volume(u, m_k)
        fields.append(u)

    history = []
    dt = 0.01
    prev_gnorm = float('inf')
    death_threshold = 0.5  # formation "dies" if max(u) < this

    for tau in range(1, max_iter + 1):
        # Record
        if tau == 1 or tau % record_interval == 0:
            masses = [float(np.sum(f)) for f in fields]
            cores = [int(np.sum(f > 0.5)) for f in fields]
            peaks = [float(np.max(f)) for f in fields]
            energies_k = [float(ec.energy(f)[0]) for f in fields]

            alive = [k for k in range(K) if peaks[k] > death_threshold]

            # Total energy including interactions
            e_total = sum(energies_k)
            for j in range(K):
                for ki in range(j + 1, K):
                    e_total += lambda_rep * float(np.sum(fields[j] * fields[ki]))

            ovlp = formation_overlap(fields, theta_supp=0.1)
            max_ovlp = 0
            for j in range(K):
                for ki in range(j + 1, K):
                    max_ovlp = max(max_ovlp, int(ovlp[j, ki]))

            history.append({
                'iter': tau,
                'masses': masses,
                'cores': cores,
                'peaks': peaks,
                'energies': energies_k,
                'total_energy': e_total,
                'alive': len(alive),
                'alive_ids': alive,
                'max_overlap': max_ovlp,
            })

        # Gradient step
        max_gnorm = 0.0
        new_fields = []

        for k in range(K):
            # Self energy gradient
            g = ec.gradient(fields[k])

            # Repulsion
            if lambda_rep > 0:
                g_rep = lambda_rep * sum(fields[j] for j in range(K) if j != k)
                g += g_rep

            # Simplex barrier
            if lambda_bar > 0:
                S = sum(fields)
                violation = np.maximum(0.0, S - 1.0)
                g += lambda_bar * 2.0 * violation

            # Project gradient
            g_sigma = g - np.mean(g)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)

            # Step
            u_new = fields[k] - dt * g_sigma

            # Mass constraint
            if mass_mode == 'fixed':
                u_new = project_volume(u_new, m_k)
            elif mass_mode == 'shared':
                # Clip to [0,1], then rescale all fields jointly after loop
                u_new = np.clip(u_new, 0.0, 1.0)
            elif mass_mode == 'free':
                u_new = np.clip(u_new, 0.0, 1.0)

            new_fields.append(u_new)

        # Joint mass redistribution for 'shared' mode
        if mass_mode == 'shared':
            current_total = sum(float(np.sum(f)) for f in new_fields)
            if current_total > 1e-10:
                scale = total_mass / current_total
                new_fields = [f * scale for f in new_fields]
                # Re-clip after scaling
                new_fields = [np.clip(f, 0.0, 1.0) for f in new_fields]

        fields = new_fields

        # Adaptive step
        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt *= 0.7
            dt = max(dt, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt *= 1.05
            dt = min(dt, 0.1)
        prev_gnorm = max_gnorm

        if tau > 50 and max_gnorm < 1e-5:
            break

    return history, fields


def summarize(history, label):
    """Print compact evolution summary."""
    print(f"\n  [{label}]")
    print(f"  {'iter':>5} {'alive':>5} {'E':>8} {'masses':>35} {'peaks':>25}")

    steps = history[::max(1, len(history) // 12)]
    for h in steps:
        m_str = ','.join(f'{m:.1f}' for m in h['masses'])
        p_str = ','.join(f'{p:.2f}' for p in h['peaks'])
        print(f"  {h['iter']:5d} {h['alive']:5d} {h['total_energy']:8.1f} {m_str:>35} {p_str:>25}")

    # Detect transitions
    alive_seq = [h['alive'] for h in history]
    transitions = []
    for i in range(1, len(alive_seq)):
        if alive_seq[i] != alive_seq[i - 1]:
            transitions.append((history[i]['iter'], alive_seq[i - 1], alive_seq[i]))

    if transitions:
        print(f"  Transitions: {transitions}")
    else:
        print(f"  No transitions — K={alive_seq[-1]} stable throughout")

    return {
        'final_alive': alive_seq[-1],
        'transitions': transitions,
        'final_masses': history[-1]['masses'],
        'final_energy': history[-1]['total_energy'],
    }


def main():
    print("Experiment 53: Progressive Constraint Relaxation")
    print("=" * 70)
    t0 = time.time()

    graph = GraphState.grid_2d(10, 10)
    n = graph.n
    K = 4
    total_mass = 0.25 * n * K  # same total

    params = ParameterRegistry(
        a_cl=3.0, beta_bd=20.0, volume_fraction=0.25,
    )

    all_results = []

    levels = [
        # (label, mass_mode, lambda_rep, lambda_bar, description)
        ('L0: fixed mass + rep + simplex',     'fixed',  5.0, 50.0, 'Standard SCC (all constraints)'),
        ('L1: shared mass + rep + simplex',    'shared', 5.0, 50.0, 'Mass transfer allowed'),
        ('L2: shared mass + weak rep + simp',  'shared', 1.0, 50.0, 'Weak repulsion'),
        ('L3: shared mass + no rep + simplex', 'shared', 0.0, 50.0, 'No repulsion, simplex only'),
        ('L4: shared mass + no rep + no simp', 'shared', 0.0,  0.0, 'No repulsion, no simplex'),
        ('L5: free mass + no rep + no simp',   'free',   0.0,  0.0, 'Fully unconstrained'),
    ]

    for label, mass_mode, lrep, lbar, desc in levels:
        print(f"\n{'━' * 60}")
        print(f"  {label}")
        print(f"  {desc}")
        print(f"  mass={mass_mode}, λ_rep={lrep}, λ_bar={lbar}")

        history, fields = evolve_relaxed(
            graph, params, K=K, total_mass=total_mass,
            lambda_rep=lrep, lambda_bar=lbar,
            mass_mode=mass_mode, max_iter=3000,
            record_interval=20, rng=np.random.RandomState(42),
        )

        analysis = summarize(history, label)

        all_results.append({
            'label': label,
            'description': desc,
            'mass_mode': mass_mode,
            'lambda_rep': lrep,
            'lambda_bar': lbar,
            'history': history,
            'analysis': analysis,
        })

    # Also test on barbell and SBM
    print(f"\n{'━' * 60}")
    print(f"  === Topology tests (shared mass, no rep, no simplex) ===")

    topo_graphs = [
        ('barbell_6', lambda: make_barbell_graph(6, 0.01)),
        ('sbm_3x20', lambda: make_sbm_graph([20, 20, 20])),
    ]

    for topo_label, make_fn in topo_graphs:
        try:
            tg = make_fn()
            tn = tg.n
            tm = 0.25 * tn * K
            tp = ParameterRegistry(a_cl=3.0, beta_bd=15.0, volume_fraction=0.25)

            history, fields = evolve_relaxed(
                tg, tp, K=K, total_mass=tm,
                lambda_rep=0.0, lambda_bar=0.0,
                mass_mode='shared', max_iter=3000,
                record_interval=20, rng=np.random.RandomState(42),
            )
            analysis = summarize(history, f"L5-{topo_label}")
            all_results.append({
                'label': f'L5-{topo_label}', 'mass_mode': 'shared',
                'lambda_rep': 0.0, 'lambda_bar': 0.0,
                'history': history, 'analysis': analysis,
            })
        except Exception as e:
            print(f"  {topo_label} FAILED: {e}")

    # Final summary
    print(f"\n{'=' * 70}")
    print(f"CONSTRAINT RELAXATION SUMMARY")
    print(f"{'=' * 70}")
    print(f"{'Level':>45} {'K_final':>7} {'Transitions':>12} {'E_final':>10}")
    for r in all_results:
        n_trans = len(r['analysis']['transitions'])
        print(f"{r['label']:>45} {r['analysis']['final_alive']:>7} "
              f"{n_trans:>12} {r['analysis']['final_energy']:>10.1f}")

    # Key finding
    first_coarsen = None
    for r in all_results:
        if r['analysis']['final_alive'] < K:
            first_coarsen = r['label']
            break

    if first_coarsen:
        print(f"\n  First coarsening at: {first_coarsen}")
    else:
        print(f"\n  No coarsening observed at any level!")

    # Mass redistribution analysis
    print(f"\n  Mass redistribution (final state):")
    for r in all_results:
        masses = r['analysis']['final_masses']
        cv = np.std(masses) / max(np.mean(masses), 1e-10)  # coefficient of variation
        print(f"    {r['label']:>45}: masses=[{','.join(f'{m:.1f}' for m in masses)}] CV={cv:.3f}")

    # Save
    output = {
        'experiment': 'exp53_constraint_relaxation',
        'description': 'Progressive constraint relaxation for formation coarsening',
        'grid': '10x10', 'K': K,
        'results': all_results,
        'elapsed_seconds': time.time() - t0,
    }
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'results', 'exp53_constraint_relaxation.json')
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {outpath}")
    print(f"Total time: {time.time() - t0:.1f}s")


def make_barbell_graph(n_side, bridge_weight):
    g1 = GraphState.grid_2d(n_side, n_side)
    n1 = g1.n
    W = np.zeros((2*n1, 2*n1))
    W[:n1, :n1] = g1.W.toarray()
    W[n1:, n1:] = g1.W.toarray()
    mid1 = n1 - n_side//2
    mid2 = n1 + n_side//2
    W[mid1, mid2] = bridge_weight
    W[mid2, mid1] = bridge_weight
    return GraphState(sp.csr_matrix(W))


def make_sbm_graph(sizes, p_in=0.3, p_out=0.005):
    rng = np.random.RandomState(42)
    n = sum(sizes)
    W = np.zeros((n, n))
    for i, si in enumerate(sizes):
        for j, sj in enumerate(sizes):
            p = p_in if i == j else p_out
            ri, rj = sum(sizes[:i]), sum(sizes[:j])
            block = (rng.rand(si, sj) < p).astype(float)
            W[ri:ri+si, rj:rj+sj] = block
    W = (W + W.T) / 2
    np.fill_diagonal(W, 0)
    return GraphState(sp.csr_matrix(W))


if __name__ == '__main__':
    main()
