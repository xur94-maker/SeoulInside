




TL;DR
A single reference document organizing the concepts, formulas, and representative values of deterministic chaos theory.
- What is chaos? → A phenomenon where the rules are perfect but the outcome is unpredictable
- Why can't we predict it? → Initial errors grow exponentially (λ>0)
- How do we identify it? → Chaotic if the Lyapunov exponent λ > 0
- What is it used for? → Control, synchronization, cryptography, time-series analysis
- Does it exist in quantum mechanics? → Yes, but through "statistics" rather than "trajectories"
- What's the fastest chaos? → Black holes (MSS bound λ_L ≤ 2πT)

Basic concepts (Lyapunov, KS entropy) → 1D/2D maps → Hamiltonian chaos → quantum/gravitational chaos → topology → applications (control, synchronization)


Understanding Chaos, the Easy Way

1. Chaos is not "disorder"
When many people hear "chaos," they picture "a tangled mess" or "disorder."
But what mathematicians mean by chaos is close to the opposite.

Chaos = "a phenomenon where the rules are perfect, but the result is unpredictable"

What does that mean?

Core analogy: the "butterfly effect"
The equations are 100% fixed. (Deterministic)

Starting from the same point always gives the same result.

But... if the starting point differs by just 0.0000001, the outcomes become completely different over time.

That's where the saying "a butterfly flapping its wings in Brazil could set off a tornado in Texas" comes from. This is called sensitive dependence on initial conditions.

2. Why can't we predict it? — The Lyapunov exponent (λ)
The essence of chaos is that "errors snowball."

Analogy: the "telephone game"
Say 10 friends pass a message down a relay line.

λ < 0 (stable): the message gets cleaned up → the original message arrives intact (e.g., a pendulum clock)

λ = 0 (neutral): the message stays exactly the same (e.g., just singing a song)

λ > 0 (chaos): the message gets more and more garbled → a completely different message arrives (e.g., weather)

Here, λ (lambda) is exactly the Lyapunov exponent.

λ > 0 → chaos!

λ < 0 → stable!

The larger λ is, the faster the error grows. (More unpredictable)

3. Three representative examples of chaos
(1) The logistic map — "the tale of the rabbit and the lion"
x_{n+1} = 4xₙ(1−xₙ)

This one simple formula produces chaos.

When μ (mu) is small: the population settles at a single value (stable)

As μ grows: it oscillates periodically between 2, 4, 8... values (bifurcation)

At μ=4: full chaos! λ = ln 2

Fun fact: at this point the population distribution follows an arcsine distribution. (Clustered at the two extremes, sparse in the middle)

(2) The Lorenz system — "the butterfly's wings"
dx/dt = 10(y−x), dy/dt = x(28−z)−y, dz/dt = xy − (8/3)z

These equations, created by meteorologist Lorenz in 1963, produce a butterfly-shaped strange attractor.

The trajectory never retraces the same path twice

But the overall shape looks like a butterfly

λ₁ ≈ 0.90563 → chaos!

(3) The heartbeat — "Van der Pol"
ẍ − μ(1−x²)ẋ + x = 0

This is not chaos! In fact, it's a stable periodic motion.

A heart beating regularly is a good thing.

λ = 0, dimension = 1 (a simple curve)

If the heart were to become chaotic, that would be arrhythmia!

Lesson: chaos isn't always bad. It depends on the situation.

4. Chaos and fractals — "a dimension of 1.26?"
Ordinary dimensions are integers like 1, 2, 3. But chaotic attractors can have dimensions like 1.26.

Analogy: the "Koch snowflake"
Draw an equilateral triangle, and fold out the middle of each side into a bump. Repeat infinitely, and what happens?

The length is infinite

The area is finite

The dimension is log 4 / log 3 ≈ 1.262

This is a fractal. Coastlines, clouds, and tree branches in nature are all fractals.

Kaplan-Yorke dimension formula:

D_KY = j + (Σλᵢ) / |λ_{j+1}|

In simple terms: the dimension is determined by "how many positive λ's there are."

5. Where is chaos used?
(1) OGY chaos control — "taming chaos"
Countless unstable periodic orbits are hidden inside chaos.
These can be stabilized with a very small intervention.

Analogy: it's similar to keeping a spinning top upright. A top naturally wants to fall over, but if you keep giving it small nudges with your hand, it keeps spinning.

Formula:

Δr = −γ(x − x*), γ = −α/β

(2) Chaos synchronization — "two chaotic systems join hands"
If you connect two chaotic systems, you can make them follow the same trajectory.

Secure communication: using a chaotic signal as an encryption key

Heartbeats: synchronization of heart cells

Lasers: aligning the phases of multiple lasers

Condition: all conditional Lyapunov exponents (CLE) must be negative.

(3) Estimating the Lyapunov exponent from time series
"Determining whether something is chaotic from data alone, with no equations"

Wolf (1985): tracks a single trajectory (weak to noise)

Rosenstein (1993): averages over all neighbor pairs (recommended!)

Kantz (1994): a similar method

Real-world use: judging whether stock prices, brain waves, or climate data are chaotic

6. The two faces of chaos — classical vs. quantum
Classical chaos
The butterfly effect, sensitive dependence on initial conditions

λ > 0, fractal attractors

Quantum chaos
Because quantum mechanics is linear, there is in principle no "diverging trajectories"

Instead, chaos is identified through energy-level statistics

Chaos → GOE statistics (Wigner-Dyson)

Integrable → Poisson statistics

🕳️ The MSS chaos bound
λ_L ≤ 2πk_BT / ℏ

"The maximum speed chaos can have in the universe"

The systems that saturate this bound are black holes. Black holes are the fastest scramblers of information in the universe.

7. One-page summary (final wrap-up)
Question	Answer
What is chaos?	A phenomenon where the rules are perfect but the outcome is unpredictable
Why can't we predict it?	Initial errors grow exponentially (λ>0)
How do we identify it?	Chaotic if the Lyapunov exponent λ > 0
What is it used for?	Control, synchronization, cryptography, time-series analysis
Does it exist in quantum mechanics?	Yes, but through "statistics" rather than "trajectories"
What's the fastest chaos?	Black holes (MSS bound λ_L ≤ 2πT)

8. One last word
"Chaos is not disorder — it is a complex order we simply haven't perceived yet."

Simple rules → complex outcomes

Perfect determinism → unpredictability

This paradox is precisely the allure of chaos.





Chaos, Seen Through Simple Math

A representative example of integer chaos: "the logistic map, in integers"

The most famous integer version is "the integer form of the Verhulst equation," or "an integer variant of the discrete logistic map."

The simplest and most famous formula:

  x_{n+1} = 4·xₙ·(N − xₙ) / N  (mod N+1)

Let's set N=100 (i.e., integers from 0 to 100) and start with two initial values that differ by just 1.

---

Experiment: "integer 49" vs. "integer 50"

Rule: x_{n+1} = 4·xₙ·(100 − xₙ) / 100  (rounded down to an integer)
Initial values: A = 49, B = 50

Step | A (49) | B (50) | Difference
-----|--------|--------|------
  0  |   49   |   50   |   1
  1  |   99   |  100   |   1
  2  |    3   |    0   |   3
  3  |   11   |    0   |  11
  4  |   39   |    0   |  39
  5  |   95   |    0   |  95
  6  |   19   |    0   |  19
  7  |   61   |    0   |  61
  8  |   95   |    0   |  95
  9  |   19   |    0   |  19
 10  |   61   |    0   |  61
 ...

Wait! In this example B gets trapped at 0, so this is not actually chaos.
Integer maps easily fall into 0 or a fixed point because of division and rounding.

So to demonstrate genuine integer chaos, we need a different approach.

---

Real integer chaos: the "shift map"

The cleanest example of integer chaos is the "Bernoulli shift."

  x_{n+1} = (2·xₙ) mod 1000

- Initial values: 123, 124 (differ by 1)
- Range: 0 to 999 (integers)
- Rule: multiply by 2, take the remainder mod 1000

