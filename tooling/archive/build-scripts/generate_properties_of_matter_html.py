# Generator for properties-of-matter.html
import json
import html

with open("matter_u1.json") as f:
    u1 = json.load(f)

def format_content(text):
    # Convert double newlines to paragraphs or preserve HTML tags
    paragraphs = text.split("\n\n")
    formatted = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith("<h") or p.startswith("<ul>") or p.startswith("<ol>") or p.startswith("<blockquote>") or p.startswith("$$"):
            formatted.append(p)
        else:
            formatted.append(f"<p>{p}</p>")
    return "\n".join(formatted)

# Pre-render sections for Unit 1
sections_html = ""
for sec in u1["sections"]:
    sec_num = sec["number"].replace("§", "")
    sim_html = ""
    if sec.get("simulation"):
        sim_html = f'''
  <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
    <div class="simulation-slot" id="sim-container-{sec["simulation"]}"></div>
  </div>'''

    sections_html += f'''
<section class="textbook-section-card" id="{sec["id"]}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{sec["number"]}</span><span>{sec["heading"]}</span></h3>
  </header>
  <div class="sec-content">
{format_content(sec["content"])}
  </div>{sim_html}
</section>'''

# Pre-render problems for Unit 1
problems_html = ""
for prob in u1["problems"]:
    steps_html = ""
    for idx, s in enumerate(prob["steps"]):
        steps_html += f'''
<div class="solution-step">
  <div class="step-title">{s["title"]}</div>
  <div class="step-math">{s["math"]}</div>
  <div class="step-explanation"><p>{s["explanation"]}</p></div>
</div>'''

    diff_class = "diff-hard" if "Honors" in prob["difficulty"] else ("diff-medium" if "Standard" in prob["difficulty"] else "diff-easy")
    diff_label = "Advanced" if "Honors" in prob["difficulty"] else ("Standard" if "Standard" in prob["difficulty"] else "Core")

    problems_html += f'''
<div class="problem-card">
  <div class="problem-header">
    <div class="problem-title-box"><span class="diff-badge {diff_class}">{diff_label}</span><strong>{prob["title"]}</strong></div>
  </div>
  <div class="problem-question-box">{prob["question"]}</div>
  <button class="solution-toggle-btn" id="btn-sol-{prob["id"]}">👁️ Reveal Complete Derivation & Solution</button>
  <div class="solution-content" id="sol-content-{prob["id"]}">
{steps_html}
  </div>
</div>'''

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Comprehensive Worldwide SEO Meta Tags -->
  <title>Properties of Matter and Waves: Interactive Digital Textbook & Simulations</title>
  <meta name="description" content="University-standard textbook on Properties of Matter and Waves covering Gravitation, Elasticity, Hydrostatics, Surface Tension, Hydrodynamics, Viscosity, Oscillations, Traveling Waves, Stationary Waves, and Sound Waves.">
  <meta name="keywords" content="Properties of Matter and Waves, Gravitation Kepler, Elasticity Hooke Stress Strain, Hydrostatics Pascals Law, Surface Tension Jurin, Bernoulli Hydrodynamics Poiseuille, Simple Harmonic Motion Resonance, Traveling Waves Phase Group Velocity, Stationary Waves Melde, Doppler Effect Mach Cone">
  <meta name="author" content="OpenSTEM Global Academic Press">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="https://openstemlibrary.org/physics/properties-of-matter">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Properties of Matter and Waves: Interactive Digital Textbook">
  <meta property="og:description" content="Complete university textbook covering Gravitation, Elasticity, Fluids, Oscillations, and Wave Acoustics with real-time interactive simulations and solved exam problems.">
  <meta property="og:site_name" content="OpenSTEM Global Academic Repository">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">
  <meta name="twitter:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <link rel="apple-touch-icon" href="logo.svg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Properties of Matter and Waves: Interactive Digital Textbook">
  <meta name="twitter:description" content="University textbook on Properties of Matter and Waves with 60 FPS interactive simulations and solved exam problems.">

  <!-- Structured Data JSON-LD for Google Academic Knowledge Graph -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Properties of Matter and Waves: University Standard Courseware",
    "description": "Comprehensive textbook covering gravitation, elasticity, hydrostatics, surface tension, hydrodynamics, Poiseuille flow, harmonic oscillations, traveling waves, stationary modes, and sound acoustics.",
    "educationalLevel": "Undergraduate Physics B.Sc. Honors & Engineering",
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
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Properties of Matter</div>
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
          <span class="badge-pill badge-credits">Properties of Matter & Waves</span>
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
              {u1["leadSummary"]}
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
              <a href="properties-of-matter.html" class="reader-trust-link active-trust-link">Properties of Matter & Waves</a>
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
  <script src="matter-data.js?v=20261004_v2"></script>
  <script src="matter-sims.js?v=20261004_v2"></script>
  <script src="app.js?v=20261004_v2"></script>
</body>
</html>
'''

with open("properties-of-matter.html", "w") as f:
    f.write(html_content)

print("Successfully generated properties-of-matter.html with pre-rendered SEO content!")
