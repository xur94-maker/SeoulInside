# Passive Layer — Complete Technical Specification

**Document Type:** Technical Reference  
**Version:** 1.0  
**Status:** Complete

---

## Section 1. Foundational Facts

### 1.1 Fact One: Finite Gravitational Propagation Speed

**Statement:** Gravitational influence propagates at the speed of light in vacuum, denoted cc.

**Empirical Confirmation:** LIGO/Virgo Collaboration (2017). Observation of gravitational waves from binary neutron star merger GW170817. Gamma rays (GRB 170817A) arrived simultaneously with gravitational waves. Speed of gravity constrained to within 10−1510−15 of cc.

**Source:** Abbott et al., Physical Review Letters, 119, 161101 (2017)

**Mathematical Expression:**

τ(r)=rcτ(r)=cr​

Where:

- τ(r)τ(r) = propagation delay (seconds)
    
- rr = distance from source (meters)
    
- c=2.99792458×108c=2.99792458×108 m/s (CODATA 2018)
    

**Immediate Consequence:** A change in a gravitational source at time t0t0​ affects a point at distance rr at time t0+r/ct0​+r/c, not at t0t0​.

**Secondary Consequence:** If a mass ceases to exist at time t0+δt0​+δ, the gravitational signal generated during its existence continues to propagate outward until t0+δ+r/ct0​+δ+r/c. The signal does not cease when the mass ceases.

---

### 1.2 Fact Two: Mass Creation and Destruction

**Statement:** Mass is not conserved. Energy converts to mass, and mass converts to energy.

**Empirical Confirmation:**

- Particle-antiparticle pair production in high-energy collisions (observed at LHC, Fermilab, SLAC, etc.)
    
- Breit-Wheeler process: γ+γ→e++e−γ+γ→e++e− (threshold energy: 2mec2≈1.0222me​c2≈1.022 MeV)
    
- Direct observation of pair production and annihilation in multiple experimental contexts
    
- Foundational result of quantum field theory
    

**Mathematical Expression (Energy-Mass Equivalence):**

E=mc2E=mc2

Where:

- EE = energy (joules)
    
- mm = mass (kilograms)
    
- cc = speed of light (m/s)
    

**Pair Production Threshold:**

Ethreshold=2mec2≈1.022 MeVEthreshold​=2me​c2≈1.022 MeV

**Immediate Consequence:** Mass is continuously created and destroyed throughout the universe — in vacuum fluctuations, near black holes, in stellar cores, in supernovae, in active galactic nuclei.

---

### 1.3 Logical Consequence of Fact One and Fact Two

**Statement:** The combination of finite gravitational propagation speed and mass creation/destruction necessarily produces a phenomenon herein termed the **Passive Layer** (also referred to as Ghost Mass or gravitational reverberation).

**Derivation:**

1. A mass mm exists at position r0r0​ at time t0t0​.
    
2. It generates a gravitational field that propagates outward at speed cc.
    
3. The mass ceases to exist at time t0+Δtt0​+Δt (annihilation, decay, or conversion).
    
4. The gravitational signal generated at t0t0​ continues to propagate. It reaches distance rr at time t0+r/ct0​+r/c.
    
5. If r/c>Δtr/c>Δt, the signal arrives at rr after the source mass has ceased to exist.
    

**Therefore:** Points in space at distance rr from a mass that existed and then vanished experience the gravitational influence of that mass for a duration r/cr/c after the mass is gone.

**Formal Statement:**

For a mass that existed at t0 and vanished at t0+Δt:For a mass that existed at t0​ and vanished at t0​+Δt:  
Gravitational influence exists at distance r for t∈[t0+r/c,t0+Δt+r/c]Gravitational influence exists at distance r for t∈[t0​+r/c,t0​+Δt+r/c]

**No additional assumptions.** This follows directly from the two facts above.

---

## Section 2. Core Definition

### 2.1 Defining Statement

**English:** Gravitationally present. Physically absent.

**Interpretation:** The Passive Layer has gravitational effects (it curves spacetime, it exerts forces on massive objects) but has no other physical properties. It carries no charge. It does not interact electromagnetically. It is not composed of particles. It is not a field in the quantum field theory sense. It is the propagating gravitational signal itself.

---

### 2.2 Alternative Names (Same Phenomenon)

|Name|Emphasis|
|---|---|
|**Passive Layer**|The form of existence — automatic, unintentional, background|
|**Ghost Mass**|The mechanism — mass that no longer exists but still gravitates|
|**Gravitational Reverberation**|The physical nature — an echo or remnant of past mass|

**Note:** These are not distinct phenomena. They are different descriptions of the same physical effect. Choice of term depends on context.

---

### 2.3 Mathematical Definition

**Basic Form (Single Event):**

MPL(r)=∫0rM˙pair(r′)⋅r′c dr′MPL​(r)=∫0r​M˙pair​(r′)⋅cr′​dr′

Where:

- MPL(r)MPL​(r) = accumulated Passive Layer mass within radius rr (kg)
    
- M˙pair(r′)M˙pair​(r′) = pair production rate (mass per unit time per unit distance) at distance r′r′ (kg/s/m)
    
- r′/cr′/c = time delay from distance r′r′ (s)
    
