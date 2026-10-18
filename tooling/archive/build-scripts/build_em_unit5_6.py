# Build Script for Units 5 and 6: Magnetic Field and Electromagnetic Induction
import json

# =========================================================================
# UNIT 5: Magnetic Field
# =========================================================================
u5_sections = [
    {
        "id": "sec-5-1",
        "number": "§5.1",
        "heading": "The Magnetic Field, Lorentz Force, and Charged Particle Trajectories",
        "simulation": "lorentz-hall-sim",
        "content": """Magnetism originates from electric charges in motion. A magnetic field is established by moving charges or permanent magnetic dipoles and exerts forces exclusively on moving charges.

<h4>1. The Lorentz Force Law</h4>
A particle carrying electric charge $q$ moving with velocity $\\vec{v}$ in a region containing both an electric field $\\vec{E}$ and a magnetic field $\\vec{B}$ experiences the unified <strong>Lorentz Force</strong>:
$$\\vec{F} = q \\left( \\vec{E} + \\vec{v} \\times \\vec{B} \\right)$$
The magnetic force component is:
$$\\vec{F}_B = q (\\vec{v} \\times \\vec{B})$$
Magnitude: $F_B = |q| v B \\sin\\theta$, where $\\theta$ is the angle between $\\vec{v}$ and $\\vec{B}$.
Direction: Governed by the vector cross product (Right-Hand Rule).
SI Unit: **Tesla (T)** ($1 \\text{ Tesla} = 1 \\text{ N}/(\\text{A}\\cdot\\text{m}) = 10^4 \\text{ Gauss}$).

<h4>2. Fundamental Properties of the Magnetic Force</h4>
<ul>
  <li><strong>Zero Work Property:</strong> Because $\\vec{F}_B$ is everywhere perpendicular to velocity $\\vec{v}$ ($\\vec{F}_B \\cdot \\vec{v} = q (\\vec{v} \\times \\vec{B}) \\cdot \\vec{v} \\equiv 0$), the instantaneous power delivered by a magnetic field is identically zero:
  $$P = \\vec{F}_B \\cdot \\vec{v} = 0 \\implies dK = 0$$
  <strong>A static magnetic field can NEVER change the kinetic energy or speed of a charged particle</strong>; it can only alter its direction of motion.</li>
</ul>

<h4>3. Cyclotron Motion and Helical Trajectories</h4>
Consider a particle of mass $m$ and charge $q$ injected into a uniform magnetic field $\\vec{B} = B \\hat{k}$ with initial velocity $\\vec{v}_\\perp = v_x \\hat{i} + v_y \\hat{j}$.
The magnetic force acts as a pure centripetal force:
$$q v_\\perp B = \\frac{m v_\\perp^2}{r} \\implies r_c = \\frac{m v_\\perp}{q B}$$
$r_c$ is the <strong>cyclotron (Larmor) radius</strong>.
The period of circular revolution and the <strong>cyclotron angular frequency</strong> $\\omega_c$ are:
$$T = \\frac{2\\pi r_c}{v_\\perp} = \\frac{2\\pi m}{q B}, \\quad \\omega_c = \\frac{q B}{m}$$
Notice that $\\omega_c$ and $T$ are **completely independent of the particle's speed or orbital radius** (isochronism of the cyclotron).
If the particle possesses a parallel velocity component $v_\\parallel = v_z \\hat{k}$, it executes a **helical path** with pitch $p = v_\\parallel T = \\frac{2\\pi m v_\\parallel}{q B}$."""
    },
    {
        "id": "sec-5-2",
        "number": "§5.2",
        "heading": "Magnetic Force on a Current-Carrying Conductor and Torque on a Current Loop",
        "simulation": "lorentz-hall-sim",
        "content": """Because electric current consists of an ensemble of moving charges, magnetic forces manifest macroscopically on current-carrying wires.

<h4>1. Magnetic Force on a Wire Element</h4>
Consider a differential segment of wire of cross-section $A$ and length $d\\vec{l}$ carrying current $I = n q A v_d$.
The number of charge carriers in the segment is $dN = n A dl$.
The total magnetic force on the element is:
$$d\\vec{F} = dN \\cdot q (\\vec{v}_d \\times \\vec{B}) = (n A dl) q (\\vec{v}_d \\times \\vec{B}) = (n q A v_d) (d\\vec{l} \\times \\vec{B})$$
$$d\\vec{F} = I (d\\vec{l} \\times \\vec{B})$$
For a straight wire of finite length $\\vec{L}$ in a uniform magnetic field:
$$\\vec{F} = I (\\vec{L} \\times \\vec{B})$$

<h4>2. Torque on a Planar Current Loop and Magnetic Dipole Moment</h4>
Consider a closed rectangular loop of dimensions $a \\times b$ (area $A = ab$) carrying current $I$ in a uniform magnetic field $\\vec{B}$.
The net translational force vanishes ($\vec{F}_{\text{net}} = 0$).
However, forces on opposite arms form a couple, generating net torque:
$$\\vec{\\tau} = \\vec{\\mu} \\times \\vec{B}$$
where $\\vec{\\mu}$ is the <strong>magnetic dipole moment vector</strong>:
$$\\vec{\\mu} = N I \\vec{A} = N I A \\hat{n}$$
for a coil of $N$ turns, where $\\hat{n}$ is the unit normal given by the right-hand grip rule.
SI Unit: $\\text{A}\\cdot\\text{m}^2 = \\text{J/T}$.
The potential energy of the magnetic dipole in field $\\vec{B}$ is:
$$U = -\\vec{\\mu} \\cdot \\vec{B} = -\\mu B \\cos\\theta$$

<h4>3. The Moving-Coil Galvanometer</h4>
In a d'Arsonval galvanometer, a rectangular coil of $N$ turns is suspended in a cylindrical soft iron core that produces a radial magnetic field ($\vec{B} \parallel$ plane of coil always, $\sin\theta = 1$).
Deflecting magnetic torque: $\\tau_d = N I A B$.
Restoring torsional torque of phosphor-bronze suspension fiber: $\\tau_r = C \\theta$.
In equilibrium ($\tau_d = \tau_r$):
$$\\theta = \\left( \\frac{N A B}{C} \\right) I$$
The angular deflection is strictly linear with current.
<ul>
  <li><strong>Current Sensitivity ($S_I$):</strong> $S_I = \\frac{\\theta}{I} = \\frac{N A B}{C}$ (rad/A or div/$\\mu$A).</li>
  <li><strong>Voltage Sensitivity ($S_V$):</strong> $S_V = \\frac{\\theta}{V} = \\frac{N A B}{C R_g}$ (rad/V).</li>
</ul>"""
    },
    {
        "id": "sec-5-3",
        "number": "§5.3",
        "heading": "The Hall Effect and Galvanomagnetic Measurement",
        "simulation": "lorentz-hall-sim",
        "content": """Edwin Herbert Hall (1879) discovered that when a magnetic field is applied perpendicular to a current-carrying conducting strip, a transverse potential difference develops across the strip.

<h4>1. Physical Mechanism of the Hall Effect</h4>
Consider a flat conducting slab of width $w$ and thickness $t$ carrying current $I$ along $+x$.
A uniform magnetic field $\\vec{B} = B \\hat{k}$ is applied along $+z$.
<ol>
  <li>Charge carriers moving with drift velocity $\\vec{v}_d$ experience transverse Lorentz magnetic force:
  $$\\vec{F}_B = q (\\vec{v}_d \\times \\vec{B})$$</li>
  <li>If charge carriers are **negative electrons** ($q = -e, \\vec{v}_d = -v_d \\hat{i}$):
  $$\\vec{F}_B = (-e) [(-v_d \\hat{i}) \\times (B \\hat{k})] = -e v_d B \\hat{j}$$
  Electrons are deflected toward the bottom edge, charging it negative and leaving the top edge positive.</li>
  <li>If charge carriers are **positive holes** ($q = +e, \\vec{v}_d = +v_d \\hat{i}$):
  $$\\vec{F}_B = (+e) [(+v_d \\hat{i}) \\times (B \\hat{k})] = -e v_d B \\hat{j}$$
  Positive charges also deflect downward, charging the bottom edge positive!</li>
</ol>
<em>Sign of Carriers:</em> The polarity of the transverse **Hall Voltage ($V_H$)** immediately reveals the sign of the charge carriers (confirming that metals conduct via negative electrons, while p-type semiconductors conduct via positive holes).

<h4>2. Derivation of the Hall Voltage and Hall Coefficient</h4>
Accumulating transverse charge creates a transverse Hall electric field $\\vec{E}_H$ pointing toward the negative edge.
At steady state, the electrostatic force balances the magnetic force:
$$q E_H = q v_d B \\implies E_H = v_d B$$
The measured transverse potential difference is:
$$V_H = E_H w = v_d B w$$
Using $I = n q A v_d = n q (w t) v_d \\implies v_d = \\frac{I}{n q w t}$:
$$V_H = \\left( \\frac{I}{n q w t} \\right) B w = \\frac{I B}{n q t}$$
We define the <strong>Hall Coefficient ($R_H$)</strong>:
$$R_H = \\frac{E_H}{J B} = \\frac{1}{n q}$$
$$V_H = R_H \\frac{I B}{t}$$
Applications: Hall effect sensors measure magnetic fields non-invasively (Gaussmeters), sense motor rotor position in brushless DC motors, and quantify carrier density $n$ in semiconductor wafer fabrication."""
    },
    {
        "id": "sec-5-4",
        "number": "§5.4",
        "heading": "The Biot-Savart Law and Magnetic Fields of Current Geometries",
        "simulation": "biot-savart-sim",
        "content": """Jean-Baptiste Biot and Félix Savart (1820) established the differential law governing the magnetic field generated by an infinitesimal current element.

<h4>1. The Biot-Savart Law</h4>
The magnetic induction $d\\vec{B}$ at field point $P$ due to a differential current element $I d\\vec{l}$ at source position $\\vec{r}'$ is:
$$d\\vec{B} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times \\hat{r}}{r^2} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times (\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3}$$
where $\\mu_0$ is the <strong>permeability of free space</strong>:
$$\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A (exact by historical definition)} \\approx 1.2566 \\times 10^{-6} \\text{ H/m}$$
For any closed circuit loop $C$:
$$\\vec{B}(\\vec{r}) = \\frac{\\mu_0 I}{4\\pi} \\oint_C \\frac{d\\vec{l}' \\times (\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3}$$

<h4>2. Magnetic Field of a Long Straight Conductor</h4>
Integrating along an infinite straight wire carrying current $I$:
At perpendicular distance $R$:
$$B = \\frac{\\mu_0 I}{4\\pi} \\int_{-\\infty}^\\infty \\frac{dx \\sin\\theta}{r^2} = \\frac{\\mu_0 I}{2\\pi R}$$
Field lines form concentric circles centered on the wire.

<h4>3. Magnetic Field on the Axis of a Circular Current Loop</h4>
Consider a circular wire loop of radius $R$ carrying current $I$ lying in the yz-plane.
At axial distance $x$ along the symmetry axis:
By symmetry, components perpendicular to the axis cancel. The axial component is:
$$B_x = \\int dB \\sin\\alpha = \\frac{\\mu_0 I}{4\\pi (x^2 + R^2)} (2\\pi R) \\left( \\frac{R}{\\sqrt{x^2 + R^2}} \\right)$$
$$B(x) = \\frac{\\mu_0 I R^2}{2(x^2 + R^2)^{3/2}}$$
<ul>
  <li>At the center of the loop ($x = 0$):
  $$B(0) = \\frac{\\mu_0 I}{2R}$$</li>
  <li>Far from the loop ($x \\gg R$): using dipole moment $\\mu = I A = I (\\pi R^2)$:
  $$B(x) \\approx \\frac{\\mu_0 \\mu}{2\\pi x^3}$$
  Decays as $1/x^3$, identical to an electric dipole.</li>
</ul>

<h4>4. Helmholtz Coils</h4>
A pair of identical coaxial coils of radius $R$, separated by distance equal to their radius ($d = R$), carrying identical current $I$ in the same direction.
At the midpoint $x = R/2$:
$$\\frac{dB}{dx} = 0, \\quad \\frac{d^2 B}{dx^2} = 0$$
The second derivative vanishes, producing an exceptionally uniform magnetic field over a wide central volume."""
    },
    {
        "id": "sec-5-5",
        "number": "§5.5",
        "heading": "Ampere's Circuital Law, Solenoids, and Toroids",
        "simulation": "biot-savart-sim",
        "content": """André-Marie Ampère (1826) formulated Ampere's circuital law, the magnetic analog of Gauss's law for high-symmetry current distributions.

<h4>1. Ampere's Circuital Law</h4>
The line integral of magnetic field $\\vec{B}$ around any closed Amperian loop $C$ equals $\\mu_0$ times the total net electric current enclosed by the loop:
$$\\oint_C \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enclosed}}$$
In differential form (applying Stokes' Theorem):
$$\\nabla \\times \\vec{B} = \\mu_0 \\vec{J}$$

<h4>2. The Ideal Long Solenoid</h4>
A helical coil of length $L$ and $N$ closely spaced turns carrying current $I$ ($n = N/L$ turns per unit meter).
Inside an infinitely long solenoid, the magnetic field is uniform and parallel to the axis; outside, it is zero.
Construct a rectangular Amperian loop of length $h$ with one side inside and one outside:
$$\\oint_C \\vec{B} \\cdot d\\vec{l} = B h + 0 + 0 + 0 = B h$$
Enclosed current: $I_{\\text{encl}} = n h I$.
$$B h = \\mu_0 (n h I) \\implies B = \\mu_0 n I$$
The field depends exclusively on turn density $n$ and current $I$, independent of solenoid cross-sectional diameter or position.

<h4>3. The Toroid (Toroidal Solenoid)</h4>
A solenoid bent into a closed donut-shaped ring of inner radius $a$ and outer radius $b$ with $N$ total turns.
Construct a circular Amperian loop of radius $r$ inside the core ($a < r < b$):
$$\\oint \\vec{B} \\cdot d\\vec{l} = B (2\\pi r) = \\mu_0 (N I) \\implies B(r) = \\frac{\\mu_0 N I}{2\\pi r}$$
Outside the toroid ($r < a$ or $r > b$), enclosed current is zero, so $\\vec{B} = 0$ everywhere. Toroids have zero external magnetic leakage."""
    }
]

