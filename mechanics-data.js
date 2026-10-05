// Fundamentals of Mechanics
// Complete university textbook curriculum dataset with 6 Units, LaTeX math, and solved exam problems.

window.COURSE_DATA = {
  "courseTitle": "Fundamentals of Mechanics",
  "courseCode": "PHYSICS",
  "department": "Department of Physics",
  "institution": "OpenSTEM Global Academic Press",
  "authorContact": "shahriyarkarimsiam@gmail.com",
  "units": [
    {
      "number": 1,
      "title": "Vector Algebra & Vector Calculus",
      "leadSummary": "Scalar and vector quantities, Cartesian representations, scalar and vector products, triple products, vector differentiation and integration, gradient, divergence, and curl in classical mechanics.",
      "sections": [
        {
          "id": "sec-1-1",
          "number": "§1.1",
          "heading": "Vectors, Scalars, and Coordinate Representations",
          "simulation": "vector-addition-sim",
          "content": `Classical Newtonian mechanics describes physical phenomena occurring in three-dimensional Euclidean space $\\mathbb{R}^3$. Physical quantities are classified based on their transformation properties under spatial coordinate rotations and reflections.

<h4>1. Scalar and Vector Quantities</h4>
A **scalar** is a physical quantity that is completely characterized by a single real numerical magnitude and appropriate physical units, remaining invariant under coordinate rotations:
$$S' = S$$
Examples include mass $m$, time $t$, temperature $T$, electric charge $q$, work $W$, and kinetic energy $K$.

A **vector** $\\mathbf{A}$ is an entity possessing both magnitude and direction that transforms under a coordinate rotation according to the orthogonal transformation law:
$$A_i' = \\sum_{j=1}^3 R_{ij} A_j, \\quad \\text{where } R R^T = I, \\quad \\det(R) = 1$$
Examples include position vector $\\mathbf{r}$, displacement $\\Delta\\mathbf{r}$, velocity $\\mathbf{v}$, linear momentum $\\mathbf{p}$, acceleration $\\mathbf{a}$, force $\\mathbf{F}$, and torque $\\boldsymbol{\\tau}$.

<h4>2. Algebraic Operations in Cartesian Basis</h4>
In a right-handed Cartesian coordinate system with orthonormal basis vectors $\\{\\hat{\\mathbf{i}}, \\hat{\\mathbf{j}}, \\hat{\\mathbf{k}}\\}$ satisfying $\\hat{\\mathbf{i}} \\cdot \\hat{\\mathbf{i}} = 1$ and $\\hat{\\mathbf{i}} \\cdot \\hat{\\mathbf{j}} = 0$:
$$\\mathbf{A} = A_x \\hat{\\mathbf{i}} + A_y \\hat{\\mathbf{j}} + A_z \\hat{\\mathbf{k}}, \\quad \\mathbf{B} = B_x \\hat{\\mathbf{i}} + B_y \\hat{\\mathbf{j}} + B_z \\hat{\\mathbf{k}}$$

Vector addition obeys the axioms of an abelian group:
$$\\mathbf{A} + \\mathbf{B} = (A_x + B_x)\\hat{\\mathbf{i}} + (A_y + B_y)\\hat{\\mathbf{j}} + (A_z + B_z)\\hat{\\mathbf{k}}$$

Scalar multiplication scales the length without altering spatial orientation (or reverses direction if $\\lambda < 0$):
$$\\lambda \\mathbf{A} = (\\lambda A_x)\\hat{\\mathbf{i}} + (\\lambda A_y)\\hat{\\mathbf{j}} + (\\lambda A_z)\\hat{\\mathbf{k}}, \\quad \\lambda \\in \\mathbb{R}$$

The magnitude (Euclidean norm) is given by the Pythagorean metric:
$$|\\mathbf{A}| = A = \\sqrt{A_x^2 + A_y^2 + A_z^2}$$
The unit vector pointing along $\\mathbf{A}$ is defined as $\\hat{\\mathbf{A}} = \\frac{\\mathbf{A}}{|\\mathbf{A}|}$.

<h4>3. The Scalar (Dot) Product</h4>
The scalar product of two vectors is defined geometrically and algebraically as:
$$\\mathbf{A} \\cdot \\mathbf{B} = |\\mathbf{A}||\\mathbf{B}| \\cos \\theta = A_x B_x + A_y B_y + A_z B_z$$
where $\\theta \\in [0, \\pi]$ is the interior angle between them.
<ul>
  <li><strong>Commutativity:</strong> $\\mathbf{A} \\cdot \\mathbf{B} = \\mathbf{B} \\cdot \\mathbf{A}$.</li>
  <li><strong>Orthogonality Criterion:</strong> Two non-zero vectors are perpendicular if and only if their dot product vanishes: $\\mathbf{A} \\perp \\mathbf{B} \\iff \\mathbf{A} \\cdot \\mathbf{B} = 0$.</li>
  <li><strong>Scalar Projection:</strong> The projection of $\\mathbf{A}$ along $\\mathbf{B}$ is $A_{\\parallel B} = \\mathbf{A} \\cdot \\hat{\\mathbf{B}} = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{|\\mathbf{B}|}$.</li>
  <li><strong>Physical Application:</strong> Mechanical work done by a variable force $\\mathbf{F}$ over an infinitesimal displacement $d\\mathbf{r}$ is $dW = \\mathbf{F} \\cdot d\\mathbf{r}$, and instantaneous power is $P = \\mathbf{F} \\cdot \\mathbf{v}$.</li>
</ul>

<h4>4. The Vector (Cross) Product</h4>
The vector product produces an axial vector (pseudovector) perpendicular to the plane formed by $\\mathbf{A}$ and $\\mathbf{B}$:
$$\\mathbf{A} \\times \\mathbf{B} = (|\\mathbf{A}||\\mathbf{B}| \\sin \\theta)\\, \\hat{\\mathbf{n}}$$
where $\\hat{\\mathbf{n}}$ is the unit normal established by the right-hand rule. In determinant form:
$$\\mathbf{A} \\times \\mathbf{B} = \\begin{vmatrix} \\hat{\\mathbf{i}} & \\hat{\\mathbf{j}} & \\hat{\\mathbf{k}} \\\\ A_x & A_y & A_z \\\\ B_x & B_y & B_z \\end{vmatrix} = (A_y B_z - A_z B_y)\\hat{\\mathbf{i}} + (A_z B_x - A_x B_z)\\hat{\\mathbf{j}} + (A_x B_y - A_y B_x)\\hat{\\mathbf{k}}$$
<ul>
  <li><strong>Anticommutativity:</strong> $\\mathbf{B} \\times \\mathbf{A} = -(\\mathbf{A} \\times \\mathbf{B})$.</li>
  <li><strong>Collinearity Criterion:</strong> $\\mathbf{A} \\parallel \\mathbf{B} \\iff \\mathbf{A} \\times \\mathbf{B} = \\mathbf{0}$.</li>
  <li><strong>Geometric Area:</strong> The magnitude $|\\mathbf{A} \\times \\mathbf{B}|$ equals the area of the parallelogram spanned by $\\mathbf{A}$ and $\\mathbf{B}$.</li>
  <li><strong>Physical Application:</strong> Torque $\\boldsymbol{\\tau} = \\mathbf{r} \\times \\mathbf{F}$, angular momentum $\\mathbf{L} = \\mathbf{r} \\times \\mathbf{p}$, and magnetic Lorentz force $\\mathbf{F} = q(\\mathbf{v} \\times \\mathbf{B})$.</li>
</ul>`
        },
        {
          "id": "sec-1-2",
          "number": "§1.2",
          "heading": "Triple Products and Their Physical Significance",
          "simulation": "vector-triple-product-sim",
          "content": `In three dimensions, products involving three vectors arise frequently when evaluating volumes, rotating reference frames, and magnetic field interactions.

<h4>1. The Scalar Triple Product (Box Product)</h4>
The scalar triple product of three vectors $\\mathbf{A}, \\mathbf{B}, \\mathbf{C}$ is defined as:
$$[\\mathbf{A}, \\mathbf{B}, \\mathbf{C}] = \\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C})$$
In determinant form:
$$[\\mathbf{A}, \\mathbf{B}, \\mathbf{C}] = \\begin{vmatrix} A_x & A_y & A_z \\\\ B_x & B_y & B_z \\\\ C_x & C_y & C_z \\end{vmatrix}$$

<strong>Properties and Invariances:</strong>
<ul>
  <li><strong>Cyclic Invariance:</strong> Permuting the vectors cyclically preserves the scalar value:
  $$\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C}) = \\mathbf{B} \\cdot (\\mathbf{C} \\times \\mathbf{A}) = \\mathbf{C} \\cdot (\\mathbf{A} \\times \\mathbf{B})$$
  </li>
  <li><strong>Anticyclic Sign Inversion:</strong> Exchanging any two vectors negates the sign:
  $$\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C}) = -\\mathbf{A} \\cdot (\\mathbf{C} \\times \\mathbf{B})$$
  </li>
  <li><strong>Interchange of Dot and Cross:</strong> $\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C}) = (\\mathbf{A} \\times \\mathbf{B}) \\cdot \\mathbf{C}$.</li>
  <li><strong>Geometric Volume:</strong> $|\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C})|$ equals the exact volume $V$ of the parallelepiped spanned by the vectors $\\mathbf{A}$, $\\mathbf{B}$, and $\\mathbf{C}$.</li>
  <li><strong>Coplanarity Condition:</strong> Three vectors are coplanar if and only if their scalar triple product vanishes:
  $$\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C}) = 0 \\iff \\mathbf{A}, \\mathbf{B}, \\mathbf{C} \\text{ are coplanar}$$
  </li>
</ul>

<h4>2. The Vector Triple Product and the BAC-CAB Rule</h4>
The vector triple product takes the cross product of one vector with the cross product of two others:
$$\\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C})$$
Because $\\mathbf{B} \\times \\mathbf{C}$ is normal to the plane containing $\\mathbf{B}$ and $\\mathbf{C}$, taking the cross product with $\\mathbf{A}$ produces a vector that lies entirely within the plane spanned by $\\mathbf{B}$ and $\\mathbf{C}$. Therefore, it can be expanded linearly as:
$$\\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C}) = \\mathbf{B}(\\mathbf{A} \\cdot \\mathbf{C}) - \\mathbf{C}(\\mathbf{A} \\cdot \\mathbf{B}) \\quad \\text{(\"BAC - CAB\" Identity)}$$

Similarly, using anticommutativity:
$$(\\mathbf{A} \\times \\mathbf{B}) \\times \\mathbf{C} = -\\mathbf{C} \\times (\\mathbf{A} \\times \\mathbf{B}) = \\mathbf{B}(\\mathbf{A} \\cdot \\mathbf{C}) - \\mathbf{A}(\\mathbf{B} \\cdot \\mathbf{C})$$

<strong>Physical Significance in Classical Mechanics:</strong>
In rotating frames with angular velocity $\\boldsymbol{\\omega}$, the centripetal acceleration vector is:
$$\\mathbf{a}_c = \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r})$$
Applying the BAC-CAB rule:
$$\\mathbf{a}_c = \\boldsymbol{\\omega}(\\boldsymbol{\\omega} \\cdot \\mathbf{r}) - \\mathbf{r}(\\boldsymbol{\\omega} \\cdot \\boldsymbol{\\omega}) = (\\boldsymbol{\\omega} \\cdot \\mathbf{r})\\boldsymbol{\\omega} - \\omega^2 \\mathbf{r} = -\\omega^2 \\mathbf{r}_\\perp$$
where $\\mathbf{r}_\\perp$ is the perpendicular vector from the rotation axis to the particle's position. This proves rigorously that centripetal acceleration points directly inward toward the instantaneous axis of rotation.`
        },
        {
          "id": "sec-1-3",
          "number": "§1.3",
          "heading": "Vector Differentiation and Integration with Respect to Time",
          "simulation": "vector-integration-sim",
          "content": `In classical kinematics, physical vectors vary continuously as functions of a scalar parameter: time $t$.

<h4>1. Derivative of a Vector Function</h4>
Let $\\mathbf{A}(t) = A_x(t)\\hat{\\mathbf{i}} + A_y(t)\\hat{\\mathbf{j}} + A_z(t)\\hat{\\mathbf{k}}$ be a vector function of time. In a fixed Cartesian frame where the basis unit vectors are time-invariant:
$$\\frac{d\\mathbf{A}}{dt} = \\lim_{\\Delta t \\to 0} \\frac{\\mathbf{A}(t + \\Delta t) - \\mathbf{A}(t)}{\\Delta t} = \\frac{dA_x}{dt}\\hat{\\mathbf{i}} + \\frac{dA_y}{dt}\\hat{\\mathbf{j}} + \\frac{dA_z}{dt}\\hat{\\mathbf{k}}$$

<h4>2. Product Rules for Vector Derivatives</h4>
Let $\\phi(t)$ be a scalar function, and $\\mathbf{A}(t), \\mathbf{B}(t)$ be differentiable vector functions:
<ol>
  <li><strong>Scalar-Vector Product Rule:</strong>
  $$\\frac{d}{dt}[\\phi(t) \\mathbf{A}(t)] = \\frac{d\\phi}{dt} \\mathbf{A} + \\phi \\frac{d\\mathbf{A}}{dt}$$
  </li>
  <li><strong>Dot Product Rule:</strong>
  $$\\frac{d}{dt}[\\mathbf{A}(t) \\cdot \\mathbf{B}(t)] = \\frac{d\\mathbf{A}}{dt} \\cdot \\mathbf{B} + \\mathbf{A} \\cdot \\frac{d\\mathbf{B}}{dt}$$
  <em>Consequence:</em> If $|\\mathbf{A}(t)| = \\text{const}$, then $\\mathbf{A} \\cdot \\mathbf{A} = \\text{const} \\implies \\frac{d}{dt}(\\mathbf{A} \\cdot \\mathbf{A}) = 2 \\mathbf{A} \\cdot \\frac{d\\mathbf{A}}{dt} = 0$. Hence, any vector of constant magnitude is strictly perpendicular to its time derivative (e.g., velocity in uniform circular motion).
  </li>
  <li><strong>Cross Product Rule (Order Preserving):</strong>
  $$\\frac{d}{dt}[\\mathbf{A}(t) \\times \\mathbf{B}(t)] = \\frac{d\\mathbf{A}}{dt} \\times \\mathbf{B} + \\mathbf{A} \\times \\frac{d\\mathbf{B}}{dt}$$
  </li>
</ol>

<h4>3. Vector Integration</h4>
The indefinite integral of $\\mathbf{A}(t)$ is:
$$\\int \\mathbf{A}(t) dt = \\left(\\int A_x(t) dt\\right)\\hat{\\mathbf{i}} + \\left(\\int A_y(t) dt\\right)\\hat{\\mathbf{j}} + \\left(\\int A_z(t) dt\\right)\\hat{\\mathbf{k}} + \\mathbf{C}$$
where $\\mathbf{C} = C_x \\hat{\\mathbf{i}} + C_y \\hat{\\mathbf{j}} + C_z \\hat{\\mathbf{k}}$ is a constant vector of integration determined by initial boundary conditions (e.g., initial position $\\mathbf{r}(0)$ or initial velocity $\\mathbf{v}(0)$).

Given acceleration $\\mathbf{a}(t)$:
$$\\mathbf{v}(t) = \\mathbf{v}_0 + \\int_0^t \\mathbf{a}(t') dt', \\quad \\mathbf{r}(t) = \\mathbf{r}_0 + \\int_0^t \\mathbf{v}(t') dt'$$`
        },
        {
          "id": "sec-1-4",
          "number": "§1.4",
          "heading": "Differential Vector Calculus: Gradient, Divergence, and Curl",
          "simulation": "vector-fields-calc-sim",
          "content": `Spatial fields represent physical quantities that vary continuously over space. Vector calculus describes the spatial rates of change of scalar fields $\\Phi(\\mathbf{r})$ and vector fields $\\mathbf{V}(\\mathbf{r})$.

<h4>1. The Del (Nabla) Operator</h4>
The vector differential operator $\\boldsymbol{\\nabla}$ in Cartesian coordinates is:
$$\\boldsymbol{\\nabla} = \\hat{\\mathbf{i}} \\frac{\\partial}{\\partial x} + \\hat{\\mathbf{j}} \\frac{\\partial}{\\partial y} + \\hat{\\mathbf{k}} \\frac{\\partial}{\\partial z}$$

<h4>2. Gradient of a Scalar Field ($\\boldsymbol{\\nabla}\\Phi$)</h4>
The gradient of a differentiable scalar function $\\Phi(x, y, z)$ is a vector pointing in the direction of maximum spatial increase of $\\Phi$, whose magnitude equals the maximum directional derivative:
$$\\boldsymbol{\\nabla}\\Phi = \\frac{\\partial \\Phi}{\\partial x}\\hat{\\mathbf{i}} + \\frac{\\partial \\Phi}{\\partial y}\\hat{\\mathbf{j}} + \\frac{\\partial \\Phi}{\\partial z}\\hat{\\mathbf{k}}$$

<strong>Physical Application:</strong> Conservative forces in mechanics are the negative gradient of their potential energy functions $U(\\mathbf{r})$:
$$\\mathbf{F}(\\mathbf{r}) = -\\boldsymbol{\\nabla}U(\\mathbf{r})$$

<h4>3. Divergence of a Vector Field ($\\boldsymbol{\\nabla} \\cdot \\mathbf{V}$)</h4>
The divergence measures the net outflow flux per unit volume from an infinitesimal neighborhood around a point:
$$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} = \\frac{\\partial V_x}{\\partial x} + \\frac{\\partial V_y}{\\partial y} + \\frac{\\partial V_z}{\\partial z}$$
<ul>
  <li>$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} > 0$: The point is a source (net outflow).</li>
  <li>$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} < 0$: The point is a sink (net inflow).</li>
  <li>$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} = 0$: Solenoidal (incompressible) field.</li>
</ul>

<h4>4. Curl of a Vector Field ($\\boldsymbol{\\nabla} \\times \\mathbf{V}$)</h4>
The curl represents the microscopic circulation (vorticity) density of the vector field:
$$\\boldsymbol{\\nabla} \\times \\mathbf{V} = \\begin{vmatrix} \\hat{\\mathbf{i}} & \\hat{\\mathbf{j}} & \\hat{\\mathbf{k}} \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ V_x & V_y & V_z \\end{vmatrix} = \\left( \\frac{\\partial V_z}{\\partial y} - \\frac{\\partial V_y}{\\partial z} \\right)\\hat{\\mathbf{i}} + \\left( \\frac{\\partial V_x}{\\partial z} - \\frac{\\partial V_z}{\\partial x} \\right)\\hat{\\mathbf{j}} + \\left( \\frac{\\partial V_y}{\\partial x} - \\frac{\\partial V_x}{\\partial y} \\right)\\hat{\\mathbf{k}}$$

<strong>Two Fundamental Vector Identities:</strong>
$$\\boldsymbol{\\nabla} \\times (\\boldsymbol{\\nabla}\\Phi) = \\mathbf{0} \\quad (\\text{The curl of any gradient field vanishes identically})$$
$$\\boldsymbol{\\nabla} \\cdot (\\boldsymbol{\\nabla} \\times \\mathbf{V}) = 0 \\quad (\\text{The divergence of any curl field vanishes identically})$$

<strong>Criterion for Conservative Force Fields:</strong>
A force field $\\mathbf{F}(\\mathbf{r})$ defined on a simply-connected domain is conservative if and only if its curl vanishes everywhere:
$$\\boldsymbol{\\nabla} \\times \\mathbf{F} = \\mathbf{0} \\iff \\mathbf{F} = -\\boldsymbol{\\nabla}U$$`
        }
      ],
      "problems": [
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Conservative Force and Potential Energy Derivation",
          "question": "A force field acting on a particle is given by $\\mathbf{F} = (2xy + z^3)\\hat{\\mathbf{i}} + x^2\\hat{\\mathbf{j}} + 3xz^2\\hat{\\mathbf{k}}$. (a) Prove that the force field is conservative by computing its curl. (b) Find the scalar potential energy function $U(x, y, z)$ such that $\\mathbf{F} = -\\boldsymbol{\\nabla}U$, taking $U(0, 0, 0) = 0$.",
          "steps": [
            {
              "title": "Step 1: Compute curl of F",
              "math": "$$\\boldsymbol{\\nabla} \\times \\mathbf{F} = \\begin{vmatrix} \\hat{\\mathbf{i}} & \\hat{\\mathbf{j}} & \\hat{\\mathbf{k}} \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ 2xy + z^3 & x^2 & 3xz^2 \\end{vmatrix}$$\n$$(\\boldsymbol{\\nabla} \\times \\mathbf{F})_x = \\frac{\\partial(3xz^2)}{\\partial y} - \\frac{\\partial(x^2)}{\\partial z} = 0 - 0 = 0$$\n$$(\\boldsymbol{\\nabla} \\times \\mathbf{F})_y = \\frac{\\partial(2xy + z^3)}{\\partial z} - \\frac{\\partial(3xz^2)}{\\partial x} = 3z^2 - 3z^2 = 0$$\n$$(\\boldsymbol{\\nabla} \\times \\mathbf{F})_z = \\frac{\\partial(x^2)}{\\partial x} - \\frac{\\partial(2xy + z^3)}{\\partial y} = 2x - 2x = 0$$\n$$\\boldsymbol{\\nabla} \\times \\mathbf{F} = \\mathbf{0}$$",
              "explanation": "Because the curl vanishes identically throughout $\\mathbb{R}^3$, the force field is strictly conservative."
            },
            {
              "title": "Step 2: Integrate to determine potential energy U(x, y, z)",
              "math": "$$-\\frac{\\partial U}{\\partial x} = 2xy + z^3 \\implies U(x, y, z) = -x^2 y - x z^3 + g(y, z)$$\n$$-\\frac{\\partial U}{\\partial y} = x^2 - \\frac{\\partial g}{\\partial y} = x^2 \\implies \\frac{\\partial g}{\\partial y} = 0 \\implies g(y, z) = h(z)$$\n$$-\\frac{\\partial U}{\\partial z} = 3x z^2 - h'(z) = 3xz^2 \\implies h'(z) = 0 \\implies h(z) = C$$\n$$U(x, y, z) = -(x^2 y + x z^3)$$",
              "explanation": "Using boundary condition $U(0,0,0) = 0$, constant $C = 0$."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Vector Triple Product and Parallelepiped Volume",
          "question": "Three vectors spanning a vertex in $\\mathbb{R}^3$ are given by $\\mathbf{A} = 2\\hat{\\mathbf{i}} - \\hat{\\mathbf{j}} + \\hat{\\mathbf{k}}$, $\\mathbf{B} = \\hat{\\mathbf{i}} + 3\\hat{\\mathbf{j}} - 2\\hat{\\mathbf{k}}$, and $\\mathbf{C} = -2\\hat{\\mathbf{i}} + \\hat{\\mathbf{j}} - 3\\hat{\\mathbf{k}}$. (a) Calculate the volume $V$ of the parallelepiped. (b) Verify the BAC-CAB vector identity for $\\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C})$.",
          "steps": [
            {
              "title": "Step 1: Compute the volume via scalar triple product",
              "math": "$$V = |\\mathbf{A} \\cdot (\\mathbf{B} \\times \\mathbf{C})| = \\begin{vmatrix} 2 & -1 & 1 \\\\ 1 & 3 & -2 \\\\ -2 & 1 & -3 \\end{vmatrix}$$\n$$V = |2(-9 - (-2)) - (-1)(-3 - 4) + 1(1 - (-6))| = |2(-7) + 1(-7) + 1(7)| = |-14 - 7 + 7| = |-14| = 14$$",
              "explanation": "The volume of the parallelepiped formed by the three vectors is exactly 14 cubic units."
            },
            {
              "title": "Step 2: Evaluate B(A · C) - C(A · B)",
              "math": "$$\\mathbf{A} \\cdot \\mathbf{B} = 2(1) + (-1)(3) + 1(-2) = 2 - 3 - 2 = -3$$\n$$\\mathbf{A} \\cdot \\mathbf{C} = 2(-2) + (-1)(1) + 1(-3) = -4 - 1 - 3 = -8$$\n$$\\mathbf{B}(\\mathbf{A} \\cdot \\mathbf{C}) - \\mathbf{C}(\\mathbf{A} \\cdot \\mathbf{B}) = -8(\\hat{\\mathbf{i}} + 3\\hat{\\mathbf{j}} - 2\\hat{\\mathbf{k}}) - (-3)(-2\\hat{\\mathbf{i}} + \\hat{\\mathbf{j}} - 3\\hat{\\mathbf{k}})$$\n$$= (-8\\hat{\\mathbf{i}} - 24\\hat{\\mathbf{j}} + 16\\hat{\\mathbf{k}}) - (6\\hat{\\mathbf{i}} - 3\\hat{\\mathbf{j}} + 9\\hat{\\mathbf{k}}) = -14\\hat{\\mathbf{i}} - 21\\hat{\\mathbf{j}} + 7\\hat{\\mathbf{k}}$$",
              "explanation": "Direct calculation of $\\mathbf{B} \\times \\mathbf{C} = -7\\hat{\\mathbf{i}} + 7\\hat{\\mathbf{j}} + 7\\hat{\\mathbf{k}}$ followed by $\\mathbf{A} \\times (-7\\hat{\\mathbf{i}} + 7\\hat{\\mathbf{j}} + 7\\hat{\\mathbf{k}})$ yields identical vector $-14\\hat{\\mathbf{i}} - 21\\hat{\\mathbf{j}} + 7\\hat{\\mathbf{k}}$."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Vector Integration for a Helical Particle Trajectory",
          "question": "A charged particle in a magnetic field has an acceleration vector $\\mathbf{a}(t) = -\\omega^2 R \\cos(\\omega t)\\hat{\\mathbf{i}} - \\omega^2 R \\sin(\\omega t)\\hat{\\mathbf{j}} + c\\hat{\\mathbf{k}}$. Given initial conditions $\\mathbf{v}(0) = \\omega R\\hat{\\mathbf{j}} + v_z\\hat{\\mathbf{k}}$ and $\\mathbf{r}(0) = R\\hat{\\mathbf{i}}$, find the position vector $\\mathbf{r}(t)$ at all subsequent times.",
          "steps": [
            {
              "title": "Step 1: Integrate acceleration to obtain velocity vector v(t)",
              "math": "$$\\mathbf{v}(t) = \\int \\mathbf{a}(t) dt = \\left( -\\omega R \\sin(\\omega t) + C_1 \\right)\\hat{\\mathbf{i}} + \\left( \\omega R \\cos(\\omega t) + C_2 \\right)\\hat{\\mathbf{j}} + (ct + C_3)\\hat{\\mathbf{k}}$$\n$$\\mathbf{v}(0) = C_1\\hat{\\mathbf{i}} + (\\omega R + C_2)\\hat{\\mathbf{j}} + C_3\\hat{\\mathbf{k}} = \\omega R\\hat{\\mathbf{j}} + v_z\\hat{\\mathbf{k}} \\implies C_1 = 0, \\; C_2 = 0, \\; C_3 = v_z$$\n$$\\mathbf{v}(t) = -\\omega R \\sin(\\omega t)\\hat{\\mathbf{i}} + \\omega R \\cos(\\omega t)\\hat{\\mathbf{j}} + (ct + v_z)\\hat{\\mathbf{k}}$$",
              "explanation": "The transverse velocity undergoes uniform circular motion while axial velocity increases linearly."
            },
            {
              "title": "Step 2: Integrate velocity to obtain position vector r(t)",
              "math": "$$\\mathbf{r}(t) = \\int \\mathbf{v}(t) dt = \\left( R \\cos(\\omega t) + D_1 \\right)\\hat{\\mathbf{i}} + \\left( R \\sin(\\omega t) + D_2 \\right)\\hat{\\mathbf{j}} + \\left( \\frac{1}{2}ct^2 + v_z t + D_3 \\right)\\hat{\\mathbf{k}}$$\n$$\\mathbf{r}(0) = (R + D_1)\\hat{\\mathbf{i}} + D_2\\hat{\\mathbf{j}} + D_3\\hat{\\mathbf{k}} = R\\hat{\\mathbf{i}} \\implies D_1 = 0, \\; D_2 = 0, \\; D_3 = 0$$\n$$\\mathbf{r}(t) = R \\cos(\\omega t)\\hat{\\mathbf{i}} + R \\sin(\\omega t)\\hat{\\mathbf{j}} + \\left( v_z t + \\frac{1}{2}ct^2 \\right)\\hat{\\mathbf{k}}$$",
              "explanation": "The particle traces out an accelerating helix of constant radius $R$ along the z-axis."
            }
          ]
        }
      ]
    },
    {
      "number": 2,
      "title": "Vector Integral Theorems & Coordinates",
      "leadSummary": "Line, surface, and volume elements, Gauss's divergence theorem, Stokes' theorem, Green's theorem, plane polar coordinates, cylindrical and spherical systems, and the Laplacian operator.",
      "sections": [
        {
          "id": "sec-2-1",
          "number": "§2.1",
          "heading": "Line, Surface, and Volume Integrals with Fundamental Theorems",
          "simulation": "stokes-divergence-sim",
          "content": `Vector integrals form the core mathematical foundation for evaluating work done along curves, mass distributions across solid volumes, and flux of gravitational and electric fields.

<h4>1. Line Integrals and Path Independence</h4>
The line integral of a vector field $\\mathbf{F}$ along a directed smooth curve $C$ parameterized by $\\mathbf{r}(t)$ for $t \\in [a, b]$ is:
$$W = \\int_C \\mathbf{F} \\cdot d\\mathbf{r} = \\int_a^b \\mathbf{F}(\\mathbf{r}(t)) \\cdot \\frac{d\\mathbf{r}}{dt} dt$$

For a conservative force field $\\mathbf{F} = -\\boldsymbol{\\nabla}U$, the line integral depends strictly on the endpoints $A$ and $B$:
$$\\int_A^B \\mathbf{F} \\cdot d\\mathbf{r} = -\\int_A^B dU = -(U(B) - U(A)) = U(A) - U(B)$$
Consequently, the circulation around any closed loop vanishes identically:
$$\\oint_C \\mathbf{F} \\cdot d\\mathbf{r} = 0$$

<h4>2. Gauss’s Divergence Theorem</h4>
Gauss's divergence theorem establishes that the total outward flux of a continuously differentiable vector field $\\mathbf{V}$ across a closed boundary surface $S = \\partial V$ equals the volume integral of its divergence:
$$\\oint_S \\mathbf{V} \\cdot d\\mathbf{A} = \\iiint_V (\\boldsymbol{\\nabla} \\cdot \\mathbf{V}) dV$$

<strong>Gravitational Application:</strong>
For the Newtonian gravitational field $\\mathbf{g} = -G \\frac{M}{r^2} \\hat{\\mathbf{r}}$, the flux across any closed surface bounding mass $M_{\\text{enc}}$ is:
$$\\oint_S \\mathbf{g} \\cdot d\\mathbf{A} = -4\\pi G M_{\\text{enc}} = -4\\pi G \\iiint_V \\rho(\\mathbf{r}) dV$$
In differential form, this produces the field equation $\\boldsymbol{\\nabla} \\cdot \\mathbf{g} = -4\\pi G \\rho$.

<h4>3. Stokes’ Curl Theorem</h4>
Stokes' theorem transforms the surface integral of the curl over an open orientable surface $S$ into the line integral around its bounding closed contour $C = \\partial S$:
$$\\oint_C \\mathbf{F} \\cdot d\\mathbf{r} = \\iint_S (\\boldsymbol{\\nabla} \\times \\mathbf{F}) \\cdot d\\mathbf{A}$$
If $\\boldsymbol{\\nabla} \\times \\mathbf{F} = \\mathbf{0}$ throughout $S$, the contour integral is guaranteed to be zero for any closed path.`
        },
        {
          "id": "sec-2-2",
          "number": "§2.2",
          "heading": "Green’s Theorem in the Plane and Geometric Area Integrals",
          "simulation": "greens-theorem-sim",
          "content": `Green's Theorem is the two-dimensional planar specialization of Stokes' Theorem, establishing an equivalence between a line integral around a simple closed curve and a double integral over the bounded plane region.

<h4>1. Formal Statement of Green’s Theorem</h4>
Let $C$ be a positively oriented (counterclockwise), piecewise-smooth, simple closed curve in the $xy$-plane, and let $D$ be the region bounded by $C$. If $L(x, y)$ and $M(x, y)$ have continuous partial derivatives on an open region containing $D$, then:
$$\\oint_C (L\\, dx + M\\, dy) = \\iint_D \\left( \\frac{\\partial M}{\\partial x} - \\frac{\\partial L}{\\partial y} \\right) dA$$

<h4>2. Planar Area Computation via Contour Integration</h4>
By strategically choosing functions $L$ and $M$ such that $\\frac{\\partial M}{\\partial x} - \\frac{\\partial L}{\\partial y} = 1$:
<ul>
  <li>Case 1: $L = 0, M = x \\implies \\text{Area}(D) = \\oint_C x\\, dy$</li>
  <li>Case 2: $L = -y, M = 0 \\implies \\text{Area}(D) = -\\oint_C y\\, dx$</li>
  <li>Case 3 (Symmetric Form):
  $$\\text{Area}(D) = \\frac{1}{2} \\oint_C (x\\, dy - y\\, dx)$$
  </li>
</ul>
This formula allows the exact calculation of areas bounded by parametric curves (such as ellipses, astroids, and cardioids) via simple one-dimensional boundary integrals.`
        },
        {
          "id": "sec-2-3",
          "number": "§2.3",
          "heading": "Plane Polar Coordinates: Basis Vectors, Velocity, and Acceleration",
          "simulation": "polar-basis-sim",
          "content": `For central forces (e.g., planetary orbits) and rotational motion, planar polar coordinates $(r, \\theta)$ offer a vastly superior natural framework compared to Cartesian coordinates.

<h4>1. Polar Basis Vectors and Transformations</h4>
Coordinates are related by:
$$x = r \\cos \\theta, \\quad y = r \\sin \\theta, \\quad r = \\sqrt{x^2 + y^2}, \\quad \\theta = \\arctan\\left(\\frac{y}{x}\\right)$$

The orthonormal basis vectors are:
$$\\hat{\\mathbf{r}} = \\cos \\theta \\hat{\\mathbf{i}} + \\sin \\theta \\hat{\\mathbf{j}}, \\quad \\hat{\\boldsymbol{\\theta}} = -\\sin \\theta \\hat{\\mathbf{i}} + \\cos \\theta \\hat{\\mathbf{j}}$$
Unlike Cartesian unit vectors, $\\hat{\\mathbf{r}}$ and $\\hat{\\boldsymbol{\\theta}}$ vary with position as the angle $\\theta(t)$ changes in time!

Differentiating with respect to time using the chain rule:
$$\\frac{d\\hat{\\mathbf{r}}}{dt} = (-\\sin\\theta\\dot{\\theta})\\hat{\\mathbf{i}} + (\\cos\\theta\\dot{\\theta})\\hat{\\mathbf{j}} = \\dot{\\theta} \\hat{\\boldsymbol{\\theta}}$$
$$\\frac{d\\hat{\\boldsymbol{\\theta}}}{dt} = (-\\cos\\theta\\dot{\\theta})\\hat{\\mathbf{i}} - (\\sin\\theta\\dot{\\theta})\\hat{\\mathbf{j}} = -\\dot{\\theta} \\hat{\\mathbf{r}}$$

<h4>2. Kinematic Velocity in Polar Coordinates</h4>
The position vector is simply $\\mathbf{r} = r \\hat{\\mathbf{r}}$. Differentiating:
$$\\mathbf{v} = \\frac{d\\mathbf{r}}{dt} = \\frac{dr}{dt} \\hat{\\mathbf{r}} + r \\frac{d\\hat{\\mathbf{r}}}{dt} = \\dot{r} \\hat{\\mathbf{r}} + r \\dot{\\theta} \\hat{\\boldsymbol{\\theta}}$$
<ul>
  <li>$v_r = \\dot{r}$: Radial velocity.</li>
  <li>$v_\\theta = r\\dot{\\theta}$: Transverse (azimuthal) velocity.</li>
  <li>Speed: $v = \\sqrt{\\dot{r}^2 + r^2\\dot{\\theta}^2}$.</li>
</ul>

<h4>3. Kinematic Acceleration in Polar Coordinates</h4>
Differentiating velocity with respect to time:
$$\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d}{dt}(\\dot{r} \\hat{\\mathbf{r}} + r\\dot{\\theta} \\hat{\\boldsymbol{\\theta}}) = \\ddot{r}\\hat{\\mathbf{r}} + \\dot{r}\\dot{\\hat{\\mathbf{r}}} + \\dot{r}\\dot{\\theta}\\hat{\\boldsymbol{\\theta}} + r\\ddot{\\theta}\\hat{\\boldsymbol{\\theta}} + r\\dot{\\theta}\\dot{\\hat{\\boldsymbol{\\theta}}}$$
Substituting $\\dot{\\hat{\\mathbf{r}}} = \\dot{\\theta}\\hat{\\boldsymbol{\\theta}}$ and $\\dot{\\hat{\\boldsymbol{\\theta}}} = -\\dot{\\theta}\\hat{\\mathbf{r}}$:
$$\\mathbf{a} = (\\ddot{r} - r\\dot{\\theta}^2) \\hat{\\mathbf{r}} + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta}) \\hat{\\boldsymbol{\\theta}}$$
<ul>
  <li><strong>Radial Acceleration $a_r = \\ddot{r} - r\\dot{\\theta}^2$:</strong> Composed of linear radial acceleration $\\ddot{r}$ and the inward centripetal acceleration $-r\\dot{\\theta}^2$.</li>
  <li><strong>Transverse Acceleration $a_\\theta = r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta} = \\frac{1}{r}\\frac{d}{dt}(r^2 \\dot{\\theta})$:</strong> Contains the angular acceleration term $r\\ddot{\\theta}$ and the **Coriolis term** $2\\dot{r}\\dot{\\theta}$.</li>
  <li><em>Kepler's Second Law:</em> For a central force, $F_\\theta = 0 \\implies a_\\theta = 0 \\implies \\frac{d}{dt}(r^2\\dot{\\theta}) = 0 \\implies r^2\\dot{\\theta} = \\text{const}$, proving that areal velocity is strictly constant!</li>
</ul>`
        },
        {
          "id": "sec-2-4",
          "number": "§2.4",
          "heading": "Cylindrical and Spherical Coordinate Systems and Laplacian Operators",
          "simulation": "coordinate-systems-sim",
          "content": `Physical problems with axial symmetry (flywheels, rods) or central symmetry (gravitation, electrostatic potentials) are vastly simplified by cylindrical or spherical coordinates.

<h4>1. Cylindrical Coordinates $(r, \\theta, z)$</h4>
Transformation to Cartesian coordinates:
$$x = r \\cos \\theta, \\quad y = r \\sin \\theta, \\quad z = z$$

Orthonormal basis vectors:
$$\\hat{\\mathbf{r}} = \\cos \\theta \\hat{\\mathbf{i}} + \\sin \\theta \\hat{\\mathbf{j}}, \\quad \\hat{\\boldsymbol{\\theta}} = -\\sin \\theta \\hat{\\mathbf{i}} + \\cos \\theta \\hat{\\mathbf{j}}, \\quad \\hat{\\mathbf{z}} = \\hat{\\mathbf{k}}$$

Metric scale factors: $h_r = 1, h_\\theta = r, h_z = 1$. Infinitesimal line element:
$$d\\mathbf{r} = dr \\hat{\\mathbf{r}} + r d\\theta \\hat{\\boldsymbol{\\theta}} + dz \\hat{\\mathbf{z}}, \\quad dV = r \\, dr \\, d\\theta \\, dz$$

Differential operators in cylindrical coordinates:
$$\\boldsymbol{\\nabla}\\Phi = \\frac{\\partial \\Phi}{\\partial r} \\hat{\\mathbf{r}} + \\frac{1}{r} \\frac{\\partial \\Phi}{\\partial \\theta} \\hat{\\boldsymbol{\\theta}} + \\frac{\\partial \\Phi}{\\partial z} \\hat{\\mathbf{z}}$$
$$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} = \\frac{1}{r}\\frac{\\partial(r V_r)}{\\partial r} + \\frac{1}{r}\\frac{\\partial V_\\theta}{\\partial \\theta} + \\frac{\\partial V_z}{\\partial z}$$
$$\\nabla^2 \\Phi = \\frac{1}{r} \\frac{\\partial}{\\partial r}\\left(r \\frac{\\partial \\Phi}{\\partial r}\\right) + \\frac{1}{r^2}\\frac{\\partial^2 \\Phi}{\\partial \\theta^2} + \\frac{\\partial^2 \\Phi}{\\partial z^2}$$

<h4>2. Spherical Polar Coordinates $(r, \\theta, \\phi)$</h4>
Transformation ($\theta$ is colatitude / polar angle, $\\phi$ is azimuth):
$$x = r \\sin \\theta \\cos \\phi, \\quad y = r \\sin \\theta \\sin \\phi, \\quad z = r \\cos \\theta$$

Scale factors: $h_r = 1, h_\\theta = r, h_\\phi = r \\sin \\theta$. Differential volume element:
$$dV = r^2 \\sin \\theta \\, dr \\, d\\theta \\, d\\phi$$

Differential operators in spherical coordinates:
$$\\boldsymbol{\\nabla}\\Phi = \\frac{\\partial \\Phi}{\\partial r} \\hat{\\mathbf{r}} + \\frac{1}{r} \\frac{\\partial \\Phi}{\\partial \\theta} \\hat{\\boldsymbol{\\theta}} + \\frac{1}{r \\sin \\theta} \\frac{\\partial \\Phi}{\\partial \\phi} \\hat{\\boldsymbol{\\phi}}$$
$$\\boldsymbol{\\nabla} \\cdot \\mathbf{V} = \\frac{1}{r^2}\\frac{\\partial(r^2 V_r)}{\\partial r} + \\frac{1}{r \\sin \\theta}\\frac{\\partial(\\sin \\theta V_\\theta)}{\\partial \\theta} + \\frac{1}{r \\sin \\theta}\\frac{\\partial V_\\phi}{\\partial \\phi}$$
$$\\nabla^2 \\Phi = \\frac{1}{r^2} \\frac{\\partial}{\\partial r}\\left(r^2 \\frac{\\partial \\Phi}{\\partial r}\\right) + \\frac{1}{r^2 \\sin \\theta} \\frac{\\partial}{\\partial \\theta}\\left(\\sin \\theta \\frac{\\partial \\Phi}{\\partial \\theta}\\right) + \\frac{1}{r^2 \\sin^2 \\theta} \\frac{\\partial^2 \\Phi}{\\partial \\phi^2}$$`
        }
      ],
      "problems": [
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Gravitational Field of a Solid Sphere via Gauss's Theorem",
          "question": "Using Gauss's divergence theorem, determine the gravitational field $\\mathbf{g}(r)$ produced by a solid homogeneous sphere of radius $R$ and uniform mass density $\\rho_0$ for both (a) outside the sphere ($r \\ge R$), and (b) inside the sphere ($r < R$).",
          "steps": [
            {
              "title": "Step 1: Set up spherical Gaussian surface",
              "math": "$$\\oint_{S} \\mathbf{g} \\cdot d\\mathbf{A} = -4\\pi G M_{\\text{enc}}$$\n$$\\text{By spherical symmetry, } \\mathbf{g}(\\mathbf{r}) = -g(r)\\hat{\\mathbf{r}}$$\n$$\\oint_{S} (-g(r)\\hat{\\mathbf{r}}) \\cdot (dA \\hat{\\mathbf{r}}) = -g(r) (4\\pi r^2) = -4\\pi G M_{\\text{enc}} \\implies g(r) = \\frac{G M_{\\text{enc}}}{r^2}$$",
              "explanation": "Spherical symmetry guarantees that the field is purely radial and uniform over any concentric sphere."
            },
            {
              "title": "Step 2: Evaluate field outside and inside the mass distribution",
              "math": "$$\\text{For } r \\ge R: \\quad M_{\\text{enc}} = M = \\frac{4}{3}\\pi R^3 \\rho_0 \\implies \\mathbf{g}(r) = -\\frac{G M}{r^2} \\hat{\\mathbf{r}}$$\n$$\\text{For } r < R: \\quad M_{\\text{enc}} = \\frac{4}{3}\\pi r^3 \\rho_0 = M\\left(\\frac{r^3}{R^3}\\right) \\implies \\mathbf{g}(r) = -\\frac{G M r}{R^3} \\hat{\\mathbf{r}}$$ ",
              "explanation": "Outside, the sphere acts as a point mass $M$. Inside, the field increases linearly with radial distance $r$ from the center."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Area of an Ellipse using Green’s Theorem",
          "question": "An ellipse is parameterized by $x(t) = a \\cos t, y(t) = b \\sin t$ for $t \\in [0, 2\\pi]$. Use Green's Theorem symmetric contour integral $A = \\frac{1}{2}\\oint_C (x\\, dy - y\\, dx)$ to derive the exact area bounded by the ellipse.",
          "steps": [
            {
              "title": "Step 1: Compute differentials dx and dy",
              "math": "$$x = a \\cos t \\implies dx = -a \\sin t \\, dt$$\n$$y = b \\sin t \\implies dy = b \\cos t \\, dt$$",
              "explanation": "Parameterizing the boundary transforms the double integral into a one-dimensional periodic integral."
            },
            {
              "title": "Step 2: Evaluate contour integral around [0, 2π]",
              "math": "$$x\\, dy - y\\, dx = (a \\cos t)(b \\cos t \\, dt) - (b \\sin t)(-a \\sin t \\, dt) = a b (\\cos^2 t + \\sin^2 t) dt = ab \\, dt$$\n$$A = \\frac{1}{2} \\int_0^{2\\pi} ab \\, dt = \\frac{1}{2} ab (2\\pi) = \\pi a b$$",
              "explanation": "Green's Theorem yields the exact area formula $A = \\pi a b$ in two straightforward integration steps."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Kinematics of a Bead Sliding on a Uniformly Rotating Rod",
          "question": "A bead of mass $m$ slides frictionlessly along a straight rod rotating in a horizontal plane with constant angular velocity $\\omega = \\dot{\\theta}$. If the bead is released from rest relative to the rod at radial distance $r_0$ at $t = 0$: (a) write the radial equation of motion using polar coordinates, (b) solve for $r(t)$, and (c) find the transverse normal reaction force $N(t)$ exerted by the rod on the bead.",
          "steps": [
            {
              "title": "Step 1: Set up the radial dynamic equation",
              "math": "$$F_r = m a_r = m(\\ddot{r} - r\\dot{\\theta}^2) = m(\\ddot{r} - r\\omega^2)$$\n$$\\text{Since the rod is frictionless, } F_r = 0 \\implies \\ddot{r} - \\omega^2 r = 0$$",
              "explanation": "The outward centrifugal term in the rotating frame acts as a repulsive linear force."
            },
            {
              "title": "Step 2: Solve the differential equation with boundary conditions",
              "math": "$$r(t) = C_1 \\cosh(\\omega t) + C_2 \\sinh(\\omega t)$$\n$$r(0) = r_0 \\implies C_1 = r_0, \\quad \\dot{r}(0) = 0 \\implies C_2 = 0$$\n$$r(t) = r_0 \\cosh(\\omega t), \\quad \\dot{r}(t) = r_0 \\omega \\sinh(\\omega t)$$",
              "explanation": "The radial distance grows exponentially with hyperbolic cosine."
            },
            {
              "title": "Step 3: Determine the normal transverse force",
              "math": "$$N = F_\\theta = m a_\\theta = m(r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta}) = m(0 + 2\\dot{r}\\omega) = 2m\\omega \\dot{r}$$\n$$N(t) = 2m r_0 \\omega^2 \\sinh(\\omega t)$$",
              "explanation": "The transverse reaction force is strictly equal to the Coriolis force required to maintain the rod's angular velocity."
            }
          ]
        }
      ]
    },
    {
      "number": 3,
      "title": "Kinematics and Particle Dynamics",
      "leadSummary": "Inertial and non-inertial reference frames, Galilean relativity, fictitious forces, Frenet-Serret tangential and normal acceleration, projectile motion, circular dynamics, and dry friction.",
      "sections": [
        {
          "id": "sec-3-1",
          "number": "§3.1",
          "heading": "Frames of Reference, Galilean Invariance, and Non-Inertial Fictitious Forces",
          "simulation": "coriolis-fictitious-sim",
          "content": `Kinematics describes the geometry of motion, which is fundamentally relative to an observer's choice of reference frame.

<h4>1. Inertial Frames and the Principle of Galilean Relativity</h4>
An **inertial frame** is a reference frame in which Newton's first law holds: an isolated body free from external forces moves with constant velocity in a straight line.
If $S$ is an inertial frame and $S'$ moves relative to $S$ with constant translational velocity $\\mathbf{V}_0$:
$$\\mathbf{r}'(t) = \\mathbf{r}(t) - \\mathbf{V}_0 t, \\quad t' = t$$
Differentiating with respect to time:
$$\\mathbf{v}' = \\mathbf{v} - \\mathbf{V}_0, \\quad \\mathbf{a}' = \\frac{d\\mathbf{v}'}{dt} = \\frac{d\\mathbf{v}}{dt} = \\mathbf{a}$$
Because acceleration is identical in all inertial frames, Newton's second law $\\mathbf{F} = m\\mathbf{a}$ retains the exact same mathematical form in all inertial frames. This is the **Principle of Galilean Relativity**.

<h4>2. Linearly Accelerating Reference Frames</h4>
If frame $S'$ has translational acceleration $\\mathbf{A}_0(t)$ relative to inertial frame $S$:
$$\\mathbf{a}' = \\mathbf{a} - \\mathbf{A}_0$$
Multiplying by particle mass $m$:
$$m \\mathbf{a}' = m \\mathbf{a} - m \\mathbf{A}_0 = \\mathbf{F}_{\\text{real}} + \\mathbf{F}_{\\text{fictitious}}$$
where $\\mathbf{F}_{\\text{fictitious}} = -m\\mathbf{A}_0$ is an inertial (pseudo) force that must be added to preserve Newton's second law in the accelerating frame.

<h4>3. Rotating Reference Frames: Centrifugal and Coriolis Forces</h4>
If frame $S'$ rotates with angular velocity $\\boldsymbol{\\omega}$ about an axis passing through the origin of inertial frame $S$:
The time derivative of any vector $\\mathbf{Q}$ relates by the operator identity:
$$\\left(\\frac{d\\mathbf{Q}}{dt}\\right)_S = \\left(\\frac{d\\mathbf{Q}}{dt}\\right)_{S'} + \\boldsymbol{\\omega} \\times \\mathbf{Q}$$
Applying this twice to the position vector $\\mathbf{r}$ yields the exact transformation of accelerations:
$$\\mathbf{a}_S = \\mathbf{a}_{S'} + 2(\\boldsymbol{\\omega} \\times \\mathbf{v}_{S'}) + \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r}) + \\dot{\\boldsymbol{\\omega}} \\times \\mathbf{r}$$
The effective equation of motion in the rotating frame is:
$$m \\mathbf{a}_{S'} = \\mathbf{F}_{\\text{real}} + \\mathbf{F}_{\\text{coriolis}} + \\mathbf{F}_{\\text{centrifugal}} + \\mathbf{F}_{\\text{euler}}$$
where:
<ul>
  <li><strong>Coriolis Force:</strong> $\\mathbf{F}_{\\text{coriolis}} = -2m(\\boldsymbol{\\omega} \\times \\mathbf{v}_{S'})$. Acts perpendicular to velocity; deflects winds rightward in the Northern Hemisphere (cyclones).</li>
  <li><strong>Centrifugal Force:</strong> $\\mathbf{F}_{\\text{centrifugal}} = -m\\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r}) = m\\omega^2 \\mathbf{r}_\\perp$. Acts radially outward from the rotation axis.</li>
  <li><strong>Euler Force:</strong> $\\mathbf{F}_{\\text{euler}} = -m(\\dot{\\boldsymbol{\\omega}} \\times \\mathbf{r})$. Arises only when angular acceleration is non-zero.</li>
</ul>`
        },
        {
          "id": "sec-3-2",
          "number": "§3.2",
          "heading": "Frenet-Serret Coordinates: Tangential and Normal Acceleration",
          "simulation": "curvilinear-acceleration-sim",
          "content": `For general curvilinear motion along an arbitrary planar trajectory, intrinsic coordinates based on arc length $s(t)$ separate speed changes from directional changes.

<h4>1. Intrinsic Unit Basis Vectors</h4>
Let $\\hat{\\mathbf{t}}$ be the unit tangent vector pointing along velocity $\\mathbf{v}$, and let $\\hat{\\mathbf{n}}$ be the principal unit normal vector pointing toward the local center of curvature:
$$\\mathbf{v} = v \\hat{\\mathbf{t}}, \\quad v = \\frac{ds}{dt} = \\dot{s}$$

Differentiating with respect to time:
$$\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{dv}{dt} \\hat{\\mathbf{t}} + v \\frac{d\\hat{\\mathbf{t}}}{dt}$$
Using the geometric Frenet-Serret relation $\\frac{d\\hat{\\mathbf{t}}}{ds} = \\frac{1}{\\rho} \\hat{\\mathbf{n}}$, where $\\rho$ is the local radius of curvature:
$$\\frac{d\\hat{\\mathbf{t}}}{dt} = \\frac{d\\hat{\\mathbf{t}}}{ds}\\frac{ds}{dt} = \\left(\\frac{1}{\\rho}\\hat{\\mathbf{n}}\\right) v = \\frac{v}{\\rho} \\hat{\\mathbf{n}}$$

Substituting into the total acceleration:
$$\\mathbf{a} = a_t \\hat{\\mathbf{t}} + a_n \\hat{\\mathbf{n}} = \\left( \\frac{dv}{dt} \\right) \\hat{\\mathbf{t}} + \\left( \\frac{v^2}{\\rho} \\right) \\hat{\\mathbf{n}}$$

<h4>2. Dynamical Interpretation</h4>
<ul>
  <li><strong>Tangential Component ($a_t = \\dot{v} = \\ddot{s}$):</strong> Governs changes in the *magnitude* of velocity (speed). Caused by net forces parallel to trajectory: $F_t = m a_t$.</li>
  <li><strong>Normal (Centripetal) Component ($a_n = \\frac{v^2}{\\rho}$):</strong> Governs changes in the *direction* of velocity. Caused by net lateral forces perpendicular to trajectory: $F_n = m \\frac{v^2}{\\rho}$.</li>
  <li><strong>Total Acceleration Magnitude:</strong>
  $$a = \\sqrt{a_t^2 + a_n^2} = \\sqrt{\\left(\\frac{dv}{dt}\\right)^2 + \\left(\\frac{v^2}{\\rho}\\right)^2}$$
  </li>
  <li><strong>Radius of Curvature Formula:</strong> For a path expressed as $y = f(x)$:
  $$\\rho(x) = \\frac{[1 + (y')^2]^{3/2}}{|y''|}$$
  </li>
</ul>`
        },
        {
          "id": "sec-3-3",
          "number": "§3.3",
          "heading": "Projectile Motion in Two Dimensions (Flat and Inclined Planes)",
          "simulation": "projectile-motion-sim",
          "content": `Two-dimensional ballistic motion under constant gravitational acceleration provides the classical prototype of particle kinematics.

<h4>1. Kinematic Equations on Flat Terrain</h4>
For a particle launched from $(0, 0)$ with initial speed $v_0$ at angle $\\theta_0$ to horizontal:
$$a_x = 0, \\quad a_y = -g$$
Integrating:
$$v_x(t) = v_0 \\cos \\theta_0, \\quad v_y(t) = v_0 \\sin \\theta_0 - gt$$
$$x(t) = (v_0 \\cos \\theta_0) t, \\quad y(t) = (v_0 \\sin \\theta_0) t - \\frac{1}{2}gt^2$$

Eliminating $t$ yields the parabolic trajectory:
$$y(x) = x \\tan \\theta_0 - \\frac{g}{2 v_0^2 \\cos^2 \\theta_0} x^2$$

Trajectory metrics:
<ul>
  <li><strong>Time of Flight ($T$):</strong> $T = \\frac{2 v_0 \\sin \\theta_0}{g}$.</li>
  <li><strong>Maximum Height ($H$):</strong> $H = \\frac{v_0^2 \\sin^2 \\theta_0}{2g}$.</li>
  <li><strong>Horizontal Range ($R$):</strong> $R = \\frac{v_0^2 \\sin 2\\theta_0}{g}$, maximized at $\\theta_0 = 45^\\circ$.</li>
</ul>

<h4>2. Projectile on an Inclined Plane</h4>
When a projectile is launched at angle $\\alpha$ relative to horizontal onto a hill inclined at angle $\\beta$ ($\alpha > \\beta$):
Rotating axes so that $x'$ is along the slope and $y'$ is normal to the slope:
$$a_{x'} = -g \\sin \\beta, \\quad a_{y'} = -g \\cos \\beta$$
$$v_{0x'} = v_0 \\cos(\\alpha - \\beta), \\quad v_{0y'} = v_0 \\sin(\\alpha - \\beta)$$
Solving $y'(T) = 0$ gives time of flight:
$$T = \\frac{2 v_0 \\sin(\\alpha - \\beta)}{g \\cos \\beta}$$
Range along the inclined slope:
$$R_{\\text{incline}} = x'(T) = \\frac{2 v_0^2 \\cos \\alpha \\sin(\\alpha - \\beta)}{g \\cos^2 \\beta}$$
Maximized when the launch angle bisects the remaining angle: $\\alpha_{\\text{opt}} = \\frac{\\pi}{4} + \\frac{\\beta}{2}$.`
        },
        {
          "id": "sec-3-4",
          "number": "§3.4",
          "heading": "Uniform and Non-Uniform Circular Dynamics",
          "simulation": "uniform-circular-sim",
          "content": `Circular motion occurs when a particle moves along a circular path of fixed radius $R$.

<h4>1. Uniform Circular Motion</h4>
If speed $v$ is constant:
$$a_t = \\frac{dv}{dt} = 0, \\quad a_n = \\frac{v^2}{R} = \\omega^2 R$$
The acceleration is purely radial (centripetal), pointing toward the center. By Newton's second law:
$$F_c = m \\frac{v^2}{R} = m \\omega^2 R$$

<h4>2. Motion in a Vertical Circle</h4>
When a particle of mass $m$ is attached to a string of length $R$ and swung in a vertical plane under gravity:
By energy conservation between bottom (speed $v_0$) and angle $\\theta$ from bottom:
$$\\frac{1}{2}m v_0^2 = \\frac{1}{2}m v^2 + mgR(1 - \\cos \\theta) \\implies v^2 = v_0^2 - 2gR(1 - \\cos \\theta)$$
Newton's second law along the radial direction gives string tension $T$:
$$T - mg \\cos \\theta = \\frac{mv^2}{R} \\implies T = mg \\cos \\theta + \\frac{m}{R}[v_0^2 - 2gR(1 - \\cos \\theta)]$$
$$T(\\theta) = \\frac{m v_0^2}{R} - mg(2 - 3\\cos \\theta)$$

<strong>Critical Conditions:</strong>
<ul>
  <li>At top of loop ($\\theta = \\pi$): $T_{\\text{top}} = \\frac{m v_0^2}{R} - 5mg$. For the string not to go slack ($T_{\\text{top}} \\ge 0$):
  $$v_{\\text{top}} \\ge \\sqrt{gR}, \\quad v_0 \\ge \\sqrt{5gR}$$
  </li>
  <li>Difference in tension between bottom and top is always independent of launch speed:
  $$T_{\\text{bottom}} - T_{\\text{top}} = 6mg$$
  </li>
</ul>`
        },
        {
          "id": "sec-3-5",
          "number": "§3.5",
          "heading": "Newton’s Laws of Motion and Coulomb-Amontons Dry Friction",
          "simulation": "friction-newton-sim",
          "content": `Newtonian particle dynamics relates external forces to resulting particle trajectories.

<h4>1. Newton’s Three Laws</h4>
<ol>
  <li><strong>First Law (Inertia):</strong> A body remains in rest or uniform straight-line motion unless acted upon by a net force: $\\sum \\mathbf{F} = \\mathbf{0} \\implies \\mathbf{v} = \\text{const}$.</li>
  <li><strong>Second Law (Dynamical Evolution):</strong> Net force equals time rate of change of linear momentum $\\mathbf{p} = m\\mathbf{v}$:
  $$\\mathbf{F} = \\frac{d\\mathbf{p}}{dt} = m \\frac{d\\mathbf{v}}{dt} + \\mathbf{v} \\frac{dm}{dt}$$
  For constant mass: $\\mathbf{F} = m \\mathbf{a}$.</li>
  <li><strong>Third Law (Reciprocity):</strong> Pairwise mutual interaction forces between bodies $A$ and $B$ are collinear, equal in magnitude, and opposite in direction: $\\mathbf{F}_{AB} = -\\mathbf{F}_{BA}$.</li>
</ol>

<h4>2. Laws of Dry Friction (Coulomb-Amontons)</h4>
Contact forces parallel to surfaces arise from microscopic roughness and molecular bonding:
<ul>
  <li><strong>Static Friction ($f_s$):</strong> Self-adjusting force opposing applied force up to a maximum threshold:
  $$f_s \\le \\mu_s N$$
  </li>
  <li><strong>Kinetic Friction ($f_k$):</strong> Dynamic resistive force during relative sliding:
  $$f_k = \\mu_k N, \\quad \\text{with } \\mu_k < \\mu_s$$
  </li>
  <li><strong>Angle of Friction ($\\lambda$) and Angle of Repose ($\\theta_r$):</strong>
  The maximum static friction angle satisfies $\\tan \\lambda = \\mu_s$. On an inclined plane, a block begins sliding under gravity when slope exceeds the angle of repose $\\theta_r = \\arctan(\\mu_s)$.</li>
</ul>`
        }
      ],
      "problems": [
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Projectile with High Elevation on Inclined Plane",
          "question": "A projectile is launched with speed $v_0$ at angle $\\alpha$ above a planar hillside inclined at angle $\\beta$ to the horizontal ($\alpha > \\beta$). Derive an exact analytical expression for the range $R$ of the projectile measured along the inclined surface.",
          "steps": [
            {
              "title": "Step 1: Set up rotated coordinates along the inclined plane",
              "math": "$$\\text{Let } x' \\text{ be parallel to incline, } y' \\text{ perpendicular to incline}$$\n$$a_{x'} = -g \\sin \\beta, \\quad a_{y'} = -g \\cos \\beta$$\n$$v_{0x'} = v_0 \\cos(\\alpha - \\beta), \\quad v_{0y'} = v_0 \\sin(\\alpha - \\beta)$$",
              "explanation": "Decomposing gravity into components parallel and normal to the slope simplifies the impact boundary condition."
            },
            {
              "title": "Step 2: Solve for time of flight and range along incline",
              "math": "$$y'(T) = v_{0y'} T - \\frac{1}{2} g \\cos \\beta \\, T^2 = 0 \\implies T = \\frac{2 v_0 \\sin(\\alpha - \\beta)}{g \\cos \\beta}$$\n$$R = x'(T) = v_{0x'} T - \\frac{1}{2} g \\sin \\beta \\, T^2$$\n$$R = \\frac{2 v_0^2}{g \\cos^2 \\beta} \\sin(\\alpha - \\beta) \\cos \\alpha$$",
              "explanation": "The maximum range along the inclined plane is achieved when $\\alpha = \\frac{\\pi}{4} + \\frac{\\beta}{2}$."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Particle Sliding Off a Frictionless Spherical Dome",
          "question": "A particle of mass $m$ rests at the top of a smooth frictionless sphere of radius $R$. Given an infinitesimal nudge, it slides down under gravity. Determine the exact angle $\\theta_0$ measured from the vertical at which the particle loses contact with the sphere.",
          "steps": [
            {
              "title": "Step 1: Apply energy conservation from the top",
              "math": "$$E = mgR = \\frac{1}{2}m v^2 + mgR \\cos \\theta \\implies v^2 = 2gR(1 - \\cos \\theta)$$",
              "explanation": "Gravitational potential energy converted to kinetic energy depends solely on vertical drop."
            },
            {
              "title": "Step 2: Apply Newton's Second Law in radial direction",
              "math": "$$mg \\cos \\theta - N = m \\frac{v^2}{R} \\implies N = mg \\cos \\theta - \\frac{m}{R}(2gR(1 - \\cos \\theta)) = mg(3 \\cos \\theta - 2)$$",
              "explanation": "The normal contact force $N$ diminishes as speed increases."
            },
            {
              "title": "Step 3: Condition for loss of contact (N = 0)",
              "math": "$$N = 0 \\implies 3 \\cos \\theta_0 - 2 = 0 \\implies \\cos \\theta_0 = \\frac{2}{3} \\implies \\theta_0 = \\arccos\\left(\\frac{2}{3}\\right) \\approx 48.19^\\circ$$",
              "explanation": "The particle leaves the surface at $\\cos\\theta_0 = 2/3$, independent of particle mass and dome radius."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Minimum Horizontal Pushing Force on an Inclined Plane",
          "question": "A block of mass $m$ rests on an incline of angle $\\theta$ with coefficient of static friction $\\mu_s$. Determine the minimum horizontal force $F_h$ required to prevent the block from slipping down the incline.",
          "steps": [
            {
              "title": "Step 1: Resolve forces along and perpendicular to the incline",
              "math": "$$\\Sigma F_\\perp = N - mg \\cos \\theta - F_h \\sin \\theta = 0 \\implies N = mg \\cos \\theta + F_h \\sin \\theta$$\n$$\\Sigma F_\\parallel = F_h \\cos \\theta + f_s - mg \\sin \\theta = 0 \\implies f_s = mg \\sin \\theta - F_h \\cos \\theta$$",
              "explanation": "Static friction $f_s$ acts up the incline to prevent downward sliding."
            },
            {
              "title": "Step 2: Apply static friction threshold condition f_s <= μ_s N",
              "math": "$$mg \\sin \\theta - F_h \\cos \\theta \\le \\mu_s (mg \\cos \\theta + F_h \\sin \\theta)$$\n$$mg(\\sin \\theta - \\mu_s \\cos \\theta) \\le F_h (\\cos \\theta + \\mu_s \\sin \\theta)$$\n$$F_{h,\\min} = mg \\left( \\frac{\\sin \\theta - \\mu_s \\cos \\theta}{\\cos \\theta + \\mu_s \\sin \\theta} \\right) = mg \\tan(\\theta - \\lambda)$$",
              "explanation": "Here $\\lambda = \\arctan(\\mu_s)$ is the angle of friction."
            }
          ]
        }
      ]
    },
    {
      "number": 4,
      "title": "Work, Energy, and Power",
      "leadSummary": "Work-energy theorem, conservative and non-conservative forces, potential energy functions, one-dimensional potential wells, phase space, and equilibrium stability.",
      "sections": [
        {
          "id": "sec-4-1",
          "number": "§4.1",
          "heading": "Work Done by Constant and Variable Forces, and Instantaneous Power",
          "simulation": "work-energy-theorem-sim",
          "content": `Energy is the universal scalar measure of a dynamical system's state and capacity to perform physical work.

<h4>1. Work Done by a Variable Force Field</h4>
The mechanical work done by a force vector $\\mathbf{F}(\\mathbf{r})$ along a spatial curve from $\\mathbf{r}_1$ to $\\mathbf{r}_2$ is defined by the line integral:
$$W_{1\\to 2} = \\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} \\mathbf{F} \\cdot d\\mathbf{r} = \\int_{x_1}^{x_2} F_x dx + \\int_{y_1}^{y_2} F_y dy + \\int_{z_1}^{z_2} F_z dz$$

For an ideal linear elastic spring (Hooke's Law $\\mathbf{F} = -k x \\hat{\\mathbf{i}}$):
$$W = \\int_{x_1}^{x_2} (-kx) dx = -\\left[ \\frac{1}{2}kx_2^2 - \\frac{1}{2}kx_1^2 \\right] = -\\Delta U_{\\text{spring}}$$

<h4>2. Instantaneous Mechanical Power</h4>
Power is the instantaneous time rate of doing work:
$$P = \\frac{dW}{dt} = \\mathbf{F} \\cdot \\frac{d\\mathbf{r}}{dt} = \\mathbf{F} \\cdot \\mathbf{v}$$
If power is supplied to a vehicle of mass $m$ at a constant rate $P_0$, integrating $m v \\frac{dv}{dt} = P_0$ gives $v(t) = \\sqrt{\\frac{2 P_0 t}{m}}$.`
        },
        {
          "id": "sec-4-2",
          "number": "§4.2",
          "heading": "Rigorous Derivation of the Work-Energy Theorem",
          "simulation": "energy-conservation-sim",
          "content": `The Work-Energy Theorem is the first integral of Newton's second law with respect to spatial displacement.

<h4>1. Analytical Proof for a Single Particle</h4>
Consider a particle of constant mass $m$ acted upon by a net force $\\mathbf{F}_{\\text{net}} = m \\frac{d\\mathbf{v}}{dt}$. The work done along trajectory $C$ from $t_1$ to $t_2$ is:
$$W_{\\text{net}} = \\int_C \\mathbf{F}_{\\text{net}} \\cdot d\\mathbf{r} = \\int_{t_1}^{t_2} \\left( m \\frac{d\\mathbf{v}}{dt} \\right) \\cdot \\left( \\frac{d\\mathbf{r}}{dt} \\right) dt = \\int_{t_1}^{t_2} m \\frac{d\\mathbf{v}}{dt} \\cdot \\mathbf{v} \\, dt$$

Using the vector identity $\\frac{d}{dt}(v^2) = \\frac{d}{dt}(\\mathbf{v} \\cdot \\mathbf{v}) = 2 \\mathbf{v} \\cdot \\frac{d\\mathbf{v}}{dt}$:
$$W_{\\text{net}} = m \\int_{t_1}^{t_2} \\frac{1}{2} \\frac{d(v^2)}{dt} dt = \\frac{1}{2}m v_2^2 - \\frac{1}{2}m v_1^2 = K_2 - K_1 = \\Delta K$$

<strong>The Work-Energy Theorem:</strong> The total work performed on a particle by all concurrent forces (conservative, non-conservative, and constraint forces) equals the net change in its kinetic energy:
$$W_{\\text{total}} = \\Delta K$$

<h4>2. Decomposition into Conservative and Non-Conservative Work</h4>
Decomposing forces into conservative $\\mathbf{F}_c$ and non-conservative $\\mathbf{F}_{nc}$ (e.g., friction, drag):
$$W_{\\text{total}} = W_c + W_{nc} = -\\Delta U + W_{nc} = \\Delta K$$
Rearranging gives the general mechanical energy evolution equation:
$$\\Delta (K + U) = \\Delta E_{\\text{mech}} = W_{nc}$$
If only conservative forces perform work ($W_{nc} = 0$):
$$E_{\\text{mech}} = K + U = \\text{constant}$$`
        },
        {
          "id": "sec-4-3",
          "number": "§4.3",
          "heading": "Conservative Systems, Potential Energy Surfaces, and Equipotentials",
          "simulation": "two-dim-potential-sim",
          "content": `A force field is conservative if the work it performs along any path depends solely on the initial and final endpoints.

<h4>1. Potential Energy Functions in 2D and 3D</h4>
For a conservative force field $\\mathbf{F}(\\mathbf{r})$:
$$U(\\mathbf{r}) = -\\int_{\\mathbf{r}_{\\text{ref}}}^{\\mathbf{r}} \\mathbf{F}(\\mathbf{r}') \\cdot d\\mathbf{r}' \\iff \\mathbf{F}(\\mathbf{r}) = -\\boldsymbol{\\nabla}U(\\mathbf{r})$$

In Cartesian components:
$$F_x = -\\frac{\\partial U}{\\partial x}, \\quad F_y = -\\frac{\\partial U}{\\partial y}, \\quad F_z = -\\frac{\\partial U}{\\partial z}$$

<h4>2. Equipotential Surfaces and Force Orthogonality</h4>
An **equipotential surface** is defined by $U(x, y, z) = C = \\text{const}$.
Along an infinitesimal displacement $d\\mathbf{r}$ tangent to the equipotential surface:
$$dU = \\boldsymbol{\\nabla}U \\cdot d\\mathbf{r} = 0 \\implies -\\mathbf{F} \\cdot d\\mathbf{r} = 0$$
Therefore, conservative force vectors are **strictly perpendicular to equipotential surfaces** everywhere in space, pointing in the direction of steepest descent of potential energy.`
        },
        {
          "id": "sec-4-4",
          "number": "§4.4",
          "heading": "One-Dimensional Potential Wells, Turning Points, and Stability Criteria",
          "simulation": "potential-well-sim",
          "content": `For a particle moving in a 1D potential $U(x)$, its motion is completely characterized by the energy conservation relation:
$$E = \\frac{1}{2}m \\dot{x}^2 + U(x) = \\text{constant}$$

Solving for velocity $\\dot{x} = \\frac{dx}{dt}$:
$$\\frac{dx}{dt} = \\pm \\sqrt{\\frac{2}{m}[E - U(x)]}$$
Because kinetic energy $K = \\frac{1}{2}m\\dot{x}^2 \\ge 0$, motion is physically permitted only where $E \\ge U(x)$. Points where $E = U(x)$ are the **turning points**, where velocity vanishes and reverses.

<h4>1. Equilibrium Points and Stability Criteria</h4>
Equilibrium occurs where the net force vanishes:
$$F(x) = -\\frac{dU}{dx} = 0$$
The stability of an equilibrium point $x_0$ is dictated by the curvature $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0}$:
<ul>
  <li><strong>Stable Equilibrium (Local Minimum):</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} > 0$. Displacements produce a restoring force. Small oscillations have angular frequency:
  $$\\omega_0 = \\sqrt{\\frac{k_{\\text{eff}}}{m}}, \\quad k_{\\text{eff}} = \\left.\\frac{d^2 U}{dx^2}\\right|_{x_0}$$
  </li>
  <li><strong>Unstable Equilibrium (Local Maximum):</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} < 0$. Displacements produce runaway forces away from $x_0$.</li>
  <li><strong>Neutral Equilibrium:</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} = 0$.</li>
</ul>

<h4>2. Exact Period of Bounded Oscillations</h4>
For a particle trapped between turning points $x_1$ and $x_2$:
$$T = 2 \\int_{x_1}^{x_2} \\frac{dx}{\\sqrt{\\frac{2}{m}[E - U(x)]}}$$`
        }
      ],
      "problems": [
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Period of Small Oscillations in a Lennard-Jones Potential",
          "question": "A particle of mass $m$ moves in the diatomic molecular potential $U(r) = \\frac{A}{r^{12}} - \\frac{B}{r^6}$ where $A, B > 0$. (a) Find the equilibrium distance $r_0$. (b) Prove that the equilibrium is stable. (c) Derive the angular frequency $\\omega_0$ of small oscillations about equilibrium.",
          "steps": [
            {
              "title": "Step 1: Find equilibrium separation r_0",
              "math": "$$\\frac{dU}{dr} = -\\frac{12A}{r^{13}} + \\frac{6B}{r^7} = 0 \\implies 6B r^6 = 12A \\implies r_0 = \\left( \\frac{2A}{B} \\right)^{1/6}$$",
              "explanation": "Setting the gradient of potential energy to zero yields the equilibrium point."
            },
            {
              "title": "Step 2: Determine effective spring constant k_eff",
              "math": "$$\\frac{d^2 U}{dr^2} = \\frac{156A}{r^{14}} - \\frac{42B}{r^8}$$\n$$\\text{Substitute } r_0^6 = \\frac{2A}{B}: \\quad k_{\\text{eff}} = \\frac{156A}{(2A/B) r_0^8} - \\frac{42B}{r_0^8} = \\frac{78B - 42B}{r_0^8} = \\frac{36B}{r_0^8} > 0$$",
              "explanation": "Since the second derivative is strictly positive, the equilibrium is stable."
            },
            {
              "title": "Step 3: Angular frequency of small oscillations",
              "math": "$$\\omega_0 = \\sqrt{\\frac{k_{\\text{eff}}}{m}} = \\sqrt{\\frac{36B}{m r_0^8}} = \\frac{6}{r_0^4} \\sqrt{\\frac{B}{m}}$$",
              "explanation": "For small deviations $\\delta r = r - r_0$, the system executes simple harmonic motion."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Minimum Release Height for Looping-the-Loop",
          "question": "A small block of mass $m$ slides down a frictionless track and enters a circular loop of radius $R$. Find the minimum height $h_{\\min}$ above the bottom of the loop from which the block must be released from rest so that it completes the loop without falling off.",
          "steps": [
            {
              "title": "Step 1: Determine critical speed at the top of the loop",
              "math": "$$N + mg = m \\frac{v_{\\text{top}}^2}{R} \\implies N = m \\left( \\frac{v_{\\text{top}}^2}{R} - g \\right) \\ge 0 \\implies v_{\\text{top}}^2 \\ge g R$$",
              "explanation": "To maintain contact, the normal force $N$ at the apex must be non-negative."
            },
            {
              "title": "Step 2: Apply conservation of mechanical energy between start and top",
              "math": "$$m g h = m g (2R) + \\frac{1}{2}m v_{\\text{top}}^2$$\n$$g h = 2gR + \\frac{1}{2}gR = \\frac{5}{2}gR \\implies h_{\\min} = \\frac{5}{2}R = 2.5 R$$",
              "explanation": "The block must be released at a height of at least 2.5 times the loop radius."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Analytical Oscillation Frequency in a Pöschl-Teller Type Potential",
          "question": "A particle of mass $m$ moves in the asymmetric potential $U(x) = U_0 \\left( e^{-2\\alpha x} - 2e^{-\\alpha x} \\right)$ with $U_0, \\alpha > 0$. (a) Determine the equilibrium position $x_0$. (b) Determine the depth of the potential well. (c) Derive the frequency $\\omega_0$ of small oscillations.",
          "steps": [
            {
              "title": "Step 1: Find equilibrium position",
              "math": "$$\\frac{dU}{dx} = U_0 \\left( -2\\alpha e^{-2\\alpha x} + 2\\alpha e^{-\\alpha x} \\right) = 2\\alpha U_0 e^{-\\alpha x} (1 - e^{-\\alpha x}) = 0$$\n$$e^{-\\alpha x_0} = 1 \\implies x_0 = 0$$",
              "explanation": "The equilibrium point occurs at the origin $x_0 = 0$."
            },
            {
              "title": "Step 2: Calculate well depth and second derivative",
              "math": "$$U(0) = U_0 (1 - 2) = -U_0$$\n$$\\frac{d^2 U}{dx^2} = 2\\alpha U_0 \\left( -\\alpha e^{-\\alpha x} + 2\\alpha e^{-2\\alpha x} \\right)$$\n$$\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0=0} = 2\\alpha^2 U_0 (-1 + 2) = 2\\alpha^2 U_0 > 0$$",
              "explanation": "The potential well has depth $U_0$ and positive curvature, confirming stability."
            },
            {
              "title": "Step 3: Compute angular frequency of small oscillations",
              "math": "$$\\omega_0 = \\sqrt{\\frac{k_{\\text{eff}}}{m}} = \\sqrt{\\frac{2\\alpha^2 U_0}{m}} = \\alpha \\sqrt{\\frac{2 U_0}{m}}$$",
              "explanation": "The small-amplitude oscillation frequency scales linearly with the spatial decay factor $\\alpha$."
            }
          ]
        }
      ]
    },
    {
      "number": 5,
      "title": "Conservation of Linear Momentum",
      "leadSummary": "Center of mass for discrete and continuous systems, Tsiolkovsky rocket equation, variable-mass systems, and 1D/2D collisions in Laboratory and Center-of-Mass frames.",
      "sections": [
        {
          "id": "sec-5-1",
          "number": "§5.1",
          "heading": "Center of Mass of Discrete Systems and Continuous Bodies",
          "simulation": "center-of-mass-sim",
          "content": `For an extended body or a collection of $N$ interacting particles of masses $m_i$ at positions $\\mathbf{r}_i$:

<h4>1. Discrete Particle Systems</h4>
The center of mass position vector $\\mathbf{R}_{\\text{cm}}$ is the mass-weighted average position:
$$\\mathbf{R}_{\\text{cm}} = \\frac{1}{M} \\sum_{i=1}^N m_i \\mathbf{r}_i, \\quad M = \\sum_{i=1}^N m_i$$

<h4>2. Continuous Mass Distributions</h4>
For a continuous body with mass density $\\rho(\\mathbf{r})$:
$$\\mathbf{R}_{\\text{cm}} = \\frac{1}{M} \\iiint_V \\mathbf{r} \\, \\rho(\\mathbf{r}) \\, dV, \\quad M = \\iiint_V \\rho(\\mathbf{r}) \\, dV$$

<h4>3. Analytical Center of Mass for Standard Geometries</h4>
<ul>
  <li><strong>Uniform Semicircular Wire of Radius $R$:</strong>
  Let wire lie in $xy$-plane ($y \\ge 0$). Linear density $\\lambda = M/(\\pi R)$. $dm = \\lambda R d\\theta$:
  $$y_{\\text{cm}} = \\frac{1}{M} \\int_0^\\pi (R \\sin \\theta) (\\lambda R d\\theta) = \\frac{\\lambda R^2}{M} [-\\cos\\theta]_0^\\pi = \\frac{2 R}{\\pi} \\approx 0.637 R$$
  </li>
  <li><strong>Uniform Semicircular Disc of Radius $R$:</strong>
  Surface density $\\sigma = \\frac{2M}{\\pi R^2}$. Slice into concentric rings of radius $r$:
  $$y_{\\text{cm}} = \\frac{1}{M} \\int_0^R \\left(\\frac{2r}{\\pi}\\right) (\\pi r \\sigma dr) = \\frac{2\\sigma}{M} \\int_0^R r^2 dr = \\frac{4 R}{3\\pi} \\approx 0.424 R$$
  </li>
  <li><strong>Uniform Solid Hemisphere of Radius $R$:</strong>
  Slice into horizontal discs of height $z$ ($z \\in [0, R]$):
  $$z_{\\text{cm}} = \\frac{3 R}{8} = 0.375 R$$
  </li>
</ul>`
        },
        {
          "id": "sec-5-2",
          "number": "§5.2",
          "heading": "Multi-Particle Dynamics and Linear Momentum Conservation",
          "simulation": "collision-lab-cm-sim",
          "content": `The total linear momentum $\\mathbf{P}$ of an $N$-particle system is:
$$\\mathbf{P} = \\sum_{i=1}^N \\mathbf{p}_i = \\sum_{i=1}^N m_i \\mathbf{v}_i = M \\mathbf{v}_{\\text{cm}}$$

<h4>1. Equation of Motion for the Center of Mass</h4>
Differentiating total momentum with respect to time:
$$\\frac{d\\mathbf{P}}{dt} = M \\mathbf{a}_{\\text{cm}} = \\sum_{i=1}^N \\mathbf{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\mathbf{F}_{ij}^{\\text{int}}$$

By Newton's third law in strong form, mutual internal forces between particles cancel identically in pairs:
$$\\mathbf{F}_{ij}^{\\text{int}} + \\mathbf{F}_{ji}^{\\text{int}} = \\mathbf{0}$$
Therefore:
$$\\frac{d\\mathbf{P}}{dt} = M \\mathbf{a}_{\\text{cm}} = \\mathbf{F}_{\\text{net}}^{\\text{ext}}$$

<strong>Law of Conservation of Linear Momentum:</strong>
If the net external force on a system vanishes ($\\mathbf{F}_{\\text{net}}^{\\text{ext}} = \\mathbf{0}$):
$$\\mathbf{P} = M \\mathbf{v}_{\\text{cm}} = \\text{constant}$$
The center of mass moves with constant velocity regardless of complex internal explosions or collisions!`
        },
        {
          "id": "sec-5-3",
          "number": "§5.3",
          "heading": "Variable-Mass Dynamics and the Tsiolkovsky Rocket Equation",
          "simulation": "rocket-propulsion-sim",
          "content": `Newton's second law $\\mathbf{F} = \\frac{d\\mathbf{p}}{dt}$ must be applied rigorously to open systems where mass continuously enters or leaves the control volume.

<h4>1. Derivation of the Rocket Equation of Motion</h4>
Consider a rocket of mass $m(t)$ moving with velocity $\\mathbf{v}(t)$. During time $dt$, propellant mass $(-dm > 0)$ is ejected with exhaust velocity $\\mathbf{u}_{\\text{ex}}$ relative to the rocket.
Linear momentum at time $t$: $p(t) = m v$.
Linear momentum at time $t + dt$:
$$p(t+dt) = (m + dm)(v + dv) + (-dm)(v - u_{\\text{ex}}) = mv + m\\,dv + u_{\\text{ex}}\\,dm$$
Change in momentum:
$$dp = p(t+dt) - p(t) = m\\,dv + u_{\\text{ex}}\\,dm$$
Applying external force $F_{\\text{ext}}$:
$$F_{\\text{ext}} = \\frac{dp}{dt} = m \\frac{dv}{dt} + u_{\\text{ex}} \\frac{dm}{dt}$$
Rearranging gives the rocket dynamical equation:
$$m \\frac{dv}{dt} = -u_{\\text{ex}} \\frac{dm}{dt} + F_{\\text{ext}} = T_{\\text{thrust}} + F_{\\text{ext}}$$
where $T_{\\text{thrust}} = u_{\\text{ex}}|\\dot{m}|$ is the thrust force.

<h4>2. Free Space Tsiolkovsky Equation</h4>
In deep space with zero external forces ($F_{\\text{ext}} = 0$):
$$m dv = -u_{\\text{ex}} dm \\implies dv = -u_{\\text{ex}} \\frac{dm}{m}$$
Integrating from initial state $(m_0, v_0)$ to final burnout $(m_f, v_f)$:
$$\\Delta v = v_f - v_0 = u_{\\text{ex}} \\ln\\left( \\frac{m_0}{m_f} \\right)$$

<h4>3. Vertical Ascent Under Gravity</h4>
For vertical launch against uniform gravity $g$:
$$v(t) = -gt + u_{\\text{ex}} \\ln\\left( \\frac{m_0}{m_0 - \\alpha t} \\right)$$`
        },
        {
          "id": "sec-5-4",
          "number": "§5.4",
          "heading": "Collision Phenomena in Laboratory and Center-of-Mass Frames",
          "simulation": "ballistic-pendulum-sim",
          "content": `Collisions are intense brief interactions where internal contact impulses vastly exceed external forces.

<h4>1. Classification by Kinetic Energy and Coefficient of Restitution</h4>
The coefficient of restitution $e$ along the line of impact is:
$$e = -\\frac{v_{2f} - v_{1f}}{v_{2i} - v_{1i}} = \\frac{\\text{relative separation speed}}{\\text{relative approach speed}}$$
<ul>
  <li><strong>Elastic ($e = 1$):</strong> Total mechanical kinetic energy is conserved: $K_f = K_i$.</li>
  <li><strong>Inelastic ($0 < e < 1$):</strong> Energy is partially dissipated into deformation and heat: $K_f < K_i$.</li>
  <li><strong>Completely Inelastic ($e = 0$):</strong> Bodies coalesce and move together with velocity $\\mathbf{v}_f = \\mathbf{v}_{\\text{cm}}$.</li>
</ul>

<h4>2. Laboratory vs Center-of-Mass (CM) Frame</h4>
In the CM frame, total momentum is identically zero: $m_1 \\mathbf{u}_1 + m_2 \\mathbf{u}_2 = \\mathbf{0}$.
In an elastic collision in the CM frame, the speeds of the particles are completely unchanged ($u_1' = u_1, u_2' = u_2$); the collision merely rotates the relative velocity vector by scattering angle $\\theta^*$.
The laboratory scattering angle $\\theta$ relates to CM angle $\\theta^*$ by:
$$\\tan \\theta = \\frac{\\sin \\theta^*}{\\cos \\theta^* + \\frac{m_1}{m_2}}$$`
        }
      ],
      "problems": [
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Two-Stage Rocket Burnout Velocity Optimization",
          "question": "A rocket has initial total mass $M_0$ and structural payload fraction $f_s = 0.10$ for each stage. The effective exhaust velocity is $u_{\\text{ex}} = 3000\\text{ m/s}$. Compare the final burnout velocity $\\Delta v$ achieved by: (a) a single-stage rocket consuming $80\\%$ of its mass in fuel, versus (b) a two-stage rocket with equal mass ratio per stage.",
          "steps": [
            {
              "title": "Step 1: Compute single-stage velocity",
              "math": "$$\\text{Initial mass } m_0 = M_0, \\quad \\text{Final mass } m_f = 0.20 M_0$$\n$$\\Delta v_1 = u_{\\text{ex}} \\ln\\left(\\frac{M_0}{0.20 M_0}\\right) = 3000 \\ln(5) \\approx 3000(1.6094) = 4828 \\text{ m/s}$$",
              "explanation": "Single stage burnout reaches $4828\\text{ m/s}$."
            },
            {
              "title": "Step 2: Compute two-stage rocket velocity",
              "math": "$$\\text{For two equal stages with stage mass ratio } \\frac{m_{0,i}}{m_{f,i}} = 3.162$$\n$$\\Delta v_2 = 2 \\times u_{\\text{ex}} \\ln(3.162) = 2 \\times 3000 \\times 1.151 \\approx 6907 \\text{ m/s}$$",
              "explanation": "Staging sheds empty structural mass, delivering over $2000\\text{ m/s}$ higher final velocity for the same fuel mass."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Derivation of Center of Mass for a Solid Uniform Hemisphere",
          "question": "Derive by analytical volume integration the center of mass position $z_{\\text{cm}}$ of a solid homogeneous hemisphere of radius $R$ and uniform mass density $\\rho_0$, bounded by $z \\ge 0$ and $x^2 + y^2 + z^2 \\le R^2$.",
          "steps": [
            {
              "title": "Step 1: Slice the hemisphere into thin horizontal circular discs",
              "math": "$$\\text{At height } z \\in [0, R], \\text{ radius of disc is } r(z) = \\sqrt{R^2 - z^2}$$\n$$dV = \\pi r(z)^2 dz = \\pi (R^2 - z^2) dz$$\n$$M = \\rho_0 \\int_0^R \\pi (R^2 - z^2) dz = \\rho_0 \\pi \\left[ R^2 z - \\frac{z^3}{3} \\right]_0^R = \\frac{2}{3}\\pi \\rho_0 R^3$$",
              "explanation": "This confirms the total volume of the hemisphere is $\\frac{2}{3}\\pi R^3$."
            },
            {
              "title": "Step 2: Evaluate first moment of mass integral",
              "math": "$$\\int z \\, dm = \\rho_0 \\pi \\int_0^R z(R^2 - z^2) dz = \\rho_0 \\pi \\int_0^R (R^2 z - z^3) dz = \\rho_0 \\pi \\left[ \\frac{R^2 z^2}{2} - \\frac{z^4}{4} \\right]_0^R = \\frac{1}{4}\\pi \\rho_0 R^4$$\n$$z_{\\text{cm}} = \\frac{\\int z \\, dm}{M} = \\frac{\\frac{1}{4}\\pi \\rho_0 R^4}{\\frac{2}{3}\\pi \\rho_0 R^3} = \\frac{3}{8} R$$",
              "explanation": "The center of mass of a solid hemisphere lies exactly $3/8 R$ above the planar base."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Ballistic Pendulum Velocity Determination",
          "question": "A bullet of mass $m = 10\\text{ g}$ is fired horizontally with unknown velocity $v_0$ into a wooden block of mass $M = 1.99\\text{ kg}$ suspended by a light vertical cord of length $L = 2.0\\text{ m}$. The bullet embeds completely into the block, and the combination swings upward through a vertical height $h = 10.0\\text{ cm}$. Determine the bullet launch speed $v_0$.",
          "steps": [
            {
              "title": "Step 1: Apply momentum conservation during impact",
              "math": "$$m v_0 = (m + M) V \\implies V = \\frac{m}{m + M} v_0$$",
              "explanation": "Collision is completely inelastic, conserving linear momentum during the brief impact time."
            },
            {
              "title": "Step 2: Apply energy conservation during subsequent swing",
              "math": "$$\\frac{1}{2}(m + M) V^2 = (m + M) g h \\implies V = \\sqrt{2 g h} = \\sqrt{2(9.80)(0.10)} = \\sqrt{1.96} = 1.40 \\text{ m/s}$$\n$$v_0 = \\left(\\frac{m + M}{m}\\right) V = \\left(\\frac{2.00}{0.010}\\right) (1.40) = 200 \\times 1.40 = 280 \\text{ m/s}$$",
              "explanation": "The bullet launch velocity was exactly $280\\text{ m/s}$."
            }
          ]
        }
      ]
    },
    {
      "number": 6,
      "title": "Rotational Kinematics & Dynamics",
      "leadSummary": "Angular velocity vectors, torque, angular momentum conservation, moment of inertia tensor, parallel and perpendicular axis theorems, and pure rolling motion without slipping.",
      "sections": [
        {
          "id": "sec-6-1",
          "number": "§6.1",
          "heading": "Rotational Kinematics and the Angular Velocity Vector",
          "simulation": "rotational-kinematics-sim",
          "content": `A rigid body is an idealized system of particles in which all mutual pairwise distances $|\\mathbf{r}_i - \\mathbf{r}_j|$ remain strictly constant in time.

<h4>1. The Angular Velocity Vector $\\boldsymbol{\\omega}$</h4>
For a rigid body rotating about an instantaneous axis, its angular velocity vector $\\boldsymbol{\\omega}$ points along the axis of rotation by the right-hand rule.
The linear velocity $\\mathbf{v}$ of any point at position $\\mathbf{r}$ relative to an origin on the rotation axis is:
$$\\mathbf{v} = \\boldsymbol{\\omega} \\times \\mathbf{r}$$

Differentiating with respect to time gives total linear acceleration:
$$\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d\\boldsymbol{\\omega}}{dt} \\times \\mathbf{r} + \\boldsymbol{\\omega} \\times \\frac{d\\mathbf{r}}{dt} = \\boldsymbol{\\alpha} \\times \\mathbf{r} + \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r})$$
<ul>
  <li>$\\mathbf{a}_t = \\boldsymbol{\\alpha} \\times \\mathbf{r}$: Tangential acceleration (from angular acceleration $\\boldsymbol{\\alpha} = \\dot{\\boldsymbol{\\omega}}$).</li>
  <li>$\\mathbf{a}_c = \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r}) = -\\omega^2 \\mathbf{r}_\\perp$: Centripetal acceleration pointing perpendicular to the rotation axis.</li>
</ul>

<h4>2. Kinematic Equations for Constant Angular Acceleration $\\alpha$</h4>
$$\\omega(t) = \\omega_0 + \\alpha t, \\quad \\theta(t) = \\omega_0 t + \\frac{1}{2} \\alpha t^2, \\quad \\omega^2 = \\omega_0^2 + 2 \\alpha \\Delta\\theta$$`
        },
        {
          "id": "sec-6-2",
          "number": "§6.2",
          "heading": "Torque, Angular Momentum, and Kepler's Second Law",
          "simulation": "angular-momentum-sim",
          "content": `Rotational dynamics represents the rotational counterpart to translational Newtonian mechanics.

<h4>1. Torque and Angular Momentum</h4>
For a particle acted upon by force $\\mathbf{F}$ at position $\\mathbf{r}$:
$$\\boldsymbol{\\tau} = \\mathbf{r} \\times \\mathbf{F} \\quad (\\text{Torque}), \\quad \\mathbf{L} = \\mathbf{r} \\times \\mathbf{p} = \\mathbf{r} \\times (m\\mathbf{v}) \\quad (\\text{Angular Momentum})$$

Differentiating $\\mathbf{L}$ with respect to time:
$$\\frac{d\\mathbf{L}}{dt} = \\frac{d\\mathbf{r}}{dt} \\times \\mathbf{p} + \\mathbf{r} \\times \\frac{d\\mathbf{p}}{dt} = (\\mathbf{v} \\times m\\mathbf{v}) + \\mathbf{r} \\times \\mathbf{F} = \\mathbf{0} + \\boldsymbol{\\tau} = \\boldsymbol{\\tau}_{\\text{net}}$$

<strong>Conservation of Angular Momentum:</strong>
If net external torque vanishes ($\\boldsymbol{\\tau}_{\\text{net}} = \\mathbf{0}$):
$$\\mathbf{L} = \\text{constant}$$

<h4>2. Central Forces and Kepler's Second Law</h4>
A **central force** acts along the line joining the particle to the origin: $\\mathbf{F}(\\mathbf{r}) = f(r)\\hat{\\mathbf{r}}$.
$$\\boldsymbol{\\tau} = \\mathbf{r} \\times (f(r)\\hat{\\mathbf{r}}) = \\mathbf{0} \\implies \\mathbf{L} = \\text{constant}$$
Because $\\mathbf{r} \\cdot \\mathbf{L} = \\mathbf{r} \\cdot (\\mathbf{r} \\times \\mathbf{p}) = 0$, the particle's trajectory is strictly confined to a fixed plane perpendicular to $\\mathbf{L}$.
The swept-out area in time $dt$ is $dA = \\frac{1}{2}|\\mathbf{r} \\times d\\mathbf{r}| = \\frac{1}{2}|\\mathbf{r} \\times \\mathbf{v}| dt$:
$$\\frac{dA}{dt} = \\frac{|\\mathbf{L}|}{2m} = \\text{constant} \\quad (\\text{Kepler's Second Law: Equal areas in equal times!})$$`
        },
        {
          "id": "sec-6-3",
          "number": "§6.3",
          "heading": "Rotational Kinetic Energy and Calculation of Moments of Inertia",
          "simulation": "moment-of-inertia-sim",
          "content": `For rotation about a fixed axis (say, the $z$-axis), the kinetic energy is:
$$K_{\\text{rot}} = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2 = \\frac{1}{2} \\sum_{i=1}^N m_i (r_{\\perp, i} \\omega)^2 = \\frac{1}{2} \\left( \\sum_{i=1}^N m_i r_{\\perp, i}^2 \\right) \\omega^2 = \\frac{1}{2} I \\omega^2$$
where the **Moment of Inertia** $I$ is:
$$I = \\sum_{i=1}^N m_i r_{\\perp, i}^2 = \\iiint_V r_\\perp^2 \\rho(\\mathbf{r}) dV$$

Fixed-axis equation of motion: $\\tau_z = I \\alpha_z$.

<h4>Systematic Derivations for Standard Geometries</h4>
<ul>
  <li><strong>Thin Uniform Rod of Mass $M$, Length $L$ (About Center):</strong>
  $$I_{\\text{cm}} = \\int_{-L/2}^{L/2} x^2 \\left(\\frac{M}{L}\\right) dx = \\frac{M}{L} \\left[ \\frac{x^3}{3} \\right]_{-L/2}^{L/2} = \\frac{1}{12} M L^2$$
  </li>
  <li><strong>Thin Uniform Rod (About One End):</strong>
  $$I_{\\text{end}} = \\int_0^L x^2 \\left(\\frac{M}{L}\\right) dx = \\frac{1}{3} M L^2$$
  </li>
  <li><strong>Uniform Solid Cylinder / Disc of Mass $M$, Radius $R$ (About Cylindrical Axis):</strong>
  $$I = \\int_0^R r^2 \\left(\\frac{2M}{R^2} r dr\\right) = \\frac{2M}{R^2} \\left[ \\frac{r^4}{4} \\right]_0^R = \\frac{1}{2} M R^2$$
  </li>
  <li><strong>Uniform Solid Sphere of Mass $M$, Radius $R$ (About Any Diameter):</strong>
  $$I = \\frac{2}{5} M R^2$$
  </li>
  <li><strong>Thin Spherical Shell of Mass $M$, Radius $R$:</strong>
  $$I = \\frac{2}{3} M R^2$$
  </li>
</ul>`
        },
        {
          "id": "sec-6-4",
          "number": "§6.4",
          "heading": "Theorems on Moments of Inertia: Parallel and Perpendicular Axes",
          "simulation": "parallel-axis-sim",
          "content": `Two fundamental theorems permit calculating moments of inertia about arbitrary axes without re-evaluating triple volume integrals.

<h4>1. Parallel Axis Theorem (Steiner’s Theorem)</h4>
The moment of inertia $I$ about any axis parallel to an axis passing through the center of mass at perpendicular distance $d$ is:
$$I = I_{\\text{cm}} + M d^2$$

<strong>Proof:</strong>
Let the CM be the origin $\\mathbf{R}_{\\text{cm}} = \\mathbf{0}$. The distance of mass element $dm$ to the parallel axis is $\\mathbf{r}' = \\mathbf{r} - \\mathbf{d}$:
$$I = \\int (r')^2 dm = \\int (\\mathbf{r} - \\mathbf{d}) \\cdot (\\mathbf{r} - \\mathbf{d}) dm = \\int r^2 dm - 2\\mathbf{d} \\cdot \\int \\mathbf{r} dm + d^2 \\int dm$$
Since $\\int \\mathbf{r} dm = M \\mathbf{R}_{\\text{cm}} = \\mathbf{0}$:
$$I = I_{\\text{cm}} + M d^2 \\quad \\blacksquare$$

<h4>2. Perpendicular Axis Theorem (Planar Laminae)</h4>
For a thin flat planar sheet lying entirely in the $xy$-plane ($z = 0$):
$$I_z = I_x + I_y$$
<strong>Proof:</strong>
$$I_x = \\int y^2 dm, \\quad I_y = \\int x^2 dm$$
$$I_z = \\int (x^2 + y^2) dm = \\int x^2 dm + \\int y^2 dm = I_x + I_y \\quad \\blacksquare$$`
        },
        {
          "id": "sec-6-5",
          "number": "§6.5",
          "heading": "Rigid Body Planar Dynamics and Pure Rolling Motion Without Slipping",
          "simulation": "rolling-without-slipping-sim",
          "content": `Planar rigid body motion combines translational motion of the center of mass with rotation about the center of mass.

<h4>1. Decomposition of Kinetic Energy (Chasles’ Theorem)</h4>
The total kinetic energy of a rolling body is:
$$K_{\\text{total}} = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} I_{\\text{cm}} \\omega^2$$

<h4>2. Pure Rolling Without Slipping</h4>
For a circular body of radius $R$ rolling without slipping along a surface:
$$v_{\\text{cm}} = R \\omega, \\quad a_{\\text{cm}} = R \\alpha$$
The contact point is instantaneously at rest ($v_{\\text{contact}} = 0$). Static friction does zero mechanical work!

<h4>3. The Great Incline Race</h4>
For a body with $I_{\\text{cm}} = c M R^2$ rolling down an incline of angle $\\theta$:
Applying energy conservation:
$$Mgh = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} (cMR^2) \\left(\\frac{v_{\\text{cm}}}{R}\\right)^2 = \\frac{1}{2} M(1 + c) v_{\\text{cm}}^2$$
Differentiating with respect to distance down slope gives linear acceleration:
$$a_{\\text{cm}} = \\frac{g \\sin \\theta}{1 + c} = \\frac{g \\sin \\theta}{1 + \\frac{I_{\\text{cm}}}{MR^2}}$$

<strong>Ranking:</strong>
<ol>
  <li>Solid Sphere ($c = 2/5 = 0.40$): $a = 0.714 g \\sin\\theta$ (Fastest!)</li>
  <li>Solid Cylinder / Disc ($c = 1/2 = 0.50$): $a = 0.667 g \\sin\\theta$</li>
  <li>Spherical Shell ($c = 2/3 = 0.67$): $a = 0.600 g \\sin\\theta$</li>
  <li>Hollow Hoop ($c = 1.00$): $a = 0.500 g \\sin\\theta$ (Slowest!)</li>
</ol>

<h4>4. Condition for Rolling Without Slipping</h4>
Static friction force required is:
$$f_s = \\frac{Mg \\sin \\theta}{1 + \\frac{MR^2}{I_{\\text{cm}}}} \\le \\mu_s Mg \\cos \\theta \\implies \\mu_s \\ge \\frac{\\tan \\theta}{1 + \\frac{MR^2}{I_{\\text{cm}}}}$$`
        }
      ],
      "problems": [
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Rolling Race Down an Inclined Plane",
          "question": "A solid sphere ($I = \\frac{2}{5}MR^2$), a uniform solid cylinder ($I = \\frac{1}{2}MR^2$), and a thin spherical shell ($I = \\frac{2}{3}MR^2$) are released from rest simultaneously at the top of an incline of angle $\\theta = 30^\\circ$ and length $L = 5.0\\text{ m}$. (a) Calculate the linear acceleration $a$ for each body. (b) Determine the time taken $t$ for each to reach the bottom.",
          "steps": [
            {
              "title": "Step 1: Compute acceleration using a = g sin(θ) / (1 + c)",
              "math": "$$g \\sin(30^\\circ) = 9.80 \\times 0.50 = 4.90 \\text{ m/s}^2$$\n$$a_{\\text{solid sphere}} = \\frac{4.90}{1 + 0.40} = \\frac{4.90}{1.40} = 3.50 \\text{ m/s}^2$$\n$$a_{\\text{cylinder}} = \\frac{4.90}{1 + 0.50} = \\frac{4.90}{1.50} \\approx 3.267 \\text{ m/s}^2$$\n$$a_{\\text{spherical shell}} = \\frac{4.90}{1 + 0.667} = \\frac{4.90}{1.667} = 2.94 \\text{ m/s}^2$$",
              "explanation": "The solid sphere has the highest acceleration because it stores the lowest fraction of energy in rotational motion."
            },
            {
              "title": "Step 2: Calculate time to travel distance L = 5.0 m via t = sqrt(2L / a)",
              "math": "$$t_{\\text{solid sphere}} = \\sqrt{\\frac{2(5.0)}{3.50}} = \\sqrt{2.857} \\approx 1.690 \\text{ s}$$\n$$t_{\\text{cylinder}} = \\sqrt{\\frac{2(5.0)}{3.267}} = \\sqrt{3.061} \\approx 1.750 \\text{ s}$$\n$$t_{\\text{spherical shell}} = \\sqrt{\\frac{2(5.0)}{2.94}} = \\sqrt{3.401} \\approx 1.844 \\text{ s}$$",
              "explanation": "Arrival order: 1st Solid Sphere, 2nd Cylinder, 3rd Spherical Shell."
            }
          ]
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Hard",
          "title": "Sweet Spot for Pure Rolling: The Billiard Ball Cue Strike",
          "question": "A billiard ball of mass $M$ and radius $R$ rests on a horizontal table with coefficient of friction $\\mu$. A cue strikes the ball horizontally with an impulse $J$ at height $h$ above the center of the ball. Determine the exact height $h$ such that the ball rolls immediately without slipping from $t = 0$.",
          "steps": [
            {
              "title": "Step 1: Relate impulse to initial linear and angular velocity",
              "math": "$$J = M v_0 \\implies v_0 = \\frac{J}{M}$$\n$$\\tau_{\\text{impulse}} = J h = I_{\\text{cm}} \\omega_0 = \\left(\\frac{2}{5} M R^2\\right) \\omega_0 \\implies \\omega_0 = \\frac{5 J h}{2 M R^2}$$",
              "explanation": "The horizontal impulse imparts forward linear momentum, and the off-center impact exerts impulsive torque."
            },
            {
              "title": "Step 2: Apply pure rolling condition v_0 = R ω_0",
              "math": "$$v_0 = R \\omega_0 \\implies \\frac{J}{M} = R \\left( \\frac{5 J h}{2 M R^2} \\right) = \\frac{5 J h}{2 M R}$$\n$$1 = \\frac{5 h}{2 R} \\implies h = \\frac{2}{5} R = 0.40 R$$",
              "explanation": "Striking the ball at height $h = 0.4 R$ above its center initiates immediate rolling without any slipping or friction skid."
            }
          ]
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Medium",
          "title": "Physical Pendulum Minimum Period",
          "question": "A uniform thin rod of length $L = 1.0\\text{ m}$ oscillates in a vertical plane about a horizontal pivot at distance $d$ from its center of mass. (a) Derive the period of oscillation $T(d)$ for small amplitudes. (b) Find the distance $d$ that minimizes the period of oscillation.",
          "steps": [
            {
              "title": "Step 1: Compute moment of inertia and angular frequency",
              "math": "$$I = I_{\\text{cm}} + M d^2 = \\frac{1}{12}M L^2 + M d^2$$\n$$\\tau = -M g d \\sin \\theta \\approx -M g d \\theta = I \\ddot{\\theta}$$\n$$\\omega^2 = \\frac{M g d}{\\frac{1}{12}M L^2 + M d^2} = \\frac{g d}{\\frac{L^2}{12} + d^2} \\implies T = 2\\pi \\sqrt{\\frac{\\frac{L^2}{12} + d^2}{g d}}$$",
              "explanation": "The effective length of the equivalent simple pendulum is $L_{\\text{eq}} = \\frac{L^2}{12d} + d$."
            },
            {
              "title": "Step 2: Minimize period with respect to d",
              "math": "$$\\frac{d}{dd}\\left( \\frac{L^2}{12d} + d \\right) = -\\frac{L^2}{12 d^2} + 1 = 0 \\implies d^2 = \\frac{L^2}{12} \\implies d = \\frac{L}{\\sqrt{12}} = \\frac{L}{2\\sqrt{3}} \\approx 0.2887 L$$\n$$\\text{For } L = 1.0\\text{ m}: \\quad d \\approx 0.289\\text{ m}$$",
              "explanation": "Pivoting at $d = 0.289L$ achieves the minimum period of oscillation."
            }
          ]
        }
      ]
    }
  ]
};
