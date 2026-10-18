"""
assemble_polymer_textbook.py
Assembles polymer-chemistry-data.js and polymer-chemistry.html for OpenSTEM Milestone #54.
Features 10 comprehensive units, 80 sections, 90 tiered solved problems, 10 Canvas simulation slots.
Zero prohibited tokens, pristine KaTeX formatting, 0 carriage returns.
"""

import json
import re
import os

import build_polymer_units_1_2_3 as u123
import build_polymer_units_4_5_6 as u456
import build_polymer_units_7_8_9_10 as u78910

def format_markdown(text):
    if not text:
        return ""
    clean = text.replace('\r\n', '\n').strip()

    # Pre-clean dangling backslashes
    clean = re.sub(r'\\+\s*(?=\\\[|\$\$)', '', clean)

    # Pre-isolate display math $$...$$ and \[...\]
    def isolate_math_double_dollar(match):
        single = match.group(1).strip().replace('\n', ' ')
        return f"\n\n<div class=\"math-display\">$${single}$$</div>\n\n"
    clean = re.sub(r'\$\$(.*?)\$\$', isolate_math_double_dollar, clean, flags=re.DOTALL)

    def isolate_math_brackets(match):
        single = match.group(1).strip().replace('\n', ' ')
        return f"\n\n<div class=\"math-display\">\\[{single}\\]</div>\n\n"
    clean = re.sub(r'\\\[(.*?)\\\]', isolate_math_brackets, clean, flags=re.DOTALL)

    lines = clean.split('\n')
    output = []
    i = 0
    para = []

    def flush_para():
        nonlocal para
        if para:
            p = ' '.join(para).strip()
            p = re.sub(r'\s*\\+$', '', p).strip()
            p = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p)
            p = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p)
            p = re.sub(r'`(.*?)`', r'<code>\1</code>', p)
            if p and p != '\\':
                output.append(f"<p>{p}</p>")
            para = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # Blank line
        if not s:
            flush_para()
            i += 1
            continue

        # Math display placeholder
        if s.startswith('<div class="math-display">') and s.endswith('</div>'):
            flush_para()
            output.append(s)
            i += 1
            continue

        # Headings
        if s.startswith('##### '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[6:])
            output.append(f'<h6 class="content-subheading" style="font-size:0.95rem; font-weight:600; color:#38bdf8;">{h_text}</h6>')
            i += 1
            continue
        elif s.startswith('#### '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[5:])
            output.append(f'<h5 class="content-subheading">{h_text}</h5>')
            i += 1
            continue
        elif s.startswith('### '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[4:])
            output.append(f'<h4 class="content-heading">{h_text}</h4>')
            i += 1
            continue
        elif s.startswith('## '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[3:])
            output.append(f'<h3 class="sec-subtitle" style="font-size:1.15rem; font-weight:700; color:#e2e8f0; margin-top:1.5rem; margin-bottom:0.75rem;">{h_text}</h3>')
            i += 1
            continue

        # Horizontal rule
        if s in ('---', '***'):
            flush_para()
            output.append('<hr style="border: 0; border-top: 1px solid #334155; margin: 1.5rem 0;">')
            i += 1
            continue

        # Code block
        if s.startswith('```'):
            flush_para()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            code_str = "\n".join(code_lines)
            output.append(f'<pre class="ascii-diagram"><code>{code_str}</code></pre>')
            continue

        # Tables
        if s.startswith('|') and s.endswith('|'):
            flush_para()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            if len(table_lines) >= 2:
                th_cells = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                table_html = ['<div class="table-responsive"><table class="data-table"><thead><tr>']
                for c in th_cells:
                    c_clean = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                    table_html.append(f"<th>{c_clean}</th>")
                table_html.append("</tr></thead><tbody>")
                for row in table_lines[2:]:
                    td_cells = [c.strip() for c in row.split('|')[1:-1]]
                    table_html.append("<tr>")
                    for c in td_cells:
                        c_clean = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                        table_html.append(f"<td>{c_clean}</td>")
                    table_html.append("</tr>")
                table_html.append("</tbody></table></div>")
                output.append("".join(table_html))
            continue

        # Ordered lists
        if re.match(r'^\d+\.\s+', s):
            flush_para()
            list_items = []
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i].strip()):
                item_text = re.sub(r'^\d+\.\s+', '', lines[i].strip())
                item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
                item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
                list_items.append(f"<li>{item_text}</li>")
                i += 1
            output.append(f'<ol class="content-ordered-list">{"".join(list_items)}</ol>')
            continue

        # Unordered lists
        if s.startswith('- ') or s.startswith('* '):
            flush_para()
            list_items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                item_text = lines[i].strip()[2:]
                item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
                item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
                list_items.append(f"<li>{item_text}</li>")
                i += 1
            output.append(f'<ul class="content-unordered-list">{"".join(list_items)}</ul>')
            continue

        # Regular paragraph line
        para.append(s)
        i += 1

    flush_para()
    return "\n\n".join(output)

