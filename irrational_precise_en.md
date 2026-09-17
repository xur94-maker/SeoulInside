# How Do You Compute Irrational Numbers? — How Is √2 Calculated?

---

# A. TL;DR

**Irrational numbers like √2 aren't computed with "one exact formula that gives the answer in a single shot." Instead, they're computed by repeatedly turning a wrong guess into a slightly better guess.** Starting from a rough guess (say, 1.4), you repeatedly check "is the square of this value bigger or smaller than 2?" and nudge the value accordingly — and the guess converges on the true answer at a frightening speed. This adjustment rule is exactly **Newton's method**, and with it, **the number of correct digits roughly doubles with every iteration.** A computer can run this loop only a few dozen times and reach hundreds of thousands of digits. This article comes with a tool that actually performs this computation for real (not just in theory) and shows the result.

---

# B. A Very Detailed Explanation and History of Newton's Method

## B-1. First, Why Is √2 Such a "Troublesome" Number?

Integers (1, 2, 3...) and fractions (1/2, 3/4...) compute cleanly. But numbers like √2, √5, or the golden ratio are provably numbers that **no fraction, however precise, can ever hit exactly**. These are called "irrational numbers."

For example, if you write √2 as a decimal:

```
1.41421356237309504880168872420969807856967187537694...
```

This decimal never ends, and no particular pattern in it ever repeats. In other words, "writing out the exact answer in full" is simply impossible from the start. All we can do is **"find an approximation as close as we want."** And that is precisely what this article's tool does — it lets you push "as close as you want" all the way to 500,000 digits after the decimal point.

## B-2. "Guess and Refine" — An Intuitive Understanding

Picture a number-guessing game. Someone thinks of a number between 1 and 100, and every time you guess, they only tell you "higher" or "lower." With just that hint, you can zero in on the answer surprisingly fast.

Finding √2 works similarly. For the question "what number, squared, gives 2?":

1. Start with any guess. Say, **1.4**.
2. Squaring 1.4 gives **1.96**. That's a bit less than 2, so we should nudge the guess up a little.
3. Try **1.42** this time. Squared, that's **2.0164**. Now it's a bit more than 2, so we should nudge it down slightly.
4. Keep repeating this process, and the value gradually tightens in on the number whose square is 2 — that is, √2.

The question is how to decide "how much to raise or lower it." Adjusting by feel alone would be endlessly slow. This is where **Newton's method** comes in — a rule that determines mathematically, and very efficiently, exactly how much to adjust.

## B-3. Understanding Newton's Method Through an Analogy

The core idea of Newton's method is this:

> **"Near the current guess, treat the original problem as if it were briefly a straight line, and jump directly to the point that line points to as the answer."**

If you zoom in very closely on a curve, it looks almost like a straight line. Newton's method exploits exactly this fact. From where you currently stand, you draw a line tangent to the curve, calculate "if this were the line, where would the answer be?", and jump to that spot. Since the actual curve isn't a perfect line, you won't hit the exact answer in one shot — but **you'll land much closer to the answer than where you started.** Repeat this just a few times, and the error shrinks dramatically.

For finding √2, working out this rule gives the following remarkably simple formula:

```
new guess = (previous guess + 2 ÷ previous guess) ÷ 2
```

In other words, it's simply **averaging the "previous guess" with "2 divided by the previous guess."** You can even try this by hand without a calculator.

- Guess: 1.4
- 2 ÷ 1.4 = 1.42857...
- Average: (1.4 + 1.42857) ÷ 2 = **1.41429** (already correct to the second decimal place: the true value is 1.41421...)
- Once more: 2 ÷ 1.41429 = 1.41413..., average = **1.41421356...** (already correct to nearly eight decimal places!)

You can see accuracy explode after just two iterations. This is exactly the phenomenon where "the number of correct digits roughly doubles with each iteration" (covered in more detail in the next section).

## B-4. Why Does "Taking the Average" Work So Well?

Here's an intuitive way to see it. Suppose some guess `x` is greater than √2. Then `2/x` must be **smaller** than √2 (since the two numbers must multiply to exactly 2, if one is big the other must be small). In other words, `x` and `2/x` are always **two values straddling the true answer**. Taking their midpoint (average) always pulls you in toward the neighborhood of the actual answer. What's more, this "speed of converging toward the middle" isn't just arithmetically slow — it's a very special speed that accelerates quadratically.

## B-5. History — When and by Whom Was This Method Invented?

What's interesting is that **this method existed long before Newton.**

**① Ancient Babylon (circa 1800–1600 BCE)**
Among the surviving clay tablets is an artifact called "YBC 7289," which shows a square and its diagonal, with a cuneiform number engraved beside it representing an approximation of √2. This value is recorded in base 60, and converted to decimal it comes out to roughly **1.41421296...** — matching the true value (1.41421356...) to an astonishing five decimal places. Scholars estimate that the Babylonians were likely already using an "averaging" iterative procedure essentially identical to what we now call "Newton's method." That's why this method is also called the **"Babylonian method."**

**② Ancient Greece — Heron of Alexandria (circa 1st century CE)**
Heron, a Greek mathematician and engineer, explicitly wrote down a procedure for finding square roots in his works. That's why this iterative procedure is also widely known as **"Heron's method."** Mathematically, it's identical to the Babylonian method — "take the average of a guess and the quotient of dividing by that guess."

