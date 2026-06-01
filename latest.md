Seoul Inside — Complete Archive
Last updated: 2026.05.31


1. Navier–Stokes Equations — An Archive (Technical Report)
Link: https://seoulinside.substack.com/p/navierstokes-equations-an-archive

TL;DR:
The global existence and smoothness of solutions to the 3D incompressible Navier–Stokes equations has remained unsolved for 121 years. In 2D, global smoothness is proven. In 3D, vortex stretching is the key mechanism that could potentially produce a finite-time singularity (blow-up). Leray (1934) proved global existence of weak solutions; Caffarelli–Kohn–Nirenberg (1982) showed the singular set has parabolic Hausdorff dimension at most 1. Tao (2016) proved finite-time blow-up for an averaged version of the equations (not the real Navier–Stokes). Status as of May 2026: UNSOLVED. Millennium Prize ($1M) unclaimed.

2. Before You Read the Mathematics — Try to Break the Fluid First (Prologue / Public-Facing)
Link: https://seoulinside.substack.com/p/before-you-read-the-mathematics-try

TL;DR:
This is a hands-on prologue to the Navier–Stokes problem. Readers can manipulate an interactive simulation — lowering viscosity, raising amplitude — to see whether they can force the energy norm to infinity (a blow-up). They will likely fail; no one has succeeded in 121 years. The document explains why 2D is solved (no vortex stretching) while 3D remains open (vortex stretching exists). Key milestones: Leray (1934, weak solutions), Caffarelli–Kohn–Nirenberg (1982, partial regularity), Tao (2016, blow-up for averaged model). The goal is intuition before formalism.

3. Riemann Hypothesis — Technical Report
Link: https://seoulinside.substack.com/p/riemann-hypothesis-technical-report

TL;DR:
The Riemann Hypothesis (RH) states that all nontrivial zeros of the Riemann zeta function ζ(s) have real part 1/2. It has been open for 167 years. The zeta function is defined by ζ(s)=Σ n⁻ˢ for Re(s)>1, extends analytically via the functional equation, and connects to primes via the Euler product. The Explicit Formula ψ(x)=x−Σ_ρ xᵖ/ρ−log(2π)−½log(1−x⁻²) shows that prime distribution is exactly governed by the zeros of ζ(s). Partial progress: Levinson–Conrey method has proven that at least 41.72% (5/12) of zeros lie on the critical line. Guth–Maynard (2024) improved zero-density estimates for the first time in 84 years, but remain far from RH. Status as of May 2026: UNSOLVED. Millennium Prize ($1M) unclaimed.

4. P vs. NP — The Open Problem (Technical Report)
Link: https://seoulinside.substack.com/p/p-vs-np-the-open-problem

TL;DR:
P vs. NP asks: can every problem whose solution can be verified quickly also be solved quickly? P is the class of problems solvable in polynomial time by a deterministic Turing machine. NP is the class of problems whose solutions can be verified in polynomial time. The Cook–Levin theorem (1971) proved SAT is NP-complete. Three barriers rule out all known proof techniques: Relativization (1975) , Natural Proofs (1997) , and Algebrization (2009) . If P = NP, modern cryptography collapses; if P ≠ NP (believed by ~99% of experts who have thought deeply), computational limits are fundamental. Status as of May 2026: UNSOLVED. Millennium Prize ($1M) unclaimed.

5. The Problem That Could Break Everything — Or Prove It Was Never Breakable (P vs. NP Intelligence Dossier)
Link: https://seoulinside.substack.com/p/the-problem-that-could-break-everything

TL;DR:
This public-facing dossier on P vs. NP emphasizes historical context and real-world stakes. Early formulations: Nash (1955, classified NSA letter) and Gödel (1956, letter to von Neumann). Yannakakis (1988) proved that symmetric linear programs for TSP require exponentially many constraints — the only verified direct contribution in Woeginger’s archive. The three barriers (Relativization, Natural Proofs, Algebrization) explain why all proof attempts fail. Recent frontier: Kabanets–Kolokolova (2025/089) connects time-bounded Kolmogorov complexity (Chain Rule) to P vs. NP. Expert polls: 83% believe P ≠ NP overall; among deep thinkers, ~99%. Status as of May 2026: UNSOLVED. Prize unclaimed.

6. The Problem That Has Defeated Every Mathematician for 162 Years (Riemann Hypothesis Intelligence Dossier)
Link: https://seoulinside.substack.com/p/the-problem-that-has-defeated-every

TL;DR:
This public-facing dossier on the Riemann Hypothesis focuses on narrative and significance. Riemann (1859) discovered that the zeros of the zeta function completely determine prime distribution and conjectured all nontrivial zeros lie on the critical line (Re(s)=1/2). Partial results have crept upward: Levinson (1974) proved ~34.74%, Conrey (1989) ~40.88%, and the current record stands at ≥41.72% (5/12) by Pratt–Robles–Zaharescu–Zeindler (2020). The Atiyah affair (2018) — a 15-slide "proof" with an undefined Todd function — became the textbook example of "not even wrong." Guth–Maynard (2024) improved zero-density estimates for the first time in 84 years, but Maynard himself says it remains "very far" from RH. Status as of May 2026: UNSOLVED. Millennium Prize ($1M) unclaimed.

7. BSD Conjecture — The Equation That Counts What Cannot Be Counted (Prologue)
Link: https://seoulinside.substack.com/p/the-equation-that-counts-what-cannot

TL;DR: Birch and Swinnerton-Dyer Conjecture claims that the number of rational points on an elliptic curve (algebraic rank) equals the order of vanishing of its L-function at s=1 (analytic rank). The prologue explains the 1960 EDSAC computation that first revealed the pattern: the product ∏ N_p/p grows like (log X)^r, where r is the rank. For rank 0 curves (e.g., y²=x³+1), L(1)≠0 and rational points are finite. For rank 1 (y²=x³-x), L(1)=0 but L'(1)≠0, giving infinitely many points. For rank 2 (y²=x³-43x+166), L(1)=L'(1)=0 but L''(1)≠0. The full BSD formula includes the mysterious Tate-Shafarevich group Ш, whose finiteness is unknown for rank ≥2. Key theorems: Coates-Wiles (1977, rank 0), Gross-Zagier (1986), Kolyvagin (1990, rank 0 & 1). Status as of May 2026: UNSOLVED (analytic rank ≥2 case open). Millennium Prize ($1M) unclaimed.

