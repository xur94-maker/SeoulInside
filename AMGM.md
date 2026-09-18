# The Arithmetic Mean–Geometric Mean (AM-GM) Inequality

---

## TL;DR (Understanding AM-GM through A·B·C)

**"For two numbers A and B, the average is always greater than or equal to the square root of the product."**

---

## What is AM-GM?

**Suppose we have two numbers, A and B.**

```
(A + B) / 2  ≥  √(A × B)
```

- Left side: **arithmetic mean** (just add and divide by 2)
- Right side: **geometric mean** (multiply and take the square root)

**In other words, "the sum divided" is always greater than or equal to "the product rooted."**

---

## Let's check with numbers

**Example 1: A = 4, B = 9**

```
Left:  (4 + 9) / 2  =  6.5
Right: √(4 × 9)     =  √36  =  6
Result: 6.5  ≥  6  ✓
```

**Example 2: A = 5, B = 5 (equal numbers)**

```
Left:  (5 + 5) / 2  =  5
Right: √(5 × 5)     =  5
Result: 5  =  5  (equality!)
```

**Example 3: A = 1, B = 100**

```
Left:  (1 + 100) / 2  =  50.5
Right: √(1 × 100)     =  10
Result: 50.5  ≥  10  ✓
```

---

## When does equality hold?

```
Equality holds only when A = B
```

**In other words, "=" holds only when the two numbers are exactly equal.**

- A = 4, B = 4 → equality ✓
- A = 4, B = 9 → not equality ✗

---

## Extending to three numbers A, B, C

**With three numbers:**

```
(A + B + C) / 3  ≥  ∛(A × B × C)
```

**Numeric example: A = 1, B = 4, C = 9**

```
Left:  (1 + 4 + 9) / 3  =  14/3  ≈  4.67
Right: ∛(1 × 4 × 9)     =  ∛36   ≈  3.30
Result: 4.67  ≥  3.30  ✓
```

---

## Extending to n numbers

**With n numbers A₁, A₂, ..., Aₙ:**

```
(A₁ + A₂ + ... + Aₙ) / n  ≥  ⁿ√(A₁ × A₂ × ... × Aₙ)
```

**In words:**

> **"The sum of everything divided by n ≥ the n-th root of everything multiplied together."**

---

## Why does it matter?

### Optimization (finding the largest value)

**Problem: Among rectangles with perimeter 20, which has the largest area?**

```
width = A, height = B, perimeter = 2(A + B) = 20
→ A + B = 10

Area = A × B

AM-GM:  (A + B) / 2  ≥  √(A × B)
        10 / 2  ≥  √(area)
        5  ≥  √(area)
        area  ≤  25
```

**Equality condition: A = B = 5 (a square)**

**→ "For a fixed perimeter, the square has the largest area."**

### Finance (investment returns)

**3-year returns: +40%, −30%, +20%**

```
Arithmetic mean:  (40 − 30 + 20) / 3  =  10%
Geometric mean:  ∛(1.4 × 0.7 × 1.2) − 1  ≈  5.55%
```

**→ "The arithmetic mean is 10%, but the actual compounded return is only 5.55%."**

**Reason: volatility causes losses.**

### Data structures and algorithms

**"If the sum is fixed, the product is maximized when all terms are equal."**

This principle is used in algorithm analysis, resource allocation, circuit design, and more.

---

## The chain of means (two numbers A, B)

**For two numbers A, B:**

```
2AB/(A+B)  ≤  √(AB)  ≤  (A+B)/2  ≤  √((A²+B²)/2)
    HM          GM         AM          QM
```

**In words:**

> **Harmonic mean ≤ Geometric mean ≤ Arithmetic mean ≤ Quadratic mean**

**Numeric example: A = 1, B = 4**

```
HM = 2·1·4/(1+4)  =  8/5   =  1.6
GM = √(1·4)        =  2
AM = (1+4)/2       =  2.5
QM = √((1+16)/2)   =  √8.5  ≈  2.92

1.6  ≤  2  ≤  2.5  ≤  2.92  ✓
```

---

## Summary of equality conditions

| Means | Equality condition |
|---|---|
| AM = GM | A = B |
| GM = HM | A = B |
| AM = QM | A = B |
| All equal | A = B |

**Conclusion: for all means to be equal, A = B is required.**

---

## Common mistakes

### Mistake 1: Plugging in negative numbers

```
A = −1, B = −4
AM = (−1 − 4)/2 = −2.5
GM = √((−1)(−4)) = 2
→ AM < GM  ✗ (does not hold)
```

**→ AM-GM holds only for non-negative numbers.**

### Mistake 2: Ignoring the equality condition

```
A = 1, B = 4
AM = 2.5, GM = 2
→ not equality
```

**→ In optimization problems, you must check the equality condition to find the optimum.**

### Mistake 3: Ignoring the sum of weights

**In weighted AM-GM:**

```
λ₁ + λ₂ + ... + λₙ = 1  (mandatory!)
```

**→ Without this condition, the inequality does not hold.**

----


----
## Table of Contents

1. Definition and basic forms of the inequality
2. Proofs (8 methods)
3. Extended inequality chain: HM ≤ GM ≤ AM ≤ QM
4. Numerical examples
5. Geometric and optimization applications
6. Financial and investment applications (volatility drag)
7. Engineering and physics applications
8. Computer science and modern optimization theory applications
9. Economics applications
10. Standing in pure mathematics and competitions
11. Advanced: Gauss's arithmetic-geometric mean iteration (AGM) and the computation of π
12. Advanced: generalization to Muirhead's inequality
13. Advanced: comparison with the method of Lagrange multipliers
14. Advanced: structural connection to information theory
15. Counterexamples, misconceptions, and failure cases
16. Self-check problems
17. Summary table

---

## 0. Guide to the four-notation format

This document presents **key formulas** in four parallel representations:

- **Unicode**: an intuitive grasp of the formula's meaning
- **LaTeX**: the formal notation of mathematics
- **Mathematica**: a symbolic computation language
- **Python (SymPy)**: a programming language

This lets readers unfamiliar with LaTeX still understand the content, while Mathematica/Python users can run the code immediately.

---

## 1. Definition and basic forms of the inequality

### 1.1 Basic form

**Unicode**

```text
(x₁ + x₂ + ... + xₙ) / n  ≥  ⁿ√(x₁ x₂ ... xₙ)
```

**LaTeX**

```latex
\frac{x_1 + x_2 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 x_2 \cdots x_n}
```

**Mathematica**

```mathematica
Assuming[And @@ (# >= 0 & /@ x),
  Sum[x[[i]], {i, 1, n}]/n >= Product[x[[i]], {i, 1, n}]^(1/n)]
```

**Python (SymPy)**

```python
from sympy import symbols, Sum, Product, Rational, Ge

x = symbols('x1:5', nonnegative=True)
n = len(x)
am = Sum(x[i], (i, 0, n-1)) / n
gm = Product(x[i], (i, 0, n-1)) ** Rational(1, n)
print(Ge(am, gm))
```

The left-hand side is called the **arithmetic mean (AM)**, and the right-hand side the **geometric mean (GM)**.

**Equality condition**: equality holds if and only if $x_1 = x_2 = \cdots = x_n$.

### 1.2 The case n = 2 (the most widely used form)

**Unicode**

```text
(a + b) / 2  ≥  √(ab)     (a, b ≥ 0)
```

**LaTeX**

```latex
\frac{a+b}{2} \geq \sqrt{ab}, \qquad a, b \geq 0
```

**Mathematica**

```mathematica
Assuming[a >= 0 && b >= 0, (a + b)/2 >= Sqrt[a b]]
```

**Python (SymPy)**

```python
from sympy import symbols, sqrt, Ge

a, b = symbols('a b', nonnegative=True)
print(Ge((a + b)/2, sqrt(a*b)))
```

This inequality already appears implicitly in Euclid's *Elements* (c. 300 BCE). Ancient mathematicians exploring the relationship between geometric figures and numbers had grasped it intuitively.

### 1.3 Weighted AM-GM

**Unicode**

```text
λ₁x₁ + λ₂x₂ + ... + λₙxₙ  ≥  x₁^λ₁ · x₂^λ₂ · ... · xₙ^λₙ
(where λᵢ ≥ 0, ∑λᵢ = 1)
```

**LaTeX**

```latex
\sum_{i=1}^n \lambda_i x_i \geq \prod_{i=1}^n x_i^{\lambda_i}, \qquad \lambda_i \geq 0, \sum \lambda_i = 1
```

**Mathematica**

```mathematica
Assuming[And @@ (# >= 0 & /@ x) && And @@ (# >= 0 & /@ lam)
         && Total[lam] == 1,
  Sum[lam[[i]] x[[i]], {i, 1, n}] >= Product[x[[i]]^lam[[i]], {i, 1, n}]]
```

**Python (SymPy)**

```python
from sympy import symbols, Sum, Product, Ge

x = symbols('x1:4', nonnegative=True)
lam = symbols('l1:4', nonnegative=True)
n = len(x)
am = Sum(lam[i] * x[i], (i, 0, n-1))
gm = Product(x[i]**lam[i], (i, 0, n-1))
print(Ge(am, gm))
```

Setting $\lambda_i = 1/n$ reduces this to the ordinary AM-GM inequality. If the weights do not sum to 1, the inequality does not hold.

### 1.4 Definitions of the three means

For non-negative reals $x_1, \ldots, x_n$:

- **Arithmetic mean (AM)**: $\displaystyle A = \frac{x_1 + \cdots + x_n}{n}$
- **Geometric mean (GM)**: $\displaystyle G = \sqrt[n]{x_1 \cdots x_n}$
- **Harmonic mean (HM)**: $\displaystyle H = \frac{n}{\frac{1}{x_1} + \cdots + \frac{1}{x_n}}$ $(x_i > 0)$
- **Quadratic mean (QM)**: $\displaystyle Q = \sqrt{\frac{x_1^2 + \cdots + x_n^2}{n}}$

