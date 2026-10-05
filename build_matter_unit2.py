# Build Script for Unit 2: Elasticity
import json

u2_sections = [
    {
        "id": "sec-2-1",
        "number": "§2.1",
        "heading": "Stress, Plane Stress, and Tensor Transformations",
        "simulation": "hooke-stress-strain-sim",
        "content": """When an external deforming force acts upon a deformable solid body, the atoms are displaced from their microscopic equilibrium lattice positions, setting up internal restoring forces that resist deformation.

<h4>1. Definition of Stress</h4>
**Stress** ($\\sigma$ or $\\tau$) is defined as the internal restoring force developed per unit area of the deformed cross section:
$$\\boldsymbol{\\sigma} = \\lim_{\\Delta A \\to 0} \\frac{\\Delta \\mathbf{F}}{\\Delta A}$$
In SI units, stress is measured in Pascals ($1\\text{ Pa} = 1\\text{ N/m}^2$) or megapascals ($1\\text{ MPa} = 10^6\\text{ Pa}$).
<ul>
  <li><strong>Normal Stress ($\\sigma$):</strong> Restoring force acts perpendicular to the cross-sectional area. Tensile stress elongates the material ($\sigma > 0$), while compressive stress shortens it ($\sigma < 0$).</li>
  <li><strong>Shear (Tangential) Stress ($\\tau$):</strong> Restoring force acts parallel (tangential) to the surface plane, sliding adjacent atomic layers past one another.</li>
</ul>

<h4>2. The State of Plane Stress</h4>
A solid element is in a state of **plane stress** when all stress vectors acting on one coordinate plane vanish identically: $\\sigma_{zz} = \\tau_{xz} = \\tau_{yz} = 0$.
The stress state is completely characterized by the 2D stress tensor:
$$\\boldsymbol{\\sigma}_{2D} = \\begin{pmatrix} \\sigma_{xx} & \\tau_{xy} \\\\ \\tau_{xy} & \\sigma_{yy} \\end{pmatrix}$$
where $\\tau_{xy} = \\tau_{yx}$ by the conservation of angular momentum (complementary shear stresses).

<h4>3. Mohr's Circle and Principal Stresses</h4>
Under a coordinate rotation by angle $\\theta$, the normal and shear stresses transform as:
$$\\sigma_{\\theta} = \\frac{\\sigma_{xx} + \\sigma_{yy}}{2} + \\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\cos(2\\theta) + \\tau_{xy}\\sin(2\\theta)$$
$$\\tau_{\\theta} = -\\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\sin(2\\theta) + \\tau_{xy}\\cos(2\\theta)$$
The maximum and minimum normal stresses are the **Principal Stresses** (where shear stress $\\tau = 0$):
$$\\sigma_{1, 2} = \\frac{\\sigma_{xx} + \\sigma_{yy}}{2} \\pm \\sqrt{\\left(\\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\right)^2 + \\tau_{xy}^2}$$
Examples of plane stress include thin-walled pressure vessels, aircraft skins, and surface beams under pure bending."""
    },
    {
        "id": "sec-2-2",
        "number": "§2.2",
        "heading": "Strain and Hydrostatic Pressure",
        "simulation": "hooke-stress-strain-sim",
        "content": """**Strain** is the fractional geometric deformation produced in a body under applied stress. Because strain is a ratio of identical physical dimensions, it is a dimensionless quantity.

<h4>1. The Three Primary Types of Strain</h4>
<ol>
  <li><strong>Longitudinal (Tensile) Strain:</strong> The fractional change in length:
  $$\\epsilon = \\frac{\\Delta L}{L}$$
  </li>
  <li><strong>Shearing Strain ($\\theta$):</strong> The angular distortion (in radians) between two lines initially perpendicular to each other in the unstrained state:
  $$\\theta = \\frac{\\Delta x}{L} \\approx \\tan\\theta$$
  </li>
  <li><strong>Volumetric Strain ($\\theta_v$):</strong> The fractional change in volume:
  $$\\theta_v = \\frac{\\Delta V}{V}$$
  </li>
</ol>

<h4>2. Hydrostatic Pressure</h4>
When a solid is submerged in a fluid, it experiences uniform normal compressive stress on every surface element with zero shear stress:
$$\\sigma_{xx} = \\sigma_{yy} = \\sigma_{zz} = -P, \\quad \\tau_{xy} = \\tau_{yz} = \\tau_{zx} = 0$$
The body undergoes pure volumetric compression without any change in shape:
$$\\frac{\\Delta V}{V} = -\\frac{P}{K}$$
where $K$ is the bulk modulus."""
    },
    {
        "id": "sec-2-3",
        "number": "§2.3",
        "heading": "Hooke's Law and the Complete Stress-Strain Diagram",
        "simulation": "hooke-stress-strain-sim",
        "content": """Robert Hooke (1676) discovered the fundamental law of elasticity: *Ut tensio, sic vis* (*as the extension, so the force*).

<h4>1. Hooke's Law</h4>
Within the elastic limit of a material, stress is directly proportional to strain:
$$\\text{Stress} \\propto \\text{Strain} \\implies \\sigma = E \\, \\epsilon$$
where the constant of proportionality $E$ is the **Modulus of Elasticity**.

<h4>2. Detailed Analysis of the Engineering Stress-Strain Curve</h4>
For a ductile material like mild structural steel subjected to tensile testing:
<ul>
  <li><strong>Region OA (Proportional Limit $\sigma_p$):</strong> Stress is strictly linear with strain. Hooke's law is valid. Slope $d\sigma/d\epsilon = Y$ gives Young's modulus.</li>
  <li><strong>Point B (Elastic Limit / Yield Point $\sigma_y$):</strong> The maximum stress to which the material can be subjected without incurring permanent plastic deformation upon release.</li>
  <li><strong>Region BC (Plastic Flow & Strain Hardening):</strong> Beyond the yield point, atomic planes slip along crystallographic planes (dislocation movement). Permanent deformation (**plastic strain**) remains upon unloading.</li>
  <li><strong>Point D (Ultimate Tensile Strength $\sigma_{\text{UTS}}$):</strong> The maximum engineering stress the material can sustain. Beyond this point, macroscopic localized cross-sectional narrowing (**necking**) occurs.</li>
  <li><strong>Point E (Fracture Point $\sigma_f$):</strong> The specimen tears apart into two pieces.</li>
</ul>

<h4>3. Ductile versus Brittle Materials</h4>
<ul>
  <li><strong>Ductile Materials (Mild Steel, Copper, Aluminum):</strong> Large plastic deformation between yield point and fracture ($> 5\\%$ strain). Can be drawn into thin wires or hammered into sheets.</li>
  <li><strong>Brittle Materials (Glass, Cast Iron, Ceramics, Concrete):</strong> Fracture occurs immediately at or slightly beyond the elastic limit with virtually zero plastic deformation. High compressive strength but poor tensile tolerance.</li>
</ul>"""
    },
    {
        "id": "sec-2-4",
        "number": "§2.4",
        "heading": "Elastic Hysteresis and Internal Friction",
        "simulation": "hooke-stress-strain-sim",
        "content": """In ideal elasticity, loading and unloading follow the exact same path. In real materials, internal atomic friction causes the unloading stress-strain curve to lag behind the loading curve.

<h4>1. The Elastic Hysteresis Loop</h4>
When a material (such as vulcanized rubber) is stretched and then allowed to relax, the strain during unloading is greater than during loading at the identical stress level.
The closed loop formed by the loading and unloading curves in the $(\\sigma, \\epsilon)$ plane is the **Elastic Hysteresis Loop**.

<h4>2. Energy Dissipation as Heat</h4>
The work done per unit volume during loading is:
$$w_{\\text{load}} = \\int_0^{\\epsilon_{\\max}} \\sigma_{\\text{load}} \\, d\\epsilon$$
The elastic work recovered per unit volume during unloading is:
$$w_{\\text{unload}} = \\int_{\\epsilon_{\\max}}^0 \\sigma_{\\text{unload}} \\, d\\epsilon$$
The net energy dissipated per unit volume per cycle is the area enclosed by the loop:
$$\\Delta U_{\\text{dissipated}} = \\oint \\sigma \\, d\\epsilon = \\text{Area of Hysteresis Loop}$$
This mechanical energy is converted irreversibly into internal thermal heat.

<h4>3. Engineering Applications</h4>
<ul>
  <li><strong>High Hysteresis Materials (Rubber, Elastomers):</strong> Used in automobile tires, engine vibration isolators, and earthquake building dampeners because they rapidly dissipate kinetic shocks into heat.</li>
  <li><strong>Low Hysteresis Materials (Quartz, Phosphor Bronze):</strong> Used for suspension strips in precision galvanometers, gravimeters, and mechanical watch balance springs to avoid energy loss and drift.</li>
</ul>"""
    },
    {
        "id": "sec-2-5",
        "number": "§2.5",
        "heading": "The Four Elastic Moduli and Poisson's Ratio",
        "simulation": "hooke-stress-strain-sim",
        "content": """Homogeneous and isotropic materials possess four foundational elastic constants that characterize their response to tension, pressure, shear, and transverse deformation.

<h4>1. Young's Modulus ($Y$)</h4>
Defined as the ratio of tensile (or compressive) longitudinal stress to longitudinal strain:
$$Y = \\frac{\\sigma}{\\epsilon} = \\frac{F / A}{\\Delta L / L} = \\frac{F L}{A \\Delta L}$$
Typical values: Steel ($Y \\approx 200\\text{ GPa}$), Copper ($Y \\approx 110\\text{ GPa}$), Glass ($Y \\approx 70\\text{ GPa}$).

<h4>2. Bulk Modulus ($K$)</h4>
Defined as the ratio of hydrostatic pressure stress to volumetric strain:
$$K = -\\frac{\\Delta P}{\\Delta V / V} = -V \\frac{dP}{dV}$$
The negative sign ensures $K > 0$ because an increase in pressure produces a decrease in volume.
The reciprocal of bulk modulus is the **Compressibility** $\\beta = 1/K$.

<h4>3. Shear Modulus / Modulus of Rigidity ($\eta$ or $G$)</h4>
Defined as the ratio of shear stress to shearing strain:
$$\\eta = \\frac{\\tau}{\\theta} = \\frac{F_t / A}{\\Delta x / L}$$
For most solid materials, shear modulus is roughly one-third of Young's modulus: $\\eta \\approx 0.35 Y$ to $0.40 Y$. Liquids and gases have zero static shear modulus ($\\eta = 0$) because they cannot resist static shear.

<h4>4. Poisson's Ratio ($\sigma$ or $\nu$)</h4>
When a rod is stretched longitudinally, it narrows laterally. Poisson's ratio is the ratio of lateral fractional contraction to longitudinal fractional elongation:
$$\\sigma = -\\frac{\\text{Lateral Strain}}{\\text{Longitudinal Strain}} = -\\frac{\\Delta d / d}{\\Delta L / L}$$
Because $\\Delta d < 0$ when $\\Delta L > 0$, the minus sign ensures $\\sigma > 0$ for conventional materials."""
    },
    {
        "id": "sec-2-6",
        "number": "§2.6",
        "heading": "Internal Elastic Strain Energy Density",
        "simulation": "hooke-stress-strain-sim",
        "content": """When external work deforms a solid elastically, the work is stored internally as **Elastic Potential Energy** (or strain energy) within the distorted interatomic electrostatic bonds.

<h4>1. Strain Energy in a Stretched Wire</h4>
Consider a wire of original length $L$ and cross-sectional area $A$. When elongated by $x$, the restoring force is $F(x) = \\frac{Y A}{L} x$.
The total work done to stretch the wire by final extension $\\Delta L$ is:
$$W = \\int_0^{\\Delta L} F(x) \\, dx = \\frac{Y A}{L} \\int_0^{\\Delta L} x \\, dx = \\frac{1}{2} \\frac{Y A}{L} (\\Delta L)^2 = \\frac{1}{2} F_{\\max} \\Delta L$$
<blockquote>
The stored elastic strain energy equals <strong>one-half</strong> the product of final stretching force and elongation:
$$U = \\frac{1}{2} F \\Delta L$$
</blockquote>

<h4>2. Strain Energy Density ($u$)</h4>
The strain energy per unit volume ($V = A L$) is:
$$u = \\frac{U}{A L} = \\frac{1}{2} \\left( \\frac{F}{A} \\right) \\left( \\frac{\\Delta L}{L} \\right) = \\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain}$$
Using Hooke's law $\\sigma = Y \\epsilon$:
$$u = \\frac{1}{2} Y \\epsilon^2 = \\frac{\\sigma^2}{2Y}$$

<h4>3. Energy Densities for Shear and Hydrostatic Compression</h4>
<ul>
  <li><strong>Under Pure Shear:</strong> $u_s = \\frac{1}{2} \\tau \\theta = \\frac{1}{2} \\eta \\theta^2 = \\frac{\\tau^2}{2\\eta}$</li>
  <li><strong>Under Hydrostatic Compression:</strong> $u_v = \\frac{1}{2} P \\left(-\\frac{\\Delta V}{V}\\right) = \\frac{1}{2} K \\theta_v^2 = \\frac{P^2}{2K}$</li>
</ul>"""
    },
    {
        "id": "sec-2-7",
        "number": "§2.7",
        "heading": "Relations Between Elastic Constants and Theoretical Limits of Poisson's Ratio",
        "simulation": "hooke-stress-strain-sim",
        "content": """For any isotropic, linear elastic solid, only **two** of the four elastic constants ($Y, K, \\eta, \\sigma$) are independent. The other two can be derived through geometry and mechanics.

<h4>1. Mathematical Derivations of the Interrelations</h4>
Consider a unit cube subjected to normal tensile stresses $\\sigma_x$ along $x$.
The resulting strains along each principal axis are:
$$\\epsilon_x = \\frac{\\sigma_x}{Y}, \\quad \\epsilon_y = -\\sigma \\frac{\\sigma_x}{Y}, \\quad \\epsilon_z = -\\sigma \\frac{\\sigma_x}{Y}$$
<ol>
  <li><strong>Relation between $Y, K$, and $\sigma$:</strong> Apply uniform hydrostatic pressure $\\sigma_x = \\sigma_y = \\sigma_z = -P$.
  The volumetric strain is $\\theta_v = \\epsilon_x + \\epsilon_y + \\epsilon_z = 3 \\epsilon_x = -3 \\frac{P}{Y}(1 - 2\\sigma)$.
  Since $K = -P / \\theta_v$:
  $$Y = 3K (1 - 2\\sigma)$$
  </li>
  <li><strong>Relation between $Y, \eta$, and $\sigma$:</strong> Apply equal and opposite tensile and compressive stresses $\\sigma_x = -\\sigma_y = \\sigma$.
  This stress state is pure shear $\\tau = \\sigma$ at $45^\\circ$, producing shear strain $\\theta = 2\\epsilon_x = \\frac{2\\sigma}{Y}(1 + \\sigma)$.
  Since $\\eta = \\tau / \\theta$:
  $$Y = 2\\eta (1 + \\sigma)$$
  </li>
  <li><strong>Combined Relations:</strong> Equating expressions for $Y$:
  $$3K(1 - 2\\sigma) = 2\\eta(1 + \\sigma) \\implies \\sigma = \\frac{3K - 2\\eta}{6K + 2\\eta}$$
  Eliminating $\\sigma$ yields the harmonic relation:
  $$\\frac{9}{Y} = \\frac{3}{\\eta} + \\frac{1}{K}$$
  </li>
</ol>

<h4>2. Theoretical Limits of Poisson's Ratio</h4>
Because physical materials require positive strain energy under any deformation:
$$K > 0 \\implies 1 - 2\\sigma > 0 \\implies \\sigma < \\frac{1}{2}$$
$$\\eta > 0 \\implies 1 + \\sigma > 0 \\implies \\sigma > -1$$
<blockquote>
<strong>Theoretical Range of Poisson's Ratio:</strong>
$$-1 \\le \\sigma \\le +0.5$$
</blockquote>
<ul>
  <li><strong>Incompressible Materials ($\sigma = 0.5$):</strong> Volume does not change under stress ($\Delta V = 0 \implies K \to \infty$). Examples: Rubber, water.</li>
  <li><strong>Typical Metals ($\sigma \\approx 0.25 - 0.35$):</strong> Volume expands under tension. Steel ($\sigma = 0.29$), Aluminum ($\sigma = 0.33$).</li>
  <li><strong>Cork ($\sigma \\approx 0$):</strong> Lateral dimension does not change when compressed (why wine bottle corks can be pushed in easily!).</li>
  <li><strong>Auxetic Materials ($\\sigma < 0$):</strong> Expand laterally when stretched. Synthetic cellular foam polymers, biological tendon tissues.</li>
</ul>"""
    },
    {
        "id": "sec-2-8",
        "number": "§2.8",
        "heading": "Torsion of a Cylinder and Torsional Pendulum",
        "simulation": "cantilever-bending-sim",
        "content": """When a torque is applied to one end of a solid cylinder or wire while the opposite end is clamped, the cylinder is subjected to **pure torsional shear**.

<h4>1. Angle of Twist and Shear Strain</h4>
Consider a solid cylinder of radius $R$ and length $L$, fixed at one end. A torque $\\tau$ applied to the free end twists it through an **angle of twist** $\\theta$.
An element at distance $r$ from the central axis is displaced along the circumference by arc length $s = r\\theta$.
The shear strain at radius $r$ is:
$$\\phi(r) = \\frac{s}{L} = \\frac{r\\theta}{L}$$
By Hooke's law, the shear stress developed at radius $r$ is:
$$\\tau(r) = \\eta \\, \\phi(r) = \\frac{\\eta r \\theta}{L}$$
Shear stress is zero at the central axis and reaches its maximum value $\\tau_{\\max} = \\frac{\\eta R \\theta}{L}$ at the outer perimeter.

<h4>2. Derivation of the Restoring Torsional Couple</h4>
Divide the cross section into thin concentric cylindrical shells of radius $r$ and thickness $dr$.
The area of a shell is $dA = 2\\pi r \\, dr$.
The shear force acting on this shell is:
$$dF = \\tau(r) \\, dA = \\left( \\frac{\\eta r \\theta}{L} \\right) (2\\pi r \\, dr) = \\frac{2\\pi \\eta \\theta}{L} r^2 \\, dr$$
The torque about the cylinder axis produced by this shell is:
$$dC = r \\, dF = \\frac{2\\pi \\eta \\theta}{L} r^3 \\, dr$$
Integrating over the entire cross section from $r = 0$ to $r = R$:
$$C = \\frac{2\\pi \\eta \\theta}{L} \\int_0^R r^3 \\, dr = \\frac{2\\pi \\eta \\theta}{L} \\left( \\frac{R^4}{4} \\right) = \\frac{\\pi \\eta R^4}{2L} \\theta$$
The **Torsional Rigidity** (couple per unit angle of twist $c = C / \\theta$) is:
$$c = \\frac{\\pi \\eta R^4}{2L}$$
Notice the extreme sensitivity to radius ($c \\propto R^4$): doubling the wire thickness increases torsional stiffness by a factor of 16!

<h4>3. The Torsional Pendulum</h4>
A heavy disc of moment of inertia $I$ suspended from a wire of torsional rigidity $c$ oscillates according to:
$$I \\ddot{\\theta} + c \\theta = 0 \\implies T = 2\\pi \\sqrt{\\frac{I}{c}} = 2\\pi \\sqrt{\\frac{2 I L}{\\pi \\eta R^4}}$$
Measuring $T$ allows high-precision experimental determination of the shear modulus $\\eta$."""
    },
    {
        "id": "sec-2-9",
        "number": "§2.9",
        "heading": "Helical Coil Springs and Effective Mass Correction",
        "simulation": "cantilever-bending-sim",
        "content": """A helical coil spring behaves primarily not through tension or bending of the wire, but through pure **torsional twisting** of the coiled wire cross section!

<h4>1. Mechanics of Extension in a Helical Spring</h4>
Consider a closely coiled helical spring made of wire of circular cross section of radius $r$, having $N$ turns of mean coil radius $R$, subjected to an axial tensile load $W$.
At any cross section of the wire:
<ul>
  <li>The axial force $W$ produces a twisting torque of magnitude:
  $$\\tau = W R$$
  </li>
  <li>The total length of wire coiled into the spring is $L = 2\\pi R N$.</li>
</ul>
From the torsion formula, the angle of twist produced in the entire wire is:
$$\\theta = \\frac{\\tau L}{c} = \\frac{(W R)(2\\pi R N)}{\\frac{1}{2}\\pi \\eta r^4} = \\frac{4 W R^2 N}{\\eta r^4}$$
The downward axial extension of the spring is:
$$\\delta = R \\theta = \\frac{4 W R^3 N}{\\eta r^4}$$
The spring constant (stiffness) is:
$$k = \\frac{W}{\\delta} = \\frac{\\eta r^4}{4 R^3 N}$$

<h4>2. Dynamic Oscillation and Effective Spring Mass Correction</h4>
When a mass $M$ is attached to the spring and set into vertical oscillation, the coils of the spring itself also move.
A coil at fractional position $z/L$ from the fixed top oscillates with amplitude $\\frac{z}{L} v$.
The kinetic energy of the spring (of total mass $m_s$) is:
$$K_{\\text{spring}} = \\int_0^L \\frac{1}{2} \\left(\\frac{m_s}{L} dz\\right) \\left( \\frac{z}{L} v \\right)^2 = \\frac{1}{2} m_s v^2 \\frac{1}{L^3} \\int_0^L z^2 dz = \\frac{1}{6} m_s v^2 = \\frac{1}{2} \\left(\\frac{m_s}{3}\\right) v^2$$
The spring contributes exactly **one-third of its own mass** to the oscillating inertia:
$$M_{\\text{eff}} = M + \\frac{m_s}{3}$$
The exact period of oscillation is:
$$T = 2\\pi \\sqrt{\\frac{M + m_s / 3}{k}} = 2\\pi \\sqrt{\\frac{4 R^3 N (M + m_s / 3)}{\\eta r^4}}$$"""
    },
    {
        "id": "sec-2-10",
        "number": "§2.10",
        "heading": "Bending of Beams and Cantilevers",
        "simulation": "cantilever-bending-sim",
        "content": """A **beam** is a structural member whose length is large compared to its lateral cross-sectional dimensions, designed to carry transverse mechanical loads.

<h4>1. The Neutral Axis and Bending Moment</h4>
When a horizontal beam is bent into a curve of radius of curvature $R$ by transverse forces:
<ul>
  <li>Filaments on the convex side are stretched in tension.</li>
  <li>Filaments on the concave side are compressed.</li>
  <li>A central surface exists where filaments experience zero strain and zero stress. This is the **Neutral Surface**, and its intersection with any cross section is the **Neutral Axis**.</li>
</ul>
At distance $y$ from the neutral axis, strain is $\\epsilon = y / R$, and stress is $\\sigma = Y y / R$.
The resisting **Bending Moment** is:
$$M = \\int \\sigma y \\, dA = \\frac{Y}{R} \\int y^2 \\, dA = \\frac{Y I_g}{R}$$
where $I_g = \\int y^2 \\, dA$ is the **Geometric Moment of Inertia** of the cross section:
<ul>
  <li>For a rectangular beam of breadth $b$ and depth $d$: $I_g = \\frac{b d^3}{12}$</li>
  <li>For a circular beam of radius $r$: $I_g = \\frac{\\pi r^4}{4}$</li>
</ul>

<h4>2. The Cantilever Loaded at the Free End</h4>
A **cantilever** is a beam fixed horizontally at one end and loaded at the free end.
For a light cantilever of length $L$ loaded with weight $W$ at its free end:
At distance $x$ from the fixed support, the bending moment is $M(x) = W(L - x)$.
The differential equation of curvature is:
$$Y I_g \\frac{d^2 y}{dx^2} = W (L - x)$$
Integrating with boundary conditions $y(0) = 0$ and $y'(0) = 0$:
$$Y I_g \\frac{dy}{dx} = W \\left( L x - \\frac{x^2}{2} \\right)$$
$$Y I_g y(x) = W \\left( \\frac{L x^2}{2} - \\frac{x^3}{6} \\right)$$
At the free end ($x = L$), the maximum depression is:
$$\\delta = \\frac{W L^3}{3 Y I_g} = \\frac{4 W L^3}{Y b d^3}$$
Notice that depression is inversely proportional to the cube of depth ($d^3$), explaining why engineering I-beams are oriented with their maximum depth vertically!"""
    }
]

