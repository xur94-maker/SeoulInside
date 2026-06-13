# Long-Term Survival of Antimatter and the Matter-Antimatter Asymmetry: A Charge Separation Mechanism via Magnetic Fields

**Date:** 2026-06-11
**Foundation:** Yang-Mills Collider v3.2 (LHC_kerr_2.html), Passive Layer Series
**Purpose:** To demonstrate that pair annihilation is not a default process but a conditional phenomenon, and to propose a new physical mechanism for the matter-antimatter asymmetry problem that requires no new particles, no new forces, and no new mathematics.

---

## References

Abbott et al. (LIGO/Virgo Collaboration). GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. Physical Review Letters, 119, 161101 (2017).
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.119.161101

Particle Data Group (2022). Review of Particle Physics.
https://pdg.lbl.gov

Sakharov, A.D. (1967). Violation of CP Invariance, C Asymmetry, and Baryon Asymmetry of the Universe. JETP Letters, 5, 24-27.
https://ufn.ru/en/articles/1991/6/f/

B. Sun. I Added a Black Hole to the LHC — and Something Unexpected Happened (2026-06-06).
https://seoulinside.substack.com/p/i-added-a-black-hole-to-the-lhc-and

B. Sun. Passive Layer — Essential Citations (2026-06-08).
https://seoulinside.substack.com/p/passive-layer-essential-citations

---

## 1. The Central Claim

Pair annihilation is not a fundamental default process. It is a conditional phenomenon that requires two things to happen simultaneously: a particle and its antiparticle must occupy the same spatial location at the same time. In the absence of any mechanism that physically separates them, this condition is naturally met. However, in the presence of a magnetic field of any non-zero strength, the Lorentz force acts on opposite charges in opposite directions, driving particles and antiparticles into geometrically distinct trajectories. Once spatially separated, they cannot annihilate. They persist as mass.

This statement contains no threshold, no minimum field strength, no special condition beyond B ≠ 0. The separation is not a matter of degree that kicks in above some critical value. It is a binary structural consequence of the sign of the charge in the Lorentz force law:

**F** = q(**v** × **B**)

For a particle with charge +q moving with velocity **v** in magnetic field **B**, the force deflects it in one direction. For its antiparticle with charge -q and identical speed, the force deflects it in the opposite direction. This is not an approximation. It is exact, and it holds for any B ≠ 0, for any particle species with non-zero charge, at any energy.

The matter-antimatter asymmetry of the universe may be, in significant part, a consequence of this elementary fact operating at cosmological scale during the early universe.

---

## 2. Why This Has Not Been the Primary Framework for Sixty Years

In 1967, Andrei Sakharov identified three conditions that any successful theory of baryogenesis must satisfy:

1. Baryon number violation
2. C and CP symmetry violation
3. Interactions out of thermal equilibrium

These conditions, now known as the Sakharov conditions, have defined the landscape of baryogenesis research for six decades. They are necessary conditions derived from thermodynamic reasoning: if all three are not satisfied, any baryon asymmetry generated will be washed out by equilibrium processes.

The Sakharov conditions are necessary within their own framework. But they are not necessary conditions in general. They describe what is required to generate an asymmetry through particle-number-changing processes in thermal equilibrium. They say nothing about mechanisms that operate through spatial separation rather than number asymmetry.

The magnetic charge separation mechanism proposed here does not violate this logic. It operates in a different regime entirely. It does not require baryon number violation. It does not require CP violation beyond what already exists. It does not require fine-tuned departures from thermal equilibrium. It requires only that a non-zero primordial magnetic field existed during the epoch when pair production was the dominant process in the universe, and that this field separated the products of pair production before they could annihilate.

The reason this mechanism has not been the central focus of baryogenesis research is not that it is known to be insufficient. It is that the field organized itself around the Sakharov framework before the quantitative implications of large-scale magnetic charge separation were systematically explored. The framework became the question, and questions outside the framework were rarely asked.

---

## 3. The Physics of Magnetic Charge Separation

### 3.1 The Lorentz Force and Opposite Deflection

Consider a photon-photon collision producing an electron-positron pair:

γ + γ → e⁻ + e⁺

Both particles are produced at the same spatial point. In the presence of a magnetic field **B** directed along the z-axis, the Boris integrator — the standard algorithm used in GEANT4 and all major plasma physics PIC codes — updates the momentum of each particle according to:

t_c = (q · Δt/2) / (γm)

**t** = t_c · **B**

**p**⁻ = **p** + **p** × **t**

**s** = 2**t** / (1 + |**t**|²)

**p**_new = **p**⁻ + **p**⁻ × **s**

