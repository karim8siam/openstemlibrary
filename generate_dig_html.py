import json

with open("dig_u1.json", "r", encoding="utf-8") as f:
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
    prob_html += f"""<div class="problem-card" id="dig-prob-{p_num.replace('.', '-')}">
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
  <title>Digital Electronics: Combinational & Sequential Systems, Data Converters, Memory & VLSI Fabrication | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering number systems, weighted codes, Hamming error correction, Boolean algebra, logic gates, semiconductor logic families (TTL, CMOS), Karnaugh map minimization, Quine-McCluskey tabulation, arithmetic circuits, latches, flip-flops, 555 timer multivibrators, synchronous and ripple counters, shift registers, MSI logic, DAC and ADC data conversion systems, semiconductor memory architectures (SRAM, DRAM, ROM, Flash), and silicon integrated circuit VLSI microfabrication with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Digital Electronics Textbook, Number Systems, Gray Code, Hamming Code SEC-DED, Boolean Algebra, De Morgan Laws, Logic Gates, Universal NAND NOR, TTL Totem-Pole, CMOS Inverter, Karnaugh Map K-Map, Quine-McCluskey, 1s 2s Complement, Full Adder, Carry Lookahead Adder, BCD Adder, SR Latch, D Flip-Flop, JK Flip-Flop, Race-Around Condition, 555 Timer, Multivibrators, Ripple Counter, Synchronous Counter, Shift Register, Johnson Counter, Decoders, Multiplexers, R-2R Ladder DAC, Flash ADC, SAR ADC, Dual-Slope ADC, SRAM 6T, DRAM 1T-1C, Flash Memory, Czochralski Silicon, Deal-Grove Oxidation, Photolithography, Ion Implantation, CMOS Fabrication">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/digital-electronics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Digital Electronics | OpenSTEM Digital Textbook">
  <meta property="og:description" content="University-standard course with 8 exhaustive chapters, complete mathematical derivations, 24 solved university exam problems, and 16 real-time interactive digital electronics simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Digital Electronics: Combinational & Sequential Systems, Data Converters, Memory & VLSI Fabrication",
    "description": "Comprehensive university curriculum covering number systems, Boolean algebra, logic families, combinational logic design, sequential circuits, data converters, semiconductor memory, and integrated circuit microfabrication.",
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
  <link rel="stylesheet" href="styles.css?v=20261005_v14">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Digital Electronics</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search topics, gates, equations..." class="search-input">
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
          <span class="badge-pill badge-course">Physics / Electronics & Microelectronics</span>
          <span class="badge-pill badge-credits">Digital Electronics I</span>
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
  <script src="digital-electronics-sims.js?v=20261005_v14"></script>
  <script src="digital-electronics-data.js?v=20261005_v14"></script>
  <script src="app.js?v=20261005_v14"></script>
</body>
</html>
"""

with open("digital-electronics.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("digital-electronics.html successfully created!")
