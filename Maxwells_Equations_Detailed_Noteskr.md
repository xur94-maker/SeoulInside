# 맥스웰 방정식: 미분형·적분형에서 상대론적 공변형식과 게이지 이론까지

---

## 목차

1. 미분형 ↔ 적분형 동치 증명
2. 변위전류 도입의 필연성
3. 전자기파 방정식 유도 + 빛의 속도와의 일치
4. 자기 홀극 부재의 수학적 표현
5. 쿨롱 법칙·비오-사바르 법칙에서 처음부터 유도하는 과정
6. 상대론적 공변형식과 4-벡터 표기
7. 게이지 변환의 상세 증명 및 현대 확장

---

# 1. 미분형 ↔ 적분형 동치 증명

맥스웰 방정식의 미분형과 적분형이 동치임을 보이는 것은 결국 **발산 정리**와 **스토크스 정리**라는 두 개의 순수한 수학적 도구에 의존합니다. 이 정리들 자체는 물리와 무관한 벡터 미적분학의 항등식이고, 맥스웰 방정식의 "물리"는 적분형(또는 미분형) 어느 한쪽에 담겨 있을 뿐입니다.

## 1.0 사전 도구: 두 적분 정리

### (A) 발산 정리 (Gauss–Ostrogradsky Theorem)

임의의 매끄러운 폐곡면 $S$가 둘러싸는 부피 $V$와, 그 위에서 미분 가능한 벡터장 $\mathbf{F}$에 대해:

$$\oint_S \mathbf{F}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{F})\, dV$$

**의미**: 벡터장이 폐곡면을 통해 빠져나가는 총 flux는, 그 내부에서 벡터장이 "생성"되는 양(발산)을 전부 더한 것과 같다.

### (B) 스토크스 정리 (Stokes' Theorem)

임의의 매끄러운 열린 곡면 $S$와 그 경계인 폐곡선 $\partial S = C$, 그 위에서 미분 가능한 벡터장 $\mathbf{F}$에 대해:

$$\oint_C \mathbf{F}\cdot d\boldsymbol{\ell} = \int_S (\nabla\times\mathbf{F})\cdot d\mathbf{A}$$

**의미**: 벡터장이 폐곡선을 따라 도는 총 순환(circulation)은, 그 곡선이 경계인 곡면 위에서 벡터장이 "회전"하는 양(컬)을 전부 더한 것과 같다.

이 두 정리는 **임의의** $V$, $S$에 대해 성립한다는 점이 핵심입니다. 이 "임의성"이 나중에 적분형 → 미분형을 유도할 때 결정적 역할을 합니다.

## 1.1 Gauss의 법칙 (전기장) — 발산 정리 적용

**적분형**:
$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{enc}}{\varepsilon_0} = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

**미분형**:
$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

### 증명 (적분형 → 미분형)

**1단계.** 적분형 좌변에 발산 정리를 적용합니다:
$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{E})\, dV$$

**2단계.** 따라서 적분형은 다음과 같이 다시 쓸 수 있습니다:
$$\int_V (\nabla\cdot\mathbf{E})\, dV = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

$$\int_V \left(\nabla\cdot\mathbf{E} - \frac{\rho}{\varepsilon_0}\right) dV = 0$$

**3단계 (핵심 — "임의의 부피" 논증).** 이 식은 특정한 $V$에 대해서만 성립하는 게 아니라, **공간 속 어떤 폐곡면을 잡더라도** 성립해야 합니다 (Gauss 법칙 자체가 임의의 곡면에 대해 성립하는 물리 법칙이므로). 만약 피적분함수 $f \equiv \nabla\cdot\mathbf{E} - \rho/\varepsilon_0$가 어떤 점 $P$에서 $0$이 아니라고 가정해봅시다. 연속성에 의해 $P$ 주변의 작은 근방에서도 $f$는 (거의) 같은 부호를 가집니다. 그 근방을 감싸는 아주 작은 부피 $V_\epsilon$을 잡으면

$$\int_{V_\epsilon} f\, dV \neq 0$$

이 되어 모순입니다. 따라서 **모든 점**에서

$$\nabla\cdot\mathbf{E} - \frac{\rho}{\varepsilon_0} = 0 \quad\Longrightarrow\quad \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

(이 "임의의 영역에서 적분이 0이면 피적분함수도 0이다"라는 논증은 이후 증명에서도 동일하게 반복되므로, **변분법의 기본 보조정리(fundamental lemma)**라고 부릅니다.)

### 역방향 (미분형 → 적분형)

미분형 $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$이 모든 점에서 성립한다고 가정하면, 임의의 부피 $V$에 대해 양변을 적분:

$$\int_V \nabla\cdot\mathbf{E}\, dV = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

좌변에 발산 정리를 적용하면 바로 적분형이 나옵니다. $\blacksquare$

## 1.2 Gauss의 법칙 (자기장) — 발산 정리 적용

**적분형**:
$$\oint_S \mathbf{B}\cdot d\mathbf{A} = 0$$

**미분형**:
$$\nabla\cdot\mathbf{B} = 0$$

### 증명

발산 정리에 의해:
$$\oint_S \mathbf{B}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{B})\, dV = 0$$

이는 **임의의** $V$에 대해 성립해야 하므로, 1.1과 동일한 기본 보조정리에 의해 모든 점에서

$$\nabla\cdot\mathbf{B} = 0$$

이 방정식은 우변이 항상 0이라는 점에서 특별한 물리적 의미를 가집니다 — 즉 "자기 홀극(magnetic monopole)이 존재하지 않는다"는 진술 그 자체가 이 방정식의 물리적 내용입니다. $\blacksquare$

## 1.3 Faraday의 법칙 — 스토크스 정리 적용

**적분형**:
$$\oint_C \mathbf{E}\cdot d\boldsymbol{\ell} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A}$$

**미분형**:
$$\nabla\times\mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

### 증명 (적분형 → 미분형)

**1단계.** 좌변에 스토크스 정리를 적용:
$$\oint_C \mathbf{E}\cdot d\boldsymbol{\ell} = \int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A}$$

**2단계.** 우변은 곡면 $S$가 시간에 대해 고정되어 있다고 가정하면 (움직이지 않는 경로), 시간 미분을 적분 안으로 넣을 수 있습니다:
$$-\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A} = -\int_S \frac{\partial \mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

**3단계.** 두 식을 합치면:
$$\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

$$\int_S \left(\nabla\times\mathbf{E} + \frac{\partial\mathbf{B}}{\partial t}\right)\cdot d\mathbf{A} = 0$$

**4단계 (임의의 곡면 논증).** 이 등식은 경계 $C$를 공유하는 **임의의** 곡면 $S$에 대해 성립해야 합니다. 앞서와 동일한 논리로, 피적분 벡터 $\nabla\times\mathbf{E} + \partial\mathbf{B}/\partial t$가 어떤 점에서 $0$이 아니면 그 점을 포함하는 아주 작은 곡면을 잡아 적분이 $0$이 아니게 만들 수 있어 모순이 됩니다. 따라서 모든 점에서

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}$$

### 역방향 (미분형 → 적분형)

미분형이 모든 점에서 성립한다고 가정하고, 고정된 경계 $C$를 갖는 임의의 곡면 $S$에 대해 양변에 면적분을 취하면:

$$\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

좌변에 스토크스 정리, 우변에 시간미분과 적분의 교환을 적용하면 바로 적분형이 복원됩니다. $\blacksquare$

## 1.4 Ampère–Maxwell 법칙 — 스토크스 정리 적용 (변위전류 포함)

**적분형**:
$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc} + \mu_0\varepsilon_0\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{A}$$

여기서 $I_{enc} = \int_S \mathbf{J}\cdot d\mathbf{A}$ (전류밀도의 면적분).

**미분형**:
$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

### 증명

**1단계.** 좌변에 스토크스 정리:
$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \int_S(\nabla\times\mathbf{B})\cdot d\mathbf{A}$$

**2단계.** 우변을 면적분 형태로 통일:
$$\mu_0 I_{enc} + \mu_0\varepsilon_0\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{A} = \int_S \mu_0\mathbf{J}\cdot d\mathbf{A} + \int_S \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\cdot d\mathbf{A}$$

**3단계.** 좌변 = 우변으로 놓고 정리:
$$\int_S \left[\nabla\times\mathbf{B} - \mu_0\mathbf{J} - \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right]\cdot d\mathbf{A} = 0$$

**4단계.** 경계 $C$를 공유하는 임의의 곡면 $S$에 대해 성립해야 하므로, 기본 보조정리에 의해 대괄호 안이 모든 점에서 $0$:

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

### 참고: 왜 변위전류 항이 "필요했는가" (일관성 확인)

미분형 양변에 발산을 취하면, 항등식 $\nabla\cdot(\nabla\times\mathbf{B}) \equiv 0$ 이므로:
$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

여기에 Gauss 법칙 $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$을 대입하면:
$$0 = \mu_0\left(\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}\right)$$

즉 **전하 보존 법칙(연속 방정식)** $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$이 자동으로 도출됩니다. 만약 맥스웰이 변위전류 항 $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$을 추가하지 않았다면 이 일관성은 깨졌을 것입니다 — 이것이 역사적으로 변위전류가 도입된 이유이기도 합니다. $\blacksquare$

## 1.5 네 증명의 공통 구조

| 방정식 | 적용 정리 | 핵심 논증 |
|---|---|---|
| Gauss (E) | 발산 정리 | 임의의 부피 → 피적분함수 = 0 |
| Gauss (B) | 발산 정리 | 임의의 부피 → 피적분함수 = 0 |
| Faraday | 스토크스 정리 | 임의의 곡면 → 피적분 벡터 = 0 |
| Ampère–Maxwell | 스토크스 정리 | 임의의 곡면 → 피적분 벡터 = 0 |

네 증명 모두 동일한 3단계 패턴을 따릅니다:

1. 적분 정리로 적분형의 좌변(또는 양변)을 같은 종류의 적분(부피적분 혹은 면적분)으로 통일한다.
2. 두 적분을 하나로 합쳐 "(피적분식) 적분 = 0" 형태로 만든다.
3. 이 적분이 **임의의** 영역에 대해 성립해야 한다는 물리적 요구사항을 이용해, 피적분식 자체가 각 점에서 항등적으로 0임을 결론짓는다(기본 보조정리).

이 구조 덕분에 "왜 두 가지 형태가 존재하는가"에 대한 답이 명확해집니다: **적분형은 유한한 영역(곡면·곡선)에 대한 전역적 진술**이고, **미분형은 공간의 각 점에서의 국소적 진술**이며, 두 정리(발산·스토크스)와 "임의의 영역" 논증이 이 둘을 정확히 연결해 줍니다.

---

# 2. 변위전류 도입의 필연성

