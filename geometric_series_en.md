### TL;DR
- This piece shows how the sum of a geometric series runs through savings deposits, installment savings, loans, real estate, and even option pricing theory (Black–Scholes).
- There's exactly one substitution at the core: the moment you plug **(1 + interest rate)** into the common ratio ρ of a geometric series, the geometric series becomes "finance."
- When you slice the compounding period infinitely thin (m→∞), the geometric series converges to **the constant e**, and the "discrete world" (Σ, stepwise) extends into the "continuous world" (exponential function, smooth).
- The commonly used "nominal rate − inflation rate" for adjusting for inflation is only an **approximation**; there is an exact formula. Under continuous compounding, this subtraction becomes exact with zero error.
- Add probability (random fluctuation of stock prices) on top of this and you get **geometric Brownian motion**, at the end of which sits the **Black–Scholes option pricing formula**. This piece also verifies, with citations to the literature, the limitations of and objections to this model.
- In other words, "computing interest on a savings account" and "pricing an option" look like completely different worlds on the surface, but mathematically they are **siblings sharing the same root**.

---

### Geometric Series

#### Adding it up by hand first

Let's start with numbers. If the first term is 3 and the sequence doubles each time, listing 7 terms gives us:

- 3, 6, 12, 24, 48, 96, 192

Let's call the sum of these 7 numbers S.

- S = 3 + 6 + 12 + 24 + 48 + 96 + 192

You can just punch this into a calculator and get the answer (381). But if there were 700 terms, or 70,000 terms, instead of 7, you couldn't add them one by one. So mathematicians use a trick to get the answer without adding term by term.

#### The trick: shift and subtract

Multiply the S we just made by the common ratio, 2. Every term shifts over by one slot, giving us:

- 2S = 6 + 12 + 24 + 48 + 96 + 192 + 384

Now line up S and 2S and subtract them.

- S = 3 + 6 + 12 + 24 + 48 + 96 + 192
- 2S = 6 + 12 + 24 + 48 + 96 + 192 + 384

Subtracting S from 2S makes the overlapping middle terms — 6, 12, 24, 48, 96, 192 — all cancel out, leaving only the two numbers at either end.

- 2S − S = 384 − 3
- S = 381

This matches exactly the value we got by adding everything up directly (381). Whether there are 7 terms or 70,000, this method lets you **get the answer by touching only the two ends, without laying a finger on any of the middle terms.**

#### Why this trick works

A geometric series is "a sequence that grows by the same multiple each time." That multiple is called the common ratio. In the example above, the common ratio was 2.

The reason this trick works is simple. When you multiply the original sequence by the common ratio, every term shifts exactly one slot over, **producing a sequence that's nearly identical to the original.** The two sequences overlap almost entirely; the only parts that don't overlap are the two terms at either end. So when you subtract, the middle cancels out entirely and only the ends remain.

Generalize this from numbers to symbols (first term a, common ratio ρ, number of terms n), and you get exactly the sum formula for geometric series covered in Part 0 below. What we just did by hand is simply that formula extended into symbols.

#### Why this matters

This one simple trick is used, later on, in the following ways:

- Calculating how much you'll have at maturity when you put the same amount into a savings plan every month is, in the end, a sum of a geometric series (because each installment earns interest for a different number of periods).
- How much you need to repay each month on an equal-installment loan is also derived by working backward from the sum of a geometric series.
- The question "if I collect rent forever, what is this piece of real estate worth?" is the limit of a geometric series sum as it continues infinitely (n→∞).
- Slice the compounding period into a day, an hour, a second... infinitely fine, and the geometric series converges to the constant e — which leads all the way to option pricing theory (Black–Scholes).

In other words, the "shift and subtract" trick we just verified by hand is the single tool running through this entire piece. Now let's move on to the generalized proof in Part 0.

---

# Geometric Series — Extended Edition
### From the 7 core formulas of discrete compounding to continuous compounding, inflation, and stochastic volatility
---
## Table of Contents
- **Part 0.** Starting point — the sum formula for a geometric series
- **Part 1.** Seven basic structures of discrete compounding (lump-sum deposits ~ real estate cap rates)
  - 1-⓪. Beginning-of-month vs. end-of-month payments — same savings plan, different result
- **Part 2.** Extension to continuous compounding (the constant e)
  - 2-1. Continuous versions and proofs of the 7 formulas
  - 2-1-ⓐ. Discrete vs. continuous compounding — a full comparison of pros and cons
  - 2-2. Inflation — from an approximation to an exact equality
  - 2-3. Stochastic volatility — geometric Brownian motion and the log-normal distribution
  - 2-3-ⓐ. Limits of GBM and Black–Scholes — historical and empirical scrutiny
- **Appendix.** Mathematica/Python code collection + full logical flow
---
# Part 0. Starting Point — The Sum Formula for a Geometric Series
## 0.1 Definition and Proof
Let the first term be a₁ = a and the common ratio be ρ (rho). The sum Sₙ of the first n terms of this geometric series is defined as follows.

**LaTeX (raw source):**
```latex
S_n = a + a\rho + a\rho^2 + \cdots + a\rho^{n-1} = \sum_{k=0}^{n-1} a\rho^{k}
```

**Unicode:**

```text
Sₙ = a + aρ + aρ² + ⋯ + aρⁿ⁻¹ = Σ(k=0 to n-1) aρᵏ
```

### Proof (standard derivation — the difference-cancellation method)

Form the expression Sₙ times the common ratio ρ, then subtract it from the original expression; the middle terms all cancel.

```latex
\begin{aligned}
S_n &= a + a\rho + a\rho^2 + \cdots + a\rho^{n-1} \quad &(1)\\
\rho S_n &= a\rho + a\rho^2 + \cdots + a\rho^{n-1} + a\rho^{n} \quad &(2)
\end{aligned}
```

(1) − (2):

```latex
S_n - \rho S_n = a - a\rho^n
```

```latex
S_n(1-\rho) = a(1-\rho^n)
```

```latex
\boxed{S_n = \frac{a(1-\rho^n)}{1-\rho} = \frac{a(\rho^n - 1)}{\rho - 1}} \qquad (\rho \neq 1)
```

**Unicode:**

```text
Sₙ(1-ρ) = a(1-ρⁿ)
Sₙ = a(1-ρⁿ)/(1-ρ) = a(ρⁿ-1)/(ρ-1)
```

### Extension to an infinite series (n → ∞)

If |ρ| < 1, then ρⁿ → 0, so:

```latex
S_\infty = \lim_{n\to\infty} \frac{a(1-\rho^n)}{1-\rho} = \frac{a}{1-\rho}
```

This equation is, later on, the mathematical basis for **perpetuities** and the **real estate income capitalization method**.

### Mathematica verification

```mathematica
(* Verifying the geometric series sum formula *)
Sum[a*rho^k, {k, 0, n - 1}] // Simplify
(* Output: a(1-rho^n)/(1-rho) *)
(* Infinite series (|rho|<1) *)
Sum[a*rho^k, {k, 0, Infinity}] // Assuming[Abs[rho] < 1, Simplify[#]] &
(* Output: a/(1-rho) *)
```

## 0.2 The Substitution in Finance: ρ = 1+r

In financial problems, the common ratio takes the form ρ = (1+r), where r is the interest rate (discount rate). This one substitution is the root of every formula that follows.

---

# Part 1. Seven Basic Structures of Discrete Compounding

## 1-⓪. Beginning-of-Month vs. End-of-Month Payments — Same Savings Plan, Different Result

### Why this distinction matters

This is the first distinction that comes up. **Whether you deposit at the beginning of the month or the end of the month** changes the final balance at maturity, even if you deposit the same amount over the same period. There is exactly one reason: **the difference in how long the interest has to accrue.**

### Beginning-of-Month Payments (Begin Mode, Type 1)

Deposit a at the **beginning** of each month. The first installment earns interest n times, and even the last installment earns it once.

```latex
S_{\text{begin}} = a(1+r)^n + a(1+r)^{n-1} + \cdots + a(1+r)^1
```

This is a geometric series with first term a(1+r), common ratio (1+r), and n terms:

```latex
S_{\text{begin}} = \frac{a(1+r)\{(1+r)^n - 1\}}{r}
```

**Unicode:** `S_begin = a(1+r){(1+r)ⁿ-1} / r`

### End-of-Month Payments (End Mode, Type 0)