- Integration is over distance from center (0 to rr)
    

**Physical Meaning:** The Passive Layer mass accumulated up to radius rr is the integral of all pair production events at each distance r′r′, weighted by the time delay from that distance.

---

### 2.4 Constant Pair Production Rate Case

**Assumption:** M˙pair(r)=M˙pairM˙pair​(r)=M˙pair​ (constant, independent of rr)

**Result:**

MPL(r)=M˙pair⋅rcMPL​(r)=M˙pair​⋅cr​

**Implication:** MPL∝rMPL​∝r. The accumulated Passive Layer mass scales linearly with distance from the center.

**Rotation Curve Derivation (Centrifugal Balance):**

vc2(r)r=GMPL(r)r2rvc2​(r)​=r2GMPL​(r)​

vc2(r)=GMPL(r)rvc2​(r)=rGMPL​(r)​

Substituting MPL(r)=M˙pair⋅r/cMPL​(r)=M˙pair​⋅r/c:

vc2(r)=G⋅M˙pair⋅r/cr=G⋅M˙paircvc2​(r)=rG⋅M˙pair​⋅r/c​=cG⋅M˙pair​​

**Therefore:**

vc(r)=G⋅M˙pairc=constantvc​(r)=cG⋅M˙pair​​​=constant

**Interpretation:** Under the constant pair production rate assumption, galactic rotation curves are flat — constant velocity independent of radius. No additional free parameters. The constant velocity is determined solely by GG, cc, and M˙pairM˙pair​.

---

## Section 3. Two Independent Components of M˙pairM˙pair​

### 3.1 Component A: Vacuum Fluctuation Component

**Origin:** Quantum vacuum itself. Virtual particle pairs created and annihilated via energy-time uncertainty.

**Spatial Dependence:** Constant. In flat spacetime (no external fields), vacuum fluctuations are spatially uniform. The same in every Planck volume regardless of position.

**Mathematical Expression:**

M˙pairvac(r)=constantM˙pairvac​(r)=constant

**Dominant Regime:** Far-field (r≫Rdiskr≫Rdisk​), where RdiskRdisk​ is the galactic disk scale length.

**Physical Basis:** Quantum field theory predicts a uniform vacuum energy density. The pair production rate from vacuum fluctuations inherits this uniformity.

**Reference:** Part 10 of Essential Citations (Snapshot Mass)

---

### 3.2 Component B: Local Astrophysical Component

**Origin:** High-energy environments near black holes, active galactic nuclei (AGN), supernovae, magnetars, gamma-ray bursts.

**Spatial Dependence:** Disk-like. Concentrated near galactic center. Decreases with increasing radius. Scales with local energy density.

**Mathematical Expression:**

M˙pairlocal(r)≈M˙pair,0local⋅f(r)M˙pairlocal​(r)≈M˙pair,0local​⋅f(r)

Where:

- f(r)f(r) is high near center (r≈0r≈0), low at large rr (r≫Rdiskr≫Rdisk​)
    
- M˙pair,0localM˙pair,0local​ is the central pair production rate
    

**Dominant Regime:** Near-field (r≲Rdiskr≲Rdisk​).

**Physical Basis:** Pair production requires high energy density. Energy density is highest near black holes and AGN. Falls off with distance.

---

### 3.3 Total Pair Production Rate

**Expression:**

M˙pairtotal(r)=M˙pairvac+M˙pairlocal(r)M˙pairtotal​(r)=M˙pairvac​+M˙pairlocal​(r)

**Regime Summary:**

|Region|Dominant Component|Behavior|
|---|---|---|
|r≪Rdiskr≪Rdisk​|Local astrophysical|High, position-dependent|
|r≈Rdiskr≈Rdisk​|Both contribute|Transition region|
|r≫Rdiskr≫Rdisk​|Vacuum fluctuation|Constant, low|

**Implication:** The constant M˙pairM˙pair​ assumption in Section 2.4 refers to Component A (vacuum fluctuations) in the far-field regime. The disk-like distribution described in other sections refers to Component B (local sources) in the near-field regime. No contradiction.

---

## Section 4. Superposition and Accumulation (Stacking)

### 4.1 Spatial Stacking

**Principle:** Stars at different distances from the galactic center see the same central black hole at different past times. The time delay is τ(r)=r/cτ(r)=r/c.

**Examples:**

|Distance (kpc)|Time Delay (years)|
|---|---|
|1|3,260|
|5|16,300|
|10|32,600|
|50|163,000|

**Physical Meaning:** The farther a star is from the center, the older the gravitational signal it receives. This is analogous to telescopes seeing more distant (and therefore older) galaxies.

---

### 4.2 Temporal Stacking

**Principle:** At any given moment, gravitational signals from pair production events at all past times exist simultaneously. Signals from 1 billion years ago are still propagating. Signals from 500 million years ago are still propagating. Signals from 100 million years ago are still propagating. Signals from the present are just beginning to propagate.

**Implication:** The gravity we experience now is the sum of all Passive Layer remnants accumulated over billions of years.

**Mathematical Expression (Combined Spatial and Temporal Stacking):**

