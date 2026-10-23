# Quantum Current without Equilibration

**Can a steady transport current be computed without waiting for the slowest mode to decay?** For a noninteracting fermion network with filled-source and empty-drain Markovian contacts, source balance bounds an auxiliary particle's mean residence time by the number of orbitals divided by the bare injection rate. This supports a quantum algorithm for one scalar current even with nonnormal dynamics, arbitrarily slow decay, or unreachable dark modes.

Let $`N`$ be the number of orbitals, $`W=\mathrm{Tr}\Gamma_L`$ the bare source rate, and $`p_R=J_R/W`$ the normalized right current. The central identities and charged estimation bound are

```math
\mathbb E\tau=\frac{\mathrm{Tr}C_L}{W}\le\frac NW,
\qquad
C_0+\widetilde O\!\left(
\frac{(aN/W)C_B+C_P}{\epsilon}
\right).
```

The algorithm estimates $`p_R`$ to additive error $`\epsilon`$. Here $`a`$ is the Hamiltonian-plus-loss block normalization, $`C_B`$ charges compiled access and interval operations, $`C_P`$ charges source preparation and its inverse, and $`C_0`$ charges setup. Controls, arithmetic, finite precision, coherent stopping and retained event work are included. Efficient access is supplied by explicit reversible circuits; no QRAM or free arbitrary data loading is assumed.

| Result | Scientific account |
|---|---|
| Source covariance, dark sectors, and finite mean residence | [Source balance](science/source_balance.md) |
| Short-time absorbing instrument and one reversible first-event record | [Coherent compiler](science/first_event_compiler.md) |
| Dyadic variable-time estimation with a full error budget | [Estimation theorem](science/estimation.md) |
| Input preparation, total-current precision, and workspace | [Charged access and accuracy](science/access_and_precision.md) |
| Analytic witnesses and matching dependence in a restricted step-oracle model | [Examples and oracle sharpness](science/examples.md) |
| Nonseparable local transmitting instances with slow side modes | [Local slab](science/local_slab.md) |
| Strong classical certificates, transport solvers, and physical signal accuracy | [Matched comparison](science/comparison.md) |

Start with the [physical model and scientific route](science/model.md). The [classical frequency estimator](science/frequency_sampling.md) supplies a finite-bit gap-independent comparison for uniform contacts. The [related-work account](references/RELATED_WORK.md) separates the inherited residence, simulation and estimation tools from the task-specific construction. The [LLM guide](llms.txt) maps questions to their authoritative files.

## Learn the project

The single educational anchor is **Breuer–Petruccione, *The Theory of Open Quantum Systems*** (original 2002; the linked publisher record is the 2007 paperback/online edition). The [source bridge](learning/BREUER_PETRUCCIONE_BRIDGE.md) connects its probability, master-equation and trajectory chapters to the specific source-balanced transport model, reversible first-event circuit and scalar estimator.

The [30-milestone map](learning/MILESTONES.md) has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. Each phase moves from local ingredients to the complete scientific story, with understanding targets, earlier dependencies and source pointers. The map is common to all readers; the [LLM guide](llms.txt) gives the same learning and proof routes.

## Reproduce the checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) explains the finite covariance, compact circuit, dark-sector and local-transport checks. These support the written arguments; they are neither a native-gate benchmark nor an asymptotic transport-scaling experiment.

## Scope and interpretation

The physical reservoirs have energy-independent occupations. The output is a current, and full steady-state preparation is not required. For absolute total-current error $`\eta`$, the leading propagation cost becomes $`\widetilde O(aNC_B/\eta)`$; for relative precision, the current size must also be charged.

The decay gap alone does not establish quantum advantage. Classical trajectory methods and Lyapunov or Green-function solvers can also avoid waiting for equilibration. The comparison gives a gap-independent classical current-error certificate and conditional size/precision estimates, without a universal classical lower bound or demonstrated hardware crossover. Source balance, Kraus compilation and variable-time estimation have established antecedents, credited in the scientific account.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
