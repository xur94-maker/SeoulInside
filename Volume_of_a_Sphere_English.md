# Methods for Deriving the Volume of a Sphere V = ⁴⁄₃π r³

---

# 1. Geometric Methods for Finding the Volume of a Sphere

## 1.1 From Cavalieri's Principle

### 1) Why consider this comparison?

Let a sphere of radius r be centered at the origin. If we slice the sphere with a plane at height h along the x-axis, the cross-section is a circle. By the Pythagorean theorem, the radius of the cross-section is √(r²-h²), so the cross-sectional area is

A_sphere(h) = π(r² - h²) = π r² - π h²

This expression can be read as "a constant π r² minus a quantity π h² proportional to h²."

- A solid with a constant cross-section π r²: a cylinder of radius r and height r
- A solid with cross-section π h²: a cone whose radius at height h is h

Therefore, the solid obtained by removing a cone from a cylinder will have exactly the same cross-sectional area profile as the sphere. This is the heuristic insight behind the proof.

### 2) Formulation of Cavalieri's principle

> **Principle (Cavalieri, 1635):** If two solids have the same height, and at every height h measured from the base the areas of the corresponding parallel cross-sections are equal, then the two solids have equal volume.

In modern terms this is simply V = ∫₀ʳ A(h) dh, so if A(h) is the same for both solids, the integrals (and hence the volumes) are equal — an obvious fact. In Cavalieri's time, without the concept of integration, it was understood as a sum of "indivisibles."

Principle 1 (area): If two plane figures, when cut by a family of parallel lines, always yield line segments of equal length, then the two figures have equal area.
Principle 2 (volume): If two solids, when cut by a family of parallel planes, always yield cross-sections of equal area, then the two solids have equal volume.

### 3) Precise placement of the two solids

- **Solid I: Hemisphere H** — the part of the ball x²+y²+z² ≤ r² with z ≥ 0. Its flat face lies on the xy-plane, and its height ranges over 0 ≤ h ≤ r.
- **Solid II: C − K** — the cylinder C: x²+y² ≤ r², 0 ≤ z ≤ r, with the cone K: x²+y² ≤ z², 0 ≤ z ≤ r removed. The cone's apex is at the center of the cylinder's base, (0,0,0), and its base is the circle of radius r on the cylinder's top face z = r.

### 4) Detailed computation of the cross-sectional areas

Cut with the plane z = h at height h from the base.

**Cross-section of the hemisphere:** From the sphere's equation, x²+y²+h² = r², so x²+y² = r²-h². This is a circle of radius R₁ = √(r²-h²).

A_(hemisphere)(h) = π R₁² = π(r²-h²)

**Cross-section of the cylinder-minus-cone:** The cylinder's cross-section is a circle of radius r, with area π r². By similarity, the cone's radius at height h is h — because the axial cross-section of the cone is an isosceles triangle, and at height h the width scales by the ratio h/r, giving r·(h/r) = h. Hence the area of the cone's cross-section is π h².

A_(C−K)(h) = π r² - π h² = π(r²-h²)

The two cross-sectional areas agree for every h ∈ [0,r]. Their shapes also match visually: both are either a circle of radius √(r²-h²) or a ring (annulus) of the same area.

### 5) Computing the volume

By Cavalieri's principle, V_(hemisphere) = V_C − V_K.

The cylinder's volume is V_C = (base area) × (height) = π r² · r = π r³.

The cone's volume is V_K = ⅓π r² · r = ⅓π r³ (this formula is itself first proved using Cavalieri's principle).

Therefore

V_(hemisphere) = π r³ − ⅓π r³ = ⅔π r³

V_sphere = 2 V_(hemisphere) = ⁴⁄₃π r³

The strength of this proof is that it obtains the volume of the sphere purely by comparing cross-sections, without using any approximation of π or any limiting process.

**Summary**
A_(hemisphere)(h) = π(r² − h²), A_(cylinder−cone)(h) = π r² − π h² = π(r² − h²)
V_(hemisphere) = π r³ − ⅓π r³ = ⅔π r³, V_sphere = 2·⅔π r³ = ⁴⁄₃π r³

---

## 1.2 From Archimedes' Spherical Cap Formula

### 1) Definition of the spherical cap

Cut the sphere S: x²+y²+z² = r², centered at the origin O with radius r, by the plane x = b (−r ≤ b ≤ r). The cap-shaped solid remaining on the side x ≥ b is called a spherical cap.

Let h = r − b denote the height of the cap.

- b = r ⇒ h = 0: volume 0
- b = 0 ⇒ h = r: a hemisphere
- b = −r ⇒ h = 2r: the whole sphere

Keep the relation b = r − h in mind.

### 2) Setting up the integral via the disk method

Take the x-axis as the axis of rotation. Slicing the sphere with a plane perpendicular to the x-axis at position x gives a cross-section that is a circle centered at (x,0,0) with radius y. From the sphere's equation, y²+z² = r² − x², so

A(x) = π y² = π(r² − x²)

If the disk's thickness is dx, the volume element is dV = A(x) dx. Hence the volume of the spherical cap is the integral from x = b to x = r:

V_(cap)(b) = ∫_bʳ π(r² − x²) dx

### 3) Detailed evaluation of the integral

V(b) = π ∫_bʳ (r² − x²) dx = π [ r²x − (x³)/3 ]_bʳ
= π { (r³ − r³/3) − (r²b − b³/3) }
= π (⅔r³ − r²b + ⅓b³)
= (π/3)(2r³ − 3r²b + b³)

Now factor 2r³ − 3r²b + b³. Since this expression vanishes at b = r, (b−r) is a factor — equivalently, group it as (r−b). Polynomial division gives:

2r³ − 3r²b + b³ = (r−b)²(2r+b)

Check: (r²−2rb+b²)(2r+b) = 2r³+r²b−4r²b−2rb²+2rb²+b³ = 2r³−3r²b+b³.

So the closed form is:

V_(cap) = ⅓π (r−b)²(2r+b)

### 4) Standard form in terms of the height h

Substituting b = r − h gives the most commonly used form:

V_(cap)(h) = ⅓π h²(3r−h) = π h²(r − h/3)

This is exactly the form Archimedes proved in *On the Sphere and Cylinder*. When h ≪ r, V ≈ π r h², which is close to the volume of a thin cylinder with base radius ≈ √(2rh).

### 5) Extending to the whole sphere

Substituting b = −r, i.e. h = 2r, means the cutting plane passes through the sphere's lowest point (−r,0,0), so the cap becomes the entire sphere.

V_sphere = V_(cap)(h=2r) = ⅓π (r−(−r))²(2r+(−r)) = ⅓π (2r)²(r) = ⁴⁄₃π r³

Or, using the h version:

V_sphere = ⅓π (2r)²(3r−2r) = ⅓π · 4r² · r = ⁴⁄₃π r³

This method has independent value because the intermediate result — the spherical-cap formula itself — is useful in geometry and physics (e.g., liquid volumes).

**Summary**
V_(cap) = ∫_bʳ π(r² − x²) dx = ⅓π(r−b)²(2r+b)
V_(cap)(h) = ⅓π h²(3r−h)
b = −r ⇒ V = ⅓π(2r)²(r) = ⁴⁄₃π r³

---

## 1.3 Kepler's Method of Infinitesimal Pyramids (Cones)

### 1) The idea: why view the sphere as a sum of cones?

Consider a circle in the plane first. Divide the circle's circumference 2π r into infinitely many tiny segments ds, and for each segment form an isosceles triangle with the circle's center. Each triangle has height r and base ds, so its area is ½ r ds. Summing gives

A_circle = ½ r × (2π r) = π r²

Kepler (1615, *Nova Stereometria Doliorum Vinariorum* — "New Solid Geometry of Wine Barrels") extended this idea to three dimensions. Divide the sphere's surface into small patches dA, and for each patch form a pyramid with that patch as base and the sphere's center O as apex; the sphere is then filled by the sum of these pyramids.

Two formulas are needed here: (A) the surface area of the sphere S, and (B) the volume of a pyramid, V = ⅓ × (base area) × (height).

### 2) Deriving the surface area S = 4π r² — the latitude-band method

Represent a point on the sphere by the angle θ measured from the north pole (co-latitude, 0 ≤ θ ≤ π) and the longitude φ. For fixed θ we get a circle of latitude with radius r sinθ.

Consider a very thin band of thickness dθ. Unrolled, this band is approximately a rectangle whose width is the circumference of the latitude circle, 2π(r sinθ), and whose length is the meridian arc length r dθ.

dS = (circumference) × (width) = 2π(r sinθ) · (r dθ) = 2π r² sinθ dθ

The whole sphere runs from θ = 0 (north pole) to θ = π (south pole), so:

S = ∫₀^π 2π r² sinθ dθ = 2π r² ∫₀^π sinθ dθ = 2π r² [−cosθ]₀^π

= 2π r² (−cosπ + cos0) = 2π r² (1+1) = 4π r²

This is the surface-area formula for a sphere, proved by Archimedes.

### 3) Volume of the infinitesimal pyramids

Now divide the sphere's surface into N very small patches. Let the area of the i-th patch be ΔAᵢ. Consider the solid Pᵢ formed by connecting the center O to the boundary of that patch.

If ΔAᵢ is sufficiently small, it can be approximated by a plane, and Pᵢ is nearly a pyramid (cone) with base area ΔAᵢ and height hᵢ, where hᵢ is the perpendicular distance from center O to the plane of the patch. Since the patch lies on the sphere's surface, every point of it is at distance r from O; as the patch shrinks, the discrepancy between the plane and the sphere's surface becomes o(ΔAᵢ), so hᵢ → r.

By the pyramid volume formula, then:

V(Pᵢ) = ⅓ ΔAᵢ · r + errorᵢ, where errorᵢ / ΔAᵢ → 0

Summing over all i:

V_sphere = Σᵢ V(Pᵢ) = ⅓ r Σᵢ ΔAᵢ + Σᵢ errorᵢ

As N → ∞ and max ΔAᵢ → 0, Σᵢ ΔAᵢ → S = 4π r², and the sum of the errors goes to 0. Taking the limit:

V_sphere = ⅓ r · S

This is the key identity of Kepler's method: once the surface area is known, the volume follows immediately.

### 4) Computation

V_sphere = ⅓ r × 4π r² = ⁴⁄₃π r³

### 5) Significance and limitations of this method

This proof can look circular, because integration was already used to obtain S = 4π r². Nevertheless, it holds great historical significance:

- Archimedes proved S = 4π r² without integration, by comparison with a circumscribed cylinder. Using that proof, one can obtain V = ⁴⁄₃π r³ without any integration at all.
- This method extends to arbitrary polyhedra. For a convex polyhedron containing the origin in its interior, the volume is V = ⅓ Σ(areaᵢ × distanceᵢ to that face). The sphere is, in a sense, the limiting case of this formula.
- Unlike §1.1 (Cavalieri) and §1.2 (spherical cap), this method reveals a differential-geometric insight — the relationship between surface area and volume: dV/dr = S.
- **A modern connection — the Divergence Theorem (Gauss's theorem):** Kepler's argument is, in essence, a prototype of the divergence theorem. For a region Ω containing the origin, with boundary ∂Ω, the identity V(Ω) = ⅓ ∮_(∂Ω) r⃗ · n̂ dA holds (this follows directly from the divergence theorem, since the divergence of the vector field r⃗ is ∇·r⃗ = 3). For a sphere, r⃗ · n̂ = r (a constant), so this integral simplifies to ⅓ r S — precisely the key identity of §1.3. In other words, Kepler's infinitesimal-pyramid argument can be seen as an early, special-case discovery of the divergence theorem, predating Newton and Leibniz, and it sits on the same conceptual line as the n-dimensional generalization in Chapter 4.

**Summary**
S = ∫₀^π 2π r² sinθ dθ = 4π r²
dVᵢ = ⅓ r dAᵢ
V = ∫_S ⅓ r dA = ⅓r ∫_S dA = ⅓r S = ⁴⁄₃π r³

---

# 2. Calculus-Based Methods for Finding the Volume of a Sphere

## 2.1 The Disk Method

### 1) The idea: why stack disks?

The most intuitive integral method for finding the volume of a sphere is to "stack infinitely many thin disks." Slicing the sphere along the x-axis, each cross-section is a circle. Integrating the area A(x) of these disks over x gives the volume. This is the essence of the method of exhaustion by summation (Riemann-sum approach).

Consider a sphere centered at the origin O with radius r. Its equation is

x² + y² + z² = r²

Slicing with a plane x = const parallel to the yz-plane, the cross-section is the circle satisfying y²+z² = r²−x². The radius of this circle is precisely y = √(r²−x²).

### 2) Rigorous derivation of the cross-sectional area function A(x)

Fix x. A point (x,y,z) on the sphere satisfies y²+z² = r²−x². If r²−x² < 0 there is no cross-section, so cross-sections exist only for −r ≤ x ≤ r.

The cross-section is then a circle centered at (x,0,0) with radius R(x) = √(r²−x²), so:

A(x) = π R(x)² = π(r²−x²)

This function attains its maximum π r² at x = 0 and equals 0 at x = ±r — a parabolic profile.

### 3) From Riemann sums to the integral

Divide [−r, r] into n subintervals, and at a representative point xᵢ of the i-th subinterval, approximate the solid by a thin cylinder (disk) of thickness Δx. The volume of this disk is A(xᵢ)Δx. The sum is a Riemann sum:

Vₙ = Σᵢ₌₁ⁿ π(r²−xᵢ²)Δx

As n → ∞ and max Δx → 0, the Riemann sum converges to the definite integral:

V_sphere = ∫₋ᵣʳ A(x) dx = ∫₋ᵣʳ π(r²−x²) dx

By symmetry, we can compute just the hemisphere and double it, which simplifies the computation:

V_(hemisphere) = ∫₀ʳ π(r²−x²) dx

### 4) The full computation of the integral

V_(hemisphere) = π ∫₀ʳ (r² − x²) dx
= π [ r²x − x³/3 ]₀ʳ
= π (r²·r − r³/3 − 0)
= π (r³ − r³/3) = ⅔π r³

Therefore, for the whole sphere:

V_sphere = 2 · ⅔π r³ = ⁴⁄₃π r³

Equivalently, integrating directly from −r to r gives the same result:

V_sphere = π [ r²x − x³/3 ]₋ᵣʳ = π(⅔r³ − (−⅔r³)) = ⁴⁄₃π r³

The reason this method's formulas match those of §1.2 (spherical cap) is that the spherical-cap method is itself a special case of the disk method.

**Summary**
A(x) = π(r²−x²)
V_(hemisphere) = ∫₀ʳ π(r²−x²) dx = ⅔π r³, V_sphere = ⁴⁄₃π r³

---

## 2.2 The Cylindrical Shell Method

### 1) The idea: why use shells?

The disk method slices with planes perpendicular to the x-axis. The shell method instead slices in a direction parallel to the x-axis. Consider revolving the semicircle y = √(r²−x²) (0 ≤ x ≤ r) about the y-axis.

Revolving a very thin rectangle of width dx and height y, located at position x, about the y-axis produces a thin cylindrical shell of radius x, height y, and thickness dx. Unrolled, this shell is approximately a rectangular box with width 2π x (the circumference), height y, and thickness dx. Hence the volume element is:

dV = 2π x · y · dx = 2π x √(r²−x²) dx

### 2) Justification via Riemann sums

As with the disk method, divide [0, r] into n equal parts, approximate the volume of the shell in each subinterval by 2π xᵢ √(r²−xᵢ²)Δx, and sum to get a Riemann sum. As n → ∞, this converges to the integral.

Integrating from x = 0 to r gives the solid obtained by revolving the region y ≥ 0 about the y-axis — that is, precisely the hemisphere on the side x ≥ 0. So this integral gives V_(hemisphere).

V_(hemisphere) = ∫₀ʳ 2π x √(r²−x²) dx

### 3) The full process of substitution

V_(hemisphere) = ∫₀ʳ 2π x √(r²−x²) dx

Let u = r² − x². Then

du = −2x dx ⇒ −du = 2x dx

The limits of integration also change:
- x = 0 ⇒ u = r² − 0 = r²
- x = r ⇒ u = r² − r² = 0

Therefore

V_(hemisphere) = ∫_(x=0)^r 2π x √(r²−x²) dx
= π √(r²−x²) · (2x dx), rewritten in terms of u:
2π x √(r²−x²) dx = π √(r²−x²) · (2x dx) = π √u · (−du)

V_(hemisphere) = ∫_(r²)^0 −π u^(1/2) du = π ∫₀^(r²) u^(1/2) du

∫ u^(1/2) du = ⅔ u^(3/2)

so

V_(hemisphere) = π [ ⅔ u^(3/2) ]₀^(r²) = π · ⅔ (r²)^(3/2) = ⅔π r³

Therefore

V_sphere = 2 V_(hemisphere) = ⁴⁄₃π r³

This matches the result from the disk method — as it must, since we are simply cutting the same sphere in a different way. The shell method requires a substitution because of the square root in the integrand, but it offers the stronger visual intuition of "peeling off shells."

**Summary**
dV = 2π x · √(r²−x²) dx
V_(hemisphere) = ∫₀ʳ 2π x√(r²−x²) dx = π∫₀^(r²) u^(1/2) du = ⅔π r³
V_sphere = ⁴⁄₃π r³

---

## 2.3 The Pappus–Guldinus Theorem

### 1) The theorem: what does it say?

> **Pappus's Second Theorem:** The volume of the solid formed by revolving a plane figure about an axis, in the same plane, that does not intersect the figure equals (the area of the figure) × (the circumference traced by the figure's centroid).

V = A · (2π r̄)

Here r̄ is the distance from the figure's centroid to the axis of revolution.

This theorem replaces integration with the geometric notion of the centroid. It was proved by Pappus (4th century) and Guldin (17th century). Today the theorem is usually proved using integration, but conversely, it can be used to find the volume of a sphere without directly performing an integral for the volume itself.

### 2) Setup: forming a sphere by revolving a half-disk

Consider the upper half-disk D with the x-axis as its diameter:

D = {(x,y) | x²+y² ≤ r², y ≥ 0}

Revolving this half-disk D by 360° about the x-axis (the diameter) produces a sphere. Each point (x,y) of the half-disk traces a circle of radius y, and the union of these circles is the sphere.

- Area of the figure: A = ½π r²
- Centroid: by symmetry, x̄ = 0. What matters is ȳ, the distance from the axis of revolution (the x-axis) to the centroid.

### 3) The key step: deriving the centroid ȳ = 4r/3π of the half-disk

This value is often used from memory, but it should be derived. By definition of the centroid:

ȳ = (1/A) ∬_D y dA

Converting to polar coordinates x = ρcosθ, y = ρsinθ (0 ≤ ρ ≤ r, 0 ≤ θ ≤ π), we have dA = ρ dρ dθ.

∬_D y dA = ∫₀^π ∫₀ʳ (ρ sinθ) ρ dρ dθ = ∫₀^π sinθ dθ ∫₀ʳ ρ² dρ

∫₀ʳ ρ² dρ = r³/3, ∫₀^π sinθ dθ = 2

So

∬_D y dA = (r³/3) · 2 = 2r³/3

Dividing by the area A = ½π r²:

ȳ = (2r³/3) / (π r²/2) = (2r³/3) · (2/(π r²)) = 4r/(3π)

This result means the centroid of the half-disk lies at a distance 4r/3π ≈ 0.424r above the diameter — slightly below the midpoint r/2 = 0.5r, because the area is concentrated more toward the inside than the outside.

### 4) Applying Pappus's theorem

The circumference traced by the centroid G = (0, ȳ) as it revolves about the x-axis is:

L = 2π ȳ = 2π · (4r/3π) = 8r/3

By the theorem, the volume of the sphere is:

V_sphere = A · L = (½π r²) · (2π ȳ) = ½π r² · (8r/3) = ⁴⁄₃π r³

Written out step by step:

V = 2π ȳ · A = 2π · (4r/3π) · ½π r² = (8r/3) · ½π r² = ⁴⁄₃π r³

### 5) Significance, and a caveat about circularity

This proof is elegant, but since finding ȳ = 4r/3π already required an integration (the double integral above), it does not entirely avoid integration. However, from a different perspective:

- If ȳ is obtained by physical experiment or by some other geometric method, one can obtain the volume of the sphere without integration.
- Conversely, if the volume of the sphere, 4/3π r³, is known, Pappus's theorem can be used in reverse to prove that the centroid of the half-disk is 4r/3π.

In other words, Pappus's theorem serves as a bridge connecting the three concepts of area, centroid, and the volume of a solid of revolution.

**Summary**
A = ½π r², ȳ = (1/A)∬_D y dA = 4r/(3π)
V = (2πȳ) A = 2π·(4r/3π)·½π r² = ⁴⁄₃π r³

---

## 2.3 Pappus–Guldinus Theorem (continued) + 3. Multiple-Integral Methods

## 2.3 The Pappus–Guldinus Theorem

### 1) Why can we trust the theorem itself?

> **Pappus–Guldinus's Second Theorem:** The volume of the solid obtained by revolving a plane figure D about an axis l, lying in the same plane and not intersecting D, is V = A · (2π r̄), where A is the area of the figure and r̄ is the distance from the figure's centroid to the axis l.

Idea of the proof: If the figure is sliced into thin strips at distance y from l, the volume swept out by a strip as it revolves is 2π y × (area of the strip). Summing over all strips gives 2π ∫ y dA = 2π ȳ A. In other words, Pappus's theorem is nothing more than the shell-method formula V = ∫ 2π y dA rewritten using the definition of the centroid, ȳ = (1/A)∫ y dA.

### 2) Setting up the half-disk

The upper half-disk with the x-axis as diameter:

D = {(x,y) | x²+y² ≤ r², y ≥ 0}

Revolving D about the x-axis produces a sphere, because for a fixed x, the vertical cross-section of D is a segment of length y = √(r²−x²), and revolving this segment about the x-axis produces a circle of radius y; the union of these circles is the sphere.

- Area: A = ½π r²
- Centroid: by symmetry, x̄ = 0. Only ȳ needs to be found.

### 3) Full derivation of the centroid ȳ = 4r/(3π) — double integral in polar coordinates

Definition:

ȳ = (1/A) ∬_D y dA

Write D in polar coordinates (ρ, θ): x = ρcosθ, y = ρsinθ, 0 ≤ ρ ≤ r, 0 ≤ θ ≤ π, dA = ρ dρ dθ.

∬_D y dA = ∫₀^π ∫₀ʳ (ρsinθ) ρ dρ dθ = (∫₀^π sinθ dθ)(∫₀ʳ ρ² dρ)

∫₀ʳ ρ² dρ = r³/3, ∫₀^π sinθ dθ = [−cosθ]₀^π = 2

So

∬_D y dA = (r³/3)·2 = 2r³/3

A = ½π r² ⇒ ȳ = (2r³/3)/(π r²/2) = 4r/(3π) ≈ 0.424r

