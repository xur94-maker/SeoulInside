# 파이(π) 계산 공식들과 인터랙티브 페이지

파이 값을 계산하는 방법은 매우 다양하며, 지금 이 순간에도 새로운 방식이 계속 제시되고 있습니다. 이 공식들이 어떤 의미를 갖고 유도되었는지, 또 어떤 내용을 설명하는지에 대해서는 조만간 매우 상세하게 글을 써서 올리도록 하겠습니다.

이번 글은 이 공식들이 어떤 의미인지, 또는 왜 이것이 파이 값을 갖는지에 대한 설명이 아니라, 파이 값을 계산하는 방법에는 어떤 것들이 있는지 살펴보고, 인터랙티브 페이지를 통해 파이 값이 계산되는 과정을 직접 구경하면서 어느 쪽이 더 효율적인지 비교해 볼 수 있는 작은 경험으로 생각해 주시면 좋겠습니다.



---

## 1. 무한급수 (Series)

### 1-1. 라이프니츠 급수 (Gregory–Leibniz, 1674년경)

**핵심 아이디어**: arctan(x)의 테일러 급수에 x=1을 대입해서 얻는 식입니다. arctan(1) = π/4라는 사실에서 나오지만, 항이 1/n 크기로만 줄어들어 수렴은 매우 느립니다.

**가) 유니코드**
```
π/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − ⋯
```

**나) LaTeX**
```latex
\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}
```

**다) Mathematica**
```mathematica
Pi/4 == Sum[(-1)^n/(2 n + 1), {n, 0, Infinity}]
(* 수치 근사 *)
N[4*Sum[(-1)^n/(2 n + 1), {n, 0, 100000}], 10]
```

**라) Python**
```python
def leibniz_pi(terms=1_000_000):
    total = 0.0
    for n in range(terms):
        total += (-1) ** n / (2 * n + 1)
    return 4 * total

print(leibniz_pi())
```

---

### 1-2. 니라칸타 급수 (Nilakantha, 15세기)

**핵심 아이디어**: 라이프니츠 급수를 재배열해 수렴을 가속한 급수입니다. 항이 1/n³ 크기로 줄어들어 원래보다 훨씬 빠르게 π에 다가갑니다.

**가) 유니코드**
```
π = 3 + 4/(2·3·4) − 4/(4·5·6) + 4/(6·7·8) − ⋯
```

**나) LaTeX**
```latex
\pi = 3 + \sum_{n=1}^{\infty} \frac{(-1)^{n+1} \cdot 4}{(2n)(2n+1)(2n+2)}
```

**다) Mathematica**
```mathematica
Pi == 3 + Sum[(-1)^(n + 1)*4/((2 n)(2 n + 1)(2 n + 2)), {n, 1, Infinity}]
N[3 + Sum[(-1)^(n + 1)*4/((2 n)(2 n + 1)(2 n + 2)), {n, 1, 10000}], 10]
```

**라) Python**
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

### 1-3. 바젤 문제 (오일러, 1735)

**핵심 아이디어**: 모든 자연수의 역제곱 합이 π²/6에 수렴한다는 오일러의 정리입니다. sin(x)/x를 다항식처럼 무한곱으로 인수분해한 뒤 계수를 테일러 급수와 비교하는 방식으로 증명되었습니다.

**가) 유니코드**
```
1/1² + 1/2² + 1/3² + ⋯ = π²/6
```

**나) LaTeX**
```latex
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
```

**다) Mathematica**
```mathematica
Sum[1/n^2, {n, 1, Infinity}] == Pi^2/6
N[Sqrt[6*Sum[1/n^2, {n, 1, 1000000}]], 10]
```

**라) Python**
```python
import math

def basel_pi(terms=1_000_000):
    total = sum(1 / n**2 for n in range(1, terms + 1))
    return math.sqrt(6 * total)

print(basel_pi())
```

---

### 1-4. 마친 공식 (Machin's formula, 1706)

