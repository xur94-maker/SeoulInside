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
