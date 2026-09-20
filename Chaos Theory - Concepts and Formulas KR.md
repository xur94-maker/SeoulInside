# 부록 E: 더 읽어보기

## E.1 전이 카오스와 카오스 안장점 — 21.9절

본문 21.9절에서 우리는 Motter 등(2013)의 "이중 전이 카오스" 현상을 소개했다. 그런데 카오스 안장점이 정확히 무엇인가? 왜 "불변 집합이 아닌"가?

**카오스 안장점 vs. 어트랙터**

일반적인 이상한 어트랙터는 불변 집합이다: 궤적이 그 위에 머물면 영원히 그 위에 머문다. 카오스 안장점은 다르다: 그것은 **비어트랙팅(non-attracting)** 불변 집합이다. 궤적은 잠시 그 근처에서 카오스적으로 배회하다가 결국 떠나 어트랙터로 수렴한다.

안장점의 구조는 안정 다양체 Wˢ와 불안정 다양체 Wᵘ의 교집합이다. 이 교집합은 전형적으로 **칸토르 집합(Cantor set)** — 르베그 측도가 0인 프랙탈이다. 궤적이 안장점 근처에서 머무는 시간은 안정/불안정 다양체의 기하학에 의해 결정된다.

**이중 전이 카오스의 미묘함**

Motter 등이 발견한 핵심은: 구동계(driven system)에서 전이 카오스의 안장점은 **불변**이다 — 계속 구동되므로 안장점이 유지된다. 그러나 무구동 소산계(undriven dissipative system)에서는 모든 운동이 결국 멈추므로, 전통적 의미의 불변 안장점이 존재하지 않는다.

그럼에도 불구하고 궤적들은 유한 시간 동안 카오스적으로 분리된다. Motter 등은 이 현상을 "이중 전이 카오스"라 명명하고, 다음을 보였다:

1. **유한 스케일에서는** 기저 경계의 측정 차원이 비정수이고, 유한시간 Lyapunov 지수가 양수이다.
2. **점근적으로는** 기저 경계의 프랙탈 공차원(fractal codimension)이 정확히 1이다 — 즉 완전한 프랙탈이 아니라 "거의 프랙탈"이다.
3. **생존 확률**은 초지수적으로 감쇠한다: P(t) ~ exp(−(κ₀/γ)e^{γt}).

이 발견의 중요성은: **카오스가 비구동 소산계에서도 보편적으로 나타날 수 있다**는 것이다. 화학 반응이 평형으로 수렴하는 과정, 쌍성계가 중력파로 에너지를 잃으며 병합되는 과정 등이 이 범주에 속할 수 있다.

**실전 판별법**

전이 카오스인지 판별하려면:

- 유한시간 Lyapunov 지수를 여러 시간 스케일에서 계산 → 양수 구간이 있으면 전이 카오스 가능성.
- 기저 경계의 박스 카운팅 차원을 여러 스케일에서 계산 → 스케일에 따라 변하면 이중 전이 카오스.
- 정착 시간(settling time) 분포를 조사 → 멱법칙이 아니라 초지수적 감쇠면 이중 전이 카오스.

출처: Motter, A. E., Gruiz, M., Károlyi, G., & Tél, T. (2013). Physical Review Letters 111, 194101.
(요약 해설: Physics 6, s142, "Transiently Chaotic", 2013.)

---

## E.2 Melnikov 방법 — 31절 (Homoclinic Chaos)

본문 31절에서 우리는 Homoclinic 점이 카오스 안장점의 "씨앗"이라고 했다. 하지만 **실제로 Homoclinic 점이 존재하는지 어떻게 판정하는가?** Melnikov 방법이 그 답이다.

**핵심 아이디어**

섭동이 없는 해밀턴 계에서 안정 다양체와 불안정 다양체는 **일치**한다(동일한 Homoclinic 궤적을 형성). 섭동이 가해지면 이 둘이 **분리**된다. Melnikov 함수 M(t₀)는 이 분리의 **부호 있는 크기**를 측정한다.

**Melnikov 함수의 정의**