The rotation encoded in the cross products **p** × **t** and **p**⁻ × **s** reverses direction when q changes sign, because t_c = (q · Δt/2)/(γm) carries the sign of q directly. For the electron (q = -e), t_c is negative; for the positron (q = +e), t_c is positive. The rotation is in opposite senses for opposite charges.

This is not a numerical artifact. It is the exact discrete analog of the continuous Lorentz force. In the source code of the Yang-Mills Collider v3.2 (LHC_kerr_2.html), this appears as a single line:

```javascript
const tc = (charge * dt * 0.5) / (gam * mass);
```

The variable `charge` carries the sign. When `charge = +1`, the rotation goes one way. When `charge = -1`, it goes the other. There is no threshold. There is no minimum field strength. There is no special parameter combination required. The separation follows from the sign of a single variable in a single line of code that implements a law of physics verified to extraordinary precision.

### 3.2 The Inevitability of Separation

The separation of charges in a magnetic field is not an emergent phenomenon that requires careful tuning. It is a structural consequence of the Lorentz force. To prevent separation, one must set B = 0 exactly. Any departure from B = 0, in any direction, of any magnitude, causes particles and antiparticles to diverge.

This has a direct implication for the early universe: if a primordial magnetic field existed — of any non-zero strength — charge separation during pair production was not merely possible. It was unavoidable.

The quantitative questions (how efficient was the separation? what fraction survived? how large were the domains?) depend on the field strength, coherence length, and duration. But the qualitative question — did separation occur? — has only one answer if B ≠ 0: yes.

### 3.3 The Larmor Radius

The radius of the circular orbit traced by a charged particle in a magnetic field is the Larmor radius:

r_L = γmv_⊥ / (|q|B) = p_⊥ / (|q|B)

where:
- γ = (1 - v²/c²)^(-1/2) is the Lorentz factor
- m is the rest mass of the particle
- v_⊥ is the component of velocity perpendicular to **B**
- p_⊥ = γmv_⊥ is the transverse momentum
- |q| is the magnitude of the electric charge
- B is the magnetic field strength

The Larmor radius determines the scale of separation, not whether separation occurs. A larger B produces a smaller r_L and tighter, more confined orbits — meaning the particle and antiparticle are more efficiently confined to separate regions. A smaller B produces larger orbits that overlap more, reducing separation efficiency. But in both cases, the orbits wind in opposite directions. The separation exists at any B ≠ 0; the Larmor radius measures its spatial scale.

For ultrarelativistic particles where E ≈ pc:

r_L ≈ E_⊥ / (|q|Bc)

The mass hierarchy of particles is directly encoded in their separation scale: heavier particles have larger Larmor radii, and therefore trace wider, less confined orbits in the same field. Protons and antiprotons separate on scales 1836 times larger than electrons and positrons at the same energy.

### 3.4 Separation Efficiency vs. Separation Existence

It is important to distinguish two questions that are often conflated:

**Question 1 — Does separation occur?**
Answer: Yes, for any B ≠ 0. This follows directly from the Lorentz force and requires no additional conditions.

**Question 2 — How efficient is the separation?**
Answer: This depends on the ratio r_L / R_system. When r_L ≪ R_system, particles are tightly confined to separate orbital regions and the encounter rate between particle and antiparticle populations approaches zero. When r_L ~ R_system, the orbits are comparable to the system size and significant overlap occurs, reducing but not eliminating the separation effect.

The condition r_L ≪ R_system therefore governs separation efficiency, not separation existence. In the early universe, as shown in Section 5, the primordial field satisfies this condition with margins of many orders of magnitude.

### 3.5 The Cross Section for Annihilation and Its Suppression

In the absence of a magnetic field, the annihilation cross section for an electron-positron pair at low relative velocity v is given by the Dirac formula:

σ_ann = πr_e²(v/c)^(-1) · [1 + (1/2)(v/c)² + ...]

where r_e = e²/(m_e c²) ≈ 2.818 × 10⁻¹³ cm is the classical electron radius. The rate of annihilation events per unit volume is:

Γ_ann = n_+ · n_- · ⟨σ_ann v_rel⟩

In the charge-separated regime, the spatial overlap between the distributions of n_+ and n_- is reduced. In the limit of complete separation:

∫ n_+(r) · n_-(r) d³r → 0

and the annihilation rate falls to zero regardless of the magnitude of σ_ann. The magnetic field does not change the intrinsic annihilation cross section. It changes the geometry of the encounter, suppressing or eliminating the encounter entirely. This suppression begins as soon as B ≠ 0 and becomes more complete as B increases.

---

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

J_CP = Im[V_ud V_cb V_ub* V_cd*] ≈ 3 × 10⁻⁵

