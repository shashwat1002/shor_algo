# Quantum Fourier Transform 

The Quantum fourier Transform uses the same matrix as the Discrete fourier transform. 

To formally define the Discrete fourier transform: 

For a vector $(\alpha_0, \alpha_1, \cdots, \alpha_{N-1})$, the out is another vector $(\beta_0, \beta_1, \cdots, \beta_{N-1})$ such that 

$$
\beta_j = \frac{1}{\sqrt{N}}\sum _{k=0} ^{N-1} \omega ^{jk}  \alpha_k
$$

where $\omega$ is the $N^{th}$ root of $1$ i.e. $\omega = e^{\frac{2 i\pi}{N}}$

The QFT (Quantum Fourier Transform) can be said to be the same matrix, just operating on the quantum computational basis.

i.e. the $QFT_N$ can be formally defined as (for $N = 2^n$): 

where $|k \rangle$ and $|j \rangle$ are computational basis vectors 

the transform: 

$$
|k \rangle \xrightarrow{QFT_{2^n}} \frac{1}{\sqrt{N}}\sum _{j=0} ^{2^n-1} \omega ^{kj} |j \rangle
$$

Where $\omega$ is the $N^{th}$ root of unity that is $\omega = e^{\frac{2 i\pi}{N}}$

As is visible right now, QFT is basically an application of the DST on the computational basis.

## Relevant properties 

There are three primary properties of the QFT that will be relevant to our purpose of solving the period-finding sub-problem in the Shor's algorithm. 

1. It is unitary (TODO: proof) and that implies we can make a quantum circuit corresponding to it. 
2. Two vectors that are just linearly shifted from each other will be transormed into two vectors that differ just in the _phase_ (formal definition and proof has been provided later in the document)
3.  Periodicity relation: suppose the input vector is periodic with $r$ then the output vector is periodic with $\frac{N}{r}$

### Property 1 

TODO 

### Property 2 

Simply put, we can say a linear shift of state vector will cause a relative phase shift in it's transform. 

What is linear shift of a vector? 

These two vectors: 

$$
\begin{bmatrix}
    \alpha_0 \\ 
    \alpha_1 \\
    . \\
    . \\
    \alpha_{N-1}
\end{bmatrix}
,
\begin{bmatrix}
    \alpha_{N-1} \\ 
    \alpha_0 \\
    . \\
    . \\
    \alpha_{N-2}
\end{bmatrix}
$$

are linearly shifted by $1$ place.

In other words, in terms of probability of what the state will collapse to once measured is the same before and after the QFT transform. 

Proof: 

considering a $N = 2^n$ state system ($n$ qubits )

Let us consider a vector of the form: 

$$
\begin{bmatrix}
    \alpha _0 \\
    \alpha _1 \\
    . \\
    . \\
    . \\
    \alpha _{N-1}
\end{bmatrix}
$$

and let us also say that: 

$$
\begin{bmatrix}
    \alpha _0 \\
    \alpha _1 \\
    . \\
    . \\
    . \\
    \alpha _{2^n-1}
\end{bmatrix}
\xrightarrow{QFT_{2^n}}
\begin{bmatrix}
    \beta_0 \\
    \beta_1 \\
    . \\
    . \\
    . \\
    \beta_{2^n - 1}
\end{bmatrix}
$$

In other words, we have that: 

$$
\beta_j = \frac{1}{\sqrt{2^n}}\sum _{k=0} ^{2^n-1} \omega ^{jk}  \alpha_k \forall j \in \{0, 1, \cdots 2^n -1 \}
$$

where $\omega = e^{\frac{2 i\pi}{2^n}}$

For convenience, I will be using $N$ instead of $2^n$ for now:

Now, let us consider a linearly shifted vector that is shifted by some constant $c$

this vector is therefore: 

$$
\begin{bmatrix}
    \alpha _{0 + c \mod{N}} \\
    \alpha _{1 + c \mod{N}} \\
    . \\
    . \\
    \alpha_{N-1} \\
    \alpha_0 \\
    . \\
    . \\
    \alpha_{(N-c) \mod{N}}
\end{bmatrix}
$$

