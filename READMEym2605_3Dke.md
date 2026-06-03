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
