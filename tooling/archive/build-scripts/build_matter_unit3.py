# Build Script for Units 3 and 4: Properties of Matter & Waves
import json

# =========================================================================
# UNIT 3: Hydrostatics and Surface Tension
# =========================================================================
u3_sections = [
    {
        "id": "sec-3-1",
        "number": "§3.1",
        "heading": "Hydrostatic Pressure and Variation with Elevation",
        "simulation": "capillary-bubble-sim",
        "content": """Hydrostatics studies fluids at rest. A fluid cannot sustain static shear stress; therefore, any force exerted by a static fluid on an adjacent boundary must act strictly normal to the surface.

<h4>1. The Concept of Hydrostatic Pressure</h4>
Pressure $P$ at a point within a fluid is defined as the normal compressive force per unit area:
$$P = \\lim_{\\Delta A \\to 0} \\frac{\\Delta F_\\perp}{\\Delta A}$$
Pressure is a scalar quantity, acting equally in all spatial directions at a given point.

<h4>2. Variation of Pressure with Elevation</h4>
Consider an infinitesimal cylindrical fluid element of cross-sectional area $A$ and height $dz$ in static equilibrium under gravity:
The vertical force balance is:
$$P(z) A - P(z + dz) A - dm \\, g = 0$$
Since $dm = \\rho A \\, dz$:
$$-dP \\, A - \\rho g A \\, dz = 0 \\implies \\frac{dP}{dz} = -\\rho g$$
This is the **Fundamental Equation of Hydrostatics**:
<ul>
  <li><strong>Incompressible Liquids ($\rho = \text{constant}$):</strong> Integrating from surface $z = h$ to depth $z = 0$:
  $$P(h) = P_0 + \\rho g h$$
  where $P_0$ is surface atmospheric pressure. Pressure increases linearly with depth $h$.</li>
  <li><strong>Compressible Isothermal Ideal Gas ($P = \rho \frac{R T}{M}$):</strong>
  $$\\frac{dP}{dz} = -\\frac{M g}{R T} P \\implies P(z) = P_0 \\exp\\left( -\\frac{M g z}{R T} \\right)$$
  This is the classical **Barometric Height Formula** for atmospheric pressure.</li>
</ul>"""
    },
    {
        "id": "sec-3-2",
        "number": "§3.2",
        "heading": "Pascal's Law and the Hydrostatic Paradox",
        "simulation": "capillary-bubble-sim",
        "content": """Blaise Pascal (1653) established the foundational transmission law for fluids.

<h4>1. Pascal's Law</h4>
<blockquote>
Pressure applied to any point of an enclosed, incompressible fluid at rest is transmitted completely undiminished to every portion of the fluid and to the walls of the containing vessel.
</blockquote>
<strong>The Hydraulic Press:</strong>
Consider two fluid cylinders with cross-sectional areas $A_1$ and $A_2$ connected by a pipe.
A downward force $F_1$ on piston 1 produces pressure $P = F_1 / A_1$.
By Pascal's law, this identical pressure acts on piston 2, producing upward force:
$$F_2 = P A_2 = F_1 \\left( \\frac{A_2}{A_1} \\right)$$
The mechanical advantage is $F_2 / F_1 = A_2 / A_1$.
Work is conserved: $F_1 d_1 = F_2 d_2$.

<h4>2. The Hydrostatic Paradox</h4>
Consider three vessels of completely different shapes (e.g., conical, cylindrical, flared) having identical base areas $A$ and filled with liquid to the exact same vertical depth $h$.
Although the vessels contain vastly different total weights of liquid, the downward force on the bottom of all three vessels is identical:
$$F = P A = (\\rho g h) A$$
The discrepancy is resolved by recognizing that the inclined walls of the flared vessel exert an upward normal force supporting the extra liquid weight, while the walls of the conical vessel exert downward thrust on the fluid."""
    },
    {
        "id": "sec-3-3",
        "number": "§3.3",
        "heading": "Hydrostatic Thrust on Immersed Surfaces and Center of Pressure",
        "simulation": "capillary-bubble-sim",
        "content": """Engineers designing dams, submarine hulls, and floodgates must calculate not only the total hydrostatic force, but also its exact point of application.

<h4>1. Total Hydrostatic Thrust on a Submerged Plane</h4>
Consider a plane surface of area $A$ immersed in a liquid of density $\\rho$ at angle $\\theta$ to the horizontal.
The hydrostatic thrust on an infinitesimal strip of area $dA$ at depth $h$ is $dF = P dA = (\\rho g h) dA$.
The total thrust is:
$$F = \\int_A \\rho g h \\, dA = \\rho g \\int_A h \\, dA = \\rho g \\bar{h} A = P_{\\text{cg}} A$$
where $\\bar{h}$ is the vertical depth of the **Center of Gravity (CG)** of the area.
The total thrust equals the area multiplied by the pressure at its centroid.

<h4>2. The Center of Pressure ($h_{\\text{cp}}$)</h4>
The **Center of Pressure (CP)** is the point on the surface where the single resultant force $F$ acts without producing any net rotational moment.
Taking moments about the surface waterline axis:
$$F \\, y_{\\text{cp}} = \\int_A y \\, dF = \\int_A y (\\rho g y \\sin\\theta) dA = \\rho g \\sin\\theta \\int_A y^2 dA = \\rho g \\sin\\theta \\, I_{xx,0}$$
where $I_{xx,0} = I_{\\text{cg}} + A \\bar{y}^2$ is the second moment of area by the parallel axis theorem.
Dividing by $F = \\rho g \\sin\\theta \\bar{y} A$:
$$y_{\\text{cp}} = \\bar{y} + \\frac{I_{\\text{cg}}}{\\bar{y} A} \\implies h_{\\text{cp}} = \\bar{h} + \\frac{I_{\\text{cg}} \\sin^2\\theta}{\\bar{h} A}$$
<blockquote>
Because $I_{\\text{cg}} > 0$, the Center of Pressure is <strong>always located strictly below</strong> the Center of Gravity!
</blockquote>

<h4>3. Force and Overturning Moment on a Vertical Dam</h4>
For a vertical rectangular dam of width $W$ holding water of depth $H$:
$$F = \\rho g \\left(\\frac{H}{2}\\right) (W H) = \\frac{1}{2} \\rho g W H^2$$
The center of pressure is located at:
$$h_{\\text{cp}} = \\frac{H}{2} + \\frac{\\frac{1}{12} W H^3}{(H/2)(W H)} = \\frac{H}{2} + \\frac{H}{6} = \\frac{2}{3} H$$
The resultant thrust acts at one-third of the height from the bottom ($H/3$), generating an overturning moment $M = F (H/3) = \\frac{1}{6}\\rho g W H^3$."""
    },
    {
        "id": "sec-3-4",
        "number": "§3.4",
        "heading": "Equilibrium of Floating Bodies and Metacentric Stability",
        "simulation": "capillary-bubble-sim",
        "content": """Archimedes of Syracuse (250 BCE) established the fundamental principle of flotation:

<h4>1. Archimedes' Principle</h4>
A body wholly or partially submerged in a fluid experiences an upward buoyant force $F_b$ equal to the weight of the displaced fluid:
$$F_b = \\rho_f V_{\\text{disp}} g$$
The buoyant force acts vertically upward through the **Center of Buoyancy ($B$)**, which is the centroid of the displaced fluid volume.

<h4>2. Flotation Equilibrium</h4>
For a floating body of mass $M$ and total volume $V$:
$$F_b = M g \\implies \\rho_f V_{\\text{disp}} g = \\rho_{\\text{body}} V g \\implies \\frac{V_{\\text{disp}}}{V} = \\frac{\\rho_{\\text{body}}}{\\rho_f}$$

<h4>3. Rotational Stability of Ships: The Metacenter ($M$)</h4>
When a floating vessel tilts through a small heel angle $\\theta$:
<ul>
  <li>The center of gravity $G$ of the ship remains fixed.</li>
  <li>The submerged geometry changes, shifting the center of buoyancy from $B$ to a new position $B'$.</li>
  <li>The vertical line of action of the buoyant force through $B'$ intersects the original vertical center line at point $M$, termed the **Metacenter**.</li>
</ul>
The distance $GM$ is the **Metacentric Height**:
$$GM = BM - BG = \\frac{I_{\\text{waterline}}}{V_{\\text{disp}}} - BG$$
where $I_{\\text{waterline}}$ is the second moment of area of the ship's waterline plane.
<ul>
  <li><strong>Stable Equilibrium ($GM > 0$):</strong> $M$ lies above $G$. The buoyant force and gravity form a restoring righting couple $\\tau = M g (GM)\\sin\\theta$ that rights the ship.</li>
  <li><strong>Unstable Equilibrium ($GM < 0$):</strong> $M$ lies below $G$. The couple capsizes the ship!</li>
  <li><strong>Neutral Equilibrium ($GM = 0$):</strong> $M$ coincides with $G$.</li>
</ul>"""
    },
    {
        "id": "sec-3-5",
        "number": "§3.5",
        "heading": "Pressure Gauges: Manometers and Barometers",
        "simulation": "capillary-bubble-sim",
        "content": """Hydrostatic pressure measurement relies on fluid column balancing.

<h4>1. The Open U-Tube Manometer</h4>
Used to measure gauge pressure of a gas container relative to atmosphere.
A U-tube contains a liquid of density $\\rho$. The difference in fluid column heights $h$ is:
$$P_{\\text{gas}} - P_{\\text{atm}} = \\rho g h$$

<h4>2. Differential Manometers</h4>
Used to measure the small pressure drop $\\Delta P = P_1 - P_2$ between two points in a pipeline:
$$P_1 - P_2 = (\\rho_m - \\rho_f) g h$$
where $\\rho_m$ is the manometer liquid density and $\\rho_f$ is the flowing fluid density.

<h4>3. The Mercury Barometer</h4>
Evangelista Torricelli (1643) invented the mercury barometer by filling a 1-meter tube with mercury and inverting it into a mercury basin.
The vacuum above the mercury column (Torricellian vacuum) has $P \\approx 0$.
Atmospheric pressure balances the mercury column:
$$P_{\\text{atm}} = \\rho_{\\text{Hg}} g h$$
Standard atmospheric pressure:
$$1\\text{ atm} = 760\\text{ mmHg} = (13,595\\text{ kg/m}^3)(9.80665\\text{ m/s}^2)(0.760\\text{ m}) = 101,325\\text{ Pa} = 1.01325\\text{ bar}$$"""
    },
    {
        "id": "sec-3-6",
        "number": "§3.6",
        "heading": "Surface Tension and Surface Free Energy",
        "simulation": "capillary-bubble-sim",
        "content": """Liquids behave as if their free surface were covered by a stretched elastic membrane under tension.

<h4>1. Microscopic Molecular Origin</h4>
In the bulk of a liquid, each molecule experiences isotropic cohesive attraction from neighboring molecules in all directions, yielding zero net force.
However, a molecule at the liquid-gas surface experiences strong downward cohesive attraction toward the liquid, but negligible attraction from vapor molecules above.
To bring a molecule from the interior to the surface requires doing positive mechanical work against this inward cohesive pull.
The surface of a liquid therefore possesses excess potential energy called **Surface Free Energy**.

<h4>2. Mechanical Definition of Surface Tension</h4>
**Surface Tension** ($\\gamma$ or $T$) is defined mechanically as the tangential tensile force acting perpendicularly across an imaginary line of unit length drawn in the liquid surface:
$$\\gamma = \\frac{F}{L}$$
In SI units, surface tension is measured in Newtons per meter ($\\text{N/m}$) or Joules per square meter ($\\text{J/m}^2$).
For pure water at $20^\\circ\\text{C}$: $\\gamma = 0.0728\\text{ N/m}$. For mercury: $\\gamma = 0.486\\text{ N/m}$.

<h4>3. Thermodynamic Equivalence</h4>
The work done to expand the surface area by $dA$ at constant temperature and composition is:
$$dW = \\gamma \\, dA \\implies \\gamma = \\left(\\frac{\\partial F}{\\partial A}\\right)_{T, V}$$
Because physical systems spontaneously minimize their free energy, liquids naturally contract to minimize their surface area, forming spherical droplets!"""
    },
    {
        "id": "sec-3-7",
        "number": "§3.7",
        "heading": "Pressure Difference Across a Curved Surface: Young-Laplace Equation",
        "simulation": "capillary-bubble-sim",
        "content": """Because a curved liquid surface is under tension, the pressure on the concave side of the interface must always be greater than the pressure on the convex side.

<h4>1. Excess Pressure Inside a Spherical Liquid Droplet</h4>
Consider a spherical liquid droplet of radius $R$ and surface tension $\\gamma$.
Let the internal pressure exceed external atmospheric pressure by $\\Delta P$.
Imagine dividing the droplet into two hemispheres:
The outward force attempting to separate the hemispheres across the diametral plane is:
$$F_{\\text{pressure}} = \\Delta P \\times (\\pi R^2)$$
This force is balanced by the surface tension acting along the circular perimeter:
$$F_{\\text{tension}} = \\gamma \\times (2\\pi R)$$
In equilibrium:
$$\\Delta P (\\pi R^2) = 2\\pi R \\gamma \\implies \\Delta P = \\frac{2\\gamma}{R}$$

<h4>2. Excess Pressure Inside a Soap Bubble</h4>
A soap bubble has **two** spherical liquid-gas interfaces (an inner surface and an outer surface):
$$\\Delta P = \\frac{4\\gamma}{R}$$
The excess pressure inside a bubble is inversely proportional to its radius ($P \\propto 1/R$).
Consequently, a small soap bubble has higher internal pressure than a large bubble: if connected by a tube, the small bubble blows its air into the large bubble and collapses!

<h4>3. The General Young-Laplace Equation</h4>
For an arbitrary curved interface characterized by principal orthogonal radii of curvature $R_1$ and $R_2$:
$$\\Delta P = \\gamma \\left( \\frac{1}{R_1} + \\frac{1}{R_2} \\right) = 2 \\gamma H$$
where $H = \\frac{1}{2}(1/R_1 + 1/R_2)$ is the **Mean Curvature** of the surface."""
    },
    {
        "id": "sec-3-8",
        "number": "§3.8",
        "heading": "Minimal Surfaces and Plateau's Laws",
        "simulation": "capillary-bubble-sim",
        "content": """In the absence of a pressure differential across the film ($\\Delta P = 0$), the Young-Laplace equation requires:
$$H = \\frac{1}{2}\\left( \\frac{1}{R_1} + \\frac{1}{R_2} \\right) = 0 \\implies \\frac{1}{R_1} = -\\frac{1}{R_2}$$
The mean curvature must be zero everywhere: the surface is a **Minimal Surface** (a saddle surface with equal and opposite principal curvatures).

<h4>1. Classic Minimal Surfaces</h4>
Joseph Plateau (1873) investigated soap films suspended on wire frames:
<ul>
  <li><strong>Catenoid:</strong> The surface of revolution formed by rotating a catenary ($y = c\\cosh(x/c)$) around an axis; the only minimal surface of revolution.</li>
  <li><strong>Helicoid:</strong> A screw-shaped minimal surface.</li>
</ul>

<h4>2. Plateau's Laws of Soap Films</h4>
Plateau formulated empirical geometric laws governing soap bubble foam clusters:
<ol>
  <li>Soap films consist of smooth surfaces of constant mean curvature.</li>
  <li>Exactly **three** soap film surfaces meet along a smooth line (called a *Plateau border*) at equal angles of strictly $120^\\circ$.</li>
  <li>Exactly **four** Plateau borders meet at a vertex at the tetrahedral angle:
  $$\\theta = \\arccos\\left(-\\frac{1}{3}\\right) \\approx 109.47^\\circ$$
  </li>
</ol>
Any other configuration is kinematically unstable and spontaneously rearranges to satisfy these angles."""
    },
    {
        "id": "sec-3-9",
        "number": "§3.9",
        "heading": "Angle of Contact and Capillarity: Jurin's Law",
        "simulation": "capillary-bubble-sim",
        "content": """When a liquid meets a solid boundary, the interface forms a characteristic **Angle of Contact** $\\theta_c$.

<h4>1. Young's Equation for Contact Angle</h4>
At the three-phase contact line where solid ($S$), liquid ($L$), and gas ($G$) meet, mechanical equilibrium requires balance of horizontal surface tension components:
$$\\gamma_{SG} = \\gamma_{SL} + \\gamma_{LG} \\cos\\theta_c \\implies \\cos\\theta_c = \\frac{\\gamma_{SG} - \\gamma_{SL}}{\\gamma_{LG}}$$
<ul>
  <li><strong>Wetting Liquid ($\theta_c < 90^\circ$):</strong> Adhesive force between liquid and solid exceeds liquid cohesive force. Concave meniscus (e.g., pure water on clean glass: $\theta_c \\approx 0^\circ$).</li>
  <li><strong>Non-Wetting Liquid ($\theta_c > 90^\circ$):</strong> Cohesion exceeds adhesion. Convex meniscus (e.g., mercury on glass: $\theta_c \\approx 138^\circ$).</li>
</ul>

<h4>2. Capillary Ascent: Jurin's Law (James Jurin, 1718)</h4>
When a narrow glass capillary tube of radius $r$ is immersed vertically in a wetting liquid:
The upward vertical component of surface tension acting along the inner circumference $2\\pi r$ is:
$$F_{\\text{up}} = 2\\pi r \\gamma \\cos\\theta_c$$
This lifts a column of liquid of height $h$ and mass $m = \\rho \\pi r^2 h$. The downward weight is:
$$W = m g = \\pi r^2 h \\rho g$$
Equating upward pull to downward weight:
$$2\\pi r \\gamma \\cos\\theta_c = \\pi r^2 h \\rho g \\implies h = \\frac{2\\gamma \\cos\\theta_c}{\\rho g r}$$
<blockquote>
<strong>Jurin's Law:</strong> The height of capillary rise is inversely proportional to tube radius:
$$h \\propto \\frac{1}{r}$$
</blockquote>
For a non-wetting liquid like mercury ($\cos\\theta_c < 0$), $h < 0$: the liquid is depressed below the external level."""
    },
    {
        "id": "sec-3-10",
        "number": "§3.10",
        "heading": "Experimental Determination of Surface Tension and Influencing Factors",
        "simulation": "capillary-bubble-sim",
        "content": """Various experimental techniques allow high-precision determination of $\\gamma$.

<h4>1. Experimental Methods</h4>
<ul>
  <li><strong>Capillary Rise Method:</strong> Direct application of Jurin's law: $\gamma = \frac{\rho g r h}{2 \cos\theta_c}$. Requires precision traveling microscope.</li>
  <li><strong>Jaeger's Maximum Bubble Pressure Method:</strong> A capillary tube of radius $r$ is dipped to depth $h_1$ in the liquid. Air pressure is slowly increased to blow a bubble. The maximum pressure occurs when the bubble is hemispherical with radius equal to tube radius $r$:
  $$P_{\max} = P_0 + \rho g h_1 + \frac{2\gamma}{r} \implies \gamma = \frac{r}{2}(P_{\max} - P_0 - \rho g h_1)$$
  Independent of contact angle $\theta_c$!</li>
  <li><strong>Rayleigh's Drop Weight Method:</strong> A liquid slowly drips from a tube of radius $r$. The weight $W$ of a detached droplet is:
  $$W = 2\pi r \gamma f$$
  where $f$ is Harkins-Brown correction factor ($f \approx 0.60 - 0.65$).</li>
</ul>

<h4>2. Factors Influencing Surface Tension</h4>
<ol>
  <li><strong>Temperature:</strong> Thermal kinetic agitation weakens intermolecular cohesive bonds, decreasing $\gamma$. According to the **Eötvös Rule**:
  $$\gamma V_m^{2/3} = k_E (T_c - T)$$
  Surface tension vanishes identically at the **Critical Temperature** $T_c$!</li>
  <li><strong>Surfactants (Soaps, Detergents):</strong> Amphiphilic molecules concentrate at the surface, dramatically lowering $\gamma$ from $73\text{ mN/m}$ to $\sim 25\text{ mN/m}$.</li>
  <li><strong>Dissolved Impurities:</strong> Highly soluble inorganic salts (NaCl) increase $\gamma$ slightly by attracting water molecules into the bulk.</li>
</ol>"""
    }
]

