# Formulas for Calculating π and an Interactive Page

There are many, many ways to calculate the value of π, and new methods are still being proposed even today. A detailed follow-up post explaining the meaning and derivation of each formula — what each one is really saying — will come soon.

This post isn't about *why* these formulas equal π or what they mean mathematically. Instead, think of it as a small experience: a survey of the different methods for computing π, paired with an interactive page where you can watch the computation happen in real time and compare which approach is more efficient.

---

## 1. Infinite Series

### 1-1. Gregory–Leibniz Series (c. 1674)

**Core idea**: Obtained by substituting x = 1 into the Taylor series for arctan(x). It follows from the fact that arctan(1) = π/4, but since the terms shrink only as 1/n, convergence is very slow.

**a) Unicode**
```
π/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − ⋯
```

**b) LaTeX**
```latex
\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}
```

**c) Mathematica**
```mathematica
Pi/4 == Sum[(-1)^n/(2 n + 1), {n, 0, Infinity}]
(* Numerical approximation *)
N[4*Sum[(-1)^n/(2 n + 1), {n, 0, 100000}], 10]
```

**d) Python**
```python
def leibniz_pi(terms=1_000_000):
    total = 0.0
    for n in range(terms):
        total += (-1) ** n / (2 * n + 1)
    return 4 * total

print(leibniz_pi())
```

---

### 1-2. Nilakantha Series (15th century)

**Core idea**: A rearrangement of the Leibniz series that accelerates convergence. The terms shrink as 1/n³, so it approaches π far faster than the original.

**a) Unicode**
```
π = 3 + 4/(2·3·4) − 4/(4·5·6) + 4/(6·7·8) − ⋯
```

**b) LaTeX**
```latex
\pi = 3 + \sum_{n=1}^{\infty} \frac{(-1)^{n+1} \cdot 4}{(2n)(2n+1)(2n+2)}
```

**c) Mathematica**
```mathematica
Pi == 3 + Sum[(-1)^(n + 1)*4/((2 n)(2 n + 1)(2 n + 2)), {n, 1, Infinity}]
N[3 + Sum[(-1)^(n + 1)*4/((2 n)(2 n + 1)(2 n + 2)), {n, 1, 10000}], 10]
```

**d) Python**
```python
def nilakantha_pi(terms=100_000):
    total = 3.0
    sign = 1
    for n in range(1, terms + 1):
        total += sign * 4 / ((2*n) * (2*n + 1) * (2*n + 2))
        sign *= -1
    return total

print(nilakantha_pi())
```

---

### 1-3. The Basel Problem (Euler, 1735)

**Core idea**: Euler's theorem that the sum of the reciprocals of the squares of all natural numbers converges to π²/6. It was proved by factoring sin(x)/x into an infinite product, as if it were a polynomial, and comparing coefficients with its Taylor series.

**a) Unicode**
```
1/1² + 1/2² + 1/3² + ⋯ = π²/6
```

**b) LaTeX**
```latex
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
```

**c) Mathematica**
```mathematica
Sum[1/n^2, {n, 1, Infinity}] == Pi^2/6
N[Sqrt[6*Sum[1/n^2, {n, 1, 1000000}]], 10]
```

**d) Python**
```python
import math

def basel_pi(terms=1_000_000):
    total = sum(1 / n**2 for n in range(1, terms + 1))
    return math.sqrt(6 * total)

print(basel_pi())
```

---

### 1-4. Machin's Formula (1706)

**Core idea**: Uses the identity π/4 = 4·arctan(1/5) − arctan(1/239). Since both arctan(1/5) and arctan(1/239) have arguments much smaller than 1, their Taylor series converge quickly.

**a) Unicode**
```
π/4 = 4·arctan(1/5) − arctan(1/239)
```

**b) LaTeX**
```latex
\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}
```

**c) Mathematica**
```mathematica
Pi/4 == 4*ArcTan[1/5] - ArcTan[1/239]
N[4*(4*ArcTan[1/5] - ArcTan[1/239]), 20]
```

**d) Python**
```python
import math

def machin_pi():
    return 4 * (4 * math.atan(1/5) - math.atan(1/239))

print(machin_pi())
```

---

### 1-5. An Accelerated Gregory Series (via the Zeta Function)

