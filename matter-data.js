// Properties of Matter and Waves (Physics Core Courseware)
// Comprehensive university-standard textbook dataset covering all 8 Units with KaTeX derivations and 24 solved exam problems.

window.COURSE_DATA = {
  "courseTitle": "Properties of Matter and Waves",
  "courseCode": "PHYSICS",
  "department": "Department of Physics",
  "institution": "OpenSTEM Global Academic Press",
  "authorContact": "shahriyarkarimsiam@gmail.com",
  "units": [
    {
      "number": 1,
      "title": "Gravitation and Planetary Motion",
      "leadSummary": "Kepler's laws, universal gravitation, shell theorem, Cavendish experiment, equivalence of inertial and gravitational mass, gravitational potential, escape velocity, and variations in g.",
      "sections": [
        {
          "id": "sec-1-1",
          "number": "\u00a71.1",
          "heading": "Kepler's Laws of Planetary Motion",
          "simulation": "kepler-orbit-sim",
          "content": "Between 1609 and 1619, Johannes Kepler analyzed decades of precision astronomical observations of planetary positions compiled by Tycho Brahe, discovering three empirical kinematic laws that dismantled Ptolemaic and Copernican circular orbits.\n\n<h4>1. Kepler's Three Laws of Planetary Motion</h4>\n<ol>\n  <li><strong>First Law (Law of Ellipses):</strong> The orbit of every planet is an ellipse with the Sun located at one of the two focal points:\n  $$r(\\theta) = \\frac{p}{1 + e \\cos\\theta}$$\n  where $p = a(1 - e^2)$ is the semi-latus rectum, $a$ is the semi-major axis, and $e \\in [0, 1)$ is the orbital eccentricity.</li>\n  <li><strong>Second Law (Law of Equal Areas):</strong> A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time:\n  $$\\frac{dA}{dt} = \\text{constant}$$\n  </li>\n  <li><strong>Third Law (Harmonic Law):</strong> The square of the orbital period $T$ of a planet is directly proportional to the cube of the semi-major axis $a$ of its orbit:\n  $$T^2 \\propto a^3 \\implies \\frac{T^2}{a^3} = \\text{constant}$$\n  </li>\n</ol>\n\n<h4>2. Mathematical Proof of Kepler's Second Law from Angular Momentum Conservation</h4>\nConsider a planet of mass $m$ orbiting the Sun under an arbitrary central force $\\mathbf{F}(\\mathbf{r}) = F(r)\\hat{\\mathbf{r}}$.\nThe net torque acting on the planet about the Sun is:\n$$\\boldsymbol{\\tau} = \\mathbf{r} \\times \\mathbf{F}(\\mathbf{r}) = \\mathbf{r} \\times [F(r)\\hat{\\mathbf{r}}] = \\mathbf{0}$$\nSince torque is the time rate of change of orbital angular momentum $\\mathbf{L}$:\n$$\\frac{d\\mathbf{L}}{dt} = \\boldsymbol{\\tau} = \\mathbf{0} \\implies \\mathbf{L} = \\mathbf{r} \\times m\\mathbf{v} = \\text{constant vector}$$\nIn polar coordinates $(r, \\theta)$, in time $dt$, the radius vector rotates through angle $d\\theta$. The infinitesimal triangular area swept out is:\n$$dA = \\frac{1}{2} |\\mathbf{r} \\times d\\mathbf{r}| = \\frac{1}{2} r (r \\, d\\theta) = \\frac{1}{2} r^2 \\dot{\\theta} \\, dt$$\nThe areal velocity is therefore:\n$$\\frac{dA}{dt} = \\frac{1}{2} r^2 \\dot{\\theta} = \\frac{L}{2m} = \\text{constant}$$\nBecause angular momentum $L$ is strictly conserved for central forces, the areal velocity is constant! This proves Kepler's Second Law for <em>any</em> central force field."
        },
        {
          "id": "sec-1-2",
          "number": "\u00a71.2",
          "heading": "Newton's Law of Universal Gravitation",
          "simulation": "kepler-orbit-sim",
          "content": "In 1687, Sir Isaac Newton published the *Philosophiae Naturalis Principia Mathematica*, formulating the universal law of gravitation that unified celestial planetary mechanics with terrestrial falling bodies.\n\n<h4>1. Formulation of the Universal Law</h4>\nEvery particle of mass $m_1$ in the universe attracts every other particle of mass $m_2$ with a force directly proportional to the product of their masses and inversely proportional to the square of the distance $r$ separating them:\n$$\\mathbf{F}_{12} = -G \\frac{m_1 m_2}{r^2} \\hat{\\mathbf{r}}_{12}$$\nwhere $G = 6.67430 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2\\text{/kg}^2$ is Newton's universal gravitational constant, and $\\hat{\\mathbf{r}}_{12}$ is the unit vector pointing from mass 1 to mass 2.\n\n<h4>2. Deduction of the Inverse-Square Dependence from Kepler's Laws</h4>\nAssume a planet of mass $m$ moves in a circular orbit of radius $r$ with speed $v = \\frac{2\\pi r}{T}$ around the Sun ($M$).\nThe centripetal acceleration is provided exclusively by gravitational force:\n$$F = m \\frac{v^2}{r} = m \\frac{4\\pi^2 r^2}{r T^2} = 4\\pi^2 m \\frac{r}{T^2}$$\nApplying Kepler's Third Law ($T^2 = K r^3$):\n$$F = \\frac{4\\pi^2 m}{K r^2} \\propto \\frac{m}{r^2}$$\nBy Newton's Third Law of action-reaction, the force must also be proportional to the Sun's mass $M$, establishing $F \\propto \\frac{M m}{r^2}$.\n\n<h4>3. The Superposition Principle</h4>\nThe net gravitational force exerted on mass $m_0$ by a collection of $N$ discrete point masses is the vector sum:\n$$\\mathbf{F}_{\\text{net}} = -G m_0 \\sum_{i=1}^N \\frac{m_i}{|\\mathbf{r}_0 - \\mathbf{r}_i|^3} (\\mathbf{r}_0 - \\mathbf{r}_i)$$\nFor a continuous mass distribution of density $\\rho(\\mathbf{r}')$:\n$$\\mathbf{F}(\\mathbf{r}) = -G m_0 \\int_V \\frac{\\rho(\\mathbf{r}')}{|\\mathbf{r} - \\mathbf{r}'|^3} (\\mathbf{r} - \\mathbf{r}') \\, d^3\\mathbf{r}'$$"
        },
        {
          "id": "sec-1-3",
          "number": "\u00a71.3",
          "heading": "Gravitational Attraction and Newton's Shell Theorem",
          "simulation": "cavendish-gravitation-sim",
          "content": "Newton delayed publishing the *Principia* for nearly two decades until he mathematically proved the **Shell Theorem**, justifying why planets and moons can be treated as idealized point masses located at their centers.\n\n<h4>1. First Shell Theorem (External Field)</h4>\n<blockquote>\nA uniform spherical shell of mass $M$ and radius $R$ attracts an external point mass $m$ located at distance $r > R$ from its center as if the entire mass of the shell were concentrated at its geometric center:\n$$\\mathbf{g}(r) = -\\frac{GM}{r^2} \\hat{\\mathbf{r}} \\quad (r > R)$$\n</blockquote>\n\n<h4>2. Second Shell Theorem (Internal Field)</h4>\n<blockquote>\nA uniform spherical shell of mass $M$ exerts strictly zero net gravitational force on any particle located anywhere in its interior:\n$$\\mathbf{g}(r) = \\mathbf{0} \\quad (r < R)$$\n</blockquote>\n<em>Proof:</em> Divide the shell into pairs of opposing elemental surface areas $dA_1$ and $dA_2$ subtended by an infinitesimal double cone of solid angle $d\\Omega$.\nThe masses are $dm_1 = \\sigma dA_1 = \\sigma r_1^2 d\\Omega$ and $dm_2 = \\sigma dA_2 = \\sigma r_2^2 d\\Omega$.\nThe opposing gravitational forces are:\n$$dF_1 = G \\frac{m \\, dm_1}{r_1^2} = G m \\sigma d\\Omega, \\quad dF_2 = G \\frac{m \\, dm_2}{r_2^2} = G m \\sigma d\\Omega$$\nBecause $dF_1 = dF_2$, the opposing forces cancel identically for every direction throughout the $4\\pi$ sphere!\n\n<h4>3. Solid Sphere of Uniform Density ($\\rho$)</h4>\nFor a solid planet of radius $R$ and total mass $M = \\frac{4}{3}\\pi R^3 \\rho$:\n<ul>\n  <li><strong>Inside the planet ($r \\le R$):</strong> By the shell theorem, all outer spherical shells with radii $> r$ produce zero force. The force is due entirely to the inner sphere of radius $r$ containing mass $M(r) = M (r/R)^3$:\n  $$g(r) = \\frac{G M(r)}{r^2} = \\frac{G M}{R^3} r = \\frac{4}{3}\\pi G \\rho r$$\n  Gravity increases <em>linearly</em> from zero at the center to $g_0$ at the surface!</li>\n  <li><strong>Outside the planet ($r \\ge R$):</strong> Gravity falls as the inverse square:\n  $$g(r) = \\frac{GM}{r^2}$$\n  </li>\n</ul>"
        },
        {
          "id": "sec-1-4",
          "number": "\u00a71.4",
          "heading": "Determination of G: The Cavendish Experiment",
          "simulation": "cavendish-gravitation-sim",
          "content": "Because gravity is the weakest fundamental force in nature, determining $G$ required exquisite experimental ingenuity. Henry Cavendish (1798) measured $G$ in his historic experiment commonly described as *\"weighing the Earth\"*.\n\n<h4>1. The Torsion Balance Apparatus</h4>\nCavendish suspended a light horizontal wooden beam of length $L$ carrying two identical small lead spheres of mass $m$ from a thin, highly sensitive quartz/tungsten torsion wire with torsion constant $C$.\nTwo large stationary lead spheres of mass $M$ were brought near the small spheres at center-to-center distance $d$.\n\n<h4>2. Equilibrium Torque Balance</h4>\nThe gravitational attractive force between each pair of spheres is $F = G \\frac{M m}{d^2}$.\nThe deflecting gravitational couple is:\n$$\\tau_{\\text{grav}} = 2 F \\left(\\frac{L}{2}\\right) = F L = G \\frac{M m L}{d^2}$$\nIn equilibrium, this torque is balanced by the restoring elastic torque of the twisted wire:\n$$\\tau_{\\text{elastic}} = C \\theta \\implies G \\frac{M m L}{d^2} = C \\theta$$\nwhere $\\theta$ is the angular deflection, measured using an optical optical lever (light beam reflected from a mirror on the wire onto a distant scale).\n\n<h4>3. Determination of the Torsion Constant ($C$)</h4>\nTo eliminate the unknown wire stiffness $C$, Cavendish measured the period $T_0$ of free torsional oscillation of the suspended beam:\n$$T_0 = 2\\pi \\sqrt{\\frac{I}{C}} \\implies C = \\frac{4\\pi^2 I}{T_0^2}$$\nwhere $I = 2 m (L/2)^2 = \\frac{1}{2} m L^2$ is the moment of inertia of the small spheres.\nSubstituting $C$ gives $G$ directly:\n$$G = \\frac{2\\pi^2 L d^2 \\theta}{M T_0^2}$$\n\n<h4>4. Mass and Density of the Earth</h4>\nOnce $G$ was known, Cavendish calculated Earth's mass from surface gravity $g = \\frac{G M_E}{R_E^2}$:\n$$M_E = \\frac{g R_E^2}{G} = \\frac{(9.81)(6.371 \\times 10^6)^2}{6.674 \\times 10^{-11}} \\approx 5.972 \\times 10^{24}\\text{ kg}$$\nEarth's mean density is:\n$$\\bar{\\rho}_E = \\frac{M_E}{\\frac{4}{3}\\pi R_E^3} = \\frac{3 g}{4\\pi G R_E} \\approx 5,515\\text{ kg/m}^3$$\nBecause surface rocks have density $\\sim 2,700\\text{ kg/m}^3$, this proved that Earth possesses a dense metallic core (iron/nickel)!"
        },
        {
          "id": "sec-1-5",
          "number": "\u00a71.5",
          "heading": "Inertial Mass versus Gravitational Mass and Equivalence",
          "simulation": "cavendish-gravitation-sim",
          "content": "In physics, mass appears in two fundamentally distinct conceptual roles:\n\n<h4>1. Two Definitions of Mass</h4>\n<ol>\n  <li><strong>Inertial Mass ($m_i$):</strong> The measure of a body's resistance to acceleration when acted upon by <em>any</em> force, defined through Newton's Second Law:\n  $$\\mathbf{F} = m_i \\mathbf{a} \\implies m_i = \\frac{|\\mathbf{F}|}{|\\mathbf{a}|}$$\n  </li>\n  <li><strong>Gravitational Mass ($m_g$):</strong> The measure of a body's gravitational coupling strength (its gravitational 'charge'), defined through Newton's law of gravitation:\n  $$\\mathbf{F}_g = m_g \\mathbf{g} = G \\frac{M m_g}{r^2} \\hat{\\mathbf{r}}$$\n  </li>\n</ol>\n\n<h4>2. The Weak Equivalence Principle</h4>\nSetting inertial force equal to gravitational force for a freely falling object:\n$$m_i \\mathbf{a} = m_g \\mathbf{g} \\implies \\mathbf{a} = \\left( \\frac{m_g}{m_i} \\right) \\mathbf{g}$$\nIf $m_g / m_i$ were different for different materials, a feather and a cannonball in a vacuum would accelerate at different rates.\nGalileo's Leaning Tower experiments, Newton's pendulum trials, and Lor\u00e1nd E\u00f6tv\u00f6s's precision torsion balance experiments (1889) demonstrated that:\n$$\\frac{m_g}{m_i} = 1.000000000000000$$\nModern satellite experiments (MICROSCOPE, 2022) confirm the equivalence to within 1 part in $10^{15}$.\n\n<h4>3. Physical Significance: General Relativity</h4>\nAlbert Einstein recognized that the strict proportionality $m_i \\equiv m_g$ is not a cosmic coincidence. It led directly to the **Einstein Equivalence Principle**:\n<blockquote>\nThe effects of a uniform gravitational field are physically indistinguishable from the effects of a uniformly accelerating frame of reference.\n</blockquote>\nThis principle forms the cornerstone of Einstein's General Theory of Relativity, where gravity is not a Newtonian force, but the curvature of four-dimensional spacetime."
        },
        {
          "id": "sec-1-6",
          "number": "\u00a71.6",
          "heading": "Gravitational Field and Potential Energy",
          "simulation": "kepler-orbit-sim",
          "content": "The gravitational interaction is a conservative vector field described by a scalar potential.\n\n<h4>1. Gravitational Field Intensity ($\\mathbf{g}$)</h4>\nThe gravitational field $\\mathbf{g}(\\mathbf{r})$ at point $\\mathbf{r}$ is the gravitational force experienced per unit test mass placed at that point:\n$$\\mathbf{g}(\\mathbf{r}) = \\lim_{m_0 \\to 0} \\frac{\\mathbf{F}_g}{m_0} = -\\frac{GM}{r^2} \\hat{\\mathbf{r}}$$\n\n<h4>2. Gravitational Potential ($V$)</h4>\nBecause gravity is a conservative force ($\\boldsymbol{\\nabla} \\times \\mathbf{g} = \\mathbf{0}$), it can be expressed as the negative gradient of a scalar **gravitational potential** $V(\\mathbf{r})$:\n$$\\mathbf{g} = -\\boldsymbol{\\nabla}V \\implies V(r) = -\\int_\\infty^r \\mathbf{g} \\cdot d\\mathbf{r}' = -\\int_\\infty^r \\left(-\\frac{GM}{r'^2}\\right) dr' = -\\frac{GM}{r}$$\ntaking $V(\\infty) = 0$ as the reference zero-potential at infinite separation.\n\n<h4>3. Gravitational Potential Energy ($U$)</h4>\nThe potential energy of a two-particle system with masses $M$ and $m$ is:\n$$U(r) = m V(r) = -\\frac{GMm}{r}$$\nNotice that $U(r)$ is strictly negative for all finite separations, reflecting an attractive bound state.\n\n<h4>4. Gravitational Self-Energy of a Uniform Sphere</h4>\nThe work required to assemble a uniform solid sphere of mass $M$, radius $R$, and density $\\rho$ by bringing infinitesimal mass shells $dm$ from infinity:\n$$U_{\\text{self}} = -\\int_0^R \\frac{G M(r) \\, dm}{r} = -\\int_0^R \\frac{G \\left(\\frac{4}{3}\\pi \\rho r^3\\right) \\left(4\\pi \\rho r^2 dr\\right)}{r} = -\\frac{16\\pi^2 G \\rho^2}{3} \\int_0^R r^4 dr$$\n$$U_{\\text{self}} = -\\frac{16\\pi^2 G \\rho^2 R^5}{15} = -\\frac{3}{5} \\frac{G M^2}{R}$$\nThis negative gravitational binding energy plays a critical role in stellar astrophysics and planetary core collapse."
        },
        {
          "id": "sec-1-7",
          "number": "\u00a71.7",
          "heading": "Escape Velocity, Orbits, and the Vis-Viva Equation",
          "simulation": "kepler-orbit-sim",
          "content": "Orbital dynamics governs the trajectories of artificial satellites, planets, and interstellar space probes.\n\n<h4>1. Escape Velocity ($v_{\\text{esc}}$)</h4>\nThe **escape velocity** is the minimum initial speed a projectile must have at the surface of a body of mass $M$ and radius $R$ to completely escape its gravitational well to infinity without further propulsion.\nBy conservation of mechanical energy:\n$$E_i = \\frac{1}{2} m v_{\\text{esc}}^2 - \\frac{GMm}{R} = E_f = 0 \\implies v_{\\text{esc}} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2 g R}$$\nFor Earth ($R = 6,371\\text{ km}, g = 9.81\\text{ m/s}^2$):\n$$v_{\\text{esc}} = \\sqrt{2 \\times 9.81 \\times 6.371 \\times 10^6} \\approx 11,180\\text{ m/s} \\approx 11.2\\text{ km/s}$$\nFor the Moon: $v_{\\text{esc}} \\approx 2.38\\text{ km/s}$. For the Sun: $v_{\\text{esc}} \\approx 618\\text{ km/s}$.\n\n<h4>2. Orbital Velocity for a Circular Orbit</h4>\nFor a circular satellite orbit at altitude $h$ above Earth's surface ($r = R + h$):\n$$\\frac{m v_{\\text{orb}}^2}{r} = \\frac{GMm}{r^2} \\implies v_{\\text{orb}} = \\sqrt{\\frac{GM}{r}} = \\frac{v_{\\text{esc}}}{\\sqrt{2}}$$\nAt low Earth orbit ($r \\approx R_E$): $v_{\\text{orb}} \\approx 7.91\\text{ km/s}$ (First Cosmic Velocity).\n\n<h4>3. The Vis-Viva Equation</h4>\nFor an arbitrary Keplerian orbit with semi-major axis $a$, the total mechanical energy is $E = -\\frac{GMm}{2a}$.\nEquating kinetic plus potential energy to total energy:\n$$\\frac{1}{2} m v^2 - \\frac{GMm}{r} = -\\frac{GMm}{2a} \\implies v^2 = G M \\left( \\frac{2}{r} - \\frac{1}{a} \\right)$$\nThis is the celebrated **Vis-Viva Equation**:\n<ul>\n  <li><strong>Circular Orbit ($a = r$):</strong> $v = \\sqrt{GM/r}$, $E < 0$.</li>\n  <li><strong>Elliptic Orbit ($a > 0$):</strong> Speed is maximum at periapsis ($r = r_{\\min}$) and minimum at apoapsis ($r = r_{\\max}$).</li>\n  <li><strong>Parabolic Orbit ($a \\to \\infty$):</strong> $v = \\sqrt{2GM/r}$, total energy $E = 0$ (marginally unbound).</li>\n  <li><strong>Hyperbolic Orbit ($a < 0$):</strong> $E > 0$ (unbound interstellar trajectory).</li>\n</ul>"
        },
        {
          "id": "sec-1-8",
          "number": "\u00a71.8",
          "heading": "The Acceleration Due to Gravity and Its Spatial Variations",
          "simulation": "cavendish-gravitation-sim",
          "content": "The local acceleration due to gravity $g$ is not universally constant; it varies systematically with altitude, depth, latitude, and local geology.\n\n<h4>1. Variation of $g$ with Altitude ($h$)</h4>\nAt an elevation $h$ above sea level ($r = R_E + h$):\n$$g(h) = \\frac{G M_E}{(R_E + h)^2} = \\frac{G M_E}{R_E^2 \\left(1 + \\frac{h}{R_E}\\right)^2} = g_0 \\left(1 + \\frac{h}{R_E}\\right)^{-2}$$\nFor altitudes small compared to Earth's radius ($h \\ll R_E \\approx 6371\\text{ km}$), expanding via binomial series:\n$$g(h) \\approx g_0 \\left(1 - \\frac{2h}{R_E}\\right)$$\nGravity decreases by approximately $0.03\\%$ for every kilometer of altitude.\n\n<h4>2. Variation of $g$ with Depth ($d$)</h4>\nInside a mine at depth $d$ below the surface ($r = R_E - d$), by the Shell Theorem:\n$$g(d) = \\frac{G M(r)}{r^2} = \\frac{4}{3}\\pi G \\rho (R_E - d) = g_0 \\left(1 - \\frac{d}{R_E}\\right)$$\nGravity decreases linearly to zero at Earth's center. Notice that gravity decreases <em>twice as rapidly with altitude</em> as it does with depth!\n\n<h4>3. Variation with Latitude ($\\phi$) due to Earth's Axial Rotation</h4>\nBecause Earth rotates with angular speed $\\omega = 7.292 \\times 10^{-5}\\text{ rad/s}$, a body at latitude $\\phi$ experiences an outward centrifugal acceleration:\n$$a_c = \\omega^2 r_\\perp = \\omega^2 (R_E \\cos\\phi)$$\nThe effective gravity measured by a spring balance is the vector sum:\n$$g_{\\text{eff}}(\\phi) \\approx g_0 - R_E \\omega^2 \\cos^2\\phi$$\n<ul>\n  <li>At the **Equator** ($\\phi = 0^\\circ$): Centrifugal reduction is maximum:\n  $$\\Delta g = R_E \\omega^2 = (6.378 \\times 10^6)(7.292 \\times 10^{-5})^2 \\approx 0.0339\\text{ m/s}^2$$\n  giving $g_{\\text{equator}} \\approx 9.780\\text{ m/s}^2$.</li>\n  <li>At the **Poles** ($\\phi = 90^\\circ$): Centrifugal effect vanishes: $g_{\\text{pole}} \\approx 9.832\\text{ m/s}^2$.</li>\n</ul>\nCombined with Earth's equatorial bulge (flattening $f \\approx 1/298$), objects weigh approximately $0.53\\%$ more at the poles than at the equator!"
        },
        {
          "id": "sec-1-9",
          "number": "\u00a71.9",
          "heading": "Measurement of g: Compound and Kater's Reversible Pendulum",
          "simulation": "cavendish-gravitation-sim",
          "content": "Accurate geodetic measurements of $g$ require eliminating measurement errors caused by distributed pendulum mass.\n\n<h4>1. The Compound (Physical) Pendulum</h4>\nA compound pendulum is any rigid body free to oscillate in a vertical plane about a fixed horizontal axis.\nLet $m$ be the total mass, $d$ the distance from the pivot point $O$ to the center of gravity $G$, and $I$ the moment of inertia about $O$:\n$$I = I_G + m d^2 = m (k^2 + d^2)$$\nwhere $k$ is the radius of gyration about $G$.\nThe restoring torque for angular displacement $\\theta$ is $\\tau = -m g d \\sin\\theta \\approx -m g d \\theta$.\nThe equation of motion is:\n$$I \\ddot{\\theta} + m g d \\theta = 0 \\implies T = 2\\pi \\sqrt{\\frac{I}{m g d}} = 2\\pi \\sqrt{\\frac{k^2 + d^2}{g d}} = 2\\pi \\sqrt{\\frac{L_{\\text{eff}}}{g}}$$\nwhere $L_{\\text{eff}} = \\frac{k^2 + d^2}{d} = d + \\frac{k^2}{d}$ is the length of the **equivalent simple pendulum**.\n\n<h4>2. Center of Oscillation and Conjugate Points</h4>\nAlong the line passing through pivot $O$ and center of mass $G$, there exists a point $O'$ at distance $d' = k^2 / d$ on the opposite side of $G$.\nIf the pendulum is inverted and suspended from $O'$, its period of oscillation is:\n$$T' = 2\\pi \\sqrt{\\frac{k^2 + d'^2}{g d'}} = 2\\pi \\sqrt{\\frac{k^2 + (k^2/d)^2}{g (k^2/d)}} = 2\\pi \\sqrt{\\frac{d + k^2/d}{g}} = T$$\nThe points $O$ and $O'$ are **mutually conjugate**: the periods of oscillation about both points are identical! The distance between them is exactly $L_{\\text{eff}} = d + d'$.\n\n<h4>3. Kater's Reversible Pendulum</h4>\nInvented by Captain Henry Kater (1818), this precision instrument consists of a rigid metal bar with two adjustable knife-edges facing inward and movable weights.\nBy adjusting the weights until the period of oscillation about knife-edge 1 ($T_1$) equals the period about knife-edge 2 ($T_2 = T_1 = T$):\n$$g = \\frac{4\\pi^2 L}{T^2}$$\nwhere $L$ is simply the physical distance between the two knife-edges, which can be measured with a traveling microscope to sub-millimeter precision!\nThis completely eliminates the need to determine the unknown moment of inertia $I$, center of mass $G$, or radius of gyration $k$!"
        }
      ],
      "problems": [
        {
          "id": "prob-1-1",
          "difficulty": "Medium",
          "title": "Geostationary Satellite Orbit Radius and Speed",
          "question": "A geostationary communications satellite must remain stationary relative to an observer on Earth's equator. (a) Derive the formula for the orbital radius $r$ of a geostationary orbit in terms of Earth's sidereal day ($T = 86,164\\text{ s}$), $G$, and $M_E$. (b) Calculate the orbital altitude $h$ above the equator and the orbital speed $v$.",
          "steps": [
            {
              "title": "Step 1: Equate centripetal force to gravitational attraction",
              "math": "$$\\frac{m v^2}{r} = m \\omega^2 r = m \\left(\\frac{2\\pi}{T}\\right)^2 r = \\frac{G M_E m}{r^2}$$\n$$r^3 = \\frac{G M_E T^2}{4\\pi^2} \\implies r = \\left( \\frac{G M_E T^2}{4\\pi^2} \\right)^{1/3}$$",
              "explanation": "To remain geostationary, the satellite's orbital period must match Earth's sidereal rotation period ($T = 86,164\\text{ s} = 23\\text{ h } 56\\text{ m } 4\\text{ s}$)."
            },
            {
              "title": "Step 2: Substitute numerical values for Earth",
              "math": "$$G M_E = (6.6743 \\times 10^{-11})(5.972 \\times 10^{24}) = 3.986 \\times 10^{14}\\text{ m}^3\\text{/s}^2$$\n$$T^2 = (86,164\\text{ s})^2 = 7.424 \\times 10^9\\text{ s}^2$$\n$$r^3 = \\frac{(3.986 \\times 10^{14})(7.424 \\times 10^9)}{4\\pi^2} = 7.496 \\times 10^{22}\\text{ m}^3$$\n$$r = (7.496 \\times 10^{22})^{1/3} = 4.2164 \\times 10^7\\text{ m} = 42,164\\text{ km}$$",
              "explanation": "This is the orbital radius measured from the center of the Earth."
            },
            {
              "title": "Step 3: Calculate altitude above surface and orbital speed",
              "math": "$$h = r - R_E = 42,164\\text{ km} - 6,371\\text{ km} = 35,793\\text{ km} \\approx 35,800\\text{ km}$$\n$$v = \\frac{2\\pi r}{T} = \\frac{2\\pi (4.2164 \\times 10^7\\text{ m})}{86,164\\text{ s}} = 3,075\\text{ m/s} \\approx 3.08\\text{ km/s}$$",
              "explanation": "Geostationary satellites orbit at roughly $35,800\\text{ km}$ altitude with a constant speed of $3.08\\text{ km/s}$."
            }
          ]
        },
        {
          "id": "prob-1-2",
          "difficulty": "Hard",
          "title": "Tunnel Through the Center of the Earth",
          "question": "Assume a straight, frictionless tunnel is drilled through the center of the Earth between opposite sides. A particle of mass $m$ is dropped into the tunnel from the surface. (a) Prove that the particle executes Simple Harmonic Motion (SHM). (b) Calculate the period of oscillation $T$ and the speed of the particle as it passes the center of the Earth.",
          "steps": [
            {
              "title": "Step 1: Apply Shell Theorem to find restoring force at distance r",
              "math": "$$F(r) = -\\frac{G M(r) m}{r^2} = -\\frac{G \\left(M_E \\frac{r^3}{R_E^3}\\right) m}{r^2} = -\\left(\\frac{G M_E m}{R_E^3}\\right) r = -\\left(\\frac{m g}{R_E}\\right) r$$",
              "explanation": "The gravitational force is strictly proportional to displacement from the center: $F = -k r$, with effective spring constant $k = \\frac{m g}{R_E}$."
            },
            {
              "title": "Step 2: Compute the period of harmonic oscillation",
              "math": "$$m \\ddot{r} + \\left(\\frac{m g}{R_E}\\right) r = 0 \\implies \\omega = \\sqrt{\\frac{g}{R_E}}$$\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{R_E}{g}} = 2\\pi \\sqrt{\\frac{6.371 \\times 10^6\\text{ m}}{9.81\\text{ m/s}^2}} = 2\\pi (805.9\\text{ s}) = 5,064\\text{ s} \\approx 84.4\\text{ minutes}$$",
              "explanation": "The round-trip period is $84.4$ minutes (a one-way journey takes exactly $42.2$ minutes), matching the period of a low-Earth circular orbit!"
            },
            {
              "title": "Step 3: Calculate maximum speed at the center",
              "math": "$$v_{\\max} = \\omega A = \\sqrt{\\frac{g}{R_E}} R_E = \\sqrt{g R_E} = \\sqrt{(9.81)(6.371 \\times 10^6)} = 7,906\\text{ m/s} \\approx 7.91\\text{ km/s}$$",
              "explanation": "As the particle shoots through Earth's center, it reaches $7.91\\text{ km/s}$ (First Cosmic Velocity)."
            }
          ]
        },
        {
          "id": "prob-1-3",
          "difficulty": "Hard",
          "title": "Hohmann Transfer Orbit to Mars",
          "question": "A spacecraft leaves Earth's orbit ($r_1 = 1.000\\text{ AU} = 1.496 \\times 10^{11}\\text{ m}$) on a semi-elliptical Hohmann transfer orbit to reach Mars ($r_2 = 1.524\\text{ AU} = 2.280 \\times 10^{11}\\text{ m}$). (a) Calculate the semi-major axis $a$ of the transfer orbit. (b) Using Kepler's Third Law, calculate the one-way travel time in Earth days. (c) Use the Vis-Viva equation to find the spacecraft's launch velocity boost relative to the Sun.",
          "steps": [
            {
              "title": "Step 1: Determine the semi-major axis a of the Hohmann ellipse",
              "math": "$$2a = r_1 + r_2 = 1.000\\text{ AU} + 1.524\\text{ AU} = 2.524\\text{ AU} \\implies a = 1.262\\text{ AU}$$",
              "explanation": "The perihelion of the transfer orbit is at Earth's orbit, and the aphelion is at Mars' orbit."
            },
            {
              "title": "Step 2: Calculate transfer time via Kepler's Third Law",
              "math": "$$T_{\\text{transfer}}^2 = a^3 = (1.262)^3 = 2.010\\text{ yr}^2 \\implies T_{\\text{transfer}} = 1.418\\text{ years}$$\n$$\\text{One-way travel time } t = \\frac{1}{2} T_{\\text{transfer}} = 0.709\\text{ years} = 0.709 \\times 365.25\\text{ days} \\approx 259\\text{ days}$$",
              "explanation": "The voyage to Mars takes approximately 259 days (~8.5 months)."
            },
            {
              "title": "Step 3: Calculate launch speed at Earth perihelion using Vis-Viva equation",
              "math": "$$v^2 = G M_\\odot \\left( \\frac{2}{r_1} - \\frac{1}{a} \\right) = (1.327 \\times 10^{20}) \\left( \\frac{2}{1.496 \\times 10^{11}} - \\frac{1}{1.888 \\times 10^{11}} \\right)$$\n$$v = 32.73\\text{ km/s}$$\n$$\\text{Earth orbital speed } v_E = 29.78\\text{ km/s} \\implies \\Delta v = 32.73 - 29.78 = 2.95\\text{ km/s}$$",
              "explanation": "A velocity boost of $2.95\\text{ km/s}$ beyond Earth escape puts the probe into the interplanetary Hohmann orbit."
            }
          ]
        }
      ]
    },
    {
      "number": 2,
      "title": "Elasticity and Mechanical Properties of Solids",
      "leadSummary": "Stress-strain tensors, plane stress, Hooke's law, elastic moduli, Poisson's ratio limits, strain energy, torsion of cylinders, coil springs, beam bending, and cantilevers.",
      "sections": [
        {
          "id": "sec-2-1",
          "number": "\u00a72.1",
          "heading": "Stress, Plane Stress, and Tensor Transformations",
          "simulation": "hooke-stress-strain-sim",
          "content": "When an external deforming force acts upon a deformable solid body, the atoms are displaced from their microscopic equilibrium lattice positions, setting up internal restoring forces that resist deformation.\n\n<h4>1. Definition of Stress</h4>\n**Stress** ($\\sigma$ or $\\tau$) is defined as the internal restoring force developed per unit area of the deformed cross section:\n$$\\boldsymbol{\\sigma} = \\lim_{\\Delta A \\to 0} \\frac{\\Delta \\mathbf{F}}{\\Delta A}$$\nIn SI units, stress is measured in Pascals ($1\\text{ Pa} = 1\\text{ N/m}^2$) or megapascals ($1\\text{ MPa} = 10^6\\text{ Pa}$).\n<ul>\n  <li><strong>Normal Stress ($\\sigma$):</strong> Restoring force acts perpendicular to the cross-sectional area. Tensile stress elongates the material ($\\sigma > 0$), while compressive stress shortens it ($\\sigma < 0$).</li>\n  <li><strong>Shear (Tangential) Stress ($\\tau$):</strong> Restoring force acts parallel (tangential) to the surface plane, sliding adjacent atomic layers past one another.</li>\n</ul>\n\n<h4>2. The State of Plane Stress</h4>\nA solid element is in a state of **plane stress** when all stress vectors acting on one coordinate plane vanish identically: $\\sigma_{zz} = \\tau_{xz} = \\tau_{yz} = 0$.\nThe stress state is completely characterized by the 2D stress tensor:\n$$\\boldsymbol{\\sigma}_{2D} = \\begin{pmatrix} \\sigma_{xx} & \\tau_{xy} \\\\ \\tau_{xy} & \\sigma_{yy} \\end{pmatrix}$$\nwhere $\\tau_{xy} = \\tau_{yx}$ by the conservation of angular momentum (complementary shear stresses).\n\n<h4>3. Mohr's Circle and Principal Stresses</h4>\nUnder a coordinate rotation by angle $\\theta$, the normal and shear stresses transform as:\n$$\\sigma_{\\theta} = \\frac{\\sigma_{xx} + \\sigma_{yy}}{2} + \\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\cos(2\\theta) + \\tau_{xy}\\sin(2\\theta)$$\n$$\\tau_{\\theta} = -\\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\sin(2\\theta) + \\tau_{xy}\\cos(2\\theta)$$\nThe maximum and minimum normal stresses are the **Principal Stresses** (where shear stress $\\tau = 0$):\n$$\\sigma_{1, 2} = \\frac{\\sigma_{xx} + \\sigma_{yy}}{2} \\pm \\sqrt{\\left(\\frac{\\sigma_{xx} - \\sigma_{yy}}{2}\\right)^2 + \\tau_{xy}^2}$$\nExamples of plane stress include thin-walled pressure vessels, aircraft skins, and surface beams under pure bending."
        },
        {
          "id": "sec-2-2",
          "number": "\u00a72.2",
          "heading": "Strain and Hydrostatic Pressure",
          "simulation": "hooke-stress-strain-sim",
          "content": "**Strain** is the fractional geometric deformation produced in a body under applied stress. Because strain is a ratio of identical physical dimensions, it is a dimensionless quantity.\n\n<h4>1. The Three Primary Types of Strain</h4>\n<ol>\n  <li><strong>Longitudinal (Tensile) Strain:</strong> The fractional change in length:\n  $$\\epsilon = \\frac{\\Delta L}{L}$$\n  </li>\n  <li><strong>Shearing Strain ($\\theta$):</strong> The angular distortion (in radians) between two lines initially perpendicular to each other in the unstrained state:\n  $$\\theta = \\frac{\\Delta x}{L} \\approx \\tan\\theta$$\n  </li>\n  <li><strong>Volumetric Strain ($\\theta_v$):</strong> The fractional change in volume:\n  $$\\theta_v = \\frac{\\Delta V}{V}$$\n  </li>\n</ol>\n\n<h4>2. Hydrostatic Pressure</h4>\nWhen a solid is submerged in a fluid, it experiences uniform normal compressive stress on every surface element with zero shear stress:\n$$\\sigma_{xx} = \\sigma_{yy} = \\sigma_{zz} = -P, \\quad \\tau_{xy} = \\tau_{yz} = \\tau_{zx} = 0$$\nThe body undergoes pure volumetric compression without any change in shape:\n$$\\frac{\\Delta V}{V} = -\\frac{P}{K}$$\nwhere $K$ is the bulk modulus."
        },
        {
          "id": "sec-2-3",
          "number": "\u00a72.3",
          "heading": "Hooke's Law and the Complete Stress-Strain Diagram",
          "simulation": "hooke-stress-strain-sim",
          "content": "Robert Hooke (1676) discovered the fundamental law of elasticity: *Ut tensio, sic vis* (*as the extension, so the force*).\n\n<h4>1. Hooke's Law</h4>\nWithin the elastic limit of a material, stress is directly proportional to strain:\n$$\\text{Stress} \\propto \\text{Strain} \\implies \\sigma = E \\, \\epsilon$$\nwhere the constant of proportionality $E$ is the **Modulus of Elasticity**.\n\n<h4>2. Detailed Analysis of the Engineering Stress-Strain Curve</h4>\nFor a ductile material like mild structural steel subjected to tensile testing:\n<ul>\n  <li><strong>Region OA (Proportional Limit $\\sigma_p$):</strong> Stress is strictly linear with strain. Hooke's law is valid. Slope $d\\sigma/d\\epsilon = Y$ gives Young's modulus.</li>\n  <li><strong>Point B (Elastic Limit / Yield Point $\\sigma_y$):</strong> The maximum stress to which the material can be subjected without incurring permanent plastic deformation upon release.</li>\n  <li><strong>Region BC (Plastic Flow & Strain Hardening):</strong> Beyond the yield point, atomic planes slip along crystallographic planes (dislocation movement). Permanent deformation (**plastic strain**) remains upon unloading.</li>\n  <li><strong>Point D (Ultimate Tensile Strength $\\sigma_{\\text{UTS}}$):</strong> The maximum engineering stress the material can sustain. Beyond this point, macroscopic localized cross-sectional narrowing (**necking**) occurs.</li>\n  <li><strong>Point E (Fracture Point $\\sigma_f$):</strong> The specimen tears apart into two pieces.</li>\n</ul>\n\n<h4>3. Ductile versus Brittle Materials</h4>\n<ul>\n  <li><strong>Ductile Materials (Mild Steel, Copper, Aluminum):</strong> Large plastic deformation between yield point and fracture ($> 5\\%$ strain). Can be drawn into thin wires or hammered into sheets.</li>\n  <li><strong>Brittle Materials (Glass, Cast Iron, Ceramics, Concrete):</strong> Fracture occurs immediately at or slightly beyond the elastic limit with virtually zero plastic deformation. High compressive strength but poor tensile tolerance.</li>\n</ul>"
        },
        {
          "id": "sec-2-4",
          "number": "\u00a72.4",
          "heading": "Elastic Hysteresis and Internal Friction",
          "simulation": "hooke-stress-strain-sim",
          "content": "In ideal elasticity, loading and unloading follow the exact same path. In real materials, internal atomic friction causes the unloading stress-strain curve to lag behind the loading curve.\n\n<h4>1. The Elastic Hysteresis Loop</h4>\nWhen a material (such as vulcanized rubber) is stretched and then allowed to relax, the strain during unloading is greater than during loading at the identical stress level.\nThe closed loop formed by the loading and unloading curves in the $(\\sigma, \\epsilon)$ plane is the **Elastic Hysteresis Loop**.\n\n<h4>2. Energy Dissipation as Heat</h4>\nThe work done per unit volume during loading is:\n$$w_{\\text{load}} = \\int_0^{\\epsilon_{\\max}} \\sigma_{\\text{load}} \\, d\\epsilon$$\nThe elastic work recovered per unit volume during unloading is:\n$$w_{\\text{unload}} = \\int_{\\epsilon_{\\max}}^0 \\sigma_{\\text{unload}} \\, d\\epsilon$$\nThe net energy dissipated per unit volume per cycle is the area enclosed by the loop:\n$$\\Delta U_{\\text{dissipated}} = \\oint \\sigma \\, d\\epsilon = \\text{Area of Hysteresis Loop}$$\nThis mechanical energy is converted irreversibly into internal thermal heat.\n\n<h4>3. Engineering Applications</h4>\n<ul>\n  <li><strong>High Hysteresis Materials (Rubber, Elastomers):</strong> Used in automobile tires, engine vibration isolators, and earthquake building dampeners because they rapidly dissipate kinetic shocks into heat.</li>\n  <li><strong>Low Hysteresis Materials (Quartz, Phosphor Bronze):</strong> Used for suspension strips in precision galvanometers, gravimeters, and mechanical watch balance springs to avoid energy loss and drift.</li>\n</ul>"
        },
        {
          "id": "sec-2-5",
          "number": "\u00a72.5",
          "heading": "The Four Elastic Moduli and Poisson's Ratio",
          "simulation": "hooke-stress-strain-sim",
          "content": "Homogeneous and isotropic materials possess four foundational elastic constants that characterize their response to tension, pressure, shear, and transverse deformation.\n\n<h4>1. Young's Modulus ($Y$)</h4>\nDefined as the ratio of tensile (or compressive) longitudinal stress to longitudinal strain:\n$$Y = \\frac{\\sigma}{\\epsilon} = \\frac{F / A}{\\Delta L / L} = \\frac{F L}{A \\Delta L}$$\nTypical values: Steel ($Y \\approx 200\\text{ GPa}$), Copper ($Y \\approx 110\\text{ GPa}$), Glass ($Y \\approx 70\\text{ GPa}$).\n\n<h4>2. Bulk Modulus ($K$)</h4>\nDefined as the ratio of hydrostatic pressure stress to volumetric strain:\n$$K = -\\frac{\\Delta P}{\\Delta V / V} = -V \\frac{dP}{dV}$$\nThe negative sign ensures $K > 0$ because an increase in pressure produces a decrease in volume.\nThe reciprocal of bulk modulus is the **Compressibility** $\\beta = 1/K$.\n\n<h4>3. Shear Modulus / Modulus of Rigidity ($\\eta$ or $G$)</h4>\nDefined as the ratio of shear stress to shearing strain:\n$$\\eta = \\frac{\\tau}{\\theta} = \\frac{F_t / A}{\\Delta x / L}$$\nFor most solid materials, shear modulus is roughly one-third of Young's modulus: $\\eta \\approx 0.35 Y$ to $0.40 Y$. Liquids and gases have zero static shear modulus ($\\eta = 0$) because they cannot resist static shear.\n\n<h4>4. Poisson's Ratio ($\\sigma$ or $\nu$)</h4>\nWhen a rod is stretched longitudinally, it narrows laterally. Poisson's ratio is the ratio of lateral fractional contraction to longitudinal fractional elongation:\n$$\\sigma = -\\frac{\\text{Lateral Strain}}{\\text{Longitudinal Strain}} = -\\frac{\\Delta d / d}{\\Delta L / L}$$\nBecause $\\Delta d < 0$ when $\\Delta L > 0$, the minus sign ensures $\\sigma > 0$ for conventional materials."
        },
        {
          "id": "sec-2-6",
          "number": "\u00a72.6",
          "heading": "Internal Elastic Strain Energy Density",
          "simulation": "hooke-stress-strain-sim",
          "content": "When external work deforms a solid elastically, the work is stored internally as **Elastic Potential Energy** (or strain energy) within the distorted interatomic electrostatic bonds.\n\n<h4>1. Strain Energy in a Stretched Wire</h4>\nConsider a wire of original length $L$ and cross-sectional area $A$. When elongated by $x$, the restoring force is $F(x) = \\frac{Y A}{L} x$.\nThe total work done to stretch the wire by final extension $\\Delta L$ is:\n$$W = \\int_0^{\\Delta L} F(x) \\, dx = \\frac{Y A}{L} \\int_0^{\\Delta L} x \\, dx = \\frac{1}{2} \\frac{Y A}{L} (\\Delta L)^2 = \\frac{1}{2} F_{\\max} \\Delta L$$\n<blockquote>\nThe stored elastic strain energy equals <strong>one-half</strong> the product of final stretching force and elongation:\n$$U = \\frac{1}{2} F \\Delta L$$\n</blockquote>\n\n<h4>2. Strain Energy Density ($u$)</h4>\nThe strain energy per unit volume ($V = A L$) is:\n$$u = \\frac{U}{A L} = \\frac{1}{2} \\left( \\frac{F}{A} \\right) \\left( \\frac{\\Delta L}{L} \\right) = \\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain}$$\nUsing Hooke's law $\\sigma = Y \\epsilon$:\n$$u = \\frac{1}{2} Y \\epsilon^2 = \\frac{\\sigma^2}{2Y}$$\n\n<h4>3. Energy Densities for Shear and Hydrostatic Compression</h4>\n<ul>\n  <li><strong>Under Pure Shear:</strong> $u_s = \\frac{1}{2} \\tau \\theta = \\frac{1}{2} \\eta \\theta^2 = \\frac{\\tau^2}{2\\eta}$</li>\n  <li><strong>Under Hydrostatic Compression:</strong> $u_v = \\frac{1}{2} P \\left(-\\frac{\\Delta V}{V}\\right) = \\frac{1}{2} K \\theta_v^2 = \\frac{P^2}{2K}$</li>\n</ul>"
        },
        {
          "id": "sec-2-7",
          "number": "\u00a72.7",
          "heading": "Relations Between Elastic Constants and Theoretical Limits of Poisson's Ratio",
          "simulation": "hooke-stress-strain-sim",
          "content": "For any isotropic, linear elastic solid, only **two** of the four elastic constants ($Y, K, \\eta, \\sigma$) are independent. The other two can be derived through geometry and mechanics.\n\n<h4>1. Mathematical Derivations of the Interrelations</h4>\nConsider a unit cube subjected to normal tensile stresses $\\sigma_x$ along $x$.\nThe resulting strains along each principal axis are:\n$$\\epsilon_x = \\frac{\\sigma_x}{Y}, \\quad \\epsilon_y = -\\sigma \\frac{\\sigma_x}{Y}, \\quad \\epsilon_z = -\\sigma \\frac{\\sigma_x}{Y}$$\n<ol>\n  <li><strong>Relation between $Y, K$, and $\\sigma$:</strong> Apply uniform hydrostatic pressure $\\sigma_x = \\sigma_y = \\sigma_z = -P$.\n  The volumetric strain is $\\theta_v = \\epsilon_x + \\epsilon_y + \\epsilon_z = 3 \\epsilon_x = -3 \\frac{P}{Y}(1 - 2\\sigma)$.\n  Since $K = -P / \\theta_v$:\n  $$Y = 3K (1 - 2\\sigma)$$\n  </li>\n  <li><strong>Relation between $Y, \\eta$, and $\\sigma$:</strong> Apply equal and opposite tensile and compressive stresses $\\sigma_x = -\\sigma_y = \\sigma$.\n  This stress state is pure shear $\\tau = \\sigma$ at $45^\\circ$, producing shear strain $\\theta = 2\\epsilon_x = \\frac{2\\sigma}{Y}(1 + \\sigma)$.\n  Since $\\eta = \\tau / \\theta$:\n  $$Y = 2\\eta (1 + \\sigma)$$\n  </li>\n  <li><strong>Combined Relations:</strong> Equating expressions for $Y$:\n  $$3K(1 - 2\\sigma) = 2\\eta(1 + \\sigma) \\implies \\sigma = \\frac{3K - 2\\eta}{6K + 2\\eta}$$\n  Eliminating $\\sigma$ yields the harmonic relation:\n  $$\\frac{9}{Y} = \\frac{3}{\\eta} + \\frac{1}{K}$$\n  </li>\n</ol>\n\n<h4>2. Theoretical Limits of Poisson's Ratio</h4>\nBecause physical materials require positive strain energy under any deformation:\n$$K > 0 \\implies 1 - 2\\sigma > 0 \\implies \\sigma < \\frac{1}{2}$$\n$$\\eta > 0 \\implies 1 + \\sigma > 0 \\implies \\sigma > -1$$\n<blockquote>\n<strong>Theoretical Range of Poisson's Ratio:</strong>\n$$-1 \\le \\sigma \\le +0.5$$\n</blockquote>\n<ul>\n  <li><strong>Incompressible Materials ($\\sigma = 0.5$):</strong> Volume does not change under stress ($\\Delta V = 0 \\implies K \\to \\infty$). Examples: Rubber, water.</li>\n  <li><strong>Typical Metals ($\\sigma \\approx 0.25 - 0.35$):</strong> Volume expands under tension. Steel ($\\sigma = 0.29$), Aluminum ($\\sigma = 0.33$).</li>\n  <li><strong>Cork ($\\sigma \\approx 0$):</strong> Lateral dimension does not change when compressed (why wine bottle corks can be pushed in easily!).</li>\n  <li><strong>Auxetic Materials ($\\sigma < 0$):</strong> Expand laterally when stretched. Synthetic cellular foam polymers, biological tendon tissues.</li>\n</ul>"
        },
        {
          "id": "sec-2-8",
          "number": "\u00a72.8",
          "heading": "Torsion of a Cylinder and Torsional Pendulum",
          "simulation": "cantilever-bending-sim",
          "content": "When a torque is applied to one end of a solid cylinder or wire while the opposite end is clamped, the cylinder is subjected to **pure torsional shear**.\n\n<h4>1. Angle of Twist and Shear Strain</h4>\nConsider a solid cylinder of radius $R$ and length $L$, fixed at one end. A torque $\\tau$ applied to the free end twists it through an **angle of twist** $\\theta$.\nAn element at distance $r$ from the central axis is displaced along the circumference by arc length $s = r\\theta$.\nThe shear strain at radius $r$ is:\n$$\\phi(r) = \\frac{s}{L} = \\frac{r\\theta}{L}$$\nBy Hooke's law, the shear stress developed at radius $r$ is:\n$$\\tau(r) = \\eta \\, \\phi(r) = \\frac{\\eta r \\theta}{L}$$\nShear stress is zero at the central axis and reaches its maximum value $\\tau_{\\max} = \\frac{\\eta R \\theta}{L}$ at the outer perimeter.\n\n<h4>2. Derivation of the Restoring Torsional Couple</h4>\nDivide the cross section into thin concentric cylindrical shells of radius $r$ and thickness $dr$.\nThe area of a shell is $dA = 2\\pi r \\, dr$.\nThe shear force acting on this shell is:\n$$dF = \\tau(r) \\, dA = \\left( \\frac{\\eta r \\theta}{L} \\right) (2\\pi r \\, dr) = \\frac{2\\pi \\eta \\theta}{L} r^2 \\, dr$$\nThe torque about the cylinder axis produced by this shell is:\n$$dC = r \\, dF = \\frac{2\\pi \\eta \\theta}{L} r^3 \\, dr$$\nIntegrating over the entire cross section from $r = 0$ to $r = R$:\n$$C = \\frac{2\\pi \\eta \\theta}{L} \\int_0^R r^3 \\, dr = \\frac{2\\pi \\eta \\theta}{L} \\left( \\frac{R^4}{4} \\right) = \\frac{\\pi \\eta R^4}{2L} \\theta$$\nThe **Torsional Rigidity** (couple per unit angle of twist $c = C / \\theta$) is:\n$$c = \\frac{\\pi \\eta R^4}{2L}$$\nNotice the extreme sensitivity to radius ($c \\propto R^4$): doubling the wire thickness increases torsional stiffness by a factor of 16!\n\n<h4>3. The Torsional Pendulum</h4>\nA heavy disc of moment of inertia $I$ suspended from a wire of torsional rigidity $c$ oscillates according to:\n$$I \\ddot{\\theta} + c \\theta = 0 \\implies T = 2\\pi \\sqrt{\\frac{I}{c}} = 2\\pi \\sqrt{\\frac{2 I L}{\\pi \\eta R^4}}$$\nMeasuring $T$ allows high-precision experimental determination of the shear modulus $\\eta$."
        },
        {
          "id": "sec-2-9",
          "number": "\u00a72.9",
          "heading": "Helical Coil Springs and Effective Mass Correction",
          "simulation": "cantilever-bending-sim",
          "content": "A helical coil spring behaves primarily not through tension or bending of the wire, but through pure **torsional twisting** of the coiled wire cross section!\n\n<h4>1. Mechanics of Extension in a Helical Spring</h4>\nConsider a closely coiled helical spring made of wire of circular cross section of radius $r$, having $N$ turns of mean coil radius $R$, subjected to an axial tensile load $W$.\nAt any cross section of the wire:\n<ul>\n  <li>The axial force $W$ produces a twisting torque of magnitude:\n  $$\\tau = W R$$\n  </li>\n  <li>The total length of wire coiled into the spring is $L = 2\\pi R N$.</li>\n</ul>\nFrom the torsion formula, the angle of twist produced in the entire wire is:\n$$\\theta = \\frac{\\tau L}{c} = \\frac{(W R)(2\\pi R N)}{\\frac{1}{2}\\pi \\eta r^4} = \\frac{4 W R^2 N}{\\eta r^4}$$\nThe downward axial extension of the spring is:\n$$\\delta = R \\theta = \\frac{4 W R^3 N}{\\eta r^4}$$\nThe spring constant (stiffness) is:\n$$k = \\frac{W}{\\delta} = \\frac{\\eta r^4}{4 R^3 N}$$\n\n<h4>2. Dynamic Oscillation and Effective Spring Mass Correction</h4>\nWhen a mass $M$ is attached to the spring and set into vertical oscillation, the coils of the spring itself also move.\nA coil at fractional position $z/L$ from the fixed top oscillates with amplitude $\\frac{z}{L} v$.\nThe kinetic energy of the spring (of total mass $m_s$) is:\n$$K_{\\text{spring}} = \\int_0^L \\frac{1}{2} \\left(\\frac{m_s}{L} dz\\right) \\left( \\frac{z}{L} v \\right)^2 = \\frac{1}{2} m_s v^2 \\frac{1}{L^3} \\int_0^L z^2 dz = \\frac{1}{6} m_s v^2 = \\frac{1}{2} \\left(\\frac{m_s}{3}\\right) v^2$$\nThe spring contributes exactly **one-third of its own mass** to the oscillating inertia:\n$$M_{\\text{eff}} = M + \\frac{m_s}{3}$$\nThe exact period of oscillation is:\n$$T = 2\\pi \\sqrt{\\frac{M + m_s / 3}{k}} = 2\\pi \\sqrt{\\frac{4 R^3 N (M + m_s / 3)}{\\eta r^4}}$$"
        },
        {
          "id": "sec-2-10",
          "number": "\u00a72.10",
          "heading": "Bending of Beams and Cantilevers",
          "simulation": "cantilever-bending-sim",
          "content": "A **beam** is a structural member whose length is large compared to its lateral cross-sectional dimensions, designed to carry transverse mechanical loads.\n\n<h4>1. The Neutral Axis and Bending Moment</h4>\nWhen a horizontal beam is bent into a curve of radius of curvature $R$ by transverse forces:\n<ul>\n  <li>Filaments on the convex side are stretched in tension.</li>\n  <li>Filaments on the concave side are compressed.</li>\n  <li>A central surface exists where filaments experience zero strain and zero stress. This is the **Neutral Surface**, and its intersection with any cross section is the **Neutral Axis**.</li>\n</ul>\nAt distance $y$ from the neutral axis, strain is $\\epsilon = y / R$, and stress is $\\sigma = Y y / R$.\nThe resisting **Bending Moment** is:\n$$M = \\int \\sigma y \\, dA = \\frac{Y}{R} \\int y^2 \\, dA = \\frac{Y I_g}{R}$$\nwhere $I_g = \\int y^2 \\, dA$ is the **Geometric Moment of Inertia** of the cross section:\n<ul>\n  <li>For a rectangular beam of breadth $b$ and depth $d$: $I_g = \\frac{b d^3}{12}$</li>\n  <li>For a circular beam of radius $r$: $I_g = \\frac{\\pi r^4}{4}$</li>\n</ul>\n\n<h4>2. The Cantilever Loaded at the Free End</h4>\nA **cantilever** is a beam fixed horizontally at one end and loaded at the free end.\nFor a light cantilever of length $L$ loaded with weight $W$ at its free end:\nAt distance $x$ from the fixed support, the bending moment is $M(x) = W(L - x)$.\nThe differential equation of curvature is:\n$$Y I_g \\frac{d^2 y}{dx^2} = W (L - x)$$\nIntegrating with boundary conditions $y(0) = 0$ and $y'(0) = 0$:\n$$Y I_g \\frac{dy}{dx} = W \\left( L x - \\frac{x^2}{2} \\right)$$\n$$Y I_g y(x) = W \\left( \\frac{L x^2}{2} - \\frac{x^3}{6} \\right)$$\nAt the free end ($x = L$), the maximum depression is:\n$$\\delta = \\frac{W L^3}{3 Y I_g} = \\frac{4 W L^3}{Y b d^3}$$\nNotice that depression is inversely proportional to the cube of depth ($d^3$), explaining why engineering I-beams are oriented with their maximum depth vertically!"
        }
      ],
      "problems": [
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
    },
    {
      "number": 3,
      "title": "Hydrostatics and Surface Tension",
      "leadSummary": "Hydrostatic pressure, Pascal's law, thrust on submerged planes, center of pressure, floating body stability, surface tension, Young-Laplace equation, minimal surfaces, and Jurin's capillary law.",
      "sections": [
        {
          "id": "sec-3-1",
          "number": "\u00a73.1",
          "heading": "Hydrostatic Pressure and Variation with Elevation",
          "simulation": "capillary-bubble-sim",
          "content": "Hydrostatics studies fluids at rest. A fluid cannot sustain static shear stress; therefore, any force exerted by a static fluid on an adjacent boundary must act strictly normal to the surface.\n\n<h4>1. The Concept of Hydrostatic Pressure</h4>\nPressure $P$ at a point within a fluid is defined as the normal compressive force per unit area:\n$$P = \\lim_{\\Delta A \\to 0} \\frac{\\Delta F_\\perp}{\\Delta A}$$\nPressure is a scalar quantity, acting equally in all spatial directions at a given point.\n\n<h4>2. Variation of Pressure with Elevation</h4>\nConsider an infinitesimal cylindrical fluid element of cross-sectional area $A$ and height $dz$ in static equilibrium under gravity:\nThe vertical force balance is:\n$$P(z) A - P(z + dz) A - dm \\, g = 0$$\nSince $dm = \\rho A \\, dz$:\n$$-dP \\, A - \\rho g A \\, dz = 0 \\implies \\frac{dP}{dz} = -\\rho g$$\nThis is the **Fundamental Equation of Hydrostatics**:\n<ul>\n  <li><strong>Incompressible Liquids ($\\rho = \\text{constant}$):</strong> Integrating from surface $z = h$ to depth $z = 0$:\n  $$P(h) = P_0 + \\rho g h$$\n  where $P_0$ is surface atmospheric pressure. Pressure increases linearly with depth $h$.</li>\n  <li><strong>Compressible Isothermal Ideal Gas ($P = \\rho \\frac{R T}{M}$):</strong>\n  $$\\frac{dP}{dz} = -\\frac{M g}{R T} P \\implies P(z) = P_0 \\exp\\left( -\\frac{M g z}{R T} \\right)$$\n  This is the classical **Barometric Height Formula** for atmospheric pressure.</li>\n</ul>"
        },
        {
          "id": "sec-3-2",
          "number": "\u00a73.2",
          "heading": "Pascal's Law and the Hydrostatic Paradox",
          "simulation": "capillary-bubble-sim",
          "content": "Blaise Pascal (1653) established the foundational transmission law for fluids.\n\n<h4>1. Pascal's Law</h4>\n<blockquote>\nPressure applied to any point of an enclosed, incompressible fluid at rest is transmitted completely undiminished to every portion of the fluid and to the walls of the containing vessel.\n</blockquote>\n<strong>The Hydraulic Press:</strong>\nConsider two fluid cylinders with cross-sectional areas $A_1$ and $A_2$ connected by a pipe.\nA downward force $F_1$ on piston 1 produces pressure $P = F_1 / A_1$.\nBy Pascal's law, this identical pressure acts on piston 2, producing upward force:\n$$F_2 = P A_2 = F_1 \\left( \\frac{A_2}{A_1} \\right)$$\nThe mechanical advantage is $F_2 / F_1 = A_2 / A_1$.\nWork is conserved: $F_1 d_1 = F_2 d_2$.\n\n<h4>2. The Hydrostatic Paradox</h4>\nConsider three vessels of completely different shapes (e.g., conical, cylindrical, flared) having identical base areas $A$ and filled with liquid to the exact same vertical depth $h$.\nAlthough the vessels contain vastly different total weights of liquid, the downward force on the bottom of all three vessels is identical:\n$$F = P A = (\\rho g h) A$$\nThe discrepancy is resolved by recognizing that the inclined walls of the flared vessel exert an upward normal force supporting the extra liquid weight, while the walls of the conical vessel exert downward thrust on the fluid."
        },
        {
          "id": "sec-3-3",
          "number": "\u00a73.3",
          "heading": "Hydrostatic Thrust on Immersed Surfaces and Center of Pressure",
          "simulation": "capillary-bubble-sim",
          "content": "Engineers designing dams, submarine hulls, and floodgates must calculate not only the total hydrostatic force, but also its exact point of application.\n\n<h4>1. Total Hydrostatic Thrust on a Submerged Plane</h4>\nConsider a plane surface of area $A$ immersed in a liquid of density $\\rho$ at angle $\\theta$ to the horizontal.\nThe hydrostatic thrust on an infinitesimal strip of area $dA$ at depth $h$ is $dF = P dA = (\\rho g h) dA$.\nThe total thrust is:\n$$F = \\int_A \\rho g h \\, dA = \\rho g \\int_A h \\, dA = \\rho g \\bar{h} A = P_{\\text{cg}} A$$\nwhere $\\bar{h}$ is the vertical depth of the **Center of Gravity (CG)** of the area.\nThe total thrust equals the area multiplied by the pressure at its centroid.\n\n<h4>2. The Center of Pressure ($h_{\\text{cp}}$)</h4>\nThe **Center of Pressure (CP)** is the point on the surface where the single resultant force $F$ acts without producing any net rotational moment.\nTaking moments about the surface waterline axis:\n$$F \\, y_{\\text{cp}} = \\int_A y \\, dF = \\int_A y (\\rho g y \\sin\\theta) dA = \\rho g \\sin\\theta \\int_A y^2 dA = \\rho g \\sin\\theta \\, I_{xx,0}$$\nwhere $I_{xx,0} = I_{\\text{cg}} + A \\bar{y}^2$ is the second moment of area by the parallel axis theorem.\nDividing by $F = \\rho g \\sin\\theta \\bar{y} A$:\n$$y_{\\text{cp}} = \\bar{y} + \\frac{I_{\\text{cg}}}{\\bar{y} A} \\implies h_{\\text{cp}} = \\bar{h} + \\frac{I_{\\text{cg}} \\sin^2\\theta}{\\bar{h} A}$$\n<blockquote>\nBecause $I_{\\text{cg}} > 0$, the Center of Pressure is <strong>always located strictly below</strong> the Center of Gravity!\n</blockquote>\n\n<h4>3. Force and Overturning Moment on a Vertical Dam</h4>\nFor a vertical rectangular dam of width $W$ holding water of depth $H$:\n$$F = \\rho g \\left(\\frac{H}{2}\\right) (W H) = \\frac{1}{2} \\rho g W H^2$$\nThe center of pressure is located at:\n$$h_{\\text{cp}} = \\frac{H}{2} + \\frac{\\frac{1}{12} W H^3}{(H/2)(W H)} = \\frac{H}{2} + \\frac{H}{6} = \\frac{2}{3} H$$\nThe resultant thrust acts at one-third of the height from the bottom ($H/3$), generating an overturning moment $M = F (H/3) = \\frac{1}{6}\\rho g W H^3$."
        },
        {
          "id": "sec-3-4",
          "number": "\u00a73.4",
          "heading": "Equilibrium of Floating Bodies and Metacentric Stability",
          "simulation": "capillary-bubble-sim",
          "content": "Archimedes of Syracuse (250 BCE) established the fundamental principle of flotation:\n\n<h4>1. Archimedes' Principle</h4>\nA body wholly or partially submerged in a fluid experiences an upward buoyant force $F_b$ equal to the weight of the displaced fluid:\n$$F_b = \\rho_f V_{\\text{disp}} g$$\nThe buoyant force acts vertically upward through the **Center of Buoyancy ($B$)**, which is the centroid of the displaced fluid volume.\n\n<h4>2. Flotation Equilibrium</h4>\nFor a floating body of mass $M$ and total volume $V$:\n$$F_b = M g \\implies \\rho_f V_{\\text{disp}} g = \\rho_{\\text{body}} V g \\implies \\frac{V_{\\text{disp}}}{V} = \\frac{\\rho_{\\text{body}}}{\\rho_f}$$\n\n<h4>3. Rotational Stability of Ships: The Metacenter ($M$)</h4>\nWhen a floating vessel tilts through a small heel angle $\\theta$:\n<ul>\n  <li>The center of gravity $G$ of the ship remains fixed.</li>\n  <li>The submerged geometry changes, shifting the center of buoyancy from $B$ to a new position $B'$.</li>\n  <li>The vertical line of action of the buoyant force through $B'$ intersects the original vertical center line at point $M$, termed the **Metacenter**.</li>\n</ul>\nThe distance $GM$ is the **Metacentric Height**:\n$$GM = BM - BG = \\frac{I_{\\text{waterline}}}{V_{\\text{disp}}} - BG$$\nwhere $I_{\\text{waterline}}$ is the second moment of area of the ship's waterline plane.\n<ul>\n  <li><strong>Stable Equilibrium ($GM > 0$):</strong> $M$ lies above $G$. The buoyant force and gravity form a restoring righting couple $\\tau = M g (GM)\\sin\\theta$ that rights the ship.</li>\n  <li><strong>Unstable Equilibrium ($GM < 0$):</strong> $M$ lies below $G$. The couple capsizes the ship!</li>\n  <li><strong>Neutral Equilibrium ($GM = 0$):</strong> $M$ coincides with $G$.</li>\n</ul>"
        },
        {
          "id": "sec-3-5",
          "number": "\u00a73.5",
          "heading": "Pressure Gauges: Manometers and Barometers",
          "simulation": "capillary-bubble-sim",
          "content": "Hydrostatic pressure measurement relies on fluid column balancing.\n\n<h4>1. The Open U-Tube Manometer</h4>\nUsed to measure gauge pressure of a gas container relative to atmosphere.\nA U-tube contains a liquid of density $\\rho$. The difference in fluid column heights $h$ is:\n$$P_{\\text{gas}} - P_{\\text{atm}} = \\rho g h$$\n\n<h4>2. Differential Manometers</h4>\nUsed to measure the small pressure drop $\\Delta P = P_1 - P_2$ between two points in a pipeline:\n$$P_1 - P_2 = (\\rho_m - \\rho_f) g h$$\nwhere $\\rho_m$ is the manometer liquid density and $\\rho_f$ is the flowing fluid density.\n\n<h4>3. The Mercury Barometer</h4>\nEvangelista Torricelli (1643) invented the mercury barometer by filling a 1-meter tube with mercury and inverting it into a mercury basin.\nThe vacuum above the mercury column (Torricellian vacuum) has $P \\approx 0$.\nAtmospheric pressure balances the mercury column:\n$$P_{\\text{atm}} = \\rho_{\\text{Hg}} g h$$\nStandard atmospheric pressure:\n$$1\\text{ atm} = 760\\text{ mmHg} = (13,595\\text{ kg/m}^3)(9.80665\\text{ m/s}^2)(0.760\\text{ m}) = 101,325\\text{ Pa} = 1.01325\\text{ bar}$$"
        },
        {
          "id": "sec-3-6",
          "number": "\u00a73.6",
          "heading": "Surface Tension and Surface Free Energy",
          "simulation": "capillary-bubble-sim",
          "content": "Liquids behave as if their free surface were covered by a stretched elastic membrane under tension.\n\n<h4>1. Microscopic Molecular Origin</h4>\nIn the bulk of a liquid, each molecule experiences isotropic cohesive attraction from neighboring molecules in all directions, yielding zero net force.\nHowever, a molecule at the liquid-gas surface experiences strong downward cohesive attraction toward the liquid, but negligible attraction from vapor molecules above.\nTo bring a molecule from the interior to the surface requires doing positive mechanical work against this inward cohesive pull.\nThe surface of a liquid therefore possesses excess potential energy called **Surface Free Energy**.\n\n<h4>2. Mechanical Definition of Surface Tension</h4>\n**Surface Tension** ($\\gamma$ or $T$) is defined mechanically as the tangential tensile force acting perpendicularly across an imaginary line of unit length drawn in the liquid surface:\n$$\\gamma = \\frac{F}{L}$$\nIn SI units, surface tension is measured in Newtons per meter ($\\text{N/m}$) or Joules per square meter ($\\text{J/m}^2$).\nFor pure water at $20^\\circ\\text{C}$: $\\gamma = 0.0728\\text{ N/m}$. For mercury: $\\gamma = 0.486\\text{ N/m}$.\n\n<h4>3. Thermodynamic Equivalence</h4>\nThe work done to expand the surface area by $dA$ at constant temperature and composition is:\n$$dW = \\gamma \\, dA \\implies \\gamma = \\left(\\frac{\\partial F}{\\partial A}\\right)_{T, V}$$\nBecause physical systems spontaneously minimize their free energy, liquids naturally contract to minimize their surface area, forming spherical droplets!"
        },
        {
          "id": "sec-3-7",
          "number": "\u00a73.7",
          "heading": "Pressure Difference Across a Curved Surface: Young-Laplace Equation",
          "simulation": "capillary-bubble-sim",
          "content": "Because a curved liquid surface is under tension, the pressure on the concave side of the interface must always be greater than the pressure on the convex side.\n\n<h4>1. Excess Pressure Inside a Spherical Liquid Droplet</h4>\nConsider a spherical liquid droplet of radius $R$ and surface tension $\\gamma$.\nLet the internal pressure exceed external atmospheric pressure by $\\Delta P$.\nImagine dividing the droplet into two hemispheres:\nThe outward force attempting to separate the hemispheres across the diametral plane is:\n$$F_{\\text{pressure}} = \\Delta P \\times (\\pi R^2)$$\nThis force is balanced by the surface tension acting along the circular perimeter:\n$$F_{\\text{tension}} = \\gamma \\times (2\\pi R)$$\nIn equilibrium:\n$$\\Delta P (\\pi R^2) = 2\\pi R \\gamma \\implies \\Delta P = \\frac{2\\gamma}{R}$$\n\n<h4>2. Excess Pressure Inside a Soap Bubble</h4>\nA soap bubble has **two** spherical liquid-gas interfaces (an inner surface and an outer surface):\n$$\\Delta P = \\frac{4\\gamma}{R}$$\nThe excess pressure inside a bubble is inversely proportional to its radius ($P \\propto 1/R$).\nConsequently, a small soap bubble has higher internal pressure than a large bubble: if connected by a tube, the small bubble blows its air into the large bubble and collapses!\n\n<h4>3. The General Young-Laplace Equation</h4>\nFor an arbitrary curved interface characterized by principal orthogonal radii of curvature $R_1$ and $R_2$:\n$$\\Delta P = \\gamma \\left( \\frac{1}{R_1} + \\frac{1}{R_2} \\right) = 2 \\gamma H$$\nwhere $H = \\frac{1}{2}(1/R_1 + 1/R_2)$ is the **Mean Curvature** of the surface."
        },
        {
          "id": "sec-3-8",
          "number": "\u00a73.8",
          "heading": "Minimal Surfaces and Plateau's Laws",
          "simulation": "capillary-bubble-sim",
          "content": "In the absence of a pressure differential across the film ($\\Delta P = 0$), the Young-Laplace equation requires:\n$$H = \\frac{1}{2}\\left( \\frac{1}{R_1} + \\frac{1}{R_2} \\right) = 0 \\implies \\frac{1}{R_1} = -\\frac{1}{R_2}$$\nThe mean curvature must be zero everywhere: the surface is a **Minimal Surface** (a saddle surface with equal and opposite principal curvatures).\n\n<h4>1. Classic Minimal Surfaces</h4>\nJoseph Plateau (1873) investigated soap films suspended on wire frames:\n<ul>\n  <li><strong>Catenoid:</strong> The surface of revolution formed by rotating a catenary ($y = c\\cosh(x/c)$) around an axis; the only minimal surface of revolution.</li>\n  <li><strong>Helicoid:</strong> A screw-shaped minimal surface.</li>\n</ul>\n\n<h4>2. Plateau's Laws of Soap Films</h4>\nPlateau formulated empirical geometric laws governing soap bubble foam clusters:\n<ol>\n  <li>Soap films consist of smooth surfaces of constant mean curvature.</li>\n  <li>Exactly **three** soap film surfaces meet along a smooth line (called a *Plateau border*) at equal angles of strictly $120^\\circ$.</li>\n  <li>Exactly **four** Plateau borders meet at a vertex at the tetrahedral angle:\n  $$\\theta = \\arccos\\left(-\\frac{1}{3}\\right) \\approx 109.47^\\circ$$\n  </li>\n</ol>\nAny other configuration is kinematically unstable and spontaneously rearranges to satisfy these angles."
        },
        {
          "id": "sec-3-9",
          "number": "\u00a73.9",
          "heading": "Angle of Contact and Capillarity: Jurin's Law",
          "simulation": "capillary-bubble-sim",
          "content": "When a liquid meets a solid boundary, the interface forms a characteristic **Angle of Contact** $\\theta_c$.\n\n<h4>1. Young's Equation for Contact Angle</h4>\nAt the three-phase contact line where solid ($S$), liquid ($L$), and gas ($G$) meet, mechanical equilibrium requires balance of horizontal surface tension components:\n$$\\gamma_{SG} = \\gamma_{SL} + \\gamma_{LG} \\cos\\theta_c \\implies \\cos\\theta_c = \\frac{\\gamma_{SG} - \\gamma_{SL}}{\\gamma_{LG}}$$\n<ul>\n  <li><strong>Wetting Liquid ($\\theta_c < 90^\\circ$):</strong> Adhesive force between liquid and solid exceeds liquid cohesive force. Concave meniscus (e.g., pure water on clean glass: $\\theta_c \\approx 0^\\circ$).</li>\n  <li><strong>Non-Wetting Liquid ($\\theta_c > 90^\\circ$):</strong> Cohesion exceeds adhesion. Convex meniscus (e.g., mercury on glass: $\\theta_c \\approx 138^\\circ$).</li>\n</ul>\n\n<h4>2. Capillary Ascent: Jurin's Law (James Jurin, 1718)</h4>\nWhen a narrow glass capillary tube of radius $r$ is immersed vertically in a wetting liquid:\nThe upward vertical component of surface tension acting along the inner circumference $2\\pi r$ is:\n$$F_{\\text{up}} = 2\\pi r \\gamma \\cos\\theta_c$$\nThis lifts a column of liquid of height $h$ and mass $m = \\rho \\pi r^2 h$. The downward weight is:\n$$W = m g = \\pi r^2 h \\rho g$$\nEquating upward pull to downward weight:\n$$2\\pi r \\gamma \\cos\\theta_c = \\pi r^2 h \\rho g \\implies h = \\frac{2\\gamma \\cos\\theta_c}{\\rho g r}$$\n<blockquote>\n<strong>Jurin's Law:</strong> The height of capillary rise is inversely proportional to tube radius:\n$$h \\propto \\frac{1}{r}$$\n</blockquote>\nFor a non-wetting liquid like mercury ($\\cos\\theta_c < 0$), $h < 0$: the liquid is depressed below the external level."
        },
        {
          "id": "sec-3-10",
          "number": "\u00a73.10",
          "heading": "Experimental Determination of Surface Tension and Influencing Factors",
          "simulation": "capillary-bubble-sim",
          "content": "Various experimental techniques allow high-precision determination of $\\gamma$.\n\n<h4>1. Experimental Methods</h4>\n<ul>\n  <li><strong>Capillary Rise Method:</strong> Direct application of Jurin's law: $\\gamma = \\frac{\\rho g r h}{2 \\cos\\theta_c}$. Requires precision traveling microscope.</li>\n  <li><strong>Jaeger's Maximum Bubble Pressure Method:</strong> A capillary tube of radius $r$ is dipped to depth $h_1$ in the liquid. Air pressure is slowly increased to blow a bubble. The maximum pressure occurs when the bubble is hemispherical with radius equal to tube radius $r$:\n  $$P_{\\max} = P_0 + \\rho g h_1 + \\frac{2\\gamma}{r} \\implies \\gamma = \\frac{r}{2}(P_{\\max} - P_0 - \\rho g h_1)$$\n  Independent of contact angle $\\theta_c$!</li>\n  <li><strong>Rayleigh's Drop Weight Method:</strong> A liquid slowly drips from a tube of radius $r$. The weight $W$ of a detached droplet is:\n  $$W = 2\\pi r \\gamma f$$\n  where $f$ is Harkins-Brown correction factor ($f \\approx 0.60 - 0.65$).</li>\n</ul>\n\n<h4>2. Factors Influencing Surface Tension</h4>\n<ol>\n  <li><strong>Temperature:</strong> Thermal kinetic agitation weakens intermolecular cohesive bonds, decreasing $\\gamma$. According to the **E\u00f6tv\u00f6s Rule**:\n  $$\\gamma V_m^{2/3} = k_E (T_c - T)$$\n  Surface tension vanishes identically at the **Critical Temperature** $T_c$!</li>\n  <li><strong>Surfactants (Soaps, Detergents):</strong> Amphiphilic molecules concentrate at the surface, dramatically lowering $\\gamma$ from $73\\text{ mN/m}$ to $\\sim 25\\text{ mN/m}$.</li>\n  <li><strong>Dissolved Impurities:</strong> Highly soluble inorganic salts (NaCl) increase $\\gamma$ slightly by attracting water molecules into the bulk.</li>\n</ol>"
        }
      ],
      "problems": [
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
    },
    {
      "number": 4,
      "title": "Hydrodynamics and Viscosity",
      "leadSummary": "A rigorous hydrodynamic study of moving fluids, streamline flow, the continuity equation, Euler and Bernoulli equations with technical applications, viscous shear, Hagen-Poiseuille capillary flow, Stokes drag, and viscosity thermometry.",
      "sections": [
        {
          "id": "sec-4-1",
          "number": "\u00a74.1",
          "heading": "Lines and Tubes of Flow: Streamline and Turbulent Motion",
          "simulation": "hydro-pipe-flow-sim",
          "content": "Fluid dynamics investigates liquids and gases in motion. The velocity of a moving fluid at spatial coordinates $(x, y, z)$ and time $t$ is represented by the vector velocity field $\\vec{v}(x, y, z, t)$.\n\n<h4>1. Steady vs. Unsteady Flow</h4>\nA fluid flow is defined as <strong>steady</strong> (or stationary) if the velocity, pressure, and density at every fixed point in space remain constant with respect to time:\n$$\\frac{\\partial \\vec{v}}{\\partial t} = 0, \\quad \\frac{\\partial P}{\\partial t} = 0, \\quad \\frac{\\partial \\rho}{\\partial t} = 0$$\nIn steady flow, while individual fluid particles accelerate as they move along their trajectory, the spatial velocity field at any given geometric coordinate remains invariant. In unsteady flow, local time derivatives are non-zero.\n\n<h4>2. Streamlines, Pathlines, and Streaklines</h4>\n<ul>\n  <li><strong>Streamline:</strong> A continuous curve drawn through the fluid such that the tangent at every point coincides with the direction of the fluid velocity vector $\\vec{v}$ at that instant:\n  $$\\frac{dx}{v_x} = \\frac{dy}{v_y} = \\frac{dz}{v_z}$$\n  Because velocity is single-valued at any point, streamlines can never intersect.</li>\n  <li><strong>Pathline:</strong> The actual physical trajectory traced out by an individual moving fluid particle over time:\n  $$\\frac{d\\vec{r}}{dt} = \\vec{v}(\\vec{r}, t)$$</li>\n  <li><strong>Streakline:</strong> The instantaneous locus of all fluid particles that have passed sequentially through a specific fixed injection point (e.g., a dye filament in water or smoke in a wind tunnel).</li>\n</ul>\n<em>Fundamental Theorem:</em> In steady flow, streamlines, pathlines, and streaklines are completely identical.\n\n<h4>3. Tube of Flow (Streamtube)</h4>\nA tube of flow is an imaginary tubular surface formed by the bundle of streamlines passing through the perimeter of an arbitrary closed curve in the fluid.\nBecause velocity vectors are everywhere tangent to the surface of the streamtube, fluid can never cross the tubular boundary. Hence, a tube of flow behaves like an impermeable pipe.\n\n<h4>4. Laminar vs. Turbulent Flow and the Reynolds Number</h4>\nOsborne Reynolds (1883) demonstrated that fluid motion occurs in two distinct fundamental regimes:\n<ul>\n  <li><strong>Laminar Flow:</strong> Fluid moves smoothly in parallel layers (laminae) that slide past one another with minimal macroscopic mixing. Governed by viscous shear stresses.</li>\n  <li><strong>Turbulent Flow:</strong> Highly irregular, chaotic, unsteady flow characterized by macroscopic eddies, vortices, and rapid momentum dissipation.</li>\n</ul>\nThe transition between these regimes is governed by the dimensionless <strong>Reynolds Number ($Re$)</strong>:\n$$Re = \\frac{\\rho v D}{\\eta} = \\frac{v D}{\\nu}$$\nwhere $\\rho$ is fluid density, $v$ is mean flow speed, $D$ is characteristic conduit diameter (or object dimension), $\\eta$ is dynamic viscosity, and $\\nu = \\eta / \\rho$ is kinematic viscosity.\nPhysical interpretation: $Re$ represents the ratio of inertial forces to viscous forces:\n$$Re = \\frac{\\text{Inertial Force}}{\\text{Viscous Force}} \\sim \\frac{\\rho v^2 D^2}{\\eta v D} = \\frac{\\rho v D}{\\eta}$$\nFor internal pipe flow:\n<ul>\n  <li>$Re < 2000$: Laminar flow regime (stable).</li>\n  <li>$2000 \\le Re \\le 4000$: Transition regime.</li>\n  <li>$Re > 4000$: Fully turbulent flow regime.</li>\n</ul>"
        },
        {
          "id": "sec-4-2",
          "number": "\u00a74.2",
          "heading": "The Equation of Continuity",
          "simulation": "hydro-pipe-flow-sim",
          "content": "The equation of continuity is the mathematical expression of the fundamental law of <strong>conservation of mass</strong> applied to fluid flow.\n\n<h4>1. 1D Continuity for a Streamtube</h4>\nConsider steady flow through a tube of flow with non-uniform cross-sectional area.\nLet $A_1$ be the cross-sectional area, $\\rho_1$ the fluid density, and $v_1$ the flow speed at entry station 1.\nIn time increment $\\Delta t$, the fluid advances by length $\\Delta x_1 = v_1 \\Delta t$.\nThe volume entering station 1 is $\\Delta V_1 = A_1 v_1 \\Delta t$, and the entering mass is:\n$$\\Delta m_1 = \\rho_1 A_1 v_1 \\Delta t$$\nSimilarly, at exit station 2 with cross-sectional area $A_2$, density $\\rho_2$, and speed $v_2$, the mass leaving the tube is:\n$$\\Delta m_2 = \\rho_2 A_2 v_2 \\Delta t$$\nBecause no mass is created, destroyed, or leaks across the streamtube boundary, mass conservation demands $\\Delta m_1 = \\Delta m_2$:\n$$\\rho_1 A_1 v_1 = \\rho_2 A_2 v_2 = \\text{constant} = \\dot{m}$$\nwhere $\\dot{m} = \\frac{dm}{dt}$ is the <strong>mass flow rate</strong> (kg/s).\n\n<h4>2. Incompressible Fluid Flow</h4>\nFor liquids and subsonic gas flows where Mach number $M < 0.3$, density variations are negligible ($\\rho_1 = \\rho_2 = \\rho = \\text{constant}$). The equation simplifies to:\n$$A_1 v_1 = A_2 v_2 = \\text{constant} = Q$$\nwhere $Q = \\frac{dV}{dt} = A v$ is the <strong>volume flow rate</strong> (m\u00b3/s).\n<em>Physical Consequence:</em> Fluid speed is inversely proportional to cross-sectional area:\n$$v \\propto \\frac{1}{A}$$\nWhen a pipe constricts to half its diameter ($D_2 = D_1 / 2$), its area drops by a factor of 4 ($A_2 = A_1 / 4$), forcing the fluid speed to quadruple ($v_2 = 4 v_1$).\n\n<h4>3. General 3D Differential Form of Continuity</h4>\nFor an arbitrary differential control volume $dxdydz$ in space:\n$$\\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot (\\rho \\vec{v}) = 0$$\n$$\\frac{\\partial \\rho}{\\partial t} + \\frac{\\partial (\\rho v_x)}{\\partial x} + \\frac{\\partial (\\rho v_y)}{\\partial y} + \\frac{\\partial (\\rho v_z)}{\\partial z} = 0$$\nFor steady incompressible flow ($\\frac{\\partial \\rho}{\\partial t} = 0$ and $\\rho = \\text{constant}$):\n$$\\nabla \\cdot \\vec{v} = 0$$\nThis solenoidal condition guarantees zero divergence of the velocity field in incompressible hydrodynamics."
        },
        {
          "id": "sec-4-3",
          "number": "\u00a74.3",
          "heading": "Euler's Equation of Motion and Bernoulli's Theorem",
          "simulation": "venturi-bernoulli-sim",
          "content": "Bernoulli's theorem, formulated by Daniel Bernoulli in 1738, is the statement of the work-energy theorem for ideal fluid flow.\n\n<h4>1. Assumptions of Ideal Flow</h4>\nBernoulli's equation applies strictly under four idealizing assumptions:\n<ol>\n  <li><strong>Inviscid:</strong> Zero internal friction / zero viscosity ($\\eta = 0$).</li>\n  <li><strong>Incompressible:</strong> Constant fluid density ($\\rho = \\text{constant}$).</li>\n  <li><strong>Steady:</strong> Flow parameters do not change with time ($\\partial \\vec{v}/\\partial t = 0$).</li>\n  <li><strong>Irrotational:</strong> Fluid elements possess zero angular velocity ($\nabla \\times \\vec{v} = 0$).</li>\n</ol>\n\n<h4>2. Derivation from Euler's Equation along a Streamline</h4>\nConsider a fluid parcel of cross-section $dA$ and length $ds$ moving along an inclined streamline at angle $\\theta$ to the horizontal.\nNewton's second law along the streamline coordinate $s$ is:\n$$dF_s = dm \\, a_s$$\nThe forces acting along $s$ are the pressure forces on the ends and the tangential component of gravity:\n$$dF_s = P \\, dA - (P + dP) \\, dA - dm \\, g \\sin\\theta$$\nSince $dm = \\rho \\, dA \\, ds$ and $\\sin\\theta = \\frac{dz}{ds}$:\n$$-dP \\, dA - \\rho g \\, dA \\, dz = (\\rho \\, dA \\, ds) \\left( v \\frac{dv}{ds} \\right)$$\nDividing through by $\\rho \\, dA$:\n$$-\\frac{dP}{\\rho} - g \\, dz = v \\, dv$$\n$$\\frac{dP}{\\rho} + v \\, dv + g \\, dz = 0$$\nThis is <strong>Euler's 1D equation of motion</strong> along a streamline.\n\n<h4>3. Integration to Bernoulli's Equation</h4>\nIntegrating along the streamline from point 1 to point 2 for constant density $\\rho$:\n$$\\int_{P_1}^{P_2} \\frac{dP}{\\rho} + \\int_{v_1}^{v_2} v \\, dv + \\int_{z_1}^{z_2} g \\, dz = 0$$\n$$\\frac{P}{\\rho} + \\frac{1}{2}v^2 + gz = \\text{constant}$$\nMultiplying by $\\rho$:\n$$P + \\frac{1}{2}\\rho v^2 + \\rho g z = \\text{constant}$$\nEach term represents an energy density (Joules per cubic meter, or Pascals):\n<ul>\n  <li>$P$: <strong>Static Pressure</strong> (internal thermodynamic compressive stress).</li>\n  <li>$\\frac{1}{2}\\rho v^2$: <strong>Dynamic Pressure</strong> (kinetic energy per unit volume).</li>\n  <li>$\\rho g z$: <strong>Hydrostatic Pressure</strong> (gravitational potential energy per unit volume).</li>\n  <li>$P_0 = P + \\frac{1}{2}\\rho v^2$: <strong>Stagnation (Total) Pressure</strong> along a horizontal streamline ($z = \\text{const}$).</li>\n</ul>\nDividing by $\\rho g$ yields the expression in terms of hydraulic heads (meters of fluid column):\n$$\\frac{P}{\\rho g} + \\frac{v^2}{2g} + z = H = \\text{constant Head}$$\nwhere $\\frac{P}{\\rho g}$ is pressure head, $\\frac{v^2}{2g}$ is velocity head, and $z$ is elevation head."
        },
        {
          "id": "sec-4-4",
          "number": "\u00a74.4",
          "heading": "Applications of Bernoulli's Equation: Venturi Meter, Pitot Tube, and Torricelli's Law",
          "simulation": "venturi-bernoulli-sim",
          "content": "Bernoulli's theorem provides the theoretical foundation for major fluid measurement instruments and drainage systems.\n\n<h4>1. The Venturi Meter</h4>\nA Venturi meter measures the volume flow rate $Q$ of liquid through a pipeline without moving parts.\nIt consists of a converging nozzle of inlet area $A_1$, a narrow throat of area $A_2 < A_1$, and a gradual diffuser to prevent turbulence.\nBy continuity for horizontal flow ($z_1 = z_2$):\n$$v_1 = \\frac{Q}{A_1}, \\quad v_2 = \\frac{Q}{A_2} = \\frac{A_1}{A_2} v_1$$\nApplying Bernoulli's equation between inlet and throat:\n$$P_1 + \\frac{1}{2}\\rho v_1^2 = P_2 + \\frac{1}{2}\\rho v_2^2$$\n$$P_1 - P_2 = \\frac{1}{2}\\rho (v_2^2 - v_1^2) = \\frac{1}{2}\\rho v_1^2 \\left[ \\left(\\frac{A_1}{A_2}\\right)^2 - 1 \\right]$$\nA differential U-tube manometer containing liquid of density $\\rho_m$ connected between stations indicates height difference $h$:\n$$P_1 - P_2 = (\\rho_m - \\rho) g h$$\nEquating expressions yields the theoretical velocity at station 1:\n$$v_1 = \\sqrt{ \\frac{2(\\rho_m - \\rho) g h}{\\rho \\left[ (A_1 / A_2)^2 - 1 \\right]} }$$\nThe actual volumetric flow rate incorporates a discharge coefficient $C_d \\approx 0.96 - 0.98$ to account for minor viscous losses:\n$$Q = C_d A_1 A_2 \\sqrt{ \\frac{2(\\rho_m - \\rho) g h}{\\rho (A_1^2 - A_2^2)} }$$\n\n<h4>2. The Pitot-Static Tube</h4>\nInvented by Henri Pitot (1732) and modified by Henry Darcy, the Pitot-static tube measures fluid flow speed (used on aircraft airspeed indicators and in wind tunnels).\n<ul>\n  <li><strong>Static tap:</strong> Aligned flush with the outer wall parallel to streamlines, measuring purely static pressure $P$.</li>\n  <li><strong>Stagnation tap:</strong> Faces directly into the oncoming flow. At the probe tip, oncoming fluid is brought to complete rest ($v_{stag} = 0$).</li>\n</ul>\nApplying Bernoulli's equation between free stream and stagnation point:\n$$P + \\frac{1}{2}\\rho v^2 = P_{stag} + 0 \\implies P_{stag} - P = \\frac{1}{2}\\rho v^2$$\nMeasuring the differential pressure $\\Delta P = P_{stag} - P$:\n$$v = \\sqrt{\\frac{2 \\Delta P}{\\rho}} = \\sqrt{\\frac{2 \\rho_m g h}{\\rho}}$$\n\n<h4>3. Torricelli's Law of Efflux</h4>\nEvangelista Torricelli (1643) studied liquid discharge from an orifice of area $a$ at depth $h$ below the free surface of an open tank of cross-sectional area $A$.\nBoth the tank free surface and the orifice exit jet are open to atmospheric pressure ($P_1 = P_2 = P_{atm}$).\nBernoulli's equation:\n$$P_{atm} + \\frac{1}{2}\\rho v_1^2 + \\rho g h = P_{atm} + \\frac{1}{2}\\rho v_2^2 + 0$$\nUsing continuity $A v_1 = a v_2 \\implies v_1 = (a / A) v_2$:\n$$gh = \\frac{1}{2}v_2^2 \\left( 1 - \\frac{a^2}{A^2} \\right) \\implies v_2 = \\sqrt{ \\frac{2gh}{1 - (a/A)^2} }$$\nWhen the tank is large compared to the orifice ($A \\gg a$):\n$$v_2 = \\sqrt{2gh}$$\n<em>Torricelli's Theorem:</em> The efflux velocity of liquid issuing under gravity from an orifice equals the speed acquired by a body falling freely from rest through height $h$.\nThe actual jet contracts to area $A_{jet} = C_c a$ where $C_c \\approx 0.62$ is the coefficient of contraction (vena contracta)."
        },
        {
          "id": "sec-4-5",
          "number": "\u00a74.5",
          "heading": "Flow in a Curved Duct and Vortex Motion",
          "simulation": "hydro-pipe-flow-sim",
          "content": "When streamlines curve, fluid elements undergo centripetal acceleration, which requires a transverse pressure gradient directed toward the center of curvature.\n\n<h4>1. Transverse Pressure Gradient</h4>\nConsider a fluid parcel of width $dr$, length $ds$, and unit depth following a circular streamline of radius of curvature $r$ with speed $v$.\nThe centripetal force required to maintain circular trajectory is:\n$$dF_r = dm \\, \\frac{v^2}{r} = (\\rho \\, dr \\, ds) \\frac{v^2}{r}$$\nThis radial force is supplied by the net normal pressure difference across the parcel:\n$$(P + dP) \\, ds - P \\, ds = dP \\, ds$$\nEquating:\n$$dP \\, ds = \\rho \\, dr \\, ds \\, \\frac{v^2}{r} \\implies \\frac{\\partial P}{\\partial r} = \\frac{\\rho v^2}{r}$$\n<em>Conclusion:</em> Pressure always increases radially outward across curved streamlines ($\\frac{\\partial P}{\\partial r} > 0$).\nIn a curved pipe or duct:\n<ul>\n  <li>The outer wall experiences high pressure.</li>\n  <li>The inner bend experiences low pressure.</li>\n</ul>\n\n<h4>2. Free vs. Forced Vortices</h4>\n<ul>\n  <li><strong>Forced (Rotational) Vortex:</strong> Fluid rotates as a solid body with constant angular velocity $\\omega$ (e.g., liquid stirred in a beaker):\n  $$v(r) = \\omega r$$\n  $$\\frac{dP}{dr} = \\rho \\frac{(\\omega r)^2}{r} = \\rho \\omega^2 r \\implies P(r) = P(0) + \\frac{1}{2}\\rho \\omega^2 r^2$$\n  The free surface forms a paraboloid of revolution: $z(r) = \\frac{\\omega^2 r^2}{2g}$.\n  Vorticity is non-zero: $\\vec{\\omega} = \\nabla \\times \\vec{v} = 2\\omega \\hat{k} \\ne 0$.</li>\n  <li><strong>Free (Irrotational) Vortex:</strong> Fluid circulates without torque; angular momentum is conserved (e.g., bathtub drain, cyclone):\n  $$L = m v r = \\text{constant} \\implies v(r) = \\frac{\\Gamma}{2\\pi r}$$\n  where $\\Gamma = \\oint \\vec{v} \\cdot d\\vec{r}$ is circulation.\n  The vorticity is zero everywhere except at the singular origin: $\\nabla \\times \\vec{v} = 0$.\n  Applying Bernoulli's equation ($P + \\frac{1}{2}\\rho v^2 = P_\\infty$):\n  $$P(r) = P_\\infty - \\frac{1}{2}\\rho \\left(\\frac{\\Gamma}{2\\pi r}\\right)^2$$\n  Pressure drops sharply toward the vortex center, causing the core depression / funnel.</li>\n</ul>"
        },
        {
          "id": "sec-4-6",
          "number": "\u00a74.6",
          "heading": "Viscosity and Newton's Law of Viscous Shear",
          "simulation": "viscosity-stokes-sim",
          "content": "Real fluids exhibit internal friction termed <strong>viscosity</strong>, which dissipates mechanical kinetic energy into internal thermal energy.\n\n<h4>1. Physical Mechanism of Viscosity</h4>\nWhen adjacent fluid layers move at different velocities, momentum is exchanged across the interface:\n<ul>\n  <li>In <strong>gases</strong>, random molecular thermal motion carries high-speed x-momentum molecules into slower layers and vice versa. Viscosity arises from molecular transport.</li>\n  <li>In <strong>liquids</strong>, viscosity arises primarily from cohesive intermolecular forces (van der Waals, hydrogen bonding) between adjacent molecular layers sliding past one another.</li>\n</ul>\n\n<h4>2. Newton's Law of Viscosity</h4>\nConsider liquid confined between two parallel plates separated by distance $h$. The lower plate is fixed, and the upper plate moves with constant velocity $U$.\nFluid in direct contact with solid boundaries adheres without slipping (the <strong>no-slip boundary condition</strong>):\n$$v(y=0) = 0, \\quad v(y=h) = U$$\nThe fluid establishes a linear velocity profile $v_x(y) = U y / h$.\nSir Isaac Newton postulated that the tangential shear stress $\\tau$ between adjacent liquid layers is directly proportional to the transverse velocity gradient $\\frac{dv_x}{dy}$:\n$$\\tau = \\frac{F}{A} = \\eta \\frac{dv_x}{dy}$$\nwhere:\n<ul>\n  <li>$\\tau = F/A$ is shear stress (N/m\u00b2 or Pa).</li>\n  <li>$\\frac{dv_x}{dy}$ is the rate of shear strain (s\u207b\u00b9).</li>\n  <li>$\\eta$ is the <strong>dynamic coefficient of viscosity</strong> (Pa\u00b7s or $\\text{kg}/(\\text{m}\\cdot\\text{s})$).</li>\n</ul>\n\n<h4>3. Units of Viscosity</h4>\n<ul>\n  <li><strong>Dynamic Viscosity ($\\eta$):</strong>\n  <ul>\n    <li>SI Unit: $\\text{Pa}\\cdot\\text{s} = \\text{N}\\cdot\\text{s}/\\text{m}^2 = \\text{kg}/(\\text{m}\\cdot\\text{s})$.</li>\n    <li>CGS Unit: Poise ($\\text{P}$) where $1 \\text{ P} = 0.1 \\text{ Pa}\\cdot\\text{s} = 1 \\text{ dyne}\\cdot\\text{s}/\\text{cm}^2$.</li>\n    <li>Centipoise: $1 \\text{ cP} = 10^{-2} \\text{ P} = 10^{-3} \\text{ Pa}\\cdot\\text{s}$. (Water at 20\u00b0C has $\\eta \\approx 1.002 \\text{ cP} \\approx 1.002 \\times 10^{-3} \\text{ Pa}\\cdot\\text{s}$).</li>\n  </ul></li>\n  <li><strong>Kinematic Viscosity ($\nu$):</strong>\n  $$\\nu = \\frac{\\eta}{\\rho}$$\n  <ul>\n    <li>SI Unit: $\\text{m}^2/\\text{s}$.</li>\n    <li>CGS Unit: Stokes ($\\text{St}$) where $1 \\text{ St} = 1 \\text{ cm}^2/\\text{s} = 10^{-4} \\text{ m}^2/\\text{s}$.</li>\n    <li>Centistokes: $1 \\text{ cSt} = 10^{-6} \\text{ m}^2/\\text{s}$.</li>\n  </ul></li>\n</ul>"
        },
        {
          "id": "sec-4-7",
          "number": "\u00a74.7",
          "heading": "Poiseuille's Law: Laminar Flow through a Capillary Tube",
          "simulation": "viscosity-stokes-sim",
          "content": "Jean L\u00e9onard Marie Poiseuille (1840) experimentally derived, and Gotthilf Hagen theoretically proved, the law governing steady laminar flow of a viscous incompressible fluid through a cylindrical capillary tube of radius $R$ and length $L$.\n\n<h4>1. Velocity Distribution Derivation</h4>\nConsider a coaxial cylindrical fluid element of radius $r$ and length $L$ inside a tube of internal radius $R$.\nThe net pressure force driving the element forward is:\n$$F_P = \\Delta P \\cdot (\\pi r^2) = (P_1 - P_2) \\pi r^2$$\nThe opposing viscous retarding force acting on the outer cylindrical surface of area $2\\pi r L$ is:\n$$F_\\eta = -\\eta (2\\pi r L) \\frac{dv}{dr}$$\nIn steady, non-accelerating flow, force equilibrium requires:\n$$\\Delta P \\pi r^2 + 2\\pi r L \\eta \\frac{dv}{dr} = 0$$\n$$\\frac{dv}{dr} = -\\frac{\\Delta P}{2\\eta L} r$$\nIntegrating with respect to $r$:\n$$v(r) = -\\frac{\\Delta P}{4\\eta L} r^2 + C$$\nApplying the <strong>no-slip boundary condition</strong> at the tube wall: $v(R) = 0$:\n$$0 = -\\frac{\\Delta P}{4\\eta L} R^2 + C \\implies C = \\frac{\\Delta P}{4\\eta L} R^2$$\nThus, the velocity distribution is a <strong>paraboloid of revolution</strong>:\n$$v(r) = \\frac{\\Delta P}{4\\eta L} (R^2 - r^2)$$\nMaximum velocity occurs at the central axis ($r = 0$):\n$$v_{max} = \\frac{\\Delta P R^2}{4\\eta L}$$\n\n<h4>2. Total Volume Flow Rate ($Q$)</h4>\nThe volumetric flow $dQ$ passing through an infinitesimal annular ring between radii $r$ and $r + dr$ is:\n$$dQ = v(r) \\cdot (2\\pi r \\, dr) = \\frac{\\pi \\Delta P}{2\\eta L} (R^2 - r^2) r \\, dr$$\nIntegrating across the entire tube from $r = 0$ to $r = R$:\n$$Q = \\int_0^R dQ = \\frac{\\pi \\Delta P}{2\\eta L} \\int_0^R (R^2 r - r^3) dr = \\frac{\\pi \\Delta P}{2\\eta L} \\left[ \\frac{R^2 r^2}{2} - \\frac{r^4}{4} \\right]_0^R$$\n$$Q = \\frac{\\pi \\Delta P}{2\\eta L} \\left( \\frac{R^4}{4} \\right) = \\frac{\\pi \\Delta P R^4}{8 \\eta L}$$\nThis is the celebrated <strong>Hagen-Poiseuille Equation</strong>.\n\n<h4>3. Hydraulic Resistance and Fourth-Power Dependence</h4>\nAnalogous to Ohm's law ($I = \\Delta V / R_{elec}$), the volumetric flow is:\n$$Q = \\frac{\\Delta P}{R_H}, \\quad \\text{where } R_H = \\frac{8 \\eta L}{\\pi R^4}$$\n$R_H$ is the <strong>hydraulic resistance</strong>.\nBecause $Q \\propto R^4$, even a minuscule reduction in radius dramatically curtails flow. For example:\n<ul>\n  <li>If an artery suffers a 19% luminal diameter constriction ($R \\to 0.81 R$), the flow rate drops by $(0.81)^4 \\approx 0.43$, cutting blood perfusion by 57%!</li>\n</ul>\nMean flow velocity is exactly half the maximum centerline velocity:\n$$\\bar{v} = \\frac{Q}{\\pi R^2} = \\frac{\\Delta P R^2}{8\\eta L} = \\frac{1}{2} v_{max}$$"
        },
        {
          "id": "sec-4-8",
          "number": "\u00a74.8",
          "heading": "Stokes' Law and Terminal Velocity",
          "simulation": "viscosity-stokes-sim",
          "content": "Sir George Gabriel Stokes (1851) solved the Navier-Stokes equations for low Reynolds number creep flow ($Re \\ll 1$) past a smooth spherical body of radius $r$.\n\n<h4>1. Derivation by Dimensional Analysis</h4>\nAssume the viscous retarding force $F_d$ on a sphere depends on:\n$$F_d \\propto \\eta^a r^b v^c$$\nWriting dimensional formulas ($[F] = M L T^{-2}$, $[\\eta] = M L^{-1} T^{-1}$, $[r] = L$, $[v] = L T^{-1}$):\n$$M L T^{-2} = (M L^{-1} T^{-1})^a (L)^b (L T^{-1})^c = M^a L^{-a + b + c} T^{-a - c}$$\nEquating powers:\n<ul>\n  <li>Mass ($M$): $a = 1$</li>\n  <li>Time ($T$): $-a - c = -2 \\implies c = 2 - a = 1$</li>\n  <li>Length ($L$): $-a + b + c = 1 \\implies -1 + b + 1 = 1 \\implies b = 1$</li>\n</ul>\nThus $F_d \\propto \\eta r v$. Stokes' full hydrodynamic boundary-value solution determines the dimensionless coefficient to be exactly $6\\pi$:\n$$F_d = 6\\pi \\eta r v$$\nThis is <strong>Stokes' Law</strong>. (Of the total drag, $4\\pi \\eta r v$ originates from viscous skin friction and $2\\pi \\eta r v$ from pressure/form drag).\n\n<h4>2. Motion of a Falling Sphere and Terminal Velocity</h4>\nConsider a solid sphere of radius $r$ and density $\\rho$ falling vertically under gravity through a viscous fluid of density $\\sigma < \\rho$.\nThree forces act on the body:\n<ol>\n  <li>Downward gravity (weight): $W = mg = \\frac{4}{3}\\pi r^3 \\rho g$</li>\n  <li>Upward buoyant force (Archimedes' thrust): $F_B = \\frac{4}{3}\\pi r^3 \\sigma g$</li>\n  <li>Upward viscous drag (Stokes retarding force): $F_d = 6\\pi \\eta r v$</li>\n</ol>\nThe equation of motion is:\n$$m \\frac{dv}{dt} = W - F_B - F_d$$\n$$\\frac{4}{3}\\pi r^3 \\rho \\frac{dv}{dt} = \\frac{4}{3}\\pi r^3 (\\rho - \\sigma) g - 6\\pi \\eta r v$$\nAs velocity $v$ increases, viscous drag $F_d$ grows until the upward forces precisely balance the weight. Acceleration ceases ($\\frac{dv}{dt} = 0$), and the sphere attains a constant <strong>terminal velocity ($v_t$)</strong>:\n$$6\\pi \\eta r v_t = \\frac{4}{3}\\pi r^3 (\\rho - \\sigma) g$$\n$$v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}$$\nNotice that terminal speed scales with $r^2$. Fine mist droplets ($r \\sim 10 \\ \\mu\\text{m}$) fall at millimeters per second, remaining suspended in clouds for hours."
        },
        {
          "id": "sec-4-9",
          "number": "\u00a74.9",
          "heading": "Experimental Determination of Viscosity and Temperature Variation",
          "simulation": "viscosity-stokes-sim",
          "content": "Accurate measurement of viscosity is vital in physical chemistry, chemical engineering, and aerodynamics.\n\n<h4>1. Experimental Methods</h4>\n<ul>\n  <li><strong>Poiseuille's Capillary Viscometer:</strong> Liquid drains under a known hydrostatic head $h$ through a precision capillary tube of radius $R$ and length $L$. By measuring efflux time $t$ for known volume $V$:\n  $$\\eta = \\frac{\\pi \\bar{P} R^4 t}{8 V L} = \\frac{\\pi \\rho g \\bar{h} R^4 t}{8 V L}$$\n  Kinetic energy end corrections (Couette correction: $L_{eff} = L + m R$) must be applied for short tubes.</li>\n  <li><strong>Ostwald Relative Viscometer:</strong> Compares flow time $t_1$ of test liquid of density $\\rho_1$ to flow time $t_2$ of reference liquid (distilled water, $\\rho_2, \\eta_2$) through the same capillary:\n  $$\\frac{\\eta_1}{\\eta_2} = \\frac{\\rho_1 t_1}{\\rho_2 t_2}$$\n  Eliminates tedious calibration of capillary radius $R$.</li>\n  <li><strong>Stokes' Falling Sphere Viscometer:</strong> A small steel ball is timed falling between two fiducial marks separated by vertical distance $h$ in a wide glass cylinder filled with viscous liquid:\n  $$\\eta = \\frac{2 r^2 (\\rho - \\sigma) g t}{9 h} \\cdot \\frac{1}{1 + 2.4 (r / R_{cyl})}$$\n  The Ladenburg wall correction factor $\\frac{1}{1 + 2.4(r/R_{cyl})}$ accounts for the retarding effect of the cylinder walls.</li>\n</ul>\n\n<h4>2. Variation of Viscosity with Temperature</h4>\nViscosity exhibits fundamentally opposite temperature dependencies in liquids versus gases:\n<ul>\n  <li><strong>Liquids:</strong> As temperature rises, molecular thermal agitation expands the intermolecular spacing, weakening attractive van der Waals bonds. Consequently, liquid viscosity drops exponentially with temperature, described by <strong>Andrade's Equation</strong>:\n  $$\\eta(T) = A e^{E_a / (R T)}$$\n  where $E_a$ is the activation energy for viscous shear flow. Water viscosity decreases from $1.79 \\text{ cP}$ at 0\u00b0C to $0.28 \\text{ cP}$ at 100\u00b0C.</li>\n  <li><strong>Gases:</strong> Kinetic theory dictates that gas viscosity is governed by momentum transport via molecular collisions:\n  $$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda = \\frac{2}{3\\pi^{3/2}} \\frac{\\sqrt{m k_B T}}{d^2}$$\n  Because mean molecular speed $\\bar{v} \\propto \\sqrt{T}$, gas viscosity increases with temperature!\n  Accounting for intermolecular attraction leads to <strong>Sutherland's Formula</strong>:\n  $$\\eta(T) = \\eta_0 \\left(\\frac{T}{T_0}\\right)^{3/2} \\frac{T_0 + C}{T + C}$$\n  where $C$ is Sutherland's constant for the gas.</li>\n</ul>"
        }
      ],
      "problems": [
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
              "explanation": "The calculated dynamic viscosity is 0.258 Pa\u00b7s (258 cP), characteristic of refined castor oil."
            },
            {
              "title": "Step 3: Verification of Reynolds number criterion",
              "math": "$$Re = \\frac{\\sigma v_t (2r)}{\\eta} = \\frac{960 \\times 0.08772 \\times (2.00 \\times 10^{-3})}{0.2577} = \\frac{0.1684}{0.2577} = 0.653$$",
              "explanation": "With Re ~ 0.65, inertial corrections are minor (Oseen correction adds ~ (1 + 3/8 Re) = 1.24 factor), validating Stokes' viscous drag formulation to high accuracy."
            }
          ]
        }
      ]
    },
    {
      "number": 5,
      "title": "Oscillations",
      "leadSummary": "A comprehensive mathematical and physical treatment of harmonic motion, phase space representation, energy conservation, compound and torsion pendulums, orthogonal superposition and Lissajous figures, damped decay regimes, logarithmic decrement, Q-factor, and forced mechanical resonance.",
      "sections": [
        {
          "id": "sec-5-1",
          "number": "\u00a75.1",
          "heading": "Harmonic Motion and Simple Harmonic Motion (SHM)",
          "simulation": "shm-resonance-sim",
          "content": "Periodic motion is any motion that repeats itself identically at regular intervals of time $T$. Harmonic motion is periodic motion where the restoring mechanism is directly proportional to displacement.\n\n<h4>1. Definition and Kinematics of SHM</h4>\nA particle executes <strong>Simple Harmonic Motion (SHM)</strong> when the restoring force acting on it is directly proportional to its displacement from equilibrium and directed toward that equilibrium position:\n$$F = -k x$$\nwhere $k$ is the force constant (stiffness) in N/m. By Newton's second law ($F = m \\ddot{x}$):\n$$m \\frac{d^2 x}{dt^2} + k x = 0 \\implies \\frac{d^2 x}{dt^2} + \\omega_0^2 x = 0$$\nwhere $\\omega_0 = \\sqrt{k/m}$ is the <strong>natural undamped angular frequency</strong> (rad/s).\nThe general harmonic solution is:\n$$x(t) = A \\cos(\\omega_0 t + \\phi)$$\nwhere:\n<ul>\n  <li>$A$: <strong>Amplitude</strong> (maximum displacement from equilibrium).</li>\n  <li>$\\omega_0 = 2\\pi f = \\frac{2\\pi}{T}$: Angular frequency.</li>\n  <li>$\\phi$: <strong>Initial phase constant</strong> (determined by initial conditions $x(0)$ and $v(0)$).</li>\n  <li>$T = 2\\pi \\sqrt{\\frac{m}{k}}$: Period of oscillation (independent of amplitude \u2014 <em>isochronism</em>).</li>\n</ul>\n\n<h4>2. Velocity and Acceleration</h4>\nDifferentiating displacement with respect to time:\n$$v(t) = \\dot{x}(t) = -\\omega_0 A \\sin(\\omega_0 t + \\phi) = \\omega_0 A \\cos\\left(\\omega_0 t + \\phi + \\frac{\\pi}{2}\\right)$$\n$$a(t) = \\ddot{x}(t) = -\\omega_0^2 A \\cos(\\omega_0 t + \\phi) = -\\omega_0^2 x(t) = \\omega_0^2 A \\cos(\\omega_0 t + \\phi + \\pi)$$\nKey phase relationships:\n<ul>\n  <li>Velocity leads displacement by $\\frac{\\pi}{2}$ radians (90\u00b0). Maximum speed $v_{max} = \\omega_0 A$ occurs at equilibrium ($x = 0$).</li>\n  <li>Acceleration leads displacement by $\\pi$ radians (180\u00b0). Maximum acceleration $a_{max} = \\omega_0^2 A$ occurs at maximum displacement ($x = \\pm A$).</li>\n</ul>\nEliminating time between $x$ and $v$ yields the elliptical phase space trajectory:\n$$v(x) = \\pm \\omega_0 \\sqrt{A^2 - x^2} \\implies \\frac{x^2}{A^2} + \\frac{v^2}{\\omega_0^2 A^2} = 1$$"
        },
        {
          "id": "sec-5-2",
          "number": "\u00a75.2",
          "heading": "Energy Considerations in Simple Harmonic Motion",
          "simulation": "shm-resonance-sim",
          "content": "Simple harmonic motion is a conservative mechanical system where potential energy and kinetic energy continuously transform into one another while total mechanical energy remains invariant.\n\n<h4>1. Kinetic and Potential Energy</h4>\n<ul>\n  <li><strong>Kinetic Energy ($T$):</strong>\n  $$T(t) = \\frac{1}{2}m v^2 = \\frac{1}{2}m \\omega_0^2 A^2 \\sin^2(\\omega_0 t + \\phi) = \\frac{1}{2}k (A^2 - x^2)$$</li>\n  <li><strong>Potential Energy ($V$):</strong> Work done against the restoring force $F = -kx$:\n  $$V(x) = -\\int_0^x (-k x') dx' = \\frac{1}{2}k x^2 = \\frac{1}{2}k A^2 \\cos^2(\\omega_0 t + \\phi)$$</li>\n</ul>\n\n<h4>2. Conservation of Total Energy</h4>\nSumming kinetic and potential energies:\n$$E = T + V = \\frac{1}{2}k A^2 \\left[ \\sin^2(\\omega_0 t + \\phi) + \\cos^2(\\omega_0 t + \\phi) \\right] = \\frac{1}{2}k A^2 = \\frac{1}{2}m \\omega_0^2 A^2 = \\text{constant}$$\nThe total mechanical energy is proportional to the square of the amplitude and independent of time and position.\nAt the turning points ($x = \\pm A$), velocity vanishes, and energy is purely potential ($E = V_{max} = \\frac{1}{2}kA^2$).\nAt the equilibrium position ($x = 0$), potential energy vanishes, and energy is purely kinetic ($E = T_{max} = \\frac{1}{2}m v_{max}^2$).\n\n<h4>3. Time-Averaged Energies and the Virial Theorem</h4>\nAveraging over a complete oscillation period $T = 2\\pi / \\omega_0$:\n$$\\langle \\sin^2(\\omega_0 t + \\phi) \\rangle = \\frac{1}{T}\\int_0^T \\sin^2(\\omega_0 t + \\phi) dt = \\frac{1}{2}$$\n$$\\langle \\cos^2(\\omega_0 t + \\phi) \\rangle = \\frac{1}{2}$$\nTherefore:\n$$\\langle T \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2}E, \\quad \\langle V \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2}E$$\n$$\\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2}E$$\nThis exact equipartition of average kinetic and potential energy is a direct consequence of the <strong>Virial Theorem</strong> for harmonic potentials ($V \\propto x^2$)."
        },
        {
          "id": "sec-5-3",
          "number": "\u00a75.3",
          "heading": "Applications of SHM: Simple, Compound, and Torsion Pendulums",
          "simulation": "shm-resonance-sim",
          "content": "Simple harmonic motion governs a multitude of oscillating mechanical and structural devices.\n\n<h4>1. Simple Pendulum</h4>\nA point mass $m$ suspended by an inextensible massless string of length $L$.\nRestoring torque about suspension point $O$:\n$$\\tau = -m g L \\sin\\theta = I \\alpha = (m L^2) \\frac{d^2\\theta}{dt^2}$$\n$$\\frac{d^2\\theta}{dt^2} + \\frac{g}{L}\\sin\\theta = 0$$\nFor small angular displacements ($\\sin\\theta \\approx \\theta$ in radians):\n$$\\frac{d^2\\theta}{dt^2} + \\omega_0^2 \\theta = 0 \\implies \\omega_0 = \\sqrt{\\frac{g}{L}}, \\quad T = 2\\pi \\sqrt{\\frac{L}{g}}$$\n\n<h4>2. Compound (Physical) Pendulum</h4>\nA rigid body of arbitrary shape and mass $M$ free to oscillate in a vertical plane about a horizontal knife-edge axis $O$.\nLet $d$ be the distance from the pivot $O$ to the center of mass $G$, and $I$ the moment of inertia about $O$.\nBy the parallel axis theorem: $I = I_G + M d^2 = M (k_g^2 + d^2)$, where $k_g$ is the radius of gyration about $G$.\nThe restoring torque is:\n$$\\tau = -M g d \\sin\\theta \\approx -M g d \\theta$$\n$$I \\frac{d^2\\theta}{dt^2} + M g d \\theta = 0 \\implies \\frac{d^2\\theta}{dt^2} + \\left(\\frac{M g d}{I}\\right) \\theta = 0$$\nThe period of oscillation is:\n$$T = 2\\pi \\sqrt{\\frac{I}{M g d}} = 2\\pi \\sqrt{\\frac{k_g^2 + d^2}{g d}} = 2\\pi \\sqrt{\\frac{L_{eq}}{g}}$$\nwhere $L_{eq} = \\frac{k_g^2 + d^2}{d} = d + \\frac{k_g^2}{d}$ is the <strong>length of the equivalent simple pendulum</strong>.\n<ul>\n  <li><strong>Center of Oscillation ($O'$):</strong> A point lying along the line $OG$ at distance $L_{eq}$ from $O$.\n  If the body is suspended from $O'$, its period of oscillation is identical to that about $O$ (<em>Theorem of Reversibility</em>, exploited in Kater's reversible pendulum to determine $g$ with parts-per-million accuracy).</li>\n  <li><strong>Minimum Period:</strong> Minimizing $L_{eq}(d)$ with respect to $d$:\n  $$\\frac{dL_{eq}}{dd} = 1 - \\frac{k_g^2}{d^2} = 0 \\implies d = k_g$$\n  The minimum period occurs when the suspension point is at a distance equal to the radius of gyration: $T_{min} = 2\\pi \\sqrt{2 k_g / g}$.</li>\n</ul>\n\n<h4>3. Torsional Pendulum</h4>\nA disk or cylinder suspended by a thin elastic wire. Twisting by angle $\\theta$ creates a restoring torque $\\tau = -C \\theta$, where $C = \\frac{\\pi \\eta r^4}{2 L}$ is the torsional rigidity of the wire.\n$$I \\frac{d^2\\theta}{dt^2} + C \\theta = 0 \\implies T = 2\\pi \\sqrt{\\frac{I}{C}}$$"
        },
        {
          "id": "sec-5-4",
          "number": "\u00a75.4",
          "heading": "Relation between SHM and Uniform Circular Motion",
          "simulation": "shm-resonance-sim",
          "content": "Simple harmonic motion can be mathematically and visually understood as the one-dimensional orthogonal projection of uniform circular motion.\n\n<h4>1. The Reference Circle and Phasor Representation</h4>\nConsider a reference particle $P$ moving counterclockwise along a circle of radius $A$ (called the <strong>reference circle</strong>) with constant angular velocity $\\omega_0$.\nAt $t = 0$, the radius vector makes an angle $\\phi$ with the positive x-axis. At subsequent time $t$, the angle is $\\theta(t) = \\omega_0 t + \\phi$.\nProjecting point $P$ onto the horizontal x-axis yields point $Q$:\n$$x(t) = A \\cos(\\omega_0 t + \\phi)$$\nProjecting point $P$ onto the vertical y-axis yields point $Q'$:\n$$y(t) = A \\sin(\\omega_0 t + \\phi) = A \\cos\\left(\\omega_0 t + \\phi - \\frac{\\pi}{2}\\right)$$\nBoth projected points $Q$ and $Q'$ execute pure simple harmonic motion with amplitude $A$ and angular frequency $\\omega_0$, separated by a 90\u00b0 phase difference.\n\n<h4>2. Kinematic Projections</h4>\n<ul>\n  <li><strong>Velocity:</strong> The linear tangential speed of $P$ on the circle is $v_0 = \\omega_0 A$.\n  Its projection on the x-axis gives the SHM velocity:\n  $$v_x = -v_0 \\sin(\\omega_0 t + \\phi) = -\\omega_0 A \\sin(\\omega_0 t + \\phi)$$</li>\n  <li><strong>Acceleration:</strong> The centripetal acceleration of $P$ directed toward the center is $a_c = \\omega_0^2 A$.\n  Its projection on the x-axis gives the SHM acceleration:\n  $$a_x = -a_c \\cos(\\omega_0 t + \\phi) = -\\omega_0^2 x(t)$$</li>\n</ul>\nThis phasor technique enables geometric addition of multiple harmonic oscillations using planar vector addition."
        },
        {
          "id": "sec-5-5",
          "number": "\u00a75.5",
          "heading": "Superposition of Harmonic Motions and Lissajous Figures",
          "simulation": "shm-resonance-sim",
          "content": "When a particle is acted upon by two or more simultaneous harmonic restoring forces, its resultant trajectory is determined by the principle of superposition.\n\n<h4>1. Superposition of Two Collinear SHMs of Identical Frequency</h4>\nLet two collinear oscillations along the x-axis be:\n$$x_1(t) = A_1 \\cos(\\omega t + \\phi_1), \\quad x_2(t) = A_2 \\cos(\\omega t + \\phi_2)$$\nThe resultant displacement is $x(t) = x_1(t) + x_2(t) = A \\cos(\\omega t + \\Phi)$, where:\n$$A = \\sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \\cos(\\phi_2 - \\phi_1)}$$\n$$\\tan\\Phi = \\frac{A_1 \\sin\\phi_1 + A_2 \\sin\\phi_2}{A_1 \\cos\\phi_1 + A_2 \\cos\\phi_2}$$\n<ul>\n  <li>If in phase ($\\Delta\\phi = 2n\\pi$): $A = A_1 + A_2$ (Constructive).</li>\n  <li>If in antiphase ($\\Delta\\phi = (2n+1)\\pi$): $A = |A_1 - A_2|$ (Destructive).</li>\n</ul>\n\n<h4>2. Superposition of Two Mutually Perpendicular SHMs: Lissajous Figures</h4>\nConsider a particle subjected to two orthogonal oscillations:\n$$x(t) = A \\cos(\\omega_x t), \\quad y(t) = B \\cos(\\omega_y t + \\delta)$$\nThe resulting path $(x(t), y(t))$ in the 2D plane is called a <strong>Lissajous Figure</strong> (discovered by Jules Antoine Lissajous, 1857).\n\n<h5>Case A: Equal Frequencies ($\\omega_x = \\omega_y = \\omega$)</h5>\nExpanding $y(t)$:\n$$\\frac{y}{B} = \\cos(\\omega t)\\cos\\delta - \\sin(\\omega t)\\sin\\delta = \\frac{x}{A}\\cos\\delta - \\sqrt{1 - \\frac{x^2}{A^2}}\\sin\\delta$$\nRearranging and squaring:\n$$\\left(\\frac{y}{B} - \\frac{x}{A}\\cos\\delta\\right)^2 = \\left(1 - \\frac{x^2}{A^2}\\right)\\sin^2\\delta$$\n$$\\frac{x^2}{A^2} - \\frac{2 x y}{A B}\\cos\\delta + \\frac{y^2}{B^2} = \\sin^2\\delta$$\nThis is the general equation of an oblique ellipse bounded within the rectangle $[-A, A] \\times [-B, B]$:\n<ul>\n  <li>$\\delta = 0$: Straight line of positive slope $y = (B/A) x$.</li>\n  <li>$\\delta = \\pi/2$: Symmetrical upright ellipse $\\frac{x^2}{A^2} + \\frac{y^2}{B^2} = 1$ (circle if $A = B$).</li>\n  <li>$\\delta = \\pi$: Straight line of negative slope $y = -(B/A) x$.</li>\n  <li>$\\delta = 3\\pi/2$: Upright ellipse traced clockwise.</li>\n</ul>\n\n<h5>Case B: Frequency Ratio 1:2 ($\\omega_y = 2\\omega_x$)</h5>\n$$x = A \\cos(\\omega t), \\quad y = B \\cos(2\\omega t + \\delta)$$\nUsing $\\cos(2\\theta) = 2\\cos^2\\theta - 1$, when $\\delta = 0$:\n$$y = B [2(x/A)^2 - 1]$$\nThis forms a parabola! For arbitrary phase differences $\\delta$, the curve traces a figure-eight (lemniscate) or distorted loop.\nThe frequency ratio is determined experimentally by counting tangencies:\n$$\\frac{\\omega_x}{\\omega_y} = \\frac{\\text{Number of intersections with vertical line}}{\\text{Number of intersections with horizontal line}}$$"
        },
        {
          "id": "sec-5-6",
          "number": "\u00a75.6",
          "heading": "Damped Harmonic Motion and the Quality Factor",
          "simulation": "shm-resonance-sim",
          "content": "Real physical oscillators experience dissipative resistive forces (viscous drag, friction) that continually remove mechanical energy.\n\n<h4>1. The Damped Equation of Motion</h4>\nAssuming viscous damping where the retarding force is proportional to velocity: $F_d = -b \\dot{x}$, where $b$ is the damping coefficient (N\u00b7s/m).\nNewton's second law:\n$$m \\ddot{x} = -k x - b \\dot{x} \\implies m \\ddot{x} + b \\dot{x} + k x = 0$$\n$$\\ddot{x} + 2\\gamma \\dot{x} + \\omega_0^2 x = 0$$\nwhere $\\gamma = \\frac{b}{2m}$ is the <strong>damping attenuation constant</strong> (s\u207b\u00b9) and $\\omega_0 = \\sqrt{k/m}$ is the natural frequency.\nSeeking solutions of the form $x(t) = e^{\\lambda t}$ yields the auxiliary equation:\n$$\\lambda^2 + 2\\gamma \\lambda + \\omega_0^2 = 0 \\implies \\lambda = -\\gamma \\pm \\sqrt{\\gamma^2 - \\omega_0^2}$$\n\n<h4>2. The Three Damping Regimes</h4>\n<ol>\n  <li><strong>Underdamped Case ($\\gamma < \\omega_0$):</strong>\n  The roots are complex conjugates $\\lambda = -\\gamma \\pm i \\omega_d$, where $\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2}$ is the damped angular frequency.\n  $$x(t) = A_0 e^{-\\gamma t} \\cos(\\omega_d t + \\phi)$$\n  The system oscillates with period $T_d = \\frac{2\\pi}{\\omega_d} > T_0$ while its amplitude decays exponentially: $A(t) = A_0 e^{-\\gamma t}$.\n  <strong>Logarithmic Decrement ($\\delta$):</strong> The natural logarithm of the ratio of two consecutive peak amplitudes separated by one period $T_d$:\n  $$\\delta = \\ln\\left( \\frac{x(t)}{x(t + T_d)} \\right) = \\ln\\left( \\frac{A_0 e^{-\\gamma t}}{A_0 e^{-\\gamma (t + T_d)}} \\right) = \\gamma T_d = \\frac{2\\pi \\gamma}{\\omega_d}$$</li>\n  <li><strong>Critically Damped Case ($\\gamma = \\omega_0$):</strong>\n  Repeated real root $\\lambda = -\\gamma$. The general solution is:\n  $$x(t) = (C_1 + C_2 t) e^{-\\gamma t}$$\n  The system returns to equilibrium in the shortest possible time without oscillating (vital for car shock absorbers, galvonometers, and door closers).</li>\n  <li><strong>Overdamped Case ($\\gamma > \\omega_0$):</strong>\n  Two unequal negative real roots. The motion is non-oscillatory and dies out sluggishly:\n  $$x(t) = C_1 e^{-(\\gamma - \\sqrt{\\gamma^2-\\omega_0^2}) t} + C_2 e^{-(\\gamma + \\sqrt{\\gamma^2-\\omega_0^2}) t}$$</li>\n</ol>\n\n<h4>3. The Quality Factor ($Q$)</h4>\nThe Quality Factor $Q$ quantifies the sharpness of an oscillator and its ability to store energy relative to rate of dissipation:\n$$Q = 2\\pi \\left( \\frac{\\text{Energy Stored in System}}{\\text{Energy Dissipated per Cycle}} \\right) = \\frac{\\omega_0}{2\\gamma} = \\frac{\\omega_0 m}{b} = \\frac{\\pi}{\\delta}$$\nHigh-Q oscillators (e.g., quartz crystals with $Q \\sim 10^5$, or optical cavities with $Q \\sim 10^9$) ring for many thousands of cycles before dying out."
        },
        {
          "id": "sec-5-7",
          "number": "\u00a75.7",
          "heading": "Forced Oscillations and Resonance",
          "simulation": "shm-resonance-sim",
          "content": "When a damped oscillator is driven by a periodic external force $F(t) = F_0 \\cos(\\omega t)$, it undergoes forced oscillations.\n\n<h4>1. Differential Equation and Steady-State Solution</h4>\n$$\\ddot{x} + 2\\gamma \\dot{x} + \\omega_0^2 x = \\frac{F_0}{m} \\cos(\\omega t)$$\nThe complete solution consists of a transient complementary function $x_h(t)$ (which decays as $e^{-\\gamma t}$) plus a steady-state particular solution $x_p(t)$ oscillating at the driving frequency $\\omega$:\n$$x(t) = x_{\\text{transient}}(t) + x_{\\text{steady}}(t)$$\nAfter transient decay, the steady-state response is:\n$$x(t) = A(\\omega) \\cos(\\omega t - \\phi)$$\nwhere amplitude $A(\\omega)$ and phase lag $\\phi(\\omega)$ are:\n$$A(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4 \\gamma^2 \\omega^2}}$$\n$$\\tan\\phi(\\omega) = \\frac{2\\gamma \\omega}{\\omega_0^2 - \\omega^2}, \\quad 0 \\le \\phi \\le \\pi$$\n\n<h4>2. Amplitude and Velocity Resonance</h4>\n<ul>\n  <li><strong>Amplitude Resonance:</strong> Maximizing $A(\\omega)$ by minimizing the denominator:\n  $$\\frac{d}{d\\omega}\\left[ (\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2 \\right] = 2(\\omega_0^2 - \\omega^2)(-2\\omega) + 8\\gamma^2 \\omega = 0$$\n  $$\\omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2}$$\n  Resonance occurs slightly below the natural frequency $\\omega_0$.\n  The peak amplitude at $\\omega = \\omega_r$ is:\n  $$A_{max} = \\frac{F_0 / m}{2\\gamma \\sqrt{\\omega_0^2 - \\gamma^2}} \\approx \\frac{F_0 / m}{2\\gamma \\omega_0} = \\frac{Q F_0}{m \\omega_0^2} = Q \\cdot x_{\\text{static}}$$\n  At resonance, amplitude is magnified by exactly the Quality Factor $Q$!</li>\n  <li><strong>Velocity (Power) Resonance:</strong> Differentiating $x(t)$ gives velocity amplitude:\n  $$v_{max}(\\omega) = \\frac{\\omega F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2}} = \\frac{F_0 / m}{\\sqrt{(\\frac{\\omega_0^2 - \\omega^2}{\\omega})^2 + 4\\gamma^2}}$$\n  The velocity resonance peak occurs exactly at $\\omega = \\omega_0$, where the velocity is in phase with the driving force ($\\phi = \\pi/2$).</li>\n</ul>\n\n<h4>3. Sharpness of Resonance and Bandwidth (FWHM)</h4>\nThe average power absorbed by the oscillator is:\n$$\\langle P(\\omega) \\rangle = \\frac{1}{2} b v_{max}^2(\\omega) = \\frac{F_0^2 \\gamma \\omega^2 / m}{(\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2}$$\nThe half-power frequencies $\\omega_1, \\omega_2$ occur when $\\langle P \\rangle = \\frac{1}{2} P_{max}$:\n$$\\Delta \\omega = \\omega_2 - \\omega_1 = 2\\gamma = \\frac{\\omega_0}{Q}$$\nThe sharpness of resonance is inversely proportional to bandwidth: a high $Q$ produces an extremely narrow, sharp resonance peak."
        }
      ],
      "problems": [
        {
          "id": "prob-5-1",
          "difficulty": "Undergraduate Honors Classical Exam Standard",
          "title": "Compound Pendulum: Equivalent Simple Length and Minimum Period",
          "question": "A uniform slender metal rod of mass $M = 2.40\\text{ kg}$ and length $L = 1.20\\text{ m}$ is pivoted about a horizontal axis passing through a small hole drilled at distance $d$ from its center of mass.\\n(a) Derive the expression for the period of oscillation $T(d)$ in terms of $d$, $L$, and $g$,\\n(b) If the rod is pivoted at a distance $d = 0.300\\text{ m}$ from its center, find the time period $T$ and the length of the equivalent simple pendulum $L_{eq}$, and\\n(c) Determine the position of the pivot $d_{min}$ that minimizes the period of oscillation and calculate that minimum time period $T_{min}$. Take $g = 9.80\\text{ m/s}^2$.",
          "steps": [
            {
              "title": "Step 1: Moment of inertia and period derivation",
              "math": "$$I_G = \\frac{1}{12}M L^2 = M k_g^2 \\implies k_g^2 = \\frac{L^2}{12} = \\frac{(1.20)^2}{12} = 0.120 \\text{ m}^2$$\n$$I = I_G + M d^2 = M(k_g^2 + d^2)$$\n$$T = 2\\pi \\sqrt{\\frac{I}{M g d}} = 2\\pi \\sqrt{\\frac{k_g^2 + d^2}{g d}} = 2\\pi \\sqrt{\\frac{L_{eq}}{g}}$$\n$$L_{eq} = d + \\frac{k_g^2}{d} = d + \\frac{L^2}{12 d}$$",
              "explanation": "The radius of gyration of a uniform slender rod about its center of mass is $k_g = L / \\sqrt{12}$."
            },
            {
              "title": "Step 2: Numerical evaluation at d = 0.300 m",
              "math": "$$L_{eq} = 0.300 + \\frac{0.120}{0.300} = 0.300 + 0.400 = 0.700 \\text{ m}$$\n$$T = 2\\pi \\sqrt{\\frac{0.700}{9.80}} = 2\\pi \\sqrt{0.071428} = 2\\pi \\times 0.26726 = 1.679 \\text{ s}$$",
              "explanation": "The equivalent simple pendulum has length 0.700 m, yielding an oscillation period of 1.68 s."
            },
            {
              "title": "Step 3: Minimum period condition",
              "math": "$$\\frac{dL_{eq}}{dd} = 1 - \\frac{k_g^2}{d^2} = 0 \\implies d_{min} = k_g = \\sqrt{0.120} = 0.3464 \\text{ m} = 34.64 \\text{ cm}$$\n$$L_{eq,min} = 2 k_g = 2 \\times 0.3464 = 0.6928 \\text{ m}$$\n$$T_{min} = 2\\pi \\sqrt{\\frac{2 k_g}{g}} = 2\\pi \\sqrt{\\frac{0.6928}{9.80}} = 2\\pi \\sqrt{0.07069} = 1.671 \\text{ s}$$",
              "explanation": "The shortest possible period is 1.671 s, occurring when suspended at 34.6 cm from the center."
            }
          ]
        },
        {
          "id": "prob-5-2",
          "difficulty": "Intermediate Classical Exam",
          "title": "Damped Oscillator: Logarithmic Decrement and Quality Factor",
          "question": "A mechanical oscillator of mass $m = 250\\text{ g}$ is attached to a spring of force constant $k = 100\\text{ N/m}$. It moves in a viscous medium where the damping force is $-b v$. The amplitude of oscillation drops to $1/e$ of its initial value after 50 complete oscillations.\\n(a) Determine the logarithmic decrement $\\delta$,\\n(b) Calculate the damping attenuation constant $\\gamma$ and the damping coefficient $b$,\\n(c) Compute the Quality Factor $Q$ and the energy dissipated after 50 oscillations.",
          "steps": [
            {
              "title": "Step 1: Compute natural frequency and logarithmic decrement",
              "math": "$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{100}{0.250}} = \\sqrt{400} = 20.0 \\text{ rad/s}$$\n$$A(t) = A_0 e^{-\\gamma t} = A_0 e^{-\\gamma N T_d}$$\n$$\\text{Given } \\frac{A_{50}}{A_0} = \\frac{1}{e} \\implies e^{-\\gamma \\cdot 50 T_d} = e^{-1} \\implies 50 \\gamma T_d = 1$$\n$$\\delta = \\gamma T_d = \\frac{1}{50} = 0.0200$$",
              "explanation": "The logarithmic decrement is the fractional decay per cycle, here exactly 0.0200."
            },
            {
              "title": "Step 2: Damping constants gamma and b",
              "math": "$$\\omega_d = \\frac{2\\pi}{T_d} \\approx \\omega_0 = 20.0 \\text{ rad/s} \\implies T_d \\approx \\frac{2\\pi}{20.0} = 0.31416 \\text{ s}$$\n$$\\gamma = \\frac{\\delta}{T_d} = \\frac{0.0200}{0.31416} = 0.06366 \\text{ s}^{-1}$$\n$$b = 2 m \\gamma = 2 \\times 0.250 \\times 0.06366 = 0.03183 \\text{ N}\\cdot\\text{s/m}$$",
              "explanation": "Because damping is very weak ($\\gamma \\ll \\omega_0$), $\\omega_d \\approx \\omega_0$ to four significant digits."
            },
            {
              "title": "Step 3: Quality factor and energy dissipation",
              "math": "$$Q = \\frac{\\pi}{\\delta} = \\frac{\\pi}{0.0200} = 157.1$$\n$$E(t) \\propto A^2(t) \\implies \\frac{E_{50}}{E_0} = \\left( \\frac{A_{50}}{A_0} \\right)^2 = \\left(\\frac{1}{e}\\right)^2 = e^{-2} \\approx 0.1353$$\n$$\\Delta E_{\\text{loss}} = (1 - 0.1353) E_0 = 86.47\\% \\text{ of initial energy dissipated.}$$",
              "explanation": "A high Quality Factor of 157 corresponds to very light damping; 86.5% of total mechanical energy is lost over 50 cycles."
            }
          ]
        },
        {
          "id": "prob-5-3",
          "difficulty": "Rigorous Honors Resonance Problem",
          "title": "Forced Oscillation Resonance Amplitude and Half-Power Bandwidth",
          "question": "An oscillating system consists of mass $m = 0.500\\text{ kg}$, spring constant $k = 450\\text{ N/m}$, and damping constant $b = 1.50\\text{ N}\\cdot\\text{s/m}$. It is driven by a sinusoidal force $F(t) = F_0 \\cos(\\omega t)$ with force amplitude $F_0 = 6.00\\text{ N}$.\\n(a) Determine the natural angular frequency $\\omega_0$, damping factor $\\gamma$, and Quality Factor $Q$,\\n(b) Find the amplitude resonance frequency $\\omega_r$ and the maximum steady-state displacement amplitude $A_{max}$, and\\n(c) Calculate the half-power bandwidth $\\Delta \\omega$ and the average power absorbed at velocity resonance.",
          "steps": [
            {
              "title": "Step 1: Compute natural frequency, damping factor, and Q",
              "math": "$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{450}{0.500}} = \\sqrt{900} = 30.0 \\text{ rad/s}$$\n$$\\gamma = \\frac{b}{2m} = \\frac{1.50}{2 \\times 0.500} = 1.50 \\text{ s}^{-1}$$\n$$Q = \\frac{\\omega_0}{2\\gamma} = \\frac{30.0}{2 \\times 1.50} = 10.0$$",
              "explanation": "The oscillator has a natural frequency of 30.0 rad/s and a quality factor $Q = 10$."
            },
            {
              "title": "Step 2: Resonance frequency and peak amplitude",
              "math": "$$\\omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2} = \\sqrt{900 - 2(1.50)^2} = \\sqrt{900 - 4.50} = \\sqrt{895.5} = 29.925 \\text{ rad/s}$$\n$$A_{max} = \\frac{F_0 / m}{2\\gamma \\sqrt{\\omega_0^2 - \\gamma^2}} = \\frac{6.00 / 0.500}{2(1.50) \\sqrt{900 - 2.25}} = \\frac{12.0}{3.0 \\times \\sqrt{897.75}} = \\frac{4.0}{29.962} = 0.1335 \\text{ m} = 13.35 \\text{ cm}$$\n$$x_{\\text{static}} = \\frac{F_0}{k} = \\frac{6.00}{450} = 0.01333 \\text{ m} = 1.333 \\text{ cm} \\implies A_{max} \\approx Q \\cdot x_{\\text{static}} = 10 \\times 1.333 = 13.33 \\text{ cm}$$",
              "explanation": "The resonance amplitude is amplified by a factor of 10 relative to the static Hookean deflection."
            },
            {
              "title": "Step 3: Bandwidth and resonance power absorption",
              "math": "$$\\Delta \\omega = 2\\gamma = 2 \\times 1.50 = 3.00 \\text{ rad/s}$$\n$$\\text{At velocity resonance } (\\omega = \\omega_0 = 30.0 \\text{ rad/s}):$$\n$$v_{max} = \\frac{F_0}{b} = \\frac{6.00}{1.50} = 4.00 \\text{ m/s}$$\n$$\\langle P_{max} \\rangle = \\frac{1}{2} F_0 v_{max} = \\frac{1}{2} \\times 6.00 \\times 4.00 = 12.0 \\text{ W}$$",
              "explanation": "The half-power resonance bandwidth is 3.0 rad/s and the system absorbs an average power of 12.0 W from the driver at peak resonance."
            }
          ]
        }
      ]
    },
    {
      "number": 6,
      "title": "Traveling Waves",
      "leadSummary": "A rigorous study of 1D wave dynamics, d'Alembert's general solution, transverse string waves, longitudinal waves in solids and fluids, Laplace's adiabatic correction, energy flux and intensity, canal gravity waves, capillary ripples, Fourier decomposition, and group versus phase velocity.",
      "sections": [
        {
          "id": "sec-6-1",
          "number": "\u00a76.1",
          "heading": "The 1D Wave Equation and Traveling Wave Kinematics",
          "simulation": "traveling-wave-sim",
          "content": "A wave is an organized disturbance that propagates through space or a material medium, transporting energy and momentum without transporting macroscopic matter.\n\n<h4>1. General Form of a 1D Traveling Wave</h4>\nConsider a 1D disturbance $\\psi(x, t)$ maintaining its shape as it translates along the x-axis with speed $v$:\n$$\\psi(x, t) = f(x \\mp vt)$$\nwhere the minus sign denotes propagation in the $+x$ direction (forward wave) and the plus sign denotes propagation in the $-x$ direction (backward wave).\n\n<h4>2. The Classical 1D Wave Equation</h4>\nUsing the chain rule with variables $\\xi = x - vt$ and $\\eta = x + vt$:\n$$\\frac{\\partial \\psi}{\\partial x} = f'(\\xi), \\quad \\frac{\\partial^2 \\psi}{\\partial x^2} = f''(\\xi)$$\n$$\\frac{\\partial \\psi}{\\partial t} = -v f'(\\xi), \\quad \\frac{\\partial^2 \\psi}{\\partial t^2} = v^2 f''(\\xi)$$\nEquating second derivatives:\n$$\\frac{\\partial^2 \\psi}{\\partial x^2} = \\frac{1}{v^2} \\frac{\\partial^2 \\psi}{\\partial t^2}$$\nThis is the celebrated linear, second-order hyperbolic <strong>Classical Wave Equation</strong>.\nIts general solution, established by Jean le Rond d'Alembert (1747), is:\n$$\\psi(x, t) = f(x - vt) + g(x + vt)$$\nwhere $f$ and $g$ are arbitrary twice-differentiable functions determined by initial Cauchy boundary data $\\psi(x, 0)$ and $\\dot{\\psi}(x, 0)$.\n\n<h4>3. Harmonic Plane Waves</h4>\nFor sinusoidal disturbances:\n$$\\psi(x, t) = A \\cos(k x - \\omega t + \\phi) = A \\cos\\left[ \\frac{2\\pi}{\\lambda} (x - v t) + \\phi \\right]$$\nwhere:\n<ul>\n  <li>$A$: Wave amplitude.</li>\n  <li>$k = \\frac{2\\pi}{\\lambda}$: <strong>Wavenumber</strong> (spatial angular frequency in rad/m).</li>\n  <li>$\\omega = 2\\pi f$: Temporal angular frequency in rad/s.</li>\n  <li>$v = \\frac{\\omega}{k} = f \\lambda$: Phase speed.</li>\n  <li>Complex notation: $\\psi(x, t) = \\text{Re}\\{ A e^{i(kx - \\omega t)} \\}$.</li>\n</ul>"
        },
        {
          "id": "sec-6-2",
          "number": "\u00a76.2",
          "heading": "Speed of Transverse Waves in a Stretched String",
          "simulation": "traveling-wave-sim",
          "content": "Consider a flexible, perfectly elastic string of uniform linear mass density $\\mu$ (kg/m) stretched under constant equilibrium tension $T$ (N).\n\n<h4>1. Derivation from Newton's Second Law</h4>\nLet the string undergo small transverse vibrations in the xy-plane. Consider an infinitesimal segment located between $x$ and $x + dx$ with mass $dm = \\mu \\, dx$.\nThe slope of the string at $x$ is $\\frac{\\partial y}{\\partial x} = \\tan\\theta_1 \\approx \\sin\\theta_1$.\nThe net transverse force $dF_y$ acting on the segment is:\n$$dF_y = T \\sin\\theta_2 - T \\sin\\theta_1 \\approx T \\left[ \\left( \\frac{\\partial y}{\\partial x} \\right)_{x+dx} - \\left( \\frac{\\partial y}{\\partial x} \\right)_x \\right] = T \\frac{\\partial^2 y}{\\partial x^2} dx$$\nBy Newton's second law ($dF_y = dm \\, a_y = \\mu \\, dx \\frac{\\partial^2 y}{\\partial t^2}$):\n$$T \\frac{\\partial^2 y}{\\partial x^2} dx = \\mu \\, dx \\frac{\\partial^2 y}{\\partial t^2}$$\n$$\\frac{\\partial^2 y}{\\partial x^2} = \\frac{\\mu}{T} \\frac{\\partial^2 y}{\\partial t^2}$$\nComparing with the general wave equation $\\frac{\\partial^2 y}{\\partial x^2} = \\frac{1}{v^2} \\frac{\\partial^2 y}{\\partial t^2}$ immediately yields:\n$$v = \\sqrt{\\frac{T}{\\mu}}$$\n<em>Physical Meaning:</em> Wave propagation speed is governed strictly by the ratio of the medium's elastic restoring property ($T$) to its inertial property ($\\mu$). Amplitude and wavelength have zero effect in non-dispersive strings."
        },
        {
          "id": "sec-6-3",
          "number": "\u00a76.3",
          "heading": "Longitudinal Waves in a Solid Bar and Fluids",
          "simulation": "traveling-wave-sim",
          "content": "Longitudinal waves transmit disturbances via compressive and rarefactive displacements along the axis of propagation.\n\n<h4>1. Longitudinal Waves in an Elastic Solid Bar</h4>\nConsider a thin cylindrical solid rod of cross-sectional area $A$, material density $\\rho$, and Young's modulus $Y$.\nLet $u(x, t)$ denote the longitudinal displacement of a cross-section originally at $x$.\nAn infinitesimal segment of initial length $dx$ experiences longitudinal strain:\n$$\\epsilon = \\frac{\\partial u}{\\partial x}$$\nThe normal compressive/tensile stress is:\n$$\\sigma = Y \\epsilon = Y \\frac{\\partial u}{\\partial x}$$\nThe net force acting on the element of mass $dm = \\rho A \\, dx$ is:\n$$dF = [\\sigma(x+dx) - \\sigma(x)] A = A \\frac{\\partial \\sigma}{\\partial x} dx = A Y \\frac{\\partial^2 u}{\\partial x^2} dx$$\nApplying Newton's second law ($dF = dm \\frac{\\partial^2 u}{\\partial t^2}$):\n$$A Y \\frac{\\partial^2 u}{\\partial x^2} dx = \\rho A \\, dx \\frac{\\partial^2 u}{\\partial t^2} \\implies \\frac{\\partial^2 u}{\\partial x^2} = \\frac{\\rho}{Y} \\frac{\\partial^2 u}{\\partial t^2}$$\nThe speed of longitudinal acoustic waves in a thin solid bar is:\n$$v = \\sqrt{\\frac{Y}{\\rho}}$$\n(For steel: $Y \\approx 2 \\times 10^{11} \\text{ Pa}, \\rho \\approx 7850 \\text{ kg/m}^3 \\implies v \\approx 5050 \\text{ m/s}$).\n\n<h4>2. Acoustic Plane Waves in Fluid Media</h4>\nIn fluids, shear modulus vanishes, so restoring forces are provided exclusively by the <strong>Bulk Modulus ($B$)</strong>:\n$$B = -V \\frac{dP}{dV} = \\rho \\frac{dP}{d\\rho}$$\nFollowing identical dynamic balance for an acoustic plane wave:\n$$v = \\sqrt{\\frac{B}{\\rho}}$$\n<ul>\n  <li><strong>Newton's Isothermal Formula (1687):</strong> Newton assumed sound compressions occurred isothermally ($P V = \\text{const} \\implies B_{iso} = P$).\n  $$v_{\\text{Newton}} = \\sqrt{\\frac{P}{\\rho}} \\approx 280 \\text{ m/s in air at STP (16\\% error!)}$$</li>\n  <li><strong>Laplace's Adiabatic Correction (1816):</strong> Pierre-Simon Laplace recognized that acoustic compressions and rarefactions happen so rapidly that heat conduction between adjacent regions is negligible. Acoustic cycles are strictly <strong>adiabatic</strong> ($P V^\\gamma = \\text{const}$):\n  $$B_{ad} = \\gamma P$$\n  $$v = \\sqrt{\\frac{\\gamma P}{\\rho}} = \\sqrt{\\frac{\\gamma R T}{M}}$$\n  where $\\gamma = C_p / C_v \\approx 1.40$ for diatomic air ($M = 0.02897 \\text{ kg/mol}$).\n  At 20\u00b0C (293.15 K): $v = \\sqrt{1.40 \\times 8.314 \\times 293.15 / 0.02897} = 343.2 \\text{ m/s}$, matching experimental data perfectly!</li>\n</ul>"
        },
        {
          "id": "sec-6-4",
          "number": "\u00a76.4",
          "heading": "Transmission of Energy and Power by Traveling Waves",
          "simulation": "traveling-wave-sim",
          "content": "Traveling waves transport mechanical energy down the medium as particles oscillate in succession.\n\n<h4>1. Energy Density of a Harmonic Transverse Wave</h4>\nConsider a harmonic wave on a string: $y(x, t) = A \\cos(kx - \\omega t)$.\nFor an element of mass $dm = \\mu \\, dx$:\n<ul>\n  <li><strong>Kinetic Energy ($dK$):</strong>\n  $$dK = \\frac{1}{2} dm \\left( \\frac{\\partial y}{\\partial t} \\right)^2 = \\frac{1}{2} \\mu \\, dx \\left[ \\omega A \\sin(kx - \\omega t) \\right]^2 = \\frac{1}{2}\\mu \\omega^2 A^2 \\sin^2(kx - \\omega t) dx$$</li>\n  <li><strong>Potential Energy ($dU$):</strong> Work done in stretching the string element from $dx$ to $ds = \\sqrt{dx^2 + dy^2} \\approx dx [1 + \\frac{1}{2}(\\frac{\\partial y}{\\partial x})^2]$:\n  $$dU = T (ds - dx) = \\frac{1}{2} T \\left( \\frac{\\partial y}{\\partial x} \\right)^2 dx = \\frac{1}{2} T \\left[ -k A \\sin(kx - \\omega t) \\right]^2 dx = \\frac{1}{2} T k^2 A^2 \\sin^2(kx - \\omega t) dx$$\n  Since $v = \\omega / k = \\sqrt{T / \\mu} \\implies T k^2 = \\mu \\omega^2$:\n  $$dU = \\frac{1}{2} \\mu \\omega^2 A^2 \\sin^2(kx - \\omega t) dx = dK$$</li>\n</ul>\n<em>Fundamental Property:</em> In a pure traveling wave, kinetic energy and potential energy are in phase and locally identical at all points!\nTotal energy per unit length (linear energy density):\n$$u_L = \\frac{dE}{dx} = \\mu \\omega^2 A^2 \\sin^2(kx - \\omega t)$$\nAverage energy density over one wavelength:\n$$\\langle u_L \\rangle = \\frac{1}{2} \\mu \\omega^2 A^2 \\quad (\\text{J/m})$$\n\n<h4>2. Wave Power and Intensity</h4>\nThe rate at which energy is transmitted through any cross-section is the instantaneous power:\n$$P(t) = -T \\left( \\frac{\\partial y}{\\partial x} \\right) \\left( \\frac{\\partial y}{\\partial t} \\right) = T k \\omega A^2 \\sin^2(kx - \\omega t)$$\nSince $T k = \\mu v^2 (\\omega / v) = \\mu v \\omega$:\n$$P(t) = \\mu v \\omega^2 A^2 \\sin^2(kx - \\omega t)$$\nThe time-averaged transmitted power is:\n$$\\langle P \\rangle = \\frac{1}{2} \\mu v \\omega^2 A^2 = \\langle u_L \\rangle v \\quad (\\text{Watts})$$\nFor a 3D medium with volume density $\\rho$, the wave <strong>intensity</strong> $I$ (power per unit area) is:\n$$I = \\frac{\\langle P \\rangle}{\\text{Area}} = \\frac{1}{2} \\rho v \\omega^2 A^2 = 2 \\pi^2 \\rho v f^2 A^2 \\quad (\\text{W/m}^2)$$\nIntensity is strictly proportional to the square of frequency and the square of amplitude ($I \\propto f^2 A^2$)."
        },
        {
          "id": "sec-6-5",
          "number": "\u00a76.5",
          "heading": "Superposition Principle, Canal Gravity Waves, and Ripples",
          "simulation": "traveling-wave-sim",
          "content": "The linear nature of the classical wave equation implies that multiple wave disturbances superpose linearly.\n\n<h4>1. The Principle of Superposition</h4>\nIf $\\psi_1(x, t)$ and $\\psi_2(x, t)$ are individual solutions to the linear wave equation, any linear combination:\n$$\\psi(x, t) = c_1 \\psi_1(x, t) + c_2 \\psi_2(x, t)$$\nis also an exact solution. When two waves pass through the same region, the net displacement is simply the algebraic sum of their separate displacements.\n\n<h4>2. Shallow Water Waves in an Open Canal</h4>\nConsider surface waves propagating along a shallow canal of uniform depth $h$ where wavelength $\\lambda \\gg h$.\nThe horizontal velocity of water parcels is nearly uniform from bed to surface.\nThe wave speed is governed purely by gravitational restoring forces:\n$$v = \\sqrt{g h}$$\nRemarkably, this shallow water wave speed is completely non-dispersive (independent of wavelength $\\lambda$).\n(This explains the immense speed of ocean tsunamis: across an ocean basin of depth $h = 4000 \\text{ m}$, speed reaches $v = \\sqrt{9.8 \\times 4000} \\approx 200 \\text{ m/s} \\approx 720 \\text{ km/h}$).\n\n<h4>3. Capillary Waves and Ripples</h4>\nOn water surfaces, restoring forces are provided by both gravity ($g$) and surface tension ($\\gamma$).\nHydrodynamic analysis of Airy wave theory yields the general dispersion relation for surface waves on water of depth $h$:\n$$\\omega^2 = \\left( g k + \\frac{\\gamma}{\\rho} k^3 \\right) \\tanh(k h)$$\nFor deep water ($k h \\gg 1 \\implies \\tanh(kh) \\to 1$):\n$$v_p^2 = \\frac{\\omega^2}{k^2} = \\frac{g}{k} + \\frac{\\gamma}{\\rho} k = \\frac{g \\lambda}{2\\pi} + \\frac{2\\pi \\gamma}{\\rho \\lambda}$$\nTwo asymptotic regimes exist:\n<ul>\n  <li><strong>Gravity Waves ($\\lambda \\gg 1.7\\text{ cm}$):</strong> Gravity dominates. Phase speed increases with wavelength:\n  $$v_p \\approx \\sqrt{\\frac{g \\lambda}{2\\pi}}$$</li>\n  <li><strong>Ripples / Capillary Waves ($\\lambda \\ll 1.7\\text{ cm}$):</strong> Surface tension dominates. Phase speed increases as wavelength gets smaller:\n  $$v_p \\approx \\sqrt{\\frac{2\\pi \\gamma}{\\rho \\lambda}}$$</li>\n</ul>\n<strong>Minimum Phase Speed:</strong> Minimizing $v_p(\\lambda)$:\n$$\\frac{d(v_p^2)}{d\\lambda} = \\frac{g}{2\\pi} - \\frac{2\\pi \\gamma}{\\rho \\lambda^2} = 0 \\implies \\lambda_c = 2\\pi \\sqrt{\\frac{\\gamma}{\\rho g}}$$\nFor pure water at 20\u00b0C ($\\gamma = 0.0728 \\text{ N/m}, \\rho = 1000 \\text{ kg/m}^3$):\n$$\\lambda_c = 2\\pi \\sqrt{\\frac{0.0728}{1000 \\times 9.80}} \\approx 1.71 \\text{ cm}$$\n$$v_{p,min} = \\left( \\frac{4 g \\gamma}{\\rho} \\right)^{1/4} = \\left( \\frac{4 \\times 9.80 \\times 0.0728}{1000} \\right)^{1/4} \\approx 0.231 \\text{ m/s} = 23.1 \\text{ cm/s}$$\nNo surface disturbance can propagate across quiet water slower than 23.1 cm/s!"
        },
        {
          "id": "sec-6-6",
          "number": "\u00a76.6",
          "heading": "Phase Velocity, Group Velocity, and Fourier Decomposition",
          "simulation": "traveling-wave-sim",
          "content": "When the wave velocity depends on frequency or wavelength ($\\frac{dv}{d\\lambda} \ne 0$), the medium is said to be <strong>dispersive</strong>.\n\n<h4>1. Phase Velocity ($v_p$) vs. Group Velocity ($v_g$)</h4>\nConsider the superposition of two harmonic waves with slightly different frequencies and wavenumbers:\n$$\\psi(x, t) = A \\cos(k_1 x - \\omega_1 t) + A \\cos(k_2 x - \\omega_2 t)$$\nLet $k = \\frac{k_1 + k_2}{2}, \\Delta k = k_1 - k_2$ and $\\omega = \\frac{\\omega_1 + \\omega_2}{2}, \\Delta \\omega = \\omega_1 - \\omega_2$.\nUsing the trigonometric identity $\\cos\\alpha + \\cos\\beta = 2\\cos\\frac{\\alpha-\\beta}{2}\\cos\\frac{\\alpha+\\beta}{2}$:\n$$\\psi(x, t) = 2 A \\cos\\left( \\frac{\\Delta k}{2} x - \\frac{\\Delta \\omega}{2} t \\right) \\cos(k x - \\omega t)$$\nThis represents a high-frequency carrier wave modulated by a slowly varying envelope:\n<ul>\n  <li><strong>Phase Velocity ($v_p$):</strong> The speed at which individual crests and troughs of the carrier advance:\n  $$v_p = \\frac{\\omega}{k}$$</li>\n  <li><strong>Group Velocity ($v_g$):</strong> The speed at which the modulation envelope (and physical wave energy/information) propagates:\n  $$v_g = \\lim_{\\Delta k \\to 0} \\frac{\\Delta \\omega}{\\Delta k} = \\frac{d\\omega}{dk}$$</li>\n</ul>\n\n<h4>2. Rayleigh's Dispersion Relation</h4>\nSince $\\omega = k v_p$:\n$$v_g = \\frac{d(k v_p)}{dk} = v_p + k \\frac{dv_p}{dk}$$\nRewriting in terms of wavelength $\\lambda = 2\\pi / k$ (where $dk = -\\frac{2\\pi}{\\lambda^2} d\\lambda$):\n$$v_g = v_p - \\lambda \\frac{dv_p}{d\\lambda}$$\n<ul>\n  <li><strong>Non-dispersive medium ($\\frac{dv_p}{d\\lambda} = 0$):</strong> $v_g = v_p$ (e.g., sound in air, light in vacuum).</li>\n  <li><strong>Normal dispersion ($\\frac{dv_p}{d\\lambda} > 0$):</strong> $v_g < v_p$ (e.g., deep-water gravity waves where $v_g = \\frac{1}{2} v_p$).</li>\n  <li><strong>Anomalous dispersion ($\\frac{dv_p}{d\\lambda} < 0$):</strong> $v_g > v_p$ (e.g., surface ripples where $v_g = \\frac{3}{2} v_p$).</li>\n</ul>\n\n<h4>3. Fourier Series and Harmonic Wave Packets</h4>\nJoseph Fourier (1822) proved that any arbitrary periodic function $f(x)$ with period $\\lambda$ can be synthesized as an infinite sum of discrete sinusoidal harmonics:\n$$f(x) = \\frac{a_0}{2} + \\sum_{n=1}^\\infty \\left[ a_n \\cos(n k x) + b_n \\sin(n k x) \\right]$$\nwhere the Fourier coefficients are obtained via orthogonality integrals:\n$$a_n = \\frac{2}{\\lambda} \\int_0^\\lambda f(x) \\cos(n k x) dx, \\quad b_n = \\frac{2}{\\lambda} \\int_0^\\lambda f(x) \\sin(n k x) dx$$\nIn a non-dispersive medium, all harmonics travel at the same speed $v$, maintaining the wave pulse shape.\nIn a dispersive medium, each harmonic travels at its own phase speed $v_p(\\omega_n)$, causing localized pulses to disperse and broaden over time."
        }
      ],
      "problems": [
        {
          "id": "prob-6-1",
          "difficulty": "Undergraduate Classical Exam Standard",
          "title": "Transverse Wave on a Stretched Wire: Speed, Tension, and Power",
          "question": "A steel piano wire of diameter $D = 1.20\\text{ mm}$ and material density $\\rho = 7800\\text{ kg/m}^3$ is stretched under tension $T = 600\\text{ N}$. A sinusoidal wave of frequency $f = 250\\text{ Hz}$ and peak-to-peak displacement $2A = 4.00\\text{ mm}$ propagates down the wire.\\n(a) Calculate the linear mass density $\\mu$ and the wave propagation speed $v$,\\n(b) Find the wavelength $\\lambda$ and angular wavenumber $k$, and\\n(c) Determine the linear energy density $\\langle u_L \\rangle$ and the average power $\\langle P \\rangle$ transmitted by the wave.",
          "steps": [
            {
              "title": "Step 1: Compute linear density and wave speed",
              "math": "$$A_{\\text{wire}} = \\frac{\\pi D^2}{4} = \\frac{\\pi (1.20 \\times 10^{-3})^2}{4} = 1.131 \\times 10^{-6} \\text{ m}^2$$\n$$\\mu = \\rho A_{\\text{wire}} = 7800 \\times 1.131 \\times 10^{-6} = 8.822 \\times 10^{-3} \\text{ kg/m}$$\n$$v = \\sqrt{\\frac{T}{\\mu}} = \\sqrt{\\frac{600}{8.822 \\times 10^{-3}}} = \\sqrt{68012} = 260.8 \\text{ m/s}$$",
              "explanation": "Wave speed is governed strictly by the square root of tension over linear mass density."
            },
            {
              "title": "Step 2: Calculate wavelength, angular frequency, and wavenumber",
              "math": "$$\\lambda = \\frac{v}{f} = \\frac{260.8}{250} = 1.043 \\text{ m}$$\n$$k = \\frac{2\\pi}{\\lambda} = \\frac{2\\pi}{1.043} = 6.024 \\text{ rad/m}$$\n$$\\omega = 2\\pi f = 2\\pi \\times 250 = 1570.8 \\text{ rad/s}$$\n$$\\text{Amplitude } A = \\frac{4.00 \\text{ mm}}{2} = 2.00 \\times 10^{-3} \\text{ m}$$",
              "explanation": "Peak displacement amplitude is half the peak-to-peak excursion."
            },
            {
              "title": "Step 3: Average energy density and transmitted power",
              "math": "$$\\langle u_L \\rangle = \\frac{1}{2} \\mu \\omega^2 A^2 = \\frac{1}{2} \\times (8.822 \\times 10^{-3}) \\times (1570.8)^2 \\times (2.00 \\times 10^{-3})^2$$\n$$\\langle u_L \\rangle = 0.5 \\times 0.008822 \\times 2.4674 \\times 10^6 \\times 4.00 \\times 10^{-6} = 4.353 \\times 10^{-2} \\text{ J/m}$$\n$$\\langle P \\rangle = \\langle u_L \\rangle v = (4.353 \\times 10^{-2}) \\times 260.8 = 11.35 \\text{ Watts}$$",
              "explanation": "The piano wire transports a continuous average mechanical power of 11.35 Watts along its length."
            }
          ]
        },
        {
          "id": "prob-6-2",
          "difficulty": "Honors Fluid Wave Mechanics",
          "title": "Capillary-Gravity Waves: Phase Speed and Transition Threshold",
          "question": "For deep-water surface waves, the dispersion relation is given by $v_p^2 = \\frac{g \\lambda}{2\\pi} + \\frac{2\\pi \\gamma}{\\rho \\lambda}$. For clean water at $20^\\circ\\text{C}$ with surface tension $\\gamma = 0.0730\\text{ N/m}$, density $\\rho = 1000\\text{ kg/m}^3$, and $g = 9.80\\text{ m/s}^2$:\\n(a) Derive the wavelength $\\lambda_c$ and frequency $f_c$ at which the phase speed is minimum,\\n(b) Compute the numerical value of minimum phase velocity $v_{p,min}$, and\\n(c) For a swell of wavelength $\\lambda = 20.0\\text{ m}$ and a ripple of wavelength $\\lambda = 5.0\\text{ mm}$, find whether each belongs to the gravity or capillary regime and compute their respective phase speeds.",
          "steps": [
            {
              "title": "Step 1: Determine critical threshold wavelength and minimum speed",
              "math": "$$\\frac{d(v_p^2)}{d\\lambda} = \\frac{g}{2\\pi} - \\frac{2\\pi \\gamma}{\\rho \\lambda^2} = 0 \\implies \\lambda_c = 2\\pi \\sqrt{\\frac{\\gamma}{\\rho g}}$$\n$$\\lambda_c = 2\\pi \\sqrt{\\frac{0.0730}{1000 \\times 9.80}} = 2\\pi \\sqrt{7.449 \\times 10^{-6}} = 2\\pi \\times 2.729 \\times 10^{-3} = 1.715 \\times 10^{-2} \\text{ m} = 1.715 \\text{ cm}$$\n$$v_{p,min} = \\left( \\frac{4 g \\gamma}{\\rho} \\right)^{1/4} = \\left( \\frac{4 \\times 9.80 \\times 0.0730}{1000} \\right)^{1/4} = (2.8616 \\times 10^{-3})^{0.25} = 0.2311 \\text{ m/s} = 23.11 \\text{ cm/s}$$",
              "explanation": "At $\\lambda = 1.71$ cm, gravity and capillary forces contribute identically to the wave speed."
            },
            {
              "title": "Step 2: Minimum frequency",
              "math": "$$f_c = \\frac{v_{p,min}}{\\lambda_c} = \\frac{0.2311 \\text{ m/s}}{0.01715 \\text{ m}} = 13.48 \\text{ Hz}$$",
              "explanation": "Disturbances at 13.5 Hz propagate at the absolute lowest phase speed possible in water."
            },
            {
              "title": "Step 3: Regime identification and speeds",
              "math": "$$\\text{For } \\lambda = 20.0 \\text{ m} \\gg \\lambda_c \\implies \\text{Pure Gravity Swell:}$$\n$$v_p = \\sqrt{\\frac{g \\lambda}{2\\pi}} = \\sqrt{\\frac{9.80 \\times 20.0}{2\\pi}} = \\sqrt{31.19} = 5.58 \\text{ m/s}$$\n$$\\text{For } \\lambda = 5.00 \\text{ mm} = 0.0050 \\text{ m} \\ll \\lambda_c \\implies \\text{Pure Capillary Ripple:}$$\n$$v_p = \\sqrt{\\frac{2\\pi \\gamma}{\\rho \\lambda}} = \\sqrt{\\frac{2\\pi \\times 0.0730}{1000 \\times 0.0050}} = \\sqrt{\\frac{0.4587}{5.0}} = \\sqrt{0.09174} = 0.303 \\text{ m/s} = 30.3 \\text{ cm/s}$$",
              "explanation": "Ocean swells travel rapidly under gravity (5.58 m/s), whereas fine wind ripples travel under surface tension (30.3 cm/s)."
            }
          ]
        },
        {
          "id": "prob-6-3",
          "difficulty": "Advanced Honors Wave Mechanics",
          "title": "Group Velocity and Rayleigh Dispersion in a Waveguide",
          "question": "In an acoustic rectangular duct, the dispersion relation for higher-order acoustic modes is given by $\\omega(k) = \\sqrt{\\omega_{co}^2 + c^2 k^2}$, where $\\omega_{co} = 2\\pi \\times 1000\\text{ rad/s}$ is the duct cutoff frequency and $c = 340\\text{ m/s}$ is the free-space speed of sound.\\n(a) Derive analytical expressions for the phase velocity $v_p(k)$ and group velocity $v_g(k)$ as functions of frequency $\\omega$,\\n(b) Prove that $v_p \\cdot v_g = c^2$, and\\n(c) For a signal operating at $\\omega = 2\\pi \\times 1250\\text{ rad/s}$, calculate $v_p$, $v_g$, and the time required for a wave packet to travel a distance $L = 50.0\\text{ m}$ through the duct.",
          "steps": [
            {
              "title": "Step 1: Derive phase velocity and group velocity",
              "math": "$$v_p = \\frac{\\omega}{k} = \\frac{\\omega}{\\sqrt{\\frac{\\omega^2 - \\omega_{co}^2}{c^2}}} = \\frac{c}{\\sqrt{1 - (\\omega_{co} / \\omega)^2}}$$\n$$v_g = \\frac{d\\omega}{dk} = \\frac{d}{dk}\\left( \\sqrt{\\omega_{co}^2 + c^2 k^2} \\right) = \\frac{c^2 k}{\\sqrt{\\omega_{co}^2 + c^2 k^2}} = \\frac{c^2 (\\frac{\\omega}{v_p})}{\\omega} = \\frac{c^2}{v_p}$$\n$$v_g = c \\sqrt{1 - \\left(\\frac{\\omega_{co}}{\\omega}\\right)^2}$$",
              "explanation": "Group velocity represents envelope energy velocity and is always less than free-space sound speed $c$."
            },
            {
              "title": "Step 2: Prove the reciprocal velocity product",
              "math": "$$v_p \\cdot v_g = \\left[ \\frac{c}{\\sqrt{1 - (\\omega_{co}/\\omega)^2}} \\right] \\times \\left[ c \\sqrt{1 - (\\omega_{co}/\\omega)^2} \\right] = c^2$$\n$$\\text{Q.E.D.}$$",
              "explanation": "This identity mirrors the relativistic de Broglie relation for massive quantum particles and electromagnetic waveguides."
            },
            {
              "title": "Step 3: Numerical calculation at 1250 Hz",
              "math": "$$\\frac{\\omega_{co}}{\\omega} = \\frac{1000}{1250} = 0.800$$\n$$\\sqrt{1 - (0.800)^2} = \\sqrt{1 - 0.640} = \\sqrt{0.360} = 0.600$$\n$$v_p = \\frac{340}{0.600} = 566.7 \\text{ m/s}$$\n$$v_g = 340 \\times 0.600 = 204.0 \\text{ m/s}$$\n$$t_{\\text{packet}} = \\frac{L}{v_g} = \\frac{50.0 \\text{ m}}{204.0 \\text{ m/s}} = 0.2451 \\text{ s} = 245.1 \\text{ ms}$$",
              "explanation": "While phase crests advance superluminally/supersonically at 566.7 m/s, physical pulse energy propagates strictly at group speed 204.0 m/s, requiring 245 ms to traverse 50 m."
            }
          ]
        }
      ]
    },
    {
      "number": 7,
      "title": "Stationary Waves",
      "leadSummary": "A comprehensive analysis of wave reflection and transmission at media interfaces, impedance matching, standing wave kinematics, nodes and antinodes, normal modes and harmonic overtone spectra of stretched strings, acoustic pipe resonance with Rayleigh end corrections, Melde's experiment, and trapped energy dynamics.",
      "sections": [
        {
          "id": "sec-7-1",
          "number": "\u00a77.1",
          "heading": "Reflection and Transmission at a Boundary Junction",
          "simulation": "standing-wave-sim",
          "content": "When a traveling wave encounters a discontinuity between two different physical media, part of the incident wave energy is reflected back into the first medium, and part is transmitted into the second medium.\n\n<h4>1. Boundary Conditions at the Interface</h4>\nConsider two semi-infinite stretched strings joined seamlessly at $x = 0$ under constant uniform tension $T$.\nMedium 1 ($x < 0$) has linear density $\\mu_1$ and wave speed $v_1 = \\sqrt{T/\\mu_1}$.\nMedium 2 ($x > 0$) has linear density $\\mu_2$ and wave speed $v_2 = \\sqrt{T/\\mu_2}$.\nAn incident harmonic wave travels in medium 1:\n$$y_i(x, t) = A_i \\cos(k_1 x - \\omega t)$$\nUpon striking $x = 0$, it gives rise to a reflected wave $y_r(x, t)$ and a transmitted wave $y_t(x, t)$:\n$$y_r(x, t) = A_r \\cos(-k_1 x - \\omega t) = A_r \\cos(k_1 x + \\omega t)$$\n$$y_t(x, t) = A_t \\cos(k_2 x - \\omega t)$$\nBecause both sides vibrate at the driving source frequency, angular frequency $\\omega$ is identical in both media.\nThe physical interface requires two fundamental boundary conditions at $x = 0$:\n<ol>\n  <li><strong>Displacement Continuity:</strong> The string must not tear:\n  $$y_1(0, t) = y_2(0, t) \\implies y_i(0, t) + y_r(0, t) = y_t(0, t)$$\n  $$A_i + A_r = A_t$$</li>\n  <li><strong>Transverse Force Continuity:</strong> By Newton's third law, the transverse vertical tension components must balance:\n  $$T \\left( \\frac{\\partial y_1}{\\partial x} \\right)_{x=0} = T \\left( \\frac{\\partial y_2}{\\partial x} \\right)_{x=0} \\implies k_1 (A_i - A_r) = k_2 A_t$$</li>\n</ol>\n\n<h4>2. Amplitude Reflection and Transmission Coefficients</h4>\nSolving the two linear equations:\n$$A_r = \\left( \\frac{k_1 - k_2}{k_1 + k_2} \\right) A_i = \\left( \\frac{v_2 - v_1}{v_1 + v_2} \\right) A_i$$\n$$A_t = \\left( \\frac{2 k_1}{k_1 + k_2} \\right) A_i = \\left( \\frac{2 v_2}{v_1 + v_2} \\right) A_i$$\nDefining the <strong>characteristic mechanical wave impedance</strong> $Z = \\mu v = \\sqrt{\\mu T} = \\frac{T}{v}$:\n$$r = \\frac{A_r}{A_i} = \\frac{Z_1 - Z_2}{Z_1 + Z_2}, \\quad t = \\frac{A_t}{A_i} = \\frac{2 Z_1}{Z_1 + Z_2}$$\n\n<h4>3. Phase Inversion Analysis</h4>\n<ul>\n  <li><strong>Denser second medium ($\\mu_2 > \\mu_1 \\implies Z_2 > Z_1$):</strong>\n  The reflection coefficient is negative ($r < 0$).\n  Since $\\cos(k_1 x + \\omega t + \\pi) = -\\cos(k_1 x + \\omega t)$, reflection at an acoustically denser medium induces an instantaneous <strong>phase reversal of $\\pi$ radians (180\u00b0)</strong>!</li>\n  <li><strong>Rarer second medium ($\\mu_2 < \\mu_1 \\implies Z_2 < Z_1$):</strong>\n  $r > 0$. The wave reflects in-phase (zero phase shift).</li>\n  <li><strong>Transmission:</strong> $t > 0$ always. The transmitted wave never undergoes phase inversion.</li>\n</ul>\n\n<h4>4. Conservation of Wave Energy Flux</h4>\nWave power is proportional to $Z A^2$:\n$$P_i = \\frac{1}{2} Z_1 \\omega^2 A_i^2, \\quad P_r = \\frac{1}{2} Z_1 \\omega^2 A_r^2, \\quad P_t = \\frac{1}{2} Z_2 \\omega^2 A_t^2$$\nDefining the energy reflection coefficient $R = P_r / P_i$ and transmission coefficient $T_{trans} = P_t / P_i$:\n$$R = \\left( \\frac{Z_1 - Z_2}{Z_1 + Z_2} \\right)^2, \\quad T_{trans} = \\frac{Z_2}{Z_1} \\left( \\frac{2 Z_1}{Z_1 + Z_2} \\right)^2 = \\frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}$$\n$$R + T_{trans} = \\frac{(Z_1 - Z_2)^2 + 4 Z_1 Z_2}{(Z_1 + Z_2)^2} = \\frac{(Z_1 + Z_2)^2}{(Z_1 + Z_2)^2} = 1$$\nEnergy is strictly conserved across the boundary.\n\n<h4>5. Boundary Conditions for No Reflection: Impedance Matching</h4>\nWhen $Z_1 = Z_2$:\n$$R = 0, \\quad T_{trans} = 1$$\nZero energy is reflected back; 100% of the wave power passes unhindered into the second medium. This is the foundational principle of <strong>impedance matching</strong>, critical in ultrasound transducer design (acoustic gel), anti-reflective optical coatings (quarter-wave dielectric layers), and electrical transmission lines."
        },
        {
          "id": "sec-7-2",
          "number": "\u00a77.2",
          "heading": "Reflection at Fixed and Free Ends: Formation of Standing Waves",
          "simulation": "standing-wave-sim",
          "content": "A stationary (standing) wave is formed when two identical harmonic waves of equal amplitude and frequency propagate in opposite directions through the same medium.\n\n<h4>1. Reflection at a Rigid Fixed End ($x = 0$)</h4>\nAt an infinitely rigid termination ($Z_2 \\to \\infty$), the displacement must vanish identically for all time: $y(0, t) = 0$.\nThe incident wave is $y_i(x, t) = A \\cos(kx - \\omega t)$.\nTo cancel $y_i$ at $x = 0$, the reflected wave must have $A_r = -A$:\n$$y_r(x, t) = -A \\cos(kx + \\omega t)$$\nSuperposing the incident and reflected waves:\n$$y(x, t) = y_i(x, t) + y_r(x, t) = A [\\cos(kx - \\omega t) - \\cos(kx + \\omega t)]$$\nUsing the prosthaphaeresis identity $\\cos(\\alpha - \\beta) - \\cos(\\alpha + \\beta) = 2\\sin\\alpha\\sin\\beta$:\n$$y(x, t) = 2 A \\sin(kx) \\sin(\\omega t)$$\nNotice the spatial and temporal variables are completely separated!\nThe amplitude of oscillation at any position $x$ is:\n$$A_{standing}(x) = 2 A |\\sin(kx)|$$\n\n<h4>2. Nodes and Antinodes</h4>\n<ul>\n  <li><strong>Nodes:</strong> Points of permanent zero displacement ($A_{standing} = 0$):\n  $$\\sin(kx) = 0 \\implies kx = n\\pi \\implies x_n = n \\frac{\\lambda}{2}, \\quad n = 0, 1, 2, \\dots$$\n  Consecutive nodes are separated by half a wavelength: $\\Delta x_{\\text{node}} = \\frac{\\lambda}{2}$.</li>\n  <li><strong>Antinodes:</strong> Points of maximum displacement amplitude ($A_{standing} = 2A$):\n  $$|\\sin(kx)| = 1 \\implies kx = \\left(n + \\frac{1}{2}\\right)\\pi \\implies x_a = \\left(n + \\frac{1}{2}\\right) \\frac{\\lambda}{2}$$\n  Consecutive antinodes are separated by $\\frac{\\lambda}{2}$.\n  The distance between an adjacent node and antinode is a quarter wavelength: $\\frac{\\lambda}{4}$.</li>\n</ul>\n\n<h4>3. Reflection at a Free End ($x = 0$)</h4>\nAt an unconstrained frictionless ring / free end, transverse force vanishes: $\\frac{\\partial y}{\\partial x}\\Big|_{x=0} = 0$.\nHere $A_r = +A$ (no phase flip):\n$$y(x, t) = A [\\cos(kx - \\omega t) + \\cos(kx + \\omega t)] = 2 A \\cos(kx) \\cos(\\omega t)$$\nAn antinode forms directly at the free boundary."
        },
        {
          "id": "sec-7-3",
          "number": "\u00a77.3",
          "heading": "Normal Modes and Proper Frequencies of a Stretched String",
          "simulation": "standing-wave-sim",
          "content": "When a string of length $L$ is clamped rigidly at both ends ($x = 0$ and $x = L$), boundary conditions permit only discrete resonant modes of oscillation, known as <strong>normal modes</strong>.\n\n<h4>1. Boundary Conditions and Mode Frequencies</h4>\nThe general standing wave solution is $y(x, t) = [C_1 \\sin(kx) + C_2 \\cos(kx)] \\cos(\\omega t + \\phi)$.\n<ol>\n  <li>At $x = 0$: $y(0, t) = 0 \\implies C_2 = 0$. Thus $y(x, t) = C_1 \\sin(kx) \\cos(\\omega t + \\phi)$.</li>\n  <li>At $x = L$: $y(L, t) = 0 \\implies C_1 \\sin(kL) = 0$.</li>\n</ol>\nFor non-trivial oscillations ($C_1 \\ne 0$):\n$$\\sin(k L) = 0 \\implies k_n L = n \\pi, \\quad n = 1, 2, 3, \\dots$$\nThe allowed wavenumbers and wavelengths are:\n$$k_n = \\frac{n\\pi}{L}, \\quad \\lambda_n = \\frac{2L}{n}$$\nSince wave speed is $v = \\sqrt{T/\\mu}$, the allowed <strong>proper (eigen) frequencies</strong> are:\n$$f_n = \\frac{v}{\\lambda_n} = \\frac{n v}{2L} = \\frac{n}{2L}\\sqrt{\\frac{T}{\\mu}}, \\quad n = 1, 2, 3, \\dots$$\n\n<h4>2. Harmonic Spectrum of a Stretched String</h4>\n<ul>\n  <li><strong>Fundamental Mode / First Harmonic ($n = 1$):</strong>\n  $$\\lambda_1 = 2L, \\quad f_1 = \\frac{1}{2L}\\sqrt{\\frac{T}{\\mu}}$$\n  Contains 2 nodes at the ends and 1 central antinode.</li>\n  <li><strong>Second Harmonic / First Overtone ($n = 2$):</strong>\n  $$\\lambda_2 = L, \\quad f_2 = 2 f_1$$\n  Contains 3 nodes (including center $x = L/2$) and 2 antinodes.</li>\n  <li><strong>Third Harmonic / Second Overtone ($n = 3$):</strong>\n  $$\\lambda_3 = \\frac{2L}{3}, \\quad f_3 = 3 f_1$$\n</ul>\nBecause all integer multiples $f_n = n f_1$ are present, the overtone spectrum is complete and richly consonant, giving musical string instruments (violin, guitar, piano) their warm, harmonic timbre.\n\n<h4>3. Mersenne's Laws of Vibrating Strings</h4>\nMarin Mersenne (1636) summarized the physical dependencies of the fundamental frequency:\n<ol>\n  <li><strong>Law of Length:</strong> $f \\propto \\frac{1}{L}$ (halving length doubles pitch).</li>\n  <li><strong>Law of Tension:</strong> $f \\propto \\sqrt{T}$ (quadrupling tension doubles pitch).</li>\n  <li><strong>Law of Density:</strong> $f \\propto \\frac{1}{\\sqrt{\\mu}} = \\frac{1}{r \\sqrt{\\rho}}$ (thicker strings produce lower pitch).</li>\n</ol>"
        },
        {
          "id": "sec-7-4",
          "number": "\u00a77.4",
          "heading": "Standing Waves in Organ Pipes and Acoustic Columns",
          "simulation": "standing-wave-sim",
          "content": "In acoustic columns (organ pipes, flutes, clarinets), standing waves are formed by longitudinal air particle displacements and pressure oscillations.\n\n<h4>1. Displacement vs. Pressure Waves</h4>\nIn a sound wave, particle displacement $s(x, t)$ and acoustic gauge pressure $p(x, t)$ are out of phase by 90\u00b0:\n$$s(x, t) = s_0 \\sin(kx - \\omega t) \\implies p(x, t) = -B \\frac{\\partial s}{\\partial x} = -B k s_0 \\cos(kx - \\omega t)$$\nConsequently:\n<ul>\n  <li>A <strong>displacement node</strong> (rigid closed boundary where air cannot move) is always a <strong>pressure antinode</strong> (maximum pressure variation).</li>\n  <li>A <strong>displacement antinode</strong> (open pipe end open to atmosphere) is always a <strong>pressure node</strong> (pressure is fixed at atmospheric $p = 0$).</li>\n</ul>\n\n<h4>2. Open Pipe (Open at Both Ends)</h4>\nBoth ends are open to atmosphere $\\implies$ displacement antinodes at both $x = 0$ and $x = L$:\n$$\\lambda_n = \\frac{2L}{n}, \\quad f_n = \\frac{n v}{2L} = n f_1, \\quad n = 1, 2, 3, \\dots$$\nAn open pipe produces all harmonics (both even and odd).\n\n<h4>3. Closed Pipe (Closed at One End, Open at the Other)</h4>\nClosed end at $x = 0$ (displacement node); open end at $x = L$ (displacement antinode):\n$$L = (2n - 1) \\frac{\\lambda_n}{4} \\implies \\lambda_n = \\frac{4L}{2n - 1}$$\n$$f_n = \\frac{(2n - 1) v}{4L} = (2n - 1) f_1, \\quad n = 1, 2, 3, \\dots$$\nA closed pipe produces <strong>only odd harmonics</strong> ($f_1, 3f_1, 5f_1, \\dots$). The fundamental frequency of a closed pipe is half that of an open pipe of identical length ($f_{1,\\text{closed}} = \\frac{1}{2} f_{1,\\text{open}}$).\n\n<h4>4. End Correction</h4>\nIn reality, the acoustic wave reflects slightly outside the open end of a tube of radius $R$.\nLord Rayleigh showed that an acoustic end correction $e \\approx 0.61 R$ must be added for each open end:\n<ul>\n  <li>Open Pipe: $L_{eff} = L + 2(0.61 R) = L + 1.22 R$.</li>\n  <li>Closed Pipe: $L_{eff} = L + 0.61 R$.</li>\n</ul>"
        },
        {
          "id": "sec-7-5",
          "number": "\u00a77.5",
          "heading": "Melde's Experiment and Energy Distribution in Stationary Waves",
          "simulation": "standing-wave-sim",
          "content": "Franz Melde (1859) devised an elegant electro-mechanical apparatus to demonstrate standing waves and verify Mersenne's laws.\n\n<h4>1. Experimental Arrangements of Melde's Apparatus</h4>\nA light string of length $L$ and linear density $\\mu$ is tied to one prong of an electrically driven tuning fork of frequency $f_{fork}$ and stretched horizontally over a frictionless pulley with suspended mass $M$ ($T = M g$).\n<ol>\n  <li><strong>Transverse Arrangement:</strong> The prongs vibrate perpendicular to the length of the string.\n  For every oscillation of the fork prong, the string is displaced once:\n  $$f_{\\text{string}} = f_{fork}$$\n  If the string vibrates in $p$ resonant loops: $L = p \\frac{\\lambda}{2} \\implies \\lambda = \\frac{2L}{p}$.\n  $$f_{fork} = \\frac{p}{2L}\\sqrt{\\frac{T}{\\mu}} = \\frac{p}{2L}\\sqrt{\\frac{M g}{\\mu}} \\implies \\frac{T}{p^2} = \\text{constant}$$</li>\n  <li><strong>Longitudinal Arrangement:</strong> The prongs vibrate parallel to the length of the string.\n  When the prong moves forward, tension drops; when it moves backward, tension peaks. The string is pulled twice during each complete cycle of the tuning fork.\n  Hence the frequency of the string is exactly half the tuning fork frequency (parametric excitation):\n  $$f_{\\text{string}} = \\frac{1}{2} f_{fork}$$\n  $$f_{fork} = \\frac{p}{L}\\sqrt{\\frac{T}{\\mu}}$$</li>\n</ol>\n\n<h4>2. Energy Distribution in Stationary Waves</h4>\nIn a traveling wave, energy flows continuously downstream.\nIn a stationary wave:\n$$y(x, t) = 2 A \\sin(kx) \\cos(\\omega t)$$\n<ul>\n  <li><strong>Kinetic Energy Density:</strong>\n  $$u_K(x, t) = \\frac{1}{2}\\mu \\left(\\frac{\\partial y}{\\partial t}\\right)^2 = 2 \\mu \\omega^2 A^2 \\sin^2(kx) \\sin^2(\\omega t)$$</li>\n  <li><strong>Potential Energy Density:</strong>\n  $$u_P(x, t) = \\frac{1}{2}T \\left(\\frac{\\partial y}{\\partial x}\\right)^2 = 2 T k^2 A^2 \\cos^2(kx) \\cos^2(\\omega t) = 2 \\mu \\omega^2 A^2 \\cos^2(kx) \\cos^2(\\omega t)$$</li>\n</ul>\nNotice:\n<ul>\n  <li>When $\\sin(\\omega t) = 1$ (string passing through equilibrium $y = 0$), potential energy is zero everywhere, and total energy resides purely as kinetic energy concentrated at the <strong>antinodes</strong> ($\\sin(kx) = 1$).</li>\n  <li>When $\\cos(\\omega t) = 1$ (string at maximum displacement), kinetic energy is zero everywhere, and total energy resides purely as potential elastic energy concentrated at the <strong>nodes</strong> ($\\cos(kx) = 1$, where string slope is steepest!).</li>\n</ul>\nTotal energy remains permanently trapped, surging periodically between nodes (elastic potential energy) and antinodes (kinetic energy) with zero net spatial flux across the nodes."
        }
      ],
      "problems": [
        {
          "id": "prob-7-1",
          "difficulty": "Honors Wave Mechanics Standard",
          "title": "Wave Reflection and Transmission at a Composite String Junction",
          "question": "A steel wire of linear density $\\mu_1 = 4.00 \\times 10^{-3}\\text{ kg/m}$ is joined at $x = 0$ to a copper wire of linear density $\\mu_2 = 9.00 \\times 10^{-3}\\text{ kg/m}$. The composite wire is maintained under uniform tension $T = 360\\text{ N}$. A sinusoidal transverse wave of frequency $f = 120\\text{ Hz}$ and amplitude $A_i = 6.00\\text{ mm}$ travels from the steel wire toward the junction.\\n(a) Calculate the wave speed and mechanical impedance in both wires,\\n(b) Determine the amplitude reflection coefficient $r$, amplitude transmission coefficient $t$, and the reflected and transmitted amplitudes $A_r$ and $A_t$, and\\n(c) Compute the energy reflection coefficient $R$ and transmission coefficient $T_{trans}$, verifying conservation of wave power.",
          "steps": [
            {
              "title": "Step 1: Compute wave speeds and mechanical impedances",
              "math": "$$v_1 = \\sqrt{\\frac{T}{\\mu_1}} = \\sqrt{\\frac{360}{4.00 \\times 10^{-3}}} = \\sqrt{90000} = 300.0 \\text{ m/s}$$\n$$v_2 = \\sqrt{\\frac{T}{\\mu_2}} = \\sqrt{\\frac{360}{9.00 \\times 10^{-3}}} = \\sqrt{40000} = 200.0 \\text{ m/s}$$\n$$Z_1 = \\sqrt{\\mu_1 T} = \\sqrt{4.00 \\times 10^{-3} \\times 360} = \\sqrt{1.44} = 1.200 \\text{ kg/s}$$\n$$Z_2 = \\sqrt{\\mu_2 T} = \\sqrt{9.00 \\times 10^{-3} \\times 360} = \\sqrt{3.24} = 1.800 \\text{ kg/s}$$",
              "explanation": "Because tension is constant throughout, impedance is directly proportional to the square root of linear density."
            },
            {
              "title": "Step 2: Amplitude coefficients and reflected/transmitted waves",
              "math": "$$r = \\frac{Z_1 - Z_2}{Z_1 + Z_2} = \\frac{1.200 - 1.800}{1.200 + 1.800} = \\frac{-0.600}{3.000} = -0.200$$\n$$t = \\frac{2 Z_1}{Z_1 + Z_2} = \\frac{2 \\times 1.200}{3.000} = \\frac{2.400}{3.000} = +0.800$$\n$$A_r = |r| A_i = 0.200 \\times 6.00 \\text{ mm} = 1.20 \\text{ mm (with } \\pi \\text{ phase shift)}$$\n$$A_t = t A_i = 0.800 \\times 6.00 \\text{ mm} = 4.80 \\text{ mm (in-phase)}$$",
              "explanation": "The reflected wave has amplitude 1.20 mm and undergoes an immediate 180\u00b0 phase inversion at the denser junction."
            },
            {
              "title": "Step 3: Energy coefficients and power verification",
              "math": "$$R = r^2 = (-0.200)^2 = 0.0400 = 4.00\\%$$\n$$T_{trans} = \\frac{Z_2}{Z_1} t^2 = \\left( \\frac{1.800}{1.200} \\right) \\times (0.800)^2 = 1.500 \\times 0.640 = 0.9600 = 96.00\\%$$\n$$R + T_{trans} = 0.0400 + 0.9600 = 1.0000 = 100\\%$$",
              "explanation": "Exactly 4.00% of incident wave energy is reflected back into the steel wire, and 96.00% is successfully transmitted into the copper wire."
            }
          ]
        },
        {
          "id": "prob-7-2",
          "difficulty": "Standard Classical Exam Problem",
          "title": "Normal Modes of a Stretched Piano Wire",
          "question": "A steel piano wire of length $L = 0.850\\text{ m}$ has a mass of $M = 5.10\\text{ g}$. It is under tension $T = 720\\text{ N}$.\\n(a) Determine the fundamental frequency $f_1$ of the wire,\\n(b) Find the frequencies of the second and third overtones, and\\n(c) By what percentage must the tension be adjusted to increase the fundamental frequency by one semitone (a factor of $2^{1/12} \\approx 1.05946$)?",
          "steps": [
            {
              "title": "Step 1: Calculate linear density and fundamental frequency",
              "math": "$$\\mu = \\frac{M}{L} = \\frac{5.10 \\times 10^{-3} \\text{ kg}}{0.850 \\text{ m}} = 6.00 \\times 10^{-3} \\text{ kg/m}$$\n$$v = \\sqrt{\\frac{T}{\\mu}} = \\sqrt{\\frac{720}{6.00 \\times 10^{-3}}} = \\sqrt{120000} = 346.41 \\text{ m/s}$$\n$$f_1 = \\frac{v}{2L} = \\frac{346.41}{2 \\times 0.850} = \\frac{346.41}{1.700} = 203.77 \\text{ Hz}$$",
              "explanation": "The fundamental mode corresponds to a half-wavelength spanning the wire length."
            },
            {
              "title": "Step 2: Frequencies of overtones",
              "math": "$$\\text{Second Harmonic (1st overtone, } n = 2): f_2 = 2 f_1 = 2 \\times 203.77 = 407.54 \\text{ Hz}$$\n$$\\text{Third Harmonic (2nd overtone, } n = 3): f_3 = 3 f_1 = 3 \\times 203.77 = 611.31 \\text{ Hz}$$\n$$\\text{Fourth Harmonic (3rd overtone, } n = 4): f_4 = 4 f_1 = 4 \\times 203.77 = 815.08 \\text{ Hz}$$",
              "explanation": "For a fixed-fixed wire, overtones are exact integer multiples of the fundamental."
            },
            {
              "title": "Step 3: Tension adjustment for semitone pitch raise",
              "math": "$$f \\propto \\sqrt{T} \\implies \\frac{f'}{f} = \\sqrt{\\frac{T'}{T}} = 1.05946$$\n$$\\frac{T'}{T} = (1.05946)^2 = 1.12246$$\n$$\\Delta T = (1.12246 - 1) \\times 100\\% = +12.25\\%$$\n$$T' = 720 \\times 1.12246 = 808.2 \\text{ N}$$",
              "explanation": "Raising the pitch by one equal-tempered semitone requires increasing the string tension by 12.25% (to 808 N)."
            }
          ]
        },
        {
          "id": "prob-7-3",
          "difficulty": "Experimental Laboratory Exam Standard",
          "title": "Melde's Experiment: Fork Frequency and Loop Analysis",
          "question": "In a Melde's experiment configured in the transverse arrangement, a string of length $L = 1.80\\text{ m}$ vibrates in 4 resonant loops when a pan carrying mass $M_1 = 50.0\\text{ g}$ is suspended. When the mass is changed to $M_2$, the string vibrates in 5 resonant loops with the same tuning fork.\\n(a) State the relationship between the number of loops $p$ and suspended tension $T$, and determine mass $M_2$,\\n(b) If the linear density of the string is $\\mu = 2.45 \\times 10^{-4}\\text{ kg/m}$, calculate the frequency of the electrically maintained tuning fork. Take $g = 9.80\\text{ m/s}^2$.",
          "steps": [
            {
              "title": "Step 1: Relate loop count to tension",
              "math": "$$\\text{In transverse mode: } f = \\frac{p}{2L} \\sqrt{\\frac{T}{\\mu}} = \\text{constant}$$\n$$p \\sqrt{T} = \\text{constant} \\implies p^2 T = \\text{constant} \\implies p_1^2 M_1 = p_2^2 M_2$$\n$$M_2 = M_1 \\left(\\frac{p_1}{p_2}\\right)^2 = 50.0 \\text{ g} \\times \\left(\\frac{4}{5}\\right)^2 = 50.0 \\times 0.640 = 32.0 \\text{ g}$$",
              "explanation": "Because higher loop numbers require shorter wavelengths, the required tension scales inversely with $p^2$."
            },
            {
              "title": "Step 2: Determine tuning fork frequency",
              "math": "$$T_1 = M_1 g = (0.0500 \\text{ kg}) \\times 9.80 \\text{ m/s}^2 = 0.490 \\text{ N}$$\n$$v_1 = \\sqrt{\\frac{T_1}{\\mu}} = \\sqrt{\\frac{0.490}{2.45 \\times 10^{-4}}} = \\sqrt{2000} = 44.721 \\text{ m/s}$$\n$$f_{\\text{fork}} = \\frac{p_1 v_1}{2L} = \\frac{4 \\times 44.721}{2 \\times 1.80} = \\frac{178.885}{3.60} = 49.69 \\text{ Hz} \\approx 50.0 \\text{ Hz}$$",
              "explanation": "The tuning fork operates at 50 Hz (matching standard AC mains vibrator frequency)."
            },
            {
              "title": "Step 3: Verification with second state",
              "math": "$$T_2 = 0.0320 \\times 9.80 = 0.3136 \\text{ N}$$\n$$v_2 = \\sqrt{\\frac{0.3136}{2.45 \\times 10^{-4}}} = \\sqrt{1280} = 35.777 \\text{ m/s}$$\n$$f = \\frac{5 \\times 35.777}{2 \\times 1.80} = \\frac{178.885}{3.60} = 49.69 \\text{ Hz}$$",
              "explanation": "Both configurations yield identical frequency, confirming Melde's law $p^2 T = \\text{constant}$."
            }
          ]
        }
      ]
    },
    {
      "number": 8,
      "title": "Sound Waves",
      "leadSummary": "A comprehensive physical and psychoacoustic study of sound waves, decibel intensity levels, human pitch and loudness perception, 3D spherical wavefront propagation, inverse-square law, interference and diffraction, acoustic radiation efficiency, beats, Tartini combination tones, Doppler frequency shifts, and supersonic Mach shock cones.",
      "sections": [
        {
          "id": "sec-8-1",
          "number": "\u00a78.1",
          "heading": "Intensity and Sound Intensity Levels: The Decibel Scale",
          "simulation": "sound-beats-doppler-sim",
          "content": "Sound is a mechanical longitudinal compression wave propagating through an elastic medium. Human auditory perception spans an extraordinary dynamic range of twelve orders of magnitude in acoustic power.\n\n<h4>1. Acoustic Intensity</h4>\nThe <strong>acoustic intensity ($I$)</strong> is defined as the time-averaged sound energy transmitted per unit time across a unit area perpendicular to the direction of wave propagation (W/m\u00b2):\n$$I = \\langle p(t) v(t) \\rangle = \\frac{p_0^2}{2 \\rho_0 c}$$\nwhere:\n<ul>\n  <li>$p_0$: Maximum acoustic pressure amplitude (Pa).</li>\n  <li>$\\rho_0$: Equilibrium medium density ($1.204 \\text{ kg/m}^3$ for dry air at 20\u00b0C).</li>\n  <li>$c$: Speed of sound ($343.2 \\text{ m/s}$ in air at 20\u00b0C).</li>\n  <li>$\\rho_0 c$: Specific acoustic impedance of air ($Z_0 \\approx 413 \\text{ Pa}\\cdot\\text{s/m} = 413 \\text{ Rayls}$).</li>\n</ul>\nThe threshold of human hearing at 1000 Hz is internationally defined as the reference intensity:\n$$I_0 = 1.00 \\times 10^{-12} \\text{ W/m}^2 \\quad (\\text{corresponding to } p_0 \\approx 20 \\ \\mu\\text{Pa})$$\nThe threshold of pain corresponds to $I \\approx 1.0 \\text{ W/m}^2$ ($p_0 \\approx 29 \\text{ Pa}$).\n\n<h4>2. The Decibel (dB) Sound Level Scale</h4>\nBecause the human ear responds logarithmically (Weber-Fechner Law), acoustic levels are measured on the logarithmic <strong>Decibel Scale</strong>:\n$$\\beta = 10 \\log_{10}\\left( \\frac{I}{I_0} \\right) \\quad (\\text{dB})$$\nIn terms of sound pressure level (SPL):\n$$\\text{SPL} = 20 \\log_{10}\\left( \\frac{p_{\\text{rms}}}{p_{\\text{ref}}} \\right) \\quad (\\text{dB, with } p_{\\text{ref}} = 20 \\ \\mu\\text{Pa})$$\nKey logarithmic benchmarks:\n<ul>\n  <li>Threshold of hearing ($I = I_0$): $\\beta = 10 \\log_{10}(1) = 0\\text{ dB}$.</li>\n  <li>Whisper: $\\approx 20 - 30\\text{ dB}$.</li>\n  <li>Normal conversation: $\\approx 60\\text{ dB}$.</li>\n  <li>Heavy city traffic: $\\approx 80 - 85\\text{ dB}$.</li>\n  <li>Rock concert / Jet engine takeoff at 50 m: $\\approx 120 - 130\\text{ dB}$ (threshold of pain).</li>\n</ul>\n<em>Rule of Thumb:</em>\n<ul>\n  <li>Doubling sound intensity ($I \\to 2I$) produces a $+3.01\\text{ dB}$ increase ($\\Delta\\beta = 10\\log_{10} 2 = 3.01\\text{ dB}$).</li>\n  <li>A tenfold increase in intensity ($I \\to 10I$) produces a $+10\\text{ dB}$ increase.</li>\n</ul>"
        },
        {
          "id": "sec-8-2",
          "number": "\u00a78.2",
          "heading": "Loudness, Pitch, and Human Psychoacoustics",
          "simulation": "sound-beats-doppler-sim",
          "content": "Human auditory perception differentiates between physical stimulus parameters (intensity, frequency, spectral content) and subjective psychoacoustic sensations (loudness, pitch, timbre).\n\n<h4>1. Pitch and Fundamental Frequency</h4>\n<strong>Pitch</strong> is the subjective sensation that orders sounds on a musical frequency scale from low/bass to high/treble.\nFor pure sinusoidal tones, pitch is predominantly determined by frequency $f$.\nFor complex multi-harmonic musical tones, the human brain perceives the pitch corresponding to the fundamental frequency $f_1$, even if the fundamental physical harmonic is filtered out or missing (the <em>\"missing fundamental\"</em> psychoacoustic illusion).\n\n<h4>2. Loudness and Equal-Loudness Contours (Fletcher-Munson Curves)</h4>\n<strong>Loudness</strong> is the subjective psychological magnitude of sound sensation. The human ear does not exhibit a flat frequency response; it is most sensitive in the range $2000 - 5000\\text{ Hz}$ (due to acoustic resonance in the ear canal).\nHarvey Fletcher and Wilden A. Munson (1933) established the standard <strong>Equal-Loudness Contours</strong>:\n<ul>\n  <li><strong>Phon Scale:</strong> A sound has a loudness level of $L$ phons if it is judged to be equally loud as a $1000\\text{ Hz}$ reference tone having a sound pressure level of $L$ dB.</li>\n  <li><strong>Sone Scale:</strong> Developed by S. S. Stevens. 1 sone is defined as the loudness of a 1000 Hz tone at 40 dB SPL (40 phons).\n  Subjective loudness doubles with every $+10\\text{ phon}$ increase:\n  $$S = 2^{(L_{\\text{phon}} - 40)/10} \\quad (\\text{sones})$$</li>\n</ul>\n\n<h4>3. Timbre and Spectral Distribution</h4>\nTimbre (tone quality) is the acoustic characteristic that enables a listener to distinguish between two musical instruments (e.g., a trumpet and an oboe) playing the exact same pitch at the exact same loudness.\nTimbre is determined by:\n<ul>\n  <li>The relative amplitude and harmonic distribution of overtones (Fourier spectrum).</li>\n  <li>Temporal envelope attack, decay, sustain, and release (ADSR) transients.</li>\n</ul>"
        },
        {
          "id": "sec-8-3",
          "number": "\u00a78.3",
          "heading": "Spherical Waves in Three Dimensions and the Inverse-Square Law",
          "simulation": "sound-beats-doppler-sim",
          "content": "In an isotropic 3D medium, a point acoustic source radiates sound uniformly in all spatial directions.\n\n<h4>1. The 3D Wave Equation in Spherical Coordinates</h4>\nThe linear acoustic wave equation in three dimensions is:\n$$\\nabla^2 p = \\frac{1}{c^2} \\frac{\\partial^2 p}{\\partial t^2}$$\nFor a spherically symmetric wave where pressure depends only on radial distance $r$ from the source:\n$$\\nabla^2 p = \\frac{1}{r^2} \\frac{\\partial}{\\partial r} \\left( r^2 \\frac{\\partial p}{\\partial r} \\right) = \\frac{1}{r} \\frac{\\partial^2 (r p)}{\\partial r^2}$$\nSubstituting into the wave equation:\n$$\\frac{\\partial^2 (r p)}{\\partial r^2} = \\frac{1}{c^2} \\frac{\\partial^2 (r p)}{\\partial t^2}$$\nDefining the auxiliary variable $\\psi(r, t) = r p(r, t)$, this reduces to the 1D classical wave equation!\nThe general solution for outgoing expanding spherical waves is:\n$$p(r, t) = \\frac{A}{r} \\cos(k r - \\omega t + \\phi)$$\n<em>Critical Consequence:</em> The pressure amplitude of a spherical wave decreases inversely with radial distance:\n$$p_0(r) \\propto \\frac{1}{r}$$\n\n<h4>2. The Inverse-Square Law of Acoustic Intensity</h4>\nBecause acoustic intensity is proportional to pressure amplitude squared ($I \\propto p_0^2$):\n$$I(r) = \\frac{P_{\\text{source}}}{4\\pi r^2} \\propto \\frac{1}{r^2}$$\nwhere $P_{\\text{source}}$ is the total acoustic power output of an omnidirectional point source (Watts).\nIntensity obeys the <strong>Inverse-Square Law</strong>:\n$$\\frac{I_2}{I_1} = \\left(\\frac{r_1}{r_2}\\right)^2$$\nOn the decibel scale, doubling the distance from a point source reduces the sound level by exactly $6.02\\text{ dB}$:\n$$\\beta_2 - \\beta_1 = 10 \\log_{10}\\left( \\frac{I_2}{I_1} \\right) = 10 \\log_{10}\\left( \\frac{r_1}{r_2} \\right)^2 = 20 \\log_{10}\\left( \\frac{r_1}{r_2} \\right) = 20 \\log_{10}(0.5) = -6.02\\text{ dB}$$"
        },
        {
          "id": "sec-8-4",
          "number": "\u00a78.4",
          "heading": "Interference, Diffraction, and Radiation Efficiency of Sound Sources",
          "simulation": "sound-beats-doppler-sim",
          "content": "Acoustic waves exhibit classical interference and diffraction phenomena governed by wave superposition and boundary conditions.\n\n<h4>1. Interference of Coherent Sound Waves</h4>\nWhen two coherent loudspeakers emit sound waves of wavelength $\\lambda$, the resultant pressure amplitude at observation point $P$ separated from the sources by paths $r_1$ and $r_2$ is:\n$$\\Delta r = |r_1 - r_2|$$\n<ul>\n  <li><strong>Constructive Interference (Maximum Loudness):</strong>\n  $$\\Delta r = n \\lambda, \\quad n = 0, 1, 2, \\dots$$</li>\n  <li><strong>Destructive Interference (Silence / Minimum):</strong>\n  $$\\Delta r = \\left(n + \\frac{1}{2}\\right) \\lambda$$</li>\n</ul>\n<em>Quincke's Interference Tube:</em> Sound enters a branch split into two paths of lengths $L_1$ and $L_2$. Sliding one tube by $\\Delta L$ produces constructive or destructive interference at the listener's ear, allowing direct precision measurement of acoustic wavelength $\\lambda = 2 \\Delta L$.\n\n<h4>2. Diffraction of Sound Waves</h4>\nSound waves diffract around obstacles and through doorways because their acoustic wavelengths ($\\lambda \\sim 0.1 - 3\\text{ m}$) are comparable to everyday architectural dimensions ($D \\sim 1\\text{ m}$).\nBy Airy's circular aperture diffraction formula:\n$$\\sin\\theta \\approx 1.22 \\frac{\\lambda}{D}$$\n<ul>\n  <li><strong>Low-frequency bass notes (100 Hz, $\\lambda = 3.4\\text{ m}$):</strong> $\\lambda \\gg D$, sound bends around obstacles into acoustic shadow zones.</li>\n  <li><strong>High-frequency treble notes (10 kHz, $\\lambda = 3.4\\text{ cm}$):</strong> $\\lambda \\ll D$, sound forms sharp directional beams and geometric acoustic shadows.</li>\n</ul>\n\n<h4>3. Radiation Efficiency of Acoustic Sources</h4>\nThe ability of a vibrating body to convert mechanical vibrational power into acoustic radiated power is quantified by its <strong>radiation efficiency</strong>:\n$$\\eta_{rad} = \\frac{R_{rad}}{\\rho_0 c A}$$\nwhere $R_{rad}$ is the real acoustic radiation resistance.\n<ul>\n  <li><strong>Monopole (Pulsating sphere):</strong> Net volume displacement changes. High acoustic radiation efficiency at low frequencies.</li>\n  <li><strong>Dipole (Unbaffled vibrating loudspeaker cone):</strong> Two out-of-phase pulsating sources separated by small distance. Air simply sloshes back and forth between front and back without radiating efficiently. Installing a baffle board or enclosed cabinet prevents dipole cancellation, dramatically boosting bass output!</li>\n</ul>"
        },
        {
          "id": "sec-8-5",
          "number": "\u00a78.5",
          "heading": "Acoustic Beats and Combination Tones",
          "simulation": "sound-beats-doppler-sim",
          "content": "When two sound waves of slightly different frequencies are sounded simultaneously, the human ear perceives acoustic beats and combination tones.\n\n<h4>1. Mathematical Theory of Beats</h4>\nConsider two acoustic pressure signals of equal amplitude $p_0$ and neighboring frequencies $f_1$ and $f_2$ ($f_1 \\approx f_2$):\n$$p_1(t) = p_0 \\cos(2\\pi f_1 t), \\quad p_2(t) = p_0 \\cos(2\\pi f_2 t)$$\nBy superposition:\n$$p(t) = p_1(t) + p_2(t) = 2 p_0 \\cos\\left[ 2\\pi \\left( \\frac{f_1 - f_2}{2} \\right) t \\right] \\cos\\left[ 2\\pi \\left( \\frac{f_1 + f_2}{2} \\right) t \\right]$$\nThe resultant wave represents a carrier vibration at the average frequency $\\bar{f} = \\frac{f_1 + f_2}{2}$ whose envelope amplitude is slowly modulated:\n$$A_{\\text{mod}}(t) = 2 p_0 \\left| \\cos\\left( \\pi (f_1 - f_2) t \\right) \\right|$$\nSince acoustic intensity is proportional to amplitude squared:\n$$I(t) \\propto A_{\\text{mod}}^2(t) = 4 p_0^2 \\cos^2\\left( \\pi (f_1 - f_2) t \\right) = 2 p_0^2 \\left[ 1 + \\cos\\left( 2\\pi (f_1 - f_2) t \\right) \\right]$$\nThe intensity surges from 0 to $4 p_0^2$ at a rate called the <strong>Beat Frequency ($f_{\\text{beat}}$)</strong>:\n$$f_{\\text{beat}} = |f_1 - f_2|$$\nPiano tuners adjust wire tension until beat frequency drops to zero, achieving unison tuning.\n\n<h4>2. Tartini Combination Tones</h4>\nIn 1714, Italian violinist Giuseppe Tartini discovered that when two loud, pure tones of frequencies $f_1$ and $f_2$ ($f_2 > f_1$) are sounded together, the ear perceives additional tones that are not physically present in the acoustic sound field!\nThese are <strong>subjective combination tones</strong> generated by the non-linear elasticity of the human eardrum and cochlea:\n$$x_{\\text{cochlea}} = a_1 p + a_2 p^2 + a_3 p^3 + \\dots$$\nWhen $p = p_1 \\cos(\\omega_1 t) + p_2 \\cos(\\omega_2 t)$, the quadratic term $p^2$ yields:\n$$p^2 = \\frac{1}{2}p_1^2 + \\frac{1}{2}p_2^2 + \\frac{1}{2}p_1^2 \\cos(2\\omega_1 t) + \\frac{1}{2}p_2^2 \\cos(2\\omega_2 t) + p_1 p_2 [\\cos((\\omega_2 - \\omega_1)t) + \\cos((\\omega_2 + \\omega_1)t)]$$\nThis generates:\n<ul>\n  <li><strong>Difference Tone (Tartini Tone):</strong> $f_{\\text{diff}} = f_2 - f_1$ (very prominent, used by organ builders to generate deep 32-foot bass notes using smaller 16-foot pipes).</li>\n  <li><strong>Summation Tone:</strong> $f_{\\text{sum}} = f_1 + f_2$ (fainter, higher in pitch).</li>\n  <li><strong>Cubic Combination Tones:</strong> $2f_1 - f_2$ and $2f_2 - f_1$ arising from the cubic term $a_3 p^3$.</li>\n</ul>"
        },
        {
          "id": "sec-8-6",
          "number": "\u00a78.6",
          "heading": "The Doppler Effect and Supersonic Shock Waves",
          "simulation": "sound-beats-doppler-sim",
          "content": "Christian Doppler (1842) demonstrated that the observed frequency of a wave depends on the relative motion between the wave source, the observer, and the propagating medium.\n\n<h4>1. The Classical Acoustic Doppler Equation</h4>\nLet:\n<ul>\n  <li>$c$: Speed of sound in the still medium.</li>\n  <li>$v_s$: Velocity of the sound source along the line connecting source and observer (positive when moving toward observer).</li>\n  <li>$v_o$: Velocity of the observer along the connecting line (positive when moving toward source).</li>\n  <li>$v_w$: Velocity of wind/medium along the line of propagation.</li>\n  <li>$f_0$: Emitted source frequency.</li>\n</ul>\nThe general observed frequency $f'$ is:\n$$f' = f_0 \\left( \\frac{c \\pm v_o}{c \\mp v_s} \\right)$$\nSign conventions:\n<ul>\n  <li><strong>Observer moving toward stationary source ($v_o > 0, v_s = 0$):</strong> Observer intercepts more wavefronts per second:\n  $$f' = f_0 \\left( \\frac{c + v_o}{c} \\right) > f_0$$</li>\n  <li><strong>Source moving toward stationary observer ($v_s > 0, v_o = 0$):</strong> Wavefronts are compressed ahead of the source ($\\lambda' = \\frac{c - v_s}{f_0}$):\n  $$f' = f_0 \\left( \\frac{c}{c - v_s} \\right) > f_0$$</li>\n  <li><strong>Approaching systems:</strong> Frequency shifts higher (blueshift).</li>\n  <li><strong>Receding systems:</strong> Frequency shifts lower (redshift).</li>\n</ul>\n\n<h4>2. Supersonic Motion and Mach Shock Waves</h4>\nWhen the source speed $v_s$ equals the speed of sound $c$ ($M = v_s / c = 1$), wavefronts pile up ahead of the source into a singular pressure barrier.\nWhen the source travels faster than sound ($M > 1$, supersonic):\nThe circular wavefronts emitted at successive positions lag behind the source, and their envelope forms a conical wavefront called the <strong>Mach Cone</strong>:\nThe half-angle of the cone (<strong>Mach Angle $\\theta$</strong>) is:\n$$\\sin\\theta = \\frac{c t}{v_s t} = \\frac{c}{v_s} = \\frac{1}{M}$$\nAcross this conical discontinuity, pressure, density, and temperature jump discontinuously.\nWhen this conical shock front sweeps past an observer on the ground, the abrupt double pressure jump produces an explosive <strong>Sonic Boom</strong>.\n\n<h4>3. Modern Technical Applications of the Doppler Effect</h4>\n<ul>\n  <li><strong>Medical Color Doppler Echocardiography:</strong> Measures blood flow velocity and detects heart valve regurgitation non-invasively via ultrasound reflected from erythrocytes.</li>\n  <li><strong>Radar Speed Guns:</strong> Police microwave radar detects vehicle speed via $\\Delta f = \\frac{2 v}{c} f_0$.</li>\n  <li><strong>Astronomical Redshifts:</strong> Hubble's discovery of cosmic expansion via Doppler redshift of spectral absorption lines in distant galaxies.</li>\n</ul>"
        }
      ],
      "problems": [
        {
          "id": "prob-8-1",
          "difficulty": "Undergraduate Classical Exam Standard",
          "title": "Decibel Sound Intensity Addition and Distance Attenuation",
          "question": "A small construction generator acts as an omnidirectional point acoustic source radiating sound power $P_{\\text{sound}} = 0.500\\text{ W}$ in an open field.\\n(a) Determine the acoustic intensity $I$ and sound level $\\beta$ at distance $r_1 = 5.00\\text{ m}$,\\n(b) Find the sound level $\\beta_2$ at distance $r_2 = 25.0\\text{ m}$, and\\n(c) If four identical generators operate simultaneously at the original location, what is the combined sound level in decibels at $r_1 = 5.00\\text{ m}$? Take $I_0 = 1.00 \\times 10^{-12}\\text{ W/m}^2$.",
          "steps": [
            {
              "title": "Step 1: Calculate intensity and sound level at 5.00 m",
              "math": "$$I_1 = \\frac{P_{\\text{sound}}}{4\\pi r_1^2} = \\frac{0.500}{4\\pi \\times (5.00)^2} = \\frac{0.500}{100\\pi} = \\frac{0.500}{314.16} = 1.5915 \\times 10^{-3} \\text{ W/m}^2$$\n$$\\beta_1 = 10 \\log_{10}\\left( \\frac{I_1}{I_0} \\right) = 10 \\log_{10}\\left( \\frac{1.5915 \\times 10^{-3}}{1.00 \\times 10^{-12}} \\right) = 10 \\log_{10}(1.5915 \\times 10^9)$$\n$$\\beta_1 = 10 \\times (9 + \\log_{10} 1.5915) = 10 \\times (9 + 0.2018) = 92.02 \\text{ dB}$$",
              "explanation": "At 5.0 m, the generator produces a loud industrial level of 92.0 dB."
            },
            {
              "title": "Step 2: Attenuation over distance to 25.0 m",
              "math": "$$\\beta_2 = \\beta_1 - 20 \\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 92.02 - 20 \\log_{10}\\left(\\frac{25.0}{5.00}\\right) = 92.02 - 20 \\log_{10}(5)$$\n$$\\beta_2 = 92.02 - 20 \\times 0.69897 = 92.02 - 13.98 = 78.04 \\text{ dB}$$",
              "explanation": "Increasing the distance fivefold reduces the sound level by 14.0 dB to 78.0 dB."
            },
            {
              "title": "Step 3: Superposition of four identical incoherent sources",
              "math": "$$I_{\\text{tot}} = 4 I_1$$\n$$\\beta_{\\text{tot}} = \\beta_1 + 10 \\log_{10}(4) = 92.02 + 10 \\times 0.60206 = 92.02 + 6.02 = 98.04 \\text{ dB}$$",
              "explanation": "Quadrupling the acoustic power adds $+6.02$ dB, raising the level to 98.0 dB."
            }
          ]
        },
        {
          "id": "prob-8-2",
          "difficulty": "Precision Acoustic Calibration Problem",
          "title": "Acoustic Beats and Tuning Fork Calibration",
          "question": "A standard calibration tuning fork $A$ has a known frequency $f_A = 440.0\\text{ Hz}$. When sounded simultaneously with an unknown fork $B$, $4.00\\text{ beats per second}$ are heard. When a small piece of beeswax is attached to the prong of fork $B$ (which increases its effective inertia), the beat frequency decreases to $2.00\\text{ beats per second}$.\\n(a) Explain why attaching wax alters the frequency of fork $B$,\\n(b) Determine the exact original frequency $f_B$ of fork $B$, and\\n(c) What would happen to the beat frequency if even more wax were added until $f_B$ drops further by $4.00\\text{ Hz}$?",
          "steps": [
            {
              "title": "Step 1: Frequency candidates from initial beat frequency",
              "math": "$$f_{\\text{beat}} = |f_A - f_B| = 4.00 \\text{ Hz}$$\n$$f_B = f_A \\pm 4.00 = 440.0 \\pm 4.00 \\implies f_B = 444.0 \\text{ Hz} \\quad \\text{or} \\quad 436.0 \\text{ Hz}$$",
              "explanation": "Initial beat frequency yields two possible mathematical solutions: 444.0 Hz or 436.0 Hz."
            },
            {
              "title": "Step 2: Effect of mass loading and unique identification",
              "math": "$$f_{\\text{fork}} = \\frac{1}{2\\pi} \\sqrt{\\frac{k}{m}} \\implies \\frac{df}{dm} < 0$$\n$$\\text{Adding wax increases mass, so } f_B' < f_B$$\n$$\\text{If } f_B = 436.0 \\text{ Hz}: \\text{ lowering it would yield } f_B' < 436.0 \\implies |440.0 - f_B'| > 4.00 \\text{ Hz (beat rate increases).}$$\n$$\\text{If } f_B = 444.0 \\text{ Hz}: \\text{ lowering it toward 440 Hz yields } |440.0 - f_B'| < 4.00 \\text{ Hz (beat rate decreases).}$$\n$$\\text{Because the observed beat frequency dropped to } 2.00 \\text{ Hz}, \\text{ the true original frequency was:}$$\n$$f_B = 444.0 \\text{ Hz}$$",
              "explanation": "Because adding inertia lowered the beat count, $f_B$ must have been initially higher than 440 Hz."
            },
            {
              "title": "Step 3: Further wax addition analysis",
              "math": "$$f_B'' = 442.0 - 4.00 = 438.0 \\text{ Hz}$$\n$$f_{\\text{beat}}'' = |440.0 - 438.0| = 2.00 \\text{ Hz}$$",
              "explanation": "Adding more wax lowers $f_B$ through unison (0 beats at 440 Hz) down to 438 Hz, where beats reappear at 2.0 Hz."
            }
          ]
        },
        {
          "id": "prob-8-3",
          "difficulty": "Honors Doppler Effect Exam Standard",
          "title": "Doppler Shift with Reflected Acoustic Echo and Beats",
          "question": "A train locomotive moves at constant speed $v_s = 20.0\\text{ m/s}$ directly toward a sheer vertical rock cliff. The locomotive engineer sounds the train whistle at frequency $f_0 = 500.0\\text{ Hz}$. The speed of sound in still air is $c = 340.0\\text{ m/s}$.\\n(a) What frequency $f_{\\text{cliff}}$ is received by a stationary observer standing at the base of the cliff?\\n(b) What frequency $f'_{\\text{echo}}$ of the reflected echo is heard by the train engineer aboard the moving locomotive?\\n(c) What beat frequency $f_{\\text{beat}}$ does the engineer hear between the direct whistle and the reflected echo from the cliff?",
          "steps": [
            {
              "title": "Step 1: Frequency incident on the cliff",
              "math": "$$f_{\\text{cliff}} = f_0 \\left( \\frac{c}{c - v_s} \\right) = 500.0 \\times \\left( \\frac{340.0}{340.0 - 20.0} \\right) = 500.0 \\times \\frac{340.0}{320.0} = 500.0 \\times 1.0625 = 531.25 \\text{ Hz}$$",
              "explanation": "Wavefronts are compressed ahead of the moving locomotive, striking the cliff at 531.25 Hz."
            },
            {
              "title": "Step 2: Frequency of reflected echo received by the engineer",
              "math": "$$\\text{The cliff acts as a stationary source re-radiating sound at } f_{\\text{cliff}} = 531.25 \\text{ Hz}.$$\n$$\\text{The engineer is an observer moving toward this stationary source with speed } v_o = v_s = 20.0 \\text{ m/s}:$$\n$$f'_{\\text{echo}} = f_{\\text{cliff}} \\left( \\frac{c + v_s}{c} \\right) = f_0 \\left( \\frac{c + v_s}{c - v_s} \\right)$$\n$$f'_{\\text{echo}} = 500.0 \\times \\left( \\frac{340.0 + 20.0}{340.0 - 20.0} \\right) = 500.0 \\times \\frac{360.0}{320.0} = 500.0 \\times 1.125 = 562.50 \\text{ Hz}$$",
              "explanation": "Because the engineer is in motion both when emitting and when intercepting the echo, the Doppler factor applies twice."
            },
            {
              "title": "Step 3: Beat frequency heard by the engineer",
              "math": "$$f_{\\text{beat}} = f'_{\\text{echo}} - f_0 = 562.50 - 500.0 = 62.50 \\text{ Hz}$$",
              "explanation": "The direct whistle (500 Hz) and reflected echo (562.5 Hz) superpose to produce a distinct rapid beat frequency of 62.5 Hz."
            }
          ]
        }
      ]
    }
  ]
};