**핵심 아이디어**: π/4 = 4arctan(1/5) − arctan(1/239)라는 항등식을 이용합니다. arctan(1/5)와 arctan(1/239) 모두 인수가 1보다 훨씬 작아 테일러 급수가 빠르게 수렴합니다.

**가) 유니코드**
```
π/4 = 4·arctan(1/5) − arctan(1/239)
```

**나) LaTeX**
```latex
\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}
```

**다) Mathematica**
```mathematica
Pi/4 == 4*ArcTan[1/5] - ArcTan[1/239]
N[4*(4*ArcTan[1/5] - ArcTan[1/239]), 20]
```

**라) Python**
```python
import math

def machin_pi():
    return 4 * (4 * math.atan(1/5) - math.atan(1/239))

print(machin_pi())
```

---

### 1-5. 그레고리 급수의 가속형 (제타 함수 이용)

**핵심 아이디어**: 라이프니츠(그레고리) 급수를 오일러 변환(Vardi 변환)으로 재배열한 것입니다. 리만 제타 함수 ζ(k+1)을 계수로 끌어들여 오차가 (3/4)^k 수준으로 줄어들도록 가속했습니다.

**가) 유니코드**
```
π = Σ[k=1,∞] (3^k − 1)/4^k · ζ(k+1)
```

**나) LaTeX**
```latex
\pi = \sum_{k=1}^{\infty} \frac{3^k - 1}{4^k}\,\zeta(k+1)
```

**다) Mathematica**
```mathematica
Pi == Sum[((3^k - 1)/4^k)*Zeta[k + 1], {k, 1, Infinity}]
N[Sum[((3^k - 1)/4^k)*Zeta[k + 1], {k, 1, 50}], 15]
```

**라) Python**
```python
from mpmath import mp, zeta, mpf

mp.dps = 30  # 소수점 자릿수

def zeta_accelerated_pi(terms=100):
    total = mpf(0)
    for k in range(1, terms + 1):
        total += (mpf(3)**k - 1) / mpf(4)**k * zeta(k + 1)
    return total

print(zeta_accelerated_pi())
```

---

### 1-6. 샤프의 급수 (Abraham Sharp, 1699)

**핵심 아이디어**: arctan(x) 급수에 x=1/√3을 대입한 것으로, arctan(1/√3) = π/6이라는 사실에서 나옵니다. 항이 1/3^k로 줄어들어 라이프니츠 급수보다 훨씬 빠릅니다.

**가) 유니코드**
```
π = Σ[k=0,∞] 2·(−1)^k·√3 / (3^k·(2k+1))
```

**나) LaTeX**
```latex
\pi = \sum_{k=0}^{\infty} \frac{2(-1)^k \sqrt{3}}{3^k(2k+1)}
```

**다) Mathematica**
```mathematica
Pi == Sum[(2*(-1)^k*Sqrt[3])/(3^k*(2 k + 1)), {k, 0, Infinity}]
N[Sum[(2*(-1)^k*Sqrt[3])/(3^k*(2 k + 1)), {k, 0, 50}], 15]
```

**라) Python**
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

### 1-7. 라마누잔 급수 (1910년경)

**핵심 아이디어**: 타원적분의 모듈러 방정식과 초기하급수 이론에서 유도된 급수입니다. 증명 없이 발표되었지만, 항 하나마다 정확한 자릿수가 약 8개씩 늘어날 정도로 강력합니다. 모듈러 방정식이 어떻게 π로 이어지는지는 별도로 상세히 다룰 예정입니다.

**가) 유니코드**
```
1/π = (2√2/9801) · Σ[k=0,∞] (4k)!·(1103+26390k) / ((k!)⁴·396^(4k))
```

**나) LaTeX**
```latex
\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^{\infty} \frac{(4k)!(1103+26390k)}{(k!)^4 \, 396^{4k}}
```

