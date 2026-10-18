# Build Script for Unit 4: Hydrodynamics and Viscosity
import json

u4_sections = [
    {
        "id": "sec-4-1",
        "number": "§4.1",
        "heading": "Lines and Tubes of Flow: Streamline and Turbulent Motion",
        "simulation": "hydro-pipe-flow-sim",
        "content": """Fluid dynamics investigates liquids and gases in motion. The velocity of a moving fluid at spatial coordinates $(x, y, z)$ and time $t$ is represented by the vector velocity field $\\vec{v}(x, y, z, t)$.

<h4>1. Steady vs. Unsteady Flow</h4>
A fluid flow is defined as <strong>steady</strong> (or stationary) if the velocity, pressure, and density at every fixed point in space remain constant with respect to time:
$$\\frac{\\partial \\vec{v}}{\\partial t} = 0, \\quad \\frac{\\partial P}{\\partial t} = 0, \\quad \\frac{\\partial \\rho}{\\partial t} = 0$$
In steady flow, while individual fluid particles accelerate as they move along their trajectory, the spatial velocity field at any given geometric coordinate remains invariant. In unsteady flow, local time derivatives are non-zero.

<h4>2. Streamlines, Pathlines, and Streaklines</h4>
<ul>
  <li><strong>Streamline:</strong> A continuous curve drawn through the fluid such that the tangent at every point coincides with the direction of the fluid velocity vector $\\vec{v}$ at that instant:
  $$\\frac{dx}{v_x} = \\frac{dy}{v_y} = \\frac{dz}{v_z}$$
  Because velocity is single-valued at any point, streamlines can never intersect.</li>
  <li><strong>Pathline:</strong> The actual physical trajectory traced out by an individual moving fluid particle over time:
  $$\\frac{d\\vec{r}}{dt} = \\vec{v}(\\vec{r}, t)$$</li>
  <li><strong>Streakline:</strong> The instantaneous locus of all fluid particles that have passed sequentially through a specific fixed injection point (e.g., a dye filament in water or smoke in a wind tunnel).</li>
</ul>
<em>Fundamental Theorem:</em> In steady flow, streamlines, pathlines, and streaklines are completely identical.

<h4>3. Tube of Flow (Streamtube)</h4>
A tube of flow is an imaginary tubular surface formed by the bundle of streamlines passing through the perimeter of an arbitrary closed curve in the fluid.
Because velocity vectors are everywhere tangent to the surface of the streamtube, fluid can never cross the tubular boundary. Hence, a tube of flow behaves like an impermeable pipe.

<h4>4. Laminar vs. Turbulent Flow and the Reynolds Number</h4>
Osborne Reynolds (1883) demonstrated that fluid motion occurs in two distinct fundamental regimes:
<ul>
  <li><strong>Laminar Flow:</strong> Fluid moves smoothly in parallel layers (laminae) that slide past one another with minimal macroscopic mixing. Governed by viscous shear stresses.</li>
  <li><strong>Turbulent Flow:</strong> Highly irregular, chaotic, unsteady flow characterized by macroscopic eddies, vortices, and rapid momentum dissipation.</li>
</ul>
The transition between these regimes is governed by the dimensionless <strong>Reynolds Number ($Re$)</strong>:
$$Re = \\frac{\\rho v D}{\\eta} = \\frac{v D}{\\nu}$$
where $\\rho$ is fluid density, $v$ is mean flow speed, $D$ is characteristic conduit diameter (or object dimension), $\\eta$ is dynamic viscosity, and $\\nu = \\eta / \\rho$ is kinematic viscosity.
Physical interpretation: $Re$ represents the ratio of inertial forces to viscous forces:
$$Re = \\frac{\\text{Inertial Force}}{\\text{Viscous Force}} \\sim \\frac{\\rho v^2 D^2}{\\eta v D} = \\frac{\\rho v D}{\\eta}$$
For internal pipe flow:
<ul>
  <li>$Re < 2000$: Laminar flow regime (stable).</li>
  <li>$2000 \\le Re \\le 4000$: Transition regime.</li>
  <li>$Re > 4000$: Fully turbulent flow regime.</li>
</ul>"""
    },
    {
        "id": "sec-4-2",
        "number": "§4.2",
        "heading": "The Equation of Continuity",
        "simulation": "hydro-pipe-flow-sim",
        "content": """The equation of continuity is the mathematical expression of the fundamental law of <strong>conservation of mass</strong> applied to fluid flow.

<h4>1. 1D Continuity for a Streamtube</h4>
Consider steady flow through a tube of flow with non-uniform cross-sectional area.
Let $A_1$ be the cross-sectional area, $\\rho_1$ the fluid density, and $v_1$ the flow speed at entry station 1.
In time increment $\\Delta t$, the fluid advances by length $\\Delta x_1 = v_1 \\Delta t$.
The volume entering station 1 is $\\Delta V_1 = A_1 v_1 \\Delta t$, and the entering mass is:
$$\\Delta m_1 = \\rho_1 A_1 v_1 \\Delta t$$
Similarly, at exit station 2 with cross-sectional area $A_2$, density $\\rho_2$, and speed $v_2$, the mass leaving the tube is:
$$\\Delta m_2 = \\rho_2 A_2 v_2 \\Delta t$$
Because no mass is created, destroyed, or leaks across the streamtube boundary, mass conservation demands $\\Delta m_1 = \\Delta m_2$:
$$\\rho_1 A_1 v_1 = \\rho_2 A_2 v_2 = \\text{constant} = \\dot{m}$$
where $\\dot{m} = \\frac{dm}{dt}$ is the <strong>mass flow rate</strong> (kg/s).

<h4>2. Incompressible Fluid Flow</h4>
For liquids and subsonic gas flows where Mach number $M < 0.3$, density variations are negligible ($\rho_1 = \rho_2 = \rho = \text{constant}$). The equation simplifies to:
$$A_1 v_1 = A_2 v_2 = \\text{constant} = Q$$
where $Q = \\frac{dV}{dt} = A v$ is the <strong>volume flow rate</strong> (m³/s).
<em>Physical Consequence:</em> Fluid speed is inversely proportional to cross-sectional area:
$$v \\propto \\frac{1}{A}$$
When a pipe constricts to half its diameter ($D_2 = D_1 / 2$), its area drops by a factor of 4 ($A_2 = A_1 / 4$), forcing the fluid speed to quadruple ($v_2 = 4 v_1$).

<h4>3. General 3D Differential Form of Continuity</h4>
For an arbitrary differential control volume $dxdydz$ in space:
$$\\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot (\\rho \\vec{v}) = 0$$
$$\\frac{\\partial \\rho}{\\partial t} + \\frac{\\partial (\\rho v_x)}{\\partial x} + \\frac{\\partial (\\rho v_y)}{\\partial y} + \\frac{\\partial (\\rho v_z)}{\\partial z} = 0$$
For steady incompressible flow ($\frac{\\partial \\rho}{\\partial t} = 0$ and $\rho = \text{constant}$):
$$\\nabla \\cdot \\vec{v} = 0$$
This solenoidal condition guarantees zero divergence of the velocity field in incompressible hydrodynamics."""
    },
    {
        "id": "sec-4-3",
        "number": "§4.3",
        "heading": "Euler's Equation of Motion and Bernoulli's Theorem",
        "simulation": "venturi-bernoulli-sim",
        "content": """Bernoulli's theorem, formulated by Daniel Bernoulli in 1738, is the statement of the work-energy theorem for ideal fluid flow.

<h4>1. Assumptions of Ideal Flow</h4>
Bernoulli's equation applies strictly under four idealizing assumptions:
<ol>
  <li><strong>Inviscid:</strong> Zero internal friction / zero viscosity ($\eta = 0$).</li>
  <li><strong>Incompressible:</strong> Constant fluid density ($\rho = \text{constant}$).</li>
  <li><strong>Steady:</strong> Flow parameters do not change with time ($\partial \\vec{v}/\\partial t = 0$).</li>
  <li><strong>Irrotational:</strong> Fluid elements possess zero angular velocity ($\nabla \\times \\vec{v} = 0$).</li>
</ol>

<h4>2. Derivation from Euler's Equation along a Streamline</h4>
Consider a fluid parcel of cross-section $dA$ and length $ds$ moving along an inclined streamline at angle $\\theta$ to the horizontal.
Newton's second law along the streamline coordinate $s$ is:
$$dF_s = dm \\, a_s$$
The forces acting along $s$ are the pressure forces on the ends and the tangential component of gravity:
$$dF_s = P \\, dA - (P + dP) \\, dA - dm \\, g \\sin\\theta$$
Since $dm = \\rho \\, dA \\, ds$ and $\\sin\\theta = \\frac{dz}{ds}$:
$$-dP \\, dA - \\rho g \\, dA \\, dz = (\\rho \\, dA \\, ds) \\left( v \\frac{dv}{ds} \\right)$$
Dividing through by $\\rho \\, dA$:
$$-\\frac{dP}{\\rho} - g \\, dz = v \\, dv$$
$$\\frac{dP}{\\rho} + v \\, dv + g \\, dz = 0$$
This is <strong>Euler's 1D equation of motion</strong> along a streamline.

<h4>3. Integration to Bernoulli's Equation</h4>
Integrating along the streamline from point 1 to point 2 for constant density $\\rho$:
$$\\int_{P_1}^{P_2} \\frac{dP}{\\rho} + \\int_{v_1}^{v_2} v \\, dv + \\int_{z_1}^{z_2} g \\, dz = 0$$
$$\\frac{P}{\\rho} + \\frac{1}{2}v^2 + gz = \\text{constant}$$
Multiplying by $\\rho$:
$$P + \\frac{1}{2}\\rho v^2 + \\rho g z = \\text{constant}$$
Each term represents an energy density (Joules per cubic meter, or Pascals):
<ul>
  <li>$P$: <strong>Static Pressure</strong> (internal thermodynamic compressive stress).</li>
  <li>$\\frac{1}{2}\\rho v^2$: <strong>Dynamic Pressure</strong> (kinetic energy per unit volume).</li>
  <li>$\\rho g z$: <strong>Hydrostatic Pressure</strong> (gravitational potential energy per unit volume).</li>
  <li>$P_0 = P + \\frac{1}{2}\\rho v^2$: <strong>Stagnation (Total) Pressure</strong> along a horizontal streamline ($z = \text{const}$).</li>
</ul>
Dividing by $\\rho g$ yields the expression in terms of hydraulic heads (meters of fluid column):
$$\\frac{P}{\\rho g} + \\frac{v^2}{2g} + z = H = \\text{constant Head}$$
where $\\frac{P}{\\rho g}$ is pressure head, $\\frac{v^2}{2g}$ is velocity head, and $z$ is elevation head."""
    },
    {
        "id": "sec-4-4",
        "number": "§4.4",
        "heading": "Applications of Bernoulli's Equation: Venturi Meter, Pitot Tube, and Torricelli's Law",
        "simulation": "venturi-bernoulli-sim",
        "content": """Bernoulli's theorem provides the theoretical foundation for major fluid measurement instruments and drainage systems.

<h4>1. The Venturi Meter</h4>
A Venturi meter measures the volume flow rate $Q$ of liquid through a pipeline without moving parts.
It consists of a converging nozzle of inlet area $A_1$, a narrow throat of area $A_2 < A_1$, and a gradual diffuser to prevent turbulence.
By continuity for horizontal flow ($z_1 = z_2$):
$$v_1 = \\frac{Q}{A_1}, \\quad v_2 = \\frac{Q}{A_2} = \\frac{A_1}{A_2} v_1$$
Applying Bernoulli's equation between inlet and throat:
$$P_1 + \\frac{1}{2}\\rho v_1^2 = P_2 + \\frac{1}{2}\\rho v_2^2$$
$$P_1 - P_2 = \\frac{1}{2}\\rho (v_2^2 - v_1^2) = \\frac{1}{2}\\rho v_1^2 \\left[ \\left(\\frac{A_1}{A_2}\\right)^2 - 1 \\right]$$
A differential U-tube manometer containing liquid of density $\\rho_m$ connected between stations indicates height difference $h$:
$$P_1 - P_2 = (\\rho_m - \\rho) g h$$
Equating expressions yields the theoretical velocity at station 1:
$$v_1 = \\sqrt{ \\frac{2(\\rho_m - \\rho) g h}{\\rho \\left[ (A_1 / A_2)^2 - 1 \\right]} }$$
The actual volumetric flow rate incorporates a discharge coefficient $C_d \\approx 0.96 - 0.98$ to account for minor viscous losses:
$$Q = C_d A_1 A_2 \\sqrt{ \\frac{2(\\rho_m - \\rho) g h}{\\rho (A_1^2 - A_2^2)} }$$

<h4>2. The Pitot-Static Tube</h4>
Invented by Henri Pitot (1732) and modified by Henry Darcy, the Pitot-static tube measures fluid flow speed (used on aircraft airspeed indicators and in wind tunnels).
<ul>
  <li><strong>Static tap:</strong> Aligned flush with the outer wall parallel to streamlines, measuring purely static pressure $P$.</li>
  <li><strong>Stagnation tap:</strong> Faces directly into the oncoming flow. At the probe tip, oncoming fluid is brought to complete rest ($v_{stag} = 0$).</li>
</ul>
Applying Bernoulli's equation between free stream and stagnation point:
$$P + \\frac{1}{2}\\rho v^2 = P_{stag} + 0 \\implies P_{stag} - P = \\frac{1}{2}\\rho v^2$$
Measuring the differential pressure $\\Delta P = P_{stag} - P$:
$$v = \\sqrt{\\frac{2 \\Delta P}{\\rho}} = \\sqrt{\\frac{2 \\rho_m g h}{\\rho}}$$

<h4>3. Torricelli's Law of Efflux</h4>
Evangelista Torricelli (1643) studied liquid discharge from an orifice of area $a$ at depth $h$ below the free surface of an open tank of cross-sectional area $A$.
Both the tank free surface and the orifice exit jet are open to atmospheric pressure ($P_1 = P_2 = P_{atm}$).
Bernoulli's equation:
$$P_{atm} + \\frac{1}{2}\\rho v_1^2 + \\rho g h = P_{atm} + \\frac{1}{2}\\rho v_2^2 + 0$$
Using continuity $A v_1 = a v_2 \\implies v_1 = (a / A) v_2$:
$$gh = \\frac{1}{2}v_2^2 \\left( 1 - \\frac{a^2}{A^2} \\right) \\implies v_2 = \\sqrt{ \\frac{2gh}{1 - (a/A)^2} }$$
When the tank is large compared to the orifice ($A \\gg a$):
$$v_2 = \\sqrt{2gh}$$
<em>Torricelli's Theorem:</em> The efflux velocity of liquid issuing under gravity from an orifice equals the speed acquired by a body falling freely from rest through height $h$.
The actual jet contracts to area $A_{jet} = C_c a$ where $C_c \\approx 0.62$ is the coefficient of contraction (vena contracta)."""
    },
    {
        "id": "sec-4-5",
        "number": "§4.5",
        "heading": "Flow in a Curved Duct and Vortex Motion",
        "simulation": "hydro-pipe-flow-sim",
        "content": """When streamlines curve, fluid elements undergo centripetal acceleration, which requires a transverse pressure gradient directed toward the center of curvature.

<h4>1. Transverse Pressure Gradient</h4>
Consider a fluid parcel of width $dr$, length $ds$, and unit depth following a circular streamline of radius of curvature $r$ with speed $v$.
The centripetal force required to maintain circular trajectory is:
$$dF_r = dm \\, \\frac{v^2}{r} = (\\rho \\, dr \\, ds) \\frac{v^2}{r}$$
This radial force is supplied by the net normal pressure difference across the parcel:
$$(P + dP) \\, ds - P \\, ds = dP \\, ds$$
Equating:
$$dP \\, ds = \\rho \\, dr \\, ds \\, \\frac{v^2}{r} \\implies \\frac{\\partial P}{\\partial r} = \\frac{\\rho v^2}{r}$$
<em>Conclusion:</em> Pressure always increases radially outward across curved streamlines ($\frac{\\partial P}{\\partial r} > 0$).
In a curved pipe or duct:
<ul>
  <li>The outer wall experiences high pressure.</li>
  <li>The inner bend experiences low pressure.</li>
</ul>

<h4>2. Free vs. Forced Vortices</h4>
<ul>
  <li><strong>Forced (Rotational) Vortex:</strong> Fluid rotates as a solid body with constant angular velocity $\\omega$ (e.g., liquid stirred in a beaker):
  $$v(r) = \\omega r$$
  $$\\frac{dP}{dr} = \\rho \\frac{(\\omega r)^2}{r} = \\rho \\omega^2 r \\implies P(r) = P(0) + \\frac{1}{2}\\rho \\omega^2 r^2$$
  The free surface forms a paraboloid of revolution: $z(r) = \\frac{\\omega^2 r^2}{2g}$.
  Vorticity is non-zero: $\\vec{\\omega} = \\nabla \\times \\vec{v} = 2\\omega \\hat{k} \\ne 0$.</li>
  <li><strong>Free (Irrotational) Vortex:</strong> Fluid circulates without torque; angular momentum is conserved (e.g., bathtub drain, cyclone):
  $$L = m v r = \\text{constant} \\implies v(r) = \\frac{\\Gamma}{2\\pi r}$$
  where $\\Gamma = \\oint \\vec{v} \\cdot d\\vec{r}$ is circulation.
  The vorticity is zero everywhere except at the singular origin: $\\nabla \\times \\vec{v} = 0$.
  Applying Bernoulli's equation ($P + \\frac{1}{2}\\rho v^2 = P_\\infty$):
  $$P(r) = P_\\infty - \\frac{1}{2}\\rho \\left(\\frac{\\Gamma}{2\\pi r}\\right)^2$$
  Pressure drops sharply toward the vortex center, causing the core depression / funnel.</li>
</ul>"""
    },
    {
        "id": "sec-4-6",
        "number": "§4.6",
        "heading": "Viscosity and Newton's Law of Viscous Shear",
        "simulation": "viscosity-stokes-sim",
        "content": """Real fluids exhibit internal friction termed <strong>viscosity</strong>, which dissipates mechanical kinetic energy into internal thermal energy.

<h4>1. Physical Mechanism of Viscosity</h4>
When adjacent fluid layers move at different velocities, momentum is exchanged across the interface:
<ul>
  <li>In <strong>gases</strong>, random molecular thermal motion carries high-speed x-momentum molecules into slower layers and vice versa. Viscosity arises from molecular transport.</li>
  <li>In <strong>liquids</strong>, viscosity arises primarily from cohesive intermolecular forces (van der Waals, hydrogen bonding) between adjacent molecular layers sliding past one another.</li>
</ul>

<h4>2. Newton's Law of Viscosity</h4>
Consider liquid confined between two parallel plates separated by distance $h$. The lower plate is fixed, and the upper plate moves with constant velocity $U$.
Fluid in direct contact with solid boundaries adheres without slipping (the <strong>no-slip boundary condition</strong>):
$$v(y=0) = 0, \\quad v(y=h) = U$$
The fluid establishes a linear velocity profile $v_x(y) = U y / h$.
Sir Isaac Newton postulated that the tangential shear stress $\\tau$ between adjacent liquid layers is directly proportional to the transverse velocity gradient $\\frac{dv_x}{dy}$:
$$\\tau = \\frac{F}{A} = \\eta \\frac{dv_x}{dy}$$
where:
<ul>
  <li>$\\tau = F/A$ is shear stress (N/m² or Pa).</li>
  <li>$\\frac{dv_x}{dy}$ is the rate of shear strain (s⁻¹).</li>
  <li>$\\eta$ is the <strong>dynamic coefficient of viscosity</strong> (Pa·s or $\\text{kg}/(\\text{m}\\cdot\\text{s})$).</li>
</ul>

<h4>3. Units of Viscosity</h4>
<ul>
  <li><strong>Dynamic Viscosity ($\eta$):</strong>
  <ul>
    <li>SI Unit: $\\text{Pa}\\cdot\\text{s} = \\text{N}\\cdot\\text{s}/\\text{m}^2 = \\text{kg}/(\\text{m}\\cdot\\text{s})$.</li>
    <li>CGS Unit: Poise ($\\text{P}$) where $1 \\text{ P} = 0.1 \\text{ Pa}\\cdot\\text{s} = 1 \\text{ dyne}\\cdot\\text{s}/\\text{cm}^2$.</li>
    <li>Centipoise: $1 \\text{ cP} = 10^{-2} \\text{ P} = 10^{-3} \\text{ Pa}\\cdot\\text{s}$. (Water at 20°C has $\\eta \\approx 1.002 \\text{ cP} \\approx 1.002 \\times 10^{-3} \\text{ Pa}\\cdot\\text{s}$).</li>
  </ul></li>
  <li><strong>Kinematic Viscosity ($\nu$):</strong>
  $$\\nu = \\frac{\\eta}{\\rho}$$
  <ul>
    <li>SI Unit: $\\text{m}^2/\\text{s}$.</li>
    <li>CGS Unit: Stokes ($\\text{St}$) where $1 \\text{ St} = 1 \\text{ cm}^2/\\text{s} = 10^{-4} \\text{ m}^2/\\text{s}$.</li>
    <li>Centistokes: $1 \\text{ cSt} = 10^{-6} \\text{ m}^2/\\text{s}$.</li>
  </ul></li>
</ul>"""
    },
    {
        "id": "sec-4-7",
        "number": "§4.7",
        "heading": "Poiseuille's Law: Laminar Flow through a Capillary Tube",
        "simulation": "viscosity-stokes-sim",
        "content": """Jean Léonard Marie Poiseuille (1840) experimentally derived, and Gotthilf Hagen theoretically proved, the law governing steady laminar flow of a viscous incompressible fluid through a cylindrical capillary tube of radius $R$ and length $L$.

<h4>1. Velocity Distribution Derivation</h4>
Consider a coaxial cylindrical fluid element of radius $r$ and length $L$ inside a tube of internal radius $R$.
The net pressure force driving the element forward is:
$$F_P = \\Delta P \\cdot (\\pi r^2) = (P_1 - P_2) \\pi r^2$$
The opposing viscous retarding force acting on the outer cylindrical surface of area $2\\pi r L$ is:
$$F_\\eta = -\\eta (2\\pi r L) \\frac{dv}{dr}$$
In steady, non-accelerating flow, force equilibrium requires:
$$\\Delta P \\pi r^2 + 2\\pi r L \\eta \\frac{dv}{dr} = 0$$
$$\\frac{dv}{dr} = -\\frac{\\Delta P}{2\\eta L} r$$
Integrating with respect to $r$:
$$v(r) = -\\frac{\\Delta P}{4\\eta L} r^2 + C$$
Applying the <strong>no-slip boundary condition</strong> at the tube wall: $v(R) = 0$:
$$0 = -\\frac{\\Delta P}{4\\eta L} R^2 + C \\implies C = \\frac{\\Delta P}{4\\eta L} R^2$$
Thus, the velocity distribution is a <strong>paraboloid of revolution</strong>:
$$v(r) = \\frac{\\Delta P}{4\\eta L} (R^2 - r^2)$$
Maximum velocity occurs at the central axis ($r = 0$):
$$v_{max} = \\frac{\\Delta P R^2}{4\\eta L}$$

<h4>2. Total Volume Flow Rate ($Q$)</h4>
The volumetric flow $dQ$ passing through an infinitesimal annular ring between radii $r$ and $r + dr$ is:
$$dQ = v(r) \\cdot (2\\pi r \\, dr) = \\frac{\\pi \\Delta P}{2\\eta L} (R^2 - r^2) r \\, dr$$
Integrating across the entire tube from $r = 0$ to $r = R$:
$$Q = \\int_0^R dQ = \\frac{\\pi \\Delta P}{2\\eta L} \\int_0^R (R^2 r - r^3) dr = \\frac{\\pi \\Delta P}{2\\eta L} \\left[ \\frac{R^2 r^2}{2} - \\frac{r^4}{4} \\right]_0^R$$
$$Q = \\frac{\\pi \\Delta P}{2\\eta L} \\left( \\frac{R^4}{4} \\right) = \\frac{\\pi \\Delta P R^4}{8 \\eta L}$$
This is the celebrated <strong>Hagen-Poiseuille Equation</strong>.

<h4>3. Hydraulic Resistance and Fourth-Power Dependence</h4>
Analogous to Ohm's law ($I = \\Delta V / R_{elec}$), the volumetric flow is:
$$Q = \\frac{\\Delta P}{R_H}, \\quad \\text{where } R_H = \\frac{8 \\eta L}{\\pi R^4}$$
$R_H$ is the <strong>hydraulic resistance</strong>.
Because $Q \\propto R^4$, even a minuscule reduction in radius dramatically curtails flow. For example:
<ul>
  <li>If an artery suffers a 19% luminal diameter constriction ($R \\to 0.81 R$), the flow rate drops by $(0.81)^4 \\approx 0.43$, cutting blood perfusion by 57%!</li>
</ul>
Mean flow velocity is exactly half the maximum centerline velocity:
$$\\bar{v} = \\frac{Q}{\\pi R^2} = \\frac{\\Delta P R^2}{8\\eta L} = \\frac{1}{2} v_{max}$$"""
    },
    {
        "id": "sec-4-8",
        "number": "§4.8",
        "heading": "Stokes' Law and Terminal Velocity",
        "simulation": "viscosity-stokes-sim",
        "content": """Sir George Gabriel Stokes (1851) solved the Navier-Stokes equations for low Reynolds number creep flow ($Re \\ll 1$) past a smooth spherical body of radius $r$.

<h4>1. Derivation by Dimensional Analysis</h4>
Assume the viscous retarding force $F_d$ on a sphere depends on:
$$F_d \\propto \\eta^a r^b v^c$$
Writing dimensional formulas ($[F] = M L T^{-2}$, $[\eta] = M L^{-1} T^{-1}$, $[r] = L$, $[v] = L T^{-1}$):
$$M L T^{-2} = (M L^{-1} T^{-1})^a (L)^b (L T^{-1})^c = M^a L^{-a + b + c} T^{-a - c}$$
Equating powers:
<ul>
  <li>Mass ($M$): $a = 1$</li>
  <li>Time ($T$): $-a - c = -2 \\implies c = 2 - a = 1$</li>
  <li>Length ($L$): $-a + b + c = 1 \\implies -1 + b + 1 = 1 \\implies b = 1$</li>
</ul>
Thus $F_d \\propto \\eta r v$. Stokes' full hydrodynamic boundary-value solution determines the dimensionless coefficient to be exactly $6\\pi$:
$$F_d = 6\\pi \\eta r v$$
This is <strong>Stokes' Law</strong>. (Of the total drag, $4\\pi \\eta r v$ originates from viscous skin friction and $2\\pi \\eta r v$ from pressure/form drag).

<h4>2. Motion of a Falling Sphere and Terminal Velocity</h4>
Consider a solid sphere of radius $r$ and density $\\rho$ falling vertically under gravity through a viscous fluid of density $\\sigma < \\rho$.
Three forces act on the body:
<ol>
  <li>Downward gravity (weight): $W = mg = \\frac{4}{3}\\pi r^3 \\rho g$</li>
  <li>Upward buoyant force (Archimedes' thrust): $F_B = \\frac{4}{3}\\pi r^3 \\sigma g$</li>
  <li>Upward viscous drag (Stokes retarding force): $F_d = 6\\pi \\eta r v$</li>
</ol>
The equation of motion is:
$$m \\frac{dv}{dt} = W - F_B - F_d$$
$$\\frac{4}{3}\\pi r^3 \\rho \\frac{dv}{dt} = \\frac{4}{3}\\pi r^3 (\\rho - \\sigma) g - 6\\pi \\eta r v$$
As velocity $v$ increases, viscous drag $F_d$ grows until the upward forces precisely balance the weight. Acceleration ceases ($\frac{dv}{dt} = 0$), and the sphere attains a constant <strong>terminal velocity ($v_t$)</strong>:
$$6\\pi \\eta r v_t = \\frac{4}{3}\\pi r^3 (\\rho - \\sigma) g$$
$$v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}$$
Notice that terminal speed scales with $r^2$. Fine mist droplets ($r \\sim 10 \\ \\mu\\text{m}$) fall at millimeters per second, remaining suspended in clouds for hours."""
    },
    {
        "id": "sec-4-9",
        "number": "§4.9",
        "heading": "Experimental Determination of Viscosity and Temperature Variation",
        "simulation": "viscosity-stokes-sim",
        "content": """Accurate measurement of viscosity is vital in physical chemistry, chemical engineering, and aerodynamics.

<h4>1. Experimental Methods</h4>
<ul>
  <li><strong>Poiseuille's Capillary Viscometer:</strong> Liquid drains under a known hydrostatic head $h$ through a precision capillary tube of radius $R$ and length $L$. By measuring efflux time $t$ for known volume $V$:
  $$\\eta = \\frac{\\pi \\bar{P} R^4 t}{8 V L} = \\frac{\\pi \\rho g \\bar{h} R^4 t}{8 V L}$$
  Kinetic energy end corrections (Couette correction: $L_{eff} = L + m R$) must be applied for short tubes.</li>
  <li><strong>Ostwald Relative Viscometer:</strong> Compares flow time $t_1$ of test liquid of density $\\rho_1$ to flow time $t_2$ of reference liquid (distilled water, $\\rho_2, \\eta_2$) through the same capillary:
  $$\\frac{\\eta_1}{\\eta_2} = \\frac{\\rho_1 t_1}{\\rho_2 t_2}$$
  Eliminates tedious calibration of capillary radius $R$.</li>
  <li><strong>Stokes' Falling Sphere Viscometer:</strong> A small steel ball is timed falling between two fiducial marks separated by vertical distance $h$ in a wide glass cylinder filled with viscous liquid:
  $$\\eta = \\frac{2 r^2 (\\rho - \\sigma) g t}{9 h} \\cdot \\frac{1}{1 + 2.4 (r / R_{cyl})}$$
  The Ladenburg wall correction factor $\\frac{1}{1 + 2.4(r/R_{cyl})}$ accounts for the retarding effect of the cylinder walls.</li>
</ul>

<h4>2. Variation of Viscosity with Temperature</h4>
Viscosity exhibits fundamentally opposite temperature dependencies in liquids versus gases:
<ul>
  <li><strong>Liquids:</strong> As temperature rises, molecular thermal agitation expands the intermolecular spacing, weakening attractive van der Waals bonds. Consequently, liquid viscosity drops exponentially with temperature, described by <strong>Andrade's Equation</strong>:
  $$\\eta(T) = A e^{E_a / (R T)}$$
  where $E_a$ is the activation energy for viscous shear flow. Water viscosity decreases from $1.79 \\text{ cP}$ at 0°C to $0.28 \\text{ cP}$ at 100°C.</li>
  <li><strong>Gases:</strong> Kinetic theory dictates that gas viscosity is governed by momentum transport via molecular collisions:
  $$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda = \\frac{2}{3\\pi^{3/2}} \\frac{\\sqrt{m k_B T}}{d^2}$$
  Because mean molecular speed $\\bar{v} \\propto \\sqrt{T}$, gas viscosity increases with temperature!
  Accounting for intermolecular attraction leads to <strong>Sutherland's Formula</strong>:
  $$\\eta(T) = \\eta_0 \\left(\\frac{T}{T_0}\\right)^{3/2} \\frac{T_0 + C}{T + C}$$
  where $C$ is Sutherland's constant for the gas.</li>
</ul>"""
    }
]

