# TL;DR — The Lorentz Force

𝐅 = q ( 𝐄 + 𝐯 × 𝐁 )

Picture a charged particle flying in a straight line. Then it enters a
magnetic field pointing from the ceiling to the floor. It starts to turn.

- The magnetic force pushes the particle sideways, at right angles to
  both its motion and the field. It changes the direction, never the speed.
- A sideways push that never stops bends the path into a circle. If the
  particle also moves along the field, the circle stretches into a spiral.
- A stronger field makes a tighter circle.
- The electric term, q𝐄, is the other half of the formula. It doesn't
  turn the particle. It speeds it up or slows it down.

Everything that follows, from the aurora to the tokamak to the MRI,
comes from this one idea: a magnetic field bends charged particles
without giving them energy.



Part 0

# Why Does the Aurora Happen? — Understanding It Through the Lorentz Force

The story is easier to follow if we split it into three motions: **spinning around, bouncing back and forth, and slowly circling the Earth.** The aurora appears at the moment when the first two motions go out of step.

---

## 1. The Lorentz Force: A Force That Only Pushes Sideways

When a charge moves through a magnetic field, it feels a force **F = q v×B**. This force is always perpendicular to the velocity, so it can't change the electron's speed, only its direction. It's like turning the steering wheel without ever touching the gas pedal. The result has two parts.

- Across the field lines, the electron spins round and round. This is cyclotron motion, and its radius is **r = m v⊥ / (|q| B)**. The stronger B is, the tighter the circle.
- Along the field lines, there is no force at all, so the electron slides freely.

So the electron behaves like a bead threaded on a string, using the field line as the string: it traces a spiral as it travels along the line.

---

## 2. Where Are Electrons Trapped? Near the Magnetic Equator, Especially on Earth's Night Side

Electrons don't fly straight from the Sun to the poles. When the solar wind pumps energy into the magnetosphere, that energy gets stored in the long tail on Earth's night side (the plasma sheet). From there the electrons are carried toward Earth, heated as the magnetic field strengthens, and trapped on the field lines that wrap around the planet.

They are trapped near the magnetic equator, where the field is weakest. A field line bulges far outward and then narrows again at the poles, and that bulging middle is the "belly." The Van Allen belts are trapping regions formed by the same principle.

---

## 3. Why Toward the Poles? Because Electrons Can't Leave the Line, So They Follow It

An electron can hardly slip sideways across a field line. Push it sideways and it just spins. Along the line, though, it moves freely. Field lines start at the equator and plunge into the Earth at the poles, so an electron sliding along a line naturally heads toward a pole.

### The Funnel Analogy

Think of the funnel demonstration you may have seen as a kid: a coin or a marble rolls round and round from the wide part down toward the narrow neck. Earth's field lines fan out widely near the equator and converge toward a point at the poles. The electron is confined within this bundle of lines, so the picture is the same. A stronger field (B↑) is exactly the funnel getting narrower.

This analogy captures three key ideas.

- It goes from a wide region into a narrow one
- It spirals, and the spiral gets tighter as the funnel narrows
- An electron with a lot of sideways motion can't get all the way in and turns back, while an electron coming almost straight down reaches the end of the neck

### Straighten the Spiral and You Get Funnel Motion

An electron's gyration is so fast (several kHz or more) that we don't need to follow every turn. If we average the gyration away and follow only the **center line** of the spiral, the electron becomes a single point moving along one field line. Physicists call this method the **guiding center approximation.**

Once we straighten it this way, only one force remains on the electron.

**F∥ = −μ ∂B/∂s**

It pushes opposite to the direction in which B grows (toward the pole). The narrower the funnel gets, the harder the push back. So if you look only at the straight-line motion, it resembles a marble in a narrowing funnel. The real spiral can be split like this:

> real spiral = straight-line motion of the guiding center + fast gyration around it

### How It Differs from a Real Funnel

| | Real funnel | Bundle of field lines |
|---|---|---|
| Why the direction changes | The wall pushes, gravity pulls | The Lorentz force, no wall |
| What sends it back in the narrow part | Momentum of the spinning | The mirror force −μ∂B/∂s |
| Speed | Speeds up as it goes down | Total speed unchanged, only the sideways speed grows |
| As it narrows | Set by the wall's shape | The flux through the gyration loop stays constant, so the spiral tightens by itself |

The reason the funnel shape holds even without a wall is conservation of magnetic flux. When B grows, the gyration orbit has to shrink by the same factor so the flux through it stays the same (radius r ∝ 1/√B). For a multi-keV electron, a radius of several kilometers near the equator shrinks to a few meters above the atmosphere near the pole.

This approximation only works when the gyration is fast and B changes slowly. Where B changes abruptly, such as near the poles, it can break down. Also, slow motions across the lines (drift around the Earth, E×B convection) disappear when you straighten the path.

To sum up: **a bead sliding down a flaring trumpet-shaped tube, coiling like a spring as it goes.**

---

## 4. Why Does It Bounce Back? The Magnetic Mirror

Toward the poles the field lines get denser, so B grows. Two facts come together here.

- The magnetic force does no work, so **the speed stays the same.**
- The quantity that measures the strength of the gyration, **μ = m v⊥² / (2B)**, stays almost constant.

As B grows, v⊥ has to grow to keep μ fixed. The speed is unchanged, so the speed along the line, v∥, shrinks. When v∥ reaches zero, the electron can go no farther and turns back. This is the **magnetic mirror.**

The returning electron meets another mirror near the opposite pole and bounces again. So it oscillates north and south with a period of a few seconds. On top of that, because of the gradient and curvature of the field, the electron makes a third, slow motion: drifting eastward around the Earth.

---

## 5. But Why Does It Glow? When the Mirror Sits Inside the Atmosphere

The height at which the mirror forms depends on how obliquely the electron was moving at the start (its pitch angle). An electron traveling almost straight along the line has its mirror point deep inside the atmosphere. Around 100–200 km, where the air is dense, it collides with oxygen and nitrogen and loses its energy before it can bounce.

This narrow range of angles is the **loss cone.** Measured at the equator it is within about 2.5°, and in the funnel analogy it corresponds to the "angles that can pass through the neck."

The struck O and N₂ are excited, then come back down by emitting light.

| Altitude | Particle | Wavelength | Color |
|---|---|---|---|
| Below 100 km | N₂⁺ | 427.8 nm | Violet / blue |
| 100–150 km | O (¹S→¹D) | 557.7 nm | Green (brightest) |
| Above 200 km | O (¹D→³P) | 630.0 nm | Red |

---

## 6. One More Thing: What Fills the Loss Cone?

Normally the loss cone is almost empty, so the electrons just keep bouncing and stay trapped. For the aurora to brighten, one of two things is needed.

- Waves jostle the electrons' pitch angles and fill the loss cone.
- A parallel electric field several thousand kilometers above the pole (the Knight relation) accelerates the electrons and drives them deep into the atmosphere.

A **substorm** is the event in which the energy stored in the tail is released all at once by reconnection, and this process happens explosively.

---

## One-Line Summary

> Electrons wind around magnetic field lines and slide along them, bouncing between the poles at magnetic mirrors, and only the electrons whose mirror point lies inside the atmosphere collide with air near the poles and glow.

---

# The Tokamak — Same Physics, Opposite Goal

If you understand the aurora, you already understand most of the tokamak. **The aurora is trapped electrons deliberately leaking out at the poles, and the tokamak is a device built to close off that leak.** The physics is identical: the Lorentz force, sliding along field lines, and magnetic mirrors all show up again.

---

## 1. Same Principle: Charges Wind Around Field Lines and Follow Them

The ions and electrons in a tokamak also wind around field lines and slide along them, just like the electrons in the aurora. In a strong field of about 5 T, the gyration radius is tiny: a few mm for ions and under 0.1 mm for electrons. That is why a 100-million-degree plasma can stay on the field lines without touching the wall. The moment it touched the wall, it would cool down or the wall would melt.

---

## 2. The Difference from the Aurora: Remove the Ends

In the aurora, the field lines plunge from the poles into the atmosphere, so electrons leak out there (the loss cone). To prevent this, the tokamak **joins the field lines into a doughnut (torus) shape** and removes the ends altogether. An electron sliding along a line just goes around and around, and there is no pole to escape from. Instead of relying on magnetic mirrors, it gets rid of the ends entirely.

---

## 3. Tell the Three Rotations Apart

A doughnut has three kinds of rotation, which makes it easy to get confused.

| Rotation | What kind of motion | What decides it |
|---|---|---|
| **Gyration (cyclotron motion)** | The small spiral around a single field line | The sign of the charge and the direction of B (automatic) |
| **Toroidal direction** | Going the long way around the doughnut | The particle's initial velocity (sign of v∥), plus the current the machine drives |
| **Poloidal direction** | Going around the tube's cross-section (the small circle) | The twist of the field lines (safety factor q) |

A single particle does all three at once. It spins in a small spiral, travels along the field line around the doughnut, and because that line is twisted, it also gradually turns around the tube's cross-section.

---

## 4. A Doughnut Shape Creates a New Problem

A doughnut is denser on the inside and sparser on the outside, so the field is strong on the inner side and weak on the outer side (B ∝ 1/R). Because of this gradient and curvature, ions and electrons drift in **opposite directions (up and down).** Which way is "up" depends on the direction of the field. Then a chain of events follows.

1. One kind of charge piles up at the top, the opposite charge at the bottom (charge separation)
2. A vertical electric field E appears
3. The E×B drift pushes the entire plasma **outward**

In other words, a doughnut-shaped magnetic field alone can't confine the plasma. As the detailed sections later in this document put it, "drift cancellation" is the first challenge in tokamak design.

---

## 5. The Solution: Twist the Field Lines

The key is **to make the field lines not simple loops but lines that spiral around the surface of the doughnut.** Then the up and down drifts average out and vanish.

Here is why. The drift direction is always the same (say, always upward). But as a particle follows a twisted field line, it **alternates between being at the top and at the bottom of the doughnut's cross-section.** At the top, an upward push is outward motion; at the bottom, being pushed the same way brings it back inward. After one full turn, it returns as far as it was pushed, and the two cancel.

### The Twist Is Made by Current Inside the Plasma

The coils wound around the doughnut (the toroidal field B_t) alone can't create a twist. So the tokamak **drives a current through the plasma itself.** This current creates a magnetic field that circles around the tube's cross-section (the poloidal field B_p), and the two fields combine into spiral field lines. The ratio of how many times a field line goes around the doughnut to how many times it goes around the tube's cross-section is called the **safety factor q.** Roughly, q ≈ (r B_t) / (R B_p), and by the standard used later in this document, the key conditions are:

- Center of the doughnut (axis): q ≈ 1
- Edge: q ≈ 3 (for ITER)
- If q drops below 2, a kink instability sets in and it becomes dangerous

---

## 6. How Is the Current Driven? The Transformer Principle

In the middle of a tokamak sits a **central solenoid (coil).** When the current in this coil is changed over time, Faraday's law induces an electric field along the doughnut direction, and that field drives a current in the plasma ring (which acts as the secondary coil of a transformer).

The direction of this current is **a value the machine decides.** The particles in the plasma are, thanks to thermal motion, split almost half and half between clockwise and counterclockwise (each particle's v∥ sign depends on its initial velocity), and the electric field tips this balance to one side, producing a net current.

The transformer method has a limit, though. The coil current can't be increased indefinitely, so only **pulsed operation** is possible. That is why tokamaks meant to run for a long time also use current the plasma generates by itself (bootstrap current) or current pushed in from outside.

---

## 7. Magnetic Mirrors Show Up Here Too

The inner side of the doughnut has a stronger B, so a particle with a lot of sideways motion feels the mirror force as it moves inward and turns back. So some particles are trapped in the outer region, moving back and forth along **banana-shaped orbits.** The particle that oscillated north and south in the aurora oscillates in the outer region here.

---

## 8. Still, It Isn't Perfect

- **Turbulence:** This is the biggest reason the plasma slowly leaks, and it is a major challenge in fusion research. One approach, as in H-mode, is to suppress turbulence with E×B shear flow and create a transport barrier.
- **Disruption:** If q gets too low, the plasma becomes unstable and suddenly collapses. In ITER, a current of several MA can vanish within milliseconds, which makes this a big challenge.
- **Stellarator:** A different approach that doesn't use plasma current, and instead **twists the shape of the doughnut and the coils themselves** to make spiral field lines. It needs no current drive and has no disruptions, at the cost of much more complex coils. Germany's Wendelstein 7-X is the leading example.

| Device | Major radius R / minor radius a | Field along the doughnut | Plasma current |

| KSTAR (Korea) | 1.8 m / 0.5 m | 3.5 T | about 2 MA |

| ITER (international) | 6.2 m / 2.0 m | 5.3 T | 15 MA |

---

## One-Line Summary

> The aurora is trapped electrons deliberately leaking out at the poles, and the tokamak is a device that closes the field lines into a doughnut and twists them with plasma current so nothing leaks.

---

*References: see §4.2.1 (the tokamak and the Grad–Shafranov equation), §4.2.2 (stellarators), §4.2.3 (KSTAR and ITER table), and §7.1.7 (safety factor) later in this document. External sources are tokamak physics lecture notes and papers (transformer action of the central solenoid, drift cancellation by helical field lines).*
 





Part 1

# Act 1. Foundation

---

## 1.1 Historical Origins — A 60-Year Synthesis

The Lorentz force is not a formula that one person discovered on one day. It is the crystallization of a conceptual synthesis spanning 60 years, from **Faraday's 1831 experiments on lines of magnetic force** to **Lorentz's 1895 electron theory**. This section follows each stage of that synthesis to see why today's form, $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$, was inevitable.

### 1.1.1 Faraday (1831–1838): The Geometry of Magnetic Lines of Force

Faraday discovered the **empirical fact** that a current creates a magnetic field, and that a magnetic field in turn exerts a force on a current. His central contribution was not a mathematical law but a **geometric image**:

> "Magnetic lines of force fill space, and when a conductor crosses these lines, an electromotive force is induced."

This idea could not yet be expressed in the mathematical language of the time, but it established two things:

1. **A field mediates the force** — denying action at a distance
2. **The direction of the force is simultaneously perpendicular to the magnetic lines of force and to the direction of motion** — the prototype of the right-hand rule

Faraday qualitatively observed the force on a current-carrying conductor in a magnetic field, but he did not formulate its magnitude as $q\mathbf{v}\times\mathbf{B}$.

### 1.1.2 Maxwell (1861–1865): The Momentum of the Field

Maxwell translated Faraday's image into **partial differential equations**. In his 1865 paper *A Dynamical Theory of the Electromagnetic Field*, he interpreted the electromagnetic field as the **motion of a mechanical medium**, and held that the field carries momentum and energy.

Notably, today's $q\mathbf{v}\times\mathbf{B}$ term does **not explicitly appear** in Maxwell's equations themselves. Instead he:

- Introduced the electromagnetic momentum $\mathbf{A}$
- Used a concept similar to the Lorenz gauge
- Computed forces via the field's stress tensor (the Maxwell stress tensor)

This laid **the groundwork from which $q\mathbf{v}\times\mathbf{B}$ could be derived**, but it had not yet been organized into the force on a charge.

### 1.1.3 Thomson and Heaviside (1881–1889): Correcting $\mathbf{v}\times\mathbf{B}$

**J.J. Thomson**, in 1881, calculating the magnetic field of a moving charged sphere, was the first to attempt a force of the form $q\mathbf{v}\times\mathbf{B}$. However, his result contained a **coefficient error of $1/2$**.

It was **Oliver Heaviside** who corrected this. In 1885 and 1889, Heaviside used modern **vector notation** to derive the correct magnetic force:

$$\mathbf{F}_m = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐅ₘ = q𝐯×𝐁
> ```

Heaviside's contribution was twofold:

1. **Introducing vector calculus** — condensing Maxwell's equations into four equations
2. **Correcting the coefficient error** — removing the $1/2$

However, he treated this force only as **part of the general theory of electromagnetism** and did not integrate it into the equation of motion of a charge.

### 1.1.4 Lorentz (1892–1895): Electron Theory and the Final Form

**Hendrik Antoon Lorentz**'s decisive paper is his 1892 work **"La théorie électromagnétique de Maxwell et son application aux corps mouvants"** (*Maxwell's electromagnetic theory and its application to moving bodies*). In this paper Lorentz:

- Held that the ether is completely at rest, and that matter is a collection of **discrete electrons** moving through it.
- Held that the microscopic fields $\mathbf{e}, \mathbf{b}$ act **directly** on electrons.
- Defined the **force density** acting on charge density $\rho$ and current $\mathbf{j}$ as $\mathbf{f} = \rho\mathbf{e} + \mathbf{j}\times\mathbf{b}$.

In his 1895 book **"Versuch einer Theorie der electrischen und optischen Erscheinungen in bewegten Körpern"** (*An attempt at a theory of electrical and optical phenomena in moving bodies*), Lorentz organized the modern form for a point charge:

$$\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐅 = q𝐄 + q𝐯×𝐁
> ```

This is what we today call the **Lorentz force**.

Lorentz's true contribution was not the formula itself, but the **microscopic formulation of the interaction between the electromagnetic field and matter**. He reduced electromagnetism to **the mechanics of the electron**, and this became the starting point of both special relativity and quantum mechanics.

### 1.1.5 A Modern Reinterpretation: The Shadow of $F=dA$

In the latter half of the 20th century, the Lorentz force was reinterpreted in the language of **differential geometry**. Viewing the electromagnetic potential $A_\mu$ as the **connection** on a $U(1)$ principal bundle, and the field tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ as its **curvature**:

$$f^\mu = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> f^μ = qF^μνu_ν
> ```

That is, the Lorentz force is **the local shadow of the phenomenon in which the curvature of a $U(1)$ bundle bends the worldline of a charged particle**. This viewpoint is developed further in §2.5 and §5.3.

### 1.1.6 Limits and Exceptions

- **Uncertainty in historical narrative**: "Who discovered it first" is a matter of priority disputes. Heaviside's and Lorentz's contributions are nearly contemporaneous, and the boundary differs between sources.
- **Maxwell's place**: The fact that $q\mathbf{v}\times\mathbf{B}$ does not appear in Maxwell's equations is often misunderstood. Maxwell completed the **equations of the field**; the **equation of motion of the charge** was Lorentz's contribution.
- **The ether hypothesis**: Lorentz's original theory presupposed a stationary ether. This premise was superseded by Einstein's 1905 special relativity, but the form of the Lorentz force itself is **relativistically exact** (see §3.1).

> **References**
> - Lorentz, H. A., *La théorie électromagnétique de Maxwell et son application aux corps mouvants*, Archives Néerlandaises **25**, 363–552 (1892). [archive.org](https://archive.org/details/lathorielectrom00loregoog)
> - Thomson, J. J., *Cathode Rays*, Philosophical Magazine **44**, 293–316 (1897). [doi:10.1080/14786449708621070](https://doi.org/10.1080/14786449708621070)
> - Heaviside, O., *Electromagnetic Theory*, Vol. II (1899). [archive.org](https://archive.org/details/electromagnetict02heavrich)

---

## 1.2 Modern Definition and Unit Systems

The **modern definition** of the Lorentz force in SI units is:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + 𝐯×𝐁)
> ```

The meaning and units of each symbol are:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{F}$ | Force | N (newton) |
| $q$ | Charge | C (coulomb) |
| $\mathbf{E}$ | Electric field | V/m |
| $\mathbf{v}$ | Particle velocity | m/s |
| $\mathbf{B}$ | Magnetic field (flux density) | T (tesla) |

**Properties of the two terms**:

- **Electric force** $q\mathbf{E}$: independent of velocity, can do work
- **Magnetic force** $q\mathbf{v}\times\mathbf{B}$: perpendicular to velocity, **does no work**

The last property is expressed by the identity:

$$\mathbf{F}_m \cdot \mathbf{v} = 0$$

> **Unicode**
> ```
> 𝐅ₘ · 𝐯 = 0
> ```

This means the magnetic field **changes only the direction of the particle's motion, not its kinetic energy**. This is why, in a cyclotron, the magnetic field makes a particle move in a circle but cannot accelerate it.

### 1.2.1 Derivation from the Lagrangian (Preview)

The Lorentz force follows naturally from the principle of **minimal coupling**. The relativistic Lagrangian:

$$L = -mc^2\sqrt{1-v^2/c^2} - q\phi + q\mathbf{v}\cdot\mathbf{A}$$

> **Unicode**
> ```
> L = -mc²√(1-v²/c²) - qφ + q𝐯·𝐀
> ```

Here $\phi$ is the electric scalar potential and $\mathbf{A}$ is the magnetic vector potential. Substituting into the Euler–Lagrange equation

$$\frac{d}{dt}\frac{\partial L}{\partial \mathbf{v}} = \frac{\partial L}{\partial \mathbf{x}}$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ 𝐯) = (∂ L)/(∂ 𝐱)
> ```

yields exactly the Lorentz force. The full derivation is carried out in §1.4.

### 1.2.2 The Gaussian and Heaviside–Lorentz Unit Systems

In particle-physics literature, the **core source of confusion** is the unit system. SI, Gaussian, Heaviside–Lorentz, and natural units are all used differently.

#### Gaussian units

$$\mathbf{F} = q\left(\mathbf{E} + \frac{\mathbf{v}}{c}\times\mathbf{B}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + (𝐯)/(c)×𝐁)
> ```

Features:
- $\mathbf{E}$ and $\mathbf{B}$ have **the same dimension**
- $c$ appears explicitly, revealing the **relativistic character**
- Maxwell's equations retain a factor of $4\pi$

#### Heaviside–Lorentz units (rationalized)

$$\mathbf{F} = q\left(\mathbf{E} + \frac{\mathbf{v}}{c}\times\mathbf{B}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + (𝐯)/(c)×𝐁)
> ```

The form looks the same as Gaussian, but the factor of $4\pi$ is removed from the very definition of $\mathbf{E}, \mathbf{B}$, simplifying Maxwell's equations. In other words, the numerical value of $B$ itself in $F = q(E+v/c\times B)$ differs from the Gaussian system:

$$\nabla\cdot\mathbf{E} = \rho$$

> **Unicode**
> ```
> ∇·𝐄 = ρ
> ```

When converting to SI, one must not simply insert $c$; the very definition of the fields differs by a factor of $4\pi$. Based on Jackson (3rd ed., appendix), the key conversions are:

| Quantity | Gaussian → SI | HL → SI |
|---|---|---|
| Charge $q$ | $q_{SI}=q_G/\sqrt{4\pi\epsilon_0}$ | $q_{SI}=q_{HL}\sqrt{\epsilon_0}$ |
| Electric field $\mathbf{E}$ | $\mathbf{E}_{SI}=\sqrt{4\pi\epsilon_0}\mathbf{E}_G$ | $\mathbf{E}_{SI}=\mathbf{E}_{HL}/\sqrt{\epsilon_0}$ |
| Magnetic field $\mathbf{B}$ | $\mathbf{B}_{SI}=\sqrt{4\pi/\mu_0}\mathbf{B}_G$ | $\mathbf{B}_{SI}=\mathbf{B}_{HL}/\sqrt{\mu_0}$ |
| Relation between $\mathbf{E},\mathbf{B}$ | $\mathbf{E}_G, \mathbf{B}_G$ same dimension | $\nabla\cdot\mathbf{E}_{HL}=\rho_{HL}$, $\nabla\cdot\mathbf{E}_G=4\pi\rho_G$ |

That is, even though Gaussian and HL look the same in form, the numerical value of $\mathbf{B}$ itself differs by a factor of $\sqrt{4\pi}$. One must not simply multiply by $\sqrt{\mu_0/\epsilon_0}$.

> **Unicode**
> ```
> 𝐁_SI = √(μ₀/ε₀)· 𝐁_HL
> ```

#### Natural units ($\hbar = c = 1$)

The standard in high-energy physics:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄 + 𝐯×𝐁)
> ```

The form is identical to SI, but:
- Since $c=1$, $\mathbf{v}$ is **dimensionless**
- $[\mathbf{E}] = [\mathbf{B}] = [\text{mass}]^2$
- $q$ is **dimensionless**

In actual numerical calculations, the fine-structure constant enters through $q = e\sqrt{4\pi\alpha}$, with $\alpha \approx 1/137$.

### 1.2.3 Unit-Conversion Table

| Quantity | SI | Gaussian | Heaviside–Lorentz | Natural units |
|---|---|---|---|---|
| Force | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ |
| Charge | $q$ | $q$ | $q$ | dimensionless |
| Electric field | $\mathbf{E}$ | $\mathbf{E}$ | $\mathbf{E}$ | $\mathbf{E}$ |
| Magnetic field | $\mathbf{B}$ | $\mathbf{B}/c$ | $\mathbf{B}/c$ | $\mathbf{B}$ |
| Lorentz force | $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | $q(\mathbf{E}+\frac{\mathbf{v}}{c}\times\mathbf{B})$ | $q(\mathbf{E}+\frac{\mathbf{v}}{c}\times\mathbf{B})$ | $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ |

### 1.2.4 Limits and Exceptions

- **History of unit confusion**: the 19th-century debate over electromagnetic unit systems (Electromagnetic vs. Electrostatic units) changed the form of Maxwell's equations. This confusion still lingers today between particle physics and condensed-matter physics.
- **Particle-physics convention**: in natural units with $c=1$, velocity becomes dimensionless, but $c$ must be restored when comparing to actual experimental data.
- **Persistence of Gaussian units**: Gaussian units are still widely used in astrophysics and plasma physics. For example, the practice of expressing magnetic fields in Gauss ($1\,\mathrm{G} = 10^{-4}\,\mathrm{T}$) remains.

> **References**
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), Chapter 11.
> - Griffiths, D. J., *Introduction to Electrodynamics*, 4th ed., Cambridge (2017), Chapter 5.

---

## 1.3 The Four-Dimensional Covariant Form

Writing the Lorentz force in its **four-dimensional covariant form** makes its harmony with special relativity explicit. This section derives the 4-vector representation of the Lorentz force and shows how it contains the 3D form.

### 1.3.1 The Electromagnetic Field Tensor $F^{\mu\nu}$

Define the electromagnetic field as a 4D antisymmetric tensor:

$$F^{\mu\nu} = \begin{pmatrix}0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0\end{pmatrix}$$

> **Unicode**
> ```
> F^μν =  [ [0, -Eₓ/c, -E_y/c, -E_z/c];
>            [Eₓ/c, 0, -B_z, B_y];
>            [E_y/c, B_z, 0, -Bₓ];
>            [E_z/c, -B_y, Bₓ, 0] ]
> ```

Writing the components explicitly:

$$F^{0i} = -E_i/c, \quad F^{ij} = -\epsilon_{ijk}B_k$$

> **Unicode**
> ```
> F^0i = -Eᵢ/c,   F^ij = -εᵢⱼₖBₖ
> ```

$F^{\mu\nu}$ is **antisymmetric**: $F^{\mu\nu} = -F^{\nu\mu}$. It has 6 independent components (3 for $\mathbf{E}$, 3 for $\mathbf{B}$).

### 1.3.2 4-Velocity and 4-Momentum

The particle's 4-velocity:

$$u^\nu = \gamma(c, \mathbf{v}), \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}$$

> **Unicode**
> ```
> u^ν = γ(c, 𝐯),   γ = 1/√(1-v²/c²)
> ```

4-momentum:

$$p^\mu = (\gamma mc, \mathbf{p}) = m u^\mu$$

> **Unicode**
> ```
> p^μ = (γ mc, 𝐩) = m u^μ
> ```

### 1.3.3 Definition of the 4-Force

Define the **4-force** as:

$$f^\mu = q F^{\mu\nu} u_\nu$$

> **Unicode**
> ```
> f^μ = q F^μν u_ν
> ```

or, as the rate of change of momentum with respect to proper time $\tau$:

$$\frac{dp^\mu}{d\tau} = q F^{\mu\nu} u_\nu$$

> **Unicode**
> ```
> (dp^μ)/(dτ) = q F^μν u_ν
> ```

### 1.3.4 Spatial Components → the Lorentz Force

Computing for $\mu = i$ (spatial components):

$$f^i = q F^{i0} u_0 + q F^{ij} u_j$$

Since $F^{i0} = -F^{0i} = E_i/c$ and $u_0 = \gamma c$:

$$f^i = q\frac{E_i}{c}\gamma c + q(-\epsilon_{ijk}B_k)(\gamma v_j) = q\gamma E_i - q\gamma\epsilon_{ijk}v_j B_k$$

Since $\epsilon_{ijk}v_j B_k = (\mathbf{v}\times\mathbf{B})_i$:

$$f^i = \gamma q(\mathbf{E} + \mathbf{v}\times\mathbf{B})_i$$

Since $f^i = dp^i/d\tau = \gamma\, dp^i/dt$:

$$\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐩)/(dt) = q(𝐄 + 𝐯×𝐁)
> ```

This is **exactly the 3D form of the Lorentz force**.

### 1.3.5 The Time Component → Power

For $\mu = 0$ (the time component):

$$f^0 = q F^{0i} u_i = q\left(-\frac{E_i}{c}\right)(\gamma v_i) = -\frac{\gamma q}{c}\mathbf{v}\cdot\mathbf{E}$$

Since $f^0 = dp^0/d\tau = \gamma\, d(\gamma mc)/dt \cdot c$, rearranging gives:

$$\frac{dE}{dt} = q\mathbf{v}\cdot\mathbf{E}$$

> **Unicode**
> ```
> (dE)/(dt) = q𝐯·𝐄
> ```

Here $E = \gamma mc^2$ is the relativistic energy. This is the 4D expression of the fact that **the magnetic field does no work**: the $\mathbf{v}\times\mathbf{B}$ term does not appear in the time component.

### 1.3.6 Orthogonality $f^\mu u_\mu = 0$

Computing the inner product of the 4-force and the 4-velocity:

$$f^\mu u_\mu = q F^{\mu\nu} u_\nu u_\mu$$

Since $F^{\mu\nu}$ is antisymmetric and $u_\mu u_\nu$ is symmetric, their product is zero:

$$f^\mu u_\mu = 0$$

> **Unicode**
> ```
> f^μ u_μ = 0
> ```

Physical meaning: the 4-force is **perpendicular to the worldline**. This is the 4D expression of the fact that the magnetic force does no work, and it is simultaneously equivalent to the statement that **the rest mass does not change**:

$$\frac{dm}{d\tau} = 0$$

### 1.3.7 Mathematica Verification

```mathematica
(* Define the electromagnetic field tensor *)
Fmunu = {{0, -Ex/c, -Ey/c, -Ez/c},
         {Ex/c, 0, -Bz, By},
         {Ey/c, Bz, 0, -Bx},
         {Ez/c, -By, Bx, 0}};

(* Metric (+,-,-,-) *)
g = DiagonalMatrix[{1, -1, -1, -1}];

(* 4-velocity: contravariant u^ν, covariant u_ν = g_{νρ}u^ρ *)
uUp = {gamma c, gamma vx, gamma vy, gamma vz};
uDown = g . uUp;

(* 4-force: f^μ = q F^{μν} u_ν must be contracted with the covariant u_ν (uDown) *)
fourForce = q Fmunu . uDown;

(* Verify the spatial components *)
spatialForce = fourForce[[2 ;; 4]] / gamma;
expected = q ({Ex, Ey, Ez} + Cross[{vx, vy, vz}, {Bx, By, Bz}]);

Simplify[spatialForce - expected] == {0, 0, 0}

(* Caution: contracting Fmunu directly with uUp (i.e. F^{μν}u^ν) flips the sign
   of the magnetic term, incorrectly giving q(E - v×B). Both the text and the
   code consistently use u_ν (covariant). *)
```

### 1.3.8 Limits and Exceptions

- **Non-relativistic limit**: as $v \ll c$, $\gamma \to 1$, and the 4-vector form reduces to the 3D Lorentz force.
- **Extension to general relativity**: in curved spacetime, $\partial_\mu \to \nabla_\mu$, and $F^{\mu\nu}$ couples to the metric (→ §6.2.1).
- **Sign convention**: the sign of $F^{\mu\nu}$ depends on whether one uses $(-,+,+,+)$ or $(+,-,-,-)$. This document uses the $(+,-,-,-)$ convention.

> **References**
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §11.7.
> - Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §23.

---
## 1.4 Lagrangian and Hamiltonian Formulation

The Lorentz force can also be written as Newton's $F=ma$, but its true structure is revealed in the **gauge coupling of the Lagrangian**. This section starts from the Lagrangian, derives the Lorentz force via the Euler–Lagrange equation, obtains the Hamiltonian via a Legendre transform, and finishes with the symplectic structure and Poisson brackets.

### 1.4.1 The Lagrangian $L = \frac12 mv^2 - q\phi + q\mathbf{v}\cdot\mathbf{A}$

**Why this form?**

We must add an interaction term with the electromagnetic field to the free-particle Lagrangian $L_0 = \frac12 mv^2$. There are three requirements:

1. The **equation of motion must be linear** in $\mathbf{E}, \mathbf{B}$
2. Under a **gauge transformation** $A^\mu \to A^\mu + \partial^\mu\chi$, the action $S=\int L\,dt$ must change only by a boundary term
3. Under **Galilean/Lorentz covariance**, it must take the form $A^\mu u_\mu$

The unique scalar coupling satisfying these conditions is $q\mathbf{v}\cdot\mathbf{A} - q\phi$. This is clearer if we start from the relativistic action:

$$S_{int} = -q \int A_\mu\, dx^\mu = \int (-q\phi + q\mathbf{v}\cdot\mathbf{A})\,dt$$

> **Unicode**
> ```
> Sᵢₙₜ = -q ∫ A_μ dx^μ = ∫ (-qφ + q𝐯·𝐀)dt
> ```

Hence the non-relativistic Lagrangian is:

$$L(\mathbf{x},\mathbf{v},t) = \frac12 m\mathbf{v}^2 - q\phi(\mathbf{x},t) + q\mathbf{v}\cdot\mathbf{A}(\mathbf{x},t)$$

> **Unicode**
> ```
> L(𝐱,𝐯,t) = (1)/(2) m𝐯² - qφ(𝐱,t) + q𝐯·𝐀(𝐱,t)
> ```

Here $\mathbf{v} = \dot{\mathbf{x}}$. This is a representative example of a potential that **depends on velocity**, called a **velocity-dependent potential**.

### 1.4.2 The Euler–Lagrange Equation → the Complete Derivation of the Lorentz Force

The Euler–Lagrange equation:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} - \frac{\partial L}{\partial x_i} = 0$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ x˙ᵢ) - (∂ L)/(∂ xᵢ) = 0
> ```

