The Three-Body (and N-Body) Problem: Concepts and Formulas


TL;DR
A reference document organizing the three-body / N-body problem of Newtonian mechanics — concepts, formulas, special solutions, and recent research (2012–2026).

What is the three-body problem? → When three or more bodies move under only their mutual gravity, there is no clean formula for predicting the future.
Why can't we solve it? → It has been proven mathematically that only 10 algebraic/analytic first integrals exist (Bruns 1887, Poincaré 1889).
Are there no exceptions? → Exact solutions do exist for special configurations: Lagrange's equilateral solution, Euler's collinear solution, the figure-eight orbit, etc.
Then why does the Solar System look stable? → Because the Sun holds about 99.8% of the total mass, so it is effectively approximated as several separate two-body problems.
How does it become unpredictable? → Sensitivity to initial conditions measured by the Lyapunov exponent (λ>0) — the "butterfly effect."
What's new recently? → In 2025 alone, 10,059 new periodic orbits were discovered, machine-learning-based searches, and the completion of the Painlevé conjecture after more than 100 years (Xue 2020).

The document proceeds: basic concepts (conserved quantities, special solutions) → restricted three-body problem → chaos and non-integrability → N-body extensions → recent research. (You can run it directly in Simulation 1: N-Body 3D · Simulation 2: N-body orbits 2D.)



## The Three-Body Problem, Put Very Simply

**The key is "how much the mass is concentrated on one side."**

**① Two bodies of similar mass?**  
Even if the two stars have similar masses, if there are **only two** bodies there is no problem. Newton already left us a perfect formula.

F = G m₁m₂ / r²   ⟹   r(θ) = p / (1 + e·cosθ)   ⟹   T² = 4π² a³ / (G(m₁+m₂))



Starting from a single law of gravity, the orbit of two bodies is **always a clean ellipse (conic section)**, and the orbital period falls exactly out of Kepler's third law. (Binary star systems are the classic example.)

**② But three bodies of similar mass?**  
Add one more star of similar mass so that all three pull on each other equally, and the problem changes completely. It has been proven mathematically that there is no way to express the future as a clean algebraic formula, and a "butterfly effect" appears in which a tiny initial difference grows explosively over time. Mathematicians call the rate at which this error grows the **Lyapunov exponent (λ)** — λ>0 means chaos, λ<0 means stability.

Words alone don't convey it, so let's actually perturb the initial positions of three stars by just **one part in 100,000 (10⁻⁶)** and run Newton's equations directly:

|Time|Position difference between the two universes|Relative to the start|

|t=0|0.000001|1×|

|t=8|0.0000574|57×|

|t=12|0.0000434|43×|

|t=12.5|0.0000525|52×|

|**t=13**|**0.00312**|**3,120×**|

|t=14|0.0443|44,296×|

|t=15|0.0859|85,876×|

See it? Up to t=12.5 it is almost unchanged (it even shrinks a bit around 50×). But **near t=13, during just 0.5 of time**, the difference suddenly jumps by a factor of 60, and after that it diverges beyond control. This is exactly the moment when two of the three bodies pass very close to each other (a close encounter) — chaos does not grow smoothly and gradually; it comes **quietly, then all at once**.

**③ Then why does our Solar System look stable?**  
Strictly speaking, the Solar System is also an "N-body problem." But **the Sun alone holds about 99.8% of the total mass**. So the planets almost ignore each other and each orbit the Sun, much closer to "several separate two-body problems."

---

**But in fact, there is a twist to this story.**

In 1889, King Oscar II of Sweden offered a prize for the question "Is the Solar System stable?" Henri Poincaré solved the problem and won, and the judging committee (including Weierstrass) praised his paper as "a work opening a new era in celestial mechanics."

But **just before** printing was finished and distribution to the nations began, Poincaré himself discovered a decisive error in his proof. He had to urgently recall all printed copies, and the cost exceeded the prize money he had received.

And in the process of fixing this error, he discovered the **opposite** of what he had originally set out to prove — not "it is stable," but "a very small difference grows beyond control." This was the **birth of chaos theory**.

In other words, the first "answer" humanity ever obtained to this problem, after even offering a prize for it, was in fact **"a proof that there is no answer."**

---

**One-line summary**: If the mass is concentrated on one side (like the Solar System), it is effectively stable and predictable, but if three similar masses pull on each other equally (the true three-body problem), the answer is not uniquely determined and becomes extremely sensitive. What was discovered in the opposite direction while trying to prove this fact was chaos theory. This unpredictability arising from perfect rules is in fact not disorder, but a complex order we have not yet fully read.

Words alone don't convey it, so in the simulator below, press the **Lagrange solution (stable)** and **random chaos (unstable)** presets and compare them directly.

---

**Note**: The local estimate λ ≈ 2.2 in the table (for the interval t=11–13.5) is a value obtained by direct numerical integration for this particular initial condition; unlike λ=ln2 of the logistic map in the chaos document (§4), it is not a "universal constant" but a value that varies from configuration to configuration — because the timing and strength of close encounters depend on the initial condition.

## Table of Contents

**Part 1. Foundations**
1. Problem Definition and Notation
2. Newton's Equations of Motion
3. Jacobi Coordinates and Degrees of Freedom
4. Lagrangian and Hamiltonian Formulation

**Part 2. Conserved Quantities**
5. The 10 Classical Conserved Quantities
6. The Virial Theorem and the Lagrange–Jacobi Identity
7. Sundman's Inequality and the Triple-Collision Condition

**Part 3. Special Solutions**
8. Euler's Collinear Solution and Lagrange's Equilateral Triangle Solution
9. Homographic Solutions and Central Configurations
10. The Figure-Eight Orbit

**Part 4. The Restricted Three-Body Problem**
11. Basics of the RTBP
12. The Jacobi Integral and Hill's Region
13. Lagrange Points
14. Hill's Approximate Problem

**Part 5. Perturbation and KAM**
15. Foundations of Perturbation Theory
16. The KAM Theorem

**Part 6. Sundman's Theory**
17. Sundman Regularization and Series Solutions

**Part 7. Non-integrability**
18. The Bruns–Poincaré Theorem and Its Extensions

**Part 8. N-Body Extensions**
19. General N-Body Equations of Motion and Conserved Quantities
20. Von Zeipel's Theorem and Relative Equilibria
21. The Painlevé Conjecture and Non-collision Singularities
22. N-Body Generalization of Choreographic Solutions

**Part 9. Chaos**
23. The Nature of Chaos and Lyapunov Exponents
24. Poincaré Sections and the Recurrence Theorem
25. The Pythagorean Three-Body Problem

**Part 10. Computation and Numerics**
26. Symplectic Integration
27. The Barnes–Hut Algorithm
28. Computational Complexity

**Part 11. History and Recent Research**
29. Chronology of Scientific History
30. Recent Research and Open Problems

**Part 12. Recent Developments in Depth (2012–2026)**
31. The Explosive Progress of Periodic-Orbit Search
32. A New Picture of Chaos: Regular Islands and Multifractals
33. Machine Learning and AI Approaches
34. Central Configurations and Relative Equilibria: Progress on Smale's Problem 6
35. Non-collision Singularities and the Completion of the Painlevé Conjecture
36. Practical Applications of KAM Theory: Toward Realistic Mass Ratios
37. Other Recent Trends
 
**Appendices**
- Appendix A. Simulation Guide
- Appendix B. Summary of Key Notation
- Appendix C. References
- Appendix D. Knowledge Framework Summary
 
---

# Part 1. Foundations

## 1. Problem Definition and Notation

The three-body problem studies the motion of three point masses interacting solely through mutual gravitational attraction. The N-body problem generalizes this to N point masses.

**Notation:**

| Symbol | Meaning |


| $m_i$ | Mass of the $i$-th body |

| $\mathbf{r}_i$ | Position vector of the $i$-th body |

| $\mathbf{p}_i$ | Momentum of the $i$-th body |

| $\mathbf{v}_i$ | Velocity of the $i$-th body |

| $\mathbf{a}_i$ | Acceleration of the $i$-th body |

| $G$ | Gravitational constant |

| $t$ | Time |

| $N$ | Number of bodies |

---

## 2. Newton's Equations of Motion

### 2.1 Component Form (Three-Body Case, $N=3$)

$$\ddot{\mathbf{r}}_1 = -Gm_2\frac{\mathbf{r}_1-\mathbf{r}_2}{|\mathbf{r}_1-\mathbf{r}_2|^3} - Gm_3\frac{\mathbf{r}_1-\mathbf{r}_3}{|\mathbf{r}_1-\mathbf{r}_3|^3}$$
$$\ddot{\mathbf{r}}_2 = -Gm_3\frac{\mathbf{r}_2-\mathbf{r}_3}{|\mathbf{r}_2-\mathbf{r}_3|^3} - Gm_1\frac{\mathbf{r}_2-\mathbf{r}_1}{|\mathbf{r}_2-\mathbf{r}_1|^3}$$
$$\ddot{\mathbf{r}}_3 = -Gm_1\frac{\mathbf{r}_3-\mathbf{r}_1}{|\mathbf{r}_3-\mathbf{r}_1|^3} - Gm_2\frac{\mathbf{r}_3-\mathbf{r}_2}{|\mathbf{r}_3-\mathbf{r}_2|^3}$$

**Unicode notation:**
```text
r̈₁ = −G m₂ (r₁ − r₂)/|r₁ − r₂|³ − G m₃ (r₁ − r₃)/|r₁ − r₃|³
r̈₂ = −G m₃ (r₂ − r₃)/|r₂ − r₃|³ − G m₁ (r₂ − r₁)/|r₂ − r₁|³
r̈₃ = −G m₁ (r₃ − r₁)/|r₃ − r₁|³ − G m₂ (r₃ − r₂)/|r₃ − r₂|³
```

### 2.2 Unified Form (Force, General N-Body)

$$m_i \frac{d^2\mathbf{r}_i}{dt^2} = \sum_{j\neq i} \frac{Gm_im_j(\mathbf{r}_j-\mathbf{r}_i)}{|\mathbf{r}_j-\mathbf{r}_i|^3}, \qquad i=1,2,\dots,N$$

```text
mᵢ d²rᵢ/dt² = Σ_{j≠i} G mᵢ mⱼ (rⱼ − rᵢ)/|rⱼ − rᵢ|³,   i = 1, …, N
```

### 2.3 Unified Form (Acceleration, General N-Body)

$$\ddot{\mathbf{r}}_i = G\sum_{j\neq i}\frac{m_j(\mathbf{r}_j-\mathbf{r}_i)}{|\mathbf{r}_j-\mathbf{r}_i|^3}$$

```text
r̈ᵢ = G Σ_{j≠i} mⱼ (rⱼ − rᵢ)/|rⱼ − rᵢ|³
```

**Dimension summary:**
- 3 second-order vector ODEs (three-body) = 18 first-order scalar ODEs
- N second-order vector ODEs (N-body) = 6N first-order scalar ODEs

---

## 3. Jacobi Coordinates and Degrees of Freedom

### 3.1 Jacobi Coordinates

To simplify computation, a coordinate system that separates out the center-of-mass motion is used, employing the relative position vector and the vector from the two-body center of mass to the third body:

$$\boldsymbol{\rho}_1 = \mathbf{r}_2 - \mathbf{r}_1$$
$$\boldsymbol{\rho}_2 = \mathbf{r}_3 - \frac{m_1\mathbf{r}_1+m_2\mathbf{r}_2}{m_1+m_2}$$

```text
ρ₁ = r₂ − r₁
ρ₂ = r₃ − (m₁r₁ + m₂r₂)/(m₁+m₂)
```

With this coordinate system, the center-of-mass motion (6 degrees of freedom) automatically separates out, reducing the effective dimension of the problem.

### 3.2 Degrees of Freedom and Phase-Space Dimension

The general three-body problem, in 3-dimensional space, has $3\times3=9$ position coordinates and 9 velocity coordinates, for a total of an **18-dimensional phase space**. This can be reduced using center-of-mass motion (6), rotational symmetry (dimension reduction from conservation of angular momentum), energy conservation, and time-translation symmetry.

General N-body case: the phase-space dimension is $6N$.

---

## 4. Lagrangian and Hamiltonian Formulation

### 4.1 The Lagrangian

$$L = T-U = \frac{1}{2}\sum_{i=1}^{N}m_i|\dot{\mathbf{r}}_i|^2 + G\sum_{i<j}\frac{m_im_j}{r_{ij}}$$

```text
L = T − U = ½ Σᵢ mᵢ |ṙᵢ|² + G Σ_{i<j} mᵢmⱼ/rᵢⱼ
```

Here the kinetic energy $T$ and potential energy $U=-G\sum_{i<j}m_im_j/r_{ij}$ (negative-sign convention) are used.

### 4.2 The Hamiltonian

Introducing the canonical momentum $\mathbf{p}_i = m_i\dot{\mathbf{r}}_i$:

$$\mathcal{H} = \sum_{i=1}^{N}\frac{|\mathbf{p}_i|^2}{2m_i} - \sum_{1\le i<j\le N}\frac{Gm_im_j}{|\mathbf{r}_i-\mathbf{r}_j|}$$

```text
ℋ = Σᵢ pᵢ²/(2mᵢ) − Σ_{i<j} G mᵢ mⱼ/|rᵢ − rⱼ|
```

### 4.3 Hamilton's Canonical Equations

$$\dot{\mathbf{r}}_i = \frac{\partial \mathcal{H}}{\partial \mathbf{p}_i}, \qquad \dot{\mathbf{p}}_i = -\frac{\partial \mathcal{H}}{\partial \mathbf{r}_i}$$

> **[Simulation]** In Simulation 1's "real-time calculation panel," you can watch Newton's equations and Verlet integration in action.

---

# Part 2. Conserved Quantities

## 5. The 10 Classical Conserved Quantities

Bruns (1887) and Poincaré (1889) proved that the only independent integrals of motion expressible as algebraic (or single-valued analytic) functions of the coordinates and their derivatives are the following 10.

### 5.1 Center-of-Mass Motion (6: 3 position + 3 velocity)

$$\mathbf{R}_{cm}(t) = \frac{1}{M}\sum_{i=1}^{N}m_i\mathbf{r}_i = \mathbf{V}_{cm}\,t+\mathbf{R}_0, \qquad M=\sum_{i=1}^{N}m_i$$

```text
R_cm(t) = (1/M) Σᵢ mᵢ rᵢ = V_cm t + R₀,   M = Σᵢ mᵢ
```

### 5.2 Conservation of Linear Momentum (contained in the 3 center-of-mass velocity components)

$$\mathbf{P} = \sum_{i=1}^{N}m_i\dot{\mathbf{r}}_i = M\mathbf{V}_{cm} = \text{const.}$$

### 5.3 Conservation of Angular Momentum (3)

$$\mathbf{L} = \sum_{i=1}^{N}m_i(\mathbf{r}_i\times\dot{\mathbf{r}}_i) = \text{const.}$$

### 5.4 Conservation of Energy (1)

$$E = T+U = \text{const.}$$

where:
- Kinetic energy: $T = \frac{1}{2}\sum_{i=1}^{N}m_i|\dot{\mathbf{r}}_i|^2$
- Potential energy (negative-sign convention): $U = -\sum_{1\le i<j\le N}\dfrac{Gm_im_j}{|\mathbf{r}_i-\mathbf{r}_j|}$

**A total of 10.** According to the Bruns–Poincaré theorem, these 10 are all the algebraically independent integrals that exist, and no further new (algebraic) general integrals exist. This result is one of the reasons the three-body problem is called "non-integrable."

