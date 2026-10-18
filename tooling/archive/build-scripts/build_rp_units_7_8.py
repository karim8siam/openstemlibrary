# -*- coding: utf-8 -*-
"""
Builder for Nuclear Reactor Physics Units 7 & 8
Unit 7: Reactor Criticality & Geometric Buckling in Core Geometries
Unit 8: Reactor Kinetics, Reactivity Feedback, Control Rods & Poisoning
"""
import json

u7_data = {
    "title": "Reactor Criticality & Geometric Buckling in Core Geometries",
    "subtitle": "Helmholtz Critical Equation, Five Canonical Core Geometries, Optimum Volume & Reflector Savings",
    "summary": "Comprehensive mathematical theory of reactor criticality and geometric buckling across canonical core shapes: derivation of the one-group Helmholtz reactor critical wave equation nabla^2 phi + B^2 phi = 0; material buckling B_m^2 = (k_infinity - 1)/M^2 versus geometric buckling B_g^2; exact analytical solutions of the boundary value problem for infinite slab, sphere, infinite cylinder, cuboid, and finite cylinder; optimum cylinder aspect ratio H/D = 1.082 and minimum critical volume theorem; spatial flux distributions, flux flatness, and peak-to-average flux peaking factors; two-region core-reflector diffusion theory, reflector thermal flux peaking, and analytical determination of reflector savings delta.",
    "sections": [
        {
            "id": "sec-7-1",
            "title": "The One-Group Reactor Equation: From Diffusion to Helmholtz Wave Form",
            "content": r"""
<h3>1. Derivation of the Steady-State Reactor Equation</h3>
<p>
Consider a bare, homogeneous nuclear reactor operating at steady state. Thermal neutrons are lost by leakage ($-D \nabla^2\phi$) and absorption ($\Sigma_a \phi$). In a multiplying medium, thermal fission generates $k_\infty \Sigma_a \phi$ fast neutrons, which slow down to thermal energy.
In one-group diffusion theory:
$$-D \nabla^2 \phi(\vec{r}) + \Sigma_a \phi(\vec{r}) = k_\infty \Sigma_a \phi(\vec{r})$$
Rearranging terms:
$$-D \nabla^2 \phi(\vec{r}) = (k_\infty - 1) \Sigma_a \phi(\vec{r})$$
Dividing both sides by $D$:
$$\nabla^2 \phi(\vec{r}) + \frac{(k_\infty - 1) \Sigma_a}{D} \phi(\vec{r}) = 0$$
Recalling that the thermal diffusion area is $L^2 = D / \Sigma_a$:
$$\mathbf{\nabla^2 \phi(\vec{r}) + B^2 \phi(\vec{r}) = 0}$$
This is the famous <strong>Helmholtz Reactor Critical Wave Equation</strong>!
</p>

<h3>2. The Separation of Variables</h3>
<p>
The eigenvalue problem $\nabla^2\phi + B^2\phi = 0$ requires that the neutron flux $\phi(\vec{r})$:
<ol>
  <li>Must be non-negative everywhere inside the physical core: $\phi(\vec{r}) \ge 0$.</li>
  <li>Must vanish at the extrapolated boundaries: $\phi(\vec{r}_{\text{extrapolated}}) = 0$.</li>
  <li>Must be finite, real, and continuous throughout the interior.</li>
</ol>
The lowest eigenvalue $B^2$ corresponding to the fundamental strictly positive eigenmode defines the <strong>geometric buckling</strong> $B_g^2$ of the reactor core!
</p>
"""
        },
        {
            "id": "sec-7-2",
            "title": "Material Buckling Bm^2 vs Geometric Buckling Bg^2 & The Criticality Condition",
            "content": r"""
<h3>1. Material Buckling $B_m^2$</h3>
<p>
The <strong>material buckling</strong> $B_m^2$ depends strictly on the nuclear, isotopic, and material composition of the fuel-moderator mixture:
$$\mathbf{B_m^2 \equiv \frac{k_\infty - 1}{M^2} = \frac{k_\infty - 1}{L^2 + \tau}}$$
It characterizes the intrinsic neutron production capacity per unit migration area of the nuclear composition, completely independent of the core shape or size!
</p>

<h3>2. Geometric Buckling $B_g^2$</h3>
<p>
The <strong>geometric buckling</strong> $B_g^2$ depends strictly on the physical size and geometric shape of the reactor core, determined by the spatial Laplacian curvature:
$$\mathbf{B_g^2 \equiv - \frac{\nabla^2 \phi}{\phi}}$$
Large cores have small geometric curvature (low leakage, small $B_g^2$). Small cores have sharp curvature (high surface-to-volume ratio, intense leakage, large $B_g^2$).
</p>

<h3>3. The Criticality Balance</h3>
<p>
Recall the Six-Factor formula $k_{\text{eff}} = \frac{k_\infty}{1 + M^2 B_g^2}$. Rearranging:
$$k_{\text{eff}} = 1 \iff 1 + M^2 B_g^2 = k_\infty \iff \mathbf{B_g^2 = \frac{k_\infty - 1}{M^2} = B_m^2}$$
Hence, the fundamental reactor criticality criterion is:
<ul>
  <li><strong>Subcritical ($k_{\text{eff}} < 1$):</strong> $B_g^2 > B_m^2$ (Core is too small; leakage dominates production).</li>
  <li><strong>Critical ($k_{\text{eff}} = 1$):</strong> $\mathbf{B_g^2 = B_m^2}$ (Exact balance between geometry and nuclear material).</li>
  <li><strong>Supercritical ($k_{\text{eff}} > 1$):</strong> $B_g^2 < B_m^2$ (Core is larger than critical size).</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-7-3",
            "title": "Helmholtz Solutions: Infinite Slab & Bare Spherical Reactor Cores",
            "content": r"""
<h3>1. Infinite Slab Reactor (Thickness $a$)</h3>
<p>
Consider an infinite slab bounded by planes at $x = \pm a/2$. With extrapolated thickness $\tilde{a} = a + 2d$:
$$\frac{d^2\phi}{dx^2} + B^2 \phi = 0$$
General solution: $\phi(x) = A \cos(B x) + C \sin(B x)$. By spatial symmetry across the midplane $x = 0$, $C = 0$.
Boundary condition: $\phi(\pm \tilde{a}/2) = 0 \implies \cos(B \tilde{a}/2) = 0 \implies B \frac{\tilde{a}}{2} = \frac{\pi}{2}$.
$$\mathbf{B_g^2 = \left( \frac{\pi}{\tilde{a}} \right)^2, \qquad \phi(x) = \phi_0 \cos\left( \frac{\pi x}{\tilde{a}} \right)}$$
</p>

<h3>2. Bare Spherical Reactor (Radius $R$)</h3>
<p>
Consider a sphere of physical radius $R$ and extrapolated radius $\tilde{R} = R + d$. In spherical coordinates:
$$\frac{1}{r^2} \frac{d}{dr}\left( r^2 \frac{d\phi}{dr} \right) + B^2 \phi = 0$$
Substitute $w(r) = r \phi(r)$:
$$\frac{d^2 w}{dr^2} + B^2 w = 0 \implies w(r) = A \sin(B r) + C \cos(B r)$$
Since the flux at the center must be finite, $\lim_{r \to 0} \frac{w(r)}{r} < \infty \implies C = 0$:
$$\phi(r) = A \frac{\sin(B r)}{r}$$
Boundary condition: $\phi(\tilde{R}) = 0 \implies \sin(B \tilde{R}) = 0 \implies B \tilde{R} = \pi$.
$$\mathbf{B_g^2 = \left( \frac{\pi}{\tilde{R}} \right)^2, \qquad \phi(r) = \phi_0 \frac{\sin(\pi r / \tilde{R})}{\pi r / \tilde{R}}}$$
where $\phi_0 = A B$ is the central peak flux.
</p>
"""
        },
        {
            "id": "sec-7-4",
            "title": "Helmholtz Solutions: Infinite Cylinder & Rectangular Parallelepiped",
            "content": r"""
<h3>1. Infinite Cylindrical Reactor (Radius $R$)</h3>
<p>
In cylindrical coordinates with axial and azimuthal symmetry:
$$\frac{1}{r} \frac{d}{dr}\left( r \frac{d\phi}{dr} \right) + B^2 \phi = 0$$
This is Bessel's differential equation of order zero. The general solution is:
$$\phi(r) = A J_0(B r) + C Y_0(B r)$$
Since the Bessel function of the second kind diverges logarithmically at the origin ($Y_0(0) \to -\infty$), physical regularity requires $C = 0$:
$$\phi(r) = \phi_0 J_0(B r)$$
Boundary condition: $\phi(\tilde{R}) = 0 \implies J_0(B \tilde{R}) = 0$.
The first positive zero of the zeroth-order Bessel function is $\nu_{0, 1} \approx 2.40483 \approx 2.405$:
$$B \tilde{R} = 2.405 \implies \mathbf{B_g^2 = \left( \frac{2.405}{\tilde{R}} \right)^2, \qquad \phi(r) = \phi_0 J_0\left( \frac{2.405 r}{\tilde{R}} \right)}$$
</p>

<h3>2. Rectangular Parallelepiped (Cuboid $a \times b \times c$)</h3>
<p>
Separating variables $\phi(x, y, z) = X(x) Y(y) Z(z)$ with origin at the center:
$$\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} + B^2 = 0 \implies -B_x^2 - B_y^2 - B_z^2 + B^2 = 0$$
Enforcing zero flux at $\pm \tilde{a}/2, \pm \tilde{b}/2, \pm \tilde{c}/2$:
$$\mathbf{B_g^2 = \left(\frac{\pi}{\tilde{a}}\right)^2 + \left(\frac{\pi}{\tilde{b}}\right)^2 + \left(\frac{\pi}{\tilde{c}}\right)^2}$$
$$\mathbf{\phi(x, y, z) = \phi_0 \cos\left( \frac{\pi x}{\tilde{a}} \right) \cos\left( \frac{\pi y}{\tilde{b}} \right) \cos\left( \frac{\pi z}{\tilde{c}} \right)}$$
For a perfect cube ($\tilde{a} = \tilde{b} = \tilde{c}$): $B_g^2 = 3 (\pi/\tilde{a})^2$.
</p>
"""
        },
        {
            "id": "sec-7-5",
            "title": "Finite Cylindrical Reactors, Optimum Dimensions & Minimum Critical Volume",
            "content": r"""
<h3>1. Solution for the Finite Cylinder (Radius $R$, Height $H$)</h3>
<p>
Combining radial Bessel dependence with axial cosine dependence:
$$\nabla^2 \phi = \frac{1}{r} \frac{\partial}{\partial r}\left( r \frac{\partial \phi}{\partial r} \right) + \frac{\partial^2 \phi}{\partial z^2}$$
Separating variables $\phi(r, z) = \mathcal{R}(r) \mathcal{Z}(z)$:
$$\mathbf{B_g^2 = B_r^2 + B_z^2 = \left( \frac{2.405}{\tilde{R}} \right)^2 + \left( \frac{\pi}{\tilde{H}} \right)^2}$$
The 2D spatial flux profile is:
$$\mathbf{\phi(r, z) = \phi_0 J_0\left( \frac{2.405 r}{\tilde{R}} \right) \cos\left( \frac{\pi z}{\tilde{H}} \right)}$$
</p>

<h3>2. The Optimum Cylinder Dimensions ($H/D = 1.082$)</h3>
<p>
For a given critical material buckling $B_m^2$, what cylinder radius $R$ and height $H$ minimize the total physical volume $V = \pi R^2 H$?
We seek to minimize $V(\tilde{R}, \tilde{H}) = \pi \tilde{R}^2 \tilde{H}$ subject to constraint $\left( \frac{2.405}{\tilde{R}} \right)^2 + \left( \frac{\pi}{\tilde{H}} \right)^2 = B^2$.
Using Lagrange multipliers or substitution $\tilde{H} = \frac{\pi}{\sqrt{B^2 - (2.405/\tilde{R})^2}}$:
$$\frac{dV}{d\tilde{R}} = 0 \implies \tilde{H}^2 = 2 \left( \frac{\pi}{2.405} \right)^2 \tilde{R}^2 = 2 \left( \frac{3.14159}{2.405} \right)^2 \tilde{R}^2 \approx 3.409 \, \tilde{R}^2$$
$$\frac{\tilde{H}}{\tilde{R}} = \sqrt{3.409} \approx 1.846 \implies \mathbf{\frac{\tilde{H}}{\tilde{D}} = \frac{1.846}{2} \approx \mathbf{1.082}}$$
A finite cylinder achieves <strong>minimum critical volume</strong> when its height is approximately $8.2\%$ greater than its diameter!
</p>

<h3>3. Canonical Geometry Comparison Table</h3>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Geometry</th>
      <th style="padding: 8px;">Buckling $B_g^2$</th>
      <th style="padding: 8px;">Flux Distribution $\phi(\vec{r}) / \phi_0$</th>
      <th style="padding: 8px;">Critical Volume $V_c$</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;"><strong>Sphere</strong> (Radius $\tilde{R}$)</td>
      <td style="padding: 8px;">$(\pi/\tilde{R})^2$</td>
      <td style="padding: 8px;">$\frac{\sin(\pi r / \tilde{R})}{\pi r / \tilde{R}}$</td>
      <td style="padding: 8px;">$\mathbf{129.88 / B^3}$ (Absolute Minimum!)</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;"><strong>Optimum Cylinder</strong> ($\tilde{H} = 1.082 \tilde{D}$)</td>
      <td style="padding: 8px;">$(2.405/\tilde{R})^2 + (\pi/\tilde{H})^2$</td>
      <td style="padding: 8px;">$J_0(2.405 r/\tilde{R}) \cos(\pi z/\tilde{H})$</td>
      <td style="padding: 8px;">$\mathbf{148.28 / B^3}$ ($+14.2\%$ vs Sphere)</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;"><strong>Cube</strong> (Side $\tilde{a}$)</td>
      <td style="padding: 8px;">$3(\pi/\tilde{a})^2$</td>
      <td style="padding: 8px;">$\cos(\pi x/\tilde{a})\cos(\pi y/\tilde{a})\cos(\pi z/\tilde{a})$</td>
      <td style="padding: 8px;">$\mathbf{161.45 / B^3}$ ($+24.3\%$ vs Sphere)</td>
    </tr>
  </tbody>
</table>
<p>
The sphere has the smallest surface-to-volume ratio, minimizing neutron leakage and thus requiring the smallest critical mass of fissile fuel.
</p>
"""
        },
        {
            "id": "sec-7-6",
            "title": "Peak-to-Average Flux Ratios & Power Peaking Factors in Critical Cores",
            "content": r"""
<h3>1. The Flux Peaking Factor $\Omega$</h3>
<p>
Because neutron fission power is proportional to local flux $P(\vec{r}) \propto \phi(\vec{r})$, the thermal margin (critical heat flux, fuel centerline melting limit) is dictated by the <strong>peak-to-average flux ratio</strong> $\Omega$:
$$\mathbf{\Omega \equiv \frac{\phi_{\max}}{\bar{\phi}} = \frac{\phi_0}{\frac{1}{V} \int_V \phi(\vec{r}) \, dV}}$$
Values for bare geometries:
<ul>
  <li><strong>Infinite Slab:</strong>
  $$\bar{\phi} = \frac{1}{\tilde{a}} \int_{-\tilde{a}/2}^{\tilde{a}/2} \phi_0 \cos\left( \frac{\pi x}{\tilde{a}} \right) dx = \frac{2}{\pi} \phi_0 \implies \mathbf{\Omega_{\text{slab}} = \frac{\pi}{2} \approx 1.571}$$</li>
  <li><strong>Bare Sphere:</strong>
  $$\bar{\phi} = \frac{1}{\frac{4}{3}\pi \tilde{R}^3} \int_0^{\tilde{R}} \phi_0 \frac{\sin(\pi r/\tilde{R})}{\pi r/\tilde{R}} 4\pi r^2 dr = \frac{3}{\pi^2} \phi_0 \implies \mathbf{\Omega_{\text{sphere}} = \frac{\pi^2}{3} \approx 3.290}$$</li>
  <li><strong>Finite Cylinder:</strong>
  $$\Omega_{\text{cyl}} = \Omega_{\text{radial}} \times \Omega_{\text{axial}} = \left[ \frac{2.405}{2 J_1(2.405)} \right] \times \left[ \frac{\pi}{2} \right] \approx 2.316 \times 1.571 \approx \mathbf{3.638}$$</li>
</ul>
A bare finite cylinder has a peak power density $3.64$ times greater than its core average! Real power reactors flatten this distribution using reflectors, fuel zoning, and burnable poison loading.
</p>
"""
        },
        {
            "id": "sec-7-7",
            "title": "Reflected Reactor Theory: Two-Region Equations & Reflector Savings",
            "content": r"""
<h3>1. Physics of the Reflector</h3>
<p>
Surrounding a bare multiplying core with an unmultiplied moderating shell (the <strong>reflector</strong>, e.g. $\text{H}_2\text{O}, \text{D}_2\text{O}, \text{Be}, \text{C}$) fundamentally improves reactor economics:
<ol>
  <li><strong>Neutron Economy:</strong> Fast and thermal neutrons leaking from the core scatter in the reflector and return to the core (neutron albedo effect).</li>
  <li><strong>Critical Mass Reduction:</strong> Returning neutrons reduce the required critical core dimensions from $R_{\text{bare}}$ to $R_{\text{core}}$.</li>
  <li><strong>Flux Flattening:</strong> Reflected neutrons thermalize in the reflector, producing a characteristic <strong>thermal flux peak</strong> near the core-reflector interface, greatly reducing peak-to-average power peaking!</li>
</ol>
</p>

<h3>2. Two-Region Diffusion Formulation</h3>
<p>
For a reflected spherical core with core radius $R$ and reflector outer radius $R_R$:
<ul>
  <li><strong>Core Region ($0 \le r \le R$):</strong> Multiplying medium:
  $$\nabla^2 \phi_c + B^2 \phi_c = 0 \implies \phi_c(r) = A \frac{\sin(B r)}{r}$$</li>
  <li><strong>Reflector Region ($R \le r \le \tilde{R}_R$):</strong> Non-multiplying medium:
  $$\nabla^2 \phi_r - \frac{1}{L_r^2} \phi_r = 0 \implies \phi_r(r) = C \frac{\sinh\left( \frac{\tilde{R}_R - r}{L_r} \right)}{r}$$</li>
</ul>
Enforcing flux and current continuity at the core-reflector interface $r = R$:
$$\phi_c(R) = \phi_r(R), \qquad D_c \left.\frac{d\phi_c}{dr}\right|_R = D_r \left.\frac{d\phi_r}{dr}\right|_R$$
Dividing the current boundary condition by the flux condition yields the logarithmic derivative matching condition:
$$D_c \left[ B \cot(B R) - \frac{1}{R} \right] = D_r \left[ -\frac{1}{L_r} \coth\left(\frac{\tilde{R}_R - R}{L_r}\right) - \frac{1}{R} \right]$$
</p>

<h3>3. Reflector Savings $\delta$</h3>
<p>
The <strong>reflector savings</strong> $\delta$ is the reduction in core dimension enabled by the reflector:
$$\mathbf{\delta \equiv R_{\text{bare}} - R_{\text{reflected}}}$$
For an infinite reflector ($R_R \to \infty$) with matched diffusion properties ($D_c \approx D_r$):
$$\mathbf{\delta \approx L_r}$$
The reflector savings is approximately equal to the thermal diffusion length $L_r$ of the reflector material! For graphite ($L_r \approx 50\text{ cm}$), reflector savings can exceed $30\text{ to }40\text{ cm}$, shrinking critical core volume by over $50\%$!
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-7-1",
            "title": "Critical Radius, Critical Mass, and Minimum Volume of a Bare Spherical Reactor",
            "statement": r"""A bare spherical reactor is fueled with a homogeneous mixture of $20\%$ enriched uranium dioxide ($\text{UO}_2$) and graphite moderator.
The material parameters of the mixture are:
- Infinite multiplication factor $k_\infty = 1.250$
- Thermal diffusion area $L^2 = 320\text{ cm}^2$
- Fermi age $\tau = 280\text{ cm}^2$
- Extrapolation distance $d = 2.1\text{ cm}$
- Fuel atom density $N_{235} = 4.20 \times 10^{20}\text{ atoms/cm}^3$
(a) Calculate the material buckling $B_m^2$ and the critical buckling $B_g^2$.
(b) Calculate the extrapolated critical radius $\tilde{R}$, the physical critical radius $R$, and the critical volume $V_c$ in liters.
(c) Calculate the critical mass of Uranium-235 ($M_{235}$) loaded into the bare sphere in kilograms.""",
            "solution": r"""**(a) Material Buckling $B_m^2$:**
Migration area:
$$M^2 = L^2 + \tau = 320\text{ cm}^2 + 280\text{ cm}^2 = 600\text{ cm}^2$$
Material buckling:
$$B_m^2 = \frac{k_\infty - 1}{M^2} = \frac{1.250 - 1}{600\text{ cm}^2} = \frac{0.250}{600\text{ cm}^2} \approx \mathbf{4.1667 \times 10^{-4}\text{ cm}^{-2}}$$
At criticality, $B_g^2 = B_m^2 = 4.1667 \times 10^{-4}\text{ cm}^{-2}$.
The critical buckling parameter is:
$$B = \sqrt{4.1667 \times 10^{-4}} \approx \mathbf{0.020412\text{ cm}^{-1}}$$

**(b) Critical Radii and Volume:**
For a bare sphere:
$$B_g = \frac{\pi}{\tilde{R}} \implies \tilde{R} = \frac{\pi}{B} = \frac{3.14159265}{0.020412\text{ cm}^{-1}} \approx \mathbf{153.91\text{ cm}}$$
Physical critical radius:
$$R = \tilde{R} - d = 153.91\text{ cm} - 2.10\text{ cm} \approx \mathbf{151.81\text{ cm}} \approx \mathbf{1.518\text{ m}}$$
Critical volume:
$$V_c = \frac{4}{3} \pi R^3 = \frac{4}{3} \pi (151.81\text{ cm})^3 \approx 1.465 \times 10^7\text{ cm}^3 = \mathbf{14{,}650\text{ liters}} \approx \mathbf{14.65\text{ m}^3}$$

**(c) Critical Mass of $^{235}\text{U}$:**
Total number of $^{235}\text{U}$ nuclei in the critical volume:
$$N_{\text{tot}} = N_{235} \times V_c = (4.20 \times 10^{20}\text{ atoms/cm}^3) \times (1.465 \times 10^7\text{ cm}^3) \approx 6.153 \times 10^{27}\text{ atoms}$$
Critical mass:
$$M_{235} = \frac{N_{\text{tot}} \times 235.044\text{ g/mol}}{6.02214 \times 10^{23}\text{ atoms/mol}} \approx 2.401 \times 10^6\text{ g} = \mathbf{2401\text{ kg}} = \mathbf{2.40\text{ metric tons}}$$
The critical mass of $^{235}\text{U}$ is **$2401\text{ kg}$**."""
        },
        {
            "id": "rp-prob-7-2",
            "title": "Optimization of Dimensions and Power Peaking in a Finite Cylindrical Reactor",
            "statement": r"""A bare cylindrical reactor has critical buckling $B^2 = 4.00 \times 10^{-4}\text{ cm}^{-2}$.
(a) For an optimum cylinder where height equals $1.082 \times \text{diameter}$ ($\tilde{H} = 2.164 \tilde{R}$), calculate the extrapolated radius $\tilde{R}$, diameter $\tilde{D}$, and height $\tilde{H}$ in meters.
(b) Calculate the minimum critical volume $V_{\text{opt}}$ in $\text{m}^3$ and compare it with a non-optimum cylinder having squashed pancake proportions $\tilde{H} = \tilde{R}$.
(c) The peak thermal neutron flux at the core center is $\phi_0 = 4.5 \times 10^{13}\text{ neutrons/cm}^2\cdot\text{s}$. Calculate the core-average thermal flux $\bar{\phi}$ and the total peak-to-average flux peaking factor $\Omega$.""",
            "solution": r"""**(a) Optimum Cylinder Dimensions:**
For a finite cylinder:
$$B^2 = \left( \frac{2.405}{\tilde{R}} \right)^2 + \left( \frac{\pi}{\tilde{H}} \right)^2$$
Substituting $\tilde{H} = 2.164 \tilde{R}$:
$$B^2 = \frac{2.405^2}{\tilde{R}^2} + \frac{\pi^2}{(2.164 \tilde{R})^2} = \frac{5.784}{\tilde{R}^2} + \frac{9.8696}{4.6829 \tilde{R}^2} = \frac{5.784 + 2.1076}{\tilde{R}^2} = \frac{7.8916}{\tilde{R}^2}$$
Solving for $\tilde{R}$:
$$\tilde{R}^2 = \frac{7.8916}{B^2} = \frac{7.8916}{4.00 \times 10^{-4}\text{ cm}^{-2}} = 19{,}729\text{ cm}^2$$
$$\tilde{R} = \sqrt{19{,}729} \approx \mathbf{140.46\text{ cm}} = \mathbf{1.405\text{ m}}$$
Diameter:
$$\tilde{D} = 2 \tilde{R} = 2 \times 140.46\text{ cm} \approx \mathbf{280.92\text{ cm}} = \mathbf{2.809\text{ m}}$$
Height:
$$\tilde{H} = 2.164 \times 140.46\text{ cm} \approx \mathbf{303.96\text{ cm}} = \mathbf{3.040\text{ m}}$$

**(b) Volume Comparison:**
Optimum volume:
$$V_{\text{opt}} = \pi \tilde{R}^2 \tilde{H} = \pi (1.4046\text{ m})^2 (3.0396\text{ m}) \approx \mathbf{18.84\text{ m}^3}$$
For squashed cylinder ($\tilde{H} = \tilde{R}$):
$$B^2 = \frac{5.784 + 9.8696}{\tilde{R}_{\text{sq}}^2} = \frac{15.6536}{\tilde{R}_{\text{sq}}^2} \implies \tilde{R}_{\text{sq}}^2 = \frac{15.6536}{4.00 \times 10^{-4}} = 39{,}134\text{ cm}^2$$
$$\tilde{R}_{\text{sq}} = 197.82\text{ cm} = 1.978\text{ m}, \qquad \tilde{H}_{\text{sq}} = 1.978\text{ m}$$
Squashed volume:
$$V_{\text{sq}} = \pi (1.9782)^2 (1.9782) \approx \mathbf{24.32\text{ m}^3}$$
Penalty of non-optimum aspect ratio:
$$\frac{V_{\text{sq}} - V_{\text{opt}}}{V_{\text{opt}}} \times 100\% = \frac{24.32 - 18.84}{18.84} \times 100\% \approx \mathbf{+29.1\%}$$
Operating off the optimum $H/D$ increases required core volume and fuel mass by nearly **$30\%$**!

**(c) Peak-to-Average Flux and Peaking Factor:**
Peaking factor:
$$\Omega = \left[ \frac{2.405}{2 J_1(2.405)} \right] \times \left[ \frac{\pi}{2} \right]$$
Given $J_1(2.405) \approx 0.51915$:
$$\Omega_{\text{radial}} = \frac{2.405}{2 \times 0.51915} = \frac{2.405}{1.0383} \approx 2.3163$$
$$\Omega_{\text{axial}} = \frac{\pi}{2} \approx 1.5708$$
$$\Omega = 2.3163 \times 1.5708 \approx \mathbf{3.6384}$$
Average thermal neutron flux:
$$\bar{\phi} = \frac{\phi_0}{\Omega} = \frac{4.5 \times 10^{13}}{3.6384} \approx \mathbf{1.237 \times 10^{13}\text{ neutrons/cm}^2\cdot\text{s}}$$"""
        },
        {
            "id": "rp-prob-7-3",
            "title": "Two-Region Reflected Slab Reactor and Exact Calculation of Reflector Savings",
            "statement": r"""A critical reactor consists of an infinite multiplying fuel slab of half-thickness $a$ surrounded on both sides by an infinitely thick graphite reflector.
The diffusion properties are:
- Core: $D_c = 0.90\text{ cm}, M^2 = 250\text{ cm}^2, k_\infty = 1.150$
- Reflector: $D_r = 0.85\text{ cm}, L_r = 50.0\text{ cm}$
(a) Calculate the material buckling $B_c^2$ of the core and determine the bare slab half-thickness $a_{\text{bare}}$ (neglecting extrapolation distance).
(b) From two-region diffusion theory, derive the transcendental criticality condition:
$$\cot(B_c a) = \frac{D_r}{D_c B_c L_r}$$
(c) Solve for the reflected half-thickness $a$ and calculate the reflector savings $\delta = a_{\text{bare}} - a$ in centimeters.""",
            "solution": r"""**(a) Bare Core Half-Thickness $a_{\text{bare}}$:**
Core material buckling:
$$B_c^2 = \frac{k_\infty - 1}{M^2} = \frac{1.150 - 1}{250\text{ cm}^2} = \frac{0.150}{250} = 6.00 \times 10^{-4}\text{ cm}^{-2}$$
$$B_c = \sqrt{6.00 \times 10^{-4}} \approx \mathbf{0.024495\text{ cm}^{-1}}$$
For a bare slab with midplane symmetry, $B_c = \pi / (2 a_{\text{bare}})$:
$$a_{\text{bare}} = \frac{\pi}{2 B_c} = \frac{\pi}{2 \times 0.024495\text{ cm}^{-1}} \approx \mathbf{64.128\text{ cm}}$$

**(b) Derivation of Criticality Condition:**
- In the core ($-a \le x \le a$): $\phi_c(x) = A \cos(B_c x)$.
- In the right reflector ($x \ge a$): $\phi_r(x) = C e^{-(x - a)/L_r}$.
Matching boundary conditions at $x = a$:
1. Flux continuity: $\phi_c(a) = \phi_r(a) \implies A \cos(B_c a) = C$
2. Current continuity: $-D_c \left.\frac{d\phi_c}{dx}\right|_a = -D_r \left.\frac{d\phi_r}{dx}\right|_a \implies D_c A B_c \sin(B_c a) = D_r \frac{C}{L_r}$
Dividing the current equation by the flux equation:
$$D_c B_c \tan(B_c a) = \frac{D_r}{L_r} \implies \tan(B_c a) = \frac{D_r}{D_c B_c L_r}$$
Taking reciprocal:
$$\mathbf{\cot(B_c a) = \frac{D_c B_c L_r}{D_r}} \quad \text{or} \quad \mathbf{\tan(B_c a) = \frac{D_r}{D_c B_c L_r}} \quad \text{(Q.E.D.)}$$

**(c) Reflected Slab Half-Thickness and Reflector Savings:**
Evaluate the right-hand side of the tangent formula:
$$\frac{D_r}{D_c B_c L_r} = \frac{0.85\text{ cm}}{(0.90\text{ cm}) \times (0.024495\text{ cm}^{-1}) \times (50.0\text{ cm})} = \frac{0.85}{1.102275} \approx 0.77113$$
Therefore:
$$\tan(B_c a) = 0.77113 \implies B_c a = \arctan(0.77113) \approx 0.65706\text{ radians}$$
Solving for $a$:
$$a = \frac{0.65706}{B_c} = \frac{0.65706}{0.024495\text{ cm}^{-1}} \approx \mathbf{26.824\text{ cm}}$$
Reflector savings:
$$\delta = a_{\text{bare}} - a = 64.128\text{ cm} - 26.824\text{ cm} \approx \mathbf{37.30\text{ cm}}$$
The graphite reflector reduces the required core half-thickness from $64.1\text{ cm}$ down to $26.8\text{ cm}$, saving **$37.3\text{ cm}$** and reducing core fuel volume by **$58.2\%$**!"""
        }
    ]
}

