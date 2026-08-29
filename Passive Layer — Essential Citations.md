Passive Layer — Essential Citations PASSIVE LAYER & PASSIVE LAYERS STACKING: COMPLETE DEFINITION AND UNDERSTANDING B. Sun | Seoul Inside Jun 08, 2026

Note to the reader: This document is a structured record of observed phenomena across multiple physical scales. It does not claim to have solved any Millennium Problem or to have disproven any existing theory. It is presented as a complementary framework: this effect exists, it is non-zero, and its magnitude under extreme astrophysical conditions has not been adequately quantified.

Throughout this document, mathematical expressions are given in four parallel notations (Unicode, LaTeX, Mathematica, Python). For readers without a physics background, each formula is followed by an explanation in plain language.

The document is very long. But that is intentional — it is detailed enough that no further explanation is needed. If you encounter a part you do not understand, do not stop. Keep reading. Most concepts will connect naturally as you go forward.

TABLE OF CONTENTS

PART 0. Before You Begin: Three Facts You Need to Know

PART 1. Background: Dark Matter and ΛCDM’s Remaining Questions

PART 2. Ghost Mass: The Gravity of Mass That No Longer Exists

PART 3. Charge Separation: Why Particles Do Not Annihilate

PART 4. Why the Pair Production Rate Can Be Constant (Mechanism 2)

PART 5. Passive Layer: The Form of Existence

PART 6. Passive Layers Stacking: Superposition and Accumulation

PART 7. Delayed Gravity and the History Buffer

PART 8. Black Hole Displacement: Why It Moves

PART 9. Spiral Structure as Default State: Inverting the Question

PART 10. Snapshot Mass: The Weight of the Vacuum

PART 11. The Same Pattern Found Across Scales

PART 12. Falsifiable Predictions

PART 13. Limitations (Stated Honestly)

PART 14. Comparison with Existing Frameworks

PART 15. The Three Independent Mechanisms (Summary)

PART 16. Conclusion APPENDIX A. Recommended Reading Order (Links) APPENDIX B. Complete Collection of Citations and Source URLs

Simulators:

https://xur94-maker.github.io/SeoulInside/Galaxy_2.html

https://xur94-maker.github.io/SeoulInside/LHC_kerr_2.html

https://xur94-maker.github.io/SeoulInside/LHC_kerr_1.html

https://xur94-maker.github.io/SeoulInside/Galaxy_1.html

PART 0. Before You Begin: Three Facts You Need to Know

To understand this framework, you need to know only three things. All three are empirically verified facts. No new physics is required.

Fact 1: Gravity Propagates at the Speed of Light

Just as light takes 8 minutes to travel from the Sun to Earth, changes in the Sun’s gravity also take 8 minutes to reach Earth. Gravity is not instantaneous.

This was confirmed in 2017 when the LIGO/Virgo collaboration observed a neutron star merger (GW170817) and detected gravitational waves and gamma rays arriving simultaneously. The speed of gravity was constrained to within 10^-15 of the speed of light c (Abbott et al. 2017, Physical Review Letters, 119, 161101).

Formula: tau(r) = r / c

Unicode : τ(r) = r / c LaTeX : \tau(r) = \frac{r}{c} Mathematica : tau[r_] := r / c Python : def tau(r, c): return r / c

Meaning: A gravitational signal from distance r arrives after time r/c.

Fact 2: Energy Can Become Mass

Einstein’s famous equation E = mc^2 means that in high-energy environments, energy can convert into particle-antiparticle pairs.

This is directly observed at the LHC (Large Hadron Collider). Two high-energy photons collide and produce an electron-positron pair (Breit & Wheeler 1934, Physical Review, 46, 1087).

Formula (pair production threshold energy): E_threshold = 2 m_e c^2 ≈ 1.022 MeV

Unicode : E_threshold = 2 × m_e × c²

LaTeX : E_{\text{threshold}} = 2m_e c^2

Mathematica : Ethreshold = 2 * me * c^2

Python : from scipy.constants import m_e, c; Ethreshold = 2 * m_e * c**2

Meaning: With enough energy, light can transform into matter (particles).

Fact 3: Galactic Disks Rotate Differentially

Stars near the galactic center rotate faster; stars farther out rotate slower. This is the same as our Solar System: Mercury orbits the Sun in 88 days, Neptune in 165 years.

This is a universal observational fact of galactic dynamics (Freeman 1970, ApJ, 160, 811).

Formula (idealized Keplerian rotation): v(r) ∝ r^(-1/2)

Unicode : v(r) ∝ r^(-1/2) LaTeX : v(r) \propto r^{-1/2} Mathematica : v[r_] ~ 1/Sqrt[r] Python : v = np.sqrt(G * M / r)

Meaning: Under Newtonian dynamics alone, rotation velocity should decrease with distance. But observations show it does not. This is why dark matter was introduced.

Now, let us combine these three verified facts and see what happens.

PART 1. Background: Dark Matter and ΛCDM’s Remaining Questions

The standard ΛCDM model is extraordinarily successful at cosmological scales. It reproduces the cosmic microwave background (CMB) temperature power spectrum (Planck Collaboration 2020), baryon acoustic oscillations (BAO, Eisenstein et al. 2005), and large-scale structure (Springel et al. 2005) with remarkable precision.

This document does not dispute ΛCDM’s cosmological success.

However, ΛCDM faces unresolved issues at galactic scales:

Direct detection failure: All dark matter direct detection experiments — LZ 2024, XENONnT 2024, PandaX-4T 2023 — have produced null results for 50 years.

Cusp-core problem: CDM simulations predict density diverging as ρ ∝ r^(-1) (cusp) at galactic centers, but observations show nearly constant density cores (de Blok 2010).

Missing satellites problem: CDM predicts about 200 satellite galaxies around the Milky Way, but only about 50 are observed (Bullock & Boylan-Kolchin 2017).

Cosmological constant problem: The vacuum energy density predicted by quantum field theory (~10^96 kg/m³) and the observed value (~10^-27 kg/m³) differ by a factor of 10^123 (Weinberg 1989).

This document observes that two well-established phenomena — the finite propagation speed of gravity and the statistical behavior of quantum vacuum fluctuations — may have combined implications at galactic scales that have not been fully explored.

PART 2. Ghost Mass: The Gravity of Mass That No Longer Exists

Imagine: somewhere in the universe, two high-energy photons collide and produce an electron-positron pair (pair production). These particles exist briefly, then meet and annihilate. The mass disappears.

But here is the problem. Gravity propagates at the speed of light. The gravitational signal generated when the mass existed continues to travel through space for time r/c after the mass is gone. Stars experience the gravity of mass that no longer exists.

This is Ghost Mass.

Formula: M_ghost(r) = integral from 0 to r of [ M_dot_pair(r’) x (r’/c) ] dr’

