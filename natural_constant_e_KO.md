# 자연상수 e를 구하는 방법 
## 쉬운 요약

**e란?**
`e ≈ 2.71828…`은 π처럼 끝없이 이어지고 반복되지 않는 숫자입니다. 지금 있는 양에 비례해서 계속 불어나는 현상이 끝까지 갔을 때 도달하는 한계값입니다.

**쉬운 예: 은행 이자**
1원을 맡기고 1년에 100% 이자를 준다고 할 때, 이자를 붙이는 횟수를 늘리면 이렇게 됩니다.

- 1년에 한 번: 2원
- 매달: 약 2.61원
- 매일: 약 2.71원
- 순간순간 계속: 약 2.71828원 (여기서 더는 늘지 않음)

아무리 자주 붙여도 이 한계를 넘지 못하는데, 그 한계값이 e입니다.

**왜 "자연"상수일까?**
세균 증식, 방사성 붕괴처럼 자연에서 "현재 양에 비례해 변하는" 현상이 이 숫자로 저절로 표현되기 때문입니다. 수학적으로도 `e^x`는 미분해도 자기 자신이 되어 계산이 가장 간단합니다.

**어디에 쓰일까?**
- 돈: 연속복리
- 생물·사회: 세균 증식, 인구 성장
- 물리: 방사성 붕괴, 커피가 식는 모양
- 통계: 정규분포, 푸아송 분포
- AI: 시그모이드, 소프트맥스 함수

**e를 구하는 여러 가지 길 (이 글의 내용)**
- 극한 `(1+1/n)^n`: 이자 이야기 그대로. 직관적이지만 수렴이 느립니다.
- 급수 `\sum 1/k!`: 가장 빠르고 실용적입니다. 35조 자리 세계기록도 이 방식에 기반합니다.
- 무한곱: 카탈랑·피핀저 공식. 피핀저 쪽이 훨씬 빨리 수렴합니다.
- 연분수: 오일러의 `[2; 1, 2, 1, 1, 4, 1, 1, 6, …]`. 규칙적인 무늬가 아름답고, e가 무리수임을 증명하는 데 쓰였습니다.
- 확률·조합: "0~1 난수를 합이 1을 넘을 때까지 더하면 평균 e개가 필요하다", "선물 교환에서 아무도 자기 선물을 못 받을 확률은 약 1/e" 같은 뜻밖의 등장이 있습니다.
- 미적분: `e^x`의 미분은 자기 자신, `\int_1^e (1/x)\,dx = 1`.
- 알고리즘: 스피곳, CORDIC, AGM.

**덤: 우연의 일치**
`163(\pi - e) ≈ 69`, `e^\pi - \pi ≈ 20` 같은 신기한 근사와, 앤드루 잭슨(1828년 당선)으로 "2.7 1828 1828"을 외우는 암기법도 소개합니다.

**한 줄 결론**
e는 "스스로 불어나는 것"의 숫자이고, 이자, 확률, 미적분 등 서로 다른 길에서 같은 값으로 모입니다.

---

# 본문

자연상수 `e \approx 2.718281828459045\ldots`는 π만큼이나 다양한 방법으로 계산되어 왔습니다. 극한, 급수, 무한곱, 연분수, 확률, 미적분, 하드웨어 알고리즘까지 — e를 만나는 방식은 생각보다 훨씬 다양합니다. 이 문서는 각 방법을 Unicode / LaTeX / Mathematica(의사코드) / Python 네 가지 형태로 나란히 정리하고, 발견자와 연대까지 함께 담았습니다.

---

## 1. 기본 정의 (극한)

**핵심 아이디어**: 야코프 베르누이(Jacob Bernoulli)가 1683년 연속복리 문제를 풀다가 처음 발견한 상수입니다. `n`을 무한히 크게 하며 이자를 "연속적으로" 복리 계산할 때 이 극한값이 등장합니다. 다만 `1/n` 형태로 오차가 줄기 때문에 수렴은 매우 느립니다.

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

