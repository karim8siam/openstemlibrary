# Build Script for Units 1 and 2: Electric Field and Electric Potential
import json

# =========================================================================
# UNIT 1: Electric Field
# =========================================================================
u1_sections = [
    {
        "id": "sec-1-1",
        "number": "§1.1",
        "heading": "Electric Charge, Quantization, and Conservation Laws",
        "simulation": "coulomb-field-sim",
        "content": """Electrostatics investigates electric charges at rest and the static electric fields they establish in vacuum and material media.

<h4>1. The Fundamental Nature of Electric Charge</h4>
Electric charge is an intrinsic fundamental property of subatomic matter. Matter exhibits two complementary types of charge:
<ul>
  <li><strong>Positive Charge ($+q$):</strong> Borne by protons ($+e$).</li>
  <li><strong>Negative Charge ($-q$):</strong> Borne by electrons ($-e$).</li>
</ul>
Like charges repel one another with mutual electrostatic forces; unlike charges attract.

<h4>2. Quantization of Electric Charge</h4>
Robert A. Millikan's oil-drop experiment (1909) experimentally confirmed that electric charge is not continuous, but exists exclusively in discrete, integer multiples of the elementary charge $e$:
$$q = \\pm n e, \\quad n = 0, 1, 2, 3, \\dots$$
where the elementary quantum of charge is defined by the 2019 SI standard:
$$e = 1.602176634 \\times 10^{-19} \\text{ Coulombs (exact)}$$
(Note: Although quarks carry fractional charges $\\pm \\frac{1}{3}e$ and $\\pm \\frac{2}{3}e$, quark confinement strictly forbids isolated fractional charges under ordinary conditions).

<h4>3. The Law of Conservation of Electric Charge</h4>
In any closed, isolated physical system, the algebraic sum of electric charges remains strictly constant over time:
$$\\sum q_i = \\text{constant}, \\quad \\frac{d Q_{\\text{total}}}{dt} = 0$$
In relativistic and high-energy particle physics, while particles can be created or annihilated (e.g., pair production $\\gamma \\to e^- + e^+$ or electron-positron annihilation $e^- + e^+ \\to 2\\gamma$), net electric charge is conserved in every known physical interaction.

<h4>4. Continuous Charge Distributions</h4>
On macroscopic scales where individual charges cannot be resolved, charge is modeled via continuous spatial density distributions:
<ul>
  <li><strong>Linear Charge Density ($\\lambda$):</strong> $\\lambda = \\frac{dq}{dl}$ (Units: C/m)</li>
  <li><strong>Surface Charge Density ($\\sigma$):</strong> $\\sigma = \\frac{dq}{dA}$ (Units: C/m²)</li>
  <li><strong>Volume Charge Density ($\\rho$):</strong> $\\rho = \\frac{dq}{dV}$ (Units: C/m³)</li>
</ul>"""
    },
    {
        "id": "sec-1-2",
        "number": "§1.2",
        "heading": "Coulomb's Law and the Electrostatic Superposition Principle",
        "simulation": "coulomb-field-sim",
        "content": """Charles-Augustin de Coulomb (1785) established the fundamental quantitative law of electrostatic force using a precision torsion balance.

<h4>1. Coulomb's Law in Vector Form</h4>
The electrostatic force $\\vec{F}_{12}$ exerted by a point charge $q_1$ located at position $\\vec{r}_1$ on a second point charge $q_2$ located at $\\vec{r}_2$ in vacuum is:
$$\\vec{F}_{12} = \\frac{1}{4\\pi\\epsilon_0} \\frac{q_1 q_2}{|\\vec{r}_2 - \\vec{r}_1|^2} \\hat{r}_{12} = \\frac{1}{4\\pi\\epsilon_0} \\frac{q_1 q_2}{|\\vec{r}_2 - \\vec{r}_1|^3} (\\vec{r}_2 - \\vec{r}_1)$$
where:
<ul>
  <li>$\\epsilon_0$: <strong>Permittivity of Free Space (Vacuum Permittivity)</strong>:
  $$\\epsilon_0 = 8.8541878128 \\times 10^{-12} \\text{ F/m (or C}^2/(\\text{N}\\cdot\\text{m}^2))$$</li>
  <li>Coulomb's constant:
  $$k_e = \\frac{1}{4\\pi\\epsilon_0} \\approx 8.98755 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2$$</li>
  <li>By Newton's third law of action and reaction: $\\vec{F}_{21} = -\\vec{F}_{12}$.</li>
</ul>

<h4>2. Coulomb's Force in a Dielectric Medium</h4>
When point charges are embedded in a linear, isotropic, homogeneous dielectric medium of relative permittivity $\\epsilon_r$ (dielectric constant $\\kappa$):
$$\\vec{F} = \\frac{1}{4\\pi\\epsilon} \\frac{q_1 q_2}{r^2} \\hat{r} = \\frac{1}{4\\pi\\epsilon_0 \\epsilon_r} \\frac{q_1 q_2}{r^2} \\hat{r} = \\frac{\\vec{F}_{\\text{vacuum}}}{\\epsilon_r}$$
Because $\\epsilon_r > 1$ for all physical media (e.g., $\\epsilon_r \\approx 80$ for pure water at 20°C), polarization of the surrounding dielectric shields the charges, reducing the electrostatic force significantly.

<h4>3. The Superposition Principle</h4>
The net electrostatic force exerted on a test charge $q_0$ by an assembly of $N$ discrete point charges $q_1, q_2, \\dots, q_N$ is the vector sum of the individual Coulomb forces:
$$\\vec{F}_{\\text{net}} = \\sum_{i=1}^N \\vec{F}_i = \\frac{q_0}{4\\pi\\epsilon_0} \\sum_{i=1}^N \\frac{q_i}{|\\vec{r}_0 - \\vec{r}_i|^3} (\\vec{r}_0 - \\vec{r}_i)$$
For a continuous volume charge distribution $\\rho(\\vec{r}')$:
$$\\vec{F}_{\\text{net}} = \\frac{q_0}{4\\pi\\epsilon_0} \\int_V \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|^3} (\\vec{r} - \\vec{r}') dV'$$"""
    },
    {
        "id": "sec-1-3",
        "number": "§1.3",
        "heading": "The Electric Field Vector and Field Line Topology",
        "simulation": "coulomb-field-sim",
        "content": """The concept of the electric field, introduced by Michael Faraday, replaces direct action-at-a-distance with a local physical intermediary.

<h4>1. Definition of the Electric Field Vector</h4>
The <strong>electric field</strong> $\\vec{E}(\\vec{r})$ at a point in space is defined as the electrostatic force experienced per unit positive test charge placed at that location, in the limit where the test charge $q_0$ approaches zero to prevent perturbing the source charge distribution:
$$\\vec{E}(\\vec{r}) = \\lim_{q_0 \\to 0} \\frac{\\vec{F}}{q_0}$$
SI Unit: $\\text{N/C}$ (equivalent to $\\text{Volts/meter}$, $\\text{V/m}$).

<h4>2. Field of a Point Charge and Continuous Distribution</h4>
For an isolated point charge $q$ at the origin:
$$\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\frac{q}{r^2} \\hat{r}$$
For an arbitrary continuous charge distribution occupying volume $V'$:
$$\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\int_{V'} \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|^3} (\\vec{r} - \\vec{r}') dV'$$

<h4>3. Motion of a Point Charge in an Electric Field</h4>
A particle of mass $m$ and charge $q$ placed in an electric field $\\vec{E}$ experiences acceleration:
$$\\vec{a} = \\frac{\\vec{F}}{m} = \\frac{q \\vec{E}}{m}$$
In a uniform electric field $\\vec{E} = E_0 \\hat{j}$:
<ul>
  <li>A charged particle launched perpendicular to $\\vec{E}$ executes a parabolic trajectory, completely analogous to projectile motion under uniform gravity (the operational principle of cathode ray oscilloscopes and ink-jet printers).</li>
</ul>

<h4>4. Electric Field Lines (Lines of Force)</h4>
Electric field lines are imaginary curves whose tangent at any point indicates the direction of the local electric field vector $\\vec{E}$:
<ol>
  <li>Field lines originate on positive charges and terminate on negative charges (or extend to infinity).</li>
  <li>The local spatial density of lines (number of lines per unit area normal to $\\vec{E}$) is directly proportional to field magnitude $|\vec{E}|$.</li>
  <li>Field lines never intersect in free space, because the electric field vector is uniquely defined at every point.</li>
</ol>"""
    },
    {
        "id": "sec-1-4",
        "number": "§1.4",
        "heading": "The Electric Dipole in an External Electric Field",
        "simulation": "coulomb-field-sim",
        "content": """An electric dipole consists of two equal and opposite point charges $+q$ and $-q$ separated by a fixed distance $2a$.

<h4>1. The Electric Dipole Moment Vector</h4>
The <strong>electric dipole moment</strong> $\\vec{p}$ is defined as:
$$\\vec{p} = q \\vec{d}$$
where $\\vec{d}$ is the displacement vector directed from the negative charge $-q$ toward the positive charge $+q$.
SI Unit: $\\text{Coulomb}\\cdot\\text{meter}$ (C·m). (In molecular physics, the Debye unit is commonly used: $1 \\text{ D} = 3.33564 \\times 10^{-30} \\text{ C}\\cdot\\text{m}$).

<h4>2. Torque on a Dipole in a Uniform Electric Field</h4>
When placed in a uniform external field $\\vec{E}$, the net translational force on the dipole vanishes:
$$\\vec{F}_{\\text{net}} = (+q)\\vec{E} + (-q)\\vec{E} = 0$$
However, the forces act along different lines of action, producing a net mechanical restoring torque:
$$\\vec{\\tau} = \\vec{r}_+ \\times (q\\vec{E}) + \\vec{r}_- \\times (-q\\vec{E}) = (\\vec{r}_+ - \\vec{r}_-) \\times q\\vec{E} = \\vec{d} \\times q\\vec{E}$$
$$\\vec{\\tau} = \\vec{p} \\times \\vec{E}$$
Magnitude: $\\tau = p E \\sin\\theta$, where $\\theta$ is the angle between $\\vec{p}$ and $\\vec{E}$.
The torque acts to align the dipole moment parallel to the external field ($\theta = 0$).

<h4>3. Potential Energy of an Electric Dipole</h4>
The external work required to rotate the dipole from reference angle $\\theta_0 = 90^\\circ$ to angle $\\theta$ is:
$$U(\\theta) = \\int_{90^\\circ}^\\theta \\tau_{\\text{ext}} d\\theta' = \\int_{90^\\circ}^\\theta (p E \\sin\\theta') d\\theta' = -p E \\cos\\theta$$
$$U = -\\vec{p} \\cdot \\vec{E}$$
<ul>
  <li><strong>Stable Equilibrium ($\\theta = 0^\circ$):</strong> Dipole aligned with $\\vec{E}$; minimum potential energy $U_{\\min} = -p E$.</li>
  <li><strong>Unstable Equilibrium ($\\theta = 180^\circ$):</strong> Dipole antiparallel to $\\vec{E}$; maximum potential energy $U_{\\max} = +p E$.</li>
</ul>

<h4>4. Dipole in a Non-Uniform Electric Field</h4>
In an inhomogeneous field where $\\vec{E}$ varies spatially, the forces on $+q$ and $-q$ do not cancel. The net translational force is:
$$\\vec{F} = (\\vec{p} \\cdot \\nabla) \\vec{E} = \\nabla (\\vec{p} \\cdot \\vec{E})$$
A neutral dipole is always pulled toward regions of stronger electric field strength."""
    },
    {
        "id": "sec-1-5",
        "number": "§1.5",
        "heading": "Electric Flux and Gauss's Law",
        "simulation": "gauss-flux-sim",
        "content": """Carl Friedrich Gauss (1835) formulated Gauss's law, which relates the total electric flux passing through a closed geometric surface to the enclosed net electric charge.

<h4>1. Definition of Electric Flux</h4>
The <strong>electric flux</strong> $d\\Phi_E$ through an infinitesimal oriented surface element $d\\vec{A} = \\hat{n} dA$ is:
$$d\\Phi_E = \\vec{E} \\cdot d\\vec{A} = E \\cos\\theta \\, dA$$
where $\\hat{n}$ is the outward unit normal vector.
For an arbitrary closed Gaussian surface $S$:
$$\\Phi_E = \\oint_S \\vec{E} \\cdot d\\vec{A}$$
SI Unit: $\\text{N}\\cdot\\text{m}^2/\\text{C} = \\text{V}\\cdot\\text{m}$.

<h4>2. Gauss's Law in Integral Form</h4>
For an isolated point charge $q$ enclosed by a concentric sphere of radius $r$:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\oint_S \\left( \\frac{q}{4\\pi\\epsilon_0 r^2} \\hat{r} \\right) \\cdot (\\hat{r} dA) = \\frac{q}{4\\pi\\epsilon_0 r^2} (4\\pi r^2) = \\frac{q}{\\epsilon_0}$$
By superposition, for any arbitrary closed surface enclosing net charge $Q_{\\text{encl}}$:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\frac{Q_{\\text{enclosed}}}{\\epsilon_0}$$
This is **Gauss's Law** (the first of Maxwell's four foundational equations of electromagnetism).

<h4>3. Key Properties of Gauss's Law</h4>
<ul>
  <li>Gauss's law holds for *any* closed surface of arbitrary shape (called a Gaussian surface).</li>
  <li>Charges located *outside* the closed surface contribute zero net flux through the surface (any flux entering must leave).</li>
  <li>Gauss's law is a direct mathematical consequence of the inverse-square nature of Coulomb's force ($F \\propto 1/r^2$). If the force followed $1/r^{2+\\delta}$, Gauss's law would fail.</li>
</ul>

<h4>4. Differential Form of Gauss's Law</h4>
Applying Gauss's Divergence Theorem:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\int_V (\\nabla \\cdot \\vec{E}) dV = \\frac{1}{\\epsilon_0} \\int_V \\rho \\, dV$$
Since this holds for any arbitrary volume $V$:
$$\\nabla \\cdot \\vec{E} = \\frac{\\rho}{\\epsilon_0}$$
This is the differential form of Gauss's law, stating that positive charge density acts as a local source (divergence) of electric field lines, and negative charge acts as a sink."""
    },
    {
        "id": "sec-1-6",
        "number": "§1.6",
        "heading": "Applications of Gauss's Law: Spherical, Cylindrical, and Planar Symmetries",
        "simulation": "gauss-flux-sim",
        "content": """Gauss's law enables direct calculation of electric field configurations when the charge distribution possesses high geometric symmetry.

<h4>1. Spherically Symmetric Charge Distribution</h4>
Consider a solid insulating sphere of radius $R$ with uniform volume charge density $\\rho$ (total charge $Q = \\frac{4}{3}\\pi R^3 \\rho$).
By spherical symmetry, $\\vec{E} = E(r) \\hat{r}$. Construct a concentric spherical Gaussian surface of radius $r$:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E(r) \\oint_S dA = E(r) (4\\pi r^2)$$
<ul>
  <li><strong>Outside the Sphere ($r \\ge R$):</strong>
  $$Q_{\\text{encl}} = Q \\implies E(r) (4\\pi r^2) = \\frac{Q}{\\epsilon_0} \\implies E(r) = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{r^2}$$
  The external field is identical to that of a point charge $Q$ at the center.</li>
  <li><strong>Inside the Sphere ($r < R$):</strong>
  $$Q_{\\text{encl}} = \\rho \\left( \\frac{4}{3}\\pi r^3 \\right) = Q \\left( \\frac{r^3}{R^3} \\right)$$
  $$E(r) (4\\pi r^2) = \\frac{Q r^3}{\\epsilon_0 R^3} \\implies E(r) = \\frac{Q}{4\\pi\\epsilon_0 R^3} r = \\frac{\\rho}{3\\epsilon_0} r$$
  Inside the sphere, the electric field increases linearly from zero at the center to maximum at the surface!</li>
</ul>

<h4>2. Infinitely Long Line of Charge (Cylindrical Symmetry)</h4>
Consider an infinite line carrying uniform linear charge density $\\lambda$ (C/m).
Construct a coaxial cylindrical Gaussian surface of radius $r$ and length $L$.
Flux through the two flat end caps is zero because $\\vec{E} \\perp \\hat{n}_{\\text{caps}}$.
Flux through the curved cylindrical jacket of area $2\\pi r L$:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E(r) (2\\pi r L) = \\frac{Q_{\\text{encl}}}{\\epsilon_0} = \\frac{\\lambda L}{\\epsilon_0}$$
$$E(r) = \\frac{\\lambda}{2\\pi\\epsilon_0 r}$$
The field decays inversely with radial distance ($E \\propto 1/r$).

<h4>3. Infinite Plane Sheet of Charge (Planar Symmetry)</h4>
Consider an infinite non-conducting flat plane with uniform surface charge density $\\sigma$ (C/m²).
Construct a cylindrical Gaussian pillbox of cross-sectional area $A$ piercing the sheet perpendicularly.
Flux through the cylindrical mantle is zero ($\vec{E} \parallel \text{mantle}$). Flux passes equally out of both end faces:
$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E A + E A = 2 E A = \\frac{Q_{\\text{encl}}}{\\epsilon_0} = \\frac{\\sigma A}{\\epsilon_0}$$
$$E = \\frac{\\sigma}{2\\epsilon_0}$$
Remarkably, the field is completely **uniform and independent of distance** from the sheet!
For a conducting surface where all charge resides on the outer boundary and $\vec{E}_{\text{inside}} = 0$:
$$E_{\\text{conductor}} = \\frac{\\sigma}{\\epsilon_0}$$"""
    }
]