u8_data = {
    "title": "Reactor Kinetics, Reactivity Feedback, Control Rods & Poisoning",
    "subtitle": "Point Kinetics Equations, Inhour Relation, Prompt Jump, Feedback & Xenon-135 Dynamics",
    "summary": "Time-dependent dynamics, kinetics, control, and transient stability of nuclear reactors: derivation of the Point Reactor Kinetics Equations (PRKE) with six delayed neutron precursor groups; prompt neutron lifetime l versus generation time Lambda; prompt criticality threshold rho = beta and explosive power runaway; the Inhour (Inverse Hour) equation relating static reactivity rho to stable asymptotic reactor period T; analytical solution of step reactivity insertions and the prompt jump approximation; control rod physics, perturbation theory, differential and integral control rod worth curves, and burnable absorbers; inherent negative reactivity feedback coefficients (fuel Doppler broadening alpha_D, moderator temperature alpha_M, and void alpha_V); fission product poisoning dynamics, coupled non-linear differential equations for the Iodine-135 / Xenon-135 chain, equilibrium xenon poisoning, the post-shutdown 'iodine pit' xenon peak, and Samarium-149 equilibrium poisoning.",
    "sections": [
        {
            "id": "sec-8-1",
            "title": "Time-Dependent Neutron Diffusion & Point Reactor Kinetics Equations (PRKE)",
            "content": r"""
<h3>1. The Time-Dependent Diffusion Equation</h3>
<p>
When neutron populations vary with time, the net time rate of change of neutron density is governed by the time-dependent diffusion equation:
$$\frac{1}{v} \frac{\partial \phi(\vec{r}, t)}{\partial t} = D \nabla^2 \phi(\vec{r}, t) - \Sigma_a \phi(\vec{r}, t) + S(\vec{r}, t)$$
In a multiplying medium, the source $S(\vec{r}, t)$ consists of two distinct components:
<ol>
  <li><strong>Prompt Neutrons:</strong> Fraction $1 - \beta$ of all fission neutrons, emitted promptly: $(1 - \beta) k_\infty \Sigma_a \phi$.</li>
  <li><strong>Delayed Neutrons:</strong> Produced via radioactive decay of six delayed precursor groups: $\sum_{i=1}^6 \lambda_i C_i(\vec{r}, t)$.</li>
</ol>
</p>

<h3>2. The Point Reactor Kinetics Equations (PRKE)</h3>
<p>
Assuming the spatial flux shape remains fixed during transients (the point reactor approximation $\phi(\vec{r}, t) \approx \psi(\vec{r}) P(t)$), integrating over core volume yields the classical <strong>Point Reactor Kinetics Equations</strong> for total neutron population $n(t)$ (or thermal power $P(t)$):
$$\mathbf{\frac{dn(t)}{dt} = \frac{\rho(t) - \beta}{\Lambda} n(t) + \sum_{i=1}^6 \lambda_i C_i(t)}$$
$$\mathbf{\frac{dC_i(t)}{dt} = \frac{\beta_i}{\Lambda} n(t) - \lambda_i C_i(t) \quad (i = 1, 2, \dots, 6)}$$
where:
<ul>
  <li>$\rho(t) = \frac{k(t) - 1}{k(t)}$ is the net reactivity.</li>
  <li>$\beta = \sum_{i=1}^6 \beta_i$ is the total delayed neutron fraction ($\beta \approx 0.0065$ for $^{235}\text{U}$).</li>
  <li>$\Lambda \equiv \frac{l}{k} \approx l$ is the prompt neutron generation time ($\Lambda \sim 10^{-4}\text{ s}$ in PWRs, $\sim 10^{-7}\text{ s}$ in fast reactors).</li>
  <li>$C_i(t)$ is the precursor population of group $i$, decaying with decay constant $\lambda_i$.</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-8-2",
            "title": "Prompt Neutron Generation Time & The Prompt Criticality Barrier (rho = beta)",
            "content": r"""
<h3>1. The Purely Prompt Regime ($\rho \ge \beta$)</h3>
<p>
If a reactor receives a reactivity insertion equal to or exceeding the delayed neutron fraction:
$$\rho \ge \beta \implies \rho - \beta \ge 0$$
The prompt production term $\frac{\rho - \beta}{\Lambda} n(t)$ becomes positive on its own! In this terrifying condition—known as <strong>Prompt Criticality</strong> ($\rho = 1\$$)—the chain reaction sustains itself entirely on prompt neutrons, completely bypassing the slow decay of delayed precursors!
The neutron population explodes as:
$$n(t) = n_0 \exp\left( \frac{\rho - \beta}{\Lambda} t \right)$$
For $\rho = 1.1 \beta$ ($\rho - \beta = 0.1 \beta \approx 6.5 \times 10^{-4}$) in a thermal reactor with $\Lambda = 10^{-4}\text{ s}$:
$$\frac{\rho - \beta}{\Lambda} = \frac{6.5 \times 10^{-4}}{10^{-4}\text{ s}} = 6.5\text{ s}^{-1} \implies n(t) = n_0 e^{6.5 t}$$
In just one second, power multiplies by $e^{6.5} \approx 665$! In a fast reactor ($\Lambda = 10^{-7}\text{ s}$), $\frac{\rho - \beta}{\Lambda} = 6500\text{ s}^{-1}$, multiplying power by $10^{28}$ in one-hundredth of a second (a catastrophic explosive disassembly).
</p>

<h3>2. The Delayed Critical Buffer</h3>
<p>
For all normal reactor operations, reactivity is strictly confined to:
$$\mathbf{0 \le \rho < \beta \quad (0 \le \rho < 1\$)}$$
In this delayed critical regime, the prompt term is negative ($\rho - \beta < 0$), forcing the system to wait for delayed precursors to decay before each new generation can be sustained.
</p>
"""
        },
        {
            "id": "sec-8-3",
            "title": "The Inhour (Inverse Hour) Equation & Stable Reactor Period",
            "content": r"""
<h3>1. Derivation of the Characteristic Equation</h3>
<p>
Assuming exponential solutions of the form $n(t) = n_0 e^{\omega t}$ and $C_i(t) = C_{i, 0} e^{\omega t}$ for constant reactivity $\rho$:
Substitute into the precursor equation:
$$\omega C_{i, 0} = \frac{\beta_i}{\Lambda} n_0 - \lambda_i C_{i, 0} \implies C_{i, 0} = \frac{\beta_i}{\Lambda (\omega + \lambda_i)} n_0$$
Substitute $C_{i, 0}$ into the neutron equation:
$$\omega n_0 = \frac{\rho - \beta}{\Lambda} n_0 + \sum_{i=1}^6 \lambda_i \left[ \frac{\beta_i}{\Lambda (\omega + \lambda_i)} n_0 \right]$$
Dividing through by $n_0$ and multiplying by $\Lambda$:
$$\omega \Lambda = \rho - \beta + \sum_{i=1}^6 \frac{\lambda_i \beta_i}{\omega + \lambda_i}$$
Since $\beta = \sum \beta_i$, we write $\rho = \omega \Lambda + \sum \beta_i - \sum \frac{\lambda_i \beta_i}{\omega + \lambda_i} = \omega \Lambda + \sum \beta_i \left( 1 - \frac{\lambda_i}{\omega + \lambda_i} \right) = \omega \Lambda + \sum \frac{\omega \beta_i}{\omega + \lambda_i}$.
Setting reactor period $T \equiv 1/\omega$:
$$\mathbf{\rho = \frac{\Lambda}{T} + \sum_{i=1}^6 \frac{\beta_i}{1 + \lambda_i T}}$$
This is the foundational <strong>Inhour Equation</strong> (named from historic units of inverse hours, $\text{hr}^{-1}$).
</p>

<h3>2. Roots and Asymptotic Stable Period</h3>
<p>
For any step reactivity $\rho$, the inhour equation possesses seven real roots: $\omega_0, \omega_1, \dots, \omega_6$.
For $\rho > 0$, the largest root $\omega_0 > 0$ defines the <strong>stable reactor period</strong> $T = 1/\omega_0$.
The remaining six roots $\omega_1, \dots, \omega_6$ are negative and die out within tens of seconds. After these transients decay, reactor power escalates cleanly as:
$$\mathbf{P(t) = P_0 e^{t / T}}$$
The <strong>doubling time</strong> $T_d$ (time for power to double) is:
$$\mathbf{T_d = T \ln 2 \approx 0.69315 \, T}$$
</p>
"""
        },
        {
            "id": "sec-8-4",
            "title": "Transient Response to Step Reactivity: The Prompt Jump Approximation",
            "content": r"""
<h3>1. The Prompt Jump Phenomenon</h3>
<p>
When a positive step reactivity $\rho < \beta$ is inserted into a critical reactor at $t = 0$, the neutron population exhibits a two-stage response:
<ol>
  <li><strong>The Prompt Jump (0 to 10 ms):</strong> Because delayed precursors cannot change instantaneously ($C_i(0^+) = C_i(0^-) = \frac{\beta_i}{\Lambda} n_0$), the prompt neutron population jumps almost instantaneously until the prompt sink balances precursor emission:
  $$\frac{dn}{dt} \approx 0 \implies \frac{\rho - \beta}{\Lambda} n(0^+) + \sum \lambda_i C_i(0) = 0 \implies \frac{\beta - \rho}{\Lambda} n(0^+) = \frac{\beta}{\Lambda} n_0$$
  $$\mathbf{n(0^+) = n_0 \frac{\beta}{\beta - \rho} = n_0 \frac{1}{1 - \rho/\beta} = n_0 \frac{1}{1 - \$}}$$
  </li>
  <li><strong>Precursor-Controlled Growth ($t > 1\text{ s}$):</strong> Following the prompt jump, power increases on the slow stable period $T \approx \frac{\beta - \rho}{\lambda_{\text{eff}} \rho}$:
  $$\mathbf{n(t) \approx n_0 \left[ \frac{\beta}{\beta - \rho} \exp\left( \frac{\lambda_{\text{eff}} \rho}{\beta - \rho} t \right) - \frac{\rho}{\beta - \rho} \exp\left( - \frac{\beta - \rho}{\Lambda} t \right) \right]}$$
</ol>
</p>
"""
        },
        {
            "id": "sec-8-5",
            "title": "Control Rod Physics: Perturbation Theory, Rod Worth & Burnable Absorbers",
            "content": r"""
<h3>1. Control Rod Worth via First-Order Perturbation Theory</h3>
<p>
Control rods contain strong neutron-absorbing materials (such as Boron Carbide $\text{B}_4\text{C}$, Cadmium, Silver-Indium-Cadmium Ag-In-Cd, or Hafnium).
When a control rod is partially inserted to depth $z$ into a cylindrical reactor of active height $H$, first-order perturbation theory shows that the differential reactivity worth $d\rho/dz$ is proportional to the square of the unperturbed axial flux:
$$\frac{d\rho}{dz} \propto \phi^2(z) = \phi_0^2 \sin^2\left( \frac{\pi z}{H} \right)$$
Integrating from $0$ to $z$ yields the cumulative <strong>Integral Control Rod Worth</strong> $\rho(z)$:
$$\rho(z) = \rho_{\text{tot}} \frac{\int_0^z \sin^2(\pi z'/H) dz'}{\int_0^H \sin^2(\pi z'/H) dz'} = \mathbf{\rho_{\text{tot}} \left[ \frac{z}{H} - \frac{1}{2\pi} \sin\left( \frac{2\pi z}{H} \right) \right]}$$
This exhibits the characteristic <strong>S-curve</strong>:
<ul>
  <li>Near the top ($z \approx 0$) and bottom ($z \approx H$), flux is low, so rod movement produces tiny reactivity change.</li>
  <li>Near the core midplane ($z = H/2$), flux is maximal, so rod movement produces maximum differential worth: $\left.\frac{d\rho}{dz}\right|_{\max} = \frac{2 \rho_{\text{tot}}}{H}$.</li>
</ul>
</p>

<h3>2. Burnable Absorbers</h3>
<p>
To compensate for the large excess reactivity of freshly loaded fuel without requiring dozens of physical control rods, reactors incorporate <strong>burnable poisons</strong> (such as Gadolinium Oxide $\text{Gd}_2\text{O}_3$ or Boron in fuel cladding). These high cross-section isotopes burn away at the same rate as fuel fissile inventory decreases, keeping net core reactivity nearly flat throughout a 24-month operating cycle.
</p>
"""
        },
        {
            "id": "sec-8-6",
            "title": "Inherent Reactivity Feedback: Fuel Doppler, Moderator & Void Coefficients",
            "content": r"""
<h3>1. Reactivity Coefficients of Temperature</h3>
<p>
Any temperature increase in a reactor core alters material densities, thermal cross sections, and resonance absorption, producing net reactivity feedback:
$$\frac{d\rho}{dt} = \alpha_F \frac{dT_{\text{fuel}}}{dt} + \alpha_M \frac{dT_{\text{mod}}}{dt} + \alpha_V \frac{d\alpha_{\text{void}}}{dt}$$
<ul>
  <li><strong>Fuel Doppler Coefficient ($\alpha_F$):</strong> Promptly negative ($\alpha_F \sim -2\text{ to }-4\text{ pcm/}^\circ\text{C}$). Operates with zero thermal delay because heat is born directly inside the $\text{UO}_2$ crystals, instantly broadening ${}^{238}\text{U}$ resonance capture.</li>
  <li><strong>Moderator Temperature Coefficient ($\alpha_M$):</strong> Governed by coolant thermal expansion. In an under-moderated PWR, heating decreases water density, reducing moderation and lowering $k_{\text{eff}}$ ($\alpha_M \sim -10\text{ to }-40\text{ pcm/}^\circ\text{C} < 0$).</li>
  <li><strong>Void Coefficient of Reactivity ($\alpha_V$):</strong> In BWRs and PWRs, steam bubble formation displaces water. Because the core is under-moderated, voiding decreases reactivity ($\alpha_V < 0$). Conversely, in the Chernobyl RBMK reactor, the over-moderated graphite design caused a positive void coefficient ($\alpha_V > 0$), which contributed directly to the runaway power explosion in 1986.</li>
</ul>
Modern nuclear regulatory safety mandates an unconditionally negative power coefficient of reactivity under all operating states.
</p>
"""
        },
        {
            "id": "sec-8-7",
            "title": "Fission Product Poisoning: Xenon-135 Dynamics, The Iodine Pit & Samarium-149",
            "content": r"""
<h3>1. Xenon-135: The Super-Poison</h3>
<p>
Xenon-135 (${}^{135}\text{Xe}$) is the most potent neutron poison known to science, with a microscopic thermal absorption cross section of:
$$\mathbf{\sigma_a({}^{135}\text{Xe}) \approx 2.65 \times 10^6\text{ barns} = 2.65 \times 10^{-18}\text{ cm}^2}$$
(Over $3{,}800$ times greater than ${}^{235}\text{U}$ fission!).
</p>

<h3>2. The Iodine-Xenon Dynamic System</h3>
<p>
${}^{135}\text{Xe}$ is formed through two pathways:
<ol>
  <li>Direct fission yield: $\gamma_{\text{Xe}} \approx 0.003$ ($0.3\%$).</li>
  <li>Radioactive decay of Iodine-135 (${}^{135}\text{I}$, yield $\gamma_I \approx 0.061 = 6.1\%$):
  $$\text{Fission} \longrightarrow {}^{135}_{53}\text{I} \xrightarrow[\beta^-, \, T_{1/2}=6.57\text{ h}]{} {}^{135}_{54}\text{Xe} \xrightarrow[\beta^-, \, T_{1/2}=9.14\text{ h}]{} {}^{135}_{55}\text{Cs}$$
</ol>
The coupled non-linear differential equations are:
$$\mathbf{\frac{d I(t)}{dt} = \gamma_I \Sigma_f \phi(t) - \lambda_I I(t)}$$
$$\mathbf{\frac{d X(t)}{dt} = \gamma_{\text{Xe}} \Sigma_f \phi(t) + \lambda_I I(t) - \lambda_{\text{Xe}} X(t) - \sigma_a^{\text{Xe}} X(t) \phi(t)}$$
where:
$$\lambda_I = \frac{\ln 2}{6.57 \times 3600\text{ s}} \approx 2.93 \times 10^{-5}\text{ s}^{-1}, \qquad \lambda_{\text{Xe}} = \frac{\ln 2}{9.14 \times 3600\text{ s}} \approx 2.10 \times 10^{-5}\text{ s}^{-1}$$
At steady-state full power:
$$I_0 = \frac{\gamma_I \Sigma_f \phi_0}{\lambda_I}, \qquad X_0 = \frac{(\gamma_I + \gamma_{\text{Xe}}) \Sigma_f \phi_0}{\lambda_{\text{Xe}} + \sigma_a^{\text{Xe}} \phi_0}$$
</p>

<h3>3. Post-Shutdown Xenon Peak ("The Iodine Pit")</h3>
<p>
When a reactor trips or is shut down from high power ($\phi \to 0$):
<ul>
  <li>Xenon destruction by neutron burnup ($\sigma_a^{\text{Xe}} X \phi$) abruptly drops to zero!</li>
  <li>Meanwhile, the large pre-existing inventory of Iodine-135 continues to decay into Xenon-135 at rate $\lambda_I I(t)$.</li>
  <li>Because $\lambda_I > \lambda_{\text{Xe}}$ ($T_{1/2}^I = 6.6\text{ h} < T_{1/2}^{\text{Xe}} = 9.1\text{ h}$), Xenon production initially outpaces its decay!</li>
</ul>
Xenon concentration swells to a colossal peak approximately $10\text{ to }11\text{ hours}$ after shutdown:
$$t_{\text{peak}} = \frac{1}{\lambda_{\text{Xe}} - \lambda_I} \ln\left( \frac{\lambda_{\text{Xe}}}{\lambda_I} \left[ 1 + \frac{\lambda_{\text{Xe}} - \lambda_I}{\lambda_I} \frac{X_0}{I_0} \right] \right) \approx \mathbf{10.5\text{ hours}}$$
In high-flux reactors, this peak introduces a massive negative reactivity deficit ($\Delta\rho \sim -3000\text{ to }-5000\text{ pcm}$) that completely exceeds control rod withdrawal worth—locking the reactor in a temporary shutdown state known as <strong>Xenon Deadtime</strong>!
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-8-1",
            "title": "Prompt Jump and Stable Reactor Period Calculation for Step Reactivity Insertions",
            "statement": r"""A critical Uranium-235 fueled thermal research reactor operates at steady thermal power $P_0 = 100\text{ kW}$.
The kinetics parameters are:
- Total delayed neutron fraction $\beta = 0.0065$
- Prompt neutron generation time $\Lambda = 5.0 \times 10^{-5}\text{ seconds}$
- Effective one-group precursor decay constant $\bar{\lambda} = 0.080\text{ s}^{-1}$
At $t = 0$, an operator accidentally withdraws a control rod, inserting a positive step reactivity of $\rho = +0.0020$ ($+200\text{ pcm} = 0.308\$$).
(a) Calculate the instantaneous power $P(0^+)$ immediately following the prompt jump.
(b) Using the one delayed group inhour equation $\rho = \frac{\Lambda}{T} + \frac{\beta}{1 + \bar{\lambda} T}$, determine the asymptotic stable reactor period $T$ in seconds.
(c) Calculate the reactor doubling time $T_d$, and compute the reactor power at $t = 30\text{ seconds}$ after insertion.""",
            "solution": r"""**(a) Power Immediately Following Prompt Jump:**
Using the prompt jump formula:
$$P(0^+) = P_0 \frac{\beta}{\beta - \rho} = P_0 \frac{0.0065}{0.0065 - 0.0020} = P_0 \frac{0.0065}{0.0045} = P_0 \left( \frac{13}{9} \right) \approx 1.4444 \, P_0$$
$$P(0^+) = 1.4444 \times 100\text{ kW} \approx \mathbf{144.4\text{ kW}}$$
Within a fraction of a millisecond, the power jumps by $+44.4\%$ before delayed precursors have had time to decay!

**(b) Stable Reactor Period $T$:**
Since $T \gg \Lambda/\beta$, the prompt term $\Lambda/T$ is negligible compared to precursor terms:
$$\rho \approx \frac{\beta}{1 + \bar{\lambda} T} \implies 1 + \bar{\lambda} T = \frac{\beta}{\rho}$$
$$\bar{\lambda} T = \frac{\beta}{\rho} - 1 = \frac{\beta - \rho}{\rho}$$
$$T \approx \frac{\beta - \rho}{\bar{\lambda} \rho}$$
Substituting numerical values:
$$T \approx \frac{0.0065 - 0.0020}{(0.080\text{ s}^{-1})(0.0020)} = \frac{0.0045}{0.000160} = \mathbf{28.125\text{ seconds}}$$
Checking the prompt term correction:
$$\rho = \frac{5.0 \times 10^{-5}}{28.125} + \frac{0.0065}{1 + 0.080 \times 28.125} = 1.78 \times 10^{-6} + \frac{0.0065}{3.25} = 0.0000018 + 0.0020000 \approx 0.002002$$
The stable asymptotic reactor period is **$T = 28.1\text{ seconds}$**.

**(c) Doubling Time and Power at $t = 30\text{ s}$:**
Doubling time:
$$T_d = T \ln 2 = 28.125 \times 0.69315 \approx \mathbf{19.5\text{ seconds}}$$
After the prompt jump, power increases as $P(t) = P(0^+) e^{t/T}$:
$$P(30\text{ s}) = 144.4\text{ kW} \times \exp\left( \frac{30}{28.125} \right) = 144.4 \times e^{1.0667} = 144.4 \times 2.9056 \approx \mathbf{419.7\text{ kW}}$$
At $30\text{ seconds}$, reactor power has risen to **$420\text{ kW}$**."""
        },
        {
            "id": "rp-prob-8-2",
            "title": "Equilibrium Xenon-135 Poisoning and Maximum Post-Shutdown Iodine Pit",
            "statement": r"""A high-power commercial PWR operates at steady thermal neutron flux $\phi_0 = 1.20 \times 10^{14}\text{ neutrons/cm}^2\cdot\text{s}$.
The nuclear parameters are:
- Macroscopic thermal fission cross section $\Sigma_f = 0.115\text{ cm}^{-1}$
- Iodine-135 fission yield $\gamma_I = 0.061$, decay constant $\lambda_I = 2.87 \times 10^{-5}\text{ s}^{-1}$ ($T_{1/2} = 6.70\text{ h}$)
- Xenon-135 fission yield $\gamma_{\text{Xe}} = 0.003$, decay constant $\lambda_{\text{Xe}} = 2.09 \times 10^{-5}\text{ s}^{-1}$ ($T_{1/2} = 9.20\text{ h}$)
- Xenon microscopic absorption cross section $\sigma_a^{\text{Xe}} = 2.65 \times 10^6\text{ b} = 2.65 \times 10^{-18}\text{ cm}^2$
- Core macroscopic absorption cross section $\Sigma_a = 0.160\text{ cm}^{-1}$
(a) Calculate the steady-state equilibrium concentrations of Iodine-135 ($I_0$) and Xenon-135 ($X_0$) in $\text{atoms/cm}^3$.
(b) Calculate the equilibrium xenon reactivity worth $\rho_{\text{Xe}} = -\frac{\Sigma_a^{\text{Xe}}}{\Sigma_a} = -\frac{X_0 \sigma_a^{\text{Xe}}}{\Sigma_a}$ in pcm.
(c) The reactor is suddenly scrammed (shutdown to zero flux $\phi = 0$). Calculate the time $t_{\text{peak}}$ at which the post-shutdown Xenon concentration reaches its maximum, and determine the peak xenon reactivity penalty in pcm.""",
            "solution": r"""**(a) Equilibrium Concentrations $I_0$ and $X_0$:**
Fission rate density:
$$R_f = \Sigma_f \phi_0 = (0.115\text{ cm}^{-1})(1.20 \times 10^{14}\text{ cm}^{-2}\text{s}^{-1}) = 1.380 \times 10^{13}\text{ fissions/cm}^3\cdot\text{s}$$
Equilibrium Iodine-135:
$$I_0 = \frac{\gamma_I \Sigma_f \phi_0}{\lambda_I} = \frac{0.061 \times 1.380 \times 10^{13}}{2.87 \times 10^{-5}\text{ s}^{-1}} = \frac{8.418 \times 10^{11}}{2.87 \times 10^{-5}} \approx \mathbf{2.933 \times 10^{16}\text{ atoms/cm}^3}$$
Xenon destruction rate constant at power:
$$\lambda_{\text{Xe}} + \sigma_a^{\text{Xe}} \phi_0 = 2.09 \times 10^{-5} + (2.65 \times 10^{-18} \times 1.20 \times 10^{14}) = 2.09 \times 10^{-5} + 3.18 \times 10^{-4} \approx 3.389 \times 10^{-4}\text{ s}^{-1}$$
Note that neutron burnup dominates Xenon radioactive decay by a factor of $15$!
Total direct and decay yield:
$$\gamma_{\text{tot}} R_f = (0.061 + 0.003) \times 1.380 \times 10^{13} = 0.064 \times 1.380 \times 10^{13} = 8.832 \times 10^{11}\text{ atoms/cm}^3\cdot\text{s}$$
Equilibrium Xenon-135:
$$X_0 = \frac{8.832 \times 10^{11}}{3.389 \times 10^{-4}} \approx \mathbf{2.606 \times 10^{15}\text{ atoms/cm}^3}$$

**(b) Equilibrium Xenon Reactivity Worth:**
$$\Sigma_a^{\text{Xe}} = X_0 \cdot \sigma_a^{\text{Xe}} = (2.606 \times 10^{15}\text{ cm}^{-3})(2.65 \times 10^{-18}\text{ cm}^2) \approx 0.006906\text{ cm}^{-1}$$
Reactivity worth:
$$\rho_{\text{Xe}} = -\frac{\Sigma_a^{\text{Xe}}}{\Sigma_a} = -\frac{0.006906}{0.160} \approx -0.04316 = \mathbf{-4316\text{ pcm}}$$
At full power, equilibrium xenon absorbs over $4.3\%$ of core reactivity!

**(c) Post-Shutdown Xenon Peak:**
Following shutdown ($\phi = 0$), the Xenon concentration as a function of time $t$ is:
$$X(t) = X_0 e^{-\lambda_{\text{Xe}} t} + \frac{\lambda_I I_0}{\lambda_I - \lambda_{\text{Xe}}} \left( e^{-\lambda_{\text{Xe}} t} - e^{-\lambda_I t} \right)$$
Setting $dX/dt = 0$:
$$t_{\text{peak}} = \frac{1}{\lambda_I - \lambda_{\text{Xe}}} \ln\left( \frac{\lambda_I}{\lambda_{\text{Xe}}} \left[ 1 - \frac{\lambda_I - \lambda_{\text{Xe}}}{\lambda_I} \frac{X_0}{I_0} \right]^{-1} \right)$$
Here $\lambda_I - \lambda_{\text{Xe}} = (2.87 - 2.09) \times 10^{-5} = 0.78 \times 10^{-5}\text{ s}^{-1}$:
$$\frac{\lambda_I - \lambda_{\text{Xe}}}{\lambda_I} \frac{X_0}{I_0} = \frac{0.78}{2.87} \times \frac{2.606 \times 10^{15}}{2.933 \times 10^{16}} = 0.2718 \times 0.08885 \approx 0.02415$$
$$1 - 0.02415 = 0.97585 \implies \frac{\lambda_I}{\lambda_{\text{Xe}} \times 0.97585} = \frac{2.87}{2.09 \times 0.97585} \approx 1.4072$$
$$t_{\text{peak}} = \frac{\ln(1.4072)}{0.78 \times 10^{-5}\text{ s}^{-1}} = \frac{0.3416}{0.78 \times 10^{-5}} \approx 43{,}790\text{ seconds} \approx \mathbf{10.2\text{ hours}}$$
Evaluating $X(t_{\text{peak}})$ at $t = 43{,}790\text{ s}$:
$$e^{-\lambda_{\text{Xe}} t} = \exp(-2.09 \times 10^{-5} \times 43790) = e^{-0.9152} \approx 0.4004$$
$$e^{-\lambda_I t} = \exp(-2.87 \times 10^{-5} \times 43790) = e^{-1.2568} \approx 0.2846$$
$$X_{\text{peak}} = (2.606 \times 10^{15})(0.4004) + \frac{2.87 \times 10^{-5} \times 2.933 \times 10^{16}}{0.78 \times 10^{-5}} (0.4004 - 0.2846)$$
$$X_{\text{peak}} = 1.043 \times 10^{15} + (1.0792 \times 10^{17})(0.1158) = 1.043 \times 10^{15} + 1.250 \times 10^{16} \approx \mathbf{1.354 \times 10^{16}\text{ atoms/cm}^3}$$
Peak Xenon reactivity penalty:
$$\rho_{\text{Xe, peak}} = -\frac{(1.354 \times 10^{16})(2.65 \times 10^{-18})}{0.160} = -\frac{0.03588}{0.160} \approx \mathbf{-22{,}425\text{ pcm}} = \mathbf{-22.4\%\ \Delta k/k}$$
Ten hours after shutdown, the xenon reactivity pit deepens by an extra **$-18{,}100\text{ pcm}$**, completely poisoning the reactor core!"""
        },
        {
            "id": "rp-prob-8-3",
            "title": "Cylindrical Control Rod Worth and Reactivity Depth Profile via Perturbation Theory",
            "statement": r"""A central control rod in a critical cylindrical reactor of core height $H = 3.60\text{ m}$ has a total shutdown worth of $\rho_{\text{tot}} = -3200\text{ pcm}$.
The axial thermal neutron flux is $\phi(z) = \phi_0 \sin\left( \frac{\pi z}{H} \right)$, where $z = 0$ is the top of the core and $z = H$ is the bottom.
The rod is inserted from the top ($z = 0$) downward.
(a) Using first-order perturbation theory, write the expression for the differential rod worth $w(z) = \frac{d\rho}{dz}$ and find the position of maximum differential worth.
(b) Calculate the maximum differential worth in $\text{pcm/cm}$.
(c) Calculate the integral reactivity inserted when the control rod is inserted to depths $z = 0.90\text{ m}$ (quarter insertion), $z = 1.80\text{ m}$ (half insertion), and $z = 2.70\text{ m}$ (three-quarter insertion).""",
            "solution": r"""**(a) Differential Rod Worth Expression:**
By first-order perturbation theory:
$$\frac{d\rho}{dz} = C \sin^2\left( \frac{\pi z}{H} \right)$$
Normalizing such that $\int_0^H \frac{d\rho}{dz} dz = \rho_{\text{tot}}$:
$$\int_0^H \sin^2\left( \frac{\pi z}{H} \right) dz = \frac{H}{2} \implies C \frac{H}{2} = \rho_{\text{tot}} \implies C = \frac{2 \rho_{\text{tot}}}{H}$$
Thus:
$$w(z) = \frac{d\rho}{dz} = \mathbf{\frac{2 \rho_{\text{tot}}}{H} \sin^2\left( \frac{\pi z}{H} \right)}$$
Maximum differential worth occurs at the core midplane where $\sin(\pi z/H) = 1$:
$$z_{\max} = \frac{H}{2} = \frac{3.60\text{ m}}{2} = \mathbf{1.80\text{ m}}$$

**(b) Maximum Differential Worth Value:**
With $\rho_{\text{tot}} = -3200\text{ pcm}$ and $H = 360\text{ cm}$:
$$w_{\max} = \frac{2 \times (-3200\text{ pcm})}{360\text{ cm}} \approx \mathbf{-17.78\text{ pcm/cm}}$$
At the core center, moving the control rod by just $1.0\text{ cm}$ introduces **$-17.8\text{ pcm}$** of reactivity.

**(c) Integral Worth at Selected Depths:**
Using the integral S-curve formula $\rho(z) = \rho_{\text{tot}} \left[ \frac{z}{H} - \frac{1}{2\pi} \sin\left( \frac{2\pi z}{H} \right) \right]$:
- At quarter insertion ($z = 0.90\text{ m} = H/4$):
  $$\frac{z}{H} = 0.25, \qquad \frac{2\pi z}{H} = \frac{\pi}{2} \implies \sin\left(\frac{\pi}{2}\right) = 1$$
  $$\rho(H/4) = \rho_{\text{tot}} \left[ 0.25 - \frac{1}{2\pi} \right] = (-3200) [0.25 - 0.15915] = (-3200)(0.09085) \approx \mathbf{-290.7\text{ pcm}}$$
  Quarter rod travel produces only **$9.1\%$** of total worth!

- At half insertion ($z = 1.80\text{ m} = H/2$):
  $$\frac{z}{H} = 0.50, \qquad \frac{2\pi z}{H} = \pi \implies \sin(\pi) = 0$$
  $$\rho(H/2) = \rho_{\text{tot}} [0.50 - 0] = 0.50 \times (-3200) = \mathbf{-1600.0\text{ pcm}}$$
  Exactly half the worth (**$50\%$**) is inserted at the core midplane.

- At three-quarter insertion ($z = 2.70\text{ m} = 3H/4$):
  $$\frac{z}{H} = 0.75, \qquad \frac{2\pi z}{H} = \frac{3\pi}{2} \implies \sin\left(\frac{3\pi}{2}\right) = -1$$
  $$\rho(3H/4) = \rho_{\text{tot}} \left[ 0.75 - \left(-\frac{1}{2\pi}\right) \right] = (-3200) [0.75 + 0.15915] = (-3200)(0.90915) \approx \mathbf{-2909.3\text{ pcm}}$$
  Three-quarter insertion yields **$90.9\%$** of total worth. Moving through the middle half of the core ($H/4$ to $3H/4$) accounts for over **$81.8\%$** of the entire control rod reactivity!"""
        }
    ]
}

with open("rp_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2, ensure_ascii=False)

with open("rp_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8_data, f, indent=2, ensure_ascii=False)

print("rp_u7.json and rp_u8.json successfully written!")
