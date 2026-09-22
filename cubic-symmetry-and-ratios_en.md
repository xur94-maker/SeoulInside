# Symmetry and Ratios in Cubic Functions — Why Does This Happen?




## Introduction: It's Not a Formula, It's a Structure

Over dinner with a close friend, the conversation drifted, oddly enough, into the properties of cubic functions.
My friend's question was whether cubic functions have some kind of consistent symmetry, the way quadratic functions do.

Quadratic functions show symmetry intuitively.
Cubic functions may not show it as intuitively, but because the quadratic function you get by differentiating them clearly has symmetry, the cubic function — which is in an integral relationship with it — also turns out to be symmetric.
Interestingly, this topic apparently shows up often in Korea's college entrance exams.

So today, just for fun, I decided to write it up.

**TL;DR**
A cubic function is point-symmetric about the point whose x-value is the x-coordinate of the vertex of its derivative (a quadratic function) — that is, about the point (x, f(x)) at that x-value. That point is also exactly where the line connecting the two extrema of the cubic meets the cubic itself.

---

## 1. Why Only Cubics? — A Comparison Across Degrees

Before understanding the symmetry of cubic functions, you should first ask:

> "Why is it specifically cubic functions that are point-symmetric? Why are linear, quadratic, and quartic functions different?"

Answering this question first gives every proof that follows the context of "so this is why cubics are special."

|Degree|Symmetry|Reason|

|Linear|Point symmetry (about every point)|A straight line|

|Quadratic|Line symmetry (about an axis)|Only the x² term survives|

|**Cubic**|**Point symmetry (about the inflection point)**|**x³ is odd, so the x² term can be eliminated**|

|Quartic|No symmetry in general|The x³ term remains, breaking symmetry|

The key question is: **"What's left after you remove the lower-degree term?"**

For a cubic function, if you eliminate the x² term by translation, the x term stays behind. What's left is "x³ + x — that is, only odd-degree terms," and that's an odd function. Hence point symmetry holds.

For a quartic function, even after eliminating the x³ term by translation, the x term generally stays behind, so the function generally remains asymmetric. It becomes an even function — with the x term vanishing too, leaving only "x⁴ + x², only even-degree terms" — only in the special case where a specific relationship holds among the coefficients (namely, that the extrema are equally spaced, i.e., that the center of symmetry of the derivative, a cubic, lies on the x-axis). So a quartic function generally isn't even guaranteed to have y-axis symmetry (line symmetry), let alone point symmetry.

In other words, cubics always end up with "only odd-degree terms left," while quartics end up that way only under a special condition. This difference — whether removing one term always drags another term down with it, or only does so when an extra condition among the coefficients is met — is the real reason cubic and quartic functions are symmetric in different ways. (The concrete substitution calculation is worked out directly in the proof in Part 2, Chapter 1.)

In short, a cubic function is **"the simplest nonlinear function, and the first example where symmetry and nonlinearity coexist."** This position is exactly what makes cubic functions special, both on exams and in mathematics as a whole.

---

## 2. The Big Picture: Two Perspectives

The point symmetry of cubic functions can be proven from **two completely different sets of ingredients**. What matters here is that arriving at the same conclusion by two entirely different routes is itself evidence that "this symmetry isn't a coincidence — it's baked deep into the structure."

### Perspective 1: The Algebraic View — Erasing the x² Term

For a general cubic f(x) = ax³ + bx² + cx + d, an appropriate translation can eliminate the x² term entirely. The function then takes the form **"odd function + constant."** An odd function is symmetric about the origin, and adding a constant just shifts the center of symmetry upward without destroying the symmetry itself.

The core of this perspective is: **"A cubic function can always be turned into an odd function by translation."** In the main body, we carry this out symbolically all the way through, to show it holds for any cubic — not just a specific example.

### Perspective 2: The Differential View — The Derivative Is a Parabola