Why it lies slightly below 0.5r: because the area is concentrated more toward the inside than toward the outside, relative to the axis.

### 4) Applying Pappus's theorem

The circumference traced by the centroid G:

L = 2πȳ = 2π·(4r/3π) = 8r/3

V_sphere = A·L = ½π r² · (8r/3) = ⁴⁄₃π r³

Written out:

V = 2πȳ A = 2π·(4r/3π)·½π r² = ⁴⁄₃π r³

### 5) Significance and a caveat about circularity

Since finding ȳ already required a double integral, this does not entirely avoid integration. Nevertheless, Pappus's theorem is a bridge linking "area–centroid–volume of revolution," and knowing V lets one work backward to find ȳ. The three concepts are, in effect, equivalent to one another.

**Summary**
A = ½π r², ȳ = 4r/(3π)
V = 2πȳ A = ⁴⁄₃π r³

---

## 3. Multiple-Integral Methods (Using the Jacobian)

### 3.1 Spherical Coordinates

#### 1) Definition of spherical coordinates

The relation between Cartesian coordinates (x,y,z) and spherical coordinates (ρ,θ,φ) (using the physics convention, where θ is measured from the z-axis and φ is the azimuthal angle in the xy-plane):

x = ρ sinθ cosφ
y = ρ sinθ sinφ
z = ρ cosθ

Ranges: ρ ≥ 0, 0 ≤ θ ≤ π, 0 ≤ φ < 2π.

ρ is the distance from the origin, θ is the co-latitude (θ = 0 at the north pole, θ = π/2 at the equator, θ = π at the south pole), and φ is the longitude.

#### 2) Why is the volume element dV = ρ²sinθ dρ dθ dφ? — deriving the Jacobian

We must compute the Jacobian J = |∂(x,y,z)/∂(ρ,θ,φ)| of the transformation from Cartesian to spherical coordinates.

∂(x,y,z)/∂(ρ,θ,φ) =
|
sinθcosφ  ρcosθcosφ  −ρsinθsinφ
sinθsinφ  ρcosθsinφ   ρsinθcosφ
cosθ      −ρsinθ      0
|

Expanding this determinant gives |J| = ρ² sinθ. Intuitively:

- thickness dρ in the ρ direction
- arc length ρ dθ in the θ direction
- arc length ρ sinθ dφ in the φ direction (at latitude θ, the radius of the circle in the longitudinal direction is ρ sinθ)

These three edges form a small box that is mutually perpendicular, so the volume is the product of the three edge lengths:

dV = (dρ)(ρ dθ)(ρ sinθ dφ) = ρ² sinθ dρ dθ dφ

#### 3) Integrating over the whole sphere

A sphere of radius R corresponds to ρ ∈ [0,R], θ ∈ [0,π], φ ∈ [0,2π].

V = ∫₀^(2π) ∫₀^π ∫₀^R ρ² sinθ dρ dθ dφ

The integral separates:

V = (∫₀^(2π) dφ) (∫₀^π sinθ dθ) (∫₀^R ρ² dρ)

Computing each factor:

∫₀^(2π) dφ = 2π
∫₀^π sinθ dθ = [−cosθ]₀^π = −(−1)+1 = 2
∫₀^R ρ² dρ = [ρ³/3]₀^R = R³/3

Multiplying:

V = 2π · 2 · (R³/3) = ⁴⁄₃π R³

This method shows that spherical coordinates are the most natural coordinate system for the symmetry of a sphere: the radial integral and the angular integrals separate completely.

**Summary**
dV = r² sinθ dr dθ dφ
V = ∫₀^(2π)∫₀^π∫₀^R r² sinθ dr dθ dφ = ⁴⁄₃π R³

---

### 3.2 Cylindrical Coordinates

#### 1) Definition of cylindrical coordinates and the volume element

Cylindrical coordinates (r,θ,z): x = r cosθ, y = r sinθ, z = z, dV = r dr dθ dz.

In cylindrical coordinates, the ball x²+y²+z² ≤ R² becomes r²+z² ≤ R². For fixed r, z ranges from −√(R²−r²) to +√(R²−r²), a length of 2√(R²−r²) in the z direction.

So the volume of the sphere is:

V = ∫_(θ=0)^(2π) ∫_(r=0)^R ∫_(z=−√(R²−r²))^(√(R²−r²)) r dz dr dθ = ∫₀^(2π) dθ ∫₀^R 2√(R²−r²) · r dr

This expression is, in essence, the shell method of §2.2 written in the language of cylindrical coordinates. The term 2π r · 2√(R²−r²) dr is the volume of a cylindrical shell of radius r, height 2√(R²−r²), and thickness dr.

#### 2) The full substitution process — repeated in detail, though equivalent to §2.2

I = ∫₀^R 2r√(R²−r²) dr

Let u = R² − r². Then du = −2r dr, r = 0 ⇒ u = R², r = R ⇒ u = 0.

I = ∫_(R²)^0 2r√u · (du)/(−2r) = ∫_(R²)^0 −√u du = ∫₀^(R²) u^(1/2) du

= [⅔u^(3/2)]₀^(R²) = ⅔(R²)^(3/2) = ⅔R³

Therefore

V = ∫₀^(2π) I dθ = 2π · ⅔R³ = ⁴⁄₃π R³

#### 3) Comparison with §2.2 — why are they the same?

In §2.2, the shell method revolved the semicircle y = √(R²−x²) about the y-axis and integrated the volume 2π x y dx. In cylindrical coordinates, x plays the role of r, and y plays the role of half the height in the z direction, √(R²−r²). The expressions 2π x y dx and 2π r √(R²−r²) dr are the same. The difference is that §3.2 combines both the upper and lower halves along z into 2√(R²−r²), so there is no need to double a hemisphere — the whole sphere's volume comes out directly.

In short, the disk method, the shell method, and cylindrical coordinates are all the same integral viewed from different geometric perspectives.

**Summary**
V = ∫₀^(2π)∫₀^R 2√(R²−r²)· r dr dθ
= 2π · ⅔R³ = ⁴⁄₃π R³

---

# 4. Analytic Generalization: The Volume of an n-Dimensional Ball (Gaussian Integral + Gamma Function)

## 1) Goal and idea: why use the Gaussian integral?

We know the volume of a 3-dimensional ball, V₃ = ⁴⁄₃π R³. What is the volume Vₙ(R) of the ball Bₙ(R) = {x ∈ ℝⁿ | |x| ≤ R} of radius R in n-dimensional space ℝⁿ?

Direct n-fold integration is difficult. Gauss's trick is to integrate the rotationally symmetric function e^(−|x|²) over all of ℝⁿ in two different ways and compare the results.

- Method A: In Cartesian coordinates, the variables separate, giving (∫ e^(−t²) dt)ⁿ.
- Method B: In spherical coordinates, the integral separates into a radial integral times the surface area Sₙ₋₁ of the unit sphere.

Since the two results must be equal, we can solve for Sₙ₋₁, and integrating Sₙ₋₁ over the radial direction then gives Vₙ(R).

### 2) Tool 1: the 1-dimensional Gaussian integral ∫_(−∞)^∞ e^(−t²) dt = √π

This result is important in its own right. It is proved using polar coordinates:

(∫_(−∞)^∞ e^(−x²) dx)² = ∫_(−∞)^∞ e^(−x²) dx ∫_(−∞)^∞ e^(−y²) dy = ∬_(ℝ²) e^(−(x²+y²)) dx dy

Converting to polar coordinates r, θ, we have dx dy = r dr dθ and x²+y² = r², so

= ∫₀^(2π) dθ ∫₀^∞ e^(−r²) r dr = 2π · [−½e^(−r²)]₀^∞ = 2π · ½ = π

Therefore ∫_(−∞)^∞ e^(−t²) dt = √π (taking the positive root).

### 3) Method A: Cartesian coordinates, separation of variables

In ℝⁿ, x = (x₁,…,xₙ), |x|² = x₁²+⋯+xₙ².

∫_(ℝⁿ) e^(−|x|²) dx = ∫_(ℝⁿ) e^(−(x₁²+⋯+xₙ²)) dx₁⋯dxₙ = ∫_(ℝⁿ) Πᵢ₌₁ⁿ e^(−xᵢ²) dx₁⋯dxₙ

By the laws of exponents this separates into a product, and by Fubini's theorem the integral separates as well:

= Πᵢ₌₁ⁿ (∫_(−∞)^∞ e^(−xᵢ²) dxᵢ) = (∫_(−∞)^∞ e^(−t²) dt)ⁿ = (√π)ⁿ = π^(n/2)

Therefore

∫_(ℝⁿ) e^(−|x|²) dx = π^(n/2)  (A)

This depends only on the dimension n, not on direction.

### 4) Method B: spherical coordinates, separating radius and surface area

Consider n-dimensional spherical coordinates. Let r = |x|, and represent the direction by a point ω on the unit sphere Sⁿ⁻¹. The volume element is

dx = rⁿ⁻¹ dr dσ(ω)

where dσ is the area element on the unit sphere Sⁿ⁻¹. Define Sₙ₋₁ = ∫_(Sⁿ⁻¹) dσ as the surface area of the n-dimensional unit sphere. (For n = 3, S₂ = 4π r² at r = 1, giving 4π.)

Since the rotationally symmetric function e^(−|x|²) = e^(−r²) does not depend on the direction ω:

∫_(ℝⁿ) e^(−|x|²) dx = ∫₀^∞ ∫_(Sⁿ⁻¹) e^(−r²) rⁿ⁻¹ dσ dr = (∫_(Sⁿ⁻¹) dσ) (∫₀^∞ rⁿ⁻¹ e^(−r²) dr)

= Sₙ₋₁ ∫₀^∞ rⁿ⁻¹ e^(−r²) dr  (B)

### 5) Tool 2: the Gamma function Γ(z)

Γ(z) = ∫₀^∞ tᶻ⁻¹ e⁻ᵗ dt, Re(z) > 0

Properties:
- Γ(1) = 1, Γ(1/2) = √π
- Γ(z+1) = zΓ(z) (proved by integration by parts)
- For a natural number n, Γ(n) = (n−1)!
- Γ(n+1/2) = ((2n)!)/(4ⁿ n!) √π

Let us convert our integral ∫₀^∞ rⁿ⁻¹ e^(−r²) dr into a Gamma function.

Substitute t = r²: r = t^(1/2), dt = 2r dr ⇒ dr = dt/(2r) = dt/(2t^(1/2)).

rⁿ⁻¹ dr = (t^(1/2))ⁿ⁻¹ · dt/(2t^(1/2)) = ½ t^((n−2)/2) dt = ½ t^(n/2 −1) dt

Therefore

∫₀^∞ rⁿ⁻¹ e^(−r²) dr = ∫₀^∞ ½ t^(n/2 −1) e⁻ᵗ dt = ½ Γ(n/2)  (C)

### 6) Comparing the two methods to find Sₙ₋₁

Since (A) = (B):

π^(n/2) = Sₙ₋₁ · ½Γ(n/2)

Solving, the surface area of the unit sphere Sⁿ⁻¹ is:

Sₙ₋₁ = (2π^(n/2)) / Γ(n/2)

Check:
- n = 2: Γ(1) = 1, S₁ = 2π¹/1 = 2π (the circumference of the unit circle)
- n = 3: Γ(3/2) = √π/2, S₂ = 2π^(3/2)/(√π/2) = 4π (the surface area of the unit sphere) ✓

### 7) Finding the volume Vₙ(R) — integrating the surface area radially

