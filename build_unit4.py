# -*- coding: utf-8 -*-
"""
build_unit4.py
Constructs Unit 4: Numerical Linear Algebra & Multi-Variable Non-Linear Systems
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Numerical Linear Algebra & Multi-Variable Non-Linear Systems",
        "leadSummary": "Direct matrix factorizations (LU, Cholesky), partial pivoting stability, iterative solvers (Jacobi, Gauss-Seidel, SOR) with spectral radius convergence criteria, power iteration for eigenvalues, and multi-dimensional Newton-Raphson.",
        "simulations": ["sim_na_linear_solvers"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Direct Solvers: Gaussian Elimination, Pivoting Strategies & LU/Cholesky Factorizations",
                "content": r"""### 1. Gaussian Elimination and Computational Complexity

Solving a linear system $A\vec{x} = \vec{b}$ with $A \in \mathbb{R}^{n \times n}$ and $\vec{b} \in \mathbb{R}^n$ is the central computational primitive of scientific computing.

**Naive Gaussian Elimination** reduces the augmented matrix $[A \mid \vec{b}]$ to upper triangular form $[U \mid \vec{c}]$ through row operations:
$$m_{ik} = \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}, \quad R_i \leftarrow R_i - m_{ik} R_k \quad (i = k+1, \dots, n)$$

#### Computational Operation Count (FLOPs):
- Forward Elimination: $\sum_{k=1}^{n-1} [2(n - k)(n - k + 1)] = \frac{2}{3} n^3 + \mathcal{O}(n^2)$ floating point operations.
- Backward Substitution: $\sum_{k=1}^n [2(n - k) + 1] = n^2 + \mathcal{O}(n)$ floating point operations.
The cubic complexity $\frac{2}{3} n^3$ dominates overall execution time.

---

### 2. Numerical Instability and Pivoting Strategies

If a pivot element $a_{kk}^{(k)}$ is zero, the algorithm crashes (division by zero). More insidiously, if $|a_{kk}^{(k)}| \ll 1$, the multipliers $m_{ik} = a_{ik} / a_{kk}$ become gigantic ($|m_{ik}| \gg 1$), causing catastrophic exponential growth of round-off errors and destroying numerical stability.

#### Partial Pivoting Algorithm:
At stage $k$, search the active column $k$ from row $k$ down to row $n$ for the element with the maximum absolute magnitude:
$$p = \arg\max_{k \le i \le n} |a_{ik}^{(k)}|$$
Interchange rows $k$ and $p$: $R_k \leftrightarrow R_p$.
This guarantees that all multipliers satisfy $|m_{ik}| \le 1$, bounding error amplification and ensuring backwards stability.

#### Scaled Partial Pivoting:
When row elements differ by orders of magnitude, row scaling factor $s_i = \max_{1 \le j \le n} |a_{ij}|$ is computed. The pivot row $p$ is selected to maximize the relative ratio:
$$p = \arg\max_{k \le i \le n} \frac{|a_{ik}^{(k)}|}{s_i}$$

---

### 3. Matrix Factorizations: LU and Cholesky

#### The LU Decomposition ($PA = LU$):
Gaussian elimination with partial pivoting factors a permutation of $A$ into:
$$PA = LU$$
where:
- $P$ is a permutation matrix recording row interchanges.
- $L$ is a unit lower-triangular matrix with $1$'s on the main diagonal and the multipliers $m_{ik}$ below the diagonal.
- $U$ is the upper-triangular matrix produced at the termination of forward elimination.

Solving $A\vec{x} = \vec{b}$ reduces to two sequential $\mathcal{O}(n^2)$ triangular solves:
1. Permute right-hand side: $\vec{b}^* = P\vec{b}$.
2. Forward solve: $L\vec{y} = \vec{b}^*$.
3. Backward solve: $U\vec{x} = \vec{y}$.

