# -*- coding: utf-8 -*-
"""
build_ra_unit3.py
Constructs Unit 3: Real Sequences: Limits, Monotone Convergence & Cauchy Sequences
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Real Sequences: Limits, Monotone Convergence & Cauchy Sequences",
        "leadSummary": "Comprehensive theory of real sequences: epsilon-N limit definition, uniqueness of limits, algebraic limit theorems, the Squeeze Theorem, monotone sequences and the Monotone Convergence Theorem, subsequential limits, limit superior and limit inferior, the Bolzano-Weierstrass theorem, and the Cauchy completeness criterion.",
        "simulations": ["sim_ra_sequence_cauchy"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Sequences and Limits: The Rigorous Epsilon-N Definition & Limit Uniqueness",
                "content": r"""### 1. Real Sequences as Functions

> **Definition 3.1 (Real Sequence):**
> A **sequence of real numbers** is a function $a: \mathbb{N} \to \mathbb{R}$.
> We typically denote the values $a(n)$ as $a_n$ (the $n$-th term), and the sequence itself by $\{a_n\}_{n=1}^\infty$, $(a_n)_{n \in \mathbb{N}}$, or simply $(a_n)$.

---

### 2. The $\epsilon$-$N$ Definition of Sequence Convergence

The concept of a limit is the foundational bedrock of all mathematical analysis, formalized by Augustin-Louis Cauchy and Karl Weierstrass to eliminate vague notions of "infinitesimal approaches."

> **Definition 3.2 (Limit of a Sequence / Convergence):**
> A sequence $(a_n)$ is said to **converge** to a real number $L \in \mathbb{R}$, denoted:
> $$\lim_{n \to \infty} a_n = L \quad \text{or} \quad a_n \to L \text{ as } n \to \infty$$
> if for every $\epsilon > 0$, there exists an index $N \in \mathbb{N}$ (dependent on $\epsilon$) such that:
> $$\forall n \ge N, \quad |a_n - L| < \epsilon$$
> In topological terms, for every $\epsilon$-neighborhood $V_\epsilon(L)$, there exists $N \in \mathbb{N}$ such that $a_n \in V_\epsilon(L)$ for all $n \ge N$.
> If no such $L \in \mathbb{R}$ exists, the sequence is said to **diverge**.

---

### 3. Theorem: Uniqueness of Sequence Limits

Can a sequence converge to two distinct real numbers simultaneously? In any Hausdorff space—and specifically $\mathbb{R}$—the answer is strictly no.

> **Theorem 3.1 (Uniqueness of Limits):**
> If a sequence $(a_n)$ converges, its limit is unique. That is, if $a_n \to L_1$ and $a_n \to L_2$, then $L_1 = L_2$.

#### Line-by-Line Proof:
We prove this by contradiction.
Suppose $a_n \to L_1$ and $a_n \to L_2$ with $L_1 \ne L_2$.
Then $|L_1 - L_2| > 0$.
Choose:
$$\epsilon = \frac{|L_1 - L_2|}{2} > 0$$
Since $a_n \to L_1$, there exists $N_1 \in \mathbb{N}$ such that:
$$\forall n \ge N_1, \quad |a_n - L_1| < \epsilon$$
Since $a_n \to L_2$, there exists $N_2 \in \mathbb{N}$ such that:
$$\forall n \ge N_2, \quad |a_n - L_2| < \epsilon$$
Let $N = \max\{N_1, N_2\}$. For any $n \ge N$, both inequalities hold simultaneously.
Using the Triangle Inequality:
$$|L_1 - L_2| = |(L_1 - a_n) + (a_n - L_2)| \le |L_1 - a_n| + |a_n - L_2| = |a_n - L_1| + |a_n - L_2|$$
Substituting the $\epsilon$-bounds:
$$|L_1 - L_2| < \epsilon + \epsilon = 2\epsilon = 2\left(\frac{|L_1 - L_2|}{2}\right) = |L_1 - L_2|$$
This yields the strict inequality $|L_1 - L_2| < |L_1 - L_2|$, an impossible contradiction!
Therefore, $L_1 = L_2$. $\blacksquare$

---

### 4. Convergence Implies Boundedness

