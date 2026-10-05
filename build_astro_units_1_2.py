import json
import os

u1 = {
    "unitId": 1,
    "title": "Celestial Mechanics, Coordinate Systems & The Astronomical Distance Ladder",
    "subtitle": "Spherical Astrometry, Space Velocity, Telescope Optics & Cosmic Metrology",
    "icon": "🔭",
    "summary": "This foundational unit establishes the quantitative framework of modern observational astrophysics. We develop the spherical geometry of the celestial sphere, transform between horizontal, equatorial, ecliptic, and galactic coordinate frameworks, and quantify the kinematics of precession, nutation, and stellar proper motions. We derive the optical principles of modern ground- and space-based telescopes, atmospheric seeing limitations, and adaptive optics. Finally, we establish the base rungs of the cosmic distance ladder—from trigonometric parallax and moving cluster kinematics to the Cepheid Leavitt Law and distance modulus formalism—constructing the geometric anchor for all astrophysical measurements.",
    "keyTakeaways": [
        "The celestial sphere maps angular positions on the sky using equatorial coordinates (Right Ascension $\\alpha$, Declination $\\delta$), which link to local observer coordinates (altitude $a$, azimuth $A$) via spherical trigonometry and Local Sidereal Time ($\\text{LST} = H + \\alpha$).",
        "A star's full space velocity vector $\\vec{v}$ decomposes into radial velocity $v_r$ measured via Doppler spectroscopic shifts and transverse velocity $v_t = 4.74 \\mu d$ measured via astrometric proper motion $\\mu$ and distance $d$.",
        "Diffraction-limited angular resolution is fundamentally governed by the Rayleigh criterion $\\theta = 1.22\\lambda/D$, with ground-based performance limited by Kolmogorov atmospheric turbulence and restored using laser guide star adaptive optics.",
        "The cosmic distance ladder anchors all extragalactic measurements through trigonometric parallax ($d = 1/p$), standard candles (Cepheid Leavitt Law $M_V \\approx -2.78\\log_{10} P - 1.35$), and the distance modulus $\\mu = m - M = 5\\log_{10}(d/\\text{pc}) - 5 + A_V$ with interstellar extinction corrections.",
        "The observable universe spans scales from subatomic nucleosynthesis realms to the Hubble horizon radius $R_H = c/H_0 \\approx 4.3\\text{ Gpc}$, with baryonic matter comprising merely $\\approx 4.9\\%$ of the cosmic energy density."
    ],
    "sections": [
        {
            "id": "sec-1-1",
            "title": "Modern Astronomy & The Celestial Sphere Geometry",
            "content": """
<p>Astronomy is intrinsically an observational science wherein empirical data arrive almost exclusively in the form of electromagnetic photons, gravitational radiation, and cosmic neutrinos. To catalog, track, and interpret astrophysical phenomena across vast distances, astrometry projects all celestial bodies onto an imaginary, infinitely large concentric sphere known as the <strong>celestial sphere</strong>, centered upon the terrestrial observer or the Earth's barycenter.</p>

<h4>Fundamental Spherical Reference Geometry</h4>
<p>The diurnal rotation of the Earth about its geographic polar axis defines fundamental reference poles and circles projected onto the sky:</p>
<ul>
  <li><strong>Zenith and Nadir:</strong> The zenith $Z$ is the point directly overhead along the local plumb line (gravitational normal), while the nadir is the diametrically opposed point directly below the observer ($180^\circ$ from zenith).</li>
  <li><strong>Astronomical Horizon:</strong> The great circle on the celestial sphere whose plane is perpendicular to the observer's local zenith-nadir vertical axis. Any point on the horizon lies exactly $90^\circ$ from the zenith.</li>
  <li><strong>Celestial Poles:</strong> The intersections of the Earth's rotation axis extended infinitely into space with the celestial sphere define the North Celestial Pole (NCP, near $\\alpha$ Ursae Minoris / Polaris) and the South Celestial Pole (SCP).</li>
  <li><strong>Celestial Equator:</strong> The projection of the Earth's terrestrial equator onto the celestial sphere, forming a great circle equidistant ($90^\circ$) from both celestial poles.</li>
  <li><strong>Ecliptic:</strong> The apparent annual path traced by the Sun across the background stars, corresponding to the projection of the Earth-Sun orbital plane. The ecliptic is tilted relative to the celestial equator by the obliquity of the ecliptic $\\varepsilon \\approx 23^\\circ 26' 14''$ ($23.44^\\circ$).</li>
  <li><strong>Equinoxes and Solstices:</strong> The two intersection nodes between the ecliptic and the celestial equator are the <em>Vernal Equinox</em> (First Point of Aries, $\\Upsilon$, solar crossing from south to north around March 21) and the <em>Autumnal Equinox</em> (solar crossing north to south around September 23). The extrema of solar declination define the summer solstice ($+23.44^\\circ$) and winter solstice ($-23.44^\\circ$).</li>
</ul>

<h4>Spherical Trigonometry Foundations</h4>
<p>Calculations on the celestial sphere operate on spherical triangles bounded by great circle arcs. For a spherical triangle with angles $A, B, C$ and opposite arc lengths $a, b, c$ (measured in radians or degrees):</p>
<div class="equation-box">
$$\\cos a = \\cos b \\cos c + \\sin b \\sin c \\cos A$$
$$\\frac{\\sin a}{\\sin A} = \\frac{\\sin b}{\\sin B} = \\frac{\\sin c}{\\sin C}$$
$$\\sin a \\cos B = \\cos b \\sin c - \\sin b \\cos c \\cos A$$
</div>
<p>These spherical relations enable exact, analytic coordinate transformations between local horizon systems and universal equatorial grids.</p>
"""
        },
        {
            "id": "sec-1-2",
            "title": "Astronomical Coordinate Frameworks & Transformations",
            "content": """
<p>Astrophysicists employ distinct coordinate systems tailored to local observation, equatorial cataloging, planetary orbital dynamics, and galactic kinematics.</p>

<h4>1. Horizontal (Alt-Azimuth) System</h4>
<p>The horizontal coordinate system is fixed to the local observer on Earth:</p>
<ul>
  <li><strong>Altitude ($a$ or $h$):</strong> The angular distance of the object measured vertically from the horizon along the object's vertical circle ($0^\\circ \\le a \\le +90^\\circ$ above horizon; negative below). The zenith angle is $z = 90^\\circ - a$.</li>
  <li><strong>Azimuth ($A$):</strong> The angular distance along the horizon measured eastward from the North cardinal point ($0^\\circ \\le A < 360^\\circ$).</li>
</ul>
<p>Because the Earth rotates, altitude and azimuth change continuously with time and differ for every terrestrial latitude $\\phi$ and longitude $\\lambda$.</p>

<h4>2. Equatorial Coordinate System</h4>
<p>The equatorial system projects the Earth's latitude and longitude onto the sky, creating a frame largely independent of observer location and diurnal rotation:</p>
<ul>
  <li><strong>Declination ($\\delta$):</strong> The angular distance north or south of the celestial equator ($-90^\\circ \\le \\delta \\le +90^\\circ$), analogous to terrestrial latitude.</li>
  <li><strong>Right Ascension ($\\alpha$ or $\\text{RA}$):</strong> The angular distance measured eastward along the celestial equator from the Vernal Equinox $\\Upsilon$ to the hour circle passing through the object. It is conventionally measured in hours, minutes, and seconds ($0^\\text{h} \\le \\alpha < 24^\\text{h}$), where $1^\\text{h} = 15^\\circ$, $1^\\text{m} = 15'$, and $1^\\text{s} = 15''$.</li>
</ul>

<h4>Sidereal Time and Hour Angle</h4>
<p>The <strong>Hour Angle ($H$)</strong> is the angle measured westward along the celestial equator from the observer's local meridian to the object's hour circle ($0^\\text{h} \\le H < 24^\\text{h}$). <strong>Local Sidereal Time ($\\text{LST}$)</strong> is defined as the hour angle of the vernal equinox. The fundamental relationship connects these quantities:</p>
<div class="equation-box">
$$\\text{LST} = H + \\alpha$$
</div>
<p>An object culminates (crosses the local celestial meridian at maximum altitude) when $H = 0^\\text{h}$, which occurs precisely when $\\text{LST} = \\alpha$.</p>

<h4>Mathematical Transformation: Equatorial to Horizontal</h4>
<p>Applying the spherical law of cosines and sines to the triangle formed by the NCP, the Zenith, and the celestial object ($Z$-$\\text{NCP}$-Object):</p>
<div class="equation-box">
$$\\sin a = \\sin \\phi \\sin \\delta + \\cos \\phi \\cos \\delta \\cos H$$
$$\\cos A = \\frac{\\sin \\delta - \\sin \\phi \\sin a}{\\cos \\phi \\cos a}$$
$$\\sin A = -\\frac{\\cos \\delta \\sin H}{\\cos a}$$
</div>
<p>where $\\phi$ is the observer's geographic latitude.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 1.1: 3D Celestial Sphere & Coordinate Converter</h4>
  </div>
  <p>Rotate the celestial sphere, adjust the observer's terrestrial latitude, and watch real-time diurnal motion with live conversion between horizontal ($a, A$) and equatorial ($\\alpha, \\delta$) coordinates.</p>
  <div id="astro-celestial-sphere-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-1-3",
            "title": "Precession, Nutation & Stellar Space Velocity Kinematics",
            "content": """
<p>Because the Earth is an oblate spheroid experiencing non-uniform gravitational torques from the Moon and the Sun, the Earth's rotational axis does not point in a constant direction in inertial space. Furthermore, individual stars are not stationary on the celestial sphere, exhibiting measurable intrinsic space motions.</p>

<h4>Precession of the Equinoxes and Nutation</h4>
<p>The gravitational torque exerted by the Moon and Sun on the Earth's equatorial bulge causes the Earth's spin axis to gyroscopically precess around the normal to the ecliptic plane with a period of:</p>
<div class="equation-box">
$$P_{\\text{prec}} \\approx 25{,}772\\text{ years}$$
</div>
<p>This <em>general precession</em> causes the vernal equinox $\\Upsilon$ to drift westward along the ecliptic at a rate of:</p>
<div class="equation-box">
$$\\dot{\\psi} = 50.29''\\text{ per year} = 1^\\circ\\text{ every } 71.6\\text{ years}$$
</div>
<p>Because $\\Upsilon$ defines the zero-point of Right Ascension and the celestial equator changes orientation, both $\\alpha$ and $\\delta$ of every star continuously drift with time. Catalogs must therefore cite an explicit <strong>standard equinox epoch</strong> (e.g., J2000.0, corresponding to 2000 January 1.5 TT). Superimposed on this smooth precession is <em>nutation</em>, a periodic nodding of the rotational axis with an amplitude of $9.2''$ and a primary period of $18.6$ years caused by the regression of the lunar orbital nodes.</p>

<h4>Stellar Space Velocity Decomposition</h4>
<p>The 3D space velocity vector $\\vec{v}$ of a star relative to the Sun decomposes into two mutually perpendicular components: the radial velocity $v_r$ along the line of sight and the transverse velocity $v_t$ perpendicular to the line of sight across the sky plane:</p>
<div class="equation-box">
$$v = |\\vec{v}| = \\sqrt{v_r^2 + v_t^2}$$
</div>

<h4>1. Radial Velocity ($v_r$)</h4>
<p>Measured directly via the non-relativistic spectroscopic Doppler shift of stellar absorption lines:</p>
<div class="equation-box">
$$z = \\frac{\\lambda_{\\text{obs}} - \\lambda_0}{\\lambda_0} = \\frac{\\Delta \\lambda}{\\lambda_0} = \\frac{v_r}{c} \\quad (v_r \\ll c)$$
</div>
<p>Positive $v_r$ signifies redshift (recession away from the Sun), while negative $v_r$ signifies blueshift (approach).</p>

<h4>2. Transverse Velocity ($v_t$) and Proper Motion ($\\mu$)</h4>
<p>The angular displacement of a star across the celestial sphere per unit time is its <strong>proper motion</strong> $\\mu$, measured in arcseconds per year ($''/\\text{yr}$). If a star lies at distance $d$ (in parsecs) and exhibits proper motion $\\mu$ (in $''/\\text{yr}$), its physical linear transverse velocity is:</p>
<div class="equation-box">
$$v_t = d \\frac{d\\theta}{dt} = d \\left(\\mu \\times \\frac{\\pi}{180 \\times 3600}\\right) \\frac{1}{3.15576 \\times 10^7\\text{ s}}$$
$$v_t \\approx 4.74047 \\left(\\frac{\\mu}{''/\\text{yr}}\\right) \\left(\\frac{d}{\\text{pc}}\\right) \\text{ km s}^{-1}$$
</div>
<p>The numerical coefficient $4.74047 \\approx \\frac{1\\text{ AU}}{1\\text{ year}}$ in $\\text{km/s}$ naturally links angular motion to linear velocities.</p>
"""
        },
        {
            "id": "sec-1-4",
            "title": "Scales of the Universe: Metric Foundations & Astronomical Units",
            "content": """
<p>Astrophysical systems span over 40 orders of magnitude in spatial dimension. To navigate these scales without unwieldy powers of ten, the International Astronomical Union (IAU) standardizes specialized metrological units anchored to solar system and stellar physics.</p>

<h4>The Fundamental Distance Units</h4>
<ul>
  <li><strong>The Astronomical Unit (AU):</strong> Formally defined by the IAU (2012) as an exact constant representing the mean Earth-Sun orbital separation:
  <div class="equation-box">
  $$1\\text{ AU} \\equiv 149{,}597{,}870{,}700\\text{ meters} \\approx 1.496 \\times 10^{11}\\text{ m} = 1.496 \\times 10^8\\text{ km}$$
  </div>
  Light travels 1 AU in $t = \\frac{1\\text{ AU}}{c} = 499.005\\text{ s} \\approx 8.317\\text{ minutes}$.</li>
  <li><strong>The Light-Year (ly):</strong> The distance traveled by a photon in a vacuum during one Julian year ($365.25\\text{ days} = 31{,}557{,}600\\text{ s}$):
  <div class="equation-box">
  $$1\\text{ ly} = c \\times 1\\text{ yr} = (2.99792458 \\times 10^8\\text{ m/s})(31{,}557{,}600\\text{ s}) = 9.46073 \\times 10^{15}\\text{ m} \\approx 63{,}241\\text{ AU}$$
  </div>
  </li>
  <li><strong>The Parsec (pc):</strong> The primary distance unit in professional stellar and galactic astronomy, defined as the distance at which an astronomical baseline of $1\\text{ AU}$ subtends an angle of exactly one arcsecond ($1'' = 1/3600^\\circ$):
  <div class="equation-box">
  $$1\\text{ pc} = \\frac{1\\text{ AU}}{\\tan(1'')} \\approx \\frac{1\\text{ AU}}{1'' \\text{ in rad}} = \\frac{1.4959787 \\times 10^{11}\\text{ m}}{(1/3600) \\times (\\pi/180)} = 3.08567758 \\times 10^{16}\\text{ m}$$
  $$1\\text{ pc} \\approx 3.26156\\text{ ly} \\approx 206{,}265\\text{ AU}$$
  </div>
  Larger cosmological scales are expressed in kiloparsecs ($1\\text{ kpc} = 10^3\\text{ pc}$), megaparsecs ($1\\text{ Mpc} = 10^6\\text{ pc}$), and gigaparsecs ($1\\text{ Gpc} = 10^9\\text{ pc}$).</li>
</ul>

<h4>Hierarchy of Cosmic Scales</h4>
<table class="data-table">
  <thead>
    <tr><th>Structure / Domain</th><th>Typical Dimension</th><th>SI Scale (m)</th></tr>
  </thead>
  <tbody>
    <tr><td>Solar Radius ($R_\\odot$)</td><td>$696{,}340\\text{ km}$</td><td>$6.96 \\times 10^8$</td></tr>
    <tr><td>Earth-Sun Distance</td><td>$1.0\\text{ AU}$</td><td>$1.50 \\times 10^{11}$</td></tr>
    <tr><td>Kuiper Belt Outer Edge</td><td>$\\sim 50\\text{ AU}$</td><td>$7.5 \\times 10^{12}$</td></tr>
    <tr><td>Oort Cloud Outer Boundary</td><td>$\\sim 50{,}000-100{,}000\\text{ AU}$</td><td>$\\sim 1-1.5 \\times 10^{16}$</td></tr>
    <tr><td>Distance to Proxima Centauri</td><td>$1.30\\text{ pc} = 4.24\\text{ ly}$</td><td>$4.01 \\times 10^{16}$</td></tr>
    <tr><td>Milky Way Stellar Disk Diameter</td><td>$\\approx 30\\text{ kpc}$</td><td>$9.26 \\times 10^{20}$</td></tr>
    <tr><td>Distance to Andromeda Galaxy (M31)</td><td>$\\approx 778\\text{ kpc} = 2.54\\text{ Mly}$</td><td>$2.40 \\times 10^{22}$</td></tr>
    <tr><td>Virgo Galaxy Cluster Distance</td><td>$\\approx 16.5\\text{ Mpc}$</td><td>$5.09 \\times 10^{23}$</td></tr>
    <tr><td>Hubble Horizon ($c/H_0$)</td><td>$\\approx 4.3\\text{ Gpc} \\approx 14.0\\text{ Gly}$</td><td>$1.33 \\times 10^{26}$</td></tr>
    <tr><td>Observable Universe Radius</td><td>$\\approx 14.3\\text{ Gpc} \\approx 46.5\\text{ Gly}$</td><td>$4.41 \\times 10^{26}$</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sec-1-5",
            "title": "Telescope Optics, Atmospheric Seeing & Detectors",
            "content": """
<p>Telescopes function primarily as photon buckets to maximize light gathering power, and secondarily as angular magnification instruments. The performance of any astronomical telescope is governed by wave optics, geometrical optics, and atmospheric turbulence.</p>

<h4>Light-Gathering Power and Plate Scale</h4>
<p>The light-gathering power (LGP) of an aperture of diameter $D$ scales with the collecting area:</p>
<div class="equation-box">
$$\\text{LGP} \\propto D^2$$
</div>
<p>A $10\\text{ m}$ telescope collects $(10 / 0.007)^2 \\approx 2 \\times 10^6$ times more photons per second than the human eye pupil ($d_{\\text{eye}} \\approx 7\\text{ mm}$).</p>
<p>The physical linear dimension $y$ on the detector plane corresponding to an angular separation $\\theta$ (in radians) on the sky produced by an objective of focal length $f$ is $y = f \\theta$. The <strong>plate scale</strong> $s$ quantifies angular separation per unit physical distance:</p>
<div class="equation-box">
$$s = \\frac{d\\theta}{dy} = \\frac{1}{f} \\text{ rad/m} = \\frac{206{,}265}{f\\text{ (mm)}} \\text{ arcsec mm}^{-1}$$
</div>

<h4>Diffraction Limit: The Airy Disk and Rayleigh Criterion</h4>
<p>Due to Fraunhofer wave diffraction through a circular aperture of diameter $D$, a distant point source produces a diffraction pattern known as the Airy disk, with the first dark zero occurring at angular radius:</p>
<div class="equation-box">
$$\\theta_{\\text{Airy}} = 1.21966 \\frac{\\lambda}{D} \\text{ radians} \\approx 251{,}643 \\left(\\frac{\\lambda}{D}\\right) \\text{ arcseconds}$$
</div>
<p>For optical observations at $\\lambda = 550\\text{ nm}$ ($V$-band) with an aperture $D$ in meters:</p>
<div class="equation-box">
$$\\theta_{\\text{diff}} \\approx 0.138'' \\left(\\frac{1\\text{ m}}{D}\\right)$$
</div>

<h4>Atmospheric Seeing & Adaptive Optics (AO)</h4>
<p>Ground-based telescopes rarely achieve their diffraction limit in visible light due to turbulent thermal eddies in Earth's atmosphere, which introduce rapid spatio-temporal phase fluctuations into incoming planar wavefronts. This turbulence is characterized by Fried's coherence parameter $r_0$ (typically $10-20\\text{ cm}$ at good astronomical sites like Mauna Kea or Paranal). The effective angular resolution without correction is set by the <strong>seeing disk</strong>:</p>
<div class="equation-box">
$$\\theta_{\\text{seeing}} \\approx \\frac{\\lambda}{r_0} \\sim 0.5'' - 1.5''$$
</div>
<p><strong>Adaptive Optics (AO)</strong> systems bypass this barrier in real time: a Shack-Hartmann wavefront sensor samples phase aberrations hundreds of times per second (using a natural guide star or a sodium laser guide star exciting mesospheric sodium atoms at $90\\text{ km}$ altitude) and applies conjugate phase deformations via a piezoelectric deformable mirror, restoring the diffraction-limited Airy pattern and dramatically boosting the Strehl ratio.</p>

<h4>Astronomical Detectors: CCDs and Signal-to-Noise Ratio</h4>
<p>Modern Charge-Coupled Devices (CCDs) and CMOS sensors convert incident photons into photoelectrons with Quantum Efficiency $\\text{QE} \\approx 80-95\\%$ (compared to photographic plates at $\\sim 1\\%$). The signal-to-noise ratio (SNR) of an observation with source photon count rate $S$, sky background rate $B$, dark current rate $D$, readout noise $\\sigma_R$, exposure time $t$, and $n_{\\text{pix}}$ pixels is given by the CCD equation:</p>
<div class="equation-box">
$$\\text{SNR} = \\frac{S t}{\\sqrt{S t + n_{\\text{pix}}(B + D)t + n_{\\text{pix}} \\sigma_R^2}}$$
</div>
"""
        },
        {
            "id": "sec-1-6",
            "title": "The Cosmic Distance Ladder: Parallax & The Leavitt Law",
            "content": """
<p>No single astronomical measurement technique spans all cosmic scales. Astronomers construct a succession of overlapping methodologies—the <strong>cosmic distance ladder</strong>—where each rung is calibrated by the preceding one.</p>

<h4>Rung 1: Trigonometric Parallax</h4>
<p>Trigonometric parallax represents the only direct, purely geometric distance measurement method in astronomy. As the Earth orbits the Sun, a nearby star exhibits an apparent annual elliptical reflex shift against distant background quasars. The <strong>parallax angle</strong> $p$ is defined as half the maximum apparent angular displacement:</p>
<div class="equation-box">
$$\\tan p = \\frac{1\\text{ AU}}{d} \\implies d = \\frac{1\\text{ AU}}{\\sin p} \\approx \\frac{1\\text{ AU}}{p \\text{ (rad)}} = \\frac{1}{p \\text{ (arcsec)}} \\text{ pc}$$
</div>
<p>The space astrometry mission <em>Gaia</em> measures parallaxes with precision $\\sigma_p \\sim 10-20\\ \\mu\\text{as}$, delivering direct geometric distances out to several kiloparsecs.</p>

<h4>Rung 2: Moving Cluster Method (Convergent Point)</h4>
<p>For open star clusters (such as the Hyades) whose stars share a common space velocity vector $\\vec{v}$, perspective causes their proper motions $\\mu$ to converge toward a single point on the celestial sphere. Measuring the angular distance $\\theta$ between a star and the convergent point connects radial velocity $v_r$ to transverse velocity $v_t$:</p>
<div class="equation-box">
$$v_r = v \\cos\\theta, \\quad v_t = v \\sin\\theta = v_r \\tan\\theta$$
$$d = \\frac{v_t}{4.74 \\mu} = \\frac{v_r \\tan\\theta}{4.74 \\mu} \\text{ pc}$$
</div>
<p>This provides an absolute physical calibration of the cluster's distance without trigonometric parallax.</p>

<h4>Rung 3: Standard Candles & Distance Modulus</h4>
<p>A <strong>standard candle</strong> is an astronomical source whose intrinsic absolute luminosity $L$ (or absolute magnitude $M$) is reliably known through physical law or empirical calibration. The distance modulus $\\mu$ relates apparent magnitude $m$, absolute magnitude $M$, physical distance $d$ (in parsecs), and interstellar extinction $A_V$:</p>
<div class="equation-box">
$$\\mu \\equiv m - M = 5\\log_{10}\\left(\\frac{d}{10\\text{ pc}}\\right) + A_V = 5\\log_{10}(d) - 5 + A_V$$
$$d = 10^{\\frac{m - M + 5 - A_V}{5}} \\text{ pc}$$
</div>

<h4>Rung 4: The Cepheid Leavitt Law</h4>
<p>Discovered by Henrietta Leavitt in 1912, Classical Cepheid pulsating variable stars exhibit an exceptionally tight empirical relation between their pulsation period $P$ (driven by the $\\kappa$-mechanism in the helium ionization zone) and their mean absolute visual or infrared magnitude:</p>
<div class="equation-box">
$$M_V \\approx -2.78 \\log_{10}(P / \\text{days}) - 1.35$$
$$M_K \\approx -3.26 \\log_{10}(P / \\text{days}) - 2.40$$
</div>
<p>Because infrared $K$-band observations are far less susceptible to dust extinction ($A_K \\approx 0.1 A_V$), infrared Cepheid measurements by the Hubble Space Telescope and JWST accurately determine distances out to $\\sim 30-40\\text{ Mpc}$, bridging galactic scales to the realm of Type Ia supernovae.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 1.2: Stellar Parallax & Cepheid Leavitt Law Calculator</h4>
  </div>
  <p>Dynamically alter the baseline orbital radius and observer parallax angle $p$ to trace the geometric parallax triangle, while exploring the empirical Cepheid period-luminosity curve to calculate distance moduli.</p>
  <div id="astro-distance-ladder-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-1-7",
            "title": "Inventory & Physical Scales of the Observable Universe",
            "content": """
<p>Synthesizing observational data from the Cosmic Microwave Background (Planck), high-redshift Type Ia supernovae, and large-scale galaxy surveys reveals the energy-density budget and structural contents of our Universe.</p>

<h4>The Cosmic Energy-Density Inventory</h4>
<p>According to the standard $\\Lambda\\text{CDM}$ cosmological model, the total critical energy density today is $\\rho_{c,0} = \\frac{3 H_0^2}{8\\pi G} \\approx 8.5 \\times 10^{-27}\\text{ kg m}^{-3} \\approx 4.8\\text{ protons m}^{-3}$. The fractional contributions $\\Omega_i = \\rho_{i,0}/\\rho_{c,0}$ partition as follows:</p>
<div class="equation-box">
$$\\Omega_{\\Lambda} \\approx 0.685 \\pm 0.007 \\quad (\\text{Dark Energy / Cosmological Constant})$$
$$\\Omega_{c} \\approx 0.266 \\pm 0.007 \\quad (\\text{Cold Dark Matter - non-baryonic})$$
$$\\Omega_{b} \\approx 0.049 \\pm 0.001 \\quad (\\text{Baryonic Matter - atoms, gas, stars})$$
$$\\Omega_{\\gamma} \\approx 5.4 \\times 10^{-5} \\quad (\\text{Relativistic Photons / CMB})$$
$$\\Omega_{\\nu} \\approx 3.4 \\times 10^{-3} \\quad (\\text{Relic Neutrinos})$$
$$\\Omega_{\\text{tot}} = \\Omega_{\\Lambda} + \\Omega_{m} + \\Omega_r = 1.000 \\pm 0.002 \\quad (\\text{Spatially Flat Flatness})$$
</div>

<h4>Baryonic Census in the Modern Universe</h4>
<p>Within the tiny $4.9\\%$ slice of baryonic matter:</p>
<ul>
  <li>Stars, stellar remnants, and planets constitute merely $\\sim 6-7\\%$ of all baryons ($< 0.3\\%$ of total cosmic energy).</li>
  <li>Cold interstellar and circumgalactic gas in galaxies comprises $\\sim 10-15\\%$.</li>
  <li>The Warm-Hot Intergalactic Medium (WHIM) and hot intra-cluster plasma ($T \\sim 10^5-10^8\\text{ K}$) host the overwhelming majority ($\\sim 80\\%$) of baryonic atoms.</li>
</ul>

<h4>The Scale Factor and Horizon Limits</h4>
<p>The observable universe is circumscribed by the <strong>particle horizon</strong>—the maximum distance from which light could have traveled to us since the Big Bang ($t_0 \\approx 13.79\\text{ Gyr}$ ago). Because the fabric of space has expanded by a factor of $(1+z)$ during this transit, the comoving radius of the observable universe today is not $c t_0 = 13.8\\text{ Gly}$, but rather:</p>
<div class="equation-box">
$$R_{\\text{obs}} = \\int_0^{t_0} \\frac{c\\,dt}{a(t)} = c \\int_0^{\\infty} \\frac{dz}{H(z)} \\approx 14.3\\text{ Gpc} \\approx 46.5\\text{ billion light-years}$$
</div>
<p>The total volume of the observable universe is thus $V_{\\text{obs}} = \\frac{4}{3}\\pi R_{\\text{obs}}^3 \\approx 3.58 \\times 10^{80}\\text{ m}^3$, containing roughly $2 \\times 10^{12}$ galaxies and $\\sim 10^{80}$ baryonic particles (mostly hydrogen and helium nuclei).</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-1-1",
            "title": "Space Velocity & 3D Kinematic Vector from Gaia Astrometric Data",
            "statement": "A nearby Population I star observed by the Gaia satellite has a measured trigonometric parallax $p = 42.50 \\pm 0.15\\ \\text{mas}$ (milliarcseconds), a proper motion in Right Ascension $\\mu_\\alpha \\cos\\delta = -185.4\\ \\text{mas/yr}$, a proper motion in Declination $\\mu_\\delta = +94.2\\ \\text{mas/yr}$, and a high-resolution spectroscopic radial velocity $v_r = -34.8\\ \\text{km s}^{-1}$.\\n\\n(a) Compute the star's distance $d$ in parsecs and light-years.\\n(b) Determine the star's total proper motion $\\mu$ and its transverse velocity $v_t$ in $\\text{km s}^{-1}$.\\n(c) Calculate the magnitude of the full 3D space velocity vector $v$ and its trajectory angle relative to the line of sight.",
            "solution": """
<h4>(a) Distance Calculation</h4>
<p>The trigonometric parallax is $p = 42.50\\text{ mas} = 0.04250''$. The distance is:</p>
<div class="equation-box">
$$d = \\frac{1}{p} = \\frac{1}{0.04250} \\approx 23.5294\\text{ pc}$$
</div>
<p>Converting to light-years ($1\\text{ pc} = 3.26156\\text{ ly}$):</p>
<div class="equation-box">
$$d = 23.5294 \\times 3.26156 \\approx 76.74\\text{ ly}$$
</div>

<h4>(b) Total Proper Motion & Transverse Velocity</h4>
<p>The total proper motion $\\mu$ across the celestial sphere is the Pythagorean sum of its orthogonal vector components:</p>
<div class="equation-box">
$$\\mu = \\sqrt{(\\mu_\\alpha \\cos\\delta)^2 + \\mu_\\delta^2} = \\sqrt{(-185.4)^2 + (94.2)^2} = \\sqrt{34373.16 + 8873.64} = \\sqrt{43246.8} \\approx 207.96\\text{ mas/yr} = 0.20796''/\\text{yr}$$
</div>
<p>The linear transverse velocity $v_t$ is obtained via $v_t = 4.74047 \\mu d$:</p>
<div class="equation-box">
$$v_t = 4.74047 \\times 0.20796 \\times 23.5294 \\approx 23.20\\text{ km s}^{-1}$$
</div>

<h4>(c) Full 3D Space Velocity & Motion Angle</h4>
<p>The magnitude of the space velocity vector $\\vec{v}$ is:</p>
<div class="equation-box">
$$v = \\sqrt{v_r^2 + v_t^2} = \\sqrt{(-34.8)^2 + (23.20)^2} = \\sqrt{1211.04 + 538.24} = \\sqrt{1749.28} \\approx 41.82\\text{ km s}^{-1}$$
</div>
<p>The angle $\\theta$ between the velocity vector and the line of sight (where $\\theta = 0^\\circ$ indicates radial motion away and $\\theta = 180^\\circ$ indicates radial approach) is:</p>
<div class="equation-box">
$$\\tan\\theta = \\frac{v_t}{|v_r|} = \\frac{23.20}{34.8} \\approx 0.6667 \\implies \\theta = 180^\\circ - \\arctan(0.6667) \\approx 180^\\circ - 33.69^\\circ = 146.31^\\circ$$
</div>
<p>The star is closing in toward the solar neighborhood at $41.82\\text{ km s}^{-1}$, tilted $33.69^\\circ$ away from pure radial approach.</p>
"""
        },
        {
            "id": "prob-1-2",
            "title": "Diffraction Limits, Plate Scales & Seeing in Large Optical Telescopes",
            "statement": "An $8.2\\text{-meter}$ diameter Ritchey-Chrétien telescope operating at the summit of Cerro Paranal has an effective focal ratio $f/15$ and observes at visual wavelength $\\lambda = 500\\text{ nm}$. Atmospheric seeing at the site is $\\theta_{\\text{see}} = 0.65''$.\\n\\n(a) Calculate the theoretical diffraction-limited angular resolution $\\theta_{\\text{diff}}$ in arcseconds.\\n(b) Determine the effective focal length $f$ and plate scale $s$ in $\\text{arcsec mm}^{-1}$.\\n(c) Find the physical diameter of the seeing disk on a CCD placed at the Cassegrain focus.\\n(d) If an adaptive optics system corrects the wavefront aberrations to achieve the diffraction limit, what is the factor of improvement in peak image intensity (Strehl ratio enhancement)?",
            "solution": """
<h4>(a) Theoretical Diffraction Limit</h4>
<p>By the Rayleigh criterion for a circular aperture of diameter $D = 8.2\\text{ m}$ at $\\lambda = 500\\text{ nm} = 5.0 \\times 10^{-7}\\text{ m}$:</p>
<div class="equation-box">
$$\\theta_{\\text{diff}} = 1.22 \\frac{\\lambda}{D} = 1.22 \\times \\frac{5.0 \\times 10^{-7}\\text{ m}}{8.2\\text{ m}} \\approx 7.439 \\times 10^{-8}\\text{ radians}$$
</div>
<p>Converting to arcseconds ($1\\text{ rad} = 206{,}265''$):</p>
<div class="equation-box">
$$\\theta_{\\text{diff}} = 7.439 \\times 10^{-8} \\times 206{,}265 \\approx 0.0153''$$
</div>

<h4>(b) Focal Length and Plate Scale</h4>
<p>With focal ratio $N = f/D = 15$, the focal length is:</p>
<div class="equation-box">
$$f = 15 \\times 8.2\\text{ m} = 123.0\\text{ meters} = 123{,}000\\text{ mm}$$
</div>
<p>The plate scale $s$ is:</p>
<div class="equation-box">
$$s = \\frac{206{,}265}{f\\text{ (mm)}} = \\frac{206{,}265}{123{,}000} \\approx 1.677\\text{ arcsec mm}^{-1}$$
</div>

<h4>(c) Physical Diameter of Seeing Disk on CCD</h4>
<p>The seeing disk angular width is $\\theta_{\\text{see}} = 0.65''$. Its physical diameter on the detector plane is:</p>
<div class="equation-box">
$$d_{\\text{spot}} = \\frac{\\theta_{\\text{see}}}{s} = \\frac{0.65''}{1.677''/\\text{mm}} \\approx 0.3876\\text{ mm} = 387.6\\ \\mu\\text{m}$$
</div>
<p>On a CCD with $15\\ \\mu\\text{m}$ pixels, the seeing disk spans $\\approx 26$ pixels across.</p>

<h4>(d) Adaptive Optics Resolution & Peak Intensity Gain</h4>
<p>The angular resolution improves by the ratio:</p>
<div class="equation-box">
$$\\frac{\\theta_{\\text{see}}}{\\theta_{\\text{diff}}} = \\frac{0.65''}{0.0153''} \\approx 42.5\\text{ times}$$
</div>
<p>Because the collected photon flux is concentrated from an uncorrected seeing area $A_{\\text{see}} \\propto \\theta_{\\text{see}}^2$ into a diffraction-limited Airy core $A_{\\text{diff}} \\propto \\theta_{\\text{diff}}^2$, the peak central surface brightness increases by roughly:</p>
<div class="equation-box">
$$\\left(\\frac{\\theta_{\\text{see}}}{\\theta_{\\text{diff}}}\\right)^2 \\approx (42.5)^2 \\approx 1{,}805\\text{ times}$$
</div>
<p>This massive boost in signal-to-noise enables detecting point sources over 8 magnitudes fainter.</p>
"""
        },
        {
            "id": "prob-1-3",
            "title": "Cepheid Variable Period-Luminosity Distance & Interstellar Extinction",
            "statement": "A Classical Cepheid variable star located in a spiral arm of the galaxy NGC 4536 is monitored with the Hubble Space Telescope. Photometric observations yield a pulsation period $P = 38.60\\text{ days}$, a time-averaged apparent visual magnitude $\\langle m_V \\rangle = 22.45$, and an apparent blue magnitude $\\langle m_B \\rangle = 23.35$.\\n\\n(a) Compute the star's absolute visual magnitude $M_V$ using the empirical Leavitt Law $M_V = -2.76\\log_{10}(P/\\text{days}) - 1.40$.\\n(b) The intrinsic unreddened color index for this Cepheid period is known to be $(B-V)_0 = 0.52$. Determine the color excess $E(B-V)$ and total visual extinction $A_V$ assuming standard interstellar dust with $R_V = 3.1$.\\n(c) Calculate the true extinction-corrected distance modulus $\\mu_0$ and the distance $d$ to NGC 4536 in megaparsecs.",
            "solution": """
<h4>(a) Absolute Magnitude from Leavitt Law</h4>
<p>With $P = 38.60\\text{ days}$:</p>
<div class="equation-box">
$$\\log_{10}(P) = \\log_{10}(38.60) \\approx 1.5866$$
$$M_V = -2.76 \\times 1.5866 - 1.40 = -4.379 - 1.40 = -5.779$$
</div>

<h4>(b) Color Excess & Interstellar Extinction</h4>
<p>The observed color index is:</p>
<div class="equation-box">
$$(B - V)_{\\text{obs}} = \\langle m_B \\rangle - \\langle m_V \\rangle = 23.35 - 22.45 = 0.90$$
</div>
<p>The color excess (reddening) is:</p>
<div class="equation-box">
$$E(B - V) = (B - V)_{\\text{obs}} - (B - V)_0 = 0.90 - 0.52 = 0.38\\text{ magnitudes}$$
</div>
<p>With standard dust extinction ratio $R_V = \\frac{A_V}{E(B-V)} = 3.1$:</p>
<div class="equation-box">
$$A_V = R_V \\times E(B - V) = 3.1 \\times 0.38 = 1.178\\text{ magnitudes}$$
</div>

<h4>(c) Distance Modulus & Metric Distance</h4>
<p>The true, extinction-corrected distance modulus $\\mu_0$ is:</p>
<div class="equation-box">
$$\\mu_0 = m_V - M_V - A_V = 22.45 - (-5.779) - 1.178 = 28.229 - 1.178 = 27.051\\text{ magnitudes}$$
</div>
<p>Using the distance modulus equation $\\mu_0 = 5\\log_{10}(d/\\text{pc}) - 5$:</p>
<div class="equation-box">
$$5\\log_{10}(d) = \\mu_0 + 5 = 27.051 + 5 = 32.051 \\implies \\log_{10}(d) = 6.4102$$
$$d = 10^{6.4102} \\approx 2{,}571{,}500\\text{ pc} = 2.57\\text{ Mpc}$$
</div>
<p>NGC 4536 is located at an extinction-corrected distance of $2.57\\text{ Mpc}$ (or $8.38\\text{ Mly}$).</p>
"""
        }
    ]
}

