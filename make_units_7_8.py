import json

# Unit 7: Elementary Operations, Row Reduced Echelon Form (RREF) & Block Matrices
u7 = {
  "unit_id": "unit_7",
  "unit_title": "Elementary Operations, RREF & Block Matrices",
  "unit_subtitle": "Elementary Row Operations, Echelon Uniqueness, Rank-Nullity Theorem, Rouché-Capelli Consistency & Schur Complements",
  "sections": [
    {
      "id": "sec_7_1",
      "title": "Elementary Row Operations & Elementary Matrices",
      "content": r"""
<h3>1. The Three Elementary Row Operations</h3>
<p>
For a matrix $A \in M_{m \times n}(\mathbb{F})$, the elementary row operations are:
<ol>
  <li><strong>Type I (Row Interchange):</strong> $R_i \leftrightarrow R_j$ (swap rows $i$ and $j$).</li>
  <li><strong>Type II (Row Scaling):</strong> $R_i \to c R_i$ with $c \ne 0$ (multiply row $i$ by a non-zero scalar).</li>
  <li><strong>Type III (Row Addition):</strong> $R_i \to R_i + c R_j$ with $i \ne j$ (add a scalar multiple of row $j$ to row $i$).</li>
</ol>
Each operation is strictly reversible by an elementary operation of the identical type!
</p>

<h3>2. Elementary Matrices</h3>
<p>
An <strong>elementary matrix</strong> $E$ is obtained by applying a single elementary row operation to the identity matrix $I_m$.<br>
<strong>Fundamental Principle:</strong> Performing a row operation on $A$ is algebraically identical to pre-multiplying $A$ by the corresponding elementary matrix:
$$\mathbf{A \xrightarrow{\text{Row Op}} B \iff B = E A}$$
Since each elementary matrix is invertible, two matrices $A$ and $B$ are <strong>row equivalent</strong> ($A \sim B$) if and only if there exist elementary matrices $E_1, \dots, E_k$ such that:
$$B = E_k \cdots E_2 E_1 A = P A, \quad \text{where } P \text{ is invertible}$$
</p>
"""
    },
    {
      "id": "sec_7_2",
      "title": "Row Echelon Form (REF) & Reduced Row Echelon Form (RREF)",
      "content": r"""
<h3>1. Row Echelon Form (REF)</h3>
<p>
A matrix is in <strong>Row Echelon Form</strong> if:
<ul>
  <li>All rows consisting entirely of zeros are at the bottom.</li>
  <li>The leading entry (first non-zero entry from the left, called the <em>pivot</em>) of each non-zero row is strictly to the right of the leading entry of the row above it.</li>
  <li>All entries in a column below a leading pivot are zero.</li>
</ul>
</p>

<h3>2. Reduced Row Echelon Form (RREF)</h3>
<p>
A matrix is in <strong>Reduced Row Echelon Form (RREF)</strong> if it satisfies REF and additionally:
<ol>
  <li>Every leading pivot entry is equal to $1$.</li>
  <li>Each leading pivot $1$ is the <em>sole non-zero entry</em> in its column (all entries above and below the pivot are zero).</li>
</ol>
<strong>Theorem (Uniqueness of RREF):</strong> Every matrix $A \in M_{m \times n}$ is row equivalent to a <em>uniquely determined</em> reduced row echelon matrix $\text{rref}(A)$.
</p>
"""
    },
    {
      "id": "sec_7_3",
      "title": "The Rank of a Matrix & The Rank-Nullity Theorem",
      "content": r"""
<h3>1. Row Rank, Column Rank & Matrix Rank</h3>
<p>
<ul>
  <li>The <strong>row space</strong> $\text{Row}(A) \subseteq \mathbb{F}^n$ is the subspace spanned by the row vectors of $A$. Its dimension is the <em>row rank</em>.</li>
  <li>The <strong>column space</strong> $\text{Col}(A) \subseteq \mathbb{F}^m$ is the subspace spanned by the column vectors of $A$. Its dimension is the <em>column rank</em>.</li>
</ul>
<strong>Fundamental Rank Theorem:</strong> For any matrix $A \in M_{m \times n}$:
$$\mathbf{\text{row rank}(A) = \text{column rank}(A) = \text{rank}(A)}$$
The rank equals the number of non-zero rows (or pivot columns) in $\text{rref}(A)$.
</p>

<h3>2. The Rank-Nullity Theorem</h3>
<p>
The <strong>nullspace</strong> (kernel) of $A$ is $\text{Null}(A) = \{X \in \mathbb{F}^n \mid AX = 0\}$. Its dimension is the <strong>nullity</strong> of $A$, which equals the number of free variables (non-pivot columns) in $\text{rref}(A)$.<br>
<strong>Theorem (Rank-Nullity):</strong> For any $m \times n$ matrix $A$:
$$\mathbf{\text{rank}(A) + \text{nullity}(A) = n \quad (\text{number of columns})}$$
</p>
"""
    },
    {
      "id": "sec_7_4",
      "title": "Systems of Linear Equations & The Rouché-Capelli Theorem",
      "content": r"""
<h3>1. The Augmented Matrix</h3>
<p>
A system of $m$ linear equations in $n$ variables $AX = B$ is represented by the augmented matrix $[A \mid B] \in M_{m \times (n+1)}$. Applying Gauss-Jordan elimination transforms $[A \mid B]$ into $[R \mid B']$ in RREF without altering the solution set.
</p>

<h3>2. The Rouché–Capelli Consistency Theorem</h3>
<p>
<strong>Theorem:</strong> The linear system $AX = B$ is <strong>consistent</strong> (possesses at least one solution) if and only if the rank of the coefficient matrix equals the rank of the augmented matrix:
$$\mathbf{\text{rank}(A) = \text{rank}([A \mid B])}$$
<em>Classification of Solution Sets:</em>
<ul>
  <li><strong>Inconsistent (No Solutions):</strong> $\text{rank}(A) < \text{rank}([A \mid B])$. This occurs if and only if $\text{rref}([A \mid B])$ contains a row of the form $[0, 0, \dots, 0 \mid 1]$.</li>
  <li><strong>Unique Solution:</strong> $\text{rank}(A) = \text{rank}([A \mid B]) = n$ (every column has a pivot, nullity = 0).</li>
  <li><strong>Infinitely Many Solutions:</strong> $\text{rank}(A) = \text{rank}([A \mid B]) = r < n$. The general solution depends on $k = n - r$ arbitrary parameters (free variables).</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_7_5",
      "title": "Gauss-Jordan Inversion & Block Matrices",
      "content": r"""
<h3>1. Gauss-Jordan Inversion Algorithm</h3>
<p>
To invert an $n \times n$ matrix $A$, form the partitioned augmented matrix $[A \mid I_n]$. Apply elementary row operations to reduce $A$ to $I_n$:
$$\mathbf{[A \mid I_n] \xrightarrow{\text{Gauss-Jordan}} [I_n \mid A^{-1}]}$$
If $\text{rref}(A)$ has fewer than $n$ pivots, $A$ is singular and has no inverse.
</p>

<h3>2. Block Matrices and the Schur Complement</h3>
<p>
Let $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ be a partitioned block matrix with $A$ invertible.<br>
The <strong>Schur complement</strong> of $A$ in $M$ is defined by:
$$\mathbf{S \equiv D - C A^{-1} B}$$
We factor $M$ via block Gaussian elimination:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & 0 \\ C A^{-1} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & S \end{pmatrix} \begin{pmatrix} I & A^{-1} B \\ 0 & I \end{pmatrix}$$
Consequently:
$$\det(M) = \det(A) \det(S) = \det(A) \det(D - C A^{-1} B)$$
If $S$ is also invertible, the explicit block inverse is:
$$\mathbf{M^{-1} = \begin{pmatrix} A^{-1} + A^{-1} B S^{-1} C A^{-1} & -A^{-1} B S^{-1} \\ -S^{-1} C A^{-1} & S^{-1} \end{pmatrix}}$$
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-gauss-jordan-rref-sim",
    "title": "Interactive Gauss-Jordan Elimination & RREF Stepper",
    "description": "Step through Gauss-Jordan row operations on an augmented matrix [A | B]. Live highlights pivot selections, applies row multipliers and row additions, and produces the canonical Reduced Row Echelon Form (RREF)."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 7.1: Computing RREF and Matrix Rank",
      "statement": r"Find the Reduced Row Echelon Form (RREF) and determine the rank of the $3 \times 4$ matrix $A = \begin{pmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & 1 & 9 \\ 3 & 6 & 2 & 14 \end{pmatrix}$.",
      "steps": [
        {
          "step": "Step 1: Eliminate Entries Below Pivot 1",
          "math": r"\begin{pmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & 1 & 9 \\ 3 & 6 & 2 & 14 \end{pmatrix} \xrightarrow{\substack{R_2 \to R_2 - 2R_1 \\ R_3 \to R_3 - 3R_1}} \begin{pmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & 3 \\ 0 & 0 & 5 & 5 \end{pmatrix}",
          "explanation": "Create zeros in column 1 below row 1."
        },
        {
          "step": "Step 2: Normalize Pivot 2",
          "math": r"\xrightarrow{R_2 \to \frac{1}{3}R_2} \begin{pmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 5 & 5 \end{pmatrix}",
          "explanation": "Scale row 2 so pivot in column 3 becomes 1."
        },
        {
          "step": "Step 3: Eliminate Entries Above and Below Pivot 2",
          "math": r"\xrightarrow{\substack{R_1 \to R_1 + R_2 \\ R_3 \to R_3 - 5R_2}} \begin{pmatrix} 1 & 2 & 0 & 4 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}",
          "explanation": "Eliminate above and below pivot column 3. Row 3 vanishes completely."
        },
        {
          "step": "Step 4: Conclude Rank and Pivot Positions",
          "math": r"\text{Pivots are at } (1, 1) \text{ and } (2, 3). \quad \text{Number of non-zero rows} = 2 \implies \text{rank}(A) = 2",
          "explanation": "There are 2 pivot columns (1 and 3) and 2 free columns (2 and 4)."
        }
      ],
      "answer": r"\mathbf{\text{rref}(A) = \begin{pmatrix} 1 & 2 & 0 & 4 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}}; \qquad \mathbf{\text{rank}(A) = 2}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 7.2: Gauss-Jordan Matrix Inversion & Parametric System",
      "statement": r"Use Gauss-Jordan elimination on $[A \mid I_3]$ to compute the inverse of $A = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}$.",
      "steps": [
        {
          "step": "Step 1: Set Up Augmented Matrix [A | I₃]",
          "math": r"\left(\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\ 2 & 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1 \end{array}\right) \xrightarrow{\substack{R_2 \to R_2 - 2R_1 \\ R_3 \to R_3 - R_1}} \left(\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\ 0 & -1 & -3 & -2 & 1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right)",
          "explanation": "Eliminate entries below first pivot."
        },
        {
          "step": "Step 2: Pivot on Column 2",
          "math": r"\xrightarrow{R_2 \to -R_2} \left(\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\ 0 & 1 & 3 & 2 & -1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right) \xrightarrow{\substack{R_1 \to R_1 - R_2 \\ R_3 \to R_3 - R_2}} \left(\begin{array}{ccc|ccc} 1 & 0 & -1 & -1 & 1 & 0 \\ 0 & 1 & 3 & 2 & -1 & 0 \\ 0 & 0 & -4 & -3 & 1 & 1 \end{array}\right)",
          "explanation": "Clear column 2 above and below row 2."
        },
        {
          "step": "Step 3: Pivot on Column 3 and Clean Columns Above",
          "math": r"\xrightarrow{R_3 \to -\frac{1}{4}R_3} \left(\begin{array}{ccc|ccc} 1 & 0 & -1 & -1 & 1 & 0 \\ 0 & 1 & 3 & 2 & -1 & 0 \\ 0 & 0 & 1 & 3/4 & -1/4 & -1/4 \end{array}\right) \xrightarrow{\substack{R_1 \to R_1 + R_3 \\ R_2 \to R_2 - 3R_3}} \left(\begin{array}{ccc|ccc} 1 & 0 & 0 & -1/4 & 3/4 & -1/4 \\ 0 & 1 & 0 & -1/4 & -1/4 & 3/4 \\ 0 & 0 & 1 & 3/4 & -1/4 & -1/4 \end{array}\right)",
          "explanation": "Normalize pivot 3 and eliminate above."
        }
      ],
      "answer": r"\mathbf{A^{-1} = \frac{1}{4}\begin{pmatrix} -1 & 3 & -1 \\ -1 & -1 & 3 \\ 3 & -1 & -1 \end{pmatrix}}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 7.3: Rouché-Capelli Parameter-Dependent System Analysis",
      "statement": r"Analyze the consistency and determine the complete solution set of the system for all values of $\lambda \in \mathbb{R}$: $\begin{cases} x + y + z = 1 \\ x + 2y + 4z = \lambda \\ x + 4y + 10z = \lambda^2 \end{cases}$.",
      "steps": [
        {
          "step": "Step 1: Set Up Augmented Matrix and Perform Row Reduction",
          "math": r"\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 2 & 4 & \lambda \\ 1 & 4 & 10 & \lambda^2 \end{array}\right) \xrightarrow{\substack{R_2 \to R_2 - R_1 \\ R_3 \to R_3 - R_1}} \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & \lambda - 1 \\ 0 & 3 & 9 & \lambda^2 - 1 \end{array}\right) \\ \xrightarrow{R_3 \to R_3 - 3R_2} \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & \lambda - 1 \\ 0 & 0 & 0 & (\lambda^2 - 1) - 3(\lambda - 1) \end{array}\right)",
          "explanation": "Reduce coefficient matrix toward upper triangular form."
        },
        {
          "step": "Step 2: Analyze the Inconsistency Entry",
          "math": r"R_3 \text{ entry: } \lambda^2 - 1 - 3\lambda + 3 = \lambda^2 - 3\lambda + 2 = (\lambda - 1)(\lambda - 2) \\ \text{Rank condition: } \text{rank}(A) = 2 \text{ always.} \\ \text{If } (\lambda - 1)(\lambda - 2) \ne 0 \implies \text{rank}([A \mid B]) = 3 > 2 \implies \text{Inconsistent (No solutions)!}",
          "explanation": "If $\\lambda \\notin \\{1, 2\\}$, the third equation is $0 = \\text{non-zero}$, so no solution exists."
        },
        {
          "step": "Step 3: Solve for Consistent Values λ = 1 and λ = 2",
          "math": r"\text{Case 1: } \lambda = 1: \quad \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right) \xrightarrow{R_1 \to R_1 - R_2} \left(\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 0 & 1 & 3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right) \\ \text{Let } z = t \implies x = 1 + 2t, \; y = -3t, \; z = t \\ \text{Case 2: } \lambda = 2: \quad \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right) \xrightarrow{R_1 \to R_1 - R_2} \left(\begin{array}{ccc|c} 1 & 0 & -2 & 0 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right) \\ \text{Let } z = t \implies x = 2t, \; y = 1 - 3t, \; z = t",
          "explanation": "For $\\lambda \\in \\{1, 2\\}$, $\\text{rank}(A) = \\text{rank}([A \\mid B]) = 2 < 3$, yielding 1 free variable $t$."
        }
      ],
      "answer": r"\begin{cases} \lambda \ne 1, 2: & \text{Inconsistent (No solution)} \\ \lambda = 1: & (x, y, z) = (1 + 2t, -3t, t), \; t \in \mathbb{R} \\ \lambda = 2: & (x, y, z) = (2t, 1 - 3t, t), \; t \in \mathbb{R} \end{cases}"
    }
  ]
}