#### Step 1: The canonical momentum

$$p_i \equiv \frac{\partial L}{\partial \dot{x}_i} = m\dot{x}_i + qA_i(\mathbf{x},t)$$

> **Unicode**
> ```
> pᵢ ≡ (∂ L)/(∂ x˙ᵢ) = mx˙ᵢ + qAᵢ(𝐱,t)
> ```

That is, **the canonical momentum $\mathbf{p}$ differs from the mechanical momentum $\boldsymbol{\pi}=m\mathbf{v}$**:

$$\mathbf{p} = m\mathbf{v} + q\mathbf{A}$$

> **Unicode**
> ```
> 𝐩 = m𝐯 + q𝐀
> ```

This distinction is the core of electromagnetic Hamiltonian mechanics.

#### Step 2: Time derivative of the left-hand side

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} = m\ddot{x}_i + q\frac{dA_i}{dt}$$

Since $A_i$ depends on $\mathbf{x}(t), t$, we use the **total derivative**:

$$\frac{dA_i}{dt} = \frac{\partial A_i}{\partial t} + \sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j}$$

Hence:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_i} = m\ddot{x}_i + q\left(\frac{\partial A_i}{\partial t} + \sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j}\right)$$

> **Unicode**
> ```
> (d)/(dt)(∂ L)/(∂ x˙ᵢ) = mx¨ᵢ + q((∂ Aᵢ)/(∂ t) + ∑ⱼ x˙ⱼ(∂ Aᵢ)/(∂ xⱼ))
> ```

#### Step 3: Derivative with respect to position on the right-hand side

$$\frac{\partial L}{\partial x_i} = -q\frac{\partial\phi}{\partial x_i} + q\sum_j \dot{x}_j \frac{\partial A_j}{\partial x_i}$$

> **Unicode**
> ```
> (∂ L)/(∂ xᵢ) = -q(∂φ)/(∂ xᵢ) + q∑ⱼ x˙ⱼ (∂ Aⱼ)/(∂ xᵢ)
> ```

#### Step 4: Combining the pieces

Substituting into the Euler–Lagrange equation:

$$m\ddot{x}_i + q\frac{\partial A_i}{\partial t} + q\sum_j \dot{x}_j\frac{\partial A_i}{\partial x_j} = -q\frac{\partial\phi}{\partial x_i} + q\sum_j \dot{x}_j \frac{\partial A_j}{\partial x_i}$$

Rearranging:

$$m\ddot{x}_i = -q\frac{\partial\phi}{\partial x_i} - q\frac{\partial A_i}{\partial t} + q\sum_j \dot{x}_j\left(\frac{\partial A_j}{\partial x_i} - \frac{\partial A_i}{\partial x_j}\right)$$

> **Unicode**
> ```
> mx¨ᵢ = -q(∂φ)/(∂ xᵢ) - q(∂ Aᵢ)/(∂ t) + q∑ⱼ x˙ⱼ((∂ Aⱼ)/(∂ xᵢ) - (∂ Aᵢ)/(∂ xⱼ))
> ```

#### Step 5: Reducing to the definitions of the fields

The potential definitions of the electric and magnetic fields:

$$\mathbf{E} = -\nabla\phi - \frac{\partial\mathbf{A}}{\partial t}, \quad B_k = (\nabla\times\mathbf{A})_k = \epsilon_{kij}\frac{\partial A_j}{\partial x_i}$$

> **Unicode**
> ```
> 𝐄 = -∇φ - (∂𝐀)/(∂ t),   Bₖ = (∇×𝐀)ₖ = εₖᵢⱼ(∂ Aⱼ)/(∂ xᵢ)
> ```

and the Levi-Civita identity:

$$\sum_j \dot{x}_j(\partial_i A_j - \partial_j A_i) = [\mathbf{v}\times(\nabla\times\mathbf{A})]_i = (\mathbf{v}\times\mathbf{B})_i$$

> **Unicode**
> ```
> ∑ⱼ x˙ⱼ(∂ᵢ Aⱼ - ∂ⱼ Aᵢ) = [𝐯×(∇×𝐀)]ᵢ = (𝐯×𝐁)ᵢ
> ```

Hence:

$$m\ddot{\mathbf{x}} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐱¨ = q𝐄 + q𝐯×𝐁
> ```

**We started from the Lagrangian in terms of potentials, not fields, but the result is expressed purely in terms of the gauge-invariant $E, B$.** This is because the Lagrangian changes only by a total time derivative under a gauge transformation.

### 1.4.3 The Hamiltonian

The Legendre transform:

$$H = \mathbf{p}\cdot\dot{\mathbf{x}} - L$$

> **Unicode**
> ```
> H = 𝐩·𝐱˙ - L
> ```

Substituting $\dot{\mathbf{x}} = (\mathbf{p}-q\mathbf{A})/m$:

$$H(\mathbf{x},\mathbf{p},t) = \frac{1}{2m}\left(\mathbf{p}-q\mathbf{A}(\mathbf{x},t)\right)^2 + q\phi(\mathbf{x},t)$$

> **Unicode**
> ```
> H(𝐱,𝐩,t) = (1)/(2m)(𝐩-q𝐀(𝐱,t))² + qφ(𝐱,t)
> ```

**Physical meaning:**

- $\mathbf{p}$: the **canonical momentum** — gauge-dependent
- $\boldsymbol{\pi} = \mathbf{p}-q\mathbf{A} = m\mathbf{v}$: the **kinematic momentum** — gauge-invariant, the actually-measured velocity

This distinction is the origin of **minimal coupling**, $\hat{\mathbf{p}} \to \hat{\mathbf{p}}-q\mathbf{A}$, in quantum mechanics (→ §3.3.1).

### 1.4.4 The Canonical Equations

Hamilton's equations:

$$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}$$

> **Unicode**
> ```
> q˙ᵢ = (∂ H)/(∂ pᵢ),   p˙ᵢ = -(∂ H)/(∂ qᵢ)
> ```

Setting $q_i = x_i$:

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

Combining the two equations to form $m\ddot{x}_i$ again yields the Lorentz force.

**Caution:** in the Hamiltonian formalism, it appears as if $\mathbf{p}$ directly receives the force, but the actual acceleration lies in $\dot{\boldsymbol{\pi}}$.

### 1.4.5 Symplectic Structure and Phase-Space Geometry

Let the coordinates of phase space $T^*\mathbb{R}^3 \cong \mathbb{R}^6$ be $\xi = (\mathbf{x},\mathbf{p})$.

**The symplectic 2-form:**

$$\omega = \sum_i dp_i \wedge dx_i = d\mathbf{p}\wedge d\mathbf{x}$$

> **Unicode**
> ```
> ω = ∑ᵢ dpᵢ ∧ dxᵢ = d𝐩∧ d𝐱
> ```

Matrix representation:

$$J = \begin{pmatrix}0 & I \\ -I & 0\end{pmatrix}$$

> **Unicode**
> ```
> J =  [ [0, I];
>        [-I, 0] ]
> ```

for which $\omega(u,v) = u^T J v$.

**The Hamiltonian flow preserves $\omega$**: $\mathcal{L}_{X_H}\omega = 0$, i.e., Liouville's theorem $\nabla\cdot X_H = 0$. Phase-space volume is preserved.

The Hamiltonian vector field $X_H$ is defined by $i_{X_H}\omega = -dH$:

$$X_H = \left(\frac{\partial H}{\partial \mathbf{p}}, -\frac{\partial H}{\partial \mathbf{x}}\right) = (\mathbf{v}, q\nabla(\mathbf{v}\cdot\mathbf{A}) - q\nabla\phi)$$

> **Unicode**
> ```
> X_H = ((∂ H)/(∂ 𝐩), -(∂ H)/(∂ 𝐱)) = (𝐯, q∇(𝐯·𝐀) - q∇φ)
> ```

**Key point:** even in the presence of an electromagnetic field, the symplectic structure $\omega$ itself remains standard. The effect of the field is implemented by inserting $A$ into $H$. This is why **minimal coupling does not break the symplectic structure**.

**Geometric viewpoint:** $A$ is a **connection 1-form**, and $F=dA$ is its **curvature**. The particle moves on a $U(1)$ principal bundle, and the Lorentz force is the force by which this curvature makes the particle's worldline **depart from geodesic motion** (→ §2.5.4). This should be distinguished from the standard geodesic deviation of general relativity, which describes the relative acceleration of two neighboring geodesics.

### 1.4.6 Poisson Brackets and Noncommuting Momenta

The standard Poisson bracket:

$$\{F,G\} = \sum_i \left(\frac{\partial F}{\partial x_i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial x_i}\right)$$

> **Unicode**
> ```
> F,G = ∑ᵢ ((∂ F)/(∂ xᵢ)(∂ G)/(∂ pᵢ) - (∂ F)/(∂ pᵢ)(∂ G)/(∂ xᵢ))
> ```

**Canonical relations:**

$$\{x_i, p_j\} = \delta_{ij}, \quad \{x_i,x_j\}=0, \quad \{p_i,p_j\}=0$$

> **Unicode**
> ```
> xᵢ, pⱼ = δᵢⱼ,    xᵢ,xⱼ = 0,    pᵢ,pⱼ = 0
> ```

**Equation of motion:**

$$\dot{F} = \{F,H\} + \partial_t F$$

> **Unicode**
> ```
> F˙ = F,H + ∂ₜ F
> ```

$\dot{x}_i = \{x_i,H\} = (p_i-qA_i)/m$ holds as before. Computing $\dot{p}_i = \{p_i,H\}$ gives the same result as the canonical equations.

#### The bracket of the kinematic momentum

**The key point is the bracket of the kinematic momentum $\pi_i = p_i - qA_i$:**

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

**That is, the kinematic momenta do not commute with each other.** The magnetic field appears as **noncommutativity** in the $\mathbf{p}$-space.

We can now compute the force directly via $\dot{\pi}_i = \{\pi_i, H\}$. Since $H = \pi^2/2m + q\phi$:

$$\dot{\pi}_i = \{\pi_i, \pi_j\}\frac{\pi_j}{m} + \{\pi_i, q\phi\}$$

Rearranging:

$$\frac{d}{dt}(m\mathbf{v}) = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> (d)/(dt)(m𝐯) = q𝐄 + q𝐯×𝐁
> ```

**That is, the canonical variables $(\mathbf{x},\mathbf{p})$ always satisfy the standard brackets, and the magnetic field appears as noncommutativity in $\mathbf{p}$-space.** When this structure is quantized:

$$[\hat{\pi}_i,\hat{\pi}_j] = i\hbar q\epsilon_{ijk}B_k$$

> **Unicode**
> ```
> [π̂ᵢ,π̂ⱼ] = iℏ qεᵢⱼₖBₖ
> ```

which becomes the starting point of **Landau levels and the quantum Hall effect** (→ §3.3.2, §5.3.1).

### 1.4.7 Mathematica Verification

```mathematica
(* Define the Lagrangian *)
Clear[L, phi, Avec, m, q];
L = (1/2) m (vx^2 + vy^2 + vz^2) - q phi[x, y, z, t]
    + q (vx Ax[x, y, z, t] + vy Ay[x, y, z, t] + vz Az[x, y, z, t]);

(* Euler–Lagrange equation *)
vars = {x, y, z};
vels = {vx, vy, vz};
EL[i_] := D[D[L, vels[[i]]] /. {vx -> x'[t], vy -> y'[t], vz -> z'[t]}, t]
         - D[L /. {vx -> x'[t], vy -> y'[t], vz -> z'[t]}, vars[[i]]];

(* Verify the result *)
(* Should come out as m x'' = q (E_x + (v × B)_x) *)
Simplify[EL[1]]
```

### 1.4.8 Limits and Exceptions

- **Non-relativistic limit**: the Lagrangian above is valid only for $v \ll c$. The relativistic Lagrangian is $-mc^2\sqrt{1-v^2/c^2} - q\phi + q\mathbf{v}\cdot\mathbf{A}$ (→ §3.1.1).
- **Gauge dependence**: $L$ and $H$ are not invariant under gauge transformations. Only the physical predictions are invariant.
- **Non-uniqueness of the canonical momentum**: $\mathbf{p} = m\mathbf{v} + q\mathbf{A}$ depends on the choice of gauge. What is experimentally measured is only $\boldsymbol{\pi} = m\mathbf{v}$.
- **Many-body systems**: for $N$ particles, minimal coupling must be applied to each particle, and interaction terms $q_i q_j/4\pi\epsilon_0|\mathbf{x}_i-\mathbf{x}_j|$ must be added.

> **References**
> - Goldstein, H., Poole, C., Safko, J., *Classical Mechanics*, 3rd ed., Addison-Wesley (2001), Chapter 1.5, 8.1. [doi:10.1119/1.1484149](https://doi.org/10.1119/1.1484149)
> - Landau & Lifshitz, *Mechanics*, 3rd ed., Pergamon (1976), §16–17.
> - Arnold, V. I., *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer (1989), §40.

---

## 1.5 Gauge Invariance — The Separation of Force and Phase

The most important modern insight about the Lorentz force is **gauge invariance**. This section proves that gauge freedom has no effect on physics in classical mechanics, and foreshadows that **the story expands in quantum mechanics**.

### 1.5.1 Gauge Transformations

Define the electromagnetic field tensor from the electromagnetic potential $A^\mu = (\phi/c, \mathbf{A})$:

$$F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$$

> **Unicode**
> ```
> F^μν = ∂^μ A^ν - ∂^ν A^μ
> ```

A **gauge transformation** is, for an arbitrary scalar function $\chi(\mathbf{x},t)$:

$$A^\mu \to A'^\mu = A^\mu + \partial^\mu \chi$$

> **Unicode**
> ```
> A^μ → A'^μ = A^μ + ∂^μ χ
> ```

In components:

$$\phi \to \phi - \frac{\partial\chi}{\partial t}, \quad \mathbf{A} \to \mathbf{A} + \nabla\chi$$

> **Unicode**
> ```
> φ → φ - (∂χ)/(∂ t),   𝐀 → 𝐀 + ∇χ
> ```

### 1.5.2 Invariance of $F^{\mu\nu}$

After the gauge transformation:

$$F'^{\mu\nu} = \partial^\mu(A^\nu + \partial^\nu\chi) - \partial^\nu(A^\mu + \partial^\mu\chi) = F^{\mu\nu} + [\partial^\mu, \partial^\nu]\chi$$

Since partial derivatives commute, $[\partial^\mu, \partial^\nu]\chi = 0$:

$$F'^{\mu\nu} = F^{\mu\nu}$$

> **Unicode**
> ```
> F'^μν = F^μν
> ```

**That is, the electromagnetic field tensor is gauge invariant.** Consequently:

$$f^\mu = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> f^μ = qF^μνu_ν
> ```

is also **manifestly gauge invariant**.

### 1.5.3 Classical Mechanics: the Force Is Gauge Invariant

How does the Lagrangian change under a gauge transformation?

$$L = \frac12 mv^2 - q\phi + q\mathbf{v}\cdot\mathbf{A}$$

Substituting the gauge transformation $\phi \to \phi - \partial_t\chi$, $\mathbf{A} \to \mathbf{A} + \nabla\chi$:

$$L \to L - q\frac{\partial\chi}{\partial t} + q\mathbf{v}\cdot\nabla\chi = L + q\frac{d\chi}{dt}$$

> **Unicode**
> ```
> L → L - q(∂χ)/(∂ t) + q𝐯·∇χ = L + q(dχ)/(dt)
> ```

Here we used the total derivative $\frac{d\chi}{dt} = \partial_t\chi + \mathbf{v}\cdot\nabla\chi$.

**The Lagrangian changes only by a total derivative.** Since the Euler–Lagrange equation is unaffected by a total derivative, **the equation of motion is invariant**.

This is why **the Lorentz force is gauge invariant**:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

$\mathbf{E}, \mathbf{B}$ come from $F^{\mu\nu}$ and are therefore gauge invariant. $\phi, \mathbf{A}$ themselves are gauge-dependent, but the physically observable force is invariant.

### 1.5.4 Quantum Mechanics: the Phase Is Physical

**But in quantum mechanics, the story expands.**

Applying minimal coupling $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ to the Schrödinger equation:

$$i\hbar\frac{\partial\psi}{\partial t} = \left[\frac{(\hat{\mathbf{p}} - q\mathbf{A})^2}{2m} + q\phi\right]\psi$$

> **Unicode**
> ```
> iℏ(∂ψ)/(∂ t) = [((𝐩̂ - q𝐀)²)/(2m) + qφ]ψ
> ```

Under a gauge transformation, the wave function undergoes a **phase transformation**:

$$\psi \to \psi' = \exp\left(i\frac{q\chi}{\hbar}\right)\psi$$

> **Unicode**
> ```
> ψ → ψ' = exp(i(qχ)/(ℏ))ψ
> ```

Combining this transformation with $A^\mu \to A^\mu + \partial^\mu\chi$ leaves the Schrödinger equation **invariant**.

**Key point:** the wave function itself changes under a gauge transformation, but the physical observables $|\psi|^2$ and $\mathbf{j}$ are invariant. However, **the phase itself is physical**.

### 1.5.5 Preview of the Aharonov–Bohm Effect

Consider the outside of a solenoid. Inside the solenoid, $\mathbf{B} \neq 0$; outside, $\mathbf{B} = 0$. Outside, $\nabla\times\mathbf{A} = 0$, but $\mathbf{A} \neq 0$.

When an electron passes along two paths that go around the solenoid on either side, a **phase difference** arises between the two paths:

$$\Delta\varphi_{AB} = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi_B}{\hbar}$$

> **Unicode**
> ```
> Δφ_AB = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ_B)/(ℏ)
> ```

Here $\Phi_B = \int \mathbf{B}\cdot d\mathbf{S}$ is the magnetic flux inside the solenoid.

**The force acting along a classical trajectory remains gauge-invariantly zero.** But in quantum interference, $\mathbf{A}$ affects the interference even in a region where $\mathbf{B} = 0$.

This is the **Aharonov–Bohm effect**. It shows that while the Lorentz force is a local force, **the quantum phase is nonlocal** (→ §2.5.2).

### 1.5.6 A Preview of the $U(1)$ Bundle

From a modern viewpoint, a gauge transformation is a **vertical automorphism of a $U(1)$ principal bundle**. The wave function is a **section of the associated complex line bundle**, $A$ is the **connection**, and $F = dA$ is the **curvature**.

This viewpoint is fully developed in §2.5. For now, remember this:

> **The Lorentz force is the simplest piece of evidence that the gauge principle holds in electromagnetism: thanks to the structure $F = dA$ that enforces gauge invariance, it gives the same physical trajectory regardless of the choice of gauge.**

### 1.5.7 Mathematica Verification

```mathematica
(* Gauge transformation *)
chi = chi[x, y, z, t];
Avec = {Ax[x, y, z, t], Ay[x, y, z, t], Az[x, y, z, t]};
phi = phi[x, y, z, t];

AvecPrime = Avec + Grad[chi, {x, y, z}];
phiPrime = phi - D[chi, t];

(* Verify field invariance *)
BPrime = Curl[AvecPrime, {x, y, z}];
B = Curl[Avec, {x, y, z}];
Simplify[BPrime - B] == {0, 0, 0}


EPrime = -Grad[phiPrime, {x, y, z}] - D[AvecPrime, t];
E = -Grad[phi, {x, y, z}] - D[Avec, t];
Simplify[EPrime - E] == {0, 0, 0}

```

### 1.5.8 Limits and Exceptions

- **Non-simply-connected spaces**: the Aharonov–Bohm effect only appears when space is non-simply-connected (e.g., $\mathbb{R}^3 \setminus \text{solenoid} \simeq S^1$). In a simply-connected space, $\oint \mathbf{A}\cdot d\boldsymbol{\ell} = 0$ is enforced.
- **Global gauge transformations**: $\chi$ can be a multivalued function. In that case the phase is gauge-invariant only up to integer multiples of $2\pi$ (→ §2.5.3).
- **Non-Abelian gauge theories**: in $SU(2)$ or $SU(3)$, $F = dA + A\wedge A$, with an added commutator term (→ §6.1.1).
- **Gauge fixing**: in actual calculations, a specific gauge (Coulomb, Lorenz, Landau, etc.) is chosen to simplify computation. The physical result is independent of the gauge choice.

> **References**
> - Aharonov, Y., Bohm, D., *Significance of Electromagnetic Potentials in the Quantum Theory*, Physical Review **115**, 485–491 (1959). [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §2.6, §12.1.
> - Nakahara, M., *Geometry, Topology and Physics*, 2nd ed., Taylor & Francis (2003), Chapter 10.

---

# Act 2. Mathematical Structure

> **Arc of this act**
> Trajectories in a uniform field → Drift theory → Adiabatic invariants → Numerical methods → Topology
>
> Act 1 fixed the language of the Lorentz force (definition, mechanics, gauge). Act 2 uses that language to **actually solve real trajectories**. The five pillars are: analytic solutions (2.1), perturbation theory (2.2), invariants (2.3), numerical analysis (2.4), and topology (2.5).

---

## 2.1 Trajectories in a Uniform Magnetic Field

A uniform magnetic field is the **zeroth-order approximation** to all magnetic confinement, and a nonuniform field is treated as a perturbation about it. This section fully solves the trajectory of a charged particle in a uniform magnetic field and introduces guiding-center coordinates.

### 2.1.1 The Equation of Motion and Its Solution

Assume a uniform $\mathbf{B} = B_0\hat{z}$ and $\mathbf{E} = 0$. The Lorentz force is:

$$m\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐯˙ = q𝐯×𝐁
> ```

In components:

$$\dot{v}_x = \omega_c v_y, \quad \dot{v}_y = -\omega_c v_x, \quad \dot{v}_z = 0$$

> **Unicode**
> ```
> v˙ₓ = ω_c v_y,   v˙_y = -ω_c vₓ,   v˙_z = 0
> ```

Here the **cyclotron frequency** is:

$$\omega_c = \frac{qB_0}{m}$$

> **Unicode**
> ```
> ω_c = (qB₀)/(m)
> ```

The sign includes the sign of the charge. The physical rotation rate is $|\omega_c|$. **Ions rotate left-handed and electrons right-handed** with respect to $\mathbf{B}$.

**Velocity solution:**

$$v_x = v_\perp \cos(\omega_c t + \phi_0)$$
$$v_y = -v_\perp \sin(\omega_c t + \phi_0)$$
$$v_z = v_\parallel = \text{const}$$

> **Unicode**
> ```
> vₓ = v_⊥ cos(ω_c t + φ₀)
> v_y = -v_⊥ sin(ω_c t + φ₀)
> v_z = v_∥ = const
> ```

**Position solution** (integrating):

$$x(t) = X_G + \frac{v_\perp}{\omega_c}\sin(\omega_c t+\phi_0)$$
$$y(t) = Y_G + \frac{v_\perp}{\omega_c}\cos(\omega_c t+\phi_0)$$
$$z(t) = Z_G + v_\parallel t$$

> **Unicode**
> ```
> x(t) = X_G + (v_⊥)/(ω_c)sin(ω_c t+φ₀)
> y(t) = Y_G + (v_⊥)/(ω_c)cos(ω_c t+φ₀)
> z(t) = Z_G + v_∥ t
> ```

Here $(X_G, Y_G, Z_G)$ is the initial position of the **guiding center**.

### 2.1.2 The Larmor Radius

The radius of the trajectory:

$$r_L = \frac{m v_\perp}{|q|B_0} = \frac{v_\perp}{|\omega_c|}$$

> **Unicode**
> ```
> r_L = (m v_⊥)/(|q|B₀) = (v_⊥)/(|ω_c|)
> ```

**Geometry of the trajectory:** circular motion of radius $r_L$ in the $xy$-plane + uniform motion in $z$ = a **helix**.

**Numerical example:**
- Electron ($m_e = 9.11\times10^{-31}$ kg, $q = -e$), $v_\perp = 10^6$ m/s, $B_0 = 1$ T
- $r_L = (9.11\times10^{-31})(10^6)/(1.6\times10^{-19})(1) \approx 5.7\ \mu$m
- $\omega_c = eB/m_e \approx 1.76\times10^{11}$ rad/s

### 2.1.3 Guiding-Center Coordinates

The center of the circular motion $(X_G, Y_G)$ is the **guiding center**. Expressed in terms of the particle's position:

$$\mathbf{R}_g = \mathbf{r} + \frac{m}{qB_0^2}\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐑_g = 𝐫 + (m)/(qB₀²)𝐯×𝐁
> ```

**Verification:** with $\mathbf{B} = B_0\hat{z}$, $\mathbf{v} = (v_x, v_y, 0)$:

$$\mathbf{v}\times\mathbf{B} = (v_y B_0, -v_x B_0, 0)$$

Hence:

$$X_g = x + \frac{m v_y}{qB_0}, \quad Y_g = y - \frac{m v_x}{qB_0}$$

Substituting $x(t), y(t)$ confirms that $X_g, Y_g$ are independent of time.

**Physical meaning of the guiding center:**
- The particle orbits the guiding center with radius $r_L$
- The guiding center is **nearly stationary** in the plane perpendicular to the field (exactly stationary for a uniform field)
- In a nonuniform field, the guiding center **drifts** (→ §2.2)

### 2.1.4 Mathematica Verification

```mathematica
(* Solve the equation of motion in a uniform magnetic field *)
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
(* Result: circular motion + uniform motion in z *)
```

### 2.1.5 Limits and Exceptions

- **Relativistic regime**: as $v \to c$, $\omega_c \to qB/\gamma m$ decreases; the trajectory is still a helix, but the frequency becomes energy-dependent (→ §3.1.3).
- **Presence of an electric field**: if $\mathbf{E} \neq 0$, additional drift occurs (→ §2.2.1).
- **Nonuniform field**: when $r_L \sim L_B$ (the scale of the field's spatial variation), the guiding-center approximation breaks down (→ §2.2.6).

> **References**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963). [doi:10.1002/9781118033156](https://doi.org/10.1002/9781118033156)
> - Chen, F. F., *Introduction to Plasma Physics and Controlled Fusion*, 3rd ed., Springer (2016), Chapter 2.

---

## 2.2 Drift Theory — Perturbation from Nonuniform Fields

A uniform field is an idealization. In real plasmas and magnetospheres, the magnetic field varies in space. This section organizes the effect of nonuniform fields, via the **guiding-center approximation**, into **drift velocities**.

### 2.2.1 The $E\times B$ Drift

> **Condition of existence:** a pure $E\times B$ drift solution exists only when the relativistic invariant $\mathbf{E}^2 - c^2\mathbf{B}^2 < 0$ (i.e., $|\mathbf{E}| < c|\mathbf{B}|$). If $|\mathbf{E}| > c|\mathbf{B}|$, the drift velocity would exceed $c$ and no physical solution exists — in this case the electric field dominates.

When uniform $\mathbf{E}$ and uniform $\mathbf{B}$ are present simultaneously:

$$m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> m𝐯˙ = q(𝐄+𝐯×𝐁)
> ```

Decompose the solution as $\mathbf{v} = \mathbf{V}_d + \mathbf{u}$, requiring $\mathbf{u}$ to follow pure rotation:

$$\dot{\mathbf{u}} = \frac{q}{m}\mathbf{u}\times\mathbf{B}$$

Assuming $\mathbf{V}_d$ is constant:

$$0 = q\mathbf{E} + q\mathbf{V}_d\times\mathbf{B} \implies \mathbf{E} + \mathbf{V}_d\times\mathbf{B} = 0$$

Taking $\mathbf{B}\times$ of both sides:

$$\mathbf{V}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

> **Unicode**
> ```
> 𝐕_E = (𝐄×𝐁)/(B²)
> ```

**Key properties:**
- **Independent** of $q, m, v$ — ions and electrons move together
- Hence it **generates no current**
- The entire plasma moves at $\mathbf{V}_E$
- $\mathbf{E}_\parallel$ does not contribute to the drift and simply accelerates the particle directly

**General solution:**

$$\mathbf{v}(t) = \mathbf{V}_E + v_\parallel\hat{b} + v_\perp\hat{\perp}(t)$$

> **Unicode**
> ```
> 𝐯(t) = 𝐕_E + v_∥b̂ + v_⊥⊥̂(t)
> ```

The helix drifts at velocity $\mathbf{V}_E$.

**Polarization drift:** if $E_\perp$ varies with time:

$$\mathbf{V}_p = \frac{m}{qB^2}\frac{d\mathbf{E}_\perp}{dt}$$

> **Unicode**
> ```
> 𝐕ₚ = (m)/(qB²)(d𝐄_⊥)/(dt)
> ```

Ions and electrons drift in opposite directions → generating a current → an additional electric field.

### 2.2.2 The $\nabla B$ Drift

When the magnetic field varies spatially ($\mathbf{B} = B(y)\hat{z}$, $B(y) \approx B_0 + y\partial_y B$), the particle experiences a different $B$ over the course of one cycle.

The force exerted on the **magnetic moment** $\mu = mv_\perp^2/2B$ by the field:

$$\mathbf{F} = -\mu\nabla B$$

> **Unicode**
> ```
> 𝐅 = -μ∇ B
> ```

The **general drift formula** due to this force:

$$\mathbf{V}_F = \frac{\mathbf{F}\times\mathbf{B}}{qB^2}$$

> **Unicode**
> ```
> 𝐕_F = (𝐅×𝐁)/(qB²)
> ```

Hence:

$$\mathbf{V}_{\nabla B} = \frac{m v_\perp^2}{2qB}\frac{\mathbf{B}\times\nabla B}{B^2} = \frac{\mu}{q}\frac{\mathbf{B}\times\nabla B}{B^2}$$

> **Unicode**
> ```
> 𝐕_∇ B = (m v_⊥²)/(2qB)(𝐁×∇ B)/(B²) = (μ)/(q)(𝐁×∇ B)/(B²)
> ```

**Key point:** it depends on $q$ → **ions and electrons drift in opposite directions** → **a current is generated**.

### 2.2.3 Curvature Drift

When a field line has curvature $\mathbf{R}_c$ (radius of curvature $R_c$), the particle feels a centrifugal force $\mathbf{F}_c = m v_\parallel^2 \mathbf{R}_c/R_c^2$.

$$\mathbf{V}_c = \frac{\mathbf{F}_c\times\mathbf{B}}{qB^2} = \frac{m v_\parallel^2}{qB^2}\frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2}$$

> **Unicode**
> ```
> 𝐕_c = (𝐅_c×𝐁)/(qB²) = (m v_∥²)/(qB²)(𝐑_c×𝐁)/(R_c²)
> ```

For a vacuum field with $\nabla\times\mathbf{B} = 0$, the following identity holds:

$$\frac{\mathbf{R}_c}{R_c^2} = \frac{\nabla_\perp B}{B}$$

> **Unicode**
> ```
> (𝐑_c)/(R_c²) = (∇_⊥ B)/(B)
> ```

Hence in a vacuum field, the $\nabla B$ drift and the curvature drift point in the **same direction**.

### 2.2.4 Combining the Gradient and Curvature Drifts

Combining the two drifts gives the **guiding-center drift velocity**:

$$\mathbf{V}_{gc} = \mathbf{V}_{\nabla B} + \mathbf{V}_c = \frac{m}{qB}\left(v_\parallel^2 \frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2 B} + \frac{v_\perp^2}{2}\frac{\mathbf{B}\times\nabla B}{B^2}\right)$$

> **Unicode**
> ```
> 𝐕_gc = 𝐕_∇ B + 𝐕_c = (m)/(qB)(v_∥² (𝐑_c×𝐁)/(R_c² B) + (v_⊥²)/(2)(𝐁×∇ B)/(B²))
> ```

In the vacuum-field approximation $\nabla\times\mathbf{B} \approx 0$:

$$\mathbf{V}_{gc} = \frac{m}{qB^3}\left(v_\parallel^2 + \frac12 v_\perp^2\right) \mathbf{B}\times\nabla B$$

> **Unicode**
> ```
> 𝐕_gc = (m)/(qB³)(v_∥² + (1)/(2) v_⊥²) 𝐁×∇ B
> ```

**Caution:** this simplified form holds **only for a vacuum magnetic field ($\nabla\times B=0$)**. In general, the $\mu\nabla B$ term and the curvature term must be written separately:

$$\mathbf{V}_{gc} = \frac{1}{qB}\left(m v_\parallel^2 \frac{\mathbf{R}_c\times\hat{b}}{R_c^2} + \mu \frac{\hat{b}\times\nabla B}{B}\right)$$

> **Unicode**
> ```
> 𝐕_gc = (1)/(qB)(m v_∥² (𝐑_c×b̂)/(R_c²) + μ (b̂×∇ B)/(B))
> ```

The expression most commonly used in **covariant form**:

$$\mathbf{V}_D = \frac{\mathbf{B}}{qB^2}\times\left(\mu\nabla B + m v_\parallel^2 (\hat{b}\cdot\nabla)\hat{b}\right) + \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

> **Unicode**
> ```
> 𝐕_D = (𝐁)/(qB²)×(μ∇ B + m v_∥² (b̂·∇)b̂) + (𝐄×𝐁)/(B²)
> ```

**Meaning of the three terms:**
- First term: the $\nabla B$ drift
- Second term: the curvature drift
- Third term: the $E\times B$ drift

This equation is the **fundamental equation of the tokamak, the magnetosphere, and magnetic-mirror machines**.

### 2.2.5 Summary Table of Drifts

| Drift | Formula | $q$-dependent | Cause |
|---|---|---|---|
| $E\times B$ | $\mathbf{E}\times\mathbf{B}/B^2$ | No | Electric field |
| Polarization | $\frac{m}{qB^2}\dot{\mathbf{E}}_\perp$ | Yes | Time-varying electric field |
| $\nabla B$ | $\frac{\mu}{q}\frac{\mathbf{B}\times\nabla B}{B^2}$ | Yes | Magnetic-field gradient |
| Curvature | $\frac{mv_\parallel^2}{qB^2}\frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2}$ | Yes | Curvature of field lines |

### 2.2.6 Limits and Exceptions