변위전류가 왜 "선택사항"이 아니라 "논리적 필연"이었는지를 보입니다. 핵심은 **전하 보존 법칙**과 **원래의 Ampère 법칙**이 정적(static)이 아닌 상황에서 서로 모순된다는 것을 수학적으로 명확히 드러내는 것입니다.

## 2.0 출발점: 두 개의 독립적인 물리 법칙

**법칙 A — 전하 보존 (연속 방정식)**:
$$\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t} = 0 \quad \cdots (1)$$

이것은 전자기학의 법칙이 아니라 더 근본적인 **실험적 사실**입니다 — 전하는 어떤 지점에서 갑자기 생겨나거나 사라지지 않고, 전류밀도 $\mathbf{J}$의 발산(유출량)만큼 그 지점의 전하밀도 $\rho$가 감소해야 한다는 뜻입니다. 이 법칙은 정적이든 동적이든 **항상, 예외 없이** 성립해야 합니다.

**법칙 B — 원래(정자기학) Ampère 법칙**:
$$\nabla\times\mathbf{B} = \mu_0 \mathbf{J} \quad \cdots (2)$$

이것은 정상 전류(steady current, 즉 $\partial\rho/\partial t = 0$)에 대해서만 실험적으로 검증되어 있던 법칙입니다.

## 2.1 모순의 발견: 항등식을 이용한 진단

임의의 벡터장 $\mathbf{B}$에 대해 다음은 순수한 수학적 항등식입니다 (벡터의 curl을 다시 divergence하면 항상 0):

$$\nabla\cdot(\nabla\times\mathbf{B}) \equiv 0 \quad \cdots (3)$$

이는 물리와 무관하게, 어떤 매끄러운 벡터장에도 성립하는 벡터 미적분학의 정리입니다 (직관적으로: curl은 "회전"을 나타내는데, 회전하는 장은 어디로도 순유출되지 않기 때문입니다).

이제 법칙 B, 즉 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$가 **일반적으로도(시간에 따라 변하는 상황에서도)** 성립한다고 가정하고, 양변에 발산을 취해봅시다.

$$\nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J}$$

좌변은 항등식 (3)에 의해 반드시 $0$이므로:

$$0 = \mu_0\,\nabla\cdot\mathbf{J} \quad\Longrightarrow\quad \nabla\cdot\mathbf{J} = 0 \quad \cdots (4)$$

**여기서 모순이 드러납니다.** 식 (4)는 "$\mathbf{J}$의 발산이 항상 0이어야 한다"고 강제합니다. 그런데 법칙 A(전하 보존, 식 (1))는:

$$\nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}$$

즉 $\mathbf{J}$의 발산은 **오직 $\rho$가 시간에 대해 변하지 않을 때만($\partial\rho/\partial t = 0$)** 0입니다.

**결론**: 원래의 Ampère 법칙 (2)는, 전하밀도가 시간에 따라 변하는(즉 $\partial\rho/\partial t \neq 0$) 모든 상황에서 전하 보존 법칙과 정면으로 모순됩니다. 두 개의 검증된 법칙이 동시에 참일 수 없는 상황이 발생한 것입니다.

## 2.2 구체적인 물리 상황으로 모순 시각화: 충전되는 축전기

이 모순은 추상적인 수식놀음이 아니라, 실제로 실험 가능한 상황에서 발생합니다. 전형적인 예가 **충전 중인 평행판 축전기**입니다.

회로에 전류 $I$가 흘러 축전기를 충전하고 있다고 합시다. Ampère 법칙의 적분형은:

$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc}$$

여기서 $I_{enc}$는 폐곡선 $C$를 경계로 하는 **어떤 곡면이든** 상관없이 그 곡면을 관통하는 전류입니다. 스토크스 정리의 논리상 $I_{enc}$는 곡면 선택에 무관해야 합니다 (경계 $C$만 같으면 됨). 이제 도선을 감싸는 폐곡선 $C$를 고정하고, 두 가지 다른 곡면을 선택해봅시다.

**곡면 $S_1$**: 도선을 수직으로 가로지르는 평평한 원판. 도선 속 전류 $I$가 그대로 관통합니다.
$$I_{enc}^{(S_1)} = I$$

**곡면 $S_2$**: 같은 경계 $C$를 가지지만, 축전기의 두 극판 사이 공간을 통과하도록 풍선처럼 부풀린 곡면. 극판 사이는 진공(또는 유전체)이므로 전도 전류가 흐르지 않습니다.
$$I_{enc}^{(S_2)} = 0$$

**같은 경계 $C$**에 대해 $I_{enc}^{(S_1)} = I \neq 0 = I_{enc}^{(S_2)}$ 라는 서로 다른 값이 나옵니다. 그런데 좌변 $\oint_C \mathbf{B}\cdot d\boldsymbol{\ell}$은 오직 $C$에만 의존하고 어떤 곡면을 골랐는지에는 무관한 값이어야 하므로, 이는 명백한 모순입니다. 이 모순은 정확히 위에서 보인 수학적 모순 $\nabla\cdot\mathbf{J} \neq 0$의 물리적 현현(顯現)입니다 — 축전기 극판에 전하가 쌓이면서($\partial\rho/\partial t \neq 0$) 도선의 전류가 극판 표면에서 "끊기기" 때문입니다.

## 2.3 해법: 무엇을 더해야 모순이 사라지는가?

모순의 근원은 식 (4), 즉 "$\nabla\times\mathbf{B} = \mu_0\mathbf{J}$의 발산을 취하면 $\nabla\cdot\mathbf{J}=0$이 강제된다"는 점이었습니다. 이를 해소하려면, Ampère 법칙 우변에 **어떤 항 $\mathbf{X}$를 추가**하여

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\mathbf{X}$$

양변의 발산을 취했을 때 자동으로 전하 보존 법칙과 정확히 일치하도록 만들어야 합니다. 즉 요구조건은:

$$\nabla\cdot(\nabla\times\mathbf{B}) = 0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\nabla\cdot\mathbf{X}$$

$$\Longrightarrow\quad \nabla\cdot\mathbf{X} = -\nabla\cdot\mathbf{J}$$

그런데 전하 보존 법칙 (1)에 의해 $-\nabla\cdot\mathbf{J} = \partial\rho/\partial t$이므로:

$$\nabla\cdot\mathbf{X} = \frac{\partial\rho}{\partial t} \quad \cdots (5)$$

**여기서 결정적인 연결고리가 등장합니다.** Gauss 법칙의 미분형은:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \quad\Longrightarrow\quad \rho = \varepsilon_0\,\nabla\cdot\mathbf{E}$$

이를 식 (5)에 대입하면:

$$\nabla\cdot\mathbf{X} = \frac{\partial}{\partial t}\left(\varepsilon_0\,\nabla\cdot\mathbf{E}\right) = \nabla\cdot\left(\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right)$$

(공간 미분 $\nabla\cdot$와 시간 미분 $\partial/\partial t$은 서로 독립적인 변수에 대한 연산이므로 순서를 바꿀 수 있습니다.)

이 등식이 성립하는 **가장 간단하고 자연스러운 해**는:

$$\mathbf{X} = \varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

(더 일반적으로는 $\nabla\times(\text{임의 벡터장})$을 더한 것도 발산이 같지만, 그런 임의성은 물리적으로 불필요하고 실험과도 맞지 않으므로 배제합니다. 즉 이 항이 유일하게 필요충분한 "최소한의" 수정입니다.)

## 2.4 수정된 Ampère 법칙의 검증

이렇게 얻은 새 법칙(Ampère–Maxwell 법칙)은:

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \cdots (6)$$

양변에 발산을 취해 일관성을 재확인합니다:

$$\underbrace{\nabla\cdot(\nabla\times\mathbf{B})}_{=0 \text{ (항등식)}} = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}\left(\frac{\rho}{\varepsilon_0}\right) = \mu_0\left(\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}\right)$$

$$\therefore\ \nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t} = 0$$

이는 정확히 전하 보존 법칙 (1) 그 자체입니다. **더 이상 모순이 없고, 오히려 전하 보존 법칙이 자동으로(항등식처럼) 도출됩니다.** $\blacksquare$

## 2.5 축전기 예제로 모순 해소 확인

$\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ 항을 **변위전류밀도** $\mathbf{J}_d \equiv \varepsilon_0\,\partial\mathbf{E}/\partial t$ 라 부릅니다. 2.2절의 축전기 예제를 다시 봅시다.

- 곡면 $S_1$ (도선 관통): 전도전류만 있고 $\mathbf{E}$는 변하지 않음(도선 내부) → $I_{enc} = I + 0 = I$
- 곡면 $S_2$ (극판 사이 관통): 전도전류는 없지만($\mathbf{J}=0$), 극판 사이에 전하가 쌓이며 전기장 $\mathbf{E}$가 시간에 따라 증가 → 변위전류 $I_d = \varepsilon_0\dfrac{d}{dt}\displaystyle\int_{S_2}\mathbf{E}\cdot d\mathbf{A} = \varepsilon_0\dfrac{d}{dt}\left(\dfrac{Q}{\varepsilon_0 A}\right)A = \dfrac{dQ}{dt} = I$

두 곡면 모두 정확히 같은 값 $I$를 주므로, **더 이상 곡면 선택에 따라 결과가 달라지지 않습니다.** 모순이 완전히 해소되었습니다.

## 2.6 논리 전개의 전체 흐름

$$
\begin{array}{c}
\text{전하 보존: } \nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t} \neq 0 \ \text{(동적 상황)} \\
\Big\Downarrow \\
\text{원래 Ampère 법칙 } \nabla\times\mathbf{B}=\mu_0\mathbf{J} \text{의 발산} \Rightarrow \nabla\cdot\mathbf{J}=0 \\
\Big\Downarrow \\
\textbf{모순} \\
\Big\Downarrow \\
\text{보정항 } \mathbf{X} \text{ 요구: } \nabla\cdot\mathbf{X} = \dfrac{\partial\rho}{\partial t} \\
\Big\Downarrow \\
\text{Gauss 법칙 대입} \Rightarrow \mathbf{X} = \varepsilon_0\dfrac{\partial\mathbf{E}}{\partial t} \\
\Big\Downarrow \\
\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\dfrac{\partial\mathbf{E}}{\partial t}
\end{array}
$$

이 논증이 아름다운 이유는, 변위전류 항이 "실험 결과에 끼워 맞춘 임시방편"이 아니라 **이미 알려진 두 법칙(전하보존 + Gauss 법칙)의 순수한 논리적 귀결**로 나온다는 점입니다. 맥스웰의 통찰은 실험이 아니라 바로 이 **수학적 일관성**에서 출발했습니다 — 그리고 이렇게 추가된 항이 나중에 전자기파의 존재를 예측하게 됩니다 ($\nabla\times\mathbf{E}$의 시간 변화가 $\mathbf{B}$를 낳고, $\mathbf{B}$의 시간 변화가 다시 $\mathbf{E}$를 낳는 자기 지속적 파동).

