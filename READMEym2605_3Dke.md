A Relativistic Particle Collider, Built in Pure JavaScript — Making the Yang-Mills Collider
A relativistic particle physics simulator in pure JavaScript
B. Sun | Seoul Inside
Jun 03, 2026

A few days ago, I asked myself a strange question.

“Could I just run a CERN particle collider in the browser?”

The short answer — yes. Quite seriously, too.

🔗 Try it yourself →

It Started with Simple Curiosity
The original code looked like a particle physics simulator, but under the hood the physics were fairly simple. Particles flew in straight lines, the magnetic field only affected the x and z directions, and decays just fired off in random directions.

“What if I put real physics in here?” That thought was the beginning of this project.

What Actually Happens Inside the LHC
At CERN’s LHC (Large Hadron Collider), two protons collide head-on at nearly the speed of light. The energy released at the moment of collision can reach up to 13.6 TeV — roughly 14,500 times the rest mass of a proton, all concentrated at a single point.

From that collision, hundreds of new particles are born in an instant. Pions, kaons, muons, electrons — each with different masses and charges, flying off in every direction. Inside a powerful solenoid magnetic field (about 3.8 Tesla), each one traces its own helical path.

The detector measures the curvature of these paths to calculate momentum. Even with the same charge, heavier particles curve gently while lighter ones curve sharply.

Reproducing this in the browser was the goal.

The Physics Engine: What’s Under the Hood
1. Special Relativity — “Nothing Can Exceed the Speed of Light”
This was the first problem to solve. Conventional game physics engines use Newtonian mechanics: F = ma. Apply a force continuously and velocity increases without limit.

But inside the LHC, protons travel at 99.9999991% of the speed of light. Newtonian mechanics breaks down completely at these speeds.

The solution is the Lorentz factor γ (gamma):

γ = E / m = 1 / √(1 - v²/c²)
As velocity approaches the speed of light, γ grows explosively — the same force produces less and less acceleration. Every particle in this simulator passes through this formula. No particle can exceed the speed of light.

2. Boris Integrator — The Same Method Used by GEANT4
Numerically computing the motion of a particle in a magnetic field is trickier than it sounds. A naive implementation lets energy slowly leak out, causing the spiral to gradually grow or shrink — a real error.

The Boris Integrator is the algorithm that solves this problem. It’s the standard method used in CERN’s GEANT4 and plasma physics PIC codes. The key idea is to split the magnetic rotation into two half-rotations:

p⁻ = p + p × t      ← first half-rotation
p⁺ = p⁻ + p⁻ × s   ← second half-rotation
This method conserves energy precisely while reproducing helical trajectories. As a result, in this simulator you can see positively charged particles curving counterclockwise and negatively charged ones curving clockwise — exactly as in a real detector.

3. The Bethe-Bloch Formula — Different Particles Slow Down Differently
Inside an LHC detector, particles lose energy as they pass through the detection material. The Bethe-Bloch formula calculates this energy loss:

-dE/dx ≈ K · z² / β² · [ln(2mₑβ²γ² / I) - β²]
The key point is that this loss differs for each particle. Light electrons lose energy quickly and trace short spirals. Heavy muons punch through almost the entire detector, leaving long straight tracks. This difference is visible in the simulator.

4. Decay Branching Ratios — π⁺ Doesn’t Always Decay the Same Way
This was personally the most fascinating part.

The positively charged pion (π⁺) is an unstable particle — it decays into other particles almost immediately after being created. But it doesn’t always decay the same way.

Decay Mode Probability π⁺ → μ⁺ + νμ 99.99% π⁺ → e⁺ + νe 0.01%

It almost always decays into a muon, but roughly once in every 10,000 times it decays into an electron instead. These values are actual experimental measurements from the PDG (Particle Data Group).

This simulator implements those probabilities exactly. Run enough collisions and you’ll occasionally see a rare decay flagged separately in the event log. When it happens, it’s genuinely exciting.

5. 4-Momentum Conservation — Physics Laws Hold Even During Decay
The directions and velocities of particles produced in a decay are determined by 4-momentum conservation. First, the decay direction is calculated in the parent particle’s rest frame (CM frame), then transformed to the lab frame via a Lorentz boost.

As a result, high-energy particle decays are collimated (concentrated forward), while low-energy decays spread more isotropically. It’s a moment where the laws of physics naturally visualize themselves.