#### Cholesky Factorization for Symmetric Positive-Definite (SPD) Matrices:
If $A = A^T$ and $\vec{x}^T A \vec{x} > 0$ for all $\vec{x} \ne \vec{0}$, then $A$ admits a unique factorization:
$$A = L L^T$$
where $L$ is a lower triangular matrix with strictly positive diagonal entries:
$$L_{jj} = \sqrt{a_{jj} - \sum_{k=1}^{j-1} L_{jk}^2}, \quad L_{ij} = \frac{1}{L_{jj}} \left( a_{ij} - \sum_{k=1}^{j-1} L_{ik} L_{jk} \right) \quad (i > j)$$
*Properties:* Cholesky factorization requires $\frac{1}{3} n^3$ FLOPs (half the work of standard LU) and is unconditionally numerically stable without any pivoting!"""
            },
            {
                "secNumber": "4.2",
                "title": "Iterative Methods for Large Sparse Systems: Jacobi, Gauss-Seidel & SOR",
                "content": r"""### 1. Matrix Splitting and General Iterative Framework

When $n$ is very large (e.g. $n = 10^5$ to $10^7$ in finite element and CFD grid models) and $A$ is sparse, direct methods ($\mathcal{O}(n^3)$) are prohibitive due to fill-in. **Iterative methods** generate a sequence of approximations $\vec{x}^{(k)} \to \vec{x}^*$ with sparse matrix-vector products ($\mathcal{O}(n)$ per iteration).

Split $A$ into:
$$A = D - L - U$$
where $D$ is the diagonal, $-L$ is the strictly lower triangular part, and $-U$ is the strictly upper triangular part of $A$.

The general stationary linear iterative scheme has the form:
$$\vec{x}^{(k+1)} = T \vec{x}^{(k)} + \vec{c}$$
where $T$ is the **iteration matrix**.

---

### 2. The Jacobi Method

The Jacobi method updates each coordinate simultaneously using values from the previous iteration $k$:
$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)$$
In matrix form:
$$D \vec{x}^{(k+1)} = (L + U)\vec{x}^{(k)} + \vec{b} \implies \vec{x}^{(k+1)} = \underbrace{D^{-1}(L + U)}_{T_J} \vec{x}^{(k)} + D^{-1}\vec{b}$$

---

### 3. The Gauss-Seidel Method

The Gauss-Seidel method immediately utilizes updated components $x_1^{(k+1)}, \dots, x_{i-1}^{(k+1)}$ as soon as they are computed:
$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)$$
In matrix form:
$$(D - L)\vec{x}^{(k+1)} = U \vec{x}^{(k)} + \vec{b} \implies \vec{x}^{(k+1)} = \underbrace{(D - L)^{-1} U}_{T_{GS}} \vec{x}^{(k)} + (D - L)^{-1}\vec{b}$$

---

### 4. Successive Over-Relaxation (SOR)

To accelerate convergence, SOR computes a weighted average of the previous iterate and the Gauss-Seidel update with relaxation parameter $\omega \in (0, 2)$:
$$x_i^{(k+1)} = (1 - \omega) x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)$$
In matrix form:
$$\vec{x}^{(k+1)} = \underbrace{(D - \omega L)^{-1}[(1 - \omega)D + \omega U]}_{T_{\omega}} \vec{x}^{(k)} + \omega(D - \omega L)^{-1}\vec{b}$$

#### Theorem 4.1 (Ostrowski-Reich Theorem):
If $A$ is a symmetric positive-definite matrix and $0 < \omega < 2$, then the SOR method converges for any initial guess $\vec{x}^{(0)}$.

#### Theorem 4.2 (Optimal Relaxation Parameter $\omega_{\text{opt}}$):
For a consistently ordered tridiagonal matrix $A$, the optimal relaxation parameter $\omega_{\text{opt}}$ that minimizes the spectral radius $\rho(T_\omega)$ is:

$$\omega_{\text{opt}} = \frac{2}{1 + \sqrt{1 - \rho(T_J)^2}}$$

where $\rho(T_J)$ is the spectral radius of the Jacobi iteration matrix. The corresponding optimal spectral radius is:
$$\rho(T_{\omega_{\text{opt}}}) = \omega_{\text{opt}} - 1$$"""
            },
            {
                "secNumber": "4.3",
                "title": "Spectral Radius Theory & Iterative Convergence Criteria",
                "content": r"""### 1. The Spectral Radius of a Matrix

#### Definition 4.1:
The **spectral radius** $\rho(M)$ of a square matrix $M \in \mathbb{C}^{n \times n}$ is the maximum absolute value of its eigenvalues:
$$\rho(M) = \max_{1 \le i \le n} |\lambda_i(M)|$$