The baryon asymmetry generated by standard model CP violation in electroweak baryogenesis is suppressed relative to the observed asymmetry by a factor that can be estimated as:

η_SM ~ (α_w)² · (m_t/M_W)² · J_CP · (T_EW/M_Pl)² · ...

where α_w is the weak coupling constant, m_t is the top quark mass, M_W is the W boson mass, T_EW ~ 100 GeV is the electroweak phase transition temperature, and M_Pl ~ 10¹⁹ GeV is the Planck mass. The result is:

η_SM ~ 10⁻²⁰

The observed baryon-to-photon ratio is:

η_obs = (n_b - n_b̄) / n_γ ≈ 6.1 × 10⁻¹⁰

(from Planck 2018 CMB analysis, consistent with Big Bang Nucleosynthesis constraints)

The discrepancy:

η_obs / η_SM ~ 10⁻¹⁰ / 10⁻²⁰ = 10¹⁰

Standard model CP violation is ten orders of magnitude too small to account for the observed asymmetry. This is not a marginal failure. It is a catastrophic failure that has motivated decades of searches for physics beyond the standard model.

The magnetic charge separation mechanism does not need to explain this ten-order-of-magnitude gap through new CP violation. It proposes a different question entirely: not "how were more baryons created than antibaryons?" but "how were baryons and antibaryons separated before they could annihilate?"

### 4.3 The Magnitude of Separation Required

For the magnetic separation mechanism to explain the observed asymmetry, it does not need to achieve perfect separation. It needs to achieve a separation efficiency such that the surviving fraction of matter exceeds the surviving fraction of antimatter by the ratio:

(n_b - n_b̄) / n_b̄ ≈ η_obs / (1 - η_obs) ≈ 6.1 × 10⁻¹⁰

This is an extraordinarily small asymmetry. For every 10¹⁰ baryons that survived, approximately 10¹⁰ - 1 antibaryons were annihilated. The mechanism does not require efficient separation — it requires a barely detectable imbalance in the fraction of matter versus antimatter that escapes boundary regions between separated domains.

Given that separation begins at B ≠ 0 and that primordial fields are expected to be many orders of magnitude above any plausible minimum, the required asymmetry of one part in 10¹⁰ is, if anything, surprisingly modest.

---

## 5. Primordial Magnetic Fields: Observational Constraints and Theoretical Predictions

### 5.1 Current Observational Upper Limits

Several independent observational probes constrain the strength of cosmological magnetic fields at different epochs:

From CMB polarization B-modes at recombination (z ~ 1100):
B_CMB < 10⁻⁹ G (comoving)

From blazar observations and the non-observation of cascade emission (z ~ 0.1–1):
B_IGM < 10⁻¹⁵ G (for correlation lengths > 1 Mpc)

From gamma-ray observations of distant blazars (Fermi-LAT):
B_IGMF < 10⁻¹⁶ G (for coherence lengths ~ Mpc)

These are upper limits on the present-day (comoving) values. The physical field at earlier epochs was stronger by (1+z)² for a field that evolves adiabatically:

B_physical(z) = B_comoving · (1+z)²

### 5.2 Theoretical Predictions for Primordial Field Generation

From the electroweak phase transition (Vachaspati 1991, Baym et al. 1996):
B_EW ~ 10²³ G (physical, at T_EW ~ 100 GeV)

Equivalent in comoving units:
B_EW,comoving ~ 10²³ / (10¹⁵)² G = 10⁻⁷ G

From the QCD phase transition (T ~ 150 MeV):
B_QCD,comoving ~ 10⁻⁶ G

### 5.3 The Separation Condition in the Early Universe

The separation efficiency condition r_L ≪ R_system, evaluated at nucleosynthesis (T ~ 1 MeV, t ~ 1 second):

R_H(t=1s) = c·t ~ 3 × 10¹⁰ cm ~ 10⁹ m

For an electron with thermal energy E_e ~ 1 MeV:

p_⊥ ~ E_e/c ~ 5.3 × 10⁻²² kg·m/s

The field required for r_L ≪ R_H:

B_required ≫ p_⊥ / (e · R_H) ~ 3 × 10⁻¹² G (physical)

In comoving units:
B_required,comoving ≫ 3 × 10⁻³⁰ G

The ratio of predicted to required field:

B_EW,comoving / B_required,comoving ~ 10⁻⁷ / 10⁻³⁰ = 10²³

The predicted primordial fields exceed the minimum required for efficient charge separation by twenty-three orders of magnitude. The separation condition is not marginally satisfied. It is overwhelmingly satisfied.

