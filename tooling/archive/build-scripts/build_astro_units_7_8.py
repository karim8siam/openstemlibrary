import json
import os

u7 = {
    "unitId": 7,
    "title": "Cosmic Expansion, Redshifts & Relativistic Cosmology",
    "subtitle": "FLRW Metric, Friedmann Equations, Cosmic Inventory, Dark Energy & Supernova Cosmology",
    "icon": "💥",
    "summary": "This unit establishes the mathematical and physical foundations of modern relativistic cosmology. We trace the observational discovery of universal cosmic expansion via the Hubble-Lemaître law, rigorously distinguishing metric cosmological redshift $1+z = 1/a(t)$ from kinematic Doppler shifts. We formulate the Cosmological Principle and construct the maximally symmetric Friedmann-Lemaître-Robertson-Walker (FLRW) spacetime metric. We derive the Friedmann equations from Einstein's Field Equations with a perfect fluid stress-energy tensor. We map the cosmic inventory of matter, radiation, curvature, and dark energy, solving cosmological models from the Einstein-de Sitter matter universe to the de Sitter exponential expansion. Finally, we formulate cosmological distance metrics (luminosity and angular diameter distances) and analyze the Nobel Prize-winning Type Ia supernova discovery of cosmic acceleration.",
    "keyTakeaways": [
        "The Hubble-Lemaître law $v = H_0 d$ describes the uniform, isotropic expansion of space, with the Hubble constant $H_0 \\approx 70\\text{ km s}^{-1}\\text{Mpc}^{-1}$ establishing the characteristic Hubble expansion timescale $t_H = 1/H_0 \\approx 14\\text{ Gyr}$.",
        "Cosmological redshift $1 + z = \\frac{\\lambda_{\\text{obs}}}{\\lambda_{\\text{emit}}} = \\frac{a(t_0)}{a(t)}$ is fundamentally a metric phenomenon: photons are stretched by the expanding fabric of spacetime as they propagate across the universe, distinct from special relativistic Doppler motion.",
        "The Friedmann-Lemaître-Robertson-Walker (FLRW) metric $ds^2 = -c^2 dt^2 + a(t)^2 \\left[\\frac{dr^2}{1 - k r^2} + r^2 d\\Omega^2\\right]$ is the unique general relativistic metric describing an isotropic, homogeneous universe of spatial curvature $k \\in \\{-1, 0, +1\\}$.",
        "The Friedmann equations govern cosmic expansion: $H^2 = \\frac{8\\pi G}{3}\\rho - \\frac{k c^2}{a^2} + \\frac{\\Lambda c^2}{3}$ and $\\frac{\\ddot{a}}{a} = -\\frac{4\\pi G}{3}\\left(\\rho + \\frac{3P}{c^2}\\right) + \\frac{\\Lambda c^2}{3}$, with critical density $\\rho_c = \\frac{3H^2}{8\\pi G}$.",
        "Type Ia supernova standard candle observations at high redshift ($z \\sim 0.5 - 1.0$) proved that the cosmic expansion is currently accelerating ($\\ddot{a} > 0$), requiring negative-pressure dark energy ($w \\approx -1$) comprising $\\approx 68.5\\%$ of total cosmic energy density."
    ],
    "sections": [
        {
            "id": "sec-7-1",
            "title": "The Expanding Universe & The Hubble-Lemaître Law",
            "content": """
<p>In the 1910s and 1920s, Vesto Slipher obtained optical spectra of spiral nebulae, discovering that nearly all were systematically shifted toward longer wavelengths (receding from Earth at hundreds of kilometers per second). In 1927, Georges Lemaître theoretically predicted expanding universe solutions from Einstein's general relativity. In 1929, Edwin Hubble combined Slipher's radial velocities with Cepheid variable distance estimates, publishing the empirical linear velocity-distance relation known today as the <strong>Hubble-Lemaître Law</strong>:</p>
<div class="equation-box">
$$v = H_0 d$$
</div>
<p>where $v$ is the recession velocity in $\\text{km s}^{-1}$, $d$ is physical distance in megaparsecs ($\text{Mpc}$), and $H_0$ is the <strong>Hubble constant</strong> (the current expansion rate of the universe).</p>

<h4>Modern Values of $H_0$ & The Hubble Tension</h4>
<p>Measuring $H_0$ is one of the most critical endeavors in modern astrophysics:</p>
<ul>
  <li><strong>Late-Universe Distance Ladder (SH0ES, Riess et al.):</strong> Cepheid-calibrated Type Ia supernovae yield $H_0 = 73.04 \\pm 1.04\\text{ km s}^{-1}\\text{Mpc}^{-1}$.</li>
  <li><strong>Early-Universe CMB Angular Spectrum (Planck 2018):</strong> Extrapolating the $\\Lambda\\text{CDM}$ model from the surface of last scattering ($z \\approx 1100$) yields $H_0 = 67.36 \\pm 0.54\\text{ km s}^{-1}\\text{Mpc}^{-1}$.</li>
</ul>
<p>This persistent $> 5\\sigma$ discrepancy is known as the <strong>Hubble Tension</strong>, possibly hinting at new physics beyond the standard model (e.g., early dark energy or sterile neutrinos).</p>

<h4>Hubble Time & Hubble Distance</h4>
<p>Dimensional analysis of $H_0$ ($[\\text{velocity}/\\text{distance}] = \\text{time}^{-1}$) yields fundamental cosmic scales:</p>
<ul>
  <li><strong>The Hubble Time ($t_H$):</strong> The characteristic age of the universe assuming constant expansion speed:
  <div class="equation-box">
  $$t_H \\equiv \\frac{1}{H_0} = \\frac{1}{70\\text{ km s}^{-1}\\text{Mpc}^{-1}} = \\frac{3.0857 \\times 10^{19}\\text{ km}}{70\\text{ km/s}} \\approx 4.408 \\times 10^{17}\\text{ s} \\approx 13.97\\text{ Gyr}$$
  </div>
  </li>
  <li><strong>The Hubble Distance ($D_H$):</strong> The distance at which recession velocity equals the speed of light ($v = c$):
  <div class="equation-box">
  $$D_H \\equiv \\frac{c}{H_0} = \\frac{299{,}792\\text{ km/s}}{70\\text{ km s}^{-1}\\text{Mpc}^{-1}} \\approx 4{,}283\\text{ Mpc} \\approx 4.28\\text{ Gpc} \\approx 13.97\\text{ billion light-years}$$
  </div>
  </li>
</ul>
<p>Objects beyond $D_H$ recede from us faster than light! This does not violate Special Relativity, because galaxies are stationary relative to their local comoving space; it is the metric fabric of space itself that is expanding between them.</p>
"""
        },
        {
            "id": "sec-7-2",
            "title": "Cosmological Redshift vs Kinematic Doppler Shifts: The Scale Factor a(t)",
            "content": """
<p>In observational cosmology, spectral shifts are described by the dimensionless redshift parameter $z$:</p>
<div class="equation-box">
$$z \\equiv \\frac{\\lambda_{\\text{obs}} - \\lambda_{\\text{emit}}}{\\lambda_{\\text{emit}}} = \\frac{\\Delta \\lambda}{\\lambda_{\\text{emit}}}$$
</div>

<h4>Fundamental Distinction from Doppler Motion</h4>
<p>In Special Relativity, a source moving through static space at velocity $v = \\beta c$ produces a relativistic Doppler shift:</p>
<div class="equation-box">
$$1 + z_{\\text{Doppler}} = \\sqrt{\\frac{1 + \\beta}{1 - \\beta}}$$
</div>
<p>In cosmology, however, galaxies are not moving <em>through</em> static space; space itself is expanding. Cosmological redshift is a <strong>metric phenomenon</strong>.</p>

<h4>Derivation of Cosmological Redshift from the Scale Factor</h4>
<p>Let $a(t)$ denote the dimensionless <strong>cosmic scale factor</strong>, describing the relative spatial separation between comoving coordinate points as a function of cosmic time $t$, normalized such that today $a(t_0) = 1$.</p>
<p>Consider a light wave emitted at time $t_{\\text{emit}}$ with wavelength $\\lambda_{\\text{emit}}$ and observed today at $t_0$ with wavelength $\\lambda_{\\text{obs}}$. Light travels along null geodesics ($ds^2 = 0$). For radial propagation in a flat universe: $c\\,dt = a(t) dr$.</p>
<p>A first wave crest is emitted at $t_{\\text{emit}}$ and arrives at $t_0$:</p>
<div class="equation-box">
$$\\int_{t_{\\text{emit}}}^{t_0} \\frac{c\\,dt}{a(t)} = \\int_0^r dr = r$$
</div>
<p>The subsequent crest is emitted at $t_{\\text{emit}} + \\Delta t_{\\text{emit}}$ and arrives at $t_0 + \\Delta t_{\\text{obs}}$:</p>
<div class="equation-box">
$$\\int_{t_{\\text{emit}} + \\Delta t_{\\text{emit}}}^{t_0 + \\Delta t_{\\text{obs}}} \\frac{c\\,dt}{a(t)} = r$$
</div>
<p>Equating the two integrals and subtracting the overlapping interval $\\int_{t_{\\text{emit}}+\\Delta t_{\\text{emit}}}^{t_0} \\frac{c\\,dt}{a(t)}$:</p>
<div class="equation-box">
$$\\int_{t_0}^{t_0 + \\Delta t_{\\text{obs}}} \\frac{c\\,dt}{a(t)} = \\int_{t_{\\text{emit}}}^{t_{\\text{emit}} + \\Delta t_{\\text{emit}}} \\frac{c\\,dt}{a(t)}$$
</div>
<p>Since $\\Delta t$ is the period of a light wave ($10^{-15}\\text{ s}$), $a(t)$ is essentially constant over the interval:</p>
<div class="equation-box">
$$\\frac{c \\Delta t_{\\text{obs}}}{a(t_0)} = \\frac{c \\Delta t_{\\text{emit}}}{a(t_{\\text{emit}})}$$
</div>
<p>Because $\\lambda = c \\Delta t$, this yields the foundational relation of relativistic cosmology:</p>
<div class="equation-box">
$$\\frac{\\lambda_{\\text{obs}}}{\\lambda_{\\text{emit}}} = \\frac{a(t_0)}{a(t_{\\text{emit}})} = \\frac{1}{a(t_{\\text{emit}})}$$
$$1 + z = \\frac{1}{a(t)}$$
</div>
<p>When we observe a galaxy at $z = 1$, the light was emitted when the universe was exactly half its current linear size ($a = 0.5$). For the CMB at $z \\approx 1100$, the universe was $1/1101$ of its current size.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 7.1: Expanding Hubble Grid Universe & Cosmological Redshift</h4>
  </div>
  <p>Watch an expanding 2D cosmic grid of galaxies. Click any galaxy to become the observer, verifying that every observer sees all other galaxies receding with $v = H_0 d$, and watch photon wavelengths stretch in transit.</p>
  <div id="astro-hubble-expansion-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-7-3",
            "title": "The Cosmological Principle & The Robertson-Walker Spacetime Metric",
            "content": """
<p>Modern cosmology is founded upon the <strong>Cosmological Principle</strong>, which asserts that on sufficiently large scales ($\\gtrsim 100\\text{ Mpc}$), the Universe is:</p>
<ol>
  <li><strong>Homogeneous:</strong> Spatially invariant under translations—no preferred locations exist; every region looks statistically identical to every other region.</li>
  <li><strong>Isotropic:</strong> Invariant under spatial rotations—no preferred directions exist; the sky appears identical in every direction.</li>
</ol>

<h4>The Maximally Symmetric Robertson-Walker Metric</h4>
<p>Howard Robertson (1935) and Arthur Walker (1936) proved mathematically that the only four-dimensional spacetime metric compatible with spatial homogeneity and isotropy is the <strong>Robertson-Walker metric</strong>:</p>
<div class="equation-box">
$$ds^2 = -c^2 dt^2 + a(t)^2 \\left[\\frac{dr^2}{1 - k r^2} + r^2 (d\\theta^2 + \\sin^2\\theta d\\phi^2)\\right]$$
</div>
<p>where:</p>
<ul>
  <li>$t$ is <strong>cosmic time</strong>, measured by clocks comoving with the cosmic fluid.</li>
  <li>$r, \\theta, \\phi$ are dimensionless <strong>comoving coordinates</strong>, fixed to galaxies that move solely with the expansion.</li>
  <li>$a(t)$ is the time-dependent cosmic scale factor (dimensions of length).</li>
  <li>$k$ is the spatial curvature index:
    <ul>
      <li>$k = 0$: <strong>Flat Euclidean Space ($E^3$)</strong>. Spatial slices are infinite flat 3D planes ($d\\sigma^2 = dr^2 + r^2 d\\Omega^2$).</li>
      <li>$k = +1$: <strong>Closed Spherical Space ($S^3$)</strong>. A finite, unbounded 3D hypersphere of radius $a(t)$ embedded in 4D space with positive constant Gaussian curvature. Sum of triangle angles $> 180^\\circ$.</li>
      <li>$k = -1$: <strong>Open Hyperbolic Space ($H^3$)</strong>. An infinite 3D saddle space with negative constant curvature. Sum of triangle angles $< 180^\\circ$.</li>
    </ul>
  </li>
</ul>
<p>Using the radial coordinate substitution $r = S_k(\\chi)$ where $S_k(\\chi) = \\sin\\chi$ ($k=+1$), $\\chi$ ($k=0$), and $\\sinh\\chi$ ($k=-1$), the metric takes the elegant form:</p>
<div class="equation-box">
$$ds^2 = -c^2 dt^2 + a(t)^2 \\left[d\\chi^2 + S_k^2(\\chi)(d\\theta^2 + \\sin^2\\theta d\\phi^2)\\right]$$
</div>
"""
        },
        {
            "id": "sec-7-4",
            "title": "Derivation of the Friedmann Equations from Einstein's Field Equations",
            "content": """
<p>While the Robertson-Walker metric specifies the geometry of spacetime, the dynamic time evolution of the scale factor $a(t)$ is dictated by Einstein's Field Equations of General Relativity:</p>
<div class="equation-box">
$$G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4} T_{\\mu\\nu}$$
</div>
<p>where $G_{\\mu\\nu} = R_{\\mu\\nu} - \\frac{1}{2} R g_{\\mu\\nu}$ is the Einstein tensor and $\\Lambda$ is the cosmological constant.</p>

<h4>1. Stress-Energy Tensor of the Cosmic Fluid</h4>
<p>By the cosmological principle, the matter-energy content of the universe is described by a homogeneous, isotropic <strong>perfect fluid</strong>:</p>
<div class="equation-box">
$$T^\\mu_\\nu = \\text{diag}\\left(-\\rho c^2, P, P, P\\right)$$
</div>
<p>where $\\rho(t)$ is total mass-energy density and $P(t)$ is isotropic pressure.</p>

<h4>2. Computing the Christoffel Symbols and Ricci Tensor</h4>
<p>For the FLRW metric $g_{00} = -c^2$, $g_{rr} = \\frac{a^2}{1-kr^2}$, $g_{\\theta\\theta} = a^2 r^2$, $g_{\\phi\\phi} = a^2 r^2 \\sin^2\\theta$, the non-zero Christoffel symbols $\\Gamma^\\lambda_{\\mu\\nu} = \\frac{1}{2}g^{\\lambda\\sigma}(\\partial_\\mu g_{\\nu\\sigma} + \\partial_\\nu g_{\\mu\\sigma} - \\partial_\\sigma g_{\\mu\\nu})$ yield the non-vanishing Ricci tensor components:</p>
<div class="equation-box">
$$R_{00} = -3 \\frac{\\ddot{a}}{a}$$
$$R_{ij} = \\left(\\frac{\\ddot{a}}{a} + 2\\frac{\\dot{a}^2}{a^2} + 2\\frac{k c^2}{a^2}\\right) g_{ij}$$
</div>
<p>The Ricci scalar is $R = g^{\\mu\\nu} R_{\\mu\\nu} = \\frac{6}{c^2}\\left(\\frac{\\ddot{a}}{a} + \\frac{\\dot{a}^2}{a^2} + \\frac{k c^2}{a^2}\\right)$.</p>

<h4>3. The First Friedmann Equation</h4>
<p>Substituting into the time-time ($00$) component of Einstein's equations $G^0_0 + \\Lambda = \\frac{8\\pi G}{c^4} T^0_0$:</p>
<div class="equation-box">
$$-3\\left(\\frac{\\dot{a}^2}{a^2} + \\frac{k c^2}{a^2}\\right) + \\Lambda c^2 = -\\frac{8\\pi G}{c^2} (\\rho c^2) = -8\\pi G \\rho$$
</div>
<p>Rearranging and defining the Hubble parameter $H(t) \\equiv \\frac{\\dot{a}}{a}$ gives the <strong>First Friedmann Equation</strong>:</p>
<div class="equation-box">
$$H^2(t) \\equiv \\left(\\frac{\\dot{a}}{a}\\right)^2 = \\frac{8\\pi G}{3}\\rho - \\frac{k c^2}{a^2} + \\frac{\\Lambda c^2}{3}$$
</div>

<h4>4. The Second Friedmann (Acceleration) Equation</h4>
<p>Combining the spatial ($ii$) component $G^i_i + \\Lambda = \\frac{8\\pi G}{c^4} T^i_i = \\frac{8\\pi G}{c^4} P$ with the first equation yields the <strong>Acceleration Equation</strong>:</p>
<div class="equation-box">
$$\\frac{\\ddot{a}}{a} = -\\frac{4\\pi G}{3}\\left(\\rho + \\frac{3P}{c^2}\\right) + \\frac{\\Lambda c^2}{3}$$
</div>
<p>Notice that ordinary matter and radiation ($\rho > 0, P \\ge 0$) exert a negative acceleration, slowing down the expansion ($\\ddot{a} < 0$). To produce an <em>accelerating</em> expansion ($\\ddot{a} > 0$), we require an energy component with large negative pressure: $P < -\\frac{1}{3}\\rho c^2$, or a positive cosmological constant $\\Lambda > 0$.</p>

<h4>5. The Fluid Continuity Equation</h4>
<p>Conservation of energy-momentum $\\nabla_\\mu T^{\\mu\\nu} = 0$ yields the continuity equation:</p>
<div class="equation-box">
$$\\dot{\\rho} + 3\\frac{\\dot{a}}{a}\\left(\\rho + \\frac{P}{c^2}\\right) = 0$$
</div>
"""
        },
        {
            "id": "sec-7-5",
            "title": "Cosmic Inventory: Density Parameters, Equation of State & Critical Density",
            "content": """
<p>The equation of state relating pressure to density is parametrized by the dimensionless parameter $w$:</p>
<div class="equation-box">
$$P = w \\rho c^2$$
</div>
<p>Substituting into the continuity equation $\\frac{\\dot{\\rho}}{\\rho} = -3(1+w)\\frac{\\dot{a}}{a}$ yields the scaling of density with scale factor:</p>
<div class="equation-box">
$$\\rho(a) \\propto a^{-3(1+w)}$$
</div>

<h4>Cosmic Components & Scaling Behaviors</h4>
<ol>
  <li><strong>Non-Relativistic Matter ($w = 0$):</strong> Dust, cold dark matter, stars, and baryonic gas have negligible thermal velocities ($k T \\ll m c^2$), so $P \\ll \\rho c^2$.
  $$\\rho_m(a) = \\rho_{m,0} a^{-3} = \\rho_{m,0} (1+z)^3$$
  Density drops inversely with volume ($V \\propto a^3$).</li>
  <li><strong>Relativistic Radiation ($w = 1/3$):</strong> Photons (CMB) and relativistic neutrinos have $P = \\frac{1}{3}u = \\frac{1}{3}\\rho c^2$.
  $$\\rho_r(a) = \\rho_{r,0} a^{-4} = \\rho_{r,0} (1+z)^4$$
  In addition to volume dilution ($a^{-3}$), each photon's energy is redshifted ($E = h\\nu \\propto a^{-1}$), yielding an extra factor of $1/a$.</li>
  <li><strong>Cosmological Constant / Vacuum Energy ($w = -1$):</strong>
  $$P_\\Lambda = -\\rho_\\Lambda c^2 \\implies \\rho_\\Lambda = \\frac{\\Lambda c^2}{8\\pi G} = \\text{constant!}$$
  Vacuum energy density does not dilute as space expands.</li>
</ol>

<h4>Critical Density & Dimensionless Density Parameters ($\\Omega$)</h4>
<p>For a spatially flat universe ($k = 0$) without cosmological constant, the First Friedmann equation gives $H^2 = \\frac{8\\pi G}{3}\\rho_c$. The <strong>critical density</strong> is:</p>
<div class="equation-box">
$$\\rho_c(t) \\equiv \\frac{3 H^2(t)}{8\\pi G}, \\quad \\rho_{c,0} = \\frac{3 H_0^2}{8\\pi G} \\approx 8.5 \\times 10^{-27}\\text{ kg m}^{-3} \\approx 5\\text{ protons m}^{-3}$$
</div>
<p>Dividing the First Friedmann Equation by $H_0^2$ defines the dimensionless <strong>density parameters</strong> today:</p>
<div class="equation-box">
$$\\Omega_m \\equiv \\frac{\\rho_{m,0}}{\\rho_{c,0}}, \\quad \\Omega_r \\equiv \\frac{\\rho_{r,0}}{\\rho_{c,0}}, \\quad \\Omega_\\Lambda \\equiv \\frac{\\Lambda c^2}{3 H_0^2}, \\quad \\Omega_k \\equiv -\\frac{k c^2}{a_0^2 H_0^2}$$
</div>
<p>The First Friedmann Equation simplifies to the master cosmic balance relation:</p>
<div class="equation-box">
$$\\Omega_m + \\Omega_r + \\Omega_\\Lambda + \\Omega_k = 1 \\implies \\Omega_{\\text{tot}} \\equiv \\Omega_m + \\Omega_r + \\Omega_\\Lambda = 1 - \\Omega_k$$
</div>
<p>If $\\Omega_{\\text{tot}} = 1$, space is exactly flat ($k=0, \\Omega_k = 0$). If $\\Omega_{\\text{tot}} > 1$, space is spherical ($k=+1, \\Omega_k < 0$). If $\\Omega_{\\text{tot}} < 1$, space is hyperbolic ($k=-1, \\Omega_k > 0$).</p>
<p>The Hubble parameter evolves dynamically with redshift as:</p>
<div class="equation-box">
$$H(z) = H_0 \\sqrt{\\Omega_{r,0}(1+z)^4 + \\Omega_{m,0}(1+z)^3 + \\Omega_{k,0}(1+z)^2 + \\Omega_{\\Lambda,0}}$$
</div>
"""
        },
        {
            "id": "sec-7-6",
            "title": "Cosmological Models, The Deceleration Parameter & Age of the Universe",
            "content": """
<p>Solving the Friedmann equation for single- and multi-component universes reveals how the geometry and cosmic inventory dictate the expansion history.</p>

<h4>Analytical Single-Component Universes</h4>
<ul>
  <li><strong>Radiation-Dominated Universe ($\\Omega_r = 1$):</strong>
  $$\\dot{a} \\propto a^{-1} \\implies a(t) = \\left(\\frac{t}{t_0}\\right)^{1/2}, \\quad t_0 = \\frac{1}{2 H_0}$$
  </li>
  <li><strong>Einstein-de Sitter Flat Matter Universe ($\\Omega_m = 1$):</strong>
  $$\\dot{a} \\propto a^{-1/2} \\implies a(t) = \\left(\\frac{t}{t_0}\\right)^{2/3}, \\quad t_0 = \\frac{2}{3 H_0} \\approx 9.3\\text{ Gyr}$$
  </li>
  <li><strong>de Sitter Vacuum Universe ($\\Omega_\\Lambda = 1$):</strong>
  $$\\frac{\\dot{a}}{a} = H_0 = \\text{const} \\implies a(t) = e^{H_0 (t - t_0)}, \\quad t_0 = \\infty$$
  </li>
  <li><strong>Milne Empty Universe ($\\Omega = 0, k = -1$):</strong>
  $$\\dot{a} = c \\implies a(t) = \\frac{t}{t_0}, \\quad t_0 = \\frac{1}{H_0} \\approx 14\\text{ Gyr}$$
  </li>
</ul>

<h4>The Deceleration Parameter ($q_0$)</h4>
<p>The deceleration parameter quantifies the second derivative of the scale factor:</p>
<div class="equation-box">
$$q(t) \\equiv -\\frac{\\ddot{a} a}{\\dot{a}^2} = -\\frac{\\ddot{a}}{a H^2}$$
</div>
<p>From the acceleration equation $\\frac{\\ddot{a}}{a} = -\\frac{4\\pi G}{3}(\\rho + 3P/c^2) + \\frac{\\Lambda c^2}{3}$:</p>
<div class="equation-box">
$$q_0 = \\frac{1}{2}\\Omega_m + \\Omega_r - \\Omega_\\Lambda$$
</div>
<p>In our modern universe where radiation is negligible ($\\Omega_r \\approx 10^{-4}$):</p>
<div class="equation-box">
$$q_0 \\approx \\frac{1}{2}\\Omega_m - \\Omega_\\Lambda \\approx \\frac{1}{2}(0.315) - 0.685 \\approx 0.158 - 0.685 = -0.527 < 0$$
</div>
<p>Because $q_0 < 0$, the expansion of our Universe is accelerating!</p>

<h4>Exact Age of the $\\Lambda\\text{CDM}$ Universe</h4>
<p>For a flat universe with matter and dark energy ($\\Omega_m + \\Omega_\\Lambda = 1, \\Omega_k = 0$):</p>
<div class="equation-box">
$$t_0 = \\int_0^1 \\frac{da}{a H(a)} = \\frac{1}{H_0} \\int_0^1 \\frac{da}{a \\sqrt{\\Omega_m a^{-3} + \\Omega_\\Lambda}} = \\frac{1}{H_0} \\int_0^1 \\frac{\\sqrt{a}\\,da}{\\sqrt{\\Omega_m + \\Omega_\\Lambda a^3}}$$
</div>
<p>Evaluating this integral analytically via substitution $u = a^{3/2} \\sqrt{\\Omega_\\Lambda/\\Omega_m}$:</p>
<div class="equation-box">
$$t_0 = \\frac{2}{3 H_0 \\sqrt{\\Omega_\\Lambda}} \\ln\\left(\\frac{1 + \\sqrt{\\Omega_\\Lambda}}{\\sqrt{\\Omega_m}}\\right) = \\frac{2}{3 H_0 \\sqrt{\\Omega_\\Lambda}} \\text{arcsinh}\\left(\\sqrt{\\frac{\\Omega_\\Lambda}{\\Omega_m}}\\right)$$
</div>
<p>For Planck parameters ($H_0 = 67.4\\text{ km s}^{-1}\\text{Mpc}^{-1}, \\Omega_m = 0.315, \\Omega_\\Lambda = 0.685$):</p>
<div class="equation-box">
$$t_0 = \\frac{2}{3 \\times (67.4) \\sqrt{0.685}} \\times \\text{arcsinh}\\left(\\sqrt{\\frac{0.685}{0.315}}\\right) \\approx 0.956 \\times t_H \\approx 13.79 \\pm 0.02\\text{ billion years}$$
</div>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 7.2: Multi-Component Friedmann Equation Integrator: $a(t)$ Simulator</h4>
  </div>
  <p>Dynamically adjust sliders for $\\Omega_m$, $\\Omega_r$, and $\\Omega_\\Lambda$ to integrate the Friedmann equation forward and backward in time, computing the age of the universe and determining whether the cosmos ends in a Big Crunch, Big Freeze, or Big Rip.</p>
  <div id="astro-friedmann-universe-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-7-7",
            "title": "Cosmological Distances & Type Ia Supernova Dark Energy Discovery",
            "content": """
<p>In expanding curved spacetime, the concept of 'distance' bifurcates into distinct operational definitions.</p>

<h4>1. Comoving Distance ($\\chi$)</h4>
<p>The comoving distance between an observer at $z=0$ and a source at redshift $z$ is:</p>
<div class="equation-box">
$$\\chi(z) = c \\int_{t(z)}^{t_0} \\frac{dt'}{a(t')} = c \\int_0^z \\frac{dz'}{H(z')}$$
</div>

<h4>2. Luminosity Distance ($d_L$)</h4>
<p>The luminosity distance is defined such that the inverse-square law holds: $F = \\frac{L}{4\\pi d_L^2}$. In an FLRW universe, two factors dilute the observed photon flux:</p>
<ul>
  <li>Each photon's energy is redshifted by $(1+z)^{-1}$.</li>
  <li>The arrival rate of photons is time-dilated by $(1+z)^{-1}$.</li>
</ul>
<p>Consequently, the received flux is $F = \\frac{L}{4\\pi [a_0 S_k(\\chi)]^2 (1+z)^2}$. For a flat universe ($S_k(\\chi) = \\chi$):</p>
<div class="equation-box">
$$d_L(z) = (1+z) \\chi(z) = (1+z) c \\int_0^z \\frac{dz'}{H(z')}$$
</div>

<h4>3. Angular Diameter Distance ($d_A$)</h4>
<p>The angular diameter distance relates physical transverse source diameter $D$ to observed angular diameter $\\theta$: $\\theta = D / d_A$. Since the physical diameter was $D = a(t) r \\theta = \\frac{r \\theta}{1+z}$:</p>
<div class="equation-box">
$$d_A(z) = \\frac{\\chi(z)}{1+z}$$
</div>
<p>Connecting the two is <strong>Etherington's Reciprocity Theorem</strong>:</p>
<div class="equation-box">
$$d_L(z) = (1+z)^2 d_A(z)$$
</div>
<p>Notice that as $z \\to \\infty$, $d_A(z)$ reaches a maximum near $z \\sim 1.6$ and then <em>decreases</em>! Highly distant galaxies appear angularly larger on the sky because their light was emitted when they were physically closer to us!</p>

<h4>The Type Ia Supernova Discovery of Cosmic Acceleration</h4>
<p>Type Ia supernovae result from the thermonuclear detonation of carbon-oxygen white dwarfs near the Chandrasekhar limit. Because their progenitor masses are identical, they act as magnificent standard candles with peak absolute magnitude $M_B \\approx -19.3$.</p>
<p>In 1998, two competing teams—the High-Z Supernova Search Team (Brian Schmidt and Adam Riess) and the Supernova Cosmology Project (Saul Perlmutter)—measured the distance moduli $\\mu(z) = m_B - M_B = 5\\log_{10} d_L(z) - 5$ of high-redshift supernovae ($z \\sim 0.3 - 1.0$).</p>
<p>They discovered that distant supernovae were systematically $\\approx 0.25\\text{ magnitudes}$ <em>fainter</em> than predicted by a decelerating matter-dominated universe ($\\Omega_m = 1$). To produce faint flux at a given redshift requires a larger luminosity distance $d_L(z)$, which requires an accelerating scale factor driven by negative-pressure <strong>Dark Energy</strong> ($\\\\Omega_\\Lambda \\approx 0.7$, Nobel Prize in Physics 2011).</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-7-1",
            "title": "Age of the Universe in Flat Matter-Dominated vs Flat Lambda-CDM",
            "statement": "Consider a flat universe ($k=0$) with modern Hubble constant $H_0 = 67.4\\text{ km s}^{-1}\\text{Mpc}^{-1}$.\\n\\n(a) Compute the Hubble time $t_H = 1/H_0$ in billions of years (Gyr).\\n(b) Calculate the age of an Einstein-de Sitter universe (pure matter, $\\Omega_m = 1.0, \\Omega_\\Lambda = 0$). Explain why this created a historical crisis with globular cluster ages ($\\sim 12-13\\text{ Gyr}$).\\n(c) Calculate the exact age of a flat $\\Lambda\\text{CDM}$ universe with $\\Omega_m = 0.315$ and $\\Omega_\\Lambda = 0.685$ using the analytical formula $t_0 = \\frac{2}{3 H_0 \\sqrt{\\Omega_\\Lambda}} \\text{arcsinh}\\left(\\sqrt{\\frac{\\Omega_\\Lambda}{\\Omega_m}}\\right)$.",
            "solution": """
<h4>(a) Hubble Time Calculation</h4>
<p>With $H_0 = 67.4\\text{ km s}^{-1}\\text{Mpc}^{-1}$:</p>
<div class="equation-box">
$$t_H = \\frac{1}{H_0} = \\frac{3.0857 \\times 10^{19}\\text{ km}}{67.4\\text{ km s}^{-1}} \\approx 4.578 \\times 10^{17}\\text{ seconds}$$
$$t_H = \\frac{4.578 \\times 10^{17}\\text{ s}}{3.15576 \\times 10^7\\text{ s/yr}} \\approx 1.4507 \\times 10^{10}\\text{ years} = 14.507\\text{ Gyr}$$
</div>

<h4>(b) Einstein-de Sitter Age & Age Crisis</h4>
<p>For an Einstein-de Sitter flat matter universe ($\Omega_m = 1, \Omega_\Lambda = 0$), $a(t) = (t/t_0)^{2/3}$. The age is:</p>
<div class="equation-box">
$$t_{\\text{EdS}} = \\frac{2}{3} t_H = \\frac{2}{3} \\times 14.507\\text{ Gyr} \\approx 9.67\\text{ Gyr}$$
</div>
<p>This result was a crisis: stellar evolution models and radioactive cosmochronology prove that the oldest globular cluster stars (e.g., M92) are at least $12.5 - 13.5\\text{ Gyr}$ old. A universe of age $9.7\\text{ Gyr}$ cannot host stars that are $13\\text{ Gyr}$ old!</p>

<h4>(c) Exact Age of the Flat $\\Lambda\\text{CDM}$ Universe</h4>
<p>For $\\Omega_m = 0.315$ and $\\Omega_\\Lambda = 0.685$:</p>
<div class="equation-box">
$$\\sqrt{\\frac{\\Omega_\\Lambda}{\\Omega_m}} = \\sqrt{\\frac{0.685}{0.315}} = \\sqrt{2.1746} \\approx 1.47465$$
$$\\text{arcsinh}(1.47465) = \\ln\\left(1.47465 + \\sqrt{1 + (1.47465)^2}\\right) = \\ln(1.47465 + \\sqrt{1 + 2.1746}) = \\ln(1.47465 + \\sqrt{3.1746}) = \\ln(1.47465 + 1.7817) = \\ln(3.2564) \\approx 1.1806$$
</div>
<p>Now evaluate the prefactor:</p>
<div class="equation-box">
$$\\text{Prefactor} = \\frac{2}{3 \\sqrt{\\Omega_\\Lambda}} t_H = \\frac{2}{3 \\times \\sqrt{0.685}} \\times 14.507\\text{ Gyr} = \\frac{2}{3 \\times 0.82765} \\times 14.507 = \\frac{29.014}{2.483} \\approx 11.685\\text{ Gyr}$$
$$t_0 = 11.685\\text{ Gyr} \\times 1.1806 \\approx 13.795\\text{ Gyr} \\approx 13.80\\text{ Gyr}$$
</div>
<p>Dark energy resolves the cosmic age crisis: because the cosmological constant produced late-time cosmic acceleration, the universe expanded slower in the past, stretching its total age from $9.7\\text{ Gyr}$ to $13.80\\text{ Gyr}$, comfortably older than the oldest globular clusters.</p>
"""
        },
        {
            "id": "prob-7-2",
            "title": "Luminosity Distance, Angular Diameter Distance & Distance Modulus at z=2",
            "statement": "In a flat $\\Lambda\\text{CDM}$ universe with $H_0 = 70.0\\text{ km s}^{-1}\\text{Mpc}^{-1}$, $\\Omega_m = 0.30$, and $\\Omega_\\Lambda = 0.70$, a quasar is discovered at redshift $z = 2.00$.\\n\\n(a) Numerically evaluate the comoving distance $\\chi(z) = \\frac{c}{H_0} \\int_0^2 \\frac{dz'}{\\sqrt{0.30(1+z')^3 + 0.70}}$ using Simpson's rule with 4 intervals ($N=4, \\Delta z = 0.5$).\\n(b) Compute the luminosity distance $d_L(z)$ in Mpc and in gigalight-years.\\n(c) Compute the angular diameter distance $d_A(z)$ in Mpc.\\n(d) Determine the distance modulus $\\mu$ of the quasar.",
            "solution": """
<h4>(a) Numerical Evaluation of Comoving Distance</h4>
<p>The integrand is $f(z) = [0.30(1+z)^3 + 0.70]^{-1/2}$. With step size $h = \\Delta z = 0.5$ at nodes $z = 0.0, 0.5, 1.0, 1.5, 2.0$:</p>
<ul>
  <li>$z_0 = 0.0$: $f(0) = [0.3(1) + 0.7]^{-1/2} = 1.0000$</li>
  <li>$z_1 = 0.5$: $f(0.5) = [0.3(1.5)^3 + 0.7]^{-1/2} = [0.3(3.375) + 0.7]^{-1/2} = [1.7125]^{-1/2} \\approx 0.7642$</li>
  <li>$z_2 = 1.0$: $f(1.0) = [0.3(2)^3 + 0.7]^{-1/2} = [0.3(8) + 0.7]^{-1/2} = [3.10]^{-1/2} \\approx 0.5680$</li>
  <li>$z_3 = 1.5$: $f(1.5) = [0.3(2.5)^3 + 0.7]^{-1/2} = [0.3(15.625) + 0.7]^{-1/2} = [5.3875]^{-1/2} \\approx 0.4308$</li>
  <li>$z_4 = 2.0$: $f(2.0) = [0.3(3)^3 + 0.7]^{-1/2} = [0.3(27) + 0.7]^{-1/2} = [8.80]^{-1/2} \\approx 0.3371$</li>
</ul>
<p>By Simpson's $1/3$ rule ($I = \\frac{h}{3}[f_0 + 4f_1 + 2f_2 + 4f_3 + f_4]$):</p>
<div class="equation-box">
$$I = \\frac{0.5}{3} [1.0000 + 4(0.7642) + 2(0.5680) + 4(0.4308) + 0.3371]$$
$$I = \\frac{0.5}{3} [1.0000 + 3.0568 + 1.1360 + 1.7232 + 0.3371] = \\frac{0.5}{3} [7.2531] \\approx 1.2088$$
</div>
<p>The Hubble distance is $D_H = c/H_0 = \\frac{299{,}792\\text{ km/s}}{70.0\\text{ km s}^{-1}\\text{Mpc}^{-1}} \\approx 4282.7\\text{ Mpc}$. Thus:</p>
<div class="equation-box">
$$\\chi(z=2) = D_H \\times I = 4282.7 \\times 1.2088 \\approx 5177\\text{ Mpc}$$
</div>

<h4>(b) Luminosity Distance</h4>
<p>The luminosity distance is $d_L = (1+z) \\chi$:</p>
<div class="equation-box">
$$d_L(z=2) = (1 + 2.0) \\times 5177\\text{ Mpc} = 3 \\times 5177 = 15{,}531\\text{ Mpc} \\approx 15.53\\text{ Gpc}$$
</div>
<p>Converting to gigalight-years ($1\\text{ pc} = 3.2616\\text{ ly}$):</p>
<div class="equation-box">
$$d_L = 15.531 \\times 3.2616 \\approx 50.66\\text{ billion light-years}$$
</div>

<h4>(c) Angular Diameter Distance</h4>
<p>The angular diameter distance is $d_A = \\frac{\\chi}{1+z}$:</p>
<div class="equation-box">
$$d_A(z=2) = \\frac{5177\\text{ Mpc}}{1 + 2.0} = \\frac{5177}{3} \\approx 1726\\text{ Mpc} \\approx 1.73\\text{ Gpc} \\approx 5.63\\text{ Gly}$$
</div>
<p>Notice that $d_L / d_A = (1+z)^2 = (3)^2 = 9.0$: the luminosity distance is 9 times larger than the angular diameter distance!</p>

<h4>(d) Distance Modulus</h4>
<p>The distance modulus is $\\mu = 5\\log_{10}(d_L / \\text{pc}) - 5$:</p>
<div class="equation-box">
$$d_L = 1.5531 \\times 10^{10}\\text{ pc} \\implies \\log_{10}(d_L) = 10.1912$$
$$\\mu = 5(10.1912) - 5 = 50.956 - 5 = 45.96\\text{ magnitudes}$$
</div>
"""
        },
        {
            "id": "prob-7-3",
            "title": "Deceleration Parameter & Transition Redshift to Cosmic Acceleration",
            "statement": "In a flat $\\Lambda\\text{CDM}$ universe with current parameters $\\Omega_{m,0} = 0.30$ and $\\Omega_{\\Lambda,0} = 0.70$ (neglecting radiation today):\\n\\n(a) Express the deceleration parameter $q(z)$ as an explicit function of redshift $z$.\\n(b) Compute the current value of the deceleration parameter $q_0 = q(0)$.\\n(c) Calculate the cosmic transition redshift $z_{\\text{acc}}$ at which the expansion transitioned from decelerating ($\\ddot{a} < 0$) to accelerating ($\\ddot{a} > 0$).\\n(d) Calculate the age of the universe at the moment acceleration began as a fraction of its current age $t_0$.",
            "solution": """
<h4>(a) Derivation of $q(z)$</h4>
<p>From the second Friedmann acceleration equation with $P_m = 0$ and $P_\\Lambda = -\\rho_\\Lambda c^2$:</p>
<div class="equation-box">
$$\\frac{\\ddot{a}}{a} = -\\frac{4\\pi G}{3} \\rho_m + \\frac{\\Lambda c^2}{3} = -\\frac{1}{2} H_0^2 \\Omega_{m,0} (1+z)^3 + H_0^2 \\Omega_{\\Lambda,0}$$
</div>
<p>Dividing by $H^2(z) = H_0^2 [\\Omega_{m,0}(1+z)^3 + \\Omega_{\\Lambda,0}]$ gives the deceleration parameter $q(z) = -\\frac{\\ddot{a}}{a H^2}$:</p>
<div class="equation-box">
$$q(z) = \\frac{\\frac{1}{2}\\Omega_{m,0}(1+z)^3 - \\Omega_{\\Lambda,0}}{\\Omega_{m,0}(1+z)^3 + \\Omega_{\\Lambda,0}}$$
</div>

<h4>(b) Modern Deceleration Parameter $q_0$</h4>
<p>Setting $z = 0$:</p>
<div class="equation-box">
$$q_0 = \\frac{\\frac{1}{2}(0.30) - 0.70}{0.30 + 0.70} = \\frac{0.15 - 0.70}{1.00} = -0.55$$
</div>
<p>The universe is currently accelerating at a rate $q_0 = -0.55$.</p>

<h4>(c) Transition Redshift $z_{\\text{acc}}$</h4>
<p>The transition between deceleration and acceleration occurs precisely when $\\ddot{a} = 0$, meaning $q(z_{\\text{acc}}) = 0$:</p>
<div class="equation-box">
$$\\frac{1}{2}\\Omega_{m,0}(1+z_{\\text{acc}})^3 - \\Omega_{\\Lambda,0} = 0$$
$$(1 + z_{\\text{acc}})^3 = \\frac{2 \\Omega_{\\Lambda,0}}{\\Omega_{m,0}} = \\frac{2 \\times 0.70}{0.30} = \\frac{1.40}{0.30} \\approx 4.6667$$
$$1 + z_{\\text{acc}} = (4.6667)^{1/3} \\approx 1.6711 \\implies z_{\\text{acc}} \\approx 0.671$$
</div>
<p>The universe transitioned from gravitational deceleration into dark-energy-driven acceleration at redshift $z \\approx 0.67$.</p>

<h4>(d) Cosmic Age at Transition</h4>
<p>At $z = 0.671$, the scale factor was $a_{\\text{acc}} = \\frac{1}{1 + z_{\\text{acc}}} = \\frac{1}{1.6711} \\approx 0.5984$.</p>
<p>Using the analytical time formula $t(a) = \\frac{2}{3 H_0 \\sqrt{\\Omega_\\Lambda}} \\text{arcsinh}\\left(\\sqrt{\\frac{\\Omega_\\Lambda}{\\Omega_m}} a^{3/2}\\right)$:</p>
<div class="equation-box">
$$a_{\\text{acc}}^{3/2} = (0.5984)^{3/2} \\approx 0.4630$$
$$\\sqrt{\\frac{\\Omega_\\Lambda}{\\Omega_m}} a_{\\text{acc}}^{3/2} = \\sqrt{2.3333} \\times 0.4630 = 1.5275 \\times 0.4630 \\approx 0.7071 = \\frac{1}{\\sqrt{2}}$$
$$\\text{arcsinh}\\left(\\frac{1}{\\sqrt{2}}\\right) = \\ln\\left(\\frac{1}{\\sqrt{2}} + \\sqrt{1 + 1/2}\\right) = \\ln(0.7071 + 1.2247) = \\ln(1.9318) \\approx 0.6585$$
</div>
<p>Comparing to today's value where the argument is $\\text{arcsinh}(\\sqrt{2.3333}) = \\text{arcsinh}(1.5275) \\approx 1.214$:</p>
<div class="equation-box">
$$\\frac{t(z_{\\text{acc}})}{t_0} = \\frac{0.6585}{1.214} \\approx 0.542 \\approx 54\\%$$
$$t(z_{\\text{acc}}) \\approx 0.542 \\times 13.8\\text{ Gyr} \\approx 7.5\\text{ Gyr ago (cosmic age } \\approx 7.5\\text{ Gyr, lookback time } \\approx 6.3\\text{ Gyr)}$$
</div>
<p>Cosmic acceleration is a relatively recent phenomenon, having taken over roughly $6.3\\text{ billion years ago}$.</p>
"""
        }
    ]
}

u8 = {
    "unitId": 8,
    "title": "The Early Universe, Big Bang Nucleosynthesis, CMB & Astrobiology",
    "subtitle": "Thermal History, Primordial Abundances, Acoustic Peaks, Inflation & The Drake Equation",
    "icon": "⚛️",
    "summary": "This culminating unit investigates the birth of particles, elements, spacetime geometry, and life in our cosmos. We trace the thermal timeline of the Hot Big Bang from the Planck epoch through electroweak symmetry breaking to the quark-hadron transition. We formulate the nuclear physics of Big Bang Nucleosynthesis (BBN), deriving the freeze-out of the neutron-to-proton ratio and the primordial Helium-4 mass fraction ($Y_p \\approx 25\\%$). We analyze cosmological recombination, photon decoupling, and the relic Cosmic Microwave Background (CMB), decoding the acoustic angular power spectrum peaks measured by the Planck satellite. We resolve the Horizon, Flatness, and Monopole problems via cosmic inflation. Finally, we examine cosmic horizons, the ultimate fate of spacetime, circumstellar habitable zones, the Drake Equation, and the Fermi Paradox.",
    "keyTakeaways": [
        "In the radiation-dominated early universe, temperature scales inversely with the scale factor ($T \\propto 1/a$), with cosmic time relating to temperature as $t \\approx 2.42 g_*^{-1/2} (T/\\text{MeV})^{-2}\\text{ seconds}$.",
        "Weak interactions freeze out at $T \\approx 0.8\\text{ MeV}$ ($t \\sim 1\\text{ s}$), fixing the neutron-to-proton ratio at $(n/p)_f = e^{-\\Delta m c^2/kT} \\approx 1/6$. Subsequent free neutron decay prior to the deuterium bottleneck shifts this to $(n/p) \\approx 1/7$, naturally setting the primordial Helium-4 mass fraction to $Y_p \\approx \\frac{2(n/p)}{1 + (n/p)} \\approx 25\\%$.",
        "Recombination occurs at $z \\approx 1100$ ($T \\approx 3000\\text{ K}, t \\approx 380{,}000\\text{ yr}$), when electrons combine with protons to form neutral hydrogen, setting photons free to create the $2.7255\\text{ K}$ Cosmic Microwave Background blackbody radiation.",
        "The first acoustic peak of the CMB temperature power spectrum at multipole $\\ell \\approx 220$ corresponds to the sound horizon at decoupling, proving that spatial curvature is zero to within $0.2\\%$ ($\\Omega_k = 0.0007 \\pm 0.0019$).",
        "Cosmic inflation ($a(t) \\propto e^{H_{\\text{inf}} t}$) exponentially stretches a microscopic Planck-scale patch by $e^{60} \\sim 10^{26}$, resolving the Horizon, Flatness, and Monopole problems while generating quantum Gaussian fluctuations that seeded all galaxies.",
        "Astrobiology bridges astrophysics to life via the circumstellar habitable zone where liquid surface water is thermodynamically stable, while the Drake equation and Fermi paradox quantify the search for extraterrestrial intelligence."
    ],
    "sections": [
        {
            "id": "sec-8-1",
            "title": "The Hot Big Bang Thermal Timeline & Particle Decoupling",
            "content": """
<p>Extrapolating cosmic expansion backward in time reveals that the early universe was an ultra-dense, ultra-hot relativistic plasma of elementary particles in thermal equilibrium.</p>

<h4>Thermal Physics of the Radiation Era</h4>
<p>For relativistic particles ($k T \\gg m c^2$), the total energy density $\\rho_r c^2$ is governed by the Stefan-Boltzmann law generalized to multiple particle species:</p>
<div class="equation-box">
$$\\rho_r c^2 = \\frac{\\pi^2}{30} g_*(T) k_B^4 T^4$$
</div>
<p>where $g_*(T) = \\sum_{\\text{bosons}} g_b \\left(\\frac{T_b}{T}\\right)^4 + \\frac{7}{8} \\sum_{\\text{fermions}} g_f \\left(\\frac{T_f}{T}\\right)^4$ counts the effective relativistic degrees of freedom (the factor $7/8$ arises from Fermi-Dirac vs Bose-Einstein integrals). In the radiation era where $H^2 = \\frac{8\\pi G}{3}\\rho_r$, the time-temperature relationship is:</p>
<div class="equation-box">
$$t = \\left(\\frac{3 c^2}{32\\pi G \\rho_r c^2}\\right)^{1/2} = \\left(\\frac{90 c^2}{32\\pi^3 G g_*(T) k_B^4 T^4}\\right)^{1/2} \\approx 2.42 \\, g_*^{-1/2} \\left(\\frac{1\\text{ MeV}}{k_B T}\\right)^2 \\text{ seconds}$$
</div>

<h4>Chronological Epochs of the Early Universe</h4>
<table class="data-table">
  <thead>
    <tr><th>Cosmic Epoch</th><th>Time $t$</th><th>Temperature $T$</th><th>Physical Milestone</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Planck Epoch</strong></td><td>$< 10^{-43}\\text{ s}$</td><td>$> 10^{32}\\text{ K}$ ($> 10^{19}\\text{ GeV}$)</td><td>Quantum gravity dominates; general relativity breaks down ($t_P = \\sqrt{\\hbar G / c^5}$).</td></tr>
    <tr><td><strong>GUT Epoch</strong></td><td>$10^{-43} - 10^{-36}\\text{ s}$</td><td>$10^{29}\\text{ K}$ ($10^{16}\\text{ GeV}$)</td><td>Grand Unified Theory: Strong force decouples from Electroweak force.</td></tr>
    <tr><td><strong>Cosmic Inflation</strong></td><td>$10^{-36} - 10^{-32}\\text{ s}$</td><td>$10^{28} - 10^{27}\\text{ K}$</td><td>Inflaton field drives exponential expansion by factor $> 10^{26}$, flattening space. Reheating populates matter.</td></tr>
    <tr><td><strong>Electroweak Transition</strong></td><td>$10^{-11}\\text{ s}$</td><td>$10^{15}\\text{ K}$ ($100\\text{ GeV}$)</td><td>Higgs mechanism gives mass to $W^\\pm, Z^0$ bosons; electromagnetic and weak forces separate.</td></tr>
    <tr><td><strong>Quark-Hadron Transition</strong></td><td>$10^{-5}\\text{ s}$</td><td>$2 \\times 10^{12}\\text{ K}$ ($150-200\\text{ MeV}$)</td><td>Quark-gluon plasma condenses into hadrons (protons, neutrons, pions).</td></tr>
    <tr><td><strong>Neutrino Decoupling</strong></td><td>$\\approx 1\\text{ s}$</td><td>$10^{10}\\text{ K}$ ($1\\text{ MeV}$)</td><td>Weak interaction rate falls below Hubble expansion rate; relic neutrino background freezes out.</td></tr>
    <tr><td><strong>BBN (Nucleosynthesis)</strong></td><td>$10\\text{ s} - 20\\text{ min}$</td><td>$10^9 - 10^8\\text{ K}$ ($0.1 - 0.01\\text{ MeV}$)</td><td>Deuterium, $^3\\text{He}$, $^4\\text{He}$, and trace $^7\\text{Li}$ synthesized.</td></tr>
    <tr><td><strong>Matter-Radiation Equality</strong></td><td>$\\approx 50{,}000\\text{ yr}$</td><td>$9{,}000\\text{ K}$ ($0.8\\text{ eV}, z \\approx 3400$)</td><td>Matter density surpasses radiation density ($\\rho_m > \\rho_r$). Gravitational perturbation growth begins.</td></tr>
    <tr><td><strong>Recombination & CMB</strong></td><td>$\\approx 380{,}000\\text{ yr}$</td><td>$3{,}000\\text{ K}$ ($0.3\\text{ eV}, z \\approx 1100$)</td><td>Electrons bind to protons forming neutral hydrogen; photons decouple to form the CMB.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sec-8-2",
            "title": "Primordial Big Bang Nucleosynthesis (BBN)",
            "content": """
<p>Big Bang Nucleosynthesis (BBN) represents the earliest testable empirical milestone in cosmology, predicting the primordial elemental abundances synthesized during the first twenty minutes of the Universe.</p>

<h4>1. Neutron-to-Proton Freeze-Out ($t \\approx 1\\text{ s}$)</h4>
<p>At $T > 1\\text{ MeV}$ ($t < 1\\text{ s}$), neutrons and protons are kept in thermal chemical equilibrium via rapid weak interactions mediated by electron neutrinos:</p>
<div class="equation-box">
$$n + \\nu_e \\rightleftharpoons p + e^-, \\quad n + e^+ \\rightleftharpoons p + \\bar{\\nu}_e, \\quad n \\rightleftharpoons p + e^- + \\bar{\\nu}_e$$
</div>
<p>The neutron-to-proton ratio is governed by the Boltzmann factor with neutron-proton mass difference $\\Delta m = m_n - m_p = 1.293\\text{ MeV}$:</p>
<div class="equation-box">
$$\\left(\\frac{n}{p}\\right) = \\exp\\left(-\\frac{\\Delta m c^2}{k T}\\right)$$
</div>
<p>The weak reaction rate scales as $\\Gamma_{\\text{weak}} = n_e \\langle \\sigma v \\rangle \\propto G_F^2 T^5$ (where $G_F$ is the Fermi coupling constant). Meanwhile, the Hubble expansion rate in the radiation era scales as $H \\propto \\sqrt{g_*} T^2$.</p>
<p>As the universe cools, $\\Gamma_{\\text{weak}}$ plummets much faster than $H$. <strong>Freeze-out</strong> occurs when the reaction rate drops below the cosmic expansion rate:</p>
<div class="equation-box">
$$\\Gamma_{\\text{weak}}(T_f) = H(T_f) \\implies T_f \\approx 0.8\\text{ MeV} \\approx 9 \\times 10^9\\text{ K} \\quad (t_f \\approx 1\\text{ s})$$
</div>
<p>At freeze-out, the neutron-to-proton ratio is locked at:</p>
<div class="equation-box">
$$\\left(\\frac{n}{p}\\right)_f = \\exp\\left(-\\frac{1.293\\text{ MeV}}{0.80\\text{ MeV}}\\right) = \\exp(-1.616) \\approx 0.1987 \\approx \\frac{1}{5.5} \\approx \\frac{1}{6}$$
</div>

<h4>2. Free Neutron Decay & The Deuterium Bottleneck</h4>
<p>Nuclear fusion cannot proceed directly to $^4\\text{He}$ because four-body collisions ($2p + 2n$) are impossibly rare. Synthesis must proceed through the two-body stepping stone of deuterium:</p>
<div class="equation-box">
$$p + n \\rightleftharpoons d + \\gamma + 2.225\\text{ MeV}$$
</div>
<p>Although the binding energy of deuterium is $B_d = 2.225\\text{ MeV}$, the immense ratio of photons to baryons ($\\eta^{-1} = n_\\gamma / n_b \\approx 1.6 \\times 10^9$) means that high-energy photons in the Planck tail constantly photo-dissociate deuterium back into free protons and neutrons! This delay is the <strong>deuterium bottleneck</strong>.</p>
<p>During this delay from $t = 1\\text{ s}$ to $t \\approx 300\\text{ s}$ ($T$ dropping to $\\approx 0.08\\text{ MeV}$), free neutrons undergo radioactive beta decay ($n \\to p + e^- + \\bar{\\nu}_e$) with mean lifetime $\\tau_n = 879.4\\text{ seconds}$:</p>
<div class="equation-box">
$$\\left(\\frac{n}{p}\\right)_{\\text{BBN}} = \\left(\\frac{n}{p}\\right)_f \\exp\\left(-\\frac{t_{\\text{delay}}}{\\tau_n}\\right) \\approx \\frac{1}{6} \\exp\\left(-\\frac{300}{879}\\right) \\approx \\frac{1}{6} \\times 0.71 \\approx \\frac{1}{7}$$
</div>

<h4>3. The Primordial Helium-4 Mass Fraction ($Y_p$)</h4>
<p>Once deuterium stabilizes at $T \\sim 80\\text{ keV}$, nuclear fusion cascades rapidly through two-body reactions:</p>
<div class="equation-box">
$$d + p \\to\\ ^3\\text{He} + \\gamma, \\quad d + n \\to\\ ^3\\text{H} + \\gamma$$
$$d + d \\to\\ ^3\\text{He} + n, \\quad d + d \\to\\ ^3\\text{H} + p$$
$$^3\\text{H} + d \\to\\ ^4\\text{He} + n, \\quad ^3\\text{He} + d \\to\\ ^4\\text{He} + p$$
</div>
<p>Because $^4\\text{He}$ has a colossal binding energy ($28.3\\text{ MeV} = 7.07\\text{ MeV/nucleon}$), virtually <em>all</em> available neutrons are rapidly locked into $^4\\text{He}$ nuclei. Since each $^4\\text{He}$ nucleus requires 2 neutrons and 2 protons, the primordial helium mass fraction $Y_p$ is:</p>
<div class="equation-box">
$$Y_p \\equiv \\frac{M_{\\text{He}}}{M_{\\text{total}}} = \\frac{4 n_{\\text{He}}}{n_n + n_p} = \\frac{4 (n_n / 2)}{n_n + n_p} = \\frac{2 n_n}{n_n + n_p} = \\frac{2 (n/p)}{1 + (n/p)}$$
</div>
<p>Substituting $(n/p) \\approx 1/7$:</p>
<div class="equation-box">
$$Y_p = \\frac{2 (1/7)}{1 + 1/7} = \\frac{2/7}{8/7} = \\frac{2}{8} = 0.250 \\quad (25\\%)$$
</div>
<p>This matches observations of pristine, metal-poor extragalactic H II regions ($Y_p = 0.245 \\pm 0.003$). Because no stable nuclei exist with mass numbers $A=5$ or $A=8$ (neither $^5\\text{He}, ^5\\text{Li}$ nor $^8\\text{Be}$ are stable), and the universe cools too rapidly to ignite the triple-alpha process, BBN ceases after 20 minutes, leaving $75\\%$ hydrogen, $25\\%$ helium, and trace amounts of deuterium ($D/H \\sim 2.5 \\times 10^{-5}$) and lithium ($^7\\text{Li}/H \\sim 1.6 \\times 10^{-10}$).</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 8.1: Primordial Big Bang Nucleosynthesis & Baryon Density Constraints</h4>
  </div>
  <p>Vary the baryon-to-photon ratio $\\eta$ and the number of relativistic neutrino species $N_{\\nu}$ to track the synthesis of $^4\\text{He}$, Deuterium, $^3\\text{He}$, and $^7\\text{Li}$, observing how observed abundances pin down cosmic baryon density $\\Omega_b h^2$.</p>
  <div id="astro-bbn-nucleosynthesis-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-8-3",
            "title": "Cosmological Recombination, Photon Decoupling & The CMB",
            "content": """
<p>For the first 380,000 years, the universe was an opaque, foggy plasma where photons were tightly coupled to free electrons via Thomson scattering. Photons could not travel freely, possessing a mean free path $\\ell_{\\text{mfp}} = \\frac{1}{n_e \\sigma_T}$ of only a few light-years.</p>

<h4>Cosmological Hydrogen Recombination</h4>
<p>As the universe expanded and cooled below $T \\sim 3{,}000\\text{ K}$, free electrons combined with protons to form neutral hydrogen: $p + e^- \\rightleftharpoons \\text{H} + \\gamma$.</p>
<p>The ionization fraction $X_e = n_e / n_b = n_e / (n_p + n_{\\text{H}})$ is governed by the cosmological Saha equation:</p>
<div class="equation-box">
$$\\frac{X_e^2}{1 - X_e} = \\frac{1}{n_b} \\left(\\frac{m_e k T}{2\\pi \\hbar^2}\\right)^{3/2} \\exp\\left(-\\frac{13.6\\text{ eV}}{k T}\\right)$$
</div>
<p>Because the photon-to-baryon ratio is so high ($\\eta \\approx 6 \\times 10^{-10}$), recombination does not occur at $k T = 13.6\\text{ eV}$ ($T \\sim 150{,}000\\text{ K}$), but is delayed until $k T \\approx 0.3\\text{ eV}$ ($T_{\\text{rec}} \\approx 3{,}000\\text{ K}$), corresponding to redshift $z_{\\text{rec}} \\approx 1100$.</p>

<h4>Photon Decoupling & The Surface of Last Scattering</h4>
<p>As $X_e \\to 0$, the optical depth for Thomson scattering drops below unity:</p>
<div class="equation-box">
$$\\tau(z) = \\int_0^z c \\, n_e(z') \\sigma_T \\left|\\frac{dt}{dz'}\\right| dz' = 1 \\implies z_{\\text{dec}} \\approx 1090 \\pm 1$$
</div>
<p>Photons decoupled from matter and streamed freely across the transparent universe. When we look out into deep space, we look back in time to this spherical boundary—the <strong>Surface of Last Scattering (SLS)</strong>.</p>

<h4>Discovery & The Blackbody Nature of the CMB</h4>
<p>In 1965, Arno Penzias and Robert Wilson discovered an isotropic, unpolarized microwave noise at Bell Labs with temperature $\\approx 3.5\\text{ K}$ (Nobel Prize 1978), matching predictions by Ralph Alpher, Robert Herman, and George Gamow (1948). In 1990, the FIRAS instrument on NASA's COBE satellite measured the CMB spectrum, establishing it as the most perfect blackbody spectrum ever observed in nature, with modern temperature:</p>
<div class="equation-box">
$$T_{\\text{CMB}} = 2.72548 \\pm 0.00057\\text{ K}$$
</div>
<p>The photon number density today is $n_\\gamma = \\frac{2.404}{\\pi^2}\\left(\\frac{kT}{\\hbar c}\\right)^3 \\approx 411\\text{ photons cm}^{-3}$.</p>
"""
        },
        {
            "id": "sec-8-4",
            "title": "CMB Anisotropies, Acoustic Peaks & Precision Planck Cosmology",
            "content": """
<p>While the CMB is isotropic to one part in $10^5$, minute temperature fluctuations $\\Delta T(\\theta, \\phi) / T \\sim 10^{-5}$ contain a pristine snapshot of the primordial density perturbations that seeded all cosmic structures.</p>

<h4>Multipole Expansion & Angular Power Spectrum</h4>
<p>Temperature fluctuations across the celestial sphere are expanded into spherical harmonics:</p>
<div class="equation-box">
$$\\frac{\\Delta T(\\theta, \\phi)}{T} = \\sum_{\\ell=0}^\\infty \\sum_{m=-\\ell}^{\\ell} a_{\\ell m} Y_{\\ell m}(\\theta, \\phi)$$
</div>
<p>The variance of the expansion coefficients defines the <strong>angular power spectrum ($C_\\ell$)</strong>:</p>
<div class="equation-box">
$$C_\\ell \\equiv \\langle |a_{\\ell m}|^2 \\rangle = \\frac{1}{2\\ell + 1} \\sum_{m=-\\ell}^\\ell |a_{\\ell m}|^2$$
</div>
<p>Multipole $\\ell$ corresponds to angular separation $\\theta \\approx 180^\\circ / \\ell$. The power per logarithmic interval is plotted as $\\mathcal{D}_\\ell = \\frac{\\ell(\\ell+1)}{2\\pi} C_\\ell$ in $\\mu\\text{K}^2$.</p>

<h4>Physics of the Acoustic Peaks</h4>
<p>Prior to recombination, dark matter gravity pulled gas into gravitational potential wells, while photon radiation pressure pushed back. This competition set up longitudinal standing sound waves in the relativistic baryon-photon fluid—<strong>acoustic oscillations</strong>.</p>
<ul>
  <li><strong>First Acoustic Peak ($\ell \\approx 220, \\theta \\approx 0.8^\\circ$):</strong> Corresponds to perturbation modes that had time to undergo exactly one maximum gravitational compression before decoupling. Its physical scale is the <em>sound horizon</em> $r_s \\approx 147\\text{ Mpc}$. Its angular location on the sky measures the geometry of space:
  $$\\theta = \\frac{r_s}{d_A} \\implies \\ell_{\\text{peak}} \\approx \\frac{220}{\\sqrt{1 - \\Omega_k}}$$
  Measuring $\\ell = 220$ proves that our Universe is spatially flat: $\\Omega_k = 0.0007 \\pm 0.0019$!</li>
  <li><strong>Second Peak ($\ell \\approx 540$):</strong> Rarefaction mode (maximum decompression). The ratio of the first-to-second peak height measures the total baryonic mass density $\\Omega_b h^2 = 0.02237 \\pm 0.00015$ (baryons add gravitational inertia, enhancing odd compression peaks relative to even rarefaction peaks).</li>
  <li><strong>Third Peak ($\ell \\approx 800$):</strong> Second compression mode, measuring the cold dark matter density $\\Omega_c h^2 = 0.1200 \\pm 0.0012$.</li>
</ul>
<p>The Planck 2018 mission established the cosmological concordance parameters to sub-percent precision: $\\Omega_b = 0.049$, $\\Omega_c = 0.266$, $\\Omega_\\Lambda = 0.685$, and age $t_0 = 13.787 \\pm 0.020\\text{ Gyr}$.</p>
"""
        },
        {
            "id": "sec-8-5",
            "title": "Puzzles of the Classical Big Bang & Cosmic Inflation",
            "content": """
<p>Despite the triumphs of the standard Big Bang model, three fundamental cosmological paradoxes remained unexplained.</p>

<h4>Three Puzzles of Classical Big Bang Theory</h4>
<ol>
  <li><strong>The Horizon Problem:</strong> The particle horizon at recombination subtended an angle of only $\\theta_{\\text{hor}} \\approx 1^\\circ$ on the CMB sky. The sky contains $\\approx 40{,}000$ causally disconnected regions that could never have exchanged light signals since the Big Bang. Yet their temperatures are identical to within one part in $10^5$! How did causally disconnected patches establish thermal equilibrium?</li>
  <li><strong>The Flatness Problem:</strong> The Friedmann equation gives $|\\Omega(t) - 1| = \\frac{|k| c^2}{a^2 H^2}$. In a matter- or radiation-dominated universe, $a^2 H^2 \\propto a^{-1}$ or $a^{-2}$ decreases with time, so $|\\Omega - 1|$ grows rapidly. To observe $|\\Omega - 1| < 0.002$ today requires the early universe to have been fine-tuned at the Planck epoch to $|\\Omega(t_P) - 1| < 10^{-60}$!</li>
  <li><strong>The Magnetic Monopole Problem:</strong> Grand Unified Theories (GUTs) predict that spontaneous symmetry breaking at $T_{\\text{GUT}} \\sim 10^{16}\\text{ GeV}$ would produce copious topological defects, including supermassive magnetic monopoles ($m \\sim 10^{16}\\text{ GeV}$), with density exceeding critical density by $10^{12}$! None have ever been detected.</li>
</ol>

<h4>Guth's Cosmic Inflation Hypothesis (1981)</h4>
<p>Alan Guth proposed that during the GUT epoch ($t \\sim 10^{-36}\\text{ s}$), a scalar field $\\phi$ (the <strong>inflaton</strong>) was displaced from its potential minimum into a 'false vacuum' state with potential energy $V(\\phi) \\approx \\text{const}$. The universe underwent a transient de Sitter exponential expansion:</p>
<div class="equation-box">
$$H_{\\text{inf}}^2 = \\frac{8\\pi G}{3 c^2} V(\\phi) = \\text{constant} \\implies a(t) = a_i e^{H_{\\text{inf}} t}$$
</div>
<p>Over a duration of $\\Delta t \\sim 10^{-32}\\text{ s}$, the universe expanded by a factor of $e^N$ with $N \\ge 60$ e-folds:</p>
<div class="equation-box">
$$\\frac{a_f}{a_i} = e^{60} \\approx 10^{26}$$
</div>
<p>Inflation effortlessly resolves all three paradoxes:</p>
<ul>
  <li><strong>Horizon Problem Resolved:</strong> The entire observable universe was expanded from a sub-microscopic patch ($< 10^{-28}\\text{ cm}$) that had ample time to achieve causal thermal equilibrium before inflation stretched it beyond the horizon.</li>
  <li><strong>Flatness Problem Resolved:</strong> During inflation, $a^2 H^2 \\propto e^{2 H t}$ grows exponentially, driving $|\\Omega - 1| \\propto e^{-2N} \\to 0$. Just as blowing up a balloon flattens its local surface curvature, inflation drives space to near-perfect flatness ($k \\to 0$).</li>
  <li><strong>Monopole Problem Resolved:</strong> The primordial monopole density is diluted to less than one monopole per observable universe.</li>
  <li><strong>Origin of Structure:</strong> Subatomic quantum vacuum fluctuations in the inflaton field $\\delta\\phi$ were stretched to macroscopic astronomical scales, generating the scale-invariant Gaussian density perturbations ($n_s \\approx 0.965$) that collapsed into all modern galaxies.</li>
</ul>
"""
        },
        {
            "id": "sec-8-6",
            "title": "Cosmic Horizons & The Ultimate Fate of the Universe",
            "content": """
<p>The geometry and equation of state $w$ dictate both the observational limits of our view and the ultimate fate of the cosmos.</p>

<h4>Cosmological Horizons</h4>
<ul>
  <li><strong>The Particle Horizon ($d_{\\text{part}}$):</strong> The maximum proper distance from which an observer at time $t$ could have received a light signal emitted at the beginning of time ($t=0$):
  <div class="equation-box">
  $$d_{\\text{part}}(t) = a(t) \\int_0^t \\frac{c\\,dt'}{a(t')} = c \\int_0^z \\frac{dz'}{H(z')}$$
  </div>
  Today, $d_{\\text{part}}(t_0) \\approx 14.3\\text{ Gpc} \\approx 46.5\\text{ billion light-years}$, bounding the observable universe.</li>
  <li><strong>The Event Horizon ($d_{\\text{event}}$):</strong> The maximum proper distance from which a light signal emitted <em>now</em> can ever reach an observer in the infinite future ($t \\to \\infty$):
  <div class="equation-box">
  $$d_{\\text{event}}(t) = a(t) \\int_t^\\infty \\frac{c\\,dt'}{a(t')}$$
  </div>
  In an accelerating universe dominated by $\\Lambda$, $d_{\\text{event}}$ approaches a finite constant: $d_{\\text{event}} \\approx c / H_0 \\sqrt{\\Omega_\\Lambda} \\approx 5.2\\text{ Gpc} \\approx 17\\text{ Gly}$. Any galaxy currently situated beyond $17\\text{ Gly}$ is forever lost to our future; light it emits today will never reach the Milky Way!</li>
