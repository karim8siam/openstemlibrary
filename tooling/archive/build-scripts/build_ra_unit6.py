# -*- coding: utf-8 -*-
"""
build_ra_unit6.py
Constructs Unit 6: Differentiability: Mean Value Theorems, Taylor's Theorem & L'Hôpital's Rule
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Differentiability: Mean Value Theorems, Taylor's Theorem & L'Hôpital's Rule",
        "leadSummary": "Exhaustive treatment of single-variable differential calculus: difference quotients, differentiability and Carathéodory's formulation, Fermat's interior extremum lemma, Darboux's theorem on derivative intermediate values, Rolle's and Lagrange's Mean Value Theorems, Cauchy's Generalized Mean Value Theorem, rigorous proof of L'Hôpital's rules, and Taylor's theorem with Lagrange, Cauchy, and integral remainders.",
        "simulations": ["sim_ra_mvt_taylor"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "The Derivative: Difference Quotients & Carathéodory's Formulation",
                "content": r"""### 1. The Classical Definition of the Derivative

> **Definition 6.1 (Derivative at a Point):**
> Let $I \subseteq \mathbb{R}$ be an open interval, $f: I \to \mathbb{R}$, and $c \in I$.
> The function $f$ is **differentiable at $c$** if the limit of the difference quotient exists:
> $$f'(c) = \lim_{x \to c} \frac{f(x) - f(c)}{x - c} = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$$
> The real number $f'(c)$ is the **derivative** of $f$ at $c$.

---

### 2. Carathéodory's Equivalent Formulation

Constantin Carathéodory introduced a powerful reformulation that eliminates division by $x - c$, vastly simplifying proofs of the Chain Rule and multivariable extensions.