The derivative f'(x) = 3ax² + 2bx + c is a quadratic function — a parabola. A parabola is always left-right symmetric about its own vertex (its axis of symmetry). And the x-coordinate of that vertex is −b/(3a), which is exactly the x-coordinate of the inflection point.

The core of this perspective is: **"The single fact that the derivative is a parabola is enough, by itself, to imply the point symmetry of the function."** In the main body, we confirm f'(x₀+t) = f'(x₀−t) symbolically, and from that derive f(x₀+t) + f(x₀−t) = 2f(x₀).

**How the two perspectives relate**: Perspective 1 is an algebraic approach — "shift the function itself to the origin to make it an odd function." Perspective 2 is a differential approach — "start from the symmetry of the derivative." Two completely different sets of ingredients arrive at the same place. Following both paths lets you feel, directly, that symmetry isn't an add-on but the very structure of the cubic function.

---

## 3. What Follows From Symmetry

Point symmetry is beautiful on its own, but the real reason it's powerful on exams is that **a huge number of proportional relationships derive from it**. Symmetry is the seed; the proportional relationships are the stems that grow out of it.

### (1) Symmetry of function values

Let the center of symmetry be x₀. Then the following always holds.

**f(x₀ − t) + f(x₀ + t) = 2f(x₀)**

This is the very definition of point symmetry. If a problem gives you a condition like f(p − q) = f(p + q), that's a signal that "the function has an inflection point at x = p." Start by sketching the graph.

### (2) Symmetry of the derivative's values

The slope of the tangent line is left-right symmetric about the inflection point.

**f'(x₀ − t) = f'(x₀ + t)**

This holds automatically because the derivative is a parabola. This relationship keeps coming up when locating extrema and when solving tangent-line problems.

### (3) Symmetry of the extrema

For a cubic with extrema, the x-coordinates of the two extrema are exactly symmetric about the inflection point.

**x₁ + x₂ = 2x₀**

This is the starting point for every proportional-relationship problem. From here, the "1:1:1 trisection," the "1:√3 ratio," and the "5 equally spaced points" all follow.

### (4) Symmetry of integrals

Integrals over intervals that are symmetric about the inflection point simplify dramatically. In area problems, this property cuts the computation down enormously.

---

## 4. A Map of the Proportional Relationships That Follow

Let's sketch, in advance, what stems grow out of the seed of symmetry. Each concrete proof is worked through, start to finish, on our one running example in the main body.

### ① The 1:1:1 trisection relationship

For a cubic with extrema, the four important x-coordinates adjacent to the inflection point — the extrema, the inflection point, and the point where the function value equals an extremum value — form an arithmetic sequence.

**−2k, −k, 0, k** (with the inflection point placed at the origin)

The spacing is exactly k throughout. This is the "1:1:1."

**Why exactly three equal parts**: The equation for "the point whose function value equals the extremum value" is a cubic equation, but since the extremum point itself is already a root, factoring leaves only a quadratic equation. The sum of its two roots is −k, and since one of them is k, the other is automatically −2k. Because it's a cubic equation, you get exactly three equally-spaced points.

### ② The 1:√3 ratio

Between the x-coordinate of the point where the horizontal line through the inflection point (parallel to the x-axis) meets the cubic's graph, and the x-coordinate of the extremum, there's a 1:√3 relationship.

**Why exactly √3**: From the extremum condition, t² = k²; from the intersection condition, t² = 3k². Since the ratio of t² values is 1:3, the ratio of t itself is 1:√3. A factor of 3 sitting inside a square, once you pull it outside, comes out attached to a square root — that's the real reason √3 appears.

### ③ The 2:1 relationship via tangent lines