### 1.5 The meaning of the equality condition

An "equality condition" refers to the case where an inequality actually becomes an equation. In AM-GM, equality holds only when all variables are exactly equal. This condition is the key information that reveals the optimal point in optimization problems.

---

## 2. Proofs (8 methods)

### 2.1 Proof for n = 2 (using a perfect square)

For $a, b \geq 0$, $(\sqrt{a}-\sqrt{b})^2 \geq 0$ always holds. Expanding:

```latex
a - 2\sqrt{ab} + b \geq 0 \implies a+b \geq 2\sqrt{ab} \implies \frac{a+b}{2}\geq\sqrt{ab}
```

Equality holds only when $\sqrt a = \sqrt b$, i.e., $a=b$. ■

### 2.2 Cauchy's forward-backward induction

First rigorously proven by Cauchy in 1821, this method proceeds in two stages.

**Forward stage (extending to powers of 2):** Assuming the inequality holds for $n=k$, split into two groups to show it holds for $n=2k$.

```latex
\frac{x_1+\cdots+x_k}{k}\geq\sqrt[k]{x_1\cdots x_k}, \qquad \frac{x_{k+1}+\cdots+x_{2k}}{k}\geq\sqrt[k]{x_{k+1}\cdots x_{2k}}
```

Applying AM-GM (in its n=2 form) to these two inequalities again gives:

```latex
\frac{x_1+\cdots+x_{2k}}{2k}\geq\sqrt{\sqrt[k]{x_1\cdots x_k}\cdot\sqrt[k]{x_{k+1}\cdots x_{2k}}}=\sqrt[2k]{x_1\cdots x_{2k}}
```

Repeating this establishes the result for every power of 2: $n=2,4,8,16,\ldots$

**Backward stage (reducing to an arbitrary n):** Assuming it holds for $n=k$, show it also holds for $n=k-1$. Given $x_1,\ldots,x_{k-1}$, add an extra term $x_k := \dfrac{x_1+\cdots+x_{k-1}}{k-1}$.

```latex
\frac{x_1+\cdots+x_{k-1}+x_k}{k}\geq\sqrt[k]{x_1\cdots x_{k-1}x_k}
```

Since the left side equals $x_k$ by definition, $x_k \geq \sqrt[k]{x_1\cdots x_{k-1}x_k}$. Raising both sides to the $k$-th power and dividing by $x_k^{k-1}$:

```latex
x_k^{k-1} \geq x_1\cdots x_{k-1} \implies \frac{x_1+\cdots+x_{k-1}}{k-1}\geq\sqrt[k-1]{x_1\cdots x_{k-1}}
```

Combining the forward stage (up to powers of 2) with the backward stage (reducing to any n) completes the proof for **every natural number n**. ■

### 2.3 Proof via Jensen's inequality

Since $\ln x$ is concave ($\ln''(x) = -1/x^2 < 0$), Jensen's inequality gives:

```latex
\frac{1}{n}\sum_{i=1}^n \ln x_i \leq \ln\!\left(\frac{1}{n}\sum_{i=1}^n x_i\right)
```

The left side equals $\ln\big((x_1\cdots x_n)^{1/n}\big) = \ln G$, and the right side equals $\ln A$, so:

```latex
\ln G \leq \ln A
```

Since $\ln$ is monotonically increasing, exponentiating gives $G \leq A$, completing the AM-GM proof. **Advantage of this method**: adding weights immediately generalizes it to weighted AM-GM. ■

### 2.4 Pólya's exponential method

Let $f(x) = e^{x-1} - x$. Then $f'(x) = e^{x-1} - 1$, and $f'(1) = 0$, $f(1) = 0$ is the unique minimum. Hence for every real $x$:

```latex
x \leq e^{x-1}
```

Let $A = \frac{1}{n}\sum x_i$ and $y_i = x_i/A$. Then:

```latex
\frac{x_i}{A} \leq e^{x_i/A - 1}
```

Multiplying over all $i$:

```latex
\frac{x_1\cdots x_n}{A^n} \leq \exp\!\left(\sum \frac{x_i}{A} - n\right) = e^{n-n} = 1
```

Hence $x_1\cdots x_n \leq A^n$, i.e., $G \leq A$. ■

### 2.5 Smoothing method

Sort $a_1,\ldots,a_n$ in decreasing order. If they are not all equal, replace $a_1$ (the maximum) and $a_n$ (the minimum) with:

```latex
M = \frac{a_1+a_n}{2}, \qquad a_1+a_n - M = M
```

The arithmetic mean is unchanged. The change in the geometric mean:

```latex
M \cdot M - a_1 a_n = \left(\frac{a_1+a_n}{2}\right)^2 - a_1 a_n = \frac{(a_1-a_n)^2}{4} > 0
```

So GM strictly increases. Repeating this operation finitely many times makes all numbers equal to $A$, so AM = GM. Since GM increases monotonically throughout, the original $G \leq A$ follows. ■

### 2.6 Proof via Lagrange multipliers (reverse direction)

Maximize $\prod x_i$ subject to the fixed constraint $\sum x_i = S$. The Lagrangian:

```latex
L = \prod x_i + \lambda\left(\sum x_i - S\right)
```

```latex
\frac{\partial L}{\partial x_i} = \prod_{j \neq i} x_j + \lambda = 0
```

Since this holds for every $i$, $\prod_{j \neq i} x_j$ must be constant → $x_i = S/n$. At this point the maximum is $G = S/n = A$. Hence $G \leq A$. ■

### 2.7 Chrystal's induction

Assume the inequality holds for $n$; prove it for $n+1$. Suppose $a_{n+1}$ is the largest among $a_1,\ldots,a_{n+1}$.

```latex
\bar a_n = \frac{a_1+\cdots+a_n}{n}, \qquad A_{n+1} = \frac{a_1+\cdots+a_{n+1}}{n+1}
```

Since $a_{n+1} \geq A_{n+1} \geq \bar a_n$:

```latex
(a_{n+1} - A_{n+1})(A_{n+1} - \bar a_n) \geq 0
```

Rearranging gives $A_{n+1}^{n+1} \geq \bar a_n^n \cdot a_{n+1}$. Combined with the induction hypothesis $\bar a_n^n \geq a_1\cdots a_n$:

```latex
A_{n+1}^{n+1} \geq a_1\cdots a_{n+1} \implies A_{n+1} \geq \sqrt[n+1]{a_1\cdots a_{n+1}}
```

■

### 2.8 Proof via Bernoulli's inequality