---

# 3. 전자기파 방정식 유도 + 속도가 빛의 속도와 같음

진공(자유공간, $\rho=0, \mathbf{J}=0$) 속 맥스웰 방정식으로부터 파동방정식을 유도하고, 그 전파 속도가 빛의 속도와 정확히 일치함을 보입니다. 이 부분이 바로 맥스웰이 "전기·자기 이론"에서 "빛의 이론"으로 도약한 순간입니다.

## 3.0 출발점: 진공 속 맥스웰 방정식 (4개)

전하와 전류가 없는 자유공간($\rho = 0$, $\mathbf{J}=0$)을 가정합니다:

$$\nabla\cdot\mathbf{E} = 0 \quad \cdots (1)$$
$$\nabla\cdot\mathbf{B} = 0 \quad \cdots (2)$$
$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} \quad \cdots (3)$$
$$\nabla\times\mathbf{B} = \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \cdots (4)$$

핵심 아이디어: (3)과 (4)는 $\mathbf{E}$와 $\mathbf{B}$가 서로의 시간 변화를 낳는 **결합된(coupled)** 방정식입니다. 이 결합을 풀어서 $\mathbf{E}$만의, $\mathbf{B}$만의 독립된 방정식으로 분리하는 것이 목표입니다.

## 3.1 필요한 벡터 항등식

임의의 벡터장 $\mathbf{F}$에 대해 성립하는 순수 수학적 항등식(curl-of-curl 항등식):

$$\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F} \quad \cdots (5)$$

여기서 $\nabla^2\mathbf{F}$는 벡터 라플라시안(각 성분에 스칼라 라플라시안을 적용)입니다. 이 항등식은 전자기학과 무관하게 항상 성립합니다.

## 3.2 E에 대한 파동방정식 유도

**1단계.** 식 (3)의 양변에 $\nabla\times$를 취합니다:

$$\nabla\times(\nabla\times\mathbf{E}) = \nabla\times\left(-\frac{\partial\mathbf{B}}{\partial t}\right)$$

**2단계.** 좌변에 항등식 (5)를 적용:

$$\nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\nabla\times\frac{\partial\mathbf{B}}{\partial t}$$

**3단계.** 좌변 첫 항은 식 (1) $\nabla\cdot\mathbf{E}=0$에 의해 사라집니다:

$$-\nabla^2\mathbf{E} = -\nabla\times\frac{\partial\mathbf{B}}{\partial t}$$

**4단계.** 우변에서, 공간 미분($\nabla\times$)과 시간 미분($\partial/\partial t$)은 서로 독립 변수에 대한 연산이므로 순서 교환이 가능합니다:

$$-\nabla^2\mathbf{E} = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B})$$

$$\nabla^2\mathbf{E} = \frac{\partial}{\partial t}(\nabla\times\mathbf{B})$$

**5단계 (결합 해소의 핵심).** 이제 우변의 $\nabla\times\mathbf{B}$에 식 (4)를 대입합니다 — 이것이 $\mathbf{B}$를 완전히 소거하고 $\mathbf{E}$만 남기는 단계입니다:

$$\nabla^2\mathbf{E} = \frac{\partial}{\partial t}\left(\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right) = \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}$$

**결과**:

$$\boxed{\nabla^2\mathbf{E} - \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2} = 0} \quad \cdots (6)$$

## 3.3 B에 대한 파동방정식 유도 (동일한 절차, 대칭적으로)

**1단계.** 식 (4)의 양변에 $\nabla\times$를 취합니다:

$$\nabla\times(\nabla\times\mathbf{B}) = \mu_0\varepsilon_0\,\nabla\times\frac{\partial\mathbf{E}}{\partial t}$$

**2단계.** 좌변에 항등식 (5) 적용:

$$\nabla(\nabla\cdot\mathbf{B}) - \nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\times\mathbf{E})$$

**3단계.** 첫 항은 식 (2) $\nabla\cdot\mathbf{B}=0$에 의해 소거:

$$-\nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\times\mathbf{E})$$

**4단계.** 우변에 식 (3), $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ 를 대입:

$$-\nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}\left(-\frac{\partial\mathbf{B}}{\partial t}\right) = -\mu_0\varepsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2}$$

**결과**:

$$\boxed{\nabla^2\mathbf{B} - \mu_0\varepsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2} = 0} \quad \cdots (7)$$

$\mathbf{E}$와 $\mathbf{B}$가 완전히 동일한 형태의 방정식을 만족한다는 점에 주목하세요 — 이는 우연이 아니라 맥스웰 방정식의 $\mathbf{E}\leftrightarrow\mathbf{B}$ 대칭성(부호 하나만 빼고)을 반영합니다.

## 3.4 이 방정식이 왜 "파동방정식"인가

일반적인 3차원 파동방정식의 표준형은:

$$\nabla^2\psi - \frac{1}{v^2}\frac{\partial^2\psi}{\partial t^2} = 0$$

이때 $v$는 파동의 전파 속도입니다. 이는 예컨대 $\psi(x,t) = f(x - vt)$ 같은 함수(모양이 변하지 않고 속도 $v$로 이동하는 파형)가 이 방정식을 만족한다는 사실로 확인할 수 있습니다: $\partial^2\psi/\partial x^2 = f''$, $\partial^2\psi/\partial t^2 = v^2 f''$이므로 대입하면 항등적으로 0이 됩니다.

식 (6), (7)을 이 표준형과 비교하면:

$$\frac{1}{v^2} = \mu_0\varepsilon_0 \quad\Longrightarrow\quad v = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

즉, **$\mathbf{E}$와 $\mathbf{B}$는 각각 속도 $v = 1/\sqrt{\mu_0\varepsilon_0}$로 공간을 전파하는 파동**이라는 결론이 순수하게 수학적으로 도출됩니다. 이 속도를 $c$라고 정의합니다:

$$c \equiv \frac{1}{\sqrt{\mu_0\varepsilon_0}} \quad \cdots (8)$$

## 3.5 수치 검증: c가 정말 빛의 속도와 같은가

맥스웰 당시(1860년대) 알려져 있던 상수값:

- 진공 투자율: $\mu_0 = 4\pi\times 10^{-7}\ \text{T}\cdot\text{m/A}$ (당시 정의상 정확한 값)
- 진공 유전율: $\varepsilon_0 \approx 8.854\times 10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$ (Weber와 Kohlrausch 등이 정전기·전류 실험으로 측정)

이 둘은 **완전히 독립적인 실험**에서 나온 값입니다:

- $\mu_0$는 두 전류 사이의 힘(자기 현상, Ampère의 실험)에서
- $\varepsilon_0$는 축전기의 전하-전압 관계(정전기 현상, Coulomb/Cavendish 류 실험)에서

측정되었으며, 애초에 빛이나 광학과는 아무 관련이 없는 상수들이었습니다.

계산 결과:

$$\mu_0\varepsilon_0 \approx 1.1127\times10^{-17}\ \text{s}^2/\text{m}^2$$

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 2.998\times 10^{8}\ \text{m/s} \approx 299{,}792{,}458\ \text{m/s}$$

이 값은 **당시 이미 Fizeau, Foucault 등의 광학 실험으로 독립적으로 측정되어 있던 빛의 속도**와 (당시 측정 오차 범위 안에서) 정확히 일치했습니다. (현재는 오히려 $c$를 정의상수 $299{,}792{,}458\ \text{m/s}$로 고정하고 미터를 거기서 역정의하지만, 맥스웰 시대에는 $c$가 독립적으로 측정된 값이었다는 점이 중요합니다.)

**맥스웰의 결론** (1862년경, 논문 "A Dynamical Theory of the Electromagnetic Field", 1865): 전기·자기 실험에서만 얻어진 두 상수 $\mu_0, \varepsilon_0$를 조합했을 뿐인데, 그 결과가 완전히 다른 분야인 광학에서 측정된 빛의 속도와 소수점 이하까지 일치한다는 것은 우연일 수 없다 — **따라서 빛 자체가 전자기 현상, 즉 전자기파다.**

## 3.6 유도의 논리 구조 정리

| 단계 | 사용한 방정식 | 소거되는 것 |
|---|---|---|
| $\nabla\times(3)$ | Faraday 법칙 | — |
| curl-of-curl 항등식 적용 | 벡터 항등식 | $\nabla(\nabla\cdot\mathbf{E})$ 항 (Gauss 법칙으로 소거) |
| $\nabla\times\mathbf{B}$에 (4) 대입 | Ampère–Maxwell 법칙 | $\mathbf{B}$가 완전히 소거되고 $\mathbf{E}$만 남음 |

이 유도에서 **네 방정식이 전부 다 사용되었다**는 점이 중요합니다:

- Gauss 법칙(E, B) → $\nabla(\nabla\cdot\mathbf{F})$ 항 소거
- Faraday 법칙 → $\mathbf{B}$를 $\mathbf{E}$의 시간 미분과 연결
- **Ampère–Maxwell 법칙(변위전류 포함)** → 이 결합 고리를 완성

만약 변위전류 항 $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$이 없었다면(즉 원래의 Ampère 법칙만 썼다면), 5단계에서 $\partial^2\mathbf{E}/\partial t^2$ 항 자체가 나타나지 않아 **파동방정식이 성립하지 않습니다** — 즉 전자기파 예측 자체가 불가능했을 것입니다. 이것이 변위전류가 이 서사의 필연적 전제조건이었던 이유입니다.

---

# 4. 자기 홀극이 없다는 것의 수학적 표현

"자기 홀극이 없다"는 물리적 진술이 왜 정확히 $\nabla\cdot\mathbf{B}=0$이라는 수식으로 표현되는지, 전기장의 경우와 대비시키면서 보입니다.

## 4.1 대조군: 전기장은 "홀극"을 가진다

먼저 비교 대상인 Gauss 법칙(전기)을 봅시다:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

여기서 $\rho$는 **전하밀도**입니다. 전자(음전하) 하나만 따로 존재할 수 있고, 양성자(양전하) 하나만 따로 존재할 수도 있습니다. 즉 전기장에는 **혼자 존재 가능한 "원천(source)"**, 즉 전하라는 실체가 있습니다.

이를 적분형으로 보면:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{enc}}{\varepsilon_0}$$

임의의 폐곡면 $S$로 전하 하나를 감싸면, 그 폐곡면을 통해 **순수하게 밖으로 빠져나가는(net outward)** flux가 0이 아닙니다. 전기력선은 양전하에서 "시작"해서 음전하에서 "끝나는" 열린 선입니다 — 즉 발산(source/sink)이 존재합니다.

## 4.2 자기장의 경우: 대응하는 법칙

$$\nabla\cdot\mathbf{B} = 0$$