u2_problems = [
    {
        "id": "prob-2-1",
        "difficulty": "Medium",
        "title": "Young's Modulus and Strain Energy of a Steel Suspension Cable",
        "question": "A vertical steel elevator cable of length $L = 50.0\\text{ m}$ and cross-sectional area $A = 4.00\\text{ cm}^2$ supports an elevator cabin of mass $M = 2,500\\text{ kg}$. (Young's modulus of steel $Y = 2.00 \\times 10^{11}\\text{ Pa}$). (a) Calculate the tensile stress and the total elongation $\\Delta L$ of the cable under static load. (b) Calculate the total elastic strain energy stored in the cable.",
        "steps": [
            {
                "title": "Step 1: Compute tensile stress in the cable",
                "math": "$$F = M g = (2,500\\text{ kg})(9.81\\text{ m/s}^2) = 24,525\\text{ N}$$\n$$A = 4.00\\text{ cm}^2 = 4.00 \\times 10^{-4}\\text{ m}^2$$\n$$\\sigma = \\frac{F}{A} = \\frac{24,525\\text{ N}}{4.00 \\times 10^{-4}\\text{ m}^2} = 6.131 \\times 10^7\\text{ Pa} = 61.31\\text{ MPa}$$",
                "explanation": "This is well below the yield strength of structural steel (~250 MPa)."
            },
            {
                "title": "Step 2: Calculate total elongation",
                "math": "$$\\Delta L = \\frac{F L}{A Y} = \\frac{\\sigma L}{Y} = \\frac{(6.131 \\times 10^7\\text{ Pa})(50.0\\text{ m})}{2.00 \\times 10^{11}\\text{ Pa}} = 1.533 \\times 10^{-2}\\text{ m} = 15.33\\text{ mm}$$",
                "explanation": "The 50-meter cable stretches by approximately 1.53 centimeters."
            },
            {
                "title": "Step 3: Calculate elastic strain energy",
                "math": "$$U = \\frac{1}{2} F \\Delta L = \\frac{1}{2} (24,525\\text{ N})(0.01533\\text{ m}) = 188.0\\text{ Joules}$$",
                "explanation": "The total stored strain energy is 188 J."
            }
        ]
    },
    {
        "id": "prob-2-2",
        "difficulty": "Hard",
        "title": "Determination of Poisson's Ratio from Volume Change",
        "question": "A cylindrical copper rod of initial length $L_0 = 1.00\\text{ m}$ and initial diameter $d_0 = 2.00\\text{ cm}$ is subjected to an axial tensile force that stretches it by $\\Delta L = 2.00\\text{ mm}$. If the total volume of the rod increases by $\\Delta V = 2.01 \\times 10^{-7}\\text{ m}^3$, calculate Poisson's ratio $\\sigma$ for copper.",
        "steps": [
            {
                "title": "Step 1: Express volumetric strain in terms of longitudinal and lateral strain",
                "math": "$$V = \\frac{\\pi}{4} d^2 L$$\n$$\\frac{\\Delta V}{V} = 2 \\frac{\\Delta d}{d} + \\frac{\\Delta L}{L} = -2 \\sigma \\epsilon_L + \\epsilon_L = \\epsilon_L (1 - 2\\sigma)$$",
                "explanation": "This establishes the fundamental link between fractional volume change and Poisson's ratio."
            },
            {
                "title": "Step 2: Calculate initial volume and longitudinal strain",
                "math": "$$V_0 = \\frac{\\pi}{4} (0.02\\text{ m})^2 (1.00\\text{ m}) = 3.1416 \\times 10^{-4}\\text{ m}^3$$\n$$\\epsilon_L = \\frac{\\Delta L}{L_0} = \\frac{0.002\\text{ m}}{1.00\\text{ m}} = 2.00 \\times 10^{-3}$$\n$$\\frac{\\Delta V}{V_0} = \\frac{2.01 \\times 10^{-7}\\text{ m}^3}{3.1416 \\times 10^{-4}\\text{ m}^3} = 6.398 \\times 10^{-4}$$",
                "explanation": "These are the measured strains."
            },
            {
                "title": "Step 3: Solve for Poisson's ratio sigma",
                "math": "$$1 - 2\\sigma = \\frac{\\Delta V / V_0}{\\epsilon_L} = \\frac{6.398 \\times 10^{-4}}{2.00 \\times 10^{-3}} = 0.3199$$\n$$2\\sigma = 1 - 0.3199 = 0.6801 \\implies \\sigma = 0.340$$",
                "explanation": "Poisson's ratio for copper is $\\sigma = 0.34$, which perfectly matches standard engineering tables."
            }
        ]
    },
    {
        "id": "prob-2-3",
        "difficulty": "Hard",
        "title": "Deflection and Bending of a Rectangular Cantilever",
        "question": "A steel cantilever ruler of length $L = 1.00\\text{ m}$, breadth $b = 3.00\\text{ cm}$, and thickness $d = 4.00\\text{ mm}$ is clamped horizontally at one end. A load of mass $M = 500\\text{ g}$ is suspended at its free end. (Young's modulus $Y = 2.10 \\times 10^{11}\\text{ Pa}$). (a) Compute the geometric moment of inertia $I_g$. (b) Calculate the depression $\\delta$ at the loaded free end.",
        "steps": [
            {
                "title": "Step 1: Compute geometric moment of inertia for rectangular cross section",
                "math": "$$b = 0.030\\text{ m}, \\quad d = 0.0040\\text{ m}$$\n$$I_g = \\frac{b d^3}{12} = \\frac{(0.030\\text{ m})(0.0040\\text{ m})^3}{12} = \\frac{(0.030)(6.40 \\times 10^{-8})}{12} = 1.60 \\times 10^{-10}\\text{ m}^4$$",
                "explanation": "This is the second moment of area about the neutral axis."
            },
            {
                "title": "Step 2: Calculate downward load force",
                "math": "$$W = M g = (0.500\\text{ kg})(9.81\\text{ m/s}^2) = 4.905\\text{ N}$$",
                "explanation": "This is the point load acting at the free end."
            },
            {
                "title": "Step 3: Calculate end depression delta",
                "math": "$$\\delta = \\frac{W L^3}{3 Y I_g} = \\frac{(4.905\\text{ N})(1.00\\text{ m})^3}{3 (2.10 \\times 10^{11}\\text{ Pa})(1.60 \\times 10^{-10}\\text{ m}^4)}$$\n$$\\delta = \\frac{4.905}{100.8} = 0.04866\\text{ m} = 4.87\\text{ cm}$$",
                "explanation": "The free tip of the cantilever deflects downward by $4.87\\text{ cm}$."
            }
        ]
    }
]

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/matter_u2.json', 'w') as f:
    json.dump({"number": 2, "title": "Elasticity and Mechanical Properties of Solids", "leadSummary": "Stress-strain tensors, plane stress, Hooke's law, elastic moduli, Poisson's ratio limits, strain energy, torsion of cylinders, coil springs, beam bending, and cantilevers.", "sections": u2_sections, "problems": u2_problems}, f, indent=2)

print("Unit 2 built successfully with 10 sections and 3 solved problems!")
