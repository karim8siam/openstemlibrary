import json

with open("nuc_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

# Pre-render Unit 1 sections
sec_html = ""
for s_idx, sec in enumerate(u1["sections"]):
    raw_num = f"1.{s_idx + 1}"
    sim_id = sec.get("simulation")
    sim_html = ""
    if sim_id:
        sim_html = f"""  <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
    <div class="simulation-slot" id="sim-container-{sim_id}"></div>
  </div>
"""

    sec_html += f"""<section class="textbook-section-card" id="{sec['id']}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{raw_num}</span><span>{sec['title']}</span></h3>
  </header>
  <div class="sec-content">
{sec['content']}
  </div>
{sim_html}</section>
"""

# Pre-render Unit 1 problems
prob_html = ""
for p_idx, prob in enumerate(u1.get("problems", [])):
    p_num = f"1.{p_idx + 1}"
    
    steps_html = ""
    if prob.get("steps"):
        for step in prob["steps"]:
            step_name = step.get("step") or step.get("stepName") or "Step"
            math_block = f'<div class="step-math">{step["math"]}</div>' if step.get("math") else ""
            explanation = step.get("explanation") or ""
            steps_html += f"""      <div class="solution-step">
        <div class="step-title">{step_name}</div>
        {math_block}
        <div class="step-explanation"><p>{explanation}</p></div>
      </div>
"""
    elif prob.get("solution"):
        steps_html = f"""      <div class="solution-step">
        <div class="step-explanation">{prob['solution']}</div>
      </div>
"""
    if prob.get("answer"):
        steps_html += f"""      <div class="solution-step" style="border-left-color: #10b981;">
        <div class="step-title" style="color: #10b981;">Final Answer & Physical Insight</div>
        <div class="step-explanation"><p><strong>{prob['answer']}</strong></p></div>
      </div>
"""

    statement = prob.get("statement") or prob.get("question") or ""
    prob_html += f"""<div class="problem-card" id="nuc-prob-{p_num.replace('.', '-')}">
  <div class="problem-header">
    <div class="prob-badge">SOLVED PROBLEM {p_num}</div>
    <h4 class="prob-title">{prob['title']}</h4>
  </div>
  <div class="problem-statement">
    <p>{statement}</p>
  </div>
  <div class="solution-container">
    <div class="solution-header">
      <span class="sol-tag">RIGOROUS DERIVATION & EXAM SOLUTION</span>
    </div>
    <div class="solution-steps">
{steps_html}    </div>
  </div>
</div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Nuclear Physics: Nuclear Structure, Radioactivity, Reactions & Particle Physics | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering nuclear constitution, charge radii, mass defect, binding energy systematics, semi-empirical mass formula (SEMF), liquid drop and shell models with spin-orbit coupling, radioactive decay kinetics, Bateman equations, alpha, beta, and gamma decay mechanisms, Fermi theory, nuclear reactions, fission, thermonuclear fusion, radiation interaction with matter, detection systems (HPGe, GM, NaI:Tl), particle accelerators, and the Standard Model with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Nuclear Physics Textbook, Semi-Empirical Mass Formula, Liquid Drop Model, Nuclear Shell Model, Magic Numbers, Spin-Orbit Coupling, Quadrupole Moment, Gamow Tunneling, Geiger-Nuttall Law, Beta Decay Fermi Theory, Kurie Plot, Neutrino, Gamma Transitions, Weisskopf Estimates, Internal Conversion, Nuclear Fission, Four-Factor Formula, Thermonuclear Fusion, Lawson Criterion, Bethe-Bloch Formula, Bragg Peak, Geiger-Muller Counter, HPGe Detector, Cyclotron, Synchrotron, Standard Model, Quarks, CKM Matrix, Higgs Boson">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/nuclear-physics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Nuclear Physics | OpenSTEM Digital Textbook">
  <meta property="og:description" content="University-standard course with 6 exhaustive chapters, complete mathematical derivations, 18 solved university exam problems, and 16 real-time interactive nuclear physics simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Nuclear Physics: Nuclear Structure, Radioactivity, Reactions & Particle Physics",
    "description": "Comprehensive university curriculum covering nuclear structure, radioactive decay kinetics, alpha/beta/gamma decay, nuclear reactions, fission, fusion, radiation detection, accelerators, and particle physics.",
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
  <link rel="stylesheet" href="styles.css?v=20261004_v13">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Nuclear Physics</div>
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

    <!-- Main Content Reader Container -->
    <main class="main-content">
      <!-- Top Sticky Navbar -->
      <header class="top-navbar">
        <div class="course-badge-container">
          <span class="badge-pill badge-course">Physics / Nuclear & Particle</span>
          <span class="badge-pill badge-credits">Nuclear Physics I</span>
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
            <h1 class="unit-title-heading" id="unit-title">{u1['title']}</h1>
            <p class="unit-desc-lead" id="unit-desc">
              {u1['description']}
            </p>
          </header>

          <!-- Textbook Sections Container -->
          <div id="textbook-sections">
{sec_html}
          </div>

          <!-- Solved University Exam Problems Section -->
          <section class="solved-problems-section" id="solved-problems-section">
            <div class="solved-section-header">
              <div class="solved-badge">EXAM SUCCESS WORKSHOP</div>
              <h3 class="solved-title">Solved University Examination Problems</h3>
              <p class="solved-desc">Step-by-step mathematical solutions to classic university honors examination questions.</p>
            </div>
            <div class="problem-cards-list" id="problem-cards-list">
{prob_html}
            </div>
          </section>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="nuclear-sims.js?v=20261004_v13"></script>
  <script src="nuclear-data.js?v=20261004_v13"></script>
  <script src="app.js?v=20261004_v13"></script>
</body>
</html>
"""

with open("nuclear-physics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("nuclear-physics.html successfully created!")