More fundamentally: even this calculation concerns separation efficiency. The separation itself — the divergence of particle and antiparticle trajectories — requires only B ≠ 0. Given that the predicted primordial fields are 10²³ times the threshold for efficient separation, the existence of any separation at all is not in question.

---

## 6. Simulation Evidence: Yang-Mills Collider v3.2

### 6.1 The Structure of the Boris Integrator

The Yang-Mills Collider v3.2 (LHC_kerr_2.html) implements the Boris algorithm for relativistic charged particle motion. The core of the magnetic rotation step is:

```javascript
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
```

The variable `tc` carries the sign of `charge` directly. When `charge = +1` (positron, proton, etc.), `ty = tc * (-Bfield)` is positive for positive Bfield. When `charge = -1` (electron, antiproton, etc.), `ty` is negative. The cross products that follow rotate the momentum vector in opposite senses for opposite signs of `ty`. This is not conditional on any parameter threshold. It executes on every timestep for every charged particle as long as Bfield ≠ 0.

The black hole gravity code applies identically to all particles regardless of charge:

```javascript
const gAcc = logMass * 120.0 / (r2 + 1.0);
p.p4.px -= gAcc * (dx / r) * dt;
p.p4.py -= gAcc * (dy / r) * dt;
p.p4.pz -= gAcc * (dz / r) * dt;
```

There is no `charge` variable here. The gravitational acceleration is identical for particle and antiparticle. The black hole pulls both toward the same point with the same force. But the Boris integrator has already rotated their momenta in opposite senses, so they approach the black hole from geometrically opposite sides. The result — charge-separated populations on opposite sides of the gravitational center — is not a programmed outcome. It is the unavoidable geometric consequence of combining opposite-sense gyration with a common gravitational center.

### 6.2 The Condition for Separation: B ≠ 0 and M_BH > 0

A direct reading of the simulator code establishes the following:

Separation does NOT occur when:
- Bfield = 0 (exactly zero), or
- BH_MASS = 0 (no gravitational center)

Separation DOES occur for all other parameter combinations. There is no minimum field strength threshold in the code. There is no minimum black hole mass threshold. There is no special orientation or geometry required. The separation is a structural property of the system, not an emergent phenomenon requiring careful tuning.

To be explicit: the following parameter ranges all produce charge separation:

Bfield: any value > 0 (the simulator range is 0 to ~14 T, but the physics has no upper limit)
BH_MASS: any value > 0 (the simulator range spans many orders of magnitude)
BH_SPIN (a*): any value from 0 to 1 (spin affects disk morphology, not separation existence)
Collision energy √s: any value (the simulator default is 13,000 GeV)
Particle species: all 39 charged species in the PDG 2022 implementation

The only way to prevent separation is to deliberately set B = 0 or M_BH = 0. In the language of experimental design: this is not an experiment where you tune parameters to find a regime where separation occurs. It is an experiment where you must actively break the physics to prevent separation from occurring.

### 6.3 Observed Phenomena Across Parameter Space

**B = 0, any BH_MASS:**
All particles absorbed by the black hole without charge separation. With no magnetic force, particle and antiparticle trajectories are not distinguished. Both are pulled radially inward.

**B > 0, BH_MASS = 0:**
Charge separation occurs — particles and antiparticles diverge into opposite-sense helical trajectories — but without a gravitational center, the separated populations disperse throughout the simulation volume rather than forming a concentrated structure.

**B > 0, BH_MASS > 0, BH_SPIN = 0 (Schwarzschild):**
Charge separation occurs and both populations are gravitationally attracted to the black hole. They arrive from opposite sides and are absorbed or captured on opposite sides. No accretion disk forms because there is no frame-dragging to impart angular momentum.

**B > 0, BH_MASS > 0, BH_SPIN > 0 (Kerr):**
Charge separation occurs, both populations are attracted to the black hole, and frame-dragging (Lense-Thirring effect) imparts angular momentum, causing the captured populations to orbit rather than fall directly inward. An accretion disk forms spontaneously. No accretion disk code was written. The disk is a geometric consequence of the combination of opposite-sense gyration, common gravitational center, and frame-dragging.

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

---

# Section 7 (Reinforced): The Boundary Asymmetry Mechanism

**Scope note:** This section extends the qualitative framework of the original Section 7 with order-of-magnitude estimates derivable from current observational and theoretical constraints. All quantitative claims are explicitly labeled by their basis (observed / theoretical prediction / derived estimate). No claim is made beyond what current knowledge permits.

---

## 7.1 Domain Structure

If the early universe magnetic field drove charge separation, the result would be a universe divided into domains: regions dominated by matter separated from regions dominated by antimatter by boundary layers where the field reverses or weakens.

