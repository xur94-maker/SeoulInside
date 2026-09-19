# Ways to Compute the Natural Constant e — and a Few Coincidences

## Summary in Plain Language

**What is e?**
`e ≈ 2.71828…` is a number that goes on forever without repeating, just like π. It is the limit you reach when something that grows in proportion to what it already has keeps growing, continuously, to the very end.

**An easy example: bank interest**
Put 1 dollar in the bank at 100% interest per year, and see what happens as you compound more often:

- Once a year: 2 dollars
- Every month: about 2.61 dollars
- Every day: about 2.71 dollars
- Continuously, every instant: about 2.71828 dollars (it never grows past this)

No matter how often you compound, you cannot pass this limit. That limit is e.

**Why "natural"?**
In nature, anything that "changes in proportion to its current amount" — bacteria multiplying, radioactive decay — is described by this number without any forcing. Mathematically, too, `e^x` is the function that stays itself when you differentiate it, which makes calculations as simple as they can be.

**Where is it used?**
- Money: continuous compounding
- Biology and society: bacterial growth, population growth
- Physics: radioactive decay, the way hot coffee cools
- Statistics: the normal distribution, the Poisson distribution
- AI: the sigmoid and softmax functions

**Different roads to e (what this article covers)**
- Limit, `(1+1/n)^n`: the interest story exactly as above. Intuitive, but slow to converge.
- Series, `\sum 1/k!`: the fastest and most practical. The 35-trillion-digit world record also uses this approach.
- Infinite products: the Catalan and Pippenger formulas. Pippenger's converges much faster.
- Continued fraction: Euler's `[2; 1, 2, 1, 1, 4, 1, 1, 6, …]`, a beautifully regular pattern that was used to prove e is irrational.
- Probability and combinatorics: "keep adding random numbers between 0 and 1 until the sum passes 1, and on average you need e of them", or "in a gift exchange, the chance that nobody gets their own gift is about 1/e".
- Calculus: the derivative of `e^x` is itself; `\int_1^e (1/x)\,dx = 1`.
- Algorithms: spigot, CORDIC, AGM.

**Bonus: coincidences**
Curious near-identities such as `163(\pi - e) ≈ 69` and `e^\pi - \pi ≈ 20`, plus the Andrew Jackson mnemonic for remembering "2.7 1828 1828".

**In one line**
e is the number of "things that grow on their own", and that is why very different roads — interest, probability, calculus — all lead to the same value.

---

# The Full Article

The natural constant `e \approx 2.718281828459045\ldots` has been computed in nearly as many different ways as π. Limits, series, infinite products, continued fractions, probability, calculus, hardware algorithms — the ways of meeting e are far more varied than you might expect. This article lays out each method side by side in four forms — Unicode / LaTeX / Mathematica (pseudocode) / Python — together with who discovered it and when.

---

## 1. The Basic Definition (Limit)

**Core idea**: This constant was first discovered by Jacob Bernoulli in 1683 while working on a continuous-compound-interest problem. As you make `n` infinitely large and compound the interest "continuously", this limit appears. However, the error shrinks only like `1/n`, so convergence is very slow.

a) Unicode
```
e = lim[n→∞] (1 + 1/n)^n
```
b) LaTeX
```latex
e = \lim_{n\to\infty} \left(1+\frac{1}{n}\right)^n
```
c) Mathematica
```mathematica
Limit[(1 + 1/n)^n, n -> Infinity]
N[(1 + 1/10^7)^(10^7), 10]
```
d) Python
```python
def limit_definition(n=10_000_000):
    return (1 + 1 / n) ** n

print(limit_definition())  # 2.7182816941... (accurate to only about 7 digits)
```

> **History in one line**: Bernoulli only proved that this limit lies between 2 and 3. The symbol "e" and the complete series expression were added later by Euler.

---

## 2. Series — The Most Practical

**Core idea**: Newton was already, in effect, working with this series around 1665 while computing logarithms, and Euler around 1727 introduced the notation "e" and formalized it as `\sum 1/k!`. Since `k!` grows explosively, it converges far faster than the limit definition.