u5_problems = [
    {
        "id": "prob-5-1",
        "difficulty": "Honors Cyclotron Dynamics Exam Standard",
        "title": "Cyclotron Resonant Frequency and Relativistic Energy",
        "question": "A medical cyclotron accelerates deuterons (mass $m = 3.344 \\times 10^{-27}\\text{ kg}$, charge $q = +1.602 \\times 10^{-19}\\text{ C}$) in a uniform magnetic field $B = 1.50\\text{ Tesla}$. The outer radius of the dees is $R_{\\max} = 0.500\\text{ m}$.\\n(a) Calculate the cyclotron resonant frequency $f_c$ in Megahertz (MHz),\\n(b) Determine the maximum exit speed $v_{\\max}$ of the deuterons, and\\n(c) Find the maximum kinetic energy $K_{\\max}$ in both Joules and Mega-electron-volts (MeV).",
        "steps": [
            {
                "title": "Step 1: Compute cyclotron resonance frequency",
                "math": "$$\\omega_c = \\frac{q B}{m} = \\frac{(1.6022 \\times 10^{-19} \\text{ C}) \\times 1.50 \\text{ T}}{3.344 \\times 10^{-27} \\text{ kg}} = \\frac{2.4033 \\times 10^{-19}}{3.344 \\times 10^{-27}} = 7.1869 \\times 10^7 \\text{ rad/s}$$\n$$f_c = \\frac{\\omega_c}{2\\pi} = \\frac{7.1869 \\times 10^7}{2\\pi} = 1.1438 \\times 10^7 \\text{ Hz} = 11.44 \\text{ MHz}$$",
                "explanation": "The RF oscillator driving the dees must oscillate at 11.44 MHz."
            },
            {
                "title": "Step 2: Maximum speed at outer radius",
                "math": "$$v_{\\max} = \\omega_c R_{\\max} = (7.1869 \\times 10^7 \\text{ rad/s}) \\times 0.500 \\text{ m} = 3.5935 \\times 10^7 \\text{ m/s}$$\n$$\\frac{v_{\\max}}{c} = \\frac{3.5935 \\times 10^7}{3.00 \\times 10^8} = 0.120 = 12.0\\% \\text{ of light speed}$$",
                "explanation": "The deuterons emerge at 12% the speed of light."
            },
            {
                "title": "Step 3: Maximum kinetic energy",
                "math": "$$K_{\\max} = \\frac{1}{2} m v_{\\max}^2 = \\frac{1}{2} \\times (3.344 \\times 10^{-27} \\text{ kg}) \\times (3.5935 \\times 10^7 \\text{ m/s})^2$$\n$$K_{\\max} = 0.5 \\times 3.344 \\times 10^{-27} \\times 1.2913 \\times 10^{15} = 2.159 \\times 10^{-12} \\text{ Joules}$$\n$$K_{\\max} = \\frac{2.159 \\times 10^{-12} \\text{ J}}{1.6022 \\times 10^{-13} \\text{ J/MeV}} = 13.48 \\text{ MeV}$$",
                "explanation": "The cyclotron delivers a beam of 13.5 MeV deuterons."
            }
        ]
    },
    {
        "id": "prob-5-2",
        "difficulty": "Experimental Solid-State Physics Standard",
        "title": "Hall Effect Carrier Density and Hall Coefficient",
        "question": "A thin rectangular strip of n-type germanium has width $w = 6.00\\text{ mm}$ and thickness $t = 0.500\\text{ mm}$. A longitudinal current $I = 25.0\\text{ mA}$ is driven through the strip in a perpendicular magnetic field $B = 0.800\\text{ Tesla}$. A digital millivoltmeter across the width records a transverse Hall voltage $V_H = -18.5\\text{ mV}$.\\n(a) Determine the Hall coefficient $R_H$ of the germanium sample,\\n(b) Calculate the conduction electron number density $n$, and\\n(c) Find the electron drift speed $v_d$ under these operating conditions.",
        "steps": [
            {
                "title": "Step 1: Calculate Hall coefficient RH",
                "math": "$$V_H = R_H \\frac{I B}{t} \\implies R_H = \\frac{V_H t}{I B}$$\n$$R_H = \\frac{(-18.5 \\times 10^{-3} \\text{ V}) \\times (0.500 \\times 10^{-3} \\text{ m})}{(25.0 \\times 10^{-3} \\text{ A}) \\times (0.800 \\text{ T})} = \\frac{-9.25 \\times 10^{-6}}{0.0200} = -4.625 \\times 10^{-4} \\text{ m}^3/\\text{C}$$",
                "explanation": "The negative sign of $R_H$ confirms that majority charge carriers are electrons."
            },
            {
                "title": "Step 2: Calculate electron carrier density n",
                "math": "$$R_H = -\\frac{1}{n e} \\implies n = \\frac{1}{|R_H| e}$$\n$$n = \\frac{1}{(4.625 \\times 10^{-4}) \\times (1.6022 \\times 10^{-19})} = \\frac{1}{7.410 \\times 10^{-23}} = 1.3495 \\times 10^{22} \\text{ electrons/m}^3$$",
                "explanation": "Carrier density in this doped semiconductor is $1.35 \\times 10^{22}$ m⁻³."
            },
            {
                "title": "Step 3: Electron drift speed",
                "math": "$$v_d = \\frac{E_H}{B} = \\frac{|V_H| / w}{B} = \\frac{18.5 \\times 10^{-3} \\text{ V} / (6.00 \\times 10^{-3} \\text{ m})}{0.800 \\text{ T}} = \\frac{3.0833 \\text{ V/m}}{0.800 \\text{ T}} = 3.854 \\text{ m/s}$$",
                "explanation": "In semiconductors, because carrier density is low, drift velocity is much faster (3.85 m/s) than in copper."
            }
        ]
    },
    {
        "id": "prob-5-3",
        "difficulty": "Undergraduate Classical Exam Problem",
        "title": "Biot-Savart Law for a Circular Coil and Axial Magnetic Field",
        "question": "A circular flat coil of radius $R = 10.0\\text{ cm}$ contains $N = 250$ closely wound turns and carries current $I = 2.40\\text{ A}$.\\n(a) Calculate the magnetic field at the center of the coil $B(0)$,\\n(b) Find the axial distance $x$ where the magnetic field drops to $1/8$ of its value at the center, and\\n(c) Calculate the magnetic dipole moment $\\mu$ of the coil.",
        "steps": [
            {
                "title": "Step 1: Compute magnetic field at coil center",
                "math": "$$B(0) = \\frac{\\mu_0 N I}{2R} = \\frac{(4\\pi \\times 10^{-7}) \\times 250 \\times 2.40}{2 \\times 0.100}$$\n$$B(0) = \\frac{(1.2566 \\times 10^{-6}) \\times 600}{0.200} = \\frac{7.5398 \\times 10^{-4}}{0.200} = 3.770 \\times 10^{-3} \\text{ Tesla} = 3.77 \\text{ mT}$$",
                "explanation": "At the center of the 250-turn coil, field magnitude is 3.77 mT."
            },
            {
                "title": "Step 2: Find axial distance for 1/8 field strength",
                "math": "$$B(x) = \\frac{\\mu_0 N I R^2}{2 (R^2 + x^2)^{3/2}} = \\frac{B(0) R^3}{(R^2 + x^2)^{3/2}} = \\frac{1}{8} B(0)$$\n$$\\frac{R^3}{(R^2 + x^2)^{3/2}} = \\frac{1}{8} \\implies \\frac{(R^2 + x^2)^{3/2}}{R^3} = 8$$\n$$\\left( \\frac{R^2 + x^2}{R^2} \\right)^{3/2} = 8 = 2^3 \\implies \\frac{R^2 + x^2}{R^2} = (2^3)^{2/3} = 2^2 = 4$$\n$$1 + \\frac{x^2}{R^2} = 4 \\implies \\frac{x^2}{R^2} = 3 \\implies x = R \\sqrt{3}$$\n$$x = 10.0 \\text{ cm} \\times \\sqrt{3} = 17.32 \\text{ cm}$$",
                "explanation": "The field drops to one-eighth of its peak value at $x = R\sqrt{3} = 17.3$ cm."
            },
            {
                "title": "Step 3: Magnetic dipole moment",
                "math": "$$\\mu = N I A = N I (\\pi R^2) = 250 \\times 2.40 \\times \\pi (0.100)^2$$\n$$\\mu = 600 \\times \\pi \\times 0.0100 = 6.00 \\pi = 18.85 \\text{ A}\\cdot\\text{m}^2 = 18.85 \\text{ J/T}$$",
                "explanation": "The magnetic dipole moment of the coil is 18.85 A·m²."
            }
        ]
    }
]

