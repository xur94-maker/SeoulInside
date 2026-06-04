# Black Hole Physics in Yang-Mills Collider v3.2

---

## 1. What Is Currently Implemented

### 1.1 Newtonian Gravity

The simplest form of gravity:

```
F = G * M * m / r^2
```

In code, log-corrected to match scene scale:

```
gAcc = log10(BH_MASS + 1) * 120.0 / (r^2 + 1.0)
dp/dt = -gAcc * (r_hat) * dt
```

Rather than curving spacetime, this approach directly adds force to momentum.  
It is Newtonian — yet all particles, regardless of mass or charge, are attracted equally.  
This effectively reproduces the **Equivalence Principle**.

---

### 1.2 Event Horizon Approximation

The event horizon radius of a Kerr black hole:

```
r_+ = M * (1 + sqrt(1 - a*^2))
```

where a* = a/M is the dimensionless spin parameter (0 to 1).

Code approximation:

```
Rs_base = max(0.8, log10(BH_MASS + 1) * 0.6)
Rs = Rs_base * (1 + sqrt(max(0, 1 - BH_SPIN^2))) * 0.5
if r < Rs * 2 : absorbed = true
```

Reflects the fact that the horizon shrinks to its minimum when spin is maximal (a* = 1).

---

### 1.3 Frame Dragging — Lense-Thirring Approximation

A defining effect of the Kerr metric. A rotating mass drags the surrounding spacetime along with it.

Exact expression:

```
Ω_LT ~ 2 * G * J / (c^2 * r^3)
```

where J = angular momentum.

Code approximation (simplified as a tangential force):

```
r_xz = sqrt(dx^2 + dz^2)
fdAcc = BH_SPIN * log10(BH_MASS+1) * 55.0 / (r^3 + 1.0)
tx = -dz / r_xz   (tangential unit vector, Y-axis rotation)
tz =  dx / r_xz
dp_x/dt += fdAcc * tx * dt
dp_z/dt += fdAcc * tz * dt
```

A tangential acceleration is used instead of full tensor computation.  
Despite this, spiral infall and the Penrose process emerge as outcomes.

---

### 1.4 Ergosphere

A region unique to Kerr black holes. Outside the event horizon, yet spacetime itself rotates.  
Remaining stationary here is impossible — everything is forced to co-rotate with the black hole.

Ergosphere radius at the equator:

```
r_ergo = 2M  (at a* = 1, equatorial plane)
r_ergo = M * (1 + sqrt(1 - a*^2 * cos^2(theta)))  (general)
```

Code approximation:

```
r_ergo_approx = Rs_base * 2.0
if r < r_ergo and BH_SPIN > 0.1:
    ergoBoost = BH_SPIN * logMass * 80.0 / (r^2 + 1.0)
    additional tangential acceleration applied
```

Visualized as a purple wireframe when spin > 0.15.

---

### 1.5 Energy-Momentum Conservation

The relativistic relation is maintained at every step:

```
E^2 = p^2 * c^2 + m^2 * c^4
```

Code:

```
pM = sqrt(px^2 + py^2 + pz^2)
E  = sqrt(pM^2 + mass^2)
```

Updated every frame after applying gravitational and magnetic forces.  
This is what allows the particle physics engine (LHC) and gravity to coexist.

---

### 1.6 Relativistic Jets (Visual)

Polar-direction jet visualization when spin > 0.6.  
Inspired by the Blandford-Znajek mechanism:

```
P_jet ~ B^2 * r_+^2 * a*^2 * c / (4 * pi)
```

Currently visual only — no physical calculation.  
However, actual particle escape driven by magnetic field + spin combinations  
near the ergosphere has been observed (see Section 2.3 below).

---

## 2. Phenomena That Emerged Without Design

### 2.1 Equivalence Principle

All particles — regardless of charge, mass, or type — are absorbed without exception.  
Simply adding Newtonian gravity produced the Equivalence Principle as an outcome.