#### Theorem 4.3 (Fundamental Convergence Criterion for Linear Iterative Schemes):
The iterative scheme $\vec{x}^{(k+1)} = T \vec{x}^{(k)} + \vec{c}$ converges to the unique solution $\vec{x}^* = (I - T)^{-1}\vec{c}$ for **any** initial vector $\vec{x}^{(0)}$ if and only if:

$$\rho(T) < 1$$

*Rigorous Proof:*
Let $\vec{e}^{(k)} = \vec{x}^{(k)} - \vec{x}^*$ denote the error vector at iteration $k$.
Subtracting $\vec{x}^* = T \vec{x}^* + \vec{c}$ from the recurrence:
$$\vec{e}^{(k+1)} = \vec{x}^{(k+1)} - \vec{x}^* = T(\vec{x}^{(k)} - \vec{x}^*) = T \vec{e}^{(k)}$$
By induction:
$$\vec{e}^{(k)} = T^k \vec{e}^{(0)}$$
For the sequence to converge for every arbitrary $\vec{e}^{(0)}$, we must have:
$$\lim_{k \to \infty} T^k = \mathbf{0}$$
By the Jordan Canonical Form theorem, $T = P J P^{-1}$ where $J = \text{diag}(J_1, \dots, J_m)$.
The powers are $T^k = P J^k P^{-1}$.
Each Jordan block of eigenvalue $\lambda$ satisfies:
$$J_i^k = \begin{pmatrix} \lambda^k & \binom{k}{1}\lambda^{k-1} & \dots \\ 0 & \lambda^k & \dots \\ \vdots & \vdots & \ddots \end{pmatrix}$$
As $k \to \infty$, $J_i^k \to \mathbf{0}$ if and only if $|\lambda_i| < 1$ for all eigenvalues $\lambda_i$.
Hence $\lim_{k \to \infty} T^k = \mathbf{0} \iff \max |\lambda_i| = \rho(T) < 1$. $\blacksquare$

---

### 2. Strictly Diagonally Dominant Matrices

#### Definition 4.2:
A matrix $A \in \mathbb{R}^{n \times n}$ is **strictly diagonally dominant (SDD)** if for every row $i$:
$$|a_{ii}| > \sum_{\substack{j=1 \\ j \ne i}}^n |a_{ij}|$$

#### Theorem 4.4:
If $A$ is strictly diagonally dominant, then both the Jacobi and Gauss-Seidel iterative methods converge unconditionally for any initial guess $\vec{x}^{(0)}$. Furthermore, Gauss-Seidel converges at least twice as fast as Jacobi:
$$\rho(T_{GS}) \le \rho(T_J)^2 < 1$$"""
            },
            {
                "secNumber": "4.4",
                "title": "Systems of Non-Linear Equations: Multi-Dimensional Newton-Raphson",
                "content": r"""### 1. Vector Formulation of Non-Linear Systems

Consider a coupled system of $n$ nonlinear equations in $n$ unknown variables:

$$\vec{F}(\vec{x}) = \begin{pmatrix} f_1(x_1, x_2, \dots, x_n) \\ f_2(x_1, x_2, \dots, x_n) \\ \vdots \\ f_n(x_1, x_2, \dots, x_n) \end{pmatrix} = \vec{0}$$

#### Definition 4.3 (The Jacobian Matrix):
The **Jacobian Matrix** $J(\vec{x}) \in \mathbb{R}^{n \times n}$ contains the first partial derivatives of $\vec{F}$:

$$J(\vec{x}) = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \dots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \dots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \dots & \frac{\partial f_n}{\partial x_n}
\end{pmatrix}$$

---

### 2. The Multi-Dimensional Newton-Raphson Scheme

Expanding $\vec{F}(\vec{x})$ about the current vector iterate $\vec{x}^{(k)}$ using the multivariate Taylor theorem:

$$\vec{F}(\vec{x}) \approx \vec{F}(\vec{x}^{(k)}) + J(\vec{x}^{(k)})(\vec{x} - \vec{x}^{(k)})$$

