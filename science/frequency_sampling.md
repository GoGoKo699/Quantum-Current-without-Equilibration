# A gap-independent classical current sampler

This construction estimates the same integrated Markov current as the [physical model](model.md). It supplies an explicit classical competitor whose accuracy does not depend on the original decay gap. Its sparse linear solves remain paid classical work; this is an upper bound for one algorithm, not an optimality claim.

## Assumptions and error allocation

Let $`h=h^\dagger`$ and let the disjoint diagonal contacts have the same rate $`\gamma>0`$ on $`r_L`$ left and $`r_R`$ right sites. Thus $`W=\gamma r_L`$ and $`S=N/W`$. Supply a justified bound $`H\ge\|h\|`$, counting its computation, and put $`b=H+\gamma`$. Uniform source-site sampling, coefficient evaluation and $`W`$ are charged. For bounded-degree procedural lattices a row-sum bound gives a suitable $`H`$ directly.

For $`0<\epsilon<1/4`$ and failure probability $`\zeta`$, choose

```math
\kappa=\frac{\epsilon}{8S},\qquad
R=H+\frac{4\gamma}{\pi\epsilon}.
```

The total error budget is $`\epsilon/4`$ each for auxiliary-loss bias, omitted energy tail, numerical/random-bit bias and sampling error. The auxiliary loss is an algorithmic regularization; the target has no added physical loss.

Define

```math
A_\kappa=-ih-\Gamma/2-\kappa I,\qquad
G_\kappa(E)=(EI-h+i\Gamma/2+i\kappa I)^{-1}.
```

The [residence bound](source_balance.md) gives

```math
p_\kappa=\mathbb E[e^{-2\kappa\tau}\mathbf1_R],\qquad
0\le p_R-p_\kappa\le2\kappa S=\epsilon/4.
```

Here $`\mathbf1_R`$ indicates right exit; the separate scalar $`R`$ is the energy cutoff. Every shifted solve is bounded by

```math
\|G_\kappa(E)\|\le1/\kappa,
```

because the imaginary part of its coefficient matrix is at least $`\kappa I`$. The original possibly tiny decay gap does not appear in this bound.

## Frequency identity and bounded samples

Entrywise Parseval applied to $`\mathbf1_{t\ge0}e^{A_\kappa t}\Gamma_L^{1/2}`$ gives

```math
p_\kappa=\frac1{2\pi W}\int_{-\infty}^{\infty}
\|\Gamma_R^{1/2}G_\kappa(E)\Gamma_L^{1/2}\|_F^2\,dE.
```

With a uniformly sampled left contact $`x`$, write

```math
F_x(E)=\|\Gamma_R^{1/2}G_\kappa(E)|x\rangle\|^2,\qquad
p_\kappa=\mathbb E_x\int\frac{F_x(E)}{2\pi}\,dE.
```

Introduce the Cauchy density $`q_b(E)=b/[\pi(E^2+b^2)]`$. The exact-real random variable

```math
Y=\frac{F_x(E)}{2\pi q_b(E)}
 =\frac{E^2+b^2}{2b}F_x(E),\qquad E\sim q_b,
```

has mean $`p_\kappa`$ and obeys

```math
0\le Y\le B_0:=\frac{5b}{2\gamma}.
```

To prove the bound, include the contact channels and the auxiliary loss in a matrix $`B`$ with $`BB^\dagger=\Gamma+2\kappa I`$. The identity $`G_\kappa-G_\kappa^\dagger=-iG_\kappa BB^\dagger G_\kappa^\dagger`$ makes $`I-iB^\dagger G_\kappa B`$ unitary. Its physical left-to-right subblock is a contraction, so $`\gamma F_x(E)\le1`$. Independently, for $`|E|>H`$, the real part of the shifted quadratic form gives

```math
F_x(E)\le\frac{\gamma}{(|E|-H)^2}.
```

For $`|E|\le2b`$ the contraction bound gives $`Y\le5b/(2\gamma)`$. For $`|E|>2b`$, $`|E|-H\ge|E|/2`$ gives $`Y\le5\gamma/(2b)\le B_0`$.

The omitted tail is controlled without locating narrow resonances:

```math
\mathbb E_x\int_{|E|>R}\frac{F_x(E)}{2\pi}\,dE
\le\frac{\gamma}{\pi(R-H)}=\epsilon/4.
```

For finite sampling, set $`a_R=\arctan(R/b)`$ and $`Z_R=2a_R/\pi`$. Draw $`u`$ uniformly on $`[-a_R,a_R]`$, set $`E=b\tan u`$, and return

```math
Y_R=Z_R\frac{E^2+b^2}{2b}F_x(E).
```

Its expectation is the truncated integral and $`0\le Y_R\le B_0`$. This conditional Cauchy sampling spends no samples on the omitted tail.

## Finite random bits and numerical tolerances

The following conservative tolerances turn the real-arithmetic construction into a finite algorithm. Differentiating the resolvent gives

```math
G_\kappa'=-G_\kappa^2,\qquad
|F_x'|\le2\gamma/\kappa^3,
```