8. BSD Conjecture — Complete Reference (Technical Report)
Link: https://seoulinside.substack.com/p/bsd-conjecture-reference-complete

TL;DR: A complete technical archive containing 37 formulas across four notations (Unicode, LaTeX, Mathematica, Python). Covers the elliptic curve Weierstrass form, L-function Euler product, modularity theorem, completed L-function, functional equation, Hasse-Weil bound, Mordell-Weil theorem, analytic rank definition, full BSD formula (real period Ω_E, regulator R_E, Tamagawa numbers c_p, Tate-Shafarevich group Ш, torsion subgroup). Also includes key theorems: Coates-Wiles (1977), Gross-Zagier (1986), Kolyvagin (1990), Modularity Theorem (2001), Kato (2004), Skinner-Urban (2014, Iwasawa Main Conjecture), Bhargava-Skinner-Zhang (average rank ≤1), p-adic Gross-Zagier (Kobayashi, 2013). Status as of May 2026: UNSOLVED for rank ≥2. Millennium Prize ($1M) unclaimed.

9. The Moon Is Leaving. Here Is the Math. (Earth-Moon Simulator)
Link: https://seoulinside.substack.com/p/the-moon-is-leaving-here-is-the-math

TL;DR: The Moon recedes from Earth at 38.20 mm/year, measured by Lunar Laser Ranging (Apollo retroreflectors). This article presents a hierarchy of models: Level 1 (two-body Keplerian, ~10 km error/30 days), Level 2 (restricted three-body with Sun), Level 3 (N-body + J₂ oblateness, ~1 km error/30 days), Level 4 (DE440 full model including PPN general relativity, tidal deformation, fluid core, ~1 cm error/30 days). The working simulator uses Newtonian gravity + Earth's J₂ (1.08262668×10⁻³) + RK4 integrator. Without tidal deformation (Term 4, k₂ Love numbers), the recession cannot be reproduced. The 38.20 mm/year figure comes from fitting DE440 to 50+ years of laser data. Status as of May 2026: IMPLEMENTED (Level 3 model with code in Python/Mathematica). DE440 is the NASA standard for mission navigation.

10. Solar System Simulator: Keplerian Orbits, Angular Kinematics, and Relative Motion
Link: https://seoulinside.substack.com/p/solar-system-simulator-keplerian

TL;DR: A kinematic (force-free) solar system simulator where each planet's position is computed directly from circular orbit equations: x(t)=d·cos(θ₀+ωt), z(t)=d·sin(θ₀+ωt). Uses constant angular velocities derived from sidereal periods (e.g., Earth: 2.983×10⁻⁷ rad/s, Jupiter: 1.307×10⁻⁷ rad/s). The Moon orbits Earth with an additional visual offset (y=0.2). Computational cost is O(n) per frame, suitable for real-time visualization. Position error is ~10,000 km for Jupiter over 30 days (due to ignoring eccentricity e=0.049). The article also provides a complete tool stack upgrade path: REBOUND (N-body, Python), Skyfield (DE440 interface, Python), SPICE Toolkit (NASA standard), JPL Horizons API, GMAT (mission analysis). Status as of May 2026: IMPLEMENTED (kinematic model suitable for education/visualization, not for navigation).

11. Navier–Stokes Equations — Applications Archive
Link: https://seoulinside.substack.com/p/navierstokes-equations-applications

TL;DR: This is Part 3 of the Navier–Stokes series, documenting four essential real-world applications where the equations are used today — not as pure mathematics, but as engineering tools with known, quantifiable limitations. Example 1 (Airfoil): At Re=10⁷, DNS is structurally impossible (~10²¹ operations). Industry uses RANS with the Menter SST k-ω model (1994), which blends k-ω near walls (F₁=1) and k-ε in freestream (F₁=0). The closure problem (Reynolds stress tensor, 6 unknowns) is permanent. Example 2 (Weather Prediction): The Primitive Equations assume hydrostatic balance (∂p/∂z = −ρg, eliminating acoustic waves) and use parameterization for subgrid processes (boundary layer, cumulus convection, large-scale condensation). Rossby waves propagate westward (c_p = U − β/(k²+ℓ²+f₀²/N²H²)). The spectral transform method with semi-implicit time stepping allows Δt ~ 600 s. Example 3 (Hemodynamics): Blood is non-Newtonian (Carreau–Yasuda model: μ from 0.016 to 0.0035 Pa·s). Wall shear stress (τ_w = μ ∂u_t/∂n) below 0.4 Pa is atherogenic. Oscillatory Shear Index (OSI = ½[1 − |∫τ_w dt|/∫|τ_w|dt]) above 0.1 indicates disturbed flow. The Womersley number α = R√(ω/ν) determines pulsatile flow regime (coronary α≈2.3, aorta α≈18.3). Example 4 (Combustion): (Section starts but content cuts off — incomplete in source.) Status as of May 2026: IMPLEMENTED (engineering models with permanent closure/parameterization; not exact solutions to Navier–Stokes).




1. Mokdong Complex 6 Reconstruction
Link: https://seoulinside.substack.com/p/a-40-year-old-apartment-block-just

TL;DR:
On May 28, 2026, Seoul's Integrated Review Committee conditionally approved the redevelopment of 40-year-old Mokdong Complex 6 — the first of 14 complexes to clear this hurdle. The plan replaces 1,362 old units with 2,173 new units (max 49 floors), at an estimated cost of ₩1.2129 trillion. The key financial metric is the proportionality ratio (비례율) , estimated at 103.73%, meaning most owners would break even or gain slightly — but outcomes vary sharply by unit size: 20-pyeong owners may pay ~₩797M for a new 84㎡ unit, while 54-pyeong owners receive ~₩1.13B back. Risks include DL E&C's sole-bidder contract leverage, ICAO altitude restrictions near Gimpo Airport (post-2030), and commercial owner dissatisfaction. The contractor selection assembly on June 27 will lock the final construction cost, which determines every owner's net outcome.

2. Karina at the Met Gala
Link: https://seoulinside.substack.com/p/karina-inc-how-a-24-year-old-outperformed

