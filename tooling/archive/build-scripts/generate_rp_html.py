# -*- coding: utf-8 -*-
"""
Generator for reactor-physics.html with SEO pre-rendered Unit 1
"""
import json

with open("rp_u1.json", "r", encoding="utf-8") as f:
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
exercises = u1.get("exercises") or u1.get("problems", [])
for i, prob in enumerate(exercises, 1):
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

joined_sections = "\n".join(sections_html)
joined_problems = "\n".join(problems_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Nuclear Reactor Physics: Neutron Diffusion, Chain Reactions, Criticality & Kinetics | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering nuclear reactor physics, fission energetics, atom density calculations, neutron cross sections, reaction rates, liquid drop fission mechanics, Watt prompt spectrum, delayed neutron kinetics, continuous slowing down, Fermi lethargy, moderating ratio, resonance escape, Boltzmann transport equation, P1 approximation, Fick's law, extrapolated boundaries, thermal diffusion length, Fermi age equation, Four-Factor and Six-Factor formulas, reactor criticality in five canonical geometries, optimum cylinder dimensions, two-region reflected core savings, point reactor kinetics PRKE, Inhour equation, prompt jump, reactivity feedback, Doppler broadening, control rod worth S-curves, and Xenon-135 / Samarium-149 poisoning dynamics with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Nuclear Reactor Physics, Neutron Diffusion Theory, Chain Reactions, Four Factor Formula, Six Factor Formula, Criticality, Geometric Buckling, Material Buckling, Finite Cylinder Reactor, Fermi Age Theory, Point Reactor Kinetics, Delayed Neutrons, Inhour Equation, Prompt Criticality, Reactivity Feedback, Fuel Doppler Coefficient, Moderator Temperature Coefficient, Xenon Poisoning, Iodine Pit, Reflector Savings, Fick's Law">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/reactor-physics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Nuclear Reactor Physics: Neutron Diffusion, Chain Reactions, Criticality & Kinetics | OpenSTEM">
  <meta property="og:description" content="University honors course with 8 exhaustive chapters, complete mathematical derivations, 24 solved honors exam problems, and 16 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Nuclear Reactor Physics: Neutron Diffusion, Chain Reactions, Criticality & Kinetics",
    "description": "Comprehensive university honors curriculum covering neutron transport and diffusion, four-factor and six-factor critical multiplication formulas, geometric buckling across canonical core shapes, reflected cores, point kinetics, reactivity feedback, control systems, and xenon poisoning dynamics.",
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
  <link rel="stylesheet" href="styles.css?v=20261005_v20">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Reactor Physics</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search diffusion, buckling, kinetics, xenon, reactivity..." class="search-input">
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
          <span class="badge-pill badge-course">Physics / Reactor Physics</span>
          <span class="badge-pill badge-credits">Nuclear Engineering & Reactor Physics</span>
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

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{joined_sections}
          </div>

          <!-- Pre-Rendered Solved Problems Container -->
          <div id="unit-problems-container" class="problems-wrapper" style="margin-top: 3rem;">
            <div class="problems-section-header">
              <div class="prob-sec-badge">ADVANCED UNIVERSITY HONORS PROBLEMS</div>
              <h3 class="prob-sec-title">Step-by-Step Solved Examination Problems</h3>
              <p class="prob-sec-desc">Comprehensive analytical derivations, quantitative calculations, and step-by-step examination solutions for Unit 1.</p>
            </div>
            <div class="problems-grid" id="problems-container">
{joined_problems}
            </div>
          </div>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="reactor-physics-sims.js?v=20261005_v20"></script>
  <script src="reactor-physics-data.js?v=20261005_v20"></script>
  <script src="app.js?v=20261005_v20"></script>
</body>
</html>
'''

with open("reactor-physics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("reactor-physics.html successfully generated!")