The volume of a thin spherical shell of radius r is (surface area) × (thickness): Sₙ₋₁ rⁿ⁻¹ dr. Integrating from 0 to R gives the volume of the ball:

Vₙ(R) = ∫₀^R Sₙ₋₁ rⁿ⁻¹ dr = Sₙ₋₁ [rⁿ/n]₀^R = Sₙ₋₁ Rⁿ/n

Substituting Sₙ₋₁:

Vₙ(R) = (2π^(n/2)) / (nΓ(n/2)) Rⁿ

Using the Gamma-function property Γ(z+1) = zΓ(z) with z = n/2 gives Γ(n/2+1) = (n/2)Γ(n/2), so 2/(nΓ(n/2)) = 1/Γ(n/2+1).

Final formula:

Vₙ(R) = (π^(n/2)) / Γ(n/2+1) · Rⁿ

This is the general formula for the volume of an n-dimensional ball. For the unit ball (R=1), Vₙ = π^(n/2)/Γ(n/2+1).

### 8) Checking n = 3 — agreement with the familiar formula

For n = 3: Γ(5/2) = Γ(3/2+1) = (3/2)Γ(3/2) = (3/2)(1/2)Γ(1/2) = (3/4)√π.

V₃(R) = π^(3/2) / ((3/4)√π) · R³ = ⁴⁄₃π R³

This exactly matches the volume of the sphere obtained by various methods in Chapters 1–3.

### 9) Bonus: values in low and high dimensions

- n = 1: V₁(R) = 2R, Γ(3/2) = √π/2, π^(1/2)/Γ(3/2) = 2 ✓
- n = 2: V₂(R) = π R², Γ(2) = 1 ✓
- n = 4: V₄(R) = π² R⁴ / 2
- n = 5: V₅(R) = 8π² R⁵ / 15

As the dimension increases, the volume of the unit ball increases up to n = 5, then decreases toward 0 — a paradoxical property of high-dimensional space.

> **Note — "n = 5 is not intrinsically special":** The fact that the maximum occurs exactly at n = 5 is a coincidence that holds only for R = 1 (the unit ball). Extending Vₙ(R) = π^(n/2)Rⁿ/Γ(n/2+1) to real values of n and differentiating log Vₙ(R) with respect to n shows that the location of the critical point shifts depending on R. As R grows larger, the dimension at which the maximum occurs becomes greater than 5; as R shrinks, it becomes smaller than 5. In other words, rather than "5-dimensional space being intrinsically special," it is simply that, once the radius is fixed at 1, the growth rate of π^(n/2) happens to balance the growth rate of Γ(n/2+1) around n = 5.

**Summary**
∫_(ℝⁿ) e^(−|x|²) dx = π^(n/2) = Sₙ₋₁∫₀^∞ rⁿ⁻¹e^(−r²) dr = Sₙ₋₁·½Γ(n/2)
Sₙ₋₁ = (2π^(n/2))/Γ(n/2), Vₙ(R) = ∫₀^R Sₙ₋₁rⁿ⁻¹dr = (π^(n/2))/Γ(n/2+1) · Rⁿ
n = 3: Γ(5/2) = (3√π)/4 ⇒ V₃(R) = ⁴⁄₃π R³

---

# 5. A Numerical (Probabilistic) Method: Monte Carlo

## 1) This is not a proof but a verification — situating the method

Chapters 1 through 4 gave rigorous mathematical proofs. Cavalieri's principle, the disk method, spherical coordinates, and the Gaussian integral all logically force V = ⁴⁄₃π R³.

Chapter 5's Monte Carlo method is different. It is a method of **approximation and verification**: it uses random numbers to experimentally measure the volume and checks whether the theoretical value ⁴⁄₃π R³ is correct. However, in modern mathematics, physics, and engineering, Monte Carlo is often the only practical method for computing high-dimensional integrals or the volumes of complicated regions, so understanding its principles is important.

> **Core idea:** If it is hard to measure the volume of the sphere directly, scatter points randomly inside an easy-to-handle enclosing shape (a cube) and estimate the volume ratio from the fraction of points that land inside the sphere.

### 2) Setup — the cube and the sphere

Consider the ball B(R) = {(x,y,z) | x²+y²+z² ≤ R²} of radius R.

The smallest cube containing this ball has side length 2R:

C(R) = [−R,R]³ = {(x,y,z) | −R ≤ x,y,z ≤ R}

- Volume of the cube: V_C = (2R)³ = 8R³
- Volume of the sphere: V_B = ? (the theoretical value we already know is ⁴⁄₃π R³)

Scatter N points uniformly inside C(R). Each point (Xᵢ,Yᵢ,Zᵢ) follows an independent uniform distribution over [−R,R].

### 3) Test — is the point inside the sphere?

For each point, compute the squared distance from the origin:

Dᵢ = Xᵢ² + Yᵢ² + Zᵢ²

- If Dᵢ ≤ R², the point is inside the sphere: add 1 to the counter M.
- If Dᵢ > R², the point is outside the sphere: discard it.

M is the number, out of N points, that fall inside the sphere.

### 4) Why does M/N converge to the volume ratio? — the Law of Large Numbers

By geometric probability, the probability p that a single point lands inside the sphere is:

p = V_B / V_C

because, under a uniform distribution, the probability of a point landing in a given region is proportional to that region's volume.

Viewing each point as a Bernoulli trial, M ~ Binomial(N,p). The expected value of M is Np, and its variance is Np(1−p).

**The (strong) law of large numbers:**

M/N →(N→∞, almost surely) p = V_B/V_C

That is, as N grows, the observed ratio M/N converges almost surely to the theoretical volume ratio V_B/V_C.

So the volume estimator is:

V̂_B = (M/N) · V_C = (M/N) · 8R³ = (8M/N) R³

This is the Monte Carlo estimator.

### 5) Connection to π — convergence to π/6

If we already know V_B = ⁴⁄₃π R³, the theoretical ratio is:

p = V_B/V_C = (⁴⁄₃π R³) / 8R³ = π/6 ≈ 0.5235987756

So in simulation, M/N should converge to about 0.5235.... Conversely, M/N can be used to estimate π:

π ≈ 6 · (M/N)

This is the classical way of estimating π via Monte Carlo. In two dimensions, the ratio of a circle's area to a square's area is π/4.

### 6) Error analysis — why 1/√N?

By the central limit theorem, the error in M/N decreases like N^(−1/2).

Since M ~ Binomial(N,p), its standard deviation is √(Np(1−p)). The standard deviation of the ratio M/N is:

SD(M/N) = √(p(1−p)/N)

Since p = π/6 ≈ 0.5236, p(1−p) ≈ 0.249. So

SD ≈ 0.499/√N ≈ 0.5/√N

The standard deviation of the estimator for V_B is V_C times this:

SD(V̂_B) = V_C · √(p(1−p)/N) = 8R³ · 0.5/√N = 4R³/√N

For N = 10⁴, the error is about 0.04 R³; for N = 10⁶, about 0.004 R³. In other words, achieving two decimal digits of accuracy requires about a million points. This is Monte Carlo's drawback: slow convergence. However, in high dimensions, grid-based methods like the disk method require on the order of Nᵈ points, whereas Monte Carlo converges as 1/√N regardless of dimension — making it advantageous in high-dimensional settings.

A 95% confidence interval is V̂_B ± 1.96 · SD.

### 7) Sample Python implementation

```python
import random
import math

def estimate_sphere_volume(R=1.0, N=1000000):
    M = 0
    for _ in range(N):
        # uniform distribution on [-R, R]
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)
        z = random.uniform(-R, R)
        if x*x + y*y + z*z <= R*R:
            M += 1
    V_est = (M / N) * (2*R)**3
    pi_est = 6 * M / N  # independent of R
    return V_est, pi_est, M, N

R = 1.0
for N in [1000, 10000, 100000, 1000000]:
    V_est, pi_est, M, _ = estimate_sphere_volume(R, N)
    print(f"N={N:7d}, M/N={M/N:.5f}, V_est={V_est:.5f}, pi_est={pi_est:.5f}, theoretical V={4/3*math.pi:.5f}")
```

Sample output:
- N = 1,000: M/N ≈ 0.51 ~ 0.54, V ≈ 4.1 ~ 4.3
- N = 1,000,000: M/N ≈ 0.523 ~ 0.524, V ≈ 4.188 ~ 4.192 (theoretical value: 4.18879)

### 8) Significance and limitations — why include this chapter?

- **Advantages:** implementation in under 10 lines, works regardless of dimension, applies to complex regions. Chapter 4 gave the theoretical formula Vₙ = π^(n/2)/Γ(n/2+1) Rⁿ for the volume of an n-dimensional ball, but if one wants to numerically verify the volume of a 100-dimensional ball, Monte Carlo is essentially the only option.
- **Disadvantages:** it is not a rigorous proof, convergence is slow, and it depends on the quality of the random-number generator.
- **The lesson:** analytic generalization (Chapter 4) and numerical verification (Chapter 5) complement each other. Chapter 4 tells us why V must equal ⁴⁄₃π R³; Chapter 5 lets us actually scatter points by computer and see with our own eyes whether the π/6 ratio really emerges.

**Summary**
p = V_sphere/V_cube = V_sphere/(2R)³, V̂_sphere = (M/N)(2R)³ = (8M/N)R³
N→∞ ⇒ M/N →(a.s.) V_sphere/8R³ = π/6, SD(M/N) = √(p(1−p)/N) = O(N^(−1/2))
π ≈ 6(M/N)

---

# 6. Archimedes' Mechanical Method (The Principle of the Lever)

## 1) Why is this method special? — how does it differ from Cavalieri's?

In §1.1, Cavalieri's principle used the idea that if two solids have equal cross-sectional area A(h) at the same height, their volumes are equal — comparing areas directly, at the same position.

Archimedes' mechanical method (*The Method*) is entirely different. It treats cross-sectional area as "weight," hangs those weights at different positions on a lever, and arranges them so that the moments (weight × distance) balance. That is, it exploits the fact that **the areas themselves need not be equal, so long as area × distance is equal**, i.e., balance.

This method was unknown until the Archimedes Palimpsest was discovered in Istanbul in 1906. Archimedes himself wrote that "by this method I first discovered the results, and afterward proved them rigorously by the method of exhaustion." The very relationship between a sphere and its circumscribed cylinder — the one he asked to have inscribed on his tomb — was discovered by this method.

> **The conclusion, stated up front:** Inside a cylinder of radius r and height 2r, inscribe a sphere and a cone of the same radius; then
> V_sphere : V_cone : V_cylinder = 2 : 1 : 3
> That is, the sphere is 2/3 of its circumscribed cylinder.

## 2) The cast of characters — a cylinder and cone four times as large

Archimedes' actual construction is somewhat more involved than the textbook version. According to an AMS commentary[^1]:

> Archimedes determined the ratio of the volume of a sphere to the volume of the circumscribed cylinder. The actual construction involves the cylinder concentric to the circumscribed cylinder but with double the diameter (and consequently four times the volume). Another essential ingredient is the cone with the same base as the large cylinder, and with the same height.

- **Small cylinder (the circumscribed cylinder):** radius r, height 2r, volume V_small = π r² · 2r = 2π r³
- **Large cylinder:** radius 2r, height 2r, volume V_(large) = π(2r)² · 2r = 8π r³ = 4 V_small
- **Large cone:** same base (radius 2r) and same height 2r as the large cylinder; by Euclid's *Elements*, Book XII, Proposition 10, its volume is 1/3 that of the cylinder[^1]

The key equation Archimedes obtains by the mechanical method is:

```
Vol(Sphere) + Vol(Cone) = (1/2) Vol(Large Cylinder)[^1]
```

Since V_(large) = 8π r³, ½V_(large) = 4π r³, and the cone's volume is ⅓V_(large) = ⁸⁄₃π r³, so the sphere's volume is 4π r³ − ⁸⁄₃π r³ = ⁴⁄₃π r³ — that is, 2/3 of the small circumscribed cylinder's volume 2π r³.

## 3) The idea of hanging cross-sections from a lever — the balance argument

According to Eves's modern reconstruction (ETSU lecture notes), place the origin at the sphere's leftmost point N, and lay out the three solids along the x-axis. The sphere's equation is (x−r)²+y² = r², so y² = r² − (x−r)² = 2rx − x² = x(2r−x)[^2].

Slicing at position x with thickness Δx, the approximate volumes of the three cross-sections are:

- Sphere slice: π x(2r−x)Δx [^2]
- Cylinder slice: π r² Δx [^2]
- Cone slice: π x² Δx [^2]

Now let the origin N be the fulcrum of the lever, and hang the sphere and cone slices at the point T(−2r, 0), a distance 2r to the left. A moment is weight (volume) × distance.

The moment about N of the sphere-plus-cone slice:

(π x(2r−x)Δx + π x² Δx)(2r) = (2rπ x − π x² + π x²)(2rΔx) = 4π r² x Δx  (*)  [^2]

The moment of the cylinder slice is (π r² Δx)(x) = π r² x Δx. So if the cylinder slice is moved 4 times as far — that is, 4r to the right — the balance holds. The AMS commentary states the same thing:

> Archimedes shows by elementary geometry that if the two smaller circles are slid along the axis to a point at twice height of the cylinder, and the large circle is left where it is, their areas will exactly balance about a fulcrum at the center[^1]

If this is done simultaneously for every slice, the weight of the whole sphere and the whole cone becomes concentrated at the right-hand point T, while the cylinder remains in its original position on the left.

The cylinder's center of mass lies at the midpoint of its axis — a distance r to the left of the fulcrum. From the lever's balance condition, m d = M D[^1]:

- m = the cylinder's mass (volume), d = r (distance to its center)
- M = the mass of the sphere plus the cone, D = 2r (distance to the endpoint)

Balance would suggest m·r = M·2r; but the actual calculation uses the large cylinder, so the coefficients adjust and the final result is M = ½m. That is:

> the entire sphere and the entire cone, their masses concentrated at the end-point, and on the left the cylinder in its original position... The equation for balancing masses is
> m d = M D [^1]

Therefore V_sphere + V_cone = ½ V_(large cylinder).

## 4) Deriving the ratio — 2 : 1 : 3

V_(large) = 8π r³,
V_(cone, large) = ⅓ V_(large) = ⁸⁄₃π r³.

From the equation V_sphere + V_(cone, large) = ½V_(large) = 4π r³:

V_sphere = 4π r³ − ⁸⁄₃π r³ = ⁴⁄₃π r³

Comparing with the small circumscribed cylinder V_small = 2π r³:

V_sphere = ⅔ V_small

The cone of the same height 2r (base radius r) has volume V_(cone, small) = ⅓π r² · 2r = ⅔π r³, so:

V_sphere : V_cone : V_cylinder = ⁴⁄₃π r³ : ⅔π r³ : 2π r³ = 2 : 1 : 3

This is the famous ratio Archimedes asked to have engraved on his tomb.

## 5) A question of rigor — why didn't Archimedes accept this as a proof?

The ETSU notes make an important point:

> In Archimedes' approach, he considers cross sections and weighs these sections by their areas. In this way, the balancing of the sections does not need any approximation. However, Archimedes avoids summing the cross sections and instead considers the cross sections taken together[^2]

That is, Archimedes avoided summing infinitely many cross-sections, and instead assumed that the cross-sections balance "all together." In modern calculus, this corresponds to the limit of a Riemann sum:

> A Riemann sum based on the slices would be introduced, in this case representing the moments about point N of the slices. A limit as the norm of the partition approaches zero produces the precise value[^2]

so it can be made rigorous through integration. Having discovered the result by this mechanical method, Archimedes went on to prove it rigorously by the method of exhaustion in Proposition 34 of Book I of *On the Sphere and Cylinder*.

**Summary**
Slices: dV_sphere = π x(2r−x)dx, dV_(cone) = π x² dx, dV_(cyl) = π r² dx
2r(dV_sphere + dV_(cone)) = 4r · dV_(cyl) (moment balance)
V_sphere + V_(cone, large) = ½ V_(large) ⇒ V_sphere = ⁴⁄₃π r³
V_sphere : V_cone : V_cylinder = 2 : 1 : 3

[^1]: ams.org — http://www.ams.org/publicoutreach/feature-column/fcarc-archimedes3
[^2]: 11.4. Archimedes' Method of Equilibrium — http://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Eves6-11-4.pdf

---

# The Volume of a Sphere in Ancient Civilizations

## Overview

The modern formula V = ⁴⁄₃π r³ = ⅙π D³ was first rigorously proved by Archimedes (287–212 BC). But before and after him, various civilizations also attempted to estimate — or exactly determine — the volume of a sphere. The key question for each is whether they had a genuine proof, or only a practical formula for measurement purposes.

---

## 1. Ancient Egypt (c. 1850 BC, the Moscow and Rhind papyri)

### 1.1 What survives?

- **Moscow Papyrus, Problem 10:** computing "the surface area of a basket (hemisphere)."
  Original text: "A basket with a mouth of 4½. What is its surface?..."
  Solution: A = (((2×D) × ⁸⁄₉) × ⁸⁄₉) × D = ¹²⁸⁄₈₁ D²
  This computes the surface area of a hemisphere using ²⁵⁶⁄₈₁ ≈ 3.16049 as an approximation of π.

  Whether this problem really computes the surface area of a genuine 3-dimensional hemisphere is, in fact, not settled. A key word at the start of the original text, which specified the shape of the "basket," is illegible due to damage to the papyrus, and ever since W. W. Struve published a German translation in 1930, debate over the identity of this figure has continued to this day. Broadly, three competing interpretations compete.

  Struve and R. J. Gillings, following the traditional reading, take it to be a 3-dimensional hemisphere. T. Eric Peet (1931), the first to challenge this translation, argued that because of the damaged word the original intent cannot be determined with certainty, and offered two alternatives. One is that the problem was never about a 3-dimensional solid at all, but about the area of a 2-dimensional semicircle; the other is that it concerned neither a hemisphere nor a semicircle, but the lateral surface area of a semi-cylinder (a cylinder cut in half lengthwise). Viewed from the side, a semi-cylinder's cross-section is a semicircle, so confusion could have arisen if a scribe, copying down the condition that the diameter and the length were equal, accidentally dropped one of the terms. As it happens, the surface area of a cylinder whose diameter equals its length is exactly equal to the surface area of a sphere of the same diameter, so the hemisphere and semi-cylinder interpretations cannot, in principle, be distinguished purely by their numerical results. Indeed, whichever interpretation is chosen, the papyrus's final answer, obtained by plugging in the original figure 4½, comes out to 32 in either case.

  In 2024, George M. Hollenback contributed new material to this debate.[^eg1] He argues that the two figures given in the original text (base 9, height 4½) correspond exactly to the dimensions of a semicircular segment, and that the computational procedure of the problem — treating the two numbers as the sides of a rectangle and repeatedly reducing the longer side by 1/9 twice — is well suited to computing the area of such a 2-dimensional figure. He points out that both the hemisphere and semi-cylinder interpretations require an additional operation (such as unrolling a 3-dimensional curved surface into a 2-dimensional net) that is not otherwise attested in any Middle Kingdom Egyptian mathematical text, and concludes that the semicircle interpretation is the more parsimonious one.

  In the end, this problem remains without a settled consensus. This document follows the traditional interpretation (the hemisphere reading of Struve and Gillings), which has most widely been cited as an example of computing a hemisphere's surface area, in the discussion that follows — but this should be understood as a choice among several credible competing hypotheses, not a scholarly consensus.

  [^eg1]: Hollenback, George M. (2024), "Another look at the nb.t in the Moscow Mathematical Papyrus," *Prague Egyptological Studies*. — https://dspace.cuni.cz/bitstream/20.500.11956/197835/1/George%20M%20Hollenback_94-105.pdf ; for Peet's two 1931 alternative interpretations, see also: "A new interpretation of Problem 10 of the Moscow Mathematical Papyrus," *Historia Mathematica* — https://www.sciencedirect.com/science/article/pii/S0315086009000305

- **Moscow Papyrus, Problem 14:** correctly computes the volume of a frustum, V = ⅓h(a²+ab+b²) — evidence that the Egyptians could handle solid geometry.

- **Rhind Papyrus, Problems 41 and 48:** approximates the area of a circle of diameter 9 by a square of side 8 (area 64). Since 64 = π(4.5)², this gives π = 256/81.

### 1.2 Where does V ≈ ⁹⁄₁₆D³ come from?

In modern notation, substituting π = 256/81 into V = ⅙π D³ gives V = ¹²⁸⁄₂₄₃ D³ ≈ 0.527 D³. The value ⁹⁄₁₆ D³ = 0.5625 D³ corresponds to π = 27/8 = 3.375. So the Egyptian formula seems to apply some value of π between 3 and 3.16 to the volume of a sphere.

### 1.3 Was there a proof?

**No.** The papyri contain only algorithms — "compute it this way" — with no explanation of why. Modern scholars such as Gillings speculate that "the Egyptians estimated π by counting the areas of polygons inscribed in and circumscribed about a circle," but the papyri themselves contain no such argument. The volume-of-a-sphere formula was likely a practical one tied to units of measurement and capacity (the *heqat*).

- **Conclusion:** Egypt could accurately (or approximately) compute the surface area of a curved figure (presumed to be a hemisphere, semicircle, or semi-cylinder) and the volume of a frustum, but exactly what that surface-area problem was really about remains disputed today, and no deductive proof for the volume of a sphere itself survives.

---

## 2. Babylonia (1900–1600 BC, clay tablets)

### 2.1 What survives?

- The area of a circle is computed as A = 3r²: implying π = 3.
- The Susa tablets (19th–17th century BC) use π = 3⅛ = 3.125.

The tablets record the relation between diameter and circumference as C = 3D.

> While the value π ≈ 3.125 itself is confirmed by many modern studies, there has been scholarly debate — ever since Bruins first proposed it in 1950 — over the method of interpreting the constant "24/25" on the Susa tablet (TMS 3) as the ratio of a regular hexagon's perimeter to its circumscribed circle's circumference, in order to back out this value of π. Separately from this debate, however, it is confirmed that Babylonian tablet computations using the coefficient 0;4,48 (= 1/(4π)), i.e. π ≈ 3.125, for multiplying the square of a circumference to get an area, date back as far as the 23rd century BC.

### 2.2 What about the volume of a sphere?

A formula for the volume of a sphere does not independently appear on Babylonian tablets. While cylinder and cone volumes are treated, it is presumed that spheres — as the three-dimensional extension of the "circle" — were estimated at roughly V ≈ ½D³.

---

## 3. China — Liu Hui (3rd century) and the father-and-son team Zu Chongzhi and Zu Gengzhi (5th century)

### 3.1 The proof

- **Liu Hui (c. 225–295):** In his commentary on the *Nine Chapters on the Mathematical Art*, he attempted but failed to find the volume of a sphere, writing, "I do not know the ratio between the volume of the *mou he fang gai* and the volume of the sphere; I leave this to a wise successor."

