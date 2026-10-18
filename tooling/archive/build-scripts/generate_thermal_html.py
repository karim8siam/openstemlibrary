# Generator for thermal-physics.html with pre-rendered static content matching the clean standard
import json

with open("tp_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

def format_content(text):
    paragraphs = text.split("\n\n")
    formatted = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith("### "):
            formatted.append(f"<h4>{p[4:]}</h4>")
        elif p.startswith("#### "):
            formatted.append(f"<h5>{p[5:]}</h5>")
        if p.startswith("<h") or p.startswith("<ul>") or p.startswith("<ol>") or p.startswith("<blockquote>") or p.startswith("$$") or p.startswith("<div") or p.startswith("<p"):
            formatted.append(p)
        else:
            formatted.append(f"<p>{p}</p>")
    return "\n".join(formatted)

# Pre-render sections for Unit 1
sections_html = ""
for idx, sec in enumerate(u1["sections"], 1):
    sim_html = ""
    if sec.get("simulation"):
        sim_html = f'''
  <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
    <div class="simulation-slot" id="sim-container-{sec["simulation"]}"></div>
  </div>'''

    sec_title = sec.get("title") or sec.get("heading")
    sections_html += f'''
<section class="textbook-section-card" id="{sec["id"]}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">1.{idx}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{format_content(sec["content"])}
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
    diff_label = prob.get("difficultyLabel") or prob.get("difficulty") or "Standard"
    diff_class = "diff-medium"

    problems_html += f'''
<div class="problem-card">
  <div class="problem-header">
    <div class="problem-title-box"><span class="diff-badge {diff_class}">{diff_label}</span><strong>Example 1.{idx}: {prob["title"]}</strong></div>
  </div>
  <div class="problem-question-box">{prob_question}</div>
  <button class="solution-toggle-btn" id="btn-sol-{prob_id}">👁️ Reveal Complete Derivation & Solution</button>
  <div class="solution-content" id="sol-content-{prob_id}">
{steps_html}
  </div>
</div>'''

lead_desc = u1.get("leadSummary") or u1.get("description") or ""

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Comprehensive Worldwide SEO Meta Tags -->
  <title>Thermal Physics: Classical Thermodynamics, Entropy & Kinetic Theory | Interactive Digital Textbook</title>
  <meta name="description" content="University-standard interactive textbook on Thermal Physics covering Zeroth and First Laws, Second Law and Carnot Engines, Entropy, Thermodynamic Potentials U, H, F, G, Maxwell Relations, Heat Conduction, Thermal Radiation, and Kinetic Transport Phenomena.">
  <meta name="keywords" content="Thermal Physics Textbook, Thermodynamics, Zeroth Law, First Law of Thermodynamics, Second Law, Carnot Engine, Entropy, Third Law, Thermodynamic Potentials, Maxwell Relations, Clausius Clapeyron, Heat Conduction Fourier, Blackbody Radiation Planck, Mean Free Path, Van der Waals Gas, Brownian Motion, Joule Thomson Effect">
  <meta name="author" content="OpenSTEM Global Academic Press">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="https://openstemlibrary.org/physics/thermal-physics">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Thermal Physics: Interactive Digital Textbook & Simulations">
  <meta property="og:description" content="Complete university courseware covering thermodynamics, statistical entropy, heat conduction, radiation laws, and transport phenomena with 60 FPS simulations and solved exam problems.">
  <meta property="og:site_name" content="OpenSTEM Global Academic Repository">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">
  <meta name="twitter:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <link rel="apple-touch-icon" href="logo.svg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Thermal Physics: Interactive Digital Textbook">
  <meta name="twitter:description" content="University textbook on Thermal Physics with 60 FPS interactive simulations and solved university exam problems.">

  <!-- Structured Data JSON-LD for Google Academic Knowledge Graph -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Thermal Physics: University Standard Courseware",
    "description": "Comprehensive digital textbook covering thermodynamics, Carnot cycles, entropy, Maxwell thermodynamic relations, heat conduction, radiation, and kinetic transport phenomena.",
    "educationalLevel": "Undergraduate Physics B.Sc. Honors & Mechanical Engineering",
    "inLanguage": "en",
    "author": {{
      "@type": "Organization",
      "name": "OpenSTEM Global Academic Press",
      "email": "shahriyarkarimsiam@gmail.com"
    }}
  }}
  </script>

  <!-- Google Fonts: Inter & Fira Code & Newsreader -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Application Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261004_v8">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Thermal Physics</div>
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
          <span class="badge-pill badge-credits">Thermal Physics</span>
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
            <h1 class="unit-title-heading" id="unit-title">{u1["title"]}</h1>
            <p class="unit-desc-lead" id="unit-desc">
              {lead_desc}
            </p>
          </header>

          <!-- Textbook Sections Container (Pre-rendered for Googlebot & SEO Crawlers) -->
          <div id="textbook-sections">
{sections_html}
          </div>

          <!-- Solved Problem Sets Section -->
          <section class="problems-section-container" id="problems-section-wrap">
            <header class="problems-header">
              <div class="problems-badge">Standard University Exam Examination Problems</div>
              <h3 class="problems-main-title">Rigorous Analytical & Numerical Solved Problems</h3>
              <p class="problems-sub">Comprehensive step-by-step mathematical proofs, dimensional evaluations, and calculations matching B.Sc. Honors university examinations.</p>
            </header>
            <div class="problems-list" id="problems-mount">
{problems_html}
            </div>
          </section>

          <!-- Textbook Reader Trust & Compliance Footer -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">← All Departments</a>
              <a href="reader.html" class="reader-trust-link">Quantum Mechanics</a>
              <a href="mechanics.html" class="reader-trust-link">Fundamentals of Mechanics</a>
              <a href="electrodynamics.html" class="reader-trust-link">Electrodynamics</a>
              <a href="optics.html" class="reader-trust-link">Wave & Modern Optics</a>
              <a href="statistical-mechanics.html" class="reader-trust-link">Statistical Mechanics</a>
              <a href="properties-of-matter.html" class="reader-trust-link">Properties of Matter & Waves</a>
              <a href="electricity-magnetism.html" class="reader-trust-link">Electricity & Magnetism</a>
              <a href="thermal-physics.html" class="reader-trust-link active-trust-link">Thermal Physics</a>
              <a href="about.html" class="reader-trust-link">About & Editorial</a>
              <a href="privacy.html" class="reader-trust-link">Privacy Policy</a>
              <a href="terms.html" class="reader-trust-link">Terms of Service</a>
              <a href="mailto:shahriyarkarimsiam@gmail.com" class="reader-trust-link">Contact (shahriyarkarimsiam@gmail.com)</a>
            </div>
            <p class="reader-trust-copy">© 2026 OpenSTEM Global Academic Press • Google AdSense Certified Academic Publisher</p>
          </footer>
        </article>
      </div>
    </main>
  </div>

  <!-- Scripts -->
  <script src="thermal-physics-data.js?v=20261004_v8"></script>
  <script src="thermal-physics-sims.js?v=20261004_v8"></script>
  <script src="app.js?v=20261004_v8"></script>
</body>
</html>
'''

with open("thermal-physics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully regenerated thermal-physics.html with 100% clean pre-rendered content and ZERO mock ads!")