**Core idea**: A rearrangement of the Gregory (Leibniz) series using the Euler transform (a Vardi-type transformation). By pulling in the Riemann zeta function ζ(k+1) as a coefficient, the error is accelerated down to roughly (3/4)^k.

**a) Unicode**
```
π = Σ[k=1,∞] (3^k − 1)/4^k · ζ(k+1)
```

**b) LaTeX**
```latex
\pi = \sum_{k=1}^{\infty} \frac{3^k - 1}{4^k}\,\zeta(k+1)
```

**c) Mathematica**
```mathematica
Pi == Sum[((3^k - 1)/4^k)*Zeta[k + 1], {k, 1, Infinity}]
N[Sum[((3^k - 1)/4^k)*Zeta[k + 1], {k, 1, 50}], 15]
```

**d) Python**
```python
from mpmath import mp, zeta, mpf

mp.dps = 30  # decimal places

def zeta_accelerated_pi(terms=100):
    total = mpf(0)
    for k in range(1, terms + 1):
        total += (mpf(3)**k - 1) / mpf(4)**k * zeta(k + 1)
    return total

print(zeta_accelerated_pi())
```

---

### 1-6. Sharp's Series (Abraham Sharp, 1699)

**Core idea**: Obtained by substituting x = 1/√3 into the arctan(x) series, following from arctan(1/√3) = π/6. The terms shrink as 1/3^k, making it much faster than the Leibniz series.

**a) Unicode**
```
π = Σ[k=0,∞] 2·(−1)^k·√3 / (3^k·(2k+1))
```

**b) LaTeX**
```latex
\pi = \sum_{k=0}^{\infty} \frac{2(-1)^k \sqrt{3}}{3^k(2k+1)}
```

**c) Mathematica**
```mathematica
Pi == Sum[(2*(-1)^k*Sqrt[3])/(3^k*(2 k + 1)), {k, 0, Infinity}]
N[Sum[(2*(-1)^k*Sqrt[3])/(3^k*(2 k + 1)), {k, 0, 50}], 15]
```

**d) Python**
```python
import math

def sharp_pi(terms=50):
    total = 0.0
    for k in range(terms):
        total += 2 * (-1)**k * math.sqrt(3) / (3**k * (2*k + 1))
    return total

print(sharp_pi())
```

---

### 1-7. Ramanujan's Series (c. 1910)

**Core idea**: Derived from modular equations of elliptic integrals and hypergeometric series theory. Published without proof, but remarkably powerful — each additional term adds roughly 8 correct digits. How modular equations lead to π will be covered in detail separately.

**a) Unicode**
```
1/π = (2√2/9801) · Σ[k=0,∞] (4k)!·(1103+26390k) / ((k!)⁴·396^(4k))
```

**b) LaTeX**
```latex
\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^{\infty} \frac{(4k)!(1103+26390k)}{(k!)^4 \, 396^{4k}}
```

**c) Mathematica**
```mathematica
1/Pi == (2*Sqrt[2]/9801)*Sum[((4 k)!*(1103 + 26390 k))/((k!)^4*396^(4 k)), {k, 0, Infinity}]
N[1/((2*Sqrt[2]/9801)*Sum[((4 k)!*(1103 + 26390 k))/((k!)^4*396^(4 k)), {k, 0, 5}]), 30]
```

**d) Python**
```python
from mpmath import mp, mpf, sqrt, factorial

mp.dps = 50

def ramanujan_pi(terms=5):
    total = mpf(0)
    for k in range(terms):
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * mpf(396)**(4*k)
        total += num / den
    inv_pi = (2 * sqrt(2) / 9801) * total
    return 1 / inv_pi

print(ramanujan_pi())
```

---

### 1-8. The Chudnovsky Algorithm (1988)

**Core idea**: In the same family as Ramanujan's series, derived from a modular equation related to the Heegner number 640320. Each term adds about 14 correct digits, making it the formula most widely used today for computing π to billions of digits. How modular equations lead to π will be covered in detail separately.

**a) Unicode**
```
1/π = 12·Σ[k=0,∞] (−1)^k·(6k)!·(13591409+545140134k) / ((3k)!·(k!)³·640320^(3k+3/2))
```

**b) LaTeX**
```latex
\frac{1}{\pi} = 12\sum_{k=0}^{\infty} \frac{(-1)^k (6k)!(13591409+545140134k)}{(3k)!(k!)^3 \, 640320^{3k+3/2}}
```

