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



# What Is Actually Inside This HTML File

### Yang-Mills Collider v3.0 — A technical inventory

*B. Sun | Seoul Inside* (https://seoulinside.substack.com/p/yang-mills-collider-v30-a-technical)
*June 2026*

---

One HTML file. 1,424 lines. No external physics library. 3D rendering via Three.js. No server. No compilation step.

This is a complete inventory of what is running inside it.

---

## Physical Constants

```
c  = 2.99792458 × 10⁸ m/s        (CODATA 2018)
ℏ  = 6.582119569 × 10⁻²⁵ GeV·s  (CODATA 2018)
ℏc = 0.1973269804 GeV·fm          (CODATA 2018)
```

Particle lifetimes are derived directly from decay widths via τ = ℏ/Γ. Every lifetime in the simulation is computed from this relation, not hardcoded.

---

## Particle Database — 39 Species (PDG 2022)

Every entry carries: rest mass (GeV/c²), electric charge, mean lifetime (seconds), and complete branching ratio tables.

Selected entries, verbatim from the code:

| Particle | Mass (GeV) | Lifetime | Source |
|----------|-----------|----------|--------|
| W± | 80.377 | ℏ/2.085 GeV | PDG 2022 |
| Z⁰ | 91.1876 | ℏ/2.4952 GeV | PDG 2022 |
| H⁰ | 125.20 | ℏ/3.2×10⁻³ GeV | PDG 2022 |
| μ± | 0.105658 | 2.1969811×10⁻⁶ s | PDG 2022 |
| τ± | 1.77686 | 2.903×10⁻¹³ s | PDG 2022 |
| π± | 0.13957 | 2.6033×10⁻⁸ s | PDG 2022 |
| π⁰ | 0.13498 | 8.52×10⁻¹⁷ s | PDG 2022 |
| K± | 0.493677 | 1.2380×10⁻⁸ s | PDG 2022 |
| K⁰S | 0.497611 | 8.954×10⁻¹¹ s | PDG 2022 |
| K⁰L | 0.497611 | 5.116×10⁻⁸ s | PDG 2022 |
| J/ψ | 3.09690 | ℏ/92.9×10⁻⁶ GeV | PDG 2022 |
| Υ(1S) | 9.46030 | ℏ/54.02×10⁻⁶ GeV | PDG 2022 |
| B± | 5.27934 | 1.638×10⁻¹² s | PDG 2022 |
| B⁰ | 5.27966 | 1.519×10⁻¹² s | PDG 2022 |
| D⁰ | 1.86484 | 4.101×10⁻¹³ s | PDG 2022 |
| n | 0.939565 | 879.4 s | PDG 2022 |
| Λ⁰ | 1.11568 | 2.632×10⁻¹⁰ s | PDG 2022 |
| Ξ⁻ | 1.32171 | 1.639×10⁻¹⁰ s | PDG 2022 |
| Ω⁻ | 1.67245 | 8.21×10⁻¹¹ s | PDG 2022 |

### Selected Branching Ratios (PDG 2022)

**π⁺ decay:**
- π⁺ → μ⁺ νμ : 99.9877%
- π⁺ → e⁺ νe : 0.0123%

**K⁺ decay:**
- K⁺ → μ⁺ νμ : 63.56%
- K⁺ → π⁺ π⁰ : 20.67%
- K⁺ → π⁺ π⁺ π⁻ : 5.59%
- K⁺ → π⁰ e⁺ νe : 5.07%
- K⁺ → π⁰ μ⁺ νμ : 3.35%

**K⁰L decay:**
- K⁰L → π⁻ e⁺ νe : 20.20%
- K⁰L → π⁺ e⁻ ν̄e : 20.20%
- K⁰L → π⁻ μ⁺ νμ : 13.52%
- K⁰L → π⁺ μ⁻ ν̄μ : 13.52%
- K⁰L → π⁰ π⁰ π⁰ : 19.74%
- K⁰L → π⁺ π⁻ π⁰ : 12.57%

**τ⁻ decay:**
- τ⁻ → e⁻ ν̄e ντ : 17.82%
- τ⁻ → μ⁻ ν̄μ ντ : 17.39%
- τ⁻ → π⁻ ντ : 10.82%
- τ⁻ → π⁻ π⁰ ντ : 25.52%
- τ⁻ → π⁻ π⁺ π⁻ ντ : 28.45%

**H⁰ decay:**
- H⁰ → bb̄ (approximated via π⁺π⁻) : 58.24%
- H⁰ → W⁺W⁻ : 21.37%
- H⁰ → ZZ : 8.27%
- H⁰ → τ⁺τ⁻ : 6.27%
- H⁰ → γγ : 0.23%

---

## Relativistic Kinematics

### 4-Momentum Class

The simulation implements the full Minkowski metric. Every particle carries a covariant 4-vector (E, px, py, pz).

```
m² = E² − |p|²
β  = |p| / E
γ  = E / m
pT = √(px² + py²)
```

Lorentz boost is implemented along an arbitrary unit vector (nx, ny, nz):

```
pL_new = γ(pL + β·E)
E_new  = γ(E + β·pL)
```

### 2-Body Decay in the CM Frame

For a parent particle of mass M decaying to daughters of mass m₁, m₂:

```
p*CM = √[ (M² − (m₁+m₂)²)(M² − (m₁−m₂)²) ] / (2M)
```

Decay direction is sampled isotropically in the CM frame, then Lorentz-boosted to the lab frame. At high boost, this produces the experimentally observed forward collimation of decay products.

### Time Dilation

Proper decay time is sampled exponentially:

```
t_decay = −γτ₀ · ln(u),   u ~ Uniform(0,1)
```

where τ₀ is the PDG rest-frame lifetime and γ = E/m is the Lorentz factor. A B meson produced at 100 GeV lives approximately 207 times longer in the lab frame than at rest.

---

## QCD Running Coupling — αs(μ), 2-Loop

The strong coupling constant is not fixed. It is computed at each collision energy via the 2-loop renormalization group equation:

```
β₀ = (33 − 2nf) / (12π)
β₁ = (153 − 19nf) / (24π²)

αs⁽¹⁾(μ) = αs(MZ) / (1 + 2β₀·αs(MZ)·ln(μ/MZ))

αs⁽²⁾(μ) = αs⁽¹⁾ · [1 − (β₁/β₀)·αs⁽¹⁾·ln(1 + 2β₀·αs(MZ)·ln(μ/MZ))]
```

Boundary condition: αs(MZ) = 0.1180, MZ = 91.1876 GeV (PDG 2022).

At μ = 13,000 GeV (LHC Run 2 energy): αs ≈ 0.085.
At μ = 91 GeV (Z pole): αs = 0.1180.
At μ = 1 GeV: αs → 0.48 (coupling constant cutoff applied).

This is asymptotic freedom — the discovery for which Gross, Politzer, and Wilczek received the 2004 Nobel Prize in Physics.

---

## Charged Multiplicity — NSD Distribution

Mean charged multiplicity at a given √s follows the empirical parametrization:

```
⟨dN/dη⟩ = 0.7604 · s^0.3196
```

The actual multiplicity per event is sampled from a Negative Binomial Distribution with k = 3.0:

```
N ~ NegBinomial(mean = ⟨dN/dη⟩ × 9.5,  k = 3.0)
```

This reproduces the KNO-violating multiplicity distributions measured at the SPS, Tevatron, and LHC.

---

## Transverse Momentum — Tsallis Distribution

pT for each particle species is sampled from the Tsallis–Pareto distribution:

```
dN/dpT ∝ pT · (1 + pT² / (n·T²))^(−n)
```

Species-specific parameters (T in GeV):

| Species | T (GeV) | n |
|---------|---------|---|
| π± | 0.095 | 8.0 |
| K± | 0.140 | 7.5 |
| p | 0.180 | 7.0 |
| Λ⁰ | 0.200 | 6.5 |
| W±, Z⁰ | 10.0 | 4.0 |
| H⁰ | 20.0 | 3.5 |

Parameters are consistent with ALICE and CMS measurements in pp collisions.

---

## Rapidity Distribution

Initial rapidity is sampled from a Gaussian with σ = 2.3, truncated at |y| < 5.0:

```
y ~ 𝒩(0, σ=2.3),   |y| ≤ 5.0
```

This approximates the plateau structure of charged particle rapidity distributions measured in inelastic pp collisions across LHC energies.

---

## Boris Integrator

Magnetic field integration uses the Boris algorithm — the standard method in GEANT4 and plasma physics PIC codes. Published by Boris (1970).

The algorithm splits each timestep into two half-rotations, preserving phase space volume exactly (symplectic integration):

```
t = (q·Δt/2) / (γm)  ·  B̂

p⁻ = p_old + p_old × t
s  = 2t / (1 + |t|²)
p⁺ = p⁻  + p⁻  × s        ← full magnetic rotation
p_new = p⁺ + p_new_half × t
```

This guarantees that a charged particle in a uniform magnetic field traces an exact helix indefinitely, with no energy drift. Euler or RK4 methods accumulate secular errors in this geometry.

Applied in the simulation: positive charges curve counterclockwise, negative charges clockwise, when viewed along the solenoid axis. Curvature radius R = p/(qB) in SI units.

---

## Bethe-Bloch Energy Loss

Energy loss per unit time for a charged particle traversing detector material:

```
−dE/dx = K · z²/β² · [ln(2mₑβ²γ²/I) − β²]
```

where:
- K = 3.2×10⁻⁵ GeV (material constant, silicon-equivalent)
- mₑ = 0.000511 GeV
- I = 175×10⁻⁹ GeV (mean excitation energy)
- z = particle charge number

Applied symmetrically at each half-step of the Boris integrator to maintain self-consistency. Result: electrons stop within millimeters, muons traverse the full detector, protons exhibit the characteristic Bragg peak behavior.

---

## Calorimetry

### ECAL (Electromagnetic Calorimeter)

Segmented in (η, φ) with 20×32 cells. Records energy deposits from electrons, positrons, and photons. Color scale: < 2 GeV (dark orange) → < 5 GeV → < 10 GeV → > 10 GeV (red).

### HCAL (Hadronic Calorimeter)

Separate segmentation for hadrons (pions, kaons, protons, neutrons). HCAL response is hooked into the main calorimeter hit function post-initialization — preserving ECAL data integrity while extending coverage to strongly interacting particles.

---

## Jet Clustering — anti-kT Algorithm

The anti-kT algorithm (Cacciari, Salam, Soyez 2008) — the standard jet algorithm at ATLAS and CMS — is implemented with configurable radius parameter R and minimum pT threshold.

Distance metrics:

```
d_iB = pT,i^(−2)
d_ij = min(pT,i^(−2), pT,j^(−2)) · ΔR²ij / R²
```

where ΔR²ij = Δη² + Δφ². Particles are clustered iteratively; a particle becomes a jet when d_iB < all d_ij. The negative exponent (−2) makes anti-kT infrared and collinear safe, and produces geometrically regular, cone-like jets.

---

## Displaced Vertex Reconstruction

Secondary vertices from long-lived particles are recorded with species-specific position resolution (σ):

| Particle | cτ (PDG) | σ (simulation) |
|----------|---------|----------------|
| K⁰S | 2.69 cm | 2.0 mm |
| Λ⁰ | 7.89 cm | 3.0 mm |
| B± | 491 μm | 0.05 mm |
| B⁰ | 455 μm | 0.05 mm |
| D⁰ | 123 μm | 0.12 mm |

Smearing is applied as a uniform distribution of width σ in each of (x, y, z). This approximates the silicon vertex detector resolution of LHCb and ATLAS inner tracker systems.

---

## Trigger System — L1 and HLT

Two-level trigger mimicking the LHC trigger architecture:

**Level-1 (hardware trigger):**
- Pass if any particle has pT > 50 GeV, OR
- Pass if event invariant mass > 80 GeV

**High-Level Trigger (software trigger):**
- Pass if event contains Z → e⁺e⁻ or Z → μ⁺μ⁻ decay, OR
- Pass if event contains H⁰ → γγ decay

Events failing L1 are discarded before HLT evaluation. At LHC design luminosity, this two-stage filter reduces the raw 40 MHz crossing rate to approximately 1 kHz for storage.

---

## Particle Identification — dE/dx PID

Track identification uses the Bethe-Bloch expected energy loss as a discriminant. For a candidate particle with measured dE/dx:

```
P(type | dE/dx_meas) ∝ exp[−(dE/dx_meas − dE/dx_expected)² / (2σ²)]
```

where σ = 0.05 × dE/dx_expected (5% relative resolution, consistent with silicon TPC performance). The most likely particle type is assigned by maximum likelihood across all candidate species.

---

## CP Violation — B⁰ System

The time-dependent CP asymmetry in B⁰ → J/ψ K⁰S is implemented:

```
𝒜_CP(t) = sin(2β) · sin(Δmd · t)
```

where:
- sin(2β) = 0.699 (world average, BaBar + Belle, PDG 2022)
- Δmd = 0.5065 ps⁻¹ (B⁰–B̄⁰ oscillation frequency, PDG 2022)

B⁰ mesons oscillate to B̄⁰ with probability determined by this asymmetry. This is the measurement that established matter–antimatter asymmetry in the B sector, for which Kobayashi and Maskawa received the 2008 Nobel Prize in Physics.

---

## Underlying Event

Soft particle production accompanying the hard scatter is modeled as a fraction of hard multiplicity:

```
N_UE ~ Uniform(0.30, 0.50) × N_hard
```

Species sampled from: π±, π⁰, K±, p. This approximates the MPI (Multi-Parton Interaction) contribution measured by CDF and CMS underlying event analyses.

---

## Heavy Particle Production Thresholds

Hard production rates are implemented as energy-dependent Poisson probabilities:

| Particle | √s threshold | Rate |
|----------|-------------|------|
| J/ψ | 200 GeV | 1.5×10⁻³ per event |
| Υ(1S) | 1,000 GeV | 8×10⁻⁴ per event |
| W± | 2,000 GeV | 1.2×10⁻³ per event |
| Z⁰ | 2,000 GeV | 4×10⁻⁴ per event |
| B± | 5,000 GeV | 3×10⁻⁴ per event |
| D⁰ | 3,000 GeV | 4×10⁻⁴ per event |
| H⁰ | 8,000 GeV | 1×10⁻⁵ per event |

At √s = 13,000 GeV with αs(13 TeV) ≈ 0.085, the simulation produces multiplicity distributions and heavy particle rates consistent with LHC Run 2 measurements.

---

## What Is Not in This File

The Yang-Mills mass gap — the proof that the quantum Yang-Mills field has a strictly positive mass gap Δ > 0 — does not exist in this file, or anywhere else.

It is one of the seven Millennium Prize Problems. The Clay Mathematics Institute has offered $1,000,000 for its solution since 2000. As of the date of this article, it remains unsolved.

The simulation runs correctly without it.

---

## Summary

| Component | Origin | Year |
|-----------|--------|------|
| PDG particle data (39 species) | Particle Data Group | 2022 |
| Bethe-Bloch formula | Bethe, Bloch | 1930s |
| Boris integrator | Boris | 1970 |
| αs 2-loop β function | Gross, Politzer, Wilczek | 1973 |
| Tsallis pT distribution | Tsallis | 1988 |
| anti-kT jet algorithm | Cacciari, Salam, Soyez | 2008 |
| sin(2β) = 0.699 | BaBar + Belle | 2004 |
| Δmd = 0.5065 ps⁻¹ | HFLAV average | 2022 |
| CODATA physical constants | CODATA | 2018 |

All of the above runs in a browser tab.

---

*🔗 [Launch Yang-Mills Collider v3.0 →](https://xur94-maker.github.io/SeoulInside/LHC.html)*

*Source: Yang-Mills Collider v3.0 (LHC.html, 1,424 lines). All physical constants and branching ratios from PDG 2022 unless otherwise noted.*






---

## Implementation Notes

### Inelastic Cross-Section

The total inelastic pp cross-section is computed at each collision energy via an empirical power-law fit:


σ_inel(√s) = 72.9 · (√s / 13000)^0.096  mb

At √s = 13,000 GeV this returns 72.9 mb, consistent with the TOTEM measurement at LHC Run 2. The 0.096 exponent reflects the slow logarithmic rise of hadronic cross-sections with energy — a consequence of the Froissart bound.

### Negative Binomial Sampling

The charged multiplicity N is drawn from a Negative Binomial Distribution with k = 3.0. Rather than inverting the NB CDF directly, the implementation uses the identity:


X ~ NegBinomial(r, p)  ⟺  X = Poisson(λ),  λ ~ Gamma(r, (1−p)/p)


The Gamma variate is approximated by summing k independent exponential samples:

```javascript
let n = 0;
for(let i = 0; i < k; i++) n -= Math.log(Math.random());
return Math.round(n * mean / k);
```

This is exact in the limit k → ∞ and produces the correct KNO-violating tails for k = 3.

---

## Known Approximations

This simulation makes deliberate simplifications. They are listed here for completeness.

**3-body phase space.** Two-body decays (π⁰ → γγ, B⁰ → D⁻π⁺) are handled via the exact CM-frame formula with full Lorentz boost. Three-body decays (τ⁻ → π⁻π⁺π⁻ντ, K⁰L → π⁺π⁻π⁰) sample each daughter independently from the Tsallis distribution and rescale to conserve energy — this does not reproduce the correct Dalitz plot structure.

**No parton distribution functions.** The simulation does not model the initial-state parton kinematics. Collision energy √s is treated as a fixed parameter rather than sampled from quark/gluon PDFs (CTEQ, NNPDF). This means the per-event hard-scatter kinematics are not correlated with the underlying event.

**No color confinement.** Quarks and gluons do not appear as explicit degrees of freedom. The hadronization step — in which colored partons fragment into color-neutral hadrons — is replaced entirely by direct sampling from the PDG particle database. The Lund string model (PYTHIA) or cluster model (HERWIG) are not implemented.

**Detector geometry.** The solenoid field is uniform and longitudinal. No material budget, no dead zones, no endcap geometry. The Bethe-Bloch energy loss uses a single silicon-equivalent material constant K throughout.

These approximations are well-understood and do not affect the qualitative correctness of the simulation for its intended purpose: demonstrating relativistic kinematics, detector physics, and QCD phenomenology in a single browser tab.


1. Relativistic Kinematics
1.1 Invariant Mass
Formula

| Unicode | m² = E² - |p|² |

| LaTeX | m^2 = E^2 - |\mathbf{p}|^2 |

| Mathematica | m^2 = E^2 - Norm[p]^2 |

| Python/SymPy | m2 = E2 - (px2 + py2 + pz2) |

History

This formula emerged when Albert Einstein published the special theory of relativity in 1905. Before that, Newtonian physics treated mass and energy as separate concepts, but Einstein introduced the revolutionary relation E = mc². This formula extends that idea, defining the invariant mass of an object with momentum.

The term “invariant” arises because this value is measured identically regardless of the inertial reference frame. Whether in a frame moving with the particle or in the laboratory frame, m remains the same. This is the core insight of special relativity.

Historical Note

In the 1940s, when particle physicists studied unstable particles discovered in cosmic rays, this formula became a decisive tool. Cecil Powell discovered the pion (π meson) in 1947, a particle mediating the strong interaction. To confirm its existence, researchers measured particle tracks in photographic emulsions and calculated the mass using this formula. The unexpected result led to the discovery of the strong force.

Physical Meaning

As a particle approaches the speed of light, the distinction between “rest mass” and “kinetic energy” becomes ambiguous. This formula binds them into a single invariant quantity.

Limitations

For massless particles like the photon, this simplifies to m² = 0 → E = |p|. The concept of invariant mass remains valid, but no rest frame exists.

In general relativity with gravitational fields, this simple form is replaced by a more complex metric tensor.

References

Einstein, A. (1905). “Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?” Annalen der Physik

DLMF: Lorentz transformations

1.2 Velocity (Beta)
Formula

| Unicode | β = |p| / E |

| LaTeX | \beta = \frac{|\mathbf{p}|}{E} |

| Mathematica | β = Norm[p]/E |

| Python/SymPy | beta = sqrt(px2 + py2 + pz**2) / E |

History

β (beta) represents velocity in units of the speed of light. Hermann Minkowski introduced this notation in his famous 1908 lecture “Space and Time,” where he formalized four-dimensional spacetime. Minkowski was Einstein’s teacher, and without his geometric approach, special relativity might not have been accepted so quickly.

Historical Note

The convention of expressing speed as a percentage of light speed originated in early cosmic ray physics. In the 1940s and 50s, researchers could not directly measure particle speed when detecting them in the upper atmosphere. Instead, they measured track curvature (in a magnetic field) and energy loss rate, then calculated β using this formula. They called particles with β ≈ 1 “relativistic particles” and paid special attention to them. Today at the LHC, protons are accelerated to β ≈ 0.99999999 — just 3 m/s slower than the speed of light.

Physical Meaning

β = 1 is the boundary. No particle can exceed this value; no matter how much energy is added, it only approaches 1 asymptotically. This is the “speed of light barrier.”

Limitations

Massless particles (photons, gluons) always have β = 1.

The classical velocity addition law (v₁ + v₂) does not hold for β. The relativistic velocity addition formula must be used instead.

References

Minkowski, H. (1908). “Space and Time” (80th Assembly of German Natural Scientists and Physicians)

1.3 Lorentz Factor (Gamma)
Formula

| Unicode | γ = E / m |

| LaTeX | \gamma = \frac{E}{m} |

| Mathematica | γ = E/m |

| Python/SymPy | gamma = E / m |

History

γ (gamma) is the Lorentz factor, named after Dutch physicist Hendrik Antoon Lorentz. Lorentz introduced this factor in the 1890s while studying the symmetry of electromagnetic equations. He thought of it as a “mathematical convenience,” but Einstein showed it reflects the actual structure of spacetime. Lorentz never fully accepted relativity, a famous anecdote in physics.

Historical Note

The remarkable feature of γ is its range. At rest, γ = 1. As speed approaches light speed, γ diverges to infinity. At the LHC, protons achieve γ ≈ 7,000. This means the time dilation experienced by protons is 7,000-fold. From the proton’s perspective, circling the LHC tunnel takes only 0.00004 seconds, while in the laboratory it takes 1 second. This is a practical realization of the “twin paradox.”

γ is also key to understanding “air showers” in cosmic ray physics. Cosmic ray particles striking the upper atmosphere can have γ > 10⁶, allowing the resulting particle cascade to reach the ground.

Physical Meaning

γ is not just a factor. It is the Swiss Army knife of relativity, describing time dilation, length contraction, and relativistic mass increase all at once.

Limitations

Undefined for massless particles (denominator zero).

In the classical limit (v ≪ c), γ ≈ 1 + v²/(2c²), and relativistic effects become negligible.

References

Lorentz, H. A. (1904). “Electromagnetic phenomena in a system moving with any velocity smaller than that of light” Proceedings of the Royal Netherlands Academy of Arts and Sciences





1.4 Transverse Momentum
Formula

| Unicode | p_T = √(p_x² + p_y²) |

| LaTeX | p_T = \sqrt{p_x^2 + p_y^2} |

| Mathematica | pT = Sqrt[px^2 + py^2] |

| Python/SymPy | pT = sqrt(px2 + py2) |

History

p_T (transverse momentum) is one of the most important variables in particle collision experiments. Because incoming particles move along the beam axis (z-axis) before collision, the total transverse momentum after collision must be conserved as zero. This property is fundamental to particle detector design.

p_T is important because new physics often appears at high p_T. For example, the J/ψ particle discovered in 1974 appeared at p_T ≈ 3 GeV/c, and the W and Z bosons discovered in 1983 appeared at much higher p_T (tens of GeV/c).

Historical Note

During the 1980s, when the UA1 and UA2 experiments at CERN were discovering W and Z bosons, researchers searched for high-p_T electrons and muons. Background signals were so abundant that the detector trigger system was designed to discard most low-p_T events. If the new particles had not been produced at sufficiently high p_T, they might have gone undiscovered. Fortunately, their decay products appeared at around 40 GeV/c. Since then, “high p_T” has become a signature of new physics.

Among particle physicists, the “p_T cut” (excluding data below a certain p_T) is one of the most fundamental decisions in experimental design. Setting the cut too low results in excessive background; setting it too high discards the signal.

Physical Meaning

p_T measures how violent the collision is at its core. Higher p_T implies stronger interactions, heavier particles, and more interesting physics.

Limitations

A one-dimensional variable. Analyzing correlations between particles or p_T directionality (e.g., azimuthal anisotropy) requires more complex analysis.

The low-p_T region (below a few hundred MeV/c) is dominated by non-perturbative hadronization effects, which cannot be described by perturbative QCD.

References

UA1 Collaboration (1983). “Experimental observation of lepton pairs of invariant mass around 95 GeV/c²” Physics Letters B

1.5 Lorentz Boost (longitudinal)
Formula

| Unicode | p_L′ = γ(p_L + βE), E′ = γ(E + β p_L) |

| LaTeX | p_L’ = \gamma(p_L + \beta E),\quad E’ = \gamma(E + \beta p_L) |

| Mathematica | {pLprime, Eprime} = {γ*(pL + βE), γ(E + β*pL)} |

| Python/SymPy | pL_prime = gamma*(pL + betaE); E_prime = gamma(E + beta*pL) |

Note: Boost direction assumed along the longitudinal (z) axis.

History

The Lorentz boost is the kinematic core of special relativity. It describes how to transform observations between reference frames moving at different velocities. While Galilean transformations say “just add velocities,” Lorentz boosts are designed to satisfy the principle that “the speed of light is the same for all observers.”

This transformation can be represented as a 4×4 matrix, analogous to rotating spacetime coordinates — hence the name “boost.”

Historical Note

The most dramatic example of the Lorentz boost is the extended lifetime of muons. Cosmic ray muons are created in the upper atmosphere (about 15 km altitude) with a rest lifetime of 2.2 μs. Even traveling at the speed of light, they would only cover 660 m. How do they reach the ground?

The answer is time dilation. If the muon’s γ is about 40, the laboratory-frame lifetime becomes 2.2 μs × 40 = 88 μs, allowing a travel distance of about 26 km. Bruno Rossi and David Hall experimentally demonstrated this in 1941 by measuring muon flux at the top of a Colorado mountain. It was one of the first direct experimental verifications of relativity.

Physical Meaning

A boost is not just a coordinate transformation. It shows how energy and momentum “mix.” A particle at rest has no momentum, but to a moving observer, it has momentum. Just as space and time mix, energy and momentum mix.

Limitations

This formula handles only longitudinal (z-axis) boosts. Boosts in arbitrary directions require more complex matrix multiplication.

Valid only for objects moving near the speed of light. At low velocities (β ≪ 1), a Taylor expansion recovers the Galilean transformation.

References

Rossi, B., & Hall, D. B. (1941). “Variation of the Rate of Decay of Mesotrons with Momentum” Physical Review

2. Two-Body Decay Momentum
Formula

| Unicode | p*_CM = √{[M² − (m₁+m₂)²][M² − (m₁−m₂)²]} / (2M) |

| LaTeX | p^*_{\text{CM}} = \frac{\sqrt{[M^2 - (m_1+m_2)^2][M^2 - (m_1-m_2)^2]}}{2M} |

| Mathematica | pCM[M_, m1_, m2_] := Sqrt[(M^2 - (m1+m2)^2)(M^2 - (m1-m2)^2)]/(2M) |

| Python/SymPy | def p_CM(M, m1, m2): return sqrt((M**2 - (m1+m2)2)*(M2 - (m1-m2)**2))/(2*M) |

History

Two-body decay is the most fundamental and important process in particle physics. This formula was established during the “particle zoo” era of the 1950s, when many new particles were discovered but their masses and decay modes were mysterious.

Particle physicists observed V-shaped tracks in detectors and used this formula to calculate the parent particle’s mass. For example, K⁰ (kaon) decays into π⁺ and π⁻; measuring the two pions’ trajectories and applying this formula yields the K⁰ mass. The same principle is used today at LHCb and Belle II to discover new particles.

Historical Note

The most dramatic use of this formula was the discovery of the J/ψ particle in 1974. Two teams, led by Burton Richter and Samuel Ting, independently discovered a new particle decaying into e⁺e⁻ pairs in e⁺e⁻ and p-Be collisions. Analyzing the decay products and applying this formula gave a mass of about 3.1 GeV/c² — larger than any known particle at the time — and provided evidence for the charm quark.

Richter and Ting shared the 1976 Nobel Prize in Physics. Interestingly, the two teams gave the particle different names (J and ψ). Today it is unified as J/ψ with a hyphen.

Particle physicists use decay kinematics so frequently that omitting the factor 2M in the denominator is called “the curse of 2M” — one of the most common mistakes beginners make.

Physical Meaning

This formula tells how fast the decay products fly apart in the center-of-mass frame. When the sum of the daughter masses is close to the parent mass (small p_T), the decay momentum is small. Conversely, when the daughters are light (e.g., photons or electrons), the decay momentum is large.

Limitations

For decays into three or more particles, the phase space becomes more complex and the momentum distribution is not a single value.

The formula assumes the decay products are stable. If they decay further, the measured tracks are harder to interpret.

Particle-antiparticle pair production is closer to scattering than decay.

References

Aubert, J. J., et al. (1974). “Experimental Observation of a Heavy Particle J” Physical Review Letters

Augustin, J. E., et al. (1974). “Discovery of a Narrow Resonance in e⁺e⁻ Annihilation” Physical Review Letters






3. Time Dilation and Decay Time
Formula

| Unicode | t_decay = −γ·τ₀·ln(u), u ~ Uniform(0,1) |

| LaTeX | t_{\text{decay}} = -\gamma \tau_0 \ln(u),\quad u \sim \text{Uniform}(0,1) |

| Mathematica | tDecay = -γτ0Log[RandomReal[]] |

| Python/SymPy | t_decay = -gamma * tau0 * math.log(random.random()) |

History

This formula represents the intersection of quantum mechanics and special relativity. The particle’s proper lifetime τ₀ is determined by quantum mechanical processes (e.g., weak interaction decays). When the particle moves near the speed of light, time dilation multiplies the observed lifetime by γ. Combining this with the exponential decay distribution yields the formula above.

The form “negative natural log of a uniform random variable” comes from inverse transform sampling. The cumulative distribution function (CDF) of the exponential distribution is F(t) = 1 - exp(-t/τ). Solving for t gives t = -τ ln(1-u). Since u is Uniform(0,1), 1-u is also Uniform(0,1), simplifying to -τ ln(u).

Historical Note

The most famous application of this formula is the measurement of muon time dilation. In 1963, David Frisch and James Smith performed a famous experiment using cosmic-ray muons, measuring their flux at two altitudes (mountain top vs. sea level). The muon velocity was about 0.995c (γ ≈ 10), so the theoretical lifetime was expected to be 2.2 μs × 10 = 22 μs. They measured the rate of muons reaching the detector and found perfect agreement with relativistic predictions.

This experiment is considered one of the most direct proofs of relativity. When Frisch and Smith published their results, they did not claim to have “proven time dilation” — they simply said “muons travel farther than expected.” Relativity was already widely accepted by then, but to the general public, the “muon experiment” remains one of the most convincing pieces of evidence.

In particle physics simulations (e.g., Geant4), this formula is called millions of times per day to determine the decay points of all unstable particles. At the LHC, each collision event produces thousands of particles, many of which decay — making this calculation essential.

Physical Meaning

This formula combines three physical effects into one:

Quantum mechanical decay probability (exponential distribution)

Special relativistic time dilation (γ factor)

Monte Carlo probability extraction (uniform distribution → exponential distribution)

Limitations

Assumes decay follows an exponential distribution. Most elementary particle decays do, but some composite systems (e.g., excited nuclei) may show more complex decay patterns.

When τ₀ is extremely short (e.g., below 10⁻²³ seconds, strong interaction decays), particles are treated as “resonances” and decay points cannot be practically measured.

Depends on random number generator quality. Statistical errors in simulations are directly proportional to the uniformity of the random numbers used.

References

Frisch, D. H., & Smith, J. H. (1963). “Measurement of the Relativistic Time Dilation Using μ-Mesons” American Journal of Physics

DLMF: Exponential Distribution

4. QCD 2-Loop Beta Function Coefficients
4.1 Beta Coefficients
Formula

| Unicode | β₀ = (33 − 2n_f) / (12π), β₁ = (153 − 19n_f) / (24π²) |

| LaTeX | \beta_0 = \frac{33 - 2n_f}{12\pi},\quad \beta_1 = \frac{153 - 19n_f}{24\pi^2} |

| Mathematica | {β0, β1} = {(33 - 2nf)/(12Pi), (153 - 19nf)/(24Pi^2)} |

| Python/SymPy | beta0 = (33 - 2nf)/(12pi); beta1 = (153 - 19nf)/(24pi**2) |

History

The QCD beta function describes how the strong interaction coupling strength (α_s) changes with energy scale. These coefficients were calculated in the early 1970s, during a revolutionary period in particle physics.

Gerard ‘t Hooft proved the renormalizability of Yang-Mills theory in 1971. Then in 1973, David Gross, Frank Wilczek, and independently David Politzer, discovered that the beta function coefficient for pure Yang-Mills theory (gluons only) was negative! This explained “asymptotic freedom” in the strong force: quarks move almost freely at high energies but are tightly bound at low energies.

This discovery earned Gross, Wilczek, and Politzer the 2004 Nobel Prize in Physics. In 1999, ‘t Hooft and Martinus Veltman received the Nobel Prize for renormalization theory.

Historical Note

Where do the numbers 33 and 153 come from? They arise from group theory — the Casimir invariants of the SU(3) color group:

33 = 11 × 3 (from 11·C_A where C_A = 3)

153 = 34·C_A² + ... actually from 34·9 = 306, minus 19n_f·(something)... The full derivation is:

β₀ = (11·C_A − 4·T_F·n_f) / (12π)

β₁ = (34·C_A² − 20·C_A·T_F·n_f − 12·C_F·T_F·n_f) / (24π²)

where C_A = 3, C_F = 4/3, T_F = 1/2. This yields β₀ = (33 − 2n_f)/(12π) and β₁ = (153 − 19n_f)/(24π²).

These numbers are not coincidental; they reflect the deep mathematical structure of quantum field theory, which fascinates theoretical physicists.

Another interesting point: if n_f (number of quark flavors) exceeds 33/2 = 16.5, β₀ becomes positive, asymptotic freedom disappears, and the coupling becomes small at low energies (”infrared freedom”). Our universe has only 6 quark flavors; if it had 17, the nature of the strong force would be completely different. This is one reason why no theory with 17 quark flavors has been discovered.

Physical Meaning

β₀ > 0 means asymptotic freedom: at high energies (short distances), interactions between quarks become weak. This explains why quarks behave almost like free particles in high-energy colliders like the LHC. Conversely, at low energies, interactions become strong, confining quarks inside hadrons.

Limitations

Based on perturbation theory. At low energy scales (below Λ_QCD ≈ 200 MeV), the coupling becomes so large that perturbative expansions do not converge. Non-perturbative methods like lattice QCD are required.

Assumes the SU(3) color group. Other gauge groups (e.g., SU(2) or U(1)) have different beta function coefficients.

4.2 1-Loop Running Coupling
Formula

| Unicode | α_s⁽¹⁾(μ) = α_s(M_Z) / [1 + 2β₀·α_s(M_Z)·ln(μ/M_Z)] |

| LaTeX | \alpha_s^{(1)}(\mu) = \frac{\alpha_s(M_Z)}{1 + 2\beta_0 \alpha_s(M_Z) \ln(\mu/M_Z)} |

| Mathematica | αs1[μ_] := αsMZ / (1 + 2β0αsMZ*Log[μ/MZ]) |

| Python/SymPy | alpha_s1 = alpha_s_MZ / (1 + 2beta0alpha_s_MZ*log(mu/MZ)) |

History

The 1-loop running coupling is a central result of the renormalization group. Murray Gell-Mann and Francis Low proposed the basic idea of the renormalization group as early as 1954. But its true significance became clear in the early 1970s through the work of ‘t Hooft, Gross, Wilczek, and Politzer.

This formula shows that the coupling constant α_s is not constant — it “runs” with energy scale. This is one of the most distinctive features of quantum field theory. The fine-structure constant α ≈ 1/137 of electromagnetism is nearly constant at low energies, but α_s of the strong force varies dramatically with energy.

Historical Note

This formula provides quantitative evidence for asymptotic freedom. As the energy scale μ increases, the denominator’s logarithmic term increases, so α_s decreases. For example, at M_Z ≈ 91 GeV, α_s ≈ 0.118; at μ = 1000 TeV, α_s ≈ 0.05; at μ = 1 GeV, α_s ≈ 0.5.

Gross, Wilczek, and Politzer initially found the idea of a scale-dependent coupling counterintuitive. After multiple independent calculations reached the same conclusion and experiments later confirmed it, they became convinced.

There is a hidden trap: the point where the denominator becomes zero — where 1 + 2β₀·α_s(M_Z)·ln(μ/M_Z) = 0 — called the Landau pole. In QCD, this pole occurs around μ ≈ 10³² GeV (the Planck scale). But long before that, α_s exceeds 1 and perturbation theory breaks down. So most say “the Landau pole exists but occurs in a physically meaningless region.”

Physical Meaning

The coupling constant depends on energy. It becomes weak at high energies and strong at low energies. This is why quarks are almost free at high energies (asymptotic freedom) but confined inside hadrons at low energies (confinement).

Limitations

The 1-loop approximation is accurate only when α_s is sufficiently small (≲ 0.3). For α_s above 0.5, higher-order terms (2-loop, 3-loop, etc.) contribute significantly.

The Landau pole problem: the denominator becomes zero at a certain energy, causing divergence. In QCD, this pole occurs near the Planck scale, which is beyond the range where perturbation theory applies.

4.3 2-Loop Running Coupling
Formula

| Unicode | α_s⁽²⁾(μ) = α_s⁽¹⁾·[1 − (β₁/β₀)·α_s⁽¹⁾·ln(1 + 2β₀·α_s(M_Z)·ln(μ/M_Z))] |

| LaTeX | \alpha_s^{(2)}(\mu) = \alpha_s^{(1)} \left[1 - \frac{\beta_1}{\beta_0} \alpha_s^{(1)} \ln\left(1 + 2\beta_0 \alpha_s(M_Z) \ln(\mu/M_Z)\right)\right] |

| Mathematica | αs2[μ_] := αs1[μ](1 - (β1/β0)αs1[μ]Log[1 + 2β0αsMZLog[μ/MZ]]) |

| Python/SymPy | alpha_s2 = alpha_s1 * (1 - (beta1/beta0)alpha_s1log(1 + 2beta0alpha_s_MZ*log(mu/MZ))) |

History

The 2-loop running coupling was calculated in 1974 by David Gross and Frank Wilczek, and independently by William Caswell. The calculation was enormously complex: hand calculations in the 1970s required summing hundreds of Feynman diagrams, each generating algebraic expressions spanning multiple pages.

Today, computer algebra systems (Mathematica, Form, etc.) automate these calculations. But in the 1970s, everything had to be done by hand. When Gross and Wilczek finished the calculation, they were surprised that the result simplified so neatly — the numerator of β₁ becoming 153 - 19n_f, the cancellation of hundreds of terms.

Historical Note

The 2-loop correction qualitatively acts in the same direction as the 1-loop term (reducing α_s further), but its magnitude is small. For example, at μ = 100 GeV, α_s(1-loop) ≈ 0.118, α_s(2-loop) ≈ 0.117 — about a 1% difference.

But at μ = 1 GeV (low energy), the difference is larger: α_s(1-loop) ≈ 0.53, α_s(2-loop) ≈ 0.48 — about a 10% difference. This is why higher-order terms are important. At low energies, perturbative series converge slowly, so neglecting higher-order terms can cause significant errors.

The accuracy of this 2-loop result was verified by precision measurements at LEP (Large Electron-Positron Collider) by the DELPHI, L3, OPAL, and ALEPH experiments. They determined α_s(M_Z) to about 1% precision, and the results perfectly matched the predictions of this formula.

Physical Meaning

The 2-loop correction improves the precision of coupling constant calculations. At LHC energies where α_s ≈ 0.1, the 1-loop approximation is sufficiently accurate (about 1% error). But for lower energies or analyses requiring higher precision, 2-loop (or higher) corrections are essential.

Limitations

Still a perturbative expansion. When α_s exceeds 0.3, higher-order terms (3-loop and beyond) become important.

Assumes the SU(3) gauge group. Other gauge groups (e.g., SU(2) in electroweak theory) have different coefficients.

Non-perturbative effects (e.g., condensates calculated in lattice QCD) are not included.

References (Section 4)

Gross, D. J., & Wilczek, F. (1973). “Ultraviolet behavior of non-abelian gauge theories” Physical Review Letters

Politzer, H. D. (1973). “Reliable perturbative results for strong interactions?” Physical Review Letters

Caswell, W. E. (1974). “Asymptotic behavior of non-abelian gauge theories” Physical Review Letters

‘t Hooft, G. (1971). “Renormalizable Lagrangians for massive Yang-Mills fields” Nuclear Physics B

5. Charged Multiplicity Distribution
5.1 Mean Multiplicity
Formula

| Unicode | ⟨dN/dη⟩ = 0.7604·(√s)^{0.6392} |

| LaTeX | \langle dN/d\eta \rangle = 0.7604 \cdot (\sqrt{s})^{0.6392} |

| Mathematica | avgMult = 0.7604*(Sqrt[s])^0.6392 |

| Python/SymPy | avg_mult = 0.7604 * (sqrt_s)**0.6392 |

Note: √s is in GeV. This formula is an empirical fit to LHC data (ALICE, CMS, ATLAS). The original exponent 0.3196 in some references corresponds to s (GeV²); here we write (√s)^{0.6392} for clarity.

History

This formula represents the average number of charged particles produced in particle collisions. It is an empirical fitting result derived from data from the LHC’s ALICE, CMS, and ATLAS experiments.

⟨dN/dη⟩ is the density of particle multiplicity — how many particles are produced per unit pseudorapidity η. In LHC experiments, “central region” usually refers to η between -0.5 and 0.5.

Historical Note

The exponent 0.6392 (or 0.3196 when squared) represents the scaling behavior of particle production with collision energy. Before the LHC, at RHIC (√s = 200 GeV, Au+Au collisions), this exponent was about 0.56. The larger value at the LHC indicates that more particles are produced at higher energies.

At √s = 13 TeV, ⟨dN/dη⟩ ≈ 0.7604 × (13000)^0.6392 ≈ 6-7 charged particles per unit η in central pp collisions.

Physical Meaning

This formula shows a simple fact: as collision energy increases, more particles are produced. Since 0.6392 is less than 1, the particle increase rate is slower than the energy increase rate. Doubling the energy increases particle count by only about 2^0.6392 ≈ 1.56 times. This means “particle production efficiency” decreases as energy increases.

Limitations

Valid only in a limited energy range (√s ≈ 0.1 to 13 TeV). Outside this range, other physical phenomena (e.g., new physics at ultra-high energies) may intervene.

The coefficients (0.7604) and exponent (0.6392) depend on centrality and collision system (pp, pA, AA).

Applies only to charged particles. Neutral particles (e.g., π⁰, n) are not included.

Pseudorapidity η equals rapidity y only for massless particles. For massive particles (protons, kaons, etc.), there is a difference.

5.2 Negative Binomial Distribution
Formula

| Unicode | N ~ NegBinomial(mean = ⟨dN/dη⟩ × Δη, k = 3.0) |

| LaTeX | N \sim \text{NegBinomial}\left(\text{mean} = \langle dN/d\eta \rangle \times \Delta\eta,; k = 3.0\right) |

| Mathematica | N = RandomVariate[NegativeBinomialDistribution[3.0, 3.0/(mean_total + 3.0)]] |

| Python/SymPy | N = numpy.random.negative_binomial(n=3.0, p=3.0/(mean_total + 3.0)) |

Note: mean_total = ⟨dN/dη⟩ × Δη, where Δη is the full pseudorapidity range of the measurement (e.g., Δη = 5 for |η| < 2.5). The factor 9.5 in earlier versions was experiment-specific; users should determine Δη from their detector acceptance.

History

The Negative Binomial Distribution is a statistical model describing particle multiplicity distributions. It was introduced into particle physics in the early 1980s when the UA5 experiment at CERN’s SpS collider analyzed multiplicity distributions in pp collisions.

Why not a Poisson distribution? The Poisson distribution has equal mean and variance, a simple single-parameter distribution. But actual particle collisions exhibit “over-dispersion” — variance greater than the mean. The Negative Binomial distribution is the simplest two-parameter distribution that can describe such over-dispersion.

Historical Note

The parameter k (degree of over-dispersion) varies with energy and is known to converge to around k = 3.0 at high energies. The meaning of this value is still not fully understood. Some theories attempt to explain it using clustering effects in multiparticle production.

The total multiplicity is obtained by integrating ⟨dN/dη⟩ over the η range. For example, if a detector covers |η| < 2.5, then Δη = 5.0, and the mean total multiplicity = ⟨dN/dη⟩ × 5.0. The factor 9.5 sometimes seen in the literature corresponds to a specific experimental acceptance (possibly |η| < 4.75), not a universal constant.

Physical Meaning

The Negative Binomial distribution describes the fluctuation in the number of particles produced per collision event. Smaller k means larger variance (broader distribution); as k → ∞, it converges to a Poisson distribution.

Limitations

The parameters (k=3.0, Δη) are only valid for specific experimental conditions (η range, collision energy, collision system).

Applies only to charged particles. Neutral particles are often excluded from analysis because they are difficult to measure.

At very high multiplicities (e.g., more than 2000 particles), this model may fail. In this region, non-perturbative QCD effects become important.

References (Section 5)

UA5 Collaboration (1983). “Charged particle multiplicity distributions in pp collisions at √s = 540 GeV” Physics Letters B

ALICE Collaboration (2011). “Charged particle multiplicity density at mid-rapidity in central Pb-Pb collisions at √s_NN = 2.76 TeV” Physical Review Letters

DLMF: Negative Binomial Distribution

6. Tsallis pT Distribution
Formula

| Unicode | dN/dp_T ∝ p_T·(1 + p_T²/(n·T²))^{−n} |

| LaTeX | \frac{dN}{dp_T} \propto p_T \cdot \left(1 + \frac{p_T^2}{n \cdot T^2}\right)^{-n} |

| Mathematica | dNdpT[pT_] := pT*(1 + pT^2/(n*T^2))^{-n} |

| Python/SymPy | def dNdpT(pT): return pT * (1 + pT2/(n*T2))**(-n) |

Note: A normalization constant is required for absolute yields.

History

The Tsallis distribution originates from “non-extensive statistics” proposed by Brazilian physicist Constantino Tsallis in 1988. Traditional Boltzmann-Gibbs (BG) statistics assumes extensivity — that entropy is proportional to system size (volume). However, in some physical systems (e.g., gravitational systems, long-range interacting plasmas, high-energy particle collisions), this assumption may not hold. Tsallis introduced a generalized entropy (S_q), and the corresponding energy distribution takes the form above.

Historical Note

The Tsallis distribution gained attention in particle physics in the early 2000s when RHIC experiments revealed that p_T spectra of produced particles followed a power-law tail rather than an exponential (Boltzmann) distribution. The Boltzmann distribution exp(-E/T) drops sharply at high energies, while the Tsallis distribution decreases more slowly — consistent with observations at the LHC, where particles are observed up to p_T of hundreds of GeV/c.

In the early 2010s, ALICE, CMS, and ATLAS showed that the Tsallis distribution fits pp collision data remarkably well. However, it does not fit A+A collisions, because in such collisions particles undergo additional interactions (energy loss, absorption) as they traverse the medium. Thus, p_T spectra in A+A collisions are fitted by Tsallis at low p_T (a few GeV/c) but require an additional power-law component at high p_T (>10 GeV/c).

Physical Meaning

The Tsallis distribution describes the energy distribution of systems that are out of equilibrium or have long-range correlations. Here, n (or q = 1 + 1/n) is the degree of non-extensivity; as n → ∞ (or q → 1), it converges to an exponential distribution. T is not the usual “temperature” but the “Tsallis temperature” or “effective temperature.”

Limitations

This formula only approximates real data. Perfect fits may require multiple Tsallis functions (e.g., double Tsallis) or more complex functions.

n and T depend on particle species (π, K, p, ...).

The microscopic origin of the Tsallis distribution is not yet fully understood. Some interpret it as a “fluctuating temperature” model; others as “non-extensive statistics.”

In A+A collisions, this simple Tsallis distribution fails for p_T above about 8-10 GeV/c.

References

Tsallis, C. (1988). “Possible generalization of Boltzmann-Gibbs statistics” Journal of Statistical Physics

Biró, T. S., et al. (2005). “Non-Gibbs particle spectra from thermal equilibrium” arXiv:hep-ph/0409157

Zheng, H., et al. (2019). “Systematic investigation of the particle spectra in Heavy-ion collisions at LHC” arXiv:1905.08623

7. Bethe-Bloch Energy Loss
Formula

| Unicode | −dE/dx = K·z²/β²·[ln(2mₑβ²γ²/I) − β²] |

| LaTeX | -\frac{dE}{dx} = K \cdot \frac{z^2}{\beta^2} \left[\ln\left(\frac{2m_e \beta^2 \gamma^2}{I}\right) - \beta^2\right] |

| Mathematica | dedx = Kz^2/β^2(Log[2meβ^2*γ^2/I] - β^2) |

| Python/SymPy | dedx = K * z2 / beta2 * (log(2mebeta2*gamma2/I) - beta**2) |

Constants in Bethe-Bloch:

K = 0.307075 MeV·cm²/g (or 4π N_A r_e^2 m_e c^2)

m_e = 0.511 MeV/c² (electron mass)

I = mean excitation energy (material-dependent. Approximations: I ≈ 10·Z eV (Bloch, 1933, crude) or I ≈ 16·Z eV for Z>1 (empirical). For precision work, consult NIST PSTAR database or PDG tables.)

z = charge number of incident particle

DLMF Reference: DLMF 10.21 — Special functions in energy loss calculations

History

The Bethe-Bloch formula has a story spanning heaven and earth. In 1930, Hans Bethe published the non-relativistic version. In 1932, he extended it to the relativistic version (the form used today). Around the same time, Felix Bloch independently derived a similar formula, giving the formula its dual name.

Bethe developed these formulas while still in Germany (Tübingen, then Munich). He was later driven out of Germany in 1933 due to his Jewish heritage and moved to Manchester, England. Remarkably, Bethe received the 1967 Nobel Prize in Physics for his work on energy production in stars (the Bethe-Weizsäcker cycle). His 1932 derivation of this formula was not part of the Nobel-winning work.

Historical Note

“I” is the mean excitation potential, a material-dependent value. In 1933, Bloch proposed the approximation I ≈ 10·Z eV. Modern data show this approximation is rough. For example, lead (Pb, Z=82) has I ≈ 823 eV, while 10·Z = 820 eV — almost exact. But carbon (C, Z=6) has I ≈ 78 eV, while 10·Z = 60 eV — a significant error. A better empirical fit for Z>1 is I ≈ 16·Z eV, but for precision work one should use tabulated values (e.g., from NIST).

This formula is central to particle detector design. For example, the LHC’s CMS silicon tracker measures dE/dx to identify particle types (π, K, p). Electrons and muons have different masses and thus different dE/dx patterns.

One caution: this formula calculates the average energy loss. Actual energy loss follows a Landau-Vavilov distribution, especially in thin detectors, where large fluctuations occur. These fluctuations often make particle identification difficult.

Physical Meaning

This formula tells how much energy a charged particle loses when traversing matter. The 1/β² term means slower particles (smaller β) lose more energy — the “Bragg peak” phenomenon. As a particle comes to rest, its energy loss increases sharply. This is used in proton therapy for cancer to concentrate energy in the tumor.

Limitations

At low energies (β ≲ 0.01, a few MeV/nucleon), the formula fails due to charge screening or complex interactions with orbital electrons.

At ultra-high energies (γ ≳ 1000), density effects and radiative loss become important. For electrons, Bremsstrahlung dominates, making this formula inaccurate.

In thin films, energy loss fluctuations are large, requiring Landau or Vavilov distributions rather than just the mean.

Assumes homogeneous material. Composite or layered structures require more complex Monte Carlo simulations.

References

Bethe, H. (1930). “Zur Theorie des Durchgangs schneller Korpuskularstrahlen durch Materie” Annalen der Physik

Bethe, H. (1932). “Bremsformel für Elektronen relativistischer Geschwindigkeit” Zeitschrift für Physik

Bloch, F. (1933). “Zur Bremsung rasch bewegter Teilchen beim Durchgang durch Materie” Annalen der Physik

NIST PSTAR/ASTAR Database — stopping power calculators

8. Boris Algorithm (Magnetic Field Integration)
8.1 Half-Rotation Vector
Formula

| Unicode | t = (q Δt / (2 γ m)) B |

| LaTeX | \mathbf{t} = \frac{q \Delta t}{2 \gamma m} \mathbf{B} |

| Mathematica | t = (qΔt/(2γ*m)) * B |

| Python/SymPy | t = (qdt/(2gamma*m)) * B |

Important: t is a vector in the direction of B with magnitude proportional to |B|, not a unit vector. This is the correct Boris formulation where t = tan(θ/2) * (B/|B|) is not used; instead the small-angle rotation approximation is applied.

8.2 First Half Rotation
Formula

| Unicode | p⁻ = p_old + p_old × t |

| LaTeX | \mathbf{p}^- = \mathbf{p}{\text{old}} + \mathbf{p}{\text{old}} \times \mathbf{t} |

| Mathematica | pminus = pold + Cross[pold, t] |

| Python/SymPy | p_minus = p_old + np.cross(p_old, t) |

8.3 Scaling Factor
Formula

| Unicode | s = 2t / (1 + |t|²) |

| LaTeX | \mathbf{s} = \frac{2\mathbf{t}}{1 + |\mathbf{t}|^2} |

| Mathematica | s = 2*t/(1 + t.t) |

| Python/SymPy | s = 2*t / (1 + np.dot(t, t)) |

8.4 Second Half Rotation
Formula

| Unicode | p⁺ = p⁻ + p⁻ × s |

| LaTeX | \mathbf{p}^+ = \mathbf{p}^- + \mathbf{p}^- \times \mathbf{s} |

| Mathematica | pplus = pminus + Cross[pminus, s] |

| Python/SymPy | p_plus = p_minus + np.cross(p_minus, s) |

8.5 Final Update (with electric field half-step)
Formula

| Unicode | p_new = p⁺ + (q·Δt/2)·E (then repeat rotation if needed) |

| LaTeX | \mathbf{p}_{\text{new}} = \mathbf{p}^+ + \frac{q \Delta t}{2} \mathbf{E} |

| Mathematica | pnew = pplus + (q*Δt/2)*E |

| Python/SymPy | p_new = p_plus + (q*dt/2)*E |

Note: The full Boris algorithm alternates: half electric acceleration → magnetic rotation → half electric acceleration. This scheme is time-reversible and second-order accurate.

History

The Boris algorithm is a numerical integration method for charged particle motion in magnetic fields, published by J.P. Boris at the U.S. Naval Research Laboratory (NRL) in 1970. Originally developed for plasma physics simulations (fusion research), it is now widely used in particle physics, space physics (particle motion in Earth’s magnetosphere), and accelerator physics.

Historical Note

The most remarkable feature of the Boris algorithm is that it preserves helical motion to second-order accuracy and is time-reversible, avoiding the energy drift seen in simpler methods (e.g., Euler, Runge-Kutta). Ordinary numerical integration methods suffer from numerical energy loss or gain over time; the Boris algorithm is specifically designed to minimize this problem.

The core idea is to split the rotation into two half-rotations. The parameter t = (q·Δt/2)/(γm)·B (scaled by B, not unit vector) corresponds to tan(θ/2) for small rotation angles. The clever step s = 2t/(1+|t|²) recovers sin θ and cos θ from tan(θ/2). This trick allows the Boris algorithm to approximate the exact rotation matrix accurately.

In the mid-2010s, E.G. Evstatiev and J.M. Finn re-examined the Boris algorithm’s mathematical structure, showing it is a special case of Lie operator methods. They explained that “the Boris algorithm redefines the rotation angle θ_B such that tan(θ_B/2) = θ/2.” From this perspective, extensions to higher accuracy are possible.

Physical Meaning

The Boris algorithm preserves the helical motion (gyration) of a particle in a magnetic field to high accuracy. This is important for several reasons:

Energy conservation: the particle’s kinetic energy (|p|²) shows minimal drift over time (when only magnetic field is present).

Structure preservation: the particle’s trajectory approximates a circle (or helix) accurately.

Time reversibility: the algorithm is symmetric when time is reversed.

Limitations

Assumes a uniform magnetic field, but in reality B changes as the particle moves (spatial variation). However, sufficiently small time steps make it approximately valid.

When an electric field E is present, acceleration is split into half-steps. This is accurate, but when both electric and magnetic fields are strong, more complex handling may be needed.

If the time step Δt is too large (compared to the particle’s cyclotron period), the rotation angle exceeds π and the algorithm becomes unstable. Generally Δt ≪ 2π/ω_c (where ω_c = qB/(γm)).

Relativistic effects are included via γ, but when γ is very large (γ ≳ 1000), numerical precision issues may arise.

References

Boris, J. P. (1970). “Relativistic Plasma Simulation - Optimization of a hybrid code” Proc. 4th Conf. on Numerical Simulation of Plasmas, NRL, Washington

Evstatiev, E. G., & Finn, J. M. (2021). “Boris solvers from Lie operators” arXiv:2109.01901

Chanteur, G. M. (2016). “A predictor-corrector schema based upon Boris schema” JpGU Meeting 2016

9. anti-kT Jet Algorithm
9.1 Beam Distance
Formula

| Unicode | d_iB = p_{T,i}^{−2} |

| LaTeX | d_{iB} = p_{T,i}^{-2} |

| Mathematica | diB = pTi^{-2} |

| Python/SymPy | d_iB = pT_i**(-2) |

9.2 Particle-Particle Distance
Formula

| Unicode | d_ij = min(p_{T,i}^{−2}, p_{T,j}^{−2})·ΔR_ij²/R² |

| LaTeX | d_{ij} = \min(p_{T,i}^{-2}, p_{T,j}^{-2}) \cdot \frac{\Delta R_{ij}^2}{R^2} |

| Mathematica | dij = Min[pTi^{-2}, pTj^{-2}] * (ΔRij^2/R^2) |

| Python/SymPy | d_ij = min(pT_i**(-2), pT_j**(-2)) * (dR2 / R2) |

9.3 Delta R Definition
Formula

| Unicode | ΔR_ij² = Δη² + Δφ² |

| LaTeX | \Delta R_{ij}^2 = \Delta \eta^2 + \Delta \phi^2 |

| Mathematica | ΔRij^2 = Δη^2 + Δφ^2 |

| Python/SymPy | dR2 = deta2 + dphi2 |

Note:

Typical jet radius parameter: R = 0.4 or 0.5

For azimuthal angle difference, enforce Δφ = min(|φ_i - φ_j|, 2π - |φ_i - φ_j|)

History

The anti-kT algorithm was proposed in 2008 by Matteo Cacciari, Gavin P. Salam, and Gregory Soyez. Today it is the standard jet clustering algorithm for all major LHC experiments (CMS, ATLAS, ALICE, LHCb).

The algorithm’s distinctive feature is d_iB = p_{T,i}^{-2} and d_ij = min(p_{T,i}^{-2}, p_{T,j}^{-2})·ΔR_ij²/R². The negative exponent (-2) is key: high-p_T particles have very small d_iB and d_ij values, so they cluster first. Low-p_T particles are absorbed later into already-formed jets. As a result, the anti-kT algorithm produces cone-shaped jets with high-p_T particles at the center.

Historical Note

Before anti-kT, the kT algorithm (d_ij = min(p_T,i², p_T,j²)·ΔR_ij²/R²) was widely used. The kT algorithm clustered low-p_T particles first, resulting in jagged jet boundaries that were difficult to interpret. The Cambridge/Aachen algorithm used only ΔR without p_T weighting, but also produced non-ideal jet shapes.

In 2008, Cacciari, Salam, and Soyez asked: “What if we flip the sign of the exponent?” The anti-kT algorithm was born. It behaves like an “ideal cone,” producing well-defined, easily interpretable jet boundaries. They demonstrated mathematically that the algorithm has properties such as “active area equals passive area” and “the anomalous dimension of the area is zero.”

The prefix “anti” simply means the algorithm is the inverse (opposite) of the kT algorithm — the exponent flips from +2 to -2. There is no intended reference to antimatter or particle-antiparticle interactions; the name reflects the mathematical inversion.

Today, the FastJet library is the standard implementation of this algorithm. LHC experiments use FastJet to cluster hundreds of thousands of particles into thousands of jets per event. The processing speed is optimized from O(N²) to O(N log N), enabling real-time data processing.

Physical Meaning

The anti-kT algorithm groups particles produced in a collision into “jets.” Jets are clusters of particles resulting from the hadronization of quarks and gluons in hadron collisions, used to estimate the momentum and direction of the parent particle (quark/gluon). Correctly reconstructing jets is one of the most important tasks in QCD phenomenology.

Limitations

Soft particles (very small p_T) can be randomly absorbed into jets, adding uncertainty to jet momentum measurements.

Jet overlap: if two jets are too close (ΔR < 2R), they may merge into one large jet. This is partially resolved by a “split-merge” step.

Underlying event: additional particles from the same collision introduce errors in jet measurements. This effect is corrected by estimating the underlying event density.

Radiation: QCD radiation (bremsstrahlung) creates long tails in jets, blurring jet boundaries. The anti-kT algorithm minimizes but does not eliminate this problem.

References

Cacciari, M., Salam, G. P., & Soyez, G. (2008). “The anti-k_t jet clustering algorithm” JHEP 04, 063

Cacciari, M., & Salam, G. P. (2006). “Dispelling the N³ myth for the k_t jet-finder” Physics Letters B

FastJet Project — official implementation

10. CP Violation (B⁰ → J/ψ K⁰S)
Formula

| Unicode | A_CP(t) = sin(2β)·sin(Δm_d·t) |

| LaTeX | \mathcal{A}_{CP}(t) = \sin(2\beta) \cdot \sin(\Delta m_d \cdot t) |

| Mathematica | ACP[t_] := Sin[2*β]Sin[Δmdt] |

| Python/SymPy | def A_CP(t): return sin(2*beta) * sin(delta_md * t) |

Note: This is the simplified time-dependent CP asymmetry for the decay B⁰ → J/ψ K⁰_S in the Standard Model. The full expression is A_CP(t) = S·sin(Δm_d·t) − C·cos(Δm_d·t), where S = sin(2β) and C ≈ 0 for this channel. The C term is negligible in the Standard Model but is an important experimental test for new physics.

History

CP violation is one of the deepest mysteries in particle physics. This formula describes the time-dependent CP asymmetry in the decay of B⁰ mesons to J/ψ (charm quark-antiquark pair) and K⁰_S (a neutral kaon containing a strange quark). Here, sin(2β) is the angle of the CKM matrix, and Δm_d is the mass difference between B⁰ and B̄⁰.

Historical Note

The history of CP violation dates back to 1964, when James Cronin and Val Fitch first discovered CP violation in neutral kaon decays. This discovery shattered the belief that particles and antiparticles always behave symmetrically, and earned them the 1980 Nobel Prize.

In 2001, the BaBar experiment (SLAC, USA) and Belle experiment (KEK, Japan) used this formula to confirm CP violation in B meson decays. They produced hundreds of millions of B mesons at special “B factories” and measured their time-dependent decays. The result sin(2β) ≈ 0.73, consistent with Standard Model predictions. This discovery earned the BaBar and Belle spokespersons Jonathan Dorfan and Hiroaki Aihara the 2008 Panofsky Prize from the American Physical Society.

A surprising point: why is sin(2β) around 0.7? The Standard Model predicts this value, but cannot answer why it is so large. This large angle comes from the phase structure of the CKM matrix, and why it has that value remains one of nature’s mysteries.

Physical Meaning

This formula provides clues to why the universe is made of matter rather than antimatter. After the Big Bang, matter and antimatter were created in equal amounts. Yet today there is almost no antimatter in the universe. Without CP violation, matter and antimatter would have behaved identically and completely annihilated, leaving only photons. CP violation creates a subtle asymmetry between matter and antimatter, which may explain why matter survived.

Limitations

Valid only within the Standard Model. New physics (e.g., supersymmetry, extra dimensions) could change the value of sin(2β) or introduce a non-zero C term.

Assumes the vacuum phase is zero. In reality, CP violation could also occur in the vacuum, adding a cos(Δm_d·t) term.

Δm_d, which describes B⁰-B̄⁰ mixing, is difficult to calculate purely within the Standard Model and is experimentally measured.

Only weak interactions are considered. Strong and electromagnetic CP violation are negligibly small.

References

Cronin, J. W., & Fitch, V. L. (1964). “Evidence for the 2π Decay of the K₂⁰ Meson” Physical Review Letters

BaBar Collaboration (2001). “Observation of CP Violation in the B⁰ Meson System” Physical Review Letters

Belle Collaboration (2001). “Observation of Large CP Violation in the Neutral B Meson System” Physical Review Letters

CKMfitter Group — global analysis of CKM matrix

11. Inelastic Cross-Section
Formula

| Unicode | σ_inel(√s) = 72.9·(√s/13000)^{0.096} mb |

| LaTeX | \sigma_{\text{inel}}(\sqrt{s}) = 72.9 \cdot \left(\frac{\sqrt{s}}{13000}\right)^{0.096} \text{ mb} |

| Mathematica | σinel[s_] := 72.9*(s/13000)^0.096 |

| Python/SymPy | sigma_inel = 72.9 * (sqrt_s/13000)**0.096 |

Note: √s in GeV. Valid only near √s = 13 TeV (13000 GeV). Extrapolation outside [10⁴, 10⁵] GeV is not reliable.

History

The inelastic cross-section represents the probability that two colliding particles (e.g., protons) interact and produce new particles. This formula is an empirical fit to data from the LHC’s TOTEM, ATLAS, ALICE, and CMS experiments.

The exponent 0.096 in (√s/13000) means the cross-section increases very slowly with energy. For example, when √s increases from 7 TeV (7000 GeV) to 13 TeV (13000 GeV) — about a factor of two — the cross-section increases by only about 2^0.096 ≈ 1.07 times (7% increase). This is consistent with the expectation that cross-sections rise logarithmically with energy.

Historical Note

The slow logarithmic rise of the cross-section with energy comes from the nature of the strong interaction. The “pomeron exchange” theory predicts that at high energies, the cross-section rises as ~ s^ε, where ε is about 0.08-0.1. The value 0.096 in the formula is consistent with pomeron theory.

When the LHC increased collision energy from 7 TeV (2010) to 13 TeV (2015), researchers checked whether the inelastic cross-section increased as expected. The results: σ_inel(7 TeV) ≈ 71 mb, σ_inel(8 TeV) ≈ 72 mb, σ_inel(13 TeV) ≈ 75 mb — in good agreement with the formula.

An interesting fact: the total cross-section is about 100 mb. The inelastic part is 75 mb, elastic 25 mb. So about 75% of collisions are inelastic (producing new particles) and 25% are elastic (simple angular deflection). At LHC energies, the elastic fraction is relatively small.

Physical Meaning

This cross-section is used to calculate how many collision events can be expected at the LHC. For example, if the LHC’s instantaneous luminosity is 10³⁴ cm⁻²s⁻¹ and σ_inel = 75 mb = 75 × 10⁻²⁷ cm², then the collision rate per second = L × σ = 10³⁴ × 75 × 10⁻²⁷ = 7.5 × 10⁸ Hz — 750 million collisions per second. Each collision produces thousands of particles, making data processing a monumental challenge.

Limitations

Valid only for proton-proton (pp) collisions. Proton-antiproton (p p̄), proton-nucleus (pA), and nucleus-nucleus (AA) collisions have different cross-section relations.

Valid range is √s ≈ 10⁴ to 10⁵ GeV (10 to 100 TeV). At higher energies, new physics (e.g., supersymmetry, extra dimensions) could alter the growth pattern.

Calculates only the inelastic part. The elastic cross-section grows differently with energy.

In cosmic ray physics, much higher energies (10⁵ to 10⁸ GeV) are of interest. Extrapolating this formula to such energies is not reliable.

References

TOTEM Collaboration (2013). “Measurement of the pp inelastic cross-section at √s = 7 TeV” EPL

ATLAS Collaboration (2016). “Measurement of the inelastic pp cross-section at √s = 13 TeV” Nature Communications

PDG: Cross-section data

Appendix A: Fundamental Constants (CODATA 2018 / PDG 2022)
| c | 2.99792458 × 10⁸ m/s | Speed of light. Fundamental constant of special relativity. |

| ℏ | 6.582119569 × 10⁻²⁵ GeV·s | Reduced Planck constant. Fundamental action quantum of quantum mechanics. |

| ℏc | 0.1973269804 GeV·fm | Conversion factor between distance and energy in nuclear/particle physics. |

| m_e | 0.511 MeV/c² | Electron mass. Key input to the Bethe-Bloch formula. |

| K | 0.307075 MeV·cm²/g | Bethe-Bloch constant. Universal, independent of material properties. |

| α_s(M_Z) | 0.1180 | Strong coupling constant at the Z boson mass. Reference point for QCD. |

| M_Z | 91.1876 GeV | Z boson mass. Energy scale of electroweak interactions. |

| sin(2β) | 0.699 | CP violation angle of the CKM matrix. Core of B physics. |

| Δm_d | 0.5065 ps⁻¹ | Mass difference for B⁰-B̄⁰ oscillation. Determines the period of time-dependent CP violation. |

Appendix B: Particle-Specific Tsallis Parameters
| Particle | T (GeV) | n |

| π⁺, π⁻ | 0.095 | 8.0 |

| K⁺, K⁻ | 0.140 | 7.5 |

| p, p̄ | 0.180 | 7.0 |

| Λ⁰ | 0.200 | 6.5 |

Note: Parameters for W⁺, W⁻, Z⁰, and H⁰ are not well-established from LHC data and are omitted here. The values in earlier versions (T≈10-20 GeV, n≈3.5-4.0) were illustrative only and lack experimental verification.

Meaning of parameters:

T (Tsallis temperature) is related to the particle’s average kinetic energy. Pions have the smallest T (”coldest”) and Λ⁰ the largest T among light hadrons.

n (or q = 1 + 1/n) indicates the degree of non-extensivity. Larger n (q closer to 1) brings the distribution closer to exponential. Heavier particles tend to have smaller n (larger q), interpreted as undergoing more interactions with the medium and exhibiting more non-thermal behavior.

Acknowledgments & References
This document is based on the following sources:

Clay Mathematics Institute. “Yang-Mills & the Mass Gap”

Biró, T. S., et al. (2005). “Non-Gibbs particle spectra from thermal equilibrium” arXiv:hep-ph/0409157

Wikipedia. “Bethe formula” (Archived 2020)

Evstatiev, E. G., & Finn, J. M. (2021). “Boris solvers from Lie operators” arXiv:2109.01901

Cacciari, M., Salam, G. P., & Soyez, G. (2008). “The anti-k_t jet clustering algorithm” JHEP 04, 063

Zheng, H., et al. (2019). “Systematic investigation of the particle spectra in Heavy-ion collisions at LHC” arXiv:1905.08623

Chanteur, G. M. (2016). “A predictor-corrector schema based upon Boris schema” JpGU Meeting 2016

Cacciari, M., Salam, G. P., & Soyez, G. (2008). “The anti-kt jet clustering algorithm” Google Scholar

Appendix C: Errata & Clarifications
This errata documents corrections and clarifications to improve physical accuracy, notational consistency, and clarity of scope.

Each item is classified as one of: Error, Approximation (unstated assumption), Omission, or Inconsistency.

C.1 Chapter Numbering Inconsistency (Inconsistency)
Location: Table of contents vs. body text

Issue:

The chapter numbering has a gap. Chapters 1–9 and 10–11 are present, but a chapter on Breit-Wigner resonance — referenced implicitly in the context of W/Z boson peaks — is missing between chapters 9 and 10. This leaves the numbering misleading.

| Body Chapter | Title | Status |

| 9 | anti-kT Jet Algorithm | ✓ Present |

| — | Breit-Wigner Resonance | ⚠️ Missing |

| 10 | CP Violation | Present but chapter gap unacknowledged |

Correction: Either restore the Breit-Wigner chapter or add a note acknowledging its intentional omission. See C.5 below.

C.2 Tsallis Distribution — Particle Mass Neglected Without Notice (Approximation)
Location: Chapter 6, formula

Current form:


dN/dp_T ∝ p_T · (1 + p_T²/(n·T²))^{−n}

Issue:

This form silently assumes m ≪ p_T (the ultrarelativistic limit). The standard form used in experimental literature employs the transverse mass m_T:


dN/dp_T ∝ p_T · (1 + m_T / (n·T))^{−n}

where: m_T = √(p_T² + m²)   (transverse mass)

For pions (m ≈ 0.14 GeV) the difference is small at p_T ≳ 1 GeV, but for protons (m ≈ 0.938 GeV) the two forms differ by tens of percent at low p_T (below ~2 GeV/c).

Suggested addition:

Note: The formula above is the ultrarelativistic approximation (m ≪ p_T). When particle mass is significant — especially for low-p_T protons and Λ⁰ — replace p_T² with m_T² = p_T² + m² in the denominator.

C.3 2-Loop Running Coupling — Analytic Approximation Not Flagged (Approximation)
Location: Chapter 4.3

Current form:


α_s⁽²⁾(μ) = α_s⁽¹⁾·[1 − (β₁/β₀)·α_s⁽¹⁾·ln(1 + 2β₀·α_s(M_Z)·ln(μ/M_Z))]

Issue:

This is an approximate analytic solution, not the exact 2-loop result. The exact 2-loop renormalization group equation is:


μ · dα_s/dμ = −2α_s · (β₀α_s + β₁α_s²)

which must be integrated numerically for precision work. The analytic form above can deviate by several percent at μ < 5 GeV or μ > 1 TeV.

Suggested addition:

Note: This is an analytic approximation to the 2-loop RGE. For precision calculations (PDF fitting, NNLO analyses), use numerical integration via RunDec (Chetyrkin & Steinhauser, 2000) or the CRunDec library.

C.4 CP Asymmetry Formula — C = 0 Approximation Not Shown in the Formula Table (Approximation)
Location: Chapter 10, formula table

Current form:


A_CP(t) = sin(2β) · sin(Δm_d · t)

Issue:

The body text Note already explains this, but the formula table itself does not flag the approximation. The full Standard Model expression is:


A_CP(t) = S·sin(Δm_d·t) − C·cos(Δm_d·t)

where S = sin(2β),  C ≈ 0  (specific to B⁰ → J/ψ K⁰_S)

A non-zero C term would be a signal of new physics. Current world average from BaBar/Belle/LHCb: C = −0.017 ± 0.021 — consistent with zero but non-trivially measured.

Suggested correction to the Unicode row:


A_CP(t) = sin(2β)·sin(Δm_d·t)   [C = 0 approximation; full form: S·sin(Δm_d·t) − C·cos(Δm_d·t)]

C.5 Missing Chapter — Breit-Wigner Resonance (Omission)
Location: Between Chapters 9 and 10

Issue:

The Breit-Wigner resonance formula is absent from the document, despite being central to LHC physics — it describes the invariant-mass peaks used to identify the W, Z, and Higgs bosons.

Proposed formula:

| Unicode | σ(E) = σ_peak · Γ² / [(E − M)² + Γ²/4] |

| LaTeX | \sigma(E) = \sigma_{\text{peak}} \cdot \frac{\Gamma^2}{(E-M)^2 + \Gamma^2/4} |

| Python/SymPy | sigma = sigma_peak * Gamma**2 / ((E - M)2 + Gamma2 / 4) |

Key parameters (PDG 2022):

| Particle | Mass M (GeV) | Width Γ (GeV) |

| Z⁰ | 91.1876 | 2.4952 |

| W± | 80.377 | 2.085 |

| H⁰ | 125.25 | 3.2 × 10⁻³ |

The extremely narrow Higgs width (Γ/M ~ 10⁻⁵) is why indirect methods are needed to measure it at the LHC.

C.6 Boris Algorithm — Scope Within LHC Context Overstated (Inconsistency)
Location: Chapter 8

Issue:

The text implies the Boris algorithm is used for particle tracking inside LHC detectors. In practice, Geant4 — the standard LHC detector simulation toolkit — uses Runge-Kutta (Dormand-Prince RK45 or Cash-Karp) steppers via G4MagIntegratorStepper, not the Boris algorithm.

The Boris algorithm is the standard in:

Plasma physics simulations (its original application)

Space physics — particle tracing in Earth’s magnetosphere

Accelerator beam dynamics — tracking the proton beam itself (not secondaries in the detector)

Suggested correction:

Replace any wording suggesting Boris is used for LHC detector simulation with: ”The Boris algorithm is the standard method in accelerator beam dynamics and plasma simulations; detector-level particle tracking in LHC experiments relies on Geant4’s Runge-Kutta integrators.”

C.7 Missing Unit Conversion Table (Omission)
Location: Appendix A supplement

Issue:

Appendix A lists fundamental constants but omits the unit conversions that practitioners need daily when working with these formulas.

Proposed addition:

| Conversion | Value | Common use |

| 1 fm | = 10⁻¹⁵ m | Nuclear/particle length scale |

| 1 mb (millibarn) | = 10⁻²⁷ cm² = 10⁻³¹ m² | Cross-section unit |

| 1 GeV⁻¹ | ≈ 0.197 fm (= ℏc) | Energy-to-distance conversion |

| 1 GeV/c² | ≈ 1.783 × 10⁻²⁷ kg | Particle mass unit |

| 1 ns | = 10⁻⁹ s | Detector timing unit |

| c | = 29.98 cm/ns | Convenient form for detector design |

C.8 Minor Notational Consistency Recommendations (Inconsistency)
| Chapter 1.2 | β = |p| / E | β = |\mathbf{p}| / E | p is a vector; bold notation recommended |

| Chapter 9.2 | ΔR_ij mixed style | \Delta R_{ij} throughout | Subscript style mixed between sections |

| Appendix B | “n (or q = 1 + 1/n)” inline | Separate table relating q and n | Prevents reader confusion |

| Chapters 5, 6 | √s unit stated; others not | Add “(√s in GeV)” to all empirical fits | Chapters 11 has it; others inconsistent |




1. BREIT-WIGNER RESONANCE FORMULA
What It Is
The Breit-Wigner distribution describes the lineshape of an unstable particle (resonance) as a function of center-of-mass energy. When a particle like the Z boson, W boson, or Higgs boson is produced and then decays, its invariant mass is not a single sharp value but a distribution peaking at the particle’s mass and decaying as a Lorentzian.

Why It’s Essential
Fit the Z boson peak at 91.1876 GeV

Distinguish a real resonance from statistical fluctuations

Calculate the production cross-section of a short-lived particle

Understand the Higgs discovery (2012)

Mathematical Form (Standard Relativistic Breit-Wigner)
Simplest form (constant width, near peak):

Unicode: σ(E) = σ_peak · (Γ²/4) / ((E − M)² + Γ²/4)

LaTeX: \sigma(E) = \sigma_{\text{peak}} \cdot \frac{\Gamma^2/4}{(E - M)^2 + \Gamma^2/4}

Mathematica: σ[E_] := σpeak * (Γ^2/4) / ((E - M)^2 + Γ^2/4)

Python: def sigma(E, sigma_peak, M, Gamma): return sigma_peak * (Gamma**2/4) / ((E - M)2 + Gamma2/4)

Full relativistic form (energy denominator as E² − M²):

Unicode: σ(E) ∝ 1 / ((E² − M²)² + M² Γ²)

LaTeX: \sigma(E) \propto \frac{1}{(E^2 - M^2)^2 + M^2 \Gamma^2}

Python: def sigma_rel(E, M, Gamma): return 1 / ((E2 - M2)2 + M2 * Gamma**2)

Physical Meaning of Parameters
Parameter: M (Mass) — Peak position of resonance (GeV) — Typical: Z: 91.1876, W: 80.379, H: 125.25 Parameter: Γ (Width) — Decay rate, inverse lifetime (GeV) — Typical: Z: 2.4952, W: 2.085, H: 0.0032 Parameter: σ_peak — Peak cross-section — Maximum production rate at E=M Parameter: ℓ — Orbital angular momentum — Affects lineshape near threshold: 0 (S-wave), 1 (P-wave)

Key PDG Values (2024)
Particle: Z⁰ — Mass: 91.1876 ± 0.0021 GeV — Width: 2.4952 ± 0.0023 GeV — Γ/M: 0.027 — Decay modes: hadrons (70%), e⁺e⁻ (3.36%), μ⁺μ⁻ (3.37%) Particle: W⁺ — Mass: 80.379 ± 0.012 GeV — Width: 2.085 ± 0.042 GeV — Γ/M: 0.026 — Decay modes: ℓν (11%), hadrons (67%) Particle: H⁰ — Mass: 125.20 ± 0.11 GeV — Width: 0.0032 ± 0.0015 GeV — Γ/M: 0.000026 — Decay modes: bb (58%), WW* (21%), gg (8%)

Important Relations
Full Width at Half Maximum (FWHM): FWHM = 2Γ (for constant-width Breit-Wigner)

Normalization check: ∫_{-∞}^{∞} (Γ²/4) / ((E-M)² + Γ²/4) dE = πΓ/2

Known Limitations & Edge Cases
Very narrow widths (Higgs-like): Γ ≪ detector resolution → Voigt profile (Gaussian convolved with Breit-Wigner)

Very broad widths (Z-like): Γ/M > 0.1 → use relativistic form with energy-dependent width

Multiple interfering resonances: sum of Breit-Wigners with complex coefficients

Near-threshold production: Blatt-Weisskopf barrier factors

Implementation Example (Python)
import numpy as np import matplotlib.pyplot as plt

def breit_wigner(E, M, Gamma, sigma_peak=1): return sigma_peak * (Gamma**2/4) / ((E - M)2 + Gamma2/4)

M_Z = 91.1876 Gamma_Z = 2.4952 E_range = np.linspace(80, 102, 1000) sigma_Z = breit_wigner(E_range, M_Z, Gamma_Z) sigma_Z = sigma_Z / np.max(sigma_Z)

print(f”Z boson: FWHM = {2 * Gamma_Z:.4f} GeV”)

plt.plot(E_range, sigma_Z) plt.xlabel(”Center-of-mass energy E (GeV)”) plt.ylabel(”Normalized cross-section”) plt.title(f”Breit-Wigner: Z boson (M={M_Z} GeV, Γ={Gamma_Z} GeV)”) plt.grid(True) plt.show()

Known Failures (When NOT to use)
Does NOT describe resonances with very strong energy-dependent width (use Flatté or coupled-channel formalism)

Does NOT describe resonances with overlapping neighbors (use K-matrix)

Does NOT describe resonances with significant non-resonant background (requires interference term)

References
PDG 2024: “Breit-Wigner and Relativistic Breit-Wigner”

Breit & Wigner (1936), Phys. Rev. 49, 519

Alternative: Gounaris & Sakurai (1968), Phys. Rev. Lett. 21, 244

2. PARTON DISTRIBUTION FUNCTIONS (PDFs)
What It Is
PDFs describe the probability density to find a parton (quark, antiquark, or gluon) inside a hadron (e.g., proton) carrying a fraction x of the hadron’s longitudinal momentum at an energy scale Q². Without PDFs, you cannot calculate the initial state of any hadron collider event.

Why It’s Essential
The LHC collides protons, not quarks. The actual collision happens between one parton from each proton.

The center-of-mass energy of the parton-parton collision is √ŝ = √(x₁x₂) √s, which is always less than the proton-proton √s.

PDFs determine the luminosity for specific processes (e.g., gg → H is dominant at LHC, while qq → W is dominant at Tevatron).

Mathematical Form
The PDF f_i(x, Q²) for parton type i satisfies:

Unicode: ∫₀¹ dx · x · f_i(x, Q²) = momentum fraction carried by parton i LaTeX: \int_0^1 dx ; x f_i(x, Q^2) = \langle x_i \rangle

Sum Rules (constraints from proton quantum numbers):

Momentum sum: ∫₀¹ x·(Σ_q f_q + f_g) dx = 1 — All proton momentum carried by partons Valence sum (u): ∫₀¹ (f_u - f_ū) dx = 2 — Proton contains 2 up quarks Valence sum (d): ∫₀¹ (f_d - f_d̄) dx = 1 — Proton contains 1 down quark

PDF Parameterization (HERA-style, simplified)
At a starting scale Q₀² ≈ 1 GeV², PDFs are often parameterized as:

Unicode: x·f_i(x, Q₀²) = A_i · x^{a_i} · (1-x)^{b_i} · (1 + c_i·√x + d_i·x) LaTeX: x f_i(x, Q_0^2) = A_i x^{a_i} (1-x)^{b_i} (1 + c_i\sqrt{x} + d_i x)

Evolution (DGLAP) — See Priority 2
PDFs change with Q² via the DGLAP equations. This is crucial for extrapolating from fixed-target experiments (Q² ~ few GeV²) to LHC scales (Q² ~ 10⁴ GeV²).

Numerical Example (CT18NLO at Q² = M_Z² = 8281 GeV²)
At x ≈ 0.01 (typical for Higgs production at 13 TeV): gluon: xg(x) ≈ 5.0 u quark: xu(x) ≈ 0.8 d quark: xd(x) ≈ 0.5 s, c, b quarks: significantly smaller

At x ≈ 0.5 (high-x, valence dominated): xu(x) ≈ 0.05, xd(x) ≈ 0.02, gluon negligible

Known Limitations
Non-perturbative region: At x < 10⁻⁵ or x > 0.9, PDFs are poorly constrained by data

Nuclear PDFs: For pA or AA collisions, PDFs are modified (shadowing, EMC effect)

Photon PDF: At high energies, the proton also has a photon content f_γ

Uncertainty quantification: PDFs come with Hessian or Monte Carlo error sets

Implementation Note
Do NOT attempt to implement PDFs from scratch. Use established libraries:

LHAPDF (C++/Python): lhapdf.getPDF(”CT18NLO”)

APFEL (Fortran/Python): Evolution and convolution

PineAPPL (C++): Fast interpolation grids

Known Failures
Leading-order PDFs cannot describe data at LHC precision (need NLO or NNLO)

Some processes require transverse momentum dependent PDFs (TMDs)

Small-x saturation effects not described by linear DGLAP

References
CT18: Hou et al. (2021), arXiv:1908.11394

NNPDF4.0: Ball et al. (2022), arXiv:2109.02671

MSHT20: Bailey et al. (2021), arXiv:2012.04684

LHAPDF: Buckley et al. (2015), arXiv:1412.7420

3. MATRIX ELEMENT |M|²
What It Is
The matrix element squared, |M|², is the quantum mechanical probability amplitude for a specific initial state (e.g., gg) to transition to a specific final state (e.g., Higgs boson, or two jets). It is the central ingredient of every cross-section calculation in particle physics.

Why It’s Essential
The cross-section σ ∝ ∫ |M|² dΦ (phase space)

Different processes have different |M|² → different angular distributions, different production rates

Interference between diagrams comes from cross-terms in |M|²

New physics beyond the Standard Model often manifests as an excess in a specific region of phase space

General Form (Lorentz-invariant)
Unicode: dσ = (1/(2s)) · |M|² · dΦ_n LaTeX: d\sigma = \frac{1}{2s} |\mathcal{M}|^2 d\Phi_n

Where: s = (p₁ + p₂)² = parton-parton center-of-mass energy squared dΦ_n = n-body Lorentz-invariant phase space

Example 1: gg → gg (QCD 2→2 scattering)
This is the most common process at the LHC. The amplitude is non-trivial due to color factors:

Unicode: |M|² = (9/4)·g_s⁴·(3 − t̂û/ŝ² − ŝû/t̂² − ŝt̂/û²) LaTeX: |\mathcal{M}|^2 = \frac{9}{4} g_s^4 \left(3 - \frac{\hat{t}\hat{u}}{\hat{s}^2} - \frac{\hat{s}\hat{u}}{\hat{t}^2} - \frac{\hat{s}\hat{t}}{\hat{u}^2}\right)

Where Mandelstam variables for 2→2 scattering: ŝ = (p₁ + p₂)² = x₁x₂ s (parton-level CM energy squared) t̂ = (p₁ - p₃)² = -ŝ(1 - cos θ*)/2 (momentum transfer squared) û = (p₁ - p₄)² = -ŝ(1 + cos θ*)/2 and ŝ + t̂ + û = 0 for massless partons

Example 2: q q̄ → Z⁰ → e⁺ e⁻ (Resonant production, simplified)
At the resonance peak (√ŝ ≈ M_Z), the propagator dominates:

Unicode: |M|² ∝ (g_Z⁴) / ((ŝ − M_Z²)² + M_Z² Γ_Z²) LaTeX: |\mathcal{M}|^2 \propto \frac{g_Z^4}{(\hat{s} - M_Z^2)^2 + M_Z^2 \Gamma_Z^2}

This is exactly the Breit-Wigner propagator from Section 1, squared. The angular distribution in the Z rest frame is (1 + cos²θ) for massless fermions.

Color and Spin Averaging
For initial-state hadrons, we must average over initial spins and colors:

Factor for quark: Spin average 1/2, Color average 1/3 Factor for gluon: Spin average 1/2, Color average 1/8

Thus, for a process with two initial gluons: average factor = (1/2)² × (1/8)² = 1/256.

Known Limitations
Perturbative expansion: |M|² = |M|₀² + α_s|M|₁² + α_s²|M|₂² + ... (LO, NLO, NNLO)

Infrared divergences: Cancel with virtual corrections (KLN theorem)

Large logarithms: Require resummation (parton showers)

Non-perturbative effects: Cannot be computed for low-energy hadronization

Implementation Note
Do NOT compute |M|² by hand except for simple cases. Use automated tools:

MadGraph5_aMC@NLO: Event generation, NLO matching

Sherpa: Multi-purpose event generator

Herwig 7: Angular-ordered parton shower

Pythia 8: Hadronization, MPI, resonance decays

Known Failures
Standard Model |M|² fails to explain several anomalies (g-2, B-decays)

Non-perturbative region (Q < 1 GeV) → lattice QCD needed

Processes with many particles (> 2→5) become computationally expensive

References
Feynman diagrams and QED: Feynman (1949), Phys. Rev. 76, 769

Color factors: ‘t Hooft (1974), Nucl. Phys. B72, 461

MadGraph: Alwall et al. (2014), arXiv:1405.0301

4. GLAUBER MODEL (Heavy-Ion Collisions)
What It Is
The Glauber model describes the collision of two nuclei (e.g., Pb+Pb or Au+Au) in terms of independent nucleon-nucleon (NN) collisions. It calculates quantities like:

Number of participating nucleons (N_part)

Number of binary NN collisions (N_coll)

Impact parameter b

Transverse energy density at mid-rapidity

Why It’s Essential
Heavy-ion collisions at LHC (ALICE, CMS, ATLAS) probe Quark-Gluon Plasma (QGP)

The initial condition (N_part, N_coll, eccentricity ε₂) determines QGP properties

Without Glauber, you cannot relate measured particle multiplicities to collision centrality

Mathematical Form
Nuclear Thickness Function T_A(s):

Unicode: T_A(s) = ∫ dz · ρ_A(s, z) LaTeX: T_A(\mathbf{s}) = \int_{-\infty}^{\infty} dz ; \rho_A(\mathbf{s}, z)

Where ρ_A(r) is the nuclear density (Woods-Saxon):

Unicode: ρ_A(r) = ρ_0 / (1 + exp((r − R_A)/a)) LaTeX: \rho_A(r) = \frac{\rho_0}{1 + \exp\left(\frac{r - R_A}{a}\right)}

With typical parameters for Lead-208: R_A = 6.62 fm a = 0.546 fm ρ₀ normalized so ∫ ρ_A d³r = A = 208

Nuclear Overlap Function T_AB(b):

Unicode: T_AB(b) = ∫ d²s · T_A(s) · T_B(b − s) LaTeX: T_{AB}(\mathbf{b}) = \int d^2s ; T_A(\mathbf{s}) ; T_B(\mathbf{b} - \mathbf{s})

Number of Participating Nucleons (Wounded Nucleon Model):

Unicode: N_part(b) = ∫ d²s · [T_A(s)·(1 − e^{−σ_NN·T_B(b−s)}) + T_B(b−s)·(1 − e^{−σ_NN·T_A(s)})] LaTeX: N_{\text{part}}(\mathbf{b}) = \int d^2s \left[ T_A(\mathbf{s}) \left(1 - e^{-\sigma_{NN} T_B(\mathbf{b}-\mathbf{s})}\right) + T_B(\mathbf{b}-\mathbf{s}) \left(1 - e^{-\sigma_{NN} T_A(\mathbf{s})}\right) \right]

Number of Binary Collisions:

Unicode: N_coll(b) = σ_NN · ∫ d²s · T_A(s) · T_B(b − s) LaTeX: N_{\text{coll}}(\mathbf{b}) = \sigma_{NN} \int d^2s ; T_A(\mathbf{s}) ; T_B(\mathbf{b} - \mathbf{s})

Where σ_NN is the inelastic nucleon-nucleon cross-section (≈ 70 mb at √s_NN = 5.02 TeV for Pb+Pb collisions).

Centrality Definition
Centrality 0-5% (central): b range 0 → ~4.5 fm, N_part ~400, N_coll ~2000 Centrality 20-30%: b range ~7 → ~9 fm, N_part ~200, N_coll ~800 Centrality 70-80% (peripheral): b range ~12 → ~15 fm, N_part ~20, N_coll ~30

Known Limitations
No nuclear deformation: Standard Glauber assumes spherical nuclei

No shadowing: PDF modifications in nuclei not included

No parton energy loss: High-p_T particles are suppressed (quenching)

No fluctuation effects: Use Monte Carlo Glauber for event-by-event fluctuations

Monte Carlo Glauber (MC Glauber)
Instead of smooth densities, MC Glauber:

Samples nucleon positions from Woods-Saxon distribution

Collides nuclei along the z-axis

For each NN pair, determines if a collision occurred (probability ∝ σ_NN)

Repeats for many events (~10⁶) to build distributions

This captures fluctuations in N_part and N_coll, eccentricity ε₂, and triangularity ε₃.

Known Failures
Does not describe parton energy loss (requires transport models)

Does not describe collective flow (requires hydrodynamic evolution)

Does not describe pre-equilibrium dynamics (requires kinetic theory)

For small systems (p+p, p+Pb), the Glauber model may not apply

References
Glauber (1959), “Lectures in Theoretical Physics”, Vol. 1

Miller et al. (2007), Ann. Rev. Nucl. Part. Sci. 57, 205 (arXiv:0704.1986)

5. α_s 2-LOOP RUNNING COUPLING (Precision Form)
What It Is
The strong coupling constant α_s is not constant. It “runs” with the energy scale μ according to the Renormalization Group Equation (RGE). The 2-loop approximation improves the 1-loop result by including the β₁ coefficient, which accounts for the next-order quantum corrections from gluon loops and quark loops.

Why Precision Matters
At LHC energies (μ ~ 100 GeV), 1-loop error is ~1%. At μ ~ 1 GeV, error grows to ~10%

PDF fitting, jet cross-sections, and top quark pair production require NNLO precision

Higgs production cross-section via gluon fusion is proportional to α_s²

Exact 2-Loop RGE (Differential Form)
Unicode: μ · dα_s/dμ = −2α_s · (β₀α_s + β₁α_s²) LaTeX: \mu \frac{d\alpha_s}{d\mu} = -2\alpha_s \left( \beta_0 \alpha_s + \beta_1 \alpha_s^2 \right)

Where (with number of active quark flavors n_f = 5 at LHC energies):

β₀ = (33 - 2n_f) / (12π) ≈ 0.610 β₁ = (153 - 19n_f) / (24π²) ≈ 0.124

Numerical Integration (Python)
import numpy as np from scipy.integrate import odeint

def dαs_dμ(αs, μ, β0, β1): return -2 * αs * (β0 * αs + β1 * αs**2) / μ

M_Z = 91.1876 αs_MZ = 0.1180 β0 = (33 - 25)/(12np.pi) β1 = (153 - 195)/(24np.pi**2)

μ_values = np.logspace(-1, 3, 100) αs_values = odeint(lambda αs, μ: dαs_dμ(αs, μ, β0, β1), αs_MZ, μ_values).flatten()

print(f”α_s(1 GeV) = {αs_values[μ_values.argmin()]:.4f}”) print(f”α_s(100 GeV) = {αs_values[np.argmax(μ_values > 100)]:.4f}”) print(f”α_s(1000 GeV) = {αs_values[np.argmax(μ_values > 1000)]:.4f}”)

Approximate Analytic Form (with caveats)
Unicode: α_s⁽²⁾(μ) = α_s⁽¹⁾·[1 − (β₁/β₀)·α_s⁽¹⁾·ln(1 + 2β₀·α_s(M_Z)·ln(μ/M_Z))] LaTeX: \alpha_s^{(2)}(\mu) = \alpha_s^{(1)} \left[1 - \frac{\beta_1}{\beta_0} \alpha_s^{(1)} \ln\left(1 + 2\beta_0 \alpha_s(M_Z) \ln(\mu/M_Z)\right)\right]

Caveat: This is an analytic approximation. For μ < 5 GeV or μ > 1 TeV, it deviates by several percent from the exact numerical solution.

Threshold Matching (Changing n_f)
When μ crosses a quark mass threshold (m_c ≈ 1.27 GeV, m_b ≈ 4.18 GeV, m_t ≈ 172.5 GeV), the number of active flavors n_f changes:

Unicode: α_s⁽ⁿᶠ⁺¹⁾(μ = m_q) = α_s⁽ⁿᶠ⁾(μ = m_q) LaTeX: \alpha_s^{(n_f+1)}(\mu = m_q) = \alpha_s^{(n_f)}(\mu = m_q)

Known Limitations
Perturbative breakdown at μ < Λ_QCD ≈ 200 MeV

Scale dependence leaves residual uncertainty: ±1-3% for LHC processes

Heavy quark thresholds: simple step-function matching is an approximation

Known Failures
Cannot describe confinement (requires non-perturbative methods)

Fails for small-x physics where α_s ln(1/x) terms become large

Does not include non-perturbative power corrections

References
Gross & Wilczek (1973), Phys. Rev. Lett. 30, 1343

Politzer (1973), Phys. Rev. Lett. 30, 1346

RunDec: Chetyrkin, Kniehl, Steinhauser (2000), arXiv:hep-ph/0004189

6. TSALLIS pT DISTRIBUTION (WITH TRANSVERSE MASS)
What It Is
The Tsallis distribution is a non-extensive generalization of the Boltzmann-Gibbs exponential. In high-energy physics, it describes the transverse momentum (pT) spectrum of produced hadrons much better than a simple exponential, especially at high pT where a power-law tail is observed. The parameter n (or q = 1 + 1/n) quantifies the degree of non-extensivity: as n → ∞, the Tsallis distribution approaches an exponential.

Why Transverse Mass Matters
The original formula ignored particle mass m (ultrarelativistic approximation). For pions (m_π ≈ 0.14 GeV), this is fine for pT > 1 GeV. But for protons (m_p ≈ 0.938 GeV) and Λ⁰ (m_Λ ≈ 1.116 GeV), the difference is tens of percent at low pT (1-2 GeV/c). The correct form uses transverse mass mT = √(pT² + m²).

Corrected Formula (with mT)
Unicode: dN/dp_T ∝ p_T · (1 + m_T/(n·T))^{−n}, where m_T = √(p_T² + m²) LaTeX: \frac{dN}{dp_T} \propto p_T \cdot \left(1 + \frac{m_T}{n \cdot T}\right)^{-n}, \quad m_T = \sqrt{p_T^2 + m^2}

Normalization (Absolute Yield)
The normalized distribution requires a factor:

Unicode: (dN/dp_T)norm = (dN/dp_T) / ∫_0^∞ (dN/dp_T’) dp_T’ LaTeX: \left.\frac{dN}{dp_T}\right|{\text{norm}} = \frac{p_T \left(1 + \frac{m_T}{nT}\right)^{-n}}{\int_0^\infty p_T’ \left(1 + \frac{\sqrt{p_T’^2 + m^2}}{nT}\right)^{-n} dp_T’}

Particle-Specific Parameters (LHC pp collisions at 13 TeV)
Particle: π⁺, π⁻ — Mass: 0.140 GeV — T: 0.095 GeV — n: 8.0 — q: 1.125 — Notes: Lightest, coldest Particle: K⁺, K⁻ — Mass: 0.494 GeV — T: 0.140 GeV — n: 7.5 — q: 1.133 — Notes: Heavier, slightly hotter Particle: p, p̄ — Mass: 0.938 GeV — T: 0.180 GeV — n: 7.0 — q: 1.143 — Notes: Proton, even hotter Particle: Λ⁰ — Mass: 1.116 GeV — T: 0.200 GeV — n: 6.5 — q: 1.154 — Notes: Heavier hyperon, hottest

Physical Interpretation of Parameters
T (Tsallis temperature): Not thermodynamic temperature. Related to average kinetic energy ⟨E_kin⟩ ∝ T

n (or q): Measures deviation from equilibrium. n → ∞ (q → 1) is exponential limit. Smaller n means longer power-law tail

Implementation Example (Python)
import numpy as np import matplotlib.pyplot as plt from scipy.integrate import quad

def tsallis_pT(pT, m, n, T): mT = np.sqrt(pT2 + m2) return pT * (1 + mT/(n*T))**(-n)

m_pi = 0.140 T_pi = 0.095 n_pi = 8.0

m_p = 0.938 T_p = 0.180 n_p = 7.0

pT_bins = np.linspace(0, 5, 100) spec_pi = tsallis_pT(pT_bins, m_pi, n_pi, T_pi) spec_p = tsallis_pT(pT_bins, m_p, n_p, T_p)

norm_pi = quad(lambda pT: tsallis_pT(pT, m_pi, n_pi, T_pi), 0, 50)[0] norm_p = quad(lambda pT: tsallis_pT(pT, m_p, n_p, T_p), 0, 50)[0]

plt.plot(pT_bins, spec_pi/norm_pi, label=’π⁺ (m=0.14 GeV)’) plt.plot(pT_bins, spec_p/norm_p, label=’p (m=0.938 GeV)’) plt.xlabel(’pT (GeV/c)’) plt.ylabel(’(1/N) dN/dpT (1/GeV)’) plt.yscale(’log’) plt.legend() plt.title(’Tsallis pT Spectra at LHC (13 TeV, pp)’) plt.show()

Known Limitations
Not a first-principles prediction. Does not derive from QCD directly

Fails for A+A collisions at high pT (>8-10 GeV/c) due to jet quenching

Valid pT range: 0.1 < pT < 50 GeV/c

No particle decay contribution from resonance decays included

Known Failures
Cannot describe anisotropic flow (v₂, v₃) in heavy-ion collisions

No dependence on collision centrality or system size built in

Does not incorporate quantum statistics (Bose-Einstein, Fermi-Dirac)

References
Tsallis (1988), J. Stat. Phys. 52, 479

ALICE Collaboration (2011), Phys. Lett. B 693, 53

CMS Collaboration (2012), JHEP 08, 086

7. DGLAP EVOLUTION EQUATION
What It Is
The Dokshitzer-Gribov-Lipatov-Altarelli-Parisi (DGLAP) equations describe how Parton Distribution Functions (PDFs) change with the energy scale Q². They connect low-energy PDF measurements to high-energy LHC scales. Without DGLAP, PDFs would be arbitrary functions; with DGLAP, they are determined by a universal splitting kernel P_ij(z).

Why It’s Essential
PDFs at Q² = M_Z² (≈ 8281 GeV²) are completely different from PDFs at Q² = 1 GeV²

The gluon PDF grows rapidly at small x due to gluon splitting

DGLAP explains why the proton’s momentum is not all carried by quarks (gluons carry ~40% at high Q²)

Mathematical Form (Leading Order, Simplified)
Unicode: ∂f_i(x, μ²)/∂ln μ² = (α_s/(2π)) · Σ_j ∫_x¹ (dz/z) · P_ij(z) · f_j(x/z, μ²) LaTeX: \frac{\partial f_i(x,\mu^2)}{\partial \ln \mu^2} = \frac{\alpha_s}{2\pi} \sum_j \int_x^1 \frac{dz}{z} P_{ij}(z) f_j\left(\frac{x}{z},\mu^2\right)

Splitting Kernels P_ij(z) (Leading Order)
Splitting: q → qg — Kernel: P_qq(z) = C_F·(1+z²)/(1-z)+ — Process: Quark emits gluon Splitting: g → qq̄ — Kernel: P_qg(z) = T_R·(z² + (1-z)²) — Process: Gluon splits into quark-antiquark Splitting: g → gg — Kernel: P_gg(z) = 2C_A·[z/(1-z)+ + (1-z)/z + z(1-z)] — Process: Gluon splits into two gluons Splitting: q → gq — Kernel: P_gq(z) = C_F·(1+(1-z)²)/z — Process: Quark emits gluon (reverse)

Where: C_F = 4/3, C_A = 3, T_R = 1/2

The “+” prescription (1/(1-z)_+) regularizes the divergence at z → 1.

Momentum Sum Rule (Consistency Check)
Unicode: d/dln μ² ∫_0¹ dx · x · (Σ_q f_q(x, μ²) + f_g(x, μ²)) = 0 LaTeX: \frac{d}{d\ln \mu^2} \int_0^1 dx ; x \left( \sum_q f_q(x,\mu^2) + f_g(x,\mu^2) \right) = 0

This holds due to the identity ∫_0¹ dz z (P_qq(z) + P_gq(z)) = 0.

Known Limitations
Leading Log only: Sums α_sⁿ lnⁿ(Q²/μ₀²) but misses α_sⁿ lnⁿ(1/x) terms

LO vs NLO vs NNLO: Higher orders introduce more complex splitting kernels

Non-linear terms: At very small x, gluon recombination becomes important (gg → g)

Heavy quark thresholds: Require variable-flavor-number scheme

Known Failures
Does not describe transverse momentum dependence (TMDs require additional equations)

Cannot handle saturation effects at small x (need BK or JIMWLK)

Perturbative expansion breaks down at low Q² (< 1 GeV²)

References
Gribov & Lipatov (1972), Sov. J. Nucl. Phys. 15, 438

Altarelli & Parisi (1977), Nucl. Phys. B126, 298

Dokshitzer (1977), Sov. Phys. JETP 46, 641

APFEL: Bertone, Carrazza, Rojo (2014), arXiv:1310.1394

8. BREMSSTRAHLUNG & PAIR PRODUCTION (Electromagnetic Shower)
What It Is
When a high-energy electron (or positron) passes through matter, it can emit a photon (Bremsstrahlung). That photon, if sufficiently energetic, can convert into an electron-positron pair. This cascade—radiation → pair production → radiation → ...—is called an electromagnetic shower. It is the primary mechanism by which electrons and photons deposit energy in calorimeters (ECAL).

Why It’s Essential
ECAL simulation at LHC experiments depends entirely on these processes

Without Bremsstrahlung and pair production, electrons would penetrate the detector without interacting

The shower shape determines energy resolution and particle identification

Bremsstrahlung (Radiation Loss)
Unicode: ⟨dE/dx⟩rad = E / X₀ LaTeX: \left\langle \frac{dE}{dx} \right\rangle{\text{rad}} = \frac{E}{X_0}

Where X₀ is the radiation length (material property).

Radiation Length X₀ for common LHC detector materials:

Material: Lead (Pb) — Z: 82 — X₀: 0.56 cm — X₀: 6.37 g/cm² — Density: 11.35 g/cm³ Material: Tungsten (W) — Z: 74 — X₀: 0.35 cm — X₀: 6.76 g/cm² — Density: 19.25 g/cm³ Material: Copper (Cu) — Z: 29 — X₀: 1.43 cm — X₀: 12.86 g/cm² — Density: 8.96 g/cm³ Material: Silicon (Si) — Z: 14 — X₀: 9.36 cm — X₀: 21.82 g/cm² — Density: 2.33 g/cm³ Material: Liquid Argon — Z: 18 — X₀: 14.0 cm — X₀: 19.55 g/cm² — Density: 1.40 g/cm³

Critical Energy E_crit (where radiation loss = ionization loss):

Unicode: E_crit = (m_e c²)/(α) · (X₀/ρ) ≈ 610 MeV / (Z + 1.24) LaTeX: E_{\text{crit}} = \frac{m_e c^2}{\alpha} \cdot \frac{X_0}{\rho} \approx \frac{610\ \text{MeV}}{Z + 1.24}

Below E_crit, ionization dominates; above E_crit, radiation dominates.

Pair Production (Photon → e⁺e⁻)
The cross-section for pair production is approximately constant at high energies:

Unicode: σ_pair ≈ (7/9) · 4α·r_e² · (ln(2E_γ/(m_e c²)) − 109/42) LaTeX: \sigma_{\text{pair}} \approx \frac{7}{9} \cdot 4\alpha r_e^2 \left( \ln\frac{2E_\gamma}{m_e c^2} - \frac{109}{42} \right)

The mean free path for pair production is ~ (9/7) X₀.

Electromagnetic Shower Development (Heitler Model)
After t radiation lengths:

Number of particles: N(t) = 2^t Average energy per particle: E(t) = E₀ / 2^t Shower maximum: t_max = ln(E₀ / E_crit) / ln 2

More accurate longitudinal profile (Gaisser-Hillas function):

Unicode: dE/dt ∝ t^{(t_max-1)} · e^{-t} LaTeX: \frac{dE}{dt} \propto t^{(t_{\text{max}}-1)} e^{-t}

Implementation Example (Python)
import numpy as np import matplotlib.pyplot as plt

def em_shower(E0_GeV, X0_cm, material, n_steps=100): E_crit_GeV = 0.610 / (material[’Z’] + 1.24) t_max = np.log2(E0_GeV / E_crit_GeV) t = np.linspace(0, 2*t_max, n_steps) dEdt = t**(t_max-1) * np.exp(-t) dEdt /= np.sum(dEdt) * (t[1]-t[0]) energy_deposit = dEdt * E0_GeV return t, energy_deposit

Pb = {’Z’: 82, ‘X0’: 0.56} t, deposits = em_shower(50.0, Pb[’X0’], Pb)

plt.plot(t, deposits) plt.xlabel(’Depth (radiation lengths)’) plt.ylabel(’Energy deposit per layer (GeV)’) plt.title(’Electromagnetic Shower: 50 GeV e⁻ in Lead’) plt.show()

Known Limitations
Heitler model ignores fluctuations. Use full Monte Carlo (Geant4) for precision

No magnetic field effects

No transition effects between different materials

No Landau fluctuations

Known Failures
Cannot describe hadronic showers (HCAL) — those involve nuclear interactions

Fails at very low energy (E < 2E_crit) where shower dies out

Simple Heitler model misses detailed angular distribution (Molière radius)

References
Bethe & Heitler (1934), Proc. R. Soc. Lond. A 146, 83

Rossi (1952), “High-Energy Particles”

PDG: “Passage of particles through matter”

9. HADRONIZATION (Lund String Model)
What It Is
Hadronization is the process by which quarks and gluons (partons) produced in a high-energy collision turn into the observed hadrons (pions, kaons, protons, etc.). The Lund String Model (implemented in Pythia) is the most widely used hadronization model.

Why It’s Essential
Without hadronization, you cannot connect parton-level calculations to detector-level observations

Hadronization accounts for ~50% of the total particle multiplicity at LHC

The hadronization process is non-perturbative (α_s > 1), so it cannot be calculated from first principles

Basic Principle: Color Flux Tubes (Strings)
When a quark and antiquark move apart, the color field between them forms a tube (string) with constant energy per unit length κ ≈ 1 GeV/fm. When the string stretches enough, it breaks by producing a new qq̄ pair.

Unicode: κ ≈ 0.9 GeV/fm (string tension) LaTeX: \kappa \approx 0.9\ \text{GeV/fm}

String Fragmentation Function (Lund Symmetric Form)
Unicode: f(z) ∝ (1/z)^{a} · (1−z)^{b} · e^{-b·m_T²/(z·κ)} LaTeX: f(z) \propto \left(\frac{1}{z}\right)^a (1-z)^b \exp\left(-\frac{b m_T^2}{z \kappa}\right)

Where: a ≈ 0.68 (controls low-z behavior) b ≈ 0.98 GeV⁻² (controls high-z suppression) mT = √(p_T² + m²) (transverse mass) κ ≈ 0.9 GeV/fm (string tension)

Flavor Production (Quark-Antiquark Pair Creation)
Flavor: uū, dd̄ — Probability: 0.4 each — Suppression factor: 1.0 Flavor: ss̄ — Probability: 0.3 — Suppression factor: 0.3 Flavor: cc̄ — Probability: ~0.04 — Suppression factor: 0.04 Flavor: bb̄ — Probability: ~0.004 — Suppression factor: 0.004

Strange quarks are suppressed due to their higher mass. Charm and beauty are even more suppressed.

Implementation Example (Python)
import numpy as np from scipy.stats import rv_continuous

class FragmentationFunction(rv_continuous): def init(self, a, b, kappa, mT): self.a = a self.b = b self.kappa = kappa self.mT = mT super().init(a=0, b=1)

def _pdf(self, z):
    if z <= 0 or z >= 1:
        return 0
    return (1/z)**self.a * (1-z)**self.b * np.exp(-self.b * self.mT**2 / (z * self.kappa))
a, b, kappa = 0.68, 0.98, 0.9 mT_pion = np.sqrt(0.32 + 0.1402)

frag = FragmentationFunction(a, b, kappa, mT_pion) z_values = frag.rvs(size=1000)

Known Limitations
Not first-principles QCD. Parameters are tuned to data

Does not describe baryon production well (diquark model is less understood)

Color reconnection in events with multiple strings is modeled phenomenologically

Finite string length effects: Pythia switches to cluster model for low masses

Known Failures
Cannot describe hadronization in heavy-ion collisions (medium modifies fragmentation)

Underpredicts baryon production at high pT

Does not describe polarization effects (e.g., Λ hyperon polarization)

References
Andersson, Gustafson, Sjöstrand (1983), Z. Phys. C 20, 317

Sjöstrand (1985), Comput. Phys. Commun. 39, 347

Pythia 8 manual: Sjöstrand et al. (2015), arXiv:1410.3012

10. LANDAU-VAVILOV DISTRIBUTION (Energy Loss Fluctuations)
What It Is
The Bethe-Bloch formula gives the mean energy loss of a charged particle in matter. However, in thin layers (e.g., a silicon tracker sensor of 300 μm thickness), the actual energy loss distribution is highly asymmetric: most particles lose near the mean, but a small fraction lose much more due to rare collisions with atomic electrons (δ-rays). This distribution is described by the Landau (for thin absorbers) or Vavilov (intermediate thickness) distributions.

Why It’s Essential
Particle identification in tracking detectors uses dE/dx measurement

The Landau tail makes it difficult to separate particles of similar mass

Detector calibration and resolution modeling require the full distribution

Landau Distribution (Thin Absorber Limit)
Unicode: f_L(λ) = (1/π) ∫_0^∞ exp(−u·ln u − λ·u) · sin(πu) du LaTeX: f_L(\lambda) = \frac{1}{\pi} \int_0^\infty e^{-u \ln u - \lambda u} \sin(\pi u) , du

Where λ is the scaled energy loss variable:

Unicode: λ = (ΔE − ⟨ΔE⟩) / ξ LaTeX: \lambda = \frac{\Delta E - \langle \Delta E \rangle}{\xi}

And ξ (the Landau scale parameter) is:

Unicode: ξ = (K/2) · (z²/β²) · (Z/A) · x LaTeX: \xi = \frac{K}{2} \cdot \frac{z^2}{\beta^2} \cdot \frac{Z}{A} \cdot x

With K = 0.307075 MeV·cm²/g.

Maximum Energy Transfer ε (for Vavilov parameter)
Unicode: ε = (2 m_e c² β² γ²) / (1 + 2γ m_e/M + (m_e/M)²) LaTeX: \epsilon = \frac{2 m_e c^2 \beta^2 \gamma^2}{1 + 2\gamma m_e/M + (m_e/M)^2}

Where: m_e = electron mass (0.000511 GeV/c²) M = incident particle mass (GeV/c²) β = v/c, γ = 1/√(1-β²)

The Vavilov parameter κ = ξ / ε.

Vavilov Distribution (Intermediate Thickness)
When κ = ξ/ε < 10, the Landau approximation breaks down:

Unicode: f_V(λ; κ, β²) = (1/π) e^{λκ} ∫_0^∞ e^{-u·ln u} cos(λu + κ·h(u)) du LaTeX: f_V(\lambda; \kappa, \beta^2) = \frac{1}{\pi} e^{\lambda \kappa} \int_0^\infty e^{-u \ln u} \cos\left(\lambda u + \kappa h(u)\right) du

The Vavilov distribution approaches Landau as κ → 0 and approaches Gaussian as κ → ∞.

Implementation Example (Python)
import numpy as np import matplotlib.pyplot as plt from scipy.stats import norm

mean_loss = 3.9 * 0.03 mpv = 0.080 gaussian = norm(loc=mean_loss, scale=0.015).rvs(10000)

ROOT method (if available):

root_landau = np.array([ROOT.TMath.Landau(mpv, 0.02) for _ in range(10000)])

Known Limitations
Landau assumes thin absorber. For thick absorbers (κ > 10), distribution becomes Gaussian

No density effect correction (matters at high γ)

No magnetic field effects

Numerical difficulty: The Landau integral is oscillatory

Known Failures
Does not apply to electrons (radiative losses dominate)

Fails for very thick detectors (use Gaussian)

Fails for composite materials (use Geant4)

References
Landau (1944), J. Phys. (USSR) 8, 201

Vavilov (1957), Sov. Phys. JETP 5, 749

ROOT TMath::Landau documentation

PDG: “Passage of particles through matter”



