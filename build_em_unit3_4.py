# Build Script for Units 3 and 4: Capacitors & Dielectrics and Current & Resistance
import json

# =========================================================================
# UNIT 3: Capacitors and Dielectrics
# =========================================================================
u3_sections = [
    {
        "id": "sec-3-1",
        "number": "§3.1",
        "heading": "Capacitor Fundamentals and Geometric Capacitance Calculations",
        "simulation": "dielectric-capacitor-sim",
        "content": """A capacitor is a passive circuit component designed to store electric charge and electrostatic energy within an electric field established between two isolated conductors.

<h4>1. Definition of Capacitance</h4>
When equal and opposite charges $+Q$ and $-Q$ are deposited on two conducting electrodes separated by an insulating gap, a potential difference $V$ develops between them.
The <strong>capacitance</strong> $C$ is defined as the ratio of the magnitude of stored charge on either conductor to the potential difference:
$$C = \\frac{Q}{V}$$
SI Unit: **Farad (F)** ($1 \\text{ Farad} = 1 \\text{ Coulomb/Volt}$).
Because 1 Farad is exceptionally large, practical capacitors are measured in microfarads ($\\mu\\text{F} = 10^{-6}\\text{ F}$), nanofarads ($\\text{nF} = 10^{-9}\\text{ F}$), or picofarads ($\\text{pF} = 10^{-12}\\text{ F}$).
Capacitance depends strictly on geometric shape, dimensions, and the permittivity of the medium, completely independent of applied charge or voltage.

<h4>2. Parallel-Plate Capacitor</h4>
Consider two parallel planar conducting plates of area $A$ separated by vacuum gap $d$ ($d \\ll \\sqrt{A}$ to minimize fringe fields).
Charge density is $\\sigma = Q/A$. By Gauss's law, the uniform electric field between plates is:
$$E = \\frac{\\sigma}{\\epsilon_0} = \\frac{Q}{\\epsilon_0 A}$$
The potential difference is:
$$V = \\int_0^d E \\, dz = E d = \\frac{Q d}{\\epsilon_0 A}$$
Therefore, the capacitance is:
$$C = \\frac{Q}{V} = \\frac{\\epsilon_0 A}{d}$$

<h4>3. Cylindrical Capacitor (Coaxial Cable)</h4>
Consider two concentric cylindrical conductors of length $L$ ($L \\gg b$), inner radius $a$, and outer radius $b$.
With linear charge density $\\lambda = Q/L$, the radial electric field between cylinders is $E(r) = \\frac{\\lambda}{2\\pi\\epsilon_0 r}$.
The potential difference is:
$$V = \\int_a^b E(r) dr = \\frac{\\lambda}{2\\pi\\epsilon_0} \\int_a^b \\frac{dr}{r} = \\frac{Q}{2\\pi\\epsilon_0 L} \\ln\\left(\\frac{b}{a}\\right)$$
$$C = \\frac{Q}{V} = \\frac{2\\pi\\epsilon_0 L}{\\ln(b/a)}$$
Capacitance per unit length: $\\frac{C}{L} = \\frac{2\\pi\\epsilon_0}{\\ln(b/a)}$ (crucial for RF transmission lines).

<h4>4. Spherical Capacitor</h4>
Consider two concentric conducting spheres of inner radius $a$ and outer radius $b$.
Radial field: $E(r) = \\frac{Q}{4\\pi\\epsilon_0 r^2}$.
$$V = \\int_a^b \\frac{Q}{4\\pi\\epsilon_0 r^2} dr = \\frac{Q}{4\\pi\\epsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) = \\frac{Q (b - a)}{4\\pi\\epsilon_0 a b}$$
$$C = \\frac{4\\pi\\epsilon_0 a b}{b - a}$$
For an **isolated spherical conductor** ($b \\to \\infty$, outer shell at infinity):
$$C_{\\text{isolated}} = 4\\pi\\epsilon_0 a$$
For Earth ($a \\approx 6.371 \\times 10^6\\text{ m}$): $C_{\\text{Earth}} \\approx 709 \\ \\mu\\text{F}$."""
    },
    {
        "id": "sec-3-2",
        "number": "§3.2",
        "heading": "Dielectric Media, Bound Charges, and Gauss's Law in Dielectrics",
        "simulation": "dielectric-capacitor-sim",
        "content": """When an insulating material (dielectric) is inserted into an electric field, its constituent atoms or molecules undergo microscopic polarization.

<h4>1. Molecular Mechanism of Dielectrics</h4>
Dielectric materials belong to two classes:
<ul>
  <li><strong>Non-Polar Dielectrics (e.g., $N_2, O_2, CH_4$):</strong> Molecular centers of positive and negative charge coincide in the absence of an external field. An applied field $\\vec{E}_0$ exerts opposite forces on electrons and nuclei, inducing microscopic dipole moments $\\vec{p} = \\alpha \\vec{E}_{\\text{loc}}$ (electronic polarization).</li>
  <li><strong>Polar Dielectrics (e.g., $H_2O, HCl$):</strong> Molecules possess permanent dipole moments. Thermal motion causes random orientations. An applied field $\\vec{E}_0$ exerts torques that partially align the dipoles along $\\vec{E}_0$ (orientational polarization).</li>
</ul>

<h4>2. Induced Bound Charge and Field Reduction</h4>
The aligned dipoles create microscopic cancellation inside the bulk, but leave net unneutralized <strong>bound surface charges</strong> $\\pm Q_b$ (or surface density $\\sigma_b$) on the dielectric faces.
These bound charges set up an internal opposing electric field $\\vec{E}_b = -(\\sigma_b / \\epsilon_0) \\hat{n}$.
The net resultant electric field inside the dielectric is:
$$\\vec{E} = \\vec{E}_0 + \\vec{E}_b = \\frac{\\vec{E}_0}{\\kappa} = \\frac{\\vec{E}_0}{\\epsilon_r}$$
where $\\kappa = \\epsilon_r > 1$ is the <strong>dielectric constant (relative permittivity)</strong>.
The presence of a dielectric weakens the electric field by a factor of $\\kappa$:
$$E = \\frac{\\sigma - \\sigma_b}{\\epsilon_0} = \\frac{\\sigma}{\\kappa \\epsilon_0} \\implies \\sigma_b = \\sigma \\left( 1 - \\frac{1}{\\kappa} \\right)$$

<h4>3. Capacitance with Dielectric</h4>
Inserting a dielectric slab of constant $\\kappa$ filling the entire gap of a capacitor:
<ul>
  <li><strong>Isolated Capacitor (Constant Charge $Q$):</strong> Potential drops $V = V_0 / \\kappa$; Capacitance increases:
  $$C = \\frac{Q}{V} = \\kappa C_0$$</li>
  <li><strong>Battery-Connected Capacitor (Constant Voltage $V$):</strong> Battery supplies extra charge $Q = \\kappa Q_0$; Capacitance increases $C = \\kappa C_0$.</li>
</ul>"""
    },
    {
        "id": "sec-3-3",
        "number": "§3.3",
        "heading": "The Three Electric Vectors: E, D, and P",
        "simulation": "dielectric-capacitor-sim",
        "content": """To treat macroscopic electrostatics in matter without resolving individual microscopic atomic charges, electromagnetic theory introduces three fundamental vector fields: $\\vec{E}$, $\\vec{D}$, and $\\vec{P}$.

<h4>1. The Electric Polarization Vector ($\\vec{P}$)</h4>
The <strong>polarization vector</strong> $\\vec{P}$ is defined as the electric dipole moment per unit volume of the dielectric medium:
$$\\vec{P} = \\lim_{\\Delta V \\to 0} \\frac{\\sum \\vec{p}_i}{\\Delta V}$$
SI Unit: $\\text{Coulomb/m}^2$ (C/m²).
The polarization $\\vec{P}$ is directly related to bound charges:
$$\\rho_b = -\\nabla \\cdot \\vec{P} \\quad (\\text{Volume bound charge density})$$
$$\\sigma_b = \\vec{P} \\cdot \\hat{n} \\quad (\\text{Surface bound charge density})$$

<h4>2. The Electric Displacement Vector ($\\vec{D}$)</h4>
In a dielectric, total charge density consists of free charges $\\rho_f$ (introduced on metal electrodes) and bound charges $\\rho_b$ (induced in dielectric):
$$\\nabla \\cdot \\vec{E} = \\frac{\\rho_{\\text{total}}}{\\epsilon_0} = \\frac{\\rho_f + \\rho_b}{\\epsilon_0} = \\frac{\\rho_f - \\nabla \\cdot \\vec{P}}{\\epsilon_0}$$
$$\\nabla \\cdot (\\epsilon_0 \\vec{E} + \\vec{P}) = \\rho_f$$
We define the <strong>Electric Displacement Field</strong> $\\vec{D}$ as:
$$\\vec{D} = \\epsilon_0 \\vec{E} + \\vec{P}$$
SI Unit: $\\text{Coulomb/m}^2$ (C/m²).
This yields **Gauss's Law in Dielectric Media**:
$$\\nabla \\cdot \\vec{D} = \\rho_f \\iff \\oint_S \\vec{D} \\cdot d\\vec{A} = Q_{\\text{free, encl}}$$
<em>Major Theoretical Advantage:</em> The flux of $\\vec{D}$ depends **exclusively on free charges** $Q_{\\text{free}}$, completely bypassing the need to know the complex bound charges!

<h4>3. Linear Isotropic Dielectrics and Susceptibility</h4>
For linear dielectrics:
$$\\vec{P} = \\epsilon_0 \\chi_e \\vec{E}$$
where $\\chi_e$ is the dimensionless <strong>electric susceptibility</strong>.
Substituting into $\\vec{D}$:
$$\\vec{D} = \\epsilon_0 \\vec{E} + \\epsilon_0 \\chi_e \\vec{E} = \\epsilon_0 (1 + \\chi_e) \\vec{E} = \\epsilon_0 \\epsilon_r \\vec{E} = \\epsilon \\vec{E}$$
$$\\epsilon_r = 1 + \\chi_e = \\kappa$$
where $\\epsilon = \\epsilon_0 \\epsilon_r$ is the absolute permittivity of the material."""
    },
    {
        "id": "sec-3-4",
        "number": "§3.4",
        "heading": "Electrostatic Energy Storage and Field Energy Density",
        "simulation": "dielectric-capacitor-sim",
        "content": """Charging a capacitor requires performing work against the opposing electric field already created by previously deposited charges.

<h4>1. Work Done in Charging a Capacitor</h4>
Consider charging a capacitor to final charge $Q$ and potential $V$.
When the capacitor carries instantaneous charge $q$, the potential difference is $v = q/C$.
The work required to transfer an additional infinitesimal charge $dq$ from the negative plate to the positive plate is:
$$dW = v \\, dq = \\frac{q}{C} dq$$
The total work required to charge the capacitor from $q = 0$ to $q = Q$ is stored as internal electrostatic potential energy $U$:
$$U = \\int_0^Q \\frac{q}{C} dq = \\frac{Q^2}{2C}$$
Using $Q = C V$:
$$U = \\frac{1}{2} \\frac{Q^2}{C} = \\frac{1}{2} C V^2 = \\frac{1}{2} Q V$$

<h4>2. Spatial Energy Density of the Electric Field ($u_E$)</h4>
Where is this electrostatic energy physically stored? Michael Faraday and James Clerk Maxwell demonstrated that energy resides not on the metal plates, but is distributed continuously throughout the **electric field itself**.
For a parallel-plate capacitor of plate area $A$ and gap $d$:
$$C = \\frac{\\epsilon A}{d}, \\quad V = E d$$
$$U = \\frac{1}{2} C V^2 = \\frac{1}{2} \\left( \\frac{\\epsilon A}{d} \\right) (E d)^2 = \\frac{1}{2} \\epsilon E^2 (A d)$$
Because the volume occupied by the electric field is $\\text{Volume} = A d$, the **electrostatic energy density** $u_E$ (Joules per cubic meter) is:
$$u_E = \\frac{U}{\\text{Volume}} = \\frac{1}{2} \\epsilon E^2 = \\frac{1}{2} \\epsilon_0 \\epsilon_r E^2 = \\frac{1}{2} \\vec{D} \\cdot \\vec{E}$$
This formula holds universally for *any* electric field configuration in vacuum or dielectric media.
The total energy in an arbitrary volume $V$ is:
$$U = \\int_V \\frac{1}{2} (\\vec{D} \\cdot \\vec{E}) dV$$"""
    }
]