Uses $(1+t)^n \geq 1+nt$ (Bernoulli's inequality, $t \geq -1$, $n \geq 1$). For $x_i > 0$, let $t_i = x_i/A - 1 \geq -1$, so $\sum t_i = 0$. By Bernoulli's inequality:

```latex
\prod \frac{x_i}{A} = \prod (1+t_i) \leq \left(1 + \frac{\sum t_i}{n}\right)^n = 1
```

Hence $G \leq A$. ■

---

## 3. Extended inequality chain: HM ≤ GM ≤ AM ≤ QM

Defining the power mean $M_p(x) = \left(\dfrac{1}{n}\sum x_i^p\right)^{1/p}$:

```latex
\min(x_i) \leq \underbrace{M_{-1}}_{\text{harmonic mean HM}} \leq \underbrace{M_0}_{\text{geometric mean GM}} \leq \underbrace{M_1}_{\text{arithmetic mean AM}} \leq \underbrace{M_2}_{\text{quadratic mean QM}} \leq \max(x_i)
```

($M_0$ is defined as the limit $p\to0$, and it is known to coincide with the geometric mean.) $M_p$ increases monotonically as $p$ increases. AM-GM is just one segment in the middle of this entire chain.

### 3.1 Two-variable form

**Unicode**

```text
2ab/(a+b)  ≤  √(ab)  ≤  (a+b)/2  ≤  √((a²+b²)/2)
```

**LaTeX**

```latex
\frac{2ab}{a+b} \leq \sqrt{ab} \leq \frac{a+b}{2} \leq \sqrt{\frac{a^2+b^2}{2}}
```

**Mathematica**

```mathematica
Assuming[a > 0 && b > 0,
  2 a b/(a + b) <= Sqrt[a b] <= (a + b)/2 <= Sqrt[(a^2 + b^2)/2]]
```

**Python (SymPy)**

```python
from sympy import symbols, sqrt, And

a, b = symbols('a b', positive=True)
chain = And(
    2*a*b/(a+b) <= sqrt(a*b),
    sqrt(a*b) <= (a+b)/2,
    (a+b)/2 <= sqrt((a**2 + b**2)/2)
)
print(chain)
```

### 3.2 Proof of HM ≤ GM

Apply AM-GM to $1/a, 1/b$:

```latex
\frac{1/a + 1/b}{2} \geq \sqrt{\frac{1}{ab}} \implies \frac{a+b}{2ab} \geq \frac{1}{\sqrt{ab}} \implies \frac{2ab}{a+b} \leq \sqrt{ab}
```

### 3.3 Proof of AM ≤ QM

```latex
(a+b)^2 \leq 2(a^2+b^2) \iff 0 \leq (a-b)^2
```

### 3.4 Recent research on the mean chain

The relationship between weighted power means and Muirhead's inequality continues to be actively researched. In particular, a 2018 paper in *Symmetry* showed that **weighted AM-GM is mathematically equivalent to Hölder's inequality and to the weighted power-mean inequality**, revealing that these three inequalities are, in effect, the same mathematical content expressed in different languages.

---

## 4. Numerical examples

Let's start with the simplest verifications.

### Example 1: basic n=2

$a=4$, $b=9$: $A=6.5$, $G=6$. Check: $6.5 \geq 6$. ✓

### Example 2: verifying equality

$a=b=5$: $A=5$, $G=5$. Equality. ✓

### Example 3: investment returns (volatility drag)

3-year returns: $+40\%$, $-30\%$, $+20\%$.

- Arithmetic mean: $\bar r_A = \dfrac{40-30+20}{3}\% = 10\%$
- Geometric mean: $1+\bar r_G = \sqrt[3]{1.4 \times 0.7 \times 1.2} \approx \sqrt[3]{1.176} \approx 1.0555$

$\bar r_G \approx 5.55\%$.

Path of 100,000 won: $10 \to 14 \to 9.8 \to 11.76$ (in units of 10,000 won). After 3 years, 117,600 won.

Volatility drag $= \bar r_A - \bar r_G \approx 4.45\%$.

Approximation: $\bar r_G \approx \bar r_A - \sigma^2/2$. The $\sigma^2$ in this approximation is the variance of the **log returns** $\ln(1+r_i)$. With $\ln 1.4 \approx 0.3365$, $\ln 0.7 \approx -0.3567$, $\ln 1.2 \approx 0.1823$, the variance of these three values is $\sigma^2 \approx 0.088$, so $\sigma^2/2 \approx 4.4\%$, closely matching the actual difference (4.45%). (Note: using the variance of the simple returns themselves instead gives $\sigma^2 \approx 0.087$, a different value — the approximation requires the variance of the log returns.) ✓

### Example 4: rectangle with fixed perimeter

Perimeter $2(x+y)=8$ → $x+y=4$. Area $\text{Area}=xy \leq \left(\dfrac{x+y}{2}\right)^2 = 4$.

Equality at $x=y=2$ (a square). Maximum area 4.

### Example 5: box with fixed surface area

Surface area $S=2(ab+bc+ca)=54$ → $ab+bc+ca=27$.

Three-variable AM-GM:

```latex
\frac{ab+bc+ca}{3} \geq \sqrt[3]{(ab)(bc)(ca)} = \sqrt[3]{(abc)^2} = V^{2/3}
```

$9 \geq V^{2/3}$ → $V \leq 27$. Equality at $ab=bc=ca$ → $a=b=c=3$. Maximum volume 27.

### Example 6: positive number plus its reciprocal

$a + 1/a \geq 2$, equality at $a=1$. For $a=3$: $3 + 1/3 = 3.333 \geq 2$. ✓

### Example 7: three-variable chain

$a=1, b=4, c=9$:

- $G = \sqrt[3]{36} \approx 3.3019$
- $A = 14/3 \approx 4.6667$

Check: $3.3019 \leq 4.6667$. ✓

---

## 5. Geometric and optimization applications

### 5.1 Maximum area of a rectangle with fixed perimeter

With perimeter $2(x+y)=P$ fixed, the maximum of area $A=xy$:

```latex
\frac{x+y}{2}\geq\sqrt{xy} \implies \frac{P/2}{2}\geq\sqrt A \implies A\leq\left(\frac{P}{4}\right)^2
```

Equality holds at $x=y$, i.e. for a **square**. Completed algebraically, with no derivatives.

### 5.2 Maximum volume of a box with fixed surface area (proof of the cube)

Width $a$, depth $b$, height $c$, with fixed surface area $S=2(ab+bc+ca)$; maximize volume $V=abc$.

Apply three-variable AM-GM to $ab, bc, ca$:

```latex
\frac{ab+bc+ca}{3}\geq\sqrt[3]{(ab)(bc)(ca)}=\sqrt[3]{a^2b^2c^2}=V^{2/3}
```

Since the left side equals $S/6$:

```latex
V^{2/3}\leq\frac{S}{6} \implies V\leq\left(\frac{S}{6}\right)^{3/2}
```

Equality condition $ab=bc=ca \Leftrightarrow a=b=c$ — the maximum volume is achieved by a **cube**.

### 5.3 The general principle of derivative-free optimization

"For positive numbers with a fixed sum, the product is maximized when all are equal" — this is the optimization principle behind AM-GM.

**Example: $\min(x + 4/x)$ for $x>0$**

**Unicode**

```text
x + 4/x  ≥  2√(x · 4/x)  =  4,   equality at x = 2
```

**LaTeX**

```latex
x + \frac{4}{x} \geq 2\sqrt{x \cdot \frac{4}{x}} = 4, \qquad x = 2
```

**Mathematica**

```mathematica
Minimize[{x + 4/x, x > 0}, x]   (* {4, {x -> 2}} *)
```

**Python (SymPy)**

```python
from sympy import symbols, sqrt

x = symbols('x', positive=True)
expr = x + 4/x
print(expr.subs(x, 2))   # 4
```

**Example: $\max x^2(1-x)$ for $0<x<1$**

```latex
x^2(1-x) = 4 \cdot \frac{x}{2} \cdot \frac{x}{2} \cdot (1-x) \leq 4\left(\frac{\frac{x}{2}+\frac{x}{2}+(1-x)}{3}\right)^3 = 4 \cdot \frac{1}{27} = \frac{4}{27}
```

Equality at $\frac{x}{2} = 1-x$ → $x=2/3$. ✓

### 5.4 The nearest point to the origin, and generalized minimization problems

Problems asking for the minimum area or volume cut off in the first quadrant (or first octant) by a curve or plane can be solved with the same logic.

For example, finding the minimum area of the triangle that the plane $\frac{x}{a} + \frac{y}{b} = 1$ $(a,b>0)$ cuts off in the first quadrant involves:

```latex
\text{Area} = \frac{ab}{2}
```

Applying AM-GM to this, or substituting the constraint, leads to the same conclusion. Such problems extend to research on "generalized AM-GM inequalities" for arbitrary dimensions and surface shapes.

---

## 6. Financial and investment applications: volatility drag

For returns $r_1,\ldots,r_n$ over $n$ years, with growth factors $x_i = 1+r_i$.

- Arithmetic-mean return: $\bar r_A = \dfrac{1}{n}\sum r_i$
- Geometric-mean (actual compound) return: $1+\bar r_G = \sqrt[n]{\prod x_i}$

Applying AM-GM directly:

```latex
\frac{\sum x_i}{n}\geq\sqrt[n]{\prod x_i} \implies 1+\bar r_A \geq 1+\bar r_G \implies \bar r_A \geq \bar r_G
```

**The arithmetic-mean return is always greater than or equal to the geometric-mean (compound) return.** Equality holds only when volatility is zero.

Using a normal-distribution approximation:

```latex
\bar r_G \approx \bar r_A - \frac{\sigma^2}{2}
```

Here $\sigma^2$ is the variance of the log returns $\ln(1+r_i)$, and $\sigma^2/2$ is the "volatility drag." In practice, reporting multi-year fund performance using the arithmetic mean always produces a number inflated above the true figure; for this reason, most financial planners and mutual funds use the compound annual growth rate (CAGR, the geometric mean) as their official metric.

**Numeric example:** returns of +40%, −30%, +20%

```latex
\bar r_A = \frac{40-30+20}{3}\% = 10\%, \qquad \bar r_G = \sqrt[3]{1.4\times0.7\times1.2}-1 \approx 5.55\%
```

100,000 won $\to$ 140,000 won $\to$ 98,000 won $\to$ 117,600 won: the actual average annual growth is 5.55%, not 10%.

### 6.1 The key inequality in four notations

**Unicode**

```text
r̄_A  ≥  r̄_G
r̄_G  ≈  r̄_A − σ²/2
```

**LaTeX**

```latex
\bar r_A \geq \bar r_G, \qquad \bar r_G \approx \bar r_A - \frac{\sigma^2}{2}
```

**Mathematica**

```mathematica
rA[r_] := Mean[r]
rG[r_] := (Times @@ (1 + r))^(1/Length[r]) - 1
drag[r_] := rA[r] - rG[r]
drag[{0.4, -0.3, 0.2}]   (* ≈ 0.0445 *)
```

**Python (NumPy)**

```python
import numpy as np

r = np.array([0.4, -0.3, 0.2])
rA = np.mean(r)
rG = np.prod(1 + r)**(1/len(r)) - 1
print(f"rA = {rA:.4f}, rG = {rG:.4f}, drag = {rA - rG:.4f}")
# rA = 0.1000, rG = 0.0555, drag = 0.0445
```

### 6.2 The relationship between leverage and volatility drag

If the leverage multiple is $k$, volatility scales roughly by $k$, and since drag is proportional to $\sigma^2$, drag scales roughly by $k^2$. Example: with no leverage, a volatility of 50% gives a drag of $50\%^2/2=12.5\%$, but with 2x leverage, volatility becomes 100% and drag becomes $100\%^2/2=50\%$ — a fourfold increase. This is the core mathematical reason why holding leveraged ETFs long-term is risky.

### 6.3 Quantitative analysis of how tight AM-GM is

There is also research that quantitatively analyzes how "tight" the AM-GM inequality is. A 2008 arXiv paper presented a refined inequality expressing the difference between AM and GM in terms of **variance**:

Larger variance means a larger gap between AM and GM, and for large $n$, a probabilistic analysis suggests the "typical" upper bound falls below 0.82. This indicates that the approximation $\bar r_G \approx \bar r_A - \sigma^2/2$ for volatility drag is more than a rough approximation — it has a **quantitative bound**.

---

## 7. Engineering and physics applications

### 7.1 The maximum power transfer theorem — derived without calculus

One of the most famous results in electrical engineering is the **maximum power transfer theorem** (to deliver maximum power from a source with internal resistance $R_s$ to a load $R_L$, we need $R_L=R_s$). It is usually proved with derivatives, but AM-GM makes the proof much shorter.

For a source with voltage $V$ and internal resistance $R_s$, the power delivered to load $R_L$ is:

```latex
P(R_L) = \frac{V^2 R_L}{(R_s+R_L)^2}
```

Instead of maximizing $P$, we minimize $1/P$:

```latex
\frac{1}{P} = \frac{(R_s+R_L)^2}{V^2 R_L} = \frac{1}{V^2}\left(\frac{R_s^2}{R_L} + 2R_s + R_L\right)
```

Applying AM-GM to $\dfrac{R_s^2}{R_L}+R_L$ on the right (excluding the constant term $2R_s$):

```latex
\frac{R_s^2}{R_L} + R_L \;\geq\; 2\sqrt{\frac{R_s^2}{R_L}\cdot R_L} = 2R_s
```

with equality when $\dfrac{R_s^2}{R_L}=R_L \iff R_L=R_s$. Therefore:

```latex
\frac{1}{P} \geq \frac{4R_s}{V^2} \;\;\Longrightarrow\;\; P \leq \frac{V^2}{4R_s}, \qquad \text{equality at } R_L=R_s
```

In other words, **the maximum power transfer theorem $R_L=R_s$ and the maximum power $P_{\max}=\dfrac{V^2}{4R_s}$ both fall out simultaneously from a single application of AM-GM, without calculus.** This is a case where the principle from §13 — "AM-GM is derivative-free optimization" — applies directly to a pure physics/engineering problem.

### 7.2 Material-minimizing design: the optimal proportions of a cylindrical container

Consider minimizing the surface area $S=2\pi r^2+2\pi rh$ of a cylinder (including lid) with fixed volume $V=\pi r^2h$. Split $S$ into three terms:

```latex
S = 2\pi r^2 + \pi rh + \pi rh
```

Apply three-variable AM-GM:

```latex
\frac{2\pi r^2+\pi rh+\pi rh}{3} \geq \sqrt[3]{(2\pi r^2)(\pi rh)(\pi rh)} = \sqrt[3]{2\pi^3r^4h^2}
```

Since $r^2h = V/\pi$, substituting $r^4h^2=(r^2h)^2=(V/\pi)^2$:

```latex
\sqrt[3]{2\pi^3\cdot\frac{V^2}{\pi^2}} = \sqrt[3]{2\pi V^2}
```

Hence $S\geq 3\sqrt[3]{2\pi V^2}$. Equality condition $2\pi r^2=\pi rh \iff h=2r$ — surface area is minimized **when the height equals the diameter**. This is the same structure ("equality condition = the most balanced shape") from §5.2's box (cube) result, applied to a cylinder.

### 7.3 Resource allocation: optimal distribution of resources across channels/paths

Given $n$ communication channels (or parallel processing paths) sharing a total resource $S$ (bandwidth, power, etc.) allocated as $x_1,\ldots,x_n$, and assuming each channel's delay is proportional to $1/x_i$, what allocation minimizes total delay $\sum 1/x_i$?

Simply use HM≤AM from §3: with $\sum x_i = S$,

```latex
\frac{S}{n} = \frac{\sum x_i}{n} \;\geq\; \frac{n}{\sum(1/x_i)}
```

Rearranging:

```latex
\sum_{i=1}^n \frac{1}{x_i} \;\geq\; \frac{n^2}{S}
```

with equality at $x_1=\cdots=x_n=S/n$, meaning **equal allocation minimizes total delay**. Problems of the form "distribute a fixed sum of resources to minimize the sum of reciprocals" — such as parallel-resistor allocation in circuits, network bandwidth distribution, and cache capacity allocation — are all solved by this single line.

---

## 8. Computer science and modern optimization theory applications

### 8.1 SAGE certificates (Sums of AM/GM Exponentials)

Proving that a polynomial or sum of exponentials $f(x)=\sum_\alpha c_\alpha e^{\langle\alpha,x\rangle}$ is non-negative for all $x$ is generally hard, but if the terms can be grouped via weighted AM-GM, it can be proven efficiently.

Given support points $\alpha_0,\ldots,\alpha_m$, weights $\lambda_i\geq0$ with $\sum\lambda_i=1$, and $\sum\lambda_i\alpha_i=\alpha_0$:

**Unicode**

```text
∑ᵢ λᵢ · e^⟨αᵢ, x⟩  ≥  e^⟨α₀, x⟩
```

**LaTeX**

```latex
\sum_{i=1}^m \lambda_i e^{\langle\alpha_i,x\rangle} - e^{\langle\alpha_0,x\rangle} \geq 0
```

**Mathematica**

```mathematica
sageCert[alphas_, lambdas_, x_] := 
  Sum[lambdas[[i]] Exp[alphas[[i]] . x], {i, Length[alphas]}] >= 
  Exp[alphas[[1]] . x]
```

**Python (NumPy)**

```python
import numpy as np

def sage_certificate(alphas, lambdas, x):
    lhs = sum(lam * np.exp(np.dot(a, x)) 
              for a, lam in zip(alphas[1:], lambdas[1:]))
    rhs = np.exp(np.dot(alphas[0], x))
    return lhs - rhs >= 0
```

This follows directly from weighted AM-GM. The set of such "AM/GM certificates" is called **SAGE**, and it is connected to **relative entropy programming** in convex optimization, and is implemented in actual polynomial optimization software.

Recent research has introduced **symmetry** into SAGE certificates. When a problem is invariant under the action of a group $G$, a symmetry-adapted decomposition theorem can be used to **reduce the size of the relative entropy program**, as systematically studied in a 2021 arXiv paper.

Also, research by Moustrou, Riener, Theobald, and Verdure ("Symmetric SAGE and SONC forms, exactness and quantitative gaps," arXiv:2312.10500, published in the *Journal of Symbolic Computation*) analyzed the relationship between **symmetric SAGE and SONC forms**, showing that in several symmetric cases, the SAGE or SONC property coincides with nonnegativity.

### 8.2 Noncommutative AM-GM and stochastic gradient descent (SGD)

The AM-GM inequality can be generalized to **matrices**. To prove that without-replacement sampling (shuffling) converges faster than with-replacement sampling in **stochastic gradient descent (SGD)** for machine learning, Recht and Ré (2012) proposed a noncommutative AM-GM conjecture for $n$ positive semidefinite matrices. They directly proved the conjecture (in expectation) for the case $m=n=2$ and for several classes of random matrices, and Zhang (2018) later extended it to $m=3$ with arbitrary $n$.

Lai and Lim (2020) showed that this conjecture is false in general. Using a noncommutative Positivstellensatz, they converted the conjecture into a semidefinite programming (SDP) problem and numerically confirmed **a concrete counterexample at $m=n=5$**. That is, it is not the case that "five or more matrices always break it" — rather, a counterexample was first found when both parameters $m,n$ in the conjecture reached 5, while the inequality holds for any $n$ when $m=2,3$ (small $m$). The case $m=4$ remains open.

This connection shows that AM-GM extends beyond pure mathematics to serve as a core tool in **modern machine learning theory**.

### 8.3 Use in algorithm analysis

AM-GM-style arguments appear when arguing for balanced partitioning in divide-and-conquer algorithms, or when deriving average-case upper bounds on resource usage. For example, when analyzing the time complexity $T(n) = 2T(n/2) + O(n)$ of a divide-and-conquer algorithm that splits a problem of size $n$ into two subproblems of size $n/2$, AM-GM can be used to bound the resource usage at each stage and show that balanced partitioning is optimal.

---

## 9. Economics applications

### 9.1 Cost minimization for the Cobb-Douglas production function — solved with weighted AM-GM instead of Lagrange

Given the production function $Y = A\,L^\alpha K^{1-\alpha}$ ($0<\alpha<1$, labor $L$, capital $K$), with labor price $w$ and capital price $r$, the problem of finding the minimum cost $C=wL+rK$ to achieve a target output $Y_0$ is usually solved using the method of Lagrange multipliers. Let's instead solve it directly with the **weighted AM-GM** from §1.3.

In weighted AM-GM ($\lambda_1+\lambda_2=1$ implies $\lambda_1y_1+\lambda_2y_2\geq y_1^{\lambda_1}y_2^{\lambda_2}$), set $\lambda_1=\alpha$, $\lambda_2=1-\alpha$, $y_1=\dfrac{wL}{\alpha}$, $y_2=\dfrac{rK}{1-\alpha}$:

```latex
\alpha\cdot\frac{wL}{\alpha} + (1-\alpha)\cdot\frac{rK}{1-\alpha} \;\geq\; \left(\frac{wL}{\alpha}\right)^{\alpha}\left(\frac{rK}{1-\alpha}\right)^{1-\alpha}
```

The left side is exactly $wL+rK=C$ (total cost). Rearranging the right side:

```latex
C \;\geq\; \left(\frac{w}{\alpha}\right)^{\alpha}\left(\frac{r}{1-\alpha}\right)^{1-\alpha}\cdot L^\alpha K^{1-\alpha}
```

Substituting the production constraint $Y_0=A\,L^\alpha K^{1-\alpha}$, i.e. $L^\alpha K^{1-\alpha}=Y_0/A$:

```latex
C \;\geq\; \frac{Y_0}{A}\left(\frac{w}{\alpha}\right)^{\alpha}\left(\frac{r}{1-\alpha}\right)^{1-\alpha}
```

The equality condition — the weighted AM-GM equality condition $y_1=y_2$ — is:

```latex
\frac{wL}{\alpha} = \frac{rK}{1-\alpha} \;\;\Longrightarrow\;\; \frac{K}{L} = \frac{(1-\alpha)\,w}{\alpha\,r}
```

This is exactly the **optimal capital-labor ratio for Cobb-Douglas cost minimization** that textbooks derive using Lagrange multipliers (or the marginal rate of technical substitution condition $MRTS=w/r$). The advantage confirmed in §13 — "AM-GM's proof length doesn't grow with the number of variables" — is applied here to economics in the form of "reading off the optimal factor allocation ratio directly, without calculus."

### 9.2 Economic interpretation of the equality condition

The equality condition $K/L=\dfrac{(1-\alpha)w}{\alpha r}$ from §9.1 means **the point at which marginal product per unit of spending becomes equal across production factors** (i.e., where the $\alpha$-weighted expenditure $wL/\alpha$ equals the $(1-\alpha)$-weighted expenditure $rK/(1-\alpha)$). This shows that the interpretation emphasized in §1.5 — "equality condition = point of balance" — takes the concrete form of "efficient allocation of resources (equalizing marginal products across production factors)" in economics.

---

## 10. Standing in pure mathematics and competitions

AM-GM is the most widely used tool among algebraic inequalities, appearing throughout introductory, intermediate, and olympiad-level problems. When it cannot be applied directly, terms are creatively split or combined with other inequalities. Let's work through two representative techniques.

### 10.1 Technique 1 — Splitting terms

**Problem**: For $a,b,c>0$, prove $a^4+a^4+b^4+c^4 \geq 4a^2bc$.

**Solution**: Apply AM-GM directly to the four terms.

```latex
\frac{a^4+a^4+b^4+c^4}{4} \geq \sqrt[4]{a^4\cdot a^4\cdot b^4\cdot c^4} = \sqrt[4]{a^8b^4c^4} = a^2bc
```

Multiplying both sides by 4 gives $a^4+a^4+b^4+c^4\geq4a^2bc$. Equality at $a=b=c$. ■

The key here is **deliberately putting $a^4$ twice on the left side**. To get $a^2bc$ on the right, the exponents need to be balanced $4:4:4:4$ so that taking the fourth root yields $a^2$; using $a^4$ only once would leave the term count mismatched, like $a^{4/4}\cdot(bc)^{4/4}\cdot\text{(empty slot)}$. "Artificially increasing the number of terms on the left to match the exponent ratio of the target right side" is the most common trick in AM-GM competition problems.

### 10.2 Technique 2 — Pairing to break cyclic inequalities

**Problem**: For $x,y,z>0$, prove $\dfrac{x^2}{y}+\dfrac{y^2}{z}+\dfrac{z^2}{x} \geq x+y+z$.

This inequality has three terms cycling $x\to y\to z\to x$, making it hard to apply AM-GM all at once. Instead, **pair each term with the variable in its denominator** and apply two-variable AM-GM three times.

```latex
\frac{x^2}{y}+y \geq 2\sqrt{\frac{x^2}{y}\cdot y} = 2x, \qquad
\frac{y^2}{z}+z \geq 2y, \qquad
\frac{z^2}{x}+x \geq 2z
```

Adding all three inequalities:

```latex
\left(\frac{x^2}{y}+\frac{y^2}{z}+\frac{z^2}{x}\right) + (x+y+z) \;\geq\; 2(x+y+z)
```

Subtracting $(x+y+z)$ from both sides gives the desired result:

```latex
\frac{x^2}{y}+\frac{y^2}{z}+\frac{z^2}{x} \;\geq\; x+y+z
```

Equality at $x=y=z$. ■

This "pairing" technique is the most powerful standard tool for cyclic inequalities, and shares the same idea as the T-transformation in §12 (Muirhead), which reduces multivariable problems to two-variable problems — **breaking a complex multivariable structure into a sum of two-variable AM-GMs**.

### 10.3 When to move on to other tools

When the two techniques in §10.1–10.2 don't work, the next standard step is to move to the Cauchy-Schwarz inequality (especially Titu's Lemma, see §16 Problem 5) or Muirhead's inequality from §12. A rough rule of thumb: if majorization appears among the exponent vectors of the terms, use Muirhead; if the expression is a sum of fractions, use Cauchy-Schwarz; otherwise, try splitting or pairing first — this order tends to be efficient in practice.


