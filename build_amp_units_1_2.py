import json

unit1 = {
    "id": "unit-1",
    "number": 1,
    "title": "Special Theory of Relativity & Spacetime Dynamics",
    "description": "Exhaustive treatment of special relativity: inertial systems and the Michelson-Morley experiment; Einstein's postulates and exact derivation of the Lorentz transformations; relativistic kinematics including simultaneity breakdown, length contraction, time dilation, and velocity addition; Minkowski spacetime geometry, worldlines, and invariant intervals; four-vector dynamics, relativistic energy-momentum invariant E^2 = p^2 c^2 + m_0^2 c^4, and covariance of Maxwell's electromagnetic field equations.",
    "sections": [
        {
            "id": "u1-sec1",
            "title": "Inertial Frames, Galilean Relativity & The Michelson-Morley Experiment",
            "simulation": "michelson-morley-interferometer-sim",
            "content": """<h4>1. Inertial Reference Frames & Galilean Transformations</h4>
<p>An <strong>inertial reference frame</strong> is one in which Newton's First Law holds: a body free from external forces moves with constant rectilinear velocity. In classical Newtonian mechanics, time is absolute and identical for all observers ($t' = t$). If frame $S'$ moves with uniform velocity $v$ along the common $x$-axis relative to frame $S$, the coordinate transformation is given by the <strong>Galilean Transformation</strong>:</p>
<div class="math-display">
$$x' = x - v t, \\quad y' = y, \\quad z' = z, \\quad t' = t$$
</div>
<p>Differentiating with respect to time yields the classical velocity addition rule:</p>
<div class="math-display">
$$u_x' = u_x - v, \\quad u_y' = u_y, \\quad u_z' = u_z$$
</div>
<p>Differentiating once more confirms the invariance of acceleration: $\\vec{a}' = \\vec{a}$. Because mass $m$ is constant, Newton's Second Law $\\vec{F} = m\\vec{a}$ is form-invariant (Galilean invariant) under these transformations.</p>

<h4>2. The Crisis of Classical Electrodynamics & The Luminiferous Ether</h4>
<p>While Newtonian mechanics is Galilean invariant, Maxwell's equations predict that electromagnetic waves propagate through vacuum at a universal speed:</p>
<div class="math-display">
$$c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 2.99792 \\times 10^8\\,\\text{m/s}$$
</div>
<p>If Galilean relativity applied to light, an observer moving with velocity $v$ toward a light wave would measure its speed as $c + v$, violating Maxwell's wave equation. To reconcile this, 19th-century physicists postulated the existence of a pervasive, stationary, invisible medium termed the <strong>Luminiferous Ether</strong>, with respect to which light propagated at speed $c$. The Earth's orbital velocity around the Sun ($v \\approx 30\\,\\text{km/s}$) should produce a measurable "ether wind."</p>

<h4>3. The Michelson-Morley Experiment & Fringe Shift Derivation</h4>
<p>In 1887, Albert Michelson and Edward Morley designed an ultra-sensitive optical interferometer to detect the Earth's velocity $v$ relative to the hypothetical ether.</p>
<p>A beam of monochromatic light of wavelength $\\lambda$ is split by a half-silvered mirror into two mutually perpendicular arms of equal length $D$:
<ul>
<li><strong>Longitudinal Arm 1 (Parallel to Ether Wind):</strong> Light travels downstream with speed $c - v$ and upstream with speed $c + v$. The round-trip time is:
<div class="math-display">
$$t_1 = \\frac{D}{c - v} + \\frac{D}{c + v} = \\frac{2 D c}{c^2 - v^2} = \\frac{2 D}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1} \\approx \\frac{2 D}{c} \\left( 1 + \\frac{v^2}{c^2} \\right)$$
</div></li>
<li><strong>Transverse Arm 2 (Perpendicular to Ether Wind):</strong> To cross perpendicularly while being swept by the ether wind, the light must follow a diagonal path with effective speed $\\sqrt{c^2 - v^2}$. The round-trip time is:
<div class="math-display">
$$t_2 = \\frac{2 D}{\\sqrt{c^2 - v^2}} = \\frac{2 D}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1/2} \\approx \\frac{2 D}{c} \\left( 1 + \\frac{1}{2} \\frac{v^2}{c^2} \\right)$$
</div></li>
</ul>
</p>
<p>The time difference between the two arms is:</p>
<div class="math-display">
$$\\Delta t = t_1 - t_2 \\approx \\frac{2 D}{c} \\left[ \\left( 1 + \\frac{v^2}{c^2} \\right) - \\left( 1 + \\frac{1}{2} \\frac{v^2}{c^2} \\right) \\right] = \\frac{D v^2}{c^3}$$
</div>
<p>When the entire apparatus is rotated by $90^\\circ$, the roles of the two arms are interchanged, doubling the optical path difference. The predicted shift in interference fringes is:</p>
<div class="math-display">
$$\\Delta N = \\frac{c (2 \\Delta t)}{\\lambda} = \\frac{2 D v^2}{\\lambda c^2}$$
</div>
<p>For $D = 11\\,\\text{m}$, $\\lambda = 590\\,\\text{nm}$, and orbital velocity $v = 30\\,\\text{km/s}$ ($v/c = 10^{-4}$), the predicted fringe shift was $\\Delta N \\approx 0.37$ fringes. The interferometer had a sensitivity capable of detecting $0.005$ fringes. Yet, the measured shift was consistently <strong>zero ($\Delta N < 0.005$)</strong> at all times of the year and all orientations!</p>
<p><strong>Physical Consequence:</strong> The luminiferous ether does not exist. The speed of light is completely independent of the Earth's motion and the orientation of the observer.</p>"""
        },
        {
            "id": "u1-sec2",
            "title": "Postulates of Special Relativity & Derivation of Lorentz Transformations",
            "content": """<h4>1. Einstein's Two Postulates of Special Relativity (1905)</h4>
<p>Albert Einstein resolved the crisis by proposing two fundamental postulates:
<ol>
<li><strong>The Principle of Relativity:</strong> The laws of physics are identical and have the same mathematical form in all inertial reference frames. There is no preferred or absolute inertial frame.</li>
<li><strong>The Constancy of the Speed of Light:</strong> The speed of light in vacuum is an absolute universal constant $c$, having the same value in all inertial reference frames, regardless of the motion of the emitting source or the observing detector.</li>
</ol>
</p>

<h4>2. Mathematical Derivation of the Lorentz Transformations</h4>
<p>Consider two inertial frames $S$ and $S'$ with axes aligned. Frame $S'$ moves with uniform velocity $v$ along the positive $x$-axis. At $t = t' = 0$, their origins coincide ($O = O'$), and a spherical flash of light is emitted from the origin.</p>
<p>By Postulate 2, the wavefront is spherical in both frames:
<div class="math-display">
$$x^2 + y^2 + z^2 - c^2 t^2 = 0 \\quad (\\text{in Frame } S)$$
</div>
<div class="math-display">
$$x'^2 + y'^2 + z'^2 - c^2 t'^2 = 0 \\quad (\\text{in Frame } S')$$
</div>
Transverse coordinates are unaffected by longitudinal motion: $y' = y$ and $z' = z$. By spacetime homogeneity and isotropy, the transformation between $(x, t)$ and $(x', t')$ must be linear:</p>
<div class="math-display">
$$x' = \\gamma (x - v t)$$
</div>
<p>By the Principle of Relativity (Postulate 1), the inverse transformation from $S'$ to $S$ must have the exact same functional form, simply reversing the sign of velocity ($v \\to -v$):</p>
<div class="math-display">
$$x = \\gamma (x' + v t')$$
</div>
<p>Substitute $x'$ from the first equation into the second:</p>
<div class="math-display">
$$x = \\gamma [ \\gamma(x - vt) + v t' ] = \\gamma^2 x - \\gamma^2 v t + \\gamma v t'$$
</div>
<p>Solving for $t'$:</p>
<div class="math-display">
$$\\gamma v t' = x (1 - \\gamma^2) + \\gamma^2 v t \\implies t' = \\gamma t + \\frac{1 - \\gamma^2}{\\gamma v} x$$
</div>
<p>Now substitute $x'$ and $t'$ into the spherical wavefront invariance relation $x'^2 - c^2 t'^2 = x^2 - c^2 t^2$:</p>
<div class="math-display">
$$\\gamma^2 (x - vt)^2 - c^2 \\left[ \\gamma t + \\frac{1 - \\gamma^2}{\\gamma v} x \\right]^2 = x^2 - c^2 t^2$$
</div>
<p>Equating coefficients of $x^2$ and $t^2$ yields the exact value for the <strong>Lorentz factor $\\gamma$</strong>:</p>
<div class="math-display">
$$\\gamma = \\frac{1}{\\sqrt{1 - \\frac{v^2}{c^2}}} = \\frac{1}{\\sqrt{1 - \\beta^2}} \\quad \\left( \\beta = \\frac{v}{c} \\right)$$
</div>
<p>Substituting $\\gamma$ back into the time equation simplifies the coefficient to $-\\frac{v}{c^2}$:</p>
<div class="math-display">
$$\\frac{1 - \\gamma^2}{\\gamma v} = -\\frac{\\gamma v}{c^2}$$
</div>

<h4>3. The Canonical Lorentz Transformation Equations</h4>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Transformation ($S \\to S'$)</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Inverse Transformation ($S' \\to S$)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$x' = \\gamma (x - v t)$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$x = \\gamma (x' + v t')$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$y' = y$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$y = y'$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$z' = z$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$z = z'$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$t' = \\gamma \\left( t - \\frac{v x}{c^2} \\right)$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$t = \\gamma \\left( t' + \\frac{v x'}{c^2} \\right)$</td>
</tr>
</tbody>
</table>
<p>When $v \\ll c$, $\\beta \\to 0$, $\\gamma \\to 1$, and the term $vx/c^2 \\to 0$. The Lorentz transformations reduce precisely to the Galilean transformations, proving Newtonian mechanics is the low-velocity asymptotic limit of special relativity.</p>"""
        },
        {
            "id": "u1-sec3",
            "title": "Relativistic Kinematics: Simultaneity, Length Contraction & Time Dilation",
            "content": """<h4>1. Relativity of Simultaneity</h4>
<p>Consider two events $A$ and $B$ that occur simultaneously at different spatial locations in frame $S$ ($\\Delta t = t_B - t_A = 0$, $\\Delta x = x_B - x_A \\neq 0$). Applying the Lorentz transformation for time:</p>
<div class="math-display">
$$\\Delta t' = t_B' - t_A' = \\gamma \\left( \\Delta t - \\frac{v \\Delta x}{c^2} \\right) = - \\frac{\\gamma v \\Delta x}{c^2} \\neq 0$$
</div>
<p><strong>Fundamental Physical Principle:</strong> Events that are simultaneous in one inertial frame are <em>not simultaneous</em> in another frame moving relative to it! Simultaneity is not an absolute property of the physical universe, but strictly observer-dependent.</p>

<h4>2. Relativistic Length Contraction (Lorentz-FitzGerald Contraction)</h4>
<p>Let a rigid rod lie at rest along the $x'$-axis of frame $S'$. Its <strong>proper length $L_0$</strong> (measured in its rest frame) is $L_0 = x_2' - x_1'$.</p>
<p>An observer in frame $S$ measures the length of the moving rod by simultaneously recording the positions of both endpoints at the same instant in their own frame ($t_1 = t_2$, so $\\Delta t = 0$). From the Lorentz transformation $x_2' - x_1' = \\gamma [ (x_2 - x_1) - v(t_2 - t_1) ]$:</p>
<div class="math-display">
$$L_0 = \\gamma L \\implies L = \\frac{L_0}{\\gamma} = L_0 \\sqrt{1 - \\frac{v^2}{c^2}}$$
</div>
<p>Because $\\gamma > 1$ for any non-zero velocity, $L < L_0$. The length of an object measured by an observer moving relative to it is contracted in the direction of motion, while perpendicular dimensions ($y$ and $z$) remain unchanged.</p>

<h4>3. Relativistic Time Dilation & The Twin Paradox</h4>
<p>Let a clock remain at rest at a fixed position $x'$ in frame $S'$. The time interval between two ticks recorded by this clock at the same spatial point ($\\Delta x' = 0$) is the <strong>proper time interval $\\Delta t_0$</strong>.</p>
<p>To an observer in frame $S$ watching this clock move past with velocity $v$, the elapsed time interval is obtained from the inverse Lorentz transformation:</p>
<div class="math-display">
$$\\Delta t = \\gamma \\left( \\Delta t_0 + \\frac{v \\Delta x'}{c^2} \\right) = \\gamma \\Delta t_0 = \\frac{\\Delta t_0}{\\sqrt{1 - \\frac{v^2}{c^2}}}$$
</div>
<p>Because $\\gamma > 1$, $\\Delta t > \\Delta t_0$. A moving clock ticks slower than an identical clock at rest. This effect has been confirmed to parts-per-billion precision via the extended lifetimes of high-velocity atmospheric cosmic-ray muons and atomic clocks aboard orbiting GPS satellites.</p>

<h4>4. Relativistic Velocity Addition</h4>
<p>Let a particle move with velocity $\\vec{u}' = (u_x', u_y', u_z')$ relative to frame $S'$. To find its velocity $\\vec{u}$ in frame $S$, differentiate the inverse Lorentz transformations:</p>
<div class="math-display">
$$dx = \\gamma (dx' + v dt'), \\quad dy = dy', \\quad dt = \\gamma \\left( dt' + \\frac{v dx'}{c^2} \\right)$$
</div>
<div class="math-display">
$$u_x = \\frac{dx}{dt} = \\frac{\\gamma (dx' + v dt')}{\\gamma (dt' + \\frac{v dx'}{c^2})} = \\frac{\\frac{dx'}{dt'} + v}{1 + \\frac{v}{c^2}\\frac{dx'}{dt'}} = \\frac{u_x' + v}{1 + \\frac{u_x' v}{c^2}}$$
</div>
<div class="math-display">
$$u_y = \\frac{u_y'}{\\gamma \\left( 1 + \\frac{u_x' v}{c^2} \\right)}, \\quad u_z = \\frac{u_z'}{\\gamma \\left( 1 + \\frac{u_x' v}{c^2} \\right)}$$
</div>
<p>Notice that if $u_x' = c$ (a beam of light emitted in $S'$):</p>
<div class="math-display">
$$u_x = \\frac{c + v}{1 + \\frac{c v}{c^2}} = \\frac{c + v}{\\frac{c + v}{c}} = c$$
</div>
<p>The speed of light $c$ is an impassable upper velocity limit that cannot be exceeded by adding velocities.</p>"""
        },
        {
            "id": "u1-sec4",
            "title": "Minkowski Spacetime Geometry: Worldlines & Invariant Intervals",
            "simulation": "lorentz-boost-spacetime-sim",
            "content": """<h4>1. Four-Dimensional Spacetime Continuum</h4>
<p>Hermann Minkowski (1908) recognized that space and time are interconnected facets of a single four-dimensional geometry: <em>"Henceforth space by itself, and time by itself, are doomed to fade away into mere shadows, and only a kind of union of the two will preserve an independent reality."</em></p>
<p>An event in spacetime is represented by coordinates $(ct, x, y, z)$. The path traced by an object through spacetime as time elapses is its <strong>worldline</strong>.</p>

<h4>2. The Invariant Spacetime Interval</h4>
<p>Just as Euclidean distance $\\Delta r^2 = \\Delta x^2 + \\Delta y^2 + \\Delta z^2$ is invariant under spatial rotations, the <strong>spacetime interval $\\Delta s^2$</strong> between two events is invariant under all Lorentz boosts and rotations:</p>
<div class="math-display">
$$\\Delta s^2 = c^2 \\Delta t^2 - (\\Delta x^2 + \\Delta y^2 + \\Delta z^2) = c^2 \\Delta t'^2 - (\\Delta x'^2 + \\Delta y'^2 + \\Delta z'^2)$$
</div>
<p>Using the Minkowski metric tensor $\\eta_{\\mu\\nu} = \\text{diag}(+1, -1, -1, -1)$:</p>
<div class="math-display">
$$ds^2 = \\eta_{\\mu\\nu} dx^\\mu dx^\\nu = c^2 dt^2 - dx^2 - dy^2 - dz^2$$
</div>

<h4>3. Classification of Spacetime Separations & The Light Cone</h4>
<p>The sign of $\\Delta s^2$ partitions all physical relationships into three geometrically distinct regimes:
<ul>
<li><strong>Timelike Separation ($\\Delta s^2 > 0$):</strong> $c^2 \\Delta t^2 > \\Delta r^2$. A physical particle traveling slower than light ($v < c$) can travel between the two events. A frame can always be found where the two events occur at the same spatial point ($\\Delta r' = 0$). Causal cause-and-effect relationships can exist between them.</li>
<li><strong>Lightlike / Null Separation ($\\Delta s^2 = 0$):</strong> $c^2 \\Delta t^2 = \\Delta r^2$. Only massless particles traveling at the speed of light ($v = c$), such as photons, can connect the events. They lie directly on the boundary of the <strong>Light Cone</strong>.</li>
<li><strong>Spacelike Separation ($\\Delta s^2 < 0$):</strong> $\\Delta r^2 > c^2 \\Delta t^2$. No signal traveling at or below speed $c$ can connect the two events. A frame can always be found where the two events are simultaneous ($\\Delta t' = 0$). No causal connection can exist without violating relativity.</li>
</ul>
</p>
<p>The <strong>Light Cone</strong> centered on an event divides spacetime into:
<ol>
<li><strong>Absolute Future:</strong> The interior of the upper forward cone ($t > 0, \\Delta s^2 > 0$), containing all events that can be influenced by the present event.</li>
<li><strong>Absolute Past:</strong> The interior of the lower backward cone ($t < 0, \\Delta s^2 > 0$), containing all historical events that could have causally affected the present event.</li>
<li><strong>Elsewhere:</strong> The exterior region ($\\Delta s^2 < 0$), causally disconnected from the present event.</li>
</ol>
</p>"""
        },
        {
            "id": "u1-sec5",
            "title": "Relativistic Dynamics & Four-Vectors: E^2 = p^2 c^2 + m_0^2 c^4",
            "simulation": "relativistic-kinematics-sim",
            "content": """<h4>1. Four-Vectors and Proper Time</h4>
<p>A <strong>four-vector</strong> $A^\\mu = (A^0, A^1, A^2, A^3) = (A^0, \\vec{A})$ transforms under Lorentz transformations in exactly the same way as coordinate differentials $dx^\\mu = (c dt, d\\vec{x})$.</p>
<p>The <strong>proper time $d\\tau$</strong> is the invariant differential time measured in the particle's instantaneous rest frame:</p>
<div class="math-display">
$$c^2 d\\tau^2 = ds^2 = c^2 dt^2 - d\\vec{x}^2 = c^2 dt^2 \\left( 1 - \\frac{u^2}{c^2} \\right) \\implies d\\tau = \\frac{dt}{\\gamma}$$
</div>
<p>The <strong>four-velocity $U^\\mu$</strong> is defined as the derivative of four-position with respect to proper time:</p>
<div class="math-display">
$$U^\\mu = \\frac{dX^\\mu}{d\\tau} = \\gamma \\frac{dX^\\mu}{dt} = \\gamma (c, \\vec{u})$$
</div>
<p>The invariant scalar product of four-velocity with itself is universally constant:</p>
<div class="math-display">
$$U_\\mu U^\\mu = \\gamma^2 (c^2 - u^2) = c^2 \\frac{c^2 - u^2}{c^2 - u^2} = c^2$$
</div>

<h4>2. Four-Momentum & Relativistic Energy</h4>
<p>The <strong>four-momentum $P^\\mu$</strong> of a particle with rest mass $m_0$ is defined as:</p>
<div class="math-display">
$$P^\\mu = m_0 U^\\mu = (\\gamma m_0 c, \\gamma m_0 \\vec{u}) = \\left( \\frac{E}{c}, \\vec{p} \\right)$$
</div>
<p>where the relativistic three-momentum is $\\vec{p} = \\gamma m_0 \\vec{u}$ and total relativistic energy is:</p>
<div class="math-display">
$$E = \\gamma m_0 c^2 = \\frac{m_0 c^2}{\\sqrt{1 - u^2/c^2}}$$
</div>
<p>At zero velocity ($u = 0, \\gamma = 1$), the particle possesses an inherent <strong>rest energy</strong>:</p>
<div class="math-display">
$$E_0 = m_0 c^2$$
</div>
<p>The relativistic <strong>kinetic energy $K$</strong> is the difference between total energy and rest energy:</p>
<div class="math-display">
$$K = E - m_0 c^2 = (\\gamma - 1) m_0 c^2$$
</div>
<p>Expanding $\\gamma$ in a binomial Taylor series for $u \\ll c$:</p>
<div class="math-display">
$$K = m_0 c^2 \\left( 1 + \\frac{1}{2}\\frac{u^2}{c^2} + \\frac{3}{8}\\frac{u^4}{c^4} + \\dots - 1 \\right) = \\frac{1}{2} m_0 u^2 + \\frac{3}{8} m_0 \\frac{u^4}{c^2} + \\dots$$
</div>
<p>recovering classical Newtonian kinetic energy $\\frac{1}{2} m_0 u^2$ at low speeds.</p>

<h4>3. The Fundamental Energy-Momentum Invariant</h4>
<p>Evaluating the invariant scalar product of four-momentum with itself:</p>
<div class="math-display">
$$P_\\mu P^\\mu = \\left(\\frac{E}{c}\\right)^2 - \\vec{p}^2 = m_0^2 U_\\mu U^\\mu = m_0^2 c^2$$
</div>
<p>Multiplying through by $c^2$ gives Einstein's celebrated energy-momentum invariant:</p>
<div class="math-display">
$$E^2 = p^2 c^2 + m_0^2 c^4$$
</div>
<p><strong>Massless Particles (Photons):</strong> For particles with zero rest mass ($m_0 = 0$):</p>
<div class="math-display">
$$E = p c \\implies p = \\frac{E}{c} = \\frac{h\\nu}{c} = \\frac{h}{\\lambda}$$
</div>
<p>Photons carry real physical momentum despite having zero rest mass, exerting measurable radiation pressure.</p>"""
        },
        {
            "id": "u1-sec6",
            "title": "Covariance of Maxwell's Field Equations & Field Transformations",
            "content": """<h4>1. Covariant Formulation of Electrodynamics</h4>
<p>In relativistic four-vector notation, electric and magnetic fields are unifications of a single antisymmetric rank-2 <strong>electromagnetic field tensor $F^{\\mu\\nu}$</strong>:</p>
<div class="math-display">
$$F^{\\mu\\nu} = \\partial^\\mu A^\\nu - \\partial^\\nu A^\\mu = \\begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\\\ E_x/c & 0 & -B_z & B_y \\\\ E_y/c & B_z & 0 & -B_x \\\\ E_z/c & -B_y & B_x & 0 \\end{pmatrix}$$
</div>
<p>where $A^\\mu = (\\Phi/c, \\vec{A})$ is the electromagnetic four-potential. In this compact tensor notation, all four Maxwell equations collapse into just two manifestly covariant equations:</p>
<div class="math-display">
$$\\partial_\\mu F^{\\mu\\nu} = \\mu_0 J^\\nu \\quad (\\text{Inhomogeneous: Gauss's & Ampere-Maxwell Laws})$$
</div>
<div class="math-display">
$$\\partial_\\mu \\tilde{F}^{\\mu\\nu} = 0 \\quad (\\text{Homogeneous: Gauss's Magnetism & Faraday Laws})$$
</div>
<p>where $J^\\nu = (c\\rho, \\vec{J})$ is the four-current density.</p>

<h4>2. Lorentz Transformation of Electric and Magnetic Fields</h4>
<p>Applying the Lorentz tensor transformation $F'^{\\mu\\nu} = \\Lambda^\\mu{}_\\alpha \\Lambda^\\nu{}_\\beta F^{\\alpha\\beta}$ for a boost along the $x$-axis with velocity $v$ yields:</p>
<div class="math-display">
$$E_x' = E_x, \\quad E_y' = \\gamma (E_y - v B_z), \\quad E_z' = \\gamma (E_z + v B_y)$$
</div>
<div class="math-display">
$$B_x' = B_x, \\quad B_y' = \\gamma \\left( B_y + \\frac{v}{c^2} E_z \\right), \\quad B_z' = \\gamma \\left( B_z - \\frac{v}{c^2} E_y \\right)$$
</div>
<p><strong>Physical Revelation:</strong> Electricity and magnetism are not independent physical entities. What an observer at rest perceives as a purely electrostatic field $\\vec{E}$ will appear to a moving observer as a combination of both an electric field $\\vec{E}'$ and a magnetic field $\\vec{B}'$. Magnetism is fundamentally a relativistic consequence of electrostatics!</p>"""
        }
    ],
    "problems": [
        {
            "id": "u1-prob1",
            "title": "Relativistic Velocity Addition & Spaceship Pursuit Kinematics",
            "statement": "An observer on a space station observes spaceship A traveling along the positive x-axis at velocity v_A = +0.80 c. Spaceship B travels along the same x-axis in the opposite direction at velocity v_B = -0.60 c. (a) Determine the relative velocity of spaceship B as measured by an astronaut on spaceship A. (b) If spaceship A fires a laser beacon along its direction of motion, what is the speed of the laser pulse as measured by spaceship B? (c) Compare the relativistic relative velocity with the Galilean prediction.",
            "solution": """<p><strong>Step 1: Relativistic Velocity Transformation</strong></p>
<p>Let frame $S$ be the space station rest frame. Let frame $S'$ be the rest frame of spaceship A, which moves relative to $S$ at velocity $v = v_A = +0.80 c$.</p>
<p>In frame $S$, spaceship B moves with velocity $u_x = v_B = -0.60 c$. The velocity of B as measured in frame $S'$ ($u_x'$) is given by the Lorentz velocity addition formula:</p>
<div class="math-display">
$$u_x' = \\frac{u_x - v}{1 - \\frac{u_x v}{c^2}} = \\frac{-0.60 c - 0.80 c}{1 - \\frac{(-0.60 c)(0.80 c)}{c^2}} = \\frac{-1.40 c}{1 - (-0.48)} = \\frac{-1.40 c}{1.48} \\approx -0.9459 c$$
</div>
<p>The speed of spaceship B relative to spaceship A is $0.946 c$ (strictly less than $c$).</p>

<p><strong>Step 2: Speed of Laser Signal</strong></p>
<p>By Einstein's Second Postulate, light travels at $c$ in all inertial frames. Using the formula with $u_x = c$:</p>
<div class="math-display">
$$u_x' = \\frac{c - v}{1 - v/c} = c$$
</div>
<p>Both spaceship A, spaceship B, and the space station measure the laser pulse velocity as identically $c$.</p>

<p><strong>Step 3: Comparison with Galilean Relativity</strong></p>
<p>Under classical Galilean mechanics:</p>
<div class="math-display">
$$u_{\\text{Galilean}} = u_x - v = -0.60 c - 0.80 c = -1.40 c$$
</div>
<p>The Galilean prediction exceeds the speed of light by $40\\%$, which is physically impossible in nature.</p>"""
        },
        {
            "id": "u1-prob2",
            "title": "Atmospheric Muon Decay: Time Dilation vs Length Contraction",
            "statement": "Muons created at an altitude of H = 10.0\\,\\text{km} in the upper atmosphere travel downward toward Earth at speed v = 0.998 c. The proper mean lifetime of a muon at rest is \\tau_0 = 2.20\\,\\mu\\text{s}. (a) Calculate the Lorentz factor \\gamma. (b) According to classical Newtonian mechanics, what distance would the muon travel before decaying? (c) According to an Earth-based observer, what is the dilated lifetime of the muon and what distance does it travel? (d) From the proper reference frame of the muon, explain how it reaches the Earth surface in terms of length contraction.",
            "solution": """<p><strong>Step 1: Calculate Lorentz Factor $\\gamma$</strong></p>
<div class="math-display">
$$\\beta = \\frac{v}{c} = 0.998 \\implies \\beta^2 = (0.998)^2 = 0.996004$$
</div>
<div class="math-display">
$$\\gamma = \\frac{1}{\\sqrt{1 - \\beta^2}} = \\frac{1}{\\sqrt{1 - 0.996004}} = \\frac{1}{\\sqrt{0.003996}} = \\frac{1}{0.06321} \\approx 15.82$$
</div>

<p><strong>Step 2: Classical Newtonian Distance Calculation</strong></p>
<div class="math-display">
$$d_{\\text{classical}} = v \\tau_0 = (0.998 \\times 3.0 \\times 10^8\\,\\text{m/s}) \\times (2.20 \\times 10^{-6}\\,\\text{s}) \\approx 658.7\\,\\text{m} = 0.659\\,\\text{km}$$
</div>
<p>Classically, muons could only travel $659\\,\\text{m}$, decaying long before reaching the ground ($10\\,\\text{km}$ below).</p>

<p><strong>Step 3: Earth Observer's Perspective (Time Dilation)</strong></p>
<p>To an observer on Earth, the moving muon clock runs slow by factor $\\gamma$:</p>
<div class="math-display">
$$\\Delta t = \\gamma \\tau_0 = 15.82 \\times 2.20\\,\\mu\\text{s} \\approx 34.80\\,\\mu\\text{s}$$
</div>
<p>The distance traveled before decay is:</p>
<div class="math-display">
$$d = v \\Delta t = (0.998 \\times 3.0 \\times 10^8\\,\\text{m/s}) \\times (34.80 \\times 10^{-6}\\,\\text{s}) \\approx 10,419\\,\\text{m} = 10.42\\,\\text{km}$$
</div>
<p>Because $10.42\\,\\text{km} > 10.0\\,\\text{km}$, the majority of muons easily reach sea-level detectors.</p>

<p><strong>Step 4: Muon's Rest Frame Perspective (Length Contraction)</strong></p>
<p>In the muon's rest frame, its lifetime is unchanged at $\\tau_0 = 2.20\\,\\mu\\text{s}$. However, the Earth and atmosphere rush toward the muon at $0.998 c$. The $10.0\\,\\text{km}$ atmospheric thickness is contracted to:</p>
<div class="math-display">
$$H' = \\frac{H}{\\gamma} = \\frac{10.0\\,\\text{km}}{15.82} \\approx 0.632\\,\\text{km} = 632\\,\\text{m}$$
</div>
<p>In $2.20\\,\\mu\\text{s}$, the rushing Earth covers $d' = v \\tau_0 = 659\\,\\text{m} > 632\\,\\text{m}$. Both frames agree completely on the physical reality of ground arrival!</p>"""
        },
        {
            "id": "u1-prob3",
            "title": "Relativistic Collision & Antiproton Production Threshold Energy",
            "statement": "An antiproton (\\bar{p}) can be created in a high-energy proton-proton collision when a moving proton of rest mass m_p strikes a stationary target proton: p + p \\to p + p + p + \\bar{p}. Given that the rest energy of a proton and antiproton is m_p c^2 = 938.3\\,\\text{MeV}$: (a) Use four-momentum invariants to derive the threshold total energy E_{th} and kinetic energy K_{th} of the incident beam proton. (b) Compute the numerical value of K_{th} in GeV.",
            "solution": """<p><strong>Step 1: Construct Four-Momentum Invariants</strong></p>
<p>Let $P_1$ be the four-momentum of the incident beam proton: $P_1 = (E_1/c, \\vec{p}_1)$. Let $P_2$ be the four-momentum of the target proton at rest: $P_2 = (m_p c, \\vec{0})$.</p>
<p>The total four-momentum of the initial system is $P_{tot} = P_1 + P_2$. Its Lorentz-invariant square is:</p>
<div class="math-display">
$$P_{tot}^2 = (P_1 + P_2)^2 = P_1^2 + P_2^2 + 2 P_1 \\cdot P_2 = m_p^2 c^2 + m_p^2 c^2 + 2 \\left( \\frac{E_1}{c}(m_p c) - \\vec{p}_1 \\cdot \\vec{0} \\right) = 2 m_p^2 c^2 + 2 m_p E_1$$
</div>

<p><strong>Step 2: Evaluate Final State at Threshold</strong></p>
<p>At threshold, all four final particles (three protons and one antiproton, total rest mass $4 m_p$) are produced at rest relative to each other in the center-of-momentum frame, moving together as a single composite mass $M_f = 4 m_p$:</p>
<div class="math-display">
$$P_{final}^2 = (M_f c)^2 = (4 m_p c)^2 = 16 m_p^2 c^2$$
</div>

<p><strong>Step 3: Equate Invariants by Conservation of Four-Momentum</strong></p>
<div class="math-display">
$$2 m_p^2 c^2 + 2 m_p E_1 = 16 m_p^2 c^2 \\implies 2 m_p E_1 = 14 m_p^2 c^2 \\implies E_1 = 7 m_p c^2$$
</div>
<p>The minimum threshold kinetic energy $K_{th}$ required of the incident beam proton is:</p>
<div class="math-display">
$$K_{th} = E_1 - m_p c^2 = 7 m_p c^2 - m_p c^2 = 6 m_p c^2$$
</div>

<p><strong>Step 4: Compute Numerical Value</strong></p>
<div class="math-display">
$$K_{th} = 6 \\times 938.3\\,\\text{MeV} = 5629.8\\,\\text{MeV} \\approx 5.63\\,\\text{GeV}$$
</div>
<p>Notice that while creating an antiproton-proton pair requires only $2 m_p c^2 = 1.88\\,\\text{GeV}$ in rest mass energy, a fixed-target accelerator requires $6 m_p c^2 = 5.63\\,\\text{GeV}$ of beam energy because the remaining $3.75\\,\\text{GeV}$ is locked up in the kinetic energy of the forward-moving center of mass.</p>"""
        }
    ]
}