unit5_data = {
    "number": 5,
    "title": "Magnetic Field",
    "leadSummary": "Lorentz force on moving charges and currents, cyclotron motion and helical trajectories, magnetic torque on current loops, moving-coil galvanometers, the Hall effect, the Biot-Savart law with circular loop applications, and Ampere's circuital law applied to straight conductors, solenoids, and toroids.",
    "sections": u5_sections,
    "problems": u5_problems
}

with open("em_u5.json", "w") as f:
    json.dump(unit5_data, f, indent=2)

print("Unit 5 built successfully with", len(u5_sections), "sections and", len(u5_problems), "problems!")

# =========================================================================
# UNIT 6: Electromagnetic Induction and Inductance
# =========================================================================
u6_sections = [
    {
        "id": "sec-6-1",
        "number": "§6.1",
        "heading": "Faraday's Law of Induction and Lenz's Law",
        "simulation": "faraday-induction-sim",
        "content": """Michael Faraday (1831) made the epochal discovery that a changing magnetic flux induces an electromotive force in an electric circuit.

<h4>1. Magnetic Flux</h4>
The <strong>magnetic flux</strong> $\\Phi_B$ through an oriented surface $S$ is defined as:
$$\\Phi_B = \\int_S \\vec{B} \\cdot d\\vec{A}$$
SI Unit: **Weber (Wb)** ($1 \\text{ Weber} = 1 \\text{ T}\\cdot\\text{m}^2 = 1 \\text{ Volt}\\cdot\\text{second}$).

<h4>2. Faraday's Law of Induction</h4>
The induced electromotive force $\\mathcal{E}$ in a closed conducting loop is directly proportional to the negative time rate of change of magnetic flux through the loop:
$$\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$$
For a closely wound coil of $N$ identical turns:
$$\\mathcal{E} = -N \\frac{d\\Phi_B}{dt}$$

<h4>3. Lenz's Law and Conservation of Energy</h4>
Heinrich Lenz (1834) established the physical origin of the negative sign:
<blockquote>
The polarity of the induced electromotive force is always such that any induced current establishes a magnetic field that opposes the original change in magnetic flux that produced it.
</blockquote>
<em>Proof by Conservation of Energy:</em>
If the induced current reinforced the flux change instead of opposing it, a minuscule initial flux increase would induce current creating more flux, accelerating indefinitely without external energy input—a perpetual motion machine.
Because Lenz's law dictates opposition, an external mechanical agent must perform work against magnetic retarding forces to move a magnet or conductor, and this mechanical work is transformed into electrical energy.

<h4>4. Differential Form of Faraday's Law</h4>
Since $\\mathcal{E} = \\oint_C \\vec{E} \\cdot d\\vec{l}$:
$$\\oint_C \\vec{E} \\cdot d\\vec{l} = -\\frac{d}{dt} \\int_S \\vec{B} \\cdot d\\vec{A} = -\\int_S \\frac{\\partial \\vec{B}}{\\partial t} \\cdot d\\vec{A}$$
Applying Stokes' Theorem:
$$\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$$
<em>Revolutionary Consequence:</em> A time-varying magnetic field creates a non-conservative, non-electrostatic **induced electric field** whose field lines form closed continuous loops ($\oint \vec{E} \cdot d\vec{l} \ne 0$)!"""
    },
    {
        "id": "sec-6-2",
        "number": "§6.2",
        "heading": "Motional EMF, Eddy Currents, and Magnetic Braking",
        "simulation": "faraday-induction-sim",
        "content": """Electromotive force can also arise purely from the physical motion of a conductor through a static magnetic field.

<h4>1. Motional EMF</h4>
Consider a conducting rod of length $L$ sliding with velocity $\\vec{v}$ along frictionless parallel rails in a uniform magnetic field $\\vec{B}$ perpendicular to the rail plane.
Free electrons in the rod experience magnetic Lorentz force:
$$\\vec{F}_m = -e (\\vec{v} \\times \\vec{B})$$
This force pushes electrons to one end, creating an internal electrostatic separating field $\\vec{E}_{\\text{ind}}$:
$$\\mathcal{E} = \\int_0^L (\\vec{v} \\times \\vec{B}) \\cdot d\\vec{l} = v B L$$
Alternatively, via Faraday's flux rule:
$$\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -\\frac{d}{dt}(B L x) = -B L \\frac{dx}{dt} = -B L v$$
If the rails are connected to an external load resistor $R$, induced current is $I = \\mathcal{E}/R = BLv/R$.
The current-carrying rod experiences a retarding magnetic drag force:
$$F_{\\text{drag}} = I L B = \\frac{B^2 L^2 v}{R}$$
The mechanical power required to pull the rod equals the electrical power dissipated as Joule heat:
$$P_{\\text{mech}} = F_{\\text{drag}} v = \\frac{B^2 L^2 v^2}{R} = I^2 R = P_{\\text{elec}}$$

<h4>2. Eddy Currents and Induction Heating</h4>
When a solid metallic block moves through a localized magnetic field, circulating loops of induced current termed **eddy currents (Foucault currents)** are set up within the bulk metal:
<ul>
  <li><strong>Magnetic Braking:</strong> By Lenz's law, eddy currents oppose the relative motion, generating smooth, wear-free braking forces (used in high-speed bullet trains and rollercoasters).</li>
  <li><strong>Lamination of Transformer Cores:</strong> Eddy currents cause severe $I^2 R$ energy losses. Transformer cores are assembled from thin, insulated silicon-steel laminations to interrupt eddy current loops, slashing core losses by over 95%.</li>
</ul>"""
    },
    {
        "id": "sec-6-3",
        "number": "§6.3",
        "heading": "Self-Inductance, Mutual Inductance, and Inductive Coupling",
        "simulation": "faraday-induction-sim",
        "content": """When the current through a circuit changes, its own magnetic flux varies, inducing a back EMF in the circuit itself—a phenomenon termed self-induction.

<h4>1. Self-Inductance ($L$)</h4>
The magnetic flux linkage $N\\Phi_B$ through a circuit carrying current $I$ is directly proportional to $I$:
$$N \\Phi_B = L I \\implies L = \\frac{N \\Phi_B}{I}$$
The constant of proportionality $L$ is the <strong>Self-Inductance</strong>.
SI Unit: **Henry (H)** ($1 \\text{ Henry} = 1 \\text{ Wb/A} = 1 \\text{ V}\\cdot\\text{s/A}$).
By Faraday's law, the **self-induced back EMF** is:
$$\\mathcal{E}_L = -N \\frac{d\\Phi_B}{dt} = -L \\frac{dI}{dt}$$
Inductance represents the electrical inertia of a circuit; it opposes any change in current.

<h4>2. Self-Inductance of an Ideal Solenoid</h4>
For a long solenoid of length $l$, cross-sectional area $A$, and $N$ total turns ($n = N/l$):
$$B = \\mu_0 n I = \\mu_0 \\left(\\frac{N}{l}\\right) I$$
$$\\Phi_B = B A = \\mu_0 \\left(\\frac{N}{l}\\right) A I$$
$$L = \\frac{N \\Phi_B}{I} = \\frac{N [\\mu_0 (N/l) A I]}{I} = \\mu_0 \\frac{N^2 A}{l} = \\mu_0 n^2 A l = \\mu_0 n^2 \\cdot (\\text{Volume})$$
Inductance scales with the square of the turn count ($L \\propto N^2$).
If the core is filled with ferromagnetic material of relative permeability $\\mu_r$: $L = \\mu_0 \\mu_r n^2 A l$.

<h4>3. Mutual Inductance ($M$) and Coupling Coefficient</h4>
When two coils 1 and 2 are in proximity, changing current $I_1$ in coil 1 produces changing flux $\\Phi_{21}$ through coil 2:
$$\\mathcal{E}_2 = -M_{21} \\frac{dI_1}{dt}, \\quad \\mathcal{E}_1 = -M_{12} \\frac{dI_2}{dt}$$
By the Neumann Reciprocity Theorem:
$$M_{12} = M_{21} = M$$
The <strong>magnetic coupling coefficient</strong> $k$ is:
$$k = \\frac{M}{\\sqrt{L_1 L_2}}, \\quad 0 \\le k \\le 1$$
$k = 1$ denotes ideal perfect magnetic flux linkage (toroidal transformers)."""
    },
    {
        "id": "sec-6-4",
        "number": "§6.4",
        "heading": "LR Circuit Transients and Magnetic Field Energy Storage",
        "simulation": "faraday-induction-sim",
        "content": """In circuits containing resistors and inductors, the back EMF prevents instantaneous changes in current.

<h4>1. Growth of Current in a Series LR Circuit</h4>
A battery $\\mathcal{E}$, resistor $R$, and inductor $L$ are connected in series; switch closed at $t = 0$.
KVL:
$$\\mathcal{E} - i R - L \\frac{di}{dt} = 0 \\implies L \\frac{di}{dt} + R i = \\mathcal{E}$$
Solving with initial condition $i(0) = 0$:
$$i(t) = \\frac{\\mathcal{E}}{R} \\left( 1 - e^{-t/\\tau_L} \\right) = I_0 \\left( 1 - e^{-t/\\tau_L} \\right)$$
where $\\tau_L = \\frac{L}{R}$ is the <strong>inductive time constant</strong> (Units: seconds, $\\text{H}/\\Omega = \\text{s}$).
<ul>
  <li>At $t = 0$: $i = 0$, back EMF is maximum ($\\mathcal{E}_L = -\\mathcal{E}$). The inductor acts as an open circuit.</li>
  <li>At $t = \\tau_L$: Current reaches $(1 - 1/e) \\approx 63.2\\%$ of $I_0$.</li>
  <li>At $t \\to \\infty$: $di/dt \\to 0$, $i \\to I_0 = \\mathcal{E}/R$. The inductor acts as an ideal zero-resistance short circuit.</li>
</ul>

<h4>2. Decay of Current in an LR Circuit</h4>
When the battery is switched out:
$$L \\frac{di}{dt} + R i = 0 \\implies i(t) = I_0 e^{-t/\\tau_L}$$

<h4>3. Energy Stored in a Magnetic Field</h4>
To establish current $I$ against the opposing back EMF, the source must perform work:
$$dW = P dt = (-\\mathcal{E}_L) i \\, dt = \\left( L \\frac{di}{dt} \\right) i \\, dt = L i \\, di$$
Integrating from $i = 0$ to $i = I$:
$$U_B = \\int_0^I L i \\, di = \\frac{1}{2} L I^2$$
For a long solenoid where $L = \\mu_0 n^2 A l$ and $B = \\mu_0 n I \\implies I = B / (\\mu_0 n)$:
$$U_B = \\frac{1}{2} (\\mu_0 n^2 A l) \\left( \\frac{B}{\\mu_0 n} \\right)^2 = \\frac{B^2}{2\\mu_0} (A l)$$
Because $Al$ is the enclosed core volume, the <strong>magnetic energy density</strong> $u_B$ (J/m³) is:
$$u_B = \\frac{B^2}{2\\mu_0} = \\frac{1}{2} \\vec{B} \\cdot \\vec{H}$$
Analogous to $u_E = \\frac{1}{2}\\epsilon_0 E^2$, magnetic energy is localized continuously throughout the space occupied by the magnetic field!"""
    }
]

