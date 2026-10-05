import json

mechanics_units = []

# =========================================================================
# UNIT 1: Vector Algebra & Differential Calculus
# =========================================================================
u1_sections = [
    {
        "id": "sec-1-1",
        "number": "§1.1",
        "heading": "Vectors, Scalars, and Coordinate Representations",
        "simulation": "vector-addition-sim",
        "content": """Classical Newtonian mechanics describes physical phenomena occurring in three-dimensional Euclidean space $\\mathbb{R}^3$. Physical quantities are classified based on their transformation properties under spatial rotations and coordinate transformations.

<h4>1. Scalar and Vector Quantities</h4>
A **scalar** is a physical quantity that is invariant under spatial rotations and coordinate transformations, completely characterized by a real magnitude (and units): e.g., mass $m$, time $t$, temperature $T$, and kinetic energy $K$.

A **vector** $\\mathbf{A}$ is an entity possessing both magnitude and direction that transforms under a coordinate rotation according to:

$$A_i' = \\sum_{j=1}^3 R_{ij} A_j$$

where $R_{ij}$ is an orthogonal transformation matrix satisfying $R R^T = I$. Examples include displacement $\\mathbf{r}$, velocity $\\mathbf{v}$, linear momentum $\\mathbf{p}$, and force $\\mathbf{F}$.

<h4>2. Algebraic Operations in Cartesian Basis</h4>
In a right-handed Cartesian coordinate system with orthonormal basis vectors $\\{\\hat{\\mathbf{i}}, \\hat{\\mathbf{j}}, \\hat{\\mathbf{k}}\\}$:

$$\\mathbf{A} = A_x \\hat{\\mathbf{i}} + A_y \\hat{\\mathbf{j}} + A_z \\hat{\\mathbf{k}}, \\quad \\mathbf{B} = B_x \\hat{\\mathbf{i}} + B_y \\hat{\\mathbf{j}} + B_z \\hat{\\mathbf{k}}$$

Vector addition and scalar multiplication satisfy linear vector space axioms:

$$\\mathbf{A} + \\mathbf{B} = (A_x + B_x)\\hat{\\mathbf{i}} + (A_y + B_y)\\hat{\\mathbf{j}} + (A_z + B_z)\\hat{\\mathbf{k}}$$

$$\\lambda \\mathbf{A} = (\\lambda A_x)\\hat{\\mathbf{i}} + (\\lambda A_y)\\hat{\\mathbf{j}} + (\\lambda A_z)\\hat{\\mathbf{k}}, \\quad \\lambda \\in \\mathbb{R}$$

The magnitude (Euclidean norm) is:

$$|\\mathbf{A}| = A = \\sqrt{A_x^2 + A_y^2 + A_z^2}$$

<h4>3. The Scalar (Dot) Product</h4>
The scalar product of two vectors is defined geometrically and algebraically as:

$$\\mathbf{A} \\cdot \\mathbf{B} = |\\mathbf{A}||\\mathbf{B}| \\cos \\theta = A_x B_x + A_y B_y + A_z B_z$$

where $\\theta \\in [0, \\pi]$ is the angle between them.
<ul>
  <li><strong>Orthogonality Condition:</strong> $\\mathbf{A} \\perp \\mathbf{B} \\iff \\mathbf{A} \\cdot \\mathbf{B} = 0$.</li>
  <li><strong>Projection:</strong> The scalar component of $\\mathbf{A}$ along $\\mathbf{B}$ is $A_B = \\mathbf{A} \\cdot \\hat{\\mathbf{B}} = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{|\\mathbf{B}|}$.</li>
  <li><strong>Physical Application:</strong> Mechanical work done by force $\\mathbf{F}$ along displacement $d\\mathbf{r}$: $dW = \\mathbf{F} \\cdot d\\mathbf{r}$.</li>
</ul>

<h4>4. The Vector (Cross) Product</h4>
The vector product produces an axial vector perpendicular to both operands:

$$\\mathbf{A} \\times \\mathbf{B} = |\\mathbf{A}||\\mathbf{B}| \\sin \\theta \\,\\hat{\\mathbf{n}}$$

where $\\hat{\\mathbf{n}}$ is determined by the right-hand rule. In determinant form:

$$\\mathbf{A} \\times \\mathbf{B} = \\begin{vmatrix} \\hat{\\mathbf{i}} & \\hat{\\mathbf{j}} & \\hat{\\mathbf{k}} \\\\ A_x & A_y & A_z \\\\ B_x & B_y & B_z \\end{vmatrix} = (A_y B_z - A_z B_y)\\hat{\\mathbf{i}} + (A_z B_x - A_x B_z)\\hat{\\mathbf{j}} + (A_x B_y - A_y B_x)\\hat{\\mathbf{k}}$$

<ul>
  <li><strong>Anticommutativity:</strong> $\\mathbf{B} \\times \\mathbf{A} = -(\\mathbf{A} \\times \\mathbf{B})$.</li>
  <li><strong>Collinearity:</strong> $\\mathbf{A} \\parallel \\mathbf{B} \\iff \\mathbf{A} \\times \\mathbf{B} = 0$.</li>
  <li><strong>Physical Application:</strong> Torque $\\boldsymbol{\\tau} = \\mathbf{r} \\times \\mathbf{F}$ and angular momentum $\\mathbf{L} = \\mathbf{r} \\times \\mathbf{p}$.</li>
</ul>"""
    },
    {
        "id": "sec-1-2",
        "number": "§1.2",
        "heading": "Differential Vector Calculus: Gradient, Divergence, and Curl",
        "simulation": "vector-fields-calc-sim",
        "content": """Spatial fields represent physical quantities that vary continuously over space. Vector calculus describes the spatial rates of change of scalar fields $\\Phi(\\mathbf{r})$ and vector fields $\\mathbf{V}(\\mathbf{r})$.

<h4>1. The Del (Nabla) Operator</h4>
The vector differential operator $\\boldsymbol{\\nabla}$ in Cartesian coordinates is:

$$\\boldsymbol{\\nabla} = \\hat{\\mathbf{i}} \\frac{\\partial}{\\partial x} + \\hat{\\mathbf{j}} \\frac{\\partial}{\\partial y} + \\hat{\\mathbf{k}} \\frac{\\partial}{\\partial z}$$

<h4>2. Gradient of a Scalar Field ($\\boldsymbol{\\nabla}\\Phi$)</h4>
The gradient of a differentiable scalar function $\\Phi(x, y, z)$ is a vector pointing in the direction of maximum spatial increase of $\\Phi$, whose magnitude equals the directional derivative:

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

<strong>Crucial Theorem for Mechanics:</strong>
A force field $\\mathbf{F}(\\mathbf{r})$ is conservative if and only if its curl vanishes everywhere in a simply-connected domain:

$$\\boldsymbol{\\nabla} \\times \\mathbf{F} = 0 \\iff \\mathbf{F} = -\\boldsymbol{\\nabla}U$$"""
    }
]