> **Theorem 3.2 (Boundedness of Convergent Sequences):**
> Every convergent sequence $(a_n)$ is bounded.

#### Proof:
Suppose $a_n \to L$. Setting $\epsilon = 1 > 0$, by the definition of limit there exists $N \in \mathbb{N}$ such that:
$$\forall n \ge N, \quad |a_n - L| < 1 \implies |a_n| < |L| + 1$$
For indices prior to $N$ (the terms $a_1, a_2, \dots, a_{N-1}$), there are only finitely many values.
Define:
$$M = \max \{ |a_1|, |a_2|, \dots, |a_{N-1}|, |L| + 1 \}$$
Then for all $n \in \mathbb{N}$, $|a_n| \le M$.
Thus, $(a_n)$ is bounded. $\blacksquare$
*(Note: The converse is false! The sequence $a_n = (-1)^n$ is bounded by 1, but diverges).*"""
            },
            {
                "secNumber": "3.2",
                "title": "Algebraic Limit Theorems, Squeeze Theorem & Order Properties",
                "content": r"""### 1. Algebraic Limit Theorems

> **Theorem 3.3 (Algebra of Limits):**
> Let $(a_n)$ and $(b_n)$ be convergent sequences with $\lim_{n \to \infty} a_n = A$ and $\lim_{n \to \infty} b_n = B$.
> 1. **Sum Rule:** $\lim_{n \to \infty} (a_n + b_n) = A + B$.
> 2. **Scalar Multiple:** $\lim_{n \to \infty} (c a_n) = c A$ for any constant $c \in \mathbb{R}$.
> 3. **Product Rule:** $\lim_{n \to \infty} (a_n b_n) = A B$.
> 4. **Quotient Rule:** If $B \ne 0$ and $b_n \ne 0$ for all $n$, then $\lim_{n \to \infty} \left(\frac{a_n}{b_n}\right) = \frac{A}{B}$.

#### Rigorous Proof of the Product Rule:
We rewrite the difference $a_n b_n - AB$ by adding and subtracting an intermediate term $a_n B$:
$$a_n b_n - AB = a_n b_n - a_n B + a_n B - AB = a_n (b_n - B) + B (a_n - A)$$
Applying the Triangle Inequality:
$$|a_n b_n - AB| \le |a_n| |b_n - B| + |B| |a_n - A|$$
By Theorem 3.2, since $(a_n)$ converges, it is bounded: there exists $M > 0$ such that $|a_n| \le M$ for all $n \in \mathbb{N}$.
Thus:
$$|a_n b_n - AB| \le M |b_n - B| + (|B| + 1) |a_n - A|$$
Let $\epsilon > 0$ be given.
Since $a_n \to A$, choose $N_1 \in \mathbb{N}$ such that $|a_n - A| < \frac{\epsilon}{2(|B| + 1)}$ for all $n \ge N_1$.
Since $b_n \to B$, choose $N_2 \in \mathbb{N}$ such that $|b_n - B| < \frac{\epsilon}{2M}$ for all $n \ge N_2$.
Set $N = \max\{N_1, N_2\}$. For all $n \ge N$:
$$|a_n b_n - AB| < M \left(\frac{\epsilon}{2M}\right) + (|B| + 1)\left(\frac{\epsilon}{2(|B| + 1)}\right) = \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
This proves that $a_n b_n \to AB$. $\blacksquare$

---

### 2. Order Properties and the Squeeze Theorem

> **Theorem 3.4 (Order Limit Theorem):**
> If $a_n \to A$ and $b_n \to B$, and there exists $N_0 \in \mathbb{N}$ such that $a_n \le b_n$ for all $n \ge N_0$, then:
> $$A \le B$$

> **Theorem 3.5 (The Squeeze / Sandwich Theorem):**
> Let $(a_n)$, $(b_n)$, and $(c_n)$ be sequences such that:
> $$a_n \le b_n \le c_n \quad \forall n \ge N_0$$
> If $\lim_{n \to \infty} a_n = L$ and $\lim_{n \to \infty} c_n = L$, then:
> $$\lim_{n \to \infty} b_n = L$$