u1_problems = [
    {
        "id": "prob-1-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Coulomb Vector Superposition for Multiple Point Charges",
        "question": "Three point charges are positioned at the vertices of an equilateral triangle of side length $a = 20.0\\text{ cm}$ in vacuum: $q_1 = +4.00\\ \\mu\\text{C}$ at $(0, 0)$, $q_2 = +4.00\\ \\mu\\text{C}$ at $(a, 0)$, and $q_3 = -2.00\\ \\mu\\text{C}$ at the top vertex $(a/2, a\\sqrt{3}/2)$.\\n(a) Calculate the magnitude and direction of the net electrostatic force $\\vec{F}_3$ exerted on charge $q_3$, and\\n(b) Determine the electric field vector $\\vec{E}$ at the centroid of the triangle.",
        "steps": [
            {
                "title": "Step 1: Compute forces from q1 and q2 on q3",
                "math": "$$F_{13} = \\frac{1}{4\\pi\\epsilon_0} \\frac{|q_1 q_3|}{a^2} = \\frac{(8.988 \\times 10^9) \\times (4.00 \\times 10^{-6}) \\times (2.00 \\times 10^{-6})}{(0.200)^2}$$\n$$F_{13} = \\frac{0.07190}{0.0400} = 1.798 \\text{ N}$$\n$$F_{23} = F_{13} = 1.798 \\text{ N (by symmetry)}$$",
                "explanation": "Because $q_3$ is negative and $q_1, q_2$ are positive, both forces are attractive and point down toward the base vertices."
            },
            {
                "title": "Step 2: Vector resolution of net force on q3",
                "math": "$$\\text{Angle with vertical: } \\theta = 30.0^\\circ$$\n$$F_{3x} = F_{13}\\sin(30^\\circ) - F_{23}\\sin(30^\\circ) = 0$$\n$$F_{3y} = -F_{13}\\cos(30^\\circ) - F_{23}\\cos(30^\\circ) = -2 \\times 1.798 \\times \\cos(30^\\circ)$$\n$$F_{3y} = -2 \\times 1.798 \\times 0.8660 = -3.114 \\text{ N}$$\n$$\\vec{F}_3 = -3.11 \\hat{j} \\text{ N}$$",
                "explanation": "Horizontal components cancel identically by symmetry, leaving a purely downward net force of 3.11 N."
            },
            {
                "title": "Step 3: Electric field at the centroid",
                "math": "$$\\text{Distance from vertex to centroid: } r_c = \\frac{a}{\\sqrt{3}} = \\frac{0.200}{\\sqrt{3}} = 0.1155 \\text{ m}$$\n$$\\vec{E}_{1+2} = \\text{sum of fields from } q_1, q_2 \\text{ points straight up along } +\\hat{j}:$$\n$$E_y = \\frac{1}{4\\pi\\epsilon_0 r_c^2} [q_1 \\cos(30^\\circ) + q_2 \\cos(30^\\circ) + |q_3|] = \\frac{8.988 \\times 10^9}{(0.1155)^2} \\times [2(4.00\\times 10^{-6})(0.866) + 2.00\\times 10^{-6}]$$\n$$E_y = \\frac{8.988 \\times 10^9}{0.01333} \\times [6.928 + 2.00] \\times 10^{-6} = (6.743 \\times 10^{11}) \\times (8.928 \\times 10^{-6}) = 6.02 \\times 10^6 \\text{ V/m} \\,\\hat{j}$$",
                "explanation": "The net electric field at the centroid points vertically upward with magnitude $6.02 \\times 10^6$ V/m."
            }
        ]
    },
    {
        "id": "prob-1-2",
        "difficulty": "Honors Electrodynamics Standard",
        "title": "Electric Dipole Field and Torque in External Field",
        "question": "A water molecule ($H_2O$) possesses a permanent electric dipole moment $p = 6.17 \\times 10^{-30}\\text{ C}\\cdot\\text{m}$. It is placed in a uniform electric field $E = 4.50 \\times 10^5\\text{ N/C}$ directed along the $+x$-axis, with its dipole moment initially inclined at $\\theta = 60.0^\\circ$ to the field.\\n(a) Calculate the magnitude of the torque $\\vec{\\tau}$ acting on the molecule,\\n(b) Find the potential energy $U$ of the dipole in this orientation, and\\n(c) Calculate the external work required to rotate the molecule from $\\theta = 60.0^\\circ$ to $\\theta = 180.0^\\circ$.",
        "steps": [
            {
                "title": "Step 1: Compute torque magnitude",
                "math": "$$\\tau = p E \\sin\\theta = (6.17 \\times 10^{-30} \\text{ C}\\cdot\\text{m}) \\times (4.50 \\times 10^5 \\text{ N/C}) \\times \\sin(60.0^\\circ)$$\n$$\\tau = (2.7765 \\times 10^{-24}) \\times 0.86603 = 2.404 \\times 10^{-24} \\text{ N}\\cdot\\text{m}$$",
                "explanation": "The torque acts clockwise to rotate the dipole into alignment with the positive x-axis."
            },
            {
                "title": "Step 2: Potential energy in field",
                "math": "$$U = -\\vec{p} \\cdot \\vec{E} = -p E \\cos\\theta = -(6.17 \\times 10^{-30}) \\times (4.50 \\times 10^5) \\times \\cos(60.0^\\circ)$$\n$$U = -2.7765 \\times 10^{-24} \\times 0.500 = -1.388 \\times 10^{-24} \\text{ Joules}$$",
                "explanation": "The negative potential energy confirms the configuration is bound relative to the 90° reference."
            },
            {
                "title": "Step 3: Work required to rotate to antiparallel orientation",
                "math": "$$W_{\\text{ext}} = \\Delta U = U(180^\\circ) - U(60^\\circ)$$\n$$U(180^\\circ) = -p E \\cos(180^\\circ) = +p E = +2.7765 \\times 10^{-24} \\text{ J}$$\n$$W_{\\text{ext}} = 2.7765 \\times 10^{-24} - (-1.3882 \\times 10^{-24}) = +4.165 \\times 10^{-24} \\text{ Joules}$$",
                "explanation": "An external agent must perform $4.17 \\times 10^{-24}$ J of work against the electrostatic restoring torque."
            }
        ]
    },
    {
        "id": "prob-1-3",
        "difficulty": "Standard University Exam Problem",
        "title": "Gauss's Law for Non-Uniform Spherical Charge Density",
        "question": "A solid insulating sphere of radius $R = 12.0\\text{ cm}$ carries a spherically symmetric charge distribution whose volume charge density varies with radial distance $r$ according to $\\rho(r) = \\rho_0 (1 - r/R)$, where $\\rho_0 = 3.50 \\times 10^{-6}\\text{ C/m}^3$.\\n(a) Determine the total charge $Q$ of the sphere,\\n(b) Derive the electric field $E(r)$ inside the sphere ($r \\le R$) and find the radial position $r_{\\max}$ where the electric field attains its maximum value, and\\n(c) Calculate the magnitude of the electric field at $r = R$ and at $r = 2R$.",
        "steps": [
            {
                "title": "Step 1: Calculate total charge by volume integration",
                "math": "$$Q = \\int_0^R \\rho(r) (4\\pi r^2 dr) = 4\\pi \\rho_0 \\int_0^R \\left( r^2 - \\frac{r^3}{R} \\right) dr$$\n$$Q = 4\\pi \\rho_0 \\left[ \\frac{R^3}{3} - \\frac{R^4}{4R} \\right] = 4\\pi \\rho_0 R^3 \\left( \\frac{1}{3} - \\frac{1}{4} \\right) = \\frac{\\pi \\rho_0 R^3}{3}$$\n$$Q = \\frac{\\pi \\times (3.50 \\times 10^{-6}) \\times (0.120)^3}{3} = \\frac{\\pi \\times 3.50 \\times 10^{-6} \\times 1.728 \\times 10^{-3}}{3} = 6.333 \\times 10^{-9} \\text{ C} = 6.33 \\text{ nC}$$",
                "explanation": "Integrating spherical shells of volume $4\pi r^2 dr$ yields a total enclosed charge of 6.33 nC."
            },
            {
                "title": "Step 2: Derive electric field inside and find maximum",
                "math": "$$Q_{\\text{encl}}(r) = 4\\pi \\rho_0 \\left[ \\frac{r^3}{3} - \\frac{r^4}{4R} \\right]$$\n$$\\oint \\vec{E} \\cdot d\\vec{A} = E(r) (4\\pi r^2) = \\frac{Q_{\\text{encl}}(r)}{\\epsilon_0} \\implies E(r) = \\frac{\\rho_0}{\\epsilon_0} \\left( \\frac{r}{3} - \\frac{r^2}{4R} \\right)$$\n$$\\text{For maximum } E: \\frac{dE}{dr} = \\frac{\\rho_0}{\\epsilon_0} \\left( \\frac{1}{3} - \\frac{2r}{4R} \\right) = 0 \\implies \\frac{1}{3} = \\frac{r}{2R} \\implies r_{\\max} = \\frac{2}{3}R$$\n$$r_{\\max} = \\frac{2}{3} \\times 12.0 \\text{ cm} = 8.00 \\text{ cm}$$",
                "explanation": "The electric field reaches its peak at two-thirds of the sphere's radius."
            },
            {
                "title": "Step 3: Evaluate electric fields at surface and r = 2R",
                "math": "$$E(R) = \\frac{\\rho_0}{\\epsilon_0} \\left( \\frac{R}{3} - \\frac{R}{4} \\right) = \\frac{\\rho_0 R}{12 \\epsilon_0} = \\frac{(3.50 \\times 10^{-6}) \\times 0.120}{12 \\times (8.854 \\times 10^{-12})} = \\frac{4.20 \\times 10^{-7}}{1.0625 \\times 10^{-10}} = 3953 \\text{ V/m}$$\n$$E(2R) = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{(2R)^2} = \\frac{E(R)}{4} \\times \\left(\\frac{R^2}{R^2}\\right) = \\frac{8.988 \\times 10^9 \\times 6.333 \\times 10^{-9}}{(0.240)^2} = \\frac{56.92}{0.0576} = 988 \\text{ V/m}$$",
                "explanation": "At the surface $E = 3.95$ kV/m; outside at $2R = 24$ cm, it drops to 988 V/m via the inverse-square law."
            }
        ]
    }
]