### 7.1.1 Domain Scale — Order-of-Magnitude Estimate

The coherence length of the primordial magnetic field, L_B, sets the characteristic domain scale. This is model-dependent, but current constraints permit a bounded estimate.

**From magnetohydrodynamic (MHD) evolution:**
A primordial field generated at the electroweak phase transition (T_EW ~ 100 GeV) evolves under MHD turbulence. The coherence length grows via inverse cascade:

L_B(t) ~ L_EW · (t/t_EW)^{2/3}

where L_EW is the initial correlation length at the electroweak scale.

**Observational constraint (Planck 2018 + Faraday rotation surveys):**
Current comoving upper limit on coherence length: L_B,comoving < 1 Mpc

**Lower bound from causality:**
At the electroweak phase transition (t_EW ~ 10^{-11} s), the Hubble horizon is:
R_H,EW ~ c · t_EW ~ 3 × 10^{-3} cm (physical)

The initial correlation length cannot exceed the Hubble horizon, so:
L_EW < 3 × 10^{-3} cm (physical at T_EW)

**Derived domain scale at nucleosynthesis (T ~ 1 MeV, t ~ 1 s):**
Scaling by MHD inverse cascade from T_EW to T_nucl:

L_nucl ~ L_EW · (t_nucl / t_EW)^{2/3}
       ~ 3×10^{-3} cm · (1 s / 10^{-11} s)^{2/3}
       ~ 3×10^{-3} · 10^{7.3} cm
       ~ 6 × 10^4 cm ~ 600 m (physical)

In comoving units (redshift factor ~10^9 from nucleosynthesis to today):
L_nucl,comoving ~ 600 m / 10^9 ~ 6 × 10^{-7} m ~ sub-micron scale today

**Status:** This is a derived estimate, sensitive to the MHD cascade model. The key point is not the precise value but the implication: domain scales at nucleosynthesis were many orders of magnitude smaller than the Hubble horizon (~3 × 10^{10} cm). There were approximately (R_H / L_nucl)^3 ~ (10^{10} / 10^5)^3 = 10^{15} domains within the observable horizon at nucleosynthesis. Even with imperfect separation, statistical averaging over 10^{15} domains strongly suppresses large-scale asymmetry — consistent with the observed uniformity of the CMB.

---

## 7.2 Asymmetric Annihilation at Domain Boundaries

At the boundaries between matter-dominated and antimatter-dominated domains, annihilation occurs as particles and antiparticles from adjacent domains encounter each other.

### 7.2.1 Annihilation Rate at the Boundary — Order-of-Magnitude Estimate

The annihilation rate per unit volume at a domain boundary:

Γ_ann = n_+ · n_- · ⟨σ_ann v_rel⟩

At nucleosynthesis (T ~ 1 MeV), the baryon number density is:
n_b ~ η_obs · n_γ ~ 6×10^{-10} · 10^{31} cm^{-3} ~ 2×10^{22} cm^{-3}

But we are concerned with the epoch before nucleosynthesis, when pair production was still active (T > m_e c^2 ~ 0.511 MeV, t < 1 s). At T ~ 1 MeV:
n_e ~ n_γ ~ (2ζ(3)/π²) T³ ~ 10^{31} cm^{-3}

The thermally-averaged annihilation cross section at v_rel ~ c:
⟨σ_ann v_rel⟩ ~ π r_e² c ~ π (2.8×10^{-13})² · 3×10^{10} ~ 7×10^{-16} cm³/s

The characteristic annihilation timescale at the boundary:
τ_ann ~ 1 / (n_e · ⟨σ_ann v_rel⟩) ~ 1 / (10^{31} · 7×10^{-16}) ~ 10^{-16} s

This is much shorter than the Hubble time at that epoch (t_H ~ 1 s at T ~ 1 MeV). This confirms that any particle and antiparticle that physically encounter each other will annihilate essentially instantaneously — reinforcing that separation must be spatial, not temporal.

### 7.2.2 Required Boundary Asymmetry — Derived from η_obs

The required surviving asymmetry is:

(n_b - n_{b̄}) / n_{b̄} ≈ η_obs ~ 6.1 × 10^{-10}

This can be recast as a geometric constraint on domain boundaries.

Consider two adjacent domains of size L (one matter, one antimatter) separated by a boundary layer of thickness δ. The fraction of particles within distance δ of the boundary is:

f_boundary ~ δ / L

For the asymmetry to survive, annihilation must be incomplete — meaning either:
(a) The boundary layer thickness δ is small compared to L, limiting the fraction that annihilates, or
(b) Annihilation at the boundary produces an asymmetric flux, with more antimatter than matter crossing from one domain to the other.