#### Proof of Squeeze Theorem:
Let $\epsilon > 0$.
Since $a_n \to L$, there exists $N_1$ such that $|a_n - L| < \epsilon \iff L - \epsilon < a_n < L + \epsilon$ for all $n \ge N_1$.
Since $c_n \to L$, there exists $N_2$ such that $|c_n - L| < \epsilon \iff L - \epsilon < c_n < L + \epsilon$ for all $n \ge N_2$.
Choose $N = \max\{N_0, N_1, N_2\}$. For all $n \ge N$:
$$L - \epsilon < a_n \le b_n \le c_n < L + \epsilon \implies L - \epsilon < b_n < L + \epsilon \iff |b_n - L| < \epsilon$$
Thus $b_n \to L$. $\blacksquare$"""
            },
            {
                "secNumber": "3.3",
                "title": "Monotone Sequences, Boundedness & The Monotone Convergence Theorem",
                "content": r"""### 1. Monotone Sequences

> **Definition 3.3 (Monotonicity):**
> A sequence of real numbers $(a_n)$ is:
> 1. **Monotonically increasing** (or non-decreasing) if $a_{n} \le a_{n+1}$ for all $n \in \mathbb{N}$.
> 2. **Strictly increasing** if $a_n < a_{n+1}$ for all $n \in \mathbb{N}$.
> 3. **Monotonically decreasing** (or non-increasing) if $a_n \ge a_{n+1}$ for all $n \in \mathbb{N}$.
> 4. **Strictly decreasing** if $a_n > a_{n+1}$ for all $n \in \mathbb{N}$.
> A sequence is **monotone** if it is either monotonically increasing or monotonically decreasing.

---

### 2. The Monotone Convergence Theorem

The Monotone Convergence Theorem is one of the most powerful analytical engines in real analysis, enabling us to prove convergence without knowing the numerical value of the limit in advance.

> **Theorem 3.6 (Monotone Convergence Theorem - MCT):**
> A monotone sequence of real numbers converges if and only if it is bounded:
> 1. If $(a_n)$ is monotonically increasing and bounded above, then:
>    $$\lim_{n \to \infty} a_n = \sup \{ a_n : n \in \mathbb{N} \}$$
> 2. If $(a_n)$ is monotonically decreasing and bounded below, then:
>    $$\lim_{n \to \infty} a_n = \inf \{ a_n : n \in \mathbb{N} \}$$

#### Line-by-Line Proof:
$(\implies)$ By Theorem 3.2, every convergent sequence is bounded.
$(\impliedby)$ Assume $(a_n)$ is monotonically increasing and bounded above.
Define the non-empty set of values:
$$S = \{ a_n : n \in \mathbb{N} \} \subset \mathbb{R}$$
Since $(a_n)$ is bounded above, $S$ is bounded above.
By the Completeness Axiom of $\mathbb{R}$, $S$ has a supremum:
$$L = \sup S = \sup \{ a_n : n \in \mathbb{N} \} \in \mathbb{R}$$
We now prove that $\lim_{n \to \infty} a_n = L$.
Let $\epsilon > 0$ be given.
Since $L$ is the *least* upper bound of $S$, $L - \epsilon$ is not an upper bound of $S$.
Therefore, there exists some element $a_N \in S$ such that:
$$a_N > L - \epsilon$$
Since $(a_n)$ is monotonically increasing, for all $n \ge N$:
$$a_n \ge a_N > L - \epsilon$$
Furthermore, since $L$ is an upper bound of $S$, for all $n \in \mathbb{N}$:
$$a_n \le L < L + \epsilon$$
Combining both inequalities, for all $n \ge N$:
$$L - \epsilon < a_n < L + \epsilon \iff |a_n - L| < \epsilon$$
This precisely satisfies the $\epsilon$-$N$ definition of limit.
Therefore, $\lim_{n \to \infty} a_n = L = \sup \{a_n\}$.
The proof for a decreasing bounded sequence follows symmetrically by considering the infimum. $\blacksquare$"""
            },
            {
                "secNumber": "3.4",
                "title": "Subsequences, Limit Superior, Limit Inferior & Bolzano-Weierstrass",
                "content": r"""### 1. Subsequences