Measured from the inflection point, the distance to the point where a horizontal tangent line through an extremum meets the curve again is twice the distance between the extremum and the inflection point. (That second meeting point is not a point of tangency — it's a simple intersection. The only point of tangency, the one that produces a double root, is the extremum itself.)

### ④ 5 equally spaced points (the 1:2 extension)

Applying the horizontal tangent lines at both the left and right extrema gives five equally spaced points.

**−2k, −k, 0, k, 2k**

This isn't a new principle — it's just the 1:1:1 result applied on both sides. Depending on which two intervals you compare, you get 1:2, 2:1, or whichever ratio you're looking for.

### ⑤ The area formula

The area enclosed between a cubic function and its tangent line is proportional to the fourth power of the distance between the point of tangency and the point of intersection.

**S = |a|/12 × |β − α|⁴**

This formula lets you find the area directly, once you know the distance between the two intersection points, without a complicated integral calculation. It's powerful for problems that ask about several area ratios at once.

### ⑥ The formula for the difference in height between the extrema

The difference in height between the local maximum and local minimum is determined by the horizontal distance between the two extrema and the leading coefficient.

**Difference of extrema = |a| · d³ / 2**

Without differentiating and computing each extremum individually, the difference between them falls out immediately once you know the leading coefficient and the distance between the extrema.

---

## 5. Why This Is Powerful on Exams

This symmetry and these proportional relationships are decisive on exams for three reasons.

**First, the amount of computation drops dramatically.** In a complicated extremum problem, if you set up your unknowns directly using the 1:1:1 ratio (e.g., setting the extrema as α, α+k, α+2k), the problem wraps up in a few lines without solving a system of equations.

**Second, it demands an integrated grasp of several concepts at once.** Differentiation, integration, and the relationship between roots and coefficients are all tangled together in a single problem, which makes it a strong discriminator.

**Third, the approach is highly standardized.** Whenever a problem shows a symmetry signal in its conditions — something like f(p−q)=f(p+q), or information about extrema and the inflection point — nearly every problem type can be solved with a single procedure:

> **See a symmetry condition → move the inflection point to the origin → arrange it as an odd function → factor**




---





# Symmetry and Ratios in Cubic Functions — Why Does It Work That Way?


In this article, we'll keep reusing one specific cubic function from start to finish, and for every property, we'll work through the order **check with numbers first → then prove why**.

---

## 0. One Running Example We'll Keep Using

We'll base everything on the following function.

f(x) = x³ − 6x² + 9x + 2

Plotting a few points:

- At x = 0, f(0) = 2
- At x = 1, f(1) = 6  ← local maximum
- At x = 2, f(2) = 4  ← inflection point
- At x = 3, f(3) = 2  ← local minimum

x = 0, 1, 2, 3 are equally spaced (spacing 1), and the values are 2, 6, 4, 2 — keep those numbers in mind, since they'll keep coming back later.

---

## 1. Every Cubic Function Is Symmetric

### Checking with our eyes first

Look at the two points that are 1 unit away from the inflection point x = 2, on either side.

- f(2 − 1) = f(1) = 6
- f(2 + 1) = f(3) = 2
- Average: (6 + 2) / 2 = 4 = f(2)

That matches the inflection point's y-value exactly. In other words,

f(2 − t) + f(2 + t) = 2 × f(2)

holds for every t. This is precisely "point symmetry" — if you rotate the graph 180° about the inflection point, it lands exactly on top of itself.

### How to spot it

If a problem gives you a condition like f(p − q) = f(p + q), that's a signal that "the function has an inflection point at x = p." Start by sketching the graph.

### Proof 1: The algebraic proof — erasing the x² term

Consider a general cubic function.

f(x) = ax³ + bx² + cx + d (with a ≠ 0)

Substituting x = t − b/(3a) makes the x² term vanish completely. Since that's easy to doubt if we only say it in words, let's check it directly with our example. Since a=1, b=−6, we get b/(3a) = −2, i.e., x = t + 2. Expanding it out:

f(t+2) = (t+2)³ − 6(t+2)² + 9(t+2) + 2
　　　 = (t³ + 6t² + 12t + 8) − 6(t² + 4t + 4) + (9t + 18) + 2
　　　 = t³ + (6t² − 6t²) + (12t − 24t + 9t) + (8 − 24 + 18 + 2)
　　　 = t³ − 3t + 4

As you can see, the coefficient of the t² term cancels out exactly, 6 − 6 = 0.

**Let's confirm this isn't a coincidence that only happens for particular numbers, by expanding it symbolically all the way through.**

Substitute x = t − m (where m = b/(3a)) into f(x) = ax³ + bx² + cx + d. First, expand x³, x², and x each as expressions in t.

x³ = (t−m)³ = t³ − 3mt² + 3m²t − m³
x² = (t−m)² = t² − 2mt + m²
x = t − m

Now substitute each into f(x) = ax³+bx²+cx+d and add everything up.

a·x³ = a t³ − 3am t² + 3am² t − am³
b·x² = 　　　 b t² − 2bm t + bm²
c·x = 　　　　　　 c t − cm
d = 　　　　　　　　　 d

Lining these up vertically and collecting coefficients by degree in t:

- Coefficient of t³: a
- Coefficient of t²: −3am + b
- Coefficient of t¹: 3am² − 2bm + c
- Coefficient of t⁰: −am³ + bm² − cm + d

**Let's check the coefficient of t².** Since m = b/(3a):

−3am + b = −3a·(b/3a) + b = −b + b = 0

It comes out to exactly 0 symbolically too. Since this holds no matter what a and b are, we've proven that this substitution makes the t² term vanish for **every** cubic function.

(For reference, working out the coefficient of t¹ gives p = 3am² − 2bm + c = (3ac − b²)/(3a), and the coefficient of t⁰, being the function value at t=0, is automatically q = f(−m) = f(−b/3a) — the y-coordinate of the inflection point. This p and q are the same p and q that will keep appearing later.)

After the substitution, the function takes the form

g(t) = a·t³ + p·t + q

(In our example, g(t) = t³ − 3t + 4.)

Now let's compute g(−t).

g(−t) = a(−t)³ + p(−t) + q = −at³ − pt + q

Adding g(t) + g(−t):

g(t) + g(−t) = 2q

That is, g(−t) = 2q − g(t). This means the graph of g(t) is point-symmetric about the point (0, q). Translating back to the original function, the center of symmetry is:

( −b/(3a), f(−b/(3a)) )

**The one-line takeaway**: Because eliminating the x² term by translation turns a cubic function into "an odd function + a constant," it's inevitable that the function ends up point-symmetric.

### Proof 2: The differential proof — using the symmetry of the derivative (a parabola)

We can prove the same conclusion using completely different ingredients. This time, instead of f(x) itself, we look at its derivative f'(x).

f'(x) = 3ax² + 2bx + c

This is a quadratic function — a parabola. A parabola is always left-right symmetric about its own vertex (axis of symmetry). The x-coordinate of f'(x)'s vertex is:

x = −2b / (2×3a) = −b/(3a)

**This is exactly the same as the x-coordinate of the inflection point.** That's no coincidence — the vertex of the parabola is exactly the point where f''(x) = 0, i.e., where you'd differentiate once more.

Checking with our example: f'(x) = 3x² − 12x + 9, whose vertex is at x=2 — matching the inflection point's location. Computing f'(2+t) and f'(2−t) directly:

f'(2+t) = 3(2+t)² − 12(2+t) + 9 = 3t² − 3
f'(2−t) = 3(2−t)² − 12(2−t) + 9 = 3t² − 3

**They're identical.** Since it's a parabola, of course the function values (here, the slopes) are equal at two points the same distance from the axis of symmetry.

**Let's confirm this in general too, expanding it symbolically all the way through.** Let x₀ = −b/(3a), and expand f'(x₀+t) and f'(x₀−t) each.

f'(x₀+t) = 3a(x₀+t)² + 2b(x₀+t) + c
　　　　 = 3a(x₀² + 2x₀t + t²) + 2bx₀ + 2bt + c
　　　　 = 3a·x₀² + 6a·x₀·t + 3a·t² + 2b·x₀ + 2b·t + c

f'(x₀−t) = 3a(x₀−t)² + 2b(x₀−t) + c
　　　　 = 3a(x₀² − 2x₀t + t²) + 2bx₀ − 2bt + c
　　　　 = 3a·x₀² − 6a·x₀·t + 3a·t² + 2b·x₀ − 2b·t + c

Subtracting the two expressions.

f'(x₀+t) − f'(x₀−t) = (6a·x₀·t + 2b·t) − (−6a·x₀·t − 2b·t) = 12a·x₀·t + 4b·t = 4t(3a·x₀ + b)

Here, since x₀ = −b/(3a), we have 3a·x₀ = 3a×(−b/3a) = −b. Substituting:

4t(3a·x₀ + b) = 4t(−b + b) = 4t × 0 = 0

That is, f'(x₀+t) − f'(x₀−t) = 0 holds for all a, b, c, t. This fully proves — not just for a particular number, but for **any** cubic function — that the derivative's parabola is left-right symmetric about the inflection point's location.

Let's use this single fact alone to prove the point symmetry of f(x). About the inflection point x₀ (which is 2 in our example), define:

k(t) = f(x₀+t) + f(x₀−t) − 2f(x₀)

If we can show this is always 0, we've proven f(x₀+t)+f(x₀−t) = 2f(x₀) — which is exactly the definition of point symmetry.

Differentiating k(t) with respect to t:

k'(t) = f'(x₀+t) − f'(x₀−t)

But as we just confirmed, f'(x₀+t) = f'(x₀−t) (the symmetry of the derivative's parabola), so:

k'(t) = 0  (for every t)

That means k(t) is a constant function, and plugging in t=0 gives k(0) = f(x₀)+f(x₀)−2f(x₀) = 0, so k(t) is always 0. Therefore f(x₀+t) + f(x₀−t) = 2f(x₀) holds for every t — exactly the same conclusion as Proof 1.

**The difference between the two proofs**: Proof 1 is an algebraic approach — "shift the function itself to the origin to make it an odd function." Proof 2 is a differential approach — using only the fact that the derivative is a parabola. Arriving at the same destination from completely different ingredients means this symmetry isn't a coincidence — it's a fact baked deep into the structure of cubic functions.

---

## 2. The "1:1:1" Trisection

### Checking with our eyes first

Back to our example. x = 0, 1, 2, 3 are all spaced 1 apart. But here's the interesting part — look at the values.

- x = 0 → f(0) = 2
- x = 3 → f(3) = 2  (the local minimum)

**There's a point, exactly at an equally-spaced position, whose function value matches an extremum's value.** Is that a coincidence? No.

### Why it happens (proof)

Let's use g(t) = at³ + pt, the function with the inflection point shifted to the origin (in our example: g(t) = t³ − 3t, with k=1).

Setting g'(t) = 3at² + p = 0, we can write the extrema as t = ±k (k>0). (For this to be possible, we need t² = −p/3a > 0, meaning a and p must have opposite signs. If they have the same sign, the cubic simply has no extrema — like f(x)=x³, which is monotonically increasing — and none of the ratio relationships from here on apply in the first place.)

Now let's find "another point whose function value matches the extremum value g(k)."

g(t) = g(k)
a(t³ − k³) + p(t − k) = 0
(t − k)[a(t² + tk + k²) + p] = 0

t = k is the obvious solution (itself), and substituting p = −3ak² from the extremum condition 3ak² + p = 0:

t² + tk + k² − 3k² = 0
t² + tk − 2k² = 0
(t − k)(t + 2k) = 0

So we get the solution t = −2k. (Combining the original factor (t−k) with the one that just appeared, the full factorization is (t−k)²(t+2k) = 0. Of course t=k is a double root — that point was, after all, "the point whose value equals its own." So the only new root that appears is t=−2k, and just that one.)

Summarizing, with the inflection point placed at the origin, the x-coordinates of the four points are:

−2k,  −k,  0,  k

The spacing is exactly k throughout. In our example, k=1, so these are −2, −1, 0, 1 (converting back to the original coordinates: 0, 1, 2, 3). Exactly matches.

**Why exactly three equal parts**: The equation g(t) = g(k) is a cubic equation because of the t³ term. But since we know t=k is already a root, factoring it out leaves only a quadratic, whose two roots sum to −k (by the relationship between roots and coefficients), and since one of them is k, the other is automatically −2k. Because it's a cubic equation, you get exactly three equally-spaced points (1:1:1).

---

## 3. "1 : √3"

### Checking with our eyes first

Let's draw the horizontal line through the inflection point (x=2, y=4) — that is, y = 4 — and find where it meets the graph.

f(x) − 4 = x³ − 6x² + 9x − 2 = 0

Using the fact that x = 2 is a root, factoring gives:

(x − 2)(x² − 4x + 1) = 0

Solving x² − 4x + 1 = 0 gives x = 2 ± √3.

So the three intersection points are x = 2, 2−√3, 2+√3.

Now let's compare two distances.

- Distance to the extremum (measured from the inflection point x=2): |1 − 2| = 1
- Distance to the intersection point we just found: |2+√3 − 2| = √3

**1 : √3** — exactly this ratio appears.

### Why it happens (proof)

Let's use the form g(t) = at³ − 3ak²t with the inflection point at the origin (written so that the extrema come out at ±k; in our example a=1, k=1).

The horizontal line through the inflection point is g(t) = 0, and solving it:

at(t² − 3k²) = 0
t = 0,  t = ±√3·k

The extrema are at t = ±k, and the intersection points we just found are at t = ±√3·k. Comparing the two t² values:

- From the extremum condition: t² = k²
- From the intersection condition: t² = 3k²

Since the ratio of t² values is 1:3, the ratio of t itself is 1:√3. A factor of 3 sitting inside a square, once you pull it outside, comes out attached to a square root — that's the real reason √3 appears.

---

## 4. The Area Formula — Finding the Area Without Computation

(The relationship we find here — "point of tangency at x=1, re-intersection at x=4" — is exactly the "2:1 relationship via tangent lines" previewed in Part 1, ③. Measured from the inflection point (x=2), the distance to the re-intersection point is 2, and the distance to the extremum is 1 — exactly 2:1.)

### Checking with our eyes first

This time let's talk about tangent lines. The tangent at the local maximum (x=1, y=6) is a horizontal line with slope 0, since it's an extremum — that is, y = 6.

f(x) − 6 = x³ − 6x² + 9x − 4

Since it's tangent at x=1, (x−1)² must be a factor. Factoring it out confirms:

(x − 1)²(x − 4) = 0

So this tangent line touches the curve twice at x=1 (a point of tangency), and meets it again at x=4 (a simple intersection).

Now let's find the area between the curve and the tangent line, from x=1 to x=4. Instead of integrating directly, we'll use a formula.

### The formula and its verification

Whenever you can write f(x) − g(x) = a(x − α)²(x − β) (where g is the tangent line), the area from α to β is:

S = |a| / 12 × |β − α|⁴

In our example, a=1, α=1, β=4, so:

S = 1/12 × 3⁴ = 81/12 = 6.75

### Full proof — actually carrying out the integral

Rather than glossing over it with "if you integrate it directly you get the same value," let's compute it fully.

The goal is to evaluate the following definite integral.

∫[α→β] a(x−α)²(x−β) dx

**Substitution**: Let u = x − α. Then x = u + α, and x − β = u + α − β = u − (β−α). Letting d = β − α, we have x−β = u−d. The bounds of integration also change from x=α→β to u=0→d.

∫[0→d] a·u²·(u−d) du

**Expansion**: Since u²(u−d) = u³ − du²:

= a ∫[0→d] (u³ − du²) du

**Carrying out the integration**: Since ∫u³du = u⁴/4 and ∫du²du = d·u³/3:

= a [ u⁴/4 − d·u³/3 ]  (evaluated over 0→d)

**Plugging in the bounds**: At u=0, both terms vanish. At u=d:

= a ( d⁴/4 − d·d³/3 ) = a ( d⁴/4 − d⁴/3 )

**Combining fractions**: d⁴/4 − d⁴/3 = 3d⁴/12 − 4d⁴/12 = −d⁴/12

Therefore:

∫[α→β] a(x−α)²(x−β) dx = a × (−d⁴/12) = −a·d⁴/12 = −a(β−α)⁴/12

**Handling the sign**: Since an area must always be positive, we take the absolute value.

S = | −a(β−α)⁴/12 | = |a|/12 × (β−α)⁴ = |a|/12 × |β−α|⁴

(Why we can write |β−α|⁴ at the end: raising something to the 4th power always yields a positive value, so it doesn't matter whether you compute β−α or α−β — the fourth power is the same either way. In other words, it doesn't matter which side you subtract first.)

This fully proves that the formula holds not just for a particular example, but for any α, β, and a whatsoever.

### Checking with our own example

Let's plug our example's numbers (a=1, α=1, β=4, d=3) into the general proof.

S = |1|/12 × 3⁴ = 81/12 = 6.75

This matches exactly the value (6.75) we got earlier just by plugging into the formula. Now the formula's correctness has been confirmed both by "proof" and by "verification."

---

## 5. The 1:√3 Extension — Up to 5 Equally Spaced Points

### Checking with our eyes first

In Chapter 4, we saw that the horizontal tangent line through the local maximum (x=1, y=6) meets the curve again at x=4. This time, let's find the horizontal tangent line through the local minimum on the other side (x=3, y=2).

f(x) − 2 = x³ − 6x² + 9x = x(x² − 6x + 9) = x(x − 3)²

It's tangent at x=3 (a double root), and meets the curve again at x=0.

Putting it all together, the following five points are all equally spaced, 1 apart.

x = 0,  1,  2,  3,  4
value = 2,  6,  4,  2,  6

**See the pattern?** The value at x=0 (which is 2) matches the local minimum on the opposite side (x=3), and the value at x=4 (which is 6) matches the local maximum on the opposite side (x=1). In other words, the horizontal tangent at each extremum produces "a point at exactly the same height as the extremum on the opposite side."

Comparing any two intervals among these five points:

- (x=1→2)=1, (x=2→4)=2 → a 1:2 ratio
- (x=0→1)=1, (x=1→3)=2 → a 1:2 ratio

### Why it happens

Let's again use g(t)=at³−3ak²t, with the inflection point at the origin. As in Chapter 4, the horizontal tangent through the local minimum (t=k) meets the curve at t=k (double root) and t=−2k. By symmetry, the horizontal tangent through the local maximum (t=−k) meets the curve at t=−k (double root) and t=2k.

Combining the two results:

−2k,  −k,  0,  k,  2k

We get exactly five equally-spaced points, with spacing k. In the end, applying the 1:1:1 result (from Chapter 4) on both sides naturally produces a structure of 5 equally-spaced points, and depending on which two intervals you compare within it, you get 1:2, 2:1, or whatever ratio you're after. It's not a new principle — it's the same principle applied on both sides at once.

---

## 6. The Formula for the Difference in the Extrema — Finding the Height Without Computation

### Checking with our eyes first

In our example, the local maximum is f(1)=6 and the local minimum is f(3)=2, so the difference is 4. And the distance between the two extrema is |3−1| = 2.

The following relationship holds between the two.

Difference of extrema = |a| × (distance between extrema)³ / 2

Plugging in: |1| × 2³ / 2 = 8/2 = 4. It matches exactly.

### Why it happens (proof)

For g(t) = at³ + pt (with extrema at t=±k), the function values at t=k and t=−k are:

g(k) = ak³ + pk,  g(−k) = −ak³ − pk = −(ak³+pk)

So g(k) = −g(−k) (which of course follows, since g is an odd function). Now, which one is the local maximum and which is the local minimum depends on the sign of a — if a>0, the local maximum is at t=−k and the local minimum at t=k; if a<0, it's the reverse. But since our goal is to find "local maximum − local minimum," rather than fixing a sign at the outset, let's just look at the absolute value of the difference between the two values.

|g(k) − g(−k)| = |2g(k)| = |2ak³ + 2pk|

Substituting the extremum condition 3ak² + p = 0, i.e., p = −3ak²:

2ak³ + 2pk = 2ak³ + 2(−3ak²)k = 2ak³ − 6ak³ = −4ak³

So the difference of extrema is |−4ak³| = 4|a|k³. This value itself is always the same, regardless of whether a is positive or negative, and regardless of which extremum is the maximum.

Let d be the distance between the two extrema, so d = 2k, i.e., k = d/2. Substituting:

4|a|(d/2)³ = 4|a| × d³/8 = |a|·d³/2

Difference of extrema = |a| · d³ / 2

**How to use it**: Without differentiating and computing each extremum individually, the difference between them falls out immediately once you know the leading coefficient and the distance between the extrema.

---

## 7. Checking with a Real Problem

Let's actually use the tools we've learned.

**Problem**: The graph of a cubic function f(x), with leading coefficient 1, has an inflection point at (2, 4). Given that the difference between the function's two extrema is 4, find the area enclosed between the tangent line at the local maximum and the curve y=f(x).

**Solution**:

Step 1 — Finding the distance between the extrema (using the Chapter 6 formula)

Difference of extrema = |a|·d³/2, and a=1, difference of extrema=4, so:

4 = 1 × d³ / 2  →  d³ = 8  →  d = 2

So the two extrema are each 1 unit away from the inflection point (x=2) — that is, k=1. The extrema are at x=1 and x=3.

Step 2 — Finding where the tangent at the local maximum meets the curve again (using the Chapter 2 principle)

In the coordinate system with the inflection point at the origin, k=1, so the horizontal tangent through the local maximum (t=−1) meets the curve at t=−1 (double root) and t=2. Converting back to the original coordinates: x=1 (the point of tangency at the local maximum) and x=4 (the re-intersection point).

Step 3 — Applying the area formula (using the Chapter 4 formula)

S = |a|/12 × |β−α|⁴ = 1/12 × |4−1|⁴ = 1/12 × 81 = 6.75

**Answer: 6.75**

Given only two lines of conditions (the location of the inflection point, and the difference of extrema), we were able to find the area without ever needing to fully determine the function's formula. This is exactly why it's worth mastering these tools — problems that look computation-heavy wrap up in just a few lines.

(For reference, the only function satisfying all these conditions is f(x) = x³ − 6x² + 9x + 2 — the exact example we've used throughout this article. The condition that the inflection point's y-coordinate is 4 pins down the constant term as 2; it's worth checking this for yourself.)

---

## 8. Summary

Summarizing the properties we've seen, one line each:

- **Point symmetry**: Necessarily occurs because eliminating the x² term by translation turns the function into an odd function + a constant
- **1:1:1**: Occurs because the cubic equation g(t)=g(k) factors as (t−k)(t+2k)
- **1:√3**: Occurs because the ratio of the extremum condition (t²=k²) to the condition for intersecting the horizontal line through the inflection point (t²=3k²), in terms of squares, is 1:3
- **The area formula**: Occurs because integrating the double-root structure at the point of tangency, (x−α)²(x−β), always simplifies into a fourth-power form
- **5 equally spaced points (the 1:2 extension)**: Occurs because applying the horizontal tangent lines at both the left and right extrema produces the five points −2k,−k,0,k,2k
- **The difference of extrema**: Occurs because the extrema come out in the form ±2ak³, and substituting the distance d=2k simplifies it to |a|d³/2

All six of these derive from a single principle: "moving the inflection point to the origin turns the function into an odd function."

**See a symmetry condition → move the inflection point to the origin → arrange it as an odd function → factor**