**다) Mathematica**
```mathematica
1/Pi == (2*Sqrt[2]/9801)*Sum[((4 k)!*(1103 + 26390 k))/((k!)^4*396^(4 k)), {k, 0, Infinity}]
N[1/((2*Sqrt[2]/9801)*Sum[((4 k)!*(1103 + 26390 k))/((k!)^4*396^(4 k)), {k, 0, 5}]), 30]
```

**라) Python**
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

### 1-8. 추드노프스키 알고리즘 (Chudnovsky, 1988)

**핵심 아이디어**: 라마누잔 급수와 같은 계열로, 헤그너 수 640320과 관련된 모듈러 방정식에서 유도되었습니다. 항 하나마다 정확한 자릿수가 약 14개씩 늘어나 오늘날 π를 수십억 자리까지 계산할 때 가장 널리 쓰이는 공식입니다. 모듈러 방정식이 어떻게 π로 이어지는지는 별도로 상세히 다룰 예정입니다.

**가) 유니코드**
```
1/π = 12·Σ[k=0,∞] (−1)^k·(6k)!·(13591409+545140134k) / ((3k)!·(k!)³·640320^(3k+3/2))
```

**나) LaTeX**
```latex
\frac{1}{\pi} = 12\sum_{k=0}^{\infty} \frac{(-1)^k (6k)!(13591409+545140134k)}{(3k)!(k!)^3 \, 640320^{3k+3/2}}
```

**다) Mathematica**
```mathematica
1/Pi == 12*Sum[((-1)^k*(6 k)!*(13591409 + 545140134 k))/((3 k)!*(k!)^3*640320^(3 k + 3/2)), {k, 0, Infinity}]
N[1/(12*Sum[((-1)^k*(6 k)!*(13591409 + 545140134 k))/((3 k)!*(k!)^3*640320^(3 k + 3/2)), {k, 0, 3}]), 50]
```

**라) Python**
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

## 2. 무한곱 (Infinite Products)

### 2-1. 월리스 곱 (Wallis, 1655)

**핵심 아이디어**: sin(x)를 무한곱 형태로 인수분해한 뒤 x=π/2를 대입해 얻는 공식입니다. 각 인수가 1에 서서히 가까워지는 형태라 수렴은 느린 편입니다.

**가) 유니코드**
```
π/2 = (2/1)·(2/3)·(4/3)·(4/5)·(6/5)·(6/7)·⋯
```

**나) LaTeX**
```latex
\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2-1}
```

**다) Mathematica**
```mathematica
Pi/2 == Product[(4 n^2)/(4 n^2 - 1), {n, 1, Infinity}]
N[2*Product[(4 n^2)/(4 n^2 - 1), {n, 1, 100000}], 8]
```

**라) Python**
```python
def wallis_pi(terms=1_000_000):
    product = 1.0
    for n in range(1, terms + 1):
        product *= (4 * n**2) / (4 * n**2 - 1)
    return 2 * product

print(wallis_pi())
```

---

### 2-2. 비에트의 공식 (Viète, 1593)

**핵심 아이디어**: 반각(半角) 공식을 반복 적용해, 원에 내접하는 정다각형(4각→8각→16각…)의 넓이가 원의 넓이에 가까워지는 과정을 무한곱으로 표현한 것입니다. 역사상 처음 발견된 무한곱 공식으로 꼽힙니다.

**가) 유니코드**
```
2/π = √(1/2) · √(1/2 + 1/2·√(1/2)) · √(1/2 + 1/2·√(1/2 + 1/2·√(1/2))) ⋯
```

**나) LaTeX**
```latex
\frac{2}{\pi} = \sqrt{\frac{1}{2}} \cdot \sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}} \cdot \sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}} \cdots
```

**다) Mathematica**
```mathematica
(* 반복적으로 항을 생성하여 근사 *)
nTerms = 15;
a = Sqrt[2]/2;
product = a;
Do[
  a = Sqrt[(1 + a)/2];
  product *= a;
  , {nTerms}];
N[2/product, 10]
```

**라) Python**
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

