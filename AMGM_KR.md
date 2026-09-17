 # 산술평균-기하평균(AM-GM) 

 

---

## TL;DR (A·B·C로 이해하는 AM-GM)   
 

## 1. **"두 수 A, B가 있을 때, 평균은 곱의 제곱근보다 항상 크거나 같다."**

---

## 2. AM-GM이 뭐예요?

**A와 B 두 수가 있다고 합시다.**

```
(A + B) / 2  ≥  √(A × B)
```

- 왼쪽: **산술평균** (그냥 더해서 2로 나눔)
- 오른쪽: **기하평균** (곱해서 제곱근)

**즉, "더해서 나눈 값"이 "곱해서 루트한 값"보다 크거나 같다.**

---

## 3. 숫자로 확인해 봅시다

**예시 1: A = 4, B = 9**

```
왼쪽:  (4 + 9) / 2  =  6.5
오른쪽: √(4 × 9)    =  √36  =  6
결과:  6.5  ≥  6  ✓
```

**예시 2: A = 5, B = 5 (같은 수)**

```
왼쪽:  (5 + 5) / 2  =  5
오른쪽: √(5 × 5)    =  5
결과:  5  =  5  (등호!)
```

**예시 3: A = 1, B = 100**

```
왼쪽:  (1 + 100) / 2  =  50.5
오른쪽: √(1 × 100)    =  10
결과:  50.5  ≥  10  ✓
```

---

## 4. 언제 등호가 되나요?

```
A = B  일 때만  등호 성립
```

**즉, 두 수가 완전히 같을 때만 "=" 가 됩니다.**

- A = 4, B = 4 → 등호 ✓
- A = 4, B = 9 → 등호 아님 ✗

---

## 5. 세 수 A, B, C로 확장

**세 수가 있을 때:**

```
(A + B + C) / 3  ≥  ∛(A × B × C)
```

**숫자 예시: A = 1, B = 4, C = 9**

```
왼쪽:  (1 + 4 + 9) / 3  =  14/3  ≈  4.67
오른쪽: ∛(1 × 4 × 9)    =  ∛36   ≈  3.30
결과:  4.67  ≥  3.30  ✓
```

---

## 6. n개의 수로 확장

**n개의 수 A₁, A₂, ..., Aₙ이 있을 때:**

```
(A₁ + A₂ + ... + Aₙ) / n  ≥  ⁿ√(A₁ × A₂ × ... × Aₙ)
```

**말로 하면:**

> **"다 더해서 n으로 나눈 값 ≥ 다 곱해서 n제곱근한 값"**

---

## 7. 왜 중요한가요?

### 7.1 최적화 (가장 큰 값 찾기)

**문제: 둘레가 20인 직사각형 중 가장 넓은 것은?**

```
가로 = A, 세로 = B, 둘레 = 2(A + B) = 20
→ A + B = 10

넓이 = A × B

AM-GM:  (A + B) / 2  ≥  √(A × B)
        10 / 2  ≥  √(넓이)
        5  ≥  √(넓이)
        넓이  ≤  25
```

**등호 조건: A = B = 5 (정사각형)**

**→ "둘레가 같으면 정사각형이 가장 넓다."**

### 7.2 금융 (투자 수익률)

**3년 수익률: +40%, −30%, +20%**

```
산술평균:  (40 − 30 + 20) / 3  =  10%
기하평균:  ∛(1.4 × 0.7 × 1.2) − 1  ≈  5.55%
```

**→ "산술평균은 10%인데, 실제 복리는 5.55%밖에 안 된다."**

**이유: 변동성 때문에 손실이 생긴다.**

### 7.3 자료구조·알고리즘

**"합이 정해져 있으면, 곱은 모두 같을 때 최대."**

이 원리가 알고리즘 분석, 자원 배분, 회로 설계 등에 쓰입니다.

---

## 8. 평균 사슬 (A, B 두 수)

**두 수 A, B에 대해:**

```
2AB/(A+B)  ≤  √(AB)  ≤  (A+B)/2  ≤  √((A²+B²)/2)
    HM          GM         AM          QM
```

**말로 하면:**

> **조화평균 ≤ 기하평균 ≤ 산술평균 ≤ 제곱평균**

**숫자 예시: A = 1, B = 4**

```
HM = 2·1·4/(1+4)  =  8/5   =  1.6
GM = √(1·4)        =  2
AM = (1+4)/2       =  2.5
QM = √((1+16)/2)   =  √8.5  ≈  2.92

1.6  ≤  2  ≤  2.5  ≤  2.92  ✓
```

---

## 9. 등호 조건 정리

| 평균 | 등호 조건 |
|---|---|
| AM = GM | A = B |
| GM = HM | A = B |
| AM = QM | A = B |
| 모두 같음 | A = B |

**결론: 모든 평균이 같아지려면 A = B여야 한다.**

---

## 10. 자주 하는 실수

### 실수 1: 음수를 넣는다

```
A = −1, B = −4
AM = (−1 − 4)/2 = −2.5
GM = √((−1)(−4)) = 2
→ AM < GM  ✗ (성립 안 함)
```

**→ AM-GM은 음이 아닌 수에서만 성립.**

### 실수 2: 등호 조건을 무시한다

```
A = 1, B = 4
AM = 2.5, GM = 2
→ 등호가 아님
```

**→ 최적화 문제에서 등호 조건을 확인해야 최적점을 찾을 수 있다.**

### 실수 3: 가중치 합을 무시한다

**가중 AM-GM에서:**

```
λ₁ + λ₂ + ... + λₙ = 1  (반드시!)
```

**→ 이 조건이 없으면 부등식이 성립하지 않는다.**

---- 



























----
## 목차

1. 부등식의 정의와 기본 형태
2. 증명 (8가지)
3. 확장된 부등식 사슬: HM ≤ GM ≤ AM ≤ QM
4. 수치 예시
5. 기하학·최적화 응용
6. 금융·투자 응용 (변동성 손실)
7. 공학·물리학 응용
8. 컴퓨터과학·현대 최적화 이론 응용
9. 경제학 응용
10. 순수 수학·경시대회에서의 위상
11. 심화: 가우스의 산술기하평균 반복법(AGM)과 π 계산
12. 심화: 뮤어헤드 부등식으로의 일반화
13. 심화: 라그랑주 승수법과의 비교
14. 심화: 정보이론과의 구조적 연결
15. 반례·오개념·실패 사례
16. 자가 점검 문제
17. 요약 표

---

## 0. 수식 4단 병기 가이드

이 문서는 **핵심 수식**에 대해 다음 4가지 표현을 병기합니다.

- **유니코드**: 수식의 의미를 직관적으로 파악
- **LaTeX**: 수학의 정식 표기
- **Mathematica**: 기호 계산 언어
- **Python (SymPy)**: 프로그래밍 언어

이렇게 하면 LaTeX를 모르는 독자도 이해할 수 있고, Mathematica/Python 사용자는 바로 실행할 수 있습니다.

---

## 1. 부등식의 정의와 기본 형태

### 1.1 기본 형태

**유니코드**

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

좌변을 **산술평균(Arithmetic Mean, AM)**, 우변을 **기하평균(Geometric Mean, GM)**이라 부릅니다.

**등호 조건**: $x_1 = x_2 = \cdots = x_n$일 때, 오직 그때만 등호가 성립합니다.

### 1.2 n=2인 경우 (가장 널리 쓰이는 형태)

**유니코드**

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

이 부등식은 유클리드 *원론*(기원전 300년경)에 이미 암시적으로 등장합니다. 기하학적 도형과 수의 관계를 탐구하던 고대 수학자들이 직관적으로 파악하고 있었던 셈입니다.

### 1.3 가중 AM-GM (Weighted AM-GM)

**유니코드**