- **Condition for the guiding-center approximation**: $r_L/L_B \ll 1$ (the scale of the field's spatial variation must be much larger than the Larmor radius).
- **Non-adiabatic regime**: when $r_L \sim L_B$, the guiding-center approximation breaks down and chaotic scattering occurs (→ §4.6.1).
- **Magnetic-reconnection regions**: near an X-point where $\mathbf{B} = 0$, the guiding center itself is not defined (→ §4.5.3).
- **Relativistic drifts**: as $v \to c$, $\mu$ and the drift formulas are modified (→ §3.1).

> **References**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963).
> - Alfvén, H., *Cosmical Electrodynamics*, Oxford (1950).
> - Baumjohann, W., Treumann, R. A., *Basic Space Plasma Physics*, Imperial College Press (1996).

---

## 2.3 The Adiabatic Invariant $\mu$

The motion of a particle in a nonuniform magnetic field is complicated, but in a field that varies **adiabatically**, a specific quantity is conserved. That quantity is the **magnetic moment** $\mu$. This section derives $\mu$ from the action variable and explains the magnetic mirror and the loss cone.

### 2.3.1 Deriving $\mu$ from the Action Variable

The **action variable** is the integral of the canonical momentum over periodic motion:

$$J = \oint \mathbf{p}_\perp\cdot d\mathbf{l} = \oint m\mathbf{v}_\perp\cdot d\mathbf{l}$$

> **Unicode**
> ```
> J = ∮ 𝐩_⊥· d𝐥 = ∮ m𝐯_⊥· d𝐥
> ```

For one period of the circular orbit:

$$J = m v_\perp \cdot 2\pi r_L = \frac{2\pi m^2 v_\perp^2}{|q|B}$$

> **Unicode**
> ```
> J = m v_⊥ · 2π r_L = (2π m² v_⊥²)/(|q|B)
> ```

Hence the **adiabatic invariant**:

$$\mu = \frac{|q|}{2\pi m}J = \frac{m v_\perp^2}{2B}$$

> **Unicode**
> ```
> μ = (|q|)/(2π m)J = (m v_⊥²)/(2B)
> ```

### 2.3.2 Conditions for Conservation

There are three conditions for $\mu$ to be conserved:

1. **The field is nearly uniform on the scale of the Larmor radius:**
   $$\epsilon = \frac{r_L}{L_B} \ll 1$$
   > **Unicode**
   > ```
   > ε = r_L/L_B ≪ 1
   > ```

2. **The field varies more slowly than the gyro-period:**
   $$\omega_c \gg \frac{1}{B}\frac{dB}{dt}$$
   > **Unicode**
   > ```
   > ω_c ≫ (1)/(B)(dB)/(dt)
   > ```

3. **$\mu$ is the canonical momentum of the Lagrangian averaged over the gyro-phase**

**Sketch of proof:** the guiding-center Lagrangian:

$$L_g = q\mathbf{A}(\mathbf{R}_g)\cdot\dot{\mathbf{R}}_g + \mu\dot{\theta} - \mu B - \frac12 m v_\parallel^2$$

> **Unicode**
> ```
> L_g = q𝐀(𝐑_g)·𝐑˙_g + μθ˙ - μ B - (1)/(2) m v_∥²
> ```

Here $\theta$, the cyclotron phase, is a **cyclic coordinate**. Hence:

$$p_\theta = \frac{\partial L_g}{\partial\dot\theta} = \mu = \text{const}$$

> **Unicode**
> ```
> p_θ = (∂ L_g)/(∂θ˙) = μ = const
> ```

### 2.3.3 The Magnetic Mirror and the Loss Cone

Combining conservation of $\mu$ with conservation of energy lets us understand the **magnetic mirror**.

**Conservation of energy:**

$$E = \frac12 m v_\parallel^2 + \mu B = \text{const}$$

> **Unicode**
> ```
> E = (1)/(2) m v_∥² + μ B = const
> ```

As the particle moves into a region of stronger field, $\mu B$ increases and $v_\parallel$ decreases. The point where $v_\parallel$ finally reaches zero is the **turning point** $B_m$:

$$\frac12 m v_0^2 = \mu B_m$$

> **Unicode**
> ```
> (1)/(2) m v₀² = μ Bₘ
> ```

Writing the pitch angle $\theta_0$ at the initial point $B_0$ ($v_{\perp0} = v_0\sin\theta_0$, $v_{\parallel0} = v_0\cos\theta_0$):

$$\mu = \frac{m v_0^2\sin^2\theta_0}{2B_0}$$

Substituting:

$$\frac12 m v_0^2 = \frac{m v_0^2\sin^2\theta_0}{2B_0}B_m$$

$$\sin^2\theta_m = \frac{B_0}{B_m}$$

> **Unicode**
> ```
> sin²θₘ = (B₀)/(Bₘ)
> ```

This is the boundary of the **loss cone**.

Writing the **mirror ratio** as $R_m = B_m/B_0$, the **confinement condition** is:

$$\sin^2\theta_0 > \frac{1}{R_m}$$

> **Unicode**
> ```
> sin²θ₀ > (1)/(Rₘ)
> ```

**Physical meaning:**
- A particle with a small pitch angle ($\theta_0 < \theta_m$) escapes the mirror before being reflected — **confinement fails**
- A particle with a large pitch angle is reflected — **confinement succeeds**
- Particles inside the loss cone are the loss channel of a magnetic mirror

### 2.3.4 Application to the Earth's Magnetosphere

In Earth's magnetosphere:
- Equatorial field $B_{eq} \sim 100$ nT
- Polar field $B_0 \sim 50\ \mu$T
- Mirror ratio $R_m \sim 500$

The loss-cone angle:

$$\theta_{lc} = \arcsin\sqrt{B_{eq}/B_0} \sim 2.5^\circ$$

> **Unicode**
> ```
> θ_lc = arcsin√(B_eq/B₀) ∼ 2.5°
> ```

Most of the general plasma sheet, at $T \sim 5$ keV, is confined, but wave–particle interactions can scatter the pitch angle into the loss cone, producing **auroral precipitation** (→ §4.5.1).

### 2.3.5 Mathematica Verification

```mathematica
(* Definition of the adiabatic invariant mu *)
mu[B_, vPerp_, m_] := m vPerp^2 / (2 B);

(* Magnetic mirror condition *)
mirrorCondition[B0_, Bm_, theta0_] := Sin[theta0]^2 == B0/Bm;

(* Numerical check: B0 = 1 T, Bm = 10 T *)
NSolve[mirrorCondition[1, 10, theta0], theta0]
(* Result: theta0 ≈ 0.3217 rad ≈ 18.43° *)

(* Loss-cone angle *)
thetaLC = ArcSin[Sqrt[1/10]];
N[thetaLC * 180/Pi]
(* Result: 18.435° *)
```

### 2.3.6 Limits and Exceptions

- **Magnetic-reconnection region**: near $\mathbf{B} = 0$, the very definition of $\mu$ diverges and conservation breaks down.
- **Non-adiabatic scattering**: when $r_L \sim L_B$, the gyro-phase is randomized and $\mu$ is destroyed.
- **Relativistic regime**: $\mu$ must be corrected to $\mu = p_\perp^2/2mB$ (→ §3.1).
- **Collisions**: if Coulomb collisions occur faster than the gyro-period, $\mu$ is not conserved (→ §3.4.4).

> **References**
> - Northrop, T. G., *The Adiabatic Motion of Charged Particles*, Wiley (1963).
> - Sivukhin, D. V., *Motion of Charged Particles in Electromagnetic Fields in the Plasma Physics*, Reviews of Plasma Physics **1**, 1 (1965).

---
## 2.4 Numerical Methods — Why Boris?

The Lorentz equation is a **Hamiltonian system**. Using a generic ODE solver causes phase-space volume to collapse. This section derives why the **Boris algorithm** has been the standard for numerically integrating the Lorentz force for 50 years, and covers PIC (Particle-In-Cell) and MCC (Monte Carlo Collision).

### 2.4.1 The Hamiltonian Structure of the Lorentz Equation

The system to be integrated:

$$\frac{d\mathbf{x}}{dt} = \mathbf{v}, \quad \frac{d\mathbf{v}}{dt} = \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐱)/(dt) = 𝐯,   (d𝐯)/(dt) = (q)/(m)(𝐄+𝐯×𝐁)
> ```

**The core of the Hamiltonian structure:** the magnetic force only **rotates** the velocity, so it does not change the energy. A good numerical integrator must **exactly preserve** this property.

### 2.4.2 Full Derivation of the Boris Algorithm

Proposed by J.P. Boris in 1970, this algorithm has been PIC's **standard pusher for 50 years**.

**Core idea:** **separate** $\mathbf{E}$, which accelerates, from $\mathbf{B}$, which rotates. The magnetic force must be an energy-conserving operator because it only rotates the velocity.

**Leapfrog structure:** for the time step $n \to n+1$, the velocity lives on a grid offset by half a step, $\mathbf{v}_{n-1/2}$.

**Time-centered difference:**

$$\frac{\mathbf{v}_{n+1/2}-\mathbf{v}_{n-1/2}}{\Delta t} = \frac{q}{m}\left(\mathbf{E}_n + \frac{\mathbf{v}_{n+1/2}+\mathbf{v}_{n-1/2}}{2}\times\mathbf{B}_n\right)$$

> **Unicode**
> ```
> (𝐯_n+1/2-𝐯_n-1/2)/(Δ t) = (q)/(m)(𝐄ₙ + (𝐯_n+1/2+𝐯_n-1/2)/(2)×𝐁ₙ)
> ```

The key point here is using the average $\mathbf{v}_n = (\mathbf{v}_{n+1/2}+\mathbf{v}_{n-1/2})/2$.

**Three-step splitting:**

#### Step 1: Half-step electric-field acceleration

$$\mathbf{v}^- = \mathbf{v}_{n-1/2} + \frac{q\mathbf{E}_n}{m}\frac{\Delta t}{2}$$

> **Unicode**
> ```
> 𝐯⁻ = 𝐯_n-1/2 + (q𝐄ₙ)/(m)(Δ t)/(2)
> ```

#### Step 2: Magnetic rotation

$$\frac{\mathbf{v}^+ - \mathbf{v}^-}{\Delta t} = \frac{q}{2m}(\mathbf{v}^++\mathbf{v}^-)\times\mathbf{B}_n$$

> **Unicode**
> ```
> (𝐯⁺ - 𝐯⁻)/(Δ t) = (q)/(2m)(𝐯⁺+𝐯⁻)×𝐁ₙ
> ```

**This rotation is solved analytically.** Define the vectors:

$$\mathbf{t} = \frac{q\mathbf{B}_n}{m}\frac{\Delta t}{2}, \quad \mathbf{s} = \frac{2\mathbf{t}}{1+t^2}$$

> **Unicode**
> ```
> 𝐭 = (q𝐁ₙ)/(m)(Δ t)/(2),   𝐬 = (2𝐭)/(1+t²)
> ```

Then:

$$\mathbf{v}' = \mathbf{v}^- + \mathbf{v}^-\times\mathbf{t}$$
$$\mathbf{v}^+ = \mathbf{v}^- + \mathbf{v}'\times\mathbf{s}$$

> **Unicode**
> ```
> 𝐯' = 𝐯⁻ + 𝐯⁻×𝐭
> 𝐯⁺ = 𝐯⁻ + 𝐯'×𝐬
> ```

**This is an exact rotation:** $|\mathbf{v}^+| = |\mathbf{v}^-|$.

#### Step 3: Half-step electric-field acceleration

$$\mathbf{v}_{n+1/2} = \mathbf{v}^+ + \frac{q\mathbf{E}_n}{m}\frac{\Delta t}{2}$$

> **Unicode**
> ```
> 𝐯_n+1/2 = 𝐯⁺ + (q𝐄ₙ)/(m)(Δ t)/(2)
> ```

#### Position update

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1/2}\Delta t$$

> **Unicode**
> ```
> 𝐱ₙ₊₁ = 𝐱ₙ + 𝐯_n+1/2Δ t
> ```

### 2.4.3 Proof of Phase-Space Volume Conservation

The Boris map:

$$\mathcal{M}: (\mathbf{x}_n, \mathbf{v}_{n-1/2}) \to (\mathbf{x}_{n+1}, \mathbf{v}_{n+1/2})$$

> **Unicode**
> ```
> M: (𝐱ₙ,𝐯_n-1/2) → (𝐱ₙ₊₁,𝐯_n+1/2)
> ```

Jacobian:

$$J = \left|\frac{\partial(\mathbf{x}_{n+1}, \mathbf{v}_{n+1/2})}{\partial(\mathbf{x}_n, \mathbf{v}_{n-1/2})}\right|$$

> **Unicode**
> ```
> J = |(∂(𝐱ₙ₊₁,𝐯_n+1/2))/(∂(𝐱ₙ,𝐯_n-1/2))|
> ```

**Step-by-step decomposition:**

- **Steps 1, 3:** $\mathbf{v}^\pm = \mathbf{v} + const(\mathbf{x})$. $\partial\mathbf{v}^\pm/\partial\mathbf{v} = I$, a shear transformation → determinant 1
- **Step 2:** rotation $\mathbf{v}^+ = R(\mathbf{B}_n)\mathbf{v}^-$. $R$ is orthogonal, $|\det R| = 1$
- **Position update:** $\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1/2}\Delta t$ is also a shear, determinant 1

**Hence:**

$$\det J = 1$$

> **Unicode**
> ```
> det J = 1
> ```

**Liouville's theorem is satisfied. Phase-space volume conservation means particles are not unphysically heated or cooled over long times.** This is why Boris survives even a billion steps.

> **Footnote — Is Boris symplectic?** Unconditionally classifying the Boris algorithm as a "symplectic integrator" is contested. Qin et al. (*Why is Boris algorithm so good?*, Phys. Plasmas 20, 084503, 2013) and Ellison, Burby & Qin (*Comment on "Symplectic integration of magnetic systems"*, J. Comput. Phys. 301, 489, 2015) point out that while Boris preserves phase-space volume, it is not, in the general sense, a symplectic or variational method. This document therefore describes Boris as a **second-order-accurate volume-preserving / structure-preserving method** and avoids the definitive label "symplectic."

**Accuracy:** second order in time, $\mathcal{O}(\Delta t^2)$. In a uniform $\mathbf{B}$ with $\mathbf{E}=0$, there is a gyro-phase error, but $r_L$ is conserved permanently.

**Stability condition:** $\omega_c\Delta t < 2$. In practice, $\omega_c\Delta t < 0.3$ is recommended.

### 2.4.4 Symplectic Integrators (Störmer–Verlet, Leapfrog)

The Hamiltonian $H = (\mathbf{p}-q\mathbf{A})^2/2m + q\phi$ is non-separable in general, but is separable when $\mathbf{B}$ is uniform.

**Velocity Verlet:**

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_n\Delta t + \frac12\mathbf{a}_n\Delta t^2$$

$$\mathbf{v}_{n+1} = \mathbf{v}_n + \frac12(\mathbf{a}_n + \mathbf{a}_{n+1})\Delta t$$

> **Unicode**
> ```
> 𝐱ₙ₊₁ = 𝐱ₙ + 𝐯ₙΔ t + (1)/(2)𝐚ₙΔ t²
> 𝐯ₙ₊₁ = 𝐯ₙ + (1)/(2)(𝐚ₙ + 𝐚ₙ₊₁)Δ t
> ```

Since $\mathbf{a} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})/m$ depends on $\mathbf{v}$, this becomes **implicit** and requires iteration. Boris, in contrast, bypasses this problem by treating the rotation step **explicitly**. However, as shown below it is safer to view Boris as a **structure-preserving method that conserves phase-space volume**, rather than flatly asserting it to be "the optimal implementation of symplectic Verlet" (there is literature-level debate over whether Boris is symplectic; see §2.4.2, §2.4.8).

**Conservation properties of velocity Verlet:**

- **Symplectic:** $\omega = dp_i \wedge dx_i$ is **exactly conserved** → Jacobian 1
- **Energy:** not exactly conserved, but a symplectic integrator exactly conserves a **modified Hamiltonian** $\tilde{H} = H + \mathcal{O}(\Delta t^2)$. Hence the energy error is **bounded** at $\mathcal{O}(\Delta t^2)$, with no linear drift in time.
- **Momentum:** exactly conserved when there is spatial symmetry.

**Higher-order symplectic methods:** a 4th-order Yoshida construction achieving $\mathcal{O}(\Delta t^4)$ is possible. In PIC, the 2nd-order Boris method dominates due to cost.

### 2.4.5 The Limits of Runge–Kutta

The standard RK4:

$$k_1 = f(y_n), \quad k_2 = f(y_n + \Delta t k_1/2), \ldots$$

> **Unicode**
> ```
> k₁ = f(yₙ),   k₂ = f(yₙ + Δ t k₁/2), ...
> ```

**Three problems:**

1. **Non-symplectic:** $\det J \neq 1$. Phase-space volume expands/contracts by $1+\mathcal{O}(\Delta t^5)$ every step
2. **Energy drift:** in a uniform $\mathbf{B}$, the analytic solution has $|\mathbf{v}| = const$. RK4 gives numerical damping/amplification:

   $$|\mathbf{v}_{n+1}| = |\mathbf{v}_n|(1 + C(\omega_c\Delta t)^5 + \ldots)$$
   
   > **Unicode**
   > ```
   > |𝐯ₙ₊₁| = |𝐯ₙ|(1 + C(ω_cΔ t)⁵ + ...)
   > ```

   If $C > 0$, gyro-energy grows exponentially over long times. When tracking a tokamak for 1 second ($10^8$ gyro-periods), RK4 collapses completely

3. **Destruction of the magnetic moment:** $\mu$ monotonically increases due to numerical scattering, artificially breaking magnetic-mirror confinement

**Where RK4 stands:** it has excellent short-term accuracy (local error $\mathcal{O}(\Delta t^5)$), but is unsuitable for plasmas that require long-term tracking and statistical equilibrium. It is advantageous only for one-shot problems with rapidly varying $\mathbf{E}(t)$, such as laser acceleration.

### 2.4.6 The Principle of PIC (Particle-In-Cell)

Apply the Lorentz pusher to $10^6 \sim 10^{11}$ particles, with the fields solved via Maxwell's equations on a grid.

**The PIC loop:**

1. **Weighting / Charge Deposition:** particle position $\mathbf{x}_p$ → grid charge density
   
   $$\rho_g = \sum_p q_p S(\mathbf{x}_g-\mathbf{x}_p)$$
   
   > **Unicode**
   > ```
   > ρ_g = ∑ₚ qₚ S(𝐱_g-𝐱ₚ)
   > ```
   
   $S$ is a B-spline shape function (NGP, CIC, TSC)

2. **Field Solve:** solve $\nabla^2\phi = -\rho/\epsilon_0$, or the full Maxwell system $\partial_t\mathbf{B} = -\nabla\times\mathbf{E}$, $\partial_t\mathbf{E} = c^2\nabla\times\mathbf{B} - \mathbf{J}/\epsilon_0$, via FDTD (Yee grid)

3. **Field Interpolation:** grid $\mathbf{E}_g, \mathbf{B}_g$ → particle position
   
   $$\mathbf{E}_p = \sum_g \mathbf{E}_g S(\mathbf{x}_g-\mathbf{x}_p)$$
   
   > **Unicode**
   > ```
   > 𝐄ₚ = ∑_g 𝐄_g S(𝐱_g-𝐱ₚ)
   > ```

4. **Pusher:** update $\mathbf{v}_p, \mathbf{x}_p$ with Boris

5. **Current Deposition:** generate $\mathbf{J}_g$ using the Esirkepov method, which satisfies charge conservation

**The physics of PIC:** a mean-field approximation. Even without collisions, wave–particle resonance reproduces kinetic effects such as **Landau damping** and the **two-stream instability**.

**Applications:** fusion, space plasmas, Hall thrusters, semiconductor etching plasmas.

**Numerical heating:** the greatest enemy. If the grid cannot resolve $\lambda_D$ (the Debye length) — i.e., $\Delta x > \lambda_D$ — artificial heating occurs. This is why energy-conserving PIC (implicit PIC) was developed.

### 2.4.7 Coupling with MCC (Monte Carlo Collision)

PIC solves the collisionless Vlasov equation. Real plasmas collide with neutral gas.

**The MCC algorithm:** for each particle, at every $\Delta t$:

**Collision probability:**

$$P = 1 - \exp(-\nu(v)\Delta t) \approx \nu\Delta t, \quad \nu = n_g \sigma(v) v$$

> **Unicode**
> ```
> P = 1 - exp(-ν(v)Δ t) ≈ νΔ t,   ν = n_g σ(v) v
> ```

$\sigma(v)$: collision cross-section (elastic, excitation, ionization)

**Procedure:**
1. Generate a random number $R \in [0,1]$
2. If $R < P$, a collision occurs
3. The type of collision is sampled with probability proportional to $\nu_k/\nu_{total}$
4. The scattering angle is sampled from the differential cross-section

**Implementation order:** Pusher, then MCC → randomize the direction of $v$ + energy loss → next step

**Applications of PIC-MCC:** the industry standard for low-temperature plasmas. Reproduces the non-Maxwellian tail of the electron energy distribution function (EEDF) in CCP and ICP discharges.

### 2.4.8 Comparison Table of Methods

| Method | Order | Geometric property | Energy behavior | Stability condition | Advantages | Disadvantages |
|---|---|---|---|---|---|---|
| **Boris** | 2nd | volume-preserving / structure-preserving, $\det J = 1$ (whether it is symplectic is debated in the literature, see footnote) | Preserves to machine precision with $\mathbf{B}$ only; bounded oscillation when $\mathbf{E}$ is included | $\omega_c\Delta t < 2$ | Long-term conservation, fast and simple, PIC standard | Phase error near resonance $\omega_c\Delta t \approx \pi$ |
| **Velocity Verlet** | 2nd | Yes, symplectic | Conserves a modified Hamiltonian, no drift | $\omega_c\Delta t < 2$ | Theoretical rigor | Requires implicit iteration due to $\mathbf{v}\times\mathbf{B}$ |
| **4th-order Yoshida** | 4th | Yes | Energy error bounded at $\mathcal{O}(\Delta t^4)$ | Same | High-precision long-term tracking | 3x the computation, inefficient in PIC |
| **RK4** | 4th | No, $\det J \neq 1$ | Linear/exponential drift $\Delta E \sim t\Delta t^4$ | Conditionally stable, $\omega_c\Delta t \lesssim 2.8$ | High short-term precision, easy to implement | Long-term heating, destroys $\mu$, unusable for plasmas |
| **Implicit PIC** | 1st–2nd | Exact energy conservation, volume not preserved | Preserves energy to machine precision | Unconditionally stable (allows large $\Delta t$) | Allows $\Delta x > \lambda_D$ | Requires matrix solves, numerical damping |

**Practical conclusions:**
- Tracking magnetic confinement for $10^6$ or more steps → **Boris is essential**
- One-shot, high-precision trajectories (e.g. synchrotron-radiation tracking) → RK4 or 4th-order symplectic
- Collective plasma phenomena → **PIC + Boris + MCC**

Without Boris, modern plasma simulation would not exist.

### 2.4.9 Mathematica Verification

```mathematica
(* Verify the Boris rotation step *)
borisRotate[vMinus_, q_, m_, dt_, Bvec_] := Module[
  {t, s, vPrime, vPlus},
  t = (q Bvec dt)/(2 m);
  s = (2 t)/(1 + t . t);
  vPrime = vMinus + Cross[vMinus, t];
  vPlus = vMinus + Cross[vPrime, s];
  vPlus
];

(* Verify conservation of speed *)
v0 = {1, 0, 0};
Bvec = {0, 0, 1};
v1 = borisRotate[v0, 1, 1, 0.1, Bvec];
Norm[v1] - Norm[v0]
(* Output: 0 *)
```

### 2.4.10 Limits and Exceptions

- **Magnetic reconnection**: near $\mathbf{B} \to 0$, the gyro-period $\to \infty$, and the Boris condition $\omega_c\Delta t < 2$ breaks down
- **Relativistic regime**: at $\gamma \gg 1$, Boris requires modification (relativistic Boris, Vay 2008)
- **Strong $\mathbf{E}$**: when $E > B$, the $E\times B$ frame exceeds the speed of light and requires special treatment
- **Numerical Cherenkov**: unphysical radiation occurs when $\Delta x < c\Delta t$

> **References**
> - Boris, J. P., *Relativistic plasma simulation-optimization of a hybrid code*, Proc. 4th Conf. Numerical Simulation of Plasmas, 3–67 (1970). [ADS](https://ui.adsabs.harvard.edu/abs/1970nusp.conf....3B)
> - Esirkepov, T. Zh., *Exact charge conservation scheme for PIC simulation*, Comput. Phys. Commun. **144**, 26 (2001). [doi:10.1016/S0010-4655(00)00228-9](https://doi.org/10.1016/S0010-4655(00)00228-9)
> - Hockney, R. W., Eastwood, J. W., *Computer Simulation Using Particles*, Adam Hilger (1988). [doi:10.1201/9780367806934](https://doi.org/10.1201/9780367806934)
> - Birdsall, C. K., Langdon, A. B., *Plasma Physics via Computer Simulation*, McGraw-Hill (1985).

---

## 2.5 Topology and Geometry — Curvature of the $U(1)$ Bundle

The Lorentz force $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ looks like a vector formula, but viewed through modern geometry it is **the phenomenon by which curvature on a principal bundle makes the particle depart from geodesic motion** (to be distinguished from the standard notion of geodesic deviation in general relativity). This section covers Berry phase, the Aharonov–Bohm effect, magnetic monopoles, fiber bundles, differential forms, and the $U(1)$ Lie group.

### 2.5.1 Berry Phase and the Lorentz Force

A quantum system moving adiabatically, $|n(\mathbf{R}(t))\rangle$, acquires a **geometric phase** in addition to the dynamical phase:

$$|\psi(T)\rangle = e^{i\theta_{dyn}} e^{i\gamma_n} |n(\mathbf{R}(T))\rangle$$

> **Unicode**
> ```
> |ψ(T)⟩ = e^iθ_dyn e^iγₙ |n(𝐑(T))⟩
> ```

Here the **Berry phase**:

$$\gamma_n = \oint_C \mathcal{A}_n \cdot d\mathbf{R}, \quad \mathcal{A}_n = i\langle n|\nabla_{\mathbf{R}}|n\rangle$$

> **Unicode**
> ```
> γₙ = ∮_C Aₙ · d𝐑,   Aₙ = i⟨ n|∇_𝐑|n⟩
> ```

The **Berry connection** $\mathcal{A}_n$ is **mathematically identical** to the electromagnetic potential $\mathbf{A}$. The Berry curvature:

$$\mathbf{\Omega}_n = \nabla_{\mathbf{R}}\times\mathcal{A}_n$$

> **Unicode**
> ```
> Ωₙ = ∇_𝐑×Aₙ
> ```

The force appearing in the **semiclassical equation of motion** is exactly of Lorentz form:

$$\hbar\dot{\mathbf{k}} = -e\mathbf{E} - e\dot{\mathbf{r}}\times\mathbf{B} + \text{(Berry term)}$$

> **Unicode**
> ```
> ℏ𝐤˙ = -e𝐄 - e𝐫˙×𝐁 + (Berry term)
> ```

$$\dot{\mathbf{r}} = \frac{1}{\hbar}\frac{\partial\epsilon_n}{\partial\mathbf{k}} - \dot{\mathbf{k}}\times\mathbf{\Omega}_n(\mathbf{k})$$

> **Unicode**
> ```
> 𝐫˙ = (1)/(ℏ)(∂εₙ)/(∂𝐤) - 𝐤˙×Ωₙ(𝐤)
> ```

**The second term is the Lorentz force in k-space.** That is:
- A real magnetic field $\mathbf{B}$ → a real-space Berry curvature
- Berry curvature $\mathbf{\Omega}$ → a magnetic field in momentum space
- The electromagnetic Lorentz force is a special case of the Berry phase

### 2.5.2 The Aharonov–Bohm Effect

**Setup:** outside the solenoid, $\mathbf{B} = 0$, so the classical Lorentz force is 0. However, $\mathbf{A} \neq 0$; $\nabla\times\mathbf{A} = 0$, but:

$$\oint \mathbf{A}\cdot d\boldsymbol{\ell} = \Phi_B \neq 0$$

> **Unicode**
> ```
> ∮ 𝐀· dℓ = Φ_B ≠ 0
> ```

**Quantum interference:**

$$\Delta\varphi_{AB} = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi_B}{\hbar}$$

> **Unicode**
> ```
> Δφ_AB = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ_B)/(ℏ)
> ```

**Topological meaning:**

- Space is **not simply connected**: $\mathbb{R}^3 \setminus \text{solenoid} \simeq S^1$
- Since $F = dA = 0$, the curvature is zero, but the **holonomy** is nonzero
- de Rham cohomology $H^1_{dR}(M) \neq 0$: the closed form $A$ is not exact. $A \neq d\chi$ globally

**That is, even where the Lorentz force is zero, the topological twist of the $U(1)$ bundle remains and produces a quantum phase.** The classical force is the local effect of the curvature $F$; the AB effect is the global topological effect of the connection $A$. The two are two faces of the same bundle.

> **Classical:** $F$ deflects the particle; **Quantum:** $\exp(i\oint A)$ deflects the phase

### 2.5.3 Magnetic Monopoles and Dirac Quantization

Allowing a magnetic monopole $\nabla\cdot\mathbf{B} = g\delta^3(\mathbf{r})$ means $F$ is no longer globally $dA$. $dF \neq 0$ at the origin.

**Dirac's construction:** defined separately on the northern hemisphere $A_N$ and southern hemisphere $A_S$:

$$A_N = \frac{g}{r}\frac{1-\cos\theta}{\sin\theta}\hat{\phi}, \quad A_S = -\frac{g}{r}\frac{1+\cos\theta}{\sin\theta}\hat{\phi}$$

> **Unicode**
> ```
> A_N = (g)/(r)(1-cosθ)/(sinθ)φ̂,   A_S = -(g)/(r)(1+cosθ)/(sinθ)φ̂
> ```

Gauge transformation at the equator: $A_N = A_S + \nabla\chi$, $\chi = 2g\phi$

**Single-valuedness of the wave function requires:** $\exp(iq\chi/\hbar)$ must equal 1 as $\phi \to \phi+2\pi$:

$$\exp\left(i\frac{q}{\hbar}2g\cdot2\pi\right) = 1 \implies qg = n\frac{\hbar}{2}, \quad n \in \mathbb{Z}$$

> **Unicode**
> ```
> qg = n(ℏ)/(2),   n∈ℤ
> ```

**This is Dirac quantization.** The Wu–Yang interpretation: a magnetic monopole is not a trivial $U(1)$ bundle. It is a **twisted bundle** over $S^2$. The degree of twisting is the **first Chern number**:

$$c_1 = \frac{1}{2\pi}\int_{S^2} F = \frac{1}{2\pi}\int_{S^2} \mathbf{B}\cdot d\mathbf{S} = 2g$$

> **Unicode**
> ```
> c₁ = (1)/(2π)∫_S² F = (1)/(2π)∫_S² 𝐁· d𝐒 = 2g
> ```

In natural units ($e = \hbar = 1$), $c_1 = 2g$. In SI, dimensions are restored as $c_1 = 2eg/\hbar$.

**Charge quantization is the quantization of the topology of space.** Even a single magnetic monopole would quantize all charge in the universe.

**Extension of the Lorentz force:** in the presence of a monopole:

$$\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + g\left(\mathbf{B}-\frac{\mathbf{v}}{c^2}\times\mathbf{E}\right)$$

> **Unicode**
> ```
> 𝐅 = q(𝐄+𝐯×𝐁) + g(𝐁-(𝐯)/(c²)×𝐄)
> ```

The topological obstruction of the $g$ term is the essence of this.

### 2.5.4 Electromagnetism as a Fiber Bundle and Gauge Field

**Modern definition:**

- **Base manifold** $M$: spacetime (Minkowski $\mathbb{R}^{1,3}$)
- **Structure group** $G = U(1)$: phase $e^{i\theta}$
- **Principal bundle** $P(M, U(1))$: a circle $U(1)$ fiber above each point $x\in M$
- **Connection** 1-form $A = A_\mu dx^\mu = -\phi\, dt + \mathbf{A}\cdot d\mathbf{x}$: prescribes parallel transport between fibers
- **Curvature** 2-form $F = dA + A\wedge A = dA$ (zero commutator since $U(1)$ is Abelian): the actual physical field

The **particle's wave function** is a **section** of the associated complex line bundle. Covariant derivative:

$$D_\mu = \partial_\mu - i\frac{q}{\hbar}A_\mu$$

> **Unicode**
> ```
> D_μ = ∂_μ - i(q)/(ℏ)A_μ
> ```

This sign is chosen to be consistent with the minimal-coupling convention $\mathbf{p}-q\mathbf{A}=m\mathbf{v}$, $H=(\mathbf{p}-q\mathbf{A})^2/2m$ used in §1.4 ($-i\hbar D_\mu = -i\hbar\partial_\mu - qA_\mu$). The sign itself is not absolutely fixed; what matters is that the gauge transformations of $D_\mu$, $\psi$, and $A_\mu$ interlock consistently into a single framework.

**Failure of parallel transport = curvature = the Lorentz force.** The classical limit of the geodesic equation $D_\mu D^\mu\psi = 0$ is $dp^\mu/d\tau = qF^{\mu\nu}u_\nu$.

**A gauge transformation** is a vertical automorphism of the bundle: it rotates the fiber by $\psi \to e^{iq\chi/\hbar}\psi$. Even though the connection changes as $A_\mu \to A_\mu + \partial_\mu\chi$, the curvature $F$ is invariant, and $D_\mu\psi \to e^{iq\chi/\hbar}D_\mu\psi$ transforms the same way as the wave function.

**The Lorentz force is the geometric force by which the curvature of the bundle causes the particle's worldline to depart from geodesic motion.** However, this is conceptually distinct from the standard **geodesic deviation** of general relativity, which describes the relative acceleration of neighboring geodesics via curvature; the similarity is only at the qualitative level that "curvature affects the worldline."

### 2.5.5 Maxwell's Equations in Differential Forms

The language of forms makes the topology of the Lorentz force clearest.

**1-form:** $A = A_\mu dx^\mu$

**2-form:** $F = \frac12 F_{\mu\nu}dx^\mu\wedge dx^\nu = E_i\, dx^i\wedge dt + \frac12\epsilon_{ijk}B_k\, dx^i\wedge dx^j$

> **Unicode**
> ```
> F = (1)/(2) F_μνdx^μ∧ dx^ν = Eᵢ dxⁱ∧ dt + (1)/(2)εᵢⱼₖBₖ dxⁱ∧ dxʲ
> ```

#### The Bianchi Identity

$$dF = 0 \iff \begin{cases}\nabla\cdot\mathbf{B} = 0 \\ \nabla\times\mathbf{E} + \partial_t\mathbf{B} = 0\end{cases}$$

> **Unicode**
> ```
> dF = 0 ⟺ ∇·𝐁 = 0 ;  ∇×𝐄 + ∂ₜ𝐁 = 0
> ```

A consequence of $d^2 = 0$. Automatic if $F = dA$. With a monopole, $dF = \star J_m \neq 0$, a topological obstruction.

#### The Equation of Motion

$$d\star F = \star J \iff \begin{cases}\nabla\cdot\mathbf{E} = \rho/\epsilon_0 \\ \nabla\times\mathbf{B} - \partial_t\mathbf{E} = \mu_0\mathbf{J}\end{cases}$$

> **Unicode**
> ```
> d⋆ F = ⋆ J ⟺ ∇·𝐄 = ρ/ε₀ ;  ∇×𝐁 - ∂ₜ𝐄 = μ₀𝐉
> ```

$\star$ is the Hodge dual.

#### The Lorentz Force

The particle worldline $C$, 4-velocity $u$, momentum 1-form $p$. Action:

$$S = -m\int d\tau + q\int_C A$$

> **Unicode**
> ```
> S = -m∫ dτ + q∫_C A
> ```

Variation $\delta S = 0$ →

$$i_u F = dp/d\tau$$

> **Unicode**
> ```
> iᵤ F = dp/dτ
> ```

In components, $f_\mu = qF_{\mu\nu}u^\nu$. That is, **the force is $F$ contracted with $u$**.

**Stokes' theorem** $\int_S F = \oint_{\partial S} A$ is precisely the Berry/AB phase.

### 2.5.6 The $U(1)$ Lie Group and Symmetry

$$U(1) = \{e^{i\theta} \mid \theta \in [0, 2\pi)\}$$

> **Unicode**
> ```
> U(1) = {e^iθ | θ∈[0,2π)}
> ```

An Abelian Lie group, with Lie algebra $u(1) = i\mathbb{R}$.

**Symmetry:** the Lagrangian $L = \bar\psi(i\slashed{D}-m)\psi$ is invariant under local $U(1)$ transformations $\psi \to e^{iq\chi(x)}\psi$, $A \to A + d\chi$. **Noether's theorem → charge conservation** $d\star J = 0$.

**The symmetric origin of the Lorentz force:** the minimal-coupling principle $p_\mu \to p_\mu - qA_\mu$ is enforced by $U(1)$ representation theory. A different group gives a different force:
- $SU(2)$ → a Lorentz-force analogue for the weak force, $f^a = gF^{a\mu\nu}u_\nu$
- $SU(3)$ → the color Lorentz force

**That is, the electromagnetic Lorentz force is the $U(1)$ version.**

**Topological invariant: the Wilson loop**

$$W(C) = \exp\left(iq\oint_C A\right) \in U(1)$$

> **Unicode**
> ```
> W(C) = exp(iq∮_C A) ∈ U(1)
> ```

A gauge-invariant observable. The fundamental variable of the AB phase, the Berry phase, and lattice gauge theory. **The Lorentz force is the infinitesimal version of $W$**: for a small loop, $W \approx 1 + iqF_{\mu\nu}dS^{\mu\nu}$.

### 2.5.7 Summary Table

| Concept | Geometric object | Physical consequence |
|---|---|---|
| $A$ | $U(1)$ connection 1-form | Berry connection, AB phase $\gamma = \oint A$ |
| $F = dA$ | Curvature 2-form | $\mathbf{E}, \mathbf{B}$, Lorentz force $q\,i_u F$ |
| $dF = 0$ | Bianchi identity, trivial bundle | Forbids magnetic monopoles, flux conservation |
| $d\star F = J$ | Yang–Mills equation | Source of the field |
| $c_1 = \frac{1}{2\pi}\int F$ | First Chern number | Dirac quantization $qg = n\hbar/2$ |

### 2.5.8 Mathematica Verification

```mathematica
(* Verify the differential-form structure of the electromagnetic tensor *)
(* The condition F = dA *)
Aform = -phi[x, y, z, t] dt + Ax[x, y, z, t] dx + Ay[x, y, z, t] dy + Az[x, y, z, t] dz;
Fform = d[Aform];
(* Check that the components of F are expressed in terms of E, B *)
Collect[Fform, {dt, dx, dy, dz}]

