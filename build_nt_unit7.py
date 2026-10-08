# -*- coding: utf-8 -*-
"""
build_nt_unit7.py
Constructs Unit 7: Non-Linear Diophantine Equations & Fermat's Descent
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Non-Linear Diophantine Equations & Fermat's Descent",
        "leadSummary": "Higher-degree Diophantine equations and quadratic reciprocity: algebraic classification of all primitive Pythagorean triples $(m^2 - n^2, 2mn, m^2 + n^2)$, Fermat's Method of Infinite Descent, impossibility of $x^4 + y^4 = z^2$ and Fermat's Last Theorem for $n = 4$, non-existence of right triangles with square area, quadratic residues and Euler's Criterion, and Gauss's Law of Quadratic Reciprocity.",
        "simulations": ["sim_nt_pythagorean_fermat_descent"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Primitive Pythagorean Triples & Geometric Characterization",
                "content": r"""### 1. Pythagorean Triples

> **Definition 7.1 (Pythagorean Triple):**
> A **Pythagorean triple** is a triplet of positive integers $(x, y, z) \in \mathbb{N}^3$ satisfying the Pythagorean equation:
> $$x^2 + y^2 = z^2$$
> The triple is called **primitive** if $\gcd(x, y, z) = 1$.

> **Lemma 7.1 (Parity in Primitive Triples):**
> In any primitive Pythagorean triple $(x, y, z)$:
> 1. Exactly one of $x, y$ is even and the other is odd.
> 2. The hypotenuse $z$ is always **odd**.

> **Proof:**
> If both $x$ and $y$ were even, then $4 \mid (x^2 + y^2) = z^2 \implies 2 \mid z$, contradicting $\gcd(x, y, z) = 1$.
> If both $x$ and $y$ were odd, then $x \equiv 1 \text{ or } 3 \pmod 4 \implies x^2 \equiv 1 \pmod 4$, and $y^2 \equiv 1 \pmod 4$.
> Thus $z^2 = x^2 + y^2 \equiv 1 + 1 = 2 \pmod 4$.
> But a square of an integer can only be $0$ or $1$ modulo $4$, never $2$!
> Thus, one of $x, y$ is even and the other is odd, which forces $z^2$ (and hence $z$) to be odd. $\blacksquare$

---

### 2. Complete Classification of Primitive Pythagorean Triples

