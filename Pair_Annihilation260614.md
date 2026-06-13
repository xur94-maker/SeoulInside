# Pair Annihilation as a Special Case: Why Antiparticles Are More Likely to Meet Ordinary Matter Than Their Own Pairs

**Date:** 2026-06-14
**Author:** B. Sun | Seoul Inside
**Foundation:** Yang-Mills Collider v3.2, Passive Layer Series, Antimatter260611
**Purpose:** To establish that pair annihilation — the assumed default fate of antiparticles — is in fact a geometrically exceptional process requiring conditions that are rarely satisfied in any realistic high-energy magnetic environment, and that antiparticles in such environments are statistically more likely to encounter ordinary matter than their own pair-produced partners.

**Relationship to prior documents:**
- *Long-Term Survival of Antimatter* (2026-06-11) established that charge separation occurs for any B ≠ 0, and that the Sakharov conditions operate in a different regime entirely.
- This document goes one step further: it asks not merely whether separation occurs, but what the separated antiparticle encounters next. The answer has not been made explicit in prior documents. It is made explicit here.

---

## References

Dirac, P.A.M. (1928). The Quantum Theory of the Electron. Proceedings of the Royal Society A, 117, 610.
https://royalsocietypublishing.org/doi/10.1098/rspa.1928.0023

Particle Data Group (2022). Review of Particle Physics.
https://pdg.lbl.gov

Boris, J.P. (1970). Relativistic Plasma Simulation — Optimization of a Hybrid Code. Proc. 4th Conf. Numerical Simulation of Plasmas, NRL, Washington.

Bhabha, H.J. (1936). The Scattering of Positrons by Electrons with Exchange on Dirac's Theory of the Positron. Proceedings of the Royal Society A, 154, 195.

B. Sun. Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry (2026-06-11).
https://seoulinside.substack.com/p/long-term-survival-of-antimatter

B. Sun. I Added a Black Hole to the LHC — and Something Unexpected Happened (2026-06-06).
https://seoulinside.substack.com/p/i-added-a-black-hole-to-the-lhc-and

---

## 1. The Central Claim

Pair annihilation requires a precise geometric coincidence: a particle and its antiparticle must occupy the same spatial location at the same time, with sufficient interaction time to complete the annihilation process. In a vacuum with no magnetic field and low relative velocity, this condition is routinely satisfied. This is the regime in which pair annihilation has been studied, measured, and theorized for nearly a century.

It is not the regime of the early universe, nor of any high-energy astrophysical environment.

In any environment characterized by:

1. Non-zero magnetic field (B ≠ 0), and
2. Ultrarelativistic particle velocities (v → c)

the geometric conditions required for pair annihilation become extraordinarily difficult to satisfy. The particle and its antiparticle, produced at the same point, immediately diverge into opposite-sense helical trajectories. Their mutual separation grows with every timestep. Meanwhile, the antiparticle is surrounded not by its pair-produced partner — which is already moving away — but by the ambient ordinary matter of its environment.

**The conclusion that follows is not subtle:**

In a magnetic environment, an antiparticle is more likely to encounter and interact with ordinary matter than with its own pair-produced partner.

Pair annihilation (e⁺ + e⁻ → γ + γ) is the textbook case. But the textbook assumes B = 0 and thermal velocities. Remove either assumption, and the geometry changes entirely.

---

## 2. The Geometry of Pair Production in a Magnetic Field

### 2.1 What Happens at the Moment of Production

Consider the simplest case: a photon-photon collision producing an electron-positron pair at position **r₀** at time t₀:

γ + γ → e⁻ + e⁺

At t = t₀, both particles occupy the same point. The annihilation cross section is at its conceptual maximum — they are literally co-located.

Now introduce B ≠ 0.

The Lorentz force acts immediately:

**F**_e⁻ = (-e)(**v** × **B**)

**F**_e⁺ = (+e)(**v** × **B**)

The forces are equal in magnitude and opposite in direction. The electron curves one way; the positron curves the other. At t = t₀ + Δt, they are no longer co-located. At t = t₀ + 2Δt, the separation is larger. The separation grows monotonically.