> **Definition 3.4 (Subsequence):**
> Let $(a_n)$ be a sequence. Let $(n_k)_{k=1}^\infty$ be a strictly increasing sequence of natural numbers:
> $$n_1 < n_2 < n_3 < \dots < n_k < n_{k+1} < \dots$$
> The sequence $(a_{n_k})_{k=1}^\infty$ is called a **subsequence** of $(a_n)$.
> Notice that $n_k \ge k$ for all $k \in \mathbb{N}$.

> **Theorem 3.7 (Convergence of Subsequences):**
> If a sequence $(a_n)$ converges to $L$, then every subsequence $(a_{n_k})$ also converges to $L$.

---

### 2. The Bolzano-Weierstrass Theorem for Sequences

> **Theorem 3.8 (Bolzano-Weierstrass Theorem for Sequences):**
> Every bounded sequence of real numbers has a convergent subsequence.

#### Rigorous Proof:
We present the classical proof using the **Peak Point Lemma** (Monotone Subsequence Theorem):

*Lemma (Peak Point Lemma):* Every sequence $(a_n)$ contains a monotone subsequence.
*Proof of Lemma:* We say that an index $m \in \mathbb{N}$ is a **peak** (or turn point) of the sequence $(a_n)$ if:
$$\forall n > m, \quad a_m \ge a_n$$
That is, $a_m$ is greater than or equal to all subsequent terms.
Now consider two mutually exclusive cases:
- **Case 1: There are infinitely many peaks.**
  Let the peaks be indexed as $m_1 < m_2 < m_3 < \dots < m_k < \dots$.
  By definition of a peak, since $m_{k+1} > m_k$, we have $a_{m_k} \ge a_{m_{k+1}}$.
  Thus, the subsequence $(a_{m_k})_{k=1}^\infty$ is monotonically decreasing!
- **Case 2: There are only finitely many peaks (or no peaks at all).**
  Then there exists an index $N_0 \in \mathbb{N}$ after which no peaks exist.
  Choose $n_1 > N_0$. Since $n_1$ is not a peak, there exists an index $n_2 > n_1$ such that $a_{n_1} < a_{n_2}$.
  Similarly, since $n_2 > N_0$, $n_2$ is not a peak, so there exists $n_3 > n_2$ such that $a_{n_2} < a_{n_3}$.
  Continuing inductively, we produce a strictly increasing sequence of indices $n_1 < n_2 < n_3 < \dots$ such that:
  $$a_{n_1} < a_{n_2} < a_{n_3} < \dots$$
  Thus, the subsequence $(a_{n_k})_{k=1}^\infty$ is strictly increasing!
In either case, $(a_n)$ contains a monotone subsequence $(a_{n_k})$. $\blacksquare$

Now, to complete the Bolzano-Weierstrass proof:
Let $(a_n)$ be a bounded sequence.
By the Peak Point Lemma, $(a_n)$ contains a monotone subsequence $(a_{n_k})$.
Since $(a_n)$ is bounded, the subsequence $(a_{n_k})$ is also bounded.
By the Monotone Convergence Theorem (Theorem 3.6), this bounded monotone subsequence must converge!
Therefore, $(a_n)$ has a convergent subsequence. $\blacksquare$

---

### 3. Limit Superior and Limit Inferior

For sequences that oscillate and do not converge (such as $a_n = (-1)^n$), the ordinary limit does not exist. However, every bounded sequence possesses a well-defined $\limsup$ and $\liminf$.

> **Definition 3.5 ($\limsup$ and $\liminf$):**
> Let $(a_n)$ be a bounded sequence of real numbers.
> For each $k \in \mathbb{N}$, define the tail bounds:
> $$u_k = \sup \{ a_n : n \ge k \} \quad \text{and} \quad v_k = \inf \{ a_n : n \ge k \}$$
> Notice that as $k$ increases, the set $\{a_n : n \ge k\}$ shrinks, so $(u_k)$ is monotonically decreasing and bounded below, while $(v_k)$ is monotonically increasing and bounded above.
> By MCT, both limits exist. We define:
> $$\limsup_{n \to \infty} a_n = \lim_{k \to \infty} u_k = \inf_{k \ge 1} \left( \sup_{n \ge k} a_n \right)$$
> $$\liminf_{n \to \infty} a_n = \lim_{k \to \infty} v_k = \sup_{k \ge 1} \left( \inf_{n \ge k} a_n \right)$$