u3_problems = [
    {
        "id": "prob-3-1",
        "difficulty": "Honors Capacitance Problem",
        "title": "Coaxial Cylindrical Cable with Two Concentric Dielectrics",
        "question": "A coaxial cable of length $L = 5.00\\text{ m}$ consists of an inner conducting cylinder of radius $a = 2.00\\text{ mm}$ and an outer conducting sheath of radius $c = 8.00\\text{ mm}$. The annular region is filled with two concentric dielectric layers: Layer 1 from $r = a$ to $r = b = 4.00\\text{ mm}$ has dielectric constant $\\kappa_1 = 4.00$, and Layer 2 from $r = b$ to $r = c$ has dielectric constant $\\kappa_2 = 2.25$.\\n(a) Derive an analytical formula for the capacitance $C$,\\n(b) Calculate the numerical capacitance of the 5.00 m cable, and\\n(c) If a potential difference $V = 1200\\text{ V}$ is applied, find the maximum electric field strength inside each dielectric layer.",
        "steps": [
            {
                "title": "Step 1: Model as two cylindrical capacitors in series",
                "math": "$$C_1 = \\frac{2\\pi \\epsilon_0 \\kappa_1 L}{\\ln(b/a)}, \\quad C_2 = \\frac{2\\pi \\epsilon_0 \\kappa_2 L}{\\ln(c/b)}$$\n$$\\frac{1}{C} = \\frac{1}{C_1} + \\frac{1}{C_2} = \\frac{\\ln(b/a)}{2\\pi\\epsilon_0 \\kappa_1 L} + \\frac{\\ln(c/b)}{2\\pi\\epsilon_0 \\kappa_2 L}$$\n$$C = \\frac{2\\pi\\epsilon_0 L}{\\frac{1}{\\kappa_1}\\ln(b/a) + \\frac{1}{\\kappa_2}\\ln(c/b)}$$",
                "explanation": "Because the same free displacement flux passes through both layers, they act as two capacitors in series."
            },
            {
                "title": "Step 2: Numerical evaluation of capacitance",
                "math": "$$\\ln(b/a) = \\ln(4.00 / 2.00) = \\ln(2.00) = 0.69315$$\n$$\\ln(c/b) = \\ln(8.00 / 4.00) = \\ln(2.00) = 0.69315$$\n$$\\text{Denominator} = \\frac{0.69315}{4.00} + \\frac{0.69315}{2.25} = 0.17329 + 0.30807 = 0.48135$$\n$$C = \\frac{2\\pi \\times (8.854 \\times 10^{-12}) \\times 5.00}{0.48135} = \\frac{2.7816 \\times 10^{-10}}{0.48135} = 5.779 \\times 10^{-10} \\text{ F} = 578 \\text{ pF}$$",
                "explanation": "The total capacitance of the composite 5-meter coaxial cable is 578 pF."
            },
            {
                "title": "Step 3: Maximum electric fields in each dielectric layer",
                "math": "$$Q = C V = (5.779 \\times 10^{-10} \\text{ F}) \\times 1200 \\text{ V} = 6.935 \\times 10^{-7} \\text{ C}$$\n$$\\lambda = \\frac{Q}{L} = \\frac{6.935 \\times 10^{-7}}{5.00} = 1.387 \\times 10^{-7} \\text{ C/m}$$\n$$\\text{In Layer 1, max field occurs at inner radius } r = a:$$\n$$E_{1,\\max} = \\frac{\\lambda}{2\\pi \\epsilon_0 \\kappa_1 a} = \\frac{1.387 \\times 10^{-7}}{2\\pi \\times (8.854 \\times 10^{-12}) \\times 4.00 \\times (2.00 \\times 10^{-3})} = \\frac{1.387 \\times 10^{-7}}{4.4505 \\times 10^{-13}} = 3.116 \\times 10^5 \\text{ V/m}$$\n$$\\text{In Layer 2, max field occurs at } r = b:$$\n$$E_{2,\\max} = \\frac{\\lambda}{2\\pi \\epsilon_0 \\kappa_2 b} = \\frac{1.387 \\times 10^{-7}}{2\\pi \\times (8.854 \\times 10^{-12}) \\times 2.25 \\times (4.00 \\times 10^{-3})} = \\frac{1.387 \\times 10^{-7}}{5.0069 \\times 10^{-13}} = 2.770 \\times 10^5 \\text{ V/m}$$",
                "explanation": "Peak dielectric stress occurs right at the surface of the inner copper conductor ($E_{1,\\max} = 312$ kV/m)."
            }
        ]
    },
    {
        "id": "prob-3-2",
        "difficulty": "Advanced Undergraduate Analytical Problem",
        "title": "Electrostatic Attractive Force on a Partially Inserted Dielectric Slab",
        "question": "A parallel plate capacitor has square plates of side length $L = 20.0\\text{ cm}$ and plate separation $d = 2.50\\text{ mm}$. It is held at a constant potential difference $V = 800\\text{ V}$ by a connected battery. A dielectric slab of dielectric constant $\\kappa = 4.50$ and thickness $d$ is inserted a distance $x = 8.00\\text{ cm}$ between the plates.\\n(a) Derive the expression for the total capacitance $C(x)$ as a function of insertion distance $x$,\\n(b) Derive the electrostatic force $F_x$ pulling the dielectric slab inward into the capacitor, and\\n(c) Calculate the numerical magnitude of this attractive force.",
        "steps": [
            {
                "title": "Step 1: Express capacitance as two parallel capacitors",
                "math": "$$\\text{The inserted region has width } x, \\text{ dielectric } \\kappa; \\text{ empty region has width } (L - x):$$\n$$C(x) = C_{\\text{diel}} + C_{\\text{vacuum}} = \\frac{\\kappa \\epsilon_0 L x}{d} + \\frac{\\epsilon_0 L (L - x)}{d}$$\n$$C(x) = \\frac{\\epsilon_0 L}{d} [L + (\\kappa - 1) x]$$",
                "explanation": "The capacitor behaves as two parallel capacitors sharing the same terminal voltage."
            },
            {
                "title": "Step 2: Derive force at constant voltage",
                "math": "$$\\text{Total energy: } U(x) = \\frac{1}{2} C(x) V^2$$\n$$\\text{Because the battery performs work } dW_{\\text{bat}} = V dq = V^2 dC = 2 dU:$$\n$$F_x = +\\left( \\frac{\\partial U}{\\partial x} \\right)_V = \\frac{1}{2} V^2 \\frac{dC}{dx}$$\n$$\\frac{dC}{dx} = \\frac{\\epsilon_0 L (\\kappa - 1)}{d}$$\n$$F_x = \\frac{\\epsilon_0 L (\\kappa - 1) V^2}{2 d}$$",
                "explanation": "The fringing field at the edges creates a non-uniform field gradient that sucks the dielectric inward."
            },
            {
                "title": "Step 3: Numerical calculation of the inward force",
                "math": "$$F_x = \\frac{(8.854 \\times 10^{-12}) \\times 0.200 \\times (4.50 - 1) \\times (800)^2}{2 \\times (2.50 \\times 10^{-3})}$$\n$$F_x = \\frac{(8.854 \\times 10^{-12}) \\times 0.200 \\times 3.50 \\times 6.40 \\times 10^5}{5.00 \\times 10^{-3}}$$\n$$F_x = \\frac{3.9666 \\times 10^{-6}}{5.00 \\times 10^{-3}} = 7.933 \\times 10^{-4} \\text{ Newtons} = 0.793 \\text{ mN}$$",
                "explanation": "The capacitor exerts a continuous inward attractive force of 0.793 mN on the dielectric slab."
            }
        ]
    },
    {
        "id": "prob-3-3",
        "difficulty": "Standard University Exam Problem",
        "title": "Energy Stored in an Isolated Spherical Capacitor",
        "question": "A spherical capacitor consists of two concentric thin metal shells of radii $a = 6.00\\text{ cm}$ and $b = 10.0\\text{ cm}$ separated by air ($\\kappa = 1.00$). The inner shell carries charge $Q = +3.00\\ \\mu\\text{C}$ and the outer shell carries $-3.00\\ \\mu\\text{C}$.\\n(a) Calculate the capacitance $C$ and the potential difference $V$,\\n(b) Calculate the stored electrostatic energy $U$ using $\\frac{1}{2}Q^2/C$, and\\n(c) Verify this result by integrating the field energy density $u_E = \\frac{1}{2}\\epsilon_0 E^2$ over the volume between the shells.",
        "steps": [
            {
                "title": "Step 1: Compute capacitance and potential difference",
                "math": "$$C = \\frac{4\\pi\\epsilon_0 a b}{b - a} = \\frac{4\\pi \\times (8.854 \\times 10^{-12}) \\times 0.0600 \\times 0.100}{0.100 - 0.0600}$$\n$$C = \\frac{6.6758 \\times 10^{-13}}{0.0400} = 1.669 \\times 10^{-11} \\text{ F} = 16.69 \\text{ pF}$$\n$$V = \\frac{Q}{C} = \\frac{3.00 \\times 10^{-6} \\text{ C}}{1.669 \\times 10^{-11} \\text{ F}} = 1.797 \\times 10^5 \\text{ Volts} = 179.7 \\text{ kV}$$",
                "explanation": "The potential difference between the shells is 180 kV."
            },
            {
                "title": "Step 2: Calculate stored energy",
                "math": "$$U = \\frac{Q^2}{2C} = \\frac{(3.00 \\times 10^{-6})^2}{2 \\times (1.669 \\times 10^{-11})} = \\frac{9.00 \\times 10^{-12}}{3.338 \\times 10^{-11}} = 0.2696 \\text{ Joules}$$",
                "explanation": "The total stored energy is 0.270 Joules."
            },
            {
                "title": "Step 3: Verification via electric field energy density integration",
                "math": "$$E(r) = \\frac{Q}{4\\pi\\epsilon_0 r^2}$$\n$$u_E(r) = \\frac{1}{2}\\epsilon_0 E^2 = \\frac{1}{2}\\epsilon_0 \\left( \\frac{Q}{4\\pi\\epsilon_0 r^2} \\right)^2 = \\frac{Q^2}{32\\pi^2 \\epsilon_0 r^4}$$\n$$U = \\int_a^b u_E(r) (4\\pi r^2 dr) = \\frac{Q^2}{8\\pi\\epsilon_0} \\int_a^b \\frac{dr}{r^2} = \\frac{Q^2}{8\\pi\\epsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$$\n$$U = \\frac{Q^2 (b - a)}{8\\pi\\epsilon_0 a b} = \\frac{Q^2}{2 \\left( \\frac{4\\pi\\epsilon_0 a b}{b - a} \\right)} = \\frac{Q^2}{2C} = 0.2696 \\text{ Joules}$$\n$$\\text{Q.E.D.}$$",
                "explanation": "Integrating energy density over the 3D spherical volume confirms the exact microscopic localization of energy."
            }
        ]
    }
]

