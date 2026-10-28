import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793227366220_3b180201.zip'

batch1_slugs = [
    'engineering-mechanics',
    'mechanics-of-solids',
    'engineering-thermodynamics',
    'fluid-mechanics',
    'manufacturing-processes'
]

def clean_html(raw_html):
    main_m = re.search(r'<main[^>]*>([\s\S]*?)</main>', raw_html)
    content = main_m.group(1) if main_m else raw_html
    # Remove script tags
    content = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', content)
    # Remove navline and back links
    content = re.sub(r'<div class=[\"\']navline[\"\']>[\s\S]*?</div>', '', content)
    content = re.sub(r'<a[^>]*href=[\"\']\.\./[^\"\']*[\"\'][^>]*>[\s\S]*?</a>', '', content)
    # Change h1 to h3
    content = re.sub(r'<h1([^>]*)>', r'<h3\1>', content)
    content = re.sub(r'</h1>', r'</h3>', content)
    return content.strip()

def transform_script(raw_script):
    s = raw_script.strip()
    # Strip opening/closing IIFE if present
    s = re.sub(r'^\s*\(\s*\(\s*\)\s*=>\s*\{', '', s)
    s = re.sub(r'\}\s*\)\s*\(\s*\)\s*;\s*$', '', s)
    # Replace document calls with card calls
    s = re.sub(r'document\.getElementById\(([\'\"`][^\'\"]+[\'\"`])\)', r'card.querySelector("#" + \1.replace(/^#/, ""))', s)
    s = re.sub(r'document\.querySelector\(', r'card.querySelector(', s)
    s = re.sub(r'document\.querySelectorAll\(', r'card.querySelectorAll(', s)
    return s.strip()

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    for slug in batch1_slugs:
        print(f"Processing simulations for {slug}...")
        models = []
        for i in range(1, 17):
            name = f'OpenSTEM-Mechanical-Engineering/books/{slug}/simulations/model-{i:02d}.html'
            raw = z.read(name).decode('utf-8', errors='ignore')
            
            clean_h = clean_html(raw)
            script_m = re.search(r'<script[^>]*>([\s\S]*?)</script>', raw)
            script_body = script_m.group(1) if script_m else ""
            transformed_s = transform_script(script_body)
            
            unit_num = ((i - 1) // 2) + 1
            models.append({
                'idx': i,
                'unit': unit_num,
                'html': clean_h,
                'script': transformed_s
            })

        out_js = [
            f"/* {slug} Interactive Simulation Suite */",
            "(function(window) {",
            "  'use strict';",
            "",
            "  var MODELS = [];"
        ]

        for m in models:
            esc_html = json.dumps(m['html'])
            out_js.append(f"""
  MODELS.push({{
    idx: {m['idx']},
    unit: {m['unit']},
    html: {esc_html},
    init: function(card) {{
      try {{
{m['script']}
      }} catch (err) {{
        console.warn('Sim init error in model {m['idx']}:', err);
      }}
    }}
  }});""")

        out_js.append("""
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }

  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';

    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') {
        unitNum = parseInt(bMatch, 10) + 1;
      } else {
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
        if (pMatch) {
          unitNum = parseInt(pMatch[1], 10);
        }
      }
    }

    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;

    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'me-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  // Auto-init when DOM is ready if #sim-container is present
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) {
          window.SimulationEngine.initSimulation('sim-container');
        }
      });
    } else {
      if (document.getElementById('sim-container')) {
        window.SimulationEngine.initSimulation('sim-container');
      }
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
""")

        target_file = os.path.join(ROOT, 'src', 'subjects', 'mechanical-engineering', slug, f"{slug}-sims.js")
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(out_js))
        print(f"Generated {target_file} ({len(models)} models)")

print("Batch 1 simulations generated successfully.")