---
## 11. Advanced: Gauss's arithmetic-geometric mean iteration (AGM) and the computation of π

This is not the AM-GM **inequality** itself but an **iterative algorithm** alternating between computing AM and GM; the fact that AM≥GM is what guarantees the convergence and direction of convergence of this algorithm.

### 11.1 The AGM iteration

Starting from $a_0=a$, $b_0=b$ ($0<b\le a$):

**Unicode**

```text
aₙ₊₁ = (aₙ + bₙ)/2
bₙ₊₁ = √(aₙ bₙ)
```

**LaTeX**

```latex
a_{n+1}=\frac{a_n+b_n}{2}, \qquad b_{n+1}=\sqrt{a_n b_n}
```

**Python**

```python
import math

def agm(a, b, n=10):
    for _ in range(n):
        a, b = (a + b) / 2, math.sqrt(a * b)
    return a, b

print(agm(1, 2, 3))   # (1.4568..., 1.4568...)
```

By AM≥GM, we always have $a_{n+1}\ge b_{n+1}$, and at the same time $b_{n+1}=\sqrt{a_nb_n}\ge b_n$ (GM increases past the smaller value) and $a_{n+1}\le a_n$ (AM decreases below the larger value). That is, $a_n$ decreases monotonically and $b_n$ increases monotonically, sandwiching each other and converging to the same limit $\text{agm}(a,b)$. In 1799 Gauss discovered that $\text{agm}(\sqrt2,1)$ connects exactly to the lemniscate constant, which became the starting point of AGM research.