a) Unicode
```
e = Σ[k=0,∞] 1/k! = 1 + 1 + 1/2! + 1/3! + ⋯
```
b) LaTeX
```latex
e = \sum_{k=0}^{\infty} \frac{1}{k!}
```
c) Mathematica
```mathematica
E == Sum[1/k!, {k, 0, Infinity}]
N[Sum[1/k!, {k, 0, 20}], 20]
```
d) Python
```python
def taylor_series(terms=20):
    total, fact = 0.0, 1
    for k in range(terms):
        if k > 0:
            fact *= k
        total += 1 / fact
    return total

print(taylor_series())  # 2.718281828459046 (15 digits accurate with just 20 terms)
```

**Dobiński's formula (1877)**: The Bell number `B_n`, which counts the ways to partition a set, can be written as `B_n = \frac{1}{e}\sum_{k=0}^{\infty}\frac{k^n}{k!}`. Turning this around gives another series expression for e, one connected to combinatorics (set partitions).

```latex
B_n = \frac{1}{e}\sum_{k=0}^{\infty} \frac{k^n}{k!} \quad\Longrightarrow\quad e = \frac{1}{B_n}\sum_{k=0}^{\infty}\frac{k^n}{k!}
```

> **World-record supplement**: Actual world-record computations of e are also based on this Taylor series, but instead of adding the terms one after another, they use **binary splitting**: the range is halved recursively and the pieces are combined. With this approach (the program y-cruncher), Jordan Ranous computed e to **35 trillion (35,000,000,000,000) digits** on December 24, 2023, which is the currently verified world record.

---

## 3. Infinite Products — A Counterpart to Wallis's Product for π

**Core idea**: Just as π has Wallis's infinite product (1655), e has two infinite-product expressions. They were proved using Stirling's formula, by Catalan in 1873 and by Pippenger in 1980 respectively.

**Catalan's product formula (1873)**

a) Unicode
```
e = (2/1)·(4/3)^(1/2)·(6/5·8/7)^(1/4)·(10/9·12/11·14/13·16/15)^(1/8)·⋯
```
b) LaTeX
```latex
e = \frac{2}{1}\left(\frac{4}{3}\right)^{1/2}\left(\frac{6}{5}\cdot\frac{8}{7}\right)^{1/4}\left(\frac{10}{9}\cdot\frac{12}{11}\cdot\frac{14}{13}\cdot\frac{16}{15}\right)^{1/8}\cdots
```
c) Mathematica
```mathematica
catalanE[nTerms_] := Module[{prod = 2.0, idx = 1, k, grp},
  Do[
   grp = Product[idx2 = idx++; (2 (idx2 + 1))/(2 idx2 + 1), {2^(k - 1)}];
   prod *= grp^(1/2^k), {k, nTerms}];
  prod]
catalanE[15]
```
d) Python
```python
def catalan_product(n_terms=15):
    product, pair_index = 2.0, 1
    for n in range(1, n_terms + 1):
        group_product = 1.0
        for _ in range(2 ** (n - 1)):
            numerator = 2 * (pair_index + 1)
            group_product *= numerator / (numerator - 1)
            pair_index += 1
        product *= group_product ** (1 / 2 ** n)
    return product

print(catalan_product())  # 2.7182530786...
```

**Pippenger's product formula (1980)** — the "e version" of Wallis's product

a) Unicode
```
e/2 = (2/1)^(1/2)·(2/3·4/3)^(1/4)·(4/5·6/5·6/7·8/7)^(1/8)·⋯
```
b) LaTeX
```latex
\frac{e}{2} = \left(\frac{2}{1}\right)^{1/2}\left(\frac{2}{3}\cdot\frac{4}{3}\right)^{1/4}\left(\frac{4}{5}\cdot\frac{6}{5}\cdot\frac{6}{7}\cdot\frac{8}{7}\right)^{1/8}\cdots
```
c) Mathematica
```mathematica
pippengerE[kTerms_] := Module[{prod = 1.0, k, term, d, hi},
  Do[
   term = If[k == 1, 2.0,
     Product[(2 j - 1)/(2 j) * (2 j + 1)/(2 j), {j, 2^(k - 2), 2^(k - 1) - 1}]];
   prod *= term^(1/2^k), {k, kTerms}];
  2*prod]
pippengerE[15]
```
d) Python
```python
def pippenger_product(k_terms=15):
    product = 1.0
    for k in range(1, k_terms + 1):
        if k == 1:
            term = 2.0
        else:
            term, d, hi = 1.0, 2 ** (k - 1) + 1, 2 ** k - 1
            while d <= hi:
                term *= (d - 1) / d * (d + 1) / d
                d += 2
        product *= term ** (1 / 2 ** k)
    return product * 2

print(pippenger_product())  # 2.7182818289... (converges much faster than the Catalan product)
```