Step | A (123) | B (124) | Difference
-----|---------|---------|------
  0  |   123   |   124   |   1
  1  |   246   |   248   |   2
  2  |   492   |   496   |   4
  3  |   984   |   992   |   8
  4  |   968   |   984   |  16
  5  |   936   |   968   |  32
  6  |   872   |   936   |  64
  7  |   744   |   872   | 128
  8  |   488   |   744   | 256
  9  |   976   |   488   | 488
 10  |   952   |   976   |  24
 11  |   904   |   952   |  48
 12  |   808   |   904   |  96
 13  |   616   |   808   | 192
 14  |   232   |   616   | 384
 15  |   464   |   232   | 232
 16  |   928   |   464   | 464
 17  |   856   |   928   |  72
 18  |   712   |   856   | 144
 19  |   424   |   712   | 288
 20  |   848   |   424   | 424

---

What this table tells us

- Steps 0-8: the difference doubles exactly each time (1 → 2 → 4 → 8 → ... → 256)
- Step 9: because of mod 1000, the trajectory "folds" and the difference jumps to 488
- After step 10: the two values trace completely unrelated trajectories

In just 9 steps, a difference of 1 blew up to a difference of 488.

---

Why does this happen? — the Lyapunov exponent

The shift map's Lyapunov exponent:

  λ = ln 2 ≈ 0.693

Growth factor of the error after n steps:

  e^(λ × n) = 2^n

- Step 8:  2^8  = 256× (the actual difference was 256 ✓)
- Step 9:  2^9  = 512× → folded down to 488 because of mod 1000
- Step 20: 2^20 = 1,048,576× → completely diverged

Chaos works perfectly even with integers.

---

Bonus: the "integer logistic map"
To see chaos in integers without using division, just use mod:

  x_{n+1} = (4·xₙ·(N − xₙ)) mod (N+1)

N=99, initial values A=1, B=2:

Step | A (1) | B (2) | Difference
-----|-------|-------|------
  0  |   1   |   2   |   1
  1  |  392  |  776  | 384
  2  |  384  |  320  |  64
  3  |   64  |  960  | 896
  4  |  960  |  320  | 640
  5  |  320  |  960  | 640
  6  |  960  |  320  | 640
  7  |  320  |  960  | 640
 ...

This falls into a period-2 cycle. The mod operation tends to get trapped at specific values.

Conclusion: the shift map (double, then mod) is the clearest demonstration of integer chaos.

---

💻 Python code (integer shift map)

def shift_map(x0, n=20, mod=1000):
    x = x0
    trajectory = [x]
    for _ in range(n):
        x = (2 * x) % mod
        trajectory.append(x)
    return trajectory

A = shift_map(123)
B = shift_map(124)

print(f"{'step':>4} | {'A':>6} | {'B':>6} | {'diff':>6}")
print("-" * 35)
for i in range(21):
    diff = abs(A[i] - B[i])
    print(f"{i:>4} | {A[i]:>6} | {B[i]:>6} | {diff:>6}")

print(f"\nTheoretical growth factor (20 steps): 2^20 = {2**20:,}x")

Output:

step |      A |      B |   diff
-----------------------------------
   0 |    123 |    124 |      1
   1 |    246 |    248 |      2
   2 |    492 |    496 |      4
   ...
   8 |    488 |    744 |    256
   9 |    976 |    488 |    488
   ...
  20 |    848 |    424 |    424

Theoretical growth factor (20 steps): 2^20 = 1,048,576x

---








# Chaos Reference

  - Main text: includes only values that have been analytically derived or confirmed in standard references.
  - Appendix D: includes reference values that may vary depending on computational conditions, parameter definitions, or the source literature.

Notation conventions:
  - The Lyapunov exponent is denoted λ, KS entropy K, and the Feigenbaum constants δ and α.
  - Unless otherwise noted, all values are given in natural log (ln).


# Table of Contents

Part 1  Basic Concepts
  1. What Is Chaos?
  2. The Lyapunov Exponent: Definition and Proof
  3. KS Entropy and the Pesin Formula

Part 2  One-Dimensional Maps
  4. The Logistic Map
  5. The Asymmetric Tent Map
  6. Bernoulli-Type Maps
  7. The Gauss Map
  8. The Chebyshev Map
  9. The Shift Map

Part 3  Two-Dimensional Maps and Continuous Systems
  10. The Hénon Map
  11. The Circle Map (Arnold Circle Map)
  12. The Lorenz System
  13. The Rössler System
  14. The Van der Pol Oscillator
  15. Other Continuous Systems

Part 4  Hamiltonian Chaos and KAM
  16. The Chirikov Standard Map
  17. The Chirikov Resonance-Overlap Criterion
  18. Greene's Residue Criterion
  19. The KAM Theorem

Part 5  Universality and Fractals
  20. The Feigenbaum Constants and Universality
  21. Fractal Dimension
  21.9 Transient Chaos and Fractal Basin Boundaries

Part 6  Quantum Chaos and Gravity
  22. Quantum Chaos
  23. The MSS Chaos Bound
  24. Gravitational Chaos

Part 7  Statistical Mechanics and Probabilistic Chaos
  25. The Loschmidt Paradox and the Stosszahlansatz
  26. Kac's Chaos

Part 8  Topological Chaos Theory
  27. Devaney Chaos
  28. Li-Yorke Chaos
  29. The Poincaré Map
  30. The Smale Horseshoe
  31. Homoclinic / Heteroclinic Chaos
  32. The Oseledec Multiplicative Ergodic Theorem
  33. Ergodicity and the Birkhoff Theorem
  34. SRB Measures
  35. Bifurcation Theory
  36. Multifractal Dimension
  37. Takens' Embedding Theorem


Part 9  Applied Chaos
  38. OGY Chaos Control
  39. Chaos Synchronization
  40. Estimating the Lyapunov Exponent from Time Series


Appendix A. Python Verification Code
Appendix B. Summary Table
Appendix C. References
Appendix D. Additional Reference Values (Condition-Dependent / Varying by Source)


# Part 1  Basic Concepts

## 1. What Is Chaos?

Chaos refers to a phenomenon that is "deterministic yet unpredictable."

Core features
  - Deterministic: the equations are completely fixed; the same initial conditions always → the same outcome.
  - Sensitivity to initial conditions: tiny initial errors grow exponentially over time
  (the "butterfly effect").
  - Topological definition: Devaney's definition requires all three of the following conditions.
  (1) Topological transitivity
  (2) Dense periodic points
  (3) Sensitive dependence on initial conditions
  Li-Yorke chaos is a looser condition (pairs of trajectories repeatedly drawing close
  and then far apart).

Sources:
  Devaney, R. L. (1989). An Introduction to Chaotic Dynamical Systems.
  Li, T.-Y. & Yorke, J. A. (1975). "Period Three Implies Chaos."
  American Mathematical Monthly.

Analogy: chaos is not "disorder" but closer to "complex order."


## 2. The Lyapunov Exponent: Definition and Proof

### 2.1 Limit Definition

  λ(x₀) = lim_{t→∞} lim_{ε→0} (1/t) log | (fᵗ(x₀+ε) − fᵗ(x₀)) / ε |

  The order of the limits matters: ε→0 is taken first (two infinitesimally close
  points), and then t→∞.