This is not an approximation. The Boris integrator — the standard algorithm for charged particle motion used in GEANT4 and all major plasma physics codes — encodes this exactly:

```javascript
const tc = (charge * dt * 0.5) / (gam * mass);
```

When `charge = +1` (positron): rotation in one sense.
When `charge = -1` (electron): rotation in the opposite sense.

One line. One sign. Inevitable divergence.

### 2.2 The Interaction Time Problem

For pair annihilation to occur, the particle and antiparticle must not merely be co-located — they must remain in sufficient proximity for the quantum mechanical interaction to complete. The annihilation cross section for relativistic particles is given by the Dirac formula (for e⁺e⁻, in the ultrarelativistic limit):

σ_ann ~ πr_e² · (m_e c² / E) · ln(2E / m_e c²)

where r_e = 2.818 × 10⁻¹³ cm is the classical electron radius.

At ultrarelativistic energies (E ≫ m_e c²), σ_ann falls as 1/E. The cross section decreases precisely as the energy — and therefore the velocity — increases.

This has a direct geometric consequence. The interaction time for two particles approaching each other at velocity v is:

τ_int ~ d / (2v)

where d is the interaction range (~r_e for electromagnetic processes). At v → c:

τ_int ~ r_e / (2c) ~ 5 × 10⁻²⁴ s

This is not zero. But in this same interval, the Lorentz force has already begun rotating the trajectories in opposite senses. The question is whether the annihilation cross section is large enough to capture the interaction before the magnetic deflection separates the particles beyond interaction range.

At high energy, the answer is: increasingly, no.

### 2.3 The Separation Rate vs. the Annihilation Rate

The rate at which pair annihilation occurs competes directly with the rate at which the magnetic field separates the pair. Define:

- **Γ_ann** = n · ⟨σ_ann v_rel⟩ : annihilation rate (per particle, per unit time)
- **Γ_sep** = v_⊥ / r_L = |q|B / (γm) = ω_c : separation rate (cyclotron frequency)

The cyclotron frequency ω_c increases with B and decreases with γm. For ultrarelativistic particles in strong magnetic fields:

ω_c = |q|B / (γm) ≫ Γ_ann

The separation rate dominates the annihilation rate. The particle and antiparticle are deflected away from each other faster than they can annihilate.

This is not a theoretical claim. It is a direct consequence of the field strength hierarchy. In the environment of M87* (B_ISCO ~ 10³ G, γ ~ 10⁶):

ω_c ~ eB / (γm_e) ~ (1.6×10⁻¹⁹)(10³) / (10⁶ × 9.1×10⁻³¹) ~ 1.8 × 10⁸ rad/s

The cyclotron period is ~ 3 × 10⁻⁸ s. The annihilation time at these densities is orders of magnitude longer. The magnetic separation is complete long before annihilation can occur.

---

## 3. What the Antiparticle Encounters Instead

### 3.1 The Population Asymmetry

Once the antiparticle is separated from its pair-produced partner, it finds itself in an environment consisting overwhelmingly of ordinary matter. The universe contains, by observation, approximately 10¹⁰ baryons for every surviving antibaryon. The ambient medium is matter-dominated.

The antiparticle's nearest neighbors are not antiparticles. They are ordinary particles.

### 3.2 Antiparticle-Matter Interactions

An antiparticle (e.g., positron) interacting with ordinary matter (e.g., electron) does undergo annihilation — but this is not pair annihilation in the standard sense. It is the annihilation of a particle and an antiparticle that were not produced together, from different production events, with different momenta and histories.

The distinction matters for two reasons:

**Reason 1 — Energy spectrum:**
Pair annihilation of particles produced in the same event conserves the center-of-mass energy of that event. The resulting photons have a specific energy determined by that collision.

Antiparticle + ambient matter annihilation has a different energy spectrum, determined by the relative velocity of the antiparticle and the ambient particle at the moment of encounter. The 511 keV line — the signature of electron-positron pair annihilation at rest — is not the expected output. The spectrum is broader, less peaked, and energy-dependent.

**Reason 2 — Reaction products:**
At high energies, antiparticle-matter interactions are not limited to the two-photon channel. They can produce pions, kaons, and other hadrons through:

p̄ + p → π⁺ + π⁻ + π⁰ + ...