```text
λ₁x₁ + λ₂x₂ + ... + λₙxₙ  ≥  x₁^λ₁ · x₂^λ₂ · ... · xₙ^λₙ
(단, λᵢ ≥ 0, ∑λᵢ = 1)
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

$\lambda_i = 1/n$으로 두면 일반 AM-GM으로 환원됩니다. 가중치 합이 1이 아니면 이 부등식은 성립하지 않습니다.

### 1.4 세 가지 평균의 정의

음이 아닌 실수 $x_1, \ldots, x_n$에 대해:

- **산술평균(AM)**: $\displaystyle A = \frac{x_1 + \cdots + x_n}{n}$
- **기하평균(GM)**: $\displaystyle G = \sqrt[n]{x_1 \cdots x_n}$
- **조화평균(HM)**: $\displaystyle H = \frac{n}{\frac{1}{x_1} + \cdots + \frac{1}{x_n}}$ $(x_i > 0)$
- **제곱평균(QM)**: $\displaystyle Q = \sqrt{\frac{x_1^2 + \cdots + x_n^2}{n}}$

### 1.5 등호 조건의 의미

"등호 조건"이란 부등식이 실제로 등식이 되는 경우를 뜻합니다. AM-GM에서 등호는 모든 변수가 완전히 같을 때만 성립합니다. 이 조건은 최적화 문제에서 최적점을 알려주는 핵심 정보입니다.

---

## 2. 증명 (8가지)

### 2.1 n=2 증명 (완전제곱식 이용)

$a, b \geq 0$일 때 $(\sqrt{a}-\sqrt{b})^2 \geq 0$은 항상 참입니다. 전개하면:

```latex
a - 2\sqrt{ab} + b \geq 0 \implies a+b \geq 2\sqrt{ab} \implies \frac{a+b}{2}\geq\sqrt{ab}
```

등호는 $\sqrt a = \sqrt b$, 즉 $a=b$일 때만 성립. ■

### 2.2 코시의 전진-후진 귀납법 (Cauchy Induction)

1821년 코시가 처음 엄밀하게 증명한 방법으로, 두 단계로 이루어집니다.

**전진 단계 (2의 거듭제곱으로 확장):** $n=k$에서 성립한다고 가정하면, 이를 두 그룹으로 나누어 $n=2k$에서도 성립함을 보일 수 있습니다.

```latex
\frac{x_1+\cdots+x_k}{k}\geq\sqrt[k]{x_1\cdots x_k}, \qquad \frac{x_{k+1}+\cdots+x_{2k}}{k}\geq\sqrt[k]{x_{k+1}\cdots x_{2k}}
```

이 두 부등식의 (n=2 형태의) AM-GM을 다시 적용하면:

```latex
\frac{x_1+\cdots+x_{2k}}{2k}\geq\sqrt{\sqrt[k]{x_1\cdots x_k}\cdot\sqrt[k]{x_{k+1}\cdots x_{2k}}}=\sqrt[2k]{x_1\cdots x_{2k}}
```

이를 반복하면 $n=2,4,8,16,\ldots$ 모든 2의 거듭제곱에서 성립.

**후진 단계 (임의의 n으로 축소):** $n=k$에서 성립한다고 가정하고 $n=k-1$에서도 성립함을 보입니다. $x_1,\ldots,x_{k-1}$이 주어졌을 때 $x_k := \dfrac{x_1+\cdots+x_{k-1}}{k-1}$을 추가 항으로 넣습니다.

```latex
\frac{x_1+\cdots+x_{k-1}+x_k}{k}\geq\sqrt[k]{x_1\cdots x_{k-1}x_k}
```

좌변이 정의상 $x_k$와 같으므로 $x_k \geq \sqrt[k]{x_1\cdots x_{k-1}x_k}$. 양변을 $k$제곱하고 $x_k^{k-1}$로 나누면:

```latex
x_k^{k-1} \geq x_1\cdots x_{k-1} \implies \frac{x_1+\cdots+x_{k-1}}{k-1}\geq\sqrt[k-1]{x_1\cdots x_{k-1}}
```

전진(2의 거듭제곱까지)과 후진(임의의 n으로 축소)을 결합하면 **모든 자연수 n**에 대해 증명 완료. ■

### 2.3 젠센 부등식(Jensen's Inequality)을 이용한 증명

$\ln x$는 오목함수($\ln''(x) = -1/x^2 < 0$)이므로 젠센 부등식에 의해:

```latex
\frac{1}{n}\sum_{i=1}^n \ln x_i \leq \ln\!\left(\frac{1}{n}\sum_{i=1}^n x_i\right)
```

좌변 $= \ln\big((x_1\cdots x_n)^{1/n}\big) = \ln G$, 우변 $= \ln A$이므로:

```latex
\ln G \leq \ln A
```

$\ln$이 단조증가이므로 지수를 취하면 $G \leq A$, 즉 AM-GM 완성. **이 방법의 장점**: 가중치를 넣기만 하면 즉시 가중 AM-GM으로 일반화됩니다. ■

### 2.4 Pólya 지수법

$f(x) = e^{x-1} - x$라 하면 $f'(x) = e^{x-1} - 1$, $f'(1) = 0$, $f(1) = 0$이 유일 최솟값. 따라서 모든 실수 $x$에 대해:

```latex
x \leq e^{x-1}
```

$A = \frac{1}{n}\sum x_i$로 두고 $y_i = x_i/A$라 하면:

```latex
\frac{x_i}{A} \leq e^{x_i/A - 1}
```

모든 $i$에 대해 곱하면:

```latex
\frac{x_1\cdots x_n}{A^n} \leq \exp\!\left(\sum \frac{x_i}{A} - n\right) = e^{n-n} = 1
```

따라서 $x_1\cdots x_n \leq A^n$, 즉 $G \leq A$. ■

### 2.5 조정법 (평활법, Smoothing)

$a_1,\ldots,a_n$을 내림차순 정렬. 모두 같지 않으면 $a_1$ (최대), $a_n$ (최소)을 다음으로 교체:

```latex
M = \frac{a_1+a_n}{2}, \qquad a_1+a_n - M = M
```

산술평균은 불변. 기하평균 변화:

```latex
M \cdot M - a_1 a_n = \left(\frac{a_1+a_n}{2}\right)^2 - a_1 a_n = \frac{(a_1-a_n)^2}{4} > 0
```

즉 GM 증가. 이 조작을 유한 번 반복하면 모든 수가 $A$가 되어 AM = GM. 과정 중 GM 단조증가 → 원래 $G \leq A$. ■

### 2.6 라그랑주 승수법을 이용한 증명 (역방향)

$\sum x_i = S$(고정) 제약 하에 $\prod x_i$를 최대화. 라그랑주 함수:

```latex
L = \prod x_i + \lambda\left(\sum x_i - S\right)
```

```latex
\frac{\partial L}{\partial x_i} = \prod_{j \neq i} x_j + \lambda = 0
```

모든 $i$에 대해 성립하므로 $\prod_{j \neq i} x_j$가 일정 → $x_i = S/n$. 이 점에서 최댓값 $G = S/n = A$. 따라서 $G \leq A$. ■

### 2.7 Chrystal 귀납법

$n$에서 성립 가정, $n+1$ 증명. $a_1,\ldots,a_{n+1}$ 중 $a_{n+1}$이 최대라 하자.

```latex
\bar a_n = \frac{a_1+\cdots+a_n}{n}, \qquad A_{n+1} = \frac{a_1+\cdots+a_{n+1}}{n+1}
```

$a_{n+1} \geq A_{n+1} \geq \bar a_n$이므로:

```latex
(a_{n+1} - A_{n+1})(A_{n+1} - \bar a_n) \geq 0
```

이를 정리하면 $A_{n+1}^{n+1} \geq \bar a_n^n \cdot a_{n+1}$. 귀납 가정 $\bar a_n^n \geq a_1\cdots a_n$과 결합:

```latex
A_{n+1}^{n+1} \geq a_1\cdots a_{n+1} \implies A_{n+1} \geq \sqrt[n+1]{a_1\cdots a_{n+1}}
```

■

### 2.8 베르누이 부등식 이용

$(1+t)^n \geq 1+nt$ (베르누이, $t \geq -1$, $n \geq 1$)를 이용. $x_i > 0$일 때 $t_i = x_i/A - 1 \geq -1$이라 하면 $\sum t_i = 0$. 베르누이 부등식으로부터:

```latex
\prod \frac{x_i}{A} = \prod (1+t_i) \leq \left(1 + \frac{\sum t_i}{n}\right)^n = 1
```

따라서 $G \leq A$. ■

---

## 3. 확장된 부등식 사슬: HM ≤ GM ≤ AM ≤ QM

거듭제곱평균(Power Mean) $M_p(x) = \left(\dfrac{1}{n}\sum x_i^p\right)^{1/p}$을 정의하면:

```latex
\min(x_i) \leq \underbrace{M_{-1}}_{\text{조화평균 HM}} \leq \underbrace{M_0}_{\text{기하평균 GM}} \leq \underbrace{M_1}_{\text{산술평균 AM}} \leq \underbrace{M_2}_{\text{제곱평균 QM}} \leq \max(x_i)
```

($M_0$은 극한 $p\to0$으로 정의되며 기하평균과 일치함이 알려져 있습니다.) $p$가 커질수록 $M_p$는 단조증가합니다. AM-GM은 이 전체 사슬의 가운데 한 구간일 뿐입니다.

### 3.1 두 변수 형태

**유니코드**

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

### 3.2 HM ≤ GM 증명

$1/a, 1/b$에 AM-GM 적용:

```latex
\frac{1/a + 1/b}{2} \geq \sqrt{\frac{1}{ab}} \implies \frac{a+b}{2ab} \geq \frac{1}{\sqrt{ab}} \implies \frac{2ab}{a+b} \leq \sqrt{ab}
```

### 3.3 AM ≤ QM 증명

```latex
(a+b)^2 \leq 2(a^2+b^2) \iff 0 \leq (a-b)^2
```

### 3.4 평균 사슬의 최신 연구

가중 거듭제곱 평균과 Muirhead 부등식 사이의 관계는 최근에도 활발히 연구되고 있습니다. 특히 **가중 AM-GM이 Hölder 부등식, 가중 거듭제곱 평균 부등식과 수학적으로 동등**하다는 결과가 2018년 *Symmetry*에 발표되어, 이 세 부등식이 사실상 같은 수학적 내용을 다른 언어로 표현한 것임이 밝혀졌습니다.

---

## 4. 수치 예시

가장 단순한 확인부터 시작해 봅시다.

### 예시 1: 기본 n=2

$a=4$, $b=9$: $A=6.5$, $G=6$. 확인: $6.5 \geq 6$. ✓

### 예시 2: 등호 확인

$a=b=5$: $A=5$, $G=5$. 등호. ✓

### 예시 3: 투자 수익률 (변동성 손실)

3년 수익률: $+40\%$, $-30\%$, $+20\%$.

- 산술평균: $\bar r_A = \dfrac{40-30+20}{3}\% = 10\%$
- 기하평균: $1+\bar r_G = \sqrt[3]{1.4 \times 0.7 \times 1.2} \approx \sqrt[3]{1.176} \approx 1.0555$

$\bar r_G \approx 5.55\%$.

10만 원 경로: $10 \to 14 \to 9.8 \to 11.76$ (만 원). 3년 후 11.76만 원.

변동성 손실 $= \bar r_A - \bar r_G \approx 4.45\%$.

근사식: $\bar r_G \approx \bar r_A - \sigma^2/2$. 이 근사식의 $\sigma^2$는 **로그수익률** $\ln(1+r_i)$의 분산입니다. $\ln 1.4 \approx 0.3365$, $\ln 0.7 \approx -0.3567$, $\ln 1.2 \approx 0.1823$이고 이 세 값의 분산은 $\sigma^2 \approx 0.088$, $\sigma^2/2 \approx 4.4\%$로 실제 차이(4.45%)에 가깝게 맞습니다. (단순 수익률 자체의 분산을 쓰면 $\sigma^2 \approx 0.087$로 값이 달라지므로, 이 근사식에서는 로그수익률의 분산을 써야 함에 유의하세요.) ✓

### 예시 4: 둘레 고정 직사각형

둘레 $2(x+y)=8$ → $x+y=4$. 넓이 $\text{Area}=xy \leq \left(\dfrac{x+y}{2}\right)^2 = 4$.

등호 $x=y=2$ (정사각형). 최대 넓이 4.

### 예시 5: 표면적 고정 상자

표면적 $S=2(ab+bc+ca)=54$ → $ab+bc+ca=27$.

3변수 AM-GM:

```latex
\frac{ab+bc+ca}{3} \geq \sqrt[3]{(ab)(bc)(ca)} = \sqrt[3]{(abc)^2} = V^{2/3}
```

$9 \geq V^{2/3}$ → $V \leq 27$. 등호 $ab=bc=ca$ → $a=b=c=3$. 최대 부피 27.

### 예시 6: 양수 + 역수

$a + 1/a \geq 2$, 등호 $a=1$. $a=3$: $3 + 1/3 = 3.333 \geq 2$. ✓

### 예시 7: 3변수 체인

$a=1, b=4, c=9$:

- $G = \sqrt[3]{36} \approx 3.3019$
- $A = 14/3 \approx 4.6667$

확인: $3.3019 \leq 4.6667$. ✓

---

## 5. 기하학·최적화 응용

### 5.1 둘레 고정 직사각형의 최대 넓이

둘레 $2(x+y)=P$가 고정일 때 넓이 $A=xy$의 최댓값:

```latex
\frac{x+y}{2}\geq\sqrt{xy} \implies \frac{P/2}{2}\geq\sqrt A \implies A\leq\left(\frac{P}{4}\right)^2
```

등호는 $x=y$, 즉 **정사각형**일 때. 미분 없이 대수적으로 완결.

### 5.2 표면적 고정 상자의 최대 부피 (정육면체 증명)

가로 $a$, 세로 $b$, 높이 $c$, 표면적 $S=2(ab+bc+ca)$ 고정, 부피 $V=abc$ 최대화.

$ab, bc, ca$에 3변수 AM-GM 적용:

```latex
\frac{ab+bc+ca}{3}\geq\sqrt[3]{(ab)(bc)(ca)}=\sqrt[3]{a^2b^2c^2}=V^{2/3}
```

좌변 $=S/6$이므로:

```latex
V^{2/3}\leq\frac{S}{6} \implies V\leq\left(\frac{S}{6}\right)^{3/2}
```

등호 조건 $ab=bc=ca \Leftrightarrow a=b=c$ — 최대 부피는 **정육면체**일 때 달성.

### 5.3 미분 없는 최적화의 일반 원리

"합이 고정된 양수들의 곱의 최댓값은 모두 같을 때" — 이것이 AM-GM의 최적화 원리입니다.

**예: $\min(x + 4/x)$ for $x>0$**

**유니코드**

```text
x + 4/x  ≥  2√(x · 4/x)  =  4,   등호 x = 2
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