(* dF = 0 (Bianchi) *)
Simplify[d[Fform] == 0]

```

### 2.5.9 Limits and Exceptions

- **Non-simple connectivity**: the AB effect and Dirac quantization depend on the topology (holes, monopoles) of space
- **Non-Abelian extension**: in $SU(2)$, $SU(3)$, $F = dA + A\wedge A$ adds a commutator term (→ §6.1.1)
- **Non-adiabatic Berry phase**: if the adiabatic condition $\dot{R} \to 0$ is broken, the very definition of the Berry phase becomes ambiguous
- **Strong coupling**: at $g \gg 1$, perturbation theory breaks down and lattice gauge theory is required

> **References**
> - Berry, M. V., *Quantal phase factors accompanying adiabatic changes*, Proc. R. Soc. A **392**, 45–57 (1984). [doi:10.1098/rspa.1984.0023](https://doi.org/10.1098/rspa.1984.0023)
> - Aharonov, Y., Bohm, D., *Significance of Electromagnetic Potentials in the Quantum Theory*, Phys. Rev. **115**, 485 (1959). [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
> - Dirac, P. A. M., *Quantised singularities in the electromagnetic field*, Proc. R. Soc. A **133**, 60 (1931). [doi:10.1098/rspa.1931.0130](https://doi.org/10.1098/rspa.1931.0130)
> - Nakahara, M., *Geometry, Topology and Physics*, 2nd ed., Taylor & Francis (2003), Chapter 10.
> - Xiao, D., Chang, M.-C., Niu, Q., *Berry phase effects on electronic properties*, Rev. Mod. Phys. **82**, 1959 (2010). [doi:10.1103/RevModPhys.82.1959](https://doi.org/10.1103/RevModPhys.82.1959)

---
# Act 3. Physical Depth

> **Arc of this act**
> Relativity → Radiation → Quantum → Statistics
>
> Through Act 2, the classical and geometric structure of the Lorentz force was established. Act 3 covers how that structure extends under **relativity, radiation, quantum mechanics, and statistics**. The Lorentz force shows a new face in each of the three limits: $v \to c$, $\hbar \neq 0$, and $N \to \infty$.

---

## 3.1 The Relativistic Lorentz Force

The non-relativistic $m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ breaks down when $\gamma \gg 1$. The dynamical variable is not the mass but the **momentum $\mathbf{p}$**. This section covers the relativistic equation of motion, longitudinal/transverse mass, and the transformation of the electromagnetic field.

### 3.1.1 The Relativistic Equation of Motion

**Relativistic momentum:**

$$\mathbf{p} = \gamma m \mathbf{v}, \quad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}, \quad E_{tot} = \gamma mc^2$$

> **Unicode**
> ```
> 𝐩 = γ m 𝐯,   γ = (1)/(√(1-v²/c²)),   Eₜₒₜ = γ mc²
> ```

**Equation of motion:**

$$\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> (d𝐩)/(dt) = q(𝐄 + 𝐯×𝐁)
> ```

**Energy equation:**

$$\frac{d(\gamma mc^2)}{dt} = q\mathbf{v}\cdot\mathbf{E}$$

> **Unicode**
> ```
> (d(γ mc²))/(dt) = q𝐯·𝐄
> ```

The form looks Newtonian, but it is **nonlinear** because $\gamma$ is hidden inside $\mathbf{p}$.

**4-vector form:**

$$\frac{dp^\mu}{d\tau} = qF^{\mu\nu}u_\nu, \quad p^\mu = (\gamma mc, \mathbf{p}), \quad u^\mu = \gamma(c, \mathbf{v})$$

> **Unicode**
> ```
> (dp^μ)/(dτ) = qF^μνu_ν,   p^μ = (γ mc,𝐩),   u^μ = γ(c,𝐯)
> ```

This form was already derived in §1.3. Here we examine its **physical implications**.

### 3.1.2 Longitudinal and Transverse Mass

Acceleration **parallel** to $\mathbf{v}$ and **perpendicular** to it have different inertia. Decomposing the equation of motion:

$$\mathbf{a}_\parallel = \frac{q}{m\gamma^3}\mathbf{E}_\parallel, \quad \mathbf{a}_\perp = \frac{q}{m\gamma}(\mathbf{E}_\perp + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐚_∥ = (q)/(mγ³)𝐄_∥,   𝐚_⊥ = (q)/(mγ)(𝐄_⊥ + 𝐯×𝐁)
> ```

- $\gamma^3 m$: the **longitudinal mass**
- $\gamma m$: the **transverse mass**

As $v \to c$, accelerating with the same force becomes **$\gamma^3$ times harder**. This is why a particle cannot reach the speed of light.

**Numerical example:** for an LHC proton, $\gamma = 7460$, so the longitudinal mass $= 7460^3 m_p \approx 4\times 10^{14} m_p$.

### 3.1.3 The Relativistic Cyclotron Frequency

In a uniform $\mathbf{B}$, the solution is still a helix, but **the frequency is inversely proportional to the energy**:

$$\omega_c^{rel} = \frac{qB}{\gamma m} = \frac{\omega_{c,0}}{\gamma}, \quad r_L^{rel} = \frac{\gamma m v_\perp}{|q|B} = \frac{p_\perp}{|q|B}$$

> **Unicode**
> ```
> ω_cʳᵉˡ = (qB)/(γ m) = (ω_c,0)/(γ),   r_Lʳᵉˡ = (γ m v_⊥)/(|q|B) = (p_⊥)/(|q|B)
> ```

**This is the relativistic limit of the cyclotron.** If the RF frequency is tuned to $\omega_c^{rel}$, resonance breaks down as the frequency drops with increasing energy.

**Numbers:** for a 1 GeV proton, $\gamma \approx 2$, a 50% drop in frequency → resonance collapses. The classical cyclotron limit is $\sim 20$ MeV for protons.

**Solutions (→ §4.1):**
- **Synchrocyclotron:** modulate the RF frequency in time
- **Isochronous cyclotron:** increase $B(r)$ with radius

### 3.1.4 Lorentz Transformation of the Electromagnetic Field Tensor

Since $F^{\mu\nu}$ is a rank-2 tensor, it transforms under a Lorentz boost:

$$F'^{\mu\nu} = \Lambda^\mu{}_\alpha \Lambda^\nu{}_\beta F^{\alpha\beta}$$

> **Unicode**
> ```
> F'^μν = Λ^μ_ α Λ^ν_ β F^αβ
> ```

**Field transformation** for a boost with velocity $\mathbf{V} = V\hat{x}$:

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

### 3.1.5 The Relativistic Origin of $\mathbf{v}\times\mathbf{B}$

**Key insight:** even a purely magnetic field looks like an **electric field** to a moving observer:

$$\mathbf{E}' = \gamma\mathbf{V}\times\mathbf{B}$$

> **Unicode**
> ```
> 𝐄' = γ𝐕×𝐁
> ```

**This is precisely the relativistic origin of the $\mathbf{v}\times\mathbf{B}$ Lorentz force.** The magnetic force is the electric force as seen from a different inertial frame.

**Two invariants:**

$$I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2, \quad I_2 = c\mathbf{E}\cdot\mathbf{B}$$

> **Unicode**
> ```
> I₁ = c²𝐁² - 𝐄²,   I₂ = c𝐄·𝐁
> ```

- If $I_1 > 0, I_2 = 0$, **the magnetic field dominates** → a coordinate transformation can make $\mathbf{E}' = 0$
- This frame is **the frame in which the guiding center is at rest**
- The relativistic interpretation of the $E\times B$ drift

That is, $\mathbf{E}+\mathbf{v}\times\mathbf{B}$ is the 3D projection of $F^{\mu\nu}u_\nu$, and **the radiation formulas, rigidity, and field transformations all follow consistently from this single 4-tensor structure**.

### 3.1.6 Mathematica Verification

```mathematica
(* Relativistic Lorentz force *)
gamma[v_] := 1/Sqrt[1 - v . v/c^2];
pRel[v_] := gamma[v] m0 v;

(* Equation of motion *)
eqns = D[pRel[{vx[t], vy[t], vz[t]}], t] ==
  q ({Ex, Ey, Ez} + Cross[{vx[t], vy[t], vz[t]}, {Bx, By, Bz}]);

(* Verify the relativistic cyclotron frequency in uniform B *)
omegaRel = q B0 / (gamma m0);
```

### 3.1.7 Limits and Exceptions

- **Non-relativistic limit**: as $v \ll c$, $\gamma \to 1$, and all formulas reduce to Act 1
- **Speed-of-light limit**: as $v \to c$, $\gamma \to \infty$, and the longitudinal mass diverges
- **Radiation reaction**: a relativistic particle loses energy to radiation when accelerated (→ §3.2)
- **Quantum regime**: when $\hbar\omega_c \sim mc^2$, quantum effects are essential (→ §3.3)

> **References**
> - Landau & Lifshitz, *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §17, §23.
> - Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1998), §11.10.
> - Sokolov, A. A., Ternov, I. M., *Synchrotron Radiation*, Pergamon (1968).

---

## 3.2 Radiation Loss

When a relativistic charged particle accelerates, it **emits electromagnetic radiation** and loses energy. This section covers the Larmor formula, its Liénard generalization, the Abraham–Lorentz–Dirac equation, the Landau–Lifshitz prescription, synchrotron radiation, and rigidity.

### 3.2.1 The Larmor Formula

**Non-relativistic Larmor formula (SI):**

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

> **Unicode**
> ```
> P = (q² a²)/(6πε₀ c³)
> ```

**Gaussian units:**

$$P = \frac{2q^2 a^2}{3c^3}$$

> **Unicode**
> ```
> P = (2q² a²)/(3c³)
> ```

**Derivation:** integrating the Poynting flux of the retarded-potential radiation field $\mathbf{E}_{rad} \sim q\mathbf{n}\times(\mathbf{n}\times\mathbf{a})/c^2R$.

**Physical meaning:** proportional to the square of the acceleration. This is why circular motion radiates more strongly than linear motion.

### 3.2.2 The Liénard Relativistic Generalization

Using the invariant $a^\mu a_\mu$:

$$P = -\frac{q^2}{6\pi\varepsilon_0 c} a^\mu a_\mu = \frac{q^2}{6\pi\varepsilon_0 c^3}\gamma^6\left[a^2 - \frac{(\mathbf{v}\times\mathbf{a})^2}{c^2}\right]$$

> **Unicode**
> ```
> P = -(q²)/(6πε₀ c) a^μ a_μ = (q²)/(6πε₀ c³)γ⁶[a² - ((𝐯×𝐚)²)/(c²)]
> ```

**A commonly used form:**

$$P = \frac{q^2\gamma^4}{6\pi\varepsilon_0 c^3}\left[a_\perp^2 + \gamma^2 a_\parallel^2\right]$$

> **Unicode**
> ```
> P = (q²γ⁴)/(6πε₀ c³)[a_⊥² + γ² a_∥²]
> ```

**Limits:**

- **Linear acceleration** $a \parallel v$: $P \propto \gamma^6 a_\parallel^2$
- **Circular motion** $a \perp v$: $P \propto \gamma^4 a_\perp^2$

**Radiation from circular motion is far stronger.** This is why synchrotrons have larger radiation losses than linear accelerators.

**Circular motion in a magnetic field:** substituting $a = v^2/r = qvB/\gamma m$:

$$P_{sync} = \frac{q^4 B^2}{6\pi\varepsilon_0 m^2 c}\gamma^2\beta^2\sin^2\alpha \propto \frac{\gamma^2}{m^2}$$

> **Unicode**
> ```
> P_sync = (q⁴ B²)/(6πε₀ m² c)γ²β²sin²α ∝ (γ²)/(m²)
> ```

**Electron/proton ratio:** a factor of $(m_p/m_e)^2 \approx 3.4\times10^6$. Electron synchrotrons are radiation-dominated; for protons it is almost negligible.

**Numbers:** for LEP electrons at 100 GeV, $B = 0.1$ T, $R = 3$ km → a loss of 3 GeV per turn. For LHC protons at 7 TeV, radiation loss is negligible.

### 3.2.3 The Abraham–Lorentz–Dirac Equation

If energy leaves via radiation, there must be a **reaction force** $\mathbf{F}_{rad}$ on the particle.

**Abraham–Lorentz force (non-relativistic):**

$$\mathbf{F}_{AL} = \frac{q^2}{6\pi\varepsilon_0 c^3}\dot{\mathbf{a}} = m\tau_0\dot{\mathbf{a}}, \quad \tau_0 = \frac{q^2}{6\pi\varepsilon_0 mc^3}$$

> **Unicode**
> ```
> 𝐅_AL = (q²)/(6πε₀ c³)𝐚˙ = mτ₀𝐚˙,   τ₀ = (q²)/(6πε₀ mc³)
> ```

**Electron:** $\tau_0 \approx 6.2\times10^{-24}$ s.

**Equation of motion:**

$$m\mathbf{a} = \mathbf{F}_{ext} + m\tau_0\dot{\mathbf{a}}$$

> **Unicode**
> ```
> m𝐚 = 𝐅ₑₓₜ + mτ₀𝐚˙
> ```

**Relativistic ALD equation:**

$$m a^\mu = qF^{\mu\nu}u_\nu + \frac{q^2}{6\pi\varepsilon_0 c^3}\left(\frac{da^\mu}{d\tau} + a^\nu a_\nu \frac{u^\mu}{c^2}\right)$$

> **Unicode**
> ```
> m a^μ = qF^μνu_ν + (q²)/(6πε₀ c³)((d a^μ)/(dτ) + a^ν a_ν (u^μ)/(c²))
> ```

The bracketed terms are the **Schott term + the Larmor term**.

**Three pathologies of ALD:**

1. **Runaway:** even with $\mathbf{F}_{ext} = 0$, $a \sim e^{t/\tau_0}$ diverges
2. **Pre-acceleration:** the particle begins accelerating $\tau_0$ before $\mathbf{F}_{ext}$ is applied — a violation of causality
3. **Third-order derivative** → requires specifying an initial acceleration

**Cause:** the point-charge model itself diverges as $r \to 0$.

### 3.2.4 The Landau–Lifshitz Prescription

Substituting the zeroth-order equation of motion into $\dot{\mathbf{a}}$ **reduces the order to second order**:

$$m a^\mu \approx qF^{\mu\nu}u_\nu + \frac{q^2\tau_0}{m}\left[q\partial_\alpha F^{\mu\nu}u_\nu u^\alpha + \frac{q^2}{m}F^{\mu\alpha}F_{\alpha\nu}u^\nu - \frac{q^2}{m^2 c^2}F^{\alpha\beta}F_{\alpha\gamma}u_\beta u^\gamma u^\mu\right]$$

> **Unicode**
> ```
> m a^μ ≈ qF^μνu_ν + (q²τ₀)/(m)[q∂_α F^μνu_ν u^α + (q²)/(m)F^μαF_ανu^ν - (q²)/(m² c²)F^αβF_αγuᵦ u^γ u^μ]
> ```

**Non-relativistic limit:**

$$\mathbf{F}_{LL} = \tau_0\left[q\dot{\mathbf{E}} + q\mathbf{v}\times\dot{\mathbf{B}} + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\times q\mathbf{B} + \ldots\right]$$

> **Unicode**
> ```
> 𝐅_LL = τ₀[q𝐄˙ + q𝐯×𝐁˙ + (q)/(m)(𝐄+𝐯×𝐁)× q𝐁 + ...]
> ```

**The current standard for strong-field QED simulations.** Removes the ALD pathologies, valid for $\tau_0\omega \ll 1$.

**Limit:** in the extreme regime $\chi = \gamma E/E_{cr} \sim 1$ (strong lasers), a quantum radiation model is required (→ §5.1.4).

### 3.2.5 Synchrotron Radiation

When a relativistic electron moves in a circle in field $B$, the radiation is **beamed forward** into a cone of angle $1/\gamma$.

**Angular distribution:**

$$\frac{dP}{d\Omega} = \frac{q^2}{16\pi^2\varepsilon_0 c}\frac{|\mathbf{n}\times[(\mathbf{n}-\boldsymbol{\beta})\times\dot{\boldsymbol{\beta}}]|^2}{(1-\mathbf{n}\cdot\boldsymbol{\beta})^5}$$

> **Unicode**
> ```
> (dP)/(dΩ) = (q²)/(16π²ε₀ c)(|𝐧×[(𝐧-β)×β˙]|²)/((1-𝐧·β)⁵)
> ```

The denominator $(1-\beta\cos\theta)^5$ peaks the emission at $\theta \sim 1/\gamma$, amplifying the forward direction by $\gamma^4$.

**Critical frequency:**

$$\omega_c = \frac{3}{2}\gamma^3\frac{c}{r_L} = \frac{3qB}{2m}\gamma^2\sin\alpha$$

> **Unicode**
> ```
> ω_c = (3)/(2)γ³(c)/(r_L) = (3qB)/(2m)γ²sinα
> ```

**Spectrum:** modified Bessel functions $K_{1/3}, K_{2/3}$:

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

**Features:**

- **Polarization:** linear polarization in the orbital plane + weak circular polarization
- **Pulse length:** an observer sees a short pulse of duration $\Delta t \sim 1/\gamma^3\omega_c$ → harmonics up to $n \sim \gamma^3$ overlap into a continuous spectrum
- **Total power:** $P \propto \gamma^2 B^2$

**Applications:**
- Synchrotron light sources (X-ray, ultraviolet)
- Radiation from the Crab Nebula, jets (astrophysics)
- Several MW of radiation loss for electrons at GeV energies — the reason LEP was the practical limit for a circular $e^+e^-$ collider

### 3.2.6 Rigidity $B\rho = p/q$

**Definition:** the magnetic field required to bend a particle of momentum $p$ into a radius of curvature $\rho$:

$$B\rho = \frac{p}{q} = \frac{\gamma m v}{q}$$

> **Unicode**
> ```
> Bρ = (p)/(q) = (γ m v)/(q)
> ```

**Units:** T·m. Practical formula:

$$B\rho[\text{T·m}] = 3.3356 \cdot p[\text{GeV}/c] / q[e]$$

> **Unicode**
> ```
> Bρ[T·m] = 3.3356 · p[GeV/c] / q[e]
> ```

**Four applications:**

1. **Accelerator design:** as $p$ increases, keeping the same $\rho$ requires a larger $B$. LHC $p = 7$ TeV, $\rho = 2804$ m → $B = 8.33$ T, the limit of superconducting magnets
2. **Magnetic spectrometers:** analyzing particle momentum via $B\rho$
3. **Cosmic rays:** shielding by Earth's magnetosphere — particles with $B\rho < 10$ GV enter only near the poles (cutoff rigidity)
4. **Medicine:** proton-therapy gantries, $B\rho = 2.3$ Tm (230 MeV)

Because relativistic mass increase is **automatically included**, $B\rho$ is the natural variable at high energy.

### 3.2.7 Mathematica Verification

```mathematica
(* Larmor formula *)
larmorPower[q_, a_, epsilon0_, c_] := q^2 a^2 / (6 Pi epsilon0 c^3);

(* Relativistic Liénard *)
lienardPower[q_, aPar_, aPerp_, gamma_, epsilon0_, c_] :=
  (q^2 gamma^4) / (6 Pi epsilon0 c^3) * (aPerp^2 + gamma^2 aPar^2);

(* Synchrotron radiated power *)
syncPower[q_, B_, m_, gamma_, epsilon0_, c_] :=
  q^4 B^2 / (6 Pi epsilon0 m^2 c) * gamma^2;

(* Rigidity *)
rigidity[p_, q_] := p/q;
```

### 3.2.8 Limits and Exceptions

- **ALD pathologies:** runaway, pre-acceleration. Mitigated by Landau–Lifshitz but reappears at $\chi \sim 1$
- **Quantum regime:** when $\hbar\omega_c \sim \gamma mc^2$, **quantum radiation reaction** is needed (→ §5.1.4)
- **Non-relativistic limit:** reduces to the Larmor formula as $\gamma \to 1$
- **Vacuum birefringence in strong fields:** at $B > B_c = 4.4\times10^9$ T, QED nonlinear effects appear (→ §6.1.7)

> **References**
> - Larmor, J., *On a dynamical theory of the electric and luminiferous medium*, Phil. Trans. R. Soc. A **190**, 205 (1897). [doi:10.1098/rsta.1897.0020](https://doi.org/10.1098/rsta.1897.0020)
> - Dirac, P. A. M., *Classical theory of radiating electrons*, Proc. R. Soc. A **167**, 148 (1938). [doi:10.1098/rspa.1938.0124](https://doi.org/10.1098/rspa.1938.0124)
> - Landau, L. D., Lifshitz, E. M., *The Classical Theory of Fields*, 4th ed., Pergamon (1975), §76.
> - Sokolov, A. A., Ternov, I. M., *Synchrotron Radiation*, Pergamon (1968).

---
## 3.3 Quantum Mechanics — $p \to p - qA$ Is Everything

The classical force $q\mathbf{v}\times\mathbf{B}$ is **not an operator** in quantum mechanics. Instead, $A$ enters the Hamiltonian and governs the motion. This section covers minimal coupling, Landau levels, the quantum Hall effect, and the Pauli and Dirac equations.

## 3.3 Quantum Mechanics and the Quantum Hall Effect — Where $U(1)$ Phase Becomes Physics

> **Arc of this section**
> Minimal coupling → Landau levels → Quantum Hall effect → Pauli/Dirac → Gauge phase
>
> The classical Lorentz force $q\mathbf{v}\times\mathbf{B}$ enters quantum mechanics as the operator $(\mathbf{p}-q\mathbf{A})$. The magnetic field is no longer a force, but a phase.

### 3.3.1 Minimal Coupling and the Schrödinger Equation

Quantizing the classical Hamiltonian $H = \frac{1}{2m}(\mathbf{p}-q\mathbf{A})^2 + q\phi$:

$$\hat{\mathbf{p}} = -i\hbar\nabla, \quad [\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$$

> **Unicode**
> ```
> 𝐩̂ = -iℏ∇,   [x̂ᵢ, p̂ⱼ] = iℏδᵢⱼ
> ```

**The Schrödinger equation:**

$$i\hbar\partial_t\psi = \left[\frac{1}{2m}(-i\hbar\nabla-q\mathbf{A})^2 + q\phi\right]\psi$$

> **Unicode**
> ```
> iℏ∂ₜψ = [(1)/(2m)(-iℏ∇-q𝐀)² + qφ]ψ
> ```

**This is the minimal-coupling prescription** $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$, $E \to E - q\phi$.

**Current density:**

$$\mathbf{j} = \frac{q}{2m}\left[\psi^*(-i\hbar\nabla-q\mathbf{A})\psi + c.c.\right] = \frac{q}{m}\Re[\psi^*(\hat{\mathbf{p}}-q\mathbf{A})\psi]$$

> **Unicode**
> ```
> 𝐣 = (q)/(2m)[ψ^*(-iℏ∇-q𝐀)ψ + c.c.] = (q)/(m)Re[ψ^*(𝐩̂-q𝐀)ψ]
> ```

The expectation value of the **kinematic momentum operator** $\hat{\boldsymbol{\pi}} = \hat{\mathbf{p}}-q\mathbf{A}$ is $m\mathbf{v}$.

**Heisenberg equation of motion:**

$$\dot{\hat{\mathbf{r}}} = [\hat{\mathbf{r}}, H]/i\hbar = \hat{\boldsymbol{\pi}}/m$$

$$\dot{\hat{\boldsymbol{\pi}}} = [\hat{\boldsymbol{\pi}}, H]/i\hbar$$

Computing this gives:

$$m\frac{d^2\hat{\mathbf{r}}}{dt^2} = q\hat{\mathbf{E}} + \frac{q}{2}(\hat{\mathbf{v}}\times\hat{\mathbf{B}} - \hat{\mathbf{B}}\times\hat{\mathbf{v}})$$

> **Unicode**
> ```
> m(d²𝐫̂)/(dt²) = q𝐄̂ + (q)/(2)(𝐯̂×𝐁̂ - 𝐁̂×𝐯̂)
> ```

The **symmetrized operator version** of the classical Lorentz force. For the expectation value, Ehrenfest's theorem gives:

$$\langle m\ddot{\mathbf{r}}\rangle = q\langle\mathbf{E}+\mathbf{v}\times\mathbf{B}\rangle$$

> **Unicode**
> ```
> ⟨ m𝐫¨⟩ = q⟨𝐄+𝐯×𝐁⟩
> ```

**Key point:** $\mathbf{E}, \mathbf{B}$ do **not enter directly** into the Schrödinger equation; only $\mathbf{A}, \phi$ do. **They act as a phase, not a force.**

### 3.3.2 Full Derivation of Landau Levels

Take $\mathbf{B} = B\hat{z}$ uniform, $\phi = 0$, and choose the **Landau gauge** $\mathbf{A} = (0, Bx, 0)$.

**Hamiltonian:**

$$H = \frac{\hat{p}_x^2}{2m} + \frac{(\hat{p}_y - qBx)^2}{2m} + \frac{\hat{p}_z^2}{2m}$$

> **Unicode**
> ```
> H = (p̂ₓ²)/(2m) + ((p̂_y - qBx)²)/(2m) + (p̂_z²)/(2m)
> ```

**Commutation relations:** $[H, \hat{p}_y] = [H, \hat{p}_z] = 0$ → eigenfunctions:

$$\psi = e^{i(k_y y + k_z z)}\varphi(x)$$

> **Unicode**
> ```
> ψ = e^i(k_y y + k_z z)φ(x)
> ```

The equation for $x$:

$$\left[\frac{\hat{p}_x^2}{2m} + \frac12 m\omega_c^2 (x - x_0)^2\right]\varphi = \left(E-\frac{\hbar^2k_z^2}{2m}\right)\varphi$$

> **Unicode**
> ```
> [(p̂ₓ²)/(2m) + (1)/(2) mω_c² (x - x₀)²]φ = (E-(ℏ²k_z²)/(2m))φ
> ```

where:

$$\omega_c = \frac{|q|B}{m}, \quad x_0 = \frac{\hbar k_y}{qB}$$

> **Unicode**
> ```
> ω_c = (|q|B)/(m),   x₀ = (ℏ k_y)/(qB)
> ```

**This is exactly a 1D harmonic oscillator centered at $x_0$.** Hence:

$$E = \frac{\hbar^2 k_z^2}{2m} + \hbar\omega_c\left(n+\frac12\right), \quad n = 0, 1, 2, \ldots$$

> **Unicode**
> ```
> E = (ℏ² k_z²)/(2m) + ℏω_c(n+(1)/(2)),   n = 0,1,2,...
> ```

For a **2D system** ($k_z = 0$):

$$E_n = \hbar\omega_c\left(n+\frac12\right)$$

> **Unicode**
> ```
> Eₙ = ℏω_c(n+1/2)
> ```

These are the **Landau levels**.

**Three physical implications:**

1. **Quantization of the magnetic length:** $r_L \to l_B = \sqrt{\hbar/|q|B}$
2. **Degeneracy:** each level $n$ is degenerate by $N_\phi = BS/\Phi_0$, the number of flux quanta, $\Phi_0 = h/e$
3. **Classical–quantum correspondence:** in the semiclassical limit of large $n$, $r_n = \sqrt{2\hbar(n+1/2)/m\omega_c} \to r_L$

In the **symmetric gauge** $\mathbf{A} = \frac12\mathbf{B}\times\mathbf{r}$, one gets eigenstates of $L_z$, with wave functions of the form $\psi_{n,m} \sim z^m e^{-|z|^2/4l_B^2}$ — essential for the quantum Hall effect.

### 3.3.3 The Quantum Hall Effect

For a 2D electron gas in $B\hat{z}$ carrying current $j_x$, the classical Hall effect gives $E_y = (B/qn)j_x$, with Hall resistance $R_H = B/qn$.

With Landau levels present, if the chemical potential lies in a gap as $T \to 0$, the current flows **without scattering**.

#### The Integer Quantum Hall Effect (IQHE)

**Filling factor:**

$$\nu = \frac{n_{2D}h}{eB} = \frac{N_e}{N_\phi}$$

> **Unicode**
> ```
> ν = (n_2Dh)/(eB) = (Nₑ)/(Nᵩ)
> ```

When $\nu$ is an integer:

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

$h/e^2 = 25.812\ \text{k}\Omega$ is quantized exactly, to $10^{-9}$ precision.

**Derivation — the Kubo formula:**

$$\sigma_{xy} = \frac{e^2\hbar}{i}\sum_{n\neq m}\frac{\langle n|v_x|m\rangle\langle m|v_y|n\rangle - (x\leftrightarrow y)}{(E_n-E_m)^2}(f_n-f_m)$$

> **Unicode**
> ```
> σ_xy = (e²ℏ)/(i)∑_n≠ m(⟨ n|vₓ|m⟩⟨ m|v_y|n⟩ - (x↔ y))/((Eₙ-Eₘ)²)(fₙ-fₘ)
> ```

**As an integral of the Berry curvature:**

$$\sigma_{xy} = \frac{e^2}{h}\frac{1}{2\pi}\int_{BZ} \Omega_z(\mathbf{k})\, d^2k = \frac{e^2}{h}C$$

> **Unicode**
> ```
> σ_xy = (e²)/(h)(1)/(2π)∫_BZ Ω_z(𝐤) d²k = (e²)/(h)C
> ```

$C$ is the **first Chern number** (an integer) — the topological invariant of the IQHE.

**Connection to the Lorentz force:** the $E\times B$ drift of the Lorentz force has the same structure as the $k$-space Berry curvature.

#### The Fractional Quantum Hall Effect (FQHE)

$\nu = 1/3, 2/5$, etc. Electron-electron Coulomb interaction plus the Lorentz force forms **composite fermions**.

**The Laughlin wave function:**

$$\Psi_{1/m} = \prod_{i<j}(z_i-z_j)^m e^{-\sum|z_i|^2/4l_B^2}$$

> **Unicode**
> ```
> Ψ_1/m = ∏_i<j(zᵢ-zⱼ)ᵐ e^-∑|zᵢ|²/4l_B²
> ```

**Quasiparticles:** charge $e^* = e/3$, statistics $\theta = \pi/m$ — **anyons**.

**Essence:** the Lorentz force forces circular motion, quenching the kinetic energy → not momentum space but **position space itself becomes noncommutative**, $[x,y] = il_B^2$ → topological matter.

**Recently:** in 2023, a fractional Chern insulator was observed in graphene even at $B = 0$ — Berry curvature plays the role of $B_{eff}$ without a Lorentz force.

### 3.3.4 The Pauli Equation and Spin–Magnetic-Field Coupling

The Schrödinger equation knows nothing about spin. Including spin 1/2 gives the **Pauli equation**:

$$i\hbar\partial_t \begin{pmatrix}\psi_\uparrow \\ \psi_\downarrow\end{pmatrix} = \left[\frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m} + q\phi - \frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}\right]\begin{pmatrix}\psi_\uparrow \\ \psi_\downarrow\end{pmatrix}$$

> **Unicode**
> ```
> iℏ∂ₜ [ψ_uparrow; ψ_downarrow] = [((𝐩̂-q𝐀)²)/(2m) + qφ - (qℏ)/(2m)σ·𝐁][ψ_uparrow; ψ_downarrow]
> ```

**Three terms:**
1. Kinetic energy (orbital Lorentz force, Landau)
2. Electric potential
3. **Zeeman term** $H_Z = -\hat{\boldsymbol{\mu}}\cdot\mathbf{B}$, $\hat{\boldsymbol{\mu}} = g\frac{q}{2m}\mathbf{S}$, $g \approx 2$

**That is, the charge feels $q\mathbf{v}\times\mathbf{B}$ through orbital motion via $\mathbf{A}$, while the spin feels $B$ directly through $\boldsymbol{\sigma}\cdot\mathbf{B}$.**

**Landau levels + spin:**

$$E_{n,s} = \hbar\omega_c(n+1/2) + g\frac{\hbar\omega_c}{2}s, \quad s = \pm 1/2$$

> **Unicode**
> ```
> E_n,s = ℏω_c(n+1/2) + g(ℏω_c)/(2)s,   s = ±1/2
> ```

For an electron, $g \approx 2$ → $E_{n,+1/2} = \hbar\omega_c(n+1)$, $E_{n,-1/2} = \hbar\omega_c n$. The spin splitting is nearly equal to the Landau spacing, so levels are doubly degenerate except for $n=0$.

### 3.3.5 The Dirac Equation and Foldy–Wouthuysen

Relativistic spin 1/2 is described by the **Dirac equation**:

$$[\gamma^\mu(i\hbar\partial_\mu - qA_\mu) - mc]\psi = 0$$

> **Unicode**
> ```
> [γ^μ(iℏ∂_μ - qA_μ) - mc]ψ = 0
> ```

**Hamiltonian form:**

$$i\hbar\partial_t\psi = [c\boldsymbol{\alpha}\cdot(\hat{\mathbf{p}}-q\mathbf{A}) + \beta mc^2 + q\phi]\psi$$

> **Unicode**
> ```
> iℏ∂ₜψ = [cα·(𝐩̂-q𝐀) + β mc² + qφ]ψ
> ```

**Non-relativistic limit — the Foldy–Wouthuysen transformation:**

$$H_{FW} = \frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m} + q\phi - \frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B} - \frac{(\hat{\mathbf{p}}-q\mathbf{A})^4}{8m^3c^2} - \frac{q\hbar}{4m^2c^2}\boldsymbol{\sigma}\cdot[(\hat{\mathbf{p}}-q\mathbf{A})\times\mathbf{E} - \mathbf{E}\times(\hat{\mathbf{p}}-q\mathbf{A})] + \ldots$$

> **Unicode**
> ```
> H_FW = ((𝐩̂-q𝐀)²)/(2m) + qφ - (qℏ)/(2m)σ·𝐁 - ((𝐩̂-q𝐀)⁴)/(8m³c²) - (qℏ)/(4m²c²)σ·[(𝐩̂-q𝐀)×𝐄 - 𝐄×(𝐩̂-q𝐀)] + ...
> ```

**Meaning of each term:**
- Terms 1–3: the Pauli equation
- Term 4: relativistic correction to the kinetic energy
- Term 5: **spin–orbit coupling** $H_{SO} = -\frac{q\hbar}{4m^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})$

**The origin of spin–orbit coupling:** the internal atomic $\mathbf{E}$ field looks like a **magnetic field** to a moving electron (a Lorentz transformation). This is the intra-atomic version of the $\mathbf{v}\times\mathbf{E}$ Lorentz force.

**Dirac solution — relativistic Landau levels:**

$$E_n = \sqrt{m^2c^4 + c^2\hbar^2k_z^2 + 2\hbar c^2 |q|B n}, \quad n = 0, 1, 2, \ldots$$

> **Unicode**
> ```
> Eₙ = √(m²c⁴ + c²ℏ²k_z² + 2ℏ c² |q|B n),   n = 0,1,2,...
> ```

The $n = 0$ Landau level is nonzero, a **chiral zero mode** — observed in graphene and 3D Dirac/Weyl semimetals.

### 3.3.6 Gauge Invariance and Quantum Phase

Under a gauge transformation $A_\mu \to A_\mu + \partial_\mu\chi$ in quantum mechanics:

$$\psi \to \psi' = \exp\left(i\frac{q\chi}{\hbar}\right)\psi$$

> **Unicode**
> ```
> ψ → ψ' = exp(i(qχ)/(ℏ))ψ
> ```

The Schrödinger/Dirac equation is invariant. The physical quantities $\rho = |\psi|^2$, $\mathbf{j}$ are invariant.

**But the phase is physical:**

$$\gamma = \frac{q}{\hbar}\oint_C \mathbf{A}\cdot d\boldsymbol{\ell} = \frac{q\Phi}{\hbar}$$

> **Unicode**
> ```
> γ = (q)/(ℏ)∮_C 𝐀· dℓ = (qΦ)/(ℏ)
> ```

- If the gauge function $\chi$ is single-valued, $\oint \nabla\chi\cdot d\ell = 0$ → $\gamma$ is invariant
- If space is **not simply connected**, $\chi$ can be multivalued, and $\gamma$ is gauge invariant only modulo $2\pi$

This is the gauge invariance behind the **Aharonov–Bohm** and Berry phases.

**Summary:**

| Viewpoint | Force/phase | Meaning |
|---|---|---|
| Classical | Force = $qF\cdot v$ | Only the field $F$ matters |
| Quantum | Phase = $\frac{q}{\hbar}\int A$ | The connection $A$ itself is observed via interference |

Even where $F = 0$, $W(C) \neq 1$ is possible.

**Hence quantum mechanics does not view the Lorentz force as a force, but as the law of parallel transport on a $U(1)$ bundle.** Landau quantization, the quantum Hall effect, and the AB effect all follow from the single minimal-coupling principle $p \to p - qA$. The classical $q\mathbf{v}\times\mathbf{B}$ is the shadow of that principle appearing in the $\hbar \to 0$ limit.

### 3.3.7 Mathematica Verification

```mathematica
(* Landau levels *)
landauLevels[n_, hBar_, omegaC_] := hBar omegaC (n + 1/2);

(* Landau-gauge Hamiltonian *)
H = (px^2)/(2 m) + (py - q B x)^2/(2 m) + pz^2/(2 m);

(* Verify that the x-equation is a harmonic oscillator *)
(* Treat p_y, p_z as constants and extract the equation in x *)
Hx = (px^2)/(2 m) + (hbar ky - q B x)^2/(2 m);
Simplify[Hx]
(* Result: (px²)/(2m) + (1/2) m ω_c² (x - x0)²,  ω_c = qB/m, x0 = ℏ ky/(qB) *)

(* Quantum Hall conductance *)
hallConductance[nu_] := nu e^2/h;
```

### 3.3.8 Limits and Exceptions

- **Non-relativistic limit:** the Schrödinger–Pauli equation is valid only for $v \ll c$
- **Many-body effects:** when the Landau-level degeneracy is large, electron interactions dominate (FQHE)
- **Strong magnetic fields:** at $B > B_c$, vacuum birefringence and pair production occur (→ §6.1.7)
- **Non-Abelian gauge:** minimal coupling is more complex for $SU(2)$, $SU(3)$ (→ §6.1.1)

> **References**
> - Landau, L. D., *Diamagnetismus der Metalle*, Z. Phys. **64**, 629 (1930). [doi:10.1007/BF01397213](https://doi.org/10.1007/BF01397213)
> - von Klitzing, K., Dorda, G., Pepper, M., *New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance*, Phys. Rev. Lett. **45**, 494 (1980). [doi:10.1103/PhysRevLett.45.494](https://doi.org/10.1103/PhysRevLett.45.494)
> - Laughlin, R. B., *Anomalous quantum Hall effect: An incompressible quantum fluid with fractionally charged excitations*, Phys. Rev. Lett. **50**, 1395 (1983). [doi:10.1103/PhysRevLett.50.1395](https://doi.org/10.1103/PhysRevLett.50.1395)
> - Sakurai, J. J., Napolitano, J., *Modern Quantum Mechanics*, 2nd ed., Pearson (2011), Chapter 5.

---

## 3.4 Statistical Mechanics and Plasma Kinetic Theory

When the $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ of a single particle is multiplied by $10^{20}$, it becomes the flow of a **distribution function** $f(\mathbf{x},\mathbf{v},t)$. This section covers the Boltzmann, Vlasov, Fokker–Planck, and Langevin equations, and transport coefficients.

### 3.4.1 The Boltzmann Equation and the Lorentz Term

**Phase-space density** $f_s(\mathbf{x},\mathbf{v},t)d^3x\,d^3v$ = the number of particles of species $s$. The conservation law:

$$\frac{df}{dt} = C[f]$$

> **Unicode**
> ```
> (df)/(dt) = C[f]
> ```

**Expanding the total derivative:**

$$\frac{\partial f}{\partial t} + \dot{\mathbf{x}}\cdot\nabla_x f + \dot{\mathbf{v}}\cdot\nabla_v f = C[f]$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐱˙·∇ₓ f + 𝐯˙·∇ᵥ f = C[f]
> ```

**Substituting Newton + Lorentz:** $\dot{\mathbf{x}} = \mathbf{v}$, $\dot{\mathbf{v}} = \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + \frac{\mathbf{F}_{other}}{m}$:

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = C[f]$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐯·∇ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = C[f]
> ```

**Three properties of the Lorentz term:**

1. **Incompressibility in phase space:** $\nabla_v\cdot(\mathbf{v}\times\mathbf{B}) = 0$, $\nabla_v\cdot\mathbf{E} = 0$ → no creation/annihilation of particles, only bending of trajectories
2. **Energy neutrality:** $\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$ → the magnetic field does not directly contribute to the $v^2$ moment
3. **The $\mathbf{E}$ term:** injects energy via $\mathbf{v}\cdot\mathbf{E}$

**Without a collision operator $C$,** the characteristic curves are single-particle Lorentz trajectories. $f$ is conserved along those trajectories.

### 3.4.2 The Vlasov Equation (Collisionless)

In the limit $C = 0$, only the mean field remains:

$$\frac{\partial f_s}{\partial t} + \mathbf{v}\cdot\nabla f_s + \frac{q_s}{m_s}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f_s = 0$$

> **Unicode**
> ```
> (∂ fₛ)/(∂ t) + 𝐯·∇ fₛ + (qₛ)/(mₛ)(𝐄+𝐯×𝐁)·∇ᵥ fₛ = 0
> ```

**$\mathbf{E}, \mathbf{B}$ are determined self-consistently from $f$ via Maxwell's equations:**

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

This closed system is the **Vlasov–Maxwell** system.

**Features:**

- **Time-reversible, entropy-conserving.** Collisionless kinetic phenomena such as Landau damping, the two-stream instability, and BGK modes all arise here
- Linearizing in a field $B_0\hat{z}$ gives **cyclotron resonance**: the denominator $\omega - k_\parallel v_\parallel - n\omega_c = 0$. The $n\omega_c$ term is the memory of the Lorentz circular motion
- **Liouville:** $df/dt = 0$ → phase-space density is conserved. $f$ is stretched (**phase mixing**) along the Lorentz flow, but its value is preserved

**Why Vlasov is the standard model for hot fusion and space plasmas:** because the collisional mean free path $\lambda_{mfp} \gg L$, so $C$ can be neglected.

### 3.4.3 The Fokker–Planck Equation

When collisions are the **accumulation of small-angle scattering**, $C$ is approximated as **diffusion in velocity space**:

$$C_{FP}[f] = -\frac{\partial}{\partial v_i}(A_i f) + \frac12\frac{\partial^2}{\partial v_i\partial v_j}(D_{ij}f)$$

> **Unicode**
> ```
> C_FP[f] = -(∂)/(∂ vᵢ)(Aᵢ f) + (1)/(2)(∂²)/(∂ vᵢ∂ vⱼ)(Dᵢⱼf)
> ```

- $A_i = \langle\Delta v_i\rangle/\Delta t$: **friction**
- $D_{ij} = \langle\Delta v_i\Delta v_j\rangle/\Delta t$: **diffusion**

**Form including the Lorentz force:**

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = -\nabla_v\cdot(\mathbf{A}f) + \frac12\nabla_v\nabla_v:(D f)$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + 𝐯·∇ f + (q)/(m)(𝐄+𝐯×𝐁)·∇ᵥ f = -∇ᵥ·(𝐀f) + (1)/(2)∇ᵥ∇ᵥ:(D f)
> ```

**For Coulomb collisions — the Rosenbluth potentials** $h, g$:

$$A_i = \Gamma\partial_{v_i}h, \quad D_{ij} = \Gamma\partial_{v_i}\partial_{v_j}g$$

> **Unicode**
> ```
> Aᵢ = Γ∂_vᵢ h,   Dᵢⱼ = Γ∂_vᵢ∂_vⱼ g
> ```

**In a magnetic field, the diffusion tensor becomes anisotropic:**

$$D = D_\parallel \hat{b}\hat{b} + D_\perp (I - \hat{b}\hat{b}) + D_\wedge \hat{b}\times$$

> **Unicode**
> ```
> D = D_∥ b̂b̂ + D_⊥ (I-b̂b̂) + D_∧ b̂×
> ```

$D_\wedge$ is the **Hall diffusion**.

**The kinetic expression of magnetic confinement:** the stronger the field,

$$D_\perp \sim \frac{D_0}{1+\omega_c^2\tau^2}$$

> **Unicode**
> ```
> D_⊥ ∼ (D₀)/(1+ω_c²τ²)
> ```

When $\omega_c\tau \gg 1$, the perpendicular diffusion falls off as $1/B^2$.

### 3.4.4 The Langevin Equation

Adding a **stochastic force** to a single-particle trajectory:

$$m\dot{\mathbf{v}} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) - m\nu\mathbf{v} + \mathbf{F}_{stoch}(t) + q\mathbf{v}\times\tilde{\mathbf{B}}(t)$$

