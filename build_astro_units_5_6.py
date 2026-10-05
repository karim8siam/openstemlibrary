import json
import os

u5 = {
    "unitId": 5,
    "title": "The Milky Way, Galactic Dynamics & Spiral Structure",
    "subtitle": "Oort Kinematics, Flat Rotation Curves, Dark Matter Halos & Lin-Shu Density Waves",
    "icon": "🌌",
    "summary": "This unit explores the architecture, kinematics, and dynamical evolution of our home galaxy, the Milky Way. We analyze its structural decomposition into thin disk, thick disk, central bulge, stellar halo, and the supermassive black hole Sagittarius A*. We formulate galactic coordinate transformations and utilize the 21-cm neutral hydrogen hyperfine line to map galactic structure through interstellar dust extinction. We derive the Oort constants of differential rotation and epicyclic stellar orbital dynamics. We demonstrate how the flat galactic rotation curve necessitates a dominant, non-baryonic dark matter halo. We resolve the classical 'winding dilemma' of spiral arms through the Lin-Shu quasi-stationary density wave theory, and analyze cosmic ray Fermi shock acceleration in galactic magnetic fields.",
    "keyTakeaways": [
        "The Milky Way is a barred spiral galaxy of type SBbc whose components (thin disk, thick disk, bulge, dark matter halo) possess distinct stellar populations, scale heights, kinematics, and metallicity distributions.",
        "Radio observations of the $21.1\\text{ cm}$ ($1420.4\\text{ MHz}$) spin-flip transition of neutral hydrogen penetrate interstellar dust extinction, enabling radar-like Doppler mapping of spiral arm gas throughout the Galactic plane.",
        "Differential galactic rotation near the Sun is quantified by the Oort constants $A = +15.3\\text{ km s}^{-1}\\text{kpc}^{-1}$ and $B = -11.9\\text{ km s}^{-1}\\text{kpc}^{-1}$, yielding the local angular rotation speed $\\Omega_0 = A - B$ and circular speed $V_0 = R_0(A - B) \\approx 220\\text{ km s}^{-1}$.",
        "The observed persistence of flat circular rotation curves ($V(R) \\approx \\text{const}$) beyond the optical disk directly contradicts Keplerian decline ($V \\propto R^{-1/2}$), proving the existence of an extended spherical dark matter halo whose enclosed mass grows linearly with radius ($M(R) \\propto R$).",
        "Spiral arms are not material structures but rather self-sustaining density waves governed by the Lin-Shu dispersion relation, wherein interstellar gas clouds decelerate into gravitational potential troughs, shocking and igniting prolific star formation along trailing spiral arms."
    ],
    "sections": [
        {
            "id": "sec-5-1",
            "title": "Morphology & Structural Architecture of the Milky Way",
            "content": """
<p>The Milky Way is a barred spiral galaxy classified as <strong>SBbc</strong> in the Hubble-de Vaucouleurs sequence. It contains approximately $(1-4) \\times 10^{11}$ stars and spans an optical diameter of roughly $30\\text{ kpc}$.</p>

<h4>Structural Components of the Galaxy</h4>
<table class="data-table">
  <thead>
    <tr><th>Component</th><th>Mass ($M_\\odot$)</th><th>Scale Height / Radius</th><th>Stellar Population & Kinematics</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Thin Disk</strong></td><td>$\\approx 5 \\times 10^{10}$</td><td>Scale height $z_d \\approx 300\\text{ pc}$, radial scale length $R_d \\approx 2.6\\text{ kpc}$</td><td>Population I stars; young open clusters, dust lanes, ongoing star formation; high metallicity ($[\\text{Fe}/\\text{H}] \\sim 0$), cold circular orbits with low velocity dispersion ($\\sigma_z \\sim 15\\text{ km/s}$)</td></tr>
    <tr><td><strong>Thick Disk</strong></td><td>$\\approx 5 \\times 10^9$</td><td>Scale height $z_d \\approx 1000\\text{ pc}$</td><td>Intermediate Population II; older stars ($> 8\\text{ Gyr}$), lower metallicity ($[\\text{Fe}/\\text{H}] \\sim -0.5$), warmer kinematics ($\\sigma_z \\sim 40\\text{ km/s}$)</td></tr>
    <tr><td><strong>Central Bulge & Bar</strong></td><td>$\\approx 1.5 \\times 10^{10}$</td><td>Major axis length $\\approx 3.5\\text{ kpc}$, tilted $\\approx 27^\\circ$ to Sun-Center axis</td><td>Old Population II stars; boxy/peanut-shaped triaxial rotating bar; high stellar densities</td></tr>
    <tr><td><strong>Stellar Halo</strong></td><td>$\\approx 10^9$</td><td>Spherical radius $R \\sim 30-50\\text{ kpc}$</td><td>Extreme Population II; globular clusters, halo field stars; very low metallicity ($[\\text{Fe}/\\text{H}] < -1.5$), highly eccentric, random non-circular orbits</td></tr>
    <tr><td><strong>Dark Matter Halo</strong></td><td>$\\approx 1.0 - 1.5 \\times 10^{12}$</td><td>Virial radius $R_{\\text{vir}} \\approx 200-250\\text{ kpc}$</td><td>Non-baryonic collisionless dark matter; spheroidal distribution dominating total mass by $> 90\\%$</td></tr>
  </tbody>
</table>

<h4>Sagittarius A*: The Central Supermassive Black Hole</h4>
<p>At the dynamic center of the Milky Way lies <strong>Sagittarius A*</strong> (Sgr A*). Infrared speckle and adaptive optics observations (Ghez, Genzel, Nobel Prize 2020) tracked the Keplerian orbital trajectories of individual stars ('S-stars') over decades. Star <strong>S2</strong> completes an elliptical orbit ($e = 0.884$) with period $P = 16.05\\text{ years}$, approaching within $r_{\\text{peri}} = 120\\text{ AU} \\approx 1400 R_s$ of Sgr A* at speeds exceeding $7700\\text{ km s}^{-1}$ ($2.6\\% c$). Applying Kepler's Third Law proves that a mass of:</p>
<div class="equation-box">
$$M_{\\text{BH}} = (4.15 \\pm 0.03) \\times 10^6 M_\\odot$$
</div>
<p>is packed inside a volume smaller than the orbit of Mercury, definitively proving the existence of a central supermassive black hole, as confirmed directly by the Event Horizon Telescope (EHT) shadow image in 2022.</p>
"""
        },
        {
            "id": "sec-5-2",
            "title": "Galactic Coordinates, Dust Extinction & The 21-cm Hyperfine Line",
            "content": """
<p>To analyze structures within our own galaxy from our internal vantage point, the IAU established the Galactic Coordinate System.</p>

<h4>Galactic Coordinates: Longitude ($l$) and Latitude ($b$)</h4>
<ul>
  <li><strong>Galactic Center:</strong> Defined as $(l = 0^\\circ, b = 0^\\circ)$, located in the constellation Sagittarius at Right Ascension $\\alpha = 17^\\text{h} 45^\\text{m} 40^\\text{s}$, Declination $\\delta = -29^\\circ 00' 28''$ (J2000).</li>
  <li><strong>Galactic Longitude ($l$):</strong> Measured eastward along the Galactic plane from the Galactic Center ($0^\\circ \\le l < 360^\\circ$). $l = 90^\\circ$ points in the direction of Galactic rotation (Cygnus), $l = 180^\\circ$ is the Galactic Anticenter (Auriga), and $l = 270^\\circ$ is Vela.</li>
  <li><strong>Galactic Latitude ($b$):</strong> Measured perpendicular to the Galactic plane ($-90^\\circ \\le b \\le +90^\\circ$), with the North Galactic Pole (NGP) at $(b = +90^\\circ)$ in Coma Berenices.</li>
</ul>

<h4>Interstellar Dust Extinction & Reddening</h4>
<p>Microscopic interstellar dust grains ($a \\sim 0.01 - 0.2\\ \\mu\\text{m}$, composed of silicates, graphite, and polycyclic aromatic hydrocarbons) absorb and scatter optical light. The scattering cross-section obeys a power law $\\sigma_{\\text{scat}} \\propto \\lambda^{-1}$ (Mie scattering regime). Consequently, blue light is scattered far more than red light, causing <strong>interstellar reddening</strong>.</p>
<p>Extinction along the line of sight reduces apparent stellar flux according to Beer's law: $F = F_0 e^{-\\tau_\\lambda} = F_0 10^{-0.4 A_\\lambda}$. In the Galactic disk plane ($b \\approx 0^\\circ$), average visual extinction is:</p>
<div class="equation-box">
$$A_V \\approx 1.8\\text{ magnitudes per kiloparsec}$$
</div>
<p>Toward the Galactic Center ($d \\approx 8.2\\text{ kpc}$), total visual extinction is $A_V \\approx 30\\text{ magnitudes}$! This attenuates optical light by a factor of $10^{-0.4 \\times 30} = 10^{-12}$ (one-trillionth), completely blinding optical telescopes to the inner galaxy and creating the 'Zone of Avoidance'.</p>

<h4>The 21-cm Hyperfine Neutral Hydrogen (H I) Line</h4>
<p>In 1944, Hendrik van de Hulst realized that neutral atomic hydrogen (H I) can be observed at radio wavelengths. Neutral hydrogen consists of one proton and one electron. In the ground state ($1s$), the nuclear magnetic dipole moment of the proton and the spin magnetic dipole moment of the electron can be aligned (parallel, higher energy) or anti-aligned (antiparallel, lower energy).</p>
<p>The quantum mechanical spin-flip transition releases an energy of $\\Delta E = 5.874 \\times 10^{-6}\\text{ eV}$, corresponding to a photon wavelength and frequency of:</p>
<div class="equation-box">
$$\\lambda_{21} = \\frac{h c}{\\Delta E} = 21.106\\text{ cm}, \\quad \\nu_{21} = 1420.40575\\text{ MHz}$$
</div>
<p>The transition is forbidden by electric dipole selection rules, proceeding via magnetic dipole transition with an Einstein $A$ coefficient of $A_{10} = 2.87 \\times 10^{-15}\\text{ s}^{-1}$ (spontaneous radiative lifetime $\\tau = 1/A_{10} \\approx 11\\text{ million years}$).</p>
<p>However, because interstellar hydrogen is vastly abundant, collisions easily maintain the population. Most importantly, at $\\lambda = 21\\text{ cm}$, interstellar dust extinction is utterly negligible ($A_{21} \\approx 10^{-4} A_V$). 21-cm radio telescopes peer directly through the entire Galactic disk, measuring Doppler velocity profiles that reveal the spiral arms of our galaxy.</p>
"""
        },
        {
            "id": "sec-5-3",
            "title": "Galactic Kinematics, Oort Constants & Epicyclic Dynamics",
            "content": """
<p>Stars in the disk of the Milky Way do not rotate as a rigid body. Instead, they exhibit <strong>differential galactic rotation</strong>, orbiting the center with an angular velocity $\\Omega(R)$ that depends on galactocentric radius $R$.</p>

<h4>Derivation of Oort's Formulae</h4>
<p>Consider the Sun at galactocentric radius $R_0 \\approx 8.2\\text{ kpc}$ moving in a circular orbit with speed $V_0 = \\Omega_0 R_0 \\approx 220\\text{ km s}^{-1}$. A star located at distance $d \\ll R_0$ and Galactic longitude $l$ moves at radius $R$ with circular speed $V = \\Omega R$.</p>
<p>The observed radial velocity $v_r$ and transverse velocity $v_t$ of the star relative to the Local Standard of Rest (LSR) are:</p>
<div class="equation-box">
$$v_r = V \\cos\\alpha - V_0 \\sin l = R \\Omega \\cos\\alpha - R_0 \\Omega_0 \\sin l$$
$$v_t = V \\sin\\alpha - V_0 \\cos l = R \\Omega \\sin\\alpha - R_0 \\Omega_0 \\cos l$$
</div>
<p>Using the sine and cosine laws for the triangle formed by the Galactic Center, Sun, and Star: $R \\sin\\alpha = R_0 \\cos l - d$ and $R \\cos\\alpha = R_0 \\sin l$:</p>
<div class="equation-box">
$$v_r = (\\Omega - \\Omega_0) R_0 \\sin l$$
$$v_t = (\\Omega - \\Omega_0) R_0 \\cos l - \\Omega d$$
</div>
<p>Expanding $\\Omega(R)$ in a Taylor series around $R = R_0$ for small distances ($d \\ll R_0$), where $R - R_0 \\approx -d \\cos l$:</p>
<div class="equation-box">
$$\\Omega - \\Omega_0 \\approx \\left(\\frac{d\\Omega}{dR}\\right)_{R_0} (R - R_0) \\approx -\\left(\\frac{d\\Omega}{dR}\\right)_{R_0} d \\cos l$$
</div>
<p>Substituting into the velocity equations yields <strong>Oort's Kinematic Equations</strong>:</p>
<div class="equation-box">
$$v_r = A d \\sin(2l)$$
$$v_t = d [A \\cos(2l) + B]$$
</div>
<p>where the <strong>Oort Constants</strong> $A$ and $B$ are defined as:</p>
<div class="equation-box">
$$A \\equiv -\\frac{1}{2} R_0 \\left(\\frac{d\\Omega}{dR}\\right)_{R_0} = \\frac{1}{2}\\left(\\frac{V_0}{R_0} - \\left.\\frac{dV}{dR}\\right|_{R_0}\\right) \\quad (\\text{Measures local shear})$$
$$B \\equiv -\\frac{1}{2} R_0 \\left(\\frac{d\\Omega}{dR}\\right)_{R_0} - \\Omega_0 = -\\frac{1}{2}\\left(\\frac{V_0}{R_0} + \\left.\\frac{dV}{dR}\\right|_{R_0}\\right) \\quad (\\text{Measures local vorticity})$$
</div>
<p>Direct subtraction and addition yield fundamental kinematic quantities:</p>
<div class="equation-box">
$$A - B = \\frac{V_0}{R_0} = \\Omega_0 \\quad (\\text{Solar Angular Velocity})$$
$$A + B = -\\left.\\frac{dV}{dR}\\right|_{R_0} \\quad (\\text{Rotation Curve Slope})$$
</div>
<p>Modern astrometric determinations (Gaia DR3) yield:</p>
<div class="equation-box">
$$A \\approx +15.3 \\pm 0.4\\text{ km s}^{-1}\\text{kpc}^{-1}, \\quad B \\approx -11.9 \\pm 0.4\\text{ km s}^{-1}\\text{kpc}^{-1}$$
$$\\Omega_0 = A - B \\approx 27.2\\text{ km s}^{-1}\\text{kpc}^{-1} \\implies P_0 = \\frac{2\\pi}{\\Omega_0} \\approx 226\\text{ million years (1 Galactic Cosmic Year)}$$
$$V_0 = \\Omega_0 R_0 \\approx 27.2 \\times 8.2 \\approx 223\\text{ km s}^{-1}$$
</div>

<h4>Epicyclic Approximation of Stellar Orbits</h4>
<p>Real stellar orbits in the disk are not perfectly circular. In Lindblad's epicyclic approximation, a star executes a small elliptical retrograde oscillation (an <strong>epicycle</strong>) centered on a guiding center that orbits circularly at radius $R_0$. The radial oscillation frequency is the <strong>epicyclic frequency ($\\kappa$)</strong>:</p>
<div class="equation-box">
$$\\kappa^2(R) = 4 \\Omega^2 + 2 R \\Omega \\frac{d\\Omega}{dR} = 4 \\Omega(R) \\left[\\Omega(R) + \\frac{R}{2}\\frac{d\\Omega}{dR}\\right] = -4 B (A - B)$$
</div>
<p>In the solar neighborhood, $\\kappa_0 = \\sqrt{-4 (-11.9)(27.2)} = \\sqrt{1294.7} \\approx 36.0\\text{ km s}^{-1}\\text{kpc}^{-1}$. The radial oscillation period is $P_\\kappa = 2\\pi / \\kappa_0 \\approx 171\\text{ Myr}$. Because $\\kappa_0 \\ne \\Omega_0$, stellar orbits do not close, tracing rosettes in the Galactic plane.</p>
"""
        },
        {
            "id": "sec-5-4",
            "title": "Galactic Rotation Curves & The Dark Matter Halo",
            "content": """
<p>Newtonian mechanics predicts how orbital speeds must behave in any self-gravitating disk system. Measuring the actual circular velocity profile $V(R)$ of the Milky Way and external spiral galaxies provides the most decisive empirical evidence for the existence of non-baryonic dark matter.</p>

<h4>The Keplerian Prediction vs The Observation</h4>
<p>Consider a galaxy whose mass is entirely luminous (baryonic stars and gas concentrated in a central bulge and exponential disk with scale length $R_d \\sim 3\\text{ kpc}$). At radii well beyond the visible disk ($R \\gg R_d$), the enclosed mass is constant: $M(R) \\to M_{\\text{lum}} = \\text{const}$. Balancing gravitational attraction and centripetal acceleration:</p>
<div class="equation-box">
$$\\frac{G M(R)}{R^2} = \\frac{V^2}{R} \\implies V(R) = \\sqrt{\\frac{G M(R)}{R}} \\propto R^{-1/2}$$
</div>
<p>Just as the orbital speeds of planets in the Solar System fall off as $V \\propto r^{-1/2}$ according to Kepler's Third Law, astronomers expected galactic rotation speeds to decline sharply beyond the optical edge ($R \\sim 15\\text{ kpc}$).</p>
<p>In the 1970s, Vera Rubin and Kent Ford (optical spectroscopy of H II regions) alongside Morton Roberts and Albert Bosma (21-cm radio observations of H I gas) measured rotation curves out to several times the visible optical radius. Shockingly, they discovered that:</p>
<div class="equation-box">
$$V(R) \\approx \\text{constant} \\approx 220\\text{ km s}^{-1} \\quad \\text{out to } R > 50-100\\text{ kpc}!$$
</div>
<p>The rotation curve does <em>not</em> decline!</p>

<h4>Inferring the Dark Matter Halo Density Profile</h4>
<p>If $V(R) = V_0 = \\text{constant}$, the enclosed mass must grow linearly with radius:</p>
<div class="equation-box">
$$M(R) = \\frac{V_0^2 R}{G} \\propto R$$
</div>
<p>Since the enclosed mass is $M(R) = \\int_0^R 4\\pi r^2 \\rho(r) dr$, differentiating with respect to $R$ yields:</p>
<div class="equation-box">
$$\\frac{dM}{dR} = 4\\pi R^2 \\rho(R) = \\frac{V_0^2}{G} \\implies \\rho(R) = \\frac{V_0^2}{4\\pi G R^2} \\propto R^{-2}$$
</div>
<p>This $R^{-2}$ density profile corresponds to an <strong>isothermal sphere</strong>. Because the visible stars and gas drop off exponentially ($\\rho_{\\text{lum}} \\propto e^{-R/R_d}$), the mass must be dominated by a vast, non-luminous, roughly spherical <strong>dark matter halo</strong>.</p>

<h4>Cosmological Halo Profiles: The NFW Model</h4>
<p>High-resolution cosmological $N$-body simulations of collisionless Cold Dark Matter (Navarro, Frenk, & White 1996) reveal a universal halo density profile:</p>
<div class="equation-box">
$$\\rho_{\\text{NFW}}(r) = \\frac{\\rho_0}{\\left(\\frac{r}{r_s}\\right) \\left(1 + \\frac{r}{r_s}\\right)^2}$$
</div>
<p>where $r_s$ is a characteristic scale radius. The profile exhibits a central cusp ($\\rho \\propto r^{-1}$ for $r \\ll r_s$), transitions to isothermal behavior ($\\rho \\propto r^{-2}$ near $r \\sim r_s$), and steepens to $\\rho \\propto r^{-3}$ at large distances ($r \\gg r_s$). The dark matter halo of the Milky Way extends out to $R_{\\text{vir}} \\approx 200\\text{ kpc}$, comprising $(1.0-1.5) \\times 10^{12} M_\\odot$—over $85-90\\%$ of the total mass of our galaxy!</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 5.1: Galactic Rotation Curve Decomposer & Dark Matter Halo</h4>
  </div>
  <p>Toggle and adjust the masses of the central bulge, exponential stellar disk, and dark matter halo to observe how the total circular velocity profile transitions from Keplerian decline to the empirically observed flat rotation curve.</p>
  <div id="astro-galaxy-rotation-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-5-5",
            "title": "Spiral Structure & The Lin-Shu Density Wave Theory",
            "content": """
<p>Spiral arms are the most visually stunning features of disk galaxies. However, explaining their persistent survival posed a fundamental theoretical crisis known as the <em>winding dilemma</em>.</p>

<h4>The Winding Dilemma</h4>
<p>If spiral arms were rigid, physical material structures composed of the same stars and gas over time, differential galactic rotation would destroy them. Because stars at smaller radii orbit faster than stars at larger radii ($d\\Omega/dR < 0$), an initially radial material arm would be wound into a tight spiral. The number of turns $n$ wound after time $t$ is:</p>
<div class="equation-box">
$$n(R) = \\frac{t}{2\\pi} [\\Omega(R) - \\Omega(R_0)]$$
</div>
<p>Over the $10\\text{ Gyr}$ lifetime of the Milky Way, differential rotation would wind the arms into more than 50 tightly wound turns, obliterating the open 2- and 4-arm patterns universally observed. Spiral arms cannot be material entities!</p>

<h4>The Lin-Shu Density Wave Theory</h4>
<p>In 1964, C.C. Lin and Frank Shu resolved the dilemma by proposing that spiral arms are <strong>quasi-stationary density waves</strong>—gravitational perturbation waves that propagate through the stellar and gaseous disk. The spiral pattern rotates as a rigid shape with a constant angular <strong>pattern speed $\\Omega_p$</strong>, while individual stars and gas clouds orbit at their local speeds $\\Omega(R)$, continually entering, passing through, and exiting the wave.</p>

<h4>Resonances in the Galactic Disk</h4>
<p>A star oscillating with epicyclic frequency $\\kappa(R)$ encounters a spiral pattern with $m$ arms at an apparent frequency $m(\\Omega - \\Omega_p)$. Resonances occur when this driving frequency matches the natural epicyclic frequency:</p>
<div class="equation-box">
$$m(\\Omega(R) - \\Omega_p) = \\pm \\kappa(R) \\implies \\Omega_p = \\Omega(R) \\pm \\frac{\\kappa(R)}{m}$$
</div>
<ul>
  <li><strong>Corotation Resonance (CR):</strong> Where the stars rotate at exactly the same speed as the spiral pattern: $\\Omega(R_{\\text{CR}}) = \\Omega_p$. Inside corotation ($R < R_{\\text{CR}}$), stars overtake the spiral wave. Outside corotation ($R > R_{\\text{CR}}$), the pattern sweeps past slower-moving stars.</li>
  <li><strong>Inner Lindblad Resonance (ILR):</strong> $\\Omega_p = \\Omega(R) - \\frac{\\kappa(R)}{m}$. Stars complete two epicycles per encounter with a 2-arm ($m=2$) pattern.</li>
  <li><strong>Outer Lindblad Resonance (OLR):</strong> $\\Omega_p = \\Omega(R) + \\frac{\\kappa(R)}{m}$.</li>
</ul>
<p>Self-consistent spiral patterns can only survive between the ILR and OLR.</p>

<h4>Star Formation in Spiral Arms</h4>
<p>As cold interstellar gas clouds orbit supersonic relative to the pattern ($v_{\\perp} = [\\Omega(R) - \\Omega_p] R \\sin i > c_s$), they slam into the gravitational potential minimum of the density wave. The sudden deceleration produces a sharp hydrodynamic <strong>galactic shock wave</strong>. The gas is compressed by factors of $5-10$, driving the local density above the Jeans threshold ($M > M_J$) and triggering the birth of massive, short-lived O and B stars. Because OB stars live only $\\sim 10-30\\text{ Myr}$, they die near their birth sites, lighting up the trailing edges of the density wave with glowing blue star clusters and pink H II emission nebulae.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 5.2: Lin-Shu Spiral Density Wave & Resonance Ring Animator</h4>
  </div>
  <p>Vary the pattern speed $\\Omega_p$ and arm count $m$ to observe nested stellar epicyclic orbits aligning to create quasi-stationary spiral density waves, showing inner Lindblad, corotation, and outer Lindblad resonances.</p>
  <div id="astro-density-wave-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-5-6",
            "title": "Cosmic Rays, Fermi Shock Acceleration & Galactic Magnetic Fields",
            "content": """
<p>The interstellar medium is permeated by relativistic charged particles known as <strong>cosmic rays</strong> and a pervasive, coherent galactic magnetic field.</p>

<h4>Composition & Energy Spectrum of Cosmic Rays</h4>
<p>Cosmic rays consist of relativistic atomic nuclei ($89\\%$ protons, $10\\%$ alpha particles, $1\\%$ heavier elements up to uranium) and relativistic electrons ($1\\%$). Their energy spectrum spans an immense range from $10^9\\text{ eV}$ ($1\\text{ GeV}$) to $> 10^{20}\\text{ eV}$ ($100\\text{ EeV}$), governed by a broken power law:</p>
<div class="equation-box">
$$\\frac{dN}{dE} \\propto E^{-s}$$
</div>
<ul>
  <li>For $10^9\\text{ eV} < E < 3 \\times 10^{15}\\text{ eV}$, $s \\approx 2.7$.</li>
  <li>At the <strong>'Knee'</strong> ($E \\approx 3 \\times 10^{15}\\text{ eV} = 3\\text{ PeV}$), the spectrum steepens to $s \\approx 3.1$, marking the maximum confinement and acceleration energy of Galactic supernova remnants.</li>
  <li>At the <strong>'Ankle'</strong> ($E \\approx 3 \\times 10^{18}\\text{ eV} = 3\\text{ EeV}$), the spectrum flattens back to $s \\approx 2.6$, signaling a transition to Ultra-High Energy Cosmic Rays (UHECRs) of extragalactic origin.</li>
</ul>

<h4>Diffusive Shock Acceleration: The First-Order Fermi Mechanism</h4>
<p>Enrico Fermi (1949, 1954) proposed that cosmic rays gain energy by scattering off magnetized plasma clouds. In a supernova blast wave expanding into the ISM at shock velocity $v_s$, particles scatter elastically off magnetic turbulence on both sides of the shock front. Because the downstream gas moves toward the upstream gas at relative speed $u = \\frac{3}{4} v_s$, every round-trip crossing across the shock is a head-on collision. The fractional energy gain per cycle is:</p>
<div class="equation-box">
$$\\frac{\\Delta E}{E} = \\frac{4}{3} \\frac{u}{c} = \\frac{v_s}{c} \\quad (\\text{First-Order Fermi Acceleration})$$
</div>
<p>Because the energy gain is linear in $v_s/c$ (first-order) and particles have a finite escape probability $P_{\\text{esc}}$ per crossing, repeated shock cycling naturally produces an exact power-law distribution $dN/dE \\propto E^{-2}$, which steepens to $E^{-2.7}$ as cosmic rays diffuse out of the Galactic magnetic trap.</p>

<h4>Galactic Magnetic Fields & Synchrotron Radiation</h4>
<p>The Milky Way hosts a large-scale magnetic field of strength $B \\approx 3-6\\ \\mu\\text{G}$ ($0.3-0.6\\text{ nT}$), ordered along the spiral arms. Relativistic electrons gyrating around magnetic field lines with Lorentz factor $\\gamma = E/(m_e c^2)$ emit beamed <strong>synchrotron radiation</strong> at critical frequency:</p>
<div class="equation-box">
$$\\nu_c = \\frac{3}{4\\pi} \\gamma^2 \\frac{e B_\\perp}{m_e c}$$
</div>
<p>A power-law electron distribution $N(E) \\propto E^{-p}$ produces a synchrotron radio spectrum with flux $S_\\nu \\propto \\nu^{-\\alpha}$, where the spectral index is $\\alpha = (p - 1)/2 \\approx 0.7-0.8$, illuminating the Milky Way at radio frequencies.</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-5-1",
            "title": "Oort Constants, Solar Galactocentric Orbit & Local Shear",
            "statement": "Precision astrometric observations of disk stars yield Oort constants $A = +15.3\\text{ km s}^{-1}\\text{kpc}^{-1}$ and $B = -11.9\\text{ km s}^{-1}\\text{kpc}^{-1}$, with the Sun located at galactocentric radius $R_0 = 8.20\\text{ kpc}$.\\n\\n(a) Compute the angular velocity of the Local Standard of Rest $\\Omega_0$ in $\\text{km s}^{-1}\\text{kpc}^{-1}$ and $\\text{rad s}^{-1}$.\\n(b) Calculate the circular orbital speed of the Sun $V_0$ in $\\text{km s}^{-1}$ and the Galactic orbital period $P_0$ in millions of years.\\n(c) Determine the slope of the rotation curve $\\frac{dV}{dR}\\Big|_{R_0}$ at the solar radius and comment on its physical implication.\\n(d) Calculate the local epicyclic frequency $\\kappa_0$ and the radial oscillation period $P_\\kappa$.",
            "solution": """
<h4>(a) Angular Velocity of the LSR</h4>
<p>The angular velocity is given by $\\Omega_0 = A - B$:</p>
<div class="equation-box">
$$\\Omega_0 = 15.3 - (-11.9) = 15.3 + 11.9 = 27.2\\text{ km s}^{-1}\\text{kpc}^{-1}$$
</div>
<p>Converting to $\\text{rad s}^{-1}$ ($1\\text{ kpc} = 3.0857 \\times 10^{16}\\text{ km}$):</p>
<div class="equation-box">
$$\\Omega_0 = \\frac{27.2\\text{ km/s}}{3.0857 \\times 10^{19}\\text{ km}} \\approx 8.815 \\times 10^{-19}\\text{ rad s}^{-1}$$
</div>

<h4>(b) Circular Orbital Speed & Galactic Year</h4>
<p>With $R_0 = 8.20\\text{ kpc}$:</p>
<div class="equation-box">
$$V_0 = \\Omega_0 R_0 = (27.2\\text{ km s}^{-1}\\text{kpc}^{-1})(8.20\\text{ kpc}) \\approx 223.04\\text{ km s}^{-1}$$
</div>
<p>The Galactic orbital period (Galactic Year) is:</p>
<div class="equation-box">
$$P_0 = \\frac{2\\pi}{\\Omega_0} = \\frac{2\\pi R_0}{V_0} = \\frac{2\\pi \\times 8.20\\text{ kpc} \\times 3.0857 \\times 10^{16}\\text{ km/kpc}}{223.04\\text{ km/s}} = \\frac{1.5898 \\times 10^{18}\\text{ km}}{223.04\\text{ km/s}} \\approx 7.128 \\times 10^{15}\\text{ s}$$
$$P_0 = \\frac{7.128 \\times 10^{15}\\text{ s}}{3.15576 \\times 10^7\\text{ s/yr}} \\approx 2.259 \\times 10^8\\text{ years} \\approx 226\\text{ million years}$$
</div>
<p>Since the formation of the Solar System ($4.57\\text{ Gyr}$ ago), the Sun has completed $\\approx 20$ full revolutions around the Galactic Center.</p>

<h4>(c) Slope of the Local Rotation Curve</h4>
<p>From the definition of Oort constants:</p>
<div class="equation-box">
$$\\left.\\frac{dV}{dR}\\right|_{R_0} = -(A + B) = -[15.3 + (-11.9)] = -[15.3 - 11.9] = -3.4\\text{ km s}^{-1}\\text{kpc}^{-1}$$
</div>
<p>The local slope is nearly zero (flat), exhibiting a very slight gentle decline of only $3.4\\text{ km/s}$ per kiloparsec, completely incompatible with pure Keplerian falloff ($\\frac{dV}{dR} = -\\frac{V_0}{2 R_0} = -\\frac{223}{16.4} \\approx -13.6\\text{ km s}^{-1}\\text{kpc}^{-1}$).</p>

<h4>(d) Epicyclic Frequency & Radial Period</h4>
<p>The epicyclic frequency is:</p>
<div class="equation-box">
$$\\kappa_0 = \\sqrt{-4 B (A - B)} = \\sqrt{-4 (-11.9)(27.2)} = \\sqrt{1294.72} \\approx 35.98\\text{ km s}^{-1}\\text{kpc}^{-1}$$
</div>
<p>Converting to period:</p>
<div class="equation-box">
$$P_\\kappa = \\frac{2\\pi}{\\kappa_0} = \\frac{2\\pi}{35.98} \\times \\frac{3.0857 \\times 10^{19}\\text{ km}}{3.1558 \\times 10^7\\text{ s/yr} \\times 1\\text{ km/s}} \\approx 1.708 \\times 10^8\\text{ years} \\approx 171\\text{ million years}$$
</div>
<p>The radial epicyclic oscillation period ($171\\text{ Myr}$) is shorter than the azimuthal period ($226\\text{ Myr}$), producing an unclosed rosette orbit.</p>
"""
        },
        {
            "id": "prob-5-2",
            "title": "Decomposing the Galactic Rotation Curve & Enclosed Dark Matter Mass",
            "statement": "At a galactocentric distance $R = 25.0\\text{ kpc}$, the circular orbital velocity of the Milky Way is measured from neutral hydrogen clouds to be $V_{\\text{obs}} = 225.0\\text{ km s}^{-1}$. The total baryonic mass (stars in the bulge and disk, plus interstellar gas) enclosed within this radius is estimated to be $M_{\\text{baryon}}(25\\text{ kpc}) = 6.50 \\times 10^{10} M_\\odot$.\\n\\n(a) Compute the circular velocity $V_{\\text{baryon}}$ expected solely from the enclosed baryonic mass.\\n(b) Calculate the total dynamical mass $M_{\\text{total}}(25\\text{ kpc})$ required to produce the observed speed $V_{\\text{obs}}$.\\n(c) Determine the mass of the dark matter halo $M_{\\text{DM}}(25\\text{ kpc})$ enclosed within $25\\text{ kpc}$ and the ratio of dark matter to baryonic matter.\\n(d) Assuming a spherical isothermal dark matter halo profile $\\rho(r) = \\frac{\\sigma^2}{2\\pi G r^2}$, determine the 1D velocity dispersion $\\sigma$ of the dark matter particles.",
            "solution": """
<h4>(a) Circular Velocity from Baryons Alone</h4>
<p>With $M_{\\text{baryon}} = 6.50 \\times 10^{10} M_\\odot = 6.50 \\times 10^{10} \\times 1.989 \\times 10^{30}\\text{ kg} = 1.293 \\times 10^{41}\\text{ kg}$ and $R = 25.0\\text{ kpc} = 25.0 \\times 3.0857 \\times 10^{19}\\text{ m} = 7.714 \\times 10^{20}\\text{ m}$:</p>
<div class="equation-box">
$$V_{\\text{baryon}} = \\sqrt{\\frac{G M_{\\text{baryon}}}{R}} = \\sqrt{\\frac{(6.6743 \\times 10^{-11})(1.293 \\times 10^{41})}{7.714 \\times 10^{20}}} = \\sqrt{\\frac{8.630 \\times 10^{30}}{7.714 \\times 10^{20}}} = \\sqrt{1.1187 \\times 10^{10}} \\approx 105{,}770\\text{ m s}^{-1} \\approx 105.8\\text{ km s}^{-1}$$
</div>
<p>Baryons can account for less than half of the observed $225\\text{ km s}^{-1}$ velocity.</p>

<h4>(b) Total Dynamical Mass</h4>
<p>From the observed circular speed $V_{\\text{obs}} = 225\\text{ km s}^{-1} = 2.25 \\times 10^5\\text{ m s}^{-1}$:</p>
<div class="equation-box">
$$M_{\\text{total}} = \\frac{V_{\\text{obs}}^2 R}{G} = \\frac{(2.25 \\times 10^5)^2 (7.714 \\times 10^{20})}{6.6743 \\times 10^{-11}} = \\frac{(5.0625 \\times 10^{10})(7.714 \\times 10^{20})}{6.6743 \\times 10^{-11}} = \\frac{3.905 \\times 10^{31}}{6.6743 \\times 10^{-11}} \\approx 5.851 \\times 10^{41}\\text{ kg}$$
</div>
<p>In solar masses ($M_\\odot = 1.989 \\times 10^{30}\\text{ kg}$):</p>
<div class="equation-box">
$$M_{\\text{total}} = \\frac{5.851 \\times 10^{41}}{1.989 \\times 10^{30}} \\approx 2.942 \\times 10^{11} M_\\odot$$
</div>

<h4>(c) Enclosed Dark Matter Mass & Dark-to-Baryonic Ratio</h4>
<p>The dark matter mass is:</p>
<div class="equation-box">
$$M_{\\text{DM}} = M_{\\text{total}} - M_{\\text{baryon}} = 2.942 \\times 10^{11} M_\\odot - 0.650 \\times 10^{11} M_\\odot = 2.292 \\times 10^{11} M_\\odot$$
</div>
<p>The ratio of dark matter to baryonic matter within $25\\text{ kpc}$ is:</p>
<div class="equation-box">
$$\\frac{M_{\\text{DM}}}{M_{\\text{baryon}}} = \\frac{2.292 \\times 10^{11}}{0.650 \\times 10^{11}} \\approx 3.53$$
</div>
<p>Dark matter outweighs normal baryonic matter by over $3.5$ to $1$ within $25\\text{ kpc}$, rising to $> 10:1$ at the virial radius.</p>

<h4>(d) Velocity Dispersion of Dark Matter Particles</h4>
<p>For a singular isothermal sphere $\\rho(r) = \\frac{\\sigma^2}{2\\pi G r^2}$, the circular speed is $V_c = \\sqrt{2} \\sigma$:</p>
<div class="equation-box">
$$\\sigma = \\frac{V_c}{\\sqrt{2}} = \\frac{225.0\\text{ km s}^{-1}}{\\sqrt{2}} \\approx 159.1\\text{ km s}^{-1}$$
</div>
<p>The dark matter halo particles swarm with a characteristic 1D velocity dispersion of $\\approx 159\\text{ km s}^{-1}$.</p>
"""
        },
        {
            "id": "prob-5-3",
            "title": "Lin-Shu Density Wave Pattern Speed & Lindblad Resonances",
            "statement": "A spiral galaxy has an exactly flat rotation curve $V(R) = V_0 = 220.0\\text{ km s}^{-1}$ from $R = 2\\text{ kpc}$ out to $R = 30\\text{ kpc}$. It possesses a two-armed ($m = 2$) spiral density wave pattern with pattern speed $\\Omega_p = 20.0\\text{ km s}^{-1}\\text{kpc}^{-1}$.\\n\\n(a) Derive the epicyclic frequency $\\kappa(R)$ as a function of $R$ for an exactly flat rotation curve.\\n(b) Determine the radius of the Corotation Resonance $R_{\\text{CR}}$ in kiloparsecs.\\n(c) Calculate the radii of the Inner Lindblad Resonance (ILR) $R_{\\text{ILR}}$ and Outer Lindblad Resonance (OLR) $R_{\\text{OLR}}$.\\n(d) Where does the gas shock wave trigger star formation relative to the spiral arm?",
            "solution": """
<h4>(a) Epicyclic Frequency for Flat Rotation Curve</h4>
<p>With $V(R) = V_0 = \\text{const}$, the angular velocity is $\\Omega(R) = V_0 / R$. Differentiating gives $\\frac{d\\Omega}{dR} = -\\frac{V_0}{R^2} = -\\frac{\\Omega}{R}$.</p>
<p>The epicyclic frequency is:</p>
<div class="equation-box">
$$\\kappa^2(R) = 4\\Omega^2 + 2 R \\Omega \\left(-\\frac{\\Omega}{R}\\right) = 4\\Omega^2 - 2\\Omega^2 = 2\\Omega^2$$
$$\\kappa(R) = \\sqrt{2} \\Omega(R) = \\sqrt{2} \\frac{V_0}{R}$$
</div>

<h4>(b) Corotation Resonance Radius</h4>
<p>At corotation, the stellar angular speed equals the pattern speed: $\\Omega(R_{\\text{CR}}) = \\Omega_p$:</p>
<div class="equation-box">
$$\\frac{V_0}{R_{\\text{CR}}} = \\Omega_p \\implies R_{\\text{CR}} = \\frac{V_0}{\\Omega_p} = \\frac{220.0\\text{ km/s}}{20.0\\text{ km s}^{-1}\\text{kpc}^{-1}} = 11.0\\text{ kpc}$$
</div>

<h4>(c) Lindblad Resonance Radii</h4>
<p>For an $m = 2$ two-armed pattern, the resonance condition is $\\Omega_p = \\Omega(R) \\pm \\frac{\\kappa(R)}{2}$. Substituting $\\kappa(R) = \\sqrt{2}\\Omega(R)$:</p>
<div class="equation-box">
$$\\Omega_p = \\Omega(R) \\left[1 \\pm \\frac{\\sqrt{2}}{2}\\right] = \\frac{V_0}{R} \\left[1 \\pm \\frac{1}{\\sqrt{2}}\\right]$$
</div>
<ol>
  <li><strong>Inner Lindblad Resonance (ILR, minus sign):</strong>
  $$R_{\\text{ILR}} = \\frac{V_0}{\\Omega_p} \\left[1 - \\frac{1}{\\sqrt{2}}\\right] = 11.0\\text{ kpc} \\times (1 - 0.70711) = 11.0 \\times 0.29289 \\approx 3.22\\text{ kpc}$$
  </li>
  <li><strong>Outer Lindblad Resonance (OLR, plus sign):</strong>
  $$R_{\\text{OLR}} = \\frac{V_0}{\\Omega_p} \\left[1 + \\frac{1}{\\sqrt{2}}\\right] = 11.0\\text{ kpc} \\times (1 + 0.70711) = 11.0 \\times 1.70711 \\approx 18.78\\text{ kpc}$$
  </li>
</ol>
<p>The stable self-sustaining spiral structure exists between $R_{\\text{ILR}} \\approx 3.2\\text{ kpc}$ and $R_{\\text{OLR}} \\approx 18.8\\text{ kpc}$.</p>

<h4>(d) Shock Wave & Star Formation Geometry</h4>
<p>Inside the corotation radius ($R < 11.0\\text{ kpc}$, which includes the solar neighborhood at $8.2\\text{ kpc}$), stars and interstellar gas rotate faster than the spiral pattern ($\\Omega(R) > \\Omega_p$). Gas enters the spiral arm from the <em>inner concave</em> side at supersonic speeds, creating an oblique shock wave marked by a prominent dark dust lane. The compressed gas collapses into young star clusters that drift downstream, emerging along the outer convex bright rim as brilliant OB stars and pink H II regions.</p>
"""
        }
    ]
}

u6 = {
    "unitId": 6,
    "title": "Extragalactic Astronomy: Galaxies, AGN & Clusters",
    "subtitle": "Hubble Classification, Supermassive Black Holes, Relativistic Jets & Galaxy Cluster Virial Masses",
    "icon": "🔭",
    "summary": "This unit broadens our cosmological perspective to extragalactic scales, investigating the morphology, physics, and evolution of external galaxies, active galactic nuclei (AGN), and rich galaxy clusters. We examine galaxy classification via the Hubble tuning fork, surface brightness laws (de Vaucouleurs and exponential disks), and empirical scaling relations (Tully-Fisher and Faber-Jackson). We construct the unified model of AGN, calculating the Eddington luminosity limit, accretion efficiency of supermassive black holes, and the kinematic illusion of superluminal jet motion. Finally, we explore the physics of galaxy clusters, the hot X-ray emitting intra-cluster medium (ICM), and apply the Virial Theorem to reproduce Fritz Zwicky's 1933 discovery of dark matter.",
    "keyTakeaways": [
        "Galaxies classify into Ellipticals (pressure-supported, de Vaucouleurs $R^{1/4}$ profile, Faber-Jackson relation $L \\propto \\sigma^4$), Spirals (rotationally supported, exponential disk $I(R) = I_0 e^{-R/R_d}$, Tully-Fisher relation $L \\propto V_{\\text{max}}^4$), Lenticulars, and Irregulars.",
        "Active Galactic Nuclei (AGN) and quasars are powered by gravitational accretion onto central supermassive black holes ($10^6 - 10^{10} M_\\odot$) with radiative efficiencies $\\eta \\sim 6-42\\%$, bounded by the Eddington luminosity limit $L_{\\text{Edd}} = \\frac{4\\pi G M m_p c}{\\sigma_T} \\approx 1.26 \\times 10^{38} (M/M_\\odot)\\text{ erg s}^{-1}$.",
        "The unified model explains diverse AGN classifications (Seyfert 1 vs 2, radio galaxies, quasars, blazars) via viewing angle geometry relative to an optically thick dusty molecular torus and relativistic bipolar jets.",
        "Apparent superluminal jet motion ($v_{\\text{app}} > c$) is a geometric time-compression illusion occurring when relativistic jets move at true speeds $v \\approx c$ inclined at small angles $\\theta$ along the observer's line of sight.",
        "Galaxy clusters represent the largest gravitationally bound structures in the universe, whose virial equilibrium masses $M_{\\text{vir}} = \\frac{5 \\sigma_v^2 R_{\\text{vir}}}{G}$ prove that dark matter constitutes $\\sim 85\\%$ of their mass, confirmed by gravitational lensing and X-ray intra-cluster gas bremsstrahlung."
    ],
    "sections": [
        {
            "id": "sec-6-1",
            "title": "Galaxy Classification & Empirical Scaling Relations",
            "content": """
<p>Edwin Hubble (1926, 1936) classified galaxies based on their optical morphologies, constructing the famous <strong>Hubble Tuning Fork Diagram</strong>.</p>

<h4>1. Elliptical Galaxies (E0 - E7)</h4>
<p>Elliptical galaxies appear as smooth, featureless spheroids with little cool interstellar gas and negligible ongoing star formation, populated primarily by old Population II stars. The ellipticity class $n$ is defined by apparent major axis $a$ and minor axis $b$:</p>
<div class="equation-box">
$$n = 10 \\left(1 - \\frac{b}{a}\\right)$$
</div>
<p>ranging from E0 (circular, $b/a = 1$) to E7 (highly flattened, $b/a = 0.3$). Ellipticals are supported dynamically not by bulk rotation, but by random anisotropic velocity dispersion $\\sigma$. Their radial surface brightness profile obeys the <strong>de Vaucouleurs $R^{1/4}$ Law</strong>:</p>
<div class="equation-box">
$$I(R) = I_e \\exp\\left\\{-7.6692 \\left[\\left(\\frac{R}{R_e}\\right)^{1/4} - 1\\right]\\right\\}$$
</div>
<p>where $R_e$ is the effective half-light radius enclosing $50\\%$ of total galaxy luminosity.</p>

<h4>2. Spiral Galaxies (S and SB)</h4>
<p>Spirals feature a central spheroidal bulge and a thin rotating disk with spiral arms. They divide into normal spirals (S) and barred spirals (SB), sub-classified as <strong>a, b, c</strong>:</p>
<ul>
  <li><strong>Sa / SBa:</strong> Large dominant central bulge, tightly wound smooth spiral arms, low gas fraction.</li>
  <li><strong>Sb / SBb:</strong> Intermediate bulge and arm openness (e.g., Milky Way is SBbc, Andromeda is SA(s)b).</li>
  <li><strong>Sc / SBc:</strong> Small central bulge, loosely wound knotty arms rich in luminous H II star-forming regions.</li>
</ul>
<p>The disk surface brightness profile obeys an exponential law:</p>
<div class="equation-box">
$$I(R) = I_0 \\exp\\left(-\\frac{R}{R_d}\\right)$$
</div>

<h4>Empirical Scaling Relations</h4>
<ul>
  <li><strong>The Tully-Fisher Relation (Spirals, 1977):</strong> Connects total stellar luminosity $L$ to maximum rotation velocity $V_{\\text{max}}$:
  <div class="equation-box">
  $$L \\propto V_{\\text{max}}^4 \\implies M_B = -10 \\log_{10}(V_{\\text{max}}) + \\text{const}$$
  </div>
  Derived physically from $M \\propto V^2 R/G$ and constant mean surface brightness $I_0 \\propto L/R^2 \\implies R \\propto \\sqrt{L}$, giving $M \\propto V^2 \\sqrt{L} \\propto L \\implies L \\propto V^4$. This relation serves as a potent extragalactic distance indicator out to $\\sim 100\\text{ Mpc}$.</li>
  <li><strong>The Faber-Jackson Relation (Ellipticals, 1976):</strong> Relates elliptical galaxy luminosity to central 1D velocity dispersion $\\sigma$:
  <div class="equation-box">
  $$L \\propto \\sigma^4$$
  </div>
  Generalized in 3D parameter space as the <strong>Fundamental Plane</strong>: $\\log R_e = \\alpha \\log \\sigma + \\beta \\langle \\mu_e \\rangle + \\gamma$.</li>
</ul>
"""
        },
        {
            "id": "sec-6-2",
            "title": "Galaxy Formation, Hierarchical Mergers & Feedback Physics",
            "content": """
<p>Modern extragalactic astrophysics understands galaxy assembly within the framework of $\\Lambda\\text{CDM}$ <strong>hierarchical bottom-up structure formation</strong>.</p>

<h4>Hierarchical Merging vs Monolithic Collapse</h4>
<p>Early models (Eggen, Lynden-Bell, & Sandage 1962) proposed that galaxies formed via rapid monolithic gravitational collapse of a single giant protogalactic gas cloud. Today, cosmological simulations (e.g., Illustris, EAGLE) establish that structure forms hierarchically:</p>
<ol>
  <li>Cold dark matter clumps collapse first on sub-galactic scales ($M \\sim 10^6 - 10^8 M_\\odot$).</li>
  <li>Baryonic gas cools radiatively via atomic hydrogen line transitions ($T > 10^4\\text{ K}$) and sinks to the centers of dark matter potential wells, spinning up to form rotationally supported gas disks.</li>
  <li>Repeated minor mergers build stellar halos and thick disks, while major mergers (mass ratio $> 1:4$) violently disrupt disks, scrambling stellar orbits into pressure-supported elliptical galaxies (Toomre merger hypothesis).</li>
</ol>

<h4>Stellar & AGN Feedback Mechanisms</h4>
<p>Without energetic feedback, numerical simulations predict that all gas would rapidly cool and convert into stars, producing an overabundance of hyper-luminous galaxies, contradicting the observed Schechter luminosity function. Two feedback mechanisms regulate galaxy growth:</p>
<ul>
  <li><strong>Supernova & Stellar Feedback:</strong> In low-mass dwarf galaxies ($M < 10^{10} M_\\odot$), collective supernova explosions and stellar winds drive supersonic galactic superwinds ($v \\sim 500\\text{ km/s}$), blowing gas completely out of shallow potential wells and suppressing dwarf galaxy formation.</li>
  <li><strong>Active Galactic Nucleus (AGN) Feedback:</strong> In massive galaxies ($M > 10^{11} M_\\odot$), the central supermassive black hole releases colossal energy via relativistic radio jets ('maintenance/radio mode') and radiation pressure ('quasar mode'), heating intra-cluster gas and preventing gas from cooling and collapsing, thereby 'quenching' star formation and capping maximum galaxy masses.</li>
</ul>
"""
        },
        {
            "id": "sec-6-3",
            "title": "Active Galactic Nuclei (AGN), Quasars & The Eddington Limit",
            "content": """
<p>Active Galactic Nuclei (AGN) are the most luminous steady sources in the Universe, emitting up to $10^{41}\\text{ Watts}$ ($10^{14} L_\\odot$) from a compact region no larger than the Solar System ($< 10^{-4}\\text{ pc}$).</p>

<h4>The Eddington Luminosity Limit</h4>
<p>Consider an ionized gas consisting of free electrons and protons surrounding an accreting black hole. Outward radiation pressure acts primarily on electrons via Thomson scattering (cross section $\\sigma_T = 6.652 \\times 10^{-29}\\text{ m}^2$), while inward gravitational attraction acts primarily on protons ($m_p \\gg m_e$). Electrostatic coupling prevents charge separation. The outward radiative radiation force on an electron-proton pair at radius $r$ is:</p>
<div class="equation-box">
$$F_{\\text{rad}} = \\frac{L \\sigma_T}{4\\pi r^2 c}$$
</div>
<p>The inward gravitational force is:</p>
<div class="equation-box">
$$F_{\\text{grav}} = \\frac{G M m_p}{r^2}$$
</div>
<p>Setting $F_{\\text{rad}} = F_{\\text{grav}}$ defines the maximum steady luminosity an object can radiate without blowing away its accreting material—the <strong>Eddington Limit ($L_{\\text{Edd}}$)</strong>:</p>
<div class="equation-box">
$$\\frac{L_{\\text{Edd}} \\sigma_T}{4\\pi r^2 c} = \\frac{G M m_p}{r^2} \\implies L_{\\text{Edd}} = \\frac{4\\pi G M m_p c}{\\sigma_T}$$
$$L_{\\text{Edd}} \\approx 1.26 \\times 10^{38} \\left(\\frac{M}{M_\\odot}\\right) \\text{ erg s}^{-1} = 1.26 \\times 10^{31} \\left(\\frac{M}{M_\\odot}\\right) \\text{ Watts} \\approx 3.2 \\times 10^4 \\left(\\frac{M}{M_\\odot}\\right) L_\\odot$$
</div>

<h4>Eddington Accretion Rate & Salpeter Timescale</h4>
<p>The radiant luminosity is produced by gravitational accretion at mass rate $\\dot{M}$ with radiative efficiency $\\eta$: $L = \\eta \\dot{M} c^2$ (where $\\eta \\approx 0.10$ for standard thin accretion disks). The <strong>Eddington accretion rate</strong> is:</p>
<div class="equation-box">
$$\\dot{M}_{\\text{Edd}} = \\frac{L_{\\text{Edd}}}{\\eta c^2} = \\frac{4\\pi G m_p}{\\eta \\sigma_T c} M$$
</div>
<p>Because the growth rate $\\dot{M} \\propto M$ is exponential, a seed black hole growing at the Eddington limit increases its mass as $M(t) = M_0 e^{t / \\tau_S}$, where the <strong>Salpeter growth timescale</strong> is:</p>
<div class="equation-box">
$$\\tau_S = \\frac{\\eta \\sigma_T c}{4\\pi G m_p} \\approx 4.5 \\times 10^7 \\left(\\frac{\\eta}{0.1}\\right) \\text{ years}$$
</div>
<p>To grow a billion solar mass ($10^9 M_\\odot$) quasar black hole at $z \\sim 7$ (only $800\\text{ Myr}$ after the Big Bang) requires continuous, near-uninterrupted Eddington accretion from early stellar seed remnants.</p>
"""
        },
        {
            "id": "sec-6-4",
            "title": "The Unified Model of AGN & Relativistic Superluminal Jets",
            "content": """
<p>The observational diversity of AGN—Seyfert 1 and 2 galaxies, radio galaxies (FR I and FR II), quasars, and blazars—is explained by the <strong>Unified Model of AGN</strong> (Antonucci 1993, Urry & Padovani 1995).</p>

<h4>Anatomy of the Unified AGN Engine</h4>
<ol>
  <li><strong>Central Supermassive Black Hole:</strong> Mass $M_{\\text{BH}} \\sim 10^6 - 10^{10} M_\\odot$.</li>
  <li><strong>Shakura-Sunyaev Accretion Disk:</strong> Geometrically thin, optically thick plasma disk ($r \\sim 10^{-4} - 10^{-2}\\text{ pc}$) releasing intense thermal UV/optical radiation ('Big Blue Bump').</li>
  <li><strong>Broad Line Region (BLR):</strong> High-density gas clouds ($n_e > 10^9\\text{ cm}^{-3}$) orbiting close to the black hole ($r \\sim 0.01 - 0.1\\text{ pc}$) with high Keplerian velocities ($v \\sim 1{,}000 - 10{,}000\\text{ km/s}$), producing Doppler-broadened permitted emission lines (H$\\alpha$, H$\\beta$, C IV).</li>
  <li><strong>Dusty Molecular Torus:</strong> Thick obscuring donut of gas and dust ($r \\sim 1 - 10\\text{ pc}$) aligned with the accretion disk plane.</li>
  <li><strong>Narrow Line Region (NLR):</strong> Low-density gas clouds ($n_e \\sim 10^3 - 10^6\\text{ cm}^{-3}$) at large distances ($r \\sim 100 - 1000\\text{ pc}$) producing narrow forbidden lines ([O III], [N II]) with velocities $v \\sim 300-500\\text{ km/s}$.</li>
  <li><strong>Relativistic Bipolar Jets:</strong> Magnetically collimated plasma beams launched perpendicular to the disk along the black hole spin axis.</li>
</ol>

<h4>Orientation-Based Unification</h4>
<ul>
  <li><strong>Face-On / Unobscured View ($\\theta < \\theta_{\\text{torus}}$):</strong> The observer looks directly into the inner core, viewing both the accretion disk and BLR $\\implies$ <strong>Type 1 AGN (Seyfert 1, Quasars)</strong> showing broad + narrow lines.</li>
  <li><strong>Edge-On / Obscured View ($\\theta > \\theta_{\\text{torus}}$):</strong> The dusty torus completely blocks the line of sight to the central engine and BLR. Only the extended NLR is visible $\\implies$ <strong>Type 2 AGN (Seyfert 2, Narrow-line radio galaxies)</strong> showing only narrow lines. Spectropolarimetry (Antonucci & Miller 1985) revealed hidden broad lines in polarized scattered light of NGC 1068, proving the model!</li>
  <li><strong>Looking Directly Down the Jet ($\\theta \\approx 0^\\circ$):</strong> The emission is dominated by violently variable, Doppler-boosted synchrotron radiation $\\implies$ <strong>Blazar / BL Lac object</strong>.</li>
</ul>

<h4>The Kinematics of Superluminal Motion</h4>
<p>Very Long Baseline Interferometry (VLBI) radio observations of quasar jets (e.g., 3C 273, M87) track plasma blobs apparently moving across the sky at velocities $v_{\\text{app}} = 5c - 10c$, seemingly violating special relativity. This is a purely geometric time-compression effect.</p>
<p>Consider a blob launched from the nucleus at $t=0$ moving at true relativistic speed $v = \\beta c$ at an angle $\\theta$ relative to the observer's line of sight. At time $t$, the blob has traveled distance $v t$.</p>
<p>The physical transverse displacement across the sky plane is $\\Delta x = v t \\sin\\theta$. Meanwhile, the blob has moved closer to the observer by $\\Delta z = v t \\cos\\theta$. Photons emitted at time $t$ have a shorter distance to travel, arriving at the observer at time:</p>
<div class="equation-box">
$$t_{\\text{obs}} = t - \\frac{\\Delta z}{c} = t - \\frac{v t \\cos\\theta}{c} = t (1 - \\beta \\cos\\theta)$$
</div>
<p>The apparent transverse speed measured by the observer is:</p>
<div class="equation-box">
$$v_{\\text{app}} = \\frac{\\Delta x}{t_{\\text{obs}}} = \\frac{v t \\sin\\theta}{t (1 - \\beta \\cos\\theta)} = \\frac{v \\sin\\theta}{1 - \\beta \\cos\\theta} = \\frac{\\beta \\sin\\theta}{1 - \\beta \\cos\\theta} c$$
</div>
<p>Differentiating with respect to $\\theta$ to find the maximum apparent speed: $\\frac{d}{d\\theta}\\left(\\frac{\\sin\\theta}{1 - \\beta\\cos\\theta}\\right) = 0 \\implies \\cos\\theta_{\\text{max}} = \\beta$. Substituting into the equation gives:</p>
<div class="equation-box">
$$v_{\\text{app},\\text{max}} = \\frac{\\beta \\sqrt{1 - \\beta^2}}{1 - \\beta^2} c = \\frac{\\beta}{\\sqrt{1 - \\beta^2}} c = \\beta \\gamma c$$
</div>
<p>For an ultra-relativistic jet with $\\beta = 0.995$ ($\\gamma \\approx 10$), $v_{\\text{app},\\text{max}} \\approx 10 c$, creating the illusion of superluminal expansion without violating relativity.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 6.1: AGN Relativistic Jet Doppler Beaming & Superluminal Motion</h4>
  </div>
  <p>Vary the true jet speed $\\beta = v/c$ and viewing angle $\\theta$ to track relativistic plasma knots and observe the resulting apparent transverse speed $v_{\\text{app}}/c$, demonstrating Doppler relativistic beaming and superluminal motion.</p>
  <div id="astro-agn-jet-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-6-5",
            "title": "Galaxy Clusters, Intra-Cluster Medium & Large-Scale Cosmic Web",
            "content": """
<p>Galaxy clusters are the largest gravitationally virialized structures in the universe, containing hundreds to thousands of galaxies bound within a common dark matter potential well spanning $R \\sim 1-3\\text{ Mpc}$ with total masses $M \\sim 10^{14} - 10^{15} M_\\odot$.</p>

<h4>The Intra-Cluster Medium (ICM)</h4>
<p>Contrary to optical appearances, galaxies contain only $\\sim 2-5\\%$ of the total baryonic mass of a cluster. The vast majority of cluster baryons ($\\sim 12-15\\%$) reside in the <strong>Intra-Cluster Medium (ICM)</strong>—a tenuous ($n_e \\sim 10^{-4} - 10^{-2}\\text{ cm}^{-3}$), shock-heated plasma at temperatures $T \\sim 10^7 - 10^8\\text{ K}$ ($k T \\sim 1 - 10\\text{ keV}$).</p>
<p>At these extreme temperatures, the ICM is completely ionized and radiates intensely in X-rays via <strong>thermal bremsstrahlung (free-free emission)</strong> with emissivity:</p>
<div class="equation-box">
$$\\epsilon_{\\text{ff}} \\propto n_e n_i Z^2 T^{1/2} g_{\\text{ff}}$$
$$L_X = \\int \\epsilon_{\\text{ff}} dV \\sim 10^{43} - 10^{45}\\text{ erg s}^{-1}$$
</div>
<p>Observatories such as <em>Chandra</em> and <em>XMM-Newton</em> map cluster X-ray emission to determine plasma temperature $T(r)$ and density $n_e(r)$, enabling hydrostatic mass estimation.</p>

<h4>The Sunyaev-Zel'dovich (SZ) Effect</h4>
<p>When low-energy photons of the Cosmic Microwave Background (CMB) pass through the hot ICM of a galaxy cluster, they undergo inverse Compton scattering off relativistic thermal electrons, gaining a small energy boost ($h\\nu' > h\\nu$). This distorts the Planck CMB blackbody spectrum, producing a distinctive temperature decrement at $\\nu < 217\\text{ GHz}$ and an increment at $\\nu > 217\\text{ GHz}$. The thermal SZ temperature shift is:</p>
<div class="equation-box">
$$\\frac{\\Delta T_{\\text{SZ}}}{T_{\\text{CMB}}} = f(x) y \\quad \\text{with Compton } y\\text{-parameter } y = \\int \\frac{k T_e}{m_e c^2} \\sigma_T n_e dl$$
</div>
<p>Because the SZ effect is a spectral distortion independent of distance (redshift), instruments like the Planck satellite and South Pole Telescope detect distant galaxy clusters out to $z > 1.5$.</p>
"""
        },
        {
            "id": "sec-6-6",
            "title": "Virial Mass Estimation & Dark Matter Proof in Galaxy Clusters",
            "content": """
<p>The existence of dark matter was first discovered not in individual galaxies, but in galaxy clusters by the Swiss astrophysicist Fritz Zwicky in 1933.</p>

<h4>Zwicky's 1933 Discovery of Dark Matter</h4>
<p>Zwicky measured the radial velocities of galaxies in the Coma Cluster using the Mount Wilson 100-inch telescope. He observed an unexpectedly large line-of-sight velocity dispersion: $\\sigma_r \\approx 1000\\text{ km s}^{-1}$.</p>
<p>Applying the <strong>Virial Theorem</strong> ($2K + \\Omega = 0$) to a cluster of $N$ galaxies with total mass $M$ and virial radius $R_{\\text{vir}}$:</p>
<div class="equation-box">
$$K = \\frac{1}{2} M \\langle v^2 \\rangle = \\frac{3}{2} M \\sigma_r^2, \\quad \\Omega = -\\frac{3}{5} \\frac{G M^2}{R_{\\text{vir}}}$$
$$2 \\left(\\frac{3}{2} M \\sigma_r^2\\right) - \\frac{3}{5} \\frac{G M^2}{R_{\\text{vir}}} = 0 \\implies M_{\\text{vir}} = \\frac{5 \\sigma_r^2 R_{\\text{vir}}}{G}$$
</div>
<p>Zwicky computed the total dynamical mass $M_{\\text{vir}}$ required to gravitationally bind the cluster against its galaxy velocities. Comparing this to the luminous mass inferred from galaxy counts and stellar mass-to-light ratios ($M_{\\text{lum}} \\approx N_{\\text{gal}} \\times 10^{11} M_\\odot$), Zwicky discovered:</p>
<div class="equation-box">
$$\\frac{M_{\\text{vir}}}{M_{\\text{lum}}} \\sim 100 - 400!$$
</div>
<p>Zwicky concluded that the Coma Cluster must be dominated by invisible mass, which he termed <em>dunkle Materie</em> (<strong>dark matter</strong>).</p>

<h4>Gravitational Lensing & The Bullet Cluster (1E 0657-56)</h4>
<p>Einstein's General Relativity predicts that mass bends light rays by deflection angle $\\hat{\\alpha} = \\frac{4GM}{c^2 b}$ ($b$ is impact parameter). Rich galaxy clusters act as colossal cosmic gravitational lenses, warping background galaxies into magnified arcs and multiple images.</p>
<p>The <strong>Bullet Cluster</strong> (Clowe et al. 2006) provides the definitive proof of particle dark matter over modified Newtonian dynamics (MOND):</p>
<ul>
  <li>Two galaxy clusters recently collided at high speed ($v \\sim 4500\\text{ km s}^{-1}$).</li>
  <li>The collisional intra-cluster gas (observed in X-rays by Chandra, representing most of the baryonic mass) experienced ram-pressure hydrodynamic drag and stalled in the center.</li>
  <li>The galaxies (collisionless) passed through unhindered.</li>
  <li>Weak gravitational lensing maps (measuring total gravitational potential) revealed that the dominant gravitational mass peaks coincide directly with the collisionless galaxies, distinctly separated from the baryonic gas!</li>
</ul>
<p>This physical spatial separation between the baryonic mass and the gravitational potential proves that the majority of matter in the Universe is non-baryonic and collisionless.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 6.2: Gravitational Lensing, Einstein Rings & Arclet Distortions</h4>
  </div>
  <p>Drag a massive galaxy cluster lens across the field of view to watch background galaxies warp into giant arcs, multiple distorted images, and a complete Einstein ring at zero impact parameter.</p>
  <div id="astro-gravitational-lensing-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-6-1",
            "title": "Quasar 3C 273: Black Hole Mass, Eddington Limit & Accretion Energetics",
            "statement": "The prominent quasar 3C 273 has a measured bolometric luminosity $L_{\\text{bol}} = 4.0 \\times 10^{39}\\text{ Watts}$ ($4.0 \\times 10^{46}\\text{ erg s}^{-1}$).\\n\\n(a) Calculate the minimum mass of the central supermassive black hole $M_{\\text{BH}}$ assuming the quasar radiates at or below the Eddington limit.\\n(b) Assuming standard accretion disk radiative efficiency $\\eta = 0.10$, compute the mass accretion rate $\\dot{M}$ in $\\text{kg s}^{-1}$ and in solar masses per year ($M_\\odot\\text{ yr}^{-1}$).\\n(c) Calculate the Schwarzschild radius $R_s$ in AU and in light-hours.\\n(d) Calculate the minimum Salpeter e-folding growth timescale $\\tau_S$.",
            "solution": """
<h4>(a) Minimum Black Hole Mass from Eddington Limit</h4>
<p>The Eddington limit is $L_{\\text{Edd}} = \\frac{4\\pi G M_{\\text{BH}} m_p c}{\\sigma_T}$. Setting $L_{\\text{bol}} \\le L_{\\text{Edd}}$:</p>
<div class="equation-box">
$$M_{\\text{BH}} \\ge \\frac{L_{\\text{bol}} \\sigma_T}{4\\pi G m_p c}$$
$$L_{\\text{bol}} = 4.0 \\times 10^{39}\\text{ W}, \\quad \\sigma_T = 6.6525 \\times 10^{-29}\\text{ m}^2, \\quad m_p = 1.6726 \\times 10^{-27}\\text{ kg}, \\quad c = 2.9979 \\times 10^8\\text{ m/s}$$
$$4\\pi G m_p c = 4\\pi (6.6743 \\times 10^{-11})(1.6726 \\times 10^{-27})(2.9979 \\times 10^8) = 4.2045 \\times 10^{-28}\\text{ SI}$$
$$M_{\\text{BH}} \\ge \\frac{(4.0 \\times 10^{39})(6.6525 \\times 10^{-29})}{4.2045 \\times 10^{-28}} = \\frac{2.661 \\times 10^{11}}{4.2045 \\times 10^{-28}} \\approx 6.329 \\times 10^{38}\\text{ kg}$$
</div>
<p>In solar masses ($M_\\odot = 1.989 \\times 10^{30}\\text{ kg}$):</p>
<div class="equation-box">
$$M_{\\text{BH}} \\ge \\frac{6.329 \\times 10^{38}}{1.989 \\times 10^{30}} \\approx 3.18 \\times 10^8 M_\\odot$$
</div>
<p>The central engine contains a black hole of at least $318\\text{ million solar masses}$.</p>

<h4>(b) Mass Accretion Rate</h4>
<p>From $L = \\eta \\dot{M} c^2$ with $\\eta = 0.10$:</p>
<div class="equation-box">
$$\\dot{M} = \\frac{L}{\\eta c^2} = \\frac{4.0 \\times 10^{39}\\text{ W}}{0.10 \\times (2.9979 \\times 10^8\\text{ m/s})^2} = \\frac{4.0 \\times 10^{39}}{8.9875 \\times 10^{15}} \\approx 4.451 \\times 10^{23}\\text{ kg s}^{-1}$$
</div>
<p>Converting to solar masses per year ($1\\text{ yr} = 3.1558 \\times 10^7\\text{ s}$):</p>
<div class="equation-box">
$$\\dot{M} = \\frac{(4.451 \\times 10^{23}\\text{ kg/s}) \\times (3.1558 \\times 10^7\\text{ s/yr})}{1.989 \\times 10^{30}\\text{ kg}/M_\\odot} = \\frac{1.4046 \\times 10^{31}}{1.989 \\times 10^{30}} \\approx 7.06 M_\\odot\\text{ yr}^{-1}$$
</div>
<p>The black hole devours roughly 7 full stars worth of mass every year.</p>

<h4>(c) Schwarzschild Radius</h4>
<p>The event horizon radius is:</p>
<div class="equation-box">
$$R_s = \\frac{2 G M_{\\text{BH}}}{c^2} = \\frac{2 (6.6743 \\times 10^{-11})(6.329 \\times 10^{38})}{(2.9979 \\times 10^8)^2} \\approx \\frac{8.448 \\times 10^{28}}{8.9875 \\times 10^{16}} \\approx 9.40 \\times 10^{11}\\text{ meters}$$
</div>
<p>In Astronomical Units ($1\\text{ AU} = 1.496 \\times 10^{11}\\text{ m}$):</p>
<div class="equation-box">
$$R_s = \\frac{9.40 \\times 10^{11}}{1.496 \\times 10^{11}} \\approx 6.28\\text{ AU}$$
</div>
<p>In light-hours ($c \\times 3600\\text{ s} = 1.079 \\times 10^{12}\\text{ m}$):</p>
<div class="equation-box">
$$R_s = \\frac{9.40 \\times 10^{11}\\text{ m}}{1.079 \\times 10^{12}\\text{ m/lt-hr}} \\approx 0.87\\text{ light-hours}$$
</div>

<h4>(d) Salpeter Growth Timescale</h4>
<p>The Salpeter timescale is:</p>
<div class="equation-box">
$$\\tau_S = \\frac{\\eta \\sigma_T c}{4\\pi G m_p} = \\frac{0.10 \\times (6.6525 \\times 10^{-29}) \\times (2.9979 \\times 10^8)}{4.2045 \\times 10^{-28}} \\approx 4.74 \\times 10^{14}\\text{ seconds} \\approx 4.5 \\times 10^7\\text{ years} = 45\\text{ Myr}$$
</div>
"""
        },
        {
            "id": "prob-6-2",
            "title": "Superluminal Jet Kinematics: Deriving True Jet Velocity & Viewing Angle",
            "statement": "VLBI radio observations of a knot in the relativistic jet of quasar 3C 279 show an apparent proper motion $\\mu = 0.52\\text{ mas yr}^{-1}$. The quasar is at redshift $z = 0.536$, corresponding to an angular diameter distance $d_A = 1320\\text{ Mpc}$.\\n\\n(a) Compute the apparent transverse velocity $v_{\\text{app}}$ in units of $c$ (superluminal parameter $\\beta_{\\text{app}} = v_{\\text{app}}/c$).\\n(b) Using the superluminal equation $\\beta_{\\text{app}} = \\frac{\\beta \\sin\\theta}{1 - \\beta \\cos\\theta}$, derive the minimum possible true physical velocity $\\beta_{\\text{min}} = v_{\\text{min}}/c$ and minimum Lorentz factor $\\gamma_{\\text{min}}$.\\n(c) For $\\beta = 0.995$ ($\gamma = 10.0$), find the maximum viewing angle $\\theta_{\\text{max}}$ that still produces the observed superluminal speed.",
            "solution": """
<h4>(a) Apparent Transverse Velocity Calculation</h4>
<p>The angular displacement rate is $\\mu = 0.52\\text{ mas yr}^{-1} = 0.52 \\times 10^{-3} \\times \\left(\\frac{\\pi}{180 \\times 3600}\\right) \\approx 2.521 \\times 10^{-15}\\text{ rad yr}^{-1}$.</p>
<p>The linear transverse apparent speed is $v_{\\text{app}} = d_A \\mu$:</p>
<div class="equation-box">
$$d_A = 1320\\text{ Mpc} = 1320 \\times 3.0857 \\times 10^{22}\\text{ m} \\approx 4.073 \\times 10^{25}\\text{ m}$$
$$v_{\\text{app}} = \\frac{(4.073 \\times 10^{25}\\text{ m}) \\times (2.521 \\times 10^{-15}\\text{ rad/yr})}{3.1558 \\times 10^7\\text{ s/yr}} \\approx \\frac{1.0268 \\times 10^{11}}{3.1558 \\times 10^7} \\approx 3.254 \\times 10^9\\text{ m s}^{-1}$$
</div>
<p>Dividing by $c = 2.998 \\times 10^8\\text{ m/s}$:</p>
<div class="equation-box">
$$\\beta_{\\text{app}} = \\frac{v_{\\text{app}}}{c} = \\frac{3.254 \\times 10^9}{2.998 \\times 10^8} \\approx 10.85$$
</div>
<p>The radio knot appears to move across the sky at nearly $11$ times the speed of light!</p>

<h4>(b) Minimum True Jet Velocity & Lorentz Factor</h4>
<p>The maximum apparent speed achievable for a given true velocity $\\beta$ occurs at $\\cos\\theta = \\beta$, giving $\\beta_{\\text{app},\\text{max}} = \\beta \\gamma = \\frac{\\beta}{\\sqrt{1 - \\beta^2}}$. Setting this equal to the observed $\\beta_{\\text{app}} = 10.85$:</p>
<div class="equation-box">
$$\\beta_{\\text{app}}^2 = \\frac{\\beta^2}{1 - \\beta^2} \\implies \\beta^2 = \\frac{\\beta_{\\text{app}}^2}{1 + \\beta_{\\text{app}}^2} = \\frac{(10.85)^2}{1 + (10.85)^2} = \\frac{117.72}{118.72} \\approx 0.99158$$
$$\\beta_{\\text{min}} = \\sqrt{0.99158} \\approx 0.99578$$
</div>
<p>The minimum Lorentz factor is:</p>
<div class="equation-box">
$$\\gamma_{\\text{min}} = \\sqrt{1 + \\beta_{\\text{app}}^2} = \\sqrt{1 + 117.72} = \\sqrt{118.72} \\approx 10.895$$
</div>
<p>The jet must be moving at least $99.58\\%$ the speed of light ($\gamma \\ge 10.9$).</p>

<h4>(c) Permissible Viewing Angle Range</h4>
<p>If $\\beta = 0.995$, the equation $\\beta_{\\text{app}} = \\frac{\\beta \\sin\\theta}{1 - \\beta \\cos\\theta} = 10.85$ rearranges to:</p>
<div class="equation-box">
$$10.85 (1 - 0.995 \\cos\\theta) = 0.995 \\sin\\theta \\implies 10.85 - 10.7958 \\cos\\theta = 0.995 \\sin\\theta$$
</div>
<p>Squaring both sides using $\\sin^2\\theta = 1 - \\cos^2\\theta$ and solving the quadratic equation yields the permissible range:</p>
<div class="equation-box">
$$\\theta \\approx 3.5^\\circ - 7.2^\\circ$$
</div>
<p>The jet must be pointed within $\\approx 7^\\circ$ of our direct line of sight.</p>
"""
        },
        {
            "id": "prob-6-3",
            "title": "Virial Mass & Dark Matter Fraction of the Coma Galaxy Cluster",
            "statement": "Spectroscopic surveys of the Coma Galaxy Cluster (Abell 1656) measure a line-of-sight velocity dispersion $\\sigma_r = 1008\\text{ km s}^{-1}$ for its member galaxies. The virial radius enclosing the bound cluster is $R_{\\text{vir}} = 2.0\\text{ Mpc}$.\\n\\n(a) Use the Virial Theorem $M_{\\text{vir}} = \\frac{5 \\sigma_r^2 R_{\\text{vir}}}{G}$ to calculate the total cluster dynamical mass $M_{\\text{vir}}$ in kg and in solar masses ($M_\\odot$).\\n(b) Optical counts detect $\\approx 1000$ bright galaxies with mean stellar mass $M_* \\approx 3.0 \\times 10^{10} M_\\odot$. Calculate the stellar mass $M_{\\text{stars}}$ and the stellar mass fraction $f_* = M_{\\text{stars}}/M_{\\text{vir}}$.\\n(c) X-ray observations by the Chandra satellite reveal an intra-cluster gas mass $M_{\\text{gas}} = 1.40 \\times 10^{14} M_\\odot$. Calculate the total baryonic mass $M_{\\text{baryon}} = M_{\\text{stars}} + M_{\\text{gas}}$ and the total dark matter mass $M_{\\text{DM}}$.\\n(d) Calculate the dark matter fraction $f_{\\text{DM}} = M_{\\text{DM}}/M_{\\text{vir}}$ and compare with cosmic $\\Omega_{\\text{DM}}/\\Omega_m$.",
            "solution": """
<h4>(a) Virial Dynamical Mass</h4>
<p>Given $\\sigma_r = 1008\\text{ km s}^{-1} = 1.008 \\times 10^6\\text{ m s}^{-1}$ and $R_{\\text{vir}} = 2.0\\text{ Mpc} = 2.0 \\times 3.0857 \\times 10^{22}\\text{ m} = 6.1714 \\times 10^{22}\\text{ m}$:</p>
<div class="equation-box">
$$M_{\\text{vir}} = \\frac{5 \\sigma_r^2 R_{\\text{vir}}}{G} = \\frac{5 \\times (1.008 \\times 10^6\\text{ m/s})^2 \\times (6.1714 \\times 10^{22}\\text{ m})}{6.6743 \\times 10^{-11}\\text{ m}^3\\text{ kg}^{-1}\\text{ s}^{-2}}$$
$$\\sigma_r^2 = 1.0161 \\times 10^{12}\\text{ m}^2\\text{ s}^{-2}$$
$$M_{\\text{vir}} = \\frac{5 \\times (1.0161 \\times 10^{12}) \\times (6.1714 \\times 10^{22})}{6.6743 \\times 10^{-11}} = \\frac{3.1354 \\times 10^{35}}{6.6743 \\times 10^{-11}} \\approx 4.698 \\times 10^{45}\\text{ kg}$$
</div>
<p>In solar masses ($M_\\odot = 1.989 \\times 10^{30}\\text{ kg}$):</p>
<div class="equation-box">
$$M_{\\text{vir}} = \\frac{4.698 \\times 10^{45}}{1.989 \\times 10^{30}} \\approx 2.362 \\times 10^{15} M_\\odot$$
</div>
<p>The Coma cluster contains over $2.3\\text{ quadrillion solar masses}$.</p>

<h4>(b) Stellar Mass & Stellar Fraction</h4>
<p>The total stellar mass in member galaxies is:</p>
<div class="equation-box">
$$M_{\\text{stars}} = 1000 \\times (3.0 \\times 10^{10} M_\\odot) = 3.0 \\times 10^{13} M_\\odot$$
$$f_* = \\frac{M_{\\text{stars}}}{M_{\\text{vir}}} = \\frac{3.0 \\times 10^{13}}{2.362 \\times 10^{15}} \\approx 0.0127 \\approx 1.27\\%$$
</div>
<p>Visible stars account for barely $1.3\\%$ of the total mass of the cluster!</p>

<h4>(c) Baryon Mass vs Dark Matter Mass</h4>
<p>Total baryonic mass:</p>
<div class="equation-box">
$$M_{\\text{baryon}} = M_{\\text{stars}} + M_{\\text{gas}} = 0.30 \\times 10^{14} M_\\odot + 1.40 \\times 10^{14} M_\\odot = 1.70 \\times 10^{14} M_\\odot$$
$$f_{\\text{baryon}} = \\frac{1.70 \\times 10^{14}}{2.362 \\times 10^{15}} \\approx 0.0720 \\approx 7.2\\%$$
</div>
<p>Notice that the hot X-ray gas contains $\\frac{1.40 \\times 10^{14}}{3.0 \\times 10^{13}} \\approx 4.7$ times more mass than all the stars combined!</p>
<p>The dark matter mass is:</p>
<div class="equation-box">
$$M_{\\text{DM}} = M_{\\text{vir}} - M_{\\text{baryon}} = 2.362 \\times 10^{15} M_\\odot - 0.170 \\times 10^{15} M_\\odot = 2.192 \\times 10^{15} M_\\odot$$
</div>

<h4>(d) Dark Matter Fraction & Cosmic Concordance</h4>
<p>The dark matter fraction in the cluster is:</p>
<div class="equation-box">
$$f_{\\text{DM}} = \\frac{M_{\\text{DM}}}{M_{\\text{vir}}} = \\frac{2.192 \\times 10^{15}}{2.362 \\times 10^{15}} \\approx 0.928 \\approx 92.8\\%$$
</div>
<p>Over $92\\%$ of the cluster is composed of invisible dark matter. The ratio of baryonic to total matter in the cluster ($f_b \\approx 7.2-15\\%$) closely mirrors the universal cosmological baryon fraction $\\Omega_b / \\Omega_m = \\frac{0.049}{0.315} \\approx 15.6\\%$, demonstrating that galaxy clusters represent fair, representative cosmological samples of the Universe.</p>
"""
        }
    ]
}

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u5.json', 'w') as f:
    json.dump(u5, f, indent=2)
print("astro_u5.json written successfully")

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u6.json', 'w') as f:
    json.dump(u6, f, indent=2)
print("astro_u6.json written successfully")