u1_problems = [
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
    }
]

mechanics_units.append({
    "number": 1,
    "title": "Vector Algebra & Differential Calculus",
    "description": "Scalar and vector quantities, dot and cross products, directional derivatives, gradient, divergence, and curl in Newtonian mechanics.",
    "sections": u1_sections,
    "problems": u1_problems
})

# =========================================================================
# UNIT 2: Vector Integral Theorems & Curvilinear Coordinates
# =========================================================================
u2_sections = [
    {
        "id": "sec-2-1",
        "number": "§2.1",
        "heading": "Line, Surface, and Volume Integrals with Fundamental Integral Theorems",
        "simulation": "stokes-divergence-sim",
        "content": """Vector integrals form the core mathematical toolkit for calculating work along physical trajectories, mass distributions across rigid volumes, and gravitational flux.

<h4>1. Line Integrals and Path Independence</h4>
The line integral of a vector field $\\mathbf{F}$ along a directed curve $C$ parameterized by $\\mathbf{r}(t)$ ($t \\in [a, b]$) is:

$$W = \\int_C \\mathbf{F} \\cdot d\\mathbf{r} = \\int_a^b \\mathbf{F}(\\mathbf{r}(t)) \\cdot \\frac{d\\mathbf{r}}{dt} dt$$

For a conservative force $\\mathbf{F} = -\\boldsymbol{\\nabla}U$, the line integral depends solely on initial and final endpoints:

$$\\int_A^B \\mathbf{F} \\cdot d\\mathbf{r} = -\\int_A^B dU = -(U(B) - U(A)) = U(A) - U(B)$$

Consequently, around any closed loop $\\oint_C \\mathbf{F} \\cdot d\\mathbf{r} = 0$.

<h4>2. Gauss’s Divergence Theorem</h4>
Gauss's divergence theorem relates the surface flux of a continuously differentiable vector field $\\mathbf{V}$ across a closed surface $S = \\partial V$ to the volume integral of its divergence:

$$\\oint_S \\mathbf{V} \\cdot d\\mathbf{A} = \\iiint_V (\\boldsymbol{\\nabla} \\cdot \\mathbf{V}) dV$$

<strong>Application in Gravitation:</strong> For the gravitational field $\\mathbf{g} = -G \\frac{M}{r^2} \\hat{\\mathbf{r}}$:

$$\\oint_S \\mathbf{g} \\cdot d\\mathbf{A} = -4\\pi G M_{\\text{enclosed}} = -4\\pi G \\iiint_V \\rho(\\mathbf{r}) dV$$

In differential form, this yields Gauss's law for gravity: $\\boldsymbol{\\nabla} \\cdot \\mathbf{g} = -4\\pi G \\rho$.

<h4>3. Stokes’ Curl Theorem</h4>
Stokes' theorem transforms the surface integral of the curl over an open surface $S$ into the line integral along its bounding closed perimeter $C = \\partial S$:

$$\\oint_C \\mathbf{F} \\cdot d\\mathbf{r} = \\iint_S (\\boldsymbol{\\nabla} \\times \\mathbf{F}) \\cdot d\\mathbf{A}$$

If $\\boldsymbol{\\nabla} \\times \\mathbf{F} = 0$, the right-hand side is zero for any surface, rigorously proving why zero curl guarantees zero closed-loop work."""
    },
    {
        "id": "sec-2-2",
        "number": "§2.2",
        "heading": "Curvilinear Coordinates: Cylindrical and Spherical Coordinate Systems",
        "simulation": "coordinate-systems-sim",
        "content": """While Cartesian coordinates are mathematically straightforward, systems with axial symmetry (flywheels, rods) or central symmetry (planetary orbits, central forces) are vastly simplified by cylindrical or spherical coordinates.

<h4>1. Cylindrical Coordinates $(r, \\theta, z)$</h4>
Transformation to Cartesian coordinates:

$$x = r \\cos \\theta, \\quad y = r \\sin \\theta, \\quad z = z$$

Orthonormal basis vectors:

$$\\hat{\\mathbf{r}} = \\cos \\theta \\hat{\\mathbf{i}} + \\sin \\theta \\hat{\\mathbf{j}}, \\quad \\hat{\\boldsymbol{\\theta}} = -\\sin \\theta \\hat{\\mathbf{i}} + \\cos \\theta \\hat{\\mathbf{j}}, \\quad \\hat{\\mathbf{z}} = \\hat{\\mathbf{k}}$$

Metric scale factors: $h_r = 1, h_\\theta = r, h_z = 1$. Infinitesimal line element:

$$d\\mathbf{r} = dr \\hat{\\mathbf{r}} + r d\\theta \\hat{\\boldsymbol{\\theta}} + dz \\hat{\\mathbf{z}}$$

Gradient and Laplacian in cylindrical coordinates:

$$\\boldsymbol{\\nabla}\\Phi = \\frac{\\partial \\Phi}{\\partial r} \\hat{\\mathbf{r}} + \\frac{1}{r} \\frac{\\partial \\Phi}{\\partial \\theta} \\hat{\\boldsymbol{\\theta}} + \\frac{\\partial \\Phi}{\\partial z} \\hat{\\mathbf{z}}$$

$$\\nabla^2 \\Phi = \\frac{1}{r} \\frac{\\partial}{\\partial r}\\left(r \\frac{\\partial \\Phi}{\\partial r}\\right) + \\frac{1}{r^2}\\frac{\\partial^2 \\Phi}{\\partial \\theta^2} + \\frac{\\partial^2 \\Phi}{\\partial z^2}$$

<h4>2. Spherical Polar Coordinates $(r, \\theta, \\phi)$</h4>
Transformation:

$$x = r \\sin \\theta \\cos \\phi, \\quad y = r \\sin \\theta \\sin \\phi, \\quad z = r \\cos \\theta$$

Scale factors: $h_r = 1, h_\\theta = r, h_\\phi = r \\sin \\theta$. Volume element:

$$dV = r^2 \\sin \\theta \\, dr \\, d\\theta \\, d\\phi$$

The Laplacian operator in spherical coordinates:

$$\\nabla^2 \\Phi = \\frac{1}{r^2} \\frac{\\partial}{\\partial r}\\left(r^2 \\frac{\\partial \\Phi}{\\partial r}\\right) + \\frac{1}{r^2 \\sin \\theta} \\frac{\\partial}{\\partial \\theta}\\left(\\sin \\theta \\frac{\\partial \\Phi}{\\partial \\theta}\\right) + \\frac{1}{r^2 \\sin^2 \\theta} \\frac{\\partial^2 \\Phi}{\\partial \\phi^2}$$"""
    }
]

