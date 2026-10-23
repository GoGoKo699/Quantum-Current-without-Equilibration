# Scalar current in a free-fermion network

An open network can have a very slowly decaying mode while its transmitted current is appreciable. Computing that one current need not require constructing the full steady state or resolving the slowest mode. The resource question here is how to estimate the current when the Hamiltonian and contacts have explicitly compiled reversible descriptions.

## Physical model and requested output

There are $`N`$ one-particle orbitals, a Hermitian one-particle Hamiltonian $`h`$, and diagonal nonnegative contact matrices $`\Gamma_L,\Gamma_R`$. Set

```math
\Gamma=\Gamma_L+\Gamma_R,\quad
A=-ih-\Gamma/2,\quad K(t)=e^{At},\quad
W=\operatorname{Tr}\Gamma_L>0.
```

Units have $`\hbar=1`$. Left contacts inject fermions into empty orbitals; right contacts extract them. These are energy-independent, fully occupied left and empty right Markovian reservoirs. With covariance convention $`C_{xy}=\langle c_y^\dagger c_x\rangle`$, the standard quadratic Lindblad equation gives

```math
\dot C=AC+CA^\dagger+\Gamma_L.
```

Starting from an empty network, the source-driven limiting covariance is

```math
C_L=\int_0^\infty K(t)\Gamma_LK(t)^\dagger\,dt.
```

The requested scalar is the current per bare injection rate,

```math
p_R=J_R/W,\qquad J_R=\operatorname{Tr}(\Gamma_R C_L).
```

An estimate $`\widehat p_R`$ must satisfy $`|\widehat p_R-p_R|\le\epsilon`$, with success probability at least $`2/3`$. The theorem covers $`0<\epsilon<1/4`$; larger error is trivial. Confidence amplification is charged logarithmically. For total-current error $`\eta`$, use $`\epsilon=\eta/W`$.

## Auxiliary absorption experiment

Prepare the one-particle mixed state $`\rho_L=\Gamma_L/W`$. Evolve it with no-jump propagator $`K(t)`$ and absorb at **both** contacts. The right-exit density and survival probability are

```math
f_R(t)=\operatorname{Tr}(\Gamma_R K(t)\rho_LK(t)^\dagger),\qquad
s(t)=\operatorname{Tr}(K(t)\rho_LK(t)^\dagger).
```

Then $`p_R=\int_0^\infty f_R(t)dt`$. This auxiliary process includes reflection into the left contact. Its initial preparation is an injection attempt, whereas successful injections in the many-fermion steady state are Pauli blocked. Thus $`p_R`$ is not a fraction of successfully injected physical particles that subsequently leave right. The [source-balance proof](source_balance.md) establishes normalization, current equivalence, and a finite mean exit time without requiring a positive global decay gap.

If constant contact occupations are $`n_L,n_R\in[0,1]`$, the source becomes $`n_L\Gamma_L+n_R\Gamma_R`$. On the dissipative sector the covariance is $`n_R I+(n_L-n_R)C_L`$, and the net current into the right reservoir is $`(n_L-n_R)Wp_R`$. General energy-resolved finite-temperature leads require a different reservoir model and its costs.

## Scientific route

1. [Source balance](source_balance.md): occupancy, dark sectors, mean residence, and exact discrete analogue.
2. [Coherent first-event circuits](first_event_compiler.md): short-time channel compilation, retained information, and inverse circuits.
3. [Estimation and charged resources](estimation.md): dyadic probability-sensitive variable-time estimation.
4. [Input and output costs](access_and_precision.md): procedural access, source preparation, and precision conversion.
5. [Examples and sharpness](examples.md): transmitting slow-mode witnesses and the restricted oracle lower bound.
6. [Matched comparison](comparison.md): classical certificates, steady-state solvers, physical signal precision, and quantum predecessors.

The attribution route is [related work](../references/RELATED_WORK.md). Numerical verification checks finite instances and circuit identities; the universal guarantee depends on the written proofs and imported algorithmic theorems.
