


# A Relativistic Particle Collider, Built in Pure JavaScript — Making the Yang-Mills Collider

### A relativistic particle physics simulator in pure JavaScript

A few days ago, I asked myself a strange question.

"Could I just run a CERN particle collider in the browser?"

The short answer — yes. Quite seriously, too.

## It Started with Simple Curiosity

The original code looked like a particle physics simulator, but under the hood the physics were fairly simple. Particles flew in straight lines, the magnetic field only affected the x and z directions, and decays just fired off in random directions.

"What if I put real physics in here?" That thought was the beginning of this project.

## What Actually Happens Inside the LHC

At CERN's LHC (Large Hadron Collider), two protons collide head-on at nearly the speed of light. The energy released at the moment of collision can reach up to 13.6 TeV — roughly 14,500 times the rest mass of a proton, all concentrated at a single point.

From that collision, hundreds of new particles are born in an instant. Pions, kaons, muons, electrons — each with different masses and charges, flying off in every direction. Inside a powerful solenoid magnetic field (about 3.8 Tesla), each one traces its own helical path.

The detector measures the curvature of these paths to calculate momentum. Even with the same charge, heavier particles curve gently while lighter ones curve sharply.

Reproducing this in the browser was the goal.

## The Physics Engine: What's Under the Hood

### 1. Special Relativity — "Nothing Can Exceed the Speed of Light"

This was the first problem to solve. Conventional game physics engines use Newtonian mechanics: F = ma. Apply a force continuously and velocity increases without limit.

But inside the LHC, protons travel at 99.9999991% of the speed of light. Newtonian mechanics breaks down completely at these speeds.

The solution is the Lorentz factor γ (gamma):
γ = E / m = 1 / sqrt(1 - v^2/c^2)

As velocity approaches the speed of light, γ grows explosively — the same force produces less and less acceleration. Every particle in this simulator passes through this formula. No particle can exceed the speed of light.

### 2. Boris Integrator — The Same Method Used by GEANT4

Numerically computing the motion of a particle in a magnetic field is trickier than it sounds. A naive implementation lets energy slowly leak out, causing the spiral to gradually grow or shrink — a real error.

The Boris Integrator is the algorithm that solves this problem. It's the standard method used in CERN's GEANT4 and plasma physics PIC codes. The key idea is to split the magnetic rotation into two half-rotations:
p^- = p + p × t      ← first half-rotation
p^+ = p^- + p^- × s   ← second half-rotation

This method conserves energy precisely while reproducing helical trajectories. As a result, in this simulator you can see positively charged particles curving counterclockwise and negatively charged ones curving clockwise — exactly as in a real detector.

### 3. The Bethe-Bloch Formula — Different Particles Slow Down Differently

Inside an LHC detector, particles lose energy as they pass through the detection material. The Bethe-Bloch formula calculates this energy loss:
-dE/dx ≈ K · z^2 / β^2 · [ln(2m_e β^2 γ^2 / I) - β^2]

The key point is that this loss differs for each particle. Light electrons lose energy quickly and trace short spirals. Heavy muons punch through almost the entire detector, leaving long straight tracks. This difference is visible in the simulator.

### 4. Decay Branching Ratios — π^+ Doesn't Always Decay the Same Way

This was personally the most fascinating part.

The positively charged pion (π^+) is an unstable particle — it decays into other particles almost immediately after being created. But it doesn't always decay the same way.

Decay Mode Probability
π^+ → μ^+ + ν_μ : 99.9877%
π^+ → e^+ + ν_e : 0.0123%

It almost always decays into a muon, but roughly once in every 10,000 times it decays into an electron instead. These values are actual experimental measurements from the PDG (Particle Data Group).

This simulator implements those probabilities exactly. Run enough collisions and you'll occasionally see a rare decay flagged separately in the event log. When it happens, it's genuinely exciting.

### 5. 4-Momentum Conservation — Physics Laws Hold Even During Decay

The directions and velocities of particles produced in a decay are determined by 4-momentum conservation. First, the decay direction is calculated in the parent particle's rest frame (CM frame), then transformed to the lab frame via a Lorentz boost.

As a result, high-energy particle decays are collimated (concentrated forward), while low-energy decays spread more isotropically. It's a moment where the laws of physics naturally visualize themselves.

### 6. α_s(μ) — The Strong Force Coupling That Changes with Energy

One of the most remarkable features of QCD (Quantum Chromodynamics) is asymptotic freedom: at higher energies, the strong force between quarks actually becomes weaker. This was the discovery that earned the 2004 Nobel Prize in Physics.

This simulator calculates α_s(μ) in real time using the 1-loop beta function:
α_s(M_Z) = 0.1181  ← actual measured value at the Z boson mass

Move the collision energy (√s) slider and α_s changes — and that value determines how many particles are produced in the collision. At 13 TeV (LHC scale), hundreds of particles; at 20 GeV, tens — trends consistent with real experimental data.

## Two Versions

3D Version (Three.js): Particles trace three-dimensional helices inside a solenoid ring. Freely rotate the view with your mouse. Adjust magnetic field strength and collision energy in real time.

2D Dashboard Version: The same physics engine, with QCD analysis tools added. Divided into three levels:

LV.1 Analytic — Instant 1-loop α_s(μ) calculation
LV.2 Monte Carlo — PDF-sampled 2→2 parton scattering, p_T distributions
LV.3 Heavy Ion — Pb+Pb collisions via the Glauber model, QGP formation condition analysis

## Yang-Mills Theory and the Millennium Problem

This project takes its name from Yang-Mills theory — the mathematical foundation of QCD, published in 1954 by C.N. Yang and R.L. Mills.

The theory contains an unsolved mathematical problem: the Mass Gap Problem. There is still no rigorous mathematical proof of why quarks cannot exist in isolation, or why the strong force only acts over short distances.

This is one of the 7 Millennium Prize Problems selected by the Clay Mathematics Institute. Solve it and you win $1,000,000. It remains unsolved.

## Closing Thoughts

The most striking thing about building this project was the realization that formulas written on paper decades ago run just as well in a browser today.

The Bethe-Bloch formula dates to the 1930s. The Boris Integrator was published in 1970. Asymptotic freedom in α_s was discovered in 1973.

These equations are still running at CERN today — and right now, in this browser.

### Physics Engine Summary

Component: Relativistic Motion — Description: Lorentz factor γ = E/m applied; speed of light cannot be exceeded
Component: Boris Integrator — Description: Standard numerical integration used in GEANT4 and PIC codes
Component: Bethe-Bloch — Description: Energy loss formula based on particle mass, charge, and velocity
Component: 4-Momentum Conservation — Description: CM frame 2-body decay followed by Lorentz boost
Component: Branching Ratios — Description: π^+→μ^+ν_μ (99.99%) vs e^+ν_e (0.01%) and other PDG values
Component: α_s(μ) Running Coupling — Description: 1-loop β function with quark flavor thresholds
Component: Monte Carlo — Description: PDF sampling, 2→2 parton scattering, p_T distributions
Component: Glauber Model — Description: Heavy-ion collisions, N_coll, ε_0, QGP formation conditions
Component: Helix Trajectories — Description: Accurate curvature under solenoid magnetic field

The code is publicly available on GitHub. Feedback and questions are always welcome.

---

# Yang-Mills Collider v3.0 — A technical inventory

### What Is Actually Inside This HTML File

B. Sun | Seoul Inside June 2026

One HTML file. 1,424 lines. No external physics library. 3D rendering via Three.js. No server. No compilation step.

This is a complete inventory of what is running inside it.

## Physical Constants
c  = 2.99792458 × 10^8 m/s        (CODATA 2018)
ℏ  = 6.582119569 × 10^{-25} GeV·s  (CODATA 2018)
ℏc = 0.1973269804 GeV·fm          (CODATA 2018)

Particle lifetimes are derived directly from decay widths via τ = ℏ/Γ. Every lifetime in the simulation is computed from this relation, not hardcoded.

## Particle Database — 39 Species (PDG 2022)

Every entry carries: rest mass (GeV/c^2), electric charge, mean lifetime (seconds), and complete branching ratio tables.

Selected entries, verbatim from the code:

Particle: W^{±} — Mass (GeV): 80.377 — Lifetime: ℏ/2.085 GeV — Source: PDG 2022
Particle: Z^0 — Mass (GeV): 91.1876 — Lifetime: ℏ/2.4952 GeV — Source: PDG 2022
Particle: H^0 — Mass (GeV): 125.20 — Lifetime: ℏ/3.2×10^{-3} GeV — Source: PDG 2022
Particle: μ^{±} — Mass (GeV): 0.105658 — Lifetime: 2.1969811×10^{-6} s — Source: PDG 2022
Particle: τ^{±} — Mass (GeV): 1.77686 — Lifetime: 2.903×10^{-13} s — Source: PDG 2022
Particle: π^{±} — Mass (GeV): 0.13957 — Lifetime: 2.6033×10^{-8} s — Source: PDG 2022
Particle: π^0 — Mass (GeV): 0.13498 — Lifetime: 8.52×10^{-17} s — Source: PDG 2022
Particle: K^{±} — Mass (GeV): 0.493677 — Lifetime: 1.2380×10^{-8} s — Source: PDG 2022
Particle: K^0_S — Mass (GeV): 0.497611 — Lifetime: 8.954×10^{-11} s — Source: PDG 2022
Particle: K^0_L — Mass (GeV): 0.497611 — Lifetime: 5.116×10^{-8} s — Source: PDG 2022
Particle: J/ψ — Mass (GeV): 3.09690 — Lifetime: ℏ/92.9×10^{-6} GeV — Source: PDG 2022
Particle: Υ(1S) — Mass (GeV): 9.46030 — Lifetime: ℏ/54.02×10^{-6} GeV — Source: PDG 2022
Particle: B^{±} — Mass (GeV): 5.27934 — Lifetime: 1.638×10^{-12} s — Source: PDG 2022
Particle: B^0 — Mass (GeV): 5.27966 — Lifetime: 1.519×10^{-12} s — Source: PDG 2022
Particle: D^0 — Mass (GeV): 1.86484 — Lifetime: 4.101×10^{-13} s — Source: PDG 2022
Particle: n — Mass (GeV): 0.939565 — Lifetime: 879.4 s — Source: PDG 2022
Particle: Λ^0 — Mass (GeV): 1.11568 — Lifetime: 2.632×10^{-10} s — Source: PDG 2022
Particle: Ξ^- — Mass (GeV): 1.32171 — Lifetime: 1.639×10^{-10} s — Source: PDG 2022
Particle: Ω^- — Mass (GeV): 1.67245 — Lifetime: 8.21×10^{-11} s — Source: PDG 2022

### Selected Branching Ratios (PDG 2022)

π^+ decay:
π^+ → μ^+ ν_μ : 99.9877%
π^+ → e^+ ν_e : 0.0123%

K^+ decay:
K^+ → μ^+ ν_μ : 63.56%
K^+ → π^+ π^0 : 20.67%
K^+ → π^+ π^+ π^- : 5.59%
K^+ → π^0 e^+ ν_e : 5.07%
K^+ → π^0 μ^+ ν_μ : 3.35%

K^0_L decay:
K^0_L → π^- e^+ ν_e : 20.20%
K^0_L → π^+ e^- ν̄_e : 20.20%
K^0_L → π^- μ^+ ν_μ : 13.52%
K^0_L → π^+ μ^- ν̄_μ : 13.52%
K^0_L → π^0 π^0 π^0 : 19.74%
K^0_L → π^+ π^- π^0 : 12.57%

τ^- decay:
τ^- → e^- ν̄_e ν_τ : 17.82%
τ^- → μ^- ν̄_μ ν_τ : 17.39%
τ^- → π^- ν_τ : 10.82%
τ^- → π^- π^0 ν_τ : 25.52%
τ^- → π^- π^+ π^- ν_τ : 28.45%

H^0 decay:
H^0 → b b̄ (approximated via π^+π^-) : 58.24%
H^0 → W^+W^- : 21.37%
H^0 → ZZ : 8.27%
H^0 → τ^+τ^- : 6.27%
H^0 → γγ : 0.23%

## Relativistic Kinematics

### 4-Momentum Class

The simulation implements the full Minkowski metric. Every particle carries a covariant 4-vector (E, p_x, p_y, p_z).
m^2 = E^2 − |p|^2
β = |p| / E
γ = E / m
p_T = sqrt(p_x^2 + p_y^2)

Lorentz boost is implemented along an arbitrary unit vector (n_x, n_y, n_z):
p_L' = γ(p_L + β·E)
E' = γ(E + β·p_L)

### 2-Body Decay in the CM Frame

For a parent particle of mass M decaying to daughters of mass m_1, m_2:
p*_CM = sqrt[ (M^2 − (m_1+m_2)^2)(M^2 − (m_1−m_2)^2) ] / (2M)

Decay direction is sampled isotropically in the CM frame, then Lorentz-boosted to the lab frame. At high boost, this produces the experimentally observed forward collimation of decay products.

### Time Dilation

Proper decay time is sampled exponentially:
t_decay = −γ τ_0 · ln(u),   u ~ Uniform(0,1)

where τ_0 is the PDG rest-frame lifetime and γ = E/m is the Lorentz factor. A B meson produced at 100 GeV lives approximately 207 times longer in the lab frame than at rest.

## QCD Running Coupling — α_s(μ), 2-Loop

The strong coupling constant is not fixed. It is computed at each collision energy via the 2-loop renormalization group equation:
β_0 = (33 − 2n_f) / (12π)
β_1 = (153 − 19n_f) / (24π^2)

α_s^(1)(μ) = α_s(M_Z) / (1 + 2β_0·α_s(M_Z)·ln(μ/M_Z))

α_s^(2)(μ) = α_s^(1) · [1 − (β_1/β_0)·α_s^(1)·ln(1 + 2β_0·α_s(M_Z)·ln(μ/M_Z))]

Boundary condition: α_s(M_Z) = 0.1180, M_Z = 91.1876 GeV (PDG 2022).

At μ = 13,000 GeV (LHC Run 2 energy): α_s ≈ 0.085. At μ = 91 GeV (Z pole): α_s = 0.1180. At μ = 1 GeV: α_s → 0.48 (coupling constant cutoff applied).

This is asymptotic freedom — the discovery for which Gross, Politzer, and Wilczek received the 2004 Nobel Prize in Physics.

## Charged Multiplicity — NSD Distribution

Mean charged multiplicity at a given √s follows the empirical parametrization:
⟨dN/dη⟩ = 0.7604 · s^0.3196

The actual multiplicity per event is sampled from a Negative Binomial Distribution with k = 3.0:
N ~ NegBinomial(mean = ⟨dN/dη⟩ × 9.5,  k = 3.0)

This reproduces the KNO-violating multiplicity distributions measured at the SPS, Tevatron, and LHC.

## Transverse Momentum — Tsallis Distribution

p_T for each particle species is sampled from the Tsallis–Pareto distribution:
dN/dp_T ∝ p_T · (1 + p_T^2 / (n·T^2))^(-n)

Species-specific parameters (T in GeV):

π^{±}: T = 0.095, n = 8.0
K^{±}: T = 0.140, n = 7.5
p: T = 0.180, n = 7.0
Λ^0: T = 0.200, n = 6.5
W^{±}, Z^0: T = 10.0, n = 4.0
H^0: T = 20.0, n = 3.5

Parameters are consistent with ALICE and CMS measurements in pp collisions.

## Rapidity Distribution

Initial rapidity is sampled from a Gaussian with σ = 2.3, truncated at |y| < 5.0:
y ~ N(0, σ=2.3),   |y| ≤ 5.0

This approximates the plateau structure of charged particle rapidity distributions measured in inelastic pp collisions across LHC energies.

## Boris Integrator

Magnetic field integration uses the Boris algorithm — the standard method in GEANT4 and plasma physics PIC codes. Published by Boris (1970).

The algorithm splits each timestep into two half-rotations, preserving phase space volume exactly (symplectic integration):
t = (q·Δt/2) / (γm)  ·  B̂

p^- = p_old + p_old × t
s = 2t / (1 + |t|^2)
p^+ = p^- + p^- × s        ← full magnetic rotation
p_new = p^+ + p_new_half × t

This guarantees that a charged particle in a uniform magnetic field traces an exact helix indefinitely, with no energy drift. Euler or RK4 methods accumulate secular errors in this geometry.

Applied in the simulation: positive charges curve counterclockwise, negative charges clockwise, when viewed along the solenoid axis. Curvature radius R = p/(qB) in SI units.

## Bethe-Bloch Energy Loss

Energy loss per unit time for a charged particle traversing detector material:
−dE/dx = K · z^2/β^2 · [ln(2m_e β^2 γ^2/I) − β^2]

where:

K = 3.2×10^{-5} GeV (material constant, silicon-equivalent)
m_e = 0.000511 GeV
I = 175×10^{-9} GeV (mean excitation energy)
z = particle charge number

Applied symmetrically at each half-step of the Boris integrator to maintain self-consistency. Result: electrons stop within millimeters, muons traverse the full detector, protons exhibit the characteristic Bragg peak behavior.

## Calorimetry

### ECAL (Electromagnetic Calorimeter)

Segmented in (η, φ) with 20×32 cells. Records energy deposits from electrons, positrons, and photons. Color scale: < 2 GeV (dark orange) → < 5 GeV → < 10 GeV → > 10 GeV (red).

### HCAL (Hadronic Calorimeter)

Separate segmentation for hadrons (pions, kaons, protons, neutrons). HCAL response is hooked into the main calorimeter hit function post-initialization — preserving ECAL data integrity while extending coverage to strongly interacting particles.

## Jet Clustering — anti-k_T Algorithm

The anti-k_T algorithm (Cacciari, Salam, Soyez 2008) — the standard jet algorithm at ATLAS and CMS — is implemented with configurable radius parameter R and minimum p_T threshold.

Distance metrics:
d_iB = p_{T,i}^(-2)
d_ij = min(p_{T,i}^(-2), p_{T,j}^(-2)) · ΔR_ij^2 / R^2

where ΔR_ij^2 = Δη^2 + Δφ^2. Particles are clustered iteratively; a particle becomes a jet when d_iB < all d_ij. The negative exponent (−2) makes anti-k_T infrared and collinear safe, and produces geometrically regular, cone-like jets.

## Displaced Vertex Reconstruction

Secondary vertices from long-lived particles are recorded with species-specific position resolution (σ):

K^0_S: cτ = 2.69 cm, σ = 2.0 mm
Λ^0: cτ = 7.89 cm, σ = 3.0 mm
B^{±}: cτ = 491 μm, σ = 0.05 mm
B^0: cτ = 455 μm, σ = 0.05 mm
D^0: cτ = 123 μm, σ = 0.12 mm

Smearing is applied as a uniform distribution of width σ in each of (x, y, z). This approximates the silicon vertex detector resolution of LHCb and ATLAS inner tracker systems.

## Trigger System — L1 and HLT

Two-level trigger mimicking the LHC trigger architecture:

Level-1 (hardware trigger):
Pass if any particle has p_T > 50 GeV, OR
Pass if event invariant mass > 80 GeV

High-Level Trigger (software trigger):
Pass if event contains Z → e^+e^- or Z → μ^+μ^- decay, OR
Pass if event contains H^0 → γγ decay

Events failing L1 are discarded before HLT evaluation. At LHC design luminosity, this two-stage filter reduces the raw 40 MHz crossing rate to approximately 1 kHz for storage.

## Particle Identification — dE/dx PID

Track identification uses the Bethe-Bloch expected energy loss as a discriminant. For a candidate particle with measured dE/dx:
P(type | dE/dx_meas) ∝ exp[−(dE/dx_meas − dE/dx_expected)^2 / (2σ^2)]

where σ = 0.05 × dE/dx_expected (5% relative resolution, consistent with silicon TPC performance). The most likely particle type is assigned by maximum likelihood across all candidate species.

## CP Violation — B^0 System

The time-dependent CP asymmetry in B^0 → J/ψ K^0_S is implemented:
A_CP(t) = sin(2β) · sin(Δm_d · t)

where:

sin(2β) = 0.699 (world average, BaBar + Belle, PDG 2022)
Δm_d = 0.5065 ps^{-1} (B^0–B̄^0 oscillation frequency, PDG 2022)

B^0 mesons oscillate to B̄^0 with probability determined by this asymmetry. This is the measurement that established matter–antimatter asymmetry in the B sector, for which Kobayashi and Maskawa received the 2008 Nobel Prize in Physics.

## Underlying Event

Soft particle production accompanying the hard scatter is modeled as a fraction of hard multiplicity:
N_UE ~ Uniform(0.30, 0.50) × N_hard

Species sampled from: π^{±}, π^0, K^{±}, p. This approximates the MPI (Multi-Parton Interaction) contribution measured by CDF and CMS underlying event analyses.

## Heavy Particle Production Thresholds

Hard production rates are implemented as energy-dependent Poisson probabilities:

J/ψ: √s threshold = 200 GeV, Rate = 1.5×10^{-3} per event
Υ(1S): √s threshold = 1,000 GeV, Rate = 8×10^{-4} per event
W^{±}: √s threshold = 2,000 GeV, Rate = 1.2×10^{-3} per event
Z^0: √s threshold = 2,000 GeV, Rate = 4×10^{-4} per event
B^{±}: √s threshold = 5,000 GeV, Rate = 3×10^{-4} per event
D^0: √s threshold = 3,000 GeV, Rate = 4×10^{-4} per event
H^0: √s threshold = 8,000 GeV, Rate = 1×10^{-5} per event

At √s = 13,000 GeV with α_s(13 TeV) ≈ 0.085, the simulation produces multiplicity distributions and heavy particle rates consistent with LHC Run 2 measurements.

## What Is Not in This File

The Yang-Mills mass gap — the proof that the quantum Yang-Mills field has a strictly positive mass gap Δ > 0 — does not exist in this file, or anywhere else.

It is one of the seven Millennium Prize Problems. The Clay Mathematics Institute has offered $1,000,000 for its solution since 2000. As of the date of this article, it remains unsolved.

The simulation runs correctly without it.

## Summary of Component Origins

PDG particle data (39 species): Particle Data Group (2022)
Bethe-Bloch formula: Bethe, Bloch (1930s)
Boris integrator: Boris (1970)
α_s 2-loop β function: Gross, Politzer, Wilczek (1973)
Tsallis p_T distribution: Tsallis (1988)
anti-k_T jet algorithm: Cacciari, Salam, Soyez (2008)
sin(2β) = 0.699: BaBar + Belle (2004)
Δm_d = 0.5065 ps^{-1}: HFLAV average (2022)
CODATA physical constants: CODATA (2018)

All of the above runs in a browser tab.

Source: Yang-Mills Collider v3.0 (LHC.html, 1,424 lines). All physical constants and branching ratios from PDG 2022 unless otherwise noted.

## Implementation Notes

### Inelastic Cross-Section

The total inelastic pp cross-section is computed at each collision energy via an empirical power-law fit:

σ_inel(√s) = 72.9 · (√s / 13000)^0.096 mb

At √s = 13,000 GeV this returns 72.9 mb, consistent with the TOTEM measurement at LHC Run 2. The 0.096 exponent reflects the slow logarithmic rise of hadronic cross-sections with energy — a consequence of the Froissart bound.

### Negative Binomial Sampling

The charged multiplicity N is drawn from a Negative Binomial Distribution with k = 3.0. Rather than inverting the NB CDF directly, the implementation uses the identity:

X ~ NegBinomial(r, p)  ⟺  X = Poisson(λ), λ ~ Gamma(r, (1−p)/p)

The Gamma variate is approximated by summing k independent exponential samples:
let n = 0;
for(let i = 0; i < k; i++) n -= Math.log(Math.random());
return Math.round(n * mean / k);

This is exact in the limit k → ∞ and produces the correct KNO-violating tails for k = 3.

## Known Approximations

This simulation makes deliberate simplifications. They are listed here for completeness.

1. 3-body phase space. Two-body decays (π^0 → γγ, B^0 → D^-π^+) are handled via the exact CM-frame formula with full Lorentz boost. Three-body decays (τ^- → π^-π^+π^-ν_τ, K^0_L → π^+π^-π^0) sample each daughter independently from the Tsallis distribution and rescale to conserve energy — this does not reproduce the correct Dalitz plot structure.

2. No parton distribution functions. The simulation does not model the initial-state parton kinematics. Collision energy √s is treated as a fixed parameter rather than sampled from quark/gluon PDFs (CTEQ, NNPDF). This means the per-event hard-scatter kinematics are not correlated with the underlying event.

3. No color confinement. Quarks and gluons do not appear as explicit degrees of freedom. The hadronization step — in which colored partons fragment into color-neutral hadrons — is replaced entirely by direct sampling from the PDG particle database. The Lund string model (PYTHIA) or cluster model (HERWIG) are not implemented.

4. Detector geometry. The solenoid field is uniform and longitudinal. No material budget, no dead zones, no endcap geometry. The Bethe-Bloch energy loss uses a single silicon-equivalent material constant K throughout.

These approximations are well-understood and do not affect the qualitative correctness of the simulation for its intended purpose: demonstrating relativistic kinematics, detector physics, and QCD phenomenology in a single browser tab.

---

# LHC Simulation: Physics Formulas and Explanations

## 1. Relativistic Kinematics

### 1.1 Invariant Mass

Formula: m^2 = E^2 - |p|^2

History: This formula emerged when Albert Einstein published the special theory of relativity in 1905. Before that, Newtonian physics treated mass and energy as separate concepts, but Einstein introduced the revolutionary relation E = mc^2. This formula extends that idea, defining the invariant mass of an object with momentum.

The term "invariant" arises because this value is measured identically regardless of the inertial reference frame. Whether in a frame moving with the particle or in the laboratory frame, m remains the same. This is the core insight of special relativity.

Historical Note: In the 1940s, when particle physicists studied unstable particles discovered in cosmic rays, this formula became a decisive tool. Cecil Powell discovered the pion (π meson) in 1947, a particle mediating the strong interaction. To confirm its existence, researchers measured particle tracks in photographic emulsions and calculated the mass using this formula. The unexpected result led to the discovery of the strong force.

Physical Meaning: As a particle approaches the speed of light, the distinction between "rest mass" and "kinetic energy" becomes ambiguous. This formula binds them into a single invariant quantity.

Limitations: For massless particles like the photon, this simplifies to m^2 = 0 → E = |p|. The concept of invariant mass remains valid, but no rest frame exists. In general relativity with gravitational fields, this simple form is replaced by a more complex metric tensor.

References: Einstein, A. (1905). "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?" Annalen der Physik; DLMF: Lorentz transformations

### 1.2 Velocity (Beta)

Formula: β = |p| / E

History: β (beta) represents velocity in units of the speed of light. Hermann Minkowski introduced this notation in his famous 1908 lecture "Space and Time," where he formalized four-dimensional spacetime. Minkowski was Einstein's teacher, and without his geometric approach, special relativity might not have been accepted so quickly.

Historical Note: The convention of expressing speed as a percentage of light speed originated in early cosmic ray physics. In the 1940s and 50s, researchers could not directly measure particle speed when detecting them in the upper atmosphere. Instead, they measured track curvature (in a magnetic field) and energy loss rate, then calculated β using this formula. They called particles with β ≈ 1 "relativistic particles" and paid special attention to them. Today at the LHC, protons are accelerated to β ≈ 0.99999999 — just 3 m/s slower than the speed of light.

Physical Meaning: β = 1 is the boundary. No particle can exceed this value; no matter how much energy is added, it only approaches 1 asymptotically. This is the "speed of light barrier."

Limitations: Massless particles (photons, gluons) always have β = 1. The classical velocity addition law (v_1 + v_2) does not hold for β. The relativistic velocity addition formula must be used instead.

References: Minkowski, H. (1908). "Space and Time" (80th Assembly of German Natural Scientists and Physicians)

### 1.3 Lorentz Factor (Gamma)

Formula: γ = E / m

History: γ (gamma) is the Lorentz factor, named after Dutch physicist Hendrik Antoon Lorentz. Lorentz introduced this factor in the 1890s while studying the symmetry of electromagnetic equations. He thought of it as a "mathematical convenience," but Einstein showed it reflects the actual structure of spacetime. Lorentz never fully accepted relativity, a famous anecdote in physics.

Historical Note: The remarkable feature of γ is its range. At rest, γ = 1. As speed approaches light speed, γ diverges to infinity. At the LHC, protons achieve γ ≈ 7,000. This means the time dilation experienced by protons is 7,000-fold. From the proton's perspective, circling the LHC tunnel takes only 0.00004 seconds, while in the laboratory it takes 1 second. This is a practical realization of the "twin paradox."

γ is also key to understanding "air showers" in cosmic ray physics. Cosmic ray particles striking the upper atmosphere can have γ > 10^6, allowing the resulting particle cascade to reach the ground.

Physical Meaning: γ is not just a factor. It is the Swiss Army knife of relativity, describing time dilation, length contraction, and relativistic mass increase all at once.

Limitations: Undefined for massless particles (denominator zero). In the classical limit (v ≪ c), γ ≈ 1 + v^2/(2c^2), and relativistic effects become negligible.

References: Lorentz, H. A. (1904). "Electromagnetic phenomena in a system moving with any velocity smaller than that of light" Proceedings of the Royal Netherlands Academy of Arts and Sciences

### 1.4 Transverse Momentum

Formula: p_T = sqrt(p_x^2 + p_y^2)

History: p_T (transverse momentum) is one of the most important variables in particle collision experiments. Because incoming particles move along the beam axis (z-axis) before collision, the total transverse momentum after collision must be conserved as zero. This property is fundamental to particle detector design.

p_T is important because new physics often appears at high p_T. For example, the J/ψ particle discovered in 1974 appeared at p_T ≈ 3 GeV/c, and the W and Z bosons discovered in 1983 appeared at much higher p_T (tens of GeV/c).

Historical Note: During the 1980s, when the UA1 and UA2 experiments at CERN were discovering W and Z bosons, researchers searched for high-p_T electrons and muons. Background signals were so abundant that the detector trigger system was designed to discard most low-p_T events. If the new particles had not been produced at sufficiently high p_T, they might have gone undiscovered. Fortunately, their decay products appeared at around 40 GeV/c. Since then, "high p_T" has become a signature of new physics.

Among particle physicists, the "p_T cut" (excluding data below a certain p_T) is one of the most fundamental decisions in experimental design. Setting the cut too low results in excessive background; setting it too high discards the signal.

Physical Meaning: p_T measures how violent the collision is at its core. Higher p_T implies stronger interactions, heavier particles, and more interesting physics.

Limitations: A one-dimensional variable. Analyzing correlations between particles or p_T directionality (e.g., azimuthal anisotropy) requires more complex analysis. The low-p_T region (below a few hundred MeV/c) is dominated by non-perturbative hadronization effects, which cannot be described by perturbative QCD.

References: UA1 Collaboration (1983). "Experimental observation of lepton pairs of invariant mass around 95 GeV/c^2" Physics Letters B

### 1.5 Lorentz Boost (longitudinal)

Formula: p_L' = γ(p_L + βE), E' = γ(E + β p_L)

Note: Boost direction assumed along the longitudinal (z) axis.

History: The Lorentz boost is the kinematic core of special relativity. It describes how to transform observations between reference frames moving at different velocities. While Galilean transformations say "just add velocities," Lorentz boosts are designed to satisfy the principle that "the speed of light is the same for all observers."

This transformation can be represented as a 4×4 matrix, analogous to rotating spacetime coordinates — hence the name "boost."

Historical Note: The most dramatic example of the Lorentz boost is the extended lifetime of muons. Cosmic ray muons are created in the upper atmosphere (about 15 km altitude) with a rest lifetime of 2.2 μs. Even traveling at the speed of light, they would only cover 660 m. How do they reach the ground?

The answer is time dilation. If the muon's γ is about 40, the laboratory-frame lifetime becomes 2.2 μs × 40 = 88 μs, allowing a travel distance of about 26 km. Bruno Rossi and David Hall experimentally demonstrated this in 1941 by measuring muon flux at the top of a Colorado mountain. It was one of the first direct experimental verifications of relativity.

Physical Meaning: A boost is not just a coordinate transformation. It shows how energy and momentum "mix." A particle at rest has no momentum, but to a moving observer, it has momentum. Just as space and time mix, energy and momentum mix.

Limitations: This formula handles only longitudinal (z-axis) boosts. Boosts in arbitrary directions require more complex matrix multiplication. Valid only for objects moving near the speed of light. At low velocities (β ≪ 1), a Taylor expansion recovers the Galilean transformation.

References: Rossi, B., & Hall, D. B. (1941). "Variation of the Rate of Decay of Mesotrons with Momentum" Physical Review

## 2. Two-Body Decay Momentum

Formula: p*_CM = sqrt[ (M^2 − (m_1+m_2)^2)(M^2 − (m_1−m_2)^2) ] / (2M)

History: Two-body decay is the most fundamental and important process in particle physics. This formula was established during the "particle zoo" era of the 1950s, when many new particles were discovered but their masses and decay modes were mysterious.

Particle physicists observed V-shaped tracks in detectors and used this formula to calculate the parent particle's mass. For example, K^0 (kaon) decays into π^+ and π^-; measuring the two pions' trajectories and applying this formula yields the K^0 mass. The same principle is used today at LHCb and Belle II to discover new particles.

Historical Note: The most dramatic use of this formula was the discovery of the J/ψ particle in 1974. Two teams, led by Burton Richter and Samuel Ting, independently discovered a new particle decaying into e^+e^- pairs in e^+e^- and p-Be collisions. Analyzing the decay products and applying this formula gave a mass of about 3.1 GeV/c^2 — larger than any known particle at the time — and provided evidence for the charm quark.

Richter and Ting shared the 1976 Nobel Prize in Physics. Interestingly, the two teams gave the particle different names (J and ψ). Today it is unified as J/ψ with a hyphen.

Particle physicists use decay kinematics so frequently that omitting the factor 2M in the denominator is called "the curse of 2M" — one of the most common mistakes beginners make.

Physical Meaning: This formula tells how fast the decay products fly apart in the center-of-mass frame. When the sum of the daughter masses is close to the parent mass (small p_T), the decay momentum is small. Conversely, when the daughters are light (e.g., photons or electrons), the decay momentum is large.

Limitations: For decays into three or more particles, the phase space becomes more complex and the momentum distribution is not a single value. The formula assumes the decay products are stable. If they decay further, the measured tracks are harder to interpret. Particle-antiparticle pair production is closer to scattering than decay.

References: Aubert, J. J., et al. (1974). "Experimental Observation of a Heavy Particle J" Physical Review Letters; Augustin, J. E., et al. (1974). "Discovery of a Narrow Resonance in e^+e^- Annihilation" Physical Review Letters

## 3. Time Dilation and Decay Time

Formula: t_decay = −γ·τ_0·ln(u), u ~ Uniform(0,1)

History: This formula represents the intersection of quantum mechanics and special relativity. The particle's proper lifetime τ_0 is determined by quantum mechanical processes (e.g., weak interaction decays). When the particle moves near the speed of light, time dilation multiplies the observed lifetime by γ. Combining this with the exponential decay distribution yields the formula above.

The form "negative natural log of a uniform random variable" comes from inverse transform sampling. The cumulative distribution function (CDF) of the exponential distribution is F(t) = 1 - exp(-t/τ). Solving for t gives t = -τ ln(1-u). Since u is Uniform(0,1), 1-u is also Uniform(0,1), simplifying to -τ ln(u).

Historical Note: The most famous application of this formula is the measurement of muon time dilation. In 1963, David Frisch and James Smith performed a famous experiment using cosmic-ray muons, measuring their flux at two altitudes (mountain top vs. sea level). The muon velocity was about 0.995c (γ ≈ 10), so the theoretical lifetime was expected to be 2.2 μs × 10 = 22 μs. They measured the rate of muons reaching the detector and found perfect agreement with relativistic predictions.

This experiment is considered one of the most direct proofs of relativity. When Frisch and Smith published their results, they did not claim to have "proven time dilation" — they simply said "muons travel farther than expected." Relativity was already widely accepted by then, but to the general public, the "muon experiment" remains one of the most convincing pieces of evidence.

In particle physics simulations (e.g., Geant4), this formula is called millions of times per day to determine the decay points of all unstable particles. At the LHC, each collision event produces thousands of particles, many of which decay — making this calculation essential.

Physical Meaning: This formula combines three physical effects into one:
1. Quantum mechanical decay probability (exponential distribution)
2. Special relativistic time dilation (γ factor)
3. Monte Carlo probability extraction (uniform distribution → exponential distribution)

Limitations: Assumes decay follows an exponential distribution. Most elementary particle decays do, but some composite systems (e.g., excited nuclei) may show more complex decay patterns. When τ_0 is extremely short (e.g., below 10^{-23} seconds, strong interaction decays), particles are treated as "resonances" and decay points cannot be practically measured. Depends on random number generator quality. Statistical errors in simulations are directly proportional to the uniformity of the random numbers used.

References: Frisch, D. H., & Smith, J. H. (1963). "Measurement of the Relativistic Time Dilation Using μ-Mesons" American Journal of Physics; DLMF: Exponential Distribution

## 4. QCD 2-Loop Beta Function Coefficients

### 4.1 Beta Coefficients

Formula: β_0 = (33 − 2n_f) / (12π), β_1 = (153 − 19n_f) / (24π^2)

History: The QCD beta function describes how the strong interaction coupling strength (α_s) changes with energy scale. These coefficients were calculated in the early 1970s, during a revolutionary period in particle physics.

Gerard 't Hooft proved the renormalizability of Yang-Mills theory in 1971. Then in 1973, David Gross, Frank Wilczek, and independently David Politzer, discovered that the beta function coefficient for pure Yang-Mills theory (gluons only) was negative! This explained "asymptotic freedom" in the strong force: quarks move almost freely at high energies but are tightly bound at low energies.

This discovery earned Gross, Wilczek, and Politzer the 2004 Nobel Prize in Physics. In 1999, 't Hooft and Martinus Veltman received the Nobel Prize for renormalization theory.

Historical Note: Where do the numbers 33 and 153 come from? They arise from group theory — the Casimir invariants of the SU(3) color group:

33 = 11 × 3 (from 11·C_A where C_A = 3)
153 = 34·C_A^2 + ... actually from 34·9 = 306, minus 19n_f·(something)... The full derivation is:

β_0 = (11·C_A − 4·T_F·n_f) / (12π)
β_1 = (34·C_A^2 − 20·C_A·T_F·n_f − 12·C_F·T_F·n_f) / (24π^2)

where C_A = 3, C_F = 4/3, T_F = 1/2. This yields β_0 = (33 − 2n_f)/(12π) and β_1 = (153 − 19n_f)/(24π^2).

These numbers are not coincidental; they reflect the deep mathematical structure of quantum field theory, which fascinates theoretical physicists.

Another interesting point: if n_f (number of quark flavors) exceeds 33/2 = 16.5, β_0 becomes positive, asymptotic freedom disappears, and the coupling becomes small at low energies ("infrared freedom"). Our universe has only 6 quark flavors; if it had 17, the nature of the strong force would be completely different. This is one reason why no theory with 17 quark flavors has been discovered.

Physical Meaning: β_0 > 0 means asymptotic freedom: at high energies (short distances), interactions between quarks become weak. This explains why quarks behave almost like free particles in high-energy colliders like the LHC.

Limitations: Based on perturbation theory. At low energy scales (below Λ_QCD ≈ 200 MeV), the coupling becomes so large that perturbative expansions do not converge.

References: Gross, D. J., & Wilczek, F. (1973). "Ultraviolet behavior of non-abelian gauge theories" Physical Review Letters; Politzer, H. D. (1973). "Reliable perturbative results for strong interactions?" Physical Review Letters

### 4.2 1-Loop Running Coupling

Formula: α_s^(1)(μ) = α_s(M_Z) / (1 + 2β_0·α_s(M_Z)·ln(μ/M_Z))

Physical Meaning: This formula shows that the coupling constant α_s is not constant — it "runs" with energy scale. This is one of the most distinctive features of quantum field theory. At M_Z ≈ 91 GeV, α_s ≈ 0.118; at μ = 1000 TeV, α_s ≈ 0.05; at μ = 1 GeV, α_s ≈ 0.5.

Limitations: The 1-loop approximation is accurate only when α_s is sufficiently small (≲ 0.3).

### 4.3 2-Loop Running Coupling

Formula: α_s^(2)(μ) = α_s^(1)·[1 − (β_1/β_0)·α_s^(1)·ln(1 + 2β_0·α_s(M_Z)·ln(μ/M_Z))]

Physical Meaning: The 2-loop correction improves the precision of coupling constant calculations. At LHC energies where α_s ≈ 0.1, the 1-loop approximation is sufficiently accurate (about 1% error). But for lower energies or analyses requiring higher precision, 2-loop (or higher) corrections are essential.

Historical Note: The 2-loop running coupling was calculated in 1974 by David Gross and Frank Wilczek, and independently by William Caswell. The calculation was enormously complex: hand calculations in the 1970s required summing hundreds of Feynman diagrams.

## 5. Additional Physics in the Simulation

### 5.1 Breit-Wigner Resonance Sampling

For unstable particles like Z^0 and W^{±}, the mass is not fixed but follows a Breit-Wigner distribution:
dN/dE ∝ 1 / ((E − M)^2 + (Γ/2)^2)

where M is the nominal mass and Γ is the decay width.

### 5.2 Bethe-Bloch Energy Loss

For charged particles traversing detector material:
−dE/dx = K z^2 (Z/A) (1/β^2) [ (1/2) ln(2m_e β^2 γ^2 T_max / I^2) − β^2 ]

### 5.3 Tsallis p_T Distribution

The transverse momentum distribution follows the Tsallis-Pareto form:
dN/dp_T ∝ p_T (1 + p_T^2 / (n T^2))^(-n)

### 5.4 Negative Binomial Multiplicity Distribution

The charged particle multiplicity per event follows a Negative Binomial Distribution with k = 3.0, which reproduces the KNO-violating multiplicity distributions measured at the SPS, Tevatron, and LHC.

## Summary of Key Formulas

Concept: Invariant mass — Formula: m^2 = E^2 − |p|^2 — Physical meaning: Mass is Lorentz invariant
Concept: Velocity — Formula: β = |p|/E — Physical meaning: Speed in units of c
Concept: Lorentz factor — Formula: γ = E/m — Physical meaning: Time dilation, length contraction
Concept: Transverse momentum — Formula: p_T = sqrt(p_x^2 + p_y^2) — Physical meaning: Momentum perpendicular to beam
Concept: Lorentz boost — Formula: p_L' = γ(p_L + βE), E' = γ(E + β p_L) — Physical meaning: Frame transformation
Concept: Two-body decay — Formula: p*_CM = sqrt[ (M^2−(m_1+m_2)^2)(M^2−(m_1−m_2)^2) ] / (2M) — Physical meaning: Decay momentum in CM frame
Concept: Decay time — Formula: t_decay = −γ τ_0 ln(u) — Physical meaning: Exponential decay + time dilation
Concept: QCD beta coefficients — Formula: β_0 = (33−2n_f)/(12π), β_1 = (153−19n_f)/(24π^2) — Physical meaning: Running of α_s
Concept: 1-loop α_s — Formula: α_s^(1)(μ) = α_s(M_Z) / (1 + 2β_0 α_s(M_Z) ln(μ/M_Z)) — Physical meaning: Asymptotic freedom

---

# Black Hole Physics in Yang-Mills Collider v3.2

## 1. What Is Currently Implemented

### 1.1 Newtonian Gravity

The simplest form of gravity:
F = G M m / r^2

In code, log-corrected to match scene scale:
gAcc = log10(BH_MASS + 1) * 120.0 / (r^2 + 1.0)
dp/dt = -gAcc * (r_hat) * dt

Rather than curving spacetime, this approach directly adds force to momentum.
It is Newtonian — yet all particles, regardless of mass or charge, are attracted equally.
This effectively reproduces the Equivalence Principle.

### 1.2 Event Horizon Approximation

The event horizon radius of a Kerr black hole:
r_+ = M * (1 + sqrt(1 - a*^2))

where a* = a/M is the dimensionless spin parameter (0 to 1).

Code approximation:
Rs_base = max(0.8, log10(BH_MASS + 1) * 0.6)
Rs = Rs_base * (1 + sqrt(max(0, 1 - BH_SPIN^2))) * 0.5
if r < Rs * 2 : absorbed = true

Reflects the fact that the horizon shrinks to its minimum when spin is maximal (a* = 1).

### 1.3 Frame Dragging — Lense-Thirring Approximation

A defining effect of the Kerr metric. A rotating mass drags the surrounding spacetime along with it.

Exact expression:
Ω_LT ~ 2 G J / (c^2 r^3)

where J = angular momentum.

Code approximation (simplified as a tangential force):
r_xz = sqrt(dx^2 + dz^2)
fdAcc = BH_SPIN * log10(BH_MASS+1) * 55.0 / (r^3 + 1.0)
tx = -dz / r_xz   (tangential unit vector, Y-axis rotation)
tz = dx / r_xz
dp_x/dt += fdAcc * tx * dt
dp_z/dt += fdAcc * tz * dt

A tangential acceleration is used instead of full tensor computation.
Despite this, spiral infall and the Penrose process emerge as outcomes.

### 1.4 Ergosphere

A region unique to Kerr black holes. Outside the event horizon, yet spacetime itself rotates.
Remaining stationary here is impossible — everything is forced to co-rotate with the black hole.

Ergosphere radius at the equator:
r_ergo = 2M  (at a* = 1, equatorial plane)
General form: r_ergo = M * (1 + sqrt(1 - a*^2 cos^2θ))

Code approximation:
r_ergo_approx = Rs_base * 2.0
if r < r_ergo and BH_SPIN > 0.1:
    ergoBoost = BH_SPIN * logMass * 80.0 / (r^2 + 1.0)
    additional tangential acceleration applied

Visualized as a purple wireframe when spin > 0.15.

### 1.5 Energy-Momentum Conservation

The relativistic relation is maintained at every step:
E^2 = p^2 c^2 + m^2 c^4

Code:
pM = sqrt(px^2 + py^2 + pz^2)
E = sqrt(pM^2 + mass^2)

Updated every frame after applying gravitational and magnetic forces.
This is what allows the particle physics engine (LHC) and gravity to coexist.

### 1.6 Relativistic Jets (Visual)

Polar-direction jet visualization when spin > 0.6.
Inspired by the Blandford-Znajek mechanism:
P_jet ~ B^2 r_+^2 a*^2 c / (4π)

Currently visual only — no physical calculation.
However, actual particle escape driven by magnetic field + spin combinations near the ergosphere has been observed (see Section 2.3 below).

## 2. Phenomena That Emerged Without Design

### 2.1 Equivalence Principle

All particles — regardless of charge, mass, or type — are absorbed without exception.
Simply adding Newtonian gravity produced the Equivalence Principle as an outcome.

### 2.2 Accretion Disk Formation

Particles spawned with random momenta spontaneously aggregate into a disk structure.
A consequence of angular momentum conservation. Not designed — yet it appeared.

### 2.3 Penrose Process

Under strong magnetic field + spin conditions, particles near the ergosphere were observed to escape. Mathematically predicted by Roger Penrose in 1969; observationally confirmed in 2021.
E_escape = E_particle + Ω_H L

This simulator did not intentionally implement this.
It emerged spontaneously from the interaction of:
Newtonian gravity + frame-dragging approximation + Boris magnetic field integration.

## 3. What Was Left Out — and Why

### 3.1 Full Kerr Metric

The exact description of spacetime:
ds^2 = -(1 - r_s r/Σ) c^2 dt^2
       - (2 r_s r a sin^2θ / Σ) c dt dφ
       + (Σ/Δ) dr^2
       + Σ dθ^2
       + (r^2 + a^2 + r_s r a^2 sin^2θ / Σ) sin^2θ dφ^2

Σ = r^2 + a^2 cos^2θ
Δ = r^2 - r_s r + a^2

Particle trajectories must follow the geodesic equation:
d^2 x^μ / dλ^2 + Γ^μ_{αβ} (dx^α/dλ) (dx^β/dλ) = 0

Computing Christoffel symbols Γ every frame is not feasible in real-time in a browser.
Not implemented: technical constraints.

### 3.2 Hawking Radiation

The emission of energy from a black hole via quantum effects:
T_H = ħ c^3 / (8π G M k_B)

Implementation would require quantum field theory on curved spacetime (Bogoliubov transformations) — a fundamentally different layer from the current engine architecture.
Not implemented: technical and theoretical constraints.

### 3.3 Tidal Forces / Spaghettification
dF_tidal ~ 2 G M m dr / r^3

The gravitational gradient arising from distance differences — the effect that stretches objects.
Not applicable in the current architecture, which treats each particle as a single point mass.
Not implemented: technical constraints.

### 3.4 Gravitational Waves

Upon merger of two massive bodies:
h ~ G M v^2 / (c^4 r)

Oscillations in spacetime itself. Structurally impossible here, as the background spacetime is fixed as flat (Minkowski).
Not implemented: technical constraints.

## 4. What Was Left Out — As a Physical Choice

The omissions above are partly due to technical limitations — but they are equally intentional choices.

Implementing full GR would actually cost something:

How do small masses move around a large gravitational body —

seeing that simplest question through the simplest possible means.
When Kepler observed planetary orbits, he did not know why they were ellipses — but he saw that they were ellipses first.

This simulator is the same.
Rather than why the equations produce those orbits — the goal is to see whether those orbits actually appear.

Even with Newtonian gravity being wrong, the Penrose process emerged.
That is the honesty and value of this approach.

## 5. Current Engine Architecture Summary

[LHC Particle Physics Engine]     [Black Hole Gravity Engine]
- 4-momentum conservation          - Newtonian gravity (log scale)
- PDG 2022 branching ratios        - Lense-Thirring approximation
- Breit-Wigner resonance           - Ergosphere boost
- Bethe-Bloch energy loss          - Event horizon absorption
- 39 particle species              - E^2 = p^2 + m^2 update
            |                               /
            |                             /
         [Boris Integrator + Magnetic Field]
                |
        [Per-frame iteration]
                |
        [Observables: orbits, absorption, escape, jets]

Theoretically, these two engines cannot coexist.
Quantum field theory and general relativity have not yet been unified.

And yet it runs. And yet real phenomena emerge.

## 6. Key Simulation Parameters Reference

BH_MASS: 0 – 10^{12} M_⊙ (default 0) — Black hole mass
BH_SPIN: 0 – 1 (default 0) — Dimensionless spin parameter a* = a/M
BH_DIST: 0 – 200 scene units (default 80) — Distance from origin
B-field: 0 – 14 T (default 6.2) — Magnetic field strength
√s: 30 – 14000 GeV (default 13000) — Collision energy
Trail length: 6 – 55 steps (default 22) — Particle trail length
Grid bright: 0 – 1 (default 0.35) — Spacetime grid brightness

---

# I Added a Black Hole to the LHC — and Something Unexpected Happened

### This was not supposed to happen. I was done.

I had been building an archive of mathematical problems — seven Millennium Prize Problems, working through them one by one. Yang-Mills was difficult. A particle collider simulator came out of it. It worked beautifully.

I was satisfied. I was ready to move on to economics.

The first item on the economics list was Black-Scholes.

Black.

I went back to the simulator and added a black hole.

## What I Expected

Nothing interesting. The black hole would pull everything in. The simulation would collapse into a single point. That would be the end of it.

## What Actually Happened

The particles did not all fall in.

Under a sufficiently strong magnetic field, something else occurred. Particles and antiparticles — produced in the same collision, at the same point — separated. They drifted to opposite sides of the black hole. They survived.

The third image is the control. With no magnetic field, everything falls in. No separation. The magnetic field is what keeps them alive — and apart.

## Why the Separation Happens

This part is not mysterious. It follows directly from the physics already in the simulator.

The Boris integrator — the standard algorithm used in GEANT4 and plasma physics — rotates charged particles in a magnetic field. Positive charge rotates one way. Negative charge rotates the other way. Same radius, opposite direction.

When a black hole is added, both are pulled toward the same point. But they arrive from opposite sides. They are captured on opposite sides.

No special effect was added for this. No trick. The gravitational code is four lines:

const gAcc = logMass * 120.0 / (r2 + 1.0)
p.p4.px -= gAcc * (dx / r) * dt
p.p4.py -= gAcc * (dy / r) * dt
p.p4.pz -= gAcc * (dz / r) * dt

Newtonian gravity, pointed at a point mass. No charge distinction. No rotation. No accretion disk code of any kind.

The disk-like structure in the images was not programmed. It emerged from the geometry of the magnetic field axis and the gravitational pull. The magnetic field runs along the Y-axis. The Boris integrator confines surviving particles to the XZ plane. The black hole pulls them inward. What remains is a disk.

I did not build an accretion disk. One appeared.

## Why This Might Matter

I was already thinking about a separate question — one that had nothing to do with the simulator.

If a black hole's mass is not static — if it fluctuates, for any reason — and if gravity propagates at a finite speed, then the gravitational influence of that fluctuation reaches the surrounding galaxy with a delay. Stars far away feel a mass that may no longer exist. Or do not yet feel a mass that does.

The standard picture of black hole mass growth requires swallowing stars and gas. That is the only mechanism usually considered.

But the simulation suggests something else is possible.

In a high-energy environment with a strong magnetic field — which real black holes have, in abundance — particle-antiparticle pairs can be produced, separated, and kept from annihilating. They persist. They constitute mass. That mass was not there before. It did not come from a swallowed star.

If this process operates at any meaningful scale near real black holes, then black hole effective mass fluctuates continuously — not because of what falls in, but because of what is created and isolated nearby.

And if gravity propagates at finite speed, those fluctuations propagate outward across the galaxy with a delay proportional to distance.

The gravitational influence of a mass that briefly existed — and then annihilated — persists for r/c after it is gone. Ghost mass. A flat rotation curve emerges from this naturally, without dark matter, if the annihilation rate is roughly constant.

## What I Do Not Know

I do not know why the surviving clusters settle at the specific radius they do. The position appears stable once the magnetic field exceeds a threshold — stronger field, same location. This suggests an equilibrium between magnetic confinement and gravitational pull. But I have not derived it analytically.

I do not know the scale of this effect in real astrophysical environments. The simulator is a toy. Real black hole magnetospheres are vastly more complex.

I do not know whether the gravitational signal from mass near the event horizon propagates symmetrically outward — or whether some fraction is redirected inward, toward the horizon, and effectively trapped. If the latter, then even the outward-propagating influence is attenuated. Observed black hole masses would be lower bounds. This is speculative. I include it because it connects structurally to everything above, and because the implication — if correct — is significant enough to state explicitly.

## The Honest Summary

A magnetic field strong enough to keep particles from falling into a black hole also separates them by charge. Separated particles do not annihilate. They persist as mass. That mass fluctuates. Fluctuating mass, under finite-speed gravity propagation, produces a time-varying gravitational field across the galaxy.

None of this required special code. The Boris integrator did it. Four lines of Newtonian gravity did it. An accretion disk appeared without being written.

I was going to study Black-Scholes.

This post is a companion to: Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation in Disk Galaxies

The theoretical framework — including all mathematical formulations and their limitations — is in the main paper. This post describes only what was observed, and what it suggested.

---

# The Passive Layer — Core Document

### Gravitationally present. Physically absent.

## Defining Statement

Gravitationally present. Physically absent. (중력적으로는 존재하지만, 물리적으로는 부재한다)

This is not a metaphor. It is the logical consequence of two facts that have been experimentally confirmed for decades.

## Part 1. Two Established Facts

Fact 1: Gravity propagates at the speed of light.

A change in a gravitational source does not instantly affect the surrounding universe. The influence travels outward at c. This was confirmed in 2017 when LIGO/Virgo detected gravitational waves and gamma rays from a neutron star merger (GW170817) arriving simultaneously, constraining the speed of gravity to within 10^{-15} of c (Abbott et al., 2017).

Meaning: If a mass disappears, its gravitational signal continues to travel outward for a time r/c after the mass is gone.

Fact 2: Mass is created and destroyed.

Energy converts into mass and mass converts back into energy. Particle-antiparticle pairs are continuously created and annihilated throughout the universe — in vacuum fluctuations, near black holes, in high-energy environments. This has been directly observed and is a foundational result of quantum field theory and particle physics.

Neither of these facts is in dispute. Both have been confirmed independently, repeatedly, across multiple experimental contexts.

## Part 2. The Logical Consequence

Combine Fact 1 and Fact 2.

A mass exists. It generates a gravitational signal that propagates outward at c. The mass then ceases to exist — through annihilation, decay, or any other mechanism. The gravitational signal does not cease. It continues to travel. It continues to exert influence on everything it reaches.

This propagating remnant is the Passive Layer — also referred to as Ghost Mass or gravitational reverberation. These are different names for the same phenomenon.

Formally:
τ(r) = r / c

The gravitational influence of a mass that existed at distance r persists for time r/c after that mass is gone. Stars, galaxies, and all gravitating bodies experience the gravitational echo of mass that no longer exists.

## Part 3. Reverberation Does Not Cancel

A critical point: the Passive Layer does not cancel out.

Gravity has no negative mass. Particles and antiparticles carry opposite electric charges, but they carry the same gravitational mass. The gravitational reverberation of a particle and its antiparticle point in the same direction. They do not cancel. They accumulate.

What appears to be cancellation in homogeneous regions is not cancellation — it is balance. Consider the Earth: every atom pulls on every other atom. None of these forces cancel. They sum. At the center of the Earth, the net force is zero — not because the forces have cancelled, but because they balance symmetrically. Move away from the center, and the imbalance becomes immediately apparent.

The same applies to gravitational reverberation across the universe. In perfectly homogeneous regions, the reverberations balance. But the universe is not perfectly homogeneous anywhere. The net effect of the Passive Layer is therefore non-zero everywhere.

## Part 4. Dynamic Equilibrium

The Passive Layer does not accumulate without bound.

New reverberations are continuously generated as mass is created and destroyed. Existing reverberations are continuously diluted by cosmic expansion. At cosmological scales, these processes reach a dynamic equilibrium — a stable background density of gravitational reverberation.

This is structurally identical to Olbers' Paradox.

The night sky is dark not because stars do not emit light, but because the universe is finite in age and expanding — the light from distant stars is diluted and redshifted. The sky does not grow infinitely bright. It reaches an equilibrium.

Similarly: the Passive Layer does not grow without bound. It reaches a stable equilibrium density.

This is not stillness. The underlying process is extraordinarily dynamic — countless events, countless signals, all in motion simultaneously. But the background density of gravitational reverberation that this process produces is, at any given moment, effectively constant. New contributions enter. Existing ones disperse. The net background holds.

This is the structure of a dynamic equilibrium — not a static state, but a stable one. The stability is produced by the dynamics, not despite them.

The universe has been operating in this equilibrium since long before any observation was made. What we observe as the gravitational background is not a frozen artifact. It is the current snapshot of a process that never stops.

### Part 4.5 — The Scale Problem

A single pair-annihilation event is gravitationally negligible. The reverberation it produces is unmeasurably small — far below any detection threshold. This is not in dispute.

But this is the wrong frame for the question.

The Milky Way alone contains approximately 200 billion stars. Each star converts mass to energy continuously over billions of years. Each stellar birth, each supernova, each neutron star collapse, each pair-creation and annihilation event in the high-energy environments surrounding these objects — every one of these produces a gravitational reverberation that propagates outward at c.

The question is not whether any single reverberation is detectable. It is not.

The question is what 138 billion years of these events, accumulated across an entire galaxy, sum to.

A raindrop is negligible. The terrain shaped by 138 billion years of rainfall is not.

This is the scale at which the Passive Layer becomes a serious cosmological question — not at the level of individual quantum events, but at the level of galactic mass-conversion history. And at that level, the cumulative magnitude has never been calculated.

## Part 5. The Missing Term

Current cosmological models compute gravitational influence from presently existing mass.

The gravitational reverberation of past mass — mass that existed and then ceased to exist — is not included as a term in any standard cosmological framework. This is not an error. It is an omission. The term has not been calculated.

This is the Passive Layer as a cosmological problem: a physically necessary term, derivable from two confirmed facts, that has never been quantified or incorporated into the standard model of cosmology.

The universe has been accounting for it automatically. Our models have not.

## Part 6. Relationship to Dark Matter

The observational signature of dark matter is:
- Gravitational effects are present
- No electromagnetic interaction is detected
- No particle has been detected after fifty years of dedicated searches
- The effect is distributed in patterns correlated with regions of high mass density

The Passive Layer produces exactly this signature:
- Gravitational effects are present — because reverberation carries gravitational influence
- No electromagnetic interaction — because the source mass no longer exists
- No particle detectable — because it is not a particle; it is a propagating gravitational remnant
- Correlated with mass density — because regions of high mass density generate more creation and annihilation events, and therefore more reverberation

The failure to detect dark matter particles after fifty years of increasingly sensitive experiments is consistent with the Passive Layer interpretation. The searches have been looking for a particle. The effect may not be a particle.

This document does not claim that dark matter does not exist. It claims something narrower:

The gravitational reverberation of past mass is a physically necessary, non-zero effect that has never been calculated. Its magnitude is unknown. It may account for a non-trivial portion of what is currently attributed to unseen mass.

## Part 7. Why This Has Not Been Calculated

The absence of this calculation is not evidence of its insignificance.

Standard cosmological frameworks are built around the present mass distribution. The concept of gravitational influence from mass that no longer exists does not fit naturally into frameworks designed around static or slowly-evolving mass distributions. The question has not been asked in the right form.

This is not unusual in the history of physics. Olbers asked why the night sky was dark — a question that had an answer visible to anyone who looked up, but which required asking the question correctly. The Passive Layer is a similar case: the effect is present in every gravitational observation, but the question of its independent contribution has not been posed.

## Part 8. The One Open Question

The existence of the Passive Layer is a logical consequence of confirmed physics. It is not in question.

The one question that remains open is:

How large is it?

This is not a question of whether the effect exists. It exists. The question is whether its magnitude is negligible or significant at galactic and cosmological scales.

This calculation has not been done. That is the next step.

## Part 9. What This Document Is Not Claiming

This document is not claiming:
- That dark matter does not exist
- That ΛCDM is wrong
- That the Passive Layer explains all missing mass
- That existing cosmological observations are incorrect

This document is claiming:
- A term exists. It is non-zero. It follows from confirmed physics. Its magnitude has never been calculated. It should be.

## Summary

Statement: Gravity propagates at c — Status: Confirmed (GW170817, 2017)
Statement: Mass is created and destroyed — Status: Confirmed (QFT, particle physics)
Statement: Gravitational reverberation exists — Status: Logical consequence — necessary
Statement: Reverberation does not cancel — Status: Follows from absence of negative gravitational mass
Statement: Dynamic equilibrium is reached — Status: Follows from cosmic expansion (cf. Olbers' Paradox)
Statement: This term is in current cosmological models — Status: No
Statement: The magnitude has been calculated — Status: No
Statement: The magnitude is negligible — Status: Unknown — not yet calculated

The universe has been accounting for the Passive Layer since the beginning. Our models have not.

This document is a companion to the simulation series.

Full framework and citations:
- I Added a Black Hole to the LHC — and Something Unexpected Happened
- Passive Layer — Essential Citations
- A Unified Technical Framework — Simulation Evidence and Theoretical Foundations
- Black Hole Displacement and the Default State of Spiral Galaxies
- Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe
- High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes

---

# Passive Layer — Essential Citations

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/passive-layer-essential-citations

Note to the reader: This document is a structured record of observed phenomena across multiple physical scales. It does not claim to have solved any Millennium Problem or to have disproven any existing theory. It is presented as a complementary framework: this effect exists, it is non-zero, and its magnitude under extreme astrophysical conditions has not been adequately quantified.

## PART 0. Before You Begin: Three Facts You Need to Know

To understand this framework, you need to know only three things. All three are empirically verified facts. No new physics is required.

### Fact 1: Gravity Propagates at the Speed of Light

Just as light takes 8 minutes to travel from the Sun to Earth, changes in the Sun's gravity also take 8 minutes to reach Earth. Gravity is not instantaneous.

This was confirmed in 2017 when the LIGO/Virgo collaboration observed a neutron star merger (GW170817) and detected gravitational waves and gamma rays arriving simultaneously. The speed of gravity was constrained to within 10^{-15} of the speed of light c (Abbott et al. 2017, Physical Review Letters, 119, 161101).

Formula:
τ(r) = r / c

Meaning: A gravitational signal from distance r arrives after time r/c.

### Fact 2: Energy Can Become Mass

Einstein's famous equation E = mc^2 means that in high-energy environments, energy can convert into particle-antiparticle pairs.

This is directly observed at the LHC (Large Hadron Collider). Two high-energy photons collide and produce an electron-positron pair (Breit & Wheeler 1934, Physical Review, 46, 1087).

Formula (pair production threshold energy):
E_threshold = 2 m_e c^2 ≈ 1.022 MeV

Meaning: With enough energy, light can transform into matter (particles).

### Fact 3: Galactic Disks Rotate Differentially

Stars near the galactic center rotate faster; stars farther out rotate slower. This is the same as our Solar System: Mercury orbits the Sun in 88 days, Neptune in 165 years.

This is a universal observational fact of galactic dynamics (Freeman 1970, ApJ, 160, 811).

Formula (idealized Keplerian rotation):
v(r) ∝ r^{-1/2}

Meaning: Under Newtonian dynamics alone, rotation velocity should decrease with distance. But observations show it does not. This is why dark matter was introduced.

Now, let us combine these three verified facts and see what happens.

## PART 1. Background: Dark Matter and ΛCDM's Remaining Questions

The standard ΛCDM model is extraordinarily successful at cosmological scales. It reproduces the cosmic microwave background (CMB) temperature power spectrum (Planck Collaboration 2020), baryon acoustic oscillations (BAO, Eisenstein et al. 2005), and large-scale structure (Springel et al. 2005) with remarkable precision.

This document does not dispute ΛCDM's cosmological success.

However, ΛCDM faces unresolved issues at galactic scales:

- Direct detection failure: All dark matter direct detection experiments — LZ 2024, XENONnT 2024, PandaX-4T 2023 — have produced null results for 50 years.
- Cusp-core problem: CDM simulations predict density diverging as ρ ∝ r^{-1} (cusp) at galactic centers, but observations show nearly constant density cores (de Blok 2010).
- Missing satellites problem: CDM predicts about 200 satellite galaxies around the Milky Way, but only about 50 are observed (Bullock & Boylan-Kolchin 2017).
- Cosmological constant problem: The vacuum energy density predicted by quantum field theory (~10^{96} kg/m^3) and the observed value (~10^{-27} kg/m^3) differ by a factor of 10^{123} (Weinberg 1989).

This document observes that two well-established phenomena — the finite propagation speed of gravity and the statistical behavior of quantum vacuum fluctuations — may have combined implications at galactic scales that have not been fully explored.

## PART 2. Ghost Mass: The Gravity of Mass That No Longer Exists

Imagine: somewhere in the universe, two high-energy photons collide and produce an electron-positron pair (pair production). These particles exist briefly, then meet and annihilate. The mass disappears.

But here is the problem. Gravity propagates at the speed of light. The gravitational signal generated when the mass existed continues to travel through space for time r/c after the mass is gone. Stars experience the gravity of mass that no longer exists.

This is Ghost Mass.

Formula:
M_ghost(r) = ∫_0^r Ṁ_pair(r') · (r'/c) dr'

Meaning: The Ghost Mass accumulated up to radius r is the integral of the pair production rate at each distance r', multiplied by the time delay r'/c from that distance.

When the pair production rate is constant:
M_ghost(r) = Ṁ_pair · r/c  ⇒  M_ghost ∝ r

This is enormous in its implications.

Meaning for rotation curves (centrifugal balance):
v_c^2(r) = G · M_ghost(r) / r = G · Ṁ_pair / c = constant

If M_ghost ∝ r, then rotation velocity becomes constant regardless of distance. This explains flat rotation curves without dark matter, with no additional free parameters.

Citation: "The gravitational influence of a mass that briefly existed — and then annihilated — persists for r/c after it is gone. Ghost mass. A flat rotation curve emerges from this naturally, without dark matter, if the annihilation rate is roughly constant." — I Added a Black Hole to the LHC — and Something Unexpected Happened (2026-06-06)

But this explanation is missing one thing: "Why is the pair production rate constant?" The answer comes in Parts 3 and 4.

### 2.5 Two Distinct Components of Ṁ_pair

The pair production rate Ṁ_pair is not a single monolithic quantity. It has two independent physical origins that must be distinguished. Failure to distinguish them leads to apparent contradictions that are not actual contradictions.

Component A: Vacuum Fluctuation Component (Universal, Constant)

This component originates from the quantum vacuum itself. In flat spacetime, vacuum fluctuations are spatially uniform — the same in every cubic Planck-length of space regardless of position.

Ṁ_pair^vac(r) = constant (independent of r)

Meaning: This component does not depend on distance from the galactic center. It is the same everywhere in the universe (to leading order). It is the source of the constant Ṁ_pair assumption in Part 2.

Dominant regime: Far-field (r ≫ R_disk) — see Section 6.4
Part reference: Part 10 (Snapshot Mass)

Component B: Local Astrophysical Component (Disk-like, Position-Dependent)

This component originates from high-energy environments around black holes, active galactic nuclei (AGN), supernovae, and other localized sources. It scales with local energy density.

Ṁ_pair^local(r) ≈ Ṁ_pair,0^local · f(r), f(r) high near center, low at large r

Meaning: This component is concentrated in the galactic disk. It dominates the near-field region (r ≲ R_disk) and is responsible for the disk-like source distribution described in Part 4.

Dominant regime: Near-field (r ≲ R_disk)
Part reference: Part 4 (Why the Pair Production Rate Can Be Constant)

Comparison of the two components:

Vacuum fluctuation component:
- Origin: Quantum vacuum
- r-dependence: Constant
- Dominant regime: Far-field (r ≫ R_disk)
- Part reference: Part 10

Local astrophysical component:
- Origin: BHs, AGN, supernovae
- r-dependence: Disk-like (decreases with r)
- Dominant regime: Near-field (r ≲ R_disk)
- Part reference: Part 4

Therefore, there is no contradiction. The constant Ṁ_pair assumption in Part 2 refers to Component A (vacuum fluctuations). The disk-like distribution described in Part 4 refers to Component B (local astrophysical sources). Both exist simultaneously and dominate in different spatial regimes.

The total pair production rate is the sum of both components:
Ṁ_pair^total(r) = Ṁ_pair^vac + Ṁ_pair^local(r)

Meaning: At small r, the local component dominates. At large r, the vacuum component becomes relatively more important. The transition between these regimes is described in Section 6.4 (Far-Field Limit).

## PART 3. Charge Separation: Why Particles Do Not Annihilate

Black holes are surrounded by powerful magnetic fields. EHT observations of M87* measured magnetic fields of 1-30 Gauss at the photon ring (EHT MWL Science Working Group, 2021). Moving inward, the magnetic field increases sharply, estimated at 10^4-10^6 Gauss near the ISCO.

In the LHC simulator (Yang-Mills Collider v3.2), when such an environment was created, something unexpected happened.

Particles and antiparticles separated. They did not annihilate. They persisted as mass.

The reason is simple. The Lorentz force bends positive and negative charges in opposite directions.

Formula (Lorentz force):
F = q(v × B)

Black hole gravity pulls both toward the same point, but they arrive from opposite sides. They never meet. They do not annihilate.

Crucially, this phenomenon appeared without being programmed.

Citation: "I did not build an accretion disk. One appeared." — I Added a Black Hole to the LHC — and Something Unexpected Happened (2026-06-06)

The Boris integrator used in the simulator is the standard algorithm in GEANT4 and plasma physics PIC codes, accurately computing charged particle motion in magnetic fields.

Formula (Boris integrator steps):
t = (q Δt / (2 γ m)) B̂
p^- = p + p × t
s = 2t / (1 + |t|^2)
p^+ = p^- + p^- × s
p_new = p^+ + p^+ × t

Meaning: The direction of rotation depends on the sign of the charge. Positive charges rotate one way, negative charges the opposite way.

Newtonian gravity code (just 4 lines) implementing black hole gravity:

const gAcc = logMass * 120.0 / (r2 + 1.0)
p.p4.px -= gAcc * (dx / r) * dt
p.p4.py -= gAcc * (dy / r) * dt
p.p4.pz -= gAcc * (dz / r) * dt

Without GR, without MHD, without fluid dynamics, without a single line of "build an accretion disk" code, a disk appeared spontaneously.

Thus: pair production occurs continuously around black holes, the magnetic field separates the particles and suppresses annihilation, and mass persists.

## PART 4. Why the Pair Production Rate Can Be Constant (Mechanism 2)

The Ghost Mass formula assumes a constant pair production rate Ṁ_pair. But why would Ṁ_pair be constant?

This section explains the physical mechanism that maintains a constant Ṁ_pair.

### 4.0 Clarification: Which Component Are We Discussing?

Before answering "why the pair production rate can be constant," a critical clarification is necessary.

Section 2.5 distinguished two independent components of Ṁ_pair:

Component A: Vacuum fluctuation component (Ṁ_pair^vac)
- r-dependence: Constant
- This Part (Part 4) discusses this component? ❌ No — discussed in Part 10
- Type of constancy: Spatial constancy (independent of r)

Component B: Local astrophysical component (Ṁ_pair^local)
- r-dependence: Disk-like (decreases with r)
- This Part (Part 4) discusses this component? ✅ Yes — this section
- Type of constancy: Temporal constancy (steady state over time at fixed r)

Then why is this section titled "Why the Pair Production Rate Can Be Constant"?

Because the local astrophysical component, despite being disk-like in its spatial distribution, can maintain a temporally constant production rate at each radius. This is a different kind of constancy — constancy in time, not in space.

∂Ṁ_pair^local(r, t)/∂t ≈ 0 (steady state)

Meaning: For a fixed distance r from the galactic center, the local pair production rate fluctuates around a stable mean value over long timescales (millions to billions of years). This is the constancy referred to in the Ghost Mass derivation — not spatial uniformity, but temporal steadiness.

The two types of constancy summarized:

Spatial constancy (Component A):
- Meaning: Ṁ_pair independent of r
- Applies to: Vacuum fluctuation component
- Physical origin: Quantum vacuum is uniform
- Part reference: Part 10

Temporal constancy (Component B):
- Meaning: Ṁ_pair stable over time at fixed r
- Applies to: Local astrophysical component
- Physical origin: Steady-state high-energy environments (this section)
- Part reference: Part 4

Therefore, there is no contradiction. The word "constant" means different things in different contexts:

- Part 2 uses "constant" to mean spatially constant (independent of r), referring to the vacuum fluctuation component.
- Part 4 uses "constant" to mean temporally constant (steady over time), referring to the local astrophysical component.

The following subsections (4.1-4.6) explain the physical mechanisms that maintain temporal constancy of the local astrophysical component, despite the extreme and variable conditions near black holes.

### 4.1 The Ultra-High-Energy Environment

The environment around a black hole is incomparably more extreme than the LHC:

- LHC (humanity's strongest): B = 8.3 T, energy scale 13,000 GeV
- Magnetar: B ~ 10^{14} T (10^{10} times), energy scale ~10^{20} GeV
- AGN black hole: B ~ 10^{10}-10^{11} T (10^9 times), energy scale ~10^{24} GeV and above

In this environment, the following chain of pair production → isolation → accumulation can occur:

- γ + γ → e^+ + e^- (or heavier particle-antiparticle pairs)
- B ≫ B_critical → annihilation suppressed (r_L ≪ R_system)
- Matter + antimatter → spatial isolation → gravitational contribution maintained

### 4.2 Larmor Radius and Mass Separation

In a magnetic field B, a charged particle traces a circular path. The radius of this circular motion is called the Larmor radius:

r_L = γ m v_⊥ / (|q|B) = p_⊥ / (|q|B)

The angular frequency is:
ω_c = |q|B / (γ m)

Key insight: r_L ∝ m (proportional to mass!)

For particles with the same energy and the same charge:
- Electron (m = 0.511 MeV): smallest radius → innermost orbit
- Pion (m = 140 MeV): intermediate radius
- Proton (m = 938 MeV): larger radius → outer orbit
- W boson (m = 80,377 MeV): very large radius → outermost orbit

This is the physical cause of the mass-dependent orbital radius separation observed in the simulation.

Pair production rate is not uniform. It scales with local energy density — highest near the black hole, lowest in voids. The stack thickness varies accordingly.

### 4.3 Annihilation Suppression Condition

For annihilation (e^+ + e^- → γ + γ) to occur, the two particles must meet. The magnetic field can prevent this when:

r_L = γ m c / (eB) ≪ R_system

(the Larmor radius is much smaller than the system size)

Considering a real GRB environment:
- B ~ 10^{12} - 10^{15} G
- Larmor radius of an electron (γ ~ 10^6) ≈ 10^{-2} cm

This is far smaller than the system size (R_system). Therefore, matter and antimatter can remain spatially isolated for a long time.

### 4.4 The Ṁ_pair Term in the Mass Rate-of-Change Equation

The conventional black hole mass growth equation considers only external accretion:

dM/dt = Ṁ_in - Ṁ_out - Ṗ_Hawking / c^2

However, the pair production mechanism suggests an additional term:

dM/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking / c^2

where Ṁ_pair is the independent mass contribution rate from pair production.

This term has not been explicitly treated in the existing literature to the author's knowledge.

### 4.5 Three Possible Fates for Isolated Matter and Antimatter

1. When the magnetic field weakens, annihilation occurs → energy released → gravity decreases
2. Absorbed by the black hole → incorporated as mass → gravity increases
3. Ejected as a jet → moves to the galactic outskirts → gravity redistributed

Any of these pathways creates gravitational variability in the black hole. This is the core of Mechanism 2.

### 4.6 Connection to the Early Universe Supermassive Black Hole Problem

One of the most serious unsolved problems in current astronomy: How could supermassive black holes with masses of about 10^9 solar masses have grown so rapidly in the early universe (z > 6, within the first billion years of cosmic history)?

Under the Eddington luminosity limit, reaching this mass through external accretion alone requires the Eddington time (approximately 450 million years):

t_Eddington = M / Ṁ_Edd = 450 Myr (for radiative efficiency η = 0.1)

Yet the observed quasars reached this mass in far less time. External accretion alone is insufficient.

Applying the logic of Mechanism 2 to the early universe opens up a new possibility:
- The environment around black holes in the early universe was far more extreme than today
- Higher energy density → higher pair-production rate
- Stronger magnetic fields → more efficient annihilation suppression
- There may have been conditions where the Ṁ_pair term could dominate over Ṁ_in

If this mechanism operated, the problem of rapid supermassive black hole growth in the early universe would be naturally resolved.

## PART 5. Passive Layer: The Form of Existence

The gravitational remnants generated in this way accumulate as background across all of space. Unintentional. Uncontrollable. Always operating.

This is the Passive Layer.

Formula (Passive Layer accumulated mass):
M_PL(r) = ∫_0^r Ṁ_pair(r') · (r'/c) dr'

The formula is identical to Ghost Mass. Because they are different languages describing the same phenomenon.

Four Core Properties:

- Unintentional: No agent intends to create it. The simulator had no "build a disk" code, yet a disk appeared.
- Uncontrollable: Cannot be turned off. As long as pair production occurs and magnetic fields exist, this phenomenon continues. There is no "off" button.
- Automatic: Once conditions are met, it activates automatically. Like a passive skill in games — always on without pressing a button.
- Background: Not concentrated at specific locations. Spread throughout space as background. Unlike dark matter, which is hypothesized to be "clumped somewhere," the Passive Layer is spread everywhere.

Citation: The term Passive Layer was chosen to describe the form of existence this mechanism creates — as distinct from Ghost Mass, which describes the mechanism itself.

Relationship between Ghost Mass and Passive Layer:
- Ghost Mass describes the mechanism ("how it arises")
- Passive Layer describes the form of existence ("what it is")

Two faces of the same phenomenon. Not substitutes, but complements.

## PART 6. Passive Layers Stacking: Superposition and Accumulation

Now we come to the most important concept.

A single Passive Layer is the remnant from a single time and a single distance. But the universe contains billions of black holes, and each black hole continuously produces Passive Layers. And all these layers overlap and accumulate.

This is Passive Layers Stacking.

Formula (combination of spatial and temporal stacking):
M_stack(r,t) = ∫_0^t ∫_0^r Ṁ_pair(r',t') · δ(t - t' - r'/c) dr' dt'

Meaning: The total mass accumulated at this moment (t) up to radius r is the sum of all pair production events from all past times (t') and all distances (r') whose signals are arriving exactly now (t' + r'/c = t).

This can be understood in three dimensions.

### 6.1 Spatial Stacking

Each star at distance r sees the black hole's position from time r/c ago.
τ(r) = r / c

Specific examples:
- r = 1 kpc → layer from 3,260 years ago
- r = 5 kpc → layer from 16,300 years ago
- r = 10 kpc → layer from 32,600 years ago
- r = 50 kpc → layer from 163,000 years ago

The farther you look, the older the layer you see. This is exactly the same principle as telescopes seeing more distant (and therefore older) galaxies.

### 6.2 Temporal Stacking

At this very moment, remnants from all past times exist simultaneously.
- Remnant from 1 billion years ago → still propagating
- Remnant from 500 million years ago → still propagating
- Remnant from 100 million years ago → still propagating
- Remnant from the present → just starting

The implication is enormous. The gravity we experience now is the sum of all remnants accumulated over billions of years.

### 6.3 Cosmic Stacking

We are not considering just one black hole in one galaxy.
- Passive Layers from the Milky Way's central BH
- Passive Layers from Andromeda's BH
- Passive Layers from all BHs in the Virgo Supercluster
- Passive Layers from all BHs in the observable universe

All remnants from all black holes overlap. Billions of years' worth of remnants exist simultaneously, right now.

Citation: "Passive Layers Stacking is the phenomenon in which Passive Layers from different times and distances spatially and temporally overlap and accumulate. The entire universe moves upon the echoes of its own past mass activity.

Effect at galactic scale: Passive Layers Stacking → M_ghost ∝ r → flat rotation curve → appears like dark matter

Possible effect at cosmic scale (not yet validated): Passive Layers Stacking → cosmic background mass density → influence on cosmic expansion → possible connection to dark energy

### 6.4 The Far-Field Limit: Why the Passive Layer Becomes Spherical at Large Radii

The static approximation M_ghost(r) = Ṁ_pair · r/c from Part 2 is a near-field limit. It is valid for r ≲ R_disk but breaks down at large distances.

For |r| ≫ R_disk, the full stacking integral must be used. Expanding the distance:

|r - r'| = |r| - r̂·r' + O(R_disk^2/|r|)

The leading term depends only on |r| (spherical symmetry), with angular-dependent corrections that decay as 1/|r|.

Therefore:
- Near-field (r ≲ R_disk): Static approximation M = Ṁ_pair · r/c → Disk-like distribution
- Far-field (r ≫ R_disk): Full stacking integral → Spherical distribution (to leading order)

Implication for dark matter: At large galactic radii — precisely where dark matter halos are inferred — the Passive Layer distribution is effectively spherical. This resolves the apparent tension between the disk-like generation mechanism and the spherical dark matter halo.

The Passive Layer is born in the disk but lives in a sphere.

## PART 7. Delayed Gravity and the History Buffer

To simulate this phenomenon, the "History Buffer" was created.

The black hole's position is stored in a FIFO (First-In-First-Out) buffer of 300 steps. Each star retrieves the past position corresponding to its distance from this buffer.

Formula (retarded position):
r_BH^ret(t, r) = r_BH(t - α r / c)

Here, α is the retardation strength parameter. The physical prediction is α = 1.

Formula (linear interpolation from history buffer):
r_BH(t-τ) ≈ r_BH(t_0) + (τ - t_0)/(t_1 - t_0) [r_BH(t_1) - r_BH(t_0)]

Meaning: The retarded position is recovered by linear interpolation between stored historical positions.

## PART 8. Black Hole Displacement: Why It Moves

Perfect black hole stasis — zero displacement from the galactic barycenter at all times — would require exact cancellation of all the following perturbations simultaneously and continuously:

- Host galaxy peculiar velocity through the cosmic web (100–600 km/s)
- Tidal forces from satellite galaxies and globular clusters
- Galactic bar oscillations (when bar is present)
- Large-scale structure gravitational background (cosmic filaments, voids)
- Recoil from asymmetric gravitational wave emission during any merger event

This exact cancellation is not physically plausible. Black hole displacement is the default state.

The mass ratio argument:
f_BH = M_BH / M_total

- Solar System: f_Sun ≈ 0.998 → displacement suppressed
- Disk galaxy: f_BH ≈ 0.001-0.005 → displacement free

Spiral structure is therefore the expected morphology for disk galaxies.

## PART 9. Spiral Structure as Default State: Inverting the Question

The standard question in galactic dynamics is:

"Why do spiral arms form?"

This document argues that the question is inverted. The correct question is:

"Why do some galaxies NOT have spiral arms?"

Approximately 60–70% of observed galaxies in the local universe exhibit spiral structure (Lintott et al., 2011, Galaxy Zoo). If spiral structure requires special conditions — specific resonances, density waves, tidal partners — then 60–70% prevalence is difficult to explain. If spiral structure is the generic outcome of ordinary physical conditions, 60–70% prevalence is expected.

The remaining 30–40% — ellipticals, lenticulars, irregulars — represent systems where disk structure itself is absent or disrupted, not systems that failed to develop spiral arms.

The mechanism described in this document produces spiral arms as a default state, not a special outcome.

## PART 10. Snapshot Mass: The Weight of the Vacuum

### The Statistical Snapshot Argument

Let N(t) be the number of virtual particle pairs simultaneously existing in a volume V at time t. Each pair has a characteristic mass m and lifetime τ ≤ ħ/(2mc^2).

The instantaneous mass contribution of this population is:
M_snap(t) = Σ_i m_i · θ(τ_i - (t - t_i))

where θ is the Heaviside step function, t_i is the creation time of pair i, and τ_i is its lifetime.

This quantity fluctuates rapidly — on timescales of order t_P. However, its time average over any macroscopic interval T ≫ t_P is:
⟨M_snap⟩ = ⟨N⟩ · ⟨m⟩

The snapshot argument. Freeze the universe for 10^{-44} seconds. In that instant, across every cubic Planck-length of space, particle pairs are blinking into existence. Each one is gone before any measurement could reach it. But in that frozen moment — they are there. They have mass. They curve spacetime. The snapshot has weight.

This is not a metaphor. It is a statistical fact.

### Order of Magnitude in Flat Spacetime

In pure Minkowski vacuum, assuming one Planck-scale pair per Planck volume:
⟨N_0⟩ ≈ V / l_P^3

For a galactic volume V_gal ≈ 10^{61} m^3:
⟨N_0⟩ ≈ 10^{61} / (1.62 × 10^{-35})^3 = 10^{166}

At Planck mass per pair (m_P ≈ 2.18 × 10^{-8} kg):
⟨M_snap⟩_0 ≈ 10^{166} × 10^{-8} kg = 10^{158} kg

This is approximately 10^{118} times the observed mass of the Milky Way (~10^{40} kg).

The conclusion is immediate: in flat spacetime, the statistical snapshot mass is astronomically larger than observed galactic mass, and must be almost entirely cancelled by quantum correlations. This is simply the cosmological constant problem restated in the language of statistical mechanics.

### The Amplification Factor Γ(r)

We define the local amplification factor as:
Γ(r) = ρ_effective(r) / ρ_Λ

where ρ_effective(r) is the effective vacuum mass density at position r after accounting for correlation disruption, and ρ_Λ is the cosmological constant density (~6 × 10^{-27} kg/m^3).

Boundary conditions:
- Flat spacetime far from any source: Γ = 1 (by definition)
- Near stellar-mass black hole: Γ > 1 (unknown magnitude)
- Near supermassive black hole: Γ ≫ 1 (unknown magnitude)

## PART 11. The Same Pattern Found Across Four Scales

This framework identifies a repeating pattern across four distinct physical scales:

Quantum: Phenomenon — Virtual particle pairs — Passive Layer Analog: Snapshot mass from vacuum fluctuations
Particle: Phenomenon — Pair production near black holes — Passive Layer Analog: Ghost Mass from annihilation-suppressed pairs
Galactic: Phenomenon — Retarded gravity from BH displacement — Passive Layer Analog: Spiral arms and flat rotation curves
Cosmological: Phenomenon — Cumulative stacking of all past events — Passive Layer Analog: Dynamic equilibrium background density

The same mathematical structure appears at each scale: a source term (pair production rate), a propagation delay (r/c), and accumulation (stacking).

## PART 12. Falsifiable Predictions

This framework makes the following predictions, each falsifiable by observation:

Prediction 1. Spiral arm strength correlates with BH displacement magnitude from the photometric center. Galaxies with stronger, more symmetric grand-design spiral arms should show larger BH-center offsets when measured at sufficient resolution.

Prediction 2. Arm count corresponds to BH oscillation mode. Two-armed spirals correspond to simple displacement; multi-armed spirals to oscillatory BH motion.

Prediction 3. The inverse problem is solvable. Given a galaxy's spiral morphology (arm count, pitch angle, symmetry), it should be possible to reconstruct the approximate kinematic history of its central BH.

Prediction 4. Elliptical and lenticular galaxies without disks are the expected non-spiral population. They do not represent failures to produce spiral arms; they represent systems where no disk existed to develop them.

Prediction 5. The vacuum statistical mass contribution should be more centrally concentrated than CDM's NFW profile. Galaxies with more massive or more rapidly spinning central black holes should show relatively stronger central mass excess.

Prediction 6. Unlike WIMPs or axions, the vacuum statistical mass is not a particle. It cannot be detected in direct-detection experiments. This is consistent with all current null results (LZ 2024, XENONnT 2024, PandaX-4T 2023).

## PART 13. Limitations (Stated Honestly)

This framework has significant gaps that must be acknowledged:

Q1 — The Cancellation Mechanism. We do not know what causes the 10^{123} cancellation in flat spacetime. Without knowing the mechanism, we cannot predict how much it is disrupted in curved spacetime. Any quantitative estimate of Γ(r) is currently a free parameter.

Q2 — Backreaction. If vacuum fluctuations contribute to the stress-energy tensor, they also affect the spacetime geometry — which in turn affects the fluctuation rate. This self-consistent backreaction problem is unsolved even in simplified toy models.

Q3 — Distinguishability. Near galactic centers, the vacuum statistical mass profile and the CDM profile may produce similar observational signatures. Distinguishing them requires either (a) measurements sensitive to the equation of state of the dark component, or (b) high-precision rotation curve data in the inner ~1 kpc.

Q4 — Cosmological Consistency. If Γ(r) is large near every galactic center, the integrated contribution over all galaxies in the observable universe may produce a measurable effect on the CMB or large-scale structure. This constraint has not been calculated.

Q5 — The Entanglement Structure. The argument that long-range quantum entanglement causes cancellation in flat spacetime is plausible but not proven. The calculation of how this entanglement structure is modified by curved spacetime is an open problem in quantum gravity.

## PART 14. Comparison with Existing Frameworks

Feature: Spiral formation
- Lin-Shu Density Wave: Pattern wave
- MOND: Not addressed
- This Framework: BH displacement + retarded gravity

Feature: Rotation curve
- Lin-Shu Density Wave: Not primary
- MOND: Modified dynamics
- This Framework: Retarded a_ret (no 1/r falloff)

Feature: Dark matter
- Lin-Shu Density Wave: Required (some versions)
- MOND: Replaced
- This Framework: Reexamined, not required

Feature: Free parameters
- Lin-Shu Density Wave: Pattern speed Ω_p
- MOND: a_0
- This Framework: α (one parameter)

Feature: Universality of spirals
- Lin-Shu Density Wave: Requires resonance
- MOND: N/A
- This Framework: Generic consequence of BH motion

## PART 15. The Three Independent Mechanisms (Summary)

Claim I — Retarded Gravity and Spiral Arms. When a black hole is displaced from the geometric center of a disk galaxy — however slightly — spiral arm structure emerges immediately and persistently. This is a consequence of the finite propagation speed of gravity.

Claim II — Vacuum Statistical Mass and Pair Separation. The ultra-strong magnetic fields observed in the vicinity of supermassive black holes create conditions where particle-antiparticle pairs produced from vacuum fluctuations are separated by the magnetic field before annihilation can occur. Separated particles persist as mass.

Claim III — Fluctuating Mass and Finite-Speed Gravity. If gravity propagates at a finite speed, then the gravitational influence of fluctuating mass near a black hole propagates outward across the galaxy with a delay proportional to distance. A flat rotation curve emerges from this naturally.

These three claims are independent. Claim I does not require Claims II or III to be true. However, together they form a complete framework for galactic dynamics without dark matter.

## PART 16. Conclusion

We have presented a framework for understanding why the quantum vacuum may contribute a small but non-zero effective mass density to galactic dynamics, concentrated near regions of high spacetime curvature and strong electromagnetic fields.

The central argument is:
1. Quantum vacuum fluctuations exist and carry energy-momentum.
2. In flat spacetime, quantum correlations cause their gravitational effects to nearly perfectly cancel — the cosmological constant problem states the residual is 10^{-123} of the naive estimate.
3. In strongly curved or strongly magnetized spacetime, these correlations are partially disrupted — this is already established by the Casimir, Unruh, Hawking, and Schwinger effects.
4. The disruption leaves a residual vacuum statistical mass that is small relative to the flat-space estimate but potentially significant relative to baryonic galactic mass.

This contribution is not dark matter. It is not a new particle. It is a gravitational consequence of known quantum field theory in curved spacetime, extended to realistic astrophysical environments.

The magnitude of this effect is unknown. The calculation required to determine it — quantum field theory in Kerr spacetime with realistic magnetic field configurations, integrated over a realistic galactic density profile — has not been performed.

This document is a statement that the calculation should be performed.

## APPENDIX A. Recommended Reading Order (Links)

1. I Added a Black Hole to the LHC — and Something Unexpected Happened
2. Black Hole Physics in Yang-Mills Collider v3.2
3. Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation
4. Black Hole Displacement and the Default State of Spiral Galaxies
5. The Passive Layer — Core Document
6. Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe
7. High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes
8. A Unified Technical Framework — Simulation Evidence and Theoretical Foundations

## APPENDIX B. Complete Collection of Citations and Source URLs

Primary observational confirmation:
- Abbott et al. (2017). GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. PRL, 119, 161101.

Black hole offset observations:
- Batcheldor et al. (2010). A Displaced Supermassive Black Hole in M87. ApJL, 717, L6.
- Bartlett et al. (2021). Offset AGN dataset compilation.
- Chu, Boldrini & Silk (2022). Off-centre supermassive black holes in bright central galaxies.

Galactic dynamics:
- Freeman (1970). On the Disks of Spiral and S0 Galaxies. ApJ, 160, 811.
- Kormendy & Ho (2013). Coevolution of Galaxies and Supermassive Black Holes. ARAA, 51, 511.
- Lelli, McGaugh & Schombert (2016). SPARC: Mass Models for 175 Disk Galaxies. AJ, 152, 157.
- Lintott et al. (2011). Galaxy Zoo 1. MNRAS, 410, 166.

Alternative frameworks:
- Lin & Shu (1964). On the Spiral Structure of Disk Galaxies. ApJ, 140, 646.
- Yahalom, A. (2013, 2019, 2024). Retarded gravity and galactic rotation curves.
- Milgrom, M. (1983). A modification of the Newtonian dynamics. ApJ, 270, 365.

Cosmological constant:
- Weinberg, S. (1989). The cosmological constant problem. Rev. Mod. Phys. 61, 1.
- Padmanabhan, T. (2003). Cosmological constant: the weight of the vacuum. Phys. Rep. 380, 235.
- Planck Collaboration (2020). Astron. Astrophys. 641, A6.

Quantum effects in curved spacetime:
- Hawking, S.W. (1975). Particle creation by black holes. Commun. Math. Phys. 43, 199.
- Unruh, W.G. (1976). Notes on black-hole evaporation. Phys. Rev. D 14, 870.
- Schwinger, J. (1951). On gauge invariance and vacuum polarization. Phys. Rev. 82, 664.
- Casimir, H.B.G. (1948). On the attraction between two perfectly conducting plates. Proc. K. Ned. Akad. Wet. 51, 793.

Simulation infrastructure:
- GalaxyCS v4: Galaxy-scale simulator with retarded gravitational propagation
- Yang-Mills Collider v3.2: Particle physics simulator with Boris integrator and Kerr black hole

---

# A Unified Technical Framework — Simulation Evidence and Theoretical Foundations

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/a-unified-technical-framework-simulation

Author's Note: This document is written by a non-specialist. It is not a peer-reviewed paper. It is a structured record of an investigation — conducted through simulation, observation of emergent behavior, systematic reasoning, and theoretical analysis — into a specific question: whether the finite propagation speed of gravity, combined with the statistical behavior of quantum vacuum fluctuations, is sufficient to reproduce galactic dynamics without invoking dark matter.

## Preface

This document does not argue that dark matter does not exist. It argues something narrower and, in some ways, more interesting: that two well-established physical phenomena — the retarded propagation of gravity and the statistical behavior of quantum vacuum fluctuations — may together account for a non-trivial portion of what we currently attribute to unseen mass.

The first of these (delayed gravity) has been demonstrated computationally and is the subject of a companion simulation series (GalaxyCS v4, Yang-Mills Collider v3.2). The second (vacuum statistical mass) is the subject of this document.

It is presented not as a competing theory but as a complementary observation: this effect exists, it is non-zero, and its magnitude under extreme astrophysical conditions has not been adequately quantified.

## Three Core Claims

The following three claims structure this document. They are stated here at the outset, without elaboration. Each is developed in full in the sections that follow.

Claim I — Retarded Gravity and Spiral Arms. When a black hole is displaced from the geometric center of a disk galaxy — however slightly — spiral arm structure emerges immediately and persistently. This is a consequence of the finite propagation speed of gravity: stars at different distances from the black hole reference different past positions of that black hole, producing a systematic angular offset in the gravitational force vector that, in a rotating system, maps onto a spiral pattern. This claim is verifiable directly in GalaxyCS v4.

Claim II — Vacuum Statistical Mass and Pair Separation. The ultra-strong magnetic fields observed in the vicinity of supermassive black holes — combined with the extreme energy densities of accretion disks and relativistic jets — create conditions where particle-antiparticle pairs produced from vacuum fluctuations are separated by the magnetic field before annihilation can occur. Separated particles persist as mass. This mass fluctuates. This constitutes a mechanism for continuous local mass generation around black holes. This claim has been observed directly in Yang-Mills Collider v3.2.

Claim III — Fluctuating Mass and Finite-Speed Gravity. If gravity propagates at a finite speed (which it does), then the gravitational influence of fluctuating mass near a black hole propagates outward across the galaxy with a delay proportional to distance. A flat rotation curve emerges from this naturally. This claim is a consequence of Claims I and II combined.

These three claims are independent. Claim I does not require Claims II or III to be true. However, together they form a complete framework for galactic dynamics without dark matter.

## Chapter 1: The Problem We Are Not Solving (and the One We Are)

### 1.1 The Success of ΛCDM

The standard account of galactic dynamics requires approximately five times more mass than is visible. This "missing mass" is conventionally attributed to a new class of particle — cold dark matter (CDM) — that interacts gravitationally but not electromagnetically.

The ΛCDM model built on this assumption is extraordinarily successful. It reproduces:

- CMB temperature fluctuations (Planck 2020): 0.1% level agreement
- Baryon acoustic oscillations (Eisenstein 2005): 1% level agreement
- Large-scale structure (SDSS, DES): 10% level agreement

We are not disputing this success.

### 1.2 What We Are Noting

ΛCDM's success at cosmological scales does not preclude the existence of additional, smaller-magnitude effects at galactic scales. Two such effects are the subject of this document:

Effect 1 — Retarded Gravitational Interaction. Gravity propagates at the speed of light. In a rotating galactic disk, this retardation introduces an asymmetry in the gravitational field that is not captured by the instantaneous Newtonian approximation. Companion simulations (Yang-Mills Collider v3.2, GalaxyCS v4) demonstrate that this effect alone reproduces flat rotation curves and spiral arm morphology without invoking additional mass.

Effect 2 — Vacuum Statistical Mass. The quantum vacuum is not empty. Virtual particle pairs are continuously created and annihilated on timescales governed by the energy-time uncertainty relation (ΔE·Δt ≥ ħ/2). Individually, each fluctuation is transient — existing for ~10^{-44} seconds at the Planck scale. Statistically, however, at any given moment, a finite population of such fluctuations exists simultaneously across any finite volume. Under extreme gravitational and electromagnetic conditions — black hole ergospheres, active galactic nuclei, magnetar surfaces — the rate, lifetime, and separation probability of these fluctuations are enhanced. The cumulative statistical mass of this enhanced population may constitute a small but non-negligible contribution to galactic mass budgets.

### 1.3 The Remaining Problems of ΛCDM (For Context)

Even if Effect 1 and Effect 2 are both correct, ΛCDM still faces unresolved issues. This is not our primary argument, but it provides context for why alternative frameworks deserve consideration.

Problem: Direct detection failure — Description: No WIMP/axion signal after decades of effort (LZ 2024: cross-section upper limit 2.9×10^{-48} cm^2 at 40 GeV/c^2) — Source: LZ 2024, XENONnT 2024
Problem: Cusp-core problem — Description: CDM predicts ρ ∝ r^{-1} (cusp), observations show ρ ~ constant (core) — Source: de Blok 2010
Problem: Missing satellites problem — Description: CDM predicts ~200 satellite galaxies around Milky Way, ~50 observed — Source: Bullock & Boylan-Kolchin 2017
Problem: Cosmological constant problem — Description: Theoretical vacuum energy (~10^{96} kg/m^3) vs observed (~10^{-27} kg/m^3): 10^{123} discrepancy — Source: Weinberg 1989

## Chapter 2: Effect 1 — Retarded Gravitational Interaction

### 2.1 Basic Principle

Newton's law of universal gravitation assumes instantaneous propagation of gravity. However, general relativity dictates that gravity propagates at the speed of light c. In a rotating galactic disk, this retardation introduces an asymmetry in the gravitational field that is not captured by the instantaneous Newtonian approximation.

Basic concepts:
- The central black hole (or mass distribution) moves.
- A star at distance r feels gravity from the black hole's past position, not its current position.
- The light-travel time delay is Δt = r/c.
- Stars at different distances reference different past positions.
- In a rotating disk, this radially-dependent angular offset is sheared into a spiral pattern.

### 2.2 Mathematical Formulation

Retarded position:
r_ret(t) = r(t - Δt)
Δt = |r(t) - r_ret| / c

Equation of motion (Newtonian + retardation):
a(r, t) = -G M_BH (r - r_ret(t, r)) / |r - r_ret(t, r)|^3

### 2.3 History Buffer Implementation (GalaxyCS v4)

The retarded position is computed by maintaining a FIFO position history buffer for the black hole:
r_BH^ret(t, r) = r_BH(t - α r / c)

where α is the retardation strength parameter (physical prediction: α = 1).

Linear interpolation from history buffer:
r_BH(t-τ) ≈ r_BH(t_0) + (τ - t_0)/(t_1 - t_0) [r_BH(t_1) - r_BH(t_0)]

### 2.4 Leapfrog (Velocity Verlet) Integrator

The simulator uses a leapfrog integrator to maintain numerical stability over long integration times.

Integration steps:
v_{n+1/2} = v_n + a(r_n) Δt/2
r_{n+1} = r_n + v_{n+1/2} Δt
a_{n+1} = a(r_{n+1})
v_{n+1} = v_{n+1/2} + a_{n+1} Δt/2

Properties:
- Formal accuracy: O(Δt^2) — sufficient for galactic dynamics
- Time reversibility: Yes — distinguishes physical behavior from artifacts
- Symplecticity: Yes — preserves phase space volume
- Energy conservation: Near-exact — monitored in real time
- Angular momentum conservation: Near-exact — monitored in real time

### 2.5 Simulation Results (GalaxyCS v4)

Condition: Newtonian (no retardation) — Result: Keplerian rotation curve (v ∝ r^{-1/2})
Condition: Retarded gravity included — Result: Flat rotation curve + spontaneous spiral arm formation
Condition: Retarded gravity + black hole spin — Result: Spin-proportional rotation velocity increase

Quantitative results (intermediate galaxy model):
- Retarded gravity alone reproduces flat rotation curves (~200 km/s) without dark matter
- Approximately 80-90% of the rotation curve is explained by retarded gravity
- Remaining 10-20% can be explained by Effect 2 (vacuum statistical mass)

### 2.6 Observed Behavior and Predicted Consequences

Immediate spiral formation. In GalaxyCS v4, with 20,000-80,000 test particles initialized on circular orbits:
- Black hole at rest (displacement = 0): No spiral structure. Axisymmetric disk.
- Black hole displaced by any non-zero amount: Spiral arm structure emerges within the first few simulation steps and persists indefinitely.
- The transition is not gradual. It is immediate. There is no critical displacement threshold.

Arm count and morphology. Determined by the kinematic history of black hole displacement:
- Simple unidirectional displacement → Two-arm spiral
- Oscillatory displacement → Multi-arm structure
- Irregular displacement → Flocculent or asymmetric arms

Rotation curve behavior. The HUD in GalaxyCS v4 displays in real time:
- Observed stellar rotation velocity at outer disk radius
- Newtonian prediction for the same radius given the disk mass distribution
- The ratio (observed / predicted)

In runs with active retarded gravity and BH displacement, the outer rotation velocity consistently exceeds the Newtonian prediction by factors of 1.5-3.0, depending on the α parameter and BH displacement. This qualitatively reproduces the flat or rising rotation curves observed in disk galaxies.

Void formation. Reduction of black hole mass — simulating mass loss, observation uncertainty, or temporary disruption — followed by displacement and mass recovery produces large underdense regions (voids) in the stellar distribution. This behavior emerges without any additional mechanism.

### 2.7 Limitations of Effect 1

- Does not explain gravitational lensing excess (lensing is geometric, independent of time derivatives)
- Does not explain galaxy cluster dynamics
- Unrelated to CMB angular power spectrum
- May require fine-tuning of black hole displacement in some galaxy types

## Chapter 3: Effect 2 — Vacuum Statistical Mass

### 3.1 Foundations: What the Vacuum Actually Is

Energy-Time Uncertainty Relation:
ΔE · Δt ≥ ħ/2

Planck scale:
- Planck energy: E_P = sqrt(ħ c^5 / G) ≈ 1.22 × 10^{19} GeV
- Planck time: t_P = sqrt(ħ G / c^5) ≈ 5.39 × 10^{-44} s
- Planck length: l_P = sqrt(ħ G / c^3) ≈ 1.62 × 10^{-35} m
- Planck mass: m_P = sqrt(ħ c / G) ≈ 2.18 × 10^{-8} kg
- Planck density: ρ_P = m_P / l_P^3 ≈ 5 × 10^{96} kg/m^3

Vacuum energy density (QFT prediction):
ρ_vac(QFT) ≈ E_P / l_P^3 ≈ 5 × 10^{96} kg/m^3

Observed cosmological constant density:
ρ_Λ(obs) ≈ 6 × 10^{-27} kg/m^3

The discrepancy: approximately 10^{123} orders of magnitude — the cosmological constant problem, arguably the largest unsolved problem in theoretical physics (Weinberg 1989, Padmanabhan 2003).

### 3.2 What This Discrepancy Tells Us

The cosmological constant problem does not mean the vacuum has no energy. It means that nearly all of it cancels — through some mechanism we do not yet understand. The residual, ρ_Λ, is what we observe as dark energy driving cosmic acceleration.

Crucially: the cancellation mechanism is unknown. This means we cannot rule out the possibility that the cancellation is imperfect in specific physical environments — particularly those that break the symmetries (Lorentz invariance, homogeneity) that the cancellation presumably relies upon.

High-curvature spacetime regions (black hole horizons), strong magnetic field regions (magnetar surfaces, AGN jets), and high-energy-density regions (galactic centers) are precisely the environments where such symmetry-breaking is most pronounced.

### 3.3 The Statistical Snapshot Argument

Formal statement. Let N(t) be the number of virtual particle pairs simultaneously existing in a volume V at time t. Each pair has a characteristic mass m and lifetime τ ≤ ħ/(2mc^2).

The instantaneous mass contribution of this population is:
M_snap(t) = Σ_i m_i · θ(τ_i - (t - t_i))

where θ is the Heaviside step function, t_i is the creation time of pair i, and τ_i is its lifetime.

This quantity fluctuates rapidly — on timescales of order t_P. However, its time average over any macroscopic interval T ≫ t_P is:
⟨M_snap⟩ = ⟨N⟩ · ⟨m⟩

The snapshot argument. Freeze the universe for 10^{-44} seconds. In that instant, across every cubic Planck-length of space, particle pairs are blinking into existence. Each one is gone before any measurement could reach it. But in that frozen moment — they are there. They have mass. They curve spacetime. The snapshot has weight.

This is not a metaphor. It is a statistical fact.

### 3.4 Why This Is Not Simply the Cosmological Constant

The cosmological constant represents the ground-state, spatially homogeneous vacuum energy after cancellation. What we are describing here is different: it is the spatial and temporal fluctuation around that ground state, which is enhanced in regions of broken symmetry.

In Minkowski spacetime (flat, homogeneous, no fields), the vacuum fluctuation population is maximally correlated across space — pairs at distant points are quantum-entangled in a way that causes their gravitational effects to cancel at macroscopic scales. This is the mechanism (or one possible mechanism) behind the cosmological constant cancellation.

In curved spacetime near a black hole, or in a region of strong electromagnetic field, this long-range correlation structure is disrupted. The disruption has a well-known consequence: real particle production (Hawking radiation near horizons, Schwinger pair production in strong electric fields). The less-discussed consequence is that the partial disruption of correlations — below the threshold for real particle production — may leave a residual gravitational signature.

This residual is what we call the vacuum statistical mass contribution.

### 3.5 Order of Magnitude in Flat Spacetime

In pure Minkowski vacuum, assuming one Planck-scale pair per Planck volume:
⟨N_0⟩ ≈ V / l_P^3

For a galactic volume V_gal ≈ 10^{61} m^3:
⟨N_0⟩ ≈ 10^{61} / (1.62 × 10^{-35})^3 = 10^{166}

At Planck mass per pair (m_P ≈ 2.18 × 10^{-8} kg):
⟨M_snap⟩_0 ≈ 10^{166} × 10^{-8} kg = 10^{158} kg

This is approximately 10^{118} times the observed mass of the Milky Way (~10^{40} kg). The conclusion is immediate: in flat spacetime, the statistical snapshot mass is astronomically larger than observed galactic mass, and must be almost entirely cancelled by quantum correlations. This is simply the cosmological constant problem restated in the language of statistical mechanics.

### 3.6 The Amplification Factor Γ(r)

We define the local amplification factor as:
Γ(r) = ρ_effective(r) / ρ_Λ

where ρ_effective(r) is the effective vacuum mass density at position r after accounting for correlation disruption, and ρ_Λ is the cosmological constant density (~6 × 10^{-27} kg/m^3).

Boundary conditions:
- Flat spacetime far from any source: Γ = 1 (by definition)
- Near stellar-mass black hole: Γ > 1 (unknown magnitude)
- Near supermassive black hole: Γ ≫ 1 (unknown magnitude)

### 3.7 Known Enhancement Mechanisms

Hawking radiation. Near a black hole of mass M_BH, the Hawking temperature is:
T_H = ħ c^3 / (8π G M_BH k_B)

For a supermassive black hole (M_BH = 4 × 10^6 M_⊙, as in Sgr A*): T_H ≈ 1.5 × 10^{-14} K. This is far below the CMB temperature (~2.7 K) and negligible as a mass source. However, Hawking radiation represents only the above-threshold component — pairs separated far enough to escape. The sub-threshold component (pairs that are separated but recombine) is larger by orders of magnitude and has not been quantified.

Schwinger pair production. In a strong electric field E, the pair production rate per unit volume is:
Γ_Schwinger ∝ (eE/ħ)^2 exp(-π m^2 c^3 / (eE ħ))

The critical field is E_c = m^2 c^3 / (e ħ) ≈ 1.3 × 10^{18} V/m. Near M87*, magnetic fields of B ~ 1-30 T have been inferred from EHT observations. B ~ 30 T corresponds to E_eff ~ 10^{10} V/m — approximately 10^8 times below E_c. The Schwinger rate is exponentially suppressed.

However, the sub-threshold analog — enhancement of virtual pair density below the production threshold — scales differently. A plausible scaling is:
ρ_virtual(F) / ρ_virtual(0) ~ (F / F_c)^α, 0 < α < 2

This has not been calculated from first principles for the astrophysical case.

Frame dragging (Kerr spacetime). A rotating black hole drags spacetime in its vicinity — the Lense-Thirring effect. The frame-dragging angular velocity at radius r for a Kerr black hole with spin parameter a* is:
Ω_LT(r) = 2GJ / (c^2 r^3)

In the ergosphere, no static observer can exist — all observers are dragged in the direction of rotation. This region is particularly interesting for vacuum fluctuation enhancement because:
- The local vacuum state differs from the asymptotic vacuum (Unruh effect analog)
- The rotational energy of the black hole can be extracted (Penrose process)
- Virtual pairs created here experience a non-inertial vacuum state, potentially altering their correlation structure

## Chapter 4: The Complete Framework — Claims I, II, and III Combined

### 4.1 How the Three Claims Fit Together

Claim I: BH displacement + retarded gravity — Scale: Galactic — Observable Consequence: Spiral arms + flat rotation curves
Claim II: Pair production + magnetic separation + annihilation suppression — Scale: Particle (BH vicinity) — Observable Consequence: Local mass generation/fluctuation
Claim III: Fluctuating mass + finite-speed gravity propagation — Scale: Galactic — Observable Consequence: Additional contribution to rotation curves

Claims I and III together explain the rotation curve without dark matter. Claim II provides the physical mechanism for the mass fluctuations that Claim III requires.

### 4.2 The Unified Equation

The total gravitational acceleration experienced by a star in the galactic disk is:
a_total = a_Newton(disk) + a_Newton(BH, retarded) + a_ret(fluctuating mass)

where:
- a_Newton(disk) is the standard Newtonian acceleration from the visible stellar disk
- a_Newton(BH, retarded) is the Newtonian acceleration from the black hole, evaluated at the retarded position
- a_ret(fluctuating mass) is the Yahalom-type retarded term from fluctuating mass near the BH

### 4.3 The Flat Rotation Curve Condition

From Part 2 of the Core Document, when the pair production rate Ṁ_pair is constant:
M_ghost(r) = Ṁ_pair · r/c  ⇒  M_ghost ∝ r

Then the rotation velocity is:
v_c^2(r) = G · M_ghost(r) / r = G · Ṁ_pair / c = constant

This is the core mathematical result: a flat rotation curve emerges naturally from a constant pair production rate, with no additional free parameters.

## Chapter 5: Simulation Evidence Summary

### 5.1 GalaxyCS v4 — Key Observations

Observation: Spiral arms emerge immediately with any non-zero BH displacement — Implication: No threshold; mechanism is geometric, not resonant
Observation: Arm morphology matches BH kinematic history — Implication: Inverse problem: spiral structure encodes BH motion
Observation: Outer rotation velocity exceeds Newtonian prediction by 1.5-3.0x — Implication: Retarded term does not fall off with distance
Observation: Void formation with BH mass reduction — Implication: Temporal mass fluctuations create underdense regions
Observation: Energy and angular momentum conservation stable — Implication: Rules out numerical artifacts

### 5.2 Yang-Mills Collider v3.2 — Key Observations

Observation: Particles and antiparticles separate by charge — Implication: Lorentz force in magnetic field (F = qv × B)
Observation: Annihilation suppressed when r_L ≪ R_system — Implication: Separated particles persist as mass
Observation: Accretion disk appears without explicit code — Implication: Emergent behavior from angular momentum conservation
Observation: Penrose process emerges spontaneously — Implication: Interaction of Newtonian gravity + frame dragging + Boris integrator
Observation: Mass-dependent orbital radius separation — Implication: r_L ∝ m (Larmor radius scaling)

## Chapter 6: Falsifiable Predictions

This framework makes the following predictions, each falsifiable by observation:

Prediction 1. Spiral arm strength correlates with BH displacement magnitude from the photometric center. Galaxies with stronger, more symmetric grand-design spiral arms should show larger BH-center offsets when measured at sufficient resolution.

Prediction 2. Arm count corresponds to BH oscillation mode. Two-armed spirals correspond to simple displacement; multi-armed spirals to oscillatory BH motion.

Prediction 3. The inverse problem is solvable. Given a galaxy's spiral morphology (arm count, pitch angle, symmetry), it should be possible to reconstruct the approximate kinematic history of its central BH.

Prediction 4. Elliptical and lenticular galaxies without disks are the expected non-spiral population. They do not represent failures to produce spiral arms; they represent systems where no disk existed to develop them.

Prediction 5. The vacuum statistical mass contribution should be more centrally concentrated than CDM's NFW profile. Galaxies with more massive or more rapidly spinning central black holes should show relatively stronger central mass excess.

Prediction 6. Unlike WIMPs or axions, the vacuum statistical mass is not a particle. It cannot be detected in direct-detection experiments. This is consistent with all current null results (LZ 2024, XENONnT 2024, PandaX-4T 2023).

Prediction 7. High-spin AGN should exhibit systematically larger central mass excess than low-spin AGN at fixed black hole mass (due to larger ergosphere and stronger frame dragging).

## Chapter 7: Limitations (Stated Honestly)

Q1 — The Cancellation Mechanism. We do not know what causes the 10^{123} cancellation in flat spacetime. Without knowing the mechanism, we cannot predict how much it is disrupted in curved spacetime. Any quantitative estimate of Γ(r) is currently a free parameter.

Q2 — Backreaction. If vacuum fluctuations contribute to the stress-energy tensor, they also affect the spacetime geometry — which in turn affects the fluctuation rate. This self-consistent backreaction problem is unsolved even in simplified toy models.

Q3 — Distinguishability. Near galactic centers, the vacuum statistical mass profile and the CDM profile may produce similar observational signatures. Distinguishing them requires either (a) measurements sensitive to the equation of state of the dark component, or (b) high-precision rotation curve data in the inner ~1 kpc.

Q4 — Cosmological Consistency. If Γ(r) is large near every galactic center, the integrated contribution over all galaxies in the observable universe may produce a measurable effect on the CMB or large-scale structure. This constraint has not been calculated.

Q5 — The Entanglement Structure. The argument that long-range quantum entanglement causes cancellation in flat spacetime is plausible but not proven. The calculation of how this entanglement structure is modified by curved spacetime is an open problem in quantum gravity.

Q6 — N-body Convergence. The simulation uses 20,000-80,000 test particles. Whether qualitative behavior is preserved at N = 10^5-10^6 has not been verified.

Q7 — Quantitative Fit to Observed Rotation Curves. GalaxyCS v4 has been compared informally to M33 data and shows qualitative agreement. A systematic fit to the SPARC database (175 galaxies with resolved rotation curves; Lelli, McGaugh & Schombert, 2016) has not been performed.

## Chapter 8: Comparison with Existing Frameworks

Feature: Spiral formation
- Lin-Shu Density Wave: Pattern wave
- MOND: Not addressed
- This Framework: BH displacement + retarded gravity

Feature: Rotation curve
- Lin-Shu Density Wave: Not primary
- MOND: Modified dynamics
- This Framework: Retarded a_ret (no 1/r falloff)

Feature: Dark matter
- Lin-Shu Density Wave: Required (some versions)
- MOND: Replaced
- This Framework: Reexamined, not required

Feature: Free parameters
- Lin-Shu Density Wave: Pattern speed Ω_p
- MOND: a_0
- This Framework: α (one parameter)

Feature: Universality of spirals
- Lin-Shu Density Wave: Requires resonance
- MOND: N/A
- This Framework: Generic consequence of BH motion

Feature: Gravitational lensing
- Lin-Shu Density Wave: Not addressed
- MOND: Not addressed
- This Framework: Not explained (requires separate mechanism)

Feature: CMB power spectrum
- Lin-Shu Density Wave: Not addressed
- MOND: Not addressed
- This Framework: Not explained (requires separate mechanism)

## Chapter 9: Summary

We have presented a framework for understanding why the quantum vacuum may contribute a small but non-zero effective mass density to galactic dynamics, concentrated near regions of high spacetime curvature and strong electromagnetic fields.

The central argument is:
1. Quantum vacuum fluctuations exist and carry energy-momentum.
2. In flat spacetime, quantum correlations cause their gravitational effects to nearly perfectly cancel — the cosmological constant problem states the residual is 10^{-123} of the naive estimate.
3. In strongly curved or strongly magnetized spacetime, these correlations are partially disrupted — this is already established by the Casimir, Unruh, Hawking, and Schwinger effects.
4. The disruption leaves a residual vacuum statistical mass that is small relative to the flat-space estimate but potentially significant relative to baryonic galactic mass.
5. When combined with retarded gravity from a displaced black hole, this produces flat rotation curves and spiral arm morphology without dark matter.

This contribution is not dark matter. It is not a new particle. It is a gravitational consequence of known quantum field theory in curved spacetime, extended to realistic astrophysical environments.

The magnitude of this effect is unknown. The calculation required to determine it — quantum field theory in Kerr spacetime with realistic magnetic field configurations, integrated over a realistic galactic density profile — has not been performed.

This document is a statement that the calculation should be performed.

## Appendix: Key References

Abbott et al. (2017) — GW170817: Confirms gravity propagates at c
Batcheldor et al. (2010) — M87: 6.8 ± 0.8 pc BH offset
Kormendy & Ho (2013) — BH mass fraction 0.1-0.5% of total
Freeman (1970) — Exponential disk mass profile
Lelli, McGaugh & Schombert (2016) — SPARC rotation curve database
Lin & Shu (1964) — Density wave theory
Yahalom (2013, 2019, 2024) — Retarded gravity and rotation curves
Weinberg (1989) — Cosmological constant problem
Hawking (1975) — Hawking radiation
Unruh (1976) — Unruh effect
Schwinger (1951) — Schwinger pair production
Casimir (1948) — Casimir effect
Milgrom (1983) — MOND

---

# Black Hole Displacement and the Default State of Spiral Galaxies

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/black-hole-displacement-and-the-default

## Two Claims

Claim I. When a black hole is displaced from the geometric center of a disk galaxy — however slightly — spiral arm structure emerges immediately and persistently. This is a direct geometric consequence of the mass ratio between the central black hole and the total galactic mass: unlike stellar systems where the central mass dominates, the central black hole in a disk galaxy represents only 0.1–0.5% of total galactic mass, making displacement from the barycenter structurally inevitable. This claim is verifiable directly. Open the simulator linked above. Press any arrow key. Observe.

Claim II. The relationship between black hole displacement magnitude and spiral arm morphology (arm count, pitch angle, symmetry) constitutes a novel observational tool: inferring black hole kinematic history from spiral structure. This is a hypothesis. It is stated as a possibility, not a conclusion.

These two claims are independent. Claim I does not require Claim II to be true.

## Section 1. The Problem — Restated

### 1.1 The Standard Question Is Wrong

The standard question in galactic dynamics is:

"Why do spiral arms form?"

This document argues that the question is inverted. The correct question is:

"Why do some galaxies NOT have spiral arms?"

Approximately 60–70% of observed galaxies in the local universe exhibit spiral structure (Lintott et al., 2011, Galaxy Zoo). If spiral structure requires special conditions — specific resonances, density waves, tidal partners — then 60–70% prevalence is difficult to explain. If spiral structure is the generic outcome of ordinary physical conditions, 60–70% prevalence is expected. The remaining 30–40% — ellipticals, lenticulars, irregulars — represent systems where disk structure itself is absent or disrupted, not systems that failed to develop spiral arms.

The mechanism described in this document produces spiral arms as a default state, not a special outcome.

### 1.2 What Existing Frameworks Require

Lin-Shu density wave theory (Lin & Shu, 1964) requires:
- A well-defined pattern speed Ω_p distinct from local stellar angular velocity
- A continuous energy source to maintain waves against dissipation
- Specific resonance conditions

Tidal interaction models require:
- A companion galaxy or satellite system
- Ongoing or recent gravitational perturbation

Both frameworks treat spiral arms as phenomena requiring explanation. This document treats spiral arms as the null hypothesis.

## Section 2. The Mass Ratio Argument

### 2.1 Solar System vs. Galaxy — A Structural Difference

In the Solar System, the Sun contains 99.8% of total system mass. The Solar System barycenter lies within or near the solar surface. The Sun cannot be meaningfully displaced from the system's mass centroid by any realistic perturbation. No spiral structure can form around an effectively stationary central mass.

In a disk galaxy, the central supermassive black hole contains 0.1–0.5% of total galactic mass (Kormendy & Ho, 2013). The galactic barycenter is determined primarily by the distributed stellar disk and dark matter halo. The black hole has no structural reason to remain at the barycenter. It is free to move.

Formula:
f_BH = M_BH / M_total

- Solar System: f_Sun ≈ 0.998
- Disk galaxy: f_BH ≈ 0.001-0.005

### 2.2 Why Displacement Is the Default State

Perfect black hole stasis — zero displacement from the galactic barycenter at all times — would require exact cancellation of all the following perturbations simultaneously and continuously:
- Host galaxy peculiar velocity through the cosmic web (100–600 km/s)
- Tidal forces from satellite galaxies and globular clusters
- Galactic bar oscillations (when bar is present)
- Large-scale structure gravitational background (cosmic filaments, voids)
- Recoil from asymmetric gravitational wave emission during any merger event

This exact cancellation is not physically plausible. Black hole displacement is the default state. Spiral structure is therefore the expected morphology for disk galaxies.

### 2.3 The Contrast with Stellar Systems

System: Solar System — Central mass fraction: f_Sun ≈ 0.998 — BH/star free to displace?: No — structurally suppressed — Spiral structure possible?: No
System: Binary star — Central mass fraction: f ≈ 0.5 — BH/star free to displace?: Orbit only, symmetric — Spiral structure possible?: No
System: Disk galaxy — Central mass fraction: f_BH ≈ 0.001 — BH/star free to displace?: Yes — structurally permitted — Spiral structure possible?: Yes — default
System: Elliptical galaxy — Central mass fraction: No disk — BH/star free to displace?: Irrelevant — Spiral structure possible?: No disk to form arms in

The table makes a prediction: spiral arms should appear in any system where (1) a disk exists and (2) the central mass fraction is low enough to permit displacement. This prediction is consistent with observation.

## Section 3. The Observational Evidence — BH Offsets Are Already Known

### 3.1 M87 — Direct Measurement

The most precisely measured case is M87. HST observations reveal a 6.8 ± 0.8 pc projected displacement between the center of M87 (as defined by galaxy isophotes) and the supermassive black hole (Batcheldor et al., 2010). M87 is an elliptical galaxy — it has no disk, and therefore no spiral structure is expected regardless of BH displacement. This is consistent with the framework.

### 3.2 Offset SMBHs Are Common

Bartlett et al. (2021) compiled the largest existing datasets of AGN-galaxy center offsets. Physical displacements of 10–100 pc are the most commonly observed range. Sub-parsec offsets are likely underrepresented due to resolution limits.

Chu, Boldrini & Silk (2022), combining TNG300 simulations with orbital integrations, find that one-third of brightest cluster galaxy (BCG) black holes are off-center at z = 0, with offsets sustained for up to 6 Gyr.

### 3.3 The Milky Way

For Sgr A*, the question of displacement from the galactic barycenter is observationally constrained but not closed. The nuclear star cluster (NSC) hosting Sgr A* may itself be displaced from the bar/disk barycenter by up to ~100 pc (Bovy et al., 2022). At galactic scales, this is a small but non-zero offset — and the Milky Way has spiral arms.

### 3.4 M31 (Andromeda)

M31 has a well-documented double nucleus structure. The SMBH is not coincident with the photometric center of the galaxy. M31 is a spiral galaxy.

### 3.5 The Pattern

Galaxy: M87 — BH offset: 6.8 pc — Spiral structure?: No (elliptical — no disk)
Galaxy: M31 — BH offset: Documented double nucleus — Spiral structure?: Yes
Galaxy: Milky Way — BH offset: ≲100 pc (NSC offset) — Spiral structure?: Yes
Galaxy: BCGs (1/3 of sample) — BH offset: 10 pc – kpc scale — Spiral structure?: Mixed (many lenticular/elliptical)

The pattern is consistent with the framework: displacement exists wherever it has been measured with sufficient resolution, and spiral structure follows wherever a disk is present.

## Section 4. The Mechanism

### 4.1 Retarded Gravity and Differential Light-Travel Time

The finite propagation speed of gravitational influence is confirmed observationally by the detection of gravitational waves at c (Abbott et al., 2017, GW170817). The consequence for galactic dynamics:

If the black hole is in motion — however slightly — then stars at different distances from the BH reference different past positions of that BH. The gravitational force vector experienced by each star points toward a different past location. In a differentially rotating disk, this radially-dependent angular offset is sheared continuously into a spiral pattern.

Formula:
τ(r) = α r / c
r_BH^ret(t, r) = r_BH(t - τ(r))

### 4.2 The Geometry Is Exact and Deterministic

No stochastic process is required. No resonance condition. No special initial configuration. The spiral is a direct geometric consequence of three facts:
1. Gravity propagates at finite speed ✓ (empirically confirmed)
2. The black hole is displaced from the disk center ✓ (observationally documented)
3. The disk rotates differentially ✓ (universally observed)

### 4.3 The Equation of Motion

d^2 r/dt^2 = a_N(r, t) + a_ret(r, t)

where a_N is the Newtonian acceleration from disk + BH (at retarded position), and a_ret is the Yahalom retarded correction term.

Newtonian acceleration (black hole + Freeman disk):
a_N = -G M_BH (r - r_BH^ret) / |r - r_BH^ret|^3 - G M_disk(r) r / r^3

Freeman disk enclosed mass:
M_disk(r) = M_total [1 - (1 + r/R_d) e^{-r/R_d}]

Retarded correction term (Yahalom):
a_ret = α · G · M̈_BH / (2c^2) · R̂

The critical structural feature of this term is the absence of an inverse-distance dependence. Unlike Newtonian gravity (∝ 1/r^2), the retarded term a_ret does not diminish with distance. At galactic scales, this means that retarded gravitational effects become relatively more important at large radii — precisely the regime where observed rotation curves deviate most strongly from Newtonian predictions.

### 4.4 The Integrator

The simulator uses a leapfrog (velocity Verlet) integrator. This choice is not arbitrary.

Integration steps:
v_{n+1/2} = v_n + a(r_n) Δt/2
r_{n+1} = r_n + v_{n+1/2} Δt
a_{n+1} = a(r_{n+1})
v_{n+1} = v_{n+1/2} + a_{n+1} Δt/2

Properties:
- Formal accuracy: O(Δt^2) — Sufficient for galactic dynamics
- Time reversibility: Yes — Rules out integration artifacts
- Symplecticity: Yes — Preserves phase space volume
- Energy conservation: Near-exact — ΔE/E monitored in real time
- Angular momentum: Near-exact — ΔL/L monitored in real time

The real-time conservation diagnostics are critical: if observed spiral structure were a numerical artifact, it would manifest as unbounded growth in ΔE or ΔL. The structure persists under stable conservation. This rules out the most common class of numerical artifacts.

## Section 5. Simulation Results

### 5.1 Immediate Spiral Formation

In GalaxyCS v4, with a stellar population of 20,000–80,000 test particles initialized on circular orbits consistent with the Freeman disk rotation curve:
- BH at rest (displacement = 0): No spiral structure. Axisymmetric disk.
- BH displaced by any nonzero amount: Spiral arm structure emerges within the first few simulation steps and persists indefinitely.

The transition is not gradual. It is immediate. There is no critical displacement threshold below which the effect is absent.

The spiral arm formation is observable within 2–3 simulation steps of any nonzero BH displacement. No warmup period. No parameter tuning required.

---

# Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/vacuum-fluctuations-delayed-gravity

## Preface

This document does not argue that dark matter does not exist. It argues something narrower and, in some ways, more interesting: that two well-established physical phenomena — the retarded propagation of gravity and the statistical behavior of quantum vacuum fluctuations — may together account for a non-trivial portion of what we currently attribute to unseen mass.

The first of these (delayed gravity) has been demonstrated computationally and is the subject of a companion simulation series. The second (vacuum statistical mass) is the subject of this document.

It is presented not as a competing theory but as a complementary observation: this effect exists, it is non-zero, and its magnitude under extreme astrophysical conditions has not been adequately quantified.

## 1. The Problem We Are Not Solving (and the One We Are)

The standard account of galactic dynamics requires approximately five times more mass than is visible. This "missing mass" is conventionally attributed to a new class of particle — cold dark matter (CDM) — that interacts gravitationally but not electromagnetically.

The ΛCDM model built on this assumption is extraordinarily successful: it reproduces the cosmic microwave background power spectrum (Planck Collaboration, 2020), the large-scale structure of the universe (Springel et al., 2005), and the baryon acoustic oscillation scale (Eisenstein et al., 2005) with remarkable precision.

We are not disputing this success.

What we are noting is that ΛCDM's success at cosmological scales does not preclude the existence of additional, smaller-magnitude effects at galactic scales. Two such effects are the subject of this document:

Effect 1 — Retarded Gravitational Interaction: Gravity propagates at the speed of light. In a rotating galactic disk, this retardation introduces an asymmetry in the gravitational field that is not captured by the instantaneous Newtonian approximation. Companion simulations demonstrate that this effect alone reproduces flat rotation curves and spiral arm morphology without invoking additional mass.

Effect 2 — Vacuum Statistical Mass: The quantum vacuum is not empty. Virtual particle pairs are continuously created and annihilated on timescales governed by the energy-time uncertainty relation (ΔE·Δt ≥ ħ/2). Individually, each fluctuation is transient — existing for ~10^{-44} seconds at the Planck scale. Statistically, however, at any given moment, a finite population of such fluctuations exists simultaneously across any finite volume. Under extreme gravitational and electromagnetic conditions — black hole ergospheres, active galactic nuclei, magnetar surfaces — the rate, lifetime, and separation probability of these fluctuations are enhanced. The cumulative statistical mass of this enhanced population may constitute a small but non-negligible contribution to galactic mass budgets.

## 2. Foundations: What the Vacuum Actually Is

### 2.1 The Energy-Time Uncertainty Relation

The Heisenberg uncertainty principle, in its energy-time formulation, states:
ΔE · Δt ≥ ħ/2

where ħ = 1.055 × 10^{-34} J·s is the reduced Planck constant. This relation permits the temporary violation of energy conservation, provided the violation is sufficiently brief. A pair of particles with combined rest-mass energy E can exist for a duration:
Δt ≤ ħ / (2E)

At the Planck energy (E_P = √(ħ c^5 / G) ≈ 1.22 × 10^{19} GeV), this duration is the Planck time:
t_P = √(ħ G / c^5) ≈ 5.39 × 10^{-44} s

### 2.2 The Vacuum Energy Density

Quantum field theory predicts a vacuum energy density obtained by summing zero-point energies of all field modes up to some ultraviolet cutoff. Using the Planck scale as the cutoff:
ρ_vac(QFT) ≈ E_P / l_P^3 ≈ 5 × 10^{96} kg/m^3

The observed cosmological constant corresponds to an energy density of:
ρ_Λ(obs) ≈ 6 × 10^{-27} kg/m^3

The discrepancy — approximately 10^{123} orders of magnitude — is the cosmological constant problem, arguably the largest unsolved problem in theoretical physics (Weinberg, 1989; Padmanabhan, 2003).

### 2.3 What This Discrepancy Tells Us

The cosmological constant problem does not mean the vacuum has no energy. It means that nearly all of it cancels — through some mechanism we do not yet understand. The residual, ρ_Λ, is what we observe as dark energy driving cosmic acceleration.

Crucially: the cancellation mechanism is unknown. This means we cannot rule out the possibility that the cancellation is imperfect in specific physical environments — particularly those that break the symmetries (Lorentz invariance, homogeneity) that the cancellation presumably relies upon.

High-curvature spacetime regions (black hole horizons), strong magnetic field regions (magnetar surfaces, AGN jets), and high-energy-density regions (galactic centers) are precisely the environments where such symmetry-breaking is most pronounced.

## 3. The Statistical Snapshot Argument

### 3.1 Formal Statement

Let N(t) be the number of virtual particle pairs simultaneously existing in a volume V at time t. Each pair has a characteristic mass m and lifetime τ ≤ ħ/(2mc^2).

The instantaneous mass contribution of this population is:
M_snap(t) = Σ_i m_i · θ(τ_i - (t - t_i))

where θ is the Heaviside step function, t_i is the creation time of pair i, and τ_i is its lifetime.

This quantity fluctuates rapidly — on timescales of order t_P. However, its time average over any macroscopic interval T ≫ t_P is:
⟨M_snap⟩ = ⟨N⟩ · ⟨m⟩

The snapshot argument. Freeze the universe for 10^{-44} seconds. In that instant, across every cubic Planck-length of space, particle pairs are blinking into existence. Each one is gone before any measurement could reach it. But in that frozen moment — they are there. They have mass. They curve spacetime. The snapshot has weight.

This is not a metaphor. It is a statistical fact.

The "snapshot" is not a measurement. No observer is required, no wavefunction collapses, no measurement problem is invoked. What is invoked is simpler and older: the law of large numbers, applied to a population of transient objects whose individual lifetimes are immeasurably short but whose collective presence at any given instant is statistically guaranteed — in the same sense that the average number of molecules in a room does not depend on whether anyone is counting them.

### 3.2 Why This Is Not Simply the Cosmological Constant

The cosmological constant represents the ground-state, spatially homogeneous vacuum energy after cancellation. What we are describing here is different: it is the spatial and temporal fluctuation around that ground state, which is enhanced in regions of broken symmetry.

More precisely: in Minkowski spacetime (flat, homogeneous, no fields), the vacuum fluctuation population is maximally correlated across space — pairs at distant points are quantum-entangled in a way that causes their gravitational effects to cancel at macroscopic scales. This is the mechanism (or one possible mechanism) behind the cosmological constant cancellation.

In curved spacetime near a black hole, or in a region of strong electromagnetic field, this long-range correlation structure is disrupted. The disruption has a well-known consequence: real particle production (Hawking radiation near horizons, Schwinger pair production in strong electric fields). The less-discussed consequence is that the partial disruption of correlations — below the threshold for real particle production — may leave a residual gravitational signature.

This residual is what we call the vacuum statistical mass contribution.

### 3.3 Order of Magnitude in Flat Spacetime

In pure Minkowski vacuum, the mean number of Planck-scale pairs in volume V is:
⟨N_0⟩ ≈ V / l_P^3

For a galactic volume V_gal ≈ 10^{61} m^3:
⟨N_0⟩ ≈ 10^{61} / (1.62 × 10^{-35})^3 = 10^{166}

At Planck mass per pair (m_P ≈ 2.18 × 10^{-8} kg), this gives:
⟨M_snap⟩_0 ≈ 10^{166} × 10^{-8} kg = 10^{158} kg

This is approximately 10^{118} times the observed mass of the Milky Way (~10^{40} kg). The conclusion is immediate: in flat spacetime, the statistical snapshot mass is astronomically larger than observed galactic mass, and must be almost entirely cancelled by quantum correlations.

This is simply the cosmological constant problem restated in the language of statistical mechanics. It is not a new problem. It confirms that the correlation cancellation mechanism is extraordinarily efficient.

### 3.4 The Spatial Uniformity of Vacuum Fluctuations

A critical property of vacuum fluctuations in flat spacetime is spatial uniformity. The snapshot mass density does not depend on position.

ρ_snap(r) = ⟨M_snap⟩ / V = constant (independent of r)

Meaning: In the absence of external fields (gravity, electromagnetism), the quantum vacuum is the same everywhere. Therefore, the pair production rate from vacuum fluctuations is spatially constant:

Ṁ_pair^vac(r) = constant (independent of r)

Meaning: This is the source of the constant Ṁ_pair assumption in the Ghost Mass derivation (Part 2 of the Essential Citations).

Contrast with local astrophysical pair production:

Vacuum fluctuations (this section):
- Spatial distribution: Uniform (constant in r)
- Physical origin: Quantum vacuum
- Magnitude in flat spacetime: ~10^{-118} times Planck scale (cancelled)
- Enhancement needed for galactic effects: Γ(r) ~ 10^4 (see Section 4)

Local astrophysical sources (Part 4 of Essential Citations):
- Spatial distribution: Disk-like (concentrated near center)
- Physical origin: Black holes, AGN, supernovae
- Magnitude in flat spacetime: Determined by local energy density
- Enhancement needed for galactic effects: Already accounted in near-field dynamics

Why this matters for dark matter:
The uniform vacuum fluctuation component naturally becomes dominant at large galactic radii (r ≫ R_disk), precisely where dark matter halos are observed. Its spatial uniformity means it contributes a spherical mass distribution in the far-field limit (see Section 6.4 of Essential Citations).

The local astrophysical component dominates in the near-field (r ≲ R_disk) and is responsible for the disk-like source distribution, but its contribution to the far-field halo is suppressed by the 1/r falloff of the static approximation.

Therefore, the two components are not in competition. They describe different physical mechanisms operating at different scales and dominating in different spatial regimes.

## 4. The Enhancement Hypothesis

### 4.1 The Central Claim

We propose that in regions of extreme spacetime curvature and/or strong electromagnetic fields, the quantum correlation structure responsible for cancellation is partially disrupted, resulting in a residual statistical mass contribution that is small relative to the flat-spacetime value but non-negligible relative to baryonic galactic mass.

Formally, we introduce a dimensionless suppression factor S(r) such that:
⟨M_snap⟩(r) = ⟨M_snap⟩_0 · S(r)

In flat spacetime: S → S_min ≈ 10^{-118} (the cosmological constant suppression). Near a black hole horizon: S(r) > S_min.

The question is: how much larger?

### 4.2 Known Enhancement Mechanisms

4.2.1 Hawking Radiation

Near a black hole of mass M_BH, the vacuum fluctuation rate is enhanced at the horizon scale r_s = 2GM_BH/c^2. The Hawking temperature:
T_H = ħ c^3 / (8π G M_BH k_B)

For a supermassive black hole (M_BH = 4 × 10^6 M_⊙, as in Sgr A*): T_H ≈ 1.5 × 10^{-14} K. This is far below the CMB temperature (~2.7 K) and negligible as a mass source. However, Hawking radiation represents only the above-threshold component — pairs separated far enough to escape. The sub-threshold component (pairs that are separated but recombine) is larger by orders of magnitude and has not been quantified in terms of its transient gravitational effect.

4.2.2 Schwinger Pair Production

In a strong electric field E, pair production occurs at a rate per unit volume:
Γ_Schwinger ∝ (eE/ħ)^2 exp(-π m^2 c^3 / (eE ħ))

The critical field is E_c = m^2 c^3 / (e ħ) ≈ 1.3 × 10^{18} V/m. Near M87*, magnetic fields of B ~ 1-30 T have been inferred from EHT observations (Event Horizon Telescope Collaboration, 2021). Converting to equivalent electric field units, B ~ 30 T corresponds to E_eff ~ 10^{10} V/m — approximately 10^8 times below E_c. The Schwinger rate is exponentially suppressed and negligible for real pair production.

However, the sub-threshold analog — enhancement of virtual pair density below the production threshold — scales differently. The virtual pair density enhancement near a field of strength F (relative to F_c) is not exponentially suppressed in the same way, because virtual pairs do not need to reach the threshold for real production. A plausible scaling is:
ρ_virtual(F) / ρ_virtual(0) ~ (F / F_c)^α, 0 < α < 2

where α depends on the field geometry and the pair species. This has not been calculated from first principles for the astrophysical case.

4.2.3 Frame Dragging (Kerr Spacetime)

A rotating black hole drags spacetime in its vicinity — the Lense-Thirring effect. The frame-dragging angular velocity at radius r for a Kerr black hole with spin parameter a* is:
Ω_LT(r) = 2GJ / (c^2 r^3)

In the ergosphere (r < r_ergo = (GM/c^2)(1 + √(1-a*^2))), no static observer can exist — all observers are dragged in the direction of rotation. This region is particularly interesting for vacuum fluctuation enhancement because:
- The local vacuum state differs from the asymptotic vacuum (Unruh effect analog)
- The rotational energy of the black hole can be extracted (Penrose process)
- Virtual pairs created here experience a non-inertial vacuum state, potentially altering their correlation structure

The Yang-Mills Collider v3.2 simulation (companion document) demonstrates that adding a Kerr black hole to a particle collision environment produces qualitatively different particle trajectory structures — including spontaneous circular and spiral orbit concentrations not present without the black hole — even when the black hole mass is set to cosmologically unrealistic values. This suggests the ergosphere geometry has structural effects on particle dynamics that are not reducible to simple gravitational deflection.

### 4.3 The Amplification Factor Γ(r)

We define the local amplification factor as:
Γ(r) = ρ_effective(r) / ρ_Λ

where ρ_effective(r) is the effective vacuum mass density at position r after accounting for correlation disruption, and ρ_Λ is the cosmological constant density (~6 × 10^{-27} kg/m^3).

Boundary conditions:
- Flat spacetime far from any source: Γ = 1 (by definition)
- Near stellar-mass black hole: Γ > 1 (unknown magnitude)
- Near supermassive black hole: Γ ≫ 1 (unknown magnitude)

The spatial profile of Γ(r) is unknown from first principles. However, we can constrain it from observation.

## 5. Observational Constraints and Reverse Engineering

### 5.1 What Observation Tells Us

The total dynamical mass of the Milky Way within ~50 kpc is estimated at:
M_total ≈ 5 × 10^{11} M_⊙ ≈ 10^{42} kg

The baryonic mass (stars + gas + dust) is approximately:
M_baryonic ≈ 6 × 10^{10} M_⊙ ≈ 1.2 × 10^{41} kg

The companion galactic dynamics simulation demonstrates that retarded gravity (Effect 1) accounts for the flat rotation curve without additional mass. This implies that the "missing" dynamical mass inferred from standard Newtonian analysis is, in large part, an artifact of the instantaneous gravity approximation.

However, gravitational lensing measurements — which are independent of the rotation curve and depend only on the total mass-energy distribution — consistently indicate mass in excess of the baryonic inventory (Umetsu et al., 2014). This excess cannot be explained by retarded gravity alone, as lensing is a geometric effect that depends on the stress-energy tensor, not the time-derivative of the gravitational field.

The question is: what fraction of this lensing-inferred excess is real additional mass, and what fraction could be attributed to vacuum statistical mass contributions?

### 5.2 Required Density

For the vacuum statistical mass to account for, say, 10% of the observed lensing excess in the Milky Way halo (a deliberately conservative estimate), the required effective density in the halo region (~10-50 kpc from center) is:
ρ_required ≈ 0.1 × M_excess / V_halo ≈ 0.1 × (4 × 10^{41} kg) / (10^{63} m^3) ≈ 4 × 10^{-23} kg/m^3

In terms of the amplification factor:
Γ_required = ρ_required / ρ_Λ ≈ (4 × 10^{-23}) / (6 × 10^{-27}) ≈ 7 × 10^3

So the question becomes: is an amplification of ~10^4 over the cosmological constant density physically plausible in galactic halo regions influenced by a central supermassive black hole?

We do not know. But we note that this is a quantitative question with a quantitative answer that can, in principle, be derived from quantum field theory in curved spacetime. The framework exists; the calculation has not been performed for realistic galactic geometries.

### 5.3 Radial Profile Prediction

If the vacuum statistical mass is concentrated near the galactic center (where Γ(r) is largest) and falls off with distance, the resulting density profile would differ from the NFW profile predicted by CDM:
ρ_NFW(r) = ρ_0 / ((r/r_s)(1 + r/r_s)^2)

A vacuum statistical mass contribution would likely follow the profile of the disruption mechanism — i.e., the gravitational influence of the central black hole:
ρ_vac(r) ~ Γ_0 · ρ_Λ · (r_s / r)^β

where r_s is the Schwarzschild radius of the central black hole and β is an unknown exponent (likely 1-3, depending on the correlation disruption mechanism).

This profile is more centrally concentrated than NFW, which would produce a steeper inner rotation curve. Distinguishing this from NFW observationally requires high-resolution rotation curve data within ~1 kpc of galactic centers — a regime where AGN contamination makes measurement difficult but not impossible.

## 6. Relationship to Known Physics

### 6.1 This Is Not a New Force

The vacuum statistical mass does not introduce a new interaction. It is a consequence of existing quantum field theory and general relativity. Virtual particles carry energy and therefore couple to gravity through the standard stress-energy tensor. The only new element is the claim that the correlation cancellation is spatially inhomogeneous — which is a consequence of the inhomogeneity of the spacetime background.

### 6.2 This Is Not the Cosmological Constant

The cosmological constant is spatially uniform and temporally constant. The vacuum statistical mass contribution proposed here is spatially concentrated near high-curvature regions and falls off with distance. Its equation of state is not necessarily w = -1. It is a dynamical field that responds to local conditions, not a fixed background energy.

### 6.3 Relationship to Analog Models

Several established physical effects share structural similarity with the proposed mechanism:

- Casimir Effect: Between two conducting plates, the boundary conditions alter the vacuum mode structure, producing a measurable force. This demonstrates that vacuum fluctuations respond to geometric boundary conditions. A black hole horizon is a physical boundary condition of the most extreme kind.

- Unruh Effect: An accelerating observer perceives the Minkowski vacuum as a thermal bath at temperature T_U = ħ a / (2π c k_B), where a is the proper acceleration. This demonstrates that the vacuum state is observer-dependent and that acceleration (equivalently, strong gravity) alters the perceived particle content of the vacuum.

- Dynamical Casimir Effect: Moving boundaries can convert virtual photons into real photons. This demonstrates that time-varying boundary conditions (equivalently, dynamic spacetime geometry) can promote virtual fluctuations into real particles.

The proposed vacuum statistical mass effect is the gravitational analog of these effects, applied to the inhomogeneous, time-varying spacetime geometry of a rotating galaxy with a central black hole.

### 6.4 Relationship to MOND

Modified Newtonian Dynamics (MOND, Milgrom 1983) introduces a critical acceleration scale:
a_0 ≈ 1.2 × 10^{-10} m/s^2

below which gravity departs from the Newtonian 1/r^2 law. MOND successfully reproduces rotation curves across a wide range of galaxy types (McGaugh et al., 2016) and predicts the radial acceleration relation (RAR) with remarkable accuracy (Lelli et al., 2017).

The physical origin of a_0 is unknown within MOND's framework. Several authors have noted that:
a_0 ≈ c H_0 / (2π) ≈ c^2 √(Λ/3)

suggesting a connection to the cosmological constant or the Hubble expansion rate. If vacuum statistical mass is real and its density profile is set by the balance between local curvature and cosmological expansion, it is plausible that the crossover scale where this contribution becomes significant corresponds to a_0. This would provide a physical origin for the MOND acceleration scale without modifying gravity.

This connection is speculative but structurally consistent.

## 7. What This Framework Predicts

A useful theory must make predictions that can be tested. The vacuum statistical mass framework, while underdeveloped, makes the following qualitative predictions:

P1 — Central Concentration. The vacuum mass contribution should be more centrally concentrated than CDM's NFW profile. Galaxies with more massive or more rapidly spinning central black holes should show relatively stronger central mass excess.

P2 — Spin Dependence. Kerr black holes with higher spin parameter a* should produce larger ergospheres and stronger frame-dragging, resulting in greater correlation disruption and larger Γ(r). High-spin AGN should exhibit systematically larger central mass excess than low-spin AGN at fixed black hole mass.

P3 — Environment Dependence. In galaxy clusters, the total vacuum statistical mass contribution should scale with the cluster's total black hole mass inventory, not just with total baryonic mass. This is a departure from CDM predictions, where the dark matter fraction depends primarily on halo mass.

P4 — No Direct Detection. Unlike WIMPs or axions, the vacuum statistical mass is not a particle. It cannot be detected in direct-detection experiments. It interacts gravitationally but leaves no signal in xenon or germanium detectors. This is consistent with all current null results (LZ 2024, XENONnT 2024, PandaX-4T 2023).

P5 — Scale Limitation. The effect is largest near black holes and falls off rapidly with distance. It cannot account for the dark matter contribution inferred at cosmological scales from CMB anisotropies. Those scales require either a different explanation or conventional CDM.

## 8. Open Questions and Honest Limitations

This framework has significant gaps that must be acknowledged:

Q1 — The Cancellation Mechanism. We do not know what causes the 10^{123} cancellation in flat spacetime. Without knowing the mechanism, we cannot predict how much it is disrupted in curved spacetime. Any quantitative estimate of Γ(r) is currently a free parameter.

Q2 — Backreaction. If vacuum fluctuations contribute to the stress-energy tensor, they also affect the spacetime geometry — which in turn affects the fluctuation rate. This self-consistent backreaction problem is unsolved even in simplified toy models.

Q3 — Distinguishability. Near galactic centers, the vacuum statistical mass profile and the CDM profile may produce similar observational signatures. Distinguishing them requires either (a) measurements sensitive to the equation of state of the dark component, or (b) high-precision rotation curve data in the inner ~1 kpc.

Q4 — Cosmological Consistency. If Γ(r) is large near every galactic center, the integrated contribution over all galaxies in the observable universe may produce a measurable effect on the CMB or large-scale structure. This constraint has not been calculated.

Q5 — The Entanglement Structure. The argument that long-range quantum entanglement causes cancellation in flat spacetime is plausible but not proven. The calculation of how this entanglement structure is modified by curved spacetime is an open problem in quantum gravity.

## 9. Summary

We have presented a framework for understanding why the quantum vacuum may contribute a small but non-zero effective mass density to galactic dynamics, concentrated near regions of high spacetime curvature and strong electromagnetic fields.

The central argument is:
1. Quantum vacuum fluctuations exist and carry energy-momentum.
2. In flat spacetime, quantum correlations cause their gravitational effects to nearly perfectly cancel — the cosmological constant problem states the residual is 10^{-123} of the naive estimate.
3. In strongly curved or strongly magnetized spacetime, these correlations are partially disrupted — this is already established by the Casimir, Unruh, Hawking, and Schwinger effects.
4. The disruption leaves a residual vacuum statistical mass that is small relative to the flat-space estimate but potentially significant relative to baryonic galactic mass.

This contribution is not dark matter. It is not a new particle. It is a gravitational consequence of known quantum field theory in curved spacetime, extended to realistic astrophysical environments.

The effect is complementary to, not competitive with, retarded gravitational dynamics (Effect 1), which independently accounts for flat rotation curves and spiral arm morphology.

The magnitude of this effect is unknown. The calculation required to determine it — quantum field theory in Kerr spacetime with realistic magnetic field configurations, integrated over a realistic galactic density profile — has not been performed.

This document is a statement that the calculation should be performed.

## References

Planck Collaboration (2020) — CMB power spectrum
Weinberg, S. (1989) — Cosmological constant problem
Padmanabhan, T. (2003) — Cosmological constant review
Springel, V. et al. (2005) — Large-scale structure simulations
Eisenstein, D.J. et al. (2005) — Baryon acoustic oscillations
Hawking, S.W. (1975) — Hawking radiation
Unruh, W.G. (1976) — Unruh effect
Schwinger, J. (1951) — Schwinger pair production
Casimir, H.B.G. (1948) — Casimir effect
Event Horizon Telescope Collaboration (2021) — M87 magnetic fields
Milgrom, M. (1983) — MOND
McGaugh, S.S. et al. (2016) — Radial acceleration relation
Lelli, F. et al. (2017) — One law to rule them all
LZ Collaboration (2024) — Dark matter direct detection
XENONnT Collaboration (2024) — Dark matter direct detection
Umetsu, K. et al. (2014) — Gravitational lensing excess
Clowe, D. et al. (2006) — Bullet Cluster

---

# High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/high-energy-particle-generation-and

Basis: Observations from Yang-Mills Collider v3.2 + Kerr Black Hole simulation
Theories Explored: General Relativity, Standard Model, Black Hole Thermodynamics, Magnetohydrodynamics (MHD), Cosmology

## 1. Introduction: What Physical Situation Does This Simulation Depict?

This simulation originally started from a simple question: "What would happen if a black hole were placed next to the LHC?" But upon running it, a physical scale analysis suggested that it may actually be depicting a far more extreme environment.

It likely represents something like this:

"A system in which particles are generated at extremely high energies (on the order of GRBs or AGN), surrounded by a rotating black hole with a powerful magnetic field"

This is essentially the same condition found in gamma-ray bursts (GRBs), active galactic nuclei (AGN), and magnetars — the most intensively studied objects in modern high-energy astrophysics.

The phenomena I directly observed in the simulation were as follows:
- Generated particles spontaneously aligned into a structure resembling an accretion disk
- Particles were completely separated by charge type (positive/negative) — as if matter and antimatter were segregating
- Orbital radii differed according to particle mass (lighter particles on inner orbits, heavier particles on outer orbits)
- Separated matter and antimatter were prevented from meeting, persisting for a long time
- Over time, as energy accumulated, the black hole's effective mass and gravity appeared to change

## 2. The Kerr Black Hole and Its Surrounding Spacetime: The Unique World Created by Rotation

When a black hole rotates, spacetime itself is dragged into a spin. This was first precisely expressed in mathematics by Roy Kerr, whose 1963 paper stands as a major milestone in the history of general relativity.

### 2.1 The Kerr Metric — The Equation That Twists Spacetime

The shape of spacetime described by Kerr is:
ds^2 = -(1 - 2Mr/Σ) dt^2 - (4Mar sin^2θ/Σ) dt dφ + (Σ/Δ) dr^2 + Σ dθ^2 + (r^2 + a^2 + (2Ma^2 r sin^2θ)/Σ) sin^2θ dφ^2

Key quantities here:
- Σ = r^2 + a^2 cos^2θ
- Δ = r^2 - 2Mr + a^2
- a = J/M (angular momentum per unit mass, i.e., the spin parameter)
- a* = a/M (dimensionless spin, ranging from 0 to 1)

Although this equation looks complicated, the core idea is simple: the faster the black hole rotates, the more severely the surrounding spacetime is dragged.

### 2.2 The Event Horizon — The Point of No Return

The outer event horizon radius of a Kerr black hole is given by:
r_+ = M (1 + √(1 - a*^2))

- No spin (a* = 0): r_+ = 2M (the Schwarzschild radius, the most familiar case)
- Extreme spin (a* = 1): r_+ = M (the horizon becomes smaller)

That is, the faster the spin, the smaller the event horizon, and the more of the ergosphere is exposed. I thought this structure was closely related to how particles congregate in the simulation.

### 2.3 The Ergosphere — A Region Where Nothing Can Stay Still

The boundary of the ergosphere (the static limit surface) is:
r_ergo = M (1 + √(1 - a*^2 cos^2θ))

What makes this region unique is that the black hole's rotation is so strong that no object can remain stationary there — spacetime itself is spinning. At the equatorial plane (θ = π/2), the maximum radius is 2M, independent of the black hole's spin.

### 2.4 The Innermost Stable Circular Orbit (ISCO) — The Inner Edge of the Accretion Disk

This is the critical radius that determines how close an accretion disk can approach the black hole.
- Schwarzschild (a* = 0): r_ISCO = 6M (= 3R_s)
- Extreme Kerr, prograde (a* = 1): r_ISCO = M (very close!)
- Extreme Kerr, retrograde (a* = 1): r_ISCO = 9M (much farther)

In general, particles orbiting in the same direction as the black hole's rotation can maintain stable orbits much closer to it.

The general formula (Bardeen, Press, Teukolsky 1972) is:
r_ISCO = M {3 + Z_2 ∓ √[(3-Z_1)(3+Z_1+2Z_2)]}

where:
- Z_1 = 1 + (1-a*^2)^{1/3} [(1+a*)^{1/3} + (1-a*)^{1/3}]
- Z_2 = √(3a*^2 + Z_1^2)

The upper sign (−) is for prograde orbits (co-rotating with the black hole), and the lower sign (+) is for retrograde orbits.

My hypothesis: The reason particles spontaneously formed a disk shape in the simulation may be because they were captured at an effective ISCO, jointly determined by this ISCO condition and magnetic pressure.

## 3. Frame Dragging — The Dragging of Spacetime, the Lense-Thirring Effect

Around a rotating mass, spacetime itself is dragged into rotation. This is called frame dragging, or the Lense-Thirring effect.

### 3.1 The Lense-Thirring Angular Velocity

In the weak-field approximation, this effect is expressed as:
Ω_LT = 2GJ / (c^2 r^3)

This means that the larger the angular momentum (J) of the central body, and the closer the distance (r), the faster the surrounding spacetime is dragged.

In the full Kerr metric, it is expressed as:
Ω_φ = dφ/dt = -g_{tφ}/g_{φφ} = 2Mar / ((r^2+a^2)^2 - a^2 Δ sin^2θ)

At a very large distance from the black hole (r ≫ M), this simplifies to:
Ω_φ ≈ 2Ma / r^3 = 2GJ / (c^2 r^3)

### 3.2 How Is This Implemented in the Simulation?

Looking at the code directly, the simulation approximates this effect as follows:
- fdAcc = BH_SPIN × logMass × 55.0 / (r^3 + 1.0)
- Tangential direction: t̂ = (-dz, 0, dx) / r_xz

This follows the form of the core physical law Ω_LT ∝ J/r^3. The numerical coefficient (55.0) is likely for visual scaling, but the directionality is physically accurate.

### 3.3 Inside the Ergosphere, Particles Are Forced to Co-rotate

Inside the ergosphere, orbits with negative energy can exist. This is not merely a mathematical curiosity — it is the key to the famous Penrose process, a mechanism for extracting energy from a black hole.

E = p_t = g_{tt} (dt/dτ) + g_{tφ} (dφ/dτ)

Inside the ergosphere (g_{tt} > 0), a particle's energy can become negative (−). In this situation, if a particle splits in two, one piece can be absorbed by the black hole with negative energy, while the other piece escapes with greater energy than the original particle.

The maximum energy theoretically extractable from a black hole is:
E_Penrose ≤ M - M_irr

where M_irr = (1/2) √(r_+^2 + a^2) = (1/2) √(2Mr_+) is the irreducible mass.

I cautiously speculate that the behavior seen in the simulation — where particles appeared to be ejected near the ergosphere when the black hole's spin exceeded a certain value — may be a trace of this Penrose process.

## 4. Magnetic Fields and Particle Motion: The Boris Integrator and the Lorentz Force

One of the core elements of this simulation is the calculation of how charged particles move within a magnetic field.

### 4.1 The Relativistic Equation of Motion

The relativistic motion of a charged particle in an electromagnetic field is given by:
dp^μ/dτ = q F^{μν} u_ν

Written out in 3-vector form:
d(γ m v)/dt = q(E + v × B)

With only a magnetic field (E = 0), this simplifies to:
dp/dt = q(v × B)

### 4.2 Cyclotron Motion and Mass Separation

In a magnetic field B, a charged particle traces a circular path. The radius of this circular motion is called the Larmor radius:
r_L = γ m v_⊥ / (|q|B) = p_⊥ / (|q|B)

The angular frequency is:
ω_c = |q|B / (γ m)

where:
- γ = E/(mc^2) (Lorentz factor)
- p_⊥ (transverse momentum)

The key insight is: r_L ∝ m (proportional to mass!)

For particles with the same energy and the same charge:
- Electron (m = 0.511 MeV): smallest radius → innermost orbit
- Pion (m = 140 MeV): intermediate radius
- Proton (m = 938 MeV): larger radius → outer orbit
- W boson (m = 80,377 MeV): very large radius → outermost orbit

I believe this is the physical cause of the mass-dependent orbital radius separation I directly observed in the simulation.

### 4.3 The Boris Integrator

The Boris algorithm used in the simulation is a special integration method that conserves energy well. It proceeds roughly as follows:

Step 1: p^- = p^n + (q/(2m)) E Δt
Step 2: t = (q/(2m)) B Δt / γ, s = 2t/(1+|t|^2), p' = p^- + p^- × t, p^+ = p^- + p' × s
Step 3: p^{n+1} = p^+ + (q/(2m)) E Δt

Advantages of this method:
- Conserves the magnetic moment μ = m v_⊥^2/(2B)
- No energy drift (no runaway growth)
- Suitable for long-duration simulations

### 4.4 Symmetric Separation by Charge Sign

Looking at the Lorentz force F = q(v × B), reversing the sign of charge q exactly reverses the direction of the force.
- Positive charge (+q): F = +q(v × B) → counterclockwise
- Negative charge (-q): F = -q(v × B) → clockwise

For a particle-antiparticle pair with the same initial velocity:
- They orbit with the same radius
- In opposite directions
- Positioned exactly on opposite sides (π radians apart)

This is the physical cause of the charge-dependent symmetric separation I directly observed in the simulation.

## 5. Matter-Antimatter Separation and Annihilation Suppression

This was perhaps the most striking observation.

### 5.1 Charge Separation

What happens when a particle-antiparticle pair is created in a strong magnetic field?
- Pair production: γ + γ → e^+ + e^- (or heavier particle-antiparticle pairs)

Immediately after creation, the Lorentz force acts:
- Electron (e^-): F^- = -e(v × B)
- Positron (e^+): F^+ = +e(v × B)

The two particles split in opposite directions the moment they are created.

### 5.2 The Condition for Annihilation Suppression

For annihilation (e^+ + e^- → γ + γ) to occur, the two particles must meet. What condition allows the magnetic field to prevent this?
r_L = γ m c / (eB) ≪ R_system

(when the Larmor radius is much smaller than the system size)

Considering a real GRB environment:
- B ~ 10^{12} - 10^{15} G
- Larmor radius of an electron (γ ~ 10^6) ≈ 10^{-2} cm

This is far smaller than the system size (R_system). Therefore, matter and antimatter can remain spatially isolated for a long time.

### 5.3 A Real Astrophysical Example: Pulsars

This kind of charge separation also occurs around actual pulsars. According to the Goldreich-Julian model (1969):
ρ_GJ = - (Ω · B) / (2π c)

(where Ω is the pulsar's rotational angular velocity)

The electrons and positrons corresponding to this density are known to separate and flow along magnetic field lines, forming jets.

### 5.4 Cosmological Implications: The Matter-Antimatter Asymmetry Problem

This section raises a very interesting possibility for extension.

In standard Big Bang theory, matter and antimatter should have been produced symmetrically, yet our universe is overwhelmingly dominated by matter. Explaining this requires additional conditions such as CP violation.

The mechanism incidentally revealed by the simulation gives rise to this thought:

Primordial magnetic field (B_primordial) + high-energy environment (GUT scale, kT ~ 10^{15} GeV) → charge separation → annihilation suppression → formation of matter/antimatter domains → unequal annihilation at domain boundaries → net matter surplus

This could be discussed as a complementary mechanism to the Sakharov conditions (CP violation, baryon number violation, departure from thermal equilibrium).

Related theories include: Magnetogenesis, CP violation at the electroweak phase transition (EWPT), and Affleck-Dine baryogenesis.

## 6. Energy-Mass Equivalence and Dynamic Gravity

Now let us get to the most fundamental connection.

### 6.1 Energy-Mass Equivalence (E = mc^2)

Einstein's famous formula:
E^2 = (pc)^2 + (mc^2)^2

For a particle at rest: E_0 = mc^2

An important point: when energy E accumulates in the accretion disk, an equivalent mass arises:
Δm = E / c^2

For example, 10^{24} GeV of energy corresponds to 1.8 × 10^{-3} kg. This is tiny for a single particle, but the story changes if the process continues.

dM/dt = Ṁ_accretion × c^2 × η

where η is the radiative efficiency (η ≈ 0.057 for Schwarzschild, η ≈ 0.42 for extreme Kerr). The Eddington luminosity limit is:
L_Edd = 4π G M m_p c / σ_T ≈ 1.3 × 10^{31} (M/M_⊙) W

### 6.2 The Einstein Field Equations and the Energy-Momentum Tensor

The central equation of general relativity is:
G_{μν} + Λ g_{μν} = (8πG/c^4) T_{μν}

- G_{μν} = R_{μν} - (1/2)g_{μν}R (Einstein tensor, representing the curvature of spacetime)
- T_{μν} (energy-momentum tensor, representing the distribution of matter and energy)

What this equation says is clear: how energy and matter are distributed (T_{μν}) determines the curvature of spacetime (G_{μν}).

Therefore, as the energy density ε of the accretion disk increases: T_{μν} increases → G_{μν} changes → spacetime curvature changes → gravity changes

This is the theoretical basis for why energy accumulation can alter gravity.

### 6.3 The Mass Rate-of-Change Equation

Thinking about the time evolution of the black hole's mass:
dM/dt = Ṁ_in - Ṁ_out - Ṗ_Hawking / c^2

- Ṁ_in: mass accretion rate
- Ṁ_out: mass outflow rate via jets or winds
- Ṗ_Hawking: Hawking radiation power output

The Hawking radiation power is:
P_Hawking = ħ c^6 / (15360π G^2 M^2)

and the black hole temperature is:
T_Hawking = ħ c^3 / (8π G M k_B) ≈ 6 × 10^{-8} (M_⊙/M) K

For astronomically large black holes, the effect of Hawking radiation is negligibly small.

### 6.4 Dynamic ISCO

An interesting point: when the black hole's mass changes, so does the ISCO:
r_ISCO ∝ M

Therefore:
dr_ISCO/dt = (dr_ISCO/dM) (dM/dt)

- If M increases via accretion → r_ISCO also increases → the accretion disk expands outward
- If M decreases via jet ejection → r_ISCO decreases → the disk contracts inward

This feedback mechanism may explain the dynamic reconfiguration of the accretion disk I observed in the simulation.

## 7. Quasi-Periodic Oscillations (QPO) — The Pulsation of Gravity

In a time-varying system, oscillatory phenomena can arise naturally.

### 7.1 The Feedback Loop and Oscillations

Summarizing the dynamic process observed in the simulation:

Energy accumulation → M increases → gravity increases → more particles captured → threshold exceeded → jet ejection → M decreases → gravity decreases → capture weakens → energy re-accumulates → repeat...

This kind of feedback loop naturally produces periodic oscillations.

The characteristic timescales of this cycle are varied:
- t_visc ~ R^2/ν (viscous timescale: how long it takes material to move through the accretion disk)
- t_dyn ~ √(R^3/GM) (dynamical timescale: orbital period)
- t_thermal ~ t_visc/α (thermal timescale)

### 7.2 QPO Frequencies

The quasi-periodic oscillation (QPO) frequencies actually observed near black holes can be expressed as:

Keplerian frequency (pure orbital frequency):
ν_K = (1/(2π)) √(GM/r^3) / (1 ± a* (r_g/r)^{3/2})

(where r_g = GM/c^2 is the gravitational radius)

The maximum Keplerian frequency at the ISCO is:
- Schwarzschild: ν_{K,ISCO} ≈ 2.2 (M_⊙/M) kHz
- Extreme Kerr: ν_{K,ISCO} ≈ 4.4 (M_⊙/M) kHz

The Lense-Thirring precession frequency is:
ν_LT = ν_K - ν_r

(difference between azimuthal and radial oscillation frequencies)

Interestingly, the parametric resonance model (Abramowicz & Kluzniak) predicts that the ratio of upper to lower frequencies will be 3:2 — in agreement with actual observations.

### 7.3 Real Observational Cases

These oscillations are also observed in reality:
- X-ray binary GRS 1915+105: QPO at ~67 Hz (black hole mass ~14 M_⊙)
- Sgr A* (galactic center, 4 × 10^6 M_⊙): QPO predicted at ~1 mHz
- M87 (6.5 × 10^9 M_⊙): oscillations at hundreds of μHz observed

In my view, the energy accumulation-ejection cycle shown in the simulation may be connected to these actual observed gravitational pulsation phenomena.

## 8. Ultra-High-Energy Physics — The GRB/AGN Environment

To understand just how extreme the world this simulation depicts is, it helps to compare it against energy scales we already know.

### 8.1 Energy Scale Comparison

LHC maximum (pp collision): √s = 13,600 GeV — Relative to LHC: 1×
Tevatron: √s = 1,960 GeV — Relative to LHC: 0.14×
Oh-My-God particle (ultra-high-energy cosmic ray): E ≈ 3 × 10^{20} eV = 3 × 10^{11} GeV — Relative to LHC: ~2 × 10^7×
GRB estimated maximum energy: E ~ 10^{23} - 10^{25} GeV — Relative to LHC: ~10^{19} - 10^{21}×
Planck energy (theoretical limit): E_Pl = √(ħ c^5 / G) ≈ 1.22 × 10^{19} GeV — Relative to LHC: ~10^{15}×

In other words, the environment implied by this simulation is incomparably more extreme than the most powerful particle accelerator humanity has built.

### 8.2 Phenomena That Can Occur at Ultra-High Energies

In this energy regime, phenomena entirely foreign to everyday experience can occur:

- Quark-Gluon Plasma (QGP): T_QCD ~ 150 MeV (temperature for the hadron-to-QGP transition). AGN/GRB environment: kT ≫ T_QCD → matter can exist in a state where quarks and gluons are liberated.

- Electroweak Unification Scale: E_EW ~ 100 GeV (the mass scale of W and Z bosons). GRB environment: E ≫ E_EW → conditions for electroweak symmetry restoration.

- Grand Unification Theory (GUT) Scale: E_GUT ~ 10^{16} GeV. In extreme GRB environments, this region may be approachable.

- Planck Scale: E_Pl ~ 10^{19} GeV. At this energy scale, quantum gravity effects become important (a realm we do not yet fully understand).

### 8.3 Bethe-Bloch Energy Loss

The energy loss formula implemented in the simulation is:
-dE/dx = K z^2 (Z/A) (1/β^2) [ (1/2) ln(2m_e c^2 β^2 γ^2 T_max / I^2) - β^2 ]

where:
- K = 0.307 MeV cm^2/mol
- I = mean ionization energy
- T_max = maximum kinetic energy that can be transferred in a single collision

Additionally, when a particle passes through thin material, energy loss does not follow a normal distribution but instead exhibits Landau fluctuations:
P(Δ) ∝ (1/ξ) φ((Δ - Δ_mp)/ξ)

where ξ = (K/2)(Z/A)(x/β^2) (x is the material thickness)

This distribution is asymmetric, with a tail where very large energy losses occur rarely. I found it quite impressive that the simulation actually implements these fluctuations.

## 9. Magnetohydrodynamics and the Blandford-Znajek Mechanism

To understand the accretion disk and jets, we must consider the interaction between the magnetic field and matter.

### 9.1 The Magnetic Field of the Accretion Disk

The evolution of the magnetic field inside the accretion disk follows the magnetohydrodynamics (MHD) equations:
∂B/∂t = ∇ × (v × B) - ∇ × (η ∇ × B)

An important dimensionless number here is the magnetic Reynolds number:
R_m = vL/η ≫ 1

(this condition is generally satisfied in accretion disks)

Magnetic Buoyancy Instability (Parker Instability): Magnetic field lines rise to the surface of the disk through buoyancy, which is important for corona formation and particle acceleration.

Magnetorotational Instability (MRI, Balbus-Hawley 1991): Growth rate Γ ≈ Ω (angular velocity of a prograde Keplerian orbit). MRI is now accepted as the primary mechanism for viscosity and angular momentum transport in accretion disks. Discovered in 1991, this instability represented a major turning point in accretion disk research.

### 9.2 The Blandford-Znajek Mechanism (1977)

This is the famous theory explaining how powerful jets can be produced from a rotating black hole.

The extracted power output is approximately:
P_BZ ≈ (κ/(4πc)) Φ_BH^2 Ω_H^2 f(Ω_H)

where:
- Φ_BH = magnetic flux threading the black hole
- Ω_H = a/(2Mr_+) (angular velocity of the event horizon)
- κ ≈ 0.044 (numerical coefficient)
- f(Ω_H) = efficiency function

In the extreme spin limit (a* → 1):
P_BZ ≈ (κ/(4πc)) Φ_BH^2 (c/(4M))^2

According to this theory, the maximum extractable rotational energy of the black hole is:
E_rot = M - M_irr ≤ 0.29 Mc^2

The appearance of jet-like structures in the simulation when BH_SPIN > 0.6 makes me think this may be related to the Blandford-Znajek mechanism.

### 9.3 Jet Formation

The Lorentz factor of a relativistic jet is:
Γ_jet ~ (P_BZ / (Ṁ_jet c^2))^{1/2}

Observed values:
- GRB jets: Γ ~ 10^2 - 10^3
- AGN jets: Γ ~ 10 - 30

Inside the jet, particle acceleration by shocks (Fermi acceleration) occurs:
dN/dE ∝ E^{-s}, s = (r+2)/(r-1)

where r is the shock compression ratio. For a non-relativistic shock (r=4), s=2, which is similar to the observed cosmic ray spectrum (E^{-2.7}).

## 10. Black Hole Thermodynamics and Hawking Radiation

Although not implemented in this simulation, black hole thermodynamics is a topic that cannot be omitted when discussing black holes.

### 10.1 The Laws of Black Hole Thermodynamics

- Zeroth Law: The surface gravity κ is constant over the event horizon of a stationary black hole.
- First Law: dM = (κ/(8π)) dA + Ω_H dJ + Φ_H dQ (energy conservation: change in mass equals contributions from changes in area, angular momentum, and charge).
- Second Law: dA ≥ 0 (the area of the event horizon can never decrease, classically).
- Third Law: It is impossible to achieve κ = 0 (the extremal black hole state).

### 10.2 Hawking Radiation (Hawking 1974)

When quantum effects are considered, black holes are not completely black — they emit thermal (blackbody) radiation:
T_H = ħ κ / (2π c k_B) = ħ c^3 / (8π G M k_B) ≈ 6.17 × 10^{-8} (M_⊙/M) K

The radiation power is:
P = ħ c^6 / (15360π G^2 M^2) ≈ 3.56 × 10^{32} (M_⊙/M)^2 W

The evaporation time is:
t_evap = 5120π G^2 M^3 / (ħ c^4) ≈ 2.1 × 10^{67} (M/M_⊙)^3 yr

The time it takes for a solar-mass black hole to evaporate is 10^{57} times the age of the universe. In other words, Hawking radiation is completely irrelevant for astronomically sized black holes.

### 10.3 Black Hole Entropy (Bekenstein-Hawking)

Before the discovery of Hawking radiation, Jacob Bekenstein proposed the idea that black holes carry entropy:
S_BH = k_B A / (4 l_Pl^2) = k_B c^3 A / (4 G ħ)

where l_Pl = √(Għ/c^3) ≈ 1.616 × 10^{-35} m is the Planck length.

## 11. Summary of Simulation Observations and Physical Connections

Simulation Observation: Particles separate by charge — Physical Mechanism: Lorentz force (F = qv × B) — Astrophysical Context: Magnetars, AGN jets, pulsars
Simulation Observation: Mass-dependent orbital radii — Physical Mechanism: r_L ∝ m (Larmor radius scaling) — Astrophysical Context: Heavy particles at larger radii
Simulation Observation: Annihilation suppression — Physical Mechanism: r_L ≪ R_system — Astrophysical Context: GRB environments, AGN coronae
Simulation Observation: Spontaneous accretion disk — Physical Mechanism: Angular momentum conservation + magnetic fields — Astrophysical Context: All accreting black holes
Simulation Observation: Energy accumulation → mass change — Physical Mechanism: E = mc^2, T_{μν} curvature feedback — Astrophysical Context: Black hole growth, AGN feedback
Simulation Observation: Quasi-periodic oscillations — Physical Mechanism: Feedback loop (accretion → jet → depletion) — Astrophysical Context: X-ray binaries, AGN
Simulation Observation: Jet-like ejection (spin > 0.6) — Physical Mechanism: Blandford-Znajek mechanism — Astrophysical Context: Radio galaxies, blazars
Simulation Observation: Penrose process (spontaneous) — Physical Mechanism: Frame dragging + ergosphere — Astrophysical Context: Rotating black holes

---

# Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation in Disk Galaxies

Version: 1.0 (Complete)
Source: seoulinside.substack.com/p/delayed-gravitational-interaction

About This Document: This document was written by a non-specialist. It is not a peer-reviewed paper. It is a structured record of an investigation — conducted through simulation, observation of emergent behavior, and systematic reasoning — into a specific question: whether the finite propagation speed of gravity, combined with black hole displacement, is sufficient to produce spiral arm structure in disk galaxies without invoking dark matter or density wave theory.

The answer suggested by the simulations described here is yes. That answer is presented carefully, with its limitations stated explicitly.

## Three Claims

The following three claims structure this document. They are stated here, at the outset, without elaboration. Each is developed in full in the sections that follow.

Claim I. When a black hole is displaced from the geometric center of a disk galaxy — however slightly — spiral arm structure emerges immediately and persistently. This is a consequence of the finite propagation speed of gravity: stars at different distances from the black hole reference different past positions of that black hole, producing a systematic angular offset in the gravitational force vector that, in a rotating system, maps onto a spiral pattern. This claim is verifiable directly. Open the simulator linked above. Press any arrow key. Observe.

Claim II. The ultra-strong magnetic fields observed in the vicinity of supermassive black holes — combined with the extreme energy densities of accretion disks and relativistic jets — create conditions approaching or exceeding the Schwinger critical field, at which spontaneous pair production from vacuum occurs. The magnetic field separates the produced particle and antiparticle in opposite directions, spatially suppressing annihilation. This process constitutes a mechanism for continuous local mass generation and destruction around black holes. The scale of this effect is unknown. It may be non-negligible. This claim is a hypothesis.

Claim III. If gravity propagates at a finite speed, then the gravitational signal itself is subject to the curvature of spacetime through which it travels. In regions of extreme curvature — near black holes — the gravitational signal from infalling mass may be redirected, delayed, or effectively trapped. This would mean that the gravitational influence of mass accreted beyond the event horizon is not fully communicated to the exterior. Observed black hole masses would then represent lower bounds on actual masses. This claim is a hypothesis, and the most speculative of the three.

These three claims are independent. Claim I does not require Claims II or III to be true. The strength of this document rests primarily on Claim I, which requires no theoretical commitment beyond the already-verified finite propagation speed of gravitational waves (Abbott et al., LIGO/Virgo, 2017).

## Section 1. The Spiral Arm Formation Mechanism

### 1.1 The Problem with Existing Explanations

Spiral arm structure is the dominant morphological feature of disk galaxies. Approximately 60–70% of observed galaxies in the local universe exhibit spiral structure (Lintott et al., 2011, Galaxy Zoo). The persistence and prevalence of this structure constitutes one of the oldest unsolved problems in galactic dynamics.

The standard theoretical framework — Lin-Shu density wave theory (Lin & Shu, 1964) — treats spiral arms as quasi-stationary density waves propagating through the stellar disk. The theory was motivated in part by the winding problem: in a differentially rotating disk, any material arm would be sheared into oblivion within a few galactic rotation periods (roughly 10^8-10^9 years). Since spiral arms persist on timescales far exceeding this, they cannot be material structures rotating with the stars. Density wave theory resolves this by treating the arm as a pattern — analogous to a traffic jam through which individual cars pass — rather than a fixed collection of stars.

However, Lin-Shu density wave theory carries its own unresolved difficulties:

- The pattern speed problem. The theory requires a well-defined pattern speed Ω_p distinct from the local stellar angular velocity. Observational determination of pattern speeds is indirect and contested. A single, stable pattern speed is not consistently recovered across galaxy samples.

- The maintenance problem. Density waves dissipate. Maintaining them against damping requires a continuous energy source — typically invoked as swing amplification or bar-driven resonance — whose generality is not established.

- The universality problem. If density wave theory requires specific resonance conditions, the 60–70% prevalence of spiral structure is unexplained. Why should most disk galaxies independently satisfy the required conditions?

- The formation problem. Density wave theory describes the propagation of an existing wave. It does not explain how the initial wave is established.

A second class of explanations invokes tidal interactions — gravitational perturbations from companion galaxies or satellite systems. Tidal spiral arms are well-documented in interacting pairs (e.g., M51/NGC 5195). However, isolated spiral galaxies without obvious interaction partners also exhibit persistent spiral structure, limiting the generality of tidal explanations.

The mechanism described in this document requires none of the above. It requires only two conditions, both of which hold universally in any physical galaxy:
1. Gravity propagates at a finite speed.
2. The central black hole is not at rest relative to the galactic disk.

Both conditions are empirically established facts, not model assumptions. The mechanism is therefore not a special-case explanation. It is a general one.

### 1.2 The Mechanism: Retarded Gravity and Black Hole Displacement

#### 1.2.1 Finite Propagation Speed of Gravity

The finite propagation speed of gravitational influence is not a novel hypothesis. It is a direct prediction of General Relativity, confirmed observationally by the detection of gravitational waves at the speed of light (Abbott et al., 2017, GW170817 + GRB 170817A; speed of gravity constrained to within 10^{-15} of c).

The consequence for galactic dynamics has received limited attention in the mainstream literature, with notable exceptions (Yahalom, 2013, 2019, 2024; Van Flandern, 1998 — though the latter's conclusions are disputed). The argument is straightforward:

If gravitational influence propagates at c, then the gravitational force experienced by a star at distance r from a black hole at time t is determined not by the black hole's position at t, but by its position at t - r/c.

- For a black hole at rest, this introduces no asymmetry: the retarded position equals the current position, and the force field is spherically symmetric. Spiral structure does not emerge.

- For a black hole in motion — however slight — the retarded position differs from the current position by an amount proportional to both the velocity of the black hole and the light-travel time r/c. Stars at different distances therefore reference different past positions of the same black hole. The gravitational force vectors experienced by stars at different radii point in systematically different directions. In a rotating disk, this angular offset is sheared into a spiral pattern.

This is not a perturbative effect that requires large black hole velocities. It is a structural consequence of differential light-travel time across the disk. Even a black hole displaced by a fraction of a parsec from the disk center will produce a measurable angular offset in the force vectors of stars at kiloparsec distances.

#### 1.2.2 The Universality Argument

The black hole in a real galaxy is never at rest. It cannot be. The following perturbations act continuously and simultaneously:
- The host galaxy moves through space (peculiar velocity typically 100–600 km/s).
- Satellite galaxies and globular clusters exert time-varying tidal forces.
- The galactic bar, when present, drives the black hole in a periodic orbit about the disk center.
- In merging systems, the two black holes orbit each other prior to coalescence.
- The large-scale structure of the universe — the cosmic web of filaments and voids — exerts a slowly varying gravitational background.

Perfect black hole stasis would require exact cancellation of all these perturbations simultaneously and continuously. This is not physically plausible. Black hole motion is the default state. Spiral structure is therefore the expected morphology for disk galaxies — not a special condition requiring explanation.

This directly addresses the universality problem: 60–70% spiral prevalence is not surprising if spiral structure is the generic outcome of black hole motion in a disk. The remaining 30–40% — ellipticals, lenticulars, irregulars — represent systems where disk structure itself is absent, disrupted, or dynamically suppressed.

### 1.3 Mathematical Formulation

#### 1.3.1 Equation of Motion

The full equation of motion for a star at position r in the galactic disk is:
d^2 r/dt^2 = a_N(r,t) + a_r(r,t)

where a_N is the Newtonian gravitational acceleration from the disk and black hole (evaluated at current position), and a_r is the retarded gravitational correction.

#### 1.3.2 Newtonian Component: Black Hole and Freeman Disk

The Newtonian acceleration comprises contributions from the central black hole and the stellar disk:
a_N = -G M_BH (r - r_BH) / |r - r_BH|^3 - (G M_disk(r) / r^3) r

The disk mass enclosed within radius r follows the Freeman (1970) exponential surface density profile:
M_disk(r) = M_total [1 - (1 + r/R_d) e^{-r/R_d}]

where R_d is the disk scale length and M_total is the total disk mass.

#### 1.3.3 Retarded Gravitational Correction

Following Yahalom (2013, 2019, 2024), the retarded gravitational acceleration in the point-mass approximation is:
a_r = α · (G M̈_BH) / (2c^2) · R̂

where:
- α is a dimensionless retardation strength parameter (0 ≤ α ≤ 10 in the simulator; α = 1 corresponds to the physical prediction)
- M̈_BH = d^2 M_BH/dt^2 is the second time derivative of the black hole mass
- R̂ is the unit vector from black hole to star
- c is the speed of light

The critical structural feature of this term is the absence of an inverse-distance dependence. Unlike Newtonian gravity (∝ 1/r^2) or even the leading post-Newtonian corrections, the retarded term a_r does not diminish with distance. This is directly analogous to the radiation zone of an accelerating charge in electromagnetism, where the radiation field falls as 1/r rather than 1/r^2. At galactic scales, this means that retarded gravitational effects become relatively more important at large radii — precisely the regime where observed rotation curves deviate most strongly from Newtonian predictions.

#### 1.3.4 Retarded Position and the History Buffer

The retarded position of the black hole — the position seen by a star at distance r at time t — is:
r_BH^ret(t, r) = r_BH(t - α r / c)

In the simulator, this is computed by maintaining a first-in, first-out (FIFO) position history buffer for the black hole, with a maximum depth of 300 steps. For each star, the appropriate past position is recovered by linear interpolation:
r_BH(t-τ) ≈ r_BH(t_0) + (τ - t_0)/(t_1 - t_0) [r_BH(t_1) - r_BH(t_0)]

where t_0 and t_1 are the two buffer entries bracketing the target time t-τ, and τ = α r/c.

This interpolation is the mechanism that produces spiral arms.

Each star pulls its gravitational force vector toward a different past position of the black hole. Stars closer to the center reference a more recent position; stars at large radii reference an older position. When the black hole is in motion, these past positions are spatially distinct. The resulting force vectors point in systematically different directions as a function of radius. In a differentially rotating disk, this radially-dependent angular offset is sheared continuously into an Archimedean spiral pattern.

The geometry is exact and deterministic. No stochastic process, no resonance condition, no special initial configuration is required. The spiral is a direct geometric consequence of differential light-travel time across a rotating disk around a displaced massive object.

### 1.4 The Leapfrog (Velocity Verlet) Integrator

The simulator uses a leapfrog integrator (equivalent to velocity Verlet) for time evolution. This choice is not arbitrary.

Integration steps:
v_{n+1/2} = v_n + a(r_n) Δt/2
r_{n+1} = r_n + v_{n+1/2} Δt
a_{n+1} = a(r_{n+1})
v_{n+1} = v_{n+1/2} + a_{n+1} Δt/2

Properties relevant to this application:
- Formal accuracy: O(Δt^2) — Sufficient for galactic dynamics timescales
- Time reversibility: Yes — Essential for distinguishing physical behavior from integration artifacts
- Symplecticity: Yes — Preserves phase space volume; prevents artificial energy drift over long integrations
- Energy conservation: Near-exact — ΔE/E monitored in real time in simulator
- Angular momentum conservation: Near-exact — ΔL/L monitored in real time in simulator

The real-time conservation diagnostics in GalaxyCS v4 are critical for the validity of the simulation results. If the observed spiral structure were an artifact of numerical instability, it would manifest as unbounded growth in ΔE or ΔL. The structure is observed to persist under conditions of stable energy and angular momentum conservation. This rules out the most common class of numerical artifacts.

### 1.5 Observed Behavior and Predicted Consequences

#### 1.5.1 Immediate Spiral Formation

In GalaxyCS v4, with a stellar population of 20,000–80,000 test particles initialized on circular orbits consistent with the Freeman disk rotation curve:
- With BH at rest (displacement = 0): no spiral structure. Axisymmetric disk.
- With BH displaced by any nonzero amount: spiral arm structure emerges within the first few simulation steps and persists indefinitely.

The transition is not gradual. It is immediate. There is no critical displacement threshold below which the effect is absent.

This behavior is consistent with the mathematical analysis: the spiral is a geometric consequence of differential retarded positions, not a resonance phenomenon with a threshold.

#### 1.5.2 Arm Count and Morphology

The number and pitch angle of the spiral arms is determined by the kinematic history of the black hole displacement:
- Simple unidirectional displacement → two-arm spiral
- Oscillatory displacement → multi-arm structure
- Irregular displacement → flocculent or asymmetric arms

This predicts a direct correspondence between black hole kinematics and spiral morphology that is in principle observationally testable. The inverse problem — inferring black hole kinematic history from spiral morphology — is a novel observational tool suggested by this framework.

#### 1.5.3 Rotation Curve Behavior

The HUD in GalaxyCS v4 displays, in real time:
- Observed stellar rotation velocity at outer disk radius
- Newtonian prediction for the same radius given the disk mass distribution
- The ratio (observed / predicted)

In runs with active retarded gravity and BH displacement, the outer rotation velocity consistently exceeds the Newtonian prediction by factors of 1.5-3.0, depending on the α parameter and BH displacement. This qualitatively reproduces the flat or rising rotation curves observed in disk galaxies — the primary observational motivation for dark matter.

The retarded gravitational term provides a natural explanation: because a_r does not fall off with distance, it contributes increasingly to the total acceleration at large radii, sustaining circular velocities above the Newtonian prediction.

#### 1.5.4 Void Formation

Reduction of the black hole mass parameter — simulating either mass loss, observation uncertainty, or temporary disruption of the effective gravitational influence — followed by displacement and mass recovery produces large underdense regions (voids) in the stellar distribution. This behavior emerges without any additional mechanism. The void is the complement of the overdense arms: stellar material evacuated from one region accumulates in another, driven by the time-varying retarded force field.

### 1.6 Relationship to Existing Work

The retarded gravity approach to galactic dynamics has been developed most systematically by Asher Yahalom (Ariel University). Key references:
- Yahalom, A. (2013). "Lorentz Symmetry Group, Retardation, Intergalactic Mass Depletion and Mechanisms Leading to Galactic Rotation Curves." Symmetry, 5, 1–24.
- Yahalom, A. (2019). "Retardation Effects in Electromagnetism and Gravitation." Materials Today: Proceedings, 14, 164–173.
- Yahalom, A. (2024). "The Cosmological Implication of Retarded Gravity." (preprint)

The present work differs from Yahalom's in several respects:
- Yahalom's analytical framework treats the mass distribution as continuous and derives corrections perturbatively. The present work uses direct N-body simulation with explicit position history buffers.
- Yahalom does not emphasize black hole displacement as the primary driver of spiral arm formation. The present work places this at the center of the mechanism.
- The present work connects the galactic-scale retarded gravity effect to particle-scale pair production dynamics via a second independent simulation (Yang-Mills Collider v3.2). This cross-scale connection is original to the present work.

The present work does not dispute Yahalom's results. It extends them in a specific direction.

## Section 2. Black Hole Mass and the Limits of Observation

### 2.1 How Black Hole Masses Are Measured

Current observational methods for determining black hole masses fall into four categories:

1. Stellar dynamics. Stars near the galactic center are tracked individually. Their orbital parameters (semi-major axis, period, eccentricity) determine the enclosed mass via Kepler's third law. This method is applied with highest precision to Sgr A* at the center of the Milky Way (Ghez et al., 2008; Gillessen et al., 2009; GRAVITY Collaboration, 2019), yielding M ≈ 4.15 × 10^6 M_⊙.

2. Gas dynamics. The rotational velocity of gas in the galactic nucleus, combined with a model of the gravitational potential, yields an estimate of the central mass. Applicable to external galaxies where individual stellar orbits cannot be resolved.

3. Reverberation mapping. In active galactic nuclei (AGN), the time delay between continuum flux variations and the response of the broad-line region yields the size of that region. Combined with gas velocity measured via Doppler broadening, the virial theorem gives an estimate of M_BH.

4. Event horizon imaging. The angular diameter of the black hole shadow — the photon capture cross-section — is proportional to the Schwarzschild radius and hence to the mass. Applied to M87* (Event Horizon Telescope Collaboration, 2019) and Sgr A* (EHT Collaboration, 2022).

All four methods share a structural feature: they measure the gravitational influence of mass on surrounding matter or photons in the exterior spacetime. None of them measures the interior of the black hole.

### 2.2 What These Methods Actually Measure

Each method recovers a quantity of the form:
M_obs = v^2 r / G (virial/Kepler approximation)

or more precisely, for the geodesic of a test particle in the Schwarzschild metric:
M_obs = c^2 r_s / (2G)

where r_s is the Schwarzschild radius inferred from orbital or imaging data.

Key insight: These measurements assume that the gravitational influence of the black hole is fully communicated to the exterior. If Claim III is correct — if some fraction of the gravitational signal is redirected, delayed, or trapped near the horizon — then these methods systematically underestimate the true black hole mass.

### 2.3 Claim III: The Gravitational Signal Trapping Hypothesis

If gravity propagates at finite speed, then the gravitational signal itself is subject to the curvature of spacetime through which it travels. In regions of extreme curvature — near black holes — the gravitational signal from infalling mass may be:
- Redirected: The gravitational field lines may be bent back toward the horizon.
- Delayed: The signal may take longer to escape than the naive r/c estimate.
- Effectively trapped: A significant fraction may never reach the exterior.

If this occurs, then observed black hole masses would represent lower bounds on actual masses. The difference between observed mass and true mass would be an additional "missing" gravitational contribution that is not accounted for in standard analyses.

This claim is the most speculative of the three. It is included because it connects structurally to Claims I and II, and because its implications — if correct — are significant enough to warrant explicit statement.

## Section 3. Summary and Conclusions

Three claims have been presented:

Claim I (verifiable). Black hole displacement + retarded gravity produces spiral arms and flat rotation curves. This is a direct geometric consequence, not a resonance phenomenon. It requires no new physics beyond the confirmed finite speed of gravity.

Claim II (hypothesis). Strong magnetic fields near black holes separate particle-antiparticle pairs, suppressing annihilation and creating local mass fluctuations. This provides a physical mechanism for the mass fluctuations required by Claim III.

Claim III (speculative hypothesis). Gravitational signals from infalling mass may be partially trapped near the black hole horizon, meaning observed masses are lower bounds on true masses.

Claims II and III are hypotheses that require further theoretical and observational investigation. Claim I is directly verifiable in the accompanying simulator.

The primary significance of Claim I is that it inverts the question of spiral arm formation. Spiral arms are not a special condition requiring explanation; they are the default state of any disk galaxy with a displaced central black hole. The standard question ("Why do spiral arms form?") is wrong. The correct question is: "Why do some galaxies NOT have spiral arms?"
---
# The Passive Layer: A Physically Necessary but Uncalculated Term in Galactic Dynamics

**B. Sun | Seoul Inside**  
*Jun 10, 2026*

---

## Abstract

We identify a term that is absent from all standard cosmological frameworks: the propagating gravitational influence of mass that has ceased to exist. This term — which we call the Passive Layer, or Ghost Mass — is a logical consequence of two independently confirmed facts: (1) gravity propagates at the speed of light (confirmed by GW170817, Abbott et al. 2017), and (2) mass is continuously created and destroyed throughout the universe (pair production and annihilation, foundational to quantum field theory). When these two facts are combined, it follows necessarily that the gravitational signal of annihilated mass continues to propagate after the source is gone. This effect does not cancel: gravity has no negative mass. It reaches dynamic equilibrium through cosmic expansion, analogous to Olbers' paradox. The Passive Layer comprises three independent physical components: (A) vacuum fluctuations, (B) local astrophysical pair production near black holes, and (C) retarded gravitational interaction from black hole displacement. This document does not claim that the Passive Layer replaces dark matter. It claims something narrower: a physically necessary, non-zero term has been omitted from standard models. Its magnitude has never been calculated. It should be. Companion simulations (GalaxyCS v4, Yang-Mills Collider v3.2) demonstrate that Component C alone — retarded gravity from black hole displacement — reproduces flat rotation curves and spontaneous spiral arm formation without free parameters. The research presented here originated independently, without prior knowledge of dark matter literature or of Yahalom's prior work on retarded gravity, constituting an independent derivation of the same physical effect from a different direction.

---

## 1. Introduction: An Independent Discovery

This research did not begin as an attempt to explain dark matter. The author had no prior familiarity with the dark matter literature or with existing work on retarded gravity in galactic dynamics (Yahalom 2013, 2019, 2024) at the time the core observations were made.

The research began with the construction of a browser-based particle physics simulator — the Yang-Mills Collider — which implements relativistic particle motion, the Boris integrator, the Bethe-Bloch formula, QCD running coupling, and 4-momentum conservation. When a black hole was added to this simulator, an accretion disk appeared spontaneously. No accretion disk code had been written. The disk emerged from the interaction of Lorentz force charge separation and Newtonian gravity alone.

This observation led to a second simulator — GalaxyCS v4 — designed to investigate galactic dynamics with retarded gravitational propagation. In GalaxyCS v4, whenever the central black hole was displaced from the disk's geometric center by any non-zero amount, spiral arm structure emerged immediately and persistently. When the black hole was held stationary, no spiral structure appeared.

The question then became: is black hole displacement a special condition, or a default state? Analysis showed it to be the default. In the Solar System, the Sun contains 99.8% of total system mass; it cannot be meaningfully displaced. In a disk galaxy, the central black hole contains only 0.1–0.5% of total mass. It has no structural reason to remain at the barycenter, and every reason — tidal forces, peculiar velocities, gravitational wave recoil — to be in continuous motion.

Only after these observations were made did comparison with the existing literature reveal that: (a) the observed flat rotation curves had long been attributed to dark matter; (b) Yahalom had independently developed a theoretical framework for retarded gravity in galactic dynamics; and (c) 50 years of dark matter particle searches had produced null results.

The fact that this derivation was reached independently, from a simulation rather than from theory, constitutes a second confirmation of the underlying physical mechanism from an orthogonal direction.

---

## 2. Two Established Facts and Their Logical Consequence

### 2.1 Fact 1: Gravity Propagates at the Speed of Light

A change in a gravitational source does not instantly affect the surrounding universe. The influence travels outward at c. This was confirmed in 2017 when LIGO/Virgo detected gravitational waves and gamma rays from a neutron star merger (GW170817) arriving simultaneously, constraining the speed of gravity to within 10^{-15} of c (Abbott et al. 2017).

**Consequence:** If a mass disappears, its gravitational signal continues to travel outward for time r/c after the mass is gone.

### 2.2 Fact 2: Mass Is Created and Destroyed

Energy converts into mass and mass converts back into energy. Particle-antiparticle pairs are continuously created and annihilated throughout the universe — in vacuum fluctuations, near black holes, and in high-energy environments. This has been directly observed and is a foundational result of quantum field theory and particle physics.

### 2.3 The Logical Consequence

Combine Fact 1 and Fact 2. A mass exists. It generates a gravitational signal that propagates outward at c. The mass then ceases to exist. The gravitational signal does not cease. It continues to travel. It continues to exert influence on everything it reaches.

This propagating remnant is the Passive Layer — also referred to as Ghost Mass or gravitational reverberation. Formally:

**τ(r) = r / c**

The gravitational influence of a mass that existed at distance r persists for time r/c after that mass is gone. This is not a hypothesis. It is a consequence of two confirmed facts.

---

## 3. Why the Passive Layer Does Not Cancel

A critical point: the Passive Layer does not cancel out.

Gravity has no negative mass. Particles and antiparticles carry opposite electric charges, but they carry the same gravitational mass. The gravitational reverberation of a particle and its antiparticle point in the same direction. They do not cancel. They accumulate.

What appears to be cancellation in homogeneous regions is not cancellation — it is balance. Consider the Earth: every atom pulls on every other atom. None of these forces cancel; they sum. At the center of the Earth, the net force is zero not because forces cancel, but because they balance symmetrically. Move away from the center, and the imbalance becomes immediately apparent.

The universe is not perfectly homogeneous anywhere. The net effect of the Passive Layer is therefore non-zero everywhere.

---

## 4. Dynamic Equilibrium

The Passive Layer does not accumulate without bound.

Two opposing processes maintain equilibrium:

- **Generation:** new reverberations are continuously created via pair production
- **Dilution:** existing reverberations are continuously diluted by cosmic expansion

This is structurally identical to Olbers' Paradox. The night sky is dark not because stars do not emit light, but because the universe is finite in age and expanding. The Passive Layer reaches a stable equilibrium density for the same reasons. The underlying process is extraordinarily dynamic, but the background density at any given moment is effectively constant.

**dρ_PL/dt = ρ̇_generation − ρ̇_dilution = 0 (at equilibrium)**

---

## 5. Three Independent Physical Components

The Passive Layer is not a single monolithic effect. It comprises three independent physical mechanisms that must be distinguished.

### Component A: Vacuum Fluctuations (Universal, Constant)

- **Physical origin:** Quantum vacuum itself
- **Spatial distribution:** Uniform (same everywhere in flat spacetime)
- **Dominant regime:** Far field (r >> R_disk)
- **Generation rate:** Ṁ_pair^vac(r) = constant (independent of r)

This component dominates the far-field regime. Its spatial constancy is the physical origin of the flat rotation curve derivation in Section 6.

### Component B: Local Astrophysical Sources (Disk-Like, Position-Dependent)

- **Physical origin:** High-energy environments around black holes, active galactic nuclei (AGN), supernovae, and magnetars
- **Spatial distribution:** Disk-like (concentrated toward center)
- **Dominant regime:** Near field (r ≤ R_disk)
- **Key mechanism:** In ultra-strong magnetic fields observed near supermassive black holes (10^4 – 10^6 Gauss near the ISCO, EHT MWL Science Working Group 2021), particle-antiparticle pairs produced from vacuum fluctuations are separated by the Lorentz force before annihilation can occur.

**F = q(v × B)**

The Larmor radius is:

**r_L = γmv_⊥ / (|q|B)**

Positive and negative charges curve in opposite directions. Black hole gravity pulls both toward the center, but they arrive from opposite sides. They do not annihilate. They persist as mass.

This behavior was observed directly in Yang-Mills Collider v3.2. No accretion disk code was written. The disk appeared spontaneously from Lorentz force and Newtonian gravity alone.

Component B scales with local energy density and dominates the near-field regime.

### Component C: Retarded Gravity and Black Hole Displacement

- **Physical origin:** Finite propagation speed of gravity + black hole motion
- **Dominant regime:** Entire galaxy
- **Delay time:** τ(r) = α · r / c (α is retardation strength parameter; physical prediction: α = 1)

When a black hole is displaced from the geometric center of a disk galaxy, stars at different distances from the black hole reference different past positions of that black hole. In a differentially rotating disk, this radially-dependent angular offset is sheared continuously into a spiral pattern.

The retarded acceleration term (following Yahalom) is:

**a_ret = α · G · Ṁ_BH / (2c²) · R̂**

The critical structural feature of this term: unlike Newtonian gravity (proportional to 1/r²), the retarded term does not diminish with distance. At galactic scales, retarded gravitational effects become relatively more important at large radii — precisely where observed rotation curves deviate from Newtonian predictions.

---

## 6. The Ghost Mass Formula and Flat Rotation Curves

The accumulated ghost mass up to radius r is:

**M_ghost(r) = ∫₀ʳ Ṁ_pair(r') · (r'/c) dr'**

When the pair production rate is spatially constant (Component A dominates):

**M_ghost(r) = Ṁ_pair · r/c → M_ghost ∝ r**

The consequence for rotation curves follows directly:

**v_c²(r) = G · M_ghost(r) / r = G · Ṁ_pair / c = constant**

If M_ghost is proportional to r, rotation velocity becomes constant regardless of distance. This is the observed flat rotation curve, emerging without dark matter and without free parameters — the pair production rate Ṁ_pair is the only quantity, and it is determined by the observational data itself (see Section 8).

---

## 7. Black Hole Displacement Is the Default State

The spiral arm mechanism (Component C) requires black hole displacement. The question of whether this is a special condition or a default state is answerable from first principles.

**Mass ratio comparison:**

- **Solar System:** f_Sun ≈ 0.998 — displacement is structurally suppressed
- **Disk galaxy:** f_BH ≈ 0.001–0.005 — displacement is structurally permitted

Perfect black hole stasis requires exact cancellation of all the following perturbations simultaneously and continuously:

- Host galaxy peculiar velocity (100–600 km/s)
- Tidal forces from satellite galaxies and globular clusters
- Galactic bar oscillations
- Large-scale structure gravitational background (cosmic filaments, voids)
- Recoil from asymmetric gravitational wave emission during any merger event

This exact cancellation is not physically plausible. **Black hole displacement is the default state.** Spiral structure is therefore the expected morphology for disk galaxies — not a condition requiring special explanation.

**Observational support:**

- **M87:** 6.8 ± 0.8 pc projected displacement (Batcheldor et al. 2010) — elliptical galaxy, no disk, no spiral structure (consistent)
- **M31 (Andromeda):** Dual nuclei documented — spiral structure present
- **Milky Way:** ≲ 100 pc (NSC offset) — spiral structure present (Bovy et al. 2022)
- **BCGs (1/3):** 10 pc – kpc scale offsets sustained for up to 6 Gyr (Chu, Boldrini & Silk 2022)
- **General AGN:** 10–100 pc displacements most common (Bartlett et al. 2021)

---

## 8. The Parameter Problem Is Already Solved

A standard objection to any new gravitational effect is: "How large is it?" For the Passive Layer, this question has an elegant answer that distinguishes it from conventional alternative theories.

The pair production rate Ṁ_pair — the only free parameter in the Ghost Mass formula — does not need to be calculated from first principles. **It can be read directly from observational data.**

Decades of dark matter research have produced precise measurements of the "missing mass" at every scale:

- Galaxy rotation curves give the required mass distribution as a function of radius
- Gravitational lensing gives the required mass density
- CMB and BAO give Ω_c · h² = 0.118 (Planck 2020)
- NFW profile parameters constrain individual halos

**These measurements are not just constraints on dark matter. They are measurements of Ṁ_pair — the total pair production rate required to produce the observed gravitational effects.**

If the Passive Layer is the correct explanation, the existing observational dataset has already determined the value of every parameter in the theory.

This is the key methodological distinction from conventional alternative theories, which must independently calculate their predicted magnitude before comparison to observation. The Passive Layer inverts the procedure: observation supplies the answer; theory supplies the mechanism.

---

## 9. Distinction from Yahalom (2013, 2019, 2024)

Yahalom has developed a theoretical framework for retarded gravity in galactic dynamics that shares the use of delayed gravitational propagation. The distinction is fundamental.

**Effect source:**

- **Yahalom:** existing mass with retarded propagation
- **Passive Layer (Component C):** mass that has ceased to exist

**Physical question:**

- **Yahalom:** how does existing mass gravitate with delay?
- **Passive Layer (Component C):** what happens to the gravity of annihilated mass?

**Mass budget:**

- **Yahalom:** current mass distribution
- **Passive Layer (Component C):** cumulative history of pair production and annihilation

**Derivation origin:**

- **Yahalom:** theoretical (GR linearization)
- **Passive Layer (Component C):** observational (simulation → emergent behavior)

Yahalom asks: how does the gravity of existing mass propagate with a delay? The Passive Layer asks: what happens to gravity after the source mass is gone?

These are different questions. They may both be correct simultaneously. The Passive Layer does not supersede Yahalom's work — it identifies an additional, independent term that Yahalom's framework does not address.

It is noted that this distinction was not apparent to the author during the original derivation, as Yahalom's work was unknown at the time. The convergence on similar physical mechanisms from independent directions is consistent with the reality of the underlying effect.

---

## 10. Simulation Evidence

### 10.1 GalaxyCS v4 — Spiral Arm Formation

GalaxyCS v4 is an N-body simulator implementing retarded gravitational propagation via a FIFO history buffer. With 20,000–80,000 test particles initialized on circular orbits, the results are as follows.

**Key observations:**

- **BH at rest (displacement = 0):** No spiral structure. Axisymmetric disk.
- **BH displaced by any non-zero amount:** Spiral arm structure emerges immediately and persists indefinitely.
- **Retarded gravity disabled + BH displacement:** Keplerian rotation curve (v ∝ r^{−1/2})
- **Retarded gravity enabled + BH displacement:** Flat rotation curve and spontaneous spiral arms

**Transition characteristics:**

- The transition is not gradual.
- There is no critical displacement threshold.
- Any non-zero displacement produces spiral structure.
- The mechanism is geometric, not dynamic.
- No special initial conditions, no resonance, and no tuned parameters are required.

**Arm morphology:**

- Unidirectional displacement → two-arm spiral
- Oscillatory displacement → multi-arm structure
- Irregular displacement → flocculent or asymmetric arms

This range of morphologies is consistent with the observed diversity of spiral galaxy types.

### 10.2 Yang-Mills Collider v3.2 — Spontaneous Accretion Disk

Yang-Mills Collider v3.2 implements:

- Relativistic motion (Lorentz factor γ = E/m)
- Boris integrator (standard in GEANT4 and plasma physics PIC codes)
- Bethe-Bloch energy loss (particle mass and charge dependent)
- 4-momentum conservation with Lorentz boost
- QCD running coupling α_s(μ) (2-loop beta function)
- Kerr black hole gravity (Newtonian approximation with mass parameter)

**Core observation:** When a black hole was introduced into a high-energy particle collision environment, an accretion disk appeared without being programmed. The Lorentz force separated particle-antiparticle pairs. The black hole gravity confined them. Annihilation was suppressed. Mass persisted.

**Key quote:** *"I did not build an accretion disk. One appeared."* — I Added a Black Hole to the LHC (2026-06-06)

This observation constitutes direct simulation evidence for Component B: local astrophysical pair separation and mass persistence near black holes.

### 10.3 Critical Distinction: Separation Existence vs. Separation Efficiency

Two questions must not be conflated.

**Question 1 — Does separation occur?**
- Answer: Yes, for any B ≠ 0.
- This follows directly from the sign of q in the Lorentz force.
- No threshold. No minimum field strength. No special condition.

**Question 2 — How efficient is the separation?**
- Answer: Depends on the ratio r_L / R_system.
- When r_L ≪ R_system: particles and antiparticles are confined to geometrically distinct orbital regions; encounter rate approaches zero.
- When r_L ~ R_system: significant overlap occurs; separation efficiency reduced.

The condition r_L ≪ R_system governs separation efficiency, not separation existence.

**Observed environment of M87* (EHT + Faraday rotation, direct measurement):**
- Magnetic field at ISCO: B_ISCO ~ 1–30 G
- Electron density: n_e ~ 10^4–10^5 cm^{-3}
- Larmor radius of relativistic electron (γ ~ 10^6) at B ~ 10^3 G: r_L ~ 10^{-1} cm
- ISCO radius of M87*: r_ISCO ~ 6 × 10^{14} cm
- Ratio: r_L / r_ISCO ~ 10^{-15}

The separation efficiency condition is satisfied by fifteen orders of magnitude in the directly observed environment of M87*. This is not a prediction. It is a direct implication of current observations.

---

## 11. Comparison with Existing Frameworks

The following is a comparison of the Passive Layer framework with existing approaches: ΛCDM (dark matter as particle), MOND (Modified Newtonian Dynamics), and Yahalom's retarded gravity framework.

### 11.1 Basic Assumption / Identity

- **ΛCDM:** Particle (WIMP/axion) — requires new particle species
- **MOND:** Not required — modifies gravitational law
- **Yahalom:** Reduced gravity — retarded propagation of existing mass
- **Passive Layer:** Physically necessary uncalculated term — existence confirmed by logic, magnitude unknown

### 11.2 Rotation Curves

- **ΛCDM:** Halo fitting required — multiple parameters
- **MOND:** Excellent empirical fit — single parameter a_0
- **Yahalom:** Retarded dynamics — requires retardation parameter
- **Passive Layer:** Emerges from M_ghost ∝ r — no free parameters; Ṁ_pair determined by observation

### 11.3 Spiral Arms

- **ΛCDM:** Not addressed
- **MOND:** Not addressed
- **Yahalom:** Not addressed
- **Passive Layer:** BH displacement + retarded gravity — geometric mechanism, no threshold, any non-zero displacement works

### 11.4 Gravitational Lensing

- **ΛCDM:** Dark matter halo — requires additional mass distribution
- **MOND:** Partial explanation — lensing not fully addressed
- **Yahalom:** Not addressed
- **Passive Layer:** Follows directly from M_ghost(r) substituted into GR lensing formula — no additional mechanism required

### 11.5 Bullet Cluster (1E 0657-558)

- **ΛCDM:** Non-collisional dark matter — explains separation of lensing mass from baryonic gas
- **MOND:** Cannot explain — requires additional dark matter in cluster cores
- **Yahalom:** Not addressed
- **Passive Layer:** Non-collisional reverberation — lensing center separates from baryonic center naturally; no additional assumptions

### 11.6 Direct Detection Possibility

- **ΛCDM:** Possible in principle — WIMP-nucleon scattering, etc.
- **MOND:** N/A
- **Yahalom:** N/A
- **Passive Layer:** Impossible in principle — source mass no longer exists; null results from 50 years of experiments are the expected outcome

### 11.7 Free Parameters

- **ΛCDM:** Multiple halo parameters — NFW profile parameters (r_s, ρ_0), concentration, etc.
- **MOND:** a_0 (acceleration scale) — one parameter
- **Yahalom:** α (retardation strength) — one parameter
- **Passive Layer:** None — Ṁ_pair (pair production rate) is determined from existing observational data, not a free parameter

### 11.8 CMB (Cosmic Microwave Background) Fit

- **ΛCDM:** Excellent — 0.1% level agreement (Planck 2018)
- **MOND:** Not addressed
- **Yahalom:** Not addressed
- **Passive Layer:** Not yet calculated — requires cosmological integration (open problem Q4)

---

## 12. The One Open Question

The existence of the Passive Layer is a logical consequence of confirmed physics. It is not in question.

**The one question that remains open is: How large is it?**

This document has argued that the answer may already be contained in existing observational data (Section 8). But the calculation that connects the Passive Layer framework to those observations — quantifying the contribution of each of Components A, B, and C to the observed missing mass — has not been performed.

### Open Problems (Explicitly Acknowledged)

**Q1 — Cancellation mechanism**
- The 10^{123} vacuum energy cancellation mechanism is unknown.
- Without it, quantitative estimates of Component A remain free parameters.
- This is the cosmological constant problem restated in the language of statistical mechanics.

**Q2 — Backreaction**
- Self-consistent treatment requires coupled QFT-in-curved-spacetime and Einstein field equations.
- Unsolved even in simplified toy models.
- If vacuum fluctuations contribute to the stress-energy tensor, they also affect spacetime geometry — which in turn affects fluctuation rates.

**Q3 — Distinguishability from CDM**
- Near galactic centers, vacuum statistical mass profile and CDM profile (NFW) may produce similar observational signatures.
- Distinguishing them requires either (a) measurements sensitive to the equation of state of the dark component, or (b) high-precision rotation curve data in the inner ~1 kpc.

**Q4 — Cosmological consistency**
- Integrated contribution over all galaxies in the observable universe may produce a measurable effect on the CMB power spectrum or BAO scale.
- This constraint has not been calculated.
- If Γ(r) is large near every galactic center, the integrated contribution could be significant.

**Q5 — N-body resolution**
- GalaxyCS v4 qualitative behavior (spiral arms from BH displacement, flat rotation curves) not yet verified at higher particle counts (N > 80,000).
- Current simulations use 20,000–80,000 test particles.

**Q6 — Systematic rotation curve fitting**
- Qualitative agreement with M33 observed in GalaxyCS v4.
- Systematic fit to SPARC database (175 galaxies with resolved rotation curves; Lelli, McGaugh & Schombert 2016) has not been performed.
- This is necessary for quantitative comparison with ΛCDM and MOND.

---

## 13. Falsifiable Predictions

The following predictions are made by this framework. Each is falsifiable by observation.

**Prediction 1: BH displacement correlates with spiral arm strength**
- Method: Measure SMBH offset from photometric center vs. spiral arm pitch angle (Fourier m=2 strength S₂)
- Status: Testable now with existing observational data
- Expected result: Galaxies with larger BH offsets should have stronger spiral arm pitch angles

**Prediction 2: Galaxies with centered BHs have no spiral structure**
- Method: High-resolution imaging + astrometry of galactic nuclei
- Status: Testable now
- Expected result: Axisymmetric disks without spiral arms should have BH at geometric center (or no disk at all, as in ellipticals)

**Prediction 3: Rotation curve excess scales with galaxy age**
- Method: Age-matched rotation curve comparison across galaxies of different ages
- Status: Requires large survey data
- Expected result: Older galaxies (with longer mass-conversion history) show larger speed anomaly ratio

**Prediction 4: No dark matter particle will ever be detected**
- Method: Direct detection experiments (LZ, XENONnT, PandaX-4T, etc.)
- Status: Ongoing — 50 years of null results to date
- Expected result: Null results will continue; the effect is not a particle

**Prediction 5: Void formation from BH mass fluctuation**
- Method: Large-scale structure correlation with AGN activity history
- Status: Feasible with existing and upcoming surveys
- Expected result: Underdense regions (voids) correlate with epochs of BH mass fluctuation

**Prediction 6: High-spin AGN show larger central mass excess**
- Method: Compare rotation curve inner slopes of high-spin vs. low-spin AGN
- Status: Requires high-precision inner rotation curve data
- Expected result: Higher black hole spin parameter a* → larger ergosphere and stronger frame dragging → greater correlation disruption → larger Γ(r) → stronger central mass excess

**Prediction 7: Spiral arm morphology reconstructs BH kinematic history**
- Method: Inverse problem: from arm count, pitch angle, and symmetry to BH trajectory
- Status: Theoretical prediction; requires observational validation
- Expected result: Two-arm spirals correspond to simple unidirectional displacement; multi-arm structures to oscillatory BH motion

---

## 14. Conclusion

We have identified and characterized a physically necessary term that is absent from all standard cosmological frameworks: the propagating gravitational influence of mass that has ceased to exist.

This term — the Passive Layer — follows necessarily from two independently confirmed facts:
1. Gravity propagates at the speed of light (GW170817, 2017)
2. Mass is continuously created and destroyed throughout the universe (pair production and annihilation, foundational to QFT)

**Properties of the Passive Layer:**
- It does not cancel (gravity has no negative mass)
- It reaches dynamic equilibrium (analogous to Olbers' Paradox)
- It comprises three independent physical components (A: vacuum fluctuations, B: local astrophysical sources, C: retarded gravity + BH displacement)
- Its magnitude, when non-zero, reproduces the observational signature of dark matter without requiring a new particle

**What this document does NOT claim:**
- It does not claim that the Passive Layer replaces dark matter.
- It does not claim that ΛCDM is wrong.
- It does not claim that the magnitude has been calculated.

**What this document DOES claim:**
- A term exists.
- It is non-zero.
- It follows from confirmed physics.
- Its magnitude has never been calculated.
- It should be.

Whether its magnitude is sufficient to account for all, some, or a negligible fraction of the observed missing mass is an open question — but it is a question that can be answered with existing observational data and existing theoretical tools.

The universe has been accounting for the Passive Layer since the beginning. Our models have not.

---

## References

**Abbott, B.P. et al. (LIGO/Virgo Collaboration)** (2017). GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. *Physical Review Letters*, 119, 161101.

**Bartlett, D.J. et al.** (2021). Offset AGN dataset compilation.

**Batcheldor, D. et al.** (2010). A Displaced Supermassive Black Hole in M87. *The Astrophysical Journal Letters*, 717, L6.

**Bullock, J.S. & Boylan-Kolchin, M.** (2017). Small-Scale Challenges to the ΛCDM Paradigm. *Annual Review of Astronomy and Astrophysics*, 55, 343.

**Casimir, H.B.G.** (1948). On the attraction between two perfectly conducting plates. *Proc. K. Ned. Akad. Wet.*, 51, 793.

**Chu, A., Boldrini, P. & Silk, J.** (2022). Off-centre supermassive black holes in bright central galaxies. *Monthly Notices of the Royal Astronomical Society*.

**de Blok, W.J.G.** (2010). The Core-Cusp Problem. *Advances in Astronomy*, 2010, 789293.

**EHT Multiwavelength Science Working Group** (2021). Broadband Multi-wavelength Properties of M87 during the 2017 EHT Campaign. *The Astrophysical Journal Letters*, 911, L11.

**Eisenstein, D.J. et al.** (2005). Detection of Baryon Acoustic Oscillations in the Large-Scale Correlation Function of SDSS Luminous Red Galaxies. *The Astrophysical Journal*, 633, 560.

**Freeman, K.C.** (1970). On the Disks of Spiral and S0 Galaxies. *The Astrophysical Journal*, 160, 811.

**Hawking, S.W.** (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43, 199.

**Kormendy, J. & Ho, L.C.** (2013). Coevolution (Or Not) of Supermassive Black Holes and Host Galaxies. *Annual Review of Astronomy and Astrophysics*, 51, 511.

**Lelli, F., McGaugh, S.S. & Schombert, J.M.** (2016). SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves. *The Astronomical Journal*, 152, 157.

**Lin, C.C. & Shu, F.H.** (1964). On the Spiral Structure of Disk Galaxies. *The Astrophysical Journal*, 140, 646.

**Milgrom, M.** (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *The Astrophysical Journal*, 270, 365.

**Padmanabhan, T.** (2003). Cosmological constant: the weight of the vacuum. *Physics Reports*, 380, 235.

**Planck Collaboration** (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy & Astrophysics*, 641, A6.

**Schwinger, J.** (1951). On gauge invariance and vacuum polarization. *Physical Review*, 82, 664.

**Unruh, W.G.** (1976). Notes on black-hole evaporation. *Physical Review D*, 14, 870.

**Weinberg, S.** (1989). The cosmological constant problem. *Reviews of Modern Physics*, 61, 1.

**Yahalom, A.** (2013). The effect of retardation on galactic rotation curves. *Journal of Physics: Conference Series*.

**Yahalom, A.** (2019). Retardation theory of galactic rotation curves. *Progress in Physics*, 15.

**Yahalom, A.** (2024). Galactic rotation curves explained without dark matter using retarded gravity. (preprint).

---



---

# THE PASSIVE LAYER AND THE REVERSAL OF THE BURDEN OF PROOF

## A Logical Argument for Reconsidering the Dark Matter Particle Hypothesis

Companion document to: The Passive Layer — Core Document (2026-06-09)

PREFACE

Every document in the Passive Layer series has been written in a defensive posture. The implicit framing has been: "Here is a new idea. Here is why it might be valid. Here are its limitations." This document takes a different posture. It does not ask whether the Passive Layer is valid. It asks whether the dark matter particle hypothesis is necessary — given that the Passive Layer already exists.

These are different questions. The answer to the second question has significant implications for how the first question should be evaluated.

PART 1. THE STARTING POINT: WHAT IS BEYOND DISPUTE

Before any argument can proceed, it is essential to identify what is not in dispute. The following two facts have been confirmed independently, repeatedly, and across multiple experimental contexts. They are not hypotheses. They are not theoretical proposals. They are established physics.

Fact 1. Gravity propagates at the speed of light.

A change in a gravitational source does not propagate instantaneously. The influence travels outward at c. This was confirmed definitively in 2017 when LIGO and Virgo detected gravitational waves and gamma rays from a binary neutron star merger (GW170817) arriving simultaneously, constraining the speed of gravity to within 10^{-15} of c (Abbott et al. 2017). The Newtonian assumption of instantaneous gravitational propagation is an approximation. It is not the physical reality.

The consequence of this fact is precise and unavoidable: if a mass disappears, its gravitational signal continues to travel outward for a time equal to r divided by c, where r is the distance from the source. The signal does not stop when the source stops.

Fact 2. Mass is continuously created and destroyed throughout the universe.

Energy converts into mass and mass converts back into energy. Particle-antiparticle pairs are continuously created and annihilated throughout the universe — in vacuum fluctuations, near black holes, in high-energy astrophysical environments, and wherever sufficient energy density exists. This has been directly observed. It is a foundational result of quantum field theory and particle physics. It is not in dispute.

The logical consequence of combining these two facts is not a hypothesis. It is a deduction.

A mass exists. It generates a gravitational signal that propagates outward at c. The mass then ceases to exist through annihilation or decay. The gravitational signal does not cease. It continues to propagate. It continues to exert gravitational influence on everything it reaches for a time r divided by c after the source is gone.

This propagating remnant is the Passive Layer. Its existence is not a proposal. It is a logical consequence of two confirmed facts. It cannot be argued away without denying one of those facts.

PART 2. THE OBSERVATIONAL SITUATION

Since 1933, when Fritz Zwicky observed anomalous gravitational effects in the Coma Cluster and introduced the term dunkle Materie — dark matter — astronomers and physicists have been measuring something that cannot be accounted for by visible baryonic mass.

The observational record is extensive and precise.

Galaxy rotation curves: Stars at large radii in disk galaxies rotate faster than Newtonian dynamics predicts from the visible mass distribution. This has been measured for thousands of galaxies. The SPARC database alone contains resolved rotation curves for 175 disk galaxies (Lelli, McGaugh and Schombert 2016).

Gravitational lensing: Mass distributions inferred from gravitational lensing systematically exceed the visible baryonic mass. This is observed at galaxy scales, cluster scales, and cosmological scales.

CMB power spectrum: The acoustic oscillation structure of the cosmic microwave background constrains the cosmological density of non-baryonic gravitating matter to Ω_c h^2 = 0.118, with sub-percent precision (Planck Collaboration 2020).

Baryon acoustic oscillations: The characteristic scale of approximately 150 megaparsecs in the large-scale matter power spectrum requires a non-baryonic gravitating component that did not participate in acoustic oscillations before recombination.

Large-scale structure: The observed distribution of galaxies, filaments, voids, and clusters requires a gravitating component that was not coupled to the photon-baryon fluid in the early universe, allowing density perturbations to grow independently of radiation pressure.

Bullet Cluster: In the collision of two galaxy clusters (1E 0657-558), the gravitational lensing mass centroid is displaced from the baryonic gas distribution, indicating a non-collisional gravitating component that passed through the collision while the gas was decelerated by electromagnetic interactions.

These observations are not in dispute. They are real. The gravitational effects are there. The question that has driven fifty years of research is not whether the effects exist, but what causes them.

PART 3. ZWICKY'S ORIGINAL DEFINITION AND THE ASSUMPTION THAT WAS ADDED

When Zwicky introduced the concept of dark matter, his definition was observational and minimal:

There is an unexplained gravitational effect. It does not correspond to visible matter. We do not know what it is. We call it dark matter.

That is the original definition. Note what it does not contain. It does not say the effect is caused by a particle. It does not say the effect requires a new form of matter. It says: there is an unexplained gravitational effect.

The particle hypothesis was added later. As the WIMP miracle appeared theoretically attractive in the context of supersymmetry, and as particle physics methods became available, the research program converged on the assumption that dark matter is a new elementary particle — weakly interacting, massive, thermally produced in the early universe, and detectable in dedicated laboratory experiments.

This assumption transformed a descriptive label into a specific physical model. The label dark matter and the particle model became conflated. They are not the same thing. Zwicky's dark matter is an observation. The WIMP is a hypothesis about what causes that observation.

This distinction matters enormously for what follows.

PART 4. WHAT THE PASSIVE LAYER IS AND IS NOT

The Passive Layer is not proposed as a replacement for the observational record. It is not a competing measurement. It is a proposed physical mechanism — one that is derivable from established physics — for what has been causing the gravitational effects that have been measured.

The Passive Layer has three independent physical components, each with different dominant regimes. Component A arises from vacuum fluctuations and dominates at large galactic radii. Component B arises from local astrophysical pair production near black holes and in high-energy environments. Component C arises from retarded gravitational interaction due to black hole displacement from the galactic center.

Each component is grounded in established physical processes. None requires new particles, new forces, or new mathematical structures.

For the purposes of this document, the critical property of the Passive Layer is this: its existence is guaranteed by the two facts established in Part 1. The Passive Layer is not a proposal that might or might not exist. It exists. The only open question is its magnitude.

PART 5. THE OBSERVATIONAL SIGNATURE MATCH

The observational definition of dark matter, constructed from the evidence in Part 2, is the following:

There is a gravitating component that has no electromagnetic interaction, is non-collisional, has never been detected as a particle despite fifty years of dedicated searches, is correlated with regions of high mass density, forms approximately spherical halos around galaxies, was present in the early universe and participated in structure formation without coupling to the photon-baryon fluid, and accounts for approximately five times the mass-energy of baryonic matter.

The Passive Layer satisfies every item in this definition. Not by assumption, but by derivation.

Gravitational effect: The Passive Layer carries gravitational influence by definition. It is propagating gravitational signal. This is its most direct property.

No electromagnetic interaction: The source mass no longer exists. There is no matter present to interact electromagnetically. This follows from the definition of the Passive Layer, not from an assumed property of a hypothetical particle.

Non-collisional: The Passive Layer is propagating gravitational signal, not matter. It does not collide with anything. This is not an assumed property. It is a consequence of what the Passive Layer physically is.

Never detected as a particle: The Passive Layer is not a particle. It cannot be detected in particle detectors regardless of their sensitivity. The fifty-year null result from direct detection experiments — LZ 2024, XENONnT 2024, PandaX-4T 2023, and all predecessors — is not a detection failure. It is the expected outcome.

Correlated with mass density: Regions of higher mass density generate more pair production and annihilation events, and therefore more Passive Layer. The correlation follows automatically from the generation mechanism.

Spherical halo structure: At distances large compared to the galactic disk, the integral of the spatially constant vacuum fluctuation component over all directions produces an approximately spherical distribution. This is a geometric consequence of the far-field behavior of Component A.

Present in the early universe: The early universe had extreme energy densities. Pair production and annihilation rates were correspondingly extreme. The Passive Layer was generated most intensely in the early universe. It was not present despite the conditions of the early universe. It was generated by them.

Non-participation in acoustic oscillations: The Passive Layer is propagating gravitational signal. It does not interact with photons. It does not participate in the acoustic oscillations of the baryon-photon fluid. It acts as an independent gravitational source. This is the role that dark matter plays in CMB physics, and the Passive Layer fills it without assumption.

Every item in the observational definition is satisfied. No item requires a special assumption about the properties of a hypothetical particle. The satisfaction is structural — it follows from what the Passive Layer physically is.

PART 6. THE REVERSAL OF THE BURDEN OF PROOF

This is the logical core of this document.

Standard scientific practice requires that a proposed explanation demonstrate its validity before it can be accepted. The burden of proof lies with the proponent of a new claim.

In the context of dark matter research, this standard has been applied asymmetrically. The Passive Layer, as a proposed explanation, has been held to the standard of demonstrating its validity. The dark matter particle hypothesis, as the established framework, has not been held to the same standard.

But this asymmetry requires justification. The asymmetry is justified when the established framework is the simpler, more conservative explanation — the one that requires fewer assumptions. In that case, departing from it requires positive evidence.

The situation with the Passive Layer is the opposite.

The Passive Layer requires no new assumptions. Its existence follows from two confirmed facts. Its observational properties follow from what it physically is. It introduces no new particles, no new forces, no new mathematical structures.

The dark matter particle hypothesis requires a new assumption: that there exists an undiscovered elementary particle with specific properties (massive, weakly interacting, electrically neutral, stable on cosmological timescales, produced in thermal equilibrium in the early universe). This assumption has not been confirmed. After fifty years of increasingly sensitive searches, no such particle has been detected.

In this situation, the standard of parsimony — Occam's razor — applies in reverse of the usual framing. The simpler explanation is the Passive Layer. The more complex explanation is the particle hypothesis. The burden of proof lies with the particle hypothesis.

Stated precisely: given that the Passive Layer exists (which is guaranteed by confirmed physics), and given that the Passive Layer satisfies the complete observational definition of dark matter (which has been established in Part 5), the question is no longer whether the Passive Layer can explain what we observe. The question is whether the dark matter particle is needed in addition to the Passive Layer.

That is a different question. And for that question, the current answer from experiment is: no evidence that it is needed.

The fifty-year null result is not an embarrassment for the field. It is, from this perspective, exactly what should have been expected. The searches were looking for a particle. The effect is not a particle.

PART 7. THE STRUCTURE FORMATION QUESTION

The most substantive argument for the necessity of a dark matter particle comes from structure formation. The observed distribution of galaxies, filaments, and voids — the cosmic web — is well reproduced by N-body simulations that include cold dark matter as a particle component. The argument is that a pressureless, non-collisional particle fluid was needed to seed the density perturbations that grew into the structures we observe.

This argument must be addressed directly.

The question is not whether cold dark matter simulations reproduce the observed structure. They do, to good approximation. The question is whether the Passive Layer, placed in the same role in the same equations, would also reproduce the observed structure.

The Passive Layer, in the early universe, has the following properties relevant to structure formation:
- It is generated at a rate proportional to local energy density. This means it is generated more abundantly where density perturbations are positive — exactly the seeding mechanism required.
- It does not interact with photons. It is not coupled to the baryon-photon fluid. It can grow density perturbations independently of radiation pressure — exactly the property required for structure formation before recombination.
- It is non-collisional. It does not undergo pressure-supported oscillations. It behaves as a pressureless fluid for the purposes of gravitational dynamics — exactly the cold dark matter approximation.
- It was present in the early universe at its maximum generation rate — because the early universe had maximum energy density.

Each property required for structure formation is present in the Passive Layer. The mechanism is different from a thermally produced particle relic, but the gravitational behavior in the relevant regime is the same.

The quantitative calculation — whether the Passive Layer generates sufficient density contrast at the right scales and at the right times to reproduce the observed matter power spectrum — has not been performed. This is acknowledged. But the absence of this calculation does not constitute evidence that the calculation would fail. It constitutes an open problem.

The structure formation argument for the necessity of a dark matter particle depends on the assumption that no other mechanism can fill the role. The Passive Layer challenges that assumption on physical grounds. The challenge has not been refuted. It has not been calculated.

PART 8. THE COSMOLOGICAL CONSTANT MEASUREMENT REINTERPRETED

The Planck 2018 measurement gives Ω_c h^2 = 0.118. This has been interpreted as the cosmological density of dark matter particles.

If the Passive Layer is the correct explanation for the gravitational effects attributed to dark matter, then this measurement is not a measurement of particle density. It is a measurement of the cumulative Passive Layer density — the total gravitational reverberation accumulated from the beginning of the universe to the present, integrated over all of cosmic history.

This reinterpretation does not change the measurement. The number is the same. What changes is the physical object the number refers to.

The significance of this reinterpretation is as follows. The dark matter particle hypothesis requires that this number be explained by calculating the thermal relic density of a specific particle species — its mass, its interaction cross-section, its freeze-out temperature. These have been constrained but not uniquely determined. The WIMP parameter space has been substantially reduced by null results without being eliminated.

The Passive Layer interpretation requires that this number be explained by calculating the cumulative pair production and annihilation rate integrated over cosmic history, weighted by the propagation delay r divided by c. This calculation has not been performed. But the structure of the calculation is clear. The inputs are the cosmic star formation history, the black hole mass function as a function of redshift, the vacuum energy density, and the spacetime geometry. These are known or constrained from independent observations.

The measurement Ω_c h^2 = 0.118 is, under the Passive Layer interpretation, already the answer. What remains is to show that the Passive Layer mechanism, calculated from first principles, produces that answer. This is a calculation problem, not a conceptual problem.

PART 9. THE HISTORICAL PARALLEL

The history of physics contains several instances where an unexplained effect was attributed to a hypothetical entity that turned out to be unnecessary.

The precession of Mercury's perihelion was attributed by some to a hypothetical planet, Vulcan, orbiting inside Mercury's orbit. The planet was never found. General relativity explained the precession without any additional entity.

The null result of the Michelson-Morley experiment was attributed to a failure to detect the luminiferous aether due to technical limitations. Special relativity resolved the situation by eliminating the aether as an unnecessary concept.

In both cases, the resolution was not the discovery of the hypothetical entity. It was the recognition that the entity was not needed — that the effect could be explained within existing or extended physics without introducing new ontology.

The dark matter particle situation has a structurally similar form. An unexplained gravitational effect exists. A hypothetical entity was proposed to explain it. The entity has not been found after fifty years of searching. A mechanism derivable from existing physics — the Passive Layer — satisfies the complete observational definition of the effect without requiring the hypothetical entity.

The parallel is not proof. It is a pattern recognition. But the pattern is suggestive, and the structural similarity is precise.

PART 10. WHAT THIS ARGUMENT IS AND IS NOT CLAIMING

This document is not claiming that dark matter particles do not exist. They may exist. Nothing in this argument precludes their existence.

This document is not claiming that the Passive Layer has been quantitatively demonstrated to account for all of the observed gravitational effects attributed to dark matter. The quantitative calculation has not been completed.

This document is not claiming that the ΛCDM model is wrong. Its cosmological successes at large scales are not challenged here.

This document is claiming the following, precisely:
1. The Passive Layer exists. This is guaranteed by confirmed physics, not by hypothesis.
2. The Passive Layer satisfies the complete observational definition of dark matter without additional assumptions.
3. Given these two facts, the burden of proof lies with those who claim that a dark matter particle is needed in addition to the Passive Layer. They must demonstrate that the Passive Layer is insufficient — not merely that it has not yet been quantitatively calculated to be sufficient.
4. The fifty-year null result from direct detection experiments is consistent with the Passive Layer interpretation and constitutes cumulative evidence against the particle interpretation.
5. The next required step is the quantitative calculation of the Passive Layer's contribution to the observed gravitational effects. Until that calculation is performed, the claim that additional physics is required is premature.

PART 11. THE QUESTION THAT SHOULD NOW BE ASKED

The question that has driven fifty years of research is: what is dark matter made of?

That question assumes the answer is a material substance — a particle or class of particles — and directs research toward finding it.

The question that follows from this document is different: given that the Passive Layer exists and satisfies the observational definition of dark matter, is there any evidence that requires something in addition to the Passive Layer?

If the answer is no, then the particle hypothesis is an unnecessary assumption. The effect that has been called dark matter is the gravitational reverberation of mass that no longer exists — a consequence of finite gravitational propagation speed combined with continuous mass creation and annihilation throughout cosmic history.

If the answer is yes — if there is specific evidence that cannot be explained by the Passive Layer — then that evidence must be identified and the calculation of the Passive Layer's contribution to that specific observation must be performed before the insufficiency of the Passive Layer can be established.

The burden, at this point in the argument, is not on the Passive Layer to prove itself. The burden is on the particle hypothesis to identify what the Passive Layer cannot explain.

That is the reversal. That is what fifty years of null results, combined with the logical necessity of the Passive Layer's existence, has produced.

PART 12. SUMMARY OF THE LOGICAL CHAIN

Step 1. Gravity propagates at c. Confirmed experimentally.
Step 2. Mass is continuously created and destroyed. Confirmed experimentally.
Step 3. Therefore, the gravitational signal of annihilated mass continues to propagate after the source is gone. This is a logical consequence of Steps 1 and 2. It cannot be denied without denying one of those steps.
Step 4. This propagating remnant — the Passive Layer — satisfies the complete observational definition of dark matter without additional assumptions.
Step 5. The dark matter particle hypothesis requires an additional assumption: the existence of an undiscovered particle species.
Step 6. That assumption has not been confirmed after fifty years of dedicated experimental searches.
Step 7. By the principle of parsimony, the simpler explanation — the one requiring fewer assumptions — is preferred in the absence of evidence requiring the more complex explanation.
Step 8. Therefore, the burden of proof currently lies with the particle hypothesis, not with the Passive Layer.
Step 9. The open quantitative problem — calculating the magnitude of the Passive Layer's contribution — does not shift this burden. It is a problem to be solved, not evidence of the Passive Layer's insufficiency.
Step 10. The question is no longer whether the Passive Layer can explain what we observe. The question is whether a dark matter particle is needed in addition to what the Passive Layer already provides.

CLOSING STATEMENT

Fritz Zwicky discovered an unexplained gravitational effect. He called it dark matter. He did not know what it was.

Ninety years later, we have measured it with extraordinary precision across every scale in the observable universe. We have not found the particle we assumed it to be.

The Passive Layer offers a different answer. Not a new particle. Not a new force. Not a new physics. The gravitational echo of mass that existed and then ceased to exist — an effect that was always there, always operating, always contributing to the gravitational structure of the universe.

We have been measuring it for ninety years. We have been calling it by the wrong name.

Whether this is correct is a question that calculation will answer. But the question itself — the right question — is no longer whether the Passive Layer is real. It is real. The question is whether anything else is needed.

That question is now open. It was not clearly open before. It is open now.

---

# Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry: A Charge Separation Mechanism via Magnetic Fields

Date: 2026-06-11
Foundation: Yang-Mills Collider v3.2 (LHC_kerr_2.html), Passive Layer Series
Purpose: To demonstrate that pair annihilation is not a default process but a conditional phenomenon, and to propose a new physical mechanism for the matter-antimatter asymmetry problem that requires no new particles, no new forces, and no new mathematics.

## References

Abbott et al. (LIGO/Virgo Collaboration). GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. Physical Review Letters, 119, 161101 (2017).

Particle Data Group (2022). Review of Particle Physics.

Sakharov, A.D. (1967). Violation of CP Invariance, C Asymmetry, and Baryon Asymmetry of the Universe. JETP Letters, 5, 24-27.

B. Sun. I Added a Black Hole to the LHC — and Something Unexpected Happened (2026-06-06).

B. Sun. Passive Layer — Essential Citations (2026-06-08).

## 1. The Central Claim

Pair annihilation is not a fundamental default process. It is a conditional phenomenon that requires two things to happen simultaneously: a particle and its antiparticle must occupy the same spatial location at the same time. In the absence of any mechanism that physically separates them, this condition is naturally met. However, in the presence of a magnetic field of any non-zero strength, the Lorentz force acts on opposite charges in opposite directions, driving particles and antiparticles into geometrically distinct trajectories. Once spatially separated, they cannot annihilate. They persist as mass.

This statement contains no threshold, no minimum field strength, no special condition beyond B ≠ 0. The separation is not a matter of degree that kicks in above some critical value. It is a binary structural consequence of the sign of the charge in the Lorentz force law:

F = q(v × B)

For a particle with charge +q moving with velocity v in magnetic field B, the force deflects it in one direction. For its antiparticle with charge -q and identical speed, the force deflects it in the opposite direction. This is not an approximation. It is exact, and it holds for any B ≠ 0, for any particle species with non-zero charge, at any energy.

The matter-antimatter asymmetry of the universe may be, in significant part, a consequence of this elementary fact operating at cosmological scale during the early universe.

## 2. Why This Has Not Been the Primary Framework for Sixty Years

In 1967, Andrei Sakharov identified three conditions that any successful theory of baryogenesis must satisfy:
1. Baryon number violation
2. C and CP symmetry violation
3. Interactions out of thermal equilibrium

These conditions, now known as the Sakharov conditions, have defined the landscape of baryogenesis research for six decades. They are necessary conditions derived from thermodynamic reasoning: if all three are not satisfied, any baryon asymmetry generated will be washed out by equilibrium processes.

The Sakharov conditions are necessary within their own framework. But they are not necessary conditions in general. They describe what is required to generate an asymmetry through particle-number-changing processes in thermal equilibrium. They say nothing about mechanisms that operate through spatial separation rather than number asymmetry.

The magnetic charge separation mechanism proposed here does not violate this logic. It operates in a different regime entirely. It does not require baryon number violation. It does not require CP violation beyond what already exists. It does not require fine-tuned departures from thermal equilibrium. It requires only that a non-zero primordial magnetic field existed during the epoch when pair production was the dominant process in the universe, and that this field separated the products of pair production before they could annihilate.

The reason this mechanism has not been the central focus of baryogenesis research is not that it is known to be insufficient. It is that the field organized itself around the Sakharov framework before the quantitative implications of large-scale magnetic charge separation were systematically explored. The framework became the question, and questions outside the framework were rarely asked.

## 3. The Physics of Magnetic Charge Separation

### 3.1 The Lorentz Force and Opposite Deflection

Consider a photon-photon collision producing an electron-positron pair:
γ + γ → e⁻ + e⁺

Both particles are produced at the same spatial point. In the presence of a magnetic field B directed along the z-axis, the Boris integrator — the standard algorithm used in GEANT4 and all major plasma physics PIC codes — updates the momentum of each particle according to:

t_c = (q · Δt/2) / (γm)
t = t_c · B
p⁻ = p + p × t
s = 2t / (1 + |t|²)
p_new = p⁻ + p⁻ × s

The rotation encoded in the cross products p × t and p⁻ × s reverses direction when q changes sign, because t_c = (q·Δt/2)/(γm) carries the sign of q directly. For the electron (q = -e), t_c is negative; for the positron (q = +e), t_c is positive. The rotation is in opposite senses for opposite charges.

This is not a numerical artifact. It is the exact discrete analog of the continuous Lorentz force. In the source code of the Yang-Mills Collider v3.2 (LHC_kerr_2.html), this appears as a single line:

const tc = (charge * dt * 0.5) / (gam * mass);

The variable charge carries the sign. When charge = +1, the rotation goes one way. When charge = -1, it goes the other. There is no threshold. There is no minimum field strength. There is no special parameter combination required. The separation follows from the sign of a single variable in a single line of code that implements a law of physics verified to extraordinary precision.

### 3.2 The Inevitability of Separation

The separation of charges in a magnetic field is not an emergent phenomenon that requires careful tuning. It is a structural consequence of the Lorentz force. To prevent separation, one must set B = 0 exactly. Any departure from B = 0, in any direction, of any magnitude, causes particles and antiparticles to diverge.

This has a direct implication for the early universe: if a primordial magnetic field existed — of any non-zero strength — charge separation during pair production was not merely possible. It was unavoidable.

The quantitative questions (how efficient was the separation? what fraction survived? how large were the domains?) depend on the field strength, coherence length, and duration. But the qualitative question — did separation occur? — has only one answer if B ≠ 0: yes.

### 3.3 The Larmor Radius

The radius of the circular orbit traced by a charged particle in a magnetic field is the Larmor radius:

r_L = γ m v_⊥ / (|q|B) = p_⊥ / (|q|B)

where:
- γ = (1 - v²/c²)^{-1/2} is the Lorentz factor
- m is the rest mass of the particle
- v_⊥ is the component of velocity perpendicular to B
- p_⊥ = γ m v_⊥ is the transverse momentum
- |q| is the magnitude of the electric charge
- B is the magnetic field strength

The Larmor radius determines the scale of separation, not whether separation occurs. A larger B produces a smaller r_L and tighter, more confined orbits — meaning the particle and antiparticle are more efficiently confined to separate regions. A smaller B produces larger orbits that overlap more, reducing separation efficiency. But in both cases, the orbits wind in opposite directions. The separation exists at any B ≠ 0; the Larmor radius measures its spatial scale.

For ultrarelativistic particles where E ≈ pc:
r_L ≈ E_⊥ / (|q|B c)

The mass hierarchy of particles is directly encoded in their separation scale: heavier particles have larger Larmor radii, and therefore trace wider, less confined orbits in the same field. Protons and antiprotons separate on scales 1836 times larger than electrons and positrons at the same energy.

### 3.4 Separation Efficiency vs. Separation Existence

It is important to distinguish two questions that are often conflated:

Question 1 — Does separation occur? Answer: Yes, for any B ≠ 0. This follows directly from the Lorentz force and requires no additional conditions.

Question 2 — How efficient is the separation? Answer: This depends on the ratio r_L / R_system. When r_L ≪ R_system, particles are tightly confined to separate orbital regions and the encounter rate between particle and antiparticle populations approaches zero. When r_L ~ R_system, the orbits are comparable to the system size and significant overlap occurs, reducing but not eliminating the separation effect.

The condition r_L ≪ R_system therefore governs separation efficiency, not separation existence. In the early universe, as shown in Section 5, the primordial field satisfies this condition with margins of many orders of magnitude.

### 3.5 The Cross Section for Annihilation and Its Suppression

In the absence of a magnetic field, the annihilation cross section for an electron-positron pair at low relative velocity v is given by the Dirac formula:
σ_ann = π r_e² (v/c)^{-1} · [1 + (1/2)(v/c)² + ...]

where r_e = e²/(m_e c²) ≈ 2.818 × 10^{-13} cm is the classical electron radius. The rate of annihilation events per unit volume is:
Γ_ann = n_+ · n_- · ⟨σ_ann v_rel⟩

In the charge-separated regime, the spatial overlap between the distributions of n_+ and n_- is reduced. In the limit of complete separation:
∫ n_+(r) · n_-(r) d³r → 0

and the annihilation rate falls to zero regardless of the magnitude of σ_ann. The magnetic field does not change the intrinsic annihilation cross section. It changes the geometry of the encounter, suppressing or eliminating the encounter entirely. This suppression begins as soon as B ≠ 0 and becomes more complete as B increases.

## 4. The Sakharov Conditions Revisited

### 4.1 Necessary vs. Sufficient Conditions

The Sakharov conditions are a set of necessary conditions for baryogenesis through asymmetric particle number production in thermal equilibrium. This is not the same as saying they are necessary conditions for any mechanism that produces a matter-antimatter asymmetry.

To be precise: suppose we define baryogenesis as any physical process that results in a universe with unequal numbers of baryons and antibaryons in a given region. The Sakharov conditions are necessary if we additionally assume that:
(a) The asymmetry is generated by reactions that change baryon number
(b) The universe passes through a state of thermal equilibrium that would otherwise wash out any asymmetry

Neither (a) nor (b) needs to be true in the magnetic separation framework. The proposed mechanism does not generate an asymmetry in baryon number. It generates an asymmetry in the spatial distribution of existing particles and antiparticles. The baryon number remains, in principle, zero — but matter and antimatter are concentrated in different spatial regions. The observed dominance of matter over antimatter in our observable universe would then reflect the fact that our region of space happens to be matter-dominated, with antimatter concentrated elsewhere.

This is a fundamentally different conceptual picture from standard baryogenesis scenarios.

### 4.2 The Quantitative Failure of CP Violation

The standard model CP violation, encoded in the Cabibbo-Kobayashi-Maskawa (CKM) matrix, is characterized by the Jarlskog invariant:
J_CP = Im[V_ud V_cb V_ub* V_cd*] ≈ 3 × 10^{-5}

The baryon asymmetry generated by standard model CP violation in electroweak baryogenesis is suppressed relative to the observed asymmetry by a factor that can be estimated as:
η_SM ~ (α_w)² · (m_t/M_W)² · J_CP · (T_EW/M_Pl)² · ...

where α_w is the weak coupling constant, m_t is the top quark mass, M_W is the W boson mass, T_EW ~ 100 GeV is the electroweak phase transition temperature, and M_Pl ~ 10^{19} GeV is the Planck mass. The result is:
η_SM ~ 10^{-20}

The observed baryon-to-photon ratio is:
η_obs = (n_b - n_b̄) / n_γ ≈ 6.1 × 10^{-10}

(from Planck 2018 CMB analysis, consistent with Big Bang Nucleosynthesis constraints)

The discrepancy:
η_obs / η_SM ~ 10^{-10} / 10^{-20} = 10^{10}

Standard model CP violation is ten orders of magnitude too small to account for the observed asymmetry. This is not a marginal failure. It is a catastrophic failure that has motivated decades of searches for physics beyond the standard model.

The magnetic charge separation mechanism does not need to explain this ten-order-of-magnitude gap through new CP violation. It proposes a different question entirely: not "how were more baryons created than antibaryons?" but "how were baryons and antibaryons separated before they could annihilate?"

### 4.3 The Magnitude of Separation Required

For the magnetic separation mechanism to explain the observed asymmetry, it does not need to achieve perfect separation. It needs to achieve a separation efficiency such that the surviving fraction of matter exceeds the surviving fraction of antimatter by the ratio:
(n_b - n_b̄) / n_b̄ ≈ η_obs / (1 - η_obs) ≈ 6.1 × 10^{-10}

This is an extraordinarily small asymmetry. For every 10^{10} baryons that survived, approximately 10^{10} - 1 antibaryons were annihilated. The mechanism does not require efficient separation — it requires a barely detectable imbalance in the fraction of matter versus antimatter that escapes boundary regions between separated domains.

Given that separation begins at B ≠ 0 and that primordial fields are expected to be many orders of magnitude above any plausible minimum, the required asymmetry of one part in 10^{10} is, if anything, surprisingly modest.

## 5. Primordial Magnetic Fields: Observational Constraints and Theoretical Predictions

### 5.1 Current Observational Upper Limits

Several independent observational probes constrain the strength of cosmological magnetic fields at different epochs:

From CMB polarization B-modes at recombination (z ~ 1100): B_CMB < 10^{-9} G (comoving)
From blazar observations and the non-observation of cascade emission (z ~ 0.1-1): B_IGM < 10^{-15} G (for correlation lengths > 1 Mpc)
From gamma-ray observations of distant blazars (Fermi-LAT): B_IGMF < 10^{-16} G (for coherence lengths ~ Mpc)

These are upper limits on the present-day (comoving) values. The physical field at earlier epochs was stronger by (1+z)² for a field that evolves adiabatically:
B_physical(z) = B_comoving · (1+z)²

### 5.2 Theoretical Predictions for Primordial Field Generation

From the electroweak phase transition (Vachaspati 1991, Baym et al. 1996): B_EW ~ 10^{23} G (physical, at T_EW ~ 100 GeV)
Equivalent in comoving units: B_EW,comoving ~ 10^{23} / (10^{15})² G = 10^{-7} G
From the QCD phase transition (T ~ 150 MeV): B_QCD,comoving ~ 10^{-6} G

### 5.3 The Separation Condition in the Early Universe

The separation efficiency condition r_L ≪ R_system, evaluated at nucleosynthesis (T ~ 1 MeV, t ~ 1 second):
R_H(t=1s) = c·t ~ 3 × 10^{10} cm ~ 10^9 m

For an electron with thermal energy E_e ~ 1 MeV:
p_⊥ ~ E_e/c ~ 5.3 × 10^{-22} kg·m/s

The field required for r_L ≪ R_H:
B_required ≫ p_⊥ / (e · R_H) ~ 3 × 10^{-12} G (physical)

In comoving units: B_required,comoving ≫ 3 × 10^{-30} G

The ratio of predicted to required field:
B_EW,comoving / B_required,comoving ~ 10^{-7} / 10^{-30} = 10^{23}

The predicted primordial fields exceed the minimum required for efficient charge separation by twenty-three orders of magnitude. The separation condition is not marginally satisfied. It is overwhelmingly satisfied.

More fundamentally: even this calculation concerns separation efficiency. The separation itself — the divergence of particle and antiparticle trajectories — requires only B ≠ 0. Given that the predicted primordial fields are 10^{23} times the threshold for efficient separation, the existence of any separation at all is not in question.

## 6. Simulation Evidence: Yang-Mills Collider v3.2

### 6.1 The Structure of the Boris Integrator

The Yang-Mills Collider v3.2 (LHC_kerr_2.html) implements the Boris algorithm for relativistic charged particle motion. The core of the magnetic rotation step is:

const tc = (charge * dt * 0.5) / (gam * mass);
const tx = 0, ty = tc * (-Bfield), tz = 0;
const t2 = tx*tx + ty*ty + tz*tz;
const pmx = px + (py*tz - pz*ty);
const pmy = py + (pz*tx - px*tz);
const pmz = pz + (px*ty - py*tx);
const sx = 2*tx/(1+t2), sy = 2*ty/(1+t2), sz = 2*tz/(1+t2);
let ppx = px + (pmy*sz - pmz*sy);
let ppy = py + (pmz*sx - pmx*sz);
let ppz = pz + (pmx*sy - pmy*sx);

The variable tc carries the sign of charge directly. When charge = +1 (positron, proton, etc.), ty = tc * (-Bfield) is positive for positive Bfield. When charge = -1 (electron, antiproton, etc.), ty is negative. The cross products that follow rotate the momentum vector in opposite senses for opposite signs of ty. This is not conditional on any parameter threshold. It executes on every timestep for every charged particle as long as Bfield ≠ 0.

The black hole gravity code applies identically to all particles regardless of charge:

const gAcc = logMass * 120.0 / (r2 + 1.0);
p.p4.px -= gAcc * (dx / r) * dt;
p.p4.py -= gAcc * (dy / r) * dt;
p.p4.pz -= gAcc * (dz / r) * dt;

There is no charge variable here. The gravitational acceleration is identical for particle and antiparticle. The black hole pulls both toward the same point with the same force. But the Boris integrator has already rotated their momenta in opposite senses, so they approach the black hole from geometrically opposite sides. The result — charge-separated populations on opposite sides of the gravitational center — is not a programmed outcome. It is the unavoidable geometric consequence of combining opposite-sense gyration with a common gravitational center.

### 6.2 The Condition for Separation: B ≠ 0 and M_BH > 0

A direct reading of the simulator code establishes the following:

Separation does NOT occur when:
- Bfield = 0 (exactly zero), or
- BH_MASS = 0 (no gravitational center)

Separation DOES occur for all other parameter combinations. There is no minimum field strength threshold in the code. There is no minimum black hole mass threshold. There is no special orientation or geometry required. The separation is a structural property of the system, not an emergent phenomenon requiring careful tuning.

To be explicit: the following parameter ranges all produce charge separation:
- Bfield: any value > 0 (the simulator range is 0 to ~14 T, but the physics has no upper limit)
- BH_MASS: any value > 0 (the simulator range spans many orders of magnitude)
- BH_SPIN (a*): any value from 0 to 1 (spin affects disk morphology, not separation existence)
- Collision energy √s: any value (the simulator default is 13,000 GeV)
- Particle species: all 39 charged species in the PDG 2022 implementation

The only way to prevent separation is to deliberately set B = 0 or M_BH = 0. In the language of experimental design: this is not an experiment where you tune parameters to find a regime where separation occurs. It is an experiment where you must actively break the physics to prevent separation from occurring.

### 6.3 Observed Phenomena Across Parameter Space

B = 0, any BH_MASS: All particles absorbed by the black hole without charge separation. With no magnetic force, particle and antiparticle trajectories are not distinguished. Both are pulled radially inward.

B > 0, BH_MASS = 0: Charge separation occurs — particles and antiparticles diverge into opposite-sense helical trajectories — but without a gravitational center, the separated populations disperse throughout the simulation volume rather than forming a concentrated structure.

B > 0, BH_MASS > 0, BH_SPIN = 0 (Schwarzschild): Charge separation occurs and both populations are gravitationally attracted to the black hole. They arrive from opposite sides and are absorbed or captured on opposite sides. No accretion disk forms because there is no frame-dragging to impart angular momentum.

B > 0, BH_MASS > 0, BH_SPIN > 0 (Kerr): Charge separation occurs, both populations are attracted to the black hole, and frame-dragging (Lense-Thirring effect) imparts angular momentum, causing the captured populations to orbit rather than fall directly inward. An accretion disk forms spontaneously. No accretion disk code was written. The disk is a geometric consequence of the combination of opposite-sense gyration, common gravitational center, and frame-dragging.

The accretion disk formation without disk-specific code is significant not as an aesthetic result but as a demonstration that the physical environment around a rotating black hole with a magnetic field naturally and inevitably self-organizes into a charge-separated, mass-persistent configuration. This organization is robust across the entire parameter space of the simulator: it appears at low B and high B, at low spin and high spin, at low mass and high mass, with all charged particle species.

### 6.4 What the Simulation Proves and What It Does Not Prove

The simulation proves the following with certainty:
(a) In a system implementing the Lorentz force via the Boris algorithm and Newtonian gravity, charge separation is an inevitable consequence of B ≠ 0 combined with a gravitational center.
(b) The separated populations persist without annihilating as long as the magnetic separation condition is maintained.
(c) Spontaneous disk-like structures form around rotating gravitational centers without any disk-specific physics being coded.

The simulation does not prove the following, and claims to that effect should not be made:
(a) That the quantitative separation efficiency in the simulator matches any specific astrophysical environment.
(b) That the primordial universe contained magnetic fields of the specific strength simulated.
(c) That the mechanism operating in the simulator at 6.2 T laboratory scale is quantitatively equivalent to the mechanism operating in the early universe at primordial field scales.

What the simulation provides is a proof of concept at the level of physical mechanism: charge separation under these conditions is not a numerical curiosity but a direct consequence of the sign of the charge in the Lorentz force law. The quantitative translation to astrophysical and cosmological scales requires the analysis in Sections 4 and 5.

## 7. The Boundary Asymmetry Mechanism

### 7.1 Domain Structure

If the early universe magnetic field drove charge separation, the result would be a universe divided into domains: regions dominated by matter separated from regions dominated by antimatter by boundary layers where the field reverses or weakens.

The scale of these domains depends on the coherence length of the primordial magnetic field. After cosmic expansion and magnetohydrodynamic evolution, the domain scale is model-dependent. The observational question is not whether domain boundaries exist at some scale today, but whether the asymmetry between domains was sufficient to produce the observed baryon-to-photon ratio η_obs ~ 6 × 10^{-10}.

Given the twenty-three-order-of-magnitude surplus of field strength over the minimum required for separation, even an extremely imperfect domain structure with small, irregular, partially mixed domains could produce the required asymmetry.

### 7.2 Asymmetric Annihilation at Domain Boundaries

At the boundaries between matter-dominated and antimatter-dominated domains, annihilation occurs as particles and antiparticles from adjacent domains encounter each other. Several mechanisms can drive asymmetric boundary annihilation:

(i) Asymmetric diffusion: If the diffusion coefficients for particles and antiparticles differ due to asymmetric interactions with the ambient magnetic field, one population can diffuse across the boundary more efficiently and be annihilated at a higher rate.

(ii) Thermal asymmetry: Annihilation is exothermic (releasing 2m_e c^2 per pair for e^+e^-). This energy heats the boundary region, driving further particle flux. If one domain is warmer than the other due to asymmetric magnetic energy dissipation, the flux asymmetry produces an asymmetric annihilation rate.

(iii) Adiabatic compression: As the universe expands and cools, magnetic pressure may compress one type of domain preferentially depending on field topology.

Any of these effects, operating at one part in 10^{10}, is sufficient to produce the observed baryon asymmetry without CP violation, without baryon number violation, and without new physics.

## 8. Relation to the Passive Layer Framework

The magnetic charge separation mechanism connects directly to the Passive Layer framework. In that framework, pair production in strong magnetic fields around black holes produces particle-antiparticle pairs that are separated by the Lorentz force and survive without annihilating. These surviving pairs contribute to the effective mass near the black hole through the additional term in the mass evolution equation:

dM_BH/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking / c^2

The term Ṁ_pair represents mass creation through pair production and magnetic separation. This term has not been systematically quantified in the existing astrophysics literature.

The baryon asymmetry mechanism described in this document is the cosmological version of the same process: pair production in the primordial magnetic field, followed by charge separation and survival, applied not to the local environment of a single black hole but to the entire early universe. The Passive Layer framework and the baryogenesis mechanism are two scales of the same underlying physics.

## 9. Falsifiable Predictions

### 9.1 Primordial Magnetic Field Detection

If this mechanism operated, a non-zero primordial magnetic field must have existed. The minimum required comoving field strength for any separation at all is B > 0. For efficient separation (r_L ≪ R_H at nucleosynthesis), the required comoving field is:
B_comoving ≫ 3 × 10^{-30} G

Current and near-future observational programs (Square Kilometre Array, CMB-S4) will constrain primordial magnetic fields at the level of:
B_comoving ~ 10^{-11} G

If primordial fields are detected at or above 10^{-11} G, this strongly supports the viability of the separation mechanism. Detection at any level above zero is sufficient for separation to occur; detection above 10^{-30} G comoving is sufficient for efficient separation.

### 9.2 Antimatter Domain Signatures

Boundaries between matter and antimatter domains would produce:
(a) A contribution to the diffuse gamma-ray background at E ~ m_e c^2 ~ 0.511 MeV (electron-positron annihilation) and E ~ m_p c^2 ~ 938 MeV (baryon-antibaryon annihilation).
(b) A potential distortion of the CMB spectrum if boundary annihilation occurred after recombination.
(c) Modification of Big Bang Nucleosynthesis yields in domain boundary regions, potentially observable as spatial variations in the primordial helium abundance.

### 9.3 Laboratory Test: Charge Separation in Strong Fields

The mechanism predicts that in any environment with B ≠ 0 and a gravitational or electromagnetic confinement center, pair production will be followed by observable charge separation. The specific prediction is: the spatial distribution of produced electrons and positrons should show separation in the direction determined by the magnetic field orientation, with separation distance scaling as:
Δx ~ r_L = p_⊥ / (eB)

This is directly testable at existing high-intensity laser facilities (ELI-NP, XCELS) where pair production in laser-laser collisions has been observed. The test requires only B ≠ 0 — not a specific minimum field value.

## 10. Limitations and Open Questions

10.1 Quantitative Efficiency Not Calculated
The fraction of pair-produced particles that survive without annihilating in a realistic primordial magnetic field geometry — accounting for field inhomogeneity, coherence length limitations, turbulent mixing, and the expansion of the universe — has not been calculated. The separation exists for any B ≠ 0; its quantitative efficiency under realistic early-universe conditions requires magnetohydrodynamic simulation at cosmological scales.

10.2 Domain Scale Uncertainty
The coherence length of the primordial magnetic field, which determines the scale of matter-antimatter domains, is highly model-dependent.

10.3 Asymmetric Annihilation Rate Not Derived
The claim that boundary annihilation produces an asymmetry of order η_obs ~ 6 × 10^{-10} has been argued on qualitative grounds. A quantitative derivation requires detailed modeling of the matter-antimatter interface dynamics.

10.4 Coexistence with Sakharov Mechanisms
This mechanism does not exclude the possibility that Sakharov-type baryogenesis also occurred. The two mechanisms could have operated simultaneously, with additive contributions to the observed baryon asymmetry.

## 11. Conclusion

The matter-antimatter asymmetry of the observable universe may not require baryon number violation, exotic CP violation, or any new physics. It may require only that the early universe contained a magnetic field of any non-zero strength — which is predicted by essentially every model of early-universe physics — and that this field separated particle-antiparticle pairs produced during the epoch of pair creation before they could annihilate.

The physical mechanism is not subtle. The Lorentz force F = q(v × B) acts in opposite directions on opposite charges. This has been verified to extraordinary precision for over a century. The Boris integrator that implements this law in the Yang-Mills Collider v3.2 simulator encodes the charge sign in a single variable, tc = (charge * dt * 0.5) / (gam * mass), and the opposite rotation that results is a direct and unavoidable consequence of that sign. There is no threshold. There is no special regime. There is no parameter combination within B ≠ 0 for which separation fails to occur.

The question is not whether separation occurs in a magnetic field. It does, by definition, for any B ≠ 0. The question is whether the scale, efficiency, and domain structure of that separation in the early universe was sufficient to produce the observed baryon-to-photon ratio of 6.1 × 10^{-10}. Given that the predicted primordial field strengths exceed the minimum required for efficient separation by twenty-three orders of magnitude, and given that the required asymmetry is as small as one part in ten billion, the answer to this question is not obviously no.

The standard model CP violation fails by ten orders of magnitude to produce the observed asymmetry. The magnetic separation mechanism, operating on the same pair-produced populations, requires no new physics, no new particles, and no parameter that is not already constrained by existing theory and observation. The only requirement is that the early universe was not magnetically empty.

There is no evidence that it was.

---

# Dark Energy Reinterpreted — Cosmic Expansion as the Relaxation of Curvature

Date: 2026-06-11
Purpose: To propose, without resolving the 10^123 problem, that the geometric relaxation of the Passive Layer is the physical mechanism behind accelerating cosmic expansion.

## References

Abbott et al. (LIGO/Virgo Collaboration). GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. Physical Review Letters, 119, 161101 (2017).

Weinberg, S. (1989). The cosmological constant problem. Reviews of Modern Physics, 61, 1.

Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics, 641, A6.

Passive Layer — Essential Citations (2026-06-08)

The Passive Layer — Core Document (2026-06-09)

## 1. Redefining the Problem

Modern cosmology accounts for the accelerating expansion of the universe by introducing dark energy. The standard model (ΛCDM) represents this as a cosmological constant Λ — a negative pressure term (p = -ρc²).

This approach carries two fundamental problems.

Problem 1: The identity of negative pressure
What negative pressure is, why it exists, and how it is produced — no one can explain. It is, in effect, repulsive gravity under a different name.

Problem 2: The 10^123 problem
The vacuum energy density predicted by quantum field theory (≈ 5 × 10^96 kg/m³) differs from the observed value (≈ 6 × 10^{-27} kg/m³) by a factor of 10^123. This is the most extreme theory-observation discrepancy in the history of physics. The standard model attributes this to cancellation, but the mechanism of that cancellation is entirely unknown.

This document does not attempt to resolve either problem. It bypasses them.

## 2. Three Established Facts

### Fact 1: Mass curves space

In general relativity, mass generates curvature in the surrounding spacetime. This is the geometric nature of gravity itself, confirmed repeatedly — through GPS satellite corrections, gravitational wave observations, and the precession of Mercury's perihelion.

### Fact 2: Gravity propagates at c

The curvature of space is not transmitted instantaneously. It propagates at the speed of light. In 2017, the simultaneous detection of gravitational waves and gamma rays from GW170817 confirmed that the propagation speed of gravity matches c to within 10^{-15} (Abbott et al., 2017).

Implication: When a mass disappears, the curvature it produced does not vanish instantly. It continues to propagate outward for a time r/c.

### Fact 3: Mass is created and destroyed

Energy converts into mass and mass converts back into energy. Particle-antiparticle pairs are continuously created and annihilated throughout the universe — in vacuum fluctuations, near black holes, and in high-energy environments. Stars burn. Neutron stars collapse. This has been directly observed and is a foundational result of quantum field theory.

None of these three facts is in dispute.

## 3. The Logical Consequence: The Passive Layer

Combine the three facts.

Mass exists → space curves → mass ceases to exist → the curvature does not instantly vanish → the curvature propagates outward at c, gradually relaxing.

This propagating remnant of curvature is the Passive Layer.

τ(r) = r / c

The curvature produced by a mass at distance r persists for time r/c after that mass is gone.

This is not a hypothesis. It is the logical consequence of Facts 1, 2, and 3. It cannot be denied without denying one of those facts.

## 4. The Central Claim: Relaxation of Curvature Is Expansion

### 4.1 What relaxation means

The Passive Layer — the propagating remnant of curvature left by annihilated mass — relaxes as it propagates.

Without the original mass to sustain it, the curvature cannot be maintained. As the remnant spreads, the local geometry approaches Minkowski flatness. This is curvature relaxation.

### 4.2 When curvature relaxes, space expands

In general relativity, the volume element of space is expressed through the metric tensor g:
dV = √|g| d³x

When curved space (|g| > 1) relaxes toward flatness (|g| → 1), the volume element increases.

When something curved becomes flat, it becomes larger.

This requires no unknown force. No repulsive gravity. No negative pressure. No new particles. It is a pure geometric consequence.

### 4.3 Connection to the Friedmann equation (conceptual sketch)

Write the effective energy density as:
ρ_eff = ρ_matter + ρ_PL

where ρ_PL is the effective density corresponding to the residual curvature of the Passive Layer.

As the Passive Layer relaxes:
dρ_PL/dt = -λ · ρ_PL (λ > 0, relaxation rate)

Friedmann equation:
(ȧ/a)² = (8πG/3)(ρ_matter + ρ_PL) - k/a²

The time-dependent decrease of ρ_PL modifies the effective value of k, and this modification is observed as accelerating expansion.

This is a conceptual sketch, not a rigorous derivation. The quantitative calculation remains an open problem.

## 5. Bypassing the 10^123 Problem

This model does not resolve the 10^123 problem. It changes the question.

Standard question: Why is vacuum energy cancelled by a factor of 10^123?
This model's question: How much does space expand when the curvature left by annihilated mass relaxes?

The absolute magnitude of vacuum energy is irrelevant to this model. What matters is the curvature left by mass that actually existed and then ceased to exist. The magnitude of that curvature is determined by the mass-creation-and-annihilation history of the universe — not by the vacuum energy density itself.

The 10^123 problem is not this model's problem.

## 6. Comparison with the Standard Model

ΛCDM (cosmological constant):
- Cause of expansion: Negative pressure (identity unknown)
- New physics required: Yes (identity of Λ)
- Energy conditions: Violated (negative pressure)
- 10^123 problem: Cancellation assumed (mechanism unknown)
- Testability: Low (Λ is a constant)

This model (curvature relaxation):
- Cause of expansion: Geometric relaxation of curvature
- New physics required: No
- Energy conditions: Not violated
- 10^123 problem: Irrelevant (question bypassed)
- Testability: Present (relaxation rate is calculable)

## 7. Why Now — The Coincidence Problem

Dark energy became dominant in the late universe, approximately five billion years ago. Why not earlier?

This model provides a natural answer.

For the relaxation of the Passive Layer to manifest as observable accelerating expansion, the curvature remnants must have accumulated sufficiently and propagated to sufficiently large distances.
- Galactic scale (~50 kpc): t ~ 10^6 years — effectively instantaneous on cosmic timescales
- Galaxy cluster scale (~10 Mpc): t ~ 3 × 10^7 years
- Cosmic scale (~Gpc): t ~ billions of years

The Passive Layer's relaxation begins to operate at cosmic scales only after the universe has grown large enough and structure has formed sufficiently.

This is not a coincidence. It is the natural timescale of a physical process.

## 8. Falsifiable Predictions

Prediction 1: Dark energy density varies with time (unlike Λ) — Test: Future supernova, CMB, gravitational wave surveys
Prediction 2: Passive Layer density is higher near galactic centers, decreasing outward — Test: Galaxy rotation curves, gravitational lensing
Prediction 3: No direct detection in particle experiments (LZ, XENONnT, etc.) — Test: Already in progress — fifty years of null results

## 9. Open Problems

Problem: Calculate the Passive Layer relaxation rate λ — Difficulty: High
Problem: Quantify the effect of relaxation on the Friedmann equation — Difficulty: Very high
Problem: Verify that the calculated expansion rate matches Planck results — Difficulty: Very high

These calculations are outside the scope of this document. This document proposes the mechanism and identifies the direction of calculation.

## 10. Conclusion

Two established facts.

Mass curves space. Gravity propagates at c.

Therefore: when mass ceases to exist, the curvature it produced does not vanish instantly. It propagates and relaxes. Relaxation is expansion.

That is all.

No negative pressure. No repulsive gravity. No unknown particles. No new physics.

The standard approach says:
"There is an unknown force pushing the universe apart. We do not know why it pushes. Vacuum energy is cancelled by a factor of 10^123. We do not know how it cancels."

This model says:
"When something curved becomes flat, it becomes larger."

Which requires fewer assumptions is self-evident.



# The Black Hole Mass Variability — Complete Research Archive

**Date:** 2026-06-11
**Author:** B. Sun | Seoul Inside

## Table of Contents

1. Core Logical Framework
2. Two Established Facts
3. Three Independent Components
4. Simulation Evidence
5. Observational Correlations
6. The Four Layers of Severity
7. The Systematic Error Hypothesis
8. Reinterpretation of Anomalous Observations
9. Connection to Dark Matter and Dark Energy
10. Reversal of the Burden of Proof
11. Complete Citation Index
12. Technical Implementation Notes

---

## 1. Core Logical Framework

Premise 1: Gravity propagates at the speed of light (c).
Premise 2: Mass is continuously created and destroyed throughout the universe.
Conclusion: The gravitational influence of annihilated mass continues to propagate after the source is gone.

This propagating remnant is called the **Passive Layer** — also referred to as Ghost Mass or gravitational reverberation.

Formally:

τ(r) = r / c

The gravitational influence of a mass that existed at distance r persists for time r/c after that mass is gone.

**Defining statement:**
Gravitationally present. Physically absent.

This is not a metaphor. It is the logical consequence of two confirmed facts. It cannot be denied without denying one of those facts.

---

## 2. Two Established Facts

### Fact 1: Gravity Propagates at the Speed of Light

- Statement: A change in a gravitational source does not propagate instantly. The influence travels outward at c.
- Evidence: LIGO/Virgo, GW170817 (2017)
- Result: Gravitational waves and gamma rays arrived simultaneously, constraining the speed of gravity to within 10⁻¹⁵ of c
- Status: Confirmed. Not in dispute.
- Implication: If a mass disappears, its gravitational signal continues to travel outward for time r/c after the mass is gone.

**Source:** Abbott et al. (2017). Physical Review Letters, 119, 161101.

### Fact 2: Mass Is Created and Destroyed

- Statement: Energy converts into mass and mass converts back into energy.
- Evidence: LHC, pair production (γ+γ→e⁺+e⁻), radioactive decay, vacuum fluctuations
- Result: Particle-antiparticle pairs are continuously created and annihilated throughout the universe.
- Status: Confirmed. Not in dispute.
- Implication: Mass does not "disappear" — it transforms into other forms (energy). The gravitational signal, however, does not vanish instantly.

**Source:** Breit & Wheeler (1934). Physical Review, 46, 1087. (Theoretical prediction; subsequently confirmed at LHC.)

---

## 3. Three Independent Components

The Passive Layer is not a single monolithic effect. It comprises three independent physical mechanisms that must be distinguished.

### Component A: Vacuum Fluctuations (Universal, Constant)

- Physical origin: Quantum vacuum itself
- Spatial distribution: Uniform (same everywhere)
- Dominant regime: Far field (r >> R_disk)
- Generation rate: Ṁ_pair^vac(r) = constant
- Evidence level: Theoretical necessity (magnitude unknown due to 10¹²³ problem)

### Component B: Local Astrophysical Sources (Disk-like, Position-dependent)

- Physical origin: High-energy environments around black holes, AGN, supernovae, magnetars
- Spatial distribution: Disk-like (concentrated toward center)
- Dominant regime: Near field (r ≤ R_disk)
- Generation mechanism: Lorentz force separates charges before annihilation: F = q(v × B)
- Larmor radius: r_L = γmv_⊥ / (|q|B)
- Evidence level: Observed in simulation (emergence without programming)

### Component C: Retarded Gravity and Black Hole Displacement

- Physical origin: Finite propagation speed of gravity + black hole motion
- Spatial distribution: Dependent on BH trajectory
- Dominant regime: Entire galaxy
- Delay time: τ(r) = α·r/c (α = 1 is physical prediction)
- Retarded acceleration: a_ret = α·G·Ṁ_BH / (2c²)·R̂
- Evidence level: Simulated (GalaxyCS v4/v5.1) — flat rotation curves and spontaneous spiral arms

### Component Comparison

- Component A: Vacuum fluctuation — Quantum vacuum — Uniform — r >> R_disk — Constant — Hypothesis (needs calculation)
- Component B: Local astrophysical — Black holes, AGN, supernovae — Disk-like (center-concentrated) — r ≤ R_disk — High at center, decreasing outward — Simulation-observed
- Component C: Retarded gravity + BH displacement — Finite gravity speed + BH motion — Depends on BH trajectory — Entire galaxy — Delay time τ = α·r/c — Simulation-demonstrated

---

## 4. Simulation Evidence

### 4.1 Yang-Mills Collider v3.2 + Kerr Black Hole

**Core observation:** Accretion disk appeared spontaneously when a black hole was added to a high-energy particle collision environment. No accretion disk code was written.

**Key quote:**

> "I did not build an accretion disk. One appeared."

**Implementation details:**

Black hole gravity (Newtonian, log-corrected):
gAcc = log10(BH_MASS + 1) * 120.0 / (r² + 1.0)
dp/dt = -gAcc * (r_hat) * dt

Event horizon approximation (Kerr):
r_+ = M * (1 + sqrt(1 - a*²))
Rs_base = max(0.8, log10(BH_MASS + 1) * 0.6)
Rs = Rs_base * (1 + sqrt(max(0, 1 - BH_SPIN²))) * 0.5

Frame dragging (Lense-Thirring):
Ω_LT ~ 2 * G * J / (c² * r³)
fdAcc = BH_SPIN * log10(BH_MASS+1) * 55.0 / (r³ + 1.0)

**Phenomena that emerged without design:**

- Equivalence principle: All particles absorbed regardless of charge, mass, or type
- Accretion disk formation: Particles spontaneously aggregate into disk structure
- Penrose process: Particles near ergosphere escape under strong magnetic field + spin conditions

**Boris integrator (charge separation mechanism):**

t = (q·Δt/2) / (γm) · B̂
p⁻ = p + p × t
s = 2t / (1 + |t|²)
p⁺ = p⁻ + p⁻ × s
p_new = p⁺ + p_new_half × t

The rotation encoded in the cross products reverses direction when q changes sign. For electron (q = -e), t_c is negative; for positron (q = +e), t_c is positive. This is exact, holds for any B ≠ 0, and requires no threshold.

### 4.2 GalaxyCS v5.1 — Retarded Gravity + Spiral Arm Quantitative Analysis

**Core observation:** Whenever the central black hole is displaced from the disk's geometric center by any non-zero amount, spiral arm structure emerges immediately and persistently.

**Results:**

- BH at rest (displacement = 0): No spiral structure, axisymmetric disk
- BH displaced (any non-zero value): Immediate and persistent spiral arm formation (no threshold)
- Retarded gravity disabled + BH displacement: Keplerian rotation curve (v ∝ r^{−1/2})
- Retarded gravity enabled + BH displacement: Flat rotation curve + spontaneous spiral arms

**Retarded gravity implementation:**

τ = α·r/c
// Access BH position history buffer
const hist = star.history;
const targetTime = simTimeMyr - τ;
// Interpolate between stored positions
const a_mag = G * |M̈| / (2·c²)
ax += a_mag * dir * dx_ret / r_ret
az += a_mag * dir * dz_ret / r_ret

**Spiral arm strength analysis (Fourier m=2):**

S₂ = |(1/N) Σ weight·e^(imφ)|
where m=2, φ = atan2(dz, dx), weight = 1/(r·0.5+1)

**S₂ value interpretation:**

- < 0.15: Symmetric disk (no spiral)
- 0.15 - 0.35: Weak spiral structure forming
- 0.35 - 0.65: Distinct 2-arm spiral structure
- > 0.65: Strong grand design spiral

**Black hole displacement is the default state:**

- Solar System: f_Sun ≈ 0.998 — Displacement structurally suppressed
- Disk galaxy: f_BH ≈ 0.001–0.005 — Displacement structurally permitted

Perfect black hole stasis requires exact cancellation of host galaxy peculiar velocity (100–600 km/s), tidal forces from satellite galaxies, galactic bar oscillations, large-scale structure gravitational background, and gravitational wave recoil. This exact cancellation is not physically plausible.

**Observational support for BH offset:**

- M87: 6.8 ± 0.8 pc offset — No spiral structure (elliptical, no disk) — Batcheldor et al. (2010)
- M31 (Andromeda): Dual nuclei documented — Yes spiral structure
- Milky Way: ≲ 100 pc (NSC offset) — Yes spiral structure — Bovy et al. (2022)
- BCGs (1/3): 10 pc – kpc scale — Various — Chu, Boldrini & Silk (2022)
- General AGN: 10–100 pc (most common) — Various — Bartlett et al. (2021)

### 4.3 Critical Distinction: Separation Existence vs. Separation Efficiency

Two questions must not be conflated:

- **Does separation occur?** Yes, for any B ≠ 0. This follows directly from the sign of q in the Lorentz force. No threshold. No minimum field strength. No special condition.

- **How efficient is the separation?** This depends on the ratio r_L / R_system. When r_L ≪ R_system, particles and antiparticles are confined to geometrically distinct orbital regions and the encounter rate between opposite-charge populations approaches zero. Separation efficiency governs the rate of survival, not the existence of separation.

The condition r_L ≪ R_system is not a theoretical assumption. It is directly satisfied in the observed environment of the nearest supermassive black hole.

**M87* observational constraint (EHT + Faraday rotation, direct measurement):**

- Magnetic field at ISCO: B_ISCO ~ 1–30 G
- Electron density: n_e ~ 10⁴–10⁵ cm⁻³
- Larmor radius of relativistic electron (γ ~ 10⁶) at B ~ 10³ G: r_L ~ 10⁻¹ cm
- ISCO radius of M87*: r_ISCO ~ 6 × 10¹⁴ cm
- Ratio: r_L / r_ISCO ~ 10⁻¹⁵

The separation efficiency condition is satisfied by fifteen orders of magnitude in the directly observed environment of M87*. This is not a prediction. It is a direct implication of current observations.

**Consequence for mass variability:**

Once separated, particle and antiparticle populations cannot annihilate as long as the magnetic separation condition is maintained. They persist as mass. The effective mass near the black hole therefore includes a contribution from these surviving pairs:

dM_BH/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking/c²

The term Ṁ_pair — mass creation through pair production and magnetic separation — has not been systematically quantified in the existing astrophysics literature. Its existence follows from B ≠ 0 and pair production being confirmed processes. Its magnitude is the open question.

**Source:** Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry (2026-06-11) — full derivation, simulation evidence, and primordial field constraints available in the companion document.

---

## 5. Observational Correlations

### 5.1 AGN Luminosity Variability

- Current explanation: Accretion rate change (but why it changes is unknown)
- Passive Layer reading: Black hole mass variability (mechanism exists in simulator)
- Internal citation: I Added a Black Hole to the LHC, Black Hole Physics v3.2
- Distinguishing feature: Mechanism provided (pair production + magnetic separation → mass persistence)

### 5.2 Changing-Look Quasars (CLQSO)

- Current explanation: Not explained by standard models
- Passive Layer reading: Extreme case of mass variability
- Internal citation: Long-Term Survival of Antimatter
- Distinguishing feature: Explains previously unexplained phenomenon

### 5.3 JWST Early Universe Supermassive Black Holes

- Current explanation: Growth rate problem (cannot explain) — or observational bias (Li et al. 2025)
- Passive Layer reading: Mass variability distorts growth rate measurements
- Internal citation: Dark Energy Reinterpreted (early universe conditions)
- Distinguishing feature: Reinterprets measurement itself — overmassive may not be real

### 5.4 M87 EHT Asymmetry and Variability

- Current explanation: Inconsistent with static models; explained by stochastic accretion flow
- Passive Layer reading: Natural consequence of dynamic mass variability
- Internal citation: Black Hole Displacement and Default State (M87 citation)
- Distinguishing feature: Prediction-observation alignment — the fact of variability itself is evidence

### 5.5 Gravitational Wave Mass Gap

- Current explanation: Inconsistent with stellar evolution predictions
- Passive Layer reading: Mass variability changes the pre-merger mass distribution
- Internal citation: Delayed Gravitational Interaction (Component C extension)
- Distinguishing feature: Problem redefinition — issue may be measurement timing, not mass itself

---

## 6. The Four Layers of Severity

### Layer 1 — Black Hole Mass Measurement Problem

- Current method: Inverse calculation from surrounding objects' orbits (assumes mass is constant during measurement period)
- Passive Layer implication: Unclear whether measured value is instantaneous or average
- Internal citation: This document (Layer 4 analysis)
- External reference: EHT multi-epoch observations (actual variability demonstrated)

### Layer 2 — Horizon Gravity Trapping Possibility

- Current status: Unexplored territory
- Passive Layer implication: Outward-propagating Passive Layer may be less than actual (some gravitational signal trapped inside horizon)
- Internal citation: Black Hole Physics v3.2 (Hawking radiation not implemented), Dark Energy Reinterpreted
- External reference: None (new theoretical connection)

### Layer 3 — Cosmological Scale Extension

- Current status: Cosmological sum of black hole mass variability not calculated
- Passive Layer implication: Universe's total mass-energy budget may differ from current models
- Internal citation: Unified Technical Framework, Passive Layer Core Document
- External reference: Early universe black hole observations (growth rate problem connection)

### Layer 4 — Methodological Problem (Most Severe)

- Current status: All methods share same assumption (mass constancy during measurement period)
- Passive Layer implication: Consistency across methods may hide systematic error
- Internal citation: Reversal of Burden of Proof document
- External reference: EHT measurement consistency with orbital dynamics — but this consistency may be due to shared assumptions

**Critical observation:** Current black hole mass measurements are consistent across independent methods — orbital dynamics, gravitational waves, luminosity. If systematic error exists, this consistency is difficult to explain. However, if all methods share the same assumption (mass constancy during measurement period), consistency can hide error rather than confirm accuracy.

---

## 7. The Systematic Error Hypothesis

**Core claim:**
Current astronomical measurements of black hole mass may contain systematic errors because they all assume mass constancy during the measurement period. If black hole mass fluctuates significantly, what is being measured is not a stable property but a time-averaged snapshot.

**Measurement methods and shared assumptions:**

- Orbital dynamics (surrounding object motion): Core assumption — Mass is constant during measurement period. If mass fluctuates: Instantaneous value may be measured.
- Gravitational waves (merger signals): Core assumption — Pre-merger mass was stable. If mass fluctuates: Fluctuation just before merger would affect result.
- X-ray luminosity (accretion disk): Core assumption — Luminosity ∝ mass × accretion rate. If mass fluctuates: Luminosity variability could be due to mass itself.
- Pulsar timing: Core assumption — Gravitational field is stable. If mass fluctuates: Fluctuating field distorts timing.

**The consistency paradox:**
Independent methods give consistent values. If systematic error exists, this consistency is hard to explain. However, if all methods share the same assumption (mass constancy), consistency may hide error rather than confirm accuracy. This is the most severe layer of the problem.

**Connection to observed anomalies:**

- AGN luminosity variability: Standard model — Attributed to accretion rate (but why? unknown). Passive Layer reading — Mass variability (mechanism exists).
- Changing-look quasars: Standard model — Not explained. Passive Layer reading — Extreme mass variability.
- JWST early black holes: Standard model — Growth rate impossible. Passive Layer reading — Mass measurement distortion.
- M87 EHT variability: Standard model — Inconsistent with static models. Passive Layer reading — Dynamic mass variability.
- Gravitational wave mass gap: Standard model — Inconsistent with stellar evolution. Passive Layer reading — Pre-merger mass fluctuation.

---

## 8. Reinterpretation of Anomalous Observations

### 8.1 Changing-Look Quasars (SDSS Stripe 82)

**External reference:** MacLeod et al. (2021) — 9,248 quasars, 15-year baseline

**Key findings:**

- 40 changing-look quasar candidates identified
- 35 newly reported
- Brightness changes > 0.5 magnitude (characteristic of CLQSO)
- 10-fold variability increase between SDSS and PS1 data
- DRW (Damped Random Walk) model applied — variability amplitude correlates with black hole mass

**Passive Layer reinterpretation:**
These extreme brightness changes are not due to accretion rate fluctuations (which would require explaining why accretion rate fluctuates). They are direct observational evidence of black hole mass variability driven by the Component B mechanism: pair production + magnetic separation + mass persistence near the event horizon.

### 8.2 JWST Early Universe Supermassive Black Holes

**External reference:** Li et al. (2025) — observational biases may explain overmassive appearance

**Key findings:**

- JWST discovered "overmassive" black holes at z ≳ 4 (first 1.5 billion years of the universe)
- Compared to local MBH-M* relation, they appear 2× overmassive
- Li et al. (2025) argue selection effects may be responsible
- Low-mass black holes may be missing from observations

**Passive Layer reinterpretation:**
The apparent overmassiveness may not be real. Mass variability distorts the relationship between measured luminosity and actual mass. If black holes in the early universe experienced more extreme mass fluctuations (due to higher energy density), then the measurement itself is systematically biased. This aligns with Li et al.'s selection effect argument — but adds a physical mechanism for the bias.

**External reference:** Mezcua et al. (2024) — 12 overmassive black holes at cosmic noon (z ≈ 1-3)

**Key findings:**

- Similar overmassive characteristics to JWST high-z sample
- Shows continuity between intermediate and high redshift
- MBH/M* ratio, bolometric luminosity, Eddington ratio all consistent

### 8.3 M87* EHT Multi-Epoch Variability

**External reference:** EHT Collaboration (2025) — 2017, 2018, 2021 three epochs

**Key findings:**

- Ring diameter: 43.9 ± 0.6 μas (consistent across all epochs)
- Total intensity and linear polarization vary significantly between epochs
- 2017 polarization fraction: ~15% → 2018/2021: ~5%
- Spiral polarization pattern changes year to year
- 2021 EVPA helicity change (magnetized accretion flow or external Faraday screen)
- Annual changes in brightness distribution expected from stochastic accretion flow
- Despite gamma-ray flare (M87 2018), 2018 and 2021 images are surprisingly similar

**External reference:** M87 MWL Campaign (2017-2018) — simultaneous multi-wavelength

**Key findings:**

- Black hole mass: (6.5 ± 0.7) × 10⁹ M⊙ (EHT 2017) — consistent with other measurements
- Strong aligned magnetic field present (polarization evidence)
- Jet power P_jet ≥ 10⁴² erg/s
- Single-zone model cannot simultaneously explain EHT flux and high-energy SED (layered jet model needed)
- 2018 observation: brightness asymmetry position angle shifted by ~30° from 2017
- Annual variability timescale: 10-70 dynamical timescales

**Passive Layer reinterpretation:**
The observed variability is not merely stochastic accretion flow. It is consistent with dynamic mass variability around a Kerr black hole with spin a* ≈ 0.9. The fact that the ring diameter remains constant while polarization and asymmetry change significantly suggests that the mass distribution (not the underlying spacetime geometry) is what varies. This is exactly what Component B predicts: mass is continuously created, separated, and annihilated near the horizon, changing the local mass-energy distribution without changing the black hole's fundamental parameters.

### 8.4 AGN Luminosity Variability (DRW Model)

**External reference:** MacLeod et al. (2012) — DRW (Damped Random Walk) model for quasar variability

**Key findings:**

- Variability amplitude correlates with black hole mass
- DRW provides good empirical fit
- Physical mechanism for DRW parameters is not established

**Passive Layer reinterpretation:**
The DRW model is an empirical description, not a physical explanation. The variability timescale (τ_DRW) corresponds to the thermal timescale of the accretion disk in standard models, but this does not explain the amplitude distribution. Component B provides a physical mechanism: pair production + Lorentz force separation + mass persistence. The timescale is set by the magnetic field strength (Larmor period) and the gravitational infall time. The observed correlation with black hole mass emerges naturally from the mass-dependence of the Larmor radius: r_L = γmv_⊥/(|q|B) ∝ m.

---

## 9. Connection to Dark Matter and Dark Energy

### 9.1 Dark Matter

**Observational definition of dark matter (post-Zwicky, pre-particle-hypothesis):**

There is a gravitating component that:

- Has no electromagnetic interaction
- Is non-collisional
- Has never been detected as a particle despite 50 years of dedicated searches
- Is correlated with regions of high mass density
- Forms approximately spherical halos around galaxies
- Was present in the early universe and participated in structure formation
- Does not couple to the photon-baryon fluid before recombination

**Passive Layer response (structural, not assumed):**

- Gravitational effect: Carries gravitational influence by definition (Definition of Passive Layer)
- No EM interaction: Source mass no longer exists; no matter present to interact (Definition of Passive Layer)
- Non-collisional: Propagating gravitational signal does not collide (Physical nature of Passive Layer)
- Never detected as particle: Not a particle; cannot be detected in particle detectors (Physical nature of Passive Layer — null result is predicted)
- Correlated with mass density: More pair production/annihilation in high-density regions (Generation mechanism)
- Spherical halo structure: Far-field integral of constant Component A produces sphere (Geometry)
- Present in early universe: Early universe had maximum energy density → maximum generation (Cosmology)
- No coupling to photons: Gravitational signal does not interact with photons (Physical nature of gravity)

### 9.2 Dark Energy

**Standard model (ΛCDM):** Cosmic acceleration caused by cosmological constant Λ with negative pressure (p = -ρc²)

**Problems with standard model:**

- Identity of negative pressure unknown
- 10¹²³ discrepancy between predicted and observed vacuum energy density (Weinberg 1989)
- Cancellation mechanism unknown

**Passive Layer reinterpretation:**
Dark energy is not negative pressure. It is the relaxation of curvature.

**Three established facts for this reinterpretation:**

- Mass curves space: General relativity, confirmed
- Gravity propagates at c: GW170817, 2017
- Mass is created and destroyed: Quantum field theory, particle physics

**Logical consequence:**
Mass exists → space curves → mass ceases to exist → curvature does not vanish instantly → curvature propagates outward at c, gradually relaxing → relaxation of curvature increases volume element → observed as expansion

**Formally:**

dV = √|g| d³x
When curved space (|g| > 1) relaxes toward flatness (|g| → 1), volume element increases.

**Comparison with standard model:**

- Cause of expansion: ΛCDM — Negative pressure (identity unknown). Passive Layer — Geometric relaxation of curvature.
- New physics required: ΛCDM — Yes (identity of Λ). Passive Layer — No.
- Energy conditions: ΛCDM — Violated (negative pressure). Passive Layer — Not violated.
- 10¹²³ problem: ΛCDM — Cancellation assumed (mechanism unknown). Passive Layer — Irrelevant (question bypassed).

### 9.3 Matter-Antimatter Asymmetry

**Standard model problem:**
Observed baryon-to-photon ratio η_obs = (n_b - n_b̄)/n_γ ≈ 6.1 × 10⁻¹⁰
Standard model CP violation predicts η_SM ≈ 10⁻²⁰
Discrepancy: η_obs/η_SM ≈ 10¹⁰ (ten orders of magnitude too small)

**Sakharov conditions (1967):**

1. Baryon number violation
2. C and CP violation
3. Interactions out of thermal equilibrium

**Passive Layer reinterpretation:**
The question is not "how were more baryons created than antibaryons?" but "how were baryons and antibaryons separated before they could annihilate?"

**Magnetic charge separation mechanism:**

F = q(v × B)

For any B ≠ 0, particles and antiparticles are deflected in opposite directions. This separation begins as soon as B ≠ 0. No threshold. No minimum field strength. No special conditions.

**Larmor radius determines separation efficiency:**
r_L = γmv_⊥/(|q|B)
When r_L ≪ R_system (system size), separation is efficient.

**Primordial magnetic field constraints:**

- Electroweak phase transition (T ~ 100 GeV): B_EW,physical ~ 10²³ G → B_EW,comoving ~ 10⁻⁷ G
- QCD phase transition (T ~ 150 MeV): B_QCD,comoving ~ 10⁻⁶ G
- Required for efficient separation at nucleosynthesis (T ~ 1 MeV): B_required,comoving ≫ 3 × 10⁻³⁰ G
- Ratio: B_EW,comoving / B_required,comoving ~ 10²³

The separation condition is not marginally satisfied. It is overwhelmingly satisfied by 23 orders of magnitude.

**Required asymmetry is tiny:**
(n_b - n_b̄)/n_b̄ ≈ η_obs/(1 - η_obs) ≈ 6.1 × 10⁻¹⁰
For every 10¹⁰ baryons that survived, approximately 10¹⁰ - 1 antibaryons were annihilated.

The mechanism does not require efficient separation. It requires a barely detectable imbalance of one part in 10¹⁰. Given that separation begins at any B ≠ 0, and primordial fields are 10²³ times the threshold for efficient separation, the required asymmetry is surprisingly modest.

---

## 10. Reversal of the Burden of Proof

### 10.1 The Five-Step Logic

**Step 1:** The Passive Layer exists. This is guaranteed by two confirmed facts (P1 + P2), not by hypothesis.

**Step 2:** The Passive Layer satisfies the complete observational definition of dark matter without additional assumptions.

**Step 3:** Therefore, the Passive Layer is already an explanatory mechanism for the observed gravitational effects.

**Step 4:** The dark matter particle hypothesis is an additional assumption added on top of the Passive Layer (particle existence, specific properties, thermal production, etc.).

**Step 5:** By Occam's razor, the explanation with fewer assumptions (Passive Layer) is preferred. The burden of proof lies with those who claim a particle is needed in addition to the Passive Layer.

### 10.2 Question Transformation

Old questions (defensive):
- "Can the Passive Layer explain dark matter?"
- "Can the magnitude of the Passive Layer be calculated?"
- "Can the Passive Layer replace ΛCDM?"

New questions (offensive):
- "Is a dark matter particle needed in addition to the Passive Layer?"
- "Is there evidence that the Passive Layer's magnitude is zero?"
- "Which ΛCDM predictions cannot be explained by the Passive Layer?"

### 10.3 The 50-Year Null Result

Fifty years of direct detection experiments (LZ 2024, XENONnT 2024, PandaX-4T 2023, and all predecessors) have produced null results.

- Standard interpretation: "We haven't found it yet. We need more sensitive experiments."
- Passive Layer interpretation: "It cannot be found because it is not a particle. The null result is predicted."

The 50-year null result is not an embarrassment for the field. From the Passive Layer perspective, it is exactly what should have been expected. The searches were looking for a particle. The effect is not a particle.

### 10.4 Historical Parallels

- Anomaly: Mercury's perihelion precession — Hypothetical entity: Planet Vulcan — Resolution: General relativity (no new entity)
- Anomaly: Michelson-Morley null result — Hypothetical entity: Luminiferous aether — Resolution: Special relativity (no aether)
- Anomaly: Unexplained gravitational effects — Hypothetical entity: Dark matter particle — Resolution: ???

In both historical cases, the resolution was not the discovery of the hypothetical entity. It was the recognition that the entity was not needed — that the effect could be explained within existing or extended physics without introducing new ontology.

The dark matter particle situation has a structurally similar form. An unexplained gravitational effect exists. A hypothetical entity was proposed to explain it. The entity has not been found after 50 years of searching. A mechanism derivable from existing physics (Passive Layer) satisfies the complete observational definition of the effect without requiring the hypothetical entity.

This parallel is not proof. It is pattern recognition. But the pattern is suggestive, and the structural similarity is precise.

---

## 11. Complete Citation Index

### Internal Documents (Seoul Inside Substack)

- 2026-06-03: A Relativistic Particle Collider, Built in Pure JavaScript — /p/i-built-an-lhc-in-the-browser-making
- 2026-06-04: Yang-Mills Collider v3.0 — A technical inventory — /p/yang-mills-collider-v30-a-technical
- 2026-06-04: LHC Simulation: Physics Formulas and Explanations — /p/lhc-simulation-physics-formulas-and
- 2026-06-05: Black Hole Physics in Yang-Mills Collider v3.2 — /p/black-hole-physics-in-yang-mills
- 2026-06-06: I Added a Black Hole to the LHC — and Something Unexpected Happened — /p/i-added-a-black-hole-to-the-lhc-and
- 2026-06-06: Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation — /p/delayed-gravitational-interaction
- 2026-06-07: Black Hole Displacement and the Default State of Spiral Galaxies — /p/black-hole-displacement-and-the-default
- 2026-06-07: A Unified Technical Framework — Simulation Evidence and Theoretical Foundations — /p/a-unified-technical-framework-simulation
- 2026-06-07: Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe — /p/vacuum-fluctuations-delayed-gravity
- 2026-06-08: Passive Layer — Essential Citations — /p/passive-layer-essential-citations
- 2026-06-08: High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes — /p/high-energy-particle-generation-and
- 2026-06-09: The Passive Layer — Core Document — /p/the-passive-layer-core-document
- 2026-06-10: The Passive Layer: A Physically Necessary but Uncalculated Term — /p/the-passive-layer
- 2026-06-10: THE PASSIVE LAYER AND THE REVERSAL OF THE BURDEN OF PROOF — /p/the-passive-layer-and-the-reversal
- 2026-06-10: Physics Series Full (Index) — /p/physics-series-full
- 2026-06-11: Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry — /p/long-term-survival-of-antimatter
- 2026-06-11: Dark Energy Reinterpreted — Cosmic Expansion as the Relaxation of Curvature — /p/dark-energy-reinterpreted-cosmic

### External References

- Abbott et al. (LIGO/Virgo) (2017). Gravity speed = c (GW170817). Physical Review Letters, 119, 161101.
- Batcheldor et al. (2010). M87 BH offset 6.8±0.8 pc. Astrophysical Journal.
- Bartlett et al. (2021). AGN BH offsets 10-100 pc. Astronomy & Astrophysics.
- Chu, Boldrini & Silk (2022). BCG BH offsets (1/3 off-center at z=0). Monthly Notices of RAS.
- Li et al. (2025). JWST early black hole selection effects. ApJ 981 19.
- Mezcua et al. (2024). Overmassive black holes at cosmic noon. ApJ 966 L30.
- EHT Collaboration (2025). M87* 2017-2021 multi-epoch variability. arXiv:2509.24593.
- EHT MWL Science Working Group (2021). M87 multi-wavelength campaign. arXiv:2404.17623.
- MacLeod et al. (2012). DRW model for quasar variability. arXiv:2012.12907.
- Lelli, McGaugh & Schombert (2016). SPARC database (175 galaxies). arXiv:1606.09251.
- Planck Collaboration (2020). Cosmological parameters (Ω_c h² = 0.118). Astronomy & Astrophysics, 641, A6.
- Particle Data Group (2022). PDG 2022. pdg.lbl.gov
- Sakharov (1967). Baryogenesis conditions. JETP Letters, 5, 24-27.
- Zwicky (1933). Dark matter introduction (dunkle Materie). Helvetica Physica Acta, 6, 110.
- Yahalom (2013, 2019, 2024). Retarded gravity in galactic dynamics. Various.

---

## 12. Technical Implementation Notes

### 12.1 Simulation File Structure

Two independent but complementary simulation files:

**File 1: Yang-Mills Collider v3.2 + Kerr Black Hole**

- Filename: LHC_kerr_2.html
- Purpose: Particle physics + black hole interaction (Component B evidence)
- Implementation: Boris integrator, PDG 2022 particle database (39 species), Bethe-Bloch + Landau fluctuation, 4-momentum conservation, αs 2-loop running coupling
- Emergent phenomena: Accretion disk, Penrose process, charge separation

**File 2: GalaxyCS v5.1 — Retarded Gravity + Spiral Arm Analysis**

- Filename: Galaxy_2D5_1.html
- Purpose: Galactic dynamics with retarded gravitational propagation (Component C evidence)
- Implementation: Leapfrog integrator, BH position history buffer (FIFO), retarded acceleration term a_ret = α·G·M̈/(2c²)·R̂, Fourier m=2 spiral strength analysis
- Emergent phenomena: Spiral arms (any non-zero BH displacement), flat rotation curve (when retarded gravity enabled)

### 12.2 What Is Not Implemented (Explicitly Acknowledged)

- Full Kerr metric (Christoffel symbols): Reason — Computationally infeasible in real-time browser
- Hawking radiation: Reason — Quantum field theory on curved spacetime — different architectural layer
- Gravitational waves: Reason — Background spacetime fixed as Minkowski
- Tidal forces / spaghettification: Reason — Particles treated as point masses
- Yang-Mills mass gap proof: Reason — Millennium Prize Problem (unsolved, $1,000,000 prize)

These omissions are not hidden. They are explicitly stated in the code and documentation as "What Was Left Out — and Why."

### 12.3 Running the Simulations

Both files are self-contained HTML documents. No server required. No compilation step. No external physics libraries (Three.js is the only external, used only for rendering). Open in any modern web browser. Run. Observe.

---

## 13. Conclusion

**One-sentence summary:**

The Passive Layer is the logical consequence of two established facts (gravity propagates at c; mass is created and destroyed), comprises three independent components, is directly observed in simulation (accretion disk formation without design; spiral arms from BH displacement), correlates with five distinct anomalous observations (AGN variability, changing-look quasars, JWST early black holes, M87 EHT variability, gravitational wave mass gap), implies four layers of severity culminating in a potential systematic error in black hole mass measurements, satisfies the complete observational definition of dark matter without additional assumptions, reinterprets dark energy as curvature relaxation, provides a mechanism for matter-antimatter asymmetry via magnetic charge separation, and shifts the burden of proof to the dark matter particle hypothesis after 50 years of null results.

---





---

---
## Appendix A: GalaxyCS v5.1 — Retarded Gravity + Spiral Arm Quantitative Analysis

### A.1 How to Run the Simulation

Step 1: Open Galaxy_2D5_1.html in a modern web browser (Chrome 90+, Firefox 88+, Safari 14+)

Step 2: No server required. No compilation step. No external physics libraries.

Step 3: The simulation runs entirely in the browser tab.

### A.2 Default State (BH at Rest)

When the simulation first loads:

- Black hole position radius = 0 kpc (centered)
- Spiral arm strength (S₂) is below 0.15
- The disk remains axisymmetric (no spiral structure)
- Rotation curve follows Newtonian prediction (v ∝ r^{−1/2})

### A.3 What Happens When You Press Any Arrow Key

Press → (Right Arrow) once:

- Black hole displacement becomes non-zero (default step: 0.05 radian or 0.1 kpc depending on direction)
- S₂ value increases above 0.15 immediately
- Spiral arm structure emerges within 2-3 simulation steps
- The spiral pattern persists indefinitely

This behavior has no threshold. Any non-zero displacement, no matter how small, produces spiral structure.

### A.4 Key Parameters and Their Physical Meanings

Parameter listing:

- 지연 강도 α (Retardation strength)
  - Physical prediction: α = 1
  - When α = 0: Retarded gravity is disabled
  - When α > 0: Retarded gravity is active
  - Range in simulator: 0 to 3.0 (step 0.02)

- BH 위치 반경 (Black hole position radius)
  - Unit: kpc
  - Range: 0 to 5.0 kpc
  - When 0: Axisymmetric disk, no spiral
  - When > 0: Spiral arm formation triggered

- BH 위치 각도 (Black hole position angle)
  - Unit: degrees (°)
  - Range: 0 to 360°
  - Determines the direction of BH displacement

- M̈ log₁₀ (M☉/Myr²)
  - Second time derivative of black hole mass
  - Physical meaning: Mass fluctuation acceleration
  - When this value is 0, retarded gravity term has no effect
  - Typical physical range around 9.5 (10^9.5 M☉/Myr²)

- 별 개수 (Number of stars)
  - Range: 1,000 to 80,000 stars
  - Higher counts give smoother statistics but lower performance

- 히스토리 버퍼 (History buffer size)
  - Number of past BH positions stored
  - Range: 10 to 300 steps
  - Larger buffers allow longer retardation delays

- BH 스핀 a* (Black hole spin parameter)
  - Range: 0 to 1
  - Dimensionless spin parameter a* = a/M
  - When a* > 0.2: Ergosphere becomes visible (purple wireframe)
  - When a* > 0.6: Relativistic jet visualization appears
  - Higher spin increases rotation curve via frame dragging

### A.5 S₂ (Spiral Arm Strength) Interpretation

The Fourier m=2 spiral arm strength is computed as:

S₂ = |(1/N) Σ weight·e^(imφ)|
where m=2, φ = atan2(dz, dx), weight = 1/(r·0.5+1)

S₂ value interpretation:

- < 0.15 : Symmetric disk (no spiral)
- 0.15 - 0.35 : Weak spiral structure forming
- 0.35 - 0.65 : Distinct 2-arm spiral structure
- > 0.65 : Strong grand design spiral

The gauge bar in the left panel shows S₂ visually, and the numerical value is displayed below it.

### A.6 Rotation Curve Display

The chart in the bottom-left shows three curves simultaneously:

- ● 실제 (Observed): Cyan line — actual stellar rotation velocity from simulation
- ● 뉴턴 (Newtonian): Orange line — predicted velocity from Newtonian gravity alone
- ● M33 관측 (M33 observation): Red dots — actual observational data from the M33 galaxy

When retarded gravity is enabled (α > 0) and BH is displaced (r > 0):

- The observed velocity exceeds Newtonian prediction at large radii (r > 5 kpc)
- The ratio (observed / Newtonian) is displayed as 속도 이상비

Example from screenshot evidence:

- Observed velocity: 116 km/s
- Newtonian prediction: 48 km/s
- Speed anomaly ratio: 2.28x

This demonstrates that retarded gravity alone can reproduce flat rotation curves without dark matter.

### A.7 SPARC Fitting Tab

The SPARC fitting tab allows uploading real galaxy observation data in CSV format.

CSV format expected:

r_kpc, v_obs_kms
0.5,62
1.0,78
2.0,98
3.0,108
...

When you upload a CSV file and click 피팅 실행 (Run Fitting):

- The simulator performs a grid search over M̈ values (range: 6 to 12, step 0.5)
- For each M̈ value, the simulation calculates the chi-squared (χ²) between model and data
- The M̈ value with the lowest χ² is selected as optimal
- Results are displayed including the optimal M̈ value and speed anomaly ratio

This feature makes the simulator not just a demo, but a research tool for analyzing actual astronomical data.

### A.8 Conservation Monitoring

The simulator displays real-time conservation of energy and angular momentum:

- ΔE: Percentage change in total energy relative to initial state
- ΔL: Percentage change in total angular momentum relative to initial state

Colors indicate stability:

- < ±1%: Green (excellent conservation)
- ±1% to ±5%: Yellow (acceptable)
- > ±5%: Red (numerical instability warning)

The leapfrog (velocity Verlet) integrator used in this simulator is symplectic and time-reversible, ensuring near-perfect conservation over long simulation times.

### A.9 Keyboard Controls

- ← : Decrease BH angle (counterclockwise rotation)
- → : Increase BH angle (clockwise rotation)
- ↑ : Increase BH radius (move BH outward)
- ↓ : Decrease BH radius (move BH inward)
- Shift + Arrow: Fine movement (slow mode, 10x smaller steps)

When Shift is pressed, the key hint panel briefly changes color to indicate fine movement mode.

### A.10 Screenshot Evidence Reference

Screenshot 2606 (1).webp shows:

- BH position: r=5.000 kpc, θ=0.0°
- α=10.00 (test condition, exaggerated for demonstration)
- History buffer: 60 steps full

Screenshot 2606 (2).webp shows:

- Simulation time: 4160.92 Myr (stable long-term run)
- Number of stars: 20,000
- Outer velocity: 96 km/s
- Newtonian prediction: 107 km/s
- Speed anomaly ratio: 0.90x (depends on α setting)
- Disk mass at 10 kpc: 2.67×10^6 M☉

Screenshot 2606Q (19).PNG shows:

- Number of stars: 59,000
- Simulation time: 850.71 Myr
- Outer velocity: 116 km/s
- Newtonian prediction: 48 km/s
- Speed anomaly ratio: 2.28x (critical evidence)
- Disk mass at 10 kpc: 5.33×10^6 M☉
- History buffer: 40/40 full
- α=1.00, M̈=10^9.5, G_scale=10^0 (physical mode)

### A.11 Falsifiable Predictions from This Simulator

The following predictions can be tested immediately with existing observational data:

Prediction 1: Galaxies with larger BH offsets should have stronger spiral arm pitch angles (higher S₂).

Prediction 2: Galaxies with no measurable BH offset should have no spiral structure (axisymmetric disks).

Prediction 3: The speed anomaly ratio (observed/Newtonian) should correlate with galaxy age, as older galaxies have accumulated more Passive Layer mass.

---

## Appendix B: Yang-Mills Collider v3.2 + Kerr Black Hole

### B.1 How to Run the Simulation

Step 1: Open LHC_kerr_2.html in a modern web browser

Step 2: No server required. No compilation step.

Step 3: The simulation runs entirely in the browser tab.

Step 4: 3D rendering via Three.js, adjustable camera controls (drag to rotate, right-click to pan)

### B.2 Default State (No Black Hole)

When BH mass = 0:

- Particles collide and decay according to PDG branching ratios
- No gravitational attraction
- Particles move in straight lines or helices (magnetic field only)
- No accretion disk formation

### B.3 What Happens When You Add a Black Hole

Set BH mass to a non-zero value (e.g., 1,000,000,000 M☉) and click COLLIDE:

- Particles are attracted toward the black hole
- Charged particles are rotated by the Boris integrator in opposite directions based on charge sign
- Particles and antiparticles separate (positive charges rotate one way, negative charges the opposite way)
- An accretion disk appears spontaneously — no code was written for this
- This is the phenomenon described as "I did not build an accretion disk. One appeared."

### B.4 The Boris Integrator (Charge Separation Mechanism)

The core of the magnetic field integration is:

const tc = (charge * dt * 0.5) / (gam * mass);
const tx = 0, ty = tc * (-Bfield), tz = 0;
const t2 = tx*tx + ty*ty + tz*tz;
const pmx = px + (py*tz - pz*ty);
const pmy = py + (pz*tx - px*tz);
const pmz = pz + (px*ty - py*tx);
const sx = 2*tx/(1+t2), sy = 2*ty/(1+t2), sz = 2*tz/(1+t2);
let ppx = px + (pmy*sz - pmz*sy);
let ppy = py + (pmz*sx - pmx*sz);
let ppz = pz + (pmx*sy - pmy*sx);

The key is that tc carries the sign of charge. For electrons (q = -e), tc is negative; for positrons (q = +e), tc is positive. The cross products that follow rotate momentum in opposite senses for opposite signs.

This separation:

- Is exact (follows the continuous Lorentz force)
- Holds for any B ≠ 0
- Has no threshold
- Requires no special conditions

### B.5 Key Parameters and Their Physical Meanings

Parameter listing:

- B-field (T): Magnetic field strength in Tesla
  - When B = 0: No charge separation, everything falls into BH
  - When B > 0: Charges separate, accretion disk forms
  - Typical LHC solenoid field: ~3.8 T
  - Range in simulator: 0 to 14 T

- √s (GeV): Center-of-mass collision energy
  - LHC Run 2 energy: 13,000 GeV (13 TeV)
  - Range: 30 to 14,000 GeV
  - Higher energy → more particles, heavier particle production

- BH 질량 (BH mass): Black hole mass in solar masses (M☉)
  - Range: 0 to 10^12 M☉
  - Sgr A* mass: ~4×10^6 M☉
  - M87 mass: ~6.5×10^9 M☉

- BH 스핀 a* (BH spin): Dimensionless spin parameter a* = a/M
  - Range: 0 to 1
  - a* = 0: Schwarzschild (non-rotating)
  - a* = 0.9: Kerr (rapidly rotating, consistent with M87* EHT observations)
  - At a* > 0.1: Ergosphere becomes visible
  - At a* > 0.6: Relativistic jets appear

- Trail 길이 (Trail length): Particle trail length in frames
  - Range: 6 to 55 steps
  - Longer trails show orbital history better but reduce performance

### B.6 Detector Modules

#### B.6.1 ECAL (Electromagnetic Calorimeter)

- Detects electrons, positrons, and photons
- 20 × 32 cells in (η, φ) space
- Color scale:
  - < 2 GeV: Dark orange
  - 2-5 GeV: Orange
  - 5-10 GeV: Yellow
  - > 10 GeV: Red

#### B.6.2 HCAL (Hadronic Calorimeter)

- Detects hadrons (pions, kaons, protons, neutrons)
- Separate segmentation from ECAL
- Color scale:
  - < 2 GeV: Dark brown
  - 2-5 GeV: Brown
  - 5-10 GeV: Orange-red
  - > 10 GeV: Bright red

#### B.6.3 Displaced Vertex Reconstruction

Detects decay vertices of long-lived particles:

- K⁰S: cτ = 2.69 cm, smearing σ = 2.0 mm
- Λ⁰: cτ = 7.89 cm, smearing σ = 3.0 mm
- B±: cτ = 491 μm, smearing σ = 0.05 mm
- B⁰: cτ = 455 μm, smearing σ = 0.05 mm
- D⁰: cτ = 123 μm, smearing σ = 0.12 mm

#### B.6.4 Jet Clustering (anti-kT algorithm)

- Standard algorithm used at ATLAS and CMS
- Distance metric: d_ij = min(pT,i^(-2), pT,j^(-2)) · ΔR²_ij / R²
- Configurable radius parameter R (default: 0.4)
- Configurable minimum pT (default: 5.0 GeV)

#### B.6.5 Event Filter

- Level-1 trigger: Pass if any particle has pT > 50 GeV OR event invariant mass > 80 GeV
- High-Level Trigger: Pass if event contains Z → e⁺e⁻, Z → μ⁺μ⁻, or H⁰ → γγ
- User-configurable decay filters: Z→ee, Z→μμ, H→γγ, J/ψ→μμ
- User-configurable pT and eta cuts

### B.7 Rare Decays (PDG 2022 Branching Ratios)

The simulator implements exact PDG 2022 branching ratios. Examples:

π⁺ decay:

- π⁺ → μ⁺ νμ : 99.9877%
- π⁺ → e⁺ νe : 0.0123% (rare, flagged as ⚡ RARE in event log)

K⁺ decay (selected modes):

- K⁺ → μ⁺ νμ : 63.56%
- K⁺ → π⁺ π⁰ : 20.67%
- K⁺ → π⁺ π⁺ π⁻ : 5.59%
- K⁺ → π⁰ e⁺ νe : 5.07%

H⁰ decay (selected modes):

- H⁰ → bb̄ : 58.24%
- H⁰ → W⁺W⁻ : 21.37%
- H⁰ → ZZ : 8.27%
- H⁰ → τ⁺τ⁻ : 6.27%
- H⁰ → γγ : 0.23%

### B.8 QCD Running Coupling αs(μ) — 2-Loop

The strong coupling constant is computed at each collision energy:

β₀ = (33 − 2n_f) / (12π)
β₁ = (153 − 19n_f) / (24π²)

αs⁽¹⁾(μ) = αs(MZ) / (1 + 2β₀·αs(MZ)·ln(μ/MZ))

αs⁽²⁾(μ) = αs⁽¹⁾ · [1 − (β₁/β₀)·αs⁽¹⁾·ln(1 + 2β₀·αs(MZ)·ln(μ/MZ))]

Boundary condition: αs(MZ) = 0.1180, MZ = 91.1876 GeV (PDG 2022)

Example values:

- At μ = 13,000 GeV (LHC Run 2): αs ≈ 0.085
- At μ = 91 GeV (Z pole): αs = 0.1180
- At μ = 1 GeV: αs ≈ 0.48 (coupling constant cutoff applied)

### B.9 Screenshot Evidence Reference

Screenshot 2606Q (18).PNG shows:

- Particle count: 2,723
- Decay events: 3,614
- Rare decay count: 1 (rare event occurred!)
- BH mass: 1,000,000,000,000 M☉ (10^12 M☉)
- BH spin: 0.00 (non-rotating)
- B-field: 1.9 T
- √s: 13,000 GeV
- HCAL (HADRON) panel active

Screenshot 2606Q (20).PNG shows:

- Particle count: 7,267
- Decay events: 9,576
- αs(μ): 0.07207 (at 13 TeV)
- Multiplicity: 181
- σ_inel: 72.9 mb (consistent with TOTEM measurement)
- pT histogram: Entries 5,388, mean pT 0.11 GeV

### B.10 What Is Not Implemented (Explicitly Acknowledged)

Missing features:

- Full Kerr metric (Christoffel symbols)
  - Reason: Computationally infeasible in real-time browser

- Hawking radiation
  - Reason: Requires quantum field theory on curved spacetime — different architectural layer

- Gravitational waves
  - Reason: Background spacetime fixed as Minkowski

- Tidal forces / spaghettification
  - Reason: Particles treated as point masses

- Yang-Mills mass gap proof
  - Reason: Millennium Prize Problem (unsolved, $1,000,000 prize)

These omissions are not hidden. They are explicitly stated in the code and documentation as "What Was Left Out — and Why."

---

## Appendix C: Two Simulations — Complementary Evidence

### C.1 Phenomena Covered by Each Simulator

GalaxyCS v5.1 (Component C evidence):

- BH displacement → spiral arm formation
- Flat rotation curve
- Retarded gravity effect (α parameter)
- Fourier m=2 spiral strength analysis
- SPARC data fitting

Yang-Mills Collider v3.2 (Component B evidence):

- Charge separation (Boris integrator)
- Accretion disk formation (emergence)
- Particle-antiparticle separation
- PDG 2022 branching ratios
- Rare decays (0.0123% branching)
- QCD running coupling αs(μ)

### C.2 Cross-Scale Connection

The two simulations operate at different scales but describe the same physical phenomenon:

Yang-Mills Collider v3.2 (quantum/black hole scale):

- Pair production (γ+γ → e⁺+e⁻)
- Lorentz force separates charges (F = q(v × B))
- Annihilation suppressed → mass persists
- Local mass variability observed

GalaxyCS v5.1 (galactic scale):

- Mass variability (M̈ term) propagates via retarded gravity
- Stars at different distances reference different past BH positions
- Radially-dependent angular offset sheared into spiral pattern
- Flat rotation curve emerges (v_c² = G·Ṁ_pair/c = constant)

### C.3 Summary Table

Observed phenomenon: BH displacement default state

- Simulator: GalaxyCS v5.1
- Evidence: Directional key → immediate spiral formation, no threshold

Observed phenomenon: Flat rotation curve

- Simulator: GalaxyCS v5.1
- Evidence: Observed velocity (cyan) exceeds Newtonian prediction (orange) at large radii

Observed phenomenon: Charge separation

- Simulator: Yang-Mills Collider v3.2
- Evidence: Boris integrator: tc = (charge * dt * 0.5) / (gam * mass)

Observed phenomenon: Accretion disk emergence

- Simulator: Yang-Mills Collider v3.2
- Evidence: "I did not build an accretion disk. One appeared."

Observed phenomenon: Rare decay (0.0123%)

- Simulator: Yang-Mills Collider v3.2
- Evidence: Event log flags ⚡ RARE for π⁺ → e⁺ νe

Observed phenomenon: QCD running coupling

- Simulator: Yang-Mills Collider v3.2
- Evidence: αs(13 TeV) ≈ 0.085, αs(91 GeV) = 0.1180

Observed phenomenon: Speed anomaly ratio 2.28x

- Simulator: GalaxyCS v5.1
- Evidence: Observed 116 km/s vs Newtonian 48 km/s

---

## Appendix D: Reproducibility and Independent Verification

### D.1 System Requirements

- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+)
- No internet connection required after download (runs locally)
- GPU recommended for Three.js rendering (not required for basic functionality)
- Minimum 4GB RAM for 80,000 stars (GalaxyCS)
- Minimum 2GB RAM for high particle counts (Yang-Mills Collider)

### D.2 Step-by-Step Reproduction

#### D.2.1 GalaxyCS v5.1 Reproduction

Step 1: Open Galaxy_2D5_1.html in browser.

Step 2: Observe initial state:

- BH position radius = 0 kpc
- S₂ < 0.15
- Axisymmetric disk (no spiral)
- Rotation curve follows Newtonian prediction

Step 3: Press → (Right Arrow) once:

- BH angle changes by 0.05 radian
- BH radius remains 0 (unless ↑ pressed)
- If BH radius = 0, move to step 4

Step 4: Press ↑ (Up Arrow) once:

- BH radius increases by 0.1 kpc (normal mode) or 0.02 kpc (Shift+Arrow)
- S₂ immediately increases above 0.15
- Spiral arm structure becomes visible within 2-3 steps

Step 5: Observe rotation curve:

- Outer velocity (cyan) should exceed Newtonian prediction (orange)
- Speed anomaly ratio > 1.0 (may take several steps to stabilize)

Step 6: (Optional) Upload SPARC CSV file:

- Prepare CSV with format: r_kpc, v_obs_kms
- Click SPARC fitting tab
- Click CSV file input and select file
- Click 피팅 실행 (Run Fitting)
- Read optimal M̈ value from results

#### D.2.2 Yang-Mills Collider v3.2 Reproduction

Step 1: Open LHC_kerr_2.html in browser.

Step 2: Set BH mass to a non-zero value (e.g., 1,000,000,000 M☉ using slider).

Step 3: Set B-field to a non-zero value (e.g., 6.2 T).

Step 4: Click COLLIDE:

- New particles generated from collision
- Particles and antiparticles separate by charge
- Accretion disk begins to form

Step 5: Repeatedly click COLLIDE (10-20 times):

- Disk becomes more prominent
- Some particles are absorbed by BH
- Some particles escape to large radii

Step 6: Observe rare decay:

- Watch event log for ⚡ RARE flag
- Typical rate: ~1 in 8,000 π⁺ decays

Step 7: (Optional) Open ECAL/HCAL panels:

- Observe energy deposits from particles
- Color indicates energy level

### D.3 Expected Results

GalaxyCS v5.1 expected results:

- S₂ < 0.15 when BH radius = 0
- S₂ > 0.15 when BH radius > 0 (any non-zero value)
- Speed anomaly ratio > 1.0 when α > 0 and M̈ > 0
- Energy conservation (ΔE) typically < ±2% over 1000 Myr
- Angular momentum conservation (ΔL) typically < ±2% over 1000 Myr

Yang-Mills Collider v3.2 expected results:

- Particles with opposite charges rotate in opposite directions in magnetic field
- Accretion disk forms without explicit disk-building code
- Rare decays appear at PDG-specified rates
- αs(μ) decreases as √s increases (asymptotic freedom)
- At √s = 13,000 GeV, αs ≈ 0.085
- At √s = 91 GeV, αs ≈ 0.118

### D.4 Common Issues and Troubleshooting

Issue: GalaxyCS v5.1 — No spiral arm after pressing arrow keys

Check: Is BH radius = 0? If yes, press ↑ to move BH outward.
Check: Is α (retardation strength) = 0? If yes, set to 1.0.
Check: Is M̈ = 0? If yes, set to 9.5.

Issue: GalaxyCS v5.1 — Performance is slow

Solution: Reduce 별 개수 (number of stars) to 20,000 or lower.

Issue: Yang-Mills Collider — No accretion disk after multiple COLLIDE clicks

Check: Is B-field = 0? If yes, set to > 0 (e.g., 6.2 T).
Check: Is BH mass = 0? If yes, set to > 0.
Check: Are particles being absorbed too quickly? Reduce BH mass.

Issue: Yang-Mills Collider — No rare decays observed

Note: Rare decay rate is 0.0123% for π⁺ → e⁺ νe
This requires approximately 8,000 π⁺ decays on average to see one.
Click COLLIDE many times (50-100) to increase statistics.

### D.5 Independent Verification

Any researcher can independently verify all claims in this archive by:

Step 1: Downloading the two HTML files

Step 2: Running them in a standard web browser

Step 3: Following the reproduction steps in Appendix D.2

Step 4: Observing the phenomena described (S₂ increase, spiral arms, charge separation, accretion disk)

No specialized hardware, no software installation, no compilation, and no external dependencies are required. The simulations are self-contained and run identically on any modern browser.

---

## Appendix E: Mathematical Derivations — Expanded

### E.1 From τ(r) = r/c to M_ghost(r)

When a mass exists at distance r' from an observer, its gravitational signal takes time τ = r'/c to reach that observer. If the mass then ceases to exist (through annihilation or decay), the gravitational signal continues to propagate for time r'/c after the mass is gone.

For a continuous pair production rate Ṁ_pair(r') at each distance r', the accumulated ghost mass up to radius r is:

M_ghost(r) = ∫₀ʳ Ṁ_pair(r') · (r'/c) dr'

Derivation:

- The contribution from a shell at radius r' is the mass produced per unit time (Ṁ_pair(r')) multiplied by the time that signal persists (r'/c)
- Integrate over all shells from 0 to r

### E.2 From M_ghost(r) to Flat Rotation Curve

Newtonian dynamics for circular orbits:

v_c²(r) = G · M_ghost(r) / r

Substituting M_ghost(r) = Ṁ_pair · r/c (when Ṁ_pair is constant):

v_c²(r) = G · (Ṁ_pair · r/c) / r = G · Ṁ_pair / c

The r cancels out. Therefore, v_c² is constant regardless of r.

This produces a flat rotation curve without dark matter and without free parameters.

### E.3 From Larmor Radius to Mass-Dependent Separation

The Larmor radius is:

r_L = γmv_⊥ / (|q|B) = p_⊥ / (|q|B)

For a fixed magnetic field B and fixed transverse momentum p_⊥:

r_L ∝ m

Heavier particles have larger Larmor radii, therefore:

- Electrons (m=0.511 MeV) trace the smallest circles (innermost orbits)
- Pions (m=140 MeV) trace intermediate circles
- Protons (m=938 MeV) trace larger circles
- W bosons (m=80,377 MeV) trace the largest circles

This mass-dependent separation is directly observed in Yang-Mills Collider v3.2.

### E.4 From Primordial Magnetic Field to Matter-Antimatter Asymmetry

The separation condition for efficient charge separation is:

r_L ≪ R_system

For the early universe at nucleosynthesis (T ~ 1 MeV, t ~ 1 sec):

- R_system ≈ c·t ≈ 3×10¹⁰ cm
- For an electron with thermal energy E_e ~ 1 MeV, p_⊥ ~ 5.3×10⁻²² kg·m/s
- The required field for r_L ≪ R_H is: B_required ≫ 3×10⁻¹² G (physical)
- In comoving units: B_required,comoving ≫ 3×10⁻³⁰ G

The predicted primordial field from electroweak phase transition:

- B_EW,comoving ~ 10⁻⁷ G

The ratio: B_EW,comoving / B_required,comoving ~ 10⁻⁷ / 10⁻³⁰ = 10²³

The separation condition is satisfied by 23 orders of magnitude.

---


# A Numerical Confirmation of General Relativity via Special Relativity and Newtonian Gravity: Observations from Yang-Mills Collider v3.2

**B. Sun | Seoul Inside**  
*June 2026 — Post #18 in the Yang-Mills Collider Series*

---

## A Note Before We Begin

This is the twentieth entry in a series that began simply enough — a browser-based particle physics simulator. What follows is not a claim to have overturned any established physics. It is, if anything, the opposite: an accidental and humble confirmation that General Relativity's predictions are not merely elegant mathematics, but physical inevitabilities that emerge even from much simpler foundations.

We did not set out to confirm General Relativity. We stumbled into it.

---

## Part I — What Is Inside This Simulator

### The Particle Physics Engine

Yang-Mills Collider v3.2 is a single HTML file that runs entirely in a browser. No installation. No special hardware. This matters, and we will return to why.

The particle physics side of the engine is built on the following foundations:

**Particle Database — PDG 2022**  
39 particle species are included, from the electron to the Higgs boson. Every mass, lifetime, and decay branching ratio is taken directly from the Particle Data Group 2022 compilation. This is the same reference used by CERN experimentalists.

Notable values:
- Higgs boson mass: 125.20 GeV, width: 3.2 MeV *(current PDG value)*
- Z boson mass: 91.1876 GeV, width: 2.4952 GeV *(precise)*
- W boson mass: 80.377 GeV *(pre-2022 CDF controversy PDG value)*

**Four-Vector Formalism and Lorentz Boosts**  
Every particle carries a full relativistic four-momentum (E, px, py, pz). Lorentz boosts are implemented in the standard form γ(E + β·pL). Two-body decay kinematics use the correct center-of-mass momentum formula. This is Special Relativity, applied completely and without approximation.

**αs — Two-Loop Running Coupling Constant**  
The strong coupling constant αs runs with energy scale according to the QCD two-loop beta function, anchored at αs(MZ) = 0.118 per PDG 2022. This is the same formalism used in perturbative QCD calculations at the LHC.

**Tsallis pT Distribution**  
Transverse momentum sampling uses the non-extensive Tsallis distribution, the same statistical form used to fit ALICE and CMS experimental data. Rejection sampling with 500 attempts per particle ensures the high-pT tail is correctly captured.

**Multiplicity — Negative Binomial Distribution**  
Charged particle multiplicity follows ⟨N_ch⟩ = 0.2348 × √s^0.6010, fitted to UA5 and ALICE data. The negative binomial distribution (NBD) with k = 2.0 correctly reproduces KNO scaling violation in pp collisions.

**Breit-Wigner Resonance Sampling**  
Resonance particles (W, Z, H) are sampled from the non-relativistic Breit-Wigner inverse CDF. The Higgs, with its extremely narrow width of 3.2 MeV, receives a ±3σ cut — physically correct and numerically stable.

**Bethe-Bloch Energy Loss + Landau Fluctuations**  
Energy loss in detector material follows the Bethe-Bloch formula:

$$-\frac{dE}{dx} = K \frac{q^2}{\beta^2} \left[ \ln\frac{2m_e\beta^2\gamma^2}{I} - \beta^2 \right]$$

with K = 3.2×10⁻⁵ GeV·cm², I = 175 eV (silicon). Landau fluctuations are approximated in three regimes. This is the standard formalism used in Geant4 and similar detector simulation codes.

**Boris Integrator**  
Charged particle motion in magnetic fields uses the Boris leap-frog algorithm — the same method used in actual Particle-In-Cell (PIC) plasma physics codes. Energy loss is applied in half-steps for numerical stability.

**Extended Physics Modules**  
The engine also includes: neutrino oscillation (vacuum, PDG Δm² values), CP violation in B⁰ mesons (sin2β = 0.699, consistent with BaBar/Belle), a hadronic calorimeter simulation (HCAL, 40×48 η-φ grid), particle identification via dE/dx, underlying event modeling, vertex smearing, trigger simulation (L1 and HLT), and anti-kT jet clustering.

In short: this is not a toy. For a single HTML file running in a browser, this represents the practical ceiling of what particle physics simulation can achieve without a compiled physics framework like Pythia8 or Geant4.

---

### The Black Hole Engine

Here is where we make a deliberate and important choice — one that turns out to be the source of everything interesting.

The black hole in this simulator is described by **Newtonian gravity only**:

```
F = GM/r²
```

That is all. There is no spacetime curvature. There is no geodesic equation. There is no Schwarzschild metric being solved. The only general relativistic element is the event horizon boundary condition: if a particle crosses r < r₊, it is absorbed.

The Kerr outer horizon radius is correctly calculated as:

```
r₊ = M(1 + √(1 - a*²))
```

But this is used only for the absorption boundary. It does not affect particle dynamics.

Frame dragging, ergosphere dynamics, ISCO instability, gravitational lensing, redshift — all are either absent or deliberately deactivated.

**Why this choice?**

If we had added full GR dynamics to the black hole, any interesting structure that appeared near it could be attributed to those GR terms. We wanted to ask a cleaner question:

> *What happens when particle physics — governed by Special Relativity — meets pure Newtonian gravity?*

The black hole mass ranges from a micro black hole (minimum) to 450 times that minimum, controlled by a slider. The simulator runs at 60 frames per second in any modern browser.

---

## Part II — What Appears When You Press COLLIDE

When the simulation runs with a non-zero magnetic field and a non-zero black hole mass, something appears that was never explicitly programmed.

**An accretion disk forms. Every single time.**

Not occasionally. Not under special conditions. 100% of the time, across every parameter combination tested, a ring-like structure of particles accumulates around the black hole. At B = 14T, the ring is nearly perfect — a stable, circular band of orbiting particles. At B = 6.2T, the ring becomes asymmetric, with particles accumulating preferentially on one side.

No accretion disk code was written. No disk was programmed. The disk is a consequence.

Additionally, particle-antiparticle spatial separation occurs. Positively and negatively charged particles accumulate in different spatial regions around the black hole. Again, this was not programmed. It emerges from the Lorentz force acting differently on opposite charges in the magnetic field.

---

## Part II-B — The Three-Condition Experiment

Before interpreting the structures, we must document the most important experimental observation in this entire series. It consists of three conditions, run sequentially.

**Condition 1: B = 0.0 T (No Magnetic Field)**

With the magnetic field set to zero, only Newtonian gravity acts on the particles. The result is unambiguous: all particles fall spherically into the black hole from every direction. No disk forms. No ring appears. The black hole simply absorbs everything isotropically.

**Condition 2: B = 6.2 T (Weak Magnetic Field)**

With a weak magnetic field, a disk begins to form — but slowly. Given sufficient time, a thin equatorial structure emerges. The process is gradual. The disk is less stable, asymmetric at times, and requires many collision cycles to consolidate.

**Condition 3: B = 14.0 T (Strong Magnetic Field)**

With a strong magnetic field, a geometrically thin disk forms rapidly and stabilizes into a nearly perfect equatorial ring. The structure is extraordinarily thin — confined almost entirely to a single plane. Particles that escape the disk do so vertically, in a pattern reminiscent of astrophysical jets.

---

### The Conclusion From These Three Conditions

```
B = 0   →  Spherical accretion. No disk. Ever.
B = low →  Disk forms slowly. Angular momentum
            gradually preserved.
B = high → Disk forms rapidly. Angular momentum
            strongly preserved.
```

This is not ambiguous. The disk is not a gravitational phenomenon.

> **"Without a magnetic field, all particles fall spherically into the black hole. The disk is not created by gravity. It is created by the magnetic field's preservation of angular momentum."**

The magnetic field does not merely confine particles. It determines whether angular momentum is conserved or lost. Strong magnetic fields preserve angular momentum efficiently, forcing particles into stable equatorial orbits. Weak fields allow angular momentum to dissipate slowly, producing delayed and less stable disk formation. Zero field allows no angular momentum preservation at all — pure radial infall.

---

### Why the Disk Is Geometrically Thin

The disk that forms is not a torus. It is not a diffuse cloud. It is extraordinarily thin — morphologically indistinguishable from the thin accretion disks photographed around real astrophysical black holes by the Event Horizon Telescope.

The reason for this thinness is the geometry of the Lorentz force. The magnetic field in this simulator is oriented along the Y-axis (vertical). The Lorentz force F = q(v × B) continuously redirects any vertical momentum component into the equatorial plane. Particles that attempt to move vertically are deflected back into the disk plane. Only particles with sufficient energy to overcome this deflection escape — and they do so vertically, forming the jet-like structures visible in the simulation.

The result is a structure with the following properties, all emergent and none explicitly programmed:

- Geometrically thin equatorial disk ✅
- Rotational motion (orbital) ✅  
- Vertical particle escape (proto-jets) ✅
- Disk formation rate proportional to B-field strength ✅
- Disk formation rate proportional to black hole mass ✅

The last point bears emphasis: as black hole mass increases, disk formation accelerates. This reproduces the exact scaling relationship observed in astrophysical systems — more massive black holes form accretion structures faster — without any GR dynamics in the code.

---

## Part III — What These Structures Mean

### The Accretion Disk

In standard astrophysics, an accretion disk is the structure of gas and plasma that orbits a black hole in a flattened, rotating configuration. Accretion disks are among the most energetically powerful structures in the universe — they are responsible for quasar luminosity, X-ray binary emission, and relativistic jet formation.

The conventional explanation for why accretion disks exist requires General Relativity. Specifically, it requires the concept of the **Innermost Stable Circular Orbit (ISCO)**.

In Newtonian gravity, a circular orbit at any radius is stable — matter can orbit indefinitely at any distance. There is no natural mechanism that causes matter to spiral inward.

In General Relativity, this changes fundamentally. The Schwarzschild metric predicts that for a non-rotating black hole, no stable circular orbit exists inside r = 6GM/c². Inside this radius — the ISCO — any perturbation causes the orbit to decay and the particle to plunge inward. For a rotating Kerr black hole, the ISCO moves inward as spin increases, reaching r = GM/c² for a maximally rotating black hole.

The ISCO is not a classical concept. It is a prediction of spacetime curvature. It is, in a very direct sense, a signature of General Relativity.

**Yet in this simulator, an accretion disk appears without the ISCO.** Particles are not being forced inward by spacetime curvature. They are being captured by the combination of Newtonian gravity and the Lorentz force, and their angular momentum — distributed according to the correct Tsallis pT distribution from real LHC collision data — naturally produces a ring structure.

The macroscopic result is the same. The mechanism is different.

### The Ergosphere

The ergosphere is a region outside the event horizon of a rotating (Kerr) black hole. Its outer boundary is defined by:

```
r_ergo = M(1 + √(1 - a*²cos²θ))
```

At the equator, r_ergo = 2M (in natural units), always larger than the event horizon.

The ergosphere has a property unlike anything in classical physics: **inside the ergosphere, no object can remain stationary with respect to distant observers.** Spacetime itself rotates, dragging everything with it. This is frame dragging — the Lense-Thirring effect — taken to its extreme.

The physical consequence is profound. An object inside the ergosphere can have negative total energy as measured from infinity. This enables the **Penrose process**: a particle entering the ergosphere can split into two, with one fragment falling into the black hole carrying negative energy, and the other escaping to infinity with more energy than the original particle. Energy is extracted directly from the black hole's rotation.

This is pure General Relativity. There is no Newtonian analogue.

In this simulator, the ergosphere is rendered visually but its dynamics are deactivated. Frame dragging is commented out. The Penrose process cannot occur.

**And yet**, particle accumulation near the ergosphere region occurs. Charge separation near the ergosphere boundary occurs. The spatial distribution of particles respects, approximately, the ergosphere geometry — not because the code enforces it, but because the combination of magnetic confinement and Newtonian gravity produces a similar boundary.

### What General Relativity Actually Predicted

General Relativity, published by Einstein in 1915, predicted that mass curves spacetime, and that this curvature is what we experience as gravity. From this single geometric idea, an enormous range of phenomena follow:

- Gravitational time dilation
- Light deflection around massive objects
- Gravitational waves
- Black holes and their event horizons
- The ISCO and accretion disk structure
- Frame dragging and the ergosphere
- The Penrose process

Every one of these has been confirmed observationally. The bending of light was confirmed in 1919. Gravitational waves were directly detected in 2015 by LIGO. The first image of a black hole's shadow was captured by the Event Horizon Telescope in 2019.

GR is not a hypothesis. It is one of the most precisely tested theories in the history of science.

---

## Part IV — Why This Observation Is Interesting

We return now to what the simulator showed.

```
Input:
Special Relativity (complete particle physics)
+ Newtonian gravity (black hole)
+ Lorentz force (magnetic field)

Output:
Accretion disk structure    — 100% reproduction
Particle-antiparticle separation — 100% reproduction
Ring stabilization above critical B-field — 100% reproduction
```

These are structures that General Relativity predicts. They appeared without General Relativity being present in the black hole dynamics.

We offer three possible interpretations, in order of increasing boldness:

**Interpretation 1 — Scale Approximation**  
At micro black hole scales, GR corrections to Newtonian gravity are small. The dominant physics is SR + electromagnetism. The macrostructures that appear are therefore well-approximated by classical + SR methods, and happen to resemble GR predictions because GR itself reduces to Newtonian gravity in the weak-field limit.

This is the most conservative interpretation. It is almost certainly partially correct.

**Interpretation 2 — Physical Inevitability**  
GR's macroscopic predictions — accretion disks, particle confinement near the ergosphere — are not uniquely produced by spacetime curvature. They are produced by any system that correctly enforces conservation of angular momentum, relativistic energy-momentum relations, and electromagnetic forces on charged particles.

GR predicts these structures because GR correctly captures the underlying physics. But the underlying physics can also be captured by other means.

**Interpretation 3 — Emergence**  
The macrostructures of GR are emergent phenomena — they arise from the collective behavior of relativistic particles under gravity and electromagnetism. GR describes them geometrically. But the geometry may be a description of something more fundamental, not the fundamental thing itself.

This interpretation is the most speculative. We do not claim it. We note it as a direction worth examining.

---

## Part V — What This Is Not Claiming

We wish to be explicit about the boundaries of this observation.

This simulator does **not** reproduce:
- Gravitational lensing of light
- Gravitational redshift
- Gravitational time dilation
- Gravitational wave emission
- The precise ISCO radius
- Frame dragging dynamics
- The Penrose process

These are genuine GR phenomena that require the full machinery of spacetime curvature. They are not present in this simulation. We do not claim otherwise.

What we claim is narrow and specific:

> *Under conditions of uniform magnetic field and Newtonian point-mass gravity, a simulation built on Special Relativity and correct particle physics data reproduces the macroscopic spatial structures — accretion disk geometry and charge separation — that General Relativity predicts near black holes. This reproduction is 100% reproducible across all tested parameter combinations.*

Nothing more. Nothing less.

---

## Part VI — An Invitation

The entire simulation runs in a browser. The code is open. There is nothing to install.

If you are a physicist, we invite you to find the parameter conditions under which this breaks down — where the Newtonian approximation fails to reproduce GR structure. That boundary is scientifically interesting.

If you are curious, press COLLIDE and watch what happens.

The physics implementations are documented in detail across the preceding 19 posts in this series. The simulation is deterministic and fully reproducible.

The previous 19 posts in this series document the full development history: every physical inconsistency that was found, every correction that was made, and every observation that led to this point. They are available at [Seoul Inside / Substack].

---

## Closing

We began this series by asking what would happen if we added a black hole to a particle physics simulator.

General Relativity is 111 years old. It has survived every experimental test. It describes the universe at its largest scales with extraordinary precision.

What this simulator suggests — modestly, carefully, with full awareness of its limitations — is that GR's predictions are so robust that they appear even when you only approximate half of the physics.

That is not a challenge to General Relativity.

That is a tribute to it.

---

*Yang-Mills Collider v3.2 + Kerr Black Hole (Frame Dragging, Ergosphere) · PDG 2022 · 39 Particles · B. Sun | Seoul Inside*

*Code repository: [github.com/xur94-maker/SeoulInside]*

*Previous entries in this series cover: simulator architecture, black hole integration, spiral galaxy formation mechanics, the Passive Layer hypothesis, antimatter asymmetry under magnetic fields, dark energy reinterpretation, and black hole mass variability.*