These are inelastic reactions with complex final states — qualitatively different from the clean two-photon output of pair annihilation.

### 3.3 The Statistical Argument

In any environment where:

(a) B ≠ 0, causing pair-produced partners to separate immediately, and
(b) The ambient medium is matter-dominated

the probability that a given antiparticle encounters ordinary matter before re-encountering its pair-produced partner is determined by the ratio of:

- Number density of ambient matter particles in the antiparticle's trajectory, vs.
- Probability of re-encountering the specific pair-produced partner

In a matter-dominated universe with 10¹⁰ baryons per antibaryon, this ratio is approximately 10¹⁰ to 1.

**The antiparticle will encounter ordinary matter first. Not because of exotic physics. Because of arithmetic.**

---

## 4. Redefining the Default Process

### 4.1 What "Default" Means

When physicists say pair annihilation is the "default" fate of antiparticles, they mean: in the absence of any mechanism preventing it, a particle and its antiparticle will eventually annihilate.

This is true. But "eventually" contains a hidden assumption: that the particle and antiparticle remain in proximity long enough for the interaction to occur.

In B = 0 environments at low velocity, this assumption is valid.

In B ≠ 0 environments at ultrarelativistic velocities, this assumption fails.

The "default" process in a realistic high-energy magnetic environment is not pair annihilation. The default process is:

1. Pair production at a common point
2. Immediate magnetic separation into opposite-sense helical trajectories
3. Independent propagation through a matter-dominated medium
4. Eventual interaction with ambient ordinary matter

Pair annihilation — the collision of a particle with its own pair-produced partner — requires the two particles to overcome their magnetic separation and find each other again in a matter-dominated medium. This is not impossible. It is geometrically suppressed.

### 4.2 The Conditions for Pair Annihilation

Pair annihilation, as a dominant process, requires:

| Condition | Standard assumption | Realistic high-energy environment |
|-----------|--------------------|------------------------------------|
| B field | B = 0 | B ≠ 0 (always, in astrophysical contexts) |
| Velocity | Thermal (v ≪ c) | Ultrarelativistic (v → c) |
| Medium | Vacuum or pair-dominated | Matter-dominated |
| Separation | None | Immediate, at production |

All four conditions of the standard assumption fail simultaneously in any realistic high-energy magnetic environment. Pair annihilation in such an environment is not the default. It is the exception.

---

## 5. Implications

### 5.1 For the Matter-Antimatter Asymmetry

The standard baryogenesis framework asks: why were more baryons created than antibaryons?

This document suggests a prior question: why did we assume that every antibaryon produced would annihilate with its pair-produced partner?

If antiparticles in magnetic environments preferentially interact with ambient ordinary matter rather than their pair-produced partners, then the survival of matter does not require an asymmetry in production. It requires only:

1. B ≠ 0 in the early universe (predicted by every model of early-universe physics)
2. A matter-dominated local region (which is the observation to be explained, not an assumption)

The matter dominance of our observable universe may reflect the geometry of charge separation, not an asymmetry in fundamental physics.

### 5.2 For BBN

If antiparticles in the early universe preferentially interacted with ambient ordinary matter rather than undergoing pair annihilation, the energy released per annihilation event is different, the reaction products are different, and the photon-to-baryon ratio evolves differently.

The helium-4 abundance and deuterium-to-hydrogen ratio predicted by Big Bang Nucleosynthesis assume a specific photon-to-baryon ratio η = 6.1 × 10⁻¹⁰. If a fraction of annihilation events produced hadrons rather than photons, η is modified. The direction of this modification — and whether it improves or worsens agreement with observation — requires quantitative calculation. It is identified here as an open problem.

### 5.3 For Observational Astrophysics

If antiparticles in astrophysical magnetic environments (AGN, magnetars, gamma-ray bursts) preferentially annihilate with ambient matter rather than their pair-produced partners, the predicted observational signature differs from standard pair annihilation:

**Standard pair annihilation signature:**
- 511 keV line (monochromatic, from e⁺e⁻ at rest)
- Two back-to-back photons in the center-of-mass frame