Deposit a at the **end** of each month. The first installment earns interest n−1 times, and **the last installment earns no interest at all.**

```latex
S_{\text{end}} = a(1+r)^{n-1} + a(1+r)^{n-2} + \cdots + a(1+r)^0
```

This is a geometric series with first term a, common ratio (1+r), and n terms:

```latex
S_{\text{end}} = \frac{a\{(1+r)^n - 1\}}{r}
```

**Unicode:** `S_end = a{(1+r)ⁿ-1} / r`

### The Relationship Between the Two Formulas — A Surprisingly Simple Truth

```latex
S_{\text{begin}} = (1+r) \cdot S_{\text{end}}
```

**That is, beginning-of-month payments come out to exactly (1+r) times the end-of-month result.** This is because every single payment earns interest one extra time.

### A Worked Example: ₩200,000/month, 24 months, 0.4% monthly rate

- **End-of-month:** 200,000 × {(1.004)²⁴ − 1}/0.004 ≈ **₩5,027,250**
- **Beginning-of-month:** 5,027,250 × 1.004 ≈ **₩5,047,359**
- **Difference:** about **₩20,109**

Simply by depositing at the start of each month over 24 months, you come out **roughly ₩20,000** ahead. This is the mathematical basis for the practical maxim that "putting money in even one day earlier is always better."

### Mathematica

```mathematica
(* End-of-month *)
S_end[a_, r_, n_] := a*((1 + r)^n - 1)/r
S_end[200000, 0.004, 24]
(* Output: 5.02725*10^6 *)
(* Beginning-of-month *)
S_begin[a_, r_, n_] := a*(1 + r)*((1 + r)^n - 1)/r
S_begin[200000, 0.004, 24]
(* Output: 5.04736*10^6 *)
(* Verifying the relationship *)
S_begin[200000, 0.004, 24] == (1 + 0.004)*S_end[200000, 0.004, 24]
(* Output: True *)
```

### Why the Beginning/End Distinction Runs Through All 7 Formulas

- **Formula ② (future value of an installment plan)** is based on **end-of-month** payments.
- **Formula ③ (required payment via reverse calculation)** is based on **beginning-of-month** payments (asking how much you need to put in "at the start of each month" to reach a target amount).
- **Formula ⑤ (loan repayment)** is based on **end-of-month** repayment (banks typically collect loan payments at month-end).
- **Formula ⑥ (present value of an annuity)** is based on **end-of-month** receipts.

**"When the cash actually changes hands" determines the shape of the formula.** This is the first key to reading the 7 formulas in Part 1.

---

## 1-① Lump-Sum Compounding

### Situation

Deposit a lump sum of a once, and let it compound at rate r for n periods. What is the balance S at maturity?

### Formula

```latex
S = a(1+r)^n
```

**Unicode:** `S = a(1+r)ⁿ`

### Proof (mathematical induction)

**Step 1 (n=1):** After 1 period, principal + interest = a + ar = a(1+r). Holds.

**Step 2 (inductive hypothesis):** Assume that after k periods, Sₖ = a(1+r)ᵏ.

**Step 3 (inductive step):** In period k+1, the entire amount Sₖ earns interest at rate r one more time.

```latex
S_{k+1} = S_k(1+r) = a(1+r)^k \cdot (1+r) = a(1+r)^{k+1}
```

By mathematical induction, Sₙ = a(1+r)ⁿ holds for every natural number n. ∎

### Example

Deposit ₩10,000,000 at an annual rate of 4% for 5 years.

```latex
S = 10{,}000{,}000 \times (1.04)^5 = 10{,}000{,}000 \times 1.216653 \approx 12{,}166{,}529\text{ won}
```

### Mathematica

```mathematica
S1[a_, r_, n_] := a*(1 + r)^n
S1[10000000, 0.04, 5]
(* Output: 1.21665*10^7 *)
```

---

## 1-② Regular Savings (End-of-Month) — Future Value

### Situation

Deposit a at the end of each month for n months at monthly rate r. What is the balance S at maturity?

### Formula

```latex
S = \frac{a\{(1+r)^n - 1\}}{r}
```

**Unicode:** `S = a{(1+r)ⁿ - 1} / r`

### Proof

The amount a deposited in the k-th installment (k=1,…,n) earns interest (n−k) times before maturity (the last installment earns zero interest).

```latex
S = \sum_{k=1}^{n} a(1+r)^{n-k} = a\sum_{j=0}^{n-1}(1+r)^{j} \quad (j = n-k)
```

This is exactly the same form as substituting ρ = 1+r into the geometric series sum formula from Section 0.1.

```latex
S = a \cdot \frac{(1+r)^n - 1}{(1+r)-1} = \frac{a\{(1+r)^n-1\}}{r} \qquad \blacksquare
```

### Example

Deposit ₩200,000 at the end of each month for 24 months, at a monthly rate of 0.4% (roughly 4.8% annually).

```latex
S = \frac{200{,}000\{(1.004)^{24}-1\}}{0.004} \approx 5{,}027{,}250\text{ won}
```

### Mathematica

```mathematica
S2[a_, r_, n_] := a*((1 + r)^n - 1)/r
S2[200000, 0.004, 24]
(* Output: 5.02725*10^6 *)
```

---

## 1-③ Reverse Calculation (Beginning-of-Month) — Required Monthly Payment

### Situation

To reach a target amount S after n months, how much a must you deposit at the beginning of each month? Since these are beginning-of-month payments, every payment earns interest once more than in ②.

### Formula

```latex
S = a(1+r)\{(1+r)^n - 1\}/r \;\;\Longrightarrow\;\; a = \frac{Sr}{(1+r)\{(1+r)^n-1\}}
```

**Unicode:** `a = Sr / [(1+r){(1+r)ⁿ-1}]`

### Proof

For beginning-of-month payments, the k-th deposit earns interest (n−k+1) times:

```latex
S = \sum_{k=1}^{n} a(1+r)^{n-k+1} = a(1+r)\sum_{j=0}^{n-1}(1+r)^j = a(1+r)\cdot\frac{(1+r)^n-1}{r}
```

Solving for a:

```latex
a = \frac{Sr}{(1+r)\{(1+r)^n-1\}} \qquad \blacksquare
```

### Example

You want to save ₩100,000,000 in 10 years (120 months), at a monthly rate of 0.3% (roughly 3.6% annually).

```latex
a = \frac{100{,}000{,}000 \times 0.003}{(1.003)\{(1.003)^{120}-1\}} = \frac{300{,}000}{1.003 \times 0.43077} \approx 694{,}400\text{ won}
```

### Mathematica

```mathematica
S3[Stot_, r_, n_] := Stot*r/((1 + r)*((1 + r)^n - 1))
S3[100000000, 0.003, 120]
(* Output: about 694400 *)
```

---

## 1-④ Present Value (Discounting)

### Situation

To have a target amount S available in n periods, how much a should you deposit now? This is the inverse of ①.

### Formula

```latex
a = \frac{S}{(1+r)^n}
```

**Unicode:** `a = S / (1+r)ⁿ`

### Proof

Since S = a(1+r)ⁿ from ①, dividing both sides by (1+r)ⁿ gives this immediately.

```latex
a = S(1+r)^{-n} \qquad \blacksquare
```

### Example

You need ₩50,000,000 in 10 years, at an annual rate of 5%.

```latex
a = \frac{50{,}000{,}000}{(1.05)^{10}} = \frac{50{,}000{,}000}{1.628895} \approx 30{,}695{,}656\text{ won}
```

### Mathematica

```mathematica
S4[Stot_, r_, n_] := Stot/(1 + r)^n
S4[50000000, 0.05, 10]
(* Output: 3.06957*10^7 *)
```

---

## 1-⑤ Fully Amortizing Loan Repayment

### Situation

Borrow a principal of S and repay it in equal monthly installments of a at the end of each month for n months until fully repaid. This requires that "the present value of the amount borrowed = the present value of all the repayments."

### Formula

```latex
a = \frac{Sr(1+r)^n}{(1+r)^n - 1}
```

**Unicode:** `a = Sr(1+r)ⁿ / [(1+r)ⁿ - 1]`

### Proof

The loan principal S must equal the sum of the present values of the repayments (using the annuity present-value formula ⑥ first):

```latex
S = \sum_{k=1}^{n} \frac{a}{(1+r)^k} = a\cdot\frac{1-(1+r)^{-n}}{r}
```