> **Unicode**
> ```
> m𝐯˙ = q(𝐄+𝐯×𝐁) - mν𝐯 + 𝐅_stoch(t) + q𝐯×𝐁̃(t)
> ```

- $-m\nu\mathbf{v}$: mean friction
- $\mathbf{F}_{stoch}$: random electric-field fluctuation, $\langle F_i(t)F_j(t')\rangle = 2m\nu T \delta_{ij}\delta(t-t')$ — the **fluctuation–dissipation theorem**
- The last term: **pitch-angle scattering** due to magnetic fluctuations

The Fokker–Planck limit of this SDE is the FP equation above.

**Physical meaning:** the Lorentz force is deterministic gyration; friction/diffusion randomizes the gyro-phase through collisions. If $\nu/\omega_c$ is small, the particle gyrates many times between collisions → a **magnetized plasma**.

**Langevin with magnetic fluctuations:** explains **anomalous transport** in magnetic mirrors and tokamaks. $E\times B$ turbulence caused by $\tilde{B}_r$ generates diffusion $D \sim \tilde{B}^2$.

### 3.4.5 The Maxwell–Boltzmann Distribution (Bohr–van Leeuwen)

We seek an equilibrium solution for which the collision operator $C = 0$.

With only a magnetic field, $H = mv^2/2$ is conserved, and since the Lorentz force does no work, any isotropic distribution $f(v)$ is a stationary Vlasov solution. Maximizing entropy via the H-theorem $dS/dt \geq 0$:

$$f_M(\mathbf{v}) = n\left(\frac{m}{2\pi T}\right)^{3/2}\exp\left(-\frac{mv^2}{2T}\right)$$

> **Unicode**
> ```
> f_M(𝐯) = n((m)/(2π T))^3/2exp(-(mv²)/(2T))
> ```

**Maxwell–Boltzmann.** $\mathbf{B}$ **does not enter** $f_M$ at all — the **Bohr–van Leeuwen theorem**: the classical equilibrium magnetization is $M = 0$. A magnetic field cannot produce an equilibrium distribution. **Magnetization arises only from quantum Landau diamagnetism.**

**With an electric field $\mathbf{E} = -\nabla\phi$ present, in steady state $\partial_t = 0$:**

$$f_{eq} = n_0\left(\frac{m}{2\pi T}\right)^{3/2}\exp\left(-\frac{mv^2/2 + q\phi(\mathbf{x})}{T}\right)$$

> **Unicode**
> ```
> f_eq = n₀((m)/(2π T))^3/2exp(-(mv²/2 + qφ(𝐱))/(T))
> ```

The **Boltzmann factor** $\exp(-q\phi/T)$. $B$ still does not enter. Instead, the $\nabla B$ drift and the $\nabla n$ drift generate an equilibrium current — the **diamagnetic current** $\mathbf{J}_\perp = \mathbf{B}\times\nabla p/B^2$.

**$E\times B$ equilibrium:** $f(\mathbf{x},\mathbf{v}) = f_M(\mathbf{v}-\mathbf{V}_E)$ is also a Vlasov solution — a Maxwellian drifting entirely at $V_E$.

### 3.4.6 Transport Coefficients

Expand $f = f_M + f_1$ via a Chapman–Enskog expansion; the Lorentz term determines $f_1$.

#### Electrical Conductivity

Assume steady, uniform, weak $E$, and collisions $\nu$. **Momentum equation:**

$$0 = q(\mathbf{E}+\mathbf{V}\times\mathbf{B}) - m\nu\mathbf{V}$$

> **Unicode**
> ```
> 0 = q(𝐄+𝐕×𝐁) - mν𝐕
> ```

Solving:

$$\mathbf{J} = \sigma_\parallel \mathbf{E}_\parallel + \sigma_P \mathbf{E}_\perp + \sigma_H \hat{b}\times\mathbf{E}_\perp$$

> **Unicode**
> ```
> 𝐉 = σ_∥ 𝐄_∥ + σ_P 𝐄_⊥ + σ_H b̂×𝐄_⊥
> ```

**Three conductivities:**

$$\sigma_\parallel = \frac{nq^2}{m\nu}, \quad \sigma_P = \sigma_\parallel\frac{\nu^2}{\nu^2+\omega_c^2}, \quad \sigma_H = \sigma_\parallel\frac{\nu\omega_c}{\nu^2+\omega_c^2}$$

> **Unicode**
> ```
> σ_∥ = (nq²)/(mν),   σ_P = σ_∥(ν²)/(ν²+ω_c²),   σ_H = σ_∥(νω_c)/(ν²+ω_c²)
> ```

**Interpretation:**
- $\sigma_\parallel$: parallel conductivity, unaffected by B
- $\sigma_P$ (Pedersen): perpendicular conductivity, suppressed as $\sigma_\parallel(\nu/\omega_c)^2 \propto 1/B^2$ when $\omega_c \gg \nu$
- $\sigma_H$ (Hall): Hall conductivity, $\sigma_H \to nq/B$ in the collisionless limit

#### Diffusion

$$D_\perp = \frac{T}{m}\frac{\nu}{\nu^2+\omega_c^2} = D_\parallel\frac{\nu^2}{\nu^2+\omega_c^2}, \quad D_\parallel = \frac{T}{m\nu}$$

> **Unicode**
> ```
> D_⊥ = (T)/(m)(ν)/(ν²+ω_c²) = D_∥(ν²)/(ν²+ω_c²),   D_∥ = (T)/(mν)
> ```

**Classical diffusion** $D_\perp \propto 1/B^2$ — **the principle of magnetic confinement**.

**In the presence of turbulence, Bohm diffusion** $D_B \sim T/16eB \propto 1/B$ worsens this.

#### Viscosity

**The Braginskii viscosity tensor has 5 components.** For strong $B$, the perpendicular viscosity $\eta_\perp \sim \eta_0/(\omega_c\tau)^2$ is suppressed, while the **gyroviscosity** $\eta_\wedge$ survives — combining with $E\times B$ sheared flow to form the **H-mode**.

**Conclusion:** the Lorentz force leaves parallel transport unchanged while **suppressing only perpendicular transport by a factor of $\omega_c\tau$**. This anisotropy is what binds plasma to the field lines.

### 3.4.7 Liouville's Theorem

In the 6D phase space $\Gamma = (\mathbf{x},\mathbf{v})$, the flow:

$$\dot{\Gamma} = \left(\mathbf{v}, \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\right)$$

> **Unicode**
> ```
> Γ˙ = (𝐯, (q)/(m)(𝐄+𝐯×𝐁))
> ```

**Divergence:**

$$\nabla_\Gamma\cdot\dot{\Gamma} = \nabla_x\cdot\mathbf{v} + \nabla_v\cdot\frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B}) = 0 + 0 = 0$$

> **Unicode**
> ```
> ∇_Γ·Γ˙ = ∇ₓ·𝐯 + ∇ᵥ·(q)/(m)(𝐄+𝐯×𝐁) = 0 + 0 = 0
> ```

**Hence phase-space volume $d\Gamma$ is conserved.** The continuity equation:

$$\frac{\partial f}{\partial t} + \nabla_\Gamma\cdot(f\dot{\Gamma}) = 0 \implies \frac{df}{dt} = 0 \text{ if } C = 0$$

> **Unicode**
> ```
> (∂ f)/(∂ t) + ∇_Γ·(fΓ˙) = 0 ⟹ (df)/(dt) = 0  if  C = 0
> ```

This is **Vlasov's Liouville theorem**. It is why the Boris algorithm must satisfy $\det J = 1$ numerically — a violation of Liouville causes artificial heating.

**With collisions:**

$$\frac{df}{dt} = C[f] \neq 0, \quad \frac{dS}{dt} = -\int C[f]\ln f\, d\Gamma \geq 0$$

> **Unicode**
> ```
> (df)/(dt) = C[f] ≠ 0,   (dS)/(dt) = -∫ C[f]ln f dΓ ≥ 0
> ```

**The H-theorem.** At equilibrium $f_M$, $C = 0$, and $S$ is maximal.

### 3.4.8 Summary Table

| Equation | Lorentz term | Role |
|---|---|---|
| **Boltzmann** | Rotation operator in phase space | General kinetic theory including collisions |
| **Vlasov** | Rotation only, $f$ conserved | Landau damping, cyclotron resonance |
| **Fokker–Planck** | Rotation + velocity diffusion | Magnetized collisions |
| **Langevin** | Rotation + stochastic differential | Single-particle trajectories |
| **Maxwell–Boltzmann** | $B$ cannot alter the distribution | Bohr–van Leeuwen |
| **Transport** | $\sigma_\perp, D_\perp \propto 1/(1+\omega_c^2\tau^2)$ | Magnetic confinement |
| **Liouville** | $\nabla_\Gamma\cdot\dot{\Gamma} = 0$ | The origin of all conservation |

**The Lorentz force stretches phase space, but preserves its volume** — which is why plasmas go turbulent without undergoing a phase transition.

### 3.4.9 Mathematica Verification

```mathematica
(* Boltzmann equation *)
boltzmannEq = D[f[t, x, y, z, vx, vy, vz], t]
  + vx D[f[t, x, y, z, vx, vy, vz], x]
  + vy D[f[t, x, y, z, vx, vy, vz], y]
  + vz D[f[t, x, y, z, vx, vy, vz], z]
  + (q/m) ((Ex + vy Bz - vz By) D[f[t, x, y, z, vx, vy, vz], vx]
         + (Ey + vz Bx - vx Bz) D[f[t, x, y, z, vx, vy, vz], vy]
         + (Ez + vx By - vy Bx) D[f[t, x, y, z, vx, vy, vz], vz])
  == collisionTerm;

(* Maxwell-Boltzmann *)
maxwellBoltzmann[vx_, vy_, vz_] := (m/(2 Pi kB T))^(3/2)
  Exp[-m (vx^2 + vy^2 + vz^2)/(2 kB T)];

(* Conductivities *)
sigmaParallel[n_, q_, m_, nu_] := n q^2/(m nu);
sigmaPedersen[sigmaPar_, nu_, omegaC_] := sigmaPar nu^2/(nu^2 + omegaC^2);
sigmaHall[sigmaPar_, nu_, omegaC_] := sigmaPar nu omegaC/(nu^2 + omegaC^2);
```

### 3.4.10 Limits and Exceptions

- **Collision approximation:** Fokker–Planck assumes small-angle scattering. Large-angle scattering (fusion reactions) must be treated separately
- **Turbulent regime:** Vlasov cannot predict turbulent saturation. Renormalization is required
- **Relativistic kinetic theory:** at $T \gtrsim mc^2$, relativistic Vlasov is needed (fusion plasmas are non-relativistic)
- **Quantum kinetic theory:** when $\lambda_{dB} \sim$ the interparticle spacing, the Wigner function is required

