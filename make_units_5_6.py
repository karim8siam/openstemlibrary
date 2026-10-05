import json

# Unit 5: Summation of Algebraic & Trigonometric Series
u5 = {
  "unit_id": "unit_5",
  "unit_title": "Summation of Algebraic & Trigonometric Series",
  "unit_subtitle": "Mathematical Induction, Telescoping Differences, AGP Closed Forms, Partial Fractions & C + iS Phasors",
  "sections": [
    {
      "id": "sec_5_1",
      "title": "Mathematical Induction & Polynomial Power Sums",
      "content": r"""
<h3>1. The Axiom of Mathematical Induction</h3>
<p>
The Principle of Mathematical Induction is fundamentally equivalent to the Well-Ordering Principle of the natural numbers $\mathbb{N}$:
<ul>
  <li><strong>Weak Induction:</strong> If a proposition $P(n)$ is true for $n = 1$, and for every $k \ge 1$ the truth of $P(k)$ implies $P(k+1)$, then $P(n)$ is true for all $n \in \mathbb{N}$.</li>
  <li><strong>Strong Induction:</strong> If $P(1)$ is true, and the truth of $P(1), P(2), \dots, P(k)$ collectively implies $P(k+1)$, then $P(n)$ is true for all $n \in \mathbb{N}$.</li>
</ul>
</p>

<h3>2. Canonical Power Sum Identities</h3>
<p>
Inductive proofs establish the classic closed forms for integer power sums:
<div class="math-display">
$$\mathbf{S_1(n) = \sum_{k=1}^n k = \frac{n(n+1)}{2}}$$
$$\mathbf{S_2(n) = \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}}$$
$$\mathbf{S_3(n) = \sum_{k=1}^n k^3 = \left[\frac{n(n+1)}{2}\right]^2 = [S_1(n)]^2}$$
</div>
The remarkable identity $S_3(n) = [S_1(n)]^2$ (Nicomachus's Theorem) states that the sum of the first $n$ cubes equals the square of the sum of the first $n$ integers.
</p>
"""
    },
    {
      "id": "sec_5_2",
      "title": "Finite Differences & The Telescoping Sum Method",
      "content": r"""
<h3>1. The Difference Operator $\Delta$</h3>
<p>
For a sequence $f(n)$, the forward difference operator is defined by:
$$\mathbf{\Delta f(n) \equiv f(n+1) - f(n)}$$
The Fundamental Theorem of Summation Calculus states that the sum of differences telescopes:
$$\mathbf{\sum_{k=1}^n \Delta f(k) = \sum_{k=1}^n [f(k+1) - f(k)] = f(n+1) - f(1)}$$
All intermediate terms cancel pairwise, leaving only the boundary evaluations!
</p>

<h3>2. Factorial Polynomials</h3>
<p>
We define the falling factorial polynomial of degree $r$:
$$n^{(r)} \equiv n(n-1)(n-2)\cdots(n-r+1)$$
Its forward difference mirrors standard polynomial differentiation:
$$\Delta [n^{(r)}] = (n+1)^{(r)} - n^{(r)} = r \, n^{(r-1)}$$
Thus, summation follows the discrete power rule:
$$\mathbf{\sum_{k=1}^n k^{(r)} = \frac{(n+1)^{(r+1)} - 1^{(r+1)}}{r + 1} = \frac{(n+1)^{(r+1)}}{r + 1}}$$
Any polynomial can be converted to factorial powers via Stirling numbers of the second kind, rendering summation algorithmic!
</p>
"""
    },
    {
      "id": "sec_5_3",
      "title": "Arithmetico-Geometric Progressions (AGP)",
      "content": r"""
<h3>1. Definition of an AGP</h3>
<p>
An <strong>Arithmetico-Geometric Progression</strong> is a sequence whose $k$-th term is the product of corresponding terms of an Arithmetic Progression ($a, a+d, a+2d, \dots$) and a Geometric Progression ($1, r, r^2, \dots$):
$$\mathbf{u_k = [a + (k-1)d] r^{k-1}}$$
The finite sum to $n$ terms is:
$$S_n = a + (a + d)r + (a + 2d)r^2 + \dots + [a + (n-1)d]r^{n-1}$$
</p>

<h3>2. Closed-Form Derivation</h3>
<p>
Multiply $S_n$ by the common ratio $r$:
$$r S_n = ar + (a + d)r^2 + \dots + [a + (n-2)d]r^{n-1} + [a + (n-1)d]r^n$$
Subtracting this equation from $S_n$:
$$(1 - r)S_n = a + d[r + r^2 + \dots + r^{n-1}] - [a + (n-1)d]r^n$$
The bracketed terms form a standard finite geometric series with sum $\frac{r(1 - r^{n-1})}{1 - r}$:
$$(1 - r)S_n = a + \frac{dr(1 - r^{n-1})}{1 - r} - [a + (n-1)d]r^n$$
Dividing by $(1 - r)$ yields the exact closed form:
$$\mathbf{S_n = \frac{a}{1 - r} + \frac{dr(1 - r^{n-1})}{(1 - r)^2} - \frac{[a + (n-1)d]r^n}{1 - r}}$$
</p>

<h3>3. Sum to Infinity</h3>
<p>
For $|r| < 1$, as $n \to \infty$, $r^n \to 0$ and $n r^n \to 0$. The infinite sum simplifies to:
$$\mathbf{S_\infty = \frac{a}{1 - r} + \frac{dr}{(1 - r)^2}}$$
</p>
"""
    },
    {
      "id": "sec_5_4",
      "title": "Summation of Series by Partial Fraction Decomposition",
      "content": r"""
<h3>1. The Method of Partial Fractions for Series</h3>
<p>
When terms of an infinite series are reciprocal products of linear factors, we decompose each term $u_k$ into partial fractions to induce telescoping cancellation:
$$u_k = \frac{1}{(k + a)(k + b)} = \frac{1}{b - a} \left[ \frac{1}{k + a} - \frac{1}{k + b} \right]$$
Summing from $k = 1$ to $n$:
$$S_n = \frac{1}{b - a} \sum_{k=1}^n \left( \frac{1}{k + a} - \frac{1}{k + b} \right)$$
Depending on the shift $b - a$, intermediate terms cancel, leaving a finite number of uncancelled boundary fractions.
</p>

<h3>2. Higher-Order Factor Decompositions</h3>
<p>
For three factors in arithmetic progression:
$$u_k = \frac{1}{(a k + b)(a(k+1) + b)(a(k+2) + b)} = \frac{1}{2a} \left[ \frac{1}{(ak+b)(a(k+1)+b)} - \frac{1}{(a(k+1)+b)(a(k+2)+b)} \right]$$
Defining $v_k = \frac{1}{(ak+b)(a(k+1)+b)}$, we observe that $u_k = \frac{1}{2a}[v_k - v_{k+1}]$.
The sum to $n$ terms telescopes directly:
$$\sum_{k=1}^n u_k = \frac{1}{2a}[v_1 - v_{n+1}]$$
and as $n \to \infty$, $v_{n+1} \to 0$, giving the exact limit $S_\infty = \frac{v_1}{2a}$!
</p>
"""
    },
    {
      "id": "sec_5_5",
      "title": "Summation of Trigonometric Series via the $C + iS$ Method",
      "content": r"""
<h3>1. The Complex Phasor Coupling Technique</h3>
<p>
To sum a cosine series $C = \sum_{k=0}^{n-1} a_k \cos(\theta_k)$ and sine series $S = \sum_{k=0}^{n-1} a_k \sin(\theta_k)$, we form the complex linear combination:
$$\mathbf{C + iS = \sum_{k=0}^{n-1} a_k [\cos(\theta_k) + i\sin(\theta_k)] = \sum_{k=0}^{n-1} a_k e^{i\theta_k}}$$
This converts trigonometric sums into geometric or binomial series in the complex domain! After evaluating $C + iS$ in closed form, equating real parts recovers $C$, and equating imaginary parts recovers $S$.
</p>

<h3>2. Sum of Sines and Cosines in Arithmetic Progression</h3>
<p>
Let $\theta_k = \alpha + k\beta$:
$$C + iS = \sum_{k=0}^{n-1} e^{i(\alpha + k\beta)} = e^{i\alpha} \sum_{k=0}^{n-1} (e^{i\beta})^k = e^{i\alpha} \frac{1 - e^{in\beta}}{1 - e^{i\beta}}$$
Factoring out half-angles:
$$1 - e^{in\beta} = -e^{in\beta/2}(e^{in\beta/2} - e^{-in\beta/2}) = -2i e^{in\beta/2}\sin(n\beta/2)$$
$$1 - e^{i\beta} = -2i e^{i\beta/2}\sin(\beta/2)$$
Dividing:
$$C + iS = e^{i\alpha} \frac{-2i e^{in\beta/2}\sin(n\beta/2)}{-2i e^{i\beta/2}\sin(\beta/2)} = \frac{\sin(n\beta/2)}{\sin(\beta/2)} e^{i\left(\alpha + \frac{n-1}{2}\beta\right)}$$
Equating real and imaginary parts gives the famous closed forms:
<div class="math-display">
$$\mathbf{C = \sum_{k=0}^{n-1} \cos(\alpha + k\beta) = \frac{\sin(n\beta/2)}{\sin(\beta/2)} \cos\left(\alpha + \frac{n-1}{2}\beta\right)}$$
$$\mathbf{S = \sum_{k=0}^{n-1} \sin(\alpha + k\beta) = \frac{\sin(n\beta/2)}{\sin(\beta/2)} \sin\left(\alpha + \frac{n-1}{2}\beta\right)}$$
</div>
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-series-cis-phasor-sim",
    "title": "Interactive C + iS Complex Phasor & Trigonometric Sum Visualizer",
    "description": "Visualize trigonometric summation by chaining complex phasors exp(i(α + kβ)) in the Argand plane. Adjust angle parameters and term count n to see the polygon of chords close onto circular arcs, verifying the closed form."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 5.1: Finite Arithmetico-Geometric Series Evaluation",
      "statement": r"Evaluate the sum of the first $n$ terms of the arithmetico-geometric series $S_n = 1\cdot 2 + 2\cdot 2^2 + 3\cdot 2^3 + \dots + n\cdot 2^n$.",
      "steps": [
        {
          "step": "Step 1: Identify Parameters and Multiply by Common Ratio",
          "math": r"a = 1, \quad d = 1, \quad r = 2 \\ S_n = 1\cdot 2^1 + 2\cdot 2^2 + 3\cdot 2^3 + \dots + n\cdot 2^n \\ 2 S_n = 1\cdot 2^2 + 2\cdot 2^3 + \dots + (n-1)\cdot 2^n + n\cdot 2^{n+1}",
          "explanation": "Shift by the common ratio $r = 2$."
        },
        {
          "step": "Step 2: Subtract the Shifted Series",
          "math": r"S_n - 2S_n = 2^1 + (2^2 + 2^3 + \dots + 2^n) - n\cdot 2^{n+1} \\ -S_n = \sum_{k=1}^n 2^k - n\cdot 2^{n+1}",
          "explanation": "Subtracting aligns terms with unit differences."
        },
        {
          "step": "Step 3: Evaluate the Geometric Sum and Solve for Sₙ",
          "math": r"\sum_{k=1}^n 2^k = \frac{2(2^n - 1)}{2 - 1} = 2^{n+1} - 2 \\ -S_n = (2^{n+1} - 2) - n\cdot 2^{n+1} = (1 - n)2^{n+1} - 2 \\ S_n = (n - 1)2^{n+1} + 2",
          "explanation": "Multiply by $-1$ to isolate $S_n$."
        }
      ],
      "answer": r"\mathbf{S_n = (n - 1)2^{n+1} + 2}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 5.2: Telescoping Partial Fraction Infinite Series",
      "statement": r"Find the sum to $n$ terms and the infinite sum of the series $S = \sum_{k=1}^\infty \frac{1}{(2k-1)(2k+1)(2k+3)}$.",
      "steps": [
        {
          "step": "Step 1: Decompose the General Term into Partial Differences",
          "math": r"u_k = \frac{1}{(2k-1)(2k+1)(2k+3)} \\ \text{Difference between outer factors: } (2k+3) - (2k-1) = 4 \\ u_k = \frac{1}{4} \left[ \frac{(2k+3) - (2k-1)}{(2k-1)(2k+1)(2k+3)} \right] = \frac{1}{4} \left[ \frac{1}{(2k-1)(2k+1)} - \frac{1}{(2k+1)(2k+3)} \right]",
          "explanation": "Split the three-factor denominator into differences of two-factor denominators."
        },
        {
          "step": "Step 2: Form the Telescoping Sum",
          "math": r"v_k = \frac{1}{(2k-1)(2k+1)} \implies u_k = \frac{1}{4}[v_k - v_{k+1}] \\ S_n = \sum_{k=1}^n u_k = \frac{1}{4}[v_1 - v_{n+1}] = \frac{1}{4}\left[ \frac{1}{1\cdot 3} - \frac{1}{(2n+1)(2n+3)} \right] = \frac{1}{12} - \frac{1}{4(2n+1)(2n+3)}",
          "explanation": "All interior terms cancel out pairwise."
        },
        {
          "step": "Step 3: Evaluate the Infinite Limit",
          "math": r"S_\infty = \lim_{n \to \infty} S_n = \frac{1}{12} - 0 = \frac{1}{12}",
          "explanation": "The terminal boundary term approaches zero as $n \\to \\infty$."
        }
      ],
      "answer": r"\mathbf{S_n = \frac{1}{12} - \frac{1}{4(2n+1)(2n+3)}}, \qquad \mathbf{S_\infty = \frac{1}{12}}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 5.3: Binomial Trigonometric Sums via the C + iS Method",
      "statement": r"Use the complex $C + iS$ method to evaluate $C = \sum_{k=0}^n \binom{n}{k} \cos(k\theta)$ and $S = \sum_{k=0}^n \binom{n}{k} \sin(k\theta)$, and prove that $C = 2^n \cos^n(\theta/2) \cos(n\theta/2)$.",
      "steps": [
        {
          "step": "Step 1: Set Up the Complex Linear Combination C + iS",
          "math": r"C + iS = \sum_{k=0}^n \binom{n}{k} [\cos(k\theta) + i\sin(k\theta)] = \sum_{k=0}^n \binom{n}{k} (e^{i\theta})^k",
          "explanation": "Combine the real cosine and imaginary sine sums."
        },
        {
          "step": "Step 2: Apply the Binomial Theorem",
          "math": r"C + iS = (1 + e^{i\theta})^n",
          "explanation": "The sum matches the binomial expansion of $(1 + z)^n$ where $z = e^{i\\theta}$."
        },
        {
          "step": "Step 3: Factor Half-Angles and Apply Euler's Formula",
          "math": r"1 + e^{i\theta} = e^{i\theta/2}(e^{-i\theta/2} + e^{i\theta/2}) = e^{i\theta/2}[2\cos(\theta/2)] = 2\cos(\theta/2) e^{i\theta/2} \\ (1 + e^{i\theta})^n = [2\cos(\theta/2) e^{i\theta/2}]^n = 2^n \cos^n(\theta/2) e^{i n\theta/2} \\ = 2^n \cos^n(\theta/2) [\cos(n\theta/2) + i\sin(n\theta/2)]",
          "explanation": "Factor $e^{i\\theta/2}$ from the base to convert to polar form."
        },
        {
          "step": "Step 4: Equate Real and Imaginary Parts",
          "math": r"C = 2^n \cos^n(\theta/2) \cos(n\theta/2) \quad \blacksquare \\ S = 2^n \cos^n(\theta/2) \sin(n\theta/2)",
          "explanation": "Real part yields $C$, and imaginary part yields $S$."
        }
      ],
      "answer": r"\mathbf{C = 2^n \cos^n(\theta/2) \cos(n\theta/2)}, \qquad \mathbf{S = 2^n \cos^n(\theta/2) \sin(n\theta/2)}."
    }
  ]
}

# Unit 6: Matrix Algebra & Determinants
u6 = {
  "unit_id": "unit_6",
  "unit_title": "Matrix Algebra & Determinants",
  "unit_subtitle": "Matrix Rings, Special Matrix Classes, Multilinear Determinants, Cauchy-Binet Multiplicativity & Adjugate Inverses",
  "sections": [
    {
      "id": "sec_6_1",
      "title": "Algebra of Matrices: Rings, Transposition & Trace",
      "content": r"""
<h3>1. The Matrix Ring</h3>
<p>
The collection of $m \times n$ matrices with entries in a field $\mathbb{F}$ ($\mathbb{R}$ or $\mathbb{C}$), denoted $M_{m \times n}(\mathbb{F})$, forms a vector space under entrywise addition and scalar multiplication.<br>
For $A \in M_{m \times p}(\mathbb{F})$ and $B \in M_{p \times n}(\mathbb{F})$, their <strong>matrix product</strong> $C = AB \in M_{m \times n}(\mathbb{F})$ has entries:
$$\mathbf{c_{ij} = \sum_{k=1}^p a_{ik} b_{kj}}$$
The product is associative ($A(BC) = (AB)C$) and distributes over addition, but is strictly non-commutative ($AB \ne BA$ in general). The square matrices $M_n(\mathbb{F})$ form a non-commutative ring with identity $I_n$.
</p>

<h3>2. The Transpose & Conjugate Transpose</h3>
<p>
The <strong>transpose</strong> $A^T$ of $A = [a_{ij}]$ is defined by $(A^T)_{ij} = a_{ji}$. Key properties:
$$(A + B)^T = A^T + B^T, \quad (cA)^T = c A^T, \quad (A^T)^T = A, \quad \mathbf{(AB)^T = B^T A^T}$$
For complex matrices, the <strong>Hermitian adjoint</strong> (conjugate transpose) is $A^\dagger \equiv (\bar{A})^T$, satisfying $(AB)^\dagger = B^\dagger A^\dagger$.
</p>

<h3>3. The Trace Function</h3>
<p>
For a square matrix $A \in M_n(\mathbb{F})$, the <strong>trace</strong> is the sum of its diagonal elements:
$$\mathbf{\text{tr}(A) \equiv \sum_{i=1}^n a_{ii}}$$
<strong>Cyclic Invariance Theorem:</strong> For any $A \in M_{m \times n}$ and $B \in M_{n \times m}$:
$$\mathbf{\text{tr}(AB) = \text{tr}(BA)}$$
<em>Proof:</em> $\text{tr}(AB) = \sum_{i=1}^m (AB)_{ii} = \sum_{i=1}^m \sum_{j=1}^n a_{ij} b_{ji} = \sum_{j=1}^n \sum_{i=1}^m b_{ji} a_{ij} = \sum_{j=1}^n (BA)_{jj} = \text{tr}(BA)$. $\blacksquare$
</p>
"""
    },
    {
      "id": "sec_6_2",
      "title": "Taxonomy of Special Classes of Matrices",
      "content": r"""
<h3>1. Real Special Matrices</h3>
<p>
Let $A \in M_n(\mathbb{R})$:
<ul>
  <li><strong>Symmetric:</strong> $A^T = A \iff a_{ij} = a_{ji}$.</li>
  <li><strong>Skew-Symmetric:</strong> $A^T = -A \iff a_{ij} = -a_{ji}$ (diagonal entries must be zero: $a_{ii} = 0$).</li>
  <li><strong>Orthogonal:</strong> $A^T A = A A^T = I \iff A^{-1} = A^T$. Rows (and columns) form an orthonormal basis of $\mathbb{R}^n$. Orthogonal transformations preserve Euclidean lengths and angles: $\|Ax\| = \|x\|$.</li>
</ul>
</p>

<h3>2. Complex Special Matrices</h3>
<p>
Let $A \in M_n(\mathbb{C})$:
<ul>
  <li><strong>Hermitian:</strong> $A^\dagger = A \iff a_{ij} = \bar{a}_{ji}$ (diagonal entries must be purely real: $a_{ii} \in \mathbb{R}$).</li>
  <li><strong>Skew-Hermitian:</strong> $A^\dagger = -A \iff a_{ij} = -\bar{a}_{ji}$ (diagonal entries must be purely imaginary).</li>
  <li><strong>Unitary:</strong> $A^\dagger A = I \iff A^{-1} = A^\dagger$. Unitary matrices preserve the complex inner product: $\langle Ux, Uy \rangle = \langle x, y \rangle$.</li>
</ul>
</p>

<h3>3. Algebraic Operational Classes</h3>
<p>
<ul>
  <li><strong>Idempotent:</strong> $A^2 = A$ (represents projection operators).</li>
  <li><strong>Nilpotent:</strong> $A^k = 0$ for some integer $k \ge 1$ (the smallest such $k$ is the index of nilpotency).</li>
  <li><strong>Involutory:</strong> $A^2 = I \iff A^{-1} = A$ (represents reflection operators).</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_6_3",
      "title": "Axiomatic Characterization & Laplace Expansion of Determinants",
      "content": r"""
<h3>1. Axiomatic Definition of the Determinant</h3>
<p>
The <strong>determinant</strong> is the unique function $\det: M_n(\mathbb{F}) \to \mathbb{F}$ satisfying three fundamental axioms:
<ol>
  <li><strong>Multilinearity:</strong> $\det$ is a linear function of each row when all other rows are held fixed.</li>
  <li><strong>Alternating Property:</strong> Swapping any two rows negates the determinant: $\det(R_1, \dots, R_i, \dots, R_j, \dots, R_n) = -\det(R_1, \dots, R_j, \dots, R_i, \dots, R_n)$. Consequently, if two rows are identical, $\det A = 0$.</li>
  <li><strong>Normalization:</strong> $\det(I_n) = 1$.</li>
</ol>
</p>

<h3>2. The Leibniz Permutation Formula</h3>
<p>
From the axioms, the explicit determinant formula is:
$$\mathbf{\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}}$$
where the sum ranges over all $n!$ permutations $\sigma$ of the symmetric group $S_n$, and $\text{sgn}(\sigma) \in \{+1, -1\}$ is the permutation parity.
</p>

<h3>3. Laplace's Cofactor Expansion Theorem</h3>
<p>
The $(i, j)$-th <strong>minor</strong> $M_{ij}$ is the determinant of the $(n-1) \times (n-1)$ submatrix formed by deleting row $i$ and column $j$. The $(i, j)$-th <strong>cofactor</strong> is:
$$C_{ij} \equiv (-1)^{i+j} M_{ij}$$
<strong>Theorem (Laplace):</strong> The determinant can be evaluated by expanding along any arbitrary row $i$ or column $j$:
$$\mathbf{\det(A) = \sum_{j=1}^n a_{ij} C_{ij} \quad (\text{Expansion along row } i)}$$
$$\mathbf{\det(A) = \sum_{i=1}^n a_{ij} C_{ij} \quad (\text{Expansion along column } j)}$$
</p>
"""
    },
    {
      "id": "sec_6_4",
      "title": "Fundamental Determinant Properties & Multiplicativity",
      "content": r"""
<h3>1. Invariance and Operational Properties</h3>
<p>
<ul>
  <li><strong>Transpose Invariance:</strong> $\det(A^T) = \det(A)$. Row operations and column operations have identical effects on determinants!</li>
  <li><strong>Triangular Matrices:</strong> If $A$ is upper-triangular, lower-triangular, or diagonal, its determinant is simply the product of its diagonal entries:
  $$\det(A) = a_{11} a_{22} \cdots a_{nn}$$</li>
  <li><strong>Type III Row Operations:</strong> Adding a scalar multiple of one row to another preserves the determinant strictly unchanged: $\det(A) = \det(E A)$ where $\det(E) = 1$.</li>
  <li><strong>Scalar Multiplication:</strong> For an $n \times n$ matrix, $\det(c A) = c^n \det(A)$.</li>
</ul>
</p>

<h3>2. The Multiplicative Theorem</h3>
<p>
<strong>Theorem (Cauchy–Binet):</strong> For any two $n \times n$ matrices $A$ and $B$:
$$\mathbf{\det(AB) = \det(A) \det(B)}$$
<em>Immediate Corollaries:</em>
<ul>
  <li>A matrix $A$ is invertible if and only if $\det(A) \ne 0$.</li>
  <li>If $A$ is invertible: $\det(A^{-1}) = \frac{1}{\det(A)}$.</li>
  <li>If $A$ and $B$ are similar ($B = P^{-1} A P$): $\det(B) = \det(P^{-1})\det(A)\det(P) = \det(A)$.</li>
  <li>If $Q$ is orthogonal: $Q^T Q = I \implies [\det(Q)]^2 = 1 \implies \det(Q) = \pm 1$.</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_6_5",
      "title": "The Classical Adjugate Matrix, Matrix Inversion & Cramer's Rule",
      "content": r"""
<h3>1. The Classical Adjugate (Adjoint)</h3>
<p>
The <strong>adjugate</strong> $\text{adj}(A)$ of an $n \times n$ matrix $A$ is the transpose of its cofactor matrix $C = [C_{ij}]$:
$$\mathbf{\text{adj}(A) \equiv C^T \implies [\text{adj}(A)]_{ij} = C_{ji} = (-1)^{i+j} M_{ji}}$$
</p>

<h3>2. The Fundamental Inversion Theorem</h3>
<p>
<strong>Theorem:</strong> For any $n \times n$ matrix $A$:
$$\mathbf{A \cdot \text{adj}(A) = \text{adj}(A) \cdot A = (\det A) I_n}$$
<em>Proof:</em> The $(i, k)$-th entry of $A \cdot \text{adj}(A)$ is $\sum_{j=1}^n a_{ij} [\text{adj}(A)]_{jk} = \sum_{j=1}^n a_{ij} C_{kj}$.
If $i = k$, this is the Laplace expansion of $\det(A)$ along row $i$.
If $i \ne k$, this represents the expansion of a matrix with two identical rows ($i$ and $k$), which vanishes identically (alien cofactors). Thus $[A \cdot \text{adj}(A)]_{ik} = \delta_{ik} \det(A)$. $\blacksquare$
</p>
<p>
Consequently, whenever $\det(A) \ne 0$, the unique matrix inverse is:
$$\mathbf{A^{-1} = \frac{1}{\det(A)} \text{adj}(A)}$$
</p>

<h3>3. Cramer’s Rule for Linear Systems</h3>
<p>
For an $n \times n$ system $AX = B$ with $\det(A) \ne 0$, $X = A^{-1} B = \frac{1}{\det A}\text{adj}(A) B$. Entrywise:
$$\mathbf{x_i = \frac{\det(A_i)}{\det(A)}}$$
where $A_i$ is the matrix obtained by replacing the $i$-th column of $A$ with the constant vector $B$.
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-matrix-determinant-sim",
    "title": "Interactive Matrix Transformation & Signed Determinant Visualizer",
    "description": "Drag the column basis vectors of a 2x2 matrix to visualize linear geometric deformations of the unit square. Live computes signed area det(A), matrix trace, orientation parity, and checks singularity conditions det(A) = 0."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 6.1: Determinant Evaluation via Row Operations & Cofactor Inversion",
      "statement": r"Given the $3 \times 3$ matrix $A = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 0 & 2 \\ 4 & 2 & 1 \end{pmatrix}$: (a) Compute $\det(A)$. (b) Construct the adjugate matrix $\text{adj}(A)$ and find $A^{-1}$.",
      "steps": [
        {
          "step": "Step 1: Compute det(A) via Row Operations",
          "math": r"\det(A) = \begin{vmatrix} 2 & 1 & 3 \\ 1 & 0 & 2 \\ 4 & 2 & 1 \end{vmatrix} \xrightarrow{R_3 \to R_3 - 2R_1} \begin{vmatrix} 2 & 1 & 3 \\ 1 & 0 & 2 \\ 0 & 0 & -5 \end{vmatrix} \\ \text{Expand along row 3: } \det(A) = (-5) \cdot (-1)^{3+3} \begin{vmatrix} 2 & 1 \\ 1 & 0 \end{vmatrix} = (-5)(1)(0 - 1) = 5",
          "explanation": "Subtracting $2R_1$ from $R_3$ produces two zeros in row 3, making cofactor expansion trivial."
        },
        {
          "step": "Step 2: Compute All 9 Cofactors",
          "math": r"C_{11} = +\begin{vmatrix} 0 & 2 \\ 2 & 1 \end{vmatrix} = -4, \quad C_{12} = -\begin{vmatrix} 1 & 2 \\ 4 & 1 \end{vmatrix} = 7, \quad C_{13} = +\begin{vmatrix} 1 & 0 \\ 4 & 2 \end{vmatrix} = 2 \\ C_{21} = -\begin{vmatrix} 1 & 3 \\ 2 & 1 \end{vmatrix} = 5, \quad C_{22} = +\begin{vmatrix} 2 & 3 \\ 4 & 1 \end{vmatrix} = -10, \quad C_{23} = -\begin{vmatrix} 2 & 1 \\ 4 & 2 \end{vmatrix} = 0 \\ C_{31} = +\begin{vmatrix} 1 & 3 \\ 0 & 2 \end{vmatrix} = 2, \quad C_{32} = -\begin{vmatrix} 2 & 3 \\ 1 & 2 \end{vmatrix} = -1, \quad C_{33} = +\begin{vmatrix} 2 & 1 \\ 1 & 0 \end{vmatrix} = -1",
          "explanation": "Evaluate the signed minors for each position."
        },
        {
          "step": "Step 3: Transpose to Form adj(A) and Compute A⁻¹",
          "math": r"\text{adj}(A) = C^T = \begin{pmatrix} -4 & 5 & 2 \\ 7 & -10 & -1 \\ 2 & 0 & -1 \end{pmatrix} \\ A^{-1} = \frac{1}{5} \begin{pmatrix} -4 & 5 & 2 \\ 7 & -10 & -1 \\ 2 & 0 & -1 \end{pmatrix} = \begin{pmatrix} -0.8 & 1.0 & 0.4 \\ 1.4 & -2.0 & -0.2 \\ 0.4 & 0.0 & -0.2 \end{pmatrix}",
          "explanation": "Divide the transposed cofactor matrix by $\\det(A) = 5$."
        }
      ],
      "answer": r"\det(A) = 5; \quad \mathbf{A^{-1} = \frac{1}{5}\begin{pmatrix} -4 & 5 & 2 \\ 7 & -10 & -1 \\ 2 & 0 & -1 \end{pmatrix}}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 6.2: Symmetric-Skew Decomposition & Vandermonde Determinant",
      "statement": r"(a) Prove that every square matrix $A$ can be uniquely decomposed as $A = S + K$, where $S$ is symmetric and $K$ is skew-symmetric. (b) Evaluate the $3 \times 3$ Vandermonde determinant $V(a, b, c) = \begin{vmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{vmatrix}$.",
      "steps": [
        {
          "step": "Step 1: Construct the Unique Decomposition",
          "math": r"S \equiv \frac{A + A^T}{2}, \quad K \equiv \frac{A - A^T}{2} \\ S^T = \frac{A^T + (A^T)^T}{2} = \frac{A^T + A}{2} = S \quad (\text{Symmetric}) \\ K^T = \frac{A^T - (A^T)^T}{2} = \frac{A^T - A}{2} = -K \quad (\text{Skew-symmetric}) \\ S + K = \frac{A + A^T + A - A^T}{2} = A",
          "explanation": "Construct $S$ and $K$ explicitly, demonstrating existence."
        },
        {
          "step": "Step 2: Prove Uniqueness",
          "math": r"\text{Suppose } A = S' + K'. \text{ Then } A^T = S'^T + K'^T = S' - K' \\ A + A^T = 2S' \implies S' = \frac{A + A^T}{2} = S \\ A - A^T = 2K' \implies K' = \frac{A - A^T}{2} = K \quad \blacksquare",
          "explanation": "Taking transposes and adding/subtracting establishes uniqueness."
        },
        {
          "step": "Step 3: Evaluate Vandermonde Determinant via Row Operations",
          "math": r"V(a, b, c) = \begin{vmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{vmatrix} \xrightarrow{\substack{R_2 \to R_2 - R_1 \\ R_3 \to R_3 - R_1}} \begin{vmatrix} 1 & a & a^2 \\ 0 & b - a & b^2 - a^2 \\ 0 & c - a & c^2 - a^2 \end{vmatrix} \\ = \begin{vmatrix} b - a & (b - a)(b + a) \\ c - a & (c - a)(c + a) \end{vmatrix} = (b - a)(c - a) \begin{vmatrix} 1 & b + a \\ 1 & c + a \end{vmatrix} \\ = (b - a)(c - a) [(c + a) - (b + a)] = (b - a)(c - a)(c - b) = (c - b)(b - a)(c - a)",
          "explanation": "Factoring $(b-a)$ and $(c-a)$ leaves a simple $2 \\times 2$ determinant."
        }
      ],
      "answer": r"\mathbf{A = \frac{A + A^T}{2} + \frac{A - A^T}{2}} \text{ is unique; } \quad \mathbf{V(a, b, c) = (b - a)(c - a)(c - b)}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 6.3: Closed Formula for Circulant Determinants via Roots of Unity",
      "statement": r"For the $3 \times 3$ circulant matrix $C = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix}$, prove that $\det(C) = (a + b + c)(a + \omega b + \omega^2 c)(a + \omega^2 b + \omega c) = a^3 + b^3 + c^3 - 3abc$, where $\omega = e^{i 2\pi/3}$ is the cube root of unity.",
      "steps": [
        {
          "step": "Step 1: Direct Column Transformation using Roots of Unity",
          "math": r"\text{Let } \omega \text{ satisfy } \omega^3 = 1, \; 1 + \omega + \omega^2 = 0 \\ \text{Add } \omega \cdot \text{Col}_2 + \omega^2 \cdot \text{Col}_3 \text{ to } \text{Col}_1: \\ \text{Row 1: } a + \omega b + \omega^2 c \\ \text{Row 2: } c + \omega a + \omega^2 b = \omega(a + \omega b + \omega^2 c) \quad (\text{since } \omega^3 c = c) \\ \text{Row 3: } b + \omega c + \omega^2 a = \omega^2(a + \omega b + \omega^2 c)",
          "explanation": "The linear combination produces a common factor $(a + \\omega b + \\omega^2 c)$ down the entire first column!"
        },
        {
          "step": "Step 2: Factor Out Eigenvalues",
          "math": r"\text{For each } k \in \{0, 1, 2\}, \text{ substituting the root } \omega^k \text{ proves that } \lambda_k = a + \omega^k b + \omega^{2k} c \text{ is an eigenvalue of } C! \\ \det(C) = \prod_{k=0}^2 \lambda_k = (a + b + c)(a + \omega b + \omega^2 c)(a + \omega^2 b + \omega c)",
          "explanation": "The determinant of any matrix equals the product of its eigenvalues."
        },
        {
          "step": "Step 3: Expand the Product",
          "math": r"(a + \omega b + \omega^2 c)(a + \omega^2 b + \omega c) = a^2 + \omega^2 ab + \omega ac + \omega ab + b^2 + \omega^2 bc + \omega^2 ac + \omega bc + c^2 \\ = a^2 + b^2 + c^2 + (\omega + \omega^2)(ab + bc + ca) = a^2 + b^2 + c^2 - (ab + bc + ca) \\ \det(C) = (a + b + c)[a^2 + b^2 + c^2 - ab - bc - ca] = a^3 + b^3 + c^3 - 3abc \quad \blacksquare",
          "explanation": "Using $1 + \\omega + \\omega^2 = 0 \\implies \\omega + \\omega^2 = -1$ recovers Euler's classical cubic product factorization."
        }
      ],
      "answer": r"\mathbf{\det(C) = a^3 + b^3 + c^3 - 3abc = (a + b + c)(a + \omega b + \omega^2 c)(a + \omega^2 b + \omega c)}."
    }
  ]
}

with open("algebra_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2, ensure_ascii=False)
print("algebra_u5.json written successfully!")

with open("algebra_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6, f, indent=2, ensure_ascii=False)
print("algebra_u6.json written successfully!")
