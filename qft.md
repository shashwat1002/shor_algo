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

Let the $QFT_N$ matrix be referred to as $Q$

Required to prove: 

$$
Q \cdot Q ^{\dagger} = I
$$

Let us consider the LHS



and let $\alpha_{jk}$ be the element on the $j^{th}$ row and the $k^{th}$ column (indexed from $0$)



thus: 

$$
\begin{aligned}
    \alpha _{jk} &= \frac{1}{N} \cdot \sum _{l=0} ^{N-1} \omega ^{jl} \cdot \overline{\omega^{lk}} \\
    &= \frac{1}{N} \cdot \sum _{l=0} ^{N-1} \omega ^{jl - lk} \\
    &= \frac{1}{N} \cdot \sum _{l=0} ^{N-1} \omega ^{l(j - k)}
\end{aligned}
$$

This leads us to two cases:

Case 1:

$j=k$

thus the summation becomes: 

$$
\begin{aligned}
    \alpha_{jk} &= \frac{1}{N} \cdot \sum _{l=0} ^{N-1} \omega ^{l(j - k)} \\
    &= \frac{1}{N} \sum _{l=0} ^{N-1} \omega^0 \\
    &= \frac{1}{N} \sum _{l=0} ^{N-1} 1 \\
    &= 1
\end{aligned}
$$

Case 2:

$j \not = k$

thus summation becomes: 

$$
\begin{aligned}
    \alpha_{jk} &= \frac{1}{N} \cdot \sum _{l=0} ^{N-1} \omega ^{l(j - k)} \\
    &= \frac{1}{N} \sum _{l=0} ^{N-1} \omega^{j-k} \omega^l \\
    &= \frac{\omega^{j-k}}{N} \sum _{l=0} ^{N-1} \omega ^l \\
    & \text{ the summation is a geometric series} \\
    &= \frac{\omega^{j-k}}{N} \cdot \frac{1 - \omega ^N}{1 - \omega} \\
    & \text{We know: } \omega^N = 1 \\
    &= 0
\end{aligned}
$$

Therefore to summarize, we can say $\alpha_{jk}$ can be described with this function: 

$$
\alpha_{jk} = 
\begin{cases}
    1 & k=j \\
    0 & \text{otherwise }
\end{cases}
$$

and this describes a $I$ matrix. 

Therefore, LHS = $I$ 

LHS = RHS 

Hence proved.


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

## Property 3

A vector with period $r$ will lead to a vector with period $\frac{r}{M}$

Note: we won't be proving this property for the general case but for the specific case required for Shor's algorithm. 

When QFT is to be used in the Shor's algorithm, we can expect the elements of the row vector to be: 

$$
\alpha_j  =
\begin{cases}
    \sqrt{\frac{r}{N}} & j = a_0 \mod {r} \\
    0 & \text{ otherwise}
\end{cases}
$$

where $\alpha_i$ is the element at the $i^{th}$ row 

and $a_0$ is some offset 

Now, say $N \mod {r} = 0$, in that case we can easily make the claim that the following vector: 

$$
\alpha'_j  =
\begin{cases}
    \sqrt{\frac{r}{N}} & j = 0 \mod {r} \\
    0 & \text{ otherwise}
\end{cases}
$$

we can say that the new vector is basically the old vector shifted by an offset of $a_0$. We know from the previous proven property that the only difference in the output will be that of relative phases. 

This implies that all the rows that would be $0$ in the output of the old vector will continue to be $0$ and the same stands for the non-zerp values. This means that the output of both the vectors will have the same periodicity. 

So if we prove our claim for the output of the second vector, we will have proved it for the first vector as well. 

Let $\beta' j$ be the value at the $j^{th}$ row for the output of the second vector 

$$
\begin{aligned}
    \beta' _j &= \sqrt{\frac{1}{N}} \sum _{k=0} ^{N-1} \omega ^{jk} \alpha' _k \\
    & \text{We know that } \alpha' _k = 0 \ \forall \ k \not \equiv 0 \mod{r} \\
    & \text{Therefore, we introduce a new parameter l, such that } l = \frac{k}{r}  \\
    & \text{Note: } l \text{ is an integer } \\
    &= \sqrt{\frac{1}{N}} \sum _{l=0} ^{\frac{N}{r} - 1} \omega ^{jrl} \alpha' _{jrl} \\
    & \text{since } jrl  \equiv  0 \mod{r}, \text{ we have } \alpha' _{jrl} = \frac{r}{N} \\
    &= \frac{\sqrt{r}}{N} \sum _{l=0} ^{\frac{N}{r} - 1} \omega ^{jrl}
\end{aligned}
$$

The last summation is actually that of a geometric series, therefore we can say: 

$$
\beta' _j = \frac{\sqrt{r}}{N} \cdot \frac{\omega^{jN} - 1}{\omega^{jr} - 1}
$$

Since $\omega ^N = 1$, the numerator is always $0$ 

and in cases when $jr \equiv 0 \mod{N}$ the denominator is also $0$ and in such cases, we calculate the limit using the L' Hospital rule 

$$
\begin{aligned}
    \lim _{j \to k \frac{N}{r}} \beta' _k &= \lim _{j \to k \frac{N}{r}} \frac{\sqrt{r}}{N} \cdot \frac{\omega^{jN} - 1}{\omega^{jr} - 1} \\
    &= \frac{\sqrt{r}}{N} \cdot \lim _{j \to k \frac{N}{r}} \frac{\omega^{jN} - 1}{\omega^{jr} - 1} \\
    &= \frac{\sqrt{r}}{N} \cdot \lim _{j \to k \frac{N}{r}} \frac{\frac{2 \pi i N}{N}}{\frac{2 \pi ir}{N}} \cdot \frac{\omega ^{jN}}{\omega ^{jr}} \\
    &= \frac{\sqrt{r}}{N} \frac{N}{r}  \\
    &= \frac{1}{\sqrt{r}}
\end{aligned}
$$


Therefore, we can say that 

$$
\beta' _j = 
\begin{cases}
    \frac{1}{\sqrt{r}} & j \equiv 0 \mod{\frac{N}{r}} \\
    0 & \text{otherwise }
\end{cases}
$$

Therefore, we can say that the vector $\beta'$ (formed by the equation of $\beta' _j$) is periodic with $\frac{N}{r}$ therefore so is the vector $\beta$ (formed by the equation of $\beta_j$)

Hence proved. 