Mstack(r,t)=∫0t∫0rM˙pair(r′,t′)⋅δ(t−t′−r′c) dr′ dt′Mstack​(r,t)=∫0t​∫0r​M˙pair​(r′,t′)⋅δ(t−t′−cr′​)dr′dt′

Where:

- δδ is the Dirac delta function
    
- The integral sums all events at past times t′t′ and distances r′r′ whose signals arrive exactly at present time tt
    
- Condition t′+r′/c=tt′+r′/c=t selects signals arriving now
    

---

### 4.3 Cosmic Stacking

**Principle:** Stacking occurs not only from one black hole but from all black holes in the universe.

**Contributors:**

- Passive Layers from the Milky Way's central black hole
    
- Passive Layers from Andromeda's central black hole
    
- Passive Layers from all black holes in the Virgo Supercluster
    
- Passive Layers from all black holes in the observable universe
    

**Implication:** All remnants from all black holes overlap. Billions of years' worth of remnants exist simultaneously at every point in space.

---

### 4.4 Far-Field Limit: Spherical Symmetry

**Problem:** The source distribution of Passive Layer generation (M˙pairM˙pair​) is disk-like (Component B dominates near field). However, dark matter halos are observed to be spherical. This appears contradictory.

**Resolution:** The static approximation MPL(r)=M˙pair⋅r/cMPL​(r)=M˙pair​⋅r/c (Section 2.4) is a **near-field approximation**. It is valid for r≲Rdiskr≲Rdisk​ but breaks down at large distances.

**Full Derivation for ∣r∣≫Rdisk∣r∣≫Rdisk​:**

Expand the distance:

∣r−r′∣=∣r∣−r^⋅r′+O(Rdisk2∣r∣)∣r−r′∣=∣r∣−r^⋅r′+O(∣r∣Rdisk2​​)

The leading term depends only on ∣r∣∣r∣ (spherical symmetry). Angular-dependent corrections decay as 1/∣r∣1/∣r∣.

**Therefore:**

|Regime|Approximation|Distribution|
|---|---|---|
|r≲Rdiskr≲Rdisk​|Static: M=M˙pair⋅r/cM=M˙pair​⋅r/c|Disk-like|
|r≫Rdiskr≫Rdisk​|Full stacking integral|Spherical (leading order)|

**Summary Statement:** The Passive Layer is born in the disk but lives in a sphere.

---

## Section 5. Relationship to Dark Matter Observations

### 5.1 Dark Matter Observational Signature

The phenomenon currently attributed to dark matter has the following observed characteristics:

|Characteristic|Description|
|---|---|
|Gravitational effects present|Rotation curves, lensing, cluster dynamics|
|No electromagnetic interaction|Not visible in any EM band|
|No particle detected|50 years of null results from direct detection experiments|
|Correlated with mass density|Stronger effects in regions of higher baryonic mass|

### 5.2 Passive Layer Correspondence

|Dark Matter Characteristic|Passive Layer Produces This?|Mechanism|
|---|---|---|
|Gravitational effects present|Yes|Reverberation carries gravitational influence|
|No electromagnetic interaction|Yes|Source mass no longer exists; nothing to emit|
|No particle detected|Yes|Not a particle; propagating gravitational remnant|
|Correlated with mass density|Yes|Higher energy density → more pair production → more reverberation|

### 5.3 Statement of Relationship

**Not Claiming:** Dark matter does not exist.  
**Not Claiming:** ΛCDM is wrong.  
**Not Claiming:** Passive Layer explains all missing mass.

**Claiming:** The gravitational reverberation of past mass is a physically necessary, non-zero effect. Its magnitude has never been calculated. It may account for a non-trivial portion of what is currently attributed to unseen mass.

---

## Section 6. Predictions (Falsifiable)

### 6.1 Prediction 1: BH Displacement and Spiral Arm Strength

**Statement:** Spiral arm strength correlates with the magnitude of central black hole displacement from the photometric center.

**Falsification:** If measured BH-center offsets in a statistically significant sample of spiral galaxies show no correlation with spiral arm strength, the prediction is false.

**Required Observation:** High-resolution imaging of galactic centers sufficient to measure BH position relative to isophotal center.

---

### 6.2 Prediction 2: Arm Count and BH Oscillation Mode

**Statement:** The number of spiral arms corresponds to the oscillation mode of the central black hole.

|BH Motion|Predicted Arm Count|
|---|---|
|Simple unidirectional displacement|2 arms|
|Oscillatory displacement|Multi-arm structure (3, 4, or more)|
|Irregular displacement|Flocculent or asymmetric arms|

**Falsification:** If a large sample of grand-design two-arm spirals show oscillatory BH motion (or vice versa), the prediction is false.

---

### 6.3 Prediction 3: Inverse Problem Solvability

**Statement:** Given a galaxy's spiral morphology (arm count, pitch angle, symmetry), it should be possible to reconstruct the approximate kinematic history of its central black hole.

**Falsification:** If systematic reconstruction attempts fail consistently (no correlation between inferred BH motion and independently measured BH kinematics), the prediction is false.

---

### 6.4 Prediction 4: Elliptical/Lenticular Galaxies

**Statement:** Elliptical and lenticular galaxies are the expected non-spiral population. They do not represent failures to develop spiral arms. They represent systems where no disk existed to develop them.