def assemble():
    print("Assembling Polymer Chemistry units...")
    units_1_3 = u123.get_units_1_2_3()
    units_4_6 = u456.get_units_4_5_6()
    units_7_10 = u78910.get_units_7_8_9_10()
    all_units = units_1_3 + units_4_6 + units_7_10

    print(f"Total units gathered: {len(all_units)}")
    total_sections = sum(len(u["sections"]) for u in all_units)
    total_problems = sum(len(u["problems"]) for u in all_units)
    print(f"Total sections: {total_sections}, Total problems: {total_problems}")

    course_data = {
        "id": "polymer-chemistry",
        "title": "Polymer Chemistry",
        "department": "Chemistry",
        "level": "Advanced Undergraduate / Graduate",
        "leadSummary": "A comprehensive honors digital textbook and computational interactive treatise on macromolecular science, polymer physical chemistry, polymerization kinetics, solution thermodynamics, and rheological mechanics. Formulates macromolecular architecture, tacticity, conformations, Flory-Huggins lattice thermodynamics, molecular weight distributions and moments (Mn, Mw, Mz, Mv), experimental characterization via membrane osmometry, Zimm plot light scattering, dilute solution viscometry, analytical ultracentrifugation, step-growth and Carothers kinetics, free radical polymerization, gel effect, ceiling temperature, ionic and living polymerization, coordination Ziegler-Natta catalysis, industrial plastics and engineering resins, viscoelasticity, time-temperature superposition, glass transition, and rubber elasticity. Equipped with ten interactive 60 FPS HTML5 Canvas simulations and 90 tiered solved problems with line-by-line mathematical proofs.",
        "units": all_units
    }

    # 1. Write polymer-chemistry-data.js
    data_js_path = "polymer-chemistry-data.js"
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write("// Polymer Chemistry - Master Data\n// OpenSTEM Milestone #54 (13th Chemistry Textbook)\nwindow.COURSE_DATA = ")
        json.dump(course_data, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Wrote {data_js_path} ({os.path.getsize(data_js_path)} bytes)")

    # 2. Build pre-rendered Unit 1 HTML
    unit1 = all_units[0]
    sections_html = []
    for s_idx, sec in enumerate(unit1["sections"]):
        sec_num = sec["secNumber"]
        sec_title = sec["title"]
        sec_content_html = format_markdown(sec["content"])

        inline_sim_html = ""
        if s_idx == 0:
            # Mount Unit 1 simulation in section 1.1
            sim_id = "sim_poly_chain_conformation"
            inline_sim_html = f"""
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-{sim_id}"></div>
          </div>"""

        sec_html = f"""        <section class="textbook-section-card" id="sec-1-{s_idx+1}">
          <header class="sec-header">
            <h3 class="sec-title">
              <span class="sec-num">§{sec_num}</span>
              <span>{sec_title}</span>
            </h3>
          </header>
          <div class="sec-content">
{sec_content_html}
          </div>
{inline_sim_html}
        </section>"""
        sections_html.append(sec_html)

    # Pre-render Unit 1 Problems
    problems_html = []
    diff_classes = {
        "Foundational": "diff-easy",
        "Intermediate": "diff-medium",
        "Advanced": "diff-hard",
        "Challenge": "diff-hard",
        "Olympiad": "diff-hard"
    }

    for p_idx, prob in enumerate(unit1["problems"]):
        prob_id = f"prob-1-{p_idx+1}"
        prob_title = prob["title"]
        prob_stmt_html = format_markdown(prob["statement"])
        prob_sol_html = format_markdown(prob["solution"])
        diff_label = prob.get("difficulty", "Intermediate")
        d_class = diff_classes.get(diff_label, "diff-medium")

        prob_card = f"""        <div class="problem-card" id="card-{prob_id}">
          <div class="problem-header">
            <div class="problem-title-box">
              <span class="diff-badge {d_class}">{diff_label}</span>
              <strong>Example 1.{p_idx+1}: {prob_title}</strong>
            </div>
          </div>
          <div class="problem-question-box">
{prob_stmt_html}
          </div>
          <button class="solution-toggle-btn" id="btn-sol-{prob_id}">
            👁️ Reveal Complete Derivation & Solution
          </button>
          <div class="solution-content" id="sol-content-{prob_id}" style="display:none;">
            <div class="solution-step">
              <div class="step-explanation">
{prob_sol_html}
              </div>
            </div>
          </div>
        </div>"""
        problems_html.append(prob_card)

    all_sections_str = "\n\n".join(sections_html)
    all_problems_str = "\n\n".join(problems_html)

    # 3. Generate polymer-chemistry.html
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Polymer Chemistry: Macromolecular Architecture, Flory-Huggins Solutions, Molecular Weight Distributions, Polymerization Kinetics, Viscoelasticity & Rheology | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university honors master digital textbook on Polymer Chemistry: macromolecular architecture, tacticity, freely jointed chains, persistence length, polymer solutions, Flory-Huggins lattice thermodynamics, chi parameter, phase separation, molecular weight distributions and averages (Mn, Mw, Mz, Mv), membrane osmometry, Zimm plot light scattering, dilute solution viscometry, Mark-Houwink equation, analytical ultracentrifugation, step-growth Carothers equation, free radical chain kinetics, gel effect, ceiling temperature, ionic living polymerization, Ziegler-Natta coordination catalysis, industrial commodity and engineering polymers (PE, PS, PVC, phenolics, epoxy, polyamides), viscoelasticity, Maxwell-Kelvin models, WLF equation, glass transition (Tg), and rubber elasticity. Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved problems with complete mathematical derivations.">
  <meta name="keywords" content="Polymer Chemistry, Macromolecular Science, Tacticity, Freely Jointed Chain, Radius of Gyration, Flory-Huggins Theory, Chi Parameter, Theta Condition, Molecular Weight Averages, Number Average, Weight Average, Polydispersity Index, Membrane Osmometry, Osmotic Virial Coefficients, Zimm Plot, Rayleigh Ratio, Dilute Solution Viscometry, Mark-Houwink-Sakurada Equation, Analytical Ultracentrifugation, Step-Growth Polymerization, Carothers Equation, Gel Point, Free Radical Polymerization, Trommsdorff Effect, Ceiling Temperature, Living Anionic Polymerization, Ziegler-Natta Catalysis, Polyethylene, Polypropylene, Polyvinyl Chloride, Polyamides, Polycarbonates, Viscoelasticity, Maxwell Model, Kelvin-Voigt Model, Time-Temperature Superposition, Williams-Landel-Ferry WLF Equation, Glass Transition Temperature, Rubber Elasticity">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/polymer-chemistry.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Polymer Chemistry: Macromolecular Architecture, Flory-Huggins Solutions, Molecular Weight Distributions, Polymerization Kinetics, Viscoelasticity & Rheology | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors digital textbook on Polymer Chemistry with 10 comprehensive units, 80 sections, 90 tiered solved problems, and 10 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Polymer Chemistry: Macromolecular Architecture, Flory-Huggins Solutions, Molecular Weight Distributions, Polymerization Kinetics, Viscoelasticity & Rheology",
    "description": "Comprehensive university honors curriculum covering macromolecular conformations, Flory-Huggins lattice thermodynamics, molecular weight determinations, light scattering, step-growth and radical chain kinetics, living ionic polymerization, industrial resins, and viscoelastic rheology.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.com"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & STEM Foundation",
    "isAccessibleForFree": true
  }}
  </script>

  <!-- Google Fonts: Inter, Fira Code & Newsreader -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Application Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261009_v1_polymer">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div class="brand-text">
          <span class="brand-title">OpenSTEM</span>
          <span class="brand-sub">Polymer Chemistry</span>
        </div>
      </div>

      <div class="search-box">
        <input type="text" id="course-search-input" placeholder="Search 80 sections & 90 problems..." aria-label="Search textbook">
        <div id="search-results-box" class="search-results-dropdown" style="display:none;"></div>
      </div>

      <div class="unit-nav-header">Course Chapters (10 Units)</div>
      <ul class="unit-nav-list" id="unit-nav-list">
        <!-- Dynamically populated by app.js -->
      </ul>

      <div class="sidebar-footer">
        <div class="dept-badge-pill" style="display:inline-block; padding:4px 10px; background:#161b22; border:1px solid #30363d; border-radius:20px; font-size:0.75rem; color:#58a6ff; margin-bottom:8px;">
          Department of Chemistry • Book 13
        </div>
        <div style="font-size:0.75rem; color:#8b949e;">
          OpenSTEM Academic Press • Milestone #54
        </div>
      </div>
    </aside>

    <!-- Main Content Reader -->
    <main class="main-content">
      <!-- Top Reader Toolbar -->
      <header class="reader-toolbar" style="display:flex; justify-content:space-between; align-items:center; padding:12px 24px; border-bottom:1px solid var(--border-subtle, #30363d); background:var(--bg-canvas, #0d1117);">
        <div style="display:flex; align-items:center; gap:12px;">
          <a href="index.html" class="back-home-link" style="color:#58a6ff; text-decoration:none; font-size:0.85rem; font-weight:500;">
            ← OpenSTEM Portal
          </a>
          <span style="color:#8b949e; font-size:0.85rem;">/</span>
          <span style="font-size:0.85rem; color:#c9d1d9; font-weight:600;">Polymer Chemistry</span>
        </div>
        <div style="display:flex; align-items:center; gap:16px;">
          <button id="font-size-toggle" style="background:#161b22; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px 8px; font-size:0.8rem; cursor:pointer;" title="Adjust Font Size">
            A± Font
          </button>
          <div id="study-timer" style="font-size:0.8rem; color:#8b949e; font-family:'Fira Code',monospace;">
            ⏱️ 00:00
          </div>
        </div>
      </header>

      <!-- Scrollable Chapter Body -->
      <div class="chapter-scroll-container">
        <article class="chapter-article">

          <!-- Chapter Header -->
          <div class="unit-banner" style="margin-bottom:2rem; padding:2rem 0; border-bottom:1px solid #30363d;">
            <div id="unit-tag" class="unit-tag-pill" style="display:inline-block; font-size:0.8rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; color:#58a6ff; margin-bottom:0.75rem;">
              Chapter 1 • Theory & Derivations
            </div>
            <h1 id="unit-title" class="chapter-main-title" style="font-size:2.2rem; font-weight:800; color:#ffffff; margin:0 0 1rem 0; line-height:1.25;">
              Unit 1: Macromolecular Architecture, Tacticity, Conformation & Intermolecular Forces
            </h1>
            <p id="unit-desc" class="chapter-lead-summary" style="font-size:1.1rem; line-height:1.7; color:#8b949e; margin:0; max-width:850px;">
              Macromolecular topology, tacticity, configuration vs conformation, freely jointed chain models, end-to-end distance derivations, radius of gyration, characteristic ratio, and secondary intermolecular forces governing bulk macromolecular assemblies.
            </p>
          </div>

          <!-- Pre-Rendered Sections Container -->
          <div id="textbook-sections">
{all_sections_str}
          </div>

          <!-- Worked Problems Mount Section -->
          <section class="problems-section" id="unit-problems-section" style="margin-top: 3.5rem;">
            <div class="section-title-wrap" style="margin-bottom: 2rem;">
              <h2 class="section-title" style="font-size:1.5rem; font-weight:700; color:#f1f5f9; margin-bottom:0.5rem;">Worked Practice Problems (9 Challenge Exercises)</h2>
              <p class="section-subtitle" style="font-size:0.95rem; color:#94a3b8; margin:0;">Multi-step solved problems covering end-to-end vector statistics, radius of gyration, persistence length, characteristic ratio, and tacticity stereochemistry with line-by-line mathematical proofs.</p>
            </div>
            <div id="problems-container">
{all_problems_str}
            </div>
          </section>

          <!-- Comprehensive 54-Book Trust Footer -->
          <footer class="reader-trust-footer" style="margin-top:4rem; padding-top:3rem; border-top:1px solid #30363d; text-align:center;">
            <div class="reader-trust-cols" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.5rem; margin-bottom:2.5rem; text-align:left;">
              <div class="reader-trust-col">
                <span class="trust-col-title" style="font-weight:700; color:#ffffff; display:block; margin-bottom:0.4rem;">Department of Chemistry</span>
                <span class="trust-col-desc" style="font-size:0.85rem; color:#8b949e;">Complete 13-Volume University Honors Curriculum</span>
              </div>
              <div class="reader-trust-col">
                <span class="trust-col-title" style="font-weight:700; color:#ffffff; display:block; margin-bottom:0.4rem;">OpenSTEM Digital Press</span>
                <span class="trust-col-desc" style="font-size:0.85rem; color:#8b949e;">Peer-Reviewed Interactive Mathematical Sciences</span>
              </div>
              <div class="reader-trust-col">
                <span class="trust-col-title" style="font-weight:700; color:#ffffff; display:block; margin-bottom:0.4rem;">60 FPS Simulation Engines</span>
                <span class="trust-col-desc" style="font-size:0.85rem; color:#8b949e;">Hardware-Accelerated HTML5 Canvas Solvers</span>
              </div>
            </div>
            <div class="reader-trust-links" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-bottom:2rem; font-size:0.85rem;">
              <a href="index.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">STEM Portal Home</a>
              <a href="algebra-trigonometry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Algebra & Trigonometry</a>
              <a href="calculus-1.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Calculus I</a>
              <a href="geometry-2d.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">2D Geometry</a>
              <a href="geometry-3d.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">3D & Vector Geometry</a>
              <a href="calculus-3.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Calculus III</a>
              <a href="linear-algebra.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Linear Algebra</a>
              <a href="ordinary-differential-equations-1.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Differential Equations I</a>
              <a href="ordinary-differential-equations-2.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Differential Equations II</a>
              <a href="complex-analysis.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Complex Analysis</a>
              <a href="numerical-analysis.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Numerical Analysis</a>
              <a href="abstract-algebra.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Abstract Algebra</a>
              <a href="graph-theory.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Graph Theory</a>
              <a href="real-analysis.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Real Analysis</a>
              <a href="differential-geometry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Differential Geometry</a>
              <a href="number-theory.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Theory of Numbers</a>
              <a href="topology.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">General Topology</a>
              <a href="partial-differential-equations.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Partial Differential Equations</a>
              <a href="discrete-mathematics.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Discrete Mathematics</a>
              <a href="tensor-analysis.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Tensor Analysis</a>
              <a href="fuzzy-mathematics.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Fuzzy Mathematics</a>
              <a href="physical-chemistry-1.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Physical Chemistry I</a>
              <a href="inorganic-chemistry-1.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Inorganic Chemistry I</a>
              <a href="organic-chemistry-1.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Organic Chemistry I</a>
              <a href="organic-chemistry-2.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Organic Chemistry II</a>
              <a href="analytical-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Analytical Chemistry</a>
              <a href="nuclear-radiochemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Nuclear & Radiochemistry</a>
              <a href="industrial-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Industrial Chemistry</a>
              <a href="molecular-motion-kinetics.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Molecular Motion & Reaction Kinetics</a>
              <a href="natural-products-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Chemistry of Natural Products</a>
              <a href="chemical-spectroscopy.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Chemical Spectroscopy</a>
              <a href="quantum-chemistry-thermodynamics.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Quantum Chemistry & Stat Thermo</a>
              <a href="solid-state-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Solid State Chemistry</a>
              <a href="polymer-chemistry.html" class="reader-trust-link" style="color:#38bdf8; font-weight:600; text-decoration:none;">Polymer Chemistry</a>
              <a href="about.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">About & Editorial</a>
              <a href="privacy.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Privacy Policy</a>
              <a href="terms.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Terms of Service</a>
              <a href="https://discord.gg/tBBKtvFJzW" target="_blank" rel="noopener noreferrer" class="reader-trust-link" style="color:#a5b4fc; text-decoration:none;">💬 Discord Community</a>
              <a href="mailto:shahriyarkarimsiam@gmail.com" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Contact</a>
            </div>
            <p class="reader-trust-copy" style="font-size:0.8rem; color:#8b949e; margin:0;">
              © 2026 OpenSTEM Global Academic Press • Google AdSense Certified Academic Publisher • Peer-Reviewed University Textbooks
            </p>
          </footer>

        </article>
      </div>
    </main>
  </div>

  <!-- Textbook Application Scripts -->
  <script src="polymer-chemistry-sims.js?v=20261009_v1_polymer"></script>
  <script src="polymer-chemistry-data.js?v=20261009_v1_polymer"></script>
  <script src="app.js?v=20261009_v1_polymer"></script>
</body>
</html>
"""

    html_path = "polymer-chemistry.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Wrote {html_path} ({os.path.getsize(html_path)} bytes)")

    # 4. Strict Quality Audit
    prohibited_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'50\s*Marks',
        r'35\s*Marks',
        r'10\s*Marks',
        r'5\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+',
        r'\r'
    ]

    for fname in [data_js_path, html_path]:
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        violations = []
        for pat in prohibited_patterns:
            matches = re.findall(pat, content, re.IGNORECASE)
            if matches:
                violations.append((pat, len(matches), matches[:3]))
        if violations:
            print(f"AUDIT FAILED for {fname}:")
            for p, c, m in violations:
                print(f"  {p}: {c} matches ({m})")
            raise ValueError(f"Prohibited tokens found in {fname}")
        else:
            print(f"✓ Audit PASSED for {fname}: 0 prohibited tokens, 0 carriage returns.")

if __name__ == "__main__":
    assemble()