(This is the same as a geometric series with common ratio 1/(1+r) and first term a/(1+r) — applying the formula from Section 0.1.)

Solving for a:

```latex
a = \frac{Sr}{1-(1+r)^{-n}}
```

Multiplying numerator and denominator by (1+r)ⁿ:

```latex
a = \frac{Sr(1+r)^n}{(1+r)^n - 1} \qquad \blacksquare
```

### Example

A loan of ₩300,000,000 at an annual rate of 4.8% (0.4% monthly), fully amortized over 240 months (20 years).

```latex
a = \frac{300{,}000{,}000 \times 0.004 \times (1.004)^{240}}{(1.004)^{240}-1}
```

Since (1.004)²⁴⁰ ≈ 2.60716:

```latex
a \approx \frac{300{,}000{,}000 \times 0.004 \times 2.60716}{1.60716} \approx \frac{3{,}128{,}592}{1.60716} \approx 1{,}946{,}500\text{ won/month}
```

### Mathematica

```mathematica
S5[Stot_, r_, n_] := Stot*r*(1 + r)^n/((1 + r)^n - 1)
S5[300000000, 0.004, 240]
(* Output: about 1.9465*10^6 *)
```

---

## 1-⑥ Present Value of an Annuity (Finite Period)

### Situation

An annuity product that pays a at the end of each month for n months. What is its present value P?

### Formula

```latex
P = \frac{a\{1-(1+r)^{-n}\}}{r}
```

**Unicode:** `P = a{1-(1+r)⁻ⁿ} / r`

### Proof

Discount each installment a back to present value and sum them (a geometric series with common ratio (1+r)⁻¹):

```latex
P = \sum_{k=1}^{n} a(1+r)^{-k} = a(1+r)^{-1}\cdot\frac{1-(1+r)^{-n}}{1-(1+r)^{-1}}
```

Since the denominator simplifies to 1−(1+r)⁻¹ = r/(1+r):

```latex
P = a(1+r)^{-1} \cdot \frac{1-(1+r)^{-n}}{\frac{r}{1+r}} = \frac{a\{1-(1+r)^{-n}\}}{r} \qquad \blacksquare
```

### Example

An annuity paying ₩1,000,000 per month for 20 years (240 months), at an annual discount rate of 4% (1/3% monthly).

```latex
P = \frac{1{,}000{,}000\{1-(1.00333)^{-240}\}}{0.00333} \approx \frac{1{,}000{,}000 \times 0.5497}{0.00333} \approx 165{,}080{,}000\text{ won}
```

### Mathematica

```mathematica
S6[a_, r_, n_] := a*(1 - (1 + r)^(-n))/r
S6[1000000, 0.04/12, 240]
(* Output: about 1.6508*10^8 *)
```

---

## 1-⑦ Perpetuity

### Situation

Take n → ∞ in ⑥. What present value P is needed to receive a forever, each period?

### Formula

```latex
P = \frac{a}{r}
```

**Unicode:** `P = a/r`

### Proof 1 (via a limit)

If r>0, then as n→∞, (1+r)⁻ⁿ→0, so from formula ⑥:

```latex
P = \lim_{n\to\infty}\frac{a\{1-(1+r)^{-n}\}}{r} = \frac{a(1-0)}{r} = \frac{a}{r} \qquad \blacksquare
```

### Proof 2 (directly via an infinite geometric series)

```latex
P = \frac{a}{1+r}+\frac{a}{(1+r)^2}+\cdots = \sum_{k=1}^{\infty}\frac{a}{(1+r)^k}
```

