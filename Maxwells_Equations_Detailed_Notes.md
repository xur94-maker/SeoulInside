# Maxwell's Equations: From Differential/Integral Forms to Relativistic Covariant Formalism and Gauge Theory

---

## Table of Contents

1. Proof of Equivalence Between Differential and Integral Forms
2. The Necessity of Introducing Displacement Current
3. Derivation of the Electromagnetic Wave Equation + Agreement with the Speed of Light
4. The Mathematical Statement of the Absence of Magnetic Monopoles
5. Deriving from First Principles: Coulomb's Law and the Biot–Savart Law
6. Relativistic Covariant Formalism and Four-Vector Notation
7. Detailed Proof of Gauge Transformations and Modern Extensions

---

# 1. Proof of Equivalence Between Differential and Integral Forms

Showing that the differential and integral forms of Maxwell's equations are equivalent ultimately rests on two purely mathematical tools: the **Divergence Theorem** and **Stokes' Theorem**. These theorems themselves are identities of vector calculus with nothing to do with physics; the "physics" of Maxwell's equations is contained entirely in either the integral form or the differential form.

## 1.0 Preliminary Tools: Two Integral Theorems

### (A) Divergence Theorem (Gauss–Ostrogradsky Theorem)

For any smooth closed surface $S$ enclosing a volume $V$, and any differentiable vector field $\mathbf{F}$ defined on it:

$$\oint_S \mathbf{F}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{F})\, dV$$

**Meaning**: The total flux of a vector field leaving through a closed surface equals the sum of everything "generated" (the divergence) inside that surface.

### (B) Stokes' Theorem

For any smooth open surface $S$ with boundary closed curve $\partial S = C$, and any differentiable vector field $\mathbf{F}$ defined on it:

$$\oint_C \mathbf{F}\cdot d\boldsymbol{\ell} = \int_S (\nabla\times\mathbf{F})\cdot d\mathbf{A}$$

**Meaning**: The total circulation of a vector field around a closed loop equals the sum of the "rotation" (the curl) of the field over any surface bounded by that loop.

The key point is that both theorems hold for **any** $V$ or $S$. This "arbitrariness" plays the decisive role later when deriving the differential form from the integral form.

## 1.1 Gauss's Law (Electric Field) — Applying the Divergence Theorem

**Integral form**:
$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{enc}}{\varepsilon_0} = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

**Differential form**:
$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

### Proof (Integral → Differential)

**Step 1.** Apply the Divergence Theorem to the left side of the integral form:
$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{E})\, dV$$

**Step 2.** The integral form can therefore be rewritten as:
$$\int_V (\nabla\cdot\mathbf{E})\, dV = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

$$\int_V \left(\nabla\cdot\mathbf{E} - \frac{\rho}{\varepsilon_0}\right) dV = 0$$

**Step 3 (Key — the "arbitrary volume" argument).** This equation must hold not just for one particular $V$, but for **any closed surface** we choose in space (since Gauss's law itself is a physical law that holds for any surface). Suppose the integrand $f \equiv \nabla\cdot\mathbf{E} - \rho/\varepsilon_0$ were nonzero at some point $P$. By continuity, $f$ keeps (roughly) the same sign in a small neighborhood of $P$. If we take a tiny volume $V_\epsilon$ enclosing that neighborhood, then

$$\int_{V_\epsilon} f\, dV \neq 0$$

which is a contradiction. Therefore, at **every point**:

$$\nabla\cdot\mathbf{E} - \frac{\rho}{\varepsilon_0} = 0 \quad\Longrightarrow\quad \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

(This argument — "if an integral vanishes over an arbitrary region, the integrand itself must vanish" — recurs identically in the proofs that follow, and is known as the **fundamental lemma of the calculus of variations**.)

### Reverse Direction (Differential → Integral)

Assuming the differential form $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ holds at every point, integrate both sides over an arbitrary volume $V$:

$$\int_V \nabla\cdot\mathbf{E}\, dV = \frac{1}{\varepsilon_0}\int_V \rho\, dV$$

Applying the Divergence Theorem to the left side immediately gives back the integral form. $\blacksquare$

## 1.2 Gauss's Law (Magnetic Field) — Applying the Divergence Theorem

**Integral form**:
$$\oint_S \mathbf{B}\cdot d\mathbf{A} = 0$$

**Differential form**:
$$\nabla\cdot\mathbf{B} = 0$$

### Proof

By the Divergence Theorem:
$$\oint_S \mathbf{B}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{B})\, dV = 0$$

Since this must hold for **any** $V$, the same fundamental lemma as in 1.1 gives, at every point,

$$\nabla\cdot\mathbf{B} = 0$$

This equation carries special physical meaning precisely because the right-hand side is always zero — the statement that "no magnetic monopoles exist" is itself the physical content of this equation. $\blacksquare$

## 1.3 Faraday's Law — Applying Stokes' Theorem

**Integral form**:
$$\oint_C \mathbf{E}\cdot d\boldsymbol{\ell} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A}$$

**Differential form**:
$$\nabla\times\mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

### Proof (Integral → Differential)

**Step 1.** Apply Stokes' Theorem to the left side:
$$\oint_C \mathbf{E}\cdot d\boldsymbol{\ell} = \int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A}$$

**Step 2.** Assuming the surface $S$ is fixed in time (a stationary path), the time derivative can be moved inside the integral:
$$-\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{A} = -\int_S \frac{\partial \mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

**Step 3.** Combining both:
$$\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

$$\int_S \left(\nabla\times\mathbf{E} + \frac{\partial\mathbf{B}}{\partial t}\right)\cdot d\mathbf{A} = 0$$

**Step 4 (Arbitrary surface argument).** This identity must hold for **any** surface $S$ sharing the boundary $C$. By the same logic as before, if the integrand vector $\nabla\times\mathbf{E} + \partial\mathbf{B}/\partial t$ were nonzero at some point, we could choose a tiny surface around that point making the integral nonzero — a contradiction. Therefore, at every point:

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}$$

### Reverse Direction (Differential → Integral)

Assuming the differential form holds everywhere, integrate both sides over any surface $S$ with a fixed boundary $C$:

$$\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{A} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A}$$

Applying Stokes' Theorem on the left and exchanging the time derivative with the integral on the right immediately restores the integral form. $\blacksquare$

## 1.4 The Ampère–Maxwell Law — Applying Stokes' Theorem (Including Displacement Current)

**Integral form**:
$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc} + \mu_0\varepsilon_0\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{A}$$

where $I_{enc} = \int_S \mathbf{J}\cdot d\mathbf{A}$ (the surface integral of the current density).

**Differential form**:
$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

### Proof

**Step 1.** Apply Stokes' Theorem to the left side:
$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \int_S(\nabla\times\mathbf{B})\cdot d\mathbf{A}$$

**Step 2.** Unify the right side as a surface integral:
$$\mu_0 I_{enc} + \mu_0\varepsilon_0\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{A} = \int_S \mu_0\mathbf{J}\cdot d\mathbf{A} + \int_S \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\cdot d\mathbf{A}$$

**Step 3.** Setting left = right and rearranging:
$$\int_S \left[\nabla\times\mathbf{B} - \mu_0\mathbf{J} - \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right]\cdot d\mathbf{A} = 0$$

**Step 4.** Since this must hold for any surface $S$ sharing the boundary $C$, the fundamental lemma gives, at every point:

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

### Note: Why the Displacement Current Term Was "Necessary" (Consistency Check)

Taking the divergence of both sides of the differential form and using the identity $\nabla\cdot(\nabla\times\mathbf{B}) \equiv 0$:
$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

Substituting Gauss's law $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$:
$$0 = \mu_0\left(\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}\right)$$

In other words, the **continuity equation (charge conservation)** $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$ falls out automatically. Had Maxwell not added the displacement current term $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$, this consistency would have been broken — this is precisely the historical reason the displacement current was introduced. $\blacksquare$

## 1.5 The Common Structure of the Four Proofs

| Equation | Theorem Applied | Key Argument |
|---|---|---|
| Gauss (E) | Divergence Theorem | Arbitrary volume → integrand = 0 |
| Gauss (B) | Divergence Theorem | Arbitrary volume → integrand = 0 |
| Faraday | Stokes' Theorem | Arbitrary surface → integrand vector = 0 |
| Ampère–Maxwell | Stokes' Theorem | Arbitrary surface → integrand vector = 0 |

All four proofs follow the same three-step pattern:

1. Use an integral theorem to convert the left side (or both sides) of the integral form into the same kind of integral (a volume integral or a surface integral).
2. Combine the two integrals into a single expression of the form "(integrand) integral = 0".
3. Use the physical requirement that this integral must hold over an **arbitrary** region to conclude that the integrand itself vanishes identically at every point (the fundamental lemma).

This structure makes clear the answer to "why do two forms exist": the **integral form is a global statement over a finite region** (a surface or a curve), while the **differential form is a local statement at each point in space**, and the two theorems (Divergence and Stokes), together with the "arbitrary region" argument, connect the two precisely.

---

# 2. The Necessity of Introducing Displacement Current