섭동된 계: ẋ = f(x) + εg(x, t), 여기서 f는 해밀턴 벡터장, g는 주기적 섭동.

Melnikov 함수:

  M(t₀) = ∫_{−∞}^{∞} f(x₀(t)) ∧ g(x₀(t), t+t₀) dt

여기서 x₀(t)는 섭동 없는 계의 Homoclinic 궤적이고, ∧는 외적(wedge product) 또는 단순히 성분별 곱의 조합이다.

**판정 기준**

- **M(t₀)가 부호를 바꾸면** (즉, 영점을 가지면): 안정 다양체와 불안정 다양체가 **횡단 교차**한다. 스말레-버코프 정리에 의해, 이는 **카오스의 충분조건**이다.
- **M(t₀) ≠ 0이면**: 두 다양체가 분리되어 있고, 횡단 교차가 없다.
- **M(t₀) ≡ 0이면**: 특별한 대칭성에 의해 두 다양체가 일치한다.

**구체적 예: 감쇠 구동 진자**

계: ẍ + δẋ + sin x = ε cos(ωt)

섭동 없는 계의 Homoclinic 궤적: x₀(t) = 4 arctan(e^t) − π (또는 유사 형태)

Melnikov 함수를 계산하면:

  M(t₀) = −(4δ/3) + 2εω sech(πω/2) sin(ωt₀)

이 함수가 영점을 가지려면:

  2εω sech(πω/2) > 4δ/3

즉, 구동 진폭 ε이 감쇠 δ에 비해 충분히 크면 카오스가 발생한다.

**Melnikov의 한계**

Melnikov는 **섭동적(perturbative)** 방법이다. ε이 작을 때만 유효하다. ε이 크면(예: Duffing 진동자의 표준 조건 ε ~ 0.5) 정량적 정확도가 떨어진다. 또한 다차원 계나 비해밀턴 계로의 확장은 까다롭다.

출처: Melnikov, V. K. (1963). "On the stability of the center for time periodic perturbations." Transactions of the Moscow Mathematical Society 12, 1–56. (원논문)
Guckenheimer, J. & Holmes, P. (1983). Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields. Springer. (Melnikov 방법의 표준 교재)

---

## E.3 OGY 제어의 일반화 — 38절

본문 38절에서 OGY 방법의 기본 공식을 제시했다. 그런데 **왜 하나의 제어 매개변수로 충분한가?** **여러 불안정 방향이 있으면 어떻게 되는가?**

**일반 선형 제어 이론과의 연결**

OGY 제어는 사실 **극점 배치(pole placement)**라는 선형 제어 이론의 특수한 경우이다.

고정점 근처에서 이산 사상의 선형화:

  x_{n+1} = A x_n + B u_n

여기서 x는 고정점으로부터의 편차, u는 제어 섭동, A = ∂F/∂x, B = ∂F/∂p.

비례 피드백 u_n = −K x_n을 적용하면:

  x_{n+1} = (A − BK) x_n

**제어 가능성(controllability)** 조건: K를 적절히 선택하여 A−BK의 모든 고유값을 단위원 내부로 넣을 수 있는가?

**핵심 정리 (OGY의 일반화)**: N차원 계에서 M개의 불안정 방향이 있어도, **일반적으로 하나의 스칼라 제어 매개변수(M=1)로 충분하다**. 단, 다음 조건이 필요하다:

- 행렬 [B, AB, A²B, ..., A^{N−1}B]의 계수가 N이어야 한다 (칼만 조건).
- 즉, 제어 매개변수가 불안정 다양체에 "충분히 결합"되어 있어야 한다.

**실전 의미**

이것은 OGY 방법의 놀라운 효율성을 설명한다: **고차원 카오스 계에서도 단 하나의 매개변수를 미세 조정하여 제어할 수 있다.** Ott, Grebogi, Yorke의 원래 통찰은 바로 이 점이었다 — 카오스의 초기조건 민감성 때문에 작은 섭동이 궤적에 극적인 변화를 일으킬 수 있다.

**실험적 응용**

OGY 및 이와 연관된 카오스 제어 기법은 다음에서 실험적으로 검증되었다(Boccaletti et al., 2000의 종합 리뷰 참조):

