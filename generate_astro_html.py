# generate_astro_html.py
# Generates astrophysics.html with pre-rendered Chapter 1 for SEO, schema.org JSON-LD, and KaTeX math rendering.

import json

with open("astro_u1.json", "r", encoding="utf-8") as f:
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
    if s_idx == 0:
        sim_html = '''
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-astro-celestial-sphere-sim"></div>
          </div>
        '''
    elif s_idx == 3:
        sim_html = '''
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-astro-distance-ladder-sim"></div>
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
    prob_id = prob.get("id", f"astro-prob-1-{p_idx + 1}")
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
  <title>Astrophysics & Cosmology: Stars, Galaxies, Expansion & The Early Universe | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering celestial mechanics, coordinate systems, astronomical distance ladder, solar physics, thermonuclear p-p and CNO fusion, exoplanetary detection, stellar interiors and Lane-Emden polytropes, stellar evolution, Hertzsprung-Russell diagram, white dwarfs, Chandrasekhar limit, neutron stars, pulsars, General Relativistic Schwarzschild black holes, galactic kinematics, flat rotation curves, dark matter halos, Lin-Shu spiral density waves, active galactic nuclei (AGN), relativistic superluminal jets, gravitational lensing, Hubble-Lemaître cosmic expansion, Friedmann-Lemaître-Robertson-Walker metrics, Big Bang nucleosynthesis, CMB radiation, and astrobiology with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Astrophysics Textbook, Cosmology Textbook, Celestial Coordinates, Right Ascension, Declination, Parallax, Cepheid Leavitt Law, Distance Modulus, Standard Solar Model, Proton-Proton Chain, CNO Cycle, Exoplanet Transit Photometry, Radial Velocity Wobble, Lane-Emden Equation, Polytropes, Hertzsprung-Russell Diagram, Stellar Evolution, Chandrasekhar Mass Limit, Electron Degeneracy, Neutron Stars, Tolman-Oppenheimer-Volkoff, Pulsars, Synchrotron Emission, Schwarzschild Metric, Black Hole Event Horizon, Photon Sphere, ISCO, Galactic Dynamics, Oort Constants, Flat Rotation Curves, Dark Matter NFW Halo, Spiral Density Waves, Lin-Shu Hypothesis, Active Galactic Nuclei, Supermassive Black Holes, Superluminal Motion, Gravitational Lensing, Einstein Ring, Hubble Law, Cosmological Redshift, Friedmann Equations, Dark Energy, Cosmic Microwave Background, Big Bang Nucleosynthesis, Light Element Abundances, Circumstellar Habitable Zone, Drake Equation">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/astrophysics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Astrophysics & Cosmology | OpenSTEM Digital Textbook">
  <meta property="og:description" content="University honors course with 8 exhaustive chapters, complete mathematical derivations, 24 solved honors exam problems, and 16 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Astrophysics & Cosmology: Stars, Galaxies, Expansion & The Early Universe",
    "description": "Comprehensive university honors curriculum covering astronomical coordinates, the distance ladder, stellar physics, degenerate remnants, galactic structure, gravitational lensing, relativistic cosmology, and early universe nucleosynthesis.",
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
  <link rel="stylesheet" href="styles.css?v=20261005_v16">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Astrophysics & Cosmology</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search topics, equations, objects..." class="search-input">
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
          <span class="badge-pill badge-course">Physics / Astrophysics</span>
          <span class="badge-pill badge-credits">Astrophysics & Cosmology</span>
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
  <script src="astrophysics-sims.js?v=20261005_v16"></script>
  <script src="astrophysics-data.js?v=20261005_v16"></script>
  <script src="app.js?v=20261005_v16"></script>
</body>
</html>
"""

with open("astrophysics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"astrophysics.html successfully generated ({len(html_content)} bytes)")