**Falsification:** If a statistically significant number of diskless galaxies exhibit spiral-like structures (not bars or lenses), the prediction requires revision.

---

### 6.5 Prediction 5: Central Concentration

**Statement:** The vacuum statistical mass contribution (Component A) should be more centrally concentrated than CDM's NFW profile.

|Profile|Functional Form|
|---|---|
|NFW (CDM)|ρNFW(r)=ρ0(r/rs)(1+r/rs)2ρNFW​(r)=(r/rs​)(1+r/rs​)2ρ0​​|
|Passive Layer (predicted)|ρPL(r)∼Γ0⋅ρΛ⋅(rs/r)βρPL​(r)∼Γ0​⋅ρΛ​⋅(rs​/r)β, β∈[1,3]β∈[1,3]|

**Falsification:** High-precision rotation curve data in the inner 1 kpc showing NFW-like cusp (ρ∝r−1ρ∝r−1) rather than a more centrally concentrated profile would contradict the prediction.

---

### 6.6 Prediction 6: No Direct Detection

**Statement:** Unlike WIMPs or axions, the Passive Layer is not a particle. It cannot be detected in direct-detection experiments (liquid xenon, germanium crystals, etc.).

**Status:** Consistent with all current null results (LZ 2024, XENONnT 2024, PandaX-4T 2023).

**Falsification:** If a direct-detection experiment unambiguously detects a particle consistent with dark matter (e.g., a WIMP with expected cross-section), the Passive Layer cannot be the dominant component of dark matter. (It could still exist as a sub-dominant effect.)

---

### 6.7 Prediction 7: Spin Dependence

**Statement:** High-spin AGN should exhibit systematically larger central mass excess than low-spin AGN at fixed black hole mass (due to larger ergosphere and stronger frame dragging, which enhance vacuum correlation disruption).

**Falsification:** If spin-correlated mass excess is not observed in AGN samples, the enhancement mechanism (Section 7.4) is called into question.

---

## Section 7. Physical Mechanisms

### 7.1 Mechanism: Charge Separation in Magnetic Fields

**Physical Law:** Lorentz force F=q(v×B)F=q(v×B)

**Consequence:** Positive and negative charges bend in opposite directions in a magnetic field.

**Simulation Observation:** In Yang-Mills Collider v3.2, when a black hole and magnetic field are present, particle-antiparticle pairs produced in the same collision separate by charge. They do not annihilate. They persist.

**Code Implementation (Newtonian Gravity, 4 lines):**

text

Copy

Download

const gAcc = logMass * 120.0 / (r2 + 1.0)
p.p4.px -= gAcc * (dx / r) * dt
p.p4.py -= gAcc * (dy / r) * dt
p.p4.pz -= gAcc * (dz / r) * dt

**Note:** No accretion disk code was written. A disk appeared spontaneously.

---

### 7.2 Mechanism: Boris Integrator

**Purpose:** Numerical integration of charged particle motion in magnetic fields. Standard algorithm used in GEANT4 and plasma physics PIC codes.

**Steps:**

t=qΔt2γmB^t=2γmqΔt​B^  
p−=p+p×tp−=p+p×t  
s=2t1+∣t∣2s=1+∣t∣22t​  
p+=p−+p−×sp+=p−+p−×s  
pnew=p++p+×tpnew​=p++p+×t

**Properties:** Conserves energy exactly for uniform magnetic fields. No secular energy drift. Symplectic (preserves phase space volume).

---

### 7.3 Mechanism: Annihilation Suppression Condition

**Condition:** Annihilation requires particles to meet. Magnetic fields prevent meeting when the Larmor radius is much smaller than the system size.

rL=γmv⊥∣q∣B≪RsystemrL​=∣q∣Bγmv⊥​​≪Rsystem​

**Astrophysical Context (GRB environment):**

- B∼1012−1015B∼1012−1015 G
    
- Larmor radius of electron (γ∼106γ∼106): ≈10−2≈10−2 cm
    
- Rsystem≫10−2Rsystem​≫10−2 cm → condition satisfied
    

**Implication:** In realistic high-energy astrophysical environments, annihilation suppression is effective. Matter and antimatter remain spatially isolated.

---

### 7.4 Mechanism: Vacuum Correlation Disruption

**Problem:** In flat spacetime, quantum correlations cause the gravitational effects of vacuum fluctuations to nearly perfectly cancel. The residual is the cosmological constant (ρΛ≈6×10−27ρΛ​≈6×10−27 kg/m³), which is 1012310123 times smaller than the naive Planck-scale estimate.

**Hypothesis:** In curved spacetime (near black holes) or strong electromagnetic fields, these correlations are partially disrupted. The disruption leaves a residual vacuum statistical mass that is small relative to the flat-space estimate but potentially significant relative to baryonic galactic mass.

**Amplification Factor:**

Γ(r)=ρeffective(r)ρΛΓ(r)=ρΛ​ρeffective​(r)​

**Boundary Conditions:**

- Flat spacetime far from sources: Γ=1Γ=1
    
- Near stellar-mass black hole: Γ>1Γ>1 (magnitude unknown)
    