**Constraint from η_obs:**
If fraction f_ann of each domain annihilates at the boundary symmetrically, and a fraction ε > 0 more antimatter than matter is destroyed:

Net surviving asymmetry ~ ε · f_ann ~ η_obs ~ 6 × 10^{-10}

For f_ann ~ 1 (most boundary material annihilates):
ε ~ 6 × 10^{-10}

This means an asymmetry of just one part in 1.6 × 10^9 in the boundary annihilation rate is sufficient. This is a surprisingly weak condition — well within the range of small physical effects such as:

- Asymmetric diffusion coefficients (electrons diffuse faster than protons by factor ~√(m_p/m_e) ~ 43)
- Thermal gradients from asymmetric magnetic energy dissipation
- CP violation at the domain interface (even the known SM CP violation of ~10^{-5} exceeds the required ~10^{-10} by five orders of magnitude when applied locally at the boundary)

**Status:** The required boundary asymmetry is derivable from η_obs. Its magnitude (one part in ~10^9–10^{10}) is so small that multiple known physical effects are individually sufficient to produce it. This does not prove the mechanism worked — it demonstrates the required condition is not stringent.

---

## 7.3 Upper Bound on Surviving Antimatter — Observational Constraint

If this mechanism operated, regions of antimatter must exist somewhere. Current observational constraints bound the scale of these regions.

**From the diffuse gamma-ray background (COMPTEL/INTEGRAL/Fermi):**
No excess 511 keV annihilation radiation has been observed beyond our galactic center and cosmic ray sources. This constrains bulk antimatter regions to:

R_anti > 10 Mpc (comoving)

meaning any surviving antimatter domains must be larger than ~10 Mpc in size today — otherwise the annihilation boundary would produce observable gamma-ray flux.

**From Big Bang Nucleosynthesis (BBN):**
BBN is sensitive to baryon-to-photon ratio η at the epoch of nucleosynthesis. Spatial variations in η from domain inhomogeneity are constrained by the observed uniformity of primordial helium abundance:

δη/η < 0.1 on scales < 100 Mpc (comoving)

**Implication:**
If surviving antimatter domains exist, they are either:
(a) Larger than ~10 Mpc (beyond current observational reach), or
(b) Completely annihilated before the present epoch

Both outcomes are consistent with the mechanism. The observational null result does not falsify the mechanism — it constrains the domain size.

**Status:** This is a genuine constraint, not a free parameter. If future surveys (SKA, Fermi-LAT extended) detect anomalous 511 keV emission on Mpc scales, it would strongly support this mechanism. Non-detection on scales below 10 Mpc is consistent with but does not require the mechanism.

---

## 7.4 Summary: What Current Knowledge Permits Us to Claim

The following table distinguishes what is known, what is derived, and what remains open.

| Claim | Basis | Status |
|---|---|---|
| Separation occurs for any B ≠ 0 | Lorentz force law | Certain |
| Predicted primordial fields exceed separation threshold by 10^{23} | Vachaspati 1991, Section 5 | Theoretical prediction (well-established models) |
| Domain scale at nucleosynthesis ~ 10^5 cm | MHD inverse cascade estimate | Order-of-magnitude estimate (model-dependent) |
| Number of domains within Hubble horizon ~ 10^{15} | Derived from domain scale | Order-of-magnitude estimate |
| Required boundary asymmetry ~ 6 × 10^{-10} | Derived from η_obs | Exact (from Planck 2018) |
| Required asymmetry is weaker than known SM effects | Comparison with known CP violation | Derived comparison |
| Surviving antimatter domains, if any, are > 10 Mpc | COMPTEL/INTEGRAL/Fermi constraints | Observational constraint |
| Quantitative efficiency under realistic early-universe conditions | Not calculated | Open question |
| Detailed domain interface dynamics | Not derived | Open question |

---

## 7.5 What This Section Does Not Claim

This reinforced section does not claim:

- That the mechanism produced exactly η_obs = 6.1 × 10^{-10}. It claims the required asymmetry is small enough that multiple known physical effects are individually sufficient to produce it.

- That the domain scale estimate (Section 7.1.1) is precise. It is an order-of-magnitude estimate based on MHD cascade models. The coherence length evolution is model-dependent.

- That surviving antimatter domains do not exist. Current observations constrain their minimum size, not their existence.

- That the magnetic separation mechanism is the sole or dominant contributor to the observed baryon asymmetry. It may be one of several contributing mechanisms.

The claims made are: (1) the mechanism exists and operates for any B ≠ 0, (2) the required asymmetry is quantitatively small by the standards of known physics, and (3) current observational constraints are consistent with the mechanism rather than excluding it.