u6_problems = [
    {
        "id": "prob-6-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Motional EMF and Dynamic Terminal Velocity",
        "question": "A metal rod of mass $m = 40.0\\text{ g}$ and length $L = 25.0\\text{ cm}$ slides downward under gravity along two frictionless vertical conductive rails separated by distance $L$. The rails are connected at the top by a resistor $R = 2.50\\ \\Omega$. A uniform horizontal magnetic field $B = 1.20\\text{ Tesla}$ is directed perpendicular to the rail plane. Acceleration due to gravity $g = 9.80\\text{ m/s}^2$.\\n(a) Derive an expression for the motional EMF $\\mathcal{E}(v)$ and induced current $I(v)$ as a function of downward velocity $v$,\\n(b) Calculate the steady-state terminal velocity $v_t$ attained by the falling rod, and\\n(c) Verify that at terminal velocity, the rate of loss of gravitational potential energy equals the electrical power dissipated in resistor $R$.",
        "steps": [
            {
                "title": "Step 1: Express motional EMF, current, and magnetic drag",
                "math": "$$\\mathcal{E} = B L v$$\n$$I = \\frac{\\mathcal{E}}{R} = \\frac{B L v}{R}$$\n$$F_{\\text{drag}} = I L B = \\frac{B^2 L^2 v}{R} \\quad (\\text{directed upward by Lenz's law})$$",
                "explanation": "As velocity increases, upward magnetic drag force grows linearly with $v$."
            },
            {
                "title": "Step 2: Terminal velocity equilibrium",
                "math": "$$m g - F_{\\text{drag}} = 0 \\implies m g = \\frac{B^2 L^2 v_t}{R}$$\n$$v_t = \\frac{m g R}{B^2 L^2} = \\frac{(0.0400 \\text{ kg}) \\times (9.80 \\text{ m/s}^2) \\times (2.50\\ \\Omega)}{(1.20 \\text{ T})^2 \\times (0.250 \\text{ m})^2}$$\n$$v_t = \\frac{0.980}{1.44 \\times 0.0625} = \\frac{0.980}{0.0900} = 10.889 \\text{ m/s} = 10.89 \\text{ m/s}$$",
                "explanation": "The rod accelerates until drag balances gravity, capping terminal speed at 10.89 m/s."
            },
            {
                "title": "Step 3: Power conservation verification",
                "math": "$$P_{\\text{grav}} = m g v_t = (0.0400 \\times 9.80) \\times 10.889 = 0.3920 \\times 10.889 = 4.268 \\text{ Watts}$$\n$$P_{\\text{elec}} = I^2 R = \\left( \\frac{B L v_t}{R} \\right)^2 R = \\frac{B^2 L^2 v_t^2}{R} = \\frac{0.0900 \\times (10.889)^2}{2.50}$$\n$$P_{\\text{elec}} = \\frac{0.0900 \\times 118.57}{2.50} = \\frac{10.671}{2.50} = 4.268 \\text{ Watts}$$\n$$P_{\\text{grav}} = P_{\\text{elec}} = 4.268 \\text{ W} \\implies \\text{Energy strictly conserved!}$$",
                "explanation": "Gravitational potential energy is transformed directly into electrical Joule heating with 100% efficiency."
            }
        ]
    },
    {
        "id": "prob-6-2",
        "difficulty": "Honors Inductance Problem",
        "title": "Self-Inductance and Stored Energy of a Toroidal Inductor",
        "question": "A toroidal coil has a rectangular cross-section with inner radius $a = 8.00\\text{ cm}$, outer radius $b = 14.0\\text{ cm}$, and axial height $h = 5.00\\text{ cm}$. It consists of $N = 1200$ closely wound turns of copper wire carrying steady current $I = 4.00\\text{ A}$ in air ($\\mu_r = 1.00$).\\n(a) Derive the exact analytical formula for the self-inductance $L$ taking into account the radial variation of $B(r)$,\\n(b) Calculate the numerical self-inductance in millihenries (mH), and\\n(c) Find the total magnetic energy stored in the toroid.",
        "steps": [
            {
                "title": "Step 1: Integrate magnetic flux over cross-section",
                "math": "$$B(r) = \\frac{\\mu_0 N I}{2\\pi r}$$\n$$dA = h \\, dr$$\n$$\\Phi_B = \\int_a^b B(r) (h \\, dr) = \\frac{\\mu_0 N I h}{2\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$\n$$L = \\frac{N \\Phi_B}{I} = \\frac{\\mu_0 N^2 h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$",
                "explanation": "Because the magnetic field varies inversely with radius across the core, flux integration is logarithmic."
            },
            {
                "title": "Step 2: Numerical evaluation of self-inductance",
                "math": "$$\\ln(b/a) = \\ln(14.0 / 8.00) = \\ln(1.75) = 0.55962$$\n$$L = \\frac{(4\\pi \\times 10^{-7}) \\times (1200)^2 \\times 0.0500}{2\\pi} \\times 0.55962$$\n$$L = 2 \\times 10^{-7} \\times (1.44 \\times 10^6) \\times 0.0500 \\times 0.55962$$\n$$L = 0.0144 \\times 0.55962 = 8.0585 \\times 10^{-3} \\text{ Henry} = 8.06 \\text{ mH}$$",
                "explanation": "The toroid has a self-inductance of 8.06 millihenries."
            },
            {
                "title": "Step 3: Stored magnetic energy",
                "math": "$$U_B = \\frac{1}{2} L I^2 = \\frac{1}{2} \\times (8.0585 \\times 10^{-3} \\text{ H}) \\times (4.00 \\text{ A})^2$$\n$$U_B = 0.5 \\times 8.0585 \\times 10^{-3} \\times 16.0 = 6.447 \\times 10^{-2} \\text{ Joules} = 64.5 \\text{ mJ}$$",
                "explanation": "The toroid stores 64.5 mJ of magnetic energy completely confined within its core."
            }
        ]
    },
    {
        "id": "prob-6-3",
        "difficulty": "Standard University Exam Problem",
        "title": "LR Circuit Transients and Inductive Back EMF",
        "question": "A series LR circuit has an inductor $L = 2.50\\text{ H}$ and a resistor $R = 50.0\\ \\Omega$ connected across an ideal DC source $\\mathcal{E} = 120.0\\text{ V}$. The circuit switch is closed at $t = 0$.\\n(a) Determine the inductive time constant $\\tau_L$ and steady-state maximum current $I_0$,\\n(b) Find the instantaneous current $i(t)$ and back EMF $\\mathcal{E}_L(t)$ at $t = 0.0500\\text{ s}$, and\\n(c) At what time $t$ will the energy stored in the magnetic field reach $50.0\\%$ of its final maximum value?",
        "steps": [
            {
                "title": "Step 1: Compute time constant and steady-state current",
                "math": "$$\\tau_L = \\frac{L}{R} = \\frac{2.50 \\text{ H}}{50.0\\ \\Omega} = 0.0500 \\text{ seconds} = 50.0 \\text{ ms}$$\n$$I_0 = \\frac{\\mathcal{E}}{R} = \\frac{120.0 \\text{ V}}{50.0\\ \\Omega} = 2.400 \\text{ Amperes}$$",
                "explanation": "The inductive time constant is exactly 50 ms and maximum current is 2.40 A."
            },
            {
                "title": "Step 2: Current and back EMF at t = 50 ms (one time constant)",
                "math": "$$i(\\tau_L) = I_0 (1 - e^{-1}) = 2.400 \\times (1 - 0.36788) = 2.400 \\times 0.63212 = 1.517 \\text{ Amperes}$$\n$$\\mathcal{E}_L(t) = -\\mathcal{E} e^{-t/\\tau_L} \\implies |\\mathcal{E}_L(\\tau_L)| = 120.0 \\times e^{-1} = 120.0 \\times 0.36788 = 44.15 \\text{ Volts}$$",
                "explanation": "After one time constant, current reaches 1.52 A (63.2%) and back EMF drops to 44.1 V (36.8%)."
            },
            {
                "title": "Step 3: Time to achieve 50% stored magnetic energy",
                "math": "$$U_B(t) = \\frac{1}{2} L [i(t)]^2 = 0.500 U_{B,\\max} = 0.500 \\left( \\frac{1}{2} L I_0^2 \\right)$$\n$$[i(t)]^2 = 0.500 I_0^2 \\implies i(t) = \\frac{I_0}{\\sqrt{2}} = 0.7071 I_0$$\n$$I_0 (1 - e^{-t/\\tau_L}) = 0.7071 I_0 \\implies e^{-t/\\tau_L} = 1 - 0.7071 = 0.2929$$\n$$-\\frac{t}{\\tau_L} = \\ln(0.2929) = -1.228 \\implies t = 1.228 \\tau_L$$\n$$t = 1.228 \\times 0.0500 \\text{ s} = 0.0614 \\text{ seconds} = 61.4 \\text{ ms}$$",
                "explanation": "Because energy scales as $i^2$, current must reach $1/\sqrt{2} \approx 70.7\%$ of maximum, requiring 61.4 ms."
            }
        ]
    }
]

unit6_data = {
    "number": 6,
    "title": "Electromagnetic Induction and Inductance",
    "leadSummary": "Faraday's law of induction, Lenz's law and energy conservation, motional EMF, eddy currents and magnetic damping, self-inductance of solenoids and toroids, mutual inductance and coupling coefficient, LR circuit growth and decay transients, and magnetic field energy storage.",
    "sections": u6_sections,
    "problems": u6_problems
}

with open("em_u6.json", "w") as f:
    json.dump(unit6_data, f, indent=2)

print("Unit 6 built successfully with", len(u6_sections), "sections and", len(u6_problems), "problems!")