print(limit_definition())  # 2.7182816941... (약 7자리 정확)
```

> **역사 한 줄**: 베르누이는 이 극한이 2와 3 사이에 있다는 것까지만 증명했습니다. "e"라는 기호와 완전한 급수 표현은 훗날 오일러가 붙였습니다.

---

## 2. 급수 (Series) — 가장 실용적

**핵심 아이디어**: 뉴턴이 1665년경 로그 계산 과정에서 이미 사실상 이 급수를 다루고 있었고, 오일러가 1727년경 "e"라는 표기를 도입하며 `\sum 1/k!` 형태로 정식화했습니다. `k!`이 폭발적으로 커지므로 극한 정의보다 훨씬 빠르게 수렴합니다.

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

print(taylor_series())  # 2.718281828459046 (20항만으로 15자리 정확)
```

**도빈스키 공식 (Dobiński's Formula, 1877)**: 집합 분할의 개수인 벨 수(Bell number) `B_n`이 `B_n = \frac{1}{e}\sum_{k=0}^{\infty}\frac{k^n}{k!}`로 표현됩니다. 뒤집으면 조합론(집합 분할)과 연결된 e의 또 다른 급수 표현을 얻습니다.

```latex
B_n = \frac{1}{e}\sum_{k=0}^{\infty} \frac{k^n}{k!} \quad\Longrightarrow\quad e = \frac{1}{B_n}\sum_{k=0}^{\infty}\frac{k^n}{k!}
```

> **세계기록 보강**: 실제 세계기록용 e 계산도 이 테일러 급수가 기본이지만, 항을 순서대로 더하지 않고 **이진 분할법(Binary Splitting)**으로 구간을 절반씩 나눠 재귀적으로 결합합니다. 이 방식(y-cruncher 프로그램)으로 2023년 12월 24일 Jordan Ranous가 e를 **35조(35,000,000,000,000) 자리**까지 계산해 현재 검증된 세계기록을 보유하고 있습니다.

---

## 3. 무한곱 (Infinite Product) — π의 월리스 곱과의 대칭

**핵심 아이디어**: π가 월리스의 무한곱(1655)을 갖는 것처럼, e에도 두 가지 무한곱 표현이 있습니다. 카탈랑(Catalan)이 1873년, 피핀저(Pippenger)가 1980년 각각 스털링 공식을 이용해 증명했습니다.

**카탈랑의 곱 공식 (1873)**
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

**피핀저의 곱 공식 (1980)** — 월리스 곱의 "e 버전"

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

print(pippenger_product())  # 2.7182818289... (카탈랑 곱보다 훨씬 빠르게 수렴)
```

> π/2의 월리스 곱은 지수가 단순히 항 개수로만 늘어나 수렴이 느린 반면, 이 두 곱은 지수가 `1/2^n`로 줄어들어 **훨씬 빠르게 수렴**합니다.

---

## 4. 연분수 (Continued Fraction) — 오일러, 1737

**핵심 아이디어**: 오일러가 1737년 저술한 논문에서 유도했고, 바로 이 연분수의 비주기성을 이용해 **e가 무리수임을 최초로 증명**했습니다(출판은 7년 뒤인 1744년). π의 연분수가 불규칙한 것과 달리, e의 연분수는 분모가 **2; 1, 2, 1, 1, 4, 1, 1, 6, ...** 로 규칙적으로 반복됩니다.

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
# 수렴 분수(convergent): 2/1, 3/1, 8/3, 11/4, 19/7, 87/32, 106/39, ...
```

> **특징**: 계산이 매우 빠르고 라운드오프 오차가 거의 없습니다. π는 연분수가 불규칙한데 e는 규칙적이라는 대조가 흥미롭습니다.

---

## 5. 확률적/조합론적 방법 (Stochastic & Combinatorial)

**5-1. 균일분포 합**

**핵심 아이디어**: (0,1) 구간의 균일분포에서 값을 계속 뽑아 더할 때, 합이 1을 넘기는 데 필요한 최소 개수의 기댓값이 정확히 e로 수렴합니다.

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

print(stochastic_uniform_sum())  # ≈2.7168 (O(1/√n)로 느리게 수렴)
```

**5-2. 교란순열(Derangement) 확률** — 몽모르(Montmort), 1708

**핵심 아이디어**: n개의 원소를 무작위로 섞었을 때 **고정점이 하나도 없을 확률**(교란순열이 될 확률)이 n이 커지면 `1/e`에 수렴합니다. 이 문제 자체는 1708년 몽모르가 처음 다뤘습니다(도박 문제에서 출발). 포함-배제 원리로 증명되며, 그 결과가 정확히 `1/e`의 테일러 급수 부분합과 일치합니다.

a) Unicode
```
lim[n→∞] Dₙ/n! = 1/e   (Dₙ: n개 원소의 교란순열 개수)
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

> 실용적으로는 "선물 교환에서 아무도 자기 선물을 못 받을 확률"처럼, `n!`을 `e`로 나눈 값에 가장 가까운 정수가 교란순열의 개수라는 관계로도 쓰입니다.

---

## 6. 미분방정식/해석학 (Calculus-based)

**핵심 아이디어**: e의 가장 근본적인 정의 — 자기 자신이 도함수가 되는 유일한 지수함수의 밑, 그리고 자연로그의 정의.

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
NIntegrate[1/x, {x, 1, E}]  (* 1로 수렴 *)
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

## 7. 알고리즘/공학적 방법 (Hardware & Digit-Extraction)

**7-1. 스피곳 알고리즘 (Spigot Algorithm)** — 라비노비츠·와곤(Rabinowitz & Wagon)의 π 스피곳(1990년대 초, 발표는 1995년) 원리를 e에 적용

**핵심 아이디어**: e를 혼합진법(mixed-radix) 표현 `(2; 1,1,1,1,\ldots)`으로 놓고, 배열을 10배씩 곱하며 자리올림을 오른쪽에서 왼쪽으로 전파시켜 **정확히 한 자릿수씩** 십진 숫자를 뽑아냅니다. 부동소수점 없이 정수 배열만으로 동작해 임베디드/하드웨어 구현에도 적합합니다.

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

**7-2. CORDIC 알고리즘** — 볼더(Jack Volder), 1959

**핵심 아이디어**: 덧셈과 비트 시프트(2⁻ⁱ 곱)만으로 `e^\theta`를 계산합니다. `e^z = \sinh(z)+\cosh(z)` 관계를 이용하며, 원래 항법 컴퓨터의 삼각함수 계산용으로 고안되었습니다.

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

**7-3. AGM (산술-기하 평균)** — 가우스·르장드르 계열

**핵심 아이디어**: `\ln(x)`를 AGM으로 고정밀 계산한 뒤, `\ln(e)=1`이라는 성질과 이분법을 결합해 e를 역산합니다.

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

## 8. 기타 변형 및 근사 (Other Methods)

- **이분법**: `\ln(e)=1`이라는 성질을 이용해 `\ln(x)=1`을 만족하는 `x`를 이분법으로 탐색.
- **오일러의 18자리 계산**: 오일러는 이 변형 급수를 이용해 e를 18자리까지 계산했습니다.

```latex
e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \cdots
```

---

## 한눈에 보기: e를 구하는 방법

**1. 극한 (Limit)**
- 대표 방법: `(1 + 1/n)^n`
- 발견자·연도: Bernoulli, 1683
- 수렴 속도: O(1/n)
- 시각화 적합성: 보통

**2. 급수 (Series)**
- 대표 방법: `\sum 1/k!`, 도빈스키 공식
- 발견자·연도: Newton/Euler, ~1665–1727 / Dobiński, 1877
- 수렴 속도: 초고속
- 시각화 적합성: 높음

**3. 무한곱 (Infinite Product)**
- 대표 방법: 카탈랑 곱, 피핀저 곱
- 발견자·연도: 1873 / 1980
- 수렴 속도: 빠름 (`1/2^n`)
- 시각화 적합성: 높음

**4. 연분수 (Continued Fraction)**
- 대표 방법: 오일러 연분수
- 발견자·연도: Euler, 1737
- 수렴 속도: 빠름
- 시각화 적합성: 높음

**5. 확률·조합 (Stochastic & Combinatorial)**
- 대표 방법: 균일분포 합, 교란순열
- 발견자·연도: — / Montmort, 1708
- 수렴 속도: O(1/√n)
- 시각화 적합성: 매우 높음

**6. 알고리즘 (Algorithm)**
- 대표 방법: 스피곳, CORDIC, AGM
- 발견자·연도: ~1990s / Volder 1959 / Gauss–Legendre
- 수렴 속도: 빠름
- 시각화 적합성: 낮음~보통

---

## 흥미로운 우연의 일치 (Aside)

π 문서에서 다룬 "π·e 조합이 정수에 가깝게 떨어지는 사례"들 중, e를 중심으로 볼 만한 것들을 모았습니다.

**1) 아직 설명이 완전하지 않은 근사**
- `163(\pi - e) \approx 69` — 정확히는 `68.99966\ldots`. 헤그너 수 163이 라마누잔 상수(`e^{\pi\sqrt{163}}`)에 이어 또 등장하는 게 흥미롭지만, 이 근사 자체의 완결된 이론적 설명은 아직 없습니다 (Irkhin, 2022, arXiv:2206.07174).
- `\pi^2 \approx 4e - 1` — 오차 약 0.04%.

