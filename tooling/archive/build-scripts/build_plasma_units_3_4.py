# build_plasma_units_3_4.py
# Generates plasma_u3.json and plasma_u4.json for Plasma Physics Course #17

import json

# =========================================================================
# UNIT 3: GUIDING CENTER DRIFTS IN INHOMOGENEOUS FIELDS & ADIABATIC INVARIANTS
# =========================================================================

unit3_data = {
    "unitId": "unit3-plasma",
    "title": "Guiding Center Drifts in Inhomogeneous Fields & Adiabatic Invariants",
    "subtitle": "∇B Drift, Curvature Drift, Magnetic Mirrors & Action Invariants",
    "summary": "Rigorous treatment of charged particle dynamics in spatially inhomogeneous magnetic fields: guiding center perturbation theory, derivation of the gradient-B drift velocity, centrifugal curvature drift, combined vacuum field drift, magnetic gradient parallel to B and the longitudinal mirror force, rigorous proof of the first adiabatic invariant (magnetic moment constancy), loss cone physics and magnetic mirror confinement, longitudinal action second invariant, drift flux third invariant, and Van Allen radiation belt trapping.",
    "sections": [
        {
            "id": "sec-3-1",
            "number": "3.1",
            "title": "The Inhomogeneous Guiding Center Approximation & Spatial Scale Separation",
            "content": """
<h3>1. Spatial Inhomogeneity and Scale Separation</h3>
<p>
In realistic astrophysical and laboratory magnetic geometries (such as tokamaks, stellarators, and planetary dipoles), magnetic fields are non-uniform in space. Exact particle trajectories cannot be integrated analytically. However, when the magnetic field varies slowly across the dimensions of a single Larmor orbit:
</p>
$$\\epsilon \\equiv \\frac{r_L}{L_B} = \\frac{r_L}{|\\nabla B / B|} \\ll 1$$
<p>
we can employ the <strong>guiding center approximation</strong>. The particle motion separates into two disparate spatial and temporal scales:
</p>
<ul>
  <li>A fast, quasi-periodic circular gyration at frequency $\\omega_c$ with radius $r_L$.</li>
  <li>A slow, secular drift of the gyration center (the guiding center $\\vec{R}$) across and along magnetic field lines.</li>
</ul>
"""
        },
        {
            "id": "sec-3-2",
            "number": "3.2",
            "title": "Transverse Magnetic Gradients: Derivation of the Gradient-B Drift Velocity v_gradB",
            "content": """
<h3>1. Physical Mechanism of Gradient Drift</h3>
<p>
Consider a magnetic field directed along $\\hat{z}$ whose strength increases along $\\hat{y}$: $\\vec{B} = B(y)\\hat{z}$, with $\\nabla B = \\frac{dB}{dy}\\hat{y}$.
</p>
<p>
As a charged particle gyrates in the $xy$-plane, its instantaneous Larmor radius $r_L(y) = \\frac{m v_\\perp}{|q| B(y)}$ is smaller at larger $y$ (stronger $B$) and larger at smaller $y$ (weaker $B$). This asymmetric curvature prevents the orbit from closing into a circle, creating a steady lateral drift perpendicular to both $\\vec{B}$ and $\\nabla B$.
</p>

<h3>2. Mathematical Derivation</h3>
<p>
Taylor expand the magnetic field around the guiding center $\\vec{R}_0 = (x_0, y_0, z_0)$:
</p>
$$\\vec{B}(\\vec{r}) \\approx \\vec{B}_0 + (\\vec{r} - \\vec{R}_0)\\cdot\\nabla\\vec{B} = \\left( B_0 + y \\frac{\\partial B}{\\partial y} \\right)\\hat{z}$$
<p>
The particle's unperturbed circular orbit around the guiding center is:
</p>
$$x(t) = r_L \\sin(\\omega_c t), \\quad y(t) = \\pm r_L \\cos(\\omega_c t)$$
$$v_x(t) = v_\\perp \\cos(\\omega_c t), \\quad v_y(t) = \\mp v_\\perp \\sin(\\omega_c t)$$
<p>
The instantaneous Lorentz force along $y$ is $F_y = -q v_x B(y)$. Taking the time average of $F_y$ over one complete gyration period $\\tau_c = 2\\pi / \\omega_c$:
</p>
$$\\langle F_y \\rangle = -q \\langle v_x B(y) \\rangle = -q \\left\\langle v_\\perp \\cos(\\omega_c t) \\left[ B_0 + \\left(\\pm r_L \\cos(\\omega_c t)\\right)\\frac{\\partial B}{\\partial y} \\right] \\right\\rangle$$
<p>
Noting that $\\langle \\cos(\\omega_c t) \\rangle = 0$ and $\\langle \\cos^2(\\omega_c t) \\rangle = \\frac{1}{2}$:
</p>
$$\\langle F_y \\rangle = \\mp q v_\\perp r_L \\frac{1}{2} \\frac{\\partial B}{\\partial y} = \\mp \\frac{1}{2} q v_\\perp \\left( \\frac{m v_\\perp}{|q| B_0} \\right) \\frac{\\partial B}{\\partial y} = -\\frac{1}{2} \\frac{m v_\\perp^2}{B_0} \\frac{\\partial B}{\\partial y}$$
<p>
In coordinate-free vector notation, the net time-averaged transverse force is:
</p>
$$\\langle \\vec{F}_{\\nabla B} \\rangle = -\\mu \\nabla B = -\\frac{m v_\\perp^2}{2 B} \\nabla B$$
<p>
where $\\mu \\equiv \\frac{m v_\\perp^2}{2 B}$ is the particle's magnetic dipole moment. Substituting this force into the general guiding center force drift formula $\\vec{v}_F = \\frac{1}{q}\\frac{\\vec{F}\\times\\vec{B}}{B^2}$:
</p>
$$\\vec{v}_{\\nabla B} = \\frac{1}{q} \\frac{(-\\mu \\nabla B) \\times \\vec{B}}{B^2} = \\frac{\\mu}{q B^2} (\\vec{B} \\times \\nabla B) = \\frac{m v_\\perp^2}{2 q B^3} (\\vec{B} \\times \\nabla B)$$
<p>
Because of the explicit factor of $q$, ions and electrons drift in <strong>opposite directions</strong> across magnetic gradients!
</p>
"""
        },
        {
            "id": "sec-3-3",
            "number": "3.3",
            "title": "Curved Magnetic Field Lines: Centrifugal Acceleration & Derivation of Curvature Drift v_c",
            "content": """
<h3>1. Centrifugal Acceleration in Curved Geometry</h3>
<p>
Consider magnetic field lines with local radius of curvature $\\vec{R}_c$, pointing from the field line toward the center of curvature:
</p>
$$\\frac{\\vec{R}_c}{R_c^2} = -(\\hat{b}\\cdot\\nabla)\\hat{b}$$
<p>
where $\\hat{b} = \\vec{B} / B$ is the unit vector along the field. A particle moving along the field with parallel velocity $v_\\parallel$ experiences a centrifugal force directed outward:
</p>
$$\\vec{F}_c = \\frac{m v_\\parallel^2}{R_c^2} \\vec{R}_c$$

<h3>2. The Curvature Drift Velocity</h3>
<p>
Substituting this centrifugal force into the general guiding center force drift formula:
</p>
$$\\vec{v}_c = \\frac{1}{q} \\frac{\\vec{F}_c \\times \\vec{B}}{B^2} = \\frac{m v_\\parallel^2}{q B^2} \\frac{\\vec{R}_c \\times \\vec{B}}{R_c^2}$$
<p>
Key physical properties of curvature drift:
</p>
<ul>
  <li>$\\vec{v}_c$ depends quadratically on parallel velocity $v_\\parallel^2$.</li>
  <li>$\\vec{v}_c$ is inversely proportional to charge $q$: ions and electrons drift in opposite directions, driving a net electric current.</li>
</ul>
"""
        },
        {
            "id": "sec-3-4",
            "number": "3.4",
            "title": "Combined Vacuum Curvature and Gradient Drift & Charge Separation Currents",
            "content": """
<h3>1. The Vacuum Field Relation</h3>
<p>
In a current-free vacuum magnetic field, Ampère's law demands $\\nabla \\times \\vec{B} = 0$. In curvilinear coordinates with cylindrical symmetry ($\vec{B} = B_\\phi(r)\\hat{\\phi}$):
</p>
$$(\\nabla \\times \\vec{B})_z = \\frac{1}{r}\\frac{\\partial(r B_\\phi)}{\\partial r} = 0 \\implies B_\\phi(r) \\propto \\frac{1}{r}$$
<p>
Consequently:
</p>
$$\\frac{\\nabla B}{B} = -\\frac{\\vec{R}_c}{R_c^2} \\implies \\frac{\\vec{R}_c \\times \\vec{B}}{R_c^2} = \\frac{\\vec{B} \\times \\nabla B}{B}$$

<h3>2. Total Combined Guiding Center Drift</h3>
<p>
Summing the gradient-B drift and curvature drift in any vacuum magnetic field:
</p>
$$\\vec{v}_D = \\vec{v}_{\\nabla B} + \\vec{v}_c = \\frac{m v_\\perp^2}{2 q B^3}(\\vec{B}\\times\\nabla B) + \\frac{m v_\\parallel^2}{q B^3}(\\vec{B}\\times\\nabla B)$$
$$\\vec{v}_D = \\frac{m}{q B^3} \\left( v_\\parallel^2 + \\frac{1}{2}v_\\perp^2 \\right) (\\vec{B} \\times \\nabla B)$$
<p>
In a toroidal magnetic field (such as a simple torus without rotational transform), this combined drift forces ions vertically upward and electrons vertically downward. This catastrophic charge separation sets up a vertical electric field $\\vec{E}$, which subsequently drives an outward $\\vec{E}\\times\\vec{B}$ drift that dumps the entire plasma into the outer chamber wall—necessitating helical twisted magnetic fields (tokamaks/stellarators) to short-circuit the charge buildup.
</p>
"""
        },
        {
            "id": "sec-3-5",
            "number": "3.5",
            "title": "Longitudinal Magnetic Gradients: The Magnetic Mirror Force F_parallel = -mu grad_parallel B",
            "content": """
<h3>1. Magnetic Convergence & Gauss's Law</h3>
<p>
Consider a cylindrically symmetric magnetic field whose strength increases along the axis of symmetry ($z$-axis): $\\frac{\\partial B_z}{\\partial z} > 0$. Because magnetic field lines must converge as $B$ intensifies, Gauss's law for magnetism $\\nabla \\cdot \\vec{B} = 0$ requires a non-zero radial magnetic field component $B_r$:
</p>
$$\\nabla \\cdot \\vec{B} = \\frac{1}{r}\\frac{\\partial(r B_r)}{\\partial r} + \\frac{\\partial B_z}{\\partial z} = 0$$
<p>
Near the axis of symmetry where $\\frac{\\partial B_z}{\\partial z}$ is approximately independent of $r$:
</p>
$$\\frac{\\partial(r B_r)}{\\partial r} \\approx -r \\frac{\\partial B_z}{\\partial z} \\implies r B_r \\approx -\\frac{r^2}{2}\\frac{\\partial B_z}{\\partial z} \\implies B_r(r, z) \\approx -\\frac{r}{2}\\frac{\\partial B_z}{\\partial z}$$

<h3>2. The Longitudinal Mirror Restoring Force</h3>
<p>
The particle's azimuthal cyclotron gyration velocity $v_\\theta = \\mp v_\\perp$ couples with this radial magnetic field $B_r$ to produce a Lorentz force along the $z$-axis:
</p>
$$F_z = q(\\vec{v}\\times\\vec{B})_z = q(v_\\theta B_r - v_r B_\\theta) = q v_\\theta B_r$$
<p>
Substituting $B_r = -\\frac{r_L}{2}\\frac{\\partial B_z}{\\partial z}$ and $v_\\theta = -\\frac{q}{|q|}v_\\perp$:
</p>
$$F_z = q \\left( -\\frac{q}{|q|}v_\\perp \\right) \\left( -\\frac{r_L}{2}\\frac{\\partial B_z}{\\partial z} \\right) = -\\frac{1}{2} |q| v_\\perp \\left( \\frac{m v_\\perp}{|q| B_z} \\right) \\frac{\\partial B_z}{\\partial z} = -\\frac{m v_\\perp^2}{2 B_z} \\frac{\\partial B_z}{\\partial z}$$
<p>
Recalling the magnetic moment $\\mu = \\frac{m v_\\perp^2}{2 B}$, the longitudinal force is:
</p>
$$F_\\parallel = -\\mu \\frac{\\partial B}{\\partial s} = -\\mu \\nabla_\\parallel B$$
<p>
This is the fundamental <strong>magnetic mirror force</strong>. Because $\\mu > 0$ and the negative sign is universal, the mirror force always repels charged particles away from regions of stronger magnetic field back toward regions of weaker magnetic field.
</p>
"""
        },
        {
            "id": "sec-3-6",
            "number": "3.6",
            "title": "The First Adiabatic Invariant mu = const, Loss Cone Angle & Magnetic Bottles",
            "content": """
<h3>1. Invariance of the Magnetic Moment</h3>
<p>
The total kinetic energy of a charged particle in a static magnetic field is strictly conserved:
</p>
$$E = E_\\parallel + E_\\perp = \\frac{1}{2}m v_\\parallel^2 + \\frac{1}{2}m v_\\perp^2 = \\frac{1}{2}m v_\\parallel^2 + \\mu B = \\text{const}$$
<p>
Differentiating total energy with respect to time along the trajectory:
</p>
$$\\frac{dE}{dt} = m v_\\parallel \\frac{dv_\\parallel}{dt} + \\frac{d(\\mu B)}{dt} = v_\\parallel F_\\parallel + \\mu \\frac{dB}{dt} + B \\frac{d\\mu}{dt} = 0$$
<p>
Using $F_\\parallel = -\\mu \\frac{\\partial B}{\\partial s}$ and noting that along the orbit $\\frac{dB}{dt} = v_\\parallel \\frac{\\partial B}{\\partial s}$:
</p>
$$v_\\parallel \\left(-\\mu \\frac{\\partial B}{\\partial s}\\right) + \\mu \\left(v_\\parallel \\frac{\\partial B}{\\partial s}\\right) + B \\frac{d\\mu}{dt} = 0 \\implies B \\frac{d\\mu}{dt} = 0$$
<p>
Therefore, the magnetic moment $\\mu$ is an exact <strong>adiabatic invariant</strong>:
</p>
$$\\mu \\equiv \\frac{m v_\\perp^2}{2 B} = \\text{const}$$

<h3>2. The Magnetic Loss Cone</h3>
<p>
As a particle travels into a converging magnetic mirror with minimum field $B_{\\text{min}}$ and maximum field $B_{\\text{max}}$ (mirror ratio $R_m \\equiv B_{\\text{max}} / B_{\\text{min}}$):
</p>
$$v_\\perp^2(s) = v_{\\perp,0}^2 \\frac{B(s)}{B_{\\text{min}}}$$
<p>
By conservation of total energy $v^2 = v_\\parallel^2(s) + v_\\perp^2(s) = v_0^2$:
</p>
$$v_\\parallel^2(s) = v_0^2 - v_{\\perp,0}^2 \\frac{B(s)}{B_{\\text{min}}}$$
<p>
A particle will be reflected at a turning point ($v_\\parallel = 0$) if and only if $B(s)$ reaches a value where $v_\\perp^2 = v_0^2$ before reaching $B_{\\text{max}}$. The threshold pitch angle $\\theta$ at the midplane ($B = B_{\\text{min}}$) defining the boundary between trapped and lost particles is the <strong>loss cone angle</strong> $\\theta_m$:
</p>
$$\\sin^2 \\theta_m = \\frac{v_{\\perp,0}^2}{v_0^2} = \\frac{B_{\\text{min}}}{B_{\\text{max}}} = \\frac{1}{R_m} \\implies \\theta_m = \\arcsin\\left( \\frac{1}{\\sqrt{R_m}} \\right)$$
<p>
Particles with initial pitch angles $\\theta < \\theta_m$ lie inside the loss cone and escape out the ends of the mirror.
</p>
"""
        },
        {
            "id": "sec-3-7",
            "number": "3.7",
            "title": "Higher Adiabatic Invariants: Longitudinal Action J, Flux Invariant Phi & Radiation Belts",
            "content": """
<h3>1. The Hierarchy of Adiabatic Invariants</h3>
<p>
Hamiltonian mechanics dictates that whenever a periodic motion has action integral $J = \\oint p\\,dq$, the action is an adiabatic invariant under slow perturbations:
</p>
<ol>
  <li><strong>First Invariant $\\mu$ (Magnetic Moment):</strong> Associated with fast cyclotron gyration (period $\\tau_c \\sim 10^{-6}\\text{ s}$):
  $$\\mu = \\frac{m v_\\perp^2}{2 B} = \\text{const}$$</li>
  <li><strong>Second Invariant $J$ (Longitudinal Action):</strong> Associated with periodic bounce motion between mirror points (period $\\tau_b \\sim 10^{-2}\\text{ s}$):
  $$J = \\oint v_\\parallel ds = \\text{const}$$</li>
  <li><strong>Third Invariant $\\Phi$ (Magnetic Flux Drift Invariant):</strong> Associated with the slow azimuthal drift of guiding centers around a closed magnetic surface (period $\\tau_d \\sim 10^2\\text{ s}$):
  $$\\Phi = \\oint \\vec{A} \\cdot d\\vec{l} = \\int \\vec{B} \\cdot d\\vec{S} = \\text{const}$$</li>
</ol>

<h3>2. Planetary Magnetospheres & The Van Allen Belts</h3>
<p>
The Earth's dipolar magnetic field naturally traps energetic protons and electrons in the <strong>Van Allen radiation belts</strong>. Trapped particles simultaneously execute:
</p>
<ul>
  <li>Fast cyclotron gyration around dipole field lines ($\tau_c \\sim 1\\;\\mu\\text{s}$).</li>
  <li>North-South bouncing between northern and southern auroral mirror points ($\tau_b \\sim 0.1\\text{ s}$).</li>
  <li>Slow longitudinal drift around the Earth (electrons east, ions west) creating the geomagnetic ring current ($\tau_d \\sim 10\\text{ minutes}$).</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-3-1",
            "title": "Complete Derivation of Gradient-B Drift from Taylor Expansion of Gyration Force over Orbit",
            "statement": """Consider a particle of mass $m$ and charge $q$ moving in a magnetic field directed along $\\hat{z}$ with a constant gradient along $\\hat{y}$: $\\vec{B}(y) = [B_0 + y (dB/dy)]\\hat{z}$.
(a) Write down the instantaneous Lorentz force components $F_x(t)$ and $F_y(t)$ along the unperturbed circular orbit $x(t) = r_L \\sin(\\omega_c t), y(t) = r_L \\cos(\\omega_c t)$ for a positive ion.
(b) Evaluate the orbit-averaged forces $\\langle F_x \\rangle$ and $\\langle F_y \\rangle$ over one full gyration period $\\tau_c = 2\\pi / \\omega_c$.
(c) Apply the general force drift equation to compute the drift velocity vector $\\vec{v}_D$ and show that it identically matches the formula $\\vec{v}_{\\nabla B} = \\frac{m v_\\perp^2}{2 q B^3}(\\vec{B}\\times\\nabla B)$.""",
            "solution": """**(a) Instantaneous Force Components:**
For a positive ion ($q > 0$), the unperturbed gyration orbit around guiding center $(0,0)$ is:
$$x(t) = r_L \\sin(\\omega_c t), \\quad y(t) = r_L \\cos(\\omega_c t)$$
$$v_x(t) = \\dot{x} = r_L \\omega_c \\cos(\\omega_c t) = v_\\perp \\cos(\\omega_c t)$$
$$v_y(t) = \\dot{y} = -r_L \\omega_c \\sin(\\omega_c t) = -v_\\perp \\sin(\\omega_c t)$$
The magnetic field at the particle's position is:
$$\\vec{B}(y) = \\left( B_0 + r_L \\cos(\\omega_c t) \\frac{dB}{dy} \\right) \\hat{z}$$
The Lorentz force is $\\vec{F} = q(\\vec{v}\\times\\vec{B}) = q(v_y B_z \\hat{x} - v_x B_z \\hat{y})$:
$$F_x(t) = q v_y(t) B_z(y(t)) = -q v_\\perp \\sin(\\omega_c t) \\left[ B_0 + r_L \\cos(\\omega_c t)\\frac{dB}{dy} \\right]$$
$$F_y(t) = -q v_x(t) B_z(y(t)) = -q v_\\perp \\cos(\\omega_c t) \\left[ B_0 + r_L \\cos(\\omega_c t)\\frac{dB}{dy} \\right]$$

**(b) Orbit-Averaged Forces:**
Integrate over one period $\\tau_c = 2\\pi / \\omega_c$:
1. For $\\langle F_x \\rangle$:
$$\\langle F_x \\rangle = -q v_\\perp B_0 \\langle \\sin(\\omega_c t) \\rangle - q v_\\perp r_L \\frac{dB}{dy} \\langle \\sin(\\omega_c t)\\cos(\\omega_c t) \\rangle$$
Since $\\langle \\sin(\\omega_c t) \\rangle = 0$ and $\\langle \\sin(\\omega_c t)\\cos(\\omega_c t) \\rangle = \\frac{1}{2}\\langle \\sin(2\\omega_c t) \\rangle = 0$:
$$\\langle F_x \\rangle = 0$$

2. For $\\langle F_y \\rangle$:
$$\\langle F_y \\rangle = -q v_\\perp B_0 \\langle \\cos(\\omega_c t) \\rangle - q v_\\perp r_L \\frac{dB}{dy} \\langle \\cos^2(\\omega_c t) \\rangle$$
Since $\\langle \\cos(\\omega_c t) \\rangle = 0$ and $\\langle \\cos^2(\\omega_c t) \\rangle = \\frac{1}{2}$:
$$\\langle F_y \\rangle = -\\frac{1}{2} q v_\\perp r_L \\frac{dB}{dy}$$
Substitute Larmor radius $r_L = \\frac{m v_\\perp}{q B_0}$:
$$\\langle F_y \\rangle = -\\frac{1}{2} q v_\\perp \\left( \\frac{m v_\\perp}{q B_0} \\right) \\frac{dB}{dy} = -\\frac{m v_\\perp^2}{2 B_0} \\frac{dB}{dy} = -\\mu \\frac{dB}{dy}$$
where $\\mu = \\frac{m v_\\perp^2}{2 B_0}$.

**(c) Drift Velocity Vector Evaluation:**
The net effective force is $\\langle \\vec{F} \\rangle = -\\mu \\frac{dB}{dy} \\hat{y} = -\\mu \\nabla B$.
Using the general force drift equation:
$$\\vec{v}_D = \\frac{1}{q} \\frac{\\langle \\vec{F} \\rangle \\times \\vec{B}}{B_0^2} = \\frac{1}{q B_0^2} \\left( -\\mu \\frac{dB}{dy}\\hat{y} \\times B_0 \\hat{z} \\right)$$
Since $\\hat{y} \\times \\hat{z} = \\hat{x}$:
$$\\vec{v}_D = -\\frac{\\mu B_0}{q B_0^2}\\frac{dB}{dy}\\hat{x} = -\\frac{\\mu}{q B_0}\\frac{dB}{dy}\\hat{x} = -\\frac{m v_\\perp^2}{2 q B_0^2}\\frac{dB}{dy}\\hat{x}$$
Now compute using the standard vector formula $\\vec{v}_{\\nabla B} = \\frac{m v_\\perp^2}{2 q B^3}(\\vec{B}\\times\\nabla B)$:
$$\\vec{B} \\times \\nabla B = (B_0 \\hat{z}) \\times \\left( \\frac{dB}{dy}\\hat{y} \\right) = B_0 \\frac{dB}{dy} (\\hat{z}\\times\\hat{y}) = -B_0 \\frac{dB}{dy}\\hat{x}$$
$$\\vec{v}_{\\nabla B} = \\frac{m v_\\perp^2}{2 q B_0^3}\\left( -B_0 \\frac{dB}{dy}\\hat{x} \\right) = -\\frac{m v_\\perp^2}{2 q B_0^2}\\frac{dB}{dy}\\hat{x}$$
The two derivations match identically, proving the theorem rigorously from first-order perturbation mechanics."""
        },
        {
            "id": "plasma-prob-3-2",
            "title": "Magnetic Mirror Loss Cone Fraction and Critical Pitch Angle for Fusion Confinement Geometry",
            "statement": """A linear magnetic mirror machine has a midplane field $B_{\\text{min}} = 0.50\\text{ Tesla}$ and throat coils generating $B_{\\text{max}} = 2.50\\text{ Tesla}$.
(a) Determine the mirror ratio $R_m$ and calculate the critical loss cone half-angle $\\theta_m$ in degrees.
(b) Assuming an isotropic velocity distribution function $f(\\vec{v}) = f(v)$, compute the fraction of particles $F_{\\text{loss}}$ that lie within the double loss cone and escape out either end.
(c) If a population of deuterium ions ($M_i = 3.34\\times 10^{-27}\\text{ kg}$) is injected at the midplane with total kinetic energy $E = 10.0\\text{ keV}$ at pitch angle $\\theta = 45^\\circ$, determine their turning point magnetic field $B_{\\text{turn}}$ and verify that they are magnetically trapped.""",
            "solution": """**(a) Mirror Ratio and Loss Cone Angle:**
The mirror ratio is:
$$R_m = \\frac{B_{\\text{max}}}{B_{\\text{min}}} = \\frac{2.50\\text{ T}}{0.50\\text{ T}} = 5.0$$
The critical loss cone angle satisfies:
$$\\sin^2 \\theta_m = \\frac{1}{R_m} = \\frac{1}{5.0} = 0.20$$
$$\\sin\\theta_m = \\sqrt{0.20} \\approx 0.4472$$
$$\\theta_m = \\arcsin(0.4472) \\approx 26.565^\\circ \\approx 26.57^\\circ$$

**(b) Loss Fraction for Isotropic Distribution:**
For an isotropic velocity distribution, the velocity space solid angle element is $d\\Omega = 2\\pi \\sin\\theta d\\theta$.
A particle escapes if its pitch angle falls within the forward loss cone ($0 \\le \\theta < \\theta_m$) or the backward loss cone ($\\pi - \\theta_m < \\theta \\le \\pi$).
The solid angle of one loss cone is:
$$\\Omega_{\\text{cone}} = \\int_0^{2\\pi} d\\phi \\int_0^{\\theta_m} \\sin\\theta d\\theta = 2\\pi [1 - \\cos\\theta_m]$$
The total solid angle for both escape cones is $2 \\Omega_{\\text{cone}} = 4\\pi [1 - \\cos\\theta_m]$.
The fraction of lost particles is:
$$F_{\\text{loss}} = \\frac{2\\Omega_{\\text{cone}}}{4\\pi} = 1 - \\cos\\theta_m$$
Since $\\sin\\theta_m = 1/\\sqrt{R_m}$:
$$\\cos\\theta_m = \\sqrt{1 - \\sin^2\\theta_m} = \\sqrt{1 - \\frac{1}{R_m}} = \\sqrt{1 - 0.20} = \\sqrt{0.80} \\approx 0.8944$$
$$F_{\\text{loss}} = 1 - 0.8944 = 0.1056 = 10.56\\%$$
Thus, approximately $10.6\\%$ of an isotropic plasma escapes immediately on the first pass, with the remaining $89.4\\%$ trapped.

**(c) Turning Point of Injected Deuterium Ions:**
Initial pitch angle is $\\theta_0 = 45^\\circ$.
Since $\\theta_0 = 45^\\circ > \\theta_m = 26.57^\\circ$, the ions lie well outside the loss cone and must be trapped!
At the midplane:
$$v_{\\perp,0}^2 = v_0^2 \\sin^2(45^\\circ) = 0.50 v_0^2$$
The magnetic moment is:
$$\\mu = \\frac{m v_{\\perp,0}^2}{2 B_{\\text{min}}} = \\frac{E \\sin^2\\theta_0}{B_{\\text{min}}} = \\frac{(10.0\\text{ keV})(0.50)}{0.50\\text{ T}} = 10.0\\text{ keV/T}$$
At the turning point, all kinetic energy is converted into perpendicular energy ($v_\\parallel = 0, E_\\perp = E$):
$$E = \\mu B_{\\text{turn}} \\implies B_{\\text{turn}} = \\frac{E}{\\mu} = \\frac{10.0\\text{ keV}}{10.0\\text{ keV/T}} = 1.00\\text{ Tesla}$$
Because $B_{\\text{turn}} = 1.00\\text{ T} < B_{\\text{max}} = 2.50\\text{ T}$, the deuterium ions reflect cleanly at the location where $B = 1.00\\text{ T}$, executing stable harmonic bounce oscillations between the two mirror throats."""
        },
        {
            "id": "plasma-prob-3-3",
            "title": "Invariance of Magnetic Moment in Slowly Time-Varying Magnetic Fields",
            "statement": """Consider a charged particle of mass $m$ and charge $q$ gyrating in a spatially uniform magnetic field that increases slowly with time: $\\vec{B}(t) = B(t)\\hat{z}$, with $\\frac{1}{B}\\frac{dB}{dt} \\ll \\omega_c$.
(a) From Faraday's law of induction, calculate the induced azimuthal electric field $E_\\theta$ around the circular gyro-orbit of radius $r_L$.
(b) Compute the net work done by $E_\\theta$ on the particle per cyclotron orbit and calculate the time rate of change of perpendicular kinetic energy $\\frac{dE_\\perp}{dt}$.
(c) Rigorously prove that $\\frac{d}{dt}\\left( \\frac{E_\\perp}{B} \\right) = 0$, confirming the adiabatic invariance of $\\mu = m v_\\perp^2 / (2B)$.""",
            "solution": """**(a) Induced Azimuthal Electric Field:**
By Faraday's law of electromagnetic induction in integral form:
$$\\oint \\vec{E} \\cdot d\\vec{l} = -\\frac{d\\Phi_B}{dt} = -\\frac{d}{dt}\\int \\vec{B}\\cdot d\\vec{S}$$
For a circular contour of radius $r_L$ centered on the guiding center:
$$\\oint \\vec{E} \\cdot d\\vec{l} = E_\\theta (2\\pi r_L) = -\\frac{d}{dt}(\\pi r_L^2 B) = -\\pi r_L^2 \\frac{dB}{dt}$$
(since $r_L$ changes slowly on the cyclotron timescale $\\tau_c$).
Solving for the induced electric field:
$$E_\\theta = -\\frac{r_L}{2}\\frac{dB}{dt}$$

**(b) Work Done per Orbit & Rate of Energy Gain:**
The work done by the electric field on the particle during one complete gyration is:
$$\\Delta E_\\perp = \\oint q \\vec{E}\\cdot d\\vec{l} = q E_\\theta (\\pm 2\\pi r_L)$$
Because the sense of gyration of the particle ($q > 0$ counter-clockwise, $q < 0$ clockwise) aligns with the accelerating torque of the induced electric field:
$$\\Delta E_\\perp = |q| |E_\\theta| (2\\pi r_L) = |q| \\left( \\frac{r_L}{2}\\frac{dB}{dt} \\right)(2\\pi r_L) = \\pi |q| r_L^2 \\frac{dB}{dt}$$
Substitute the Larmor radius $r_L = \\frac{v_\\perp}{\\omega_c} = \\frac{m v_\\perp}{|q| B}$:
$$\\pi |q| r_L^2 = \\pi |q| \\left( \\frac{m v_\\perp}{|q| B} \\right)^2 = \\frac{\\pi m^2 v_\\perp^2}{|q| B^2} = \\frac{2\\pi m}{|q| B} \\left( \\frac{1}{2}m v_\\perp^2 \\frac{1}{B} \\right) = \\tau_c \\left( \\frac{E_\\perp}{B} \\right)$$
where $\\tau_c = \\frac{2\\pi}{\\omega_c} = \\frac{2\\pi m}{|q| B}$ is the cyclotron period.
The average time rate of change of perpendicular energy is:
$$\\frac{dE_\\perp}{dt} = \\frac{\\Delta E_\\perp}{\\tau_c} = \\frac{E_\\perp}{B} \\frac{dB}{dt}$$

**(c) Proof of Invariance of $\\mu$:**
Differentiate $\\mu = \\frac{E_\\perp}{B}$ with respect to time using the quotient rule:
$$\\frac{d\\mu}{dt} = \\frac{d}{dt}\\left( \\frac{E_\\perp}{B} \\right) = \\frac{1}{B}\\frac{dE_\\perp}{dt} - \\frac{E_\\perp}{B^2}\\frac{dB}{dt}$$
Substitute the result $\\frac{dE_\\perp}{dt} = \\frac{E_\\perp}{B}\\frac{dB}{dt}$:
$$\\frac{d\\mu}{dt} = \\frac{1}{B}\\left( \\frac{E_\\perp}{B}\\frac{dB}{dt} \\right) - \\frac{E_\\perp}{B^2}\\frac{dB}{dt} = \\frac{E_\\perp}{B^2}\\frac{dB}{dt} - \\frac{E_\\perp}{B^2}\\frac{dB}{dt} = 0$$
This rigorously proves that $\\mu = \\text{const}$ is invariant under slow temporal variations of the magnetic field! As $B$ increases, the perpendicular energy increases proportionally ($E_\\perp \\propto B$) while the Larmor radius compresses ($r_L \\propto B^{-1/2}$), which is the operational basis of **betatron acceleration** and **adiabatic magnetic compression** in fusion devices."""
        }
    ]
}

# =========================================================================
# UNIT 4: PLASMA AS A FLUID & MAGNETOHYDRODYNAMICS (MHD)
# =========================================================================

unit4_data = {
    "unitId": "unit4-plasma",
    "title": "Plasma as a Fluid: The Dielectric Multi-Fluid Equations & MHD",
    "subtitle": "Continuity, Momentum Balance, Diamagnetic Drift & Flux Freezing",
    "summary": "Macroscopic fluid description of plasma: velocity moments of the Boltzmann equation, continuity equation, momentum balance with pressure tensor and collisional friction, equation of state, the plasma approximation and quasi-neutrality, fluid diamagnetic drift velocity and magnetization current, derivation of single-fluid Magnetohydrodynamics (MHD), generalized Ohm's law, magnetic induction equation, magnetic Reynolds number, Alfvén's magnetic flux-freezing theorem, magnetic pressure and tension, and the plasma beta parameter.",
    "sections": [
        {
            "id": "sec-4-1",
            "number": "4.1",
            "title": "Macroscopic Fluid Transition: Velocity Moments of the Kinetic Boltzmann Equation",
            "content": """
<h3>1. From Microscopic Distribution to Fluid Fields</h3>
<p>
Tracking $10^{20}$ individual charged particles through single-particle equations of motion is computationally intractable. In the fluid description, we average over velocity space by taking moments of the phase space distribution function $f_\\alpha(\\vec{r}, \\vec{v}, t)$:
</p>
$$\\langle \\chi \\rangle_\\alpha = \\frac{1}{n_\\alpha} \\int \\chi(\\vec{v}) f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v$$
<p>
The fundamental macroscopic fluid variables are:
</p>
<ul>
  <li><strong>Number Density (Zeroth Moment):</strong>
  $$n_\\alpha(\\vec{r}, t) = \\int f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v$$</li>
  <li><strong>Mean Fluid Velocity (First Moment):</strong>
  $$\\vec{u}_\\alpha(\\vec{r}, t) = \\langle \\vec{v} \\rangle = \\frac{1}{n_\\alpha} \\int \\vec{v} f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v$$</li>
  <li><strong>Stress Tensor (Second Moment):</strong>
  $$\\mathbf{P}_\\alpha(\\vec{r}, t) = m_\\alpha \\int (\\vec{v} - \\vec{u}_\\alpha)(\\vec{v} - \\vec{u}_\\alpha) f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v$$</li>
</ul>
"""
        },
        {
            "id": "sec-4-2",
            "number": "4.2",
            "title": "Zeroth & First Velocity Moments: Fluid Continuity & Momentum Balance Equations",
            "content": """
<h3>1. The Continuity Equation (Zeroth Moment)</h3>
<p>
Integrating the Boltzmann equation over all velocity space $d^3v$:
</p>
$$\\int \\left[ \\frac{\\partial f_\\alpha}{\\partial t} + \\nabla \\cdot (\\vec{v} f_\\alpha) + \\frac{q_\\alpha}{m_\\alpha}\\nabla_v \\cdot \\left( (\\vec{E} + \\vec{v}\\times\\vec{B})f_\\alpha \\right) \\right] d^3v = \\int \\left( \\frac{\\partial f_\\alpha}{\\partial t} \\right)_{\\text{coll}} d^3v$$
<p>
Assuming elastic collisions that conserve particle number:
</p>
$$\\frac{\\partial n_\\alpha}{\\partial t} + \\nabla \\cdot (n_\\alpha \\vec{u}_\\alpha) = 0$$

<h3>2. The Fluid Momentum Equation (First Moment)</h3>
<p>
Multiplying the Boltzmann equation by $m_\\alpha \\vec{v}$ and integrating over velocity space:
</p>
$$m_\\alpha n_\\alpha \\left[ \\frac{\\partial \\vec{u}_\\alpha}{\\partial t} + (\\vec{u}_\\alpha \\cdot \\nabla)\\vec{u}_\\alpha \\right] = q_\\alpha n_\\alpha (\\vec{E} + \\vec{u}_\\alpha \\times \\vec{B}) - \\nabla \\cdot \\mathbf{P}_\\alpha + \\vec{R}_{\\alpha\\beta}$$
<p>
where $\\vec{R}_{\\alpha\\beta} = -m_\\alpha n_\\alpha \\nu_{\\alpha\\beta}(\\vec{u}_\\alpha - \\vec{u}_\\beta)$ represents the inter-species collisional frictional drag.
</p>
"""
        },
        {
            "id": "sec-4-3",
            "number": "4.3",
            "title": "Second Velocity Moment, Scalar Pressure Approximations & Polytropic Equations of State",
            "content": """
<h3>1. Scalar Pressure & The Closure Problem</h3>
<p>
Each moment equation contains the next higher moment: continuity contains fluid velocity $\\vec{u}$, momentum contains the pressure tensor $\\mathbf{P}$, and energy contains the heat flux tensor $\\vec{Q}$. This is the famous <strong>closure problem</strong> of kinetic theory.
</p>
<p>
To close the fluid equations, we assume an isotropic velocity distribution, reducing the stress tensor to a scalar pressure:
</p>
$$\\mathbf{P}_\\alpha = P_\\alpha \\mathbf{I} \\implies \\nabla \\cdot \\mathbf{P}_\\alpha = \\nabla P_\\alpha$$
<p>
where $P_\\alpha = n_\\alpha k_B T_\\alpha$ is the ideal gas equation of state.
</p>

<h3>2. Polytropic Equation of State</h3>
<p>
The thermodynamic response is modeled by the polytropic relation:
</p>
$$P_\\alpha n_\\alpha^{-\\gamma} = \\text{const} \\iff \\nabla P_\\alpha = \\gamma k_B T_\\alpha \\nabla n_\\alpha$$
<p>
where:
</p>
<ul>
  <li>$\\gamma = 1$: Isothermal compression (rapid thermal conduction along field lines).</li>
  <li>$\\gamma = 5/3$: Adiabatic compression in 3 dimensions ($C_p / C_v = (d+2)/d = 5/3$).</li>
  <li>$\\gamma = 3$: Adiabatic compression in 1 dimension along strong magnetic field lines ($d=1$).</li>
</ul>
"""
        },
        {
            "id": "sec-4-4",
            "number": "4.4",
            "title": "The Plasma Approximation: Quasi-Neutrality with Non-Vanishing Electric Fields",
            "content": """
<h3>1. The Apparent Paradox of Quasi-Neutrality</h3>
<p>
In fluid plasma physics, we universally employ the <strong>plasma approximation</strong>:
</p>
$$n_e \\approx Z n_i \\equiv n$$
<p>
However, Poisson's equation states $\\nabla \\cdot \\vec{E} = \\frac{e(n_i - n_e)}{\\varepsilon_0}$. If $n_e = n_i$, one might naively conclude that $\\nabla \\cdot \\vec{E} = 0$, implying that electrostatic fields cannot exist inside a plasma!
</p>

<h3>2. Resolution of the Paradox</h3>
<p>
The paradox is resolved by recognizing that the fractional charge imbalance $\\delta n / n = |n_i - n_e| / n_0$ required to create enormous macroscopic electric fields is vanishingly small:
</p>
$$\\frac{\\delta n}{n_0} = \\frac{\\varepsilon_0 \\nabla \\cdot \\vec{E}}{e n_0} \\sim \\frac{\\varepsilon_0 (E/L)}{e n_0} \\sim \\left( \\frac{\\lambda_D}{L} \\right)^2 \\ll 1$$
<p>
Because $\\lambda_D / L \\sim 10^{-4}$ in typical laboratory plasmas, a fractional charge imbalance of only 1 part in $10^8$ creates millions of volts per meter! Therefore, in the fluid momentum equations we safely set $n_e = n_i = n$ everywhere except inside Poisson's equation itself. In practice, we determine $\\vec{E}$ directly from the fluid equations of motion rather than from Poisson's equation.
</p>
"""
        },
        {
            "id": "sec-4-5",
            "number": "4.5",
            "title": "Fluid Drifts: Derivation of the Diamagnetic Drift Velocity v_D and Magnetization Current",
            "content": """
<h3>1. The Steady-State Perpendicular Fluid Equation</h3>
<p>
Consider a steady-state ($\\partial / \\partial t = 0$), low-velocity ($(\\vec{u}\\cdot\\nabla)\\vec{u} \\approx 0$), collisionless fluid equilibrium in a uniform magnetic field $\\vec{B}$:
</p>
$$0 = q n (\\vec{E} + \\vec{u}_\\perp \\times \\vec{B}) - \\nabla P$$
<p>
Taking the vector cross product with $\\vec{B}$:
</p>
$$q n \\vec{E} \\times \\vec{B} + q n (\\vec{u}_\\perp \\times \\vec{B}) \\times \\vec{B} - \\nabla P \\times \\vec{B} = 0$$
<p>
Using $(\\vec{u}_\\perp \\times \\vec{B}) \\times \\vec{B} = -B^2 \\vec{u}_\\perp$ and solving for $\\vec{u}_\\perp$:
</p>
$$\\vec{u}_\\perp = \\frac{\\vec{E} \\times \\vec{B}}{B^2} - \\frac{\\nabla P \\times \\vec{B}}{q n B^2} = \\vec{v}_E + \\vec{v}_D$$

<h3>2. The Diamagnetic Drift Velocity</h3>
<p>
The second term is the <strong>diamagnetic drift velocity</strong> $\\vec{v}_D$:
</p>
$$\\vec{v}_D \\equiv -\\frac{\\nabla P \\times \\vec{B}}{q n B^2}$$
<p>
Fundamental properties of diamagnetic drift:
</p>
<ul>
  <li><strong>Not a Single-Particle Guiding Center Drift:</strong> Individual guiding centers do not drift with velocity $\\vec{v}_D$! $\\vec{v}_D$ is a purely macroscopic fluid effect: in the presence of a density or pressure gradient, more particles gyrate across an area element in one direction than in the reverse, resulting in a net fluid flux.</li>
  <li><strong>Charge Dependence:</strong> Ions and electrons drift in opposite directions, driving a net macroscopic <strong>diamagnetic current</strong> $\\vec{J}_D$:
  $$\\vec{J}_D = n e (\\vec{v}_{Di} - \\vec{v}_{De}) = -\\frac{(\\nabla P_i + \\nabla P_e) \\times \\vec{B}}{B^2} = -\\frac{\\nabla P \\times \\vec{B}}{B^2}$$</li>
</ul>
"""
        },
        {
            "id": "sec-4-6",
            "number": "4.6",
            "title": "Single-Fluid Ideal Magnetohydrodynamics (MHD): Center-of-Mass Equations & Generalized Ohm's Law",
            "content": """
<h3>1. Single-Fluid Center-of-Mass Variables</h3>
<p>
Combining electron and ion fluid equations yields the single-fluid Magnetohydrodynamic (MHD) description:
</p>
$$\\rho_m \\equiv n_i M_i + n_e m_e \\approx n M_i, \\quad \\vec{v} \\equiv \\frac{M_i \\vec{u}_i + m_e \\vec{u}_e}{M_i + m_e} \\approx \\vec{u}_i$$
$$\\vec{J} \\equiv n e (\\vec{u}_i - \\vec{u}_e), \\quad P \\equiv P_i + P_e$$

<h3>2. The Ideal MHD Equations</h3>
<p>
Adding the electron and ion momentum equations yields the <strong>MHD equation of motion</strong>:
</p>
$$\\rho_m \\left[ \\frac{\\partial \\vec{v}}{\\partial t} + (\\vec{v} \\cdot \\nabla)\\vec{v} \\right] = \\vec{J} \\times \\vec{B} - \\nabla P$$
<p>
Subtracting the electron equation from the ion equation (and neglecting small electron inertia terms) yields the <strong>generalized Ohm's law</strong>:
</p>
$$\\vec{E} + \\vec{v} \\times \\vec{B} = \\eta \\vec{J} + \\frac{1}{n e}\\vec{J}\\times\\vec{B} - \\frac{1}{n e}\\nabla P_e$$
<p>
In <strong>ideal MHD</strong>, resistivity $\\eta \\to 0$, Hall effect, and electron pressure gradient terms are neglected, yielding the simple ideal Ohm's law:
</p>
$$\\vec{E} + \\vec{v} \\times \\vec{B} = 0$$
"""
        },
        {
            "id": "sec-4-7",
            "number": "4.7",
            "title": "The Magnetic Induction Equation, Alfven's Flux-Freezing Theorem & The Plasma Beta",
            "content": """
<h3>1. The Magnetic Induction Equation</h3>
<p>
Combining Faraday's law $\\frac{\\partial \\vec{B}}{\\partial t} = -\\nabla \\times \\vec{E}$ with Ohm's law $\\vec{E} = -\\vec{v}\\times\\vec{B} + \\eta \\vec{J}$ and Ampère's law $\\mu_0 \\vec{J} = \\nabla \\times \\vec{B}$:
</p>
$$\\frac{\\partial \\vec{B}}{\\partial t} = \\nabla \\times (\\vec{v} \\times \\vec{B}) + \\frac{\\eta}{\\mu_0} \\nabla^2 \\vec{B}$$
<p>
The ratio of the convective (advective) term to the resistive diffusion term defines the <strong>magnetic Reynolds number</strong> $R_m$:
</p>
$$R_m \\equiv \\frac{|\\nabla \\times (\\vec{v}\\times\\vec{B})|}{|(\\eta/\\mu_0)\\nabla^2\\vec{B}|} = \\frac{v L}{\\eta_m} = \\frac{\\mu_0 v L}{\\eta}$$
<p>
In high-temperature fusion plasmas and astrophysical systems ($L \\sim 10^6\\text{ m}$, $T \\sim 10^7\\text{ K}$), $R_m \\gg 10^6$, rendering resistivity entirely negligible.
</p>

<h3>2. Alfvén's Flux-Freezing Theorem</h3>
<p>
When $R_m \\to \\infty$, the magnetic flux $\\Phi = \\int_S \\vec{B}\\cdot d\\vec{S}$ through any closed fluid contour moving with the plasma velocity $\\vec{v}$ is strictly conserved in time:
</p>
$$\\frac{d\\Phi}{dt} = 0$$
<p>
This is <strong>Hannes Alfvén's Flux-Freezing Theorem</strong>: the magnetic field lines are "frozen into" the fluid and move synchronously with the plasma.
</p>

<h3>3. Magnetic Pressure, Magnetic Tension & The Plasma Beta</h3>
<p>
Using the vector identity $(\\nabla \\times \\vec{B}) \\times \\vec{B} = (\\vec{B}\\cdot\\nabla)\\vec{B} - \\nabla(B^2/2)$:
</p>
$$\\vec{J} \\times \\vec{B} = \\frac{1}{\\mu_0}(\\nabla \\times \\vec{B}) \\times \\vec{B} = -\\nabla\\left( \\frac{B^2}{2\\mu_0} \\right) + \\frac{(\\vec{B}\\cdot\\nabla)\\vec{B}}{\\mu_0}$$
<p>
The Lorentz force decomposes into:
</p>
<ul>
  <li><strong>Magnetic Pressure:</strong> $P_{\\text{mag}} = \\frac{B^2}{2\\mu_0}$ (isotropic perpendicular expansion force).</li>
  <li><strong>Magnetic Tension:</strong> $\\frac{(\\vec{B}\\cdot\\nabla)\\vec{B}}{\\mu_0} = \\frac{B^2}{\\mu_0}\\frac{\\hat{R}_c}{R_c}$ (restoring force along curved field lines).</li>
</ul>
<p>
The ratio of thermal kinetic pressure to magnetic pressure is the fundamental <strong>plasma beta</strong> parameter $\\beta$:
</p>
$$\\beta \\equiv \\frac{P_{\\text{thermal}}}{P_{\\text{magnetic}}} = \\frac{n k_B(T_e + T_i)}{B^2 / (2\\mu_0)} = \\frac{2\\mu_0 n k_B T}{B^2}$$
<p>
In tokamaks, $\\beta \\sim 0.05$ (low-beta magnetically dominated); in the solar photosphere, $\\beta \\sim 1$; and in the solar wind, $\\beta \\sim 1\\text{ to }10$.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-4-1",
            "title": "Mathematical Demonstration of Diamagnetic Current and Cancellation with Guiding Center Drifts",
            "statement": """Consider a slab of collisionless plasma in a uniform magnetic field $\\vec{B} = B_0 \\hat{z}$, with a density gradient along $\\hat{x}$: $n(x) = n_0(1 + x / L_n)$, and uniform isothermal temperature $T_e = T_i = T_0$.
(a) Compute the diamagnetic drift velocity $\\vec{v}_D$ for electrons and ions.
(b) Evaluate the macroscopic diamagnetic current density $\\vec{J}_D$.
(c) Compute the single-particle guiding center drift velocity $\\vec{v}_{\\text{gc}}$ and explain why individual guiding centers do not move while the fluid sustains a non-zero current.""",
            "solution": """**(a) Diamagnetic Drift Velocities:**
The pressure is $P_\\alpha(x) = n(x) k_B T_0$.
The pressure gradient is:
$$\\nabla P_\\alpha = \\frac{dP_\\alpha}{dx}\\hat{x} = \\frac{n_0 k_B T_0}{L_n}\\hat{x} = \\frac{P_0}{L_n}\\hat{x}$$
The diamagnetic drift velocity formula is:
$$\\vec{v}_{D\\alpha} = -\\frac{\\nabla P_\\alpha \\times \\vec{B}}{q_\\alpha n(x) B^2}$$
With $\\vec{B} = B_0 \\hat{z}$:
$$\\nabla P_\\alpha \\times \\vec{B} = \\left( \\frac{P_0}{L_n}\\hat{x} \\right) \\times (B_0 \\hat{z}) = -\\frac{P_0 B_0}{L_n}\\hat{y}$$
1. **For Ions ($q = +e$):**
$$\\vec{v}_{Di} = -\\frac{-(P_0 B_0 / L_n)\\hat{y}}{e n(x) B_0^2} = +\\frac{k_B T_0}{e B_0 L_n}\\hat{y}$$
2. **For Electrons ($q = -e$):**
$$\\vec{v}_{De} = -\\frac{-(P_0 B_0 / L_n)\\hat{y}}{(-e) n(x) B_0^2} = -\\frac{k_B T_0}{e B_0 L_n}\\hat{y}$$
Ions drift in the $+\\hat{y}$ direction, while electrons drift in the $-\\hat{y}$ direction.

**(b) Diamagnetic Current Density $\\vec{J}_D$:**
$$\\vec{J}_D = n(x) e (\\vec{v}_{Di} - \\vec{v}_{De}) = n(x) e \\left[ \\frac{k_B T_0}{e B_0 L_n}\\hat{y} - \\left( -\\frac{k_B T_0}{e B_0 L_n}\\hat{y} \\right) \\right]$$
$$\\vec{J}_D = \\frac{2 n(x) k_B T_0}{B_0 L_n}\\hat{y} = \\frac{2 P(x)}{B_0 L_n}\\hat{y} = -\\frac{\\nabla(P_i + P_e)\\times\\vec{B}}{B_0^2}$$
The net current flows in the $+\\hat{y}$ direction.

**(c) Single-Particle Guiding Center Drift Comparison:**
In a spatially uniform magnetic field $\\vec{B} = B_0\\hat{z}$ with zero electric field ($\\vec{E} = 0$):
$$\\nabla B = 0, \\quad \\vec{R}_c \\to \\infty, \\quad \\vec{E} = 0$$
Therefore, all single-particle guiding center drifts are strictly zero:
$$\\vec{v}_{\\text{gc}} = \\vec{v}_E + \\vec{v}_{\\nabla B} + \\vec{v}_c = 0$$
**Physical Explanation:**
The individual guiding centers remain completely stationary. The non-vanishing fluid current $\\vec{J}_D$ arises entirely because each gyrating particle represents a microscopic magnetic dipole of moment $\\vec{\\mu} = -\\frac{m v_\\perp^2}{2 B_0}\\hat{z}$.
In the presence of a density gradient, the macroscopic magnetization is non-uniform: $\\vec{M}(x) = n(x) \\langle \\vec{\\mu} \\rangle = -\\frac{P(x)}{B_0}\\hat{z}$.
By Maxwell's equations, a spatially varying magnetization produces a bound magnetization current:
$$\\vec{J}_{\\text{mag}} = \\nabla \\times \\vec{M} = \\nabla \\times \\left( -\\frac{P(x)}{B_0}\\hat{z} \\right) = -\\frac{1}{B_0}\\frac{dP}{dx}(\\hat{x}\\times\\hat{z}) = +\\frac{1}{B_0}\\frac{dP}{dx}\\hat{y} = \\vec{J}_D$$
This rigorously proves that the fluid diamagnetic current is identical to the microscopic magnetization current of stationary gyrating orbits."""
        },
        {
            "id": "plasma-prob-4-2",
            "title": "Rigorous Proof of Alfven's Magnetic Flux-Freezing Theorem from Ideal Ohm's Law",
            "statement": """Let $S(t)$ be an open surface bounded by a closed fluid contour $C(t)$ that moves along with the ideal plasma velocity field $\\vec{v}(\\vec{r}, t)$. The magnetic flux through $S(t)$ is $\\Phi(t) = \\int_{S(t)} \\vec{B}(\\vec{r}, t) \\cdot d\\vec{S}$.
(a) Using Leibniz's Reynolds transport theorem for moving surfaces, express the total time derivative $\\frac{d\\Phi}{dt}$ in terms of $\\frac{\\partial\\vec{B}}{\\partial t}$, $\\vec{v}$, and $\\vec{B}$.
(b) Apply Faraday's law of induction and the ideal Ohm's law $\\vec{E} + \\vec{v}\\times\\vec{B} = 0$.
(c) Prove rigorously that $\\frac{d\\Phi}{dt} = 0$, and explain the physical consequence for plasma transport across magnetic field lines.""",
            "solution": """**(a) Reynolds Transport Theorem for Magnetic Flux:**
For a surface $S(t)$ whose boundary contour $C(t)$ moves with velocity $\\vec{v}$, the rate of change of flux consists of the intrinsic field variation plus the flux swept out by the moving boundary $d\\vec{l} \\times (\\vec{v} dt)$:
$$\\frac{d\\Phi}{dt} = \\frac{d}{dt}\\int_{S(t)} \\vec{B} \\cdot d\\vec{S} = \\int_{S(t)} \\frac{\\partial\\vec{B}}{\\partial t} \\cdot d\\vec{S} + \\oint_{C(t)} \\vec{B} \\cdot (\\vec{v} \\times d\\vec{l})$$
Using the vector scalar triple product identity $\\vec{A}\\cdot(\\vec{B}\\times\\vec{C}) = -(\\vec{B}\\times\\vec{A})\\cdot\\vec{C}$:
$$\\vec{B} \\cdot (\\vec{v} \\times d\\vec{l}) = -(\\vec{v} \\times \\vec{B}) \\cdot d\\vec{l}$$
Substituting this identity:
$$\\frac{d\\Phi}{dt} = \\int_{S(t)} \\frac{\\partial\\vec{B}}{\\partial t} \\cdot d\\vec{S} - \\oint_{C(t)} (\\vec{v} \\times \\vec{B}) \\cdot d\\vec{l}$$
Applying Stokes' theorem to the closed line integral $\\oint_C (\\vec{v}\\times\\vec{B})\\cdot d\\vec{l} = \\int_S [\\nabla \\times (\\vec{v}\\times\\vec{B})] \\cdot d\\vec{S}$:
$$\\frac{d\\Phi}{dt} = \\int_{S(t)} \\left[ \\frac{\\partial\\vec{B}}{\\partial t} - \\nabla \\times (\\vec{v} \\times \\vec{B}) \\right] \\cdot d\\vec{S}$$

**(b) Application of Faraday's Law & Ideal Ohm's Law:**
From Faraday's law of induction:
$$\\frac{\\partial\\vec{B}}{\\partial t} = -\\nabla \\times \\vec{E}$$
In ideal MHD, the electric field is governed by the ideal Ohm's law:
$$\\vec{E} + \\vec{v} \\times \\vec{B} = 0 \\implies \\vec{E} = -(\\vec{v} \\times \\vec{B})$$
Taking the curl of this electric field:
$$\\nabla \\times \\vec{E} = -\\nabla \\times (\\vec{v} \\times \\vec{B})$$
Substituting into Faraday's law:
$$\\frac{\\partial\\vec{B}}{\\partial t} = -[-\\nabla \\times (\\vec{v} \\times \\vec{B})] = \\nabla \\times (\\vec{v} \\times \\vec{B})$$
$$\\frac{\\partial\\vec{B}}{\\partial t} - \\nabla \\times (\\vec{v} \\times \\vec{B}) = 0$$

**(c) Proof and Physical Consequence:**
Substituting the induction relation into the transport theorem:
$$\\frac{d\\Phi}{dt} = \\int_{S(t)} \\left[ 0 \\right] \\cdot d\\vec{S} = 0$$
This rigorously proves **Alfvén's Theorem**: the magnetic flux linking any fluid element is strictly invariant in time.
**Physical Consequence:**
In an ideal plasma, fluid particles that initially share a given magnetic field line remain permanently tied to that same field line throughout all subsequent motion. Plasma cannot diffuse across magnetic field lines, and magnetic field lines cannot slip through the plasma. Any compression, stretching, or twisting of the fluid forces an identical deformation of the embedded magnetic field lines."""
        },
        {
            "id": "plasma-prob-4-3",
            "title": "Radial Magnetohydrodynamic Equilibrium: Bennett Pinch Current Criterion and Plasma Beta",
            "statement": """A cylindrical plasma column of radius $a$ carries an axial current density $J_z(r) \\hat{z}$ that generates an azimuthal magnetic field $B_\\theta(r) \\hat{\\theta}$. The system is in steady-state radial magnetohydrodynamic equilibrium: $\\nabla P = \\vec{J} \\times \\vec{B}$.
(a) Write down the radial component of the force balance equation in cylindrical coordinates.
(b) Multiply by $r^2$ and integrate from $r=0$ to $r=a$ (with $P(a) = 0$) to derive the famous **Bennett pinch relation**:
$$I^2 = \\frac{8\\pi}{\\mu_0} N k_B(T_e + T_i)$$
where $I$ is the total axial current and $N = \\int_0^a 2\\pi r n(r) dr$ is the number of particles per unit length.
(c) For a fusion Z-pinch with linear density $N = 2.0 \\times 10^{19}\\text{ m}^{-1}$ and equal temperatures $k_B T_e = k_B T_i = 5.0\\text{ keV}$, calculate the critical axial current $I$ required for magnetic self-confinement.""",
            "solution": """**(a) Radial Force Balance Equation:**
In cylindrical coordinates with radial symmetry, the pressure gradient is $\\nabla P = \\frac{dP}{dr}\\hat{r}$.
The current density is $\\vec{J} = J_z(r)\\hat{z}$, and the magnetic field is $\\vec{B} = B_\\theta(r)\\hat{\\theta}$.
The Lorentz force is:
$$\\vec{J}\\times\\vec{B} = (J_z \\hat{z}) \\times (B_\\theta \\hat{\\theta}) = -J_z B_\\theta \\hat{r}$$
The radial force balance $\\nabla P = \\vec{J}\\times\\vec{B}$ requires:
$$\\frac{dP}{dr} = -J_z(r) B_\\theta(r)$$
From Ampère's law in integral form:
$$\\mu_0 I(r) = 2\\pi r B_\\theta(r) \\implies B_\\theta(r) = \\frac{\\mu_0}{2\\pi r}\\int_0^r 2\\pi r' J_z(r') dr'$$
In differential form: $J_z(r) = \\frac{1}{\\mu_0 r}\\frac{d}{dr}(r B_\\theta)$.
Substituting into force balance:
$$\\frac{dP}{dr} = -\\frac{B_\\theta}{\\mu_0 r}\\frac{d}{dr}(r B_\\theta) = -\\frac{B_\\theta^2}{\\mu_0 r} - \\frac{B_\\theta}{\\mu_0}\\frac{dB_\\theta}{dr} = -\\frac{1}{2\\mu_0 r^2}\\frac{d}{dr}(r^2 B_\\theta^2)$$

**(b) Derivation of the Bennett Relation:**
Multiply both sides of $\\frac{dP}{dr} = -J_z B_\\theta$ by $r^2$ and integrate from $0$ to $a$:
$$\\int_0^a r^2 \\frac{dP}{dr} dr = -\\int_0^a r^2 J_z B_\\theta dr$$
Integrate the left side by parts with $u = r^2, dv = dP$:
$$\\int_0^a r^2 \\frac{dP}{dr} dr = [r^2 P(r)]_0^a - \\int_0^a 2r P(r) dr$$
At the boundaries, $r=0$ gives zero, and at $r=a$, the plasma pressure vanishes ($P(a) = 0$). Thus:
$$\\int_0^a r^2 \\frac{dP}{dr} dr = -2\\int_0^a r P(r) dr = -\\frac{1}{\\pi}\\int_0^a 2\\pi r P(r) dr$$
The total line-integrated thermal energy per unit length is:
$$\\int_0^a 2\\pi r P(r) dr = \\int_0^a 2\\pi r n(r) k_B(T_e + T_i) dr = N k_B(T_e + T_i)$$
Therefore, the left side evaluates to:
$$\\int_0^a r^2 \\frac{dP}{dr} dr = -\\frac{1}{\\pi} N k_B(T_e + T_i)$$
Now evaluate the right side: substitute $J_z = \\frac{1}{\\mu_0 r}\\frac{d(r B_\\theta)}{dr}$:
$$-\\int_0^a r^2 J_z B_\\theta dr = -\\frac{1}{\\mu_0}\\int_0^a (r B_\\theta) \\frac{d(r B_\\theta)}{dr} dr = -\\frac{1}{2\\mu_0}[(r B_\\theta)^2]_0^a = -\\frac{1}{2\\mu_0} (a B_\\theta(a))^2$$
At the outer boundary $r = a$, by Ampère's law $2\\pi a B_\\theta(a) = \\mu_0 I \\implies a B_\\theta(a) = \\frac{\\mu_0 I}{2\\pi}$.
Substituting this result:
$$-\\frac{1}{2\\mu_0}\\left( \\frac{\\mu_0 I}{2\\pi} \\right)^2 = -\\frac{\\mu_0 I^2}{8\\pi^2}$$
Equating both sides:
$$-\\frac{1}{\\pi} N k_B(T_e + T_i) = -\\frac{\\mu_0 I^2}{8\\pi^2}$$
Multiplying by $-8\\pi^2 / \\mu_0$ yields the famous **Bennett pinch relation**:
$$I^2 = \\frac{8\\pi}{\\mu_0} N k_B(T_e + T_i)$$

**(c) Numerical Calculation of Critical Confinement Current:**
Given:
$N = 2.0 \\times 10^{19}\\text{ m}^{-1}$
$k_B(T_e + T_i) = 5.0\\text{ keV} + 5.0\\text{ keV} = 10.0\\text{ keV} = 10.0 \\times 10^3 \\times 1.6022\\times 10^{-19}\\text{ J} = 1.6022 \\times 10^{-15}\\text{ J}$
$\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$
Evaluate $I^2$:
$$I^2 = \\frac{8\\pi}{4\\pi \\times 10^{-7}} (2.0 \\times 10^{19}) (1.6022 \\times 10^{-15}) = (2 \\times 10^7) \\times (3.2044 \\times 10^4) = 6.409 \\times 10^{11}\\text{ A}^2$$
Taking the square root:
$$I = \\sqrt{6.409 \\times 10^{11}} \\approx 8.005 \\times 10^5\\text{ A} \\approx 800\\text{ kA}$$
A tremendous current of approximately **800 kiloamperes** is required for the self-induced magnetic field to balance internal thermal pressure."""
        }
    ]
}

with open("plasma_u3.json", "w", encoding="utf-8") as f:
    json.dump(unit3_data, f, indent=2)
print("plasma_u3.json written successfully")

with open("plasma_u4.json", "w", encoding="utf-8") as f:
    json.dump(unit4_data, f, indent=2)
print("plasma_u4.json written successfully")