Setting $\vec{F}(\vec{x}) = \vec{0}$ and defining the update step $\Delta \vec{x}^{(k)} = \vec{x}^{(k+1)} - \vec{x}^{(k)}$:

$$\boxed{J(\vec{x}^{(k)}) \Delta \vec{x}^{(k)} = -\vec{F}(\vec{x}^{(k)})}$$
$$\boxed{\vec{x}^{(k+1)} = \vec{x}^{(k)} + \Delta \vec{x}^{(k)}}$$

*Key Algorithmic Principle:* One must **never** compute the matrix inverse $J^{-1}$ explicitly! Instead, at each iteration, solve the linear system $J \Delta \vec{x} = -\vec{F}$ using LU decomposition with partial pivoting.

#### Theorem 4.5 (Quadratic Convergence in $\mathbb{R}^n$):
If $\vec{F} \in C^2(\mathbb{R}^n)$, $J(\vec{x}^*)$ is non-singular at the root $\vec{x}^*$, and $\vec{x}^{(0)}$ is chosen within a sufficiently small ball $\|\vec{x}^{(0)} - \vec{x}^*\| \le \delta$, then the multivariate Newton sequence converges **quadratically**:

$$\|\vec{x}^{(k+1)} - \vec{x}^*\| \le C \|\vec{x}^{(k)} - \vec{x}^*\|^2$$"""
            }
        ],
        "problems": [
            {
                "id": "na-prob-4-1",
                "tier": 1,
                "difficultyLabel": "Tier 1 • Foundational",
                "title": "LU Factorization with Partial Pivoting & Tri-Diagonal Solve",
                "statement": r"Given the linear system $A\vec{x} = \vec{b}$:<br>$$\begin{pmatrix} 1 & 2 & 4 \\ 3 & 8 & 14 \\ 2 & 6 & 13 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 7 \\ 25 \\ 21 \end{pmatrix}$$<br>1. Perform Gaussian elimination with partial pivoting to factor $PA = LU$.<br>2. Solve the system via sequential forward and backward substitution.<br>3. Verify the residual vector $\vec{r} = \vec{b} - A\vec{x} = \vec{0}$.",
                "solution": r"""<b>Step 1: LU Factorization with Partial Pivoting</b><br>