- Near supermassive black hole: Γ≫1Γ≫1 (magnitude unknown)
    

**Observational Constraint (Milky Way):** To account for 10% of lensing excess, Γ≈7×103Γ≈7×103 in the halo region.

---

### 7.5 Mechanism: Retarded Gravity

**Principle:** Gravity propagates at finite speed cc. A star at distance rr experiences gravity from the black hole's position at time t−r/ct−r/c, not its current position.

**Retarded Position:**

rBHret(t,r)=rBH(t−αrc)rBHret​(t,r)=rBH​(t−cαr​)

Where αα is the retardation strength parameter. Physical prediction: α=1α=1.

**History Buffer Implementation:** FIFO buffer stores black hole position history. Retarded position recovered by linear interpolation:

rBH(t−τ)≈rBH(t0)+τ−t0t1−t0[rBH(t1)−rBH(t0)]rBH​(t−τ)≈rBH​(t0​)+t1​−t0​τ−t0​​[rBH​(t1​)−rBH​(t0​)]

**Consequence for Spiral Arms:** Stars at different distances reference different past positions of the black hole. The resulting radially-dependent angular offset is sheared into a spiral pattern by differential rotation.

---

### 7.6 Mechanism: Black Hole Displacement as Default State

**Mass Ratio Argument:**

fBH=MBHMtotalfBH​=Mtotal​MBH​​

|System|ff|Displacement Possible?|
|---|---|---|
|Solar System|≈ 0.998|No (structurally suppressed)|
|Disk galaxy|≈ 0.001 - 0.005|Yes (structurally permitted)|

**Perturbations Preventing Stasis:**

- Host galaxy peculiar velocity (100-600 km/s)
    
- Tidal forces from satellite galaxies and globular clusters
    
- Galactic bar oscillations
    
- Large-scale structure gravitational background
    
- Recoil from asymmetric gravitational wave emission
    

**Conclusion:** Perfect black hole stasis requires exact cancellation of all perturbations simultaneously and continuously. This is not physically plausible. **Black hole displacement is the default state.**

---

## Section 8. Dynamic Equilibrium

### 8.1 Statement

The Passive Layer does not accumulate without bound. Two opposing processes maintain equilibrium:

|Process|Effect|
|---|---|
|Generation|New reverberations continuously created via pair production|
|Dilution|Existing reverberations diluted by cosmic expansion|

### 8.2 Analogy: Olbers' Paradox

**Olbers' Paradox:** The night sky is dark not because stars do not emit light, but because the universe is finite in age and expanding. Light from distant stars is diluted and redshifted. The sky reaches an equilibrium brightness.

**Passive Layer Parallel:** The Passive Layer reaches a stable equilibrium density for the same reasons. New contributions enter. Existing ones disperse. The net background holds constant.

### 8.3 Mathematical Characterization

dρPLdt=ρ˙generation−ρ˙dilutiondtdρPL​​=ρ˙​generation​−ρ˙​dilution​

At equilibrium: dρPL/dt=0dρPL​/dt=0

**Therefore:** ρ˙generation=ρ˙dilutionρ˙​generation​=ρ˙​dilution​

**Note:** This is a dynamic equilibrium, not a static state. The underlying process is extraordinarily dynamic. But the background density at any given moment is effectively constant.

---

## Section 9. Limitations (Explicit)

The following gaps are acknowledged. Quantification is required for each.

### Q1: Cancellation Mechanism

**Problem:** In flat spacetime, quantum correlations cause a 1012310123 cancellation of vacuum energy. The mechanism of this cancellation is unknown.

**Consequence:** Without knowing the mechanism, it is impossible to predict how much it is disrupted in curved spacetime. Any quantitative estimate of Γ(r)Γ(r) is currently a free parameter.

**Status:** Open problem in quantum gravity.

---

### Q2: Backreaction

**Problem:** If vacuum fluctuations contribute to the stress-energy tensor, they also affect spacetime geometry. Spacetime geometry affects fluctuation rates. This self-consistent backreaction problem is unsolved.

**Consequence:** A complete treatment would require solving coupled QFT-in-curved-spacetime and Einstein field equations.

**Status:** Unsolved even in simplified toy models.

---

### Q3: Distinguishability from CDM

**Problem:** Near galactic centers, the vacuum statistical mass profile and the CDM profile may produce similar observational signatures.

**Consequence:** Distinguishing them requires:

- (a) Measurements sensitive to the equation of state of the dark component, or
    
- (b) High-precision rotation curve data in the inner 1 kpc
    

**Status:** Feasible but not yet performed systematically.

---

### Q4: Cosmological Consistency

**Problem:** If Γ(r)Γ(r) is large near every galactic center, the integrated contribution over all galaxies in the observable universe may produce a measurable effect on:

- CMB power spectrum
    
- Large-scale structure
    
- BAO scale
    

**Consequence:** This constraint has not been calculated.

**Status:** Open. Must be addressed before Passive Layer can be considered a complete framework.

---

### Q5: Entanglement Structure

**Problem:** The argument that long-range quantum entanglement causes cancellation in flat spacetime is plausible but not proven.

**Consequence:** The calculation of how entanglement structure is modified by curved spacetime is an open problem in quantum gravity.