> **Theorem 3.9 (Convergence Criterion via Limsup and Liminf):**
> A bounded sequence $(a_n)$ converges if and only if:
> $$\limsup_{n \to \infty} a_n = \liminf_{n \to \infty} a_n = L$$
> in which case $\lim_{n \to \infty} a_n = L$."""
            },
            {
                "secNumber": "3.5",
                "title": "Cauchy Sequences, Cauchy Criterion & The Completeness of R",
                "content": r"""### 1. Cauchy Sequences

In many applications, evaluating the limit $L$ of a sequence directly is impossible because $L$ is unknown. Augustin-Louis Cauchy introduced a revolutionary criterion: instead of testing how close terms get to an external limit $L$, test how close the terms get to *each other*!

> **Definition 3.6 (Cauchy Sequence):**
> A sequence $(a_n)$ is a **Cauchy sequence** if for every $\epsilon > 0$, there exists an index $N \in \mathbb{N}$ such that:
> $$\forall n, m \ge N, \quad |a_n - a_m| < \epsilon$$

---

### 2. Properties of Cauchy Sequences

> **Lemma 3.1 (Convergent Sequences are Cauchy):**
> If $\lim_{n \to \infty} a_n = L$, then $(a_n)$ is a Cauchy sequence.
> 
> *Proof:* Let $\epsilon > 0$. Since $a_n \to L$, choose $N$ such that $|a_k - L| < \frac{\epsilon}{2}$ for all $k \ge N$.
> For any $n, m \ge N$:
> $$|a_n - a_m| = |(a_n - L) - (a_m - L)| \le |a_n - L| + |a_m - L| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon \quad \blacksquare$$

> **Lemma 3.2 (Cauchy Sequences are Bounded):**
> Every Cauchy sequence is bounded.
> 
> *Proof:* Let $\epsilon = 1$. Choose $N$ such that $|a_n - a_m| < 1$ for all $n, m \ge N$.
> In particular, setting $m = N$: $|a_n - a_N| < 1 \implies |a_n| < |a_N| + 1$ for all $n \ge N$.
> Taking $M = \max\{|a_1|, |a_2|, \dots, |a_{N-1}|, |a_N| + 1\}$ bounds the sequence for all $n$. $\blacksquare$

---

### 3. The Cauchy Completeness Criterion

> **Theorem 3.10 (Cauchy Completeness of $\mathbb{R}$):**
> A sequence of real numbers $(a_n)$ converges in $\mathbb{R}$ if and only if it is a Cauchy sequence.

#### Complete Rigorous Proof:
$(\implies)$ Proved in Lemma 3.1.
$(\impliedby)$ Let $(a_n)$ be a Cauchy sequence in $\mathbb{R}$.
1. **Find a candidate limit $L$:**
   By Lemma 3.2, $(a_n)$ is bounded.
   By the Bolzano-Weierstrass Theorem (Theorem 3.8), $(a_n)$ contains a convergent subsequence $(a_{n_k})$.
   Let:
   $$\lim_{k \to \infty} a_{n_k} = L \in \mathbb{R}$$
2. **Prove that the entire sequence $(a_n)$ converges to $L$:**
   Let $\epsilon > 0$ be arbitrary.
   Since $(a_n)$ is Cauchy, choose $N_1 \in \mathbb{N}$ such that:
   $$\forall n, m \ge N_1, \quad |a_n - a_m| < \frac{\epsilon}{2}$$
   Since $a_{n_k} \to L$, choose $K \in \mathbb{N}$ such that:
   $$\forall k \ge K, \quad |a_{n_k} - L| < \frac{\epsilon}{2}$$
   Now pick an index $k \ge K$ large enough so that $n_k \ge N_1$ (which is always possible since $n_k \ge k$).
   Then for any index $n \ge N_1$, we set $m = n_k$:
   $$|a_n - L| = |(a_n - a_{n_k}) + (a_{n_k} - L)| \le |a_n - a_{n_k}| + |a_{n_k} - L|$$
   Since $n \ge N_1$ and $n_k \ge N_1$, $|a_n - a_{n_k}| < \frac{\epsilon}{2}$.
   And since $k \ge K$, $|a_{n_k} - L| < \frac{\epsilon}{2}$.
   Therefore:
   $$|a_n - L| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
   Since this holds for all $n \ge N_1$, we conclude that:
   $$\lim_{n \to \infty} a_n = L$$