Matrix $A_0 = \begin{pmatrix} 1 & 2 & 4 \\ 3 & 8 & 14 \\ 2 & 6 & 13 \end{pmatrix}$, Permutation vector $P = [1, 2, 3]^T$.<br>
Column 1: Pivots are $1, 3, 2$. Maximum is $3$ in Row 2. Swap $R_1 \leftrightarrow R_2$ ($P = [2, 1, 3]^T$):<br>
$$A \to \begin{pmatrix} 3 & 8 & 14 \\ 1 & 2 & 4 \\ 2 & 6 & 13 \end{pmatrix}$$
Eliminate below pivot 3:<br>
- $m_{21} = 1/3$. $R_2 \leftarrow R_2 - (1/3)R_1$: $(2 - 8/3, 4 - 14/3) = (-2/3, -2/3)$.<br>
- $m_{31} = 2/3$. $R_3 \leftarrow R_3 - (2/3)R_1$: $(6 - 16/3, 13 - 28/3) = (2/3, 11/3)$.<br>
Column 2: Entries in row 2 and 3 are $-2/3$ and $2/3$. Magnitudes are equal $|2/3| = |-2/3|$. Swap $R_2 \leftrightarrow R_3$ to choose positive pivot ($P = [2, 3, 1]^T$):<br>
Swap row 2 and 3 of active submatrix (and swap multipliers $m_{21} \leftrightarrow m_{31}$):<br>
$$m_{21} = 2/3, \quad m_{31} = 1/3$$
$$\begin{pmatrix} 3 & 8 & 14 \\ 0 & 2/3 & 11/3 \\ 0 & -2/3 & -2/3 \end{pmatrix}$$
Eliminate below pivot $2/3$ in row 3:<br>
- $m_{32} = \frac{-2/3}{2/3} = -1$.<br>
$R_3 \leftarrow R_3 - (-1)R_2$: $-2/3 - (-1)(11/3) = -2/3 + 11/3 = 9/3 = 3$.<br>
Thus, the factors are:
$$P = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}, \quad L = \begin{pmatrix} 1 & 0 & 0 \\ 2/3 & 1 & 0 \\ 1/3 & -1 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 3 & 8 & 14 \\ 0 & 2/3 & 11/3 \\ 0 & 0 & 3 \end{pmatrix}$$
<br><br>
<b>Step 2: Forward Substitution $L\vec{y} = P\vec{b}$</b><br>
$P\vec{b} = [b_2, b_3, b_1]^T = [25, 21, 7]^T$.<br>
- $y_1 = 25$.<br>
- $y_2 = 21 - (2/3)y_1 = 21 - (2/3)(25) = 21 - 50/3 = 13/3$.<br>
- $y_3 = 7 - (1/3)y_1 - (-1)y_2 = 7 - 25/3 + 13/3 = 7 - 12/3 = 7 - 4 = 3$.<br>
Vector $\vec{y} = [25, 13/3, 3]^T$.
<br><br>
<b>Step 3: Backward Substitution $U\vec{x} = \vec{y}$</b><br>
- $3 x_3 = 3 \implies x_3 = 1$.<br>
- $\frac{2}{3} x_2 + \frac{11}{3} x_3 = \frac{13}{3} \implies \frac{2}{3} x_2 + \frac{11}{3}(1) = \frac{13}{3} \implies \frac{2}{3} x_2 = \frac{2}{3} \implies x_2 = 1$.<br>
- $3 x_1 + 8 x_2 + 14 x_3 = 25 \implies 3 x_1 + 8(1) + 14(1) = 25 \implies 3 x_1 + 22 = 25 \implies 3 x_1 = 3 \implies x_1 = 1$.<br>
Solution: $\vec{x} = [1, 1, 1]^T$.
<br><br>
<b>Step 4: Residual Verification</b><br>
$A\vec{x} = \begin{pmatrix} 1(1) + 2(1) + 4(1) \\ 3(1) + 8(1) + 14(1) \\ 2(1) + 6(1) + 13(1) \end{pmatrix} = \begin{pmatrix} 7 \\ 25 \\ 21 \end{pmatrix} = \vec{b}$. Residual is identically zero!""",
                "answer": r"Solution vector $\vec{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$. $PA = LU$ with $P = [2, 3, 1]^T, \vec{y} = [25, 13/3, 3]^T$."
            },
            {
                "id": "na-prob-4-2",
                "tier": 2,
                "difficultyLabel": "Tier 2 • Intermediate Exam",
                "title": "Spectral Radius Analysis & SOR Optimal Relaxation Parameter",
                "statement": r"Consider the linear system with coefficient matrix:<br>$$A = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 1 \\ 0 & 1 & 4 \end{pmatrix}$$<br>1. Calculate the Jacobi iteration matrix $T_J$ and determine its exact spectral radius $\rho(T_J)$.<br>2. Calculate the Gauss-Seidel iteration matrix $T_{GS}$ and verify the relationship $\rho(T_{GS}) = \rho(T_J)^2$.<br>3. Determine the theoretical optimal SOR relaxation parameter $\omega_{\text{opt}}$ and compute the optimal asymptotic rate of convergence.",
                "solution": r"""<b>Step 1: Jacobi Iteration Matrix $T_J$ and Spectral Radius</b><br>
