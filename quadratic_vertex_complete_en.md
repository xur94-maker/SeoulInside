# Quadratic Functions, Revisited — Much Easier Than You Remember
### Six ways to find the vertex, and a proof that starts from y = ax² + bx + c

---

## Introduction: Why Quadratics?

The moment you see "x² − 4x + 3," a flood of school-day math memories may come back. But this material is taught around grades 9–10 (the last year of middle school and the first year of high school in Korea), and almost every later topic in math borrows its intuition from here. Looked at again as an adult, it mostly ends with a shrug and an "Oh, that's all it was?"

There is another reason to revisit it: quadratics are close to everyday life.

- The moment a thrown ball reaches its highest point
- The price at which revenue is maximized
- The rectangle with the largest area for a fixed length of fence
- The relationship between a car's speed and its braking distance

Each of these is a question about the "largest" or "smallest" value, and the answer is the **vertex**.

In this article I'll show you **six ways** to find the vertex. In a textbook each method shows up in a different chapter, so they feel like unrelated tricks. In fact they are the same landscape seen from different angles. Once you see the connection, there is almost nothing left to memorize.

### How to read this article: two layers

Each method follows the same pattern.

1. **Try it with numbers.** We fix one expression (x² − 4x + 3) and follow it by hand to build a feel for the idea.
2. **Prove it in general form.** We carry out the same idea symbolically, starting from y = ax² + bx + c. This is the part that tells you the numbers were no coincidence.

The word "proof" can sound intimidating, but every line is just middle-school-level algebra. If proofs feel heavy, reading only the "Try it with numbers" parts is enough to follow the flow. You can come back to the proofs whenever your curiosity kicks in.

There is only one thing we are going to prove:

> **The x-coordinate of the vertex of y = ax² + bx + c (a ≠ 0) is x = −b/2a.**

---

## 0. Warm-Up: Terms and Conventions

Half of what made math hard was probably the vocabulary. Let's pin down the terms first.

**Quadratic function**: a function whose highest-degree term is x². The general form is:

> **y = f(x) = ax² + bx + c** (a ≠ 0)

Here a, b, c are just numbers. If a were 0, the x² term would vanish and we'd have a straight line, which is why the condition a ≠ 0 is attached.

**Parabola**: the shape of a quadratic's graph. If a > 0 it opens upward like a bowl (a U shape); if a < 0 it opens downward like a hill (an ∩ shape).

**Vertex**: the point where the parabola turns around. On a U shape it is the lowest point (the **minimum**); on an ∩ shape it is the highest point (the **maximum**).

**Axis of symmetry**: the vertical line that folds the parabola exactly in half. The vertex always lies on it, and the equation of the axis is the x-coordinate of the vertex.

**Root (solution)**: a value of x with f(x) = 0. On the graph, it is the x-coordinate of a point where the parabola meets the x-axis.

**The star of this article**

> **f(x) = x² − 4x + 3**

Here a = 1, b = −4, c = 3. This expression is nice because the numbers work out cleanly. To give away the answer now: the vertex is **(2, −1)**. We will arrive at it from six different directions.

---

## Path 1: Rewriting the Expression Neatly (Completing the Square)

### The core idea

> A square can never be negative. So when the squared part becomes 0, the whole expression is at its smallest.

Think about (x − 5)². It equals 0 when x is 5, and grows as x moves away from 5 in either direction. It can never go below 0.

So if we can rewrite an expression in the form **(x − p)² + q**, the answer is immediately visible:

- (x − p)² is at least 0, and equals exactly 0 when x = p.
- Therefore the minimum value of f(x) is q, reached at x = p.
- The vertex is **(p, q)**.

### ▶ Try it with numbers

Our goal is to rewrite x² − 4x + 3 in the form (x − p)² + q.

**Step 1: Look only at the part containing x.**

> f(x) = (x² − 4x) + 3

**Step 2: Fill in a number so that it becomes a "perfect square."**