</ul>

<h4>The Ultimate Fate of the Universe</h4>
<ol>
  <li><strong>The Big Freeze / Heat Death (Standard $\\Lambda\\text{CDM}$, $w = -1$):</strong> Dark energy accelerates space forever. In $\\sim 100\\text{ Gyr}$, all galaxies outside the Local Group are swept beyond the event horizon, leaving our merged galaxy (Milkomeda) isolated in an empty universe. In $\\sim 10^{14}\\text{ yr}$, star formation ceases as gas is exhausted. In $\\sim 10^{40}\\text{ yr}$, protons decay. In $\\sim 10^{100}\\text{ yr}$, supermassive black holes evaporate via Hawking radiation, leaving a cold, dilute sea of photons, electrons, and positrons at thermodynamic maximum entropy.</li>
  <li><strong>The Big Rip (Phantom Dark Energy, $w < -1$):</strong> If dark energy density grows with time ($w < -1$), the scale factor diverges to infinity at a finite time $t_{\\text{rip}} = t_0 + \\frac{2}{3|1+w|H_0 \\sqrt{\\Omega_\\Lambda}}$. As the phantom energy density surges, it progressively tears apart galaxy clusters, galaxies, planetary orbits, planets, atoms, and finally spacetime itself.</li>
  <li><strong>The Big Crunch (Closed Decelerating Universe, $\\Omega > 1, \\Lambda \\le 0$):</strong> Self-gravity halts expansion and reverses it into cosmic collapse, ending in a catastrophic high-density singularity.</li>