Splitting $A = D - L - U$:
$$D = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \quad L = \begin{pmatrix} 0 & 0 & 0 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix}, \quad U = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix}$$
$D^{-1} = \frac{1}{4} I$.
$$T_J = D^{-1}(L + U) = -\frac{1}{4} \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$
Find eigenvalues of $M = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$:
$$\det(M - \mu I) = \begin{vmatrix} -\mu & 1 & 0 \\ 1 & -\mu & 1 \\ 0 & 1 & -\mu \end{vmatrix} = -\mu(\mu^2 - 1) - 1(-\mu) = -\mu^3 + \mu + \mu = -\mu(\mu^2 - 2) = 0$$
Eigenvalues of $M$: $\mu_1 = \sqrt{2}, \mu_2 = 0, \mu_3 = -\sqrt{2}$.<br>
Therefore, eigenvalues of $T_J = -\frac{1}{4} M$:
$$\lambda_1 = -\frac{\sqrt{2}}{4}, \quad \lambda_2 = 0, \quad \lambda_3 = \frac{\sqrt{2}}{4}$$
$$\boxed{\rho(T_J) = \frac{\sqrt{2}}{4} \approx 0.353553}$$
Since $\rho(T_J) \approx 0.3536 < 1$, Jacobi iteration converges.
<br><br>
<b>Step 2: Gauss-Seidel Matrix $T_{GS}$ and Verification</b><br>
For a tridiagonal consistently ordered matrix, the Young-David theorem establishes $\rho(T_{GS}) = \rho(T_J)^2$:
$$\rho(T_{GS}) = \left(\frac{\sqrt{2}}{4}\right)^2 = \frac{2}{16} = \frac{1}{8} = 0.125000$$
Gauss-Seidel converges roughly 3 times faster than Jacobi per iteration!
<br><br>
<b>Step 3: Optimal SOR Parameter $\omega_{\text{opt}}$</b><br>
Using Theorem 4.2:
$$\omega_{\text{opt}} = \frac{2}{1 + \sqrt{1 - \rho(T_J)^2}} = \frac{2}{1 + \sqrt{1 - (1/8)}} = \frac{2}{1 + \sqrt{7/8}} = \frac{2}{1 + \frac{\sqrt{14}}{4}} = \frac{8}{4 + \sqrt{14}}$$
Evaluating numerically:
$\sqrt{14} \approx 3.741657 \implies 4 + \sqrt{14} \approx 7.741657$.<br>
$$\omega_{\text{opt}} = \frac{8}{7.741657} \approx 1.03337$$
The optimal spectral radius for SOR is:
$$\rho(T_{\omega_{\text{opt}}}) = \omega_{\text{opt}} - 1 \approx 1.03337 - 1 = 0.03337$$
Comparing spectral radii:
- Jacobi: $\rho = 0.3536$
- Gauss-Seidel: $\rho = 0.1250$
- SOR ($\omega = 1.0334$): $\rho = 0.0334$ (Error shrinks by a factor of 30 every single step!)""",
                "answer": r"$\rho(T_J) = \frac{\sqrt{2}}{4} \approx 0.3536$, $\rho(T_{GS}) = \frac{1}{8} = 0.1250$. Optimal SOR parameter $\omega_{\text{opt}} \approx 1.0334$ yielding spectral radius $\rho(T_{\omega}) \approx 0.0334$."
            },
            {
                "id": "na-prob-4-3",
                "tier": 3,
                "difficultyLabel": "Tier 3 • Honors Challenge",
                "title": "Multivariate Newton-Raphson 2D System Quadratic Convergence",
                "statement": r"Consider the nonlinear system of equations:<br>$$f_1(x, y) = x^2 + y^2 - 4 = 0$$<br>$$f_2(x, y) = e^x + y - 1 = 0$$<br>1. Formulate the symbolic Jacobian matrix $J(x, y)$ and write the explicit Newton step $J(\vec{x}_k)\Delta \vec{x}_k = -\vec{F}(\vec{x}_k)$.<br>2. Perform 2 iterations of multivariate Newton-Raphson starting from $\vec{x}_0 = (1.0, -1.0)^T$.<br>3. Prove analytically that the residual $\|\vec{F}(\vec{x}_k)\|$ converges quadratically.",
                "solution": r"""<b>Step 1: Jacobian Matrix Formulation</b><br>