u3_problems = [
    {
        "id": "prob-3-1",
        "difficulty": "Medium",
        "title": "Capillary Ascent in a Glass Tube",
        "question": "A clean glass capillary tube of internal radius $r = 0.250\\text{ mm}$ is dipped vertically into pure water at $20^\\circ\\text{C}$ (density $\\rho = 1000\\text{ kg/m}^3$, surface tension $\\gamma = 0.0728\\text{ N/m}$, contact angle $\\theta_c = 0^\\circ$). (a) Calculate the capillary rise height $h$ using Jurin's law. (b) Calculate the total work done by surface tension during the rise and show that exactly half the work is dissipated as viscous heat.",
        "steps": [
            {
                "title": "Step 1: Calculate capillary rise height via Jurin's law",
                "math": "$$h = \\frac{2\\gamma \\cos\\theta_c}{\\rho g r} = \\frac{2(0.0728\\text{ N/m})\\cos(0^\\circ)}{(1000\\text{ kg/m}^3)(9.81\\text{ m/s}^2)(2.50 \\times 10^{-4}\\text{ m})} = \\frac{0.1456}{2.4525} = 0.05937\\text{ m} = 5.94\\text{ cm}$$",
                "explanation": "Water rises nearly $6\\text{ cm}$ up the narrow tube."
            },
            {
                "title": "Step 2: Calculate work done by upward surface tension force",
                "math": "$$F_{\\text{up}} = 2\\pi r \\gamma = 2\\pi (2.50 \\times 10^{-4}\\text{ m})(0.0728\\text{ N/m}) = 1.1435 \\times 10^{-4}\\text{ N}$$\n$$W_{\\text{tension}} = F_{\\text{up}} \\times h = (1.1435 \\times 10^{-4}\\text{ N})(0.05937\\text{ m}) = 6.789 \\times 10^{-6}\\text{ J}$$",
                "explanation": "This is the total work done by the capillary meniscus."
            },
            {
                "title": "Step 3: Compare with gained potential energy",
                "math": "$$\\Delta U_{\\text{grav}} = m g \\frac{h}{2} = (\\rho \\pi r^2 h) g \\frac{h}{2} = \\frac{1}{2} \\rho g \\pi r^2 h^2 = \\frac{1}{2} W_{\\text{tension}} = 3.395 \\times 10^{-6}\\text{ J}$$\n$$W_{\\text{dissipated}} = W_{\\text{tension}} - \\Delta U_{\\text{grav}} = \\frac{1}{2} W_{\\text{tension}}$$",
                "explanation": "Remarkably, exactly 50% of the work done by surface tension is stored as gravitational potential energy; the other 50% is converted into heat by viscous drag as the liquid ascends!"
            }
        ]
    },
    {
        "id": "prob-3-2",
        "difficulty": "Hard",
        "title": "Coalescence of Two Soap Bubbles",
        "question": "Two spherical soap bubbles of radii $r_1 = 3.00\\text{ cm}$ and $r_2 = 4.00\\text{ cm}$ in vacuum coalesce under isothermal conditions into a single soap bubble of radius $R$. Assuming the soap film surface tension is $\\gamma$ and ambient atmospheric pressure is negligible ($P_0 = 0$), derive the relationship between $R, r_1,$ and $r_2$ and calculate the final radius $R$.",
        "steps": [
            {
                "title": "Step 1: Write internal pressure and ideal gas law for each bubble",
                "math": "$$P_1 = \\frac{4\\gamma}{r_1}, \\quad P_2 = \\frac{4\\gamma}{r_2}, \\quad P = \\frac{4\\gamma}{R}$$\n$$V_1 = \\frac{4}{3}\\pi r_1^3, \\quad V_2 = \\frac{4}{3}\\pi r_2^3, \\quad V = \\frac{4}{3}\\pi R^3$$",
                "explanation": "Under isothermal conditions, total moles of trapped air are conserved: $n_{\\text{total}} = n_1 + n_2 \\implies P V = P_1 V_1 + P_2 V_2$."
            },
            {
                "title": "Step 2: Substitute pressures into the conservation relation",
                "math": "$$\\left( \\frac{4\\gamma}{R} \\right) \\left( \\frac{4}{3}\\pi R^3 \\right) = \\left( \\frac{4\\gamma}{r_1} \\right) \\left( \\frac{4}{3}\\pi r_1^3 \\right) + \\left( \\frac{4\\gamma}{r_2} \\right) \\left( \\frac{4}{3}\\pi r_2^3 \\right)$$\n$$R^2 = r_1^2 + r_2^2$$",
                "explanation": "The sum of the squares of the radii is conserved when two bubbles coalesce in a vacuum."
            },
            {
                "title": "Step 3: Compute numerical radius R",
                "math": "$$R = \\sqrt{r_1^2 + r_2^2} = \\sqrt{(3.00\\text{ cm})^2 + (4.00\\text{ cm})^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5.00\\text{ cm}$$",
                "explanation": "The combined soap bubble has a radius of exactly $5.00\\text{ cm}$."
            }
        ]
    },
    {
        "id": "prob-3-3",
        "difficulty": "Hard",
        "title": "Overturning Stability of a Concrete Gravity Dam",
        "question": "A vertical concrete gravity dam has a height of $H = 30.0\\text{ m}$ and a crest width of $W = 100.0\\text{ m}$. Water is filled to the top ($h = 30.0\\text{ m}$, density $\\rho = 1000\\text{ kg/m}^3$). (a) Calculate the total horizontal hydrostatic thrust $F$ acting on the dam. (b) Find the depth of the center of pressure. (c) Calculate the overturning torque $\\tau$ about the toe of the dam at the base.",
        "steps": [
            {
                "title": "Step 1: Compute total hydrostatic thrust",
                "math": "$$F = \\frac{1}{2} \\rho g W H^2 = \\frac{1}{2} (1000\\text{ kg/m}^3)(9.81\\text{ m/s}^2)(100.0\\text{ m})(30.0\\text{ m})^2$$\n$$F = 490.5 \\times 100 \\times 900 = 4.415 \\times 10^8\\text{ N} = 441.5\\text{ MN}$$",
                "explanation": "The water exerts over 441 million Newtons of horizontal force against the dam face."
            },
            {
                "title": "Step 2: Locate the center of pressure",
                "math": "$$h_{\\text{cp}} = \\frac{2}{3} H = \\frac{2}{3} (30.0\\text{ m}) = 20.0\\text{ m from the surface}$$\n$$y_{\\text{base}} = H - h_{\\text{cp}} = 30.0\\text{ m} - 20.0\\text{ m} = 10.0\\text{ m above the base}$$",
                "explanation": "The resultant force acts at a height of 10 meters above the dam foundation."
            },
            {
                "title": "Step 3: Calculate the overturning torque about the toe",
                "math": "$$\\tau = F \\times y_{\\text{base}} = (4.415 \\times 10^8\\text{ N})(10.0\\text{ m}) = 4.415 \\times 10^9\\text{ N}\\cdot\\text{m} = 4.415\\text{ GN}\\cdot\\text{m}$$",
                "explanation": "The dam's own self-weight must produce a stabilizing moment substantially exceeding $4.415\\text{ GN}\\cdot\\text{m}$ to guarantee a factor of safety against tipping."
            }
        ]
    }
]

# Write Unit 3
with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/matter_u3.json', 'w') as f:
    json.dump({"number": 3, "title": "Hydrostatics and Surface Tension", "leadSummary": "Hydrostatic pressure, Pascal's law, thrust on submerged planes, center of pressure, floating body stability, surface tension, Young-Laplace equation, minimal surfaces, and Jurin's capillary law.", "sections": u3_sections, "problems": u3_problems}, f, indent=2)

print("Unit 3 built successfully with 10 sections and 3 solved problems!")