**예: $\max x^2(1-x)$ for $0<x<1$**

```latex
x^2(1-x) = 4 \cdot \frac{x}{2} \cdot \frac{x}{2} \cdot (1-x) \leq 4\left(\frac{\frac{x}{2}+\frac{x}{2}+(1-x)}{3}\right)^3 = 4 \cdot \frac{1}{27} = \frac{4}{27}
```

등호 $\frac{x}{2} = 1-x$ → $x=2/3$. ✓

### 5.4 원점에서 가장 가까운 점, 일반화된 최소화 문제

곡선/평면이 제1사분면(또는 제1팔분원)에서 잘라내는 최소 넓이·부피 문제들도 동일한 논리로 풀립니다.

예를 들어 평면 $\frac{x}{a} + \frac{y}{b} = 1$ $(a,b>0)$이 제1사분면에서 잘라내는 삼각형의 최소 넓이를 구하는 문제는:

```latex
\text{Area} = \frac{ab}{2}
```

에 AM-GM을 적용하거나, 제약 조건을 대입해 동일한 결론에 도달합니다. 이런 문제는 임의의 차원과 곡면 형태로 일반화된 "일반화된 AM-GM 부등식" 연구로 이어집니다.

---

## 6. 금융·투자 응용: 변동성 손실 (Volatility Drag)

$n$년간 수익률 $r_1,\ldots,r_n$, 성장 배수 $x_i = 1+r_i$.

- 산술평균 수익률: $\bar r_A = \dfrac{1}{n}\sum r_i$
- 기하평균(실제 복리) 수익률: $1+\bar r_G = \sqrt[n]{\prod x_i}$

AM-GM을 바로 적용:

```latex
\frac{\sum x_i}{n}\geq\sqrt[n]{\prod x_i} \implies 1+\bar r_A \geq 1+\bar r_G \implies \bar r_A \geq \bar r_G
```

**산술평균 수익률은 항상 기하평균(복리) 수익률보다 크거나 같다.** 등호는 변동성이 0일 때만.

정규분포 근사를 쓰면:

```latex
\bar r_G \approx \bar r_A - \frac{\sigma^2}{2}
```

여기서 $\sigma^2$는 로그수익률 $\ln(1+r_i)$의 분산이며, $\sigma^2/2$가 "변동성 손실"입니다. 실무에서는 다년간 펀드 성과를 보고할 때 산술평균을 쓰면 실제보다 항상 부풀려진 숫자가 나오며, 이 때문에 대부분의 재무설계사나 뮤추얼 펀드는 복리 성장률(CAGR, 기하평균)을 공식 지표로 사용합니다.

**수치 예:** 수익률 +40%, −30%, +20%

```latex
\bar r_A = \frac{40-30+20}{3}\% = 10\%, \qquad \bar r_G = \sqrt[3]{1.4\times0.7\times1.2}-1 \approx 5.55\%
```

$10\text{만원} \to 14\text{만원} \to 9.8\text{만원} \to 11.76\text{만원}$: 실제 연평균 성장은 5.55%이지 10%가 아닙니다.

### 6.1 핵심 부등식 4단 병기

**유니코드**

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

### 6.2 레버리지와 변동성 손실의 관계

레버리지 배수를 $k$라 하면 변동성도 대략 $k$배가 되고 드래그는 $\sigma^2$에 비례하므로 대략 $k^2$배로 커집니다. 예: 무레버리지 변동성 50%의 드래그는 $50\%^2/2=12.5\%$인데, 2배 레버리지 시 변동성이 100%가 되어 드래그가 $100\%^2/2=50\%$로 4배가 됩니다. 이는 레버리지 ETF의 장기 보유가 위험한 핵심 수학적 이유입니다.

### 6.3 AM-GM 개선의 정량적 분석

AM-GM 부등식이 "얼마나 tight한가"를 정량적으로 분석하는 연구도 있습니다. 2008년 arXiv 논문은 AM과 GM의 차이를 **분산**으로 표현하는 개선된 부등식을 제시했습니다:

분산이 크면 AM과 GM의 차이도 커지며, $n$이 클 때 "typical" upper bound가 0.82보다 작아진다는 확률적 분석도 제시되었습니다. 이는 변동성 손실의 근사식 $\bar r_G \approx \bar r_A - \sigma^2/2$가 단순한 근사를 넘어 **정량적 한계**를 가진다는 것을 시사합니다.

---
 
---
## 7. 공학·물리학 응용
 
### 7.1 최대 전력 전달 정리 — 미분 없이 유도하기
 
전기공학에서 가장 유명한 결과 중 하나가 **최대 전력 전달 정리**(내부저항 $R_s$인 전원에서 부하 $R_L$로 최대 전력을 전달하려면 $R_L=R_s$여야 한다)입니다. 보통은 미분으로 증명하지만, AM-GM으로 훨씬 짧게 끝낼 수 있습니다.
 
전압 $V$, 내부저항 $R_s$인 전원이 부하 $R_L$에 전달하는 전력은:
 
```latex
P(R_L) = \frac{V^2 R_L}{(R_s+R_L)^2}
```
 
$P$를 최대화하는 대신 $1/P$를 최소화합니다:
 
```latex
\frac{1}{P} = \frac{(R_s+R_L)^2}{V^2 R_L} = \frac{1}{V^2}\left(\frac{R_s^2}{R_L} + 2R_s + R_L\right)
```
 
우변에서 상수항 $2R_s$를 제외한 $\dfrac{R_s^2}{R_L}+R_L$에 AM-GM을 적용하면:
 
```latex
\frac{R_s^2}{R_L} + R_L \;\geq\; 2\sqrt{\frac{R_s^2}{R_L}\cdot R_L} = 2R_s
```
 
등호는 $\dfrac{R_s^2}{R_L}=R_L \iff R_L=R_s$일 때. 따라서:
 
```latex
\frac{1}{P} \geq \frac{4R_s}{V^2} \;\;\Longrightarrow\;\; P \leq \frac{V^2}{4R_s}, \qquad \text{등호 } R_L=R_s
```
 
즉 **최대 전력 전달 정리 $R_L=R_s$와 최대 전력 $P_{\max}=\dfrac{V^2}{4R_s}$가 미분 없이 한 번의 AM-GM 적용으로 동시에 나옵니다.** §13에서 다룬 "AM-GM은 미분 없는 최적화"라는 원리가 순수 물리·공학 문제에도 그대로 적용되는 예입니다.
 
### 7.2 재료 최소화 설계: 원통형 용기의 최적 비율
 
부피 $V=\pi r^2h$가 고정된 원통(뚜껑 포함)의 표면적 $S=2\pi r^2+2\pi rh$을 최소화하는 문제를 봅시다. $S$를 3개 항으로 쪼갭니다:
 
```latex
S = 2\pi r^2 + \pi rh + \pi rh
```
 
3변수 AM-GM 적용:
 
```latex
\frac{2\pi r^2+\pi rh+\pi rh}{3} \geq \sqrt[3]{(2\pi r^2)(\pi rh)(\pi rh)} = \sqrt[3]{2\pi^3r^4h^2}
```
 
$r^2h = V/\pi$이므로 $r^4h^2=(r^2h)^2=(V/\pi)^2$을 대입하면:
 
```latex
\sqrt[3]{2\pi^3\cdot\frac{V^2}{\pi^2}} = \sqrt[3]{2\pi V^2}
```
 
따라서 $S\geq 3\sqrt[3]{2\pi V^2}$. 등호 조건 $2\pi r^2=\pi rh \iff h=2r$ — **높이가 지름과 같을 때** 표면적이 최소가 됩니다. 이는 §5.2의 직육면체(정육면체) 결과와 정확히 같은 구조("등호 조건 = 가장 균형 잡힌 형태")를 원통에 그대로 옮긴 것입니다.
 
### 7.3 자원 배분: 채널·경로에 자원을 나눌 때의 최적 분배
 
$n$개의 통신 채널(또는 병렬 처리 경로)에 총 자원 $S$(대역폭, 전력 등)를 $x_1,\ldots,x_n$으로 나눠줄 때, 각 채널의 지연시간이 $1/x_i$에 비례한다고 하면 총 지연시간 $\sum 1/x_i$을 최소화하는 배분은 어떻게 될까요?
 
§3의 HM≤AM을 그대로 씁니다: $\sum x_i = S$일 때,
 
```latex
\frac{S}{n} = \frac{\sum x_i}{n} \;\geq\; \frac{n}{\sum(1/x_i)}
```
 
정리하면:
 
```latex
\sum_{i=1}^n \frac{1}{x_i} \;\geq\; \frac{n^2}{S}
```
 
등호는 $x_1=\cdots=x_n=S/n$일 때, 즉 **균등 배분이 총 지연시간을 최소화**합니다. 회로의 병렬저항 배분, 네트워크 대역폭 분배, 캐시 용량 분배 등 "합이 고정된 자원을 나누어 역수의 합을 줄이는" 형태의 문제는 모두 이 한 줄로 해결됩니다.
 