### 11.2 Quadratic convergence: why is it so fast — a direct derivation

Let's derive the key identity first.

```latex
a_{n+1}-b_{n+1} = \frac{a_n+b_n}{2}-\sqrt{a_nb_n}
```

Substituting $\sqrt{a_n}=u$, $\sqrt{b_n}=v$ on the right side:

```latex
\frac{u^2+v^2}{2}-uv = \frac{u^2-2uv+v^2}{2} = \frac{(u-v)^2}{2}
```

That is:

```latex
a_{n+1}-b_{n+1} = \frac{(\sqrt{a_n}-\sqrt{b_n})^2}{2}
```

This is the previously known identity. Now let's check whether the error $\varepsilon_n := a_n-b_n$ actually shrinks **quadratically**. Rationalizing the numerator:

```latex
\sqrt{a_n}-\sqrt{b_n} = \frac{a_n-b_n}{\sqrt{a_n}+\sqrt{b_n}} = \frac{\varepsilon_n}{\sqrt{a_n}+\sqrt{b_n}}
```

Substituting this into the equation above:

```latex
\varepsilon_{n+1} = \frac{\varepsilon_n^{\,2}}{2\left(\sqrt{a_n}+\sqrt{b_n}\right)^2}
```

Since both $a_n$ and $b_n$ converge to the common limit $M=\text{agm}(a,b)$, as $n$ grows the denominator approaches the **positive constant** $2(\sqrt M+\sqrt M)^2 = 8M$. Hence:

```latex
\varepsilon_{n+1} \approx \frac{\varepsilon_n^{\,2}}{8M} \qquad (\text{for large } n)
```

This is the precise meaning of **quadratic convergence**: since the error shrinks by squaring, if the accuracy at one step is $10^{-k}$, the next step gives roughly $10^{-2k}$ — **the number of correct digits roughly doubles with every iteration.** This is fundamentally different from linear convergence (where the error shrinks by only a fixed ratio each time, so digits increase by a fixed amount each step); thanks to this, AGM can reach millions of digits of precision with only 20–30 iterations.

### 11.3 The Gauss-Legendre (Brent-Salamin) algorithm: applying AGM directly to compute π

Using the complete elliptic integral

```latex
I(a,b)=\int_0^\infty \frac{dx}{\sqrt{(x^2+a^2)(x^2+b^2)}} = \frac{\pi}{2\,\text{agm}(a,b)}
```

we can compute π using AGM. Brent and Salamin independently formulated a practical algorithm in 1976, as follows.

**Initial values**: $a_0=1$, $b_0=\dfrac{1}{\sqrt2}$, $t_0=\dfrac14$, $p_0=1$

**Iteration ($n=0,1,2,\ldots$)**:

```latex
a_{n+1}=\frac{a_n+b_n}{2}, \qquad
b_{n+1}=\sqrt{a_nb_n}, \qquad
t_{n+1}=t_n-p_n(a_n-a_{n+1})^2, \qquad
p_{n+1}=2p_n
```

**Approximation**:

```latex
\pi \approx \frac{(a_{n+1}+b_{n+1})^2}{4\,t_{n+1}}
```

```python
import math

def pi_brent_salamin(iterations=4):
    a, b, t, p = 1.0, 1/math.sqrt(2), 0.25, 1.0
    for _ in range(iterations):
        a_next = (a + b) / 2
        b_next = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        p *= 2
        a, b = a_next, b_next
    return (a + b) ** 2 / (4 * t)

print(pi_brent_salamin(4))   # 3.14159265358979... (accurate to dozens of decimal places after only 4 iterations)
```

Thanks to the quadratic convergence result from §11.2, this algorithm achieves an accuracy of more than 20-30 decimal places with just 4-5 iterations. Combined with fast (FFT-based) multiplication algorithms, the resulting **Gauss-Legendre algorithm** is the foundation of the algorithm family actually used in record-setting computations of π to tens of millions of digits and beyond.

### 11.4 Performance optimization of the AGM iteration (Ooura, 1998)