> **Theorem 7.1 (Euclid's Formula for Pythagorean Triples):**
> Without loss of generality, let $y$ be the even member.
> Then $(x, y, z)$ is a primitive Pythagorean triple if and only if there exist coprime positive integers $m > n > 0$ of opposite parity ($\gcd(m, n) = 1$ and $m \not\equiv n \pmod 2$) such that:
> $$x = m^2 - n^2, \qquad y = 2 m n, \qquad z = m^2 + n^2$$

> **Proof:**
> **Verification ($\impliedby$):**
> $x^2 + y^2 = (m^2 - n^2)^2 + (2mn)^2 = m^4 - 2m^2 n^2 + n^4 + 4m^2 n^2 = m^4 + 2m^2 n^2 + n^4 = (m^2 + n^2)^2 = z^2$.
> Coprimality follows because any prime dividing both $z$ and $x$ must divide $z + x = 2m^2$ and $z - x = 2n^2$, forcing $p \mid 2$ (ruled out since $z$ is odd) or $p \mid \gcd(m, n) = 1$.
>
> **Derivation ($\implies$):**
> Rearrange $x^2 + y^2 = z^2$ with $y$ even:
> $$y^2 = z^2 - x^2 = (z - x)(z + x) \implies \left(\frac{y}{2}\right)^2 = \left(\frac{z - x}{2}\right)\left(\frac{z + x}{2}\right)$$
> Since $x$ and $z$ are both odd, $\frac{z - x}{2}$ and $\frac{z + x}{2}$ are integers.
> Let $d = \gcd\left(\frac{z - x}{2}, \frac{z + x}{2}\right)$.
> Then $d \mid \left(\frac{z + x}{2} + \frac{z - x}{2}\right) = z$, and $d \mid \left(\frac{z + x}{2} - \frac{z - x}{2}\right) = x$.
> Since $\gcd(x, z) = 1$, we have $d = 1$.
> Two coprime positive integers whose product is a perfect square must each be perfect squares!
> Therefore:
> $$\frac{z + x}{2} = m^2, \qquad \frac{z - x}{2} = n^2$$
> for some positive integers $m > n > 0$ with $\gcd(m, n) = 1$.
> Adding and subtracting these two equations gives:
> $$z = m^2 + n^2, \qquad x = m^2 - n^2$$
> And:
> $$\left(\frac{y}{2}\right)^2 = m^2 n^2 \implies y = 2 m n \quad \blacksquare$$"""
            },
            {
                "secNumber": "7.2",
                "title": "Fermat's Method of Infinite Descent & Impossibility of x^4 + y^4 = z^2",
                "content": r"""### 1. The Method of Infinite Descent

Pierre de Fermat invented the **Method of Infinite Descent** (*descente infinie*), a proof-by-contradiction technique based on the Well-Ordering Principle of $\mathbb{N}$:
1. Assume a Diophantine equation possesses a non-trivial solution in positive integers.
2. Select a solution that minimizes a specific positive invariant (such as $z > 0$).
3. Use the algebraic properties of the equation to construct a strictly smaller positive integer solution ($0 < z' < z$).
4. The existence of an infinite descending sequence of positive integers $z > z' > z'' > \dots > 0$ contradicts the Well-Ordering Principle!
5. Conclude that no positive integer solutions exist.

---

### 2. Impossibility of $x^4 + y^4 = z^2$

> **Theorem 7.2 (Fermat's Theorem on Sums of Fourth Powers):**
> The Diophantine equation:
> $$x^4 + y^4 = z^2$$
> has no solutions in non-zero integers $x, y, z \in \mathbb{Z} \setminus \{0\}$.

> **Proof:**
> Suppose for contradiction that non-zero solutions exist.
> We may assume $x, y, z > 0$ and $\gcd(x, y) = 1$ (dividing out any common factors).
> By the Well-Ordering Principle, choose a solution with the **smallest possible positive value of $z$**.
> Write the equation as:
> $$(x^2)^2 + (y^2)^2 = z^2$$
> This is a primitive Pythagorean triple $(x^2, y^2, z)$.
> By Theorem 7.1, exactly one of $x^2, y^2$ is even; without loss of generality, let $x^2$ be odd and $y^2$ be even.
> Then there exist coprime integers $m > n > 0$ of opposite parity such that:
> $$x^2 = m^2 - n^2, \qquad y^2 = 2 m n, \qquad z = m^2 + n^2$$
> Rewrite $x^2 = m^2 - n^2$ as:
> $$x^2 + n^2 = m^2$$
> Since $\gcd(x, y) = 1$ and $y^2 = 2mn$, we have $\gcd(m, n) = 1$, so $(x, n, m)$ is also a primitive Pythagorean triple!
> Since $x$ is odd, $n$ must be even.
> Applying Euclid's formula (Theorem 7.1) a second time:
> $$n = 2 a b, \qquad m = a^2 + b^2$$
> where $\gcd(a, b) = 1$ and $a, b > 0$.
> Now examine $y^2 = 2 m n = 2(a^2 + b^2)(2 a b) = 4 a b (a^2 + b^2)$:
> $$\left(\frac{y}{2}\right)^2 = a \cdot b \cdot (a^2 + b^2)$$
> Since $\gcd(a, b) = 1$, the three integers $a, b,$ and $a^2 + b^2$ are pairwise coprime!
> Since their product is a square $(y/2)^2$, each factor must individually be a square:
> $$a = u^2, \qquad b = v^2, \qquad a^2 + b^2 = w^2$$
> for some positive integers $u, v, w > 0$.
> Substituting $a = u^2$ and $b = v^2$ into $a^2 + b^2 = w^2$:
> $$(u^2)^2 + (v^2)^2 = w^2 \iff u^4 + v^4 = w^2$$
> Thus, $(u, v, w)$ is another positive integer solution to the original equation!
> We now compare $w$ with $z$:
> $$z = m^2 + n^2 > m^2 = (a^2 + b^2)^2 = (w^2)^2 = w^4 \ge w$$
> Thus $0 < w < z$, contradicting the minimality of $z$!
> Therefore, no non-zero integer solutions exist. $\blacksquare$"""
            },
            {
                "secNumber": "7.3",
                "title": "Fermat's Last Theorem for n = 4 & Congruent Number Problem",
                "content": r"""### 1. Fermat's Last Theorem for $n = 4$

> **Corollary 7.1 (Fermat's Last Theorem for $n = 4$):**
> The equation:
> $$x^4 + y^4 = z^4$$
> has no solutions in non-zero integers $x, y, z$.

> **Proof:**
> If $x^4 + y^4 = z^4$ had a solution $(x, y, z)$, then setting $Z = z^2$ would yield:
> $$x^4 + y^4 = (z^2)^2 = Z^2$$
> By Theorem 7.2, $x^4 + y^4 = Z^2$ has no non-zero integer solutions.
> Thus $x^4 + y^4 = z^4$ has no non-zero integer solutions. $\blacksquare$

---

### 2. Non-Existence of Right Triangles with Square Area

Fermat noted in the margin of Diophantus's *Arithmetica* that the area of a right triangle with integer sides cannot be a square.

> **Theorem 7.3 (No Right Triangle with Square Area):**
> There do not exist positive integers $a, b, c, w$ such that:
> $$a^2 + b^2 = c^2 \quad \text{and} \quad \frac{1}{2} a b = w^2$$

> **Proof:**
> Suppose such a triangle exists.
> Adding and subtracting $4 w^2 = 2 a b$ from $c^2 = a^2 + b^2$:
> $$c^2 + 4 w^2 = a^2 + 2 a b + b^2 = (a + b)^2$$
> $$c^2 - 4 w^2 = a^2 - 2 a b + b^2 = (a - b)^2$$
> Multiplying these two equations:
> $$(c^2 + 4 w^2)(c^2 - 4 w^2) = (a + b)^2(a - b)^2 \iff c^4 - 16 w^4 = (a^2 - b^2)^2$$
> Setting $X = a^2 - b^2$, $Y = 2 w$, and $Z = c$:
> $$X^2 + Y^4 = Z^4 \iff (Z^2)^2 - (Y^2)^2 = X^2$$
> This leads directly to a solution of $u^4 + v^4 = t^2$, which was proved impossible in Theorem 7.2! $\blacksquare$"""
            },
            {
                "secNumber": "7.4",
                "title": "Quadratic Residues, The Legendre Symbol & Euler's Criterion",
                "content": r"""### 1. Quadratic Residues

> **Definition 7.2 (Quadratic Residue and Non-Residue):**
> Let $p$ be an odd prime and $\gcd(a, p) = 1$.
> $a$ is called a **quadratic residue modulo $p$** if the congruence:
> $$x^2 \equiv a \pmod p$$
> has an integer solution. If no solution exists, $a$ is called a **quadratic non-residue modulo $p$**.

Among the reduced residues $\{1, 2, \dots, p - 1\}$, exactly half ($\frac{p-1}{2}$) are quadratic residues, and the other half ($\frac{p-1}{2}$) are quadratic non-residues.

---

### 2. The Legendre Symbol

> **Definition 7.3 (The Legendre Symbol):**
> For an odd prime $p$ and $a \in \mathbb{Z}$:
> $$\left(\frac{a}{p}\right) = \begin{cases}
> 1 & \text{if } a \text{ is a quadratic residue modulo } p \text{ and } p \nmid a \\
> -1 & \text{if } a \text{ is a quadratic non-residue modulo } p \\
> 0 & \text{if } p \mid a
> \end{cases}$$

---

### 3. Euler's Criterion

> **Theorem 7.4 (Euler's Criterion, 1748):**
> For any odd prime $p$ and integer $a$:
> $$\left(\frac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p$$

> **Proof:**
> If $p \mid a$, then $0 \equiv 0 \pmod p$.
> Now assume $p \nmid a$.
> - **Case 1: $a$ is a quadratic residue.**
>   Then $x^2 \equiv a \pmod p$ for some $x$.
>   By Fermat's Little Theorem (Theorem 4.1):
>   $$a^{\frac{p-1}{2}} \equiv (x^2)^{\frac{p-1}{2}} = x^{p-1} \equiv 1 \equiv \left(\frac{a}{p}\right) \pmod p$$
> - **Case 2: $a$ is a quadratic non-residue.**
>   For each $u \in \{1, 2, \dots, p - 1\}$, there is a unique $v \in \{1, 2, \dots, p - 1\}$ such that $u v \equiv a \pmod p$.
>   Since $a$ is a non-residue, $u \ne v$ always.
>   Thus the $p - 1$ integers pair up into $\frac{p-1}{2}$ pairs $\{u_i, v_i\}$ each having product $a$.
>   Multiplying them all together:
>   $$(p - 1)! \equiv a^{\frac{p-1}{2}} \pmod p$$
>   By Wilson's Theorem (Theorem 4.6), $(p - 1)! \equiv -1 \pmod p$.
>   Thus:
>   $$a^{\frac{p-1}{2}} \equiv -1 \equiv \left(\frac{a}{p}\right) \pmod p \quad \blacksquare$$

> **Corollary 7.2 (First Supplement to Quadratic Reciprocity):**
> Setting $a = -1$ in Euler's Criterion:
> $$\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}} = \begin{cases} 1 & \text{if } p \equiv 1 \pmod 4 \\ -1 & \text{if } p \equiv 3 \pmod 4 \end{cases}$$
> Thus $-1$ is a quadratic residue modulo $p$ if and only if $p \equiv 1 \pmod 4$!"""
            },
            {
                "secNumber": "7.5",
                "title": "Gauss's Lemma & The Law of Quadratic Reciprocity",
                "content": r"""### 1. Gauss's Lemma

> **Theorem 7.5 (Gauss's Lemma, 1808):**
> Let $p$ be an odd prime and $\gcd(a, p) = 1$.
> Consider the set of multiples:
> $$S = \left\{ a, 2a, 3a, \dots, \left(\frac{p-1}{2}\right)a \right\}$$
> Reduce each element to its least positive residue modulo $p$.
> Let $\nu$ be the number of these residues that exceed $p/2$.
> Then:
> $$\left(\frac{a}{p}\right) = (-1)^\nu$$

---

### 2. The Second Supplement: When is 2 a Quadratic Residue?

> **Theorem 7.6 (Second Supplement to Quadratic Reciprocity):**
> For any odd prime $p$:
> $$\left(\frac{2}{p}\right) = (-1)^{\frac{p^2 - 1}{8}} = \begin{cases} 1 & \text{if } p \equiv \pm 1 \pmod 8 \\ -1 & \text{if } p \equiv \pm 3 \pmod 8 \end{cases}$$

---

### 3. The Law of Quadratic Reciprocity

Gauss called this theorem the *Theorema Aureum* ("Golden Theorem"), publishing eight distinct proofs over his lifetime.

> **Theorem 7.7 (The Law of Quadratic Reciprocity - Gauss, 1796):**
> Let $p$ and $q$ be distinct odd prime numbers. Then:
> $$\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{\left(\frac{p-1}{2}\right)\left(\frac{q-1}{2}\right)}$$
> Equivalently:
> $$\left(\frac{p}{q}\right) = \begin{cases}
> -\left(\frac{q}{p}\right) & \text{if } p \equiv q \equiv 3 \pmod 4 \\
> \left(\frac{q}{p}\right) & \text{if } p \equiv 1 \pmod 4 \text{ or } q \equiv 1 \pmod 4
> \end{cases}$$

Eisenstein's geometric proof counts integer lattice points inside the rectangle $\left[1, \frac{p-1}{2}\right] \times \left[1, \frac{q-1}{2}\right]$, establishing the identity through triangular partition."""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-7-1",
                "tier": "Foundational",
                "title": "Evaluation of Legendre Symbol via Quadratic Reciprocity",
                "statement": r"""Compute the Legendre symbol:
$$\left(\frac{219}{383}\right)$$
given that $383$ is a prime number.
1. Factor the numerator $219$ into prime factors.
2. Apply the multiplicativity of the Legendre symbol.
3. Use the Law of Quadratic Reciprocity and its supplements to evaluate the symbol completely.""",
                "hints": [
                    "Factor 219 = 3 * 73.",
                    "Split (219/383) = (3/383) * (73/383).",
                    "Check 383 mod 4, 3 mod 4, and 73 mod 4 to apply reciprocity."
                ],
                "solution": r"""### 1. Factorization of the Numerator
Factor $219$:
$$219 = 3 \times 73$$
Both $3$ and $73$ are prime numbers.
By the multiplicativity of the Legendre symbol:
$$\left(\frac{219}{383}\right) = \left(\frac{3}{383}\right) \left(\frac{73}{383}\right) \quad \blacksquare$$

---

### 2. Evaluating $\left(\frac{3}{383}\right)$
Check the primes modulo $4$:
$$383 = 4 \times 95 + 3 \equiv 3 \pmod 4$$
$$3 \equiv 3 \pmod 4$$
Since both $3 \equiv 3 \pmod 4$ and $383 \equiv 3 \pmod 4$, the Law of Quadratic Reciprocity introduces a negative sign:
$$\left(\frac{3}{383}\right) = -\left(\frac{383}{3}\right)$$
Reduce $383$ modulo $3$:
$$383 = 3 \times 127 + 2 \equiv 2 \pmod 3$$
Thus:
$$\left(\frac{383}{3}\right) = \left(\frac{2}{3}\right) = -1$$
Therefore:
$$\left(\frac{3}{383}\right) = -(-1) = 1 \quad \blacksquare$$

---

### 3. Evaluating $\left(\frac{73}{383}\right)$
Check $73$ modulo $4$:
$$73 = 4 \times 18 + 1 \equiv 1 \pmod 4$$
Since $73 \equiv 1 \pmod 4$, Quadratic Reciprocity preserves the sign:
$$\left(\frac{73}{383}\right) = \left(\frac{383}{73}\right)$$
Reduce $383$ modulo $73$:
$$383 = 5 \times 73 + 18 \implies 383 \equiv 18 \pmod{73}$$
Thus:
$$\left(\frac{383}{73}\right) = \left(\frac{18}{73}\right) = \left(\frac{2 \times 3^2}{73}\right) = \left(\frac{2}{73}\right) \left(\frac{3^2}{73}\right) = \left(\frac{2}{73}\right)(1) = \left(\frac{2}{73}\right)$$
Now evaluate $\left(\frac{2}{73}\right)$ using the Second Supplement:
Check $73$ modulo $8$:
$$73 = 8 \times 9 + 1 \equiv 1 \pmod 8$$
By Theorem 7.6:
$$\left(\frac{2}{73}\right) = 1$$
Therefore:
$$\left(\frac{73}{383}\right) = 1 \quad \blacksquare$$

---

### 4. Final Product
Multiplying the two symbols:
$$\left(\frac{219}{383}\right) = \left(\frac{3}{383}\right) \left(\frac{73}{383}\right) = (1)(1) = 1 \quad \blacksquare$$
Thus, $219$ is a quadratic residue modulo $383$!"""
            },
            {
                "id": "nt-prob-7-2",
                "tier": "Advanced",
                "title": "Non-Solvability of Right Triangles with Square Area",
                "statement": r"""Prove that there does not exist any right-angled triangle with integer side lengths whose area is a perfect square.
1. Formulate the problem as a system of Diophantine equations: $a^2 + b^2 = c^2$ and $\frac{1}{2}ab = w^2$.
2. Reduce the problem to primitive Pythagorean triples where $a = m^2 - n^2, b = 2mn, c = m^2 + n^2$.
3. Deduce that $mn(m^2 - n^2) = w^2$ and use coprimality to derive that $m, n, m-n, m+n$ are all perfect squares.
4. Conclude by deriving a strictly smaller solution to $x^4 - y^4 = z^2$ via infinite descent.""",
                "hints": [
                    "Assume a minimal positive solution exists.",
                    "Area = (1/2) * (m^2 - n^2) * (2mn) = mn(m - n)(m + n) = w^2.",
                    "Since m, n, m-n, m+n are pairwise coprime, each must be a square."
                ],
                "solution": r"""### 1. Mathematical Formulation
Let the right triangle have integer legs $a, b$ and hypotenuse $c$, with area $\frac{1}{2} a b = w^2$.
Dividing out common factors, we may assume $\gcd(a, b, c) = 1$, so $(a, b, c)$ is a primitive Pythagorean triple with minimal hypotenuse $c > 0$. $\blacksquare$

---

### 2. Parametric Form
By Theorem 7.1, there exist coprime integers $m > n > 0$ of opposite parity such that:
$$a = m^2 - n^2, \qquad b = 2 m n, \qquad c = m^2 + n^2$$
The area condition is:
$$\text{Area} = \frac{1}{2} a b = \frac{1}{2}(m^2 - n^2)(2 m n) = m n (m^2 - n^2) = m n (m - n)(m + n) = w^2 \quad \blacksquare$$

---

### 3. Pairwise Coprimality of Factors
We examine the four factors $m, n, m - n, m + n$:
- $\gcd(m, n) = 1$.
- Any prime dividing $m$ and $m - n$ must divide $n$, contradiction.
- Any prime dividing $n$ and $m - n$ must divide $m$, contradiction.
- Any prime dividing $m - n$ and $m + n$ must divide their sum $2m$ and difference $2n$. Since $m, n$ have opposite parity, $m - n$ and $m + n$ are both odd, so $p \ne 2$. Thus $p \mid m$ and $p \mid n$, contradiction.
Therefore, the four factors $m, n, m - n, m + n$ are **pairwise relatively prime**!
Since their product is a perfect square $w^2$, each factor must individually be a square:
$$m = u^2, \qquad n = v^2, \qquad m + n = r^2, \qquad m - n = s^2$$
for some positive integers $u, v, r, s > 0$. $\blacksquare$

---

### 4. Descent Contradiction
Notice that:
$$r^2 + s^2 = (m + n) + (m - n) = 2 m = 2 u^2$$
$$r^2 - s^2 = (m + n) - (m - n) = 2 n = 2 v^2$$
Adding and subtracting:
$$\left(\frac{r + s}{2}\right)^2 + \left(\frac{r - s}{2}\right)^2 = \frac{r^2 + s^2}{2} = u^2$$
This forms a new right triangle with legs $X = \frac{r + s}{2}, Y = \frac{r - s}{2}$ and hypotenuse $u$.
Its area is:
$$\text{Area}' = \frac{1}{2} X Y = \frac{1}{2}\left(\frac{r + s}{2}\right)\left(\frac{r - s}{2}\right) = \frac{r^2 - s^2}{8} = \frac{2 v^2}{8} = \left(\frac{v}{2}\right)^2 = \text{a perfect square}!$$
Now compare hypotenuses:
$$\text{Hypotenuse}' = u = \sqrt{m} < m < m^2 + n^2 = c$$
Thus, we have constructed a strictly smaller right triangle $(X, Y, u)$ with integer sides and square area!
This generates an infinite descending sequence of positive integer hypotenuses, which contradicts the Well-Ordering Principle of $\mathbb{N}$!
Hence, no such right triangle can exist. $\blacksquare$"""
            },
            {
                "id": "nt-prob-7-3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Proof of Fermat's Fourth Power Equation x^4 + y^4 = z^2",
                "statement": r"""Provide a complete, unskipped line-by-line proof that the Diophantine equation:
$$x^4 + y^4 = z^2$$
has no solutions in non-zero integers $x, y, z$.
1. Set up the minimal counterexample $(x, y, z)$ with $z > 0$ minimal.
2. Apply the Pythagorean parametrization to $(x^2, y^2, z)$ and show $y^2 = 2mn$.
3. Apply the parametrization a second time to $x^2 + n^2 = m^2$.
4. Derive the existence of a new non-trivial solution $(u, v, w)$ with $w < z$, establishing Fermat's infinite descent contradiction.""",
                "hints": [
                    "Ensure gcd(x, y) = 1 by dividing out common factors.",
                    "Show that x^2 must be odd and y^2 even, so y^2 = 2mn.",
                    "Then x^2 + n^2 = m^2 is a primitive triple with n even."
                ],
                "solution": r"""### 1. Minimal Counterexample Setup
Suppose non-zero integer solutions exist.
Without loss of generality, assume $x, y, z > 0$ and $\gcd(x, y) = 1$.
By the Well-Ordering Principle, choose a solution $(x, y, z)$ such that $z$ is the **strictly minimal positive integer** among all solutions. $\blacksquare$

---

### 2. First Pythagorean Reduction
View the equation as:
$$(x^2)^2 + (y^2)^2 = z^2$$
Since $\gcd(x, y) = 1$, $(x^2, y^2, z)$ is a primitive Pythagorean triple.
By Lemma 7.1, one of $x^2, y^2$ is even and the other odd.
Without loss of generality, assume $x^2$ is odd and $y^2$ is even.
By Theorem 7.1, there exist coprime integers $m > n > 0$ of opposite parity such that:
$$x^2 = m^2 - n^2, \qquad y^2 = 2 m n, \qquad z = m^2 + n^2 \quad \blacksquare$$

---

### 3. Second Pythagorean Reduction
Rewrite $x^2 = m^2 - n^2$ as:
$$x^2 + n^2 = m^2$$
Since $\gcd(m, n) = 1$, this is another primitive Pythagorean triple $(x, n, m)$.
Since $x$ is odd, $n$ must be even, and $m$ is odd.
Applying Theorem 7.1 again, there exist coprime integers $a > b > 0$ of opposite parity such that:
$$n = 2 a b, \qquad m = a^2 + b^2, \qquad x = a^2 - b^2 \quad \blacksquare$$

---

### 4. Factorization of $y^2$ and Synthesis of New Solution
Now substitute $m = a^2 + b^2$ and $n = 2ab$ into $y^2 = 2 m n$:
$$y^2 = 2(a^2 + b^2)(2 a b) = 4 a b (a^2 + b^2)$$
Dividing by $4$:
$$\left(\frac{y}{2}\right)^2 = a \cdot b \cdot (a^2 + b^2)$$
Since $\gcd(a, b) = 1$ and $a, b$ have opposite parity:
- $\gcd(a, a^2 + b^2) = \gcd(a, b^2) = 1$.
- $\gcd(b, a^2 + b^2) = \gcd(b, a^2) = 1$.
Thus, $a, b,$ and $a^2 + b^2$ are pairwise coprime positive integers whose product is a perfect square.
By unique prime factorization, each factor must be a square:
$$a = u^2, \qquad b = v^2, \qquad a^2 + b^2 = w^2$$
for some positive integers $u, v, w > 0$.
Substitute $a = u^2$ and $b = v^2$ into $a^2 + b^2 = w^2$:
$$(u^2)^2 + (v^2)^2 = w^2 \iff u^4 + v^4 = w^2$$
Thus $(u, v, w)$ is a new non-zero integer solution to the original equation!

Now compare $w$ with $z$:
$$z = m^2 + n^2 > m^2 = (a^2 + b^2)^2 = (w^2)^2 = w^4 \ge w^2 \ge w$$
Thus:
$$0 < w < z$$
This directly contradicts the assumption that $z$ was the minimal positive integer!
Therefore, no non-zero integer solutions exist. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print(f"Loaded Unit 7: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