6. αs(μ) — The Strong Force Coupling That Changes with Energy
One of the most remarkable features of QCD (Quantum Chromodynamics) is asymptotic freedom: at higher energies, the strong force between quarks actually becomes weaker. This was the discovery that earned the 2004 Nobel Prize in Physics.

This simulator calculates αs(μ) in real time using the 1-loop beta function:

αs(MZ) = 0.1181  ← actual measured value at the Z boson mass
Move the collision energy (√s) slider and αs changes — and that value determines how many particles are produced in the collision. At 13 TeV (LHC scale), hundreds of particles; at 20 GeV, tens — trends consistent with real experimental data.

Two Versions
3D Version (Three.js) Particles trace three-dimensional helices inside a solenoid ring. Freely rotate the view with your mouse. Adjust magnetic field strength and collision energy in real time.

2D Dashboard Version The same physics engine, with QCD analysis tools added. Divided into three levels:

LV.1 Analytic — Instant 1-loop αs(μ) calculation

LV.2 Monte Carlo — PDF-sampled 2→2 parton scattering, pT distributions

LV.3 Heavy Ion — Pb+Pb collisions via the Glauber model, QGP formation condition analysis

Yang-Mills Theory and the Millennium Problem
This project takes its name from Yang-Mills theory — the mathematical foundation of QCD, published in 1954 by C.N. Yang and R.L. Mills.

The theory contains an unsolved mathematical problem: the Mass Gap Problem. There is still no rigorous mathematical proof of why quarks cannot exist in isolation, or why the strong force only acts over short distances.

This is one of the 7 Millennium Prize Problems selected by the Clay Mathematics Institute. Solve it and you win $1,000,000. It remains unsolved.

Closing Thoughts
The most striking thing about building this project was the realization that formulas written on paper decades ago run just as well in a browser today.

The Bethe-Bloch formula dates to the 1930s. The Boris Integrator was published in 1970. Asymptotic freedom in αs was discovered in 1973.

These equations are still running at CERN today — and right now, in this browser.

🔗 Launch the 3D Simulator →

Physics Engine Summary
Component Description Relativistic Motion Lorentz factor γ = E/m applied; speed of light cannot be exceeded Boris Integrator Standard numerical integration used in GEANT4 and PIC codes Bethe-Bloch Energy loss formula based on particle mass, charge, and velocity 4-Momentum Conservation CM frame 2-body decay followed by Lorentz boost Branching Ratios π⁺→μ⁺νμ (99.99%) vs e⁺νe (0.01%) and other PDG values αs(μ) Running Coupling 1-loop β function with quark flavor thresholds Monte Carlo PDF sampling, 2→2 parton scattering, pT distributions Glauber Model Heavy-ion collisions, Ncoll, ε₀, QGP formation conditions Helix Trajectories Accurate curvature under solenoid magnetic field

The code is publicly available on GitHub. Feedback and questions are always welcome.
# ⚛️ Yang-Mills Collider — Full Physics Simulation

> **A browser-based particle physics simulator implementing relativistic dynamics, QCD running coupling, and realistic decay chains — entirely in vanilla JavaScript.**

