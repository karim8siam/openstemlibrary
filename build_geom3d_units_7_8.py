import json

def build_unit_7():
    return {
        "id": "geom3d-u7",
        "title": "Unit 7: Vector Algebra in Space & Multi-Vector Products",
        "description": "Exhaustive treatment of vector products in Euclidean 3-space: scalar product, vector cross product, scalar triple product, vector triple product (BAC-CAB theorem), and higher-order 4-vector identities.",
        "sections": [
            {
                "id": "sec-geom3d-7-1",
                "title": "7.1 Inner and Outer Products in R^3",
                "content": r"""Vector algebra in three-dimensional Euclidean space $\mathbb{R}^3$ forms the foundational language of mathematical physics, mechanics, and geometric analysis.

---

### 1. The Dot (Scalar Inner) Product

Given two vectors $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$, their **scalar product** is defined geometrically as:

$$\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos\theta$$

where $\theta \in [0, \pi]$ is the interior angle between them. In orthonormal Cartesian components:

$$\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3$$

#### Key Properties:
- **Commutativity:** $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$.
- **Magnitude:** $|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}}$.
- **Orthogonality:** $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$ (for non-zero vectors).
- **Cauchy-Schwarz Inequality:** $|\vec{a} \cdot \vec{b}| \le |\vec{a}| |\vec{b}|$, with equality if and only if $\vec{a} \parallel \vec{b}$.

---

### 2. The Cross (Vector Outer) Product

The **vector product** $\vec{a} \times \vec{b}$ produces a vector perpendicular to both $\vec{a}$ and $\vec{b}$, oriented according to the right-hand rule:

$$\vec{a} \times \vec{b} = |\vec{a}| |\vec{b}| \sin\theta \, \hat{n}$$

where $\hat{n}$ is the unit normal vector such that $(\vec{a}, \vec{b}, \hat{n})$ forms a right-handed orthogonal triad.

In Cartesian component form:

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = (a_2 b_3 - a_3 b_2)\hat{i} + (a_3 b_1 - a_1 b_3)\hat{j} + (a_1 b_2 - a_2 b_1)\hat{k}$$

#### Key Properties:
- **Anti-commutativity:** $\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$.
- **Collinearity:** $\vec{a} \parallel \vec{b} \iff \vec{a} \times \vec{b} = \vec{0}$.
- **Geometric Area:** The magnitude $|\vec{a} \times \vec{b}|$ equals the area of the parallelogram spanned by $\vec{a}$ and $\vec{b}$.

---

### 3. Lagrange's Identity

**Theorem (Lagrange's Identity):**  
For any vectors $\vec{a}, \vec{b} \in \mathbb{R}^3$:

$$|\vec{a} \times \vec{b}|^2 = |\vec{a}|^2 |\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2$$

#### Proof:
From geometric definitions:
$$\text{LHS} = (|\vec{a}| |\vec{b}| \sin\theta)^2 = |\vec{a}|^2 |\vec{b}|^2 \sin^2\theta$$
$$= |\vec{a}|^2 |\vec{b}|^2 (1 - \cos^2\theta) = |\vec{a}|^2 |\vec{b}|^2 - |\vec{a}|^2 |\vec{b}|^2 \cos^2\theta$$
$$= |\vec{a}|^2 |\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2 = \text{RHS} \quad \blacksquare$$"""
            },
            {
                "id": "sec-geom3d-7-2",
                "title": "7.2 The Scalar Triple Product (Box Product)",
                "content": r"""### 1. Definition and Determinant Representation

The **scalar triple product** (or **box product**) of three vectors $\vec{a}, \vec{b}, \vec{c} \in \mathbb{R}^3$ is defined as:

$$[\vec{a}, \vec{b}, \vec{c}] \equiv \vec{a} \cdot (\vec{b} \times \vec{c})$$

Let $\vec{a} = (a_1, a_2, a_3)$, $\vec{b} = (b_1, b_2, b_3)$, and $\vec{c} = (c_1, c_2, c_3)$. Expanding via the dot product:

$$\vec{a} \cdot (\vec{b} \times \vec{c}) = a_1 (b_2 c_3 - b_3 c_2) + a_2 (b_3 c_1 - b_1 c_3) + a_3 (b_1 c_2 - b_2 c_1)$$

This is precisely the expansion of the $3 \times 3$ determinant:

$$[\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}$$

---

### 2. Geometric Interpretation: Parallelepiped and Tetrahedral Volume

- **Volume of a Parallelepiped:**  
  The base of the parallelepiped formed by $\vec{b}$ and $\vec{c}$ has area $A = |\vec{b} \times \vec{c}|$. The unit normal to the base is $\hat{n} = \frac{\vec{b} \times \vec{c}}{|\vec{b} \times \vec{c}|}$.  
  The height $h$ is the projection of $\vec{a}$ onto $\hat{n}$: $h = |\vec{a} \cdot \hat{n}|$.  
  Hence, the volume is:
  $$V_{para} = A \cdot h = |\vec{b} \times \vec{c}| \frac{|\vec{a} \cdot (\vec{b} \times \vec{c})|}{|\vec{b} \times \vec{c}|} = |[\vec{a}, \vec{b}, \vec{c}]|$$

- **Volume of a Tetrahedron:**  
  A tetrahedron with coterminous edges $\vec{a}, \vec{b}, \vec{c}$ has volume equal to one-sixth of the parallelepiped:
  $$V_{tet} = \frac{1}{6} |[\vec{a}, \vec{b}, \vec{c}]|$$

---

### 3. Cyclic Symmetries and Coplanarity

From the determinant properties under row swaps:

$$[\vec{a}, \vec{b}, \vec{c}] = [\vec{b}, \vec{c}, \vec{a}] = [\vec{c}, \vec{a}, \vec{b}]$$
$$[\vec{a}, \vec{b}, \vec{c}] = -[\vec{b}, \vec{a}, \vec{c}] = -[\vec{a}, \vec{c}, \vec{b}] = -[\vec{c}, \vec{b}, \vec{a}]$$

> **Interchange of Dot and Cross:**  
> $$\vec{a} \cdot (\vec{b} \times \vec{c}) = (\vec{a} \times \vec{b}) \cdot \vec{c}$$

- **Condition of Coplanarity:**  
  Three vectors $\vec{a}, \vec{b}, \vec{c}$ are coplanar if and only if their scalar triple product vanishes:
  $$[\vec{a}, \vec{b}, \vec{c}] = 0$$"""
            },
            {
                "id": "sec-geom3d-7-3",
                "title": "7.3 The Vector Triple Product & Higher-Order Identities",
                "content": r"""### 1. The Vector Triple Product (BAC-CAB Theorem)

Given three vectors $\vec{a}, \vec{b}, \vec{c}$, their **vector triple product** is $\vec{a} \times (\vec{b} \times \vec{c})$.

**Theorem (The BAC-CAB Rule):**  
$$\mathbf{\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}}$$

#### Proof:
1. **Geometric Orientation:** The vector $\vec{b} \times \vec{c}$ is perpendicular to the plane spanned by $\vec{b}$ and $\vec{c}$. Therefore, $\vec{a} \times (\vec{b} \times \vec{c})$ is perpendicular to $\vec{b} \times \vec{c}$, which implies it must lie in the plane of $\vec{b}$ and $\vec{c}$.  
   Hence, there exist scalars $\lambda, \mu$ such that:
   $$\vec{a} \times (\vec{b} \times \vec{c}) = \lambda \vec{b} + \mu \vec{c}$$

2. **Coordinate Setup:** Without loss of generality, choose an orthonormal coordinate system such that:
   - The $x$-axis lies along $\vec{b}$: $\vec{b} = (b_1, 0, 0)$.
   - The $xy$-plane contains $\vec{c}$: $\vec{c} = (c_1, c_2, 0)$.
   - $\vec{a} = (a_1, a_2, a_3)$ is general.

3. **Compute the Cross Products:**
   $$\vec{b} \times \vec{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ b_1 & 0 & 0 \\ c_1 & c_2 & 0 \end{vmatrix} = (0)\hat{i} + (0)\hat{j} + (b_1 c_2)\hat{k} = (0, 0, b_1 c_2)$$

   Now evaluate $\vec{a} \times (\vec{b} \times \vec{c})$:
   $$\vec{a} \times (\vec{b} \times \vec{c}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ 0 & 0 & b_1 c_2 \end{vmatrix} = (a_2 b_1 c_2)\hat{i} - (a_1 b_1 c_2)\hat{j} + (0)\hat{k}$$

4. **Compute RHS:**
   $$\vec{a} \cdot \vec{c} = a_1 c_1 + a_2 c_2$$
   $$\vec{a} \cdot \vec{b} = a_1 b_1$$
   $$(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} = (a_1 c_1 + a_2 c_2)(b_1 \hat{i}) - (a_1 b_1)(c_1 \hat{i} + c_2 \hat{j})$$
   $$= (a_1 b_1 c_1 + a_2 b_1 c_2 - a_1 b_1 c_1)\hat{i} - (a_1 b_1 c_2)\hat{j}$$
   $$= (a_2 b_1 c_2)\hat{i} - (a_1 b_1 c_2)\hat{j}$$

The LHS and RHS are identical in every component. Since the choice of coordinate axes is arbitrary, the result holds universally for all vectors in $\mathbb{R}^3$. $\blacksquare$

---

### 2. Jacobi's Identity

Summing cyclic permutations of the vector triple product:

$$\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$$
$$\vec{b} \times (\vec{c} \times \vec{a}) = (\vec{b} \cdot \vec{a})\vec{c} - (\vec{b} \cdot \vec{c})\vec{a}$$
$$\vec{c} \times (\vec{a} \times \vec{b}) = (\vec{c} \cdot \vec{b})\vec{a} - (\vec{c} \cdot \vec{a})\vec{b}$$

Summing all three equations:

$$\mathbf{\vec{a} \times (\vec{b} \times \vec{c}) + \vec{b} \times (\vec{c} \times \vec{a}) + \vec{c} \times (\vec{a} \times \vec{b}) = \vec{0}}$$

This is **Jacobi's Identity**, proving that the Lie algebra of 3D rotations $(\mathbb{R}^3, \times)$ satisfies the Jacobi relation.

---

### 3. Products of Four Vectors

1. **Scalar Product of Four Vectors:**
   $$(\vec{a} \times \vec{b}) \cdot (\vec{c} \times \vec{d}) = (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c}) = \begin{vmatrix} \vec{a} \cdot \vec{c} & \vec{a} \cdot \vec{d} \\ \vec{b} \cdot \vec{c} & \vec{b} \cdot \vec{d} \end{vmatrix}$$

2. **Vector Product of Four Vectors:**
   $$(\vec{a} \times \vec{b}) \times (\vec{c} \times \vec{d}) = [\vec{a}, \vec{b}, \vec{d}]\vec{c} - [\vec{a}, \vec{b}, \vec{c}]\vec{d} = [\vec{a}, \vec{c}, \vec{d}]\vec{b} - [\vec{b}, \vec{c}, \vec{d}]\vec{a}$$"""
            }
        ],
        "simulations": [
            {
                "id": "sim_geom3d_vector_products",
                "title": "3D Interactive Scalar & Vector Triple Products Engine",
                "description": "Manipulate 3D vectors a, b, and c in real time. Inspect the spanned parallelepiped, cross products, and visualize the BAC-CAB decomposition vector dynamically.",
                "controls": [
                    {"param": "ax", "label": "Vector a X", "min": -3, "max": 3, "step": 0.5, "default": 2},
                    {"param": "ay", "label": "Vector a Y", "min": -3, "max": 3, "step": 0.5, "default": 1},
                    {"param": "bx", "label": "Vector b X", "min": -3, "max": 3, "step": 0.5, "default": -1},
                    {"param": "bz", "label": "Vector b Z", "min": -3, "max": 3, "step": 0.5, "default": 2}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-geom3d-7-1",
                "tier": 1,
                "title": "Computation of Box Product and Parallelepiped Volume",
                "statement": r"""Given three vectors:
$$\vec{a} = 2\hat{i} - 3\hat{j} + \hat{k}, \qquad \vec{b} = \hat{i} + \hat{j} - 2\hat{k}, \qquad \vec{c} = 3\hat{i} - \hat{j} - \hat{k}$$
(a) Compute the scalar triple product $[\vec{a}, \vec{b}, \vec{c}]$.  
(b) Find the volume of the parallelepiped spanned by them.  
(c) Find the volume of the tetrahedron with coterminous edges $\vec{a}, \vec{b}, \vec{c}$.""",
                "solution": r"""**Step 1: Set up the determinant for $[\vec{a}, \vec{b}, \vec{c}]$**  
$$[\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} 2 & -3 & 1 \\ 1 & 1 & -2 \\ 3 & -1 & -1 \end{vmatrix}$$

---

**Step 2: Expand the determinant along the first row**  
$$[\vec{a}, \vec{b}, \vec{c}] = 2\begin{vmatrix} 1 & -2 \\ -1 & -1 \end{vmatrix} - (-3)\begin{vmatrix} 1 & -2 \\ 3 & -1 \end{vmatrix} + 1\begin{vmatrix} 1 & 1 \\ 3 & -1 \end{vmatrix}$$

Evaluate each $2 \times 2$ minor:
$$\begin{vmatrix} 1 & -2 \\ -1 & -1 \end{vmatrix} = 1(-1) - (-2)(-1) = -1 - 2 = -3$$
$$\begin{vmatrix} 1 & -2 \\ 3 & -1 \end{vmatrix} = 1(-1) - (-2)(3) = -1 + 6 = 5$$
$$\begin{vmatrix} 1 & 1 \\ 3 & -1 \end{vmatrix} = 1(-1) - 1(3) = -1 - 3 = -4$$

Substitute back:
$$[\vec{a}, \vec{b}, \vec{c}] = 2(-3) + 3(5) + 1(-4) = -6 + 15 - 4 = 5$$

---

**Step 3: Parallelepiped and Tetrahedral Volumes**  
- **Parallelepiped Volume:**
  $$V_{para} = |[\vec{a}, \vec{b}, \vec{c}]| = |5| = 5 \text{ cubic units}$$

- **Tetrahedron Volume:**
  $$V_{tet} = \frac{1}{6} |[\vec{a}, \vec{b}, \vec{c}]| = \frac{5}{6} \text{ cubic units}$$"""
            },
            {
                "id": "prob-geom3d-7-2",
                "tier": 2,
                "title": "Verification of the Vector Triple Product BAC-CAB Identity",
                "statement": r"""For the vectors:
$$\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}, \qquad \vec{b} = 2\hat{i} - \hat{j} + \hat{k}, \qquad \vec{c} = 3\hat{i} + \hat{j} - \hat{k}$$
compute explicitly both sides of the BAC-CAB theorem:
$$\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$$
and verify that they yield identically equal vectors.""",
                "solution": r"""**Step 1: Compute LHS by direct cross products**  
First, compute $\vec{b} \times \vec{c}$:
$$\vec{b} \times \vec{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -1 & 1 \\ 3 & 1 & -1 \end{vmatrix}$$
$$= \hat{i}((-1)(-1) - (1)(1)) - \hat{j}((2)(-1) - (1)(3)) + \hat{k}((2)(1) - (-1)(3))$$
$$= \hat{i}(1 - 1) - \hat{j}(-2 - 3) + \hat{k}(2 + 3) = 0\hat{i} + 5\hat{j} + 5\hat{k} = (0, 5, 5)$$

Next, evaluate $\vec{a} \times (\vec{b} \times \vec{c})$:
$$\vec{a} \times (\vec{b} \times \vec{c}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 0 & 5 & 5 \end{vmatrix}$$
$$= \hat{i}(2 \cdot 5 - 3 \cdot 5) - \hat{j}(1 \cdot 5 - 3 \cdot 0) + \hat{k}(1 \cdot 5 - 2 \cdot 0)$$
$$= \hat{i}(10 - 15) - \hat{j}(5 - 0) + \hat{k}(5 - 0) = -5\hat{i} - 5\hat{j} + 5\hat{k}$$

Thus:
$$\text{LHS} = (-5, -5, 5)$$

---

**Step 2: Compute RHS using dot products**  
Evaluate the dot products:
$$\vec{a} \cdot \vec{c} = 1(3) + 2(1) + 3(-1) = 3 + 2 - 3 = 2$$
$$\vec{a} \cdot \vec{b} = 1(2) + 2(-1) + 3(1) = 2 - 2 + 3 = 3$$

Now evaluate $(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$:
$$\text{RHS} = 2(2\hat{i} - \hat{j} + \hat{k}) - 3(3\hat{i} + \hat{j} - \hat{k})$$
$$= (4\hat{i} - 2\hat{j} + 2\hat{k}) - (9\hat{i} + 3\hat{j} - 3\hat{k})$$
$$= (4 - 9)\hat{i} + (-2 - 3)\hat{j} + (2 - (-3))\hat{k}$$
$$= -5\hat{i} - 5\hat{j} + 5\hat{k}$$

---

**Step 3: Conclusion**  
$$\text{LHS} = -5\hat{i} - 5\hat{j} + 5\hat{k} = \text{RHS}$$
The identity is fully verified."""
            },
            {
                "id": "prob-geom3d-7-3",
                "tier": 3,
                "title": "Proof of the Four-Vector Inner Product Identity",
                "statement": r"""Prove analytically for any four vectors $\vec{a}, \vec{b}, \vec{c}, \vec{d} \in \mathbb{R}^3$ that:
$$(\vec{a} \times \vec{b}) \cdot (\vec{c} \times \vec{d}) = \begin{vmatrix} \vec{a} \cdot \vec{c} & \vec{a} \cdot \vec{d} \\ \vec{b} \cdot \vec{c} & \vec{b} \cdot \vec{d} \end{vmatrix}$$
Hence, deduce Lagrange's Identity as a special corollary when $\vec{c} = \vec{a}$ and $\vec{d} = \vec{b}$.""",
                "solution": r"""**Step 1: Treat $\vec{c} \times \vec{d}$ as a single vector**  
Let $\vec{v} = \vec{c} \times \vec{d}$. The left-hand side is:
$$(\vec{a} \times \vec{b}) \cdot \vec{v}$$

Using the cyclic property of the scalar triple product:
$$(\vec{a} \times \vec{b}) \cdot \vec{v} = \vec{a} \cdot (\vec{b} \times \vec{v})$$

Substitute back $\vec{v} = \vec{c} \times \vec{d}$:
$$\text{LHS} = \vec{a} \cdot [\vec{b} \times (\vec{c} \times \vec{d})]$$

---

**Step 2: Apply the BAC-CAB Rule to $\vec{b} \times (\vec{c} \times \vec{d})$**  
$$\vec{b} \times (\vec{c} \times \vec{d}) = (\vec{b} \cdot \vec{d})\vec{c} - (\vec{b} \cdot \vec{c})\vec{d}$$

---

**Step 3: Take the dot product with $\vec{a}$**  
$$\vec{a} \cdot [(\vec{b} \cdot \vec{d})\vec{c} - (\vec{b} \cdot \vec{c})\vec{d}] = (\vec{b} \cdot \vec{d})(\vec{a} \cdot \vec{c}) - (\vec{b} \cdot \vec{c})(\vec{a} \cdot \vec{d})$$
$$= (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$$

---

**Step 4: Express as a $2 \times 2$ determinant**  
Notice that:
$$\begin{vmatrix} \vec{a} \cdot \vec{c} & \vec{a} \cdot \vec{d} \\ \vec{b} \cdot \vec{c} & \vec{b} \cdot \vec{d} \end{vmatrix} = (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$$

This precisely equals the expression derived in Step 3. $\blacksquare$

---

**Step 5: Deduction of Lagrange's Identity**  
Set $\vec{c} = \vec{a}$ and $\vec{d} = \vec{b}$:
$$(\vec{a} \times \vec{b}) \cdot (\vec{a} \times \vec{b}) = \begin{vmatrix} \vec{a} \cdot \vec{a} & \vec{a} \cdot \vec{b} \\ \vec{b} \cdot \vec{a} & \vec{b} \cdot \vec{b} \end{vmatrix}$$
$$|\vec{a} \times \vec{b}|^2 = |\vec{a}|^2 |\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2$$

This yields Lagrange's Identity immediately as a special case. $\blacksquare$"""
            }
        ]
    }

def build_unit_8():
    return {
        "id": "geom3d-u8",
        "title": "Unit 8: Applications of Vectors in Spatial Geometry",
        "description": "Advanced geometric applications of vector calculus: vector representations of lines and planes, intersection piercing points, distance theorems, and the theory of reciprocal vector triads.",
        "sections": [
            {
                "id": "sec-geom3d-8-1",
                "title": "8.1 Vector Formulation of Lines and Planes",
                "content": r"""The vector formalism condenses three-dimensional analytical geometry into coordinate-free, coordinate-independent equations.

---

### 1. Vector Equations of a Straight Line

1. **Line through a Point with a Given Direction:**  
   Passing through $\vec{a}$ parallel to $\vec{b}$:
   $$\mathbf{\vec{r} = \vec{a} + t\vec{b}} \quad (t \in \mathbb{R})$$
   In non-parametric form (since $\vec{r} - \vec{a} \parallel \vec{b}$):
   $$\mathbf{(\vec{r} - \vec{a}) \times \vec{b} = \vec{0}}$$

2. **Line Passing Through Two Points:**  
   Passing through $\vec{a}$ and $\vec{b}$:
   $$\mathbf{\vec{r} = (1 - t)\vec{a} + t\vec{b}} \quad \iff \quad (\vec{r} - \vec{a}) \times (\vec{b} - \vec{a}) = \vec{0}$$

---

### 2. Vector Equations of a Plane

1. **Point-Normal Form:**  
   Passing through $\vec{a}$ with normal vector $\vec{n}$:
   $$\mathbf{(\vec{r} - \vec{a}) \cdot \vec{n} = 0 \iff \vec{r} \cdot \vec{n} = d} \quad (d = \vec{a} \cdot \vec{n})$$

2. **Hesse Normal Form:**  
   Using unit normal $\hat{n}$ pointing away from the origin, $p$ is the perpendicular distance from origin:
   $$\mathbf{\vec{r} \cdot \hat{n} = p} \quad (p \ge 0)$$

3. **Plane Through Three Non-Collinear Points:**  
   Passing through $\vec{a}, \vec{b}, \vec{c}$. The vectors $\vec{r} - \vec{a}$, $\vec{b} - \vec{a}$, and $\vec{c} - \vec{a}$ are coplanar:
   $$(\vec{r} - \vec{a}) \cdot [(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a})] = 0$$
   Expanding:
   $$\mathbf{[\vec{r}, \vec{b}, \vec{c}] + [\vec{r}, \vec{c}, \vec{a}] + [\vec{r}, \vec{a}, \vec{b}] = [\vec{a}, \vec{b}, \vec{c}]}$$

---

### 3. Intersection of a Vector Line and a Vector Plane

Let the line be $\vec{r} = \vec{a} + t\vec{d}$ and the plane be $\vec{r} \cdot \vec{n} = q$.

Substitute the line parametrization into the plane equation:

$$(\vec{a} + t\vec{d}) \cdot \vec{n} = q \implies \vec{a} \cdot \vec{n} + t(\vec{d} \cdot \vec{n}) = q$$

If $\vec{d} \cdot \vec{n} \neq 0$ (line is not parallel to the plane):

$$\mathbf{t = \frac{q - \vec{a} \cdot \vec{n}}{\vec{d} \cdot \vec{n}}}$$

Substituting this unique parameter $t$ into $\vec{r}(t)$ yields the exact coordinates of the **piercing point**."""
            },
            {
                "id": "sec-geom3d-8-2",
                "title": "8.2 Spatial Distance Formulas via Vector Projection",
                "content": r"""Vector cross and dot products provide concise derivations of all spatial distance formulas.

---

### 1. Distance from a Point to a Straight Line

Let $P(\vec{p})$ be a point in space, and let the line be $\mathcal{L}: \vec{r} = \vec{a} + t\vec{d}$.

Consider the vector $\vec{aP} = \vec{p} - \vec{a}$. The area of the parallelogram formed by $\vec{p} - \vec{a}$ and the direction vector $\vec{d}$ is:

$$\text{Area} = |(\vec{p} - \vec{a}) \times \vec{d}|$$

On the other hand, $\text{Area} = \text{base} \times \text{height} = |\vec{d}| \cdot D$, where $D$ is the perpendicular distance from $P$ to the line. Equating:

$$\mathbf{D = \frac{|(\vec{p} - \vec{a}) \times \vec{d}|}{|\vec{d}|}}$$

---

### 2. Distance from a Point to a Plane

Let $P(\vec{p})$ be a point and let the plane be $\Pi: \vec{r} \cdot \vec{n} = d$.

Let $A(\vec{a})$ be any point on the plane, so that $\vec{a} \cdot \vec{n} = d$. The perpendicular distance $D$ is the absolute value of the scalar projection of $\vec{p} - \vec{a}$ onto the normal vector $\vec{n}$:

$$D = \left| (\vec{p} - \vec{a}) \cdot \frac{\vec{n}}{|\vec{n}|} \right| = \frac{|\vec{p} \cdot \vec{n} - \vec{a} \cdot \vec{n}|}{|\vec{n}|}$$

$$\mathbf{D = \frac{|\vec{p} \cdot \vec{n} - d|}{|\vec{n}|}}$$

---

### 3. Angle Between a Line and a Plane

Let the line have direction $\vec{d}$ and the plane have normal $\vec{n}$. The angle $\theta$ between the line and the plane is the complement of the angle between $\vec{d}$ and $\vec{n}$:

$$\sin\theta = \frac{|\vec{d} \cdot \vec{n}|}{|\vec{d}| |\vec{n}|}$$"""
            },
            {
                "id": "sec-geom3d-8-3",
                "title": "8.3 Reciprocal Triad of Vectors and Polyhedral Geometry",
                "content": r"""### 1. Definition of the Reciprocal System

Let $\vec{a}, \vec{b}, \vec{c}$ be three non-coplanar vectors in $\mathbb{R}^3$, so that their scalar triple product is non-zero:

$$V = [\vec{a}, \vec{b}, \vec{c}] \neq 0$$

The **reciprocal triad** (or **dual basis**) of vectors, denoted by $\vec{a}', \vec{b}', \vec{c}'$, is defined as:

$$\mathbf{\vec{a}' = \frac{\vec{b} \times \vec{c}}{[\vec{a}, \vec{b}, \vec{c}]}, \qquad \vec{b}' = \frac{\vec{c} \times \vec{a}}{[\vec{a}, \vec{b}, \vec{c}]}, \qquad \vec{c}' = \frac{\vec{a} \times \vec{b}}{[\vec{a}, \vec{b}, \vec{c}]}}$$

---

### 2. Fundamental Orthogonality and Normalization Relations

**Theorem:**  
For the direct triad $(\vec{a}_1, \vec{a}_2, \vec{a}_3) = (\vec{a}, \vec{b}, \vec{c})$ and the reciprocal triad $(\vec{a}'_1, \vec{a}'_2, \vec{a}'_3) = (\vec{a}', \vec{b}', \vec{c}')$:

$$\mathbf{\vec{a}_i \cdot \vec{a}'_j = \delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}}$$

#### Proof:
For $i = j = 1$:
$$\vec{a} \cdot \vec{a}' = \vec{a} \cdot \left( \frac{\vec{b} \times \vec{c}}{[\vec{a}, \vec{b}, \vec{c}]} \right) = \frac{\vec{a} \cdot (\vec{b} \times \vec{c})}{[\vec{a}, \vec{b}, \vec{c}]} = \frac{[\vec{a}, \vec{b}, \vec{c}]}{[\vec{a}, \vec{b}, \vec{c}]} = 1$$

For $i \neq j$, say $\vec{a} \cdot \vec{b}'$:
$$\vec{a} \cdot \vec{b}' = \vec{a} \cdot \left( \frac{\vec{c} \times \vec{a}}{[\vec{a}, \vec{b}, \vec{c}]} \right) = \frac{[\vec{a}, \vec{c}, \vec{a}]}{[\vec{a}, \vec{b}, \vec{c}]} = \frac{0}{[\vec{a}, \vec{b}, \vec{c}]} = 0$$
since any determinant with two identical vectors vanishes identically. $\blacksquare$

---

### 3. Reciprocal Volume Theorem

**Theorem:**  
The scalar triple product of the reciprocal vectors is the reciprocal of the scalar triple product of the original vectors:

$$\mathbf{[\vec{a}', \vec{b}', \vec{c}'] = \frac{1}{[\vec{a}, \vec{b}, \vec{c}]}}$$

#### Proof:
By definition:
$$[\vec{a}', \vec{b}', \vec{c}'] = \vec{a}' \cdot (\vec{b}' \times \vec{c}') = \frac{\vec{b} \times \vec{c}}{V} \cdot \left( \frac{\vec{c} \times \vec{a}}{V} \times \frac{\vec{a} \times \vec{b}}{V} \right)$$
$$= \frac{1}{V^3} (\vec{b} \times \vec{c}) \cdot \left[ (\vec{c} \times \vec{a}) \times (\vec{a} \times \vec{b}) \right]$$

Using the product of four vectors identity $(\vec{u} \times \vec{v}) \times \vec{w} = (\vec{u} \cdot \vec{w})\vec{v} - (\vec{v} \cdot \vec{w})\vec{u}$ with $\vec{w} = \vec{a} \times \vec{b}$:
$$[(\vec{c} \times \vec{a}) \times \vec{w}] = [\vec{c}, \vec{a}, \vec{b}]\vec{a} - [\vec{a}, \vec{a}, \vec{b}]\vec{c} = V\vec{a} - \vec{0} = V\vec{a}$$

Substitute this back:
$$[\vec{a}', \vec{b}', \vec{c}'] = \frac{1}{V^3} (\vec{b} \times \vec{c}) \cdot (V\vec{a}) = \frac{V}{V^3} (\vec{b} \times \vec{c}) \cdot \vec{a} = \frac{V \cdot V}{V^3} = \frac{1}{V} = \frac{1}{[\vec{a}, \vec{b}, \vec{c}]} \quad \blacksquare$$

---

### 4. Expansion of an Arbitrary Vector

Any vector $\vec{r} \in \mathbb{R}^3$ can be decomposed immediately in terms of either basis without inverting matrices:

$$\mathbf{\vec{r} = (\vec{r} \cdot \vec{a}')\vec{a} + (\vec{r} \cdot \vec{b}')\vec{b} + (\vec{r} \cdot \vec{c}')\vec{c}}$$
$$\mathbf{\vec{r} = (\vec{r} \cdot \vec{a})\vec{a}' + (\vec{r} \cdot \vec{b})\vec{b}' + (\vec{r} \cdot \vec{c})\vec{c}'}$$

This property makes reciprocal triads indispensable in solid-state physics and crystallography for defining **reciprocal lattices**."""
            }
        ],
        "simulations": [
            {
                "id": "sim_geom3d_spatial_apps",
                "title": "3D Interactive Line-Plane Piercing & Reciprocal Vectors Engine",
                "description": "Visualize line-plane piercing points, orthogonal projections, and explore reciprocal vector triads with interactive orientation angles and real-time algebraic coordinate readouts.",
                "controls": [
                    {"param": "tLine", "label": "Line Parameter t", "min": -3, "max": 3, "step": 0.2, "default": 0.5},
                    {"param": "planeTilt", "label": "Plane Tilt Angle (°)", "min": -60, "max": 60, "step": 2, "default": 25},
                    {"param": "pointDist", "label": "Test Point Height", "min": -4, "max": 4, "step": 0.5, "default": 2.0},
                    {"param": "showReciprocal", "label": "Show Reciprocal Triad", "min": 0, "max": 1, "step": 1, "default": 1}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-geom3d-8-1",
                "tier": 1,
                "title": "Perpendicular Distance from a Point to a Vector Line",
                "statement": r"""Find the perpendicular distance from the point $P(1, 2, 3)$ to the straight line given by:
$$\vec{r} = (2\hat{i} - \hat{j} + 4\hat{k}) + t(\hat{i} + 2\hat{j} - 2\hat{k})$$""",
                "solution": r"""**Step 1: Identify reference vectors**  
- Line reference point $\vec{a} = (2, -1, 4)$.
- Line direction vector $\vec{d} = (1, 2, -2)$.
- Given point $\vec{p} = (1, 2, 3)$.

The connecting displacement vector is:
$$\vec{p} - \vec{a} = (1 - 2)\hat{i} + (2 - (-1))\hat{j} + (3 - 4)\hat{k} = (-1, 3, -1)$$

---

**Step 2: Compute the cross product $(\vec{p} - \vec{a}) \times \vec{d}$**  
$$(\vec{p} - \vec{a}) \times \vec{d} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -1 & 3 & -1 \\ 1 & 2 & -2 \end{vmatrix}$$
$$= \hat{i}(3(-2) - (-1)(2)) - \hat{j}((-1)(-2) - (-1)(1)) + \hat{k}((-1)(2) - 3(1))$$
$$= \hat{i}(-6 + 2) - \hat{j}(2 + 1) + \hat{k}(-2 - 3) = -4\hat{i} - 3\hat{j} - 5\hat{k}$$

---

**Step 3: Evaluate magnitudes**  
$$|(\vec{p} - \vec{a}) \times \vec{d}| = \sqrt{(-4)^2 + (-3)^2 + (-5)^2} = \sqrt{16 + 9 + 25} = \sqrt{50} = 5\sqrt{2}$$

$$|\vec{d}| = \sqrt{1^2 + 2^2 + (-2)^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$

---

**Step 4: Compute perpendicular distance**  
$$D = \frac{|(\vec{p} - \vec{a}) \times \vec{d}|}{|\vec{d}|} = \frac{5\sqrt{2}}{3} \approx 2.357 \text{ units}$$"""
            },
            {
                "id": "prob-geom3d-8-2",
                "tier": 2,
                "title": "Piercing Point and Angle of Line-Plane Intersection",
                "statement": r"""Find the point of intersection (piercing point) of the line:
$$\vec{r} = (3\hat{i} - \hat{j} + 2\hat{k}) + t(2\hat{i} + \hat{j} - \hat{k})$$
with the plane:
$$\vec{r} \cdot (2\hat{i} - 3\hat{j} + 4\hat{k}) = 7$$
Also compute the angle $\theta$ between the line and the plane.""",
                "solution": r"""**Step 1: Determine the intersection parameter $t$**  
The line is $\vec{r}(t) = (3 + 2t)\hat{i} + (-1 + t)\hat{j} + (2 - t)\hat{k}$.  
Substitute into the plane equation $\vec{r} \cdot \vec{n} = 7$ where $\vec{n} = (2, -3, 4)$:

$$(3 + 2t)(2) + (-1 + t)(-3) + (2 - t)(4) = 7$$
$$(6 + 4t) + (3 - 3t) + (8 - 4t) = 7$$
$$(6 + 3 + 8) + (4t - 3t - 4t) = 7$$
$$17 - 3t = 7$$
$$-3t = 7 - 17 = -10 \implies t = \frac{10}{3}$$

---

**Step 2: Compute piercing point coordinates**  
Substitute $t = \frac{10}{3}$ into $\vec{r}(t)$:
$$x = 3 + 2\left(\frac{10}{3}\right) = 3 + \frac{20}{3} = \frac{29}{3}$$
$$y = -1 + \left(\frac{10}{3}\right) = \frac{7}{3}$$
$$z = 2 - \left(\frac{10}{3}\right) = -\frac{4}{3}$$

Thus, the piercing point is $P\left(\frac{29}{3}, \frac{7}{3}, -\frac{4}{3}\right)$.

---

**Step 3: Angle between line and plane**  
Line direction $\vec{d} = (2, 1, -1)$, plane normal $\vec{n} = (2, -3, 4)$.

$$\vec{d} \cdot \vec{n} = 2(2) + 1(-3) + (-1)(4) = 4 - 3 - 4 = -3$$
$$|\vec{d}| = \sqrt{2^2 + 1^2 + (-1)^2} = \sqrt{4 + 1 + 1} = \sqrt{6}$$
$$|\vec{n}| = \sqrt{2^2 + (-3)^2 + 4^2} = \sqrt{4 + 9 + 16} = \sqrt{29}$$

$$\sin\theta = \frac{|\vec{d} \cdot \vec{n}|}{|\vec{d}| |\vec{n}|} = \frac{|-3|}{\sqrt{6}\sqrt{29}} = \frac{3}{\sqrt{174}}$$

$$\theta = \arcsin\left(\frac{3}{\sqrt{174}}\right) \approx \arcsin(0.2274) \approx 13.14^\circ$$"""
            },
            {
                "id": "prob-geom3d-8-3",
                "tier": 3,
                "title": "Construction and Verification of Reciprocal Vector Triad",
                "statement": r"""Given the non-coplanar triad of vectors:
$$\vec{a} = \hat{i} + \hat{j}, \qquad \vec{b} = \hat{j} + \hat{k}, \qquad \vec{c} = \hat{k} + \hat{i}$$
(a) Compute the scalar triple product $[\vec{a}, \vec{b}, \vec{c}]$.  
(b) Construct the reciprocal triad of vectors $(\vec{a}', \vec{b}', \vec{c}')$.  
(c) Verify explicitly that $\vec{a} \cdot \vec{a}' = 1$, $\vec{a} \cdot \vec{b}' = 0$, and $[\vec{a}', \vec{b}', \vec{c}'] = \frac{1}{[\vec{a}, \vec{b}, \vec{c}]}$.""",
                "solution": r"""**Part (a): Evaluate $[\vec{a}, \vec{b}, \vec{c}]$**  
$$\vec{a} = (1, 1, 0), \quad \vec{b} = (0, 1, 1), \quad \vec{c} = (1, 0, 1)$$

$$V = [\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix}$$
Expanding along the first row:
$$V = 1(1 - 0) - 1(0 - 1) + 0 = 1 + 1 = 2$$

Since $V = 2 \neq 0$, the vectors form a valid non-coplanar triad.

---

**Part (b): Construct the reciprocal triad**  
1. Compute $\vec{b} \times \vec{c}$:
   $$\vec{b} \times \vec{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix} = \hat{i}(1 - 0) - \hat{j}(0 - 1) + \hat{k}(0 - 1) = \hat{i} + \hat{j} - \hat{k} = (1, 1, -1)$$
   $$\vec{a}' = \frac{\vec{b} \times \vec{c}}{V} = \frac{1}{2}(\hat{i} + \hat{j} - \hat{k})$$

2. Compute $\vec{c} \times \vec{a}$:
   $$\vec{c} \times \vec{a} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{vmatrix} = \hat{i}(0 - 1) - \hat{j}(0 - 1) + \hat{k}(1 - 0) = -\hat{i} + \hat{j} + \hat{k} = (-1, 1, 1)$$
   $$\vec{b}' = \frac{\vec{c} \times \vec{a}}{V} = \frac{1}{2}(-\hat{i} + \hat{j} + \hat{k})$$

3. Compute $\vec{a} \times \vec{b}$:
   $$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = \hat{i}(1 - 0) - \hat{j}(1 - 0) + \hat{k}(1 - 0) = \hat{i} - \hat{j} + \hat{k} = (1, -1, 1)$$
   $$\vec{c}' = \frac{\vec{a} \times \vec{b}}{V} = \frac{1}{2}(\hat{i} - \hat{j} + \hat{k})$$

---

**Part (c): Verification of Properties**  
1. **Normalization:**
   $$\vec{a} \cdot \vec{a}' = (1, 1, 0) \cdot \frac{1}{2}(1, 1, -1) = \frac{1}{2}(1(1) + 1(1) + 0(-1)) = \frac{1}{2}(2) = 1 \quad \checkmark$$

2. **Orthogonality:**
   $$\vec{a} \cdot \vec{b}' = (1, 1, 0) \cdot \frac{1}{2}(-1, 1, 1) = \frac{1}{2}(1(-1) + 1(1) + 0(1)) = \frac{1}{2}(0) = 0 \quad \checkmark$$

3. **Reciprocal Volume:**
   $$[\vec{a}', \vec{b}', \vec{c}'] = \begin{vmatrix} 1/2 & 1/2 & -1/2 \\ -1/2 & 1/2 & 1/2 \\ 1/2 & -1/2 & 1/2 \end{vmatrix} = \left(\frac{1}{2}\right)^3 \begin{vmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix}$$
   Evaluate the integer determinant:
   $$\begin{vmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix} = 1(1 - (-1)) - 1(-1 - 1) + (-1)(1 - 1)$$
   $$= 1(2) - 1(-2) - 1(0) = 2 + 2 = 4$$
   Thus:
   $$[\vec{a}', \vec{b}', \vec{c}'] = \frac{1}{8} \times 4 = \frac{4}{8} = \frac{1}{2}$$

   Notice that:
   $$\frac{1}{[\vec{a}, \vec{b}, \vec{c}]} = \frac{1}{2}$$

   Therefore, $[\vec{a}', \vec{b}', \vec{c}'] = \frac{1}{[\vec{a}, \vec{b}, \vec{c}]} = \frac{1}{2}$ holds with absolute mathematical precision. $\blacksquare$"""
            }
        ]
    }

if __name__ == "__main__":
    print("Building 3D Geometry: Units 7 & 8...")
    u7 = build_unit_7()
    with open("geom3d_u7.json", "w", encoding="utf-8") as f:
        json.dump(u7, f, indent=2, ensure_ascii=False)
    print("Saved geom3d_u7.json successfully.")

    u8 = build_unit_8()
    with open("geom3d_u8.json", "w", encoding="utf-8") as f:
        json.dump(u8, f, indent=2, ensure_ascii=False)
    print("Saved geom3d_u8.json successfully.")