unit1_data = {
    "number": 1,
    "title": "Electric Field and Gauss's Law",
    "leadSummary": "A rigorous foundation of electrostatics: charge quantization and conservation, Coulomb's inverse-square law, vector superposition, electric field lines, dipole dynamics and torque, electric flux, Gauss's law in integral and differential forms, and applications to spherical, cylindrical, and planar symmetries.",
    "sections": u1_sections,
    "problems": u1_problems
}

with open("em_u1.json", "w") as f:
    json.dump(unit1_data, f, indent=2)

print("Unit 1 built successfully with", len(u1_sections), "sections and", len(u1_problems), "problems!")

# =========================================================================
# UNIT 2: Electric Potential
# =========================================================================
u2_sections = [
    {
        "id": "sec-2-1",
        "number": "§2.1",
        "heading": "Electrostatic Potential and Conservative Electric Fields",
        "simulation": "potential-gradient-sim",
        "content": """The electrostatic force is conservative, which allows the introduction of a scalar electric potential field.

<h4>1. Path Independence and Conservative Nature</h4>
The work done by the electrostatic force on a test charge $q_0$ moving from point $A$ to point $B$ in any static electric field is strictly independent of the physical path taken:
$$W_{A \\to B} = \\int_A^B \\vec{F} \\cdot d\\vec{r} = q_0 \\int_A^B \\vec{E} \\cdot d\\vec{r}$$
Consequently, the line integral of the electrostatic field around any closed loop vanishes identically:
$$\\oint_C \\vec{E} \\cdot d\\vec{r} = 0$$
By Stokes' theorem:
$$\\oint_C \\vec{E} \\cdot d\\vec{r} = \\int_S (\\nabla \\times \\vec{E}) \\cdot d\\vec{A} = 0 \\implies \\nabla \\times \\vec{E} = 0$$
The static electric field is strictly **irrotational** (conservative).

<h4>2. Definition of Electric Potential ($V$)</h4>
The electric potential difference $\\Delta V = V_B - V_A$ between points $A$ and $B$ is defined as the external work required per unit positive test charge to transport it from $A$ to $B$ at constant kinetic energy:
$$\\Delta V = V_B - V_A = -\\int_A^B \\vec{E} \\cdot d\\vec{r}$$
Taking the standard reference point at infinity ($V(\\infty) = 0$), the absolute electric potential at point $P$ is:
$$V(\\vec{r}) = -\\int_\\infty^{\\vec{r}} \\vec{E} \\cdot d\\vec{r}'$$
SI Unit: **Volt (V)**:
$$1 \\text{ Volt} = 1 \\text{ Joule/Coulomb (J/C)}$$
Dimensionally: $[V] = M L^2 T^{-3} I^{-1}$.

<h4>3. Electric Potential Energy ($U$)</h4>
The electrostatic potential energy $U$ of a charge $q$ located at a point of electric potential $V$ is:
$$U = q V$$
The electron-volt (eV) is defined as the kinetic energy acquired by an electron accelerated through a potential difference of 1 Volt:
$$1 \\text{ eV} = 1.602176634 \\times 10^{-19} \\text{ Joules}$$"""
    },
    {
        "id": "sec-2-2",
        "number": "§2.2",
        "heading": "Potential due to Point Charges, Dipoles, and Continuous Distributions",
        "simulation": "potential-gradient-sim",
        "content": """Calculating the scalar electric potential is algebraically much simpler than computing the vector electric field directly.

<h4>1. Potential of an Isolated Point Charge</h4>
Integrating the radial field $\\vec{E} = \\frac{q}{4\\pi\\epsilon_0 r^2}\\hat{r}$ from $\\infty$ to $r$:
$$V(r) = -\\int_\\infty^r \\frac{q}{4\\pi\\epsilon_0 r'^2} dr' = \\left[ \\frac{q}{4\\pi\\epsilon_0 r'} \\right]_\\infty^r = \\frac{1}{4\\pi\\epsilon_0} \\frac{q}{r}$$
Notice $V \\propto 1/r$ (whereas field $E \\propto 1/r^2$).
By scalar superposition, the potential due to $N$ discrete point charges is:
$$V(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\sum_{i=1}^N \\frac{q_i}{|\\vec{r} - \\vec{r}_i|}$$

<h4>2. Potential of an Electric Dipole</h4>
Consider a dipole consisting of $+q$ at $(0, 0, a)$ and $-q$ at $(0, 0, -a)$ with dipole moment $p = 2qa$ aligned along the z-axis.
At field point $(r, \\theta)$ where distance $r \\gg a$:
$$r_+ \\approx r - a \\cos\\theta, \\quad r_- \\approx r + a \\cos\\theta$$
$$V(r, \\theta) = \\frac{q}{4\\pi\\epsilon_0} \\left( \\frac{1}{r_+} - \\frac{1}{r_-} \\right) \\approx \\frac{q}{4\\pi\\epsilon_0} \\left( \\frac{r_- - r_+}{r^2} \\right) = \\frac{q (2a \\cos\\theta)}{4\\pi\\epsilon_0 r^2}$$
$$V(r, \\theta) = \\frac{1}{4\\pi\\epsilon_0} \\frac{\\vec{p} \\cdot \\hat{r}}{r^2} = \\frac{1}{4\\pi\\epsilon_0} \\frac{p \\cos\\theta}{r^2}$$
Key properties of the dipole potential:
<ul>
  <li>Decays as $1/r^2$ (faster than the $1/r$ point charge monopole potential).</li>
  <li>Vanishes identically in the equatorial plane ($\\theta = 90^\\circ \\implies \\cos(90^\\circ) = 0$).</li>
</ul>

<h4>3. Continuous Charge Distributions</h4>
For continuous sources:
$$V(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\int_{V'} \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dV'$$
$$V_{\\text{surface}} = \\frac{1}{4\\pi\\epsilon_0} \\int_{S'} \\frac{\\sigma(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dA', \\quad V_{\\text{line}} = \\frac{1}{4\\pi\\epsilon_0} \\int_{L'} \\frac{\\lambda(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dl'$$"""
    },
    {
        "id": "sec-2-3",
        "number": "§2.3",
        "heading": "Calculation of Electric Field from Potential: The Negative Gradient",
        "simulation": "potential-gradient-sim",
        "content": """Because the electrostatic field is conservative ($\\nabla \\times \\vec{E} = 0$), vector calculus guarantees that it can be expressed as the negative gradient of a scalar potential.

<h4>1. The Gradient Relation</h4>
Consider an infinitesimal displacement $d\\vec{r} = dx \\hat{i} + dy \\hat{j} + dz \\hat{k}$:
$$dV = -\\vec{E} \\cdot d\\vec{r} = - (E_x dx + E_y dy + E_z dz)$$
By the multivariable chain rule:
$$dV = \\frac{\\partial V}{\\partial x} dx + \\frac{\\partial V}{\\partial y} dy + \\frac{\\partial V}{\\partial z} dz$$
Equating coefficients:
$$E_x = -\\frac{\\partial V}{\\partial x}, \\quad E_y = -\\frac{\\partial V}{\\partial y}, \\quad E_z = -\\frac{\\partial V}{\\partial z}$$
In compact vector notation:
$$\\vec{E} = -\\nabla V$$
where $\\nabla = \\hat{i} \\frac{\\partial}{\\partial x} + \\hat{j} \\frac{\\partial}{\\partial y} + \\hat{k} \\frac{\\partial}{\\partial z}$ is the vector del operator.

<h4>2. Physical Interpretation</h4>
<ul>
  <li>The mathematical gradient $\\nabla V$ points in the direction of maximum spatial increase of potential.</li>
  <li>Therefore, the electric field vector $\\vec{E} = -\\nabla V$ **always points in the direction of steepest potential decrease**.</li>
  <li>Positive charges naturally accelerate from regions of high electric potential toward regions of low electric potential.</li>
</ul>

<h4>3. Equipotential Surfaces and Orthogonality</h4>
An **equipotential surface** is the spatial locus of all points having identical electric potential ($V(x, y, z) = \\text{constant}$).
For any displacement $d\\vec{r}$ lying entirely within an equipotential surface:
$$dV = -\\vec{E} \\cdot d\\vec{r} = 0$$
Because $d\\vec{r}$ is non-zero, this requires:
$$\\vec{E} \\perp d\\vec{r}$$
<em>Fundamental Geometric Theorem:</em> The electric field vector is everywhere perpendicular (orthogonal) to equipotential surfaces. Equipotential lines and electric field lines form a mutually orthogonal coordinate mesh."""
    },
    {
        "id": "sec-2-4",
        "number": "§2.4",
        "heading": "Electrostatic Properties of Insulated Conductors in Equilibrium",
        "simulation": "potential-gradient-sim",
        "content": """In an electrical conductor, valence electrons are free to migrate throughout the crystalline lattice. In static equilibrium, charge migration ceases, establishing several fundamental physical theorems.

<h4>1. Zero Internal Electric Field</h4>
Inside the bulk material of a conductor in electrostatic equilibrium:
$$\\vec{E}_{\\text{internal}} = 0$$
*Proof:* If $\\vec{E}$ were non-zero inside, the free electrons would experience forces $\\vec{F} = -e\\vec{E}$ and accelerate, generating macroscopic currents, contradicting the premise of static equilibrium.

<h4>2. Zero Net Internal Charge Density</h4>
Applying Gauss's law $\\nabla \\cdot \\vec{E} = \\rho / \\epsilon_0$ to any interior region:
$$\\vec{E} = 0 \\implies \\rho = 0$$
*Theorem:* Any net excess electric charge deposited on an insulated conductor resides entirely on its outer geometric surface.

<h4>3. The Entire Conductor is an Equipotential Volume</h4>
For any two interior points $A$ and $B$:
$$V_B - V_A = -\\int_A^B \\vec{E} \\cdot d\\vec{r} = 0 \\implies V_A = V_B = \\text{constant}$$
The surface and entire interior of a conductor exist at the exact same scalar potential.

<h4>4. Electric Field Immediately Outside a Charged Conductor</h4>
Construct a Gaussian pillbox of area $dA$ straddling the conductor surface:
The bottom face inside the metal has $\\vec{E} = 0$. The curved side has zero flux. The top face outside has field $\\vec{E} \\perp$ surface:
$$\\oint \\vec{E} \\cdot d\\vec{A} = E dA = \\frac{dq}{\\epsilon_0} = \\frac{\\sigma dA}{\\epsilon_0} \\implies E = \\frac{\\sigma}{\\epsilon_0}$$
$$\\vec{E} = \\frac{\\sigma}{\\epsilon_0} \\hat{n}$$
Notice this field is exactly double the field of a single non-conducting sheet ($\\sigma / 2\\epsilon_0$), because charge inside the conductor rearranges to produce zero field internally and constructive reinforcement externally.

<h4>5. Electrostatic Shielding (Faraday Cage)</h4>
In a hollow conducting shell with a cavity containing zero charge, $\\vec{E} = 0$ everywhere inside the cavity, regardless of external electric fields. This is **electrostatic shielding**."""
    },
    {
        "id": "sec-2-5",
        "number": "§2.5",
        "heading": "The Van de Graaff Electrostatic Generator and High Voltage Physics",
        "simulation": "potential-gradient-sim",
        "content": """Robert J. Van de Graaff (1929) developed the electrostatic accelerator generator, capable of generating potentials exceeding 5 to 20 million Volts.

<h4>1. Working Principle</h4>
The Van de Graaff generator exploits two electrostatic principles:
<ol>
  <li><strong>Corona Discharge (Action of Sharp Points):</strong> At sharp conducting needles of radius of curvature $r$, the surface charge density $\\sigma \\propto 1/r$ becomes immense. When local field exceeds the dielectric breakdown strength of air ($E_{\\text{breakdown}} \\approx 3 \\times 10^6 \\text{ V/m}$), air molecules ionize, spraying ions onto an insulating moving belt.</li>
  <li><strong>Cavity Charge Transfer:</strong> When a charged conductor contacts the *interior* surface of a hollow conducting sphere, all charge transfers completely to the *exterior* surface, regardless of how high the sphere's potential already is!</li>
</ol>

<h4>2. Mathematical Limit on Terminal Potential</h4>
For a spherical high-voltage dome of radius $R$ carrying charge $Q$:
$$V = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{R}, \\quad E = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{R^2} = \\frac{V}{R}$$
Hence, the maximum sustainable potential is limited by dielectric breakdown of the surrounding gas:
$$V_{\\max} = R \\cdot E_{\\text{breakdown}}$$
In atmospheric air ($E_b = 3 \\text{ MV/m}$), a dome of radius $R = 1.0\\text{ m}$ attains $V_{\\max} = 3.0\\text{ MV}$.
Immersing the generator in high-pressure insulating sulfur hexafluoride ($SF_6$) gas raises $E_b$ fivefold, enabling tandem accelerators to reach 25 million Volts for nuclear transmutation experiments."""
    }
]