u2_problems = [
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
    }
]

mechanics_units.append({
    "number": 2,
    "title": "Vector Integral Theorems & Coordinates",
    "description": "Line and surface integrals, Gauss's divergence theorem, Stokes' theorem, cylindrical and spherical coordinate systems, and Laplacian operators.",
    "sections": u2_sections,
    "problems": u2_problems
})

# =========================================================================
# UNIT 3: Kinematics and Particle Dynamics
# =========================================================================
u3_sections = [
    {
        "id": "sec-3-1",
        "number": "§3.1",
        "heading": "Kinematics in a Plane: Tangential and Normal Acceleration",
        "simulation": "curvilinear-acceleration-sim",
        "content": """Kinematics describes the geometry of motion without regard to the forces causing it.

<h4>1. Position, Velocity, and Acceleration Vectors</h4>
Let $\\mathbf{r}(t)$ denote the trajectory of a particle. Its velocity and acceleration vectors are:

$$\\mathbf{v}(t) = \\frac{d\\mathbf{r}}{dt} = \\dot{\\mathbf{r}}, \\quad \\mathbf{a}(t) = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2\\mathbf{r}}{dt^2} = \\ddot{\\mathbf{r}}$$

<h4>2. Tangential and Normal Components of Acceleration</h4>
For general curvilinear planar motion along arc length $s(t)$, let $\\hat{\\mathbf{t}}$ be the unit tangent vector and $\\hat{\\mathbf{n}}$ the unit principal normal vector pointing toward the local center of curvature.

The velocity vector is strictly tangential:

$$\\mathbf{v} = v \\hat{\\mathbf{t}}, \\quad v = \\frac{ds}{dt}$$

Differentiating with respect to time:

$$\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{dv}{dt} \\hat{\\mathbf{t}} + v \\frac{d\\hat{\\mathbf{t}}}{dt}$$

Using the Frenet-Serret geometric formula $\\frac{d\\hat{\\mathbf{t}}}{ds} = \\frac{1}{\\rho} \\hat{\\mathbf{n}}$, where $\\rho$ is the local radius of curvature:

$$\\frac{d\\hat{\\mathbf{t}}}{dt} = \\frac{d\\hat{\\mathbf{t}}}{ds} \\frac{ds}{dt} = \\left(\\frac{1}{\\rho} \\hat{\\mathbf{n}}\\right) v = \\frac{v}{\\rho} \\hat{\\mathbf{n}}$$

Substituting into the acceleration equation:

$$\\mathbf{a} = a_t \\hat{\\mathbf{t}} + a_n \\hat{\\mathbf{n}} = \\left( \\frac{dv}{dt} \\right) \\hat{\\mathbf{t}} + \\left( \\frac{v^2}{\\rho} \\right) \\hat{\\mathbf{n}}$$

<ul>
  <li><strong>Tangential Acceleration ($a_t = \\dot{v}$):</strong> Governs changes in the *speed* of the particle.</li>
  <li><strong>Normal (Centripetal) Acceleration ($a_n = v^2/\\rho$):</strong> Governs changes in the *direction* of the velocity vector.</li>
  <li><strong>Total Acceleration Magnitude:</strong> $a = \\sqrt{a_t^2 + a_n^2} = \\sqrt{\\left(\\frac{dv}{dt}\\right)^2 + \\left(\\frac{v^2}{\\rho}\\right)^2}$.</li>
</ul>"""
    },
    {
        "id": "sec-3-2",
        "number": "§3.2",
        "heading": "Projectile Motion and Uniform Circular Motion",
        "simulation": "projectile-motion-sim",
        "content": """Planar two-dimensional motion under constant acceleration provides the foundation for classical ballistics and orbital mechanics.

<h4>1. Projectile Motion with Gravitational Acceleration</h4>
For a projectile launched from the origin $(0, 0)$ with initial speed $v_0$ at angle $\\theta_0$ to the horizontal in the absence of air drag:

$$a_x = 0, \\quad a_y = -g$$

Integrating with respect to time:

$$v_x(t) = v_0 \\cos \\theta_0, \\quad v_y(t) = v_0 \\sin \\theta_0 - g t$$

$$x(t) = (v_0 \\cos \\theta_0) t, \\quad y(t) = (v_0 \\sin \\theta_0) t - \\frac{1}{2} g t^2$$

Eliminating $t = \\frac{x}{v_0 \\cos \\theta_0}$ yields the parabolic trajectory equation:

$$y(x) = x \\tan \\theta_0 - \\frac{g}{2 v_0^2 \\cos^2 \\theta_0} x^2$$

Key trajectory parameters:
<ul>
  <li><strong>Time of Flight ($T$):</strong> $y(T) = 0 \\implies T = \\frac{2 v_0 \\sin \\theta_0}{g}$.</li>
  <li><strong>Maximum Altitude ($H$):</strong> $v_y = 0 \\implies H = \\frac{v_0^2 \\sin^2 \\theta_0}{2g}$.</li>
  <li><strong>Horizontal Range ($R$):</strong> $R = x(T) = \\frac{v_0^2 \\sin 2\\theta_0}{g}$, maximized at $\\theta_0 = 45^\\circ$.</li>
</ul>

<h4>2. Uniform Circular Motion</h4>
For motion along a circle of radius $R$ at constant angular velocity $\\omega = \\dot{\\theta}$:

$$\\mathbf{r}(t) = R \\cos(\\omega t) \\hat{\\mathbf{i}} + R \\sin(\\omega t) \\hat{\\mathbf{j}}$$

$$\\mathbf{v}(t) = -R\\omega \\sin(\\omega t) \\hat{\\mathbf{i}} + R\\omega \\cos(\\omega t) \\hat{\\mathbf{j}} \\implies v = R\\omega$$

$$\\mathbf{a}(t) = -R\\omega^2 \\cos(\\omega t) \\hat{\\mathbf{i}} - R\\omega^2 \\sin(\\omega t) \\hat{\\mathbf{j}} = -\\omega^2 \\mathbf{r}(t) = -\\frac{v^2}{R} \\hat{\\mathbf{r}}$$

The acceleration is directed strictly toward the center with constant magnitude $a_c = \\frac{v^2}{R} = \\omega^2 R$."""
    },
    {
        "id": "sec-3-3",
        "number": "§3.3",
        "heading": "Newton’s Laws of Motion, Inertial Reference Frames, and Friction",
        "simulation": "friction-newton-sim",
        "content": """Isaac Newton's *Philosophiae Naturalis Principia Mathematica* (1687) formulated the foundational dynamical laws governing classical particle mechanics.

<h4>1. Newton's Three Laws of Motion</h4>
<ol>
  <li><strong>First Law (Law of Inertia):</strong> A particle remains in its state of rest or uniform motion in a straight line unless acted upon by a non-zero net external force:
  
  $$\\sum \\mathbf{F} = \\mathbf{0} \\implies \\mathbf{v} = \\text{constant}$$
  </li>
  <li><strong>Second Law (Fundamental Dynamical Equation):</strong> The net external force acting on a particle equals the time rate of change of its linear momentum $\\mathbf{p} = m\\mathbf{v}$:
  
  $$\\mathbf{F} = \\frac{d\\mathbf{p}}{dt} = \\frac{d(m\\mathbf{v})}{dt} = m \\frac{d\\mathbf{v}}{dt} + \\mathbf{v} \\frac{dm}{dt}$$
  
  For constant mass $m$:
  
  $$\\mathbf{F} = m \\mathbf{a} = m \\frac{d^2\\mathbf{r}}{dt^2}$$
  </li>
  <li><strong>Third Law (Action and Reaction):</strong> Whenever body $A$ exerts a force $\\mathbf{F}_{AB}$ on body $B$, body $B$ exerts an equal and opposite force $\\mathbf{F}_{BA}$ on body $A$:
  
  $$\\mathbf{F}_{AB} = -\\mathbf{F}_{BA}$$
  </li>
</ol>

<h4>2. Inertial and Non-Inertial Reference Frames</h4>
An **inertial frame** is a frame of reference in which Newton's first law holds. Any frame moving with constant velocity relative to an inertial frame is also inertial (Galilean relativity).

In an accelerating reference frame with translational acceleration $\\mathbf{A}_0$, an observer must introduce a fictitious (inertial) force:

$$\\mathbf{F}_{\\text{fictitious}} = -m \\mathbf{A}_0$$

<h4>3. Coulomb-Amontons Laws of Dry Friction</h4>
Friction arises from electromagnetic intermolecular bonds between microscopic contact asperities:
<ul>
  <li><strong>Static Friction ($f_s$):</strong> Prevents relative motion up to a threshold limit:
  
  $$f_s \\le \\mu_s N$$
  </li>
  <li><strong>Kinetic (Sliding) Friction ($f_k$):</strong> Opposes ongoing relative velocity:
  
  $$f_k = \\mu_k N, \\quad (\\mu_k < \\mu_s)$$
  </li>
</ul>"""
    }
]