- **What is the *mou he fang gai*?** It is the solid formed by the intersection of two mutually perpendicular cylinders of radius r, both inscribed in a cube of side 2r. In the West this is called the Steinmetz solid. Liu Hui discovered that the sphere is inscribed within the *mou he fang gai*, and that sphere : mou-he-fang-gai = π : 4. So once the volume of the mou-he-fang-gai is known, the sphere's volume follows.

- **Zu Chongzhi (429–500) and his son Zu Gengzhi (480–525):** succeeded in finding the volume of the mou-he-fang-gai.

  **Zu Geng's Principle (祖暅原理):** "If solids of equal height have cross-sections of equal area at every height, their volumes are equal" (冪勢既同，則積不容異).

  Proof outline:
  1. At height h, the mou-he-fang-gai's cross-section is a square of side √(r²−h²) with a quarter-circle of the inscribed circle removed.
  2. This matches the cross-section, at the same height, of an inverted pyramid with base r and height r.
  3. The pyramid's volume is ⅓r³, so the volume of 1/8 of the mou-he-fang-gai is r³ − ⅓r³ = ⅔r³.
  4. The whole mou-he-fang-gai is 8 × ⅔r³ = ¹⁶⁄₃r³.
  5. Since sphere : mou-he-fang-gai = π : 4, V_sphere = (π/4) × ¹⁶⁄₃r³ = ⁴⁄₃πr³ = ⅙πD³.

### 3.2 π = 355/113

By computing with an inscribed 12,288-gon, Zu Chongzhi obtained

3.1415926 < π < 3.1415927

and gave the "approximate ratio" 22/7 and the "precise ratio" (密率) 355/113. Since 355/113 = 3.141592920…, the error is 2.7×10⁻⁷ — the best rational approximation with denominator under 16,600.

---

## 4. India — Aryabhata, Brahmagupta, and Bhāskara II

### 4.1 Aryabhata's (476–550) sphere-volume formula and its reception history

In the 7th verse of the *Ganitapada* chapter of the *Aryabhatiya*, right after correctly giving the formula for the area of a circle (half the circumference times the radius), Aryabhata addresses the volume of a sphere. Letting A denote the area of the great circle of the sphere, he gives the sphere's volume as

V_sphere = A√A

that is, in the form V = A^(3/2). Interestingly, Aryabhata himself, in the original Sanskrit, described this result with the word "*niravaśeṣa*" (無餘) — "without remainder," i.e., exact.[^in1] He regarded this not as an approximation but as a rigorous formula.

However, substituting A = πr² gives V = πr²√(πr²) = π^(3/2)r³ ≈ 5.568r³, considerably larger than the true value ⁴⁄₃πr³ ≈ 4.189r³. The scaling (that volume grows as the cube) was correct, but the coefficient was wrong. This is presumed to be an analogical error — extending, without modification, the plane-figure method of multiplying two lengths to get an area, into three dimensions. In the same verse, the volume of a tetrahedron is likewise given incorrectly as V = ½Ah (1.5 times the true value), showing the same pattern of naively applying a lower-dimensional formula to a higher dimension.

The scholarly evaluation of this "error" is more nuanced than commonly summarized. Most historians of mathematics classify it as a genuine computational mistake on Aryabhata's part, but Kurt Elfering (1977) took a different position.[^in2] He argued that if two technical terms in the verse are translated differently from their conventional meanings, correct formulas can be obtained for both the tetrahedron and the sphere. However, this reinterpretation has not been widely accepted, largely because there is no evidence that these terms were used with such meanings in other texts; Filliozat and Mazars (1985), among others, opposed the reinterpretation and supported the original (erroneous) reading. Elfering's view remains a minority position today.

More noteworthy is the subsequent history of reception. Bhāskara I (who wrote a commentary in 629 AD), a direct successor of Aryabhata, apparently did not notice that his teacher's formula was wrong, and used it as-is in his own calculations. That is, even 130-odd years after Aryabhata proposed this formula, even his direct disciple failed to catch the error.[^in3] Brahmagupta (598–668, *Brahmasphutasiddhanta*, 628 AD), famous for sharply criticizing many of Aryabhata's statements, is silent on the volumes of the sphere and tetrahedron — offering no separate rule of his own. Whether this is because he noticed the error, or because he himself did not know the correct value, remains unclear. In the end, it appears that this formula circulated unquestioned within the Indian mathematical tradition for centuries, until Sridhara (8th century) and Bhāskara II (1114–1185) finally corrected it to V = ⁴⁄₃πr³.

In short, the fact that this formula is "numerically wrong" is a separate matter from whether it was "recognized as wrong and rejected from the moment it was published." Aryabhata himself presented it as a rigorous result, and subsequent scholars carried it forward largely unquestioned for a considerable time. It was only corrected centuries after it was first written.

[^in1]: For the original Sanskrit ("ghanagolaphalam niravaśeṣam") and its translation, see: https://www.slideshare.net/slideshow/volume-of-sphere1/47896885 ; for the fuller context of the verse, see the MacTutor biography: https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/
[^in2]: Elfering, K. (1977), "The area of a triangle and the volume of a pyramid as well as the area of a circle and the surface of the hemisphere in the mathematics of Aryabhata I," *Indian Journal of History of Science* 12(2), 232–236 (introduced via MacTutor) — https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/ ; for a rebuttal of the reinterpretation, see Bronkhorst, J., "Pāṇini and Euclid" — https://jainqq.org/explore/269453/7
[^in3]: Bronkhorst, J., "Pāṇini and Euclid: Reflections on Indian Geometry," SOAS — https://www.soas.ac.uk/sites/default/files/2022-06/Jaina%20Versus%20Brahmanical%20Mathematicians%20file112271.pdf

### 4.2 Brahmagupta (598–668, *Brahmasphutasiddhanta*, 628 AD)

Brahmagupta treats the volumes of solids in Chapter 12.

- He corrected the error in the tetrahedron-volume formula, but did not correct the error in the sphere-volume formula.
- Bhāskara II later points out that "even Brahmagupta missed Aryabhata's error in the volume of the sphere."

Brahmagupta's work was translated into Arabic and had a major influence on Arabic astronomy.

### 4.3 Bhāskara II (1114–1185, *Lilavati*) and Sridhara (8th century)

Sridhara stated the correct rule for the sphere's volume, and Bhāskara II established

V = ⁴⁄₃π r³

as the correct formula in the *Lilavati*. The proof resembles Kepler's method: dividing the sphere's surface into small patches and viewing each patch together with the center as forming a pyramid.

V = ⅓ × (surface area) × r = ⅓ × 4π r² × r = ⁴⁄₃π r³

---

## 5. The Islamic World — A Bridge Between Greece and India/Europe

The three brothers of the Banū Mūsā (Muḥammad, Aḥmad, and al-Ḥasan), active in the Abbasid "House of Wisdom," brought Thābit ibn Qurra to Baghdad and sponsored the translation of Greek mathematical classics — Archimedes, Apollonius, and others — into Arabic. Their own treatise, *The Book on the Measurement of Plane and Spherical Figures* (*Verba filiorum*), covered the area of a circle and the surface area and volume of a sphere, among other topics; when Gerard of Cremona translated it into Latin in the 12th century, it became one of the standard textbooks of medieval European geometry. This work served as a crucial channel through which Archimedes' result on the volume of a sphere reached Europe.

Later, scholars contemporary with al-Khwārizmī, and Ibn al-Haytham (known in the West as Alhazen, 11th century), independently revisited the problem of the sphere's volume in works such as *On the Measurement of the Sphere*, and Arabic-Persian mathematicians continued to treat the topic steadily up through the 15th-century Persian scholar Jamshīd al-Kāshī. For the most part, these scholars faithfully carried forward Archimedes' results while refining the computational techniques (algebraic representations, decimal expansions, and so on).

The contribution of the scholars of the Islamic Golden Age lay less in "discovering new formulas" than in "refining the Greeks' rigorous proofs into computational tools usable in practice (surveying, architecture, astronomy) and passing them on to the next civilization (Europe)." Without this chapter, there would appear to be a historical gap between Archimedes (Chapter 1) and modern European calculus (Chapter 2 onward), as well as between these and Indian mathematics — but in fact, the Islamic world was filling exactly that gap.

---

# Appendix: Formula Compendium (LaTeX and Mathematica Reference)

*The tables below restate, in compact LaTeX and Mathematica form, the key formulas already derived in the chapters above. They are provided as a quick reference and repeat no new content.*

## 1.1 Cavalieri's Principle

**Sphere cross-section radius**
- LaTeX: $\sqrt{r^2-h^2}$
- Mathematica:
```mathematica
SectionRadius[r_,h_] := Sqrt[r^2 - h^2]
```

**Sphere cross-sectional area**
- LaTeX: $A_{\text{sphere}}(h) = \pi(r^2 - h^2)$
- Mathematica:
```mathematica
CrossSectionSphere[h_,r_] := Pi*(r^2 - h^2)
```

**Hemisphere cross-sectional area**
- LaTeX: $A_{\text{hemisphere}}(h) = \pi(r^2-h^2)$
- Mathematica:
```mathematica
CrossSectionHemisphere[h_,r_] := Pi*(r^2 - h^2)
```

**Cylinder-minus-cone cross-section**
- LaTeX: $A_{C-K}(h) = \pi r^2 - \pi h^2$
- Mathematica:
```mathematica
CrossSectionCylinderMinusCone[h_,r_] := Pi*r^2 - Pi*h^2
```

**Cavalieri integral for volume**
- LaTeX: $V = \int_0^r A(h) dh$
- Mathematica:
```mathematica
VolumeViaCavalieriIntegral[r_] := Integrate[CrossSectionSphere[h,r], {h,0,r}]
```

**Cylinder volume (height r)**
- LaTeX: $V_C = \pi r^2 \cdot r = \pi r^3$
- Mathematica:
```mathematica
VolumeCylinderSmall[r_] := Pi*r^2*r
```

**Cone volume (height r)**
- LaTeX: $V_K = \frac13 \pi r^2 r = \frac13 \pi r^3$
- Mathematica:
```mathematica
VolumeConeSmall[r_] := (1/3)*Pi*r^2*r
```

**Hemisphere volume**
- LaTeX: $V_{\text{hemisphere}} = \pi r^3 - \frac13 \pi r^3 = \frac23 \pi r^3$
- Mathematica:
```mathematica
VolumeHemisphereCavalieri[r_] := VolumeCylinderSmall[r] - VolumeConeSmall[r]
```

**Sphere volume**
- LaTeX: $V_{\text{sphere}} = 2 V_{\text{hemisphere}} = \frac43 \pi r^3$
- Mathematica:
```mathematica
VolumeSphereCavalieri[r_] := 2*VolumeHemisphereCavalieri[r]
```

---

## 1.2 Archimedes' Spherical Cap

**Disk cross-sectional area**
- LaTeX: $A(x) = \pi y^2 = \pi(r^2 - x^2)$
- Mathematica:
```mathematica
DiskArea[x_,r_] := Pi*(r^2 - x^2)
```

**Spherical-cap volume, integral form**
- LaTeX: $V_{\text{cap}}(b) = \int_{b}^{r} \pi(r^2 - x^2) dx$
- Mathematica:
```mathematica
VolumeSphericalCapFromB[b_,r_] := Integrate[Pi*(r^2 - x^2), {x,b,r}]
```

**Expanded integral**
- LaTeX: $\pi\left[ r^2x - \frac{x^3}{3}\right]_{b}^{r}$
- Mathematica:
```mathematica
Integrate[Pi*(r^2 - x^2), {x,b,r}]
```