Each step of the Brent-Salamin algorithm requires, in addition to addition and division, a **square root computation** (which internally needs several multiplications when done via Newton's iteration). T. Ooura presented a modified version that reduces the cost of this square-root computation. The key idea is as follows.

To compute $\sqrt{x}$, one typically first computes $1/\sqrt{x}$ via Newton's iteration and then multiplies by $x$:

```latex
y_{k+1} = y_k\cdot\frac{3-x\,y_k^2}{2} \qquad (\text{converges to } 1/\sqrt{x} \text{ without division})
```

In the AGM iteration, $b_{n+1}=\sqrt{a_nb_n}$ must be computed at every step, so a naive implementation must run an independent Newton iteration (and its internal multiplications) fresh at every step. Ooura's improvement rearranges the Newton iteration needed for this square-root computation so that it proceeds **simultaneously** with the AGM's mean computation, reusing intermediate multiplication results shared by the two computations. This reduces the total number of multiplications needed per iteration to roughly half of the original. The published modified version takes the following form (after initialization, iterate):

```text
c = √0.125;  a = 1 + 3c;  b = √a;  e = b - 0.625
b = 2b;  c = e - c;  a = a + e;  npow = 4

Iterate:
    npow = 2·npow
    e = (a + b)/2
    b = √(ab)
    e = e - b
    b = 2b
    c = c - e
    a = e + b
(until e falls below the target precision)

e = e²/4
a = a + b
π ≈ (a² - e - e/2) / (a·c - e) / npow
```

An extension of the same principle (relocating the cost of the square-root computation) has also produced a **quartically convergent algorithm**, leading to real speedups in large-scale π computations.

### 11.5 Numeric example: tracking the convergence rate directly

Starting from $a_0=1$, $b_0=2$, let's track whether the error $\varepsilon_n=a_n-b_n$ actually shrinks quadratically.

| $n$ | $a_n$ | $b_n$ | $\varepsilon_n = a_n-b_n$ |
|---|---|---|---|
| 0 | 1 | 2 | $1$ |
| 1 | $1.5$ | $\sqrt2\approx1.41421$ | $\approx0.08579$ |
| 2 | $\approx1.45711$ | $\approx1.45648$ | $\approx0.00062$ |
| 3 | $\approx1.456792$ | $\approx1.456792$ | $\approx3.3\times10^{-8}$ |

$\varepsilon_1\approx0.086 \to \varepsilon_2\approx6.2\times10^{-4}$: this is approximately $(0.086)^2/(8\times1.46)\approx6.3\times10^{-4}$, matching the approximation from §11.2 exactly. In the step $\varepsilon_2\to\varepsilon_3$, the error drops from $6.2\times10^{-4}$ to $3.3\times10^{-8}$ — you can see the number of correct digits nearly double.

---

## 12. Advanced: generalization to Muirhead's inequality

### 12.1 Definition of majorization

Let sequences $a=(a_1,\ldots,a_n)$ and $b=(b_1,\ldots,b_n)$ be sorted in decreasing order ($a_1\geq\cdots\geq a_n$, $b_1\geq\cdots\geq b_n$). We say $a$ **majorizes** $b$ ($a \succ b$) if:

```latex
\sum_{i=1}^k a_i \geq \sum_{i=1}^k b_i \quad (k=1,\ldots,n-1), \qquad \sum_{i=1}^n a_i = \sum_{i=1}^n b_i
```

That is, "the partial sums of $a$ are always at least those of $b$, but the total sums are equal." Intuitively, $a$ is **less evenly distributed** than $b$.

**Example**: $(3,0,0) \succ (2,1,0) \succ (1,1,1)$. All have total sum 3, but the further left, the more skewed toward one side.

### 12.2 Statement of Muirhead's inequality

If $x_1,\ldots,x_n \geq 0$ and $a \succ b$, then for the symmetric sums (sums over all permutations):

```latex
\sum_{\sigma\in S_n} x_{\sigma(1)}^{a_1}\cdots x_{\sigma(n)}^{a_n} \;\geq\; \sum_{\sigma\in S_n} x_{\sigma(1)}^{b_1}\cdots x_{\sigma(n)}^{b_n}
```

### 12.3 Verifying directly that AM-GM is a special case of Muirhead

Let's rewrite AM-GM ($\frac{x_1+\cdots+x_n}{n}\geq \sqrt[n]{x_1\cdots x_n}$) in Muirhead form.

- $a = (1,0,\ldots,0)$, $b = (\tfrac1n,\ldots,\tfrac1n)$

**Checking $a \succ b$**: the partial-sum condition is $\sum_{i=1}^k a_i = 1$ (for every $k\geq1$), $\sum_{i=1}^k b_i = k/n$. If $k<n$ then $1 \geq k/n$ always holds. The total sums are both 1. Hence $a \succ b$.

**Computing both symmetric sums**:

- $a$ side: $\sum_\sigma x_{\sigma(1)}^1x_{\sigma(2)}^0\cdots x_{\sigma(n)}^0$. Only which variable receives exponent 1 affects the result ($n$ choices), and the remaining $(n-1)!$ permutations give identical values, so the sum is $(n-1)!\sum_i x_i$.
- $b$ side: all exponents equal $1/n$, so any permutation gives the same value $(x_1\cdots x_n)^{1/n}$. With $n!$ permutations, the sum is $n!\,(x_1\cdots x_n)^{1/n}$.

Substituting into Muirhead's inequality:

```latex
(n-1)!\sum_i x_i \;\geq\; n!\,(x_1\cdots x_n)^{1/n}
```

Dividing both sides by $(n-1)!\cdot n$:

```latex
\frac{1}{n}\sum_i x_i \;\geq\; (x_1\cdots x_n)^{1/n}
```

This is exactly AM-GM. In other words, Muirhead is not just a "verbal generalization" — the entire AM-GM inequality can be re-derived from the single fact that the exponent vector $(1,0,\ldots,0)$ majorizes $(\tfrac1n,\ldots,\tfrac1n)$.

### 12.4 Sketch of Muirhead's proof: reduction to adjacent transpositions and two-variable AM-GM

Muirhead's inequality is proved via the following lemma.

**Lemma (reduction via adjacent transpositions, the T-transformation)**: If $a \succ b$ and $a\neq b$, then starting from $a$ we can reach $b$ through a finite sequence of operations that each **change only two components**. Each operation (a T-transformation) replaces two components with $a_i > a_j$ by $a_i' = a_i-t$, $a_j'=a_j+t$ ($t>0$, $a_i'\geq a_j'$).

**Key inequality**: how the symmetric sum changes before and after a single T-transformation reduces to a single inequality in two variables $x,y$.

```latex
x^{a_i}y^{a_j} + x^{a_j}y^{a_i} \;\geq\; x^{a_i'}y^{a_j'} + x^{a_j'}y^{a_i'}
```

Subtracting the right side from the left:

```latex
x^{a_i}y^{a_j}+x^{a_j}y^{a_i}-x^{a_i'}y^{a_j'}-x^{a_j'}y^{a_i'} = \left(x^{a_i'}-x^{a_j'}\right)\left(y^{a_j'}-y^{a_i'}\right)
```

Since $a_i'\ge a_j'$, for $x>0$, the sign of $x^{a_i'}-x^{a_j'}$ always matches the sign of the corresponding factor in $y$ (both depend consistently on whether $x\gtrless y$), so the product is always non-negative. That is, **Muirhead's inequality as a whole decomposes into a chain of two-variable inequalities** — exactly the same structure as Cauchy's forward-backward induction reducing AM-GM to the two-variable case.

### 12.5 Example: a complete solution applying Muirhead

**Problem**: For $x,y>0$, prove $x^2y^3 + x^3y^2 \leq xy^4 + x^4y$.

**Solution**: Sorting the exponent vectors in decreasing order, the left side gives $(3,2)$ and the right side gives $(4,1)$. Check $(4,1) \succ (3,2)$: partial sum $4 \geq 3$ ✓, total sum $5=5$ ✓. So by Muirhead's inequality, immediately

```latex
\sum_\sigma x^{4}y^{1} \;\geq\; \sum_\sigma x^{3}y^{2} \quad\Longleftrightarrow\quad x^4y+xy^4 \;\geq\; x^3y^2+x^2y^3
```

holds. (With two variables, the symmetric sums have only two terms each, so checking the majorization relation alone completes the proof immediately.) Equality at $x=y$. ■

### 12.6 Limitations of Muirhead's inequality

Muirhead is **powerful, but only applies when a majorization relation exists**. If the exponent vectors are not comparable under majorization, Muirhead says nothing. With three or more variables, exponent pairs with no majorization relation are common, requiring other tools such as Schur-convex functions or sum-of-squares (SOS) decompositions.

### 12.7 Connection to SAGE and SONC

Research by Moustrou, Riener, Theobald, and Verdure (arXiv:2312.10500, published in the *Journal of Symbolic Computation*) showed that when SAGE/SONC certificates (§8.1 — also derived directly from weighted AM-GM as a nonnegativity-proving tool) are combined with symmetry, the SAGE or SONC property coincides with nonnegativity in several symmetric cases. SAGE from §8.1 and Muirhead from this section are naturally connected, in that both are tools derived from the same root: "applying weighted AM-GM (≡ a special case of majorization) term by term to prove nonnegativity."

---

## 13. Advanced: comparison with the method of Lagrange multipliers

### 13.1 Solving the §5.2 problem with Lagrange multipliers

Solving §5.2's box-volume problem (fixed surface area $S=2(ab+bc+ca)$, maximize volume $V=abc$) via Lagrange multipliers gives:

```latex
\nabla V = \lambda \nabla g \implies (bc,\,ac,\,ab) = \lambda(2b+2c,\,2a+2c,\,2a+2b)
```

Solving this system of equations to derive $a=b=c$ requires calculus and equation-solving. Dividing the first two equations:

```latex
\frac{bc}{ac} = \frac{2b+2c}{2a+2c} \implies \frac{b}{a} = \frac{b+c}{a+c} \implies b(a+c) = a(b+c) \implies bc = ac \implies a = b
```

Similarly one obtains $b=c$, reaching $a=b=c$.

By contrast, the AM-GM solution in §5.2 obtains the maximum value and the equality condition (the optimal point) simultaneously from **a single algebraic inequality** — a representative case of "derivative-free optimization."

### 13.2 Scaling with the number of variables: comparing the two methods' scalability

The practical difference between the two methods becomes clear **as the number of variables grows**. Consider the following problem.

**Problem**: For $x_1,\ldots,x_n>0$ with $x_1x_2\cdots x_n=1$, find the minimum of $x_1+x_2+\cdots+x_n$.

**With AM-GM (one line, regardless of the number of variables)**:

```latex
\frac{x_1+\cdots+x_n}{n}\geq\sqrt[n]{x_1\cdots x_n}=\sqrt[n]{1}=1 \implies x_1+\cdots+x_n\geq n
```

Equality at $x_1=\cdots=x_n=1$. The solution process is **completely identical** whether $n$ is 2 or 100.

**With Lagrange multipliers (the number of equations grows with the number of variables)**:

```latex
L = \sum_i x_i + \lambda\left(\prod_i x_i - 1\right), \qquad \frac{\partial L}{\partial x_i} = 1+\lambda\prod_{j\neq i}x_j=0 \quad (i=1,\ldots,n)
```

This produces $n$ equations, requiring $\prod_{j\neq i}x_j = -1/\lambda$ to hold as **the same value for every $i$**. To show that $\prod_{j\neq i}x_j$ is independent of $i$, one needs a symmetry argument: for arbitrary indices $i,k$, rearranging $\prod_{j\neq i}x_j=\prod_{j\neq k}x_j$ derives $x_k=x_i$. Substituting $x_i=c$ (a constant) into the constraint then gives $c^n=1\Rightarrow c=1$, reaching the minimum value $n$.

That is, as $n$ grows, the Lagrange method's **number of simultaneous equations and the complexity of the symmetry argument both grow**, whereas AM-GM finishes with a single-line inequality regardless of the number of variables. This is the practical meaning of the statement that "AM-GM is a representative case of derivative-free optimization" — not merely that no derivatives are used, but the scalability advantage that **the length of the proof does not grow even as the dimension grows**.

### 13.3 When Lagrange is preferable

Conversely, when the objective function or constraints don't reduce cleanly to AM-GM form (e.g., quadratic forms, non-polynomial functions, or cases with many inequality constraints requiring the full KKT conditions), the Lagrange (or KKT) method is the only option. AM-GM is a tool specialized for problems with the structure "maximize a product given a fixed sum" (or its reverse: "minimize a sum given a fixed product"), and it cannot be applied outside that structure.

---

## 14. Advanced: structural connection to information theory

### 14.1 Why AM-GM and KL divergence are "the same proof" — a direct correspondence

Let's lay Gibbs' inequality (nonnegativity of entropy, $D_{KL}(p\|q)\geq 0$) and AM-GM's Jensen proof (§2.3) side by side and match them step by step.

| Step | AM-GM (§2.3) | KL divergence |
|---|---|---|
| Choice of concave function | $f(x) = \ln x$ | $f(x) = \ln x$ (same) |
| Object of Jensen's inequality | $n$ equally weighted values $x_1,\ldots,x_n$ | Values $q_i/p_i$ weighted by probabilities $p_i$ |
| Jensen's inequality | $\dfrac1n\sum \ln x_i \leq \ln\!\Big(\dfrac1n\sum x_i\Big)$ | $\displaystyle\sum_i p_i \ln\frac{q_i}{p_i} \leq \ln\!\Big(\sum_i p_i\frac{q_i}{p_i}\Big)$ |
| Simplifying the right side | $\ln\big(\tfrac1n\sum x_i\big) = \ln A$ | $\ln\big(\sum_i q_i\big) = \ln 1 = 0$ |
| Conclusion | $\ln G \leq \ln A \Rightarrow G\leq A$ | $\sum p_i\ln\frac{q_i}{p_i}\leq0 \Rightarrow D_{KL}(p\|q)\geq0$ |

**Direct derivation**: applying Jensen's inequality (concave function $\ln$, weights $p_i$) to $y_i = q_i/p_i$:

```latex
\sum_i p_i \ln\frac{q_i}{p_i} \;\leq\; \ln\!\left(\sum_i p_i\cdot\frac{q_i}{p_i}\right) = \ln\!\left(\sum_i q_i\right) = \ln 1 = 0
```

Multiplying both sides by $-1$ immediately gives $D_{KL}(p\|q) = \sum_i p_i\ln\dfrac{p_i}{q_i} \geq 0$. The equality conditions also correspond exactly: just as AM-GM's equality holds "when all $x_i$ are equal," KL divergence's equality holds "when $q_i/p_i$ is the same for every $i$" — i.e., $q_i=p_i$ (when the two probability distributions are identical).

**One step further — confirming this is exactly weighted AM-GM**: this argument is in fact weighted AM-GM itself. In weighted AM-GM $\sum \lambda_i x_i \geq \prod x_i^{\lambda_i}$, setting $\lambda_i = p_i$, $x_i = q_i/p_i$:

```latex
\sum_i p_i \cdot \frac{q_i}{p_i} \;\geq\; \prod_i \left(\frac{q_i}{p_i}\right)^{p_i} \;\;\Longrightarrow\;\; 1 \;\geq\; \prod_i \left(\frac{q_i}{p_i}\right)^{p_i}
```

Taking logarithms of both sides gives $0 \geq \sum_i p_i \ln(q_i/p_i)$ — exactly the same conclusion as above. **Weighted AM-GM ⟺ Jensen (log) ⟺ Gibbs' inequality**: these three are, literally, the same single-line inequality expressed in three different languages.

### 14.2 A numeric check

For $p=(0.5,0.5)$, $q=(0.9,0.1)$:

```latex
D_{KL}(p\|q) = 0.5\ln\frac{0.5}{0.9} + 0.5\ln\frac{0.5}{0.1} = 0.5\ln(0.5556) + 0.5\ln(5) \approx 0.5(-0.5878)+0.5(1.6094) \approx 0.5108
```

We can directly confirm it is positive. On the other hand, if $q=p=(0.5,0.5)$ then $D_{KL}=0$ — exactly matching AM-GM's equality condition ($x_i$ all equal, here $q_i/p_i$ all equal to 1).

### 14.3 Why this correspondence is useful

This correspondence is not a mere coincidence — it shows that the single template of "concave function + Jensen's inequality" operates identically across two seemingly unrelated fields (algebraic inequalities and information theory). Plugging a different concave function into the same template in place of $f(x)=\ln x$ derives other information inequalities in the same way, such as Rényi entropy and $f$-divergences — meaning AM-GM can be viewed as the simplest case of this template (the case of a uniform distribution, $p_i \equiv 1/n$).

### 14.4 Connection to recent research

Yeung's research ("Inequalities Revisited," arXiv:2503.03766) showed that the formal methodology developed for dealing with Shannon entropy inequalities — the geometric framework used to discover non-Shannon-type inequalities — can also be applied to classical inequalities outside information theory, such as AM-GM, the Markov inequality, and the Cauchy-Schwarz inequality. The fact directly confirmed in §14.1–14.3 — that "AM-GM and KL divergence share the same proof skeleton" — is a concrete example of why this kind of formal methodology can cross between fields.

---

## 15. Counterexamples, misconceptions, and failure cases

Let's go over the traps people commonly fall into when using AM-GM.

### 15.1 It doesn't hold with negative numbers

$a=-1, b=-4$: $A=-2.5$, $G=\sqrt{(-1)(-4)}=2$. $A<G$. AM-GM holds only for non-negative reals.

### 15.2 Ignoring the equality condition

$a=1, b=4$: $A=2.5$, $G=2$. $A>G$. Not equality. Failing to check the equality condition in optimization means missing the optimal point.

### 15.3 The misconception that "the arithmetic mean is always larger"

When the geometric mean is undefined (e.g. with negative numbers), no comparison is possible. Also, when $n=1$, they are trivially equal.

### 15.4 The misconception that "AM-GM gives every inequality"

AM-GM is powerful but has its limits. For example, an inequality like $\sum x_i^2 \geq \sum x_i x_{i+1}$ cannot be obtained directly from AM-GM; other tools such as Cauchy-Schwarz, Jensen, or Muirhead are needed.

### 15.5 The misconception that "the weights don't need to sum to 1"

In weighted AM-GM, $\sum \lambda_i = 1$ is mandatory. Without it, the inequality does not hold.

### 15.6 Lessons from failed approaches

- **Applying substitution without care**: $x^2+y^2 \geq 2xy$ is AM-GM. But a variant like $x^3+y^3 \geq 2xy\sqrt{xy}$ requires a separate derivation.
- **Skipping the equality-condition check**: in an optimization problem you might compute a "maximum," but if the equality condition falls outside the domain, it isn't actually the maximum.
- **Missing weight normalization**: in weighted AM-GM, failing to check $\sum \lambda_i = 1$ leads to incorrect conclusions.

---

## 16. Self-check problems

### Problem 1 (basic)

For $a,b>0$, prove $\dfrac{a}{b}+\dfrac{b}{a}\geq 2$.

**Answer**: Let $x=a/b$. Then $x+1/x \geq 2\sqrt{x \cdot 1/x} = 2$. Equality at $a=b$.

### Problem 2 (intermediate)

For $x,y,z>0$ with $x+y+z=6$, find the maximum of $xyz$.

**Answer**: AM-GM: $\dfrac{x+y+z}{3} \geq \sqrt[3]{xyz}$ → $2 \geq \sqrt[3]{xyz}$ → $xyz \leq 8$. Equality at $x=y=z=2$. Maximum value 8.

### Problem 3 (intermediate)

For $x>0$, find the minimum of $x + \dfrac{2}{x}$.

**Answer**: $x + \dfrac{2}{x} \geq 2\sqrt{2}$. Equality at $x=\sqrt{2}$. Minimum value $2\sqrt{2}$.

### Problem 4 (advanced)

For $a,b,c>0$ with $abc=1$, prove $a+b+c \geq 3$.

**Answer**: AM-GM: $\dfrac{a+b+c}{3} \geq \sqrt[3]{abc} = 1$ → $a+b+c \geq 3$. Equality at $a=b=c=1$.

### Problem 5 (advanced) — full solution of Nesbitt's inequality

Prove $\dfrac{a}{b+c}+\dfrac{b}{c+a}+\dfrac{c}{a+b}\geq \dfrac{3}{2}$ $(a,b,c>0)$.

**Solution (Titu's Lemma):**

```latex
\sum \frac{a}{b+c} = \sum \frac{a^2}{a(b+c)} \geq \frac{(a+b+c)^2}{2(ab+bc+ca)}
```

$\dfrac{(a+b+c)^2}{2(ab+bc+ca)} \geq \dfrac{3}{2}$ is equivalent to

```latex
(a+b+c)^2 \geq 3(ab+bc+ca) \iff a^2+b^2+c^2 \geq ab+bc+ca
```

which holds because $(a-b)^2+(b-c)^2+(c-a)^2 \geq 0$. Equality at $a=b=c$. ■

### Problem 6 (advanced)

Starting an AGM iteration with $a_0=1$, $b_0=2$, find $a_1,b_1,a_2,b_2$.

**Answer**: $a_1=1.5$, $b_1=\sqrt{2}\approx 1.4142$. $a_2=(1.5+1.4142)/2\approx 1.4571$, $b_2=\sqrt{1.5 \times 1.4142}\approx 1.4565$.

---

### 17. Summary — applications by field

**1. Geometry / optimization**
- Key use: maximum area/volume for fixed perimeter/surface area (squares, cubes)
- Meaning of the equality condition: the "most balanced" shape

**2. Finance / investment**
- Key use: arithmetic vs. geometric mean returns, volatility drag
- Meaning of the equality condition: volatility = 0 (same return every year)

**3. Engineering / physics**
- Key use: upper bounds on energy conversion efficiency, resource-allocation optimization
- Meaning of the equality condition: balanced allocation among components

**4. Computer science**
- Key use: SAGE certificates, noncommutative AM-GM (SGD theory)
- Meaning of the equality condition: term-level balance point / advantage of without-replacement sampling

**5. Economics**
- Key use: production-function optimization, resource allocation
- Meaning of the equality condition: efficient allocation of input factors

**6. Competitions / pure mathematics**
- Key use: a fundamental tool for proving inequalities
- Meaning of the equality condition: variables are identical

**7. Numerical analysis (advanced)**
- Key use: computing π via the Gauss AGM iteration
- Meaning of the equality condition: the two sequences converge to the same value

**8. Theory of symmetric functions (advanced)**
- Key use: Muirhead's inequality, connection to SAGE
- Meaning of the equality condition: a special point in the majorization chain

### 17.1 Core summary

- **Inequality**: $A \geq G$ (for non-negative reals)
- **Equality condition**: all variables equal
- **n=2 form**: $(a+b)/2 \geq \sqrt{ab}$
- **Weighted form**: $\sum \lambda_i x_i \geq \prod x_i^{\lambda_i}$, $\sum \lambda_i = 1$
- **Mean chain**: $H \leq G \leq A \leq Q$
- **Optimization principle**: fixed sum → maximum product (when all are equal)
- **Financial application**: $\bar r_A \geq \bar r_G$, drag $\approx \sigma^2/2$
- **Information theory**: the Jensen proof is isomorphic to KL divergence
- **Muirhead**: AM-GM is a special case of majorization
- **SAGE (recent)**: AM/GM certificates, relative entropy programming, symmetry reduction
- **Noncommutative AM-GM**: connection to SGD theory, counterexample at m=n=5 (Lai & Lim, 2020)
- **AGM iteration**: quadratic convergence, computing π, performance optimization
- **Counterexample**: does not hold with negative numbers
- **Number of proofs**: 8 (perfect square, Cauchy induction, Jensen, Pólya, smoothing, Lagrange, Chrystal, Bernoulli)

---

**References**
 
**1. Cauchy, A.-L. (1821).** | [archive.org](https://archive.org/details/coursdanalysedel00cauc)

_Cours d’analyse de l’École royale polytechnique._ The textbook that completed the rigorization of analysis, first defining limits, continuity, convergence, and series tests rigorously. The forward-backward induction in §2.2 — Cauchy’s proof of AM-GM — appears here for the first time. Its structure (”prove for powers of 2, then reduce to arbitrary n”) became a standard tool for inequality proofs thereafter.

---

**2. Gauss, C. F. (1799/1866).** | [Göttingen Digital Library](https://gdz.sub.uni-goettingen.de/id/PPN235993352)

_Werke_, Band III. In his mathematical diary entry of May 30, 1799, Gauss recorded the exact connection between AGM(1, √2) and the lemniscate constant ϖ, verifying it to 11 decimal places and calling it “a completely new field of analysis.” Note the distinction: Gauss’s 1799 **doctoral dissertation** was on the fundamental theorem of algebra; the **AGM discovery came from contemporaneous diary notes**. This entry is the historical starting point for the AGM theory in §11.

---

**3. Hardy, G. H., Littlewood, J. E., & Pólya, G. (1934).** | [Cambridge University Press](https://www.cambridge.org/core/books/inequalities/7B1F1C4E5D9A2B8F)

_Inequalities._ The standard textbook of the field. It systematically organizes the core inequalities of analysis — AM-GM, Hölder, Minkowski, Hardy — and establishes symmetrization and majorization techniques. Both the mean chain in §3 and the Muirhead theory in §12 rest on the framework laid out here.

---

**4. Muirhead, R. F. (1903).** | [Cambridge Core](https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/F222600CC0076146E369EE27C8559F78)

_Some methods applicable to identities and inequalities of symmetric algebraic functions of n letters._ The original paper presenting **Muirhead’s inequality**, a criterion for symmetric-sum inequalities. It proves that a majorization relation between two exponent vectors implies an inequality between the corresponding symmetric sums, becoming a fundamental tool for proving symmetric inequalities. The entirety of §12 is an exposition of this paper.

---

**5. Pólya, G., & Szegő, G. (1925).** | [Springer](https://link.springer.com/book/10.1007/978-3-642-61905-2)

_Aufgaben und Lehrsätze aus der Analysis._ A classic of analysis education through problem-solving. A source of advanced problems on inequalities, the distribution of zeros of polynomials, determinants, and other topics, used to train inequality-proving techniques. The Pólya exponential method in §2.4 connects to the approach in this book.

---

**6. Alzer, H. (1999).** | [Cambridge Core](https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/A08079A284DB1A10ABE840010A640887)

_Some inequalities for arithmetic and geometric means._ Provides precise upper and lower bounds on the ratio between the weighted arithmetic mean and the geometric mean. Offers sharpened forms that improve upon the classical AM-GM inequality and the Ky Fan inequality, and connects directly to the “recent research on the mean chain” mentioned in §3.4.

---

**7. Moustrou, P., Riener, C., Theobald, T., & Verdure, H. (2025).** | [arXiv:2312.10500](https://arxiv.org/abs/2312.10500)

_Symmetric SAGE and SONC forms, exactness and quantitative gaps._ _Journal of Symbolic Computation_, 127, 102374. Analyzes the relationship between symmetric SAGE/SONC forms and nonnegativity, showing that in several symmetric cases the SAGE or SONC property coincides with nonnegativity. It also shows that SONC certificates **generalize Muirhead’s inequality**. Directly corresponds to §8.1 (SAGE) and §12.7 (the SAGE–Muirhead connection).

---

**8. Ooura, T. (1998).** | [Ooura’s page](https://www.kurims.kyoto-u.ac.jp/~ooura/pi_fft.html)

_Improvement of the π calculation algorithm and implementation of fast multiple-precision computation._ IPSJ SIG Notes, 98-HPC-74. Rearranges the square-root computation required at each step of the Brent–Salamin algorithm, reducing the number of multiplications per AGM iteration to roughly half of the original. The original source for the performance optimization discussed in §11.4.

---

**9. Recht, B., & Ré, C. (2012).** | [arXiv:1202.4184](https://arxiv.org/abs/1202.4184)

_Toward a noncommutative arithmetic-geometric mean inequality: conjectures, case-studies, and consequences._ COLT 2012, PMLR 23, 11.1–11.24. Conjectures an AM-GM inequality in the noncommutative setting of matrices. Starting from the observation that without-replacement sampling is more stable than with-replacement sampling in SGD, it proposes an inequality-form conjecture about the expected value of matrix products. The starting point for §8.2.

---

**10. Zhang, T. (2014).** | [arXiv:1411.5058](https://arxiv.org/abs/1411.5058)

_A note on the non-commutative arithmetic-geometric mean inequality._ A follow-up analysis of the Recht–Ré conjecture, extending it to the case m=3_m_=3 with arbitrary n_n_. Shows the conjecture holds for small m_m_, and became the stepping stone for later disproof work.

---

**11. Lai, Z., & Lim, L.-H. (2020).** | [arXiv:2006.01510](https://arxiv.org/abs/2006.01510)

_Recht-Ré noncommutative arithmetic-geometric mean conjecture is false._ ICML 2020, PMLR 119, 5608–5617. Using a noncommutative Positivstellensatz to convert the conjecture into a semidefinite programming (SDP) problem, it numerically confirms **a concrete counterexample at** **m=n=5_m_=_n_=5**. The conjecture is thus false in general, concluding the narrative of §8.2.

---

**12. Yeung, R. (2025).** | [arXiv:2503.03766](https://arxiv.org/abs/2503.03766)

_Inequalities revisited._ Shows that the formal methodology developed for Shannon entropy inequalities — the geometric framework used to discover non-Shannon-type inequalities — can also be applied to classical inequalities outside information theory, such as AM-GM, the Markov inequality, and the Cauchy–Schwarz inequality. The formal background for the fact discussed in §14.4, that “AM-GM and KL divergence share the same proof skeleton.”

---

**13. Chen, H., Khare, A., & Sahi, S. (2025).** | [arXiv:2509.19649](https://arxiv.org/abs/2509.19649)

_Majorization via positivity of Jack and Macdonald polynomial differences._ Characterizes the majorization relation via the positivity of differences of Jack and Macdonald polynomials. Shows that majorization holds when the coefficients of symmetric polynomials are positive, generalizing Muirhead’s inequality — an extension tool for the cases discussed in §12.6 where no majorization relation exists.