u3_problems = [
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
    }
]

mechanics_units.append({
    "number": 3,
    "title": "Kinematics and Particle Dynamics",
    "description": "Tangential and normal acceleration, projectile motion, circular dynamics, Newton's laws of motion, inertial frames, and friction.",
    "sections": u3_sections,
    "problems": u3_problems
})

# =========================================================================
# UNIT 4: Work, Energy, and Power
# =========================================================================
u4_sections = [
    {
        "id": "sec-4-1",
        "number": "§4.1",
        "heading": "Work-Energy Theorem and Conservative Force Fields",
        "simulation": "work-energy-theorem-sim",
        "content": """Energy is the universal scalar measure of a system's capacity to perform work.

<h4>1. Work Done by Variable Forces</h4>
The work done by a vector force $\\mathbf{F}(\\mathbf{r})$ along a spatial path from $\\mathbf{r}_1$ to $\\mathbf{r}_2$ is:

$$W_{1\\to 2} = \\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} \\mathbf{F} \\cdot d\\mathbf{r}$$

For instantaneous power $P$, defined as the time rate of doing work:

$$P = \\frac{dW}{dt} = \\mathbf{F} \\cdot \\frac{d\\mathbf{r}}{dt} = \\mathbf{F} \\cdot \\mathbf{v}$$

<h4>2. Rigorous Proof of the Work-Energy Theorem</h4>
Consider a particle of constant mass $m$ acted upon by a net force $\\mathbf{F}_{\\text{net}} = m \\frac{d\\mathbf{v}}{dt}$:

$$W_{1\\to 2} = \\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} \\mathbf{F}_{\\text{net}} \\cdot d\\mathbf{r} = \\int_{t_1}^{t_2} \\left( m \\frac{d\\mathbf{v}}{dt} \\right) \\cdot \\mathbf{v} dt$$

Using the vector identity $\\frac{d}{dt}(v^2) = \\frac{d}{dt}(\\mathbf{v} \\cdot \\mathbf{v}) = 2 \\mathbf{v} \\cdot \\frac{d\\mathbf{v}}{dt}$:

$$W_{1\\to 2} = m \\int_{t_1}^{t_2} \\frac{1}{2} \\frac{d(v^2)}{dt} dt = \\frac{1}{2}m v_2^2 - \\frac{1}{2}m v_1^2 = K_2 - K_1 = \\Delta K$$

The **Work-Energy Theorem** states that the total work done by all forces (conservative and non-conservative) equals the change in kinetic energy:

$$W_{\\text{total}} = \\Delta K$$

<h4>3. Potential Energy of Conservative Forces</h4>
For a conservative force, the work done is independent of path and can be expressed in terms of a scalar potential energy function $U(\\mathbf{r})$:

$$W_{\\text{cons}} = -\\Delta U = U_1 - U_2 \\implies \\mathbf{F} = -\\boldsymbol{\\nabla}U$$

Total mechanical energy $E = K + U$ is strictly conserved when only conservative forces act:

$$\\Delta E = \\Delta K + \\Delta U = 0 \\implies E = K + U = \\text{constant}$$"""
    },
    {
        "id": "sec-4-2",
        "number": "§4.2",
        "heading": "One-Dimensional Potential Wells and Equilibrium Stability",
        "simulation": "potential-well-sim",
        "content": """For a particle moving in a one-dimensional potential $U(x)$, its motion is completely characterized by the energy conservation relation:

$$E = \\frac{1}{2}m \\dot{x}^2 + U(x) = \\text{constant}$$

Solving for velocity $\\dot{x} = \\frac{dx}{dt}$:

$$\\frac{dx}{dt} = \\pm \\sqrt{\\frac{2}{m}[E - U(x)]}$$

Because kinetic energy $K = \\frac{1}{2}m\\dot{x}^2 \\ge 0$, motion is physically permitted only in regions where:

$$E \\ge U(x)$$

The points where $E = U(x)$ are the **turning points**, where $\\dot{x} = 0$.

<h4>1. Equilibrium Points and Stability Criteria</h4>
Equilibrium occurs where the net force vanishes:

$$F(x) = -\\frac{dU}{dx} = 0$$

The stability of an equilibrium point $x_0$ is determined by the second derivative $\\frac{d^2 U}{dx^2}$:
<ul>
  <li><strong>Stable Equilibrium (Local Minimum):</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} > 0$. Small displacements generate a restoring force ($F \\propto -\\Delta x$). The particle undergoes oscillations with angular frequency:
  
  $$\\omega = \\sqrt{\\frac{k_{\\text{eff}}}{m}}, \\quad k_{\\text{eff}} = \\left.\\frac{d^2 U}{dx^2}\\right|_{x_0}$$
  </li>
  <li><strong>Unstable Equilibrium (Local Maximum):</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} < 0$. Displacements produce forces driving the particle away from $x_0$.</li>
  <li><strong>Neutral Equilibrium:</strong> $\\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} = 0$.</li>
</ul>"""
    }
]

