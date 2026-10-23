# Examples, limits, and oracle sharpness

These examples separate a slowest decay rate, source-weighted residence, and the complexity of extracting a scalar current. The capacity theorem is [source balance](source_balance.md).

## A continuous-time near-dark example

Take real $`g`$ and

```math
h_g=\begin{pmatrix}0&1&g\\1&0&0\\g&0&0\end{pmatrix},
\quad
\Gamma_L=\mathrm{diag}(1,0,0),
\quad
\Gamma_R=\mathrm{diag}(0,1,0).
```

Here $`W=1`$. For every $`g\ne0`$, the full space is source reachable, all eigenvalues of $`A_g=-ih_g-(\Gamma_L+\Gamma_R)/2`$ have negative real part, and its source-driven covariance is

```math
C_L(g)=\frac1{5+2g^2}
\begin{pmatrix}
3+2g^2&i&0\\
-i&2&2g\\
0&2g&1+2g^2
\end{pmatrix}.
```

Direct substitution gives $`A_gC_L+C_LA_g^\dagger=-\Gamma_L`$. Therefore

```math
p_R(g)=\frac2{5+2g^2},
\qquad
\mathbb E\tau_g=\frac{6+4g^2}{5+2g^2},
\qquad(g\ne0).
```

The characteristic equation is

```math
\lambda\bigl[(\lambda+1/2)^2+1\bigr]
+g^2(\lambda+1/2)=0.
```

Its slow root satisfies $`\lambda_{\mathrm{slow}}=-2g^2/5+O(g^4)`$, so the slow population-decay rate is

```math
\Delta_g=-2\mathrm{Re}\lambda_{\mathrm{slow}}
=\frac45g^2+O(g^4).
```

The remaining eigenvalues approach $`-1/2\pm i`$. A slow right eigenvector, normalized to have third component one, has leading components $`(-2ig/5,-4g/5,1)`$. Since $`A_g`$ is complex symmetric, its spectral projection of the source $`|1\rangle`$ has coefficient $`-2ig/5+O(g^3)`$ along this vector. After the fast transient, the slow survival tail therefore has leading weight $`(4/25)g^2`$ and rate $`(4/5)g^2`$. Its contribution to the integrated residence tends to $`1/5`$. Thus an arbitrarily long lifetime tail coexists with bounded mean and nonzero limiting current.

At exactly $`g=0`$, the third site is a dark, unreachable mode. The source-driven covariance is selected by its time integral:

```math
C_L(0)=
\begin{pmatrix}
3/5&i/5&0\\
-i/5&2/5&0\\
0&0&0
\end{pmatrix},
\qquad
p_R(0)=\frac25,\qquad
\mathbb E\tau_0=1.
```

In particular,

```math
\lim_{g\to0,\ g\ne0}\mathbb E\tau_g=\frac65
\ne\mathbb E\tau_0.
```

The current is continuous, but the mean residence is not. The $`g\ne0`$ covariance formula must not be used at the exactly disconnected point: its limit contains an additional dark-site occupation $`1/5`$, whereas the source-driven integral at $`g=0`$ has none. This is a noncommutation of the infinite-time and zero-coupling limits, not a failure of the source-balanced bound.


## Bounded coefficients and long-lived barrier modes

A larger analytic witness uses an internal Hamiltonian $`H_{\rm int}`$ on $`m`$ sites and a distinguished contact projector $`P_0`$. On two copies let

```math
h=H_{\rm int}\otimes I_2+J P_0\otimes X,\quad
\Gamma_L=\gamma P_0\otimes|L\rangle\langle L|,\quad
\Gamma_R=\gamma P_0\otimes|R\rangle\langle R|.
```

If the contact is cyclic for $`H_{\rm int}`$, the full space is source reachable. Solving the two-mode contact problem gives a covariance $`C_2`$ with trace one. The exact full solution is $`C_L=I_m\otimes C_2`$: its internal commutator vanishes and every remaining term carries the same $`P_0`$. With $`N=2m`$ and $`W=\gamma`$,

```math
p_R=\frac{2J^2}{\gamma^2+4J^2},\qquad
\mathbb E\tau=\frac{m}{\gamma}=\frac{N}{2W}.
```

A chain with unit hoppings, contact and terminal onsite energies zero, and intervening barrier onsite energies five has bounded matrix entries and bounded norm at every size. At $`J=\gamma=1`$, the current fraction is exactly $`0.4`$, while a remote terminal produces a long-lived mode. In the [finite checks](../verification/README.md), increasing the barrier from one to seven sites decreases the resolved population-decay rate from $`2.33\times10^{-2}`$ to $`1.16\times10^{-10}`$. The mean grows only from three to nine.

The explicit covariance makes this an analytic mechanism witness and a useful conditioning check. Its simple answer supplies no computational hardness. The [nonseparable slab](local_slab.md) removes the mirror reduction in additional finite transmitting examples. Neither finite family proves a generic asymptotic diffusion law.

## Sharpness in the discrete step-oracle model