**Closed form (general)**
- LaTeX: $V = \frac{\pi}{3}(2r^3 - 3r^2b + b^3)$
- Mathematica:
```mathematica
VolumeSphericalCapFromBGeneral[b_,r_] := Pi/3*(2r^3 - 3r^2 b + b^3)
```

**Factorization check**
- LaTeX: $2r^3 - 3r^2b + b^3 = (r-b)^2(2r+b)$
- Mathematica:
```mathematica
FactorCheck[r_,b_] := Expand[(r-b)^2*(2r+b)]
```

**Closed form, final (factored)**
- LaTeX: $V_{\text{cap}} = \frac13\pi(r-b)^2(2r+b)$
- Mathematica:
```mathematica
VolumeSphericalCapFromBClosed[b_,r_] := (1/3) Pi (r-b)^2 (2r+b)
```

**Standard form in terms of height h**
- LaTeX: $V_{\text{cap}}(h) = \frac13\pi h^2(3r-h) = \pi h^2(r - h/3)$
- Mathematica:
```mathematica
VolumeCapHeight[h_,r_] := (1/3) Pi h^2 (3r - h)
VolumeCapHeightAlt[h_,r_] := Pi h^2 (r - h/3)
```

**Relation**
- LaTeX: $b = r-h, h=r-b$
- Mathematica:
```mathematica
b = r - h
```

**Whole sphere (b = −r)**
- LaTeX: $V = \frac13\pi(2r)^2(r) = \frac43\pi r^3$
- Mathematica:
```mathematica
VolumeSphereFromCapB[r_] := VolumeSphericalCapFromBClosed[-r,r]
```

**Whole sphere (h = 2r)**
- LaTeX: $V = \frac13\pi(2r)^2(3r-2r)$
- Mathematica:
```mathematica
VolumeSphereFromCapH[r_] := VolumeCapHeight[2r,r]
```

---

## 1.3 Kepler's Method of Infinitesimal Pyramids

**Circle area via triangle decomposition**
- LaTeX: $A_{\text{circle}} = \frac12 r \times 2\pi r = \pi r^2$
- Mathematica:
```mathematica
AreaCircleViaTriangle[r_] := 1/2 r (2 Pi r)
```

**Pyramid volume formula**
- LaTeX: $V = \frac13 \times \text{base area} \times \text{height}$
- Mathematica:
```mathematica
VolumePyramid[base_,h_] := 1/3 base h
```

**Infinitesimal area of latitude band**
- LaTeX: $dS = 2\pi(r\sin\theta)(r d\theta) = 2\pi r^2 \sin\theta d\theta$
- Mathematica:
```mathematica
dSStrip[r_,theta_] := 2 Pi r^2 Sin[theta]
```

**Sphere surface-area integral**
- LaTeX: $S = \int_0^\pi 2\pi r^2 \sin\theta d\theta = 2\pi r^2[-\cos\theta]_0^\pi = 4\pi r^2$
- Mathematica:
```mathematica
SurfaceAreaSphereViaStrip[r_] := Integrate[2 Pi r^2 Sin[theta], {theta,0,Pi}]
SurfaceAreaSphere[r_] := 4 Pi r^2
```

**Infinitesimal pyramid volume**
- LaTeX: $V(P_i) = \frac13 \Delta A_i \cdot r$
- Mathematica:
```mathematica
dVPyramid[r_,dA_] := 1/3 r dA
```

**Sum for the sphere's volume**
- LaTeX: $V = \sum V(P_i) = \frac13 r \sum \Delta A_i$
- Mathematica:
```mathematica
VolumeSphereKepler[r_] := 1/3 r SurfaceAreaSphere[r]
```

**Final result**
- LaTeX: $V_{\text{sphere}} = \frac13 r S = \frac13 r 4\pi r^2 = \frac43\pi r^3$
- Mathematica:
```mathematica
VolumeSphereKepler[r_] := 4/3 Pi r^3
```

**Connection to the divergence theorem**
- LaTeX: $V = \frac13 \oint \vec r\cdot \hat n dA$, $\nabla\cdot\vec r =3$
- Mathematica:
```mathematica
VolumeViaDivergence[area_,r_] := 1/3 r area
```

---

## 2.1 The Disk Method — Riemann Sums

**Equation of the sphere**
- LaTeX: $x^2+y^2+z^2=r^2$
- Mathematica:
```mathematica
x^2 + y^2 + z^2 == r^2
```

**Cross-section circle radius**
- LaTeX: $R(x)=\sqrt{r^2-x^2}$
- Mathematica:
```mathematica
SectionRadius[r,x]
```

**Cross-sectional area function**
- LaTeX: $A(x)=\pi R(x)^2 = \pi(r^2-x^2)$
- Mathematica:
```mathematica
DiskCrossSection[x_,r_] := Pi*(r^2 - x^2)
```

**Riemann sum**
- LaTeX: $V_n = \sum \pi(r^2-x_i^2)\Delta x$
- Mathematica:
```mathematica
Sum[Pi*(r^2 - xi^2) DeltaX, {i,1,n}]
```

**Hemisphere integral**
- LaTeX: $V_{\text{hemisphere}} = \int_0^r \pi(r^2-x^2)dx = \frac23\pi r^3$
- Mathematica:
```mathematica
VolumeHemisphereDisk[r_] := Integrate[Pi*(r^2 - x^2), {x,0,r}]
```

**Whole-sphere integral**
- LaTeX: $V_{\text{sphere}} = \int_{-r}^{r} \pi(r^2-x^2)dx = \frac43\pi r^3$
- Mathematica:
```mathematica
VolumeSphereDisk[r_] := Integrate[Pi*(r^2 - x^2), {x,-r,r}]
```

**Direct evaluation**
- LaTeX: $\pi\left[r^2x - \frac{x^3}{3}\right]_{-r}^{r}$
- Mathematica:
```mathematica
Pi*(r^2 x - x^3/3) /. {{x->r},{x->-r}}
```

---

## 2.2 The Cylindrical Shell Method

**Shell volume element**
- LaTeX: $dV = 2\pi x \cdot y \cdot dx = 2\pi x \sqrt{r^2-x^2}dx$
- Mathematica:
```mathematica
ShellVolumeElement[x_,r_] := 2 Pi x Sqrt[r^2 - x^2]
```

**Hemisphere integral**
- LaTeX: $V_{\text{hemisphere}} = \int_0^r 2\pi x \sqrt{r^2-x^2}dx$
- Mathematica:
```mathematica
VolumeHemisphereShell[r_] := Integrate[2 Pi x Sqrt[r^2-x^2], {x,0,r}]
```

**Substitution $u=r^2-x^2$**
- LaTeX: $du=-2xdx$, $x=0\to u=r^2$, $x=r\to u=0$
- Mathematica:
```mathematica
u = r^2 - x^2
```

**After substitution**
- LaTeX: $V = \int_{r^2}^{0} -\pi u^{1/2} du = \pi\int_0^{r^2} u^{1/2}du$
- Mathematica:
```mathematica
VolumeHemisphereShellU[r_] := Pi*Integrate[u^(1/2), {u,0,r^2}]
```

**Antiderivative**
- LaTeX: $\int u^{1/2}du = \frac23 u^{3/2}$
- Mathematica:
```mathematica
AntiderivativeSqrt[u_] := 2/3 u^(3/2)
```

**Result**
- LaTeX: $V_{\text{hemisphere}} = \pi\frac23 (r^2)^{3/2} = \frac23\pi r^3$
- Mathematica:
```mathematica
2/3 Pi r^3
```

**Whole sphere**
- LaTeX: $V_{\text{sphere}} = 2V_{\text{hemisphere}} = \frac43\pi r^3$
- Mathematica:
```mathematica
VolumeSphereShell[r_] := 2*VolumeHemisphereShell[r]
```

---

## 2.3 The Pappus–Guldinus Theorem

**Second theorem**
- LaTeX: $V = A\cdot(2\pi\bar r)$
- Mathematica:
```mathematica
PappusVolume[area_,rbar_] := area*(2 Pi rbar)
```

**Half-disk, defined**
- LaTeX: $D=\{(x,y)\mid x^2+y^2\le r^2, y\ge0\}$
- Mathematica:
```mathematica
AreaSemicircularDisk[r_] := 1/2 Pi r^2
```

**Area**
- LaTeX: $A=\frac12\pi r^2$
- Mathematica:
```mathematica
1/2 Pi r^2
```

**Centroid, defined**
- LaTeX: $\bar y = \frac1A\iint_D y dA$
- Mathematica:
```mathematica
YBar = 1/A * Integrate[y, D]
```

**Polar coordinate transformation (2D)**
- LaTeX: $x=\rho\cos\theta, y=\rho\sin\theta, dA=\rho d\rho d\theta$
- Mathematica:
```mathematica
PolarToCartesian2D[rho,theta]
```

**Double integral**
- LaTeX: $\iint_D y dA = \int_0^\pi\sin\theta d\theta \int_0^r\rho^2 d\rho = 2\cdot\frac{r^3}{3}$
- Mathematica:
```mathematica
IntegralYdA[r_] := r^3/3 * 2
```

**Centroid result**
- LaTeX: $\bar y = \frac{2r^3/3}{\pi r^2/2} = \frac{4r}{3\pi}$
- Mathematica:
```mathematica
YBarSemicircleClosed[r_] := 4r/(3 Pi)
```

**Circumference traced by the centroid**
- LaTeX: $L=2\pi\bar y = \frac{8r}{3}$
- Mathematica:
```mathematica
CircumferenceOfCentroid[r_] := 2 Pi*4r/(3 Pi)
```

**Sphere volume**
- LaTeX: $V=A\cdot L = \frac12\pi r^2\cdot\frac{8r}{3} = \frac43\pi r^3$
- Mathematica:
```mathematica
VolumeSpherePappus[r_] := AreaSemicircularDisk[r]*CircumferenceOfCentroid[r]
```

---

## 3.1 Spherical Coordinates

**Transformation**
- LaTeX: $x=\rho\sin\theta\cos\varphi$, $y=\rho\sin\theta\sin\varphi$, $z=\rho\cos\theta$
- Mathematica:
```mathematica
SphericalToCartesian[rho,theta,phi]
```

**Jacobian**
- LaTeX: $|J| = \rho^2\sin\theta$
- Mathematica:
```mathematica
JacobianSpherical[rho_,theta_] := rho^2 Sin[theta]
```

**Volume element**
- LaTeX: $dV = \rho^2\sin\theta d\rho d\theta d\varphi$
- Mathematica:
```mathematica
VolumeElementSpherical[rho_,theta_] := rho^2 Sin[theta]
```

**Integral**
- LaTeX: $V = \int_0^{2\pi}\int_0^\pi\int_0^R \rho^2\sin\theta d\rho d\theta d\varphi$
- Mathematica:
```mathematica
VolumeSphereSpherical[R_] := Integrate[rho^2 Sin[theta], {phi,0,2Pi}, {theta,0,Pi}, {rho,0,R}]
```

**Separation of variables**
- LaTeX: $= (\int d\varphi)(\int\sin\theta d\theta)(\int\rho^2 d\rho)$
- Mathematica:
```mathematica
VolumeSphereSphericalSeparated[R_]
```

**Values of each factor**
- LaTeX: $\int_0^{2\pi}=2\pi$, $\int_0^\pi\sin\theta=2$, $\int_0^R\rho^2=R^3/3$
- Mathematica:
```mathematica
IntPhi[]:=2Pi
IntSinTheta[]:=2
IntRho2[R_]:=R^3/3
```