Thus, every Cauchy sequence in $\mathbb{R}$ converges. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 3.1",
                "title": "Rigorous Epsilon-N Verification of Rational Rational Sequence Limits",
                "statement": r"""Prove directly from the $\epsilon$-$N$ definition that the sequence:
$$a_n = \frac{3n^2 - 4}{2n^2 + 5n + 1}$$
converges to $L = \frac{3}{2}$.
Provide an explicit construction of the index $N(\epsilon)$ for any given $\epsilon > 0$.""",
                "hints": [
                    "Compute the algebraic difference |a_n - 3/2| and find a common denominator.",
                    "Bound the numerator by a linear multiple of n and the denominator from below."
                ],
                "solution": r"""### 1. Algebraic Difference Computation
We evaluate $|a_n - L|$:
$$\begin{aligned}
\left| \frac{3n^2 - 4}{2n^2 + 5n + 1} - \frac{3}{2} \right| &= \left| \frac{2(3n^2 - 4) - 3(2n^2 + 5n + 1)}{2(2n^2 + 5n + 1)} \right| \\
&= \left| \frac{6n^2 - 8 - 6n^2 - 15n - 3}{2(2n^2 + 5n + 1)} \right| \\
&= \left| \frac{-15n - 11}{4n^2 + 10n + 2} \right| = \frac{15n + 11}{4n^2 + 10n + 2}
\end{aligned}$$

---

### 2. Establishing Upper Bounds
For all $n \ge 1$:
- In the numerator: $11 \le 11n$, so $15n + 11 \le 15n + 11n = 26n$.
- In the denominator: since $10n + 2 > 0$, we have $4n^2 + 10n + 2 > 4n^2$.
Therefore:
$$\frac{15n + 11}{4n^2 + 10n + 2} < \frac{26n}{4n^2} = \frac{13}{2n}$$

---

### 3. Explicit Construction of $N(\epsilon)$
Let $\epsilon > 0$ be arbitrary. We desire:
$$\frac{13}{2n} < \epsilon \iff 2n > \frac{13}{\epsilon} \iff n > \frac{13}{2\epsilon}$$
By the Archimedean property, choose:
$$N = \left\lceil \frac{13}{2\epsilon} \right\rceil + 1$$
Then for all $n \ge N$:
$$\left| a_n - \frac{3}{2} \right| < \frac{13}{2n} \le \frac{13}{2N} < \epsilon$$
This completes the formal $\epsilon$-$N$ proof that $\lim_{n \to \infty} a_n = \frac{3}{2}$. $\blacksquare$"""
            },
            {
                "tier": "Advanced / Problem 3.2",
                "title": "Non-Linear Recursive Sequence Convergence via the Monotone Convergence Theorem",
                "statement": r"""Consider the recursively defined real sequence:
$$x_1 = 1, \quad x_{n+1} = \sqrt{2 + x_n} \quad \text{for } n \ge 1$$
1. Prove by mathematical induction that $x_n < 2$ for all $n \in \mathbb{N}$ (boundedness above).
2. Prove by mathematical induction that $x_n < x_{n+1}$ for all $n \in \mathbb{N}$ (monotonically increasing).
3. Conclude by the Monotone Convergence Theorem that $(x_n)$ converges, and determine its exact limit $L$.""",
                "hints": [
                    "Base case: x_1 = 1 < 2.",
                    "If x_k < 2, then x_{k+1} = sqrt(2 + x_k) < sqrt(2 + 2) = 2.",
                    "Take the limit on both sides of the recurrence relation x_{n+1} = sqrt(2 + x_n)."
                ],
                "solution": r"""### 1. Proof of Boundedness Above: $x_n < 2$ for all $n \ge 1$
We proceed by mathematical induction.
- **Base Step ($n = 1$):** $x_1 = 1 < 2$. The base statement holds.
- **Inductive Step:** Assume the inductive hypothesis $x_k < 2$ for some $k \ge 1$.
  Then:
  $$2 + x_k < 2 + 2 = 4$$
  Since the square root function is strictly increasing on $[0, \infty)$:
  $$x_{k+1} = \sqrt{2 + x_k} < \sqrt{4} = 2$$
  The inductive step is verified.
Therefore, by the principle of mathematical induction, $x_n < 2$ for all $n \in \mathbb{N}$.

---

### 2. Proof of Monotonicity: $x_n < x_{n+1}$ for all $n \ge 1$
We again use mathematical induction.
- **Base Step ($n = 1$):**
  $$x_1 = 1, \quad x_2 = \sqrt{2 + 1} = \sqrt{3} \approx 1.732$$
  Clearly $x_1 < x_2$.
- **Inductive Step:** Assume $x_k < x_{k+1}$ for some $k \ge 1$.
  Adding 2 to both sides:
  $$2 + x_k < 2 + x_{k+1}$$
  Taking square roots:
  $$\sqrt{2 + x_k} < \sqrt{2 + x_{k+1}} \iff x_{k+1} < x_{k+2}$$
  The inductive step holds.
Therefore, $(x_n)$ is strictly increasing for all $n \in \mathbb{N}$.

---

### 3. Application of MCT and Limit Determination
Since $(x_n)$ is monotonically increasing and bounded above by 2, by the Monotone Convergence Theorem (Theorem 3.6), the sequence converges to some real number:
$$L = \lim_{n \to \infty} x_n = \sup \{ x_n : n \in \mathbb{N} \}$$
Since $x_n \ge 1$ for all $n$, we have $1 \le L \le 2$.
Taking the limit as $n \to \infty$ on both sides of $x_{n+1} = \sqrt{2 + x_n}$:
$$L = \lim_{n \to \infty} x_{n+1} = \lim_{n \to \infty} \sqrt{2 + x_n} = \sqrt{2 + \lim_{n \to \infty} x_n} = \sqrt{2 + L}$$
Squaring both sides:
$$L^2 = 2 + L \iff L^2 - L - 2 = 0 \iff (L - 2)(L + 1) = 0$$
This yields two algebraic roots: $L = 2$ and $L = -1$.
Since $x_n \ge 1$ for all $n$, the order limit theorem requires $L \ge 1$.
Hence, $L = -1$ is extraneous.
We conclude definitively that:
$$\lim_{n \to \infty} x_n = 2 \quad \blacksquare$$"""
            },
            {
                "tier": "Honors / Problem 3.3",
                "title": "Comprehensive Equivalence Proof: Cauchy Criterion & Completeness of R",
                "statement": r"""A metric space $(X, d)$ is said to be Cauchy-complete if every Cauchy sequence in $X$ converges to a point in $X$.
1. Prove that if every bounded monotone sequence in an ordered field $F$ converges (Monotone Completeness), then every Cauchy sequence in $F$ converges (Cauchy Completeness).
2. Conversely, prove that if an ordered field $F$ is Cauchy-complete and Archimedean, then it satisfies the Least Upper Bound Property (Dedekind Completeness).
3. Conclude the complete equivalence of the three formulations of real completeness.""",
                "hints": [
                    "For Part 1: Cauchy implies bounded. Peak Point Lemma gives monotone subsequence. Monotone Completeness ensures subsequence converges. Cauchy ensures whole sequence converges.",
                    "For Part 2: Given a non-empty set S bounded above, construct a sequence of bisection intervals [a_n, b_n] where a_n in S and b_n is an upper bound."
                ],
                "solution": r"""### 1. Proof that Monotone Completeness Implies Cauchy Completeness

Assume every bounded monotone sequence in $F$ converges.
Let $(x_n)$ be a Cauchy sequence in $F$.
- **Step 1: $(x_n)$ is bounded.**
  Setting $\epsilon = 1$, there exists $N_1$ such that $|x_n - x_{N_1}| < 1$ for all $n \ge N_1$.
  Thus $|x_n| \le \max\{|x_1|, \dots, |x_{N_1-1}|, |x_{N_1}| + 1\} = M$.
- **Step 2: Existence of a monotone subsequence.**
  By the Peak Point Lemma (proven in Section 3.4), any sequence in an ordered field contains a monotone subsequence $(x_{n_k})$.
- **Step 3: Convergence of the subsequence.**
  The subsequence $(x_{n_k})$ is monotone and bounded by $M$.
  By our hypothesis (Monotone Completeness), $(x_{n_k})$ converges to some $L \in F$.
- **Step 4: Convergence of the full Cauchy sequence.**
  Let $\epsilon > 0$. Since $(x_n)$ is Cauchy, choose $N_2$ such that $|x_n - x_m| < \epsilon/2$ for all $n, m \ge N_2$.
  Since $x_{n_k} \to L$, choose $K$ such that $|x_{n_k} - L| < \epsilon/2$ for all $k \ge K$.
  Pick $k \ge K$ with $n_k \ge N_2$. For any $n \ge N_2$:
  $$|x_n - L| \le |x_n - x_{n_k}| + |x_{n_k} - L| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
  Hence $x_n \to L$. Thus $F$ is Cauchy complete. $\blacksquare$

---

### 2. Proof that Cauchy-Complete + Archimedean Implies Least Upper Bound Property

Let $S \subset F$ be non-empty and bounded above by $M \in F$.
Choose $s_0 \in S$ and let $b_0 = M$. Since $b_0$ is an upper bound and $s_0 \in S$, $s_0 \le b_0$.
If $s_0 = b_0$, then $\sup S = s_0$ and we are done. Assume $s_0 < b_0$.
Let $a_0 = s_0$. We define intervals $[a_n, b_n]$ inductively:
At step $n$, let $m_n = \frac{a_n + b_n}{2}$ be the midpoint.
- If $m_n$ is an upper bound for $S$, set $a_{n+1} = a_n$ and $b_{n+1} = m_n$.
- If $m_n$ is not an upper bound for $S$ (meaning there is some $s \in S$ with $s > m_n$), set $a_{n+1} = s$ and $b_{n+1} = b_n$.

By construction:
1. $a_0 \le a_1 \le a_2 \le \dots \le b_2 \le b_1 \le b_0$.
2. For each $n$, there is an element of $S$ greater than or equal to $a_n$, and $b_n$ is an upper bound of $S$.
3. The interval length satisfies:
   $$b_n - a_n \le \frac{b_0 - a_0}{2^n}$$
Since $F$ is Archimedean, for any $\epsilon > 0$, there exists $N$ such that $\frac{b_0 - a_0}{2^N} < \epsilon$.
For any $n, m \ge N$:
$$|b_n - b_m| \le b_N - a_N < \epsilon$$
Thus $(b_n)$ is a Cauchy sequence in $F$!
Since $F$ is Cauchy-complete, $(b_n)$ converges to some limit $L = \lim_{n \to \infty} b_n \in F$.
Similarly, since $b_n - a_n \to 0$, $a_n \to L$.

Now we verify that $L = \sup S$:
- **$L$ is an upper bound:** Let $x \in S$. Since each $b_n$ is an upper bound of $S$, $x \le b_n$ for all $n$.
  Taking limits gives $x \le L$.
- **$L$ is the least upper bound:** Let $\epsilon > 0$.
  Since $a_n \to L$, choose $n$ such that $a_n > L - \epsilon$.
  By construction, there exists $s \in S$ with $s \ge a_n > L - \epsilon$.
  Thus no number less than $L$ can be an upper bound.
Therefore, $L = \sup S$. $\blacksquare$

---

### 3. Conclusion of Triple Equivalence
We have established the cycle of implications:
$$\text{Least Upper Bound Property} \implies \text{Monotone Completeness} \implies \text{Cauchy Completeness} \implies \text{Least Upper Bound Property}$$
All three formulations of completeness are mathematically equivalent for Archimedean ordered fields. $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u = get_unit3()
    print(f"Loaded Unit 3: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