### 2.2 Practical Formula (Chain Rule)

  λ(x₀) = lim_{n→∞} (1/n) Σ_{i=0}^{n−1} log |f′(xᵢ)|

  Proof (pure calculus):
  Step 1 — the ε→0 limit is exactly the definition of the derivative:
  lim_{ε→0} |(fⁿ(x₀+ε) − fⁿ(x₀))/ε| = |(fⁿ)′(x₀)|
  Step 2 — chain rule for composite functions (xᵢ := fⁱ(x₀)):
  (fⁿ)′(x₀) = ∏_{i=0}^{n−1} f′(xᵢ)
  Step 3 — convert the product to a sum via the logarithm
  Step 4 — divide by n and take the limit:
  λ(x₀) = lim_{n→∞} (1/n) Σ log|f′(xᵢ)|

  Existence of the limit is guaranteed by Birkhoff's ergodic theorem:
  taking φ(x) = log|f'(x)| as the observable, in an ergodic system the
  time average converges, for almost every x₀, to the same constant
  (∫log|f'| dμ).

### 2.3 Classification Criteria

  λ < 0  ⟺  stable
  λ = 0  ⟺  periodic / neutral
  λ > 0  ⟺  chaotic (unstable)

### 2.4 Lyapunov Time

  T_Lyap ≈ (1/λ) ln | L / δx |

  Meaning: the time it takes for an initial error δx to grow to the size L of the system.

### 2.5 Multidimensional Lyapunov Spectrum

  λᵢ = lim_{N→∞} (1/N) log ( ‖vᵢ(N)‖ / ‖vᵢ(0)‖ )

### 2.6 Hamiltonian vs. Dissipative Systems

  Hamiltonian: Σᵢ λᵢ = 0    (phase-space volume is conserved)
  Dissipative:   Σᵢ λᵢ < 0    (phase-space volume contracts)

### 2.7 The Kaplan-Yorke Dimension

  D_KY = j + (Σ_{i=1}^{j} λᵢ) / |λ_{j+1}|

  Here j is the largest integer satisfying Σ_{i=1}^{j} λᵢ ≥ 0.


## 3. KS Entropy and the Pesin Formula

### 3.1 Definition

  K = Σ_{λᵢ>0} λᵢ

  Meaning: this is the theorem stating that the amount of information a system
  generates per unit time (KS entropy) equals the sum of the positive
  Lyapunov exponents.

### 3.2 Proof Sketch

  The inequality direction (always holds) — the Margulis-Ruelle inequality:
  Divide phase space into ε-cells and iterate n times; cells along expanding
  directions (λᵢ>0) split into e^{nλᵢ} pieces, while contracting directions
  contribute nothing. Number of distinguishable cells:
  N(n,ε) ~ e^{n Σ_{λᵢ>0}λᵢ}
  From the definition of KS entropy, K = lim (1/n) log N(n,ε), it follows that K ≤ Σλᵢ.

  Condition for equality — the SRB measure:
  μ_SRB|_{Wᵘ} ≪ m_{Wᵘ}
  (the invariant measure is absolutely continuous with respect to the natural
  volume measure on the unstable manifold)

  Full proof: Pesin's stable manifold theorem + a rigorous version of the
  Margulis-Ruelle inequality + the Ledrappier-Young (1985) theorem.

Sources:
  Pesin, Ya. B. (1977). Russian Math. Surveys.
  Ledrappier, F. & Young, L.-S. (1985). Annals of Mathematics.

### 3.3 The Ruelle Inequality (General Relation)

  K ≤ Σ_{λᵢ>0} λᵢ

  A general inequality that holds even when no SRB measure exists.

### 3.4 Relation to Topological Entropy

  h_top(f) ≥ K(μ)   (for every invariant measure μ)


# Part 2  One-Dimensional Maps


## 4. The Logistic Map (μ=4)

  x_{n+1} = 4xₙ(1−xₙ)

  Invariant distribution: f(x) = 1/(π√(x(1−x)))  (arcsine distribution)

  λ = ln 2 ≈ 0.693147

  Fixed points:
  x* = 0
  x* = 1 − 1/μ   (μ > 1)


## 5. The Asymmetric Tent Map (γ=0.4)

  f(x) = x/γ           (x < γ)
  f(x) = (1−x)/(1−γ)   (x ≥ γ)

  This map has the uniform distribution (Lebesgue measure) on [0,1] as its
  invariant measure, so its Lyapunov exponent is exactly equal to the binary
  entropy function:

  λ = −γ ln γ − (1−γ) ln(1−γ)

  γ=0.4: λ ≈ 0.673012

  ※ Independent literature check: the 2019 JSIAM Letters confirmed that for the
  asymmetric tent map T_k(x) (peak at x=1/k), the Lyapunov exponent is given by
  λ = −(1/k)log(1/k) − ((k−1)/k)log((k−1)/k)
  which reduces to the symmetric tent map's λ=ln2 when k=2.


## 6. Bernoulli-Type Maps (parameter=0.4)

If this map is defined as "splitting the interval at point γ and linearly
stretching each piece to fill [0,1]," it is mathematically identical in form to
the tent map in Section 5 (both are two linear pieces with the same slope
structure).

  With parameter=0.4, λ ≈ 0.673012 — the same value as the tent map.

Note: the standard (symmetric) Bernoulli shift map (the doubling map,
x_{n+1} = 2x mod 1) has λ = ln 2 ≈ 0.693147, and is topologically conjugate to
the logistic map (μ=4), hence shares the same value.


## 7. The Gauss Map (Continued-Fraction Map)

  f(x) = 1/x mod 1  (x≠0),  f(0)=0

  Invariant measure (Gauss-Kuzmin measure): dμ = 1/((1+x) ln2) dx

  λ = π²/(6 ln 2) ≈ 2.3731382208...

Sources: Rokhlin, V. A. (1961). "Exact endomorphisms of a Lebesgue space."
  Khinchin, A. Ya. Continued Fractions.


## 8. The Chebyshev Map (T_k, k=5)

  T_k(cos θ) = cos(kθ)

  Under the natural invariant measure (arcsine distribution), λ = ln k

  k=5: λ = ln 5 ≈ 1.609438


## 9. The Shift Map (Doubling Map)

  θ_{n+1} = (2θₙ) mod 1

  λ = ln 2 ≈ 0.693147   (topologically conjugate to the logistic map at μ=4)


# Part 3  Two-Dimensional Maps and Continuous Systems


## 10. The Hénon Map (a=1.4, b=0.3)

  x_{n+1} = 1 − a xₙ² + yₙ
  y_{n+1} = b xₙ

  λ₁ ≈ 0.419217
  λ₂ ≈ −1.623190
  D_KY ≈ 1.258267

Source: Sprott, J.C., Chaos and Time-Series Analysis (Oxford, 2003);
  sprott.physics.wisc.edu/chaos/lespec.htm


## 11. The Circle Map (Arnold Circle Map)

  θ_{n+1} = θₙ + Ω − (K/2π) sin(2πθₙ)  (mod 1)

  K=1 is the critical point at which this map loses invertibility
  (the critical circle map), and for K>1 chaotic regions can appear.

  Ω=0.5, K=2.2 (chaotic region): λ ≈ 0.565


## 12. The Lorenz System (σ=10, ρ=28, β=8/3)

  dx/dt = σ(y−x)
  dy/dt = x(ρ−z) − y
  dz/dt = xy − βz

  Lyapunov spectrum:
  λ₁ ≈ 0.90563
  λ₂ = 0
  λ₃ ≈ −14.57219

  Kaplan-Yorke dimension:
  D_KY = 2 + λ₁/|λ₃| ≈ 2.06215

Source: Sprott (2003), sprott.physics.wisc.edu/chaos/lespec.htm

Note: Ouyang and Lin (2011) argued that the chaos observed in the Lorenz model
  may not be a physical phenomenon but rather error values arising from
  mathematical differences between nearly identical quantities. Since this
  differs from the mainstream view, it should be taken as "one group of
  researchers' interpretation."


## 13. The Rössler System (a=0.2, b=0.2, c=5.7)

  dx/dt = −y − z
  dy/dt = x + ay
  dz/dt = b + z(x − c)

  Lyapunov spectrum:
  λ₁ ≈ 0.0714
  λ₂ = 0
  λ₃ ≈ −5.3943

Source: Sprott (2003)


## 14. The Van der Pol Oscillator

  ẍ − μ(1−x²)ẋ + x = 0

  A limit-cycle oscillator — not chaos.
  λ = 0, D_KY = 1.0 (a limit cycle is a one-dimensional curve)


## 15. Other Continuous Systems

### 15.1 The Chen System (a=35, b=3, c=28)

  dx₁/dt = a(x₂ − x₁)
  dx₂/dt = (c−a)x₁ − x₁x₃ + c x₂
  dx₃/dt = x₁x₂ − b x₃

### 15.2 The Li System (a=1, b=0.5)

  dx₁/dt = −x₁ + x₂
  dx₂/dt = −x₃ sgn(x₁) + x₄
  dx₃/dt = |x₁| − a
  dx₄/dt = −b x₂

### 15.3 The Yu-Wang System

  dx₁/dt = a(x₂ − x₁)
  dx₂/dt = b x₁ − c x₁x₃ + k x₂
  dx₃/dt = e^(x₁x₂) − d x₃

  a=15, b=30, c=3.2, d=2, k=−5.2

### 15.4 The Duffing Oscillator

  ẍ + δẋ + αx + βx³ = γ cos(ωt)

  Standard values: α=−1, β=1, δ=0.3, γ=0.5, ω=1.2

### 15.5 The Rabinovich-Fabrikant System

  dx₁/dt = x₂(x₃ − 1 + x₁²) + a x₁
  dx₂/dt = x₁(3x₃ + 1 − x₁²) + a x₂
  dx₃/dt = −2x₃(b + x₁x₂)

  a=−1, b<0


# Part 4  Hamiltonian Chaos and KAM


## 16. The Chirikov Standard Map

  p_{n+1} = pₙ + K sin xₙ
  x_{n+1} = xₙ + p_{n+1}  (mod 2π)


## 17. The Chirikov Resonance-Overlap Criterion (1959)

The simplest (first-order) resonance-overlap estimate gives K_c ~ 1 (order of
magnitude 1). This is not a fixed universal constant like π²/4 (≈2.47), but
rather an approximate criterion whose estimate varies roughly between 0.75 and
1.5 depending on which resonances are included (first-order only vs.
higher-order harmonics as well).

Half-width of a resonance:
  (ΔI)_r ≡ 2 [ ε V(I_r) / ω′(I_r) ]^{1/2}

Overlap criterion:
  2(ΔI)_r ≥ |I_r* − I_r|

Sources:
  Scholarpedia, "Chirikov criterion" (Shepelyansky, 2009)
  B. Chirikov, arXiv:nlin/0006021
  — using first-order resonances alone overestimates; including up to the
  third harmonic brings the estimate close to K_c≈1.


## 18. Greene's Residue Criterion (1979)

Based on the observation that the KAM torus with rotation number equal to the
golden ratio φ=(√5−1)/2 is the last to survive. A method that locates the point
at which the stability residue of nearby periodic orbits diverges/converges.

  R = (2 − Tr(M)) / 4

Precise critical value: K_c ≈ 0.971635
  (more precisely: 0.97163540631...)

Sources:
  Greene, J. M. (1979). J. Math. Phys. 20, 1183.
  Chirikov, arXiv:nlin/0006021
  Fox & Meiss (2018)
  MacKay & Percival: upper bound K_c < 63/64 ≈ 0.9844
  Falcolini & de la Llave: proved that Greene's method never exceeds the upper bound


## 19. The KAM Theorem

### 19.1 The Diophantine Condition

  |ω · l| > γ / ⟨l⟩^τ,   ∀l ∈ ℤ^d \ {0}

  where γ ∈ (0,1), τ > d−1, ⟨l⟩ = max(1, |l|).

### 19.2 The Non-Degeneracy Condition (Twist Condition)

  det( ∂²h/∂Iᵢ∂Iⱼ (I*) ) ≠ 0

### 19.3 Conclusion

  ∃ ε₀ > 0: |ε| < ε₀ ⟹ the invariant torus survives
  Measure of the Cantor set: |C| → 1  (as ε → 0)


# Part 5  Universality and Fractals


## 20. The Feigenbaum Constants and Universality

Feigenbaum's δ (ratio of bifurcation parameters):

  δ = lim_{n→∞} (μ_{n+1} − μₙ)/(μ_{n+2} − μ_{n+1})
  = 4.669201609102990...

Feigenbaum's α (ratio of spacing between periodic orbits):

  α = lim_{n→∞} dₙ/d_{n+1} = 2.502907875...

  ※ Depending on the definition, including a (−1)^n sign factor makes this
  negative, but this document adopts the positive convention. Some sources
  write α = −2.5029....

Universality:
  For any unimodal one-dimensional map with a locally quadratic maximum, the
  same δ arises regardless of the specific details of the function.

Sources:
  Feigenbaum, M. J. (1978). J. Stat. Phys. 19, 25–52.
  Lanford's rigorous proof (1982).
  MathWorld, "Feigenbaum Constant"
  Wikipedia, "Feigenbaum constants"

Scaling laws:
  dₙ ≈ α^{−n} d₀
  μ_∞ − μₙ ≈ δ^{−n} (μ_∞ − μ₀)


## 21. Fractal Dimension

### 21.1 Box-Counting Dimension

  D_B = lim_{ε→0} ln N(ε) / ln(1/ε)

### 21.2 Self-Similarity Dimension

  D_S = ln n(r) / ln(1/r)

### 21.3 Hausdorff Dimension

  H_p(ε) = inf Σᵢ εᵢ^p
  lim_{ε→0} H_p(ε) = 0        (p > D_H)
  = finite   (p = D_H)
  = ∞        (p < D_H)

### 21.4 Fourier-Transform Fractal Dimension

  D_FT = (4 + β) / 2
  (β is the log-log slope of the power spectrum)

### 21.5 Example: the Koch Curve

  r = 1/3, n(r) = 4 → D_S = ln 4 / ln 3 ≈ 1.262

### 21.6 The Kaplan-Yorke Dimension

  D_KY = j + (Σ_{i=1}^{j} λᵢ) / |λ_{j+1}|

### 21.7 Correlation Dimension

  C(ε) = lim_{N→∞} (1/N²) Σ_{i,j} Θ(ε − |xᵢ − xⱼ|)
  D₂ = lim_{ε→0} ln C(ε) / ln ε

### 21.8 The Grassberger-Procaccia Algorithm

  C(ε) ∝ ε^{D₂}
  log C(ε) = D₂ log ε + const


## 21.9 Transient Chaos and Fractal Basin Boundaries

#### 21.9.1 Transient Chaos and the Chaotic Saddle

Transient chaos is a phenomenon in which a trajectory moves chaotically for a
finite time before eventually converging to a periodic orbit or fixed point.
The fractal invariant set where the trajectory lingers during this time is
called a chaotic saddle.

Characteristics of a chaotic saddle:
  - A Cantor set formed by the intersection of the stable manifold Wˢ and
  unstable manifold Wᵘ.
  - λ > 0, yet it is not an attractor, and has measure zero.
  - The trajectory eventually leaves the saddle after a finite time and
  converges to an attractor.

#### 21.9.2 Doubly Transient Chaos in Undriven Dissipative Systems

Traditionally, transient chaos has been studied in driven or conservative
systems. Motter et al. (2013) showed that transient chaos also appears
universally in undriven dissipative systems [4][11].

Characteristics of doubly transient chaos:

  (i) The measured dimension of the basin boundary can be non-integer, and the
  finite-time Lyapunov exponent can be positive at every finite scale, yet
  this does not hold asymptotically.

  (ii) The asymptotic fractal codimension of the basin boundary is 1.

  (iii) The survival probability decays super-exponentially:

  P(t) ~ exp(−(κ₀/γ) e^{γt})                    (21.9.1)

  The stabilization rate κ(t) = κ₀ e^{γt} increases exponentially with time.

  (iv) No invariant chaotic set exists, but a transient chaotic saddle still
  plays a dominant role over a finite energy range [11].

#### 21.9.3 Example: the Magnetic Pendulum

A magnetic pendulum with three magnets placed at the vertices of an
equilateral triangle is a representative example of an undriven dissipative
system. The pendulum converges to one of three stable fixed points, but during
the transient interval before convergence, the finite-time Lyapunov exponent
is positive and the basin boundary shows a fractal structure [11].

Model equations (small-angle approximation):

  ẍ = −ω₀² x − α ẋ + Σᵢ (x − x̃ᵢ)/|x − x̃ᵢ|³
  ÿ = −ω₀² y − α ẏ + Σᵢ (y − ỹᵢ)/|x − x̃ᵢ|³        (21.9.2)

  where (x̃ᵢ, ỹᵢ) are the coordinates of the i-th magnet, ω₀ is the natural
frequency, and α is the damping coefficient.

#### 21.9.4 Connection to Homoclinic Chaos

Transient chaotic saddles are closely connected to the existence of homoclinic
points. If a homoclinic point x_h ∈ Wˢ(x*) ∩ Wᵘ(x*) exists, a chaotic saddle
forms in its vicinity. This connects directly to the content of Section 31
(Homoclinic / Heteroclinic Chaos).

Key connections:
  - A homoclinic point → the "seed" of a chaotic saddle.
  - The escape time of transient chaos is determined by the structure of the
  saddle's stable/unstable manifolds.
  - In driven systems, a chaotic saddle coexists with an attractor, producing
  transient chaos.

References:
  Motter, A. E., Gruiz, M., Károlyi, G., & Tél, T. (2013).
  "Doubly transient chaos: Generic form of chaos in autonomous
  dissipative systems." Physical Review Letters 111, 194101.
  Tél, T. & Gruiz, M. (2006). Chaotic Dynamics: An Introduction
  Based on Classical and Quantum Complex Systems. Cambridge.




# Part 6  Quantum Chaos and Gravity


## 22. Quantum Chaos

Because the time evolution of quantum mechanics (the Schrödinger equation) is
linear and unitary, there is in principle no "exponentially diverging
trajectory" in the classical sense. Instead, one uses:

  - The OTOC (Out-of-Time-Order Correlator)
  - Energy-level statistics (agreement with random matrix theory, RMT)
  - The Ehrenfest time

### 22.1 The BGS Conjecture (Bohigas-Giannoni-Schmit)

  Classically chaotic system → GOE statistics
  Integrable system → Poisson statistics

### 22.2 Energy-Level Spacing Distributions

  Poisson:        P(s) = e^{−s}
  Wigner-Dyson (GOE):  P(s) = (π/2) s e^{−πs²/4}
  GUE:            P(s) = (32/π²) s² e^{−4s²/π}

### 22.3 Spectral Rigidity

  Δ₃(L) = (1/L) min_{A,B} ∫₀^L [N(E) − AE − B]² dE

### 22.4 The OTOC

  F(t) = ⟨[q(t), p(0)]²⟩
  F(t) ~ e^{λt}

### 22.5 The Quantum Lyapunov Exponent

  λ_th(T) = (1/t) log[ −∫dE ρ(E) e^{−βE} ⟨E|[q(t),p(0)]²|E⟩ ]

### 22.6 Quantum Chaos and RMT

  P(s) = a s^β e^{−b s²}
  β = 1 (GOE), 2 (GUE), 4 (GSE)


## 23. The MSS Chaos Bound (Maldacena-Shenker-Stanford)

  λ_L ≤ 2πk_BT / ℏ

  (in units where k_B = 1: λ_L ≤ 2πT/ℏ)

Source: Maldacena, Shenker, Stanford, "A bound on chaos",
  arXiv:1503.01409 (2015), JHEP 08 (2016) 106.

The systems that "saturate" this bound are black holes (and the SYK model),
which correspond directly, in holography (AdS/CFT), to the surface gravity of
the black hole horizon, κ=2πT.

### 23.1 The Energy Limit of Chaos

  λ(E) ∝ E^c,   c ≤ 1   (as E → ∞)

### 23.2 The Fast-Scrambling Conjecture

  Minimum depth for forming a strong unitary design over n qubits = Θ(log n)


## 24. Gravitational Chaos

  - The N-body problem: gravitational systems with three or more bodies are
  generally chaotic (long-term stability of the solar system, orbital
  resonances, etc.)
  - Black holes = the fastest scramblers of information: the Sekino-Susskind
  conjecture
  - The MSS bound connects directly to this domain

### 24.1 Bekenstein-Hawking Entropy

  S_BH = A / 4

### 24.2 The Page Curve

  S_rad(t) = min( S_BH(t), S_thermal(t) )


# Part 7  Statistical Mechanics and Probabilistic Chaos


## 25. The Loschmidt Paradox and the Stosszahlansatz

The objection Josef Loschmidt (1876) raised against Boltzmann:
Newtonian mechanics is time-reversible, so why does the H-theorem predict
irreversible entropy increase?

Elements of the resolution:
  1. The Stosszahlansatz (molecular chaos assumption)
  — the very assumption that the velocity distributions of two particles are
  independent just before a collision already secretly builds in a preferred
  direction of time.
  f₂(v₁, v₂, t) = f(v₁, t) · f(v₂, t)   (before collision)

  2. Chaos makes reversed trajectories practically unrealizable
  — reversing the velocities exactly would require a precision only
  achievable within the Lyapunov time,
  T_Lyap ≈ (1/λ)ln|L/δx|, which is physically impossible for a system with
  Avogadro's number (~10²³) of particles.

  3. The larger K in the Pesin formula, the more exponentially the required
  precision grows, which "practically cements" irreversibility.

### 25.1 The Boltzmann Equation

  ∂f/∂t + v·∇_r f + (F/m)·∇_v f = C[f]

### 25.2 The Collision Integral

  C[f] = ∫∫ [f(v′) f(v₁′) − f(v) f(v₁)] |v − v₁| σ dΩ d³v₁

### 25.3 The H-Theorem

  H = ∫ f(v) ln f(v) d³v
  dH/dt ≤ 0
  S = −k_B H + const
  → dS/dt ≥ 0

### 25.4 Boltzmann Entropy and Shannon Entropy

  S = k_B ln Ω
  H = −Σ p log p
  p_i = 1/Ω → H = ln Ω,  S = k_B H


## 26. Kac's "Chaos" — the Probabilistic Meaning

A concept proposed by Mark Kac, with a meaning completely different from
chaos (trajectory instability) in dynamical systems.

### 26.1 Definition of Kac's Chaos

  L(Z₁ᴺ, ..., Zⱼᴺ) → f^⊗j   (weak convergence, N → ∞)

  A sequence of random variables (Z^N) is called f-Kac chaotic if the joint
  distribution of any j of them converges, as N→∞, to the independent product
  f^⊗j.

### 26.2 Integral Form of Asymptotic Independence

  ∫ φ₁(z₁)···φⱼ(zⱼ) dFᴺ(z₁,...,zⱼ) → ∏ᵢ ∫ φᵢ(z) dF(z)

### 26.3 Propagation of Chaos

  F₀ᴺ is f₀-Kac chaotic ⟹ Fₜᴺ is fₜ-Kac chaotic  (∀t ≥ 0)

  If this independence holds at the initial time, it holds at every later
  time as well — this is the mathematical basis of the Boltzmann equation and
  mean-field approximations.

Source: Kac, M. (1956). "Foundations of kinetic theory",
  Proc. 3rd Berkeley Symposium.

### 26.4 The Kac Model

  ∂f(x,t)/∂t = (ν/2π) ∫_{−∞}^{∞} ∫₀^{2π} {
  f(x cosθ + y sinθ, t) f(−x sinθ + y cosθ, t)
  − f(x,t) f(y,t)
  } dθ dy


# Part 8  Topological Chaos Theory


## 27. Devaney Chaos

  f : X → X

  ① Topological transitivity
  ∀ U,V ⊂ X, U,V ≠ ∅
  ∃ n ≥ 0 : fⁿ(U) ∩ V ≠ ∅

  ② Periodic points are dense
  Per(f) = {x ∈ X | ∃ n ≥ 1, fⁿ(x)=x}
  cl(Per(f)) = X

  ③ Sensitivity to initial conditions
  ∃ δ > 0 :
  ∀ x ∈ X, ∀ ε > 0,
  ∃ y ∈ X, ∃ n ≥ 0 :
  d(x,y) < ε ∧ d(fⁿ(x),fⁿ(y)) > δ


## 28. Li-Yorke Chaos

### 28.1 Scrambled Pair

  liminf_{n→∞} d(fⁿ(x), fⁿ(y)) = 0
  limsup_{n→∞} d(fⁿ(x), fⁿ(y)) > 0

### 28.2 Li-Yorke Scrambled Set

  S ⊂ X
  ∀ x,y ∈ S, x ≠ y:
  liminf_{n→∞} d(fⁿ(x), fⁿ(y)) = 0
  limsup_{n→∞} d(fⁿ(x), fⁿ(y)) > 0

Source: Li, T.-Y. & Yorke, J. A. (1975). "Period Three Implies Chaos",
  American Mathematical Monthly.


## 29. The Poincaré Map

### 29.1 The Poincaré Section

  Σ = { x ∈ M | h(x) = 0 }
  Dh(x) · F(x) ≠ 0

### 29.2 The Poincaré Map

  P : Σ → Σ
  P(xₙ) = xₙ₊₁

### 29.3 Periodic-Orbit Condition

  Pⁿ(x*) = x*


## 30. The Smale Horseshoe

### 30.1 The Horseshoe Map

  f : Q → Q
  Λ = ⋂_{n∈ℤ} fⁿ(Q)

### 30.2 Symbolic Dynamics

  Σ₂ = {0,1}^ℤ
  σ((xₙ)) = (xₙ₊₁)
  f|Λ ≅ σ

### 30.3 Topological Entropy of the Horseshoe

  h_top(f|Λ) = log 2


## 31. Homoclinic / Heteroclinic Chaos

### 31.1 Stable and Unstable Manifolds

  Wˢ(x*) = {x | d(fⁿ(x), fⁿ(x*)) → 0, n→∞}
  Wᵘ(x*) = {x | d(f⁻ⁿ(x), f⁻ⁿ(x*)) → 0, n→∞}

### 31.2 Homoclinic Orbit

  x(t) → x*       as t → +∞
  x(t) → x*       as t → −∞
  x(t) ∈ Wˢ(x*) ∩ Wᵘ(x*)


## 32. The Oseledec Multiplicative Ergodic Theorem

### 32.1 Basic Form

  Aₙ(x) = Dfⁿ(x)
  λᵢ = lim_{n→∞} (1/n) log ‖Aₙ(x)vᵢ‖

### 32.2 Lyapunov Decomposition

  TₓM = ⊕ᵢ Eᵢ(x)
  Df(x) Eᵢ(x) = Eᵢ(f(x))

### 32.3 Exponential Growth Rate

  lim_{n→∞} (1/n) log ‖Dfⁿ(x)v‖ = λᵢ


## 33. Ergodicity and the Birkhoff Theorem

### 33.1 Invariant Measure

  μ(f⁻¹A) = μ(A)

### 33.2 Ergodicity

  f⁻¹A = A ⟹ μ(A) = 0 or 1

### 33.3 Birkhoff's Time-Average Theorem

  lim_{n→∞} (1/n) Σ_{k=0}^{n−1} φ(fᵏx) = ∫ φ dμ
  (for almost every x, in the ergodic case)


## 34. SRB Measures

  μ_SRB = invariant measure
  μ_SRB(Wˢ(x)) = 1
  μ_SRB|_{Wᵘ} ≪ m_{Wᵘ}

  Expressed as the property that the conditional measure on the unstable
  manifold Wᵘ is absolutely continuous with respect to the usual volume
  measure.


## 35. Bifurcation Theory

### 35.1 Saddle-Node Bifurcation

  ẋ = μ − x²
  x* = ±√μ   (μ ≥ 0)

### 35.2 Transcritical Bifurcation

  ẋ = μx − x²
  x* = 0,  x* = μ

### 35.3 Pitchfork Bifurcation

  ẋ = μx − x³
  x* = 0,  x* = ±√μ

### 35.4 Hopf Bifurcation

  ẋ = μx − ωy − x(x²+y²)
  ẏ = ωx + μy − y(x²+y²)

  Polar coordinates: ṙ = μr − r³,  θ̇ = ω
  Periodic orbit: r = √μ   (μ > 0)


## 36. Multifractal Dimension

### 36.1 The Generalized Dimension D_q

  D_q = 1/(q−1) · lim_{ε→0} [ ln Σᵢ pᵢ(ε)^q / ln ε ]

### 36.2 Information Dimension

  D₁ = lim_{ε→0} [ Σᵢ pᵢ ln pᵢ / ln ε ]

### 36.3 Correlation Dimension

  D₂ = lim_{ε→0} ln C(ε) / ln ε

### 36.4 Singularity Spectrum

  α(q) = dτ(q)/dq
  f(α) = qα − τ(q)
  τ(q) = (q−1)D_q


## 37. Takens' Embedding Theorem

### 37.1 Delay-Coordinate Embedding

  X(t) = [x(t), x(t−τ), x(t−2τ), ..., x(t−(m−1)τ)]

### 37.2 Embedding-Dimension Condition

  m ≥ 2d + 1
  (d is the dimension of the manifold of the original state space)

### 37.3 The Embedding Map

  Φ(x) = (h(x), h(f(x)), h(f²(x)), ..., h(f²ᵈ(x)))


# Appendix A. Python Verification Code

### A.1 Computing the Lyapunov Exponent (Logistic Map)

```python
import numpy as np

def lyapunov_logistic(a, n=10000, x0=0.1):
    x = x0
    lam = 0
    for _ in range(n):
        x = a * x * (1 - x)
        lam += np.log(abs(a * (1 - 2*x)))
    return lam / n

print(f"a=4: λ = {lyapunov_logistic(4):.4f} (theory: {np.log(2):.4f})")
```

### A.2 Sensitivity to Initial Conditions

```python
def sensitivity(a=4, x0=0.1, eps=1e-8, n=50):
    x1, x2 = x0, x0 + eps
    for _ in range(n):
        x1 = a * x1 * (1 - x1)
        x2 = a * x2 * (1 - x2)
    return abs(x1 - x2)

print(f"Error after 50 iterations: {sensitivity():.4f} (initial error: 1e-8)")
```

### A.3 Lyapunov Exponent of the Asymmetric Tent Map (Compared with Binary Entropy)

```python
import numpy as np

def lyapunov_tent(gamma, n=2_000_000, x0=0.3):
    x = x0
    lam = 0
    for _ in range(n):
        if x < gamma:
            x = x / gamma
            lam += np.log(1 / gamma)
        else:
            x = (1 - x) / (1 - gamma)
            lam += np.log(1 / (1 - gamma))
    return lam / n

gamma = 0.4
theoretical = -gamma*np.log(gamma) - (1-gamma)*np.log(1-gamma)
print(f"γ=0.4: numeric = {lyapunov_tent(gamma):.6f}, "
      f"theory = {theoretical:.6f}")
```

### A.4 Simulating the Lorenz Equations

```python
import numpy as np
from scipy.integrate import odeint

def lorenz(state, t, sigma=10, beta=8/3, rho=28):
    x, y, z = state
    return [sigma*(y-x), x*(rho-z)-y, x*y-beta*z]

t = np.linspace(0, 50, 10000)
sol = odeint(lorenz, [1, 1, 1], t)
```

### A.5 Estimating KS Entropy

```python
def ks_entropy_estimate(lyapunov_spectrum):
    return sum(l for l in lyapunov_spectrum if l > 0)

lyap_lorenz = [0.90563, 0, -14.57219]
print(f"KS entropy: {ks_entropy_estimate(lyap_lorenz):.4f}")
```



# Appendix B. Summary Table

| Ch. | Topic | Key Formula / Value |
|---|---|---|
| 1 | Definition of chaos | Devaney's 3 conditions, Li-Yorke condition |
| 2 | Lyapunov | λ = lim (1/n) Σ log\|f'(xᵢ)\| |
| 3 | KS entropy | K = Σ_{λᵢ>0} λᵢ (Pesin) |
| 4 | Logistic map | λ = ln 2 |
| 5 | Asymmetric tent map | λ = −γlnγ−(1−γ)ln(1−γ) |
| 6 | Bernoulli-type maps | same as tent map |
| 7 | Gauss map | λ = π²/(6 ln 2) |
| 8 | Chebyshev map | λ = ln k |
| 9 | Shift map | λ = ln 2 |
| 10 | Hénon map | λ₁ = 0.419217, λ₂ = −1.623190 |
| 11 | Circle map | λ ≈ 0.565 (K=2.2, Ω=0.5) |
| 12 | Lorenz | (0.90563, 0, −14.57219), D_KY = 2.06215 |
| 13 | Rössler | (0.0714, 0, −5.3943) |
| 14 | Van der Pol | not chaos (λ = 0) |
| 15 | Other continuous systems | Chen, Li, Yu-Wang, Duffing, etc. |
| 16 | Chirikov standard map | p' = p + K sin x, x' = x + p' |
| 17 | Chirikov criterion | K_c ~ 1 (approximate) |
| 18 | Greene criterion | K_c ≈ 0.971635 |
| 19 | KAM | Diophantine + twist condition |
| 20 | Feigenbaum | δ = 4.669..., α = 2.503... |
| 21 | Fractal dimension | D_B = lim ln N(ε)/ln(1/ε) |
| 21.9 | Transient chaos | chaotic saddle, P(t) ~ exp(−(κ₀/γ)e^{γt}) |
| 22 | Quantum chaos | BGS, GOE/GUE |
| 23 | MSS bound | λ_L ≤ 2πk_BT/ℏ |
| 24 | Gravitational chaos | S_BH = A/4, Page curve |
| 25 | Loschmidt | Stosszahlansatz |
| 26 | Kac chaos | L(Z₁,...,Zⱼ) → f^⊗j |
| 27 | Devaney | fⁿ(U)∩V≠∅ |
| 28 | Li-Yorke | liminf=0, limsup>0 |
| 29 | Poincaré | P:Σ→Σ |
| 30 | Horseshoe | h_top = log 2 |
| 31 | Homoclinic | Wˢ∩Wᵘ≠∅ |
| 32 | Oseledec | λᵢ = lim n⁻¹ log‖Dfⁿvᵢ‖ |
| 33 | Ergodicity | f⁻¹A=A ⇒ μ(A)∈{0,1} |
| 34 | SRB measure | μ_SRB\|Wᵘ ≪ m_Wᵘ |
| 35 | Bifurcation theory | ẋ = μx − x³, etc. |
| 36 | Multifractal | D_q = 1/(q−1) lim ln Σpᵢ^q/ln ε |
| 37 | Takens | m ≥ 2d+1 |
| 38 | OGY control | Δr_n = −γ n̂·(x_n − x*), γ = −α/β |
| 39 | Synchronization | all CLE < 0 ⟹ complete synchronization |
| 40 | Time-series Lyapunov | S(ε,m,t) slope = λ_max |

# Appendix C. References

Devaney, R. L. (1989). An Introduction to Chaotic Dynamical Systems.

Li, T.-Y. & Yorke, J. A. (1975). "Period Three Implies Chaos."
American Mathematical Monthly.

Sprott, J. C. (2003). Chaos and Time-Series Analysis. Oxford.
(Table of Lyapunov spectra: sprott.physics.wisc.edu/chaos/lespec.htm)

Feigenbaum, M. J. (1978). "Quantitative universality for a class of
nonlinear transformations." J. Stat. Phys. 19, 25–52.

Pesin, Ya. B. (1977). "Characteristic Lyapunov exponents and smooth
ergodic theory." Russian Math. Surveys.

Ledrappier, F. & Young, L.-S. (1985). "The metric entropy of
diffeomorphisms." Annals of Mathematics.

Greene, J. M. (1979). "A method for determining a stochastic
transition." J. Math. Phys. 20, 1183.

Chirikov, B. V. "Critical perturbation in standard map: A better
approximation." arXiv:nlin/0006021.

Maldacena, J., Shenker, S. H., & Stanford, D. (2016). "A bound on
chaos." JHEP 08, 106. arXiv:1503.01409 (2015).

Kac, M. (1956). "Foundations of kinetic theory." Proc. 3rd Berkeley
Symposium on Mathematical Statistics and Probability.

Rokhlin, V. A. (1961). "Exact endomorphisms of a Lebesgue space."
(the original source for the Gauss map's Lyapunov exponent)

Khinchin, A. Ya. Continued Fractions. (the standard result for the
Gauss-Kuzmin measure)

Shepelyansky, D. L. (2009). Scholarpedia, "Chirikov criterion".

Fox, A. M. & Meiss, J. D. (2018). "Greene's Residue Criterion..."

MacKay, R. S. & Percival, I. C. (1985). (computation of the KAM
critical-value upper bound)

Falcolini, C. & de la Llave, R. (1992). (proof of the upper bound on
Greene's method)

Ouyang, Z. & Lin, S. (2011). (a cautionary note on the interpretation
of Lorenz)

2019 JSIAM Letters (independent confirmation of the Lyapunov-exponent
formula for the asymmetric tent map)

Ott, E., Grebogi, C., & Yorke, J. A. (1990). "Controlling chaos."
  Physical Review Letters 64, 1196.

Pecora, L. M. & Carroll, T. L. (1990). "Synchronization in chaotic
  systems." Physical Review Letters 64, 821.

Wolf, A. et al. (1985). "Determining Lyapunov exponents from a time
  series." Physica D 16, 285.

Rosenstein, M. T. et al. (1993). "A practical method for calculating
  largest Lyapunov exponents from small data sets." Physica D 65, 117.

Kantz, H. (1994). "A robust method to estimate the maximal Lyapunov
  exponent of a time series." Physics Letters A 185, 77.

Motter, A. E., Gruiz, M., Károlyi, G., & Tél, T. (2013).
  "Doubly transient chaos: Generic form of chaos in autonomous
  dissipative systems." Physical Review Letters 111, 194101.

Awrejcewicz, J. et al. (2018). "Quantifying Chaos by Various
  Computational Methods." Entropy 20(3), 175.

Santos, R. B. B. & Graves, J. C. (2010). "Estimating chaos control
  parameters from time series." Dynamics Days 2010, INPE.

Chen, H.-K. & Lin, T.-N. (2003). "Chaotic synchronization based on
  stability criterion of linear systems." Physics Letters A 314, 292.


# Appendix D. Additional Reference Values (Condition-Dependent / Varying by Source)

This appendix records reference values not adopted in the main text. These
values can vary depending on computational conditions (number of steps,
initial conditions, treatment of transients), parameter definitions, or
the source literature.

### D.1 One-Dimensional Maps

**Cubic map**
x_{n+1} = λ xₙ³ + (1−λ) xₙ
At λ=4, λ₁ ≈ 1.5827 (the definition varies across sources)

**Alternative definitions:**
x_{n+1} = A xₙ(1−xₙ²), A=3 → λ ≈ 1.0986
x_{n+1} = 0.35xₙ³ − 2.75xₙ² + c xₙ

### D.2 Two-Dimensional Maps

**The Ikeda map**
z_{n+1} = A + B zₙ exp(i(|zₙ|² + φ))
At R=0.9, C₁=0.4, C₂=0.9, C₃=6, λ_max ≈ 0.51

**Alternative circle-map value**
At Ω=0.5, K=2.2, λ ≈ 0.5766
(likely arising from differing computational conditions)

### D.3 Continuous Systems

**The Chen system (a=35, b=3, c=28)**
λ₁ ≈ 2.0272 (literature value)

**The Yu-Wang system (4D version)**
LE1 = 1.4247 (literature value)

**The Rabinovich-Fabrikant system**
For the self-excited chaotic attractor, λ₁ ≈ 0.5 is possible
Hidden attractors can have λ<0 — strange nonchaotic
At a=0.14, b=0.10, initial conditions [-1, 0, 0.5], the exact value of
λ₁ requires separate verification

**The Duffing oscillator**
At α=−1, β=1, δ=0.3, γ=0.5, ω=1.2, λ₁ ≈ 0.15
Under other conditions (a=0.2, b=1, c=0.16, d=0.75), σ₁ ≈ 0.17 has been reported

### D.4 Hamiltonian Chaos

**The Chirikov resonance-overlap bound**
2023, Dynamics, using a random-matrix method, K≈2.43
(close to π²/4≈2.47, but represents an entirely different transition from
Greene's K_c≈0.9716)


# Part 9  Applied Chaos

## 38. OGY Chaos Control (Ott-Grebogi-Yorke Method)

### 38.1 Basic Principle

Countless unstable periodic orbits (UPOs) are densely embedded inside a
chaotic (strange) attractor. The OGY method selects one of these and
stabilizes it by applying a very small perturbation to the system's control
parameter.

Key insight: because of a chaotic system's sensitivity to initial conditions,
a small perturbation can produce a dramatic change in the trajectory, and
since every small region of phase space is crossed by trajectories that visit
every other region of the attractor, control turns out to be remarkably
efficient [1].

### 38.2 Mathematical Formulation (Codimension-1 Map)

  x_{n+1} = F(x_n, r_n)                                    (38.1)

  where r_n is the control parameter. Linearizing near the target unstable
fixed point x* and nominal parameter r₀:

  x_{n+1} ≈ x* + α(x_n − x*) + β(r_n − r₀)                (38.2)

  where the sensitivity coefficients are:

  α = ∂F/∂x |_{x=x*, r=r₀}                                  (38.3)
  β = ∂F/∂r |_{x=x*, r=r₀}                                  (38.4)

  The control input takes a feedback form proportional to the deviation from
the fixed point:

  Δr_n = r_n − r₀ = −γ n̂ · (x_n − x*),   γ = −α/β          (38.5)

  where n̂ is a unit vector normal to the Poincaré section Σ near the
unstable fixed point [1].

### 38.3 A Logistic-Map Example

  x_{n+1} = r x_n(1 − x_n)                                  (38.6)

  Unstable fixed point: x* = 1 − 1/r₀

  Modified map under control:

  x_{n+1} = (r₀ − γ(x_n − x*)) x_n(1 − x_n)                 (38.7)

  Choosing γ = −α/β achieves optimal control.

  Numerical example: analyzing just two 100-point time series is enough to
estimate α and β to within 2% of the analytical values, and using these
estimates, OGY control successfully stabilizes a period-1 unstable periodic
orbit embedded in the logistic map's chaotic attractor [1].

### 38.4 Practical Implications

- Control parameters can be estimated from time series alone, with no model
  equations.
- The size of the control perturbation is on the order of O(ε), and does not
  change the overall dynamics of the system.
- The size of the basin of control is determined by the amount of available
  information and the Lyapunov exponent λ*: ε ≥ e^{λ*} ε_m [8].

References:
  Ott, E., Grebogi, C., & Yorke, J. A. (1990). "Controlling chaos."
  Physical Review Letters 64, 1196.
  Santos, R. B. B. & Graves, J. C. (2010). "Estimating chaos control
  parameters from time series." Dynamics Days 2010, INPE.


## 39. Chaos Synchronization

### 39.1 Basic Concept

Chaos synchronization is a phenomenon in which two (or more) chaotic systems,
through coupling, come to follow an identical trajectory. Pecora and Carroll
proposed a drive-response scheme, showing that feeding some variables of a
driving system as input into a response system can bring the two systems
into synchronization [9].

### 39.2 The Pecora-Carroll Method

Decompose a chaotic system S into two subsystems S₁ and S₂. Let S₁ have a
positive Lyapunov exponent and S₂ a negative one. Using S₁ as the drive
signal to drive a copy Ŝ₂ of S₂, S₂ and Ŝ₂ become synchronized.

Necessary and sufficient condition for synchronization: all of the response
system's conditional Lyapunov exponents (CLEs) must be negative.

  all CLE < 0  ⟹  complete synchronization                       (39.1)

### 39.3 Examples with the Lorenz and Rössler Systems

The Lorenz system:

  ẋ₁ = σ(x₂ − x₁)
  ẋ₂ = −x₁x₃ + rx₁ − x₂
  ẋ₃ = x₁x₂ − b x₃                                  (39.2)

- Using x₃ as the drive signal does not synchronize (x₁, x₂).
- At σ=16, r=45.92, b=4, the Jacobian matrix A has negative real
  eigenvalues (−16, −1, −4), and a decomposition based on this makes
  synchronization possible [16].

The Rössler system:

  ẋ = −y − z
  ẏ = x + ay
  ż = b + z(x − c)                                  (39.3)

- With x-drive, the CLEs include a positive value (+0.2), so synchronization
  fails.
- With y-drive, all CLEs are negative, so synchronization succeeds.
- Thus, whether the drive variable is chosen well determines success or
  failure of synchronization [2].

### 39.4 Alternatives When Synchronization Fails

Even a system with a positive CLE can be synchronized via a convex
combination: using a weighted average of the drive signal and the response
signal as the new drive signal, the response-system component acts to
suppress chaos and induce synchronization [2].

### 39.5 Practical Implications

- Secure communication: using a chaotic signal as an encryption key.
- Biological systems: synchronization phenomena in heartbeats and neural
  networks.
- Laser arrays: phase synchronization of coupled lasers.

References:
  Pecora, L. M. & Carroll, T. L. (1990). "Synchronization in chaotic
  systems." Physical Review Letters 64, 821.
  Pecora, L. M. & Carroll, T. L. (1991). "Driving systems with chaotic
  signals." Physical Review A 44, 2374.
  Chen, H.-K. & Lin, T.-N. (2003). "Chaotic synchronization based on
  stability criterion of linear systems." Physics Letters A 314, 292.


## 40. Estimating the Lyapunov Exponent from Time Series

### 40.1 Problem Setup

The problem of estimating the maximal Lyapunov exponent from an observed
time series {x(t)} alone, without knowing the model equations. Three
standard algorithms are widely used: Wolf (1985), Rosenstein (1993), and
Kantz (1994) [10].

### 40.2 Common Principle

After phase-space reconstruction (Takens embedding), compute the average
separation rate of nearest-neighbor pairs as a function of time. If this
separation rate grows exponentially, that growth rate is the maximal
Lyapunov exponent.

  |Δ(t)| ≈ |Δ(0)| e^{λt}                             (40.1)

### 40.3 The Wolf Algorithm (1985)

Follows a single reference trajectory, tracking how the distance to the
nearest neighbor at each point changes. It is the oldest method, but because
it relies on a single trajectory, it is sensitive to noise and prone to
large errors [6].

  L₁ = (1/m) Σ ln(df_i/dt) / (EVOLV · dt)              (40.2)

### 40.4 The Rosenstein / Kantz Algorithms (1993 / 1994)

The two algorithms are essentially the same. They find all nearest-neighbor
pairs and compute the average distance between them as a function of time:

  S(ε, m, t) = ⟨ ln( (1/|U_n|) Σ_{S'_n ∈ U_n} |S_{n+1} − S'_{n+1}| ) ⟩
  (40.3)

  where U_n is the ε-neighborhood set of point S_n. If S(ε, m, t) grows
linearly, its slope is the maximal Lyapunov exponent [3].

  It is necessary to confirm independence from the embedding parameters
(τ, m). The result can be trusted if the slope stays consistent for
sufficiently large m and over a reasonable range of ε [3].

### 40.5 Performance Comparison

Benchmark results for the Hénon, hyperchaotic Hénon, logistic, Rössler, and
Lorenz systems [6]:

  System        | Best method           | Worst method
  Hénon         | Benettin, Rosenstein | Wolf
  Rössler       | Benettin, Rosenstein | Kantz (underestimates)
  Lorenz        | Benettin, Rosenstein | Wolf (underestimates)

  In general, the Rosenstein and Kantz methods outperform Wolf. Neural
network-based methods also perform well, but require separate training [6].

### 40.6 Practical Implications

- Used to determine whether experimental data (physics, biology, finance) is
  chaotic.
- Requires an embedding dimension m ≥ 2d+1 (Takens' theorem).
- Under changes in sampling frequency, the Rosenstein method is stable,
  while the Kantz method tends to underestimate [6].

References:
  Wolf, A. et al. (1985). "Determining Lyapunov exponents from a time
  series." Physica D 16, 285.
  Rosenstein, M. T. et al. (1993). "A practical method for calculating
  largest Lyapunov exponents from small data sets." Physica D 65, 117.
  Kantz, H. (1994). "A robust method to estimate the maximal Lyapunov
  exponent of a time series." Physics Letters A 185, 77.
  Awrejcewicz, J. et al. (2018). "Quantifying Chaos by Various
  Computational Methods." Entropy 20(3), 175.