## 3. 연분수 (Continued Fractions)

### 3-1. 브롱커의 연분수 (Brouncker, 1655)

**핵심 아이디어**: 월리스 곱을 연분수 형태로 바꿔 쓴 것입니다. 두 표현이 실제로 같은 값에 수렴한다는 사실은 이후 오일러가 일반적인 방법으로 증명했습니다.

**가) 유니코드**
```
4/π = 1 + 1²/(2 + 3²/(2 + 5²/(2 + 7²/(2 + ⋯))))
```

**나) LaTeX**
```latex
\frac{4}{\pi} = 1 + \cfrac{1^2}{2+\cfrac{3^2}{2+\cfrac{5^2}{2+\cfrac{7^2}{2+\cdots}}}}
```

**다) Mathematica**
```mathematica
(* 아래에서 위로 연분수를 계산 *)
depth = 200;
cf = 0;
Do[
  cf = (2 n - 1)^2/(2 + cf);
  , {n, depth, 1, -1}];
N[4/(1 + cf), 10]
```

**라) Python**
```python
def brouncker_pi(depth=1000):
    cf = 0.0
    for n in range(depth, 0, -1):
        cf = (2*n - 1)**2 / (2 + cf)
    return 4 / (1 + cf)

print(brouncker_pi())
```

---

## 4. 기하학적 방법 (고전)

### 4-1. 아르키메데스의 다각형법 (BC 250년경)

**핵심 아이디어**: 원에 내접하는 정다각형과 외접하는 정다각형의 둘레로 원주(π)를 위아래에서 조여 오는 방식입니다. 변의 수를 두 배로 늘릴 때마다(반각 공식 적용) 오차가 대략 4분의 1씩 줄어듭니다.

**가) 유니코드**
```
2^k·n·sin(π/(2^k·n)) < π < 2^k·n·tan(π/(2^k·n))
```

**나) LaTeX**
```latex
2^k \cdot n \sin\!\left(\frac{\pi}{2^k n}\right) \;<\; \pi \;<\; 2^k \cdot n \tan\!\left(\frac{\pi}{2^k n}\right)
```

**다) Mathematica**
```mathematica
(* 정육각형(n=6)에서 시작해 k번 변을 두 배로 늘려 근사 *)
archimedesBounds[k_, n_ : 6] := Module[{lower, upper},
  lower = N[2^k*n*Sin[Pi/(2^k*n)], 10];
  upper = N[2^k*n*Tan[Pi/(2^k*n)], 10];
  {lower, upper}
]
archimedesBounds[10]
```

**라) Python**
```python
import math

def archimedes_bounds(k, n=6):
    lower = 2**k * n * math.sin(math.pi / (2**k * n))
    upper = 2**k * n * math.tan(math.pi / (2**k * n))
    return lower, upper

print(archimedes_bounds(10))
```

---

## 5. 확률적 방법

### 5-1. 몬테카를로 방법

**핵심 아이디어**: 한 변의 길이가 2인 정사각형과 그 안에 내접한 반지름 1인 원의 넓이 비는 π/4입니다. 정사각형 안에 점을 무작위로 뿌려 원 안에 떨어지는 비율을 세면 이 넓이 비를 통계적으로 추정할 수 있습니다.

**가) 유니코드**
```
π ≈ 4 · (정사각형 안에서 원 안에 떨어진 점의 수) / (전체 점의 수)
```

**나) LaTeX**
```latex
\pi \approx 4 \cdot \frac{\text{정사각형 안에서 원 안에 떨어진 점의 수}}{\text{전체 점의 수}}
```

**다) Mathematica**
```mathematica
SeedRandom[1];
n = 1000000;
pts = RandomReal[{-1, 1}, {n, 2}];
inside = Count[pts, {x_, y_} /; x^2 + y^2 <= 1];
N[4*inside/n, 6]
```

**라) Python**
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

### 5-2. 뷔퐁의 바늘 문제 (Buffon's needle, 1777)

