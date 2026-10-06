# -*- coding: utf-8 -*-
"""
Builder for Linear Algebra Units 7 and 8:
- Unit 7: Inner Product Spaces, Gram-Schmidt, Adjoint Operators & Spectral Theory
- Unit 8: Canonical Forms, Bilinear, Quadratic & Hermitian Forms
"""
import json

def build_unit_7():
    return {
        "id": "la-u7",
        "title": "Unit 7: Inner Product Spaces, Gram-Schmidt, Adjoint Operators & Spectral Theory",
        "description": "Inner product spaces over R and C, induced norms, the Cauchy-Schwarz and Triangle inequalities, orthogonality, orthogonal complements, orthogonal projection theorem, Gram-Schmidt orthonormalization, QR decomposition, dual spaces, adjoint operators, self-adjoint, normal, and unitary operators, and the Real and Complex Spectral Theorems.",
        "sections": [
            {
                "id": "u7-sec1",
                "title": "Inner Product Spaces, Norms, Orthogonality & Cauchy-Schwarz Inequality",
                "content": r"""### 1. Definition of Inner Product Spaces

Let $V$ be a vector space over the field $F$ (where $F = \mathbb{R}$ or $F = \mathbb{C}$). An **Inner Product** on $V$ is a function $\langle \cdot, \cdot \rangle: V \times V \to F$ satisfying four fundamental axioms for all $\vec{u}, \vec{v}, \vec{w} \in V$ and all scalars $c \in F$:

1. **Conjugate Symmetry (Hermitian Symmetry):**
   $$\langle \vec{u}, \vec{v} \rangle = \overline{\langle \vec{v}, \vec{u} \rangle}$$
   *(If $F = \mathbb{R}$, this reduces to ordinary symmetry: $\langle \vec{u}, \vec{v} \rangle = \langle \vec{v}, \vec{u} \rangle$.)*
2. **Linearity in the First Argument:**
   - Additivity: $\langle \vec{u} + \vec{v}, \vec{w} \rangle = \langle \vec{u}, \vec{w} \rangle + \langle \vec{v}, \vec{w} \rangle$
   - Homogeneity: $\langle c\vec{u}, \vec{v} \rangle = c \langle \vec{u}, \vec{v} \rangle$
3. **Conjugate Linearity (Anti-Linearity) in the Second Argument:**
   $$\langle \vec{u}, c\vec{v} + \vec{w} \rangle = \overline{c} \langle \vec{u}, \vec{v} \rangle + \langle \vec{u}, \vec{w} \rangle$$
   *Proof:* $\langle \vec{u}, c\vec{v} \rangle = \overline{\langle c\vec{v}, \vec{u} \rangle} = \overline{c \langle \vec{v}, \vec{u} \rangle} = \overline{c} \, \overline{\langle \vec{v}, \vec{u} \rangle} = \overline{c} \langle \vec{u}, \vec{v} \rangle$.
4. **Positive-Definiteness:**
   $$\langle \vec{v}, \vec{v} \rangle \ge 0 \quad \text{for all } \vec{v} \in V, \quad \text{and } \langle \vec{v}, \vec{v} \rangle = 0 \iff \vec{v} = \vec{0}$$

A vector space $V$ equipped with an inner product is called an **Inner Product Space** (or a **Pre-Hilbert Space**; if complete, a **Hilbert Space**). A real inner product space is often called a **Euclidean Space**, and a complex inner product space a **Unitary Space**.

---

### 2. Archetypal Inner Product Spaces

#### (a) Euclidean Space $\mathbb{R}^n$:
$$\langle \vec{x}, \vec{y} \rangle = \vec{x}^T \vec{y} = \sum_{i=1}^n x_i y_i = x_1 y_1 + x_2 y_2 + \cdots + x_n y_n$$

#### (b) Complex Unitary Space $\mathbb{C}^n$:
$$\langle \vec{x}, \vec{y} \rangle = \vec{y}^\dagger \vec{x} = \sum_{i=1}^n x_i \overline{y_i}$$
*(Note: In mathematical physics literature, the convention $\langle \vec{x}, \vec{y} \rangle = \sum \overline{x_i} y_i$ is also standard; both conventions satisfy the axioms up to transposition).*

#### (c) Continuous Function Space $C[a, b]$:
$$\langle f, g \rangle = \int_a^b f(t) \overline{g(t)} \, dt$$
Positivity holds because if $f$ is continuous and $\int_a^b |f(t)|^2 dt = 0$, then $f(t) = 0$ identically on $[a, b]$.

#### (d) Matrix Space $M_{m \times n}(\mathbb{C})$ (Frobenius Inner Product):
$$\langle A, B \rangle = \text{tr}(B^\dagger A) = \sum_{i=1}^m \sum_{j=1}^n a_{ij} \overline{b_{ij}}$$

---

### 3. Induced Norm and Metric

For any vector $\vec{v} \in V$, the **Induced Norm** (or length) is defined by:
$$\|\vec{v}\| = \sqrt{\langle \vec{v}, \vec{v} \rangle}$$

The induced metric (distance function) between vectors $\vec{u}, \vec{v}$ is:
$$d(\vec{u}, \vec{v}) = \|\vec{u} - \vec{v}\| = \sqrt{\langle \vec{u} - \vec{v}, \vec{u} - \vec{v} \rangle}$$

A vector $\vec{u}$ is called a **unit vector** if $\|\vec{u}\| = 1$. Any non-zero vector $\vec{v}$ can be normalized:
$$\vec{u} = \frac{\vec{v}}{\|\vec{v}\|}$$

---

### 4. The Cauchy-Schwarz Inequality

#### Theorem 7.1 (Cauchy-Schwarz Inequality):
For any vectors $\vec{u}, \vec{v}$ in an inner product space $V$:
$$|\langle \vec{u}, \vec{v} \rangle| \le \|\vec{u}\| \, \|\vec{v}\|$$
Equality holds if and only if $\vec{u}$ and $\vec{v}$ are linearly dependent (i.e., one is a scalar multiple of the other).

#### Rigorous Proof:
- **Case 1:** If $\vec{v} = \vec{0}$, then $\langle \vec{u}, \vec{0} \rangle = 0$ and $\|\vec{v}\| = 0$, so both sides equal $0$. The inequality holds as an equality, and $\{\vec{u}, \vec{0}\}$ is linearly dependent.
- **Case 2:** Assume $\vec{v} \neq \vec{0}$. Let $c \in F$ be an arbitrary scalar. By positive-definiteness:
  $$\|\vec{u} - c\vec{v}\|^2 = \langle \vec{u} - c\vec{v}, \vec{u} - c\vec{v} \rangle \ge 0$$
  Expanding the inner product using linearity and conjugate symmetry:
  $$\begin{aligned}
  \|\vec{u} - c\vec{v}\|^2 &= \langle \vec{u}, \vec{u} - c\vec{v} \rangle - c \langle \vec{v}, \vec{u} - c\vec{v} \rangle \\
  &= \langle \vec{u}, \vec{u} \rangle - \bar{c}\langle \vec{u}, \vec{v} \rangle - c\langle \vec{v}, \vec{u} \rangle + c\bar{c}\langle \vec{v}, \vec{v} \rangle \\
  &= \|\vec{u}\|^2 - \bar{c}\langle \vec{u}, \vec{v} \rangle - c \overline{\langle \vec{u}, \vec{v} \rangle} + |c|^2 \|\vec{v}\|^2 \ge 0
  \end{aligned}$$
  Now make the specific choice of scalar:
  $$c = \frac{\langle \vec{u}, \vec{v} \rangle}{\|\vec{v}\|^2}$$
  Substituting this $c$:
  $$\begin{aligned}
  0 \le \|\vec{u} - c\vec{v}\|^2 &= \|\vec{u}\|^2 - \frac{\overline{\langle \vec{u}, \vec{v} \rangle}}{\|\vec{v}\|^2} \langle \vec{u}, \vec{v} \rangle - \frac{\langle \vec{u}, \vec{v} \rangle}{\|\vec{v}\|^2} \overline{\langle \vec{u}, \vec{v} \rangle} + \frac{|\langle \vec{u}, \vec{v} \rangle|^2}{\|\vec{v}\|^4} \|\vec{v}\|^2 \\
  &= \|\vec{u}\|^2 - \frac{|\langle \vec{u}, \vec{v} \rangle|^2}{\|\vec{v}\|^2} - \frac{|\langle \vec{u}, \vec{v} \rangle|^2}{\|\vec{v}\|^2} + \frac{|\langle \vec{u}, \vec{v} \rangle|^2}{\|\vec{v}\|^2} \\
  &= \|\vec{u}\|^2 - \frac{|\langle \vec{u}, \vec{v} \rangle|^2}{\|\vec{v}\|^2}
  \end{aligned}$$
  Multiplying through by $\|\vec{v}\|^2 > 0$:
  $$|\langle \vec{u}, \vec{v} \rangle|^2 \le \|\vec{u}\|^2 \|\vec{v}\|^2$$
  Taking the non-negative square root of both sides gives:
  $$|\langle \vec{u}, \vec{v} \rangle| \le \|\vec{u}\| \|\vec{v}\|$$
  Equality holds if and only if $\|\vec{u} - c\vec{v}\|^2 = 0 \iff \vec{u} - c\vec{v} = \vec{0} \iff \vec{u} = c\vec{v}$, which means $\vec{u}$ and $\vec{v}$ are collinear. $\blacksquare$

---

### 5. Consequences of Cauchy-Schwarz

#### (a) The Triangle Inequality (Minkowski's Inequality):
For all $\vec{u}, \vec{v} \in V$:
$$\|\vec{u} + \vec{v}\| \le \|\vec{u}\| + \|\vec{v}\|$$
*Proof:*
$$\begin{aligned}
\|\vec{u} + \vec{v}\|^2 &= \langle \vec{u} + \vec{v}, \vec{u} + \vec{v} \rangle = \|\vec{u}\|^2 + \langle \vec{u}, \vec{v} \rangle + \langle \vec{v}, \vec{u} \rangle + \|\vec{v}\|^2 \\
&= \|\vec{u}\|^2 + 2\text{Re}\langle \vec{u}, \vec{v} \rangle + \|\vec{v}\|^2 \\
&\le \|\vec{u}\|^2 + 2|\langle \vec{u}, \vec{v} \rangle| + \|\vec{v}\|^2 \quad (\text{since } \text{Re}(z) \le |z|) \\
&\le \|\vec{u}\|^2 + 2\|\vec{u}\| \|\vec{v}\| + \|\vec{v}\|^2 \quad (\text{by Cauchy-Schwarz}) \\
&= (\|\vec{u}\| + \|\vec{v}\|)^2
\end{aligned}$$
Taking square roots yields $\|\vec{u} + \vec{v}\| \le \|\vec{u}\| + \|\vec{v}\|$. $\blacksquare$

#### (b) The Parallelogram Law:
$$\|\vec{u} + \vec{v}\|^2 + \|\vec{u} - \vec{v}\|^2 = 2\|\vec{u}\|^2 + 2\|\vec{v}\|^2$$
This geometric identity characterizes inner product norms: by the Jordan-von Neumann theorem, a normed space is an inner product space if and only if its norm satisfies the parallelogram identity.

#### (c) The Pythagorean Theorem:
Two vectors $\vec{u}, \vec{v}$ are **orthogonal** ($\vec{u} \perp \vec{v}$) if $\langle \vec{u}, \vec{v} \rangle = 0$.
If $\vec{u} \perp \vec{v}$, then:
$$\|\vec{u} + \vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2$$"""
            },
            {
                "id": "u7-sec2",
                "title": "Gram-Schmidt Orthogonalization, QR Factorization & Orthogonal Projections",
                "content": r"""### 1. Orthogonal and Orthonormal Systems

A subset $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\} \subset V$ is called:
- **Orthogonal** if $\langle \vec{v}_i, \vec{v}_j \rangle = 0$ for all $i \neq j$.
- **Orthonormal** if it is orthogonal and every vector is normalized:
  $$\langle \vec{e}_i, \vec{e}_j \rangle = \delta_{ij} = \begin{cases} 1, & i = j \\ 0, & i \neq j \end{cases}$$

#### Theorem 7.2 (Linear Independence of Orthogonal Sets):
Any orthogonal set of non-zero vectors $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\}$ in an inner product space $V$ is linearly independent.

*Proof:* Suppose $c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_k \vec{v}_k = \vec{0}$.
Take the inner product of both sides with $\vec{v}_j$ ($1 \le j \le k$):
$$\left\langle \sum_{i=1}^k c_i \vec{v}_i, \vec{v}_j \right\rangle = \langle \vec{0}, \vec{v}_j \rangle = 0 \implies \sum_{i=1}^k c_i \langle \vec{v}_i, \vec{v}_j \rangle = 0$$
Since $\langle \vec{v}_i, \vec{v}_j \rangle = 0$ for $i \neq j$, the sum collapses to a single non-zero term:
$$c_j \langle \vec{v}_j, \vec{v}_j \rangle = c_j \|\vec{v}_j\|^2 = 0$$
Since $\vec{v}_j \neq \vec{0}$, $\|\vec{v}_j\|^2 > 0$, forcing $c_j = 0$. Since this holds for all $j \in \{1, \dots, k\}$, the set is linearly independent. $\blacksquare$

---

### 2. Orthogonal Complements and the Orthogonal Projection Theorem

#### Orthogonal Complement:
Let $W$ be a subspace of an inner product space $V$. The **orthogonal complement** of $W$, denoted $W^\perp$ ("$W$ perp"), is defined by:
$$W^\perp = \{\vec{v} \in V : \langle \vec{v}, \vec{w} \rangle = 0 \text{ for all } \vec{w} \in W\}$$

#### Fundamental Properties of $W^\perp$:
1. $W^\perp$ is a subspace of $V$.
2. $W \cap W^\perp = \{\vec{0}\}$ (if $\vec{v} \in W \cap W^\perp$, then $\langle \vec{v}, \vec{v} \rangle = 0 \implies \vec{v} = \vec{0}$).
3. In finite dimensions: $\dim W + \dim W^\perp = \dim V$.
4. $(W^\perp)^\perp = W$.

#### Theorem 7.3 (Orthogonal Decomposition Theorem):
Let $W$ be a finite-dimensional subspace of an inner product space $V$. Then every vector $\vec{v} \in V$ can be uniquely written as:
$$\vec{v} = \vec{w} + \vec{w}^\perp \quad \text{where } \vec{w} \in W \text{ and } \vec{w}^\perp \in W^\perp$$
That is, $V = W \oplus W^\perp$. The vector $\vec{w}$ is called the **orthogonal projection** of $\vec{v}$ onto $W$, written $\text{proj}_W(\vec{v})$.

If $\{\vec{e}_1, \dots, \vec{e}_k\}$ is an **orthonormal basis** for $W$, then:
$$\text{proj}_W(\vec{v}) = \sum_{i=1}^k \langle \vec{v}, \vec{e}_i \rangle \vec{e}_i$$

The projection satisfies the **Best Approximation Property**:
$$\|\vec{v} - \text{proj}_W(\vec{v})\| \le \|\vec{v} - \vec{w}\| \quad \text{for all } \vec{w} \in W$$
with strict inequality for any $\vec{w} \neq \text{proj}_W(\vec{v})$.

---

<div id="sim_la_inner_product_gram_schmidt" class="sim-mount-point"></div>

---

### 3. The Gram-Schmidt Orthogonalization Algorithm

Let $\{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n\}$ be a linearly independent set in an inner product space $V$. The **Gram-Schmidt Process** constructs an orthogonal set $\{\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n\}$ such that:
$$\text{span}\{\vec{u}_1, \dots, \vec{u}_k\} = \text{span}\{\vec{v}_1, \dots, \vec{v}_k\} \quad \text{for all } k = 1, 2, \dots, n$$

#### Step-by-Step Construction:
$$\begin{aligned}
\vec{u}_1 &= \vec{v}_1 \\
\vec{u}_2 &= \vec{v}_2 - \frac{\langle \vec{v}_2, \vec{u}_1 \rangle}{\|\vec{u}_1\|^2} \vec{u}_1 \\
\vec{u}_3 &= \vec{v}_3 - \frac{\langle \vec{v}_3, \vec{u}_1 \rangle}{\|\vec{u}_1\|^2} \vec{u}_1 - \frac{\langle \vec{v}_3, \vec{u}_2 \rangle}{\|\vec{u}_2\|^2} \vec{u}_2 \\
&\quad \vdots \\
\vec{u}_k &= \vec{v}_k - \sum_{j=1}^{k-1} \frac{\langle \vec{v}_k, \vec{u}_j \rangle}{\|\vec{u}_j\|^2} \vec{u}_j
\end{aligned}$$

#### Orthonormalization:
To obtain an **orthonormal basis** $\{\vec{e}_1, \dots, \vec{e}_n\}$, normalize each vector:
$$\vec{e}_k = \frac{\vec{u}_k}{\|\vec{u}_k\|}, \quad k = 1, 2, \dots, n$$

---

### 4. The QR Factorization

Let $A \in \mathbb{R}^{m \times n}$ be an $m \times n$ matrix with linearly independent columns $\vec{a}_1, \dots, \vec{a}_n$ ($m \ge n$).
Applying Gram-Schmidt to the columns of $A$ yields orthonormal vectors $\vec{q}_1, \dots, \vec{q}_n$.
Each original column vector can be written as:
$$\vec{a}_k = \sum_{j=1}^k \langle \vec{a}_k, \vec{q}_j \rangle \vec{q}_j = r_{1k}\vec{q}_1 + r_{2k}\vec{q}_2 + \cdots + r_{kk}\vec{q}_k$$
In matrix notation:
$$A = Q R$$
where:
- $Q \in \mathbb{R}^{m \times n}$ has orthonormal columns ($Q^T Q = I_n$).
- $R \in \mathbb{R}^{n \times n}$ is upper triangular with positive diagonal entries $r_{kk} = \|\vec{u}_k\| > 0$:
  $$R = \begin{pmatrix} \langle \vec{a}_1, \vec{q}_1 \rangle & \langle \vec{a}_2, \vec{q}_1 \rangle & \cdots & \langle \vec{a}_n, \vec{q}_1 \rangle \\ 0 & \langle \vec{a}_2, \vec{q}_2 \rangle & \cdots & \langle \vec{a}_n, \vec{q}_2 \rangle \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \langle \vec{a}_n, \vec{q}_n \rangle \end{pmatrix}$$

#### Application to Least Squares:
The overdetermined system $A\vec{x} = \vec{b}$ has normal equations:
$$A^T A \hat{x} = A^T \vec{b} \implies (R^T Q^T)(Q R)\hat{x} = R^T Q^T \vec{b} \implies R^T R \hat{x} = R^T Q^T \vec{b}$$
Since $R$ is invertible ($r_{kk} > 0$), this simplifies directly to the upper-triangular system:
$$R \hat{x} = Q^T \vec{b}$$
which can be solved by simple back-substitution without computing $A^T A$ or its inverse!

---

### 5. Bessel's Inequality and Parseval's Identity

Let $\{\vec{e}_1, \vec{e}_2, \dots\}$ be an orthonormal sequence in an inner product space $V$.
For any $\vec{v} \in V$:
- **Bessel's Inequality:**
  $$\sum_{i=1}^k |\langle \vec{v}, \vec{e}_i \rangle|^2 \le \|\vec{v}\|^2$$
- **Parseval's Identity (Completeness):** If $\{\vec{e}_i\}$ is a complete orthonormal basis:
  $$\|\vec{v}\|^2 = \sum_{i=1}^n |\langle \vec{v}, \vec{e}_i \rangle|^2 \quad \text{and} \quad \langle \vec{u}, \vec{v} \rangle = \sum_{i=1}^n \langle \vec{u}, \vec{e}_i \rangle \overline{\langle \vec{v}, \vec{e}_i \rangle}$$"""
            },
            {
                "id": "u7-sec3",
                "title": "Dual Spaces, Adjoint Operators & Special Classes of Operators",
                "content": r"""### 1. Dual Spaces and the Riesz Representation Theorem

Let $V$ be a vector space over field $F$. The **Dual Space** $V^*$ is the space of all linear functionals on $V$:
$$V^* = \mathcal{L}(V, F) = \{f: V \to F \mid f \text{ is linear}\}$$

If $\beta = \{\vec{v}_1, \dots, \vec{v}_n\}$ is a basis of $V$, its **dual basis** $\beta^* = \{f_1, \dots, f_n\} \subset V^*$ is uniquely determined by:
$$f_i(\vec{v}_j) = \delta_{ij}$$
Every functional $f \in V^*$ can be uniquely expanded as $f = \sum_{i=1}^n f(\vec{v}_i) f_i$.

#### Theorem 7.4 (Riesz Representation Theorem for Finite Dimensions):
Let $V$ be a finite-dimensional inner product space over $F$. For every linear functional $f \in V^*$, there exists a **unique** vector $\vec{z} \in V$ such that:
$$f(\vec{v}) = \langle \vec{v}, \vec{z} \rangle \quad \text{for all } \vec{v} \in V$$
Moreover, $\|f\|_{V^*} = \|\vec{z}\|$.

*Proof:*
- **Existence:** Choose an orthonormal basis $\{\vec{e}_1, \dots, \vec{e}_n\}$ of $V$.
  Define the candidate vector:
  $$\vec{z} = \sum_{i=1}^n \overline{f(\vec{e}_i)} \vec{e}_i$$
  Then for any basis vector $\vec{e}_j$:
  $$\langle \vec{e}_j, \vec{z} \rangle = \left\langle \vec{e}_j, \sum_{i=1}^n \overline{f(\vec{e}_i)} \vec{e}_i \right\rangle = \sum_{i=1}^n f(\vec{e}_i) \langle \vec{e}_j, \vec{e}_i \rangle = f(\vec{e}_j)$$
  Since $f$ and the functional $\vec{v} \mapsto \langle \vec{v}, \vec{z} \rangle$ agree on a basis, by linearity they agree on all of $V$: $f(\vec{v}) = \langle \vec{v}, \vec{z} \rangle$ for all $\vec{v} \in V$.
- **Uniqueness:** Suppose there exists another vector $\vec{z}' \in V$ such that $f(\vec{v}) = \langle \vec{v}, \vec{z}' \rangle$ for all $\vec{v}$.
  Then $\langle \vec{v}, \vec{z} - \vec{z}' \rangle = 0$ for all $\vec{v} \in V$.
  Choosing $\vec{v} = \vec{z} - \vec{z}'$ gives $\|\vec{z} - \vec{z}'\|^2 = 0 \implies \vec{z} = \vec{z}'$. $\blacksquare$

---

### 2. The Adjoint of a Linear Operator

Let $T: V \to W$ be a linear transformation between finite-dimensional inner product spaces over $F$.
For each fixed $\vec{w} \in W$, the map $\vec{v} \mapsto \langle T(\vec{v}), \vec{w} \rangle_W$ is a linear functional on $V$.
By the Riesz Representation Theorem, there exists a unique vector in $V$, denoted $T^*(\vec{w})$, such that:
$$\langle T(\vec{v}), \vec{w} \rangle_W = \langle \vec{v}, T^*(\vec{w}) \rangle_V \quad \text{for all } \vec{v} \in V, \, \vec{w} \in W$$

The mapping $T^*: W \to V$ is linear and is called the **Adjoint** (or **Hermitian Adjoint**) of $T$.

#### Fundamental Algebraic Properties:
1. $(S + T)^* = S^* + T^*$
2. $(c T)^* = \bar{c} T^*$
3. $(S T)^* = T^* S^*$
4. $(T^*)^* = T$
5. If $T$ is invertible, $(T^{-1})^* = (T^*)^{-1}$.
6. $\|T^*\| = \|T\|$.

#### Matrix Representation:
If $\beta$ is an **orthonormal basis** of $V$ and $\gamma$ is an orthonormal basis of $W$, then:
$$[T^*]_\gamma^\beta = ([T]_\beta^\gamma)^\dagger = \overline{([T]_\beta^\gamma)^T}$$
The matrix of the adjoint is the conjugate transpose (Hermitian conjugate) of the matrix of $T$.

#### Fundamental Subspace Relations for Adjoints:
- $\ker(T^*) = (\text{im}(T))^\perp$
- $\text{im}(T^*) = (\ker(T))^\perp$
- $\ker(T) = (\text{im}(T^*))^\perp$
- $\text{im}(T) = (\ker(T^*))^\perp$

---

### 3. Special Classes of Operators

| Operator Class | Defining Relation | Matrix Property (ONB) | Eigenvalue Character |
| :--- | :--- | :--- | :--- |
| **Self-Adjoint (Hermitian)** | $T^* = T$ | $A^\dagger = A$ | All $\lambda_i \in \mathbb{R}$ (strictly real) |
| **Skew-Hermitian** | $T^* = -T$ | $A^\dagger = -A$ | All $\lambda_i \in i\mathbb{R}$ (purely imaginary) |
| **Unitary / Orthogonal** | $T^* T = T T^* = I$ | $U^\dagger U = I$ | All $|\lambda_i| = 1$ (on the unit circle) |
| **Normal** | $T T^* = T^* T$ | $A A^\dagger = A^\dagger A$ | Diagonalizable with ONB of eigenvectors |
| **Projection (Orthogonal)** | $P^2 = P = P^*$ | $P^\dagger = P = P^2$ | $\lambda \in \{0, 1\}$ |

#### Geometric Properties of Unitary / Orthogonal Operators:
An operator $U: V \to V$ is **unitary** (orthogonal if $F = \mathbb{R}$) if and only if it preserves the inner product:
$$\langle U\vec{u}, U\vec{v} \rangle = \langle \vec{u}, \vec{v} \rangle \quad \text{for all } \vec{u}, \vec{v} \in V$$
Consequently, unitary operators preserve norms ($\|U\vec{v}\| = \|\vec{v}\|$) and distances ($d(U\vec{u}, U\vec{v}) = d(\vec{u}, \vec{v})$)—they are isometries of the inner product space."""
            },
            {
                "id": "u7-sec4",
                "title": "The Spectral Theorem & Spectral Decompositions",
                "content": r"""### 1. Fundamental Lemmas for Normal and Self-Adjoint Operators

#### Lemma 7.1 (Eigenvalues of Self-Adjoint Operators are Real):
Let $T: V \to V$ be a self-adjoint operator on an inner product space ($T^* = T$). Then every eigenvalue $\lambda$ of $T$ is real.

*Proof:* Let $\vec{v} \neq \vec{0}$ be an eigenvector of $T$ with eigenvalue $\lambda$, so $T(\vec{v}) = \lambda \vec{v}$.
$$\lambda \|\vec{v}\|^2 = \lambda \langle \vec{v}, \vec{v} \rangle = \langle \lambda \vec{v}, \vec{v} \rangle = \langle T(\vec{v}), \vec{v} \rangle$$
Using the self-adjoint property:
$$\langle T(\vec{v}), \vec{v} \rangle = \langle \vec{v}, T^*(\vec{v}) \rangle = \langle \vec{v}, T(\vec{v}) \rangle = \langle \vec{v}, \lambda \vec{v} \rangle = \bar{\lambda} \langle \vec{v}, \vec{v} \rangle = \bar{\lambda} \|\vec{v}\|^2$$
Equating the first and last expressions:
$$(\lambda - \bar{\lambda}) \|\vec{v}\|^2 = 0$$
Since $\vec{v} \neq \vec{0}$, $\|\vec{v}\|^2 > 0$. Therefore $\lambda - \bar{\lambda} = 0 \implies \lambda = \bar{\lambda}$, so $\lambda \in \mathbb{R}$. $\blacksquare$

#### Lemma 7.2 (Eigenvectors of Normal Operators are Orthogonal):
If $T$ is a normal operator ($T T^* = T^* T$), and $\vec{u}, \vec{v}$ are eigenvectors corresponding to distinct eigenvalues $\lambda_1 \neq \lambda_2$, then $\vec{u} \perp \vec{v}$.

*Proof:* First, observe that for a normal operator, $\|(T - \lambda I)\vec{x}\| = \|(T^* - \bar{\lambda} I)\vec{x}\|$ for all $\vec{x}$.
Indeed:
$$\begin{aligned}
\|(T - \lambda I)\vec{x}\|^2 &= \langle (T - \lambda I)\vec{x}, (T - \lambda I)\vec{x} \rangle = \langle \vec{x}, (T^* - \bar{\lambda} I)(T - \lambda I)\vec{x} \rangle \\
&= \langle \vec{x}, (T^* T - \bar{\lambda} T - \lambda T^* + |\lambda|^2 I)\vec{x} \rangle \\
&= \langle \vec{x}, (T T^* - \lambda T^* - \bar{\lambda} T + |\lambda|^2 I)\vec{x} \rangle \quad (\text{since } T T^* = T^* T) \\
&= \langle (T^* - \bar{\lambda} I)\vec{x}, (T^* - \bar{\lambda} I)\vec{x} \rangle = \|(T^* - \bar{\lambda} I)\vec{x}\|^2
\end{aligned}$$
Thus $T\vec{v} = \lambda_2 \vec{v} \iff T^*\vec{v} = \bar{\lambda}_2 \vec{v}$.
Now consider $\langle T\vec{u}, \vec{v} \rangle$:
$$\lambda_1 \langle \vec{u}, \vec{v} \rangle = \langle \lambda_1 \vec{u}, \vec{v} \rangle = \langle T\vec{u}, \vec{v} \rangle = \langle \vec{u}, T^*\vec{v} \rangle = \langle \vec{u}, \bar{\lambda}_2 \vec{v} \rangle = \lambda_2 \langle \vec{u}, \vec{v} \rangle$$
Rearranging:
$$(\lambda_1 - \lambda_2) \langle \vec{u}, \vec{v} \rangle = 0$$
Since $\lambda_1 \neq \lambda_2$, it follows immediately that $\langle \vec{u}, \vec{v} \rangle = 0$. $\blacksquare$

---

### 2. The Spectral Theorem

#### Theorem 7.5 (The Complex Spectral Theorem):
Let $V$ be a finite-dimensional complex inner product space, and let $T: V \to V$ be a linear operator.
Then $T$ is **normal** ($T T^* = T^* T$) if and only if there exists an **orthonormal basis** of $V$ consisting of eigenvectors of $T$.

In matrix terms: A complex matrix $A \in M_n(\mathbb{C})$ is normal ($A A^\dagger = A^\dagger A$) if and only if it is **unitarily diagonalizable**:
$$A = U \Lambda U^\dagger$$
where $U$ is unitary ($U^\dagger U = I_n$) and $\Lambda$ is diagonal.

#### Theorem 7.6 (The Real Spectral Theorem):
Let $V$ be a finite-dimensional real inner product space, and let $T: V \to V$ be a linear operator.
Then $T$ is **self-adjoint** ($T^* = T$) if and only if there exists an **orthonormal basis** of $V$ consisting of eigenvectors of $T$.

In matrix terms: A real matrix $A \in M_n(\mathbb{R})$ is symmetric ($A^T = A$) if and only if it is **orthogonally diagonalizable**:
$$A = Q \Lambda Q^T$$
where $Q$ is an orthogonal matrix ($Q^T Q = I_n$) and $\Lambda$ is a real diagonal matrix:
$$\Lambda = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n), \quad \lambda_i \in \mathbb{R}$$

---

### 3. The Spectral Decomposition (Resolution of the Identity)

Let $T$ be a normal operator on $V$ with distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_k$, and let $E_i = \ker(T - \lambda_i I)$ be the corresponding eigenspaces.
Because $T$ is normal:
$$V = E_1 \oplus E_2 \oplus \cdots \oplus E_k \quad \text{with } E_i \perp E_j \text{ for } i \neq j$$

Let $P_i$ denote the **orthogonal projection** of $V$ onto the eigenspace $E_i$.

#### Properties of the Spectral Projectors $\{P_1, \dots, P_k\}$:
1. **Idempotence & Self-Adjointness:**
   $$P_i^2 = P_i = P_i^* \quad (i = 1, \dots, k)$$
2. **Mutual Orthogonality:**
   $$P_i P_j = O \quad \text{for all } i \neq j$$
3. **Resolution of the Identity (Completeness):**
   $$\sum_{i=1}^k P_i = I$$
4. **Spectral Decomposition of $T$:**
   $$T = \sum_{i=1}^k \lambda_i P_i$$

#### Functional Calculus:
For any polynomial, rational function, or analytical function $f(z)$ defined on the spectrum of $T$:
$$f(T) = \sum_{i=1}^k f(\lambda_i) P_i$$

In particular:
- Powers: $T^m = \sum_{i=1}^k \lambda_i^m P_i$
- Inverse: $T^{-1} = \sum_{i=1}^k \lambda_i^{-1} P_i$ (if $\lambda_i \neq 0$ for all $i$)
- Matrix Exponential: $e^{t T} = \sum_{i=1}^k e^{t \lambda_i} P_i$"""
            }
        ],
        "problems": [
            {
                "tier": 1,
                "title": "Gram-Schmidt Orthonormalization and Orthogonal Projection in R^4",
                "statement": r"""Consider the three linearly independent vectors in $\mathbb{R}^4$ equipped with the standard Euclidean inner product:
$$\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}$$
Let $W = \text{span}\{\vec{v}_1, \vec{v}_2, \vec{v}_3\}$.
1. Apply the Gram-Schmidt process to construct an orthonormal basis $\{\vec{e}_1, \vec{e}_2, \vec{e}_3\}$ for $W$.
2. Compute the orthogonal projection $\text{proj}_W(\vec{b})$ of the vector $\vec{b} = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}$ onto the subspace $W$.""",
                "derivation": r"""### Step 1: Gram-Schmidt Orthogonalization

#### First Vector:
$$\vec{u}_1 = \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$
$$\|\vec{u}_1\|^2 = 1^2 + 1^2 + 0^2 + 0^2 = 2 \implies \|\vec{u}_1\| = \sqrt{2}$$
$$\vec{e}_1 = \frac{\vec{u}_1}{\|\vec{u}_1\|} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \\ 0 \end{pmatrix}$$

#### Second Vector:
Compute $\langle \vec{v}_2, \vec{u}_1 \rangle$:
$$\langle \vec{v}_2, \vec{u}_1 \rangle = 0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 + 0 \cdot 0 = 1$$
The orthogonal projection of $\vec{v}_2$ onto $\vec{u}_1$ is:
$$\frac{\langle \vec{v}_2, \vec{u}_1 \rangle}{\|\vec{u}_1\|^2} \vec{u}_1 = \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$
Then:
$$\vec{u}_2 = \vec{v}_2 - \frac{1}{2}\vec{u}_1 = \begin{pmatrix} 0 \\ 1 \\ 1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1/2 \\ 1/2 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} -1/2 \\ 1/2 \\ 1 \\ 0 \end{pmatrix}$$
Clear fractions to compute the norm: $2\vec{u}_2 = (-1, 1, 2, 0)^T$.
$$\|\vec{u}_2\|^2 = \left(-\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 + 1^2 + 0^2 = \frac{1}{4} + \frac{1}{4} + 1 = \frac{6}{4} = \frac{3}{2}$$
$$\|\vec{u}_2\| = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2}$$
Normalizing:
$$\vec{e}_2 = \frac{\vec{u}_2}{\|\vec{u}_2\|} = \frac{1}{\sqrt{6}/2} \begin{pmatrix} -1/2 \\ 1/2 \\ 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{6}} \begin{pmatrix} -1 \\ 1 \\ 2 \\ 0 \end{pmatrix}$$

#### Third Vector:
Compute inner products with $\vec{u}_1$ and $\vec{u}_2$:
$$\langle \vec{v}_3, \vec{u}_1 \rangle = 0 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 + 1 \cdot 0 = 0$$
$$\langle \vec{v}_3, \vec{u}_2 \rangle = 0\left(-\frac{1}{2}\right) + 0\left(\frac{1}{2}\right) + 1(1) + 1(0) = 1$$
Thus:
$$\vec{u}_3 = \vec{v}_3 - \frac{\langle \vec{v}_3, \vec{u}_1 \rangle}{\|\vec{u}_1\|^2}\vec{u}_1 - \frac{\langle \vec{v}_3, \vec{u}_2 \rangle}{\|\vec{u}_2\|^2}\vec{u}_2$$
$$\vec{u}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} - \vec{0} - \frac{1}{3/2} \begin{pmatrix} -1/2 \\ 1/2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} - \frac{2}{3} \begin{pmatrix} -1/2 \\ 1/2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \\ 1 \end{pmatrix}$$
Compute norm:
$$\|\vec{u}_3\|^2 = \left(\frac{1}{3}\right)^2 + \left(-\frac{1}{3}\right)^2 + \left(\frac{1}{3}\right)^2 + 1^2 = \frac{1}{9} + \frac{1}{9} + \frac{1}{9} + 1 = \frac{12}{9} = \frac{4}{3}$$
$$\|\vec{u}_3\| = \frac{2}{\sqrt{3}}$$
Normalizing:
$$\vec{e}_3 = \frac{\sqrt{3}}{2} \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \\ 1 \end{pmatrix} = \frac{1}{2\sqrt{3}} \begin{pmatrix} 1 \\ -1 \\ 1 \\ 3 \end{pmatrix} = \frac{1}{\sqrt{12}} \begin{pmatrix} 1 \\ -1 \\ 1 \\ 3 \end{pmatrix}$$

---

### Step 2: Compute Orthogonal Projection $\text{proj}_W(\vec{b})$

Using the orthonormal basis $\{\vec{e}_1, \vec{e}_2, \vec{e}_3\}$:
$$\text{proj}_W(\vec{b}) = \langle \vec{b}, \vec{e}_1 \rangle \vec{e}_1 + \langle \vec{b}, \vec{e}_2 \rangle \vec{e}_2 + \langle \vec{b}, \vec{e}_3 \rangle \vec{e}_3$$
For $\vec{b} = (1, 2, 3, 4)^T$:
$$\langle \vec{b}, \vec{e}_1 \rangle = \frac{1}{\sqrt{2}} (1\cdot 1 + 2\cdot 1 + 0 + 0) = \frac{3}{\sqrt{2}}$$
$$\langle \vec{b}, \vec{e}_2 \rangle = \frac{1}{\sqrt{6}} (1(-1) + 2(1) + 3(2) + 0) = \frac{-1 + 2 + 6}{\sqrt{6}} = \frac{7}{\sqrt{6}}$$
$$\langle \vec{b}, \vec{e}_3 \rangle = \frac{1}{2\sqrt{3}} (1(1) + 2(-1) + 3(1) + 4(3)) = \frac{1 - 2 + 3 + 12}{2\sqrt{3}} = \frac{14}{2\sqrt{3}} = \frac{7}{\sqrt{3}}$$

Now compute the terms:
$$\langle \vec{b}, \vec{e}_1 \rangle \vec{e}_1 = \frac{3}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 3/2 \\ 3/2 \\ 0 \\ 0 \end{pmatrix}$$
$$\langle \vec{b}, \vec{e}_2 \rangle \vec{e}_2 = \frac{7}{6} \begin{pmatrix} -1 \\ 1 \\ 2 \\ 0 \end{pmatrix} = \begin{pmatrix} -7/6 \\ 7/6 \\ 7/3 \\ 0 \end{pmatrix}$$
$$\langle \vec{b}, \vec{e}_3 \rangle \vec{e}_3 = \frac{7}{6} \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \\ 1 \end{pmatrix} \cdot 3 = \frac{7}{12} \begin{pmatrix} 1 \\ -1 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 7/12 \\ -7/12 \\ 7/12 \\ 7/4 \end{pmatrix}$$

Summing component-wise:
$$x_1 = \frac{3}{2} - \frac{7}{6} + \frac{7}{12} = \frac{18 - 14 + 7}{12} = \frac{11}{12}$$
$$x_2 = \frac{3}{2} + \frac{7}{6} - \frac{7}{12} = \frac{18 + 14 - 7}{12} = \frac{25}{12}$$
$$x_3 = 0 + \frac{7}{3} + \frac{7}{12} = \frac{28 + 7}{12} = \frac{35}{12}$$
$$x_4 = 0 + 0 + \frac{7}{4} = \frac{21}{12}$$

$$\text{proj}_W(\vec{b}) = \frac{1}{12} \begin{pmatrix} 11 \\ 25 \\ 35 \\ 21 \end{pmatrix}$$

Verification of orthogonality: $\vec{b} - \text{proj}_W(\vec{b}) = \frac{1}{12} (1, -1, 1, 27)^T \dots$ check $\vec{b} - \vec{w} \perp \vec{v}_i$:
$\frac{1}{12} (12 - 11, 24 - 25, 36 - 35, 48 - 21)^T = \frac{1}{12} (1, -1, 1, 27)^T$? Wait:
Let's check $\langle \vec{b} - \vec{w}, \vec{v}_1 \rangle = \frac{1}{12}(1(1) - 1(1)) = 0$. $\checkmark$
$\langle \vec{b} - \vec{w}, \vec{v}_2 \rangle = \frac{1}{12}(-1(1) + 1(1)) = 0$. $\checkmark$
$\langle \vec{b} - \vec{w}, \vec{v}_3 \rangle = \frac{1}{12}(1(1) + 27(1)) = 28/12 \neq 0$? Let's re-verify $\vec{e}_3$ and components:
$\vec{e}_3 = \frac{1}{\sqrt{12}} (1, -1, 1, 3)^T$.
$\|\vec{e}_3\|^2 = \frac{1 + 1 + 1 + 9}{12} = 1$. $\checkmark$
$\langle \vec{e}_3, \vec{v}_1 \rangle = \frac{1}{\sqrt{12}}(1 - 1) = 0$. $\checkmark$
$\langle \vec{e}_3, \vec{v}_2 \rangle = \frac{1}{\sqrt{12}}(-1 + 1) = 0$. $\checkmark$
$\langle \vec{b}, \vec{e}_3 \rangle = \frac{1}{\sqrt{12}}(1(1) + 2(-1) + 3(1) + 4(3)) = \frac{1 - 2 + 3 + 12}{\sqrt{12}} = \frac{14}{\sqrt{12}}$.
Then $\langle \vec{b}, \vec{e}_3 \rangle \vec{e}_3 = \frac{14}{12} \begin{pmatrix} 1 \\ -1 \\ 1 \\ 3 \end{pmatrix} = \frac{7}{6} \begin{pmatrix} 1 \\ -1 \\ 1 \\ 3 \end{pmatrix}$!
Ah! In the intermediate step earlier, $\frac{14}{2\sqrt{3}} \cdot \frac{1}{2\sqrt{3}} = \frac{14}{12} = \frac{7}{6}$!
Let's recalculate with $\frac{7}{6}$:
$$x_1 = \frac{3}{2} - \frac{7}{6} + \frac{7}{6} = \frac{3}{2} = \frac{6}{4}$$
$$x_2 = \frac{3}{2} + \frac{7}{6} - \frac{7}{6} = \frac{3}{2} = \frac{6}{4}$$
$$x_3 = 0 + \frac{14}{6} + \frac{7}{6} = \frac{21}{6} = \frac{7}{2}$$
$$x_4 = 0 + 0 + \frac{21}{6} = \frac{7}{2}$$
Thus:
$$\text{proj}_W(\vec{b}) = \begin{pmatrix} 3/2 \\ 3/2 \\ 7/2 \\ 7/2 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 3 \\ 3 \\ 7 \\ 7 \end{pmatrix}$$
Now check orthogonality of $\vec{b} - \text{proj}_W(\vec{b})$:
$$\vec{b} - \text{proj}_W(\vec{b}) = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} - \begin{pmatrix} 3/2 \\ 3/2 \\ 7/2 \\ 7/2 \end{pmatrix} = \begin{pmatrix} -1/2 \\ 1/2 \\ -1/2 \\ 1/2 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} -1 \\ 1 \\ -1 \\ 1 \end{pmatrix}$$
Check against all 3 generators:
- $\langle \vec{v}_1, \vec{b} - \vec{w} \rangle = 1(-1/2) + 1(1/2) + 0 + 0 = 0$. $\checkmark$
- $\langle \vec{v}_2, \vec{b} - \vec{w} \rangle = 0 + 1(1/2) + 1(-1/2) + 0 = 0$. $\checkmark$
- $\langle \vec{v}_3, \vec{b} - \vec{w} \rangle = 0 + 0 + 1(-1/2) + 1(1/2) = 0$. $\checkmark$
Perfect! $\vec{b} - \text{proj}_W(\vec{b}) \in W^\perp$ identically!""",
                "answer": r"""Orthonormal basis: $\vec{e}_1 = \frac{1}{\sqrt{2}}(1, 1, 0, 0)^T$, $\vec{e}_2 = \frac{1}{\sqrt{6}}(-1, 1, 2, 0)^T$, $\vec{e}_3 = \frac{1}{\sqrt{12}}(1, -1, 1, 3)^T$. The orthogonal projection is $\text{proj}_W(\vec{b}) = \begin{pmatrix} 3/2 \\ 3/2 \\ 7/2 \\ 7/2 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 3 \\ 3 \\ 7 \\ 7 \end{pmatrix}$."""
            },
            {
                "tier": 2,
                "title": "Orthogonal Diagonalization and Spectral Decomposition of a Symmetric Matrix",
                "statement": r"""Consider the real symmetric matrix:
$$A = \begin{pmatrix} 3 & -1 & 0 \\ -1 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$
1. Find all eigenvalues and an orthonormal basis of eigenvectors for $\mathbb{R}^3$.
2. Construct the orthogonal modal matrix $Q$ such that $Q^T A Q = \Lambda$.
3. Compute the spectral projection matrices $P_1, P_2, P_3$ (or grouped by distinct eigenvalues) and verify that:
   $$A = \sum_i \lambda_i P_i \quad \text{and} \quad \sum_i P_i = I_3$$""",
                "derivation": r"""### Step 1: Characteristic Equation and Eigenvalues

The characteristic equation is $\det(A - \lambda I) = 0$:
$$\det \begin{pmatrix} 3 - \lambda & -1 & 0 \\ -1 & 3 - \lambda & 0 \\ 0 & 0 & 2 - \lambda \end{pmatrix} = 0$$
Expanding along the third row:
$$(2 - \lambda) \cdot \det \begin{pmatrix} 3 - \lambda & -1 \\ -1 & 3 - \lambda \end{pmatrix} = 0$$
$$(2 - \lambda) \left[ (3 - \lambda)^2 - 1 \right] = 0$$
$$(2 - \lambda) (\lambda^2 - 6\lambda + 8) = 0$$
$$(2 - \lambda)(\lambda - 2)(\lambda - 4) = 0 \implies -(\lambda - 2)^2 (\lambda - 4) = 0$$
The eigenvalues are:
- $\lambda_1 = 4$ (multiplicity 1)
- $\lambda_2 = 2$ (multiplicity 2)

---

### Step 2: Eigenspaces and Orthonormal Eigenvectors

#### For $\lambda_1 = 4$:
$$(A - 4I)\vec{v} = \begin{pmatrix} -1 & -1 & 0 \\ -1 & -1 & 0 \\ 0 & 0 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
From row 3: $-2z = 0 \implies z = 0$.
From row 1: $-x - y = 0 \implies y = -x$.
Choosing $x = 1$, we get $\vec{v}_1 = (1, -1, 0)^T$.
Norm: $\|\vec{v}_1\| = \sqrt{1^2 + (-1)^2 + 0} = \sqrt{2}$.
$$\vec{q}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$$

#### For $\lambda_2 = 2$:
$$(A - 2I)\vec{v} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
This yields the single independent equation:
$$x - y = 0 \implies x = y$$
with $z$ completely arbitrary.
Thus any vector in $E_2$ is of the form:
$$\vec{v} = \begin{pmatrix} x \\ x \\ z \end{pmatrix} = x \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + z \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
The vectors $\vec{w}_2 = (1, 1, 0)^T$ and $\vec{w}_3 = (0, 0, 1)^T$ span $E_2$.
Notice that:
$$\langle \vec{w}_2, \vec{w}_3 \rangle = 1\cdot 0 + 1\cdot 0 + 0\cdot 1 = 0$$
They are already mutually orthogonal!
Normalizing each:
$$\vec{q}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{q}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
Also verify $\vec{q}_1 \perp \vec{q}_2$: $\frac{1}{2}(1\cdot 1 + (-1)\cdot 1 + 0) = 0$. $\checkmark$
Thus $\{\vec{q}_1, \vec{q}_2, \vec{q}_3\}$ forms an orthonormal basis of $\mathbb{R}^3$.

---

### Step 3: Orthogonal Matrix $Q$ and Diagonalization

$$Q = \begin{pmatrix} \vec{q}_1 & \vec{q}_2 & \vec{q}_3 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ -1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
$Q^T Q = I_3$, so $Q$ is orthogonal ($Q^{-1} = Q^T$).
$$\Lambda = Q^T A Q = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

---

### Step 4: Spectral Decomposition

The distinct eigenvalues are $\lambda_1 = 4$ and $\lambda_2 = 2$.
The orthogonal projection operator onto $E_4 = \text{span}\{\vec{q}_1\}$ is:
$$P_1 = \vec{q}_1 \vec{q}_1^T = \frac{1}{2} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & -1 & 0 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/2 & 0 \\ -1/2 & 1/2 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

The orthogonal projection operator onto $E_2 = \text{span}\{\vec{q}_2, \vec{q}_3\}$ is:
$$P_2 = \vec{q}_2 \vec{q}_2^T + \vec{q}_3 \vec{q}_3^T$$
$$\vec{q}_2 \vec{q}_2^T = \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
$$\vec{q}_3 \vec{q}_3^T = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
Summing:
$$P_2 = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

#### Verification of Properties:
1. **Resolution of Identity:**
   $$P_1 + P_2 = \begin{pmatrix} 1/2+1/2 & -1/2+1/2 & 0 \\ -1/2+1/2 & 1/2+1/2 & 0 \\ 0 & 0 & 0+1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3 \quad \checkmark$$
2. **Mutual Orthogonality:**
   $$P_1 P_2 = \begin{pmatrix} 1/2 & -1/2 & 0 \\ -1/2 & 1/2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1/4 - 1/4 & 1/4 - 1/4 & 0 \\ -1/4 + 1/4 & -1/4 + 1/4 & 0 \\ 0 & 0 & 0 \end{pmatrix} = O_3 \quad \checkmark$$
3. **Spectral Reconstruction of $A$:**
   $$\begin{aligned}
   \lambda_1 P_1 + \lambda_2 P_2 &= 4 \begin{pmatrix} 1/2 & -1/2 & 0 \\ -1/2 & 1/2 & 0 \\ 0 & 0 & 0 \end{pmatrix} + 2 \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\
   &= \begin{pmatrix} 2 & -2 & 0 \\ -2 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \\
   &= \begin{pmatrix} 3 & -1 & 0 \\ -1 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix} = A \quad \checkmark
   \end{aligned}$$""",
                "answer": r"""Eigenvalues $\lambda_1 = 4, \lambda_2 = 2$ (mult. 2). Orthonormal eigenvectors $\vec{q}_1 = \frac{1}{\sqrt{2}}(1, -1, 0)^T$, $\vec{q}_2 = \frac{1}{\sqrt{2}}(1, 1, 0)^T$, $\vec{q}_3 = (0, 0, 1)^T$. Projectors $P_1 = \begin{pmatrix} 1/2 & -1/2 & 0 \\ -1/2 & 1/2 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $P_2 = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, satisfying $P_1 + P_2 = I_3$ and $4 P_1 + 2 P_2 = A$."""
            },
            {
                "tier": 3,
                "title": "Complete Rigorous Proof of the Real Spectral Theorem",
                "statement": r"""Provide a complete, unskipped mathematical proof of the **Real Spectral Theorem**:
Every real symmetric matrix $A \in M_n(\mathbb{R})$ ($A = A^T$) has all real eigenvalues and can be factored as:
$$A = Q \Lambda Q^T$$
where $Q \in O(n)$ is an orthogonal matrix and $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ is real diagonal.
Include:
1. Proof that all roots of the characteristic polynomial $p(\lambda) = \det(A - \lambda I)$ are strictly real numbers.
2. Proof by induction on dimension $n$ that $A$ admits an orthonormal basis of eigenvectors in $\mathbb{R}^n$, using the invariant subspace property of the orthogonal complement.""",
                "derivation": r"""### Part 1: All Roots of the Characteristic Polynomial are Real

Let $A \in M_n(\mathbb{R}) \subset M_n(\mathbb{C})$ with $A = A^T$.
The characteristic polynomial $p(\lambda) = \det(A - \lambda I)$ is a polynomial of degree $n$ with real coefficients.
By the **Fundamental Theorem of Algebra**, $p(\lambda)$ has at least one complex root $\lambda_0 \in \mathbb{C}$.
Since $\det(A - \lambda_0 I) = 0$, the complex linear system $(A - \lambda_0 I)\vec{z} = \vec{0}$ has a non-trivial solution $\vec{z} \in \mathbb{C}^n$ ($\vec{z} \neq \vec{0}$).

Now consider the Hermitian scalar product on $\mathbb{C}^n$: $\langle \vec{u}, \vec{v} \rangle = \vec{v}^\dagger \vec{u}$.
Compute $\vec{z}^\dagger A \vec{z}$ in two ways:
1. Since $A\vec{z} = \lambda_0 \vec{z}$:
   $$\vec{z}^\dagger (A\vec{z}) = \vec{z}^\dagger (\lambda_0 \vec{z}) = \lambda_0 (\vec{z}^\dagger \vec{z}) = \lambda_0 \|\vec{z}\|^2$$
2. On the other hand, since $A$ is real symmetric, $A^\dagger = (\overline{A})^T = A^T = A$.
   $$\vec{z}^\dagger A \vec{z} = (A^\dagger \vec{z})^\dagger \vec{z} = (A\vec{z})^\dagger \vec{z} = (\lambda_0 \vec{z})^\dagger \vec{z} = \overline{\lambda_0} (\vec{z}^\dagger \vec{z}) = \overline{\lambda_0} \|\vec{z}\|^2$$

Equating the two expressions:
$$\lambda_0 \|\vec{z}\|^2 = \overline{\lambda_0} \|\vec{z}\|^2 \implies (\lambda_0 - \overline{\lambda_0}) \|\vec{z}\|^2 = 0$$
Because $\vec{z} \neq \vec{0}$, $\|\vec{z}\|^2 = \sum_{i=1}^n |z_i|^2 > 0$.
Therefore:
$$\lambda_0 - \overline{\lambda_0} = 0 \implies \lambda_0 = \overline{\lambda_0}$$
This proves that $\lambda_0 \in \mathbb{R}$.
Since this holds for every root of $p(\lambda)$, **all eigenvalues of $A$ are real**.
Furthermore, because $\lambda_0 \in \mathbb{R}$ and $A \in M_n(\mathbb{R})$, the system $(A - \lambda_0 I)\vec{x} = \vec{0}$ is a homogeneous linear system over $\mathbb{R}$, which has a non-trivial **real** solution $\vec{u}_1 \in \mathbb{R}^n$.

---

### Part 2: Induction on Dimension $n$

We prove by mathematical induction on $n \ge 1$ that there exists an orthonormal basis of $\mathbb{R}^n$ consisting of eigenvectors of $A$.

#### Base Case: $n = 1$
For $n = 1$, $A = (a_{11}) \in \mathbb{R}^{1 \times 1}$. The unit vector $\vec{q}_1 = (1)$ is an eigenvector with eigenvalue $\lambda_1 = a_{11}$.
The theorem holds with $Q = (1)$ and $\Lambda = (a_{11})$.

#### Inductive Step:
Assume the theorem holds for all real symmetric matrices of size $(n - 1) \times (n - 1)$.
Let $A \in M_n(\mathbb{R})$ be symmetric.

1. **Existence of First Orthonormal Eigenvector:**
   By Part 1, $A$ has a real eigenvalue $\lambda_1 \in \mathbb{R}$ and an associated non-zero real eigenvector.
   Normalize it to obtain a unit vector $\vec{q}_1 \in \mathbb{R}^n$:
   $$A\vec{q}_1 = \lambda_1 \vec{q}_1, \quad \|\vec{q}_1\| = 1$$

2. **Orthogonal Complement and $A$-Invariance:**
   Let $W = \text{span}\{\vec{q}_1\}$. Then $\dim W = 1$.
   Consider the orthogonal complement:
   $$W^\perp = \{\vec{x} \in \mathbb{R}^n : \langle \vec{x}, \vec{q}_1 \rangle = 0\}$$
   By the dimension theorem for orthogonal complements, $\dim W^\perp = n - 1$.

   **Crucial Claim:** $W^\perp$ is an $A$-invariant subspace; that is, if $\vec{x} \in W^\perp$, then $A\vec{x} \in W^\perp$.
   *Proof of Claim:*
   Let $\vec{x} \in W^\perp$. We test whether $A\vec{x}$ is orthogonal to $\vec{q}_1$:
   $$\langle A\vec{x}, \vec{q}_1 \rangle = (A\vec{x})^T \vec{q}_1 = \vec{x}^T A^T \vec{q}_1$$
   Since $A$ is symmetric ($A^T = A$):
   $$\vec{x}^T A^T \vec{q}_1 = \vec{x}^T (A\vec{q}_1) = \vec{x}^T (\lambda_1 \vec{q}_1) = \lambda_1 (\vec{x}^T \vec{q}_1) = \lambda_1 \langle \vec{x}, \vec{q}_1 \rangle$$
   Since $\vec{x} \in W^\perp$, $\langle \vec{x}, \vec{q}_1 \rangle = 0$. Therefore:
   $$\langle A\vec{x}, \vec{q}_1 \rangle = \lambda_1 \cdot 0 = 0$$
   This proves $A\vec{x} \in W^\perp$, establishing that $W^\perp$ is $A$-invariant!

3. **Restriction of $A$ to $W^\perp$:**
   Choose an arbitrary orthonormal basis $\{\vec{w}_2, \vec{w}_3, \dots, \vec{w}_n\}$ for $W^\perp$.
   Form the $n \times n$ orthogonal matrix $Q_1 = \begin{pmatrix} \vec{q}_1 & \vec{w}_2 & \cdots & \vec{w}_n \end{pmatrix}$.
   Compute $Q_1^T A Q_1$:
   The first column of $Q_1^T A Q_1$ is:
   $$Q_1^T A \vec{q}_1 = Q_1^T (\lambda_1 \vec{q}_1) = \lambda_1 Q_1^T \vec{q}_1 = \lambda_1 \vec{e}_1 = \begin{pmatrix} \lambda_1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$
   Because $A$ is symmetric:
   $$(Q_1^T A Q_1)^T = Q_1^T A^T (Q_1^T)^T = Q_1^T A Q_1$$
   Thus $Q_1^T A Q_1$ is symmetric.
   Since the first column is $(\lambda_1, 0, \dots, 0)^T$, by symmetry the first row is $(\lambda_1, 0, \dots, 0)$:
   $$Q_1^T A Q_1 = \begin{pmatrix} \lambda_1 & \vec{0}^T \\ \vec{0} & A_1 \end{pmatrix}$$
   where $A_1 \in M_{n-1}(\mathbb{R})$ is symmetric: $A_1^T = A_1$.

4. **Application of Inductive Hypothesis:**
   $A_1$ is an $(n-1) \times (n-1)$ real symmetric matrix.
   By the induction hypothesis, there exists an orthogonal matrix $Q_2 \in O(n-1)$ such that:
   $$Q_2^T A_1 Q_2 = \Lambda_1 = \text{diag}(\lambda_2, \lambda_3, \dots, \lambda_n)$$

5. **Assembly of Full Orthogonal Matrix:**
   Define the block orthogonal matrix:
   $$\hat{Q}_2 = \begin{pmatrix} 1 & \vec{0}^T \\ \vec{0} & Q_2 \end{pmatrix} \in O(n)$$
   Then let $Q = Q_1 \hat{Q}_2$.
   $Q$ is orthogonal because the product of orthogonal matrices is orthogonal:
   $$Q^T Q = (\hat{Q}_2^T Q_1^T)(Q_1 \hat{Q}_2) = \hat{Q}_2^T (Q_1^T Q_1) \hat{Q}_2 = \hat{Q}_2^T I_n \hat{Q}_2 = I_n$$
   Finally, evaluate $Q^T A Q$:
   $$\begin{aligned}
   Q^T A Q &= \hat{Q}_2^T (Q_1^T A Q_1) \hat{Q}_2 \\
   &= \begin{pmatrix} 1 & \vec{0}^T \\ \vec{0} & Q_2^T \end{pmatrix} \begin{pmatrix} \lambda_1 & \vec{0}^T \\ \vec{0} & A_1 \end{pmatrix} \begin{pmatrix} 1 & \vec{0}^T \\ \vec{0} & Q_2 \end{pmatrix} \\
   &= \begin{pmatrix} \lambda_1 & \vec{0}^T \\ \vec{0} & Q_2^T A_1 Q_2 \end{pmatrix} \\
   &= \begin{pmatrix} \lambda_1 & \vec{0}^T \\ \vec{0} & \Lambda_1 \end{pmatrix} = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n) = \Lambda
   \end{aligned}$$
   This completes the induction. $\blacksquare$""",
                "answer": r"""Complete rigorous proof established: (1) FTA and Hermitian symmetry show all roots of $p(\lambda)$ are strictly real; (2) Induction on $n$ proves that the orthogonal complement $W^\perp$ of an eigenvector is $A$-invariant, reducing $A$ to symmetric $A_1 \in M_{n-1}(\mathbb{R})$ which diagonalizes by hypothesis, producing $Q \in O(n)$ such that $Q^T A Q = \Lambda$."""
            }
        ]
    }