**Antiparticle-matter annihilation signature:**
- Broad, energy-dependent spectrum (not monochromatic)
- Additional hadronic channels at high energy
- No sharp 511 keV line from relativistic interactions

This prediction is testable. Observations of AGN jets, magnetar flares, and gamma-ray burst afterglows that show anomalous continuum emission without a sharp 511 keV line may be consistent with this mechanism.

---

## 6. The B = 0 Special Case

There exists exactly one environment in which pair annihilation is the unambiguous default: B = 0, at thermal or sub-relativistic velocities, in a pair-symmetric medium.

This is the environment of the laboratory positron annihilation experiment. It is also the environment of no known astrophysical system.

Every known astrophysical environment with significant pair production — AGN, gamma-ray bursts, magnetar magnetospheres, the early universe above the pair-production threshold — contains magnetic fields. The B = 0 assumption, which underlies the standard treatment of pair annihilation as the default process, is an idealization that applies nowhere in the universe where pair production is actually occurring at significant rates.

The appropriate default for any realistic pair-production environment is therefore not:

> "The antiparticle will annihilate with its pair-produced partner."

It is:

> "The antiparticle will be magnetically separated from its pair-produced partner and will subsequently interact with whatever it encounters first — which, in a matter-dominated universe, is ordinary matter."

Pair annihilation is the special case. B = 0 is the special case.

---

## 7. Open Problems

**7.1 Quantitative Suppression Factor**
The ratio Γ_sep / Γ_ann as a function of B and γ has not been computed across the full parameter space relevant to the early universe. This calculation would yield a quantitative suppression factor for pair annihilation as a function of field strength and particle energy.

**7.2 Antiparticle-Matter Interaction Spectrum**
The energy spectrum of photons and hadrons produced when a relativistic antiparticle annihilates with ambient ordinary matter (rather than its pair-produced partner) has not been computed for early-universe conditions. This spectrum would serve as a direct observational discriminant.

**7.3 BBN Modification**
The quantitative effect on the helium-4 and deuterium abundances of replacing a fraction of pair annihilation events with antiparticle-matter annihilation events requires detailed BBN calculation. The direction and magnitude of the modification are identified here as open problems.

**7.4 Domain Boundary Dynamics**
At the boundaries between matter-dominated and antimatter-dominated domains (as described in Antimatter260611), the interaction of antiparticles with ordinary matter — rather than pair annihilation — produces a different energy injection history. The effect on the thermal history of the universe at domain boundaries requires magnetohydrodynamic simulation.

---

## 8. Conclusion

Pair annihilation is taught as the inevitable fate of antiparticles. The teaching is correct for B = 0 at thermal velocities. It does not generalize.

In any environment with B ≠ 0 and ultrarelativistic particle velocities — which is to say, in every astrophysical environment where pair production occurs at significant rates — the following sequence is not pair annihilation but its suppression:

1. γ + γ → e⁻ + e⁺ at a common point
2. **F** = q(**v** × **B**) acts in opposite directions on opposite charges
3. Separation begins at t = t₀ + Δt, grows monotonically
4. The separation rate ω_c = |q|B/(γm) exceeds the annihilation rate Γ_ann
5. The antiparticle propagates independently through a matter-dominated medium
6. The antiparticle encounters ordinary matter — not its pair-produced partner

The standard question — "why do we live in a matter-dominated universe?" — assumes that pair annihilation was the default process in the early universe, and that some mechanism had to overcome it. This document argues that the assumption is wrong. Pair annihilation was never the default in a magnetized, ultrarelativistic early universe.

The question to ask is not: **"What prevented pair annihilation?"**

The question to ask is: **"What would have caused pair annihilation to dominate in an environment where B ≠ 0 and v → c?"**

The answer is: nothing. Pair annihilation, under those conditions, is the special case.

---

**Author:** B. Sun | Seoul Inside
seoulinside.substack.com

*This document extends the argument of Long-Term Survival of Antimatter (2026-06-11) by making explicit what that document left implicit: that the separated antiparticle does not find its pair-produced partner again. It finds ordinary matter. The implications of this geometric fact for baryogenesis, BBN, and observational astrophysics are identified as open problems for quantitative calculation.*

*Post #19 in the Yang-Mills Collider / Passive Layer Series*