> In the Wallis product for π/2, the exponent simply grows with the number of terms and convergence is slow, whereas in these two products the exponents shrink like `1/2^n`, so they **converge much faster**.

---

## 4. Continued Fraction — Euler, 1737

**Core idea**: Euler derived it in a paper written in 1737, and used the non-periodicity of this very continued fraction to give **the first proof that e is irrational** (published seven years later, in 1744). Unlike the erratic continued fraction of π, the continued fraction of e follows a regular pattern, with the terms **2; 1, 2, 1, 1, 4, 1, 1, 6, ...** repeating in an orderly way.

a) Unicode
```
e = 2 + 1/(1 + 1/(2 + 1/(1 + 1/(1 + 1/(4 + ⋯)))))
```
b) LaTeX
```latex
e = 2 + \cfrac{1}{1+\cfrac{1}{2+\cfrac{1}{1+\cfrac{1}{1+\cfrac{1}{4+\cdots}}}}}
```
c) Mathematica
```mathematica
ContinuedFraction[E, 15]
(* {2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10} *)
N[FromContinuedFraction[{2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8}], 15]
```
d) Python
```python
from fractions import Fraction

def continued_fraction(depth=20):
    def pattern(i):
        if i == 0: return 1
        return 2 * ((i - 1) // 3 + 1) if (i - 1) % 3 == 1 else 1
    value = Fraction(pattern(depth))
    for i in range(depth - 1, 0, -1):
        value = pattern(i) + Fraction(1) / value
    return 2 + Fraction(1) / value

print(float(continued_fraction(20)))  # 2.718281828459045
# convergents: 2/1, 3/1, 8/3, 11/4, 19/7, 87/32, 106/39, ...
```

> **Features**: Very fast to compute, with almost no round-off error. It is interesting that the continued fraction of π is irregular while that of e is regular.

---

## 5. Stochastic and Combinatorial Methods

**5-1. Sum of uniform random variables**

**Core idea**: Keep drawing values from the uniform distribution on (0,1) and adding them up. The expected minimum number of draws needed for the sum to exceed 1 is exactly e.

a) Unicode
```
E[min{n : X₁+X₂+⋯+Xₙ > 1}] = e,  Xᵢ ~ Uniform(0,1)
```
b) LaTeX
```latex
\mathbb{E}\big[\min\{n : X_1+\cdots+X_n > 1\}\big] = e,\quad X_i \sim \mathrm{Uniform}(0,1)
```
c) Mathematica
```mathematica
SeedRandom[1];
trials = 200000;
Mean[Table[
  Module[{s = 0., n = 0},
   While[s <= 1, s += RandomReal[]; n++]; n], {trials}]]
```
d) Python
```python
import random

def stochastic_uniform_sum(trials=200_000):
    total_count = 0
    for _ in range(trials):
        s, count = 0.0, 0
        while s <= 1.0:
            s += random.random()
            count += 1
        total_count += count
    return total_count / trials

print(stochastic_uniform_sum())  # ≈2.7168 (converges slowly, O(1/√n))
```

**5-2. Probability of a derangement** — Montmort, 1708

**Core idea**: If you shuffle n items at random, the **probability that no item stays in its original place** (that is, the probability of getting a derangement) converges to `1/e` as n grows. The problem itself was first treated by Montmort in 1708 (starting from a gambling problem). It is proved with the inclusion–exclusion principle, and the result matches exactly the partial sums of the Taylor series of `1/e`.