We show why the displacement current is not "optional" but a **logical necessity**. The key is to make mathematically explicit the contradiction between **charge conservation** and the **original Ampère's law** in non-static situations.

## 2.0 Starting Point: Two Independent Physical Laws

**Law A — Charge Conservation (Continuity Equation)**:
$$\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t} = 0 \quad \cdots (1)$$

This is not a law of electromagnetism but a more fundamental **experimental fact** — charge does not suddenly appear or disappear anywhere; the local charge density $\rho$ decreases exactly as much as the divergence (net outflow) of the current density $\mathbf{J}$. This law must hold **always, without exception**, whether static or dynamic.

**Law B — The Original (Magnetostatic) Ampère's Law**:
$$\nabla\times\mathbf{B} = \mu_0 \mathbf{J} \quad \cdots (2)$$

This was experimentally verified only for steady currents (i.e., $\partial\rho/\partial t = 0$).

## 2.1 Discovering the Contradiction: A Diagnosis via Identity

For any vector field $\mathbf{B}$, the following is a purely mathematical identity (the divergence of a curl is always zero):

$$\nabla\cdot(\nabla\times\mathbf{B}) \equiv 0 \quad \cdots (3)$$

This holds for any smooth vector field regardless of physics (intuitively: curl represents "rotation," and a rotating field has no net outflow anywhere).

Now suppose Law B, $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$, holds **generally** — even in time-varying situations — and take the divergence of both sides:

$$\nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\,\nabla\cdot\mathbf{J}$$

The left side must be $0$ by identity (3), so:

$$0 = \mu_0\,\nabla\cdot\mathbf{J} \quad\Longrightarrow\quad \nabla\cdot\mathbf{J} = 0 \quad \cdots (4)$$

**Here the contradiction appears.** Equation (4) forces "the divergence of $\mathbf{J}$ must always be zero." But according to Law A (charge conservation, Equation (1)):

$$\nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}$$

meaning the divergence of $\mathbf{J}$ is zero **only when $\rho$ does not change in time** ($\partial\rho/\partial t = 0$).

**Conclusion**: The original Ampère's law (2) contradicts charge conservation outright in every situation where the charge density changes with time ($\partial\rho/\partial t \neq 0$). Two verified laws cannot both be true simultaneously.

## 2.2 Visualizing the Contradiction in a Concrete Physical Situation: A Charging Capacitor

This contradiction is not an abstract mathematical curiosity — it arises in an experimentally realizable situation. The classic example is a **charging parallel-plate capacitor**.

Suppose a current $I$ flows in a circuit charging a capacitor. The integral form of Ampère's law is:

$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc}$$

where $I_{enc}$ is the current through **any** surface bounded by the closed loop $C$. By the logic of Stokes' Theorem, $I_{enc}$ must be independent of which surface we choose (only the boundary $C$ matters). Now fix the closed loop $C$ around the wire and choose two different surfaces.

**Surface $S_1$**: A flat disk cutting straight across the wire. The wire's current $I$ passes right through it.
$$I_{enc}^{(S_1)} = I$$

**Surface $S_2$**: A surface sharing the same boundary $C$, but bulging like a balloon so that it passes through the space between the two capacitor plates. Since the space between the plates is vacuum (or dielectric), no conduction current flows there.
$$I_{enc}^{(S_2)} = 0$$

For the **same boundary** $C$, we get different values $I_{enc}^{(S_1)} = I \neq 0 = I_{enc}^{(S_2)}$. But the left side $\oint_C \mathbf{B}\cdot d\boldsymbol{\ell}$ should depend only on $C$, not on which surface was chosen — an outright contradiction. This contradiction is precisely the physical manifestation of the mathematical contradiction $\nabla\cdot\mathbf{J} \neq 0$ shown above — as charge accumulates on the capacitor plates ($\partial\rho/\partial t \neq 0$), the current in the wire appears to "stop" at the plate surface.

## 2.3 The Solution: What Must Be Added to Resolve the Contradiction?

The root of the contradiction was Equation (4): "taking the divergence of $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ forces $\nabla\cdot\mathbf{J}=0$." To resolve this, we add **some term $\mathbf{X}$** to the right side of Ampère's law:

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\mathbf{X}$$

such that taking the divergence of both sides automatically matches charge conservation. The requirement is:

$$\nabla\cdot(\nabla\times\mathbf{B}) = 0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\nabla\cdot\mathbf{X}$$

$$\Longrightarrow\quad \nabla\cdot\mathbf{X} = -\nabla\cdot\mathbf{J}$$

By charge conservation (1), $-\nabla\cdot\mathbf{J} = \partial\rho/\partial t$, so:

$$\nabla\cdot\mathbf{X} = \frac{\partial\rho}{\partial t} \quad \cdots (5)$$

**Here the decisive link appears.** The differential form of Gauss's law is:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \quad\Longrightarrow\quad \rho = \varepsilon_0\,\nabla\cdot\mathbf{E}$$

Substituting this into Equation (5):

$$\nabla\cdot\mathbf{X} = \frac{\partial}{\partial t}\left(\varepsilon_0\,\nabla\cdot\mathbf{E}\right) = \nabla\cdot\left(\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right)$$

(The spatial derivative $\nabla\cdot$ and the time derivative $\partial/\partial t$ act on independent variables, so their order can be swapped.)

The **simplest and most natural solution** to this equation is:

$$\mathbf{X} = \varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

(More generally, adding $\nabla\times(\text{any vector field})$ would give the same divergence, but such arbitrariness is neither physically necessary nor consistent with experiment, so it is excluded. That is, this term is the unique, necessary and sufficient "minimal" correction.)

## 2.4 Verifying the Corrected Ampère's Law

The resulting new law (the Ampère–Maxwell law) is:

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \cdots (6)$$

Take the divergence of both sides to re-check consistency:

$$\underbrace{\nabla\cdot(\nabla\times\mathbf{B})}_{=0 \text{ (identity)}} = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\frac{\partial}{\partial t}\left(\frac{\rho}{\varepsilon_0}\right) = \mu_0\left(\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}\right)$$

$$\therefore\ \nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t} = 0$$

This is exactly charge conservation, Equation (1). **There is no longer any contradiction — charge conservation now follows automatically, almost as an identity.** $\blacksquare$

## 2.5 Confirming the Resolution with the Capacitor Example

Call the term $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ the **displacement current density** $\mathbf{J}_d \equiv \varepsilon_0\,\partial\mathbf{E}/\partial t$. Revisit the capacitor example from 2.2.

- Surface $S_1$ (through the wire): only conduction current, and $\mathbf{E}$ does not change (inside the wire) → $I_{enc} = I + 0 = I$
- Surface $S_2$ (between the plates): no conduction current ($\mathbf{J}=0$), but charge accumulates between the plates so the electric field $\mathbf{E}$ increases with time → displacement current $I_d = \varepsilon_0\dfrac{d}{dt}\displaystyle\int_{S_2}\mathbf{E}\cdot d\mathbf{A} = \varepsilon_0\dfrac{d}{dt}\left(\dfrac{Q}{\varepsilon_0 A}\right)A = \dfrac{dQ}{dt} = I$

Both surfaces now give exactly the same value $I$, so **the result no longer depends on the choice of surface.** The contradiction is fully resolved.

## 2.6 The Overall Logical Flow