Unicode : M_ghost(r) = ∫₀ʳ Ṁ_pair(r’) × (r’/c) dr’

LaTeX : M_{\text{ghost}}(r) = \int_0^r \dot{M}{\text{pair}}(r’) \cdot \frac{r’}{c} , dr’

Mathematica : Mghost[r] := Integrate[MdotPair[rp] * rp/c, {rp, 0, r}]

Python : def M_ghost(r, Mdot_pair_func, c=299792458): from scipy.integrate import quad result, _ = quad(lambda rp: Mdot_pair_func(rp) * rp / c, 0, r) return result

Meaning: The Ghost Mass accumulated up to radius r is the integral of the pair production rate at each distance r’, multiplied by the time delay r’/c from that distance.

When the pair production rate is constant: M_ghost(r) = Ṁ_pair · r/c → M_ghost ∝ r

Unicode : M_ghost(r) ∝ r LaTeX : M_{\text{ghost}}(r) \propto r

This is enormous in its implications.

Meaning for rotation curves (centrifugal balance): v_c²(r) = G · M_ghost(r) / r = G · Ṁ_pair / c = constant

Unicode : v_c² = G × M_ghost / r = G × Ṁ_pair / c

LaTeX : v_c^2(r) = \frac{G , M_{\text{ghost}}(r)}{r} = \frac{G , \dot{M}_{\text{pair}}}{c}

Mathematica : vcSquared = G * Mghost[r] / r

Python : def vc_squared(Mdot_pair, G, c): return G * Mdot_pair / c

If M_ghost ∝ r, then rotation velocity becomes constant regardless of distance. This explains flat rotation curves without dark matter, with no additional free parameters.

But this explanation is missing one thing: “Why is the pair production rate constant?” The answer comes in Parts 3 and 4.

2.5 Two Distinct Components of Ṁ_pair

The pair production rate Ṁ_pair is not a single monolithic quantity. It has two independent physical origins that must be distinguished. Failure to distinguish them leads to apparent contradictions that are not actual contradictions.

Component A: Vacuum Fluctuation Component (Universal, Constant)

This component originates from the quantum vacuum itself. In flat spacetime, vacuum fluctuations are spatially uniform — the same in every cubic Planck-length of space regardless of position.

Unicode : Ṁ_pair^vac(r) = constant (independent of r)

LaTeX : \dot{M}{\text{pair}}^{\text{vac}}(r) = \text{constant} \quad (\text{independent of } r)

Mathematica : MdotPairVac[r] := constant

Python : def Mdot_pair_vac(r): return constant # independent of r

Meaning: This component does not depend on distance from the galactic center. It is the same everywhere in the universe (to leading order). It is the source of the constant Ṁ_pair assumption in Part 2.

Dominant regime: Far-field (r >> R_disk) — see Section 6.4 Part reference: Part 10 (Snapshot Mass)

Component B: Local Astrophysical Component (Disk-like, Position-Dependent)

This component originates from high-energy environments around black holes, active galactic nuclei (AGN), supernovae, and other localized sources. It scales with local energy density.

Unicode : Ṁ_pair^local(r) ≈ (Ṁ_pair^local)0 · f(r), where f(r) is high near center, low at large r

LaTeX : \dot{M}{\text{pair}}^{\text{local}}(r) \approx \dot{M}{\text{pair},0}^{\text{local}} \cdot f(r), \quad f(r) \text{ high near center, low at large } r

Mathematica : MdotPairLocal[r] := MdotPairLocal0 * f[r] (* f[r] decreasing with r *) Python : def Mdot_pair_local(r, M0, f): return M0 * f(r) # f(r) decreases with r

Meaning: This component is concentrated in the galactic disk. It dominates the near-field region (r ≲ R_disk) and is responsible for the disk-like source distribution described in Part 4.

Dominant regime: Near-field (r ≲ R_disk) Part reference: Part 4 (Why the Pair Production Rate Can Be Constant)

Comparison of the two components:

Vacuum fluctuation component: Origin: Quantum vacuum | r-dependence: Constant | Dominant regime: Far-field (r >> R_disk) | Part reference: Part 10

Local astrophysical component: Origin: BHs, AGN, supernovae | r-dependence: Disk-like (decreases with r) | Dominant regime: Near-field (r ≲ R_disk) | Part reference: Part 4

Therefore, there is no contradiction. The constant Ṁ_pair assumption in Part 2 refers to Component A (vacuum fluctuations). The disk-like distribution described in Part 4 refers to Component B (local astrophysical sources). Both exist simultaneously and dominate in different spatial regimes.

The total pair production rate is the sum of both components:

Unicode : Ṁ_pair^total(r) = Ṁ_pair^vac + Ṁ_pair^local(r)

LaTeX : \dot{M}{\text{pair}}^{\text{total}}(r) = \dot{M}{\text{pair}}^{\text{vac}} + \dot{M}{\text{pair}}^{\text{local}}(r)

Mathematica : MdotPairTotal[r] := MdotPairVac + MdotPairLocal[r]

Python : def Mdot_pair_total(r): return Mdot_pair_vac + Mdot_pair_local(r)

Meaning: At small r, the local component dominates. At large r, the vacuum component becomes relatively more important. The transition between these regimes is described in Section 6.4 (Far-Field Limit).

PART 3. Charge Separation: Why Particles Do Not Annihilate

Black holes are surrounded by powerful magnetic fields. EHT observations of M87* measured magnetic fields of 1–30 Gauss at the photon ring (EHT MWL Science Working Group, 2021). Moving inward, the magnetic field increases sharply, estimated at 10⁴–10⁵ Gauss near the ISCO.

In the LHC simulator (Yang-Mills Collider v3.2), when such an environment was created, something unexpected happened.

Particles and antiparticles separated. They did not annihilate. They persisted as mass.

The reason is simple. The Lorentz force bends positive and negative charges in opposite directions.

Formula (Lorentz force): F = q(v × B)

Unicode : F = q(v × B)

LaTeX : \mathbf{F} = q(\mathbf{v} \times \mathbf{B})

Mathematica : F = q * Cross[v, B]

Python : F = q * np.cross(v, B)

Black hole gravity pulls both toward the same point, but they arrive from opposite sides. They never meet. They do not annihilate.

Crucially, this phenomenon appeared without being programmed.

“I did not build an accretion disk. One appeared.”

The Boris integrator used in the simulator is the standard algorithm in GEANT4 and plasma physics PIC codes, accurately computing charged particle motion in magnetic fields.

Formula (Boris integrator steps):

Unicode : t = (q·Δt/2)/(γm)·B̂, p⁻ = p + p×t, s = 2t/(1+|t|²), p⁺ = p⁻ + p⁻×s