With first term a/(1+r) and common ratio 1/(1+r) (which converges since it's <1):

```latex
P = \frac{\frac{a}{1+r}}{1-\frac{1}{1+r}} = \frac{\frac{a}{1+r}}{\frac{r}{1+r}} = \frac{a}{r} \qquad \blacksquare
```

### Proof 3 (an intuitive proof — preserving principal)

If a principal P earns interest at rate r, the interest per period is Pr. If you withdraw only this interest and preserve the principal, it can continue forever:

```latex
a = Pr \;\Longrightarrow\; P = \frac{a}{r} \qquad \blacksquare
```

**The fact that all three proofs converge on the same result shows that this formula isn't a "coincidence" — it's structurally necessary.**

### Application: Real Estate Income Capitalization

For a real estate value P, monthly rent (net operating income) a, and market required return (cap rate) r, exactly the same formula applies:

```latex
P_{\text{real estate}} = \frac{a}{r}
```

**Proof (equivalence):** A deposit and a piece of real estate are both, mathematically, the same object — "a recurring cash flow of a, a, a, … discounted at rate r into present value."

```latex
P_{\text{deposit}} = \sum_{k=1}^{\infty}\frac{a}{(1+r)^k} = \frac{a}{r} = \sum_{k=1}^{\infty}\frac{a}{(1+r)^k} = P_{\text{real estate}}
```

Additionally, the very definitions are already identical: r_interest ≡ (return)/(principal), r_cap-rate ≡ (rent)/(price). Since the two definitions are formally identical, the two results being identical is necessary. ∎

### Example

**Finance:** To receive ₩2,000,000 per month forever, assuming an annual rate of 3.5% (0.2917% monthly):

```latex
P = \frac{2{,}000{,}000}{0.0029167} \approx 685{,}714{,}000\text{ won}
```

**Real estate:** Monthly net rental income of ₩3,000,000, market cap rate of 3.6% annually:

```latex
P = \frac{3{,}000{,}000\times 12}{0.036} = \frac{36{,}000{,}000}{0.036} = 1{,}000{,}000{,}000\text{ won (1 billion won)}
```

### Mathematica

```mathematica
S7[a_, r_] := a/r
S7[2000000, 0.035/12]
(* Output: about 6.85714*10^8 *)
(* Real estate reverse calculation: finding the cap rate *)
CapRate[a_, P_] := a/P
CapRate[3000000*12, 1000000000]
(* Output: 0.036 *)
```

### Growing Perpetuity

When the periodic payment keeps growing at rate g (e.g., rent rising with inflation):

```latex
P = \frac{a}{r-g} \qquad (r>g)
```

**Proof:** The payment in period k is a(1+g)^(k−1). The sum of present values:

```latex
P = \sum_{k=1}^{\infty} \frac{a(1+g)^{k-1}}{(1+r)^k} = \frac{a}{1+r}\sum_{k=0}^{\infty}\left(\frac{1+g}{1+r}\right)^{k}
```

Since the common ratio (1+g)/(1+r) < 1 (i.e., g<r), it converges:

```latex
P = \frac{a}{1+r}\cdot\frac{1}{1-\frac{1+g}{1+r}} = \frac{a}{1+r}\cdot\frac{1+r}{r-g} = \frac{a}{r-g} \qquad \blacksquare
```

> **Caution:** If g ≥ r, the series diverges and this model becomes meaningless. In practice, when valuing hyper-growth startups, you need to switch to a finite-period model or a multi-stage growth model.

---

# Part 2. Extension to Continuous Compounding (the Constant e)

## 2-1. Rules for Converting Discrete → Continuous, and Re-deriving the 7 Formulas

### The Definition of the Natural Constant (Financial Perspective)

```latex
e^r \equiv \lim_{m\to\infty}\left(1+\frac{r}{m}\right)^m
```

**Unicode:** `e^r ≡ lim(m→∞) (1 + r/m)^m`

**Historical context:** This limit was first recognized in 1683 by Jacob Bernoulli while studying compound interest. His question was: "Starting with a principal of 1 at 100% annual interest, if you split the compounding into n installments, what value does the result converge to as n → ∞?" Bernoulli proved this limit lies between 2 and 3; later, Euler denoted this value with e and revealed its significance.

### Sketch of the Proof (Expansion via the Binomial Theorem)

```latex
\left(1+\frac{r}{m}\right)^m = \sum_{k=0}^{m}\binom{m}{k}\left(\frac{r}{m}\right)^k = \sum_{k=0}^{m}\frac{m!}{k!(m-k)!}\cdot\frac{r^k}{m^k}
```

For fixed k, as m→∞:

```latex
\frac{m!}{(m-k)!\,m^k} = \frac{m(m-1)\cdots(m-k+1)}{m^k} \longrightarrow 1
```

Therefore:

```latex
\lim_{m\to\infty}\left(1+\frac{r}{m}\right)^m = \sum_{k=0}^{\infty}\frac{r^k}{k!} = 1+r+\frac{r^2}{2!}+\frac{r^3}{3!}+\cdots =: e^r \qquad \blacksquare
```

(This also shows agreement with the Taylor series definition of the exponential function.)

### From Σ to ∫ — the Core Intuition Behind the Conversion

- **The discrete world:** Σ (sum), common ratio ρ = 1+r, integer index k, "how many times has interest been applied"
- **The continuous world:** ∫ (integral), exponential function e^(rt), real-valued time s, "how long has it been"

This correspondence governs all 7 formulas. **When a sum (sigma) becomes an integral, a geometric series becomes an exponential function.**

### Correspondence Table (All 7 Formulas)

- **①** Discrete: `S = a(1+r)^n` / Continuous: `S = a e^{rt}`
- **②** Discrete: `S = a{(1+r)^n - 1}/r` / Continuous: `S = (a/r)(e^{rt} - 1)`
- **③** Discrete: `a = Sr / [(1+r){(1+r)^n - 1}]` / Continuous: `a = Sr/(e^{rt} - 1)`
- **④** Discrete: `a = S/(1+r)^n` / Continuous: `a = S e^{-rt}`
- **⑤** Discrete: `a = Sr(1+r)^n / {(1+r)^n - 1}` / Continuous: `a = Sr e^{rt}/(e^{rt} - 1)`
- **⑥** Discrete: `P = a{1-(1+r)^{-n}}/r` / Continuous: `P = (a/r)(1 - e^{-rt})`
- **⑦** Discrete: `P = a/r` / Continuous: `P = a/r` (identical)

### Proof of Formula ① — Using a Limit Instead of an Integral

Split 1 year into m intervals, apply a rate of r/m in each interval; after t years, compounding has occurred mt times total:

```latex
S = a\left(1+\frac{r}{m}\right)^{mt} = a\left[\left(1+\frac{r}{m}\right)^{m}\right]^{t} \xrightarrow{m\to\infty} a\,(e^{r})^{t} = ae^{rt} \qquad \blacksquare
```

### Proof of Formula ② — From a Riemann Sum to an Integral

Suppose an amount a·ds is deposited during each infinitesimal instant ds. The amount deposited at time s grows through continuous compounding over the remaining period (t−s):

```latex
S = \int_0^t a\,e^{r(t-s)}\,ds = ae^{rt}\int_0^t e^{-rs}\,ds = ae^{rt}\left[-\frac{1}{r}e^{-rs}\right]_0^t = ae^{rt}\cdot\frac{1-e^{-rt}}{r} = \frac{a}{r}(e^{rt}-1) \qquad \blacksquare
```

### Proofs of Formulas ⑤ and ⑥ — Integrating the Present Value of Repayments

If continuous repayments of a·ds keep occurring, the sum of present values is:

```latex
P = \int_0^t a\,e^{-rs}\,ds = a\left[-\frac{1}{r}e^{-rs}\right]_0^t = \frac{a}{r}(1-e^{-rt})
```

This is the continuous version of ⑥. Setting the loan principal S=P and solving for a gives ⑤:

```latex
a = \frac{Sr}{1-e^{-rt}} = \frac{Sre^{rt}}{e^{rt}-1} \qquad \blacksquare
```

### Formula ⑦ — Discrete and Continuous Agree Exactly in the Infinite Limit

```latex
\lim_{t\to\infty}\frac{a}{r}(1-e^{-rt}) = \frac{a}{r}(1-0) = \frac{a}{r}
```

This is exactly the same as the discrete limit a/r — over short periods, discrete and continuous compounding differ subtly, but **as time goes to infinity, that difference disappears.**

### Comparison of Effective Interest Rates (Nominal Annual 6%)

- **Annual compounding:** (1+0.06)¹ − 1 = 6.000%
- **Semiannual compounding:** (1+0.03)² − 1 = 6.090%
- **Quarterly compounding:** (1+0.015)⁴ − 1 = 6.136%
- **Monthly compounding:** (1+0.005)¹² − 1 = 6.168%
- **Daily compounding:** (1+0.06/365)³⁶⁵ − 1 = 6.183%
- **Continuous compounding:** e^0.06 − 1 = 6.184%

**Observation:** The gap between daily and continuous compounding is on the order of 0.001 percentage points. This is why practitioners say "daily compounding ≈ continuous compounding." But theoretically, continuous compounding is always greater — the sequence (1+r/m)^(tm) increases monotonically with m and converges to e^(rt).

### Mathematica

```mathematica
(* Verifying the limit definition of the natural constant *)
Limit[(1 + r/m)^m, m -> Infinity]
(* Output: E^r *)
(* Comparing effective rates *)
Table[{n, (1 + 0.06/n)^n - 1}, {n, {1, 2, 4, 12, 365}}]
Exp[0.06] - 1
(* Continuous compounding: 0.0618365 *)
(* Continuous versions of formulas ①~⑦ *)
C1[a_, r_, t_] := a*E^(r*t)
C2[a_, r_, t_] := (a/r)*(E^(r*t) - 1)
C3[Stot_, r_, t_] := Stot*r/(E^(r*t) - 1)
C4[Stot_, r_, t_] := Stot*E^(-r*t)
C5[Stot_, r_, t_] := Stot*r*E^(r*t)/(E^(r*t) - 1)
C6[a_, r_, t_] := (a/r)*(1 - E^(-r*t))
C7[a_, r_] := a/r
(* Verifying the limit: as t->Infinity, formula ⑥ -> ⑦ *)
Limit[C6[a, r, t], t -> Infinity]
(* Output: a/r, matches formula ⑦ *)
```

---

## 2-1-ⓐ. Discrete vs. Continuous Compounding — A Full Comparison of Pros and Cons

### Core Summary

- **Best suited for:** Discrete compounding = actual financial products / Continuous compounding = theoretical analysis, financial engineering
- **Core tool:** Discrete compounding = sum of a geometric series / Continuous compounding = exponential functions and calculus
- **Character:** Discrete compounding = stepwise (discontinuous) growth / Continuous compounding = smooth (continuous) growth

### Pros and Cons of Discrete Compounding (Geometric Series)

**✅ Pros**

1. **It matches real-world financial products exactly.** Bank savings plans, loan repayments, and deposit interest are all calculated on fixed cycles (monthly, quarterly, annually). It models "what actually happens" directly.
2. **The calculations are intuitive.** You just count "which interest payment is this," so even people without a math background can follow it.
3. **A single geometric series formula covers many situations.** Monthly, annual, or quarterly payments are all just variations of the same geometric series structure.
4. **It maps directly onto real-world documents.** Contracts, disclosed rates, and repayment schedules are all stated on a discrete basis.

**❌ Cons**

1. **The result varies subtly depending on the compounding period.** Even at a nominal annual rate of 6%, monthly compounding and annual compounding differ in effective rate by 0.168 percentage points. This makes comparing products across compounding frequencies cumbersome.
2. **The exponent n is restricted to integers.** Getting a value at an arbitrary point in time (e.g., after 3.5 months) requires separate interpolation.
3. **It isn't smoothly differentiable.** Because the function jumps in steps, it's awkward to work with when computing an "instantaneous growth rate" or solving optimization problems.

### Pros and Cons of Continuous Compounding (e^(rt))

**✅ Pros**

1. **It's a smooth function of time t.** Differentiation and integration are unrestricted, making it powerful for computing instantaneous growth rates and optimal timing. e^(rt) retains its own form when differentiated, becoming r·e^(rt) — this "self-similarity" property greatly simplifies the calculus.
2. **It eliminates the variable of "compounding period" altogether.** Multiple products or models can be compared within a single unified framework. Indeed, financial engineering standardly uses the continuous-compounding rate r_c = ln(1+r).
3. **It's mathematically identical to exponential growth/decay in physics.** It shares the same form as population growth, radioactive decay, chemical reaction kinetics, and so on, giving it a wide range of applications.
4. **It's the standard in financial engineering (option pricing, derivatives).** The Black–Scholes model is derived on the assumption of continuous compounding. The discount term e^(−rT) is exactly the continuous version of formula ④ from Part 1.

**❌ Cons**

1. **No financial product actually accrues interest at every single instant.** It's a purely theoretical/approximate model. (That said, daily compounding comes so close to continuous compounding that it remains valid as a "practical approximation.")
2. **e^(rt) itself is a transcendental function, making it hard to compute by hand or in your head.** A calculator or software is essential.
3. **Practical interest rates and continuous-compounding rates differ in value.** For example, a nominal annual rate of 12% corresponds to about 11.33% under continuous compounding. Confusion can arise during this conversion.
4. **It's tied to the controversy over the "unrealism" of theoretical models like Black–Scholes.** Since the Black–Scholes model — the 1997 Nobel Prize in Economics-winning achievement — is built on continuous compounding, it has drawn criticism as "an assumption disconnected from actual finance." (This is a separate debate about the model's limitations, distinct from the mathematical soundness of the model itself.)

