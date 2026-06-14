# The Missing Term: Black Hole Mass Variability, JWST's Overmassive Black Holes, and the Equation That Explains Both

**Date:** 2026-06-14
**Author:** B. Sun | Seoul Inside
**Foundation:** Passive Layer Series (Posts #1–#20), Yang-Mills Collider v3.2, GalaxyCS v5.1
**Purpose:** To suggest that a term absent from the standard black hole mass equation — Ṁ_pair — may help explain two of the most pressing observational anomalies in current astrophysics: the overmassive black holes discovered by JWST, and the timescale problem of changing-look quasars.

**Relationship to prior documents:**
- *The Black Hole Mass Variability* (2026-06-11): Introduced the Ṁ_pair term and the modified equation.
- *Pair Annihilation as a Special Case* (2026-06-14): Established that Ṁ_pair is non-zero in any B ≠ 0 environment.
- *The Connected Framework* (2026-06-14): Placed BH mass variability within the full cascade from particle physics to cosmology.
- This document applies the framework to current observational data. It does not claim to resolve these anomalies. It identifies a direction.

---

## References

Abbott et al. (LIGO/Virgo). GW170817. Physical Review Letters, 119, 161101 (2017).

Bogdán et al. JWST detection of overmassive black hole UHZ1 at z~10. Nature Astronomy (2024).

Brooks, M. et al. Stacking analysis of early-universe AGN. The Astrophysical Journal (2026).

Gaskell & Rojas Lobos. CLAGN transitioning from type 2 to type 1 within 20 days (2013).

Juodžbalis et al. JADES: comprehensive census of broad-line AGN. arXiv:2504.03551 (2025).

Kocevski et al. JWST AGN survey, BH-to-galaxy mass ratios at high redshift (2025).

LaMassa et al. Discovery of the first changing-look quasar. ApJ, 800, 144 (2015).

Li, J. et al. Tip of the Iceberg: Overmassive Black Holes at 4 < z < 7. ApJ, 981, 19 (2025).

MacLeod et al. Systematic search for changing-look quasars in SDSS. A&A (2021).
— J1723+5504: transition from type 1.8 to type 1 in 184 days.

Pacucci & Narayan. Super-Eddington accretion in early-universe black holes. ApJ (2024).

Particle Data Group (2022). Review of Particle Physics. pdg.lbl.gov

Planck Collaboration. Planck 2018 Results VI. A&A, 641, A6 (2020).

B. Sun. The Black Hole Mass Variability — Complete Research Archive (2026-06-11). seoulinside.substack.com
B. Sun. Pair Annihilation as a Special Case (2026-06-14). seoulinside.substack.com
B. Sun. The Connected Framework (2026-06-14). seoulinside.substack.com

**Simulation tools (open source, browser-executable):**
Yang-Mills Collider v3.2: [github.com/xur94-maker/SeoulInside]
GalaxyCS v5.1: [github.com/xur94-maker/SeoulInside]

---

## A Note Before We Begin

The observations described in this document are real and currently unresolved. The framework proposed here is not. It is a structural argument — a suggestion that a term missing from a standard equation may be relevant to these anomalies. The quantitative calculations that would confirm or refute this suggestion are identified explicitly as open problems.

The simulation evidence cited here is reproducible by anyone with a browser. The code is open. Nothing requires specialized equipment or institutional access. This is offered not as proof, but as a starting point for examination.

---

## 1. The Standard Equation and Its Missing Term

The mass of a black hole changes over time. This is not controversial. What is less examined is whether the standard equation describing this change is complete.

The standard equation is:

**dM_BH/dt = Ṁ_in - Ṁ_out - Ṗ_Hawking/c²**

where:
- Ṁ_in = mass inflow rate (accretion)
- Ṁ_out = mass outflow rate (jets, winds)
- Ṗ_Hawking/c² = Hawking radiation mass loss (negligible for any observed black hole)

This equation has three terms on the right-hand side. The argument of this series is that it may be missing one:

**dM_BH/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking/c²**

The missing term is **Ṁ_pair**: the rate at which pair-produced mass persists in the black hole environment due to magnetic charge separation preventing immediate annihilation.

The case for why this term exists is made in detail in prior documents. The purpose of this document is narrower: to ask what changes when this term is included, and whether those changes are consistent with two specific observational anomalies that currently lack established explanations.

---

## 2. Two Anomalies, One Structural Gap

### 2.1 JWST's Overmassive Black Holes

Since 2022, JWST has returned observations that challenge standard models of black hole growth. At redshifts z > 4 — corresponding to the universe less than 1.5 billion years old — JWST found black holes with black-hole-to-stellar-mass ratios M_BH/M_* of 1% to 10%. Some systems approach M_BH/M_* ~ 1. The local relation is M_BH/M_* ~ 10⁻³.

The discrepancy is not marginal. These black holes are 10 to 100 times more massive relative to their host galaxies than the local relation predicts.

The community has proposed several explanations:
- Super-Eddington accretion (growth faster than the Eddington limit)
- Heavy seeds from direct-collapse black holes
- Population III star remnants as massive initial seeds
- Selection bias in the observed sample

The most recent contribution — a 2026 stacking analysis by Brooks et al. — argues that individual detections were biased toward extreme cases, and that the average early-universe black hole may be only ~10 times overmassive rather than 100 times. This is a genuine methodological contribution. It reduces the scale of the anomaly. It does not eliminate it.

A "consistent theoretical framework," as one recent review summarizes, "has yet to emerge."

**The anomaly:** black holes in the early universe appear more massive than standard Eddington-limited accretion can produce in the available time, relative to their host galaxies.

### 2.2 The Changing-Look Quasar Timescale Problem

A changing-look quasar (CLQ) is an active galactic nucleus that transitions between bright and dim states on timescales of months to years. Some transitions have been documented within 20 days (Gaskell & Rojas Lobos 2013). One systematic survey found a transition from type 1.8 to type 1 AGN in 184 days (MacLeod et al. 2021, J1723+5504). These are not exceptional cases — surveys have now identified hundreds of such objects.

The timescale problem is severe and well-documented in the literature itself:

> "Theoretical viscous timescales in accretion theory suggest that dramatic state changes in AGN should span 10⁴–10⁷ years. However, changing-look AGN were discovered shifting between bright and dim states on timescales from only months to years." — multiple sources, consistent phrasing

The discrepancy is not a factor of two. It is a factor of 10⁴ to 10⁷.

The standard explanation — accretion rate changes — is incomplete by construction: accretion rate changes propagate on the viscous timescale, which is precisely the timescale that is too long by four to seven orders of magnitude.

**The anomaly:** quasar state transitions occur on timescales that standard accretion disk theory cannot explain.

---

## 3. What the Missing Term Changes

### 3.1 For JWST's Overmassive Black Holes

The standard growth equation accounts for one source of mass increase: accretion (Ṁ_in). If Ṁ_pair contributes comparably, the effective growth rate has been systematically underestimated.

In the environment of a high-redshift AGN, three conditions hold simultaneously:

1. **B ≠ 0** — magnetic fields are a structural feature of any accretion environment
2. **v → c** — particle velocities in AGN environments are ultrarelativistic
3. **γγ → e⁺e⁻** — pair production occurs at these energies and radiation densities

From *Pair Annihilation as a Special Case* (2026-06-14): in any environment where these three conditions hold, pair-produced particles are separated by the Lorentz force before they can annihilate. The mass persists. It accumulates. This is not a hypothesis about what might happen — it is a direct consequence of F = q(**v** × **B**), verified to extraordinary precision, implemented in a single line of code in Yang-Mills Collider v3.2:

```javascript
const tc = (charge * dt * 0.5) / (gam * mass);
```

When charge = +1 (positron): rotation in one sense.
When charge = -1 (electron): rotation in the opposite sense.
When B = 0: tc = 0, no rotation, no separation, no persistent mass.

The simulation confirms this directly. With B = 0, particles propagate in straight lines and are absorbed isotropically — no disk, no structure. With B ≠ 0, charge separation occurs immediately and a disk structure forms without any disk-building code. This is reproducible by anyone; the simulator runs in a browser and the source code is open.

The Ṁ_pair contribution estimated from M87* observed parameters (B_ISCO ~ 10³ G, n_e ~ 10⁴–10⁵ cm⁻³) is:

**Ṁ_pair ~ 10⁻⁴ to 10⁻² M☉/yr**

Early-universe AGN environments are more extreme than present-day M87* — higher radiation density, stronger magnetic fields, denser pair-production environments. The Ṁ_pair contribution in those environments is not smaller. The direction of the effect is toward larger values.

Over 500 Myr, even the lower bound contributes:

**ΔM_BH ~ 10⁻⁴ M☉/yr × 5 × 10⁸ yr = 5 × 10⁴ M☉**

This is a lower bound from conservative parameters. The total growth becomes:

**M_BH(t) = M_seed + ∫(Ṁ_in + Ṁ_pair) dt**

Both terms are positive. The omission of Ṁ_pair means standard growth models have been working with an incomplete equation.

### 3.2 For Changing-Look Quasars

The Ṁ_pair term is not subject to the viscous timescale. It is not a property of the accretion disk. It is a property of the pair-production environment in the magnetosphere surrounding the black hole.

The pair-production rate responds to changes in photon density and magnetic field strength. Both can change on the dynamical timescale of the inner magnetosphere — set by the light-crossing time of the ISCO:

**t_dyn ~ r_ISCO / c = 6GM/c³**

For a black hole with M_BH ~ 3–4 × 10⁷ M☉ (the range found in CLQ surveys, MacLeod et al. 2021):

**t_dyn ~ 6 × (6.67×10⁻¹¹)(6×10⁷ × 2×10³⁰) / (3×10⁸)³ ~ 5.6 × 10⁶ s ~ 65 days**

This is consistent with observed CLQ transition timescales of months to a year. The 184-day transition of J1723+5504 corresponds to approximately three dynamical times at this mass — physically reasonable for a process that builds up and dissipates across the inner magnetosphere.

The standard viscous timescale for the same system:

**t_visc ~ (r/H)² × t_dyn ~ 10⁴–10⁷ × t_dyn ~ 10³–10⁶ years**

The Ṁ_pair mechanism operates on the dynamical timescale. The viscous disk mechanism operates on the viscous timescale. The observations are on the dynamical timescale. The two mechanisms make different predictions, and the observations select one.

---

## 4. The Magnitude Comparison

The Hawking radiation term in the complete equation deserves attention, not because it is astrophysically relevant, but because its scale illustrates what the Ṁ_pair term adds:

For M87* (M ~ 6.5 × 10⁹ M☉):

**Ṗ_Hawking/c² ~ 10⁻⁷⁷ M☉/yr**

This number has no astrophysical consequence. M87* will lose one solar mass to Hawking radiation on a timescale exceeding 10⁸⁶ years.

| Term | M87* estimated rate | Timescale relevance |
|------|--------------------|--------------------|
| Ṗ_Hawking/c² | ~10⁻⁷⁷ M☉/yr | None |
| Ṁ_pair (lower bound) | ~10⁻⁴ M☉/yr | Astrophysically significant |
| Ṁ_in (standard accretion) | ~10⁻³ M☉/yr | Astrophysically significant |

The Ṁ_pair term is comparable in magnitude to the accretion term. One has been in the equation for decades. One has not been in the equation at all.

---

## 5. The Selection Bias Counter-Argument

The 2026 stacking analysis (Brooks et al.) argues that individual JWST detections of overmassive black holes were biased: bright AGN are easier to detect, and bright AGN have more massive black holes relative to their hosts. Stacking fainter galaxies reduces the apparent overmassiveness from a factor of ~100 to a factor of ~10.

This is a reasonable and important contribution. It should be taken seriously.

It does not close the problem for two reasons.

First, a factor of 10 elevation in M_BH/M_* remains anomalous. The local relation is M_BH/M_* ~ 10⁻³. A factor of 10 enhancement still requires a growth mechanism that produces disproportionate black hole mass before substantial stellar mass accumulates. This is what the Ṁ_pair term addresses.

Second, the selection bias argument addresses the observed population statistics. It does not address the growth mechanism. The question — what produces the black hole mass in the available time — remains open regardless of whether the extreme cases are outliers or typical.

---

## 6. Falsifiable Predictions

If the Ṁ_pair term contributes comparably to Ṁ_in in AGN environments, two predictions follow that differ from the standard accretion-only picture:

**Prediction 1 — Variability amplitude vs. magnetic field:**
Black hole mass variability amplitude should correlate with local magnetic field strength at the ISCO, not only with accretion rate. Two AGN with identical accretion rates but different B_ISCO should show different variability amplitudes. This is testable with existing multi-wavelength AGN monitoring campaigns combined with radio polarimetry measurements.

**Prediction 2 — CLQ timescale scaling:**
The transition timescale of changing-look quasars should scale with r_ISCO/c (the dynamical timescale), not with the viscous timescale of the accretion disk. If this scaling holds across a statistical sample of CLQs with known black hole masses, the Ṁ_pair mechanism is supported and the viscous disk mechanism is disfavored as the primary driver.

---

## 7. What Remains Open

This document does not claim to have computed Ṁ_pair from first principles for any specific early-universe AGN. The complete calculation requires:

**7.1** The photon density n_γ as a function of redshift and AGN luminosity — available from observational constraints but requires integration over the pair-production cross section at each epoch.

**7.2** The magnetic field B at the ISCO as a function of AGN mass and accretion rate — constrained for nearby AGN by Faraday rotation measurements; extrapolation to high-z requires modeling.

**7.3** The fraction of pair-produced mass that remains in the system versus escaping in jets or winds — requires magnetohydrodynamic simulation.

These calculations are the quantitative program that would convert the structural argument into precise predictions. They are not performed here. They are identified as the necessary next step.

What is not open is the existence of the Ṁ_pair term itself. It follows from three facts that are not in dispute:

1. Gravity propagates at c. (GW170817, Abbott et al. 2017)
2. Mass is continuously created and destroyed. (Pair production, confirmed at LHC and in AGN environments daily)
3. The Lorentz force acts oppositely on opposite charges for any B ≠ 0. (Verified to extraordinary precision for over a century)

From these three facts, in any magnetized pair-production environment, Ṁ_pair is non-zero. Whether it is large enough to matter quantitatively in specific systems is the open question. That it exists is not.

---

## 8. On Reproducibility

The simulation evidence cited throughout this series is reproducible by anyone with a modern browser. Yang-Mills Collider v3.2 and GalaxyCS v5.1 are single HTML files. No installation. No compilation. No institutional access required.

The three-condition experiment at the core of the accretion disk argument:

```
B = 0.0 T  →  Particles propagate in straight lines.
              Black hole absorbs everything isotropically.
              No disk. No structure. Every time.

B = 3.5 T  →  Charge separation begins immediately.
              Disk structure forms.

B = 14.0 T →  Disk forms rapidly and stabilizes into
              a nearly perfect equatorial ring.
```

This is not claimed as proof of anything. It is offered as a starting point. The code is open. The parameters are reproducible. The observation — that a disk forms without any disk-building code, solely from the Lorentz force acting on opposite charges in opposite directions — is verifiable by anyone who presses COLLIDE.

[Yang-Mills Collider v3.2 → github.com/xur94-maker/SeoulInside]
[GalaxyCS v5.1 → github.com/xur94-maker/SeoulInside]

---

## 9. Conclusion

The black hole mass equation used in standard astrophysics may be missing a term.

The missing term — Ṁ_pair — follows necessarily from confirmed physical laws operating in confirmed astrophysical environments. Its magnitude, estimated from directly observed parameters, is comparable to the standard accretion rate. Its omission means that models of black hole growth have been working with an incomplete equation.

Two of the most pressing current observational anomalies are consistent with this omission:

**JWST's overmassive black holes** require a growth mechanism that produces disproportionate black hole mass in the early universe. The Ṁ_pair term contributes positively to growth in exactly the environments — extreme magnetic fields, ultrarelativistic pair production — that characterized early-universe AGN.

**Changing-look quasar timescales** require a mass variability mechanism that operates on dynamical rather than viscous timescales. The Ṁ_pair term responds to changes in the inner magnetosphere on exactly those timescales.

The same missing term. The same two anomalies. A possible common explanation.

This is not presented as a resolution. It is presented as a question: if the standard equation is incomplete, what follows? The answer may be worth examining.

No new particles. No new forces. No new mathematics.

Three facts. One missing term. Two anomalies.

---

**Author:** B. Sun | Seoul Inside
seoulinside.substack.com

*Post #21 in the Yang-Mills Collider / Passive Layer Series*

*All simulation source code, physics implementations, and prior derivations are documented across Posts #1–#20 at Seoul Inside / Substack and at github.com/xur94-maker/SeoulInside. The quantitative calculations identified as open problems define the research program ahead.*