u4_problems = [
    {
        "id": "prob-4-1",
        "difficulty": "Undergraduate Classical Exam Standard",
        "title": "Venturi Tube Flow Rate and Pressure Differential",
        "question": "A horizontal water pipeline of internal diameter $D_1 = 15.0\\text{ cm}$ constricts to a throat diameter $D_2 = 5.0\\text{ cm}$ in a Venturi meter. A differential mercury manometer connected between the main pipe and the throat indicates a height difference of $h = 24.5\\text{ cm}$ of mercury. Taking the density of water $\\rho = 1000\\text{ kg/m}^3$, the density of mercury $\\rho_m = 13600\\text{ kg/m}^3$, acceleration due to gravity $g = 9.80\\text{ m/s}^2$, and discharge coefficient $C_d = 0.980$, calculate:\\n(a) The pressure difference $\\Delta P = P_1 - P_2$ in $\\text{N/m}^2$,\\n(b) The linear velocity of water at the throat $v_2$, and\\n(c) The volumetric flow rate $Q$ in liters per second.",
        "steps": [
            {
                "title": "Step 1: Compute cross-sectional areas and area ratio",
                "math": "$$A_1 = \\frac{\\pi D_1^2}{4} = \\frac{\\pi (0.150)^2}{4} = 1.7671 \\times 10^{-2} \\text{ m}^2$$\n$$A_2 = \\frac{\\pi D_2^2}{4} = \\frac{\\pi (0.050)^2}{4} = 1.9635 \\times 10^{-3} \\text{ m}^2$$\n$$\\frac{A_1}{A_2} = \\left(\\frac{D_1}{D_2}\\right)^2 = 3.0^2 = 9.00$$",
                "explanation": "Because area scales with diameter squared, the inlet area is exactly 9 times greater than the throat area."
            },
            {
                "title": "Step 2: Determine pressure difference from manometer reading",
                "math": "$$\\Delta P = P_1 - P_2 = (\\rho_m - \\rho) g h$$\n$$\\Delta P = (13600 - 1000) \\times 9.80 \\times 0.245 = 12600 \\times 9.80 \\times 0.245 = 30252.6 \\text{ Pa} \\approx 3.025 \\times 10^4 \\text{ N/m}^2$$",
                "explanation": "The effective buoyant manometer deflection accounts for the displaced water column over the mercury interface."
            },
            {
                "title": "Step 3: Calculate throat velocity and flow rate",
                "math": "$$v_2 = C_d \\sqrt{ \\frac{2 \\Delta P}{\\rho \\left[ 1 - (A_2 / A_1)^2 \\right]} } = 0.980 \\times \\sqrt{ \\frac{2 \\times 30252.6}{1000 \\times [1 - (1/9)^2]} }$$\n$$v_2 = 0.980 \\times \\sqrt{ \\frac{60505.2}{1000 \\times [1 - 1/81]} } = 0.980 \\times \\sqrt{\\frac{60.5052}{0.98765}} = 0.980 \\times \\sqrt{61.261} = 0.980 \\times 7.827 = 7.67 \\text{ m/s}$$\n$$Q = A_2 v_2 = (1.9635 \\times 10^{-3} \\text{ m}^2) \\times (7.67 \\text{ m/s}) = 0.01506 \\text{ m}^3/\\text{s} = 15.06 \\text{ L/s}$$",
                "explanation": "The linear water speed at the throat reaches 7.67 m/s, yielding a steady delivery rate of 15.1 liters per second."
            }
        ]
    },
    {
        "id": "prob-4-2",
        "difficulty": "Rigorous Honors Problem",
        "title": "Poiseuille Capillary Flow and Hydraulic Resistance in Network",
        "question": "A capillary tube $A$ of internal radius $r_A = 1.0\\text{ mm}$ and length $L_A = 20.0\\text{ cm}$ is connected in series with a second capillary tube $B$ of internal radius $r_B = 1.5\\text{ mm}$ and length $L_B = 30.0\\text{ cm}$. A steady total pressure drop of $\\Delta P_{tot} = 4000\\text{ Pa}$ is maintained across the composite system for glycerin flowing laminarly with viscosity $\\eta = 0.850\\text{ Pa}\\cdot\\text{s}$.\\n(a) Derive and calculate the hydraulic resistance of each tube and the total equivalent resistance of the series network,\\n(b) Find the volume flow rate $Q$, and\\n(c) Determine the individual pressure drop across tube $A$ and tube $B$.",
        "steps": [
            {
                "title": "Step 1: Compute hydraulic resistance of each capillary tube",
                "math": "$$R_H = \\frac{8 \\eta L}{\\pi r^4}$$\n$$R_{HA} = \\frac{8 \\times 0.850 \\times 0.20}{\\pi \\times (1.0 \\times 10^{-3})^4} = \\frac{1.36}{\\pi \\times 10^{-12}} = 4.329 \\times 10^{11} \\text{ Pa}\\cdot\\text{s/m}^3$$\n$$R_{HB} = \\frac{8 \\times 0.850 \\times 0.30}{\\pi \\times (1.5 \\times 10^{-3})^4} = \\frac{2.04}{\\pi \\times 5.0625 \\times 10^{-12}} = 1.283 \\times 10^{11} \\text{ Pa}\\cdot\\text{s/m}^3$$",
                "explanation": "Even though tube B is 50% longer than tube A, its 50% larger radius reduces its resistance by $(1.5)^4 = 5.06$ times."
            },
            {
                "title": "Step 2: Total series resistance and volumetric flow rate",
                "math": "$$R_{tot} = R_{HA} + R_{HB} = (4.329 + 1.283) \\times 10^{11} = 5.612 \\times 10^{11} \\text{ Pa}\\cdot\\text{s/m}^3$$\n$$Q = \\frac{\\Delta P_{tot}}{R_{tot}} = \\frac{4000}{5.612 \\times 10^{11}} = 7.128 \\times 10^{-9} \\text{ m}^3/\\text{s} = 7.13 \\times 10^{-3} \\text{ mL/s}$$",
                "explanation": "Flow rates in series are identical through both tubes, analogous to electric current in series resistors."
            },
            {
                "title": "Step 3: Calculate individual pressure drops",
                "math": "$$\\Delta P_A = Q R_{HA} = 7.128 \\times 10^{-9} \\times 4.329 \\times 10^{11} = 3086 \\text{ Pa}$$\n$$\\Delta P_B = Q R_{HB} = 7.128 \\times 10^{-9} \\times 1.283 \\times 10^{11} = 914 \\text{ Pa}$$\n$$\\Delta P_A + \\Delta P_B = 3086 + 914 = 4000 \\text{ Pa}$$",
                "explanation": "Over 77% of the total pressure drop occurs across tube A due to its narrower bore."
            }
        ]
    },
    {
        "id": "prob-4-3",
        "difficulty": "Experimental Physics Exam Standard",
        "title": "Stokes Terminal Velocity and Viscosity Measurement",
        "question": "A small spherical lead pellet of diameter $d = 2.00\\text{ mm}$ and density $\\rho = 11340\\text{ kg/m}^3$ falls through castor oil of density $\\sigma = 960\\text{ kg/m}^3$ held in a cylindrical jar. The pellet achieves terminal velocity and traverses two graduation marks separated by vertical distance $h = 25.0\\text{ cm}$ in a time of $t = 2.85\\text{ s}$.\\n(a) Determine the terminal velocity $v_t$,\\n(b) Calculate the coefficient of dynamic viscosity $\\eta$ of the oil using Stokes' law,\\n(c) Verify whether the flow satisfies the low Reynolds number criterion ($Re < 0.5$). Take $g = 9.80\\text{ m/s}^2$.",
        "steps": [
            {
                "title": "Step 1: Calculate terminal velocity of the pellet",
                "math": "$$v_t = \\frac{h}{t} = \\frac{0.250 \\text{ m}}{2.85 \\text{ s}} = 0.08772 \\text{ m/s} = 8.77 \\text{ cm/s}$$\n$$\\text{Radius } r = \\frac{d}{2} = 1.00 \\times 10^{-3} \\text{ m}$$",
                "explanation": "Because the pellet falls between marks after already reaching terminal equilibrium, velocity is steady."
            },
            {
                "title": "Step 2: Solve Stokes' formula for dynamic viscosity",
                "math": "$$v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta} \\implies \\eta = \\frac{2 r^2 (\\rho - \\sigma) g}{9 v_t}$$\n$$\\rho - \\sigma = 11340 - 960 = 10380 \\text{ kg/m}^3$$\n$$\\eta = \\frac{2 \\times (1.00 \\times 10^{-3})^2 \\times 10380 \\times 9.80}{9 \\times 0.08772} = \\frac{2 \\times 10^{-6} \\times 101724}{0.7895} = \\frac{0.20345}{0.7895} = 0.2577 \\text{ Pa}\\cdot\\text{s} = 2.58 \\text{ Poise}$$",
                "explanation": "The calculated dynamic viscosity is 0.258 Pa·s (258 cP), characteristic of refined castor oil."
            },
            {
                "title": "Step 3: Verification of Reynolds number criterion",
                "math": "$$Re = \\frac{\\sigma v_t (2r)}{\\eta} = \\frac{960 \\times 0.08772 \\times (2.00 \\times 10^{-3})}{0.2577} = \\frac{0.1684}{0.2577} = 0.653$$",
                "explanation": "With Re ~ 0.65, inertial corrections are minor (Oseen correction adds ~ (1 + 3/8 Re) = 1.24 factor), validating Stokes' viscous drag formulation to high accuracy."
            }
        ]
    }
]

unit4_data = {
    "number": 4,
    "title": "Hydrodynamics and Viscosity",
    "leadSummary": "A rigorous hydrodynamic study of moving fluids, streamline flow, the continuity equation, Euler and Bernoulli equations with technical applications, viscous shear, Hagen-Poiseuille capillary flow, Stokes drag, and viscosity thermometry.",
    "sections": u4_sections,
    "problems": u4_problems
}

with open("matter_u4.json", "w") as f:
    json.dump(unit4_data, f, indent=2)

print("Unit 4 built successfully with", len(u4_sections), "sections and", len(u4_problems), "solved problems!")