---
 
## 8. 컴퓨터과학·현대 최적화 이론 응용
 
### 8.1 SAGE 인증서 (Sums of AM/GM Exponentials)
 
다항식이나 지수함수합 $f(x)=\sum_\alpha c_\alpha e^{\langle\alpha,x\rangle}$이 모든 $x$에서 0 이상임을 증명하는 문제는 일반적으로 어렵지만, 가중 AM-GM으로 항을 묶을 수 있으면 효율적으로 증명할 수 있습니다.
 
서포트 점 $\alpha_0,\ldots,\alpha_m$과 가중치 $\lambda_i\geq0$, $\sum\lambda_i=1$, $\sum\lambda_i\alpha_i=\alpha_0$가 있을 때:
 
**유니코드**
 
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
 
이는 가중 AM-GM에서 직접 도출됩니다. 이런 "AM/GM 인증서"들의 집합을 **SAGE**라 부르며, 볼록 최적화의 **상대 엔트로피 프로그래밍(relative entropy programming)**과 연결되어 실제 다항식 최적화 소프트웨어에 구현되어 있습니다.
 
최근 연구는 SAGE 인증서에 **대칭성(symmetry)**을 도입했습니다. 문제가 군 $G$의 작용에 대해 불변일 때, 대칭성에 적응된 분해 정리를 통해 **상대 엔트로피 프로그램의 크기를 줄일 수 있다**는 것이 2021년 arXiv 논문에서 체계적으로 연구되었습니다.
 
또한 Moustrou, Riener, Theobald, Verdure의 연구("Symmetric SAGE and SONC forms, exactness and quantitative gaps", arXiv:2312.10500, *Journal of Symbolic Computation* 게재)는 **대칭 SAGE와 SONC 형식**의 관계를 분석하고, 여러 대칭적 경우에서 SAGE 또는 SONC 속성이 비음수성(nonnegativity)과 일치함을 보였습니다.
 
### 8.2 비가환 AM-GM과 확률적 경사하강법 (SGD)
 
AM-GM 부등식은 **행렬**로 일반화될 수 있습니다. Recht와 Ré (2012)는 기계학습의 **확률적 경사하강법(SGD)**에서 with-replacement 샘플링보다 without-replacement 샘플링(shuffling)이 더 빠르게 수렴함을 증명하기 위해, $n$개의 양의 정부호 행렬에 대한 비가환 AM-GM 추측을 제안했습니다. 이들은 $m=n=2$인 경우와 여러 무작위 행렬 클래스에서(기댓값 의미로) 이 추측을 직접 증명했고, 이후 Zhang(2018)이 $m=3$, 임의의 $n$인 경우로 확장했습니다.
 
이 추측이 일반적으로는 거짓임은 Lai와 Lim(2020)이 보였습니다. 이들은 비가환 Positivstellensatz를 이용해 추측을 준정부호계획법(SDP) 문제로 바꾸고, **$m=n=5$인 구체적인 경우에 반례**가 존재함을 수치적으로 확인했습니다. 즉 "5개 이상의 행렬이면 무조건 깨진다"는 것이 아니라, 추측에 등장하는 두 파라미터 $m, n$이 모두 5에 이르렀을 때 처음으로 반례가 발견된 것이며, $m=2,3$처럼 작은 $m$에 대해서는 임의의 $n$에서도 부등식이 성립합니다. $m=4$인 경우는 여전히 미해결로 남아 있습니다.
 
이 연결은 AM-GM이 순수 수학을 넘어 **현대 기계학습 이론**의 핵심 도구로 쓰이고 있음을 보여줍니다.
 
### 8.3 알고리즘 분석에서의 활용
 
분할정복 알고리즘의 균형 잡힌 분할(balanced partition)을 논증할 때, 또는 자원 사용량의 평균적 상한을 구할 때 AM-GM류의 논증이 등장합니다. 예를 들어, 크기 $n$인 문제를 크기 $n/2$인 두 부분문제로 나누는 분할정복 알고리즘의 시간 복잡도 $T(n) = 2T(n/2) + O(n)$을 분석할 때, 각 단계의 자원 사용량을 AM-GM으로 상한 지어 균형 잡힌 분할이 최적임을 보일 수 있습니다.
 
---
 
## 9. 경제학 응용
 
### 9.1 콥-더글라스 생산함수의 비용 최소화 — 가중 AM-GM으로 라그랑주 없이 풀기
 
생산함수 $Y = A\,L^\alpha K^{1-\alpha}$ ($0<\alpha<1$, 노동 $L$·자본 $K$)가 있고, 노동 단가 $w$, 자본 단가 $r$일 때 목표 생산량 $Y_0$를 달성하는 최소 비용 $C=wL+rK$를 구하는 문제는 보통 라그랑주 승수법으로 풉니다. 이를 §1.3의 **가중 AM-GM**으로 직접 풀어보겠습니다.
 
가중 AM-GM($\lambda_1+\lambda_2=1$일 때 $\lambda_1y_1+\lambda_2y_2\geq y_1^{\lambda_1}y_2^{\lambda_2}$)에서 $\lambda_1=\alpha$, $\lambda_2=1-\alpha$, $y_1=\dfrac{wL}{\alpha}$, $y_2=\dfrac{rK}{1-\alpha}$로 두면:
 
```latex
\alpha\cdot\frac{wL}{\alpha} + (1-\alpha)\cdot\frac{rK}{1-\alpha} \;\geq\; \left(\frac{wL}{\alpha}\right)^{\alpha}\left(\frac{rK}{1-\alpha}\right)^{1-\alpha}
```
 
좌변은 정확히 $wL+rK=C$(총 비용)입니다. 우변을 정리하면:
 
```latex
C \;\geq\; \left(\frac{w}{\alpha}\right)^{\alpha}\left(\frac{r}{1-\alpha}\right)^{1-\alpha}\cdot L^\alpha K^{1-\alpha}
```
 
생산 제약 $Y_0=A\,L^\alpha K^{1-\alpha}$, 즉 $L^\alpha K^{1-\alpha}=Y_0/A$를 대입하면:
 
```latex
C \;\geq\; \frac{Y_0}{A}\left(\frac{w}{\alpha}\right)^{\alpha}\left(\frac{r}{1-\alpha}\right)^{1-\alpha}
```
 
등호 조건은 가중 AM-GM의 등호 조건인 $y_1=y_2$, 즉:
 
```latex
\frac{wL}{\alpha} = \frac{rK}{1-\alpha} \;\;\Longrightarrow\;\; \frac{K}{L} = \frac{(1-\alpha)\,w}{\alpha\,r}
```
 
이것이 바로 교과서에서 라그랑주 승수법(또는 한계기술대체율 $MRTS=w/r$ 조건)으로 유도하는 **콥-더글라스 비용 최소화의 최적 자본-노동 비율**과 정확히 일치합니다. §13에서 확인한 "AM-GM은 변수 개수가 늘어나도 증명이 길어지지 않는다"는 이점이, 여기서는 "미분 없이 최적 요소 배분 비율을 직접 읽어낸다"는 형태로 경제학에 그대로 적용된 것입니다.
 
### 9.2 등호 조건의 경제학적 해석
 
9.1절의 등호 조건 $K/L=\dfrac{(1-\alpha)w}{\alpha r}$은, **각 생산요소에 지출한 금액당 한계생산이 요소 간에 균등해지는 지점**을 의미합니다(즉 $\alpha$-가중 지출 $wL/\alpha$와 $(1-\alpha)$-가중 지출 $rK/(1-\alpha)$이 같아지는 지점). 이는 §1.5에서 강조한 "등호 조건 = 균형점"이라는 해석이, 경제학에서는 구체적으로 "자원의 효율적 배분(생산요소 간 한계생산 균등화)"으로 나타난다는 것을 보여줍니다.
 
---
 
## 10. 순수 수학·경시대회에서의 위상
 
AM-GM은 대수 부등식 중 가장 널리 쓰이는 도구로, 입문·중급·올림피아드 수준 문제 전반에 등장합니다. 직접 적용이 안 될 때는 항을 창의적으로 쪼개거나, 다른 부등식과 결합해 접근합니다. 두 가지 대표적인 기법을 직접 풀어보겠습니다.
 
### 10.1 기법 1 — 항 쪼개기 (Splitting)
 
**문제**: $a,b,c>0$일 때 $a^4+a^4+b^4+c^4 \geq 4a^2bc$를 증명하시오.
 
**풀이**: 4개 항에 바로 AM-GM을 적용합니다.
 
```latex
\frac{a^4+a^4+b^4+c^4}{4} \geq \sqrt[4]{a^4\cdot a^4\cdot b^4\cdot c^4} = \sqrt[4]{a^8b^4c^4} = a^2bc
```
 
양변에 4를 곱하면 $a^4+a^4+b^4+c^4\geq4a^2bc$. 등호는 $a=b=c$일 때. ■
 
여기서 핵심은 **좌변에 굳이 $a^4$을 두 번 넣은 것**입니다. 우변의 $a^2bc$가 나오려면 지수를 $4:4:4:4$로 맞춰 4제곱근을 취했을 때 $a^2$가 나와야 하는데, $a^4$을 한 번만 쓰면 $a^{4/4}\cdot(bc)^{4/4}\cdot\text{(빈 자리)}$처럼 항 개수가 안 맞습니다. "목표 우변의 지수 비율에 맞춰 좌변 항의 개수를 인위적으로 늘리는 것"이 AM-GM 경시대회 문제의 가장 흔한 트릭입니다.
 
### 10.2 기법 2 — 짝짓기 (Pairing)로 순환 부등식 깨기
 
**문제**: $x,y,z>0$일 때 $\dfrac{x^2}{y}+\dfrac{y^2}{z}+\dfrac{z^2}{x} \geq x+y+z$를 증명하시오.
 
이 부등식은 세 항이 $x\to y\to z\to x$로 순환하는 구조라 한 번에 AM-GM을 적용하기 어렵습니다. 대신 **각 항을 분모의 변수와 짝지어** 2변수 AM-GM을 세 번 적용합니다.
 
```latex
\frac{x^2}{y}+y \geq 2\sqrt{\frac{x^2}{y}\cdot y} = 2x, \qquad
\frac{y^2}{z}+z \geq 2y, \qquad
\frac{z^2}{x}+x \geq 2z
```
 
세 부등식을 모두 더하면:
 