> **Theorem 6.1 (Carathéodory's Theorem):**
> Let $f: I \to \mathbb{R}$ and $c \in I$. Then $f$ is differentiable at $c$ if and only if there exists a function $\phi: I \to \mathbb{R}$ that is **continuous at $c$** such that:
> $$f(x) - f(c) = \phi(x) (x - c) \quad \forall x \in I$$
> In this case, $\phi(c) = f'(c)$.

#### Proof:
$(\implies)$ If $f'(c)$ exists, define:
$$\phi(x) = \begin{cases} \frac{f(x) - f(c)}{x - c} & \text{if } x \ne c \\ f'(c) & \text{if } x = c \end{cases}$$
Then $\lim_{x \to c} \phi(x) = f'(c) = \phi(c)$, so $\phi$ is continuous at $c$, and $f(x) - f(c) = \phi(x)(x - c)$ holds for all $x$.
$(\impliedby)$ If such a continuous $\phi$ exists, then for $x \ne c$:
$$\frac{f(x) - f(c)}{x - c} = \phi(x)$$
Taking limits as $x \to c$: $\lim_{x \to c} \frac{f(x) - f(c)}{x - c} = \lim_{x \to c} \phi(x) = \phi(c)$, so $f'(c) = \phi(c)$ exists. $\blacksquare$

---

### 3. Differentiability Implies Continuity

> **Theorem 6.2 (Differentiability Implies Continuity):**
> If $f$ is differentiable at $c$, then $f$ is continuous at $c$.

#### Proof:
Using Carathéodory's formulation:
$$\lim_{x \to c} [f(x) - f(c)] = \lim_{x \to c} [\phi(x) (x - c)] = \phi(c) \cdot 0 = 0 \implies \lim_{x \to c} f(x) = f(c) \quad \blacksquare$$

> **The Chain Rule via Carathéodory:**
> Let $g$ be differentiable at $c$ and $f$ differentiable at $g(c)$.
> By Carathéodory: $g(x) - g(c) = \psi(x)(x - c)$ with $\psi(c) = g'(c)$, and $f(y) - f(g(c)) = \phi(y)(y - g(c))$ with $\phi(g(c)) = f'(g(c))$.
> Substituting $y = g(x)$:
> $$(f \circ g)(x) - (f \circ g)(c) = \phi(g(x))(g(x) - g(c)) = [\phi(g(x)) \psi(x)] (x - c)$$
> Since composite continuous functions are continuous, $\lim_{x \to c} [\phi(g(x)) \psi(x)] = f'(g(c)) g'(c)$.
> Thus $(f \circ g)'(c) = f'(g(c)) g'(c)$ with zero division-by-zero complications! $\blacksquare$"""
            },
            {
                "secNumber": "6.2",
                "title": "Local Extrema, Fermat's Lemma & Darboux's Theorem for Derivatives",
                "content": r"""### 1. Interior Local Extrema: Fermat's Theorem

> **Definition 6.2 (Local Extrema):**
> Let $f: E \to \mathbb{R}$. A point $c \in E$ is a **local maximum** (resp. **local minimum**) if there exists $\delta > 0$ such that $f(x) \le f(c)$ (resp. $f(x) \ge f(c)$) for all $x \in (c - \delta, c + \delta) \cap E$.

> **Theorem 6.3 (Fermat's Interior Extremum Lemma):**
> Let $f: (a, b) \to \mathbb{R}$ have a local extremum at an interior point $c \in (a, b)$. If $f$ is differentiable at $c$, then:
> $$f'(c) = 0$$

#### Line-by-Line Proof:
Assume without loss of generality that $c$ is a local maximum (the local minimum case is analogous).
Then there exists $\delta > 0$ such that $f(x) \le f(c)$ for all $x \in (c - \delta, c + \delta) \subseteq (a, b)$.
1. **Left-hand difference quotient ($x < c$):**
   For any $x \in (c - \delta, c)$, $x - c < 0$ and $f(x) - f(c) \le 0$.
   Therefore:
   $$\frac{f(x) - f(c)}{x - c} \ge 0 \implies f'(c) = \lim_{x \to c^-} \frac{f(x) - f(c)}{x - c} \ge 0$$
2. **Right-hand difference quotient ($x > c$):**
   For any $x \in (c, c + \delta)$, $x - c > 0$ and $f(x) - f(c) \le 0$.
   Therefore:
   $$\frac{f(x) - f(c)}{x - c} \le 0 \implies f'(c) = \lim_{x \to c^+} \frac{f(x) - f(c)}{x - c} \le 0$$
Since $f$ is differentiable at $c$, both one-sided limits exist and equal $f'(c)$:
$$0 \le f'(c) \le 0 \implies f'(c) = 0 \quad \blacksquare$$

---

### 2. Darboux's Intermediate Value Theorem for Derivatives

Does the derivative of a function have to be continuous? No! For instance, $f(x) = x^2 \sin(1/x)$ for $x \ne 0$ with $f(0) = 0$ is everywhere differentiable, but its derivative oscillates wildly and is discontinuous at $x = 0$.
However, Jean Gaston Darboux proved that **every derivative still satisfies the Intermediate Value Property**, even if it is completely discontinuous!

> **Theorem 6.4 (Darboux's Theorem):**
> Let $f: [a, b] \to \mathbb{R}$ be differentiable on $[a, b]$.
> If $k$ is any real number strictly between $f'(a)$ and $f'(b)$, then there exists at least one $c \in (a, b)$ such that:
> $$f'(c) = k$$

#### Proof:
Assume without loss of generality that $f'(a) < k < f'(b)$.
Define the auxiliary function:
$$g(x) = f(x) - k x \quad \text{on } [a, b]$$
Since $f$ is differentiable on $[a, b]$, $g$ is continuous on $[a, b]$.
By the Weierstrass Extreme Value Theorem (Theorem 5.4), $g$ attains its global minimum on $[a, b]$ at some point $c \in [a, b]$.
We show that $c$ cannot be $a$ or $b$:
- At $a$: $g'(a) = f'(a) - k < 0$.
  Since $g'(a) < 0$, $\lim_{x \to a^+} \frac{g(x) - g(a)}{x - a} < 0$, which means $g(x) < g(a)$ for all $x$ sufficiently close to $a$ on the right.
  Thus $a$ is not the minimum: $c \ne a$.
- At $b$: $g'(b) = f'(b) - k > 0$.
  Since $g'(b) > 0$, $\lim_{x \to b^-} \frac{g(x) - g(b)}{x - b} > 0$, which means $g(x) < g(b)$ for all $x$ sufficiently close to $b$ on the left.
  Thus $b$ is not the minimum: $c \ne b$.
Therefore, the minimum must occur at an interior point $c \in (a, b)$.
By Fermat's Lemma (Theorem 6.3):
$$g'(c) = 0 \iff f'(c) - k = 0 \iff f'(c) = k \quad \blacksquare$$"""
            },
            {
                "secNumber": "6.3",
                "title": "Rolle's Theorem, Lagrange & Cauchy Mean Value Theorems",
                "content": r"""### 1. Rolle's Theorem

> **Theorem 6.5 (Rolle's Theorem):**
> Let $f: [a, b] \to \mathbb{R}$ satisfy:
> 1. $f$ is continuous on the closed interval $[a, b]$.
> 2. $f$ is differentiable on the open interval $(a, b)$.
> 3. $f(a) = f(b)$.
> Then there exists at least one point $c \in (a, b)$ such that $f'(c) = 0$.

#### Proof:
By the Extreme Value Theorem, $f$ attains both a maximum $M$ and a minimum $m$ on $[a, b]$.
- If $M = m$, $f$ is constant on $[a, b]$, so $f'(c) = 0$ for all $c \in (a, b)$.
- If $M \ne m$, since $f(a) = f(b)$, at least one of the extrema (either $M$ or $m$) must occur at an interior point $c \in (a, b)$.
By Fermat's Lemma, at this interior extremum, $f'(c) = 0$. $\blacksquare$

---

### 2. Lagrange's Mean Value Theorem

> **Theorem 6.6 (Lagrange's Mean Value Theorem - MVT):**
> Let $f: [a, b] \to \mathbb{R}$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
> Then there exists at least one point $c \in (a, b)$ such that:
> $$f'(c) = \frac{f(b) - f(a)}{b - a} \iff f(b) - f(a) = f'(c)(b - a)$$

#### Proof:
The secant line connecting $(a, f(a))$ and $(b, f(b))$ has equation:
$$y = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$$
Define the vertical distance function $h: [a, b] \to \mathbb{R}$:
$$h(x) = f(x) - \left[ f(a) + \frac{f(b) - f(a)}{b - a}(x - a) \right]$$
1. $h$ is continuous on $[a, b]$ (linear combination of continuous functions).
2. $h$ is differentiable on $(a, b)$ with $h'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$.
3. $h(a) = f(a) - f(a) = 0$, and $h(b) = f(b) - f(b) = 0$.
Thus $h(a) = h(b) = 0$.
By Rolle's Theorem, there exists $c \in (a, b)$ such that $h'(c) = 0$:
$$f'(c) - \frac{f(b) - f(a)}{b - a} = 0 \iff f'(c) = \frac{f(b) - f(a)}{b - a} \quad \blacksquare$$

---

### 3. Cauchy's Generalized Mean Value Theorem

> **Theorem 6.7 (Cauchy's Mean Value Theorem):**
> Let $f, g: [a, b] \to \mathbb{R}$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
> Then there exists $c \in (a, b)$ such that:
> $$[f(b) - f(a)] g'(c) = [g(b) - g(a)] f'(c)$$
> If $g'(x) \ne 0$ on $(a, b)$, this is equivalently written as:
> $$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

#### Proof:
Define the auxiliary function:
$$h(x) = [f(b) - f(a)] g(x) - [g(b) - g(a)] f(x)$$
Notice that:
- $h(a) = f(b)g(a) - f(a)g(a) - g(b)f(a) + g(a)f(a) = f(b)g(a) - g(b)f(a)$.
- $h(b) = f(b)g(b) - f(a)g(b) - g(b)f(b) + g(a)f(b) = f(b)g(a) - g(b)f(a) = h(a)$.
$h$ satisfies Rolle's Theorem on $[a, b]$. Thus there exists $c \in (a, b)$ with $h'(c) = 0$:
$$[f(b) - f(a)] g'(c) - [g(b) - g(a)] f'(c) = 0 \quad \blacksquare$$"""
            },
            {
                "secNumber": "6.4",
                "title": "Indeterminate Forms & Rigorous Proof of L'Hôpital's Rule",
                "content": r"""### 1. The $0/0$ Indeterminate Form

> **Theorem 6.8 (L'Hôpital's Rule for $0/0$):**
> Let $f$ and $g$ be differentiable on $(a, b) \setminus \{c\}$, where $c \in [a, b]$.
> Suppose:
> 1. $\lim_{x \to c} f(x) = 0$ and $\lim_{x \to c} g(x) = 0$.
> 2. $g'(x) \ne 0$ for all $x \in (a, b) \setminus \{c\}$.
> 3. $\lim_{x \to c} \frac{f'(x)}{g'(x)} = L$ (where $L \in \mathbb{R}$ or $\pm \infty$).
> Then:
> $$\lim_{x \to c} \frac{f(x)}{g(x)} = L$$

#### Complete Line-by-Line Proof:
We extend $f$ and $g$ continuously to $c$ by defining $f(c) = 0$ and $g(c) = 0$.
Since $\lim_{x \to c} f(x) = 0 = f(c)$ and $\lim_{x \to c} g(x) = 0 = g(c)$, both $f$ and $g$ are continuous at $c$.
Let $x \in (c, b)$. Both $f$ and $g$ are continuous on $[c, x]$ and differentiable on $(c, x)$.
By Cauchy's Generalized Mean Value Theorem (Theorem 6.7), there exists a point $\xi_x \in (c, x)$ such that:
$$\frac{f(x) - f(c)}{g(x) - g(c)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$
Since $f(c) = 0$ and $g(c) = 0$:
$$\frac{f(x)}{g(x)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$
As $x \to c^+$, the point $\xi_x \in (c, x)$ is squeezed towards $c$: $c < \xi_x < x \implies \lim_{x \to c^+} \xi_x = c$.
Therefore:
$$\lim_{x \to c^+} \frac{f(x)}{g(x)} = \lim_{x \to c^+} \frac{f'(\xi_x)}{g'(\xi_x)} = \lim_{\xi \to c^+} \frac{f'(\xi)}{g'(\xi)} = L$$
An identical argument on $(a, c)$ establishes the left-hand limit $\lim_{x \to c^-} \frac{f(x)}{g(x)} = L$.
Combining both one-sided limits proves the theorem. $\blacksquare$

---

### 2. The $\infty/\infty$ Indeterminate Form

> **Theorem 6.9 (L'Hôpital's Rule for $\infty/\infty$):**
> If $\lim_{x \to c} |g(x)| = \infty$ and $\lim_{x \to c} \frac{f'(x)}{g'(x)} = L$, then:
> $$\lim_{x \to c} \frac{f(x)}{g(x)} = L$$
> Notice that we do not even need to assume that $\lim f(x) = \infty$!"""
            },
            {
                "secNumber": "6.5",
                "title": "Taylor's Theorem with Lagrange, Cauchy & Integral Remainder Forms",
                "content": r"""### 1. Taylor Polynomials and Approximations

> **Definition 6.3 (Taylor Polynomial):**
> Let $f$ be $n$-times differentiable at $x_0$. The **$n$-th order Taylor polynomial** of $f$ centered at $x_0$ is:
> $$P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k = f(x_0) + f'(x_0)(x - x_0) + \dots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$
> The **remainder** (error) is $R_n(x) = f(x) - P_n(x)$.

---

### 2. Taylor's Theorem with Lagrange Remainder

> **Theorem 6.10 (Taylor's Theorem with Lagrange Remainder):**
> Let $f$ be $(n+1)$-times differentiable on an open interval $I$ containing $x_0$ and $x$.
> Then there exists some point $c$ strictly between $x_0$ and $x$ such that:
> $$f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + \frac{f^{(n+1)}(c)}{(n+1)!}(x - x_0)^{n+1}$$

#### Complete Rigorous Proof:
Fix $x \ne x_0$. Define the constant $M$ such that:
$$f(x) - P_n(x) = M (x - x_0)^{n+1} \iff M = \frac{f(x) - P_n(x)}{(x - x_0)^{n+1}}$$
Consider the auxiliary function $g: I \to \mathbb{R}$ defined for $t$ between $x_0$ and $x$:
$$g(t) = f(x) - \left[ \sum_{k=0}^n \frac{f^{(k)}(t)}{k!}(x - t)^k \right] - M(x - t)^{n+1}$$
Notice that:
- At $t = x$: $g(x) = f(x) - f(x) - 0 = 0$.
- At $t = x_0$: $g(x_0) = f(x) - P_n(x) - M(x - x_0)^{n+1} = 0$ (by definition of $M$).
Thus $g(t)$ is continuous on the closed interval between $x_0$ and $x$, and differentiable in between.
Now we compute the derivative $g'(t)$ with respect to $t$.
Differentiating the summation using the product rule:
$$\begin{aligned}
\frac{d}{dt}\left[ \sum_{k=0}^n \frac{f^{(k)}(t)}{k!}(x - t)^k \right] &= f'(t) + \sum_{k=1}^n \left( \frac{f^{(k+1)}(t)}{k!}(x - t)^k - \frac{f^{(k)}(t)}{(k-1)!}(x - t)^{k-1} \right) \\
&= \frac{f^{(n+1)}(t)}{n!}(x - t)^n \quad \text{(all other terms telescope and cancel!)}
\end{aligned}$$
Differentiating the $M$ term: $\frac{d}{dt}[-M(x - t)^{n+1}] = (n+1) M (x - t)^n$.
Therefore:
$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n + (n+1) M (x - t)^n$$
By Rolle's Theorem (Theorem 6.5), there exists $c$ strictly between $x_0$ and $x$ such that $g'(c) = 0$:
$$-\frac{f^{(n+1)}(c)}{n!}(x - c)^n + (n+1) M (x - c)^n = 0$$
Since $c \ne x$, $(x - c)^n \ne 0$. Dividing by $(x - c)^n$:
$$(n+1) M = \frac{f^{(n+1)}(c)}{n!} \implies M = \frac{f^{(n+1)}(c)}{(n+1)!}$$
Substituting $M$ back into $R_n(x) = M(x - x_0)^{n+1}$ yields:
$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - x_0)^{n+1} \quad \blacksquare$$

---

### 3. Cauchy and Integral Forms of the Remainder
- **Cauchy Remainder Form:**
  $$R_n(x) = \frac{f^{(n+1)}(c)}{n!}(x - c)^n (x - x_0)$$
- **Integral Remainder Form (via integration by parts):**
  $$R_n(x) = \frac{1}{n!} \int_{x_0}^x f^{(n+1)}(t)(x - t)^n \, dt$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 6.1",
                "title": "Differentiability with Discontinuous Derivative: The Classical Counterexample",
                "statement": r"""Consider the piecewise function:
$$f(x) = \begin{cases} x^2 \sin\left(\frac{1}{x}\right) & \text{if } x \ne 0 \\ 0 & \text{if } x = 0 \end{cases}$$
1. Prove directly from the limit definition that $f$ is differentiable at $x = 0$ and find $f'(0)$.
2. Calculate $f'(x)$ for all $x \ne 0$.
3. Prove that $f'(x)$ is discontinuous at $x = 0$, demonstrating that differentiability does not guarantee continuity of the derivative.""",
                "hints": [
                    "Evaluate the difference quotient (f(h) - f(0))/h as h -> 0.",
                    "Use the Squeeze Theorem using |sin(1/h)| <= 1.",
                    "For continuity of f', evaluate lim_{x -> 0} f'(x) using two distinct sequences."
                ],
                "solution": r"""### 1. Derivative at $x = 0$ via Difference Quotient
By Definition 6.1:
$$f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h} = \lim_{h \to 0} \frac{h^2 \sin(1/h) - 0}{h} = \lim_{h \to 0} h \sin\left(\frac{1}{h}\right)$$
Since $|\sin(1/h)| \le 1$ for all $h \ne 0$:
$$-|h| \le h \sin\left(\frac{1}{h}\right) \le |h|$$
Since $\lim_{h \to 0} (-|h|) = 0$ and $\lim_{h \to 0} |h| = 0$, by the Squeeze Theorem:
$$f'(0) = \lim_{h \to 0} h \sin\left(\frac{1}{h}\right) = 0$$
Thus $f$ is differentiable at $x = 0$ with $f'(0) = 0$. $\blacksquare$

---

### 2. Derivative for $x \ne 0$
For $x \ne 0$, we apply standard differentiation rules (product rule and chain rule):
$$f'(x) = \frac{d}{dx}[x^2] \cdot \sin\left(\frac{1}{x}\right) + x^2 \cdot \frac{d}{dx}\left[\sin\left(\frac{1}{x}\right)\right]$$
$$f'(x) = 2x \sin\left(\frac{1}{x}\right) + x^2 \left( \cos\left(\frac{1}{x}\right) \cdot \left(-\frac{1}{x^2}\right) \right) = 2x \sin\left(\frac{1}{x}\right) - \cos\left(\frac{1}{x}\right)$$

---

### 3. Discontinuity of $f'$ at $x = 0$
$f'(x)$ is continuous at $0$ if and only if $\lim_{x \to 0} f'(x) = f'(0) = 0$.
Examine the limit:
$$\lim_{x \to 0} f'(x) = \lim_{x \to 0} \left[ 2x \sin\left(\frac{1}{x}\right) - \cos\left(\frac{1}{x}\right) \right]$$
As $x \to 0$, $2x \sin(1/x) \to 0$ by the Squeeze Theorem.
However, consider the sequence $x_n = \frac{1}{2\pi n} \to 0$:
$$f'(x_n) = 2\left(\frac{1}{2\pi n}\right)\sin(2\pi n) - \cos(2\pi n) = 0 - 1 = -1 \to -1$$
Now consider the sequence $y_n = \frac{1}{(2n+1)\pi} \to 0$:
$$f'(y_n) = 0 - \cos((2n+1)\pi) = -(-1) = 1 \to 1$$
Since different sequences give different limits, $\lim_{x \to 0} f'(x)$ does not exist!
Therefore, $f'(x)$ is **discontinuous at $x = 0$**. $\blacksquare$"""
            },
            {
                "tier": "Advanced / Problem 6.2",
                "title": "Complete Deductive Chain: Cauchy MVT to Rigorous L'Hôpital's Rule",
                "statement": r"""1. State and prove Cauchy's Generalized Mean Value Theorem (Theorem 6.7).
2. Use Cauchy's MVT to prove L'Hôpital's Rule for the one-sided limit:
   $$\lim_{x \to a^+} \frac{f(x)}{g(x)} = \lim_{x \to a^+} \frac{f'(x)}{g'(x)} = L$$
   where $\lim_{x \to a^+} f(x) = 0$ and $\lim_{x \to a^+} g(x) = 0$ with $g'(x) \ne 0$ on $(a, b)$.
3. Evaluate the limit: $\lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$.""",
                "hints": [
                    "For Cauchy MVT, construct the linear combination h(x) = (f(b)-f(a))g(x) - (g(b)-g(a))f(x).",
                    "For part 3, apply L'Hôpital's rule iteratively."
                ],
                "solution": r"""### 1. Proof of Cauchy's Generalized MVT
Let $f, g: [a, b] \to \mathbb{R}$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
Define $h(x) = [f(b) - f(a)] g(x) - [g(b) - g(a)] f(x)$.
- $h$ is continuous on $[a, b]$ and differentiable on $(a, b)$.
- Evaluating at endpoints:
  $$h(a) = f(b)g(a) - g(b)f(a) = h(b)$$
By Rolle's Theorem, there exists $c \in (a, b)$ such that $h'(c) = 0$:
$$[f(b) - f(a)] g'(c) - [g(b) - g(a)] f'(c) = 0 \iff [f(b) - f(a)] g'(c) = [g(b) - g(a)] f'(c) \quad \blacksquare$$

---

### 2. Proof of L'Hôpital's Rule ($0/0$)
Extend $f$ and $g$ to $a$ by defining $f(a) = 0$ and $g(a) = 0$.
Since $\lim_{x \to a^+} f(x) = 0 = f(a)$ and $\lim_{x \to a^+} g(x) = 0 = g(a)$, $f$ and $g$ are continuous on $[a, x]$ for any $x \in (a, b)$.
By Cauchy's MVT on $[a, x]$, there exists $c_x \in (a, x)$ such that:
$$[f(x) - f(a)] g'(c_x) = [g(x) - g(a)] f'(c_x)$$
Since $f(a) = g(a) = 0$ and $g'(c_x) \ne 0$:
$$\frac{f(x)}{g(x)} = \frac{f'(c_x)}{g'(c_x)}$$
As $x \to a^+$, since $a < c_x < x$, by the Squeeze Theorem $c_x \to a^+$.
Therefore:
$$\lim_{x \to a^+} \frac{f(x)}{g(x)} = \lim_{x \to a^+} \frac{f'(c_x)}{g'(c_x)} = \lim_{c \to a^+} \frac{f'(c)}{g'(c)} = L \quad \blacksquare$$

---

### 3. Evaluating the Limit
Evaluate $\lim_{x \to 0} \frac{e^x - 1 - x - x^2/2}{x^3}$.
As $x \to 0$, numerator $\to 1 - 1 - 0 - 0 = 0$, denominator $\to 0$. Form: $0/0$.
- Step 1 (L'Hôpital): $\lim_{x \to 0} \frac{e^x - 1 - x}{3x^2}$ ($0/0$).
- Step 2 (L'Hôpital): $\lim_{x \to 0} \frac{e^x - 1}{6x}$ ($0/0$).
- Step 3 (L'Hôpital): $\lim_{x \to 0} \frac{e^x}{6} = \frac{e^0}{6} = \frac{1}{6}$.
Thus, the limit is $\frac{1}{6}$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 6.3",
                "title": "Taylor Remainder Derivation & The Analytic Proof of the Irrationality of e",
                "statement": r"""1. State Taylor's Theorem with the Lagrange remainder for $f(x) = e^x$ centered at $x_0 = 0$.
2. Prove that the Maclaurin series for $e^x$ converges to $e^x$ for all $x \in \mathbb{R}$.
3. Using the Taylor remainder estimate for $e = \sum_{k=0}^n \frac{1}{k!} + R_n(1)$, provide an unassailable proof that Euler's number $e$ is **irrational**.""",
                "hints": [
                    "For e^x, the (n+1)-th derivative is e^x. On [0, 1], e^c < e < 3.",
                    "Assume e = p/q with p, q in N. Choose n = q in Taylor's theorem.",
                    "Multiply by q! to show an integer lies strictly between 0 and 1, creating a contradiction."
                ],
                "solution": r"""### 1. Taylor Expansion with Lagrange Remainder for $e^x$
For $f(x) = e^x$, all derivatives are identical: $f^{(k)}(x) = e^x$ for all $k \ge 0$.
Centering at $x_0 = 0$: $f^{(k)}(0) = e^0 = 1$.
The $n$-th order Taylor polynomial is $P_n(x) = \sum_{k=0}^n \frac{x^k}{k!}$.
By Taylor's Theorem (Theorem 6.10), for any $x \in \mathbb{R}$, there exists $c$ between 0 and $x$ such that:
$$e^x = \sum_{k=0}^n \frac{x^k}{k!} + \frac{e^c}{(n+1)!} x^{n+1}$$

---

### 2. Convergence of the Maclaurin Series for All $x \in \mathbb{R}$
Fix $x \in \mathbb{R}$. Since $c$ is between 0 and $x$, $e^c < e^{|x|}$.
The Lagrange remainder satisfies:
$$|R_n(x)| = \left| \frac{e^c}{(n+1)!} x^{n+1} \right| \le e^{|x|} \frac{|x|^{n+1}}{(n+1)!}$$
For any fixed $x$, the ratio of consecutive terms in the series $\sum \frac{|x|^n}{n!}$ is $\frac{|x|}{n+1} \to 0 < 1$.
By the Ratio Test, $\sum \frac{|x|^n}{n!}$ converges, which forces its general term to approach zero:
$$\lim_{n \to \infty} \frac{|x|^{n+1}}{(n+1)!} = 0 \implies \lim_{n \to \infty} R_n(x) = 0$$
Therefore, $e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$ converges for all $x \in \mathbb{R}$. $\blacksquare$

---

### 3. Rigorous Proof that $e$ is Irrational
Setting $x = 1$ in the Taylor expansion:
$$e = \sum_{k=0}^n \frac{1}{k!} + \frac{e^c}{(n+1)!}, \quad \text{where } 0 < c < 1$$
Since $0 < c < 1$, we have $1 < e^c < e < 3$. Thus:
$$0 < R_n(1) = \frac{e^c}{(n+1)!} < \frac{3}{(n+1)!}$$
Now assume for contradiction that $e$ is rational:
$$e = \frac{p}{q} \quad \text{for some } p, q \in \mathbb{N}, \; q \ge 2$$
Choose $n = q$ in the Taylor remainder formula:
$$\frac{p}{q} = \sum_{k=0}^q \frac{1}{k!} + R_q(1) \iff R_q(1) = \frac{p}{q} - \sum_{k=0}^q \frac{1}{k!}$$
Multiply both sides by $q!$:
$$q! R_q(1) = q! \frac{p}{q} - \sum_{k=0}^q \frac{q!}{k!} = p (q - 1)! - \sum_{k=0}^q \frac{q!}{k!}$$
Notice:
- $p (q - 1)!$ is an integer.
- For each $k \in \{0, 1, \dots, q\}$, $\frac{q!}{k!} = q(q-1)\dots(k+1)$ is an integer.
Therefore, the difference is an **integer**:
$$\mathcal{Z} = q! R_q(1) \in \mathbb{Z}$$
Now we bound $\mathcal{Z} = q! R_q(1)$ using the remainder inequality:
$$0 < q! R_q(1) < q! \cdot \frac{3}{(q+1)!} = \frac{3}{q+1}$$
Since $q \ge 2$, $q + 1 \ge 3$, which means:
$$\frac{3}{q+1} \le \frac{3}{3} = 1$$
(If $q \ge 3$, $\frac{3}{q+1} \le \frac{3}{4} < 1$; for $q = 2$, $e = p/2 \implies 2 < e < 3$, impossible).
In all cases:
$$0 < \mathcal{Z} < 1$$
This asserts the existence of an integer $\mathcal{Z}$ strictly between 0 and 1, which is impossible!
This contradiction refutes the assumption that $e$ is rational.
Therefore, $e$ is **irrational**. $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print(f"Loaded Unit 6: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