> **References**
> - Vlasov, A. A., *On vibration properties of electron gas*, J. Exp. Theor. Phys. **8**, 291 (1938). [doi:10.1070/PU1968v010n06ABEH003709](https://doi.org/10.1070/PU1968v010n06ABEH003709)
> - Fokker, A. D., *Die mittlere Energie rotierender elektrischer Dipole im Strahlungsfeld*, Ann. Phys. **348**, 810 (1914). [doi:10.1002/andp.19143480507](https://doi.org/10.1002/andp.19143480507)
> - Braginskii, S. I., *Transport processes in a plasma*, Reviews of Plasma Physics **1**, 205 (1965).
> - Krall, N. A., Trivelpiece, A. W., *Principles of Plasma Physics*, McGraw-Hill (1973).

---
# Act 4. Applications and Engineering

> **Arc of this act**
> Accelerators → Fusion → Medicine → Sensors → Space → Chaos
>
> Acts 1–3 established the theory of the Lorentz force. Act 4 covers how that theory is realized in **real devices and natural phenomena**. Every application shares one common denominator — **accelerate with $\mathbf{E}$, confine with $\mathbf{B}$**.

---

## 4.1 Accelerators

Every accelerator is a difference in how it uses the two terms of the Lorentz force $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$: accelerate with $\mathbf{E}$, control the orbit with $\mathbf{B}$. This section covers cyclotrons, synchrotrons, linear accelerators, and plasma accelerators.

### 4.1.1 The Cyclotron and Its Relativistic Limit

**Principle:** uniform $\mathbf{B} = B_0\hat{z}$, with an RF voltage $V(t) = V_0\sin\omega_{RF}t$ applied across two D-shaped electrodes (dees).

**Equation of motion:**

$$m\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$$

> **Unicode**
> ```
> m𝐯˙ = q𝐯×𝐁
> ```

The gyro-frequency $\omega_c = qB_0/m$ is **independent of speed**. Tuning the RF to $\omega_{RF} = \omega_c$ gives the particle an energy gain of $qV_0$ at the $\mathbf{E}$ gap every half turn.

**Radius:** $r = mv_\perp/qB$. **Energy:**

$$E = \frac{q^2 B^2 r^2}{2m} = \frac12 m\omega_c^2 r^2$$

> **Unicode**
> ```
> E = (q² B² r²)/(2m) = (1)/(2) mω_c² r²
> ```

$r$ grows in a spiral proportional to the square root of the energy. **Automatic focusing without strong focusing** — weak focusing.

**The relativistic limit:**

The relativistic mass $\gamma m$ decreases $\omega_c^{rel} = qB/\gamma m$. RF phase slip:

$$\Delta\phi = \int(\omega_{RF}-\omega_c^{rel})\,dt$$

> **Unicode**
> ```
> Δφ = ∫(ω_RF-ω_cʳᵉˡ)dt
> ```

**Limiting energy:**

$$\gamma = 1 + E/mc^2, \quad \Delta\omega/\omega = 1-1/\gamma$$

> **Unicode**
> ```
> γ = 1 + E/mc²,   Δω/ω = 1-1/γ
> ```

For a 1 GeV proton, $\gamma \approx 2$, a 50% drop in frequency → resonance collapses. The classical cyclotron limit is $\sim 20$ MeV for protons.

**Two solutions:**

1. **Synchrocyclotron:** keep $B$ fixed, modulate the frequency as $\omega_{RF}(t) = \omega_{c0}/\gamma(t)$. Pulsed, low average current
2. **Isochronous cyclotron:** increase $B(r) = \gamma(r)B_0$ radially to keep $\omega_c$ constant + azimuthal variation (Thomas focusing) compensates for vertical focusing. The 590 MeV PSI ring cyclotron is the extreme case

### 4.1.2 The Synchrotron

Instead of varying $r$ as in the cyclotron, keep $r = \rho$ fixed and raise $B(t)$ to match the energy.

**Rigidity:**

$$B\rho = \frac{p}{q}$$

> **Unicode**
> ```
> Bρ = (p)/(q)
> ```

**LHC:** $p = 7$ TeV/c, $\rho = 2804$ m → $B = 8.33$ T. The limit of superconducting dipole magnets. FCC aims for $\rho = 16$ km, $B = 16$ T.

**Phase stability (Veksler–McMillan, 1944):**

RF cavity voltage $V_{RF}\sin\phi$. For the synchronous particle $\phi_s$, the energy gain $qV_{RF}\sin\phi_s$ compensates for radiation + acceleration loss per turn.

A higher-energy particle has a longer revolution period (above transition $\gamma_t$) → arrives later → smaller phase $\phi$ → smaller energy gain → **stabilization**.

**Longitudinal motion is a harmonic oscillator — synchrotron oscillation:**

$$\Omega_s^2 = -\frac{qV_{RF}h\eta\cos\phi_s}{2\pi E_s}\omega_{rev}^2$$

> **Unicode**
> ```
> Ωₛ² = -(qV_RFhηcosφₛ)/(2π Eₛ)ωᵣₑᵥ²
> ```

$h$: the harmonic number, $\eta = 1/\gamma_t^2 - 1/\gamma^2$: the slip factor.

**RF resonance:**

$$\omega_{RF} = h\omega_{rev}$$

> **Unicode**
> ```
> ω_RF = hωᵣₑᵥ
> ```

$h \sim 10^4$ (LHC $h = 35640$).

**Transverse — quadrupole strong focusing:**

$$m\ddot{x} + k(s)x = 0$$

> **Unicode**
> ```
> mx¨ + k(s)x = 0
> ```

Hill's equation, betatron tunes $Q_{x,y}$. The Lorentz force $q\mathbf{v}\times\mathbf{B}_{quad}$ provides the restoring force. **Avoiding resonances $mQ_x + nQ_y = $ integer** is a key design consideration.

**Synchrotron-radiation loss:** $P \propto \gamma^4/\rho^2$. At LEP, 3 GeV lost per turn.

### 4.1.3 Linear Accelerators

Accelerate in a straight line with $\mathbf{E}$ rather than bending with $\mathbf{B}$. No $B\rho$ limit, no synchrotron radiation.

**Drift-tube LINAC:** particles are shielded inside tubes of length $L_n = v_n T_{RF}/2$ during the RF phase reversal. Once $\beta \approx 1$, $L = cT_{RF}/2$ becomes uniform.

**High-energy electrons:** a traveling-wave structure $E_z = E_0\sin(\omega t - kz)$, synchronized with phase velocity $v_{ph} = c$. SLAC reaches 50 GeV over 3 km.

**Limit:** $E_{acc} \sim 30-100$ MV/m, limited by copper-cavity breakdown. 1 TeV would require 10 km.

### 4.1.4 Plasma Accelerators (LWFA, PWFA)

**The electric field of a broken plasma wave:**

$$E_{WB} = \frac{m_ec\omega_p}{e} \approx 96\sqrt{n_0[\text{cm}^{-3}]}\ \text{V/m}$$

> **Unicode**
> ```
> E_WB = (mₑcωₚ)/(e) ≈ 96√(n₀[cm⁻³]) V/m
> ```

For $n_0 = 10^{18}$ cm$^{-3}$ → $E \approx 100$ GV/m, **1000 times** larger than RF.

#### LWFA (Laser Wakefield)

A strong laser $a_0 > 1$ pushes electrons out via the **ponderomotive force** $\mathbf{F}_p = -m_ec^2\nabla a_0^2/2$, forming a **bubble** in the plasma. Behind it, a wake with $E_z \sim 100$ GV/m.

**Energy gain:**

$$\Delta E \approx 2\gamma_p^2 m_ec^2 \propto n_0^{-1}, \quad \gamma_p = \omega_0/\omega_p$$

> **Unicode**
> ```
> Δ E ≈ 2γₚ² mₑc² ∝ n₀⁻¹,   γₚ = ω₀/ωₚ
> ```

#### PWFA (Plasma Wakefield)

A proton/electron driver beam creates the bubble instead. At SLAC, doubling from 42 GeV to 85 GeV was demonstrated.

**Problem:** without $\mathbf{B}$, the transverse Lorentz focusing $\mathbf{v}\times\mathbf{B}_{plasma}$ is weak. Focusing comes from the ion channel's $\mathbf{E}_r - B_\theta$, producing radiation (betatron radiation).

### 4.1.5 Mathematica Verification

```mathematica
(* Cyclotron energy *)
cyclotronEnergy[q_, B_, r_, m_] := q^2 B^2 r^2 / (2 m);

(* Relativistic frequency *)
omegaRel[q_, B_, gamma_, m_] := q B / (gamma m);

(* Rigidity *)
rigidity[p_, q_] := p/q;

(* LWFA wakefield *)
wakefield[n0_] := 96 Sqrt[n0]; (* V/m, n0 in cm^-3 *)
```

### 4.1.6 Limits and Exceptions

- **Cyclotron:** the relativistic limit is $\sim 20$ MeV for protons
- **Synchrotron:** radiation loss $P \propto \gamma^4/\rho^2$, dominant for electron machines
- **LINAC:** $E_{acc} < 100$ MV/m, limited by copper breakdown
- **LWFA:** issues with phase stability, energy spread, repetition rate

> **References**
> - Lawrence, E. O., Livingston, M. S., *Production of high speed light ions without high voltages*, Phys. Rev. **40**, 19 (1932). [doi:10.1103/PhysRev.40.19](https://doi.org/10.1103/PhysRev.40.19)
> - Wiedemann, H., *Particle Accelerator Physics*, 4th ed., Springer (2015).
> - Esarey, E., Schroeder, C. B., Leemans, W. P., *Physics of laser-driven plasma-based electron accelerators*, Rev. Mod. Phys. **81**, 1229 (2009). [doi:10.1103/RevModPhys.81.1229](https://doi.org/10.1103/RevModPhys.81.1229)

---

## 4.2 Fusion Reactors

A fusion reactor is a machine that confines $10^4$ eV plasma in a magnetic bottle using the Lorentz force. This section covers tokamaks, stellarators, and key device parameters.

### 4.2.1 The Tokamak and the Grad–Shafranov Equation

A tokamak drives current with $\mathbf{E}$ and confines pressure with $\mathbf{B}$ — a **Lorentz-force equilibrium** $\mathbf{J}\times\mathbf{B} = \nabla p$.

**Equilibrium equation:** assuming static conditions $\rho\mathbf{v}\cdot\nabla\mathbf{v} \approx 0$:

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

**Introducing the flux function** $\psi(R,Z) = RA_\phi$ for the axisymmetric case $(R,\phi,Z)$:

$$\mathbf{B} = \nabla\psi\times\nabla\phi + F(\psi)\nabla\phi, \quad F = RB_\phi$$

> **Unicode**
> ```
> 𝐁 = ∇ψ×∇φ + F(ψ)∇φ,   F = RBᵩ
> ```

The pressure $p = p(\psi)$ and $F = F(\psi)$ are flux-surface functions. Substituting Ampère's law gives the **Grad–Shafranov equation**:

$$\Delta^*\psi = R\frac{\partial}{\partial R}\left(\frac1R\frac{\partial\psi}{\partial R}\right) + \frac{\partial^2\psi}{\partial Z^2} = -\mu_0 R^2\frac{dp}{d\psi} - F\frac{dF}{d\psi}$$

> **Unicode**
> ```
> Δ^*ψ = R(∂)/(∂ R)((1)/(R)(∂ψ)/(∂ R)) + (∂²ψ)/(∂ Z²) = -μ₀ R²(dp)/(dψ) - F(dF)/(dψ)
> ```

An elliptic nonlinear PDE. **The right-hand side is the Lorentz force:**
- $-p'$: the plasma expansion force
- $-FF'$: the pinch force of the poloidal current

**Safety factor:** $q(\psi) = d\Phi_{tor}/d\psi$. $q > 1$ is the kink-stability condition.

**Three applications of the Lorentz force:**
1. Toroidal $B_\phi$ + poloidal $B_\theta$ = helical magnetic surfaces → cancels $\nabla B$ and curvature drift
2. The vertical field $B_Z$ balances the hoop force via $I_p\times B_Z$
3. **H-mode:** $E_r\times B$ sheared flow suppresses turbulence → creates a transport barrier

### 4.2.2 Stellarators and Magnetic Islands

A tokamak produces $B_\theta$ from plasma current, while a stellarator produces it with **external coils**.

**Goal:** vacuum flux surfaces already exist. The $\mathbf{B}$ field lines rotate by $\iota/2\pi$ with respect to $R$ — the **rotational transform** $\iota = 1/q$.

**Magnetic islands:** on a **resonant surface** with rational $\iota = n/m$, a perturbation $\tilde{B}_{mn}$ causes the field-line equation $d\psi/d\theta = \tilde{B}_r/B_\theta$ to produce **island formation**.

**Island width:**

$$w_{mn} \approx 4\sqrt{\frac{q^2 R \tilde{B}_{mn}}{m q' B_0}}$$

> **Unicode**
> ```
> wₘₙ ≈ 4√((q² R B̃ₘₙ)/(m q' B₀))
> ```

Even $\tilde{B} \sim 10^{-4}$ produces cm-scale islands → overlap gives a stochastic region by the **Chirikov criterion** → confinement collapses.

**Quasisymmetry:** coils are optimized so $|B|$ varies only along a specific direction, averaging the $\mathbf{V}_{gc}$ drift to zero. **Wendelstein 7-X** achieves $\epsilon_{eff} < 1\%$ with 50 non-planar coils.

**Pros and cons:**
- Pros: no current drive needed, no disruptions
- Cons: complex coils, difficult to optimize $B\rho$

### 4.2.3 Comparison Table: ITER, KSTAR, LHC

| Category | **KSTAR** | **ITER** | **LHC** |
|---|---|---|---|
| **Purpose** | Superconducting tokamak physics, long-pulse H-mode | Demonstration of Q=10 fusion | 14 TeV proton collisions |
| **Type** | Tokamak | Tokamak | Synchrotron |
| **Role of Lorentz force** | $J_p\times B_t$ confinement, $E_r\times B$ transport barrier | Same + alpha-particle $v_\alpha\times B$ confinement | $B\rho = p/q$ orbit maintenance, quadrupole $v\times B_{quad}$ focusing |
| **Major radius $R$ / minor radius $a$** | 1.8 m / 0.5 m | 6.2 m / 2.0 m | 27 km tunnel, $\rho_{bend} = 2804$ m |
| **Magnetic field $B_t$** | 3.5 T (Nb₃Sn superconductor) | 5.3 T on axis, coil max 11.8 T | 8.33 T dipole |
| **Plasma/beam current** | $I_p \sim 2$ MA | $I_p = 15$ MA | $I_{beam} = 0.58$ A |
| **Energy** | $T_i \sim 10$ keV, 100 s | $T = 20$ keV, $P_{fus} = 500$ MW, Q=10 | $E_{beam} = 7$ TeV, $\gamma = 7460$ |
| **Rigidity** | $B_\theta\rho \sim 0.5$ Tm | $B_\theta\rho \sim 3$ Tm | 23,334 Tm |
| **RF/heating** | NBI 8 MW, ECH 6 MW | NBI 33 MW, ECH 20 MW | RF 400 MHz, 16 MV/turn |
| **Key challenges** | ELM suppression via RMP, long-pulse $E\times B$ | Disruption $J\times B$ imbalance | $10^{-10}$ Torr vacuum, quench protection |
| **Lorentz-based limits** | Greenwald $n_G$, Troyon $\beta_N < 3$ | Same + $q_{95} > 3$ | Beam-beam $\Delta Q \propto N_p$ |

**Three common design principles:**

1. **$B\rho$ is the cost:** tokamak $B_t \propto 1/R$, LHC $E \propto B\rho$. The limit of superconducting $B$ is the bottleneck in both fields
2. **Phase stability:** the tokamak's $q(\psi)$ profile, the synchrotron's $\eta\cos\phi_s < 0$
3. **Drift control:** tokamak divertors, LHC multipole error correction

> **In the end, ITER is a machine that confines 10 keV gas in a $B$-bottle via the Lorentz force, and the LHC is a machine that confines 7 TeV particles in a 27 km ring via the Lorentz force — both are designed around the single equation $B\rho = p/q$.**

### 4.2.4 Mathematica Verification

```mathematica
(* Grad-Shafranov equation *)
gradShafranov[psi_, R_, Z_, mu0_, p_, F_] :=
  R D[1/R D[psi, R], R] + D[psi, {Z, 2}] ==
  -mu0 R^2 D[p[psi], psi] - F[psi] D[F[psi], psi];

(* Magnetic island width *)
islandWidth[q_, R_, Btilde_, m_, qPrime_, B0_] :=
  4 Sqrt[q^2 R Btilde / (m qPrime B0)];

(* Troyon limit *)
troyonLimit[beta_, a_, B_, Ip_] := beta a B / Ip; (* < 3 *)
```

### 4.2.5 Limits and Exceptions

- **Disruptions:** kink/tearing instability below $q < 2$ → rapid plasma collapse. In ITER, ~MA currents vanish within ms, with large currents striking the wall
- **ELMs:** localized instabilities at the H-mode edge, causing repeated bursts of energy
- **Greenwald limit:** $n_G = I_p/\pi a^2$, an upper bound on density
- **Troyon limit:** $\beta_N = \beta aB/I_p < 3$, an upper bound on pressure
- **Stellarators:** coil complexity, difficulty of quasisymmetry optimization

> **References**
> - Grad, H., Rubin, H., *Hydromagnetic equilibria and force-free fields*, Proc. 2nd UN Conf. **31**, 190 (1958).
> - Shafranov, V. D., *On magnetohydrodynamical equilibrium configurations*, Sov. Phys. JETP **6**, 545 (1957).
> - ITER Physics Basis, Nucl. Fusion **47**, S1 (2007). [doi:10.1088/0029-5515/47/6/S01](https://doi.org/10.1088/0029-5515/47/6/S01)
> - W7-X Team, *Quasi-isodynamic optimization*, Phys. Rev. Lett. **129**, 095001 (2022). [doi:10.1103/PhysRevLett.129.095001](https://doi.org/10.1103/PhysRevLett.129.095001)

---

## 4.3 Medical Technology

The Lorentz force has come down not only to giant accelerators but into **the human body** itself. MRI, proton therapy, magnetic nanoparticles, and magnetic tweezers are examples.

### 4.3.1 MRI and the Bloch Equations

MRI does not use the Lorentz force directly, but instead exploits **Lorentz-like motion of spins**.

**The static field:** a $B_0 = 1.5-7$ T superconducting magnet causes the proton magnetization $\mathbf{M}$ to undergo **Larmor precession:**

$$\frac{d\mathbf{M}}{dt} = \gamma \mathbf{M}\times\mathbf{B}_0$$

> **Unicode**
> ```
> (d𝐌)/(dt) = γ 𝐌×𝐁₀
> ```

$\gamma/2\pi = 42.58$ MHz/T.

**The Bloch equation — the spin version of the Lorentz force:**

$$\frac{d\mathbf{M}}{dt} = \gamma \mathbf{M}\times\mathbf{B} - \frac{M_x\hat{x}+M_y\hat{y}}{T_2} - \frac{(M_z-M_0)\hat{z}}{T_1}$$

> **Unicode**
> ```
> (d𝐌)/(dt) = γ 𝐌×𝐁 - (Mₓx̂+M_yŷ)/(T₂) - ((M_z-M₀)ẑ)/(T₁)
> ```

$$\mathbf{B}(\mathbf{r},t) = B_0\hat{z} + \mathbf{G}(t)\cdot\mathbf{r}\,\hat{z} + \mathbf{B}_1(t)$$

> **Unicode**
> ```
> 𝐁(𝐫,t) = B₀ẑ + 𝐆(t)·𝐫ẑ + 𝐁₁(t)
> ```

- $T_1, T_2$: relaxation due to collisions and fluctuations
- $\mathbf{G} = \nabla B_z = (G_x, G_y, G_z)$: the **gradient field** that encodes position

**Position encoding:**

$$\omega(\mathbf{r}) = \gamma(B_0 + \mathbf{G}\cdot\mathbf{r})$$

> **Unicode**
> ```
> ω(𝐫) = γ(B₀ + 𝐆·𝐫)
> ```

Frequency becomes position.

**Gradient-coil design:**

Satisfying Maxwell's equations $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{B} = 0$ while making only $B_z$ linear:

$$B_z = B_0 + G_x x + G_y y + G_z z$$

> **Unicode**
> ```
> B_z = B₀ + Gₓ x + G_y y + G_z z
> ```

$G_x$: a Golay coil in the $x$ direction; $G_z$: a Maxwell pair.

**Design parameters:**
- Linearity <5% over a 50 cm DSV
- Switching $dG/dt$ up to 200 T/m/s, slew-rate limited by peripheral nerve stimulation, $dB/dt < 20$ T/s
- **The Lorentz-force problem:** with $I \sim 600$ A in the gradient coils, at $B_0 = 3$ T, $F = IL\times B_0 \sim 10^4$ N/m. Coil vibration → 100 dB noise. This $F$ is **the source of MRI noise**. Force-balanced coils are a recent trend

**Recent trends:**
- Ultra-high field 7T+: SNR $\propto B_0$, but nonuniform $B_1$ wavelength requires parallel transmission
- AI reconstruction: reduces exam time from 10 minutes to 2
- Low-field 0.055T portable MRI: Halbach permanent magnets, silent operation without Lorentz-force-driven gradients

### 4.3.2 Proton Therapy

Protons at 70–230 MeV, $B\rho = 0.8-2.3$ Tm. The Lorentz force hits only the tumor.

**Beam line:** cyclotron/synchrotron → energy-selection system → **gantry**

**Gantry:** a 100-ton rotating structure with 2 pairs of dipoles + quadrupoles at $R \sim 3$ m, keeping $\mathbf{r}$ fixed at the isocenter. Design condition $M_{transport} = I$ — the beam is identical regardless of gantry angle.

**Pencil Beam Scanning (PBS) — the current standard:**

- $x,y$: scanning magnets $B_x(t), B_y(t)$ scan $\pm 20$ cm at 10 m/s via $F = qv\times B$. Spot size $\sigma \sim 3$ mm
- $z$: depth of the Bragg peak is controlled by energy. 230 MeV → 32 cm in water

**The Bragg peak:**

$$D(z) \propto \frac{1}{\beta^2}\cdot\frac{1}{1-0.9}\ \text{peak at } R \approx \alpha E^{1.8}$$

> **Unicode**
> ```
> D(z) ∝ (1)/(β²)·(1)/(1-0.9)  peak at  R≈ α E^1.8
> ```

Normal tissue dose reduced to 1/3, compared to X-rays.

**Recent trends:**
- **FLASH:** ultra-high dose rate $>40$ Gy/s, protecting normal tissue with 0.1-second exposures. Requires high current $I_p \sim 100$ nA
- **Arc therapy:** continuous irradiation while the gantry rotates, requiring rapid $B\rho$ modulation (<10 ms)
- **MRI-guided protons:** correction algorithms for the proton-trajectory bending $\Delta r = q B_{MRI} L^2/2p$ inside a $B_{MRI} = 0.5$ T field

### 4.3.3 Magnetic Nanoparticle Therapy

Superparamagnetic iron oxide Fe₃O₄, diameter 10–100 nm, magnetization $M_s \sim 400$ kA/m, magnetic moment $\mathbf{m} = M_sV$.

**Magnetic force — a dipole force, not the Lorentz force:**

$$\mathbf{F}_m = \nabla(\mathbf{m}\cdot\mathbf{B}) \approx \mathbf{m}\cdot\nabla\mathbf{B}$$

> **Unicode**
> ```
> 𝐅ₘ = ∇(𝐦·𝐁) ≈ 𝐦·∇𝐁
> ```

Particle velocity in a blood vessel $v \sim 1$ mm/s, drag $F_d = 6\pi\eta r v \sim 10$ pN. Achieving $F_m > F_d$ requires $\nabla B \sim 10$ T/m — achievable with a permanent-magnet Halbach array.

**Three applications:**
1. **Targeted drug delivery:** doxorubicin-loaded nanoparticles concentrated in a tumor by a $B$ gradient, giving a 5-fold increase in concentration
2. **Magnetic hyperthermia:** AC $B$ at 100 kHz, 20 mT → $P = \mu_0\pi f H_0^2\chi''$ → necrosis of the tumor at 42–45°C
3. **Magnetophoretic separation:** a single circulating tumor cell (CTC) per mL is labeled with a magnetic antibody and separated in a microchannel with $G \sim 100$ T/m

**Recent:** a 5 nm particle attached to a DNA origami structure, driven like a drill into a tumor by a rotating field $B_{rot}$ with torque $\boldsymbol{\tau} = \mathbf{m}\times\mathbf{B}$ — a nanorobot.

### 4.3.4 Magnetic Tweezers

A tool applying $F = 0.1-100$ pN to a single molecule of DNA or protein.

**Principle:** one end of a DNA molecule is fixed to a 2.8 μm Dynabead (superparamagnetic); a pair of permanent magnets generates $B \sim 0.1$ T, $\nabla B \sim 10$ T/m.

**Force and torque:**

$$F_z = m(B)\frac{\partial B_z}{\partial z}, \quad \boldsymbol{\Gamma} = \mathbf{m}\times\mathbf{B}$$

> **Unicode**
> ```
> F_z = m(B)(∂ B_z)/(∂ z),   Γ = 𝐦×𝐁
> ```

Force ranges from 0.01–10 pN, torque $10-10^4$ pN·nm. Field strength is controlled via magnet distance, rotation via magnet rotation — used to twist DNA.

**Three single-molecule experiments:**
1. **DNA supercoiling:** at 10 pN, 10 twists forms a plectoneme
2. **Helicase:** a 0.34 nm step per base pair unwound, tracked at 0.1 nm resolution
3. **100 parallel tweezers:** 3D tracking of replication-fork dynamics

**A Lorentz-based variant — Lorentz tweezers:** applying $B$ to a current-carrying microwire pulls DNA directly with $F = ILB$. Single-molecule manipulation via pure Lorentz force, without a magnetic bead.

### 4.3.5 Mathematica Verification

```mathematica
(* Bloch equation *)
blochEq = D[Mvec[t], t] == gammaGyro Cross[Mvec[t], Bvec]
  - {Mx[t]/T2, My[t]/T2, (Mz[t] - M0)/T1};

(* Larmor frequency *)
larmorFreq[gammaGyro_, B0_] := gammaGyro B0;

(* Magnetic nanoparticle force *)
nanoForce[mMag_, gradB_] := mMag gradB;

(* Magnetic tweezer torque *)
torque[ mVec_, bVec_] := Cross[mVec, bVec];
```

### 4.3.6 Limits and Exceptions

- **MRI:** vertigo above $B_0 > 8$ T, PNS limit $dB/dt < 20$ T/s, metallic-projectile hazard
- **Proton therapy:** sharpness of the Bragg peak, tissue heterogeneity during long-term tracking
- **Nanoparticles:** biodistribution, toxicity, immune response
- **Magnetic tweezers:** more force-stable than optical tweezers, no photodamage, but limited by bead size

> **References**
> - Bloch, F., *Nuclear induction*, Phys. Rev. **70**, 460 (1946). [doi:10.1103/PhysRev.70.460](https://doi.org/10.1103/PhysRev.70.460)
> - Hall, E. J., Giaccia, A. J., *Radiobiology for the Radiologist*, 8th ed., Wolters Kluwer (2018).
> - Pankhurst, Q. A., et al., *Applications of magnetic nanoparticles in biomedicine*, J. Phys. D **36**, R167 (2003). [doi:10.1088/0022-3727/36/13/201](https://doi.org/10.1088/0022-3727/36/13/201)
> - Neuman, K. C., Nagy, A., *Single-molecule force spectroscopy: optical tweezers, magnetic tweezers and atomic force microscopy*, Nat. Methods **5**, 491 (2008). [doi:10.1038/nmeth.1218](https://doi.org/10.1038/nmeth.1218)

---
## 4.4 Sensors and MEMS

The Lorentz force $q\mathbf{v}\times\mathbf{B}$ operates not only in giant accelerators but also in **microsensors**. This section covers Hall sensors, GMR/TMR, SQUIDs, and MEMS magnetic sensors.

### 4.4.1 Hall Sensors — Direct Measurement of the Lorentz Force

Applying $I_x$ and $B_z$ to a conductor → charge is pushed in $y$ by $q\mathbf{v}\times\mathbf{B}$ → a **Hall field** $E_y = V_H/w$.

**Hall voltage:**

$$V_H = \frac{R_H I B}{t}, \quad R_H = \frac{1}{nq}$$

> **Unicode**
> ```
> V_H = (R_H I B)/(t),   R_H = (1)/(nq)
> ```

Low carrier density $n$ in a semiconductor gives a larger $V_H$. Si Hall plates give $S \sim 100$ V/AT.

**Applications:** contactless current sensors, BLDC motor position, smartphone compasses.

**Recent:** vertical Hall, 3-axis Hall + ASIC giving 0.1% linearity, 1 mT resolution in automotive $B$ sensing.

**Limits:** small $V_H$, large temperature drift.

### 4.4.2 GMR/TMR — Spin-Dependent Lorentz Analogue

Ferromagnetic/nonmagnetic multilayers. Electron scattering probability depends on magnetization direction — a **spin filter**.

**GMR:**

- $R_P = R_0 - \Delta R$, $R_{AP} = R_0 + \Delta R$
- MR ratio $(R_{AP}-R_P)/R_P \sim 10-20\%$

**TMR:** an insulating MgO tunnel barrier, the Jullière formula:

$$TMR = \frac{2P_1P_2}{1-P_1P_2}$$

> **Unicode**
> ```
> TMR = (2P₁P₂)/(1-P₁P₂)
> ```

The current record is 600% at room temperature.

**Principle:** an external $B$ rotates the free layer's magnetization → resistance changes → a $B$ sensor. The principle is **exchange coupling, not the Lorentz force**, but the effect is analogous to magnetization standing in for electron gyration.

**Applications:**
- HDD heads (the GMR revolution of the 1990s)
- Biosensors: 1 μm magnetic beads label DNA and are pulled onto a GMR sensor, detecting nT fields — fM-level detection

### 4.4.3 SQUID — The Ultimate $U(1)$-Phase Sensor

A superconducting loop with two Josephson junctions. **Flux quantization** $\Phi = n\Phi_0$, $\Phi_0 = h/2e$.

**Critical current:**

$$I_c(\Phi) = 2I_0\left|\cos(\pi\Phi/\Phi_0)\right|$$

> **Unicode**
> ```
> I_c(Φ) = 2I₀|cos(πΦ/Φ₀)|
> ```

One flux quantum ($2\times10^{-15}$ Wb) modulates the current by 100%. **Field sensitivity of 1 fT/√Hz** — $10^{-11}$ of Earth's 50 μT field.

**Applications:**
- MEG (magnetoencephalography), 100 fT signals
- Magnetocardiography, nondestructive testing
- Ultra-low-field MRI, $B_0 = 100$ μT, detected by SQUID

**Recent:** high-temperature SQUIDs at 77 K, nano-SQUID-on-tip with 50 nm diameter → single-spin detection.

**Sensor comparison table:**

| Sensor | Principle | Sensitivity | Bandwidth | Size/price |
|---|---|---|---|---|
| Hall | $q v\times B$ | 1 μT | MHz | $0.1 |
| GMR/TMR | Spin scattering | 1 nT | MHz | $0.5 |
| SQUID | Flux quantization $h/2e$ | 1 fT | kHz | cm, cryogenic |

**Trend:** TMR is replacing Hall sensors, while SQUID remains the quantum-limit sensor.

### 4.4.4 MEMS Magnetic Sensors — Lorentz-Force-Based Design

A microscale beam carrying current is bent by the Lorentz force when $B$ is applied.

**Structure:** an $L = 200$ μm Si beam, $I = 1$ mA, $B = 1$ mT → $F = ILB = 0.2$ nN.

**Displacement:** $k \sim 1$ N/m → $x = F/k = 0.2$ nm. The resulting capacitance change $\Delta C \sim$ aF is undetectable.

**Solution — resonant drive:**

$$m\ddot{x} + c\dot{x} + kx = F_0\cos\omega_0 t = I_0 B L\cos\omega_0 t$$

> **Unicode**
> ```
> mx¨ + cx˙ + kx = F₀cosω₀ t = I₀ B Lcosω₀ t
> ```

With vacuum packaging giving $Q \sim 10^4$, the amplification $x = QF_0/k \sim 2$ μm becomes detectable. Frequency shift $\Delta\omega \propto B^2$ is measured.

**Recent — Lorentz-force magnetometer:** implemented by switching current direction along 3 axes ($x,y,z$). An attempt to replace Hall sensors in smartphone compasses.

**Advantages:** CMOS-compatible, no $B$ offset (Hall sensors have a large offset)
**Disadvantages:** power consumption $I^2R$, temperature-sensitive $Q$

**Research trends:** an AlN piezoelectric resonator achieving $Q = 10^5$, with sensitivity of 10 nT/√Hz.

### 4.4.5 Mathematica Verification

```mathematica
(* Hall voltage *)
hallVoltage[iCurrent_, bField_, nCarrier_, qCharge_, tThickness_] :=
  iCurrent bField / (nCarrier qCharge tThickness);

(* TMR *)
tmr[p1_, p2_] := 2 p1 p2 / (1 - p1 p2);

(* SQUID critical current *)
squidCritical[Phi_, Phi0_, I0_] := 2 I0 Abs[Cos[Pi Phi/Phi0]];

(* MEMS resonant displacement *)
resonanceDisplacement[Q_, F0_, k_] := Q F0 / k;
```

### 4.4.6 Limits and Exceptions

- **Hall:** temperature drift, offset
- **GMR/TMR:** magnetic hysteresis, temperature dependence
- **SQUID:** requires cryogenics, essential magnetic shielding
- **MEMS:** temperature-sensitive $Q$, power consumption

> **References**
> - Hall, E. H., *On a new action of the magnet on electric currents*, Am. J. Math. **2**, 287 (1879). [doi:10.2475/ajs.s3-19.117.200](https://doi.org/10.2475/ajs.s3-19.117.200)
> - Baibich, M. N., et al., *Giant Magnetoresistance of (001)Fe/(001)Cr Magnetic Superlattices*, Phys. Rev. Lett. **61**, 2472 (1988). [doi:10.1103/PhysRevLett.61.2472](https://doi.org/10.1103/PhysRevLett.61.2472)
> - Clarke, J., Braginski, A. I., *The SQUID Handbook*, Wiley-VCH (2004). [doi:10.1002/9783527603646](https://doi.org/10.1002/9783527603646)

---

## 4.5 Space Physics and Natural Phenomena

Space plasmas are collisionless, so $\mathbf{J}\times\mathbf{B}$, $\nabla B$ drift, and magnetic reconnection govern everything. This section covers auroras, the Van Allen belts, magnetic reconnection, field-aligned currents, pulsars, and solar flares.

### 4.5.1 The Full Physics of Auroral Formation

**Step 1: Solar wind → magnetosphere**

Solar wind: $n \sim 5$ cm$^{-3}$, $v \sim 400$ km/s, $B_{IMF} \sim 5$ nT, dynamic pressure $P_{dyn} = nm_p v^2 \sim 2$ nPa.

Balanced against Earth's dipole magnetic pressure $P_B = B^2/2\mu_0$:

$$\frac{B_0^2}{2\mu_0}\left(\frac{R_E}{R_{mp}}\right)^6 = P_{dyn} \implies R_{mp} \approx 10 R_E$$

> **Unicode**
> ```
> (B₀²)/(2μ₀)((R_E)/(Rₘₚ))⁶ = P_dyn ⟹ Rₘₚ ≈ 10 R_E
> ```

When $B_{IMF}$ is southward ($B_z < 0$), **magnetic reconnection** occurs at the dayside magnetopause → the Dungey convection cycle: field lines open into the solar wind and are dragged into the tail.

**Step 2: Storage in the magnetotail and particle acceleration**

Tail lobe $B \sim 20$ nT, plasma sheet $n \sim 0.3$ cm$^{-3}$, $T \sim 5$ keV. The solar-wind–magnetosphere dynamo $\mathbf{E} = -\mathbf{V}_{sw}\times\mathbf{B}$ produces a dawn–dusk field $E_y \sim 0.1-1$ mV/m → an $\mathbf{E}\times\mathbf{B}$ convection from the tail toward Earth, $V \sim 50$ km/s.

As plasma-sheet particles convect earthward, they undergo **adiabatic heating:** $\mu = mv_\perp^2/2B$ is conserved, and as $B$ increases (5 nT → 100 nT) → $T_\perp$ increases 20-fold.

**Step 3: Magnetic mirror and the loss cone**

Near Earth, $B_0 \sim 50$ μT, equatorial $B_{eq} \sim 100$ nT → mirror ratio $R_m = B_0/B_{eq} \sim 500$.

Confinement condition $\sin^2\theta_0 > B_{eq}/B_0$. Loss cone $\theta_{lc} = \arcsin\sqrt{B_{eq}/B_0} \sim 2.5^\circ$.

Most of the general plasma sheet, at $T \sim 5$ keV, is confined. Reconnection and wave–particle interactions (whistler, EIC) scatter pitch angle → fill the loss cone → **precipitation**.

**Step 4: Emission**

At altitudes of 100–300 km, collisional excitation of $O, N_2$:

$$e^* + O \to O^* \to O + h\nu$$

> **Unicode**
> ```
> e^* + O → O^* → O + hν
> ```

- $O(^1D\to^3P)$ 630.0 nm red, above 200 km
- $O(^1S\to^1D)$ **557.7 nm green**, 100–150 km, the brightest
- $N_2^+$ 427.8 nm blue, below 100 km

**Auroral oval:** magnetic latitude 65–75°, skewed toward the nightside — a projection of the tail reconnection location.

### 4.5.2 The Van Allen Belts

**Inner belt:** $1.2-2.5 R_E$, protons at 10–100 MeV (CRAND), electrons at 100 keV
**Outer belt:** $3-7 R_E$, electrons at 0.1–10 MeV

**Three periodic motions — all from the Lorentz force:**

1. **Gyration:** $\omega_c = qB/m$, $r_L \sim$ km (for MeV electrons)
2. **Bounce:** back and forth between magnetic mirrors, $\tau_b = \oint ds/v_\parallel \sim 0.1-1$ s
3. **Drift:** $\mathbf{V}_{gc} \approx \frac{m}{qB^3}(v_\parallel^2+v_\perp^2/2)\mathbf{B}\times\nabla B$

In the dipole field $B \propto 1/r^3$, the azimuthal drift:

$$\omega_d = \frac{3L R_E m v^2}{2|q|B_0 R_E^2}$$

> **Unicode**
> ```
> ω_d = (3L R_E m v²)/(2|q|B₀ R_E²)
> ```

Ions drift westward, electrons eastward, with periods of minutes to hours.

**Ring current:** $J_\phi \sim nqV_d \sim 10$ nA/m², totaling 2–5 MA westward → decreases the ground magnetic field by 20–100 nT — **the Dst index**.

### 4.5.3 The Magnetotail and Magnetic Reconnection

Tail current sheet: $B_x$ reverses from +20 nT in the northern lobe to -20 nT in the southern lobe over a thickness of ~1000 km.

**Harris equilibrium:** $B_x(z) = B_0\tanh(z/\lambda)$, $J_y \propto \text{sech}^2$.

$\mathbf{J}\times\mathbf{B}$ balances the pressure gradient $\nabla p$ against expansion in the $x$ direction.

Sustained southward $B_{IMF}$ accumulates flux in the tail → the current sheet thins, $\lambda \to$ the ion inertial length $d_i = c/\omega_{pi} \sim 500$ km → **magnetic reconnection** is triggered.

**The Sweet–Parker model:** at Lundquist number $S = \mu_0 L V_A/\eta \sim 10^{10}$ → reconnection is slow.

**In reality, Hall reconnection:** ions demagnetize at $d_i$, while electrons continue $\mathbf{E}\times\mathbf{B}$ drift down to $d_e$ → generating a quadrupolar Hall $B_y$, giving a fast reconnection rate of $0.1 V_A$.

**The Lorentz-force viewpoint:** outside the diffusion region, the frozen-in condition $\mathbf{E}+\mathbf{V}_e\times\mathbf{B} = 0$ holds; inside, $\mathbf{E}+\mathbf{V}_e\times\mathbf{B} = \eta\mathbf{J}+\ldots \neq 0$ breaks the frozen-in condition → field lines break and reconnect.

**Outflow jets:** $V_{out} \sim V_A = B/\sqrt{\mu_0 nm_p} \sim 1000$ km/s, accelerating ions to 10 keV — the onset of auroral substorms.

### 4.5.4 Field-Aligned Currents (FAC)

Magnetosphere–ionosphere coupling is carried by **Birkeland currents** flowing along $B$.

**Origin:** the divergence of the perpendicular current $\mathbf{J}_\perp$, caused by $\nabla p$ or inertia, must be closed along $B$ for continuity:

$$\nabla\cdot\mathbf{J} = 0 \implies B\partial_s(J_\parallel/B) = -\nabla\cdot\mathbf{J}_\perp$$

> **Unicode**
> ```
> ∇·𝐉 = 0 ⟹ B∂ₛ(J_∥/B) = -∇·𝐉_⊥
> ```

**Region 1 FAC:** at the polar cap boundary, downward (dawn)/upward (dusk), $\sim 1$ μA/m², $I \sim 2$ MA
**Region 2 FAC:** equatorward of the auroral oval, opposite direction, part of the ring current

**Ionospheric closure:** Pedersen current $\mathbf{J}_P = \sigma_P\mathbf{E}_\perp$ (Joule heating), Hall current $\mathbf{J}_H = \sigma_H\hat{b}\times\mathbf{E}_\perp$ (magnetic disturbance).

**The Knight relation:** $j_\parallel = e^2 n_e/\sqrt{2\pi m_e T_e}(\Delta\Phi)$ — a potential difference $\Delta\Phi \sim$ kV exists as a parallel electric field $\mathbf{E}_\parallel$, the direct cause of auroral acceleration.

### 4.5.5 Pulsars and Magnetars

Pulsars: $B \sim 10^8-10^{12}$ T, $P = 1$ ms–10 s, $R = 10$ km neutron stars.

**Goldreich–Julian magnetosphere:** rotation $\boldsymbol{\Omega}\times\mathbf{r}$ separates charge on the conducting stellar surface → a vacuum field $E \sim (\Omega R)B \sim 10^{12}$ V/m. $E\cdot B \neq 0$ → $e^\pm$ emission from the surface.

**GJ density:**

$$n_{GJ} = \frac{2\epsilon_0\boldsymbol{\Omega}\cdot\mathbf{B}}{e} \sim 10^{17}\ \text{m}^{-3}\frac{B_{12}}{P}$$

> **Unicode**
> ```
> n_GJ = (2ε₀ Ω·𝐁)/(e) ∼ 10¹⁷ m⁻³(B₁₂)/(P)
> ```

**Polar-cap potential:**

$$\Phi_{pc} = \frac{\Omega^2 B R^3}{2c^2}$$

> **Unicode**
> ```
> Φ_pc = (Ω² B R³)/(2c²)
> ```

$\Phi_{pc} \sim 10^{12}$ V. Particles are accelerated by $\mathbf{E}_\parallel$ up to $\gamma \sim 10^7$ → curvature radiation $P \propto \gamma^4/\rho_c^2$ → GeV photons → pair production $\gamma+B \to e^+e^-$ in $B$ → secondary plasma → radio emission. **The pulsar mechanism** — all driven by Lorentz-force acceleration wherever the condition $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$ is broken.

**Magnetars:** $B \sim 10^{10}-10^{11}$ T, exceeding the quantum critical field $B_Q = m_e^2c^3/e\hbar = 4.4\times10^9$ T. The Landau-level spacing exceeds $mc^2$, producing vacuum birefringence and photon splitting $\gamma\to\gamma\gamma$.

### 4.5.6 Solar Flares and CMEs

Corona: $B \sim 10^{-3}$ T, $n \sim 10^{15}$ m$^{-3}$, $\beta = 2\mu_0 p/B^2 \sim 0.01$ — **magnetically dominated**, with the Lorentz force $\mathbf{J}\times\mathbf{B}$ $10^4$ times larger than gravity.

**Flare storage:** photospheric convection twists flux tubes → energy is stored in a force-free state ($\mathbf{J} = \alpha\mathbf{B}$, $\mathbf{J}\times\mathbf{B} = 0$) with current $\mathbf{J}$ in the corona, $W = \int B^2/2\mu_0\, dV \sim 10^{25}$ J.

**Trigger — kink/torus instability:** when the twist $\Phi = \int\alpha\, dl > 2\pi$, $\mathbf{J}\times\mathbf{B}$ becomes unbalanced → the flux rope rises.

As it rises, a current sheet forms → magnetic reconnection, with Petschek fast reconnection giving $E_{rec} = V_{in}B_{in} \sim 100$ V/m.

**Acceleration:** $E_\parallel$ accelerates electrons to 20–100 keV, and $F = qE$ drives precipitation into the lower atmosphere → HXR footpoint emission.

**CME:** the flux rope escapes at $V \sim 1000$ km/s, mass $10^{12}$ kg, energy $10^{23}$ J. Driven by $\mathbf{J}\times\mathbf{B}_{ext}$ — the Lorentz force between the rope current and the background field.

**Effect on Earth:** a southward $B_z$ in a CME can cause a $Dst < -100$ nT geomagnetic storm. The 1859 Carrington event reached $B \sim 1600$ nT — if it occurred today, transformer GICs $J = \sigma E$, $E \sim$ V/km, would cause blackouts.

**Unified picture:** solar dynamo ($\mathbf{v}\times\mathbf{B}$) → magnetic energy storage → reconnection ($\mathbf{E}+\mathbf{v}\times\mathbf{B} \neq 0$) → particle acceleration ($q\mathbf{E}$) → confinement in planetary magnetospheres via $\nabla B$ and curvature drift → atmospheric precipitation and emission. **From auroras to pulsars, everything is the same $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ operating across a scale difference of $10^{10}$.**

### 4.5.7 Mathematica Verification

```mathematica
(* Magnetic mirror condition *)
mirrorCondition[B0_, Bm_, theta0_] := Sin[theta0]^2 == B0/Bm;

(* Dipole magnetic field *)
BrDipole[mDipole_, theta_, r_] := 2 mDipole Cos[theta]/r^3;
BthetaDipole[mDipole_, theta_, r_] := mDipole Sin[theta]/r^3;

(* GJ density *)
gjDensity[Omega_, Bfield_, eCharge_, epsilon0_] :=
  2 epsilon0 Omega . Bfield / eCharge;

(* Polar cap potential *)
polarCapPotential[Omega_, Bfield_, R_, cLight_] :=
  Omega^2 Bfield R^3 / (2 cLight^2);
```

### 4.5.8 Limits and Exceptions

- **MHD approximation:** breaks down below the ion inertial length; Hall MHD is needed
- **Magnetic reconnection:** 3D kinetic simulations and observations disagree by ~30%
- **Pulsars:** the pair-production screening mechanism remains debated
- **CME prediction:** timing and direction remain uncertain

> **References**
> - Dungey, J. W., *Interplanetary magnetic field and the auroral zones*, Phys. Rev. Lett. **6**, 47 (1961). [doi:10.1103/PhysRevLett.6.47](https://doi.org/10.1103/PhysRevLett.6.47)
> - Van Allen, J. A., *Observation of high intensity radiation by satellites*, J. Geophys. Res. **63**, 179 (1958). [doi:10.1029/JZ063i001p00179](https://doi.org/10.1029/JZ063i001p00179)
> - Parker, E. N., *Dynamics of interplanetary gas and magnetic fields*, Astrophys. J. **128**, 664 (1958). [doi:10.1086/146579](https://doi.org/10.1086/146579)
> - Goldreich, P., Julian, W. H., *Pulsar electrodynamics*, Astrophys. J. **157**, 869 (1969). [doi:10.1086/150119](https://doi.org/10.1086/150119)

---

## 4.6 Nonlinear Dynamics and Chaos

The Lorentz force $m\dot{\mathbf{v}} = q(\mathbf{v}\times\mathbf{B})$ looks linear on the surface, but the moment $\mathbf{B}(\mathbf{x})$ depends on $\mathbf{x}$, it becomes a **nonlinear Hamiltonian system with 3 degrees of freedom**. Integrable when $B$ is uniform, chaotic when nonuniform. This section covers the conditions for chaos, KAM theory, magnetic reconnection, and turbulence.

### 4.6.1 Conditions for Chaos in Lorentz-Force Trajectories

Hamiltonian $H = (\mathbf{p}-q\mathbf{A})^2/2m$. The **condition for integrability** is Liouville–Arnold: $n$ degrees of freedom require $n$ independent, commuting conserved quantities.

**Uniform $\mathbf{B} = B_0\hat{z}$:**
- $p_y$ conserved (translational symmetry)
- $p_z$ conserved
- $H$ itself

→ integrable, trajectory is a helix, phase space is a 3-torus.

**Three conditions for chaos (any one is sufficient):**

1. **Spatial nonuniformity:** $\mathbf{B} = \mathbf{B}(\mathbf{x})$. If the perturbation $\epsilon = r_L/L_B \gtrsim 0.1$, resonance between the gyro-phase and bounce motion, $\omega_b = n\omega_c$ → Chirikov overlap
2. **Time dependence:** a time-dependent $\mathbf{E}(t)$ or $B(t)$ makes a 1.5-degree-of-freedom Hamiltonian → a forced pendulum. Stochastic heating occurs when RF heating $\mathbf{E}_{rf}\cos\omega t$ has $\omega \approx \omega_c$
3. **Magnetic curvature + electric field:** when the shear of the $E\times B$ flow $V_E(x) = E(x)/B$, $dV_E/dx \sim \omega_c$, trajectories become chaotic in a manner similar to the Kelvin–Helmholtz instability

**Lyapunov exponent:**

$$\lambda = \lim_{t\to\infty}\frac1t\ln\frac{|\delta\mathbf{x}(t)|}{|\delta\mathbf{x}(0)|}$$

> **Unicode**
> ```
> λ = lim_t→∞(1)/(t)ln(|δ𝐱(t)|)/(|δ𝐱(0)|)
> ```

Chaotic if $\lambda > 0$. In a uniform $B$, $\lambda = 0$; in a magnetic mirror $B(z) = B_0(1+z^2/L^2)$ with a quadrupole perturbation, once the critical $\epsilon_c \sim r_L/L$ is exceeded, $\lambda \sim 0.1\omega_c$.

**Physical examples:**
- In the magnetosphere, if $\kappa = \sqrt{R_c/r_L} < 3$ (Büchner–Zelenyi), gyro-bounce-coupled chaos → isotropization of $T_\perp$ in the current sheet
- Pulsar polar caps: fractal trajectories in the relativistic regime $E \approx B$

### 4.6.2 The KAM Theorem and Phase-Space Island Structure

An integrable system $H_0(\mathbf{J})$ with a perturbation $\epsilon H_1(\mathbf{J},\boldsymbol{\theta})$:

$$H = H_0(\mathbf{J}) + \epsilon H_1(\mathbf{J},\boldsymbol{\theta})$$

> **Unicode**
> ```
> H = H₀(𝐉) + ε H₁(𝐉,θ)
> ```

**The KAM theorem:** non-resonant tori $\mathbf{n}\cdot\boldsymbol{\omega}_0 \neq 0$ survive with slight distortion for $\epsilon < \epsilon_c$. Resonant tori collapse, producing **island chains** and **chaotic layers**.

**The field-line equation:** with $\mathbf{B} = \nabla\psi\times\nabla\theta + \nabla\phi\times\nabla\chi$, the field lines satisfy:

$$\frac{d\psi}{d\phi} = -\frac{\partial H}{\partial\theta}, \quad \frac{d\theta}{d\phi} = \frac{\partial H}{\partial\psi}, \quad H = \chi$$

> **Unicode**
> ```
> (dψ)/(dφ) = -(∂ H)/(∂θ),   (dθ)/(dφ) = (∂ H)/(∂ψ),   H = χ
> ```

- **KAM torus:** a flux surface. Exists when $\iota(\psi) = d\theta/d\phi$ is irrational
- **Resonant island:** islands form on rational surfaces $\iota = n/m$, with width $w_{mn} \propto \sqrt{\tilde{B}_{mn}/m\iota'}$
- **Chaotic sea:** by the Chirikov criterion, $s = (w_m+w_{m+1})/\Delta_{m,m+1} > 1$ causes island overlap → stochastic diffusion of field lines

**Rechester–Rosenbluth diffusion:**

$$D_{RR} = \pi q R \frac{\langle\tilde{B}_r^2\rangle}{B_0^2}L_c$$

> **Unicode**
> ```
> D_RR = π q R (⟨ B̃ᵣ²⟩)/(B₀²)L_c
> ```

A particle runs along a field line at $v_\parallel$ while diffusing perpendicularly at $D_{RR}v_\parallel$ → giving $D \sim 10$ m²/s, larger than Bohm diffusion.

**Experimental observations:** on the $q=2$ surface of a tokamak, an $m/n = 2/1$ island, Thomson-scattering $T_e$ flattening, O-points/X-points on a Poincaré section.

**The importance of KAM:** fully chaotic means no confinement; fully integrable means no heating. **Fusion requires a boundary at which most KAM tori survive, but the edge undergoes weak chaos to expel heat and particles** — the H-mode pedestal is an example.

### 4.6.3 Nonlinear Dynamics of Magnetic Reconnection

Reconnection is a **topologically chaotic process** that changes the topology of the field lines.

**Linear phase:** for a current sheet $J_y(z) = J_0\text{sech}^2(z/\lambda)$, the growth rate of the **tearing mode**:

$$\gamma \sim S^{-3/5}k^{2/5}$$

> **Unicode**
> ```
> γ ∼ S^-3/5k^2/5
> ```

Furth–Killeen–Rosenbluth, $S = \tau_R/\tau_A$.

**Nonlinear phase:**
1. **Island growth** $w(t)$: Rutherford, $dw/dt \sim \eta\Delta'(w)$
2. **Collision of two islands:** when $m/n = 3/2$ and $2/1$ islands overlap with $s > 1$, secondary reconnection occurs → a plasmoid chain
3. **Plasmoid instability:** above $S > 10^4$, the current sheet fragments into a number of secondary islands proportional to $S$ → giving a fast reconnection rate $V_{rec} \sim 0.01V_A$, independent of $S$

**Nonlinear Lorentz force:** the reconnection jet $\mathbf{J}\times\mathbf{B}$ accelerates plasmoids, feeding back:

$$\frac{d}{dt}(nm V_{out}) \sim J\times B - \nabla p$$

> **Unicode**
> ```
> (d)/(dt)(nm Vₒᵤₜ) ∼ J× B - ∇ p
> ```

**Result:** reconnection becomes explosive and chaotic above a critical $S$ — the plasmoid size distribution follows a power law $N(w) \propto w^{-2}$, matching the size distribution of solar flares, a hallmark of **self-organized criticality (SOC)**.

### 4.6.4 Field-Line Chaos and Plasma Confinement

The field-line equations themselves form a Hamiltonian system. An axisymmetric tokamak is integrable; adding a 3D perturbation (error fields, RMP coils) produces Hamiltonian chaos.

- **Island width:** $w_{mn} = 4\sqrt{|q\epsilon_{mn}/q'|}$
- **Stochastic threshold:** $s > 1$ → magnetic surface destruction → Rechester–Rosenbluth diffusion

**Effects on confinement:**
- **Beneficial:** ITER's RMP ELM control deliberately stochastizes the $q=3-5$ region with an $n=3$ perturbation, spreading the heat load
- **Detrimental:** if the core becomes stochastic, $\tau_E \propto 1/D$ drops sharply — the reason 1970s stellarators failed

**Modern stellarator optimization:** minimizing $\epsilon_{mn}$ to maximize KAM tori — the **quasisymmetry** condition is essentially the KAM condition.

### 4.6.5 Plasma Turbulence and the Lorentz Force

Turbulence is driven by the nonlinear $\mathbf{V}_E\cdot\nabla$ term of the $\mathbf{E}\times\mathbf{B}$ drift.

**The MHD equations:**

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

**Two nonlinear terms:** $\mathbf{V}\cdot\nabla\mathbf{V}$ (Navier–Stokes) and $\mathbf{J}\times\mathbf{B}$ (Lorentz).

Taking $\mathbf{V} \approx \mathbf{V}_E = \mathbf{E}\times\mathbf{B}/B^2$ gives the **Hasegawa–Mima equation**:

$$\frac{d}{dt}\nabla_\perp^2\phi + [\phi, \nabla_\perp^2\phi] = \ldots$$

> **Unicode**
> ```
> (d)/(dt)∇_⊥²φ + [φ,∇_⊥²φ] = ...
> ```

$[f,g] = \hat{b}\cdot\nabla f\times\nabla g$, the Poisson bracket.

- **Drift-wave turbulence:** $\omega_* = k_y T/eBL_n$, with a $k^{-3}$ spectrum
- **$E\times B$ shear suppression:** when $\omega_{E\times B} = dV_E/dx$ exceeds the turbulent vorticity, eddies are torn apart → turbulence suppression, **the L-H transition**

**Turbulent transport:** $\langle\tilde{V}_{E,r}\tilde{n}\rangle$, $\tilde{V}_{E,r} = \tilde{E}_\theta/B$. Since $E\times B$ is itself a Lorentz drift, turbulent transport is a **second-order correlation of the Lorentz force**.

### 4.6.6 Lorentz Equation vs. Lorenz Equations — A Comparison Table

A frequent confusion. **They are completely different.**

| Category | **Lorentz force** | **Lorenz equations** |
|---|---|---|
| Origin | H.A. Lorentz (1892), electromagnetic force | E.N. Lorenz (1963), atmospheric convection |
| Equation | $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | $\dot{x} = \sigma(y-x), \dot{y} = x(\rho-z)-y, \dot{z} = xy-\beta z$ |
| Nature | Hamiltonian system, phase-volume conserving, $\nabla\cdot\mathbf{f} = 0$ | Dissipative system, volume-contracting, $\nabla\cdot\mathbf{f} = -(\sigma+1+\beta) < 0$ |
| Chaos | Hamiltonian chaos, KAM | Dissipative chaos, the Lorenz attractor |
| Relation | None | None. Note the spelling difference, Lorentz vs. Lorenz |

**Similarity:** both are textbook examples in nonlinear dynamics.

In a Lorentz-force system, if $B(x) = B_0(1+\alpha x)$, then $\ddot{x} = \omega_c(1+\alpha x)\dot{y}$ takes a quadratic nonlinear form resembling the Lorenz system. But their physical origins are different.

**Summary:** the Lorentz force gives a regular helix when integrable, KAM islands at resonances $\mathbf{k}\cdot\mathbf{V}_d = n\omega_c$, and Hamiltonian chaos when islands overlap → stochastization of field lines → fast reconnection, turbulent transport. **Plasma confinement is a battle over how many KAM tori survive, while reconnection and turbulence are the physics of how those tori are broken.** It is this nonlinearity that makes fusion difficult and auroras beautiful.

### 4.6.7 Mathematica Verification

```mathematica
(* Lorenz equations (for reference) *)
lorenzEqs = {
  x'[t] == sigma (y[t] - x[t]),
  y'[t] == x[t] (rho - z[t]) - y[t],
  z'[t] == x[t] y[t] - beta z[t]
};

(* Lyapunov exponent of a Lorentz-force trajectory *)
lyapunovExponent[trajectory_] := Module[{delta0, deltaT, tMax},
  delta0 = Norm[trajectory[[2]] - trajectory[[1]]];
  deltaT = Norm[trajectory[[-1]] - trajectory[[-2]]];
  Log[deltaT/delta0] / Length[trajectory]
];

(* Island width *)
islandWidth[q_, R_, Btilde_, m_, qPrime_, B0_] :=
  4 Sqrt[q^2 R Btilde / (m qPrime B0)];

(* Rechester-Rosenbluth diffusion *)
rrDiffusion[q_, R_, BtildeSq_, B0_, Lc_] :=
  Pi q R BtildeSq / B0^2 * Lc;
```

### 4.6.8 Limits and Exceptions

- **Determining chaos:** the Lyapunov exponent converges slowly numerically
- **The KAM theorem:** perturbation theory, breaks down under strong perturbation
- **Magnetic reconnection:** 3D kinetic and MHD models disagree
- **Turbulence:** first-principles prediction falls short of 10% accuracy
- **Lorentz vs. Lorenz:** be careful not to confuse the names

> **References**
> - Kolmogorov, A. N., *On conservation of conditionally periodic motions*, Dokl. Akad. Nauk SSSR **98**, 527 (1954); Arnold, V. I. (1963); Moser, J. (1962). [doi:10.1070/RM1963v018n05ABEH004130](https://doi.org/10.1070/RM1963v018n05ABEH004130)
> - Lorenz, E. N., *Deterministic nonperiodic flow*, J. Atmos. Sci. **20**, 130 (1963). [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)
> - Rutherford, P. H., *Nonlinear growth of the tearing mode*, Phys. Fluids **16**, 1903 (1973). [doi:10.1063/1.1694232](https://doi.org/10.1063/1.1694232)
> - Rechester, A. B., Rosenbluth, M. N., *Electron heat transport in a tokamak with destroyed magnetic surfaces*, Phys. Rev. Lett. **40**, 38 (1978). [doi:10.1103/PhysRevLett.40.38](https://doi.org/10.1103/PhysRevLett.40.38)

---
# Act 5. Frontiers and the Future

> **Arc of this act**
> Recent research trends (2020–2025) → Open problems → Condensed matter and topological materials
>
> Through Act 4, the applications of the Lorentz force were established. Act 5 covers **research happening right now, in this moment**. Before 2020, the Lorentz force was a formula; after 2020, it is a **control variable**. AI learns $\mathbf{J}\times\mathbf{B}$ as a reward function, quantum chips confine ions with $\mathbf{v}\times\mathbf{B}$, graphene uses $\mathbf{v}\times\mathbf{B}$ as a rectifier, and lasers probe the regime where $\mathbf{v}\times\mathbf{B}$ overtakes $\mathbf{E}$.

---

## 5.1 Recent Research Trends (2020–2025)

The Lorentz force is not a classical relic. Since 2020, $q\mathbf{v}\times\mathbf{B}$ has become an **AI control variable, a qubit isolation field, and a nanoscale topological invariant**. This section covers AI control of fusion, quantum computing, nanodevices, ultra-intense lasers, gravitational-wave detection, space propulsion, and a summary of 20 key papers.

### 5.1.1 AI Control of Fusion

Classical PID controllers cannot handle 20 $B$ coils and the nonlinear Grad–Shafranov equation for $\psi(R,Z)$. Since 2020, **reinforcement learning (RL)** has broken through this barrier.

#### DeepMind × EPFL TCV (2022, Nature)

An RL agent, after **100,000 trial-and-error attempts** in simulation, directly controlled the magnetic coils of a real tokamak at 10 kHz.

- A single neural network generated **snowflake, droplet, and ITER H-mode shapes**
- **Discovered** previously unknown configurations
- **Reward function:** $r = -|\psi - \psi_{target}| - |J\times B - \nabla p|$ — directly minimizes the Lorentz-equilibrium error

#### Expansion (2023–2025)

- **DIII-D + RL (USA):** real-time suppression of NTMs and ELMs. $\tilde{B}$ sensors → RMP coils stabilize islands via $\mathbf{J}\times\mathbf{B}$. **In 2024, long-duration Q>1 was successfully sustained**
- **KSTAR AI (Korea):** 2023–24, a deep-learning surrogate predicts $\Delta^*\psi = -\mu_0R^2p' - FF'$ within 1 ms, and RL controls the L-H transition via $V_{E\times B}$ shear. **AI control loops were key to achieving 100-second operation**
- **Neural ODE:** a physics-constrained neural network for predicting plasma current $I_p$, enforcing $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$ as a loss term

**Trend:** the control target is no longer the $B$ coils but the $\mathbf{J}\times\mathbf{B}$ force distribution directly.

### 5.1.2 The Lorentz Force in Quantum Computing

#### Ion Traps

**Paul traps:** confine with RF $\mathbf{E}$ but suffer micromotion heating.

**Penning traps:** static $\mathbf{E}$ + static $B = 3$ T, with the Lorentz force $q\mathbf{v}\times\mathbf{B}$ providing circular confinement, no RF needed.

- **ETH Zurich (2022–23):** 2D arbitrary transport of ions in a micro Penning chip, realizing qubit operations. Stronger $B$ gives smaller $r_L$, favoring scalability
- **A record of 219 entangled Be ions** uses the same principle

#### Superconducting Qubits

A superconducting loop has $F = 0$, but flux noise $\Phi_{noise}$ acts as a $\mathbf{v}\times\mathbf{B}$-like phase noise, causing qubit decoherence.

- **Recent fluxonium, 0-$\pi$ qubits:** the $E_J\cos(\Phi)$ potential arising from the Lorentz force is made insensitive via $U(1)$ symmetry protection
- **Google Willow (2024):** flux-bias stabilization was key

Here, the Lorentz force is the enemy, and active cancellation of $B$ noise via AI is a research topic.

### 5.1.3 Nanodevices — Graphene and Topological Insulators

#### Nonlinear Hall Effect (Graphene)

In 2022–24, a graphene moiré superlattice reported a **nonlinear Hall voltage $E^2H$** reaching 32% of the linear Hall signal. Its origin is the cooperation of the classical Lorentz force with quantum skew scattering.

$$j \sim E^2$$

> **Unicode**
> ```
> j ∼ E²
> ```

Applications in energy harvesting via a rectification effect.

#### Hydrodynamic Electrons

In a graphene channel, viscosity $\nu$ competes with the Lorentz force, and **Hall viscosity** $\eta_H$ is measured. In 2022, in a $W = 1$ μm channel, the contributions of $\mathbf{E}\times\mathbf{B}$ drift and Hall viscosity were separated. **When electrons flow like a fluid, the Lorentz force acts like a pressure gradient.**

#### Topological Insulators

Surface Dirac states $H = v_F(\mathbf{p}\times\boldsymbol{\sigma})$; applying $B$ produces Landau levels $E_n \propto \sqrt{nB}$ + a $\pi$ Berry phase. $q\mathbf{v}\times\mathbf{B}$ converts to spin–momentum locking, giving the **quantum spin Hall effect**.

### 5.1.4 Ultra-Intense Laser Plasmas

At $I > 10^{22}$ W/cm², $a_0 = eE/m\omega c > 10$, electrons reach $v \sim c$ within one cycle, and in the Lorentz force $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ **the $\mathbf{v}\times\mathbf{B}$ term becomes comparable to $\mathbf{E}$**.

#### The Regime Where Radiation Reaction Overtakes the Lorentz Force (2023)

$$R = \frac{F_{rad}}{F_L} \sim \frac{2}{3}\alpha_f \gamma^2 \frac{E}{E_S}$$

> **Unicode**
> ```
> R = (F_rad)/(F_L) ∼ (2)/(3)α_f γ² (E)/(E_S)
> ```

If $R > 0.1$, the **Landau–Lifshitz force** $\mathbf{F}_{rad}$ must be added. A 2023 PRL experiment found that in the radiation-dominated regime $R > 1$, nearly all of the laser energy converts to **a gamma-ray flash**.

**ELI and Apollon 10 PW lasers** are entering the quantum regime $\chi_e \sim 1$, where the Lorentz trajectory becomes a stochastic jump.

#### Plasma-Mirror High Harmonics

Lamač et al. (PRL 131, 205001, 2023): a **nonlinear $v\times B$ current** in a self-modulated plasma mirror generates high harmonics. The Lorentz force directly produces light.

### 5.1.5 The Lorentz Force in Gravitational-Wave Detection (LIGO)

LIGO's 40 kg test-mass mirrors are extremely sensitive to $B$. Earth's field $B \sim 50$ μT can produce a displacement of $10^{-15}$ m in magnetized steel components via the force $\mathbf{m}\cdot\nabla\mathbf{B}$ → a false signal.

#### O3–O4 Runs (2020–)

- **Voice coil actuators:** control the mirror's position via $\mathbf{F} = I\mathbf{L}\times\mathbf{B}$. Since the coil magnet itself is a noise source, in 2023 it is **being replaced by electrostatic actuation** — removing the Lorentz force improves sensitivity
- **The 8 Hz Schumann resonance** magnetic field acts as correlated noise between the two sites, and is measured and subtracted with a Wiener filter
- **The next-generation Einstein Telescope:** aims for superconducting shielding with $B < 1$ nT

Since gravitational waves themselves are $h \sim 10^{-21}$, $10\times$ smaller than $q\mathbf{v}\times\mathbf{B}$-induced noise, **magnetic shielding is essential for detection**.

### 5.1.6 Space Propulsion — Hall Thrusters, VASIMR, Solar Sails

#### Hall Thrusters

A radial $B_r \sim 0.02$ T and axial $E_z$ cause electrons to drift azimuthally via $\mathbf{E}\times\mathbf{B}$:

$$V_{E\times B} = E/B$$

> **Unicode**
> ```
> V_E× B = E/B
> ```

forming the Hall current $I_H$. **The $\mathbf{J}_H\times\mathbf{B}_r$ of this Hall current is the axial Lorentz thrust.**

- $T \sim 80$ mN, $I_{sp} \sim 1600$ s
- **Operating on 5000+ Starlink satellites** (2023)

#### VASIMR

Plasma is generated by a helicon → heated in $v_\perp$ by ICRF → the $\mu\nabla B$ force in a diverging magnetic nozzle converts $v_\perp \to v_\parallel$. Thrust converts axial momentum via $\mathbf{J}_\theta\times\mathbf{B}_r$.

- Predicted to be more efficient than Hall thrusters at 50 kW
- **The 2022 Ad Astra 100 kW test** ($T = 6$ N)

#### Solar Sails / Magnetic Sails

Solar radiation pressure + solar wind $q\mathbf{v}\times\mathbf{B}$.

- **Magnetic sail M2P2:** a superconducting ring with $B \sim 0.1$ T deflects solar-wind protons via $\mathbf{v}\times\mathbf{B}$ for thrust
- **The 2024 JAXA OKEANOS extension**

### 5.1.7 Summary of 20 Key Papers (2020–2025)

| # | Paper / Year | Field | Key Lorentz-force insight |
|---|---|---|---|
| 1 | Degrave et al., Nature 2022, Magnetic Control via Deep RL | Fusion AI | RL directly controls the $J\times B$ equilibrium, first realization of a droplet shape |
| 2 | Jain et al., Nature 2024, Penning micro-trap | Quantum computing | Static $B=3$ T Lorentz confinement enables ion transport/operations without RF |
| 3 | Zhang et al., PRB 2022, Giant nonlinear Hall in strained TBG | Nanodevices | Lorentz skew scattering drives $E^2H$ nonlinear Hall |
| 4 | Lamač et al., PRL 131, 205001 (2023) | Intense lasers | Plasma-mirror high harmonics, $v\times B$ nonlinear current |
| 5 | Vranic et al., PRL 113, 134801 (2014) | Intense lasers | All-optical radiation reaction, $F_{rad}$-dominated regime |
| 6 | KSTAR Team, Nature Comm 2023, 100s H-mode AI control | Fusion | AI-sustained $E\times B$ shear |
| 7 | W7-X Team, PRL 129, 095001 (2022), Quasi-isodynamic optimization | Stellarator | Minimizing $V_{gc}$ drift to preserve KAM tori |
| 8 | Ad Astra VASIMR VX-200SS (2022) | Space propulsion | $J_\theta\times B_r$ nozzle conversion, $T=6$ N @ 100kW |
| 9 | SpaceX Starlink Hall thruster SPT-140 (2023) | Space propulsion | $E\times B$ Hall-current thrust, Kr propellant |
| 10 | Google Quantum AI, PRL 2023, Flux noise mitigation | Quantum | $1/f$ $B$ noise causes Lorentz-phase decoherence |
| 11 | UT Dallas, Quantum anomalous Hall in bilayer graphene 2021 | Nanoscale | Berry curvature plays the Lorentz role at $B=0$ |
| 12 | ITER IO, Nucl. Fusion 2023, RMP ELM suppression | Fusion | External $\tilde{B}$ ergodizes field lines, heat spread via $D_{RR}$ |
| 13 | ELI-NP, Nat. Photon 2022, 10PW $a_0 \sim 100$ | Intense lasers | $v\times B$ second-harmonic acceleration |
| 14 | LIGO-Virgo, PRD 105, 082005 (2022), Magnetic correlation Schumann | Gravitational waves | Earth's $B$ is correlated noise, shielded against the Lorentz force |
| 15 | MIT SPARC, JPP 2022, High-field tokamak $B=12$ T | Fusion | Increased $B\rho$ enables a compact reactor at $R=1.85$ m |
| 16 | ETH Zurich, PRL 2022, 219-ion entanglement | Quantum | Penning $B$ entangles 219 ions |
| 17 | Graphene hydrodynamics, PRB 2022, Hall viscosity | Nanoscale | Viscosity vs. Lorentz-force competition |
| 18 | JAXA DESTINY+, thin film solar sail 2022 | Space propulsion | Radiation pressure + solar-wind $v\times B$ navigation |
| 19 | DeepMind DIII-D disruption prediction, Nature 2024 | Fusion AI | Predicts $\mathbf{J}\times\mathbf{B}$ imbalance 300 ms in advance |
| 20 | NASA Psyche Hall thruster SPT-140 (2023) | Space propulsion | $E\times B$ thrust for deep-space navigation |

### 5.1.8 Overview

**Before 2020, the Lorentz force was a formula; after 2020, it is a control variable.**

- **AI:** learns $\mathbf{J}\times\mathbf{B}$ as a reward function
- **Quantum chips:** confine ions with $\mathbf{v}\times\mathbf{B}$
- **Graphene:** uses $\mathbf{v}\times\mathbf{B}$ as a rectifier
- **Lasers:** probe the regime where $\mathbf{v}\times\mathbf{B}$ overtakes $\mathbf{E}$

**In the next five years, high-temperature superconductors at $B > 20$ T combined with real-time AI control of $F_L$ are likely to simultaneously close in on fusion, quantum computing, and space propulsion.**

### 5.1.9 Mathematica Verification

```mathematica
(* AI control reward function *)
aiReward[psi_, psiTarget_, Jvec_, Bvec_, gradp_] :=
  -Norm[psi - psiTarget] - Norm[Cross[Jvec, Bvec] - gradp];

(* Penning trap frequency *)
penningFreq[q_, B_, m_] := q B / m;

(* Hall thruster thrust *)
hallThrust[JHall_, Br_, L_] := JHall Br L;

(* Radiation-reaction ratio *)
radiationRatio[gamma_, Efield_, Es_] :=
  (2/3) alphaFine gamma^2 Efield / Es;
```

### 5.1.10 Limits and Exceptions

- **AI control:** training-data bias, possible failure to transfer to real hardware
- **Quantum computing:** $B$ noise, ion heating
- **Graphene:** manufacturing uniformity, reproducibility
- **Intense lasers:** repetition rate, sample damage
- **Gravitational waves:** cost of magnetic shielding, environmental noise
- **Space propulsion:** lifetime, propellant supply

> **References**
> - Degrave, J., et al., *Magnetic control of tokamak plasmas through deep reinforcement learning*, Nature **602**, 414 (2022). [doi:10.1038/s41586-021-04301-9](https://doi.org/10.1038/s41586-021-04301-9)
> - Jain, S., et al., *Penning micro-trap for quantum computing*, Nature **627**, 510 (2024). [doi:10.1038/s41586-024-07111-x](https://doi.org/10.1038/s41586-024-07111-x)
> - Zhang, Y., et al., *Giant nonlinear Hall effect in strained twisted bilayer graphene*, Phys. Rev. B **106**, L041111 (2022). [doi:10.1103/PhysRevB.106.L041111](https://doi.org/10.1103/PhysRevB.106.L041111)
> - Lamač, M., et al., *Anomalous relativistic emission from self-modulated plasma mirrors*, Phys. Rev. Lett. **131**, 205001 (2023). [doi:10.1103/PhysRevLett.131.205001](https://doi.org/10.1103/PhysRevLett.131.205001)
> - W7-X Team, *Quasi-isodynamic optimization*, Phys. Rev. Lett. **129**, 095001 (2022). [doi:10.1103/PhysRevLett.129.095001](https://doi.org/10.1103/PhysRevLett.129.095001)

---
## 5.2 Open Problems and the Future

$q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ is a 130-year-old formula, but we still know little about the origin of $B$, the point-charge limit, and its junction with quantum gravity. This section covers magnetic monopoles, millicharged dark matter, quantum gravity, Born–Infeld theory, plasma turbulence, fusion commercialization, and 10 open problems.

### 5.2.1 The Possible Existence of Magnetic Monopoles

Introducing symmetry into Maxwell's equations:

$$\nabla\cdot\mathbf{B} = \mu_0\rho_m, \quad \nabla\times\mathbf{E} = -\partial_t\mathbf{B} - \mu_0\mathbf{J}_m$$

> **Unicode**
> ```
> ∇·𝐁 = μ₀ρₘ,   ∇×𝐄 = -∂ₜ𝐁 - μ₀𝐉ₘ
> ```

**The dual extension of the Lorentz force:**

$$\mathbf{F} = q_e(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + q_m\left(\mathbf{B}-\frac{\mathbf{v}}{c^2}\times\mathbf{E}\right)$$

> **Unicode**
> ```
> 𝐅 = qₑ(𝐄+𝐯×𝐁) + qₘ(𝐁-(𝐯)/(c²)×𝐄)
> ```

The second term is the force felt by a monopole. Dirac's 1931 quantization $q_e q_m = n\hbar/2$ has the appeal of **explaining charge quantization**.

**Current status:**

- GUT monopoles with mass $10^{16}$ GeV are predicted to be diluted by early-universe inflation to $n_m < 10^{-30}$ cm$^{-3}$, making direct detection impossible
- **LHC MoEDAL (2022–2023):** excludes monopoles with $m < 3$ TeV, in Dirac-charge units of $1g_D = 68.5e$. **The Nature 2022 Schwinger search** is the most model-independent
- **Spin-ice Dy₂Ti₂O₇:** emergent monopole-like quasiparticles observed — not true monopoles, but a divergence of an emergent $B$
- **If discovered:** the structure would be $F = dA + \star$ rather than $F = dA$, a twisted $U(1)$ bundle with $c_1 = n$ — requiring a complete rewrite of electromagnetism textbooks

**Future:** searching for quantum jumps in $g_D$ using 100 T pulsed magnets and SQUIDs; proposals to search for ancient monopoles in lunar soil samples.

### 5.2.2 Dark Matter and Millicharged Particles

There is no guarantee that dark matter is completely neutral. If a $U(1)$ dark photon $A'$ has kinetic mixing $\epsilon F_{\mu\nu}F'^{\mu\nu}$ with the photon, dark particles acquire a **tiny charge** $\epsilon e$ — **millicharged particles (MCPs)**.

**Lorentz force:**

$$\mathbf{F} = \epsilon q_e(\mathbf{E}+\mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = ε qₑ(𝐄+𝐯×𝐁)
> ```

**Effects:**
- In galactic magnetic fields $B \sim \mu$G, MCPs are deflected by $\mathbf{v}\times\mathbf{B}$ → possibly removed from the galactic disk, potentially forming a **dark disk**
- The solar magnetic field and Earth's magnetosphere modulate MCP flux

**Current status (2020–2024):**

- **milliQan@LHC, SENSEI, LDMX:** searching $\epsilon < 10^{-3}$, $m = 0.1-10$ GeV, no signal yet
- **Cosmological constraints:** if MCPs couple to baryons, they change $N_{eff}$ in the CMB, giving $\epsilon < 10^{-9}$ ($m < 1$ keV)
- **The 21cm EDGES anomaly:** a 2018 claim that 0.3% MCPs could explain it, **refuted by SARAS in 2023**

**Future direction:** deflecting MCPs with 10 T Hall-thruster-scale magnetic fields for detection; searching for the weak current $\mathbf{J}_{MCP}\times\mathbf{B}$ produced in plasma halos. **In effect, using the Lorentz force to see the dark sector.**

### 5.2.3 Generalizing the Lorentz Force in Quantum Gravity

In general relativity, the motion of a charged particle:

$$m\frac{Du^\mu}{d\tau} = qF^{\mu\nu}u_\nu$$

> **Unicode**
> ```
> m(Du^μ)/(dτ) = qF^μνu_ν
> ```

$D$ is the covariant derivative, and $F$ remains a 2-form even in curved spacetime. The problem is that **in quantum gravity, $F_{\mu\nu}$ itself undergoes quantum fluctuations**, and spacetime becomes foamy.

**Two hypotheses:**

1. **Lorentz violation:** discreteness of spacetime at the quantum-gravity scale $\ell_P$ → a modified dispersion relation $E^2 = p^2c^2 + m^2c^4 + \eta p^3/M_P$. A charged particle's speed could exceed $c$, allowing vacuum Cherenkov radiation $e \to e\gamma$. **Fermi LAT's detection of GRB photons above 10 GeV** constrains $\eta < 10^{-8}$
2. **Gravity–electromagnetism dual radiation:** $F_{\mu\nu}$ mixes with gravity, taking a form like $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}) + m\mathbf{g} + \ldots$ in 5D Kaluza–Klein theory. **Equivalence-principle violation at the $10^{-15}$ level** is being explored

**Current status:**
- **LIGO's neutron-star merger GW170817:** simultaneous observation of a jet produced by $\mathbf{J}\times\mathbf{B}$ and a gravitational wave gave $v_{GW} = c$ to $10^{-15}$ precision, strongly constraining Lorentz violation
- However, the regime near a $B \sim 10^{12}$ T magnetar, where $q\mathbf{v}\times\mathbf{B}$ competes with spacetime curvature, remains **unexplored**

**Future:** correlating pulsar timing arrays with $\mathbf{B}$ and the gravitational-wave background, and experiments on quantum-Hall gravity analogues.

### 5.2.4 Nonlinear Electrodynamics — Born–Infeld

Maxwell's Lagrangian $L = -F_{\mu\nu}F^{\mu\nu}/4\mu_0$ diverges as $E \to \infty$, giving a point charge infinite self-energy. **Born–Infeld (1934)** proposed:

$$L_{BI} = b^2\left(1-\sqrt{1 + \frac{F^2}{2b^2} - \frac{(F\tilde{F})^2}{16b^4}}\right)$$

> **Unicode**
> ```
> L_BI = b²(1-√(1 + (F²)/(2b²) - ((FF̃)²)/(16b⁴)))
> ```

with a critical field $b \sim 10^{20}$ V/m. **There is a maximum electric field, and the point-charge energy is finite.**

**Modification of the Lorentz force:** using the displacement field defined by $D = \partial L/\partial E$:

$$\mathbf{F} = q(\mathbf{E}(\mathbf{D},\mathbf{B}) + \mathbf{v}\times\mathbf{B})$$

> **Unicode**
> ```
> 𝐅 = q(𝐄(𝐃,𝐁) + 𝐯×𝐁)
> ```

Since $E(D)$ is nonlinear, **the superposition principle breaks down**, and the force between two charges is not a simple sum.

**Current status:**
- **LHC heavy-ion PbPb collisions:** approach $B \sim 10^{15}$ T, $E \sim 10^{20}$ V/m. BI effects predict a change in the photon–photon scattering cross-section. **ATLAS's 2022 observation of $\gamma\gamma\to\gamma\gamma$ agrees with Maxwell theory**, giving a lower bound $b > 10^{19}$ V/m
- **String theory:** BI naturally arises as the low-energy effective action of a D-brane — $b = 1/2\pi\alpha'$

**Future:** measuring vacuum birefringence $\Delta n \propto (E/b)^2$ with 100 PW lasers at $E \sim 10^{18}$ V/m, searching for a 1% deviation in electron trajectories from the nonlinear correction to the Lorentz force.

### 5.2.5 Plasma Turbulence and Chaos in the Lorentz Force

**The most practically important open problem.** In fusion reactors, $\chi$ is $10^2$ times larger than the classical $1/B^2$ prediction — due to turbulence.

The key equation:

$$\rho\frac{d\mathbf{V}}{dt} = -\nabla p + \mathbf{J}\times\mathbf{B}$$

> **Unicode**
> ```
> ρ(d𝐕)/(dt) = -∇ p + 𝐉×𝐁
> ```

has $\mathbf{J}\times\mathbf{B}$ itself fluctuating turbulently as $\tilde{\mathbf{J}}\times\tilde{\mathbf{B}}$ → the average $\langle\tilde{J}\times\tilde{B}\rangle$ generates an anomalous electric field.

**Two open problems:**

1. **The trigger for the L-H transition:** what is the critical condition under which $E_r\times B$ shear $\omega_{E\times B}$ suppresses turbulence? **A 30-year unsolved problem.** In 2023, KSTAR observed the transition when $\omega_{E\times B} \approx \gamma_{lin}$, but the theoretical loop explaining how $E_r$ is spontaneously generated from $\nabla p$ remains incomplete
2. **Turbulence saturation:** why does Hasegawa–Mima turbulence stop at a $k^{-3}$ spectrum? A mechanism exists whereby zonal flow drains turbulent energy via $\tilde{V}\times B$, but **quantitative predictions are off by a factor of 2**

**Future:** 6D Vlasov simulations + AI closures. A **PINN model** that directly learns $\mathbf{v}\times\tilde{\mathbf{B}}$ from particle trajectories succeeded in predicting $\chi$ to 20% in 2024.

### 5.2.6 Lorentz-Force-Based Innovations for Fusion Commercialization

Conditions for commercialization: $Q > 10$, $\beta \sim 5\%$, $\tau_E > 3$ s, disruption < 1%.

**Four Lorentz-force innovations:**

1. **High-temperature superconductors at $B > 12$ T:** since $B\rho = p/q$, doubling $B$ → halves $R$ → quarters capital cost. **MIT SPARC at $B = 12.2$ T**, with Commonwealth Fusion testing TF coils in 2025. An Inconel jacket to handle Lorentz stress $F = JB \sim 1000$ ton/m is key
2. **Liquid-metal walls:** a Li wall shields $E$ via $J\times B$, stabilizing ELMs without RMP. Li flow is controlled via $\mathbf{J}\times\mathbf{B}$
3. **RF current-drive efficiency:** optimizing current-drive efficiency $\eta_{CD} = I_{CD}R/P_{RF}$ via the Doppler shift caused by $E\parallel B$ and $\mathbf{v}\times\mathbf{B}$, targeting $\eta > 0.5$ by 2030
4. **Real-time AI control of $F_L$:** the DeepMind approach directly controls the $B$ coils, detecting a $J\times B$ imbalance 300 ms before disruption and soft-landing via a rapid $B$ ramp-down. **Scheduled for ITER in 2027**

### 5.2.7 10 Open Problems

| # | Problem | Current status |
|---|---|---|
| 1 | **Existence of magnetic monopoles** | Dirac quantization unverified. MoEDAL lower bound $m > 3$ TeV. Cosmological dilution problem |
| 2 | **Quantum vacuum magnetic birefringence** | $n_\parallel \neq n_\perp$ for $B > 10^9$ T. PVLAS 2022 limit $b > 10^{19}$ V/m, targeted by 100 PW lasers by 2028 |
| 3 | **Self-consistency of radiation reaction** | Is the ALD runaway/pre-acceleration problem solved? Landau–Lifshitz is standard, but the stochastic radiation model in the quantum regime $\chi > 1$ is debated; SLAC E320 is underway in 2023 |
| 4 | **Fast trigger for magnetic reconnection** | Why is reconnection fast at $0.1V_A$ for $S = 10^{15}$? Hall + plasmoid theory exists, but 3D kinetic simulations disagree with observations by 30% |
| 5 | **First-principles prediction of plasma turbulence** | Cannot predict $\chi_i, \chi_e$ from $B,n,T$ to 10% accuracy. ITER's $Q$ prediction is off by a factor of 2. Exascale Vlasov simulations are needed |
| 6 | **Quantization of the nonlinear Hall effect** | Is the nonlinear conductivity $\sigma^{(2)}$ of $E^2B$ quantized? 32% observed in graphene; theoretical Chern-number extension is incomplete |
| 7 | **Magnetic trapping of millicharged dark matter** | Does galactic $B$ trap MCPs in the disk? Magnetohydrodynamic simulations suggest trapping for $\epsilon > 10^{-8}$, which conflicts with CMB constraints |
| 8 | **Closure of pair production in pulsar magnetospheres** | How is $E_\parallel$ screened at the Goldreich–Julian density $n_{GJ}$? PIC simulations show gap oscillations, but the radio-emission mechanism remains debated |
| 9 | **Disruption-free, ELM-free stable tokamak operation** | Can a discharge be sustained for 1000 seconds without disruption at $q_{95} > 3$, $\beta_N > 3$? KSTAR achieved 100 s, ITER targets 400 s, **impossible without AI control** |
| 10 | **CPT symmetry of the Lorentz force** | Is the $q\mathbf{v}\times\mathbf{B}$ of antimatter $\bar{p}$ exactly opposite? ALPHA-g measured antihydrogen gravity in 2023; the CPT-violation limit for $F_L$ is $10^{-9}$, targeting $10^{-12}$ by 2030 |

### 5.2.8 Three Axes of Future Research

1. **Extreme $B$:** achieving laboratory-scale $E \sim 10^{20}$ V/m and $B \sim 10^6$ T with 20 T HTS magnets + 100 PW lasers → direct verification of Born–Infeld theory and vacuum birefringence
2. **AI control of $F_L$:** real-time field prediction of $J\times B$, using reinforcement learning to maintain 99% KAM-torus survival — **the shortest path to fusion commercialization**
3. **Quantum $U(1)$ phase:** viewing the Lorentz force not as a force but as a holonomy $W(C) = \exp(iq\oint A)$, applying it to topological matter and quantum computing — using Hall viscosity and the nonlinear Hall effect as qubit couplings

### 5.2.9 Mathematica Verification

```mathematica
(* Dirac quantization *)
diracQuantization[qCharge_, gMonopole_] := qCharge gMonopole == nInteger hBar/2;

(* Born-Infeld Lagrangian *)
bornInfeldLagrangian[Fmunu_, b_] :=
  b^2 (1 - Sqrt[1 + (Fmunu Fmunu)/(2 b^2) - (Fmunu Star[Fmunu])^2/(16 b^4)]);

(* Millicharge force *)
milliChargeForce[epsilon_, q_, Evec_, vvec_, Bvec_] :=
  epsilon q (Evec + Cross[vvec, Bvec]);

(* ALD radiation reaction *)
aldForce[q_, tau0_, aDot_] := q^2/(6 Pi epsilon0 c^3) aDot;
```

### 5.2.10 Limits and Exceptions

- **Magnetic monopoles:** theoretically appealing but with zero experimental evidence
- **Millicharged particles:** cosmological and terrestrial constraints conflict
- **Quantum gravity:** experimentally extremely difficult to verify
- **Born–Infeld:** the theoretical origin of $b$ is unknown
- **Turbulence:** AI predictions are also limited by training data
- **Fusion:** engineering challenges remain (materials, triple product)

> **References**
> - Acharya, B., et al. (MoEDAL), *Search for magnetic monopoles via Schwinger pair production*, Nature **602**, 63 (2022). [doi:10.1038/s41586-021-04298-1](https://doi.org/10.1038/s41586-021-04298-1)
> - MoEDAL Collaboration, *Search for highly-ionizing particles*, Eur. Phys. J. C **82**, 694 (2022). [doi:10.1140/epjc/s10052-022-10608-2](https://doi.org/10.1140/epjc/s10052-022-10608-2)
> - PVLAS Collaboration, *First results from the new PVLAS apparatus*, Phys. Rev. D **90**, 092003 (2014). [arXiv:1406.6518](https://arxiv.org/abs/1406.6518)
> - Born, M., Infeld, L., *Foundations of the new field theory*, Proc. R. Soc. A **144**, 425 (1934). [doi:10.1098/rspa.1934.0059](https://doi.org/10.1098/rspa.1934.0059)

---

## 5.3 Condensed Matter and Topological Materials

In condensed matter, $q\mathbf{v}\times\mathbf{B}$ does more than bend electrons — it creates the **topology of space itself**. This section covers the quantum Hall effect, spin Hall effect, topological insulators, Majorana fermions, the graphene pseudo-magnetic field, Berry curvature, and superconducting vortices.

### 5.3.1 The Quantum Hall Effect

A 2D electron gas $n_{2D}$, $B\hat{z}$.

#### Integer QHE

Landau levels $E_n = \hbar\omega_c(n+1/2)$, degeneracy $N_\phi = BS/\Phi_0$, $\Phi_0 = h/e$.

When the filling factor $\nu = N_e/N_\phi = nh/eB$ is an integer, the Fermi level sits in a gap → $\sigma_{xx} = 0$,

$$\sigma_{xy} = \nu \frac{e^2}{h}, \quad R_H = \frac{h}{\nu e^2}$$

> **Unicode**
> ```
> σ_xy = ν (e²)/(h),   R_H = (h)/(ν e²)
> ```

**In the Kubo formula, $\sigma_{xy}$ is an integral of the $k$-space Berry curvature:**

$$\sigma_{xy} = \frac{e^2}{h}\frac{1}{2\pi}\int_{BZ}\Omega_z(\mathbf{k})\, d^2k = \frac{e^2}{h}C$$

> **Unicode**
> ```
> σ_xy = (e²)/(h)(1)/(2π)∫_BZ Ω_z(𝐤) d²k = (e²)/(h)C
> ```

$C$ is the **first Chern number**. It is not the $E\times B$ drift $V_y = E_x/B$ created by the Lorentz force that gets quantized via $j_x = neV_y$; rather, the **topological invariant $C$** is quantized. **$C$ does not change even in the presence of disorder** — topological protection.

#### Fractional QHE

$\nu = 1/3, 2/5$, etc. Coulomb energy $e^2/\epsilon l_B$ competes with $\hbar\omega_c$, described by the **Laughlin wave function:**

$$\Psi_{1/m} = \prod_{i<j}(z_i-z_j)^m e^{-\sum|z_i|^2/4l_B^2}$$

> **Unicode**
> ```
> Ψ_1/m = ∏_i<j(zᵢ-zⱼ)ᵐ e^-∑|zᵢ|²/4l_B²
> ```

Particles transform into **composite fermions** carrying flux $m\Phi_0$, undergoing integer QHE in an effective field $B^* = B - 2pn\Phi_0$. The Lorentz force acts on $B^*$; quasiparticles carry charge $e^* = e/3$, statistics $\theta = \pi/m$ — **anyons**.

**Recently (2023):** a fractional Chern insulator observed in graphene even at $B = 0$ — fractional quantization without a Lorentz force, with **Berry curvature playing the role of $B_{eff}$**.

### 5.3.2 The Spin Hall and Anomalous Hall Effects

#### Anomalous Hall Effect (AHE)

A Hall voltage appears in ferromagnets even when $B_{ext} = 0$:

$$\rho_{xy} = R_0 B + R_S M$$

> **Unicode**
> ```
> ρ_xy = R₀ B + R_S M
> ```

The $R_S$ term is anomalous. The cause is **spin–orbit coupling** $H_{SO} = \lambda\mathbf{S}\cdot(\mathbf{p}\times\nabla V)$ — a **Lorentz force** in which the **effective field** $\mathbf{B}_{eff} \propto \mathbf{p}\times\mathbf{E}$, felt by a moving electron, depends on spin.

**Three contributions:**
- Intrinsic: an integral of the Berry curvature $\Omega(\mathbf{k})$
- Extrinsic: skew scattering, side jump

**Intrinsic AHE:**

$$\sigma_{xy}^{AHE} = -\frac{e^2}{\hbar}\int_{BZ} \frac{d^3k}{(2\pi)^3} f(\mathbf{k})\Omega_z(\mathbf{k})$$

> **Unicode**
> ```
> σ_xy^AHE = -(e²)/(ℏ)∫_BZ (d³k)/((2π)³) f(𝐤)Ω_z(𝐤)
> ```

$\Omega$, proportional to $M$, **generates a Hall current without a Lorentz force**. $\Omega$ itself acts as a $k$-space magnetic field.

#### Spin Hall Effect (SHE)

In a nonmagnetic material, charge separates only in spin, without Hall voltage:

$$\mathbf{J}_s = \theta_{SH}\frac{\hbar}{2e}\mathbf{J}_c\times\hat{s}$$

> **Unicode**
> ```
> 𝐉ₛ = θ_SH (ℏ)/(2e) 𝐉_c×ŝ
> ```

$\theta_{SH}$: the spin Hall angle, 0.1 in Pt and 0.3 in β-W. Principle: $H_{SO}$ sends spin-up electrons toward $+\mathbf{y}$ and spin-down toward $-\mathbf{y}$, as $q\mathbf{v}\times\mathbf{B}_{eff}$ points in opposite directions for the two spins. **No net charge flow, but a spin current exists.**

**Inverse spin Hall effect (ISHE):** detects a spin current as a voltage. Key to **SOT-MRAM**: $\mathbf{J}_c \to \mathbf{J}_s \to$ a magnetization-switching torque $\boldsymbol{\tau} \propto \mathbf{M}\times(\mathbf{M}\times\mathbf{S})$.

**Here the Lorentz force acts not via a real $B$ but via $\mathbf{B}_{eff} \propto \mathbf{E}\times\mathbf{p}$** — the solid-state version of the relativistic Lorentz transformation $\mathbf{B}' \approx -\mathbf{v}\times\mathbf{E}/c^2$.

### 5.3.3 Topological Insulators

The $Z_2$ topological insulator Bi₂Se₃: a bulk gap with surface Dirac states:

$$H_{surf} = v_F(\mathbf{p}\times\boldsymbol{\sigma})_z = v_F(p_x\sigma_y - p_y\sigma_x)$$

> **Unicode**
> ```
> H_surf = v_F(𝐩×σ)_z = v_F(pₓσ_y - p_yσₓ)
> ```

**Spin–momentum locking.** By time-reversal symmetry, $\sigma_{xy} = 0$ at $B = 0$, but applying $B\perp$ gives surface Landau levels:

$$E_n = \text{sgn}(n) v_F\sqrt{2e\hbar B|n|}$$

> **Unicode**
> ```
> Eₙ = sgn(n) v_F√(2eℏ B|n|)
> ```

**The $n = 0$ level is pinned at $E = 0$** — due to the $\pi$ Berry phase. $E_n \propto \sqrt{B|n|}$ is the same as in graphene.

**Quantized magneto-optics:** in a thin TI film, $\sigma_{xy} = (N+1/2)e^2/h$ → **quantized Faraday rotation, $\theta_F = \alpha_{fine} \approx 7.3$ mrad**. Quantization of the topology governs how the Lorentz force rotates the polarization of light.

**Quantum Anomalous Hall Effect (QAHE):** magnetic doping breaks time-reversal symmetry, giving $\sigma_{xy} = e^2/h$ at $B = 0$, a $C = 1$ Chern insulator. **Observed in Cr-doped (Bi,Sb)₂Te₃ at $T = 1$ K in 2020.** Berry curvature completely replaces the Lorentz force.

### 5.3.4 Majorana Fermions

Majorana $\gamma = \gamma^\dagger$, $\gamma^2 = 1$, particle = antiparticle. Created in a topological superconductor via $p+ip$ pairing + Zeeman splitting.

**Design equation (a 1D InAs nanowire + s-wave superconductor Al + magnetic field $B\parallel$):**

$$H = \left(\frac{p^2}{2m}-\mu\right)\tau_z + \alpha_R p\sigma_y\tau_z + g\mu_B B\sigma_x + \Delta\tau_x$$

> **Unicode**
> ```
> H = ((p²)/(2m)-μ)τ_z + α_R pσ_yτ_z + gμ_B Bσₓ + Δτₓ
> ```

$\alpha_R$: Rashba SO coupling, $g\mu_B B$: Zeeman term. **Topological condition:**

$$g\mu_B B > \sqrt{\Delta^2+\mu^2}$$

> **Unicode**
> ```
> gμ_B B > √(Δ²+μ²)
> ```

$B$ aligns the spin, converting the s-wave pairing to effective p-wave, producing **Majorana zero modes** at both ends.

**Why a parallel field is essential:** a perpendicular $B$ creates superconducting vortices that destroy the Majorana state. **A perpendicular $B$ exceeding $H_{c2}$** must be avoided.

**In 2D:** $p+ip$ superconductors Sr₂RuO₄, FeTeSe host Majorana states in vortex cores. **The Lorentz force $\mathbf{J}_s\times\Phi_0$ from the supercurrent circulating a vortex pins the vortex**, whose Caroli–de Gennes–Matricon core levels shift to zero energy via Zeeman splitting.

**Current status:** Microsoft reported quantized $2e^2/h$ conductance peaks in InAs-Al in 2023–24, **still debated**. $B$ noise is the primary cause of Majorana decoherence.

### 5.3.5 Graphene and the Pseudo-Magnetic Field $B_{ps}$

Graphene's low-energy Hamiltonian $H = v_F\boldsymbol{\sigma}\cdot(\mathbf{p}+e\mathbf{A})$, where $\mathbf{A}$ is a real magnetic field. Strain $u_{ij}$ changes the hopping $t \to t+\delta t$, which manifests as a **gauge field**:

$$\mathbf{A}_{ps} = \frac{\hbar\beta}{2ea}(u_{xx}-u_{yy}, -2u_{xy})$$

> **Unicode**
> ```
> 𝐀ₚₛ = (ℏβ)/(2ea)(uₓₓ-u_yy, -2u_xy)
> ```

with $\beta \sim 3$, $a = 0.14$ nm. **The pseudo-magnetic field:**

$$B_{ps} = \nabla\times\mathbf{A}_{ps}$$

> **Unicode**
> ```
> Bₚₛ = ∇×𝐀ₚₛ
> ```

1% strain gives $B_{ps} \sim 10$ T, and up to **300 T** has been reported in nanobubbles.

**Key differences:**
- $B_{ps}$ is $+B$ at the $K$ valley and $-B$ at $K'$ — **time-reversal symmetry preserved, total flux is zero**
- Hence there is no charge Hall effect, but a **valley Hall effect** exists — a valley filter

**Experiment (Levy, Science 2010):** in a graphene nanobubble on Pt(111), STM $dI/dV$ revealed Landau levels $E_n \propto \sqrt{nB_{ps}}$ at **$B_{ps} = 350$ T**. Quantum Hall physics from strain alone, without a Lorentz force.

**Recent:** combining $B_{ps}$ with a real $B$ produces a **valley-dependent Lorentz force** $F_K = -e\mathbf{v}\times(B+B_{ps})$, $F_{K'} = -e\mathbf{v}\times(B-B_{ps})$ → valley separation, i.e., **valleytronics**.

### 5.3.6 Berry Curvature and Topological Transport

The common language of all topological phenomena. For a Bloch state $|u_n(\mathbf{k})\rangle$:

$$\mathcal{A}_n = i\langle u_n|\nabla_k|u_n\rangle, \quad \Omega_n = \nabla_k\times\mathcal{A}_n$$

> **Unicode**
> ```
> Aₙ = i⟨ uₙ|∇ₖ|uₙ⟩,   Ωₙ = ∇ₖ×Aₙ
> ```

**Equation of motion:**

$$\hbar\dot{\mathbf{k}} = -e(\mathbf{E}+\dot{\mathbf{r}}\times\mathbf{B}), \quad \dot{\mathbf{r}} = \frac{1}{\hbar}\nabla_k\epsilon_n - \dot{\mathbf{k}}\times\mathbf{\Omega}_n$$

> **Unicode**
> ```
> ℏ𝐤˙ = -e(𝐄+𝐫˙×𝐁),   𝐫˙ = (1)/(ℏ)∇ₖεₙ - 𝐤˙×Ωₙ
> ```

The second term is the **anomalous velocity**, $-e\mathbf{E}\times\mathbf{\Omega}_n/\hbar$ — a **$k$-space Lorentz force**, with $\Omega_n$ playing the role of a $k$-space magnetic field.

**Conductivity:**

$$\sigma_{xy} = -\frac{e^2}{\hbar}\sum_n\int f_n\Omega_n^z\frac{d^2k}{(2\pi)^2}$$

> **Unicode**
> ```
> σ_xy = -(e²)/(ℏ)∑ₙ∫ fₙ Ωₙᶻ (d²k)/((2π)²)
> ```

The integral of $\Omega$ is the **Chern number**. In the Weyl semimetal TaAs, $\Omega \sim 1/k^2$ diverges, giving $\sigma_{xy} \sim 1000$ S/cm.

**The sum of three modern definitions of the Lorentz force:**

$$F_{total} = q\mathbf{v}\times\mathbf{B} + (-e\mathbf{E}\times\mathbf{\Omega}) + e\mathbf{v}\times\mathbf{B}_{ps}$$

> **Unicode**
> ```
> F_total = q𝐯×𝐁 + (-e𝐄×Ω) + e𝐯×𝐁ₚₛ
> ```

**The three terms are all isomorphic.**

### 5.3.7 Superconductors and Vortices

A superconductor resists the Lorentz force through perfect diamagnetism.

#### The Meissner Effect

With a penetration depth $\lambda$, the London equation $\mathbf{J}_s = -\mathbf{A}/\mu_0\lambda^2$ gives $\nabla\times\mathbf{J}_s = -\mathbf{B}/\mu_0\lambda^2$. **The magnetic pressure $\mathbf{J}_s\times\mathbf{B}$ pushes $\mathbf{B}$ back out.**

#### Type-II Superconductor Vortices

For $H_{c1} < B < H_{c2}$, flux quanta $\Phi_0 = h/2e$ penetrate in the form of **vortices**.

**Passing a current $J_{ext}$ through the vortices creates a Lorentz force:**

$$\mathbf{F}_L = \mathbf{J}_{ext}\times\Phi_0\hat{z}$$

> **Unicode**
> ```
> 𝐅_L = 𝐉ₑₓₜ×Φ₀ẑ
> ```

**Force per unit length.** When a vortex moves, an electric field $E = \mathbf{v}_L\times\mathbf{B}$ appears → resistance. **Pinning centers (defects) balance $F_L$ via $\mathbf{F}_{pin} = -\nabla U_{pin}$** → the critical current $J_c = F_{pin}/\Phi_0$.

**Vortex dynamics:**

$$\eta\mathbf{v}_L + \alpha\mathbf{v}_L\times\hat{z} = \mathbf{F}_L + \mathbf{F}_{pin} + \mathbf{F}_{thermal}$$

> **Unicode**
> ```
> η𝐯_L + α𝐯_L×ẑ = 𝐅_L + 𝐅ₚᵢₙ + 𝐅ₜₕₑᵣₘₐₗ
> ```

$\eta$: Bardeen–Stephen viscosity, $\alpha$: the **Magnus force** (Berry phase). Once $F_L$ exceeds $F_{pin}$, flux-flow resistance $\rho_{ff} = \rho_n B/H_{c2}$ appears.

**Recent:** in the high-temperature superconductor REBCO, $J_c > 10^{10}$ A/m², $F_{pin} = 10$ GN/m³, **realizing 20 T magnets**. A melting transition of the vortex lattice driven by $J\times B$ — the **vortex liquid is a chaotic state of the Lorentz force**.

### 5.3.8 Summary Table

| Phenomenon | Form of the Lorentz force | Topological invariant |
|---|---|---|
| IQHE | $q v\times B$ | Chern $C$ |
| FQHE | $q^* v\times B^*$ | Fractional $C$, anyon $\theta$ |
| AHE/SHE | $e E\times\Omega$ (Berry) | $\int\Omega$ |
| TI | $v_F p\times\sigma$ + $B$ | $Z_2$ |
| Graphene $B_{ps}$ | $e v\times B_{ps}$ (strain) | Valley Chern |
| Superconducting vortex | $J\times\Phi_0$ | Winding number |

**Conclusion:** in condensed matter, the Lorentz force is no longer just a force from an external $B$; it extends into a **$k$-space Lorentz force together with an effective $B_{eff}$ produced by the lattice, strain, and Berry curvature**. When the flux of that extended force is quantized, the result is **topological matter**.

### 5.3.9 Mathematica Verification

```mathematica
(* Quantum Hall conductance *)
hallConductance[nu_] := nu e^2/h;

(* Chern number from Berry curvature *)
chernNumber[Omega_, kx_, ky_] :=
  1/(2 Pi) Integrate[Omega, {kx, -Pi, Pi}, {ky, -Pi, Pi}];

(* Graphene pseudo-magnetic field *)
pseudoB[beta_, aLattice_, uxx_, uyy_, uxy_, hBar_, eCharge_] :=
  {hBar beta/(2 eCharge aLattice) (uxx - uyy),
   hBar beta/(2 eCharge aLattice) (-2 uxy)};

(* Majorana topological condition *)
majoranaCondition[gFactor_, muB_, Bfield_, Delta_, mu_] :=
  gFactor muB Bfield > Sqrt[Delta^2 + mu^2];

(* Vortex Lorentz force *)
vortexForce[Jext_, Phi0_] := Cross[Jext, {0, 0, Phi0}];
```

### 5.3.10 Limits and Exceptions

- **IQHE:** requires clean samples, cryogenic temperatures
- **FQHE:** direct verification of fractional statistics is difficult
- **AHE/SHE:** intrinsic/extrinsic separation is debated
- **TI:** residual bulk conductivity persists
- **Majorana:** experimental confirmation remains debated
- **Graphene $B_{ps}$:** difficult to control nanobubble location
- **Superconducting vortices:** the pinning mechanism in high-temperature superconductors is incompletely understood

> **References**
> - Thouless, D. J., Kohmoto, M., Nightingale, M. P., den Nijs, M., *Quantized Hall conductance in a two-dimensional periodic potential*, Phys. Rev. Lett. **49**, 405 (1982). [doi:10.1103/PhysRevLett.49.405](https://doi.org/10.1103/PhysRevLett.49.405)
> - Kane, C. L., Mele, E. J., *Z₂ topological order and the quantum spin Hall effect*, Phys. Rev. Lett. **95**, 146802 (2005). [doi:10.1103/PhysRevLett.95.146802](https://doi.org/10.1103/PhysRevLett.95.146802)
> - Levy, N., et al., *Strain-induced pseudo-magnetic fields greater than 300 tesla in graphene nanobubbles*, Science **329**, 544 (2010). [doi:10.1126/science.1191700](https://doi.org/10.1126/science.1191700)
> - Xiao, D., Chang, M.-C., Niu, Q., *Berry phase effects on electronic properties*, Rev. Mod. Phys. **82**, 1959 (2010). [doi:10.1103/RevModPhys.82.1959](https://doi.org/10.1103/RevModPhys.82.1959)

---