우변이 **항상, 무조건 0**이라는 점이 핵심입니다. Gauss 법칙(전기)의 우변에는 $\rho/\varepsilon_0$이라는, 존재할 수도 없을 수도 있는 물리량이 있었지만, 이 방정식의 우변에는 애초에 그런 자리 자체가 없습니다 — "자기 전하밀도"라는 양이 이론에 존재하지 않는다는 뜻입니다.

## 4.3 발산의 물리적 의미로 직접 연결

발산 $\nabla\cdot\mathbf{B}$란 한 점 근방에서 $\mathbf{B}$가 **얼마나 순수하게 뿜어져 나오는지(net outflow)**를 나타내는 양입니다. 만약 자기 홀극(예: 고립된 N극, 혹은 "자기 전하" $\rho_m$)이 존재한다면, 그 이론은 다음과 같은 형태를 가져야 할 것입니다:

$$\nabla\cdot\mathbf{B} = \mu_0\,\rho_m \quad (\text{가상의 방정식, 실제로는 성립하지 않음})$$

$\nabla\cdot\mathbf{B}=0$이라는 것은 이 $\rho_m$이 **항등적으로 0**, 즉 우주 어디에도 자기 홀극이 존재하지 않는다는 것과 수학적으로 동치입니다.

## 4.4 적분형과의 관계 (발산 정리를 통한 연결)

$$\oint_S \mathbf{B}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{B})\, dV = 0$$

이 식이 의미하는 바: **어떤 폐곡면을 잡더라도, 그 곡면을 뚫고 나가는 자기력선의 수(밖으로)와 들어오는 자기력선의 수(안으로)가 정확히 같다.**

이것이 바로 "자석을 아무리 쪼개도 항상 N극과 S극이 쌍으로 나온다"는 익숙한 사실의 수학적 표현입니다. 막대자석 하나를 상상해보면:

- 자석 내부·외부를 관통하는 자기력선은 N극에서 **나가서** S극으로 **다시 들어오는 닫힌 루프**를 그립니다 (전기력선처럼 열린 선이 아니라, 시작도 끝도 없는 폐곡선).
- 이 자석 전체를 감싸는 임의의 폐곡면 $S$를 잡으면, 밖으로 나가는 힘선 개수(N극 쪽)와 다시 안으로 들어오는 힘선 개수(S극 쪽)가 정확히 상쇄되어 순 flux는 $0$이 됩니다.
- 폐곡면을 아무리 작게, N극 주변만 살짝 감싸도록 잡아도 마찬가지입니다 — N극만 감싸고 S극은 감싸지 않는 폐곡면을 만들 수 없기 때문입니다(N극만 "고립"시킬 수 없음). 이것이 바로 전하와의 결정적 차이입니다: 전하는 양전하만 감싸는 작은 폐곡면을 얼마든지 만들 수 있지만(그래서 $\oint\mathbf{E}\cdot d\mathbf{A}\neq 0$), 자석은 아무리 작게 쪼개도 항상 N-S 쌍이 함께 나옵니다.

## 4.5 대응 관계표

| | 전기장 | 자기장 |
|---|---|---|
| 미분형 | $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ | $\nabla\cdot\mathbf{B} = 0$ |
| 적분형 | $\oint\mathbf{E}\cdot d\mathbf{A} = Q_{enc}/\varepsilon_0$ | $\oint\mathbf{B}\cdot d\mathbf{A} = 0$ |
| 힘선의 모양 | 전하에서 시작·끝나는 **열린 선** | 시작도 끝도 없는 **닫힌 루프** |
| 원천(source) | 전하 $\rho$ (고립 가능) | 자기 홀극 $\rho_m$ — **존재하지 않음** |
| 폐곡면으로 고립 가능? | 가능 (전하 하나만 감쌀 수 있음) | 불가능 (N,S는 항상 쌍) |

즉 $\nabla\cdot\mathbf{B}=0$은 단순히 "우연히 우변이 0인 방정식"이 아니라, **"자기 홀극이라는 것이 이 우주의 방정식 체계 안에 아예 자리가 없다"**는 것을 가장 압축된 형태로 진술하는 문장입니다. (참고로 이론적으로는 자기 홀극을 허용하는 확장 이론 — Dirac monopole — 도 존재하지만, 지금까지 실험적으로 발견된 적은 없습니다.)

---

# 5. 쿨롱 법칙 · 비오-사바르 법칙에서 처음부터 유도하는 과정

쿨롱 법칙과 비오-사바르 법칙은 각각 정지한 전하, 정상전류가 만드는 장에 대한 **실험 법칙**입니다. 이로부터 출발해서 Gauss 법칙과 (정자기학의) Ampère 법칙을 유도하는 과정을 보입니다. 이것이 바로 맥스웰 방정식의 "역사적 기원"입니다.

## Part A. 쿨롱 법칙 → Gauss 법칙

### A.1 점전하의 쿨롱 법칙

전하 $q$가 원점에 있을 때, 위치 $\mathbf{r}$에서의 전기장:

$$\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{\mathbf{r}}$$

이것은 순수하게 실험(Coulomb의 비틀림 저울 실험, 1785)으로 얻어진 법칙입니다.

### A.2 점전하를 감싸는 구면에 대한 flux 계산

전하 $q$를 중심으로 하는 반지름 $r$의 구면 $S$를 잡고 flux를 계산합니다. 구면 위 모든 점에서 $\mathbf{E}$는 $\hat{\mathbf{r}}$ 방향이고 면적요소 $d\mathbf{A}$도 $\hat{\mathbf{r}}$ 방향(구면의 바깥법선)이므로 $\mathbf{E}\cdot d\mathbf{A} = E\,dA$:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \oint_S \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\, dA = \frac{q}{4\pi\varepsilon_0 r^2}\oint_S dA$$

구의 표면적 $\oint_S dA = 4\pi r^2$이므로:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\varepsilon_0 r^2}\cdot 4\pi r^2 = \frac{q}{\varepsilon_0}$$

**핵심 관찰**: 결과에 $r$이 완전히 사라졌습니다. 즉 flux는 구의 반지름과 무관합니다. 이는 쿨롱 법칙의 $1/r^2$ 의존성과 구 표면적의 $r^2$ 의존성이 정확히 상쇄되기 때문입니다 — **역제곱 법칙의 필연적 귀결**입니다.

### A.3 임의의 폐곡면으로 확장 (입체각 논증)

구가 아닌 **임의의 모양**의 폐곡면 $S'$가 전하 $q$를 감싸는 경우를 봅시다. $S'$ 위의 작은 면적요소 $d\mathbf{A}$를 지나는 flux는:

$$d\Phi = \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf{r}}\cdot d\mathbf{A}}{r^2}$$

여기서 $\hat{\mathbf{r}}\cdot d\mathbf{A}/r^2$는 정확히 그 면적요소가 전하 위치에서 바라볼 때 차지하는 **입체각(solid angle)** $d\Omega$의 정의입니다:

$$d\Omega \equiv \frac{\hat{\mathbf{r}}\cdot d\mathbf{A}}{r^2}$$

따라서:

$$d\Phi = \frac{q}{4\pi\varepsilon_0}\,d\Omega$$

폐곡면 전체에 대해 적분하면, 전하를 감싸는 폐곡면이 입체각으로 보는 전체 공간은 항상 $4\pi$ 스테라디안이므로:

$$\Phi = \oint_{S'} d\Phi = \frac{q}{4\pi\varepsilon_0}\oint d\Omega = \frac{q}{4\pi\varepsilon_0}\cdot 4\pi = \frac{q}{\varepsilon_0}$$

**즉 곡면의 모양이 구든 울퉁불퉁하든, flux는 정확히 $q/\varepsilon_0$로 동일합니다.** (만약 전하가 곡면 바깥에 있다면, 곡면을 "들어가는" 입체각과 "나가는" 입체각이 정확히 상쇄되어 순 flux는 $0$이 됩니다 — 폐곡면 바깥의 전하는 flux에 기여하지 않음.)

### A.4 중첩의 원리로 다중 전하 → 연속 전하분포로 확장

전기장은 선형이므로(맥스웰 방정식 이전에 이미 알려진 실험적 사실), 여러 전하 $q_1, q_2, \ldots$가 있으면 전체 장은 각 장의 벡터합입니다:

$$\mathbf{E} = \sum_i \mathbf{E}_i$$

폐곡면 $S$에 대해 flux도 선형이므로:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \sum_i \oint_S \mathbf{E}_i\cdot d\mathbf{A} = \sum_{i:\, q_i \text{ 내부}} \frac{q_i}{\varepsilon_0} = \frac{Q_{enc}}{\varepsilon_0}$$

(바깥에 있는 전하는 A.3에서 보였듯 기여가 $0$이므로 합에서 자동으로 빠집니다.) 연속적인 전하분포 $\rho(\mathbf{r})$의 경우 $Q_{enc} = \int_V \rho\,dV$로 바뀌어:

$$\boxed{\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{1}{\varepsilon_0}\int_V \rho\, dV} \quad \text{(적분형 Gauss 법칙)}$$

### A.5 미분형으로 변환

발산 정리 $\oint_S\mathbf{E}\cdot d\mathbf{A} = \int_V(\nabla\cdot\mathbf{E})dV$를 적용하고 "임의의 부피" 논증(1.1절 참조)을 쓰면:

$$\boxed{\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}}$$

**요약**: 쿨롱 법칙의 $1/r^2$ 의존성 → 입체각이 항상 $4\pi$라는 기하학적 사실 → flux가 곡면 모양과 무관하다는 결론 → Gauss 법칙. **Gauss 법칙은 쿨롱 법칙과 동등한 정보를 담고 있지만, "역제곱"이라는 구체적 형태 대신 "발산이 전하밀도에 비례한다"는 국소적 진술로 재포장한 것**입니다.

## Part B. 비오-사바르 법칙 → (정자기학) Ampère 법칙

### B.1 비오-사바르 법칙

정상전류(steady current, $\partial\rho/\partial t=0$) 밀도 $\mathbf{J}(\mathbf{r}')$가 만드는 자기장:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\times\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^3}\, dV'$$

이것도 쿨롱 법칙과 마찬가지로 순수 실험 법칙입니다 (Biot & Savart, 1820, Ørsted의 발견 직후).

### B.2 벡터 포텐셜 표현으로 전환 (계산을 쉽게 하기 위한 트릭)

직접 curl을 계산하기 전에, 다음 수학적 사실을 이용합니다:

$$\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^3} = -\nabla\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right)$$