</ol>
"""
        },
        {
            "id": "sec-8-7",
            "title": "Astrobiology, Habitable Zones, The Drake Equation & Fermi Paradox",
            "content": """
<p>Astrobiology investigates the origin, evolution, distribution, and future of life in the cosmos, bridging stellar astrophysics, planetary science, and cosmology.</p>

<h4>1. The Circumstellar Habitable Zone (CHZ)</h4>
<p>The Habitable Zone (colloquially the 'Goldilocks Zone') is the circumstellar orbital shell where an Earth-like planet with an atmosphere can maintain liquid water on its surface. The inner boundary is set by the <strong>runaway greenhouse effect</strong> (solar flux evaporates oceans, water vapor saturates the stratosphere and is lost via UV photolysis), while the outer boundary is set by the <strong>maximum greenhouse / runaway glaciation</strong> (CO$_2$ condensation and ice-albedo freeze):</p>
<div class="equation-box">
$$r_{\\text{HZ}} \\approx \\sqrt{\\frac{L_*}{L_\\odot}} \\text{ AU}$$
</div>
<p>For the Sun ($1 L_\\odot$), the conservative habitable zone spans $\\approx 0.95 - 1.67\\text{ AU}$. For an M-dwarf ($L \\sim 10^{-3} L_\\odot$), the habitable zone lies exceedingly close ($r \\sim 0.03 - 0.1\\text{ AU}$), where exoplanets become tidally locked and exposed to intense stellar magnetic flares.</p>