**Deficiency of integrals:**

| N | Integrals needed (6N) | Integrals known | Integrals missing |
 
 | 2 | 12 | 10 | 2 |

| 3 | 18 | 10 | 8 |

| 4 | 24 | 10 | 14 |

| 5 | 30 | 10 | 20 |

---

## 6. The Virial Theorem and the Lagrange–Jacobi Identity

### 6.1 Moment of Inertia

In the center-of-mass frame:

$$I = \sum_{i=1}^{N}m_i|\mathbf{r}_i|^2 = \frac{1}{M}\sum_{i<j}m_im_j r_{ij}^2$$

### 6.2 The Lagrange–Jacobi Identity

When the potential $U$ is a homogeneous function of degree $k$ (for Newtonian gravity, $k=-1$):

$$\ddot{I} = 4T - 2kU = 4\mathcal{H} - 2(k+2)U$$

For Newtonian gravity ($k=-1$, $\mathcal{H}=E$):

$$\ddot{I} = 4T+2U = 4E-2U$$

> **Sign note (footnote):** This document uses $U=-G\sum m_im_j/r_{ij}$ (negative-sign convention). In sources that use the positive-sign convention $V=-U$, the same physics is written as $\ddot I = 4T-2V = 4E+2V$. The two expressions differ only in sign and describe the same content.

### 6.3 The Virial Theorem

Taking the time average (for a system undergoing bounded motion):

$$2\langle T\rangle + \langle U\rangle = 0$$

---

## 7. Sundman's Inequality and the Triple-Collision Condition

### 7.1 Sundman's Inequality

In the frame where the center of mass is fixed at the origin, defining $I=|x|^2$, $J=x\cdot y$, $K=|y|^2$ (where $x$ is the mass-weighted position and $y$ is the mass-weighted velocity):

$$IK-J^2 \ge |C|^2$$

where $C$ is the angular momentum. This is derived from the Cauchy–Schwarz inequality and is a key tool for analyzing the global behavior of the system (collision, escape).

### 7.2 Triple-Collision Condition (Sundman–Birkhoff)

- A triple (total) collision can occur only when the angular momentum $C=0$.
- If $C\neq0$ and the size of the system $I$ becomes sufficiently small, one body must necessarily escape to infinity.

> **[Simulation]** You can observe the time evolution of E and L in Simulation 2's "conserved-quantity drift" panel.

---

# Part 3. Special Solutions

## 8. Euler's Collinear Solution and Lagrange's Equilateral Triangle Solution

In the general three-body problem, the only known **explicit (analytic) closed-form solutions** are the two families discovered by Euler and Lagrange. Both are "homographic solutions": the relative configuration of the bodies (the shape of the triangle) does not change over time, only its overall rotation and size change.

### 8.1 Euler's Collinear Solution (1767)

