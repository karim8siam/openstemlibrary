# Generator for classical-mechanics.html with the identical sleek styling as thermal-physics.html
import json

with open("cm_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

# Pre-render sections for Unit 1
sections_html = ""
for idx, sec in enumerate(u1["sections"], 1):
    sim_html = ""
    sim_id = sec.get("simulation")
    if not sim_id and idx == 1:
        sim_id = "particle-system-momentum-sim"
    elif not sim_id and idx == 2:
        sim_id = "rotating-wire-hoop-sim"

    if sim_id:
        sim_html = f'''
  <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
    <div class="simulation-slot" id="sim-container-{sim_id}"></div>
  </div>'''

    sec_title = sec.get("title") or sec.get("heading")
    sections_html += f'''
<section class="textbook-section-card" id="{sec["id"]}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">1.{idx}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{sec["content"]}
  </div>{sim_html}
</section>'''

# Pre-render problems for Unit 1
problems_html = ""
for idx, prob in enumerate(u1["problems"], 1):
    steps_html = ""
    for s_idx, s in enumerate(prob["steps"], 1):
        step_title = s.get("title") or s.get("step") or f"Step {s_idx}"
        step_math = s.get("math") or ""
        step_detail = s.get("explanation") or s.get("detail") or ""
        
        math_block = f'<div class="step-math">{step_math}</div>' if step_math else ""
        steps_html += f'''
<div class="solution-step">
  <div class="step-title">{step_title}</div>
  {math_block}
  <div class="step-explanation"><p>{step_detail}</p></div>
</div>'''

    if prob.get("answer"):
        steps_html += f'''
<div class="solution-step" style="border-left-color: #10b981;">
  <div class="step-title" style="color: #10b981;">Final Answer & Physical Insight</div>
  <div class="step-explanation"><p><strong>{prob["answer"]}</strong></p></div>
</div>'''

    prob_id = prob.get("id") or f"prob-1-{idx}"
    prob_question = prob.get("question") or prob.get("statement") or ""

    problems_html += f'''
<div class="problem-card" id="{prob_id}">
  <div class="problem-header">
    <div class="prob-badge">SOLVED PROBLEM 1.{idx}</div>
    <h4 class="prob-title">{prob["title"]}</h4>
  </div>
  <div class="problem-statement">
    <p>{prob_question}</p>
  </div>
  <div class="solution-container">
    <div class="solution-header">
      <span class="sol-tag">RIGOROUS DERIVATION & EXAM SOLUTION</span>
    </div>
    <div class="solution-steps">
{steps_html}
    </div>
  </div>
</div>'''

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Classical Mechanics: Lagrangian, Hamiltonian & Relativistic Dynamics | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university-standard digital textbook covering Lagrangian & Hamiltonian formulations, rigid body Euler equations, Poisson brackets, and special relativity with 15 interactive 60 FPS simulations.">
  <meta name="keywords" content="Classical Mechanics Textbook, Lagrangian Mechanics, Hamiltonian Dynamics, D'Alembert Principle, Calculus of Variations, Euler Angles, Rigid Body Motion, Poisson Brackets, Liouville Theorem, Special Relativity, Lorentz Transformations, Four Vectors, Minkowski Spacetime">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/classical-mechanics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Classical Mechanics & Relativistic Dynamics | OpenSTEM Textbook">
  <meta property="og:description" content="University-standard course with 8 exhaustive chapters, complete mathematical proofs, solved university problems, and real-time interactive physics simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Classical Mechanics: Lagrangian, Hamiltonian & Relativistic Dynamics",
    "description": "Advanced undergraduate physics course covering analytical mechanics, D'Alembert's principle, variational action, central forces, rigid bodies, canonical transformations, and 4-vector relativistic dynamics.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.org"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors",
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
  <link rel="stylesheet" href="styles.css?v=20261004_v9">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Classical Mechanics</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search topics, equations..." class="search-input">
      </div>

      <div class="nav-section-title">Table of Contents</div>
      <ul class="unit-nav-list" id="unit-nav-list">
        <!-- Rendered dynamically by app.js from COURSE_DATA -->
      </ul>
    </aside>

    <!-- Main Content Area -->
    <main class="main-wrapper">
      <!-- Top Sticky Navbar -->
      <header class="top-navbar">
        <div class="course-badge-container">
          <span class="badge-pill badge-course">Physics</span>
          <span class="badge-pill badge-credits">Classical Mechanics</span>
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

      <!-- Content Columns (Wide Centered Reader, No Right Sidebar) -->
      <div class="content-columns" id="main-content-area">
        <!-- Center Textbook Article -->
        <article class="reader-main-column" id="textbook-article">
          <!-- Chapter Hero Header -->
          <header class="unit-hero">
            <div class="unit-number-tag" id="unit-tag">Chapter 1 • Theory & Derivations</div>
            <h1 class="unit-title-heading" id="unit-title">Review of Elementary Principles & D'Alembert's Principle</h1>
            <p class="unit-desc-lead" id="unit-desc">
              Mechanics of particle systems, classification of kinematic constraints, generalized coordinates, principle of virtual work, D'Alembert's dynamic principle, derivation of Lagrange's equations, generalized velocity-dependent potentials (Lorentz force), and Rayleigh dissipation functions.
            </p>
          </header>

          <!-- Textbook Sections Container -->
          <div id="textbook-sections">
{sections_html}
          </div>

          <!-- Standalone Fallback Simulations Mount (If Any) -->
          <div class="sim-section-wrapper" id="sim-section-wrap" style="display:none;">
            <div class="section-divider">
              <span class="divider-text">CHAPTER NUMERICAL SIMULATIONS</span>
            </div>
            <div id="simulations-mount"></div>
          </div>

          <!-- Solved Problems Section -->
          <section class="problems-section" id="problems-section">
            <div class="problems-section-header">
              <span class="section-tag-pill">EXAMINATION PROBLEM SET</span>
              <h2 class="problems-heading">Standard University Exam Solved Problems</h2>
            </div>
            <div id="problems-container">
{problems_html}
            </div>
          </section>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="classical-mechanics-sims.js?v=20261004_v9"></script>
  <script src="classical-mechanics-data.js?v=20261004_v9"></script>
  <script src="app.js?v=20261004_v9"></script>
</body>
</html>
'''

with open("classical-mechanics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("classical-mechanics.html regenerated with clean styling!")