Function vector $\vec{F}(x, y) = \begin{pmatrix} x^2 + y^2 - 4 \\ e^x + y - 1 \end{pmatrix}$.<br>
Partial derivatives:<br>
- $\frac{\partial f_1}{\partial x} = 2x, \quad \frac{\partial f_1}{\partial y} = 2y$<br>
- $\frac{\partial f_2}{\partial x} = e^x, \quad \frac{\partial f_2}{\partial y} = 1$<br>
Jacobian matrix:
$$J(x, y) = \begin{pmatrix} 2x & 2y \\ e^x & 1 \end{pmatrix}$$
Determinant: $\det(J) = 2x(1) - 2y(e^x) = 2(x - y e^x)$.<br>
Linear system for Newton step:
$$\begin{pmatrix} 2x_k & 2y_k \\ e^{x_k} & 1 \end{pmatrix} \begin{pmatrix} \Delta x_k \\ \Delta y_k \end{pmatrix} = -\begin{pmatrix} x_k^2 + y_k^2 - 4 \\ e^{x_k} + y_k - 1 \end{pmatrix}$$
<br><br>
<b>Step 2: Iteration 1 with $\vec{x}_0 = (1.0, -1.0)^T$</b><br>
Evaluate $\vec{F}(\vec{x}_0)$:
- $f_1(1, -1) = 1^2 + (-1)^2 - 4 = 2 - 4 = -2$.<br>
- $f_2(1, -1) = e^1 + (-1) - 1 = 2.718282 - 2 = 0.718282$.<br>
Evaluate $J(\vec{x}_0)$:
$$J(1, -1) = \begin{pmatrix} 2(1) & 2(-1) \\ e^1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -2 \\ 2.718282 & 1 \end{pmatrix}$$
$\det(J) = 2(1) - (-2)(2.718282) = 2 + 5.436564 = 7.436564$.<br>
Solve $\begin{pmatrix} 2 & -2 \\ 2.718282 & 1 \end{pmatrix} \begin{pmatrix} \Delta x_0 \\ \Delta y_0 \end{pmatrix} = \begin{pmatrix} 2 \\ -0.718282 \end{pmatrix}$:
Using Cramer's Rule:
$$\Delta x_0 = \frac{\begin{vmatrix} 2 & -2 \\ -0.718282 & 1 \end{vmatrix}}{7.436564} = \frac{2(1) - (-2)(-0.718282)}{7.436564} = \frac{2 - 1.436564}{7.436564} = \frac{0.563436}{7.436564} \approx 0.075766$$
$$\Delta y_0 = \frac{\begin{vmatrix} 2 & 2 \\ 2.718282 & -0.718282 \end{vmatrix}}{7.436564} = \frac{2(-0.718282) - 2(2.718282)}{7.436564} = \frac{-1.436564 - 5.436564}{7.436564} = \frac{-6.873128}{7.436564} \approx -0.924234$$
Update:
$$\vec{x}_1 = \vec{x}_0 + \Delta \vec{x}_0 = \begin{pmatrix} 1.0 + 0.075766 \\ -1.0 - 0.924234 \end{pmatrix} = \begin{pmatrix} 1.075766 \\ -1.924234 \end{pmatrix}$$
<br><br>
<b>Step 3: Iteration 2</b><br>
Evaluate $\vec{F}(\vec{x}_1)$:
- $f_1 = (1.075766)^2 + (-1.924234)^2 - 4 = 1.157272 + 3.702677 - 4 = 0.859949$.<br>
- $f_2 = e^{1.075766} - 1.924234 - 1 = 2.932230 - 2.924234 = 0.007996$.<br>
Jacobian $J(\vec{x}_1) = \begin{pmatrix} 2.151532 & -3.848468 \\ 2.932230 & 1 \end{pmatrix}$, $\det(J) = 2.151532 + 11.284594 = 13.436126$.<br>
$$\Delta x_1 = \frac{-0.859949(1) - (-3.848468)(-0.007996)}{13.436126} = \frac{-0.859949 - 0.030772}{13.436126} = \frac{-0.890721}{13.436126} \approx -0.066293$$
$$\Delta y_1 = \frac{2.151532(-0.007996) - (-0.859949)(2.932230)}{13.436126} = \frac{-0.017204 + 2.521568}{13.436126} = \frac{2.504364}{13.436126} \approx 0.186390$$
Update:
$$\vec{x}_2 = \begin{pmatrix} 1.075766 - 0.066293 \\ -1.924234 + 0.186390 \end{pmatrix} = \begin{pmatrix} 1.009473 \\ -1.737844 \end{pmatrix}$$
Residual: $\|\vec{F}(\vec{x}_2)\| \approx 0.039$, demonstrating robust quadratic convergence toward the root $(1.00417, -1.72998)^T$!""",
                "answer": r"Iterates: $\vec{x}_0 = (1.0, -1.0)^T, \vec{x}_1 \approx (1.075766, -1.924234)^T, \vec{x}_2 \approx (1.009473, -1.737844)^T$, confirming multidimensional quadratic error reduction."
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Unit 4 built successfully with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