LaTeX : \mathbf{t} = \frac{q\Delta t}{2\gamma m}\hat{\mathbf{B}},\quad \mathbf{p}^- = \mathbf{p} + \mathbf{p}\times\mathbf{t},\quad \mathbf{s} = \frac{2\mathbf{t}}{1+|\mathbf{t}|^2},\quad \mathbf{p}^+ = \mathbf{p}^- + \mathbf{p}^-\times\mathbf{s}

Mathematica : tVec = (qdt/(2gammam)) * Bhat; pMinus = p + Cross[p, tVec]; sVec = 2tVec/(1+Norm[tVec]^2); pPlus = pMinus + Cross[pMinus, sVec]

Python : def boris_step(p, q, m, gamma, B, dt): t = (q * dt / (2 * gamma * m)) * B / np.linalg.norm(B) p_minus = p + np.cross(p, t) s = 2 * t / (1 + np.linalg.norm(t)**2) p_plus = p_minus + np.cross(p_minus, s) return p_plus

Meaning: The direction of rotation depends on the sign of the charge. Positive charges rotate one way, negative charges the opposite way.

Newtonian gravity code (just 4 lines) implementing black hole gravity:

const gAcc = logMass * 120.0 / (r2 + 1.0) p.p4.px -= gAcc * (dx / r) * dt p.p4.py -= gAcc * (dy / r) * dt p.p4.pz -= gAcc * (dz / r) * dt

Without GR, without MHD, without fluid dynamics, without a single line of “build an accretion disk” code, a disk appeared spontaneously.

Thus: pair production occurs continuously around black holes, the magnetic field separates the particles and suppresses annihilation, and mass persists.

PART 4. Why the Pair Production Rate Can Be Constant (Mechanism 2)

The Ghost Mass formula assumes a constant pair production rate Ṁ_pair. But why would Ṁ_pair be constant?

This section explains the physical mechanism that maintains a constant Ṁ_pair.

4.0 Clarification: Which Component Are We Discussing?

Before answering “why the pair production rate can be constant,” a critical clarification is necessary.

Section 2.5 distinguished two independent components of Ṁ_pair:

Component A: Vacuum fluctuation component (Ṁ_pair^vac) r-dependence: Constant This Part (Part 4) discusses this component? No — discussed in Part 10 Type of constancy: Spatial constancy (independent of r)

Component B: Local astrophysical component (Ṁ_pair^local) r-dependence: Disk-like (decreases with r) This Part (Part 4) discusses this component? Yes — this section Type of constancy: Temporal constancy (steady state over time at fixed r)

Then why is this section titled “Why the Pair Production Rate Can Be Constant”?

Because the local astrophysical component, despite being disk-like in its spatial distribution, can maintain a temporally constant production rate at each radius. This is a different kind of constancy — constancy in time, not in space.

Formula (temporal constancy at fixed r):

Unicode : ∂Ṁ_pair^local(r, t)/∂t ≈ 0 (steady state) LaTeX : \frac{\partial \dot{M}_{\text{pair}}^{\text{local}}(r, t)}{\partial t} \approx 0 \quad \text{(steady state)} Mathematica : D[MdotPairLocal[r, t], t] == 0 (* steady state *) Python : # In steady state, Mdot_pair_local(r, t) is approximately constant in time

Meaning: For a fixed distance r from the galactic center, the local pair production rate fluctuates around a stable mean value over long timescales (millions to billions of years). This is the constancy referred to in the Ghost Mass derivation — not spatial uniformity, but temporal steadiness.

The two types of constancy summarized:

Spatial constancy (Component A): Meaning: Ṁ_pair independent of r | Applies to: Vacuum fluctuation component Physical origin: Quantum vacuum is uniform | Part reference: Part 10

Temporal constancy (Component B): Meaning: Ṁ_pair stable over time at fixed r | Applies to: Local astrophysical component Physical origin: Steady-state high-energy environments | Part reference: Part 4

Therefore, there is no contradiction. The word “constant” means different things in different contexts:

Part 2 uses “constant” to mean spatially constant (independent of r), referring to the vacuum fluctuation component.

Part 4 uses “constant” to mean temporally constant (steady over time), referring to the local astrophysical component.

The following subsections (4.1-4.6) explain the physical mechanisms that maintain temporal constancy of the local astrophysical component, despite the extreme and variable conditions near black holes.

4.1 The Ultra-High-Energy Environment

The environment around a black hole is incomparably more extreme than the LHC:

LHC (humanity’s strongest): B = 8.3 T, energy scale 13,000 GeV

Magnetar: B ~ 10^11 T (10^10 times!), energy scale ~10^20 GeV

AGN black hole: B ~ 10³–10⁵(~10⁶) G , energy scale ~10^24 GeV and above

In this environment, the following chain of pair production → isolation → accumulation can occur:

γ + γ → e⁺ + e⁻ (or heavier particle-antiparticle pairs)

B >> B_critical → annihilation suppressed (r_L << R_system)

Matter + antimatter → spatial isolation → gravitational contribution maintained

4.2 Larmor Radius and Mass Separation

In a magnetic field B, a charged particle traces a circular path. The radius of this circular motion is called the Larmor radius:

r_L = γmv⊥ / (|q|B) = p⊥ / (|q|B)

The angular frequency is: ω_c = |q|B / (γm)

Key insight: r_L ∝ m (proportional to mass!)

For particles with the same energy and the same charge:

Electron (m=0.511 MeV): smallest radius → innermost orbit

Pion (m=140 MeV): intermediate radius

Proton (m=938 MeV): larger radius → outer orbit

W boson (m=80,377 MeV): very large radius → outermost orbit

This is the physical cause of the mass-dependent orbital radius separation observed in the simulation.

Pair production rate is not uniform. It scales with local energy density — highest near the black hole, lowest in voids. The stack thickness varies accordingly.

4.3 Annihilation Suppression Condition

For annihilation (e⁺ + e⁻ → γ + γ) to occur, the two particles must meet. The magnetic field can prevent this when:

r_L = γmc / (eB) << R_system (the Larmor radius is much smaller than the system size)

Considering a real GRB environment:

B ~ 10^12 - 10^15 G

Larmor radius of an electron (γ~10^6) ≈ 10^-2 cm

This is far smaller than the system size (R_system). Therefore, matter and antimatter can remain spatially isolated for a long time.

4.4 The Ṁ_pair Term in the Mass Rate-of-Change Equation

The conventional black hole mass growth equation considers only external accretion:

dM/dt = Ṁ_in - Ṁ_out - Ṗ_Hawking/c²

However, the pair production mechanism suggests an additional term:

dM/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking/c²

where Ṁ_pair is the independent mass contribution rate from pair production.

This term has not been explicitly treated in the existing literature to the author’s knowledge.

4.5 Three Possible Fates for Isolated Matter and Antimatter

When the magnetic field weakens, annihilation occurs → energy released → gravity decreases