**핵심 아이디어**: 일정한 간격의 평행선 위에 바늘을 무작위로 던졌을 때 선에 걸칠 확률은 기하학적으로 2l/(πt)로 계산됩니다(l: 바늘 길이, t: 선 간격). 이 확률을 실험적으로 추정한 뒤 식을 뒤집어 π를 근사합니다.

**가) 유니코드**
```
π ≈ (2·l·n) / (t·h)
(l: 바늘 길이, t: 평행선 간격, n: 던진 횟수, h: 선에 걸친 횟수)
```

**나) LaTeX**
```latex
\pi \approx \frac{2 \cdot l \cdot n}{t \cdot h}
```

**다) Mathematica**
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

**라) Python**
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

## 6. 반복(iterative) 알고리즘

### 6-1. 가우스-르장드르 / 브렌트-살라민 알고리즘 (1976)

**핵심 아이디어**: 두 수의 산술평균과 기하평균을 번갈아 계산하는 산술-기하 평균(AGM)이 타원적분과 연결된다는 사실을 이용합니다. 반복할 때마다 정확한 자릿수가 두 배로 늘어나는 2차 수렴 알고리즘입니다. AGM과 타원적분이 왜 연결되는지는 별도로 상세히 다룰 예정입니다.

**가) 유니코드**
```
a₀=1, b₀=1/√2, t₀=1/4, p₀=1
a(n+1)=(aₙ+bₙ)/2, b(n+1)=√(aₙbₙ), t(n+1)=tₙ−pₙ(aₙ−a(n+1))², p(n+1)=2pₙ
π ≈ (aₙ+bₙ)²/(4tₙ)
```

**나) LaTeX**
```latex
a_0=1,\ b_0=\dfrac{1}{\sqrt2},\ t_0=\dfrac14,\ p_0=1

a_{n+1}=\frac{a_n+b_n}{2},\quad b_{n+1}=\sqrt{a_n b_n},\quad t_{n+1}=t_n-p_n(a_n-a_{n+1})^2,\quad p_{n+1}=2p_n

\pi \approx \frac{(a_n+b_n)^2}{4t_n}
```

**다) Mathematica**
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

**라) Python**
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

### 6-2. 보웨인 형제의 4차 수렴 알고리즘 (Borwein's quartic algorithm, 1985)

**핵심 아이디어**: 타원적분의 모듈러 방정식 이론에서 유도된 알고리즘입니다. 정확히 계산하면 이 알고리즘의 한 번 반복이 가우스-르장드르 알고리즘의 두 번 반복과 같은 결과를 내놓기 때문에, 자릿수가 반복마다 네 배씩 늘어나는 4차 수렴이 나타납니다. 이 등가 관계와 모듈러 방정식의 유도 과정은 별도로 상세히 다룰 예정입니다.

**가) 유니코드**
```
a₀=6−4√2, y₀=√2−1
y(k+1)=(1−(1−y⁴ₖ)^(1/4)) / (1+(1−y⁴ₖ)^(1/4))
a(k+1)=aₖ(1+y(k+1))⁴ − 2^(2k+3)·y(k+1)·(1+y(k+1)+y(k+1)²)
1/aₖ → π (4차 수렴)
```

**나) LaTeX**
```latex
a_0 = 6-4\sqrt{2}, \quad y_0 = \sqrt{2}-1

y_{k+1} = \frac{1-(1-y_k^4)^{1/4}}{1+(1-y_k^4)^{1/4}}

a_{k+1} = a_k(1+y_{k+1})^4 - 2^{2k+3}y_{k+1}(1+y_{k+1}+y_{k+1}^2)

\lim_{k\to\infty}\frac{1}{a_k} = \pi
```

**다) Mathematica**
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

**라) Python**
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

## 7. 스피곳(digit-extraction) 알고리즘

### 7-1. BBP 공식 (Bailey–Borwein–Plouffe, 1995)