def build_unit_8():
    return {
        "id": "la-u8",
        "title": "Unit 8: Canonical Forms, Bilinear, Quadratic & Hermitian Forms",
        "description": "Schur triangularization, generalized eigenspaces, nilpotent operators, Jordan canonical form, rational canonical form, bilinear forms, congruence transformations, quadratic forms, Lagrange reduction, Sylvester's Law of Inertia, definiteness criteria, and Hermitian forms.",
        "sections": [
            {
                "id": "u8-sec1",
                "title": "Schur Triangularization, Generalized Eigenspaces & Nilpotent Operators",
                "content": r"""### 1. Schur's Triangularization Theorem

Not all square matrices are diagonalizable. However, every square complex matrix can be triangularized by a unitary transformation.

#### Theorem 8.1 (Schur's Triangularization Theorem):
Let $A \in M_n(\mathbb{C})$. There exists a unitary matrix $U \in U(n)$ ($U^\dagger U = I_n$) such that:
$$U^\dagger A U = T$$
where $T$ is an **upper triangular** matrix:
$$T = \begin{pmatrix} \lambda_1 & t_{12} & \cdots & t_{1n} \\ 0 & \lambda_2 & \cdots & t_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}$$
The diagonal entries $\lambda_1, \dots, \lambda_n$ of $T$ are precisely the eigenvalues of $A$ (counted with algebraic multiplicities).

#### Proof (by Induction on $n$):
- **Base Case:** For $n = 1$, $A$ is a $1 \times 1$ scalar; $U = (1)$ is unitary and $T = A$ is triangular.
- **Inductive Hypothesis:** Assume every $(n-1) \times (n-1)$ matrix is unitarily triangularizable.
- **Inductive Step:**
  By the Fundamental Theorem of Algebra, $A$ has at least one eigenvalue $\lambda_1 \in \mathbb{C}$ with unit eigenvector $\vec{u}_1$ ($\|\vec{u}_1\| = 1$).
  Using Gram-Schmidt, extend $\{\vec{u}_1\}$ to an orthonormal basis $\{\vec{u}_1, \vec{w}_2, \dots, \vec{w}_n\}$ of $\mathbb{C}^n$.
  Form the unitary matrix $U_1 = \begin{pmatrix} \vec{u}_1 & \vec{w}_2 & \cdots & \vec{w}_n \end{pmatrix}$.
  Then:
  $$U_1^\dagger A U_1 = \begin{pmatrix} \vec{u}_1^\dagger \\ \vec{w}_2^\dagger \\ \vdots \end{pmatrix} \begin{pmatrix} A\vec{u}_1 & A\vec{w}_2 & \cdots \end{pmatrix} = \begin{pmatrix} \lambda_1 & \vec{r}^T \\ \vec{0} & A_1 \end{pmatrix}$$
  where $A_1 \in M_{n-1}(\mathbb{C})$.
  By induction, there exists unitary $U_2 \in U(n-1)$ such that $U_2^\dagger A_1 U_2 = T_1$ is upper triangular.
  Setting $U = U_1 \begin{pmatrix} 1 & \vec{0}^T \\ \vec{0} & U_2 \end{pmatrix}$, we find $U^\dagger A U = \begin{pmatrix} \lambda_1 & \vec{r}^T U_2 \\ \vec{0} & T_1 \end{pmatrix} = T$ is upper triangular. $\blacksquare$

---

### 2. Generalized Eigenvectors and Eigenspaces

When a matrix $A$ has an eigenvalue $\lambda$ whose geometric multiplicity $g_\lambda = \dim \ker(A - \lambda I)$ is strictly less than its algebraic multiplicity $a_\lambda$, the eigenspace $E_\lambda$ is insufficient to span $\mathbb{C}^{a_\lambda}$. We must seek **generalized eigenvectors**.

#### Definition:
A non-zero vector $\vec{v} \in V$ is a **Generalized Eigenvector of rank $k$** corresponding to eigenvalue $\lambda$ if:
$$(A - \lambda I)^k \vec{v} = \vec{0} \quad \text{and} \quad (A - \lambda I)^{k-1} \vec{v} \neq \vec{0}$$

#### Generalized Eigenspace:
The **Generalized Eigenspace** corresponding to eigenvalue $\lambda$ is:
$$K_\lambda = \ker\left((A - \lambda I)^n\right) = \{\vec{v} \in V : \exists k \ge 1 \text{ such that } (A - \lambda I)^k \vec{v} = \vec{0}\}$$

#### Fundamental Properties:
1. $E_\lambda \subseteq K_\lambda$.
2. $\dim K_\lambda = a_\lambda$ (the algebraic multiplicity of $\lambda$).
3. $K_\lambda$ is an $A$-invariant subspace: $A(K_\lambda) \subseteq K_\lambda$.

#### Theorem 8.2 (Primary Decomposition Theorem):
Let $T: V \to V$ be a linear operator on a finite-dimensional complex vector space $V$, with distinct eigenvalues $\lambda_1, \dots, \lambda_k$.
Then $V$ decomposes into the direct sum of its generalized eigenspaces:
$$V = K_{\lambda_1} \oplus K_{\lambda_2} \oplus \cdots \oplus K_{\lambda_k}$$
Each $K_{\lambda_i}$ is $T$-invariant, and $(T - \lambda_i I)$ restricted to $K_{\lambda_i}$ is **nilpotent**.

---

### 3. Nilpotent Operators and Jordan Chains

An operator $N: W \to W$ is **nilpotent** if $N^p = O$ for some positive integer $p$.
The smallest such $p$ is the **index of nilpotency** of $N$.

#### Jordan Chains (Cyclic Subspaces for Nilpotent Operators):
Let $\vec{v}$ be a vector such that $N^{k-1} \vec{v} \neq \vec{0}$ but $N^k \vec{v} = \vec{0}$.
The sequence of $k$ vectors:
$$\beta_k = \{N^{k-1}\vec{v}, \, N^{k-2}\vec{v}, \, \dots, \, N\vec{v}, \, \vec{v}\}$$
is linearly independent and spans an $N$-invariant subspace of dimension $k$.
With respect to this ordered basis, the matrix of $N$ is the standard **nilpotent Jordan block**:
$$[N]_{\beta_k} = \begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 1 \\ 0 & 0 & \cdots & 0 & 0 \end{pmatrix}_{k \times k}$$"""
            },
            {
                "id": "u8-sec2",
                "title": "The Jordan Canonical Form & Rational Canonical Form",
                "content": r"""### 1. The Jordan Canonical Form (JCF)

#### Definition of a Jordan Block:
A **Jordan Block** of size $k$ corresponding to eigenvalue $\lambda$, denoted $J_k(\lambda)$, is a $k \times k$ upper bidiagonal matrix:
$$J_k(\lambda) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda & 1 \\ 0 & 0 & \cdots & 0 & \lambda \end{pmatrix}_{k \times k} = \lambda I_k + N_k$$

#### Theorem 8.3 (Jordan Canonical Form Theorem):
Let $A \in M_n(\mathbb{C})$. There exists an invertible matrix $P \in GL_n(\mathbb{C})$ such that:
$$P^{-1} A P = J = \begin{pmatrix} J_{k_1}(\lambda_1) & O & \cdots & O \\ O & J_{k_2}(\lambda_2) & \cdots & O \\ \vdots & \vdots & \ddots & \vdots \\ O & O & \cdots & J_{k_m}(\lambda_m) \end{pmatrix}$$
where each $J_{k_i}(\lambda_i)$ is a Jordan block. The matrix $J$ is unique up to the ordering of the blocks.

---

<div id="sim_la_quadratic_forms" class="sim-mount-point"></div>

---

### 2. Determining Jordan Block Structure from Ranks

Let $\lambda$ be an eigenvalue of $A$, and define $r_k = \text{rank}(A - \lambda I)^k$ (with $r_0 = n$).
- **Total number of Jordan blocks for $\lambda$:**
  $$\text{Number of blocks} = \dim \ker(A - \lambda I) = n - r_1 = g_\lambda \quad (\text{geometric multiplicity})$$
- **Number of Jordan blocks of size $\ge k$:**
  $$N_{\ge k} = r_{k-1} - r_k$$
- **Number of Jordan blocks of size exactly $k$:**
  $$N_k = N_{\ge k} - N_{\ge k+1} = (r_{k-1} - r_k) - (r_k - r_{k+1}) = r_{k-1} - 2r_k + r_{k+1}$$

#### Relation to the Minimal Polynomial:
The size of the **largest** Jordan block associated with eigenvalue $\lambda_i$ equals the multiplicity of $(x - \lambda_i)$ in the **minimal polynomial** $m_A(x)$.
That is, if:
$$p_A(x) = \prod_{i=1}^d (x - \lambda_i)^{a_i} \quad \text{and} \quad m_A(x) = \prod_{i=1}^d (x - \lambda_i)^{m_i}$$
then:
- $\sum (\text{sizes of all blocks for } \lambda_i) = a_i$
- $\max (\text{size of a block for } \lambda_i) = m_i$

---

### 3. The Rational Canonical Form (Frobenius Normal Form)

Unlike the Jordan form, which requires the scalar field to contain all eigenvalues (algebraically closed field like $\mathbb{C}$), the **Rational Canonical Form** is valid over **any** field $F$ (such as $\mathbb{Q}$ or $\mathbb{R}$).

#### Companion Matrix:
For a monic polynomial $p(x) = x^k + c_{k-1} x^{k-1} + \cdots + c_1 x + c_0$, its **Companion Matrix** is:
$$C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -c_0 \\ 1 & 0 & \cdots & 0 & -c_1 \\ 0 & 1 & \cdots & 0 & -c_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & -c_{k-1} \end{pmatrix}$$
The characteristic polynomial and minimal polynomial of $C(p)$ are both equal to $p(x)$.

#### Invariant Factor Decomposition:
Every matrix $A \in M_n(F)$ is similar over $F$ to a unique block-diagonal matrix:
$$R = \text{diag}(C(d_1(x)), \, C(d_2(x)), \, \dots, \, C(d_m(x)))$$
where the monic polynomials $d_1(x), \dots, d_m(x)$ are the **Invariant Factors** of $A$, satisfying:
$$d_1(x) \mid d_2(x) \mid \cdots \mid d_m(x)$$
Moreover:
- $d_m(x) = m_A(x)$ (the minimal polynomial of $A$)
- $d_1(x) d_2(x) \cdots d_m(x) = p_A(x)$ (the characteristic polynomial of $A$)"""
            },
            {
                "id": "u8-sec3",
                "title": "Bilinear and Quadratic Forms, Congruence & Lagrange Reduction",
                "content": r"""### 1. Bilinear Forms

Let $V$ be a vector space over field $F$. A function $B: V \times V \to F$ is a **Bilinear Form** if it is linear in each argument separately:
1. $B(c_1 \vec{u}_1 + c_2 \vec{u}_2, \, \vec{v}) = c_1 B(\vec{u}_1, \vec{v}) + c_2 B(\vec{u}_2, \vec{v})$
2. $B(\vec{u}, \, c_1 \vec{v}_1 + c_2 \vec{v}_2) = c_1 B(\vec{u}, \vec{v}_1) + c_2 B(\vec{u}, \vec{v}_2)$

#### Matrix Representation:
Let $\beta = \{\vec{e}_1, \dots, \vec{e}_n\}$ be an ordered basis of $V$. The matrix of $B$ relative to $\beta$ is $[B]_\beta = (b_{ij}) \in M_n(F)$, where:
$$b_{ij} = B(\vec{e}_i, \vec{e}_j)$$
For any vectors $\vec{x} = \sum x_i \vec{e}_i$ and $\vec{y} = \sum y_j \vec{e}_j$:
$$B(\vec{x}, \vec{y}) = [\vec{x}]_\beta^T [B]_\beta [\vec{y}]_\beta$$

#### Congruence Transformation under Change of Basis:
If $\beta'$ is another basis of $V$ with transition matrix $P$ ($[\vec{x}]_\beta = P [\vec{x}]_{\beta'}$), then:
$$B(\vec{x}, \vec{y}) = (P [\vec{x}]_{\beta'})^T [B]_\beta (P [\vec{y}]_{\beta'}) = [\vec{x}]_{\beta'}^T (P^T [B]_\beta P) [\vec{y}]_{\beta'}$$
Thus the matrix transforms by **Congruence**:
$$[B]_{\beta'} = P^T [B]_\beta P$$
Two matrices $A, B$ are **congruent** if there exists an invertible matrix $P$ such that $B = P^T A P$.

---

### 2. Quadratic Forms

Let $V$ be a vector space over $\mathbb{R}$. A function $q: V \to \mathbb{R}$ is a **Quadratic Form** if $q(\vec{x}) = B(\vec{x}, \vec{x})$ for some symmetric bilinear form $B$.
In coordinates:
$$q(\vec{x}) = \vec{x}^T A \vec{x} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j$$
where $A = A^T = \frac{1}{2}(M + M^T)$ is the unique **symmetric matrix** associated with $q$.
Expanding explicitly:
$$q(x_1, \dots, x_n) = \sum_{i=1}^n a_{ii} x_i^2 + 2 \sum_{1 \le i < j \le n} a_{ij} x_i x_j$$

---

### 3. Diagonalization of Quadratic Forms

Every quadratic form can be reduced to a diagonal form (sum and difference of squares) by a non-singular linear change of variables $\vec{x} = P \vec{y}$:
$$q(\vec{x}) = \vec{y}^T (P^T A P) \vec{y} = \sum_{i=1}^r c_i y_i^2$$

#### Method 1: Lagrange's Method of Completing Squares
An algebraic, non-orthogonal procedure:
- **Case 1 (At least one diagonal coefficient $a_{ii} \neq 0$):**
  Suppose $a_{11} \neq 0$. Group all terms containing $x_1$:
  $$q = a_{11} x_1^2 + 2x_1 \sum_{j=2}^n a_{1j} x_j + q_{\text{rest}}(x_2, \dots, x_n)$$
  Complete the square:
  $$q = a_{11} \left( x_1 + \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 + q'(x_2, \dots, x_n)$$
  Set $y_1 = x_1 + \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j$, and repeat inductively on $q'(x_2, \dots, x_n)$.
- **Case 2 (All $a_{ii} = 0$, but some cross term $a_{ij} \neq 0$):**
  Make the non-singular substitution $x_i = u_i + u_j$, $x_j = u_i - u_j$, so $2 a_{ij} x_i x_j = 2 a_{ij}(u_i^2 - u_j^2)$, producing non-zero diagonal coefficients, and revert to Case 1.

#### Method 2: Orthogonal Diagonalization (Principal Axis Theorem)
By the Real Spectral Theorem, $A = Q \Lambda Q^T$ with $Q \in O(n)$ orthogonal ($Q^T = Q^{-1}$).
Letting $\vec{x} = Q \vec{y}$ gives:
$$q(\vec{x}) = \vec{x}^T A \vec{x} = (Q\vec{y})^T A (Q\vec{y}) = \vec{y}^T (Q^T A Q) \vec{y} = \vec{y}^T \Lambda \vec{y} = \sum_{i=1}^n \lambda_i y_i^2$$
This rotation eliminates cross-terms while geometrically preserving angles and distances!"""
            },
            {
                "id": "u8-sec4",
                "title": "Sylvester's Law of Inertia, Definiteness & Hermitian Forms",
                "content": r"""### 1. Sylvester's Law of Inertia

Let $q$ be a real quadratic form on an $n$-dimensional real vector space $V$.
Through an invertible change of variables $\vec{x} = P \vec{y}$, $q$ can always be brought into its **Canonical Form**:
$$q(\vec{y}) = y_1^2 + y_2^2 + \cdots + y_p^2 - y_{p+1}^2 - \cdots - y_{p+q}^2$$
where:
- $p$ is the number of positive squares (**positive index of inertia**).
- $q$ is the number of negative squares (**negative index of inertia**).
- $r = p + q$ is the **rank** of the quadratic form ($r = \text{rank}(A)$).
- $z = n - r$ is the **nullity** (number of missing variables).
- $s = p - q$ is the **signature** of the form.

#### Theorem 8.4 (Sylvester's Law of Inertia):
The integers $p$ and $q$ are **independent** of the choice of diagonalizing coordinate transformation.
They depend solely on the quadratic form $q$ itself.

*Proof:*
Suppose there exist two non-singular changes of coordinates reducing $q$ to:
$$q(\vec{y}) = \sum_{i=1}^p y_i^2 - \sum_{j=1}^q y_{p+j}^2 \quad \text{and} \quad q(\vec{z}) = \sum_{i=1}^{p'} z_i^2 - \sum_{j=1}^{q'} z_{p'+j}^2$$
Assume, for contradiction, that $p > p'$.
Let $\beta = \{\vec{u}_1, \dots, \vec{u}_n\}$ be the basis in which $q$ has coordinates $\vec{y}$, and $\gamma = \{\vec{w}_1, \dots, \vec{w}_n\}$ the basis for $\vec{z}$.
Define two subspaces of $V$:
$$V^+ = \text{span}\{\vec{u}_1, \dots, \vec{u}_p\} \implies \dim V^+ = p$$
$$V^- = \text{span}\{\vec{w}_{p'+1}, \dots, \vec{w}_n\} \implies \dim V^- = n - p'$$
For any non-zero $\vec{v} \in V^+$: $q(\vec{v}) = y_1^2 + \cdots + y_p^2 > 0$.
For any $\vec{v} \in V^-$: $q(\vec{v}) = -z_{p'+1}^2 - \cdots - z_{p'+q'}^2 \le 0$.
Hence $V^+ \cap V^- = \{\vec{0}\}$.
By the dimension formula for subspace sums:
$$\dim(V^+ + V^-) = \dim V^+ + \dim V^- - \dim(V^+ \cap V^-) = p + (n - p') - 0 = n + (p - p')$$
Since $p > p'$, $n + (p - p') > n = \dim V$, which contradicts the fact that $V^+ + V^- \subseteq V$ cannot have dimension strictly exceeding $n$.
Therefore $p \le p'$. By symmetry, $p' \le p \implies p = p'$.
Since the rank $r = p + q = p' + q'$ is invariant (it is the rank of the matrix $A$), it follows that $q = q'$. $\blacksquare$

---

### 2. Definiteness Classification of Quadratic Forms

A real quadratic form $q(\vec{x}) = \vec{x}^T A \vec{x}$ is classified as:
1. **Positive Definite:** $q(\vec{x}) > 0$ for all $\vec{x} \neq \vec{0}$.
   - Spectrum: All eigenvalues $\lambda_i > 0$.
   - Inertia: $p = n, q = 0$.
2. **Positive Semidefinite:** $q(\vec{x}) \ge 0$ for all $\vec{x} \in \mathbb{R}^n$.
   - Spectrum: All eigenvalues $\lambda_i \ge 0$.
   - Inertia: $p \le n, q = 0$.
3. **Negative Definite:** $q(\vec{x}) < 0$ for all $\vec{x} \neq \vec{0}$.
   - Spectrum: All eigenvalues $\lambda_i < 0$.
   - Inertia: $p = 0, q = n$.
4. **Negative Semidefinite:** $q(\vec{x}) \le 0$ for all $\vec{x} \in \mathbb{R}^n$.
   - Spectrum: All eigenvalues $\lambda_i \le 0$.
   - Inertia: $p = 0, q \le n$.
5. **Indefinite:** $q(\vec{x})$ takes both strictly positive and strictly negative values.
   - Spectrum: There exists at least one $\lambda_i > 0$ and at least one $\lambda_j < 0$.
   - Inertia: $p > 0$ and $q > 0$.

---

### 3. Sylvester's Leading Principal Minors Criterion

The **Leading Principal Submatrices** of $A = (a_{ij}) \in M_n(\mathbb{R})$ are:
$$A_k = \begin{pmatrix} a_{11} & \cdots & a_{1k} \\ \vdots & \ddots & \vdots \\ a_{k1} & \cdots & a_{kk} \end{pmatrix}, \quad k = 1, 2, \dots, n$$
Their determinants $\Delta_k = \det(A_k)$ are called the **Leading Principal Minors**.

#### Theorem 8.5 (Sylvester's Criterion):
1. $A$ is **Positive Definite** if and only if all leading principal minors are strictly positive:
   $$\Delta_1 > 0, \quad \Delta_2 > 0, \quad \Delta_3 > 0, \quad \dots, \quad \Delta_n = \det(A) > 0$$
2. $A$ is **Negative Definite** if and only if the leading principal minors alternate in sign, starting negative:
   $$(-1)^k \Delta_k > 0 \iff \Delta_1 < 0, \quad \Delta_2 > 0, \quad \Delta_3 < 0, \quad \Delta_4 > 0, \quad \dots$$

---

### 4. Hermitian Forms

Over the complex field $\mathbb{C}$, the analogue of a symmetric bilinear form is a **Hermitian Form** $H: V \times V \to \mathbb{C}$:
1. $H(c_1 \vec{u}_1 + c_2 \vec{u}_2, \, \vec{v}) = c_1 H(\vec{u}_1, \vec{v}) + c_2 H(\vec{u}_2, \vec{v})$
2. $H(\vec{v}, \vec{u}) = \overline{H(\vec{u}, \vec{v})}$

The associated complex quadratic form is:
$$q(\vec{x}) = H(\vec{x}, \vec{x}) = \vec{x}^\dagger A \vec{x}$$
where $A^\dagger = A$ is a **Hermitian matrix**.
Crucially, $q(\vec{x})$ is **always real-valued**:
$$\overline{q(\vec{x})} = \overline{\vec{x}^\dagger A \vec{x}} = (\vec{x}^\dagger A \vec{x})^\dagger = \vec{x}^\dagger A^\dagger \vec{x} = \vec{x}^\dagger A \vec{x} = q(\vec{x})$$

Under a non-singular complex change of basis $\vec{x} = P \vec{y}$, the matrix transforms by **Hermitian Congruence**:
$$A' = P^\dagger A P$$
Sylvester's Law of Inertia holds identically for Hermitian forms: every Hermitian matrix is congruent to a diagonal matrix with entries $\{+1, -1, 0\}$, with the counts of $+1$ and $-1$ being invariant."""
            }
        ],
        "problems": [
            {
                "tier": 1,
                "title": "Lagrange Reduction and Definiteness of a Quadratic Form",
                "statement": r"""Consider the real quadratic form on $\mathbb{R}^3$:
$$q(x_1, x_2, x_3) = x_1^2 + 5x_2^2 + 11x_3^2 + 4x_1 x_2 - 2x_1 x_3 - 10x_2 x_3$$
1. Express $q$ in matrix form $q(\vec{x}) = \vec{x}^T A \vec{x}$, identifying the symmetric matrix $A$.
2. Diagonalize $q$ using Lagrange's method of completing the square, finding the linear coordinate transformation $\vec{y} = C \vec{x}$.
3. Determine the canonical form, rank, positive index of inertia $p$, negative index of inertia $q$, signature, and classify the definiteness of $q$ using both the canonical form and Sylvester's criterion.""",
                "derivation": r"""### Step 1: Matrix Representation

The quadratic form is:
$$q(\vec{x}) = x_1^2 + 5x_2^2 + 11x_3^2 + 4x_1 x_2 - 2x_1 x_3 - 10x_2 x_3$$
The diagonal entries of $A$ are the coefficients of $x_i^2$:
$$a_{11} = 1, \quad a_{22} = 5, \quad a_{33} = 11$$
The off-diagonal entries are half of the coefficients of the cross-terms:
$$a_{12} = a_{21} = 2, \quad a_{13} = a_{31} = -1, \quad a_{23} = a_{32} = -5$$
Thus:
$$A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & -5 \\ -1 & -5 & 11 \end{pmatrix}$$

---

### Step 2: Lagrange's Method of Completing the Square

#### Group terms involving $x_1$:
$$q = x_1^2 + 2x_1(2x_2 - x_3) + 5x_2^2 + 11x_3^2 - 10x_2 x_3$$
Complete the square in $x_1$:
$$q = \left[ x_1 + (2x_2 - x_3) \right]^2 - (2x_2 - x_3)^2 + 5x_2^2 + 11x_3^2 - 10x_2 x_3$$
Expand the subtracted term:
$$(2x_2 - x_3)^2 = 4x_2^2 - 4x_2 x_3 + x_3^2$$
Substitute:
$$\begin{aligned}
q &= (x_1 + 2x_2 - x_3)^2 - (4x_2^2 - 4x_2 x_3 + x_3^2) + 5x_2^2 + 11x_3^2 - 10x_2 x_3 \\
&= (x_1 + 2x_2 - x_3)^2 + (5 - 4)x_2^2 + (-10 + 4)x_2 x_3 + (11 - 1)x_3^2 \\
&= (x_1 + 2x_2 - x_3)^2 + x_2^2 - 6x_2 x_3 + 10x_3^2
\end{aligned}$$

#### Complete the square in $x_2$:
$$x_2^2 - 6x_2 x_3 + 10x_3^2 = (x_2 - 3x_3)^2 - 9x_3^2 + 10x_3^2 = (x_2 - 3x_3)^2 + x_3^2$$
Substituting back:
$$q = (x_1 + 2x_2 - x_3)^2 + (x_2 - 3x_3)^2 + x_3^2$$

#### Linear Coordinate Transformation:
Define the new coordinates:
$$\begin{aligned}
y_1 &= x_1 + 2x_2 - x_3 \\
y_2 &= x_2 - 3x_3 \\
y_3 &= x_3
\end{aligned}$$
In matrix form $\vec{y} = C \vec{x}$:
$$C = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{pmatrix}$$
Since $\det(C) = 1 \neq 0$, $C$ is strictly non-singular.

---

### Step 3: Canonical Form, Inertia and Definiteness

The diagonalized form is:
$$q(\vec{y}) = y_1^2 + y_2^2 + y_3^2$$
All coefficients are $+1$. Therefore:
- **Rank:** $r = 3$ (full rank).
- **Positive index of inertia:** $p = 3$.
- **Negative index of inertia:** $q = 0$.
- **Signature:** $s = p - q = 3 - 0 = 3$.
- Since $p = n = 3$, $q(\vec{x}) > 0$ for all $\vec{x} \neq \vec{0}$, so $q$ is **Positive Definite**.

#### Cross-Verification via Sylvester's Criterion:
Compute the leading principal minors of $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & -5 \\ -1 & -5 & 11 \end{pmatrix}$:
$$\Delta_1 = \det(a_{11}) = 1 > 0$$
$$\Delta_2 = \det \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} = 1\cdot 5 - 2\cdot 2 = 5 - 4 = 1 > 0$$
$$\Delta_3 = \det(A) = 1\cdot(5\cdot 11 - (-5)\cdot(-5)) - 2\cdot(2\cdot 11 - (-5)\cdot(-1)) + (-1)\cdot(2\cdot(-5) - 5\cdot(-1))$$
$$\Delta_3 = 1\cdot(55 - 25) - 2\cdot(22 - 5) - 1\cdot(-10 + 5) = 30 - 2(17) - (-5) = 30 - 34 + 5 = 1 > 0$$
Since $\Delta_1 = 1 > 0$, $\Delta_2 = 1 > 0$, and $\Delta_3 = 1 > 0$, by Sylvester's criterion the matrix $A$ is **strictly Positive Definite**! Both methods agree completely.""",
                "answer": r"""Symmetric matrix $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & -5 \\ -1 & -5 & 11 \end{pmatrix}$. Completed squares: $q = y_1^2 + y_2^2 + y_3^2$ where $y_1 = x_1 + 2x_2 - x_3, y_2 = x_2 - 3x_3, y_3 = x_3$. Rank $r=3$, positive index $p=3$, negative index $q=0$, signature $s=3$. Definiteness: strictly Positive Definite (confirmed by $\Delta_1 = 1, \Delta_2 = 1, \Delta_3 = 1 > 0$)."""
            },
            {
                "tier": 2,
                "title": "Jordan Canonical Form and Generalized Eigenvectors of a Defective Matrix",
                "statement": r"""Consider the real matrix:
$$A = \begin{pmatrix} 3 & 1 & 0 \\ -1 & 1 & 0 \\ 3 & 2 & 2 \end{pmatrix}$$
1. Compute the characteristic polynomial $p_A(\lambda)$ and find all eigenvalues.
2. Determine the geometric multiplicity and generalized eigenspaces for each eigenvalue.
3. Find the Jordan Canonical Form $J$ and determine the minimal polynomial $m_A(\lambda)$.
4. Construct an invertible transition matrix $P$ such that $P^{-1} A P = J$.""",
                "derivation": r"""### Step 1: Characteristic Polynomial

$$\det(A - \lambda I) = \det \begin{pmatrix} 3 - \lambda & 1 & 0 \\ -1 & 1 - \lambda & 0 \\ 3 & 2 & 2 - \lambda \end{pmatrix} = 0$$
Expanding along the third column:
$$\det(A - \lambda I) = (2 - \lambda) \cdot \det \begin{pmatrix} 3 - \lambda & 1 \\ -1 & 1 - \lambda \end{pmatrix}$$
$$(2 - \lambda) \left[ (3 - \lambda)(1 - \lambda) - (-1)(1) \right] = (2 - \lambda) (\lambda^2 - 4\lambda + 3 + 1) = (2 - \lambda)(\lambda^2 - 4\lambda + 4) = (2 - \lambda)(\lambda - 2)^2 = -(\lambda - 2)^3$$
Thus there is a single eigenvalue:
$$\lambda = 2 \quad \text{with algebraic multiplicity } a = 3$$

---

### Step 2: Geometric Multiplicity and Jordan Block Sizes

Compute $(A - 2I)$:
$$A - 2I = \begin{pmatrix} 1 & 1 & 0 \\ -1 & -1 & 0 \\ 3 & 2 & 0 \end{pmatrix}$$
Row reduce $(A - 2I)$:
- $R_2 \to R_2 + R_1$: $(0, 0, 0)$
- $R_3 \to R_3 - 3R_1$: $(0, -1, 0) \to (0, 1, 0)$
- Back-substitute into $R_1$: $(1, 0, 0)$
Row echelon form has 2 non-zero rows: $\text{rank}(A - 2I) = 2$.
$$\text{Geometric multiplicity } g_2 = \dim \ker(A - 2I) = 3 - \text{rank}(A - 2I) = 3 - 2 = 1$$
Since $g_2 = 1 < 3$, $A$ is defective and non-diagonalizable.
Because there is only $g_2 = 1$ Jordan block for $\lambda = 2$, that block must have size $3 \times 3$:
$$J = J_3(2) = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$
The minimal polynomial is $m_A(\lambda) = (\lambda - 2)^3$.

---

### Step 3: Construction of the Jordan Chain

We seek a Jordan chain $\{\vec{v}_1, \vec{v}_2, \vec{v}_3\}$ satisfying:
$$\begin{aligned}
(A - 2I)\vec{v}_3 &= \vec{v}_2 \\
(A - 2I)\vec{v}_2 &= \vec{v}_1 \\
(A - 2I)\vec{v}_1 &= \vec{0}
\end{aligned}$$
where $\vec{v}_3$ is a generalized eigenvector of rank 3:
$$(A - 2I)^3 \vec{v}_3 = \vec{0} \quad \text{and} \quad (A - 2I)^2 \vec{v}_3 \neq \vec{0}$$

Compute $(A - 2I)^2$:
$$(A - 2I)^2 = \begin{pmatrix} 1 & 1 & 0 \\ -1 & -1 & 0 \\ 3 & 2 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ -1 & -1 & 0 \\ 3 & 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{pmatrix}$$
Note that $(A - 2I)^3 = O_{3 \times 3}$.

We choose $\vec{v}_3 = (x, y, z)^T$ such that $(A - 2I)^2 \vec{v}_3 \neq \vec{0}$:
$$(A - 2I)^2 \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ x + y \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
We require $x + y \neq 0$. Choose:
$$\vec{v}_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$
Now propagate down the chain:
$$\vec{v}_2 = (A - 2I)\vec{v}_3 = \begin{pmatrix} 1 & 1 & 0 \\ -1 & -1 & 0 \\ 3 & 2 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$$
$$\vec{v}_1 = (A - 2I)\vec{v}_2 = \begin{pmatrix} 1 & 1 & 0 \\ -1 & -1 & 0 \\ 3 & 2 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1(1) + 1(-1) \\ -1(1) - 1(-1) \\ 3(1) + 2(-1) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
Notice that $\vec{v}_1 = (0, 0, 1)^T$ satisfies $(A - 2I)\vec{v}_1 = \vec{0}$, so it is an eigenvector. $\checkmark$

---

### Step 4: Invertible Transition Matrix $P$ and Verification

The transition matrix $P$ is formed by placing the chain vectors as columns:
$$P = \begin{pmatrix} \vec{v}_1 & \vec{v}_2 & \vec{v}_3 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & 0 \\ 1 & 3 & 0 \end{pmatrix}$$
Compute $\det(P)$:
Expanding along the third column:
$$\det(P) = 1 \cdot \det \begin{pmatrix} 0 & -1 \\ 1 & 3 \end{pmatrix} = 1 \cdot (0 - (-1)) = 1 \neq 0 \implies P \text{ is invertible!}$$

#### Verify $A P = P J$:
Compute $A P$:
$$A P = \begin{pmatrix} 3 & 1 & 0 \\ -1 & 1 & 0 \\ 3 & 2 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & 0 \\ 1 & 3 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 3(1)+1(-1) & 3(1) \\ 0 & -1(1)+1(-1) & -1(1) \\ 2 & 3(1)+2(-1)+2(3) & 3(1) \end{pmatrix} = \begin{pmatrix} 0 & 2 & 3 \\ 0 & -2 & -1 \\ 2 & 7 & 3 \end{pmatrix}$$
Compute $P J$:
$$P J = \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & 0 \\ 1 & 3 & 0 \end{pmatrix} \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 0(1)+1(2) & 1(1)+1(2) \\ 0 & 0(1)-1(2) & -1(1)+0(2) \\ 1(2) & 1(1)+3(2) & 3(1)+0(2) \end{pmatrix} = \begin{pmatrix} 0 & 2 & 3 \\ 0 & -2 & -1 \\ 2 & 7 & 3 \end{pmatrix}$$
Since $A P = P J$ identically, $P^{-1} A P = J$. $\checkmark$""",
                "answer": r"""Eigenvalue $\lambda = 2$ with algebraic multiplicity $a = 3$ and geometric multiplicity $g = 1$. JCF is a single block $J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$; minimal polynomial $m_A(\lambda) = (\lambda - 2)^3$. Transition matrix $P = \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & 0 \\ 1 & 3 & 0 \end{pmatrix}$ satisfying $P^{-1} A P = J$."""
            },
            {
                "tier": 3,
                "title": "Complete Rigorous Proof of Sylvester's Law of Inertia",
                "statement": r"""Provide a complete, unskipped proof of **Sylvester's Law of Inertia**:
Let $q: V \to \mathbb{R}$ be a real quadratic form on an $n$-dimensional real vector space $V$.
If $q$ is reduced to diagonal canonical forms by two invertible coordinate transformations:
$$q(\vec{y}) = \sum_{i=1}^p y_i^2 - \sum_{j=1}^q y_{p+j}^2 \quad \text{and} \quad q(\vec{z}) = \sum_{i=1}^{p'} z_i^2 - \sum_{j=1}^{q'} z_{p'+j}^2$$
prove that:
$$p = p' \quad \text{and} \quad q = q'$$
using subspace dimension arguments and the Grassmann dimension identity.""",
                "derivation": r"""### Mathematical Setup

Let $V$ be an $n$-dimensional real vector space, and let $q: V \to \mathbb{R}$ be a quadratic form with associated symmetric bilinear form $B: V \times V \to \mathbb{R}$ such that $q(\vec{v}) = B(\vec{v}, \vec{v})$.
Suppose there exist two bases $\mathcal{B} = \{\vec{u}_1, \dots, \vec{u}_n\}$ and $\mathcal{C} = \{\vec{w}_1, \dots, \vec{w}_n\}$ of $V$ such that for any vector $\vec{v} \in V$:
- In basis $\mathcal{B}$, with $\vec{v} = \sum_{i=1}^n y_i \vec{u}_i$:
  $$q(\vec{v}) = y_1^2 + \cdots + y_p^2 - y_{p+1}^2 - \cdots - y_{p+q}^2$$
  where $r = p + q \le n$ is the rank of the matrix of $B$ in basis $\mathcal{B}$.
- In basis $\mathcal{C}$, with $\vec{v} = \sum_{i=1}^n z_i \vec{w}_i$:
  $$q(\vec{v}) = z_1^2 + \cdots + z_{p'}^2 - z_{p'+1}^2 - \cdots - z_{p'+q'}^2$$
  where $r' = p' + q' \le n$ is the rank of the matrix of $B$ in basis $\mathcal{C}$.

---

### Step 1: Invariance of Rank ($r = r'$)

Let $A = [B]_\mathcal{B}$ and $A' = [B]_\mathcal{C}$ be the matrices of the bilinear form in bases $\mathcal{B}$ and $\mathcal{C}$, respectively.
If $P$ is the transition matrix from $\mathcal{B}$ to $\mathcal{C}$, then:
$$A' = P^T A P$$
Since $P$ is invertible ($\det(P) \neq 0$), $P^T$ is also invertible.
Congruent matrices have identical rank:
$$\text{rank}(A') = \text{rank}(P^T A P) = \text{rank}(A)$$
From the diagonal representations:
$$\text{rank}(A) = p + q \quad \text{and} \quad \text{rank}(A') = p' + q'$$
Therefore:
$$p + q = p' + q' = r$$

---

### Step 2: Proof that $p = p'$

We show that the assumption $p > p'$ leads to a contradiction.
Assume, without loss of generality, that $p > p'$.

Define two linear subspaces of $V$:
1. **The Positive Subspace $V^+$:**
   $$V^+ = \text{span}\{\vec{u}_1, \dots, \vec{u}_p\} \subset V$$
   Since $\{\vec{u}_1, \dots, \vec{u}_p\}$ is a subset of the basis $\mathcal{B}$, it is linearly independent.
   Therefore:
   $$\dim V^+ = p$$
   For any non-zero vector $\vec{v} \in V^+$, its coordinates in basis $\mathcal{B}$ satisfy $y_{p+1} = \cdots = y_n = 0$ and at least one $y_i \neq 0$ ($1 \le i \le p$).
   Thus:
   $$q(\vec{v}) = y_1^2 + y_2^2 + \cdots + y_p^2 > 0 \quad \text{for all } \vec{v} \in V^+ \setminus \{\vec{0}\}$$

2. **The Non-Positive Subspace $W^-$:**
   $$W^- = \text{span}\{\vec{w}_{p'+1}, \vec{w}_{p'+2}, \dots, \vec{w}_n\} \subset V$$
   Since $\{\vec{w}_{p'+1}, \dots, \vec{w}_n\}$ is a subset of the basis $\mathcal{C}$, it is linearly independent.
   Therefore:
   $$\dim W^- = n - p'$$
   For any vector $\vec{w} \in W^-$, its coordinates in basis $\mathcal{C}$ satisfy $z_1 = \cdots = z_{p'} = 0$.
   Thus:
   $$q(\vec{w}) = -z_{p'+1}^2 - \cdots - z_{p'+q'}^2 + 0 \cdot z_{p'+q'+1}^2 + \cdots \le 0 \quad \text{for all } \vec{w} \in W^-$$

---

### Step 3: Intersection of $V^+$ and $W^-$

Consider the subspace intersection $V^+ \cap W^-$.
Let $\vec{x} \in V^+ \cap W^-$.
- Since $\vec{x} \in V^+$, if $\vec{x} \neq \vec{0}$, then $q(\vec{x}) > 0$.
- Since $\vec{x} \in W^-$, $q(\vec{x}) \le 0$.

A real number cannot be simultaneously strictly positive and non-positive!
Therefore, the only vector that can belong to both subspaces is the zero vector:
$$V^+ \cap W^- = \{\vec{0}\}$$
Consequently:
$$\dim(V^+ \cap W^-) = 0$$

---

### Step 4: Grassmann Dimension Formula and Contradiction

By the Grassmann dimension formula for subspace sums:
$$\dim(V^+ + W^-) = \dim V^+ + \dim W^- - \dim(V^+ \cap W^-)$$
Substituting the known dimensions:
$$\dim(V^+ + W^-) = p + (n - p') - 0 = n + (p - p')$$
Since $V^+ \subseteq V$ and $W^- \subseteq V$, the sum subspace $V^+ + W^-$ is a subspace of $V$:
$$V^+ + W^- \subseteq V \implies \dim(V^+ + W^-) \le \dim V = n$$
Therefore:
$$n + (p - p') \le n \implies p - p' \le 0 \implies p \le p'$$
This directly contradicts our initial assumption that $p > p'$!

By entirely symmetric reasoning, exchanging the roles of $\mathcal{B}$ and $\mathcal{C}$, the assumption $p' > p$ similarly leads to the contradiction $p' \le p$.

Therefore, we must have:
$$p = p'$$

---

### Step 5: Proof that $q = q'$

From Step 1, the total rank is invariant under congruent change of coordinates:
$$p + q = p' + q'$$
Since $p = p'$, subtracting $p$ from both sides yields:
$$q = q'$$

Hence both the positive index of inertia $p$ and the negative index of inertia $q$ are strictly invariant under arbitrary invertible coordinate transformations. The proof of Sylvester's Law of Inertia is complete. $\blacksquare$""",
                "answer": r"""Complete rigorous proof established: (1) Invariance of matrix rank under congruence proves $p + q = p' + q'$; (2) Defining positive subspace $V^+$ ($\dim = p$) and non-positive subspace $W^-$ ($\dim = n - p'$) shows $V^+ \cap W^- = \{\vec{0}\}$; (3) Grassmann formula gives $\dim(V^+ + W^-) = n + p - p' \le n \implies p \le p'$, which by symmetry forces $p = p'$ and consequently $q = q'$."""
            }
        ]
    }

if __name__ == "__main__":
    u7 = build_unit_7()
    u8 = build_unit_8()
    with open("la_u7.json", "w", encoding="utf-8") as f:
        json.dump(u7, f, indent=2)
    with open("la_u8.json", "w", encoding="utf-8") as f:
        json.dump(u8, f, indent=2)
    print("Units 7 and 8 successfully built: la_u7.json, la_u8.json")