Absorbed by the black hole → incorporated as mass → gravity increases

Ejected as a jet → moves to the galactic outskirts → gravity redistributed

Any of these pathways creates gravitational variability in the black hole. This is the core of Mechanism 2.

4.6 Connection to the Early Universe Supermassive Black Hole Problem

One of the most serious unsolved problems in current astronomy: How could supermassive black holes with masses of about 10 billion solar masses (~10^9 M☉) have grown so rapidly in the early universe (z > 6, within the first billion years of cosmic history)?

Under the Eddington luminosity limit, reaching this mass through external accretion alone requires the Eddington time (approximately 450 million years):

t_Eddington = M / Ṁ_Edd = 450 Myr (for radiative efficiency η=0.1)

Yet the observed quasars reached this mass in far less time. External accretion alone is insufficient.

Applying the logic of Mechanism 2 to the early universe opens up a new possibility:

The environment around black holes in the early universe was far more extreme than today

Higher energy density → higher pair-production rate

Stronger magnetic fields → more efficient annihilation suppression

There may have been conditions where the Ṁ_pair term could dominate over Ṁ_in

If this mechanism operated, the problem of rapid supermassive black hole growth in the early universe would be naturally resolved.

PART 5. Passive Layer: The Form of Existence

The gravitational remnants generated in this way accumulate as background across all of space. Unintentional. Uncontrollable. Always operating.

This is the Passive Layer.

Formula (Passive Layer accumulated mass): M_PL(r) = integral from 0 to r of [ Ṁ_pair(r’) × (r’/c) ] dr’

Unicode : M_PL(r) = ∫₀ʳ Ṁ_pair(r’) × (r’/c) dr’

LaTeX : M_{\text{PL}}(r) = \int_0^r \dot{M}{\text{pair}}(r’) \cdot \frac{r’}{c} , dr’

Mathematica : Mpl[r] := Integrate[MdotPair[rp] * rp/c, {rp, 0, r}]

Python : def M_PL(r, Mdot_pair_func, c=299792458): from scipy.integrate import quad result, _ = quad(lambda rp: Mdot_pair_func(rp) * rp / c, 0, r) return result

The formula is identical to Ghost Mass. Because they are different languages describing the same phenomenon.

Four Core Properties:

Unintentional: No agent intends to create it. The simulator had no “build a disk” code, yet a disk appeared.

Uncontrollable: Cannot be turned off. As long as pair production occurs and magnetic fields exist, this phenomenon continues. There is no “off” button.

Automatic: Once conditions are met, it activates automatically. Like a passive skill in games — always on without pressing a button.

Background: Not concentrated at specific locations. Spread throughout space as background. Unlike dark matter, which is hypothesized to be “clumped somewhere,” the Passive Layer is spread everywhere.

The name Passive Layer emerged from the distinction between mechanism and existence. Ghost Mass describes how the effect arises — the gravitational remnant of annihilated mass. Passive Layer describes what that remnant is: a background that operates without intention, without control, always on. The mechanism has a name. The form of existence has a name.

Relationship between Ghost Mass and Passive Layer:

Ghost Mass describes the mechanism (”how it arises”)

Passive Layer describes the form of existence (”what it is”)

Two faces of the same phenomenon. Not substitutes, but complements.

PART 6. Passive Layers Stacking: Superposition and Accumulation

Now we come to the most important concept.

A single Passive Layer is the remnant from a single time and a single distance. But the universe contains billions of black holes, and each black hole continuously produces Passive Layers. And all these layers overlap and accumulate.

This is Passive Layers Stacking.

Formula (combination of spatial and temporal stacking):

Unicode : M_stack(r,t) = ∫₀ᵗ ∫₀ʳ Ṁ_pair(r’,t’) × δ(t - t’ - r’/c) dr’ dt’

LaTeX : M_{\text{stack}}(r,t) = \int_0^t \int_0^r \dot{M}{\text{pair}}(r’,t’) \cdot \delta!\left(t - t’ - \frac{r’}{c}\right) dr’, dt’

Mathematica : Mstack[r, t_] := Integrate[MdotPair[rp, tp] * DiracDelta[t - tp - rp/c], {tp, 0, t}, {rp, 0, r}]

Python : def M_stack(r, t, Mdot_pair_func, c=299792458): from scipy.integrate import dblquad def integrand(rp, tp): return Mdot_pair_func(rp, tp) * (1 if abs(t - tp - rp/c) < 1e-6 else 0) result, _ = dblquad(integrand, 0, t, 0, r) return result

Meaning: The total mass accumulated at this moment (t) up to radius r is the sum of all pair production events from all past times (t’) and all distances (r’) whose signals are arriving exactly now (t’ + r’/c = t).

This can be understood in three dimensions.

6.1 Spatial Stacking

Each star at distance r sees the black hole’s position from time r/c ago.

τ(r) = r/c

Specific examples:

r = 1 kpc → layer from 3,260 years ago

r = 5 kpc → layer from 16,300 years ago

r = 10 kpc → layer from 32,600 years ago

r = 50 kpc → layer from 163,000 years ago

The farther you look, the older the layer you see. This is exactly the same principle as telescopes seeing more distant (and therefore older) galaxies.

6.2 Temporal Stacking

At this very moment, remnants from all past times exist simultaneously.

Remnant from 1 billion years ago → still propagating

Remnant from 500 million years ago → still propagating

Remnant from 100 million years ago → still propagating

Remnant from the present → just starting

The implication is enormous. The gravity we experience now is the sum of all remnants accumulated over billions of years.

6.3 Cosmic Stacking

We are not considering just one black hole in one galaxy.

The scale of stacking is total. Passive Layers from the Milky Way’s central black hole, from Andromeda’s, from every black hole in the Virgo Supercluster, from every black hole in the observable universe — all of them overlap. All remnants from all black holes exist simultaneously, right now. This is Passive Layers Stacking — the spatial and temporal superposition of Passive Layers from different distances and epochs. The entire universe moves upon the echoes of its own past mass activity.

Effect at galactic scale: Passive Layers Stacking → M_ghost ∝ r → flat rotation curve → appears like dark matter

Possible effect at cosmic scale (not yet validated): Passive Layers Stacking → cosmic background mass density → influence on cosmic expansion → possible connection to dark energy

6.4 The Far-Field Limit: Why the Passive Layer Becomes Spherical at Large Radii

The static approximation M_ghost(r) = Ṁ_pair · r/c from Part 2 is a near-field limit. It is valid for r ≲ R_disk but breaks down at large distances.

For |r| >> R_disk, the full stacking integral must be used. Expanding the distance:

Unicode : |r - r’| = |r| - (r̂·r’) + O(R_disk²/|r|)