**Final result**
- LaTeX: $V=2\pi\cdot2\cdot R^3/3 = \frac43\pi R^3$
- Mathematica:
```mathematica
2 Pi*2*R^3/3
```

---

## 3.2 Cylindrical Coordinates

**Transformation**
- LaTeX: $x=r\cos\theta, y=r\sin\theta, z=z$, $dV=r dr d\theta dz$
- Mathematica:
```mathematica
VolumeElementCylindrical[r_]:=r
```

**Condition for the sphere**
- LaTeX: $r^2+z^2\le R^2$, $z\in[-\sqrt{R^2-r^2},+\sqrt{R^2-r^2}]$
- Mathematica:
```mathematica
-Sqrt[R^2 - r^2] <= z <= Sqrt[R^2 - r^2]
```

**Triple integral**
- LaTeX: $V=\int_0^{2\pi}\int_0^R\int_{-\sqrt{R^2-r^2}}^{\sqrt{R^2-r^2}} r dz dr d\theta$
- Mathematica:
```mathematica
VolumeSphereCylindrical[R_] := Integrate[r, {theta,0,2Pi}, {r,0,R}, {z,-Sqrt[R^2-r^2], Sqrt[R^2-r^2]}]
```

**Inner integral**
- LaTeX: $I=\int_0^R 2r\sqrt{R^2-r^2}dr$
- Mathematica:
```mathematica
InnerIntegralCylindrical[R_] := Integrate[2r Sqrt[R^2-r^2], {r,0,R}]
```

**Substitution**
- LaTeX: $u=R^2-r^2$, $du=-2rdr$
- Mathematica:
```mathematica
CylindricalUSubstitution[R_]
```

**Result**
- LaTeX: $I=2/3 R^3$, $V=2\pi\cdot2/3 R^3$
- Mathematica:
```mathematica
2/3 R^3
```

---

## Chapter 4: The n-Dimensional Ball

**1-dimensional Gaussian**
- LaTeX: $\int_{-\infty}^\infty e^{-t^2}dt = \sqrt\pi$
- Mathematica:
```mathematica
Gaussian1D[] := Sqrt[Pi]
```

**2-dimensional check**
- LaTeX: $(\int e^{-x^2}dx)^2 = \iint e^{-(x^2+y^2)} = \pi$
- Mathematica:
```mathematica
Gaussian2DCheck[] := Pi
```

**n-dimensional, direct**
- LaTeX: $\int_{\mathbb R^n} e^{-|x|^2}dx = \pi^{n/2}$
- Mathematica:
```mathematica
GaussianNDirect[n_] := Pi^(n/2)
```

**Separation via spherical coordinates**
- LaTeX: $= S_{n-1}\int_0^\infty r^{n-1}e^{-r^2}dr$
- Mathematica:
```mathematica
S_{n-1} * IntegralRnExp
```

**Connection to the Gamma function**
- LaTeX: $\int_0^\infty r^{n-1}e^{-r^2}dr = \frac12\Gamma(n/2)$
- Mathematica:
```mathematica
IntegralRnExp[n_] := 1/2 Gamma[n/2]
```

**Surface area of the unit n-sphere**
- LaTeX: $S_{n-1}=2\pi^{n/2}/\Gamma(n/2)$
- Mathematica:
```mathematica
SurfaceAreaUnitNSphere[n_] := 2 Pi^(n/2)/Gamma[n/2]
```

**n-dimensional volume integral**
- LaTeX: $V_n(R)=\int_0^R S_{n-1}r^{n-1}dr = S_{n-1}R^n/n$
- Mathematica:
```mathematica
VolumeNBallViaSurface[n_,R_] := SurfaceAreaUnitNSphere[n] R^n/n
```

**General final formula**
- LaTeX: $V_n(R)=\pi^{n/2}/\Gamma(n/2+1) R^n$
- Mathematica:
```mathematica
VolumeNBall[n_,R_] := Pi^(n/2)/Gamma[n/2+1] R^n
```

**Check at n = 3**
- LaTeX: $\Gamma(5/2)=3\sqrt\pi/4$, $V_3=4/3\pi R^3$
- Mathematica:
```mathematica
VolumeNBall[3,R]
```

**Specific dimensions**
- LaTeX: $V_4=\pi^2 R^4/2$, $V_5=8\pi^2 R^5/15$
- Mathematica:
```mathematica
VolumeNBall4[R_] := Pi^2/2 R^4
VolumeNBall5[R_] := 8 Pi^2/15 R^5
```

---

## Chapter 5: Monte Carlo

**Enclosing cube**
- LaTeX: $C(R)=[-R,R]^3$, $V_C=(2R)^3=8R^3$
- Mathematica:
```mathematica
VolumeCubeEnclosing[R_] := (2R)^3
```

**The sphere**
- LaTeX: $B(R)=\{x^2+y^2+z^2\le R^2\}$
- Mathematica:
```mathematica
IsInsideSphere[x_,y_,z_,R_] := x^2 + y^2 + z^2 <= R^2
```

**Probability**
- LaTeX: $p=V_B/V_C$
- Mathematica:
```mathematica
ProbabilityInsideSphere[] := Pi/6
```

**Expectation**
- LaTeX: $M\sim\text{Binomial}(N,p)$, $M/N\to p$
- Mathematica:
```mathematica
M/N -> p
```

**Estimator**
- LaTeX: $\hat V_B = M/N\cdot8R^3$
- Mathematica:
```mathematica
VolumeEstimateMonteCarlo[M_,N_,R_] := M/N (2R)^3
```

**Theoretical ratio**
- LaTeX: $p=\frac{4/3\pi R^3}{8R^3}=\pi/6\approx0.523598$
- Mathematica:
```mathematica
Pi/6
```

**π estimate**
- LaTeX: $\pi\approx6M/N$
- Mathematica:
```mathematica
PiEstimateMonteCarlo[M_,N_]:=6 M/N
```

**Standard deviation**
- LaTeX: $\text{SD}(M/N)=\sqrt{p(1-p)/N}\approx0.5/\sqrt N$
- Mathematica:
```mathematica
SDRatio[p_,N_]:=Sqrt[p(1-p)/N]
```

**Volume standard deviation**
- LaTeX: $\text{SD}(\hat V_B)=4R^3/\sqrt N$
- Mathematica:
```mathematica
SDVolumeEstimate[R_,N_]:=4 R^3/Sqrt[N]
```

**Simulation (with implementation)**
- LaTeX: Python function `estimate_sphere_volume`
- Mathematica:
```mathematica
EstimateSphereVolumeMonteCarlo[R_, N_] := Module[{pts, m},
  pts = RandomReal[{-R, R}, {N, 3}];
  m = Count[pts, {x_, y_, z_} /; x^2 + y^2 + z^2 <= R^2];
  m/N (2 R)^3
]
```

---

## Chapter 6: Archimedes' Lever (Appendix)

**Small cylinder**
- LaTeX: $V_{small}= \pi r^2\cdot2r=2\pi r^3$
- Mathematica:
```mathematica
VolumeCylinderArchimedesSmall[r_]:=Pi r^2 2r
```

**Large cylinder**
- LaTeX: $V_{large}= \pi(2r)^2\cdot2r=8\pi r^3=4V_{small}$
- Mathematica:
```mathematica
VolumeCylinderArchimedesLarge[r_]:=Pi (2r)^2 2r
```

**Large cone**
- LaTeX: $V_{cone,large}=1/3 V_{large}=8/3\pi r^3$
- Mathematica:
```mathematica
VolumeConeArchimedesLarge[r_]:=(1/3)VolumeCylinderArchimedesLarge[r]
```

**Slices**
- LaTeX: $dV_{sphere}=\pi x(2r-x)dx$, $dV_{cone}=\pi x^2dx$, $dV_{cyl}=\pi r^2dx$
- Mathematica:
```mathematica
SphereSliceArchimedes[x_,r_]:=Pi x (2r - x)
ConeSliceArchimedes[x_]:=Pi x^2
CylinderSliceArchimedes[r_]:=Pi r^2
```

**Moment balance**
- LaTeX: $2r(dV_{sphere}+dV_{cone})=4\pi r^2 x dx$
- Mathematica:
```mathematica
MomentSpherePlusCone[x_,r_] := 2r (SphereSliceArchimedes[x,r] + ConeSliceArchimedes[x])
```

**Equilibrium**
- LaTeX: $V_{sphere}+V_{cone,large}=1/2 V_{large}$
- Mathematica:
```mathematica
EquilibriumCheck[r_] := VolumeSphereCavalieri[r] + VolumeConeArchimedesLarge[r] == (1/2) VolumeCylinderArchimedesLarge[r]
```

**Result**
- LaTeX: $V_{sphere}=4\pi r^3-8/3\pi r^3=4/3\pi r^3$
- Mathematica:
```mathematica
VolumeSphereCavalieri[r]
```

**Ratio**
- LaTeX: $V_{\text{sphere}}:V_{\text{cone}}:V_{\text{cylinder}}=2:1:3$
- Mathematica:
```mathematica
RatioArchimedesNormalized[]:={2,1,3}
```

---

## Chapter 7: Historical Approximations (Appendix)

**Egypt, Rhind**
- LaTeX: $\pi=256/81\approx3.16049$, $A=64=\pi(4.5)^2$
- Mathematica:
```mathematica
PiEgyptRhind[]:=256/81
```

**Egyptian volume**
- LaTeX: $V\approx9/16 D^3\approx0.5625 D^3$
- Mathematica:
```mathematica
VolumeEgypt[D_]:=9/16 D^3
```

**Modern conversion**
- LaTeX: $V=128/243 D^3\approx0.527 D^3$
- Mathematica:
```mathematica
VolumeModernFromEgyptPi[D_]:=128/243 D^3
```

**Babylonia**
- LaTeX: $A=3r^2$, $\pi=3$, $\pi=3\frac18=3.125$
- Mathematica:
```mathematica
PiBabylonian1[]:=3
PiBabylonian2[]:=3+1/8
```

**China, Liu Hui's mou-he-fang-gai**
- LaTeX: $V_{mhfg}=16/3 r^3$, $V_{\text{sphere}}:V_{mhfg}=\pi:4$
- Mathematica:
```mathematica
VolumeMouHeFangGai[r_]:=16/3 r^3
```

**China, the sphere**
- LaTeX: $V_{\text{sphere}}=\pi/4\cdot16/3 r^3=4/3\pi r^3=1/6\pi D^3$
- Mathematica:
```mathematica
VolumeSphereViaMouHe[r_]:=Pi/4*16/3 r^3
```

**Zu Chongzhi's precise ratio (密率)**
- LaTeX: $3.1415926<\pi<3.1415927$, $355/113$
- Mathematica:
```mathematica
PiZuChongzhiMilu[]:=355/113
```

**India, Aryabhata's error**
- LaTeX: $V=A\sqrt A$, $A=\pi r^2$ → $V=\pi^{3/2}r^3$
- Mathematica:
```mathematica
VolumeAryabhataError[r_]:=(Pi r^2) Sqrt[Pi r^2]
```

**Bhāskara, exact**
- LaTeX: $V=1/3\cdot\text{surface area}\cdot r = 4/3\pi r^3$
- Mathematica:
```mathematica
VolumeBhaskara[r_]:=4/3 Pi r^3
```

**Modern**
- LaTeX: $V=4/3\pi r^3 = 1/6\pi D^3$
- Mathematica:
```mathematica
VolumeSphereModern[r_]:=4/3 Pi r^3
VolumeSphereDiameter[D_]:=1/6 Pi D^3
```