and a valid derivative bound on $`[-R,R]`$ is

```math
\left|\frac{dY_R}{dE}\right|\le
M_R:=\frac{\gamma}{b}
\left(\frac{R^2+b^2}{\kappa^3}+\frac{R}{\kappa^2}\right).
```

Represent $`u`$ by the midpoint of one of $`2^k`$ equally likely bins. Since $`dE/du\le(R^2+b^2)/b`$, coupling the continuous and midpoint draws gives

```math
|\Delta E|\le\frac{\pi(R^2+b^2)}{2b}\,2^{-k}.
```

It suffices to choose $`2^k\ge8\pi M_R(R^2+b^2)/(b\epsilon)`$, which contributes at most $`\epsilon/16`$ bias. Evaluate the angle, tangent and resulting energy with additional absolute energy error at most $`\epsilon/(16M_R)`$, and clamp the result to $`[-R,R]`$. This adds at most $`\epsilon/16`$. Thus energy discretization and evaluation consume at most $`\epsilon/8`$.

For a shifted solve $`z=G_\kappa(E)|x\rangle`$, a computed $`\widetilde z`$ with $`\|\widetilde z-z\|\le e`$ satisfies

```math
\left|\|\Gamma_R^{1/2}\widetilde z\|^2-F_x(E)\right|
\le\gamma(2e/\kappa+e^2).
```

The sufficient tolerance

```math
e\le\min\left\{\frac1\kappa,
\frac{\epsilon b\kappa}{32\gamma(R^2+b^2)}\right\}
```

therefore changes $`Y_R`$ by less than $`\epsilon/16`$. Certify it by a linear-system residual norm at most $`\kappa e`$. This follows directly from $`\|G_\kappa\|\le1/\kappa`$ and does not use the original gap. Coefficient and residual evaluation errors must be included in that certified residual budget.

Reserve the remaining $`\epsilon/16`$ numerical bias as follows. Uniform source-site rejection sampling from a power-of-two range accepts with probability greater than $`1/2`$; limit it to $`t\ge\lceil\log_2(64B_0/\epsilon)\rceil`$ attempts, returning zero upon failure. The failure bias is at most $`\epsilon/64`$. Compute $`Z_R`$ to absolute error at most $`\epsilon/[64(B_0+1)]`$, reserving another $`\epsilon/64`$. Evaluate contact norms, the scalar prefactor and their products to total output error at most $`\epsilon/32`$, using dimension-aware rounding bounds. Finally clip the implemented value to $`[0,B_0+1]`$; this cannot increase its distance from the ideal $`Y_R\in[0,B_0]`$.

These allocations sum to at most $`\epsilon/4`$ numerical/random-bit bias. At fixed physical scales $`H,\gamma`$, the required random-bit and arithmetic word lengths are $`O(\log(S/\epsilon)+\log N)`$; this follows because the displayed cutoff, derivative bound and inverse tolerances are polynomials in $`S`$ and $`1/\epsilon`$. Source rejection uses a further logarithmic number of trials. Sparse-solver operation counts and coefficient evaluation remain charged; the word-length statement is not a claim of constant-time arithmetic.

## Sampling work and matched interpretation

For independent implemented samples in $`[0,B_0+1]`$, Hoeffding's inequality gives error at most $`\epsilon/4`$ with failure probability $`\zeta`$ using

```math
m\ge\frac{8(B_0+1)^2}{\epsilon^2}\log\frac2\zeta.
```

Together with the three deterministic bias allocations this gives $`|\widehat p_R-p_R|\le\epsilon`$. Each sample uses one source draw, one energy draw, one shifted solve and a drain-contact norm. With bounded $`H/\gamma`$, the sample count is $`O(\epsilon^{-2}\log(1/\zeta))`$. There is no factor from the original dissipative gap. In ideal arithmetic $`Y^2\le B_0Y`$, so variance-sensitive sampling can further exploit a small current; the Hoeffding count is a sufficient general bound, not the best precision comparison for every regime.

On the cubic geometry in the [matched comparison](comparison.md), one standard nested-dissection factorization per sample gives $`\widetilde O(L^6/\epsilon^2)`$ arithmetic and $`O(L^4)`$ factor storage, subject to its stated numerical pivoting and arithmetic assumptions. Iterative methods, factorization reuse and deterministic Lyapunov solvers may improve this. The coherent algorithm's smaller stated bound is not a lower-bound-certified advantage over all classical methods.

The scattering/Green-function framework and numerical transport solvers are established; see Waintal et al., [*Computational quantum transport: a scattering approach perspective*, arXiv:2407.16257v3](https://arxiv.org/html/2407.16257v3), Sections 5–6. The derivation here fixes the exact Markovian source normalization and a complete error budget for this particular classical comparator.

The [frequency verification](../verification/frequency_check.py) audits Parseval normalization, regularization and tail bounds, source-channel contraction, resolvent/derivative inequalities and solve-error bounds in finite examples, including an exactly dark sector. It does not benchmark performance or prove the asymptotic analysis.