- 기계 진동 (자기탄성 리본)
- 전자 회로 (다이오드 공진기)
- 화학 반응 (Belousov-Zhabotinsky 반응)
- 비선형 광학 (다중모드 레이저)
- 유체역학 (대류 불안정성)
- 생체역학 (부정맥을 보이는 심장 조직에서의 카오스 제어)

출처: Ott, E., Grebogi, C., & Yorke, J. A. (1990). "Controlling chaos." Physical Review Letters 64, 1196.
Boccaletti, S., Grebogi, C., Lai, Y.-C., Mancini, H., & Maza, D. (2000). "The control of chaos: theory and applications." Physics Reports 329, 103–197. (실험적 응용 사례들의 표준 리뷰)
Santos, R. B. B. & Graves, J. C. (2010). "Estimating chaos control parameters from time series." Dynamics Days 2010, INPE.

---

## E.4 시계열로부터 Lyapunov 지수 추정의 함정 — 40절

본문 40절에서 Wolf, Rosenstein, Kantz 방법을 소개했다. 실전에서는 **어떤 함정**이 있는가?

**임베딩 매개변수 선택**

Takens 정리에 따르면 m ≥ 2d+1이면 위상학적으로 올바른 매립이 보장된다. 하지만 **실제 데이터에서는** d를 모른다. 너무 작은 m은 거짓 최근접 이웃을 만들고, 너무 큰 m은 노이즈를 증폭하고 계산 비용을 증가시킨다.

**Wolf vs. Rosenstein vs. Kantz**

Awrejcewicz 등(2018)의 체계적 벤치마크에 따르면:

| 시스템   | 최적 방법             | 최악 방법        |
|---------|----------------------|-----------------|
| Hénon 맵 | Benettin, Rosenstein | Wolf            |
| Rössler | Benettin, Rosenstein | Kantz (과소평가) |
| Lorenz  | Benettin, Rosenstein | Wolf (작은 값)   |

**Rosenstein 방법의 장점**: 모든 최근접 이웃 쌍의 평균을 사용하므로 노이즈에 강하고, 임베딩 매개변수에 덜 민감하다.

**Kantz 방법의 함정**: 샘플링 주파수가 변하면 과소평가하는 경향이 있다. 반면 Rosenstein은 안정적이다.

**신경망 방법**

최근에는 훈련된 신경망으로 Lyapunov 스펙트럼을 계산하는 방법이 제안되었다. 방정식을 몰라도 작동하며, 정규 동역학에서 카오스로의 전이를 감지할 수 있다.

출처: Awrejcewicz, J. et al. (2018). "Quantifying Chaos by Various Computational Methods. Part 1." Entropy 20(3), 175.

---

## E.5 이상한 비카오스 어트랙터(SNA) — 본문 어디에도 없는 주제

본문의 카오스 정의(λ > 0, 프랙탈 어트랙터)에 **반례**가 있다: **이상한 비카오스 어트랙터(Strange Nonchaotic Attractor, SNA)**.

**SNA란 무엇인가?**

SNA는 **기하학적으로는 프랙탈(이상한)**이지만 **동역학적으로는 카오스가 아닌** 어트랙터이다.

- **기하학**: 프랙탈 차원을 가진다 (이상한).
- **동역학**: Lyapunov 지수가 **음수 또는 영**이다 (카오스가 아님).
- **궤적**: 비주기적(aperiodic)이지만, 근처 초기조건의 궤적들이 **분리하지 않는다**.

즉, 궤적이 복잡하게 보이지만 **예측 가능**하다.

**SNA는 어디서 나타나는가?**

SNA라는 개념은 Grebogi, Ott, Pelikan, Yorke(1984)가 두 개의 비공약(incommensurate) 주파수로 외부 구동되는 사상을 통해 처음 구성했다. 이들은 SNA가 **준주기적 구동(quasiperiodic driving)**이 있는 계에서 유한한 파라미터 구간에 걸쳐 견고하게(robustly) 나타날 수 있음을 보였다. 준주기 구동이 없으면 SNA는 일반적으로 특정 임계 파라미터에서만 존재하는 비견고한 현상이다.

