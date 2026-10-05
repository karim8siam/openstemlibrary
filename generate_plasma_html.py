# generate_plasma_html.py
# Generates plasma-physics.html with pre-rendered Chapter 1 for SEO, schema.org JSON-LD, and KaTeX math rendering.

import json

with open("plasma_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

# Format Chapter 1 sections HTML
sections_html = ""
for s_idx, sec in enumerate(u1["sections"]):
    raw_num = f"1.{s_idx + 1}"
    sec_id = sec.get("id", f"sec-1-{s_idx + 1}")
    title = sec.get("title", "")
    content = sec.get("content", "")
    
    # Check if section has a simulation
    sim_html = ""
    if s_idx == 3: # sec-1-4: Debye shielding
        sim_html = '''
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-plasma-debye-shielding-sim"></div>
          </div>
        '''
    elif s_idx == 6: # sec-1-7: DC discharge Paschen curve
        sim_html = '''
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-plasma-dc-discharge-paschen-sim"></div>
          </div>
        '''

    sections_html += f"""
<section class="textbook-section-card" id="{sec_id}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">§{raw_num}</span><span>{title}</span></h3>
  </header>
  <div class="sec-content">
{content}
  </div>
{sim_html}
</section>
"""

# Format Chapter 1 solved problems HTML
problems_html = ""
for p_idx, prob in enumerate(u1["problems"]):
    prob_num = f"1.{p_idx + 1}"
    prob_id = prob.get("id", f"plasma-prob-1-{p_idx + 1}")
    title = prob.get("title", "")
    statement = prob.get("statement", "")
    solution = prob.get("solution", "")

    problems_html += f"""
<div class="problem-card" id="{prob_id}">
  <div class="problem-header">
    <div class="prob-badge">SOLVED PROBLEM {prob_num}</div>
    <h4 class="prob-title">{title}</h4>
  </div>
  <div class="problem-statement">
    <p>{statement}</p>
  </div>
  <div class="solution-container">
    <div class="solution-header">
      <span class="sol-tag">RIGOROUS DERIVATION & EXAM SOLUTION</span>
    </div>
    <div class="solution-steps">
      <div class="solution-step">
        <div class="step-title">Full Rigorous Analytical Solution</div>
        <div class="step-explanation">{solution}</div>
      </div>
      <div class="solution-step" style="border-left-color: #10b981;">
        <div class="step-title" style="color: #10b981;">Final Answer & Verification</div>
        <div class="step-explanation"><p><strong>Complete rigorous derivation and proof detailed above.</strong></p></div>
      </div>
    </div>
  </div>
</div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Plasma Physics: Single-Particle Dynamics, Fluid Theory, Waves, MHD & Kinetic Landau Damping | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering Debye shielding, plasma parameters, single-particle Lorentz dynamics, guiding center drifts, adiabatic invariants, magnetic mirrors, multi-fluid equations, diamagnetic drift, ideal magnetohydrodynamics (MHD), flux-freezing, electrostatic Langmuir and ion acoustic waves, electromagnetic waves in magnetized plasmas, whistlers, Faraday rotation, shear Alfvén waves, fast/slow magnetosonic modes, Rayleigh-Taylor and kink instabilities, Vlasov kinetic theory, and collisionless Landau damping with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Plasma Physics Textbook, Debye Shielding, Debye Length, Plasma Parameter, Saha Ionization Equation, Paschen Law, Townsend Avalanche, DC Glow Discharge, Cyclotron Frequency, Larmor Radius, ExB Drift, Polarization Drift, Grad-B Drift, Curvature Drift, Magnetic Mirror, First Adiabatic Invariant, Loss Cone, Diamagnetic Drift, Two-Fluid Plasma, Generalized Ohm Law, Ideal MHD, Magnetic Flux Freezing, Alfven Theorem, Sweet-Parker Reconnection, Langmuir Oscillations, Bohm-Gross Wave, Ion Acoustic Wave, Transverse EM Waves, Plasma Cutoff, Skin Depth, Whistler Waves, Faraday Rotation, Shear Alfven Waves, Magnetosonic Waves, Rayleigh-Taylor Instability, Kruskal-Shafranov Limit, Kink Instability, Vlasov Equation, Landau Damping, BGK Modes, Collisionless Dissipation">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/plasma-physics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Plasma Physics: Waves, MHD & Landau Damping | OpenSTEM Digital Textbook">
  <meta property="og:description" content="University honors course with 8 exhaustive chapters, complete mathematical derivations, 24 solved honors exam problems, and 16 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Plasma Physics: Single-Particle Dynamics, Fluid Theory, Waves, MHD & Kinetic Landau Damping",
    "description": "Comprehensive university honors curriculum covering Debye screening, single-particle guiding center drifts, magnetic mirrors, two-fluid theory, ideal MHD, electrostatic and electromagnetic waves, whistlers, Alfvén waves, MHD instabilities, and Vlasov-Landau kinetic damping.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.org"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & Graduate",
    "isAccessibleForFree": true
  }}
  </script>

  <!-- Google Fonts: Inter & Fira Code -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Application Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261005_v17">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Plasma Physics & MHD</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search topics, equations, drifts, waves..." class="search-input">
      </div>

      <div class="nav-section-title">Table of Contents</div>
      <ul class="unit-nav-list" id="unit-nav-list">
        <!-- Rendered dynamically by app.js from COURSE_DATA -->
      </ul>
    </aside>

    <!-- Main Content Reader Container -->
    <main class="main-content">
      <!-- Top Sticky Navbar -->
      <header class="top-navbar">
        <div class="course-badge-container">
          <span class="badge-pill badge-course">Physics / Plasma Physics</span>
          <span class="badge-pill badge-credits">Plasma Physics & MHD</span>
          <span class="badge-pill" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">100% Free Open Access</span>
        </div>
        <div class="navbar-actions">
          <a href="index.html" class="btn-tool" style="text-decoration:none; display:flex; align-items:center; gap:0.35rem; color:#38bdf8;">← STEM Library</a>
          <button id="btn-font-toggle" class="btn-tool" title="Toggle Academic Reading Font">A/A Academic</button>
          <div class="protection-notice">
            🔒 <span>In-Browser Protected • Direct Download Disabled</span>
          </div>
        </div>
      </header>

      <!-- Content Columns (Wide Centered Reader) -->
      <div class="content-columns" id="main-content-area">
        <!-- Center Textbook Article -->
        <article class="reader-main-column" id="textbook-article">
          <!-- Chapter Hero Header -->
          <header class="unit-hero">
            <div class="unit-number-tag" id="unit-tag">Chapter 1 • Theory & Derivations</div>
            <h1 class="unit-title-heading" id="unit-title">{u1["title"]}</h1>
            <p class="unit-desc-lead" id="unit-desc">
              {u1["summary"]}
            </p>
          </header>

          <!-- Textbook Sections Container -->
          <div id="textbook-sections">
{sections_html}
          </div>

          <!-- Fallback Simulation Wrapper (Mounted dynamically by app.js if needed) -->
          <div id="sim-section-wrap" style="display: none; margin-top: 3rem;">
            <div class="sec-header">
              <h3 class="sec-title"><span>Interactive Laboratory Simulations</span></h3>
            </div>
            <div id="simulations-mount"></div>
          </div>

          <!-- Solved Problems Section -->
          <section class="problems-section-wrapper" style="margin-top: 4rem;">
            <div class="sec-header" style="border-bottom: 2px solid #334155; padding-bottom: 0.75rem; margin-bottom: 2rem;">
              <h3 class="sec-title" style="font-size: 1.4rem; color: #f1f5f9;">
                <span>Honors Examination Worked Problems & Solutions</span>
              </h3>
              <p class="text-muted" style="margin-top: 0.25rem; font-size: 0.9rem;">
                Rigorous step-by-step mathematical proofs and solutions to university degree examination problems.
              </p>
            </div>
            <div id="problems-mount">
{problems_html}
            </div>
          </section>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="plasma-physics-sims.js?v=20261005_v17"></script>
  <script src="plasma-physics-data.js?v=20261005_v17"></script>
  <script src="app.js?v=20261005_v17"></script>
</body>
</html>
"""

with open("plasma-physics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"plasma-physics.html successfully generated ({len(html_content)} bytes)")