### Practice vs. Theory — What to Use Where

- **Bank deposit/savings calculations:** Discrete compounding — actual contract terms
- **Loan repayment schedules:** Discrete compounding — banking systems
- **Comparing returns across products:** Effective-rate conversion — removes the difference in compounding cycles
- **Option pricing:** Continuous compounding — the Black–Scholes standard
- **Risk modeling (VaR, etc.):** Continuous compounding — easier calculus
- **Analyzing long-term growth trends:** Continuous compounding — a smooth approximation

**One-line conclusion:** In practice, use discrete compounding for exact calculations, and use continuous compounding as an approximation for theoretical development or risk modeling. The bridge connecting these two worlds is the **effective rate**.

### Mathematica — A Numerical Comparison of the Two Methods

```mathematica
(* Comparing discrete vs. continuous for a nominal annual rate of 5% over 3 years *)
r = 0.05; t = 3;
(* Discrete compounding: various cycles *)
discrete[m_] := (1 + r/m)^(m*t)
Table[{m, discrete[m]}, {m, {1, 2, 4, 12, 365}}]
(* Continuous compounding *)
continuous = Exp[r*t]
(* Result: as m increases, it converges to continuous compounding *)
(* {1, 1.15763}, {2, 1.15969}, {4, 1.16075}, {12, 1.16147}, {365, 1.16182} *)
(* Continuous: 1.16183 *)
```

---

## 2-2. Inflation — From an Approximation to an Exact Equality

### The Real Interest Rate Under Discrete Compounding (the Fisher Equation)

With nominal interest rate r and inflation rate i, the real interest rate r_real is defined as:

```latex
1+r_{real} \equiv \frac{1+r}{1+i}
```

(Definition: real value growth is nominal value growth divided out by the effect of inflation.)

```latex
r_{real} = \frac{1+r}{1+i}-1 = \frac{(1+r)-(1+i)}{1+i} = \frac{r-i}{1+i}
```

Approximation when i is small:

```latex
r_{real} \approx r-i
```

**The exact error term:**

```latex
r_{real} - (r-i) = \frac{r-i}{1+i} - (r-i) = (r-i)\left(\frac{1}{1+i}-1\right) = -\frac{i(r-i)}{1+i}
```

That is, the error is the product of i and (r−i). If you only assume i is small, the error remains of order O(i); it only shrinks to order O(ε²) when r and i are both "small quantities of the same order."

### When Does "Subtraction" Work Well — Concrete Criteria

Looking at the error term `-i(r-i)/(1+i)` above, the conditions under which the approximation `r_real ≈ r - i` works well become clear. The size of the error is determined by the **product of `i` and `(r-i)`**. So the approximation improves when the following two conditions hold simultaneously:

1. **The inflation rate `i` is small** — this shrinks the multiplying factor itself.
2. **`r` and `i` are close to each other** — this shrinks `(r-i)`, further reducing the product.

**A practical rule of thumb:** In a low-rate, low-inflation environment (both `r` and `i` are single digits, with `r ≈ i`), the error falls below 0.1 percentage points, making the approximation essentially exact. But in a high-rate, high-inflation environment (e.g., `r = 25%`, `i = 20%`), the error becomes non-negligible. The list below gives a feel for this.

- **r = 5%, i = 3.5%:** Approximation r−i = 1.50%, exact r_real = 1.449%, error = 0.051 pp
- **r = 5%, i = 5%:** Approximation r−i = 0%, exact r_real = 0%, error = 0 pp
- **r = 15%, i = 12%:** Approximation r−i = 3%, exact r_real = 2.679%, error = 0.321 pp
- **r = 25%, i = 20%:** Approximation r−i = 5%, exact r_real = 4.167%, error = 0.833 pp

**Intuition:** When `r ≈ i`, the numerator `r-i` becomes small, and the error shrinks along with it. The reason the intuition of "real rate = nominal rate minus inflation" holds up in most practical situations is precisely that `r` and `i` tend to stay in the same order of magnitude.

**An extreme warning:** During the 1980s Latin American debt crisis, Argentina saw nominal rates around 1,200% alongside inflation around 3,000%. Here, `r - i = -1,800%` is entirely meaningless; only the exact formula, `(1+r)/(1+i) - 1 = 13/31 - 1 ≈ -58%`, reflects the actual change in purchasing power. **Unless `r ≈ i`, you must use the exact formula.**

### The Real Interest Rate Under Continuous Compounding (an Exact Equality)

Nominal value growth is e^(rt), and price growth is e^(it). Real value is then:

```latex
\text{real value} = \frac{ae^{rt}}{e^{it}} = a\,e^{(r-i)t}
```

Since this simply applies the exponent rule e^(rt)/e^(it) = e^((r−i)t):

```latex
\boxed{r_{real} = r - i} \qquad (\text{an exact equality, not an approximation})
```

### Proof: Why the Error Is Zero Under Continuous Compounding

Let's analyze the discrete error term via logarithms. Since ln(1+x) = x − x²/2 + x³/3 − ⋯ (a Taylor expansion):

```latex
\ln(1+r_{real}) = \ln(1+r)-\ln(1+i)
```

```latex
r_{real}-\frac{r_{real}^2}{2}+\cdots = \left(r-\frac{r^2}{2}+\cdots\right)-\left(i-\frac{i^2}{2}+\cdots\right)
```

Looking only at the first-order term, r_real ≈ r−i, but second- and higher-order terms remain, producing an error. **Continuous compounding is defined, from the outset, in a coordinate system already based on ln (log returns), so these higher-order terms never arise in the first place.** In other words, the continuous-compounding rate itself corresponds to the concept ln(1+r), which is exactly why the subtraction holds exactly. ∎

### Numerical Comparison (Nominal 5%, Inflation 3.5%)

- **Discrete (exact Fisher formula):** (0.05−0.035)/1.035 = 1.4493%
- **Discrete (approximation):** 0.05−0.035 = 1.5000%
- **Continuous compounding (exact):** 0.05−0.035 = **1.5000% (zero error)**

### Application to the 7 Formulas (Example: Formula ②)

```latex
S_{real} = \frac{a}{r-i}\left(e^{(r-i)t}-1\right)
```

Just substitute (r−i) in place of r — no approximation or correction term needed.

### Mathematica

```mathematica
(* Exact vs. approximate discrete real interest rate *)
rReal[r_, i_] := (r - i)/(1 + i)
rReal[0.05, 0.035]
(* Output: 0.0144928 *)
r - i /. {r -> 0.05, i -> 0.035}
(* Approximation output: 0.015 *)
(* Verifying the exact error term *)
Simplify[(r - i)/(1 + i) - (r - i) + i*(r - i)/(1 + i)]
(* Output: 0 *)
Series[Log[1 + r] - Log[1 + i], {r, 0, 2}, {i, 0, 2}]
(* First-order term: r - i, higher-order terms remain -> the source of the discrete-compounding error *)
(* Extreme high-inflation example: Argentina 1989 *)
rReal[12.0, 30.0]
(* Output: -0.5806 → about -58% *)
12.0 - 30.0
(* Output: -18 → entirely meaningless *)
```

---

## 2-3. Stochastic Volatility — Geometric Brownian Motion and the Log-Normal Distribution

### Motivation

If you plug a random variable rₖ into the discrete compounding expression a(1+r₁)(1+r₂)⋯(1+rₙ), you have to deal with the distribution of a **product** of multiple random variables, which is very complex. With continuous compounding, a·e^(rt), you only need to add a random term into the exponent, making the analysis much easier.

### The Geometric Brownian Motion (GBM) Model

```latex
S_t = a\,\exp\!\left[\left(r-\frac{\sigma^2}{2}\right)t + \sigma W_t\right]
```

**Unicode:**