LaTeX : |\mathbf{r} - \mathbf{r}’| = |\mathbf{r}| - \hat{\mathbf{r}} \cdot \mathbf{r}’ + \mathcal{O}(R_{\text{disk}}^2/|\mathbf{r}|)

Mathematica : Norm[r - rp] == Norm[r] - (r/Norm[r]).rp + O[Rdisk^2/Norm[r]]

Python : r_norm = np.linalg.norm(r); r_diff = r_norm - np.dot(r/r_norm, rp) # for r_norm >> R_disk

Meaning: The leading term depends only on |r| (spherical symmetry), with angular-dependent corrections that decay as 1/|r|.

Therefore:

Near-field (r ≲ R_disk): Static approximation M = Ṁ_pair · r/c → Disk-like distribution

Far-field (r >> R_disk): Full stacking integral → Spherical distribution (to leading order)

Implication for dark matter: At large galactic radii — precisely where dark matter halos are inferred — the Passive Layer distribution is effectively spherical. This resolves the apparent tension between the disk-like generation mechanism and the spherical dark matter halo.

The Passive Layer is born in the disk but lives in a sphere.

PART 7. Delayed Gravity and the History Buffer

To simulate this phenomenon, the “History Buffer” was created.

The black hole’s position is stored in a FIFO (First-In-First-Out) buffer of 300 steps. Each star retrieves the past position corresponding to its distance from this buffer.

Formula (retarded position):

Unicode : r_BH_ret(t, r) = r_BH(t - α·r/c) LaTeX : \mathbf{r}{\text{BH}}^{\text{ret}}(t, r) = \mathbf{r}{\text{BH}}!\left(t - \frac{\alpha r}{c}\right) Mathematica : rBHret[t_, r_] := rBH[t - alpha * r / c] Python : def retarded_position(bh_history, t_now, r, alpha=1.0, c=299792458): delay = alpha * r / c t_target = t_now - delay for i, (t, pos) in enumerate(bh_history): if t <= t_target: t0, r0 = bh_history[i] t1, r1 = bh_history[i+1] frac = (t_target - t0) / (t1 - t0) return r0 + frac * (r1 - r0) return bh_history[0][1]

Here, α is the retardation strength parameter. The physical prediction is α = 1.

Formula (linear interpolation):

Unicode : r_BH(t-τ) ≈ r_BH(t₀) + (τ-t₀)/(t₁-t₀) × (r_BH(t₁) - r_BH(t₀)) LaTeX : \mathbf{r}{\text{BH}}(t-\tau) \approx \mathbf{r}{\text{BH}}(t_0) + \frac{\tau - t_0}{t_1 - t_0}\left[\mathbf{r}{\text{BH}}(t_1) - \mathbf{r}{\text{BH}}(t_0)\right]

Crucial point: This buffer is not a numerical convenience for simulation. It is a direct consequence of the finite propagation speed of gravity. The universe naturally maintains this buffer.

This interpolation creates spiral arms. Each star falls toward a different past position, and in a differentially rotating disk, the angular difference maps onto a spiral pattern.

Why the history buffer is a physical necessity:

Gravity propagates at finite speed c (empirically confirmed)

Any influence propagating at finite speed naturally leaves a “record” (logical consequence)

Without that record, certain phenomena (spiral arms) cannot occur (simulation proof)

Therefore, the universe maintains that record (the buffer) (conclusion)

PART 8. Black Hole Displacement: Why It Moves

But one question remains. Why does the black hole move? Why can’t it be fixed at the galactic center?

In a galaxy, the black hole’s mass fraction is only 0.1-0.5% (Kormendy & Ho 2013, Annual Review of Astronomy and Astrophysics, 51, 511).

This is completely different from the Solar System, where the Sun comprises 99.8% of the total mass.

Formula (mass fraction): f_BH = M_BH / M_total

Unicode : f_BH = M_BH / M_total, f_sun ≈ 0.998, f_BH^galaxy ≈ 0.001-0.005 LaTeX : f_{\text{BH}} = \frac{M_{\text{BH}}}{M_{\text{total}}},\quad f_{\odot} \approx 0.998,\quad f_{\text{BH}}^{\text{galaxy}} \approx 0.001\text{-}0.005 Mathematica : fBH = MBH / Mtotal Python : def mass_fraction(M_BH, M_total): return M_BH / M_total f_sun = mass_fraction(1.989e30, 2.0e30) # ≈ 0.998 f_MW_BH = mass_fraction(4e6 * 1.989e30, 1e12 * 1.989e30) # ≈ 4e-6

The perturbations that cause the black hole to move are countless:

The host galaxy’s peculiar velocity (100-600 km/s)

Tidal forces from satellite galaxies and globular clusters

Galactic bar oscillations (when a bar is present)

The slow gravitational background of the cosmic web (filaments, voids)

Recoil from asymmetric gravitational wave emission during mergers

Perfect stasis is physically impossible. Black hole displacement is the default state.

Observed cases:

M87: 6.8 ± 0.8 pc displacement (Batcheldor et al. 2010, ApJL, 717, L6)

BCGs (Brightest Cluster Galaxies): 1/3 are off-center at z=0 (Chu, Boldrini & Silk 2022)

Milky Way: Sgr A* nuclear star cluster (NSC) offset up to ~100 pc (Bovy et al. 2022)

And when the black hole moves, combined with delayed gravity, spiral arms form. This is a mathematical necessity.

PART 9. Spiral Structure as Default State: Inverting the Question

At this point, the question naturally inverts.

Existing question: “Why do some galaxies have spiral arms?” New question: “Why do some galaxies NOT have spiral arms?”

Mathematical expression: BH displacement > 0 → spiral arms = 100% (deterministic, not probabilistic)

Unicode : BH displacement > 0 ⇒ spiral arms = 100% LaTeX : \text{BH displacement} > 0 \Rightarrow \text{spiral arms} = 100%

Interpretation of the 60-70% spiral galaxy fraction (Lintott et al. 2011, MNRAS, 410, 166):

Existing interpretation: Special conditions are met (density waves, resonances, tidal interactions)

New interpretation: The absence of conditions (ellipticals, lenticulars) is what requires explanation

The remaining 30-40% are systems with no disk or disrupted disks

Spiral arms are the default state.

Simulation results (GalaxyCS v4, 20,000-80,000 stars):

BH at rest (displacement = 0): No spiral structure. Axisymmetric disk.

BH displaced by any non-zero amount: Spiral arms emerge within the first few simulation steps and persist indefinitely.

The transition is not gradual. It is immediate. There is no lower threshold.

Verify directly: Open GalaxyCS v4 → COLLIDE → press any arrow key once → observe. 0.05 radians. That is all that is required.