**c) Mathematica**
```mathematica
1/Pi == 12*Sum[((-1)^k*(6 k)!*(13591409 + 545140134 k))/((3 k)!*(k!)^3*640320^(3 k + 3/2)), {k, 0, Infinity}]
N[1/(12*Sum[((-1)^k*(6 k)!*(13591409 + 545140134 k))/((3 k)!*(k!)^3*640320^(3 k + 3/2)), {k, 0, 3}]), 50]
```

**d) Python**
```python
from mpmath import mp, mpf, sqrt, factorial

mp.dps = 60

def chudnovsky_pi(terms=3):
    total = mpf(0)
    for k in range(terms):
        num = (-1)**k * factorial(6*k) * (13591409 + 545140134*k)
        den = factorial(3*k) * factorial(k)**3 * mpf(640320)**(3*k + mpf(3)/2)
        total += num / den
    inv_pi = 12 * total
    return 1 / inv_pi

print(chudnovsky_pi())
```

---

## 2. Infinite Products

### 2-1. Wallis Product (Wallis, 1655)

**Core idea**: Obtained by factoring sin(x) into an infinite product and substituting x = π/2. Since each factor only slowly approaches 1, convergence is relatively slow.

**a) Unicode**
```
π/2 = (2/1)·(2/3)·(4/3)·(4/5)·(6/5)·(6/7)·⋯
```

**b) LaTeX**
```latex
\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2-1}
```

**c) Mathematica**
```mathematica
Pi/2 == Product[(4 n^2)/(4 n^2 - 1), {n, 1, Infinity}]
N[2*Product[(4 n^2)/(4 n^2 - 1), {n, 1, 100000}], 8]
```

**d) Python**
```python
def wallis_pi(terms=1_000_000):
    product = 1.0
    for n in range(1, terms + 1):
        product *= (4 * n**2) / (4 * n**2 - 1)
    return 2 * product

print(wallis_pi())
```

---

### 2-2. Viète's Formula (Viète, 1593)

**Core idea**: Expresses, as an infinite product, the process by which the area of regular polygons inscribed in a circle (4 sides → 8 → 16 → …) approaches the area of the circle, obtained by repeatedly applying the half-angle formula. It is considered the first infinite-product formula ever discovered.

**a) Unicode**
```
2/π = √(1/2) · √(1/2 + 1/2·√(1/2)) · √(1/2 + 1/2·√(1/2 + 1/2·√(1/2))) ⋯
```

**b) LaTeX**
```latex
\frac{2}{\pi} = \sqrt{\frac{1}{2}} \cdot \sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}} \cdot \sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}} \cdots
```

**c) Mathematica**
```mathematica
(* Approximate by iteratively generating terms *)
nTerms = 15;
a = Sqrt[2]/2;
product = a;
Do[
  a = Sqrt[(1 + a)/2];
  product *= a;
  , {nTerms}];
N[2/product, 10]
```

**d) Python**
```python
import math

def viete_pi(terms=30):
    a = math.sqrt(2) / 2
    product = a
    for _ in range(terms):
        a = math.sqrt((1 + a) / 2)
        product *= a
    return 2 / product

print(viete_pi())
```

---

## 3. Continued Fractions

### 3-1. Brouncker's Continued Fraction (Brouncker, 1655)

**Core idea**: A rewriting of the Wallis product in continued-fraction form. Euler later proved, using a general method, that the two expressions actually converge to the same value.

**a) Unicode**
```
4/π = 1 + 1²/(2 + 3²/(2 + 5²/(2 + 7²/(2 + ⋯))))
```

**b) LaTeX**
```latex
\frac{4}{\pi} = 1 + \cfrac{1^2}{2+\cfrac{3^2}{2+\cfrac{5^2}{2+\cfrac{7^2}{2+\cdots}}}}
```

**c) Mathematica**
```mathematica
(* Evaluate the continued fraction from bottom to top *)
depth = 200;
cf = 0;
Do[
  cf = (2 n - 1)^2/(2 + cf);
  , {n, depth, 1, -1}];
N[4/(1 + cf), 10]
```

**d) Python**
```python
def brouncker_pi(depth=1000):
    cf = 0.0
    for n in range(depth, 0, -1):
        cf = (2*n - 1)**2 / (2 + cf)
    return 4 / (1 + cf)

print(brouncker_pi())
```

