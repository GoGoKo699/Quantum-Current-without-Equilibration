# Source-balanced current and residence time

Consider an $`N`$-mode number-conserving quadratic fermion system with Hermitian one-particle Hamiltonian $`h`$. A filled Markovian left reservoir injects with rate matrix $`\Gamma_L\succeq0`$, and an empty right reservoir removes particles with rate matrix $`\Gamma_R\succeq0`$. Put

```math
\Gamma=\Gamma_L+\Gamma_R,\qquad
A=-ih-\Gamma/2,\qquad K(t)=e^{At},\qquad
W=\mathrm{Tr}\Gamma_L>0.
```

With covariance convention $`C_{ij}=\langle c_j^\dagger c_i\rangle`$, the standard quadratic Lindblad equation is

```math
\dot C=AC+CA^\dagger+\Gamma_L.
```

The reservoir occupations are independent of energy. The physical interpretation and the Lyapunov formulation are established open-system tools; see [Jin, Filippone and Giamarchi (2020)](https://arxiv.org/abs/2008.11747) and [Purkayastha (2022)](https://arxiv.org/abs/2201.00677). This model does not by itself represent arbitrary finite-temperature energy-selective electronic reservoirs.

## The theorem

Let $`\mathcal D`$ be the largest $`h`$-invariant subspace contained in $`\ker\Gamma`$, let $`\mathcal B=\mathcal D^\perp`$, and let $`P_{\mathcal B}`$ be the orthogonal projector onto $`\mathcal B`$. Define

```math
C_r(T)=\int_0^T K(t)\Gamma_rK(t)^\dagger\,dt,
\qquad r\in\{L,R\}.
```

Both positive integrals have finite limits $`C_L,C_R`$, and

```math
0\preceq C_L\preceq P_{\mathcal B},\qquad
C_L+C_R=P_{\mathcal B},\qquad
AC_L+C_LA^\dagger=-\Gamma_L.
```

The last equation holds on the full one-particle space. Its source-driven solution is selected by $`C_LP_{\mathcal D}=P_{\mathcal D}C_L=0`$; unrestricted steady solutions can have additional dark-sector terms.

Consider an auxiliary one-particle absorption process whose initial density matrix is

```math
\rho_{\mathrm{in}}=\Gamma_L/W.
```

The particle evolves without absorption by $`K(t)`$ and can be absorbed at either contact. Absorption occurs with probability one, its right-contact probability is

```math
p_R=\frac{\mathrm{Tr}(\Gamma_RC_L)}{W},
```

and its mean residence time satisfies

```math
\mathbb E\tau
=\frac{\mathrm{Tr}C_L}{W}
\le\frac{\dim\mathcal R_L}{W}
\le\frac{\dim\mathcal B}{W}
\le\frac NW.
```

Here $`\mathcal R_L=\mathrm{span}\{A^k\mathrm{ran}\Gamma_L:0\le k<N\}`$ is the source-reachable subspace. Its dimension is a mathematical sharpening; computing it is an additional task unless the input supplies it.

The steady right current of the fermionic system is

```math
J_R=\mathrm{Tr}(\Gamma_RC_L)=Wp_R.
```

This current is well-defined even when the full covariance does not converge because undamped dark coherences keep rotating. No positive global dissipative gap, normality of $`A`$, or unique full-system steady state is required.

## Proof

The identity $`A+A^\dagger=-\Gamma`$ gives two contraction relations:

```math
\frac{d}{dt}\bigl(K(t)^\dagger K(t)\bigr)
=-K(t)^\dagger\Gamma K(t),
```

```math
\frac{d}{dt}\bigl(K(t)K(t)^\dagger\bigr)
=-K(t)\Gamma K(t)^\dagger.
```

For the second equality, $`A`$ commutes with $`K(t)`$, and $`A^\dagger`$ commutes with $`K(t)^\dagger`$; normality is unnecessary. Integration yields

```math
C_L(T)+C_R(T)=I-K(T)K(T)^\dagger\preceq I.
```

Each $`C_r(T)`$ is increasing in the positive-semidefinite order and bounded above by $`I`$, so it converges in finite dimension.

Because $`h`$ is Hermitian and $`\Gamma\succeq0`$, $`\mathcal D`$ reduces both operators: $`h`$ preserves $`\mathcal D`$ and its orthogonal complement, while $`\Gamma`$ vanishes on $`\mathcal D`$. On $`\mathcal D`$, $`K(t)`$ is unitary. Every eigenvalue of $`A`$ has nonpositive real part. If $`Av=i\omega v`$, then

```math
0=\mathrm{Re}\langle v,Av\rangle
=-\langle v,\Gamma v\rangle/2,
```

so $`\Gamma v=0`$ and $`hv=-\omega v`$. Thus $`v\in\mathcal D`$. The restriction $`A|_{\mathcal B}`$ has only strictly negative-real-part eigenvalues, and consequently $`K(t)|_{\mathcal B}\to0`$. Hence

```math
K(t)K(t)^\dagger\longrightarrow P_{\mathcal D},
\qquad C_L+C_R=P_{\mathcal B}.
```

Positivity and $`\Gamma_L\preceq\Gamma`$ imply $`\Gamma_LP_{\mathcal D}=0`$. Therefore $`K(T)\Gamma_LK(T)^\dagger\to0`$. Differentiating under the finite integral gives

```math
AC_L(T)+C_L(T)A^\dagger
=K(T)\Gamma_LK(T)^\dagger-\Gamma_L,
```

which proves the claimed global Lyapunov equation. The range of every integrand lies in $`\mathcal R_L`$; thus $`C_L`$ is supported there, and $`C_L\preceq P_{\mathcal R_L}`$. Taking its trace proves the dimension bound.

The auxiliary survival probability and lead-resolved absorption densities are

```math
q(t)=\mathrm{Tr}\bigl(K(t)\rho_{\mathrm{in}}K(t)^\dagger\bigr),
\qquad
f_r(t)=\mathrm{Tr}\bigl(\Gamma_rK(t)\rho_{\mathrm{in}}K(t)^\dagger\bigr).
```

They obey $`-q'(t)=f_L(t)+f_R(t)`$. Since the source is supported on $`\mathcal B`$, $`q(0)=1`$ and $`q(\infty)=0`$. Integration gives $`p_L+p_R=1`$, $`p_r=\mathrm{Tr}(\Gamma_rC_L)/W`$, and

```math
\mathbb E\tau=\int_0^\infty q(t)\,dt
=\mathrm{Tr}C_L/W.
```

Finally, for arbitrary physical initial covariance $`0\preceq C(0)\preceq I`$,

```math
C(t)=K(t)C(0)K(t)^\dagger+C_L(t).
```

The first term's bright and bright-dark blocks decay. Its surviving dark block is annihilated by $`\Gamma_R`$, so $`\mathrm{Tr}(\Gamma_RC(t))\to J_R`$. This proves the current statement without assuming full-state convergence.

## Interpretation and useful consequences

The physical left injection rate is Pauli blocked:

```math
J_L=\mathrm{Tr}\bigl(\Gamma_L(I-C_L)\bigr).
```

Taking the trace of the Lyapunov equation gives $`W=\mathrm{Tr}(\Gamma C_L)`$, hence $`J_L=J_R`$. Accordingly, $`p_R=J_R/W`$ is the auxiliary right-absorption probability, or current per bare injection attempt. It is not a fraction of successful many-body injection events.

Write $`S=N/W`$. Monotonicity of $`q`$ and $`\int q\le S`$ imply, for every $`T>0`$,

```math
\Pr(\tau>T)=q(T)\le\min\{1,S/T\},
\qquad
\int_T^\infty f_R(t)\,dt\le q(T),
```

```math
\mathbb E\bigl[\min(\tau,T)^2\bigr]
=2\int_0^T t q(t)\,dt\le2ST.
```

These are the tail and truncated-second-moment guarantees used by a stopped estimator. They do not themselves give a quantum speedup; a measured first-exit simulation benefits from the same mean bound.

If $`W_R=\mathrm{Tr}\Gamma_R>0`$, define the analogous mean $`\mathbb E\tau_R=\mathrm{Tr}C_R/W_R`$ for injection from the right. The exact sum rule is

```math
W\mathbb E\tau+W_R\mathbb E\tau_R=\dim\mathcal B.
```

Also $`0\le J_R\le\min\{W,W_R\}`$. These bounds are independent of how small a bright-sector decay rate becomes.

For constant occupations $`n_L,n_R\in[0,1]`$, the source-driven covariance on $`\mathcal B`$ is $`n_RC_R+n_LC_L`$, and the net right current is $`(n_L-n_R)Wp_R`$. This extension retains energy-independent Markovian contacts.

The source condition is essential. A general initial state can have order-one overlap with a nearly dark mode and an arbitrarily large lifetime. More generally, a positive source $`Q\preceq c\Gamma`$ obeys $`\int_0^\infty K(t)QK(t)^\dagger dt\preceq cP_{\mathcal B}`$, giving mean residence at most $`c\dim\mathcal B/\mathrm{Tr}Q`$ for initial state $`Q/\mathrm{Tr}Q`$.

## Exact discrete theorem and chronology

The discrete theorem distinguishes the source matrix from the measured exit effect. Let $`A`$ be any contraction, let $`0\preceq Q\preceq I-AA^\dagger`$ with $`W=\mathrm{Tr}Q>0`$, and choose positive exit effects $`E_r`$ satisfying

```math
\sum_r E_r=I-A^\dagger A.
```

Starting from $`\rho_{\mathrm{in}}=Q/W`$, a step either survives with Kraus operator $`A`$ or exits through effects $`E_r`$. Define

```math
C=\sum_{k=0}^\infty A^kQ(A^\dagger)^k.
```

Then

```math
0\preceq C\preceq I,\qquad C=ACA^\dagger+Q,\qquad
\mathbb E\tau=\frac{\mathrm{Tr}C}{W}\le\frac NW,
```

```math
p_r=\frac{\mathrm{Tr}(E_rC)}W,\qquad \sum_rp_r=1.
```

The residence time $`\tau`$ counts steps up to and including the exit step, so $`\tau\in\{1,2,\ldots\}`$. Indeed, the finite sum obeys

```math
\sum_{k=0}^{m-1} A^kQ(A^\dagger)^k
\preceq
\sum_{k=0}^{m-1}A^k(I-AA^\dagger)(A^\dagger)^k
=I-A^m(A^\dagger)^m\preceq I.
```

Its trace bounds $`\sum_{k\ge0}\Pr(\tau>k)`$ and implies that survival tends to zero. The identity

```math
\Pr(\tau>k)-\Pr(\tau>k+1)
=\sum_r\mathrm{Tr}\!\left(E_rA^k\rho_{\mathrm{in}}(A^\dagger)^k\right)
```

then proves exit normalization and the probability formula. The same source-reachable-rank refinement holds as in continuous time.

For a unitary step $`U`$ followed by diagonal attenuation $`D`$, put

```math
A=DU,\qquad B_L+B_R=I-D^2,\qquad Q=B_L.
```

The source is inserted after attenuation. A particle present at that time is first propagated by $`U`$, then tested at the contacts. Therefore

```math
I-AA^\dagger=B_L+B_R,\qquad
E_r=U^\dagger B_rU,\qquad
I-A^\dagger A=E_L+E_R,
```

```math
C=\sum_{k=0}^\infty(DU)^kB_L(U^\dagger D)^k,\qquad
p_R=\frac{\mathrm{Tr}(U^\dagger B_RUC)}{\mathrm{Tr}B_L}.
```

Replacing the exit effect $`U^\dagger B_RU`$ by $`B_R`$ generally gives the wrong answer. With disjoint diagonal left and right contact sets, the associated filled-left/empty-right Gaussian collision model has covariance update $`C\mapsto DUC U^\dagger D+B_L`$ and right loss per step $`\mathrm{Tr}(B_RUC U^\dagger)=Wp_R`$. The continuous physical theorem permits general positive rate matrices; the discrete bath-current interpretation here uses these explicit independent contact collisions.
