# Unit 7 & Unit 8 Builder for Classical Mechanics & Special Relativity
import json

u7 = {
    "unitNumber": 7,
    "number": 7,
    "title": "Special Theory of Relativity: Kinematics & Transformations",
    "subtitle": "Michelson-Morley Experiment, Postulates, Lorentz Transformations, Simultaneity, Dilation & Relativistic Addition",
    "description": "Historical failure of Galilean relativity, the Michelson-Morley null experiment, Einstein's two postulates of Special Relativity, rigorous derivation of the Lorentz transformation equations, relativity of simultaneity, kinematic time dilation, Lorentz-Fitzgerald length contraction, relativistic velocity addition theorem, and relativistic longitudinal & transverse Doppler shifts.",
    "topics": [
        "Failure of Galilean Relativity & Ether Drift",
        "Michelson-Morley Interferometer Experiment",
        "Einstein's Two Postulates of Special Relativity",
        "Derivation of the Lorentz Transformation Equations",
        "Relativity of Simultaneity & Causality",
        "Time Dilation & Muon Decay Verification",
        "Length Contraction & Relativistic Velocity Addition"
    ],
    "sections": [
        {
            "id": "u7-sec1",
            "title": "Breakdown of Galilean Relativity & The Michelson-Morley Experiment",
            "content": """
<h4>1. The Galilean Transformation & The Classical Velocity Addition</h4>
In Newtonian mechanics, space and time are absolute entities independent of the observer. For two inertial reference frames $S$ and $S'$ with parallel axes where $S'$ moves along the positive $x$-axis with constant speed $v$ relative to $S$, the <strong>Galilean transformation</strong> is:
<div class="math-display">$$x' = x - v t, \\quad y' = y, \\quad z' = z, \\quad t' = t$$</div>
Differentiating with respect to the absolute time $t = t'$ yields the Galilean velocity addition law:
<div class="math-display">$$\\vec{u}' = \\vec{u} - \\vec{v}$$</div>
While Newton's laws of mechanics are invariant under Galilean transformations, <strong>Maxwell's equations of electrodynamics are not</strong>. Maxwell's equations predict that electromagnetic waves propagate in vacuum at a universal constant speed:
<div class="math-display">$$c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 2.9979 \\times 10^8 \\text{ m/s}$$</div>
Under Galilean transformations, an observer moving through the putative luminiferous ether at speed $v$ should measure a variable light speed $c' = c \\pm v$.

<h4>2. The Michelson-Morley Interferometer Experiment (1887)</h4>
Albert A. Michelson and Edward W. Morley devised a high-precision optical interferometer floating on a pool of mercury to detect the Earth's orbital velocity through the ether ($v_{\\text{Earth}} \\approx 30 \\text{ km/s}$, $v/c \\approx 10^{-4}$).
A monochromatic beam of light from source $S$ is split by a half-silvered mirror into two mutually perpendicular paths of length $L_1$ and $L_2$:
<ul>
  <li><strong>Longitudinal Arm (Parallel to Ether Wind):</strong> The light travels downstream at speed $c - v$ and upstream at $c + v$. The round-trip transit time is:
  <div class="math-display">$$t_\\parallel = \\frac{L_1}{c - v} + \\frac{L_1}{c + v} = \\frac{2 L_1 c}{c^2 - v^2} = \\frac{2 L_1}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1} \\approx \\frac{2 L_1}{c} \\left( 1 + \\frac{v^2}{c^2} \\right)$$</div></li>
  <li><strong>Transverse Arm (Perpendicular to Ether Wind):</strong> By the Pythagorean theorem, the effective light speed is $\\sqrt{c^2 - v^2}$. The round-trip time is:
  <div class="math-display">$$t_\\perp = \\frac{2 L_2}{\\sqrt{c^2 - v^2}} = \\frac{2 L_2}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1/2} \\approx \\frac{2 L_2}{c} \\left( 1 + \\frac{1}{2}\\frac{v^2}{c^2} \\right)$$</div></li>
</ul>
Setting $L_1 = L_2 = L$, the round-trip time difference is:
<div class="math-display">$$\\Delta t = t_\\parallel - t_\\perp \\approx \\frac{L}{c} \\frac{v^2}{c^2}$$</div>
Rotating the apparatus by $90^\\circ$ exchanges the roles of the arms, doubling the time difference to $2\\Delta t$. The expected fringe shift on the detector was:
<div class="math-display">$$\\Delta N = \\frac{c (2\\Delta t)}{\\lambda} = \\frac{2 L v^2}{\\lambda c^2} \\approx 0.4 \\text{ fringes}$$</div>
The experiment was sensitive to $0.01$ fringes, yet <strong>no fringe shift was observed</strong>. The ether drift was conclusively zero.
"""
        },
        {
            "id": "u7-sec2",
            "title": "Einstein's Postulates & Derivation of Lorentz Transformations",
            "content": """
<h4>1. Einstein's Two Postulates of Special Relativity (1905)</h4>
Albert Einstein resolved the conflict between Newtonian mechanics and Maxwellian electrodynamics by abandoning absolute Newtonian space and time, founding the Special Theory of Relativity on two postulates:
<ol>
  <li><strong>The Principle of Relativity:</strong> The laws of physics take identical mathematical forms in all inertial reference frames. No physical experiment can distinguish between absolute rest and uniform rectilinear motion.</li>
  <li><strong>The Constancy of the Speed of Light:</strong> The speed of light in vacuum is an absolute universal constant $c$ in all inertial frames, independent of the motion of the emitting source or the observer.</li>
</ol>

<h4>2. Mathematical Derivation of the Lorentz Transformations</h4>
Let frame $S'$ move at speed $v$ along the $x$-axis of frame $S$. Due to homogeneity of space and time, the transformation must be linear:
<div class="math-display">$$x' = \\gamma(x - v t), \\quad y' = y, \\quad z' = z$$</div>
By the relativity postulate, the inverse transformation must be identical with $v \\to -v$:
<div class="math-display">$$x = \\gamma(x' + v t')$$</div>
Consider a spherical light wave emitted from the coincident origins at $t = t' = 0$. The wavefront is described in both frames by:
<div class="math-display">$$x^2 + y^2 + z^2 - c^2 t^2 = 0, \\quad x'^2 + y'^2 + z'^2 - c^2 t'^2 = 0$$</div>
Since $y' = y$ and $z' = z$, along the $x$-axis $x = c t$ and $x' = c t'$. Substituting into the transformation equations:
<div class="math-display">$$c t' = \\gamma(c - v) t, \\quad c t = \\gamma(c + v) t'$$</div>
Multiplying the two equations:
<div class="math-display">$$c^2 t t' = \\gamma^2 (c^2 - v^2) t t' \\implies \\gamma^2 = \\frac{c^2}{c^2 - v^2} = \\frac{1}{1 - v^2/c^2}$$</div>
Taking the positive root (preserving direction of time):
<div class="math-display">$$\\gamma = \\frac{1}{\\sqrt{1 - \\beta^2}}, \\quad \\beta = \\frac{v}{c}$$</div>
Substituting $x' = \\gamma(x - vt)$ into $x = \\gamma(x' + vt')$ to solve for $t'$:
<div class="math-display">$$x = \\gamma[\\gamma(x - vt) + vt'] \\implies \\frac{x}{\\gamma} - \\gamma(x - vt) = \\gamma vt'$$</div>
<div class="math-display">$$t' = \\gamma \\left( t - \\frac{v x}{c^2} \\right)$$</div>
Collecting the <strong>Lorentz Transformation Equations</strong>:
<div class="math-display">$$x' = \\gamma (x - v t), \\quad y' = y, \\quad z' = z, \\quad t' = \\gamma \\left( t - \\frac{v x}{c^2} \\right)$$</div>
"""
        },
        {
            "id": "u7-sec3",
            "title": "Relativity of Simultaneity, Time Dilation & Length Contraction",
            "content": """
<h4>1. The Relativity of Simultaneity</h4>
Consider two spatial events $A$ and $B$ that occur simultaneously at different spatial locations in frame $S$: $\\Delta t = t_B - t_A = 0$ with $\\Delta x = x_B - x_A \\neq 0$.
In the moving frame $S'$, the time difference is:
<div class="math-display">$$\\Delta t' = \\gamma \\left( \\Delta t - \\frac{v \\Delta x}{c^2} \\right) = -\\gamma \\frac{v \\Delta x}{c^2} \\neq 0$$</div>
<p><strong>Crucial Consequence:</strong> Two spatially separated events that are simultaneous in one inertial frame are <em>never</em> simultaneous in any other inertial frame moving relative to it. Absolute simultaneity is physically meaningless.</p>

<h4>2. Kinematic Time Dilation</h4>
Let a clock be located at a fixed position in frame $S'$ ($x_1' = x_2'$, so $\\Delta x' = 0$). The time interval between two ticks measured by this clock is the <strong>proper time</strong> $\\Delta t_0 = \\Delta t' = \\tau$.
In frame $S$, using the inverse Lorentz transformation $t = \\gamma(t' + v x'/c^2)$:
<div class="math-display">$$\\Delta t = \\gamma \\Delta t' = \\gamma \\Delta t_0 = \\frac{\\Delta t_0}{\\sqrt{1 - v^2/c^2}} > \\Delta t_0$$</div>
<p><strong>Moving Clocks Run Slow:</strong> A clock moving relative to an observer ticks slower by a factor of $\\gamma$.</p>
<p><em>Experimental Proof:</em> High-energy cosmic-ray muons created in the upper atmosphere ($\sim 15\\text{ km}$) travel at $v \\approx 0.999c$ ($\\gamma \\approx 22.4$). Their laboratory lifetime expands from $\\tau_0 = 2.2 \\;\\mu\\text{s}$ to $\\Delta t = 49.3 \\;\\mu\\text{s}$, allowing them to survive and reach ground-level detectors.</p>

<h4>3. Lorentz-Fitzgerald Length Contraction</h4>
Let a rod lie at rest along the $x'$-axis in frame $S'$. Its <strong>proper length</strong> is $L_0 = x_2' - x_1'$.
To measure the length $L = x_2 - x_1$ in frame $S$, the coordinates of both ends must be measured <em>simultaneously</em> at $t_1 = t_2$ ($\\Delta t = 0$).
Applying the Lorentz transformation $x' = \\gamma(x - vt)$:
<div class="math-display">$$L_0 = x_2' - x_1' = \\gamma(x_2 - x_1) - \\gamma v(t_2 - t_1) = \\gamma L$$</div>
<div class="math-display">$$L = \\frac{L_0}{\\gamma} = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} < L_0$$</div>
<p><strong>Moving Objects Contract:</strong> The physical length of an object is contracted along its direction of motion by factor $1/\\gamma$. Dimensions perpendicular to the velocity ($y, z$) remain completely unaffected.</p>
"""
        },
        {
            "id": "u7-sec4",
            "title": "Relativistic Velocity Addition & The Relativistic Doppler Effect",
            "content": """
<h4>1. Relativistic Velocity Transformation Formula</h4>
Let a particle move with velocity $\\vec{u} = (u_x, u_y, u_z) = (dx/dt, dy/dt, dz/dt)$ in frame $S$. In frame $S'$:
<div class="math-display">$$dx' = \\gamma(dx - v dt), \\quad dy' = dy, \\quad dz' = dz, \\quad dt' = \\gamma\\left(dt - \\frac{v dx}{c^2}\\right)$$</div>
Dividing $dx'$ by $dt'$:
<div class="math-display">$$u_x' = \\frac{dx'}{dt'} = \\frac{\\gamma(dx - v dt)}{\\gamma\\left(dt - \\frac{v dx}{c^2}\\right)} = \\frac{\\frac{dx}{dt} - v}{1 - \\frac{v}{c^2}\\frac{dx}{dt}} = \\frac{u_x - v}{1 - \\frac{u_x v}{c^2}}$$</div>
For transverse components:
<div class="math-display">$$u_y' = \\frac{dy'}{dt'} = \\frac{u_y}{\\gamma \\left(1 - \\frac{u_x v}{c^2}\\right)}, \\quad u_z' = \\frac{dz'}{dt'} = \\frac{u_z}{\\gamma \\left(1 - \\frac{u_x v}{c^2}\\right)}$$</div>
<p><strong>Universal Speed Limit:</strong> If a photon travels at $u_x = c$, then in any frame moving at speed $v$:
<div class="math-display">$$u_x' = \\frac{c - v}{1 - \\frac{c v}{c^2}} = \\frac{c - v}{1 - v/c} = c$$</div>
The speed of light $c$ is invariant under velocity addition. No compounding of sub-luminal velocities can ever exceed $c$.</p>

<h4>2. Relativistic Doppler Effect</h4>
For an electromagnetic source emitting frequency $\\nu_0$ moving at speed $v$ relative to an observer:
<ul>
  <li><strong>Longitudinal Doppler Effect (Source Moving Away):</strong>
  <div class="math-display">$$\\nu = \\nu_0 \\sqrt{\\frac{1 - v/c}{1 + v/c}} = \\nu_0 \\frac{\\sqrt{1 - \\beta^2}}{1 + \\beta}$$</div>
  The observed wavelength is redshifted: $\\lambda = \\lambda_0 \\sqrt{\\frac{1 + \\beta}{1 - \\beta}}$.</li>
  <li><strong>Transverse Doppler Effect ($\theta = 90^\\circ$):</strong>
  When the source moves perpendicular to the line of sight:
  <div class="math-display">$$\\nu_{\\perp} = \\frac{\\nu_0}{\\gamma} = \\nu_0 \\sqrt{1 - \\frac{v^2}{c^2}}$$</div>
  A purely relativistic phenomenon resulting directly from time dilation (predicted to be exactly zero in classical physics).</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-7-1",
            "title": "Muon Atmospheric Decay: Time Dilation vs. Length Contraction",
            "statement": "Muons are created at an altitude of $h = 10.0\\text{ km}$ above sea level and travel vertically downward toward Earth at $v = 0.998 c$. The proper rest lifetime of a muon is $\\tau_0 = 2.20 \\;\\mu\\text{s}$. (a) Calculate the fraction of muons that survive to reach sea level in the Earth observer frame. (b) Re-evaluate the problem in the muon's rest frame using length contraction.",
            "steps": [
                {
                    "step": "Step 1: Compute the Lorentz Factor γ",
                    "math": "$$\\beta = 0.998 \\implies \\gamma = \\frac{1}{\\sqrt{1 - (0.998)^2}} = \\frac{1}{\\sqrt{0.003996}} \\approx 15.82$$",
                    "explanation": "The relativistic time dilation and length contraction factor is $\\gamma \\approx 15.82$."
                },
                {
                    "step": "Step 2: Earth Frame Calculation (Time Dilation)",
                    "math": "$$\\Delta t_{\\text{lab}} = \\frac{h}{v} = \\frac{10^4 \\text{ m}}{0.998 \\times 3 \\times 10^8 \\text{ m/s}} = 33.40 \\;\\mu\\text{s}, \\quad \\tau_{\\text{lab}} = \\gamma \\tau_0 = 15.82 \\times 2.20 = 34.80 \\;\\mu\\text{s}$$",
                    "explanation": "The survival fraction according to radioactive exponential decay $N/N_0 = e^{-\\Delta t / \\tau}$ is $e^{-33.40 / 34.80} = e^{-0.9598} \\approx 0.383$ (38.3% survive). Without relativity, $N/N_0 = e^{-33.40/2.20} = e^{-15.18} \\approx 2.5 \\times 10^{-7}$."
                },
                {
                    "step": "Step 3: Muon Frame Calculation (Length Contraction)",
                    "math": "$$h' = \\frac{h}{\\gamma} = \\frac{10.0 \\text{ km}}{15.82} = 632.1 \\text{ m}, \\quad \\Delta t' = \\frac{h'}{v} = \\frac{632.1}{0.998 c} = 2.112 \\;\\mu\\text{s}$$",
                    "explanation": "In the muon's frame, the clock ticks at normal proper rate $\\tau_0 = 2.20 \\;\\mu\\text{s}$, but the atmosphere is contracted to $632.1\\text{ m}$. Survival fraction: $N/N_0 = e^{-\\Delta t' / \\tau_0} = e^{-2.112 / 2.20} = e^{-0.960} \\approx 0.383$, yielding identical physical predictions."
                }
            ],
            "answer": "Survival fraction is 38.3% in both frames, demonstrating the physical equivalence of time dilation (Earth frame) and length contraction (muon frame)."
        },
        {
            "id": "cm-prob-7-2",
            "title": "Relativistic Head-On Spacecraft Velocity Composition",
            "statement": "Two starships $A$ and $B$ approach each other head-on as observed from a space station. Starship $A$ travels at $u_A = 0.80 c$ to the right, and starship $B$ travels at $u_B = 0.90 c$ to the left. (a) Calculate the speed of starship $B$ relative to starship $A$. (b) If starship $A$ fires a laser pulse toward $B$, calculate the speed of the laser pulse as measured by $B$.",
            "steps": [
                {
                    "step": "Step 1: Set Up the Relativistic Velocity Transformation",
                    "math": "$$u_x' = \\frac{u_x - v}{1 - \\frac{u_x v}{c^2}}$$",
                    "explanation": "Let frame $S$ be the space station. Frame $S'$ is attached to starship $A$, so $v = +0.80 c$. The velocity of starship $B$ in $S$ is $u_x = -0.90 c$."
                },
                {
                    "step": "Step 2: Calculate Relative Velocity of Starship B",
                    "math": "$$u_B' = \\frac{-0.90 c - 0.80 c}{1 - \\frac{(-0.90 c)(0.80 c)}{c^2}} = \\frac{-1.70 c}{1 - (-0.72)} = \\frac{-1.70 c}{1.72} \\approx -0.9884 c$$",
                    "explanation": "The relative approach speed is $0.9884 c$, strictly less than $c$. Classical Galilean addition would have given an unphysical $1.70 c$."
                },
                {
                    "step": "Step 3: Laser Pulse Speed Measured by B",
                    "math": "$$u_{\\text{laser}}' = \\frac{c - (-0.9884 c)}{1 - \\frac{c(-0.9884 c)}{c^2}} = \\frac{c(1 + 0.9884)}{1 + 0.9884} = c$$",
                    "explanation": "By Einstein's second postulate, light travels at speed $c$ in all inertial reference frames regardless of relative velocities."
                }
            ],
            "answer": "(a) Relative speed of B as seen by A is 0.9884 c. (b) Laser pulse speed measured by B is exactly c."
        },
        {
            "id": "cm-prob-7-3",
            "title": "Cosmological Redshift & Relativistic Doppler Shift of a Quasar",
            "statement": "A distant quasar emits the Lyman-alpha spectral line of atomic hydrogen at rest wavelength $\\lambda_0 = 121.6\\text{ nm}$. The spectral line is observed on Earth at a redshifted wavelength $\\lambda_{\\text{obs}} = 486.4\\text{ nm}$. Determine the recession velocity $v/c$ of the quasar.",
            "steps": [
                {
                    "step": "Step 1: Relate Observed and Rest Wavelengths to Relativistic Doppler Formula",
                    "math": "$$\\frac{\\lambda_{\\text{obs}}}{\\lambda_0} = \\sqrt{\\frac{1 + \\beta}{1 - \\beta}} = 1 + z$$",
                    "explanation": "The measured redshift parameter is $z = \\frac{\\lambda_{\\text{obs}} - \\lambda_0}{\\lambda_0} = \\frac{486.4 - 121.6}{121.6} = \\frac{364.8}{121.6} = 3.0$."
                },
                {
                    "step": "Step 2: Square Both Sides and Solve for β = v/c",
                    "math": "$$\\frac{1 + \\beta}{1 - \\beta} = (1 + z)^2 = (1 + 3.0)^2 = 4^2 = 16$$",
                    "explanation": "Cross-multiplying: $1 + \\beta = 16(1 - \\beta) = 16 - 16\\beta$."
                },
                {
                    "step": "Step 3: Solve for Dimensionless Velocity β",
                    "math": "$$17 \\beta = 15 \\implies \\beta = \\frac{v}{c} = \\frac{15}{17} \\approx 0.8824$$",
                    "explanation": "The quasar is receding away from Earth at $88.24\\%$ of the speed of light ($v \\approx 2.65 \\times 10^8\\text{ m/s}$)."
                }
            ],
            "answer": "Recession velocity: v/c = 15/17 ≈ 0.8824 (88.24% of light speed)."
        }
    ]
}

# Unit 8: Relativistic Mechanics & Spacetime Dynamics
u8 = {
    "unitNumber": 8,
    "number": 8,
    "title": "Relativistic Mechanics & Four-Vectors",
    "subtitle": "Minkowski Spacetime, Invariant Intervals, 4-Momentum, Mass-Energy Equivalence & Compton Scattering",
    "description": "Foundations of four-dimensional Minkowski spacetime, metric tensor η_μν, invariant spacetime intervals (timelike, spacelike, null), light cones, proper time, four-velocity, relativistic momentum, relativistic kinetic energy, universal mass-energy equivalence E=mc², four-momentum invariant E² = p²c² + m²c⁴, Minkowski four-force, and particle collision dynamics with Compton scattering.",
    "topics": [
        "Four-Dimensional Minkowski Spacetime & Metric Tensor",
        "Invariant Spacetime Intervals & Light Cone Geometry",
        "Proper Time & Four-Velocity Vector",
        "Relativistic Momentum & Relativistic Mass",
        "Relativistic Work-Energy Theorem & Kinetic Energy",
        "Mass-Energy Equivalence (E = mc²) & Four-Momentum",
        "Minkowski Four-Force & Compton Scattering"
    ],
    "sections": [
        {
            "id": "u8-sec1",
            "title": "Minkowski Four-Dimensional Spacetime & Invariant Intervals",
            "content": """
<h4>1. The Four-Vector Formalism</h4>
In 1908, Hermann Minkowski recognized that Special Relativity unifies three-dimensional space and one-dimensional time into a single four-dimensional continuum: <strong>spacetime</strong>.
An event is specified by a contravariant position four-vector $x^\\mu$ ($\\mu = 0, 1, 2, 3$):
<div class="math-display">$$x^\\mu = (x^0, x^1, x^2, x^3) = (c t, x, y, z)$$</div>
The Minkowski spacetime metric tensor $\\eta_{\\mu\\nu}$ in the mostly-minus convention is:
<div class="math-display">$$\\eta_{\\mu\\nu} = \\begin{pmatrix} 1 & 0 & 0 & 0 \\\\ 0 & -1 & 0 & 0 \\\\ 0 & 0 & -1 & 0 \\\\ 0 & 0 & 0 & -1 \\end{pmatrix}$$</div>
Lowering indices via the metric defines the covariant four-vector $x_\\mu = \\eta_{\\mu\\nu} x^\\nu = (c t, -x, -y, -z)$.

<h4>2. The Invariant Spacetime Interval</h4>
The scalar product of the infinitesimal displacement four-vector $dx^\\mu$ with itself defines the <strong>invariant spacetime interval</strong> $ds^2$:
<div class="math-display">$$ds^2 = dx_\\mu dx^\\mu = \\eta_{\\mu\\nu} dx^\\mu dx^\\nu = c^2 dt^2 - dx^2 - dy^2 - dz^2$$</div>
<p><strong>Lorentz Invariance:</strong> $ds^2$ is an absolute scalar: its numerical value is identical for all inertial observers: $ds^2 = ds'^2$.</p>

<h4>3. Causal Structure & Light Cones</h4>
The sign of $ds^2$ categorizes the causal connection between two spacetime events:
<ul>
  <li><strong>Timelike Interval ($ds^2 > 0$):</strong> $c^2 \\Delta t^2 > \\Delta \\vec{r}^2$. A physical signal traveling at speed $v < c$ can connect the two events. A reference frame exists where the events occur at the exact same spatial location. Events lie within the future or past <strong>light cone</strong>.</li>
  <li><strong>Spacelike Interval ($ds^2 < 0$):</strong> $c^2 \\Delta t^2 < \\Delta \\vec{r}^2$. No physical signal can travel between the events without exceeding $c$. A reference frame exists where the events occur simultaneously ($\\Delta t' = 0$). Events lie outside the light cone.</li>
  <li><strong>Lightlike / Null Interval ($ds^2 = 0$):</strong> $c^2 \\Delta t^2 = \\Delta \\vec{r}^2$. Events can be connected only by photons traveling at speed $c$. Events lie on the boundary surface of the light cone.</li>
</ul>
"""
        },
        {
            "id": "u8-sec2",
            "title": "Proper Time, Four-Velocity & Relativistic Momentum",
            "content": """
<h4>1. Proper Time $\\tau$</h4>
The <strong>proper time</strong> $d\\tau$ is the time interval measured by a clock carried along with the moving particle ($d\\vec{r}' = 0$ in the instantaneous rest frame):
<div class="math-display">$$ds^2 = c^2 d\\tau^2 \\implies d\\tau = \\frac{ds}{c} = \\sqrt{dt^2 - \\frac{d\\vec{r}^2}{c^2}} = dt \\sqrt{1 - \\frac{u^2}{c^2}} = \\frac{dt}{\\gamma}$$</div>
Since $ds$ and $c$ are Lorentz invariants, <strong>proper time $\\tau$ is a Lorentz scalar</strong>.

<h4>2. Four-Velocity Vector $U^\\mu$</h4>
Differentiating the position four-vector $x^\\mu$ with respect to the invariant proper time $\\tau$:
<div class="math-display">$$U^\\mu = \\frac{dx^\\mu}{d\\tau} = \\gamma \\frac{dx^\\mu}{dt} = \\gamma (c, \\vec{u}) = (\\gamma c, \\gamma u_x, \\gamma u_y, \\gamma u_z)$$</div>
The invariant magnitude of the four-velocity is universally constant:
<div class="math-display">$$U^\\mu U_\\mu = \\gamma^2 (c^2 - u^2) = \\frac{c^2 - u^2}{1 - u^2/c^2} = c^2 = \\text{constant for all particles}$$</div>

<h4>3. Relativistic Momentum & Four-Momentum $P^\\mu$</h4>
Multiplying the four-velocity by the invariant rest mass $m$:
<div class="math-display">$$P^\\mu = m U^\\mu = (\\gamma m c, \\gamma m \\vec{u})$$</div>
The spatial part gives the <strong>relativistic three-momentum</strong>:
<div class="math-display">$$\\vec{p} = \\gamma m \\vec{u} = \\frac{m \\vec{u}}{\\sqrt{1 - u^2/c^2}}$$</div>
Notice that as particle speed approaches light speed ($u \\to c$), $\\gamma \\to \\infty$, so $\\vec{p} \\to \\infty$. An infinite amount of momentum (and energy) is required to accelerate any massive body to $c$.
"""
        },
        {
            "id": "u8-sec3",
            "title": "Relativistic Work-Energy Theorem & Mass-Energy Equivalence",
            "content": """
<h4>1. Derivation of Relativistic Kinetic Energy</h4>
Newton's Second Law in relativistic mechanics defines force as the time rate of change of relativistic momentum: $\\vec{F} = \\frac{d\\vec{p}}{dt} = \\frac{d}{dt}(\\gamma m \\vec{u})$.
The work done by the force in moving a particle from rest to velocity $\\vec{u}$ is:
<div class="math-display">$$W = \\int_0^{\\vec{r}} \\vec{F} \\cdot d\\vec{r} = \\int_0^t \\frac{d\\vec{p}}{dt} \\cdot \\vec{u} dt = \\int_0^{\\vec{p}} \\vec{u} \\cdot d\\vec{p}$$</div>
Integrating by parts:
<div class="math-display">$$W = \\vec{u} \\cdot \\vec{p} - \\int_0^{\\vec{u}} \\vec{p} \\cdot d\\vec{u} = \\gamma m u^2 - \\int_0^u \\frac{m u du}{\\sqrt{1 - u^2/c^2}}$$</div>
Evaluating the integral:
<div class="math-display">$$\\int_0^u \\frac{m u du}{\\sqrt{1 - u^2/c^2}} = \\left[ -m c^2 \\sqrt{1 - u^2/c^2} \\right]_0^u = m c^2 - \\frac{m c^2}{\\gamma}$$</div>
Substituting back:
<div class="math-display">$$W = \\gamma m u^2 + \\frac{m c^2}{\\gamma} - m c^2 = m c^2 \\left( \\frac{\\gamma^2 u^2/c^2 + 1}{\\gamma} \\right) - m c^2 = \\gamma m c^2 - m c^2$$</div>
Since initial kinetic energy at rest was zero, the <strong>relativistic kinetic energy</strong> $K$ is:
<div class="math-display">$$K = (\\gamma - 1) m c^2$$</div>
<p><strong>Non-Relativistic Limit ($u \\ll c$):</strong> Expanding $\\gamma = (1 - u^2/c^2)^{-1/2} \\approx 1 + \\frac{1}{2}\\frac{u^2}{c^2} + \\frac{3}{8}\\frac{u^4}{c^4} + \\dots$:
<div class="math-display">$$K = \\left( 1 + \\frac{1}{2}\\frac{u^2}{c^2} - 1 \\right) m c^2 = \\frac{1}{2}m u^2$$</div>
reproducing classical Newtonian kinetic energy.</p>

<h4>2. Mass-Energy Equivalence ($E = mc^2$)</h4>
Einstein defined the <strong>total relativistic energy</strong> $E$ as the sum of kinetic energy and rest-mass energy $E_0$:
<div class="math-display">$$E = K + m c^2 = (\\gamma - 1)m c^2 + m c^2 = \\gamma m c^2$$</div>
When the particle is at rest ($u = 0, \\gamma = 1$), it retains an intrinsic <strong>rest mass energy</strong>:
<div class="math-display">$$E_0 = m c^2$$</div>
<p>Mass and energy are fundamentally equivalent: mass is concentrated, latent energy ($1\\text{ kg} \\approx 9 \\times 10^{16}\\text{ J}$).</p>

<h4>3. The Four-Momentum Vector & The Energy-Momentum Invariant</h4>
The temporal component of four-momentum is $P^0 = \\gamma m c = E/c$. Thus:
<div class="math-display">$$P^\\mu = \\left( \\frac{E}{c}, \\vec{p} \\right)$$</div>
Evaluating the Lorentz-invariant norm $P^\\mu P_\\mu$:
<div class="math-display">$$P^\\mu P_\\mu = \\left( \\frac{E}{c} \\right)^2 - \\vec{p}^2 = m^2 U^\\mu U_\\mu = m^2 c^2$$</div>
Multiplying by $c^2$ yields the fundamental <strong>Energy-Momentum Relation</strong>:
<div class="math-display">$$E^2 = p^2 c^2 + m^2 c^4$$</div>
For massless particles ($m = 0$, such as photons):
<div class="math-display">$$E = p c \\implies p = \\frac{E}{c} = \\frac{h \\nu}{c} = \\frac{h}{\\lambda}$$</div>
"""
        },
        {
            "id": "u8-sec4",
            "title": "Minkowski Four-Force & Relativistic Collisions",
            "content": """
<h4>1. The Minkowski Four-Force $K^\\mu$</h4>
The relativistic generalization of Newton's Second Law in four-vector form is:
<div class="math-display">$$K^\\mu = \\frac{dP^\\mu}{d\\tau} = \\gamma \\frac{dP^\\mu}{dt} = \\gamma \\left( \\frac{1}{c} \\frac{dE}{dt}, \\frac{d\\vec{p}}{dt} \\right)$$</div>
Since $\\vec{F} = \\frac{d\\vec{p}}{dt}$ and power delivered is $\\frac{dE}{dt} = \\vec{F} \\cdot \\vec{u}$:
<div class="math-display">$$K^\\mu = \\gamma \\left( \\frac{\\vec{F} \\cdot \\vec{u}}{c}, \\vec{F} \\right)$$</div>

<h4>2. Conservation of Four-Momentum in Particle Collisions</h4>
In any closed system of colliding particles, the total four-momentum is strictly conserved:
<div class="math-display">$$\\sum_{i=1}^{N_{\\text{in}}} P_i^\\mu = \\sum_{f=1}^{N_{\\text{out}}} P_f^\\mu$$</div>
This single four-vector relation encapsulates both <strong>conservation of total relativistic energy</strong> ($\\mu = 0$) and <strong>conservation of total three-momentum</strong> ($\\mu = 1, 2, 3$).

<h4>3. Derivation of Compton Scattering</h4>
Consider a photon of initial wavelength $\\lambda$ and four-momentum $P_\\gamma = (E/c, \\vec{p}_\\gamma)$ colliding with an electron of rest mass $m_e$ initially at rest: $P_e = (m_e c, \\vec{0})$.
After scattering at angle $\\theta$, the photon has four-momentum $P_\\gamma' = (E'/c, \\vec{p}_\\gamma')$ and the electron has $P_e'$.
Conservation of four-momentum: $P_\\gamma + P_e = P_\\gamma' + P_e' \\implies P_e' = P_\\gamma - P_\\gamma' + P_e$.
Squaring both sides using $P^\\mu P_\\mu$:
<div class="math-display">$$P_e'^2 = (P_\\gamma - P_\\gamma' + P_e)^2$$</div>
Since $P_e^2 = P_e'^2 = m_e^2 c^2$ and $P_\\gamma^2 = P_\\gamma'^2 = 0$:
<div class="math-display">$$m_e^2 c^2 = -2 P_\\gamma \\cdot P_\\gamma' + 2 P_\\gamma \\cdot P_e - 2 P_\\gamma' \\cdot P_e + m_e^2 c^2$$</div>
<div class="math-display">$$P_\\gamma \\cdot P_\\gamma' = (P_\\gamma - P_\\gamma') \\cdot P_e$$</div>
Evaluating scalar products:
<div class="math-display">$$P_\\gamma \\cdot P_\\gamma' = \\frac{E E'}{c^2} - \\vec{p}_\\gamma \\cdot \\vec{p}_\\gamma' = \\frac{E E'}{c^2}(1 - \\cos \\theta)$$</div>
<div class="math-display$$(P_\\gamma - P_\\gamma') \\cdot P_e = \\left( \\frac{E - E'}{c} \\right)(m_e c) - 0 = m_e (E - E')$$</div>
Equating expressions:
<div class="math-display">$$\\frac{E E'}{c^2}(1 - \\cos \\theta) = m_e (E - E')$$</div>
Dividing by $E E' m_e c$:
<div class="math-display">$$\\frac{1}{E'} - \\frac{1}{E} = \\frac{1}{m_e c^2}(1 - \\cos \\theta)$$</div>
Using $E = hc/\\lambda$ and $E' = hc/\\lambda'$ yields the <strong>Compton Scattering Formula</strong>:
<div class="math-display">$$\\lambda' - \\lambda = \\frac{h}{m_e c}(1 - \\cos \\theta) = \\lambda_C (1 - \\cos \\theta)$$</div>
where $\\lambda_C = \\frac{h}{m_e c} \\approx 2.426 \\times 10^{-12}\\text{ m} = 0.002426\\text{ nm}$ is the Compton wavelength of the electron.
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-8-1",
            "title": "Threshold Kinetic Energy for Antiproton Creation via p + p Collision",
            "statement": "Calculate the minimum threshold kinetic energy $K_{\\text{th}}$ in the laboratory frame required for an incident proton of rest mass $m_p$ colliding with a target proton at rest to produce a proton-antiproton pair: $p + p \\to p + p + p + \\bar{p}$.",
            "steps": [
                {
                    "step": "Step 1: Set Up Initial Four-Momentum in Laboratory Frame",
                    "math": "$$P_{\\text{tot}}^{\\text{lab}} = P_1 + P_2 = \\left( \\frac{E_1 + m_p c^2}{c}, \\vec{p}_1 \\right)$$",
                    "explanation": "Target proton 2 is at rest, so $P_2 = (m_p c, \\vec{0})$. The incident proton 1 has total energy $E_1 = K_{\\text{th}} + m_p c^2$."
                },
                {
                    "step": "Step 2: Evaluate Invariant Mass Squared s = P_tot^μ P_tot,μ",
                    "math": "$$s = (P_1 + P_2)^2 = P_1^2 + P_2^2 + 2 P_1 \\cdot P_2 = m_p^2 c^2 + m_p^2 c^2 + 2 \\left( \\frac{E_1}{c}(m_p c) - 0 \\right) = 2 m_p^2 c^2 + 2 m_p E_1$$",
                    "explanation": "Because $s$ is a Lorentz scalar, its value in the laboratory frame must equal its value in the center-of-mass (CM) frame."
                },
                {
                    "step": "Step 3: Evaluate s at Threshold in Center-of-Mass Frame",
                    "math": "$$s = \\left(\\sum_{i=1}^4 m_i c\\right)^2 = (4 m_p c)^2 = 16 m_p^2 c^2$$",
                    "explanation": "At threshold, all four final particles ($3p + 1\\bar{p}$) are produced at rest in the CM frame with zero residual kinetic energy."
                },
                {
                    "step": "Step 4: Equate Invariant Masses and Solve for Threshold Energy",
                    "math": "$$2 m_p^2 c^2 + 2 m_p E_1 = 16 m_p^2 c^2 \\implies 2 m_p E_1 = 14 m_p^2 c^2 \\implies E_1 = 7 m_p c^2$$",
                    "explanation": "The threshold kinetic energy is $K_{\\text{th}} = E_1 - m_p c^2 = 7 m_p c^2 - m_p c^2 = 6 m_p c^2$. Since $m_p c^2 \\approx 938.3\\text{ MeV}$, $K_{\\text{th}} = 6 \\times 938.3 = 5.63\\text{ GeV}$."
                }
            ],
            "answer": "Threshold incident kinetic energy: K_th = 6 m_p c² ≈ 5.63 GeV (6 times the rest mass energy of a proton)."
        },
        {
            "id": "cm-prob-8-2",
            "title": "Invariant Mass and Velocity of a Decaying Neutral Pion",
            "statement": "A neutral pion $\\pi^0$ of rest mass $m_\\pi = 135.0\\text{ MeV}/c^2$ decays in flight into two high-energy photons: $\\pi^0 \\to \\gamma_1 + \\gamma_2$. In the laboratory frame, the two photons have energies $E_1 = 100.0\\text{ MeV}$ and $E_2 = 60.0\\text{ MeV}$. (a) Find the opening angle $\\theta$ between the two photons. (b) Find the velocity $v/c$ of the parent pion.",
            "steps": [
                {
                    "step": "Step 1: Apply Four-Momentum Conservation P_π = P_γ1 + P_γ2",
                    "math": "$$P_\\pi^2 = (P_{\\gamma 1} + P_{\\gamma 2})^2 = P_{\\gamma 1}^2 + P_{\\gamma 2}^2 + 2 P_{\\gamma 1} \\cdot P_{\\gamma 2}$$",
                    "explanation": "Since $P_\\pi^2 = m_\\pi^2 c^2$ and photons are massless ($P_\\gamma^2 = 0$), $m_\\pi^2 c^2 = 2 P_{\\gamma 1} \\cdot P_{\\gamma 2}$."
                },
                {
                    "step": "Step 2: Expand Photon Four-Vector Dot Product",
                    "math": "$$2 P_{\\gamma 1} \\cdot P_{\\gamma 2} = 2 \\left( \\frac{E_1 E_2}{c^2} - \\vec{p}_1 \\cdot \\vec{p}_2 \\right) = \\frac{2 E_1 E_2}{c^2}(1 - \\cos \\theta) = m_\\pi^2 c^2$$",
                    "explanation": "Solving for $\\cos \\theta$: $1 - \\cos \\theta = \\frac{m_\\pi^2 c^4}{2 E_1 E_2} = \\frac{(135.0)^2}{2(100.0)(60.0)} = \\frac{18225}{12000} = 1.51875$. Notice that for physical decay, $\\cos\\theta = 1 - 1.51875 = -0.51875$, so $\\theta = \\arccos(-0.51875) \\approx 121.25^\\circ$."
                },
                {
                    "step": "Step 3: Determine Pion Total Energy and Velocity",
                    "math": "$$E_\\pi = E_1 + E_2 = 160.0\\text{ MeV}, \\quad \\gamma = \\frac{E_\\pi}{m_\\pi c^2} = \\frac{160.0}{135.0} \\approx 1.1852$$",
                    "explanation": "The velocity is $\\beta = \\frac{v}{c} = \\sqrt{1 - 1/\\gamma^2} = \\sqrt{1 - (135/160)^2} = \\sqrt{1 - 0.7119} = \\sqrt{0.2881} \\approx 0.5367$."
                }
            ],
            "answer": "(a) Opening angle between photons: θ ≈ 121.3°; (b) Parent pion velocity: v/c ≈ 0.537 (53.7% light speed)."
        },
        {
            "id": "cm-prob-8-3",
            "title": "Relativistic Rocket Motion: The Relativistic Tsiolkovsky Equation",
            "statement": "A relativistic rocket accelerates from rest in interstellar space by expelling propellant exhaust gas at constant speed $u_{\\text{ex}}$ relative to the rocket nozzle. Derive the relativistic generalization of Tsiolkovsky's rocket equation relating final velocity $v$ to the mass ratio $M_0 / M_f$.",
            "steps": [
                {
                    "step": "Step 1: Balance Momentum in the Instantaneous Rest Frame of the Rocket",
                    "math": "$$M dv' + u_{\\text{ex}} dM = 0 \\implies dv' = -u_{\\text{ex}} \\frac{dM}{M}$$",
                    "explanation": "In the rocket's instantaneous comoving frame, the change in rocket velocity is $dv'$ and exhaust mass expelled is $-dM$."
                },
                {
                    "step": "Step 2: Relate Comoving dv' to Lab Frame dv via Velocity Addition",
                    "math": "$$v + dv = \\frac{v + dv'}{1 + v dv'/c^2} \\approx (v + dv')(1 - v dv'/c^2) \\implies dv = dv' (1 - v^2/c^2) = \\frac{dv'}{\\gamma^2}$$",
                    "explanation": "Inverting gives $dv' = \\frac{dv}{1 - v^2/c^2}$."
                },
                {
                    "step": "Step 3: Integrate Differential Equation",
                    "math": "$$\\int_0^v \\frac{dv}{1 - v^2/c^2} = -u_{\\text{ex}} \\int_{M_0}^{M_f} \\frac{dM}{M} \\implies \\frac{c}{2} \\ln\\left( \\frac{1 + v/c}{1 - v/c} \\right) = u_{\\text{ex}} \\ln\\left( \\frac{M_0}{M_f} \\right)$$",
                    "explanation": "Exponentiating: $\\frac{1 + v/c}{1 - v/c} = \\left( \\frac{M_0}{M_f} \\right)^{2 u_{\\text{ex}} / c}$. Solving for $v/c$ delivers the relativistic rocket velocity."
                }
            ],
            "answer": "Relativistic rocket velocity: v/c = [(M0/Mf)^(2 u_ex/c) - 1] / [(M0/Mf)^(2 u_ex/c) + 1]. In the photon rocket limit (u_ex = c), v/c = [(M0/Mf)² - 1] / [(M0/Mf)² + 1]."
        }
    ]
}

with open("cm_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7, f, indent=2)

with open("cm_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8, f, indent=2)

print("cm_u7.json and cm_u8.json generated successfully!")