These three claims are supportable from current knowledge. Everything beyond them is labeled as open.

---

## 8. Relation to the Passive Layer Framework

The magnetic charge separation mechanism connects directly to the Passive Layer framework. In that framework, pair production in strong magnetic fields around black holes produces particle-antiparticle pairs that are separated by the Lorentz force and survive without annihilating. These surviving pairs contribute to the effective mass near the black hole through the additional term in the mass evolution equation:

dM_BH/dt = Ṁ_in + Ṁ_pair - Ṁ_out - Ṗ_Hawking/c²

The term Ṁ_pair represents mass creation through pair production and magnetic separation. This term has not been systematically quantified in the existing astrophysics literature.

The baryon asymmetry mechanism described in this document is the cosmological version of the same process: pair production in the primordial magnetic field, followed by charge separation and survival, applied not to the local environment of a single black hole but to the entire early universe. The Passive Layer framework and the baryogenesis mechanism are two scales of the same underlying physics.

---

## 9. Falsifiable Predictions

### 9.1 Primordial Magnetic Field Detection

If this mechanism operated, a non-zero primordial magnetic field must have existed. The minimum required comoving field strength for any separation at all is B > 0. For efficient separation (r_L ≪ R_H at nucleosynthesis), the required comoving field is:

B_comoving ≫ 3 × 10⁻³⁰ G

Current and near-future observational programs (Square Kilometre Array, CMB-S4) will constrain primordial magnetic fields at the level of:

B_comoving ~ 10⁻¹¹ G

If primordial fields are detected at or above 10⁻¹¹ G, this strongly supports the viability of the separation mechanism. Detection at any level above zero is sufficient for separation to occur; detection above 10⁻³⁰ G comoving is sufficient for efficient separation.

### 9.2 Antimatter Domain Signatures

Boundaries between matter and antimatter domains would produce:

(a) A contribution to the diffuse gamma-ray background at E ~ m_e c² ~ 0.511 MeV (electron-positron annihilation) and E ~ m_p c² ~ 938 MeV (baryon-antibaryon annihilation).

(b) A potential distortion of the CMB spectrum if boundary annihilation occurred after recombination.

(c) Modification of Big Bang Nucleosynthesis yields in domain boundary regions, potentially observable as spatial variations in the primordial helium abundance.

### 9.3 Laboratory Test: Charge Separation in Strong Fields

The mechanism predicts that in any environment with B ≠ 0 and a gravitational or electromagnetic confinement center, pair production will be followed by observable charge separation. The specific prediction is: the spatial distribution of produced electrons and positrons should show separation in the direction determined by the magnetic field orientation, with separation distance scaling as:

Δx ~ r_L = p_⊥ / (eB)

This is directly testable at existing high-intensity laser facilities (ELI-NP, XCELS) where pair production in laser-laser collisions has been observed. The test requires only B ≠ 0 — not a specific minimum field value.

---

## 10. Limitations and Open Questions

**10.1 Quantitative Efficiency Not Calculated**

The fraction of pair-produced particles that survive without annihilating in a realistic primordial magnetic field geometry — accounting for field inhomogeneity, coherence length limitations, turbulent mixing, and the expansion of the universe — has not been calculated. The separation exists for any B ≠ 0; its quantitative efficiency under realistic early-universe conditions requires magnetohydrodynamic simulation at cosmological scales.

**10.2 Domain Scale Uncertainty**

The coherence length of the primordial magnetic field, which determines the scale of matter-antimatter domains, is highly model-dependent.

**10.3 Asymmetric Annihilation Rate Not Derived**

The claim that boundary annihilation produces an asymmetry of order η_obs ~ 6 × 10⁻¹⁰ has been argued on qualitative grounds. A quantitative derivation requires detailed modeling of the matter-antimatter interface dynamics.

**10.4 Coexistence with Sakharov Mechanisms**

This mechanism does not exclude the possibility that Sakharov-type baryogenesis also occurred. The two mechanisms could have operated simultaneously, with additive contributions to the observed baryon asymmetry.

---

## 11. Conclusion

The matter-antimatter asymmetry of the observable universe may not require baryon number violation, exotic CP violation, or any new physics. It may require only that the early universe contained a magnetic field of any non-zero strength — which is predicted by essentially every model of early-universe physics — and that this field separated particle-antiparticle pairs produced during the epoch of pair creation before they could annihilate.