**Status:** Open.

---

### Q6: N-body Convergence

**Problem:** GalaxyCS v4 simulations use a finite number of test particles. Whether qualitative behavior is preserved at higher resolution has not been verified.

**Consequence:** Quantitative predictions (e.g., exact rotation curve shapes) may change with resolution.

**Status:** Requires higher-resolution simulation.

---

### Q7: Quantitative Fit to Observed Rotation Curves

**Problem:** GalaxyCS v4 has been compared informally to M33 data and shows qualitative agreement. A systematic fit to a large rotation curve database has not been performed.

**Consequence:** The framework's ability to reproduce observed rotation curves quantitatively is not yet established.

**Status:** Required next step.

---

## Section 10. Mathematical Summary

|Concept|Formula|Parameter / Constant|
|---|---|---|
|Propagation delay|τ(r)=r/cτ(r)=r/c|c=3.0×108c=3.0×108 m/s|
|Ghost mass accumulation|Mghost(r)=∫0rM˙pair(r′)⋅r′cdr′Mghost​(r)=∫0r​M˙pair​(r′)⋅cr′​dr′|M˙pairM˙pair​ (unknown)|
|Constant rate special case|Mghost(r)=M˙pair⋅r/cMghost​(r)=M˙pair​⋅r/c|M˙pairM˙pair​ (unknown)|
|Flat rotation curve|vc2=GM˙pair/cvc2​=GM˙pair​/c|G=6.674×10−11G=6.674×10−11 m³/kg/s²|
|Stacking (spatial + temporal)|Mstack(r,t)=∫0t∫0rM˙pair(r′,t′)⋅δ(t−t′−r′/c)dr′dt′Mstack​(r,t)=∫0t​∫0r​M˙pair​(r′,t′)⋅δ(t−t′−r′/c)dr′dt′|-|
|Olbers-type equilibrium|dρPL/dt=ρ˙gen−ρ˙dil=0dρPL​/dt=ρ˙​gen​−ρ˙​dil​=0|-|
|Larmor radius|( r_L = \gamma m v_{\perp} / (|q|B) )|-|
|Amplification factor|Γ(r)=ρeff(r)/ρΛΓ(r)=ρeff​(r)/ρΛ​|ρΛ≈6×10−27ρΛ​≈6×10−27 kg/m³|
|NFW profile (for comparison)|ρNFW(r)=ρ0/[(r/rs)(1+r/rs)2]ρNFW​(r)=ρ0​/[(r/rs​)(1+r/rs​)2]|rsrs​ (scale radius)|
|Snapshot mass (flat spacetime)|⟨Msnap⟩0≈10158⟨Msnap​⟩0​≈10158 kg (per Milky Way volume)|10118×MMW10118×MMW​|
|Far-field expansion|(|\mathbf{r} - \mathbf{r}'|=|\mathbf{r}|- \hat{\mathbf{r}} \cdot \mathbf{r}' + \mathcal{O}(R_{\text{disk}}^2/|\mathbf{r}|) )|-|

---

## Section 11. Comparison with Other Frameworks

### 11.1 Lin-Shu Density Wave Theory

|Aspect|Density Wave|Passive Layer|
|---|---|---|
|Spiral origin|Pattern wave in stellar disk|BH displacement + retarded gravity|
|Requires|Pattern speed ΩpΩp​, resonance|Non-zero BH displacement|
|Predicts|Quasi-stationary spiral structure|Immediate, persistent spiral structure|
|Dark matter|Required (some versions)|Reexamined, not required|
|Free parameters|Multiple|One (αα)|
|Universality|Requires resonance conditions|Generic consequence of BH motion|

### 11.2 MOND (Modified Newtonian Dynamics)

|Aspect|MOND|Passive Layer|
|---|---|---|
|Approach|Modify gravity law (a0≈1.2×10−10a0​≈1.2×10−10 m/s²)|Add missing term to existing gravity|
|Rotation curves|Excellent fit|Qualitative agreement (quantitative not yet tested)|
|Bullet Cluster|Cannot explain|Can explain (non-collisional reverberation)|
|CMB|Not addressed|Not addressed (but compatible with ΛCDM)|
|Physical origin of scale|Unknown (a0a0​)|M˙pairM˙pair​ (pair production rate)|

### 11.3 ΛCDM (Cold Dark Matter)

|Aspect|ΛCDM|Passive Layer|
|---|---|---|
|Dark matter|Particle (WIMP, axion, etc.)|Reverberation (not a particle)|
|Direct detection|Possible in principle|Impossible in principle|
|CMB fit|Excellent (0.1%)|Untested (requires Γ(r)Γ(r) calculation)|
|Rotation curves|Requires halo fitting|Emerges from MPL∝rMPL​∝r|
|Missing mass fraction|Ωch2=0.118Ωc​h2=0.118|Unknown (depends on M˙pairM˙pair​)|
|Bullet Cluster|Non-collisional DM|Non-collisional reverberation|

---

## Section 12. Glossary