unit3_data = {
    "number": 3,
    "title": "Capacitors and Dielectrics",
    "leadSummary": "Comprehensive physical analysis of capacitors and capacitance calculations for planar, cylindrical, and spherical geometries, atomic mechanisms of dielectric polarization, Gauss's law in dielectrics, the three electric vectors E, D, and P, electrostatic energy storage, and field energy density.",
    "sections": u3_sections,
    "problems": u3_problems
}

with open("em_u3.json", "w") as f:
    json.dump(unit3_data, f, indent=2)

print("Unit 3 built successfully with", len(u3_sections), "sections and", len(u3_problems), "problems!")

# =========================================================================
# UNIT 4: Current and Resistance
# =========================================================================
u4_sections = [
    {
        "id": "sec-4-1",
        "number": "§4.1",
        "heading": "Electric Current, Current Density, and the Microscopic Drude Model",
        "simulation": "drude-current-sim",
        "content": """Electric current is the organized macroscopic transport of electric charge across a cross-section of a conducting medium.

<h4>1. Electric Current and Current Density</h4>
The instantaneous <strong>electric current</strong> $I$ is defined as the net charge passing through a surface per unit time:
$$I = \\frac{dq}{dt}$$
SI Unit: **Ampere (A)** ($1 \\text{ A} = 1 \\text{ C/s}$).
Current is a macroscopic scalar quantity. The microscopic vector characterizing charge flow at every spatial point is the <strong>Current Density</strong> $\\vec{J}$:
$$I = \\int_S \\vec{J} \\cdot d\\vec{A}$$
For uniform current across a normal cross-sectional area $A$:
$$J = \\frac{I}{A} \\quad (\\text{Units: A/m}^2)$$

<h4>2. Drift Velocity of Charge Carriers</h4>
In a conductor with free charge carrier density $n$ (electrons/m³) each carrying charge $q = -e$:
In time increment $dt$, carriers advance by length $dx = v_d dt$, where $v_d$ is the average **drift velocity**.
The charge traversing cross-section $A$ is $dq = n q (A v_d dt)$.
Hence:
$$I = n q A v_d = n e A v_d \\implies \\vec{J} = n q \\vec{v}_d = -n e \\vec{v}_d$$
<em>Striking Numerical Fact:</em> While electrical signals propagate at near the speed of light ($c \\sim 3 \\times 10^8\\text{ m/s}$), the physical drift velocity of electrons in copper under typical domestic currents is astonishingly slow:
$$v_d \\sim 10^{-4} \\text{ m/s} = 0.1 \\text{ mm/s}$$
An electron takes roughly three hours to travel one meter down a copper wire!

<h4>3. The Classical Drude Model of Electrical Conduction</h4>
Paul Drude (1900) modeled conduction electrons as an ideal classical gas undergoing random thermal collisions with positive ionic cores in a crystal lattice.
Between collisions, electrons accelerate under electric field $\\vec{E}$:
$$\\vec{a} = \\frac{-e \\vec{E}}{m}$$
Let $\\tau$ be the <strong>mean relaxation time</strong> (average time between collisions).
The average drift velocity acquired is:
$$\\vec{v}_d = \\vec{a} \\tau = -\\frac{e \\tau}{m} \\vec{E}$$
Substituting into current density:
$$\\vec{J} = -n e \\vec{v}_d = \\left( \\frac{n e^2 \\tau}{m} \\right) \\vec{E}$$
Defining electrical conductivity $\\sigma$:
$$\\vec{J} = \\sigma \\vec{E} \\quad (\\text{Microscopic Ohm's Law})$$
where:
$$\\sigma = \\frac{n e^2 \\tau}{m}, \\quad \\rho = \\frac{1}{\\sigma} = \\frac{m}{n e^2 \\tau}$$
This demonstrates that Ohm's law arises directly from frequent momentum-relaxing collisions."""
    },
    {
        "id": "sec-4-2",
        "number": "§4.2",
        "heading": "Resistance, Resistivity, and Temperature Dependence",
        "simulation": "drude-current-sim",
        "content": """Resistance is the macroscopic property of an electrical conductor that opposes the flow of electric current.

<h4>1. Macroscopic Ohm's Law and Resistance</h4>
Consider a conductor of uniform length $L$ and cross-sectional area $A$ carrying current $I$ under potential difference $V$.
Using $E = V/L$ and $J = I/A$ in $\\vec{J} = \\sigma \\vec{E}$:
$$\\frac{I}{A} = \\sigma \\frac{V}{L} = \\frac{1}{\\rho} \\frac{V}{L} \\implies V = I \\left( \\frac{\\rho L}{A} \\right)$$
We define <strong>Electrical Resistance ($R$)</strong>:
$$R = \\frac{V}{I} = \\frac{\\rho L}{A}$$
SI Unit: **Ohm ($\\Omega$)** ($1 \\ \\Omega = 1 \\text{ V/A}$).
<strong>Resistivity ($\\rho$)</strong> is an intrinsic material property (Units: $\\Omega\\cdot\\text{m}$).

<h4>2. Temperature Variation of Resistivity</h4>
As temperature rises, thermal lattice vibrations (phonons) increase in amplitude, scattering conduction electrons more frequently and reducing collision time $\\tau$.
Over moderate temperature intervals:
$$\\rho(T) = \\rho_0 [1 + \\alpha (T - T_0)]$$
$$R(T) = R_0 [1 + \\alpha (T - T_0)]$$
where $\\alpha$ is the <strong>temperature coefficient of resistivity</strong> (K⁻¹ or °C⁻¹).
<ul>
  <li><strong>Metals ($\\alpha > 0$):</strong> Resistivity increases with temperature (e.g., copper $\\alpha \\approx +0.0039\\text{ K}^{-1}$).</li>
  <li><strong>Semiconductors ($\\alpha < 0$):</strong> In silicon and germanium, higher temperatures thermally excite vastly more covalent electrons into the conduction band, increasing carrier density $n$ exponentially ($n \\propto e^{-E_g/2k_B T}$). Thus, resistivity drops sharply with temperature!</li>
  <li><strong>Superconductors:</strong> Below a critical temperature $T_c$, electrical resistance vanishes completely ($R \\equiv 0$).</li>
</ul>"""
    },
    {
        "id": "sec-4-3",
        "number": "§4.3",
        "heading": "Electromotive Force, Terminal Voltage, and Kirchhoff's Laws",
        "simulation": "drude-current-sim",
        "content": """To maintain a steady continuous current through a closed circuit, an energy source must perform work on charge carriers to transport them against electrostatic fields from low potential to high potential.

<h4>1. Electromotive Force (EMF, $\\mathcal{E}$)</h4>
An <strong>Electromotive Force</strong> $\\mathcal{E}$ is any non-electrostatic mechanism (chemical in batteries, mechanical/magnetic in dynamos, thermal in thermocouples) that does work on charge:
$$\\mathcal{E} = \\frac{dW_{\\text{non-elec}}}{dq}$$
A real voltage source possesses internal resistance $r$.
When delivering load current $I$, the terminal potential difference $V$ across the battery is:
$$V = \\mathcal{E} - I r$$
If the source is open-circuited ($I = 0$), $V = \\mathcal{E}$.

<h4>2. Kirchhoff's Circuit Laws</h4>
Gustav Kirchhoff (1845) formulated two fundamental conservation laws for multi-loop electrical networks:
<ol>
  <li><strong>Kirchhoff's Current Law (KCL / Junction Rule):</strong>
  The algebraic sum of all electric currents entering any junction node is identically zero:
  $$\\sum_{k} I_k = 0$$
  <em>Physical Basis:</em> Direct consequence of the <strong>conservation of electric charge</strong> ($\frac{\partial\rho}{\partial t} = 0$).</li>
  <li><strong>Kirchhoff's Voltage Law (KVL / Loop Rule):</strong>
  The algebraic sum of all potential differences (EMFs and resistive $IR$ drops) around any closed circuit loop is zero:
  $$\\sum_{k} \\mathcal{E}_k - \\sum_{k} I_k R_k = 0$$
  <em>Physical Basis:</em> Direct consequence of the <strong>conservation of energy</strong> in a conservative electrostatic field ($\\oint \\vec{E} \\cdot d\\vec{r} = 0$).</li>
</ol>"""
    },
    {
        "id": "sec-4-4",
        "number": "§4.4",
        "heading": "Electrical Measuring Instruments: Galvanometer, Ammeter, Voltmeter, and Potentiometer",
        "simulation": "drude-current-sim",
        "content": """Laboratory electrical measurements rely on precision meters configured from a basic d'Arsonval moving-coil galvanometer.

<h4>1. The Moving-Coil Galvanometer</h4>
A galvanometer detects minute currents. A coil of $N$ turns and resistance $R_g$ suspended in a radial magnetic field experiences deflecting torque $\\tau = N I A B$.
Balanced by torsional spring restoring torque $\\tau_s = C \\theta$:
$$I = \\left(\\frac{C}{N A B}\\right) \\theta = K \\theta$$
The deflection angle $\\theta$ is directly proportional to current.
Full-scale deflection current is denoted $I_g$ (typically $50\\ \\mu\\text{A} - 1\\text{ mA}$).

<h4>2. Conversion of Galvanometer to an Ammeter</h4>
An ammeter must connect in series and possess extremely low resistance to avoid perturbing circuit current.
A low-resistance resistor called a <strong>shunt resistor ($R_s$)</strong> is connected in parallel with the galvanometer:
$$I_s R_s = I_g R_g \\implies (I - I_g) R_s = I_g R_g$$
$$R_s = \\frac{I_g R_g}{I - I_g}$$

<h4>3. Conversion of Galvanometer to a Voltmeter</h4>
A voltmeter must connect in parallel and possess extremely high resistance so it draws negligible current from the circuit.
A large <strong>multiplier resistor ($R_m$)</strong> is connected in series with the galvanometer:
$$V = I_g (R_g + R_m) \\implies R_m = \\frac{V}{I_g} - R_g$$

<h4>4. The Slide-Wire Potentiometer</h4>
A potentiometer measures unknown EMF $\\mathcal{E}_x$ without drawing any current at balance (null deflection), providing the theoretical ideal of an infinite-impedance voltmeter:
$$\\frac{\\mathcal{E}_x}{\\mathcal{E}_0} = \\frac{l_x}{l_0}$$
where $l_x$ is the balancing length for the test cell and $l_0$ for the standard cell."""
    },
    {
        "id": "sec-4-5",
        "number": "§4.5",
        "heading": "RC Circuits: Charging and Discharging Transients",
        "simulation": "rc-transient-sim",
        "content": """In circuits containing both resistors and capacitors, voltages and currents do not change instantaneously, but evolve exponentially over time.

<h4>1. Charging an RC Circuit</h4>
Consider a series circuit with battery $\\mathcal{E}$, resistor $R$, capacitor $C$, and switch closed at $t = 0$.
By Kirchhoff's voltage law:
$$\\mathcal{E} - i R - \\frac{q}{C} = 0$$
Since $i = \\frac{dq}{dt}$:
$$R \\frac{dq}{dt} + \\frac{q}{C} = \\mathcal{E} \\implies \\frac{dq}{dt} = -\\frac{q - C\\mathcal{E}}{RC}$$
Integrating with initial condition $q(0) = 0$:
$$q(t) = C\\mathcal{E} \\left( 1 - e^{-t/RC} \\right) = Q_0 \\left( 1 - e^{-t/\\tau} \\right)$$
where $\\tau = R C$ is the **capacitive time constant** (Units: seconds, $\\Omega \\cdot \\text{F} = \\text{s}$).
Differentiating charge gives the decaying charging current:
$$i(t) = \\frac{dq}{dt} = \\frac{\\mathcal{E}}{R} e^{-t/\\tau} = I_0 e^{-t/\\tau}$$

<h4>2. Discharging an RC Circuit</h4>
Disconnecting the battery and closing the loop across $R$:
$$-i R - \\frac{q}{C} = 0 \\implies R \\frac{dq}{dt} + \\frac{q}{C} = 0$$
$$q(t) = Q_0 e^{-t/\\tau}, \\quad i(t) = -\\frac{Q_0}{RC} e^{-t/\\tau} = -I_0 e^{-t/\\tau}$$

<h4>3. The 50% Energy Paradox in Capacitor Charging</h4>
During charging to final voltage $V$:
<ul>
  <li>Total energy delivered by the battery:
  $$W_{\\text{battery}} = \\int_0^\\infty \\mathcal{E} i(t) dt = \\mathcal{E} \\int_0^\\infty dq = \\mathcal{E} Q_0 = C\\mathcal{E}^2$$</li>
  <li>Final electrostatic energy stored in capacitor:
  $$U_C = \\frac{1}{2} C\\mathcal{E}^2$$</li>
  <li>Total Joule thermal energy dissipated in resistor:
  $$W_{\\text{heat}} = \\int_0^\\infty i^2 R \\, dt = \\int_0^\\infty \\left(\\frac{\\mathcal{E}}{R} e^{-t/RC}\\right)^2 R \\, dt = \\frac{\\mathcal{E}^2}{R} \\int_0^\\infty e^{-2t/RC} dt = \\frac{1}{2} C\\mathcal{E}^2$$</li>
</ul>
<em>Fundamental Thermodynamic Theorem:</em> Exactly **50% of the energy supplied by the battery is inevitably dissipated as Joule heat** in the circuit, completely independent of the resistance $R$! (Even if $R \\to 0$, energy is lost via electromagnetic radiation)."""
    },
    {
        "id": "sec-4-6",
        "number": "§4.6",
        "heading": "Thermoelectricity: Seebeck, Peltier, and Thomson Effects",
        "simulation": "drude-current-sim",
        "content": """Thermoelectricity encompasses the direct microscopic coupling between thermal gradients and electric potential differences in conductors and semiconductors.

<h4>1. The Seebeck Effect (1821)</h4>
Thomas Johann Seebeck discovered that when two dissimilar conducting wires $A$ and $B$ are joined at two junctions maintained at different temperatures $T_1$ and $T_2$, an open-circuit **thermoelectric EMF** $\\mathcal{E}_{AB}$ is established:
$$\\mathcal{E}_{AB} = \\int_{T_1}^{T_2} S_{AB}(T) \\, dT$$
where $S_{AB} = S_A - S_B$ is the differential <strong>Seebeck coefficient (Thermoelectric Power)</strong> in $\\mu\\text{V/K}$.
Over modest temperature ranges:
$$\\mathcal{E} = a (T_h - T_c) + \\frac{1}{2} b (T_h - T_c)^2$$
The <strong>neutral temperature ($T_n$)</strong> is the hot-junction temperature where EMF reaches its maximum ($\frac{d\mathcal{E}}{dT} = 0 \implies T_n = -a/b$).
Beyond the <strong>inversion temperature ($T_i = 2T_n - T_c$)</strong>, the polarity of the EMF reverses.

<h4>2. The Peltier Effect (1834)</h4>
Jean Charles Athanase Peltier discovered the exact thermodynamic inverse of the Seebeck effect:
When an electric current $I$ is driven through a junction between two dissimilar conductors, heat is either absorbed or released at the junction (over and above irreversible Joule heating):
$$\\frac{dQ_{\\text{Peltier}}}{dt} = \\Pi_{AB} I$$
where $\\Pi_{AB}$ is the <strong>Peltier coefficient</strong> (Volts).
Reversing current direction reverses heating to cooling! This enables solid-state thermoelectric coolers (Peltier coolers) used in satellite sensors, PCR machines, and silent refrigeration.

<h4>3. The Thomson Effect and Kelvin Relations</h4>
William Thomson (Lord Kelvin, 1854) applied thermodynamics to prove that heat is reversibly absorbed or evolved when current passes along an individual homogeneous conductor having a temperature gradient $dT/dx$:
$$\\frac{dQ_{\\text{Thomson}}}{dx} = \\mu I \\frac{dT}{dx}$$
Kelvin derived the celebrated **Kelvin (Onsager) Relations**:
$$\\Pi_{AB} = T \\cdot S_{AB}, \\quad \\mu_A - \\mu_B = T \\frac{dS_{AB}}{dT}$$
Connecting all three thermoelectric effects into a unified thermodynamic framework."""
    }
]