**핵심 아이디어**: 처음부터 순서대로 계산하지 않고도 16진수(또는 2진수) 상의 특정 위치의 자릿수를 바로 뽑아낼 수 있는 최초의 '스피곳' 공식입니다. PSLQ라는 정수관계 탐색 알고리즘으로 컴퓨터가 발견했습니다.

**가) 유니코드**
```
π = Σ[k=0,∞] (1/16^k)·(4/(8k+1) − 2/(8k+4) − 1/(8k+5) − 1/(8k+6))
```

**나) LaTeX**
```latex
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right)
```

**다) Mathematica**
```mathematica
Pi == Sum[(1/16^k)*(4/(8 k + 1) - 2/(8 k + 4) - 1/(8 k + 5) - 1/(8 k + 6)), {k, 0, Infinity}]
N[Sum[(1/16^k)*(4/(8 k + 1) - 2/(8 k + 4) - 1/(8 k + 5) - 1/(8 k + 6)), {k, 0, 20}], 20]
```

**라) Python**
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

### 7-2. 벨라르 공식 (Bellard's formula, 1997)

**핵심 아이디어**: BBP 공식과 같은 원리를 쓰지만 항의 개수와 계수를 최적화한 변형입니다. 같은 정밀도를 BBP보다 약 43% 더 적은 연산으로 얻을 수 있어, 대규모 계산 결과를 검증하는 데 자주 쓰입니다.

**가) 유니코드**
```
π = (1/2⁶)·Σ[k=0,∞] ((−1)^k/2^(10k))·(−2⁵/(4k+1) − 1/(4k+3) + 2⁸/(10k+1) − 2⁶/(10k+3) − 2²/(10k+5) − 2²/(10k+7) + 1/(10k+9))
```

**나) LaTeX**
```latex
\pi = \frac{1}{2^{6}} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{2^{10k}} \left( -\frac{2^{5}}{4k+1} - \frac{1}{4k+3} + \frac{2^{8}}{10k+1} - \frac{2^{6}}{10k+3} - \frac{2^{2}}{10k+5} - \frac{2^{2}}{10k+7} + \frac{1}{10k+9} \right)
```

**다) Mathematica**
```mathematica
bellardTerm[k_] := ((-1)^k/2^(10 k))*(-2^5/(4 k + 1) - 1/(4 k + 3) +
     2^8/(10 k + 1) - 2^6/(10 k + 3) - 2^2/(10 k + 5) -
     2^2/(10 k + 7) + 1/(10 k + 9))
N[(1/2^6)*Sum[bellardTerm[k], {k, 0, 20}], 20]
```

**라) Python**
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

## 참고 사항

- **Mathematica** 코드는 무한합/무한곱 기호(`Sum`, `Product`)로 정의를 먼저 표기하고, 실제 값을 얻기 위한 `N[...]` 유한항 근사 코드를 함께 제시했습니다.
- **Python** 코드는 표준 라이브러리(`math`, `random`)만으로 가능한 항목은 그렇게 작성했고, 고정밀도가 필요한 항목(라마누잔, 추드노프스키, 보웨인, BBP, 벨라르)은 `mpmath` 라이브러리를 사용했습니다 (`pip install mpmath` 필요).
- 보웨인 형제의 **3차 수렴 알고리즘**과 **유휘(劉徽)의 할원술**은 원문에서 구체적 공식이 제시되지 않아 이번 4단 표기에서 제외했습니다. 필요하시면 별도로 정리해 드릴 수 있습니다.
- 함께 제공하는 인터랙티브 페이지(HTML)에는 이 문서의 18개 공식 중 **1-5. 그레고리 급수의 가속형(제타 함수 이용)** 을 제외한 17개가 구현되어 있습니다.
- 1-6 샤프의 급수는 자료에 따라 발표 연도를 1699년 또는 1717년(보다 일반화된 급수 형태 기준)으로 표기하기도 합니다. 그가 π를 72자리까지 계산한 시점은 1699년이 가장 널리 인용되는 연도입니다.
