# -*- coding: utf-8 -*-
"""
Generator for nuclear-physics-2.html with SEO pre-rendered Unit 1
"""
import json

with open("nuc2_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

sections_html = []
for sec in u1["sections"]:
    sec_id = sec["id"]
    sec_title = sec["title"]
    sec_content = sec["content"].strip()
    sec_num = "§1." + sec_id.split("-")[-1]
    
    sim_markup = ""
    if "simulation" in sec:
        sim_id = sec["simulation"]
        sim_markup = f'\n  <div id="sim-{sec_id}" class="sim-mount-point"></div>'
        
    s_html = f'''<section class="textbook-section-card" id="{sec_id}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{sec_num}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{sec_content}
  </div>{sim_markup}
</section>'''
    sections_html.append(s_html)

problems_html = []
for i, prob in enumerate(u1.get("problems", []), 1):
    pid = prob["id"]
    ptitle = prob["title"]
    pstatement = prob["statement"]
    psolution = prob["solution"]
    
    p_card = f'''<div class="problem-card" id="{pid}">
  <div class="problem-header">
    <div class="prob-badge">SOLVED PROBLEM 1.{i}</div>
    <h4 class="prob-title">{ptitle}</h4>
  </div>
  <div class="problem-statement">
    <p>{pstatement}</p>
  </div>
  <div class="solution-container">
    <div class="solution-header">
      <span class="sol-tag">RIGOROUS DERIVATION & EXAM SOLUTION</span>
    </div>
    <div class="solution-steps">
      <div class="solution-step">
        <div class="step-title">Full Rigorous Analytical Solution</div>
        <div class="step-explanation">{psolution}</div>
      </div>
      <div class="solution-step" style="border-left-color: #10b981;">
        <div class="step-title" style="color: #10b981;">Final Answer & Verification</div>
        <div class="step-explanation"><p><strong>Complete rigorous derivation and proof detailed above.</strong></p></div>
      </div>
    </div>
  </div>
</div>'''
    problems_html.append(p_card)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Nuclear Physics II: Two-Body Bound States, Nuclear Forces, Reaction Models & Hadron Symmetries | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering the deuteron bound state, electric quadrupole moment, photodisintegration, N-N scattering, phase shifts, effective range theory, ortho/para-hydrogen, Yukawa meson theory, One-Boson-Exchange model, isospin SU(2)_I, electromagnetic multipole transitions, Weisskopf single-particle rates, internal conversion, Giant Dipole Resonance, Mayer-Jensen spin-orbit shell model, Bohr-Mottelson collective deformations, Coriolis backbending, optical model, compound resonances, Breit-Wigner formula, deep inelastic scattering, Cornell quark confinement, parity violation in 60Co, neutral kaon CP violation, SU(3) flavor Eightfold Way, Gell-Mann-Okubo formula, Ω⁻ discovery, QCD, electroweak unification, and PMNS neutrino oscillations with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Nuclear Physics II, Deuteron Bound State, Tensor Force, D-State Admixture, Photodisintegration, N-N Scattering, Phase Shifts, Scattering Lengths, Effective Range Expansion, Ortho Para Hydrogen, Isospin Symmetries, Yukawa Potential, Meson Exchange, One-Boson-Exchange OBE, Multipole Selection Rules, Weisskopf Rates, Internal Conversion, Giant Dipole Resonance, Shell Model, Woods-Saxon, Mayer-Jensen Spin-Orbit, Magic Numbers, Collective Bohr-Mottelson, Rotational Bands, Coriolis Backbending, Optical Model, Compound Nucleus, Breit-Wigner Resonance, Deep Inelastic Scattering, Quark Confinement, Parity Violation, CP Violation Neutral Kaons, Eightfold Way SU(3) Flavor, Gell-Mann-Okubo Mass Formula, Omega-Minus Discovery, QCD Asymptotic Freedom, Electroweak Unification, Neutrino Oscillations PMNS">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/nuclear-physics-2.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Nuclear Physics II: Two-Body Bound States, Nuclear Forces, Reaction Models & Hadron Symmetries | OpenSTEM">
  <meta property="og:description" content="University honors course with 8 exhaustive chapters, complete mathematical derivations, 24 solved honors exam problems, and 16 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Nuclear Physics II: Two-Body Bound States, Nuclear Forces, Reaction Models & Hadron Symmetries",
    "description": "Comprehensive university honors curriculum covering the deuteron problem, nucleon-nucleon scattering, One-Boson-Exchange meson theory, multipole radiation, advanced shell and collective models, optical model reactions, Breit-Wigner resonances, discrete symmetries, CP violation, SU(3) flavor Eightfold Way, Quantum Chromodynamics, and electroweak unification.",
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
  <link rel="stylesheet" href="styles.css?v=20261005_v19">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Nuclear Physics II</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search deuteron, scattering, quarks, SU(3)..." class="search-input">
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
          <span class="badge-pill badge-course">Physics / Nuclear Physics II</span>
          <span class="badge-pill badge-credits">Hadron Symmetries & Nuclear Forces</span>
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
{chr(10).join(sections_html)}
          </div>

          <!-- Unit Solved Problems -->
          <div id="unit-problems-container" style="margin-top: 3rem;">
            <header class="sec-header" style="margin-top: 2rem;">
              <h3 class="sec-title" style="color: #f59e0b;"><span class="sec-num">★</span><span>Solved Examination Problems: Chapter 1</span></h3>
            </header>
            <div class="problems-grid">
{chr(10).join(problems_html)}
            </div>
          </div>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="nuclear-physics-2-sims.js?v=20261005_v19"></script>
  <script src="nuclear-physics-2-data.js?v=20261005_v19"></script>
  <script src="app.js?v=20261005_v19"></script>
</body>
</html>
'''

with open("nuclear-physics-2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("nuclear-physics-2.html successfully generated!")