**실험적 예시**

1. **자기탄성 리본**: Ditto 등(1990)이 SNA를 최초로 실험적으로 관측했다. 황금비에 가까운 두 개의 비공약 주파수 자기장으로 구동되는 자기변형 리본에서, 예측된 스케일링 거동과 프랙탈 차원 측정을 통해 SNA의 존재를 확인했다.
2. **전자 회로, 전기화학 셀, 네온 방전관**: 이후 여러 실험실에서 유사한 준주기 구동 조건 하에 SNA가 견고하게 관측되었다.
3. **Rabinovich-Fabrikant 계의 숨은 어트랙터**: Danca와 Kuznetsov(2021)는 RF 계의 일부 "숨은 카오스 어트랙터"가 실제로는 SNA임을 보였다 — 프랙탈 구조와 비주기 동역학을 가지지만 유한시간 Lyapunov 지수가 음수이다.
4. **천체물리학적 관측**: 2015년, 케플러 우주망원경이 관측한 일부 RR Lyrae 변광성(두 진동 모드의 주파수 비가 황금비에 가까운 별들)에서 SNA적 동역학의 특징이 확인된 바 있다.

**SNA vs. 카오스: 실전 구별**

시각적으로 SNA와 이상한 카오스 어트랙터는 매우 유사하다. 구별법:

- **SNA**: 근처 궤적들이 결국 수렴한다 (Lyapunov ≤ 0). 비주기적이지만 예측 가능.
- **카오스**: 근처 궤적들이 지수적으로 분리한다 (Lyapunov > 0). 예측 불가능.

**응용: 강건한 동기화**

SNA의 중요한 성질은 **강건한 동기화(robust synchronization)**이다. SNA의 궤적들은 서로 수렴하는 경향이 있으므로, SNA를 사용한 통신 시스템은 카오스 기반 시스템보다 동기화가 더 안정적일 수 있다.

출처: Grebogi, C., Ott, E., Pelikan, S., & Yorke, J. A. (1984). "Strange attractors that are not chaotic." Physica D 13, 261–268. (SNA 개념의 원논문)
Ditto, W. L., Spano, M. L., Savage, H. T., Rauseo, S. N., Heagy, J., & Ott, E. (1990). "Experimental observation of a strange nonchaotic attractor." Physical Review Letters 65, 533. (최초의 실험적 관측)
Prasad, A. et al. (2001). "Strange Nonchaotic Attractors." arXiv:nlin/0105022. (개관 논문)
Danca, M.-F. & Kuznetsov, N. (2021). "Hidden Strange Nonchaotic Attractors." Mathematics 9(6), 652.

---

## E.6 심장 박동: 카오스인가 항상성인가? — 14절의 심층 확장

본문 14절에서 "심장이 카오스가 되면 부정맥"이라고 했다. 이것은 **부분적으로만 맞으며, 학계에서도 여전히 논쟁 중인 주제**다.

**Goldberger의 반전: 건강한 심장은 카오스적이다(라는 초기 주장)**

Goldberger(1991, 1992)의 연구는 놀라운 결론을 제시했다: **정상 심장 박동은 단순한 주기적 리듬이 아니라, 카오스적(프랙탈적) 변동성을 보인다**.

- 건강한 심장의 박동 간격은 **단일 시간 스케일이 없다** — 프랙탈/멀티프랙탈 구조를 가진다.
- **부정맥, 심부전, 노화**는 종종 **프랙탈 복잡성의 감소**와 관련된다.
- 즉, "너무 규칙적인" 심장은 오히려 **병적**일 수 있다.

**"항상성" 대 "복잡성"**

Cannon의 항상성(homeostasis) 원리는 생리계가 **일정한 상태를 추구**한다고 가정한다. 그러나 심장 박동 데이터는 다른 그림을 보여준다: **불규칙한 변동성이 "신체의 지혜"일 수 있다**.

**단, 이것이 엄밀한 의미의 "카오스"인지는 논쟁 중이다**