u4_problems = [
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
    }
]

mechanics_units.append({
    "number": 4,
    "title": "Work, Energy, and Power",
    "description": "Work-energy theorem, conservative and non-conservative forces, potential energy functions, one-dimensional potential wells, and equilibrium stability.",
    "sections": u4_sections,
    "problems": u4_problems
})

# =========================================================================
# UNIT 5: Conservation of Linear Momentum & Many-Particle Systems
# =========================================================================
u5_sections = [
    {
        "id": "sec-5-1",
        "number": "§5.1",
        "heading": "Center of Mass and Linear Momentum of Multi-Particle Systems",
        "simulation": "center-of-mass-sim",
        "content": """For an extended body or a collection of $N$ interacting particles of masses $m_i$ at positions $\\mathbf{r}_i$:

<h4>1. Center of Mass Vector</h4>
The center of mass $\\mathbf{R}_{\\text{cm}}$ is the mass-weighted average position:

$$\\mathbf{R}_{\\text{cm}} = \\frac{\\sum_{i=1}^N m_i \\mathbf{r}_i}{\\sum_{i=1}^N m_i} = \\frac{1}{M} \\sum_{i=1}^N m_i \\mathbf{r}_i, \\quad M = \\sum_{i=1}^N m_i$$

For a continuous rigid body with mass density $\\rho(\\mathbf{r})$:

$$\\mathbf{R}_{\\text{cm}} = \\frac{1}{M} \\iiint_V \\mathbf{r} \\rho(\\mathbf{r}) dV, \\quad M = \\iiint_V \\rho(\\mathbf{r}) dV$$

<h4>2. Total Linear Momentum and Center-of-Mass Velocity</h4>
Differentiating with respect to time:

$$\\mathbf{v}_{\\text{cm}} = \\dot{\\mathbf{R}}_{\\text{cm}} = \\frac{1}{M} \\sum_{i=1}^N m_i \\mathbf{v}_i$$

The total linear momentum $\\mathbf{P}$ of the entire system is:

$$\\mathbf{P} = \\sum_{i=1}^N \\mathbf{p}_i = \\sum_{i=1}^N m_i \\mathbf{v}_i = M \\mathbf{v}_{\\text{cm}}$$

<h4>3. The Fundamental Center-of-Mass Equation of Motion</h4>
Differentiating total momentum with respect to time:

$$\\frac{d\\mathbf{P}}{dt} = M \\mathbf{a}_{\\text{cm}} = \\sum_{i=1}^N \\mathbf{F}_i$$

Separating the force acting on particle $i$ into external forces $\\mathbf{F}_i^{\\text{ext}}$ and internal mutual forces $\\sum_{j \\neq i} \\mathbf{F}_{ij}$:

$$\\frac{d\\mathbf{P}}{dt} = \\sum_{i=1}^N \\mathbf{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\mathbf{F}_{ij}$$

By Newton's third law, internal pairwise forces cancel identically: $\\mathbf{F}_{ij} + \\mathbf{F}_{ji} = \\mathbf{0}$. Therefore:

$$\\frac{d\\mathbf{P}}{dt} = M \\mathbf{a}_{\\text{cm}} = \\mathbf{F}_{\\text{net}}^{\\text{ext}}$$

**Law of Conservation of Linear Momentum:**
If the net external force acting on a system vanishes ($\\mathbf{F}_{\\text{net}}^{\\text{ext}} = \\mathbf{0}$):

$$\\mathbf{P} = M \\mathbf{v}_{\\text{cm}} = \\text{constant}$$"""
    },
    {
        "id": "sec-5-2",
        "number": "§5.2",
        "heading": "Variable-Mass Systems and the Tsiolkovsky Rocket Equation",
        "simulation": "rocket-propulsion-sim",
        "content": """Newton's second law $\\mathbf{F} = \\frac{d\\mathbf{p}}{dt}$ must be applied carefully to open systems whose mass changes continuously through mass ejection or accretion.

<h4>1. Derivation of the Rocket Equation of Motion</h4>
Consider a rocket of instantaneous mass $m(t)$ moving with velocity $\\mathbf{v}(t)$ in one dimension. During time interval $dt$, the rocket ejects propellant mass $(-dm > 0)$ with exhaust velocity $\\mathbf{u}_{\\text{ex}}$ relative to the rocket.

Linear momentum at time $t$:

$$p(t) = m v$$

Linear momentum at time $t + dt$:
<ul>
  <li>Rocket mass: $m + dm$ (where $dm < 0$), velocity: $v + dv$.</li>
  <li>Ejected propellant mass: $-dm$, velocity in ground frame: $v - u_{\\text{ex}}$.</li>
</ul>

$$p(t + dt) = (m + dm)(v + dv) + (-dm)(v - u_{\\text{ex}}) = m v + m dv + v dm - v dm + u_{\\text{ex}} dm$$

$$p(t + dt) = m v + m dv + u_{\\text{ex}} dm$$

Change in momentum over $dt$:

$$dp = p(t + dt) - p(t) = m dv + u_{\\text{ex}} dm$$

Applying Newton's second law with external force $F_{\\text{ext}}$ (e.g., gravity):

$$F_{\\text{ext}} = \\frac{dp}{dt} = m \\frac{dv}{dt} + u_{\\text{ex}} \\frac{dm}{dt}$$

Rearranging gives the rocket dynamical equation:

$$m \\frac{dv}{dt} = -u_{\\text{ex}} \\frac{dm}{dt} + F_{\\text{ext}}$$

The term $T_{\\text{thrust}} = -u_{\\text{ex}} \\frac{dm}{dt} = u_{\\text{ex}} |\\dot{m}|$ is the **rocket thrust**.

<h4>2. Tsiolkovsky Rocket Formula</h4>
In deep space free of external gravity and drag ($F_{\\text{ext}} = 0$):

$$m dv = -u_{\\text{ex}} dm \\implies dv = -u_{\\text{ex}} \\frac{dm}{m}$$

Integrating from initial state $(m_0, v_0)$ to final state $(m_f, v_f)$:

$$\\Delta v = v_f - v_0 = -u_{\\text{ex}} \\int_{m_0}^{m_f} \\frac{dm}{m} = u_{\\text{ex}} \\ln\\left(\\frac{m_0}{m_f}\\right)$$

This is the celebrated **Tsiolkovsky Rocket Equation**. The velocity increment depends logarithmically on the mass ratio $\\frac{m_0}{m_f}$ and linearly on exhaust velocity $u_{\\text{ex}}$."""
    },
    {
        "id": "sec-5-3",
        "number": "§5.3",
        "heading": "Collision Phenomena in Laboratory and Center-of-Mass Frames",
        "simulation": "collision-lab-cm-sim",
        "content": """Collisions are brief interactions where impulsive mutual forces dominate over external forces.

<h4>1. Classification by Kinetic Energy Conservation</h4>
<ul>
  <li><strong>Elastic Collisions:</strong> Total mechanical kinetic energy is conserved: $K_f = K_i$.</li>
  <li><strong>Inelastic Collisions:</strong> Kinetic energy is partially transformed into heat, deformation, or internal excitation: $K_f < K_i$.</li>
  <li><strong>Perfectly Inelastic Collisions:</strong> Bodies coalesce and stick together, moving with identical final velocity $\\mathbf{v}_f = \\mathbf{v}_{\\text{cm}}$.</li>
</ul>

<h4>2. The Coefficient of Restitution ($e$)</h4>
For a one-dimensional collision along the line of centers:

$$e = -\\frac{v_{2f} - v_{1f}}{v_{2i} - v_{1i}} = \\frac{\\text{Relative separation velocity}}{\\text{Relative approach velocity}}$$

<ul>
  <li>$e = 1$: Perfectly elastic collision.</li>
  <li>$0 < e < 1$: Inelastic collision.</li>
  <li>$e = 0$: Completely inelastic collision.</li>
</ul>

<h4>3. The Center-of-Mass (CM) Frame Transformation</h4>
In the CM frame, the total linear momentum is identically zero by definition:

$$\\mathbf{P}_{\\text{cm}} = \\mathbf{0} \\implies m_1 \\mathbf{u}_1 + m_2 \\mathbf{u}_2 = \\mathbf{0}$$

For an elastic collision in the CM frame, the magnitudes of the velocities remain completely unchanged; the collision merely rotates the relative velocity vector by a scattering angle $\\theta^*$:

$$|\\mathbf{u}_1'| = |\\mathbf{u}_1|, \\quad |\\mathbf{u}_2'| = |\\mathbf{u}_2|$$"""
    }
]