a) Unicode
```
lim[n→∞] Dₙ/n! = 1/e   (Dₙ: number of derangements of n elements)
```
b) LaTeX
```latex
\lim_{n\to\infty} \frac{D_n}{n!} = \frac{1}{e}
```
c) Mathematica
```mathematica
Dn[n_] := n! Sum[(-1)^k/k!, {k, 0, n}]
N[20!/Dn[20], 15]
```
d) Python
```python
import math

def derangement_count(n):
    if n == 0: return 1
    if n == 1: return 0
    d2, d1 = 1, 0
    for i in range(2, n + 1):
        d2, d1 = d1, (i - 1) * (d1 + d2)
    return d1

print(math.factorial(15) / derangement_count(15))  # 2.718281828459379
```

> In practice, this is also used in the form of a relation: the integer nearest to `n!/e` is the number of derangements — for example, in a gift exchange where nobody receives their own gift.

---

## 6. Differential Equations and Analysis (Calculus-Based)

**Core idea**: The most fundamental definition of e — the base of the one exponential function that is its own derivative, and the definition of the natural logarithm.

a) Unicode
```
d/dx eˣ = eˣ         ∫[1,e] (1/x) dx = 1
```
b) LaTeX
```latex
\frac{d}{dx}e^x = e^x \qquad \int_1^e \frac{1}{x}\,dx = 1
```
c) Mathematica
```mathematica
D[E^x, x] == E^x
NIntegrate[1/x, {x, 1, E}]  (* converges to 1 *)
```
d) Python
```python
import math

def calculus_ln_integral(upper, steps=200_000):
    a, b = 1.0, upper
    n = steps if steps % 2 == 0 else steps + 1
    h = (b - a) / n
    total = 1/a + 1/b
    for i in range(1, n):
        total += (4 if i % 2 else 2) / (a + i*h)
    return total * h / 3

print(calculus_ln_integral(math.e))  # 1.0000000000
```

---

## 7. Algorithmic and Engineering Methods (Hardware and Digit Extraction)

**7-1. Spigot algorithm** — applying the principle of Rabinowitz and Wagon's π spigot (early 1990s, published in 1995) to e

**Core idea**: Write e in the mixed-radix representation `(2; 1,1,1,1,\ldots)`, multiply the array by 10 at each step, and propagate the carries from right to left, which yields the decimal digits **exactly one at a time**. It works with only an integer array and no floating point, so it is also well suited to embedded and hardware implementations.

d) Python
```python
def spigot_algorithm(n_digits=100):
    N = n_digits + 2
    A = [1] * N
    digits = []
    for _ in range(N - 2):
        q = 0
        for j in range(N - 1, -1, -1):
            A[j] = A[j] * 10 + q
            q = A[j] // (j + 2)
            A[j] %= (j + 2)
        digits.append(str(q))
    return "2." + "".join(digits)

print(spigot_algorithm(50))
# 2.71828182845904523536028747135266249775724709369995
```

**7-2. CORDIC algorithm** — Jack Volder, 1959

**Core idea**: It computes `e^\theta` using only additions and bit shifts (multiplication by 2⁻ⁱ). It relies on the relation `e^z = \sinh(z)+\cosh(z)`, and was originally devised for computing trigonometric functions in navigation computers.

d) Python
```python
import math

def cordic_exp(theta=1.0, iterations=40):
    x, y, z, gain = 1.0, 0.0, theta, 1.0
    repeat_indices = {4, 13, 40, 121}
    i, steps_done = 1, 0
    while steps_done < iterations:
        for _ in range(2 if i in repeat_indices else 1):
            d = 1 if z >= 0 else -1
            atanh_i = math.atanh(2 ** -i)
            x, y, z = x + d*y*2**-i, y + d*x*2**-i, z - d*atanh_i
            gain *= math.sqrt(1 - 2 ** (-2*i))
            steps_done += 1
        i += 1
    return (x + y) / gain

print(cordic_exp(1.0))  # 2.7182818285
```

**7-3. AGM (arithmetic–geometric mean)** — the Gauss–Legendre family

**Core idea**: Compute `\ln(x)` to high precision with the AGM, then combine it with the property `\ln(e)=1` and bisection to work backward to e.