---

## 4. Geometric Methods (Classical)

### 4-1. Archimedes' Polygon Method (c. 250 BC)

**Core idea**: Squeezes the circumference (π) from above and below using the perimeters of regular polygons inscribed in and circumscribed about a circle. Each time the number of sides is doubled (applying the half-angle formula), the error shrinks by roughly a factor of four.

**a) Unicode**
```
2^k·n·sin(π/(2^k·n)) < π < 2^k·n·tan(π/(2^k·n))
```

**b) LaTeX**
```latex
2^k \cdot n \sin\!\left(\frac{\pi}{2^k n}\right) \;<\; \pi \;<\; 2^k \cdot n \tan\!\left(\frac{\pi}{2^k n}\right)
```

**c) Mathematica**
```mathematica
(* Starting from a regular hexagon (n=6), double the sides k times to approximate *)
archimedesBounds[k_, n_ : 6] := Module[{lower, upper},
  lower = N[2^k*n*Sin[Pi/(2^k*n)], 10];
  upper = N[2^k*n*Tan[Pi/(2^k*n)], 10];
  {lower, upper}
]
archimedesBounds[10]
```

**d) Python**
```python
import math

def archimedes_bounds(k, n=6):
    lower = 2**k * n * math.sin(math.pi / (2**k * n))
    upper = 2**k * n * math.tan(math.pi / (2**k * n))
    return lower, upper

print(archimedes_bounds(10))
```

---

## 5. Probabilistic Methods

### 5-1. The Monte Carlo Method

**Core idea**: For a square with side length 2 and an inscribed circle of radius 1, the ratio of the circle's area to the square's area is π/4. By scattering random points inside the square and counting the fraction that land inside the circle, this area ratio can be estimated statistically.

**a) Unicode**
```
π ≈ 4 · (number of points landing inside the circle within the square) / (total number of points)
```

**b) LaTeX**
```latex
\pi \approx 4 \cdot \frac{\text{number of points landing inside the circle within the square}}{\text{total number of points}}
```

**c) Mathematica**
```mathematica
SeedRandom[1];
n = 1000000;
pts = RandomReal[{-1, 1}, {n, 2}];
inside = Count[pts, {x_, y_} /; x^2 + y^2 <= 1];
N[4*inside/n, 6]
```

**d) Python**
```python
import random

def monte_carlo_pi(n=1_000_000):
    inside = 0
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n

print(monte_carlo_pi())
```

---

### 5-2. Buffon's Needle Problem (1777)

**Core idea**: If a needle is dropped at random onto a surface ruled with equally spaced parallel lines, the probability it crosses a line is, by geometry, 2l/(πt) (l: needle length, t: line spacing). By estimating this probability experimentally and inverting the formula, π can be approximated.

**a) Unicode**
```
π ≈ (2·l·n) / (t·h)
(l: needle length, t: spacing between parallel lines, n: number of drops, h: number of drops that crossed a line)
```

**b) LaTeX**
```latex
\pi \approx \frac{2 \cdot l \cdot n}{t \cdot h}
```

**c) Mathematica**
```mathematica
SeedRandom[1];
needleLength = 1; lineGap = 2; nDrops = 1000000;
hits = 0;
Do[
  center = RandomReal[{0, lineGap/2}];
  angle = RandomReal[{0, Pi/2}];
  If[center <= (needleLength/2)*Sin[angle], hits++];
  , {nDrops}];
N[(2*needleLength*nDrops)/(lineGap*hits), 6]
```

**d) Python**
```python
import random, math

def buffon_pi(needle_length=1.0, line_gap=2.0, drops=1_000_000):
    hits = 0
    for _ in range(drops):
        center = random.uniform(0, line_gap / 2)
        angle = random.uniform(0, math.pi / 2)
        if center <= (needle_length / 2) * math.sin(angle):
            hits += 1
    return (2 * needle_length * drops) / (line_gap * hits)

print(buffon_pi())
```

---

## 6. Iterative Algorithms

### 6-1. Gauss–Legendre / Brent–Salamin Algorithm (1976)

**Core idea**: Uses the fact that the arithmetic-geometric mean (AGM) — alternately computing the arithmetic mean and geometric mean of two numbers — is connected to elliptic integrals. This is a quadratically convergent algorithm: the number of correct digits roughly doubles with each iteration. Why the AGM connects to elliptic integrals will be covered in detail separately.