The physical mechanism is not subtle. The Lorentz force F = q(v × B) acts in opposite directions on opposite charges. This has been verified to extraordinary precision for over a century. The Boris integrator that implements this law in the Yang-Mills Collider v3.2 simulator encodes the charge sign in a single variable, `tc = (charge * dt * 0.5) / (gam * mass)`, and the opposite rotation that results is a direct and unavoidable consequence of that sign. There is no threshold. There is no special regime. There is no parameter combination within B ≠ 0 for which separation fails to occur.

The question is not whether separation occurs in a magnetic field. It does, by definition, for any B ≠ 0. The question is whether the scale, efficiency, and domain structure of that separation in the early universe was sufficient to produce the observed baryon-to-photon ratio of 6.1 × 10⁻¹⁰. Given that the predicted primordial field strengths exceed the minimum required for efficient separation by twenty-three orders of magnitude, and given that the required asymmetry is as small as one part in ten billion, the answer to this question is not obviously no.

The standard model CP violation fails by ten orders of magnitude to produce the observed asymmetry. The magnetic separation mechanism, operating on the same pair-produced populations, requires no new physics, no new particles, and no parameter that is not already constrained by existing theory and observation. The only requirement is that the early universe was not magnetically empty.

There is no evidence that it was.

---

## Appendix A: Derivation of the Larmor Radius in the Relativistic Case

For a relativistic charged particle of rest mass m, charge q, moving with velocity **v** in a uniform magnetic field **B** = Bẑ, the relativistic equation of motion is:

d(γm**v**)/dt = q(**v** × **B**)

Since the magnetic force does no work, **v** · **F** = q**v** · (**v** × **B**) = 0, and γ is constant in a pure magnetic field. Therefore:

γm(dv_x/dt) = qv_y B   →   dv_x/dt = ω_c v_y
γm(dv_y/dt) = -qv_x B  →   dv_y/dt = -ω_c v_x

where the relativistic cyclotron frequency is:

ω_c = |q|B / (γm)

The solution is circular motion with radius:

r_L = v_⊥/ω_c = γmv_⊥ / (|q|B) = p_⊥ / (|q|B)

For a particle with charge -q (antiparticle), ω_c changes sign:

ω_c,anti = -|q|B / (γm) = -ω_c

The antiparticle gyrates in the opposite sense, with identical Larmor radius but reversed handedness. This reversed handedness is the mathematical foundation of charge separation: the same equations of motion, with only the sign of q changed, produce orbits that wind in opposite directions around the same magnetic field axis.

---

## Appendix B: The Boris Integrator and Charge Sign

The Boris algorithm advances charged particle trajectories in electromagnetic fields. Its key property relevant here is that the sign of the charge q enters directly and exclusively through the factor:

t_c = (q · Δt) / (2γm)

All subsequent operations — the half-rotation vectors **t**, the cross products, the final momentum update — are determined by this single signed scalar. Changing q → -q is equivalent to changing **t** → -**t**, which reverses the sense of the rotation in all three cross products simultaneously.

In the Yang-Mills Collider v3.2 source code:

```javascript
const tc = (charge * dt * 0.5) / (gam * mass);
const tx = 0, ty = tc * (-Bfield), tz = 0;
```

With Bfield > 0 and charge = +1: ty < 0
With Bfield > 0 and charge = -1: ty > 0

The cross products that follow rotate in opposite senses for these two cases. This is not a special feature of the simulator — it is the correct physical behavior, and it is present in every correct implementation of charged particle motion in a magnetic field.

The conclusion is unavoidable: in any system correctly implementing the Lorentz force, particles and antiparticles gyrate in opposite senses in a magnetic field. Separation is not a result to be achieved. It is a result to be prevented — and it can only be prevented by setting B = 0.

---

## Appendix C: Observational Evidence for Magnetic Fields in AGN Environments

The Event Horizon Telescope (EHT) Collaboration (2021) reported measurements consistent with ordered magnetic fields in the emission region of M87*. Faraday rotation measurements yield:

Rotation measure RM ~ 10⁵ rad/m² (near the photon ring)

Combined with the estimated electron density n_e ~ 10⁴–10⁵ cm⁻³:

B_ISCO ~ 1–30 G (at the innermost stable circular orbit)

The Larmor radius of a relativistic electron (γ ~ 10⁶) in B ~ 10³ G:

r_L = γm_e c² / (eBc) ~ 10⁻¹ cm

The ISCO radius of M87*:

r_ISCO(M87*) ~ 6 × 10¹⁴ cm

The ratio:

r_L / r_ISCO ~ 10⁻¹ / 10¹⁴ = 10⁻¹⁵

The charge separation efficiency condition is satisfied by fifteen orders of magnitude in the directly observed environment of the nearest supermassive black hole. This is not a theoretical prediction. It is a direct implication of current observations.

---