(여기서 $\nabla$는 $\mathbf{r}$에 대한 미분이며, $\mathbf{r}'$는 적분변수로 취급되어 고정됨.) 이를 대입하면:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\times\left[-\nabla\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right]dV' = \frac{\mu_0}{4\pi}\int_V \nabla\frac{1}{|\mathbf{r}-\mathbf{r}'|}\times\mathbf{J}(\mathbf{r}')\,dV'$$

벡터 항등식 $\nabla f\times\mathbf{c} = -\nabla\times(f\mathbf{c})$ ($\mathbf{c}$가 $\mathbf{r}$에 무관한 상수 벡터일 때, 여기선 $\mathbf{J}(\mathbf{r}')$가 $\mathbf{r}$의 함수가 아니므로 성립)를 적용해 정리하면 결국:

$$\mathbf{B}(\mathbf{r}) = \nabla\times\left[\frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\,dV'\right] \equiv \nabla\times\mathbf{A}(\mathbf{r})$$

여기서 **벡터 포텐셜**을 다음과 같이 정의했습니다:

$$\mathbf{A}(\mathbf{r}) \equiv \frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\, dV'$$

($\nabla\times\nabla f \equiv 0$이므로 $\mathbf{B}=\nabla\times\mathbf{A}$ 형태로 쓰면 $\nabla\cdot\mathbf{B}=\nabla\cdot(\nabla\times\mathbf{A})=0$이 자동으로 성립함을 주목하세요 — 이것이 바로 Gauss 법칙(자기)이 비오-사바르 법칙에 이미 내포되어 있다는 증거입니다.)

### B.3 B의 컬(curl) 계산

이제 목표는 $\nabla\times\mathbf{B} = \nabla\times(\nabla\times\mathbf{A})$를 계산하는 것입니다. curl-of-curl 항등식을 씁니다:

$$\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$$

**Coulomb 게이지**: $\mathbf{A}$의 정의로부터 $\nabla\cdot\mathbf{A}=0$임을 보일 수 있습니다 (정상전류 조건 $\nabla\cdot\mathbf{J}=0$을 이용해 부분적분으로 증명 가능하나, 여기서는 결과만 사용). 따라서 첫 항이 사라지고:

$$\nabla\times\mathbf{B} = -\nabla^2\mathbf{A} = -\frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\,\nabla^2\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right)dV'$$

### B.4 델타함수 항등식 (전위 이론의 핵심 결과)

여기서 정전기학(포텐셜 이론)에서 잘 알려진 항등식을 사용합니다:

$$\nabla^2\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right) = -4\pi\,\delta^3(\mathbf{r}-\mathbf{r}')$$

(이 항등식은 $\mathbf{r}\neq\mathbf{r}'$일 때 $1/|\mathbf{r}-\mathbf{r}'|$가 라플라스 방정식을 만족한다는 사실과, 원점 근방에서 작은 구에 대해 발산 정리를 적용해 $-4\pi$라는 계수가 나온다는 사실로 증명됩니다. 이는 정전기학에서 점전하의 포텐셜 $\phi = q/(4\pi\varepsilon_0 r)$가 Gauss 법칙 $\nabla^2\phi = -\rho/\varepsilon_0$을 만족해야 한다는 요구조건과 본질적으로 동일한 수학입니다.)

이를 대입하면:

$$\nabla\times\mathbf{B} = -\frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\left[-4\pi\,\delta^3(\mathbf{r}-\mathbf{r}')\right]dV' = \mu_0\int_V \mathbf{J}(\mathbf{r}')\,\delta^3(\mathbf{r}-\mathbf{r}')\,dV'$$

델타함수의 정의(체 걸러내기 성질, sifting property)에 의해 적분이 즉시 계산됩니다:

$$\boxed{\nabla\times\mathbf{B} = \mu_0\mathbf{J}(\mathbf{r})} \quad \text{(미분형, 정자기학 Ampère 법칙)}$$

### B.5 적분형으로 변환

스토크스 정리를 적용하면:

$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \int_S(\nabla\times\mathbf{B})\cdot d\mathbf{A} = \mu_0\int_S \mathbf{J}\cdot d\mathbf{A} = \mu_0 I_{enc}$$

$$\boxed{\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc}} \quad \text{(적분형, 정자기학 Ampère 법칙)}$$

## 5.6 전체 논리 흐름의 대칭적 요약

| | 전기 (Part A) | 자기 (Part B) |
|---|---|---|
| 출발 실험법칙 | 쿨롱 법칙 $\mathbf{E}\propto \hat{\mathbf{r}}/r^2$ | 비오-사바르 법칙 $\mathbf{B}\propto \mathbf{J}\times\hat{\mathbf{r}}/r^2$ |
| 핵심 기하학적 사실 | 입체각의 총합 $=4\pi$ | 그린함수 $\nabla^2(1/r) = -4\pi\delta^3$ |
| 중간 결과 | 폐곡면 flux $=q/\varepsilon_0$, 곡면 모양 무관 | $\mathbf{B}=\nabla\times\mathbf{A}$, $\nabla\cdot\mathbf{B}=0$ 자동 성립 |
| 최종 미분형 | $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ | $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ |
| 담당 적분정리 | 발산 정리 | 스토크스 정리 |

이렇게 얻은 두 법칙 — $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$과 $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ — 이 바로 **맥스웰 이전** 단계의 정전기학·정자기학 법칙입니다. 여기에 Faraday의 유도 법칙(실험적 발견, $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$)을 추가하고, 2절에서 다룬 **변위전류 보정**($\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$)을 가하면, 비로소 완전한 맥스웰 방정식 4개가 완성됩니다.

즉 전체 역사적·논리적 계보는:

$$\text{쿨롱 법칙} \to \text{Gauss 법칙(E)}, \qquad \text{비오-사바르 법칙} \to \text{Ampère 법칙(정적)} \to \text{(변위전류 추가)} \to \text{Ampère–Maxwell 법칙}$$

이 네 단계가 합쳐져 맥스웰 방정식이라는 하나의 완결된 체계를 이룹니다.

---

# 6. 상대론적 공변형식과 4-벡터 표기

맥스웰 방정식 네 개가 사실은 **단 두 개의 4차원 텐서 방정식**으로 압축된다는 것을 보입니다. 이것이 특수상대론과 전자기학이 애초에 "한 몸"이었다는 것을 가장 극명하게 드러내는 대목입니다.

## 6.0 표기법 정리 (Minkowski 시공간)

계량(metric)은 $(+,-,-,-)$ 부호를 사용합니다:

$$\eta_{\mu\nu} = \text{diag}(1,-1,-1,-1)$$

4차원 좌표: $x^\mu = (ct, x, y, z)$, $\mu = 0,1,2,3$

편미분 연산자 (아래첨자, covariant):
$$\partial_\mu \equiv \frac{\partial}{\partial x^\mu} = \left(\frac{1}{c}\frac{\partial}{\partial t}, \nabla\right)$$

위첨자(contravariant) 미분연산자:
$$\partial^\mu = \eta^{\mu\nu}\partial_\nu = \left(\frac{1}{c}\frac{\partial}{\partial t}, -\nabla\right)$$

아인슈타인 합 규약(반복된 위·아래 인덱스는 자동으로 합산)을 사용합니다.

## 6.1 4-전위(Four-potential)의 도입

**동기**: $\nabla\cdot\mathbf{B}=0$은 항등식 $\nabla\cdot(\nabla\times\mathbf{A})\equiv 0$에 의해, 벡터 포텐셜 $\mathbf{A}$를 도입하면

$$\mathbf{B} = \nabla\times\mathbf{A}$$

로 두면 자동으로 만족됩니다. 이를 Faraday 법칙 $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$에 대입하면:

$$\nabla\times\mathbf{E} = -\frac{\partial}{\partial t}(\nabla\times\mathbf{A}) = -\nabla\times\frac{\partial\mathbf{A}}{\partial t}$$

$$\nabla\times\left(\mathbf{E}+\frac{\partial\mathbf{A}}{\partial t}\right) = 0$$

컬이 0인 벡터장은 어떤 스칼라 함수의 그래디언트로 쓸 수 있으므로 ($\nabla\times\nabla\phi\equiv 0$):

$$\mathbf{E} + \frac{\partial\mathbf{A}}{\partial t} = -\nabla\phi \quad\Longrightarrow\quad \mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}$$

이렇게 스칼라 포텐셜 $\phi$와 벡터 포텐셜 $\mathbf{A}$를 도입하면, **Gauss(자기) 법칙과 Faraday 법칙(동차 방정식 두 개)이 자동으로, 항등적으로 만족**됩니다.

**핵심 관찰**: $\phi$와 $\mathbf{A}$는 정확히 4개의 성분을 가지며, 이를 다음과 같이 하나의 4-벡터로 묶을 수 있습니다:

$$A^\mu \equiv \left(\frac{\phi}{c}, \mathbf{A}\right)$$

이것이 실제로 로런츠 변환 하에서 4-벡터처럼 변환한다는 것은 별도로 증명이 필요하지만(상대론적 전자기학의 표준 결과), 여기서는 이 구성을 받아들이고 그 귀결을 따라가겠습니다.

## 6.2 전자기장 텐서 (Faraday tensor)의 정의

$$F^{\mu\nu} \equiv \partial^\mu A^\nu - \partial^\nu A^\mu$$

이는 정의상 **반대칭 텐서**($F^{\mu\nu}=-F^{\nu\mu}$, 따라서 대각성분은 모두 0)이며, $4\times4$ 행렬이 반대칭이므로 독립성분은 $6$개입니다 — 정확히 $\mathbf{E}$의 3성분과 $\mathbf{B}$의 3성분의 개수와 일치합니다.

### 6.2.1 성분을 직접 계산

$F^{0i}$ 성분을 계산합니다 ($i=1,2,3$은 공간성분):

$$F^{0i} = \partial^0 A^i - \partial^i A^0$$

$\partial^0 = \frac{1}{c}\partial_t$, $\partial^i = -\partial_i$ (공간 미분의 위첨자는 부호가 뒤집힘), $A^i = A_i$(3-벡터 $\mathbf{A}$의 성분), $A^0 = \phi/c$이므로:

$$F^{0i} = \frac{1}{c}\frac{\partial A^i}{\partial t} - (-\partial_i)\frac{\phi}{c} = \frac{1}{c}\left(\frac{\partial A^i}{\partial t} + \partial_i \phi\right) = -\frac{1}{c}\left(-\partial_i\phi - \frac{\partial A^i}{\partial t}\right) = -\frac{E^i}{c}$$

(마지막 단계에서 $\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$의 정의를 사용했습니다.) 즉:

$$F^{0i} = -\frac{E_i}{c}, \qquad F^{i0} = \frac{E_i}{c}$$

이제 $F^{ij}$ 성분($i,j$ 모두 공간):

$$F^{ij} = \partial^i A^j - \partial^j A^i = -\partial_i A^j + \partial_j A^i = -(\partial_i A_j - \partial_j A_i)$$

이는 정확히 $\mathbf{B}=\nabla\times\mathbf{A}$의 성분, 즉 $B_k = \epsilon_{kij}\partial_i A_j$ (Levi-Civita 기호 사용)와 연결됩니다. 구체적으로 계산하면:

$$F^{12} = -(\partial_1 A_2 - \partial_2 A_1) = -B_3, \quad F^{23} = -B_1, \quad F^{31} = -B_2$$

### 6.2.2 완성된 행렬 형태

$$F^{\mu\nu} = \begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{pmatrix}$$

이 하나의 텐서 안에 $\mathbf{E}$와 $\mathbf{B}$가 모두 담겨 있습니다 — **전기장과 자기장은 별개의 독립적인 장이 아니라, 하나의 시공간 텐서 $F^{\mu\nu}$를 관찰자의 기준틀에 따라 "시간-공간" 성분과 "공간-공간" 성분으로 나눈 것**에 불과합니다. (실제로 로런츠 부스트를 가하면 $\mathbf{E}$와 $\mathbf{B}$가 서로 섞입니다 — 이것이 "전자기장"이라는 이름이 단일 개체를 가리키는 진짜 이유입니다.)

## 6.3 동차 맥스웰 방정식 (Gauss-B, Faraday) → Bianchi 항등식

$F^{\mu\nu}=\partial^\mu A^\nu - \partial^\nu A^\mu$로 정의했다는 사실 자체로부터, 다음이 **항등적으로** 성립합니다 (편미분의 교환 가능성 $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$에서 유도):

$$\boxed{\partial^\lambda F^{\mu\nu} + \partial^\mu F^{\nu\lambda} + \partial^\nu F^{\lambda\mu} = 0} \quad \text{(Bianchi 항등식)}$$

**증명**: $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$를 대입하면

$$\partial^\lambda(\partial^\mu A^\nu - \partial^\nu A^\mu) + \partial^\mu(\partial^\nu A^\lambda - \partial^\lambda A^\nu) + \partial^\nu(\partial^\lambda A^\mu - \partial^\mu A^\lambda)$$

각 항을 전개하면 $\partial^\lambda\partial^\mu A^\nu$, $-\partial^\lambda\partial^\nu A^\mu$, $\partial^\mu\partial^\nu A^\lambda$, $-\partial^\mu\partial^\lambda A^\nu$, $\partial^\nu\partial^\lambda A^\mu$, $-\partial^\nu\partial^\mu A^\lambda$의 6개 항이 나오는데, 편미분의 교환법칙에 의해 이들이 정확히 두 개씩 짝지어 상쇄됩니다 ($\partial^\lambda\partial^\mu A^\nu$와 $-\partial^\mu\partial^\lambda A^\nu$가 상쇄, 등). 따라서 전체는 $0$입니다. $\blacksquare$

**이 하나의 항등식이 Gauss 법칙(자기)과 Faraday 법칙을 모두 포함합니다.** 인덱스 $(\lambda,\mu,\nu)=(1,2,3)$을 대입하면 $\nabla\cdot\mathbf{B}=0$이, $(\lambda,\mu,\nu)$에 시간성분 $0$이 하나 섞이면 Faraday 법칙이 나옵니다.

## 6.4 비동차 맥스웰 방정식 (Gauss-E, Ampère-Maxwell)

### 6.4.1 4-전류(Four-current)의 정의

$$J^\mu \equiv (c\rho, \mathbf{J})$$

이것이 4-벡터로 변환한다는 사실은 전하 보존이 로런츠 불변이어야 한다는 요구에서 나옵니다.

### 6.4.2 공변형 방정식

나머지 두 방정식(Gauss-E, Ampère-Maxwell)은 다음 하나의 텐서 방정식으로 통합됩니다:

$$\boxed{\partial_\mu F^{\mu\nu} = \mu_0 J^\nu}$$

### 6.4.3 성분별로 풀어서 원래 방정식 복원

**$\nu=0$ 성분**:
$$\partial_\mu F^{\mu 0} = \mu_0 J^0$$
$$\partial_0 F^{00} + \partial_i F^{i0} = \mu_0 (c\rho)$$

$F^{00}=0$(반대칭이므로 대각성분은 0), $F^{i0}=E_i/c$이므로:

$$\partial_i\left(\frac{E_i}{c}\right) = \mu_0 c\rho \quad\Longrightarrow\quad \nabla\cdot\mathbf{E} = \mu_0 c^2 \rho$$

$\mu_0 c^2 = \mu_0\cdot\dfrac{1}{\mu_0\varepsilon_0} = \dfrac{1}{\varepsilon_0}$ (여기서 $c^2=1/\mu_0\varepsilon_0$, 3절에서 유도한 관계 사용)이므로:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \quad \checkmark \text{Gauss 법칙(전기)}$$

**$\nu=k$ (공간성분, $k=1,2,3$)**:
$$\partial_\mu F^{\mu k} = \mu_0 J^k = \mu_0 J_k$$
$$\partial_0 F^{0k} + \partial_j F^{jk} = \mu_0 J_k$$

$F^{0k}=-E_k/c$, $\partial_0 = \frac1c\partial_t$이므로 첫 항은 $-\dfrac{1}{c^2}\dfrac{\partial E_k}{\partial t}$. $F^{jk}$는 $-\epsilon_{jkl}B_l$ 형태이므로 두 번째 항은 $(\nabla\times\mathbf{B})_k$에 해당(부호 정리 후). 정리하면:

$$(\nabla\times\mathbf{B})_k - \frac{1}{c^2}\frac{\partial E_k}{\partial t} = \mu_0 J_k$$

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \frac{1}{c^2}\frac{\partial\mathbf{E}}{\partial t} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \checkmark \text{Ampère–Maxwell 법칙}$$

**즉 맥스웰 방정식 4개 전부가 단 두 개의 텐서 방정식으로 압축됩니다:**

$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad (\text{비동차, 2개 방정식}) \qquad\qquad \partial^{[\lambda}F^{\mu\nu]}=0 \quad (\text{동차, 2개 방정식})$$

## 6.5 전하 보존 = 4-발산 = 0 (자동 도출)

$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$의 양변에 다시 $\partial_\nu$를 취하면:

$$\partial_\nu\partial_\mu F^{\mu\nu} = \mu_0\,\partial_\nu J^\nu$$

좌변에서 $\partial_\nu\partial_\mu$는 $\mu,\nu$에 대해 대칭(미분 교환 가능)인데 $F^{\mu\nu}$는 반대칭이므로, 대칭×반대칭의 축약은 항등적으로 $0$입니다:

$$\partial_\nu\partial_\mu F^{\mu\nu} = 0 \quad\Longrightarrow\quad \partial_\nu J^\nu = 0$$

이를 성분으로 풀면:

$$\partial_\nu J^\nu = \partial_0 J^0 + \partial_i J^i = \frac{1}{c}\partial_t(c\rho) + \nabla\cdot\mathbf{J} = \frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J} = 0$$

즉 **전하 보존 법칙이 $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$라는 방정식의 수학적 구조(반대칭성) 자체에서 자동으로 따라나옵니다.** 이는 2절에서 "변위전류를 손으로 끼워맞춰야 전하보존과 일치시켰던" 과정이, 공변형식에서는 애초에 **필요조차 없게** 자동으로 내장되어 있다는 뜻입니다 — 공변형식의 우아함을 보여주는 대표적 사례입니다.

## 6.6 로런츠 게이지와 파동방정식의 공변형 유도

$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$를 $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$에 대입:

$$\partial_\mu(\partial^\mu A^\nu - \partial^\nu A^\mu) = \mu_0 J^\nu$$

$$\partial_\mu\partial^\mu A^\nu - \partial^\nu(\partial_\mu A^\mu) = \mu_0 J^\nu$$

**로런츠 게이지 조건**을 부과합니다 (게이지 자유도를 이용한 선택):

$$\partial_\mu A^\mu = 0 \quad\Longleftrightarrow\quad \frac{1}{c^2}\frac{\partial\phi}{\partial t} + \nabla\cdot\mathbf{A} = 0$$

그러면 두 번째 항이 사라지고:

$$\partial_\mu\partial^\mu A^\nu = \mu_0 J^\nu$$

여기서 $\partial_\mu\partial^\mu \equiv \Box$ 는 **달랑베르시안(d'Alembertian)**이라 불리는 연산자로:

$$\Box \equiv \partial_\mu\partial^\mu = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2$$

따라서:

$$\boxed{\Box A^\nu = \mu_0 J^\nu}$$

진공($J^\nu=0$)에서는:

$$\Box A^\nu = 0 \quad\Longrightarrow\quad \nabla^2 A^\nu - \frac{1}{c^2}\frac{\partial^2 A^\nu}{\partial t^2}=0$$

이는 3절에서 $\mathbf{E}$, $\mathbf{B}$에 대해 따로따로 유도했던 파동방정식을, $A^\nu$(따라서 $\phi,\mathbf{A}$)에 대해 **단 하나의 4-벡터 방정식**으로 통합한 것입니다. 게다가 $\Box$가 로런츠 불변 연산자이므로, 이 파동방정식이 모든 관성계에서 동일한 형태를 가진다는 것, 즉 **빛의 속도 $c$가 모든 관성계에서 같다**는 특수상대론의 두 번째 공준이 전자기 이론 안에 이미 내장되어 있었다는 것이 드러납니다.

## 6.7 로렌츠 힘의 공변형

마지막으로, 전하 $q$, 4-속도 $u^\mu = \gamma(c,\mathbf{v})$를 갖는 입자의 운동방정식(로렌츠 힘)도 공변형으로 쓸 수 있습니다:

$$\boxed{\frac{dp^\mu}{d\tau} = q\,F^{\mu\nu}u_\nu}$$

여기서 $p^\mu$는 4-운동량, $\tau$는 고유시간입니다. 공간성분($\mu=i$)을 풀어보면 정확히 익숙한 $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$가 복원됩니다 — 즉 전자기장이 입자에 미치는 힘까지 포함해서, 전자기학 전체가 $F^{\mu\nu}$라는 단일 텐서로 완결됩니다.

## 6.8 총정리

| 3차원 형태 (4개 방정식) | 4차원 공변형 (2개 방정식) |
|---|---|
| $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ 의 $\nu=0$ |
| $\nabla\times\mathbf{B}-\frac{1}{c^2}\partial_t\mathbf{E}=\mu_0\mathbf{J}$ | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ 의 $\nu=i$ |
| $\nabla\cdot\mathbf{B}=0$ | Bianchi 항등식의 공간성분 |
| $\nabla\times\mathbf{E}+\partial_t\mathbf{B}=0$ | Bianchi 항등식의 시공간 혼합성분 |

이 압축이 단순한 "표기의 편의"가 아닌 이유는, $F^{\mu\nu}$가 로런츠 변환에 대해 **텐서로서 정확하게** 변환한다는 사실 때문입니다. 즉 한 관성계에서 순수한 전기장으로 보이는 것이 다른 관성계에서는 전기장+자기장의 혼합으로 보일 수 있는데($\mathbf{E},\mathbf{B}$가 뒤섞임), $F^{\mu\nu}$ 전체는 하나의 기하학적 대상으로서 그 변환을 일관되게 기술합니다. 이것이 맥스웰이 (무의식적으로) 특수상대론을 이미 자신의 방정식 안에 심어두었다는, 아인슈타인이 1905년에 명시적으로 드러낸 사실의 수학적 실체입니다.

---

# 7. 게이지 변환의 상세 증명 및 현대 확장

게이지 변환은 "같은 물리적 상황을 서로 다른 수식으로 표현할 수 있는 자유도"입니다. 이 자유도가 왜 존재하는지, $F^{\mu\nu}$가 왜 불변인지 엄밀히 증명하고, 이것이 현대 물리학(양자역학, 표준모형)으로 어떻게 확장되는지까지 다룹니다.

## Part 1. 게이지 변환의 정의와 기원

### 1.1 게이지 자유도가 생기는 이유

$\mathbf{B}=\nabla\times\mathbf{A}$로 정의했을 때, 벡터 항등식 $\nabla\times(\nabla f)\equiv 0$ (임의의 스칼라함수 $f$)에 의해:

$$\mathbf{A}' = \mathbf{A} + \nabla\chi$$

로 바꿔도 $\nabla\times\mathbf{A}' = \nabla\times\mathbf{A} + \nabla\times(\nabla\chi) = \nabla\times\mathbf{A} = \mathbf{B}$, 즉 **동일한 $\mathbf{B}$**를 줍니다. 4차원 표기로는 정확히 이것이:

$$A^\mu \to A'^\mu = A^\mu + \partial^\mu\lambda$$

($\lambda$는 시공간 좌표 $x^\mu$에 대한 임의의 스칼라 함수 — "게이지 함수")

**직관**: $A^\mu$ 자체는 "실재하는" 물리량이 아니라 계산 편의를 위한 보조 변수이고, 실제로 측정 가능한 것은 $\mathbf{E},\mathbf{B}$(즉 $F^{\mu\nu}$)뿐입니다. $A^\mu$에서 $F^{\mu\nu}$로 가는 사상(mapping)은 **일대일이 아니라 다대일**이므로, 같은 $F^{\mu\nu}$를 주는 $A^\mu$들이 무수히 많이 존재하는 것입니다.

### 1.2 $F^{\mu\nu}$의 게이지 불변성 — 엄밀한 증명

**주장**: $F^{\mu\nu}=\partial^\mu A^\nu - \partial^\nu A^\mu$는 $A^\mu\to A^\mu+\partial^\mu\lambda$ 변환 하에서 불변이다.

**증명**: 변환된 텐서를 직접 계산합니다.

$$F'^{\mu\nu} = \partial^\mu A'^\nu - \partial^\nu A'^\mu = \partial^\mu(A^\nu+\partial^\nu\lambda) - \partial^\nu(A^\mu+\partial^\mu\lambda)$$

$$= \partial^\mu A^\nu - \partial^\nu A^\mu + \partial^\mu\partial^\nu\lambda - \partial^\nu\partial^\mu\lambda$$

$$= F^{\mu\nu} + \left(\partial^\mu\partial^\nu\lambda - \partial^\nu\partial^\mu\lambda\right)$$

$\lambda$가 매끄러운(smooth) 함수라면 편미분은 순서에 무관하게 교환 가능합니다 (Clairaut/Schwarz 정리):

$$\partial^\mu\partial^\nu\lambda = \partial^\nu\partial^\mu\lambda$$

따라서 괄호 안은 항등적으로 $0$이고:

$$\boxed{F'^{\mu\nu} = F^{\mu\nu}}$$

$\blacksquare$

**즉 게이지 변환의 "핵심 메커니즘"은 정확히 편미분의 교환법칙입니다.** 이것이 3차원에서 $\nabla\times\nabla\chi=0$이었던 사실의 4차원 버전입니다.

### 1.3 3차원 성분으로 직접 재확인

4차원 게이지 변환 $A^\mu\to A^\mu+\partial^\mu\lambda$를 성분으로 풀면:

$$A^0 \to A^0 + \partial^0\lambda = \frac{\phi}{c} + \frac{1}{c}\frac{\partial\lambda}{\partial t} \quad\Longrightarrow\quad \phi\to\phi+\frac{\partial\lambda}{\partial t}$$

$$A^i \to A^i + \partial^i\lambda = A^i - \partial_i\lambda \quad\Longrightarrow\quad \mathbf{A}\to\mathbf{A}-\nabla\lambda$$

(부호가 뒤집히는 것은 $\partial^i=-\partial_i$이기 때문. 관례에 따라 $\chi\equiv-\lambda$로 다시 정의하면 익숙한 형태가 됩니다.) 표준적으로는:

$$\mathbf{A}\to\mathbf{A}+\nabla\chi, \qquad \phi\to\phi-\frac{\partial\chi}{\partial t}$$

이제 $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$에 직접 대입해서 불변성을 재확인합니다:

$$\mathbf{E}' = -\nabla\left(\phi-\frac{\partial\chi}{\partial t}\right) - \frac{\partial}{\partial t}\left(\mathbf{A}+\nabla\chi\right)$$

$$= -\nabla\phi + \nabla\frac{\partial\chi}{\partial t} - \frac{\partial\mathbf{A}}{\partial t} - \frac{\partial}{\partial t}\nabla\chi$$

$\nabla$와 $\partial/\partial t$는 독립 변수에 대한 연산이므로 교환 가능, 따라서 $\nabla(\partial\chi/\partial t)$와 $-\partial(\nabla\chi)/\partial t$가 정확히 상쇄:

$$\mathbf{E}' = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t} = \mathbf{E} \quad\checkmark$$

$\mathbf{B}' = \nabla\times\mathbf{A}' = \nabla\times\mathbf{A}+\nabla\times(\nabla\chi) = \mathbf{B}$ (이미 1.1에서 확인) $\checkmark$

## Part 2. 게이지 고정 (Gauge Fixing)

$A^\mu$에 무한한 자유도가 있다는 것은, 실제 계산을 하려면 **하나의 대표(representative)를 골라야** 한다는 뜻입니다. 이를 "게이지를 고정한다"고 합니다.

### 2.1 로런츠 게이지 (Lorenz gauge)

$$\partial_\mu A^\mu = 0$$

**임의의 게이지에서 로런츠 게이지로 항상 이동 가능함을 증명**: 어떤 $A^\mu$가 $\partial_\mu A^\mu = f(x)\neq 0$이라 하더라도, 게이지 변환 $A'^\mu = A^\mu+\partial^\mu\lambda$을 적용하면:

$$\partial_\mu A'^\mu = \partial_\mu A^\mu + \partial_\mu\partial^\mu\lambda = f + \Box\lambda$$

이것이 $0$이 되도록 하려면 $\Box\lambda = -f$를 풀면 됩니다. 이는 소스가 있는 파동방정식이므로(그린함수 방법 등으로) **항상 해 $\lambda$가 존재**합니다. 따라서 어떤 $A^\mu$에서 출발해도 로런츠 게이지를 만족하는 $A'^\mu$로 옮겨갈 수 있습니다. 이 게이지의 장점: 로런츠 불변성이 명백하게 유지되어 상대론적 계산(6.6절의 $\Box A^\nu=\mu_0 J^\nu$)이 깔끔해집니다.

로런츠 게이지 자체도 완전히 유일하지는 않습니다 — $\Box\lambda=0$(파동방정식의 동차해)을 만족하는 **잔여 게이지 자유도**가 여전히 남아 있습니다.

### 2.2 쿨롱 게이지 (Coulomb gauge, radiation gauge)

$$\nabla\cdot\mathbf{A} = 0$$

이 게이지에서는 Gauss 법칙 $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$을 $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$에 대입하면:

$$-\nabla^2\phi - \frac{\partial}{\partial t}(\nabla\cdot\mathbf{A}) = \frac{\rho}{\varepsilon_0} \quad\Longrightarrow\quad \nabla^2\phi = -\frac{\rho}{\varepsilon_0}$$

즉 $\phi$가 **순간적으로(instantaneously)** $\rho$에 반응하는 정전기 포텐셜 형태로 나옵니다 (이는 물리적으로 정보가 초광속 전달되는 게 아니라, $\phi$ 자체가 게이지 의존적이라 직접 관측 불가능한 양이기 때문에 문제가 없습니다 — 관측 가능한 $\mathbf{E},\mathbf{B}$는 항상 인과적으로 전파됨). 이 게이지는 양자전기역학의 비상대론적 극한이나 다중극 전개에 유용합니다.

### 2.3 게이지 고정의 일반 원리

핵심 개념: 물리적 자유도(2개 편광의 광자)는 $A^\mu$의 4개 성분보다 적습니다. 게이지 대칭 때문에 2개의 "가짜(spurious)" 자유도(게이지 자유도 1개 + 그로 인한 구속조건 1개)가 있으며, 게이지를 고정한다는 것은 이 가짜 자유도를 제거해서 계산을 다루기 쉽게 만드는 절차입니다. 어떤 게이지를 쓰든 **물리적 관측량**($\mathbf{E},\mathbf{B}$, 그리고 입자의 궤적 등)은 항상 동일해야 하며, 이것이 이론이 "게이지 불변"이라는 것의 실질적 의미입니다.

## Part 3. 게이지 대칭과 전하 보존 — Noether 정리와의 연결

고전 전자기학에서는 게이지 대칭이 "여분의 수학적 자유도"처럼 보이지만, **양자역학과 결합하면 이 대칭이 전하 보존 법칙 자체의 근원**이 됩니다. Noether의 정리: 연속 대칭 ↔ 보존량. 게이지 대칭(전역 위상 대칭의 국소화, 아래에서 설명) ↔ 전하 보존. 이 연결이 다음 절의 핵심입니다.

## Part 4. 현대적 확장 (1): 양자역학과 국소 U(1) 게이지 대칭

### 4.1 문제의 재구성: 왜 전자기 상호작용이 존재하는가?

이것이 게이지 원리(gauge principle)의 현대적 관점입니다: 자유 전자의 슈뢰딩거(또는 디랙) 방정식은 파동함수의 **전역(global) 위상 변환**

$$\psi(x) \to e^{i\alpha}\psi(x) \quad (\alpha = \text{상수})$$

에 대해 불변합니다 ($|\psi|^2$만 물리적으로 의미가 있으므로). 이제 이 대칭을 **국소적(local)**으로 요구해봅시다 — 즉 위상 $\alpha$가 시공간 점마다 다를 수 있게:

$$\psi(x) \to e^{iq\alpha(x)/\hbar}\psi(x)$$

### 4.2 국소 대칭이 강제하는 것: 공변 미분

문제: 자유 입자의 라그랑지안(또는 슈뢰딩거 방정식)에는 $\partial_\mu\psi$ 항이 들어가는데,

$$\partial_\mu\left(e^{iq\alpha(x)/\hbar}\psi\right) = e^{iq\alpha/\hbar}\left(\partial_\mu\psi + \frac{iq}{\hbar}(\partial_\mu\alpha)\psi\right)$$

추가항 $\frac{iq}{\hbar}(\partial_\mu\alpha)\psi$가 남아서, 단순한 $\partial_\mu\psi$는 국소 위상변환 하에서 불변이 아닙니다. 이를 상쇄하려면 새로운 장 $A_\mu$를 도입해서 **공변미분(covariant derivative)**을 정의해야 합니다:

$$D_\mu \equiv \partial_\mu - \frac{iq}{\hbar}A_\mu$$

그리고 $A_\mu$가 다음과 같이 변환한다고 요구하면:

$$A_\mu \to A_\mu + \partial_\mu\alpha$$

(바로 이것이 Part 1의 게이지 변환입니다!) $D_\mu\psi$ 전체가 $\psi$와 똑같이 단순하게 변환함을 보일 수 있습니다:

$$D_\mu\psi \to e^{iq\alpha/\hbar}D_\mu\psi$$

**결론**: 파동함수의 위상을 시공간 점마다 자유롭게 바꿀 수 있으려면(국소 게이지 대칭을 요구하면), 전자기 벡터 포텐셜 $A_\mu$의 존재가 **수학적으로 강제**됩니다. 즉 전자기 상호작용은 "우연히 존재하는 힘"이 아니라 **국소 위상 대칭을 유지하기 위해 필연적으로 등장하는 것**이라는 것이 현대적 재해석입니다. 이것이 바로 맥스웰 방정식이 물리학에서 "게이지 이론"이라 불리는 이유이자, U(1) 게이지 이론이라 부르는 이유입니다 (위상변환 $e^{i\alpha}$의 집합이 $U(1)$ 군을 이루기 때문).

### 4.3 Aharonov–Bohm 효과: A^μ의 물리적 실재성

고전적으로는 $\mathbf{E}=\mathbf{B}=0$인 영역에서 $\mathbf{A}\neq0$이면 "아무 물리적 효과가 없다"고 생각하기 쉽지만, 양자역학에서는 $\mathbf{A}$가 파동함수의 위상에 직접 영향을 미칩니다:

$$\psi \to \psi\, \exp\left(\frac{iq}{\hbar}\int \mathbf{A}\cdot d\boldsymbol{\ell}\right)$$

솔레노이드(자기장이 내부에만 갇혀 있고 외부에는 $\mathbf{B}=0$이지만 $\mathbf{A}\neq0$인 영역) 주위로 전자를 두 경로로 보내 간섭시키면, $\mathbf{B}$가 $0$인 영역을 지났음에도 간섭무늬가 이동합니다 — 이는 실험적으로 확인된 사실(Aharonov-Bohm, 1959; Tonomura 등의 실험, 1980년대)입니다. 이는 $A^\mu$가 단순한 계산 편의 수단이 아니라, **위상수학적으로(topologically) 실제 물리적 정보를 담고 있음**을 보여줍니다 (다만 게이지 불변량인 $\oint\mathbf{A}\cdot d\boldsymbol{\ell}$, 즉 $\mathbf{A}$가 둘러싸는 자속(flux)만이 관측 가능하며, 이 특정 선적분 자체는 게이지 불변입니다).

## Part 5. 현대적 확장 (2): 비아벨 게이지 이론 (Yang–Mills)

### 5.1 U(1)에서 SU(N)으로

전자기학의 게이지군은 $U(1)$ — 즉 하나의 위상 $e^{i\alpha}$로, 곱셈이 **교환 가능(abelian)**합니다: $e^{i\alpha}e^{i\beta}=e^{i\beta}e^{i\alpha}$. 1954년 Yang과 Mills는 이를 **비아벨(non-abelian)** 군, 즉 원소끼리 곱셈이 교환되지 않는 군(예: $SU(2)$, $SU(3)$)으로 일반화했습니다.

$SU(N)$ 게이지 변환:
$$\psi \to U(x)\psi, \qquad U(x) = e^{ig\,\theta^a(x)T^a}$$

여기서 $T^a$는 군의 생성자(generator)들이고, $a=1,\ldots,N^2-1$입니다 (예: $SU(3)$는 8개 생성자 — 강한 상호작용의 8개 글루온에 대응). 공변미분은:

$$D_\mu = \partial_\mu - igA_\mu^a T^a$$

### 5.2 핵심적 차이: 장 텐서의 자체 상호작용

U(1)에서는 $F_{\mu\nu}=\partial_\mu A_\nu - \partial_\nu A_\mu$로 끝이지만, 비아벨의 경우 생성자들의 교환자(commutator) $[T^a,T^b]=if^{abc}T^c$가 $0$이 아니기 때문에 추가항이 생깁니다:

$$F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc}A_\mu^b A_\nu^c$$

이 추가항 $gf^{abc}A_\mu^bA_\nu^c$ 때문에 **게이지 보손(gauge boson) 자체가 서로 상호작용**합니다 — 이것이 글루온끼리 서로 상호작용하는 이유(강한 상호작용의 점근적 자유, color confinement 등 핵심 현상들의 근원)이며, 광자끼리는 서로 상호작용하지 않는(전자기학은 선형) 것과 결정적으로 다른 지점입니다.

### 5.3 표준모형에서의 위치

| 게이지군 | 매개 입자 | 대응 힘 |
|---|---|---|
| $U(1)_{EM}$ | 광자 | 전자기력 (맥스웰 방정식 그 자체) |
| $SU(2)_L\times U(1)_Y$ | $W^\pm, Z^0$, 광자 | 약전자기 통합이론 (Weinberg-Salam) |
| $SU(3)_C$ | 글루온 8개 | 강한 상호작용 (양자색역학, QCD) |

즉 맥스웰의 "게이지 대칭 → 힘의 존재"라는 발상이 표준모형 전체의 설계 원리로 확장되었습니다. 맥스웰 방정식은 이 계보에서 **가장 단순한($U(1)$) 특수 경우**에 해당합니다.

## Part 6. 현대적 확장 (3): 미분형식(Differential Forms)을 이용한 최종적 압축

가장 현대적이고 기하학적인 서술: $A^\mu$를 1-형식 $A = A_\mu dx^\mu$로, $F^{\mu\nu}$를 그 외미분(exterior derivative) $F=dA$로 씁니다. 게이지 변환은:

$$A \to A + d\lambda$$

이고,

$$F=dA \to d(A+d\lambda) = dA + d(d\lambda) = dA = F$$

($d^2\equiv0$이라는 외미분의 기본 성질 — 이것이 Part 1.2에서 증명한 "편미분의 교환법칙"의 좌표계 독립적 버전입니다.) 동차 방정식(Bianchi 항등식)은 단순히 $dF=0$이고, 비동차 방정식은 $d\star F = \mu_0 J$($\star$는 Hodge 쌍대 연산자)로 쓰입니다. 이 언어는 좌표계에 전혀 의존하지 않고 곡률(curvature) 개념으로 직결되어, 일반상대론의 리만 곡률 텐서와 정확히 평행한 구조를 이룹니다 — **게이지장은 기하학적으로 "접속(connection)"이고, $F^{\mu\nu}$는 그 "곡률"**이라는 것이 현대 미분기하학적 관점입니다.

## 7.7 총정리

| 단계 | 내용 |
|---|---|
| 고전 게이지 대칭 | $A^\mu\to A^\mu+\partial^\mu\lambda$, $F^{\mu\nu}$ 불변 (편미분 교환법칙에서 유도) |
| 게이지 고정 | 로런츠 게이지($\partial_\mu A^\mu=0$), 쿨롱 게이지($\nabla\cdot\mathbf{A}=0$) 등 |
| 양자역학적 재해석 | 국소 $U(1)$ 위상대칭 요구 ⇒ $A_\mu$의 존재가 강제됨 (게이지 원리) |
| 실험적 확인 | Aharonov–Bohm 효과 — $A^\mu$가 topologically 실재함을 입증 |
| 비아벨 확장 | Yang–Mills 이론 — $SU(N)$, 게이지 보손 자체상호작용, 표준모형의 기초 |
| 기하학적 완성 | $A=$ 접속, $F=dA=$ 곡률 — 미분형식·섬유다발 이론으로 통합 |

맥스웰 방정식의 게이지 대칭은 처음엔 "계산의 여분 자유도"처럼 보이지만, 20세기를 거치며 **모든 기본 상호작용(전자기력, 약력, 강력)을 구성하는 근본 원리**로 밝혀졌습니다. "게이지 대칭을 요구하면 힘이 필연적으로 등장한다"는 이 발상은, 맥스웰이 $\nabla\times\mathbf{A}$라는 단순한 수학적 트릭을 도입한 데서 시작해 현대 입자물리학의 표준모형 전체를 떠받치는 핵심 원리로 성장했습니다.

---

## 전체 요약: 하나의 이야기로 본 맥스웰 방정식

1. **미분형·적분형**은 발산 정리와 스토크스 정리, 그리고 "임의의 영역" 논증으로 완전히 동치임이 증명됩니다.
2. **변위전류**는 전하 보존 법칙과 원래 Ampère 법칙 사이의 모순을 해소하기 위해 수학적으로 **필연적으로** 요구되는 항입니다.
3. 완성된 네 방정식을 진공에서 결합하면 **파동방정식**이 튀어나오고, 그 속도가 독립적으로 측정된 **빛의 속도와 정확히 일치**함으로써 "빛 = 전자기파"라는 결론에 도달합니다.
4. $\nabla\cdot\mathbf{B}=0$은 **자기 홀극의 부재**를 가장 압축적으로 표현하는 방정식입니다.
5. 네 방정식은 애초에 **쿨롱 법칙과 비오-사바르 법칙**이라는 정적 실험 법칙에서 발산 정리·스토크스 정리·델타함수 항등식을 통해 유도된 것입니다.
6. 특수상대론의 언어로 옮기면, 네 방정식은 **두 개의 텐서 방정식**($\partial_\mu F^{\mu\nu}=\mu_0J^\nu$와 Bianchi 항등식)으로 압축되며, 전하 보존이 자동으로 내장됩니다.
7. 이 구조의 밑바탕에 있는 **게이지 대칭**은 고전적으로는 계산의 자유도이지만, 양자역학과 결합하면 전자기 상호작용의 존재 자체를 강제하는 원리(게이지 원리)로 재해석되며, 이는 Yang-Mills 이론을 거쳐 현대 표준모형 전체의 설계 원리로 확장됩니다.