The three bodies always lie on a single straight line and move along **Keplerian orbits** (ellipse/circle/parabola/hyperbola). The ratio of the two distances $\lambda=r_{23}/r_{12}$ is determined as the unique positive real root of the following **quintic equation (Euler's quintic)**:

$$(m_1+m_2)\lambda^5+(3m_1+2m_2)\lambda^4+(3m_1+m_2)\lambda^3-(m_2+3m_3)\lambda^2-(2m_2+3m_3)\lambda-(m_2+m_3)=0$$

It has been proven that for every combination of masses, exactly one positive real solution exists. There are three configurations in total, determined by which body sits in the middle — these share a common origin with the collinear Lagrange points $L_1,L_2,L_3$ of the RTBP.  

### 8.2 Lagrange's Equilateral Triangle Solution (1772)

Regardless of the masses, the three bodies **always maintain an equilateral triangle**:

$$r_{12}=r_{23}=r_{31}\equiv r(t)$$

Each body traces a Keplerian ellipse (of the same eccentricity) with the common center of mass as a focus, while the whole triangle rotates, expands, and contracts.   In the circular case, the angular velocity $\omega$ is:

$$\omega^2 = \frac{G(m_1+m_2+m_3)}{r^3}$$

This satisfies a form of **Kepler's third law**, as if the total mass $M=m_1+m_2+m_3$ were concentrated at the center.  

### 8.3 Routh's Criterion (Stability Condition)

**Stability condition for $L_4/L_5$ in the RTBP:**

$$(m_1+m_2)^2 \ge 27\,m_1m_2$$

**Linear stability condition for Lagrange's equilateral solution in the general three-body problem:**

$$(m_1+m_2+m_3)^2 \ge 27\,(m_1m_2+m_2m_3+m_3m_1)$$

**Meaning:**
- When the mass ratio is sufficiently extreme (one body dominates the other two), $L_4/L_5$ is stable
- In the Sun–Jupiter system this condition is satisfied, so the Trojan asteroid groups exist at $L_4/L_5$
- Routh's critical mass ratio: $\mu_{crit}=\frac{1}{2}\left(1-\sqrt{23/27}\right)\approx0.0385$

> **[Simulation]** You can check this directly in Simulation 2's "Euler collinear solution" and "Lagrange equilateral triangle solution" presets.

---

## 9. Homographic Solutions and Central Configurations

### 9.1 Unified Representation of Homographic Solutions

Both solutions (Euler's and Lagrange's) can be expressed, on the complex plane $\mathbb{C}$, as a shape $\mathbf{q}_0$ rotated and scaled by a scalar function $\lambda(t)\in\mathbb{C}^*$:

$$\mathbf{q}(t) = \lambda(t)\,\mathbf{q}_0$$

For this condition to satisfy Newton's equations, $\lambda(t)$ must satisfy the same equation as the Kepler problem,

$$\ddot{\lambda} = -\frac{c\,\lambda}{|\lambda|^3}$$

(where $c=-U(\mathbf{q}_0)/I(\mathbf{q}_0)$), and the shape $\mathbf{q}_0$ itself must satisfy the following "shape equation":

$$\frac{c}{2}\nabla I(\mathbf{q}_0) = \nabla U(\mathbf{q}_0)$$

It is known that the solutions of this shape equation are exactly Euler's 3 collinear configurations and Lagrange's 2 equilateral-triangle configurations (mirror images), for a total of exactly 5 (**central configurations**).

### 9.2 Central Configurations — General N-Body Case

**Definition:** A configuration $(\mathbf{r}_1,\dots,\mathbf{r}_N)$ is called a central configuration if it satisfies (relative to the center of mass $\mathbf{c}$):

$$\lambda(\mathbf{r}_i-\mathbf{c}) = \sum_{j\neq i}\frac{Gm_j}{r_{ij}^3}(\mathbf{r}_i-\mathbf{r}_j) \equiv \frac{1}{m_i}\frac{\partial U}{\partial \mathbf{r}_i}, \qquad i=1,\dots,N$$

where $\lambda$ is a constant (Lagrange multiplier) that is the same for all $i$. This is equivalent to the condition that "the force acting on each body is proportional to its position vector from the center of mass." In matrix form:

$$M^{-1}\frac{\partial U}{\partial \mathbf{Q}} = \lambda\mathbf{Q}$$

Since the potential $U$ is a homogeneous function of degree $-1$, by Euler's homogeneous function theorem:

$$\lambda = -\frac{U(\mathbf{q})}{\mathbf{q}^T M\mathbf{q}} = -\frac{U}{I}$$

**Physical meaning:** If, at a central configuration, we give appropriate initial velocities (velocities proportional to the size of the configuration by the same ratio $\gamma$ for all bodies, all at the same angle), the entire configuration remains self-similar while rotating and expanding/contracting, giving a **homographic solution** — the Euler/Lagrange solutions are the case $N=3$.

**Pair-space perspective:** The equivalent condition for a central configuration is that the pair angular momentum $\mathbf{L}_{ij}=\mu_{ij}(\mathbf{q}_{ij}\times\dot{\mathbf{q}}_{ij})$ of the relative position vectors $\mathbf{q}_{ij}=\mathbf{r}_i-\mathbf{r}_j$ is **conserved for every pair**:

$$\ddot{\mathbf{q}}_{ij} = -\lambda_{ij}\,\mathbf{q}_{ij}, \qquad \lambda_{ij}=\lambda_{ji}$$

### 9.3 The Number of Central Configurations — an Open Problem

| N | Result |
 
| 3 | Exactly 5 (3 Euler + 2 Lagrange, independent of mass) |

| 4 | Finite (Hampton–Moeckel, 2006, computer-assisted proof) |

| ≥5 | **Open** — Smale's 21st-century Problem #6 |

---

## 10. The Figure-Eight Orbit

### 10.1 Overview

Discovered numerically by Cristopher Moore in 1993, and proven to exist by Chenciner and Montgomery in 2000 using variational methods, this is a choreographic solution in which three equal masses, with zero total angular momentum, chase one another along a **single fixed figure-eight curve**. It is one of the few periodic solutions whose stability has been numerically confirmed.

>  The figure-eight solution is no longer "one of the few" stable periodic solutions. Since 2013, tens of thousands to hundreds of thousands of new periodic solutions have been reported (§31), with well over a thousand reported as linearly stable. What makes the figure-eight solution special lies in its *variational existence proof* (Chenciner–Montgomery 2000) and *rigorous KAM stability proof* (Kapela–Simó 2017).

### 10.2 Simó's (2000) Exact Initial Values (equal masses $m=1$, units with $G=1$)

**Initial positions:**
$$(x_1,y_1)=(-0.97000436,\ 0.24308753), \quad (x_2,y_2)=(0.97000436,\ -0.24308753), \quad (x_3,y_3)=(0,\ 0)$$

**Initial velocities:**
$$(\dot x_3,\dot y_3)=(0.93240737,\ 0.86473146), \qquad (\dot x_1,\dot y_1)=(\dot x_2,\dot y_2)=-\tfrac{1}{2}(\dot x_3,\dot y_3)$$

**Period** $T=6.32591398\ldots$

The initial positions are collinear with the center of mass at the origin, and the initial velocities are chosen so that the total linear and angular momentum are zero and the total moment of inertia is at an extremum (stationary point).  

### 10.3 Stability (KAM Perspective)

- **Linear stability**: numerically confirmed
- **KAM stability**: Kapela and Simó (2017) provided a rigorous computer-assisted proof
- The figure-eight solution satisfies the KAM conditions, and invariant tori exist around it
- This means the figure-eight solution is an elliptic island of stability situated within a chaotic region

### 10.4 Features and Limitations

- It has been numerically confirmed that fourth-, sixth-, and eighth-degree polynomials cannot exactly represent the figure-eight trajectory.
- To date, **no closed-form analytic expression** for the figure-eight orbit has been found — its existence has been proven only by variational methods (minimization of the action functional); there is no explicit formula.
- It has been numerically confirmed to be (linearly) stable under Newtonian gravity.

### 10.5 General Definition of a Choreography

A solution in which $N$ equal masses follow a single closed curve $\gamma(t)$ offset from each other by a time delay of $T/N$:

$$\mathbf{r}_k(t) = \gamma\!\left(t+\frac{(k-1)T}{N}\right), \qquad k=1,\dots,N$$

The figure-eight orbit is the representative example for $N=3$.

> **[Simulation]** You can check this directly in Simulation 1's "Figure-8" preset and Simulation 2's "figure-eight orbit" preset.

---

# Part 4. The Restricted Three-Body Problem

## 11. Basics of the RTBP

This deals with the case where two large masses (the "primaries") orbit each other in circular orbits, and a third body of negligible mass moves within their gravitational field.

### 11.1 Normalized Unit System

- Sum of the two primaries' masses: $m_1+m_2=1$
- Distance between the two bodies: $=1$
- Orbital angular velocity: $=1$
- Mass-ratio parameter: $\mu=\dfrac{m_2}{m_1+m_2}$ (by convention $m_2\le m_1$)

### 11.2 Equations of Motion in the Rotating Frame

In the frame (synodic frame) rotating together with the two primaries, letting the coordinates of the third (massless) body be $(x,y,z)$:

$$\ddot{x}-2\dot{y}=\frac{\partial\Omega}{\partial x}, \qquad \ddot{y}+2\dot{x}=\frac{\partial\Omega}{\partial y}, \qquad \ddot{z}=\frac{\partial\Omega}{\partial z}$$

The terms $-2\dot y$ and $+2\dot x$ on the left arise from the Coriolis force, and the $\tfrac12(x^2+y^2)$ term in $\Omega$ arises from the centrifugal potential.

### 11.3 The Effective Potential

$$\Omega(x,y,z) = \frac{1}{2}(x^2+y^2) + \frac{1-\mu}{r_1} + \frac{\mu}{r_2} + \frac{1}{2}\mu(1-\mu)$$

(The last constant term is sometimes omitted, depending on convention.)

$$r_1=\sqrt{(x+\mu)^2+y^2+z^2}, \qquad r_2=\sqrt{(x-1+\mu)^2+y^2+z^2}$$

Here $r_1$ is the distance to the larger primary ($m_1$, at coordinates $(-\mu,0,0)$), and $r_2$ is the distance to the smaller primary ($m_2$, at coordinates $(1-\mu,0,0)$).

### 11.4 Circular vs. Elliptic RTBP

- **CR3BP** (Circular Restricted Three-Body Problem): the two primaries follow circular orbits — the equations above correspond to this case.
- **ER3BP** (Elliptic Restricted Three-Body Problem): when the two primaries follow elliptical orbits with eccentricity $e$, the equations become time-dependent (non-autonomous), and it is common to use the true anomaly $\nu$ as the independent variable:

$$x''-2y' = \frac{1}{1+e\cos\nu}\frac{\partial\Omega}{\partial x}, \qquad \cdots$$

---

## 12. The Jacobi Integral and Hill's Region

### 12.1 The Jacobi Integral

The only known constant of motion in the CR3BP, in the rotating frame:

$$C_J = 2\Omega(x,y,z) - (\dot x^2+\dot y^2+\dot z^2) = \text{const.}$$

Expanded:

$$C_J = x^2+y^2+\frac{2(1-\mu)}{r_1}+\frac{2\mu}{r_2}-(\dot x^2+\dot y^2+\dot z^2)$$

### 12.2 Hill's Region

For a given value of $C_J$, the region reachable by the body:

$$\{(x,y,z) : 2\Omega(x,y,z) \ge C_J\}$$

The boundary surface (where the velocity becomes zero) is called the **zero-velocity surface**, defined by the equation:

$$2\Omega(x,y,z) = C_J$$

This surface plays a central role in determining reachable regions for spacecraft trajectory design (e.g., halo orbits near Lagrange points).

---

## 13. Lagrange Points

Equilibrium points are where $\nabla\Omega=0$, i.e., points where the acceleration vanishes in the rotating frame ($\dot x=\dot y=\ddot x=\ddot y=0$).

### 13.1 The Collinear Points $L_1,L_2,L_3$ (Euler's collinear points)

On the axis $y=z=0$, given as solutions of:

$$x - \frac{(1-\mu)(x+\mu)}{|x+\mu|^3} - \frac{\mu(x-1+\mu)}{|x-1+\mu|^3} = 0$$

This is effectively a quintic equation, with three real roots $L_1,L_2,L_3$.

**Approximate positions** (for mass ratio $\mu\ll1$, using the Hill radius $r_H=(\mu/3)^{1/3}$):

$$L_1\approx1-\mu-r_H, \qquad L_2\approx1-\mu+r_H, \qquad L_3\approx-1-\frac{5\mu}{12}$$

### 13.2 The Triangular Points $L_4,L_5$ (Lagrange's equilateral points)

$$x=\frac12-\mu, \qquad y=\pm\frac{\sqrt3}{2}, \qquad z=0$$

That is, $r_1=r_2=1$ — the three bodies ($m_1$, $m_2$, and the test mass) always form an **equilateral triangle**.

### 13.3 Linear Stability of the Lagrange Points

Introducing small perturbations $(\xi,\eta)$ near each equilibrium point and linearizing:

$$\ddot\xi-2\dot\eta=\Omega_{xx}^0\,\xi+\Omega_{xy}^0\,\eta$$
$$\ddot\eta+2\dot\xi=\Omega_{xy}^0\,\xi+\Omega_{yy}^0\,\eta$$

Assuming a solution $\xi,\eta\propto e^{\lambda t}$, the characteristic equation is:

$$\lambda^4+(4-\Omega_{xx}^0-\Omega_{yy}^0)\lambda^2+\left(\Omega_{xx}^0\Omega_{yy}^0-(\Omega_{xy}^0)^2\right)=0$$

**Results:**
- $L_1,L_2,L_3$: always unstable (a positive real root always exists)
- $L_4,L_5$: (linearly) stable if the mass ratio satisfies

$$\mu<\mu_{crit}=\frac12\left(1-\sqrt{23/27}\right)\approx0.0385$$

### 13.4 Real-World Examples

- In the Jupiter–Sun system, the Earth–Moon system, and most actual celestial systems, this condition is satisfied, so Trojan asteroid groups exist near $L_4,L_5$. 
- The James Webb Space Telescope operates near the Sun–Earth $L_2$ point.

### 13.5 Modern Research Supplement

Recent research provides a unified analytical framework for Lissajous orbits, halo orbits, and quasi-halo orbits near Lagrange points.

> "It is not frequency resonance but nonlinear coupling that is the true cause of orbital bifurcation."

> **[Simulation]** You can check the Lagrange points and related orbits in Simulation 1's "Solar System" preset.

---

## 14. Hill's Approximate Problem

Taking the limit in the RTBP where $\mu\to0$ while the third body remains near the smaller primary ($m_2$) yields these local approximate equations (introduced by Hill for studying lunar motion).

$$\ddot x-2\dot y=3x-\frac{x}{\rho^3}, \qquad \ddot y+2\dot x=-\frac{y}{\rho^3}, \qquad \ddot z=-z-\frac{z}{\rho^3}$$

where $\rho=\sqrt{x^2+y^2+z^2}$, and the coordinate origin is fixed at the smaller primary. Hill's counterpart to the Jacobi integral:

$$C_H = 3x^2-z^2+\frac{2}{\rho}-(\dot x^2+\dot y^2+\dot z^2)$$

This approximation is widely used for satellites or asteroids passing close to a planet (flybys), or for stability analysis of satellite systems.

---

# Part 5. Perturbation and KAM

## 15. Foundations of Perturbation Theory

When one mass dominates overwhelmingly (as in Sun–planet–moon systems), the problem is treated as a perturbation of Keplerian motion.

### 15.1 The Disturbing Function

When body 1 is the central body and body 2 is the perturbing body, the disturbing function for body 3 (or body 1):

$$R = Gm_2\left(\frac{1}{\Delta}-\frac{\mathbf{r}\cdot\mathbf{r}_2}{r_2^3}\right)$$

where $\Delta=|\mathbf{r}-\mathbf{r}_2|$, and the second term on the right is an indirect term arising when the coordinate origin is placed at the primary body.

### 15.2 Lagrange's Planetary Equations (rates of change of orbital elements)

For the semi-major axis $a$, eccentricity $e$, inclination $i$, etc. (e.g., for the semi-major axis):

$$\frac{da}{dt} = \frac{2}{na}\frac{\partial R}{\partial M}$$

where $n$ is the mean motion and $M$ is the mean anomaly. Similar equations exist for each of $e,i,\Omega,\omega,M$ (the six standard equations of perturbation theory).

---

## 16. The KAM Theorem

### 16.1 Core Content

- Proposed by Kolmogorov (1954), resolved by Arnold and Moser
- Under a small perturbation, tori with sufficiently irrational frequency ratios are not destroyed but only deformed
- Tori with rationally resonant frequencies are completely destroyed and become chaotic regions
- Stable tori are not dense in phase space, but occupy a subset whose measure approaches 1

### 16.2 The Diophantine Condition

$$|\omega\cdot l| > \frac{\gamma}{\langle l\rangle^\tau}, \qquad \forall l\in\mathbb{Z}^d\setminus\{0\}$$

where $\gamma\in(0,1)$, $\tau>d-1$, $\langle l\rangle=\max(1,|l|)$.

### 16.3 The Non-degeneracy Condition (Twist Condition)

$$\det\left(\frac{\partial^2 h}{\partial I_i\partial I_j}(I^*)\right)\neq0$$

### 16.4 Conclusion

$$\exists\,\varepsilon_0>0 : |\varepsilon|<\varepsilon_0 \implies \text{invariant tori survive}$$

Measure of the Cantor set: $|C|\to1$ (as $\varepsilon\to0$)

### 16.5 Application to the Three-Body Problem

- **Arnold (1963)**: applied the KAM theorem to the planar planetary three-body problem, proving the existence of quasi-periodic solutions
- **Original applicability condition**: mass ratio $<10^{-300}$ (derived by Hénon as a necessary condition from Arnold's proof)
- **Recent improvement**: Castan (2017, PhD thesis at Université Paris VI, *"Stability in the plane, planetary three-body problem"*) proved that a mass ratio up to $<10^{-85}$ is achievable (a sufficient condition)  
- This is far more stringent than the **actual mass ratio in the Solar System** (Jupiter/Sun $\approx10^{-3}$), but is significant as a mathematical existence proof

>(1) Hénon's check value is cited in the literature as approximately $10^{-333}$ for the *restricted* three-body problem. (2) Castan's (2017) $\approx10^{-85}$ can be raised, since it is independently cited by Figueras–Haro (2024/25) as "a quantitative Arnold theorem, computer-assisted, for the planar three-body problem." In a planar Sun–Jupiter–Saturn model at the actual mass ratio ($10^{-3}$), the KAM condition has been numerically verified (§36).

### 16.6 N-Body Extension (the 1+N-Body Problem)

- KAM can be applied to the "1+N-body problem" (1 large body + N small bodies)
- Zeroth-order Hamiltonian: the sum of N separate two-body problems (completely integrable)
- Perturbation: mass ratio $\varepsilon$
- The KAM condition becomes more stringent as N grows (shrinking exponentially)

---

# Part 6. Sundman's Theory

## 17. Sundman Regularization and Series Solutions

### 17.1 Sundman Regularization

The Finnish mathematician Karl Sundman (1907–1912) introduced a new independent variable $\tau$ to remove the two-body collision singularity:

$$\frac{d\tau}{dt}=\frac{1}{r}, \qquad \text{or the reparametrization} \quad s=|t_1-t|^{1/3}$$

where $t_1$ is the time at which the two-body collision occurs. Through this reparametrization, the singularity is removed, and the coordinates become analytic functions expandable in powers of $\tau$ (or $s$).

### 17.2 The Sundman Series Solution

For initial conditions without a triple collision (angular momentum $C\neq0$), Sundman constructed a series solution of the following form that **converges for all real time**:

$$\mathbf{r}_i(t) = \sum_{k=0}^{\infty}\mathbf{c}_k\,\tau^k$$

(In the original time variable, this takes the form of powers of $t^{1/3}$.)

### 17.3 Sundman Estimates

For a pair of bodies colliding at time $t_0$:

$$\|\mathbf{r}_i-\mathbf{r}_j\| = O(|t-t_0|^{2/3}), \qquad \|\dot{\mathbf{r}}_i-\dot{\mathbf{r}}_j\| = O(|t-t_0|^{-1/3})$$

### 17.4 Practical Limitations

- Although this series is theoretically a complete general solution, its convergence is extremely slow, making it nearly useless for practical computation.
- Belorizky's (1930) estimate: to achieve accuracy comparable to observational precision, roughly $10^{8{,}000{,}000}$ terms would be needed.
- It is generally accepted, therefore, that this solution is useful for neither qualitative insight nor practical numerical computation.

### 17.5 Relation to Non-integrability

Sundman's series solution does not contradict the non-integrability theorems — Sundman's solution converges as a function not of time $t$ but of the reparametrized variable $\tau$, and since the relationship between $\tau$ and $t$ is itself part of the solution, this is a result on a different level from the "first integral as a function of the coordinates" discussed by Bruns and Poincaré.

---

# Part 7. Non-integrability

## 18. The Bruns–Poincaré Theorem and Its Extensions

### 18.1 Bruns's Theorem (1887)

The equations of motion of the three-body problem have no independent first integrals other than the 10 (6 center-of-mass, 3 angular momentum, 1 energy) expressible as **algebraic functions** of the coordinates and their derivatives.

### 18.2 Poincaré's Theorem (1889/1892)

Poincaré further proved that the equations of motion of the three-body problem admit no new independent integral expressible as a **single-valued analytic function** (including transcendental functions) of the coordinates. This was Poincaré's answer to King Oscar II's Prize (1889), and it later became the starting point for chaos theory.

### 18.3 Painlevé's Theorem (1898)

Proved that no new integral exists in the form of an algebraic function of the velocity components either.

### 18.4 Siegel's Theorem (1941)

Proved that in the planar circular restricted three-body problem, no new algebraic integral exists beyond the Jacobi integral.

### 18.5 Summary of Historical Results

| Year | Researcher | Result | 

| 1843 | Jacobi | The problem could be solved if all but 2 of the remaining 8 integrals were found |

| 1887 | Bruns | No new algebraic integral exists when coordinates and velocity components are used as the basic variables |

| 1889 | Poincaré | No new single-valued analytic integral exists when combinations of orbital elements are used as variables |

| 1898 | Painlevé | No new integral in the form of an algebraic function of the velocity components exists either |

| 1941 | Siegel | In the planar circular restricted three-body problem, no new algebraic integral exists beyond the Jacobi integral |

---

# Part 8. N-Body Extensions

## 19. General N-Body Equations of Motion and Conserved Quantities

### 19.1 General N-Body Equations of Motion

$$m_i\frac{d^2\mathbf{r}_i}{dt^2} = \sum_{j\neq i}\frac{Gm_im_j(\mathbf{r}_j-\mathbf{r}_i)}{|\mathbf{r}_j-\mathbf{r}_i|^3}, \qquad i=1,2,\dots,N$$

or, using the Newtonian potential $U=G\sum_{1\le i<j\le N}m_im_j/r_{ij}$ (**positive-sign convention**):

$$m_i\ddot{\mathbf{r}}_i = \frac{\partial U}{\partial \mathbf{r}_i}, \qquad i=1,\dots,N$$

> **Sign note**: Since the main text of this document uses the negative-sign convention $U=-G\sum m_im_j/r_{ij}$, the equation in this section becomes $m_i\ddot{\mathbf{r}}_i=-\partial U/\partial\mathbf{r}_i$ under the main text's convention. Because the original source (Document 1, §19.1) uses the positive-sign convention only in this section, it has been left as-is to avoid confusion, and this footnote clarifies the conversion.

The phase-space dimension is $6N$, and the equations are defined on the configuration space excluding the collision set $\Delta=\{r_{ij}=0 \text{ for some } i\neq j\}$.

### 19.2 Conserved Quantities (10, independent of N)

**Center of mass:**
$$\mathbf{R}_{cm}(t) = \frac{1}{M}\sum_{i=1}^N m_i\mathbf{r}_i = \mathbf{V}_{cm}\,t+\mathbf{R}_0, \qquad M=\sum_{i=1}^N m_i$$

**Angular momentum:**
$$\mathbf{L} = \sum_{i=1}^N m_i(\mathbf{r}_i\times\dot{\mathbf{r}}_i) = \text{const.}$$

**Energy:**
$$E = \sum_{i=1}^N \frac{1}{2}m_i|\dot{\mathbf{r}}_i|^2 - U = \text{const.}$$

Bruns's theorem (1887) was originally proven for the N-body case (particularly $N=3$), and guarantees that **the only independent first integrals expressible as algebraic functions are the above 10** (6 center-of-mass, 3 angular momentum, 1 energy). This number does not increase as N grows.

---

## 20. Von Zeipel's Theorem and Relative Equilibria

### 20.1 Von Zeipel's Theorem (1908)

For the moment of inertia $I=\sum_i m_i|\mathbf{r}_i-\mathbf{R}_{cm}|^2$:

$$\ddot I = 4T+2U = 4E-2U$$

From this we derive **von Zeipel's theorem**: for a singularity that is not a collision singularity (a non-collision singularity) to exist, the maximum mutual distance $D(t)=\max_{i,j}r_{ij}(t)$ and the minimum mutual distance $d(t)=\min_{i,j}r_{ij}(t)$ must, at some finite time $t^*$, simultaneously satisfy

$$\limsup_{t\to t^*}D(t)=\infty, \qquad \liminf_{t\to t^*}d(t)=0$$

That is, at a non-collision singularity, some body must necessarily escape to infinity within finite time.

### 20.2 Relative Equilibria

**Definition:** A solution in which all point masses rotate about the common center of mass without changing their relative positions.

- $N=3$: Lagrange points (5 of them)
- Regular-N-gon solutions: N equal masses rotating at the vertices of a regular N-gon
- **Wintner's question**: Is the number of relative equilibria finite for given positive masses?
  - $N=3$: finite (5)
  - $N=4$: classification complete for the equal-mass case (Albouy)
  - $N\ge5$: **open** (one of Smale's 21st-century problems)
  - Roberts (1999): showed that continuum relative equilibria exist in a five-body problem including negative masses
  - Hamilton & Moeckel (2006): proved finiteness for $N=5$ (excluding a specific codimension submanifold)

 

---

## 21. The Painlevé Conjecture and Non-collision Singularities

According to von Zeipel's theorem, non-collision singularities require a body to escape, which seems intuitively strange. Nonetheless:

- **Painlevé's theorem (1897):** For $N\le3$, every finite-time singularity is a collision singularity (no non-collision singularities exist).
- **Painlevé's conjecture:** For $N\ge4$, non-collision singularities exist (e.g., solutions that diverge to infinity or oscillate within finite time).
- **Xia (1988/1992):** partially proved the conjecture by constructing an explicit example of a non-collision singularity in a spatial (3-dimensional) $N=5$ problem.
- **Gerver (1991):** presented an example of a non-collision singularity in the planar (2-dimensional) $3N$-body problem for sufficiently large $N$.
- **Xue (2014/2020):** proved that non-collision singularities exist even in the planar $N=4$ problem, which had remained open the longest, completing the Painlevé conjecture for all $N\ge4$. (Gerver's result is distinguished by having held only for "sufficiently large N.")

**Mechanism of Xia's example:** while two pairs of binary systems contract nearly to collision and fly apart to infinity, a single lightweight body caught between them oscillates back and forth between the two pairs with ever-increasing frequency and amplitude, carrying energy.

 

---

## 22. N-Body Generalization of Choreographic Solutions

- The figure-eight solution is one example of a "choreography."
- **Definition:** a solution in which N bodies move along the same curve with a constant phase offset.
- Research on the existence of N-body choreographic solutions is ongoing.
- A 2020 study: analyzed the bifurcation of the figure-eight solution using group theory, noting that it is "broadly applicable to understanding periodic solutions of the general N-body problem."
- The existence of "super-eight" solutions for the four-body problem has been proven (using the Chenciner–Montgomery method).

---

# Part 9. Chaos

## 23. The Nature of Chaos and Lyapunov Exponents

### 23.1 The Nature of Chaos

Very small differences in initial conditions are amplified exponentially over time → long-term prediction becomes essentially impossible.

### 23.2 The Lyapunov Exponent

The rate of growth over time of the distance $|\delta\mathbf{Z}(t)|$ between two neighboring trajectories in phase space:

$$\lambda_{\text{Lyap}} = \lim_{t\to\infty}\frac{1}{t}\ln\frac{|\delta\mathbf{Z}(t)|}{|\delta\mathbf{Z}(0)|}$$

If $\lambda_{\text{Lyap}}>0$, this indicates chaotic behavior that is exponentially sensitive to initial conditions. The majority of orbits in the general three-body problem have a positive Lyapunov exponent. * 

**Classification criteria:**
- $\lambda<0$ ⟺ stable
- $\lambda=0$ ⟺ periodic / neutral
- $\lambda>0$ ⟺ chaotic (unstable)

**Lyapunov time:**
$$T_{\text{Lyap}} \approx \frac{1}{\lambda}\ln\left|\frac{L}{\delta x}\right|$$

**Multidimensional Lyapunov spectrum:**
$$\lambda_i = \lim_{N\to\infty}\frac{1}{N}\log\frac{\|v_i(N)\|}{\|v_i(0)\|}$$

**Hamiltonian vs. dissipative systems:**
- Hamiltonian systems: $\sum_i\lambda_i=0$ (phase-space volume conserved)
- Dissipative systems: $\sum_i\lambda_i<0$ (phase-space volume contracts)

**Kaplan–Yorke dimension:**
$$D_{KY} = j + \frac{\sum_{i=1}^{j}\lambda_i}{|\lambda_{j+1}|}$$

where $j$ is the largest integer satisfying $\sum_{i=1}^{j}\lambda_i\ge0$.

> **[Simulation]** You can check this directly in Simulation 2's "chaotic twins + Lyapunov sensitivity chart."

 
---

## 24. Poincaré Sections and the Recurrence Theorem

### 24.1 The Poincaré Section

A technique for reducing a continuous flow to a discrete map, by observing the sequence $\{P_n\}$ of intersection points between a trajectory and a specific hypersurface $\Sigma$ in phase space:

$$P_{n+1} = f(P_n)$$

The existence of homoclinic intersections is used as evidence of chaos (Smale horseshoe map).

### 24.2 The Poincaré Recurrence Theorem

For a bounded trajectory of a conservative dynamical system, after a sufficiently long time, the system returns arbitrarily close to its initial state.

**Caveats:**
- The theorem does not specify the time required for recurrence
- For systems with a very large number of particles, the waiting time may exceed physically meaningful scales
- This holds equally in the N-body problem

---

## 25. The Pythagorean Three-Body Problem

- Three masses: 3, 4, 5
- Initially at rest at the vertices of a triangle with side lengths 3, 4, 5
- Tiny changes in the initial positions dramatically change the final outcome
- Chaotic motion over most of the region of initial conditions
- Only in a small number of "regular regions" do the final parameters vary continuously

 

---

# Part 10. Computation and Numerics

## 26. Symplectic Integration

### 26.1 Verlet / Leapfrog Integration

$$\mathbf{r}_i^{(n+1)} = \mathbf{r}_i^{(n)} + \mathbf{v}_i^{(n)}\Delta t + \frac12\mathbf{a}_i^{(n)}(\Delta t)^2$$
$$\mathbf{v}_i^{(n+1)} = \mathbf{v}_i^{(n)} + \mathbf{a}_i^{(n)}\Delta t$$

**Acceleration computation:**
$$\mathbf{a}_i^{(n)} = G\sum_{j\neq i}m_j\frac{\mathbf{r}_j^{(n)}-\mathbf{r}_i^{(n)}}{|\mathbf{r}_j^{(n)}-\mathbf{r}_i^{(n)}|^3}$$

### 26.2 Velocity Verlet (an equivalent form)

$$\mathbf{v}_{n+1/2} = \mathbf{v}_{n-1/2} + \mathbf{a}(\mathbf{r}_n)\,\Delta t, \qquad \mathbf{r}_{n+1} = \mathbf{r}_n + \mathbf{v}_{n+1/2}\,\Delta t$$

### 26.3 Characteristics

- Verlet / Leapfrog is a symplectic integrator.
- Long-term energy error is bounded (no secular drift).
- Well-suited for long-term simulations of conservative systems (the three-body problem, N-body problem, etc.). While it does not conserve energy exactly, it is used as a standard tool in celestial-dynamics simulations thanks to the advantage that error remains bounded over long-term simulations.  

 
 

---

## 27. The Barnes–Hut Algorithm

- Reduces $O(N^2)$ direct computation to $O(N\log N)$.
- Uses an octree (3D) or quadtree (2D).
- The $\theta$ parameter: the criterion for approximating a tree node as a single point mass.
- $\theta=0.5\sim1.0$ is standard.

> **[Simulation]** You can experience this directly with Simulation 1's "Barnes-Hut toggle + θ slider."

---

## 28. Computational Complexity

### 28.1 Core Theorem (the Sitnikov Problem)

A result proved by Vasiliev & Pavlov (2017, *Journal of Mathematical Sciences*):

- The initial value problem (IVP) of the Sitnikov problem (a special case of the restricted three-body problem, in which the two primaries follow elliptical orbits and the third body oscillates along a line perpendicular to their plane) does not have a polynomial-time upper bound (non-polynomial time complexity).
- That is, no Turing machine can compute the solution within polynomial time in the length of $t$.
- The Sitnikov problem can be reduced to the general three-body problem in polynomial time.
- Therefore, no polynomial-time solution exists for the general three-body problem either.

### 28.2 Important Caveats

- This result is a theoretical asymptotic statement.
- Even for the Sitnikov problem, no known obstacle currently prevents obtaining a solution over a sufficiently long time with practically sufficient precision.
- Separate approximation techniques may exist for special cases, such as the Solar System.

### 28.3 N-Body Extension

- No polynomial-time solution exists for the general N-body problem either.
- However, approximate polynomial-time solutions exist for special cases, such as hierarchical systems.

---

# Part 11. History and Recent Research

## 29. Chronology of Scientific History

| Year | Researcher | Achievement |
 
| 1687 | Newton | Law of universal gravitation; first formulation of the three-body problem |

| 1744 | Euler | Research on special solutions of the three-body problem |

| 1767 | Euler | Discovery of the collinear solution |

| 1772 | Lagrange | Discovery of the Lagrange points; equilateral triangle solution |

| 1843 | Jacobi | Theory of integrals |

| 1877 | Routh | Stability condition for Lagrange's solution |

| 1887 | Bruns | Impossibility of algebraic integrals |

| 1889/1892 | Poincaré | Non-integrability theorem; qualitative theory |

| 1897/1898 | Painlevé | Collision-singularity theorem; impossibility of algebraic-function integrals |

| 1907–1912 | Sundman | Regularization and general solution of the three-body problem |

| 1908 | von Zeipel | Non-collision singularity theorem |

| 1930 | Belorizky | Estimate of the practical convergence rate of Sundman's series |

| 1941 | Siegel | Non-integrability of the restricted three-body problem |

| 1954 | Kolmogorov | Proposal of the KAM theorem |

| 1962 | Moser | Completion of the KAM theorem |

| 1963 | Arnold | Application of the KAM theorem to the three-body problem |

| 1988/1992 | Xia | Construction of an $N=5$ non-collision singularity example |

| 1991 | Gerver | Non-collision singularity example for large N |

| 1993 | Moore | Numerical discovery of the figure-eight solution |

| 1999 | Roberts | Continuum relative equilibria in a five-body problem including negative masses |

| 2000 | Chenciner & Montgomery | Proof of existence of the figure-eight solution |

| 2000 | Simó | Precise initial values for the figure-eight solution |

| 2006 | Hampton & Moeckel | Finiteness of $N=4$ central configurations |

| 2017 | Kapela & Simó | Rigorous proof of KAM stability of the figure-eight solution |

| 2017 | Castan | Improved mass-ratio bound for KAM application (PhD thesis) |

| 2017 | Vasiliev & Pavlov | Proof of non-polynomial time complexity for the Sitnikov problem |

| 2014/2020 | Xue | Completion of the Painlevé conjecture ($N=4$ planar case) |

### 29.1 Supplementary Chronology (2012–2026)

| Year | Researcher | Achievement |


| 2012 | Albouy & Kaloshin | Finiteness of planar 5-body central configurations (generic masses) |

| 2013 | Šuvakov & Dmitrašinović | 11 new families of periodic solutions for equal-mass three-body systems (from 3 known families → beginning of the search era) |

| 2015 | Boekholt & Portegies Zwart | BRUTUS, an arbitrary-precision N-body code |

| 2017 | Li & Liao | 695 families of planar equal-mass periodic solutions (CNS) |

| 2018 | Li, Jing & Liao | 1,349 families for unequal-mass three-body systems |

| 2019 | Stone & Leigh | Statistical solution of the chaotic three-body problem (*Nature*) |

| 2020 | Breen et al. | Deep neural network surrogate model |

| 2020 | Boekholt, Portegies Zwart & Valtonen | Gargantuan chaos and irreversibility down to the Planck length |

| 2021 | Kol | Statistical theory based on phase-space flux |

| 2021 | Li, Li & Liao | 135,445 planar periodic orbits for arbitrary mass ratios (13,315 stable) |

| 2021 | Boekholt, Moerman & Portegies Zwart | The relativistic Pythagorean problem |

| 2024 | Trani et al. | Regular islands amid chaos, multifractals, numerical chaos |

| 2024 | Hristov et al. | 24,582 equal-mass free-fall initial conditions (12,409 distinct solutions) |

| 2024 | Montgomery | *Four Open Questions for the N-Body Problem* |

| 2024–25 | Figueras & Haro | Numerical verification of KAM conditions for the planar Sun–Jupiter–Saturn system |

| 2025 | Jensen & Leykin | Reconfirmation of finiteness for generic masses at $n\le5$ using tropical geometry |

| 2025 | Li & Liao | 10,059 three-dimensional periodic orbits, 21 3D choreographies, 273 "piano-trio" solutions (preprint) |

| 2025 | Hristov, Hristova & Tanikawa | 971 linearly stable initial conditions (preprint) |

| 2026 | Kollias & Matzakos | PINN-based periodic-orbit discovery (preprint) |


---

## 30. Recent Research and Open Problems

### 30.1 Recent Research (2017–2026)

- **Castan (2017)**: applied the KAM theorem to the planar planetary three-body problem, mass ratio $<10^{-85}$  
- **Kapela & Simó (2017)**: rigorous proof of KAM stability of the figure-eight solution (computer-assisted proof)
- **Vasiliev & Pavlov (2017)**: proved that the initial-value problem of the Sitnikov problem does not have polynomial time complexity
- **Xue (2014/2020)**: completed the Painlevé conjecture for the planar $N=4$ problem
- **Hampton & Moeckel (2006)**: proved finiteness of $N=4$ central configurations
- **2020 study**: analyzed the bifurcation of the figure-eight solution using group theory
- **(2026-09 supplement)** New developments from 2012–2026 are detailed in Part 12 (§31–§38). Summary: hundreds of thousands of newly discovered periodic solutions (§31), regular islands and multifractals (§32), machine learning (§33), central configurations (§34), completion of the Painlevé conjecture (§35), practical application of KAM (§36).

### 30.2 Open Problems

- **Smale's 21st-century Problem #6**: is the number of central configurations always finite for given masses? (open for $N\ge5$)
- **The Painlevé conjecture**: existence of non-collision singularities for general $N\ge4$ (completed for the planar $N=4$ case by Xue 2020; general $N$ remains open)
- **Application of the KAM theorem to the actual mass ratio of the Solar System ($10^{-3}$)**
- **The general existence of N-body choreographic solutions**

 

---

# Part 12. Recent Developments in Depth (2012–2026)

 

## Overview

1. **Explosion of periodic solutions (§31):** Periodic solutions, which numbered only 3 families for 300 years, have grown to tens/hundreds of thousands since 2013 (roughly 135,000 planar, roughly 24,000 equal-mass free-fall initial conditions, roughly 10,000 three-dimensional). The main drivers are *topological classification + high-precision arithmetic + supercomputing*.
2. **Reassessment of chaos (§32):** In the phase space of three-body scattering, **regular islands** where the outcome is smoothly predictable occupy roughly 28–84% (depending on setup), conflicting with statistical escape theory based on the ergodic hypothesis. This structure is multifractal and persists down to below the Planck length.
3. **Machine learning (§33):** Various attempts have been made — surrogate models, Hamiltonian/PINN networks, hybrid integrators, periodic-orbit search — but limitations in long-term prediction and periodic-orbit reproduction have been repeatedly noted.
4. **Central configurations (§34):** Finiteness has been proven for the planar 5-body case (excluding an exceptional mass set) (Albouy–Kaloshin 2012). Six or more bodies remain open, with computational-algebra and tropical-geometry approaches ongoing.
5. **Non-collision singularities (§35):** The Painlevé conjecture has been completed up to $N=4$ by Xue (2020), resolving the case for all $N\ge4$.
6. **Practical application of KAM (§36):** KAM conditions have been numerically verified for a planar Sun–Jupiter–Saturn (mass ratio $10^{-3}$) model (Figueras–Haro 2024/25). A rigorous computer-assisted proof is in progress.
7. **Other (§37–§38):** the Lucy spacecraft's Trojan-asteroid flybys (2027–), Montgomery's 2024 book

---

## 31. The Explosive Progress of Periodic-Orbit Search (2013–2025)

### 31.1 What Changed

For about 300 years after Newton, only three *families* of periodic solutions were known.

1. The Lagrange–Euler family (§8) — plus one orbit found by Moore (1993)
2. The Broucke–Hadjidemetriou–Hénon family (1970s)
3. The figure-eight family (§10; Moore 1993 → Chenciner–Montgomery 2000 → extended to rotating figure-eights)

In 2013, Šuvakov–Dmitrašinović broke this stagnation, and since then three factors have combined to increase the number of discoveries by several orders of magnitude.

- **Topological classification:** classifying orbits by elements of the free group / syzygy sequences made it possible to determine whether an orbit represents "a new family"
- **High-precision arithmetic + high-order Taylor series methods + Newton's method:** converges orbits that could not be found in double precision due to chaos (CNS, §31.6)
- **Supercomputing / parallel computation:** densely searches grids of millions to tens of millions of initial conditions

Poincaré assessed periodic solutions as essentially the only way to penetrate a region (the three-body problem) that had seemed inaccessible, and this assessment is still repeatedly cited in the opening of papers in this field.

### 31.2 Formulation of the Search Problem (equal masses, planar, zero angular momentum)

The two-parameter initial condition ("Euler half-twist initial condition") commonly used in recent search papers is as follows ($m_i=1,\ G=1$).

$$\mathbf r_1(0)=(-1,0),\quad \mathbf r_2(0)=(0,0),\quad \mathbf r_3(0)=(1,0)$$
$$\mathbf v_1(0)=\mathbf v_3(0)=(v_x,v_y),\qquad \mathbf v_2(0)=-2\,(v_x,v_y)$$

For this initial condition, total linear momentum and angular momentum are zero, and the energy is

$$E(v_x,v_y)=-\tfrac52+3\,(v_x^2+v_y^2)$$

Since bounded motion requires $E<0$, the search region is the 2-dimensional region $v_x,v_y\ge0,\ v_x^2+v_y^2<5/6$.

- $v_y=0$: collinear orbit — the **Schubart orbit** (involves collisions)
- $v_x=0$: isosceles orbit — the **Broucke orbit** (involves collisions)
- Interior of the region: collisionless orbits (including the figure-eight solution)

**Symmetry:** if a periodic orbit passes through this initial condition at $t=0$, it passes through it again at the half-period $t=T/2$, so instead of the full-period equation, the **half-period equation** can be solved, reducing the computational cost (Hristov & Hristova 2024).

> **[Cross-reference to main text · direct calculation verification]** The Simó initial values of §10.2 have the same structure (equal velocities for the two outer bodies, the middle body's velocity at $-2$ times that, collinear configuration). Computing from the values in §10.2 gives $|\mathbf v_{\text{outer}}|=0.63583\ldots$, $E=-1.28714\ldots$, and the scale-invariant period $T^*=T|E|^{3/2}=9.2377\ldots$ (linear and angular momentum are zero). This is consistent with the expression $E=-5/2+3v^2$ above. *(Computed directly for this update)*

**Scale-invariant period:** to compare orbits at different energy scales,

$$T^{*}=T\,|E|^{3/2}$$

is used. In recent studies, search-range notations such as "$T^*<80$" or "$T^*<800$" refer to this quantity.

### 31.3 Timeline of Discoveries

| Year | Study | Setting | Result | Notes |


| 2013 | Šuvakov & Dmitrašinović (PRL) | equal-mass, planar, $L=0$ | 15 initial conditions presented (13 distinct orbits). **11 new families** beyond the 3 known ones, classified into 4 classes | Introduced topological classification. Names such as Butterfly, Bumblebee, Moth, Yin-Yang |

| 2014 | Li & Liao (Sci. China) | re-verified with CNS | At least **7** of the above 15 deviate substantially from a periodic orbit after sufficiently long time → insufficient initial-value precision, unstable | Highlighted the need for high-precision verification |

| 2014 | Šuvakov & Dmitrašinović (Am. J. Phys.); Šuvakov (CMDA) | explanation of search procedure; search around the figure-eight | "A guide to hunting periodic three-body orbits"; "slaloming" search around the figure-eight | Public disclosure of methodology |

| 2015 | Hudomal | equal masses | 25 families (cited in the preface of Li–Liao 2017) | |

| 2017 | Li & Liao (Sci. China) | equal masses, $L=0$, high-precision CNS | **695 families** (of which 229 have $T\le100$ and 466 have $T>100$), over 600 newly discovered | Used a national supercomputer |

| 2018 | Dmitrašinović, Hudomal, Shibayama, Sugita (J. Phys. A) | linear stability | 16 additional stable orbits found → list of 20 | Examined the topology-dependence of Kepler's third law |

| 2018 | Li, Jing & Liao (PASJ) | unequal masses | **1,349 families (1,223 new)**, 7 classes | A tendency for the scale-invariant mean period to increase linearly with mass |

| 2019 | Li & Liao (New Astron.) | free-fall | 313 collisionless periodic-orbit initial conditions (30 equal-mass) | Revisited later (2024) |

| 2020 | Janković, Dmitrašinović, Šuvakov (CPC) | nonzero angular momentum | search guide | |

| 2021 | Li, Li & Liao (Sci. China) | arbitrary mass ratio, numerical continuation + Newton–Raphson | **135,445** new planar periodic orbits (**13,315 stable**) | search over mass-ratio space |

| 2022 | Liao et al. / Hristov et al. | roadmap for arbitrary masses (CNS + neural network) / high-precision Newton's method for equal masses | roadmap presented / 123 solutions outside the existing database of 695 (105 new topological families) | |

| 2023 | Vasiljević, Raonić, Dmitrašinović (New Astron.) | unequal masses | existence of "islands" of linearly stable orbits — a possible connection to circumbinary exoplanets is raised | title phrased as a question; conclusions are exploratory |

| 2024 | Hristov, Hristova, Dmitrašinović, Tanikawa (CMDA) | free-fall, equal-mass, $T^*<80$ | **24,582 initial conditions → 12,409 distinct solutions**, of which 236 self-dual | large expansion of the 2019 results |

| 2024 | Same authors (J. Phys. Conf. Ser.) | linear stability | All discovered free-fall orbits were **unstable** (hyperbolic–hyperbolic or hyperbolic–elliptic) → hypothesis that "collisionless equal-mass free-fall periodic orbits are unstable" | |

| 2024 | Hristov & Hristova (Astron. Comput.) | orbits passing through the Euler configuration | improved efficiency via the half-period equation | |

| 2025 | Li & Liao (Sci. China) | review | comprehensive summary of the history, classification, and CNS results of planar periodic-orbit research | introductory |

| 2025 | Li & Liao (arXiv) | **3D**, $m_1=m_2=1,\ m_3=0.1n\ (1\le n\le20)$ | **10,059** 3D periodic orbits (1,996 linearly stable, ~20%); **21 equal-mass 3D choreographies**; **273 "piano-trio" solutions**, where two equal masses share one orbit and the third follows a different orbit | preprint (2025-08)|

| 2025 | Hristov, Hristova, Tanikawa (arXiv) | equal-mass, $L=0$, planar 2D region, $T^*<800$ | **971 linearly stable** initial conditions (685 distinct solutions), 4 stable regions, syzygy-sequence patterns | preprint (2025-10) |

### 31.4 Orbit Classification: Free Groups and Syzygy Sequences

- **Free-group classification:** classifies orbits on the shape sphere (the shape space of the triangle) by the free homotopy class of closed curves avoiding the three binary-collision points. This method traces back through Moore (1993) and Montgomery (1998), and served as the criterion for judging "new families" in the 2013 search. *(General knowledge)*
- **Syzygy sequence:** a string, ordered in time, of *which body is in the middle* at each instant when the three bodies become collinear. In 2025, Hristov et al. distinguished the 4 stable regions of the equal-mass 2D domain by their sequence patterns.
  - Figure-eight region: form $(213)^{2k}$
  - Broucke region (e.g., Bumblebee): includes $(213)^2(231)^2$
  - Intermediate island regions (e.g., Moth I): includes (cyclically) $(213)^2\,2123\,(123)^2$ but not $(213\,2123\,123)^2$
  - Largest region (Schubart/S orbits, e.g., Butterfly III): includes $(213\,2123\,123)^2$ or $(2123\,123)^2$
- Stable orbits largely inherit features of the four "basic orbits" (Schubart, S, figure-eight, Broucke), and a tendency has been observed for the figure-eight orbit to appear as a "distorted figure-eight" mixed into other regions.

### 31.5 Three Levels of Stability Assessment

| Level | Meaning | Verification method | Status |
|---|---|---|---|
| **Linear (spectral) stability** | eigenvalues of the monodromy matrix lie on the unit circle | high-precision numerical computation | confirmed for thousands of orbits |
| **KAM stability** | linear stability + non-resonance condition + twist condition | non-resonance is numerically checkable; twist requires separate computation | rigorously proven for only a handful, such as the figure-eight |
| **Rigorous computer-assisted proof** | proving the above conditions via interval arithmetic | Kapela–Simó (2017) | the figure-eight solution and 2 rotating figure-eights |

- **Linear stability:** there are four key eigenvalues; for elliptic stability they take the form $e^{\pm i2\pi\omega_1},\ e^{\pm i2\pi\omega_2}\ (0<\omega_1<\omega_2<\tfrac12)$. All remaining eigenvalues equal 1 (this fact is cited based on Roberts's (2007) linear stability analysis of the figure-eight orbit).
- **Non-resonance condition (up to order 4):** there must be no integers $(k_0,k_1,k_2)$ with $0<|k_1|+|k_2|\le4$ satisfying $k_1\omega_1+k_2\omega_2=k_0$.
- In 2025, Hristov et al. confirmed that all 971 linearly stable initial conditions **satisfy the non-resonance condition**, and, showing no deviation over 100 periods and long-time integration up to $t^*=10^6$, presented them as "KAM stability candidates." Verification of the twist condition remains for future work.
- Kapela–Simó provided, in 2007, computer-assisted proofs of the existence of asymmetric planar choreographies and the stability of the figure-eight orbit, and in 2017, **rigorous KAM results** around arbitrary periodic orbits (including the figure-eight solution and 2 rotating figure-eights).

> **[Caution in interpretation]** The stability ratios reported in the discovery papers (3D: 1,996/10,059 ≈ 19.8%; arbitrary-mass planar: 13,315/135,445 ≈ 9.8%) should not be read as "the fraction of stable orbits among all periodic orbits." Hristov et al. note that the 2D searches of 2013/2017 used methods that were poor at capturing unstable orbits, inflating the apparent stable fraction, and that when the half-period method is used, hundreds of thousands of unstable periodic orbits are found in the chaotic region. Similar selection biases may exist in other searches. *(estimate)*

### 31.6 Numerical Reliability: CNS and High-Precision Taylor Series Methods

- **CNS (Clean Numerical Simulation, Liao's group):** controls noise using arbitrary-order Taylor series methods plus arbitrary-precision arithmetic, converging chaotic trajectories within a "predictable critical time $T_c$." The observation that some 2013 initial conditions were insufficiently precise (Li & Liao 2014) came from this method, and it became the foundation for large-scale searches from 2017 onward.
- **Hristov's group:** Newton's method + high-precision Taylor series methods (allocating 64 bits of precision per 22nd order) + automatic differentiation. Converges the return proximity to $10^{-220}$, checks whether the logarithmic ratio between two successive iterations approaches 2 (quadratic convergence of Newton's method), and computes the monodromy matrix to 160 digits.
- **Digits of initial conditions:** Li–Liao (2025) provides, as an example, the initial conditions and period of the linearly stable orbit O3(1.0) to 70 significant digits in supplementary material, and Hristov et al. (2025) publish 971 initial conditions to 100 digits. This connects directly to the discussion of Lyapunov time in §23 — with insufficient digits, a "periodic orbit" may in fact not persist for long.
- Data availability: initial conditions and animations are published at Sofia University (db2.fmi.uni-sofia.bg) and Shanghai Jiao Tong University (numericaltank.sjtu.edu.cn/three-body, GitHub sjtu-liao/three-body).

### 31.7 Significance and Limitations

- **Significance:** periodic solutions are regarded as the "skeleton" of chaotic phase space. Around a stable periodic solution lie KAM tori (§16), forming an island of regular motion, so the collection of periodic solutions provides the material for understanding the "regular island" structure discussed in §32. Syzygy sequences and topological classification also connect to attempts at symbolic dynamics for the three-body problem (Tanikawa–Mikkola).
- **Limitation 1:** most are confirmations of *numerical* existence. Very few have variational proofs (Chenciner–Montgomery 2000) or computer-assisted proofs (Kapela–Zgliczyński 2003, Kapela–Simó 2007/2017).
- **Limitation 2:** "are there infinitely many families?" and "how far does the stable region of each family extend?" remain open questions. The second ("do stable periodic orbits exist?") and third ("are all braids realized?") of Montgomery's (2024) four open questions connect to this line of work (§37.2).
- **Limitation 3:** the 2025 3D results are preprints, so details (symmetry, residuals, stability determination) may be adjusted after peer review.

> **[Simulation]** You can directly examine the initial-condition structure (collinear configuration, middle body's velocity at $-2\times$) in Simulation 2's "figure-eight orbit" preset. Initial conditions for newly discovered orbits (e.g., Butterfly, Bumblebee) can be obtained from the databases above and entered manually, but since single-precision integrators diverge within a few periods, the precision described in §31.6 is required for long-term reproduction.

---

## 32. A New Picture of Chaos: Regular Islands and Multifractals (2019–2024)

### 32.1 Genealogy of Statistical Escape Theory

Instead of tracking chaotic orbits individually, a theory has developed that predicts the *distribution of outcomes* using the **ergodic hypothesis** (that the system uniformly fills the accessible phase space). For given energy, angular momentum, and masses, it provides, in closed form, "which body escapes" and "what is the distribution of the remaining binary's energy and eccentricity."

| Year | Study | Key point |
|---|---|---|
| 1976 | Monaghan | microcanonical ensemble, based on phase-space volume |
| 2019 | Stone & Leigh (Nature 576, 406) | derived a **closed-form distribution** of escape outcomes using the ergodic hypothesis |
| 2021 | Ginat & Perets (Phys. Rev. X 11, 031020) | a **random-walk** model between close three-body encounters, incorporating detailed-balance and dissipative effects |
| 2021 | Kol (CMDA 133, 17) | based on **phase-space flux** rather than volume; removed the artificial "strong-interaction radius" that had entered the theory |
| 2020–24 | Manwadkar et al. | compared statistical theory against large-scale TSUNAMI simulations, verifying flux theory by measuring "chaotic absorptivity" |
| 2022–25 | Dandekar, Kol et al. | regularized definitions of phase-space volume and its distribution (including follow-up preprints) |

The representative predictions of these theories are a **thermal eccentricity distribution** and a power-law distribution of the escape semi-major axis. These theories are actually used in population-synthesis calculations for black-hole binary merger (gravitational-wave) formation scenarios.

### 32.2 Trani et al. (2024): "Regular Islands in a Sea of Chaos"

**Setup:** simulated non-hierarchical three-body interactions using the precise, regularized code TSUNAMI.

- A circular binary (semi-major axis $a=5$ au) and a single body, initially at rest in the center-of-mass frame, separated by $d=100$ au
- Masses of 12.5, 15, 17.5 $M_\odot$
- Two initial degrees of freedom: the binary's **phase $\lambda$ and inclination $\iota$**
- $10^6$ realizations of the full space + **14-step zoom-in** magnifying by a factor of 5 each time, integrated for up to $10^9$ years (only 6 out of $10^6$ did not disrupt)

**Results:**

| Item | Result |

| Fraction of regular (non-chaotic) trajectories | about **37%** in this setup; **28%–84%** across 9 hyperbolic-encounter setups |

| Structure | coloring by which body escapes reveals **4 large regular islands** of uniform color and countless thin **regular streaks** |

| Lifetime of regular trajectories | very short (order of the free-fall time, about 26 years in this setup). Extremely long-lived trajectories surround the edges of the regular regions |

| Escape probability (12.5/15/17.5 $M_\odot$) | simulation 43% / 30% / 27% ↔ Stone–Leigh theory 64% / 25% / 11% |

| Excluding the regular islands | good agreement with theory (thermal eccentricity distribution, power-law semi-major axis) |

| Fractality | two-point correlation dimension $D_2<2$, with values differing at each zoom level — a **multifractal** |

| Numerical chaos | integration error artificially mixes the regular regions ("numerical chaos") |

- **Numerical chaos:** recomputing with the arbitrary-precision code BRUTUS (256-bit, tolerance $10^{-30}$) makes the regular streaks sharper. Calculations with larger error underestimate the fraction of regular region by about 25% (in the rare case where the more massive body escapes, by about 80%); nevertheless, the *statistics of the overall ensemble* remain accurate to within less than 0.5%.
- **Chaos even below the Planck length:** zooming in by a further factor of $2\times10^{41}$, so that the initial position differences fall below the Planck-length scale ($\sim10^{-46}$ au), the intermixing of regular and chaotic regions continues to appear. The authors argue that while chaos erases microscopic effects, regular regions may be a channel connecting the microscopic and macroscopic scales *(the authors' interpretation)*.
- **Implications for gravitational waves:** binaries formed via regular interactions tend to have high eccentricity, giving short gravitational-wave merger times ($t_{\rm GW}\propto(1-e^2)^{7/2}$, Peters 1964). Among binaries with merger time $t_{\rm GW}<10^7$ years, the regular side outnumbers the chaotic side by about a factor of 3. Statistical theory may therefore **underestimate the merger efficiency and eccentric-merger fraction** of binaries formed via three-body interactions.
- **Limitations:** Newtonian gravity, without collisions or post-Newtonian corrections (the authors expect post-Newtonian corrections would, if anything, increase regularity, but did not verify this). Dependence on mass ratio remains an open question, and a tendency for regular islands to break apart at larger mass differences has been reported (Manwadkar et al. 2020).



### 32.3 "Gargantuan Chaos" and Time Irreversibility (Boekholt et al. 2020, 2024)

- **Result:** free-fall three-body systems (in the Agekyan–Anosova region) were integrated with the arbitrary-precision code BRUTUS, then time-reversed as a **reversibility test**. Because the amplification factor of the initial perturbation has a power-law tail, **the fraction of irreversible solutions decreases as a power law with increasing numerical accuracy**, but the authors concluded that a **finite fraction** remains irreversible even at precision finer than the Planck length.
- **Prior results:** Dejonghe & Hut (1986) measured that initial perturbations could be amplified by up to $10^{150}$ times, and Lehto et al. (2008) reported that about half of three-body systems are irreversible in double precision.
- **Follow-up:** the 2024 paper (II) addresses the dependence on angular momentum and astrophysical scale. The authors argue this irreversibility fraction may be related to the arrow of time, which is **the authors' own hypothesis**.
- **The Pythagorean problem:** Portegies Zwart & Boekholt (2018) obtained a converged, reversible solution of the Pythagorean three-body problem of §25, recovering the initial coordinates from the final state to 10 decimal places.

### 32.4 The Relativistic Three-Body Problem

- Boekholt, Moerman & Portegies Zwart (2021, Phys. Rev. D 104, 083020): incorporated post-Newtonian pairwise terms (up to 2.5 PN order) and a first-order expansion of the Einstein–Infeld–Hoffmann equations into BRUTUS to solve the **relativistic Pythagorean problem**. They showed that a definitive solution can be obtained via a time-reversibility test in a conservative system, and confirmed, as in the Newtonian case, that the minimum required numerical accuracy correlates with the amplification factor of the initial perturbation.
- Portegies Zwart et al. (2022, A&A 659, A86): general-relativistic pericenter precession significantly reduces chaos in the strong-gravity regime $v/c\gtrsim0.005$.
- Noted at the end of Appendix C (this document focuses on classical Newtonian gravity) as a separate topic — a recent example of the relativistic three-body problem.

### 32.5 Landscape of High-Precision Tools

| Tool | Characteristics | Source |

| TSUNAMI | regularization + Richardson extrapolation, energy error $<10^{-10}$ | Trani et al. |

| BRUTUS | arbitrary precision (convergence approach: raises precision/accuracy until convergence) | Boekholt & Portegies Zwart 2015 |

| CNS / high-order Taylor | arbitrary order, arbitrary digits | Liao; Biscani & Izzo 2021 |

| IAS15 (REBOUND) | high-order adaptive integrator | Rein & Spiegel 2015 |

A principle emphasized by the BRUTUS paper is that "even if individual trajectories do not converge, the **statistics** of a sufficiently large ensemble can still be correct" (reconfirmed by Trani 2024). The symplectic integration of §26 (bounded long-term energy) is a tool for *energy conservation*, whereas the tools above are aimed at *convergence of individual trajectories* — different purposes.

### 32.6 Lyapunov Time and Lifetime

- Several studies report an approximate power-law relationship between the lifetime $t_{\rm life}$ of a three-body system and its Lyapunov time $t_{\rm Lyap}$ (Lecar et al. 1992, Orlov et al. 2010, Mikkola & Tanikawa 2007, Urminsky & Heggie 2009) (cited by Trani 2024). Long-lived systems undergo more "democratic resonances."
- Lyapunov time shortens as the number of particles increases (Portegies Zwart et al. 2022), and close encounters increase chaos.
- Physical origin of chaos: non-hierarchical three-body systems alternate between **democratic resonance**, in which all three bodies interact within a small region, and **excursion**, in which two bodies temporarily form a binary while the third departs and returns; disruption occurs only during democratic-resonance states.

> **[Simulation]** Simulation 2's "chaotic twins" ($10^{-5}$ perturbation) illustrates the exponential divergence of §23.2, but within a regular island, the perturbation does not grow. Around Simulation 1's "Pythagoras" preset, you can compare regions where small changes in initial position lead to smoothly varying final escaping bodies with regions where the outcome mixes chaotically.

---

## 33. Machine Learning and AI Approaches (2019–2026)

### 33.1 Six Lines of Attempt

| Line | Representative study | Key content | Limitations / debate |

| **① Surrogate models** | Breen et al. (MNRAS 494, 2020) | For a planar equal-mass three-body problem (zero initial velocity), trained a deep neural network (DNN) on **converged solutions** obtained from the arbitrary-precision integrator BRUTUS. Fixed computational cost over a finite time interval, up to **10⁸ times** faster than the integrator. Showed that training on solutions from a general fixed-precision integrator introduces error, so *training on converged solutions is crucial* | Li, Li & Liao (2020, preprint): using the same trained model to predict 30 equal-mass free-fall periodic orbits generated by CNS, the model diverges starting from the shortest-period orbit ($T\approx3.9039$) → current accuracy is insufficient for predicting periodic orbits. Differential Euler (arXiv:2101.08486): limited to a special 2D case, details undisclosed, and points out a lack of generalization to untrained cases, proposing a benchmark |

| **② Structure-preserving neural networks** | Hamiltonian NN (Greydanus et al. 2019), SympNets (Jin et al. 2020), Chen & Tao (2021, learning exactly symplectic maps), Cai, Portegies Zwart & Podareanu (2021, Hamiltonian inductive bias for N-body); Generalized HNN (J. Comput. Phys. 2024) | Embeds Hamiltonian structure into the neural network to suppress energy drift. GHNN reportedly outperformed SympNet, HénonNet, and MLP for the pendulum, double pendulum, and gravitational three-body problem, under matched inference speed | Training can become difficult for realistic problems (Saz Ulibarrena et al. 2024) |

| **③ PINN** | Raissi et al. (2019); Santos Pereira et al. (arXiv:2503.04585, IAC-24) | Incorporates the equations of motion (ODEs) as a regularization term in the loss. Trained on 30,000 simulations with unit masses and zero initial velocity, the authors conclude it gives better prediction quality than prior best ML methods, and is a time-efficient open-form solution compared to the cost problem of numerical integrators | A 2026 follow-up study explicitly states that PINN is *not a replacement* for existing numerical methods |

| **④ Hybrid integrators** | Saz Ulibarrena et al. (J. Comput. Phys. 496, 2024); Saz Ulibarrena & Portegies Zwart (CNSNS 145, 2025) | Replaces the expensive part of planetary-system-plus-asteroid integration with a neural network. A plain DNN fails to conserve energy and diverges quickly from the reference solution; the hybrid integrator prevents large energy errors. In this problem, it becomes faster when there are roughly 70 or more asteroids. There is also research using reinforcement learning to adaptively adjust the timestep of three-body integration | Benefit depends on problem scale |

| **⑤ Periodic-orbit/structure search** | Liao et al. (2022 roadmap); Kollias & Matzakos (arXiv:2607.23501, 2026-07); "Restricted three-body periodic-orbit generative design" (arXiv:2408.03691) | A roadmap for searching arbitrary-mass periodic orbits using CNS + neural networks. PINN recovers periodic orbits from sparse, noisy observations **without initial conditions**, and in two 100-seed ensembles, 23–25% converge to families not present in the training data. Which family emerges depends significantly on the source of the training data ($\chi^2$ test). A generative model based on a dataset of 44,112 restricted three-body orbits | many preprints |

| **⑥ Classification/diagnosis** | Celletti et al. (Sci. Rep. 12, 2022), Lalande & Trani (ApJ 938, 2022), Li et al. (MNRAS 511·524, 2022–23); NNPT (arXiv:2512.01558); binary-formation prediction (arXiv:2607.16776); Sitnikov active learning (arXiv:2311.18010) | Classification of regular/chaotic motion, hierarchical three-body stability determination (CNN), trajectory prediction for bodies in 2:3 mean-motion resonance with Neptune (predicting 18,750 years ahead using 6,250 years of integration data, with resonance-angle errors of a few degrees), large-step symplectic neural networks. NNPT proposes that learning only the *residual* after subtracting the exact solution reduces validation error by 28–54× compared to learning the whole trajectory, and that the network capacity required grows 7-fold near a critical value $\hat f_c=15.6\pm1.0$ when Jupiter's mass is varied — suggesting this could serve as a **chaos-precursor indicator** | The Sitnikov paper's title suggests caution regarding active learning on fractal decision boundaries |

| **⑦ Symbolic AI** | Alfarano, Charton & Hayat (NeurIPS 2024) | Used transformers to search for **Lyapunov functions** of dynamical systems (§33.2) | Not specifically about the three-body problem itself |

### 33.2 Distinguishing the Lyapunov "Exponent" from the Lyapunov "Function"

| | Lyapunov **exponent** $\lambda$ (§23) | Lyapunov **function** $V$ |

| Definition | exponential rate of growth of the distance between neighboring trajectories | a scalar function on state space with $V>0$ (except at equilibrium), with $\dot V\le0$ along the flow, guaranteeing stability |

| Use | diagnosing chaos, estimating predictability time | proving (global) stability of equilibria/sets, control |

| Relation to the three-body problem | direct (§23, §32.6) | indirect — Hamiltonian systems conserve phase-space volume, so no asymptotically stable equilibrium exists *(general knowledge)* |

Alfarano et al. trained a sequence-to-sequence transformer on **synthetic training data generated from random solutions**, reporting that it outperformed algorithmic methods and human experts on polynomial systems and discovered new Lyapunov functions for non-polynomial systems. This is not research on predicting the *Lyapunov exponent* of the three-body problem, nor is it research directly addressing the three-body problem.

### 33.3 Overall Assessment

- **Quality of training data:** because of chaos, double-precision integration results may not converge for individual trajectories, so training data must consist of converged solutions (BRUTUS, CNS, etc.) (§32.5).
- **Tasks demanding high accuracy:** there is criticism that periodic-orbit reproduction and long-term prediction remain unreliable (Li, Li & Liao 2020). On the other hand, where *statistical outcomes* matter, as in population synthesis, fast surrogate models are practical.
- **Structure preservation:** in the same spirit as the symplectic integration of §26, there is a strong trend toward designing neural networks that do not violate conserved quantities. However, training remains difficult for realistic problems, and verification is needed.
- **Modes of use:** (a) fast surrogate models, (b) hybrids that replace part of an integrator, (c) generating initial candidates for periodic-orbit search, (d) diagnosing chaos/stability.

 

---

## 34. Central Configurations and Relative Equilibria: Progress on Smale's Problem 6

**The finiteness conjecture (Chazy–Wintner):** for any $n$ positive masses, is the number of similarity classes of central configurations (§9.2) finite? Chazy (1918) assumed non-degeneracy, Wintner (1941) stated it in its current form, and it was included as Problem #6 in Smale's list of 21st-century problems (1998).

| $N$ | Known result | Source |

| 3 | **5** similarity classes (3 collinear + 2 equilateral) | Euler 1767, Lagrange 1772 |

| collinear $N$ | 1 per ordering of the bodies → $N!/2$ | Moulton 1910 *(general knowledge)* |

| 4 (planar) | **finite for all positive masses** | Hampton & Moeckel (Invent. Math. 163, 2006) |

| 5 (planar) | finite except when masses belong to an algebraic set of **codimension 2** → **finite for generic masses** | Albouy & Kaloshin (Ann. Math. 176, 2012) |

| 5 (spatial) | paper on finiteness of spatial 5-body central configurations | Hampton & Jensen (CMDA 109, 2011) (citation confirmed; result described at title level) |

| 5 (reconfirmation) | reconfirmed finiteness for generic masses at $n\le5$ using tropical geometry + computation | Jensen & Leykin (Exp. Math. 2025) |

| 6 (planar) | generic finiteness for specific symmetric classes (Dias & Pan 2020); symbolic-computation approaches toward finiteness: (I) diagram/order determination (J. Symb. Comput. 2024), (II) mass-relation determination (SIAM J. Appl. Dyn. Syst. 2025) | |

| $\ge6$ generic | **open** | |

- **Jensen–Leykin's method:** a new attempt to prove "the planar central configurations for generic masses at a given $n$ are finite," delegating the human-driven part to tropical geometry and the core computation to a computer. They completed the computation for $n\le5$, reproducing the Albouy–Kaloshin result. The equations use the Albouy–Chenciner form (using only mutual distances, rotation-invariant).
- **Significance:** the "open for N≥5" statements in §9.2, §20.2, and §30.2 should be updated to *"planar $N=5$ is resolved for generic masses (with an exceptional mass set remaining), and $N\ge6$ remains open"* (§38).
- Montgomery's (2024) first open question is precisely this finiteness problem, introduced as using tools from algebraic geometry.

---

## 35. Non-collision Singularities and the Completion of the Painlevé Conjecture

| Year | Study | Content |

| 1897 | Painlevé | no non-collision singularities for $N=3$ |

| 1908 | von Zeipel | if non-collision singularities exist, some body must go to infinity within finite time (§20.1) |

| 1975 | Mather & McGehee | 4 collinear bodies diverge to infinity within finite time after infinitely many binary collisions. Since collisions are involved, this is not a counterexample, but it raises the plausibility of the conjecture |

| 1988/1992 | Xia (Ann. Math. 135, 411) | non-collision singularity for spatial 5-body case |

| 1991 | Gerver | planar $3N$-body case ($N$ sufficiently large) |

| 2003 | Gerver (Exp. Math. 12) | heuristically presented a planar 4-body scenario (detailed calculation too extensive to publish) |

| 2013–14 | Xue & Dolgopyat | realized Gerver's scenario in a simplified planar *two-center-two-body* model |

| **2020** | **Xue (Acta Math. 224, 253–388)** | proved that for a Cantor set of initial conditions in the **planar 4-body problem**, the four bodies escape to infinity in finite time without collision — the author describes this as **the last remaining open case of the conjecture** |

| 2022 | Gerver, Huang & Xue (arXiv:2202.08534) | constructed planar 4-body non-collision singularities in a different model (allowing arbitrarily fast acceleration and comparable masses). The authors describe it as solving an analogue of the Anosov conjecture |

| 2023 | super-hyperbolic orbits (arXiv:2302.12410) | global solutions with infinitely growing velocity, described as a "decelerated version" of non-collision singularities |

- **Rationale for the general $N\ge4$ completion:** there is a general belief that "if a non-collision singularity is known for N bodies, adding one distant light body yields an example for $(N+1)$ bodies," so $N=4$ was the last key case (as stated in Xue's introduction).
- **Remaining question (measure):** initial conditions leading to collision have measure zero (Saari), and it is also known that initial conditions leading to non-collision singularities have measure zero for $N=4$ (Xue–Dolgopyat introduction). The measure question for $N\ge5$ could not be confirmed and remains open.
- **Relation to the main text:** §21 already states that the Painlevé conjecture is completed for all $N\ge4$ by Xue (2020), but §30.2 and the table in §29 could be read as "general $N$ remains open," requiring reconciliation (§38).

---

## 36. Practical Applications of KAM Theory: Toward Realistic Mass Ratios

### 36.1 "From $10^{-333}$ to $10^{-3}$"

The biggest weakness of the KAM theorem (§16) has been the condition that *the perturbation must be extremely small*. The progress narrowing this gap can be summarized as follows.

| Year | Study | Model | Condition/Result | Character |


| 1962–63 | Arnold | planetary system | quasi-periodic motion exists for sufficiently small mass ratio | theorem |

| 1966 | Hénon (cited via Laskar's account) | restricted three-body | checking the mass upper bound required by Arnold's theorem gives $\sim10^{-333}$. Hénon assessed that "as it stands, this cannot be applied to real problems," while also noting numerically that invariant curves persist for much larger perturbations | verification |

| 1995 | Robutel | spatial three-body planetary system | quasi-periodic motion exists for almost all semi-major-axis ratios $\alpha\in]0,0.8]$, up to mutual inclinations of about 1° (extending Arnold's result) | theorem |

| 2000 (follow-up 2007) | Locatelli & Giorgilli | **secular (averaged) model** for Sun–Jupiter–Saturn | permanent orbital stability via a semi-numerical proof using interval arithmetic, in dynamics averaged over fast angles (per the 2000 paper's abstract) | computer-assisted (averaged model) |

| 2004, 2011 | Féjoz (completing Herman's proof); Chierchia & Pinzari | spatial planetary N-body | complete proof of Arnold's theorem | theorem |

| 2017 | Castan | planar three-body | quantitative Arnold theorem + computer-assisted, up to mass ratio $\approx10^{-85}$ | computer-assisted proof |

| 2024–25 | **Figueras & Haro** | **planar Sun–Jupiter–Saturn, real data** ($\mu_0=10^{-3}$) | KAM conditions **numerically verified** (below) | numerical verification (rigorous proof in progress) |

### 36.2 Figueras–Haro's Method and Results

**Model:** the planar Newtonian Sun–Jupiter–Saturn system. Masses, semi-major axes, eccentricities, and perihelion precession are taken close to real values, with the masses of Jupiter and Saturn taken as $0.9546\times10^{-3}$ and $0.2856\times10^{-3}$ solar masses. In a 3-degree-of-freedom Hamiltonian with total angular momentum eliminated, they search for a **3-dimensional invariant torus** (frequencies: two fast ones plus one slow precession frequency).

**Difficulty:** at $\mu=0$ (two independent Kepler problems), the invariant torus is 2-dimensional and the precession frequency is zero, so the problem is **degenerate**, and standard continuation methods cannot be used.

**Method:**

1. **Translated tori**: add a term to the Hamiltonian to compensate for the degeneracy, continue from $\mu=0$ to $\mu_0=10^{-3}$, and finally adjust the total-angular-momentum parameter via Newton's method so that the compensating term vanishes
2. Refine the resulting torus using the invariant-torus algorithm of the **parameterization method** (grid $512^3$, 57 digits → $1024^3$, 76 digits; about 194 GB RAM per grid, about a week for the final Newton step)
3. Verify the conditions using the constants of an **a posteriori-form KAM theorem** and iterative lemmas

**Verification figures:**

| Item | Value required by the theorem | Value actually achieved |

| Invariance error (tangential component) | $\lesssim10^{-38}$ | $3.6\times10^{-54}$ |

| Invariance error (normal component) | $\lesssim10^{-44}$ | $1.7\times10^{-57}$ |

- They certified that a Diophantine vector ($\tau=2.4,\ \gamma=1.69\times10^{-6}$) exists within $10^{-80}$ of the frequency vector (Diophantine condition of §16.2).
- Kepler frequencies $\omega^\ell\approx(0.08395,\ 0.03382)$ (in units where Earth's frequency = 1), precession frequency $\omega^{\hat g}\approx-1.85\times10^{-5}$.

**Status:** as the title ("...may exist") suggests, this is **strong numerical evidence** for existence, not a completed mathematical proof. The authors state they are working on the last of a three-step plan (① a tailored KAM theorem, ② numerical computation, ③ a computer-assisted proof combining these two with rigorous numerics), and a May 2025 CRM introduction also describes this as "in progress" (the torus is represented by over 6 billion Fourier coefficients). Whether it has since been completed could not be confirmed in this search.

**Limitation:** it is a planar, two-planet model, and has not been applied to a spatial Solar System or multi-planet system.

### 36.3 Ancillary Results

- Kapela & Simó (2017) present a rigorous KAM method around arbitrary periodic orbits, applying it to the figure-eight solution and 2 rotating figure-eights of the three-body problem, and also verify the existence of *very small elliptic islands* within a large chaotic region for a quartic-potential system (§31.5).
- The KAM theorem via the parameterization method is also being extended to time-dependent (quasi-periodically forced) systems (Caracciolo–Figueras–Haro 2025).


---

## 37. Other Recent Trends

### 37.1 Lagrange Points and Trojan Asteroids: The Lucy Mission

The stability of $L_4,L_5$ ($\mu<\mu_{crit}\approx0.0385$) discussed in §13.3–§13.4, which gives rise to the Jupiter Trojan population, is being directly explored for the first time by NASA's Lucy spacecraft.

| Timing | Event |

| 2021-10 | Launch |

| 2025-04-20 | Flyby of main-belt asteroid (52246) Donaldjohanson (completed) |

| Spring 2026 | Rehearsal observation of 4 targets using the high-resolution camera (announced by NASA, 2026-08) |

| 2027-08-12 | $L_4$: (3548) Eurybates and its moon Queta |

| 2027-09-15 | $L_4$: (15094) Polymele |

| 2028-04-18 | $L_4$: (11351) Leucus |

| 2028-11-11 | $L_4$: (21900) Orus |

| 2033-03 | $L_5$: the (617) Patroclus–Menoetius pair |

One goal is to test the scenario in which the Trojans originally formed farther out and were captured during an early planetary rearrangement. (The *orbital stability* of the Trojans connects directly to the KAM and resonance theory of the three-body problem.)

### 37.2 Montgomery (2024): Four Open Questions

Richard Montgomery's book *Four Open Questions for the N-Body Problem* (Cambridge University Press, December 2024) summarizes progress over the past 20 years around the following four questions.

1. **Are central configurations finite?** — algebraic-geometry tools (§34)
2. **Do stable periodic orbits exist?** — dynamics, KAM (§31.5, §36)
3. **Are all braids realized?** — topology, variational methods
4. **Is the image of a scattering beam dense?** — a relatively new question requiring considerable effort to formalize

### 37.3 Reviews and Resources

- Li & Liao, "A review on periodic orbits of the general planar three-body problem" (Sci. China 68, 289501, 2025) — history, classification methods, CNS, and equal-/unequal-mass results in periodic-orbit research.
- Kol, "The simplest complexity: the story of the three-body problem" (arXiv:2510.18848, 2025) — introduced as a review from the perspective of flux-based statistical theory.
- Initial-condition databases: Sofia University (db2.fmi.uni-sofia.bg), Shanghai Jiao Tong University (numericaltank.sjtu.edu.cn/three-body).

### 37.4 Revised Table of Open Problems (replacing §30.2)

| # | Problem | Status as of 2026 |

| 1 | Finiteness of central configurations (Smale #6) | Resolved for all masses at $N=4$; planar $N=5$ resolved for generic masses (an exceptional mass set remains); $N\ge6$ open |

| 2 | Rigorous understanding of stable periodic orbits | Rigorous proof of KAM stability exists for only the figure-eight solution and 2 rotating figure-eights. Thousands of linearly stable and KAM candidates (twist condition unverified) |

| 3 | Realization of all braids / density of the scattering beam | open (Montgomery Q3, Q4) |

| 4 | Statistical theory incorporating regular islands | discrepancy between statistical escape theory and regular islands (28–84%) confirmed. A unified theory remains incomplete |

| 5 | KAM applied to real mass ratios | numerically verified for planar Sun–Jupiter–Saturn, rigorous proof in progress. Spatial/multi-planet cases remain open |

| 6 | The Painlevé conjecture | the existence question is completed for $N\ge4$. The measure question for $N\ge5$ is unconfirmed |

| 7 | Gargantuan chaos and irreversibility | a finite irreversible fraction has been reported even below the Planck length. Physical meaning remains debated |

| 8 | Long-term reliability of machine learning | periodic-orbit reproduction and long-term prediction remain inadequate; statistical uses are practical |

| 9 | General existence of $N$-body choreographic solutions | open (as in §22) |

---


---

# Appendices

## Appendix A. Simulation Guide

### A.1 Simulation 1: N-Body 3D v2.1

- **File**: three-body-3d.html
- **Technology**: Three.js, WebGL, Barnes–Hut octree
- **Dimension**: 3D
- **Scale**: up to 500 bodies
- **Purpose**: large-scale N-body simulation, experimental intuition

**Key features:**
- Presets: Random 8/16/100, Pythagoras, Figure-8, Solar System, Sun+Planets, Cluster 50, Galaxy 200
- Barnes–Hut ($\theta$ slider)
- Verlet integration
- Collision modes: Elastic / Inelastic (merge)
- Particle effects
- COM-tracking camera (FREE / COM / BODY)
- Real-time calculation panel (Verlet formulas, acceleration computation process)
- Energy graph (T, V, E)

### A.2 Simulation 2: N-Body Orbit Simulator

- **File**: nbody.html
- **Technology**: vanilla Canvas 2D, Velocity Verlet
- **Dimension**: 2D
- **Scale**: up to 20 bodies
- **Purpose**: contrasting exact solutions with chaos, for educational use

**Key features:**
- Presets: figure-eight orbit, Lagrange equilateral-triangle solution, Euler collinear solution, random N-body — chaos
- Velocity Verlet integration
- Chaotic twins (initial-position perturbation of $10^{-5}$)
- Conserved-quantity drift (E, L drift %)
- Lyapunov sensitivity chart ($\log_{10}\|\delta\mathbf{Z}(t)\|$)
- Trajectory display toggle
- N slider (3–20, chaos preset)

### A.3 Cross-Reference Between Simulations and Theory

| Sim 1 feature | Theory part |
 
| Pythagoras | §25 the Pythagorean three-body problem |

| Figure-8 | §10 the figure-eight orbit |

| Solar System | §13 Lagrange points |

| Verlet integration | §26 symplectic integration |

| Barnes–Hut | §27 the Barnes–Hut algorithm |

| COM tracking | §5 conserved quantities |

| real-time calculation panel | §26 symplectic integration |

| Sim 2 feature | Theory part |

| figure-eight orbit | §10 the figure-eight orbit |

| Lagrange equilateral-triangle solution | §8.2 Lagrange's equilateral triangle solution |

| Euler collinear solution | §8.1 Euler's collinear solution |

| random N-body chaos | §23 the nature of chaos |

| chaotic twins | §23.2 the Lyapunov exponent |

| conserved-quantity drift | §5 conserved quantities |

| Lyapunov sensitivity | §23.2 the Lyapunov exponent |

| Velocity Verlet | §26 symplectic integration |

---

## Appendix B. Summary of Key Notation

| Symbol | LaTeX | Unicode | Meaning |


| $m_i$ | `m_i` | mᵢ | mass of the $i$-th body |

| $\mathbf{r}_i$ | `\mathbf{r}_i` | rᵢ | position of the $i$-th body |

| $r_{ij}$ | `r_{ij}` | rᵢⱼ | distance between bodies $i,j$ |

| $\mathbf{p}_i$ | `\mathbf{p}_i` | pᵢ | momentum of the $i$-th body |

| $\mathbf{v}_i$ | `\mathbf{v}_i` | vᵢ | velocity of the $i$-th body |

| $\mathbf{a}_i$ | `\mathbf{a}_i` | aᵢ | acceleration of the $i$-th body |

| $G$ | `G` | G | gravitational constant |

| $\mathcal{H}$ | `\mathcal{H}` | ℋ | Hamiltonian |

| $T$ | `T` | T | kinetic energy |

| $U$ (main text), $V$ (some sources) | `U`, `V` | U, V | potential energy (sign convention varies by source — this text uses the negative-sign convention $U$ uniformly) |

| $E, H$ | `E`, `H` | E, H | total energy (Hamiltonian) |

| $\mathbf{P}$ | `\mathbf{P}` | P | total momentum |

| $\mathbf{L}$ | `\mathbf{L}` | L | total angular momentum |

| $\mathbf{R}_{cm}$ | `\mathbf{R}_{\text{cm}}` | R_cm | center-of-mass position |

| $I$ | `I` | I | moment of inertia |

| $\mu$ | `\mu` | μ | RTBP mass ratio |

| $\Omega$ | `\Omega` | Ω | RTBP effective potential |

| $C_J$ | `C_J` | C_J | Jacobi integral |

| $\lambda_{\text{Lyap}}$ | `\lambda_{\text{Lyap}}` | λ_Lyap | Lyapunov exponent |

| $\Delta t$ | `\Delta t` | Δt | time step |

| $N$ | `N` | N | number of bodies |

| $\boldsymbol{\rho}_i$ | `\boldsymbol{\rho}_i` | ρᵢ | Jacobi coordinate |

---

## Appendix C. References

### C.1 Primary Sources

- Bruns, H. (1887). *Über die Integrale des Vielkörper-Problems*
- Poincaré, H. (1889, 1892). *Les méthodes nouvelles de la mécanique céleste*
- Sundman, K. (1907, 1909, 1912). Papers on regularization and the general solution of the three-body problem
- Belorizky, D. (1930). Estimate of the convergence rate of Sundman's series
- Chenciner, A., Montgomery, R. (2000). *A remarkable periodic solution of the three-body problem in the case of equal masses*, Annals of Mathematics, 152, 881–901
- Simó, C. (2000). *Dynamical properties of the figure eight solution of the three-body problem*
- Kapela, T., Simó, C. (2017). *Computer assisted proofs for nonsymmetric planar choreographies and for stability of the Eight*
- Castan, T. (2017). *Stability in the plane, planetary three-body problem*. PhD Thesis, Université Paris VI (Sorbonne Université)
- Vasiliev, N., Pavlov, D. (2017). *The Computational Complexity of the Initial Value Problem for the Three Body Problem*, Journal of Mathematical Sciences
- Xue, J. (2014/2020). *Noncollision singularities in the planar four-body problem*

### C.2 Reviews and Reference Works

- Barrow-Green, J. (1997). *Poincaré and the Three Body Problem*
- Moeckel, R. et al. — reviews related to central configurations and non-integrability
- Scholarpedia: "Three body problem"
- Encyclopedia of Mathematics: "Three-body problem"

> *Note: this document focuses on the classical (non-relativistic) three-body problem under Newtonian gravity. The general-relativistic three-body problem (post-Newtonian approximations, relativistic extensions of choreographies, etc.) can be treated as a separate topic.  

### C.3 Recent Literature (2006–2026) — Basis for Part 12


**(1) Periodic-orbit search (§31)**

- Šuvakov, M., Dmitrašinović, V. (2013). *Three classes of Newtonian three-body planar periodic orbits*. Phys. Rev. Lett. 110, 114301 (arXiv:1303.0181)
- Šuvakov, M., Dmitrašinović, V. (2014). *A guide to hunting periodic three-body orbits*. Am. J. Phys. 82, 609–619
- Šuvakov, M. (2014). *Numerical search for periodic solutions in the vicinity of the figure-eight orbit: slaloming around singularities on the shape sphere*. Celest. Mech. Dyn. Astron. 119, 369–377
- Li, X., Liao, S. (2014). *On the stability of the three classes of Newtonian three-body planar periodic orbits*. Sci. China Phys. Mech. Astron. 57, 2121–2126
- Li, X., Liao, S. (2017). *More than six hundred new families of Newtonian periodic planar collisionless three-body orbits*. Sci. China Phys. Mech. Astron. 60 (arXiv:1705.00527)
- Dmitrašinović, V., Hudomal, A., Shibayama, M., Sugita, A. (2018). *Linear stability of periodic three-body orbits with zero angular momentum and topological dependence of Kepler's third law: a numerical test*. J. Phys. A 51, 315101
- Li, X., Jing, Y., Liao, S. (2018). *Over a thousand new periodic orbits of a planar three-body system with unequal masses*. Publ. Astron. Soc. Jpn. 70, 64 (arXiv:1709.04775)
- Li, X., Liao, S. (2019). *Collisionless periodic orbits in the free-fall three-body problem*. New Astron. 70, 22–26 (arXiv:1805.07980)
- Janković, M. R., Dmitrašinović, V., Šuvakov, M. (2020). *A guide to hunting periodic three-body orbits with non-vanishing angular momentum*. Comput. Phys. Commun. 250, 107052
- Li, X., Li, X., Liao, S. (2021). *One family of 13315 stable periodic orbits of non-hierarchical unequal-mass triple systems*. Sci. China Phys. Mech. Astron. 64, 219511 (arXiv:2007.10184)
- Liao, S. et al. (2022). *A roadmap to find periodic orbits of three-body systems with arbitrary masses* (bibliographic details: see the Shanghai Jiao Tong University project page)
- Hristov, I. et al. (2022). *New families of periodic orbits for the planar three-body problem computed with high precision*. arXiv:2205.14709
- Vasiljević, V., Raonić, B., Dmitrašinović, V. (2023). *An island of linearly stable non-hierarchical unequal mass periodic three-body orbits: a harbinger of circumbinary exoplanets?* New Astron. 100, 101969
- Hristov, I., Hristova, R., Dmitrašinović, V., Tanikawa, K. (2024). *Three-body periodic collisionless equal-mass free-fall orbits revisited*. Celest. Mech. Dyn. Astron. 136, 7 (arXiv:2308.16159)
- Hristov, I., Hristova, R., Dmitrašinović, V., Tanikawa, K. (2024). *Instability of three-body periodic collisionless equal-mass free-fall orbits*. J. Phys.: Conf. Ser. 2910, 012030
- Hristov, I., Hristova, R. (2024). *An efficient approach for searching three-body periodic orbits passing through Eulerian configuration*. Astron. Comput. 49, 100880 (arXiv:2404.16526)
- Hristov, I. et al. (2025). *Numerical search for three-body periodic free-fall orbits with central symmetry*. Commun. Nonlinear Sci. Numer. Simul., 109066 (arXiv:2503.00432)
- Li, X., Liao, S. (2025). *A review on periodic orbits of the general planar three-body problem*. Sci. China Phys. Mech. Astron. 68, 289501
- Li, X., Liao, S. (2025). *Discovery of 10,059 new three-dimensional periodic orbits of general three-body problem*. arXiv:2508.08568
- Hristov, I., Hristova, R., Tanikawa, K. (2025). *An extensive search for stable periodic orbits of the equal-mass zero angular momentum three-body problem*. arXiv:2510.22802
- Roberts, G. (2007). *Linear stability analysis of the figure-eight orbit in the three-body problem*. Ergodic Theory Dyn. Syst. 27, 1947–1963
- Kapela, T., Zgliczyński, P. (2003). *The existence of simple choreographies for the N-body problem — a computer-assisted proof*. Nonlinearity 16, 1899–1918
- Kapela, T., Simó, C. (2007). *Computer assisted proofs for nonsymmetric planar choreographies and for stability of the Eight*. Nonlinearity 20, 1241–1255
- Kapela, T., Simó, C. (2017). *Rigorous KAM results around arbitrary periodic orbits for Hamiltonian systems*. Nonlinearity 30, 965–986 (arXiv:1105.3235)

**(2) Chaos, statistical theory, numerical reliability (§32)**

- Stone, N. C., Leigh, N. W. C. (2019). *A statistical solution to the chaotic, non-hierarchical three-body problem*. Nature 576, 406–410
- Ginat, Y. B., Perets, H. B. (2021). *Analytical, statistical approximate solution of dissipative and nondissipative binary-single stellar encounters*. Phys. Rev. X 11, 031020
- Kol, B. (2021). *Flux-based statistical prediction of three-body outcomes*. Celest. Mech. Dyn. Astron. 133, 17 (arXiv:2002.11496)
- Dandekar, Y., Kol, B., Lederer, L., Mazumdar, S. (2022). *Regularized phase-space volume for the three-body problem*. Celest. Mech. Dyn. Astron. 134, 55
- Kol, B. et al. (2025). *Distribution of regularized three-body phase-volume*. arXiv:2501.02013; Kol, B. (2025). *The simplest complexity: the story of the three-body problem*. arXiv:2510.18848
- Manwadkar, V., Trani, A. A., Leigh, N. W. C. (2020). MNRAS 497, 3694; Manwadkar, V., Kol, B., Trani, A. A., Leigh, N. W. C. (2021). MNRAS 506, 692; Manwadkar, V., Trani, A. A., Kol, B. (2024). *Measurement of three-body chaotic absorptivity predicts chaotic outcome distribution*. Celest. Mech. Dyn. Astron. 136, 4
- Trani, A. A., Leigh, N. W. C., Boekholt, T. C. N., Portegies Zwart, S. (2024). *Isles of regularity in a sea of chaos amid the gravitational three-body problem*. Astron. Astrophys. 689, A24 (arXiv:2403.03247)
- Boekholt, T., Portegies Zwart, S. (2015). *On the reliability of N-body simulations*. Comput. Astrophys. Cosmol. 2, 2
- Portegies Zwart, S., Boekholt, T. (2018). *Numerical verification of the microscopic time reversibility of Newton's equations of motion: fighting exponential divergence*. Commun. Nonlinear Sci. Numer. Simul. 61, 160–166
- Boekholt, T. C. N., Portegies Zwart, S. F., Valtonen, M. (2020). *Gargantuan chaotic gravitational three-body systems and their irreversibility to the Planck length*. MNRAS 493, 3932–3937
- Boekholt, T. C. N., Portegies Zwart, S. F. (2024). *Gargantuan chaotic gravitational three-body systems II. Dependence on angular momentum and astrophysical scale*. MNRAS 536, 2993
- Boekholt, T. C. N., Moerman, A., Portegies Zwart, S. F. (2021). *Relativistic Pythagorean three-body problem*. Phys. Rev. D 104, 083020
- Portegies Zwart, S. F., Boekholt, T. C. N., Por, E. H., Hamers, A. S., McMillan, S. L. W. (2022). *Chaos in self-gravitating many-body systems: Lyapunov time dependence of N and the influence of general relativity*. Astron. Astrophys. 659, A86
- Rein, H., Spiegel, D. S. (2015). *IAS15: a fast, adaptive, high-order integrator for gravitational dynamics, accurate to machine precision over a billion orbits*. MNRAS 446, 1424–1437
- Biscani, F., Izzo, D. (2021). *Revisiting high-order Taylor methods for astrodynamics and celestial mechanics*. MNRAS 504, 2614–2628

**(3) Machine learning (§33)**

- Breen, P. G., Foley, C. N., Boekholt, T., Portegies Zwart, S. (2020). *Newton versus the machine: solving the chaotic three-body problem using deep neural networks*. MNRAS 494, 2465–2470
- Li, J., Li, X., Liao, S. (2020). *Can machine learning really solve the three-body problem?* (Research Square preprint)
- Greydanus, S., Dzamba, M., Yosinski, J. (2019). *Hamiltonian neural networks*. arXiv:1906.01563; Jin, P. et al. (2020). *SympNets*. Neural Netw. 132, 166–179; Chen, R., Tao, M. (2021). *Data-driven prediction of general Hamiltonian dynamics via learning exactly-symplectic maps*. arXiv:2103.05632; Cai, M. X., Portegies Zwart, S., Podareanu, D. (2021). *Neural symplectic integrator with Hamiltonian inductive bias for the gravitational N-body problem*. arXiv:2111.15631
- Raissi, M., Perdikaris, P., Karniadakis, G. E. (2019). *Physics-informed neural networks…*. J. Comput. Phys. 378, 686–707
- Santos Pereira, M. et al. (2025). *Advancing solutions for the three-body problem through physics-informed neural networks*. arXiv:2503.04585 (IAC-24)
- Saz Ulibarrena, V. et al. (2024). *A hybrid approach for solving the gravitational N-body problem with artificial neural networks*. J. Comput. Phys. 496, 112596; Saz Ulibarrena, V., Portegies Zwart, S. (2025). *Reinforcement learning for adaptive time-stepping in the chaotic gravitational three-body problem*. Commun. Nonlinear Sci. Numer. Simul. 145
- Kollias, N., Matzakos, N. (2026). *Physics-informed neural networks for discovering periodic orbits in the gravitational three-body problem*. arXiv:2607.23501
- Alfarano, A., Charton, F., Hayat, A. (2024). *Global Lyapunov functions: a long-standing open problem in mathematics, with symbolic transformers*. NeurIPS 37; arXiv:2410.08304
- Celletti, A. et al. (2022). Sci. Rep. 12, 1890; Lalande, F., Trani, A. A. (2022). ApJ 938, 18; Li, X. et al. (2022). MNRAS 511, 2218; Li, X. et al. (2023). MNRAS 524, 1374
- Other preprints: "Differential Euler" arXiv:2101.08486; "Restricted three-body periodic-orbit generative design" arXiv:2408.03691; NNPT arXiv:2512.01558; binary-formation prediction arXiv:2607.16776; Sitnikov active learning arXiv:2311.18010

**(4) Central configurations, singularities, KAM (§34–§36)**

- Hampton, M., Moeckel, R. (2006). *Finiteness of relative equilibria of the four-body problem*. Invent. Math. 163, 289–312
- Albouy, A., Kaloshin, V. (2012). *Finiteness of central configurations of five bodies in the plane*. Ann. Math. 176, 535–588
- Hampton, M., Jensen, A. N. (2011). *Finiteness of spatial central configurations in the five-body problem*. Celest. Mech. Dyn. Astron. 109, 321–332
- Dias, T., Pan, B.-Y. (2020). J. Dyn. Diff. Equ. 32, 1579–1602; Chang, K.-M., Chen, K.-C. (2024). J. Symb. Comput. 123, 102277; (2025). SIAM J. Appl. Dyn. Syst. 24(3), 2369–2404
- Jensen, A. N., Leykin, A. (2025). *Smale's 6th problem for generic masses*. Exp. Math.; arXiv:2301.02305
- Montgomery, R. (2024). *Four Open Questions for the N-Body Problem*. Cambridge University Press
- Xue, J. (2020). *Non-collision singularities in a planar 4-body problem*. Acta Math. 224, 253–388; Xue, J., Dolgopyat, D. arXiv:1307.2645; Gerver, J. L. (2003). Exp. Math. 12, 187–198; Gerver, J., Huang, G., Xue, J. arXiv:2202.08534; Xia, Z. (1992). Ann. Math. 135, 411–468
- Hénon, M. (1966). Bull. Astron. 3, 49–66 (cited secondhand); Robutel, P. (1995). Celest. Mech. Dyn. Astron. 62, 219–261; Féjoz, J. (2004). Ergodic Theory Dyn. Syst. 24, 1521–1582; Chierchia, L., Pinzari, G. (2011). Invent. Math. 186, 1–77; Locatelli, U., Giorgilli, A. (2000). Celest. Mech. Dyn. Astron. 78, 47–74
- Castan, T. (2017). *Stability in the plane, planetary three-body problem*. PhD thesis (numbers via secondary sources)
- Figueras, J.-Ll., Haro, À. (2024). *A modified parameterization method for invariant Lagrangian tori for partially integrable Hamiltonian systems*. Physica D 462, 134127; Figueras, J.-Ll., Haro, À. (2025). *Sun–Jupiter–Saturn system may exist: a verified computation of quasiperiodic solutions for the planar three-body problem*. J. Nonlinear Sci. 35(1), 1–20 (arXiv:2403.10152)

**(5) Exploration and other**

- NASA/SwRI, Lucy mission page and NASA Science blog (2026-08-06)

- 
--

Further reading

[§8.1 Euler's collinear solution]

  There are three configurations of Euler's collinear solution in total,
  determined by which body sits in the middle. This shares a common root
  with the collinear Lagrange points L₁, L₂, L₃ of the restricted
  three-body problem. Indeed, the fact that L₁, L₂, L₃ lie on the line
  joining the two primaries in the RTBP can be viewed as a special case
  of Euler's collinear solution.


[§10.2 Initial values of the figure-eight solution]

  However, Fujiwara et al. (2003) proved that under a Newtonian potential,
  no figure-eight choreography exists whose moment of inertia remains
  constant along the trajectory. That is, the moment of inertia of the
  figure-eight solution varies within the period, and the initial
  condition above corresponds to choosing a stationary point of that
  variation.


[§14 Hill's approximate problem]

  This C_H is the only known constant of motion of Hill's equations, and
  shows how the Jacobi integral of the RTBP transforms in the local limit.
  Historically, Hill's approximation originated from Hill's 1877–1878
  study of lunar motion theory, in which he neglected the Sun's parallax
  and set the eccentricity of the Sun's orbit to zero, describing the
  Earth–Moon system's lunar motion in a simplified form.


[§15.2 Lagrange's planetary equations]

  The equation for the semi-major axis is only an example; in fact, for
  each of the six orbital elements there exists a first-order equation of
  the following kind:

      da/dt, de/dt, di/dt, dΩ/dt, dω/dt, dM/dt

  Collectively these are called Lagrange's planetary equations, and each
  right-hand side is expressed as a partial derivative of the disturbing
  function R. These six equations, first derived by Lagrange, later
  became the standard starting point for planetary perturbation theory.


[§17.1 Sundman regularization]

  To remove the two-body collision singularity, Sundman also introduced
  the reparametrization

      s = |t₁ − t|^(1/3)

  where t₁ is the time at which the two-body collision occurs. This
  reparametrization removes the singularity, and the coordinates become
  analytic functions expandable in powers of s.


[§17.2 The Sundman series solution]

  This series solution converges for all real time, for initial
  conditions (angular momentum C ≠ 0) in which no triple collision
  occurs. This was the realization of the convergent series that
  Weierstrass had foreseen in connection with the King's Prize problem.
  However, the fact that its convergence rate is extremely slow, making
  it of little practical computational use, is addressed again in §17.4.


[§19.1 General N-body equations of motion]

  Depending on the source, if the potential is defined with the positive
  convention

      U = G Σ_{i<j} mᵢmⱼ/rᵢⱼ

  then the N-body equations of motion can be written simply as

      mᵢ r̈ᵢ = ∂U/∂rᵢ

  This document uses the negative convention U = −G Σ mᵢmⱼ/rᵢⱼ, so under
  the main text's convention this becomes mᵢ r̈ᵢ = −∂U/∂rᵢ. The two
  notations differ only in sign and describe the same physics.