unit2 = {
    "id": "unit-2",
    "number": 2,
    "title": "Particle Properties of Waves, Photons & X-Ray Physics",
    "description": "Comprehensive quantum theory of electromagnetic radiation: Planck's blackbody quantum hypothesis; photoelectric effect and Einstein's work function formalism; relativistic Compton scattering kinematics and wavelength shift; pair production, pair annihilation, and threshold conservation laws; gravitational photon interactions and black holes; continuous and characteristic X-ray generation, Moseley's atomic law, and Bragg crystal diffraction.",
    "sections": [
        {
            "id": "u2-sec1",
            "title": "Electromagnetic Radiation, Blackbody Radiation & Planck's Quantum Hypothesis",
            "content": """<h4>1. Classical Failure & The Ultraviolet Catastrophe</h4>
<p>Classical thermodynamics and electrodynamics proved completely unable to describe the spectral distribution of blackbody radiation. Rayleigh and Jeans treated radiation inside a cavity of volume $V$ as an ensemble of classical standing electromagnetic waves. The number of modes per unit volume in the frequency interval $[\nu, \nu + d\nu]$ is:</p>
<div class="math-display">
$$g(\\nu) d\\nu = \\frac{8\\pi \\nu^2}{c^3} d\\nu$$
</div>
<p>By the classical equipartition theorem, each harmonic oscillator mode possesses average thermal energy $\\langle E \\rangle = k_B T$. This gives the <strong>Rayleigh-Jeans Spectral Energy Density</strong>:</p>
<div class="math-display">
$$u(\\nu) d\\nu = \\frac{8\\pi \\nu^2}{c^3} k_B T d\\nu$$
</div>
<p>As $\\nu \\to \\infty$ in the ultraviolet and X-ray regimes, $u(\\nu) \\to \\infty$. The total integrated energy density diverges to infinity ($\int_0^\infty u(\\nu) d\nu = \infty$), predicting that every heated object should instantaneously incinerate the universe with an infinite burst of high-frequency radiation—the famous <strong>Ultraviolet Catastrophe</strong>.</p>

<h4>2. Max Planck's Quantum Revolution (1900)</h4>
<p>Max Planck resolved the catastrophe by proposing a revolutionary quantum postulate: the atomic oscillators in the cavity walls cannot absorb or emit radiation continuously, but only in discrete discrete packets (quanta) of energy proportional to frequency:</p>
<div class="math-display">
$$E_n = n h \\nu \\quad (n = 0, 1, 2, 3, \\dots)$$
</div>
<p>where $h = 6.626 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}$ is <strong>Planck's constant</strong>.</p>
<p>Using Boltzmann statistics, the average energy $\\langle E \\rangle$ of an oscillator of frequency $\\nu$ is derived via the discrete partition function:</p>
<div class="math-display">
$$\\langle E \\rangle = \\frac{\\sum_{n=0}^\\infty (n h\\nu) e^{-n h\\nu / k_B T}}{\\sum_{n=0}^\\infty e^{-n h\\nu / k_B T}} = \\frac{h\\nu}{e^{h\\nu / k_B T} - 1}$$
</div>
<p>Multiplying by the mode density $g(\\nu)$ delivers <strong>Planck's Blackbody Radiation Law</strong>:</p>
<div class="math-display">
$$u(\\nu) d\\nu = \\frac{8\\pi h \\nu^3}{c^3} \\frac{1}{e^{h\\nu / k_B T} - 1} d\\nu$$
</div>
<p>At high frequencies ($h\\nu \\gg k_B T$), the exponential denominator explodes, suppressing mode occupancy to zero and cleanly eliminating the ultraviolet catastrophe.</p>"""
        },
        {
            "id": "u2-sec2",
            "title": "Photoelectric Effect: Stopping Potentials & Einstein's Photoelectric Equation",
            "simulation": "photoelectric-effect-sim",
            "content": """<h4>1. Experimental Observations of the Photoelectric Effect</h4>
<p>When ultraviolet light shines on clean metallic surfaces (e.g., zinc, sodium, cesium), electrons are ejected (photoelectrons). Philipp Lenard (1902) discovered experimental features that completely contradicted classical wave theory:
<ol>
<li><strong>Absence of Time Lag:</strong> Photoelectrons are emitted instantaneously ($t < 10^{-9}\\,\\text{s}$) upon illumination, even under ultra-weak light intensities where classical wave theory requires hours of continuous wave-front soaking to accumulate the necessary escape energy.</li>
<li><strong>Threshold Frequency ($\\nu_0$):</strong> For each metal, there exists a distinct threshold frequency $\\nu_0$. If $\\nu < \\nu_0$, zero electrons are emitted regardless of how intense the light beam is.</li>
<li><strong>Independence of Kinetic Energy on Intensity:</strong> The maximum kinetic energy $K_{max}$ of the ejected electrons depends strictly on the <em>frequency $\nu$</em> of the incident light, and is entirely independent of light intensity.</li>
<li><strong>Linear Dependence on Intensity:</strong> Increasing the light intensity increases only the <em>rate of photoelectron emission</em> (photocurrent), not their individual kinetic energies.</li>
</ol>
</p>

<h4>2. Einstein's Photon Hypothesis (1905)</h4>
<p>Albert Einstein explained these observations by postulating that light itself propagates and interacts as localized particle-like energy packets called <strong>photons</strong>, each carrying discrete energy $E = h\\nu$.</p>
<p>When a photon strikes an electron in the metal, it transfers its entire energy $h\\nu$ instantaneously in a 1-to-1 collision. A portion of this energy, the <strong>work function $W_0 = \Phi$</strong>, is expended to overcome the electrostatic binding potential holding the electron in the metal lattice. The remaining energy emerges as the electron's maximum kinetic energy $K_{max}$:</p>
<div class="math-display">
$$h\\nu = W_0 + K_{max} \\implies K_{max} = h\\nu - W_0 = h(\\nu - \\nu_0)$$
</div>
<p>where the <strong>threshold frequency $\\nu_0$</strong> and <strong>threshold wavelength $\\lambda_0$</strong> are:</p>
<div class="math-display">
$$\\nu_0 = \\frac{W_0}{h}, \\quad \\lambda_0 = \\frac{c}{\\nu_0} = \\frac{hc}{W_0}$$
</div>

<h4>3. Stopping Potential Measurement</h4>
<p>By applying a retarding negative potential to the collector plate, electrons are decelerated. The exact potential $V_0$ that reduces the photocurrent to zero is the <strong>stopping potential</strong>:</p>
<div class="math-display">
$$e V_0 = K_{max} = h\\nu - W_0 \\implies V_0 = \\left( \\frac{h}{e} \\right) \\nu - \\frac{W_0}{e}$$
</div>
<p>Robert Millikan (1916) plotted $V_0$ versus frequency $\\nu$ across numerous alkali metals. The resulting graphs were straight lines with universal slope $h/e$, verifying Einstein's equation with high precision and earning Einstein the 1921 Nobel Prize in Physics.</p>"""
        },
        {
            "id": "u2-sec3",
            "title": "Compton Scattering: Relativistic Kinematics & Compton Shift Derivation",
            "simulation": "compton-scattering-sim",
            "content": """<h4>1. Arthur Compton's Discovery (1923)</h4>
<p>When monochromatic X-rays ($\lambda \sim 0.07\text{ nm}$) were scattered from a graphite target, Arthur Compton discovered that the scattered radiation contained not only the incident wavelength $\lambda$, but also an additional component shifted toward longer wavelengths $\lambda' > \lambda$, with the shift depending only on the scattering angle $\theta$. Classical Thomson scattering predicted $\lambda' = \lambda$.</p>

<h4>2. Rigorous Relativistic Kinematic Derivation</h4>
<p>Treat the process as an elastic collision between an incident photon and a stationary free electron of rest mass $m_0$.
<ul>
<li><strong>Before Collision:</strong>
<ul>
<li>Incident photon four-momentum: $P_i = (E/c, \vec{p}) = (h\nu/c, \frac{h\nu}{c} \hat{x})$</li>
<li>Target electron at rest: $P_e = (m_0 c, \vec{0})$</li>
</ul></li>
<li><strong>After Collision:</strong>
<ul>
<li>Scattered photon: Energy $E' = h\nu'$, momentum $\vec{p}'$ at angle $\theta$ relative to $\hat{x}$</li>
<li>Recoil electron: Energy $E_e = \gamma m_0 c^2$, momentum $\vec{p}_e$ at angle $\phi$</li>
</ul></li>
</ul>
</p>
<p>By conservation of four-momentum: $P_i + P_e = P_f + P_e'$. Isolating the recoil electron four-momentum:</p>
<div class="math-display">
$$P_e' = P_i + P_e - P_f$$
</div>
<p>Taking the invariant scalar product of both sides with itself:</p>
<div class="math-display">
$$(P_e')^2 = (P_i + P_e - P_f)^2$$
</div>
<div class="math-display">
$$m_0^2 c^2 = P_i^2 + P_e^2 + P_f^2 + 2 P_i \\cdot P_e - 2 P_i \\cdot P_f - 2 P_e \\cdot P_f$$
</div>
<p>Since photons are massless ($P_i^2 = P_f^2 = 0$) and the initial electron is at rest ($P_e^2 = m_0^2 c^2$):</p>
<div class="math-display">
$$m_0^2 c^2 = m_0^2 c^2 + 2 P_i \\cdot P_e - 2 P_i \\cdot P_f - 2 P_e \\cdot P_f$$
</div>
<div class="math-display">
$$P_i \\cdot P_f = P_e \\cdot (P_i - P_f)$$
</div>
<p>Evaluating the four-vector products:
<ul>
<li>$P_i \\cdot P_f = \\left(\\frac{h\\nu}{c}\\right)\\left(\\frac{h\\nu'}{c}\\right) - \\vec{p} \\cdot \\vec{p}' = \\frac{h^2 \\nu \\nu'}{c^2} (1 - \\cos\\theta)$</li>
<li>$P_e \\cdot (P_i - P_f) = (m_0 c) \\left( \\frac{h\\nu}{c} - \\frac{h\\nu'}{c} \\right) = m_0 h (\\nu - \\nu')$</li>
</ul>
</p>
<p>Equating both expressions:</p>
<div class="math-display">
$$\\frac{h^2 \\nu \\nu'}{c^2} (1 - \\cos\\theta) = m_0 h (\\nu - \\nu')$$
</div>
<p>Dividing both sides by $m_0 h \nu \nu'$:</p>
<div class="math-display">
$$\\frac{h}{m_0 c^2} (1 - \\cos\\theta) = \\frac{\\nu - \\nu'}{\\nu \\nu'} = \\frac{1}{\\nu'} - \\frac{1}{\\nu}$$
</div>
<p>Multiplying by $c$ ($c/\nu' = \lambda'$, $c/\nu = \lambda$) yields the celebrated <strong>Compton Wavelength Shift Formula</strong>:</p>
<div class="math-display">
$$\\Delta \\lambda = \\lambda' - \\lambda = \\frac{h}{m_0 c} (1 - \\cos\\theta) = \\lambda_c (1 - \\cos\\theta)$$
</div>
<p>where the <strong>Compton wavelength of the electron</strong> is:</p>
<div class="math-display">
$$\\lambda_c = \\frac{h}{m_0 c} = \\frac{6.626 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}}{(9.109 \\times 10^{-31}\\,\\text{kg})(2.998 \\times 10^8\\,\\text{m/s})} = 2.426 \\times 10^{-12}\\,\\text{m} = 0.02426\\,\\text{\\AA}$$
</div>
<p>The maximum shift occurs in backscattering ($\\theta = 180^\\circ, \\cos\\theta = -1$):</p>
<div class="math-display">
$$\\Delta \\lambda_{max} = 2 \\lambda_c \\approx 0.0485\\,\\text{\\AA}$$
</div>"""
        },
        {
            "id": "u2-sec4",
            "title": "Pair Production, Annihilation & Photons in Gravitational Fields",
            "content": """<h4>1. Pair Production ($h\nu \to e^- + e^+$)</h4>
<p>In pair production, a high-energy gamma-ray photon materializes into an electron-positron pair: $\\gamma \\to e^- + e^+$.</p>
<p><strong>Conservation Laws and Threshold Energy:</strong></p>
<div class="math-display">
$$E_{th} = 2 m_0 c^2 = 2 \\times 0.511\\,\\text{MeV} = 1.022\\,\\text{MeV}$$
</div>
<p>Any excess photon energy beyond $1.022\\,\\text{MeV}$ appears as kinetic energy of the produced pair: $K_{e^-} + K_{e^+} = h\nu - 2 m_0 c^2$.</p>
<p><strong>Impossibility in Vacuum:</strong> Pair production cannot occur in empty space. In the center-of-momentum frame of the electron-positron pair, net momentum is zero. A single photon, however, always carries momentum $p = E/c \\neq 0$. Energy and momentum cannot be simultaneously conserved in vacuum; a heavy atomic nucleus must be present to absorb the recoil momentum.</p>

<h4>2. Pair Annihilation ($e^- + e^+ \to 2\gamma$)</h4>
<p>The inverse process occurs when a positron encounters an electron, forming a short-lived hydrogen-like atom called <strong>positronium</strong> before annihilating into pure radiation. To conserve momentum in the rest frame, the pair must annihilate into at least two collinear, opposite-traveling gamma photons:</p>
<div class="math-display">
$$e^- + e^+ \\to \\gamma_1 + \\gamma_2$$
</div>
<div class="math-display">
$$E_{\\gamma 1} = E_{\\gamma 2} = m_0 c^2 = 511\\,\\text{keV}$$
</div>
<p>This 511 keV coincidence radiation is the foundational operating principle of medical <strong>Positron Emission Tomography (PET)</strong> scanning.</p>

<h4>3. Photons and Gravity: Gravitational Redshift & Black Holes</h4>
<p>Although photons have zero rest mass, they carry effective gravitational mass $m_g = E/c^2 = h\nu / c^2$ by the Equivalence Principle.</p>
<p>When a photon climbs upward against gravity through height $H$ in a gravitational field $g$, it loses gravitational potential energy:</p>
<div class="math-display">
$$\\Delta E = m_g g H = \\left( \\frac{h\\nu}{c^2} \\right) g H = h \\Delta \\nu$$
</div>
<div class="math-display">
$$\\frac{\\Delta \\nu}{\\nu} = - \\frac{g H}{c^2}$$
</div>
<p>This fractional frequency drop is the <strong>Gravitational Redshift</strong>, verified experimentally by Pound and Rebka (1959) using Mössbauer gamma-ray spectroscopy over a $22.5\\,\\text{m}$ tower at Harvard.</p>
<p><strong>Black Holes:</strong> If a mass $M$ is compressed until the escape velocity equals the speed of light ($v_{esc} = \\sqrt{2GM/R} = c$), no light or matter can escape. This defines the <strong>Schwarzschild Radius</strong>:</p>
<div class="math-display">
$$R_s = \\frac{2 G M}{c^2}$$
</div>
<p>For the Sun, $R_s \\approx 2.95\\,\\text{km}$; for Earth, $R_s \\approx 8.87\\,\\text{mm}$.</p>"""
        },
        {
            "id": "u2-sec5",
            "title": "X-Ray Production: Bremsstrahlung, Duane-Hunt Cutoff & Moseley's Law",
            "simulation": "xray-moseley-diffraction-sim",
            "content": """<h4>1. X-Ray Generation Mechanism (Coolidge Tube)</h4>
<p>In a Coolidge X-ray tube, electrons emitted from a thermionic tungsten filament are accelerated through a colossal high-voltage potential difference $V$ ($20\\,\\text{kV} - 150\\,\\text{kV}$) and crash into a heavy metal anode target (tungsten, molybdenum, copper).</p>
<p>The resulting emission spectrum consists of two distinct components:
<ol>
<li><strong>Continuous X-Ray Spectrum (Bremsstrahlung / Braking Radiation):</strong> High-speed electrons decelerate rapidly in the Coulomb fields of target nuclei. The lost kinetic energy is emitted as continuous radiation.</li>
<li><strong>Characteristic X-Ray Spectrum:</strong> Bombarding electrons knock out inner-shell electrons ($K, L, M$ shells) from target atoms. When outer-shell electrons fall into the vacancies, sharp spectral lines ($K_\\alpha, K_\\beta, L_\\alpha$) characteristic of the anode element are emitted.</li>
</ol>
</p>

<h4>2. The Duane-Hunt Cutoff Limit</h4>
<p>An electron gives up its entire kinetic energy $e V$ in a single head-on collision, producing a photon of maximum frequency $\nu_{max}$ and minimum wavelength $\lambda_{min}$:</p>
<div class="math-display">
$$e V = h \\nu_{max} = \\frac{h c}{\\lambda_{min}}$$
</div>
<div class="math-display">
$$\\lambda_{min} = \\frac{h c}{e V} = \\frac{1.2398 \\times 10^{-6}\\,\\text{V}\\cdot\\text{m}}{V} = \\frac{12,398}{V\\,(\\text{in Volts})}\\,\\text{\\AA}$$
</div>
<p>The short-wavelength cutoff $\lambda_{min}$ depends solely on the accelerating voltage $V$, and is completely independent of the target material.</p>

<h4>3. Moseley's Law & The Concept of Atomic Number (1913)</h4>
<p>Henry Moseley systematically measured the characteristic $K_\\alpha$ X-ray lines across the periodic table from aluminum to gold. He discovered that the square root of the frequency $\nu$ was strictly linear with atomic number $Z$:</p>
<div class="math-display">
$$\\sqrt{\\nu} = a (Z - \\sigma)$$
</div>
<p>where $a$ is a proportionality constant and $\\sigma$ is the <strong>screening constant</strong> ($\\sigma = 1$ for the $K$-series, due to the single remaining electron screening the nucleus). Using Bohr's formula for a transition from $n = 2$ to $n = 1$:</p>
<div class="math-display">
$$\\nu = c R_\\infty (Z - 1)^2 \\left( \\frac{1}{1^2} - \\frac{1}{2^2} \\right) = \\frac{3}{4} c R_\\infty (Z - 1)^2$$
</div>
<div class="math-display">
$$\\sqrt{\\nu} = \\sqrt{\\frac{3}{4} c R_\\infty} \\, (Z - 1)$$
</div>
<p><strong>Historic Importance:</strong> Moseley proved that the periodic table is ordered by <strong>nuclear charge / atomic number ($Z$)</strong> rather than atomic weight, resolving historical anomalies (such as Argon-Potassium and Cobalt-Nickel) and predicting the existence of undiscovered elements ($Z = 43, 61, 72, 75$).</p>"""
        },
        {
            "id": "u2-sec6",
            "title": "X-Ray Diffraction: Bragg's Law & Crystal Structure Determination",
            "content": """<h4>1. Crystals as Natural Three-Dimensional Diffraction Gratings</h4>
<p>Because X-ray wavelengths ($\lambda \sim 0.1\text{ nm}$) match the interatomic lattice spacings $d$ of crystalline solids, Max von Laue (1912) recognized that crystals act as natural three-dimensional diffraction gratings.</p>

<h4>2. Bragg's Law Derivation</h4>
<p>William Henry Bragg and William Lawrence Bragg (1913) modeled diffraction as specular reflection from parallel atomic planes separated by spacing $d_{hkl}$.</p>
<p>Consider a monochromatic parallel X-ray beam striking parallel planes at glancing angle $\theta$ (measured relative to the crystal surface, not the normal). The path difference between waves reflected from adjacent planes is:</p>
<div class="math-display">
$$\\Delta = AB + BC = d \\sin\\theta + d \\sin\\theta = 2 d \\sin\\theta$$
</div>
<p>For constructive interference, this path difference must equal an integer number of wavelengths $n\\lambda$:</p>
<div class="math-display">
$$2 d \\sin\\theta = n \\lambda \\quad (n = 1, 2, 3, \\dots)$$
</div>
<p>This is <strong>Bragg's Law</strong>. Since $\sin\theta \le 1$, diffraction can only occur if $\lambda \le 2d$. Visible light ($\lambda \approx 500\text{ nm}$) cannot produce crystal diffraction because its wavelength is thousands of times larger than lattice spacings.</p>

<h4>3. Experimental Methods of X-Ray Crystallography</h4>
<ul>
<li><strong>Laue Method:</strong> Uses a single stationary crystal illuminated by a continuous "white" polychromatic X-ray beam. Each plane selects the specific wavelength satisfying Bragg's law, producing a pattern of diffraction spots revealing crystal symmetry.</li>
<li><strong>Bragg Spectrometer:</strong> Uses monochromatic X-rays and rotates a single crystal on a precision goniometer to measure scattering angles $\theta$ and determine lattice planes.</li>
<li><strong>Debye-Scherrer Powder Method:</strong> Uses a fine polycrystalline powder containing millions of tiny randomly oriented micro-crystallites. The diffraction beams form concentric cones of constructive interference, recorded as concentric rings on photographic film.</li>
</ul>"""
        }
    ],
    "problems": [
        {
            "id": "u2-prob1",
            "title": "Photoelectric Effect Stopping Potential & Work Function Analysis",
            "statement": "When a metallic cesium surface is illuminated with ultraviolet light of wavelength \\lambda_1 = 300\\,\\text{nm}, the stopping potential required to extinguish the photocurrent is measured to be V_{01} = 2.24\\,\\text{V}. When the wavelength is increased to \\lambda_2 = 450\\,\\text{nm}, the stopping potential drops to V_{02} = 0.86\\,\\text{V}. (a) Use Einstein's photoelectric equation to determine Planck's constant h and the work function W_0 of cesium in electron-volts. (b) Find the threshold frequency \\nu_0 and threshold wavelength \\lambda_0 for cesium. (c) What is the maximum speed of emitted photoelectrons under \\lambda_1 illumination?",
            "solution": """<p><strong>Step 1: Set Up Einstein's Equations</strong></p>
<p>For two frequencies $\nu_1 = c/\lambda_1$ and $\nu_2 = c/\lambda_2$:</p>
<div class="math-display">
$$e V_{01} = h \\nu_1 - W_0 = \\frac{h c}{\\lambda_1} - W_0$$
</div>
<div class="math-display">
$$e V_{02} = h \\nu_2 - W_0 = \\frac{h c}{\\lambda_2} - W_0$$
</div>
<p>Subtracting the second equation from the first eliminates the work function $W_0$:</p>
<div class="math-display">
$$e (V_{01} - V_{02}) = h c \\left( \\frac{1}{\\lambda_1} - \\frac{1}{\\lambda_2} \\right)$$
</div>
<div class="math-display">
$$V_{01} - V_{02} = 2.24\\,\\text{V} - 0.86\\,\\text{V} = 1.38\\,\\text{V}$$
</div>
<div class="math-display">
$$\\frac{1}{\\lambda_1} - \\frac{1}{\\lambda_2} = \\frac{1}{300 \\times 10^{-9}} - \\frac{1}{450 \\times 10^{-9}} = 3.333 \\times 10^6 - 2.222 \\times 10^6 = 1.111 \\times 10^6\\,\\text{m}^{-1}$$
</div>

<p><strong>Step 2: Calculate Planck's Constant $h$</strong></p>
<div class="math-display">
$$h = \\frac{e (V_{01} - V_{02})}{c \\left( \\frac{1}{\\lambda_1} - \\frac{1}{\\lambda_2} \\right)} = \\frac{(1.602 \\times 10^{-19}\\,\\text{C})(1.38\\,\\text{V})}{(3.0 \\times 10^8\\,\\text{m/s})(1.111 \\times 10^6\\,\\text{m}^{-1})} = \\frac{2.2108 \\times 10^{-19}}{3.333 \\times 10^{14}} \\approx 6.63 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}$$
</div>

<p><strong>Step 3: Calculate Work Function $W_0$</strong></p>
<div class="math-display">
$$\\frac{h c}{\\lambda_1} = \\frac{1240\\,\\text{eV}\\cdot\\text{nm}}{300\\,\\text{nm}} \\approx 4.133\\,\\text{eV}$$
</div>
<div class="math-display">
$$W_0 = \\frac{h c}{\\lambda_1} - e V_{01} = 4.133\\,\\text{eV} - 2.24\\,\\text{eV} = 1.893\\,\\text{eV} \\approx 1.89\\,\\text{eV}$$
</div>

<p><strong>Step 4: Threshold Frequency and Wavelength</strong></p>
<div class="math-display">
$$\\lambda_0 = \\frac{h c}{W_0} = \\frac{1240\\,\\text{eV}\\cdot\\text{nm}}{1.893\\,\\text{eV}} \\approx 655\\,\\text{nm}$$
</div>
<div class="math-display">
$$\\nu_0 = \\frac{c}{\\lambda_0} = \\frac{3.0 \\times 10^8\\,\\text{m/s}}{655 \\times 10^{-9}\\,\\text{m}} \\approx 4.58 \\times 10^{14}\\,\\text{Hz}$$
</div>

<p><strong>Step 5: Maximum Speed of Photoelectrons</strong></p>
<div class="math-display">
$$K_{max} = e V_{01} = 2.24\\,\\text{eV} = 2.24 \\times 1.602 \\times 10^{-19}\\,\\text{J} = 3.588 \\times 10^{-19}\\,\\text{J}$$
</div>
<div class="math-display">
$$v_{max} = \\sqrt{\\frac{2 K_{max}}{m_e}} = \\sqrt{\\frac{2(3.588 \\times 10^{-19}\\,\\text{J})}{9.109 \\times 10^{-31}\\,\\text{kg}}} = \\sqrt{7.878 \\times 10^{11}} \\approx 8.88 \\times 10^5\\,\\text{m/s}$$
</div>"""
        },
        {
            "id": "u2-prob2",
            "title": "Compton Scattering Energy & Recoil Electron Dynamics",
            "statement": "A gamma-ray photon with energy E = 0.511\\,\\text{MeV} (equal to the rest mass energy of an electron) collides with a stationary free electron and is scattered at an angle of \\theta = 60^\\circ. Calculate: (a) The incident photon wavelength \\lambda, (b) The Compton shift \\Delta \\lambda and the scattered photon wavelength \\lambda', (c) The scattered photon energy E', (d) The kinetic energy of the recoil electron K_e, and (e) The recoil angle \\phi of the electron.",
            "solution": """<p><strong>Step 1: Calculate Incident Photon Wavelength $\\lambda$</strong></p>
<p>Since $E = h\nu = m_0 c^2$, the incident wavelength equals precisely the Compton wavelength $\lambda_c$:</p>
<div class="math-display">
$$\\lambda = \\frac{h c}{E} = \\frac{h c}{m_0 c^2} = \\frac{h}{m_0 c} = \\lambda_c = 0.02426\\,\\text{\\AA} = 2.426\\,\\text{pm}$$
</div>

<p><strong>Step 2: Calculate Compton Shift $\\Delta \\lambda$ and Scattered Wavelength $\\lambda'$</strong></p>
<div class="math-display">
$$\\Delta \\lambda = \\lambda_c (1 - \\cos 60^\\circ) = \\lambda_c (1 - 0.5) = 0.5 \\lambda_c = 0.5 \\times 2.426\\,\\text{pm} = 1.213\\,\\text{pm}$$
</div>
<div class="math-display">
$$\\lambda' = \\lambda + \\Delta \\lambda = 2.426\\,\\text{pm} + 1.213\\,\\text{pm} = 3.639\\,\\text{pm} = 1.5 \\lambda_c$$
</div>

<p><strong>Step 3: Calculate Scattered Photon Energy $E'$</strong></p>
<div class="math-display">
$$E' = \\frac{h c}{\\lambda'} = \\frac{h c}{1.5 \\lambda_c} = \\frac{E}{1.5} = \\frac{0.511\\,\\text{MeV}}{1.5} \\approx 0.3407\\,\\text{MeV} = 340.7\\,\\text{keV}$$
</div>

<p><strong>Step 4: Calculate Kinetic Energy of Recoil Electron $K_e$</strong></p>
<div class="math-display">
$$K_e = E - E' = 511.0\\,\\text{keV} - 340.7\\,\\text{keV} = 170.3\\,\\text{keV}$$
</div>

<p><strong>Step 5: Calculate Recoil Angle $\\phi$</strong></p>
<p>From momentum conservation perpendicular and parallel to the incident beam:</p>
<div class="math-display">
$$\\tan\\phi = \\frac{p' \\sin\\theta}{p - p' \\cos\\theta} = \\frac{\\frac{E'}{c} \\sin\\theta}{\\frac{E}{c} - \\frac{E'}{c} \\cos\\theta} = \\frac{\\sin 60^\\circ}{\\frac{E}{E'} - \\cos 60^\\circ} = \\frac{0.8660}{1.5 - 0.5} = \\frac{0.8660}{1.0} = 0.8660$$
</div>
<div class="math-display">
$$\\phi = \\arctan(0.8660) = 40.89^\\circ$$
</div>"""
        },
        {
            "id": "u2-prob3",
            "title": "Duane-Hunt Cutoff & Moseley's Law X-Ray Tube Analysis",
            "statement": "An X-ray tube operates with an accelerating voltage of V = 50\\,\\text{kV}$. (a) Calculate the Duane-Hunt minimum wavelength \\lambda_{min} of the continuous Bremsstrahlung spectrum. (b) If the anode target is replaced by an unknown element whose characteristic K_\\alpha line wavelength is measured to be \\lambda_{K\\alpha} = 0.1542\\,\\text{nm}, use Moseley's law with screening constant \\sigma = 1 to identify the unknown atomic number Z and the chemical element. (c) What is the maximum frequency of the X-ray photons produced?",
            "solution": """<p><strong>Step 1: Calculate Duane-Hunt Minimum Wavelength $\\lambda_{min}$</strong></p>
<div class="math-display">
$$\\lambda_{min} = \\frac{h c}{e V} = \\frac{12,398\\,\\text{V}\\cdot\\text{\\AA}}{50,000\\,\\text{V}} = 0.2480\\,\\text{\\AA} = 0.0248\\,\\text{nm} = 24.8\\,\\text{pm}$$
</div>

<p><strong>Step 2: Calculate Maximum Photon Frequency $\\nu_{max}$</strong></p>
<div class="math-display">
$$\\nu_{max} = \\frac{c}{\\lambda_{min}} = \\frac{3.0 \\times 10^8\\,\\text{m/s}}{2.480 \\times 10^{-11}\\,\\text{m}} \\approx 1.21 \\times 10^{19}\\,\\text{Hz}$$
</div>

<p><strong>Step 3: Determine Atomic Number $Z$ via Moseley's Law</strong></p>
<p>The frequency of the $K_\\alpha$ line is:</p>
<div class="math-display">
$$\\nu = \\frac{c}{\\lambda_{K\\alpha}} = \\frac{3.0 \\times 10^8\\,\\text{m/s}}{0.1542 \\times 10^{-9}\\,\\text{m}} \\approx 1.9455 \\times 10^{18}\\,\\text{Hz}$$
</div>
<p>From Bohr's formula for $K_\\alpha$ ($n = 2 \\to n = 1$ with $\\sigma = 1$):</p>
<div class="math-display">
$$\\nu = \\frac{3}{4} c R_\\infty (Z - 1)^2$$
</div>
<p>Using Rydberg constant $R_\\infty = 1.09737 \\times 10^7\\,\\text{m}^{-1}$:</p>
<div class="math-display">
$$\\frac{3}{4} c R_\\infty = \\frac{3}{4} \\times (2.9979 \\times 10^8\\,\\text{m/s}) \\times (1.09737 \\times 10^7\\,\\text{m}^{-1}) = 2.4674 \\times 10^{15}\\,\\text{Hz}$$
</div>
<div class="math-display">
$$(Z - 1)^2 = \\frac{\\nu}{\\frac{3}{4} c R_\\infty} = \\frac{1.9455 \\times 10^{18}}{2.4674 \\times 10^{15}} = 788.48$$
</div>
<div class="math-display">
$$Z - 1 = \\sqrt{788.48} \\approx 28.08 \\implies Z \\approx 29$$
</div>
<p>Atomic number $Z = 29$ corresponds precisely to <strong>Copper ($\text{Cu}$)</strong>, whose celebrated $K_\alpha$ emission line at $1.5418\,\text{\AA}$ is the universal laboratory standard for X-ray diffraction worldwide.</p>"""
        }
    ]
}

with open("amp_u1.json", "w") as f:
    json.dump(unit1, f, indent=2)

with open("amp_u2.json", "w") as f:
    json.dump(unit2, f, indent=2)

print("amp_u1.json and amp_u2.json generated successfully!")