```latex
\left(\frac{x^2}{y}+\frac{y^2}{z}+\frac{z^2}{x}\right) + (x+y+z) \;\geq\; 2(x+y+z)
```
 
양변에서 $(x+y+z)$를 빼면 원하는 결과가 나옵니다:
 
```latex
\frac{x^2}{y}+\frac{y^2}{z}+\frac{z^2}{x} \;\geq\; x+y+z
```
 
등호는 $x=y=z$일 때. ■
 
이 "짝짓기" 기법은 순환 부등식(cyclic inequality)에서 가장 강력한 표준 도구이며, §12(뮤어헤드)의 T-변환이 다변수 문제를 2변수 문제로 환원했던 것과 같은 발상 — **복잡한 다변수 구조를 2변수 AM-GM의 합으로 쪼개서 해결**하는 전략입니다.
 
### 10.3 언제 다른 도구로 넘어가야 하는가
 
10.1~10.2절의 두 기법으로도 안 풀리는 경우, 그다음 표준 단계는 코시-슈바르츠 부등식(특히 Titu's Lemma, §16 문제 5 참고)이나 §12의 뮤어헤드 부등식으로 넘어가는 것입니다. 대략적인 판단 기준: 항의 지수 벡터들 사이에 majorization 관계가 보이면 뮤어헤드, 분수 형태의 합이면 코시-슈바르츠, 그 외의 경우 항 쪼개기·짝짓기를 먼저 시도하는 순서가 실전에서 효율적입니다.
 

---
 ## 11. 심화: 가우스의 산술기하평균 반복법(AGM)과 π 계산

이는 AM-GM **부등식**이 아니라 AM과 GM을 번갈아 계산하는 **반복 알고리즘**이며, AM≥GM이 이 알고리즘의 수렴성과 수렴 방향을 보장하는 핵심 원리입니다.

### 11.1 AGM 반복

$a_0=a$, $b_0=b$ ($0<b\le a$)에서 시작:

**유니코드**

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

AM≥GM에 의해 항상 $a_{n+1}\ge b_{n+1}$이고, 동시에 $b_{n+1}=\sqrt{a_nb_n}\ge b_n$(GM은 더 작은 쪽보다 커짐), $a_{n+1}\le a_n$(AM은 더 큰 쪽보다 작아짐)이 성립합니다. 즉 $a_n$은 단조감소, $b_n$은 단조증가하며 서로를 향해 조여들어(sandwich) 같은 극한값 $\text{agm}(a,b)$로 수렴합니다. 가우스는 1799년 $\text{agm}(\sqrt2,1)$이 렘니스케이트 곡선의 상수와 정확히 연결됨을 발견했고, 이것이 AGM 연구의 출발점이 되었습니다.

### 11.2 2차 수렴: 왜 이렇게 빠른가 — 직접 유도

핵심 항등식부터 유도합니다.

```latex
a_{n+1}-b_{n+1} = \frac{a_n+b_n}{2}-\sqrt{a_nb_n}
```

우변을 $\sqrt{a_n}=u$, $\sqrt{b_n}=v$로 치환하면:

```latex
\frac{u^2+v^2}{2}-uv = \frac{u^2-2uv+v^2}{2} = \frac{(u-v)^2}{2}
```

즉:

```latex
a_{n+1}-b_{n+1} = \frac{(\sqrt{a_n}-\sqrt{b_n})^2}{2}
```

여기까지가 원래 알려진 항등식입니다. 이제 오차 $\varepsilon_n := a_n-b_n$이 실제로 **제곱으로** 줄어드는지 확인해 봅시다. 분자를 유리화하면:

```latex
\sqrt{a_n}-\sqrt{b_n} = \frac{a_n-b_n}{\sqrt{a_n}+\sqrt{b_n}} = \frac{\varepsilon_n}{\sqrt{a_n}+\sqrt{b_n}}
```

이를 위 식에 대입하면:

```latex
\varepsilon_{n+1} = \frac{\varepsilon_n^{\,2}}{2\left(\sqrt{a_n}+\sqrt{b_n}\right)^2}
```

$a_n, b_n$은 모두 공통 극한 $M=\text{agm}(a,b)$로 수렴하므로, $n$이 커지면 분모는 $2(\sqrt M+\sqrt M)^2 = 8M$이라는 **양의 상수**에 가까워집니다. 따라서:

```latex
\varepsilon_{n+1} \approx \frac{\varepsilon_n^{\,2}}{8M} \qquad (n \text{이 클 때})
```

이것이 **2차 수렴(quadratic convergence)**의 정확한 의미입니다: 오차가 제곱이 되어 줄어들므로, 한 자릿수의 정확도가 $10^{-k}$면 다음 단계는 대략 $10^{-2k}$가 되어 — **매 반복마다 정확한 자릿수가 거의 두 배로 늘어납니다.** 이는 선형 수렴(오차가 매번 일정 비율로만 줄어드는 경우, 자릿수가 매번 일정하게만 증가)과 근본적으로 다른 속도이며, 이 덕분에 AGM은 20~30번의 반복만으로 수백만 자리의 정밀도에 도달할 수 있습니다.

### 11.3 가우스-르장드르(Brent-Salamin) 알고리즘: π 계산에 직접 적용

완전 타원적분

```latex
I(a,b)=\int_0^\infty \frac{dx}{\sqrt{(x^2+a^2)(x^2+b^2)}} = \frac{\pi}{2\,\text{agm}(a,b)}
```

를 이용하면 AGM으로 π를 계산할 수 있습니다. 1976년 브렌트(Brent)와 살라민(Salamin)이 독립적으로 정리한 실행 가능한 알고리즘은 다음과 같습니다.

**초기값**: $a_0=1$, $b_0=\dfrac{1}{\sqrt2}$, $t_0=\dfrac14$, $p_0=1$

**반복 ($n=0,1,2,\ldots$)**:

```latex
a_{n+1}=\frac{a_n+b_n}{2}, \qquad
b_{n+1}=\sqrt{a_nb_n}, \qquad
t_{n+1}=t_n-p_n(a_n-a_{n+1})^2, \qquad
p_{n+1}=2p_n
```

**근사값**:

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

print(pi_brent_salamin(4))   # 3.14159265358979... (4번만 반복해도 소수점 수십 자리 정확)
```

11.2절의 2차 수렴 결과 덕분에, 이 알고리즘은 단 4~5회 반복만으로 소수점 20~30자리 이상의 정확도를 얻습니다. 이후 빠른 곱셈 알고리즘(FFT 기반)과 결합한 **가우스-르장드르 알고리즘**은 수천만 자리 이상의 π 계산 기록에 실제로 쓰인 알고리즘 계열의 근간입니다.

### 11.4 AGM 반복의 성능 최적화 (Ooura, 1998)

Brent-Salamin 알고리즘의 각 단계는 덧셈·나눗셈 외에 **제곱근 계산**(뉴턴 반복 시 내부적으로 여러 번의 곱셈 필요)을 요구합니다. 오우라(T. Ooura)는 이 제곱근 계산 비용을 줄인 수정 버전을 제시했습니다. 핵심 아이디어는 다음과 같습니다.

일반적으로 $\sqrt{x}$를 구할 때는 뉴턴 반복으로 $1/\sqrt{x}$를 먼저 구한 뒤 $x$를 곱합니다:

```latex
y_{k+1} = y_k\cdot\frac{3-x\,y_k^2}{2} \qquad (\text{나눗셈 없이 } 1/\sqrt{x}\text{에 수렴})
```

AGM 반복에서는 매 단계마다 $b_{n+1}=\sqrt{a_nb_n}$을 구해야 하므로, 순진하게 구현하면 단계마다 독립적인 뉴턴 반복(그리고 그 안의 곱셈들)을 새로 돌려야 합니다. Ooura의 개선은 이 제곱근 계산에 필요한 뉴턴 반복을 AGM의 평균 계산과 **동시에(simultaneously)** 진행하도록 재배열하여, 두 계산에서 공통으로 쓰이는 중간 곱셈 결과를 재사용하는 것입니다. 이렇게 하면 반복당 필요한 전체 곱셈 횟수가 원래 대비 절반 수준으로 줄어듭니다. 실제 공개된 수정 버전은 다음과 같은 형태입니다(초기화 후 반복):

```text
c = √0.125;  a = 1 + 3c;  b = √a;  e = b - 0.625
b = 2b;  c = e - c;  a = a + e;  npow = 4

반복:
    npow = 2·npow
    e = (a + b)/2
    b = √(ab)
    e = e - b
    b = 2b
    c = c - e
    a = e + b
(e가 목표 정밀도 이하가 될 때까지)

e = e²/4
a = a + b
π ≈ (a² - e - e/2) / (a·c - e) / npow
```

같은 원리(제곱근 계산 비용의 재배치)를 확장한 **4차 수렴 알고리즘**도 도출되어 있어, 대규모 π 계산에서 실질적인 속도 향상으로 이어집니다.

### 11.5 수치 예: 수렴 속도 직접 확인

$a_0=1$, $b_0=2$로 시작해 오차 $\varepsilon_n=a_n-b_n$이 실제로 제곱으로 줄어드는지 추적해 봅시다.

| $n$ | $a_n$ | $b_n$ | $\varepsilon_n = a_n-b_n$ |
|---|---|---|---|
| 0 | 1 | 2 | $1$ |
| 1 | $1.5$ | $\sqrt2\approx1.41421$ | $\approx0.08579$ |
| 2 | $\approx1.45711$ | $\approx1.45648$ | $\approx0.00062$ |
| 3 | $\approx1.456792$ | $\approx1.456792$ | $\approx3.3\times10^{-8}$ |

$\varepsilon_1\approx0.086 \to \varepsilon_2\approx6.2\times10^{-4}$: 대략 $(0.086)^2/(8\times1.46)\approx6.3\times10^{-4}$로 11.2절의 근사식과 정확히 들어맞습니다. $\varepsilon_2\to\varepsilon_3$ 단계에서는 오차가 $6.2\times10^{-4}$에서 $3.3\times10^{-8}$로, 정확히 자릿수가 두 배 가까이 늘어나는 것을 확인할 수 있습니다.

---

## 12. 심화: 뮤어헤드 부등식(Muirhead's Inequality)으로의 일반화

### 12.1 majorization의 정의

수열 $a=(a_1,\ldots,a_n)$, $b=(b_1,\ldots,b_n)$을 내림차순 정렬했다고 하자($a_1\geq\cdots\geq a_n$, $b_1\geq\cdots\geq b_n$). $a$가 $b$를 **majorize**한다($a \succ b$)는 것은:

```latex
\sum_{i=1}^k a_i \geq \sum_{i=1}^k b_i \quad (k=1,\ldots,n-1), \qquad \sum_{i=1}^n a_i = \sum_{i=1}^n b_i
```

즉 "부분합은 항상 $a$가 크거나 같지만, 전체 합은 같다." 직관적으로 $a$가 $b$보다 **덜 고르게 분포**되어 있다는 뜻입니다.

**예**: $(3,0,0) \succ (2,1,0) \succ (1,1,1)$. 총합은 모두 3이지만, 왼쪽으로 갈수록 한쪽으로 쏠려 있습니다.

### 12.2 뮤어헤드 부등식의 진술

$x_1,\ldots,x_n \geq 0$이고 $a \succ b$이면, 대칭합(symmetric sum, 모든 순열에 대한 합)에 대해:

```latex
\sum_{\sigma\in S_n} x_{\sigma(1)}^{a_1}\cdots x_{\sigma(n)}^{a_n} \;\geq\; \sum_{\sigma\in S_n} x_{\sigma(1)}^{b_1}\cdots x_{\sigma(n)}^{b_n}
```

### 12.3 AM-GM이 뮤어헤드의 특수 사례임을 직접 확인

AM-GM ($\frac{x_1+\cdots+x_n}{n}\geq \sqrt[n]{x_1\cdots x_n}$)을 뮤어헤드 형태로 다시 써봅시다.

- $a = (1,0,\ldots,0)$, $b = (\tfrac1n,\ldots,\tfrac1n)$

**$a \succ b$인지 확인**: 부분합 조건은 $\sum_{i=1}^k a_i = 1$ ($k\geq1$인 모든 $k$), $\sum_{i=1}^k b_i = k/n$. $k<n$이면 $1 \geq k/n$이 항상 성립합니다. 전체 합은 둘 다 1로 같습니다. 따라서 $a \succ b$.

**양변의 대칭합 계산**:

- $a$쪽: $\sum_\sigma x_{\sigma(1)}^1x_{\sigma(2)}^0\cdots x_{\sigma(n)}^0$. 지수 1을 받는 변수가 어느 것이냐만 결과에 영향을 주고($n$가지), 나머지 $(n-1)!$개의 순열은 값이 동일하므로 합은 $(n-1)!\sum_i x_i$.
- $b$쪽: 모든 지수가 $1/n$으로 같으므로 어떤 순열이든 값이 $(x_1\cdots x_n)^{1/n}$로 동일. 순열은 $n!$개이므로 합은 $n!\,(x_1\cdots x_n)^{1/n}$.

뮤어헤드 부등식을 대입하면:

```latex
(n-1)!\sum_i x_i \;\geq\; n!\,(x_1\cdots x_n)^{1/n}
```

양변을 $(n-1)!\cdot n$으로 나누면:

```latex
\frac{1}{n}\sum_i x_i \;\geq\; (x_1\cdots x_n)^{1/n}
```

바로 AM-GM입니다. 즉 뮤어헤드는 "말로만 일반화"가 아니라, 지수 벡터 $(1,0,\ldots,0)$이 $(\tfrac1n,\ldots,\tfrac1n)$을 majorize한다는 사실 **하나**로부터 AM-GM 전체를 재도출할 수 있다는 뜻입니다.

### 12.4 뮤어헤드의 증명 스케치: 인접전치와 2변수 AM-GM으로의 환원

뮤어헤드는 다음 보조정리로 증명됩니다.

**보조정리 (인접전치 감소, T-변환)**: $a \succ b$이고 $a\neq b$이면, $a$에서 시작해 **성분 두 개만 바꾸는** 유한한 조작을 거쳐 $b$에 도달할 수 있습니다. 각 조작(T-변환)은 $a_i > a_j$인 두 성분을 $a_i' = a_i-t$, $a_j'=a_j+t$ ($t>0$, $a_i'\geq a_j'$)로 바꾸는 것입니다.

**핵심 부등식**: 하나의 T-변환 전후로 대칭합이 어떻게 바뀌는지는, 두 변수 $x,y$에 대한 부등식 하나로 환원됩니다.

```latex
x^{a_i}y^{a_j} + x^{a_j}y^{a_i} \;\geq\; x^{a_i'}y^{a_j'} + x^{a_j'}y^{a_i'}
```

좌변에서 우변을 빼면:

```latex
x^{a_i}y^{a_j}+x^{a_j}y^{a_i}-x^{a_i'}y^{a_j'}-x^{a_j'}y^{a_i'} = \left(x^{a_i'}-x^{a_j'}\right)\left(y^{a_j'}-y^{a_i'}\right)
```

$a_i'\ge a_j'$이므로 $x>0$일 때 $x^{a_i'}-x^{a_j'}$와 $y$에 대한 대응 인수의 부호가 항상 일치하여(둘 다 $x\gtrless y$ 여부에 따라 같은 방향), 곱은 항상 0 이상입니다. 즉 **뮤어헤드 전체가 결국 2변수짜리 부등식의 연쇄**로 분해됩니다 — 코시의 전진-후진 귀납법이 AM-GM을 2변수 경우로 환원했던 것과 정확히 같은 구조입니다.

### 12.5 예: Muirhead 응용 (완전한 풀이)

**문제**: $x,y>0$일 때 $x^2y^3 + x^3y^2 \leq xy^4 + x^4y$를 증명하시오.

**풀이**: 좌변 지수 벡터를 내림차순 정렬하면 $(3,2)$, 우변은 $(4,1)$입니다. $(4,1) \succ (3,2)$인지 확인: 부분합 $4 \geq 3$ ✓, 전체합 $5=5$ ✓. 따라서 뮤어헤드에 의해 곧바로

```latex
\sum_\sigma x^{4}y^{1} \;\geq\; \sum_\sigma x^{3}y^{2} \quad\Longleftrightarrow\quad x^4y+xy^4 \;\geq\; x^3y^2+x^2y^3
```

이 성립합니다. (2변수라 대칭합은 항이 2개뿐이므로, majorize 관계만 확인하면 증명이 즉시 끝납니다.) 등호는 $x=y$일 때. ■

### 12.6 뮤어헤드의 한계

뮤어헤드는 **강력하지만 majorization 관계가 존재할 때만** 쓸 수 있습니다. 지수 벡터 사이에 majorization이 성립하지 않으면(두 벡터가 비교 불가능하면) 뮤어헤드로는 아무것도 말할 수 없습니다. 3변수 이상에서는 majorize 관계가 존재하지 않는 지수쌍이 흔히 나오며, 이때는 Schur-convex 함수, SOS(sum-of-squares) 분해 등 다른 도구가 필요합니다.

### 12.7 SAGE·SONC와의 연결

Moustrou, Riener, Theobald, Verdure의 연구(arXiv:2312.10500, *Journal of Symbolic Computation* 게재)는 SAGE·SONC 인증서(§8.1 참고 — 이 역시 가중 AM-GM에서 직접 도출되는 비음성 증명 도구입니다)와 대칭성이 결합될 때, 여러 대칭적인 경우에서 SAGE 또는 SONC 속성이 곧 비음수성(nonnegativity)과 일치함을 보였습니다. §8.1의 SAGE와 본 절의 뮤어헤드는 둘 다 "가중 AM-GM(≡ majorization의 특수 사례)을 항 단위로 적용해 비음성을 증명한다"는 같은 뿌리에서 나온 도구라는 점에서 자연스럽게 연결됩니다.

---

## 13. 심화: 라그랑주 승수법과의 비교

### 13.1 §5.2 문제를 라그랑주 승수법으로 풀기

§5.2의 상자 부피 문제(표면적 $S=2(ab+bc+ca)$ 고정, 부피 $V=abc$ 최대화)를 라그랑주 승수법으로 풀면:

```latex
\nabla V = \lambda \nabla g \implies (bc,\,ac,\,ab) = \lambda(2b+2c,\,2a+2c,\,2a+2b)
```

이 연립방정식을 풀어 $a=b=c$를 유도해야 하며, 미분과 방정식 풀이가 필요합니다. 첫 두 식을 나누면:

```latex
\frac{bc}{ac} = \frac{2b+2c}{2a+2c} \implies \frac{b}{a} = \frac{b+c}{a+c} \implies b(a+c) = a(b+c) \implies bc = ac \implies a = b
```

마찬가지로 $b=c$를 얻어 $a=b=c$에 도달합니다.

반면 §5.2의 AM-GM 풀이는 **대수적 부등식 하나**로 최댓값과 등호 조건(최적점)을 동시에 얻습니다 — "미분 없는 최적화"의 대표 사례입니다.

### 13.2 변수 개수가 늘어날 때: 두 방법의 확장성 비교

두 방법의 실질적 차이는 **변수가 많아질 때** 뚜렷해집니다. 다음 문제를 봅시다.

**문제**: $x_1,\ldots,x_n>0$, $x_1x_2\cdots x_n=1$일 때 $x_1+x_2+\cdots+x_n$의 최솟값을 구하시오.

**AM-GM으로 (변수 개수와 무관하게 한 줄)**:

```latex
\frac{x_1+\cdots+x_n}{n}\geq\sqrt[n]{x_1\cdots x_n}=\sqrt[n]{1}=1 \implies x_1+\cdots+x_n\geq n
```

등호는 $x_1=\cdots=x_n=1$일 때. $n$이 2든 100이든 풀이 과정이 **완전히 동일**합니다.

**라그랑주 승수법으로 (변수 개수만큼 방정식이 늘어남)**:

```latex
L = \sum_i x_i + \lambda\left(\prod_i x_i - 1\right), \qquad \frac{\partial L}{\partial x_i} = 1+\lambda\prod_{j\neq i}x_j=0 \quad (i=1,\ldots,n)
```

$n$개의 방정식이 나오며, $\prod_{j\neq i}x_j = -1/\lambda$가 **모든 $i$에 대해 같은 값**이어야 합니다. 이로부터 $\prod_{j\neq i}x_j$가 $i$에 무관하다는 것을 보이려면, 임의의 두 인덱스 $i,k$에 대해 $\prod_{j\neq i}x_j=\prod_{j\neq k}x_j$를 정리해 $x_k=x_i$를 이끌어내는 대칭성 논증이 필요합니다. 그 후 제약식에 $x_i=c$(상수)를 대입해 $c^n=1\Rightarrow c=1$을 얻어야 최솟값 $n$에 도달합니다.

즉 라그랑주 방법은 $n$이 커질수록 **연립방정식의 개수와 대칭성 논증의 복잡도가 함께 증가**하는 반면, AM-GM은 변수 개수에 관계없이 한 줄의 부등식으로 끝납니다. 이것이 "AM-GM이 미분 없는 최적화의 대표 사례"라는 말의 실질적인 의미입니다 — 단지 미분을 안 쓴다는 것이 아니라, **차원이 늘어나도 증명의 길이가 늘어나지 않는다**는 확장성의 이점입니다.

### 13.3 라그랑주가 유리한 경우

반대로 목적함수나 제약이 AM-GM으로 깔끔하게 정리되지 않는 형태(예: 이차형식, 비다항식 함수, 부등식 제약이 많아 KKT 조건 전체를 다뤄야 하는 경우)라면 라그랑주(혹은 KKT) 방법이 유일한 선택지입니다. AM-GM은 "합이 고정될 때 곱을 최대화" 또는 그 역(곱이 고정될 때 합을 최소화) 구조의 문제에 특화된 도구이며, 그 구조를 벗어나면 적용할 수 없습니다.

---

## 14. 심화: 정보이론과의 구조적 연결

### 14.1 왜 AM-GM과 KL divergence가 "같은 증명"인가 — 직접 대응시키기

깁스 부등식(엔트로피의 비음성, $D_{KL}(p\|q)\geq 0$)과 AM-GM의 젠센 증명(§2.3)을 나란히 놓고 한 줄씩 대응시켜 보겠습니다.

| 단계 | AM-GM (§2.3) | KL divergence |
|---|---|---|
| 오목함수 선택 | $f(x) = \ln x$ | $f(x) = \ln x$ (동일) |
| 젠센 적용 대상 | $n$개의 균등가중 값 $x_1,\ldots,x_n$ | 확률 $p_i$로 가중된 값 $q_i/p_i$ |
| 젠센 부등식 | $\dfrac1n\sum \ln x_i \leq \ln\!\Big(\dfrac1n\sum x_i\Big)$ | $\displaystyle\sum_i p_i \ln\frac{q_i}{p_i} \leq \ln\!\Big(\sum_i p_i\frac{q_i}{p_i}\Big)$ |
| 우변 정리 | $\ln\big(\tfrac1n\sum x_i\big) = \ln A$ | $\ln\big(\sum_i q_i\big) = \ln 1 = 0$ |
| 결론 | $\ln G \leq \ln A \Rightarrow G\leq A$ | $\sum p_i\ln\frac{q_i}{p_i}\leq0 \Rightarrow D_{KL}(p\|q)\geq0$ |

**직접 유도**: 젠센 부등식(오목함수 $\ln$, 가중치 $p_i$)을 $y_i = q_i/p_i$에 적용하면

```latex
\sum_i p_i \ln\frac{q_i}{p_i} \;\leq\; \ln\!\left(\sum_i p_i\cdot\frac{q_i}{p_i}\right) = \ln\!\left(\sum_i q_i\right) = \ln 1 = 0
```

양변에 $-1$을 곱하면 바로 $D_{KL}(p\|q) = \sum_i p_i\ln\dfrac{p_i}{q_i} \geq 0$이 나옵니다. 등호 조건도 그대로 대응됩니다: AM-GM의 등호가 "모든 $x_i$가 같을 때"이듯, KL divergence의 등호는 "모든 $i$에 대해 $q_i/p_i$가 같을 때" — 즉 $q_i=p_i$(두 확률분포가 같을 때)입니다.

**한 걸음 더 — 가중 AM-GM과 완전히 같은 식임을 확인**: 이 논증은 사실 가중 AM-GM 그 자체입니다. 가중 AM-GM $\sum \lambda_i x_i \geq \prod x_i^{\lambda_i}$에서 $\lambda_i = p_i$, $x_i = q_i/p_i$로 두면:

```latex
\sum_i p_i \cdot \frac{q_i}{p_i} \;\geq\; \prod_i \left(\frac{q_i}{p_i}\right)^{p_i} \;\;\Longrightarrow\;\; 1 \;\geq\; \prod_i \left(\frac{q_i}{p_i}\right)^{p_i}
```

양변에 로그를 취하면 $0 \geq \sum_i p_i \ln(q_i/p_i)$, 즉 위와 정확히 같은 결론입니다. **가중 AM-GM ⟺ 젠센(로그) ⟺ 깁스 부등식**, 이 셋은 문자 그대로 같은 한 줄의 부등식을 세 가지 언어로 표현한 것입니다.

### 14.2 수치 예시로 확인

$p=(0.5,0.5)$, $q=(0.9,0.1)$일 때:

```latex
D_{KL}(p\|q) = 0.5\ln\frac{0.5}{0.9} + 0.5\ln\frac{0.5}{0.1} = 0.5\ln(0.5556) + 0.5\ln(5) \approx 0.5(-0.5878)+0.5(1.6094) \approx 0.5108
```

양수임을 직접 확인할 수 있습니다. 반면 $q=p=(0.5,0.5)$면 $D_{KL}=0$ — AM-GM의 등호 조건($x_i$가 모두 같음, 여기선 $q_i/p_i$가 모두 1)과 정확히 일치합니다.

### 14.3 왜 이 대응이 유용한가

이 대응 관계는 단순한 우연이 아니라, **"오목함수 + 젠센 부등식"이라는 하나의 템플릿**이 서로 무관해 보이는 두 분야(대수적 부등식, 정보이론)에서 동일하게 작동한다는 것을 보여줍니다. 같은 템플릿에 $f(x)=\ln x$ 대신 다른 오목함수를 넣으면 Rényi 엔트로피, $f$-divergence 등 다른 정보량 불평등도 같은 방식으로 유도됩니다 — 즉 AM-GM은 이 템플릿의 가장 단순한 사례($p_i \equiv 1/n$인 균등분포 경우)로 볼 수 있습니다.

### 14.4 최신 연구와의 연결

Yeung의 연구("Inequalities Revisited", arXiv:2503.03766)는 섀넌 엔트로피 부등식을 다루면서 발전해 온 형식적 방법론(비-섀넌형 부등식을 발견하는 데 쓰인 기하학적 틀)을, AM-GM·마르코프 부등식·코시-슈바르츠 부등식과 같은 정보이론 바깥의 고전 부등식에 적용할 수 있음을 보였습니다. 14.1~14.3절에서 직접 확인한 "AM-GM과 KL divergence가 같은 증명 골격을 공유한다"는 사실은, 이런 형식적 방법론이 왜 분야를 넘어 통할 수 있는지를 보여주는 구체적인 사례이기도 합니다.

---

## 15. 반례·오개념·실패 사례

AM-GM을 쓸 때 자주 빠지는 함정들을 정리해 봅시다.

### 15.1 음수가 있으면 성립하지 않음

$a=-1, b=-4$: $A=-2.5$, $G=\sqrt{(-1)(-4)}=2$. $A<G$. AM-GM은 음이 아닌 실수에서만 성립합니다.

### 15.2 등호 조건 무시

$a=1, b=4$: $A=2.5$, $G=2$. $A>G$. 등호가 아님. 최적화에서 등호 조건을 확인하지 않으면 최적점을 놓칩니다.

### 15.3 "항상 산술평균이 크다"는 오해

기하평균이 정의되지 않는 경우(음수 포함)에는 비교 불가. 또한 $n=1$일 때는 자명하게 같습니다.

### 15.4 "AM-GM이 모든 부등식을 준다"는 오해

AM-GM은 강력하지만 한계가 있습니다. 예: $\sum x_i^2 \geq \sum x_i x_{i+1}$ 같은 부등식은 AM-GM으로 직접 안 됩니다. Cauchy-Schwarz, Jensen, Muirhead 등 다른 도구가 필요합니다.

### 15.5 "가중치 합이 1이 아니어도 된다"는 오해

가중 AM-GM에서 $\sum \lambda_i = 1$은 필수입니다. 그렇지 않으면 부등식이 성립하지 않습니다.

### 15.6 실패한 접근의 교훈

- **변수 치환 없이 바로 적용**: $x^2+y^2 \geq 2xy$는 AM-GM. 하지만 $x^3+y^3 \geq 2xy\sqrt{xy}$ 같은 변형은 별도 유도 필요.
- **등호 조건 확인 생략**: 최적화 문제에서 "최댓값"을 구했지만 등호 조건이 정의역 밖이면 최댓값이 아님.
- **가중치 정규화 누락**: 가중 AM-GM에서 $\sum \lambda_i = 1$을 확인하지 않으면 잘못된 결론.

---

## 16. 자가 점검 문제

### 문제 1 (기초)

$a,b>0$일 때 $\dfrac{a}{b}+\dfrac{b}{a}\geq 2$를 증명하시오.

**답**: $x=a/b$로 두면 $x+1/x \geq 2\sqrt{x \cdot 1/x} = 2$. 등호 $a=b$.

### 문제 2 (중급)

$x,y,z>0$, $x+y+z=6$일 때 $xyz$의 최댓값을 구하시오.

**답**: AM-GM: $\dfrac{x+y+z}{3} \geq \sqrt[3]{xyz}$ → $2 \geq \sqrt[3]{xyz}$ → $xyz \leq 8$. 등호 $x=y=z=2$. 최댓값 8.

### 문제 3 (중급)

$x>0$일 때 $x + \dfrac{2}{x}$의 최솟값.

**답**: $x + \dfrac{2}{x} \geq 2\sqrt{2}$. 등호 $x=\sqrt{2}$. 최솟값 $2\sqrt{2}$.

### 문제 4 (상급)

$a,b,c>0$, $abc=1$일 때 $a+b+c \geq 3$을 증명하시오.

**답**: AM-GM: $\dfrac{a+b+c}{3} \geq \sqrt[3]{abc} = 1$ → $a+b+c \geq 3$. 등호 $a=b=c=1$.

### 문제 5 (상급) — Nesbitt 부등식 완전 풀이

$\dfrac{a}{b+c}+\dfrac{b}{c+a}+\dfrac{c}{a+b}\geq \dfrac{3}{2}$ $(a,b,c>0)$를 증명하시오.

**풀이 (Titu's lemma):**

```latex
\sum \frac{a}{b+c} = \sum \frac{a^2}{a(b+c)} \geq \frac{(a+b+c)^2}{2(ab+bc+ca)}
```

$\dfrac{(a+b+c)^2}{2(ab+bc+ca)} \geq \dfrac{3}{2}$는

```latex
(a+b+c)^2 \geq 3(ab+bc+ca) \iff a^2+b^2+c^2 \geq ab+bc+ca
```

이고, 이는 $(a-b)^2+(b-c)^2+(c-a)^2 \geq 0$에서 성립. 등호 $a=b=c$. ■

### 문제 6 (심화)

AGM 반복에서 $a_0=1$, $b_0=2$일 때 $a_1,b_1,a_2,b_2$를 구하시오.

**답**: $a_1=1.5$, $b_1=\sqrt{2}\approx 1.4142$. $a_2=(1.5+1.4142)/2\approx 1.4571$, $b_2=\sqrt{1.5 \times 1.4142}\approx 1.4565$.

---
 
### 17. 요약 - 분야별 활용

**1. 기하학·최적화**
- 핵심 활용: 둘레/표면적 고정 시 최대 넓이·부피 (정사각형·정육면체)
- 등호 조건의 의미: 도형이 "가장 균형 잡힌" 형태

**2. 금융·투자**
- 핵심 활용: 산술평균 vs 기하평균 수익률, 변동성 손실
- 등호 조건의 의미: 변동성=0 (매년 동일 수익률)

**3. 공학·물리학**
- 핵심 활용: 에너지 변환 효율 상한, 자원 배분 최적화
- 등호 조건의 의미: 구성요소 간 균형 배분

**4. 컴퓨터과학**
- 핵심 활용: SAGE 인증서, 비가환 AM-GM (SGD 이론)
- 등호 조건의 의미: 항들의 균형점 / without-replacement 우위

**5. 경제학**
- 핵심 활용: 생산함수 최적화, 자원 배분
- 등호 조건의 의미: 투입 요소의 효율적 배분

**6. 경시대회·순수수학**
- 핵심 활용: 부등식 증명의 기본 도구
- 등호 조건의 의미: 변수 동일

**7. 수치해석 (심화)**
- 핵심 활용: 가우스 AGM 반복 → π 계산
- 등호 조건의 의미: 두 수열이 같은 값으로 수렴

**8. 대칭함수 이론 (심화)**
- 핵심 활용: 뮤어헤드 부등식, SAGE와의 연결
- 등호 조건의 의미: majorization 사슬의 특수점

### 17.1 핵심 요약

- **부등식**: $A \geq G$ (음이 아닌 실수)
- **등호 조건**: 모든 변수 동일
- **n=2 형태**: $(a+b)/2 \geq \sqrt{ab}$
- **가중 형태**: $\sum \lambda_i x_i \geq \prod x_i^{\lambda_i}$, $\sum \lambda_i = 1$
- **평균 사슬**: $H \leq G \leq A \leq Q$
- **최적화 원리**: 합 고정 → 곱 최대 (모두 같을 때)
- **금융 응용**: $\bar r_A \geq \bar r_G$, 드래그 $\approx \sigma^2/2$
- **정보이론**: 젠센 증명이 KL divergence와 동형
- **Muirhead**: AM-GM은 majorization의 특수 케이스
- **SAGE (최신)**: AM/GM 인증서, 상대 엔트로피 프로그래밍, 대칭성 축소
- **비가환 AM-GM**: SGD 이론과의 연결, m=n=5에서 반례 (Lai & Lim, 2020)
- **AGM 반복**: 2차 수렴, π 계산, 성능 최적화
- **반례**: 음수 포함 시 성립 안 함
- **증명 수**: 8가지 (완전제곱, 코시 귀납, 젠센, Pólya, 조정, 라그랑주, Chrystal, 베르누이) 

---

 

**References**

- Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique. Première partie. Analyse algébrique.* Paris: L'Imprimerie Royale. https://archive.org/details/coursdanalysedel00cauc

- Gauss, C. F. (1866). *Werke, Band III.* Göttingen: Königlichen Gesellschaft der Wissenschaften zu Göttingen. https://gdz.sub.uni-goettingen.de/id/PPN235993352 [Original dissertation 1799]

- Hardy, G. H., Littlewood, J. E., & Pólya, G. (1934). *Inequalities.* Cambridge: Cambridge University Press.

- Muirhead, R. F. (1903). Some methods applicable to identities and inequalities of symmetric algebraic functions of n letters. *Proceedings of the Edinburgh Mathematical Society,* 21, 144–157. https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/F222600CC0076146E369EE27C8559F78

- Pólya, G., & Szegő, G. (1925). *Aufgaben und Lehrsätze aus der Analysis.* Berlin: Julius Springer.

- Alzer, H. (1999). Some inequalities for arithmetic and geometric means. *Proceedings of the Royal Society of Edinburgh, Section A: Mathematics,* 129A(2), 221–228. https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/A08079A284DB1A10ABE840010A640887

- Moustrou, P., Riener, C., Theobald, T., & Verdure, H. (2025). Symmetric SAGE and SONC forms, exactness and quantitative gaps. *Journal of Symbolic Computation,* 127, 102374. arXiv:2312.10500. https://arxiv.org/abs/2312.10500

- Ooura, T. (1998). Improvement of the π calculation algorithm and implementation of fast multiple-precision computation. *Information Processing Society of Japan, SIG Notes,* 98-HPC-74. https://www.kurims.kyoto-u.ac.jp/~ooura/pi_fft.html

- Recht, B., & Ré, C. (2012). Toward a noncommutative arithmetic-geometric mean inequality: conjectures, case-studies, and consequences. *Proceedings of the 25th Annual Conference on Learning Theory (COLT 2012),* PMLR 23, 11.1–11.24. https://proceedings.mlr.press/v23/recht12.html [Preprint arXiv:1202.4184]

- Zhang, T. (2014). A note on the non-commutative arithmetic-geometric mean inequality. arXiv:1411.5058. https://arxiv.org/abs/1411.5058

- Lai, Z., & Lim, L.-H. (2020). Recht-Ré noncommutative arithmetic-geometric mean conjecture is false. *Proceedings of the 37th International Conference on Machine Learning (ICML),* PMLR 119, 5608–5617. https://proceedings.mlr.press/v119/lai20a.html

- Yeung, R. (2025). Inequalities revisited. arXiv:2503.03766. https://arxiv.org/abs/2503.03766

- Chen, H., Khare, A., & Sahi, S. (2025). Majorization via positivity of Jack and Macdonald polynomial differences. arXiv:2509.19649. https://arxiv.org/abs/2509.19649




---
 
**1. Cauchy, A.-L. (1821). *Cours d'analyse de l'École Royale Polytechnique*.**
해석학의 엄밀화를 완성한 교과서. 극한, 연속성, 수렴, 급수 판정법을 처음으로 엄밀하게 정의하고, 이후 모든 부등식 연구의 논리적 토대를 제공.

**2. Gauss, C. F. (1799/1866). *Werke*, Band III.**
대수학의 기본정리에 대한 최초의 엄밀한 증명을 포함. 전집 3권에는 산술-기하평균(AGM)과 타원함수에 관한 미발표 연구가 수록되어 있어 현대 부등식 이론의 역사적 기원이 됨.

**3. Hardy, G. H., Littlewood, J. E., & Pólya, G. (1934). *Inequalities*.**
부등식 분야의 표준 교과서. AM-GM, Hölder, Minkowski, Hardy 부등식 등 해석학의 핵심 부등식을 체계적으로 정리하고, 대칭화 및 majorization 기법을 정립.

**4. Muirhead, R. F. (1903). Some methods applicable to identities and inequalities...**
대칭식 부등식의 판정법인 Muirhead 부등식을 제시. 두 지수 벡터 간의 majorization 관계가 대칭합 부등식으로 이어짐을 증명하여 대칭 부등식 증명의 기본 도구가 됨.

**5. Pólya, G., & Szegő, G. (1925). *Aufgaben und Lehrsätze aus der Analysis*.**
문제 해결을 통한 해석학 교육의 고전. 부등식, 다항식의 영점 분포, 행렬식 등 다양한 주제의 심화 문제를 통해 부등식 증명 기법을 훈련시키는 원천 자료.

**6. Alzer, H. (1999). Some inequalities for arithmetic and geometric means.**
가중 산술평균과 기하평균 사이의 비율에 대한 정밀한 상·하한을 제시. 고전적인 AM-GM 부등식과 Ky Fan 부등식을 개선하는 샤프한 형태의 부등식을 제공.

**7. Moustrou, P., et al. (2024). Symmetric SAGE and SONC forms...**
다항식의 비음수성을 증명하는 SAGE/SONC 기법을 대칭 다항식에 적용. 대칭 SAGE/SONC가 모든 대칭 비음수 다항식을 표현할 수 있는지 여부와, 표현이 불가능할 때 발생하는 간극을 정량적으로 분석.

**8. Ooura, T. (1998). Improvement of the π calculation algorithm...**
원주율 π의 고속 계산 알고리즘을 개선. Gauss-Legendre 알고리즘의 수렴 속도를 높이고 FFT 기반 다배장 정밀도 연산을 구현하여 대규모 수치 계산의 효율성을 크게 향상.

**9. Recht, B., & Ré, C. (2012). Beneath the valley of the noncommutative AM-GM...**
행렬과 같은 비가환 환경에서의 산술-기하평균 부등식을 추측. 비복원 무작위 추출이 복원 추출보다 안정적이라는 관찰에서 출발하여, 행렬 곱의 기대값에 대한 부등식 형태의 추측을 제안.

**10. Zhang, T. (2018). A note on the non-commutative AM-GM inequality.**
Recht-Ré 추측에 대한 후속 분석. 작은 차원에서는 추측이 성립함을 보이고, 일반적인 경우의 성립 여부를 검토하기 위한 행렬 구성 방법을 논의.

**11. Lai, Z., & Lim, L.-H. (2020). Recht-Ré noncommutative AM-GM conjecture is false.**
Recht-Ré 추측이 일반적으로 성립하지 않음을 증명. 명시적인 행렬 반례를 구성하고 확률적 방법론을 통해 추측이 실패하는 조건을 제시하여 해당 추측을 완전히 반증.

**12. Yeung, R. (2025). Inequalities revisited.**
정보이론에서의 부등식을 재조명. Shannon 엔트로피의 기본 부등식과 지난 20년간 발견된 non-Shannon 부등식들을 통합적으로 정리하여 정보 부등식의 전체 구조를 제시.

**13. Chen, H., Khare, A., & Sahi, S. (2025). Majorization via positivity of Jack and Macdonald polynomial differences.**
Majorization 관계를 Jack 다항식과 Macdonald 다항식의 차이의 양수성으로 특징화. 대칭 다항식의 계수가 양수일 때 majorization이 성립함을 보여 Muirhead 부등식을 일반화.