The dependence on mean residence time and additive precision is necessary in a black-box unitary-step model. This statement concerns the exact discrete absorption problem. It is not a lower bound for every explicitly described local transport problem or for every continuous-time Hamiltonian-access model.

### An explicit clock interferometer

Fix an integer $`L\ge4`$, set $`m=L-2`$, and use $`N=2L`$ one-particle basis modes $`|c,b\rangle`$ with clock $`c\in\{0,\ldots,L-1\}`$ and arm $`b\in\{0,1\}`$. Write

```math
H=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad P_\theta=\mathrm{diag}(1,e^{i\theta}).
```

Define the unitary step by

```math
U_\theta
=\sum_{c=0}^{L-1}|c+1\bmod L\rangle\langle c|
\otimes V_c(\theta),
```

```math
V_0=H,\qquad
V_c=P_\theta\quad(1\le c\le L-2),\qquad
V_{L-1}=H.
```

There are exactly $`m=L-2`$ phase applications in one circuit of the clock. The left and right ports are the two clock-zero modes:

```math
B_L=|0,0\rangle\langle0,0|,\qquad
B_R=|0,1\rangle\langle0,1|,\qquad
D=I-B_L-B_R.
```

Thus $`D^2=D`$, $`B_L+B_R=I-D^2`$, and $`A_\theta=DU_\theta`$ is the no-exit step. The source is $`\rho_{\mathrm{in}}=B_L`$ and $`W=\mathrm{Tr}B_L=1`$. As always for this step ordering, the measured exit effects are $`E_r=U_\theta^\dagger B_rU_\theta`$.

The particle starts at clock zero, is split by the first step, accumulates $`m`$ phases, and is recombined on its first return to clock zero. No intermediate clock value is absorbing. Therefore

```math
\tau=L\quad\text{with probability one},\qquad
\mathbb E\tau=L.
```

Just before final absorption the arm state is

```math
HP_\theta^mH|0\rangle
=\frac{1+e^{im\theta}}2|0\rangle
+\frac{1-e^{im\theta}}2|1\rangle,
```

and hence

```math
p_R(\theta)=\sin^2(m\theta/2).
```

The source-driven covariance is a sum of $`L`$ mutually orthogonal normalized states, one at each clock value. It has trace and rank $`L`$. The source-reachable dimension bound on mean residence is therefore attained exactly, while the ambient bound is $`N/W=2L=2\mathbb E\tau`$. In fact $`A_\theta^L=0`$: this witness does not rely on a small spectral decay gap.

### Query lower bound

Assume that $`\theta`$ is hidden in an oracle supplying $`U_\theta`$ and $`U_\theta^\dagger`$, including their controlled versions. The contact matrices and source preparation are known and independent of $`\theta`$. Arbitrary additional operations independent of the unknown parameter are allowed.

Suppose an algorithm estimates $`p_R`$ to additive error at most $`\epsilon`$ with probability at least $`2/3`$ on every input, where $`0<\epsilon\le1/8`$. Put

```math
a=\arcsin(4\epsilon),\qquad
\theta_\pm=\frac{\pi/2\pm a}{m}.
```

The two target probabilities are exactly

```math
p_R(\theta_\pm)=\frac12\pm2\epsilon.
```

Their $`\epsilon`$-accuracy intervals are disjoint. Comparing the estimate with $`1/2`$ distinguishes the two inputs with success at least $`2/3`$.

The clock blocks give

```math
\|U_{\theta_+}-U_{\theta_-}\|
=|e^{i\theta_+}-e^{i\theta_-}|
\le|\theta_+-\theta_-|
=\frac{2a}{m}.
```

Taking adjoints preserves this norm. Adding any control preserves the same bound, since the difference vanishes on the inactive control block. An oracle query that multiplexes forward and inverse calls also has a difference bounded by the maximum of the corresponding blocks. Thus inverses, coherent control, arbitrary input states and ancillas do not evade the bound.

A hybrid argument over $`Q`$ oracle calls bounds the Euclidean distance of final purified states, and therefore their trace distance, by $`2Qa/m`$. Intermediate measurements and adaptive choices can be deferred into coherent records, so the same conclusion applies to adaptive algorithms. Successful discrimination with probability $`2/3`$ requires final trace distance at least $`1/3`$. Consequently

```math
Q\ge\frac{m}{6a}
=\Omega\!\left(\frac{L}{\epsilon}\right)
=\Omega\!\left(\frac{\mathbb E\tau}{\epsilon}\right)
=\Omega\!\left(\frac{N/W}{\epsilon}\right).
```

For example, $`a\le8\epsilon`$ on the stated range gives the explicit bound $`Q\ge m/(48\epsilon)`$. The inequalities use only the telescoping hybrid method and the trace-distance characterization of discrimination. They remain true when every call has unit cost and all other gates are free.

A call to $`U_\theta^k`$ counts as $`k`$ step calls in this access model; a unit-cost arbitrary-power oracle is a different model. Likewise, an explicitly supplied numerical $`\theta`$ makes the displayed current formula elementary to evaluate. This example establishes query sharpness of the stopped-estimation dependence; it supplies neither a classical hardness result for explicit data nor a practical hardware advantage.