# Unit 8: The Leontief Input-Output Economic Model
u8 = {
  "unit_id": "unit_8",
  "unit_title": "The Leontief Input-Output Economic Model",
  "unit_subtitle": "Inter-Industry Technological Matrices, The Open Leontief Equation, Hawkins-Simon Viability & Neumann Multipliers",
  "sections": [
    {
      "id": "sec_8_1",
      "title": "Economic Foundations of Inter-Industry Analysis",
      "content": r"""
<h3>1. The Inter-Industry Economic Network</h3>
<p>
Wassily Leontief (1973 Nobel Laureate in Economics) developed input-output analysis to model the interdependence of industries in an economy. In an economy divided into $n$ sectors (e.g., Agriculture, Manufacturing, Energy, Transportation), the output of any one sector serves a dual role:
<ul>
  <li><strong>Intermediate Output:</strong> Consumed by other industries (and by itself) as inputs required for production.</li>
  <li><strong>Final Demand:</strong> Consumed by households, government, capital investment, or export.</li>
</ul>
</p>

<h3>2. The Flow Matrix of Transactions</h3>
<p>
Let $x_{ij}$ denote the dollar value of output from sector $i$ consumed as intermediate input by sector $j$ during a given production period.<br>
Let $d_i$ be the external final consumer demand for sector $i$'s product.<br>
Let $x_i$ be the total gross output produced by sector $i$. Conservation of economic output requires:
$$\mathbf{x_i = \sum_{j=1}^n x_{ij} + d_i, \quad i = 1, 2, \dots, n}$$
Total Gross Output = Total Intermediate Inputs Consumed + Final Demand.
</p>
"""
    },
    {
      "id": "sec_8_2",
      "title": "The Consumption (Technological) Matrix $C$",
      "content": r"""
<h3>1. The Technological Coefficients</h3>
<p>
Assuming constant returns to scale and fixed production recipes, the <strong>technological coefficient</strong> $c_{ij}$ is the dollar amount of sector $i$'s goods required to produce one dollar's worth of sector $j$'s output:
$$\mathbf{c_{ij} \equiv \frac{x_{ij}}{x_j} \iff x_{ij} = c_{ij} x_j}$$
The $n \times n$ matrix $C = [c_{ij}]$ is called the <strong>consumption matrix</strong> (or technological matrix).
</p>

<h3>2. Properties of the Consumption Matrix</h3>
<p>
<ul>
  <li>Every entry is non-negative: $c_{ij} \ge 0$.</li>
  <li>Column $j$ represents the complete cost recipe per dollar produced by industry $j$:
  $$\mathbf{C_{*, j} = \begin{pmatrix} c_{1j} \\ c_{2j} \\ \vdots \\ c_{nj} \end{pmatrix}}$$</li>
  <li><strong>Economic Profitability Condition:</strong> In an economy where industries create value rather than destroying resources, the sum of intermediate material costs per dollar of output must be strictly less than one:
  $$\sum_{i=1}^n c_{ij} < 1, \quad \text{for all } j = 1, \dots, n$$
  The remainder $v_j = 1 - \sum_{i=1}^n c_{ij} > 0$ represents the <strong>value added</strong> (wages, taxes, and operating profit) per dollar of production!</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_8_3",
      "title": "The Open Leontief Production Equation",
      "content": r"""
<h3>1. Derivation of the Matrix Equation</h3>
<p>
Substituting $x_{ij} = c_{ij} x_j$ into the economic conservation balance:
$$x_i = \sum_{j=1}^n c_{ij} x_j + d_i \iff X = C X + D$$
where:
$$X = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \quad (\text{Gross Output Vector}), \qquad D = \begin{pmatrix} d_1 \\ d_2 \\ \vdots \\ d_n \end{pmatrix} \quad (\text{Final Demand Vector})$$
Rewriting into canonical linear system form:
$$\mathbf{(I_n - C) X = D}$$
The matrix $I_n - C$ is called the <strong>Leontief Matrix</strong>.
</p>

<h3>2. The Equilibrium Production Solution</h3>
<p>
If the Leontief matrix $I_n - C$ is invertible, the gross output required across all sectors to satisfy final demand $D$ is uniquely determined by:
$$\mathbf{X = (I_n - C)^{-1} D}$$
The inverse matrix $(I - C)^{-1}$ is termed the <strong>Leontief Inverse</strong> (or Total Requirements Matrix). Its $(i, j)$-th entry represents the total dollar amount that sector $i$ must produce directly and indirectly to supply one dollar of final demand to sector $j$!
</p>
"""
    },
    {
      "id": "sec_8_4",
      "title": "The Hawkins-Simon Economic Viability Conditions",
      "content": r"""
<h3>1. The Economic Viability Problem</h3>
<p>
In real-world economics, negative production is impossible ($X \ge 0$). An economy is defined as <strong>economically viable</strong> if for <em>every</em> non-negative final demand vector $D \ge 0$, there exists a unique non-negative gross production vector $X \ge 0$ satisfying $(I - C)X = D$.
</p>

<h3>2. The Hawkins–Simon Theorem</h3>
<p>
<strong>Theorem (David Hawkins & Herbert Simon, 1949):</strong> An input-output system with consumption matrix $C \ge 0$ is economically viable if and only if all leading principal minors of the Leontief matrix $I - C$ are strictly positive:
<div class="math-display">
$$\Delta_1 = 1 - c_{11} > 0$$
$$\Delta_2 = \begin{vmatrix} 1 - c_{11} & -c_{12} \\ -c_{21} & 1 - c_{22} \end{vmatrix} > 0$$
$$\dots$$
$$\Delta_n = \det(I - C) > 0$$
</div>
<em>Economic Intuition:</em>
<ul>
  <li>$\Delta_1 > 0 \iff c_{11} < 1$: Sector 1 cannot consume more of its own product than it produces.</li>
  <li>$\Delta_2 > 0 \iff (1 - c_{11})(1 - c_{22}) > c_{12} c_{21}$: The combined direct and indirect feedback loops between sectors 1 and 2 must not consume more than their collective net capacity.</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_8_5",
      "title": "Neumann Series Multipliers & The Dual Leontief Price Model",
      "content": r"""
<h3>1. The Neumann Power Series Expansion</h3>
<p>
If the spectral radius $\rho(C) < 1$, the Leontief inverse can be expanded as a convergent geometric matrix series (the <strong>Neumann Series</strong>):
$$\mathbf{(I - C)^{-1} = I + C + C^2 + C^3 + \dots = \sum_{k=0}^\infty C^k}$$
Substituting into the output equation $X = (I - C)^{-1} D$:
$$\mathbf{X = D + C D + C^2 D + C^3 D + \dots}$$
<strong>Economic Multiplier Breakdown:</strong>
<ul>
  <li>$D$: Direct final consumer demand.</li>
  <li>$CD$: First-round intermediate inputs required by industries to produce $D$.</li>
  <li>$C^2 D$: Second-round inputs required to produce the intermediate inputs $CD$.</li>
  <li>$C^k D$: $k$-th generation indirect supply chain requirements throughout the economy.</li>
</ul>
</p>

<h3>2. The Dual Leontief Price Model</h3>
<p>
Let $P = (p_1, p_2, \dots, p_n)$ be the unit price row vector across sectors, and let $V = (v_1, v_2, \dots, v_n)$ be the value-added row vector (wages + profits per unit).
The equilibrium pricing relation states that price equals intermediate material costs plus value added:
$$P = P C + V \iff P(I - C) = V$$
Multiplying by the Leontief inverse from the right yields the equilibrium price structure:
$$\mathbf{P = V (I - C)^{-1}}$$
This allows governments and central banks to calculate how changes in wages or energy tax ($V$) propagate throughout the entire price level of the macroeconomy!
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-leontief-economy-sim",
    "title": "Interactive Leontief Multi-Sector Economy & Supply Chain Simulator",
    "description": "Simulate a 3-sector macroeconomy (Agriculture, Manufacturing, Energy). Adjust consumer demand sliders D and inter-industry dependencies to watch dynamic matrix inversion (I - C)⁻¹, verify Hawkins-Simon viability, and trace supply chain flows."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 8.1: Two-Sector Leontief Economy and Production Equilibrium",
      "statement": r"A two-sector economy consisting of Energy ($E$) and Manufacturing ($M$) has consumption matrix $C = \begin{pmatrix} 0.2 & 0.4 \\ 0.3 & 0.1 \end{pmatrix}$. (a) Verify the Hawkins-Simon conditions. (b) Compute the Leontief inverse $(I - C)^{-1}$. (c) Find the gross production vector $X$ required to satisfy final demand $D = \begin{pmatrix} 100 \\ 200 \end{pmatrix}$ million dollars.",
      "steps": [
        {
          "step": "Step 1: Verify Hawkins-Simon Viability Conditions",
          "math": r"I - C = \begin{pmatrix} 1 - 0.2 & -0.4 \\ -0.3 & 1 - 0.1 \end{pmatrix} = \begin{pmatrix} 0.8 & -0.4 \\ -0.3 & 0.9 \end{pmatrix} \\ \Delta_1 = 0.8 > 0 \quad \checkmark \\ \Delta_2 = \det(I - C) = (0.8)(0.9) - (-0.4)(-0.3) = 0.72 - 0.12 = 0.60 > 0 \quad \checkmark",
          "explanation": "Both principal minors are strictly positive, guaranteeing that the economy is viable."
        },
        {
          "step": "Step 2: Invert the 2x2 Leontief Matrix",
          "math": r"(I - C)^{-1} = \frac{1}{\det(I - C)} \begin{pmatrix} 0.9 & 0.4 \\ 0.3 & 0.8 \end{pmatrix} = \frac{1}{0.6} \begin{pmatrix} 0.9 & 0.4 \\ 0.3 & 0.8 \end{pmatrix} = \begin{pmatrix} 1.5 & 0.667 \\ 0.5 & 1.333 \end{pmatrix}",
          "explanation": "Apply the $2 \\times 2$ matrix inverse formula."
        },
        {
          "step": "Step 3: Compute the Gross Output Vector X",
          "math": r"X = (I - C)^{-1} D = \frac{1}{0.6} \begin{pmatrix} 0.9 & 0.4 \\ 0.3 & 0.8 \end{pmatrix} \begin{pmatrix} 100 \\ 200 \end{pmatrix} \\ = \frac{1}{0.6} \begin{pmatrix} 0.9(100) + 0.4(200) \\ 0.3(100) + 0.8(200) \end{pmatrix} = \frac{1}{0.6} \begin{pmatrix} 90 + 80 \\ 30 + 160 \end{pmatrix} = \frac{1}{0.6} \begin{pmatrix} 170 \\ 190 \end{pmatrix} = \begin{pmatrix} 283.33 \\ 316.67 \end{pmatrix}",
          "explanation": "Multiply the Leontief inverse by the external demand vector."
        }
      ],
      "answer": r"\text{Hawkins-Simon conditions are satisfied; } \mathbf{(I - C)^{-1} = \begin{pmatrix} 1.5 & 0.667 \\ 0.5 & 1.333 \end{pmatrix}}; \quad \mathbf{X = \begin{pmatrix} 283.33 \\ 316.67 \end{pmatrix}} \text{ million dollars}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 8.2: Three-Sector Economic Shift and Output Reallocation",
      "statement": r"A 3-sector economy with technological matrix $C = \begin{pmatrix} 0.1 & 0.2 & 0.2 \\ 0.2 & 0.1 & 0.1 \\ 0.1 & 0.2 & 0.1 \end{pmatrix}$ has current final demand $D = \begin{pmatrix} 50 \\ 60 \\ 40 \end{pmatrix}$. If consumer demand in Sector 2 increases by 50% while others remain unchanged, compute the required change in gross output vector $\Delta X$.",
      "steps": [
        {
          "step": "Step 1: Form the Leontief Matrix I - C",
          "math": r"I - C = \begin{pmatrix} 0.9 & -0.2 & -0.2 \\ -0.2 & 0.9 & -0.1 \\ -0.1 & -0.2 & 0.9 \end{pmatrix}",
          "explanation": "Subtract consumption matrix $C$ from identity matrix $I_3$."
        },
        {
          "step": "Step 2: Determine Demand Shift ΔD",
          "math": r"\Delta D = \begin{pmatrix} 0 \\ 0.50 \times 60 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 30 \\ 0 \end{pmatrix}",
          "explanation": "Only sector 2 experiences an external demand increase of 30 units."
        },
        {
          "step": "Step 3: Solve (I - C) ΔX = ΔD",
          "math": r"\begin{pmatrix} 0.9 & -0.2 & -0.2 \\ -0.2 & 0.9 & -0.1 \\ -0.1 & -0.2 & 0.9 \end{pmatrix} \begin{pmatrix} \Delta x_1 \\ \Delta x_2 \\ \Delta x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 30 \\ 0 \end{pmatrix} \\ \det(I - C) = 0.9(0.81 - 0.02) + 0.2(-0.18 - 0.01) - 0.2(0.04 + 0.09) \\ = 0.9(0.79) + 0.2(-0.19) - 0.2(0.13) = 0.711 - 0.038 - 0.026 = 0.647 \\ \text{Using Cramer's Rule for Column 2 of } (I - C)^{-1}: \\ \text{Cofactors: } C_{12} = -(-0.18 - 0.01) = 0.19, \quad C_{22} = 0.81 - 0.02 = 0.79, \quad C_{32} = -(-0.09 - 0.02) = 0.11 \\ \Delta X = \frac{30}{0.647} \begin{pmatrix} 0.19 \\ 0.79 \\ 0.11 \end{pmatrix} \approx \begin{pmatrix} 8.81 \\ 36.63 \\ 5.10 \end{pmatrix}",
          "explanation": "Compute the direct and indirect multiplier impact using cofactors."
        }
      ],
      "answer": r"\mathbf{\Delta X \approx \begin{pmatrix} 8.81 \\ 36.63 \\ 5.10 \end{pmatrix}} \implies \text{All three sectors must expand output to support Sector 2's demand growth}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 8.3: Neumann Series Convergence & The Dual Price Equilibrium",
      "statement": r"Given an $n$-sector economy with non-negative consumption matrix $C$: (a) Prove that if the maximum column sum satisfies $\|C\|_1 = \max_j \sum_{i=1}^n c_{ij} < 1$, the spectral radius satisfies $\rho(C) < 1$, and the Neumann series $\sum_{k=0}^\infty C^k$ converges strictly to $(I - C)^{-1}$. (b) If $C = \begin{pmatrix} 0.3 & 0.2 \\ 0.1 & 0.4 \end{pmatrix}$ and the value-added vector per unit output is $V = (14, 21)$ dollars, determine the equilibrium price vector $P = (p_1, p_2)$.",
      "steps": [
        {
          "step": "Step 1: Prove Neumann Series Convergence",
          "math": r"\text{For any induced matrix norm } \|\cdot\|, \quad \rho(C) \le \|C\|_1 < 1 \\ \text{Consider partial sum } S_m = \sum_{k=0}^m C^k. \quad (I - C) S_m = I - C^{m+1} \\ \text{Since } \rho(C) < 1, \quad \lim_{m \to \infty} C^{m+1} = 0 \\ \lim_{m \to \infty} (I - C) S_m = I \implies \sum_{k=0}^\infty C^k = (I - C)^{-1} \quad \blacksquare",
          "explanation": "Use operator norm and Gelfand's formula to prove absolute convergence of the matrix power series."
        },
        {
          "step": "Step 2: Formulate the Dual Price Equation P = V(I - C)⁻¹",
          "math": r"P(I - C) = V \iff \begin{pmatrix} p_1 & p_2 \end{pmatrix} \begin{pmatrix} 0.7 & -0.2 \\ -0.1 & 0.6 \end{pmatrix} = \begin{pmatrix} 14 & 21 \end{pmatrix}",
          "explanation": "Set up the horizontal row equation $P(I - C) = V$."
        },
        {
          "step": "Step 3: Invert (I - C) and Compute Equilibrium Prices",
          "math": r"\det(I - C) = (0.7)(0.6) - (-0.2)(-0.1) = 0.42 - 0.02 = 0.40 \\ (I - C)^{-1} = \frac{1}{0.40} \begin{pmatrix} 0.6 & 0.2 \\ 0.1 & 0.7 \end{pmatrix} = \begin{pmatrix} 1.5 & 0.5 \\ 0.25 & 1.75 \end{pmatrix} \\ P = \begin{pmatrix} 14 & 21 \end{pmatrix} \begin{pmatrix} 1.5 & 0.5 \\ 0.25 & 1.75 \end{pmatrix} \\ p_1 = 14(1.5) + 21(0.25) = 21 + 5.25 = 26.25 \\ p_2 = 14(0.5) + 21(1.75) = 7 + 36.75 = 43.75",
          "explanation": "Multiply the value-added row vector by the Leontief inverse."
        }
      ],
      "answer": r"\mathbf{P = (26.25, \; 43.75)} \implies p_1 = \$26.25 \text{ and } p_2 = \$43.75 \text{ per unit}."
    }
  ]
}

with open("algebra_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7, f, indent=2, ensure_ascii=False)
print("algebra_u7.json written successfully!")

with open("algebra_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8, f, indent=2, ensure_ascii=False)
print("algebra_u8.json written successfully!")