🔗 **Live Demo (3D):** [xur94-maker.github.io/SeoulInside/ym2605_3D.HTML](https://xur94-maker.github.io/SeoulInside/ym2605_3D.HTML)

---

## 🇰🇷 한국어 소개

브라우저에서 실행되는 입자물리 시뮬레이터입니다. CERN LHC에서 일어나는 양성자 충돌을 물리적으로 최대한 정확하게 재현하는 것을 목표로 합니다.

### 구현된 물리 엔진

| 항목 | 내용 |
|------|------|
| **상대론적 운동** | 로런츠 인자 γ = E/m 적용, 광속 초과 불가 |
| **Boris Integrator** | GEANT4·PIC 코드에서 표준으로 쓰이는 수치 적분법 |
| **Bethe-Bloch** | 질량·전하·속도에 따른 에너지 손실 공식 |
| **4-운동량 보존** | CM frame 2체 붕괴 후 로런츠 부스트 |
| **분기비(Branching Ratio)** | π⁺→μ⁺νμ (99.99%) vs e⁺νe (0.01%) 등 PDG 실제 값 |
| **αs(μ) 달리기 결합상수** | 2-loop β함수, 쿼크 맛 문턱값 포함 |
| **Monte Carlo** | PDF 샘플링, 2→2 파톤 산란, pT 분포 |
| **Glauber 모형** | 중이온 충돌, Ncoll, ε₀, QGP 형성 조건 |
| **나선(Helix) 궤적** | 솔레노이드 자기장 하에서 정확한 곡률 |

### 파일 구성

```
SeoulInside/
├── ym2605_3D.HTML        # Three.js 3D 시뮬레이터
└── collider_v2D1.html    # 2D 대시보드 (QCD 엔진 + 캔버스 애니메이션)
```

---

## 🌐 English

A particle physics simulator running entirely in the browser. It aims to physically reproduce proton collisions as they occur at the CERN LHC.

### Physics Engine

**Relativistic Dynamics**
All particles obey special relativity. The Lorentz factor γ = E/m is applied at every integration step, making it impossible for any particle to exceed the speed of light.

**Boris Integrator**
The same symplectic integration method used in GEANT4 and plasma PIC codes. It conserves energy exactly under a magnetic field, producing accurate helical trajectories for charged particles.

```
p⁻ = p + p × t          ← half-rotation
p⁺ = p⁻ + p⁻ × s        ← remaining half-rotation
position: x += (p/γm)·dt
```

**Bethe-Bloch Energy Loss**
```
-dE/dx ≈ K·z²/β² · [ln(2mₑβ²γ²/I) - β²]
```
Heavier particles lose less energy per unit length; light particles (electrons) spiral inward rapidly.

**4-Momentum Conserving Decay**
Two-body decays are computed in the center-of-momentum frame and Lorentz-boosted back to the lab frame. Kinematically forbidden decays (insufficient mass) are automatically rejected.

**Branching Ratios (PDG values)**

| Decay | Branch | Probability |
|-------|--------|-------------|
| π⁺ → μ⁺ νμ | dominant | 99.99% |
| π⁺ → e⁺ νe | rare | 0.01% |
| K⁺ → μ⁺ νμ | dominant | 63.56% |
| K⁺ → π⁺ π⁰ | — | 20.67% |
| K⁺ → π⁺ π⁺ π⁻ | — | 5.59% |
| μ⁻ → e⁻ ν̄e νμ | — | 100% |

**Running Coupling αs(μ)**
2-loop renormalization group equation with active quark flavor thresholds (mc, mb, mt). The multiplicity of produced particles is determined by αs(√s/2) — higher energy collisions produce more particles, consistent with KNO scaling.

**Monte Carlo (Level 2)**
Parton distribution functions (PDF) are sampled using importance sampling. 2→2 partonic scattering (gg → gg) is simulated with realistic pT power-law distributions.

**Glauber Model (Level 3)**
Heavy-ion collisions (Pb+Pb) are modeled using the optical Glauber approach. Outputs include Ncoll, Npart, initial energy density ε₀, QGP formation condition (ε > 2 GeV/fm³), initial temperature T_init, and elliptic flow coefficient v₂.

### Particle Database

| Particle | Mass (GeV) | Charge | Lifetime |
|----------|-----------|--------|----------|
| p (proton) | 0.938272 | +1 | stable |
| π⁺ / π⁻ | 0.139570 | ±1 | 2.2 s* |
| π⁰ | 0.134977 | 0 | 0.1 s* |
| K⁺ / K⁻ | 0.493677 | ±1 | 1.6 s* |
| μ⁺ / μ⁻ | 0.105658 | ±1 | 2.8 s* |
| e⁻ / e⁺ | 0.000511 | ±1 | stable |
| γ (photon) | 0 | 0 | — |
| νe, νμ (neutrino) | ≈ 0 | 0 | invisible |

*scene-scaled lifetimes

### Tech Stack

- **Vanilla JavaScript** — no physics library
- **Three.js r128** — 3D rendering
- **Canvas 2D API** — 2D dashboard
- **OrbitControls** — interactive camera

---

## 📐 Yang-Mills & The Mass Gap

This simulator is named after **Yang-Mills theory**, the mathematical foundation of QCD (Quantum Chromodynamics) — the theory of the strong nuclear force. The **mass gap problem** asks why the lowest-energy excitation of a Yang-Mills field has strictly positive mass (i.e., why free quarks are never observed). It is one of the **seven Millennium Prize Problems** and remains **UNSOLVED**.

---

## 📄 License

MIT License — © 2026 xur94-maker  

Feel free to use, fork, or modify. Attribution appreciated.