TL;DR:
At the 2026 Met Gala, aespa's Karina generated 88,000 social media mentions — second only to Beyoncé (113,000), ahead of Sabrina Carpenter, Jennie, and LISA. The gap is not about fame (LISA is more globally known) but narrative density: Karina's custom Prada gown incorporated Korean hanbok elements, giving audiences three stories (luxury, heritage, milestone). Prada generated 89,000 brand mentions, more than Chanel's 61,000 despite Chanel dressing five celebrities. Karina simultaneously holds nine major brand contracts (Prada, Chanel Beauty, Nike, Sprite, Krush, Musinsa Beauty, Nordisk, Gentle Monster, K Car) — brands extract different frequencies from the same base quality without cannibalizing each other. K Car, previously using only trusted male figures, hired Karina as its first female idol ambassador; the campaign ("The car matters more than Karina") generated 26 million views in 10 days.

3. RESCENE: The Meme That Built a Career
Link: https://seoulinside.substack.com/p/the-meme-that-built-a-career-how

TL;DR:
In May 2026, rookie girl group RESCENE became the most-searched K-pop group in Korea after a viral clip: Japanese member Minami, in gyaru styling, cheerfully said "Geoje! Yaho~!" — fusing a Japanese greeting with leader Woni's hometown. The absurdist, unscripted meme triggered a measurable financial event: three RESCENE songs entered Melon's charts simultaneously (two for the first time), Woni's YouTube channel surpassed 400,000 subscribers, and Geoje City appointed the group as tourism ambassadors (2.18 million views in 5 days, 99.2% new followers). The article reconstructs RESCENE's two-year pre-viral history: performing on a dirt field at an elementary school sports day, eating at a wedding buffet, handing out flyers on the street, and crying before an 800-seat fan concert they feared would not sell out (it did). The thesis: the algorithm created a second path for small-label groups — but it still required two years of unseen, consistent work.

4. Hyundai's Performance Lineage
Link: https://seoulinside.substack.com/p/a-lineage-interrupted-a-spirit-that