**2) 최근에야 설명이 밝혀진 경우**
- `e^{\pi} - \pi \approx 20` (정확히는 `19.9991\ldots`) — 1988년 슬로안·콘웨이·플루프가 거의 동시에 발견했지만 "왜"인지는 오랫동안 미스터리였습니다. 야코비 세타함수 항등식 `\sum(8\pi k^2-2)e^{-\pi k^2}=1`에서 첫 항이 압도적으로 지배적이라는 사실로 2023년에야 널리 정리되었습니다.

**3) 순수한 암기용 트릭 (수학적 우연 아님)**
- `e = 2.7\ 1828\ 1828\ 45\ 90\ 45\ \ldots` — 앤드루 잭슨이 미국 **7**대 대통령이고, **1828**년에 당선되어 재선까지 했다는 사실(1828이 두 번 반복)을 이용한 유명한 암기법입니다. 미국 학생들 사이에서 자주 쓰이는 방식입니다.
- 재밌는 실화: 2004년 구글이 기업공개(IPO) 당시 목표 공모액을 **$2,718,281,828**로 설정했습니다 — 정확히 `e \times 10^9` 달러입니다 (센트 단위 45는 생략).

---

## Notes
- Mathematica 코드는 먼저 `Sum`/`Product`/`Limit` 같은 무한 연산 기호로 정의를 서술한 뒤, `N[...]`으로 유한 항 근사를 구합니다.
- Python 코드는 표준 라이브러리(`math`, `random`, `fractions`)만 사용했습니다. 더 높은 정밀도가 필요하면 `decimal` 또는 `mpmath`를 사용하세요.
- 매트릭스 지수함수(Padé 근사 + scaling-and-squaring) 방식은 실무에서 널리 쓰이지만, 이 문서에서는 스칼라 e 계산에 초점을 맞춰 생략했습니다. 필요하시면 별도로 정리해드릴 수 있습니다.
- 모든 수치는 직접 실행하여 참값 `e = 2.718281828459045\ldots`과 비교 검증했습니다.