u2_problems = [
    {
        "id": "prob-2-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Electric Potential of an Annular Charged Disk",
        "question": "A thin flat non-conducting annular ring has inner radius $a = 5.00\\text{ cm}$ and outer radius $b = 15.0\\text{ cm}$. It carries a uniform surface charge density $\\sigma = 4.00 \\times 10^{-6}\\text{ C/m}^2$.\\n(a) Derive an analytical expression for the electric potential $V(z)$ along the central axis of symmetry at perpendicular distance $z$ from the plane of the ring,\\n(b) Calculate $V$ at $z = 10.0\\text{ cm}$, and\\n(c) Use $\\vec{E} = -\\nabla V$ to determine the axial electric field $E_z(z)$ at $z = 10.0\\text{ cm}$.",
        "steps": [
            {
                "title": "Step 1: Integrate annular rings to derive potential",
                "math": "$$dq = \\sigma (2\\pi r dr)$$\n$$\\text{Distance to axial point: } R_d = \\sqrt{z^2 + r^2}$$\n$$V(z) = \\frac{1}{4\\pi\\epsilon_0} \\int_a^b \\frac{\\sigma (2\\pi r dr)}{\\sqrt{z^2 + r^2}} = \\frac{\\sigma}{2\\epsilon_0} \\left[ \\sqrt{z^2 + r^2} \\right]_a^b$$\n$$V(z) = \\frac{\\sigma}{2\\epsilon_0} \\left( \\sqrt{z^2 + b^2} - \\sqrt{z^2 + a^2} \\right)$$",
                "explanation": "Integrating concentric infinitesimal rings of area $2\pi r dr$ gives the exact axial potential."
            },
            {
                "title": "Step 2: Numerical evaluation at z = 10.0 cm",
                "math": "$$\\sqrt{z^2 + b^2} = \\sqrt{(0.100)^2 + (0.150)^2} = \\sqrt{0.0100 + 0.0225} = \\sqrt{0.0325} = 0.18028 \\text{ m}$$\n$$\\sqrt{z^2 + a^2} = \\sqrt{(0.100)^2 + (0.050)^2} = \\sqrt{0.0100 + 0.0025} = \\sqrt{0.0125} = 0.11180 \\text{ m}$$\n$$\\Delta R_d = 0.18028 - 0.11180 = 0.06848 \\text{ m}$$\n$$V = \\frac{4.00 \\times 10^{-6}}{2 \\times (8.854 \\times 10^{-12})} \\times 0.06848 = (2.2588 \\times 10^5) \\times 0.06848 = 15468 \\text{ Volts} = 15.47 \\text{ kV}$$",
                "explanation": "The electric potential at $z = 10$ cm on the axis is 15.5 kV."
            },
            {
                "title": "Step 3: Differentiate to find axial electric field",
                "math": "$$E_z = -\\frac{dV}{dz} = -\\frac{\\sigma}{2\\epsilon_0} \\left( \\frac{z}{\\sqrt{z^2 + b^2}} - \\frac{z}{\\sqrt{z^2 + a^2}} \\right) = \\frac{\\sigma z}{2\\epsilon_0} \\left( \\frac{1}{\\sqrt{z^2 + a^2}} - \\frac{1}{\\sqrt{z^2 + b^2}} \\right)$$\n$$E_z = (2.2588 \\times 10^5) \\times 0.100 \\times \\left( \\frac{1}{0.11180} - \\frac{1}{0.18028} \\right)$$\n$$E_z = 22588 \\times (8.9446 - 5.5469) = 22588 \\times 3.3977 = 76747 \\text{ V/m} = 76.7 \\text{ kV/m}$$",
                "explanation": "Evaluating the negative gradient gives an axial field of 76.7 kV/m directed outward along $+z$."
            }
        ]
    },
    {
        "id": "prob-2-2",
        "difficulty": "Honors Electrodynamics Standard",
        "title": "Electrostatic Potential Energy and Assembly of Charge Distribution",
        "question": "A spherical ball of radius $R = 8.00\\text{ cm}$ carries total charge $Q = 12.0\\ \\mu\\text{C}$ uniformly distributed throughout its volume.\\n(a) Derive the total electrostatic potential energy $U$ stored in the system by assembling spherical shell layers from infinity,\\n(b) Calculate the numerical value of $U$ in Joules, and\\n(c) What fraction of this total energy resides strictly inside the sphere ($r < R$) versus outside ($r > R$)?",
        "steps": [
            {
                "title": "Step 1: Assemble sphere shell by shell",
                "math": "$$\\text{When sphere has reached radius } r, \\text{ charge is } q(r) = Q \\left(\\frac{r^3}{R^3}\\right)$$\n$$\\text{Potential at surface: } V(r) = \\frac{1}{4\\pi\\epsilon_0} \\frac{q(r)}{r} = \\frac{Q r^2}{4\\pi\\epsilon_0 R^3}$$\n$$\\text{Work to bring shell } dq = \\rho (4\\pi r^2 dr) = \\left(\\frac{3Q}{4\\pi R^3}\\right) (4\\pi r^2 dr) = \\frac{3Q r^2 dr}{R^3}:$$\n$$dU = V(r) dq = \\left( \\frac{Q r^2}{4\\pi\\epsilon_0 R^3} \\right) \\left( \\frac{3Q r^2 dr}{R^3} \\right) = \\frac{3 Q^2 r^4 dr}{4\\pi\\epsilon_0 R^6}$$\n$$U = \\frac{3 Q^2}{4\\pi\\epsilon_0 R^6} \\int_0^R r^4 dr = \\frac{3 Q^2}{4\\pi\\epsilon_0 R^6} \\left(\\frac{R^5}{5}\\right) = \\frac{3 Q^2}{20 \\pi \\epsilon_0 R} = \\frac{3}{5} \\left( \\frac{1}{4\\pi\\epsilon_0} \\frac{Q^2}{R} \\right)$$",
                "explanation": "The total self-energy of a uniformly charged solid sphere is $\\frac{3}{5} \\frac{Q^2}{4\pi\epsilon_0 R}$."
            },
            {
                "title": "Step 2: Numerical evaluation",
                "math": "$$U = \\frac{3}{5} \\times (8.988 \\times 10^9) \\times \\frac{(12.0 \\times 10^{-6})^2}{0.0800}$$\n$$U = 0.600 \\times (8.988 \\times 10^9) \\times \\frac{1.44 \\times 10^{-10}}{0.0800} = 5.3928 \\times 10^9 \\times 1.80 \\times 10^{-9} = 9.707 \\text{ Joules}$$",
                "explanation": "The electrostatic self-energy of the charged ball is 9.71 Joules."
            },
            {
                "title": "Step 3: Energy partitioned inside versus outside",
                "math": "$$u_E = \\frac{1}{2}\\epsilon_0 E^2$$\n$$U_{\\text{outside}} = \\int_R^\\infty \\frac{1}{2}\\epsilon_0 \\left( \\frac{Q}{4\\pi\\epsilon_0 r^2} \\right)^2 (4\\pi r^2 dr) = \\frac{Q^2}{8\\pi\\epsilon_0} \\int_R^\\infty \\frac{dr}{r^2} = \\frac{Q^2}{8\\pi\\epsilon_0 R} = \\frac{1}{2} \\left( \\frac{1}{4\\pi\\epsilon_0} \\frac{Q^2}{R} \\right)$$\n$$U_{\\text{inside}} = U_{\\text{total}} - U_{\\text{outside}} = \\left(\\frac{3}{5} - \\frac{1}{2}\\right) \\frac{Q^2}{4\\pi\\epsilon_0 R} = \\frac{1}{10} \\left( \\frac{1}{4\\pi\\epsilon_0} \\frac{Q^2}{R} \\right)$$\n$$\\frac{U_{\\text{inside}}}{U_{\\text{total}}} = \\frac{1/10}{3/5} = \\frac{1}{6} \\approx 16.67\\%, \\quad \\frac{U_{\\text{outside}}}{U_{\\text{total}}} = \\frac{5}{6} \\approx 83.33\\%$$",
                "explanation": "Exactly 5/6 (83.3%) of the electrostatic energy resides in the surrounding space outside the sphere!"
            }
        ]
    },
    {
        "id": "prob-2-2-b",
        "difficulty": "Experimental Accelerator Exam Standard",
        "title": "Van de Graaff Generator Maximum Operating Limits",
        "question": "A Van de Graaff electrostatic generator has a spherical high-voltage terminal of radius $R = 85.0\\text{ cm}$. The surrounding atmospheric air has a dielectric breakdown strength of $E_b = 3.00 \\times 10^6\\text{ V/m}$.\\n(a) Calculate the maximum electrical charge $Q_{\\max}$ that can be maintained on the terminal,\\n(b) Find the maximum electrical potential $V_{\\max}$ of the terminal relative to ground, and\\n(c) If the charging belt transports a continuous charging current $I = 150\\ \\mu\\text{A}$, what is the minimum power required to maintain the generator at full potential against leakage?",
        "steps": [
            {
                "title": "Step 1: Compute maximum charge before dielectric breakdown",
                "math": "$$E_{\\max} = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q_{\\max}}{R^2} = E_b$$\n$$Q_{\\max} = 4\\pi \\epsilon_0 R^2 E_b = \\frac{(0.850)^2 \\times (3.00 \\times 10^6)}{8.988 \\times 10^9} = \\frac{0.7225 \\times 3.00 \\times 10^6}{8.988 \\times 10^9} = \\frac{2.1675 \\times 10^6}{8.988 \\times 10^9} = 2.411 \\times 10^{-4} \\text{ C} = 241 \\ \\mu\\text{C}$$",
                "explanation": "Air breaks down into spark discharges if the charge exceeds 241 microCoulombs."
            },
            {
                "title": "Step 2: Maximum terminal voltage",
                "math": "$$V_{\\max} = R E_b = 0.850 \\text{ m} \\times (3.00 \\times 10^6 \\text{ V/m}) = 2.55 \\times 10^6 \\text{ Volts} = 2.55 \\text{ Megavolts (MV)}$$",
                "explanation": "The maximum terminal voltage is directly the product of dome radius and breakdown electric field."
            },
            {
                "title": "Step 3: Mechanical power required to drive belt",
                "math": "$$P = V_{\\max} I = (2.55 \\times 10^6 \\text{ V}) \\times (150 \\times 10^{-6} \\text{ A}) = 382.5 \\text{ Watts}$$",
                "explanation": "The motor driving the belt must deliver at least 383 Watts of mechanical power to overcome electrostatic repulsion."
            }
        ]
    }
]

unit2_data = {
    "number": 2,
    "title": "Electric Potential",
    "leadSummary": "Conservative nature of electrostatic fields, scalar electric potential, line integrals, potential of point charges, dipoles, and continuous charge distributions, negative gradient theorem E = -grad V, equipotential surfaces, conductor electrostatics, Faraday cages, and Van de Graaff high-voltage physics.",
    "sections": u2_sections,
    "problems": u2_problems
}

with open("em_u2.json", "w") as f:
    json.dump(unit2_data, f, indent=2)

print("Unit 2 built successfully with", len(u2_sections), "sections and", len(u2_problems), "problems!")