u4_problems = [
    {
        "id": "prob-4-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Microscopic Electron Drift Speed in a Copper Conductor",
        "question": "A cylindrical copper wire of diameter $D = 2.05\\text{ mm}$ (12 AWG gauge) carries a steady direct current $I = 15.0\\text{ A}$. Copper has density $\\rho = 8960\\text{ kg/m}^3$, atomic mass $M = 63.55\\text{ g/mol}$, and provides one conduction electron per atom. Avogadro's number $N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}$, and elementary charge $e = 1.602 \\times 10^{-19}\\text{ C}$.\\n(a) Determine the free electron number density $n$ in copper,\\n(b) Calculate the current density $J$ in the wire, and\\n(c) Find the electron drift speed $v_d$ and the time required for an electron to travel $L = 3.00\\text{ m}$ along the wire.",
        "steps": [
            {
                "title": "Step 1: Compute free electron density n",
                "math": "$$n = \\frac{\\rho N_A}{M} = \\frac{(8960 \\text{ kg/m}^3) \\times (6.022 \\times 10^{23} \\text{ atoms/mol})}{0.06355 \\text{ kg/mol}}$$\n$$n = \\frac{5.3957 \\times 10^{27}}{0.06355} = 8.4905 \\times 10^{28} \\text{ electrons/m}^3$$",
                "explanation": "Copper contains roughly $8.49 \\times 10^{28}$ conduction electrons per cubic meter."
            },
            {
                "title": "Step 2: Calculate cross-sectional area and current density",
                "math": "$$A = \\frac{\\pi D^2}{4} = \\frac{\\pi (2.05 \\times 10^{-3})^2}{4} = 3.3006 \\times 10^{-6} \\text{ m}^2$$\n$$J = \\frac{I}{A} = \\frac{15.0 \\text{ A}}{3.3006 \\times 10^{-6} \\text{ m}^2} = 4.5446 \\times 10^6 \\text{ A/m}^2 = 4.54 \\text{ MA/m}^2$$",
                "explanation": "The current density is $4.54 \\times 10^6$ A/m²."
            },
            {
                "title": "Step 3: Calculate drift speed and travel time",
                "math": "$$v_d = \\frac{J}{n e} = \\frac{4.5446 \\times 10^6}{(8.4905 \\times 10^{28}) \\times (1.6022 \\times 10^{-19})} = \\frac{4.5446 \\times 10^6}{1.3603 \\times 10^{10}} = 3.3408 \\times 10^{-4} \\text{ m/s} = 0.334 \\text{ mm/s}$$\n$$t = \\frac{L}{v_d} = \\frac{3.00 \\text{ m}}{3.3408 \\times 10^{-4} \\text{ m/s}} = 8979.8 \\text{ s} \\approx 2.49 \\text{ hours}$$",
                "explanation": "Electrons drift at a sluggish 0.33 mm per second, taking nearly 2.5 hours to traverse 3 meters of wire."
            }
        ]
    },
    {
        "id": "prob-4-2",
        "difficulty": "Multi-Loop Network Standard Exam",
        "title": "Multi-Loop Network Analysis via Kirchhoff's Rules",
        "question": "A two-loop circuit contains two real DC batteries: Battery 1 has EMF $\\mathcal{E}_1 = 12.0\\text{ V}$ and internal resistance $r_1 = 1.00\\ \\Omega$; Battery 2 has EMF $\\mathcal{E}_2 = 6.00\\text{ V}$ and internal resistance $r_2 = 1.00\\ \\Omega$. The batteries are connected in parallel across a common load resistor $R_L = 10.0\\ \\Omega$, with each branch containing an additional resistor: $R_1 = 3.00\\ \\Omega$ in branch 1 and $R_2 = 2.00\\ \\Omega$ in branch 2.\\n(a) Write the Kirchhoff current and loop equations for the network,\\n(b) Solve for branch currents $I_1$ and $I_2$, and the load current $I_L$, and\\n(c) Find the potential difference across the load resistor and the power delivered to it.",
        "steps": [
            {
                "title": "Step 1: Formulate Kirchhoff equations",
                "math": "$$\\text{Branch 1 total resistance: } R_{b1} = R_1 + r_1 = 3.00 + 1.00 = 4.00\\ \\Omega$$\n$$\\text{Branch 2 total resistance: } R_{b2} = R_2 + r_2 = 2.00 + 1.00 = 3.00\\ \\Omega$$\n$$\\text{Junction rule: } I_L = I_1 + I_2$$\n$$\\text{Loop 1 (Battery 1 and Load): } \\mathcal{E}_1 - I_1 R_{b1} - I_L R_L = 0 \\implies 12.0 - 4.00 I_1 - 10.0 (I_1 + I_2) = 0$$\n$$14.0 I_1 + 10.0 I_2 = 12.0 \\quad \\text{--- (1)}$$\n$$\\text{Loop 2 (Battery 2 and Load): } \\mathcal{E}_2 - I_2 R_{b2} - I_L R_L = 0 \\implies 6.00 - 3.00 I_2 - 10.0 (I_1 + I_2) = 0$$\n$$10.0 I_1 + 13.0 I_2 = 6.00 \\quad \\text{--- (2)}$$",
                "explanation": "Applying KVL to each independent loop produces two linear simultaneous equations."
            },
            {
                "title": "Step 2: Solve simultaneous equations for currents",
                "math": "$$\\text{From (1): } I_1 = \\frac{12.0 - 10.0 I_2}{14.0} = \\frac{6.0 - 5.0 I_2}{7.0}$$\n$$\\text{Substitute into (2): } 10.0 \\left( \\frac{6.0 - 5.0 I_2}{7.0} \\right) + 13.0 I_2 = 6.00$$\n$$\\frac{60.0 - 50.0 I_2 + 91.0 I_2}{7.0} = 6.00 \\implies 60.0 + 41.0 I_2 = 42.0$$\n$$41.0 I_2 = -18.0 \\implies I_2 = -0.4390 \\text{ A}$$\n$$I_1 = \\frac{12.0 - 10.0(-0.4390)}{14.0} = \\frac{12.0 + 4.390}{14.0} = \\frac{16.390}{14.0} = +1.1707 \\text{ A}$$\n$$I_L = I_1 + I_2 = 1.1707 - 0.4390 = 0.7317 \\text{ A}$$",
                "explanation": "Because $I_2 < 0$, Battery 2 is actually being charged backwards by the stronger 12V Battery 1!"
            },
            {
                "title": "Step 3: Load voltage and power dissipation",
                "math": "$$V_L = I_L R_L = (0.7317 \\text{ A}) \\times (10.0\\ \\Omega) = 7.317 \\text{ Volts}$$\n$$P_L = I_L^2 R_L = (0.7317)^2 \\times 10.0 = 0.5354 \\times 10.0 = 5.354 \\text{ Watts}$$",
                "explanation": "The load resistor sustains 7.32 V and dissipates 5.35 W of electrical power."
            }
        ]
    },
    {
        "id": "prob-4-3",
        "difficulty": "Honors RC Circuit Problem",
        "title": "RC Circuit Transient Analysis and 50% Energy Partitioning",
        "question": "A series RC circuit consists of a battery $\\mathcal{E} = 100.0\\text{ V}$, a resistor $R = 50.0\\text{ k}\\Omega$, and an uncharged capacitor $C = 20.0\\ \\mu\\text{F}$. The switch is closed at $t = 0$.\\n(a) Determine the capacitive time constant $\\tau$ and the initial current $I_0$,\\n(b) Calculate the time required for the capacitor to charge to $90.0\\%$ of its final maximum voltage, and\\n(c) Calculate the total electrical energy delivered by the battery, the final energy stored in the capacitor, and the total Joule thermal heat dissipated in the resistor as $t \\to \\infty$.",
        "steps": [
            {
                "title": "Step 1: Compute time constant and initial current",
                "math": "$$\\tau = R C = (50.0 \\times 10^3\\ \\Omega) \\times (20.0 \\times 10^{-6} \\text{ F}) = 1.000 \\text{ second}$$\n$$I_0 = \\frac{\\mathcal{E}}{R} = \\frac{100.0 \\text{ V}}{50000\\ \\Omega} = 2.00 \\times 10^{-3} \\text{ A} = 2.00 \\text{ mA}$$",
                "explanation": "The time constant is exactly 1.00 s and initial peak current is 2.00 mA."
            },
            {
                "title": "Step 2: Time to reach 90% charge",
                "math": "$$V_C(t) = \\mathcal{E} (1 - e^{-t/\\tau}) = 0.900 \\mathcal{E}$$\n$$1 - e^{-t/\\tau} = 0.900 \\implies e^{-t/\\tau} = 0.100$$\n$$-\\frac{t}{\\tau} = \\ln(0.100) = -2.3026 \\implies t = 2.3026 \\tau$$\n$$t = 2.3026 \\times 1.000 \\text{ s} = 2.303 \\text{ seconds}$$",
                "explanation": "Reaching 90% full voltage requires $2.30$ time constants."
            },
            {
                "title": "Step 3: Energy delivered, stored, and dissipated",
                "math": "$$Q_0 = C\\mathcal{E} = (20.0 \\times 10^{-6} \\text{ F}) \\times 100.0 \\text{ V} = 2.00 \\times 10^{-3} \\text{ C}$$\n$$W_{\\text{battery}} = Q_0 \\mathcal{E} = (2.00 \\times 10^{-3} \\text{ C}) \\times 100.0 \\text{ V} = 0.2000 \\text{ Joules}$$\n$$U_C = \\frac{1}{2} C\\mathcal{E}^2 = \\frac{1}{2} \\times (20.0 \\times 10^{-6}) \\times (100.0)^2 = 0.1000 \\text{ Joules}$$\n$$W_{\\text{heat}} = W_{\\text{battery}} - U_C = 0.2000 - 0.1000 = 0.1000 \\text{ Joules}$$\n$$\\frac{U_C}{W_{\\text{battery}}} = 50.0\\%, \\quad \\frac{W_{\\text{heat}}}{W_{\\text{battery}}} = 50.0\\%$$",
                "explanation": "The battery supplies 0.200 J; exactly 0.100 J (50%) is stored in the capacitor and 0.100 J (50%) is converted to heat in the resistor."
            }
        ]
    }
]

unit4_data = {
    "number": 4,
    "title": "Current and Resistance",
    "leadSummary": "Microscopic and macroscopic physics of electric current, current density, the classical Drude model of electron drift, temperature-dependent resistivity, Electromotive Force, Kirchhoff's circuit rules, multi-loop networks, galvanometers, ammeters, voltmeters, potentiometers, RC charging and discharging transients, and thermoelectric phenomena (Seebeck, Peltier, Thomson).",
    "sections": u4_sections,
    "problems": u4_problems
}

with open("em_u4.json", "w") as f:
    json.dump(unit4_data, f, indent=2)

print("Unit 4 built successfully with", len(u4_sections), "sections and", len(u4_problems), "problems!")
