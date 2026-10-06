// Electricity and Magnetism (Physics Core Courseware)
// Comprehensive university-standard textbook dataset covering all 8 Units with KaTeX derivations and 24 solved exam problems.

window.COURSE_DATA = {
  "courseTitle": "Electricity and Magnetism",
  "courseCode": "PHYSICS",
  "department": "Department of Physics",
  "institution": "OpenSTEM Global Academic Press",
  "authorContact": "shahriyarkarimsiam@gmail.com",
  "units": [
    {
      "number": 1,
      "title": "Electric Field and Gauss's Law",
      "leadSummary": "A rigorous foundation of electrostatics: charge quantization and conservation, Coulomb's inverse-square law, vector superposition, electric field lines, dipole dynamics and torque, electric flux, Gauss's law in integral and differential forms, and applications to spherical, cylindrical, and planar symmetries.",
      "sections": [
        {
          "id": "sec-1-1",
          "number": "\u00a71.1",
          "heading": "Electric Charge, Quantization, and Conservation Laws",
          "simulation": "coulomb-field-sim",
          "content": "Electrostatics investigates electric charges at rest and the static electric fields they establish in vacuum and material media.\n\n<h4>1. The Fundamental Nature of Electric Charge</h4>\nElectric charge is an intrinsic fundamental property of subatomic matter. Matter exhibits two complementary types of charge:\n<ul>\n  <li><strong>Positive Charge ($+q$):</strong> Borne by protons ($+e$).</li>\n  <li><strong>Negative Charge ($-q$):</strong> Borne by electrons ($-e$).</li>\n</ul>\nLike charges repel one another with mutual electrostatic forces; unlike charges attract.\n\n<h4>2. Quantization of Electric Charge</h4>\nRobert A. Millikan's oil-drop experiment (1909) experimentally confirmed that electric charge is not continuous, but exists exclusively in discrete, integer multiples of the elementary charge $e$:\n$$q = \\pm n e, \\quad n = 0, 1, 2, 3, \\dots$$\nwhere the elementary quantum of charge is defined by the 2019 SI standard:\n$$e = 1.602176634 \\times 10^{-19} \\text{ Coulombs (exact)}$$\n(Note: Although quarks carry fractional charges $\\pm \\frac{1}{3}e$ and $\\pm \\frac{2}{3}e$, quark confinement strictly forbids isolated fractional charges under ordinary conditions).\n\n<h4>3. The Law of Conservation of Electric Charge</h4>\nIn any closed, isolated physical system, the algebraic sum of electric charges remains strictly constant over time:\n$$\\sum q_i = \\text{constant}, \\quad \\frac{d Q_{\\text{total}}}{dt} = 0$$\nIn relativistic and high-energy particle physics, while particles can be created or annihilated (e.g., pair production $\\gamma \\to e^- + e^+$ or electron-positron annihilation $e^- + e^+ \\to 2\\gamma$), net electric charge is conserved in every known physical interaction.\n\n<h4>4. Continuous Charge Distributions</h4>\nOn macroscopic scales where individual charges cannot be resolved, charge is modeled via continuous spatial density distributions:\n<ul>\n  <li><strong>Linear Charge Density ($\\lambda$):</strong> $\\lambda = \\frac{dq}{dl}$ (Units: C/m)</li>\n  <li><strong>Surface Charge Density ($\\sigma$):</strong> $\\sigma = \\frac{dq}{dA}$ (Units: C/m\u00b2)</li>\n  <li><strong>Volume Charge Density ($\\rho$):</strong> $\\rho = \\frac{dq}{dV}$ (Units: C/m\u00b3)</li>\n</ul>"
        },
        {
          "id": "sec-1-2",
          "number": "\u00a71.2",
          "heading": "Coulomb's Law and the Electrostatic Superposition Principle",
          "simulation": "coulomb-field-sim",
          "content": "Charles-Augustin de Coulomb (1785) established the fundamental quantitative law of electrostatic force using a precision torsion balance.\n\n<h4>1. Coulomb's Law in Vector Form</h4>\nThe electrostatic force $\\vec{F}_{12}$ exerted by a point charge $q_1$ located at position $\\vec{r}_1$ on a second point charge $q_2$ located at $\\vec{r}_2$ in vacuum is:\n$$\\vec{F}_{12} = \\frac{1}{4\\pi\\epsilon_0} \\frac{q_1 q_2}{|\\vec{r}_2 - \\vec{r}_1|^2} \\hat{r}_{12} = \\frac{1}{4\\pi\\epsilon_0} \\frac{q_1 q_2}{|\\vec{r}_2 - \\vec{r}_1|^3} (\\vec{r}_2 - \\vec{r}_1)$$\nwhere:\n<ul>\n  <li>$\\epsilon_0$: <strong>Permittivity of Free Space (Vacuum Permittivity)</strong>:\n  $$\\epsilon_0 = 8.8541878128 \\times 10^{-12} \\text{ F/m (or C}^2/(\\text{N}\\cdot\\text{m}^2))$$</li>\n  <li>Coulomb's constant:\n  $$k_e = \\frac{1}{4\\pi\\epsilon_0} \\approx 8.98755 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2$$</li>\n  <li>By Newton's third law of action and reaction: $\\vec{F}_{21} = -\\vec{F}_{12}$.</li>\n</ul>\n\n<h4>2. Coulomb's Force in a Dielectric Medium</h4>\nWhen point charges are embedded in a linear, isotropic, homogeneous dielectric medium of relative permittivity $\\epsilon_r$ (dielectric constant $\\kappa$):\n$$\\vec{F} = \\frac{1}{4\\pi\\epsilon} \\frac{q_1 q_2}{r^2} \\hat{r} = \\frac{1}{4\\pi\\epsilon_0 \\epsilon_r} \\frac{q_1 q_2}{r^2} \\hat{r} = \\frac{\\vec{F}_{\\text{vacuum}}}{\\epsilon_r}$$\nBecause $\\epsilon_r > 1$ for all physical media (e.g., $\\epsilon_r \\approx 80$ for pure water at 20\u00b0C), polarization of the surrounding dielectric shields the charges, reducing the electrostatic force significantly.\n\n<h4>3. The Superposition Principle</h4>\nThe net electrostatic force exerted on a test charge $q_0$ by an assembly of $N$ discrete point charges $q_1, q_2, \\dots, q_N$ is the vector sum of the individual Coulomb forces:\n$$\\vec{F}_{\\text{net}} = \\sum_{i=1}^N \\vec{F}_i = \\frac{q_0}{4\\pi\\epsilon_0} \\sum_{i=1}^N \\frac{q_i}{|\\vec{r}_0 - \\vec{r}_i|^3} (\\vec{r}_0 - \\vec{r}_i)$$\nFor a continuous volume charge distribution $\\rho(\\vec{r}')$:\n$$\\vec{F}_{\\text{net}} = \\frac{q_0}{4\\pi\\epsilon_0} \\int_V \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|^3} (\\vec{r} - \\vec{r}') dV'$$"
        },
        {
          "id": "sec-1-3",
          "number": "\u00a71.3",
          "heading": "The Electric Field Vector and Field Line Topology",
          "simulation": "coulomb-field-sim",
          "content": "The concept of the electric field, introduced by Michael Faraday, replaces direct action-at-a-distance with a local physical intermediary.\n\n<h4>1. Definition of the Electric Field Vector</h4>\nThe <strong>electric field</strong> $\\vec{E}(\\vec{r})$ at a point in space is defined as the electrostatic force experienced per unit positive test charge placed at that location, in the limit where the test charge $q_0$ approaches zero to prevent perturbing the source charge distribution:\n$$\\vec{E}(\\vec{r}) = \\lim_{q_0 \\to 0} \\frac{\\vec{F}}{q_0}$$\nSI Unit: $\\text{N/C}$ (equivalent to $\\text{Volts/meter}$, $\\text{V/m}$).\n\n<h4>2. Field of a Point Charge and Continuous Distribution</h4>\nFor an isolated point charge $q$ at the origin:\n$$\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\frac{q}{r^2} \\hat{r}$$\nFor an arbitrary continuous charge distribution occupying volume $V'$:\n$$\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\int_{V'} \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|^3} (\\vec{r} - \\vec{r}') dV'$$\n\n<h4>3. Motion of a Point Charge in an Electric Field</h4>\nA particle of mass $m$ and charge $q$ placed in an electric field $\\vec{E}$ experiences acceleration:\n$$\\vec{a} = \\frac{\\vec{F}}{m} = \\frac{q \\vec{E}}{m}$$\nIn a uniform electric field $\\vec{E} = E_0 \\hat{j}$:\n<ul>\n  <li>A charged particle launched perpendicular to $\\vec{E}$ executes a parabolic trajectory, completely analogous to projectile motion under uniform gravity (the operational principle of cathode ray oscilloscopes and ink-jet printers).</li>\n</ul>\n\n<h4>4. Electric Field Lines (Lines of Force)</h4>\nElectric field lines are imaginary curves whose tangent at any point indicates the direction of the local electric field vector $\\vec{E}$:\n<ol>\n  <li>Field lines originate on positive charges and terminate on negative charges (or extend to infinity).</li>\n  <li>The local spatial density of lines (number of lines per unit area normal to $\\vec{E}$) is directly proportional to field magnitude $|\\vec{E}|$.</li>\n  <li>Field lines never intersect in free space, because the electric field vector is uniquely defined at every point.</li>\n</ol>"
        },
        {
          "id": "sec-1-4",
          "number": "\u00a71.4",
          "heading": "The Electric Dipole in an External Electric Field",
          "simulation": "coulomb-field-sim",
          "content": "An electric dipole consists of two equal and opposite point charges $+q$ and $-q$ separated by a fixed distance $2a$.\n\n<h4>1. The Electric Dipole Moment Vector</h4>\nThe <strong>electric dipole moment</strong> $\\vec{p}$ is defined as:\n$$\\vec{p} = q \\vec{d}$$\nwhere $\\vec{d}$ is the displacement vector directed from the negative charge $-q$ toward the positive charge $+q$.\nSI Unit: $\\text{Coulomb}\\cdot\\text{meter}$ (C\u00b7m). (In molecular physics, the Debye unit is commonly used: $1 \\text{ D} = 3.33564 \\times 10^{-30} \\text{ C}\\cdot\\text{m}$).\n\n<h4>2. Torque on a Dipole in a Uniform Electric Field</h4>\nWhen placed in a uniform external field $\\vec{E}$, the net translational force on the dipole vanishes:\n$$\\vec{F}_{\\text{net}} = (+q)\\vec{E} + (-q)\\vec{E} = 0$$\nHowever, the forces act along different lines of action, producing a net mechanical restoring torque:\n$$\\vec{\\tau} = \\vec{r}_+ \\times (q\\vec{E}) + \\vec{r}_- \\times (-q\\vec{E}) = (\\vec{r}_+ - \\vec{r}_-) \\times q\\vec{E} = \\vec{d} \\times q\\vec{E}$$\n$$\\vec{\\tau} = \\vec{p} \\times \\vec{E}$$\nMagnitude: $\\tau = p E \\sin\\theta$, where $\\theta$ is the angle between $\\vec{p}$ and $\\vec{E}$.\nThe torque acts to align the dipole moment parallel to the external field ($\\theta = 0$).\n\n<h4>3. Potential Energy of an Electric Dipole</h4>\nThe external work required to rotate the dipole from reference angle $\\theta_0 = 90^\\circ$ to angle $\\theta$ is:\n$$U(\\theta) = \\int_{90^\\circ}^\\theta \\tau_{\\text{ext}} d\\theta' = \\int_{90^\\circ}^\\theta (p E \\sin\\theta') d\\theta' = -p E \\cos\\theta$$\n$$U = -\\vec{p} \\cdot \\vec{E}$$\n<ul>\n  <li><strong>Stable Equilibrium ($\\theta = 0^\\circ$):</strong> Dipole aligned with $\\vec{E}$; minimum potential energy $U_{\\min} = -p E$.</li>\n  <li><strong>Unstable Equilibrium ($\\theta = 180^\\circ$):</strong> Dipole antiparallel to $\\vec{E}$; maximum potential energy $U_{\\max} = +p E$.</li>\n</ul>\n\n<h4>4. Dipole in a Non-Uniform Electric Field</h4>\nIn an inhomogeneous field where $\\vec{E}$ varies spatially, the forces on $+q$ and $-q$ do not cancel. The net translational force is:\n$$\\vec{F} = (\\vec{p} \\cdot \\nabla) \\vec{E} = \\nabla (\\vec{p} \\cdot \\vec{E})$$\nA neutral dipole is always pulled toward regions of stronger electric field strength."
        },
        {
          "id": "sec-1-5",
          "number": "\u00a71.5",
          "heading": "Electric Flux and Gauss's Law",
          "simulation": "gauss-flux-sim",
          "content": "Carl Friedrich Gauss (1835) formulated Gauss's law, which relates the total electric flux passing through a closed geometric surface to the enclosed net electric charge.\n\n<h4>1. Definition of Electric Flux</h4>\nThe <strong>electric flux</strong> $d\\Phi_E$ through an infinitesimal oriented surface element $d\\vec{A} = \\hat{n} dA$ is:\n$$d\\Phi_E = \\vec{E} \\cdot d\\vec{A} = E \\cos\\theta \\, dA$$\nwhere $\\hat{n}$ is the outward unit normal vector.\nFor an arbitrary closed Gaussian surface $S$:\n$$\\Phi_E = \\oint_S \\vec{E} \\cdot d\\vec{A}$$\nSI Unit: $\\text{N}\\cdot\\text{m}^2/\\text{C} = \\text{V}\\cdot\\text{m}$.\n\n<h4>2. Gauss's Law in Integral Form</h4>\nFor an isolated point charge $q$ enclosed by a concentric sphere of radius $r$:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\oint_S \\left( \\frac{q}{4\\pi\\epsilon_0 r^2} \\hat{r} \\right) \\cdot (\\hat{r} dA) = \\frac{q}{4\\pi\\epsilon_0 r^2} (4\\pi r^2) = \\frac{q}{\\epsilon_0}$$\nBy superposition, for any arbitrary closed surface enclosing net charge $Q_{\\text{encl}}$:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\frac{Q_{\\text{enclosed}}}{\\epsilon_0}$$\nThis is **Gauss's Law** (the first of Maxwell's four foundational equations of electromagnetism).\n\n<h4>3. Key Properties of Gauss's Law</h4>\n<ul>\n  <li>Gauss's law holds for *any* closed surface of arbitrary shape (called a Gaussian surface).</li>\n  <li>Charges located *outside* the closed surface contribute zero net flux through the surface (any flux entering must leave).</li>\n  <li>Gauss's law is a direct mathematical consequence of the inverse-square nature of Coulomb's force ($F \\propto 1/r^2$). If the force followed $1/r^{2+\\delta}$, Gauss's law would fail.</li>\n</ul>\n\n<h4>4. Differential Form of Gauss's Law</h4>\nApplying Gauss's Divergence Theorem:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = \\int_V (\\nabla \\cdot \\vec{E}) dV = \\frac{1}{\\epsilon_0} \\int_V \\rho \\, dV$$\nSince this holds for any arbitrary volume $V$:\n$$\\nabla \\cdot \\vec{E} = \\frac{\\rho}{\\epsilon_0}$$\nThis is the differential form of Gauss's law, stating that positive charge density acts as a local source (divergence) of electric field lines, and negative charge acts as a sink."
        },
        {
          "id": "sec-1-6",
          "number": "\u00a71.6",
          "heading": "Applications of Gauss's Law: Spherical, Cylindrical, and Planar Symmetries",
          "simulation": "gauss-flux-sim",
          "content": "Gauss's law enables direct calculation of electric field configurations when the charge distribution possesses high geometric symmetry.\n\n<h4>1. Spherically Symmetric Charge Distribution</h4>\nConsider a solid insulating sphere of radius $R$ with uniform volume charge density $\\rho$ (total charge $Q = \\frac{4}{3}\\pi R^3 \\rho$).\nBy spherical symmetry, $\\vec{E} = E(r) \\hat{r}$. Construct a concentric spherical Gaussian surface of radius $r$:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E(r) \\oint_S dA = E(r) (4\\pi r^2)$$\n<ul>\n  <li><strong>Outside the Sphere ($r \\ge R$):</strong>\n  $$Q_{\\text{encl}} = Q \\implies E(r) (4\\pi r^2) = \\frac{Q}{\\epsilon_0} \\implies E(r) = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{r^2}$$\n  The external field is identical to that of a point charge $Q$ at the center.</li>\n  <li><strong>Inside the Sphere ($r < R$):</strong>\n  $$Q_{\\text{encl}} = \\rho \\left( \\frac{4}{3}\\pi r^3 \\right) = Q \\left( \\frac{r^3}{R^3} \\right)$$\n  $$E(r) (4\\pi r^2) = \\frac{Q r^3}{\\epsilon_0 R^3} \\implies E(r) = \\frac{Q}{4\\pi\\epsilon_0 R^3} r = \\frac{\\rho}{3\\epsilon_0} r$$\n  Inside the sphere, the electric field increases linearly from zero at the center to maximum at the surface!</li>\n</ul>\n\n<h4>2. Infinitely Long Line of Charge (Cylindrical Symmetry)</h4>\nConsider an infinite line carrying uniform linear charge density $\\lambda$ (C/m).\nConstruct a coaxial cylindrical Gaussian surface of radius $r$ and length $L$.\nFlux through the two flat end caps is zero because $\\vec{E} \\perp \\hat{n}_{\\text{caps}}$.\nFlux through the curved cylindrical jacket of area $2\\pi r L$:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E(r) (2\\pi r L) = \\frac{Q_{\\text{encl}}}{\\epsilon_0} = \\frac{\\lambda L}{\\epsilon_0}$$\n$$E(r) = \\frac{\\lambda}{2\\pi\\epsilon_0 r}$$\nThe field decays inversely with radial distance ($E \\propto 1/r$).\n\n<h4>3. Infinite Plane Sheet of Charge (Planar Symmetry)</h4>\nConsider an infinite non-conducting flat plane with uniform surface charge density $\\sigma$ (C/m\u00b2).\nConstruct a cylindrical Gaussian pillbox of cross-sectional area $A$ piercing the sheet perpendicularly.\nFlux through the cylindrical mantle is zero ($\\vec{E} \\parallel \\text{mantle}$). Flux passes equally out of both end faces:\n$$\\oint_S \\vec{E} \\cdot d\\vec{A} = E A + E A = 2 E A = \\frac{Q_{\\text{encl}}}{\\epsilon_0} = \\frac{\\sigma A}{\\epsilon_0}$$\n$$E = \\frac{\\sigma}{2\\epsilon_0}$$\nRemarkably, the field is completely **uniform and independent of distance** from the sheet!\nFor a conducting surface where all charge resides on the outer boundary and $\\vec{E}_{\\text{inside}} = 0$:\n$$E_{\\text{conductor}} = \\frac{\\sigma}{\\epsilon_0}$$"
        }
      ],
      "problems": [
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
              "explanation": "The negative potential energy confirms the configuration is bound relative to the 90\u00b0 reference."
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
              "explanation": "Integrating spherical shells of volume $4\\pi r^2 dr$ yields a total enclosed charge of 6.33 nC."
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
    },
    {
      "number": 2,
      "title": "Electric Potential",
      "leadSummary": "Conservative nature of electrostatic fields, scalar electric potential, line integrals, potential of point charges, dipoles, and continuous charge distributions, negative gradient theorem E = -grad V, equipotential surfaces, conductor electrostatics, Faraday cages, and Van de Graaff high-voltage physics.",
      "sections": [
        {
          "id": "sec-2-1",
          "number": "\u00a72.1",
          "heading": "Electrostatic Potential and Conservative Electric Fields",
          "simulation": "potential-gradient-sim",
          "content": "The electrostatic force is conservative, which allows the introduction of a scalar electric potential field.\n\n<h4>1. Path Independence and Conservative Nature</h4>\nThe work done by the electrostatic force on a test charge $q_0$ moving from point $A$ to point $B$ in any static electric field is strictly independent of the physical path taken:\n$$W_{A \\to B} = \\int_A^B \\vec{F} \\cdot d\\vec{r} = q_0 \\int_A^B \\vec{E} \\cdot d\\vec{r}$$\nConsequently, the line integral of the electrostatic field around any closed loop vanishes identically:\n$$\\oint_C \\vec{E} \\cdot d\\vec{r} = 0$$\nBy Stokes' theorem:\n$$\\oint_C \\vec{E} \\cdot d\\vec{r} = \\int_S (\\nabla \\times \\vec{E}) \\cdot d\\vec{A} = 0 \\implies \\nabla \\times \\vec{E} = 0$$\nThe static electric field is strictly **irrotational** (conservative).\n\n<h4>2. Definition of Electric Potential ($V$)</h4>\nThe electric potential difference $\\Delta V = V_B - V_A$ between points $A$ and $B$ is defined as the external work required per unit positive test charge to transport it from $A$ to $B$ at constant kinetic energy:\n$$\\Delta V = V_B - V_A = -\\int_A^B \\vec{E} \\cdot d\\vec{r}$$\nTaking the standard reference point at infinity ($V(\\infty) = 0$), the absolute electric potential at point $P$ is:\n$$V(\\vec{r}) = -\\int_\\infty^{\\vec{r}} \\vec{E} \\cdot d\\vec{r}'$$\nSI Unit: **Volt (V)**:\n$$1 \\text{ Volt} = 1 \\text{ Joule/Coulomb (J/C)}$$\nDimensionally: $[V] = M L^2 T^{-3} I^{-1}$.\n\n<h4>3. Electric Potential Energy ($U$)</h4>\nThe electrostatic potential energy $U$ of a charge $q$ located at a point of electric potential $V$ is:\n$$U = q V$$\nThe electron-volt (eV) is defined as the kinetic energy acquired by an electron accelerated through a potential difference of 1 Volt:\n$$1 \\text{ eV} = 1.602176634 \\times 10^{-19} \\text{ Joules}$$"
        },
        {
          "id": "sec-2-2",
          "number": "\u00a72.2",
          "heading": "Potential due to Point Charges, Dipoles, and Continuous Distributions",
          "simulation": "potential-gradient-sim",
          "content": "Calculating the scalar electric potential is algebraically much simpler than computing the vector electric field directly.\n\n<h4>1. Potential of an Isolated Point Charge</h4>\nIntegrating the radial field $\\vec{E} = \\frac{q}{4\\pi\\epsilon_0 r^2}\\hat{r}$ from $\\infty$ to $r$:\n$$V(r) = -\\int_\\infty^r \\frac{q}{4\\pi\\epsilon_0 r'^2} dr' = \\left[ \\frac{q}{4\\pi\\epsilon_0 r'} \\right]_\\infty^r = \\frac{1}{4\\pi\\epsilon_0} \\frac{q}{r}$$\nNotice $V \\propto 1/r$ (whereas field $E \\propto 1/r^2$).\nBy scalar superposition, the potential due to $N$ discrete point charges is:\n$$V(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\sum_{i=1}^N \\frac{q_i}{|\\vec{r} - \\vec{r}_i|}$$\n\n<h4>2. Potential of an Electric Dipole</h4>\nConsider a dipole consisting of $+q$ at $(0, 0, a)$ and $-q$ at $(0, 0, -a)$ with dipole moment $p = 2qa$ aligned along the z-axis.\nAt field point $(r, \\theta)$ where distance $r \\gg a$:\n$$r_+ \\approx r - a \\cos\\theta, \\quad r_- \\approx r + a \\cos\\theta$$\n$$V(r, \\theta) = \\frac{q}{4\\pi\\epsilon_0} \\left( \\frac{1}{r_+} - \\frac{1}{r_-} \\right) \\approx \\frac{q}{4\\pi\\epsilon_0} \\left( \\frac{r_- - r_+}{r^2} \\right) = \\frac{q (2a \\cos\\theta)}{4\\pi\\epsilon_0 r^2}$$\n$$V(r, \\theta) = \\frac{1}{4\\pi\\epsilon_0} \\frac{\\vec{p} \\cdot \\hat{r}}{r^2} = \\frac{1}{4\\pi\\epsilon_0} \\frac{p \\cos\\theta}{r^2}$$\nKey properties of the dipole potential:\n<ul>\n  <li>Decays as $1/r^2$ (faster than the $1/r$ point charge monopole potential).</li>\n  <li>Vanishes identically in the equatorial plane ($\\theta = 90^\\circ \\implies \\cos(90^\\circ) = 0$).</li>\n</ul>\n\n<h4>3. Continuous Charge Distributions</h4>\nFor continuous sources:\n$$V(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0} \\int_{V'} \\frac{\\rho(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dV'$$\n$$V_{\\text{surface}} = \\frac{1}{4\\pi\\epsilon_0} \\int_{S'} \\frac{\\sigma(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dA', \\quad V_{\\text{line}} = \\frac{1}{4\\pi\\epsilon_0} \\int_{L'} \\frac{\\lambda(\\vec{r}')}{|\\vec{r} - \\vec{r}'|} dl'$$"
        },
        {
          "id": "sec-2-3",
          "number": "\u00a72.3",
          "heading": "Calculation of Electric Field from Potential: The Negative Gradient",
          "simulation": "potential-gradient-sim",
          "content": "Because the electrostatic field is conservative ($\\nabla \\times \\vec{E} = 0$), vector calculus guarantees that it can be expressed as the negative gradient of a scalar potential.\n\n<h4>1. The Gradient Relation</h4>\nConsider an infinitesimal displacement $d\\vec{r} = dx \\hat{i} + dy \\hat{j} + dz \\hat{k}$:\n$$dV = -\\vec{E} \\cdot d\\vec{r} = - (E_x dx + E_y dy + E_z dz)$$\nBy the multivariable chain rule:\n$$dV = \\frac{\\partial V}{\\partial x} dx + \\frac{\\partial V}{\\partial y} dy + \\frac{\\partial V}{\\partial z} dz$$\nEquating coefficients:\n$$E_x = -\\frac{\\partial V}{\\partial x}, \\quad E_y = -\\frac{\\partial V}{\\partial y}, \\quad E_z = -\\frac{\\partial V}{\\partial z}$$\nIn compact vector notation:\n$$\\vec{E} = -\\nabla V$$\nwhere $\\nabla = \\hat{i} \\frac{\\partial}{\\partial x} + \\hat{j} \\frac{\\partial}{\\partial y} + \\hat{k} \\frac{\\partial}{\\partial z}$ is the vector del operator.\n\n<h4>2. Physical Interpretation</h4>\n<ul>\n  <li>The mathematical gradient $\\nabla V$ points in the direction of maximum spatial increase of potential.</li>\n  <li>Therefore, the electric field vector $\\vec{E} = -\\nabla V$ **always points in the direction of steepest potential decrease**.</li>\n  <li>Positive charges naturally accelerate from regions of high electric potential toward regions of low electric potential.</li>\n</ul>\n\n<h4>3. Equipotential Surfaces and Orthogonality</h4>\nAn **equipotential surface** is the spatial locus of all points having identical electric potential ($V(x, y, z) = \\text{constant}$).\nFor any displacement $d\\vec{r}$ lying entirely within an equipotential surface:\n$$dV = -\\vec{E} \\cdot d\\vec{r} = 0$$\nBecause $d\\vec{r}$ is non-zero, this requires:\n$$\\vec{E} \\perp d\\vec{r}$$\n<em>Fundamental Geometric Theorem:</em> The electric field vector is everywhere perpendicular (orthogonal) to equipotential surfaces. Equipotential lines and electric field lines form a mutually orthogonal coordinate mesh."
        },
        {
          "id": "sec-2-4",
          "number": "\u00a72.4",
          "heading": "Electrostatic Properties of Insulated Conductors in Equilibrium",
          "simulation": "potential-gradient-sim",
          "content": "In an electrical conductor, valence electrons are free to migrate throughout the crystalline lattice. In static equilibrium, charge migration ceases, establishing several fundamental physical theorems.\n\n<h4>1. Zero Internal Electric Field</h4>\nInside the bulk material of a conductor in electrostatic equilibrium:\n$$\\vec{E}_{\\text{internal}} = 0$$\n*Proof:* If $\\vec{E}$ were non-zero inside, the free electrons would experience forces $\\vec{F} = -e\\vec{E}$ and accelerate, generating macroscopic currents, contradicting the premise of static equilibrium.\n\n<h4>2. Zero Net Internal Charge Density</h4>\nApplying Gauss's law $\\nabla \\cdot \\vec{E} = \\rho / \\epsilon_0$ to any interior region:\n$$\\vec{E} = 0 \\implies \\rho = 0$$\n*Theorem:* Any net excess electric charge deposited on an insulated conductor resides entirely on its outer geometric surface.\n\n<h4>3. The Entire Conductor is an Equipotential Volume</h4>\nFor any two interior points $A$ and $B$:\n$$V_B - V_A = -\\int_A^B \\vec{E} \\cdot d\\vec{r} = 0 \\implies V_A = V_B = \\text{constant}$$\nThe surface and entire interior of a conductor exist at the exact same scalar potential.\n\n<h4>4. Electric Field Immediately Outside a Charged Conductor</h4>\nConstruct a Gaussian pillbox of area $dA$ straddling the conductor surface:\nThe bottom face inside the metal has $\\vec{E} = 0$. The curved side has zero flux. The top face outside has field $\\vec{E} \\perp$ surface:\n$$\\oint \\vec{E} \\cdot d\\vec{A} = E dA = \\frac{dq}{\\epsilon_0} = \\frac{\\sigma dA}{\\epsilon_0} \\implies E = \\frac{\\sigma}{\\epsilon_0}$$\n$$\\vec{E} = \\frac{\\sigma}{\\epsilon_0} \\hat{n}$$\nNotice this field is exactly double the field of a single non-conducting sheet ($\\sigma / 2\\epsilon_0$), because charge inside the conductor rearranges to produce zero field internally and constructive reinforcement externally.\n\n<h4>5. Electrostatic Shielding (Faraday Cage)</h4>\nIn a hollow conducting shell with a cavity containing zero charge, $\\vec{E} = 0$ everywhere inside the cavity, regardless of external electric fields. This is **electrostatic shielding**."
        },
        {
          "id": "sec-2-5",
          "number": "\u00a72.5",
          "heading": "The Van de Graaff Electrostatic Generator and High Voltage Physics",
          "simulation": "potential-gradient-sim",
          "content": "Robert J. Van de Graaff (1929) developed the electrostatic accelerator generator, capable of generating potentials exceeding 5 to 20 million Volts.\n\n<h4>1. Working Principle</h4>\nThe Van de Graaff generator exploits two electrostatic principles:\n<ol>\n  <li><strong>Corona Discharge (Action of Sharp Points):</strong> At sharp conducting needles of radius of curvature $r$, the surface charge density $\\sigma \\propto 1/r$ becomes immense. When local field exceeds the dielectric breakdown strength of air ($E_{\\text{breakdown}} \\approx 3 \\times 10^6 \\text{ V/m}$), air molecules ionize, spraying ions onto an insulating moving belt.</li>\n  <li><strong>Cavity Charge Transfer:</strong> When a charged conductor contacts the *interior* surface of a hollow conducting sphere, all charge transfers completely to the *exterior* surface, regardless of how high the sphere's potential already is!</li>\n</ol>\n\n<h4>2. Mathematical Limit on Terminal Potential</h4>\nFor a spherical high-voltage dome of radius $R$ carrying charge $Q$:\n$$V = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{R}, \\quad E = \\frac{1}{4\\pi\\epsilon_0} \\frac{Q}{R^2} = \\frac{V}{R}$$\nHence, the maximum sustainable potential is limited by dielectric breakdown of the surrounding gas:\n$$V_{\\max} = R \\cdot E_{\\text{breakdown}}$$\nIn atmospheric air ($E_b = 3 \\text{ MV/m}$), a dome of radius $R = 1.0\\text{ m}$ attains $V_{\\max} = 3.0\\text{ MV}$.\nImmersing the generator in high-pressure insulating sulfur hexafluoride ($SF_6$) gas raises $E_b$ fivefold, enabling tandem accelerators to reach 25 million Volts for nuclear transmutation experiments."
        }
      ],
      "problems": [
        {
          "id": "prob-2-1",
          "difficulty": "Undergraduate Standard Classical Exam",
          "title": "Electric Potential of an Annular Charged Disk",
          "question": "A thin flat non-conducting annular ring has inner radius $a = 5.00\\text{ cm}$ and outer radius $b = 15.0\\text{ cm}$. It carries a uniform surface charge density $\\sigma = 4.00 \\times 10^{-6}\\text{ C/m}^2$.\\n(a) Derive an analytical expression for the electric potential $V(z)$ along the central axis of symmetry at perpendicular distance $z$ from the plane of the ring,\\n(b) Calculate $V$ at $z = 10.0\\text{ cm}$, and\\n(c) Use $\\vec{E} = -\\nabla V$ to determine the axial electric field $E_z(z)$ at $z = 10.0\\text{ cm}$.",
          "steps": [
            {
              "title": "Step 1: Integrate annular rings to derive potential",
              "math": "$$dq = \\sigma (2\\pi r dr)$$\n$$\\text{Distance to axial point: } R_d = \\sqrt{z^2 + r^2}$$\n$$V(z) = \\frac{1}{4\\pi\\epsilon_0} \\int_a^b \\frac{\\sigma (2\\pi r dr)}{\\sqrt{z^2 + r^2}} = \\frac{\\sigma}{2\\epsilon_0} \\left[ \\sqrt{z^2 + r^2} \\right]_a^b$$\n$$V(z) = \\frac{\\sigma}{2\\epsilon_0} \\left( \\sqrt{z^2 + b^2} - \\sqrt{z^2 + a^2} \\right)$$",
              "explanation": "Integrating concentric infinitesimal rings of area $2\\pi r dr$ gives the exact axial potential."
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
              "explanation": "The total self-energy of a uniformly charged solid sphere is $\\frac{3}{5} \\frac{Q^2}{4\\pi\\epsilon_0 R}$."
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
    },
    {
      "number": 3,
      "title": "Capacitors and Dielectrics",
      "leadSummary": "Comprehensive physical analysis of capacitors and capacitance calculations for planar, cylindrical, and spherical geometries, atomic mechanisms of dielectric polarization, Gauss's law in dielectrics, the three electric vectors E, D, and P, electrostatic energy storage, and field energy density.",
      "sections": [
        {
          "id": "sec-3-1",
          "number": "\u00a73.1",
          "heading": "Capacitor Fundamentals and Geometric Capacitance Calculations",
          "simulation": "dielectric-capacitor-sim",
          "content": "A capacitor is a passive circuit component designed to store electric charge and electrostatic energy within an electric field established between two isolated conductors.\n\n<h4>1. Definition of Capacitance</h4>\nWhen equal and opposite charges $+Q$ and $-Q$ are deposited on two conducting electrodes separated by an insulating gap, a potential difference $V$ develops between them.\nThe <strong>capacitance</strong> $C$ is defined as the ratio of the magnitude of stored charge on either conductor to the potential difference:\n$$C = \\frac{Q}{V}$$\nSI Unit: **Farad (F)** ($1 \\text{ Farad} = 1 \\text{ Coulomb/Volt}$).\nBecause 1 Farad is exceptionally large, practical capacitors are measured in microfarads ($\\mu\\text{F} = 10^{-6}\\text{ F}$), nanofarads ($\\text{nF} = 10^{-9}\\text{ F}$), or picofarads ($\\text{pF} = 10^{-12}\\text{ F}$).\nCapacitance depends strictly on geometric shape, dimensions, and the permittivity of the medium, completely independent of applied charge or voltage.\n\n<h4>2. Parallel-Plate Capacitor</h4>\nConsider two parallel planar conducting plates of area $A$ separated by vacuum gap $d$ ($d \\ll \\sqrt{A}$ to minimize fringe fields).\nCharge density is $\\sigma = Q/A$. By Gauss's law, the uniform electric field between plates is:\n$$E = \\frac{\\sigma}{\\epsilon_0} = \\frac{Q}{\\epsilon_0 A}$$\nThe potential difference is:\n$$V = \\int_0^d E \\, dz = E d = \\frac{Q d}{\\epsilon_0 A}$$\nTherefore, the capacitance is:\n$$C = \\frac{Q}{V} = \\frac{\\epsilon_0 A}{d}$$\n\n<h4>3. Cylindrical Capacitor (Coaxial Cable)</h4>\nConsider two concentric cylindrical conductors of length $L$ ($L \\gg b$), inner radius $a$, and outer radius $b$.\nWith linear charge density $\\lambda = Q/L$, the radial electric field between cylinders is $E(r) = \\frac{\\lambda}{2\\pi\\epsilon_0 r}$.\nThe potential difference is:\n$$V = \\int_a^b E(r) dr = \\frac{\\lambda}{2\\pi\\epsilon_0} \\int_a^b \\frac{dr}{r} = \\frac{Q}{2\\pi\\epsilon_0 L} \\ln\\left(\\frac{b}{a}\\right)$$\n$$C = \\frac{Q}{V} = \\frac{2\\pi\\epsilon_0 L}{\\ln(b/a)}$$\nCapacitance per unit length: $\\frac{C}{L} = \\frac{2\\pi\\epsilon_0}{\\ln(b/a)}$ (crucial for RF transmission lines).\n\n<h4>4. Spherical Capacitor</h4>\nConsider two concentric conducting spheres of inner radius $a$ and outer radius $b$.\nRadial field: $E(r) = \\frac{Q}{4\\pi\\epsilon_0 r^2}$.\n$$V = \\int_a^b \\frac{Q}{4\\pi\\epsilon_0 r^2} dr = \\frac{Q}{4\\pi\\epsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) = \\frac{Q (b - a)}{4\\pi\\epsilon_0 a b}$$\n$$C = \\frac{4\\pi\\epsilon_0 a b}{b - a}$$\nFor an **isolated spherical conductor** ($b \\to \\infty$, outer shell at infinity):\n$$C_{\\text{isolated}} = 4\\pi\\epsilon_0 a$$\nFor Earth ($a \\approx 6.371 \\times 10^6\\text{ m}$): $C_{\\text{Earth}} \\approx 709 \\ \\mu\\text{F}$."
        },
        {
          "id": "sec-3-2",
          "number": "\u00a73.2",
          "heading": "Dielectric Media, Bound Charges, and Gauss's Law in Dielectrics",
          "simulation": "dielectric-capacitor-sim",
          "content": "When an insulating material (dielectric) is inserted into an electric field, its constituent atoms or molecules undergo microscopic polarization.\n\n<h4>1. Molecular Mechanism of Dielectrics</h4>\nDielectric materials belong to two classes:\n<ul>\n  <li><strong>Non-Polar Dielectrics (e.g., $N_2, O_2, CH_4$):</strong> Molecular centers of positive and negative charge coincide in the absence of an external field. An applied field $\\vec{E}_0$ exerts opposite forces on electrons and nuclei, inducing microscopic dipole moments $\\vec{p} = \\alpha \\vec{E}_{\\text{loc}}$ (electronic polarization).</li>\n  <li><strong>Polar Dielectrics (e.g., $H_2O, HCl$):</strong> Molecules possess permanent dipole moments. Thermal motion causes random orientations. An applied field $\\vec{E}_0$ exerts torques that partially align the dipoles along $\\vec{E}_0$ (orientational polarization).</li>\n</ul>\n\n<h4>2. Induced Bound Charge and Field Reduction</h4>\nThe aligned dipoles create microscopic cancellation inside the bulk, but leave net unneutralized <strong>bound surface charges</strong> $\\pm Q_b$ (or surface density $\\sigma_b$) on the dielectric faces.\nThese bound charges set up an internal opposing electric field $\\vec{E}_b = -(\\sigma_b / \\epsilon_0) \\hat{n}$.\nThe net resultant electric field inside the dielectric is:\n$$\\vec{E} = \\vec{E}_0 + \\vec{E}_b = \\frac{\\vec{E}_0}{\\kappa} = \\frac{\\vec{E}_0}{\\epsilon_r}$$\nwhere $\\kappa = \\epsilon_r > 1$ is the <strong>dielectric constant (relative permittivity)</strong>.\nThe presence of a dielectric weakens the electric field by a factor of $\\kappa$:\n$$E = \\frac{\\sigma - \\sigma_b}{\\epsilon_0} = \\frac{\\sigma}{\\kappa \\epsilon_0} \\implies \\sigma_b = \\sigma \\left( 1 - \\frac{1}{\\kappa} \\right)$$\n\n<h4>3. Capacitance with Dielectric</h4>\nInserting a dielectric slab of constant $\\kappa$ filling the entire gap of a capacitor:\n<ul>\n  <li><strong>Isolated Capacitor (Constant Charge $Q$):</strong> Potential drops $V = V_0 / \\kappa$; Capacitance increases:\n  $$C = \\frac{Q}{V} = \\kappa C_0$$</li>\n  <li><strong>Battery-Connected Capacitor (Constant Voltage $V$):</strong> Battery supplies extra charge $Q = \\kappa Q_0$; Capacitance increases $C = \\kappa C_0$.</li>\n</ul>"
        },
        {
          "id": "sec-3-3",
          "number": "\u00a73.3",
          "heading": "The Three Electric Vectors: E, D, and P",
          "simulation": "dielectric-capacitor-sim",
          "content": "To treat macroscopic electrostatics in matter without resolving individual microscopic atomic charges, electromagnetic theory introduces three fundamental vector fields: $\\vec{E}$, $\\vec{D}$, and $\\vec{P}$.\n\n<h4>1. The Electric Polarization Vector ($\\vec{P}$)</h4>\nThe <strong>polarization vector</strong> $\\vec{P}$ is defined as the electric dipole moment per unit volume of the dielectric medium:\n$$\\vec{P} = \\lim_{\\Delta V \\to 0} \\frac{\\sum \\vec{p}_i}{\\Delta V}$$\nSI Unit: $\\text{Coulomb/m}^2$ (C/m\u00b2).\nThe polarization $\\vec{P}$ is directly related to bound charges:\n$$\\rho_b = -\\nabla \\cdot \\vec{P} \\quad (\\text{Volume bound charge density})$$\n$$\\sigma_b = \\vec{P} \\cdot \\hat{n} \\quad (\\text{Surface bound charge density})$$\n\n<h4>2. The Electric Displacement Vector ($\\vec{D}$)</h4>\nIn a dielectric, total charge density consists of free charges $\\rho_f$ (introduced on metal electrodes) and bound charges $\\rho_b$ (induced in dielectric):\n$$\\nabla \\cdot \\vec{E} = \\frac{\\rho_{\\text{total}}}{\\epsilon_0} = \\frac{\\rho_f + \\rho_b}{\\epsilon_0} = \\frac{\\rho_f - \\nabla \\cdot \\vec{P}}{\\epsilon_0}$$\n$$\\nabla \\cdot (\\epsilon_0 \\vec{E} + \\vec{P}) = \\rho_f$$\nWe define the <strong>Electric Displacement Field</strong> $\\vec{D}$ as:\n$$\\vec{D} = \\epsilon_0 \\vec{E} + \\vec{P}$$\nSI Unit: $\\text{Coulomb/m}^2$ (C/m\u00b2).\nThis yields **Gauss's Law in Dielectric Media**:\n$$\\nabla \\cdot \\vec{D} = \\rho_f \\iff \\oint_S \\vec{D} \\cdot d\\vec{A} = Q_{\\text{free, encl}}$$\n<em>Major Theoretical Advantage:</em> The flux of $\\vec{D}$ depends **exclusively on free charges** $Q_{\\text{free}}$, completely bypassing the need to know the complex bound charges!\n\n<h4>3. Linear Isotropic Dielectrics and Susceptibility</h4>\nFor linear dielectrics:\n$$\\vec{P} = \\epsilon_0 \\chi_e \\vec{E}$$\nwhere $\\chi_e$ is the dimensionless <strong>electric susceptibility</strong>.\nSubstituting into $\\vec{D}$:\n$$\\vec{D} = \\epsilon_0 \\vec{E} + \\epsilon_0 \\chi_e \\vec{E} = \\epsilon_0 (1 + \\chi_e) \\vec{E} = \\epsilon_0 \\epsilon_r \\vec{E} = \\epsilon \\vec{E}$$\n$$\\epsilon_r = 1 + \\chi_e = \\kappa$$\nwhere $\\epsilon = \\epsilon_0 \\epsilon_r$ is the absolute permittivity of the material."
        },
        {
          "id": "sec-3-4",
          "number": "\u00a73.4",
          "heading": "Electrostatic Energy Storage and Field Energy Density",
          "simulation": "dielectric-capacitor-sim",
          "content": "Charging a capacitor requires performing work against the opposing electric field already created by previously deposited charges.\n\n<h4>1. Work Done in Charging a Capacitor</h4>\nConsider charging a capacitor to final charge $Q$ and potential $V$.\nWhen the capacitor carries instantaneous charge $q$, the potential difference is $v = q/C$.\nThe work required to transfer an additional infinitesimal charge $dq$ from the negative plate to the positive plate is:\n$$dW = v \\, dq = \\frac{q}{C} dq$$\nThe total work required to charge the capacitor from $q = 0$ to $q = Q$ is stored as internal electrostatic potential energy $U$:\n$$U = \\int_0^Q \\frac{q}{C} dq = \\frac{Q^2}{2C}$$\nUsing $Q = C V$:\n$$U = \\frac{1}{2} \\frac{Q^2}{C} = \\frac{1}{2} C V^2 = \\frac{1}{2} Q V$$\n\n<h4>2. Spatial Energy Density of the Electric Field ($u_E$)</h4>\nWhere is this electrostatic energy physically stored? Michael Faraday and James Clerk Maxwell demonstrated that energy resides not on the metal plates, but is distributed continuously throughout the **electric field itself**.\nFor a parallel-plate capacitor of plate area $A$ and gap $d$:\n$$C = \\frac{\\epsilon A}{d}, \\quad V = E d$$\n$$U = \\frac{1}{2} C V^2 = \\frac{1}{2} \\left( \\frac{\\epsilon A}{d} \\right) (E d)^2 = \\frac{1}{2} \\epsilon E^2 (A d)$$\nBecause the volume occupied by the electric field is $\\text{Volume} = A d$, the **electrostatic energy density** $u_E$ (Joules per cubic meter) is:\n$$u_E = \\frac{U}{\\text{Volume}} = \\frac{1}{2} \\epsilon E^2 = \\frac{1}{2} \\epsilon_0 \\epsilon_r E^2 = \\frac{1}{2} \\vec{D} \\cdot \\vec{E}$$\nThis formula holds universally for *any* electric field configuration in vacuum or dielectric media.\nThe total energy in an arbitrary volume $V$ is:\n$$U = \\int_V \\frac{1}{2} (\\vec{D} \\cdot \\vec{E}) dV$$"
        }
      ],
      "problems": [
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
    },
    {
      "number": 4,
      "title": "Current and Resistance",
      "leadSummary": "Microscopic and macroscopic physics of electric current, current density, the classical Drude model of electron drift, temperature-dependent resistivity, Electromotive Force, Kirchhoff's circuit rules, multi-loop networks, galvanometers, ammeters, voltmeters, potentiometers, RC charging and discharging transients, and thermoelectric phenomena (Seebeck, Peltier, Thomson).",
      "sections": [
        {
          "id": "sec-4-1",
          "number": "\u00a74.1",
          "heading": "Electric Current, Current Density, and the Microscopic Drude Model",
          "simulation": "drude-current-sim",
          "content": "Electric current is the organized macroscopic transport of electric charge across a cross-section of a conducting medium.\n\n<h4>1. Electric Current and Current Density</h4>\nThe instantaneous <strong>electric current</strong> $I$ is defined as the net charge passing through a surface per unit time:\n$$I = \\frac{dq}{dt}$$\nSI Unit: **Ampere (A)** ($1 \\text{ A} = 1 \\text{ C/s}$).\nCurrent is a macroscopic scalar quantity. The microscopic vector characterizing charge flow at every spatial point is the <strong>Current Density</strong> $\\vec{J}$:\n$$I = \\int_S \\vec{J} \\cdot d\\vec{A}$$\nFor uniform current across a normal cross-sectional area $A$:\n$$J = \\frac{I}{A} \\quad (\\text{Units: A/m}^2)$$\n\n<h4>2. Drift Velocity of Charge Carriers</h4>\nIn a conductor with free charge carrier density $n$ (electrons/m\u00b3) each carrying charge $q = -e$:\nIn time increment $dt$, carriers advance by length $dx = v_d dt$, where $v_d$ is the average **drift velocity**.\nThe charge traversing cross-section $A$ is $dq = n q (A v_d dt)$.\nHence:\n$$I = n q A v_d = n e A v_d \\implies \\vec{J} = n q \\vec{v}_d = -n e \\vec{v}_d$$\n<em>Striking Numerical Fact:</em> While electrical signals propagate at near the speed of light ($c \\sim 3 \\times 10^8\\text{ m/s}$), the physical drift velocity of electrons in copper under typical domestic currents is astonishingly slow:\n$$v_d \\sim 10^{-4} \\text{ m/s} = 0.1 \\text{ mm/s}$$\nAn electron takes roughly three hours to travel one meter down a copper wire!\n\n<h4>3. The Classical Drude Model of Electrical Conduction</h4>\nPaul Drude (1900) modeled conduction electrons as an ideal classical gas undergoing random thermal collisions with positive ionic cores in a crystal lattice.\nBetween collisions, electrons accelerate under electric field $\\vec{E}$:\n$$\\vec{a} = \\frac{-e \\vec{E}}{m}$$\nLet $\\tau$ be the <strong>mean relaxation time</strong> (average time between collisions).\nThe average drift velocity acquired is:\n$$\\vec{v}_d = \\vec{a} \\tau = -\\frac{e \\tau}{m} \\vec{E}$$\nSubstituting into current density:\n$$\\vec{J} = -n e \\vec{v}_d = \\left( \\frac{n e^2 \\tau}{m} \\right) \\vec{E}$$\nDefining electrical conductivity $\\sigma$:\n$$\\vec{J} = \\sigma \\vec{E} \\quad (\\text{Microscopic Ohm's Law})$$\nwhere:\n$$\\sigma = \\frac{n e^2 \\tau}{m}, \\quad \\rho = \\frac{1}{\\sigma} = \\frac{m}{n e^2 \\tau}$$\nThis demonstrates that Ohm's law arises directly from frequent momentum-relaxing collisions."
        },
        {
          "id": "sec-4-2",
          "number": "\u00a74.2",
          "heading": "Resistance, Resistivity, and Temperature Dependence",
          "simulation": "drude-current-sim",
          "content": "Resistance is the macroscopic property of an electrical conductor that opposes the flow of electric current.\n\n<h4>1. Macroscopic Ohm's Law and Resistance</h4>\nConsider a conductor of uniform length $L$ and cross-sectional area $A$ carrying current $I$ under potential difference $V$.\nUsing $E = V/L$ and $J = I/A$ in $\\vec{J} = \\sigma \\vec{E}$:\n$$\\frac{I}{A} = \\sigma \\frac{V}{L} = \\frac{1}{\\rho} \\frac{V}{L} \\implies V = I \\left( \\frac{\\rho L}{A} \\right)$$\nWe define <strong>Electrical Resistance ($R$)</strong>:\n$$R = \\frac{V}{I} = \\frac{\\rho L}{A}$$\nSI Unit: **Ohm ($\\Omega$)** ($1 \\ \\Omega = 1 \\text{ V/A}$).\n<strong>Resistivity ($\\rho$)</strong> is an intrinsic material property (Units: $\\Omega\\cdot\\text{m}$).\n\n<h4>2. Temperature Variation of Resistivity</h4>\nAs temperature rises, thermal lattice vibrations (phonons) increase in amplitude, scattering conduction electrons more frequently and reducing collision time $\\tau$.\nOver moderate temperature intervals:\n$$\\rho(T) = \\rho_0 [1 + \\alpha (T - T_0)]$$\n$$R(T) = R_0 [1 + \\alpha (T - T_0)]$$\nwhere $\\alpha$ is the <strong>temperature coefficient of resistivity</strong> (K\u207b\u00b9 or \u00b0C\u207b\u00b9).\n<ul>\n  <li><strong>Metals ($\\alpha > 0$):</strong> Resistivity increases with temperature (e.g., copper $\\alpha \\approx +0.0039\\text{ K}^{-1}$).</li>\n  <li><strong>Semiconductors ($\\alpha < 0$):</strong> In silicon and germanium, higher temperatures thermally excite vastly more covalent electrons into the conduction band, increasing carrier density $n$ exponentially ($n \\propto e^{-E_g/2k_B T}$). Thus, resistivity drops sharply with temperature!</li>\n  <li><strong>Superconductors:</strong> Below a critical temperature $T_c$, electrical resistance vanishes completely ($R \\equiv 0$).</li>\n</ul>"
        },
        {
          "id": "sec-4-3",
          "number": "\u00a74.3",
          "heading": "Electromotive Force, Terminal Voltage, and Kirchhoff's Laws",
          "simulation": "drude-current-sim",
          "content": "To maintain a steady continuous current through a closed circuit, an energy source must perform work on charge carriers to transport them against electrostatic fields from low potential to high potential.\n\n<h4>1. Electromotive Force (EMF, $\\mathcal{E}$)</h4>\nAn <strong>Electromotive Force</strong> $\\mathcal{E}$ is any non-electrostatic mechanism (chemical in batteries, mechanical/magnetic in dynamos, thermal in thermocouples) that does work on charge:\n$$\\mathcal{E} = \\frac{dW_{\\text{non-elec}}}{dq}$$\nA real voltage source possesses internal resistance $r$.\nWhen delivering load current $I$, the terminal potential difference $V$ across the battery is:\n$$V = \\mathcal{E} - I r$$\nIf the source is open-circuited ($I = 0$), $V = \\mathcal{E}$.\n\n<h4>2. Kirchhoff's Circuit Laws</h4>\nGustav Kirchhoff (1845) formulated two fundamental conservation laws for multi-loop electrical networks:\n<ol>\n  <li><strong>Kirchhoff's Current Law (KCL / Junction Rule):</strong>\n  The algebraic sum of all electric currents entering any junction node is identically zero:\n  $$\\sum_{k} I_k = 0$$\n  <em>Physical Basis:</em> Direct consequence of the <strong>conservation of electric charge</strong> ($\\frac{\\partial\\rho}{\\partial t} = 0$).</li>\n  <li><strong>Kirchhoff's Voltage Law (KVL / Loop Rule):</strong>\n  The algebraic sum of all potential differences (EMFs and resistive $IR$ drops) around any closed circuit loop is zero:\n  $$\\sum_{k} \\mathcal{E}_k - \\sum_{k} I_k R_k = 0$$\n  <em>Physical Basis:</em> Direct consequence of the <strong>conservation of energy</strong> in a conservative electrostatic field ($\\oint \\vec{E} \\cdot d\\vec{r} = 0$).</li>\n</ol>"
        },
        {
          "id": "sec-4-4",
          "number": "\u00a74.4",
          "heading": "Electrical Measuring Instruments: Galvanometer, Ammeter, Voltmeter, and Potentiometer",
          "simulation": "drude-current-sim",
          "content": "Laboratory electrical measurements rely on precision meters configured from a basic d'Arsonval moving-coil galvanometer.\n\n<h4>1. The Moving-Coil Galvanometer</h4>\nA galvanometer detects minute currents. A coil of $N$ turns and resistance $R_g$ suspended in a radial magnetic field experiences deflecting torque $\\tau = N I A B$.\nBalanced by torsional spring restoring torque $\\tau_s = C \\theta$:\n$$I = \\left(\\frac{C}{N A B}\\right) \\theta = K \\theta$$\nThe deflection angle $\\theta$ is directly proportional to current.\nFull-scale deflection current is denoted $I_g$ (typically $50\\ \\mu\\text{A} - 1\\text{ mA}$).\n\n<h4>2. Conversion of Galvanometer to an Ammeter</h4>\nAn ammeter must connect in series and possess extremely low resistance to avoid perturbing circuit current.\nA low-resistance resistor called a <strong>shunt resistor ($R_s$)</strong> is connected in parallel with the galvanometer:\n$$I_s R_s = I_g R_g \\implies (I - I_g) R_s = I_g R_g$$\n$$R_s = \\frac{I_g R_g}{I - I_g}$$\n\n<h4>3. Conversion of Galvanometer to a Voltmeter</h4>\nA voltmeter must connect in parallel and possess extremely high resistance so it draws negligible current from the circuit.\nA large <strong>multiplier resistor ($R_m$)</strong> is connected in series with the galvanometer:\n$$V = I_g (R_g + R_m) \\implies R_m = \\frac{V}{I_g} - R_g$$\n\n<h4>4. The Slide-Wire Potentiometer</h4>\nA potentiometer measures unknown EMF $\\mathcal{E}_x$ without drawing any current at balance (null deflection), providing the theoretical ideal of an infinite-impedance voltmeter:\n$$\\frac{\\mathcal{E}_x}{\\mathcal{E}_0} = \\frac{l_x}{l_0}$$\nwhere $l_x$ is the balancing length for the test cell and $l_0$ for the standard cell."
        },
        {
          "id": "sec-4-5",
          "number": "\u00a74.5",
          "heading": "RC Circuits: Charging and Discharging Transients",
          "simulation": "rc-transient-sim",
          "content": "In circuits containing both resistors and capacitors, voltages and currents do not change instantaneously, but evolve exponentially over time.\n\n<h4>1. Charging an RC Circuit</h4>\nConsider a series circuit with battery $\\mathcal{E}$, resistor $R$, capacitor $C$, and switch closed at $t = 0$.\nBy Kirchhoff's voltage law:\n$$\\mathcal{E} - i R - \\frac{q}{C} = 0$$\nSince $i = \\frac{dq}{dt}$:\n$$R \\frac{dq}{dt} + \\frac{q}{C} = \\mathcal{E} \\implies \\frac{dq}{dt} = -\\frac{q - C\\mathcal{E}}{RC}$$\nIntegrating with initial condition $q(0) = 0$:\n$$q(t) = C\\mathcal{E} \\left( 1 - e^{-t/RC} \\right) = Q_0 \\left( 1 - e^{-t/\\tau} \\right)$$\nwhere $\\tau = R C$ is the **capacitive time constant** (Units: seconds, $\\Omega \\cdot \\text{F} = \\text{s}$).\nDifferentiating charge gives the decaying charging current:\n$$i(t) = \\frac{dq}{dt} = \\frac{\\mathcal{E}}{R} e^{-t/\\tau} = I_0 e^{-t/\\tau}$$\n\n<h4>2. Discharging an RC Circuit</h4>\nDisconnecting the battery and closing the loop across $R$:\n$$-i R - \\frac{q}{C} = 0 \\implies R \\frac{dq}{dt} + \\frac{q}{C} = 0$$\n$$q(t) = Q_0 e^{-t/\\tau}, \\quad i(t) = -\\frac{Q_0}{RC} e^{-t/\\tau} = -I_0 e^{-t/\\tau}$$\n\n<h4>3. The 50% Energy Paradox in Capacitor Charging</h4>\nDuring charging to final voltage $V$:\n<ul>\n  <li>Total energy delivered by the battery:\n  $$W_{\\text{battery}} = \\int_0^\\infty \\mathcal{E} i(t) dt = \\mathcal{E} \\int_0^\\infty dq = \\mathcal{E} Q_0 = C\\mathcal{E}^2$$</li>\n  <li>Final electrostatic energy stored in capacitor:\n  $$U_C = \\frac{1}{2} C\\mathcal{E}^2$$</li>\n  <li>Total Joule thermal energy dissipated in resistor:\n  $$W_{\\text{heat}} = \\int_0^\\infty i^2 R \\, dt = \\int_0^\\infty \\left(\\frac{\\mathcal{E}}{R} e^{-t/RC}\\right)^2 R \\, dt = \\frac{\\mathcal{E}^2}{R} \\int_0^\\infty e^{-2t/RC} dt = \\frac{1}{2} C\\mathcal{E}^2$$</li>\n</ul>\n<em>Fundamental Thermodynamic Theorem:</em> Exactly **50% of the energy supplied by the battery is inevitably dissipated as Joule heat** in the circuit, completely independent of the resistance $R$! (Even if $R \\to 0$, energy is lost via electromagnetic radiation)."
        },
        {
          "id": "sec-4-6",
          "number": "\u00a74.6",
          "heading": "Thermoelectricity: Seebeck, Peltier, and Thomson Effects",
          "simulation": "drude-current-sim",
          "content": "Thermoelectricity encompasses the direct microscopic coupling between thermal gradients and electric potential differences in conductors and semiconductors.\n\n<h4>1. The Seebeck Effect (1821)</h4>\nThomas Johann Seebeck discovered that when two dissimilar conducting wires $A$ and $B$ are joined at two junctions maintained at different temperatures $T_1$ and $T_2$, an open-circuit **thermoelectric EMF** $\\mathcal{E}_{AB}$ is established:\n$$\\mathcal{E}_{AB} = \\int_{T_1}^{T_2} S_{AB}(T) \\, dT$$\nwhere $S_{AB} = S_A - S_B$ is the differential <strong>Seebeck coefficient (Thermoelectric Power)</strong> in $\\mu\\text{V/K}$.\nOver modest temperature ranges:\n$$\\mathcal{E} = a (T_h - T_c) + \\frac{1}{2} b (T_h - T_c)^2$$\nThe <strong>neutral temperature ($T_n$)</strong> is the hot-junction temperature where EMF reaches its maximum ($\\frac{d\\mathcal{E}}{dT} = 0 \\implies T_n = -a/b$).\nBeyond the <strong>inversion temperature ($T_i = 2T_n - T_c$)</strong>, the polarity of the EMF reverses.\n\n<h4>2. The Peltier Effect (1834)</h4>\nJean Charles Athanase Peltier discovered the exact thermodynamic inverse of the Seebeck effect:\nWhen an electric current $I$ is driven through a junction between two dissimilar conductors, heat is either absorbed or released at the junction (over and above irreversible Joule heating):\n$$\\frac{dQ_{\\text{Peltier}}}{dt} = \\Pi_{AB} I$$\nwhere $\\Pi_{AB}$ is the <strong>Peltier coefficient</strong> (Volts).\nReversing current direction reverses heating to cooling! This enables solid-state thermoelectric coolers (Peltier coolers) used in satellite sensors, PCR machines, and silent refrigeration.\n\n<h4>3. The Thomson Effect and Kelvin Relations</h4>\nWilliam Thomson (Lord Kelvin, 1854) applied thermodynamics to prove that heat is reversibly absorbed or evolved when current passes along an individual homogeneous conductor having a temperature gradient $dT/dx$:\n$$\\frac{dQ_{\\text{Thomson}}}{dx} = \\mu I \\frac{dT}{dx}$$\nKelvin derived the celebrated **Kelvin (Onsager) Relations**:\n$$\\Pi_{AB} = T \\cdot S_{AB}, \\quad \\mu_A - \\mu_B = T \\frac{dS_{AB}}{dT}$$\nConnecting all three thermoelectric effects into a unified thermodynamic framework."
        }
      ],
      "problems": [
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
              "explanation": "The current density is $4.54 \\times 10^6$ A/m\u00b2."
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
    },
    {
      "number": 5,
      "title": "Magnetic Field",
      "leadSummary": "Lorentz force on moving charges and currents, cyclotron motion and helical trajectories, magnetic torque on current loops, moving-coil galvanometers, the Hall effect, the Biot-Savart law with circular loop applications, and Ampere's circuital law applied to straight conductors, solenoids, and toroids.",
      "sections": [
        {
          "id": "sec-5-1",
          "number": "\u00a75.1",
          "heading": "The Magnetic Field, Lorentz Force, and Charged Particle Trajectories",
          "simulation": "lorentz-hall-sim",
          "content": "Magnetism originates from electric charges in motion. A magnetic field is established by moving charges or permanent magnetic dipoles and exerts forces exclusively on moving charges.\n\n<h4>1. The Lorentz Force Law</h4>\nA particle carrying electric charge $q$ moving with velocity $\\vec{v}$ in a region containing both an electric field $\\vec{E}$ and a magnetic field $\\vec{B}$ experiences the unified <strong>Lorentz Force</strong>:\n$$\\vec{F} = q \\left( \\vec{E} + \\vec{v} \\times \\vec{B} \\right)$$\nThe magnetic force component is:\n$$\\vec{F}_B = q (\\vec{v} \\times \\vec{B})$$\nMagnitude: $F_B = |q| v B \\sin\\theta$, where $\\theta$ is the angle between $\\vec{v}$ and $\\vec{B}$.\nDirection: Governed by the vector cross product (Right-Hand Rule).\nSI Unit: **Tesla (T)** ($1 \\text{ Tesla} = 1 \\text{ N}/(\\text{A}\\cdot\\text{m}) = 10^4 \\text{ Gauss}$).\n\n<h4>2. Fundamental Properties of the Magnetic Force</h4>\n<ul>\n  <li><strong>Zero Work Property:</strong> Because $\\vec{F}_B$ is everywhere perpendicular to velocity $\\vec{v}$ ($\\vec{F}_B \\cdot \\vec{v} = q (\\vec{v} \\times \\vec{B}) \\cdot \\vec{v} \\equiv 0$), the instantaneous power delivered by a magnetic field is identically zero:\n  $$P = \\vec{F}_B \\cdot \\vec{v} = 0 \\implies dK = 0$$\n  <strong>A static magnetic field can NEVER change the kinetic energy or speed of a charged particle</strong>; it can only alter its direction of motion.</li>\n</ul>\n\n<h4>3. Cyclotron Motion and Helical Trajectories</h4>\nConsider a particle of mass $m$ and charge $q$ injected into a uniform magnetic field $\\vec{B} = B \\hat{k}$ with initial velocity $\\vec{v}_\\perp = v_x \\hat{i} + v_y \\hat{j}$.\nThe magnetic force acts as a pure centripetal force:\n$$q v_\\perp B = \\frac{m v_\\perp^2}{r} \\implies r_c = \\frac{m v_\\perp}{q B}$$\n$r_c$ is the <strong>cyclotron (Larmor) radius</strong>.\nThe period of circular revolution and the <strong>cyclotron angular frequency</strong> $\\omega_c$ are:\n$$T = \\frac{2\\pi r_c}{v_\\perp} = \\frac{2\\pi m}{q B}, \\quad \\omega_c = \\frac{q B}{m}$$\nNotice that $\\omega_c$ and $T$ are **completely independent of the particle's speed or orbital radius** (isochronism of the cyclotron).\nIf the particle possesses a parallel velocity component $v_\\parallel = v_z \\hat{k}$, it executes a **helical path** with pitch $p = v_\\parallel T = \\frac{2\\pi m v_\\parallel}{q B}$."
        },
        {
          "id": "sec-5-2",
          "number": "\u00a75.2",
          "heading": "Magnetic Force on a Current-Carrying Conductor and Torque on a Current Loop",
          "simulation": "lorentz-hall-sim",
          "content": "Because electric current consists of an ensemble of moving charges, magnetic forces manifest macroscopically on current-carrying wires.\n\n<h4>1. Magnetic Force on a Wire Element</h4>\nConsider a differential segment of wire of cross-section $A$ and length $d\\vec{l}$ carrying current $I = n q A v_d$.\nThe number of charge carriers in the segment is $dN = n A dl$.\nThe total magnetic force on the element is:\n$$d\\vec{F} = dN \\cdot q (\\vec{v}_d \\times \\vec{B}) = (n A dl) q (\\vec{v}_d \\times \\vec{B}) = (n q A v_d) (d\\vec{l} \\times \\vec{B})$$\n$$d\\vec{F} = I (d\\vec{l} \\times \\vec{B})$$\nFor a straight wire of finite length $\\vec{L}$ in a uniform magnetic field:\n$$\\vec{F} = I (\\vec{L} \\times \\vec{B})$$\n\n<h4>2. Torque on a Planar Current Loop and Magnetic Dipole Moment</h4>\nConsider a closed rectangular loop of dimensions $a \\times b$ (area $A = ab$) carrying current $I$ in a uniform magnetic field $\\vec{B}$.\nThe net translational force vanishes ($\\vec{F}_{\\text{net}} = 0$).\nHowever, forces on opposite arms form a couple, generating net torque:\n$$\\vec{\\tau} = \\vec{\\mu} \\times \\vec{B}$$\nwhere $\\vec{\\mu}$ is the <strong>magnetic dipole moment vector</strong>:\n$$\\vec{\\mu} = N I \\vec{A} = N I A \\hat{n}$$\nfor a coil of $N$ turns, where $\\hat{n}$ is the unit normal given by the right-hand grip rule.\nSI Unit: $\\text{A}\\cdot\\text{m}^2 = \\text{J/T}$.\nThe potential energy of the magnetic dipole in field $\\vec{B}$ is:\n$$U = -\\vec{\\mu} \\cdot \\vec{B} = -\\mu B \\cos\\theta$$\n\n<h4>3. The Moving-Coil Galvanometer</h4>\nIn a d'Arsonval galvanometer, a rectangular coil of $N$ turns is suspended in a cylindrical soft iron core that produces a radial magnetic field ($\\vec{B} \\parallel$ plane of coil always, $\\sin\\theta = 1$).\nDeflecting magnetic torque: $\\tau_d = N I A B$.\nRestoring torsional torque of phosphor-bronze suspension fiber: $\\tau_r = C \\theta$.\nIn equilibrium ($\\tau_d = \\tau_r$):\n$$\\theta = \\left( \\frac{N A B}{C} \\right) I$$\nThe angular deflection is strictly linear with current.\n<ul>\n  <li><strong>Current Sensitivity ($S_I$):</strong> $S_I = \\frac{\\theta}{I} = \\frac{N A B}{C}$ (rad/A or div/$\\mu$A).</li>\n  <li><strong>Voltage Sensitivity ($S_V$):</strong> $S_V = \\frac{\\theta}{V} = \\frac{N A B}{C R_g}$ (rad/V).</li>\n</ul>"
        },
        {
          "id": "sec-5-3",
          "number": "\u00a75.3",
          "heading": "The Hall Effect and Galvanomagnetic Measurement",
          "simulation": "lorentz-hall-sim",
          "content": "Edwin Herbert Hall (1879) discovered that when a magnetic field is applied perpendicular to a current-carrying conducting strip, a transverse potential difference develops across the strip.\n\n<h4>1. Physical Mechanism of the Hall Effect</h4>\nConsider a flat conducting slab of width $w$ and thickness $t$ carrying current $I$ along $+x$.\nA uniform magnetic field $\\vec{B} = B \\hat{k}$ is applied along $+z$.\n<ol>\n  <li>Charge carriers moving with drift velocity $\\vec{v}_d$ experience transverse Lorentz magnetic force:\n  $$\\vec{F}_B = q (\\vec{v}_d \\times \\vec{B})$$</li>\n  <li>If charge carriers are **negative electrons** ($q = -e, \\vec{v}_d = -v_d \\hat{i}$):\n  $$\\vec{F}_B = (-e) [(-v_d \\hat{i}) \\times (B \\hat{k})] = -e v_d B \\hat{j}$$\n  Electrons are deflected toward the bottom edge, charging it negative and leaving the top edge positive.</li>\n  <li>If charge carriers are **positive holes** ($q = +e, \\vec{v}_d = +v_d \\hat{i}$):\n  $$\\vec{F}_B = (+e) [(+v_d \\hat{i}) \\times (B \\hat{k})] = -e v_d B \\hat{j}$$\n  Positive charges also deflect downward, charging the bottom edge positive!</li>\n</ol>\n<em>Sign of Carriers:</em> The polarity of the transverse **Hall Voltage ($V_H$)** immediately reveals the sign of the charge carriers (confirming that metals conduct via negative electrons, while p-type semiconductors conduct via positive holes).\n\n<h4>2. Derivation of the Hall Voltage and Hall Coefficient</h4>\nAccumulating transverse charge creates a transverse Hall electric field $\\vec{E}_H$ pointing toward the negative edge.\nAt steady state, the electrostatic force balances the magnetic force:\n$$q E_H = q v_d B \\implies E_H = v_d B$$\nThe measured transverse potential difference is:\n$$V_H = E_H w = v_d B w$$\nUsing $I = n q A v_d = n q (w t) v_d \\implies v_d = \\frac{I}{n q w t}$:\n$$V_H = \\left( \\frac{I}{n q w t} \\right) B w = \\frac{I B}{n q t}$$\nWe define the <strong>Hall Coefficient ($R_H$)</strong>:\n$$R_H = \\frac{E_H}{J B} = \\frac{1}{n q}$$\n$$V_H = R_H \\frac{I B}{t}$$\nApplications: Hall effect sensors measure magnetic fields non-invasively (Gaussmeters), sense motor rotor position in brushless DC motors, and quantify carrier density $n$ in semiconductor wafer fabrication."
        },
        {
          "id": "sec-5-4",
          "number": "\u00a75.4",
          "heading": "The Biot-Savart Law and Magnetic Fields of Current Geometries",
          "simulation": "biot-savart-sim",
          "content": "Jean-Baptiste Biot and F\u00e9lix Savart (1820) established the differential law governing the magnetic field generated by an infinitesimal current element.\n\n<h4>1. The Biot-Savart Law</h4>\nThe magnetic induction $d\\vec{B}$ at field point $P$ due to a differential current element $I d\\vec{l}$ at source position $\\vec{r}'$ is:\n$$d\\vec{B} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times \\hat{r}}{r^2} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times (\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3}$$\nwhere $\\mu_0$ is the <strong>permeability of free space</strong>:\n$$\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A (exact by historical definition)} \\approx 1.2566 \\times 10^{-6} \\text{ H/m}$$\nFor any closed circuit loop $C$:\n$$\\vec{B}(\\vec{r}) = \\frac{\\mu_0 I}{4\\pi} \\oint_C \\frac{d\\vec{l}' \\times (\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3}$$\n\n<h4>2. Magnetic Field of a Long Straight Conductor</h4>\nIntegrating along an infinite straight wire carrying current $I$:\nAt perpendicular distance $R$:\n$$B = \\frac{\\mu_0 I}{4\\pi} \\int_{-\\infty}^\\infty \\frac{dx \\sin\\theta}{r^2} = \\frac{\\mu_0 I}{2\\pi R}$$\nField lines form concentric circles centered on the wire.\n\n<h4>3. Magnetic Field on the Axis of a Circular Current Loop</h4>\nConsider a circular wire loop of radius $R$ carrying current $I$ lying in the yz-plane.\nAt axial distance $x$ along the symmetry axis:\nBy symmetry, components perpendicular to the axis cancel. The axial component is:\n$$B_x = \\int dB \\sin\\alpha = \\frac{\\mu_0 I}{4\\pi (x^2 + R^2)} (2\\pi R) \\left( \\frac{R}{\\sqrt{x^2 + R^2}} \\right)$$\n$$B(x) = \\frac{\\mu_0 I R^2}{2(x^2 + R^2)^{3/2}}$$\n<ul>\n  <li>At the center of the loop ($x = 0$):\n  $$B(0) = \\frac{\\mu_0 I}{2R}$$</li>\n  <li>Far from the loop ($x \\gg R$): using dipole moment $\\mu = I A = I (\\pi R^2)$:\n  $$B(x) \\approx \\frac{\\mu_0 \\mu}{2\\pi x^3}$$\n  Decays as $1/x^3$, identical to an electric dipole.</li>\n</ul>\n\n<h4>4. Helmholtz Coils</h4>\nA pair of identical coaxial coils of radius $R$, separated by distance equal to their radius ($d = R$), carrying identical current $I$ in the same direction.\nAt the midpoint $x = R/2$:\n$$\\frac{dB}{dx} = 0, \\quad \\frac{d^2 B}{dx^2} = 0$$\nThe second derivative vanishes, producing an exceptionally uniform magnetic field over a wide central volume."
        },
        {
          "id": "sec-5-5",
          "number": "\u00a75.5",
          "heading": "Ampere's Circuital Law, Solenoids, and Toroids",
          "simulation": "biot-savart-sim",
          "content": "Andr\u00e9-Marie Amp\u00e8re (1826) formulated Ampere's circuital law, the magnetic analog of Gauss's law for high-symmetry current distributions.\n\n<h4>1. Ampere's Circuital Law</h4>\nThe line integral of magnetic field $\\vec{B}$ around any closed Amperian loop $C$ equals $\\mu_0$ times the total net electric current enclosed by the loop:\n$$\\oint_C \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enclosed}}$$\nIn differential form (applying Stokes' Theorem):\n$$\\nabla \\times \\vec{B} = \\mu_0 \\vec{J}$$\n\n<h4>2. The Ideal Long Solenoid</h4>\nA helical coil of length $L$ and $N$ closely spaced turns carrying current $I$ ($n = N/L$ turns per unit meter).\nInside an infinitely long solenoid, the magnetic field is uniform and parallel to the axis; outside, it is zero.\nConstruct a rectangular Amperian loop of length $h$ with one side inside and one outside:\n$$\\oint_C \\vec{B} \\cdot d\\vec{l} = B h + 0 + 0 + 0 = B h$$\nEnclosed current: $I_{\\text{encl}} = n h I$.\n$$B h = \\mu_0 (n h I) \\implies B = \\mu_0 n I$$\nThe field depends exclusively on turn density $n$ and current $I$, independent of solenoid cross-sectional diameter or position.\n\n<h4>3. The Toroid (Toroidal Solenoid)</h4>\nA solenoid bent into a closed donut-shaped ring of inner radius $a$ and outer radius $b$ with $N$ total turns.\nConstruct a circular Amperian loop of radius $r$ inside the core ($a < r < b$):\n$$\\oint \\vec{B} \\cdot d\\vec{l} = B (2\\pi r) = \\mu_0 (N I) \\implies B(r) = \\frac{\\mu_0 N I}{2\\pi r}$$\nOutside the toroid ($r < a$ or $r > b$), enclosed current is zero, so $\\vec{B} = 0$ everywhere. Toroids have zero external magnetic leakage."
        }
      ],
      "problems": [
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
              "explanation": "Carrier density in this doped semiconductor is $1.35 \\times 10^{22}$ m\u207b\u00b3."
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
              "explanation": "The field drops to one-eighth of its peak value at $x = R\\sqrt{3} = 17.3$ cm."
            },
            {
              "title": "Step 3: Magnetic dipole moment",
              "math": "$$\\mu = N I A = N I (\\pi R^2) = 250 \\times 2.40 \\times \\pi (0.100)^2$$\n$$\\mu = 600 \\times \\pi \\times 0.0100 = 6.00 \\pi = 18.85 \\text{ A}\\cdot\\text{m}^2 = 18.85 \\text{ J/T}$$",
              "explanation": "The magnetic dipole moment of the coil is 18.85 A\u00b7m\u00b2."
            }
          ]
        }
      ]
    },
    {
      "number": 6,
      "title": "Electromagnetic Induction and Inductance",
      "leadSummary": "Faraday's law of induction, Lenz's law and energy conservation, motional EMF, eddy currents and magnetic damping, self-inductance of solenoids and toroids, mutual inductance and coupling coefficient, LR circuit growth and decay transients, and magnetic field energy storage.",
      "sections": [
        {
          "id": "sec-6-1",
          "number": "\u00a76.1",
          "heading": "Faraday's Law of Induction and Lenz's Law",
          "simulation": "faraday-induction-sim",
          "content": "Michael Faraday (1831) made the epochal discovery that a changing magnetic flux induces an electromotive force in an electric circuit.\n\n<h4>1. Magnetic Flux</h4>\nThe <strong>magnetic flux</strong> $\\Phi_B$ through an oriented surface $S$ is defined as:\n$$\\Phi_B = \\int_S \\vec{B} \\cdot d\\vec{A}$$\nSI Unit: **Weber (Wb)** ($1 \\text{ Weber} = 1 \\text{ T}\\cdot\\text{m}^2 = 1 \\text{ Volt}\\cdot\\text{second}$).\n\n<h4>2. Faraday's Law of Induction</h4>\nThe induced electromotive force $\\mathcal{E}$ in a closed conducting loop is directly proportional to the negative time rate of change of magnetic flux through the loop:\n$$\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$$\nFor a closely wound coil of $N$ identical turns:\n$$\\mathcal{E} = -N \\frac{d\\Phi_B}{dt}$$\n\n<h4>3. Lenz's Law and Conservation of Energy</h4>\nHeinrich Lenz (1834) established the physical origin of the negative sign:\n<blockquote>\nThe polarity of the induced electromotive force is always such that any induced current establishes a magnetic field that opposes the original change in magnetic flux that produced it.\n</blockquote>\n<em>Proof by Conservation of Energy:</em>\nIf the induced current reinforced the flux change instead of opposing it, a minuscule initial flux increase would induce current creating more flux, accelerating indefinitely without external energy input\u2014a perpetual motion machine.\nBecause Lenz's law dictates opposition, an external mechanical agent must perform work against magnetic retarding forces to move a magnet or conductor, and this mechanical work is transformed into electrical energy.\n\n<h4>4. Differential Form of Faraday's Law</h4>\nSince $\\mathcal{E} = \\oint_C \\vec{E} \\cdot d\\vec{l}$:\n$$\\oint_C \\vec{E} \\cdot d\\vec{l} = -\\frac{d}{dt} \\int_S \\vec{B} \\cdot d\\vec{A} = -\\int_S \\frac{\\partial \\vec{B}}{\\partial t} \\cdot d\\vec{A}$$\nApplying Stokes' Theorem:\n$$\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$$\n<em>Revolutionary Consequence:</em> A time-varying magnetic field creates a non-conservative, non-electrostatic **induced electric field** whose field lines form closed continuous loops ($\\oint \\vec{E} \\cdot d\\vec{l} \ne 0$)!"
        },
        {
          "id": "sec-6-2",
          "number": "\u00a76.2",
          "heading": "Motional EMF, Eddy Currents, and Magnetic Braking",
          "simulation": "faraday-induction-sim",
          "content": "Electromotive force can also arise purely from the physical motion of a conductor through a static magnetic field.\n\n<h4>1. Motional EMF</h4>\nConsider a conducting rod of length $L$ sliding with velocity $\\vec{v}$ along frictionless parallel rails in a uniform magnetic field $\\vec{B}$ perpendicular to the rail plane.\nFree electrons in the rod experience magnetic Lorentz force:\n$$\\vec{F}_m = -e (\\vec{v} \\times \\vec{B})$$\nThis force pushes electrons to one end, creating an internal electrostatic separating field $\\vec{E}_{\\text{ind}}$:\n$$\\mathcal{E} = \\int_0^L (\\vec{v} \\times \\vec{B}) \\cdot d\\vec{l} = v B L$$\nAlternatively, via Faraday's flux rule:\n$$\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -\\frac{d}{dt}(B L x) = -B L \\frac{dx}{dt} = -B L v$$\nIf the rails are connected to an external load resistor $R$, induced current is $I = \\mathcal{E}/R = BLv/R$.\nThe current-carrying rod experiences a retarding magnetic drag force:\n$$F_{\\text{drag}} = I L B = \\frac{B^2 L^2 v}{R}$$\nThe mechanical power required to pull the rod equals the electrical power dissipated as Joule heat:\n$$P_{\\text{mech}} = F_{\\text{drag}} v = \\frac{B^2 L^2 v^2}{R} = I^2 R = P_{\\text{elec}}$$\n\n<h4>2. Eddy Currents and Induction Heating</h4>\nWhen a solid metallic block moves through a localized magnetic field, circulating loops of induced current termed **eddy currents (Foucault currents)** are set up within the bulk metal:\n<ul>\n  <li><strong>Magnetic Braking:</strong> By Lenz's law, eddy currents oppose the relative motion, generating smooth, wear-free braking forces (used in high-speed bullet trains and rollercoasters).</li>\n  <li><strong>Lamination of Transformer Cores:</strong> Eddy currents cause severe $I^2 R$ energy losses. Transformer cores are assembled from thin, insulated silicon-steel laminations to interrupt eddy current loops, slashing core losses by over 95%.</li>\n</ul>"
        },
        {
          "id": "sec-6-3",
          "number": "\u00a76.3",
          "heading": "Self-Inductance, Mutual Inductance, and Inductive Coupling",
          "simulation": "faraday-induction-sim",
          "content": "When the current through a circuit changes, its own magnetic flux varies, inducing a back EMF in the circuit itself\u2014a phenomenon termed self-induction.\n\n<h4>1. Self-Inductance ($L$)</h4>\nThe magnetic flux linkage $N\\Phi_B$ through a circuit carrying current $I$ is directly proportional to $I$:\n$$N \\Phi_B = L I \\implies L = \\frac{N \\Phi_B}{I}$$\nThe constant of proportionality $L$ is the <strong>Self-Inductance</strong>.\nSI Unit: **Henry (H)** ($1 \\text{ Henry} = 1 \\text{ Wb/A} = 1 \\text{ V}\\cdot\\text{s/A}$).\nBy Faraday's law, the **self-induced back EMF** is:\n$$\\mathcal{E}_L = -N \\frac{d\\Phi_B}{dt} = -L \\frac{dI}{dt}$$\nInductance represents the electrical inertia of a circuit; it opposes any change in current.\n\n<h4>2. Self-Inductance of an Ideal Solenoid</h4>\nFor a long solenoid of length $l$, cross-sectional area $A$, and $N$ total turns ($n = N/l$):\n$$B = \\mu_0 n I = \\mu_0 \\left(\\frac{N}{l}\\right) I$$\n$$\\Phi_B = B A = \\mu_0 \\left(\\frac{N}{l}\\right) A I$$\n$$L = \\frac{N \\Phi_B}{I} = \\frac{N [\\mu_0 (N/l) A I]}{I} = \\mu_0 \\frac{N^2 A}{l} = \\mu_0 n^2 A l = \\mu_0 n^2 \\cdot (\\text{Volume})$$\nInductance scales with the square of the turn count ($L \\propto N^2$).\nIf the core is filled with ferromagnetic material of relative permeability $\\mu_r$: $L = \\mu_0 \\mu_r n^2 A l$.\n\n<h4>3. Mutual Inductance ($M$) and Coupling Coefficient</h4>\nWhen two coils 1 and 2 are in proximity, changing current $I_1$ in coil 1 produces changing flux $\\Phi_{21}$ through coil 2:\n$$\\mathcal{E}_2 = -M_{21} \\frac{dI_1}{dt}, \\quad \\mathcal{E}_1 = -M_{12} \\frac{dI_2}{dt}$$\nBy the Neumann Reciprocity Theorem:\n$$M_{12} = M_{21} = M$$\nThe <strong>magnetic coupling coefficient</strong> $k$ is:\n$$k = \\frac{M}{\\sqrt{L_1 L_2}}, \\quad 0 \\le k \\le 1$$\n$k = 1$ denotes ideal perfect magnetic flux linkage (toroidal transformers)."
        },
        {
          "id": "sec-6-4",
          "number": "\u00a76.4",
          "heading": "LR Circuit Transients and Magnetic Field Energy Storage",
          "simulation": "faraday-induction-sim",
          "content": "In circuits containing resistors and inductors, the back EMF prevents instantaneous changes in current.\n\n<h4>1. Growth of Current in a Series LR Circuit</h4>\nA battery $\\mathcal{E}$, resistor $R$, and inductor $L$ are connected in series; switch closed at $t = 0$.\nKVL:\n$$\\mathcal{E} - i R - L \\frac{di}{dt} = 0 \\implies L \\frac{di}{dt} + R i = \\mathcal{E}$$\nSolving with initial condition $i(0) = 0$:\n$$i(t) = \\frac{\\mathcal{E}}{R} \\left( 1 - e^{-t/\\tau_L} \\right) = I_0 \\left( 1 - e^{-t/\\tau_L} \\right)$$\nwhere $\\tau_L = \\frac{L}{R}$ is the <strong>inductive time constant</strong> (Units: seconds, $\\text{H}/\\Omega = \\text{s}$).\n<ul>\n  <li>At $t = 0$: $i = 0$, back EMF is maximum ($\\mathcal{E}_L = -\\mathcal{E}$). The inductor acts as an open circuit.</li>\n  <li>At $t = \\tau_L$: Current reaches $(1 - 1/e) \\approx 63.2\\%$ of $I_0$.</li>\n  <li>At $t \\to \\infty$: $di/dt \\to 0$, $i \\to I_0 = \\mathcal{E}/R$. The inductor acts as an ideal zero-resistance short circuit.</li>\n</ul>\n\n<h4>2. Decay of Current in an LR Circuit</h4>\nWhen the battery is switched out:\n$$L \\frac{di}{dt} + R i = 0 \\implies i(t) = I_0 e^{-t/\\tau_L}$$\n\n<h4>3. Energy Stored in a Magnetic Field</h4>\nTo establish current $I$ against the opposing back EMF, the source must perform work:\n$$dW = P dt = (-\\mathcal{E}_L) i \\, dt = \\left( L \\frac{di}{dt} \\right) i \\, dt = L i \\, di$$\nIntegrating from $i = 0$ to $i = I$:\n$$U_B = \\int_0^I L i \\, di = \\frac{1}{2} L I^2$$\nFor a long solenoid where $L = \\mu_0 n^2 A l$ and $B = \\mu_0 n I \\implies I = B / (\\mu_0 n)$:\n$$U_B = \\frac{1}{2} (\\mu_0 n^2 A l) \\left( \\frac{B}{\\mu_0 n} \\right)^2 = \\frac{B^2}{2\\mu_0} (A l)$$\nBecause $Al$ is the enclosed core volume, the <strong>magnetic energy density</strong> $u_B$ (J/m\u00b3) is:\n$$u_B = \\frac{B^2}{2\\mu_0} = \\frac{1}{2} \\vec{B} \\cdot \\vec{H}$$\nAnalogous to $u_E = \\frac{1}{2}\\epsilon_0 E^2$, magnetic energy is localized continuously throughout the space occupied by the magnetic field!"
        }
      ],
      "problems": [
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
              "explanation": "Because energy scales as $i^2$, current must reach $1/\\sqrt{2} \\approx 70.7\\%$ of maximum, requiring 61.4 ms."
            }
          ]
        }
      ]
    },
    {
      "number": 7,
      "title": "Alternating Current",
      "leadSummary": "AC generator dynamics, RMS and average effective values, response of pure resistive, inductive, and capacitive elements, phasor analysis and complex impedance, series LCR circuits, resonance sharpness and Quality factor, real and reactive power, power factor correction, and transformer physics.",
      "sections": [
        {
          "id": "sec-7-1",
          "number": "\u00a77.1",
          "heading": "AC Generator Principles and Mathematical Representation of Sinusoids",
          "simulation": "ac-rlc-resonance-sim",
          "content": "Alternating Current (AC) is electric current whose magnitude and direction reverse periodically in time according to a sinusoidal function.\n\n<h4>1. The Simple AC Generator (Alternator)</h4>\nConsider a planar rectangular armature coil of $N$ turns and area $A$ rotated with constant angular velocity $\\omega$ in a uniform magnetic field $\\vec{B}$.\nThe instantaneous angle between the coil normal and the field is $\\theta(t) = \\omega t$.\nThe magnetic flux through the coil is:\n$$\\Phi_B(t) = B A \\cos(\\omega t)$$\nBy Faraday's law of electromagnetic induction, the induced EMF is:\n$$\\mathcal{E}(t) = -N \\frac{d\\Phi_B}{dt} = -N B A \\frac{d}{dt}[\\cos(\\omega t)] = N B A \\omega \\sin(\\omega t)$$\n$$\\mathcal{E}(t) = \\mathcal{E}_0 \\sin(\\omega t)$$\nwhere $\\mathcal{E}_0 = N B A \\omega$ is the **peak voltage amplitude** (Volts).\n\n<h4>2. Root-Mean-Square (R.M.S.) and Average Values</h4>\nConsider a sinusoidal voltage $v(t) = V_0 \\sin(\\omega t)$ with period $T = 2\\pi / \\omega$:\n<ul>\n  <li><strong>Full-Cycle Average:</strong>\n  $$\\bar{V} = \\frac{1}{T}\\int_0^T V_0 \\sin(\\omega t) dt = 0$$\n  The average over a complete cycle vanishes because positive and negative half-cycles cancel identically.</li>\n  <li><strong>Half-Cycle Average:</strong>\n  $$\\bar{V}_{1/2} = \\frac{2}{T}\\int_0^{T/2} V_0 \\sin(\\omega t) dt = \\frac{2 V_0}{\\pi} \\approx 0.6366 V_0$$</li>\n  <li><strong>Root-Mean-Square (R.M.S. / Effective) Value:</strong>\n  The equivalent DC voltage that produces the identical average heating power in a pure resistor:\n  $$V_{\\text{rms}} = \\sqrt{ \\frac{1}{T}\\int_0^T [V_0 \\sin(\\omega t)]^2 dt } = \\sqrt{ \\frac{V_0^2}{T}\\int_0^T \\left(\\frac{1 - \\cos(2\\omega t)}{2}\\right) dt } = \\frac{V_0}{\\sqrt{2}} \\approx 0.7071 V_0$$\n  $$I_{\\text{rms}} = \\frac{I_0}{\\sqrt{2}} \\approx 0.7071 I_0$$\n  (Standard household mains 230 V or 120 V AC are R.M.S. values; the peak amplitude is $V_0 = 230\\sqrt{2} \\approx 325\\text{ V}$).</li>\n</ul>"
        },
        {
          "id": "sec-7-2",
          "number": "\u00a77.2",
          "heading": "AC Response of Pure Circuit Elements: Resistors, Inductors, and Capacitors",
          "simulation": "ac-rlc-resonance-sim",
          "content": "When sinusoidal voltage $v(t) = V_0 \\sin(\\omega t)$ is applied individually to ideal passive elements, distinct phase relationships emerge.\n\n<h4>1. Pure Resistive Circuit ($R$)</h4>\nApplying Ohm's law:\n$$i_R(t) = \\frac{v(t)}{R} = \\frac{V_0}{R} \\sin(\\omega t) = I_0 \\sin(\\omega t)$$\n<em>Phase:</em> Current and voltage are strictly **in phase** ($\\phi = 0$).\n\n<h4>2. Pure Inductive Circuit ($L$)</h4>\nBy Faraday's law: $v(t) = L \\frac{di}{dt} \\implies di = \\frac{V_0}{L} \\sin(\\omega t) dt$.\nIntegrating:\n$$i_L(t) = -\\frac{V_0}{\\omega L} \\cos(\\omega t) = \\frac{V_0}{\\omega L} \\sin\\left( \\omega t - \\frac{\\pi}{2} \\right) = I_0 \\sin\\left( \\omega t - \\frac{\\pi}{2} \\right)$$\nwhere $X_L = \\omega L = 2\\pi f L$ is the <strong>Inductive Reactance</strong> ($\\Omega$).\n<em>Phase:</em> In an inductor, current **lags voltage by 90\u00b0 ($\\pi/2$ radians)**. An inductor opposes high frequencies ($X_L \\propto f$).\n\n<h4>3. Pure Capacitive Circuit ($C$)</h4>\nBy charge-voltage relation: $q(t) = C v(t) = C V_0 \\sin(\\omega t)$.\nCurrent is $i(t) = \\frac{dq}{dt}$:\n$$i_C(t) = \\omega C V_0 \\cos(\\omega t) = \\frac{V_0}{1/(\\omega C)} \\sin\\left( \\omega t + \\frac{\\pi}{2} \\right) = I_0 \\sin\\left( \\omega t + \\frac{\\pi}{2} \\right)$$\nwhere $X_C = \\frac{1}{\\omega C} = \\frac{1}{2\\pi f C}$ is the <strong>Capacitive Reactance</strong> ($\\Omega$).\n<em>Phase:</em> In a capacitor, current **leads voltage by 90\u00b0 ($\\pi/2$ radians)**. A capacitor blocks DC ($X_C \\to \\infty$ as $f \\to 0$) and passes high frequencies ($X_C \\to 0$).\n<em>Mnemonic:</em> **ELI the ICE man** (in $L$, $E$ leads $I$; in $C$, $I$ leads $E$)."
        },
        {
          "id": "sec-7-3",
          "number": "\u00a77.3",
          "heading": "Series LCR Circuits, Complex Impedance, and Electrical Resonance",
          "simulation": "ac-rlc-resonance-sim",
          "content": "Connecting a resistor, inductor, and capacitor in series across an AC source $v(t) = V_0 \\sin(\\omega t)$ establishes a driven harmonic system.\n\n<h4>1. Phasor Addition and Total Impedance ($Z$)</h4>\nBecause elements are in series, the common current is $i(t) = I_0 \\sin(\\omega t - \\phi)$.\nThe voltage drops across each element are:\n$$V_R = I_0 R, \\quad V_L = I_0 X_L, \\quad V_C = I_0 X_C$$\nOn the phasor plane, $V_L$ leads $I$ by $+90^\\circ$ and $V_C$ lags $I$ by $-90^\\circ$. The net reactive voltage is $V_L - V_C$.\nBy the Pythagorean theorem:\n$$V_0 = \\sqrt{ V_R^2 + (V_L - V_C)^2 } = I_0 \\sqrt{ R^2 + (X_L - X_C)^2 } = I_0 Z$$\nThe <strong>Impedance ($Z$)</strong> of the series LCR circuit is:\n$$Z = \\sqrt{ R^2 + (\\omega L - \\frac{1}{\\omega C})^2 }$$\nThe phase angle $\\phi$ of voltage relative to current is:\n$$\\tan\\phi = \\frac{X_L - X_C}{R} = \\frac{\\omega L - 1/(\\omega C)}{R}$$\n<ul>\n  <li>If $X_L > X_C$: $\\phi > 0$ (circuit is inductive, voltage leads current).</li>\n  <li>If $X_L < X_C$: $\\phi < 0$ (circuit is capacitive, current leads voltage).</li>\n  <li>If $X_L = X_C$: $\\phi = 0$ (circuit is purely resistive).</li>\n</ul>\n\n<h4>2. Series Electrical Resonance</h4>\nWhen the applied frequency makes inductive reactance balance capacitive reactance:\n$$X_L = X_C \\implies \\omega_0 L = \\frac{1}{\\omega_0 C} \\implies \\omega_0 = \\frac{1}{\\sqrt{LC}}, \\quad f_0 = \\frac{1}{2\\pi\\sqrt{LC}}$$\nAt the <strong>resonant frequency $\\omega_0$</strong>:\n<ol>\n  <li>The total impedance drops to its absolute theoretical minimum: $Z_{\\min} = R$.</li>\n  <li>The current reaches its absolute theoretical maximum: $I_{\\max} = V_0 / R$.</li>\n  <li>Current and voltage are perfectly in phase ($\\phi = 0$, power factor $\\cos\\phi = 1$).</li>\n</ol>\n\n<h4>3. Quality Factor ($Q$) and Bandwidth</h4>\nThe Quality Factor $Q$ quantifies the sharpness and selectivity of resonance:\n$$Q = \\frac{\\omega_0 L}{R} = \\frac{1}{\\omega_0 C R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$$\nThe half-power bandwidth is $\\Delta\\omega = \\omega_2 - \\omega_1 = \\frac{R}{L} = \\frac{\\omega_0}{Q}$.\nHigh $Q$ produces extreme selectivity, essential for radio tuning circuits."
        },
        {
          "id": "sec-7-4",
          "number": "\u00a77.4",
          "heading": "Power Dissipation in AC Circuits and Ideal Transformers",
          "simulation": "ac-rlc-resonance-sim",
          "content": "Unlike DC circuits where power is simply $P = V I$, AC power calculations must account for the phase angle between voltage and current.\n\n<h4>1. Instantaneous and Real Average Power</h4>\nLet $v(t) = V_0 \\sin(\\omega t)$ and $i(t) = I_0 \\sin(\\omega t - \\phi)$.\nThe instantaneous power is:\n$$p(t) = v(t) i(t) = V_0 I_0 \\sin(\\omega t) [\\sin(\\omega t)\\cos\\phi - \\cos(\\omega t)\\sin\\phi]$$\n$$p(t) = V_0 I_0 \\sin^2(\\omega t)\\cos\\phi - \\frac{1}{2} V_0 I_0 \\sin(2\\omega t)\\sin\\phi$$\nAveraging over a complete cycle ($\\langle \\sin^2\\omega t \\rangle = 1/2$, $\\langle \\sin 2\\omega t \\rangle = 0$):\n$$\\langle P \\rangle = \\frac{1}{2} V_0 I_0 \\cos\\phi = \\left(\\frac{V_0}{\\sqrt{2}}\\right) \\left(\\frac{I_0}{\\sqrt{2}}\\right) \\cos\\phi$$\n$$\\langle P \\rangle = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi$$\nwhere:\n<ul>\n  <li>$P$: <strong>Real (Active) Power</strong> dissipated as heat or mechanical work (Watts, W). Pure inductors and capacitors consume zero average real power!</li>\n  <li>$S = V_{\\text{rms}} I_{\\text{rms}}$: <strong>Apparent Power</strong> (Volt-Amperes, VA).</li>\n  <li>$Q_{\\text{react}} = V_{\\text{rms}} I_{\\text{rms}} \\sin\\phi$: <strong>Reactive Power</strong> surging back and forth between source and reactive fields (Volt-Amperes Reactive, VAR).</li>\n  <li>$\\cos\\phi = \\frac{R}{Z}$: <strong>Power Factor</strong> ($0 \\le \\cos\\phi \\le 1$). Power companies mandate $\\cos\\phi \\ge 0.95$ using power factor correction capacitors to minimize transmission line $I^2 R$ heat losses.</li>\n</ul>\n\n<h4>2. The Ideal Transformer</h4>\nA transformer consists of two coils (primary of $N_p$ turns and secondary of $N_s$ turns) wound around a common laminated ferromagnetic core.\nAssuming zero flux leakage ($k = 1$) and zero resistance:\n$$\\mathcal{E}_p = -N_p \\frac{d\\Phi_B}{dt}, \\quad \\mathcal{E}_s = -N_s \\frac{d\\Phi_B}{dt}$$\nDividing:\n$$\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = a \\quad (\\text{Transformation Ratio})$$\nBy energy conservation ($P_{\\text{in}} = P_{\\text{out}} \\implies V_p I_p = V_s I_s$):\n$$\\frac{I_p}{I_s} = \\frac{V_s}{V_p} = \\frac{N_s}{N_p} = a \\implies I_s = \\frac{I_p}{a}$$\nImpedance reflection: A load $R_L$ connected across the secondary reflects back to the primary as an equivalent impedance:\n$$R_{\\text{in}} = \\frac{V_p}{I_p} = \\frac{V_s / a}{a I_s} = \\frac{1}{a^2}\\left(\\frac{V_s}{I_s}\\right) = \\frac{R_L}{a^2} = \\left(\\frac{N_p}{N_s}\\right)^2 R_L$$\nThis principle allows audio and RF engineers to achieve impedance matching for maximum power transfer."
        }
      ],
      "problems": [
        {
          "id": "prob-7-1",
          "difficulty": "Undergraduate Standard Classical Exam",
          "title": "Series LCR Resonance and Resonance Magnification",
          "question": "A series LCR circuit has resistance $R = 8.00\\ \\Omega$, inductance $L = 40.0\\text{ mH}$, and capacitance $C = 2.50\\ \\mu\\text{F}$. It is driven by an AC voltage source of amplitude $V_0 = 120.0\\text{ V}$ with variable angular frequency $\\omega$.\\n(a) Determine the resonant angular frequency $\\omega_0$ and linear frequency $f_0$,\\n(b) Calculate the Quality Factor $Q$ and half-power bandwidth $\\Delta f$, and\\n(c) At resonance, compute the peak current $I_0$ and the peak voltages across the inductor ($V_{L0}$) and capacitor ($V_{C0}$).",
          "steps": [
            {
              "title": "Step 1: Compute resonance frequency",
              "math": "$$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{(40.0 \\times 10^{-3} \\text{ H}) \\times (2.50 \\times 10^{-6} \\text{ F})}} = \\frac{1}{\\sqrt{1.000 \\times 10^{-7}}} = \\frac{1}{3.1623 \\times 10^{-4}}$$\n$$\\omega_0 = 3162.3 \\text{ rad/s}$$\n$$f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{3162.3}{2\\pi} = 503.3 \\text{ Hz}$$",
              "explanation": "The circuit resonates at 3162 rad/s (503.3 Hz)."
            },
            {
              "title": "Step 2: Calculate Quality Factor and bandwidth",
              "math": "$$Q = \\frac{\\omega_0 L}{R} = \\frac{(3162.3 \\text{ rad/s}) \\times (0.0400 \\text{ H})}{8.00\\ \\Omega} = \\frac{126.49}{8.00} = 15.81$$\n$$\\Delta f = \\frac{f_0}{Q} = \\frac{503.3 \\text{ Hz}}{15.81} = 31.83 \\text{ Hz}$$",
              "explanation": "A high Quality Factor of 15.8 corresponds to a narrow, sharp resonance bandwidth of 31.8 Hz."
            },
            {
              "title": "Step 3: Current and voltages at resonance",
              "math": "$$\\text{At resonance, } Z = R = 8.00\\ \\Omega:$$\n$$I_0 = \\frac{V_0}{R} = \\frac{120.0 \\text{ V}}{8.00\\ \\Omega} = 15.00 \\text{ A}$$\n$$X_{L0} = \\omega_0 L = 3162.3 \\times 0.0400 = 126.49\\ \\Omega$$\n$$V_{L0} = I_0 X_{L0} = 15.00 \\times 126.49 = 1897.4 \\text{ Volts}$$\n$$V_{C0} = I_0 X_{C0} = 1897.4 \\text{ Volts}$$\n$$\\frac{V_{L0}}{V_0} = \\frac{1897.4}{120.0} = 15.81 = Q$$",
              "explanation": "Notice the dramatic resonance voltage magnification: the inductor and capacitor each sustain 1.90 kV (nearly 16 times the 120 V supply voltage!)."
            }
          ]
        },
        {
          "id": "prob-7-2",
          "difficulty": "Industrial AC Engineering Problem",
          "title": "AC Power Factor Correction with Shunt Capacitance",
          "question": "A small factory operating on a $V_{\\text{rms}} = 240\\text{ V}$, $f = 50.0\\text{ Hz}$ single-phase AC supply draws real power $P = 12.0\\text{ kW}$ at a lagging power factor $\\cos\\phi_1 = 0.650$ due to induction motors.\\n(a) Determine the initial apparent power $S_1$, reactive power $Q_1$, and total line current $I_{\\text{rms,1}}$,\\n(b) What reactive power $Q_C$ must be supplied by a shunt power factor correction capacitor to raise the overall power factor to $\\cos\\phi_2 = 0.950$ (lagging), and\\n(c) Calculate the required capacitance $C$ of the capacitor and the reduction in supply line current.",
          "steps": [
            {
              "title": "Step 1: Compute initial uncompensated parameters",
              "math": "$$\\cos\\phi_1 = 0.650 \\implies \\phi_1 = \\arccos(0.650) = 49.458^\\circ, \\quad \\tan\\phi_1 = 1.1691$$\n$$S_1 = \\frac{P}{\\cos\\phi_1} = \\frac{12.0 \\text{ kW}}{0.650} = 18.462 \\text{ kVA}$$\n$$I_{\\text{rms,1}} = \\frac{S_1}{V_{\\text{rms}}} = \\frac{18462 \\text{ VA}}{240 \\text{ V}} = 76.92 \\text{ A}$$\n$$Q_1 = P \\tan\\phi_1 = 12.0 \\times 1.1691 = 14.029 \\text{ kVAR}$$",
              "explanation": "The motors draw 76.9 A of line current and 14.0 kVAR of lagging reactive power."
            },
            {
              "title": "Step 2: Determine target compensated parameters",
              "math": "$$\\cos\\phi_2 = 0.950 \\implies \\phi_2 = \\arccos(0.950) = 18.195^\\circ, \\quad \\tan\\phi_2 = 0.3287$$\n$$Q_2 = P \\tan\\phi_2 = 12.0 \\times 0.3287 = 3.944 \\text{ kVAR}$$\n$$Q_C = Q_1 - Q_2 = 14.029 - 3.944 = 10.085 \\text{ kVAR}$$",
              "explanation": "The capacitor must inject 10.09 kVAR of leading reactive power."
            },
            {
              "title": "Step 3: Calculate required capacitance and new line current",
              "math": "$$Q_C = V_{\\text{rms}}^2 \\omega C = V_{\\text{rms}}^2 (2\\pi f) C$$\n$$C = \\frac{Q_C}{2\\pi f V_{\\text{rms}}^2} = \\frac{10085 \\text{ VAR}}{2\\pi \\times 50.0 \\times (240)^2} = \\frac{10085}{314.16 \\times 57600} = \\frac{10085}{1.80956 \\times 10^7} = 5.573 \\times 10^{-4} \\text{ F} = 557 \\ \\mu\\text{F}$$\n$$I_{\\text{rms,2}} = \\frac{P}{V_{\\text{rms}} \\cos\\phi_2} = \\frac{12000}{240 \\times 0.950} = \\frac{12000}{228} = 52.63 \\text{ A}$$\n$$\\Delta I = 76.92 - 52.63 = 24.29 \\text{ A (31.6\\% line current reduction)}$$",
              "explanation": "Installing a 557 microfarad capacitor slashes supply current by 24.3 A, reducing cable $I^2 R$ heat losses by 53%."
            }
          ]
        },
        {
          "id": "prob-7-3",
          "difficulty": "Standard University Exam Problem",
          "title": "Step-Down Transformer Efficiency and Reflected Impedance",
          "question": "A step-down power distribution transformer has $N_p = 2400$ primary turns and $N_s = 200$ secondary turns. The primary connects to an AC line of $V_p = 2400\\text{ V}$ (RMS) at $50\\text{ Hz}$. The secondary delivers electrical power to a resistive heating load $R_L = 4.00\\ \\Omega$. Assume an ideal transformer with zero losses.\\n(a) Determine the secondary voltage $V_s$ and secondary load current $I_s$,\\n(b) Find the primary current $I_p$ and total power delivered, and\\n(c) Calculate the equivalent reflected load impedance $R_{\\text{in}}$ seen by the primary supply line.",
          "steps": [
            {
              "title": "Step 1: Compute secondary voltage and current",
              "math": "$$\\text{Turns ratio: } a = \\frac{N_s}{N_p} = \\frac{200}{2400} = \\frac{1}{12}$$\n$$V_s = a V_p = \\frac{1}{12} \\times 2400 \\text{ V} = 200.0 \\text{ Volts}$$\n$$I_s = \\frac{V_s}{R_L} = \\frac{200.0 \\text{ V}}{4.00\\ \\Omega} = 50.00 \\text{ Amperes}$$",
              "explanation": "The transformer steps down the 2400 V primary voltage to 200 V, delivering 50 A."
            },
            {
              "title": "Step 2: Primary current and delivered power",
              "math": "$$I_p = a I_s = \\left(\\frac{1}{12}\\right) \\times 50.00 \\text{ A} = 4.167 \\text{ Amperes}$$\n$$P = V_s I_s = 200.0 \\text{ V} \\times 50.00 \\text{ A} = 10000 \\text{ Watts} = 10.0 \\text{ kW}$$\n$$P_{\\text{primary}} = V_p I_p = 2400 \\text{ V} \\times 4.167 \\text{ A} = 10000 \\text{ Watts}$$",
              "explanation": "Primary draw is only 4.17 A while delivering 10.0 kW of power."
            },
            {
              "title": "Step 3: Reflected input impedance",
              "math": "$$R_{\\text{in}} = \\frac{V_p}{I_p} = \\frac{2400 \\text{ V}}{4.167 \\text{ A}} = 576.0\\ \\Omega$$\n$$\\text{Check via formula: } R_{\\text{in}} = \\left(\\frac{N_p}{N_s}\\right)^2 R_L = (12)^2 \\times 4.00 = 144 \\times 4.00 = 576.0\\ \\Omega$$\n$$\\text{Q.E.D.}$$",
              "explanation": "The 4-ohm secondary resistor is reflected into the primary circuit as an equivalent 576-ohm load."
            }
          ]
        }
      ]
    },
    {
      "number": 8,
      "title": "Circuit Analysis & Network Theorems",
      "leadSummary": "Comprehensive network analysis methods: Thevenin's theorem and equivalent voltage generators, Norton's theorem and dual current generators, the Superposition theorem, Maximum Power Transfer theorem with impedance matching proofs, and second-order RLC transient dynamics (underdamped, critically damped, overdamped).",
      "sections": [
        {
          "id": "sec-8-1",
          "number": "\u00a78.1",
          "heading": "Thevenin's Theorem and Equivalent Voltage Generators",
          "simulation": "thevenin-norton-sim",
          "content": "L\u00e9on Charles Th\u00e9venin (1883) formulated one of the most powerful network reduction theorems in electrical engineering.\n\n<h4>1. Statement of Thevenin's Theorem</h4>\n<blockquote>\nAny linear, bilateral, two-terminal electrical network containing independent voltage sources, current sources, and linear resistors can be replaced, across its two open terminals $A$ and $B$, by an equivalent circuit consisting of a single ideal voltage source $V_{\\text{th}}$ in series with a single internal resistance $R_{\\text{th}}$.\n</blockquote>\n\n<h4>2. Determination of Thevenin Parameters</h4>\n<ol>\n  <li><strong>Thevenin Equivalent Voltage ($V_{\\text{th}}$):</strong>\n  The open-circuit potential difference appearing across terminals $A$ and $B$ when the load resistor $R_L$ is completely disconnected:\n  $$V_{\\text{th}} = V_{AB,\\text{open}}$$</li>\n  <li><strong>Thevenin Equivalent Resistance ($R_{\\text{th}}$):</strong>\n  The equivalent resistance measured between terminals $A$ and $B$ with the load removed and all independent energy sources **deactivated**:\n  <ul>\n    <li>Independent voltage sources are replaced by **short circuits** (zero internal resistance, $V = 0$).</li>\n    <li>Independent current sources are replaced by **open circuits** (infinite internal resistance, $I = 0$).</li>\n  </ul>\n  $$R_{\\text{th}} = R_{AB,\\text{deactivated}}$$</li>\n</ol>\n\n<h4>3. Calculation of Load Current and Voltage</h4>\nWhen an arbitrary load resistance $R_L$ is connected across terminals $A$ and $B$, the load current $I_L$ and terminal voltage $V_L$ are given instantly by Ohm's law:\n$$I_L = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L}, \\quad V_L = I_L R_L = V_{\\text{th}} \\left( \\frac{R_L}{R_{\\text{th}} + R_L} \\right)$$\nThis eliminates the need to resolve the entire multi-loop system every time the load resistor changes."
        },
        {
          "id": "sec-8-2",
          "number": "\u00a78.2",
          "heading": "Norton's Theorem and Source Transformations",
          "simulation": "thevenin-norton-sim",
          "content": "Edward Lawry Norton (1926) independently established the dual current-source counterpart to Thevenin's theorem.\n\n<h4>1. Statement of Norton's Theorem</h4>\n<blockquote>\nAny linear, bilateral, two-terminal electrical network can be replaced across its terminals by an equivalent circuit consisting of a single ideal current source $I_N$ connected in parallel with a single internal resistance $R_N$.\n</blockquote>\n\n<h4>2. Determination of Norton Parameters</h4>\n<ol>\n  <li><strong>Norton Equivalent Current ($I_N$):</strong>\n  The short-circuit current that flows between terminals $A$ and $B$ when a zero-resistance conductor connects them:\n  $$I_N = I_{AB,\\text{short}}$$</li>\n  <li><strong>Norton Resistance ($R_N$):</strong>\n  The equivalent resistance between terminals $A$ and $B$ with all independent sources deactivated.\n  <em>Fundamental Identity:</em>\n  $$R_N = R_{\\text{th}}$$</li>\n</ol>\n\n<h4>3. Thevenin-Norton Source Transformation Equivalence</h4>\nThevenin and Norton circuits are dual mathematical representations of the exact same physical reality:\n$$V_{\\text{th}} = I_N R_{\\text{th}}, \\quad I_N = \\frac{V_{\\text{th}}}{R_{\\text{th}}}$$\nFor load resistor $R_L$:\nBy the current divider rule across parallel resistors $R_N$ and $R_L$:\n$$I_L = I_N \\left( \\frac{R_N}{R_N + R_L} \\right) = \\left( \\frac{V_{\\text{th}}}{R_{\\text{th}}} \\right) \\left( \\frac{R_{\\text{th}}}{R_{\\text{th}} + R_L} \\right) = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L}$$\nBoth theorems yield identical load current and voltage."
        },
        {
          "id": "sec-8-3",
          "number": "\u00a78.3",
          "heading": "The Superposition Theorem and Maximum Power Transfer",
          "simulation": "thevenin-norton-sim",
          "content": "Linear electrical networks obey the fundamental principles of superposition and impedance matching.\n\n<h4>1. The Superposition Theorem</h4>\n<blockquote>\nIn any linear, bilateral electrical network energized by multiple independent sources, the net current or voltage in any branch equals the algebraic sum of the currents or voltages produced by each independent source acting alone, with all other independent sources turned off.\n</blockquote>\n<ul>\n  <li>Turn off independent voltage sources $\\to$ Replace with short circuits.</li>\n  <li>Turn off independent current sources $\\to$ Replace with open circuits.</li>\n</ul>\n<em>Caution:</em> Superposition applies strictly to linear quantities (current and voltage: $I = I_1 + I_2$). It does **NOT** apply directly to power ($P \\propto I^2 \ne I_1^2 + I_2^2$), because power is a quadratic, non-linear function of current!\n\n<h4>2. The Maximum Power Transfer Theorem</h4>\nConsider a linear source characterized by Thevenin equivalent parameters $V_{\\text{th}}$ and $R_{\\text{th}}$ driving an adjustable load resistance $R_L$.\nThe power delivered to the load resistor is:\n$$P_L = I_L^2 R_L = \\left( \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L} \\right)^2 R_L = \\frac{V_{\\text{th}}^2 R_L}{(R_{\\text{th}} + R_L)^2}$$\nTo maximize power with respect to $R_L$, differentiate and set to zero:\n$$\\frac{dP_L}{dR_L} = V_{\\text{th}}^2 \\left[ \\frac{(R_{\\text{th}} + R_L)^2 - 2 R_L (R_{\\text{th}} + R_L)}{(R_{\\text{th}} + R_L)^4} \\right] = 0$$\n$$(R_{\\text{th}} + R_L) - 2 R_L = 0 \\implies R_{\\text{th}} - R_L = 0$$\n$$R_L = R_{\\text{th}}$$\n<em>Theorem:</em> A resistive load absorbs maximum power from a linear network when its resistance equals the Thevenin resistance of the network (**impedance matching**).\nThe maximum power delivered is:\n$$P_{L,\\max} = \\frac{V_{\\text{th}}^2 R_{\\text{th}}}{(2 R_{\\text{th}})^2} = \\frac{V_{\\text{th}}^2}{4 R_{\\text{th}}}$$\n<em>Efficiency at Maximum Power:</em>\n$$\\eta = \\frac{P_{\\text{load}}}{P_{\\text{total}}} = \\frac{I_L^2 R_L}{I_L^2 (R_{\\text{th}} + R_L)} = \\frac{R_L}{2 R_L} = 50.0\\%$$\nWhile essential in communications and weak-signal electronics to extract maximum signal power, maximum power transfer is deliberately avoided in electrical power grid distribution (where engineers aim for $R_L \\gg R_{\\text{th}}$ to achieve $> 98\\%$ transmission efficiency)."
        },
        {
          "id": "sec-8-4",
          "number": "\u00a78.4",
          "heading": "Transient Currents in Second-Order RLC Circuits",
          "simulation": "thevenin-norton-sim",
          "content": "When a circuit contains both inductive storage elements ($L$) and capacitive storage elements ($C$) along with damping resistance ($R$), its dynamic response is governed by a second-order linear differential equation.\n\n<h4>1. The Governing Differential Equation</h4>\nApplying Kirchhoff's voltage law to a series RLC loop discharging from initial charge $Q_0$:\n$$L \\frac{di}{dt} + R i + \\frac{q}{C} = 0$$\nSince $i = \\frac{dq}{dt}$:\n$$L \\frac{d^2 q}{dt^2} + R \\frac{dq}{dt} + \\frac{1}{C} q = 0 \\implies \\frac{d^2 q}{dt^2} + 2\\gamma \\frac{dq}{dt} + \\omega_0^2 q = 0$$\nwhere $\\gamma = \\frac{R}{2L}$ is the damping factor (s\u207b\u00b9) and $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ is the natural undamped frequency.\nAuxiliary equation:\n$$\\lambda^2 + 2\\gamma \\lambda + \\omega_0^2 = 0 \\implies \\lambda = -\\gamma \\pm \\sqrt{\\gamma^2 - \\omega_0^2}$$\n\n<h4>2. The Three Transient Regimes</h4>\n<ol>\n  <li><strong>Underdamped Oscillatory Regime ($R < 2\\sqrt{L/C} \\iff \\gamma < \\omega_0$):</strong>\n  The roots are complex conjugates $\\lambda = -\\gamma \\pm i \\omega_d$, where $\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2}$.\n  $$q(t) = Q_0 e^{-\\gamma t} \\cos(\\omega_d t + \\phi)$$\n  The charge oscillates back and forth between capacitor plates while dying out exponentially.</li>\n  <li><strong>Critically Damped Regime ($R = 2\\sqrt{L/C} \\iff \\gamma = \\omega_0$):</strong>\n  $R_{\\text{crit}} = 2\\sqrt{\\frac{L}{C}}$.\n  $$q(t) = (C_1 + C_2 t) e^{-\\gamma t}$$\n  The capacitor discharges in the shortest possible time without ringing or overshoot.</li>\n  <li><strong>Overdamped Aperiodic Regime ($R > 2\\sqrt{L/C} \\iff \\gamma > \\omega_0$):</strong>\n  Two real negative roots. Non-oscillatory sluggish decay:\n  $$q(t) = C_1 e^{-(\\gamma - \\sqrt{\\gamma^2-\\omega_0^2})t} + C_2 e^{-(\\gamma + \\sqrt{\\gamma^2-\\omega_0^2})t}$$</li>\n</ol>"
        }
      ],
      "problems": [
        {
          "id": "prob-8-1",
          "difficulty": "Undergraduate Standard Classical Exam",
          "title": "Thevenin and Norton Equivalent Circuit of a Bridge T-Network",
          "question": "A linear DC circuit consists of an independent voltage source $\\mathcal{E} = 36.0\\text{ V}$ connected across a resistive T-network: resistor $R_1 = 12.0\\ \\Omega$ in series with the source, a shunt resistor $R_2 = 24.0\\ \\Omega$ across the line, and an output resistor $R_3 = 8.00\\ \\Omega$ leading to output terminals $A$ and $B$. A variable load resistor $R_L$ is connected between $A$ and $B$.\\n(a) Determine the Thevenin equivalent voltage $V_{\\text{th}}$ and Thevenin resistance $R_{\\text{th}}$,\\n(b) Find the Norton equivalent current $I_N$, and\\n(c) Calculate the load current $I_L$ and power dissipated in $R_L$ when $R_L = 16.0\\ \\Omega$.",
          "steps": [
            {
              "title": "Step 1: Determine Thevenin voltage and resistance",
              "math": "$$\\text{Open circuit across A-B: no current flows through } R_3.$$\n$$V_{\\text{th}} = V_{R2} = \\mathcal{E} \\left( \\frac{R_2}{R_1 + R_2} \\right) = 36.0 \\times \\left( \\frac{24.0}{12.0 + 24.0} \\right) = 36.0 \\times \\left(\\frac{24.0}{36.0}\\right) = 24.00 \\text{ Volts}$$\n$$\\text{Deactivate voltage source (short circuit): } R_1 \\text{ is in parallel with } R_2:$$\n$$R_{12} = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{12.0 \\times 24.0}{12.0 + 24.0} = \\frac{288}{36.0} = 8.00\\ \\Omega$$\n$$R_{\\text{th}} = R_{12} + R_3 = 8.00 + 8.00 = 16.00\\ \\Omega$$",
              "explanation": "The entire network simplifies to a 24.0 V voltage source in series with 16.0 ohms."
            },
            {
              "title": "Step 2: Norton equivalent current",
              "math": "$$I_N = \\frac{V_{\\text{th}}}{R_{\\text{th}}} = \\frac{24.00 \\text{ V}}{16.00\\ \\Omega} = 1.500 \\text{ Amperes}$$\n$$R_N = R_{\\text{th}} = 16.00\\ \\Omega$$",
              "explanation": "The Norton equivalent is a 1.50 A current source in parallel with 16.0 ohms."
            },
            {
              "title": "Step 3: Load analysis for RL = 16.0 ohms",
              "math": "$$I_L = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L} = \\frac{24.00 \\text{ V}}{16.00 + 16.00} = \\frac{24.00}{32.00} = 0.750 \\text{ A}$$\n$$P_L = I_L^2 R_L = (0.750 \\text{ A})^2 \\times 16.00\\ \\Omega = 0.5625 \\times 16.00 = 9.00 \\text{ Watts}$$",
              "explanation": "Because $R_L = R_{\\text{th}} = 16\\ \\Omega$, this represents the exact maximum power transfer condition ($P_{\\max} = 9.00$ W)."
            }
          ]
        },
        {
          "id": "prob-8-2",
          "difficulty": "Honors Circuit Analysis Standard",
          "title": "Superposition Theorem with Dual Independent Sources",
          "question": "A linear network contains an independent DC voltage source $\\mathcal{E}_1 = 28.0\\text{ V}$, an independent DC current source $I_s = 3.00\\text{ A}$, and three resistors: $R_1 = 4.00\\ \\Omega$, $R_2 = 6.00\\ \\Omega$, and $R_3 = 12.0\\ \\Omega$. The voltage source is in series with $R_1$. The current source is in parallel with $R_3$. Resistor $R_2$ connects between the common nodes.\\n(a) Use the Superposition Theorem to determine the current $I_2$ through resistor $R_2$ by activating each source individually, and\\n(b) Verify the result using nodal analysis.",
          "steps": [
            {
              "title": "Step 1: Case A - Voltage source alone (Current source opened)",
              "math": "$$\\text{Current source is open circuit. } R_2 \\text{ and } R_3 \\text{ are in series:}$$\n$$R_{23} = R_2 + R_3 = 6.00 + 12.0 = 18.0\\ \\Omega$$\n$$R_{\\text{total}} = R_1 + R_{23} = 4.00 + 18.0 = 22.0\\ \\Omega$$\n$$I_2' = \\frac{\\mathcal{E}_1}{R_{\\text{total}}} = \\frac{28.0 \\text{ V}}{22.0\\ \\Omega} = 1.2727 \\text{ A}$$",
              "explanation": "The voltage source acting alone drives 1.27 A through resistor $R_2$."
            },
            {
              "title": "Step 2: Case B - Current source alone (Voltage source shorted)",
              "math": "$$\\text{Voltage source is shorted to ground. } R_1 \\text{ and } R_2 \\text{ are in series across } R_3:$$\n$$R_{12} = R_1 + R_2 = 4.00 + 6.00 = 10.0\\ \\Omega$$\n$$\\text{By current divider rule, current splitting through the } (R_1+R_2) \\text{ branch:}$$\n$$I_2'' = -I_s \\left( \\frac{R_3}{R_{12} + R_3} \\right) = -3.00 \\times \\left( \\frac{12.0}{10.0 + 12.0} \\right) = -3.00 \\times \\left(\\frac{12.0}{22.0}\\right) = -1.6364 \\text{ A}$$",
              "explanation": "The current source drives 1.64 A in the opposite direction through $R_2$."
            },
            {
              "title": "Step 3: Algebraic superposition sum",
              "math": "$$I_2 = I_2' + I_2'' = 1.2727 - 1.6364 = -0.3636 \\text{ A} = -364 \\text{ mA}$$",
              "explanation": "Superposing the two states yields a net current of 364 mA flowing upward against the voltage source."
            }
          ]
        },
        {
          "id": "prob-8-3",
          "difficulty": "Second-Order RLC Transient Standard Exam",
          "title": "RLC Transient Oscillation and Critical Damping Resistance",
          "question": "A series RLC circuit has an inductor $L = 50.0\\text{ mH}$ and a capacitor $C = 2.00\\ \\mu\\text{F}$.\\n(a) Calculate the critical damping resistance $R_{\\text{crit}}$,\\n(b) If the actual resistance in the circuit is $R = 60.0\\ \\Omega$, determine whether the transient discharge is underdamped, overdamped, or critically damped, and\\n(c) Calculate the damped oscillation frequency $\\omega_d$ and the logarithmic decrement $\\delta$.",
          "steps": [
            {
              "title": "Step 1: Compute critical resistance and natural frequency",
              "math": "$$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{(50.0 \\times 10^{-3} \\text{ H}) \\times (2.00 \\times 10^{-6} \\text{ F})}} = \\frac{1}{\\sqrt{1.000 \\times 10^{-7}}} = 3162.3 \\text{ rad/s}$$\n$$R_{\\text{crit}} = 2\\sqrt{\\frac{L}{C}} = 2\\sqrt{\\frac{50.0 \\times 10^{-3}}{2.00 \\times 10^{-6}}} = 2\\sqrt{25000} = 2 \\times 158.11 = 316.2\\ \\Omega$$",
              "explanation": "Critical damping requires a resistance of 316.2 ohms."
            },
            {
              "title": "Step 2: Regime identification for R = 60.0 ohms",
              "math": "$$R = 60.0\\ \\Omega < R_{\\text{crit}} = 316.2\\ \\Omega \\implies \\text{UNDERDAMPED OSCILLATORY REGIME}$$\n$$\\gamma = \\frac{R}{2L} = \\frac{60.0\\ \\Omega}{2 \\times (50.0 \\times 10^{-3} \\text{ H})} = \\frac{60.0}{0.100} = 600.0 \\text{ s}^{-1}$$",
              "explanation": "Because $R < R_{\\text{crit}}$, the circuit oscillates with decaying amplitude."
            },
            {
              "title": "Step 3: Damped frequency and logarithmic decrement",
              "math": "$$\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2} = \\sqrt{(3162.3)^2 - (600.0)^2} = \\sqrt{1.000 \\times 10^7 - 3.60 \\times 10^5} = \\sqrt{9.640 \\times 10^6} = 3104.8 \\text{ rad/s}$$\n$$f_d = \\frac{\\omega_d}{2\\pi} = \\frac{3104.8}{2\\pi} = 494.1 \\text{ Hz}$$\n$$T_d = \\frac{1}{f_d} = 2.0238 \\times 10^{-3} \\text{ s}$$\n$$\\delta = \\gamma T_d = 600.0 \\times (2.0238 \\times 10^{-3}) = 1.214$$",
              "explanation": "The circuit rings at 494 Hz with a logarithmic decrement $\\delta = 1.21$."
            }
          ]
        }
      ]
    }
  ]
};