여기서 중요한 단서를 하나 덧붙여야 한다. Goldberger 등이 말하는 "카오스적"이라는 표현은 정성적 의미(불규칙, 프랙탈적 변동)로 쓰인 경우가 많고, 본문 2절에서 정의한 것처럼 **양의 Lyapunov 지수를 엄밀하게 확인한 저차원 결정론적 카오스**인지는 별개의 문제다. 학술지 Chaos는 2009년 이 주제를 공식적으로 "미해결 논쟁"으로 다룬 특집을 마련했는데, 여기서 여러 연구자들이 "정상 심박이 정말 (좁은 의미의) 카오스인가, 아니면 스케일링/프랙탈/멀티프랙탈 현상으로 부르는 것이 더 정확한가"에 대해 상반된 입장을 냈다. 즉:

- 일부 연구는 짧은 시계열에서도 저차원 카오스의 신호(민감한 초기조건 의존성)를 검출했다고 주장한다.
- 다른 연구는 심박 변동성이 카오스라기보다는 **1/f 유사 스케일링을 가진 확률적(멀티프랙탈) 과정**에 가깝다고 반박하며, "카오스"라는 용어 사용에 신중해야 한다고 지적한다.

본문 14절의 진술("심장이 카오스가 되면 부정맥")과는 **긴장 관계**에 있는데, 해결책은 다음과 같다: **맥락과 스케일이 중요하다**. Van der Pol 진동자의 극한 사이클은 심장 세포의 **개별** 진동을 모델링하며, 여기서는 규칙성이 정상이다. 반면 **심장 전체의 리듬 변동성**은 (엄밀한 카오스이든, 프랙탈적 스케일링이든) 복잡성을 띠며, 이 복잡성의 **소실**이 병리로 이어진다는 점에서는 여러 연구가 대체로 일치한다.

**실전 연결**

심박 변동성(Heart Rate Variability, HRV) 분석은 임상에서 심장 질환 위험을 평가하는 도구로 사용된다. 프랙탈 차원이나 (때로는) Lyapunov 지수 유사 지표가 HRV 데이터에서 계산되며, 복잡성 감소는 사망률 증가·급성 심장사 위험과 상관관계가 있다는 보고가 많다. 다만 이 지표들이 진짜 결정론적 카오스를 반영하는지, 아니면 확률적 스케일링 현상을 반영하는지는 여전히 활발한 논쟁 대상이다.

출처: Goldberger, A. L. (1991). "Is the normal heartbeat chaotic or homeostatic?" News in Physiological Sciences 6, 87–91.
Goldberger, A. L. (1992). "Fractal mechanisms in the electrophysiology of the heart." IEEE Engineering in Medicine and Biology Magazine 11(2), 47–52.
Glass, L. (2009). "Introduction to controversial topics in nonlinear science: is the normal heart rate chaotic?" Chaos 19, 028501. (논쟁을 정리한 특집 서문)

---

## E.7 빠른 스크램블링과 OTOC — 22-23절

본문 22-23절에서 OTOC와 MSS 경계를 소개했다. **OTOC가 실제로 무엇을 측정하는가?**

**OTOC의 정의와 직관**

OTOC (Out-of-Time-Order Correlator):

  F(t) = ⟨[q(t), p(0)]²⟩

여기서 q(t)는 시간 t에서의 위치 연산자, p(0)는 초기 운동량 연산자.

**고전적 직관**: 초기 섭동 p(0)가 시간이 지나면서 q(t)에 얼마나 큰 영향을 미치는가? 카오스계에서는 영향이 지수적으로 커진다: F(t) ~ e^{λt}.

**양자적 의미**: OTOC는 "정보 스크램블링"의 속도를 측정한다. 초기에 국소적이던 정보가 계 전체로 퍼져나가는 속도다.

**MSS 경계의 물리적 기원**

Maldacena, Shenker, Stanford(2015)는 열적 양자계에서

  λ_L ≤ 2πk_BT/ℏ

를 추측하고, "그럴듯한 물리적 가정"(인과성, 유니터리성 등)에 기반한 정밀한 논증을 제시했다.

이 경계를 **포화**시키는 계는:

- 블랙홀 (홀로그래피에서)
- SYK 모델 (Sachdev-Ye-Kitaev)
- 강하게 결합된 이론의 일부 극한

**SYK 모델이 중요한 이유**

SYK 모델은 N개의 마요라나 페르미온이 무작위 결합을 하는 0+1차원 양자계이다. 이 모델은:

1. MSS 경계를 포화시킨다.
2. 홀로그래피에서 near-extremal 블랙홀과 이중된다.
3. 최대 카오스계의 장난감 모델로 사용된다.

**실전 연결: 양자 시뮬레이터**

OTOC는 트랩된 이온, 초전도 큐비트, 리드버그 원자 배열 등에서 측정 가능하다. 이는 "양자 카오스를 실험실에서 관측"하는 것을 가능하게 한다.

출처: Maldacena, J., Shenker, S. H., & Stanford, D. (2016). "A bound on chaos." JHEP 08, 106. arXiv:1503.01409 (2015).

---

## E.8 정리: 본문과 부록의 관계

| 본문 장 | 본문 결론              | 부록 심층                        |
|--------|-----------------------|----------------------------------|
| 21.9   | 이중 전이 카오스 존재    | E.1: 안장점 구조, 판별법            |
| 31     | Homoclinic → 카오스    | E.2: Melnikov 함수로 판정          |
| 38     | OGY 공식               | E.3: 하나의 매개변수로 충분한 이유    |
| 40     | Rosenstein 추천        | E.4: 함정, 신경망 방법             |
| (없음)  | —                     | E.5: SNA (카오스의 반례)          |
| 14     | 심장 카오스 = 부정맥     | E.6: 건강한 심장의 (논쟁적인) 카오스성 |
| 22-23  | OTOC, MSS             | E.7: 스크램블링의 의미             |

---

## E.9 추가 참고문헌

Motter, A. E., Gruiz, M., Károlyi, G., & Tél, T. (2013). "Doubly transient chaos: Generic form of chaos in autonomous dissipative systems." Physical Review Letters 111, 194101.

Melnikov, V. K. (1963). "On the stability of the center for time periodic perturbations." Transactions of the Moscow Mathematical Society 12, 1–56.

Guckenheimer, J. & Holmes, P. (1983). Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields. Springer.

Ott, E., Grebogi, C., & Yorke, J. A. (1990). "Controlling chaos." Physical Review Letters 64, 1196.

Boccaletti, S., Grebogi, C., Lai, Y.-C., Mancini, H., & Maza, D. (2000). "The control of chaos: theory and applications." Physics Reports 329, 103–197.

Grebogi, C., Ott, E., Pelikan, S., & Yorke, J. A. (1984). "Strange attractors that are not chaotic." Physica D 13, 261–268.

Ditto, W. L., Spano, M. L., Savage, H. T., Rauseo, S. N., Heagy, J., & Ott, E. (1990). "Experimental observation of a strange nonchaotic attractor." Physical Review Letters 65, 533.

Danca, M.-F. & Kuznetsov, N. (2021). "Hidden Strange Nonchaotic Attractors." Mathematics 9(6), 652.

Prasad, A. et al. (2001). "Strange Nonchaotic Attractors." arXiv:nlin/0105022.

Goldberger, A. L. (1991). "Is the normal heartbeat chaotic or homeostatic?" News in Physiological Sciences 6, 87–91.

Goldberger, A. L. (1992). "Fractal mechanisms in the electrophysiology of the heart." IEEE Engineering in Medicine and Biology Magazine 11(2), 47–52.

Glass, L. (2009). "Introduction to controversial topics in nonlinear science: is the normal heart rate chaotic?" Chaos 19, 028501.

Maldacena, J., Shenker, S. H., & Stanford, D. (2016). "A bound on chaos." JHEP 08, 106. arXiv:1503.01409 (2015).

Awrejcewicz, J., et al. (2018). "Quantifying Chaos by Various Computational Methods. Part 1." Entropy 20(3), 175.

Santos, R. B. B. & Graves, J. C. (2010). "Estimating chaos control parameters from time series." Dynamics Days 2010, INPE.
