# build_plasma_units_7_8.py
# Generates plasma_u7.json and plasma_u8.json for Plasma Physics Course #17

import json

# =========================================================================
# UNIT 7: MAGNETOHYDRODYNAMIC WAVES & PLASMA INSTABILITIES
# =========================================================================

unit7_data = {
    "unitId": "unit7-plasma",
    "title": "Magnetohydrodynamic Waves & Plasma Instabilities",
    "subtitle": "Shear Alfvén Waves, Magnetosonic Modes, Rayleigh-Taylor & Kink Instabilities",
    "summary": "Comprehensive magnetohydrodynamic wave propagation and macroscopic plasma stability: linearization of the ideal MHD equations, transverse shear Alfvén waves, magnetic tension as an elastic string restoring force, Alfvén velocity, exact magnetic and kinetic energy equipartition, compressional Alfvén waves, fast and slow magnetosonic wave dispersion relations, Friedrichs phase velocity polar diagrams, classification of plasma instabilities, gravitational and acceleration-driven Rayleigh-Taylor instability, magnetic shear stabilization, Kelvin-Helmholtz shear flow instability, and macroscopic tokamak MHD instabilities including sausage, kink, and the Kruskal-Shafranov stability limit.",
    "sections": [
        {
            "id": "sec-7-1",
            "number": "7.1",
            "title": "Linearization of the Ideal Magnetohydrodynamic (MHD) Equations",
            "content": """
<h3>1. The Ideal MHD System</h3>
<p>
Ideal magnetohydrodynamics treats the plasma as an electrically conducting, magnetized single fluid governed by:
</p>
$$\\rho_m \\left[ \\frac{\\partial \\vec{v}}{\\partial t} + (\\vec{v}\\cdot\\nabla)\\vec{v} \\right] = \\vec{J} \\times \\vec{B} - \\nabla P$$
$$\\frac{\\partial \\vec{B}}{\\partial t} = \\nabla \\times (\\vec{v} \\times \\vec{B})$$
$$\\frac{\\partial \\rho_m}{\\partial t} + \\nabla \\cdot (\\rho_m \\vec{v}) = 0$$
$$\\nabla P = c_s^2 \\nabla \\rho_m, \\quad \\vec{J} = \\frac{1}{\\mu_0}\\nabla \\times \\vec{B}, \\quad \\nabla\\cdot\\vec{B} = 0$$
<p>
where $c_s = \\sqrt{\\gamma P_0 / \\rho_0}$ is the adiabatic sound speed.
</p>

<h3>2. First-Order Perturbation Expansion</h3>
<p>
Consider a static, homogeneous equilibrium embedded in a uniform magnetic field:
</p>
$$\\vec{B} = B_0 \\hat{z}, \\quad \\rho_m = \\rho_0, \\quad P = P_0, \\quad \\vec{v}_0 = 0$$
<p>
Applying small harmonic perturbations $\\propto e^{i(\\vec{k}\\cdot\\vec{r} - \\omega t)}$:
</p>
$$-i\\omega \\rho_0 \\vec{v}_1 = \\frac{1}{\\mu_0}(i\\vec{k}\\times\\vec{B}_1)\\times\\vec{B}_0 - i\\vec{k} P_1$$
$$-i\\omega \\vec{B}_1 = i\\vec{k} \\times (\\vec{v}_1 \\times \\vec{B}_0)$$
$$-i\\omega \\rho_1 + i\\rho_0 \\vec{k}\\cdot\\vec{v}_1 = 0 \\implies P_1 = c_s^2 \\rho_1 = \\rho_0 c_s^2 \\frac{\\vec{k}\\cdot\\vec{v}_1}{\\omega}$$
"""
        },
        {
            "id": "sec-7-2",
            "number": "7.2",
            "title": "Shear Alfvén Waves: Magnetic Tension, Plucked Strings & Alfvén Velocity v_A",
            "content": """
<h3>1. The Pure Shear Alfvén Wave</h3>
<p>
Consider incompressible perturbations ($\\nabla \\cdot \\vec{v}_1 = 0 \\implies \\rho_1 = 0, P_1 = 0$) propagating along the magnetic field with $\\vec{k} = k_\\parallel \\hat{z}$.
</p>
<p>
Let the fluid velocity perturb along $\\hat{x}$: $\\vec{v}_1 = v_{1x} \\hat{x}$. The induction equation gives:
</p>
$$-i\\omega \\vec{B}_1 = i k_\\parallel \\hat{z} \\times (v_{1x}\\hat{x} \\times B_0\\hat{z}) = i k_\\parallel B_0 v_{1x} \\hat{x} \\implies \\vec{B}_1 = -\\frac{k_\\parallel B_0}{\\omega} v_{1x} \\hat{x}$$
<p>
The linearized momentum equation becomes:
</p>
$$-i\\omega \\rho_0 v_{1x} \\hat{x} = \\frac{1}{\\mu_0}(i k_\\parallel \\hat{z} \\times B_{1x}\\hat{x})\\times(B_0\\hat{z}) = \\frac{i k_\\parallel B_0}{\\mu_0} B_{1x}\\hat{x}$$
<p>
Substitute $B_{1x} = -\\frac{k_\\parallel B_0}{\\omega} v_{1x}$:
</p>
$$-i\\omega \\rho_0 v_{1x} = \\frac{i k_\\parallel B_0}{\\mu_0}\\left( -\\frac{k_\\parallel B_0}{\\omega} v_{1x} \\right) = -i \\frac{k_\\parallel^2 B_0^2}{\\mu_0 \\omega} v_{1x}$$
<p>
Multiplying by $i\\omega / (\\rho_0 v_{1x})$:
</p>
$$\\omega^2 = \\frac{B_0^2}{\\mu_0 \\rho_0} k_\\parallel^2 \\equiv v_A^2 k_\\parallel^2$$
<p>
where the characteristic propagation speed is the famous <strong>Alfvén velocity</strong> $v_A$:
</p>
$$v_A \\equiv \\frac{B_0}{\\sqrt{\\mu_0 \\rho_0}}$$

<h3>2. The Plucked Magnetic String Analogy</h3>
<p>
A shear Alfvén wave is the magnetohydrodynamic analog of transverse vibrations on a plucked violin string of tension $T$ and mass per unit length $\\mu$: $v = \\sqrt{T / \\mu}$. In a magnetized plasma:
</p>
$$T_{\\text{mag}} = \\frac{B_0^2}{\\mu_0}, \\quad \\text{Inertia} = \\rho_0 \\implies v_A = \\sqrt{\\frac{T_{\\text{mag}}}{\\rho_0}} = \\frac{B_0}{\\sqrt{\\mu_0 \\rho_0}}$$
<p>
Magnetic tension provides the restoring force, while fluid mass density $\\rho_0$ provides the inertia. Shear Alfvén waves carry magnetic and kinetic energy in exact equipartition: $\\frac{1}{2}\\rho_0 v_1^2 = \\frac{B_1^2}{2\\mu_0}$.
</p>
"""
        },
        {
            "id": "sec-7-3",
            "number": "7.3",
            "title": "Compressional Alfvén Waves & Fast/Slow Magnetosonic Waves",
            "content": """
<h3>1. Compressible Oblique Perturbations</h3>
<p>
When the fluid is compressible ($\nabla \\cdot \\vec{v}_1 \\ne 0$) and the wave propagates at an arbitrary angle $\\theta$ relative to $\\vec{B}_0$ ($\vec{k} = k_\\perp \\hat{x} + k_\\parallel \\hat{z}$, with $\\cos\\theta = k_\\parallel / k$):
</p>
<p>
Substituting $\\vec{B}_1$ and $P_1$ into the momentum equation yields the master MHD wave dispersion relation:
</p>
$$\\left( \\frac{\\omega^2}{k^2} - v_A^2 \\cos^2\\theta \\right) \\left[ \\frac{\\omega^4}{k^4} - (v_A^2 + c_s^2)\\frac{\\omega^2}{k^2} + v_A^2 c_s^2 \\cos^2\\theta \\right] = 0$$

<h3>2. The Three Fundamental MHD Modes</h3>
<ol>
  <li><strong>Shear Alfvén Wave (Intermediate Mode):</strong>
  $$\\frac{\\omega^2}{k^2} = v_A^2 \\cos^2\\theta \\implies \\omega = k v_A \\cos\\theta = k_\\parallel v_A$$</li>
  <li><strong>Fast Magnetosonic Wave:</strong>
  $$\\left(\\frac{\\omega}{k}\\right)^2_{\\text{fast}} = \\frac{1}{2}\\left( v_A^2 + c_s^2 + \\sqrt{(v_A^2 + c_s^2)^2 - 4 v_A^2 c_s^2 \\cos^2\\theta} \\right)$$</li>
  <li><strong>Slow Magnetosonic Wave:</strong>
  $$\\left(\\frac{\\omega}{k}\\right)^2_{\\text{slow}} = \\frac{1}{2}\\left( v_A^2 + c_s^2 - \\sqrt{(v_A^2 + c_s^2)^2 - 4 v_A^2 c_s^2 \\cos^2\\theta} \\right)$$</li>
</ol>
<p>
The phase velocities satisfy the strict hierarchy:
</p>
$$v_{ph,\\text{slow}} \\le v_{ph,\\text{Alfvén}} \\le v_{ph,\\text{fast}}$$
"""
        },
        {
            "id": "sec-7-4",
            "number": "7.4",
            "title": "Friedrichs Phase Velocity Diagrams & Magnetosonic Wave Polarization",
            "content": """
<h3>1. Friedrichs Polar Diagrams</h3>
<p>
A polar plot of phase velocity $v_{ph}(\\theta) = \\omega / k$ as a function of propagation angle $\\theta$ relative to the magnetic field $\\vec{B}_0$ is known as a <strong>Friedrichs diagram</strong>:
</p>
<ul>
  <li><strong>Shear Alfvén Wave:</strong> Traces two tangent circles touching at the origin along the magnetic field axis ($v_{ph} = v_A |\\cos\\theta|$). Phase velocity is strictly zero perpendicular to $\\vec{B}_0$ ($\theta = 90^\\circ$).</li>
  <li><strong>Fast Magnetosonic Wave:</strong> Traces an oval (nearly spherical) outer shell. At $\\theta = 90^\\circ$, it propagates at the combined <strong>magnetosonic speed</strong>:
  $$v_{ph,\\text{fast}}(\\theta=90^\\circ) = \\sqrt{v_A^2 + c_s^2}$$
  Here, thermal acoustic pressure and magnetic pressure compress in phase, reinforcing each other.</li>
  <li><strong>Slow Magnetosonic Wave:</strong> Traces two cusped lobes inside the Alfvén circles. At $\\theta = 90^\\circ$, $v_{ph,\\text{slow}} = 0$. Thermal and magnetic pressure compress out of phase, partially canceling.</li>
</ul>
"""
        },
        {
            "id": "sec-7-5",
            "number": "7.5",
            "title": "Introduction to Plasma Instabilities: Free Energy, Hydrodynamic vs Kinetic",
            "content": """
<h3>1. Free Energy and Instability Mechanism</h3>
<p>
A plasma equilibrium is characterized by time-independent macroscopic state variables. If a small initial perturbation $\\psi_1(t) \\propto e^{-i\\omega t}$ has a complex frequency $\\omega = \\omega_r + i\\gamma$:
</p>
$$\\psi_1(t) = \\psi_1(0) e^{-i(\\omega_r + i\\gamma)t} = \\psi_1(0) e^{\\gamma t} e^{-i\\omega_r t}$$
<ul>
  <li>If $\\gamma < 0$: The perturbation is damped; the plasma is <strong>stable</strong>.</li>
  <li>If $\\gamma > 0$: The perturbation grows exponentially with growth rate $\\gamma$; the plasma is <strong>unstable</strong>.</li>
</ul>
<p>
Instabilities are powered by tapping reservoirs of <strong>free energy</strong> stored in the non-equilibrium plasma:
</p>
<ul>
  <li>Spatial gradients: Density $\\nabla n$, temperature $\\nabla T$, or pressure gradients $\\nabla P$.</li>
  <li>Currents and magnetic shear: Non-zero $\\nabla \\times \\vec{B} = \\mu_0 \\vec{J}$.</li>
  <li>Velocity space anisotropy: Non-Maxwellian beams ($v_d > v_{\\text{th}}$) or pitch angle anisotropy ($T_\\perp \\ne T_\\parallel$).</li>
</ul>

<h3>2. Classification of Instabilities</h3>
<ol>
  <li><strong>Macro-Instabilities (MHD / Hydrodynamic):</strong> Driven by macroscopic spatial gradients. Wavelengths are macroscopic ($\\lambda \\gg r_L$). They rapidly destroy global plasma confinement on microsecond timescales (e.g., kink, sausage, Rayleigh-Taylor).</li>
  <li><strong>Micro-Instabilities (Kinetic):</strong> Driven by non-thermal features in velocity space. Wavelengths are microscopic ($\\lambda \\sim r_L, \\lambda_D$). They cause anomalous cross-field transport and turbulent diffusion (e.g., two-stream, drift waves, loss cone modes).</li>
</ol>
"""
        },
        {
            "id": "sec-7-6",
            "number": "7.6",
            "title": "The Gravitational Rayleigh-Taylor Instability & Magnetic Shear Stabilization",
            "content": """
<h3>1. The Plasma Rayleigh-Taylor Instability</h3>
<p>
Consider a dense plasma of mass density $\\rho_0$ supported against gravity $\\vec{g} = -g\\hat{y}$ by a magnetic field $\\vec{B} = B_0\\hat{z}$ or by a lighter fluid below (an "inverted density gradient").
</p>
<p>
If a small rippled perturbation $y_1 \\propto e^{i(k_x x - \\omega t)}$ forms at the interface:
</p>
<ul>
  <li>Ions and electrons experience opposite gravitational drifts:
  $$\\vec{v}_g = \\frac{m}{q}\\frac{\\vec{g}\\times\\vec{B}}{B^2} = -\\frac{m g}{q B}\\hat{x}$$</li>
  <li>Positive ions drift along $-\\hat{x}$; electrons drift along $+\\hat{x}$.</li>
  <li>At ripple crests and troughs, this differential drift accumulates positive charge on one side of a crest and negative charge on the other side.</li>
  <li>This charge separation produces a perturbed electric field $\\vec{E}_1$ along $\\hat{x}$.</li>
  <li>The resulting $\\vec{E}_1 \\times \\vec{B}_0$ drift velocity $\\vec{v}_E = \\frac{\\vec{E}_1\\times\\vec{B}_0}{B_0^2}$ is directed <strong>upward at crests and downward at troughs</strong>!</li>
</ul>
<p>
The $\\vec{E}\\times\\vec{B}$ drift amplifies the initial perturbation, driving runaway exponential growth with classical growth rate:
</p>
$$\\omega^2 = -g k \\implies \\gamma = \\sqrt{g k}$$

<h3>2. Magnetic Field Line Bending Stabilization</h3>
<p>
If the magnetic field possesses a component along the perturbation wavevector $\\vec{k}$ (so that $\\vec{k}\\cdot\\vec{B}_0 \\ne 0$), rippling the interface bends magnetic field lines. Magnetic tension opposes the deformation, modifying the dispersion relation to:
</p>
$$\\omega^2 = -g k + \\frac{(\\vec{k}\\cdot\\vec{B}_0)^2}{\\mu_0 \\rho_0}$$
<p>
The interface is completely stabilized ($\omega^2 \\ge 0$) against Rayleigh-Taylor modes whenever:
</p>
$$\\frac{(\\vec{k}\\cdot\\vec{B}_0)^2}{\\mu_0 \\rho_0} \\ge g k$$
<p>
This magnetic line-tying and shear stabilization is essential for stabilizing solar prominences and inertial confinement fusion (ICF) implosions.
</p>
"""
        },
        {
            "id": "sec-7-7",
            "number": "7.7",
            "title": "Macroscopic Tokamak MHD Instabilities: Kink, Sausage & Kruskal-Shafranov Limit",
            "content": """
<h3>1. Current-Driven MHD Instabilities</h3>
<p>
In a cylindrical current-carrying plasma column (Z-pinch or tokamak), perturbations are decomposed into azimuthal Fourier modes $e^{i(m\\theta - k_z z)}$:
</p>
<ul>
  <li><strong>$m = 0$ Mode (Sausage Instability):</strong> Axisymmetric constrictions along the column. Where the radius narrows ($r < a$), the azimuthal magnetic field $B_\\theta \\propto I/r$ intensifies, increasing magnetic pressure $B_\\theta^2 / (2\\mu_0)$ and pinching the neck even tighter until the column snaps.</li>
  <li><strong>$m = 1$ Mode (Kink Instability):</strong> The entire column bends into a helix. Field lines on the inside of the bend crowd together, raising magnetic pressure, while field lines on the outside spread out, lowering pressure. The net pressure imbalance kicks the bend outward, causing violent helical disruption.</li>
</ul>

<h3>2. The Kruskal-Shafranov Stability Criterion</h3>
<p>
To stabilize the dangerous $m=1$ kink instability in tokamaks, a strong toroidal magnetic field $B_z$ (or $B_\\phi$) is applied along the column. As the column kinks, it is forced to stretch the strong axial field lines, which resists the deformation via magnetic tension.
</p>
<p>
Defining the <strong>safety factor</strong> $q(r)$:
</p>
$$q(r) \\equiv \\frac{r B_z(r)}{R B_\\theta(r)}$$
<p>
where $R$ is the major radius and $r$ is the minor radius. The column is completely stable against the fundamental external kink mode if and only if the safety factor at the plasma edge exceeds unity:
</p>
$$q(a) > 1$$
<p>
This is the celebrated <strong>Kruskal-Shafranov stability limit</strong>. It sets an absolute upper bound on the maximum toroidal current $I_p$ that can be stably driven in any tokamak:
</p>
$$I_p < \\frac{2\\pi a^2 B_z}{\\mu_0 R}$$
<p>
Exceeding this current triggers immediate catastrophic kink disruption.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-7-1",
            "title": "Derivation of the Shear Alfven Wave Dispersion Relation and Magnetic-Kinetic Energy Equipartition",
            "statement": """Consider a homogeneous, incompressible ideal MHD plasma in a uniform background magnetic field $\\vec{B}_0 = B_0 \\hat{z}$ with mass density $\\rho_0$. Let a transverse perturbation propagate along $\\vec{B}_0$ with wavevector $\\vec{k} = k\\hat{z}$ and fluid velocity $\\vec{v}_1 = v_1 \\hat{x} e^{i(k z - \\omega t)}$.
(a) From the linearized induction equation, find the perturbed magnetic field $\\vec{B}_1$.
(b) From the linearized momentum equation, derive the dispersion relation $\\omega^2 = k^2 v_A^2$ and verify the Alfvén velocity formula $v_A = B_0 / \\sqrt{\\mu_0 \\rho_0}$.
(c) Compute the time-averaged kinetic energy density $\\langle u_k \\rangle = \\frac{1}{4}\\rho_0 |v_1|^2$ and magnetic energy density $\\langle u_m \\rangle = \\frac{1}{4\\mu_0}|B_1|^2$, and prove that shear Alfvén waves satisfy exact energy equipartition.""",
            "solution": """**(a) Perturbed Magnetic Field $\\vec{B}_1$:**
From the linearized induction equation:
$$\\frac{\\partial \\vec{B}_1}{\\partial t} = \\nabla \\times (\\vec{v}_1 \\times \\vec{B}_0)$$
With $\\vec{v}_1 = v_1 \\hat{x} e^{i(kz - \\omega t)}$ and $\\vec{B}_0 = B_0 \\hat{z}$:
$$\\vec{v}_1 \\times \\vec{B}_0 = (v_1 \\hat{x}) \\times (B_0 \\hat{z}) = -v_1 B_0 \\hat{y}$$
Taking the curl $\\nabla \\times (\\dots) = i k \\hat{z} \\times (\\dots)$:
$$\\nabla \\times (\\vec{v}_1 \\times \\vec{B}_0) = i k \\hat{z} \\times (-v_1 B_0 \\hat{y}) = -i k v_1 B_0 (\\hat{z}\\times\\hat{y}) = +i k v_1 B_0 \\hat{x}$$
Since $\\frac{\\partial \\vec{B}_1}{\\partial t} = -i\\omega \\vec{B}_1$:
$$-i\\omega \\vec{B}_1 = i k v_1 B_0 \\hat{x} \\implies \\vec{B}_1 = -\\frac{k B_0}{\\omega} v_1 \\hat{x}$$

**(b) Dispersion Relation Derivation:**
For incompressible perturbations, $\\nabla \\cdot \\vec{v}_1 = i k v_{1z} = 0 \\implies P_1 = 0$.
The linearized momentum equation is:
$$\\rho_0 \\frac{\\partial \\vec{v}_1}{\\partial t} = \\vec{J}_1 \\times \\vec{B}_0 = \\frac{1}{\\mu_0}(\\nabla \\times \\vec{B}_1) \\times \\vec{B}_0$$
Compute the curl:
$$\\nabla \\times \\vec{B}_1 = i k \\hat{z} \\times \\left( B_{1x} \\hat{x} \\right) = i k B_{1x} \\hat{y}$$
Now evaluate the Lorentz force:
$$(\\nabla \\times \\vec{B}_1) \\times \\vec{B}_0 = (i k B_{1x} \\hat{y}) \\times (B_0 \\hat{z}) = i k B_0 B_{1x} \\hat{x}$$
Substitute into momentum:
$$-i\\omega \\rho_0 v_1 \\hat{x} = \\frac{1}{\\mu_0} i k B_0 B_{1x} \\hat{x} \\implies -i\\omega \\rho_0 v_1 = \\frac{i k B_0}{\\mu_0} B_{1x}$$
Substitute $B_{1x} = -\\frac{k B_0}{\\omega} v_1$:
$$-i\\omega \\rho_0 v_1 = \\frac{i k B_0}{\\mu_0} \\left( -\\frac{k B_0}{\\omega} v_1 \\right) = -i \\frac{k^2 B_0^2}{\\mu_0 \\omega} v_1$$
Divide by $-i v_1 / \\omega$:
$$\\omega^2 \\rho_0 = \\frac{k^2 B_0^2}{\\mu_0} \\implies \\omega^2 = k^2 \\left( \\frac{B_0^2}{\\mu_0 \\rho_0} \\right) = k^2 v_A^2$$
where $v_A = \\frac{B_0}{\\sqrt{\\mu_0 \\rho_0}}$ is the Alfvén velocity.

**(c) Proof of Energy Equipartition:**
The time-averaged kinetic energy density of the fluid perturbation is:
$$\\langle u_k \\rangle = \\frac{1}{4}\\rho_0 |v_1|^2$$
The time-averaged magnetic energy density of the wave perturbation is:
$$\\langle u_m \\rangle = \\frac{1}{4\\mu_0} |B_1|^2$$
From part (a), $|B_1| = \\frac{k B_0}{\\omega} |v_1|$.
Since $\\frac{\\omega}{k} = v_A = \\frac{B_0}{\\sqrt{\\mu_0 \\rho_0}}$, we have:
$$\\frac{k B_0}{\\omega} = \\frac{B_0}{v_A} = \\frac{B_0}{B_0 / \\sqrt{\\mu_0 \\rho_0}} = \\sqrt{\\mu_0 \\rho_0}$$
Therefore:
$$|B_1| = \\sqrt{\\mu_0 \\rho_0} |v_1|$$
Now substitute $|B_1|$ into the magnetic energy density:
$$\\langle u_m \\rangle = \\frac{1}{4\\mu_0} |B_1|^2 = \\frac{1}{4\\mu_0} \\left( \\sqrt{\\mu_0 \\rho_0} |v_1| \\right)^2 = \\frac{1}{4\\mu_0} (\\mu_0 \\rho_0 |v_1|^2) = \\frac{1}{4}\\rho_0 |v_1|^2$$
Comparing the two expressions:
$$\\langle u_m \\rangle = \\langle u_k \\rangle$$
This proves that shear Alfvén waves possess **exact 50/50 equipartition** between oscillating kinetic energy of the fluid and oscillating magnetic energy of the distorted field lines."""
        },
        {
            "id": "plasma-prob-7-2",
            "title": "Rayleigh-Taylor Growth Rate Derivation at Inverted Plasma-Vacuum Boundary and Magnetic Line Bending Suppression",
            "statement": """A slab of dense plasma with mass density $\\rho_0$ occupies the upper half-space $y > 0$ above an evacuated region ($y < 0$), subject to downward gravitational acceleration $\\vec{g} = -g\\hat{y}$. The plasma is permeated by a magnetic field $\\vec{B}_0 = B_0 \\hat{z}$.
(a) Assuming an incompressible ripple perturbation at the interface $y_1(x) = \\xi_0 e^{i(k_x x - \\omega t)}$, show from the linearized jump conditions that the unmagnetized gravitational Rayleigh-Taylor growth rate is $\\gamma = \\sqrt{g k_x}$.
(b) If the magnetic field is tilted to possess a component along the wavevector $\\vec{B}_0 = B_x \\hat{x} + B_z \\hat{z}$ so that $\\vec{k}\\cdot\\vec{B}_0 = k_x B_x \\ne 0$, show that the dispersion relation becomes:
$$\\omega^2 = -g k_x + \\frac{k_x^2 B_x^2}{\\mu_0 \\rho_0}$$
(c) For a laser-fusion pellet target where $g = 10^{13}\\text{ m/s}^2$, $\\rho_0 = 1000\\text{ kg/m}^3$, and perturbation wavelength $\\lambda = 10\\;\\mu\\text{m}$, calculate the unmagnetized growth time $\\tau = 1/\\gamma$. What minimum magnetic field $B_x$ is required to completely stabilize this perturbation?""",
            "solution": """**(a) Unmagnetized Rayleigh-Taylor Growth Rate:**
In the upper half-space ($y > 0$), incompressibility requires $\\nabla^2 \\phi_1 = 0 \\implies \\phi_1(x, y) = A e^{-k_x y} e^{i(k_x x - \\omega t)}$.
The vertical velocity at the boundary is $v_{y1} = -\\frac{\\partial \\phi_1}{\\partial y} = k_x A = -i\\omega \\xi_0$.
The linearized momentum equation yields the perturbed pressure at the interface:
$$P_1 = \\rho_0 \\frac{\\omega^2}{k_x}\\xi_0$$
The interface position is perturbed by $\\xi(x) = \\xi_0 e^{i(k_x x - \\omega t)}$. The gravitational pressure jump across the perturbed interface is:
$$\\Delta P_{\\text{grav}} = \\rho_0 g \\xi_0$$
Equating the dynamic pressure to the gravitational hydrostatic jump:
$$\\rho_0 \\frac{\\omega^2}{k_x}\\xi_0 = -\\rho_0 g \\xi_0 \\implies \\omega^2 = -g k_x$$
Since $\\omega^2 < 0$, $\\omega = \\pm i\\sqrt{g k_x} = \\pm i\\gamma$, where the instability growth rate is:
$$\\gamma = \\sqrt{g k_x}$$

**(b) Magnetic Shear / Line Bending Stabilization:**
When $\\vec{k}\\cdot\\vec{B}_0 = k_x B_x \\ne 0$, the perturbation distorts the magnetic field lines. The perturbed magnetic field inside the plasma is:
$$\\vec{B}_1 = \\nabla \\times (\\vec{\\xi} \\times \\vec{B}_0) = i(\\vec{k}\\cdot\\vec{B}_0)\\vec{\\xi} = i(k_x B_x)\\xi_0 \\hat{y}$$
The magnetic tension restoring force per unit volume is:
$$\\vec{F}_{\\text{tension}} = \\frac{1}{\\mu_0}(\\vec{B}_0\\cdot\\nabla)\\vec{B}_1 = \\frac{1}{\\mu_0}(i k_x B_x)\\left( i k_x B_x \\xi_0 \\hat{y} \\right) = -\\frac{k_x^2 B_x^2}{\\mu_0}\\xi_0 \\hat{y}$$
Integrating this restoring force across the boundary layer adds an effective positive spring constant to the interface equation of motion:
$$\\rho_0 \\frac{\\omega^2}{k_x}\\xi_0 = -\\rho_0 g \\xi_0 + \\frac{k_x B_x^2}{\\mu_0}\\xi_0$$
Dividing by $\\rho_0 \\xi_0 / k_x$:
$$\\omega^2 = -g k_x + \\frac{k_x^2 B_x^2}{\\mu_0 \\rho_0} = -g k_x + k_x^2 v_{Ax}^2$$
where $v_{Ax} = \\frac{B_x}{\\sqrt{\\mu_0 \\rho_0}}$.
Complete stability ($\omega^2 \\ge 0$) is achieved if and only if:
$$\\frac{k_x^2 B_x^2}{\\mu_0 \\rho_0} \\ge g k_x \\implies B_x^2 \\ge \\frac{\\mu_0 \\rho_0 g}{k_x}$$

**(c) Numerical Evaluation for Laser Fusion Target:**
Given:
$g = 10^{13}\\text{ m/s}^2$
$\\rho_0 = 1000\\text{ kg/m}^3$
$\\lambda = 10\\;\\mu\\text{m} = 1.0\\times 10^{-5}\\text{ m} \\implies k_x = \\frac{2\\pi}{1.0\\times 10^{-5}} = 6.283 \\times 10^5\\text{ m}^{-1}$

1. **Unmagnetized Growth Rate & Time:**
$$\\gamma = \\sqrt{g k_x} = \\sqrt{(10^{13}\\text{ m/s}^2)(6.283\\times 10^5\\text{ m}^{-1})} = \\sqrt{6.283\\times 10^{18}} \\approx 2.507 \\times 10^9\\text{ s}^{-1}$$
The growth e-folding time is:
$$\\tau = \\frac{1}{\\gamma} = \\frac{1}{2.507\\times 10^9\\text{ s}^{-1}} \\approx 3.99 \\times 10^{-10}\\text{ s} \\approx 0.40\\text{ nanoseconds}$$
The perturbation grows by a factor of $e$ in less than half a nanosecond!

2. **Minimum Stabilizing Magnetic Field $B_x$:**
$$B_{x,\\text{min}}^2 = \\frac{\\mu_0 \\rho_0 g}{k_x} = \\frac{(4\\pi\\times 10^{-7}\\text{ H/m})(1000\\text{ kg/m}^3)(10^{13}\\text{ m/s}^2)}{6.283\\times 10^5\\text{ m}^{-1}} = \\frac{1.257\\times 10^{10}}{6.283\\times 10^5} = 2.00 \\times 10^4\\text{ T}^2$$
Taking the square root:
$$B_{x,\\text{min}} = \\sqrt{2.00\\times 10^4} \\approx 141.4\\text{ Tesla}$$
A magnetic field of at least **141 Tesla** is required to completely suppress the Rayleigh-Taylor mode via magnetic tension."""
        },
        {
            "id": "plasma-prob-7-3",
            "title": "Kruskal-Shafranov Safety Factor and Maximum Stable Current in a Cylindrical Tokamak Geometry",
            "statement": """A medium-sized research tokamak has major radius $R = 1.50\\text{ m}$, minor radius $a = 0.40\\text{ m}$, and on-axis toroidal magnetic field $B_z = 2.50\\text{ Tesla}$.
(a) State the Kruskal-Shafranov stability condition for the $m=1$ external helical kink mode in terms of the safety factor $q(a)$.
(b) Derive the formula for the maximum stable plasma current $I_{\\text{max}}$ allowed before kink disruption occurs.
(c) Calculate the numerical value of $I_{\\text{max}}$ in Mega-amperes (MA).
(d) If the experimentalist attempts to drive a current $I_p = 1.20\\text{ MA}$, calculate the actual edge safety factor $q(a)$ and explain what will physically occur.""",
            "solution": """**(a) Kruskal-Shafranov Stability Condition:**
The safety factor at the plasma boundary $r = a$ is:
$$q(a) = \\frac{a B_z}{R B_\\theta(a)}$$
where $B_\\theta(a)$ is the poloidal magnetic field generated by the plasma current.
The Kruskal-Shafranov criterion states that the plasma column is stable against the dangerous $m=1$ external helical kink mode if and only if:
$$q(a) > 1$$

**(b) Maximum Stable Plasma Current Formula:**
By Ampère's law, the poloidal magnetic field at the plasma boundary $r=a$ is:
$$\\oint \\vec{B}_\\theta \\cdot d\\vec{l} = 2\\pi a B_\\theta(a) = \\mu_0 I_p \\implies B_\\theta(a) = \\frac{\\mu_0 I_p}{2\\pi a}$$
Substitute $B_\\theta(a)$ into the expression for $q(a)$:
$$q(a) = \\frac{a B_z}{R \\left( \\frac{\\mu_0 I_p}{2\\pi a} \\right)} = \\frac{2\\pi a^2 B_z}{\\mu_0 R I_p}$$
Applying the stability condition $q(a) > 1$:
$$\\frac{2\\pi a^2 B_z}{\\mu_0 R I_p} > 1 \\implies I_p < \\frac{2\\pi a^2 B_z}{\\mu_0 R} \\equiv I_{\\text{max}}$$
where $I_{\\text{max}}$ is the Kruskal-Shafranov current limit.

**(c) Numerical Calculation of $I_{\\text{max}}$:**
Given:
$a = 0.40\\text{ m} \\implies a^2 = 0.16\\text{ m}^2$
$R = 1.50\\text{ m}$
$B_z = 2.50\\text{ T}$
$\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$
Evaluating:
$$I_{\\text{max}} = \\frac{2\\pi (0.16\\text{ m}^2)(2.50\\text{ T})}{(4\\pi \\times 10^{-7}\\text{ H/m})(1.50\\text{ m})} = \\frac{0.80\\pi}{(6.0\\pi \\times 10^{-7})} = \\frac{0.80}{6.0\\times 10^{-7}} = \\frac{4}{3} \\times 10^6\\text{ A} \\approx 1.333 \\times 10^6\\text{ A}$$
$$I_{\\text{max}} \\approx 1.33\\text{ MA}$$
The maximum stable current allowed by the Kruskal-Shafranov limit is **1.33 Mega-amperes**.

**(d) Evaluation at $I_p = 1.20\\text{ MA}$:**
For $I_p = 1.20\\text{ MA}$:
$$q(a) = \\frac{I_{\\text{max}}}{I_p} = \\frac{1.333\\text{ MA}}{1.20\\text{ MA}} \\approx 1.111 > 1$$
Because $q(a) = 1.11 > 1$, the plasma remains macroscopically stable against the $m=1$ kink mode. However, in practice, tokamaks operate with $q(a) \\ge 3.0$ (known as the Greenwald-Hugill operating boundary) because higher-order resistive tearing modes ($m=2, n=1$ and $m=3, n=2$) become unstable when $q(a) < 2$, causing catastrophic major disruptions and thermal quench of the plasma into the divertor walls."""
        }
    ]
}

# =========================================================================
# UNIT 8: KINETIC THEORY OF PLASMAS & LANDAU DAMPING
# =========================================================================

unit8_data = {
    "unitId": "unit8-plasma",
    "title": "Kinetic Theory of Plasmas, Vlasov Equation & Landau Damping",
    "subtitle": "6D Phase Space, Vlasov-Maxwell System, Moments & Collisionless Damping",
    "summary": "Microscopic statistical foundations of plasma kinetics: the six-dimensional phase space, physical meaning of the distribution function, Liouville's theorem and phase space volume incompressibility, the collisionless Vlasov equation and the self-consistent Vlasov-Maxwell system, rigorous velocity moment derivation of multi-fluid equations and the closure hierarchy, linearized electrostatic perturbations, failure of classical Fourier analysis and the necessity of Laplace contour integration in time, the Landau contour and pole singularity, rigorous derivation of collisionless Landau damping, wave-particle resonant energy exchange physics, two-stream instability, and phase mixing in phase space.",
    "sections": [
        {
            "id": "sec-8-1",
            "number": "8.1",
            "title": "The Microscopic 6D Phase Space & Physical Meaning of Distribution Function f(r, v, t)",
            "content": """
<h3>1. Phase Space Representation</h3>
<p>
When particles possess a spread in velocities that cannot be captured by a single mean fluid velocity $\\vec{u}(\\vec{r}, t)$, fluid theory fails. We must describe the system microscopically in a six-dimensional <strong>phase space</strong> $(\\vec{r}, \\vec{v}) = (x, y, z, v_x, v_y, v_z)$.
</p>
<p>
The state of species $\\alpha$ is defined by its <strong>distribution function</strong> $f_\\alpha(\\vec{r}, \\vec{v}, t)$:
</p>
$$dN_\\alpha = f_\\alpha(\\vec{r}, \\vec{v}, t) d^3r d^3v = f_\\alpha(\\vec{r}, \\vec{v}, t) dx dy dz dv_x dv_y dv_z$$
<p>
where $dN_\\alpha$ is the expected number of particles located in the spatial volume element $d^3r$ around $\\vec{r}$ having velocities within the velocity volume element $d^3v$ around $\\vec{v}$ at time $t$.
</p>
<p>
The distribution function must be strictly non-negative: $f_\\alpha(\\vec{r}, \\vec{v}, t) \\ge 0$, and integrating over all velocity space recovers the local macroscopic number density:
</p>
$$\\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f_\\alpha(\\vec{r}, \\vec{v}, t) dv_x dv_y dv_z = n_\\alpha(\\vec{r}, t)$$
"""
        },
        {
            "id": "sec-8-2",
            "number": "8.2",
            "title": "Liouville's Theorem, Incompressibility of Phase Space Flow & The Boltzmann Transport Equation",
            "content": """
<h3>1. Liouville's Theorem in Hamiltonian Phase Space</h3>
<p>
In Hamiltonian mechanics, particle trajectories are governed by Hamilton's canonical equations $\\dot{\\vec{r}} = \\nabla_p H, \\dot{\\vec{p}} = -\\nabla_r H$. The phase space velocity field $\\vec{w} = (\\dot{\\vec{r}}, \\dot{\\vec{p}})$ is strictly divergence-free:
</p>
$$\\nabla_r \\cdot \\dot{\\vec{r}} + \\nabla_p \\cdot \\dot{\\vec{p}} = \\nabla_r \\cdot (\\nabla_p H) - \\nabla_p \\cdot (\\nabla_r H) = 0$$
<p>
According to <strong>Liouville's Theorem</strong>, the flow of representative points in phase space behaves as an <strong>incompressible fluid</strong>:
</p>
$$\\frac{df}{dt} = 0$$
<p>
The phase space density $f$ remains constant along any dynamical trajectory!
</p>

<h3>2. The Boltzmann Transport Equation</h3>
<p>
Expanding the total convective time derivative along a trajectory governed by acceleration $\\vec{a} = \\frac{q}{m}(\\vec{E} + \\vec{v}\\times\\vec{B})$:
</p>
$$\\frac{df}{dt} = \\frac{\\partial f}{\\partial t} + \\dot{\\vec{r}}\\cdot\\nabla_r f + \\dot{\\vec{v}}\\cdot\\nabla_v f = \\frac{\\partial f}{\\partial t} + \\vec{v}\\cdot\\nabla f + \\frac{q}{m}(\\vec{E} + \\vec{v}\\times\\vec{B})\\cdot\\nabla_v f$$
<p>
In the presence of discrete, short-range binary collisions between particles:
</p>
$$\\frac{\\partial f}{\\partial t} + \\vec{v}\\cdot\\nabla f + \\frac{q}{m}(\\vec{E} + \\vec{v}\\times\\vec{B})\\cdot\\nabla_v f = \\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}}$$
<p>
This is the <strong>Boltzmann transport equation</strong>.
</p>
"""
        },
        {
            "id": "sec-8-3",
            "number": "8.3",
            "title": "The Collisionless Vlasov Equation & The Self-Consistent Vlasov-Maxwell System",
            "content": """
<h3>1. The Vlasov Equation</h3>
<p>
In high-temperature, low-density plasmas where the plasma parameter $N_D = \\frac{4}{3}\\pi n_e \\lambda_D^3 \\gg 1$, long-range collective Coulomb fields dominate over discrete binary collisions. Setting the collision integral to zero yields the <strong>Vlasov equation</strong> (or collisionless Boltzmann equation):
</p>
$$\\frac{\\partial f_\\alpha}{\\partial t} + \\vec{v}\\cdot\\nabla f_\\alpha + \\frac{q_\\alpha}{m_\\alpha}\\left( \\vec{E}(\\vec{r}, t) + \\vec{v}\\times\\vec{B}(\\vec{r}, t) \\right)\\cdot\\frac{\\partial f_\\alpha}{\\partial \\vec{v}} = 0$$
<p>
Here, $\\vec{E}$ and $\\vec{B}$ are not external fields, but the <strong>self-consistent, macroscopic average electromagnetic fields</strong> generated by the collective charge density $\\rho_q$ and current density $\\vec{J}$ of all particles in the plasma:
</p>
$$\\rho_q(\\vec{r}, t) = \\sum_\\alpha q_\\alpha \\int f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v, \\quad \\vec{J}(\\vec{r}, t) = \\sum_\\alpha q_\\alpha \\int \\vec{v} f_\\alpha(\\vec{r}, \\vec{v}, t) d^3v$$

<h3>2. The Self-Consistent Vlasov-Maxwell System</h3>
<p>
Coupled with Maxwell's equations:
</p>
$$\\nabla \\cdot \\vec{E} = \\frac{\\rho_q}{\\varepsilon_0}, \\quad \\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$$
$$\\nabla \\cdot \\vec{B} = 0, \\quad \\nabla \\times \\vec{B} = \\mu_0 \\vec{J} + \\frac{1}{c^2}\\frac{\\partial \\vec{E}}{\\partial t}$$
<p>
The Vlasov-Maxwell system provides a complete, exact, collisionless description of plasma physics, capturing all kinetic phenomena including wave-particle resonances and Landau damping.
</p>
"""
        },
        {
            "id": "sec-8-4",
            "number": "8.4",
            "title": "Systematic Derivation of Multi-Fluid Equations by Velocity Moments of the Vlasov Equation",
            "content": """
<h3>1. The General Moment Theorem</h3>
<p>
Let $\\chi(\\vec{v})$ be an arbitrary function of velocity. Multiplying the Vlasov equation by $\\chi(\\vec{v})$ and integrating over all velocity space $d^3v$:
</p>
$$\\int \\chi(\\vec{v}) \\frac{\\partial f}{\\partial t} d^3v + \\int \\chi(\\vec{v}) \\vec{v}\\cdot\\nabla f d^3v + \\frac{q}{m}\\int \\chi(\\vec{v}) (\\vec{E} + \\vec{v}\\times\\vec{B})\\cdot\\nabla_v f d^3v = 0$$
<p>
Using integration by parts on the third term and noting that $f \\to 0$ as $v \\to \\pm\\infty$:
</p>
$$\\frac{\\partial}{\\partial t}\\left( n \\langle \\chi \\rangle \\right) + \\nabla \\cdot \\left( n \\langle \\vec{v} \\chi \\rangle \\right) - \\frac{q}{m} n \\left\\langle (\\vec{E} + \\vec{v}\\times\\vec{B})\\cdot\\nabla_v \\chi \\right\\rangle = 0$$

<h3>2. Systematic Derivation of Fluid Equations</h3>
<ol>
  <li><strong>Zeroth Moment ($\\chi = 1$):</strong> Since $\\nabla_v(1) = 0$:
  $$\\frac{\\partial n}{\\partial t} + \\nabla \\cdot (n \\vec{u}) = 0 \\quad \\text{(Continuity Equation)}$$</li>
  <li><strong>First Moment ($\\chi = m \\vec{v}$):</strong> Since $\\nabla_v(m\\vec{v}) = m \\mathbf{I}$:
  $$m n \\left[ \\frac{\\partial \\vec{u}}{\\partial t} + (\\vec{u}\\cdot\\nabla)\\vec{u} \\right] = q n (\\vec{E} + \\vec{u}\\times\\vec{B}) - \\nabla \\cdot \\mathbf{P} \\quad \\text{(Momentum Equation)}$$</li>
  <li><strong>Second Moment ($\\chi = \\frac{1}{2}m v^2$):</strong> Yields the thermal energy transport equation containing the heat flux vector $\\vec{Q} = \\frac{1}{2}m \\int (\\vec{v} - \\vec{u})|\\vec{v} - \\vec{u}|^2 f d^3v$.</li>
</ol>
"""
        },
        {
            "id": "sec-8-5",
            "number": "8.5",
            "title": "Linearized Electrostatic Vlasov Perturbations & Failure of Standard Fourier Transforms",
            "content": """
<h3>1. Linearization of 1D Vlasov Equation</h3>
<p>
Consider 1D electrostatic perturbations in an unmagnetized plasma with stationary ion background. Decompose the electron distribution function:
</p>
$$f(x, v, t) = f_0(v) + f_1(x, v, t)$$
<p>
where $f_0(v)$ is an unperturbed homogeneous equilibrium (e.g., Maxwellian) and $f_1$ is small ($|f_1| \\ll f_0$). Neglecting the second-order term $E_1 \\frac{\\partial f_1}{\\partial v}$:
</p>
$$\\frac{\\partial f_1}{\\partial t} + v \\frac{\\partial f_1}{\\partial x} - \\frac{e}{m_e} E_1 \\frac{\\partial f_0}{\\partial v} = 0$$
<p>
coupled to Poisson's equation:
</p>
$$\\frac{\\partial E_1}{\\partial x} = -\\frac{e}{\\varepsilon_0}\\int_{-\\infty}^\\infty f_1(x, v, t) dv$$

<h3>2. Failure of the Standard Fourier Transform</h3>
<p>
If one attempts to solve this initial-value problem using a standard Fourier transform in time ($e^{-i\\omega t}$):
</p>
$$-i(\\omega - k v) f_1 = \\frac{e}{m_e} E_1 \\frac{\\partial f_0}{\\partial v} \\implies f_1(k, v, \\omega) = \\frac{i e E_1}{m_e} \\frac{\\partial f_0 / \\partial v}{\\omega - k v}$$
<p>
Substituting $f_1$ into Poisson's equation yields the dielectric permittivity integral:
</p>
$$\\varepsilon(k, \\omega) = 1 + \\frac{e^2}{\\varepsilon_0 m_e k} \\int_{-\\infty}^\\infty \\frac{\\partial f_0 / \\partial v}{\\omega - k v} dv = 1 - \\frac{\\omega_{pe}^2}{k^2} \\int_{-\\infty}^\\infty \\frac{f_0'(v)}{v - \\omega/k} dv$$
<p>
Here lies the profound crisis that perplexed early plasma physicists: if $\\omega$ is real, the integrand has a <strong>singularity pole on the real axis</strong> at $v = \\omega / k$ (the phase velocity). Standard Fourier integration fails because it cannot handle the initial conditions or resolve the singularity properly.
</p>
"""
        },
        {
            "id": "sec-8-6",
            "number": "8.6",
            "title": "The Landau Contour Integral, Pole Singularity at v = omega/k & Derivation of Landau Damping",
            "content": """
<h3>1. Landau's Laplace Transform Method</h3>
<p>
In 1946, Soviet physicist Lev Landau resolved the singularity by treating the perturbation as an initial-value problem with a <strong>one-sided Laplace transform in time</strong>:
</p>
$$\\tilde{f}_1(k, v, p) = \\int_0^\\infty f_1(k, v, t) e^{-p t} dt, \\quad \\text{Re}(p) > 0$$
<p>
Inverting the Laplace transform requires integrating along the Bromwich contour in the complex $p$-plane:
</p>
$$E_1(k, t) = \\frac{1}{2\\pi i} \\int_{\\sigma - i\\infty}^{\\sigma + i\\infty} \\tilde{E}_1(k, p) e^{p t} dp$$
<p>
To perform the analytic continuation into the damping half-plane ($\\text{Re}(p) < 0$), Landau proved that the integration contour in velocity space must be deformed so that the pole at $v = \\omega / k = -i p / k$ always remains <strong>above the contour</strong>. This defines the famous <strong>Landau contour</strong> $C$:
</p>
$$\\int_C \\frac{f_0'(v)}{v - \\omega/k} dv = \\mathcal{P}\\int_{-\\infty}^\\infty \\frac{f_0'(v)}{v - \\omega/k} dv + i \\pi f_0'\\left( \\frac{\\omega}{k} \\right)$$
<p>
where $\\mathcal{P}$ denotes the Cauchy principal value, and the term $+i\\pi f_0'(\\omega/k)$ is the residue from wrapping around the pole from below.
</p>

<h3>2. The Landau Damping Rate</h3>
<p>
Writing the complex frequency as $\\omega = \\omega_r + i\\gamma$, where $\\gamma$ is the damping rate ($|\\gamma| \\ll \\omega_r$). Expanding $\\varepsilon(k, \\omega_r + i\\gamma) = 0$ in Taylor series:
</p>
$$\\varepsilon_r(k, \\omega_r) + i\\gamma \\frac{\\partial \\varepsilon_r}{\\partial \\omega} + i\\varepsilon_i(k, \\omega_r) = 0$$
<p>
The real part yields the Bohm-Gross frequency: $\\omega_r^2 \\approx \\omega_{pe}^2 + 3 k^2 v_{\\text{th}}^2$.
The imaginary part yields the <strong>Landau damping rate</strong> $\\gamma_L$:
</p>
$$\\gamma_L = -\\frac{\\varepsilon_i}{\\partial \\varepsilon_r / \\partial \\omega} = \\frac{\\pi}{2} \\frac{\\omega_r \\omega_{pe}^2}{k^2} \\left[ \\frac{\\partial f_0}{\\partial v} \\right]_{v = \\omega_r/k}$$
<p>
For a Maxwellian distribution $f_0(v) = \\frac{1}{\\sqrt{2\\pi}v_{\\text{th}}}e^{-v^2 / (2v_{\\text{th}}^2)}$, the derivative at the phase velocity is strictly negative: $\\left[ \\frac{\\partial f_0}{\\partial v} \\right]_{v_{ph}} < 0$.
Consequently:
</p>
$$\\gamma_L < 0$$
<p>
The wave is <strong>exponentially damped in time</strong>:
</p>
$$E_1(t) \\propto e^{-|\\gamma_L| t} \\cos(\\omega_r t)$$
<p>
Evaluating explicitly for a Maxwellian distribution:
</p>
$$\\gamma_L = -\\sqrt{\\frac{\\pi}{8}} \\frac{\\omega_{pe}}{(k\\lambda_D)^3} \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right)$$
<p>
This is the discovery of <strong>Landau damping</strong>: irreversible wave dissipation occurring in a completely collisionless, conservative Hamiltonian plasma!
</p>
"""
        },
        {
            "id": "sec-8-7",
            "number": "8.7",
            "title": "Physical Mechanism of Landau Damping: Resonant Wave-Particle Energy Exchange & Two-Stream Instability",
            "content": """
<h3>1. Physical Mechanism: Surfing the Wave</h3>
<p>
Landau damping is not caused by dissipative collisions, but by a <strong>resonant energy exchange</strong> between the electrostatic wave and particles moving near the wave's phase velocity:
</p>
$$v \\approx v_{ph} = \\frac{\\omega}{k}$$
<p>
Consider a surfer catching an ocean wave:
</p>
<ul>
  <li><strong>Particles slightly slower than the wave ($v < v_{ph}$):</strong> The wave pushes them forward, accelerating them and transferring energy <em>from the wave to the particles</em>.</li>
  <li><strong>Particles slightly faster than the wave ($v > v_{ph}$):</strong> They push forward against the wave potential, decelerating and transferring energy <em>from the particles to the wave</em>.</li>
</ul>
<p>
In a thermal Maxwellian distribution, the distribution function decreases monotonically with speed ($\partial f_0 / \partial v < 0$). Therefore, there are always <strong>more slightly slower particles than slightly faster particles</strong>:
</p>
$$N(v < v_{ph}) > N(v > v_{ph})$$
<p>
On net, more particles gain kinetic energy from the wave than give energy to it. As a result, the wave loses electrostatic energy, damping exponentially away!
</p>

<h3>2. The Two-Stream Instability (Inverse Landau Damping)</h3>
<p>
If the plasma contains an electron beam moving at drift speed $v_d > 0$, the distribution function develops a bump on the tail. In the velocity range where the distribution function slope is positive:
</p>
$$\\left[ \\frac{\\partial f_0}{\\partial v} \\right]_{v = v_{ph}} > 0$$
<p>
Now there are more faster particles than slower particles! The resonant particles transfer net kinetic energy to the wave, causing the wave amplitude to grow exponentially ($\gamma > 0$). This is <strong>inverse Landau damping</strong>, which drives the classic <strong>two-stream instability</strong> (or bump-on-tail instability).
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-8-1",
            "title": "Exact Velocity Moment Derivation of Fluid Continuity and Momentum Equations from the 1D Vlasov Equation",
            "statement": """Consider the 1D collisionless Vlasov equation for electrons in an electrostatic field $E(x, t)$:
$$\\frac{\\partial f}{\\partial t} + v \\frac{\\partial f}{\\partial x} - \\frac{e E}{m_e} \\frac{\\partial f}{\\partial v} = 0$$
where $n(x, t) = \\int_{-\\infty}^\\infty f(x, v, t) dv$ is the number density, $u(x, t) = \\frac{1}{n}\\int_{-\\infty}^\\infty v f dv$ is the mean fluid velocity, and $P(x, t) = m_e \\int_{-\\infty}^\\infty (v - u)^2 f dv$ is the kinetic scalar pressure.
(a) Multiply by $v^0 = 1$ and integrate over all velocity space $dv$ to derive the fluid continuity equation $\\frac{\\partial n}{\\partial t} + \\frac{\\partial(n u)}{\\partial x} = 0$.
(b) Multiply by $m_e v$ and integrate over $dv$ to derive the exact momentum balance equation:
$$m_e n \\left[ \\frac{\\partial u}{\\partial t} + u \\frac{\\partial u}{\\partial x} \\right] = -e n E - \\frac{\\partial P}{\\partial x}$$
(c) Explicitly show how the pressure term $\\frac{\\partial P}{\\partial x}$ emerges from the convective velocity dispersion moment.""",
            "solution": """**(a) Zeroth Moment (Fluid Continuity):**
Integrate the 1D Vlasov equation over $v \\in (-\\infty, \\infty)$:
$$\\int_{-\\infty}^\\infty \\frac{\\partial f}{\\partial t} dv + \\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial x} dv - \\frac{e E}{m_e} \\int_{-\\infty}^\\infty \\frac{\\partial f}{\\partial v} dv = 0$$
Evaluate each term:
1. $\\int_{-\\infty}^\\infty \\frac{\\partial f}{\\partial t} dv = \\frac{\\partial}{\\partial t}\\int_{-\\infty}^\\infty f dv = \\frac{\\partial n}{\\partial t}$
2. $\\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial x} dv = \\frac{\\partial}{\\partial x}\\int_{-\\infty}^\\infty v f dv = \\frac{\\partial(n u)}{\\partial x}$
3. $\\int_{-\\infty}^\\infty \\frac{\\partial f}{\\partial v} dv = [f(x, v, t)]_{v=-\\infty}^{v=+\\infty} = 0 - 0 = 0$ (since $f \\to 0$ as $v \\to \\pm\\infty$).
Summing the terms:
$$\\frac{\\partial n}{\\partial t} + \\frac{\\partial(n u)}{\\partial x} = 0$$
This rigorously proves the fluid continuity equation.

**(b) & (c) First Moment (Fluid Momentum Equation):**
Multiply the Vlasov equation by $m_e v$ and integrate over $v$:
$$m_e \\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial t} dv + m_e \\int_{-\\infty}^\\infty v^2 \\frac{\\partial f}{\\partial x} dv - e E \\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial v} dv = 0$$
Evaluate each term:
1. First term:
$$m_e \\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial t} dv = m_e \\frac{\\partial}{\\partial t}\\int_{-\\infty}^\\infty v f dv = m_e \\frac{\\partial(n u)}{\\partial t} = m_e \\left( n \\frac{\\partial u}{\\partial t} + u \\frac{\\partial n}{\\partial t} \\right)$$

2. Third term (integrate by parts with $U = v, dV = \\frac{\\partial f}{\\partial v}dv$):
$$\\int_{-\\infty}^\\infty v \\frac{\\partial f}{\\partial v} dv = [v f]_{-\\infty}^\\infty - \\int_{-\\infty}^\\infty f dv = 0 - n = -n$$
So the third term is:
$$-e E (-n) = +e n E$$

3. Second term (velocity dispersion expansion):
Notice that $v = u + (v - u)$. Squaring both sides:
$$v^2 = [u + (v - u)]^2 = u^2 + 2 u (v - u) + (v - u)^2$$
Integrate $m_e v^2 f$ over $v$:
$$m_e \\int_{-\\infty}^\\infty v^2 f dv = m_e u^2 \\int f dv + 2 m_e u \\int (v - u) f dv + m_e \\int (v - u)^2 f dv$$
Since by definition $\\int (v - u) f dv = \\int v f dv - u \\int f dv = n u - n u = 0$, the cross-term vanishes identically!
The third integral is precisely the definition of scalar kinetic pressure:
$$P(x, t) \\equiv m_e \\int_{-\\infty}^\\infty (v - u)^2 f dv$$
Therefore:
$$m_e \\int_{-\\infty}^\\infty v^2 f dv = m_e n u^2 + P$$
The spatial derivative of the second term is:
$$m_e \\frac{\\partial}{\\partial x}\\int v^2 f dv = \\frac{\\partial}{\\partial x}(m_e n u^2 + P) = m_e \\frac{\\partial(n u^2)}{\\partial x} + \\frac{\\partial P}{\\partial x}$$
$$= m_e \\left( u \\frac{\\partial(n u)}{\\partial x} + n u \\frac{\\partial u}{\\partial x} \\right) + \\frac{\\partial P}{\\partial x}$$

Now assemble all three terms:
$$m_e \\left( n \\frac{\\partial u}{\\partial t} + u \\frac{\\partial n}{\\partial t} \\right) + m_e u \\frac{\\partial(n u)}{\\partial x} + m_e n u \\frac{\\partial u}{\\partial x} + \\frac{\\partial P}{\\partial x} - e n E = 0$$
Group the terms multiplying $m_e u$:
$$m_e n \\frac{\\partial u}{\\partial t} + m_e n u \\frac{\\partial u}{\\partial x} + m_e u \\underbrace{\\left[ \\frac{\\partial n}{\\partial t} + \\frac{\\partial(n u)}{\\partial x} \\right]}_{= 0 \\text{ by continuity!}} + \\frac{\\partial P}{\\partial x} = -e n E$$
The bracketed term vanishes by the continuity equation proved in (a)!
We are left with:
$$m_e n \\left[ \\frac{\\partial u}{\\partial t} + u \\frac{\\partial u}{\\partial x} \\right] = -e n E - \\frac{\\partial P}{\\partial x}$$
This completes the exact, rigorous moment derivation, showing that thermal kinetic pressure is simply the random velocity dispersion of the kinetic distribution function."""
        },
        {
            "id": "plasma-prob-8-2",
            "title": "Analytical Derivation of the Weak Landau Damping Rate for a Maxwellian Velocity Distribution",
            "statement": """Derive the weak Landau damping rate for electron plasma waves in a 1D Maxwellian plasma:
$$f_0(v) = \\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}} \\exp\\left( -\\frac{v^2}{2 v_{\\text{th}}^2} \\right)$$
where $v_{\\text{th}} = \\sqrt{k_B T_e / m_e}$ and $\\lambda_D = v_{\\text{th}} / \\omega_{pe}$.
(a) Evaluate the derivative $\\frac{\\partial f_0}{\\partial v}$ at the phase velocity $v = v_{ph} = \\omega / k$.
(b) Using the Bohm-Gross dispersion relation $\\omega^2 = \\omega_{pe}^2(1 + 3 k^2 \\lambda_D^2)$, show that in the long-wavelength limit $k\\lambda_D \\ll 1$:
$$\\frac{v_{ph}^2}{2 v_{\\text{th}}^2} \\approx \\frac{1}{2 (k\\lambda_D)^2} + \\frac{3}{2}$$
(c) Substitute this result into the Landau damping rate formula $\\gamma_L = \\frac{\\pi}{2}\\frac{\\omega_{pe}^3}{k^2 n_0}\\left[ \\frac{\\partial f_0}{\\partial v} \\right]_{v_{ph}}$ to derive the asymptotic damping expression:
$$\\gamma_L = -\\sqrt{\\frac{\\pi}{8}} \\frac{\\omega_{pe}}{(k\\lambda_D)^3} \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right)$$
(d) For $k\\lambda_D = 0.20$, compute the ratio of the damping rate to the plasma frequency $|\\gamma_L| / \\omega_{pe}$ and calculate the number of oscillation cycles required for the wave amplitude to decay to $1/e$ of its initial value.""",
            "solution": """**(a) Derivative of the Maxwellian Distribution:**
$$f_0(v) = \\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}} e^{-v^2 / (2 v_{\\text{th}}^2)}$$
Differentiating with respect to $v$:
$$\\frac{\\partial f_0}{\\partial v} = \\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}} \\left( -\\frac{v}{v_{\\text{th}}^2} \\right) e^{-v^2 / (2 v_{\\text{th}}^2)} = -\\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}^3} v e^{-v^2 / (2 v_{\\text{th}}^2)}$$
Evaluating at $v = v_{ph} = \\omega / k$:
$$\\left[ \\frac{\\partial f_0}{\\partial v} \\right]_{v_{ph}} = -\\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}^3} \\left( \\frac{\\omega}{k} \\right) \\exp\\left( -\\frac{\\omega^2}{2 k^2 v_{\\text{th}}^2} \\right)$$

**(b) Long-Wavelength Expansion of the Exponent:**
From the Bohm-Gross relation:
$$\\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{\\text{th}}^2 = \\omega_{pe}^2 (1 + 3 k^2 \\lambda_D^2)$$
where $\\lambda_D = v_{\\text{th}} / \\omega_{pe}$.
The exponent argument is:
$$\\frac{\\omega^2}{2 k^2 v_{\\text{th}}^2} = \\frac{\\omega_{pe}^2(1 + 3 k^2 \\lambda_D^2)}{2 k^2 v_{\\text{th}}^2} = \\frac{\\omega_{pe}^2}{2 k^2 v_{\\text{th}}^2} + \\frac{3 k^2 v_{\\text{th}}^2}{2 k^2 v_{\\text{th}}^2} = \\frac{1}{2 k^2 \\lambda_D^2} + \\frac{3}{2}$$
Therefore:
$$\\exp\\left( -\\frac{\\omega^2}{2 k^2 v_{\\text{th}}^2} \\right) = \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right)$$

**(c) Asymptotic Landau Damping Rate Formula:**
Substitute the derivative into the Landau formula:
$$\\gamma_L = \\frac{\\pi}{2}\\frac{\\omega_{pe}^3}{k^2 n_0}\\left[ -\\frac{n_0}{\\sqrt{2\\pi}v_{\\text{th}}^3} \\left(\\frac{\\omega}{k}\\right) \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right) \\right]$$
In the long-wavelength limit $k\\lambda_D \\ll 1$, $\\omega \\approx \\omega_{pe}$:
$$\\gamma_L = -\\frac{\\pi}{2\\sqrt{2\\pi}} \\frac{\\omega_{pe}^4}{k^3 v_{\\text{th}}^3} \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right)$$
Notice that:
$$\\frac{\\pi}{2\\sqrt{2\\pi}} = \\frac{\\sqrt{\\pi}}{2\\sqrt{2}} = \\sqrt{\\frac{\\pi}{8}}$$
and:
$$\\frac{\\omega_{pe}^4}{k^3 v_{\\text{th}}^3} = \\omega_{pe} \\left( \\frac{\\omega_{pe}}{k v_{\\text{th}}} \\right)^3 = \\frac{\\omega_{pe}}{(k\\lambda_D)^3}$$
Therefore, we obtain the celebrated formula:
$$\\gamma_L = -\\sqrt{\\frac{\\pi}{8}} \\frac{\\omega_{pe}}{(k\\lambda_D)^3} \\exp\\left( -\\frac{1}{2(k\\lambda_D)^2} - \\frac{3}{2} \\right)$$

**(d) Numerical Evaluation for $k\\lambda_D = 0.20$:**
Given $k\\lambda_D = 0.20$:
$$(k\\lambda_D)^3 = (0.20)^3 = 0.0080$$
$$\\sqrt{\\frac{\\pi}{8}} = \\sqrt{0.3927} \\approx 0.6267$$
$$\\frac{1}{2(k\\lambda_D)^2} = \\frac{1}{2(0.04)} = \\frac{1}{0.08} = 12.50$$
The total exponent is:
$$-12.50 - 1.50 = -14.00$$
Evaluating the exponential factor:
$$e^{-14.00} \\approx 8.315 \\times 10^{-7}$$
Evaluating the ratio $|\\gamma_L| / \\omega_{pe}$:
$$\\frac{|\\gamma_L|}{\\omega_{pe}} = \\frac{0.6267}{0.0080} \\times (8.315 \\times 10^{-7}) = 78.33 \\times (8.315 \\times 10^{-7}) \\approx 6.51 \\times 10^{-5}$$
The damping time is:
$$\\tau_{\\text{damp}} = \\frac{1}{|\\gamma_L|} = \\frac{1}{6.51\\times 10^{-5} \\omega_{pe}} \\approx \\frac{15,350}{\\omega_{pe}}$$
The period of one oscillation is $T = \\frac{2\\pi}{\\omega} \\approx \\frac{2\\pi}{\\omega_{pe}}$.
The number of oscillation cycles $N_{\\text{cycles}}$ before the wave amplitude drops to $1/e$ is:
$$N_{\\text{cycles}} = \\frac{\\tau_{\\text{damp}}}{T} = \\frac{15350 / \\omega_{pe}}{2\\pi / \\omega_{pe}} = \\frac{15350}{2\\pi} \\approx 2,443\\text{ cycles}$$
At $k\\lambda_D = 0.20$, the wave is very weakly damped, surviving for over 2,400 full oscillation periods because very few thermal electrons possess speeds as high as $v_{ph} = 5 v_{\\text{th}}$."""
        },
        {
            "id": "plasma-prob-8-3",
            "title": "Penrose Stability Criterion and Two-Stream Instability Growth Rate in Counter-Streaming Electron Beams",
            "statement": """Consider an unmagnetized plasma consisting of two identical cold electron beams counter-streaming along $\\hat{x}$ with equal and opposite drift velocities $\\pm v_0$ and equal density $n_0 / 2$, moving through a stationary neutralizing ion background.
(a) From the linearized cold fluid equations for both beams, derive the two-stream dispersion relation:
$$1 - \\frac{\\omega_{pe}^2 / 2}{(\\omega - k v_0)^2} - \\frac{\\omega_{pe}^2 / 2}{(\\omega + k v_0)^2} = 0$$
(b) Show that for $k v_0 < \\omega_{pe}$, the system becomes unstable with purely imaginary frequency $\\omega = i\\gamma$.
(c) Determine the critical wavenumber $k_{\\text{max}}$ where the growth rate reaches its maximum, and calculate the maximum growth rate $\\gamma_{\\text{max}}$ in terms of $\\omega_{pe}$.""",
            "solution": """**(a) Derivation of Two-Stream Dispersion Relation:**
Let beam 1 have equilibrium velocity $+v_0$ and beam 2 have $-v_0$, with unperturbed densities $n_{01} = n_{02} = n_0 / 2$.
For beam 1, linearized continuity and momentum equations:
$$-i(\\omega - k v_0) n_{11} + i k (n_0/2) u_{11} = 0 \\implies n_{11} = \\frac{n_0}{2}\\frac{k u_{11}}{\\omega - k v_0}$$
$$-i(\\omega - k v_0) m_e u_{11} = -e E_1 \\implies u_{11} = \\frac{e E_1}{i m_e (\\omega - k v_0)}$$
$$n_{11} = -\\frac{i (n_0/2) e k E_1}{m_e (\\omega - k v_0)^2}$$
Similarly for beam 2 with velocity $-v_0$:
$$n_{12} = -\\frac{i (n_0/2) e k E_1}{m_e (\\omega + k v_0)^2}$$
Substitute total electron perturbation $n_{e1} = n_{11} + n_{12}$ into Poisson's equation $i k \\varepsilon_0 E_1 = -e n_{e1}$:
$$i k \\varepsilon_0 E_1 = -e \\left[ -\\frac{i (n_0/2) e k E_1}{m_e (\\omega - k v_0)^2} - \\frac{i (n_0/2) e k E_1}{m_e (\\omega + k v_0)^2} \\right]$$
Dividing by $i k \\varepsilon_0 E_1$ and using $\\omega_{pe}^2 = \\frac{n_0 e^2}{\\varepsilon_0 m_e}$:
$$1 = \\frac{\\omega_{pe}^2 / 2}{(\\omega - k v_0)^2} + \\frac{\\omega_{pe}^2 / 2}{(\\omega + k v_0)^2}$$
$$1 - \\frac{\\omega_{pe}^2 / 2}{(\\omega - k v_0)^2} - \\frac{\\omega_{pe}^2 / 2}{(\\omega + k v_0)^2} = 0$$

**(b) Instability Condition:**
Let $y = \\omega^2$ and $a = k v_0$. Putting the dispersion relation over a common denominator:
$$1 = \\frac{\\omega_{pe}^2}{2} \\left[ \\frac{(\\omega + a)^2 + (\\omega - a)^2}{[(\\omega - a)(\\omega + a)]^2} \\right] = \\frac{\\omega_{pe}^2}{2} \\left[ \\frac{2\\omega^2 + 2a^2}{(\\omega^2 - a^2)^2} \\right] = \\omega_{pe}^2 \\frac{y + a^2}{(y - a^2)^2}$$
$$(y - a^2)^2 = \\omega_{pe}^2 (y + a^2) \\implies y^2 - 2a^2 y + a^4 - \\omega_{pe}^2 y - \\omega_{pe}^2 a^2 = 0$$
$$y^2 - (2a^2 + \\omega_{pe}^2) y + a^2(a^2 - \\omega_{pe}^2) = 0$$
Solving for $y = \\omega^2$ using the quadratic formula:
$$\\omega^2 = \\frac{(2a^2 + \\omega_{pe}^2) \\pm \\sqrt{(2a^2 + \\omega_{pe}^2)^2 - 4a^2(a^2 - \\omega_{pe}^2)}}{2}$$
Evaluate the discriminant $\\Delta$:
$$\\Delta = (4a^4 + 4a^2\\omega_{pe}^2 + \\omega_{pe}^4) - (4a^4 - 4a^2\\omega_{pe}^2) = 8a^2\\omega_{pe}^2 + \\omega_{pe}^4 = \\omega_{pe}^2(8a^2 + \\omega_{pe}^2) > 0$$
Since $\\Delta > 0$, both roots for $\\omega^2$ are real.
Now check the product of the roots:
$$P = y_1 y_2 = a^2(a^2 - \\omega_{pe}^2)$$
If $a = k v_0 < \\omega_{pe}$, then $a^2 - \\omega_{pe}^2 < 0$, which guarantees that the product of the roots is strictly negative ($P < 0$)!
One root $\\omega^2$ is positive (stable oscillation), while the other root $\\omega^2$ is **strictly negative**:
$$\\omega^2 < 0 \\implies \\omega = \\pm i\\gamma$$
This rigorously proves that for all wavenumbers satisfying $k < \\frac{\\omega_{pe}}{v_0}$, the counter-streaming plasma is unstable!

**(c) Maximum Growth Rate:**
Taking the negative root for $\\omega^2 = -\\gamma^2$:
$$\\gamma(a) = \\sqrt{\\frac{\\sqrt{\\omega_{pe}^4 + 8a^2\\omega_{pe}^2} - (2a^2 + \\omega_{pe}^2)}{2}}$$
To find the maximum growth rate, differentiate with respect to $a^2$ and set to zero:
$$\\frac{d}{d(a^2)}\\left[ \\sqrt{\\omega_{pe}^4 + 8a^2\\omega_{pe}^2} - 2a^2 \\right] = 0 \\implies \\frac{8\\omega_{pe}^2}{2\\sqrt{\\omega_{pe}^4 + 8a^2\\omega_{pe}^2}} - 2 = 0$$
$$\\frac{4\\omega_{pe}^2}{\\sqrt{\\omega_{pe}^4 + 8a^2\\omega_{pe}^2}} = 2 \\implies \\sqrt{\\omega_{pe}^4 + 8a^2\\omega_{pe}^2} = 2\\omega_{pe}^2$$
Squaring both sides:
$$\\omega_{pe}^4 + 8a^2\\omega_{pe}^2 = 4\\omega_{pe}^4 \\implies 8a^2\\omega_{pe}^2 = 3\\omega_{pe}^4 \\implies a^2 = \\frac{3}{8}\\omega_{pe}^2$$
$$a = k_{\\text{max}} v_0 = \\sqrt{\\frac{3}{8}}\\omega_{pe} \\approx 0.612 \\omega_{pe} \\implies k_{\\text{max}} = \\frac{\\sqrt{3/8}\\omega_{pe}}{v_0}$$
Now substitute $a^2 = \\frac{3}{8}\\omega_{pe}^2$ into $\\gamma^2$:
$$\\gamma_{\\text{max}}^2 = \\frac{2\\omega_{pe}^2 - \\left( 2\\left(\\frac{3}{8}\\omega_{pe}^2\\right) + \\omega_{pe}^2 \\right)}{2} = \\frac{2\\omega_{pe}^2 - \\left( \\frac{3}{4}\\omega_{pe}^2 + \\omega_{pe}^2 \\right)}{2} = \\frac{2\\omega_{pe}^2 - \\frac{7}{4}\\omega_{pe}^2}{2} = \\frac{\\frac{1}{4}\\omega_{pe}^2}{2} = \\frac{1}{8}\\omega_{pe}^2$$
Taking the square root:
$$\\gamma_{\\text{max}} = \\frac{1}{\\sqrt{8}}\\omega_{pe} = \\frac{1}{2\\sqrt{2}}\\omega_{pe} \\approx 0.3536 \\omega_{pe}$$
The maximum growth rate is approximately **$0.354 \\omega_{pe}$**, which occurs at wavenumber $k_{\\text{max}} = 0.612 \\omega_{pe} / v_0$. The instability grows violently on the sub-nanosecond timescale of a few plasma oscillation periods."""
        }
    ]
}

with open("plasma_u7.json", "w", encoding="utf-8") as f:
    json.dump(unit7_data, f, indent=2)
print("plasma_u7.json written successfully")

with open("plasma_u8.json", "w", encoding="utf-8") as f:
    json.dump(unit8_data, f, indent=2)
print("plasma_u8.json written successfully")