**a) Unicode**
```
a₀=1, b₀=1/√2, t₀=1/4, p₀=1
a(n+1)=(aₙ+bₙ)/2, b(n+1)=√(aₙbₙ), t(n+1)=tₙ−pₙ(aₙ−a(n+1))², p(n+1)=2pₙ
π ≈ (aₙ+bₙ)²/(4tₙ)
```

**b) LaTeX**
```latex
a_0=1,\ b_0=\dfrac{1}{\sqrt2},\ t_0=\dfrac14,\ p_0=1

a_{n+1}=\frac{a_n+b_n}{2},\quad b_{n+1}=\sqrt{a_n b_n},\quad t_{n+1}=t_n-p_n(a_n-a_{n+1})^2,\quad p_{n+1}=2p_n

\pi \approx \frac{(a_n+b_n)^2}{4t_n}
```

**c) Mathematica**
```mathematica
gaussLegendrePi[iterations_] := Module[{a, b, t, p},
  a = 1.0; b = 1/Sqrt[2.0]; t = 1/4.0; p = 1.0;
  Do[
    anew = (a + b)/2;
    bnew = Sqrt[a*b];
    t = t - p*(a - anew)^2;
    p = 2*p;
    a = anew; b = bnew;
    , {iterations}];
  N[(a + b)^2/(4*t), 20]
]
gaussLegendrePi[5]
```

**d) Python**
```python
import math

def gauss_legendre_pi(iterations=5):
    a, b, t, p = 1.0, 1/math.sqrt(2), 1/4, 1.0
    for _ in range(iterations):
        a_next = (a + b) / 2
        b_next = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        p *= 2
        a, b = a_next, b_next
    return (a + b)**2 / (4 * t)

print(gauss_legendre_pi())
```

---

### 6-2. The Borwein Brothers' Quartic Algorithm (1985)

**Core idea**: Derived from modular equation theory for elliptic integrals. When computed exactly, one iteration of this algorithm produces the same result as two iterations of the Gauss–Legendre algorithm, which is why it exhibits quartic convergence — the number of correct digits quadruples with each step. This equivalence and the derivation from modular equations will be covered in detail separately.

**a) Unicode**
```
a₀=6−4√2, y₀=√2−1
y(k+1)=(1−(1−y⁴ₖ)^(1/4)) / (1+(1−y⁴ₖ)^(1/4))
a(k+1)=aₖ(1+y(k+1))⁴ − 2^(2k+3)·y(k+1)·(1+y(k+1)+y(k+1)²)
1/aₖ → π (quartic convergence)
```

**b) LaTeX**
```latex
a_0 = 6-4\sqrt{2}, \quad y_0 = \sqrt{2}-1

y_{k+1} = \frac{1-(1-y_k^4)^{1/4}}{1+(1-y_k^4)^{1/4}}

a_{k+1} = a_k(1+y_{k+1})^4 - 2^{2k+3}y_{k+1}(1+y_{k+1}+y_{k+1}^2)

\lim_{k\to\infty}\frac{1}{a_k} = \pi
```

**c) Mathematica**
```mathematica
borweinQuarticPi[iterations_] := Module[{a, y},
  a = 6 - 4*Sqrt[2.0]; y = Sqrt[2.0] - 1;
  Do[
    ynew = (1 - (1 - y^4)^(1/4))/(1 + (1 - y^4)^(1/4));
    a = a*(1 + ynew)^4 - 2^(2 k + 3)*ynew*(1 + ynew + ynew^2);
    y = ynew;
    , {k, 0, iterations - 1}];
  N[1/a, 25]
]
borweinQuarticPi[3]
```

**d) Python**
```python
from mpmath import mp, mpf, sqrt

mp.dps = 50

def borwein_quartic_pi(iterations=3):
    a = 6 - 4*sqrt(2)
    y = sqrt(2) - 1
    for k in range(iterations):
        root = (1 - y**4) ** mpf('0.25')
        y_next = (1 - root) / (1 + root)
        a = a * (1 + y_next)**4 - mpf(2)**(2*k + 3) * y_next * (1 + y_next + y_next**2)
        y = y_next
    return 1 / a

print(borwein_quartic_pi())
```

---

## 7. Spigot (Digit-Extraction) Algorithms

### 7-1. The BBP Formula (Bailey–Borwein–Plouffe, 1995)