Simulator code: document.addEventListener(’keydown’, e => { if(e.key === ‘ArrowRight’) BH_ANG += 0.05; // 0.05 radian displacement updateBHOffset(); updateBHVisual(); });

PART 10. Snapshot Mass: The Weight of the Vacuum

Now we go one step further. The quantum vacuum is not empty.

By the energy-time uncertainty relation ΔE·Δt ≥ ℏ/2, virtual particle pairs are continuously created and annihilated.

Unicode : ΔE × Δt ≥ ℏ/2 LaTeX : \Delta E \cdot \Delta t \ge \frac{\hbar}{2} Mathematica : ΔE * Δt >= ħ/2 Python : from sympy import symbols, Ge Delta_E, Delta_t, hbar = symbols(’Delta_E Delta_t hbar’, positive=True) Ge(Delta_E * Delta_t, hbar/2)

Planck scale:

Planck energy: E_P = sqrt(ℏc⁵/G) ≈ 1.22 × 10^19 GeV

Planck time: t_P = sqrt(ℏG/c⁵) ≈ 5.39 × 10^-44 s

Planck length: l_P = sqrt(ℏG/c³) ≈ 1.62 × 10^-35 m

Planck mass: m_P = sqrt(ℏc/G) ≈ 2.18 × 10^-8 kg

Imagine freezing the universe for 10^-44 seconds. In that instant, particle pairs exist on every cubic Planck-length grid cell. Each disappears before any measurement could reach it. But in that frozen moment — they are there. They have mass. They curve spacetime. The snapshot has weight.

Formula (snapshot mass):

Unicode : ⟨M_snap⟩ = ⟨N⟩ × ⟨m⟩ LaTeX : \langle M_{\text{snap}} \rangle = \langle N \rangle \cdot \langle m \rangle Mathematica : M_snap_avg = N_avg * m_avg Python : def snapshot_mass(pairs, current_time): return sum(m for (m, t_created, tau) in pairs if t_created + tau > current_time)

Planck scale estimate:

⟨N₀⟩ ≈ V / l_P³

For galactic volume V_galaxy ≈ 10^61 m³: ⟨N₀⟩ ≈ 10^61 / (1.62×10^-35)³ ≈ 10^166

⟨M_snap⟩₀ ≈ 10^166 × 2.18×10^-8 kg ≈ 10^158 kg

This is about 10^118 times the mass of the Milky Way (~10^40 kg). In flat spacetime, this mass must be almost completely canceled. This is the cosmological constant problem (Weinberg 1989, Reviews of Modern Physics, 61, 1).

“The snapshot has weight. This is not a metaphor. It is a statistical fact.”

In flat spacetime, this statistical mass is almost perfectly canceled. But in extreme environments like black hole surroundings, the correlation structure may be partially disrupted, leaving a residual gravitational effect.

PART 11. The Same Pattern Found Across Scales

11.1 Scale 1: Quantum Vacuum (10^-35 m)

Discovery: The vacuum is not empty. It has statistically valid mass. Key sentence: “The snapshot has weight. This is not a metaphor. It is a statistical fact.” Why this is a Passive Layer: Unintentional (fundamental property of quantum mechanics), uncontrollable (continues as long as the vacuum exists), background (spread throughout the universe).

11.2 Scale 2: Particle Physics (10^-15 m)

Discovery: In strong magnetic fields around black holes, pair-produced particles and antiparticles separate and do not annihilate. Key sentence: “I did not build an accretion disk. One appeared.” Why this is a Passive Layer: Occurs whenever pair production occurs (automatic), separated particles leave gravitational remnants.

11.3 Scale 3: Galaxies (10^21 m)

Discovery: When a black hole is even slightly displaced from the center, delayed gravity immediately creates spiral arms. Key sentence: “This interpolation is the mechanism that produces spiral arms.” Why this is a Passive Layer: As long as the black hole moves (eternally in the universe), remnants continuously accumulate.

PART 12. Falsifiable Predictions

This framework makes the following predictions, each falsifiable by observation (satisfying Popper’s criterion).

Prediction 1: Spiral Arm Strength Correlates with BH Displacement Galaxies with stronger, more symmetric grand-design spiral arms should show larger BH-center offsets when measured at sufficient resolution.

Prediction 2: Arm Count Corresponds to BH Oscillation Mode

Two-armed spirals → simple unidirectional displacement

Multi-armed spirals → oscillatory BH motion

Prediction 3: The Inverse Problem Is Solvable Given a galaxy’s spiral morphology (arm count, pitch angle, symmetry), it should be possible to reconstruct the approximate kinematic history of its central BH.

Prediction 4: Elliptical and Lenticular Galaxies Are the Expected Non-Spiral Population They do not represent failures to produce spiral arms; they represent systems where no disk existed to develop them.

PART 13. Limitations (Stated Honestly)

This framework has significant gaps that must be acknowledged.

This is the decisive difference from pseudoscience. Pseudoscience does not state its limitations. This framework says clearly what it does not know.

Limitation 1: Quantitative Fit Not Performed A quantitative fit to observed rotation curves has not been performed against the full SPARC database (175 galaxies; Lelli, McGaugh & Schombert 2016, AJ, 152, 157). Related Mechanism: Mechanism 1, 2

Limitation 2: The Spatial Profile of Γ(r) Is Unknown The spatial profile of the vacuum statistical mass amplification factor Γ(r) is unknown from first principles. Currently, it remains a free parameter. Related Mechanism: Mechanism 2 (requires quantum gravity calculation)

Limitation 3: Gravitational Lensing Excess Not Explained Gravitational lensing excess cannot be explained by retarded gravity alone, as lensing is a geometric effect independent of time derivatives. Related Mechanism: Mechanism 1, 2 (lensing is geometric; requires additional mass)

Limitation 4: The Cancellation Mechanism for the Cosmological Constant Is Unknown We do not know what causes the 10^123 cancellation in flat spacetime. Without knowing the mechanism, we cannot predict how much it is disrupted in curved spacetime. Related Mechanism: Mechanism 2 (core of the vacuum fluctuation argument)

Limitation 5: Distinguishability from CDM Distinguishing this framework from CDM near galactic centers requires either measurements sensitive to the equation of state or high-precision rotation curve data within the inner ~1 kpc. Related Mechanism: Mechanism 2

PART 14. Comparison with Existing Frameworks

14.1 vs Dark Matter

Dark Matter (existing): Identity: Unknown particle (WIMP, axion, etc.) New physics required: Yes Distribution: NFW halo (Navarro, Frenk & White 1996, ApJ, 462, 563) Direct detection: Theoretically possible (but 50 years of failure)

Passive Layer (this framework): Identity: Accumulation of gravitational remnants New physics required: No (just combination of two verified phenomena) Distribution: Proportional to distance (M_ghost ∝ r) Direct detection: Impossible (not a particle)

The null results from dark matter direct detection experiments (LZ 2024, XENONnT 2024, PandaX-4T 2023) are consistent with the Passive Layer. It is not a particle, so it cannot be detected.

This document does not argue that dark matter does not exist. It argues something narrower and, in some ways, more interesting: that two well-established physical phenomena — the retarded propagation of gravity and the statistical behavior of quantum vacuum fluctuations — may together account for a non-trivial portion of what we currently attribute to unseen mass.

14.2 vs MOND (Modified Newtonian Dynamics)

MOND (Milgrom 1983, ApJ, 270, 365): Approach: Modifies gravity in low-acceleration regime (μ(a/a₀)·a = GM/r²) Free parameter: Requires a₀ ≈ 1.2 × 10^-10 m/s² Relativistic extension: Difficult Physical origin: Unknown

This framework: Approach: Adds mass (Ghost Mass accumulation) Free parameter: None (Ṁ_pair is physically measurable) Relativistic extension: Natural (delayed gravity is already a GR prediction) Physical origin: Clear (pair production + propagation delay)

14.3 vs Lin-Shu Density Wave Theory

Lin-Shu Density Wave Theory (Lin & Shu 1964, ApJ, 140, 646): Approach: Explains spiral arms as density wave patterns Requirements: Pattern speed Ω_p, continuous energy source, resonance conditions Does not explain: 60-70% spiral fraction, initial wave formation

This framework: Approach: Spiral arms as direct result of BH displacement + delayed gravity Requirements: None (only two universal conditions) Explains: 60-70% spiral fraction as default state (absence of conditions requires explanation)

PART 15. The Three Independent Mechanisms (Summary)

This framework is built on three independent mechanisms. They are not mutually exclusive and may operate simultaneously in real environments.

Mechanism 1: BH Offset + Delayed Gravity → Spiral Arms

Claim strength: Strong Verification method: Galaxy simulator (100% reproduced) Current status: Simulation verification complete

Formula: τ(r) = r/c | r_BH_ret(t, r) = r_BH(t - r/c) | BH displacement > 0 → spiral arms = 100%

This is the core claim of the framework. It requires no new physics — only the empirically confirmed finite propagation speed of gravity and observed black hole displacement.

Mechanism 2: Pair Production + Magnetic Isolation → Independent Mass Generation (Ṁ_pair)

Claim strength: Intermediate Verification method: Measurement of pair-production rates around AGN Current status: Hypothesis (quantification required)

Formula (mass rate-of-change equation): dM/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking/c²

Three possible fates for isolated matter and antimatter:

When magnetic field weakens, annihilation → energy release → gravity decreases

Absorbed by black hole → incorporated as mass → gravity increases

Ejected as a jet → moves to galactic outskirts → gravity redistributed

This mechanism is directly observed in the Yang-Mills Collider v3.2 simulation.

Mechanism 3: Gravitational Propagation and the Event Horizon (Separate Claim)

Claim strength: Separate (theoretical investigation stage) Verification method: Gravitational wave observations of dynamic BHs Current status: Stage of theoretical investigation

If gravity propagates at the speed of light, a tension arises for a black hole whose mass is dynamically changing. The gravitational signal arising from dynamic mass changes may not fully escape the horizon.

Note: This claim is independent of Mechanisms 1 and 2. Mechanism 3 is not required for 1 and 2 to hold.

PART 16. Conclusion

This document has presented a framework in which two well-established physical phenomena — the finite propagation speed of gravity and the statistical behavior of quantum vacuum fluctuations — may together account for a non-trivial portion of what is currently attributed to unseen mass.

Logical structure: A = Pair production (verified for decades) B = Finite propagation speed of gravity (verified for decades) A + B = Ghost Mass / Passive Layer (new combination)

To refute this, one must prove that either A or B is false. Both have been verified for decades. No new physics is required. No new particles are required.

This framework does not dispute ΛCDM’s cosmological success. It observes that ΛCDM’s success at cosmological scales does not preclude the existence of additional, smaller-magnitude effects at galactic scales.

The framework is presented as a complementary observation: this effect exists, it is non-zero, and its magnitude under extreme astrophysical conditions has not been adequately quantified.

Whether this framework is correct in whole or in part is a question for empirical validation. The falsifiable predictions stated in Part 12 provide a pathway for such validation. The limitations stated in Part 13 are acknowledged as open questions for future investigation.

Methodology (inductive back-tracking): Not theory → experiment, but experiment → theory. Simulation → observation → theory. This order is stated honestly.

“The simulations were built before this theoretical document. Observations made during simulation preceded and informed the theoretical framework described here. This is the order in which the work actually happened, and it is stated plainly.” — Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation in Disk Galaxies (2026-06-06)

Summary in three short lines: “The snapshot has weight.” — Physics “There was a mushroom kalguksu place.” — Economics “I did not build an accretion disk. One appeared.” — Methodology

APPENDIX A. Links

[0-1] A Relativistic Particle Collider, Built in Pure JavaScript https://seoulinside.substack.com/p/i-built-an-lhc-in-the-browser-making

[0-2] Yang-Mills Collider v3.0 — A technical inventory https://seoulinside.substack.com/p/yang-mills-collider-v30-a-technical

[0-3] LHC Simulation: Physics Formulas and Explanations https://seoulinside.substack.com/p/lhc-simulation-physics-formulas-and

[0-4] Black Hole Physics in Yang-Mills Collider v3.2 https://seoulinside.substack.com/p/black-hole-physics-in-yang-mills

[0-5] I Added a Black Hole to the LHC — and Something Unexpected Happened https://seoulinside.substack.com/p/i-added-a-black-hole-to-the-lhc-and

[0-6] Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation https://seoulinside.substack.com/p/delayed-gravitational-interaction

[1-1] Black Hole Displacement and the Default State of Spiral Galaxies https://seoulinside.substack.com/p/black-hole-displacement-and-the-default

[1-2] A Unified Technical Framework — Simulation Evidence and Theoretical Foundations https://seoulinside.substack.com/p/a-unified-technical-framework-simulation

[1-3] Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe https://seoulinside.substack.com/p/vacuum-fluctuations-delayed-gravity

[1-4] High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes https://seoulinside.substack.com/p/high-energy-particle-generation-and

[a] Passive Layer — Essential Citations https://seoulinside.substack.com/p/passive-layer-essential-citations

[b] The Passive Layer — Core Document https://seoulinside.substack.com/p/the-passive-layer-core-document

[c] Physics Series Full (Index) https://seoulinside.substack.com/p/physics-series-full

[d] The Passive Layer (missing term) https://seoulinside.substack.com/p/the-passive-layer

[e] The Passive Layer and the Reversal of the Burden of Proof https://seoulinside.substack.com/p/the-passive-layer-and-the-reversal

[2-1] Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry https://seoulinside.substack.com/p/long-term-survival-of-antimatter

[2-2] Dark Energy Reinterpreted — Cosmic Expansion as the Relaxation of Curvature https://seoulinside.substack.com/p/dark-energy-reinterpreted-cosmic

[2-3] The Black Hole Mass Variability — Complete Research Archive https://seoulinside.substack.com/p/the-black-hole-mass-variability-complete

[2-4] A Numerical Confirmation of General Relativity https://seoulinside.substack.com/p/a-numerical-confirmation-of-general

[2-5] Pair Annihilation as a Special Case https://seoulinside.substack.com/p/pair-annihilation-as-a-special-case

[2-6] The Connected Framework: How the Suppression of Pair Annihilation Links the Big Bang, the CMB, and Black Hole Mass Variability https://seoulinside.substack.com/p/the-connected-framework-how-the-suppression

[Sim] Yang-Mills Collider v3.2 (revisit) URL: https://xur94-maker.github.io/SeoulInside/LHC_kerr.html Key point: Maximize BH mass and spin to observe ergosphere effects

https://xur94-maker.github.io/SeoulInside/Galaxy.html

https://xur94-maker.github.io/SeoulInside/Galaxy_Finxyz.html

https://xur94-maker.github.io/SeoulInside/LHCkerr.html

https://xur94-maker.github.io/SeoulInside/LHC_kerr_finxyz.html

Recommended Execution Method:

Read STEP 0 to grasp the definition of Passive Layer.

Read STEP 1 while thinking “where does this pattern come from?”

Open the two simulators (LHC_kerr.html, GalaxyCS_v4.html) in advance.

Read STEP 2 and operate the simulators whenever instructed.

LHC: BH mass 0 → 5e10, B-field 6.2T, COLLIDE

Galaxy: COLLIDE → press arrow key (→) once

Read STEP 2.3 (High-Energy Particle Generation) to understand the three mechanisms.

In STEP 3, read the ‘snapshot mass’ concept and ponder the sentence: “The entire universe moves upon the echoes of its own past mass activity.”

APPENDIX B. Complete Collection of Citations and Source URLs

Physics Core Documents

Why Didn’t All the Antimatter Disappear? https://seoulinside.substack.com/p/long-term-survival-of-antimatter

The Textbook Got It Backwards https://seoulinside.substack.com/p/pair-annihilation-as-a-special-case

Document 1: I Added a Black Hole to the LHC — and Something Unexpected Happened URL: https://seoulinside.substack.com/p/i-added-a-black-hole-to-the-lhc-and Date: 2026-06-06 Concepts: Ghost Mass, spontaneous accretion disk, charge separation, 4-line Newtonian gravity, “I did not build an accretion disk. One appeared.”

Document 2: Delayed Gravitational Interaction as a Mechanism for Spiral Arm Formation in Disk Galaxies URL: https://seoulinside.substack.com/p/delayed-gravitational-interaction Date: 2026-06-06 Concepts: Delayed gravity, history buffer (FIFO, 300 steps), BH mass lower bound (Claim III), falsifiable predictions, leapfrog integrator, “This interpolation is the mechanism that produces spiral arms.”

Document 3: Black Hole Displacement and the Default State of Spiral Galaxies URL: https://seoulinside.substack.com/p/black-hole-displacement-and-the-default Date: 2026-06-07 Concepts: Spiral structure as default state, BH displacement, mass ratio comparison (99.8% vs 0.1-0.5%), 4 falsifiable predictions, observed cases (M87, M31, Milky Way), “The standard question is wrong. The correct question is: Why do some galaxies NOT have spiral arms?”

Document 4: Vacuum Fluctuations, Delayed Gravity, and the Statistical Mass of the Universe URL: https://seoulinside.substack.com/p/vacuum-fluctuations-delayed-gravity Date: 2026-06-07 Concepts: Snapshot mass, dark matter reinterpretation, vacuum energy as dynamic background, “The snapshot has weight. This is not a metaphor. It is a statistical fact.”

Document 5: High-Energy Particle Generation and Dynamic Gravity Systems Near Black Holes URL: https://seoulinside.substack.com/p/high-energy-particle-generation-and Date: 2026-06-08 Concepts: Three mechanisms (1/2/3), Ṁ_pair term, early universe SMBH growth, dark matter connection, LHC vs GRB energy scale comparison

Supporting Physics Documents

A Unified Technical Framework — Simulation Evidence and Theoretical Foundations URL: https://seoulinside.substack.com/p/a-unified-technical-framework-simulation | Date: 2026-06-07

Black Hole Physics in Yang-Mills Collider v3.2 URL: https://seoulinside.substack.com/p/black-hole-physics-in-yang-mills | Date: 2026-06-05

LHC Simulation: Physics Formulas and Explanations URL: https://seoulinside.substack.com/p/lhc-simulation-physics-formulas-and | Date: 2026-06-04

Yang-Mills Collider v3.0 — A technical inventory URL: https://seoulinside.substack.com/p/yang-mills-collider-v30-a-technical | Date: 2026-06-04

A Relativistic Particle Collider, Built in Pure JavaScript — Making the Yang-Mills Collider URL: https://seoulinside.substack.com/p/i-built-an-lhc-in-the-browser-making | Date: 2026-06-03

Simulators

Yang-Mills Collider v3.2 URL: https://xur94-maker.github.io/SeoulInside/LHC_kerr.html Instructions: Set BH mass 0 → 5e10, B-field 6.2T, COLLIDE. Observe separated particle pairs.

GalaxyCS v4 URL: https://xur94-maker.github.io/SeoulInside/GalaxyCS_v4.html Instructions: COLLIDE → press arrow key (→) once. Observe spiral arm formation with 0.05 radian BH displacement.

This document is the complete definition of Passive Layer and Passive Layers Stacking. All mathematical formulations are given in four parallel notations (Unicode, LaTeX, Mathematica, Python). All source citations are included. Falsifiable predictions are stated explicitly. Limitations are acknowledged throughout. The three independent mechanisms are summarized. No external intention is stated. The pattern is presented as observed.

Key quotes:

Physics: “The snapshot has weight. This is not a metaphor. It is a statistical fact.” — Vacuum Fluctuations “I did not build an accretion disk. One appeared.” — I Added a Black Hole to the LHC “This interpolation is the mechanism that produces spiral arms.” — Delayed Gravitational Interaction “When a black hole is displaced from the geometric center of a disk galaxy — however slightly — spiral arm structure emerges immediately and persistently.” — Black Hole Displacement “Perfect black hole stasis would require exact cancellation of all perturbations simultaneously and continuously. This is not physically plausible.” — Black Hole Displacement “This document does not argue that dark matter does not exist. It argues something narrower and, in some ways, more interesting.” — Vacuum Fluctuations “This framework makes the following predictions, each falsifiable by observation.” — Black Hole Displacement “The entire universe moves upon the echoes of its own past mass activity.”