$$
\begin{array}{c}
\text{Charge conservation: } \nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t} \neq 0 \ \text{(dynamic case)} \\
\Big\Downarrow \\
\text{Divergence of original Ampère's law } \nabla\times\mathbf{B}=\mu_0\mathbf{J} \Rightarrow \nabla\cdot\mathbf{J}=0 \\
\Big\Downarrow \\
\textbf{Contradiction} \\
\Big\Downarrow \\
\text{Require correction term } \mathbf{X}: \nabla\cdot\mathbf{X} = \dfrac{\partial\rho}{\partial t} \\
\Big\Downarrow \\
\text{Substitute Gauss's law} \Rightarrow \mathbf{X} = \varepsilon_0\dfrac{\partial\mathbf{E}}{\partial t} \\
\Big\Downarrow \\
\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\dfrac{\partial\mathbf{E}}{\partial t}
\end{array}
$$

What makes this argument elegant is that the displacement current term is not "a fudge fitted to experimental data" but the **pure logical consequence of two already-known laws (charge conservation + Gauss's law)**. Maxwell's insight originated not from experiment but from this **mathematical consistency** — and this very term added is what later predicts the existence of electromagnetic waves (a self-sustaining wave in which the time variation of $\nabla\times\mathbf{E}$ produces $\mathbf{B}$, whose time variation in turn produces $\mathbf{E}$ again).

---

# 3. Derivation of the Electromagnetic Wave Equation + Its Speed Equals the Speed of Light

We derive the wave equation from Maxwell's equations in vacuum (free space, $\rho=0, \mathbf{J}=0$) and show that its propagation speed exactly matches the speed of light. This is the very moment where Maxwell's theory of "electricity and magnetism" leapt to a "theory of light."

## 3.0 Starting Point: Maxwell's Equations in Vacuum (4 Equations)

Assuming free space with no charges or currents ($\rho = 0$, $\mathbf{J}=0$):

$$\nabla\cdot\mathbf{E} = 0 \quad \cdots (1)$$
$$\nabla\cdot\mathbf{B} = 0 \quad \cdots (2)$$
$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} \quad \cdots (3)$$
$$\nabla\times\mathbf{B} = \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \cdots (4)$$

Key idea: Equations (3) and (4) are **coupled**, with $\mathbf{E}$ and $\mathbf{B}$ each driving the other's time variation. The goal is to decouple these into independent equations involving only $\mathbf{E}$ and only $\mathbf{B}$.

## 3.1 The Necessary Vector Identity

For any vector field $\mathbf{F}$, the following is a purely mathematical identity (the curl-of-curl identity):

$$\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F} \quad \cdots (5)$$

Here $\nabla^2\mathbf{F}$ is the vector Laplacian (the scalar Laplacian applied to each component). This identity always holds, independent of electromagnetism.

## 3.2 Deriving the Wave Equation for E

**Step 1.** Take $\nabla\times$ of both sides of Equation (3):

$$\nabla\times(\nabla\times\mathbf{E}) = \nabla\times\left(-\frac{\partial\mathbf{B}}{\partial t}\right)$$

**Step 2.** Apply identity (5) to the left side:

$$\nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\nabla\times\frac{\partial\mathbf{B}}{\partial t}$$

**Step 3.** The first term on the left vanishes by Equation (1), $\nabla\cdot\mathbf{E}=0$:

$$-\nabla^2\mathbf{E} = -\nabla\times\frac{\partial\mathbf{B}}{\partial t}$$

**Step 4.** The spatial derivative ($\nabla\times$) and the time derivative ($\partial/\partial t$) on the right act on independent variables, so their order can be swapped:

$$-\nabla^2\mathbf{E} = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B})$$

$$\nabla^2\mathbf{E} = \frac{\partial}{\partial t}(\nabla\times\mathbf{B})$$

**Step 5 (Key: decoupling).** Now substitute Equation (4) for $\nabla\times\mathbf{B}$ on the right — this is the step that eliminates $\mathbf{B}$ entirely, leaving only $\mathbf{E}$:

$$\nabla^2\mathbf{E} = \frac{\partial}{\partial t}\left(\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right) = \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}$$

**Result**:

$$\boxed{\nabla^2\mathbf{E} - \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2} = 0} \quad \cdots (6)$$

## 3.3 Deriving the Wave Equation for B (Identical Procedure, by Symmetry)

**Step 1.** Take $\nabla\times$ of both sides of Equation (4):

$$\nabla\times(\nabla\times\mathbf{B}) = \mu_0\varepsilon_0\,\nabla\times\frac{\partial\mathbf{E}}{\partial t}$$

**Step 2.** Apply identity (5) to the left side:

$$\nabla(\nabla\cdot\mathbf{B}) - \nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\times\mathbf{E})$$

**Step 3.** The first term vanishes by Equation (2), $\nabla\cdot\mathbf{B}=0$:

$$-\nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\times\mathbf{E})$$

**Step 4.** Substitute Equation (3), $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$, on the right:

$$-\nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}\left(-\frac{\partial\mathbf{B}}{\partial t}\right) = -\mu_0\varepsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2}$$

**Result**:

$$\boxed{\nabla^2\mathbf{B} - \mu_0\varepsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2} = 0} \quad \cdots (7)$$

Note that $\mathbf{E}$ and $\mathbf{B}$ satisfy exactly the same form of equation — this is not a coincidence but a reflection of the ($\mathbf{E}\leftrightarrow\mathbf{B}$) symmetry of Maxwell's equations (up to a single sign).

## 3.4 Why This Is a "Wave Equation"

The standard form of the 3D wave equation is:

$$\nabla^2\psi - \frac{1}{v^2}\frac{\partial^2\psi}{\partial t^2} = 0$$

where $v$ is the wave's propagation speed. This can be confirmed by noting that a function such as $\psi(x,t) = f(x - vt)$ (a waveform of fixed shape moving with speed $v$) satisfies this equation: $\partial^2\psi/\partial x^2 = f''$, $\partial^2\psi/\partial t^2 = v^2 f''$, so substitution gives an identity of zero.

Comparing Equations (6) and (7) with this standard form:

$$\frac{1}{v^2} = \mu_0\varepsilon_0 \quad\Longrightarrow\quad v = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

That is, we arrive purely mathematically at the conclusion that **$\mathbf{E}$ and $\mathbf{B}$ are each waves propagating through space at speed $v = 1/\sqrt{\mu_0\varepsilon_0}$**. We define this speed as $c$:

$$c \equiv \frac{1}{\sqrt{\mu_0\varepsilon_0}} \quad \cdots (8)$$

## 3.5 Numerical Verification: Does c Really Equal the Speed of Light?

The constants known in Maxwell's era (1860s):

- Vacuum permeability: $\mu_0 = 4\pi\times 10^{-7}\ \text{T}\cdot\text{m/A}$ (an exact value by definition at that time)
- Vacuum permittivity: $\varepsilon_0 \approx 8.854\times 10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$ (measured by Weber, Kohlrausch, and others through electrostatic/current experiments)

These two constants came from **completely independent experiments**:

- $\mu_0$ from the force between two currents (a magnetic phenomenon, Ampère's experiments)
- $\varepsilon_0$ from the charge–voltage relation of a capacitor (an electrostatic phenomenon, Coulomb/Cavendish-type experiments)

and had, at first, nothing whatsoever to do with light or optics.

Computed result:

$$\mu_0\varepsilon_0 \approx 1.1127\times10^{-17}\ \text{s}^2/\text{m}^2$$

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 2.998\times 10^{8}\ \text{m/s} \approx 299{,}792{,}458\ \text{m/s}$$

This value matched — within the experimental uncertainty of the time — **the speed of light already independently measured through optical experiments by Fizeau, Foucault, and others**. (Today, $c$ is instead fixed as the defined constant $299{,}792{,}458\ \text{m/s}$, and the meter is defined in terms of it; but in Maxwell's era, $c$ was an independently measured quantity, and that fact is what matters here.)

**Maxwell's conclusion** (around 1862, in "A Dynamical Theory of the Electromagnetic Field," 1865): Two constants obtained purely from electric and magnetic experiments were combined, and the result matched — down to the decimal — the speed of light measured in an entirely different field, optics. This could not be a coincidence — **therefore light itself is an electromagnetic phenomenon: an electromagnetic wave.**

## 3.6 Summary of the Logical Structure of the Derivation

| Step | Equation Used | What Is Eliminated |
|---|---|---|
| $\nabla\times(3)$ | Faraday's law | — |
| Apply the curl-of-curl identity | Vector identity | The $\nabla(\nabla\cdot\mathbf{E})$ term (eliminated via Gauss's law) |
| Substitute (4) for $\nabla\times\mathbf{B}$ | Ampère–Maxwell law | $\mathbf{B}$ is eliminated entirely, leaving only $\mathbf{E}$ |

It matters that **all four equations were used** in this derivation:

- Gauss's law (E, B) → eliminates the $\nabla(\nabla\cdot\mathbf{F})$ term
- Faraday's law → links $\mathbf{B}$ to the time derivative of $\mathbf{E}$
- **The Ampère–Maxwell law (with the displacement current)** → completes this coupling loop

If the displacement current term $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ were absent (i.e., using only the original Ampère's law), the $\partial^2\mathbf{E}/\partial t^2$ term itself would never appear in Step 5 — **the wave equation would not arise at all**, meaning the prediction of electromagnetic waves would have been impossible. This is why the displacement current was a necessary precondition for this entire story.

---

# 4. The Mathematical Statement of the Absence of Magnetic Monopoles

We show why the physical statement "no magnetic monopoles exist" is expressed precisely by the equation $\nabla\cdot\mathbf{B}=0$, contrasting it with the case of the electric field.

## 4.1 Control Case: The Electric Field Has "Monopoles"

First consider the comparison case, Gauss's law (electric):

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}$$

Here $\rho$ is the **charge density**. A single electron (negative charge) can exist on its own, and a single proton (positive charge) can also exist on its own. In other words, the electric field has a **"source" that can exist in isolation**: the electric charge.

In integral form:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{enc}}{\varepsilon_0}$$

If we enclose a single charge with any closed surface $S$, the **net outward** flux through that surface is nonzero. Electric field lines are open lines that "begin" at positive charges and "end" at negative charges — that is, divergence (a source/sink) exists.

## 4.2 The Magnetic Field Case: The Corresponding Law

$$\nabla\cdot\mathbf{B} = 0$$

The key point is that the right-hand side is **always, unconditionally, zero**. Whereas Gauss's law (electric) had $\rho/\varepsilon_0$ on the right — a physical quantity that may or may not exist — this equation's right side has no such place to begin with, meaning that a quantity called "magnetic charge density" does not exist in the theory.

## 4.3 Linking Directly to the Physical Meaning of Divergence

The divergence $\nabla\cdot\mathbf{B}$ represents how much $\mathbf{B}$ has a **net outflow** near a point. If magnetic monopoles (say, an isolated north pole, or a "magnetic charge" $\rho_m$) existed, the theory would need to have a form such as:

$$\nabla\cdot\mathbf{B} = \mu_0\,\rho_m \quad (\text{a hypothetical equation that does not actually hold})$$

$\nabla\cdot\mathbf{B}=0$ mathematically states that this $\rho_m$ is **identically zero** — that is, no magnetic monopole exists anywhere in the universe.

## 4.4 Relation to the Integral Form (Via the Divergence Theorem)

$$\oint_S \mathbf{B}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{B})\, dV = 0$$

The meaning of this equation: **for any closed surface, the number of magnetic field lines leaving it exactly equals the number entering it.**

This is the mathematical expression of the familiar fact that "no matter how you cut a magnet, you always get a paired N pole and S pole." Consider a bar magnet:

- The magnetic field lines threading through and around the magnet form **closed loops** that leave the N pole and **come back in** at the S pole (unlike open electric field lines, they have neither beginning nor end).
- If we enclose the entire magnet with any closed surface $S$, the number of field lines leaving (near the N pole) exactly cancels the number re-entering (near the S pole), giving zero net flux.
- Even if we shrink the closed surface to wrap tightly around only the N pole, the same holds — it is impossible to construct a closed surface enclosing only the N pole while excluding the S pole (the N pole cannot be "isolated"). This is precisely the decisive difference from electric charge: a charge can always be enclosed on its own by a small closed surface (so $\oint\mathbf{E}\cdot d\mathbf{A}\neq 0$ is possible), but a magnet, no matter how finely divided, always comes with an N–S pair.

## 4.5 Correspondence Table

| | Electric Field | Magnetic Field |
|---|---|---|
| Differential form | $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ | $\nabla\cdot\mathbf{B} = 0$ |
| Integral form | $\oint\mathbf{E}\cdot d\mathbf{A} = Q_{enc}/\varepsilon_0$ | $\oint\mathbf{B}\cdot d\mathbf{A} = 0$ |
| Shape of field lines | **Open lines** beginning/ending at charges | **Closed loops** with neither beginning nor end |
| Source | Charge $\rho$ (can exist in isolation) | Magnetic monopole $\rho_m$ — **does not exist** |
| Can be isolated by a closed surface? | Yes (a single charge can be enclosed) | No (N and S always come as a pair) |

So $\nabla\cdot\mathbf{B}=0$ is not simply "an equation whose right side happens to be zero" — it is the most compressed possible statement that **"magnetic monopoles have no place at all within the equation system of this universe."** (For reference, theoretical extensions allowing magnetic monopoles do exist — the Dirac monopole — but none has ever been experimentally discovered.)

---

# 5. Deriving from First Principles: Coulomb's Law and the Biot–Savart Law

Coulomb's law and the Biot–Savart law are **experimental laws** for the fields produced, respectively, by static charges and steady currents. Starting from these, we show the derivation of Gauss's law and (magnetostatic) Ampère's law. This is precisely the "historical origin" of Maxwell's equations.

## Part A. Coulomb's Law → Gauss's Law

### A.1 Coulomb's Law for a Point Charge

For a charge $q$ at the origin, the electric field at position $\mathbf{r}$:

$$\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{\mathbf{r}}$$

This is a law obtained purely through experiment (Coulomb's torsion balance experiment, 1785).

### A.2 Computing the Flux Through a Sphere Enclosing the Point Charge

Place a sphere $S$ of radius $r$ centered on the charge $q$ and compute the flux. At every point on the sphere, $\mathbf{E}$ points in the $\hat{\mathbf{r}}$ direction, and the area element $d\mathbf{A}$ (the outward normal of the sphere) also points in the $\hat{\mathbf{r}}$ direction, so $\mathbf{E}\cdot d\mathbf{A} = E\,dA$:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \oint_S \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\, dA = \frac{q}{4\pi\varepsilon_0 r^2}\oint_S dA$$

Since the sphere's surface area is $\oint_S dA = 4\pi r^2$:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\varepsilon_0 r^2}\cdot 4\pi r^2 = \frac{q}{\varepsilon_0}$$

**Key observation**: $r$ has completely cancelled out of the result — the flux is independent of the sphere's radius. This is because the $1/r^2$ dependence of Coulomb's law exactly cancels the $r^2$ dependence of the sphere's surface area — the **necessary consequence of the inverse-square law**.

### A.3 Extending to an Arbitrary Closed Surface (the Solid Angle Argument)

Now consider an **arbitrarily shaped** closed surface $S'$ enclosing the charge $q$. The flux through a small area element $d\mathbf{A}$ on $S'$ is:

$$d\Phi = \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf{r}}\cdot d\mathbf{A}}{r^2}$$

Here $\hat{\mathbf{r}}\cdot d\mathbf{A}/r^2$ is precisely the definition of the **solid angle** $d\Omega$ subtended by that area element as seen from the charge:

$$d\Omega \equiv \frac{\hat{\mathbf{r}}\cdot d\mathbf{A}}{r^2}$$

so:

$$d\Phi = \frac{q}{4\pi\varepsilon_0}\,d\Omega$$

Integrating over the whole closed surface, since a closed surface enclosing a charge always subtends the entire $4\pi$ steradians of solid angle:

$$\Phi = \oint_{S'} d\Phi = \frac{q}{4\pi\varepsilon_0}\oint d\Omega = \frac{q}{4\pi\varepsilon_0}\cdot 4\pi = \frac{q}{\varepsilon_0}$$

**In other words, whether the surface is a sphere or an irregular shape, the flux is exactly $q/\varepsilon_0$.** (If the charge lies outside the closed surface, the solid angle "entering" and "leaving" through the surface cancels exactly, giving zero net flux — a charge outside a closed surface contributes nothing to the flux.)

### A.4 Extending from Multiple Charges to a Continuous Charge Distribution via Superposition

Because the electric field is linear (an experimental fact already known before Maxwell's equations), if several charges $q_1, q_2, \ldots$ are present, the total field is the vector sum of the individual fields:

$$\mathbf{E} = \sum_i \mathbf{E}_i$$

Since flux through a surface $S$ is also linear:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \sum_i \oint_S \mathbf{E}_i\cdot d\mathbf{A} = \sum_{i:\, q_i \text{ inside}} \frac{q_i}{\varepsilon_0} = \frac{Q_{enc}}{\varepsilon_0}$$

(Charges outside contribute zero, as shown in A.3, and drop out of the sum automatically.) For a continuous charge distribution $\rho(\mathbf{r})$, $Q_{enc} = \int_V \rho\,dV$, so:

$$\boxed{\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{1}{\varepsilon_0}\int_V \rho\, dV} \quad \text{(Integral form of Gauss's law)}$$

### A.5 Converting to the Differential Form

Applying the Divergence Theorem $\oint_S\mathbf{E}\cdot d\mathbf{A} = \int_V(\nabla\cdot\mathbf{E})dV$ together with the "arbitrary volume" argument (see Section 1.1):

$$\boxed{\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}}$$

**Summary**: The $1/r^2$ dependence of Coulomb's law → the geometric fact that solid angle always totals $4\pi$ → the conclusion that flux is independent of surface shape → Gauss's law. **Gauss's law carries the same information as Coulomb's law, but repackaged from a specific "inverse-square" form into the local statement that "the divergence is proportional to the charge density."**

## Part B. The Biot–Savart Law → (Magnetostatic) Ampère's Law

### B.1 The Biot–Savart Law

For a steady-current ($\partial\rho/\partial t=0$) density $\mathbf{J}(\mathbf{r}')$, the resulting magnetic field:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\times\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^3}\, dV'$$

Like Coulomb's law, this is a purely experimental law (Biot & Savart, 1820, immediately after Ørsted's discovery).

### B.2 Converting to the Vector Potential Representation (A Trick to Simplify the Calculation)

Before directly computing the curl, we use the mathematical fact:

$$\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^3} = -\nabla\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right)$$

(Here $\nabla$ is the derivative with respect to $\mathbf{r}$, with $\mathbf{r}'$ treated as the fixed integration variable.) Substituting:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\times\left[-\nabla\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right]dV' = \frac{\mu_0}{4\pi}\int_V \nabla\frac{1}{|\mathbf{r}-\mathbf{r}'|}\times\mathbf{J}(\mathbf{r}')\,dV'$$

Applying the vector identity $\nabla f\times\mathbf{c} = -\nabla\times(f\mathbf{c})$ (valid when $\mathbf{c}$ is a vector constant with respect to $\mathbf{r}$, as is the case here since $\mathbf{J}(\mathbf{r}')$ is not a function of $\mathbf{r}$) and simplifying, we ultimately get:

$$\mathbf{B}(\mathbf{r}) = \nabla\times\left[\frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\,dV'\right] \equiv \nabla\times\mathbf{A}(\mathbf{r})$$

where we have defined the **vector potential**:

$$\mathbf{A}(\mathbf{r}) \equiv \frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\, dV'$$

(Since $\nabla\times\nabla f \equiv 0$, writing $\mathbf{B}=\nabla\times\mathbf{A}$ automatically gives $\nabla\cdot\mathbf{B}=\nabla\cdot(\nabla\times\mathbf{A})=0$ — this shows that Gauss's law (magnetic) is already implicit in the Biot–Savart law.)

### B.3 Computing the Curl of B

The goal is now to compute $\nabla\times\mathbf{B} = \nabla\times(\nabla\times\mathbf{A})$. We use the curl-of-curl identity:

$$\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$$

**Coulomb Gauge**: One can show from the definition of $\mathbf{A}$ that $\nabla\cdot\mathbf{A}=0$ (provable by integration by parts using the steady-current condition $\nabla\cdot\mathbf{J}=0$; we simply use the result here). So the first term vanishes:

$$\nabla\times\mathbf{B} = -\nabla^2\mathbf{A} = -\frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\,\nabla^2\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right)dV'$$

### B.4 The Delta-Function Identity (A Key Result of Potential Theory)

Here we use a well-known identity from electrostatics (potential theory):

$$\nabla^2\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right) = -4\pi\,\delta^3(\mathbf{r}-\mathbf{r}')$$

(This identity is proven from the fact that $1/|\mathbf{r}-\mathbf{r}'|$ satisfies Laplace's equation for $\mathbf{r}\neq\mathbf{r}'$, together with applying the Divergence Theorem to a tiny sphere near the origin to obtain the coefficient $-4\pi$. This is essentially the same mathematics as the requirement, in electrostatics, that the point-charge potential $\phi = q/(4\pi\varepsilon_0 r)$ satisfies Gauss's law $\nabla^2\phi = -\rho/\varepsilon_0$.)

Substituting:

$$\nabla\times\mathbf{B} = -\frac{\mu_0}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\left[-4\pi\,\delta^3(\mathbf{r}-\mathbf{r}')\right]dV' = \mu_0\int_V \mathbf{J}(\mathbf{r}')\,\delta^3(\mathbf{r}-\mathbf{r}')\,dV'$$

By the sifting property of the delta function, the integral is computed immediately:

$$\boxed{\nabla\times\mathbf{B} = \mu_0\mathbf{J}(\mathbf{r})} \quad \text{(Differential form, magnetostatic Ampère's law)}$$

### B.5 Converting to the Integral Form

Applying Stokes' Theorem:

$$\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \int_S(\nabla\times\mathbf{B})\cdot d\mathbf{A} = \mu_0\int_S \mathbf{J}\cdot d\mathbf{A} = \mu_0 I_{enc}$$

$$\boxed{\oint_C \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0 I_{enc}} \quad \text{(Integral form, magnetostatic Ampère's law)}$$

## 5.6 The Symmetric Overall Logical Flow

| | Electric (Part A) | Magnetic (Part B) |
|---|---|---|
| Starting experimental law | Coulomb's law $\mathbf{E}\propto \hat{\mathbf{r}}/r^2$ | Biot–Savart law $\mathbf{B}\propto \mathbf{J}\times\hat{\mathbf{r}}/r^2$ |
| Key geometric fact | Total solid angle $=4\pi$ | Green's function $\nabla^2(1/r) = -4\pi\delta^3$ |
| Intermediate result | Closed-surface flux $=q/\varepsilon_0$, independent of surface shape | $\mathbf{B}=\nabla\times\mathbf{A}$, so $\nabla\cdot\mathbf{B}=0$ automatically |
| Final differential form | $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ | $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ |
| Integral theorem used | Divergence Theorem | Stokes' Theorem |

The two laws obtained this way — $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ and $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ — are precisely the electrostatics/magnetostatics laws that existed **before Maxwell**. Adding Faraday's law of induction (an experimental discovery, $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$) and the **displacement current correction** discussed in Section 2 ($\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$), the four complete Maxwell's equations are finally assembled.

So the entire historical and logical lineage is:

$$\text{Coulomb's law} \to \text{Gauss's law (E)}, \qquad \text{Biot–Savart law} \to \text{Ampère's law (static)} \to \text{(displacement current added)} \to \text{Ampère–Maxwell law}$$

These four stages combine into the single, complete system known as Maxwell's equations.

---

# 6. Relativistic Covariant Formalism and Four-Vector Notation

We show that the four Maxwell's equations actually compress into **just two four-dimensional tensor equations**. This most starkly reveals that special relativity and electromagnetism were, from the very beginning, a single unified whole.

## 6.0 Notational Conventions (Minkowski Spacetime)

We use the $(+,-,-,-)$ signature for the metric:

$$\eta_{\mu\nu} = \text{diag}(1,-1,-1,-1)$$

Four-coordinates: $x^\mu = (ct, x, y, z)$, $\mu = 0,1,2,3$

Partial derivative operator (lower index, covariant):
$$\partial_\mu \equiv \frac{\partial}{\partial x^\mu} = \left(\frac{1}{c}\frac{\partial}{\partial t}, \nabla\right)$$

Upper-index (contravariant) derivative operator:
$$\partial^\mu = \eta^{\mu\nu}\partial_\nu = \left(\frac{1}{c}\frac{\partial}{\partial t}, -\nabla\right)$$

We use the Einstein summation convention (repeated upper and lower indices are automatically summed).

## 6.1 Introducing the Four-Potential

**Motivation**: $\nabla\cdot\mathbf{B}=0$ is automatically satisfied if we introduce the vector potential $\mathbf{A}$ by writing

$$\mathbf{B} = \nabla\times\mathbf{A}$$

owing to the identity $\nabla\cdot(\nabla\times\mathbf{A})\equiv 0$. Substituting this into Faraday's law $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$:

$$\nabla\times\mathbf{E} = -\frac{\partial}{\partial t}(\nabla\times\mathbf{A}) = -\nabla\times\frac{\partial\mathbf{A}}{\partial t}$$

$$\nabla\times\left(\mathbf{E}+\frac{\partial\mathbf{A}}{\partial t}\right) = 0$$

A vector field with zero curl can be written as the gradient of some scalar function (since $\nabla\times\nabla\phi\equiv 0$):

$$\mathbf{E} + \frac{\partial\mathbf{A}}{\partial t} = -\nabla\phi \quad\Longrightarrow\quad \mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}$$

By introducing the scalar potential $\phi$ and vector potential $\mathbf{A}$ this way, **Gauss's law (magnetic) and Faraday's law (the two homogeneous equations) are automatically and identically satisfied.**

**Key observation**: $\phi$ and $\mathbf{A}$ together have exactly 4 components, which can be bundled into a single four-vector:

$$A^\mu \equiv \left(\frac{\phi}{c}, \mathbf{A}\right)$$

That this actually transforms as a four-vector under Lorentz transformations requires a separate proof (a standard result of relativistic electromagnetism); here we accept this construction and follow its consequences.

## 6.2 Defining the Electromagnetic Field Tensor (Faraday Tensor)

$$F^{\mu\nu} \equiv \partial^\mu A^\nu - \partial^\nu A^\mu$$

By definition this is an **antisymmetric tensor** ($F^{\mu\nu}=-F^{\nu\mu}$, so all diagonal components are zero); since a $4\times4$ antisymmetric matrix has $6$ independent components, this matches exactly the 3 components of $\mathbf{E}$ plus the 3 components of $\mathbf{B}$.

### 6.2.1 Direct Computation of Components

Compute the $F^{0i}$ components ($i=1,2,3$ are spatial components):

$$F^{0i} = \partial^0 A^i - \partial^i A^0$$

Since $\partial^0 = \frac{1}{c}\partial_t$, $\partial^i = -\partial_i$ (the sign flips for spatial upper indices), $A^i = A_i$ (the components of the 3-vector $\mathbf{A}$), and $A^0 = \phi/c$:

$$F^{0i} = \frac{1}{c}\frac{\partial A^i}{\partial t} - (-\partial_i)\frac{\phi}{c} = \frac{1}{c}\left(\frac{\partial A^i}{\partial t} + \partial_i \phi\right) = -\frac{1}{c}\left(-\partial_i\phi - \frac{\partial A^i}{\partial t}\right) = -\frac{E^i}{c}$$

(In the last step we used $\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$.) That is:

$$F^{0i} = -\frac{E_i}{c}, \qquad F^{i0} = \frac{E_i}{c}$$

Now the $F^{ij}$ components (both $i,j$ spatial):

$$F^{ij} = \partial^i A^j - \partial^j A^i = -\partial_i A^j + \partial_j A^i = -(\partial_i A_j - \partial_j A_i)$$

This connects directly to the components of $\mathbf{B}=\nabla\times\mathbf{A}$, i.e., $B_k = \epsilon_{kij}\partial_i A_j$ (using the Levi-Civita symbol). Computing explicitly:

$$F^{12} = -(\partial_1 A_2 - \partial_2 A_1) = -B_3, \quad F^{23} = -B_1, \quad F^{31} = -B_2$$

### 6.2.2 The Completed Matrix Form

$$F^{\mu\nu} = \begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{pmatrix}$$

Both $\mathbf{E}$ and $\mathbf{B}$ are contained within this single tensor — **the electric and magnetic fields are not separate, independent fields, but simply the "time-space" and "space-space" components of a single spacetime tensor $F^{\mu\nu}$, sliced according to the observer's reference frame.** (Indeed, under a Lorentz boost, $\mathbf{E}$ and $\mathbf{B}$ mix into each other — this is the real reason the name "electromagnetic field" refers to a single entity.)

## 6.3 The Homogeneous Maxwell Equations (Gauss-B, Faraday) → the Bianchi Identity

Simply from the fact that $F^{\mu\nu}=\partial^\mu A^\nu - \partial^\nu A^\mu$ by definition, the following holds **identically** (derived from the commutativity of partial derivatives, $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$):

$$\boxed{\partial^\lambda F^{\mu\nu} + \partial^\mu F^{\nu\lambda} + \partial^\nu F^{\lambda\mu} = 0} \quad \text{(Bianchi identity)}$$

**Proof**: Substituting $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$:

$$\partial^\lambda(\partial^\mu A^\nu - \partial^\nu A^\mu) + \partial^\mu(\partial^\nu A^\lambda - \partial^\lambda A^\nu) + \partial^\nu(\partial^\lambda A^\mu - \partial^\mu A^\lambda)$$

Expanding gives six terms: $\partial^\lambda\partial^\mu A^\nu$, $-\partial^\lambda\partial^\nu A^\mu$, $\partial^\mu\partial^\nu A^\lambda$, $-\partial^\mu\partial^\lambda A^\nu$, $\partial^\nu\partial^\lambda A^\mu$, $-\partial^\nu\partial^\mu A^\lambda$, which cancel exactly in pairs by the commutativity of partial derivatives ($\partial^\lambda\partial^\mu A^\nu$ cancels with $-\partial^\mu\partial^\lambda A^\nu$, and so on). So the entire expression is $0$. $\blacksquare$

**This single identity contains both Gauss's law (magnetic) and Faraday's law.** Substituting the spatial indices $(\lambda,\mu,\nu)=(1,2,3)$ gives $\nabla\cdot\mathbf{B}=0$, while indices mixing in the time component $0$ give Faraday's law.

## 6.4 The Inhomogeneous Maxwell Equations (Gauss-E, Ampère-Maxwell)

### 6.4.1 Defining the Four-Current

$$J^\mu \equiv (c\rho, \mathbf{J})$$

That this transforms as a four-vector follows from the requirement that charge conservation be Lorentz invariant.

### 6.4.2 The Covariant Equation

The remaining two equations (Gauss-E, Ampère-Maxwell) combine into the single tensor equation:

$$\boxed{\partial_\mu F^{\mu\nu} = \mu_0 J^\nu}$$

### 6.4.3 Recovering the Original Equations Component by Component

**The $\nu=0$ component**:
$$\partial_\mu F^{\mu 0} = \mu_0 J^0$$
$$\partial_0 F^{00} + \partial_i F^{i0} = \mu_0 (c\rho)$$

Since $F^{00}=0$ (diagonal components vanish by antisymmetry) and $F^{i0}=E_i/c$:

$$\partial_i\left(\frac{E_i}{c}\right) = \mu_0 c\rho \quad\Longrightarrow\quad \nabla\cdot\mathbf{E} = \mu_0 c^2 \rho$$

Using $\mu_0 c^2 = \mu_0\cdot\dfrac{1}{\mu_0\varepsilon_0} = \dfrac{1}{\varepsilon_0}$ (with $c^2=1/\mu_0\varepsilon_0$ from Section 3):

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \quad \checkmark \text{Gauss's law (electric)}$$

**The $\nu=k$ (spatial) components, $k=1,2,3$**:
$$\partial_\mu F^{\mu k} = \mu_0 J^k = \mu_0 J_k$$
$$\partial_0 F^{0k} + \partial_j F^{jk} = \mu_0 J_k$$

Since $F^{0k}=-E_k/c$ and $\partial_0 = \frac1c\partial_t$, the first term becomes $-\dfrac{1}{c^2}\dfrac{\partial E_k}{\partial t}$. Since $F^{jk}$ has the form $-\epsilon_{jkl}B_l$, the second term corresponds to $(\nabla\times\mathbf{B})_k$ (after sorting out the sign). Rearranging:

$$(\nabla\times\mathbf{B})_k - \frac{1}{c^2}\frac{\partial E_k}{\partial t} = \mu_0 J_k$$

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \frac{1}{c^2}\frac{\partial\mathbf{E}}{\partial t} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \quad \checkmark \text{Ampère–Maxwell law}$$

**Thus all four Maxwell's equations compress into just two tensor equations:**

$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad (\text{inhomogeneous, 2 equations}) \qquad\qquad \partial^{[\lambda}F^{\mu\nu]}=0 \quad (\text{homogeneous, 2 equations})$$

## 6.5 Charge Conservation = Four-Divergence = 0 (Automatically Derived)

Taking $\partial_\nu$ of both sides of $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ once more:

$$\partial_\nu\partial_\mu F^{\mu\nu} = \mu_0\,\partial_\nu J^\nu$$

On the left, $\partial_\nu\partial_\mu$ is symmetric in $\mu,\nu$ (partial derivatives commute), while $F^{\mu\nu}$ is antisymmetric — the contraction of a symmetric quantity with an antisymmetric one is identically $0$:

$$\partial_\nu\partial_\mu F^{\mu\nu} = 0 \quad\Longrightarrow\quad \partial_\nu J^\nu = 0$$

Written out in components:

$$\partial_\nu J^\nu = \partial_0 J^0 + \partial_i J^i = \frac{1}{c}\partial_t(c\rho) + \nabla\cdot\mathbf{J} = \frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J} = 0$$

In other words, **charge conservation follows automatically from the mathematical structure (antisymmetry) of the equation $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$ itself.** This means that the process in Section 2 — where the displacement current had to be manually fitted in to match charge conservation — is, in the covariant formalism, **already built in automatically, with no need for it at all.** This is a prime example of the elegance of the covariant formalism.

## 6.6 The Lorenz Gauge and the Covariant Derivation of the Wave Equation

Substituting $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ into $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$:

$$\partial_\mu(\partial^\mu A^\nu - \partial^\nu A^\mu) = \mu_0 J^\nu$$

$$\partial_\mu\partial^\mu A^\nu - \partial^\nu(\partial_\mu A^\mu) = \mu_0 J^\nu$$

Impose the **Lorenz gauge condition** (a choice made using the gauge freedom):

$$\partial_\mu A^\mu = 0 \quad\Longleftrightarrow\quad \frac{1}{c^2}\frac{\partial\phi}{\partial t} + \nabla\cdot\mathbf{A} = 0$$

Then the second term vanishes:

$$\partial_\mu\partial^\mu A^\nu = \mu_0 J^\nu$$

Here $\partial_\mu\partial^\mu \equiv \Box$ is the operator known as the **d'Alembertian**:

$$\Box \equiv \partial_\mu\partial^\mu = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2$$

so:

$$\boxed{\Box A^\nu = \mu_0 J^\nu}$$

In vacuum ($J^\nu=0$):

$$\Box A^\nu = 0 \quad\Longrightarrow\quad \nabla^2 A^\nu - \frac{1}{c^2}\frac{\partial^2 A^\nu}{\partial t^2}=0$$

This unifies the wave equations for $\mathbf{E}$ and $\mathbf{B}$ derived separately in Section 3 into a **single four-vector equation** for $A^\nu$ (and hence $\phi,\mathbf{A}$). Moreover, since $\Box$ is a Lorentz-invariant operator, this reveals that this wave equation takes the same form in every inertial frame — that is, the second postulate of special relativity, that **the speed of light $c$ is the same in every inertial frame**, was already built into electromagnetic theory.

## 6.7 The Covariant Form of the Lorentz Force

Finally, the equation of motion (Lorentz force) for a particle of charge $q$ with four-velocity $u^\mu = \gamma(c,\mathbf{v})$ can also be written in covariant form:

$$\boxed{\frac{dp^\mu}{d\tau} = q\,F^{\mu\nu}u_\nu}$$

Here $p^\mu$ is the four-momentum and $\tau$ is the proper time. Working out the spatial components ($\mu=i$) recovers exactly the familiar $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ — meaning that including the force exerted by the electromagnetic field on a particle, the entirety of electromagnetism is completed within the single tensor $F^{\mu\nu}$.

## 6.8 Overall Summary

| 3D Form (4 equations) | 4D Covariant Form (2 equations) |
|---|---|
| $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$, the $\nu=0$ component |
| $\nabla\times\mathbf{B}-\frac{1}{c^2}\partial_t\mathbf{E}=\mu_0\mathbf{J}$ | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$, the $\nu=i$ components |
| $\nabla\cdot\mathbf{B}=0$ | Spatial component of the Bianchi identity |
| $\nabla\times\mathbf{E}+\partial_t\mathbf{B}=0$ | Mixed spacetime component of the Bianchi identity |

The reason this compression is not merely notational convenience is that $F^{\mu\nu}$ transforms **exactly as a tensor** under Lorentz transformations. That is, what appears as a pure electric field in one inertial frame may appear as a mixture of electric and magnetic fields in another (with $\mathbf{E},\mathbf{B}$ mixing together), while $F^{\mu\nu}$ as a whole consistently describes this transformation as a single geometric object. This is the mathematical substance of the fact — made explicit by Einstein in 1905 — that Maxwell had (unknowingly) already planted special relativity within his equations.

---

# 7. Detailed Proof of Gauge Transformations and Modern Extensions

Gauge transformation is "the freedom to express the same physical situation with different formulas." We give a rigorous proof of why this freedom exists, why $F^{\mu\nu}$ is invariant under it, and then explore how it extends into modern physics (quantum mechanics, the Standard Model).

## Part 1. The Definition and Origin of Gauge Transformations

### 1.1 Why Gauge Freedom Arises

Having defined $\mathbf{B}=\nabla\times\mathbf{A}$, the vector identity $\nabla\times(\nabla f)\equiv 0$ (for any scalar function $f$) means that changing

$$\mathbf{A}' = \mathbf{A} + \nabla\chi$$

still gives $\nabla\times\mathbf{A}' = \nabla\times\mathbf{A} + \nabla\times(\nabla\chi) = \nabla\times\mathbf{A} = \mathbf{B}$, i.e., **the same $\mathbf{B}$**. In four-dimensional notation, this is precisely:

$$A^\mu \to A'^\mu = A^\mu + \partial^\mu\lambda$$

($\lambda$ is an arbitrary scalar function of the spacetime coordinates $x^\mu$ — the "gauge function")

**Intuition**: $A^\mu$ itself is not a "real" physical quantity but an auxiliary variable introduced for computational convenience; what is actually measurable is $\mathbf{E},\mathbf{B}$ (i.e., $F^{\mu\nu}$). The map from $A^\mu$ to $F^{\mu\nu}$ is **many-to-one, not one-to-one**, so there exist infinitely many $A^\mu$'s that yield the same $F^{\mu\nu}$.

### 1.2 Gauge Invariance of $F^{\mu\nu}$ — Rigorous Proof

**Claim**: $F^{\mu\nu}=\partial^\mu A^\nu - \partial^\nu A^\mu$ is invariant under the transformation $A^\mu\to A^\mu+\partial^\mu\lambda$.

**Proof**: Compute the transformed tensor directly.

$$F'^{\mu\nu} = \partial^\mu A'^\nu - \partial^\nu A'^\mu = \partial^\mu(A^\nu+\partial^\nu\lambda) - \partial^\nu(A^\mu+\partial^\mu\lambda)$$

$$= \partial^\mu A^\nu - \partial^\nu A^\mu + \partial^\mu\partial^\nu\lambda - \partial^\nu\partial^\mu\lambda$$

$$= F^{\mu\nu} + \left(\partial^\mu\partial^\nu\lambda - \partial^\nu\partial^\mu\lambda\right)$$

If $\lambda$ is a smooth function, partial derivatives commute regardless of order (Clairaut/Schwarz theorem):

$$\partial^\mu\partial^\nu\lambda = \partial^\nu\partial^\mu\lambda$$

so the bracketed term is identically $0$:

$$\boxed{F'^{\mu\nu} = F^{\mu\nu}}$$

$\blacksquare$

**In other words, the "core mechanism" of gauge transformation is precisely the commutativity of partial derivatives.** This is the four-dimensional version of the 3D fact $\nabla\times\nabla\chi=0$.

### 1.3 Re-verifying via the 3D Components

Writing out the four-dimensional gauge transformation $A^\mu\to A^\mu+\partial^\mu\lambda$ in components:

$$A^0 \to A^0 + \partial^0\lambda = \frac{\phi}{c} + \frac{1}{c}\frac{\partial\lambda}{\partial t} \quad\Longrightarrow\quad \phi\to\phi+\frac{\partial\lambda}{\partial t}$$

$$A^i \to A^i + \partial^i\lambda = A^i - \partial_i\lambda \quad\Longrightarrow\quad \mathbf{A}\to\mathbf{A}-\nabla\lambda$$

(The sign flip is because $\partial^i=-\partial_i$. By convention, redefining $\chi\equiv-\lambda$ gives the familiar form.) In the standard convention:

$$\mathbf{A}\to\mathbf{A}+\nabla\chi, \qquad \phi\to\phi-\frac{\partial\chi}{\partial t}$$

Substituting this directly into $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$ to re-verify invariance:

$$\mathbf{E}' = -\nabla\left(\phi-\frac{\partial\chi}{\partial t}\right) - \frac{\partial}{\partial t}\left(\mathbf{A}+\nabla\chi\right)$$

$$= -\nabla\phi + \nabla\frac{\partial\chi}{\partial t} - \frac{\partial\mathbf{A}}{\partial t} - \frac{\partial}{\partial t}\nabla\chi$$

Since $\nabla$ and $\partial/\partial t$ act on independent variables and commute, $\nabla(\partial\chi/\partial t)$ and $-\partial(\nabla\chi)/\partial t$ cancel exactly:

$$\mathbf{E}' = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t} = \mathbf{E} \quad\checkmark$$

$\mathbf{B}' = \nabla\times\mathbf{A}' = \nabla\times\mathbf{A}+\nabla\times(\nabla\chi) = \mathbf{B}$ (already confirmed in 1.1) $\checkmark$

## Part 2. Gauge Fixing

The fact that $A^\mu$ has infinite freedom means that, for practical calculation, we need to **choose one representative**. This is called "fixing the gauge."

### 2.1 The Lorenz Gauge

$$\partial_\mu A^\mu = 0$$

**Proof that one can always move from an arbitrary gauge to the Lorenz gauge**: Even if some $A^\mu$ has $\partial_\mu A^\mu = f(x)\neq 0$, applying a gauge transformation $A'^\mu = A^\mu+\partial^\mu\lambda$ gives:

$$\partial_\mu A'^\mu = \partial_\mu A^\mu + \partial_\mu\partial^\mu\lambda = f + \Box\lambda$$

For this to be $0$, we need to solve $\Box\lambda = -f$. This is a sourced wave equation, so (via Green's function methods, etc.) a solution $\lambda$ **always exists**. So starting from any $A^\mu$, we can always move to some $A'^\mu$ satisfying the Lorenz gauge. Advantage of this gauge: Lorentz invariance remains manifest, making relativistic calculations (such as $\Box A^\nu=\mu_0 J^\nu$ in Section 6.6) clean.

The Lorenz gauge itself is not entirely unique either — there remains **residual gauge freedom** satisfying $\Box\lambda=0$ (a homogeneous solution of the wave equation).

### 2.2 The Coulomb Gauge (Radiation Gauge)

$$\nabla\cdot\mathbf{A} = 0$$

In this gauge, substituting Gauss's law $\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ into $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$:

$$-\nabla^2\phi - \frac{\partial}{\partial t}(\nabla\cdot\mathbf{A}) = \frac{\rho}{\varepsilon_0} \quad\Longrightarrow\quad \nabla^2\phi = -\frac{\rho}{\varepsilon_0}$$

That is, $\phi$ takes the form of an electrostatic potential responding **instantaneously** to $\rho$ (this does not physically mean information travels faster than light — since $\phi$ itself is gauge-dependent and not directly observable, this poses no problem — the observable quantities $\mathbf{E},\mathbf{B}$ always propagate causally). This gauge is useful for the non-relativistic limit of quantum electrodynamics and for multipole expansions.

### 2.3 General Principle of Gauge Fixing

Key concept: the physical degrees of freedom (2 polarizations of the photon) are fewer than the 4 components of $A^\mu$. Because of gauge symmetry, there are 2 "spurious" degrees of freedom (1 gauge freedom + the constraint it induces), and fixing the gauge is the procedure of removing these spurious degrees of freedom to make calculation tractable. Whichever gauge is used, the **physical observables** ($\mathbf{E},\mathbf{B}$, and particle trajectories, etc.) must always come out the same — this is the practical meaning of the theory being "gauge invariant."

## Part 3. Gauge Symmetry and Charge Conservation — The Connection to Noether's Theorem

In classical electromagnetism, gauge symmetry looks like "extra mathematical freedom," but **once combined with quantum mechanics, this symmetry becomes the very origin of charge conservation.** Noether's theorem: continuous symmetry ↔ conserved quantity. Gauge symmetry (the localization of global phase symmetry, explained below) ↔ charge conservation. This connection is the key to the next section.

## Part 4. Modern Extension (1): Quantum Mechanics and Local U(1) Gauge Symmetry

### 4.1 Reframing the Question: Why Does Electromagnetic Interaction Exist?

This is the modern viewpoint of the gauge principle: the Schrödinger (or Dirac) equation for a free electron is invariant under a **global phase transformation** of the wavefunction

$$\psi(x) \to e^{i\alpha}\psi(x) \quad (\alpha = \text{constant})$$

(since only $|\psi|^2$ has physical meaning). Now let's require this symmetry to hold **locally** — i.e., let the phase $\alpha$ vary from point to point in spacetime:

$$\psi(x) \to e^{iq\alpha(x)/\hbar}\psi(x)$$

### 4.2 What Local Symmetry Forces: The Covariant Derivative

The problem: the Lagrangian (or Schrödinger equation) of a free particle contains a term $\partial_\mu\psi$, and

$$\partial_\mu\left(e^{iq\alpha(x)/\hbar}\psi\right) = e^{iq\alpha/\hbar}\left(\partial_\mu\psi + \frac{iq}{\hbar}(\partial_\mu\alpha)\psi\right)$$

leaves an extra term $\frac{iq}{\hbar}(\partial_\mu\alpha)\psi$, so the plain $\partial_\mu\psi$ is not invariant under local phase transformations. To cancel this, we must introduce a new field $A_\mu$ and define the **covariant derivative**:

$$D_\mu \equiv \partial_\mu - \frac{iq}{\hbar}A_\mu$$

and require $A_\mu$ to transform as:

$$A_\mu \to A_\mu + \partial_\mu\alpha$$

(This is exactly the gauge transformation of Part 1!) One can then show that $D_\mu\psi$ as a whole transforms as simply as $\psi$ itself:

$$D_\mu\psi \to e^{iq\alpha/\hbar}D_\mu\psi$$

**Conclusion**: To allow the wavefunction's phase to vary freely from point to point in spacetime (to demand local gauge symmetry), the existence of the electromagnetic vector potential $A_\mu$ is **mathematically forced**. That is, the modern reinterpretation is that electromagnetic interaction is not "a force that just happens to exist," but **something that necessarily emerges in order to maintain local phase symmetry.** This is precisely why Maxwell's equations are called a "gauge theory" in physics, and specifically a $U(1)$ gauge theory (since the set of phase transformations $e^{i\alpha}$ forms the group $U(1)$).

### 4.3 The Aharonov–Bohm Effect: The Physical Reality of $A^\mu$

Classically, one might think that in a region where $\mathbf{E}=\mathbf{B}=0$ but $\mathbf{A}\neq0$, "there is no physical effect at all" — but in quantum mechanics, $\mathbf{A}$ directly affects the phase of the wavefunction:

$$\psi \to \psi\, \exp\left(\frac{iq}{\hbar}\int \mathbf{A}\cdot d\boldsymbol{\ell}\right)$$

If electrons are sent along two paths around a solenoid (where the magnetic field is confined inside, with $\mathbf{B}=0$ outside but $\mathbf{A}\neq0$) and made to interfere, the interference pattern shifts even though the paths passed through a region with $\mathbf{B}=0$ — this has been experimentally confirmed (Aharonov-Bohm, 1959; experiments by Tonomura and others in the 1980s). This shows that $A^\mu$ is not merely a computational convenience but carries **real, topologically meaningful physical information** (though only the gauge-invariant quantity $\oint\mathbf{A}\cdot d\boldsymbol{\ell}$ — the flux enclosed by $\mathbf{A}$ — is actually observable, and this particular line integral is itself gauge invariant).

## Part 5. Modern Extension (2): Non-Abelian Gauge Theory (Yang–Mills)

### 5.1 From U(1) to SU(N)

The gauge group of electromagnetism is $U(1)$ — a single phase $e^{i\alpha}$ whose multiplication is **commutative (abelian)**: $e^{i\alpha}e^{i\beta}=e^{i\beta}e^{i\alpha}$. In 1954, Yang and Mills generalized this to **non-abelian** groups — groups whose elements do not commute under multiplication (e.g., $SU(2)$, $SU(3)$).

An $SU(N)$ gauge transformation:
$$\psi \to U(x)\psi, \qquad U(x) = e^{ig\,\theta^a(x)T^a}$$

where $T^a$ are the group's generators, $a=1,\ldots,N^2-1$ (e.g., $SU(3)$ has 8 generators — corresponding to the 8 gluons of the strong interaction). The covariant derivative is:

$$D_\mu = \partial_\mu - igA_\mu^a T^a$$

### 5.2 The Key Difference: Self-Interaction of the Field Tensor

For U(1), $F_{\mu\nu}=\partial_\mu A_\nu - \partial_\nu A_\mu$ is the whole story, but in the non-abelian case, since the commutator of generators $[T^a,T^b]=if^{abc}T^c$ is nonzero, an additional term appears:

$$F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc}A_\mu^b A_\nu^c$$

This extra term $gf^{abc}A_\mu^bA_\nu^c$ causes the **gauge bosons themselves to interact with each other** — this is the reason gluons interact with one another (the root of key phenomena such as asymptotic freedom in the strong interaction and color confinement), a decisive difference from the fact that photons do not interact with each other (electromagnetism is linear).

### 5.3 Position within the Standard Model

| Gauge group | Mediating particle | Corresponding force |
|---|---|---|
| $U(1)_{EM}$ | Photon | Electromagnetic force (Maxwell's equations themselves) |
| $SU(2)_L\times U(1)_Y$ | $W^\pm, Z^0$, photon | Electroweak unified theory (Weinberg-Salam) |
| $SU(3)_C$ | 8 gluons | Strong interaction (quantum chromodynamics, QCD) |

That is, Maxwell's idea "gauge symmetry → the existence of a force" was extended into the design principle of the entire Standard Model. Maxwell's equations correspond to the **simplest ($U(1)$) special case** in this lineage.

## Part 6. Modern Extension (3): The Final Compression via Differential Forms

The most modern and geometric description: writing $A^\mu$ as the 1-form $A = A_\mu dx^\mu$, and $F^{\mu\nu}$ as its exterior derivative $F=dA$. The gauge transformation is:

$$A \to A + d\lambda$$

and

$$F=dA \to d(A+d\lambda) = dA + d(d\lambda) = dA = F$$

(the fundamental property $d^2\equiv0$ of the exterior derivative — this is the coordinate-independent version of the "commutativity of partial derivatives" proven in Part 1.2.) The homogeneous equation (the Bianchi identity) is simply $dF=0$, and the inhomogeneous equation is written $d\star F = \mu_0 J$ (where $\star$ is the Hodge dual operator). This language is entirely coordinate-independent and connects directly to the concept of curvature, forming a structure exactly parallel to the Riemann curvature tensor of general relativity — the modern differential-geometric viewpoint is that **the gauge field is geometrically a "connection," and $F^{\mu\nu}$ is its "curvature."**

## 7.7 Overall Summary

| Stage | Content |
|---|---|
| Classical gauge symmetry | $A^\mu\to A^\mu+\partial^\mu\lambda$, $F^{\mu\nu}$ invariant (derived from the commutativity of partial derivatives) |
| Gauge fixing | Lorenz gauge ($\partial_\mu A^\mu=0$), Coulomb gauge ($\nabla\cdot\mathbf{A}=0$), etc. |
| Quantum mechanical reinterpretation | Requiring local $U(1)$ phase symmetry ⇒ the existence of $A_\mu$ is forced (the gauge principle) |
| Experimental confirmation | The Aharonov–Bohm effect — proves the topological reality of $A^\mu$ |
| Non-abelian extension | Yang–Mills theory — $SU(N)$, self-interacting gauge bosons, the foundation of the Standard Model |
| Geometric completion | $A=$ connection, $F=dA=$ curvature — unified via differential forms and fiber bundle theory |

The gauge symmetry of Maxwell's equations may at first look like "an extra degree of freedom in the calculation," but over the course of the 20th century it was revealed to be **the fundamental principle underlying all elementary interactions (electromagnetism, the weak force, the strong force).** The idea that "requiring gauge symmetry necessarily gives rise to a force" grew — starting from Maxwell's introduction of the simple mathematical trick $\nabla\times\mathbf{A}$ — into the core principle supporting the entire Standard Model of modern particle physics.

---

## Overall Summary: Maxwell's Equations as a Single Story

1. The **differential and integral forms** are proven fully equivalent via the Divergence Theorem, Stokes' Theorem, and the "arbitrary region" argument.
2. The **displacement current** is a term **mathematically required by necessity** to resolve the contradiction between charge conservation and the original Ampère's law.
3. Combining the completed four equations in vacuum produces the **wave equation**, whose speed **exactly matches the independently measured speed of light**, leading to the conclusion "light = electromagnetic wave."
4. $\nabla\cdot\mathbf{B}=0$ is the most compressed expression of the **absence of magnetic monopoles**.
5. The four equations were originally derived from the static experimental laws of **Coulomb's law and the Biot–Savart law**, via the Divergence Theorem, Stokes' Theorem, and the delta-function identity.
6. Translated into the language of special relativity, the four equations compress into **two tensor equations** ($\partial_\mu F^{\mu\nu}=\mu_0J^\nu$ and the Bianchi identity), with charge conservation built in automatically.
7. The **gauge symmetry** underlying this structure is, classically, merely a computational degree of freedom, but once combined with quantum mechanics it is reinterpreted as the principle (the gauge principle) that forces the very existence of electromagnetic interaction — and this idea extends, through Yang–Mills theory, into the design principle of the entire modern Standard Model.
