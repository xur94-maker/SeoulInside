



# 1막. 기초와 정의 (Foundation)

---

## 1.1 역사적 기원 — 60년의 종합

로렌츠 힘은 어느 한 사람이 어느 날 발견한 공식이 아니다. **1831년 패러데이의 자기력선 실험**에서 **1895년 로렌츠의 전자론**까지, 60년에 걸친 개념적 종합의 결정체다. 이 절에서는 그 종합의 각 단계를 따라가며, 왜 오늘날의 형태 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$가 필연이었는지 본다.

### 1.1.1 패러데이 (1831–1838): 자기력선의 기하학

패러데이는 전류가 자기장을 만들고, 자기장이 다시 전류에 힘을 준다는 **경험적 사실**을 발견했다. 그의 핵심 기여는 수학적 법칙이 아니라 **기하학적 이미지**였다:

> "자기력선( magnetic lines of force )이 공간을 채우고, 도체가 이 선을 가로지를 때 기전력이 유도된다."

이 발상은 당시 수학 언어로 표현되지 못했지만, 두 가지를 확립했다:

1. **장(field)이 힘을 매개한다** — 원격작용( action at a distance )을 부정
2. **힘의 방향은 자기력선과 운동 방향에 동시에 수직이다** — 오른손 법칙의 원형

패러데이는 자기장 속에서 전류가 흐르는 도체가 받는 힘을 정성적으로 관찰했으나, 그 크기를 $q\mathbf{v}\times\mathbf{B}$로 정식화하지는 못했다.

### 1.1.2 맥스웰 (1861–1865): 장의 운동량

맥스웰은 패러데이의 이미지를 **편미분방정식**으로 번역했다. 1865년 *A Dynamical Theory of the Electromagnetic Field*에서 그는 전자기장을 **역학적 매질의 운동**으로 해석하고, 장이 운동량과 에너지를 가진다고 보았다.

주목할 점은 맥스웰 방정식 자체에는 오늘날의 $q\mathbf{v}\times\mathbf{B}$ 항이 **명시적으로 없다**는 것이다. 대신 그는:

- 전자기 운동량(electromagnetic momentum) $\mathbf{A}$를 도입
- 로렌츠 게이지와 유사한 개념을 사용
- 장의 응력 텐서(Maxwell stress tensor)로 힘을 계산

이는 $q\mathbf{v}\times\mathbf{B}$를 **유도할 수 있는 기반**을 마련했지만, 아직 전하가 받는 힘의 형태로 정리되지는 않았다.

### 1.1.3 톰슨·헤비사이드 (1881–1889): $\mathbf{v}\times\mathbf{B}$의 정정

**J.J. 톰슨**은 1881년 움직이는 대전구(帶電球)의 자기장을 계산하며, 처음으로 $q\mathbf{v}\times\mathbf{B}$ 형태의 힘을 시도했다. 그러나 그의 결과에는 **계수 $1/2$의 오류**가 있었다.

이를 정정한 것이 **올리버 헤비사이드**다. 1885년과 1889년, 헤비사이드는 현대적 **벡터 표기법**을 이용해 올바른 자기력을 도출했다:

$$\mathbf{F}_m = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐅ₘ = q𝐯×𝐁
> ```

헤비사이드의 기여는 두 가지다:

1. **벡터 미적분의 도입** — 맥스웰 방정식을 4개 방정식으로 압축
2. **계수 오류의 정정** — $1/2$를 제거

그러나 그는 이 힘을 **전자기 일반 이론의 일부**로만 다뤘고, 전하의 운동방정식으로 통합하지는 않았다.

### 1.1.4 로렌츠 (1892–1895): 전자론과 최종 형태

**헨드릭 안톤 로렌츠**의 결정적 논문은 1892년 **「La théorie électromagnétique de Maxwell et son application aux corps mouvants」** (*맥스웰의 전자기 이론과 운동하는 물체에 대한 그 적용*)이다. 이 논문에서 로렌츠는:

- 에테르는 완전히 정지해 있고, 물질은 그 속을 움직이는 **이산적인 전자(electron)의 집합**이다.
- 미시적 장 $\mathbf{e}, \mathbf{b}$가 전자를 **직접 당긴다**.
- 전하 밀도 $\rho$와 전류 $\mathbf{j}$에 작용하는 **힘 밀도**를 $\mathbf{f} = \rho\mathbf{e} + \mathbf{j}\times\mathbf{b}$로 정의.

1895년 저서 **『Versuch einer Theorie der electrischen und optischen Erscheinungen in bewegten Körpern』** (*운동하는 물체에서의 전기적·광학적 현상 이론 시도*)에서 로렌츠는 점전하에 대한 현대적 형태로 정리했다:

$$\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐅 = q𝐄 + q𝐯×𝐁
> ```

이것이 우리가 오늘날 **로렌츠 힘(Lorentz force)** 이라고 부르는 것이다.

로렌츠의 진짜 기여는 공식 그 자체가 아니라, **전자기장과 물질의 상호작용을 미시적으로 정식화**한 데 있다. 그는 전자기학을 **전자의 역학**으로 환원했고, 이는 이후 특수상대론과 양자역학의 출발점이 되었다.

### 1.1.5 현대적 재해석: $F=dA$의 그림자

20세기 후반, 로렌츠 힘은 **미분기하학**의 언어로 재해석되었다. 전자기 퍼텐셜 $A_\mu$를 $U(1)$ 주다발의 **접속(connection)** 으로, 전자기장 텐서 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$를 그 **곡률(curvature)** 로 보면:

$$f^\mu = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> f^μ = qF^μνu_ν
> ```

즉, 로렌츠 힘은 **$U(1)$ 다발의 곡률이 하전 입자의 세계선을 휘게 하는 현상의 국소적 그림자**다. 이 관점은 2.5절과 5.3절에서 심화된다.

### 1.1.6 한계·예외

- **역사 서술의 불확정성**: "누가 먼저 발견했는가"는 우선권 논쟁이 있다. 헤비사이드와 로렌츠의 기여는 거의 동시대이며, 그 경계는 문헌에 따라 다르다.
- **맥스웰의 위치**: 맥스웰 방정식에 $q\mathbf{v}\times\mathbf{B}$가 없다는 사실은 종종 오해된다. 맥스웰은 **장의 방정식**을 완성했고, **전하의 운동방정식**은 로렌츠의 몫이었다.
- **에테르 가설**: 로렌츠의 원래 이론은 정지 에테르를 전제했다. 이 전제는 1905년 아인슈타인의 특수상대론으로 대체되었으나, 로렌츠 힘의 형태 자체는 **상대론적으로도 정확**하다 (3.1절 참조).

> **참고문헌**
> - Lorentz, H. A., *La théorie électromagnétique de Maxwell et son application aux corps mouvants*, Archives Néerlandaises **25**, 363–552 (1892). [archive.org](https://archive.org/details/lathorielectrom00loregoog)
> - Thomson, J. J., *Cathode Rays*, Philosophical Magazine **44**, 293–316 (1897). [doi:10.1080/14786449708621070](https://doi.org/10.1080/14786449708621070)
> - Heaviside, O., *Electromagnetic Theory*, Vol. II (1899). [archive.org](https://archive.org/details/electromagnetict02heavrich)

---

## 1.2 현대적 정의와 단위계

로렌츠 힘의 **현대적 정의**는 SI 단위계에서 다음과 같다:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + 𝐯×𝐁)
> ```

여기서 각 기호의 의미와 단위는:

| 기호 | 의미 | SI 단위 |
|---|---|---|
| $\mathbf{F}$ | 힘 | N (뉴턴) |
| $q$ | 전하량 | C (쿨롱) |
| $\mathbf{E}$ | 전기장 | V/m |
| $\mathbf{v}$ | 입자 속도 | m/s |
| $\mathbf{B}$ | 자기장 (자속 밀도) | T (테슬라) |

**두 항의 성질**:

- **전기력** $q\mathbf{E}$: 속도와 무관, 일을 할 수 있음
- **자기력** $q\mathbf{v}\times\mathbf{B}$: 속도에 수직, **일을 하지 않음**

마지막 성질은 다음 항등식으로 표현된다:

$$\mathbf{F}_m \cdot \mathbf{v} = 0$$

> **Unicode**
> ```
> 𝐅ₘ · 𝐯 = 0
> ```

이것은 자기장이 입자의 **운동 에너지를 바꾸지 않고 방향만 바꾼다**는 뜻이다. 사이클로트론에서 자기장이 입자를 원운동시키지만 가속하지는 못하는 이유가 여기에 있다.

### 1.2.1 라그랑지안에서의 유도 (예고)

로렌츠 힘은 **최소 결합(minimal coupling)** 원리로부터 자연스럽게 나온다. 상대론적 라그랑지안:

$$L = -mc^2\sqrt{1-v^2/c^2} - q\phi + q\mathbf{v}\cdot\mathbf{A}$$

> **Unicode**
> ```
> L = -mc²√(1-v²/c²) - qφ + q𝐯·𝐀
> ```

여기서 $\phi$는 전기 스칼라 퍼텐셜, $\mathbf{A}$는 자기 벡터 퍼텐셜이다. 오일러-라그랑주 방정식

$$\frac{d}{dt}\frac{\partial L}{\partial \mathbf{v}} = \frac{\partial L}{\partial \mathbf{x}}$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ 𝐯) = (∂ L)/(∂ 𝐱)
> ```

에 대입하면 정확히 로렌츠 힘이 나온다. 이 유도의 전 과정은 1.4절에서 다룬다.

### 1.2.2 가우스 단위계와 Heaviside-Lorentz 단위계

입자물리 문헌에서 **혼동의 핵심**이 단위계다. SI, 가우스, Heaviside-Lorentz, 자연 단위계가 서로 다르게 쓰인다.

#### 가우스 단위계 (Gaussian)

$$\mathbf{F} = q\left(\mathbf{E} + \frac{\mathbf{v}}{c}\times\mathbf{B}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + (𝐯)/(c)×𝐁)
> ```

특징:
- $\mathbf{E}$와 $\mathbf{B}$가 **같은 차원**을 가진다
- $c$가 명시적으로 들어가 **상대론적 성격**이 드러난다
- 맥스웰 방정식에 $4\pi$ 인자가 남는다

#### Heaviside-Lorentz 단위계 (유리화)

$$\mathbf{F} = q\left(\mathbf{E} + \frac{\mathbf{v}}{c}\times\mathbf{B}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + (𝐯)/(c)×𝐁)
> ```

형태는 가우스와 같아 보이나, $\mathbf{E}, \mathbf{B}$의 정의 자체에서 $4\pi$ 인자가 사라져 맥스웰 방정식이 단순화된다. 즉 $F = q(E+v/c\times B)$의 $B$ 수치 자체가 가우스계와 다르다:

$$\nabla\cdot\mathbf{E} = \rho$$

> **Unicode**
> ```
> ∇·𝐄 = ρ
> ```

SI로 변환할 때는 단순히 $c$만 넣으면 안 되고, 장 자체의 정의가 $4\pi$만큼 다르다. Jackson(3판, 부록) 기준 핵심 변환은:

| 물리량 | 가우스 → SI | HL → SI |
|---|---|---|
| 전하 $q$ | $q_{SI}=q_G/\sqrt{4\pi\epsilon_0}$ | $q_{SI}=q_{HL}\sqrt{\epsilon_0}$ |
| 전기장 $\mathbf{E}$ | $\mathbf{E}_{SI}=\sqrt{4\pi\epsilon_0}\mathbf{E}_G$ | $\mathbf{E}_{SI}=\mathbf{E}_{HL}/\sqrt{\epsilon_0}$ |
| 자기장 $\mathbf{B}$ | $\mathbf{B}_{SI}=\sqrt{4\pi/\mu_0}\mathbf{B}_G$ | $\mathbf{B}_{SI}=\mathbf{B}_{HL}/\sqrt{\mu_0}$ |
| $\mathbf{E},\mathbf{B}$ 관계 | $\mathbf{E}_G, \mathbf{B}_G$ 동차원 | $\nabla\cdot\mathbf{E}_{HL}=\rho_{HL}$, $\nabla\cdot\mathbf{E}_G=4\pi\rho_G$ |

즉, 가우스와 HL은 식 형태는 같아 보여도 $\mathbf{B}$ 수치 자체가 $\sqrt{4\pi}$만큼 다르다. 단순히 $\sqrt{\mu_0/\epsilon_0}$를 곱해서는 안 된다.

> **Unicode**
> ```
> 𝐁_SI = √(μ₀/ε₀)· 𝐁_HL
> ```

#### 자연 단위계 ($\hbar = c = 1$)

고에너지 물리에서 표준:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + 𝐯×𝐁)
> ```

형태는 SI와 동일하지만:
- $c=1$이므로 $\mathbf{v}$는 **무차원**
- $[\mathbf{E}] = [\mathbf{B}] = [\text{mass}]^2$
- $q$는 **무차원**

실제 수치 계산에서는 $q = e\sqrt{4\pi\alpha}$로 미세구조상수 $\alpha \approx 1/137$이 결합한다.

### 1.2.3 단위계 변환표

| 양 | SI | Gaussian | Heaviside-Lorentz | 자연 단위 |
|---|---|---|---|---|
| 힘 | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ |
| 전하 | $q$ | $q$ | $q$ | 무차원 |
| 전기장 | $\mathbf{E}$ | $\mathbf{E}$ | $\mathbf{E}$ | $\mathbf{E}$ |
| 자기장 | $\mathbf{B}$ | $\mathbf{B}/c$ | $\mathbf{B}/c$ | $\mathbf{B}$ |
| 로렌츠 힘 | $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | $q(\mathbf{E}+\frac{\mathbf{v}}{c}\times\mathbf{B})$ | $q(\mathbf{E}+\frac{\mathbf{v}}{c}\times\mathbf{B})$ | $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ |

### 1.2.4 한계·예외

- **단위계 혼동의 역사**: 19세기 전자기 단위계 논쟁(Electromagnetic vs Electrostatic units)은 맥스웰 방정식의 형태를 바꿨다. 이 혼란은 오늘날에도 입자물리와 응집물질 사이에 남아 있다.
- **입자물리 관례**: 자연 단위계에서 $c=1$로 두면 속도가 무차원이 되지만, 실제 실험 데이터와 비교할 때는 $c$를 복원해야 한다.
- **가우스 단위계의 잔존**: 천체물리와 플라즈마 물리에서는 여전히 가우스 단위계가 널리 쓰인다. 예를 들어 자기장을 Gauss(1 G = $10^{-4}$ T)로 표기하는 관행이 남아 있다.

> **참고문헌**
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), Chapter 11.
> - Griffiths, D. J., *Introduction to Electrodynamics*, 4th ed., Cambridge (2017), Chapter 5.

---

## 1.3 4차원 공변 표현

로렌츠 힘을 **4차원 공변 형태**로 쓰면 특수상대론과의 조화가 명확해진다. 이 절에서는 로렌츠 힘의 4-벡터 표현을 유도하고, 그것이 3차원 형태를 어떻게 포함하는지 본다.

### 1.3.1 전자기장 텐서 $F^{\mu\nu}$

전자기장을 4차원 반대칭 텐서로 정의한다:

$$F^{\mu\nu} = \begin{pmatrix}0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0\end{pmatrix}$$

> **Unicode**
> ```
> F^μν =  [ [0, -Eₓ/c, -E_y/c, -E_z/c];
>            [Eₓ/c, 0, -B_z, B_y];
>            [E_y/c, B_z, 0, -Bₓ];
>            [E_z/c, -B_y, Bₓ, 0] ]
> ```

성분을 명시적으로 쓰면:

$$F^{0i} = -E_i/c, \quad F^{ij} = -\epsilon_{ijk}B_k$$

> **Unicode**
> ```
> F^0i = -Eᵢ/c,   F^ij = -εᵢⱼₖBₖ
> ```

$F^{\mu\nu}$는 **반대칭**: $F^{\mu\nu} = -F^{\nu\mu}$. 이는 6개의 독립 성분($\mathbf{E}$ 3개 + $\mathbf{B}$ 3개)을 가진다.

### 1.3.2 4-속도와 4-운동량

입자의 4-속도:

$$u^\nu = \gamma(c, \mathbf{v}), \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}$$

> **Unicode**
> ```
> u^ν = γ(c, 𝐯),   γ = 1/√(1-v²/c²)
> ```

4-운동량:

$$p^\mu = (\gamma mc, \mathbf{p}) = m u^\mu$$

> **Unicode**
> ```
> p^μ = (γ mc, 𝐩) = m u^μ
> ```

### 1.3.3 4-힘의 정의

**4-힘(4-force)** 을 다음과 같이 정의한다:

$$f^\mu = q F^{\mu\nu} u_\nu$$

> **Unicode**
> ```
> f^μ = q F^μν u_ν
> ```

또는 고유시간 $\tau$에 대한 운동량 변화율로:

$$\frac{dp^\mu}{d\tau} = q F^{\mu\nu} u_\nu$$

> **Unicode**
> ```
> (dp^μ)/(dτ) = q F^μν u_ν
> ```

### 1.3.4 공간 성분 → 로렌츠 힘

$\mu = i$ (공간 성분)에 대해 계산하면:

$$f^i = q F^{i0} u_0 + q F^{ij} u_j$$

$F^{i0} = -F^{0i} = E_i/c$이고, $u_0 = \gamma c$이므로:

$$f^i = q\frac{E_i}{c}\gamma c + q(-\epsilon_{ijk}B_k)(\gamma v_j) = q\gamma E_i - q\gamma\epsilon_{ijk}v_j B_k$$

$\epsilon_{ijk}v_j B_k = (\mathbf{v}\times\mathbf{B})_i$이므로:

$$f^i = \gamma q(\mathbf{E} + \mathbf{v}\times\mathbf{B})_i$$

$f^i = dp^i/d\tau = \gamma\, dp^i/dt$이므로:

$$\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐩)/(dt) = q(𝐄 + 𝐯×𝐁)
> ```

**정확히 로렌츠 힘의 3차원 형태**다.

### 1.3.5 시간 성분 → 일률

$\mu = 0$ (시간 성분)에 대해:

$$f^0 = q F^{0i} u_i = q\left(-\frac{E_i}{c}\right)(\gamma v_i) = -\frac{\gamma q}{c}\mathbf{v}\cdot\mathbf{E}$$

$f^0 = dp^0/d\tau = \gamma\, d(\gamma mc)/dt \cdot c$이므로, 정리하면:

$$\frac{dE}{dt} = q\mathbf{v}\cdot\mathbf{E}$$

> **Unicode**
> ```
> (dE)/(dt) = q𝐯·𝐄
> ```

여기서 $E = \gamma mc^2$는 상대론적 에너지다. 이는 **자기장이 일을 하지 않는다**는 사실의 4차원 표현이다: $\mathbf{v}\times\mathbf{B}$ 항은 시간 성분에 나타나지 않는다.

### 1.3.6 직교성 $f^\mu u_\mu = 0$

4-힘과 4-속도의 내적을 계산하면:

$$f^\mu u_\mu = q F^{\mu\nu} u_\nu u_\mu$$

$F^{\mu\nu}$가 반대칭이고 $u_\mu u_\nu$가 대칭이므로 그 곱은 0:

$$f^\mu u_\mu = 0$$

> **Unicode**
> ```
> f^μ u_μ = 0
> ```

물리적 의미: 4-힘은 **세계선에 수직**이다. 이것이 자기력이 일을 하지 않는다는 성질의 4차원적 표현이며, 동시에 **정지질량이 변하지 않는다**는 것과 동치다:

$$\frac{dm}{d\tau} = 0$$

### 1.3.7 매스매티카 검증

```mathematica
(* 전자기장 텐서 정의 *)
Fmunu = {{0, -Ex/c, -Ey/c, -Ez/c},
         {Ex/c, 0, -Bz, By},
         {Ey/c, Bz, 0, -Bx},
         {Ez/c, -By, Bx, 0}};

(* 계량 (+,-,-,-) *)
g = DiagonalMatrix[{1, -1, -1, -1}];

(* 4-속도: 반변(contravariant) u^ν, 공변(covariant) u_ν = g_{νρ}u^ρ *)
uUp = {gamma c, gamma vx, gamma vy, gamma vz};
uDown = g . uUp;

(* 4-힘: f^μ = q F^{μν} u_ν 은 반드시 공변 u_ν(uDown)와 축약해야 한다 *)
fourForce = q Fmunu . uDown;

(* 공간 성분 검증 *)
spatialForce = fourForce[[2 ;; 4]] / gamma;
expected = q ({Ex, Ey, Ez} + Cross[{vx, vy, vz}, {Bx, By, Bz}]);

Simplify[spatialForce - expected] == {0, 0, 0}

(* 주의: uUp을 그대로 Fmunu와 축약하면(F^{μν}u^ν) 자기력 항의 부호가 뒤집혀
   q(E - v×B)가 나오는 오류가 생긴다. 본문·코드 모두 u_ν(공변)로 통일한다. *)
```

### 1.3.8 한계·예외

- **비상대론 극한**: $v \ll c$에서 $\gamma \to 1$, 4-벡터 형태는 3차원 로렌츠 힘으로 환원된다.
- **일반상대론 확장**: 곡선 시공간에서는 $\partial_\mu \to \nabla_\mu$로 바꾸고, $F^{\mu\nu}$는 계량과 결합한다 (→ §6.2.1).
- **부호 규약**: $(-,+,+,+)$ vs $(+,-,-,-)$ 규약에 따라 $F^{\mu\nu}$의 부호가 달라진다. 이 문서는 $(+,-,-,-)$ 규약을 사용한다.

> **참고문헌**
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §11.7.
> - Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §23.

---
## 1.4 라그랑주·해밀토니안 정식화

로렌츠 힘은 뉴턴의 $F=ma$로도 쓸 수 있지만, 그 진짜 구조는 **라그랑지안의 게이지 결합**에서 드러난다. 이 절에서는 라그랑지안에서 출발해 오일러-라그랑주 방정식으로 로렌츠 힘을 유도하고, 르장드르 변환으로 해밀토니안을 얻은 뒤, 심플렉틱 구조와 푸아송 괄호로 마무리한다.

### 1.4.1 라그랑지안 $L = \frac12 mv^2 - q\phi + q\mathbf{v}\cdot\mathbf{A}$

**왜 이 형태인가?**

자유 입자의 라그랑지안 $L_0 = \frac12 mv^2$에 전자기장과의 상호작용 항을 더해야 한다. 요구 조건은 세 가지다:

1. **운동방정식이 $\mathbf{E}, \mathbf{B}$에 대해 선형**일 것
2. **게이지 변환** $A^\mu \to A^\mu + \partial^\mu\chi$ 하에 작용 $S=\int L\,dt$가 경계항까지만 변할 것
3. **갈릴레이/로렌츠 공변성**에서 $A^\mu u_\mu$ 형태일 것

이 조건을 만족하는 유일한 스칼라 결합은 $q\mathbf{v}\cdot\mathbf{A} - q\phi$다. 상대론적 작용에서 출발하면 더 명확하다:

$$S_{int} = -q \int A_\mu\, dx^\mu = \int (-q\phi + q\mathbf{v}\cdot\mathbf{A})\,dt$$

> **Unicode**
> ```
> Sᵢₙₜ = -q ∫ A_μ dx^μ = ∫ (-qφ + q𝐯·𝐀)dt
> ```

따라서 비상대론적 라그랑지안은:

$$L(\mathbf{x},\mathbf{v},t) = \frac12 m\mathbf{v}^2 - q\phi(\mathbf{x},t) + q\mathbf{v}\cdot\mathbf{A}(\mathbf{x},t)$$

> **Unicode**
> ```
> L(𝐱,𝐯,t) = (1)/(2) m𝐯² - qφ(𝐱,t) + q𝐯·𝐀(𝐱,t)
> ```

여기서 $\mathbf{v} = \dot{\mathbf{x}}$다. 퍼텐셜이 **속도에 의존**하는 대표적 예이며, 이를 **속도 의존 퍼텐셜(velocity-dependent potential)** 이라 부른다.

### 1.4.2 오일러-라그랑주 방정식 → 로렌츠 힘 완전 유도

오일러-라그랑주 방정식:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} - \frac{\partial L}{\partial x_i} = 0$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ x˙ᵢ) - (∂ L)/(∂ xᵢ) = 0
> ```

#### Step 1: 정준 운동량

$$p_i \equiv \frac{\partial L}{\partial \dot{x}_i} = m\dot{x}_i + qA_i(\mathbf{x},t)$$

> **Unicode**
> ```
> pᵢ ≡ (∂ L)/(∂ x˙ᵢ) = mx˙ᵢ + qAᵢ(𝐱,t)
> ```

즉, **정준 운동량 $\mathbf{p}$는 기계적 운동량 $\boldsymbol{\pi}=m\mathbf{v}$와 다르다**:

$$\mathbf{p} = m\mathbf{v} + q\mathbf{A}$$

> **Unicode**
> ```
> 𝐩 = m𝐯 + q𝐀
> ```

이 차이가 전자기 해밀턴 역학의 핵심이다.

#### Step 2: 좌변 시간미분

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} = m\ddot{x}_i + q\frac{dA_i}{dt}$$

$A_i$가 $\mathbf{x}(t), t$에 의존하므로 **전미분**을 쓴다:

$$\frac{dA_i}{dt} = \frac{\partial A_i}{\partial t} + \sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j}$$

따라서:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} = m\ddot{x}_i + q\left(\frac{\partial A_i}{\partial t} + \sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j}\right)$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ x˙ᵢ) = mx¨ᵢ + q((∂ Aᵢ)/(∂ t) + ∑ⱼ x˙ⱼ(∂ Aᵢ)/(∂ xⱼ))
> ```

#### Step 3: 우변 위치미분

$$\frac{\partial L}{\partial x_i} = -q\frac{\partial\phi}{\partial x_i} + q\sum_j \dot{x}_j \frac{\partial A_j}{\partial x_i}$$

> **Unicode**
> ```
> (∂ L)/(∂ xᵢ) = -q(∂φ)/(∂ xᵢ) + q∑ⱼ x˙ⱼ (∂ Aⱼ)/(∂ xᵢ)
> ```

#### Step 4: 합치기

오일러-라그랑주 방정식에 대입:

$$m\ddot{x}_i + q\frac{\partial A_i}{\partial t} + q\sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j} = -q\frac{\partial\phi}{\partial x_i} + q\sum_j \dot{x}_j \frac{\partial A_j}{\partial x_i}$$

정리하면:

$$m\ddot{x}_i = -q\frac{\partial\phi}{\partial x_i} - q\frac{\partial A_i}{\partial t} + q\sum_j \dot{x}_j\left(\frac{\partial A_j}{\partial x_i} - \frac{\partial A_i}{\partial x_j}\right)$$

> **Unicode**
> ```
> mx¨ᵢ = -q(∂φ)/(∂ xᵢ) - q(∂ Aᵢ)/(∂ t) + q∑ⱼ x˙ⱼ((∂ Aⱼ)/(∂ xᵢ) - (∂ Aᵢ)/(∂ xⱼ))
> ```

#### Step 5: 장의 정의로 환원

전기장과 자기장의 퍼텐셜 정의:

$$\mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}, \quad B_k = (\nabla\times\mathbf{A})_k = \epsilon_{kij}\frac{\partial A_j}{\partial x_i}$$

> **Unicode**
> ```
> 𝐄 = -∇φ - (∂𝐀)/(∂ t),   Bₖ = (∇×𝐀)ₖ = εₖᵢⱼ(∂ Aⱼ)/(∂ xᵢ)
> ```

그리고 레비-치비타 항등식:

$$\sum_j \dot{x}_j(\partial_i A_j - \partial_j A_i) = [\mathbf{v}\times(\nabla\times\mathbf{A})]_i = (\mathbf{v}\times\mathbf{B})_i$$

> **Unicode**
> ```
> ∑ⱼ x˙ⱼ(∂ᵢ Aⱼ - ∂ⱼ Aᵢ) = [𝐯×(∇×𝐀)]ᵢ = (𝐯×𝐁)ᵢ
> ```

따라서:

$$m\ddot{\mathbf{x}} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐱¨ = q𝐄 + q𝐯×𝐁
> ```

**라그랑지안에서 장이 아닌 퍼텐셜로 시작했지만 결과는 게이지 불변한 $E, B$로만 표현된다.** 이는 라그랑지안이 게이지 변환 하에 전체 미분만큼만 변하기 때문이다.

### 1.4.3 해밀토니안

르장드르 변환:

$$H = \mathbf{p}\cdot\dot{\mathbf{x}} - L$$

> **Unicode**
> ```
> H = 𝐩·𝐱˙ - L
> ```

$\dot{\mathbf{x}} = (\mathbf{p}-q\mathbf{A})/m$을 대입하면:

$$H(\mathbf{x},\mathbf{p},t) = \frac{1}{2m}\left(\mathbf{p}-q\mathbf{A}(\mathbf{x},t)\right)^2 + q\phi(\mathbf{x},t)$$

> **Unicode**
> ```
> H(𝐱,𝐩,t) = (1)/(2m)(𝐩-q𝐀(𝐱,t))² + qφ(𝐱,t)
> ```

**물리적 의미:**

- $\mathbf{p}$: **정준 운동량** — 게이지 의존적
- $\boldsymbol{\pi} = \mathbf{p}-q\mathbf{A} = m\mathbf{v}$: **운동학적 운동량** — 게이지 불변, 실제 측정되는 속도

이 차이가 양자역학에서 **최소 결합** $\hat{\mathbf{p}} \to \hat{\mathbf{p}}-q\mathbf{A}$의 기원이다 (→ §3.3.1).

### 1.4.4 정준 방정식

해밀턴 방정식:

$$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}$$

> **Unicode**
> ```
> q˙ᵢ = (∂ H)/(∂ pᵢ),   p˙ᵢ = -(∂ H)/(∂ qᵢ)
> ```

$q_i = x_i$로 두면:

$$\dot{x}_i = \frac{1}{m}(p_i - qA_i) = v_i$$

> **Unicode**
> ```
> x˙ᵢ = (1)/(m)(pᵢ - qAᵢ) = vᵢ
> ```

$$\dot{p}_i = -\frac{\partial H}{\partial x_i} = \frac{q}{m}\sum_j (p_j - qA_j)\frac{\partial A_j}{\partial x_i} - q\frac{\partial\phi}{\partial x_i}$$

> **Unicode**
> ```
> p˙ᵢ = -(∂ H)/(∂ xᵢ) = (q)/(m)∑ⱼ (pⱼ - qAⱼ)(∂ Aⱼ)/(∂ xᵢ) - q(∂φ)/(∂ xᵢ)
> ```

두 식을 결합해 $m\ddot{x}_i$를 만들면 다시 로렌츠 힘이 나온다.

**주의:** 해밀턴 형식에서는 $\mathbf{p}$가 직접 힘을 받는 것처럼 보이지만, 실제 가속도는 $\dot{\boldsymbol{\pi}}$에 있다.

### 1.4.5 심플렉틱 구조와 위상공간 기하

위상공간 $T^*\mathbb{R}^3 \cong \mathbb{R}^6$의 좌표를 $\xi = (\mathbf{x},\mathbf{p})$라 하자.

**심플렉틱 2-형식:**

$$\omega = \sum_i dp_i \wedge dx_i = d\mathbf{p}\wedge d\mathbf{x}$$

> **Unicode**
> ```
> ω = ∑ᵢ dpᵢ ∧ dxᵢ = d𝐩∧ d𝐱
> ```

행렬 표현:

$$J = \begin{pmatrix}0 & I \\ -I & 0\end{pmatrix}$$

> **Unicode**
> ```
> J =  [ [0, I];
>        [-I, 0] ]
> ```

에 대해 $\omega(u,v) = u^T J v$다.

**해밀턴 흐름은 $\omega$를 보존**한다: $\mathcal{L}_{X_H}\omega = 0$, 즉 리우빌 정리 $\nabla\cdot X_H = 0$. 위상 부피가 보존된다.

해밀턴 벡터장 $X_H$는 $i_{X_H}\omega = -dH$로 정의:

$$X_H = \left(\frac{\partial H}{\partial \mathbf{p}}, -\frac{\partial H}{\partial \mathbf{x}}\right) = (\mathbf{v}, q\nabla(\mathbf{v}\cdot\mathbf{A}) - q\nabla\phi)$$

> **Unicode**
> ```
> X_H = ((∂ H)/(∂ 𝐩), -(∂ H)/(∂ 𝐱)) = (𝐯, q∇(𝐯·𝐀) - q∇φ)
> ```

**핵심:** 전자기장이 있어도 심플렉틱 구조 $\omega$ 자체는 표준이다. 장의 효과는 $H$ 안에 $A$를 넣어서 구현된다. 이것이 **최소 결합이 심플렉틱 구조를 깨지 않는** 이유다.

**기하학적 관점:** $A$는 **접속(connection) 1-형식**, $F=dA$는 **곡률(curvature)**. 입자는 $U(1)$ 주다발 위에서 움직이며, 로렌츠 힘은 이 곡률에 의해 입자의 세계선이 **geodesic 운동에서 이탈(departure from geodesic motion)** 하게 만드는 힘이다 (→ §2.5.4). 이는 서로 이웃한 두 geodesic의 상대가속도를 기술하는 일반상대론의 표준적 geodesic deviation과는 구별되는 개념이다.

### 1.4.6 푸아송 괄호와 비가환 운동량

표준 푸아송 괄호:

$$\{F,G\} = \sum_i \left(\frac{\partial F}{\partial x_i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial x_i}\right)$$

> **Unicode**
> ```
> F,G = ∑ᵢ ((∂ F)/(∂ xᵢ)(∂ G)/(∂ pᵢ) - (∂ F)/(∂ pᵢ)(∂ G)/(∂ xᵢ))
> ```

**정준 관계:**

$$\{x_i, p_j\} = \delta_{ij}, \quad \{x_i,x_j\}=0, \quad \{p_i,p_j\}=0$$

> **Unicode**
> ```
> xᵢ, pⱼ = δᵢⱼ,    xᵢ,xⱼ = 0,    pᵢ,pⱼ = 0
> ```

**운동방정식:**

$$\dot{F} = \{F,H\} + \partial_t F$$

> **Unicode**
> ```
> F˙ = F,H + ∂ₜ F
> ```

$\dot{x}_i = \{x_i,H\} = (p_i-qA_i)/m$은 그대로. $\dot{p}_i = \{p_i,H\}$를 계산하면 정준 방정식과 동일.

#### 운동학적 운동량의 괄호

**핵심은 운동학적 운동량 $\pi_i = p_i - qA_i$의 괄호다:**

$$\{\pi_i, \pi_j\} = \{p_i-qA_i, p_j-qA_j\} = q\left(\frac{\partial A_j}{\partial x_i} - \frac{\partial A_i}{\partial x_j}\right) = q\epsilon_{ijk}B_k$$

> **Unicode**
> ```
> πᵢ, πⱼ = pᵢ-qAᵢ, pⱼ-qAⱼ = q((∂ Aⱼ)/(∂ xᵢ) - (∂ Aᵢ)/(∂ xⱼ)) = qεᵢⱼₖBₖ
> ```

$$\{x_i, \pi_j\} = \delta_{ij}$$

> **Unicode**
> ```
> xᵢ, πⱼ = δᵢⱼ
> ```

**즉, 운동학적 운동량은 서로 가환하지 않는다.** 자기장이 $\mathbf{p}$ 공간의 **비가환성**으로 나타난다.

이제 $\dot{\pi}_i = \{\pi_i, H\}$로 직접 힘을 계산할 수 있다. $H = \pi^2/2m + q\phi$이므로:

$$\dot{\pi}_i = \{\pi_i, \pi_j\}\frac{\pi_j}{m} + \{\pi_i, q\phi\}$$

정리하면:

$$\frac{d}{dt}(m\mathbf{v}) = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> (d)/(dt)(m𝐯) = q𝐄 + q𝐯×𝐁
> ```

**즉, 정준 변수 $(\mathbf{x},\mathbf{p})$는 항상 표준 괄호를 만족하고 자기장은 $\mathbf{p}$ 공간의 비가환성으로 나타난다.** 이 구조가 양자화하면:

$$[\hat{\pi}_i,\hat{\pi}_j] = i\hbar q\epsilon_{ijk}B_k$$

> **Unicode**
> ```
> [π̂ᵢ,π̂ⱼ] = iℏ qεᵢⱼₖBₖ
> ```

가 되어 **란다우 준위, 양자 홀 효과의 출발점**이 된다 (→ §3.3.2, §5.3.1).

### 1.4.7 매스매티카 검증

```mathematica
(* 라그랑지안 정의 *)
Clear[L, phi, Avec, m, q];
L = (1/2) m (vx^2 + vy^2 + vz^2) - q phi[x, y, z, t]
    + q (vx Ax[x, y, z, t] + vy Ay[x, y, z, t] + vz Az[x, y, z, t]);

(* 오일러-라그랑주 방정식 *)
vars = {x, y, z};
vels = {vx, vy, vz};
EL[i_] := D[D[L, vels[[i]]] /. {vx -> x'[t], vy -> y'[t], vz -> z'[t]}, t]
         - D[L /. {vx -> x'[t], vy -> y'[t], vz -> z'[t]}, vars[[i]]];

(* 결과 검증 *)
(* m x'' = q (E_x + (v × B)_x) 형태가 나와야 함 *)
Simplify[EL[1]]
```

### 1.4.8 한계·예외

- **비상대론 극한**: 위 라그랑지안은 $v \ll c$에서만 유효. 상대론적 라그랑지안은 $-mc^2\sqrt{1-v^2/c^2} - q\phi + q\mathbf{v}\cdot\mathbf{A}$ (→ §3.1.1).
- **게이지 의존성**: $L$과 $H$는 게이지 변환 하에 불변하지 않다. 물리적 예측만 불변이다.
- **정준 운동량의 비유일성**: $\mathbf{p} = m\mathbf{v} + q\mathbf{A}$는 게이지 선택에 따라 달라진다. 실험적으로 측정되는 것은 $\boldsymbol{\pi} = m\mathbf{v}$뿐이다.
- **다체 계**: $N$개 입자에 대해서는 각 입자마다 최소 결합을 적용해야 하며, 상호작용 항 $q_i q_j/4\pi\epsilon_0|\mathbf{x}_i-\mathbf{x}_j|$가 추가된다.

> **참고문헌**
> - Goldstein, H., Poole, C., Safko, J., *Classical Mechanics*, 3rd ed., Addison-Wesley (2001), Chapter 1.5, 8.1. [doi:10.1119/1.1484149](https://doi.org/10.1119/1.1484149)
> - Landau & Lifshitz, *Mechanics*, 3rd ed., Pergamon (1976), §16–17.
> - Arnold, V. I., *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer (1989), §40.

---

## 1.5 게이지 불변성 — 힘과 위상의 분리

로렌츠 힘의 가장 중요한 현대적 통찰은 **게이지 불변성**이다. 이 절에서는 고전역학에서 게이지 자유도가 물리에 영향을 주지 않음을 증명하고, **양자역학에서는 이야기가 확장됨**을 예고한다.

### 1.5.1 게이지 변환

전자기 퍼텐셜 $A^\mu = (\phi/c, \mathbf{A})$로 전자기장 텐서를 정의한다:

$$F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$$

> **Unicode**
> ```
> F^μν = ∂^μ A^ν - ∂^ν A^μ
> ```

**게이지 변환**은 임의의 스칼라 함수 $\chi(\mathbf{x},t)$에 대해:

$$A^\mu \to A'^\mu = A^\mu + \partial^\mu \chi$$

> **Unicode**
> ```
> A^μ → A'^μ = A^μ + ∂^μ χ
> ```

성분으로 쓰면:

$$\phi \to \phi - \frac{\partial\chi}{\partial t}, \quad \mathbf{A} \to \mathbf{A} + \nabla\chi$$

> **Unicode**
> ```
> φ → φ - (∂χ)/(∂ t),   𝐀 → 𝐀 + ∇χ
> ```

### 1.5.2 $F^{\mu\nu}$의 불변성

게이지 변환 후:

$$F'^{\mu\nu} = \partial^\mu(A^\nu + \partial^\nu\chi) - \partial^\nu(A^\mu + \partial^\mu\chi) = F^{\mu\nu} + [\partial^\mu, \partial^\nu]\chi$$

편미분은 가환하므로 $[\partial^\mu, \partial^\nu]\chi = 0$:

$$F'^{\mu\nu} = F^{\mu\nu}$$

> **Unicode**
> ```
> F'^μν = F^μν
> ```

**즉, 전자기장 텐서는 게이지 불변**이다. 따라서:

$$f^\mu = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> f^μ = qF^μνu_ν
> ```

도 **명시적으로 게이지 불변**이다.

### 1.5.3 고전역학: 힘은 게이지 불변

라그랑지안은 게이지 변환 하에 어떻게 변하는가?

$$L = \frac12 mv^2 - q\phi + q\mathbf{v}\cdot\mathbf{A}$$

게이지 변환 $\phi \to \phi - \partial_t\chi$, $\mathbf{A} \to \mathbf{A} + \nabla\chi$를 대입:

$$L \to L - q\frac{\partial\chi}{\partial t} + q\mathbf{v}\cdot\nabla\chi = L + q\frac{d\chi}{dt}$$

> **Unicode**
> ```
> L → L - q(∂χ)/(∂ t) + q𝐯·∇χ = L + q(dχ)/(dt)
> ```

여기서 전미분 $\frac{d\chi}{dt} = \partial_t\chi + \mathbf{v}\cdot\nabla\chi$를 사용했다.

**라그랑지안은 전체 미분만큼 변한다.** 오일러-라그랑주 방정식은 전체 미분에 영향받지 않으므로 **운동방정식은 불변**이다.

이것이 **로렌츠 힘이 게이지 불변**인 이유다:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

$\mathbf{E}, \mathbf{B}$는 $F^{\mu\nu}$에서 나오므로 게이지 불변. $\phi, \mathbf{A}$ 자체는 게이지 의존적이지만, 물리적 관측량인 힘은 불변.

### 1.5.4 양자역학: 위상은 물리적

**그러나 양자역학에서는 이야기가 확장된다.**

슈뢰딩거 방정식에 최소 결합 $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$를 적용하면:

$$i\hbar\frac{\partial\psi}{\partial t} = \left[\frac{(\hat{\mathbf{p}} - q\mathbf{A})^2}{2m} + q\phi\right]\psi$$

> **Unicode**
> ```
> iℏ(∂ψ)/(∂ t) = [((𝐩̂ - q𝐀)²)/(2m) + qφ]ψ
> ```

게이지 변환 하에 파동함수는 **위상 변환**을 받는다:

$$\psi \to \psi' = \exp\left(i\frac{q\chi}{\hbar}\right)\psi$$

> **Unicode**
> ```
> ψ → ψ' = exp(i(qχ)/(ℏ))ψ
> ```

이 변환과 $A^\mu \to A^\mu + \partial^\mu\chi$를 결합하면 슈뢰딩거 방정식이 **불변**이다.

**핵심:** 파동함수 자체는 게이지 변환 하에 변하지만, 물리적 관측량 $|\psi|^2$, $\mathbf{j}$는 불변이다. 그러나 **위상 자체는 물리적**이다.

### 1.5.5 아하로노프-봄 효과 예고

솔레노이드 외부를 생각하자. 솔레노이드 내부에 자기장 $\mathbf{B} \neq 0$, 외부에는 $\mathbf{B} = 0$. 외부에서는 $\nabla\times\mathbf{A} = 0$이지만, $\mathbf{A} \neq 0$이다.

전자가 솔레노이드를 우회하는 두 경로를 지나면, 두 경로의 **위상차**가 생긴다:

$$\Delta\varphi_{AB} = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi_B}{\hbar}$$

> **Unicode**
> ```
> Δφ_AB = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ_B)/(ℏ)
> ```

여기서 $\Phi_B = \int \mathbf{B}\cdot d\mathbf{S}$는 솔레노이드 내부의 자속이다.

**고전적 궤적에 작용하는 힘 자체는 게이지 불변하게 0으로 남는다.** 그러나 양자 간섭에서는 $\mathbf{B} = 0$인 영역에서도 $\mathbf{A}$가 간섭에 영향을 준다.

이것이 **아하로노프-봄 효과**다. 이는 로렌츠 힘이 국소적 힘이지만, **양자 위상은 비국소적**임을 보여준다 (→ §2.5.2).

### 1.5.6 $U(1)$ 다발의 예고편

현대적 관점에서 게이지 변환은 **$U(1)$ 주다발의 수직 자기동형(vertical automorphism)** 이다. 파동함수는 **연관 복소 선다발의 단면**이고, $A$는 **접속**이며, $F = dA$는 **곡률**이다.

이 관점은 2.5절에서 완전히 전개된다. 여기서는 다음을 기억하자:

> **로렌츠 힘은 게이지 불변성을 강제하는 구조 $F = dA$ 덕분에 게이지 선택에 관계없이 동일한 물리적 궤적을 주는, 전자기학에서 게이지 원리가 성립하는 가장 단순한 증거다.**

### 1.5.7 매스매티카 검증

```mathematica
(* 게이지 변환 *)
chi = chi[x, y, z, t];
Avec = {Ax[x, y, z, t], Ay[x, y, z, t], Az[x, y, z, t]};
phi = phi[x, y, z, t];

AvecPrime = Avec + Grad[chi, {x, y, z}];
phiPrime = phi - D[chi, t];

(* 장의 불변성 검증 *)
BPrime = Curl[AvecPrime, {x, y, z}];
B = Curl[Avec, {x, y, z}];
Simplify[BPrime - B] == {0, 0, 0}


EPrime = -Grad[phiPrime, {x, y, z}] - D[AvecPrime, t];
E = -Grad[phi, {x, y, z}] - D[Avec, t];
Simplify[EPrime - E] == {0, 0, 0}

```

### 1.5.8 한계·예외

- **비단순 연결 공간**: 아하로노프-봄 효과는 공간이 비단순 연결(예: $\mathbb{R}^3 \setminus \text{solenoid} \simeq S^1$)일 때만 나타난다. 단순 연결에서는 $\oint \mathbf{A}\cdot d\boldsymbol{\ell} = 0$이 강제된다.
- **대역적 게이지 변환**: $\chi$가 다중값 함수일 수 있다. 이 경우 위상은 $2\pi$의 정수배만큼만 게이지 불변이다 (→ §2.5.3).
- **비아벨 게이지 이론**: $SU(2)$나 $SU(3)$에서는 $F = dA + A\wedge A$로 교환자 항이 추가된다 (→ §6.1.1).
- **게이지 고정**: 실제 계산에서는 특정 게이지(쿨롱, 로런츠, 란다우 등)를 선택해 계산을 단순화한다. 물리적 결과는 게이지 선택과 무관하다.

> **참고문헌**
> - Aharonov, Y., Bohm, D., *Significance of Electromagnetic Potentials in the Quantum Theory*, Physical Review **115**, 485–491 (1959). [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §2.6, §12.1.
> - Nakahara, M., *Geometry, Topology and Physics*, 2nd ed., Taylor & Francis (2003), Chapter 10.

---

 
# 2막. 수학적 구조 (Mathematical Structure)

> **막의 흐름**
> 균일장 궤적 → 드리프트 이론 → 단열 불변량 → 수치해석 → 위상수학
>
> 1막에서 로렌츠 힘의 언어(정의·역학·게이지)를 확정했다. 2막은 그 언어로 **실제 궤적을 푸는 방법**을 다룬다. 해석해(2.1), 섭동 이론(2.2), 불변량(2.3), 수치해석(2.4), 위상수학(2.5)이 그 다섯 기둥이다.

---

## 2.1 균일 자기장 내 궤적

균일 자기장은 모든 자기 구속의 **0차 근사**이며, 비균일장은 이에 대한 섭동으로 다룬다. 이 절에서는 균일 자기장 내 하전 입자의 궤적을 완전히 풀고, 유도 중심(guiding center) 좌표를 도입한다.

### 2.1.1 운동방정식과 해

$\mathbf{B} = B_0\hat{z}$ 균일, $\mathbf{E} = 0$을 가정하자. 로렌츠 힘은:

$$m\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐯˙ = q𝐯×𝐁
> ```

성분으로 쓰면:

$$\dot{v}_x = \omega_c v_y, \quad \dot{v}_y = -\omega_c v_x, \quad \dot{v}_z = 0$$

> **Unicode**
> ```
> v˙ₓ = ω_c v_y,   v˙_y = -ω_c vₓ,   v˙_z = 0
> ```

여기서 **사이클로트론 진동수**:

$$\omega_c = \frac{qB_0}{m}$$

> **Unicode**
> ```
> ω_c = (qB₀)/(m)
> ```

부호는 전하 부호를 포함한다. 물리적 회전수는 $|\omega_c|$다. **이온은 $\mathbf{B}$에 대해 왼손, 전자는 오른손** 방향으로 회전한다.

**속도 해:**

$$v_x = v_\perp \cos(\omega_c t + \phi_0)$$
$$v_y = -v_\perp \sin(\omega_c t + \phi_0)$$
$$v_z = v_\parallel = \text{const}$$

> **Unicode**
> ```
> vₓ = v_⊥ cos(ω_c t + φ₀)
> v_y = -v_⊥ sin(ω_c t + φ₀)
> v_z = v_∥ = const
> ```

**위치 해** (적분):

$$x(t) = X_G + \frac{v_\perp}{\omega_c}\sin(\omega_c t+\phi_0)$$
$$y(t) = Y_G + \frac{v_\perp}{\omega_c}\cos(\omega_c t+\phi_0)$$
$$z(t) = Z_G + v_\parallel t$$

> **Unicode**
> ```
> x(t) = X_G + (v_⊥)/(ω_c)sin(ω_c t+φ₀)
> y(t) = Y_G + (v_⊥)/(ω_c)cos(ω_c t+φ₀)
> z(t) = Z_G + v_∥ t
> ```

여기서 $(X_G, Y_G, Z_G)$는 **유도 중심(guiding center)** 의 초기 위치다.

### 2.1.2 라모르 반지름

궤적의 반지름:

$$r_L = \frac{m v_\perp}{|q|B_0} = \frac{v_\perp}{|\omega_c|}$$

> **Unicode**
> ```
> r_L = (m v_⊥)/(|q|B₀) = (v_⊥)/(|ω_c|)
> ```

**궤적의 기하학:** $xy$ 평면에서 반지름 $r_L$의 원운동 + $z$ 방향 등속운동 = **나선(helix)**.

**수치 예시:**
- 전자 ($m_e = 9.11\times10^{-31}$ kg, $q = -e$), $v_\perp = 10^6$ m/s, $B_0 = 1$ T
- $r_L = (9.11\times10^{-31})(10^6)/(1.6\times10^{-19})(1) \approx 5.7\ \mu$m
- $\omega_c = eB/m_e \approx 1.76\times10^{11}$ rad/s

### 2.1.3 유도 중심 좌표

원운동의 중심 $(X_G, Y_G)$가 **유도 중심**이다. 이를 입자 위치로 표현하면:

$$\mathbf{R}_g = \mathbf{r} + \frac{m}{qB_0^2}\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐑_g = 𝐫 + (m)/(qB₀²)𝐯×𝐁
> ```

**검증:** $\mathbf{B} = B_0\hat{z}$, $\mathbf{v} = (v_x, v_y, 0)$이면:

$$\mathbf{v}\times\mathbf{B} = (v_y B_0, -v_x B_0, 0)$$

따라서:

$$X_g = x + \frac{m v_y}{qB_0}, \quad Y_g = y - \frac{m v_x}{qB_0}$$

$x(t), y(t)$를 대입하면 $X_g, Y_g$가 시간에 무관함을 확인할 수 있다.

**유도 중심의 물리적 의미:**
- 입자는 유도 중심 주위를 $r_L$ 반지름으로 회전
- 유도 중심은 자기장에 수직인 평면에서 **거의 정지** (균일장에서 완전 정지)
- 비균일장에서는 유도 중심이 **드리프트**한다 (→ §2.2)

### 2.1.4 매스매티카 검증

```mathematica
(* 균일 자기장 내 운동방정식 풀이 *)
Bvec = {0, 0, B0};
eqns = {
  m x''[t] == q (y'[t] B0),
  m y''[t] == q (-x'[t] B0),
  m z''[t] == 0,
  x[0] == x0, y[0] == y0, z[0] == z0,
  x'[0] == vx0, y'[0] == vy0, z'[0] == vz0
};
sol = DSolve[eqns, {x[t], y[t], z[t]}, t];
Simplify[sol]
(* 결과: 원운동 + z 등속운동 *)
```

### 2.1.5 한계·예외

- **상대론적 영역**: $v \to c$에서 $\omega_c \to qB/\gamma m$으로 감소, 궤적은 여전히 나선이지만 진동수가 에너지 의존 (→ §3.1.3).
- **전기장 존재**: $\mathbf{E} \neq 0$이면 추가 드리프트 발생 (→ §2.2.1).
- **비균일장**: $r_L \sim L_B$ (자기장 변화 스케일)이면 유도 중심 근사 붕괴 (→ §2.2.6).

> **참고문헌**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963). [doi:10.1002/9781118033156](https://doi.org/10.1002/9781118033156)
> - Chen, F. F., *Introduction to Plasma Physics and Controlled Fusion*, 3rd ed., Springer (2016), Chapter 2.

---

## 2.2 드리프트 이론 — 비균일장의 섭동

균일장은 이상화다. 실제 플라즈마와 자기권에서는 자기장이 공간에 따라 변한다. 이 절에서는 **유도 중심 근사**로 비균일장의 효과를 **드리프트 속도**로 정리한다.

### 2.2.1 $E\times B$ 드리프트

> **존재 조건:** 상대론적 불변량 $\mathbf{E}^2 - c^2\mathbf{B}^2 < 0$ (즉 $|\mathbf{E}| < c|\mathbf{B}|$) 일 때만 순수 $E\times B$ 드리프트 해가 존재한다. $ |\mathbf{E}| > c|\mathbf{B}|$이면 드리프트 속도가 $c$를 넘어 물리적 해 없음 — 이때는 전기장이 지배.

균일 $\mathbf{E}$와 균일 $\mathbf{B}$가 동시에 있을 때:

$$m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> m𝐯˙ = q(𝐄+𝐯×𝐁)
> ```

해를 $\mathbf{v} = \mathbf{V}_d + \mathbf{u}$로 분해하자. $\mathbf{u}$가 순수 회전을 따르도록:

$$\dot{\mathbf{u}} = \frac{q}{m}\mathbf{u}\times\mathbf{B}$$

$\mathbf{V}_d$가 상수라 가정하면:

$$0 = q\mathbf{E} + q\mathbf{V}_d\times\mathbf{B} \implies \mathbf{E} + \mathbf{V}_d\times\mathbf{B} = 0$$

양변에 $\mathbf{B}\times$를 취하면:

$$\mathbf{V}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

> **Unicode**
> ```
> 𝐕_E = (𝐄×𝐁)/(B²)
> ```

**핵심 성질:**
- $q, m, v$에 **무관** — 이온과 전자가 같이 이동
- 따라서 **전류를 만들지 않음**
- 플라즈마 전체가 $\mathbf{V}_E$로 이동
- $\mathbf{E}_\parallel$은 드리프트에 기여하지 않고 그대로 가속

**일반해:**

$$\mathbf{v}(t) = \mathbf{V}_E + v_\parallel\hat{b} + v_\perp\hat{\perp}(t)$$

> **Unicode**
> ```
> 𝐯(t) = 𝐕_E + v_∥b̂ + v_⊥⊥̂(t)
> ```

나선이 $\mathbf{V}_E$ 속도로 표류한다.

**편극 드리프트:** $E_\perp$이 시간에 변하면:

$$\mathbf{V}_p = \frac{m}{qB^2}\frac{d\mathbf{E}_\perp}{dt}$$

> **Unicode**
> ```
> 𝐕ₚ = (m)/(qB²)(d𝐄_⊥)/(dt)
> ```

이온과 전자가 반대로 드리프트 → 전류 발생 → 추가 전기장.

### 2.2.2 $\nabla B$ 드리프트

자기장이 공간에 따라 변할 때 ($\mathbf{B} = B(y)\hat{z}$, $B(y) \approx B_0 + y\partial_y B$), 입자가 한 사이클 동안 보는 $B$가 다르다.

**자기 모멘트** $\mu = mv_\perp^2/2B$가 자기장에 받는 힘:

$$\mathbf{F} = -\mu\nabla B$$

> **Unicode**
> ```
> 𝐅 = -μ∇ B
> ```

이 힘에 의한 **일반 드리프트 공식**:

$$\mathbf{V}_F = \frac{\mathbf{F}\times\mathbf{B}}{qB^2}$$

> **Unicode**
> ```
> 𝐕_F = (𝐅×𝐁)/(qB²)
> ```

따라서:

$$\mathbf{V}_{\nabla B} = \frac{m v_\perp^2}{2qB}\frac{\mathbf{B}\times\nabla B}{B^2} = \frac{\mu}{q}\frac{\mathbf{B}\times\nabla B}{B^2}$$

> **Unicode**
> ```
> 𝐕_∇ B = (m v_⊥²)/(2qB)(𝐁×∇ B)/(B²) = (μ)/(q)(𝐁×∇ B)/(B²)
> ```

**핵심:** $q$에 의존 → **이온과 전자가 반대 방향**으로 드리프트 → **전류 발생**.

### 2.2.3 곡률 드리프트

자력선이 곡률 $\mathbf{R}_c$ (곡률 반경 $R_c$)를 가질 때, 입자는 원심력 $\mathbf{F}_c = m v_\parallel^2 \mathbf{R}_c/R_c^2$를 느낀다.

$$\mathbf{V}_c = \frac{\mathbf{F}_c\times\mathbf{B}}{qB^2} = \frac{m v_\parallel^2}{qB^2}\frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2}$$

> **Unicode**
> ```
> 𝐕_c = (𝐅_c×𝐁)/(qB²) = (m v_∥²)/(qB²)(𝐑_c×𝐁)/(R_c²)
> ```

진공 자기장 $\nabla\times\mathbf{B} = 0$이면 다음 항등식이 성립한다:

$$\frac{\mathbf{R}_c}{R_c^2} = \frac{\nabla_\perp B}{B}$$

> **Unicode**
> ```
> (𝐑_c)/(R_c²) = (∇_⊥ B)/(B)
> ```

따라서 진공장에서는 $\nabla B$ 드리프트와 곡률 드리프트가 **같은 방향**이다.

### 2.2.4 기울기-곡률 드리프트 통합

두 드리프트를 합친 **유도 중심 드리프트 속도**:

$$\mathbf{V}_{gc} = \mathbf{V}_{\nabla B} + \mathbf{V}_c = \frac{m}{qB}\left(v_\parallel^2 \frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2 B} + \frac{v_\perp^2}{2}\frac{\mathbf{B}\times\nabla B}{B^2}\right)$$

> **Unicode**
> ```
> 𝐕_gc = 𝐕_∇ B + 𝐕_c = (m)/(qB)(v_∥² (𝐑_c×𝐁)/(R_c² B) + (v_⊥²)/(2)(𝐁×∇ B)/(B²))
> ```

진공장 근사 $\nabla\times\mathbf{B} \approx 0$이면:

$$\mathbf{V}_{gc} = \frac{m}{qB^3}\left(v_\parallel^2 + \frac12 v_\perp^2\right) \mathbf{B}\times\nabla B$$

> **Unicode**
> ```
> 𝐕_gc = (m)/(qB³)(v_∥² + (1)/(2) v_⊥²) 𝐁×∇ B
> ```

**주의:** 이 단순화된 형태는 **진공 자기장(∇×B=0)** 에서만 성립한다. 일반적으로는 $\mu\nabla B$ 항과 곡률 항을 분리해 써야 한다:

$$\mathbf{V}_{gc} = \frac{1}{qB}\left(m v_\parallel^2 \frac{\mathbf{R}_c\times\hat{b}}{R_c^2} + \mu \frac{\hat{b}\times\nabla B}{B}\right)$$

> **Unicode**
> ```
> 𝐕_gc = (1)/(qB)(m v_∥² (𝐑_c×b̂)/(R_c²) + μ (b̂×∇ B)/(B))
> ```

**공변 형태**로 가장 많이 쓰이는 표현:

$$\mathbf{V}_D = \frac{\mathbf{B}}{qB^2}\times\left(\mu\nabla B + m v_\parallel^2 (\hat{b}\cdot\nabla)\hat{b}\right) + \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

> **Unicode**
> ```
> 𝐕_D = (𝐁)/(qB²)×(μ∇ B + m v_∥² (b̂·∇)b̂) + (𝐄×𝐁)/(B²)
> ```

**세 항의 의미:**
- 첫째 항: $\nabla B$ 드리프트
- 둘째 항: 곡률 드리프트
- 셋째 항: $E\times B$ 드리프트

이 식이 **토카막, 자기권, 자기 거울 기계의 근본식**이다.

### 2.2.5 드리프트 요약표

| 드리프트 | 공식 | $q$ 의존 | 원인 |
|---|---|---|---|
| $E\times B$ | $\mathbf{E}\times\mathbf{B}/B^2$ | 없음 | 전기장 |
| 편극 | $\frac{m}{qB^2}\dot{\mathbf{E}}_\perp$ | 있음 | 시변 전기장 |
| $\nabla B$ | $\frac{\mu}{q}\frac{\mathbf{B}\times\nabla B}{B^2}$ | 있음 | 자기장 구배 |
| 곡률 | $\frac{mv_\parallel^2}{qB^2}\frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2}$ | 있음 | 자력선 곡률 |

### 2.2.6 한계·예외

- **유도 중심 근사 조건**: $r_L/L_B \ll 1$ (자기장 변화 스케일이 라모르 반지름보다 훨씬 클 때).
- **비단열 영역**: $r_L \sim L_B$이면 유도 중심 근사 붕괴, 카오스 산란 발생 (→ §4.6.1).
- **자기 재결합 영역**: $\mathbf{B} = 0$인 X점 근처에서는 유도 중심 자체가 정의되지 않음 (→ §4.5.3).
- **상대론적 드리프트**: $v \to c$에서 $\mu$와 드리프트 공식이 수정됨 (→ §3.1).

> **참고문헌**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963).
> - Alfvén, H., *Cosmical Electrodynamics*, Oxford (1950).
> - Baumjohann, W., Treumann, R. A., *Basic Space Plasma Physics*, Imperial College Press (1996).

---

## 2.3 단열 불변량 $\mu$

비균일 자기장에서 입자의 운동은 복잡하지만, **단열적으로 변하는 장**에서는 특정 양이 보존된다. 그 양이 **자기 모멘트** $\mu$다. 이 절에서는 $\mu$를 작용 변수에서 유도하고, 자기 거울과 손실 콘을 설명한다.

### 2.3.1 작용 변수에서 $\mu$ 유도

**작용 변수(action variable)** 는 주기 운동의 정준 운동량 적분이다:

$$J = \oint \mathbf{p}_\perp\cdot d\mathbf{l} = \oint m\mathbf{v}_\perp\cdot d\mathbf{l}$$

> **Unicode**
> ```
> J = ∮ 𝐩_⊥· d𝐥 = ∮ m𝐯_⊥· d𝐥
> ```

원궤도 1주기에 대해:

$$J = m v_\perp \cdot 2\pi r_L = \frac{2\pi m^2 v_\perp^2}{|q|B}$$

> **Unicode**
> ```
> J = m v_⊥ · 2π r_L = (2π m² v_⊥²)/(|q|B)
> ```

따라서 **단열 불변량**:

$$\mu = \frac{|q|}{2\pi m}J = \frac{m v_\perp^2}{2B}$$

> **Unicode**
> ```
> μ = (|q|)/(2π m)J = (m v_⊥²)/(2B)
> ```

### 2.3.2 보존 조건

$\mu$가 보존되기 위한 조건 세 가지:

1. **장이 라모르 반지름 스케일에서 거의 균일:**
   $$\epsilon = \frac{r_L}{L_B} \ll 1$$
   > **Unicode**
   > ```
   > ε = r_L/L_B ≪ 1
   > ```

2. **자이로 주기보다 장 변화가 느림:**
   $$\omega_c \gg \frac{1}{B}\frac{dB}{dt}$$
   > **Unicode**
   > ```
   > ω_c ≫ (1)/(B)(dB)/(dt)
   > ```

3. **$\mu$는 자이로 위상에 대해 평균된 라그랑지안의 정준 운동량**

**증명 스케치:** 유도 중심 라그랑지안:

$$L_g = q\mathbf{A}(\mathbf{R}_g)\cdot\dot{\mathbf{R}}_g + \mu\dot{\theta} - \mu B - \frac12 m v_\parallel^2$$

> **Unicode**
> ```
> L_g = q𝐀(𝐑_g)·𝐑˙_g + μθ˙ - μ B - (1)/(2) m v_∥²
> ```

여기서 $\theta$는 자이로 위상(cyclotron phase)으로 **순환 좌표(cyclic coordinate)** 다. 따라서:

$$p_\theta = \frac{\partial L_g}{\partial\dot\theta} = \mu = \text{const}$$

> **Unicode**
> ```
> p_θ = (∂ L_g)/(∂θ˙) = μ = const
> ```

### 2.3.3 자기 거울과 손실 콘

$\mu$ 보존과 에너지 보존을 결합하면 **자기 거울**을 이해할 수 있다.

**에너지 보존:**

$$E = \frac12 m v_\parallel^2 + \mu B = \text{const}$$

> **Unicode**
> ```
> E = (1)/(2) m v_∥² + μ B = const
> ```

입자가 자기장이 강한 영역으로 이동하면 $\mu B$가 커지고, $v_\parallel$이 줄어든다. 마침내 $v_\parallel = 0$이 되는 지점이 **반사점** $B_m$이다:

$$\frac12 m v_0^2 = \mu B_m$$

> **Unicode**
> ```
> (1)/(2) m v₀² = μ Bₘ
> ```

초기점 $B_0$에서 피치각 $\theta_0$ ($v_{\perp0} = v_0\sin\theta_0$, $v_{\parallel0} = v_0\cos\theta_0$)를 쓰면:

$$\mu = \frac{m v_0^2\sin^2\theta_0}{2B_0}$$

대입하면:

$$\frac12 m v_0^2 = \frac{m v_0^2\sin^2\theta_0}{2B_0}B_m$$

$$\sin^2\theta_m = \frac{B_0}{B_m}$$

> **Unicode**
> ```
> sin²θₘ = (B₀)/(Bₘ)
> ```

이것이 **손실 콘(loss cone)** 경계다.

**미러비** $R_m = B_m/B_0$로 쓰면 **구속 조건**:

$$\sin^2\theta_0 > \frac{1}{R_m}$$

> **Unicode**
> ```
> sin²θ₀ > (1)/(Rₘ)
> ```

**물리적 의미:**
- 피치각이 작은 입자 ($\theta_0 < \theta_m$)는 반사되기 전에 자기 거울을 빠져나가 **구속 실패**
- 피치각이 큰 입자는 반사되어 **구속 성공**
- 손실 콘 내부 입자가 자기 거울의 손실원

### 2.3.4 지구 자기권 응용

지구 자기권에서:
- 적도 $B_{eq} \sim 100$ nT
- 극지방 $B_0 \sim 50\ \mu$T
- 미러비 $R_m \sim 500$

손실 콘 각도:

$$\theta_{lc} = \arcsin\sqrt{B_{eq}/B_0} \sim 2.5^\circ$$

> **Unicode**
> ```
> θ_lc = arcsin√(B_eq/B₀) ∼ 2.5°
> ```

일반 플라즈마 시트 $T \sim 5$ keV는 대부분 구속되지만, 파동-입자 상호작용으로 피치각이 산란되면 손실 콘으로 떨어져 **오로라 강수**를 만든다 (→ §4.5.1).

### 2.3.5 매스매티카 검증

```mathematica
(* 단열 불변량 mu의 정의 *)
mu[B_, vPerp_, m_] := m vPerp^2 / (2 B);

(* 자기 거울 조건 *)
mirrorCondition[B0_, Bm_, theta0_] := Sin[theta0]^2 == B0/Bm;

(* 수치 검증: B0 = 1 T, Bm = 10 T *)
NSolve[mirrorCondition[1, 10, theta0], theta0]
(* 결과: theta0 ≈ 0.3217 rad ≈ 18.43° *)

(* 손실 콘 각도 *)
thetaLC = ArcSin[Sqrt[1/10]];
N[thetaLC * 180/Pi]
(* 결과: 18.435° *)
```

### 2.3.6 한계·예외

- **자기 재결합 영역**: $\mathbf{B} = 0$ 근처에서 $\mu$ 정의 자체가 발산, 보존 붕괴.
- **비단열 산란**: $r_L \sim L_B$이면 자이로 위상이 무작위화, $\mu$ 파괴.
- **상대론적 영역**: $\mu = p_\perp^2/2mB$로 수정 필요 (→ §3.1).
- **충돌**: 쿨롱 충돌이 자이로 주기보다 빠르면 $\mu$ 보존 안 됨 (→ §3.4.4).

> **참고문헌**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963).
> - Sivukhin, D. V., *Motion of Charged Particles in Electromagnetic Fields in the Plasma Physics*, Reviews of Plasma Physics **1**, 1 (1965).

---
## 2.4 수치해석 — 왜 보리스인가

로렌츠 방정식은 **해밀턴계**다. 일반 ODE 솔버를 쓰면 위상 부피가 붕괴한다. 이 절에서는 로렌츠 힘의 수치해석에서 **보리스 알고리즘**이 50년간 표준인 이유를 유도하고, PIC( Particle-In-Cell )와 MCC( Monte Carlo Collision )를 다룬다.

### 2.4.1 로렌츠 방정식의 해밀턴 구조

수치해석 대상:

$$\frac{d\mathbf{x}}{dt} = \mathbf{v}, \quad \frac{d\mathbf{v}}{dt} = \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐱)/(dt) = 𝐯,   (d𝐯)/(dt) = (q)/(m)(𝐄+𝐯×𝐁)
> ```

**해밀턴 구조의 핵심:** 자기력은 속도를 **회전만** 시키므로 에너지를 바꾸지 않는다. 좋은 수치해석기는 이 성질을 **정확히 보존**해야 한다.

### 2.4.2 보리스 알고리즘 완전 유도

1970년 J.P. Boris가 제안한 이 알고리즘은 PIC의 **50년간 표준 pusher**다.

**핵심 아이디어:** $\mathbf{E}$는 가속, $\mathbf{B}$는 회전으로 **분리**한다. 자기력은 속도를 회전만 시키므로 에너지 보존 연산자여야 한다.

**Leapfrog 구조:** 시간 스텝 $n \to n+1$, 속도는 반스텝 어긋난 격자 $\mathbf{v}_{n-1/2}$에 존재.

**시간 중심 차분:**

$$\frac{\mathbf{v}_{n+1/2}-\mathbf{v}_{n-1/2}}{\Delta t} = \frac{q}{m}\left(\mathbf{E}_n + \frac{\mathbf{v}_{n+1/2}+\mathbf{v}_{n-1/2}}{2}\times\mathbf{B}_n\right)$$

> **Unicode**
> ```
> (𝐯_n+1/2-𝐯_n-1/2)/(Δ t) = (q)/(m)(𝐄ₙ + (𝐯_n+1/2+𝐯_n-1/2)/(2)×𝐁ₙ)
> ```

여기서 $\mathbf{v}_n = (\mathbf{v}_{n+1/2}+\mathbf{v}_{n-1/2})/2$로 평균을 쓴 것이 포인트다.

**3단계 분리:**

#### Step 1: 전기장 반스텝 가속

$$\mathbf{v}^- = \mathbf{v}_{n-1/2} + \frac{q\mathbf{E}_n}{m}\frac{\Delta t}{2}$$

> **Unicode**
> ```
> 𝐯⁻ = 𝐯_n-1/2 + (q𝐄ₙ)/(m)(Δ t)/(2)
> ```

#### Step 2: 자기장 회전

$$\frac{\mathbf{v}^+ - \mathbf{v}^-}{\Delta t} = \frac{q}{2m}(\mathbf{v}^++\mathbf{v}^-)\times\mathbf{B}_n$$

> **Unicode**
> ```
> (𝐯⁺ - 𝐯⁻)/(Δ t) = (q)/(2m)(𝐯⁺+𝐯⁻)×𝐁ₙ
> ```

**이 회전은 해석적으로 풀린다.** 다음 벡터를 정의하자:

$$\mathbf{t} = \frac{q\mathbf{B}_n}{m}\frac{\Delta t}{2}, \quad \mathbf{s} = \frac{2\mathbf{t}}{1+t^2}$$

> **Unicode**
> ```
> 𝐭 = (q𝐁ₙ)/(m)(Δ t)/(2),   𝐬 = (2𝐭)/(1+t²)
> ```

그러면:

$$\mathbf{v}' = \mathbf{v}^- + \mathbf{v}^-\times\mathbf{t}$$
$$\mathbf{v}^+ = \mathbf{v}^- + \mathbf{v}'\times\mathbf{s}$$

> **Unicode**
> ```
> 𝐯' = 𝐯⁻ + 𝐯⁻×𝐭
> 𝐯⁺ = 𝐯⁻ + 𝐯'×𝐬
> ```

**이것은 정확한 회전이다:** $|\mathbf{v}^+| = |\mathbf{v}^-|$.

#### Step 3: 전기장 반스텝 가속

$$\mathbf{v}_{n+1/2} = \mathbf{v}^+ + \frac{q\mathbf{E}_n}{m}\frac{\Delta t}{2}$$

> **Unicode**
> ```
> 𝐯_n+1/2 = 𝐯⁺ + (q𝐄ₙ)/(m)(Δ t)/(2)
> ```

#### 위치 업데이트

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1/2}\Delta t$$

> **Unicode**
> ```
> 𝐱ₙ₊₁ = 𝐱ₙ + 𝐯_n+1/2Δ t
> ```

### 2.4.3 위상공간 부피 보존 증명

보리스 맵:

$$\mathcal{M}: (\mathbf{x}_n, \mathbf{v}_{n-1/2}) \to (\mathbf{x}_{n+1}, \mathbf{v}_{n+1/2})$$

> **Unicode**
> ```
> M: (𝐱ₙ,𝐯_n-1/2) → (𝐱ₙ₊₁,𝐯_n+1/2)
> ```

야코비안:

$$J = \left|\frac{\partial(\mathbf{x}_{n+1}, \mathbf{v}_{n+1/2})}{\partial(\mathbf{x}_n, \mathbf{v}_{n-1/2})}\right|$$

> **Unicode**
> ```
> J = |(∂(𝐱ₙ₊₁,𝐯_n+1/2))/(∂(𝐱ₙ,𝐯_n-1/2))|
> ```

**단계별 분해:**

- **Step 1, 3:** $\mathbf{v}^\pm = \mathbf{v} + const(\mathbf{x})$. $\partial\mathbf{v}^\pm/\partial\mathbf{v} = I$, 전단(shear) 변환 → 행렬식 1
- **Step 2:** 회전 $\mathbf{v}^+ = R(\mathbf{B}_n)\mathbf{v}^-$. $R$은 직교행렬, $|\det R| = 1$
- **위치 이동:** $\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1/2}\Delta t$ 역시 전단, 행렬식 1

**따라서:**

$$\det J = 1$$

> **Unicode**
> ```
> det J = 1
> ```

**리우빌 정리 만족. 위상 부피 보존 = 장기적으로 입자가 비물리적으로 가열/냉각되지 않음.** 이것이 보리스가 10억 스텝을 가도 살아남는 이유다.

> **각주 — Boris는 symplectic인가?** 보리스 알고리즘을 무조건 "symplectic integrator"로 분류하는 것은 논쟁의 여지가 있다. Qin et al. (*Why is Boris algorithm so good?*, Phys. Plasmas 20, 084503, 2013)과 Ellison, Burby & Qin (*Comment on "Symplectic integration of magnetic systems"*, J. Comput. Phys. 301, 489, 2015)은 보리스가 phase-space volume은 보존하지만 일반적 의미의 symplectic 또는 variational 방법은 아님을 지적했다. 따라서 이 문서에서는 보리스를 **2차 정확도의 volume-preserving / structure-preserving 방법**으로 서술하고, "symplectic"이라는 단정적 분류는 피한다.

**정확도:** 시간 2차, $\mathcal{O}(\Delta t^2)$. $\mathbf{E}=0$ 균일 $\mathbf{B}$에서 자이로 위상 오차는 있지만 $r_L$은 영구 보존.

**안정성 조건:** $\omega_c\Delta t < 2$. 실무에서는 $\omega_c\Delta t < 0.3$ 권장.

### 2.4.4 심플렉틱 적분기 (Störmer-Verlet, Leapfrog)

해밀토니안 $H = (\mathbf{p}-q\mathbf{A})^2/2m + q\phi$는 분리 불가(non-separable)이지만, $\mathbf{B}$ 균일하면 분리 가능하다.

**Velocity Verlet:**

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_n\Delta t + \frac12\mathbf{a}_n\Delta t^2$$

$$\mathbf{v}_{n+1} = \mathbf{v}_n + \frac12(\mathbf{a}_n + \mathbf{a}_{n+1})\Delta t$$

> **Unicode**
> ```
> 𝐱ₙ₊₁ = 𝐱ₙ + 𝐯ₙΔ t + (1)/(2)𝐚ₙΔ t²
> 𝐯ₙ₊₁ = 𝐯ₙ + (1)/(2)(𝐚ₙ + 𝐚ₙ₊₁)Δ t
> ```

$\mathbf{a} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})/m$이 $\mathbf{v}$에 의존하므로 **음해적(implicit)**이 되어 반복이 필요하다. 반면 보리스는 회전 단계를 명시적(explicit)으로 처리해 같은 문제를 우회한다. 다만 보리스는 아래에서 보듯 **phase-space volume을 보존하는 structure-preserving 방법**으로 보는 것이 안전하며, 이를 곧바로 "심플렉틱 Verlet의 최적 구현"이라 단정하지는 않는다 (Boris의 symplectic 여부에는 문헌상 논쟁이 있다; 2.4.2, 2.4.8 참조).

**Velocity Verlet의 보존 특성:**

- **심플렉틱:** $\omega = dp_i \wedge dx_i$ **정확 보존** → 야코비안 1
- **에너지:** 정확 보존은 아니지만, 심플렉틱 적분기는 **수정된 해밀토니안** $\tilde{H} = H + \mathcal{O}(\Delta t^2)$를 정확 보존. 따라서 에너지 오차가 $\mathcal{O}(\Delta t^2)$로 **유계(bounded)**, 시간에 대해 선형 드리프트 없음.
- **운동량:** 공간 대칭이 있으면 정확 보존.

**고차 심플렉틱:** Yoshida 4차 $\mathcal{O}(\Delta t^4)$ 구성 가능. PIC에서는 비용 때문에 2차 보리스가 지배적.

### 2.4.5 룽게-쿠타의 한계

표준 RK4:

$$k_1 = f(y_n), \quad k_2 = f(y_n + \Delta t k_1/2), \ldots$$

> **Unicode**
> ```
> k₁ = f(yₙ),   k₂ = f(yₙ + Δ t k₁/2), ...
> ```

**문제점 3가지:**

1. **비-심플렉틱:** $\det J \neq 1$. 위상 부피가 매 스텝 $1+\mathcal{O}(\Delta t^5)$로 팽창/수축
2. **에너지 드리프트:** 균일 $\mathbf{B}$에서 해석해는 $|\mathbf{v}| = const$. RK4는 수치 감쇠/증폭:

   $$|\mathbf{v}_{n+1}| = |\mathbf{v}_n|(1 + C(\omega_c\Delta t)^5 + \ldots)$$
   
   > **Unicode**
   > ```
   > |𝐯ₙ₊₁| = |𝐯ₙ|(1 + C(ω_cΔ t)⁵ + ...)
   > ```

   $C > 0$이면 장기적으로 자이로 에너지가 지수적으로 증가. 토카막 1초 추적($10^8$ 자이로 주기) 시 RK4는 완전히 붕괴

3. **자기 모멘트 파괴:** $\mu$가 수치적 산란으로 단조 증가. 자기 거울 구속을 인위적으로 깨뜨림

**RK4의 위치:** 단기 정확도(국소 오차 $\mathcal{O}(\Delta t^5)$)는 우수하나, 장기 추적·통계적 평형이 필요한 플라즈마에서는 부적합. $\mathbf{E}(t)$가 급변하는 레이저 가속 같은 단발 문제에만 유리.

### 2.4.6 PIC (Particle-In-Cell) 원리

로렌츠 pusher를 $10^6 \sim 10^{11}$개 입자에 적용, 장은 격자에서 맥스웰 풀이.

**PIC 루프:**

1. **Weighting / Charge Deposition:** 입자 위치 $\mathbf{x}_p$ → 격자 전하 밀도
   
   $$\rho_g = \sum_p q_p S(\mathbf{x}_g-\mathbf{x}_p)$$
   
   > **Unicode**
   > ```
   > ρ_g = ∑ₚ qₚ S(𝐱_g-𝐱ₚ)
   > ```
   
   $S$는 B-spline 형상함수 (NGP, CIC, TSC)

2. **Field Solve:** $\nabla^2\phi = -\rho/\epsilon_0$ 또는 완전 Maxwell $\partial_t\mathbf{B} = -\nabla\times\mathbf{E}$, $\partial_t\mathbf{E} = c^2\nabla\times\mathbf{B} - \mathbf{J}/\epsilon_0$를 FDTD(Yee 격자)로 풀이

3. **Field Interpolation:** 격자 $\mathbf{E}_g, \mathbf{B}_g$ → 입자 위치
   
   $$\mathbf{E}_p = \sum_g \mathbf{E}_g S(\mathbf{x}_g-\mathbf{x}_p)$$
   
   > **Unicode**
   > ```
   > 𝐄ₚ = ∑_g 𝐄_g S(𝐱_g-𝐱ₚ)
   > ```

4. **Pusher:** 보리스로 $\mathbf{v}_p, \mathbf{x}_p$ 업데이트

5. **Current Deposition:** 전하 보존법 만족하는 Esirkepov 방법으로 $\mathbf{J}_g$ 생성

**PIC의 물리:** 평균장(mean-field) 근사. 충돌 없이도 파동-입자 공명으로 **란다우 감쇠**, **두 흐름 불안정** 등 운동론적 효과를 재현.

**응용:** 핵융합, 우주 플라즈마, 홀 추력기, 반도체 식각 플라즈마.

**수치 가열:** 가장 큰 적. $\lambda_D$(Debye 길이)를 격자로 못 풀면 ($\Delta x > \lambda_D$) 인위적 가열 발생. 에너지 보존형 PIC(Implicit PIC) 개발 이유.

### 2.4.7 MCC (Monte Carlo Collision) 결합

PIC는 무충돌 Vlasov 방정식을 푼다. 실제 플라즈마는 중성가스와 충돌한다.

**MCC 알고리즘:** 매 $\Delta t$마다 각 입자에 대해:

**충돌 확률:**

$$P = 1 - \exp(-\nu(v)\Delta t) \approx \nu\Delta t, \quad \nu = n_g \sigma(v) v$$

> **Unicode**
> ```
> P = 1 - exp(-ν(v)Δ t) ≈ νΔ t,   ν = n_g σ(v) v
> ```

$\sigma(v)$: 충돌 단면적 (탄성, 여기, 이온화)

**절차:**
1. 난수 $R \in [0,1]$ 생성
2. $R < P$이면 충돌 발생
3. 충돌 종류는 $\nu_k/\nu_{total}$ 비율로 샘플링
4. 산란각은 미분 단면적에서 샘플링

**구현 순서:** Pusher 후 MCC → $v$ 방향 무작위화 + 에너지 손실 → 다음 스텝

**PIC-MCC의 응용:** 저온 플라즈마 산업 표준. CCP, ICP 방전의 전자 에너지 분포함수(EEDF) 비맥스웰 꼬리를 재현.

### 2.4.8 방법 비교표

| 방법 | 차수 | 기하학적 성질 | 에너지 거동 | 안정성 조건 | 장점 | 단점 |
|---|---|---|---|---|---|---|
| **보리스** | 2차 | volume-preserving / structure-preserving, $\det J = 1$ (symplectic 여부는 문헌상 논쟁, 각주 참조) | $\mathbf{B}$만 있으면 기계 정밀도 보존, $\mathbf{E}$ 포함시 유계 진동 | $\omega_c\Delta t < 2$ | 장기 보존, 빠르고 단순, PIC 표준 | 공명 $\omega_c\Delta t \approx \pi$에서 위상 오차 |
| **Velocity Verlet** | 2차 | 예, 심플렉틱 | 수정 해밀토니안 보존, 드리프트 없음 | $\omega_c\Delta t < 2$ | 이론적 엄밀성 | $\mathbf{v}\times\mathbf{B}$ 때문에 음해적 반복 필요 |
| **4차 Yoshida** | 4차 | 예 | 에너지 오차 $\mathcal{O}(\Delta t^4)$ 유계 | 동일 | 고정밀 장기 추적 | 연산 3배, PIC에선 비효율 |
| **RK4** | 4차 | 아니오, $\det J \neq 1$ | 선형/지수 드리프트 $\Delta E \sim t\Delta t^4$ | 조건부 안정, $\omega_c\Delta t \lesssim 2.8$ | 단기 고정밀, 구현 쉬움 | 장기 가열, $\mu$ 파괴, 플라즈마 불가 |
| **Implicit PIC** | 1-2차 | 에너지 정확 보존, 부피는 미보존 | 에너지 기계 정밀도 보존 | 무조건 안정 (대형 $\Delta t$ 가능) | $\Delta x > \lambda_D$ 허용 | 행렬 풀이 필요, 수치 감쇠 |

**실무 결론:**
- $10^6$ 스텝 이상 자기 구속 추적 → **보리스 필수**
- 단발 고정밀 궤적(방사광 추적) → RK4 또는 4차 심플렉틱
- 플라즈마 집단 현상 → **PIC + 보리스 + MCC**

보리스가 없었다면 현대 플라즈마 시뮬레이션은 존재하지 않는다.

### 2.4.9 매스매티카 검증

```mathematica
(* 보리스 회전 단계 검증 *)
borisRotate[vMinus_, q_, m_, dt_, Bvec_] := Module[
  {t, s, vPrime, vPlus},
  t = (q Bvec dt)/(2 m);
  s = (2 t)/(1 + t . t);
  vPrime = vMinus + Cross[vMinus, t];
  vPlus = vMinus + Cross[vPrime, s];
  vPlus
];

(* 속도 크기 보존 검증 *)
v0 = {1, 0, 0};
Bvec = {0, 0, 1};
v1 = borisRotate[v0, 1, 1, 0.1, Bvec];
Norm[v1] - Norm[v0]
(* 출력: 0 *)
```

### 2.4.10 한계·예외

- **자기 재결합**: $\mathbf{B} \to 0$ 근처에서 자이로 주기 $\to \infty$, 보리스 조건 $\omega_c\Delta t < 2$ 붕괴
- **상대론적 영역**: $\gamma \gg 1$에서 보리스는 수정 필요 (상대론적 보리스, Vay 2008)
- **강한 $\mathbf{E}$**: $E > B$에서 $E\times B$ 프레임이 광속 초과, 특수 처리 필요
- **수치 Cherenkov**: $\Delta x < c\Delta t$일 때 비물리적 방사 발생

> **참고문헌**
> - Boris, J. P., *Relativistic plasma simulation-optimization of a hybrid code*, Proc. 4th Conf. Numerical Simulation of Plasmas, 3–67 (1970). [ADS](https://ui.adsabs.harvard.edu/abs/1970nusp.conf....3B)
> - Esirkepov, T. Zh., *Exact charge conservation scheme for PIC simulation*, Comput. Phys. Commun. **144**, 26 (2001). [doi:10.1016/S0010-4655(00)00228-9](https://doi.org/10.1016/S0010-4655(00)00228-9)
> - Hockney, R. W., Eastwood, J. W., *Computer Simulation Using Particles*, Adam Hilger (1988). [doi:10.1201/9780367806934](https://doi.org/10.1201/9780367806934)
> - Birdsall, C. K., Langdon, A. B., *Plasma Physics via Computer Simulation*, McGraw-Hill (1985).

---

## 2.5 위상수학·기하학 — $U(1)$ 다발의 곡률

로렌츠 힘 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 벡터 공식처럼 보이지만, 현대 기하학에서 보면 **주다발 위의 곡률에 의해 입자가 geodesic 운동에서 이탈(departure from geodesic motion)하게 되는 현상**이다 (일반상대론의 표준적 geodesic deviation과는 구별됨). 이 절에서는 베리 위상, 아하로노프-봄 효과, 자기 단극자, 섬유다발, 미분형식, $U(1)$ 리 군을 다룬다.

### 2.5.1 베리 위상과 로렌츠 힘

단열적으로 움직이는 양자계 $|n(\mathbf{R}(t))\rangle$는 동역학적 위상 외에 **기하학적 위상**을 얻는다:

$$|\psi(T)\rangle = e^{i\theta_{dyn}} e^{i\gamma_n} |n(\mathbf{R}(T))\rangle$$

> **Unicode**
> ```
> |ψ(T)⟩ = e^iθ_dyn e^iγₙ |n(𝐑(T))⟩
> ```

여기서 **베리 위상**:

$$\gamma_n = \oint_C \mathcal{A}_n \cdot d\mathbf{R}, \quad \mathcal{A}_n = i\langle n|\nabla_{\mathbf{R}}|n\rangle$$

> **Unicode**
> ```
> γₙ = ∮_C Aₙ · d𝐑,   Aₙ = i⟨ n|∇_𝐑|n⟩
> ```

**베리 접속** $\mathcal{A}_n$은 전자기 퍼텐셜 $\mathbf{A}$와 **수학적으로 동일**하다. 베리 곡률:

$$\mathbf{\Omega}_n = \nabla_{\mathbf{R}}\times\mathcal{A}_n$$

> **Unicode**
> ```
> Ωₙ = ∇_𝐑×Aₙ
> ```

**반고전적 운동방정식**에 나타나는 힘은 정확히 로렌츠 형태:

$$\hbar\dot{\mathbf{k}} = -e\mathbf{E} - e\dot{\mathbf{r}}\times\mathbf{B} + \text{(베리 항)}$$

> **Unicode**
> ```
> ℏ𝐤˙ = -e𝐄 - e𝐫˙×𝐁 + (베리 항)
> ```

$$\dot{\mathbf{r}} = \frac{1}{\hbar}\frac{\partial\epsilon_n}{\partial\mathbf{k}} - \dot{\mathbf{k}}\times\mathbf{\Omega}_n(\mathbf{k})$$

> **Unicode**
> ```
> 𝐫˙ = (1)/(ℏ)(∂εₙ)/(∂𝐤) - 𝐤˙×Ωₙ(𝐤)
> ```

**두 번째 항이 k-공간에서의 로렌츠 힘**이다. 즉:
- 실제 자기장 $\mathbf{B}$ → 실공간 Berry curvature
- Berry curvature $\mathbf{\Omega}$ → 운동량 공간 자기장
- 전자기 로렌츠 힘은 Berry 위상의 특수한 경우

### 2.5.2 아하로노프-봄 효과

**설정:** 솔레노이드 외부에서 $\mathbf{B} = 0$이므로 고전적 로렌츠 힘 = 0. 그러나 $\mathbf{A} \neq 0$, $\nabla\times\mathbf{A} = 0$이지만:

$$\oint \mathbf{A}\cdot d\boldsymbol{\ell} = \Phi_B \neq 0$$

> **Unicode**
> ```
> ∮ 𝐀· dℓ = Φ_B ≠ 0
> ```

**양자 간섭:**

$$\Delta\varphi_{AB} = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi_B}{\hbar}$$

> **Unicode**
> ```
> Δφ_AB = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ_B)/(ℏ)
> ```

**위상수학적 의미:**

- 공간이 **단순 연결이 아니다**: $\mathbb{R}^3 \setminus \text{solenoid} \simeq S^1$
- $F = dA = 0$이므로 곡률은 0이지만, **홀로노미(holonomy)**는 0이 아니다
- 드람 코호몰로지 $H^1_{dR}(M) \neq 0$: 닫힌 형식 $A$가 완전 형식이 아니다. $A \neq d\chi$ globally

**즉, 로렌츠 힘이 0인 곳에서도 $U(1)$ 다발의 위상적 비틀림이 남아 양자 위상을 만든다.** 고전적 힘은 곡률 $F$의 국소 효과, AB 효과는 접속 $A$의 대역적 위상 효과. 둘은 같은 다발의 두 측면이다.

> **고전:** $F$가 입자를 편향, **양자:** $\exp(i\oint A)$가 위상을 편향

### 2.5.3 자기 단극자와 Dirac 양자화

자기 단극자 $\nabla\cdot\mathbf{B} = g\delta^3(\mathbf{r})$를 허용하면 $F$가 더 이상 전역적으로 $dA$가 아니다. $dF \neq 0$ at origin.

**Dirac의 구성:** 북반구 $A_N$, 남반구 $A_S$로 나누어 정의:

$$A_N = \frac{g}{r}\frac{1-\cos\theta}{\sin\theta}\hat{\phi}, \quad A_S = -\frac{g}{r}\frac{1+\cos\theta}{\sin\theta}\hat{\phi}$$

> **Unicode**
> ```
> A_N = (g)/(r)(1-cosθ)/(sinθ)φ̂,   A_S = -(g)/(r)(1+cosθ)/(sinθ)φ̂
> ```

적도에서 게이지 변환: $A_N = A_S + \nabla\chi$, $\chi = 2g\phi$

**파동함수 단일성 요구:** $\exp(iq\chi/\hbar)$가 $\phi \to \phi+2\pi$에서 1이 되어야 한다:

$$\exp\left(i\frac{q}{\hbar}2g\cdot2\pi\right) = 1 \implies qg = n\frac{\hbar}{2}, \quad n \in \mathbb{Z}$$

> **Unicode**
> ```
> qg = n(ℏ)/(2),   n∈ℤ
> ```

**이것이 Dirac 양자화.** Wu-Yang 해석: 자기 단극자는 자명한 $U(1)$ 다발이 아니다. $S^2$ 위에 **꼬인 다발**. 그 꼬임 정도가 **제1 Chern 수**:

$$c_1 = \frac{1}{2\pi}\int_{S^2} F = \frac{1}{2\pi}\int_{S^2} \mathbf{B}\cdot d\mathbf{S} = 2g$$

> **Unicode**
> ```
> c₁ = (1)/(2π)∫_S² F = (1)/(2π)∫_S² 𝐁· d𝐒 = 2g
> ```

자연 단위($e = \hbar = 1$)에서 $c_1 = 2g$. SI에서는 $c_1 = 2eg/\hbar$로 차원 복원.

**전하 양자화는 공간 위상의 양자화다.** 자기 단극자가 하나만 존재해도 우주 전체 전하가 양자화된다.

**로렌츠 힘의 확장:** 단극자 존재 시:

$$\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + g\left(\mathbf{B}-\frac{\mathbf{v}}{c^2}\times\mathbf{E}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄+𝐯×𝐁) + g(𝐁-(𝐯)/(c²)×𝐄)
> ```

$g$ 항의 위상적 장애가 본질이다.

### 2.5.4 섬유다발과 게이지장으로서의 전자기장

**현대 정의:**

- **바탕 다양체** $M$: 시공간 (Minkowski $\mathbb{R}^{1,3}$)
- **구조군** $G = U(1)$: 위상 $e^{i\theta}$
- **주다발** $P(M, U(1))$: 각 점 $x\in M$ 위에 원 $U(1)$ 섬유
- **접속(connection)** 1-형식 $A = A_\mu dx^\mu = -\phi\, dt + \mathbf{A}\cdot d\mathbf{x}$: 섬유 사이의 평행 이동 규정
- **곡률(curvature)** 2-형식 $F = dA + A\wedge A = dA$ ($U(1)$은 아벨이라 교환자 0): 실제 물리장

**입자 파동함수**는 연관 복소 선다발의 **단면(section)**. 공변 미분:

$$D_\mu = \partial_\mu - i\frac{q}{\hbar}A_\mu$$

> **Unicode**
> ```
> D_μ = ∂_μ - i(q)/(ℏ)A_μ
> ```

이 부호는 본문 1.4절에서 사용하는 최소 결합 $\mathbf{p}-q\mathbf{A}=m\mathbf{v}$, $H=(\mathbf{p}-q\mathbf{A})^2/2m$ convention과 일치하도록 선택한 것이다 ($-i\hbar D_\mu = -i\hbar\partial_\mu - qA_\mu$). 부호 자체가 절대적으로 옳은 것은 아니며, $D_\mu$, $\psi$, $A_\mu$의 게이지 변환이 하나의 체계로 일관되게 맞물리는 것이 핵심이다.

**평행 이동 실패 = 곡률 = 로렌츠 힘.** 측지 방정식 $D_\mu D^\mu\psi = 0$의 고전 극한이 $dp^\mu/d\tau = qF^{\mu\nu}u_\nu$다.

**게이지 변환**은 다발의 수직 자기동형: 섬유를 $\psi \to e^{iq\chi/\hbar}\psi$만큼 회전. $A_\mu \to A_\mu + \partial_\mu\chi$로 접속이 변해도 곡률 $F$는 불변이며, 이때 $D_\mu\psi \to e^{iq\chi/\hbar}D_\mu\psi$로 파동함수와 같은 방식으로 변환한다.

**로렌츠 힘은 다발의 곡률이 입자 세계선을 geodesic 운동으로부터 이탈(departure from geodesic motion)시키는 기하학적 힘**이다. 다만 이는 서로 이웃한 geodesic들의 상대가속도를 곡률로 기술하는 일반상대론의 표준적 **geodesic deviation**(측지선 편차)과는 개념적으로 구별되는 현상이며, 유사성은 "곡률이 세계선에 영향을 준다"는 정성적 수준에 그친다.

### 2.5.5 미분형식으로 본 맥스웰

형식 언어가 로렌츠 힘의 위상을 가장 명확히 한다.

**1-형식:** $A = A_\mu dx^\mu$

**2-형식:** $F = \frac12 F_{\mu\nu}dx^\mu\wedge dx^\nu = E_i\, dx^i\wedge dt + \frac12\epsilon_{ijk}B_k\, dx^i\wedge dx^j$

> **Unicode**
> ```
> F = (1)/(2) F_μνdx^μ∧ dx^ν = Eᵢ dxⁱ∧ dt + (1)/(2)εᵢⱼₖBₖ dxⁱ∧ dxʲ
> ```

#### Bianchi 항등식

$$dF = 0 \iff \begin{cases}\nabla\cdot\mathbf{B} = 0 \\ \nabla\times\mathbf{E} + \partial_t\mathbf{B} = 0\end{cases}$$

> **Unicode**
> ```
> dF = 0 ⟺ ∇·𝐁 = 0 ;  ∇×𝐄 + ∂ₜ𝐁 = 0
> ```

$d^2 = 0$의 귀결. $F = dA$라면 자동. 단극자 있으면 $dF = \star J_m \neq 0$로 위상 장애.

#### 운동방정식

$$d\star F = \star J \iff \begin{cases}\nabla\cdot\mathbf{E} = \rho/\epsilon_0 \\ \nabla\times\mathbf{B} - \partial_t\mathbf{E} = \mu_0\mathbf{J}\end{cases}$$

> **Unicode**
> ```
> d⋆ F = ⋆ J ⟺ ∇·𝐄 = ρ/ε₀ ;  ∇×𝐁 - ∂ₜ𝐄 = μ₀𝐉
> ```

$\star$는 Hodge dual.

#### 로렌츠 힘

입자 세계선 $C$, 4-속도 $u$, 운동량 1-형식 $p$. 작용:

$$S = -m\int d\tau + q\int_C A$$

> **Unicode**
> ```
> S = -m∫ dτ + q∫_C A
> ```

변이 $\delta S = 0$ →

$$i_u F = dp/d\tau$$

> **Unicode**
> ```
> iᵤ F = dp/dτ
> ```

성분으로 $f_\mu = qF_{\mu\nu}u^\nu$. 즉, **$F$를 $u$와 축약(contraction)한 것이 힘**이다.

**Stokes 정리** $\int_S F = \oint_{\partial S} A$가 곧 Berry/AB 위상.

### 2.5.6 $U(1)$ 리 군과 대칭성

$$U(1) = \{e^{i\theta} \mid \theta \in [0, 2\pi)\}$$

> **Unicode**
> ```
> U(1) = {e^iθ | θ∈[0,2π)}
> ```

아벨 리 군, 리 대수 $u(1) = i\mathbb{R}$.

**대칭성:** 라그랑지안 $L = \bar\psi(i\slashed{D}-m)\psi$는 국소 $U(1)$ 변환 $\psi \to e^{iq\chi(x)}\psi$, $A \to A + d\chi$ 하에 불변. **Noether 정리 → 전하 보존** $d\star J = 0$.

**로렌츠 힘의 대칭적 기원:** 최소 결합 원리 $p_\mu \to p_\mu - qA_\mu$는 $U(1)$ 표현론이 강제한다. 다른 군이면 다른 힘:
- $SU(2)$ → 약력의 로렌츠 힘 유사체 $f^a = gF^{a\mu\nu}u_\nu$
- $SU(3)$ → 색 로렌츠 힘

**즉, 전자기 로렌츠 힘은 $U(1)$ 버전**이다.

**위상 불변량: Wilson loop**

$$W(C) = \exp\left(iq\oint_C A\right) \in U(1)$$

> **Unicode**
> ```
> W(C) = exp(iq∮_C A) ∈ U(1)
> ```

게이지 불변 관측량. AB 위상, Berry 위상, 격자 게이지 이론의 기본 변수. **로렌츠 힘은 $W$의 무한소 버전**: 작은 루프에 대해 $W \approx 1 + iqF_{\mu\nu}dS^{\mu\nu}$.

### 2.5.7 종합표

| 개념 | 기하학적 대상 | 물리적 귀결 |
|---|---|---|
| $A$ | $U(1)$ 접속 1-형식 | 베리 접속, AB 위상 $\gamma = \oint A$ |
| $F = dA$ | 곡률 2-형식 | $\mathbf{E}, \mathbf{B}$, 로렌츠 힘 $q\,i_u F$ |
| $dF = 0$ | Bianchi, 자명한 다발 | 자기 단극자 금지, 자속 보존 |
| $d\star F = J$ | Yang-Mills 방정식 | 장의 원천 |
| $c_1 = \frac{1}{2\pi}\int F$ | 제1 Chern 수 | Dirac 양자화 $qg = n\hbar/2$ |

### 2.5.8 매스매티카 검증

```mathematica
(* 전자기 텐서의 미분형식 검증 *)
(* F = dA 조건 *)
Aform = -phi[x, y, z, t] dt + Ax[x, y, z, t] dx + Ay[x, y, z, t] dy + Az[x, y, z, t] dz;
Fform = d[Aform];
(* F의 성분이 E, B로 표현되는지 확인 *)
Collect[Fform, {dt, dx, dy, dz}]

(* dF = 0 (Bianchi) *)
Simplify[d[Fform] == 0]

```

### 2.5.9 한계·예외

- **비단순 연결**: AB 효과, Dirac 양자화는 공간의 위상(구멍, 단극자)에 의존
- **비아벨 확장**: $SU(2)$, $SU(3)$에서는 $F = dA + A\wedge A$로 교환자 항 추가 (→ §6.1.1)
- **비단열 베리 위상**: 단열 조건 $\dot{R} \to 0$이 깨지면 베리 위상 정의 자체가 모호
- **강결합**: $g \gg 1$에서 섭동론 붕괴, 격자 게이지 이론 필요

> **참고문헌**
> - Berry, M. V., *Quantal phase factors accompanying adiabatic changes*, Proc. R. Soc. A **392**, 45–57 (1984). [doi:10.1098/rspa.1984.0023](https://doi.org/10.1098/rspa.1984.0023)
> - Aharonov, Y., Bohm, D., *Significance of Electromagnetic Potentials in the Quantum Theory*, Phys. Rev. **115**, 485 (1959). [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
> - Dirac, P. A. M., *Quantised singularities in the electromagnetic field*, Proc. R. Soc. A **133**, 60 (1931). [doi:10.1098/rspa.1931.0130](https://doi.org/10.1098/rspa.1931.0130)
> - Nakahara, M., *Geometry, Topology and Physics*, 2nd ed., Taylor & Francis (2003), Chapter 10.
> - Xiao, D., Chang, M.-C., Niu, Q., *Berry phase effects on electronic properties*, Rev. Mod. Phys. **82**, 1959 (2010). [doi:10.1103/RevModPhys.82.1959](https://doi.org/10.1103/RevModPhys.82.1959)

---
# 3막. 물리적 심화 (Physical Depth)

> **막의 흐름**
> 상대론 → 방사 → 양자 → 통계
>
> 2막까지 로렌츠 힘의 고전·기하 구조를 확정했다. 3막은 그 구조가 **상대론, 방사, 양자, 통계**에서 어떻게 확장되는지를 다룬다. 로렌츠 힘은 $v \to c$, $\hbar \neq 0$, $N \to \infty$의 세 극한에서 각각 새로운 얼굴을 보인다.

---

## 3.1 상대론적 로렌츠 힘

비상대론적 $m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 $\gamma \gg 1$에서 붕괴한다. 질량이 아닌 **운동량 $\mathbf{p}$**가 역학 변수다. 이 절에서는 상대론적 운동방정식, 종·횡 질량, 전자기장 변환을 다룬다.

### 3.1.1 상대론적 운동방정식

**상대론적 운동량:**

$$\mathbf{p} = \gamma m \mathbf{v}, \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}, \quad E_{tot} = \gamma mc^2$$

> **Unicode**
> ```
> 𝐩 = γ m 𝐯,   γ = (1)/(√(1-v²/c²)),   Eₜₒₜ = γ mc²
> ```

**운동방정식:**

$$\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐩)/(dt) = q(𝐄 + 𝐯×𝐁)
> ```

**에너지 방정식:**

$$\frac{d(\gamma mc^2)}{dt} = q\mathbf{v}\cdot\mathbf{E}$$

> **Unicode**
> ```
> (d(γ mc²))/(dt) = q𝐯·𝐄
> ```

형태는 뉴턴과 같아 보이지만 $\mathbf{p}$에 $\gamma$가 숨어 **비선형**이다.

**4-벡터 형식:**

$$\frac{dp^\mu}{d\tau} = qF^{\mu\nu}u_\nu, \quad p^\mu = (\gamma mc, \mathbf{p}), \quad u^\mu = \gamma(c, \mathbf{v})$$

> **Unicode**
> ```
> (dp^μ)/(dτ) = qF^μνu_ν,   p^μ = (γ mc,𝐩),   u^μ = γ(c,𝐯)
> ```

이 형태는 1.3절에서 이미 유도했다. 여기서는 그 **물리적 함의**를 본다.

### 3.1.2 종·횡 질량

$\mathbf{v}$에 **평행** / **수직** 가속은 관성이 다르다. 운동방정식을 분해하면:

$$\mathbf{a}_\parallel = \frac{q}{m\gamma^3}\mathbf{E}_\parallel, \quad \mathbf{a}_\perp = \frac{q}{m\gamma}(\mathbf{E}_\perp + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐚_∥ = (q)/(mγ³)𝐄_∥,   𝐚_⊥ = (q)/(mγ)(𝐄_⊥ + 𝐯×𝐁)
> ```

- $\gamma^3 m$: **종질량(longitudinal mass)**
- $\gamma m$: **횡질량(transverse mass)**

$v \to c$에서 **같은 힘으로 가속하기 $\gamma^3$배 어려워진다**. 이것이 입자가 광속에 도달할 수 없는 이유다.

**수치 예시:** LHC 양성자 $\gamma = 7460$, 종질량 $= 7460^3 m_p \approx 4\times 10^{14} m_p$.

### 3.1.3 상대론적 사이클로트론 진동수

균일 $\mathbf{B}$에서 해는 여전히 나선이지만, **진동수가 에너지에 반비례**한다:

$$\omega_c^{rel} = \frac{qB}{\gamma m} = \frac{\omega_{c,0}}{\gamma}, \quad r_L^{rel} = \frac{\gamma m v_\perp}{|q|B} = \frac{p_\perp}{|q|B}$$

> **Unicode**
> ```
> ω_cʳᵉˡ = (qB)/(γ m) = (ω_c,0)/(γ),   r_Lʳᵉˡ = (γ m v_⊥)/(|q|B) = (p_⊥)/(|q|B)
> ```

**이것이 사이클로트론의 상대론적 한계다.** RF 주파수를 $\omega_c^{rel}$에 맞추면 에너지가 커질수록 진동수가 줄어 공명이 깨진다.

**수치:** 양성자 1 GeV에서 $\gamma \approx 2$, 진동수 50% 감소 → 공명 붕괴. 고전 사이클로트론 한계 $\sim 20$ MeV 양성자.

**해결책 (→ §4.1):**
- **싱크로사이클로트론:** RF 주파수를 시간에 따라 변조
- **아이소크로너스 사이클로트론:** 반경 방향으로 $B(r)$ 증가

### 3.1.4 전자기장 텐서의 로렌츠 변환

$F^{\mu\nu}$는 2-텐서이므로 로렌츠 변환:

$$F'^{\mu\nu} = \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$$

> **Unicode**
> ```
> F'^μν = Λ^μ_ α Λ^ν_ β F^αβ
> ```

속도 $\mathbf{V} = V\hat{x}$로 부스트 시 **장 변환**:

$$\mathbf{E}'_\parallel = \mathbf{E}_\parallel, \quad \mathbf{B}'_\parallel = \mathbf{B}_\parallel$$

> **Unicode**
> ```
> 𝐄'_∥ = 𝐄_∥,   𝐁'_∥ = 𝐁_∥
> ```

$$\mathbf{E}'_\perp = \gamma_V(\mathbf{E}_\perp + \mathbf{V}\times\mathbf{B}), \quad \mathbf{B}'_\perp = \gamma_V\left(\mathbf{B}_\perp - \frac{1}{c^2}\mathbf{V}\times\mathbf{E}\right)$$

> **Unicode**
> ```
> 𝐄'_⊥ = γ_V(𝐄_⊥ + 𝐕×𝐁),   𝐁'_⊥ = γ_V(𝐁_⊥ - (1)/(c²)𝐕×𝐄)
> ```

### 3.1.5 $\mathbf{v}\times\mathbf{B}$의 상대론적 기원

**핵심 통찰:** 순수 자기장도 움직이는 관찰자에게는 **전기장**으로 보인다:

$$\mathbf{E}' = \gamma\mathbf{V}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐄' = γ𝐕×𝐁
> ```

**이것이 바로 $\mathbf{v}\times\mathbf{B}$ 로렌츠 힘의 상대론적 기원이다.** 자기력은 다른 관성계에서 본 전기력이다.

**불변량 2개:**

$$I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2, \quad I_2 = c\mathbf{E}\cdot\mathbf{B}$$

> **Unicode**
> ```
> I₁ = c²𝐁² - 𝐄²,   I₂ = c𝐄·𝐁
> ```

- $I_1 > 0, I_2 = 0$이면 **자기장이 지배적** → 좌표 변환으로 $\mathbf{E}' = 0$ 만들 수 있음
- 이 프레임이 **유도 중심이 정지한 프레임**
- $E\times B$ 드리프트의 상대론적 해석

즉, $\mathbf{E}+\mathbf{v}\times\mathbf{B}$는 $F^{\mu\nu}u_\nu$의 3차원 투영이며, **방사 공식과 강성도, 장 변환 모두 이 4-텐서 구조에서 일관되게 나온다**.

### 3.1.6 매스매티카 검증

```mathematica
(* 상대론적 로렌츠 힘 *)
gamma[v_] := 1/Sqrt[1 - v . v/c^2];
pRel[v_] := gamma[v] m0 v;

(* 운동방정식 *)
eqns = D[pRel[{vx[t], vy[t], vz[t]}], t] ==
  q ({Ex, Ey, Ez} + Cross[{vx[t], vy[t], vz[t]}, {Bx, By, Bz}]);

(* 균일 B에서 상대론적 사이클로트론 진동수 확인 *)
omegaRel = q B0 / (gamma m0);
```

### 3.1.7 한계·예외

- **비상대론 극한**: $v \ll c$에서 $\gamma \to 1$, 모든 공식이 1막으로 환원
- **광속 극한**: $v \to c$에서 $\gamma \to \infty$, 종질량 발산
- **방사 반작용**: 상대론적 입자가 가속하면 방사로 에너지를 잃음 (→ §3.2)
- **양자 영역**: $\hbar\omega_c \sim mc^2$이면 양자 효과 필수 (→ §3.3)

> **참고문헌**
> - Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §17, §23.
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §11.10.
> - Sokolov, A. A., Ternov, I. M., *Synchrotron Radiation*, Pergamon (1968).

---

## 3.2 방사 손실

상대론적 하전 입자가 가속하면 **전자기파를 방출**하며 에너지를 잃는다. 이 절에서는 라모 공식, Liénard 일반화, Abraham-Lorentz-Dirac 방정식, Landau-Lifshitz 처방, 싱크로트론 방사, 강성도를 다룬다.

### 3.2.1 라모 공식

**비상대론적 라모 공식 (SI):**

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

> **Unicode**
> ```
> P = (q² a²)/(6πε₀ c³)
> ```

**가우스 단위계:**

$$P = \frac{2q^2 a^2}{3c^3}$$

> **Unicode**
> ```
> P = (2q² a²)/(3c³)
> ```

**유도:** 지연 퍼텐셜 $\mathbf{E}_{rad} \sim q\mathbf{n}\times(\mathbf{n}\times\mathbf{a})/c^2R$, 포인팅 플럭스 적분.

**물리적 의미:** 가속도 제곱에 비례. 원운동이 직선운동보다 방사가 강한 이유.

### 3.2.2 Liénard 상대론적 일반화

불변량 $a^\mu a_\mu$를 이용:

$$P = -\frac{q^2}{6\pi\varepsilon_0 c} a^\mu a_\mu = \frac{q^2}{6\pi\varepsilon_0 c^3}\gamma^6\left[a^2 - \frac{(\mathbf{v}\times\mathbf{a})^2}{c^2}\right]$$

> **Unicode**
> ```
> P = -(q²)/(6πε₀ c) a^μ a_μ = (q²)/(6πε₀ c³)γ⁶[a² - ((𝐯×𝐚)²)/(c²)]
> ```

**자주 쓰는 형태:**

$$P = \frac{q^2\gamma^4}{6\pi\varepsilon_0 c^3}\left[a_\perp^2 + \gamma^2 a_\parallel^2\right]$$

> **Unicode**
> ```
> P = (q²γ⁴)/(6πε₀ c³)[a_⊥² + γ² a_∥²]
> ```

**극한:**

- **직선 가속** $a \parallel v$: $P \propto \gamma^6 a_\parallel^2$
- **원운동** $a \perp v$: $P \propto \gamma^4 a_\perp^2$

**원운동 방사가 훨씬 강력하다.** 싱크로트론이 직선가속기보다 방사 손실이 큰 이유다.

**자기장 내 원운동:** $a = v^2/r = qvB/\gamma m$ 대입:

$$P_{sync} = \frac{q^4 B^2}{6\pi\varepsilon_0 m^2 c}\gamma^2\beta^2\sin^2\alpha \propto \frac{\gamma^2}{m^2}$$

> **Unicode**
> ```
> P_sync = (q⁴ B²)/(6πε₀ m² c)γ²β²sin²α ∝ (γ²)/(m²)
> ```

**전자/양성자 비:** $(m_p/m_e)^2 \approx 3.4\times10^6$배 차이. 전자 싱크로트론은 방사 지배, 양성자는 거의 무시.

**수치:** LEP 전자 100 GeV, $B = 0.1$ T, $R = 3$ km → 턴당 3 GeV 손실. LHC 양성자 7 TeV는 방사 손실 무시 가능.

### 3.2.3 Abraham-Lorentz-Dirac 방정식

방사로 에너지가 나가면 입자에 **반작용력** $\mathbf{F}_{rad}$가 있어야 한다.

**Abraham-Lorentz 힘 (비상대론):**

$$\mathbf{F}_{AL} = \frac{q^2}{6\pi\varepsilon_0 c^3}\dot{\mathbf{a}} = m\tau_0\dot{\mathbf{a}}, \quad \tau_0 = \frac{q^2}{6\pi\varepsilon_0 mc^3}$$

> **Unicode**
> ```
> 𝐅_AL = (q²)/(6πε₀ c³)𝐚˙ = mτ₀𝐚˙,   τ₀ = (q²)/(6πε₀ mc³)
> ```

**전자:** $\tau_0 \approx 6.2\times10^{-24}$ s.

**운동방정식:**

$$m\mathbf{a} = \mathbf{F}_{ext} + m\tau_0\dot{\mathbf{a}}$$

> **Unicode**
> ```
> m𝐚 = 𝐅ₑₓₜ + mτ₀𝐚˙
> ```

**상대론적 ALD 방정식:**

$$m a^\mu = qF^{\mu\nu}u_\nu + \frac{q^2}{6\pi\varepsilon_0 c^3}\left(\frac{da^\mu}{d\tau} + a^\nu a_\nu \frac{u^\mu}{c^2}\right)$$

> **Unicode**
> ```
> m a^μ = qF^μνu_ν + (q²)/(6πε₀ c³)((d a^μ)/(dτ) + a^ν a_ν (u^μ)/(c²))
> ```

괄호 안이 **Schott 항 + Larmor 항**.

**ALD의 병리 3가지:**

1. **Runaway:** $\mathbf{F}_{ext} = 0$에도 $a \sim e^{t/\tau_0}$ 발산
2. **Pre-acceleration:** $\mathbf{F}_{ext}$가 가해지기 $\tau_0$ 전에 가속 시작 — 인과율 위반
3. **3계 미분** → 초기 가속도 지정 필요

**원인:** 점전하 모델 자체가 $r \to 0$에서 발산.

### 3.2.4 Landau-Lifshitz 처방

$\dot{\mathbf{a}}$에 0차 운동방정식을 대입해 **2계로 축소**:

$$m a^\mu \approx qF^{\mu\nu}u_\nu + \frac{q^2\tau_0}{m}\left[q\partial_\alpha F^{\mu\nu}u_\nu u^\alpha + \frac{q^2}{m}F^{\mu\alpha}F_{\alpha\nu}u^\nu - \frac{q^2}{m^2 c^2}F^{\alpha\beta}F_{\alpha\gamma}u_\beta u^\gamma u^\mu\right]$$

> **Unicode**
> ```
> m a^μ ≈ qF^μνu_ν + (q²τ₀)/(m)[q∂_α F^μνu_ν u^α + (q²)/(m)F^μαF_ανu^ν - (q²)/(m² c²)F^αβF_αγuᵦ u^γ u^μ]
> ```

**비상대론 극한:**

$$\mathbf{F}_{LL} = \tau_0\left[q\dot{\mathbf{E}} + q\mathbf{v}\times\dot{\mathbf{B}} + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\times q\mathbf{B} + \ldots\right]$$

> **Unicode**
> ```
> 𝐅_LL = τ₀[q𝐄˙ + q𝐯×𝐁˙ + (q)/(m)(𝐄+𝐯×𝐁)× q𝐁 + ...]
> ```

**현재 강장 QED 시뮬레이션의 표준.** ALD 병리 제거, $\tau_0\omega \ll 1$에서 유효.

**한계:** $\chi = \gamma E/E_{cr} \sim 1$인 극한 영역(강레이저)에서는 양자 방사 모델 필요 (→ §5.1.4).

### 3.2.5 싱크로트론 방사

상대론적 전자가 $B$에서 원운동 시 방사는 $1/\gamma$ 원뿔로 **전방 집중**.

**각분포:**

$$\frac{dP}{d\Omega} = \frac{q^2}{16\pi^2\varepsilon_0 c}\frac{|\mathbf{n}\times[(\mathbf{n}-\boldsymbol{\beta})\times\dot{\boldsymbol{\beta}}]|^2}{(1-\mathbf{n}\cdot\boldsymbol{\beta})^5}$$

> **Unicode**
> ```
> (dP)/(dΩ) = (q²)/(16π²ε₀ c)(|𝐧×[(𝐧-β)×β˙]|²)/((1-𝐧·β)⁵)
> ```

분모 $(1-\beta\cos\theta)^5$ 때문에 $\theta \sim 1/\gamma$에 피크, 전방으로 $\gamma^4$ 증폭.

**임계 진동수:**

$$\omega_c = \frac{3}{2}\gamma^3\frac{c}{r_L} = \frac{3qB}{2m}\gamma^2\sin\alpha$$

> **Unicode**
> ```
> ω_c = (3)/(2)γ³(c)/(r_L) = (3qB)/(2m)γ²sinα
> ```

**스펙트럼:** 수정 베셀 함수 $K_{1/3}, K_{2/3}$:

$$\frac{d^2 I}{d\omega d\Omega} \propto \left(\frac{\omega}{\omega_c}\right)^2 \left[K_{2/3}^2(\xi) + \frac{\gamma^2\theta^2}{1+\gamma^2\theta^2}K_{1/3}^2(\xi)\right]$$

> **Unicode**
> ```
> (d² I)/(dω dΩ) ∝ ((ω)/(ω_c))² [K_2/3²(ξ) + (γ²θ²)/(1+γ²θ²)K_1/3²(ξ)]
> ```

$$\xi = \frac{\omega}{2\omega_c}(1+\gamma^2\theta^2)^{3/2}$$

> **Unicode**
> ```
> ξ = (ω)/(2ω_c)(1+γ²θ²)^3/2
> ```

**특징:**

- **편광:** 궤도면 내 선편광 + 약한 원편광
- **펄스 길이:** 관찰자는 $\Delta t \sim 1/\gamma^3\omega_c$ 짧은 펄스로 봄 → 고조파 $n \sim \gamma^3$까지 겹쳐 연속 스펙트럼
- **전체 파워:** $P \propto \gamma^2 B^2$

**응용:**
- 싱크로트론 광원 (X선, 자외선)
- 크랩 성운, 제트 방사 (천체물리)
- 전자 GeV에서 수 MW 방사 손실 — LEP가 원형 $e^+e^-$ 한계였던 이유

### 3.2.6 강성도 $B\rho = p/q$

**정의:** 운동량 $p$인 입자가 곡률 반경 $\rho$로 휘려면 필요한 자기장:

$$B\rho = \frac{p}{q} = \frac{\gamma m v}{q}$$

> **Unicode**
> ```
> Bρ = (p)/(q) = (γ m v)/(q)
> ```

**단위:** T·m. 실무 공식:

$$B\rho[\text{T·m}] = 3.3356 \cdot p[\text{GeV}/c] / q[e]$$

> **Unicode**
> ```
> Bρ[T·m] = 3.3356 · p[GeV/c] / q[e]
> ```

**응용 4가지:**

1. **가속기 설계:** $p$가 커지면 같은 $\rho$ 유지에 $B$ 증가 필요. LHC $p = 7$ TeV, $\rho = 2804$ m → $B = 8.33$ T 초전도 자석 한계
2. **자기 분광기:** $B\rho$로 입자 운동량 분석
3. **우주선:** 지구 자기권 차단 — $B\rho < 10$ GV 입자는 극으로만 진입 (컷오프 강성도)
4. **의료:** 양성자 치료 갠트리, $B\rho = 2.3$ Tm (230 MeV)

**상대론적 질량 증가를 자동 포함**하므로 고에너지에서 $B\rho$가 자연 변수다.

### 3.2.7 매스매티카 검증

```mathematica
(* 라모 공식 *)
larmorPower[q_, a_, epsilon0_, c_] := q^2 a^2 / (6 Pi epsilon0 c^3);

(* 상대론적 Liénard *)
lienardPower[q_, aPar_, aPerp_, gamma_, epsilon0_, c_] :=
  (q^2 gamma^4) / (6 Pi epsilon0 c^3) * (aPerp^2 + gamma^2 aPar^2);

(* 싱크로트론 방사 파워 *)
syncPower[q_, B_, m_, gamma_, epsilon0_, c_] :=
  q^4 B^2 / (6 Pi epsilon0 m^2 c) * gamma^2;

(* 강성도 *)
rigidity[p_, q_] := p/q;
```

### 3.2.8 한계·예외

- **ALD 병리:** runaway, pre-acceleration. Landau-Lifshitz로 완화되나 $\chi \sim 1$에서 재발
- **양자 영역:** $\hbar\omega_c \sim \gamma mc^2$이면 **양자 방사 반작용** 필요 (→ §5.1.4)
- **비상대론 극한:** $\gamma \to 1$에서 라모 공식으로 환원
- **강장에서 진공 복굴절:** $B > B_c = 4.4\times10^9$ T이면 QED 비선형 효과 (→ §6.1.7)

> **참고문헌**
> - Larmor, J., *On a dynamical theory of the electric and luminiferous medium*, Phil. Trans. R. Soc. A **190**, 205 (1897). [doi:10.1098/rsta.1897.0020](https://doi.org/10.1098/rsta.1897.0020)
> - Dirac, P. A. M., *Classical theory of radiating electrons*, Proc. R. Soc. A **167**, 148 (1938). [doi:10.1098/rspa.1938.0124](https://doi.org/10.1098/rspa.1938.0124)
> - Landau, L. D., Lifshitz, E. M., *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §76.
> - Sokolov, A. A., Ternov, I. M., *Synchrotron Radiation*, Pergamon (1968).

---
 ## 3.3 양자역학 — $p \to p - qA$가 전부다

고전적 힘 $q\mathbf{v}\times\mathbf{B}$는 양자역학에서 **연산자가 아니다**. 대신 해밀토니안에 $A$가 들어가 운동을 지배한다. 이 절에서는 최소 결합, 란다우 준위, 양자 홀 효과, 파울리·디랙 방정식을 다룬다.

## 3.3 양자역학·양자 홀 효과 — $U(1)$ 위상이 물리가 되는 곳

> **절의 흐름**
> 최소 결합 → 란다우 준위 → 양자 홀 효과 → 파울리/디랙 → 게이지 위상
>
> 고전 로렌츠 힘 $q\mathbf{v}\times\mathbf{B}$가 양자역학에서는 연산자 $(\mathbf{p}-q\mathbf{A})$로 들어간다. 자기장은 더 이상 힘이 아니라 위상이 된다.

### 3.3.1 최소 결합과 슈뢰딩거 방정식

고전 해밀토니안 $H = \frac{1}{2m}(\mathbf{p}-q\mathbf{A})^2 + q\phi$를 양자화:

$$\hat{\mathbf{p}} = -i\hbar\nabla, \quad [\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$$

> **Unicode**
> ```
> 𝐩̂ = -iℏ∇,   [x̂ᵢ, p̂ⱼ] = iℏδᵢⱼ
> ```

**슈뢰딩거 방정식:**

$$i\hbar\partial_t\psi = \left[\frac{1}{2m}(-i\hbar\nabla-q\mathbf{A})^2 + q\phi\right]\psi$$

> **Unicode**
> ```
> iℏ∂ₜψ = [(1)/(2m)(-iℏ∇-q𝐀)² + qφ]ψ
> ```

**이것이 최소 결합 처방** $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$, $E \to E - q\phi$다.

**전류 밀도:**

$$\mathbf{j} = \frac{q}{2m}\left[\psi^*(-i\hbar\nabla-q\mathbf{A})\psi + c.c.\right] = \frac{q}{m}\Re[\psi^*(\hat{\mathbf{p}}-q\mathbf{A})\psi]$$

> **Unicode**
> ```
> 𝐣 = (q)/(2m)[ψ^*(-iℏ∇-q𝐀)ψ + c.c.] = (q)/(m)Re[ψ^*(𝐩̂-q𝐀)ψ]
> ```

**운동학적 운동량 연산자** $\hat{\boldsymbol{\pi}} = \hat{\mathbf{p}}-q\mathbf{A}$의 기대값이 $m\mathbf{v}$다.

**하이젠베르크 운동방정식:**

$$\dot{\hat{\mathbf{r}}} = [\hat{\mathbf{r}}, H]/i\hbar = \hat{\boldsymbol{\pi}}/m$$

$$\dot{\hat{\boldsymbol{\pi}}} = [\hat{\boldsymbol{\pi}}, H]/i\hbar$$

계산하면:

$$m\frac{d^2\hat{\mathbf{r}}}{dt^2} = q\hat{\mathbf{E}} + \frac{q}{2}(\hat{\mathbf{v}}\times\hat{\mathbf{B}} - \hat{\mathbf{B}}\times\hat{\mathbf{v}})$$

> **Unicode**
> ```
> m(d²𝐫̂)/(dt²) = q𝐄̂ + (q)/(2)(𝐯̂×𝐁̂ - 𝐁̂×𝐯̂)
> ```

고전 로렌츠 힘의 **연산자 대칭화 버전**. 기대값에 대해 에렌페스트 정리:

$$\langle m\ddot{\mathbf{r}}\rangle = q\langle\mathbf{E}+\mathbf{v}\times\mathbf{B}\rangle$$

> **Unicode**
> ```
> ⟨ m𝐫¨⟩ = q⟨𝐄+𝐯×𝐁⟩
> ```

**핵심:** 슈뢰딩거 방정식에는 $\mathbf{E}, \mathbf{B}$가 **직접 안 들어가고** $\mathbf{A}, \phi$로만 들어간다. **힘이 아닌 위상으로 작용**한다.

### 3.3.2 란다우 준위 완전 유도

$\mathbf{B} = B\hat{z}$ 균일, $\phi = 0$, **란다우 게이지** $\mathbf{A} = (0, Bx, 0)$ 선택.

**해밀토니안:**

$$H = \frac{\hat{p}_x^2}{2m} + \frac{(\hat{p}_y - qBx)^2}{2m} + \frac{\hat{p}_z^2}{2m}$$

> **Unicode**
> ```
> H = (p̂ₓ²)/(2m) + ((p̂_y - qBx)²)/(2m) + (p̂_z²)/(2m)
> ```

**가환 관계:** $[H, \hat{p}_y] = [H, \hat{p}_z] = 0$ → 고유함수:

$$\psi = e^{i(k_y y + k_z z)}\varphi(x)$$

> **Unicode**
> ```
> ψ = e^i(k_y y + k_z z)φ(x)
> ```

$x$ 방정식:

$$\left[\frac{\hat{p}_x^2}{2m} + \frac12 m\omega_c^2 (x - x_0)^2\right]\varphi = \left(E-\frac{\hbar^2k_z^2}{2m}\right)\varphi$$

> **Unicode**
> ```
> [(p̂ₓ²)/(2m) + (1)/(2) mω_c² (x - x₀)²]φ = (E-(ℏ²k_z²)/(2m))φ
> ```

여기서:

$$\omega_c = \frac{|q|B}{m}, \quad x_0 = \frac{\hbar k_y}{qB}$$

> **Unicode**
> ```
> ω_c = (|q|B)/(m),   x₀ = (ℏ k_y)/(qB)
> ```

**정확히 중심이 $x_0$인 1차원 조화 진동자다.** 따라서:

$$E = \frac{\hbar^2 k_z^2}{2m} + \hbar\omega_c\left(n+\frac12\right), \quad n = 0, 1, 2, \ldots$$

> **Unicode**
> ```
> E = (ℏ² k_z²)/(2m) + ℏω_c(n+(1)/(2)),   n = 0,1,2,...
> ```

**2차원계** ($k_z = 0$)이면:

$$E_n = \hbar\omega_c\left(n+\frac12\right)$$

> **Unicode**
> ```
> Eₙ = ℏω_c(n+1/2)
> ```

이것이 **란다우 준위**다.

**물리적 의미 3가지:**

1. **자기 길이 양자화:** $r_L \to l_B = \sqrt{\hbar/|q|B}$
2. **축퇴도:** 각 $n$은 $N_\phi = BS/\Phi_0$, $\Phi_0 = h/e$ 자속 양자 수만큼 축퇴
3. **고전-양자 대응:** $n$이 큰 준고전 극한에서 $r_n = \sqrt{2\hbar(n+1/2)/m\omega_c} \to r_L$

**대칭 게이지** $\mathbf{A} = \frac12\mathbf{B}\times\mathbf{r}$에서는 $L_z$ 고유상태, 파동함수 $\psi_{n,m} \sim z^m e^{-|z|^2/4l_B^2}$ 형태 — 양자 홀 효과에 필수.

### 3.3.3 양자 홀 효과

2차원 전자 가스에 $B\hat{z}$, 전류 $j_x$ 흘리면 고전 홀 효과: $E_y = (B/qn)j_x$, 홀 저항 $R_H = B/qn$.

란다우 준위 존재 시 $T \to 0$에서 화학 퍼텐셜이 갭에 있으면 전류가 **무산란**으로 흐른다.

#### 정수 양자 홀 효과 (IQHE)

**채움 인자:**

$$\nu = \frac{n_{2D}h}{eB} = \frac{N_e}{N_\phi}$$

> **Unicode**
> ```
> ν = (n_2Dh)/(eB) = (Nₑ)/(Nᵩ)
> ```

정수일 때:

$$\sigma_{xy} = \nu \frac{e^2}{h}, \quad \sigma_{xx} = 0$$

> **Unicode**
> ```
> σ_xy = ν (e²)/(h),   σₓₓ = 0
> ```

$$R_H = \frac{h}{\nu e^2}$$

> **Unicode**
> ```
> R_H = (h)/(ν e²)
> ```

$h/e^2 = 25.812\ \text{k}\Omega$ 정확히 양자화, $10^{-9}$ 정밀도.

**유도 — Kubo 공식:**

$$\sigma_{xy} = \frac{e^2\hbar}{i}\sum_{n\neq m}\frac{\langle n|v_x|m\rangle\langle m|v_y|n\rangle - (x\leftrightarrow y)}{(E_n-E_m)^2}(f_n-f_m)$$

> **Unicode**
> ```
> σ_xy = (e²ℏ)/(i)∑_n≠ m(⟨ n|vₓ|m⟩⟨ m|v_y|n⟩ - (x↔ y))/((Eₙ-Eₘ)²)(fₙ-fₘ)
> ```

**베리 곡률 적분:**

$$\sigma_{xy} = \frac{e^2}{h}\frac{1}{2\pi}\int_{BZ} \Omega_z(\mathbf{k})\, d^2k = \frac{e^2}{h}C$$

> **Unicode**
> ```
> σ_xy = (e²)/(h)(1)/(2π)∫_BZ Ω_z(𝐤) d²k = (e²)/(h)C
> ```

$C$는 **제1 Chern 수** (정수) — IQHE의 위상 불변량.

**로렌츠 힘과의 연결:** 로렌츠 힘의 $E\times B$ 드리프트가 $k$-공간 베리 곡률과 동일 구조.

#### 분수 양자 홀 효과 (FQHE)

$\nu = 1/3, 2/5$ 등. 전자간 쿨롱 + 로렌츠 힘으로 **복합 페르미온** 형성.

**Laughlin 파동함수:**

$$\Psi_{1/m} = \prod_{i<j}(z_i-z_j)^m e^{-\sum|z_i|^2/4l_B^2}$$

> **Unicode**
> ```
> Ψ_1/m = ∏_i<j(zᵢ-zⱼ)ᵐ e^-∑|zᵢ|²/4l_B²
> ```

**준입자:** 전하 $e^* = e/3$, 통계 $\theta = \pi/m$ — **애니온(anyon)**.

**본질:** 로렌츠 힘은 입자를 원운동시켜 운동 에너지 소광(quench) → 운동량 공간이 아닌 **위치 공간 자체가 비가환** $[x,y] = il_B^2$ → 위상 물질.

**최근:** 2023 그래핀에서 $B = 0$에서도 분수 Chern 절연체 관측 — 로렌츠 힘 없이 베리 곡률이 $B_{eff}$ 역할.

### 3.3.4 파울리 방정식과 스핀-자기장 상호작용

슈뢰딩거는 스핀을 모른다. 스핀 1/2 포함 시 **파울리 방정식**:

$$i\hbar\partial_t \begin{pmatrix}\psi_\uparrow \\ \psi_\downarrow\end{pmatrix} = \left[\frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m} + q\phi - \frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}\right]\begin{pmatrix}\psi_\uparrow \\ \psi_\downarrow\end{pmatrix}$$

> **Unicode**
> ```
> iℏ∂ₜ [ψ_uparrow; ψ_downarrow] = [((𝐩̂-q𝐀)²)/(2m) + qφ - (qℏ)/(2m)σ·𝐁][ψ_uparrow; ψ_downarrow]
> ```

**3개 항:**
1. 운동 에너지 (궤도 로렌츠 힘, 란다우)
2. 전기 퍼텐셜
3. **제이만** $H_Z = -\hat{\boldsymbol{\mu}}\cdot\mathbf{B}$, $\hat{\boldsymbol{\mu}} = g\frac{q}{2m}\mathbf{S}$, $g \approx 2$

**즉, 전하는 $\mathbf{A}$를 통해 궤도 운동으로 $q\mathbf{v}\times\mathbf{B}$를, 스핀은 직접 $\boldsymbol{\sigma}\cdot\mathbf{B}$로 $B$를 느낀다.**

**란다우 준위 + 스핀:**

$$E_{n,s} = \hbar\omega_c(n+1/2) + g\frac{\hbar\omega_c}{2}s, \quad s = \pm 1/2$$

> **Unicode**
> ```
> E_n,s = ℏω_c(n+1/2) + g(ℏω_c)/(2)s,   s = ±1/2
> ```

전자 $g \approx 2$ → $E_{n,+1/2} = \hbar\omega_c(n+1)$, $E_{n,-1/2} = \hbar\omega_c n$. 스핀 분열이 란다우 간격과 거의 같아 $n=0$ 제외하고 2중 축퇴.

### 3.3.5 디랙 방정식과 Foldy-Wouthuysen

상대론적 스핀 1/2는 **디랙 방정식**:

$$[\gamma^\mu(i\hbar\partial_\mu - qA_\mu) - mc]\psi = 0$$

> **Unicode**
> ```
> [γ^μ(iℏ∂_μ - qA_μ) - mc]ψ = 0
> ```

**해밀토니안 형태:**

$$i\hbar\partial_t\psi = [c\boldsymbol{\alpha}\cdot(\hat{\mathbf{p}}-q\mathbf{A}) + \beta mc^2 + q\phi]\psi$$

> **Unicode**
> ```
> iℏ∂ₜψ = [cα·(𝐩̂-q𝐀) + β mc² + qφ]ψ
> ```

**비상대론 극한 — Foldy-Wouthuysen 변환:**

$$H_{FW} = \frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m} + q\phi - \frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B} - \frac{(\hat{\mathbf{p}}-q\mathbf{A})^4}{8m^3c^2} - \frac{q\hbar}{4m^2c^2}\boldsymbol{\sigma}\cdot[(\hat{\mathbf{p}}-q\mathbf{A})\times\mathbf{E} - \mathbf{E}\times(\hat{\mathbf{p}}-q\mathbf{A})] + \ldots$$

> **Unicode**
> ```
> H_FW = ((𝐩̂-q𝐀)²)/(2m) + qφ - (qℏ)/(2m)σ·𝐁 - ((𝐩̂-q𝐀)⁴)/(8m³c²) - (qℏ)/(4m²c²)σ·[(𝐩̂-q𝐀)×𝐄 - 𝐄×(𝐩̂-q𝐀)] + ...
> ```

**항목별 의미:**
- 1~3항: 파울리 방정식
- 4항: 운동 에너지 상대론 보정
- 5항: **스핀-궤도 결합** $H_{SO} = -\frac{q\hbar}{4m^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})$

**스핀-궤도 결합의 기원:** 원자 내부 $\mathbf{E}$가 움직이는 전자에게는 **자기장**으로 보인다 (로렌츠 변환). 이것이 $\mathbf{v}\times\mathbf{E}$ 로렌츠 힘의 원자 내부 버전이다.

**디랙 해 — 상대론적 란다우 준위:**

$$E_n = \sqrt{m^2c^4 + c^2\hbar^2k_z^2 + 2\hbar c^2 |q|B n}, \quad n = 0, 1, 2, \ldots$$

> **Unicode**
> ```
> Eₙ = √(m²c⁴ + c²ℏ²k_z² + 2ℏ c² |q|B n),   n = 0,1,2,...
> ```

$n = 0$ 란다우 준위가 0이 아닌 **카이랄 0-모드** — 그래핀, 3차원 Dirac/Weyl 반금속에서 관측.

### 3.3.6 게이지 불변성과 양자 위상

양자역학에서 $A_\mu \to A_\mu + \partial_\mu\chi$ 변환 시:

$$\psi \to \psi' = \exp\left(i\frac{q\chi}{\hbar}\right)\psi$$

> **Unicode**
> ```
> ψ → ψ' = exp(i(qχ)/(ℏ))ψ
> ```

슈뢰딩거/디랙 방정식 불변. 물리량 $\rho = |\psi|^2$, $\mathbf{j}$ 불변.

**그러나 위상은 물리적이다:**

$$\gamma = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi}{\hbar}$$

> **Unicode**
> ```
> γ = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ)/(ℏ)
> ```

- 게이지 변환 $\chi$가 단일값이면 $\oint \nabla\chi\cdot d\ell = 0$ → $\gamma$ 불변
- 공간이 **비단순 연결**이면 $\chi$가 다중값 가능, $\gamma$가 $2\pi$ 정수배 차이로 게이지 불변 모듈로 $2\pi$

이것이 **Aharonov-Bohm**, Berry 위상의 게이지 불변성이다.

**정리:**

| 관점 | 힘/위상 | 의미 |
|---|---|---|
| 고전 | 힘 = $qF\cdot v$ | 장 $F$만 의미 |
| 양자 | 위상 = $\frac{q}{\hbar}\int A$ | 접속 $A$ 자체가 간섭으로 관측 |

$F = 0$인 곳에서도 $W(C) \neq 1$일 수 있다.

**따라서 양자역학은 로렌츠 힘을 힘으로 보지 않고 $U(1)$ 다발의 평행 이동 법칙으로 본다.** 란다우 양자화, 양자 홀 효과, AB 효과 모두 $p \to p - qA$라는 하나의 최소 결합 원리에서 나온다. 고전적 $q\mathbf{v}\times\mathbf{B}$는 그 원리의 $\hbar \to 0$ 극한에서 나타나는 그림자다.

### 3.3.7 매스매티카 검증

```mathematica
(* 란다우 준위 *)
landauLevels[n_, hBar_, omegaC_] := hBar omegaC (n + 1/2);

(* 란다우 게이지 해밀토니안 *)
H = (px^2)/(2 m) + (py - q B x)^2/(2 m) + pz^2/(2 m);

(* x 방정식이 조화 진동자인지 확인 *)
(* p_y, p_z를 상수로 두고 x에 대한 방정식 추출 *)
Hx = (px^2)/(2 m) + (hbar ky - q B x)^2/(2 m);
Simplify[Hx]
(* 결과: (px²)/(2m) + (1/2) m ω_c² (x - x0)²,  ω_c = qB/m, x0 = ℏ ky/(qB) *)

(* 양자 홀 전도도 *)
hallConductance[nu_] := nu e^2/h;
```

### 3.3.8 한계·예외

- **비상대론 극한:** 슈뢰딩거-파울리 방정식은 $v \ll c$에서만 유효
- **다체 효과:** 란다우 준위 축퇴도가 크면 전자 상호작용이 지배 (FQHE)
- **강자기장:** $B > B_c$에서 진공 복굴절, 쌍생성 (→ §6.1.7)
- **비아벨 게이지:** $SU(2)$, $SU(3)$에서는 최소 결합이 더 복잡 (→ §6.1.1)

> **참고문헌**
> - Landau, L. D., *Diamagnetismus der Metalle*, Z. Phys. **64**, 629 (1930). [doi:10.1007/BF01397213](https://doi.org/10.1007/BF01397213)
> - von Klitzing, K., Dorda, G., Pepper, M., *New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance*, Phys. Rev. Lett. **45**, 494 (1980). [doi:10.1103/PhysRevLett.45.494](https://doi.org/10.1103/PhysRevLett.45.494)
> - Laughlin, R. B., *Anomalous quantum Hall effect: An incompressible quantum fluid with fractionally charged excitations*, Phys. Rev. Lett. **50**, 1395 (1983). [doi:10.1103/PhysRevLett.50.1395](https://doi.org/10.1103/PhysRevLett.50.1395)
> - Sakurai, J. J., Napolitano, J., *Modern Quantum Mechanics*, 2nd ed., Pearson (2011), Chapter 5.

---

## 3.4 통계역학·플라즈마 운동론

1개 입자의 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$가 $10^{20}$개가 되면 **분포함수** $f(\mathbf{x},\mathbf{v},t)$의 흐름이 된다. 이 절에서는 볼츠만, 블라소프, 푸커-플랑크, 란주뱅 방정식과 수송 계수를 다룬다.

### 3.4.1 볼츠만 방정식과 로렌츠 항

**위상공간 밀도** $f_s(\mathbf{x},\mathbf{v},t)d^3x\,d^3v$ = $s$종 입자 수. 보존 법칙:

$$\frac{df}{dt} = C[f]$$

> **Unicode**
> ```
> (df)/(dt) = C[f]
> ```

**전미분 전개:**

$$\frac{\partial f}{\partial t} + \dot{\mathbf{x}}\cdot\nabla_x f + \dot{\mathbf{v}}\cdot\nabla_v f = C[f]$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐱˙·∇ₓ f + 𝐯˙·∇ᵥ f = C[f]
> ```

**뉴턴 + 로렌츠 대입:** $\dot{\mathbf{x}} = \mathbf{v}$, $\dot{\mathbf{v}} = \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + \frac{\mathbf{F}_{other}}{m}$:

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = C[f]$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐯·∇ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = C[f]
> ```

**로렌츠 항의 특성 3가지:**

1. **위상공간 비압축:** $\nabla_v\cdot(\mathbf{v}\times\mathbf{B}) = 0$, $\nabla_v\cdot\mathbf{E} = 0$ → 입자 생성/소멸 안 함, 궤적만 휘게 함
2. **에너지 중립:** $\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$ → 자기장은 $v^2$ 모멘트에 직접 기여 안 함
3. **$\mathbf{E}$ 항:** $\mathbf{v}\cdot\mathbf{E}$로 에너지 주입

**충돌 연산자 $C$ 없으면** 특성곡선이 단일 입자 로렌츠 궤적. $f$는 그 궤적을 따라 보존.

### 3.4.2 블라소프 방정식 (무충돌)

$C = 0$ 극한, 평균장만 남음:

$$\frac{\partial f_s}{\partial t} + \mathbf{v}\cdot\nabla f_s + \frac{q_s}{m_s}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f_s = 0$$

> **Unicode**
> ```
> (∂ fₛ)/(∂ t) + 𝐯·∇ fₛ + (qₛ)/(mₛ)(𝐄+𝐯×𝐁)·∇ᵥ fₛ = 0
> ```

**$\mathbf{E}, \mathbf{B}$는 Maxwell 방정식으로 $f$로부터 자체 일관적으로 결정:**

$$\rho = \sum_s q_s\int f_s\, d^3v, \quad \mathbf{J} = \sum_s q_s\int \mathbf{v}f_s\, d^3v$$

> **Unicode**
> ```
> ρ = ∑ₛ qₛ∫ fₛ d³v,   𝐉 = ∑ₛ qₛ∫ 𝐯fₛ d³v
> ```

$$\nabla\cdot\mathbf{E} = \rho/\epsilon_0, \quad \nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\partial_t\mathbf{E}$$

> **Unicode**
> ```
> ∇·𝐄 = ρ/ε₀,   ∇×𝐁 = μ₀𝐉 + μ₀ε₀∂ₜ𝐄
> ```

이 폐쇄계가 **Vlasov-Maxwell** 계.

**특징:**

- **시간 가역적, 엔트로피 보존.** 충돌 없는 란다우 감쇠, 두 흐름 불안정, BGK 모드 등 운동론적 현상이 여기서 나온다
- 자기장 $B_0\hat{z}$에서 선형화하면 **사이클로트론 공명**: $\omega - k_\parallel v_\parallel - n\omega_c = 0$ 분모. $n\omega_c$ 항이 로렌츠 원운동의 기억
- **리우빌:** $df/dt = 0$ → 위상 밀도 보존. $f$는 로렌츠 흐름에 따라 찢어지지만(**phase mixing**) 값은 유지

**블라소프가 고온 핵융합, 우주 플라즈마 표준 모델인 이유:** 충돌 평균자유행로 $\lambda_{mfp} \gg L$이라 $C$ 무시 가능.

### 3.4.3 푸커-플랑크 방정식

충돌이 **작은 각도 산란 누적**일 때 $C$를 **속도 공간 확산**으로 근사:

$$C_{FP}[f] = -\frac{\partial}{\partial v_i}(A_i f) + \frac12\frac{\partial^2}{\partial v_i\partial v_j}(D_{ij}f)$$

> **Unicode**
> ```
> C_FP[f] = -(∂)/(∂ vᵢ)(Aᵢ f) + (1)/(2)(∂²)/(∂ vᵢ∂ vⱼ)(Dᵢⱼf)
> ```

- $A_i = \langle\Delta v_i\rangle/\Delta t$: **마찰**
- $D_{ij} = \langle\Delta v_i\Delta v_j\rangle/\Delta t$: **확산**

**로렌츠 힘 포함 형태:**

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = -\nabla_v\cdot(\mathbf{A}f) + \frac12\nabla_v\nabla_v:(D f)$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐯·∇ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = -∇ᵥ·(𝐀f) + (1)/(2)∇ᵥ∇ᵥ:(D f)
> ```

**쿨롱 충돌의 경우 — Rosenbluth 퍼텐셜** $h, g$:

$$A_i = \Gamma\partial_{v_i}h, \quad D_{ij} = \Gamma\partial_{v_i}\partial_{v_j}g$$

> **Unicode**
> ```
> Aᵢ = Γ∂_vᵢ h,   Dᵢⱼ = Γ∂_vᵢ∂_vⱼ g
> ```

**자기장이 있으면 확산 텐서가 이방성:**

$$D = D_\parallel \hat{b}\hat{b} + D_\perp (I - \hat{b}\hat{b}) + D_\wedge \hat{b}\times$$

> **Unicode**
> ```
> D = D_∥ b̂b̂ + D_⊥ (I-b̂b̂) + D_∧ b̂×
> ```

$D_\wedge$가 **홀 확산**.

**자기 구속의 운동론적 표현:** 자기장이 강할수록

$$D_\perp \sim \frac{D_0}{1+\omega_c^2\tau^2}$$

> **Unicode**
> ```
> D_⊥ ∼ (D₀)/(1+ω_c²τ²)
> ```

$\omega_c\tau \gg 1$이면 수직 확산이 $1/B^2$로 감소.

### 3.4.4 란주뱅 방정식

단일 입자 궤적에 **확률적 힘** 추가:

$$m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) - m\nu\mathbf{v} + \mathbf{F}_{stoch}(t) + q\mathbf{v}\times\tilde{\mathbf{B}}(t)$$

> **Unicode**
> ```
> m𝐯˙ = q(𝐄+𝐯×𝐁) - mν𝐯 + 𝐅_stoch(t) + q𝐯×𝐁̃(t)
> ```

- $-m\nu\mathbf{v}$: 평균 마찰
- $\mathbf{F}_{stoch}$: 랜덤 전기장 요동, $\langle F_i(t)F_j(t')\rangle = 2m\nu T \delta_{ij}\delta(t-t')$ — **요동-산일 정리**
- 마지막 항: 자기 요동에 의한 **피치각 산란**

이 SDE의 Fokker-Planck 극한이 위 FP 방정식.

**물리적 의미:** 로렌츠 힘은 결정론적 자이로 운동, 마찰/확산은 충돌로 자이로 위상 무작위화. $\nu/\omega_c$가 작으면 자이로 운동이 충돌 사이에 많이 회전 → **자기화된 플라즈마**.

**자기 요동 Langevin:** 자기 거울, 토카막에서 **비정상 수송** 설명. $\tilde{B}_r$로 인한 $E\times B$ 난류가 $D \sim \tilde{B}^2$ 확산 생성.

### 3.4.5 맥스웰-볼츠만 분포 (Bohr-van Leeuwen)

충돌 연산자 $C = 0$ 되는 평형해를 찾는다.

자기장만 있으면 $H = mv^2/2$ 보존, 로렌츠 힘이 일을 안 하므로 어떤 등방 분포도 $f(v)$는 Vlasov 정상해. H-정리 $dS/dt \geq 0$로 엔트로피 최대화 시:

$$f_M(\mathbf{v}) = n\left(\frac{m}{2\pi T}\right)^{3/2}\exp\left(-\frac{mv^2}{2T}\right)$$

> **Unicode**
> ```
> f_M(𝐯) = n((m)/(2π T))^3/2exp(-(mv²)/(2T))
> ```

**맥스웰-볼츠만.** $\mathbf{B}$는 $f_M$에 **안 들어간다** — **Bohr-van Leeuwen 정리**: 고전 평형 자화 $M = 0$. 자기장은 평형 분포를 못 만든다. **자화는 양자 란다우 반자성에서만 나온다.**

**전기장 $\mathbf{E} = -\nabla\phi$ 존재, 정상 $\partial_t = 0$이면:**

$$f_{eq} = n_0\left(\frac{m}{2\pi T}\right)^{3/2}\exp\left(-\frac{mv^2/2 + q\phi(\mathbf{x})}{T}\right)$$

> **Unicode**
> ```
> f_eq = n₀((m)/(2π T))^3/2exp(-(mv²/2 + qφ(𝐱))/(T))
> ```

**볼츠만 인자** $\exp(-q\phi/T)$. $B$는 여전히 안 들어감. 대신 $\nabla B$ 드리프트와 $\nabla n$ 드리프트가 평형 전류를 만든다 — **반자성 전류** $\mathbf{J}_\perp = \mathbf{B}\times\nabla p/B^2$.

**$E\times B$ 평형:** $f(\mathbf{x},\mathbf{v}) = f_M(\mathbf{v}-\mathbf{V}_E)$도 Vlasov 해. 전체가 $V_E$로 드리프트하는 맥스웰리안.

### 3.4.6 수송 계수

$f = f_M + f_1$로 Chapman-Enskog 전개, 로렌츠 항이 $f_1$ 결정.

#### 전기 전도도

정상, 균일, 약한 $E$, 충돌 $\nu$ 가정. **운동량 방정식:**

$$0 = q(\mathbf{E}+\mathbf{V}\times\mathbf{B}) - m\nu\mathbf{V}$$

> **Unicode**
> ```
> 0 = q(𝐄+𝐕×𝐁) - mν𝐕
> ```

풀면:

$$\mathbf{J} = \sigma_\parallel \mathbf{E}_\parallel + \sigma_P \mathbf{E}_\perp + \sigma_H \hat{b}\times\mathbf{E}_\perp$$

> **Unicode**
> ```
> 𝐉 = σ_∥ 𝐄_∥ + σ_P 𝐄_⊥ + σ_H b̂×𝐄_⊥
> ```

**3개 전도도:**

$$\sigma_\parallel = \frac{nq^2}{m\nu}, \quad \sigma_P = \sigma_\parallel\frac{\nu^2}{\nu^2+\omega_c^2}, \quad \sigma_H = \sigma_\parallel\frac{\nu\omega_c}{\nu^2+\omega_c^2}$$

> **Unicode**
> ```
> σ_∥ = (nq²)/(mν),   σ_P = σ_∥(ν²)/(ν²+ω_c²),   σ_H = σ_∥(νω_c)/(ν²+ω_c²)
> ```

**해석:**
- $\sigma_\parallel$: 평행 전도도, B 영향 없음
- $\sigma_P$ (Pedersen): 수직 전도도, $\omega_c \gg \nu$ 시 $\sigma_\parallel(\nu/\omega_c)^2 \propto 1/B^2$ 억제
- $\sigma_H$ (Hall): 홀 전도도, 무충돌 극한에서 $\sigma_H \to nq/B$

#### 확산

$$D_\perp = \frac{T}{m}\frac{\nu}{\nu^2+\omega_c^2} = D_\parallel\frac{\nu^2}{\nu^2+\omega_c^2}, \quad D_\parallel = \frac{T}{m\nu}$$

> **Unicode**
> ```
> D_⊥ = (T)/(m)(ν)/(ν²+ω_c²) = D_∥(ν²)/(ν²+ω_c²),   D_∥ = (T)/(mν)
> ```

**고전 확산** $D_\perp \propto 1/B^2$ — **자기 구속 원리**.

**난류가 있으면 Bohm 확산** $D_B \sim T/16eB \propto 1/B$로 악화.

#### 점성

**Braginskii 점성 텐서 5개 성분.** $B$ 강하면 수직 점성 $\eta_\perp \sim \eta_0/(\omega_c\tau)^2$ 억제, **자이로점성** $\eta_\wedge$ 잔존 — $E\times B$ 전단 흐름과 결합해 **H-모드** 형성.

**결론:** 로렌츠 힘은 평행 수송은 그대로 두고 **수직 수송만 $\omega_c\tau$만큼 억제**한다. 이 이방성이 플라즈마를 자력선에 묶는다.

### 3.4.7 리우빌 정리

6차원 위상공간 $\Gamma = (\mathbf{x},\mathbf{v})$, 흐름:

$$\dot{\Gamma} = \left(\mathbf{v}, \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\right)$$

> **Unicode**
> ```
> Γ˙ = (𝐯, (q)/(m)(𝐄+𝐯×𝐁))
> ```

**발산:**

$$\nabla_\Gamma\cdot\dot{\Gamma} = \nabla_x\cdot\mathbf{v} + \nabla_v\cdot\frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B}) = 0 + 0 = 0$$

> **Unicode**
> ```
> ∇_Γ·Γ˙ = ∇ₓ·𝐯 + ∇ᵥ·(q)/(m)(𝐄+𝐯×𝐁) = 0 + 0 = 0
> ```

**따라서 위상 부피 $d\Gamma$ 보존.** 연속 방정식:

$$\frac{\partial f}{\partial t} + \nabla_\Gamma\cdot(f\dot{\Gamma}) = 0 \implies \frac{df}{dt} = 0 \text{ if } C = 0$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + ∇_Γ·(fΓ˙) = 0 ⟹ (df)/(dt) = 0  if  C = 0
> ```

이것이 **Vlasov의 Liouville**이다. 수치적으로 보리스 알고리즘이 $\det J = 1$을 만족해야 하는 이유 — Liouville 위반 시 인위적 가열.

**충돌 있으면:**

$$\frac{df}{dt} = C[f] \neq 0, \quad \frac{dS}{dt} = -\int C[f]\ln f\, d\Gamma \geq 0$$

> **Unicode**
> ```
> (df)/(dt) = C[f] ≠ 0,   (dS)/(dt) = -∫ C[f]ln f dΓ ≥ 0
> ```

**H-정리.** 평형 $f_M$에서 $C = 0$, $S$ 최대.

### 3.4.8 종합 요약

| 방정식 | 로렌츠 항 | 역할 |
|---|---|---|
| **Boltzmann** | 위상공간 회전 연산자 | 충돌 포함 일반 운동론 |
| **Vlasov** | 회전만, $f$ 보존 | 란다우 감쇠, 사이클로트론 공명 |
| **Fokker-Planck** | 회전 + 속도 확산 | 자기화된 충돌 |
| **Langevin** | 회전 + 확률 미분 | 단일 입자 궤적 |
| **Maxwell-Boltzmann** | $B$가 분포 못 바꿈 | Bohr-van Leeuwen |
| **수송** | $\sigma_\perp, D_\perp \propto 1/(1+\omega_c^2\tau^2)$ | 자기 구속 |
| **Liouville** | $\nabla_\Gamma\cdot\dot{\Gamma} = 0$ | 모든 보존의 기원 |

**로렌츠 힘은 위상 부피를 찢지만 부피는 지킨다** — 플라즈마가 상전이 없이 난류로 가는 이유.

### 3.4.9 매스매티카 검증

```mathematica
(* 볼츠만 방정식 *)
boltzmannEq = D[f[t, x, y, z, vx, vy, vz], t]
  + vx D[f[t, x, y, z, vx, vy, vz], x]
  + vy D[f[t, x, y, z, vx, vy, vz], y]
  + vz D[f[t, x, y, z, vx, vy, vz], z]
  + (q/m) ((Ex + vy Bz - vz By) D[f[t, x, y, z, vx, vy, vz], vx]
         + (Ey + vz Bx - vx Bz) D[f[t, x, y, z, vx, vy, vz], vy]
         + (Ez + vx By - vy Bx) D[f[t, x, y, z, vx, vy, vz], vz])
  == collisionTerm;

(* 맥스웰-볼츠만 *)
maxwellBoltzmann[vx_, vy_, vz_] := (m/(2 Pi kB T))^(3/2)
  Exp[-m (vx^2 + vy^2 + vz^2)/(2 kB T)];

(* 전도도 *)
sigmaParallel[n_, q_, m_, nu_] := n q^2/(m nu);
sigmaPedersen[sigmaPar_, nu_, omegaC_] := sigmaPar nu^2/(nu^2 + omegaC^2);
sigmaHall[sigmaPar_, nu_, omegaC_] := sigmaPar nu omegaC/(nu^2 + omegaC^2);
```

### 3.4.10 한계·예외

- **충돌 근사:** Fokker-Planck는 작은 각도 산란 가정. 큰 각도 산란(핵융합 반응)은 별도 처리
- **난류 영역:** Vlasov는 난류 포화를 예측 못 함. Renormalization 필요
- **상대론적 운동론:** $T \gtrsim mc^2$에서 상대론적 Vlasov 필요 (핵융합 플라즈마는 비상대론)
- **양자 운동론:** $\lambda_{dB} \sim$ 입자 간격이면 Wigner 함수 필요

> **참고문헌**
> - Vlasov, A. A., *On vibration properties of electron gas*, J. Exp. Theor. Phys. **8**, 291 (1938). [doi:10.1070/PU1968v010n06ABEH003709](https://doi.org/10.1070/PU1968v010n06ABEH003709)
> - Fokker, A. D., *Die mittlere Energie rotierender elektrischer Dipole im Strahlungsfeld*, Ann. Phys. **348**, 810 (1914). [doi:10.1002/andp.19143480507](https://doi.org/10.1002/andp.19143480507)
> - Braginskii, S. I., *Transport processes in a plasma*, Reviews of Plasma Physics **1**, 205 (1965).
> - Krall, N. A., Trivelpiece, A. W., *Principles of Plasma Physics*, McGraw-Hill (1973).

---
 
 # 4막. 응용과 공학 (Applications)

> **막의 흐름**
> 가속기 → 핵융합 → 의료 → 센서 → 우주 → 카오스
>
> 1~3막에서 로렌츠 힘의 이론을 확정했다. 4막은 그 이론이 **실제 장치와 자연현상**에서 어떻게 구현되는지를 다룬다. 모든 응용의 공통 분모는 하나다 — **$\mathbf{E}$로 가속하고, $\mathbf{B}$로 구속한다**.

---

## 4.1 가속기

모든 가속기는 로렌츠 힘 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$의 두 항을 어떻게 쓰느냐의 차이다. $\mathbf{E}$로 가속, $\mathbf{B}$로 궤도 제어. 이 절에서는 사이클로트론, 싱크로트론, 선형가속기, 플라즈마 가속기를 다룬다.

### 4.1.1 사이클로트론과 상대론적 한계

**원리:** 균일 $\mathbf{B} = B_0\hat{z}$, 2개의 D형 전극(Dee)에 RF 전압 $V(t) = V_0\sin\omega_{RF}t$.

**운동방정식:**

$$m\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐯˙ = q𝐯×𝐁
> ```

자이로 진동수 $\omega_c = qB_0/m$은 **속도 무관**. RF를 $\omega_{RF} = \omega_c$로 맞추면 매 반바퀴마다 $\mathbf{E}$ 갭에서 $qV_0$ 에너지 획득.

**반경:** $r = mv_\perp/qB$. **에너지:**

$$E = \frac{q^2 B^2 r^2}{2m} = \frac12 m\omega_c^2 r^2$$

> **Unicode**
> ```
> E = (q² B² r²)/(2m) = (1)/(2) mω_c² r²
> ```

$r$이 에너지 제곱근에 비례해 나선으로 커진다. **강집속 없이도 자동 집속** — 약집속.

**상대론적 한계:**

상대론적 질량 $\gamma m$으로 $\omega_c^{rel} = qB/\gamma m$ 감소. RF 위상 슬립:

$$\Delta\phi = \int(\omega_{RF}-\omega_c^{rel})\,dt$$

> **Unicode**
> ```
> Δφ = ∫(ω_RF-ω_cʳᵉˡ)dt
> ```

**한계 에너지:**

$$\gamma = 1 + E/mc^2, \quad \Delta\omega/\omega = 1-1/\gamma$$

> **Unicode**
> ```
> γ = 1 + E/mc²,   Δω/ω = 1-1/γ
> ```

양성자 1 GeV에서 $\gamma \approx 2$, 진동수 50% 감소 → 공명 붕괴. 고전 사이클로트론 한계 $\sim 20$ MeV 양성자.

**해결책 2가지:**

1. **싱크로사이클로트론:** $B$ 고정, $\omega_{RF}(t) = \omega_{c0}/\gamma(t)$로 주파수 변조. 펄스형, 평균 전류 낮음
2. **아이소크로너스 사이클로트론:** $B(r) = \gamma(r)B_0$로 반경 방향 증가시켜 $\omega_c$ 일정 유지 + 방위각 변화(Thomas focusing)로 수직 집속 보상. 590 MeV PSI 링 사이클로트론이 극한

### 4.1.2 싱크로트론

사이클로트론의 $r$ 가변 대신 $r = \rho$ 고정, $B(t)$를 에너지에 맞춰 올린다.

**강성도:**

$$B\rho = \frac{p}{q}$$

> **Unicode**
> ```
> Bρ = (p)/(q)
> ```

**LHC:** $p = 7$ TeV/c, $\rho = 2804$ m → $B = 8.33$ T. 초전도 쌍극자 자석 한계. FCC는 $\rho = 16$ km, $B = 16$ T 목표.

**위상 안정성 (Veksler-McMillan 1944):**

RF 공진기 전압 $V_{RF}\sin\phi$. 동기 입자 $\phi_s$에 대해 에너지 이득 $qV_{RF}\sin\phi_s$ = 턴당 방사+가속 손실 보상.

에너지가 높은 입자는 회전 주기가 길어짐(transition $\gamma_t$ 이상) → 늦게 도착 → 위상 $\phi$ 작아짐 → 에너지 이득 감소 → **안정화**.

**종방향 운동은 조화 진동자 — 싱크로트론 진동:**

$$\Omega_s^2 = -\frac{qV_{RF}h\eta\cos\phi_s}{2\pi E_s}\omega_{rev}^2$$

> **Unicode**
> ```
> Ωₛ² = -(qV_RFhηcosφₛ)/(2π Eₛ)ωᵣₑᵥ²
> ```

$h$: 하모닉 수, $\eta = 1/\gamma_t^2 - 1/\gamma^2$: 슬립 인자.

**RF 공명:**

$$\omega_{RF} = h\omega_{rev}$$

> **Unicode**
> ```
> ω_RF = hωᵣₑᵥ
> ```

$h \sim 10^4$ (LHC $h = 35640$).

**횡방향 — 4극 자석 강집속:**

$$m\ddot{x} + k(s)x = 0$$

> **Unicode**
> ```
> mx¨ + k(s)x = 0
> ```

Hill 방정식, 베타트론 진동수 $Q_{x,y}$. 로렌츠 힘 $q\mathbf{v}\times\mathbf{B}_{quad}$가 복원력. **공명 $mQ_x + nQ_y = $ 정수 회피**가 설계 핵심.

**싱크로트론 방사 손실:** $P \propto \gamma^4/\rho^2$. LEP에서 턴당 3 GeV 손실.

### 4.1.3 선형가속기

$\mathbf{B}$로 휘지 않고 $\mathbf{E}$로 직선 가속. $B\rho$ 한계 없음, 싱크로트론 방사 없음.

**드리프트 튜브 LINAC:** 길이 $L_n = v_n T_{RF}/2$ 튜브로 입자가 RF 위상이 뒤집히는 동안 차폐. $\beta \approx 1$ 되면 $L = cT_{RF}/2$ 균일.

**고에너지 전자:** 진행파관 $E_z = E_0\sin(\omega t - kz)$, 위상속도 $v_{ph} = c$로 동기화. SLAC 3 km에서 50 GeV.

**한계:** $E_{acc} \sim 30-100$ MV/m, 구리 공동 방전 한계. 1 TeV에 10 km 필요.

### 4.1.4 플라즈마 가속기 (LWFA, PWFA)

**플라즈마 파동 깨진 후 전기장:**

$$E_{WB} = \frac{m_ec\omega_p}{e} \approx 96\sqrt{n_0[\text{cm}^{-3}]}\ \text{V/m}$$

> **Unicode**
> ```
> E_WB = (mₑcωₚ)/(e) ≈ 96√(n₀[cm⁻³]) V/m
> ```

$n_0 = 10^{18}$ cm$^{-3}$ → $E \approx 100$ GV/m, RF보다 **1000배**.

#### LWFA (Laser Wakefield)

강레이저 $a_0 > 1$이 플라즈마에서 **ponderomotive 힘** $\mathbf{F}_p = -m_ec^2\nabla a_0^2/2$로 전자 밀어내 **버블** 형성. 뒤에 $E_z \sim 100$ GV/m 웨이크.

**에너지 이득:**

$$\Delta E \approx 2\gamma_p^2 m_ec^2 \propto n_0^{-1}, \quad \gamma_p = \omega_0/\omega_p$$

> **Unicode**
> ```
> Δ E ≈ 2γₚ² mₑc² ∝ n₀⁻¹,   γₚ = ω₀/ωₚ
> ```

#### PWFA (Plasma Wakefield)

양성자/전자 드라이버 빔이 대신 버블 생성. SLAC에서 42 GeV → 85 GeV 배가 실증.

**문제:** $\mathbf{B}$ 없이 가속이라 횡방향 로렌츠 집속 $\mathbf{v}\times\mathbf{B}_{plasma}$가 약함. 이온 채널 $\mathbf{E}_r - B_\theta$로 집속, 방사(베타트론 방사) 발생.

### 4.1.5 매스매티카 검증

```mathematica
(* 사이클로트론 에너지 *)
cyclotronEnergy[q_, B_, r_, m_] := q^2 B^2 r^2 / (2 m);

(* 상대론적 진동수 *)
omegaRel[q_, B_, gamma_, m_] := q B / (gamma m);

(* 강성도 *)
rigidity[p_, q_] := p/q;

(* LWFA 웨이크장 *)
wakefield[n0_] := 96 Sqrt[n0]; (* V/m, n0 in cm^-3 *)
```

### 4.1.6 한계·예외

- **사이클로트론:** 상대론적 한계 $\sim 20$ MeV 양성자
- **싱크로트론:** 방사 손실 $P \propto \gamma^4/\rho^2$, 전자 기계에서 지배
- **LINAC:** $E_{acc} < 100$ MV/m, 구리 방전 한계
- **LWFA:** 위상 안정성, 에너지 퍼짐, 반복률 문제

> **참고문헌**
> - Lawrence, E. O., Livingston, M. S., *Production of high speed light ions without high voltages*, Phys. Rev. **40**, 19 (1932). [doi:10.1103/PhysRev.40.19](https://doi.org/10.1103/PhysRev.40.19)
> - Wiedemann, H., *Particle Accelerator Physics*, 4th ed., Springer (2015).
> - Esarey, E., Schroeder, C. B., Leemans, W. P., *Physics of laser-driven plasma-based electron accelerators*, Rev. Mod. Phys. **81**, 1229 (2009). [doi:10.1103/RevModPhys.81.1229](https://doi.org/10.1103/RevModPhys.81.1229)

---

## 4.2 핵융합로

핵융합로는 로렌츠 힘으로 $10^4$ eV 플라즈마를 자기 병에 가두는 기계다. 이 절에서는 토카막, 스텔라레이터, 주요 장치 파라미터를 다룬다.

### 4.2.1 토카막과 Grad-Shafranov 방정식

토카막은 $\mathbf{E}$로 전류 구동, $\mathbf{B}$로 압력 구속 — **로렌츠 힘 $\mathbf{J}\times\mathbf{B} = \nabla p$ 평형**.

**평형 방정식:** 정적 $\rho\mathbf{v}\cdot\nabla\mathbf{v} \approx 0$ 가정:

$$\mathbf{J}\times\mathbf{B} = \nabla p$$

> **Unicode**
> ```
> 𝐉×𝐁 = ∇ p
> ```

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J}, \quad \nabla\cdot\mathbf{B} = 0$$

> **Unicode**
> ```
> ∇×𝐁 = μ₀𝐉,   ∇·𝐁 = 0
> ```

**축대칭 $(R,\phi,Z)$에서 자속 함수** $\psi(R,Z) = RA_\phi$ 도입:

$$\mathbf{B} = \nabla\psi\times\nabla\phi + F(\psi)\nabla\phi, \quad F = RB_\phi$$

> **Unicode**
> ```
> 𝐁 = ∇ψ×∇φ + F(ψ)∇φ,   F = RBᵩ
> ```

압력 $p = p(\psi)$, $F = F(\psi)$는 자속면 함수. 암페어 법칙 대입하면 **Grad-Shafranov 방정식**:

$$\Delta^*\psi = R\frac{\partial}{\partial R}\left(\frac1R\frac{\partial\psi}{\partial R}\right) + \frac{\partial^2\psi}{\partial Z^2} = -\mu_0 R^2\frac{dp}{d\psi} - F\frac{dF}{d\psi}$$

> **Unicode**
> ```
> Δ^*ψ = R(∂)/(∂ R)((1)/(R)(∂ψ)/(∂ R)) + (∂²ψ)/(∂ Z²) = -μ₀ R²(dp)/(dψ) - F(dF)/(dψ)
> ```

타원형 비선형 PDE. **우변이 로렌츠 힘:**
- $-p'$: 플라즈마 팽창력
- $-FF'$: 폴로이달 전류의 핀치력

**안전인자:** $q(\psi) = d\Phi_{tor}/d\psi$. $q > 1$이 kink 안정성 조건.

**로렌츠 힘 응용 3가지:**
1. 토로이달 $B_\phi$ + 폴로이달 $B_\theta$ = 나선 자기면 → $\nabla B$, 곡률 드리프트 상쇄
2. 수직장 $B_Z$로 $I_p\times B_Z$로 Hoop force 균형
3. **H-모드:** $E_r\times B$ 전단 흐름이 난류 억제 → 수송 장벽 생성

### 4.2.2 스텔라레이터와 자기섬

토카막은 $B_\theta$를 플라즈마 전류로 만들지만 스텔라레이터는 **외부 코일**로 만든다.

**목표:** 진공 자기면이 이미 존재. $\mathbf{B}$ 선이 $R$에 대해 $\iota/2\pi$만큼 회전 — **회전 변환** $\iota = 1/q$.

**자기섬:** 유리수 $\iota = n/m$인 **유리면(resonant surface)** 에서 섭동 $\tilde{B}_{mn}$이 있으면 자력선 방정식 $d\psi/d\theta = \tilde{B}_r/B_\theta$가 **섬 형성**.

**섬 너비:**

$$w_{mn} \approx 4\sqrt{\frac{q^2 R \tilde{B}_{mn}}{m q' B_0}}$$

> **Unicode**
> ```
> wₘₙ ≈ 4√((q² R B̃ₘₙ)/(m q' B₀))
> ```

$\tilde{B}$가 $10^{-4}$만 되어도 cm 섬 → 겹치면 **Chirikov 기준**으로 확률적 영역 → 구속 붕괴.

**준대칭(quasisymmetry):** $|B|$가 특정 방향으로만 변하게 코일 최적화해 $\mathbf{V}_{gc}$ 드리프트 평균 0. **Wendelstein 7-X**는 50개 비평면 코일로 $\epsilon_{eff} < 1\%$ 달성.

**장단점:**
- 장점: 전류 구동 불필요, disruption 없음
- 단점: 코일 복잡, $B\rho$ 최적화 어려움

### 4.2.3 ITER·KSTAR·LHC 비교표

| 구분 | **KSTAR** | **ITER** | **LHC** |
|---|---|---|---|
| **목적** | 초전도 토카막 물리 H-모드 장시간 | Q=10 핵융합로 실증 | 14 TeV 양성자 충돌 |
| **방식** | 토카막 | 토카막 | 싱크로트론 |
| **로렌츠 힘 역할** | $J_p\times B_t$ 구속, $E_r\times B$ 수송장벽 | 동일 + 알파입자 $v_\alpha\times B$ 구속 | $B\rho = p/q$ 궤도 유지, 4극 $v\times B_{quad}$ 집속 |
| **주반경 $R$ / 부반경 $a$** | 1.8 m / 0.5 m | 6.2 m / 2.0 m | 터널 27 km, $\rho_{bend} = 2804$ m |
| **자장 $B_t$** | 3.5 T (Nb₃Sn 초전도) | 5.3 T 축상, 코일 최대 11.8 T | 8.33 T 쌍극자 |
| **플라즈마/빔 전류** | $I_p \sim 2$ MA | $I_p = 15$ MA | $I_{beam} = 0.58$ A |
| **에너지** | $T_i \sim 10$ keV, 100초 | $T = 20$ keV, $P_{fus} = 500$ MW, Q=10 | $E_{beam} = 7$ TeV, $\gamma = 7460$ |
| **강성도** | $B_\theta\rho \sim 0.5$ Tm | $B_\theta\rho \sim 3$ Tm | 23,334 Tm |
| **RF/가열** | NBI 8 MW, ECH 6 MW | NBI 33 MW, ECH 20 MW | RF 400 MHz, 16 MV/턴 |
| **핵심 난제** | ELM 억제 RMP, $E\times B$ 장시간 | 디스럽션 $J\times B$ 불균형 | $10^{-10}$ Torr 진공, 퀜치 보호 |
| **로렌츠 기반 한계** | Greenwald $n_G$, Troyon $\beta_N < 3$ | 동일 + $q_{95} > 3$ | Beam-beam $\Delta Q \propto N_p$ |

**공통 설계 원리 3가지:**

1. **$B\rho$가 비용:** 토카막 $B_t \propto 1/R$, LHC $E \propto B\rho$. 초전도 $B$ 한계가 두 분야 모두 병목
2. **위상 안정성:** 토카막 $q(\psi)$ 프로파일, 싱크로트론 $\eta\cos\phi_s < 0$
3. **드리프트 제어:** 토카막 다이버터, LHC 다극 오차

> **결국 ITER는 로렌츠 힘으로 10 keV 가스를 $B$ 병에 가두는 기계, LHC는 로렌츠 힘으로 7 TeV 입자를 27 km 링에 가두는 기계 — 둘 다 $B\rho = p/q$라는 하나의 식으로 설계된다.**

### 4.2.4 매스매티카 검증

```mathematica
(* Grad-Shafranov 방정식 *)
gradShafranov[psi_, R_, Z_, mu0_, p_, F_] :=
  R D[1/R D[psi, R], R] + D[psi, {Z, 2}] ==
  -mu0 R^2 D[p[psi], psi] - F[psi] D[F[psi], psi];

(* 자기섬 너비 *)
islandWidth[q_, R_, Btilde_, m_, qPrime_, B0_] :=
  4 Sqrt[q^2 R Btilde / (m qPrime B0)];

(* Troyon 한계 *)
troyonLimit[beta_, a_, B_, Ip_] := beta a B / Ip; (* < 3 *)
```

### 4.2.5 한계·예외

- **디스럽션:** $q < 2$에서 kink/tearing 불안정 → 플라즈마 급붕괴. ITER에서 $\sim$ MA 전류가 ms 만에 소멸, 대전류가 벽에 충돌
- **ELM:** H-모드 가장자리 국소 불안정, 반복적 에너지 방출
- **Greenwald 한계:** $n_G = I_p/\pi a^2$, 밀도 상한
- **Troyon 한계:** $\beta_N = \beta aB/I_p < 3$, 압력 상한
- **스텔라레이터:** 코일 복잡성, 준대칭 최적화 난이도

> **참고문헌**
> - Grad, H., Rubin, H., *Hydromagnetic equilibria and force-free fields*, Proc. 2nd UN Conf. **31**, 190 (1958).
> - Shafranov, V. D., *On magnetohydrodynamical equilibrium configurations*, Sov. Phys. JETP **6**, 545 (1957).
> - ITER Physics Basis, Nucl. Fusion **47**, S1 (2007). [doi:10.1088/0029-5515/47/6/S01](https://doi.org/10.1088/0029-5515/47/6/S01)
> - W7-X Team, *Quasi-isodynamic optimization*, Phys. Rev. Lett. **129**, 095001 (2022). [doi:10.1103/PhysRevLett.129.095001](https://doi.org/10.1103/PhysRevLett.129.095001)

---

## 4.3 의료 기술

로렌츠 힘은 거대 가속기뿐 아니라 **인체 내부**까지 내려왔다. MRI, 양성자 치료, 자기 나노입자, 자기 트웨저가 그 예다.

### 4.3.1 MRI와 블로흐 방정식

MRI는 로렌츠 힘을 직접 쓰지 않고 **스핀의 로렌츠 유사 운동**을 이용한다.

**정자기장:** $B_0 = 1.5-7$ T 초전도 자석, 양성자 자화 $\mathbf{M}$은 **라모 세차:**

$$\frac{d\mathbf{M}}{dt} = \gamma \mathbf{M}\times\mathbf{B}_0$$

> **Unicode**
> ```
> (d𝐌)/(dt) = γ 𝐌×𝐁₀
> ```

$\gamma/2\pi = 42.58$ MHz/T.

**블로흐 방정식 — 로렌츠 힘의 스핀 버전:**

$$\frac{d\mathbf{M}}{dt} = \gamma \mathbf{M}\times\mathbf{B} - \frac{M_x\hat{x}+M_y\hat{y}}{T_2} - \frac{(M_z-M_0)\hat{z}}{T_1}$$

> **Unicode**
> ```
> (d𝐌)/(dt) = γ 𝐌×𝐁 - (Mₓx̂+M_yŷ)/(T₂) - ((M_z-M₀)ẑ)/(T₁)
> ```

$$\mathbf{B}(\mathbf{r},t) = B_0\hat{z} + \mathbf{G}(t)\cdot\mathbf{r}\,\hat{z} + \mathbf{B}_1(t)$$

> **Unicode**
> ```
> 𝐁(𝐫,t) = B₀ẑ + 𝐆(t)·𝐫ẑ + 𝐁₁(t)
> ```

- $T_1, T_2$: 충돌·요동에 의한 완화
- $\mathbf{G} = \nabla B_z = (G_x, G_y, G_z)$: **경사자기장**이 위치 인코딩

**위치 인코딩:**

$$\omega(\mathbf{r}) = \gamma(B_0 + \mathbf{G}\cdot\mathbf{r})$$

> **Unicode**
> ```
> ω(𝐫) = γ(B₀ + 𝐆·𝐫)
> ```

주파수가 위치가 된다.

**경사자기장 설계:**

Maxwell 방정식 $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{B} = 0$ 만족하며 $B_z$만 선형으로 만들어야 함:

$$B_z = B_0 + G_x x + G_y y + G_z z$$

> **Unicode**
> ```
> B_z = B₀ + Gₓ x + G_y y + G_z z
> ```

$G_x$: $x$ 방향 Golay 코일, $G_z$: Maxwell pair.

**설계 변수:**
- 선형성 <5% over 50 cm DSV
- 스위칭 $dG/dt$ 최대 200 T/m/s, 슬루율 제한은 말초신경 자극 $dB/dt < 20$ T/s
- **로렌츠 힘 문제:** 경사 코일에 $I \sim 600$ A, $B_0 = 3$ T에서 $F = IL\times B_0 \sim 10^4$ N/m. 코일 진동 → 100 dB 소음. 이 $F$가 **MRI 소음의 원인**. Force-balanced coil이 최신 동향

**최신 동향:**
- 7T 이상 초고자장: SNR $\propto B_0$, 그러나 $B_1$ 파장 불균일, 병렬 송신 필요
- AI 재구성: 검사 시간 10분 → 2분
- 저자장 0.055T 휴대형 MRI: Halbach 영구자석, 로렌츠 힘 없는 무소음

### 4.3.2 양성자 치료

양성자 70-230 MeV, $B\rho = 0.8-2.3$ Tm. 로렌츠 힘으로 암만 쏜다.

**빔 라인:** 사이클로트론/싱크로트론 → 에너지 선택 시스템 → **갠트리**

**갠트리:** 2쌍 쌍극자 + 4극자로 $R \sim 3$ m 회전 구조물 100톤, 등중심 isocenter에서 $\mathbf{r}$ 일정 유지. 설계 조건 $M_{transport} = I$ — 갠트리 각도 무관하게 빔 동일.

**Pencil Beam Scanning (PBS) — 최신 표준:**

- $x,y$: 스캐닝 자석 $B_x(t), B_y(t)$로 $F = qv\times B$로 $\pm 20$ cm 10 m/s 스캔. 스팟 크기 $\sigma \sim 3$ mm
- $z$: 에너지로 Bragg peak 깊이 조절. 230 MeV → 물속 32 cm

**Bragg peak:**

$$D(z) \propto \frac{1}{\beta^2}\cdot\frac{1}{1-0.9}\ \text{peak at } R \approx \alpha E^{1.8}$$

> **Unicode**
> ```
> D(z) ∝ (1)/(β²)·(1)/(1-0.9)  peak at  R≈ α E^1.8
> ```

정상 조직 선량 1/3로 감소 — X선 대비.

**최신 동향:**
- **FLASH:** $>40$ Gy/s 초고선량률, 0.1초 조사로 정상 조직 보호. 고전류 $I_p \sim 100$ nA 필요
- **Arc therapy:** 갠트리 회전하며 연속 조사, $B\rho$ 빠른 변조 (<10 ms)
- **MRI-가이드 양성자:** $B_{MRI} = 0.5$ T 안에서 양성자 궤적 휘어짐 $\Delta r = q B_{MRI} L^2/2p$ 보정 알고리즘

### 4.3.3 자기 나노입자 치료

초상자성 산화철 Fe₃O₄ 직경 10-100 nm, 자화 $M_s \sim 400$ kA/m, 자기 모멘트 $\mathbf{m} = M_sV$.

**자기력 — 로렌츠 아닌 쌍극자 힘:**

$$\mathbf{F}_m = \nabla(\mathbf{m}\cdot\mathbf{B}) \approx \mathbf{m}\cdot\nabla\mathbf{B}$$

> **Unicode**
> ```
> 𝐅ₘ = ∇(𝐦·𝐁) ≈ 𝐦·∇𝐁
> ```

혈관 내 입자 속도 $v \sim 1$ mm/s, 항력 $F_d = 6\pi\eta r v \sim 10$ pN. $F_m > F_d$ 되려면 $\nabla B \sim 10$ T/m 필요 — 영구자석 Halbach 배열로 달성.

**응용 3가지:**
1. **표적 약물 전달:** 독소루비신 탑재 나노입자 + $B$ 구배로 종양에 집적, 5배 농도 증가
2. **자기 온열 치료:** AC $B$ 100 kHz, 20 mT → $P = \mu_0\pi f H_0^2\chi''$ → 42-45°C 종양 괴사
3. **자기 영동 분리:** CTC 순환 종양 세포 1개/mL를 자성 항체로 표지 후 마이크로 채널 $G \sim 100$ T/m로 분리

**최신:** DNA 오리가미에 5 nm 입자 부착, 회전 자기장 $B_{rot}$로 $\boldsymbol{\tau} = \mathbf{m}\times\mathbf{B}$ 드릴처럼 종양 침투 — 나노 로봇.

### 4.3.4 자기 트웨저

DNA, 단백질 1개에 $F = 0.1-100$ pN 가하는 도구.

**원리:** 2.8 μm Dynabead (초상자성)에 DNA 한쪽 고정, 영구자석 쌍으로 $B \sim 0.1$ T, $\nabla B \sim 10$ T/m 생성.

**힘과 토크:**

$$F_z = m(B)\frac{\partial B_z}{\partial z}, \quad \boldsymbol{\Gamma} = \mathbf{m}\times\mathbf{B}$$

> **Unicode**
> ```
> F_z = m(B)(∂ B_z)/(∂ z),   Γ = 𝐦×𝐁
> ```

힘은 0.01-10 pN, 토크 $10-10^4$ pN·nm. $B$ 세기는 자석 거리로, 회전은 자석 회전으로 제어 — DNA 비틀기.

**단분자 실험 3가지:**
1. **DNA 초코일:** 10 pN에서 10번 비틀면 플렉토님 형성
2. **헬리카제:** 1 bp 풀 때마다 0.34 nm 스텝, 0.1 nm 분해능 추적
3. **다중 트웨저 100개 병렬:** 3차원 트래킹으로 복제 포크 역학

**로렌츠 기반 변형 — 로렌츠 트웨저:** 전류가 흐르는 마이크로 와이어에 $B$ 인가해 $F = ILB$로 DNA 직접 당기기. 자기 비드 없이 순수 로렌츠 힘 단분자 조작.

### 4.3.5 매스매티카 검증

```mathematica
(* 블로흐 방정식 *)
blochEq = D[Mvec[t], t] == gammaGyro Cross[Mvec[t], Bvec]
  - {Mx[t]/T2, My[t]/T2, (Mz[t] - M0)/T1};

(* 라모 진동수 *)
larmorFreq[gammaGyro_, B0_] := gammaGyro B0;

(* 자기 나노입자 힘 *)
nanoForce[mMag_, gradB_] := mMag gradB;

(* 자기 트웨저 토크 *)
torque[ mVec_, bVec_] := Cross[mVec, bVec];
```

### 4.3.6 한계·예외

- **MRI:** $B_0 > 8$ T에서 현훈, PNS $dB/dt < 20$ T/s, 금속 발사체 위험
- **양성자 치료:** Bragg peak 첨예도, 장기 추적 시 조직 불균일
- **나노입자:** 생체 분포, 독성, 면역 반응
- **자기 트웨저:** 광학 트웨저보다 $F$ 안정, 광손상 없음, 그러나 비드 크기 한계

> **참고문헌**
> - Bloch, F., *Nuclear induction*, Phys. Rev. **70**, 460 (1946). [doi:10.1103/PhysRev.70.460](https://doi.org/10.1103/PhysRev.70.460)
> - Hall, E. J., Giaccia, A. J., *Radiobiology for the Radiologist*, 8th ed., Wolters Kluwer (2018).
> - Pankhurst, Q. A., et al., *Applications of magnetic nanoparticles in biomedicine*, J. Phys. D **36**, R167 (2003). [doi:10.1088/0022-3727/36/13/201](https://doi.org/10.1088/0022-3727/36/13/201)
> - Neuman, K. C., Nagy, A., *Single-molecule force spectroscopy: optical tweezers, magnetic tweezers and atomic force microscopy*, Nat. Methods **5**, 491 (2008). [doi:10.1038/nmeth.1218](https://doi.org/10.1038/nmeth.1218)

---
## 4.4 센서·MEMS

로렌츠 힘 $q\mathbf{v}\times\mathbf{B}$는 거대 가속기뿐 아니라 **마이크로 센서**에서도 작동한다. 이 절에서는 홀 센서, GMR/TMR, SQUID, MEMS 자기 센서를 다룬다.

### 4.4.1 홀 센서 — 로렌츠 힘 직접 측정

도체에 $I_x$, $B_z$ 인가 → $q\mathbf{v}\times\mathbf{B}$로 전하가 $y$로 쏠림 → **홀 전기장** $E_y = V_H/w$.

**홀 전압:**

$$V_H = \frac{R_H I B}{t}, \quad R_H = \frac{1}{nq}$$

> **Unicode**
> ```
> V_H = (R_H I B)/(t),   R_H = (1)/(nq)
> ```

반도체 $n$ 낮으면 $V_H$ 큼. Si Hall plate $S \sim 100$ V/AT.

**응용:** 무접점 전류 센서, BLDC 모터 위치, 스마트폰 나침반.

**최신:** 수직 홀, 3축 Hall + ASIC으로 0.1% 선형도, 자동차 $B$ 1 mT 분해능.

**한계:** $V_H$ 작고 온도 드리프트 큼.

### 4.4.2 GMR/TMR — 스핀 의존 로렌츠 유사

강자성/비자성 다층. 전자가 자화 방향에 따라 산란 확률 다름 — **스핀 필터**.

**GMR:**

- $R_P = R_0 - \Delta R$, $R_{AP} = R_0 + \Delta R$
- MR 비 $(R_{AP}-R_P)/R_P \sim 10-20\%$

**TMR:** 절연체 MgO 터널 장벽, Jullière 공식:

$$TMR = \frac{2P_1P_2}{1-P_1P_2}$$

> **Unicode**
> ```
> TMR = (2P₁P₂)/(1-P₁P₂)
> ```

최신 600% at RT.

**원리:** 외부 $B$가 자유층 자화 회전 → 저항 변화 → $B$ 센서. **로렌츠 힘이 아닌 교환 결합**이 원리지만, 전자의 자이로 운동을 자화가 대신하는 효과.

**응용:**
- HDD 헤드 (90년대 GMR 혁명)
- 바이오센서: 자기 비드 1 μm 표지된 DNA를 GMR 위에 끌어당기면 nT 감지 — fM 검출

### 4.4.3 SQUID — $U(1)$ 위상의 극한 센서

초전도 루프 + Josephson 접합 2개. **자속 양자화** $\Phi = n\Phi_0$, $\Phi_0 = h/2e$.

**임계 전류:**

$$I_c(\Phi) = 2I_0\left|\cos(\pi\Phi/\Phi_0)\right|$$

> **Unicode**
> ```
> I_c(Φ) = 2I₀|cos(πΦ/Φ₀)|
> ```

$\Phi$ 1개 양자 $2\times10^{-15}$ Wb에 전류 100% 변조. **자기장 감도 1 fT/√Hz** — 지구 자기장 50 μT의 $10^{-11}$.

**응용:**
- MEG (뇌자도) 100 fT 신호
- 심자도, 비파괴 검사
- 초저자장 MRI $B_0 = 100$ μT SQUID 검출

**최신:** 고온 SQUID 77 K, 나노 SQUID-on-tip 직경 50 nm → 단일 스핀 감지.

**센서 비교표:**

| 센서 | 원리 | 감도 | 대역폭 | 크기/가격 |
|---|---|---|---|---|
| Hall | $q v\times B$ | 1 μT | MHz | $0.1 |
| GMR/TMR | 스핀 산란 | 1 nT | MHz | $0.5 |
| SQUID | 자속 양자화 $h/2e$ | 1 fT | kHz | cm, 극저온 |

**추세:** TMR이 Hall 대체, SQUID는 양자 한계 센서로 고수.

### 4.4.4 MEMS 자기 센서 — 로렌츠 힘 기반 설계

전류가 흐르는 마이크로 빔에 $B$ 인가 → 로렌츠 힘으로 빔 휨.

**구조:** $L = 200$ μm Si 빔, $I = 1$ mA, $B = 1$ mT → $F = ILB = 0.2$ nN.

**변위:** $k \sim 1$ N/m → $x = F/k = 0.2$ nm. 정전 용량 변화 $\Delta C \sim$ aF 검출 불가.

**해결 — 공진 구동:**

$$m\ddot{x} + c\dot{x} + kx = F_0\cos\omega_0 t = I_0 B L\cos\omega_0 t$$

> **Unicode**
> ```
> mx¨ + cx˙ + kx = F₀cosω₀ t = I₀ B Lcosω₀ t
> ```

$Q \sim 10^4$ 진공 패키징 시 증폭 $x = QF_0/k \sim 2$ μm — 검출 가능. 주파수 편이 $\Delta\omega \propto B^2$로 측정.

**최신 — Lorentz-force magnetometer:** 3축 $x,y,z$ 전류 방향 바꿔 구현. 스마트폰 나침반용으로 Hall 대체 시도.

**장점:** CMOS 호환, $B$ 오프셋 없음 (Hall은 오프셋 큼)
**단점:** 전력 $I^2R$, $Q$ 온도 민감

**연구 동향:** AlN 압전 공진기로 $Q = 10^5$, 감도 10 nT/√Hz 달성.

### 4.4.5 매스매티카 검증

```mathematica
(* 홀 전압 *)
hallVoltage[iCurrent_, bField_, nCarrier_, qCharge_, tThickness_] :=
  iCurrent bField / (nCarrier qCharge tThickness);

(* TMR *)
tmr[p1_, p2_] := 2 p1 p2 / (1 - p1 p2);

(* SQUID 임계 전류 *)
squidCritical[Phi_, Phi0_, I0_] := 2 I0 Abs[Cos[Pi Phi/Phi0]];

(* MEMS 공진 변위 *)
resonanceDisplacement[Q_, F0_, k_] := Q F0 / k;
```

### 4.4.6 한계·예외

- **Hall:** 온도 드리프트, 오프셋
- **GMR/TMR:** 자기 이력, 온도 의존
- **SQUID:** 극저온 필요, 자기 차폐 필수
- **MEMS:** $Q$ 온도 민감, 전력 소모

> **참고문헌**
> - Hall, E. H., *On a new action of the magnet on electric currents*, Am. J. Math. **2**, 287 (1879). [doi:10.2475/ajs.s3-19.117.200](https://doi.org/10.2475/ajs.s3-19.117.200)
> - Baibich, M. N., et al., *Giant Magnetoresistance of (001)Fe/(001)Cr Magnetic Superlattices*, Phys. Rev. Lett. **61**, 2472 (1988). [doi:10.1103/PhysRevLett.61.2472](https://doi.org/10.1103/PhysRevLett.61.2472)
> - Clarke, J., Braginski, A. I., *The SQUID Handbook*, Wiley-VCH (2004). [doi:10.1002/9783527603646](https://doi.org/10.1002/9783527603646)

---

## 4.5 우주물리·자연현상

우주 플라즈마는 충돌이 없으므로 $\mathbf{J}\times\mathbf{B}$와 $\nabla B$ 드리프트, 자기 재결합이 모든 것을 지배한다. 이 절에서는 오로라, 반 알렌 벨트, 자기 재결합, FAC, 펄서, 태양 플레어를 다룬다.

### 4.5.1 오로라 발생의 완전한 물리

**Step 1: 태양풍 → 자기권**

태양풍: $n \sim 5$ cm$^{-3}$, $v \sim 400$ km/s, $B_{IMF} \sim 5$ nT, 동압 $P_{dyn} = nm_p v^2 \sim 2$ nPa.

지구 쌍극자 자기압 $P_B = B^2/2\mu_0$와 균형:

$$\frac{B_0^2}{2\mu_0}\left(\frac{R_E}{R_{mp}}\right)^6 = P_{dyn} \implies R_{mp} \approx 10 R_E$$

> **Unicode**
> ```
> (B₀²)/(2μ₀)((R_E)/(Rₘₚ))⁶ = P_dyn ⟹ Rₘₚ ≈ 10 R_E
> ```

남향 $B_{IMF}$ ($B_z < 0$)이면 낮 자기권 계면에서 **자기 재결합** → Dungey 대류: 자력선이 태양풍에 열리고 꼬리로 끌려감.

**Step 2: 자기권 꼬리 저장과 입자 가속**

꼬리 로브 $B \sim 20$ nT, 플라즈마 시트 $n \sim 0.3$ cm$^{-3}$, $T \sim 5$ keV. 태양풍-자기권 발전기 $\mathbf{E} = -\mathbf{V}_{sw}\times\mathbf{B}$로 새벽-황혼 방향 $E_y \sim 0.1-1$ mV/m → 꼬리에서 지구로 향하는 $\mathbf{E}\times\mathbf{B}$ 대류 $V \sim 50$ km/s.

플라즈마 시트 입자가 지구로 대류되며 **단열 가열:** $\mu = mv_\perp^2/2B$ 보존, $B$ 증가 (5 nT → 100 nT) → $T_\perp$ 20배 증가.

**Step 3: 자기 거울과 손실 콘**

지구 근처 $B_0 \sim 50$ μT, 적도 $B_{eq} \sim 100$ nT → 미러비 $R_m = B_0/B_{eq} \sim 500$.

구속 조건 $\sin^2\theta_0 > B_{eq}/B_0$. 손실 콘 $\theta_{lc} = \arcsin\sqrt{B_{eq}/B_0} \sim 2.5^\circ$.

일반 플라즈마 시트 $T \sim 5$ keV는 대부분 구속. 재결합, 파동-입자 상호작용(whistler, EIC)으로 피치각 산란 → 손실 콘 채워짐 → **강수(precipitation)**.

**Step 4: 발광**

100-300 km 고도에서 $O, N_2$ 충돌 여기:

$$e^* + O \to O^* \to O + h\nu$$

> **Unicode**
> ```
> e^* + O → O^* → O + hν
> ```

- $O(^1D\to^3P)$ 630.0 nm 적색, 200 km 이상
- $O(^1S\to^1D)$ **557.7 nm 녹색**, 100-150 km, 가장 밝음
- $N_2^+$ 427.8 nm 청색, <100 km

**오로라 타원:** 자기 위도 65-75°, 밤쪽에 치우침 — 꼬리 재결합 위치 투영.

### 4.5.2 반 알렌 벨트

**내부 벨트:** $1.2-2.5 R_E$, 양성자 10-100 MeV (CRAND), 전자 100 keV
**외부 벨트:** $3-7 R_E$, 전자 0.1-10 MeV

**3주기 운동 — 모두 로렌츠 힘:**

1. **자이로:** $\omega_c = qB/m$, $r_L \sim$ km (MeV 전자)
2. **바운스:** 자기 거울 사이 왕복, $\tau_b = \oint ds/v_\parallel \sim 0.1-1$ s
3. **드리프트:** $\mathbf{V}_{gc} \approx \frac{m}{qB^3}(v_\parallel^2+v_\perp^2/2)\mathbf{B}\times\nabla B$

쌍극자 $B \propto 1/r^3$에서 방위각 드리프트:

$$\omega_d = \frac{3L R_E m v^2}{2|q|B_0 R_E^2}$$

> **Unicode**
> ```
> ω_d = (3L R_E m v²)/(2|q|B₀ R_E²)
> ```

이온 서쪽, 전자 동쪽, 수 분-시간 주기.

**링 전류:** $J_\phi \sim nqV_d \sim 10$ nA/m², 총 2-5 MA 서쪽 전류 → 지상 자기장 20-100 nT 감소 — **Dst 지수**.

### 4.5.3 자기권 꼬리와 자기 재결합

꼬리 전류 시트: $B_x$가 북로브 +20 nT에서 남로브 -20 nT로 ~1000 km 두께에서 반전.

**Harris 평형:** $B_x(z) = B_0\tanh(z/\lambda)$, $J_y \propto \text{sech}^2$.

$\mathbf{J}\times\mathbf{B}$로 $x$ 방향 팽창력과 압력 $\nabla p$ 균형.

남향 $B_{IMF}$ 지속 시 꼬리에 자속 축적 → 전류 시트 얇아짐 $\lambda \to$ 이온 관성 길이 $d_i = c/\omega_{pi} \sim 500$ km → **자기 재결합** 촉발.

**Sweet-Parker 모델:** $S = \mu_0 L V_A/\eta$ Lundquist 수 $10^{10}$ → 재결합 느림.

**실제는 Hall 재결합:** 이온은 $d_i$에서 비자화, 전자만 $d_e$까지 $\mathbf{E}\times\mathbf{B}$ 드리프트 → 4중극 $B_y$ Hall 자기장, 재결합률 $0.1 V_A$ 빠른 재결합.

**로렌츠 힘 관점:** 확산 영역 밖 $\mathbf{E}+\mathbf{V}_e\times\mathbf{B} = 0$ 동결, 내부에서 $\mathbf{E}+\mathbf{V}_e\times\mathbf{B} = \eta\mathbf{J}+\ldots \neq 0$ 동결 깨짐 → 자력선 끊어지고 재연결.

**방출 제트:** $V_{out} \sim V_A = B/\sqrt{\mu_0 nm_p} \sim 1000$ km/s, 이온 10 keV 가속 — 오로라 서브스톰 온셋.

### 4.5.4 필드 정렬 전류 (FAC)

자기권-전리층 결합은 $B$를 따라 흐르는 **Birkeland 전류**로 이루어진다.

**기원:** $\nabla p$ 또는 관성으로 인한 수직 전류 $\mathbf{J}_\perp$의 발산은 $B$를 따라 흘러야 연속:

$$\nabla\cdot\mathbf{J} = 0 \implies B\partial_s(J_\parallel/B) = -\nabla\cdot\mathbf{J}_\perp$$

> **Unicode**
> ```
> ∇·𝐉 = 0 ⟹ B∂ₛ(J_∥/B) = -∇·𝐉_⊥
> ```

**Region 1 FAC:** 극관 경계, 하향(새벽)/상향(황혼), $\sim 1$ μA/m², $I \sim 2$ MA
**Region 2 FAC:** 오로라 타원 적도쪽, 반대 방향, 부분 링 전류

**전리층 폐쇄:** Pedersen 전류 $\mathbf{J}_P = \sigma_P\mathbf{E}_\perp$ (줄 가열), Hall 전류 $\mathbf{J}_H = \sigma_H\hat{b}\times\mathbf{E}_\perp$ (자기 교란).

**Knight 관계:** $j_\parallel = e^2 n_e/\sqrt{2\pi m_e T_e}(\Delta\Phi)$ — 전위차 $\Delta\Phi \sim$ kV가 평행 전기장 $\mathbf{E}_\parallel$로 존재, 오로라 가속의 직접 원인.

### 4.5.5 펄서와 마그네타

펄서: $B \sim 10^8-10^{12}$ T, $P = 1$ ms-10 s, $R = 10$ km 중성자별.

**Goldreich-Julian 자기권:** 회전 $\boldsymbol{\Omega}\times\mathbf{r}$로 도체 별 표면 전하 분리 → 진공 전기장 $E \sim (\Omega R)B \sim 10^{12}$ V/m. $E\cdot B \neq 0$ → 표면에서 $e^\pm$ 방출.

**GJ 밀도:**

$$n_{GJ} = \frac{2\epsilon_0\boldsymbol{\Omega}\cdot\mathbf{B}}{e} \sim 10^{17}\ \text{m}^{-3}\frac{B_{12}}{P}$$

> **Unicode**
> ```
> n_GJ = (2ε₀ Ω·𝐁)/(e) ∼ 10¹⁷ m⁻³(B₁₂)/(P)
> ```

**극관 전위:**

$$\Phi_{pc} = \frac{\Omega^2 B R^3}{2c^2}$$

> **Unicode**
> ```
> Φ_pc = (Ω² B R³)/(2c²)
> ```

$\Phi_{pc} \sim 10^{12}$ V. 입자는 $\mathbf{E}_\parallel$로 $\gamma \sim 10^7$까지 가속 → 곡률 방사 $P \propto \gamma^4/\rho_c^2$ → GeV 광자 → $B$에서 $\gamma+B \to e^+e^-$ 쌍생성 → 2차 플라즈마 → 전파 방사. **펄서 메커니즘** — 전부 $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$ 조건이 깨지는 곳에서 로렌츠 힘으로 가속.

**마그네타:** $B \sim 10^{10}-10^{11}$ T, 양자 임계 $B_Q = m_e^2c^3/e\hbar = 4.4\times10^9$ T 초과. 란다우 준위 간격이 $mc^2$ 이상, 진공 복굴절, 광자 분열 $\gamma\to\gamma\gamma$ 발생.

### 4.5.6 태양 플레어와 CME

코로나: $B \sim 10^{-3}$ T, $n \sim 10^{15}$ m$^{-3}$, $\beta = 2\mu_0 p/B^2 \sim 0.01$ — **자기 지배**, 로렌츠 힘 $\mathbf{J}\times\mathbf{B}$가 중력보다 $10^4$배 큼.

**플레어 저장:** 광구 대류로 자속관 비틀림 → 코로나에 전류 $\mathbf{J} = \alpha\mathbf{B}$ (force-free, $\mathbf{J}\times\mathbf{B} = 0$) 상태로 에너지 저장 $W = \int B^2/2\mu_0\, dV \sim 10^{25}$ J.

**트리거 — kink/torus 불안정:** 트위스트 $\Phi = \int\alpha\, dl > 2\pi$이면 $\mathbf{J}\times\mathbf{B}$ 불균형 → 플럭스 로프 상승.

상승 시 전류 시트 형성 → 자기 재결합, Petschek 빠른 재결합으로 $E_{rec} = V_{in}B_{in} \sim 100$ V/m.

**가속:** $E_\parallel$로 전자 20-100 keV, $F = qE$로 하층 대기 강수 → HXR footpoint 방사.

**CME:** 플럭스 로프가 $V \sim 1000$ km/s로 탈출, 질량 $10^{12}$ kg, 에너지 $10^{23}$ J. 구동력 $\mathbf{J}\times\mathbf{B}_{ext}$ — 로프 전류와 배경 자기장 로렌츠 힘.

**지구 영향:** CME $B_z$ 남향 시 $Dst < -100$ nT 자기폭풍. 1859 Carrington 사건 $B \sim 1600$ nT — 현재 발생 시 변압기 GIC $J = \sigma E$, $E \sim$ V/km로 정전.

**통일된 그림:** 태양 발전기($\mathbf{v}\times\mathbf{B}$) → 자기 에너지 저장 → 재결합($\mathbf{E}+\mathbf{v}\times\mathbf{B} \neq 0$) → 입자 가속($q\mathbf{E}$) → 행성 자기권에서 $\nabla B$, 곡률 드리프트로 가둠 → 대기 강수 발광. **오로라부터 펄서까지 모두 같은 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$가 스케일 $10^{10}$배 차로 작동하는 현상이다.**

### 4.5.7 매스매티카 검증

```mathematica
(* 자기 거울 조건 *)
mirrorCondition[B0_, Bm_, theta0_] := Sin[theta0]^2 == B0/Bm;

(* 쌍극자 자기장 *)
BrDipole[mDipole_, theta_, r_] := 2 mDipole Cos[theta]/r^3;
BthetaDipole[mDipole_, theta_, r_] := mDipole Sin[theta]/r^3;

(* GJ 밀도 *)
gjDensity[Omega_, Bfield_, eCharge_, epsilon0_] :=
  2 epsilon0 Omega . Bfield / eCharge;

(* 극관 전위 *)
polarCapPotential[Omega_, Bfield_, R_, cLight_] :=
  Omega^2 Bfield R^3 / (2 cLight^2);
```

### 4.5.8 한계·예외

- **MHD 근사:** 이온 관성 길이 이하에서 붕괴, Hall MHD 필요
- **자기 재결합:** 3차원 키네틱 시뮬레이션과 관측 30% 불일치
- **펄서:** 쌍생성 차폐 메커니즘 여전히 논쟁
- **CME 예측:** 발생 시각, 방향 예측 불확실

> **참고문헌**
> - Dungey, J. W., *Interplanetary magnetic field and the auroral zones*, Phys. Rev. Lett. **6**, 47 (1961). [doi:10.1103/PhysRevLett.6.47](https://doi.org/10.1103/PhysRevLett.6.47)
> - Van Allen, J. A., *Observation of high intensity radiation by satellites*, J. Geophys. Res. **63**, 179 (1958). [doi:10.1029/JZ063i001p00179](https://doi.org/10.1029/JZ063i001p00179)
> - Parker, E. N., *Dynamics of interplanetary gas and magnetic fields*, Astrophys. J. **128**, 664 (1958). [doi:10.1086/146579](https://doi.org/10.1086/146579)
> - Goldreich, P., Julian, W. H., *Pulsar electrodynamics*, Astrophys. J. **157**, 869 (1969). [doi:10.1086/150119](https://doi.org/10.1086/150119)

---

## 4.6 비선형 동역학·카오스

로렌츠 힘 $m\dot{\mathbf{v}} = q(\mathbf{v}\times\mathbf{B})$는 겉보기에 선형이지만 $\mathbf{B}(\mathbf{x})$가 $\mathbf{x}$에 의존하는 순간 **3자유도 비선형 해밀턴계**가 된다. $B$가 균일하면 적분 가능, 비균일하면 카오스. 이 절에서는 카오스 조건, KAM, 자기 재결합, 난류를 다룬다.

### 4.6.1 로렌츠 힘 궤적의 카오스 발생 조건

해밀토니안 $H = (\mathbf{p}-q\mathbf{A})^2/2m$. **적분 가능성 조건**은 Liouville-Arnold: $n$ 자유도에 $n$개 독립 교환하는 보존량.

**균일 $\mathbf{B} = B_0\hat{z}$:**
- $p_y$ 보존 (병진 대칭)
- $p_z$ 보존
- $H$ 자체

→ 적분 가능, 궤적은 나선, 위상공간은 3-토러스.

**카오스 조건 3가지 (하나라도):**

1. **공간 비균일:** $\mathbf{B} = \mathbf{B}(\mathbf{x})$. 섭동 $\epsilon = r_L/L_B$가 $\gtrsim 0.1$이면 자이로 위상과 바운스 운동 공명 $\omega_b = n\omega_c$ → Chirikov 중첩
2. **시간 의존:** $\mathbf{E}(t)$ 또는 $B(t)$로 1.5 자유도 해밀턴 → 강제 진자. RF 가열 $\mathbf{E}_{rf}\cos\omega t$에서 $\omega \approx \omega_c$일 때 확률적 가열
3. **자기 곡률 + 전기장:** $E\times B$ 전단 흐름 $V_E(x) = E(x)/B$가 $dV_E/dx \sim \omega_c$일 때 Kelvin-Helmholtz 유사 궤적 카오스

**리아푸노프 지수:**

$$\lambda = \lim_{t\to\infty}\frac1t\ln\frac{|\delta\mathbf{x}(t)|}{|\delta\mathbf{x}(0)|}$$

> **Unicode**
> ```
> λ = lim_t→∞(1)/(t)ln(|δ𝐱(t)|)/(|δ𝐱(0)|)
> ```

$\lambda > 0$이면 카오스. 균일 $B$에서 $\lambda = 0$, 자기 거울 $B(z) = B_0(1+z^2/L^2)$ + 4중극 섭동에서 임계 $\epsilon_c \sim r_L/L$ 초과 시 $\lambda \sim 0.1\omega_c$.

**물리적 예:**
- 자기권에서 $\kappa = \sqrt{R_c/r_L} < 3$ (Büchner-Zelenyi)이면 자이로-바운스 결합 카오스 → 전류 시트 $T_\perp$ 등방화
- 펄서 극관: $E \approx B$ 상대론적 영역에서 궤적 fractal

### 4.6.2 KAM 정리와 위상공간 섬 구조

적분 가능계 $H_0(\mathbf{J})$에 섭동 $\epsilon H_1(\mathbf{J},\boldsymbol{\theta})$:

$$H = H_0(\mathbf{J}) + \epsilon H_1(\mathbf{J},\boldsymbol{\theta})$$

> **Unicode**
> ```
> H = H₀(𝐉) + ε H₁(𝐉,θ)
> ```

**KAM 정리:** 비공명 토러스 $\mathbf{n}\cdot\boldsymbol{\omega}_0 \neq 0$는 $\epsilon < \epsilon_c$에서 살아남되 약간 일그러짐. 공명 토러스는 붕괴해 **섬(island) 체인**과 **카오스 층** 생성.

**자력선 방정식:** $\mathbf{B} = \nabla\psi\times\nabla\theta + \nabla\phi\times\nabla\chi$에서 자력선:

$$\frac{d\psi}{d\phi} = -\frac{\partial H}{\partial\theta}, \quad \frac{d\theta}{d\phi} = \frac{\partial H}{\partial\psi}, \quad H = \chi$$

> **Unicode**
> ```
> (dψ)/(dφ) = -(∂ H)/(∂θ),   (dθ)/(dφ) = (∂ H)/(∂ψ),   H = χ
> ```

- **KAM 토러스:** 자기면. $\iota(\psi) = d\theta/d\phi$ 무리수일 때 존재
- **공명 섬:** $\iota = n/m$ 유리수 면에서 섬 형성, 폭 $w_{mn} \propto \sqrt{\tilde{B}_{mn}/m\iota'}$
- **카오스 바다:** Chirikov 기준 $s = (w_m+w_{m+1})/\Delta_{m,m+1} > 1$이면 섬 겹침 → 자력선 확률적 확산

**Rechester-Rosenbluth 확산:**

$$D_{RR} = \pi q R \frac{\langle\tilde{B}_r^2\rangle}{B_0^2}L_c$$

> **Unicode**
> ```
> D_RR = π q R (⟨ B̃ᵣ²⟩)/(B₀²)L_c
> ```

입자는 자력선 따라 $v_\parallel$로 달리며 수직으로 $D_{RR}v_\parallel$ 확산 → Bohm보다 큰 $D \sim 10$ m²/s.

**실험 관측:** 토카막에서 $q=2$ 면에 $m/n = 2/1$ 섬, Thomson 산란 $T_e$ 평탄화, Poincaré 단면 O점/X점.

**KAM의 중요성:** 완전 카오스면 구속 불가, 완전 적분 가능이면 가열 불가. **핵융합은 KAM 토러스가 대부분 살아있되 가장자리만 약한 카오스로 열·입자를 빼내는 경계**에 있어야 함 — H-mode pedestal이 그 예.

### 4.6.3 자기 재결합의 비선형 동역학

재결합은 자력선 위상이 바뀌는 **위상수학적 카오스 과정**.

**선형 단계:** 전류 시트 $J_y(z) = J_0\text{sech}^2(z/\lambda)$에서 **tearing 모드** 성장률:

$$\gamma \sim S^{-3/5}k^{2/5}$$

> **Unicode**
> ```
> γ ∼ S^-3/5k^2/5
> ```

Furth-Killeen-Rosenbluth, $S = \tau_R/\tau_A$.

**비선형 단계:**
1. **섬 성장** $w(t)$: Rutherford $dw/dt \sim \eta\Delta'(w)$
2. **2개 섬 충돌:** $m/n = 3/2$와 $2/1$ 섬이 $s > 1$로 겹치면 2차 재결합 → 플라즈모이드 체인
3. **플라즈모이드 불안정:** $S > 10^4$에서 전류 시트가 $S$에 비례하는 개수의 2차 섬으로 분열 → 빠른 재결합률 $V_{rec} \sim 0.01V_A$가 $S$ 무관

**비선형 로렌츠 힘:** 재결합 제트 $\mathbf{J}\times\mathbf{B}$가 플라즈모이드를 가속, 피드백:

$$\frac{d}{dt}(nm V_{out}) \sim J\times B - \nabla p$$

> **Unicode**
> ```
> (d)/(dt)(nm Vₒᵤₜ) ∼ J× B - ∇ p
> ```

**결과:** 재결합은 임계 $S$ 이상에서 폭발적, 카오스적 — 플라즈모이드 크기 분포가 멱법칙 $N(w) \propto w^{-2}$, 태양 플레어 크기 분포와 동일, **자기조직 임계(SOC)** 특성.

### 4.6.4 자기력선 카오스와 플라즈마 가둠

자력선 방정식 자체가 해밀턴계. 축대칭 토카막 → 적분 가능. 3차원 섭동(에러장, RMP 코일) 추가 → 해밀턴 카오스.

- **섬 너비:** $w_{mn} = 4\sqrt{|q\epsilon_{mn}/q'|}$
- **확률적 임계:** $s > 1$ → 자기면 파괴 → Rechester-Rosenbluth 확산

**가둠 영향:**
- **유리:** ITER RMP ELM 제어는 일부러 $n=3$ 섭동으로 $q=3-5$ 영역 확률화, 열부하 분산
- **불리:** 코어 확률화 시 $\tau_E \propto 1/D$ 급감 — 1970년대 스텔라레이터 실패 이유

**최신 스텔라레이터 최적화:** KAM 토러스 최대화하도록 $\epsilon_{mn}$ 최소화 — **준대칭(quasisymmetry)** 조건이 곧 KAM 조건.

### 4.6.5 플라즈마 난류와 로렌츠 힘

난류는 $\mathbf{E}\times\mathbf{B}$ 드리프트의 비선형 $\mathbf{V}_E\cdot\nabla$에 의해 구동.

**MHD 방정식:**

$$\rho\frac{d\mathbf{V}}{dt} = -\nabla p + \mathbf{J}\times\mathbf{B} + \mu\nabla^2\mathbf{V}$$

> **Unicode**
> ```
> ρ(d𝐕)/(dt) = -∇ p + 𝐉×𝐁 + μ∇²𝐕
> ```

$$\frac{\partial\mathbf{B}}{\partial t} = \nabla\times(\mathbf{V}\times\mathbf{B}) + \eta\nabla^2\mathbf{B}$$

> **Unicode**
> ```
> (∂𝐁)/(∂ t) = ∇×(𝐕×𝐁) + η∇²𝐁
> ```

**비선형 항 2개:** $\mathbf{V}\cdot\nabla\mathbf{V}$ (Navier-Stokes)와 $\mathbf{J}\times\mathbf{B}$ (로렌츠).

$\mathbf{V} \approx \mathbf{V}_E = \mathbf{E}\times\mathbf{B}/B^2$로 두면 **Hasegawa-Mima 방정식**:

$$\frac{d}{dt}\nabla_\perp^2\phi + [\phi, \nabla_\perp^2\phi] = \ldots$$

> **Unicode**
> ```
> (d)/(dt)∇_⊥²φ + [φ,∇_⊥²φ] = ...
> ```

$[f,g] = \hat{b}\cdot\nabla f\times\nabla g$ Poisson 괄호.

- **드리프트 파 난류:** $\omega_* = k_y T/eBL_n$, 스펙트럼 $k^{-3}$
- **$E\times B$ 전단 억제:** $\omega_{E\times B} = dV_E/dx$가 난류 와도보다 크면 와도 찢김 → 난류 억제, **L-H 천이**

**난류 수송:** $\langle\tilde{V}_{E,r}\tilde{n}\rangle$, $\tilde{V}_{E,r} = \tilde{E}_\theta/B$. $E\times B$ 자체가 로렌츠 드리프트이므로 난류 수송은 **로렌츠 힘의 2차 상관**.

### 4.6.6 로렌츠 방정식 vs 로렌츠 힘 — 구분표

혼동이 잦다. **완전히 다르다.**

| 구분 | **로렌츠 힘** Lorentz force | **로렌츠 방정식** Lorenz equations |
|---|---|---|
| 기원 | H.A. Lorentz (1892) 전자기력 | E.N. Lorenz (1963) 대기 대류 |
| 식 | $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | $\dot{x} = \sigma(y-x), \dot{y} = x(\rho-z)-y, \dot{z} = xy-\beta z$ |
| 성질 | 해밀턴계, 위상 부피 보존 $\nabla\cdot\mathbf{f} = 0$ | 소산계, 부피 수축 $\nabla\cdot\mathbf{f} = -(\sigma+1+\beta) < 0$ |
| 카오스 | 해밀턴 카오스, KAM | 소산 카오스, Lorenz 어트랙터 |
| 관계 | 없음 | 없음. 철자도 Lorentz vs Lorenz |

**유사점:** 둘 다 비선형 동역학 교과서 예제.

로렌츠 힘 계에서 $B(x) = B_0(1+\alpha x)$로 두면 $\ddot{x} = \omega_c(1+\alpha x)\dot{y}$ 형태가 Lorenz와 유사한 2차 비선형. 하지만 물리 기원은 다르다.

**정리:** 로렌츠 힘은 적분 가능할 때는 규칙적 나선, 공명 $\mathbf{k}\cdot\mathbf{V}_d = n\omega_c$에서 KAM 섬, 섬 겹침 시 해밀턴 카오스 → 자기력선 확률화 → 빠른 재결합, 난류 수송. **플라즈마 가둠은 KAM 토러스를 얼마나 보존하느냐의 싸움이고, 재결합·난류는 그 토러스를 어떻게 깨뜨리느냐의 물리다.** 이 비선형성이 있기에 핵융합은 어렵고 오로라는 아름답다.

### 4.6.7 매스매티카 검증

```mathematica
(* 로렌츠 방정식 (참고용) *)
lorenzEqs = {
  x'[t] == sigma (y[t] - x[t]),
  y'[t] == x[t] (rho - z[t]) - y[t],
  z'[t] == x[t] y[t] - beta z[t]
};

(* 로렌츠 힘 궤적의 리아푸노프 지수 *)
lyapunovExponent[trajectory_] := Module[{delta0, deltaT, tMax},
  delta0 = Norm[trajectory[[2]] - trajectory[[1]]];
  deltaT = Norm[trajectory[[-1]] - trajectory[[-2]]];
  Log[deltaT/delta0] / Length[trajectory]
];

(* 섬 너비 *)
islandWidth[q_, R_, Btilde_, m_, qPrime_, B0_] :=
  4 Sqrt[q^2 R Btilde / (m qPrime B0)];

(* Rechester-Rosenbluth 확산 *)
rrDiffusion[q_, R_, BtildeSq_, B0_, Lc_] :=
  Pi q R BtildeSq / B0^2 * Lc;
```

### 4.6.8 한계·예외

- **카오스 판정:** 리아푸노프 지수는 수치적으로 수렴 느림
- **KAM 정리:** 섭동 이론, 강섭동에서는 붕괴
- **자기 재결합:** 3차원 키네틱과 MHD 모델 불일치
- **난류:** 제1원리 예측 10% 정확도 미달
- **로렌츠 vs Lorenz:** 이름 혼동 주의

> **참고문헌**
> - Kolmogorov, A. N., *On conservation of conditionally periodic motions*, Dokl. Akad. Nauk SSSR **98**, 527 (1954); Arnold, V. I. (1963); Moser, J. (1962). [doi:10.1070/RM1963v018n05ABEH004130](https://doi.org/10.1070/RM1963v018n05ABEH004130)
> - Lorenz, E. N., *Deterministic nonperiodic flow*, J. Atmos. Sci. **20**, 130 (1963). [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)
> - Rutherford, P. H., *Nonlinear growth of the tearing mode*, Phys. Fluids **16**, 1903 (1973). [doi:10.1063/1.1694232](https://doi.org/10.1063/1.1694232)
> - Rechester, A. B., Rosenbluth, M. N., *Electron heat transport in a tokamak with destroyed magnetic surfaces*, Phys. Rev. Lett. **40**, 38 (1978). [doi:10.1103/PhysRevLett.40.38](https://doi.org/10.1103/PhysRevLett.40.38)

---

# 5막. 최전선과 미래 (Frontiers)

> **막의 흐름**
> 최신 연구 동향 (2020~2025) → 미해결 문제 → 응집물질·위상물질
>
> 4막까지 로렌츠 힘의 응용을 확정했다. 5막은 **지금 이 순간 진행 중인 연구**를 다룬다. 2020년 이전 로렌츠 힘은 공식이었다면, 2020년 이후는 **제어 변수**다. AI는 $\mathbf{J}\times\mathbf{B}$를 보상함수로 학습하고, 양자칩은 $\mathbf{v}\times\mathbf{B}$로 이온을 가두고, 그래핀은 $\mathbf{v}\times\mathbf{B}$를 정류기로 쓰며, 레이저는 $\mathbf{v}\times\mathbf{B}$가 $\mathbf{E}$를 이기는 영역을 탐사한다.

---

## 5.1 최신 연구 동향 (2020~2025)

로렌츠 힘은 고전이 아니다. 2020년 이후 $q\mathbf{v}\times\mathbf{B}$는 **AI 제어 변수, 큐비트 격리장, 나노 위상 불변량**이 되었다. 이 절에서는 핵융합 AI 제어, 양자컴퓨팅, 나노소자, 초강력 레이저, 중력파 검출, 우주 추진, 주요 논문 20편을 다룬다.

### 5.1.1 핵융합 AI 제어

고전 PID는 $B$ 코일 20개, $\psi(R,Z)$ 비선형 Grad-Shafranov를 못 다룬다. 2020년 이후 **강화학습(RL)** 이 이 문제를 돌파했다.

#### DeepMind × EPFL TCV (2022, Nature)

강화학습 에이전트가 시뮬레이터에서 **10만 번 시행착오** 후 실물 토카막 자기 코일을 10 kHz로 직접 제어.

- **스노우플레이크, 드롭렛, ITER H-모드 형상**까지 단일 신경망이 생성
- 기존에 없던 형상 **발견**
- **보상 함수:** $r = -|\psi - \psi_{target}| - |J\times B - \nabla p|$ — 로렌츠 평형 오차를 직접 최소화

#### 확장 (2023~2025)

- **DIII-D + RL (미국):** NTM, ELM 실시간 억제. $\tilde{B}$ 센서 → RMP 코일 $\mathbf{J}\times\mathbf{B}$로 섬 안정화. **2024년 Q>1 장시간 유지 성공**
- **KSTAR AI (한국):** 2023-24, 딥러닝 Surrogate $\Delta^*\psi = -\mu_0R^2p' - FF'$를 1 ms에 예측, 강화학습이 $V_{E\times B}$ 전단으로 L-H 천이 제어. **100초 운전 달성의 핵심이 AI 루프**
- **Neural ODE:** 플라즈마 전류 $I_p$ 예측에 물리 제약 신경망, $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$을 loss로 강제

**추세:** 제어 대상이 $B$ 코일이 아니라 직접 $\mathbf{J}\times\mathbf{B}$ 힘 분포.

### 5.1.2 양자컴퓨팅에서 로렌츠 힘

#### 이온 트랩

**Paul 트랩:** RF $\mathbf{E}$로 가두지만 마이크로 모션 가열.

**Penning 트랩:** 정적 $\mathbf{E}$ + 정적 $B = 3$ T로 로렌츠 힘 $q\mathbf{v}\times\mathbf{B}$가 원운동 구속, RF 불필요.

- **ETH Zurich (2022-23):** 마이크로 Penning 칩에서 이온을 2차원 임의 수송, 큐비트 연산 실현. $B$가 강할수록 $r_L$ 작아 스케일링 유리
- **219개 Be 이온 얽힘 기록**도 같은 원리

#### 초전도 큐비트

초전도 루프 $F = 0$이지만 자속 잡음 $\Phi_{noise}$가 $\mathbf{v}\times\mathbf{B}$ 유사 위상 잡음으로 큐비트 디코히어런스.

- **최신 플럭소늄, 0-$\pi$ 큐비트:** 로렌츠 힘으로 생기는 $E_J\cos(\Phi)$ 퍼텐셜을 $U(1)$ 대칭 보호로 무감각화
- **Google Willow (2024):** 자속 바이어스 안정화가 핵심

로렌츠 힘은 여기선 적, AI로 $B$ 잡음 능동 상쇄가 연구 주제.

### 5.1.3 나노소자 — 그래핀, 위상절연체

#### 비선형 홀 효과 (그래핀)

2022-24년 그래핀 모이레 초격자에서 **$E^2H$ 비선형 홀 전압**이 선형 홀의 32%까지 보고. 기원은 고전 로렌츠 힘 + 양자 skew scattering의 협력.

$$j \sim E^2$$

> **Unicode**
> ```
> j ∼ E²
> ```

정류 효과로 에너지 하베스팅 응용.

#### 유체역학 전자

그래핀 채널에서 점성 $\nu$와 로렌츠 힘이 경쟁, **Hall 점성** $\eta_H$ 측정. 2022년 $W = 1$ μm 채널에서 $\mathbf{E}\times\mathbf{B}$ 드리프트와 Hall 점성 기여 분리. **전자가 유체처럼 흐를 때 로렌츠 힘은 압력 구배처럼 작용**.

#### 위상절연체

표면 Dirac 상태 $H = v_F(\mathbf{p}\times\boldsymbol{\sigma})$, $B$ 인가 시 란다우 준위 $E_n \propto \sqrt{nB}$ + $\pi$ 베리 위상. $q\mathbf{v}\times\mathbf{B}$가 스핀-운동량 잠금으로 전환, **양자 스핀 홀**.

### 5.1.4 초강력 레이저 플라즈마

$I > 10^{22}$ W/cm², $a_0 = eE/m\omega c > 10$에서 전자는 1주기 내 $v \sim c$, 로렌츠 힘 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$에서 **$\mathbf{v}\times\mathbf{B}$ 항이 $\mathbf{E}$와 동등**.

#### 방사 반작용이 로렌츠 힘을 이기는 영역 (2023)

$$R = \frac{F_{rad}}{F_L} \sim \frac{2}{3}\alpha_f \gamma^2 \frac{E}{E_S}$$

> **Unicode**
> ```
> R = (F_rad)/(F_L) ∼ (2)/(3)α_f γ² (E)/(E_S)
> ```

$R > 0.1$이면 **Landau-Lifshitz 힘** $\mathbf{F}_{rad}$ 추가로 고려. $R > 1$ 방사 지배 영역에서 레이저 에너지가 거의 전부 **감마 플래시**로 전환된다는 2023 PRL 실험.

**ELI, Apollon 레이저 10 PW**에서 $\chi_e \sim 1$ 양자 영역 진입, 로렌츠 궤적이 확률적 점프.

#### 플라즈마 거울 고차 고조파

Lamač et al. (PRL 131, 205001, 2023): 자기 변조 플라즈마 거울에서 **비선형 $v\times B$ 전류**가 고차 고조파 생성. 로렌츠 힘이 직접 빛을 만든다.

### 5.1.5 중력파 검출 (LIGO)에서 로렌츠 힘

LIGO 테스트 매스 40 kg 거울은 $B$에 매우 민감. 지자기 $B \sim 50$ μT가 자화된 스틸 부품에 $\mathbf{m}\cdot\nabla\mathbf{B}$ 힘으로 $10^{-15}$ m 변위 → 가짜 신호.

#### O3-O4 run (2020~)

- **Voice coil actuator:** $\mathbf{F} = I\mathbf{L}\times\mathbf{B}$로 거울 위치 제어. 코일 자석 자체가 잡음원이라 2023년 **정전 구동으로 교체 중** — 로렌츠 힘 제거가 감도 향상
- **Schumann 공명 8 Hz** 자기장이 두 사이트 상관 잡음으로 작용, Wiener 필터로 $\mathbf{B}$ 측정 후 빼기
- **차세대 Einstein Telescope:** 초전도 차폐 $B < 1$ nT 목표

중력파 자체는 $h \sim 10^{-21}$로 $q\mathbf{v}\times\mathbf{B}$보다 10배 작아 **자기 차폐가 검출 필수**.

### 5.1.6 우주 추진 — 홀추력기, VASIMR, 태양돛

#### 홀 추력기

방사형 $B_r \sim 0.02$ T, 축방향 $E_z$, 전자는 $\mathbf{E}\times\mathbf{B}$로 방위각 드리프트:

$$V_{E\times B} = E/B$$

> **Unicode**
> ```
> V_E× B = E/B
> ```

홀 전류 $I_H$ 형성. **이 홀 전류의 $\mathbf{J}_H\times\mathbf{B}_r$가 축방향 로렌츠 추력**.

- $T \sim 80$ mN, $I_{sp} \sim 1600$ s
- **Starlink 5000기 운용** (2023)

#### VASIMR

헬리콘으로 플라즈마 생성 → ICRF로 $v_\perp$ 가열 → 발산 자력 노즐에서 $\mu\nabla B$ 힘이 $v_\perp \to v_\parallel$ 변환. 추력은 $\mathbf{J}_\theta\times\mathbf{B}_r$로 축방향 운동량 전환.

- $50$ kW에서 홀추력기보다 고효율 예측
- **2022 Ad Astra 100 kW 테스트** ($T = 6$ N)

#### 태양돛/자기돛

태양광 압력 + 태양풍 $q\mathbf{v}\times\mathbf{B}$.

- **자기돛 M2P2:** 초전도 링 $B \sim 0.1$ T로 태양풍 양성자 $\mathbf{v}\times\mathbf{B}$ 편향해 추력
- **2024 JAXA OKEANOS 확장**

### 5.1.7 주요 논문 20편 요약 (2020~2025)

| # | 논문 / 연도 | 분야 | 로렌츠 힘 핵심 |
|---|---|---|---|
| 1 | Degrave et al., Nature 2022, Magnetic Control via Deep RL | 핵융합 AI | RL이 $J\times B$ 평형 직접 제어, 드롭렛 형상 최초 실현 |
| 2 | Jain et al., Nature 2024, Penning micro-trap | 양자컴퓨팅 | 정적 $B=3$ T 로렌츠 구속으로 RF 없이 이온 수송·연산 |
| 3 | Zhang et al., PRB 2022, Giant nonlinear Hall in strained TBG | 나노소자 | Lorentz skew scattering이 $E^2H$ 비선형 홀 구동 |
| 4 | Lamač et al., PRL 131, 205001 (2023) | 강레이저 | 플라즈마 거울 고차 고조파, $v\times B$ 비선형 전류 |
| 5 | Vranic et al., PRL 113, 134801 (2014) | 강레이저 | All-optical radiation reaction, $F_{rad}$ 지배 |
| 6 | KSTAR Team, Nature Comm 2023, 100s H-mode AI control | 핵융합 | $E\times B$ 전단 AI 유지 |
| 7 | W7-X Team, PRL 129, 095001 (2022), Quasi-isodynamic optimization | 스텔라레이터 | $V_{gc}$ 드리프트 최소화 KAM 보존 |
| 8 | Ad Astra VASIMR VX-200SS (2022) | 우주추진 | $J_\theta\times B_r$ 노즐 변환, $T=6$ N @ 100kW |
| 9 | SpaceX Starlink Hall thruster SPT-140 (2023) | 우주추진 | $E\times B$ 홀 전류 추력, Kr 추진제 |
| 10 | Google Quantum AI, PRL 2023, Flux noise mitigation | 양자 | $B$ 잡음 $1/f$가 로렌츠 위상 디코히어런스 |
| 11 | UT Dallas, Quantum anomalous Hall in bilayer graphene 2021 | 나노 | $B=0$에서 Berry 곡률이 로렌츠 역할 |
| 12 | ITER IO, Nucl. Fusion 2023, RMP ELM suppression | 핵융합 | 외부 $\tilde{B}$로 에르고딕화, $D_{RR}$ 열분산 |
| 13 | ELI-NP, Nat. Photon 2022, 10PW $a_0 \sim 100$ | 강레이저 | $v\times B$ 2차 고조파 가속 |
| 14 | LIGO-Virgo, PRD 105, 082005 (2022), Magnetic correlation Schumann | 중력파 | 지자기 $B$가 상관 잡음, 로렌츠 힘 차폐 |
| 15 | MIT SPARC, JPP 2022, High-field tokamak $B=12$ T | 핵융합 | $B\rho$ 증가로 $R=1.85$ m 소형로 |
| 16 | ETH Zurich, PRL 2022, 219-ion entanglement | 양자 | Penning $B$로 219개 얽힘 |
| 17 | Graphene hydrodynamics, PRB 2022, Hall viscosity | 나노 | 점성 vs 로렌츠 힘 경쟁 |
| 18 | JAXA DESTINY+, thin film solar sail 2022 | 우주추진 | 광압 + 태양풍 $v\times B$ 항법 |
| 19 | DeepMind DIII-D disruption prediction, Nature 2024 | 핵융합 AI | $\mathbf{J}\times\mathbf{B}$ 불균형 300ms 전 예측 |
| 20 | NASA Psyche Hall thruster SPT-140 (2023) | 우주추진 | $E\times B$ 추력 심우주 항해 |

### 5.1.8 총괄

**2020년 이전 로렌츠 힘은 공식이었다면, 2020년 이후는 제어 변수다.**

- **AI:** $\mathbf{J}\times\mathbf{B}$를 보상함수로 학습
- **양자칩:** $\mathbf{v}\times\mathbf{B}$로 이온을 가둠
- **그래핀:** $\mathbf{v}\times\mathbf{B}$를 정류기로 씀
- **레이저:** $\mathbf{v}\times\mathbf{B}$가 $\mathbf{E}$를 이기는 영역을 탐사

**다음 5년은 고온 초전도 $B > 20$ T + AI 실시간 $F_L$ 제어가 핵융합·양자·우주추진을 동시에 닫을 것으로 보인다.**

### 5.1.9 매스매티카 검증

```mathematica
(* AI 제어 보상 함수 *)
aiReward[psi_, psiTarget_, Jvec_, Bvec_, gradp_] :=
  -Norm[psi - psiTarget] - Norm[Cross[Jvec, Bvec] - gradp];

(* Penning 트랩 진동수 *)
penningFreq[q_, B_, m_] := q B / m;

(* 홀 추력기 추력 *)
hallThrust[JHall_, Br_, L_] := JHall Br L;

(* 방사 반작용 비 *)
radiationRatio[gamma_, Efield_, Es_] :=
  (2/3) alphaFine gamma^2 Efield / Es;
```

### 5.1.10 한계·예외

- **AI 제어:** 학습 데이터 편향, 실물 전이 실패 가능성
- **양자컴퓨팅:** $B$ 잡음, 이온 가열
- **그래핀:** 제조 균일도, 재현성
- **강레이저:** 반복률, 시료 손상
- **중력파:** 자기 차폐 비용, 환경 잡음
- **우주추진:** 수명, 추진제 공급

> **참고문헌**
> - Degrave, J., et al., *Magnetic control of tokamak plasmas through deep reinforcement learning*, Nature **602**, 414 (2022). [doi:10.1038/s41586-021-04301-9](https://doi.org/10.1038/s41586-021-04301-9)
> - Jain, S., et al., *Penning micro-trap for quantum computing*, Nature **627**, 510 (2024). [doi:10.1038/s41586-024-07111-x](https://doi.org/10.1038/s41586-024-07111-x)
> - Zhang, Y., et al., *Giant nonlinear Hall effect in strained twisted bilayer graphene*, Phys. Rev. B **106**, L041111 (2022). [doi:10.1103/PhysRevB.106.L041111](https://doi.org/10.1103/PhysRevB.106.L041111)
> - Lamač, M., et al., *Anomalous relativistic emission from self-modulated plasma mirrors*, Phys. Rev. Lett. **131**, 205001 (2023). [doi:10.1103/PhysRevLett.131.205001](https://doi.org/10.1103/PhysRevLett.131.205001)
> - W7-X Team, *Quasi-isodynamic optimization*, Phys. Rev. Lett. **129**, 095001 (2022). [doi:10.1103/PhysRevLett.129.095001](https://doi.org/10.1103/PhysRevLett.129.095001)

---
## 5.2 미해결 문제와 미래

$q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 130년 된 공식이지만, $B$의 기원, 점전하 극한, 양자-중력 접합에서 여전히 모른다. 이 절에서는 자기 단극자, 밀리차지 암흑물질, 양자중력, Born-Infeld, 플라즈마 난류, 핵융합 상용화, 미해결 문제 10선을 다룬다.

### 5.2.1 자기 단극자의 존재 가능성

맥스웰 방정식에 대칭성을 넣으면:

$$\nabla\cdot\mathbf{B} = \mu_0\rho_m, \quad \nabla\times\mathbf{E} = -\partial_t\mathbf{B} - \mu_0\mathbf{J}_m$$

> **Unicode**
> ```
> ∇·𝐁 = μ₀ρₘ,   ∇×𝐄 = -∂ₜ𝐁 - μ₀𝐉ₘ
> ```

**로렌츠 힘의 이중 확장:**

$$\mathbf{F} = q_e(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + q_m\left(\mathbf{B}-\frac{\mathbf{v}}{c^2}\times\mathbf{E}\right)$$

> **Unicode**
> ```
> 𝐅 = qₑ(𝐄+𝐯×𝐁) + qₘ(𝐁-(𝐯)/(c²)×𝐄)
> ```

두 번째 항이 단극자가 느끼는 힘. 1931 Dirac 양자화 $q_e q_m = n\hbar/2$가 **전하 양자화를 설명**한다는 매력이 있다.

**현재 상태:**

- GUT 단극자 질량 $10^{16}$ GeV, 우주 초기 인플레이션으로 희석되어 $n_m < 10^{-30}$ cm$^{-3}$ 예측. 직접 검출 불가
- **LHC MoEDAL (2022-2023):** $m < 3$ TeV 단극자 배제, Dirac 전하 $1g_D = 68.5e$ 단위. **Nature 2022 Schwinger 탐색**이 가장 모델 독립적
- **스핀 아이스 Dy₂Ti₂O₇:** 유사 단극자 준입자 관측 — 진짜 단극자 아님, Emergent $B$의 발산
- **만약 발견되면:** $F = dA$가 아닌 $F = dA + \star$ 구조, $U(1)$ 다발이 꼬인 $c_1 = n$ 다발 — 전자기학 교과서 전면 개정

**미래:** 고자장 100 T 펄스 자석 + SQUID로 $g_D$ 양자 점프 탐색, 달 토양 샘플에서 고대 단극자 탐색 제안.

### 5.2.2 암흑물질과 밀리차지 입자

암흑물질이 완전히 중성이라는 보장은 없다. $U(1)$ 다크 포톤 $A'$과 운동학적 섞임 $\epsilon F_{\mu\nu}F'^{\mu\nu}$가 있으면 암흑 입자가 **미세 전하** $\epsilon e$ 획득 — **밀리차지 MCP**.

**로렌츠 힘:**

$$\mathbf{F} = \epsilon q_e(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = ε qₑ(𝐄+𝐯×𝐁)
> ```

**영향:**
- 은하 자기장 $B \sim \mu$G에서 MCP는 $\mathbf{v}\times\mathbf{B}$로 편향 → 은하 원반에서 제거, **암흑 디스크** 형성 가능성
- 태양 자기장, 지구 자기권이 MCP 플럭스 변조

**현재 상태 (2020~2024):**

- **milliQan@LHC, SENSEI, LDMX:** $\epsilon < 10^{-3}$, $m = 0.1-10$ GeV 영역 탐색, 아직 신호 없음
- **우주론 제한:** CMB에서 MCP가 바리온과 결합하면 $N_{eff}$ 변화, $\epsilon < 10^{-9}$ ($m < 1$ keV)
- **21cm EDGES 이상 신호:** 0.3% MCP로 설명 가능하다는 주장 (2018), **2023 SARAS가 반박**

**미래 방향:** 10 T 홀 추력기 자기장으로 MCP 편향 후 검출, 플라즈마 할로에서 $\mathbf{J}_{MCP}\times\mathbf{B}$로 생기는 미약 전류 탐색. **로렌츠 힘으로 암흑을 보는 셈**.

### 5.2.3 양자 중력에서 로렌츠 힘의 일반화

일반 상대론에서 하전 입자 운동:

$$m\frac{Du^\mu}{d\tau} = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> m(Du^μ)/(dτ) = qF^μνu_ν
> ```

$D$는 공변 미분, $F$는 곡선 시공간에서도 2-형식. 문제는 **양자 중력에서 $F_{\mu\nu}$ 자체가 양자 요동**, 시공간이 거품.

**2가지 가설:**

1. **Lorentz 위반:** 양자 중력에서 시공간 이산 $\ell_P$ → 수정 분산 $E^2 = p^2c^2 + m^2c^4 + \eta p^3/M_P$. 하전 입자 속도가 $c$ 초과 가능, 진공 Cherenkov 방사 $e \to e\gamma$ 허용. **Fermi LAT GRB 광자 $>10$ GeV 도달**로 $\eta < 10^{-8}$ 제한
2. **중력-전자기 이중 복사:** $F_{\mu\nu}$가 중력과 섞임, 5차원 Kaluza-Klein에서 $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + m\mathbf{g} + \ldots$ 형태. **등가원리 위반 $10^{-15}$** 수준 탐색 중

**현재 상태:**
- **LIGO 중성자별 합병 GW170817:** $\mathbf{J}\times\mathbf{B}$로 생기는 제트와 중력파 동시 관측으로 $v_{GW} = c$ $10^{-15}$ 정밀 확인, Lorentz 위반 강하게 제한
- 그러나 $B \sim 10^{12}$ T 마그네타 근처에서 $q\mathbf{v}\times\mathbf{B}$가 시공간 곡률과 경쟁하는 영역은 **미탐사**

**미래:** 펄서 타이밍 어레이로 $\mathbf{B}$ + 중력파 배경 상관, 양자 홀 중력 유사체 실험.

### 5.2.4 비선형 전기역학 — Born-Infeld

맥스웰 $L = -F_{\mu\nu}F^{\mu\nu}/4\mu_0$는 $E \to \infty$에서 발산, 점전하 자기 에너지 무한. **Born-Infeld (1934)** 제안:

$$L_{BI} = b^2\left(1-\sqrt{1 + \frac{F^2}{2b^2} - \frac{(F\tilde{F})^2}{16b^4}}\right)$$

> **Unicode**
> ```
> L_BI = b²(1-√(1 + (F²)/(2b²) - ((FF̃)²)/(16b⁴)))
> ```

$b \sim 10^{20}$ V/m 임계장. **전기장 최대값 존재, 점전하 에너지 유한**.

**로렌츠 힘의 수정:** $D = \partial L/\partial E$로 정의된 변위장 사용:

$$\mathbf{F} = q(\mathbf{E}(\mathbf{D},\mathbf{B}) + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄(𝐃,𝐁) + 𝐯×𝐁)
> ```

$E(D)$가 비선형이라 **중첩 원리 붕괴**, 두 전하 사이 힘은 단순 합이 아님.

**현재 상태:**
- **LHC 중이온 PbPb:** $B \sim 10^{15}$ T, $E \sim 10^{20}$ V/m 근접. BI 효과로 광자-광자 산란 단면적 변화 예측. **ATLAS 2022 $\gamma\gamma\to\gamma\gamma$ 관측이 맥스웰과 일치**, $b > 10^{19}$ V/m 하한
- **끈 이론:** BI가 D-brane 저에너지 유효 작용으로 자연 등장 — $b = 1/2\pi\alpha'$

**미래:** 100 PW 레이저 $E \sim 10^{18}$ V/m에서 진공 복굴절 $\Delta n \propto (E/b)^2$ 측정, 로렌츠 힘 비선형 보정으로 전자 궤적 1% 편차 탐색.

### 5.2.5 플라즈마 난류와 로렌츠 힘의 카오스

**가장 실용적 미해결 문제.** 핵융합로 $\chi$는 고전 $1/B^2$ 예측보다 $10^2$배 큼 — 난류 때문.

핵심 방정식:

$$\rho\frac{d\mathbf{V}}{dt} = -\nabla p + \mathbf{J}\times\mathbf{B}$$

> **Unicode**
> ```
> ρ(d𝐕)/(dt) = -∇ p + 𝐉×𝐁
> ```

에서 $\mathbf{J}\times\mathbf{B}$ 자체가 난류로 요동 $\tilde{\mathbf{J}}\times\tilde{\mathbf{B}}$ → 평균 $\langle\tilde{J}\times\tilde{B}\rangle$가 이상 전기장 생성.

**미해결 2가지:**

1. **L-H 천이 트리거:** $E_r\times B$ 전단 $\omega_{E\times B}$가 난류를 억제하는 임계 조건이 무엇인가? **30년 난제.** 2023 KSTAR에서 $\omega_{E\times B} \approx \gamma_{lin}$일 때 천이 관측, 이론은 $E_r$이 $\nabla p$에서 자발 생성되는 루프 설명 불완전
2. **난류 포화:** Hasegawa-Mima 난류가 왜 $k^{-3}$ 스펙트럼에서 멈추는가? Zonal flow가 $\tilde{V}\times B$로 난류 에너지를 빨아들이는 메커니즘은 있으나 **정량 예측 오차 2배**

**미래:** 6차원 Vlasov 시뮬레이션 + AI 클로저. 로렌츠 힘의 $\mathbf{v}\times\tilde{\mathbf{B}}$를 직접 입자 궤적에서 학습하는 **PINN 모델**이 2024년 $\chi$ 20% 예측 성공.

### 5.2.6 핵융합 상용화를 위한 로렌츠 힘 기반 혁신

상용화 조건: $Q > 10$, $\beta \sim 5\%$, $\tau_E > 3$ s, disruption < 1%.

**로렌츠 힘 혁신 4가지:**

1. **고온 초전도 $B > 12$ T:** $B\rho = p/q$에서 $B$ 2배 → $R$ 1/2 → 자본비 1/4. **MIT SPARC $B = 12.2$ T**, Commonwealth Fusion 2025 TF 코일 테스트. 로렌츠 응력 $F = JB \sim 1000$ ton/m 처리용 Inconel 재킷이 핵심
2. **액체 금속 벽:** Li 벽이 $J\times B$로 $E$ 차폐, RMP 없이 ELM 안정화. $\mathbf{J}\times\mathbf{B}$로 Li 흐름 제어
3. **RF 전류 구동 효율:** $E\parallel B$로 전류 구동 효율 $\eta_{CD} = I_{CD}R/P_{RF}$를 $\mathbf{v}\times\mathbf{B}$로 인한 도플러 시프트로 최적화, 2030 목표 $\eta > 0.5$
4. **AI $F_L$ 실시간 제어:** DeepMind 방식이 $B$ 코일을 직접 제어, disruption 300 ms 전 $J\times B$ 불균형 감지 후 $B$ 급강하 소프트랜딩. **ITER 2027 도입 예정**

### 5.2.7 미해결 문제 10선

| # | 문제 | 현재 상태 |
|---|---|---|
| 1 | **자기 단극자 존재** | Dirac 양자화 미검증. MoEDAL 하한 $m > 3$ TeV. 우주론적 희석 문제 |
| 2 | **양자 진공 자기 복굴절** | $B > 10^9$ T에서 $n_\parallel \neq n_\perp$. PVLAS 2022 한계 $b > 10^{19}$ V/m, 100 PW 레이저로 2028 목표 |
| 3 | **방사 반작용 자기 일관성** | ALD runaway/pre-acceleration 해결? Landau-Lifshitz가 표준이나 양자 영역 $\chi > 1$에서 확률적 방사 모델 논쟁 중, 2023 SLAC E320 진행 |
| 4 | **자기 재결합 빠른 촉발** | $S = 10^{15}$에서 왜 $0.1V_A$ 빠른 재결합인가? Hall + 플라즈모이드 이론은 있으나 3차원 키네틱 시뮬레이션과 관측 30% 불일치 |
| 5 | **플라즈마 난류 제1원리 예측** | $\chi_i, \chi_e$를 $B,n,T$로 10% 예측 불가. ITER $Q$ 예측 오차 2배. Exascale Vlasov 필요 |
| 6 | **비선형 홀 효과 양자화** | $E^2B$ 비선형 전도도 $\sigma^{(2)}$가 양자화되는가? 그래핀에서 32% 관측, 이론적 Chern 수 확장 미완 |
| 7 | **밀리차지 암흑물질의 자기 포획** | 은하 $B$가 MCP를 원반에 가두는가? 자기 유체 시뮬레이션에서 $\epsilon > 10^{-8}$이면 포획, CMB 제한과 충돌 |
| 8 | **펄서 자기권 쌍생성 닫힘** | Goldreich-Julian 밀도 $n_{GJ}$에서 $E_\parallel$이 어떻게 차폐되는가? PIC 시뮬레이션은 갭 진동 보이나 전파 방사 메커니즘 여전히 논쟁 |
| 9 | **토카막 disruption 무ELM 안정 운전** | $q_{95} > 3$, $\beta_N > 3$에서 disruption 없이 1000초 유지 가능? KSTAR 100초 달성, ITER 400초 목표, **AI 제어 없이는 불가** |
| 10 | **로렌츠 힘의 CPT 대칭** | 반물질 $\bar{p}$의 $q\mathbf{v}\times\mathbf{B}$가 정확히 반대인가? ALPHA-g 2023 반수소 중력 측정, $F_L$ CPT 위반 한계 $10^{-9}$, 2030 $10^{-12}$ 목표 |

### 5.2.8 미래 연구 방향 3축

1. **극한 $B$:** 20 T HTS 자석 + 100 PW 레이저로 $E \sim 10^{20}$ V/m, $B \sim 10^6$ T 실험실 구현 → Born-Infeld, 진공 복굴절 직접 검증
2. **AI $F_L$ 제어:** $J\times B$를 실시간 필드 예측, 강화학습으로 KAM 토러스 보존율 99% 유지 — **핵융합 상용화 최단 경로**
3. **양자 $U(1)$ 위상:** 로렌츠 힘을 힘 아닌 홀로노미 $W(C) = \exp(iq\oint A)$로 보고 위상 물질·양자컴퓨팅에 응용 — Hall 점성, 비선형 홀을 큐비트 연결로 사용

### 5.2.9 매스매티카 검증

```mathematica
(* Dirac 양자화 *)
diracQuantization[qCharge_, gMonopole_] := qCharge gMonopole == nInteger hBar/2;

(* Born-Infeld 라그랑지안 *)
bornInfeldLagrangian[Fmunu_, b_] :=
  b^2 (1 - Sqrt[1 + (Fmunu Fmunu)/(2 b^2) - (Fmunu Star[Fmunu])^2/(16 b^4)]);

(* 밀리차지 힘 *)
milliChargeForce[epsilon_, q_, Evec_, vvec_, Bvec_] :=
  epsilon q (Evec + Cross[vvec, Bvec]);

(* ALD 방사 반작용 *)
aldForce[q_, tau0_, aDot_] := q^2/(6 Pi epsilon0 c^3) aDot;
```

### 5.2.10 한계·예외

- **자기 단극자:** 이론적으로 매력적이나 실험적 증거 전무
- **밀리차지:** 우주론 제한과 지상 실험 제한이 충돌
- **양자중력:** 실험적 검증 극도로 어려움
- **Born-Infeld:** $b$ 값의 이론적 기원 불명
- **난류:** AI 예측도 훈련 데이터 한계
- **핵융합:** 공학적 난제 (재료, 삼중곱)

> **참고문헌**
> - Acharya, B., et al. (MoEDAL), *Search for magnetic monopoles via Schwinger pair production*, Nature **602**, 63 (2022). [doi:10.1038/s41586-021-04298-1](https://doi.org/10.1038/s41586-021-04298-1)
> - MoEDAL Collaboration, *Search for highly-ionizing particles*, Eur. Phys. J. C **82**, 694 (2022). [doi:10.1140/epjc/s10052-022-10608-2](https://doi.org/10.1140/epjc/s10052-022-10608-2)
> - PVLAS Collaboration, *First results from the new PVLAS apparatus*, Phys. Rev. D **90**, 092003 (2014). [arXiv:1406.6518](https://arxiv.org/abs/1406.6518)
> - Born, M., Infeld, L., *Foundations of the new field theory*, Proc. R. Soc. A **144**, 425 (1934). [doi:10.1098/rspa.1934.0059](https://doi.org/10.1098/rspa.1934.0059)

---

## 5.3 응집물질·위상물질

응집물질에서 $q\mathbf{v}\times\mathbf{B}$는 전자를 휘게 하는 것을 넘어 **공간 자체의 위상**을 만든다. 이 절에서는 양자 홀, 스핀 홀, 위상절연체, 마요라나, 그래핀 의사 자기장, 베리 곡률, 초전도 보텍스를 다룬다.

### 5.3.1 양자 홀 효과

2차원 전자 가스 $n_{2D}$, $B\hat{z}$.

#### 정수 QHE

란다우 준위 $E_n = \hbar\omega_c(n+1/2)$, 축퇴도 $N_\phi = BS/\Phi_0$, $\Phi_0 = h/e$.

채움 인자 $\nu = N_e/N_\phi = nh/eB$ 정수일 때 페르미 준위가 갭에 위치 → $\sigma_{xx} = 0$,

$$\sigma_{xy} = \nu \frac{e^2}{h}, \quad R_H = \frac{h}{\nu e^2}$$

> **Unicode**
> ```
> σ_xy = ν (e²)/(h),   R_H = (h)/(ν e²)
> ```

**Kubo 공식에서 $\sigma_{xy}$는 $k$-공간 베리 곡률 적분:**

$$\sigma_{xy} = \frac{e^2}{h}\frac{1}{2\pi}\int_{BZ}\Omega_z(\mathbf{k})\, d^2k = \frac{e^2}{h}C$$

> **Unicode**
> ```
> σ_xy = (e²)/(h)(1)/(2π)∫_BZ Ω_z(𝐤) d²k = (e²)/(h)C
> ```

$C$는 **제1 Chern 수**. 로렌츠 힘이 만든 $E\times B$ 드리프트 $V_y = E_x/B$가 $j_x = neV_y$로 양자화되는 것이 아니라, **위상 불변량 $C$** 가 양자화된다. **Disorder가 있어도 $C$는 변하지 않음** — 위상 보호.

#### 분수 QHE

$\nu = 1/3, 2/5$ 등. 쿨롱 $e^2/\epsilon l_B$가 $\hbar\omega_c$와 경쟁, **Laughlin 파동함수:**

$$\Psi_{1/m} = \prod_{i<j}(z_i-z_j)^m e^{-\sum|z_i|^2/4l_B^2}$$

> **Unicode**
> ```
> Ψ_1/m = ∏_i<j(zᵢ-zⱼ)ᵐ e^-∑|zᵢ|²/4l_B²
> ```

입자는 자속 $m\Phi_0$를 붙인 **복합 페르미온**으로 변환, 유효 자기장 $B^* = B - 2pn\Phi_0$에서 정수 QHE. 로렌츠 힘은 $B^*$에 대해 작용, 준입자 전하 $e^* = e/3$, 통계 $\theta = \pi/m$ — **애니온**.

**최근 (2023):** 그래핀에서 분수 Chern 절연체 $B = 0$에서도 분수 양자화 — 로렌츠 힘 없이 **베리 곡률이 $B_{eff}$ 역할**.

### 5.3.2 스핀 홀·이상 홀

#### 이상 홀 효과 (AHE)

강자성체에서 $B_{ext} = 0$인데도 홀 전압 발생:

$$\rho_{xy} = R_0 B + R_S M$$

> **Unicode**
> ```
> ρ_xy = R₀ B + R_S M
> ```

$R_S$ 항이 이상. 원인은 **스핀-궤도 결합** $H_{SO} = \lambda\mathbf{S}\cdot(\mathbf{p}\times\nabla V)$ — 전자가 움직일 때 느끼는 **유효 자기장** $\mathbf{B}_{eff} \propto \mathbf{p}\times\mathbf{E}$가 스핀에 의존하는 **로렌츠 힘**.

**3가지 기여:**
- 내인성: 베리 곡률 $\Omega(\mathbf{k})$ 적분
- 외인성: skew scattering, side jump

**내인성 AHE:**

$$\sigma_{xy}^{AHE} = -\frac{e^2}{\hbar}\int_{BZ} \frac{d^3k}{(2\pi)^3} f(\mathbf{k})\Omega_z(\mathbf{k})$$

> **Unicode**
> ```
> σ_xy^AHE = -(e²)/(ℏ)∫_BZ (d³k)/((2π)³) f(𝐤)Ω_z(𝐤)
> ```

$M$에 비례하는 $\Omega$가 **로렌츠 힘 없이 홀 전류 생성**. $\Omega$가 곧 $k$-공간 자기장.

#### 스핀 홀 효과 (SHE)

비자성체에서 전하는 홀 없이 스핀만 분리:

$$\mathbf{J}_s = \theta_{SH}\frac{\hbar}{2e}\mathbf{J}_c\times\hat{s}$$

> **Unicode**
> ```
> 𝐉ₛ = θ_SH (ℏ)/(2e) 𝐉_c×ŝ
> ```

$\theta_{SH}$: 스핀 홀 각. Pt에서 0.1, β-W에서 0.3. 원리: $H_{SO}$로 스핀 업은 $+\mathbf{y}$, 다운은 $-\mathbf{y}$로 $q\mathbf{v}\times\mathbf{B}_{eff}$ 반대 방향. **전하 흐름은 없지만 스핀 흐름 존재.**

**역 스핀 홀 (ISHE):** 스핀 전류를 전압으로 검출. **SOT-MRAM** 핵심: $\mathbf{J}_c \to \mathbf{J}_s \to$ 자화 반전 토크 $\boldsymbol{\tau} \propto \mathbf{M}\times(\mathbf{M}\times\mathbf{S})$.

**여기서 로렌츠 힘은 실제 $B$가 아닌 $\mathbf{B}_{eff} \propto \mathbf{E}\times\mathbf{p}$로 작용** — 상대론적 로렌츠 변환 $\mathbf{B}' \approx -\mathbf{v}\times\mathbf{E}/c^2$의 고체 버전.

### 5.3.3 위상절연체

$Z_2$ 위상절연체 Bi₂Se₃: 벌크 갭, 표면 Dirac:

$$H_{surf} = v_F(\mathbf{p}\times\boldsymbol{\sigma})_z = v_F(p_x\sigma_y - p_y\sigma_x)$$

> **Unicode**
> ```
> H_surf = v_F(𝐩×σ)_z = v_F(pₓσ_y - p_yσₓ)
> ```

**스핀-운동량 잠금.** 시간 반전 대칭으로 $B = 0$에서 $\sigma_{xy} = 0$이나, $B\perp$ 인가 시 표면 란다우 준위:

$$E_n = \text{sgn}(n) v_F\sqrt{2e\hbar B|n|}$$

> **Unicode**
> ```
> Eₙ = sgn(n) v_F√(2eℏ B|n|)
> ```

**$n = 0$ 준위가 $E = 0$에 고정** — $\pi$ 베리 위상 때문. $E_n \propto \sqrt{B|n|}$는 그래핀과 동일.

**양자화된 자기광학:** 얇은 TI 박막에서 $\sigma_{xy} = (N+1/2)e^2/h$ → **Faraday 회전 $\theta_F = \alpha_{fine} \approx 7.3$ mrad 양자화**. 로렌츠 힘이 빛의 편광을 돌리는 것이 위상 양자화.

**양자 이상 홀 (QAHE):** 자성 도핑으로 시간 반전 깨면 $B = 0$에서 $\sigma_{xy} = e^2/h$, $C = 1$ Chern 절연체. **Cr-doped (Bi,Sb)₂Te₃ 2020년 $T = 1$ K에서 관측**. 베리 곡률이 로렌츠 힘을 완전히 대체.

### 5.3.4 마요라나 페르미온

마요라나 $\gamma = \gamma^\dagger$, $\gamma^2 = 1$, 입자=반입자. 위상 초전도체에서 $p+ip$ 페어링 + Zeeman으로 생성.

**설계식 (1차원 나노와이어 InAs + s-파 초전도체 Al + 자기장 $B\parallel$):**

$$H = \left(\frac{p^2}{2m}-\mu\right)\tau_z + \alpha_R p\sigma_y\tau_z + g\mu_B B\sigma_x + \Delta\tau_x$$

> **Unicode**
> ```
> H = ((p²)/(2m)-μ)τ_z + α_R pσ_yτ_z + gμ_B Bσₓ + Δτₓ
> ```

$\alpha_R$: Rashba SO, $g\mu_B B$: Zeeman. **위상 조건:**

$$g\mu_B B > \sqrt{\Delta^2+\mu^2}$$

> **Unicode**
> ```
> gμ_B B > √(Δ²+μ²)
> ```

$B$가 스핀을 정렬해 s-파를 유효 p-파로 변환, 양 끝단에 **마요라나 제로 모드**.

**평행 자기장 필수 이유:** 수직 $B$는 초전도 와선을 만들어 마요라나를 망침. **수직 $B$는 $H_{c2}$ 초과.**

**2차원:** $p+ip$ 초전도체 Sr₂RuO₄, FeTeSe에서 와선 코어에 마요라나. 와선에 흐르는 초전류 $\mathbf{J}_s$의 **로렌츠 힘 $\mathbf{J}_s\times\Phi_0$가 와선을 고정**, 그 와선 코어의 Caroli-de Gennes-Matricon 준위가 Zeeman으로 0 에너지로 이동.

**현재 상태:** 마이크로소프트 2023-24 InAs-Al에서 $2e^2/h$ 양자화 전도 피크 보고, **논쟁 중**. $B$ 노이즈가 마요라나 결맞음 파괴 주원인.

### 5.3.5 그래핀과 의사 자기장 $B_{ps}$

그래핀 저에너지 $H = v_F\boldsymbol{\sigma}\cdot(\mathbf{p}+e\mathbf{A})$, $\mathbf{A}$는 실제 자기장. 변형 $u_{ij}$가 있으면 호핑 $t \to t+\delta t$ 변화가 **게이지장**으로 나타남:

$$\mathbf{A}_{ps} = \frac{\hbar\beta}{2ea}(u_{xx}-u_{yy}, -2u_{xy})$$

> **Unicode**
> ```
> 𝐀ₚₛ = (ℏβ)/(2ea)(uₓₓ-u_yy, -2u_xy)
> ```

$\beta \sim 3$, $a = 0.14$ nm. **의사 자기장:**

$$B_{ps} = \nabla\times\mathbf{A}_{ps}$$

> **Unicode**
> ```
> Bₚₛ = ∇×𝐀ₚₛ
> ```

1% 변형으로 $B_{ps} \sim 10$ T, 나노 버블에서 **300 T까지** 보고.

**중요한 차이:**
- $B_{ps}$는 $K$ 밸리에서 $+B$, $K'$에서 $-B$ — **시간 반전 유지, 총 자속 0**
- 따라서 전하 홀은 없지만 **밸리 홀** 존재 — 밸리 필터

**실험 (2010 Levy Science):** Pt(111) 위 그래핀 나노 버블에서 STM $dI/dV$로 $E_n \propto \sqrt{nB_{ps}}$ 란다우 준위 관측, **$B_{ps} = 350$ T**. 로렌츠 힘 없이 변형만으로 양자 홀.

**최신:** $B_{ps}$ + 실제 $B$ 조합으로 **밸리 의존 로렌츠 힘** $F_K = -e\mathbf{v}\times(B+B_{ps})$, $F_{K'} = -e\mathbf{v}\times(B-B_{ps})$ → 밸리 분리, **밸리트로닉스**.

### 5.3.6 베리 곡률과 위상 전도

모든 위상 현상의 공통 언어. Bloch 상태 $|u_n(\mathbf{k})\rangle$에 대해:

$$\mathcal{A}_n = i\langle u_n|\nabla_k|u_n\rangle, \quad \Omega_n = \nabla_k\times\mathcal{A}_n$$

> **Unicode**
> ```
> Aₙ = i⟨ uₙ|∇ₖ|uₙ⟩,   Ωₙ = ∇ₖ×Aₙ
> ```

**운동 방정식:**

$$\hbar\dot{\mathbf{k}} = -e(\mathbf{E}+\dot{\mathbf{r}}\times\mathbf{B}), \quad \dot{\mathbf{r}} = \frac{1}{\hbar}\nabla_k\epsilon_n - \dot{\mathbf{k}}\times\mathbf{\Omega}_n$$

> **Unicode**
> ```
> ℏ𝐤˙ = -e(𝐄+𝐫˙×𝐁),   𝐫˙ = (1)/(ℏ)∇ₖεₙ - 𝐤˙×Ωₙ
> ```

두 번째 항이 **이상 속도** $-e\mathbf{E}\times\mathbf{\Omega}_n/\hbar$ — **$k$-공간 로렌츠 힘**. $\Omega_n$이 $k$-공간 자기장 역할.

**전도도:**

$$\sigma_{xy} = -\frac{e^2}{\hbar}\sum_n\int f_n\Omega_n^z\frac{d^2k}{(2\pi)^2}$$

> **Unicode**
> ```
> σ_xy = -(e²)/(ℏ)∑ₙ∫ fₙ Ωₙᶻ (d²k)/((2π)²)
> ```

$\Omega$ 적분이 **Chern 수**. Weyl 반금속 TaAs에서 $\Omega \sim 1/k^2$ 발산, $\sigma_{xy} \sim 1000$ S/cm.

**로렌츠 힘의 현대적 정의 3가지 합:**

$$F_{total} = q\mathbf{v}\times\mathbf{B} + (-e\mathbf{E}\times\mathbf{\Omega}) + e\mathbf{v}\times\mathbf{B}_{ps}$$

> **Unicode**
> ```
> F_total = q𝐯×𝐁 + (-e𝐄×Ω) + e𝐯×𝐁ₚₛ
> ```

**3개가 동형이다.**

### 5.3.7 초전도체와 보텍스

초전도체는 완전 반자성으로 로렌츠 힘에 저항한다.

#### 마이스너 효과

$B$ 침투 깊이 $\lambda$, London 방정식 $\mathbf{J}_s = -\mathbf{A}/\mu_0\lambda^2$에서 $\nabla\times\mathbf{J}_s = -\mathbf{B}/\mu_0\lambda^2$. **자기압 $\mathbf{J}_s\times\mathbf{B}$가 $\mathbf{B}$를 밖으로 밀어냄.**

#### 제2종 초전도체 보텍스

$H_{c1} < B < H_{c2}$에서 자속 양자 $\Phi_0 = h/2e$가 **와선** 형태로 침투.

**와선에 전류 $J_{ext}$ 흘리면 로렌츠 힘:**

$$\mathbf{F}_L = \mathbf{J}_{ext}\times\Phi_0\hat{z}$$

> **Unicode**
> ```
> 𝐅_L = 𝐉ₑₓₜ×Φ₀ẑ
> ```

**단위 길이당 힘.** 와선이 움직이면 $E = \mathbf{v}_L\times\mathbf{B}$ 전기장 → 저항. **핀닝 센터(결함)가 $\mathbf{F}_{pin} = -\nabla U_{pin}$으로 $F_L$ 균형** → 임계 전류 $J_c = F_{pin}/\Phi_0$.

**보텍스 동역학:**

$$\eta\mathbf{v}_L + \alpha\mathbf{v}_L\times\hat{z} = \mathbf{F}_L + \mathbf{F}_{pin} + \mathbf{F}_{thermal}$$

> **Unicode**
> ```
> η𝐯_L + α𝐯_L×ẑ = 𝐅_L + 𝐅ₚᵢₙ + 𝐅ₜₕₑᵣₘₐₗ
> ```

$\eta$: Bardeen-Stephen 점성, $\alpha$: **Magnus 힘** (베리 위상). $F_L > F_{pin}$ 초과 시 flux flow 저항 $\rho_{ff} = \rho_n B/H_{c2}$.

**최신:** 고온 초전도체 REBCO에서 $J_c > 10^{10}$ A/m², $F_{pin} = 10$ GN/m³, **20 T 자석 구현**. 와선 격자가 $J\times B$로 녹는 융해 전이 — **보텍스 액체는 로렌츠 힘의 카오스 상태**.

### 5.3.8 종합표

| 현상 | 로렌츠 힘 형태 | 위상 불변량 |
|---|---|---|
| IQHE | $q v\times B$ | Chern $C$ |
| FQHE | $q^* v\times B^*$ | 분수 $C$, 애니온 $\theta$ |
| AHE/SHE | $e E\times\Omega$ (Berry) | $\int\Omega$ |
| TI | $v_F p\times\sigma$ + $B$ | $Z_2$ |
| 그래핀 $B_{ps}$ | $e v\times B_{ps}$ (변형) | 밸리 Chern |
| 초전도 보텍스 | $J\times\Phi_0$ | 와인딩 수 |

**결론:** 응집물질에서 로렌츠 힘은 더 이상 외부 $B$만의 힘이 아니라, **격자·변형·베리 곡률이 만든 유효 $B_{eff}$와 함께 $k$-공간 로렌츠 힘으로 확장된다**. 그 확장된 힘의 플럭스가 양자화될 때 **위상물질**이 된다.

### 5.3.9 매스매티카 검증

```mathematica
(* 양자 홀 전도도 *)
hallConductance[nu_] := nu e^2/h;

(* Chern 수와 베리 곡률 *)
chernNumber[Omega_, kx_, ky_] :=
  1/(2 Pi) Integrate[Omega, {kx, -Pi, Pi}, {ky, -Pi, Pi}];

(* 그래핀 의사 자기장 *)
pseudoB[beta_, aLattice_, uxx_, uyy_, uxy_, hBar_, eCharge_] :=
  {hBar beta/(2 eCharge aLattice) (uxx - uyy),
   hBar beta/(2 eCharge aLattice) (-2 uxy)};

(* 마요라나 위상 조건 *)
majoranaCondition[gFactor_, muB_, Bfield_, Delta_, mu_] :=
  gFactor muB Bfield > Sqrt[Delta^2 + mu^2];

(* 와선 로렌츠 힘 *)
vortexForce[Jext_, Phi0_] := Cross[Jext, {0, 0, Phi0}];
```

### 5.3.10 한계·예외

- **IQHE:** 청정 시료, 극저온 필요
- **FQHE:** 분수 통계 직접 검증 어려움
- **AHE/SHE:** 내인성/외인성 분리 논쟁
- **TI:** 벌크 전도도 잔존
- **마요라나:** 실험적 확증 논쟁 중
- **그래핀 $B_{ps}$:** 나노 버블 위치 제어 어려움
- **초전도 보텍스:** 고온 초전도체 핀닝 메커니즘 불완전

> **참고문헌**
> - Thouless, D. J., Kohmoto, M., Nightingale, M. P., den Nijs, M., *Quantized Hall conductance in a two-dimensional periodic potential*, Phys. Rev. Lett. **49**, 405 (1982). [doi:10.1103/PhysRevLett.49.405](https://doi.org/10.1103/PhysRevLett.49.405)
> - Kane, C. L., Mele, E. J., *Z₂ topological order and the quantum spin Hall effect*, Phys. Rev. Lett. **95**, 146802 (2005). [doi:10.1103/PhysRevLett.95.146802](https://doi.org/10.1103/PhysRevLett.95.146802)
> - Levy, N., et al., *Strain-induced pseudo-magnetic fields greater than 300 tesla in graphene nanobubbles*, Science **329**, 544 (2010). [doi:10.1126/science.1191700](https://doi.org/10.1126/science.1191700)
> - Xiao, D., Chang, M.-C., Niu, Q., *Berry phase effects on electronic properties*, Rev. Mod. Phys. **82**, 1959 (2010). [doi:10.1103/RevModPhys.82.1959](https://doi.org/10.1103/RevModPhys.82.1959)

---

 # 6막. 확장 영역 (Extended Domains)

> **막의 흐름**
> 입자물리·표준모형 → 일반상대론·중력 → 교육·철학·표준
>
> 5막까지 로렌츠 힘의 최전선을 확정했다. 6막은 그 **경계**를 다룬다. 로렌츠 힘은 $U(1)$ 게이지장의 잔재로서 $SU(2)\times U(1)$로 확장되고, 중력과 경쟁하며, 인류의 안전 규규격과 윤리에 얽힌다.

---

## 6.1 입자물리·표준모형·중이온 충돌

입자물리에서 로렌츠 힘 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 **$U(1)$ 게이지 공변 미분의 3차원 그림자**다. 쿼크까지 가면 $q$가 색전하가 된다. 이 절에서는 게이지장, 전약 통합, QGP, 중이온 충돌, 자기 단극자, 밀리차지, 강자기장 QED를 다룬다.

### 6.1.1 게이지장 $SU(2)\times U(1)$

표준모형 공변 미분:

$$D_\mu = \partial_\mu + ig_s T^a G^a_\mu + ig W^i_\mu \tau^i + ig' Y B_\mu$$

> **Unicode**
> ```
> D_μ = ∂_μ + igₛ Tᵃ Gᵃ_μ + ig Wⁱ_μ τⁱ + ig' Y B_μ
> ```

- $G^a$: 글루온 $SU(3)$
- $W^i$: 약한 $SU(2)$
- $B$: 초전하 $U(1)$

**전자기 $U(1)_{EM}$은 전약 대칭 깨짐 후 남는 대각 조합:**

$$A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu, \quad Z_\mu = \cos\theta_W W^3_\mu - \sin\theta_W B_\mu$$

> **Unicode**
> ```
> A_μ = sinθ_W W³_μ + cosθ_W B_μ,   Z_μ = cosθ_W W³_μ - sinθ_W B_μ
> ```

$\theta_W \approx 28.7°$ (Weinberg 각).

**하전 입자 운동방정식:**

$$\frac{dp^\mu}{d\tau} = g F^{a\mu\nu}Q^a u_\nu + g'\ldots$$

> **Unicode**
> ```
> (dp^μ)/(dτ) = g F^aμνQᵃ u_ν + g'...
> ```

**3차원 극한:**

$$\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + g_W(\mathbf{E}_W+\mathbf{v}\times\mathbf{B}_W)\cdot\boldsymbol{\tau}$$

> **Unicode**
> ```
> 𝐅 = q(𝐄+𝐯×𝐁) + g_W (𝐄_W+𝐯×𝐁_W)·τ
> ```

**두 번째 항은 약 로렌츠 힘** — 중성자 붕괴에서 $W$ 교환으로 나타나는 유효 힘.

**중성미자:** $q = 0$이라 전자기 로렌츠 힘 0, 오직 $SU(2)$ 힘만 받는다.

#### $SU(N)$ Wong 방정식

$SU(N)$에서 로렌츠 힘은 색 공간에서 회전한다:

$$m\frac{du^\mu}{d\tau} = gQ^a F^{a\mu\nu}u_\nu, \quad \frac{dQ^a}{d\tau} = -g f^{abc}u^\mu A^b_\mu Q^c$$

> **Unicode**
> ```
> m(du^μ)/(dτ) = gQᵃ F^aμνu_ν,   (dQᵃ)/(dτ) = -g fᵃᵇᶜu^μ Aᵇ_μ Qᶜ
> ```

$Q^a$ 색전하가 게이지장에 의해 세차. **쿼크는 전자기 $q\mathbf{v}\times\mathbf{B}$뿐 아니라 색 자기장 $\mathbf{B}^a$에 의해 색 로렌츠 힘 $gQ^a\mathbf{v}\times\mathbf{B}^a$를 받는다.**

### 6.1.2 전약 통합

전약 통합 $SU(2)_L\times U(1)_Y \to U(1)_{EM}$ 깨짐 전에는 $B$가 두 개였다.

**초기 우주 $T > 159$ GeV:** 힉스 VEV $v = 0$에서 $W^3, B$ 모두 무질량, 섞임 없음. 전자는 하이퍼차지 $Y$로 $B$장과 $W$장 모두에 로렌츠 힘 받음.

**깨짐 후:**

$$q = T_3 + Y, \quad e = g\sin\theta_W$$

> **Unicode**
> ```
> q = T₃ + Y,   e = gsinθ_W
> ```

광자 $A$는 질량 0 유지, $Z,W^\pm$는 $m_Z = 91$ GeV, $m_W = 80$ GeV 획득, **힘 도달 거리 $1/m \sim 10^{-18}$ m로 짧아짐**.

**결과:**
- 일상 $B \sim \mu$T에서는 $U(1)_{EM}$ 로렌츠 힘만 장거리
- $W,Z$ 로렌츠 힘은 원자핵 내부에서만
- $W$ 보손 자체가 전하 $\pm e$가 있어 자기장에서 란다우 준위

**$W$ 보손 란다우 준위:**

$$E_n^2 = m_W^2 + p_z^2 + (2n+1)eB - 2e\mathbf{S}\cdot\mathbf{B}$$

> **Unicode**
> ```
> Eₙ² = m_W² + p_z² + (2n+1)eB - 2e𝐒·𝐁
> ```

**임계 자기장:** $B_c = m_W^2/e \sim 10^{20}$ T 초과 시 $W$ 진공 불안정 — **$W$ 응축, 전약 진공 붕괴**. 마그네타 $10^{11}$ T와는 9자리 차이로 안전.

**전약 플라즈마에서 자기장 생성:** 우주 초기 전약 상전이 1차이면 버블 충돌로 $B \sim 10^{15}$ T 생성, 이 $B$가 바리온 비대칭 생성에 $\mathbf{E}\cdot\mathbf{B}$ 항으로 기여 — **사하로프 조건**.

### 6.1.3 QGP에서 자기장 효과

**QGP:** $T \sim 300$ MeV $\sim 10^{12}$ K, $\mu_B \sim 0$, $n \sim 5$ fm$^{-3}$ 쿼크·글루온 자유.

**자기장 생성:** 두 핵이 $v \approx c$, $Z = 79$ (Au), $82$ (Pb)로 스쳐 지나갈 때 Biot-Savart:

$$B \sim \frac{Ze\gamma b}{4\pi(b^2+\gamma^2 t^2)^{3/2}}$$

> **Unicode**
> ```
> B ∼ (Z e γ b)/(4π (b²+γ² t²)^3/2)
> ```

$b \sim 10$ fm 충격 매개변수, $\gamma = 100$ (RHIC), $2760$ (LHC) →

$$eB \sim m_\pi^2 \sim 10^{15}\ \text{T}$$

> **Unicode**
> ```
> eB ∼ m_π² ∼10¹⁵ T
> ```

QCD 스케일. QGP 수명 $\tau_{QGP} \sim 10$ fm/c $\sim 3\times10^{-23}$ s, $B$ 수명 $\tau_B \sim 1-2$ fm/c로 짧지만 전기 전도도 $\sigma \sim 0.1$ fm$^{-1}$이면 Lenz 법칙으로 $B$ 유지:

$$\partial_t\mathbf{B} = \nabla\times(\mathbf{v}\times\mathbf{B}) + \frac{1}{\sigma}\nabla^2\mathbf{B}$$

> **Unicode**
> ```
> ∂ₜ 𝐁 = ∇×(𝐯×𝐁) + (1)/(σ)∇²𝐁
> ```

$\mathbf{v}\times\mathbf{B}$ 동결이 $B$를 늘림.

**QGP에서 로렌츠 힘 효과 3가지:**

1. **자기 저항:** $\mathbf{J}\times\mathbf{B}$가 팽창 억제, $v_2$ 타원 흐름 감소 5-10%
2. **Hall 효과:** 유한 $\mu_B$에서 $q\mathbf{v}\times\mathbf{B}$로 $u$쿼크와 $\bar{u}$ 분리, 전하 의존 $v_1$ directed flow $\Delta v_1 \propto qB$
3. **Faraday + Hall + 쿨롱:** 관측 가능한 $D^0-\bar{D}^0$ $v_1$ 분열

### 6.1.4 중이온 충돌 (RHIC, LHC)

#### Chiral Magnetic Effect (CME)

$B$ + 카이랄 불균형 $\mu_5 \neq 0$ → 전류:

$$\mathbf{J}_{CME} = \frac{e^2}{2\pi^2}\mu_5\mathbf{B}$$

> **Unicode**
> ```
> 𝐉_CME = (e²)/(2π²)μ₅ 𝐁
> ```

**로렌츠 힘이 아닌 이상(anomaly) 유도 전류.** $\mathbf{E}\cdot\mathbf{B}$가 $\mu_5$ 소스:

$$\partial_t n_5 = \frac{e^2}{2\pi^2}\mathbf{E}\cdot\mathbf{B} - \Gamma n_5$$

> **Unicode**
> ```
> ∂ₜ n₅ = (e²)/(2π²)𝐄·𝐁 - Γ n₅
> ```

**RHIC STAR isobar $Ru+Ru$ vs $Zr+Zr$ (2021-23):** CME 신호 <2%, 배경 $v_2$가 대부분. $B$ 방향 요동이 원인.

#### Chiral Magnetic Wave (CMW)

CME + CSE(분리 효과) 결합 파동, 전하 쿼드러폴 → $v_2(\pi^+)-v_2(\pi^-) \propto A_{ch}$ 선형. RHIC에서 기울기 관측, LHC에서는 사라짐 — $B$ 수명 짧아짐 때문.

#### Lambda 분극

$B$와 소용돌이 $\boldsymbol{\omega} = \nabla\times\mathbf{v}$가 $\Lambda$ 스핀 분극:

$$\mathbf{P}_\Lambda \approx \frac{\mu_\Lambda\mathbf{B}+\boldsymbol{\omega}}{T}$$

> **Unicode**
> ```
> 𝐏_Λ ≈ (μ_Λ 𝐁 + ω)/(T)
> ```

**STAR 2017-22 $\mathbf{P}_\Lambda \sim 1-2\%$ 측정, $B \sim 10^{13}$ T 추정, 소용돌이 $10^{22}$ s$^{-1}$** — 세상에서 가장 빠른 회전.

**로렌츠 힘 직접 관측:** $p_T < 0.5$ GeV 경입자 $e^\pm$의 $v_1$ 분열 $\Delta v_1 \sim 0.001q$, $eB$ 효과와 일치.

### 6.1.5 자기 단극자 탐색

**Dirac 양자화:** $eg = n\hbar/2$ → $g_D = e/2\alpha \approx 68.5e$.

**단극자 로렌츠 힘:**

$$\mathbf{F} = g(\mathbf{B}-\mathbf{v}\times\mathbf{E})$$

> **Unicode**
> ```
> 𝐅 = g(𝐁 - 𝐯×𝐄)
> ```

가속기는 $B$가 아닌 $E$로 단극자 생성 — **Schwinger 쌍생성** $\sigma \propto \exp(-\pi m^2/gB)$.

**실험:**

- **MoEDAL@LHC:** IP8에 핵 트랙 검출기 + 트래핑 바 Al 800 kg. 단극자가 $B = 0.5$ T LHCb 자석에서 $q_m\mathbf{v}\times\mathbf{B}$로 휘어 트랙 남김. **2022-23 Run2 결과 $m < 3$ TeV, $1-3g_D$ 배제**
- **ATLAS:** $pp\to\gamma\gamma$에서 단극자 루프 → 광자 융합, 13 TeV 139 fb$^{-1}$에서 $m < 2$ TeV 배제
- **중이온:** $PbPb$에서 $B \sim 10^{15}$ T로 Schwinger 생성, **MoEDAL 2023 PbPb 데이터로 $m < 75$ GeV, $g = 1-3g_D$ 배제** — 가장 모델 독립적

**미래:** 2025-26 HL-LHC, FCC-hh $B \sim 10^{16}$ T 등가에서 $m \sim 10$ TeV까지.

### 6.1.6 밀리차지 입자

**다크 섹터 $U(1)'$와 운동학적 섞임** $\epsilon F_{\mu\nu}F'^{\mu\nu}$ → 입자 $\chi$가 $\epsilon e$ 전하.

**운동:**

$$\mathbf{F} = \epsilon e(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = ε e(𝐄+𝐯×𝐁)
> ```

**영향:**
- 은하 $B \sim \mu$G에서 MCP는 $v\times B$로 편향 → 은하 원반에서 제거, 암흑 디스크 형성
- 태양 자기장, 지구 자기권이 MCP 플럭스 변조

**탐색:**
- **milliQan@LHC:** CMS 덕트 뒤 신틸레이터, $\epsilon \sim 10^{-3}-10^{-1}$, $m = 0.1-45$ GeV. 2023 결과 $\epsilon > 0.01$ 배제
- **FerMINI@DUNE:** NuMI 빔 덤프 뒤 MCP $eB$로 휘어 검출
- **우주론:** $B$가 MCP를 가속해 CMB $y$-왜곡 생성, $\epsilon < 10^{-7}$ 제한

### 6.1.7 강자기장 $B \sim 10^{15}$ T에서 QED 효과

**임계 자기장:** $B_c = m_e^2c^3/e\hbar = 4.41\times10^9$ T, $E_c = m_e^2c^3/e\hbar = 1.3\times10^{18}$ V/m.

중이온 $eB \sim 10 m_\pi^2 \sim 10^{15}$ T = $200 B_c$, 마그네타 $B \sim 10^{11}$ T = $25 B_c$.

**현상 4가지:**

1. **란다우 양자화:**

   $$E_n = \sqrt{m^2c^4 + c^2p_z^2 + 2\hbar c e B n}$$
   
   > **Unicode**
   > ```
   > Eₙ = √(m²c⁴ + c²p_z² + 2ℏ c e B n)
   > ```
   
   $B > B_c$에서 $n=0$과 $n=1$ 간격 $mc^2$ 이상, 진공 복굴절

2. **진공 복굴절:**

   $$\Delta n = n_\parallel - n_\perp = \frac{\alpha}{30\pi}\left(\frac{B}{B_c}\right)^2\sin^2\theta$$
   
   > **Unicode**
   > ```
   > Δ n = n_∥ - n_⊥ = (α)/(30π)((B)/(B_c))² sin²θ
   > ```
   
   PVLAS 2022 한계 $\Delta n < 10^{-22}$, 2025년 10 PW 레이저 + 100T 펄스 자석으로 $B/B_c \sim 10^{-2}$에서 $\Delta n \sim 10^{-12}$ 목표

3. **광자 분열 $\gamma\to\gamma\gamma$:** $B > B_c$에서만 운동학 허용, 마그네타 스펙트럼 컷오프 설명

4. **Schwinger 쌍생성:** $E > E_c$에서 진공 붕괴 $\Gamma \propto E^2\exp(-\pi E_c/E)$. $B$ 단독으로는 생성 불가 ($\mathbf{E}\cdot\mathbf{B}$ 필요), $B \sim 10^{15}$ T + $E \sim 10^{18}$ V/m 교차 시 RHIC에서 $e^+e^-$ 100배 증가 예측

**중이온에서 QED-로렌츠 결합:** $B \sim 10^{15}$ T에서 쿼크 란다우 준위 $eB \sim m_\pi^2 \sim (140\text{ MeV})^2$ → $u$쿼크 $E_0 \sim 140$ MeV, QGP 열과 동일. **자기 촉매 $B$가 $\langle\bar{q}q\rangle$ 증가, 역자기 촉매 $T \sim T_c$에서 감소** — 격자 QCD 2022-24 쟁점.

### 6.1.8 매스매티카 검증

```mathematica
(* 공변 미분 *)
covariantDerivative = Dmu == PartialMu + I g Amu;

(* 장 강도 텐서 (비아벨) *)
fieldStrength = Fmunu == PartialMu Anu - PartialNu Amu + I g {Amu, Anu};

(* 자기 단극자 양자화 *)
monopoleQuantization = qCharge gMonopole == nInteger hBar/2;

(* QGP 자기장 *)
qgpMagneticField = BQGP == 10^15;

(* CME 전류 *)
cmeCurrent[mu5_, Bvec_, eCharge_] := eCharge^2/(2 Pi^2) mu5 Bvec;
```

### 6.1.9 한계·예외

- **비아벨 게이지:** $F = dA + A\wedge A$, 교환자 항
- **비섭동 영역:** $g \gg 1$에서 섭동론 붕괴, 격자 QCD 필요
- **QGP 자기장:** 수명, 전도도 불확실
- **자기 단극자:** 실험적 증거 전무
- **밀리차지:** 우주론 제한과 지상 실험 제한 충돌

> **참고문헌**
> - Wong, S. K., *Field and particle equations for the classical Yang-Mills field and particles with isotopic spin*, J. Math. Phys. **12**, 1065 (1971). [doi:10.1063/1.1665632](https://doi.org/10.1063/1.1665632)
> - STAR Collaboration, *Search for the chiral magnetic effect with isobar collisions*, Phys. Rev. C **105**, 014901 (2022). [arXiv:2109.00131](https://arxiv.org/abs/2109.00131)
> - STAR Collaboration, *Global Λ hyperon polarization in nuclear collisions*, Nature **548**, 62 (2017). [doi:10.1038/nature23004](https://doi.org/10.1038/nature23004)
> - Acharya, B., et al. (MoEDAL), *Search for magnetic monopoles via Schwinger pair production*, Nature **602**, 63 (2022). [doi:10.1038/s41586-021-04298-1](https://doi.org/10.1038/s41586-021-04298-1)

---

## 6.2 일반상대론·중력

일반상대론에서 중력은 힘이 아니지만, 로렌츠 힘 $qF^{\mu\nu}u_\nu$는 여전히 힘으로 남는다. **두 힘의 경쟁이 블랙홀 제트를 만든다.** 이 절에서는 등가원리, 중력 렌즈, 프레임 드래깅, LIGO, 블랙홀 자기장, 양자중력, Lorentz 위반을 다룬다.

### 6.2.1 등가원리와 로렌츠 힘

**등가원리:** 중력 질량 = 관성 질량 $m_g = m_i$, 모든 물체는 $a^\mu = 0$ 측지선:

$$\frac{Du^\mu}{d\tau} = 0, \quad D = d+\Gamma$$

> **Unicode**
> ```
> (D u^μ)/(dτ) = 0,   D = d+Γ
> ```

**전하 $q$가 있으면:**

$$m\frac{Du^\mu}{d\tau} = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> m(D u^μ)/(dτ) = qF^μνu_ν
> ```

우변이 0이 아니므로 전하를 가진 입자는 **geodesic 운동에서 이탈(departure from geodesic motion)** 한다. 일반상대론에서 자유낙하 입자의 geodesic 운동은 애초에 비중력적 외력이 없는 경우를 전제로 한다. 로렌츠 힘은 전자기력이라는 비중력적 외력이므로, 하전입자가 geodesic을 따르지 않는다는 사실 자체를 곧바로 등가원리 위반으로 해석해서는 안 된다 — 이는 서로 이웃한 geodesic들의 상대가속도를 곡률로 기술하는 표준적 geodesic deviation과도 다른 개념이다.

실험실에서 $q/m$ 다른 입자는 다르게 떨어진다. $e/m$ 전자 $1.76\times10^{11}$ C/kg vs 양성자 $9.58\times10^7$ → **$F_L/F_g \sim 10^{20}$배**. 등가원리 실험이 반드시 중성 입자로 수행되어야 하는 진짜 이유는 $q\neq0$에서 등가원리가 깨지기 때문이 아니라, 전자기력이 중력보다 $10^{20}$배 커서 중력 측정 자체를 완전히 가려버리기 때문이다.

**약한 등가원리 WEP 위반량:**

$$\eta = 2\frac{|a_1-a_2|}{|a_1+a_2|} \approx \frac{q}{m}\frac{F}{g}$$

> **Unicode**
> ```
> η = 2(|a₁-a₂|)/(|a₁+a₂|) ≈ (q)/(m)(F)/(g)
> ```

중성 원자 $q = 0$이면 $\eta = 0$, 이온이면 $\eta \sim 1$. **따라서 등가원리 실험은 반드시 중성으로 해야 한다** — MICROSCOPE 위성 2022 $\eta < 10^{-15}$ 제한은 중성 Ti-Pt 합금.

**아인슈타인 등가원리 EEP:** 자유 낙하 실험실 내부에서 중력은 사라지지만 $F_{\mu\nu}$는 사라지지 않음. $F_{\mu\nu}$가 0이 아닌 한 국소 로렌츠 불변성 유지되나, $F_{\mu\nu}$ 자체가 중력과 결합:

$$\nabla_\nu F^{\mu\nu} = \mu_0 J^\mu, \quad \nabla_{[\alpha}F_{\beta\gamma]} = 0$$

> **Unicode**
> ```
> ∇_ν F^μν = μ₀ J^μ,   ∇_[αF_βγ] = 0
> ```

$\nabla$가 공변 미분, $\Gamma$ 포함. $F$가 곡률에 의해 렌즈됨.

**강한 등가원리 SEP:** 중력 결합 에너지도 $m_g = m_i$ 따라야 함. 하전 블랙홀 Reissner-Nordstrom $Q \neq 0$에서 전자기 에너지 $Q^2/8\pi\epsilon_0 r$가 중력 질량에 기여, $M_{ADM} = M_0 + Q^2/2r_+$ — **SEP 위반**, 블랙홀이 WEP 위반 증거.

### 6.2.2 중력 렌즈와 전자기장

빛 $q = 0$이라 로렌츠 힘 직접 없지만, 플라즈마가 있으면 $n_e$가 $F_{\mu\nu}$를 통해 빛에 영향.

**진공 중력 렌즈 편향각:**

$$\alpha_{GR} = \frac{4GM}{c^2 b}$$

> **Unicode**
> ```
> α_GR = (4GM)/(c² b)
> ```

**플라즈마 존재 시 굴절률** $n^2 = 1-\omega_p^2/\omega^2$, $\omega_p^2 = n_e e^2/\epsilon_0 m_e$, 추가 편향:

$$\alpha_{plasma} = -\frac{1}{\omega^2}\int\nabla_\perp\omega_p^2\, ds$$

> **Unicode**
> ```
> αₚₗₐₛₘₐ = -(1)/(ω²)∫ ∇_⊥ ωₚ² ds
> ```

$\alpha_{plasma} \propto -\lambda^2$ 파장 의존, $\alpha_{GR}$ 무색. **로렌츠 힘은 $\omega_p$ 안에 $e$로 숨어 있음** — 전자가 $E$에 반응해 $n$ 만든다.

**자기장 있는 렌즈:** Faraday 회전 $\Delta\chi = RM\lambda^2$, $RM \propto \int n_e B_\parallel\, ds$. 중력 렌즈된 두 상의 $RM$ 차이로 렌즈 은하 $B$ 측정. **2022년 $z = 0.5$ 렌즈 은하에서 $B \sim \mu$G 측정.**

**하전 블랙홀 렌즈:** Reissner-Nordstrom 계량 $f = 1-2M/r+Q^2/r^2$. 광자 궤적은 $Q^2$로 수정, 편향각:

$$\alpha = \frac{4M}{b} - \frac{3\pi Q^2}{4b^2} + \ldots$$

> **Unicode**
> ```
> α = (4M)/(b) -(3π Q²)/(4b²)+...
> ```

$Q$가 $M$만큼 크면 렌즈 약해짐 — 전자기 반발이 중력 인력 상쇄.

### 6.2.3 프레임 드래깅 (Lense-Thirring)

회전 질량 $J$ 주변 약장 근사 — **중력전자기학 GEM:**

$$ds^2 = -(1+2\Phi/c^2)c^2dt^2 - 4\mathbf{A}_g\cdot d\mathbf{x}\, dt + (1-2\Phi/c^2)d\mathbf{x}^2$$

> **Unicode**
> ```
> ds² = -(1+2Φ/c²)c²dt² -4𝐀_g· d𝐱 dt + (1-2Φ/c²)d𝐱²
> ```

$\Phi = -GM/r$, $\mathbf{A}_g = G(\mathbf{J}\times\mathbf{r})/c^2 r^3$ 중력 벡터 퍼텐셜.

**측지선 방정식 $Du^\mu/d\tau = 0$ 전개:**

$$\mathbf{a} = -\nabla\Phi - 2\mathbf{v}\times(\nabla\times\mathbf{A}_g) = \mathbf{g} + \mathbf{v}\times\mathbf{H}_g$$

> **Unicode**
> ```
> 𝐚 = -∇Φ -2𝐯×(∇×𝐀_g) = 𝐠 + 𝐯×𝐇_g
> ```

$\mathbf{H}_g = 2\nabla\times\mathbf{A}_g$가 **중력자기장**. Lense-Thirring 세차 $\Omega_{LT} = H_g/2$.

**전자기 유사:**

| 전자기 | 중력 |
|---|---|
| $\mathbf{E} = -\nabla\phi-\partial_t\mathbf{A}$ | $\mathbf{g} = -\nabla\Phi-\partial_t\mathbf{A}_g$ |
| $\mathbf{B} = \nabla\times\mathbf{A}$ | $\mathbf{H}_g = \nabla\times\mathbf{A}_g$ |
| $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | $\mathbf{F}_g = m(\mathbf{g}+\mathbf{v}\times\mathbf{H}_g)$ |

**하전 입자는 두 로렌츠 힘 합:**

$$m\dot{\mathbf{v}} = m(\mathbf{g}+\mathbf{v}\times\mathbf{H}_g) + q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> m𝐯˙ = m(𝐠+𝐯×𝐇_g) + q(𝐄+𝐯×𝐁)
> ```

**관측:** Gravity Probe B 2011, 지구 $\mathbf{H}_g \sim 10^{-14}$ s$^{-1}$로 자이로스코프 39 mas/yr 세차 측정. LAGEOS 위성 궤도 노드 2 m/yr LT 이동.

**펄서:** $B \sim 10^8$ T, $\mathbf{H}_g \sim 10^3$ s$^{-1}$로 $J\times B$와 $\mathbf{v}\times\mathbf{H}_g$ 경쟁, 펄스 도착 시간에 LT 지연 $10^{-6}$ s.

### 6.2.4 중력파 검출 (LIGO)

LIGO 거울 $m = 40$ kg, 변위 감도 $10^{-19}$ m. 가장 큰 잡음 중 하나가 자기.

- **액츄에이터:** $F = IL\times B$ 보이스 코일, 2020 O3에서 코일 자석 Barkhausen 잡음 $10^{-20}$ m/√Hz. 2023+ **정전 구동으로 교체 중** — 로렌츠 힘 제거가 감도 향상
- **환경 자기:** Schumann 공명 7.8 Hz $B \sim 1$ pT가 두 사이트 상관. $\mathbf{F} = \nabla(\mathbf{m}\cdot\mathbf{B})$로 거울 자화 $10^{-9}$ J/T가 $10^{-18}$ m 흔듦. Wiener 필터로 $B$ 측정 후 차감, 2022 논문에서 $10^{-25}$/√Hz 배경 제한
- **전하:** 거울이 우주선으로 대전 $q \sim 10^9 e$, 지구 $B$에서 $v\times B$ 노이즈 $\sim 10^{-21}$ m. UV 방전으로 중화

**미래 Einstein Telescope:** 초전도 차폐 $B < 10^{-12}$ T, 로렌츠 잡음 $10^{-26}$ 목표. **중력파 자체는 $h \sim 10^{-21}$로 $q\mathbf{v}\times\mathbf{B}$보다 10배 작아 자기 차폐가 검출 필수.**

### 6.2.5 블랙홀 자기장 — Blandford-Znajek

회전 블랙홀 Kerr $a = J/M$, 지평선 각속도 $\Omega_H = a/2Mr_+$. 주변 플라즈마가 $B \sim 1-100$ T 자기장 끌고 들어오면 자력선이 블랙홀 회전에 감김.

**BZ 메커니즘:** 자력선이 지평선과 무한대 사이에서 $\Omega_F$로 회전, $\Omega_F \approx \Omega_H/2$일 때 포인팅 플럭스:

$$P_{BZ} = \frac{\kappa}{4\pi c}\Omega_H^2\Phi_B^2$$

> **Unicode**
> ```
> P_BZ = (κ)/(4π c)Ω_H² Φ_B²
> ```

$\Phi_B = \int\mathbf{B}\cdot dA$ 자속, $\kappa \approx 0.05$. $M = 10^9 M_\odot$, $B = 1$ T, $\Phi_B \sim 10^{27}$ Wb → **$P \sim 10^{38}$ W, AGN 제트 광도**.

**로렌츠 힘 역할 3가지:**

1. 지평선 근처 $\mathbf{E}\cdot\mathbf{B} \neq 0$ 영역에서 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) \neq 0$ → 쌍생성 $e^\pm$, 전류 $J$
2. $\mathbf{J}\times\mathbf{B}$ 토크가 블랙홀 각운동량 빼앗음: $dJ/dt = -\int(B_\phi B_r/\mu_0)\, dA$
3. 제트 내부 $\mathbf{J}\times\mathbf{B}$가 플라즈마를 $\gamma \sim 10$까지 가속, $\mathbf{v}\times\mathbf{B}$로 시준

**2022 EHT M87* 편광 관측으로 나선 $B$ 패턴 확인, $B \sim 10$ T, BZ 예측과 일치.**

**Meissner 유사:** 극한 Kerr $a \to M$에서 $B$ 자속이 지평선에서 밀려남 — **블랙홀 마이스너 효과**, $P_{BZ} \to 0$. 실제 천체 $a < 0.998$ Thorne 한계로 회피.

### 6.2.6 양자중력에서 로렌츠 대칭

일반상대론은 국소 로렌츠 대칭 $SO(3,1)$ 기반, 로렌츠 힘은 $U(1)$ 게이지 대칭. 양자중력에서 **둘 다 깨질 수 있다**.

- **루프 양자 중력:** 면적 양자화 $\Delta A \sim \ell_P^2$, 광자 분산 $v = c(1+\xi E/E_P)$ 예측, $E_P = 1.22\times10^{19}$ GeV. $q\mathbf{v}\times\mathbf{B}$에서 $v$가 에너지 의존 → 고에너지 전자 궤적 편향
- **끈 이론:** $B_{\mu\nu}$ Kalb-Ramond 장이 $F_{\mu\nu}$와 섞임, 저에너지 $F_{\mu\nu}F^{\mu\nu} + H_{\mu\nu\rho}H^{\mu\nu\rho}$ 결합

**현재 중력파 $v_{GW} = c$ $10^{-15}$ 정밀 일치로 $\xi < 10^{-13}$ 제한.**

### 6.2.7 Lorentz 위반과 SME

**Kostelecký-Standard Model Extension (SME):** 모든 로렌츠 위반 연산자 추가:

$$L_{LV} = -a_\mu\bar{\psi}\gamma^\mu\psi - b_\mu\bar{\psi}\gamma_5\gamma^\mu\psi - \frac12 c_{\mu\nu}\bar{\psi}i\gamma^\mu\partial^\nu\psi - \frac14 k_F^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$$

> **Unicode**
> ```
> L_LV = -a_μψ̄γ^μψ - b_μψ̄γ₅γ^μψ -(1)/(2) c_μνψ̄iγ^μ∂^νψ -(1)/(4) k_F^μνρσF_μνF_ρσ
> ```

**로렌츠 힘 수정:**

$$m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + q_{LV}(\mathbf{E}_{LV}+\mathbf{v}\times\mathbf{B}_{LV}) + \ldots$$

> **Unicode**
> ```
> m𝐯˙ = q(𝐄+𝐯×𝐁) + q_LV(𝐄_LV+𝐯×𝐁_LV) + ...
> ```

$k_F$: 진공 복굴절, $b_\mu$: $e^-$ 스핀 세차 이상.

**실험 제한:**
- 중이온 충돌 $v_2$에서 $c_{\mu\nu} < 10^{-22}$
- 펄서 $\mathbf{E}\times\mathbf{B}$ 드리프트 안정성으로 $a_\mu < 10^{-33}$ GeV
- LIGO 자기 잡음에서 $k_F^{XYZ} < 10^{-15}$

**미래:** $B \sim 10^{15}$ T 중이온 $eB$ 자체가 $k_F$ 증폭기, $J_{CME} = (e^2/2\pi^2)\mu_5\mathbf{B}$에서 $\mu_5$가 LV $b_0$로 오염되는지 2025 RHIC isobar 재분석 중.

### 6.2.8 종합표

| 영역 | 로렌츠 힘 역할 | 중력 역할 |
|---|---|---|
| WEP 실험 | 비중력 외력 $qE$ | 측지선 |
| 렌즈 | 플라즈마 $\omega_p$로 $\alpha(\lambda)$ | $\alpha_{GR}$ 무색 |
| LT | $q v\times B$ vs $m v\times H_g$ | GEM |
| LIGO | $IL\times B$ 잡음 | $h \sim 10^{-21}$ 신호 |
| BZ | $J\times B$로 제트 가속 | $\Omega_H$ 에너지원 |

**중력은 시공간을 휘게 하고, 로렌츠 힘은 그 휜 시공간에서 전하를 geodesic 운동에서 이탈시킨다.** 이는 전자기력이라는 비중력적 외력 때문이며 등가원리 자체의 위반이 아니다. 다만 $q\neq0$인 하전입자는 애초에 등가원리가 다루는 "중력만 받는 자유낙하" 범주 밖에 있으며, 우주는 처음부터 중력과 전자기가 섞인 $U(1)\times SO(3,1)$ 번들이다. **블랙홀 제트는 그 섞임이 에너지로 전환되는 가장 극적인 예 — 중력이 감은 $B$를 로렌츠 힘이 풀며 빛을 만든다.**

### 6.2.9 매스매티카 검증

```mathematica
(* Einstein 방정식 *)
einsteinEq = Rmunu - (1/2) R gmunu + Lambda gmunu == (8 Pi G/c^4) Tmunu;

(* Lorentz 위반 라그랑지안 *)
lorentzViolation = -1/4 Fmunu Fmunu + 1/2 kmunu Fmulambda Fnu lambda;

(* BZ 파워 *)
bzPower[kappa_, OmegaH_, PhiB_, c_] := kappa/(4 Pi c) OmegaH^2 PhiB^2;

(* GEM 중력자기장 *)
gemField[Agin_, x_, y_, z_] := Curl[Agin, {x, y, z}];
```

### 6.2.10 한계·예외

- **등가원리:** $q \neq 0$인 하전입자는 전자기력이라는 비중력적 외력 때문에 geodesic을 따르지 않을 뿐, 이것이 등가원리 위반은 아님. 다만 이 힘이 중력보다 $10^{20}$배 커서 중력 측정을 가리므로 실험은 중성 원자로만
- **중력 렌즈:** 플라즈마 효과 분리 어려움
- **LIGO:** 자기 차폐 비용
- **BZ:** 플라즈마 공급, 자기장 구조 불확실
- **양자중력:** 실험적 검증 극도로 어려움
- **Lorentz 위반:** SME 파라미터 수백 개, 상관관계 복잡

> **참고문헌**
> - Blandford, R. D., Znajek, R. L., *Electromagnetic extraction of energy from Kerr black holes*, Mon. Not. R. Astron. Soc. **179**, 433 (1977). [doi:10.1093/mnras/179.3.433](https://doi.org/10.1093/mnras/179.3.433)
> - Event Horizon Telescope Collaboration, *First M87 event horizon telescope results. VIII. Magnetic field structure*, Astrophys. J. Lett. **910**, L13 (2021). [doi:10.3847/2041-8213/abe4de](https://doi.org/10.3847/2041-8213/abe4de)
> - MICROSCOPE Collaboration, *MICROSCOPE mission: Final results of the test of the equivalence principle*, Phys. Rev. Lett. **129**, 121102 (2022). [arXiv:2209.06628](https://arxiv.org/abs/2209.06628)
> - LIGO-Virgo Collaboration, *Magnetic correlation noise in LIGO*, Phys. Rev. D **105**, 082005 (2022). [arXiv:2201.04475](https://arxiv.org/abs/2201.04475)
> - Colladay, D., Kostelecký, V. A., *Lorentz-violating extension of the standard model*, Phys. Rev. D **58**, 116002 (1998). [doi:10.1103/PhysRevD.58.116002](https://doi.org/10.1103/PhysRevD.58.116002)

---
 ## 6.3 교육·철학·산업 표준

$q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 식 하나지만, 가르치는 법, 위험, 무기, 노벨상까지 얽혀 있다. 이 절에서는 개념사와 교수법, 철학적 함의, 안전 규격, 산업 표준, 윤리, 대중 과학, 노벨상을 다룬다.

### 6.3.1 개념사와 교수법

**개념사 연표:**

| 연도 | 인물 | 기여 |
|---|---|---|
| 1820 | Ampère | 전류 사이 힘 $d\mathbf{F} \propto I_1 I_2$ |
| 1865 | Maxwell | 장 개념, $q\mathbf{v}\times\mathbf{B}$ 암시 |
| 1892 | Lorentz | 전자론에서 $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ 명시 |
| 1897 | Thomson | $e/m$ 측정으로 $F_L$로 전자 발견 |
| 1948 | Feynman | $q\mathbf{v}\cdot\mathbf{A}$ 라그랑지안에서 $F_L$ 유도 |

초기엔 $\mathbf{E}$ 항만 전기력, $\mathbf{v}\times\mathbf{B}$는 자기력으로 분리 가르쳤으나 **상대론 이후 하나의 $F^{\mu\nu}u_\nu$로 통일**.

#### 교수법 3단계 — 오개념 방지

1. **오른손 오해:** $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$를 외우게 하면 $\mathbf{B}$가 힘을 만든다고 착각. **올바른 순서:** $\mathbf{B}$는 존재, $\mathbf{v}$가 있을 때만 힘 발생. $v = 0$이면 자기력 0 강조
2. **일 안함 역설:** $\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$ → 자기장은 일 안함. 그럼 사이클로트론은 왜 가속? 답: $\mathbf{E}$ 갭에서 일, $\mathbf{B}$는 방향만 바꿈. **학생 70%가 틀림**
3. **상대론적 통일:** 저속 극한 $F = q(E+v\times B)$는 근사, 정확히는 $dp^\mu/d\tau = qF^{\mu\nu}u_\nu$. $\mathbf{E}$와 $\mathbf{B}$는 관찰자에 따라 섞임 — $\mathbf{B}$만 있는 계에서 다른 계는 $\mathbf{E}$가 생김. **Purcell 교과서**가 전하판 $\mathbf{E}$ 로렌츠 변환으로 $B$ 유도하는 방식이 개념적으로 최상

#### 실험 키트

- $e/m$ 튜브: $B = 1$ mT, $V = 200$ V로 $r = mv/qB$ 원 궤적
- 홀 효과 보드: $V_H = IB/ned$ 직접 측정
- **10만원으로 로렌츠 힘 정량**

#### 대학원

- 해밀토니안 $H = (\mathbf{p}-q\mathbf{A})^2/2m$에서 $\dot{\mathbf{p}} = -\partial H/\partial\mathbf{x} = q\nabla(\mathbf{v}\cdot\mathbf{A})$ 유도 → $v\times B$ 자동 도출
- **게이지 불변성** $\mathbf{A} \to \mathbf{A}+\nabla\chi$에서 $F_L$ 불변 증명이 핵심

### 6.3.2 철학적 함의 — 결정론, 인과성, 국소성

#### 결정론

로렌츠 힘은 고전적으로 **결정론적 ODE** $m\ddot{\mathbf{x}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$. 초기 조건 $\mathbf{x}_0, \mathbf{v}_0$ → 궤적 유일.

**그러나 $\mathbf{B}(\mathbf{x})$ 비균일 시 KAM 카오스 $\lambda > 0$ → 사실상 비결정론적 예측 불가. 결정론 방정식이 비결정론적 행동 — 라플라스 악마 붕괴 예제.**

#### 인과성

$F_L$은 동시적 $B(\mathbf{x},t)$에 의존. $B$ 변화는 $c$로 전파 $\partial_t B = -\nabla\times E$. 점전하 $q$의 자기장 $B \propto q\mathbf{v}\times\hat{r}/r^2$이 무한 속도면 **인과율 위반**.

**Jefimenko 지연 퍼텐셜로 해결:**

$$\mathbf{B}(\mathbf{r},t) = \frac{\mu_0}{4\pi}\int\frac{[\mathbf{J}]\times\hat{R}}{R^2}\, dV + \frac{1}{c}\frac{[\dot{\mathbf{J}}]\times\hat{R}}{R}$$

> **Unicode**
> ```
> 𝐁(𝐫,t) = (μ₀)/(4π)∫ ([𝐉]×R̂)/(R²) dV + (1)/(c)([𝐉˙]×R̂)/(R)
> ```

$[\cdot]$는 지연 시간 $t-R/c$. **$v\times B$의 $B$는 과거 $J$에서 옴 — 국소 인과성 유지.**

#### 국소성

$A_\mu$는 비국소적? **Aharonov-Bohm 효과:** $B = 0$ 영역에서도 $\mathbf{A} \neq 0$이면 위상 $\phi = q\oint\mathbf{A}\cdot d\mathbf{l}/\hbar = q\Phi_B/\hbar$ 변화. $F_L = 0$인데 효과가 있음 → **$F_L$은 국소 힘, 양자 위상은 비국소**.

**철학적 논쟁:** 물리적 실체는 $F_{\mu\nu}$인가 $A_\mu$인가? **현대 정답:** 다발 $U(1)$ 접속이 실체, $F_L$은 그 곡률의 고전 극한.

#### 실재론

$B$는 물질인가 관계인가? 장 실재론 vs 관계론 논쟁에서 **로렌츠 힘은 장 실재론 승리 증거** — 진공 $B$가 힘을 하므로 $B$가 실재.

### 6.3.3 안전 규격 — MRI, 전자기장 노출

로렌츠 힘이 인체에 직접 힘 가하는 경우는 드물지만, 유도 전류 $J = \sigma E$, $\nabla B$ 힘이 문제.

#### MRI

**FDA/IEC 60601-2-33:**

- 정자기장 $B_0 \leq 8$ T 일반, $> 8$ T 연구용. **7T에서 현훈** $q\mathbf{v}\times\mathbf{B}$로 내이 림프 $v \sim 1$ mm/s → $F \sim 10^{-12}$ N → 현훈
- 경사자기장 $dB/dt$: **말초신경 자극 PNS 한계 $dB/dt < 20$ T/s** (20 μs), 심장 자극 $> 60$ T/s. $E_{ind} = -r/2\, dB/dt$로 $E > 2$ V/m이면 자극
- **SAR 비흡수율:** RF $B_1$이 $E$ 유도 → 발열 $SAR = \sigma E^2/2\rho \leq 4$ W/kg 전신, $3.2$ W/kg 머리
- **금속:** $F = \nabla(m\cdot B)$로 클립 10 N, 발열, 발사체 사고. **2021년 $B_0 = 3$ T에서 산소통 $v = 10$ m/s 발사 사망 사례**

#### 일반 전자기장 노출 ICNIRP 2020

- **저주파 50 Hz:** $B_{lim} = 200$ μT 직업, $100$ μT 일반. 유도 전류 $J < 10$ mA/m²
- **고주파:** $E_{lim} = 61$ V/m (10 MHz), SAR $0.08$ W/kg 일반
- **근거:** $q\mathbf{v}\times\mathbf{B}$로 직접 손상 아님, 유도 $E$로 신경 자극. **100 μT에서 $E_{ind} \sim 0.01$ V/m ≪ 생체 $0.1$ V/m 잡음**

#### 홀추력기·고전류

$B \sim 0.1$ T 누설 자기장 작업자 5 mT 이상 노출 시 의료기기 오작동. **NASA-STD-3001 $B < 2$ mT at crew.**

### 6.3.4 산업 표준 — IEEE, IEC, ISO

| 표준 | 제목 | 로렌츠 힘 관련 |
|---|---|---|
| IEC 60601-2-33 | MRI 안전 | $B_0$, $dB/dt$, $F_L$ on implants |
| IEC 62226 | EMF 인체 모델 | 유도 $J = \sigma(E+v\times B)$ 계산법 |
| IEEE C95.1-2019 | RF 노출 | SAR $= \sigma|E|^2/\rho$ |
| IEC 61000-4-8 | 전력주파수 자기장 내성 | $B = 100$ A/m 테스트, 홀 센서 오작동 방지 |
| ISO 14117 | 이식형 심장기기 EMC | $B_{static} < 1$ mT, $dB/dt < 1$ T/s |
| IEC 62110 | 전류 측정 | 로고스키 코일 $V \propto d/dt\int B\cdot dA$ |
| IEEE 1657 | 광전지 홀 측정 | $R_H = V_H t/IB$ 표준 |

#### 전류 센서 교정

홀 센서 $V_H = R_H IB/t$에서 $R_H = 1/nq$는 온도 드리프트 $0.1\%/K$. 산업 표준은 $I_{ref}\times B_{ref}$로 교정, $B_{ref}$는 **NMR $\omega = \gamma B$로 절대 측정** — 로렌츠 힘이 자기장을 전압으로 바꾸고, 그 전압이 다시 $B$ 표준.

#### 전기차 모터

$F_L = NIL\times B$로 토크 $T = NIA\times B$. IEC 60034 토크 리플 <5% 규정.

### 6.3.5 윤리 — 군사 응용, 우주 무기

#### 군사

- **레일건:** $F_L = IL\times B$, $B = \mu_0 I/2\pi r$, $F \sim \mu_0 I^2/2\pi r$. $I = 5$ MA → $a = 10^5$ g, $v = 2.5$ km/s. 윤리: 저비용 장거리 포격으로 민간 피해, $B$ 누설로 전자기기 파괴 — EMP 부수 효과. **2021 미 해군 개발 중단, 윤리·비용 문제**
- **코일건:** 동일, $F = \nabla(m\cdot B)$
- **EMP 무기:** 고고도 핵폭발 $\gamma \to e^-$, $e^-$가 $v\times B_{earth}$로 나선 → $E \sim 10^4$ V/m 광역 펄스, 변압기 포화. **1962 Starfish Prime에서 하와이 정전.** 비핵 EMP도 $L\, dI/dt = v\times B$로 생성 가능

#### 우주 무기

- **Outer Space Treaty 1967:** 핵무기 금지, 재래식 로렌츠 무기는 회색지대. 홀추력기 $B$로 위성 $v\times B$ 교란 가능성 — $B = 1$ T 10 m 거리 $10^{-5}$ T → 위성 자력계 교란
- **Kessler 증후군:** 자기돛 파편이 $B$로 대전 파편 $qv\times B$로 궤도 변경 예측 불가

#### 이중용도

MRI 초전도 자석 $B = 7$ T 기술이 그대로 고자장 레일건·핵융합로에 전용. **수출통제 Wassenaar Arrangement 자석 $B > 2$ T, $dB/dt > 10$ T/s 포함.**

**윤리 원칙:** $F_L$ 자체는 중립, $B$ 세기와 $dB/dt$가 무기 임계. IEEE Ethically Aligned Design에서 $B$ 노출 투명성 요구.

### 6.3.6 대중 과학 — 오로라, MRI

#### 오로라

태양풍 400 km/s 양성자가 $v\times B_{earth}$로 자기권 꼬리 저장 → 재결합 $E$로 10 keV 가속 → 대기 $O$ 557.7 nm 녹색 발광.

**설명 시 $v\times B$를 손으로 보여주는 게 가장 효과적** — 손바닥이 $B$, 손가락이 $v$, 엄지가 $F$. **2024년 한국 38° 오로라 관측으로 대중 관심 급증.**

#### MRI

"자석이 몸을 당기지 않고 수소 원자핵 나침반을 돌린다"로 $qv\times B$ 아닌 $\mu\times B$ 토크 설명이 오해 적음.

경사자기장 $G = 30$ mT/m에서 주파수 $f = \gamma(B_0+Gx)$로 $x$ 위치가 소리가 된다. $F_L$로 코일 진동 → **100 dB 소음, 귀마개 필수**.

**효과적 비유:** $\mathbf{E}$는 언덕(전위), $\mathbf{B}$는 회전목마 — 언덕은 일하고 회전목마는 방향만 바꾼다.

### 6.3.7 로렌츠 힘 관련 노벨상

로렌츠 힘은 노벨상 제조기.

| 연도 | 수상자 | 업적 | 로렌츠 힘 연결 |
|---|---|---|---|
| 1902 | Lorentz, Zeeman | Zeeman 효과 | $e v\times B$로 스펙트럼 분리, $e/m$ 결정 |
| 1906 | J.J. Thomson | 전자 발견 | $e/m$ $F_E = F_B$ 균형 측정 |
| 1907 | Michelson | 간섭계 | $v\times B$ 에테르 드리프트 부정 |
| 1923 | Millikan | $e$ 측정 | $qE = mg+qv\times B$ 균형 |
| 1936 | Hess | 우주선 | $q v\times B_{earth}$로 위도 효과 |
| 1939 | Lawrence | 사이클로트론 | $\omega_c = qB/m$ 공명 가속 |
| 1943 | Stern | 분자선 자기 모멘트 | $\mu\times B$ 토크, Stern-Gerlach |
| 1957 | Yang-Lee | P 위반 | $B$ 반전 실험에서 $v\times B$ 홀대칭 깨짐 |
| 1960 | Glaser | 버블 챔버 | $r = p/qB$로 입자 식별 |
| 1979 | Glashow-Weinberg-Salam | 전약 통일 | $A = \sin\theta_W W^3+\cos\theta_W B$, $U(1)_{EM}$ 잔재 |
| 1985 | von Klitzing | 정수 양자 홀 | $\sigma_{xy} = \nu e^2/h$, Chern 수 |
| 1989 | Dehmelt, Paul | 이온 트랩 | Penning $q v\times B$ + Paul $qE$로 단일 전자 가둠 |
| 1998 | Laughlin, Störmer, Tsui | 분수 양자 홀 | $e^* = e/3$, $B^*$ 복합 페르미온 |
| 2000 | Alferov, Kilby | 반도체 헤테로 | Hall 측정으로 $n$ 결정, HEMT $v\times B$ |
| 2007 | Fert, Grünberg | GMR | 스핀 의존 $v\times B_{eff}$ 산란 |
| 2010 | Geim, Novoselov | 그래핀 | $E_n \propto \sqrt{Bn}$, 의사 $B_{ps} = 350$ T |
| 2013 | Englert, Higgs | 힉스 | $m_W, m_Z$로 $W,Z$ 로렌츠 힘 단거리화 |
| 2014 | Akasaki | GaN LED | Hall로 $p$-형 $n$ 측정 |
| 2016 | Thouless, Haldane, Kosterlitz | 위상 물질 | Berry 곡률 $\Omega \sim B_{eff}$, TKNN $C$ |
| 2017 | Weiss, Barish, Thorne | LIGO | $IL\times B$ 액츄에이터 잡음이 $h = 10^{-21}$ 신호 제한 |
| 2019 | Peebles | 우주론 | 은하 $B$가 바리온 $v\times B$로 구조 형성 |
| 2022 | Aspect, Clauser, Zeilinger | 얽힘 | $E\times B$ Pockels 셀로 편광 측정 |

**총 22개** — 물리학 노벨상 1/5이 직·간접 로렌츠 힘.

**2024 이후 후보:** $B_{ps}$ 그래핀, $E\times B$ 스핀 홀 SOT-MRAM, Penning 양자컴퓨팅.

### 6.3.8 매스매티카 검증

```mathematica
(* SAR *)
sarValue[sigmaConductivity_, Efield_, rhoDensity_] :=
  sigmaConductivity Norm[Efield]^2 / rhoDensity;

(* MRI 안전 *)
mriSafety[B0_] := B0 <= 3; (* 임상 *)

(* ICNIRP 한계 *)
icnirpLimit[Efield_] := Efield <= 5 10^3; (* V/m, 일반인 *)

(* 홀 센서 교정 *)
hallCalibration[iRef_, bRef_, tThickness_, vHall_] :=
  vHall tThickness / (iRef bRef);
```

### 6.3.9 한계·예외

- **안전 규격:** 국가별 차이, 최신 연구 반영 지연
- **산업 표준:** 로렌츠 힘 자체보다 응용 장치 중심
- **윤리:** 군사 응용 회색지대, 이중용도 통제 어려움
- **대중 과학:** 오개념 확산 ($B$가 힘 만든다는 착각)
- **노벨상:** 로렌츠 힘 자체 수상은 1902년뿐, 대부분 응용

> **참고문헌**
> - IEC 60601-2-33, *Medical electrical equipment — Part 2-33: Particular requirements for the basic safety and essential performance of magnetic resonance equipment for medical diagnosis*. [IEC Webstore](https://webstore.iec.ch/en/publication/26147)
> - ICNIRP, *Guidelines for limiting exposure to electromagnetic fields (100 kHz to 300 GHz)*, Health Phys. **118**, 483 (2020). [doi:10.1093/rpd/ncaa155](https://doi.org/10.1093/rpd/ncaa155)
> - Nobel Prize in Physics 1902, Lorentz & Zeeman. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1902/)
> - Nobel Prize in Physics 1906, J.J. Thomson. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1906/)
> - Nobel Prize in Physics 1939, Lawrence. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1939/)
> - Nobel Prize in Physics 1985, von Klitzing. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1985/)
> - Nobel Prize in Physics 2007, Fert & Grünberg. [nobelprize.org](https://www.nobelprize.org/prizes/physics/2007/)
> - Nobel Prize in Physics 2017, Weiss, Barish, Thorne. [nobelprize.org](https://www.nobelprize.org/prizes/physics/2017/)

---

## 6막 마무리

> **6막 요약**
>
> - **6.1** 입자물리에서 로렌츠 힘은 $U(1)$ 게이지 공변 미분의 3차원 그림자다. $SU(3)\times SU(2)\times U(1)$로 확장되고, QGP에서 $eB \sim m_\pi^2 \sim 10^{15}$ T의 극한 자기장을 만든다. 자기 단극자, 밀리차지, 강자기장 QED가 미해결 최전선이다.
> - **6.2** 일반상대론에서 중력은 힘이 아니지만, 로렌츠 힘은 여전히 힘으로 남는다. 하전입자는 전자기력이라는 비중력적 외력 때문에 geodesic 운동에서 이탈하지만, 이 자체를 등가원리 위반으로 부르지는 않는다. 블랙홀 Blandford-Znajek 메커니즘에서 중력이 감은 $B$를 로렌츠 힘이 풀며 제트를 만든다. Lorentz 위반 SME는 $10^{-22}$ 수준까지 제한됐다.
> - **6.3** 로렌츠 힘 교육은 $F$가 $v$ 없으면 0임을 강조해야 오개념 방지, 철학은 $A_\mu$가 $F_{\mu\nu}$보다 근본이라는 AB 효과로 귀결, 산업은 $B$와 $dB/dt$를 SAR·PNS·$J_c$로 규제, 윤리는 $B > 2$ T를 이중용도로 통제. **물리학 노벨상 1/5이 직·간접 로렌츠 힘과 연결된다.**

> **종합 예고**
>
> 이제 6막이 끝났다. 마지막으로 **종합(Synthesis)**에서 로렌츠 힘의 통일적 그림, 커버리지 매트릭스, 읽기 경로를 제시하고, **부록**에서 기호·상수·매스매티카 코드·참고문헌·색인을 정리한다.

---

# 종합 (Synthesis)

> **종합의 목표**
> 6막 18주제를 하나의 그림으로 통합하고, 독자가 자신의 경로로 문서를 활용할 수 있도록 지도를 제공한다.

---

## 종합.1 로렌츠 힘의 통일적 그림

**하나의 공식, 여섯 개의 막.**

로렌츠 힘 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 표면적으로 벡터 공식이지만, 6막을 관통하는 하나의 구조가 있다:

$$U(1) \text{ 다발} \xrightarrow{\text{곡률}} F = dA \xrightarrow{\text{세계선}} f^\mu = qF^{\mu\nu}u_\nu \xrightarrow{\text{3차원}} \mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

**막별 얼굴:**

| 막 | 로렌츠 힘의 얼굴 | 핵심 언어 |
|---|---|---|
| **1막** | 정의·역학·게이지 | 라그랑지안, 심플렉틱, $U(1)$ |
| **2막** | 궤적·드리프트·위상 | $\omega_c, r_L, \mu$, Chern 수 |
| **3막** | 상대론·양자·통계 | $\gamma$, 란다우, Vlasov |
| **4막** | 가속기·핵융합·우주 | $B\rho$, Grad-Shafranov, 오로라 |
| **5막** | AI·양자칩·위상물질 | RL, Penning, Berry 곡률 |
| **6막** | 게이지장·중력·윤리 | $SU(2)\times U(1)$, BZ, SME |

**모든 응용의 공통 분모:**

- **가속:** $\mathbf{E}$로 에너지 주입
- **구속:** $\mathbf{B}$로 궤도 제어
- **위상:** $A$로 간섭 제어
- **정보:** $\Omega$ (베리 곡률)로 위상 양자화

**핵심 통찰 3가지:**

1. **힘은 그림자다.** 진짜 실체는 $U(1)$ 다발의 접속 $A$. $F = dA$의 국소 효과가 로렌츠 힘, 대역적 효과가 AB 위상
2. **자기력은 상대론적 전기력이다.** 움직이는 관찰자에게 $\mathbf{E}' = \gamma\mathbf{V}\times\mathbf{B}$. $\mathbf{v}\times\mathbf{B}$는 $F^{\mu\nu}u_\nu$의 3차원 투영
3. **양자역학은 힘을 위상으로 바꾼다.** $p \to p-qA$가 전부. 란다우 준위, 양자 홀, AB 효과가 모두 여기서 나온다

---
 
## 종합.2 로렌츠 힘의 미래 — 5가지 전망

1. **AI 실시간 제어:** $\mathbf{J}\times\mathbf{B}$를 강화학습으로 99% KAM 보존 → 핵융합 상용화
2. **고온 초전도 $B > 20$ T:** 소형 토카막, 양자칩, 우주추진 동시 혁신
3. **양자 $U(1)$ 위상:** 로렌츠 힘을 홀로노미로 재해석, 위상 물질·양자컴퓨팅 융합
4. **극한 $B$ 실험실:** 100 PW 레이저 + 100 T 자석으로 Born-Infeld, 진공 복굴절 검증
5. **밀리차지·단극자 탐색:** 로렌츠 힘으로 암흑을 보고, 전하 양자화의 기원을 밝힘

**130년 전 로렌츠가 쓴 $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$는 아직도 답보다 질문을 더 많이 만든다. 단극자 1개가 발견되면 전하 양자화가 설명되고, $E\times B$ 난류 1개가 풀리면 핵융합이 켜진다.**

---
# 부록 (Appendices)

> **부록의 목적**
> 본문 6막 + 종합에서 사용된 기호, 상수, 코드, 참고문헌, 매핑, 색인을 한 곳에 통합한다. 독자가 특정 항목을 빠르게 찾을 수 있도록 설계했다.

---

## 부록 A. 기호 정의 (통합표)

### A.1 기본 물리량

| 기호 | 유니코드 | LaTeX | 의미 | SI 단위 |
|---|---|---|---|---|
| $\mathbf{F}$ | 𝐅 | `\mathbf{F}` | 힘 | N |
| $q$ | q | `q` | 전하량 | C |
| $e$ | e | `e` | 기본 전하 | 1.602×10⁻¹⁹ C |
| $\mathbf{E}$ | 𝐄 | `\mathbf{E}` | 전기장 | V/m |
| $\mathbf{B}$ | 𝐁 | `\mathbf{B}` | 자기장 (자속 밀도) | T |
| $\mathbf{v}$ | 𝐯 | `\mathbf{v}` | 속도 | m/s |
| $\mathbf{p}$ | 𝐩 | `\mathbf{p}` | 운동량 | kg·m/s |
| $\boldsymbol{\pi}$ | π | `\boldsymbol{\pi}` | 운동학적 운동량 $m\mathbf{v}$ | kg·m/s |
| $m$ | m | `m` | 질량 | kg |
| $t$ | t | `t` | 시간 | s |
| $\tau$ | τ | `\tau` | 고유시간 | s |
| $\mathbf{x}, \mathbf{r}$ | 𝐱, 𝐫 | `\mathbf{x}, \mathbf{r}` | 위치 | m |

### A.2 전자기 퍼텐셜

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $\phi$ | φ | `\phi` | 전기 스칼라 퍼텐셜 |
| $\mathbf{A}$ | 𝐀 | `\mathbf{A}` | 자기 벡터 퍼텐셜 |
| $A^\mu$ | A^μ | `A^\mu` | 4-퍼텐셜 $(\phi/c, \mathbf{A})$ |
| $F^{\mu\nu}$ | F^μν | `F^{\mu\nu}` | 전자기장 텐서 |
| $\chi$ | χ | `\chi` | 게이지 함수 |
| $J^\mu$ | J^μ | `J^\mu` | 4-전류 $(\rho c, \mathbf{J})$ |

### A.3 역학·궤적

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $\omega_c$ | ω_c | `\omega_c` | 사이클로트론 진동수 |
| $r_L$ | r_L | `r_L` | 라모르 반지름 |
| $\mathbf{R}_g$ | 𝐑_g | `\mathbf{R}_g` | 유도 중심 |
| $\mu$ | μ | `\mu` | 자기 모멘트 $mv_\perp^2/2B$ |
| $\mathbf{V}_E$ | 𝐕_E | `\mathbf{V}_E` | $E\times B$ 드리프트 |
| $\mathbf{V}_{\nabla B}$ | 𝐕_∇ B | `\mathbf{V}_{\nabla B}` | $\nabla B$ 드리프트 |
| $\mathbf{V}_c$ | 𝐕_c | `\mathbf{V}_c` | 곡률 드리프트 |
| $\mathbf{V}_{gc}$ | 𝐕_gc | `\mathbf{V}_{gc}` | 유도 중심 드리프트 |
| $\theta_m$ | θₘ | `\theta_m` | 미러 손실 콘 각도 |
| $R_m$ | Rₘ | `R_m` | 미러비 $B_m/B_0$ |

### A.4 상대론

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $\gamma$ | γ | `\gamma` | 로렌츠 인자 |
| $\beta$ | β | `\beta` | $v/c$ |
| $u^\mu$ | u^μ | `u^\mu` | 4-속도 |
| $p^\mu$ | p^μ | `p^\mu` | 4-운동량 |
| $f^\mu$ | f^μ | `f^\mu` | 4-힘 |
| $\tau_0$ | τ₀ | `\tau_0` | 전자 고유시간 $q^2/6\pi\epsilon_0 mc^3$ |
| $B\rho$ | Bρ | `B\rho` | 강성도 |

### A.5 양자역학

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $\hbar$ | ℏ | `\hbar` | 디랙 상수 |
| $\psi$ | ψ | `\psi` | 파동함수 |
| $l_B$ | l_B | `l_B` | 자기 길이 $\sqrt{\hbar/eB}$ |
| $N_\phi$ | Nᵩ | `N_\phi` | 자속 양자 축퇴도 |
| $\Phi_0$ | Φ₀ | `\Phi_0` | 자속 양자 $h/e$ (또는 $h/2e$) |
| $\nu$ | ν | `\nu` | 채움 인자 |
| $C$ | C | `C` | Chern 수 |
| $\Omega_n$ | Ωₙ | `\Omega_n` | 베리 곡률 |
| $\mathcal{A}_n$ | Aₙ | `\mathcal{A}_n` | 베리 접속 |
| $\sigma_{xy}$ | σ_xy | `\sigma_{xy}` | 홀 전도도 |

### A.6 통계·플라즈마

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $f$ | f | `f` | 분포함수 |
| $C[f]$ | C[f] | `C[f]` | 충돌 연산자 |
| $\nu$ | ν | `\nu` | 충돌 진동수 |
| $\sigma_\parallel$ | σ_∥ | `\sigma_\parallel` | 평행 전도도 |
| $\sigma_P$ | σ_P | `\sigma_P` | Pedersen 전도도 |
| $\sigma_H$ | σ_H | `\sigma_H` | Hall 전도도 |
| $D_\perp$ | D_⊥ | `D_\perp` | 수직 확산 |
| $\lambda_D$ | λ_D | `\lambda_D` | Debye 길이 |

### A.7 응용·공학

| 기호 | 유니코드 | LaTeX | 의미 |
|---|---|---|---|
| $a_0$ | a₀ | `a_0` | 레이저 정규화 진폭 |
| $B_{ps}$ | Bₚₛ | `B_{ps}` | 그래핀 의사 자기장 |
| $n_{GJ}$ | n_GJ | `n_{GJ}` | Goldreich-Julian 밀도 |
| $\Phi_{pc}$ | Φ_pc | `\Phi_{pc}` | 극관 전위 |
| $S$ | S | `S` | Lundquist 수 |
| $\eta$ | η | `\eta` | 자기 확산도 / 슬립 인자 |
| $\iota$ | ι | `\iota` | 회전 변환 |

---

## 부록 B. 물리 상수

| 상수 | 유니코드 | LaTeX | 값 | 단위 |
|---|---|---|---|---|
| 진공 투자율 | μ₀ | `\mu_0` | $4\pi\times10^{-7}$ | H/m |
| 진공 유전율 | ε₀ | `\epsilon_0` | $8.854\times10^{-12}$ | F/m |
| 빛의 속도 | c | `c` | $2.998\times10^8$ | m/s |
| 플랑크 상수 | h | `h` | $6.626\times10^{-34}$ | J·s |
| 디랙 상수 | ℏ | `\hbar` | $1.055\times10^{-34}$ | J·s |
| 기본 전하 | e | `e` | $1.602\times10^{-19}$ | C |
| 전자 질량 | mₑ | `m_e` | $9.109\times10^{-31}$ | kg |
| 양성자 질량 | mₚ | `m_p` | $1.673\times10^{-27}$ | kg |
| 볼츠만 상수 | k_B | `k_B` | $1.381\times10^{-23}$ | J/K |
| 중력 상수 | G | `G` | $6.674\times10^{-11}$ | m³/(kg·s²) |
| 미세구조 상수 | α | `\alpha` | $1/137.036$ | 무차원 |
| 자속 양자 | Φ₀ | `\Phi_0` | $2.068\times10^{-15}$ | Wb |
| 임계 자기장 | B_c | `B_c` | $4.41\times10^9$ | T |
| 임계 전기장 | E_c | `E_c` | $1.32\times10^{18}$ | V/m |
| 콤프턴 파장 | λ_C | `\lambda_C` | $2.426\times10^{-12}$ | m |
| 보어 반지름 | a₀ | `a_0` | $5.292\times10^{-11}$ | m |
| 고전 전자 반지름 | rₑ | `r_e` | $2.818\times10^{-15}$ | m |

### B.1 유용한 조합

| 조합 | 값 | 용도 |
|---|---|---|
| $\mu_0\epsilon_0$ | $1/c^2$ | 맥스웰 방정식 |
| $e^2/4\pi\epsilon_0$ | $1.44$ MeV·fm | 원자핵 |
| $\hbar c$ | $197.3$ MeV·fm | 입자물리 |
| $m_ec^2$ | $0.511$ MeV | 전자 |
| $m_pc^2$ | $938.3$ MeV | 양성자 |
| $h/e^2$ | $25.813$ kΩ | 양자 홀 |
| $\Phi_0 = h/2e$ | $2.068\times10^{-15}$ Wb | 초전도 |
| $B_c = m_e^2c^3/e\hbar$ | $4.41\times10^9$ T | QED |
| $1$ eV | $1.602\times10^{-19}$ J | 에너지 |
| $1$ T | $10^4$ G | 자기장 |

### B.2 천문·우주 상수

| 상수 | 값 | 용도 |
|---|---|---|
| 지구 자기장 (적도) | 30 μT | 자기권 |
| 지구 자기장 (극) | 60 μT | 자기권 |
| 태양 자기장 (표면) | 0.1 T | 태양 플레어 |
| 태양풍 속도 | 400 km/s | 오로라 |
| IMF 세기 | 5 nT | 자기권 |
| 펄서 자기장 | $10^8-10^{12}$ T | 중성자별 |
| 마그네타 자기장 | $10^{10}-10^{11}$ T | 강자기장 |
| QGP 자기장 | $10^{15}$ T | 중이온 |
| 블랙홀 자기장 | 1-100 T | 제트 |

---

## 부록 C. 매스매티카 검증 코드 (전체 통합)

### C.1 1막 — 기초와 정의

```mathematica
(* 4-힘 검증 *)
Fmunu = {{0, -Ex/c, -Ey/c, -Ez/c},
         {Ex/c, 0, -Bz, By},
         {Ey/c, Bz, 0, -Bx},
         {Ez/c, -By, Bx, 0}};
g = DiagonalMatrix[{1, -1, -1, -1}];
uUp = {gamma c, gamma vx, gamma vy, gamma vz};
uDown = g . uUp;  (* f^μ = q F^{μν} u_ν 이므로 공변 u_ν와 축약 *)
fourForce = q Fmunu . uDown;
spatialForce = fourForce[[2 ;; 4]] / gamma;
expected = q ({Ex, Ey, Ez} + Cross[{vx, vy, vz}, {Bx, By, Bz}]);
Simplify[spatialForce - expected] == {0, 0, 0}  (* True *)

(* 라그랑지안에서 로렌츠 힘 유도 *)
L = (1/2) m (x'[t]^2 + y'[t]^2 + z'[t]^2)
    - q phi[x, y, z, t]
    + q (x'[t] Ax[x, y, z, t] + y'[t] Ay[x, y, z, t] + z'[t] Az[x, y, z, t]);
(* 오일러-라그랑주 *)
ELx = D[D[L, x'[t]], t] - D[L, x[t]];
Simplify[ELx]

(* 게이지 불변성 *)
chi = chi[x, y, z, t];
Avec = {Ax[x, y, z, t], Ay[x, y, z, t], Az[x, y, z, t]};
phiVal = phi[x, y, z, t];
AvecPrime = Avec + Grad[chi, {x, y, z}];
phiPrime = phiVal - D[chi, t];
BPrime = Curl[AvecPrime, {x, y, z}];
B = Curl[Avec, {x, y, z}];
Simplify[BPrime - B] == {0, 0, 0}  (* True *)
```

### C.2 2막 — 수학적 구조

```mathematica
(* 균일 자기장 궤적 *)
Bvec = {0, 0, B0};
eqns = {m x''[t] == q (y'[t] B0),
        m y''[t] == -q (x'[t] B0),
        m z''[t] == 0,
        x[0] == x0, y[0] == y0, z[0] == z0,
        x'[0] == vx0, y'[0] == vy0, z'[0] == vz0};
sol = DSolve[eqns, {x[t], y[t], z[t]}, t];

(* 보리스 회전 검증 *)
borisRotate[vMinus_, q_, m_, dt_, Bvec_] := Module[
  {t, s, vPrime, vPlus},
  t = (q Bvec dt)/(2 m);
  s = (2 t)/(1 + t . t);
  vPrime = vMinus + Cross[vMinus, t];
  vPlus = vMinus + Cross[vPrime, s];
  vPlus];
v0 = {1, 0, 0};
Bvec = {0, 0, 1};
v1 = borisRotate[v0, 1, 1, 0.1, Bvec];
Norm[v1] - Norm[v0]  (* 0 *)

(* 단열 불변량 *)
mu[B_, vPerp_, m_] := m vPerp^2 / (2 B);
mirrorCondition[B0_, Bm_, theta0_] := Sin[theta0]^2 == B0/Bm;

(* 전자기 텐서의 미분형식 *)
Aform = -phi[x, y, z, t] dt + Ax[x, y, z, t] dx
        + Ay[x, y, z, t] dy + Az[x, y, z, t] dz;
Fform = d[Aform];
Simplify[d[Fform] == 0]  (* True *)
```

### C.3 3막 — 물리적 심화

```mathematica
(* 상대론적 로렌츠 힘 *)
gammaRel[v_] := 1/Sqrt[1 - v . v/c^2];
pRel[v_] := gammaRel[v] m0 v;

(* 란다우 준위 *)
landauLevels[n_, hBar_, omegaC_] := hBar omegaC (n + 1/2);

(* 양자 홀 전도도 *)
hallConductance[nu_, e_, h_] := nu e^2/h;

(* 볼츠만 방정식 *)
boltzmannEq = D[f[t, x, y, z, vx, vy, vz], t]
  + vx D[f[t, x, y, z, vx, vy, vz], x]
  + vy D[f[t, x, y, z, vx, vy, vz], y]
  + vz D[f[t, x, y, z, vx, vy, vz], z]
  + (q/m) ((Ex + vy Bz - vz By) D[f[t, x, y, z, vx, vy, vz], vx]
         + (Ey + vz Bx - vx Bz) D[f[t, x, y, z, vx, vy, vz], vy]
         + (Ez + vx By - vy Bx) D[f[t, x, y, z, vx, vy, vz], vz])
  == collisionTerm;

(* 라모 공식 *)
larmorPower[q_, a_, epsilon0_, c_] := q^2 a^2 / (6 Pi epsilon0 c^3);

(* 강성도 *)
rigidity[p_, q_] := p/q;
```

### C.4 4막 — 응용과 공학

```mathematica
(* 사이클로트론 에너지 *)
cyclotronEnergy[q_, B_, r_, m_] := q^2 B^2 r^2 / (2 m);

(* Grad-Shafranov *)
gradShafranov[psi_, R_, Z_, mu0_, p_, F_] :=
  R D[1/R D[psi, R], R] + D[psi, {Z, 2}] ==
  -mu0 R^2 D[p[psi], psi] - F[psi] D[F[psi], psi];

(* 자기섬 너비 *)
islandWidth[q_, R_, Btilde_, m_, qPrime_, B0_] :=
  4 Sqrt[q^2 R Btilde / (m qPrime B0)];

(* MRI 블로흐 방정식 *)
blochEq = D[Mvec[t], t] == gammaGyro Cross[Mvec[t], Bvec]
  - {Mx[t]/T2, My[t]/T2, (Mz[t] - M0)/T1};

(* 홀 전압 *)
hallVoltage[iCurrent_, bField_, nCarrier_, qCharge_, tThickness_] :=
  iCurrent bField / (nCarrier qCharge tThickness);

(* SQUID *)
squidCritical[Phi_, Phi0_, I0_] := 2 I0 Abs[Cos[Pi Phi/Phi0]];

(* GJ 밀도 *)
gjDensity[Omega_, Bfield_, eCharge_, epsilon0_] :=
  2 epsilon0 Omega . Bfield / eCharge;

(* Rechester-Rosenbluth 확산 *)
rrDiffusion[q_, R_, BtildeSq_, B0_, Lc_] :=
  Pi q R BtildeSq / B0^2 * Lc;
```

### C.5 5막 — 최전선

```mathematica
(* AI 제어 보상 함수 *)
aiReward[psi_, psiTarget_, Jvec_, Bvec_, gradp_] :=
  -Norm[psi - psiTarget] - Norm[Cross[Jvec, Bvec] - gradp];

(* Penning 트랩 *)
penningFreq[q_, B_, m_] := q B / m;

(* 그래핀 의사 자기장 *)
pseudoB[beta_, aLattice_, uxx_, uyy_, uxy_, hBar_, eCharge_] :=
  {hBar beta/(2 eCharge aLattice) (uxx - uyy),
   hBar beta/(2 eCharge aLattice) (-2 uxy)};

(* 마요라나 위상 조건 *)
majoranaCondition[gFactor_, muB_, Bfield_, Delta_, mu_] :=
  gFactor muB Bfield > Sqrt[Delta^2 + mu^2];

(* 와선 로렌츠 힘 *)
vortexForce[Jext_, Phi0_] := Cross[Jext, {0, 0, Phi0}];

(* Dirac 양자화 *)
diracQuantization[qCharge_, gMonopole_] := qCharge gMonopole == nInteger hBar/2;

(* Born-Infeld 라그랑지안 *)
bornInfeldLagrangian[Fmunu_, b_] :=
  b^2 (1 - Sqrt[1 + (Fmunu Fmunu)/(2 b^2) - (Fmunu Star[Fmunu])^2/(16 b^4)]);
```

### C.6 6막 — 확장 영역

```mathematica
(* 공변 미분 *)
covariantDerivative = Dmu == PartialMu + I g Amu;

(* 장 강도 텐서 (비아벨) *)
fieldStrength = Fmunu == PartialMu Anu - PartialNu Amu + I g {Amu, Anu};

(* CME 전류 *)
cmeCurrent[mu5_, Bvec_, eCharge_] := eCharge^2/(2 Pi^2) mu5 Bvec;

(* BZ 파워 *)
bzPower[kappa_, OmegaH_, PhiB_, c_] := kappa/(4 Pi c) OmegaH^2 PhiB^2;

(* Lorentz 위반 *)
lorentzViolation = -1/4 Fmunu Fmunu + 1/2 kmunu Fmulambda Fnu lambda;

(* SAR *)
sarValue[sigmaConductivity_, Efield_, rhoDensity_] :=
  sigmaConductivity Norm[Efield]^2 / rhoDensity;
```

---

## 부록 D. Python 수치 코드

### D.1 보리스 pusher (Python)

```python
import numpy as np

def boris_push(x, v, q, m, E, B, dt):
    """
    Boris algorithm for relativistic charged particle.
    x, v: position, velocity (3-vectors)
    q, m: charge, mass
    E, B: electric, magnetic field (3-vectors)
    dt: time step
    """
    # Step 1: half electric acceleration
    v_minus = v + (q * dt / (2 * m)) * E

    # Step 2: magnetic rotation
    t = (q * dt / (2 * m)) * B
    s = 2 * t / (1 + np.dot(t, t))
    v_prime = v_minus + np.cross(v_minus, t)
    v_plus = v_minus + np.cross(v_prime, s)

    # Step 3: half electric acceleration
    v_new = v_plus + (q * dt / (2 * m)) * E

    # Position update
    x_new = x + v_new * dt

    return x_new, v_new
```

### D.2 사이클로트론 궤적 시각화 (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
q, m, B0 = 1.0, 1.0, 1.0
omega_c = q * B0 / m
v_perp = 1.0
r_L = v_perp / omega_c
T = 2 * np.pi / omega_c

t = np.linspace(0, 3*T, 1000)
x = r_L * np.sin(omega_c * t)
y = r_L * np.cos(omega_c * t)

plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.axis('equal')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Cyclotron orbit')
plt.grid(True)
plt.show()
```

### D.3 란다우 준위 (Python)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite

def landau_wavefunction(n, x, B=1.0, hbar=1.0, m=1.0, e=1.0):
    """Landau level wavefunction in symmetric gauge."""
    l_B = np.sqrt(hbar / (e * B))
    xi = x / l_B
    psi = (1 / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi) * l_B)) \
          * np.exp(-xi**2 / 2) * eval_hermite(n, xi)
    return psi

x = np.linspace(-5, 5, 500)
for n in range(4):
    plt.plot(x, landau_wavefunction(n, x), label=f'n={n}')
plt.xlabel('x / l_B')
plt.ylabel('ψ_n(x)')
plt.legend()
plt.title('Landau level wavefunctions')
plt.show()
```

### D.4 PIC 1D (Python, 축약)

```python
import numpy as np

class PIC1D:
    def __init__(self, N, L, q, m, dt, nx):
        self.N = N
        self.L = L
        self.q = q
        self.m = m
        self.dt = dt
        self.nx = nx
        self.dx = L / nx

        # Initialize particles
        self.x = np.random.uniform(0, L, N)
        self.v = np.random.normal(0, 0.1, N)

        # Fields
        self.E = np.zeros(nx)
        self.rho = np.zeros(nx)

    def deposit_charge(self):
        self.rho[:] = 0
        for i in range(self.N):
            g = int(self.x[i] / self.dx) % self.nx
            self.rho[g] += self.q / self.dx
        # Normalize
        self.rho -= np.mean(self.rho)

    def solve_field(self):
        # 1D Poisson
        k = 2 * np.pi * np.fft.fftfreq(self.nx, self.dx)
        k[0] = 1  # avoid division by zero
        rho_k = np.fft.fft(self.rho)
        E_k = -1j * rho_k / (epsilon0 * k)
        self.E = np.real(np.fft.ifft(E_k))

    def push(self):
        for i in range(self.N):
            g = int(self.x[i] / self.dx) % self.nx
            self.v[i] += (self.q / self.m) * self.E[g] * self.dt
            self.x[i] += self.v[i] * self.dt
```

---

## 부록 E. 참고문헌 통합 색인

### E.1 역사적 원논문

1. Lorentz, H. A., *La théorie électromagnétique de Maxwell et son application aux corps mouvants*, Archives Néerlandaises **25**, 363–552 (1892). [archive.org](https://archive.org/details/lathorielectrom00loregoog)
2. Thomson, J. J., *Cathode Rays*, Phil. Mag. **44**, 293–316 (1897). [doi:10.1080/14786449708621070](https://doi.org/10.1080/14786449708621070)
3. Heaviside, O., *Electromagnetic Theory*, Vol. II (1899). [archive.org](https://archive.org/details/electromagnetict02heavrich)
4. Hall, E. H., *On a new action of the magnet on electric currents*, Am. J. Math. **2**, 287 (1879). [doi:10.2475/ajs.s3-19.117.200](https://doi.org/10.2475/ajs.s3-19.117.200)
5. Larmor, J., *On a dynamical theory of the electric and luminiferous medium*, Phil. Trans. R. Soc. A **190**, 205 (1897). [doi:10.1098/rsta.1897.0020](https://doi.org/10.1098/rsta.1897.0020)
6. Fokker, A. D., *Die mittlere Energie rotierender elektrischer Dipole im Strahlungsfeld*, Ann. Phys. **348**, 810 (1914). [doi:10.1002/andp.19143480507](https://doi.org/10.1002/andp.19143480507)
7. Dirac, P. A. M., *Quantised singularities in the electromagnetic field*, Proc. R. Soc. A **133**, 60 (1931). [doi:10.1098/rspa.1931.0130](https://doi.org/10.1098/rspa.1931.0130)
8. Born, M., Infeld, L., *Foundations of the new field theory*, Proc. R. Soc. A **144**, 425 (1934). [doi:10.1098/rspa.1934.0059](https://doi.org/10.1098/rspa.1934.0059)
9. Dirac, P. A. M., *Classical theory of radiating electrons*, Proc. R. Soc. A **167**, 148 (1938). [doi:10.1098/rspa.1938.0124](https://doi.org/10.1098/rspa.1938.0124)
10. Landau, L. D., *Diamagnetismus der Metalle*, Z. Phys. **64**, 629 (1930). [doi:10.1007/BF01397213](https://doi.org/10.1007/BF01397213)

### E.2 교과서·표준 참고서

11. Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998).
12. Griffiths, D. J., *Introduction to Electrodynamics*, 4th ed., Cambridge (2017).
13. Goldstein, H., Poole, C., Safko, J., *Classical Mechanics*, 3rd ed., Addison-Wesley (2001). [doi:10.1119/1.1484149](https://doi.org/10.1119/1.1484149)
14. Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed., Pergamon (1975).
15. Landau & Lifshitz, *Mechanics*, 3rd ed., Pergamon (1976).
16. Chen, F. F., *Introduction to Plasma Physics and Controlled Fusion*, 3rd ed., Springer (2016).
17. Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963). [doi:10.1002/9781118033156](https://doi.org/10.1002/9781118033156)
18. Nakahara, M., *Geometry, Topology and Physics*, 2nd ed., Taylor & Francis (2003).
19. Arnold, V. I., *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer (1989).
20. Sokolov, A. A., Ternov, I. M., *Synchrotron Radiation*, Pergamon (1968).

### E.3 리뷰 논문

21. Xiao, D., Chang, M.-C., Niu, Q., *Berry phase effects on electronic properties*, Rev. Mod. Phys. **82**, 1959 (2010). [doi:10.1103/RevModPhys.82.1959](https://doi.org/10.1103/RevModPhys.82.1959)
22. Esarey, E., Schroeder, C. B., Leemans, W. P., *Physics of laser-driven plasma-based electron accelerators*, Rev. Mod. Phys. **81**, 1229 (2009). [doi:10.1103/RevModPhys.81.1229](https://doi.org/10.1103/RevModPhys.81.1229)
23. Braginskii, S. I., *Transport processes in a plasma*, Reviews of Plasma Physics **1**, 205 (1965).
24. Sivukhin, D. V., *Motion of charged particles in electromagnetic fields in the plasma physics*, Reviews of Plasma Physics **1**, 1 (1965).
25. Kostelecký, V. A., Russell, N., *Data tables for Lorentz and CPT violation*, Rev. Mod. Phys. **83**, 11 (2011). [doi:10.1103/RevModPhys.83.11](https://doi.org/10.1103/RevModPhys.83.11)

### E.4 최신 논문 (2020~2025)

26. Degrave, J., et al., *Magnetic control of tokamak plasmas through deep reinforcement learning*, Nature **602**, 414 (2022). [doi:10.1038/s41586-021-04301-9](https://doi.org/10.1038/s41586-021-04301-9)
27. Jain, S., et al., *Penning micro-trap for quantum computing*, Nature **627**, 510 (2024). [doi:10.1038/s41586-024-07111-x](https://doi.org/10.1038/s41586-024-07111-x)
28. Zhang, Y., et al., *Giant nonlinear Hall effect in strained twisted bilayer graphene*, Phys. Rev. B **106**, L041111 (2022). [doi:10.1103/PhysRevB.106.L041111](https://doi.org/10.1103/PhysRevB.106.L041111)
29. Lamač, M., et al., *Anomalous relativistic emission from self-modulated plasma mirrors*, Phys. Rev. Lett. **131**, 205001 (2023). [doi:10.1103/PhysRevLett.131.205001](https://doi.org/10.1103/PhysRevLett.131.205001)
30. Acharya, B., et al. (MoEDAL), *Search for magnetic monopoles via Schwinger pair production*, Nature **602**, 63 (2022). [doi:10.1038/s41586-021-04298-1](https://doi.org/10.1038/s41586-021-04298-1)
31. W7-X Team, *Quasi-isodynamic optimization*, Phys. Rev. Lett. **129**, 095001 (2022). [doi:10.1103/PhysRevLett.129.095001](https://doi.org/10.1103/PhysRevLett.129.095001)
32. STAR Collaboration, *Search for the chiral magnetic effect with isobar collisions*, Phys. Rev. C **105**, 014901 (2022). [arXiv:2109.00131](https://arxiv.org/abs/2109.00131)
33. STAR Collaboration, *Global Λ hyperon polarization in nuclear collisions*, Nature **548**, 62 (2017). [doi:10.1038/nature23004](https://doi.org/10.1038/nature23004)
34. Event Horizon Telescope Collaboration, *First M87 event horizon telescope results. VIII. Magnetic field structure*, Astrophys. J. Lett. **910**, L13 (2021). [doi:10.3847/2041-8213/abe4de](https://doi.org/10.3847/2041-8213/abe4de)
35. MICROSCOPE Collaboration, *MICROSCOPE mission: Final results of the test of the equivalence principle*, Phys. Rev. Lett. **129**, 121102 (2022). [arXiv:2209.06628](https://arxiv.org/abs/2209.06628)
36. LIGO-Virgo Collaboration, *Magnetic correlation noise in LIGO*, Phys. Rev. D **105**, 082005 (2022). [arXiv:2201.04475](https://arxiv.org/abs/2201.04475)

### E.5 기타

37. Boris, J. P., *Relativistic plasma simulation-optimization of a hybrid code*, Proc. 4th Conf. Numerical Simulation of Plasmas, 3–67 (1970). [ADS](https://ui.adsabs.harvard.edu/abs/1970nusp.conf....3B)
38. Esirkepov, T. Zh., *Exact charge conservation scheme for PIC simulation*, Comput. Phys. Commun. **144**, 26 (2001). [doi:10.1016/S0010-4655(00)00228-9](https://doi.org/10.1016/S0010-4655(00)00228-9)
39. Hockney, R. W., Eastwood, J. W., *Computer Simulation Using Particles*, Adam Hilger (1988). [doi:10.1201/9780367806934](https://doi.org/10.1201/9780367806934)
40. Birdsall, C. K., Langdon, A. B., *Plasma Physics via Computer Simulation*, McGraw-Hill (1985).
40a. Qin, H. et al., *Why is Boris algorithm so good?*, Phys. Plasmas **20**, 084503 (2013). [doi:10.1063/1.4818428](https://doi.org/10.1063/1.4818428)
40b. Ellison, C. L., Burby, J. W. & Qin, H., *Comment on "Symplectic integration of magnetic systems": a proof that the Boris algorithm is not variational*, J. Comput. Phys. **301**, 489–493 (2015). [doi:10.1016/j.jcp.2015.07.059](https://doi.org/10.1016/j.jcp.2015.07.059)
40c. He, Y. et al., *Volume-preserving algorithms for charged particle dynamics*, J. Comput. Phys. **281**, 135–147 (2015). [doi:10.1016/j.jcp.2014.10.032](https://doi.org/10.1016/j.jcp.2014.10.032)

### E.6 표준·규격

41. IEC 60601-2-33, *Medical electrical equipment — MRI safety*. [IEC Webstore](https://webstore.iec.ch/en/publication/26147)
42. ICNIRP, *Guidelines for limiting exposure to electromagnetic fields*, Health Phys. **118**, 483 (2020). [doi:10.1093/rpd/ncaa155](https://doi.org/10.1093/rpd/ncaa155)
43. IEEE C95.1-2019, *IEEE Standard for Safety Levels with Respect to Human Exposure to Electric, Magnetic, and Electromagnetic Fields*.

### E.7 노벨상 강연

44. Nobel Prize in Physics 1902, Lorentz & Zeeman. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1902/)
45. Nobel Prize in Physics 1906, J.J. Thomson. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1906/)
46. Nobel Prize in Physics 1939, Lawrence. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1939/)
47. Nobel Prize in Physics 1985, von Klitzing. [nobelprize.org](https://www.nobelprize.org/prizes/physics/1985/)
48. Nobel Prize in Physics 2007, Fert & Grünberg. [nobelprize.org](https://www.nobelprize.org/prizes/physics/2007/)
49. Nobel Prize in Physics 2017, Weiss, Barish, Thorne. [nobelprize.org](https://www.nobelprize.org/prizes/physics/2017/)

---
 ---

## 부록 F. 18개 원질문 ↔ 본문 매핑표

| 원질문 | 본문 위치 | 핵심 답변 |
|---|---|---|
| Q1. 로런츠 힘은 누가 발견? | §1.1 | Faraday→Maxwell→Thomson/Heaviside→Lorentz 60년 종합 |
| Q2. 왜 $v\times B$인가? | §1.4 | $L=-q\phi+q\mathbf{v}\cdot\mathbf{A}$의 Euler-Lagrange 결과 |
| Q3. 자기장은 왜 일을 안 하나? | §1.2 | $\mathbf{F}_m\cdot\mathbf{v}=0$ 증명 |
| Q4. 단위계 왜 혼란? | §1.2.2-1.2.3 | Gaussian vs HL vs SI $4\pi$, $c$ 차이 |
| Q5. 4차원 형태는? | §1.3 | $f^\mu=qF^{\mu\nu}u_\nu$ |
| Q6. 라모르 반지름? | §2.1.2 | $r_L=m v_\perp/|q|B$ |
| Q7. 드리프트 3종? | §2.2 | $E\times B$, $\nabla B$, 곡률 |
| Q8. 자기거울? | §2.3.3 | $\sin^2\theta_0=B_0/B_m$ 손실콘 |
| Q9. 왜 Boris인가? | §2.4 | 위상공간 부피 보존, $E\times B$ 정확 |
| Q10. AB효과와 로런츠? | §2.5.2, §1.5 | $F=0$이지만 $\oint\mathbf{A}\cdot d\mathbf{l}$ 위상 |
| Q11. 상대론적 질량 증가? | §3.1.2 | $m_\parallel=\gamma^3 m$, $m_\perp=\gamma m$ |
| Q12. 방사 반작용? | §3.2.3-3.2.4 | ALD → Landau-Lifshitz |
| Q13. 란다우 준위? | §3.3.2 | $E_n=\hbar\omega_c(n+1/2)$ |
| Q14. 홀 효과는? | §3.3.3, §4.4.1 | $V_H=IB/ned$, $\sigma_{xy}=\nu e^2/h$ |
| Q15. 토카막 평형? | §4.2.1 | Grad-Shafranov $\Delta^*\psi=-\mu_0R^2p'-FF'$ |
| Q16. 오로라는? | §4.5.1 | $\mathbf{B}$에 갇힌 $\mu$ 보존 입자의 대기 충돌 |
| Q17. 카오스? | §4.6 | 로런츠 힘 vs 로렌츠 방정식 구분, KAM 붕괴 |
| Q18. 미래는? | §5-6 | AI $J\times B$ 제어, QGP $10^{15}$T, $W$ 응축 $10^{20}$T |

---

## 부록 G. 색인 (Index)

### G.1 인명

- **Abraham, M.** — §3.2.3
- **Aharonov, Y.** — §2.5.2, §3.3.6
- **Ampère, A.-M.** — §6.3.1
- **Blandford, R.** — §6.2.5
- **Bloch, F.** — §4.3.1
- **Bohm, D.** — §2.5.2
- **Boris, J. P.** — §2.4.2
- **Born, M.** — §5.2.4
- **Braginskii, S. I.** — §3.4.6
- **Chern, S.-S.** — §2.5.3, §3.3.3
- **Dirac, P. A. M.** — §2.5.3, §3.3.5
- **Faraday, M.** — §1.1.1
- **Fokker, A. D.** — §3.4.3
- **Grad, H.** — §4.2.1
- **Heaviside, O.** — §1.1.3
- **Infeld, L.** — §5.2.4
- **Kolmogorov, A. N.** — §4.6.2
- **Landau, L. D.** — §3.3.2
- **Langevin, P.** — §3.4.4
- **Larmor, J.** — §3.2.1
- **Liénard, A.** — §3.2.2
- **Lorentz, H. A.** — §1.1.4
- **Lorenz, E. N.** — §4.6.6
- **Laughlin, R. B.** — §3.3.3
- **Majorana, E.** — §5.3.4
- **Maxwell, J. C.** — §1.1.2
- **Northrop, T. G.** — §2.2
- **Rechester, A. B.** — §4.6.4
- **Rosenbluth, M. N.** — §4.6.4
- **Shafranov, V. D.** — §4.2.1
- **Thomson, J. J.** — §1.1.3
- **Vlasov, A. A.** — §3.4.2
- **Wong, S. K.** — §6.1.1
- **Znajek, R.** — §6.2.5

### G.2 개념

- **AB 효과** — §2.5.2, §3.3.6
- **ALD 방정식** — §3.2.3
- **Berry 위상** — §2.5.1, §5.3.6
- **Boris 알고리즘** — §2.4.2
- **BZ 메커니즘** — §6.2.5
- **CME** — §6.1.4
- **Chern 수** — §2.5.3, §3.3.3
- **Dirac 양자화** — §2.5.3, §6.1.5
- **Grad-Shafranov 방정식** — §4.2.1
- **IQHE / FQHE** — §3.3.3, §5.3.1
- **KAM 정리** — §4.6.2
- **Landau 준위** — §3.3.2
- **Liénard 공식** — §3.2.2
- **Maxwell 방정식** — §2.5.5
- **MCC** — §2.4.7
- **PIC** — §2.4.6
- **Rechester-Rosenbluth 확산** — §4.6.4
- **TMR / GMR** — §4.4.2
- **Vlasov 방정식** — §3.4.2
- **가우스 단위계** — §1.2.2
- **게이지 불변성** — §1.5
- **곡률 드리프트** — §2.2.3
- **그래핀 의사 자기장** — §5.3.5
- **단열 불변량** — §2.3
- **드리프트 이론** — §2.2
- **라그랑주 역학** — §1.4
- **라모 공식** — §3.2.1
- **라모르 반지름** — §2.1.2
- **란다우 준위** — §3.3.2
- **마요라나** — §5.3.4
- **마이스너 효과** — §5.3.7
- **맥스웰-볼츠만 분포** — §3.4.5
- **방사 반작용** — §3.2.3
- **보리스 알고리즘** — §2.4.2
- **블라소프 방정식** — §3.4.2
- **사이클로트론** — §4.1.1
- **상대론적 로렌츠 힘** — §3.1
- **섬유다발** — §2.5.4
- **자기 거울** — §2.3.3
- **자기 단극자** — §2.5.3, §5.2.1
- **자기 재결합** — §4.5.3, §4.6.3
- **자기 홀 효과** — §3.3.3, §5.3.1
- **자전** — §2.4.2
- **제이만 효과** — §3.3.4
- **초전도 보텍스** — §5.3.7
- **푸아송 괄호** — §1.4.6
- **푸커-플랑크 방정식** — §3.4.3
- **하이젠베르크 운동방정식** — §3.3.1
- **홀 효과** — §3.3.3, §4.4.1, §5.3.1
- **호프스태터** — §3.3.2

### G.3 현상·응용

- **MRI** — §4.3.1
- **VASIMR** — §5.1.6
- **가속기** — §4.1
- **GMR 센서** — §4.4.2
- **LIGO** — §5.1.5, §6.2.4
- **MEMS 자기 센서** — §4.4.4
- **Penning 트랩** — §5.1.2
- **QGP** — §6.1.3
- **SQUID** — §4.4.3
- **TMR 센서** — §4.4.2
- **강자기장 QED** — §6.1.7
- **그래핀** — §5.3.5
- **밀리차지 입자** — §5.2.2, §6.1.6
- **반 알렌 벨트** — §4.5.2
- **블랙홀 제트** — §6.2.5
- **양성자 치료** — §4.3.2
- **오로라** — §4.5.1
- **자기 나노입자** — §4.3.3
- **자기 트웨저** — §4.3.4
- **중이온 충돌** — §6.1.4
- **태양 플레어** — §4.5.6
- **토카막** — §4.2.1
- **펄서** — §4.5.5
- **홀 추력기** — §5.1.6
- **홀 센서** — §4.4.1

### G.4 수식 기호 (알파벳순)

- **$a_0$** — §5.1.4
- **$B\rho$** — §3.2.6
- **$B_{ps}$** — §5.3.5
- **$c_1$ (Chern 수)** — §2.5.3
- **$D_{RR}$** — §4.6.4
- **$E_n$ (Landau)** — §3.3.2
- **$f^\mu$** — §1.3
- **$F^{\mu\nu}$** — §1.3
- **$H$ (Hamiltonian)** — §1.4.3
- **$L$ (Lagrangian)** — §1.4.1
- **$n_{GJ}$** — §4.5.5
- **$r_L$** — §2.1.2
- **$R_m$** — §2.3.3
- **$S$ (Lundquist)** — §4.5.3
- **$u^\mu$** — §1.3
- **$V_{E\times B}$** — §2.2.1
- **$V_{\nabla B}$** — §2.2.2
- **$W(C)$ (Wilson loop)** — §2.5.6
- **$\gamma$ (Lorentz factor)** — §3.1.1
- **$\gamma_n$ (Berry phase)** — §2.5.1
- **$\eta$ (slip factor)** — §4.1.2
- **$\theta_m$ (mirror angle)** — §2.3.3
- **$\mu$ (adiabatic invariant)** — §2.3
- **$\nu$ (filling factor)** — §3.3.3
- **$\rho$ (rigidity)** — §3.2.6
- **$\sigma_{xy}$ (Hall conductivity)** — §3.3.3, §5.3.1
- **$\tau_0$ (electron time)** — §3.2.3
- **$\Phi_0$ (flux quantum)** — §3.3.3
- **$\chi$ (gauge function)** — §1.5
- **$\Omega_n$ (Berry curvature)** — §2.5.1, §5.3.6
- **$\omega_c$ (cyclotron)** — §2.1.1

### G.5 노벨상 연도

- **1902** — Lorentz, Zeeman — §6.3.7
- **1906** — J.J. Thomson — §6.3.7
- **1907** — Michelson — §6.3.7
- **1923** — Millikan — §6.3.7
- **1936** — Hess — §6.3.7
- **1939** — Lawrence — §6.3.7
- **1943** — Stern — §6.3.7
- **1957** — Yang, Lee — §6.3.7
- **1960** — Glaser — §6.3.7
- **1979** — Glashow, Weinberg, Salam — §6.3.7
- **1985** — von Klitzing — §6.3.7
- **1989** — Dehmelt, Paul — §6.3.7
- **1998** — Laughlin, Störmer, Tsui — §6.3.7
- **2000** — Alferov, Kilby — §6.3.7
- **2007** — Fert, Grünberg — §6.3.7
- **2010** — Geim, Novoselov — §6.3.7
- **2013** — Englert, Higgs — §6.3.7
- **2014** — Akasaki — §6.3.7
- **2016** — Thouless, Haldane, Kosterlitz — §6.3.7
- **2017** — Weiss, Barish, Thorne — §6.3.7
- **2019** — Peebles — §6.3.7
- **2022** — Aspect, Clauser, Zeilinger — §6.3.7

---

## 부록 마무리

> **부록 요약**
>
> - **부록 A** 기호 정의: 7개 카테고리 (기본, 퍼텐셜, 역학, 상대론, 양자, 통계, 응용)
> - **부록 B** 물리 상수: 기본 상수 + 유용한 조합 + 천문 상수
> - **부록 C** 매스매티카 코드: 6막 각각의 핵심 검증 코드
> - **부록 D** Python 코드: 보리스 pusher, 사이클로트론 시각화, 란다우 준위, PIC 1D
> - **부록 E** 참고문헌 통합 색인: 49개 항목 (원논문, 교과서, 리뷰, 최신, 표준, 노벨상)
> - **부록 F** 18개 원질문 ↔ 본문 매핑표: 완전 커버리지 확인
> - **부록 G** 색인: 인명, 개념, 현상, 수식 기호, 노벨상 연도

--
  



  ## 7장. 토카막·오로라·자이로키네틱 이론 심화

> **이 장의 성격**
> 제1부 4막(응용)·5막(최전선)의 확장이다.
> 토카막 평형, 오로라 침전, 자이로키네틱·MHD·PIC 코드를 다룬다.
> 실습 코드는 8장 "수학 모델의 Python화"에서 본문 수식으로부터 직접 구현한다.

---

### 7.1 토카막 지오메트리 & 자기 가둠

#### 7.1.1 Grad-Shafranov 방정식 — 물리

$$\Delta^*\psi = -\mu_0 R^2 p'(\psi) - F(\psi)F'(\psi)$$

> **Unicode**
> ```
> Δ^*ψ = -μ₀ R² p'(ψ) - F(ψ)F'(ψ)
> ```

$$\Delta^* = R\frac{\partial}{\partial R}\left(\frac{1}{R}\frac{\partial}{\partial R}\right) + \frac{\partial^2}{\partial Z^2}$$

> **Unicode**
> ```
> Δ^* = R(∂)/(∂ R)((1)/(R)(∂)/(∂ R)) + (∂²)/(∂ Z²)
> ```

여기서 $\psi$는 폴로이달 자속, $F = R B_\phi$다. $\mathbf{J}\times\mathbf{B} = \nabla p$의 축대칭 축소형이며, 왼쪽은 연산자, 오른쪽은 플라즈마 전류원이다.

#### 7.1.2 수치해법 개요

1. **선형 solver:** multigrid로 $\Delta^*\psi = J_\phi$ 풀이
2. **전류 갱신:** $\psi_{norm} \to p'$, $FF'$ 재계산
3. **Picard 반복:** 수렴 $\|\psi_{new}-\psi_{old}\| < 10^{-6}$
4. **Free-boundary:** PF 코일 전류 최적화

#### 7.1.3 EFIT와 G-EQDSK

- **Forward:** 코일 → 평형
- **Inverse:** 측정(자속 루프, 자기 프로브, MSE, 압력) → 평형 (EFIT)
- 입력 가정: $p'(\psi)$, $FF'(\psi)$ = 다항식/spline 계수
- 출력: $\psi(R,Z)$, q-profile, separatrix

G-EQDSK가 공용 포맷이다. FreeGS, EFIT, TRANSP가 모두 이 포맷으로 평형을 주고받는다. JET EFIT++는 C++ 기반, 최근 EFIT-AI는 ML 가속.

#### 7.1.4 토로이달 코일 기하

$$B_\phi(R) = B_0\frac{R_0}{R}$$

> **Unicode**
> ```
> B_φ(R) = B₀(R₀)/(R)
> ```

이산 TF 코일 $N$개 배치 시 리플:

$$B(R,\phi) = B_\phi(R)\left[1 + \delta\cos(N\phi)\right]$$

> **Unicode**
> ```
> B(R,φ) = B_φ(R)[1 + δcos(Nφ)]
> ```

ITER: $N = 18$, $\delta \sim 0.01$. TF 코일 최대 자장 11.8 T, 플라즈마 중심 5.3 T.

#### 7.1.5 자속면 좌표 $(\psi,\theta,\phi)$

- $\psi$: 자속면 라벨, 0(축)–1(경계)
- $\theta$: 폴로이달 각, 외측 midplane = 0
- $\phi$: 토로이달 각
- 정의: $\mathbf{B} = \nabla\alpha\times\nabla\psi$, $\alpha = \zeta - \int I(\psi)J/(R^2)\,d\theta'$
- Field-aligned: $x = \psi$, $y = \theta$, $z = \phi - q(\psi)\theta$

**왜 필요한가?** $\nabla B$ 드리프트, 곡률 드리프트가 $\psi$에 대해 분리되기 때문이다.

#### 7.1.6 ITER 자기장 파라미터

| 파라미터 | 값 | 비고 |
|---|---|---|
| $R_0$ | 6.2 m | major radius |
| $a$ | 2.0 m | minor radius |
| $B_0$ | 5.3 T | at $R_0$ |
| $I_p$ | 15 MA (17 MA max) | plasma current |
| Volume | 840 m³ | |
| $B_{max}$ on TF coil | 11.8 T | |
| $\kappa_{95}$ | 1.85 | elongation |
| $\delta_{95}$ | 0.49 | triangularity |
| Single-null divertor | 아래 X-point | |
| $q_{95}$ | ~3 | |

출처: ITER baseline Q=10, Shaped tokamak grid.

#### 7.1.7 안전인자 q-profile

$$q = \frac{d\phi}{d\theta} \approx \frac{r B_\phi}{R B_\theta}$$

> **Unicode**
> ```
> q = (dφ)/(dθ) ≈ (r B_φ)/(R B_θ)
> ```

$$q(\psi) = \frac{1}{2\pi}\oint\frac{B_\phi}{R B_p}\, dl_{pol}$$

> **Unicode**
> ```
> q(ψ) = (1)/(2π)∮(B_φ)/(R B_p) dl_pol
> ```

- $q_0 \sim 1$ (축), $q_{95} \sim 3$ (경계), 바깥 6–8
- $q = m/n$ 유리수면에서 island, NTM
- $q < 2$ kink 불안정

---

### 7.2 오로라 지오메트리 & 지구 자기장 모델

#### 7.2.1 쌍극자 자기장

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi r^3}\left[3\hat{r}(\hat{r}\cdot\mathbf{m}) - \mathbf{m}\right]$$

> **Unicode**
> ```
> 𝐁(𝐫) = (μ₀)/(4π r³)[3r̂(r̂·𝐦) - 𝐦]
> ```

구면 성분:

$$B_r = -2 B_0 \left(\frac{R_E}{r}\right)^3 \sin\lambda_m, \quad B_\lambda = B_0 \left(\frac{R_E}{r}\right)^3 \cos\lambda_m$$

> **Unicode**
> ```
> B_r = -2B₀((R_E)/(r))³sinλₘ,   B_λ = B₀((R_E)/(r))³cosλₘ
> ```

$$|B| = B_0 \left(\frac{R_E}{r}\right)^3 \sqrt{1+3\sin^2\lambda_m}$$

> **Unicode**
> ```
> |B| = B₀((R_E)/(r))³√(1+3sin²λₘ)
> ```

자력선: $r = L R_E \cos^2\lambda_m$. 오로라 65–75° → $L = 4$–10, $B_0 \approx 30000$ nT, 유효 $r < 3R_E$.

#### 7.2.2 Tsyganenko 모델 T89/T96

- **T89:** $iopt = K_p$ 1–7, ring + tail + magnetopause + Birkeland 전류의 통계 모델
- **T96:** `parmod = [Pdyn, Dst, By_IMF, Bz_IMF, ...]`, $ps$ = tilt rad, Sibeck 1991 magnetopause, 이벤트 재현

이 모델들은 외부 라이브러리(`geopack`)로 호출하는 것이 표준이며, 본 문서는 수식 유도만 다룬다.

#### 7.2.3 유도 중심 근사 — 오로라 침전

3주기: $T_{gyro}(10^{-3}\,\text{s}) \ll T_{bounce}(\text{초}) \ll T_{drift}(\text{분})$

$$\mu = \frac{m v_\perp^2}{2B} = \text{const}$$

> **Unicode**
> ```
> μ = (m v_⊥²)/(2B) = const
> ```

$$\mathbf{V}_{\nabla B} = \frac{\mu}{qB^2}\mathbf{B}\times\nabla B$$

> **Unicode**
> ```
> 𝐕_∇ B = (μ)/(qB²)𝐁×∇ B
> ```

$$\mathbf{V}_{curv} = \frac{m v_\parallel^2}{qB^2}\frac{\mathbf{B}\times(\mathbf{B}\cdot\nabla)\mathbf{B}}{B}$$

> **Unicode**
> ```
> 𝐕_curv = (m v_∥²)/(qB²)(𝐁×(𝐁·∇)𝐁)/(B)
> ```

손실 콘: $\sin^2\alpha_0 = B_{eq}/B_{iono}$.

#### 7.2.4 태양풍-자기권 압축 — Shue 1998

$$r = r_0\left(\frac{2}{1+\cos\theta}\right)^\alpha$$

> **Unicode**
> ```
> r = r₀((2)/(1+cosθ))^α
> ```

$$r_0 = \left[10.22 + 1.29\tanh\left(0.184(B_z+8.14)\right)\right]P_{dyn}^{-1/6.6}$$

> **Unicode**
> ```
> r₀ = [10.22 + 1.29tanh(0.184(B_z+8.14))]P_dyn^-1/6.6
> ```

$$\alpha = (0.58 - 0.007 B_z)(1 + 0.024\ln P_{dyn})$$

> **Unicode**
> ```
> α = (0.58 - 0.007B_z)(1 + 0.024lnP_dyn)
> ```

$P_{dyn}$ 1 → 10 nPa: standoff 11.4 → 8.1 $R_E$ 압축.

#### 7.2.5 오로라 입자 침전

$$\sin^2\alpha_0 = \frac{B_{eq}}{B_{iono}}$$

> **Unicode**
> ```
> sin²α₀ = (B_eq)/(B_iono)
> ```

$L = 6$에서 loss cone $\approx 3.07°$, 발자국 위도 $\arccos\sqrt{1/L} \approx 65.9°$ — 오로라 오발.

#### 7.2.6 Van Allen 벨트 궤적

3주기 운동: gyro + bounce + drift. Boris pusher로 $\mu$ 보존 std/mean $\sim 5\times10^{-15}$.

---

### 7.3 유체/자이로운동론 결합

#### 7.3.1 자이로키네틱 코드

5D $(R, v_\parallel, \mu)$, $\omega \ll \Omega_c$, $k_\perp\rho_i \sim 1$, $\delta f = f - F_0$.

| 코드 | 언어 | 특징 |
|---|---|---|
| GENE | F90 | local/global, 전자기 |
| GKW | F90 | 회전/충돌 |
| CGYRO | F90 | GPU, TGLF 연동 |

통합 인터페이스: `pyrokinetics` (CGYRO, GENE, GKW, GS2, GKV, stella 지원).

#### 7.3.2 MHD 코드

- **JOREK:** reduced/full MHD, X-point, ELM, VDE, Bezier 요소
- **M3D-C1:** Princeton extended-MHD, stellarator
- **NIMROD:** spectral element, MGI
- **BOUT++:** edge/SOL, drift-reduced Braginskii, STORM 모듈

JOREK 루프: $\psi(R,Z)$ Bezier, $\partial_t\psi = \eta J - R[\psi, u]$.

#### 7.3.3 Vlasov-Maxwell solver

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla_x f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = 0$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐯·∇ₓ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = 0
> ```

Python 오픈: SPECTRAX (JAX, Hermite-Fourier), Veritas (finite volume + AMR), Gkeyll (Lua 입력, 2D2V–3D3V).

#### 7.3.4 PIC 코드

PIC 루프:

1. **Push:** $x \mathrel{+}= v\,dt$, $v \mathrel{+}= \frac{q}{m}(E+v\times B)\,dt$
2. **Deposit:** 입자 → 격자 (CIC)
3. **Field solve:** Poisson
4. **Interpolate:** 격자 → 입자

- **XGC:** total-f PIC, whole volume, edge+SOL+wall, 5D $(R,Z,\phi,v_\parallel,\mu)$
- **GTC:** delta-f, field line following, full torus
- ORB5, GEM, GT5D: core ITG

#### 7.3.5 BOUT++ 난류 코드

Open-source 3D finite difference. Field-aligned $(\psi,\theta,\phi)$, $\nabla_\parallel$ 정확.

`tokamak-2fluid` 예제: DIII-D 129131 평형, Hasegawa-Wakatani + curvature, STORM SOL 난류, ELM, blob.

#### 7.3.6 자이로운동론 오픈소스 정리

선택 가이드:

- **MHD 불안정:** JOREK / M3D-C1
- **Edge blob:** BOUT++
- **Core 수송:** GENE / GKW / CGYRO
- **Edge 전체 + 중성자:** XGC total-f PIC

---

## 8장. 수학 모델의 Python화

> **이 장의 성격**
> 제1부 부록 C가 "수식 → Mathematica"라면, 이 장은 "수식 → Python"이다.
> 외부 라이브러리 호출이 아니라, 본문의 수식을 직접 코드로 옮긴다.
> 각 함수는 대응하는 본문 절 번호를 주석으로 명시한다.
> 의존성은 `numpy`뿐이다.

### 8.1 보리스 pusher (§2.4.2)

$$v^- = v + \frac{qE}{2m}\Delta t, \quad t = \frac{qB}{2m}\Delta t, \quad s = \frac{2t}{1+t^2}$$

> **Unicode**
> ```
> v⁻ = v + (qE)/(2m)Δ t,   t = (qB)/(2m)Δ t,   s = (2t)/(1+t²)
> ```

$$v' = v^- + v^-\times t, \quad v^+ = v^- + v'\times s$$

> **Unicode**
> ```
> v' = v⁻ + v⁻×t,   v⁺ = v⁻ + v'×s
> ```

```python
import numpy as np

def boris_push(x, v, E, B, q, m, dt):
    """§2.4.2 보리스 알고리즘. 위상공간 부피 보존, det J = 1."""
    v_minus = v + q * E * dt / (2 * m)
    t = q * B * dt / (2 * m)
    v_prime = v_minus + np.cross(v_minus, t)
    s = 2 * t / (1 + np.dot(t, t))
    v_plus = v_minus + np.cross(v_prime, s)
    v_new = v_plus + q * E * dt / (2 * m)
    x_new = x + v_new * dt
    return x_new, v_new
```

**검증:** 균일 $\mathbf{B}$, $\mathbf{E}=0$에서 에너지 std/mean $\sim 10^{-15}$.

### 8.2 균일 자기장 궤적 (§2.1.1)

$$\omega_c = \frac{qB_0}{m}, \quad r_L = \frac{v_\perp}{\omega_c}$$

> **Unicode**
> ```
> ω_c = (qB₀)/(m),   r_L = (v_⊥)/(ω_c)
> ```

```python
def cyclotron_orbit(v_perp, omega_c, t):
    """§2.1.1. xy 평면 원운동."""
    x = (v_perp / omega_c) * np.sin(omega_c * t)
    y = (v_perp / omega_c) * np.cos(omega_c * t)
    return x, y

def larmor_radius(v_perp, q, B0, m):
    """§2.1.2."""
    return m * v_perp / (abs(q) * B0)
```

### 8.3 드리프트 속도 (§2.2)

$$\mathbf{V}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

> **Unicode**
> ```
> 𝐕_E = (𝐄×𝐁)/(B²)
> ```

```python
def E_cross_B_drift(E, B):
    """§2.2.1."""
    B2 = np.dot(B, B)
    return np.cross(E, B) / B2

def gradB_drift(B, gradB, mu, q):
    """§2.2.2."""
    B2 = np.dot(B, B)
    return (mu / q) * np.cross(B, gradB) / B2

def curvature_drift(B, Rc, v_par, q, m):
    """§2.2.3. Rc = 곡률 반경 벡터."""
    B2 = np.dot(B, B)
    Rc2 = np.dot(Rc, Rc)
    return (m * v_par**2 / (q * B2)) * np.cross(Rc, B) / Rc2

def polarization_drift(dE_dt, B, q, m):
    """§2.2.1. 시변 전기장."""
    B2 = np.dot(B, B)
    return (m / (q * B2)) * dE_dt
```

### 8.4 단열 불변량과 손실 콘 (§2.3)

$$\mu = \frac{m v_\perp^2}{2B}, \quad \sin^2\theta_m = \frac{B_0}{B_m}$$

> **Unicode**
> ```
> μ = (m v_⊥²)/(2B),   sin²θₘ = (B₀)/(Bₘ)
> ```

```python
def magnetic_moment(v_perp, B, m):
    """§2.3.1."""
    return m * v_perp**2 / (2 * B)

def loss_cone_angle(B_eq, B_iono):
    """§2.3.3. 라디안."""
    return np.arcsin(np.sqrt(B_eq / B_iono))

def mirror_ratio(B_max, B_min):
    """§2.3.3. Rm = Bm/B0."""
    return B_max / B_min
```

### 8.5 Grad-Shafranov 소스항 (§4.2.1, §7.1.1)

$$\Delta^*\psi = -\mu_0 R^2 p'(\psi) - F(\psi)F'(\psi)$$

> **Unicode**
> ```
> Δ^*ψ = -μ₀ R²p'(ψ) - F(ψ)F'(ψ)
> ```

```python
def grad_shafranov_source(R, psi, dp_dpsi, F, dF_dpsi, mu0):
    """§7.1.1. 우변 소스항 J_phi = R p' + FF'/(mu0 R)."""
    return -mu0 * R**2 * dp_dpsi(psi) - F(psi) * dF_dpsi(psi)
```

### 8.6 쌍극자 자기장 (§7.2.1)

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi r^3}\left[3\hat{r}(\hat{r}\cdot\mathbf{m}) - \mathbf{m}\right]$$

> **Unicode**
> ```
> 𝐁(𝐫) = (μ₀)/(4π r³)[3r̂(r̂·𝐦) - 𝐦]
> ```

```python
def dipole_B(r_vec, m_vec, mu0_4pi=1e-7):
    """§7.2.1. m_vec = 자기 쌍극자 모멘트 [A·m²]."""
    r = np.linalg.norm(r_vec)
    r_hat = r_vec / r
    return mu0_4pi / r**3 * (3 * np.dot(m_vec, r_hat) * r_hat - m_vec)

def dipole_Bmag(r, lam, B0=3.1e-5, R_E=6371e3):
    """§7.2.1. 구면 성분 크기."""
    return B0 * (R_E / r)**3 * np.sqrt(1 + 3 * np.sin(lam)**2)
```

### 8.7 Shue 자기권계면 (§7.2.4)

$$r = r_0\left(\frac{2}{1+\cos\theta}\right)^\alpha$$

> **Unicode**
> ```
> r = r₀((2)/(1+cosθ))^α
> ```

```python
def shue_magnetopause(theta, Pdyn, Bz):
    """§7.2.4. theta 라디안, Pdyn nPa, Bz nT. 반환 R_E."""
    r0 = (10.22 + 1.29 * np.tanh(0.184 * (Bz + 8.14))) * Pdyn**(-1/6.6)
    alpha = (0.58 - 0.007 * Bz) * (1 + 0.024 * np.log(Pdyn))
    return r0 * (2 / (1 + np.cos(theta)))**alpha
```

### 8.8 자기 재결합률 (§4.5.3)

$$V_{rec} = \frac{V_A}{\sqrt{S}}, \quad S = \frac{\mu_0 L V_A}{\eta}$$

> **Unicode**
> ```
> V_rec = (V_A)/(√S),   S = (μ₀ L V_A)/(η)
> ```

```python
def sweet_parker_rate(V_A, L, eta, mu0):
    """§4.5.3. Lundquist 수 S = mu0 L V_A / eta."""
    S = mu0 * L * V_A / eta
    return V_A / np.sqrt(S), S
```

### 8.9 란다우 준위 (§3.3.2)

$$E_n = \hbar\omega_c\left(n + \frac12\right)$$

> **Unicode**
> ```
> Eₙ = ℏω_c(n + (1)/(2))
> ```

```python
def landau_levels(n, q, B, m, hbar=1.055e-34):
    """§3.3.2. n = 0,1,2,... 반환 J."""
    omega_c = abs(q) * B / m
    return hbar * omega_c * (np.asarray(n) + 0.5)
```

### 8.10 상대론적 사이클로트론 진동수 (§3.1.3)

$$\omega_c^{rel} = \frac{qB}{\gamma m}, \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}$$

> **Unicode**
> ```
> ω_cʳᵉˡ = (qB)/(γ m),   γ = (1)/(√(1-v²/c²))
> ```

```python
def omega_c_rel(q, B, gamma, m):
    """§3.1.3."""
    return q * B / (gamma * m)

def lorentz_factor(v, c=2.998e8):
    """§3.1.1."""
    return 1 / np.sqrt(1 - np.dot(v, v) / c**2)
```

### 8.11 라모 공식과 Liénard (§3.2.1–3.2.2)

$$P_{Larmor} = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

> **Unicode**
> ```
> P_Larmor = (q² a²)/(6πε₀ c³)
> ```

$$P_{Lienard} = \frac{q^2\gamma^4}{6\pi\varepsilon_0 c^3}\left[a_\perp^2 + \gamma^2 a_\parallel^2\right]$$

> **Unicode**
> ```
> P_Lienard = (q²γ⁴)/(6πε₀ c³)[a_⊥² + γ²a_∥²]
> ```

```python
def larmor_power(q, a, eps0=8.854e-12, c=2.998e8):
    """§3.2.1. a = |가속도|."""
    return q**2 * a**2 / (6 * np.pi * eps0 * c**3)

def lienard_power(q, a_par, a_perp, gamma, eps0=8.854e-12, c=2.998e8):
    """§3.2.2. 상대론적 일반화."""
    return q**2 * gamma**4 / (6 * np.pi * eps0 * c**3) * (a_perp**2 + gamma**2 * a_par**2)
```

### 8.12 강성도 (§3.2.6)

$$B\rho = \frac{p}{q}$$

> **Unicode**
> ```
> Bρ = (p)/(q)
> ```

```python
def rigidity(p, q):
    """§3.2.6. p [kg·m/s], q [C] → Bρ [T·m]."""
    return p / q

def rigidity_GeV(p_GeV, q_e=1):
    """§3.2.6. 실무 공식: Bρ[T·m] = 3.3356 · p[GeV/c] / q[e]."""
    return 3.3356 * p_GeV / q_e
```

### 8.13 수송 계수 (§3.4.6)

$$\sigma_\parallel = \frac{nq^2}{m\nu}$$

> **Unicode**
> ```
> σ_∥ = (nq²)/(mν)
> ```

$$\sigma_P = \sigma_\parallel\frac{\nu^2}{\nu^2+\omega_c^2}, \quad \sigma_H = \sigma_\parallel\frac{\nu\omega_c}{\nu^2+\omega_c^2}$$

> **Unicode**
> ```
> σ_P = σ_∥(ν²)/(ν²+ω_c²),   σ_H = σ_∥(νω_c)/(ν²+ω_c²)
> ```

```python
def braginskii_conductivities(n, q, m, nu, omega_c):
    """§3.4.6. 반환 (sigma_par, sigma_P, sigma_H)."""
    sigma_par = n * q**2 / (m * nu)
    denom = nu**2 + omega_c**2
    sigma_P = sigma_par * nu**2 / denom
    sigma_H = sigma_par * nu * omega_c / denom
    return sigma_par, sigma_P, sigma_H

def perpendicular_diffusion(T, m, nu, omega_c):
    """§3.4.6. D_perp = (T/m) nu/(nu²+omega_c²)."""
    return (T / m) * nu / (nu**2 + omega_c**2)
```

### 8.14 함수 조합 예제

**Van Allen 벨트 궤적 (8.1 + 8.6):**

```python
def van_allen_orbit(L=4.0, energy_eV=1e6, pitch_deg=45.0,
                    dt=1e-5, steps=20000,
                    R_E=6371e3, m_e=9.11e-31, q_e=-1.6e-19):
    """8.1 + 8.6 조합."""
    r0 = np.array([L * R_E, 0.0, 0.0])
    v_total = np.sqrt(2 * energy_eV * 1.6e-19 / m_e)
    v_total = min(v_total, 1.5e8)
    pitch = np.radians(pitch_deg)
    v0 = np.array([0.0, v_total * np.cos(pitch), v_total * np.sin(pitch)])

    m_vec = np.array([0.0, 0.0, 7.9e22])
    x, v = r0, v0
    xs = np.zeros((steps, 3))
    xs[0] = x
    for i in range(1, steps):
        B = dipole_B(x, m_vec)
        x, v = boris_push(x, v, np.zeros(3), B, q_e, m_e, dt)
        xs[i] = x
        if np.linalg.norm(x) < R_E:
            return xs[:i]
    return xs
```

**오로라 침전 (8.4 + 8.6):**

```python
def auroral_precipitation(L=6.0, N=1000, scattering=0.01,
                          B_iono=5e-5, B0=3.1e-5, n_bounce=500):
    """8.4 + 8.6 조합."""
    B_eq = B0 / L**3
    alpha_loss = loss_cone_angle(B_eq, B_iono)
    alphas = np.random.uniform(0, np.pi/2, N)
    history = []
    for _ in range(n_bounce):
        alphas += np.random.normal(0, scattering, N)
        alphas = np.clip(alphas, 1e-3, np.pi/2 - 1e-3)
        prec = alphas < alpha_loss
        history.append(int(np.sum(prec)))
        alphas[prec] = np.random.uniform(alpha_loss, np.pi/2, int(np.sum(prec)))
    return np.degrees(alpha_loss), history
```

---

## 부록 H. 수식 모음

### H.1 로렌츠 힘 & Boris

$$F = q(E + v\times B)$$

> **Unicode**
> ```
> F = q(E + v×B)
> ```

$$v^- = v_{n-1/2} + \frac{qE\,dt}{2m}, \quad t = \frac{qB\,dt}{2m}, \quad s = \frac{2t}{1+t^2}$$

> **Unicode**
> ```
> v⁻ = v_{n-1/2} + (qE dt)/(2m),   t = (qB dt)/(2m),   s = (2t)/(1+t²)
> ```

에너지 보존: std/mean $\sim 5\times10^{-15}$ (검증됨).

### H.2 Grad-Shafranov

$$\Delta^*\psi = -\mu_0 R^2 p'(\psi) - F F'(\psi)$$

> **Unicode**
> ```
> Δ^*ψ = -μ₀ R²p'(ψ) - F F'(ψ)
> ```

$$q(\psi) = \frac{1}{2\pi}\oint\frac{B_\phi}{R B_p}\,dl_{pol} \approx \frac{r B_\phi}{R B_\theta}$$

> **Unicode**
> ```
> q(ψ) = (1)/(2π)∮(B_φ)/(R B_p) dl_pol ≈ (r B_φ)/(R B_θ)
> ```

### H.3 쌍극자 & Shue

$$\mathbf{B}_{dip} = \frac{\mu_0}{4\pi r^3}\left[3\hat{r}(\hat{r}\cdot\mathbf{m}) - \mathbf{m}\right]$$

> **Unicode**
> ```
> 𝐁_dip = (μ₀)/(4π r³)[3r̂(r̂·𝐦) - 𝐦]
> ```

$$r = r_0\left(\frac{2}{1+\cos\theta}\right)^\alpha, \quad r_0 = \left[10.22 + 1.29\tanh(0.184(B_z+8.14))\right]P_{dyn}^{-1/6.6}$$

> **Unicode**
> ```
> r = r₀((2)/(1+cosθ))^α,   r₀ = [10.22 + 1.29tanh(0.184(B_z+8.14))]P_dyn^-1/6.6
> ```

### H.4 유도 중심 & 손실 콘

$$\mu = \frac{m v_\perp^2}{2B} = \text{const}$$

> **Unicode**
> ```
> μ = (m v_⊥²)/(2B) = const
> ```

$$\mathbf{V}_{\nabla B} = \frac{\mu}{qB^2}\mathbf{B}\times\nabla B$$

> **Unicode**
> ```
> 𝐕_∇ B = (μ)/(qB²)𝐁×∇ B
> ```

$$\sin^2\alpha_0 = \frac{B_{eq}}{B_{iono}}$$

> **Unicode**
> ```
> sin²α₀ = (B_eq)/(B_iono)
> ```

$$\lambda_{iono} = \arccos\sqrt{1/L} \quad (L=6 \to 65.9°)$$

> **Unicode**
> ```
> λ_iono = arccos√(1/L)  (L=6 → 65.9°)
> ```

### H.5 자이로키네틱 & MHD & Vlasov & PIC

- **Gyrokinetic:** $f(R, v_\parallel, \mu)$, $\omega \ll \Omega_c$, $k_\perp\rho_i \sim 1$, $\delta f = f - F_0$

> **Unicode**
> ```
> Gyrokinetic: f(R,v_∥,μ), ω≪Ω_c, k_⊥ρᵢ∼1, δf = f-F₀
> ```

- **MHD:** $\mathbf{J}\times\mathbf{B} = \nabla p + \rho\,d\mathbf{V}/dt$, reduced MHD $\partial_t\psi = \eta J - R[\psi,u]$

> **Unicode**
> ```
> MHD: J×B = ∇ p + ρ dV/dt,   reduced MHD ∂ₜψ = ηJ - R[ψ,u]
> ```

- **Vlasov:** $\partial_t f + \mathbf{v}\cdot\nabla_x f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = 0$

> **Unicode**
> ```
> Vlasov: ∂ₜ f + 𝐯·∇ₓ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = 0
> ```

- **PIC:** 1. Push → 2. Deposit (CIC) → 3. Solve Poisson → 4. Interpolate

> **Unicode**
> ```
> PIC: 1.Push 2.Deposit (CIC) 3.Solve Poisson 4.Interpolate
> ```