u5_problems = [
    {
        "difficulty": "Medium",
        "difficultyLabel": "Medium",
        "title": "Two-Stage Rocket Velocity Optimization",
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
    }
]

mechanics_units.append({
    "number": 5,
    "title": "Conservation of Linear Momentum",
    "description": "Center of mass, multi-particle systems, Tsiolkovsky rocket equation, variable-mass dynamics, and elastic/inelastic collisions in Lab and CM frames.",
    "sections": u5_sections,
    "problems": u5_problems
})

# =========================================================================
# UNIT 6: Rotational Kinematics & Dynamics of Rigid Bodies
# =========================================================================
u6_sections = [
    {
        "id": "sec-6-1",
        "number": "§6.1",
        "heading": "Rotational Kinematics and the Angular Velocity Vector",
        "simulation": "rotational-kinematics-sim",
        "content": """A rigid body is an idealized system of particles in which all pairwise distances $|\\mathbf{r}_i - \\mathbf{r}_j|$ remain strictly constant in time.

<h4>1. The Angular Velocity Vector $\\boldsymbol{\\omega}$</h4>
For a rigid body rotating about an instantaneous axis, its angular velocity vector $\\boldsymbol{\\omega}$ points along the axis of rotation by the right-hand rule.

The linear velocity $\\mathbf{v}$ of any point located at position $\\mathbf{r}$ relative to an origin on the rotation axis is:

$$\\mathbf{v} = \\boldsymbol{\\omega} \\times \\mathbf{r}$$

Differentiating with respect to time gives the linear acceleration:

$$\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d\\boldsymbol{\\omega}}{dt} \\times \\mathbf{r} + \\boldsymbol{\\omega} \\times \\frac{d\\mathbf{r}}{dt} = \\boldsymbol{\\alpha} \\times \\mathbf{r} + \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r})$$

<ul>
  <li>$\\mathbf{a}_t = \\boldsymbol{\\alpha} \\times \\mathbf{r}$: Tangential acceleration (due to angular acceleration $\\boldsymbol{\\alpha} = \\dot{\\boldsymbol{\\omega}}$).</li>
  <li>$\\mathbf{a}_c = \\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r}) = -\\omega^2 \\mathbf{r}_\\perp$: Centripetal acceleration pointing perpendicular to the rotation axis.</li>
</ul>

<h4>2. Kinematic Equations for Constant Angular Acceleration $\\alpha$</h4>
$$\\omega(t) = \\omega_0 + \\alpha t$$

$$\\theta(t) = \\omega_0 t + \\frac{1}{2} \\alpha t^2$$

$$\\omega^2 = \\omega_0^2 + 2 \\alpha \\Delta\\theta$$"""
    },
    {
        "id": "sec-6-2",
        "number": "§6.2",
        "heading": "Torque, Angular Momentum, and the Moment of Inertia Tensor",
        "simulation": "moment-of-inertia-sim",
        "content": """Rotational dynamics is the rotational analogue of translational Newtonian mechanics.

<h4>1. Torque and Angular Momentum</h4>
For a particle acted upon by force $\\mathbf{F}$ at position $\\mathbf{r}$:

$$\\boldsymbol{\\tau} = \\mathbf{r} \\times \\mathbf{F} \\quad (\\text{Torque})$$

$$\\mathbf{L} = \\mathbf{r} \\times \\mathbf{p} = \\mathbf{r} \\times (m\\mathbf{v}) \\quad (\\text{Angular Momentum})$$

Differentiating $\\mathbf{L}$ with respect to time:

$$\\frac{d\\mathbf{L}}{dt} = \\frac{d\\mathbf{r}}{dt} \\times \\mathbf{p} + \\mathbf{r} \\times \\frac{d\\mathbf{p}}{dt} = (\\mathbf{v} \\times m\\mathbf{v}) + \\mathbf{r} \\times \\mathbf{F}$$

Since $\\mathbf{v} \\times \\mathbf{v} = \\mathbf{0}$:

$$\\boldsymbol{\\tau}_{\\text{net}} = \\frac{d\\mathbf{L}}{dt}$$

**Conservation of Angular Momentum:** If the net external torque is zero ($\\boldsymbol{\\tau}_{\\text{net}} = \\mathbf{0}$), total angular momentum is strictly conserved: $\\mathbf{L} = \\text{constant}$.

<h4>2. Moment of Inertia for Fixed-Axis Rotation</h4>
For rotation about a fixed axis (say, the $z$-axis), the kinetic energy is:

$$K_{\\text{rot}} = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2 = \\frac{1}{2} \\sum_{i=1}^N m_i (r_{\\perp, i} \\omega)^2 = \\frac{1}{2} \\left( \\sum_{i=1}^N m_i r_{\\perp, i}^2 \\right) \\omega^2 = \\frac{1}{2} I \\omega^2$$

where the **Moment of Inertia** $I$ is:

$$I = \\sum_{i=1}^N m_i r_{\\perp, i}^2 = \\iiint_V r_\\perp^2 \\rho(\\mathbf{r}) dV$$

The fixed-axis equation of motion becomes:

$$\\tau_z = I \\alpha_z = I \\frac{d^2\\theta}{dt^2}$$

<h4>3. Fundamental Moment of Inertia Theorems</h4>
<ul>
  <li><strong>Parallel Axis Theorem (Steiner’s Theorem):</strong>
  The moment of inertia $I$ about any axis parallel to an axis passing through the center of mass at distance $d$ is:
  
  $$I = I_{\\text{cm}} + M d^2$$
  </li>
  <li><strong>Perpendicular Axis Theorem (Planar Laminas):</strong>
  For a thin flat lamina lying in the $xy$-plane:
  
  $$I_z = I_x + I_y$$
  </li>
</ul>"""
    },
    {
        "id": "sec-6-3",
        "number": "§6.3",
        "heading": "Rigid Body Planar Dynamics and Rolling Motion Without Slipping",
        "simulation": "rolling-without-slipping-sim",
        "content": """Planar rigid body motion combines translational motion of the center of mass with rotation about the center of mass.

<h4>1. Decomposition of Kinetic Energy (Chasles’ Theorem)</h4>
The total kinetic energy of a rigid body of mass $M$ is the sum of center-of-mass translation and rotation about the center of mass:

$$K_{\\text{total}} = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} I_{\\text{cm}} \\omega^2$$

<h4>2. Pure Rolling Without Slipping</h4>
For a round body (cylinder, sphere, hoop) of radius $R$ rolling without slipping along a surface:

$$v_{\\text{cm}} = R \\omega, \\quad a_{\\text{cm}} = R \\alpha$$

The point of instantaneous contact with the surface is at rest ($v_{\\text{contact}} = 0$).

<h4>3. Acceleration of a Rolling Body Down an Inclined Plane</h4>
For a body of mass $M$, radius $R$, and moment of inertia $I_{\\text{cm}} = c M R^2$ ($c = 1/2$ for solid cylinder, $c = 2/5$ for solid sphere) rolling down an incline of angle $\\theta$:

Applying energy conservation from height $h$:

$$M g h = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} (c M R^2) \\left(\\frac{v_{\\text{cm}}}{R}\\right)^2 = \\frac{1}{2} M (1 + c) v_{\\text{cm}}^2$$

Solving for linear acceleration down the incline:

$$a_{\\text{cm}} = \\frac{g \\sin \\theta}{1 + c} = \\frac{g \\sin \\theta}{1 + \\frac{I_{\\text{cm}}}{M R^2}}$$

Bodies with lower mass distribution factors $c$ (e.g., solid sphere $c=0.4$ vs cylinder $c=0.5$ vs hoop $c=1.0$) accelerate faster and win the race down the ramp!"""
    }
]

u6_problems = [
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
    }
]

mechanics_units.append({
    "number": 6,
    "title": "Rotational Kinematics & Dynamics",
    "description": "Angular velocity vector, torque, angular momentum conservation, moment of inertia tensor, parallel/perpendicular axis theorems, and pure rolling motion.",
    "sections": u6_sections,
    "problems": u6_problems
})

# Write course data JS
course_data = {
    "courseTitle": "Fundamentals of Mechanics",
    "courseCode": "PHY-101",
    "department": "Department of Physics",
    "institution": "OpenSTEM Global Academic Press",
    "authorContact": "shahriyarkarimsiam@gmail.com",
    "units": mechanics_units
}

with open("mechanics-data.js", "w", encoding="utf-8") as f:
    f.write("// Fundamentals of Mechanics (PHY-101)\n")
    f.write("// Complete university textbook curriculum dataset with 6 Units, LaTeX math, and solved exam problems.\n\n")
    f.write("window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n")

print("Generated mechanics-data.js successfully with all 6 units!")