### 2.2 Accretion Disk Formation

Particles spawned with random momenta spontaneously aggregate into a disk structure.  
A consequence of angular momentum conservation. Not designed — yet it appeared.

### 2.3 Penrose Process

Under strong magnetic field + spin conditions, particles near the ergosphere  
were observed to escape. Mathematically predicted by Roger Penrose in 1969;  
observationally confirmed in 2021.

```
E_escape = E_particle + Ω_H * L
```

This simulator did not intentionally implement this.  
It emerged spontaneously from the interaction of  
Newtonian gravity + frame-dragging approximation + Boris magnetic field integration.

---

## 3. What Was Left Out — and Why

### 3.1 Full Kerr Metric

The exact description of spacetime:

```
ds^2 = -(1 - r_s*r/Sigma)*c^2*dt^2
       - (2*r_s*r*a*sin^2(theta)/Sigma)*c*dt*dphi
       + (Sigma/Delta)*dr^2
       + Sigma*d(theta)^2
       + (r^2 + a^2 + r_s*r*a^2*sin^2(theta)/Sigma)*sin^2(theta)*dphi^2

Sigma = r^2 + a^2*cos^2(theta)
Delta = r^2 - r_s*r + a^2
```

Particle trajectories must follow the geodesic equation:

```
d^2 x^mu / d lambda^2 + Gamma^mu_alpha_beta * (dx^alpha/dlambda) * (dx^beta/dlambda) = 0
```

Computing Christoffel symbols Γ every frame is not feasible in real-time in a browser.  
**Not implemented: technical constraints.**

### 3.2 Hawking Radiation

The emission of energy from a black hole via quantum effects:

```
T_H = hbar * c^3 / (8 * pi * G * M * k_B)
```

Implementation would require quantum field theory on curved spacetime (Bogoliubov transformations) —  
a fundamentally different layer from the current engine architecture.  
**Not implemented: technical and theoretical constraints.**

### 3.3 Tidal Forces / Spaghettification

```
dF_tidal ~ 2 * G * M * m * dr / r^3
```

The gravitational gradient arising from distance differences — the effect that stretches objects.  
Not applicable in the current architecture, which treats each particle as a single point mass.  
**Not implemented: technical constraints.**

### 3.4 Gravitational Waves

Upon merger of two massive bodies:

```
h ~ G * M * v^2 / (c^4 * r)
```

Oscillations in spacetime itself. Structurally impossible here,  
as the background spacetime is fixed as flat (Minkowski).  
**Not implemented: technical constraints.**

---

## 4. What Was Left Out — As a Physical Choice

The omissions above are partly due to technical limitations —  
but they are equally **intentional choices**.

Implementing full GR would actually cost something:

> How do small masses move around a large gravitational body —  
> seeing that simplest question through the simplest possible means.

When Kepler observed planetary orbits,  
he did not know why they were ellipses — but he saw that they were ellipses first.

This simulator is the same.  
Rather than why the equations produce those orbits —  
the goal is to see **whether those orbits actually appear**.

Even with Newtonian gravity being wrong, the Penrose process emerged.  
That is the honesty and value of this approach.

---

## 5. Current Engine Architecture Summary

```
[LHC Particle Physics Engine]     [Black Hole Gravity Engine]
- 4-momentum conservation          - Newtonian gravity (log scale)
- PDG 2022 branching ratios        - Lense-Thirring approximation
- Breit-Wigner resonance           - Ergosphere boost
- Bethe-Bloch energy loss          - Event horizon absorption
- 39 particle species              - E^2 = p^2 + m^2 update
        \                                /
         \                              /
          [Boris Integrator + Magnetic Field]
                        |
                [Per-frame iteration]
                        |
        [Observables: orbits, absorption, escape, jets]
```

Theoretically, these two engines cannot coexist.  
Quantum field theory and general relativity have not yet been unified.

And yet it runs. And yet real phenomena emerge.

---

*Yang-Mills Collider v3.2 — B. Sun*