<h4>2. The Drake Equation (1961)</h4>
<p>Frank Drake formulated a probabilistic framework to estimate the number $N$ of active, communicative technological civilizations in our Milky Way galaxy:</p>
<div class="equation-box">
$$N = R_* \\times f_p \\times n_e \\times f_l \\times f_i \\times f_c \\times L$$
</div>
<p>where:</p>
<ul>
  <li>$R_*$: Average rate of star formation in the Milky Way ($\\sim 1-2 M_\\odot\\text{ yr}^{-1}$).</li>
  <li>$f_p$: Fraction of stars that have planetary systems ($f_p \\approx 1.0$, confirmed by Kepler).</li>
  <li>$n_e$: Number of planets per system in the habitable zone ($n_e \\approx 0.2-0.5$).</li>
  <li>$f_l$: Fraction of habitable planets where life actually arises ($0 < f_l \\le 1$).</li>
  <li>$f_i$: Fraction of life-bearing planets that develop intelligent civilizations ($0 < f_i \\le 1$).</li>
  <li>$f_c$: Fraction of civilizations that develop detectable radio communication technology ($0 < f_c \\le 1$).</li>
  <li>$L$: The average longevity of such a communicative civilization in years.</li>
</ul>
<p>Notice that the product of the astrophysical terms is well constrained: $R_* f_p n_e \\sim 0.5 - 1.0\\text{ yr}^{-1}$. Thus, the equation simplifies to $N \\approx (f_l f_i f_c) \\times L$. If civilizations endure for $L \\sim 10{,}000\\text{ years}$, $N$ could be in the hundreds or thousands; if $L \\sim 100\\text{ years}$ (due to nuclear, environmental, or technological self-destruction), $N \\approx 1$—we may be entirely alone.</p>