u2 = {
    "unitId": 2,
    "title": "The Sun, Stellar Interiors & Nuclear Energy Generation",
    "subtitle": "Standard Solar Model, Hydrostatic Equilibrium, Thermonuclear p-p/CNO Cycles & Exoplanet Dynamics",
    "icon": "☀️",
    "summary": "This unit investigates the physics of our closest star, the Sun, and generalizes its internal mechanics to all main-sequence stellar structures. We begin with solar system surveys and planetary dynamics, deriving Kepler's laws from Newtonian gravity and analyzing exoplanet detection via Doppler radial velocities and transit light curves. We formulate the fundamental equations of stellar structure: hydrostatic equilibrium, mass continuity, radiative and convective energy transport, and the Virial Theorem. We probe the microscopic quantum mechanics of thermonuclear fusion, solving the Gamow peak penetration integral for the proton-proton chain and CNO catalytic cycle. Finally, we explore the solar atmosphere, coronal heating, solar wind kinematics, and helioseismology as an empirical tomographic probe of stellar cores.",
    "keyTakeaways": [
        "Planetary orbits obey Kepler's laws derived from central force mechanics, enabling precise mass and radius characterization of extrasolar planets via spectroscopic Doppler radial velocity amplitudes $K$ and photometric transit dips $\\Delta F/F = (R_p/R_*)^2$.",
        "A star in mechanical equilibrium balances inward gravitational attraction against outward gas and radiation pressure gradients via the hydrostatic equation $\\frac{dP}{dr} = -\\frac{G M(r)\\rho(r)}{r^2}$.",
        "The Virial Theorem dictates that for self-gravitating ideal gas spheres, total energy is $E = \\frac{1}{2}\\Omega = -K$. Thus, during gravitational contraction, half of the released gravitational potential energy radiates into space while the other half heats the stellar core.",
        "Energy generation in stellar cores occurs via quantum mechanical tunneling through the Coulomb barrier at the Gamow peak, dominated by the $p$-$p$ chain in low-mass stars ($M \\lesssim 1.3 M_\\odot$) and the temperature-sensitive CNO cycle in higher-mass stars.",
        "Energy transport transitions between radiative diffusion (governed by Rosseland mean opacity $\\kappa$) and convective instability whenever the radiative temperature gradient exceeds the adiabatic gradient (Schwarzschild criterion)."
    ],
    "sections": [
        {
            "id": "sec-2-1",
            "title": "Global Architecture & Surveying the Solar System",
            "content": """
<p>The Sun is a middle-aged, G2V spectral dwarf star containing $99.86\\%$ of the total mass of the Solar System. Understanding its physical parameters provides the canonical baseline ('solar units') against which all other stars are measured.</p>

<h4>Global Solar Parameters</h4>
<table class="data-table">
  <thead>
    <tr><th>Parameter</th><th>Symbol</th><th>Measured Value (SI)</th><th>Astrophysical Significance</th></tr>
  </thead>
  <tbody>
    <tr><td>Solar Mass</td><td>$M_\\odot$</td><td>$1.98847 \\times 10^{30}\\text{ kg}$</td><td>Determined via Kepler's 3rd law applied to planetary orbits</td></tr>
    <tr><td>Solar Radius</td><td>$R_\\odot$</td><td>$6.957 \\times 10^8\\text{ m} = 695{,}700\\text{ km}$</td><td>$109.2$ times the Earth's volumetric mean radius</td></tr>
    <tr><td>Solar Luminosity</td><td>$L_\\odot$</td><td>$3.828 \\times 10^{26}\\text{ W} = 3.828 \\times 10^{33}\\text{ erg/s}$</td><td>Total radiant electromagnetic power output</td></tr>
    <tr><td>Effective Temperature</td><td>$T_{\\text{eff}}$</td><td>$5778\\text{ K}$</td><td>Defined via $L_\\odot = 4\\pi R_\\odot^2 \\sigma T_{\\text{eff}}^4$</td></tr>
    <tr><td>Solar Constant</td><td>$S_0$</td><td>$1361\\text{ W m}^{-2}$</td><td>Integrated solar radiant flux at $1\\text{ AU}$ outside Earth's atmosphere</td></tr>
    <tr><td>Central Temperature</td><td>$T_c$</td><td>$1.57 \\times 10^7\\text{ K}$</td><td>Standard Solar Model core condition for $p$-$p$ ignition</td></tr>
    <tr><td>Central Density</td><td>$\\rho_c$</td><td>$1.52 \\times 10^5\\text{ kg m}^{-3} = 152\\text{ g cm}^{-3}$</td><td>$\\approx 13$ times denser than solid lead</td></tr>
    <tr><td>Mean Density</td><td>$\\bar{\\rho}$</td><td>$1408\\text{ kg m}^{-3} = 1.408\\text{ g cm}^{-3}$</td><td>Slightly denser than liquid water</td></tr>
  </tbody>
</table>

<h4>Solar Composition by Mass</h4>
<p>Spectroscopic abundance analyses and helioseismic inversions establish the initial zero-age solar composition as:</p>
<div class="equation-box">
$$X = 0.7381 \\quad (\\text{Hydrogen}), \\quad Y = 0.2485 \\quad (\\text{Helium}), \\quad Z = 0.0134 \\quad (\\text{Metals: elements heavier than He})$$
</div>
<p>Due to $4.57\\text{ Gyr}$ of nuclear burning, the modern core has burned hydrogen into helium, shifting its central abundances to $X_c \\approx 0.34$, $Y_c \\approx 0.64$.</p>
"""
        },
        {
            "id": "sec-2-2",
            "title": "Planetary Orbital Dynamics & Derivation of Kepler's Laws",
            "content": """
<p>Johannes Kepler formulated three empirical laws of planetary motion based on Tycho Brahe's precision observational data. Isaac Newton later derived these laws from first principles using universal gravitation and Newtonian mechanics in a reduced two-body framework.</p>

<h4>1. Kepler's First Law (The Law of Ellipses)</h4>
<p><em>Every planet moves in an elliptical orbit with the Sun situated at one of the two foci.</em></p>
<p>In polar coordinates $(r, \\theta)$ centered on the Sun, the equation of an ellipse is:</p>
<div class="equation-box">
$$r(\\theta) = \\frac{p}{1 + e \\cos\\theta} = \\frac{a(1 - e^2)}{1 + e \\cos\\theta}$$
</div>
<p>where $a$ is the semi-major axis, $e$ is the orbital eccentricity ($0 \\le e < 1$), $\\theta$ is the true anomaly (angle from perihelion), and $p = a(1-e^2)$ is the semi-latus rectum. The perihelion distance is $r_p = a(1-e)$ and the aphelion distance is $r_a = a(1+e)$.</p>

<h4>2. Kepler's Second Law (The Law of Equal Areas)</h4>
<p><em>A line joining a planet and the Sun sweeps out equal areas during equal intervals of time.</em></p>
<p>This is a direct mathematical consequence of the conservation of orbital angular momentum $\\vec{L}$ in a central force field:</p>
<div class="equation-box">
$$d\\vec{A} = \\frac{1}{2} \\vec{r} \\times d\\vec{r} \\implies \\frac{dA}{dt} = \\frac{1}{2} |\\vec{r} \\times \\vec{v}| = \\frac{L}{2\\mu} = \\text{constant}$$
</div>
<p>where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$ is the reduced mass. Thus, a planet travels fastest at perihelion ($v_p = \\sqrt{\\frac{GM}{a}\\frac{1+e}{1-e}}$) and slowest at aphelion ($v_a = \\sqrt{\\frac{GM}{a}\\frac{1-e}{1+e}}$).</p>

<h4>3. Kepler's Third Law (The Harmonic Law)</h4>
<p><em>The square of the orbital period $P$ of a planet is proportional to the cube of its semi-major axis $a$.</em></p>
<p>Integrating the areal velocity $\\frac{dA}{dt} = \\frac{L}{2\\mu}$ over one full orbital period $P$ yields the area of an ellipse $A = \\pi a b = \\pi a^2 \\sqrt{1-e^2}$:</p>
<div class="equation-box">
$$P = \\frac{2\\mu A}{L} = \\frac{2\\pi a^2 \\sqrt{1-e^2}}{L/\\mu}$$
</div>
<p>Substituting $L/\\mu = \\sqrt{G(M_1 + M_2)a(1-e^2)}$ yields Newton's generalized form of Kepler's 3rd Law:</p>
<div class="equation-box">
$$P^2 = \\frac{4\\pi^2}{G(M_1 + M_2)} a^3$$
</div>
<p>When mass is in solar masses ($M_\\odot$), period in Earth years ($\text{yr}$), and distance in Astronomical Units ($\text{AU}$), this simplifies to $P^2 = a^3 / (M_1 + M_2)$.</p>

<h4>The Vis-Viva Equation</h4>
<p>Conservation of total specific orbital mechanical energy $\\mathcal{E} = \\frac{1}{2}v^2 - \\frac{GM}{r} = -\\frac{GM}{2a}$ yields the fundamental <strong>vis-viva equation</strong> relating instantaneous orbital speed $v$ to radius $r$:</p>
<div class="equation-box">
$$v^2 = G M \\left(\\frac{2}{r} - \\frac{1}{a}\\right)$$
</div>
"""
        },
        {
            "id": "sec-2-3",
            "title": "Extrasolar Planets: Detection Physics, Transits & Radial Velocities",
            "content": """
<p>Since the 1995 discovery of 51 Pegasi b, the detection of exoplanets has transformed astronomy. Two dominant quantitative techniques account for the vast majority of discoveries: the spectroscopic radial velocity method and photometric transit observations.</p>

<h4>1. The Radial Velocity (Doppler Wobble) Method</h4>
<p>A planet of mass $m_p$ orbiting a host star of mass $M_*$ ($m_p \\ll M_*$) in an orbit inclined at angle $i$ relative to the sky plane causes the star to reflexively orbit the common center of mass. The observable line-of-sight radial velocity of the star varies sinusoidally:</p>
<div class="equation-box">
$$v_{r,*}(t) = \\gamma + K \\left[\\cos(\\omega + \\theta(t)) + e \\cos\\omega\\right]$$
</div>
<p>where $\\gamma$ is the systemic velocity and $K$ is the <strong>semi-amplitude of the radial velocity</strong>:</p>
<div class="equation-box">
$$K = \\left(\\frac{2\\pi G}{P}\\right)^{1/3} \\frac{m_p \\sin i}{(M_* + m_p)^{2/3}} \\frac{1}{\\sqrt{1 - e^2}}$$
</div>
<p>For a circular orbit ($e=0$) with $m_p \\ll M_*$:</p>
<div class="equation-box">
$$K \\approx 28.4\\text{ m s}^{-1} \\left(\\frac{m_p \\sin i}{M_{\\text{Jup}}}\\right) \\left(\\frac{M_*}{M_\\odot}\\right)^{-2/3} \\left(\\frac{P}{1\\text{ yr}}\\right)^{-1/3}$$
</div>
<p>Radial velocity observations directly determine the minimum planetary mass $m_p \\sin i$. For a Jupiter-mass planet at $1\\text{ AU}$ around a solar-type star, $K \\approx 28.4\\text{ m/s}$; for an Earth-mass planet at $1\\text{ AU}$, $K \\approx 8.9\\text{ cm/s}$, requiring extreme spectrometer precision (e.g., ESPRESSO, HARPS).</p>

<h4>2. Photometric Transit Method</h4>
<p>If the planetary orbital plane is oriented nearly edge-on ($i \\approx 90^\\circ$), the planet transits the stellar disk once per orbit. The geometric transit probability is:</p>
<div class="equation-box">
$$\\mathcal{P}_{\\text{transit}} = \\frac{R_* + R_p}{a} \\approx \\frac{R_*}{a}$$
</div>
<p>During transit, the fractional decrease in stellar flux (the <strong>transit depth</strong>) is directly proportional to the ratio of geometric surface areas:</p>
<div class="equation-box">
$$\\delta = \\frac{\\Delta F}{F_*} = \\left(\\frac{R_p}{R_*}\\right)^2$$
</div>
<p>For a Jupiter-sized planet ($R_p \\approx 0.1 R_\\odot$), $\\delta \\approx 1\\%$. For an Earth-sized planet ($R_p \\approx 0.009 R_\\odot$), $\\delta \\approx 8.4 \\times 10^{-5} \\approx 84\\text{ ppm}$ (parts per million), which space telescopes like <em>Kepler</em> and <em>TESS</em> routinely measure.</p>
<p>Combining radial velocity ($m_p \\sin i$ with $i$ determined from transit duration) and transit measurements ($R_p$) uniquely yields the planet's true mass, physical radius, and mean bulk density $\\bar{\\rho}_p = \\frac{m_p}{\\frac{4}{3}\\pi R_p^3}$, distinguishing rocky terrestrial worlds from water worlds, gas giants, and puffy planets.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 2.1: Exoplanet Transit Photometry & Radial Velocity Wobble</h4>
  </div>
  <p>Adjust planet radius, orbital period, inclination angle, and eccentricity to observe simultaneous live planetary transit light curve dips and stellar radial velocity Doppler oscillations.</p>
  <div id="astro-exoplanet-transit-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-2-4",
            "title": "Hydrostatic Equilibrium & The Stellar Virial Theorem",
            "content": """
<p>A star is a stable, self-gravitating plasma configuration. Its macroscopic structure is governed by an exact mechanical balance between inward gravitational force and outward thermal and radiation pressure gradients.</p>

<h4>Equation of Hydrostatic Equilibrium</h4>
<p>Consider an infinitesimal cylindrical fluid element of cross-sectional area $dA$, height $dr$, and density $\\rho(r)$ situated at radius $r$ inside a spherically symmetric star. The mass of the element is $dm = \\rho(r) dA dr$. The forces acting radially are:</p>
<ol>
  <li>Inward gravitational force: $dF_g = -\\frac{G M(r) dm}{r^2} = -\\frac{G M(r) \\rho(r) dA dr}{r^2}$</li>
  <li>Net outward pressure force: $dF_p = [P(r) - P(r + dr)] dA = -\\frac{dP}{dr} dr dA$</li>
</ol>
<p>Setting the sum of forces to zero ($dF_g + dF_p = 0$) and dividing by $dA dr$ gives the fundamental <strong>equation of hydrostatic equilibrium</strong>:</p>
<div class="equation-box">
$$\\frac{dP}{dr} = -\\frac{G M(r) \\rho(r)}{r^2}$$
</div>
<p>Paired with the <strong>mass conservation equation</strong>:</p>
<div class="equation-box">
$$\\frac{dM(r)}{dr} = 4\\pi r^2 \\rho(r)$$
</div>

<h4>Derivation of the Virial Theorem for Stars</h4>
<p>Multiply both sides of the hydrostatic equation by $4\\pi r^3 dr$ and integrate from the center ($r=0$) to the stellar surface ($r=R$):</p>
<div class="equation-box">
$$\\int_0^R 4\\pi r^3 \\frac{dP}{dr} dr = -\\int_0^R \\frac{G M(r) \\rho(r) 4\\pi r^2}{r} dr = -\\int_0^{M_*} \\frac{G M(r)}{r} dM(r)$$
</div>
<p>The right-hand side is precisely the total gravitational potential energy of the star: $\\Omega = -\\int_0^{M_*} \\frac{G M(r)}{r} dM(r) < 0$.</p>
<p>Integrating the left-hand side by parts:</p>
<div class="equation-box">
$$\\left[4\\pi r^3 P(r)\\right]_0^R - \\int_0^R 12\\pi r^2 P(r) dr = 0 - 3 \\int_0^R P(r) 4\\pi r^2 dr = -3 \\int_V P\\,dV$$
</div>
<p>Equating both sides: $3 \\int_V P\\,dV = -\\Omega$.</p>
<p>For a non-relativistic classical monoatomic ideal gas, the pressure is related to the thermal kinetic energy density $u_k$ by $P = \\frac{2}{3} u_k$. Therefore:</p>
<div class="equation-box">
$$3 \\int_V \\left(\\frac{2}{3} u_k\\right) dV = 2 K = -\\Omega \\implies 2K + \\Omega = 0$$
</div>

<h4>Thermodynamic Implications of the Virial Theorem</h4>
<p>The total mechanical energy of the star is:</p>
<div class="equation-box">
$$E = K + \\Omega = -K = \\frac{1}{2}\\Omega < 0$$
</div>
<p>This profound result has critical consequences for stellar physics:</p>
<ul>
  <li><strong>Negative Heat Capacity:</strong> As a star loses energy by radiating luminosity $L = -\\frac{dE}{dt} > 0$, its total energy $E$ becomes more negative, which means $\\Omega$ decreases (the star contracts), and $K$ <em>increases</em> ($dK = -dE > 0$). Contracting stars heat up!</li>
  <li><strong>Kelvin-Helmholtz Timescale:</strong> The timescale over which a star can shine solely by releasing gravitational potential energy is:
  <div class="equation-box">
  $$\\tau_{\\text{KH}} = \\frac{|\\Omega|}{2 L} \\approx \\frac{3 G M^2}{10 R L} \\sim 3 \\times 10^7\\text{ years for the Sun}$$
  </div>
  Because Earth's geological record proves ages $> 4\\text{ Gyr}$, gravitational contraction cannot power the Sun, necessitating nuclear fusion.</li>
</ul>
"""
        },
        {
            "id": "sec-2-5",
            "title": "Energy Transport: Radiative Diffusion & Convective Instability",
            "content": """
<p>Energy generated in the deep stellar core must be transported outward to the surface. Stars utilize three potential mechanisms: conduction (negligible except in degenerate white dwarfs), radiative diffusion, and fluid convection.</p>

<h4>1. Radiative Transport & The Diffusion Approximation</h4>
<p>Inside a star, the photon mean free path $\\ell_{\\text{mfp}} = \\frac{1}{\\kappa \\rho} \\sim 1\\text{ mm} - 1\\text{ cm}$ is microscopic compared to the stellar radius. Photons undergo trillions of random walk scatterings in near-perfect local thermodynamic equilibrium (LTE). The radiative flux $F_{\\text{rad}}$ is governed by Fick's law of diffusion for radiation energy density $u = a_{\\text{rad}} T^4$:</p>
<div class="equation-box">
$$F_{\\text{rad}} = -\\frac{c}{3\\kappa \\rho} \\frac{du}{dr} = -\\frac{c}{3\\kappa \\rho} \\frac{d}{dr}(a_{\\text{rad}} T^4) = -\\frac{4 a_{\\text{rad}} c T^3}{3\\kappa \\rho} \\frac{dT}{dr}$$
</div>
<p>Since the total luminosity flowing through a sphere of radius $r$ is $L(r) = 4\\pi r^2 F_{\\text{rad}}$, we obtain the <strong>equation of radiative temperature gradient</strong>:</p>
<div class="equation-box">
$$\\frac{dT}{dr} = -\\frac{3 \\kappa(r) \\rho(r) L(r)}{16\\pi a_{\\text{rad}} c r^2 T(r)^3}$$
</div>
<p>where $\\kappa$ is the Rosseland mean opacity ($\text{cm}^2\\text{ g}^{-1}$), arising from electron Thomson scattering ($\\kappa_{\\text{es}} = 0.40\\text{ cm}^2\\text{ g}^{-1}$ for pure hydrogen) and Kramers' free-free / bound-free opacity ($\\kappa \\propto \\rho T^{-7/2}$).</p>

<h4>2. The Schwarzschild Criterion for Convective Instability</h4>
<p>Consider a fluid parcel displaced adiabatically upward by distance $\\Delta r > 0$. The parcel expands to match the surrounding ambient pressure ($P_p = P_a$), but retains its own entropy. If the resulting parcel density is lower than the surrounding ambient density ($\\rho_p < \\rho_a$), the parcel experiences a positive Archimedean buoyant force and continues accelerating upward—the layer is <strong>convectively unstable</strong>.</p>
<p>Comparing temperature gradients gives the <strong>Schwarzschild criterion</strong>:</p>
<div class="equation-box">
$$\\left|\\frac{dT}{dr}\\right|_{\\text{rad}} > \\left|\\frac{dT}{dr}\\right|_{\\text{ad}} = \\left(1 - \\frac{1}{\\gamma}\\right) \\frac{T}{P} \\left|\\frac{dP}{dr}\\right|$$
</div>
<p>Expressed in terms of the logarithmic temperature gradient $\\nabla \\equiv \\frac{d\\ln T}{d\\ln P}$:</p>
<div class="equation-box">
$$\\nabla_{\\text{rad}} > \\nabla_{\\text{ad}} = \\frac{\\gamma - 1}{\\gamma} = 0.4 \\quad (\\text{for an ideal monoatomic gas with } \\gamma = 5/3)$$
</div>
<p>Convection is triggered whenever:</p>
<ul>
  <li>The opacity $\\kappa$ is extremely high (e.g., in cool outer stellar envelopes where hydrogen/helium recombine, driving $\\nabla_{\\text{rad}} \\propto \\kappa$ up).</li>
  <li>The nuclear energy generation is intensely concentrated at the center (e.g., in massive stars where the CNO cycle produces huge core $L(r)/r^2$).</li>
</ul>
<p>Consequently, the Sun possesses a <strong>radiative core</strong> ($0 \\le r \\le 0.71 R_\\odot$) surrounded by an outer <strong>convective envelope</strong> ($0.71 R_\\odot \\le r \\le R_\\odot$). Massive stars ($M > 1.3 M_\\odot$) feature convective cores and radiative envelopes.</p>
"""
        },
        {
            "id": "sec-2-6",
            "title": "Thermonuclear Fusion: The Gamow Peak, p-p Chain & CNO Cycle",
            "content": """
<p>At classical temperatures of $T_c \\sim 1.5 \\times 10^7\\text{ K}$, the average thermal kinetic energy of protons is $k T \\approx 1.3\\text{ keV}$. However, the electrostatic Coulomb repulsive potential barrier between two approaching protons separated by nuclear radius $r_n \\approx 1\\text{ fm}$ is:</p>
<div class="equation-box">
$$E_{\\text{Coulomb}} = \\frac{e^2}{4\\pi\\varepsilon_0 r_n} \\approx 1.44\\text{ MeV} \\approx 1000 \\times kT$$
</div>
<p>Classically, zero protons possess enough energy to fuse. Stellar fusion is possible exclusively through <strong>quantum mechanical wave tunneling</strong>.</p>

<h4>The Gamow Peak</h4>
<p>The fusion cross-section $\\sigma(E)$ decomposes into the geometrical de Broglie area $\\pi \\lambda^2 \\propto 1/E$, the quantum mechanical barrier penetration probability $P(E)$, and an intrinsic nuclear reaction structure factor $S(E)$:</p>
<div class="equation-box">
$$\\sigma(E) = \\frac{S(E)}{E} \\exp\\left(-\\sqrt{\\frac{E_G}{E}}\\right)$$
</div>
<p>where $E_G = 2 m_r c^2 (\\pi \\alpha Z_1 Z_2)^2$ is the <strong>Gamow energy</strong> ($m_r$ is the reduced mass). The total nuclear reaction rate per unit volume is the Maxwell-Boltzmann average:</p>
<div class="equation-box">
$$\\langle \\sigma v \\rangle = \\left(\\frac{8}{\\pi m_r (kT)^3}\\right)^{1/2} \\int_0^\\infty S(E) \\exp\\left[-\\left(\\frac{E}{kT} + \\sqrt{\\frac{E_G}{E}}\\right)\\right] dE$$
</div>
<p>The integrand is the product of a falling Maxwellian tail $\\exp(-E/kT)$ and a rising quantum tunneling factor $\\exp(-\\sqrt{E_G/E})$. The product forms a sharp, localized Gaussian known as the <strong>Gamow Peak</strong> centered at energy:</p>
<div class="equation-box">
$$E_0 = \\left(\\frac{E_G (kT)^2}{4}\\right)^{1/3} \\approx 1.22 \\left(Z_1^2 Z_2^2 \\frac{m_r}{m_u} T_7^2\\right)^{1/3}\\text{ keV}$$
</div>

<h4>1. The Proton-Proton ($p$-$p$) Chain</h4>
<p>Dominates in stars with $M \\le 1.3 M_\\odot$ ($T_c < 1.8 \\times 10^7\\text{ K}$). Net reaction: $4\\,^1\\text{H} \\to\\ ^4\\text{He} + 2e^+ + 2\\nu_e + 26.73\\text{ MeV}$.</p>
<ol>
  <li><strong>PP-I Initiation:</strong>
  $$^1\\text{H} + ^1\\text{H} \\to\\ ^2\\text{H} + e^+ + \\nu_e \\quad (Q = 1.442\\text{ MeV}, \\tau \\sim 10^{10}\\text{ yr - weak force bottleneck})$$
  $$^2\\text{H} + ^1\\text{H} \\to\\ ^3\\text{He} + \\gamma \\quad (Q = 5.494\\text{ MeV}, \\tau \\sim 1\\text{ s})$$
  $$^3\\text{He} + ^3\\text{He} \\to\\ ^4\\text{He} + 2\\,^1\\text{H} \\quad (Q = 12.86\\text{ MeV}, \\tau \\sim 10^6\\text{ yr})$$
  </li>
  <li><strong>PP-II Branch ($14\\%$ in Sun):</strong> Produces $^7\\text{Be}$ and $^7\\text{Li}$, terminating in $^4\\text{He}$.</li>
  <li><strong>PP-III Branch ($0.02\\%$ in Sun):</strong> Produces high-energy $^8\\text{B}$ neutrinos ($E_\\nu \\le 14\\text{ MeV}$) detected by Super-Kamiokande and SNO.</li>
</ol>
<p>The energy generation rate scales as $\\epsilon_{pp} \\propto \\rho X^2 T^4$.</p>

<h4>2. The CNO (Carbon-Nitrogen-Oxygen) Cycle</h4>
<p>Uses pre-existing carbon, nitrogen, and oxygen as nuclear catalysts:</p>
<div class="equation-box">
$$^{12}\\text{C}(p, \\gamma)^{13}\\text{N}(e^+\\nu_e)^{13}\\text{C}(p, \\gamma)^{14}\\text{N}(p, \\gamma)^{15}\\text{O}(e^+\\nu_e)^{15}\\text{N}(p, \\alpha)^{12}\\text{C}$$
</div>
<p>Because the Coulomb barrier between protons and $Z=6, 7, 8$ nuclei is much higher ($E_G$ is large), the CNO cycle has a ferocious temperature sensitivity: $\\epsilon_{\\text{CNO}} \\propto \\rho X Z_{\\text{CNO}} T^{17}$. Above $T \\approx 1.8 \\times 10^7\\text{ K}$ ($M \\gtrsim 1.3 M_\\odot$), the CNO cycle completely surpasses the $p$-$p$ chain.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 2.2: Standard Solar Model Radial Profiles & Fusion Rates</h4>
  </div>
  <p>Inspect the radial interior structure of the Sun from center to photosphere. Toggle core temperature to compare $p$-$p$ chain vs CNO cycle cross-sections and examine radiative vs convective boundaries.</p>
  <div id="astro-solar-interior-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-2-7",
            "title": "The Solar Atmosphere, Helioseismology & The Solar Wind",
            "content": """
<p>Above the dense convective envelope lies the stratified solar atmosphere: the photosphere, chromosphere, transition region, and corona.</p>

<h4>1. The Photosphere & Limb Darkening</h4>
<p>The photosphere is the optical surface layer (optical depth $\\tau_\\nu \\approx 2/3$, thickness $\\sim 400\\text{ km}$) from which photons escape into space. Because we look along slant paths near the apparent edge (limb) of the solar disk, our line of sight penetrates to a shallower, cooler physical depth compared to disk center. The resulting <strong>limb darkening</strong> is described by the Eddington-Barbier approximation:</p>
<div class="equation-box">
$$\\frac{I(\\theta)}{I(0)} = \\frac{2}{5} + \\frac{3}{5}\\cos\\theta$$
</div>
<p>where $\\theta$ is the angle between the emergent ray and the surface normal.</p>

<h4>2. The Solar Corona & Coronal Heating Problem</h4>
<p>Above the chromosphere ($T \\sim 10^4\\text{ K}$) and a razor-thin transition region lies the <strong>corona</strong>, where temperatures paradoxically surge to $T \\sim 1-3 \\times 10^6\\text{ K}$, emitting energetic soft X-rays. This thermal inversion violates simple conductive/radiative thermodynamic transfer from the $5778\\text{ K}$ photosphere. Modern solar magnetohydrodynamics (MHD) attributes coronal heating to:</p>
<ul>
  <li><strong>Magnetic Reconnection & Nanoflares:</strong> Tangling and sudden topological reconnection of complex magnetic flux tubes driving localized bursts of magnetic energy dissipation (Parker nanoflare model).</li>
  <li><strong>MHD Alfvén Wave Dissipation:</strong> Upward-propagating Alfvén waves excited by convective granulation turbulent churning that dissipate energy nonlinearly in the low-density coronal plasma.</li>
</ul>

<h4>3. The Solar Wind: Parker's Hydrodynamic Solution</h4>
<p>Eugene Parker (1958) demonstrated that a static, isothermal corona cannot maintain zero pressure at spatial infinity ($P(\\infty) > 0$), requiring a continuous, supersonic hydrodynamic expansion known as the <strong>solar wind</strong>. The radial momentum equation for steady isothermal spherical expansion:</p>
<div class="equation-box">
$$v \\frac{dv}{dr} = -\\frac{1}{\\rho}\\frac{dP}{dr} - \\frac{G M_\\odot}{r^2} = -\\frac{c_s^2}{\\rho}\\frac{d\\rho}{dr} - \\frac{G M_\\odot}{r^2}$$
</div>
<p>Using mass conservation $\\dot{M} = 4\\pi r^2 \\rho v = \\text{const}$, this transforms into the celebrated de Laval nozzle equation:</p>
<div class="equation-box">
$$\\left(\\frac{v^2}{c_s^2} - 1\\right) \\frac{1}{v}\\frac{dv}{dr} = \\frac{2}{r}\\left(1 - \\frac{r_c}{r}\\right)$$
</div>
<p>where $r_c = \\frac{G M_\\odot}{2 c_s^2}$ is the <strong>critical sonic radius</strong>. The physical solution starts subsonic ($v < c_s$) near the Sun, accelerates smoothly through the critical point $r = r_c$ where $v = c_s$, and becomes highly supersonic ($v \\sim 400-800\\text{ km s}^{-1}$) throughout the heliosphere.</p>

<h4>4. Helioseismology</h4>
<p>Convective turbulence excites millions of resonant acoustic standing waves ($p$-modes) that propagate throughout the solar interior and reflect at the surface. By Doppler-mapping surface velocity oscillations (periods $\\sim 5\\text{ minutes}$), helioseismologists invert the acoustic dispersion relation $\\omega^2 = k_h^2 c_s^2$ to measure the internal sound speed profile $c_s(r) = \\sqrt{\\gamma P/\\rho}$ to within $0.1\\%$, mapping the base of the convective envelope ($0.713 R_\\odot$) and validating the Standard Solar Model.</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-2-1",
            "title": "Exoplanet System Characterization: Mass, Radius & Density",
            "statement": "An exoplanet orbiting a solar-type star ($M_* = 1.05 M_\\odot$, $R_* = 1.10 R_\\odot$) in a circular orbit ($e=0$) is observed with high-precision transit photometry and radial velocity spectroscopy. The observations reveal an orbital period $P = 4.20\\text{ days}$, a photometric transit depth $\\delta = \\Delta F/F = 0.0121$ ($1.21\\%$), and a stellar radial velocity semi-amplitude $K = 145.0\\text{ m s}^{-1}$. Assume edge-on inclination ($i = 90^\\circ$).\\n\\n(a) Calculate the orbital semi-major axis $a$ in AU.\\n(b) Determine the physical radius of the planet $R_p$ in Jupiter radii ($R_{\\text{Jup}} = 7.1492 \\times 10^7\\text{ m}$).\\n(c) Calculate the planet's mass $m_p$ in Jupiter masses ($M_{\\text{Jup}} = 1.898 \\times 10^{27}\\text{ kg}$).\\n(d) Calculate the planet's mean bulk density $\\bar{\\rho}_p$ in $\\text{g cm}^{-3}$ and classify the world.",
            "solution": """
<h4>(a) Orbital Semi-Major Axis</h4>
<p>From Kepler's Third Law $a = \\left[\\frac{G M_* P^2}{4\\pi^2}\\right]^{1/3}$:</p>
<div class="equation-box">
$$P = 4.20\\text{ days} = 4.20 \\times 86{,}400\\text{ s} = 362{,}880\\text{ s}$$
$$M_* = 1.05 \\times 1.989 \\times 10^{30}\\text{ kg} = 2.088 \\times 10^{30}\\text{ kg}$$
$$a = \\left[\\frac{(6.6743 \\times 10^{-11})(2.088 \\times 10^{30})(362{,}880)^2}{4\\pi^2}\\right]^{1/3} = \\left[\\frac{1.8327 \\times 10^{31}}{39.478}\\right]^{1/3} = (4.642 \\times 10^{29})^{1/3} \\approx 7.743 \\times 10^9\\text{ m}$$
$$a = \\frac{7.743 \\times 10^9\\text{ m}}{1.496 \\times 10^{11}\\text{ m/AU}} \\approx 0.0518\\text{ AU}$$
</div>

<h4>(b) Physical Radius of the Planet</h4>
<p>The transit depth is $\\delta = (R_p / R_*)^2 = 0.0121$. Thus:</p>
<div class="equation-box">
$$\\frac{R_p}{R_*} = \\sqrt{0.0121} = 0.110$$
$$R_* = 1.10 R_\\odot = 1.10 \\times 6.957 \\times 10^8\\text{ m} = 7.653 \\times 10^8\\text{ m}$$
$$R_p = 0.110 \\times 7.653 \\times 10^8\\text{ m} = 8.418 \\times 10^7\\text{ m}$$
</div>
<p>In Jupiter radii ($R_{\\text{Jup}} = 7.1492 \\times 10^7\\text{ m}$):</p>
<div class="equation-box">
$$R_p = \\frac{8.418 \\times 10^7}{7.1492 \\times 10^7} \\approx 1.177 R_{\\text{Jup}}$$
</div>

<h4>(c) Planetary Mass</h4>
<p>For a circular orbit with $i=90^\\circ$ ($\\sin i = 1$), the radial velocity amplitude is $K = \\left(\\frac{2\\pi G}{P}\\right)^{1/3} \\frac{m_p}{M_*^{2/3}}$. Rearranging for $m_p$:</p>
<div class="equation-box">
$$m_p = K M_*^{2/3} \\left(\\frac{P}{2\\pi G}\\right)^{1/3}$$
$$M_*^{2/3} = (2.088 \\times 10^{30})^{2/3} \\approx 1.6338 \\times 10^{20}$$
$$\\left(\\frac{P}{2\\pi G}\\right)^{1/3} = \\left(\\frac{362{,}880}{2\\pi \\times 6.6743 \\times 10^{-11}}\\right)^{1/3} = (8.654 \\times 10^{14})^{1/3} \\approx 95{,}298$$
$$m_p = 145.0 \\times 1.6338 \\times 10^{20} \\times 95{,}298 \\approx 2.2575 \\times 10^{27}\\text{ kg}$$
</div>
<p>In Jupiter masses ($M_{\\text{Jup}} = 1.898 \\times 10^{27}\\text{ kg}$):</p>
<div class="equation-box">
$$m_p = \\frac{2.2575 \\times 10^{27}}{1.898 \\times 10^{27}} \\approx 1.189 M_{\\text{Jup}}$$
</div>

<h4>(d) Bulk Density & Planet Classification</h4>
<p>The planet's volume is $V_p = \\frac{4}{3}\\pi R_p^3 = \\frac{4}{3}\\pi (8.418 \\times 10^7\\text{ m})^3 \\approx 2.498 \\times 10^{24}\\text{ m}^3 = 2.498 \\times 10^{30}\\text{ cm}^3$. The mean density is:</p>
<div class="equation-box">
$$\\bar{\\rho}_p = \\frac{2.2575 \\times 10^{30}\\text{ g}}{2.498 \\times 10^{30}\\text{ cm}^3} \\approx 0.904\\text{ g cm}^{-3}$$
</div>
<p>The planet has mass $1.19 M_{\\text{Jup}}$, radius $1.18 R_{\\text{Jup}}$, and bulk density $0.90\\text{ g/cm}^3$ orbiting at $0.052\\text{ AU}$ with a 4.2-day period. This is a canonical <strong>Hot Jupiter</strong>, inflated by intense stellar irradiation.</p>
"""
        },
        {
            "id": "prob-2-2",
            "title": "Central Pressure, Temperature & The Kelvin-Helmholtz Timescale",
            "statement": "Approximate the Sun as a spherically symmetric star with a parabolic density profile $\\rho(r) = \\rho_c [1 - (r/R)^2]$, where $\\rho_c$ is the central density and $R$ is the stellar surface radius.\\n\\n(a) Determine the relationship between central density $\\rho_c$ and mean density $\\bar{\\rho}$. Compute $\\rho_c$ for the Sun ($M_\\odot = 1.989 \\times 10^{30}\\text{ kg}$, $R_\\odot = 6.96 \\times 10^8\\text{ m}$).\\n(b) Derive the exact central pressure $P_c$ from the hydrostatic equation.\\n(c) Assuming an ideal gas equation of state $P = \\frac{\\rho k T}{\\mu m_H}$ with mean molecular weight $\\mu = 0.60$, calculate the central temperature $T_c$.\\n(d) Calculate the total gravitational potential energy $\\Omega$ and the Kelvin-Helmholtz timescale $\\tau_{\\text{KH}}$ if $L_\\odot = 3.828 \\times 10^{26}\\text{ W}$.",
            "solution": """
<h4>(a) Mass Integration & Central Density</h4>
<p>The total mass $M$ is:</p>
<div class="equation-box">
$$M = \\int_0^R 4\\pi r^2 \\rho(r) dr = 4\\pi \\rho_c \\int_0^R \\left(r^2 - \\frac{r^4}{R^2}\\right) dr = 4\\pi \\rho_c \\left[\\frac{R^3}{3} - \\frac{R^3}{5}\\right] = 4\\pi \\rho_c \\frac{2 R^3}{15} = \\frac{8\\pi}{15}\\rho_c R^3$$
</div>
<p>Since the mean density is $\\bar{\\rho} = \\frac{M}{\\frac{4}{3}\\pi R^3} = \\frac{8\\pi \\rho_c R^3 / 15}{4\\pi R^3 / 3} = \\frac{2}{5}\\rho_c$, we have:</p>
<div class="equation-box">
$$\\rho_c = \\frac{5}{2} \\bar{\\rho} = 2.5 \\times \\frac{1.989 \\times 10^{30}}{\\frac{4}{3}\\pi (6.96 \\times 10^8)^3} = 2.5 \\times 1409\\text{ kg m}^{-3} \\approx 3522\\text{ kg m}^{-3} = 3.522\\text{ g cm}^{-3}$$
</div>

<h4>(b) Central Pressure Derivation</h4>
<p>The enclosed mass $M(r)$ is:</p>
<div class="equation-box">
$$M(r) = 4\\pi \\rho_c \\left[\\frac{r^3}{3} - \\frac{r^5}{5 R^2}\\right]$$
</div>
<p>Integrating the hydrostatic equation $\\frac{dP}{dr} = -\\frac{G M(r)\\rho(r)}{r^2}$ with boundary condition $P(R) = 0$:</p>
<div class="equation-box">
$$P_c = \\int_0^R \\frac{G M(r)\\rho(r)}{r^2} dr = 4\\pi G \\rho_c^2 \\int_0^R \\left(\\frac{r}{3} - \\frac{r^3}{5R^2}\\right)\\left(1 - \\frac{r^2}{R^2}\\right) dr$$
$$P_c = 4\\pi G \\rho_c^2 \\int_0^R \\left(\\frac{r}{3} - \\frac{8 r^3}{15 R^2} + \\frac{r^5}{5 R^4}\\right) dr = 4\\pi G \\rho_c^2 R^2 \\left[\\frac{1}{6} - \\frac{2}{15} + \\frac{1}{30}\\right] = 4\\pi G \\rho_c^2 R^2 \\left[\\frac{5 - 4 + 1}{30}\\right] = \\frac{4\\pi}{15} G \\rho_c^2 R^2$$
</div>
<p>Substituting $\\rho_c = \\frac{15 M}{8\\pi R^3}$:</p>
<div class="equation-box">
$$P_c = \\frac{4\\pi}{15} G \\left(\\frac{15 M}{8\\pi R^3}\\right)^2 R^2 = \\frac{15}{16\\pi} \\frac{G M^2}{R^4} \\approx 0.2984 \\frac{G M^2}{R^4}$$
</div>
<p>Evaluating numerically for the Sun:</p>
<div class="equation-box">
$$P_c = 0.2984 \\times \\frac{(6.674 \\times 10^{-11})(1.989 \\times 10^{30})^2}{(6.96 \\times 10^8)^4} \\approx 3.34 \\times 10^{14}\\text{ N m}^{-2} = 3.34 \\times 10^{15}\\text{ dyn cm}^{-2}$$
</div>

<h4>(c) Central Temperature</h4>
<p>From the ideal gas law $P_c = \\frac{\\rho_c k T_c}{\\mu m_H}$:</p>
<div class="equation-box">
$$T_c = \\frac{P_c \\mu m_H}{\\rho_c k} = \\frac{(3.34 \\times 10^{14})(0.60 \\times 1.6735 \\times 10^{-27})}{(3522)(1.3807 \\times 10^{-23})} \\approx 6.9 \\times 10^6\\text{ K}$$
</div>
<p>This simple parabolic approximation captures the correct order of magnitude (the true Standard Solar Model with strong central concentration yields $T_c \\approx 1.57 \\times 10^7\\text{ K}$).</p>

<h4>(d) Gravitational Potential Energy & Kelvin-Helmholtz Timescale</h4>
<p>The gravitational energy is $\\Omega = -\\int_0^R \\frac{G M(r)}{r} 4\\pi r^2 \\rho(r) dr = -\\frac{5}{7} \\frac{G M^2}{R}$:</p>
<div class="equation-box">
$$|\\Omega| = \\frac{5}{7} \\frac{(6.674 \\times 10^{-11})(1.989 \\times 10^{30})^2}{6.96 \\times 10^8} \\approx 2.71 \\times 10^{41}\\text{ Joules}$$
</div>
<p>The Kelvin-Helmholtz timescale is:</p>
<div class="equation-box">
$$\\tau_{\\text{KH}} = \\frac{|\\Omega|}{2 L_\\odot} = \\frac{2.71 \\times 10^{41}\\text{ J}}{2 \\times 3.828 \\times 10^{26}\\text{ W}} \\approx 3.54 \\times 10^{14}\\text{ s} \\approx 1.12 \\times 10^7\\text{ years}$$
</div>
<p>This confirms that gravitational contraction could sustain solar luminosity for only $\\approx 11\\text{ million years}$, proving that nuclear energy must power the Sun over cosmological epochs.</p>
"""
        },
        {
            "id": "prob-2-3",
            "title": "Quantum Tunneling & Temperature Sensitivity of the p-p Chain vs CNO Cycle",
            "statement": "The nuclear energy generation rate for hydrogen fusion can be modeled locally as $\\epsilon(T) = \\epsilon_0 T^n$.\\n\\n(a) For the proton-proton chain at core temperature $T_6 = 15$ ($1.5 \\times 10^7\\text{ K}$), calculate the Gamow peak energy $E_0$ and the effective temperature exponent $n_{pp} = \\frac{d\\ln\\epsilon_{pp}}{d\\ln T}$.\\n(b) For the CNO cycle key reaction $^{14}\\text{N}(p, \\gamma)^{15}\\text{O}$ at the same temperature, compute the Gamow peak energy $E_{0,\\text{CNO}}$ and the exponent $n_{\\text{CNO}}$.\\n(c) If the core temperature of a star rises by $10\\%$, calculate the percentage increase in energy generation for the $p$-$p$ chain vs the CNO cycle. Explain why massive stars possess convective cores.",
            "solution": """
<h4>(a) Proton-Proton Chain Gamow Peak & Exponent</h4>
<p>For $p + p$, $Z_1 = 1$, $Z_2 = 1$, and reduced mass $m_r = \\frac{m_p m_p}{m_p + m_p} = \\frac{1}{2}m_p \\approx 0.50\\text{ amu}$.</p>
<p>The Gamow peak energy is:</p>
<div class="equation-box">
$$E_0 = 1.2204 \\left(Z_1^2 Z_2^2 m_r T_6^2\\right)^{1/3}\\text{ keV} = 1.2204 \\left(1 \\times 1 \\times 0.50 \\times 15^2\\right)^{1/3} = 1.2204 \\times (112.5)^{1/3} \\approx 1.2204 \\times 4.8274 \\approx 5.89\\text{ keV}$$
</div>
<p>The analytical temperature power-law exponent for any non-resonant Gamow reaction is $n = \\frac{\\tau - 2}{3}$, where $\\tau = 3 \\left(\\frac{E_0}{kT}\\right) = 3 \\frac{E_0}{0.08617 T_6/11.6045}$. At $T_6 = 15$, $kT = 1.293\\text{ keV}$.</p>
<div class="equation-box">
$$\\tau = 3 \\left(\\frac{5.891}{1.2926}\\right) \\approx 13.67 \\implies n_{pp} = \\frac{\\tau - 2}{3} = \\frac{13.67 - 2}{3} = \\frac{11.67}{3} \\approx 3.89 \\approx 4$$
</div>
<p>Thus $\\epsilon_{pp} \\propto T^4$.</p>

<h4>(b) CNO Cycle Gamow Peak & Exponent</h4>
<p>For $^{14}\\text{N} + p$, $Z_1 = 7$, $Z_2 = 1$, and $m_r = \\frac{14 \\times 1}{14 + 1} = \\frac{14}{15} \\approx 0.9333\\text{ amu}$.</p>
<div class="equation-box">
$$E_{0,\\text{CNO}} = 1.2204 \\left(7^2 \\times 1^2 \\times 0.9333 \\times 15^2\\right)^{1/3} = 1.2204 \\times (49 \\times 0.9333 \\times 225)^{1/3} = 1.2204 \\times (10{,}290)^{1/3} \\approx 1.2204 \\times 21.75 \\approx 26.54\\text{ keV}$$
</div>
<p>The dimensionless parameter $\\tau_{\\text{CNO}}$ is:</p>
<div class="equation-box">
$$\\tau_{\\text{CNO}} = 3 \\left(\\frac{26.54}{1.2926}\\right) \\approx 61.61 \\implies n_{\\text{CNO}} = \\frac{61.61 - 2}{3} = \\frac{59.61}{3} \\approx 19.87 \\approx 17-20$$
</div>
<p>Thus $\\epsilon_{\\text{CNO}} \\propto T^{17}$.</p>

<h4>(c) Thermal Response & Convective Core Trigger</h4>
<p>If temperature increases by $10\\%$ ($T'/T = 1.10$):</p>
<ul>
  <li>For the $p$-$p$ chain ($n \\approx 4$):
  $$\\frac{\\epsilon'}{\\epsilon} = (1.10)^4 = 1.4641 \\implies +46.4\\%\\text{ increase}$$
  </li>
  <li>For the CNO cycle ($n \\approx 17$):
  $$\\frac{\\epsilon'}{\\epsilon} = (1.10)^{17} \\approx 5.054 \\implies +405.4\\%\\text{ increase (a factor of 5!)}$$
  </li>
</ul>
<p>Because the CNO cycle generates energy with extreme temperature sensitivity ($\propto T^{17}$), in massive stars where the CNO cycle dominates, the energy output is exceptionally concentrated in the innermost few percent of the radius. This creates a steep radiative temperature gradient $\\left|\\frac{dT}{dr}\\right| \\propto \\frac{L(r)}{r^2}$ that exceeds the adiabatic gradient, triggering large-scale convection and establishing a turbulent <strong>convective core</strong>.</p>
"""
        }
    ]
}

os.makedirs('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library', exist_ok=True)
with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u1.json', 'w') as f:
    json.dump(u1, f, indent=2)
print("astro_u1.json written successfully")

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u2.json', 'w') as f:
    json.dump(u2, f, indent=2)
print("astro_u2.json written successfully")