Expanding (x − 2)² gives x² − 4x + 4. Our expression has only x² − 4x, so it is **+4** short. We add 4, but since the value must not change, we subtract 4 right away. Adding and subtracting the same number is the same as adding 0, so the expression stays the same.

> f(x) = (x² − 4x + 4) − 4 + 3

**Step 3: Group the parentheses and do the leftover arithmetic.**

> f(x) = (x − 2)² − 1

**Step 4: Read off the answer.**

(x − 2)² is 0 when x = 2, which makes it as small as possible. At that point f(2) = −1. So the vertex is **(2, −1)**.

#### How did we know to use 4?

It is "the **square** of **half** of the x-coefficient −4." (Half of −4 is −2; squared, that's 4.)

The reason is that (x + m)² = x² + 2mx + m². If the middle coefficient 2m is −4, then m = −2, and the missing constant term is m² = 4. Taking half undoes the "2" in 2m, and squaring produces m². There is no need to memorize anything; just remember that "when you expand (x + m)², the middle term is 2m."

#### When the coefficient is odd and fractions appear

> h(x) = x² + 3x + 1

Half of the coefficient 3 is 3/2, and its square is 9/4.

> h(x) = (x² + 3x + 9/4) − 9/4 + 1
> h(x) = (x + 3/2)² − 5/4

The vertex is (−3/2, −5/4). Fractions don't change the procedure.

#### When a is not 1

> g(x) = 2x² − 8x + 6

If the number in front of x² isn't 1, first factor it out.

> g(x) = 2(x² − 4x) + 6
> g(x) = 2(x² − 4x + 4 − 4) + 6
> g(x) = 2(x − 2)² − 8 + 6
> g(x) = **2(x − 2)² − 2**

The thing to watch is that when you take the −4 out of the parentheses, the 2 in front multiplies it and gives −8. This is the most common slip. The vertex is (2, −2).

### ▶ Prove it in general form

**Step 1.** Factor a out of the terms containing x² and x.

> f(x) = ax² + bx + c = a( x² + (b/a)x ) + c

**Step 2.** We want to make the inside of the parentheses a perfect square. Since (x + m)² = x² + 2mx + m², the middle coefficient 2m must equal b/a.

> 2m = b/a  →  m = b/2a

Then the missing constant is m² = (b/2a)². We **add it and immediately subtract it.**

> f(x) = a( x² + (b/a)x + (b/2a)² − (b/2a)² ) + c

**Step 3.** Group the first three terms as a square. The term we subtracted comes outside the parentheses with a multiplied in.

> f(x) = a( x + b/2a )² − a·(b/2a)² + c

**Step 4.** Simplify the constants outside the parentheses.

> a·(b/2a)² = a·b²/4a² = b²/4a
> f(x) = a( x + b/2a )² − b²/4a + c
> f(x) = a( x + b/2a )² − (b² − 4ac)/4a

**Step 5.** Compare with the form a(x − p)² + q.

> **p = −b/2a**
> **q = −(b² − 4ac)/4a**

**Step 6.** Read off the conclusion.

If a > 0, then a(x − p)² ≥ 0 and equals 0 only at x = p, so f has its minimum value q at x = p. If a < 0, the inequality flips and q is the maximum. Either way, the vertex is

> **(−b/2a, −(b² − 4ac)/4a)**

∎

**Check**: for f(x) = x² − 4x + 3, p = −(−4)/(2·1) = 2 and q = −(16 − 12)/4 = −1. This matches (x − 2)² − 1, which we got by hand. ✔

### Strengths and weaknesses of this path

The strength is that you get not only the x-coordinate of the vertex but also the y-coordinate (the minimum value) in one go. The weakness is that the arithmetic gets messy when the coefficients are awkward fractions.

---

## Path 2: Sliding the Graph Around (Translation)

This path is a picture of what Path 1 gave us, **(x − 2)² − 1**. Once you understand it, you can simply *see* why the completed square tells you the vertex.

### ▶ Try it with numbers

#### The simplest parabola

The graph of y = x² is the most basic U shape, with its vertex at the origin (0, 0).

#### Shift 2 units to the right

y = (x − 2)² is y = x² moved **2 units to the right.**

> Why does "−2" mean "right"? In the original graph the bottom was at x = 0. In the new graph the bottom is where x − 2 = 0, that is, x = 2. The bottom moved to 2, so the graph moved right. That is why the sign feels backwards.

#### Shift 1 unit down

y = (x − 2)² − 1 is moved **1 unit down** once more. This time the sign agrees with intuition: subtract, and it goes down.

#### Conclusion

y = (x − p)² + q is y = x² moved **p to the right and q up**, so its vertex is **(p, q)**. For our expression p = 2 and q = −1, so the vertex is **(2, −1)**.

#### A one-line memory aid

> A number inside the parentheses moves the graph horizontally with the opposite sign; a number outside moves it vertically with the same sign.

### ▶ Prove it in general form

In Path 1 we rewrote the general form as

> f(x) = a(x − p)² + q  (p = −b/2a, q = −(b² − 4ac)/4a)

Move q to the left side and give names to x − p and y − q, calling them X and Y:

> y − q = a(x − p)²  →  **Y = aX²**

Y = aX² is the basic parabola with its vertex at the origin. (If a > 0, then aX² ≥ 0 and equals 0 only at X = 0, so the vertex is at X = 0, Y = 0.)

X = 0 means x = p, and Y = 0 means y = q. Therefore the graph of y = ax² + bx + c is **y = ax² moved p to the right and q up**, and its vertex is (p, q). ∎

This proof also tells us something new:

- **a** determines the shape of the parabola (how narrow or wide it is, and whether it opens up or down).
- **b and c** don't affect the shape at all; they only determine the **position**, through p and q.

In other words, every quadratic graph is just a parabola of the same shape (for the same a), slid into position. The same principle will show up again when you shift trigonometric or exponential graphs, so understanding it once pays off for a long time.

---

## Path 3: The Midpoint of the Two Roots (Symmetry)

### The core idea

> A parabola is perfectly left-right symmetric, like a reflection in a mirror. So the midpoint of the two points where it meets the x-axis is the axis of symmetry.

Picture a bridge. The highest point of an arched bridge sits exactly halfway between its two ends, because the arch is symmetric. A parabola works the same way.

### ▶ Try it with numbers

Solve f(x) = 0 to find the two roots. By factoring,

> x² − 4x + 3 = (x − 1)(x − 3) = 0

The two roots are x = 1 and x = 3.

Their midpoint is

> (1 + 3) ÷ 2 = **2**

So the x-coordinate of the vertex is 2. The y-coordinate is f(2) = 4 − 8 + 3 = −1, and the vertex is **(2, −1)**.

#### You only need one root

If the axis is at 2 and one root is 3, then 3 lies 1 unit to the right of the axis, so the other root is 2 − 1 = **1**. There is no computation here, just a reflection in a mirror.

### ▶ Prove it in general form: rereading the quadratic formula as symmetry

The quadratic formula looks like this:

> x = (−b ± √(b² − 4ac)) / 2a

Split it into two pieces and its meaning becomes clear:

> x = −b/2a **±** √(b² − 4ac)/2a

- First part, **−b/2a**: the "center" shared by both roots
- Second part, **√(b² − 4ac)/2a**: the "spread" that moves away from the center, left and right

Writing out each root:

> x₁ = −b/2a − √(b² − 4ac)/2a
> x₂ = −b/2a + √(b² − 4ac)/2a

Because + and − are paired, the two roots lie on the left and right of the center at the **same distance**. When you add the two roots, the spread cancels out:

> x₁ + x₂ = −2b/2a = −b/a
> (x₁ + x₂)/2 = **−b/2a** ∎

The quadratic formula you memorized in school turns out to have the humble structure "center ± spread."

**Plugging in our expression**: the center is −(−4)/(2·1) = 2, and the spread is √(16 − 12)/2 = 1. So the two roots are 2 ± 1, that is, **1 and 3**.

**Reading it through Vieta's formulas**: the sum of the roots is x₁ + x₂ = −b/a, which is exactly what the calculation above produced. So without finding the roots, you can read "half the sum of the roots" straight from the coefficients. For our expression x₁ + x₂ = 4, and 4/2 = 2.

### A limitation

This path needs real roots (b² − 4ac ≥ 0). For a parabola that never touches the x-axis (for example x² + 1), it can't be used, and the next path comes to the rescue.

---

## Path 4: Two Points at the Same Height (Symmetry Without Roots)

This is the upgraded version of Path 3.

### The core idea

> The power of symmetry is not limited to the points on the x-axis. Any two points at the same height have their midpoint on the axis of symmetry.

The mirror is not only at height 0; it works the same way at every height. Two points on a parabola at the same height are always on opposite sides of the axis of symmetry.

### ▶ Try it with numbers

#### The easiest pair: the y-intercept

When x = 0, f(0) = c. For us that height is 3. Let's find the other x with the same height 3.

> x² − 4x + 3 = 3
> x² − 4x = 0
> x(x − 4) = 0
> x = 0 or x = 4

The two points at height 3 are at x = 0 and x = 4. Their midpoint is

> (0 + 4) ÷ 2 = **2**

We got 2 again.

#### A mental-math shortcut

For an expression of the form x² + bx + c, the c cancels on both sides, leaving x² + bx = 0, that is, x(x + b) = 0. So the pair is always **x = 0 and x = −b**, and the midpoint is −b/2. For us b = −4, so −(−4)/2 = 2. You don't even need scratch paper: look at the coefficient of the linear term, flip its sign, and halve it.

#### Where this path shines

It works even for expressions with no roots, such as x² + 2x + 5 (negative discriminant). The midpoint of 0 and −2 is −1, which is the axis, and since f(−1) = 1 − 2 + 5 = 4, the vertex is (−1, 4). You can find the vertex even if the parabola never touches the x-axis.

### ▶ Prove it in general form

Suppose two different points x₁ and x₂ give the same function value.

> f(x₁) = f(x₂)
> ax₁² + bx₁ + c = ax₂² + bx₂ + c

Cancel c from both sides and collect everything on one side:

> a(x₁² − x₂²) + b(x₁ − x₂) = 0

Since x₁² − x₂² = (x₁ − x₂)(x₁ + x₂), factoring out (x₁ − x₂) gives

> (x₁ − x₂)( a(x₁ + x₂) + b ) = 0

Because x₁ ≠ x₂, we know (x₁ − x₂) ≠ 0. Therefore

> a(x₁ + x₂) + b = 0
> x₁ + x₂ = −b/a
> **(x₁ + x₂)/2 = −b/2a** ∎

So for any two points at the same height, the midpoint is always **−b/2a**. That is the axis of symmetry.

**The y-intercept pair in general form**: solving f(x) = c gives

> ax² + bx = 0  →  x(ax + b) = 0  →  x = 0 or x = −b/a

The midpoint is (0 + (−b/a))/2 = −b/2a. A shortcut that reads directly off the coefficients, no quadratic formula needed.

**Relation to Path 3**: the "two roots" of Path 3 are simply two points at height 0, so Path 3 is a special case of this proof.

### The practical signal of this path

In a quadratic problem, when you see the condition **f(m) = f(n) (m ≠ n)**, it immediately means **the axis of symmetry is x = (m + n)/2.** Knowing just this signal turns many problems into two-liners. (See Practice Problem 3 below.)

---

## Path 5: Finding the Minimum First (the Discriminant)

### The core idea

> Ask "can y take this value?" The boundary of the possible values of y is exactly the y-coordinate of the vertex.

So far we found the x-coordinate first. This path goes the other way and finds the **y-coordinate** first. It uses the fact that the discriminant tells us when a quadratic equation has real roots.

### ▶ Try it with numbers

Suppose the function can take some value k.

> x² − 4x + 3 = k
> x² − 4x + (3 − k) = 0

For a real number x to exist, the discriminant D must be at least 0.

> D = (−4)² − 4·1·(3 − k) = 16 − 12 + 4k = 4 + 4k
> 4 + 4k ≥ 0
> k ≥ −1

So the value of this expression can only exist if it is **−1 or more**. Values below −1 can't be produced. The minimum is therefore **−1**.

#### What is x at that moment?

When k = −1 the equation becomes

> x² − 4x + 4 = 0
> (x − 2)² = 0

a double root x = 2. The vertex is **(2, −1)**.

#### Understanding it with a picture

Draw a horizontal line y = k across the parabola. If the line is below the parabola, they never meet (no roots, D < 0). If the line is above the vertex, they meet at two points (two roots, D > 0). The instant the line just grazes the parabola at a single point is the height of the vertex (double root, D = 0). The condition D = 0 was the signal that "the line just touched the vertex."

### ▶ Prove it in general form

We find the condition for a real x to exist with f(x) = k.

> ax² + bx + c = k
> ax² + bx + (c − k) = 0

The discriminant is

> D = b² − 4a(c − k) = b² − 4ac + 4ak

A real root exists only if D ≥ 0.

> b² − 4ac + 4ak ≥ 0
> 4ak ≥ −(b² − 4ac)

**When a > 0**: divide both sides by 4a (a positive number).

> k ≥ −(b² − 4ac)/4a

The right-hand side is exactly the **q** from Path 1. So function values can exist only when they are at least q, and the minimum is q. (If a < 0, dividing by 4a flips the inequality to k ≤ q, so q is the maximum.)

**The x at that moment**: when D = 0 there is a double root. For ax² + bx + (c − k) = 0, the root in the quadratic formula has its square-root part equal to 0, so

> x = −b/2a ∎

Even the x-coordinate agrees with −b/2a.

**Check**: for h(x) = x² + 3x + 1, D = 9 − 4(1 − k) = 5 + 4k ≥ 0, so k ≥ −5/4. This is the same as the Path 1 result (−5/4). ✔

### The charm of this path

You probably learned the discriminant only as a tool for deciding how many roots an equation has. It also turns out to be a tool for maximum and minimum problems. Seeing the same tool used in a completely different problem gives you the feeling that math is one connected whole.

---

## Path 6: Where the Slope Is Zero (Differentiation)

### The core idea

> At the bottom of a bowl, a ball doesn't roll in either direction. The slope at the bottom is 0.

There is no need to be intimidated by the word "differentiation." It is simply a tool that tells you "how steep the graph is at each point."

### ▶ Try it with numbers

#### Getting a feel for slope

The left slope of a bowl-shaped parabola goes downhill (negative slope), and the right slope goes uphill (positive slope). Somewhere in the middle, where downhill turns into uphill, the slope must be 0. That place is the bottom, the vertex.

#### Doing it

One rule from high school is enough: the derivative of xⁿ is n·xⁿ⁻¹, and the derivative of a constant is 0.

> f(x) = x² − 4x + 3
> f′(x) = 2x − 4

f′(x) is the slope at each point. Find where the slope is 0.

> 2x − 4 = 0
> x = **2**

#### Check: does it really switch from downhill to uphill?

- At x = 1, f′(1) = 2 − 4 = **−2** (downhill)
- At x = 2, f′(2) = 4 − 4 = **0** (flat)
- At x = 3, f′(3) = 6 − 4 = **+2** (uphill)

The order downhill, flat, uphill confirms that x = 2 is where the minimum occurs.

### ▶ Prove it in general form

**Step 1. Differentiate directly from the definition.** The derivative is the limit of "the average slope over a very short interval h."

> f′(x) = lim (h→0) [ f(x + h) − f(x) ] / h

Expand f(x + h):

> f(x + h) = a(x + h)² + b(x + h) + c
> = ax² + 2axh + ah² + bx + bh + c

Subtract f(x):

> f(x + h) − f(x) = 2axh + ah² + bh

Divide by h:

> [ f(x + h) − f(x) ] / h = 2ax + ah + b

As h → 0, the ah term disappears, so

> **f′(x) = 2ax + b**

(This agrees with the high-school rule "xⁿ → n·xⁿ⁻¹.")

**Step 2. Find where the slope is 0.**

> 2ax + b = 0
> **x = −b/2a** ∎

**Step 3. Check that it really is a minimum (or maximum).**

We can write f′(x) = 2ax + b = 2a( x − (−b/2a) ). If a > 0:

- for x < −b/2a, f′ < 0 (downhill)
- for x > −b/2a, f′ > 0 (uphill)

Downhill turns into uphill, so x = −b/2a is a minimum. If a < 0, it's the reverse, and it is a maximum.

**Check**: f(x) = x² − 4x + 3 → f′(x) = 2x − 4 = 0 → x = 2. Since f′(1) = −2 and f′(3) = +2, the slope switches from downhill to uphill. ✔

### What this path means

For quadratics, the earlier methods are often faster, but differentiation is a **master key** that works just as well for cubics, quartics, and far more complicated functions. The quadratic is its practice ground.

---

## Explaining All Six Paths with One Formula

We can explain at once why the six paths all lead to the same place. Let's write the result of Path 1 again.

> **f(x) = a(x − p)² + q**  (p = −b/2a)

Look at two points t away from p on the left and on the right.

> f(p + t) = a(p + t − p)² + q = **at² + q**
> f(p − t) = a(p − t − p)² + q = **at² + q**

Since t² is unchanged when t is replaced by −t, all six paths fall out of this single line.

| Path | How to read it from `f(p ± t) = at² + q` |
|---|---|
| ① Completing the square | at² is 0 only at t = 0, so for a > 0 the minimum is at t = 0, that is, x = p |
| ② Translation | With t = x − p, subtracting q from the height gives y − q = at², the basic form |
| ③ Midpoint of the roots | If f = 0 then at² = −q, so t = ±√(−q/a): two roots equally far from p, on opposite sides |
| ④ Two points at the same height | Equal heights mean equal at², so the points are t and −t. The midpoint is p |
| ⑤ Discriminant | If f = k then at² = k − q. A real t exists only if (k − q)/a ≥ 0. The boundary is k = q |
| ⑥ Differentiation | The slope is the rate of change of at², which is 2at. It is 0 at t = 0 |

So the six paths are all **the single sentence "at² + q" read in different words.** at² is symmetric (t² is even), it is minimal (a square is at least 0), and it has zero slope (the derivative of t² is 2t, which is 0 at t = 0). Three faces of the same fact.

---

## Where the Six Paths Meet

| Path | Core idea | Result |
|---|---|---|
| ① Completing the square | A square is smallest when it is 0 | x = 2 |
| ② Translation | It is the graph of x² moved | x = 2 |
| ③ Midpoint of the roots | A parabola is left-right symmetric | x = 2 |
| ④ Two points at the same height | Symmetry works at every height | x = 2 |
| ⑤ Discriminant | Find the lowest height it can reach | y = −1, x = 2 |
| ⑥ Differentiation | The slope at the bottom is 0 | x = 2 |

All six paths converge on a single formula: **x = −b/2a**.

We were taught that memorizing one formula is enough. But in truth, several different intuitions, "a square is at least 0," "left-right symmetry," and "zero slope," were all pointing to the same answer. That is the beauty of mathematics. Arriving at the same place by different roads is also the strongest evidence that the answer is right.

### Which path is best when?

| Situation | Recommended path |
|---|---|
| An expression that factors immediately | ③ Midpoint of the roots |
| No roots, or messy ones | ④ Two points at the same height, or ① Completing the square |
| Both the x and y of the vertex at once | ① Completing the square |
| Only the minimum (or maximum) is needed | ⑤ Discriminant |
| The condition "f(m) = f(n)" is given | ④ Two points at the same height |
| Drawing or shifting the graph | ② Translation |
| You already know calculus and want speed | ⑥ Differentiation |

---

## Practice: How to Solve Problems Like These

### Problem 1. The fence problem

You want to make a rectangular vegetable garden with 20 m of fencing. If the width is x m, the length is (10 − x) m. For which x is the area the largest?

> Area f(x) = x(10 − x) = −x² + 10x

Since a = −1 and b = 10,

> x = −b/2a = −10/(2·(−1)) = **5**

When it is a 5 m by 5 m square, the area is largest, at 25 m². This problem can also be solved with the midpoint of the roots: the roots of x(10 − x) = 0 are 0 and 10, whose midpoint is 5.

### Problem 2. A ball thrown upward

If the height of a ball thrown upward is h(t) = −5t² + 20t + 1 (meters, seconds), at what time does it reach its highest point?

> t = −b/2a = −20/(2·(−5)) = **2 seconds**

The height is h(2) = −20 + 40 + 1 = **21 m**. Since a is negative, the parabola is ∩-shaped and the vertex is the maximum.

### Problem 3. Using the "same height" signal

For the quadratic f(x) = x² + bx + c, suppose f(1) = f(5) and f(0) = 2. Find the minimum value of f.

**Solution.** Since f(1) = f(5), the axis of symmetry is (1 + 5)/2 = 3. The axis is −b/2, so −b/2 = 3, that is, b = −6. Since f(0) = c = 2,

> f(x) = x² − 6x + 2 = (x − 3)² − 7

The minimum value is **−7**.

**Check.** f(1) = 1 − 6 + 2 = −3 and f(5) = 25 − 30 + 2 = −3. They are indeed equal. ✔

---

## Common Mistakes

1. **Sign errors**: in the completed square (x − 2)², the x-coordinate of the vertex is +2. It is the opposite of the sign inside the parentheses.
2. **Handling the constant when factoring out a**: in 2(x² − 4x + 4 − 4) + 6, it is easy to forget to multiply the −4 by 2 when you take it out.
3. **The 2 in the denominator of −b/2a**: the denominator is all of 2a, "twice a." It is not −b/2·a.
4. **Mixing up the minimum and the maximum**: if a > 0 the vertex is the minimum; if a < 0 it is the maximum.
5. **Forgetting the y-coordinate of the vertex**: after finding x, always substitute it into f(x) to get the y-coordinate too.
6. **The "two different points" condition for same-height points**: in f(x₁) = f(x₂), if x₁ = x₂ the equation carries no information. The midpoint is the axis only when the two points are different.
7. **The direction of the inequality in the discriminant method**: in Path 5, when a < 0 the inequality flips as you divide by 4a. You have to read the result as a maximum, not a minimum.

---

## Closing: But Wait…

If you've read this far, the formula x = −b/2a that you once only memorized probably doesn't feel unfamiliar anymore. The memorized formula turned out to be the meeting point of six natural ideas.

Math may have felt hard not because we weren't smart enough, but because we skipped the flow of thought and memorized only the conclusions. Once you've grasped the intuition, you can rebuild the formula even after forgetting it. The exams are long over, so now you can enjoy it with a relaxed mind.

And yet, something odd catches the eye here.

Quadratics had such clear symmetry. The two sides were a **perfect mirror image** around the vertex, and the center of that symmetry was −b/2a. Differentiation gave us the line f′(x) = 2ax + b, and this line passes through 0 exactly at the axis x = −b/2a, flipping its sign there.

So then, going the other way, what about the cubic function you get by **integrating** the quadratic? For example, integrating our f(x) = x² − 4x + 3 gives

> F(x) = x³/3 − 2x² + 3x (+ C)

Does the clean "left-right symmetry" that quadratics had survive, **in some form**, in the cubic one degree higher?

**Wait — if quadratics had such clear symmetry, does the cubic function you get by integrating one also have some special property???**