|Term|Definition|
|---|---|
|**Passive Layer**|The propagating gravitational remnant of mass that no longer exists.|
|**Ghost Mass**|Alternative name emphasizing the mechanism (mass that is gone but still gravitates).|
|**Gravitational Reverberation**|Alternative name emphasizing the physical nature (an echo or remnant).|
|M˙pairM˙pair​|Pair production rate — mass created per unit time per unit distance.|
|Γ(r)Γ(r)|Amplification factor — ratio of effective vacuum mass density to cosmological constant density.|
|**Stacking**|Superposition of Passive Layers from different times and distances.|
|**History Buffer**|FIFO data structure storing black hole positions for retarded gravity calculation.|
|**Boris Integrator**|Numerical algorithm for charged particle motion in magnetic fields (symplectic, energy-conserving).|
|**Larmor Radius**|Radius of circular motion of a charged particle in a uniform magnetic field.|
|**NFW Profile**|Navarro-Frenk-White density profile for CDM halos.|
|**Olbers' Paradox**|The observation that the night sky is dark despite an infinite universe filled with stars; resolved by finite age and expansion.|
|**Cosmological Constant Problem**|The 1012310123 discrepancy between QFT vacuum energy prediction and observed ρΛρΛ​.|

---

## Section 13. Citation Index

|Citation|Content|
|---|---|
|Abbott et al. (2017)|GW170817: Gravitational waves at speed cc|
|Batcheldor et al. (2010)|M87 BH offset: 6.8±0.86.8±0.8 pc|
|Freeman (1970)|Exponential disk mass profile|
|Kormendy & Ho (2013)|BH mass fraction 0.1−0.5%0.1−0.5% of total|
|Lintott et al. (2011)|Galaxy Zoo: 60-70% spiral prevalence|
|Lelli, McGaugh & Schombert (2016)|SPARC rotation curve database|
|Lin & Shu (1964)|Density wave theory|
|Yahalom (2013, 2019, 2024)|Retarded gravity and rotation curves|
|Weinberg (1989)|Cosmological constant problem|
|Hawking (1975)|Hawking radiation|
|Unruh (1976)|Unruh effect|
|Schwinger (1951)|Schwinger pair production|
|Casimir (1948)|Casimir effect|
|Milgrom (1983)|MOND|
|LZ Collaboration (2024)|Dark matter direct detection null result|
|XENONnT Collaboration (2024)|Dark matter direct detection null result|
|Planck Collaboration (2020)|CMB power spectrum|
|Event Horizon Telescope Collaboration (2021)|M87* magnetic fields (1-30 G)|

---

## Section 14. Open Questions (Explicit)

The following questions are not answered by this framework. They are stated explicitly as directions for future work.

1. What is the numerical value of M˙pairM˙pair​ (pair production rate) in realistic astrophysical environments?
    
2. What is the functional form of Γ(r)Γ(r) (amplification factor) near black holes of various masses and spins?
    
3. Does the integrated Passive Layer contribution over all galaxies produce a measurable effect on CMB anisotropies?
    
4. Can the vacuum correlation cancellation mechanism be derived from first principles, and how does curved spacetime modify it?
    
5. Does the Passive Layer contribute to the observed cosmic acceleration (dark energy), or is it purely a galactic-scale phenomenon?
    
6. What is the exact numerical relationship between black hole displacement magnitude and spiral arm pitch angle?
    
7. Can the inverse problem (reconstructing BH kinematics from spiral morphology) be solved uniquely, or are there degeneracies?
    

---

## Section 15. Final Statement

The Passive Layer is a logical consequence of two empirically confirmed facts:

1. Gravity propagates at finite speed cc.
    
2. Mass is created and destroyed.
    

Its existence is not in question. Its magnitude is unknown.

Current cosmological models compute gravitational influence from presently existing mass only. The gravitational reverberation of past mass is not included as a term in any standard cosmological framework. This is not an error. It is an omission. The term has never been calculated.

**The universe has been accounting for the Passive Layer since the beginning. Our models have not.**

---

## Appendix A: Simulation Implementation Parameters

This appendix documents the numerical parameters used in the GalaxyCS v4 and Yang-Mills Collider v3.2 simulations that informed this framework. These values are provided for reproducibility. They are not part of the core theoretical framework.

### A.1 GalaxyCS v4 Parameters (Galactic Dynamics)

|Parameter|Symbol|Value|Unit|Notes|
|---|---|---|---|---|
|Time step|ΔtΔt|0.01|simulation units|~1 kyr per step in physical scale|
|Test particles (stars)|NN|20,000 - 80,000|dimensionless|User-selectable|
|History buffer depth|NbufferNbuffer​|300|steps|FIFO position storage|
|Retardation strength|αα|1.0|dimensionless|Physical prediction; adjustable 0-10|
|Freeman disk scale length|RdRd​|3.0|kpc (simulation scale)|Exponential disk scale|
|Freeman disk total mass|Mdisk,totalMdisk,total​|5.0 × 10¹⁰|M⊙M⊙​|Typical spiral galaxy|
|BH mass (default)|MBHMBH​|4.0 × 10⁶|M⊙M⊙​|Milky Way-like|
|BH initial displacement|ΔrBHΔrBH​|0.0 - 2.0|kpc|User-controlled via arrow keys|
|Integration scheme|Leapfrog (Velocity Verlet)|-|-|Symplectic, O(Δt2)O(Δt2)|