```text
Sₜ = a · exp[(r - σ²/2)t + σWₜ]
```

Here Wₜ is standard Brownian motion (a Wiener process), and σ is the volatility.

**Definition of a Wiener process (reference):** Wₜ is a stochastic process satisfying the following three conditions:

1. W₀ = 0
2. Independent increments: for 0 ≤ t₁ < t₂ < ⋯, the increments W_(t₂)−W_(t₁), W_(t₃)−W_(t₂), … are independent
3. Normal increments: W_(s+t)−W_s ∼ N(0, t) (mean 0, variance t)

**An important property:** the sample paths of a Wiener process are nowhere differentiable (total variation is infinite).

**"If it's not differentiable, how can we even write `dS`?"** — this is where a reader might get stuck. The answer is that **`dW` is not interpreted as a pathwise derivative**. In the Itô integral, `dW` is defined as a **formal differential** satisfying **quadratic variation `(dW)² = dt`**. That is, `∫σS dW` is not "the integral of the derivative of `W`" — it's defined as a **separate integral operation (the Itô integral)** over a Wiener process with independent, normal increments. Differentiability is never required. This counterintuitive equation, `(dW)² = dt`, is exactly what produces the `−σ²/2` term in Itô's lemma.

**Why `(dW)² = dt` — an intuitive explanation**

Unlike ordinary calculus, where `(dx)² ≈ 0` can be ignored, in a Wiener process `dW` fluctuates on the scale of `~√dt`. So `(dW)² ~ dt` — this is not a "negligible second-order term" but a **deterministic term of the same order as the first-order term**. The core insight of Itô's lemma is precisely that "we do not discard the second-order term."

**A numerical example:** with `dt = 1/252` (daily) and `σ = 0.2`:

- Diffusion contribution: `σ · dW ~ 0.2 × √(1/252) ≈ 0.0126` (1.26%)
- Itô correction term: `−½σ² · dt ≈ −0.5 × 0.04 × 0.00397 ≈ −7.9 × 10⁻⁵`
- **Ratio:** the correction is about 0.6% of the diffusion term. Small on a daily basis, but **it becomes non-negligible when accumulated over decades.**

**Comparing the Magnitudes of Each Term**

- **Drift term:** `r · dt`, magnitude O(dt), role = deterministic growth
- **Diffusion term:** `σ · dW`, magnitude O(√dt), role = random fluctuation
- **Itô correction:** `−½σ² · dt`, magnitude O(dt), role = the deterministic absorption of randomness

### Relationship to the Stochastic Differential Equation (SDE) Form

GBM is defined as the solution to the following stochastic differential equation:

```latex
dS_t = rS_t\,dt + \sigma S_t\,dW_t
```

This means "the instantaneous return follows a normal distribution with mean r·dt and standard deviation σ√dt."

- **rSₜ dt (the drift term):** deterministic growth — corresponds to the continuous-compounding term a·e^(rt)
- **σSₜ dWₜ (the diffusion term):** random fluctuation — an element absent from discrete compounding

### Sketch of the Derivation Using Itô's Lemma

Applying Itô's lemma to f(Sₜ)=ln Sₜ:

```latex
d(\ln S_t) = \frac{1}{S_t}dS_t - \frac{1}{2S_t^2}(dS_t)^2
```

Substituting dSₜ = rSₜ dt + σSₜ dWₜ and using (dWₜ)² = dt (the Itô identity):

```latex
d(\ln S_t) = \left(r-\frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
```

Integrating both sides from 0 to t:

```latex
\ln S_t - \ln a = \left(r-\frac{\sigma^2}{2}\right)t + \sigma W_t
```

```latex
\boxed{S_t = a\exp\!\left[\left(r-\frac{\sigma^2}{2}\right)t+\sigma W_t\right]} \qquad \blacksquare
```

**Key insight:** the −σ²/2 term (the volatility correction, or Itô correction) is absent from the deterministic continuous-compounding formula a·e^(rt); it arises purely from randomness (the second-order term in Itô calculus).

### Distribution of Log Returns

```latex
\ln\left(\frac{S_t}{a}\right) = \left(r-\frac{\sigma^2}{2}\right)t+\sigma W_t \;\sim\; N\!\left(\left(r-\frac{\sigma^2}{2}\right)t,\;\sigma^2 t\right)
```

That is, **the price Sₜ itself follows a log-normal distribution** (which is consistent with the fact that prices are always positive).

### Why Discrete Compounding Isn't as Clean

Taking the log of the discrete product ∏(1+rₖ):

```latex
\ln\prod_{k=1}^{n}(1+r_k) = \sum_{k=1}^n \ln(1+r_k) \approx \sum_{k=1}^n r_k
```

By the central limit theorem, the **sum** of independent random variables converges to a normal distribution, but the discrete form generates an approximation error every time, since ln(1+rₖ) ≠ rₖ. Continuous compounding has this "take-the-log-then-add" step built directly into its definition, so no such error arises.

### The Connection to the Black–Scholes Formula

On top of the geometric Brownian motion model, the price C of a European call option is derived as follows (the Black–Scholes formula, 1973):

```latex
C = a\,N(d_1) - Ke^{-rT}N(d_2)
```

```latex
d_1 = \frac{\ln(a/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1-\sigma\sqrt{T}
```

where:

- N(·): the cumulative distribution function of the standard normal distribution
- K: the strike price
- T: time to expiration
- a: the current stock price (the underlying asset price)

**The discount term e^(−rT) in this formula is exactly formula ④ (present value) from Part 1**, and the log-normal distribution derived from GBM becomes the probabilistic foundation for option pricing.

**Connection to the Black–Scholes PDE:** the option price C(S,t) satisfies the following partial differential equation:

```latex
\frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS\frac{\partial C}{\partial S} - rC = 0
```

Solving this PDE yields the Black–Scholes formula above. **The coefficients r and σ in the PDE come directly from the GBM model, which is itself built on continuous compounding, e^(rt).**

### Mathematica

```mathematica
(* GBM simulation (one path) *)
SeedRandom[1];
a0 = 100; r = 0.05; sigma = 0.2; T = 1; nSteps = 252;
dt = T/nSteps;
W = Accumulate[Prepend[RandomVariate[NormalDistribution[0, Sqrt[dt]], nSteps], 0]];
path = a0*Exp[(r - sigma^2/2)*dt*Range[0, nSteps] + sigma*W];
ListLinePlot[path, PlotLabel -> "GBM Price Path Simulation",
  AxesLabel -> {"Step", "Price"}]
(* Verifying the log-normal distribution: the distribution of St at maturity *)
StDist = TransformedDistribution[
   a0*Exp[(r - sigma^2/2)*T + sigma*Sqrt[T]*z],
   z \[Distributed] NormalDistribution[0, 1]];
PDF[StDist, s]
(* Confirming equivalence with LogNormalDistribution *)
Simplify[PDF[StDist, s] == 
  PDF[LogNormalDistribution[Log[a0] + (r - sigma^2/2)*T, sigma*Sqrt[T]], s]]
(* Black-Scholes call option price (implemented directly, without a built-in function) *)
BSCall[a0_, K_, r_, sigma_, T_] := Module[{d1, d2},
   d1 = (Log[a0/K] + (r + sigma^2/2)*T)/(sigma*Sqrt[T]);
   d2 = d1 - sigma*Sqrt[T];
   a0*CDF[NormalDistribution[0, 1], d1] - 
    K*Exp[-r*T]*CDF[NormalDistribution[0, 1], d2]
   ];
BSCall[100, 100, 0.05, 0.2, 1]
(* Output: about 10.4506 *)
```

---

## 2-3-ⓐ. Limits of GBM and Black–Scholes — Historical and Empirical Scrutiny (Verified and Corrected Edition)

> This section is a supplementary piece that organizes, with evidence-based literature, the limitations and controversies of the GBM (geometric Brownian motion) and Black–Scholes models introduced only in outline in Part 2-3. Every claim below was checked against original sources via web search, and errors found in an earlier draft (missing authors, misstated journal names, omitted study subjects) have been corrected in this edition.

---

### (1) The Discovery of the Natural Constant e — Sharpening the Historical Facts

#### The Problem with the Common Narrative

The claim that "Bernoulli discovered e in 1683" is broadly correct but imprecise. It leaves out the following:

- Bernoulli only **proved the limit exists and lies between 2 and 3** — he did not compute its value or assign it a symbol.
- Bernoulli did not recognize that this limit was related to logarithms.
- The first person to use the symbol **'e'** was Euler, estimated to be in the **late 1720s**, and it was officially documented in a **1731 letter to Goldbach**.
- Even before that, Leibniz had used the symbol **'b'** in 1690.

#### Timeline

- **1683:** Jacob Bernoulli, studying the problem of continuous compounding, proves that the limit `lim(n→∞) (1+1/n)ⁿ` converges and lies between 2 and 3. No symbol is introduced and no connection to logarithms is made.
- **1690:** In a letter to Huygens, Leibniz denotes this constant with the symbol 'b'.
- **Late 1720s:** Euler is estimated to have begun using the symbol 'e' in unpublished manuscripts.
- **1731:** In a letter to Goldbach, Euler defines "e as the number whose hyperbolic logarithm equals 1," marking the first officially documented use of the symbol 'e.' The consensus in the literature is that Euler chose 'e' because a, b, c, and d were already in use for other purposes — not because it stands for his own name (Euler).
- **1748:** In his *Introductio in analysin infinitorum*, Euler systematically formalizes e, deriving the series `e = Σ 1/k!` and redefining the exponential function as `e^x = lim(n→∞)(1+x/n)^n`.

#### An Early Precursor from Ancient Mesopotamia

A Mesopotamian clay tablet from roughly 2000 BCE (now held at the Louvre) records a compound-interest problem: **"At 20% annual interest, how many years does it take for the principal to double?"** Since exponents couldn't be solved via logarithms at the time, the value of (6/5)ⁿ was tabulated at n=3 and n=4, and the answer was found by **linear interpolation** between them. The result is known to be **3 years, 9 and 4/9 months (=3.7870 years)**, while the exact value (log 2 / log 1.2) is about **3.8018 years** — an error of roughly 0.4%.

It would be a stretch to call this "the discovery of e"; it's more accurate to describe it as **"one of the oldest known records of approximating an exponential-growth problem via linear interpolation."**

#### Mathematica Verification

```mathematica
(* Mesopotamian clay tablet problem: time to double at 20% annual compounding *)
Solve[(1 + 0.20)^t == 2, t]
(* Output: t = Log[2]/Log[1.2] ≈ 3.8018 *)
3.7870/3.8018
(* Output: 0.9961 → about a 0.4% error relative to the tablet's approximation *)
(* Verifying the series expansion of the natural constant e *)
N[Sum[1/k!, {k, 0, 20}], 20]
(* Output: 2.7182818284590452354 *)
```

---

### (2) The Empirical Limits of the Black–Scholes Model — Specific Literature-Based Evidence

#### The Problem with the Common Narrative

Saying "Black–Scholes is criticized for being unrealistic" is far too broad a claim. In reality, the academic literature identifies **four distinct problems**, raised from different angles, along with **one counterargument**.

#### Problem 1 — The Log-Normal Assumption and Fat Tails

Black–Scholes assumes that the underlying asset's returns follow a log-normal distribution, but numerous empirical studies have pointed out that real return distributions show **"fat tails"** — extreme values occur far more often than a normal distribution would predict.

- **Theoretical prediction:** under a standard normal distribution, the probability of a 5σ event is `P(|Z| > 5) ≈ 5.73 × 10⁻⁷`. On a "once-per-trading-day" basis, that's **roughly once every 4,776 years**.
- **Empirical observation (S&P 500, 1950–2012):** actual 5σ-or-greater daily returns have been observed about **0.18%** of the time (on the downside) — **hundreds to thousands of times** more frequent than the normal-distribution prediction. The March 2020 COVID crash was rated at roughly **5σ**, an event the normal distribution would predict to occur "once every 13,932 years," yet it actually happened.
- **Implication:** Mandelbrot and Hudson argue that risk has been badly mismeasured and that the true odds of financial ruin have been grossly underestimated, contending that actual market returns behave more like a "wild," **power-law** distribution.

**Source note:** the theoretical normal-distribution probability of a 5σ event, roughly `5.7×10⁻⁷`, is computed directly from the standard normal two-tailed probability `P(|Z|>5) ≈ 5.73×10⁻⁷`. The empirical observation frequency on the order of `10⁻³` (once every year or few years) is a general finding repeatedly confirmed across Mandelbrot's stable-distribution research, standard textbooks such as Hull's, and numerous empirical papers. For citing specific figures, the following sources are appropriate.

- **Mandelbrot, B. B. & Hudson, R. L. (2004).** *The (Mis)Behavior of Markets: A Fractal View of Risk, Ruin, and Reward.* Basic Books. — A landmark work emphasizing that 5σ-scale events occur dozens to hundreds of times more often than the normal distribution predicts.
- **Hull, J. C.** *Options, Futures, and Other Derivatives.* — A standard textbook-level discussion of how fat tails clash with the assumptions of Black–Scholes.
- **Voss, J. (2012).** "Fact File: S&P 500 Sigma Events." CFA Institute. — Frequency data on S&P 500 sigma events from 1950–2012.

**Caution:** the 5σ figures above vary by asset, period, and sample, so the "roughly 1,700 times" ratio should be taken as a **representative rough estimate**; to claim a precise multiple, a specific sample and period must be stated.

**A List of Empirical Data Points for Comparison**

- **S&P 500, daily (1950–2012):** 5σ frequency about 0.18% (downside), normal-distribution prediction 5.7×10⁻⁷
- **DAX, daily (1965–2019):** 5σ frequency 96 occurrences (about 0.7% of all trading days), normal-distribution prediction effectively zero
- **March 2020 COVID crash:** about 5σ, which under the normal distribution would occur "roughly once every 14,000 years"

**Additional citation:** Mandelbrot first identified a power-law pattern in his 1962 analysis of cotton prices, and later confirmed the same pattern in wheat prices, interest rates, and railroad stocks.

#### Problem 2 — The Volatility Smile/Skew

The model assumes constant volatility σ, but the **implied volatility** backed out of market option prices systematically varies with strike price and maturity. In particular, since the 1987 Black Monday crash, S&P 500 index options have shown an asymmetric pattern (a "skew" or "smirk" rather than a symmetric "smile") in which out-of-the-money put options carry higher implied volatility than at-the-money options. This is a case where the model's core assumption of constant volatility is directly contradicted by market data.

#### Problem 3 — Asymmetric Price Dynamics Across Tails

**Chavas, Li & Wang (2023)**, *Journal of Commodity Markets*, **32**, 100381, DOI: 10.1016/j.jcomm.2023.100381, apply a Quantile Autoregression (QAR) model to soybean futures market data and find the following:

- **Upper tail:** overreaction and local instability — consistent with bubble and herding behavior during price spikes.
- **Lower tail:** underreaction and local stability — consistent with liquidity constraints and margin calls.
- **Key conclusion:** the authors conclude that failing to capture the local instability of the upper tail is a more serious problem than simple "fat tails," and that **"the most serious problem with the Black–Scholes model arises in how it represents price dynamics in the lower tail."**

(Note: this study focuses on a **commodity futures market (soybeans)** rather than individual equities.)

#### Problem 4 — Conflating Explanatory Power with Predictive Power (a Philosophy-of-Science Critique)

**Cifuentes & Charlin (2024)**, *Philosophy of Science* (published by Cambridge University Press for the Philosophy of Science Association), revisit the Black–Scholes model from a philosophy-of-science perspective and point out the following:

- That in practice, the model is often used **in a way that contradicts its own premises** (e.g., pricing is based on the assumption of a riskless dynamic hedge, even though such a hedge is actually impossible).
- That although the model's **predictions** are not well supported by market reality, it still functions powerfully as a framework for **explaining** why a given price is rational.
- In other words, the ability to explain "why this price is rational" and the ability to "predict actual prices" are different properties — Black–Scholes is strong at the former and weak at the latter.

#### Problem 5 (a Counterargument) — Rogers & Satchell (2000)

There is also an academic rebuttal to the criticisms above. **Rogers & Satchell (2000)**, *Applied Financial Economics* 10(1), 37-39, "Does the behaviour of the asset tell us anything about the option price formula? A cautionary tale," argue the following:

- The Black–Scholes formula is derived under the **risk-neutral measure**, which is a different object from the **real-world measure** return distribution that we actually observe.
- The observation that log returns under the real-world measure show fat tails, non-constant volatility, or autocorrelation **does not logically imply that the Black–Scholes formula fails to hold under the risk-neutral measure.**
- The authors show that as long as the real-world distribution satisfies a strong condition (positive density everywhere), the Black–Scholes option pricing formula can still hold.
- **Caution:** this does not mean "Black–Scholes is correct." It's a point about **the structure of the argument** — that the mere observation of fat tails or non-constant volatility does not, by itself, logically establish that the model is wrong. Empirical anomalies like the volatility smile itself still remain.

#### Summary

- **Problem 1:** the log-normal assumption vs. fat tails — numerous empirical studies (Mandelbrot & Hudson 2004; Hull; Voss 2012)
- **Problem 2:** the constant-volatility assumption vs. the volatility skew — market data (standardly observed since 1987)
- **Problem 3:** asymmetry in upper- vs. lower-tail dynamics — Chavas, Li & Wang (2023), *J. of Commodity Markets*, 32, 100381
- **Problem 4:** explanatory power ≠ predictive power — Cifuentes & Charlin (2024), *Philosophy of Science*
- **Counterargument:** the real-world measure ≠ the risk-neutral measure — Rogers & Satchell (2000), *Applied Financial Economics*, 10(1), 37-39

**A careful note on the causal relationship between "the Nobel Prize and the financial crisis":** the 1997 Nobel Prize in Economics was awarded to Black, Scholes, and Merton (Black was excluded, having passed away in 1995). However, the claim that "the Black–Scholes model caused the 2008 financial crisis" is inaccurate. More precisely, complex derivatives trading built on this model — and on the broader derivatives-pricing framework it represents — is cited as one factor that amplified systemic risk; establishing a simple causal link between the model itself and the crisis is not academically supported.

---

### (3) The Gap Between Daily and Continuous Compounding — Refining "0.001 Percentage Points"

#### The Problem with the Common Narrative

The claim that "the gap between daily and continuous compounding is about 0.001 percentage points" is roughly correct as a rule of thumb, but it omits the condition that **the value depends on the nominal interest rate.**

#### Exact Figures (Based on a Nominal Annual Rate of 6%)

- **Annual compounding:** 6.0000%
- **Semiannual compounding:** 6.0900%
- **Quarterly compounding:** 6.1364%
- **Monthly compounding:** 6.1678%
- **Daily compounding:** 6.1831%
- **Continuous compounding:** 6.1837%

The gap between daily and continuous compounding is `6.1837% − 6.1831% = 0.0006 percentage points`. Writing "0.001 percentage points" overstates the actual gap by roughly 66%.

#### The Gap Widens as the Nominal Rate Rises

- **Nominal 6%:** gap of 0.0006 pp
- **Nominal 15%:** gap of 0.0036 pp
- **Nominal 25%:** gap of 0.0109 pp (about 18 times the gap at 6%)

**Implication:** the practical maxim "daily compounding ≈ continuous compounding" is only an accurate approximation in a low-interest-rate environment.

#### Mathematica Verification

```mathematica
effectiveDaily[r_] := (1 + r/365)^365 - 1;
effectiveContinuous[r_] := Exp[r] - 1;
Table[
  {r, 100*(effectiveContinuous[r] - effectiveDaily[r])},
  {r, {0.06, 0.15, 0.25}}
]
(* Output: {0.06, 0.0006}, {0.15, 0.0036}, {0.25, 0.0109} *)
```

---

### References for This Section

1. Rogers, L. C. G. & Satchell, S. E. (2000). "Does the behaviour of the asset tell us anything about the option price formula? A cautionary tale." *Applied Financial Economics*, 10(1), 37-39.
2. Chavas, J.-P., Li, J. & Wang, L. (2023). "Option pricing revisited: The role of price volatility and dynamics." *Journal of Commodity Markets*, 32, 100381. DOI: 10.1016/j.jcomm.2023.100381
3. Cifuentes, A. & Charlin, V. (2024). "Further Reflections Based on the Black–Scholes (B-S) Model." *Philosophy of Science*, published online by Cambridge University Press for the Philosophy of Science Association.
4. Black, F. & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy*, 81(3), 637-654.
5. Mandelbrot, B. B. & Hudson, R. L. (2004). *The (Mis)Behavior of Markets: A Fractal View of Risk, Ruin, and Reward.* Basic Books.
6. Voss, J. (2012). "Fact File: S&P 500 Sigma Events." CFA Institute.
7. Hull, J. C. *Options, Futures, and Other Derivatives.* Pearson. (latest edition, of several)

*(The bibliographic details above were confirmed by directly checking the original texts/abstracts via web search; the in-text citations paraphrase and reconstruct the intent of the originals rather than quoting them directly.)*

---

# Appendix. Full Formula Summary

- **① Lump sum:** Discrete `a(1+r)^n` / Continuous `a e^{rt}`
- **② Regular savings (end of period):** Discrete `a{(1+r)^n-1}/r` / Continuous `(a/r)(e^{rt}-1)`
- **③ Reverse calculation (start of period):** Discrete `Sr/[(1+r){(1+r)^n-1}]` / Continuous `Sr/(e^{rt}-1)`
- **④ Present value:** Discrete `S/(1+r)^n` / Continuous `S e^{-rt}`
- **⑤ Loan repayment:** Discrete `Sr(1+r)^n/{(1+r)^n-1}` / Continuous `Sr e^{rt}/(e^{rt}-1)`
- **⑥ Present value of an annuity:** Discrete `a{1-(1+r)^{-n}}/r` / Continuous `(a/r)(1-e^{-rt})`
- **⑦ Perpetuity:** Discrete `a/r` / Continuous `a/r` (identical)
- **Growing perpetuity:** Discrete `a/(r-g)`, where `g<r` / Continuous: extendable to the same structure
- **Real interest rate:** Discrete (exact) `(r-i)/(1+i)`, approximation `r-i` (error `-i(r-i)/(1+i)`) / Continuous `r-i` (exact)
- **Stochastic extension (GBM):** Continuous only `a·exp[(r-σ²/2)t + σWₜ]`

## Full Logical Flow

```text
Sum of a geometric series (Part 0)
   │
   ├─ Substitution: common ratio ρ = (1+r)
   │
Part 1: The 7 discrete-compounding formulas (①~⑦)
   │       │
   │       ├─ Beginning vs. end of month (1-⓪) — the timing of cash flow determines the formula's form
   │       │
   │       └─ Limit as n → ∞ ⇒ perpetuity ⑦ = real estate income capitalization (g=0)
   │              └─ Growing perpetuity: g < r (diverges if g ≥ r)
   │
   ├─ m → ∞ (infinitely subdividing the compounding period) ⇒ the natural constant e emerges
   │
Part 2-1: The 7 continuous-compounding formulas (Σ → ∫)
   │       │
   │       └─ 2-1-ⓐ: pros and cons of discrete vs. continuous — practice uses discrete, theory uses continuous
   │
   ├─ Applying the laws of exponents
   │
Part 2-2: Inflation, from an approximation → an exact equality (r - i)
   │       │
   │       └─ Caution: when r and i diverge significantly, use (r-i)/(1+i)
   │
   ├─ Adding a stochastic term σWₜ into the exponent, via Itô's lemma
   │       │
   │       └─ (dW)² = dt — the second-order term generates the −σ²/2 correction
   │
Part 2-3: Geometric Brownian motion → log-normal distribution → Black–Scholes option pricing
   │
2-3-ⓐ: The limits of GBM and Black–Scholes
   │       ├─ Problem 1: fat tails (Mandelbrot 1962; S&P 500 5σ frequency)
   │       ├─ Problem 2: the volatility smile/skew
   │       ├─ Problem 3: asymmetric tail dynamics (Chavas et al. 2023)
   │       ├─ Problem 4: explanatory power ≠ predictive power (Cifuentes & Charlin 2024)
   │       └─ Counterargument: the risk-neutral measure vs. the real-world measure (Rogers & Satchell 2000)
```

---

*This document lays out how a single mathematical tool — the sum of a geometric series — extends consistently across deposits, savings plans, loans, real estate valuation, inflation adjustment, and stochastic asset pricing models (option pricing theory). Through the contrast between discrete and continuous compounding, the distinction between beginning- and end-of-period payments, a full pros-and-cons comparison, and literature-verified evidence on the empirical limits of GBM and Black–Scholes, it aims to provide the educational context for "why you need to understand both worlds."*