**③ 17th Century — Isaac Newton and Joseph Raphson**
The name we now use, "Newton's method," traces back to Isaac Newton. Around 1669, Newton **wrote** a work titled "De analysi per aequationes numero terminorum infinitas," in which he described a procedure for iteratively approximating the roots of polynomial equations. (This work wasn't published until 1711, and Newton's method wasn't widely disclosed until 1736 through "The Method of Fluxions and Infinite Series.") However, Newton's original description was somewhat different from the form we learn today (the general formula using derivatives), and his notation was more complicated.

Later, **Joseph Raphson** reorganized and published this procedure in a much more concise, algebraic form in his 1690 work "Analysis Aequationum." This is why today's college math/engineering textbooks refer to this method jointly as the **"Newton-Raphson method."**

Interestingly, what Newton and Raphson dealt with was originally a general procedure for solving **polynomial equations in general**. "Finding a square root" is merely a **special case** that emerges when this general method is applied to the very simple equation `f(x) = x² - N`. Historically speaking, then:

```
Babylonian/Heron's "square-root averaging" procedure  (special case, much older)
              ↓ (generalized, millennia later)
Newton-Raphson's "general root-finding" procedure  (general case, 17th century)
```

That's the order in which things developed. So when we say today that we're "finding a square root using Newton's method," we're actually re-expressing the historically older Babylonian/Heron method within the more general Newton-Raphson framework established much later.

**④ 20th Century Onward — The Computer Age**
With the advent of electronic computers in the mid-20th century, Newton's method became a practically vital tool for implementing hardware division circuits, square-root functions (`sqrt`), and floating-point arithmetic in general. Because it requires few iterations and converges quickly, it was especially advantageous for computing with gradually increasing precision. A famous example is the "fast inverse square root" trick from 1990s video games (Quake III), which combined a **bit trick (the magic constant `0x5f3759df`) with a single iteration of Newton's method** to speed up lighting calculations. Even today, when a browser-based tool like the one accompanying this article computes hundreds of thousands of digits of precision, it's ultimately using the very same principle that was inscribed on clay tablets thousands of years ago.

## B-6. Why Digits "Double" Each Time — Building a Bit More Intuition

In the earlier example, you saw the correct digits grow from 2 → 5 → 8+ digits as the sequence went 1.4 → 1.41429 → 1.41421356... This isn't a coincidence — it's an intrinsic property of Newton's method.

Here's the intuitive reason. When the error is small (when the guess is quite close to the answer), the curve and its tangent line become nearly indistinguishable. But the "difference between the curve and the tangent line" shrinks in proportion to the **square** of the error (because of the second-order and higher terms that cause the curve to bend). So each time the error shrinks, the next error becomes smaller by roughly the square of the current one.

- If the error was 0.01 (about 2 correct digits) → the next error is about 0.0001 (about 4 correct digits)
- If the error was 0.0001 (4 digits) → the next error is about 0.00000001 (8 digits)

This is exactly how the number of "correct digits" nearly exactly doubles with each iteration. In mathematical terms, this property is called **quadratic convergence**. (A rigorous formal proof of this appears in Chapter 4 of Section C below.)

## B-7. So What's Different About a Computer?

When a person computes by hand, they're satisfied with a decimal of around 15 digits like "1.4," but a computer can run this iterative procedure using pure integer arithmetic with no limit on the number of digits (the `BigInt` used in the implementation plays this role — see Appendix C). And because the number of iterations needed grows not in proportion to the number of digits, but only in proportion to **the logarithm of the number of digits** — for example, computing 100,000 digits requires, in theory, fewer than 20 iterations — even hundreds of thousands of digits can be computed almost instantly. (See Chapter 6 of Section C for a detailed analysis of the actual time this takes.)

---

# C. (Earlier Version) Original Technical Document

> Below is the full text of a technical document written earlier, kept as-is for reference. The actual code for this article is gathered at the very bottom in **Appendices A/B/C**. The document below is a detailed explanation directly tied to that code.

## 1. What Is This

The tool accompanying this article is a web tool that actually computes irrational numbers like √2, √5, ∛7, and the golden ratio (φ) to as many decimal digits as you want (up to 500,000 digits) and displays the result.

The key word here is "actually." Most calculators use JavaScript's default real-number type (`double`), which cannot accurately represent more than about 15–16 digits. To sidestep this limitation, this tool directly implements **fixed-point arithmetic** using `BigInt` (arbitrary-size integers) together with **Newton's method**, genuinely performing as many iterations of computation as there are digits.

It additionally shows two more things:
- A table recording, at each iteration, how many digits match the true answer (so you can visually see the convergence speed)
- An animated graph showing the geometric principle of Newton's method (the process of finding the next approximation from where the tangent line meets the x-axis)

## 2. Why Is This Needed — The Limits of `double`

A computer's default real-number type, `double` (double-precision floating point, IEEE 754), stores values in the following form:

```
value = sign × mantissa × 2^exponent
```

The mantissa is 52 bits, which translates to roughly **15–17 significant decimal digits**. Beyond that, there's simply no storage space left, so the remaining digits get rounded off or discarded.

For example, if you compute `Math.sqrt(5)` in a JavaScript console:

```
2.23606797749979
```

it cuts off right there. From the 16th digit onward, the information simply doesn't exist. It's not that "a more precise value theoretically exists but can't be represented" — the computation process itself never produces precision beyond that point.

**Why does this matter?**
- Fields like cryptography, numerical-analysis research, and record-chasing computations of pi/irrational numbers often need hundreds to tens of thousands of digits of precision.
- When many operations are chained together, `double`'s rounding errors accumulate, and it's common to end up with far fewer than even 15 trustworthy digits.

That's why this tool removes `double` from the core of the computation entirely and instead adopts an approach that **simulates real numbers using only integer arithmetic (fixed-point)**. Integer arithmetic, done with `BigInt`, has no limit on the number of digits.

## 3. Core Math 1 — Newton's Method

### 3.1 General Principle

Newton's method is an iterative algorithm for finding a solution to `f(x) = 0`. At the current approximation `x_n`, you draw the tangent line to the function, and take the point where that tangent line crosses the x-axis as the next approximation `x_{n+1}`.

```
x_{n+1} = x_n - f(x_n) / f'(x_n)
```

Geometrically, this is the repeated process of "drawing a tangent line at a point on the curve and jumping to where it crosses the x-axis." Since the tangent line approximates the curve, as long as the starting point is close enough to the solution and `f'` varies smoothly, each jump lands substantially closer to the solution.

### 3.2 The Specific Formulas Used in This Tool

**① The k-th root of N** (including √2, ∛7, and user-specified N and k)

What we want to find is the solution to `x^k = N`, i.e., `f(x) = x^k - N = 0`. Since `f'(x) = k·x^(k-1)`, substituting into the general Newton formula gives:

```
x_{n+1} = x_n - (x_n^k - N) / (k·x_n^(k-1))
        = ((k-1)·x_n^k + N) / (k·x_n^(k-1))
```

This is the Newton update for square roots. When k=2, this becomes exactly the equation we commonly know as the "Babylonian square root method":

```
x_{n+1} = (x_n + N/x_n) / 2   (equivalent to the k=2 form above)
```

(See **Appendix A** for the actual code.)

**② The golden ratio φ**

φ is the positive solution to `x² = x + 1`, i.e., `f(x) = x² - x - 1 = 0`. Since `f'(x) = 2x - 1`:

```
x_{n+1} = x_n - (x_n² - x_n - 1) / (2x_n - 1)
        = (x_n² + 1) / (2x_n - 1)
```

(See **Appendix B** for the actual code.)

### 3.3 How the Initial Guess Is Determined

Newton's method may fail to converge, or diverge to an unrelated value, if the starting point is too far from the solution. Fortunately, the functions this tool handles (powers, golden ratio) have the property of converging stably as long as the initial value is reasonably close. (Note, however, that the update formula for φ, `(x²+1)/(2x-1)`, diverges as `x → 0.5`, because the denominator approaches zero — so care is needed when the initial value is near 0.5. See **Appendix B**.)

So this tool uses a clever strategy:

1. First, quickly compute a low-precision approximation like `Math.pow(N, 1/k)` using `double` precision. (This value is only accurate to about 15 digits, but that's plenty for a "starting point.")
2. Convert this value into BigInt fixed-point form and use it as `x_0` for the Newton iteration.

In other words, the approach isn't "trying to find the precise answer from the start with infinite precision," but rather "starting from a roughly correct spot and letting the precision grow on its own through pure integer arithmetic."

## 4. Core Math 2 — Why the Number of Digits Doubles With Each Iteration

Looking at this tool's table (the actual convergence record per iteration step), you can confirm that the "number of matching digits" roughly doubles with each iteration. This isn't a coincidence — it's due to a property of Newton's method called **quadratic convergence**.

### 4.1 Proof Sketch

Let the true value be `r`, and define the error of the n-th approximation as `e_n = x_n - r`. Taylor-expanding `f` around `x_n`:

```
0 = f(r) ≈ f(x_n) + f'(x_n)(r - x_n) + (1/2)f''(x_n)(r - x_n)²
```

Substituting the Newton update formula `x_{n+1} = x_n - f(x_n)/f'(x_n)` and rearranging gives the following relation:

```
e_{n+1} ≈ (f''(x_n) / (2·f'(x_n))) × e_n²
```

That is, **the next error is proportional to the square of the previous error.** The fact that the error shrinks quadratically means that, when converted to decimal digits (number of digits ≈ -log₁₀(error)), **the number of correct digits roughly doubles with each iteration.**

For instance, if the error is 10⁻⁵ (5 correct digits), then in the next iteration the error becomes roughly (10⁻⁵)² = 10⁻¹⁰ (10 correct digits). The tool's explanation that "the number of correct digits roughly doubles with each iteration" directly reflects this fact.

### 4.2 Practical Implications

Thanks to this property, the number of iterations needed to increase precision doesn't grow in proportion to the number of digits, but rather **in proportion to the logarithm of the number of digits**. Even if you need 100,000 digits, log₂(100,000) ≈ 17 iterations are, in theory, enough. This is why the implementation's iteration cap (200) has plenty of headroom. (See **Appendix C**.)

## 5. How the Implementation Works — Simulating Real Numbers with BigInt (Fixed-Point)

`BigInt` only handles integers. Representing decimals requires a trick, and this tool uses **fixed-point** arithmetic.

The idea is simple. To store a real number `r`, you multiply `r` by a power of 10 to turn it into an integer, and store only that integer.

```
R = round(r × 10^P)
```

Here, `P` determines "how many digits after the decimal point to treat as part of the integer." For example, if `r = 2.236` and `P = 3`, then it's stored as the integer `R = 2236`. This way, addition and subtraction become plain integer addition and subtraction; multiplication is simulated as integer multiplication followed by division by `10^P`; and division is simulated by first multiplying the numerator by `10^P` and then doing integer division. This is why `* scale` and `/ scale` appear repeatedly in the code from section 3.2 above and **Appendices A/B**.

### 5.1 Why Is There a GUARD (Buffer Digits)?

Because integer division discards the remainder, every operation introduces a tiny error (up to about 1 ULP). If this error accumulates over many iterations, the tail end of the target number of digits can end up wrong.

To prevent this, the tool computes with 30 extra digits of buffer beyond the actual target number of digits, and discards this buffer when finally truncating the result. In other words, it computes internally to "target digits + 30 digits" and only displays the target number of digits externally. This 30-digit buffer is kept as the constant `GUARD = 30` in **Appendix C**. How much buffer is needed to be safe is actually a topic studied theoretically in the field of arbitrary-precision numerical computation as well (there is research deriving the minimum guard digits needed to guarantee an error within 1 ULP).

## 6. Performance Characteristics — Why Things Get Dramatically Slower as Digits Increase

This tool advertises that "even 100,000 digits takes around 1 second." Digging a bit deeper into this claim:

- BigInt multiplication and division (especially in simple implementations) typically use an approach (the schoolbook algorithm) that takes **O(n²)** time for `n` digits. That is, doubling the number of digits makes a single multiplication/division take 4 times as long.
- Division is generally known to be an even heavier operation than multiplication.
- The number of Newton's-method iterations itself is very small, proportional to log(digits) (see Chapter 4), but **the cost of each individual multiplication/division performed within each iteration** grows in proportion to the square of the number of digits.

So overall, it's theoretically safer to assume that total computation time grows roughly **in proportion to the square of the number of digits**. If it took about 1 second at 100,000 digits, then at this tool's maximum of 500,000 digits (5x), arithmetically it could take about 25 times as long (20+ seconds or more). The guidance that "increasing digits only adds tens of milliseconds to about a second" may hold in the middle range of digit counts, but it's worth keeping in mind that near the maximum, the perceived speed may be slower than that.

---

## 7. Summary — What Connects to What Math

```
[Element of the tool]                          → [Connected math/concept]                     (Code location)

· Why BigInt is used instead of double
    → The limited significant digits of IEEE 754 floating point (~15-16 digits)   (Appendix C)

· The logic of repeatedly refining an approximation
    → Newton's method (x_{n+1} = x_n − f(x_n)/f'(x_n))                     (Appendices A·B)

· The formula for computing √N, ∛N, the k-th root of N
    → The result of applying Newton's method to f(x) = x^k − N               (Appendix A)

· The formula for computing the golden ratio
    → The result of applying Newton's method to f(x) = x² − x − 1            (Appendix B)

· "Matching digits double with each iteration"
    → Newton's method's quadratic convergence (error shrinks quadratically)   (Body, Chapter 4)

· How BigInt represents decimals
    → Fixed-point representation (R = round(r × 10^P))                       (Appendix C)

· GUARD = 30
    → Buffer digits absorbing rounding error from repeated division          (Appendix C)

· Why double is used to set the initial value
    → The closer the initial value is to the solution, the more stable and fast the convergence   (Appendix C)

· Why things slow down as digit count increases
    → The O(n²) time complexity of BigInt multiplication/division            (Body, Chapter 6)
```

---

# Appendix: The Actual Implementation Code

The code below corresponds 1:1 with the explanations in the body above. The first line of each appendix indicates "which section of the body this is the code version of," so you can understand it from the appendix alone without needing to re-read the body.

## Appendix A: The Square-Root Newton Update (`nthRootStep`)

> This is the code version of Body Section 3.2 ①.

**Formula**: `x_{n+1} = ((k-1)·x_n^k + N) / (k·x_n^(k-1))`

**Full code**:

```js
// k-th root Newton update: x_{n+1} = ((k-1)x^k + N) / (k * x^(k-1))
// X, Nfp_asInt, scale are all fixed-point integers (real number × 10^P)
function nthRootStep(X, k, Nfp_asInt, scale) {
  // Compute x^(k-1), x^k in fixed-point
  let pk1 = X; // x^1
  for (let i = 2; i <= k - 1; i++) pk1 = (pk1 * X) / scale;
  const pk = (pk1 * X) / scale; // x^k

  const numerator = BigInt(k - 1) * pk + Nfp_asInt; // (k-1)x^k + N  (fixed-point)
  const denom = BigInt(k) * pk1;                    // k * x^(k-1)  (fixed-point)
  return (numerator * scale) / denom;
}
```

**The key 3 lines** (mapping 1:1 to the formula):

```js
const numerator = BigInt(k - 1) * pk + Nfp_asInt; // (k-1)·x^k + N
const denom     = BigInt(k)   * pk1;              // k·x^(k-1)
return (numerator * scale) / denom;
```

**When k=2**: This formula reduces to `(x + N/x) / 2` — that is, exactly the same averaging seen in section B-3 above: "the average of the previous guess and N divided by the previous guess."

## Appendix B: The Golden Ratio Newton Update (`phiStep`)

> This is the code version of Body Section 3.2 ②.

**Formula**: `x_{n+1} = (x_n² + 1) / (2x_n - 1)`

**Full code**:

```js
// Golden ratio Newton update: x_{n+1} = (x^2+1) / (2x-1)
// Finds the positive root of f(x) = x^2 - x - 1
function phiStep(X, scale) {
  const x2 = (X * X) / scale;
  const numerator = x2 + scale;      // x^2 + 1
  const denom = 2n * X - scale;      // 2x - 1
  return (numerator * scale) / denom;
}
```

**Caution**: This formula diverges as `x → 0.5`, since the denominator approaches zero. Because the iteration can become unstable when the initial value is near 0.5, the initial value should start from something comfortably greater than 1 (e.g., a double-precision approximation).

## Appendix C: Fixed-Point Arithmetic and the Computation Loop

> This is the code version of Body Chapters 5, 5.1, and 6.

**Fixed-point representation**: A real number `r` is stored as the integer `R = round(r × 10^P)`.

```js
const GUARD = 30; // Buffer digits to prevent accumulated error during computation
const P = digits + GUARD;
const scale = 10n ** BigInt(P);
```

**Initial value**: A roughly-computed double-precision approximation is converted into a fixed-point integer.

```js
function initialGuess(approxDouble, P) {
  const initDigits = 15;
  const initScale = 10n ** BigInt(initDigits);
  let X = BigInt(Math.round(approxDouble * Number(initScale)));
  if (P > initDigits) {
    X = X * (10n ** BigInt(P - initDigits));
  } else if (P < initDigits) {
    X = X / (10n ** BigInt(initDigits - P));
  }
  return X;
}
```

**Computation loop**: Newton's method is iterated up to the iteration cap. The cap is 200 because, while quadratic convergence means even 500,000 digits should theoretically take about 20 iterations, a generous safety margin has been set.

```js
while (iter < 200) {
  // ... (one iteration)
  let next = (target.kind === 'phi')
    ? phiStep(X, scale)
    : nthRootStep(X, target.k, NfpAsInt, scale);
  // ... (convergence check)
}
```

**Converting the result back to a string**: The stored integer `X` is converted back into a decimal string.

```js
function toDigitString(X, P) {
  const scale = 10n ** BigInt(P);
  const neg = X < 0n;
  const Xa = neg ? -X : X;
  const intPart = Xa / scale;
  const fracPart = Xa % scale;
  return (neg ? '-' : '') + intPart.toString() + '.' + fracPart.toString().padStart(P, '0');
}
```

---

---

# D. Going Further — Other Ways to Compute √2

So far, this article has focused on **Newton's method** as the way to compute √2. But Newton's method **is not the only way to find √2.** The real question to ask is **"why is Newton's method the most widely used?"**

This section exists **to prevent the misconception that "Newton's method = the only method."** It compares 10 different ways of finding √2, laying out each one's convergence speed, pros/cons, and use cases. At the end, it also covers why Newton's method doesn't work for **transcendental numbers like π and e**.

## D-1. The Conclusion First

**No.** Newton's method is **one of the most famous and efficient methods**, but it is **not the only one.** There are **dozens of methods** for finding √2, each differing in **convergence speed, implementation difficulty, and historical background.**

In other words, there is no such thing as "the one and only way to find √2." The real question to ask is **"why is Newton's method the most famous?"**

## D-2. Why Newton's Method Seems Like "the Only One"

### (1) Overwhelming convergence speed
The number of digits **doubles** with every iteration (quadratic convergence). 100 digits → 200 → 400 → … That means **about 10 iterations gets you over 1000 digits.**

### (2) Astonishingly simple to implement
```
x ← (x + N/x) / 2
```
Just **addition, division, and averaging.** There's hardly a simpler method than this.

### (3) An overwhelmingly long history
It traces back to the Babylonian clay tablet YBC 7289, from **around 1800–1600 BCE.** In other words, this method has been used for **about 3,800 years.**

### (4) A widely used standard in computer science
Newton's-method variants are widely used in hardware `sqrt`/`div` circuits, Quake III's fast inverse sqrt, and arbitrary-precision libraries (GMP, MPFR).

These four factors together created the perception that **"Newton's method = the standard for computing √2."** But it is a **"standard," not the "only" method.**

## D-3. The Other Methods — In Detail

### (1) Bisection — the most primitive

**Idea**: Repeatedly halve the interval where the sign of `f(x) = x² - 2` changes.

```
If f(a) < 0 < f(b) on [a, b]:
  m = (a + b) / 2
  if f(m) < 0, then a ← m
  if f(m) > 0, then b ← m
```

- **Convergence speed**: **1 bit** per iteration (about 0.3 digits)
- **Advantage**: **Guaranteed to converge** (as long as f is continuous)
- **Disadvantage**: **Very slow** — reaching 1000 digits takes **about 3,300 iterations**
- **Use case**: Often used **to safely establish an initial value for Newton's method**

Finding √2 by bisection narrows between 1.4 and 1.5 → 1.45 → 1.425 → 1.4125 → … and so on. Reaching 1000 digits needs about 3,300 iterations (versus about 10 for Newton's method).

### (2) Secant Method — Newton's method's cousin

**Idea**: Newton's method uses the **derivative f'(x)**, whereas the secant method approximates it with **a line through two points**.

```
x_{n+1} = x_n - f(x_n) · (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
```

- **Convergence speed**: Order **1.618** (the golden ratio! — the secant method's order of convergence is the root of the equation `x² = x + 1`)
- **Advantage**: **No need to know the derivative**
- **Disadvantage**: **Somewhat slower** than Newton's method, and requires 2 initial values
- **Use case**: When f' is difficult to obtain

For √2, since `f(x) = x² - 2` and `f'(x) = 2x` make Newton's method easy, the secant method isn't really used in practice here.

### (3) Fixed-Point Iteration

**Idea**: Rewrite the equation in the form `x = g(x)` and iterate.

For √2:
```
x = 2/x        (g(x) = 2/x)     → does not converge (oscillates)
x = (x + 2/x)/2                 → this is Newton's method!
x = 1 + 1/(1+x)                 → continued fraction (linear convergence)
```

- **Convergence speed**: **Linear** (error decreases by a constant ratio each iteration)
- **Advantage**: Simple
- **Disadvantage**: **Whether it converges at all depends on the magnitude of g'(r)**

The continued-fraction representation of √2, `√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))`, is a type of fixed-point iteration and has **linear convergence** (much slower than Newton's method).

### (4) Continued Fraction — theoretically beautiful

The continued fraction of √2 is `√2 = [1; 2, 2, 2, 2, ...]`.

- **Convergence speed**: Linear (about 1 digit per step)
- **Advantage**: **A clear pattern** — √2 has a periodic continued fraction
- **Disadvantage**: **Slow**

Mathematically beautiful, but unsuited for practical computation.

### (5) Taylor Series (generalized binomial series)

```
√2 = (1 + 1)^(1/2) = 1 + 1/2 - 1/8 + 1/16 - 5/128 + ...
```

- **Convergence speed**: Linear (very slow)
- **Problem**: The **radius of convergence is 1**, so √2 sits right at the **boundary** → it does converge, but **very slowly**

This series is more useful for computing π or e than for √2. For √2, it's inefficient.

### (6) CORDIC — a classic standard in embedded systems/FPGAs

**Idea**: Rotate a vector using rotation matrices to compute `√(x² + y²)`.

- **Convergence speed**: **1 bit** per iteration
- **Advantage**: Can be implemented using **only addition/shifts** (no multiplication needed)
- **Disadvantage**: Slow
- **Use case**: **Embedded systems, FPGAs, older calculators** (modern CPUs mainly use polynomial approximation + angle reduction instead of CORDIC)

### (7) Goldschmidt's Algorithm — the GPU standard

**Idea**: Similar to Newton's method, but uses **only multiplication**.

```
y_0 ≈ 1/√N
b_0 = N
x_0 = N
Iterate:
  y_{n+1} = y_n (3 - b_n y_n²) / 2
  b_{n+1} = b_n y_{n+1}²
  x_{n+1} = x_n y_{n+1}
```

- **Convergence speed**: **Quadratic** (same as Newton's method)
- **Advantage**: Uses **only multiplication** (no division needed) → **favorable for GPUs/hardware**
- **Disadvantage**: Slightly worse numerical stability than Newton's method

Used in modern GPUs' `rsqrt` (reciprocal square root).

### (8) Analog/Geometric Construction — the ancient method

In ancient Greece, √2 was constructed geometrically using the fact that the diagonal of a square equals √2 times its side. Before Newton, this was the standard.

- **Precision**: **Limited** (by straightedge and compass)
- **Today**: Used for educational purposes

### (9) Variants of Newton's Method

- **Householder's method**: **Cubic convergence** (3x the digits) — faster but more complex
- **Halley's method**: **Cubic convergence** — good for rational-function roots
- **Euler-Chebyshev**: Polynomial approximation

Since quadratic convergence is already enough for √2, these aren't much used for it.

### (10) Numerical Integration/Differential Equations

Just as `dx/dt = x, x(0) = 1` can be solved to find `e`, √2 can also, in principle, be approached via a **differential equation**. But this would be overkill.

## D-4. So Why Is Newton's Method "the Standard"?

Consider the case of √2.

- `f'(x) = 2x` is **trivial** → Newton's method's only real drawback (needing the derivative) disappears.
- The initial value can be as simple as **about 1.4**.
- As a result, **Newton's method is overwhelmingly favorable.**

Just looking at convergence speed: to get 1000 digits, Newton's method takes about 10 iterations, bisection about 3,300, the secant method about 20, and continued fractions about 1000.

**So, "Newton's method is the best choice for √2,"** but it is **not "the only one."**

## D-5. A Good Example of "Not the Only One" — π and e

- **π**: Archimedes (polygons), Machin (series), Ramanujan (ultra-fast), Chudnovsky (today's standard)
- **e**: `(1 + 1/n)^n`, Taylor series, continued fractions

**Newton's method doesn't work for π or e.** This is because they are constants, not roots of an equation. In other words, the equation **"irrational number = Newton's method" applies only to algebraic irrationals** like √2.

**Transcendental numbers (π, e)** require **series/continued fractions/special algorithms.**

## D-6. Summing It Up With an Analogy

"Is the KTX the only way to get from Seoul to Busan?" → **No** (plane, bus, car, bicycle…)

"So is the KTX the best option?" → **In most cases, yes** (fast, comfortable, reasonable)

The same is true for Newton's method and √2.

- **Not the only method** (bisection, continued fractions, secant method, CORDIC…)
- **But the best one** (quadratic convergence + simple implementation + trivial derivative)
- **The historical standard, too** (about 3,800 years)

## D-7. Why This Article's Main Body Made "Newton's Method" the Star

Sections B and C above centered on Newton's method **not "because it's the only one,"** but because:

1. **It's optimal for algebraic irrationals like √2, √5, φ**
2. **The implementation is simple** (perfect for educational purposes)
3. **The history is long and interesting** (Babylon → Heron → Newton)
4. **Quadratic convergence looks dramatic** (digits doubling)

**In other words, Newton's method is optimal for "educational purposes."**

Had this article covered **π** instead, it would have discussed the Machin series, the Ramanujan series, and the Chudnovsky algorithm. **In other words, the best method depends on which kind of irrational number you're dealing with.**

## D-8. Conclusion

**"√2 = Newton's method" is shorthand for "Newton's method is the best choice for √2,"** not **"the only one."** Making this distinction is what can take this article's completeness up a notch.

---

# E. Mathematical Appendix — Rigorous Derivations

> Sections B and C above state the results ("take the average," "digits double each time") somewhat informally. This appendix derives the same facts formally, with calculus and algebra, so the article can stand on its own as a self-contained mathematical reference rather than relying on intuition alone.

## E-1. Deriving the Update Formula From First Principles

### E-1.1 Setting Up the Problem

We want a root of

```
f(x) = x² - 2 = 0
```

Newton's method is defined by drawing the **tangent line** to `f` at the current point `x_n` and using the tangent line's x-intercept as the next guess `x_{n+1}`.

### E-1.2 The Tangent Line

The tangent line to `f` at `x = x_n` is, by definition of the derivative, the best linear approximation to `f` near `x_n`:

```
L(x) = f(x_n) + f'(x_n) (x - x_n)
```

For `f(x) = x² - 2`, we have `f'(x) = 2x`, so:

```
L(x) = (x_n² - 2) + 2x_n (x - x_n)
```

### E-1.3 Finding Where the Tangent Line Crosses the x-Axis

Setting `L(x) = 0` and solving for `x` gives the next approximation `x_{n+1}`:

```
0 = (x_n² - 2) + 2x_n (x_{n+1} - x_n)
2x_n (x_n - x_{n+1}) = x_n² - 2
x_n - x_{n+1} = (x_n² - 2) / (2x_n)
x_{n+1} = x_n - (x_n² - 2) / (2x_n)
```

This is just the general Newton's-method formula `x_{n+1} = x_n - f(x_n)/f'(x_n)` written out for this specific `f`.

### E-1.4 Simplifying Into the "Average" Form

Put the right-hand side over a common denominator:

```
x_{n+1} = (2x_n² - (x_n² - 2)) / (2x_n)
        = (x_n² + 2) / (2x_n)
        = (1/2) · (x_n + 2/x_n)
```

So:

```
x_{n+1} = (x_n + 2/x_n) / 2
```

which is exactly the "average `x_n` with `2/x_n`" rule used in the main article. Nothing was assumed beyond the definition of the derivative — this is a full derivation, not just a pattern that happens to work.

### E-1.5 The Geometric Picture, One More Time

Picture the parabola `y = x² - 2`. At the point `(x_n, x_n² - 2)`, draw the tangent line. Because the parabola curves upward (`f'' = 2 > 0`), the tangent line always sits **below** the parabola except at the point of tangency. This means the tangent line crosses the x-axis **before** the parabola does (i.e., closer to the true root `√2`, on the side the parabola is bending away from) — which is exactly why the Newton step always lands strictly between the old guess and the truth, and never overshoots past the root on the correct side, for this particular convex function.

## E-2. An Exact Identity for the Error (Not Just an Approximation)

Section C-4.1 uses a Taylor-series *approximation* to argue that error shrinks quadratically. For `f(x) = x² - N` specifically, we can actually derive an **exact** identity — no approximation needed.

### E-2.1 Derivation

Let `r = √2` (the true root) and define the error `e_n = x_n - r`. Start from the update formula:

```
x_{n+1} - r = (x_n + 2/x_n)/2 - r
```

Put everything over `2x_n`:

```
x_{n+1} - r = (x_n² + 2 - 2·r·x_n) / (2x_n)
```

Since `r² = 2`, replace the `2` in the numerator with `r²`:

```
x_{n+1} - r = (x_n² - 2·r·x_n + r²) / (2x_n)
            = (x_n - r)² / (2x_n)
```

So we obtain the **exact** identity:

```
e_{n+1} = e_n² / (2x_n)
```

### E-2.2 Why This Is Better Than the Taylor Argument

- It holds **exactly**, for any `x_n ≠ 0`, not just "approximately when `e_n` is small."
- It immediately shows `e_{n+1} ≥ 0` whenever `x_n > 0` — i.e., after the first step every subsequent guess is a slight **over-estimate** of `√2` (approaches from above), which is a fact the numerical table in the tool actually exhibits.
- When `x_n` is close to `r = √2`, the denominator `2x_n ≈ 2√2 ≈ 2.828`, so `e_{n+1} ≈ e_n² / 2.828`. This recovers the Taylor result with an explicit, computable constant instead of a vague "proportional to."
- It confirms **quadratic convergence** directly: if `e_n` has `d` correct digits (`e_n ≈ 10^-d`), then `e_{n+1} ≈ 10^-2d / 2.828`, i.e., **about `2d` correct digits** — the doubling claim, proven exactly rather than sketched.

## E-3. Order of Convergence — A Quantitative Comparison Table

Section D already compares methods qualitatively. Here is the same comparison made quantitative, using the standard definition of **order of convergence** `p`, where `e_{n+1} ≈ C · e_n^p`.

- **Bisection** — order `p = 1` (linear). Halves the interval each step. Iterations for ~1,000 digits: **≈ 3,322** (= 1000 / log₁₀2).
- **Continued fraction** — order `p = 1` (linear). About 1 digit per convergent. Iterations for ~1,000 digits: **≈ 1,000**.
- **CORDIC** — order `p = 1` (linear). About 1 bit per step. Iterations for ~1,000 digits: **≈ 3,322**.
- **Secant method** — order `p ≈ 1.618` (the golden ratio). Superlinear; needs no derivative. Iterations for ~1,000 digits: **≈ 20**.
- **Newton's method** — order `p = 2` (quadratic). `e_{n+1} ≈ C·e_n²`. Iterations for ~1,000 digits: **≈ 10**.
- **Goldschmidt's algorithm** — order `p = 2` (quadratic, same order as Newton, multiplication-only). Iterations for ~1,000 digits: **≈ 10**.
- **Householder's method** — order `p = 3` (cubic). `e_{n+1} ≈ C·e_n³`. Iterations for ~1,000 digits: **≈ 7**.
- **Halley's method** — order `p = 3` (cubic). `e_{n+1} ≈ C·e_n³`. Iterations for ~1,000 digits: **≈ 7**.

Two things stand out:

1. **Order 1 → 2 is the single biggest jump.** Going from bisection/continued fractions (linear) to Newton (quadratic) cuts the iteration count by roughly two orders of magnitude (3,322 → 10).
2. **Order 2 → 3 barely matters here.** Going from Newton (quadratic) to Householder/Halley (cubic) only saves about 3 iterations, at the cost of a noticeably more complex update formula (it needs `f''` as well as `f'`). This is exactly why, as Section D-9 notes, cubic methods are rarely used just to compute √2 — the marginal benefit doesn't justify the added complexity once you already have quadratic convergence.

## E-4. Is √2 Really Irrational? — A Proof

The whole article rests on the premise that √2 cannot be written as a fraction. Here is the classical proof (attributed to the Pythagorean school), by contradiction.

**Claim:** `√2` is not a rational number.

**Proof:** Suppose, for contradiction, that `√2 = p/q` for some integers `p, q` with `q ≠ 0` and `p/q` written in lowest terms (i.e., `p` and `q` share no common factor).

1. Squaring both sides: `2 = p²/q²`, so `p² = 2q²`.
2. This means `p²` is even. Since the square of an odd number is always odd, `p` itself must be even. Write `p = 2k` for some integer `k`.
3. Substituting: `(2k)² = 2q²`, i.e., `4k² = 2q²`, i.e., `q² = 2k²`.
4. By the same reasoning as step 2, `q²` is even, so `q` is also even.
5. But now both `p` and `q` are even — contradicting the assumption that `p/q` was in lowest terms (they'd share the common factor 2).

This contradiction means the original assumption was false: `√2` cannot be written as a ratio of integers. **∎**

### E-4.1 Where √2 Sits in the Bigger Picture

- `√2` is a root of the polynomial `x² - 2 = 0`, which has **integer coefficients**. Any number that satisfies such a polynomial is called an **algebraic number**. So `√2` is irrational, but it *is* algebraic (degree 2, specifically).
- The continued-fraction expansion of `√2` is the simplest possible non-terminating one: `√2 = [1; 2, 2, 2, 2, ...]` (a 1, followed by 2's forever). This periodicity is itself a theorem (Lagrange's theorem: a real number has an eventually periodic continued fraction if and only if it is a root of a quadratic with integer coefficients — i.e., a "quadratic irrational"). This is the deeper reason Section D-3(4) could say the continued fraction of √2 has "a clear pattern": it's not a coincidence, it's guaranteed by √2 being algebraic of degree 2.
- `π` and `e`, by contrast, are **transcendental**: no polynomial with integer (or even rational) coefficients has them as a root. This is precisely why Section D-5's claim — "Newton's method doesn't work for π or e" — is exactly right in a technical sense: Newton's method finds roots of equations `f(x) = 0`, and `π`/`e` are not naturally the root of any simple algebraic `f`. (One *can* apply Newton's method to a transcendental equation like `sin(x) = 0` to approach `π`, but this converges no faster, and is far more delicate to set up correctly, than the dedicated series methods already covered in Section D-5.)

## E-5. A Closing Note on Rounding Error (Tying Back to Section C-5.1)

The exact identity in E-2.1 assumed **infinite-precision** arithmetic. In the tool's actual `BigInt` fixed-point implementation, every multiplication and division is rounded to `P + GUARD` digits, introducing a small extra error of at most about `10^-(P+GUARD)` per operation (one "unit in the last place," or ULP, of the internal representation). Over the roughly `log₂(digits)` iterations needed, these per-step rounding errors can, in the worst case, accumulate roughly linearly — which is precisely why a **fixed buffer of extra digits (`GUARD = 30`)**, rather than zero buffer, is kept internally and only stripped off at the very end (Section C-5.1). The quadratic convergence proved in E-2 guarantees the *mathematical* error shrinks fast; the `GUARD` digits are what keep the *implementation's* rounding error from quietly eating into that guarantee.