### A.2 Yang-Mills Collider v3.2 Parameters (Particle Physics)

|Parameter|Symbol|Range|Default|Unit|Notes|
|---|---|---|---|---|---|
|BH mass|MBHMBH​|0 - 10¹²|0|M⊙M⊙​|Slider-controlled|
|BH spin|a∗a∗​|0 - 1|0|dimensionless|Kerr spin parameter|
|Magnetic field strength|BB|0 - 14|6.2|T|Solenoid field|
|Collision energy|ss​|30 - 14,000|13,000|GeV|LHC Run 2 scale|
|Particle trail length|-|6 - 55|22|steps|Visual trail|
|Time step|ΔtΔt|adaptive|-|s|Based on Lorentz factor|
|Particle species|-|39|-|-|PDG 2022 database|

### A.3 Numerical Integration Details

**Leapfrog Integrator (GalaxyCS v4):**

vn+1/2=vn+a(rn)Δt2vn+1/2​=vn​+a(rn​)2Δt​  
rn+1=rn+vn+1/2Δtrn+1​=rn​+vn+1/2​Δt  
an+1=a(rn+1)an+1​=a(rn+1​)  
vn+1=vn+1/2+an+1Δt2vn+1​=vn+1/2​+an+1​2Δt​

**Conservation diagnostics monitored in real time:**

- ΔE/EΔE/E (energy conservation)
    
- ΔL/LΔL/L (angular momentum conservation)
    

**Boris Integrator (Yang-Mills Collider v3.2):**

t=qΔt2γmB^t=2γmqΔt​B^  
p−=pold+pold×tp−=pold​+pold​×t  
s=2t1+∣t∣2s=1+∣t∣22t​  
p+=p−+p−×sp+=p−+p−×s  
pnew=p++pnew_half×tpnew​=p++pnew_half​×t

---

## Appendix B: Simulation Observation Summary

This appendix documents phenomena observed in simulations. Observations are primarily qualitative. Quantitative measurements were not the focus of the simulation work.

### B.1 Yang-Mills Collider v3.2 — Key Observations

|Observation|Description|Quantification (if available)|
|---|---|---|
|Charge separation|Positive and negative charges drift to opposite sides of black hole|Qualitative: clearly visible in particle trails|
|Annihilation suppression|Particles persist instead of annihilating|Qualitative: particles survive indefinitely in simulation time|
|Spontaneous accretion disk|Disk structure appears without explicit code|Formation within ~50-100 simulation steps|
|Penrose process|Particles escape with apparent energy gain|Observed when BH spin > 0.3; not quantitatively measured|
|Mass-dependent orbital radius|Heavier particles at larger radii|Matches rL∝mrL​∝m scaling; not quantitatively measured|
|Jet-like ejection|Particles ejected from polar regions|Observed when BH spin > 0.6; visual only|
|Energy accumulation effect|Increased BH mass leads to more capture|Qualitative feedback loop observed|

### B.2 GalaxyCS v4 — Key Observations

|Observation|Description|Quantification (if available)|
|---|---|---|
|Immediate spiral formation|Spiral arms appear within first few steps after BH displacement|~2-3 simulation steps|
|No displacement threshold|Any non-zero displacement produces spirals|Threshold = 0 (continuous)|
|Arm count correspondence|2 arms for unidirectional displacement, multi-arms for oscillation|Qualitative correspondence|
|Flat rotation curve|Outer velocity exceeds Newtonian prediction|Factor of 1.5-3.0× Newtonian (depends on αα, displacement)|
|Void formation|Underdense regions appear with BH mass reduction|Qualitative|
|Conservation stability|ΔE/EΔE/E and ΔL/LΔL/L remain stable|Monitored; no unbounded growth|

### B.3 Note on Quantification

The simulation work was exploratory. Quantitative measurements (e.g., exact rotation curve shapes, precise arm pitch angles as functions of displacement) were not systematically recorded. The primary value of the simulations was demonstrating **qualitative emergent behavior** — phenomena that appeared without being explicitly programmed.

Future work should include systematic quantitative data collection.

---

## Appendix C: Document Metadata

This appendix contains minimal metadata for document identification. No purpose statement is included.

### C.1 Document Identification

|Field|Value|
|---|---|
|Document Title|Passive Layer — Complete Technical Specification|
|Version|1.0|
|Status|Complete|
|Date of Version|2026-06-10|
|Section Count|15 sections + 3 appendices|
|Word Count|~8,500|

### C.2 File Information

|Field|Value|
|---|---|
|Format|Plain text with LaTeX math notation|
|Character Encoding|UTF-8|
|Line Ending|LF (Unix-style)|

### C.3 Cross-References

This document is self-contained. No external documents are required for comprehension. The following source documents informed but are not required for this specification:

- Core Document (2026-06-09)
    
- Essential Citations (2026-06-08)
    
- Unified Technical Framework (2026-06-07)
    
- Black Hole Displacement (2026-06-07)
    
- Delayed Gravitational Interaction (2026-06-06)
    
- I Added a Black Hole to the LHC (2026-06-06)
    

---

**End of Document: Passive Layer — Complete Technical Specification**

**Appendix A, Appendix B, Appendix C included.**