d) Python
```python
import math

def agm(a, b, iterations=30):
    for _ in range(iterations):
        a, b = (a + b) / 2, math.sqrt(a * b)
    return a

def agm_based_ln(x, precision_bits=60):
    s = x * (2 ** precision_bits)
    a = agm(1.0, 4 / s)
    return math.pi / (2 * a) - precision_bits * math.log(2)

def find_e_via_agm_bisection(lo=2.5, hi=3.0, iters=60):
    for _ in range(iters):
        mid = (lo + hi) / 2
        if agm_based_ln(mid) < 1: lo = mid
        else: hi = mid
    return (lo + hi) / 2

print(find_e_via_agm_bisection())  # 2.7182818285
```

---

## 8. Other Variants and Approximations

- **Bisection**: Using the property `\ln(e)=1`, search by bisection for the `x` that satisfies `\ln(x)=1`.
- **Euler's 18-digit computation**: Euler used this variant of the series to compute e to 18 digits.

```latex
e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \cdots
```

---

## Overview: Ways to Compute e at a Glance

**1. Limit**
- Representative method: `(1 + 1/n)^n`
- Discoverer / year: Bernoulli, 1683
- Convergence speed: O(1/n)
- Suitability for visualization: moderate

**2. Series**
- Representative methods: `\sum 1/k!`, Dobiński's formula
- Discoverer / year: Newton/Euler, ~1665–1727 / Dobiński, 1877
- Convergence speed: extremely fast
- Suitability for visualization: high

**3. Infinite products**
- Representative methods: Catalan's product, Pippenger's product
- Discoverer / year: 1873 / 1980
- Convergence speed: fast (`1/2^n`)
- Suitability for visualization: high

**4. Continued fraction**
- Representative method: Euler's continued fraction
- Discoverer / year: Euler, 1737
- Convergence speed: fast
- Suitability for visualization: high

**5. Stochastic and combinatorial**
- Representative methods: sum of uniform variables, derangements
- Discoverer / year: — / Montmort, 1708
- Convergence speed: O(1/√n)
- Suitability for visualization: very high

**6. Algorithms**
- Representative methods: spigot, CORDIC, AGM
- Discoverer / year: ~1990s / Volder 1959 / Gauss–Legendre
- Convergence speed: fast
- Suitability for visualization: low to moderate

---

## Some Interesting Coincidences (Aside)

From the cases in the companion π article of "combinations of π and e that land close to an integer", here are some worth looking at with e at the center.

**1) Approximations not yet fully explained**
- `163(\pi - e) \approx 69` — precisely `68.99966\ldots`. It is intriguing that the Heegner number 163 shows up again, after the Ramanujan constant (`e^{\pi\sqrt{163}}`), but no complete theoretical explanation of this approximation exists yet (Irkhin, 2022, arXiv:2206.07174).
- `\pi^2 \approx 4e - 1` — an error of about 0.04%.

**2) Cases explained only recently**
- `e^{\pi} - \pi \approx 20` (precisely `19.9991\ldots`) — discovered almost simultaneously by Sloane, Conway, and Plouffe in 1988, but the "why" remained a mystery for a long time. It was widely settled only in 2023, through the fact that the first term overwhelmingly dominates in the Jacobi theta function identity `\sum(8\pi k^2-2)e^{-\pi k^2}=1`.

**3) Pure memorization tricks (not mathematical coincidences)**
- `e = 2.7\ 1828\ 1828\ 45\ 90\ 45\ \ldots` — a well-known mnemonic based on the fact that Andrew Jackson was the **7**th President of the United States and was elected in **1828** (and re-elected), so "1828" repeats twice. It is often used among American students.
- A fun true story: in 2004, Google set the target amount for its initial public offering (IPO) at **$2,718,281,828** — exactly `e \times 10^9` dollars (dropping the "45" at the cents level).

---

## Notes
- The Mathematica code first states each definition with infinite-operation symbols such as `Sum`, `Product`, and `Limit`, then obtains finite-term approximations with `N[...]`.
- The Python code uses only the standard library (`math`, `random`, `fractions`). If you need higher precision, use `decimal` or `mpmath`.
- The matrix exponential (Padé approximation + scaling-and-squaring) is widely used in practice, but this article focuses on computing the scalar e and leaves it out. I can put together a separate write-up if you need it.
- All values were checked by running the code and comparing against the true value `e = 2.718281828459045\ldots`.
