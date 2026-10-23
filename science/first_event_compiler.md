# Coherent first-event circuits

The algorithm retains one first-event record while reusing each short-interval circuit's temporary work. The source and output model is in [the model](model.md); the resulting estimator is in [estimation](estimation.md).

## A short interval as a finite Kraus stack

Adjoin two orthogonal sink copies. Define

```math
J_r=\sum_x\sqrt{\gamma_r(x)}\,|r,x\rangle\langle x|,
\qquad J_r^\dagger J_r=\Gamma_r.
```

The Hamiltonian and jumps vanish on the sinks. This replacement preserves the
live no-jump evolution and total lead probabilities. It avoids a normalization
proportional to contact area: $`\|J_r\|^2\le\gamma_{\max}`$, whereas summing the
norms of separate site jumps would introduce an unnecessary factor.

For live input, the exact interval instrument has no-jump operator
$`K(\Delta)=e^{A\Delta}`$ and jump operators
$`J_rK(s)\sqrt{ds}`$, $`0\le s\le\Delta`$. The identity

```math
K(\Delta)^\dagger K(\Delta)
+\sum_r\int_0^\Delta K(s)^\dagger\Gamma_rK(s)\,ds=I
```

makes this a trace-preserving instrument. This identity uses the derivative
of $`K^\dagger K`$; the separate occupancy proof uses the derivative of
$`KK^\dagger`$.

Choose a positive $`q`$-node Gauss rule $`(s_\ell,w_\ell)`$ on the interval,
and a degree-$`d`$ Taylor polynomial $`P_d(s)`$ for $`e^{As}`$. Form

```math
M_0=P_d(\Delta),\qquad
M_{r\ell}=\sqrt{w_\ell}\,J_rP_d(s_\ell),\qquad
M=\begin{pmatrix}M_0\\M_{L1}\\\vdots\\M_{Rq}\end{pmatrix}.
```

Both $`q,d=O(\log(1/\eta))`$ suffice for diamond-norm instrument error
$`O(\eta)`$. To see that this estimate has no dimension factor, write
$`\mathcal L_0(X)=AX+XA^\dagger`$, so
$`\|\mathcal L_0\|_\diamond\le2a`$. Gauss exactness through degree $`2q-1`$,
positive weights summing to $`\Delta`$, and the exponential Taylor remainder
bound give jump-integral error at most

```math
O\!\left(\gamma_{\max}\Delta\, e^{2a\Delta}
\frac{(2a\Delta)^{2q}}{(2q)!}\right).
```

The uniform operator-norm Taylor remainder controls the no-jump operator and
the weighted stack of jump operators. The sum of squared weights is not needed:
$`\sum_\ell w_\ell=\Delta`$ bounds the stacked error. Consequently
$`\|M^\dagger M-I\|=O(\eta)`$.

Taylor LCU block-encodes $`P_d(s)`$ with normalization at most $`e^{as}`$.
The standard Kraus-stack construction therefore has squared normalization
bounded by

```math
\beta^2\le e^{2a\Delta}(1+2\gamma_{\max}\Delta)<4.
```

A known attenuation makes this normalization exactly 2. Kraus-index and
Taylor-index preparations have only polynomially logarithmic length. They can
be synthesized by direct multiplexed rotations; no quantum random-access
memory is required. All node, weight, coefficient and rotation computation is
charged to $`C_0`$ or the circuit's precision-dependent compilation cost.

One oblivious isometry-amplification step has accepted block

```math
F=\frac12M(3I-M^\dagger M).
```

Writing $`E=M^\dagger M-I`$ gives

```math
F^\dagger F=I-\tfrac34E^2+\tfrac14E^3.
```

Thus the rejected amplitude is $`O(\eta)`$, its probability is
$`O(\eta^2)`$, and the accepted lead-labelled instrument differs from the
desired one by $`O(\eta)`$ in diamond norm. The accepted no-jump row is still
the unique row with every segment-work register zero. Physical jump rows and
all numerical-failure rows have nonzero segment work. A numerical failure is
recorded as a stopped bad event, never silently reset or postselected away.

The stack construction and oblivious amplification are inherited primitives;
see Borras and Marvian, *Quantum simulation algorithms based on quantum trajectories*,
arXiv:2509.10425v2, Section 2.1, Lemmas 1–2 (themselves attributed there to Li and Wang). Their full trajectory algorithm's
constant-total-rate hypothesis is not used here. The polynomial identity above
also directly verifies the approximate-isometry case needed here.

## Reversible first-event memory

Let $`w`$ be the complete segment-work register, not only the physical Kraus
index. Introduce a record $`R=(R_t,R_e)`$, initialized to zero, where $`R_e`$
has the same size as $`w`$. At interval $`k`$, apply the segment unitary
controlled on $`R_t=0`$, then apply the permutation

```math
(0,0,b)\longleftrightarrow(k,b,0)\qquad(b\ne0)
```

on $`(R_t,R_e,w)`$. It fixes the live all-zero case and every earlier record.
This is a full reversible permutation, not a many-to-one erasure. An explicit
implementation is $`SXS`$: $`S`$ swaps $`R_e,w`$ when $`R_t=0`$, and $`X`$
interchanges time values 0 and $`k`$ when $`w=0`$, $`R_e\ne0`$.

On every reachable branch, $`w`$ is exactly zero after this permutation. A
stopped branch retains its system register, source-purification reference and
entire event-work label; later intervals fix it. In reverse order the same
permutation restores the event work and the inverse segment circuit restores
the preceding state. There is no irreversible reset, garbage deletion, or
fresh persistent environment register per interval.

With at most $`n_*`$ intervals, the extra record uses
$`O(\log n_*+b_{\rm work})`$ qubits, alongside one reusable
$`b_{\rm work}`$-qubit segment register. Taylor products may themselves require
$`O(d b_B)`$ block-encoding ancillas; these are included in
$`b_{\rm work}`$, rather than assumed free. A succinct input with
$`b_B=\mathrm{polylog}N`$ consequently has polynomially logarithmic
workspace. Source-purification qubits are additional and retained.