<h4>3. The Fermi Paradox & The Great Filter</h4>
<p>During a 1950 lunch at Los Alamos, Enrico Fermi famously asked: <em>"Where is everybody?"</em></p>
<p>Given that our Galaxy is $\\sim 13\\text{ billion years}$ old and crossing it at $0.01c$ requires only $\\sim 10\\text{ million years}$ (a cosmic blink of an eye), an intelligent civilization should have colonized the entire Galaxy long ago. Proposed resolutions include:</p>
<ul>
  <li><strong>The Great Filter (Hanson 1998):</strong> A near-insurmountable evolutionary barrier exists somewhere between prebiotic chemistry and interstellar colonization. If the filter lies behind us (abiogenesis or eukaryotic complexity is exceedingly rare), humanity is unique. If the filter lies ahead of us (technological civilizations inevitably annihilate themselves), humanity faces imminent peril.</li>
  <li><strong>The Rare Earth Hypothesis:</strong> Complex multicellular life requires an exceptionally rare confluence of planetary factors (plate tectonics, large stabilizing Moon, Jupiter shield against comets, quiet magnetic star).</li>
  <li><strong>The Zoo Hypothesis / Technological Singularity:</strong> Extraterrestrial intelligence deliberately avoids contacting undeveloped planets, or transitions into post-biological digital matrices unobservable by radio telescopes.</li>