**Core idea**: The first "spigot" formula that can extract a specific digit — in base 16 (or base 2) — without computing all the digits before it in order. It was discovered by computer, using an integer-relation-detection algorithm called PSLQ.

**a) Unicode**
```
π = Σ[k=0,∞] (1/16^k)·(4/(8k+1) − 2/(8k+4) − 1/(8k+5) − 1/(8k+6))
```

**b) LaTeX**
```latex
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right)
```

**c) Mathematica**
```mathematica
Pi == Sum[(1/16^k)*(4/(8 k + 1) - 2/(8 k + 4) - 1/(8 k + 5) - 1/(8 k + 6)), {k, 0, Infinity}]
N[Sum[(1/16^k)*(4/(8 k + 1) - 2/(8 k + 4) - 1/(8 k + 5) - 1/(8 k + 6)), {k, 0, 20}], 20]
```

**d) Python**
```python
from mpmath import mp, mpf

mp.dps = 30

def bbp_pi(terms=30):
    total = mpf(0)
    for k in range(terms):
        total += (mpf(1)/16**k) * (mpf(4)/(8*k+1) - mpf(2)/(8*k+4) - mpf(1)/(8*k+5) - mpf(1)/(8*k+6))
    return total

print(bbp_pi())
```

---

### 7-2. Bellard's Formula (1997)

**Core idea**: Uses the same principle as the BBP formula but with the number of terms and coefficients optimized. It can reach the same precision using about 43% fewer operations than BBP, so it is often used to verify large-scale computation results.

**a) Unicode**
```
π = (1/2⁶)·Σ[k=0,∞] ((−1)^k/2^(10k))·(−2⁵/(4k+1) − 1/(4k+3) + 2⁸/(10k+1) − 2⁶/(10k+3) − 2²/(10k+5) − 2²/(10k+7) + 1/(10k+9))
```

**b) LaTeX**
```latex
\pi = \frac{1}{2^{6}} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{2^{10k}} \left( -\frac{2^{5}}{4k+1} - \frac{1}{4k+3} + \frac{2^{8}}{10k+1} - \frac{2^{6}}{10k+3} - \frac{2^{2}}{10k+5} - \frac{2^{2}}{10k+7} + \frac{1}{10k+9} \right)
```

**c) Mathematica**
```mathematica
bellardTerm[k_] := ((-1)^k/2^(10 k))*(-2^5/(4 k + 1) - 1/(4 k + 3) +
     2^8/(10 k + 1) - 2^6/(10 k + 3) - 2^2/(10 k + 5) -
     2^2/(10 k + 7) + 1/(10 k + 9))
N[(1/2^6)*Sum[bellardTerm[k], {k, 0, 20}], 20]
```

**d) Python**
```python
from mpmath import mp, mpf

mp.dps = 30

def bellard_pi(terms=20):
    total = mpf(0)
    for k in range(terms):
        term = (mpf(-1)**k / mpf(2)**(10*k)) * (
            -mpf(2)**5/(4*k+1) - mpf(1)/(4*k+3)
            + mpf(2)**8/(10*k+1) - mpf(2)**6/(10*k+3)
            - mpf(2)**2/(10*k+5) - mpf(2)**2/(10*k+7)
            + mpf(1)/(10*k+9)
        )
        total += term
    return total / 64  # 1/2^6

print(bellard_pi())
```

---

## Notes

- **Mathematica** code first states the definition symbolically using infinite sum/product notation (`Sum`, `Product`), then gives a finite-term `N[...]` approximation to obtain an actual numerical value.
- **Python** code uses only the standard library (`math`, `random`) where possible; items requiring high precision (Ramanujan, Chudnovsky, Borwein, BBP, Bellard) use the `mpmath` library (requires `pip install mpmath`).
- The Borwein brothers' **cubic convergence algorithm** and **Liu Hui's circle-cutting method** were excluded from this four-format presentation because the original source material did not provide their concrete formulas. Let us know if you'd like these prepared separately.
- Of the 18 formulas in this document, the accompanying interactive HTML page implements 17 — all except **1-5, the accelerated Gregory series (via the zeta function)**.
- The publication year of Sharp's series (1-6) is given as either 1699 or 1717 (based on a more generalized form of the series), depending on the source. 1699 is the most widely cited year for when he computed π to 72 digits.