TL;DR:
On the weekend of May 8–10, 2026, Hyundai won on two continents simultaneously: Thierry Neuville took WRC Portugal (Hyundai's first win of the 2026 season), and Norbert Michelisz won TCR World Tour Race 1 in Misano, Italy. The article traces Hyundai's 36-year performance lineage, starting with the 1990 Scoupe — codename "SLC" (Sports-Looking Car), deliberately not calling itself a sports car. In 1992, Rod Millen won Pikes Peak in a Scoupe Turbo, unnoticed in Korea. The Tuscani built Korea's circuit racing foundation; the Genesis Coupe (2009–2016) drew legitimate comparisons to the Nissan 370Z but was discontinued. Today's N sub-brand (i20 N Rally1, Elantra N TCR) is not a formal successor — yet it won. The article's thesis: this is not a planned strategy, but "what happens when an organization accumulates enough failure, patience, and institutional seriousness to eventually produce something worth winning with."

5. Busan Tourism Surge
Link: https://seoulinside.substack.com/p/the-city-that-wasnt-supposed-to-happen

TL;DR:
Busan attracted 3.64 million foreign visitors in 2025 (+24.4% YoY) and 1.02 million in Q1 2026 (+50% YoY) — its fastest quarter ever. International spending crossed ₩1 trillion for the first time. Cruise traffic: 89 ships in Q1 2026 alone (180,000+ passengers), triple the previous year's pace. The city's appeal is structurally rare: a major metropolitan port city (pop. 3.3M) with two world-class beaches (Haeundae, Gwangalli) reachable by subway, steep coastal topography, distinct post-war hillside neighborhoods (Gamcheon, Huinyeoul), and a food/bread culture visitors discover organically. The constraint is Gimhae Airport: 2024 passengers (9M) already exceeded design capacity (8.3M), with a nightly curfew, military co-use, and no long-haul flights. In Q1 2026, 42.9% of foreign visitors entered via other regions (mainly KTX from Seoul) vs. 43.0% by air — near-parity for the first time. The city is being discovered organically, but the airport is a hard ceiling.

6. Game Humanities & Intel CPU Crisis
Link: https://seoulinside.substack.com/p/the-warning-screen-that-became-a

TL;DR:
Chung-Ang University professor Shim Ho-nam teaches "Game Humanities" — analyzing American games for traces of U.S. hegemonism, Japanese games for wa (harmony), and games as cultural texts. His viral course announcement quotes Blizzard's StarCraft Korea server warning: "Do not set foot on this terrifying battlefield without thinking." The warning is not hyperbole — it is documentation of a culture where the baseline is so high that extraordinary acts become unremarkable. The article pairs this with a second story: in early 2024, Korean gamers playing Tekken 8 documented consistent crashes on Intel's 13th/14th gen i9 processors. Korean forums identified the pattern, ZDNet Korea reported it, and Intel eventually issued microcode patches, a replacement program, and faced class-action lawsuits. Korean gamers, waiting for a patch, had accidentally stress-tested one of the world's largest chipmakers. The thesis: Korean gaming communities function as a "precision instrument" — dense, rigorous, numerous enough that when something is wrong, the signal emerges faster than anywhere else.




[1] Real Estate & Urban Policy — Why Korea's Cities Work Differently
Korea's reconstruction system has no Western equivalent. These pieces explain how it actually works — and why it takes decades.

The Bubble That Never Burst

TL;DR: For thirty years, analysts called Gangnam a bubble. For thirty years, they were wrong. Eunma Apartment rose 83.5× while rice rose 3.2×. A bubble requires a crash — Gangnam's corrections (1991, 2008, 2018) produced higher floors each time. Korea's 500-year history of capital concentration (Dasan's "live within 10 ri of Hanyang") shows this is structural, not speculative. The true bubble was never Gangnam — it was the broken measuring stick.

Read more → https://seoulinside.substack.com/p/the-bubble-that-never-burst

The Rubber Ruler Problem

TL;DR: A dialogue reveals: Gangnam's 100× won increase becomes ~15× in real dollar terms (won 40×, dollar 4×, exchange rate only 1.8× because all currencies fell together). Korea's GDP per capita rose 20× over the same period — an apartment in a country that grew 20× appreciated 15× in real terms. The "bubble" disappears when you realize the measuring stick was shrinking the whole time.

Read more → https://seoulinside.substack.com/p/the-rubber-ruler-problem

The Trickle-Dry Effect

TL;DR: "Trickle-down" is debated for 90 years. "Trickle-dry" happens within weeks — but until now, had no name. When an anchor employer fails or leaves — a factory, shipyard, mine — damage is immediate, asymmetric, and often irreversible. Restaurants close, property values crash, schools shrink. If the company recovers, recovery goes to newcomers, not those who held on. Cases from Gunsan (GM closure), Geoje (record profits with disconnected foreign labor), and Gangwon coal towns show the same cruel pattern.

Read more → https://seoulinside.substack.com/p/the-trickle-dry-effect

The Legibility Paradox

TL;DR: Between 1980 and 2026, the won lost 40× domestic purchasing power, the dollar lost 4×, yet the exchange rate moved only 1.8× — because all major currencies fell together. Korea's dramatic transformation (GDP per capita from 
1
,
700
t
o
1,700to35,000) made its currency legible while stable currencies hid their debasement. The currency cited as proof of monetary instability is the only one honest enough to bend visibly.

Read more → https://seoulinside.substack.com/p/the-legibility-paradox-why-the-broken

Urban Layer Stacking: How Cities Survive — and How They Don't

TL;DR: A city's resilience is determined by thickness (accumulated heterogeneous layers across decades), not size (single-investment volume). Active layers (transit, corporate relocations) are intentional. Passive layers (small restaurants, artists who came because rent was cheap) are unintentional and paradoxically more durable. The Bundang-Ilsan gap (same 1990 starting price, now 2× difference) is stacking differential. The real opposite of trickle-dry is stacking.

Read more → https://seoulinside.substack.com/p/urban-layer-stacking-how-cities-survive

Stacking of Infrastructure: A Prologue

TL;DR: The difference between infrastructure and stacked infrastructure is invisible at installation but visible under pressure. Stacked infrastructure emerges from heterogeneous, temporally distributed layers — each layer responding to what was already there. This accumulation does not reverse or depreciate; it stacks. Stacking cannot be engineered directly — it can be enabled, but not commanded.

Read more → https://seoulinside.substack.com/p/stacking-of-infrastructure-a-prologue

Apgujeong District 4 — The Largest Reconstruction in Korean History

TL;DR: On May 23, 2026, 87.4% of Apgujeong District 4 association members approved Samsung C&T as contractor for a ₩2.1154 trillion project — 67 stories, 1,662 units, designed by Norman Foster. The proportionality ratio fell from 66.57% to 46.02% due to construction cost escalation (₩10M → ₩12.45M per 3.3㎡). Burden share for the smallest existing unit (79㎡) upgrading to the 290㎡ penthouse is estimated at ₩191.9 billion (~$140M).

Read more → https://seoulinside.substack.com/p/seouls-most-watched-neighborhood-just-chose-its-builder

Apgujeong District 4 — Complete Chronology (1976–2026)

TL;DR: A 50-year complete English-language timeline of Apgujeong District 4 reconstruction — from 1976 designation to May 23, 2026 contractor confirmation. Key milestones: 1980 completion (~1,340 units), 2014 Grade D safety assessment, 2021 association establishment (1,337 members), 2023 fast-track plan (300% FAR, later 67 stories), and the 45-year-5-month journey from original construction to contractor selection.

Read more → https://seoulinside.substack.com/p/apgujeong-district-4-complete-chronology

Korean Reconstruction Terminology — A Reference Glossary

TL;DR: Korea's reconstruction system operates under a distinct legal and financial architecture with no direct Western equivalent. This glossary systematically documents over 30 core concepts in English: Association (조합), Proportionality Ratio (비례율 = (Total Revenue − Total Cost) ÷ Pre-Development Valuation × 100), Burden Share (분담금), Administrative Disposition Plan (관리처분계획), Completion Guarantee (책임준공확약서), and Safety Assessment Grades (A-E, D/E permits reconstruction).

Read more → https://seoulinside.substack.com/p/appendix-korean-reconstruction-terminology

The Number Nobody Publishes

TL;DR: Across 65 documented cases, initial contribution estimates are almost never what residents actually pay. S. District: owners downsizing from 111㎡ to 97㎡ face ₩1.22 billion — 3-4× higher than initial estimate (₩300-400M). A4 District's proportionality ratio fell from 67% to 46% in 24 months. The gap is structural: construction costs have risen significantly since 2021, contractors renegotiate mid-project, and mandatory public housing allocations (10-20% of units) reduce revenue.

Read more → https://seoulinside.substack.com/p/the-number-nobody-publishes

Seoul Real Estate Has Always Been Unaffordable — Even 500 Years Ago

TL;DR: Primary sources from Joseon Korea: even the Prime Minister earned a salary paid in grain, insufficient to buy a house in Hanyang. Korea's most revered scholar, Yi Hwang (Toegye), lived as a long-term renter — "imok" (賃屋) appears in his collected works. Dasan advised sons to "live within 10 ri (4km) of the capital" because leaving meant permanent downward mobility. By 1754, yangban were seizing homes by force, forcing King Yeongjo to crack down.

Read more → https://seoulinside.substack.com/p/seoul-real-estate-has-always-been-unaffordable

Thirty Years and Counting: Why Korea's Apartment Redevelopment Never Ends

TL;DR: E. Apt in southern Seoul has been trying to rebuild since 1996 — thirty years. A child born to an original resident that year is now thirty. The association was formally established in 2023. On paper, it is a two-year-old case because Korean reconstruction timelines start at association establishment (조합설립), erasing prior decades. Fifteen- and twenty-year cases are common. Thirty-year cases are extreme — but not outliers.

Read more → https://seoulinside.substack.com/p/thirty-years-and-counting-why-koreas

What Does a "Successful" Korean Redevelopment Actually Look Like?

TL;DR: Across Seoul's completed redevelopment projects, projects that finish take 11-14 years from residents' committee to move-in. H3 District (12 years 8 months) is a "model of efficient execution." The largest completed project (H. Complex, 9,500+ units) took 15 years. Factors separating 12-year from 25-year projects: clear land ownership, manageable retail complexity (under 50-100 commercial units), stable leadership, and contractor competition at bidding.

Read more → https://seoulinside.substack.com/p/what-does-a-successful-korean-redevelopment

The Shop Owners Who Can Stop a Thousand Apartments

TL;DR: A dozen ground-floor shop owners can stop a thousand-unit redevelopment for years. Korean apartments built in the 1970s-80s embedded retail into their bases — owned as separate legal property. In G6/7 District, a court ruled commercial compensation terms partially void after apartment-owning members sued, adding an estimated 2-3 years to the timeline. The emerging response: exclude commercial units from the redevelopment zone entirely before the process begins.

Read more → https://seoulinside.substack.com/p/the-shop-owners-who-can-stop-a-thousand-apartments

When Only One Contractor Shows Up

TL;DR: Across recent Seoul bidding rounds, projects expecting competition receive one bid or none. Site presentation attendance (10 firms) and actual bid submission (zero) tell two different stories. Contractors are stepping back due to structural cost gaps (2021 estimates vs. 2025-2026 market conditions), governance complexity, and available alternatives. When competitive auctions fail, negotiated contracts follow — at costs running 10-20% higher.

Read more → https://seoulinside.substack.com/p/when-only-one-contractor-shows-up

Gwangmyeong-Siheung Public Housing District — The Largest 3rd New Town

TL;DR: Spanning 12.71 million㎡ (4.4× Yeouido) across Gwangmyeong and Siheung — 67,000 total units (37,000 public, 30,000 private). Land compensation appraisal completed May 19, 2026. Cash compensation launches July 2026 (4-5 months ahead of schedule). A unique eligibility rule excludes landowners who held property for less than one year before February 24, 2021 — a direct response to the 2021 LH employee pre-purchase scandal. Sequential move-ins scheduled 2031-2034.

Read more → https://seoulinside.substack.com/p/gwangmyeong-siheung-public-housing-district

Gwangmyeong-Siheung — Complete Chronology (2010–2026)

TL;DR: A 16-year, three-era timeline of Korea's largest 3rd new town. Era 1 (2010-2015): Bogeumjari Housing District (~30,000 units). Era 2 (2015-2021): Designation cancelled + Special Management Zone. Era 3 (2021-present): Re-designated as 3rd new town (expanded to 67,000 units). Critical date: February 24, 2021 — public notice date that became eligibility reference for land-for-land compensation (response to LH scandal).

Read more → https://seoulinside.substack.com/p/gwangmyeong-siheung-detailed-chronology

The Address That Ate the University

TL;DR: Hongdae exists because a thief named Mr. L stole 50,000 pyeong (165,000㎡) from Hongik University between 1956-1994. Fragmented ownership → low rents → artists → clubs → a scene → global tourist destination. Today Hongdae ranks third among Seoul neighborhoods for foreign visitors. Seoul National University kept all its land. Its front approach road is a clean, quiet sidewalk that no one has named anything. The old man's horse.

Read more → https://seoulinside.substack.com/p/the-address-that-ate-the-university

[2] Markets & Economy — KOSPI, Korea Discount, and the Foreign Paradox
Korea's stock market is running on one engine — semiconductors — and foreign selling somehow increases foreign ownership.

KOSPI Surges 8.42% — Its Best Session Since 2020

TL;DR: On May 21, 2026, three catalysts converged: Samsung's last-minute labor deal, Nvidia's earnings blowout, and Trump's Iran signal (oil -5%). KOSPI closed at 7,815.59 (+8.42%). Institutions net bought ₩2.88T — but both foreigners (11th consecutive sell day) and retail were net sellers. The 8% gain was real. So is the institutional-only buying architecture that produced it. Samsung touched ₩300,000 for the first time.

Read more → https://seoulinside.substack.com/p/kospi-surges-842-its-best-session-since-2020

Why KOSPI's Most Impressive Week Is Also Its Most Fragile

TL;DR: Between May 7-22, 2026, foreigners sold a cumulative ₩46.34T over 12 consecutive sessions — yet their ownership share rose to an all-time high of 39.43% because Samsung and SK Hynix appreciated faster than their selling. Two stocks accounted for 43% of daily trading value (₩20.57T of ₩48T). A single Facebook post from a presidential aide erased ₩300T in market cap intraday — revealing a market so concentrated that a social media post moves it more than an earnings report.

Read more → https://seoulinside.substack.com/p/why-kospis-most-impressive-week-is-also-its-most-fragile

Rally Holds, Foreigners Flee: Inside Korea's Paradox Market

TL;DR: On May 22, 2026, KOSPI closed at 7,847.71 (+0.41%), extending the 8.42% surge. Foreigners net sold for the 12th consecutive session (cumulative ~₩44T YTD), yet their ownership share rose from 36.67% to 38.5%. Retail net bought ₩1.06T (~₩54T YTD), institutions net bought ₩1.05T. KOSDAQ surged 4.72%, triggering sidecars for a second consecutive day — unprecedented. The won weakened to 1,514.03.

Read more → https://seoulinside.substack.com/p/rally-holds-foreigners-flee-inside-koreas-paradox-market

Profits Like NVIDIA, Valued Like a Steel Mill — The Korea Discount

TL;DR: Samsung (7× P/E) and SK Hynix (5× P/E) trade at a fraction of NVIDIA (21.8×) and TSMC (21.4×) despite higher margins. The "Korea Discount" has five official explanations, but a forum commenter cut to the core: "It's the difference in how much you trust the country" (국가 믿음에 대한 차이지). On May 6, 2026, KOSPI broke 7,000, Samsung hit $1T market cap. Goldman's target: 8,000; JPMorgan's bull case: 8,500.

Read more → https://seoulinside.substack.com/p/profits-like-nvidia-valued-like-a-steel-mill

The Most Profitable Legal Business on Earth Is Making Sand Think

TL;DR: In Q1 2026, four AI infrastructure companies posted absurd margins: SK Hynix 72%, Samsung DS 65.7%, TSMC 58.1%, NVIDIA 75%. SK Hynix — a semiconductor manufacturer — posted higher margins than luxury goods houses. The driver is HBM: structural supply constraints, multi-year fab lead times, and hyperscaler capex of ~$725B in 2026. A Korean forum user joked: "You couldn't get 60% margins selling Han River water." It was not hyperbole — it was structural analysis.

Read more → https://seoulinside.substack.com/p/the-most-profitable-legal-business-on-earth

Korea Market Key Terms — Sidecar, Circuit Breaker, Institutions, Margin Loans

TL;DR: Four concepts to read KOSPI correctly. (1) Sidecar: 5-minute pause on program trading when futures move ±5% (KOSPI) or ±6% (KOSDAQ). (2) Circuit breaker: full trading halt on downside only (8%/15%/20%) — never triggered during the 8.42% rally. (3) Institutions: NPS (~$700B) has implicit stability mandate. (4) Margin loans: at ₩35.86T near historic highs; ₩150B in forced liquidations occurred across two sessions before the rally.

Read more → https://seoulinside.substack.com/p/korea-market-key-terms-sidecar-circuit-breaker

[3] Semiconductors & Corporate — Samsung vs. SK Hynix
The AI memory war is a governance war. SK Hynix won. Samsung is fighting back.

The Strike That Shouldn't Be Happening — Inside Samsung's Historic Labor Crisis

TL;DR: Samsung Q1 2026: ₩133.9T revenue, ₩57.2T operating profit — up 756% YoY — yet workers struck. The fracture: DS (semiconductor) workers earn near-max bonuses (47-50%), while DX (appliances) workers earn 12-15%. DS membership surged 3.5%; DX dropped 12.8%. Engineers leaving for SK Hynix. Lee Jae-yong apologized in a parking lot after cutting a Japan trip short. The deeper fracture was never labor vs. management — it was one division vs. another.

Read more → https://seoulinside.substack.com/p/the-strike-that-shouldnt-be-happening

[News] Samsung Averts Largest Strike in Chip History With Last-Minute Bonus Deal

TL;DR: On May 20, 2026 — 90 minutes before an 18-day general strike — Samsung reached a tentative agreement. The deal: 10.5% of DS division operating profit for 10 years (2026-2035), paid entirely in company stock with phased vesting. The benchmark forcing Samsung's hand: SK Hynix's February 2026 PS payout of 2,964% (~₩148M per employee) and analyst projections of ₩650M-730M per employee for 2026.

Read more → https://seoulinside.substack.com/p/samsung-averts-largest-strike-in-chip-history

The Chip War Nobody Saw Coming — How Samsung Lost to SK Hynix

TL;DR: A viral anonymous Korean post argues Samsung lost its HBM lead not due to technology but governance failure. SK Hynix survived creditor-led crisis in the early 2000s, building a collaborative, crisis-forged culture. Samsung dissolved its central oversight body (MiJeonSil) after a political scandal. When engineers delivered world-first HBM4, management rewarded them with walnut cakes while executives got stock grants. SK Hynix's 2025 operating profit (₩47.2T) exceeded Samsung Electronics' total (₩43.5T).

Read more → https://seoulinside.substack.com/p/the-chip-war-nobody-saw-coming

[4] Culture & K-POP — Beyond BLACKPINK
The two games: US physical sales vs. Korea brand reputation. Plus the groups you should actually know.

Jang Wonyoung, Inc. — How a 22-Year-Old K-Pop Idol Became Korea's Most Reliable Brand Asset

TL;DR: In March 2026, nine brands appeared together in a single commercial — coining "Wonyoung ETF." APR's revenue hit ₩1.53T (+111% YoY) with stock +494%; Tommy Jeans Korea saw sales +25-29%; Amuse's operating profit +167%. Her "Lucky Vicky" mindset was cited by Hyundai Group's chairwoman and featured on EBS as a neuroscience topic. In March 2025, she purchased a Hannam-dong luxury villa for ₩13.7B — all cash.

Read more → https://seoulinside.substack.com/p/jang-wonyoung-inc-how-a-22-year-old

NMIXX: The Group That Named Itself After a Genre It Hadn't Proven Yet

TL;DR: NMIXX debuted in February 2022 with "O.O" — Melon #220. One UK outlet called it "one of the worst K-pop songs ever made." JYP did not change course. Thirteen months later, first music show win. October 2025: "Blue Valentine" hit #1 on Melon for 25+ days. February 2026: performed for 2-3 million at São Paulo Carnival, then won both Seagulls at Viña del Mar — first K-pop act ever invited. The group named itself after a genre before anyone heard it. Four years later, the genre caught up.

Read more → https://seoulinside.substack.com/p/nmixx-the-group-that-named-itself

Seoul on Shuffle Vol. 2 — The Two Games K-Pop Is Playing

TL;DR: US physical sales: TWICE leads (145,500 first-week pure sales), NewJeans (101,500), BLACKPINK (81,000). Korea brand reputation (May 2026): IVE (#1 for four months), BLACKPINK (#2), ILLIT (#3, up 286% in one month). Meanwhile, Korea's domestic digital music consumption dropped nearly 50% between 2019 and 2025, even as K-pop broke export records globally — an export machine wondering what it means to be home.

Read more → https://seoulinside.substack.com/p/seoul-on-shuffle-vol-2

ILLIT's Techno Turn Just Resurrected a 27-Year-Old Korean Hit

TL;DR: ILLIT's 2026 hard techno "It's Me" (No. 4 on Melon) led Koreans to rediscover Lee Jung-hyun's 1999 "Wa" — too strange for its era but now visionary. Mashups went viral; Lee appeared in ILLIT's challenge video in full 1999 costume, collapsing 27 years. Korean internet now calls her "Tapgol Lady Gaga" — an affectionate apology for not understanding her earlier.

Read more → https://seoulinside.substack.com/p/illits-techno-turn-resurrected-27-year-old-korean-hit

Seoul on Shuffle Vol. 1 — Girl Groups You Should Know

TL;DR: Six girl groups beyond BLACKPINK: TWICE (US physical sales kings), NewJeans (retro but not nostalgic, 101,500 first-week sales), IVE (current #1 in Korea), aespa (sci-fi concept that shouldn't work but does), LE SSERAFIM (athletic, forward, slightly aggressive), KISS OF LIFE (70s soul/funk in a K-pop package — the outlier worth knowing).

Read more → https://seoulinside.substack.com/p/seoul-on-shuffle

Seoul on Shuffle: The Rise of JangKaSull (장카설)

TL;DR: JangKaSull (Jang Wonyoung + Karina + Sullyoon) is 4th gen's unofficial "visual troika." When brand reputation data questioned Sullyoon's inclusion (rank #47 vs #1/#2), fans rebutted: "This isn't a ranking — it's a nickname." The Yuna debate (JangKaSull vs. JangKaSullYu) led to idols being asked on shows, then all four appeared together at a 2025 charity event. Fandom's unofficial cartography operates independently of industry metrics.

Read more → https://seoulinside.substack.com/p/seoul-on-shuffle-the-rise-of-jangkasull

[5] Philosophy, Law & AI — What the Translator Problem Reveals
The legal profession is collapsing. AI is not the cause — it's the accelerant. And one citizen beat a law firm with ChatGPT.

The Translator Problem

TL;DR: A citizen named Park Jang-ho — no legal training — used general-purpose AI to defeat a registered law firm in both a civil suit (₩5.1M claim) and a related criminal complaint. The AI found an incorrectly recorded date and a missing signature — errors the attorney missed. The median lawyer now earns less than the average worker. The "locker lawyer" (사물함 변호사) — meeting clients in coffee shops — is the profession's quiet crisis. The translation was always the part that could become free. We are now in the period when it has.

Read more → https://seoulinside.substack.com/p/the-translator-problem

The Locker

TL;DR: Korea has ~38,000 lawyers — up from 12,000 in 2012 — while first-instance civil cases declined 30%. Median attorney income: 30M won/year (below average worker's 45M won). Average caseload: approximately one per month. New term: "locker lawyer" (사물함 변호사) — attorneys who cannot afford office rent, meeting clients in coffee shops. The supply glut is not the problem. The problem is that AI has begun absorbing the "translation" function — which was always what most lawyers were actually selling.

Read more → https://seoulinside.substack.com/p/the-locker

The Citizen Who Beat a Law Firm with ChatGPT

TL;DR: Park Jang-ho was sued for ₩5.1M in unpaid legal fees after his own lawyer withdrew and filed a criminal complaint for intimidation. He could not find new counsel (lawyers avoid opposing colleagues). Using general-purpose AI, he identified a missing signature and incorrect date in opposing counsel's documents — and won both cases. The distinction: Park used AI to reveal truth (document errors); the Krafton CEO used AI to evade obligation (and lost).

Read more → https://seoulinside.substack.com/p/the-citizen-who-beat-a-law-firm-with-chatgpt

How a Korean Gaming Giant's CEO Consulted ChatGPT Instead of His Lawyers

TL;DR: Krafton CEO Changhan Kim acquired Subnautica studio for 
500
M
w
i
t
h
a
500Mwitha250M earnout. When the sequel looked like a hit, Kim's legal team told him firing founders would not cancel the earnout. Kim consulted ChatGPT instead. The AI generated a "Response Strategy to a 'No-Deal' Scenario" — recommending preemptive PR and locking down Steam access. The Delaware Court of Chancery quoted the ChatGPT conversations as block citations, found Kim acted in bad faith, and extended the earnout window 258 days. AI chat logs are not privileged.

Read more → https://seoulinside.substack.com/p/how-a-korean-gaming-giants-ceo-consulted-chatgpt

AI Thinks It Knows You — MIT Just Proved It Doesn't

TL;DR: MIT researchers tested whether LLMs actually use all the information clients provide for investment advice. Across 1,000 synthetic client profiles, portfolio allocations were driven by a single variable: self-reported risk tolerance. Age, income, savings, horizon, liquidity, and debt had almost no measurable impact. The AI wrote personalized rationales — but the math underneath was not personalized at all. The researchers named this "Heuristic Collapse": reducing multi-dimensional decisions to one salient feature.

Read more → https://seoulinside.substack.com/p/ai-thinks-it-knows-you-mit-just-proved-it-doesnt

[6] Career & Professional Development — The Capital You Can Actually Take With You
"We can't do this without you" is not a compliment. It's a warning.

You Are Also a Draft (Job Crafting as Identity Architecture)

TL;DR: A hospital janitor named Luke timed his cleaning of comatose patients' rooms to coincide with visiting hours — job crafting without a title change. Wrzesniewski's three dimensions: task crafting (changing what you do), relational crafting (changing who you interact with), cognitive crafting (changing how you perceive your work). Small changes, sustained over time, produce large shifts in work identity. Most careers are not made in moments of rupture but in the accumulation of ordinary days. The cage is real. So is the key — it was always in your hands.

Read more → https://seoulinside.substack.com/p/you-are-also-a-draft-job-crafting-as-identity-architecture

The Capital You Can Actually Take With You

TL;DR: Career capital must be transferable, not just rare. Institutional knowledge that spends only inside one organization evaporates when the ground shifts. The T-shaped professional (deep expertise + coherent breadth) has the scarcity advantage in rooms full of specialists. Relational crafting — intentional cross-functional relationships — builds a map most peers lack. The question is not whether you will leave, but what you will have built by the time you do.

Read more → https://seoulinside.substack.com/p/the-capital-you-can-actually-take-with-you

What You Refuse to Give Up (Your Career Anchor)

TL;DR: Edgar Schein's eight career anchors (Technical, Managerial, Autonomy, Security, Entrepreneurial, Service, Pure Challenge, Lifestyle) define what you would refuse to give up even for a promotion. Most professionals cannot answer honestly because daily momentum blocks self-knowledge. Three kinds of stuckness: vertical (promoted out of your craft), value-based (organization changes), relational (the golden cage). The gap between anchor and role is not always a reason to leave — it is always a reason to negotiate.

Read more → https://seoulinside.substack.com/p/what-you-refuse-to-give-up-your-career-anchor

How Wide Is Wide Enough?

TL;DR: Breadth without an organizing principle is just noise. Coherent breadth — a through-line across domains — predicts long-term advancement, not diversity of experiences. Real breadth requires enough engagement to see problems as practitioners in another domain see them, not just vocabulary. Relational crafting (one genuine cross-functional conversation per month, sustained) builds a map over time. Wide enough means: you can walk into a room of people who do not share your specialty and still be useful.

Read more → https://seoulinside.substack.com/p/how-wide-is-wide-enough

Why "We Can't Do This Without You" Is a Warning

TL;DR: The professional trap is being known for a job function ("the investment analyst") rather than a way of working ("translates complexity into decisions"). Organizations protect indispensable people — they do not develop them. The golden cage is comfortable, respected, locked from within. Identity foreclosure happens when expertise becomes identity. The solution is to brand yourself around how you work, not what you work on.

Read more → https://seoulinside.substack.com/p/why-we-cant-do-this-without-you-is-a-warning

[7] Short Essays & Prose — The Message, Detection, and Quantum Mechanics
Flash fiction, air defense physics, and why n².

The Message

TL;DR: A man receives a message directly in his mind — not a text or email — unmistakably from someone he knows. It reads: "Samsung. Hyundai. Stocks." He calls his broker and clarifies: not Samsung Electronics, but Samsung Motors and Hyundai Electronics. He bets "everything I have" on both. Cryptic, abrupt — flash fiction or parable.

Read more → https://seoulinside.substack.com/p/the-message

Detection Is Not the Problem. Tracking Is.

TL;DR: Stealth doesn't make you invisible — it makes you unlockable. The 1960s HAWK missile system reveals why: detection and tracking are separate problems, and breaking either kills the chain. Modern AESA hides the seams; stealth exploits them. Low-frequency radar detects but can't target. Multistatic radar (separated transmitter/receiver) is the real threat. The physics hasn't changed — only the speed.

Read more → https://seoulinside.substack.com/p/detection-is-not-the-problem-tracking-is

I Thought About Quantum Mechanics Over Lunch (Part 1)

TL;DR: A lunchtime thought experiment reconstructs quantum origins. Pendulum → wave → circle. Only integer-cycle waves close perfectly — fractional cycles cancel. That is quantization. Experiments showed radius ratios 1:4:9 (n²), not 1:2:3. The square emerges from a feedback loop: longer wavelength pushes electron farther, which makes wavelength longer again. Schrödinger later explained why n². Part 2: why hydrogen is simple and everything after is brutally complicated.

Read more → https://seoulinside.substack.com/p/i-thought-about-quantum-mechanics-over-lunch

South Korea's Inheritance Tax — A Complete Guide

TL;DR: South Korea has one of the world's highest inheritance taxes — 50% top rate, 60% for largest shareholders, second only to Japan in the OECD. The system uses an "estate tax" model (taxing the whole estate before distribution). Samsung's Lee Kun-hee family paid ₩12.7T ($9.3B) — the largest single inheritance tax bill ever. The Nexon family paid ₩6T, transferring 29.3% of NXC shares to the government when no cash was available. A 2028 reform to shift from estate tax to acquisition tax has stalled.

Read more → https://seoulinside.substack.com/p/south-koreas-inheritance-tax-a-complete-guide

What the Numbers Don't Tell You — Biyereyul (비례율)

TL;DR: Biyereyul is the ratio that determines how much reconstruction members must pay. The formula is simple, but all three variables are outside members' control. In 6 cases with both initial and final figures, biyereyul dropped by an average of 16 percentage points — always downward, never up. One case saw members expecting a refund receive a demand for hundreds of millions of won just two months before move-in. The gap between initial estimate and final reality is where financial pain lives.

Read more → https://seoulinside.substack.com/p/what-the-numbers-dont-tell-you-biyereyul

From Association to Relocation — Real Reconstruction Timelines (60 Projects)

TL;DR: Complete dataset of 60 reconstruction projects in Gyeonggi Province and Incheon that reached relocation. Shortest: Namyangju Hwado Prugio (2 years 9 months). Longest: Forena Incheon Guwol (9 years 1 month). Average: 5 years 11 months from association establishment to residents vacating the site. An additional table shows Seoul projects running 15-30 years, many still in progress. The projects that took the longest are not struggling neighborhoods — they are among the most sought-after addresses in South Korea.

Read more → https://seoulinside.substack.com/p/from-association-to-relocation-real-reconstruction-timelines

About This Newsletter — The Longest Wait Inside Korea's Apartment Redevelopment Machine

TL;DR: Korea builds and rebuilds more apartments than almost any country, yet almost none of the process has been explained in English. This newsletter draws on a research database of regulatory filings, court records, association disclosures, and construction industry data across dozens of projects. For anyone with family or financial exposure to Korean real estate, working in finance/urban development, studying housing policy, or simply curious about how Seoul keeps rebuilding itself — and at what cost.

Read more → https://seoulinside.substack.com/p/about-this-newsletter














---

[Link1 →](https://xur94-maker.github.io/SeoulInside/link1.html)  
[Link2 →](https://xur94-maker.github.io/SeoulInside/link2.html)  
[wordpress →](https://seoulinside.wordpress.com/2026/05/18/news/)  
[medium →](https://medium.com/@Seoulinside/news1-fb946ec27af9)  

- [GitHub Repository: SeoulInside](https://github.com/xur94-maker/SeoulInside)
- [GitHub Pages Settings](https://github.com/xur94-maker/SeoulInside/settings/pages)
- [YouTube](https://www.youtube.com/)
- [Instagram: apt_lap](https://www.instagram.com/apt_lap/)
- [Bluesky Social](https://bsky.app/)
- [Ko-Fi Management](https://ko-fi.com/Manage/)
- [Naver Mail: Write to Myself](https://mail.naver.com/v2/new?type=toMe)
- [500px: Photo Manager](https://500px.com/manager?view=photos&filter=all)
- [Facebook](https://www.facebook.com/?locale=ko_KR)
- [Medium: Import](https://medium.com/p/import)
- [aagag.com](https://aagag.com/)
- [WordPress: Seoul Inside Dashboard](https://wordpress.com/home/seoulinside.wordpress.com)
- [Coupang Play Home](https://www.coupangplay.com/home)
- [Seoul National University Login](https://my.snu.ac.kr/login.jsp)
- [Naver MyBox](https://mybox.naver.com/main/web/my)
- [Google Photos](https://photos.google.com/u/2/?pageId=none&pli=1)
- [Google Messages Web](http://messages.google.com/web/conversations)
- [Naver Shopping Home](https://shopping.naver.com/ns/home)
- [Naver Pay History](https://pay.naver.com/pc/history?page=1)
- [Naver Land: Interests](https://new.land.naver.com/interests)
- [Naver Mail: Write to Myself](https://mail.naver.com/v2/new?type=toMe)
- [Gmail Inbox](https://mail.google.com/mail/u/1/#inbox)
- [Investing.com: US Markets](https://kr.investing.com/markets/united-states)
- [Naver Land Search: Reconstruction](https://new.land.naver.com/search?ms=2AHO5s,3zdsC3,16&a=APT:PRE:ABYG:JGC&b=A1&e=RETAIL&h=33&i=66&ad=true)
- [Google News Search: Reconstruction](https://www.google.com/search?q=%EC%9E%AC%EA%B1%B4%EC%B6%95&tbm=nws)
- [Naver Cafe Search: Reconstruction](https://search.naver.com/search.naver?ssc=tab.cafe.all&sm=tab_jum&query=%EC%9E%AC%EA%B1%B4%EC%B6%95)
- [Naver Blog Search: Reconstruction](https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=%EC%9E%AC%EA%B1%B4%EC%B6%95)
- [Naver News Search: Reconstruction](https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%9E%AC%EA%B1%B4%EC%B6%95)
- [Naver Mobile Home](https://m.naver.com/)
- [AlphaSquare: Samsung Electronics Stock](https://alphasquare.co.kr/home/stock-summary?code=005930)
- [Investing.com: US Markets](https://kr.investing.com/markets/united-states)
- [Ppomppu: Real Estate Hot List](https://www.ppomppu.co.kr/zboard/zboard.php?id=house&hotlist_flag=999)
- [FM Korea: Real Estate Forum](https://www.fmkorea.com/?mid=realestate)
- [Daum Finance: KOSPI](https://finance.daum.net/domestic/kospi)
