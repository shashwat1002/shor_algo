<!-- Nielsen and Chuang based notes -->
## Reduction of factoring to order-finding

Given $N$ as a positive integer and $x$ co-prime to $N$, $1 \leq x < N$,
the order of $x$ modulo $N$ is defined as the *least positive* integer
$r$ such that:
$$ x^r \equiv 1 \text{ mod } N $$

Our reduction from factoring to order-finding can be done in two basic steps:

1. Firstly, we show that we can compute a factor of $n$ if we can find
   a non-trivial solution to the equation $x^{2} \equiv 1 \text{ mod } N$, i.e.
   there exists $x$ such that $x \not\equiv \pm 1 \text{ mod } N$.

2. Secondly, we show that for a random $y$ co-prime to $N$, it is highly
   probably that the order of $y$, $r$ is an even number, and $y^{\frac{r}{2}}
   \not\equiv \pm 1 \text{ mod } N$, and thus $x \equiv y^{\frac{r}{2}} \text{
   mod } N$ is a solution to $x^2 \equiv 1 \text{ mod } N$

### Step 1

Now let us suppose we have the non trivial root of $1$ modulo $N$,
then
$$
\begin{aligned}
x^2 &\equiv 1 &\text{ mod } N \\
x^2 - 1 &\equiv 0 &\text{ mod } N \\
(x + 1)(x - 1) &\equiv 0 &\text{ mod } N \\
\end{aligned}
$$

So $N$ divides $(x + 1)(x - 1)$, which means $N$ must have a common factor
with either $(x + 1)$ or $(x + 1)$. Now recall that $x - 1 < x + 1 < N$,
and thus $N$ cannot completely divide either of $(x - 1)$ or $(x + 1)$,
so the common factor that they share must be a factor of $N$ as well.

<!-- How to guarantee that at least one of gcd gives a non-trivial factor? -->
Thus, we can use Euclid's algorithm to compute $\text{gcd}(x - 1, N)$,
and $\text{gcd}(x + 1, N)$, obtaining a non-trivial factor of $N$.
This is done in $O(log^3(N))$ time. Why is this the complexity?

There are a maximum of $log(N)$ steps in the Euclidean algorithm, each
involving the division of one number by another, and the computation of
a remainder. Thus, each step takes $log^2(N)$ time itself, for a total of
$O(L^3)$ time complexity, where $L = log(N)$.

### Step 2

This step itself can be further broken down as such:

- First, we show that for the group $Z_{p^{\alpha}}^{*}$, there exists a generator.

- Next, we show that if we have the greatest number $2^{d}$ which divides
  $\varphi(p^{\alpha})$, then it divides the order of a of a random number in
  the previously mentioned group with probability $\frac{1}{2}$.

- Next we show that the for the prime factorization of an odd composite natural
  number, there is a high probability that a randomly chosen number from
  $Z_{N}^{*}$ has an even order mod $N$.

Let us proceed to formally state the first of these statements.

### Lemma 1
Let $p$ be an odd prime, $\alpha$ a natural number. Then the group
$Z_{p^\alpha}^{*}$ is cyclic.

### Proof

We state this lemma without proof.

#### Lemma 2
Let $p$ be an odd prime, and $2^d$ be the largest power of 2 dividing
$\varphi(p^\alpha)$, where $\varphi$ is Euler's totient function. Then with
probability one-half, $2^d$ divides the order, modulo $p^\alpha$ of a random
element of $Z_{p^\alpha}^{*}$

#### Proof
$\varphi$, Euler's totient function counts the numbers from 1 to the given
number, which are co-prime to the given number. It also has a specific
property, that $\varphi(ab) = \varphi(a) \varphi(b)$.

We note $\varphi(p^\alpha) = \varphi(p^{\alpha - 1}) \varphi(p)
= \varphi(p^{\alpha - 1})(p - 1)$, because $p$ is a prime. Since $p$ is also
odd, $p - 1$ must be even, and as a result, $d \geq 1$.

Now, from the previous lemma, we know that there exists a generator $g$ for
$Z_{p^\alpha}^{*}$, since it is a cyclic group. We already know that there
must be $\varphi(p^\alpha)$ elements in the group. Since the order of an element in
the finite cyclic group cannot exceed the number of elements in it,
an arbitrary element in the group can be written as $g^{k}$, for some
$k$ in the range of 1 to $\varphi(p^{\alpha})$.

Let $r$ be the order of $g^{k} \text{ mod } p^{\alpha}$, and consider
two possible cases:

i. $k$ is odd. Then $g^{kr} \equiv 1 \text{ mod } p^{\alpha}$ implies that the
   number of the elements in the group i.e. $\varphi(p^{\alpha})$ must divide
   $kr$, <!-- Why? This is order of the group. (that doesn't make sense) --> and
   thus $2^d$ must divide $kr$, and since $k$ is odd, it contains no powers of
   2 in its prime factorization, i.e. $2^d$ must divide $r$. 

ii. $k$ is even. Then
$$
\begin{aligned}
g^{\frac{\varphi(p^{\alpha})}{2} k} &=
\left(g^{\varphi(p^{\alpha})}\right)^{\frac{k}{2}} \\
	&= 1 ^{\frac{k}{2}}\\
	&= 1 \text{ mod } p^{\alpha}\\
\end{aligned}
$$
which in turn implies that $r$ must divide $\varphi(p^{\alpha})/2$, since $r$
is by definition the least natural number such that $g^{kr} \equiv 1 \text{ mod
} p^{\alpha}$. This implies that $2^d$ does not divide $r$.

We can see this by noting that $\varphi(p^{\alpha})/2 = 2^{d-1} \cdot c_0$,
where $c_0$ is some odd constant. Then since $r$ divides $\varphi(p^{\alpha})$,
if $r = 2^b \cdot c_1$, where $2^b$ is the highest power of 2 that
divides $r$  and $c_1$ is another odd constant, then $b \leq (d - 1)$,
since otherwise $r$ would not be able to divide $\varphi(p^{\alpha})$.
This means that $2^d$ cannot divide $r$.

Note that in this manner, dependent on whether $k$ is odd or even,
we were able to predict whether or not $2^d$ divides the order $r$, of
an arbitrary element $g^k$ in the group.

All of this together means that $Z_{p^{\alpha}}^{*}$ can be cleanly partitioned
into two sets of equal size. The first are $g^k$ with odd $k$, for which $2^d$
divides $r$, and the second are $g^k$ with even $k$, for which $2^d$ does not
divide $r$. Thus, for a randomly chosen element in the group,
with probability $\frac{1}{2}$, the integer $2^d$ divides the order $r$ of the
element.

However, this was stated for the group $Z_{p^{\alpha}}^{*}$, so
how is it useful for the composite number which we are trying to consider?
For this we move on to our next lemma.

#### Lemma 3
Let $N = p_1^{\alpha_1} p_2^{\alpha_2} \dots p_m^{\alpha_m}$, where $p_i$'s are all
distinct primes. Then if we choose an arbitrary $x$ from $Z_{N}^{*}$,
with order $r$ modulo $N$, we have
$$
P(r \text{ is even and } x^{\frac{r}{2}} \not\equiv \pm 1 (\text{ mod } N)) \geq 1 - \frac{1}{2^m}
$$

#### Proof
Let us prove instead, the following, equivalent statement (we can see that the
statements are equivalent by a clever application of De Morgan's law):
$$
P(r \text{ is odd or } x^{\frac{r}{2}} \equiv \pm 1 (\text{ mod } N)) \leq \frac{1}{2^m}
$$

From the Chinese remainder theorem, there is one and only one $x$ modulo $N$,
such that $x \equiv x_j (\text{ mod } p_{j}^{\alpha_j})$ for each $j$, since
the numbers $p_{j}^{\alpha_j}$ are all obviously pairwise co-prime.
Thus, it is equivalent to chose the sequence of $x_j$ independently from $Z_{p_{j}^{\alpha_j}}^{*}$, or to choose a single $x$ from $N$.

Now, let $r_j$ be the order of $x_j \text{ mod } p_{j}^{\alpha_j}$, 
$2^{d_j}$ be the largest power of 2 that divides $r_j$,
and $2^d$ be the largest power of 2 that divides $r$.

In order to have $r$ be odd or $x^{\frac{r}{2}} = \pm 1 (\text{ mod } N)$, all
$d_j$ must be equal to each other for all $j$.

We can see this by breaking it down into two cases:

- $r$ is odd. Since each $r_j$ divides $r$,
<!-- Why? -->
  since $r$ is odd, it follows that each $r_j$ must also be odd.
  As a result, there will be no power of 2 that will divide any $r_j$,
  i.e $d_j = 0$ for all $j$.

- $r$ is even, and $x^{\frac{r}{2}} \equiv \pm 1 (\text{ mod } N)$.
  In this case, $x^{\frac{r}{2}} \equiv \pm 1 (\text{ mod } p_{j}^{\alpha_j})$.
  We can see this because $x^{\frac{r}{2}} \pm 1 \equiv 0 \text{ mod } N$,
  which means $N$ divides $x^{\frac{r}{2}} \pm 1$. Now,
  $p_{j}^{\alpha_j}$ in turn divides $N$, and thus
  $p_{j}^{\alpha_j}$ divides $x^{\frac{r}{2}} \pm 1$, and finally,
  $x^{\frac{r}{2}} \equiv \pm 1 (\text{ mod } p_{j}^{\alpha_j})$.

  Thus, $r_j$ does not divide $\frac{r}{2}$, but $r_j$ did indeed divide
  $r$. The only way this is possible is if $d_j = d$ for all $j$.
<!-- HUH?? -->

The probability of all these values $d_j$ being the same, is at most $\frac{1}{2^m}$.
We can see this from lemma 2.
<!-- What the fuck, I sure as fuck can't -->