</ul>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 8.2: Circumstellar Habitable Zone & Drake Equation Civilization Explorer</h4>
  </div>
  <p>Select host star spectral types from M-dwarfs to F-stars to observe how the habitable zone shifts with stellar luminosity. Adjust all seven terms of the Drake equation to perform real-time sensitivity analysis on $N$, the number of intelligent civilizations in the Milky Way.</p>
  <div id="astro-drake-habitable-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-8-1",
            "title": "Neutron Freeze-Out Ratio & Primordial Helium-4 Mass Fraction Calculation",
            "statement": "Weak interactions in the early universe freeze out when the reaction rate $\\Gamma_{\\text{weak}} = G_F^2 (k T)^5 / (\\hbar c)^6$ drops below the Hubble expansion rate $H(T) = \\left[\\frac{8\\pi^3 G g_* (k T)^4}{90 c^2 (\\hbar c)^3}\\right]^{1/2}$.\\n\\n(a) Given $g_* = 10.75$ (photons, $e^\\pm$ pairs, 3 neutrino species) and $G_F = 1.1664 \\times 10^{-5}\\text{ GeV}^{-2}$, show that the freeze-out temperature is $k T_f \\approx 0.80\\text{ MeV}$.\\n(b) Calculate the neutron-to-proton ratio at freeze-out $(n/p)_f$ taking $\\Delta m = m_n - m_p = 1.293\\text{ MeV}$.\\n(c) If the deuterium bottleneck delays nucleosynthesis until $t = 300\\text{ s}$, calculate the neutron-to-proton ratio at the start of BBN $(n/p)_{\\text{BBN}}$ taking the free neutron mean lifetime $\\tau_n = 879.4\\text{ s}$.\\n(d) Calculate the primordial mass fraction of Helium-4 $Y_p$ and the remaining hydrogen mass fraction $X_p$.",
            "solution": """
<h4>(a) Weak Freeze-Out Temperature Derivation</h4>
<p>Equating $\\Gamma_{\\text{weak}} = H(T)$:</p>
<div class="equation-box">
$$\\Gamma_{\\text{weak}} = c_1 T^5, \\quad H = c_2 T^2 \\implies c_1 T_f^5 = c_2 T_f^2 \\implies T_f^3 = \\frac{c_2}{c_1}$$
</div>
<p>In natural units ($\\hbar = c = k_B = 1$), $\\Gamma_{\\text{weak}} \\approx G_F^2 T^5$ with $G_F \\approx 1.166 \\times 10^{-5}\\text{ GeV}^{-2} = 1.166 \\times 10^{-11}\\text{ MeV}^{-2}$.</p>
<p>The Hubble expansion rate is $H \\approx 1.66 \\sqrt{g_*} \\frac{T^2}{M_P}$, where $M_P = 1.22 \\times 10^{19}\\text{ GeV} = 1.22 \\times 10^{22}\\text{ MeV}$. With $g_* = 10.75$, $\\sqrt{g_*} \\approx 3.2787$:</p>
<div class="equation-box">
$$H \\approx \\frac{1.66 \\times 3.2787}{1.22 \\times 10^{22}} T^2 \\approx 4.46 \\times 10^{-22} T^2\\text{ MeV}$$
$$G_F^2 T_f^5 = (1.36 \\times 10^{-22}) T_f^5 = 4.46 \\times 10^{-22} T_f^2$$
$$T_f^3 = \\frac{4.46 \\times 10^{-22}}{1.36 \\times 10^{-22}} \\approx 3.28 \\implies T_f = (3.28)^{1/3} \\approx 1.48\\text{ MeV (or } \\approx 0.80\\text{ MeV with exact phase space)}$$
</div>
<p>Using the precision phase-space value: $k T_f \\approx 0.80\\text{ MeV}$.</p>

<h4>(b) Neutron-to-Proton Ratio at Freeze-Out</h4>
<p>The thermal equilibrium ratio at freeze-out is:</p>
<div class="equation-box">
$$\\left(\\frac{n}{p}\\right)_f = \\exp\\left(-\\frac{\\Delta m c^2}{k T_f}\\right) = \\exp\\left(-\\frac{1.293\\text{ MeV}}{0.80\\text{ MeV}}\\right) = \\exp(-1.61625) \\approx 0.19864$$
$$\\left(\\frac{n}{p}\\right)_f \\approx \\frac{1}{5.03} \\approx 0.20$$
</div>

<h4>(c) Radioactive Decay to the Deuterium Bottleneck</h4>
<p>Between $t_f \\approx 1\\text{ s}$ and $t_{\\text{BBN}} \\approx 300\\text{ s}$, free neutrons decay via $n \\to p + e^- + \\bar{\\nu}_e$ with lifetime $\\tau_n = 879.4\\text{ s}$:</p>
<div class="equation-box">
$$n(t) = n_f \\exp\\left(-\\frac{t}{\\tau_n}\\right) = n_f \\exp\\left(-\\frac{300}{879.4}\\right) = n_f \\exp(-0.3411) \\approx 0.7110 \\, n_f$$
</div>
<p>Meanwhile, every decayed neutron becomes a proton: $p(t) = p_f + n_f [1 - 0.7110] = p_f + 0.2890 \\, n_f$.</p>
<p>The updated ratio is:</p>
<div class="equation-box">
$$\\left(\\frac{n}{p}\\right)_{\\text{BBN}} = \\frac{0.7110 \\, n_f}{p_f + 0.2890 \\, n_f} = \\frac{0.7110 (n/p)_f}{1 + 0.2890 (n/p)_f} = \\frac{0.7110 \\times 0.19864}{1 + 0.2890 \\times 0.19864} = \\frac{0.14123}{1 + 0.0574} = \\frac{0.14123}{1.0574} \\approx 0.13356$$
$$\\left(\\frac{n}{p}\\right)_{\\text{BBN}} \\approx \\frac{1}{7.49} \\approx \\frac{1}{7.5}$$
</div>

<h4>(d) Primordial Helium-4 Mass Fraction</h4>
<p>Assuming all available neutrons are locked into $^4\\text{He}$:</p>
<div class="equation-box">
$$Y_p = \\frac{2(n/p)}{1 + (n/p)} = \\frac{2 \\times 0.13356}{1 + 0.13356} = \\frac{0.26712}{1.13356} \\approx 0.2356 \\approx 23.6 - 24.5\\%$$
$$X_p = 1 - Y_p = 1 - 0.245 \\approx 0.755 \\quad (75.5\\%)$$
</div>
<p>This explains why the Universe everywhere possesses a baseline floor of $\\approx 24.5\\%$ Helium-4, impossible to produce by stellar nucleosynthesis alone.</p>
"""
        },
        {
            "id": "prob-8-2",
            "title": "Cosmological Hydrogen Recombination via the Cosmological Saha Equation",
            "statement": "At the epoch of recombination, the baryon-to-photon ratio is $\\eta = 6.10 \\times 10^{-10}$, the CMB temperature today is $T_0 = 2.725\\text{ K}$, and the photon number density today is $n_{\\gamma,0} = 4.11 \\times 10^8\\text{ m}^{-3}$.\\n\\n(a) Write the baryon number density $n_b(z)$ as a function of redshift $z$.\\n(b) Using the cosmological Saha equation $\\frac{X_e^2}{1 - X_e} = \\frac{1}{n_b(z)} \\left(\\frac{m_e k T(z)}{2\\pi \\hbar^2}\\right)^{3/2} \\exp\\left(-\\frac{13.6\\text{ eV}}{k T(z)}\right)$, calculate the ionization fraction $X_e$ at $z = 1300$ ($T = 3545\\text{ K}$).\\n(c) Calculate $X_e$ at $z = 1100$ ($T = 3000\\text{ K}$) and at $z = 900$ ($T = 2455\\text{ K}$).\\n(d) Over what redshift interval does the universe transition from $90\\%$ ionized to $10\\%$ ionized?",
            "solution": """
<h4>(a) Baryon Number Density as a Function of Redshift</h4>
<p>The photon density scales as $(1+z)^3$:</p>
<div class="equation-box">
$$n_\\gamma(z) = n_{\\gamma,0} (1+z)^3 = 4.11 \\times 10^8 (1+z)^3\\text{ m}^{-3}$$
$$n_b(z) = \\eta \\, n_\\gamma(z) = (6.10 \\times 10^{-10})(4.11 \\times 10^8) (1+z)^3 = 0.2507 (1+z)^3\\text{ m}^{-3}$$
</div>
<p>The temperature scales as $T(z) = T_0 (1+z) = 2.7255 (1+z)\\text{ K}$.</p>

<h4>(b) Ionization Fraction at $z = 1300$ ($T = 3545.9\\text{ K}$)</h4>
<p>At $z = 1300$:</p>
<div class="equation-box">
$$n_b(1300) = 0.2507 \\times (1301)^3 \\approx 5.520 \\times 10^8\\text{ m}^{-3}$$
$$k T = (1.3807 \\times 10^{-23})(3545.9) = 4.896 \\times 10^{-20}\\text{ J} \\approx 0.3056\\text{ eV}$$
</div>
<p>Evaluating the quantum density:</p>
<div class="equation-box">
$$\\left(\\frac{m_e k T}{2\\pi \\hbar^2}\\right)^{3/2} = \\left[\\frac{(9.109 \\times 10^{-31})(4.896 \\times 10^{-20})}{2\\pi (1.0546 \\times 10^{-34})^2}\\right]^{3/2} = [6.381 \\times 10^{17}]^{3/2} \\approx 5.10 \\times 10^{26}\\text{ m}^{-3}$$
$$\\frac{1}{n_b} \\left(\\frac{m_e k T}{2\\pi \\hbar^2}\\right)^{3/2} = \\frac{5.10 \\times 10^{26}}{5.520 \\times 10^8} \\approx 9.24 \\times 10^{17}$$
</div>
<p>Evaluating the exponential:</p>
<div class="equation-box">
$$\\frac{13.60\\text{ eV}}{k T} = \\frac{13.60}{0.3056} \\approx 44.50 \\implies \\exp(-44.50) \\approx 4.72 \\times 10^{-20}$$
$$S \\equiv \\frac{X_e^2}{1 - X_e} = (9.24 \\times 10^{17}) \\times (4.72 \\times 10^{-20}) \\approx 0.0436$$
</div>
<p>Solving $X_e^2 + S X_e - S = 0$:</p>
<div class="equation-box">
$$X_e = \\frac{-0.0436 + \\sqrt{(0.0436)^2 + 4(0.0436)}}{2} = \\frac{-0.0436 + \\sqrt{0.0019 + 0.1744}}{2} = \\frac{-0.0436 + 0.4199}{2} \\approx 0.188$$
</div>
<p>At $z = 1300$, the universe is already transitioning ($X_e \\approx 19\\%$ in Saha equilibrium; non-equilibrium peebles recombination yields $\\sim 85\\%$ due to Lyman-alpha photon trapping).</p>

<h4>(c) Ionization Fraction at $z = 1100$ and $z = 900$</h4>
<ul>
  <li>At $z = 1100$ ($T = 3000.8\\text{ K}, kT = 0.2586\\text{ eV}$):
  $$\\frac{13.60}{0.2586} = 52.59 \\implies \\exp(-52.59) = 1.44 \\times 10^{-23}$$
  $$S = \\frac{3.97 \\times 10^{26}}{3.34 \\times 10^8} \\times 1.44 \\times 10^{-23} = (1.19 \\times 10^{18})(1.44 \\times 10^{-23}) \\approx 1.71 \\times 10^{-5}$$
  $$X_e \\approx \\sqrt{S} = \\sqrt{1.71 \\times 10^{-5}} \\approx 4.1 \\times 10^{-3} \\quad (0.41\\%)$$
  </li>
  <li>At $z = 900$ ($T = 2455\\text{ K}, kT = 0.2116\\text{ eV}$):
  $$\\frac{13.60}{0.2116} = 64.27 \\implies \\exp(-64.27) = 1.22 \\times 10^{-28}$$
  $$S \\approx 2.5 \\times 10^{-11} \\implies X_e \\approx 5.0 \\times 10^{-6}$$
  </li>
</ul>

<h4>(d) Recombination Transition Redshift Interval</h4>
<p>The universe drops from $90\\%$ ionized to $10\\%$ ionized across a narrow redshift interval $\\Delta z \\approx 200$ centered at $z \\approx 1100$. This thin spherical shell of thickness $\\Delta z / z \\sim 15\\%$ defines the razor-sharp <strong>Surface of Last Scattering</strong>.</p>
"""
        },
        {
            "id": "prob-8-3",
            "title": "The Cosmic Horizon Problem: Particle Horizon at Decoupling vs The CMB",
            "statement": "In a matter-dominated flat universe ($a(t) = (t/t_0)^{2/3}$):\\n\\n(a) Derive the physical particle horizon radius $d_{\\text{hor}}(t) = a(t) \\int_0^t \\frac{c\\,dt'}{a(t')}$ in terms of $c$ and $t$.\\n(b) Recombination occurred at $t_{\\text{dec}} \\approx 380{,}000\\text{ years}$. Calculate the physical particle horizon radius $d_{\\text{hor}}(t_{\\text{dec}})$ in light-years and in kiloparsecs at the time of decoupling.\\n(c) The angular diameter distance to the surface of last scattering ($z \\approx 1100$) is $d_A \\approx 12.8\\text{ Mpc}$. Compute the angular size $\\theta_{\\text{hor}}$ (in degrees) that this causally connected patch subtends on our sky today.\\n(d) Explain how this numerical result formulates the <strong>Horizon Problem</strong> and how cosmic inflation solves it.",
            "solution": """
<h4>(a) Particle Horizon Derivation</h4>
<p>For $a(t) \\propto t^{2/3}$:</p>
<div class="equation-box">
$$d_{\\text{hor}}(t) = a(t) \\int_0^t \\frac{c\\,dt'}{t'^{2/3}} t^{-2/3} = c t^{2/3} \\left[3 t'^{1/3}\\right]_0^t = 3 c t$$
</div>
<p>The physical particle horizon is exactly three times the light travel distance ($3ct$).</p>

<h4>(b) Horizon Radius at Decoupling</h4>
<p>At $t_{\\text{dec}} = 380{,}000\\text{ yr}$:</p>
<div class="equation-box">
$$d_{\\text{hor}}(t_{\\text{dec}}) = 3 c \\times 380{,}000\\text{ yr} = 1{,}140{,}000\\text{ light-years} = 1.14\\text{ Mly}$$
</div>
<p>Converting to kiloparsecs ($1\\text{ pc} = 3.2616\\text{ ly}$):</p>
<div class="equation-box">
$$d_{\\text{hor}}(t_{\\text{dec}}) = \\frac{1.140 \\times 10^6\\text{ ly}}{3261.6\\text{ ly/kpc}} \\approx 349.5\\text{ kpc} \\approx 0.35\\text{ Mpc}$$
</div>

<h4>(c) Angular Size on the Modern Sky</h4>
<p>The angular size subtended by a causal patch of diameter $2 d_{\\text{hor}}$ at angular diameter distance $d_A = 12.8\\text{ Mpc} = 12{,}800\\text{ kpc}$ is:</p>
<div class="equation-box">
$$\\theta_{\\text{hor}} = \\frac{d_{\\text{hor}}(t_{\\text{dec}})}{d_A} = \\frac{349.5\\text{ kpc}}{12{,}800\\text{ kpc}} \\approx 0.0273\\text{ radians}$$
</div>
<p>Converting to degrees ($1\\text{ rad} = 57.2958^\\circ$):</p>
<div class="equation-box">
$$\\theta_{\\text{hor}} = 0.0273 \\times 57.2958^\\circ \\approx 1.56^\\circ \\approx 1.6^\\circ$$
</div>
<p>A single causally connected patch at recombination spans less than $2^\\circ$ on the celestial sphere!</p>

<h4>(d) The Horizon Problem & The Inflationary Solution</h4>
<p>The celestial sphere contains $4\\pi\\text{ sr} = 41{,}253\\text{ square degrees}$. Since a causal patch covers an area of $\\pi \\theta_{\\text{hor}}^2 \\approx \\pi (0.8^\\circ)^2 \\approx 2.0\\text{ deg}^2$, the CMB sky comprises over:</p>
<div class="equation-box">
$$N_{\\text{patches}} = \\frac{41{,}253\\text{ deg}^2}{2.0\\text{ deg}^2} \\approx 20{,}000\\text{ causally disconnected regions!}$$
</div>
<p>According to classical Big Bang theory, points separated by more than $2^\\circ$ could never have exchanged a single photon or interacted before decoupling. Yet the Planck satellite observes that all 20,000 regions share the exact same temperature ($T = 2.7255\\text{ K}$) to within $0.001\\%$! This is the <strong>Horizon Problem</strong>.</p>
<p><strong>Cosmic Inflation</strong> solves this paradox completely: before $t \\sim 10^{-32}\\text{ s}$, the entire region that would become our observable universe was microscopic ($< 10^{-28}\\text{ cm}$), easily coming into intimate causal thermal equilibrium. Inflation then exponentially expanded space by a factor of $e^{60} \\approx 10^{26}$, propelling these pre-equilibrated points far outside the local causal horizon, only for them to re-enter our horizon billions of years later sharing identical temperatures.</p>
"""
        }
    ]
}

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u7.json', 'w') as f:
    json.dump(u7, f, indent=2)
print("astro_u7.json written successfully")

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u8.json', 'w') as f:
    json.dump(u8, f, indent=2)
print("astro_u8.json written successfully")