without loss of generality, we can assume $c < N$ 

if the $k^{th}$ row of this vector is referred to as the $\alpha' _k$ then 

$$
\alpha' _k = \alpha _{(k+c) \mod N}
$$

Now, say that: 

$$
\begin{bmatrix}
    \alpha'_0 \\
    \alpha'_1 \\
    . \\
    . \\
    \alpha'_{N-1}
\end{bmatrix}
\xrightarrow{QFT_N}
\begin{bmatrix}
    \beta' _0 \\
    \beta' _1 \\
    . \\
    . \\
    \beta' _{N-1}
\end{bmatrix}
$$

and from the definition of QFT, we get 

$$
\beta'_j = \frac{1}{\sqrt{N}}\sum _{k=0} ^{N-1} \omega ^{jk}  \alpha'_k \forall j \in \{0, 1, \cdots N -1 \}
$$

Now, working on the term for an arbitrary $j \in \{0, 1, 2, \cdots N\}$

$$
\begin{aligned}
    \beta'_j &= \frac{1}{\sqrt{N}}\sum _{k=0} ^{N-1} \omega ^{jk}  \alpha'_k \\
    &= \frac{1}{\sqrt{N}} \sum _{k=0} ^{N-1} \omega ^{jk}  \alpha_{(k+c) \mod{N}} \\
    &= \frac{1}{\sqrt{N}} \sum _{k=0} ^{N-1} \omega ^{jk+jc} \omega^{-jc}  \alpha_{(k+c) \mod{N}}  \\
    & \text{and since } jc \text{ is a constant, we can say: } \\
    &= \frac{\omega^{jc}}{\sqrt{N}} \sum_{k=0} ^{N-1} \omega ^{j(k+c)} \alpha_{(k+c) \mod{N}} \\
    &= \frac{\omega^{jc}}{\sqrt{N}} \sum_{k=0} ^{N-1} (\omega ^{(k+c)})^j \alpha_{(k+c) \mod{N}} \\
    & \text{Since, we know } \omega^N = 1, \text{We an say: } \omega^x = \omega^{x \mod{N}} \text{, thus: } \\
    &= \frac{\omega^{jc}}{\sqrt{N}} \sum_{k=0} ^{N-1} (\omega ^{(k+c) \mod{N}})^j \alpha_{(k+c) \mod{N}} \\
    &= \frac{\omega^{jc}}{\sqrt{N}} \sum_{k=0} ^{N-1} \omega ^{j((k+c) \mod{N})} \alpha_{(k+c) \mod{N}} 
\end{aligned}
$$

Now, at this point we must note that that the function $f(x) = (x+c) \mod{N} \text{ for some } c \in \mathbb{Z}_N$ is a  **bijection** from $\mathbb{Z}_N \to \mathbb{Z}_N$

which means that due to the commutativity of the summation operation, we can say: 

$$
\sum_{k=0} ^{N-1} \omega ^{j((k+c) \mod{N})} \alpha_{(k+c) \mod{N}} = \sum_{l=0} ^{N-1} \omega ^{jl} \alpha_{l}
$$

We can do the above because the bijeciton takes all the values of $\mathbb{Z}_N$ when $k$ takes all the values of $\mathbb{Z}_N$

Therefore, we can write the last equation as 

$$
\beta' _j = \frac{\omega^{jc}}{\sqrt{N}} \sum_{l=0} ^{N-1} \omega ^{jl} \alpha_{l}
$$

and we know from before that 

$$
\beta _j = \frac{1}{\sqrt{N}} \sum_{k=0} ^{N-1} \omega ^{kl} \alpha_{k}
$$

and thus we have that: 

$$
\beta' _j = \omega_{jc} \beta _j
$$

and this is valid for all $j$ and therefore we can say that the outputs of the QFT of two linearly shifted vectors differ only in relative phase. 

Hence proved. 

As mentioned before, the reason this is so significant is that when we sample the outputs of the QFT, our observations will be the same for linearly shifted vectors because the relative phase difference can't manifest itself in the probability (because $|\omega^{jx}|^2 = 1$ and it is multiplied to the terms of the summation of the probability expression)


