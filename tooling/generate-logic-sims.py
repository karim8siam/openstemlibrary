import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793141595693_55b360e9.zip'

slugs = [
    'formal-logic',
    'model-theory-and-mathematical-semantics',
    'proof-theory-and-deductive-systems',
    'set-theory-and-foundations',
    'symbolic-and-predicate-logic'
]

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    for slug in slugs:
        prefix = f"OpenSTEM-Logic-and-Systems-Science/books/{slug}/simulations/"
        html_files = sorted([n for n in z.namelist() if n.startswith(prefix) and re.search(r'-\d+\.html$', n)])
        
        # Read the simulation JS
        sim_js_name = [n for n in z.namelist() if n.startswith(prefix) and n.endswith('.js')][0]
        sim_js_code = z.read(sim_js_name).decode('utf-8')
        
        models = []
        for i, h in enumerate(html_files):
            raw = z.read(h).decode('utf-8')
            t_m = re.search(r'<h1>(.*?)</h1>', raw)
            title = t_m.group(1).strip() if t_m else f"Model {i+1}"
            
            p_m = re.search(r'<h1>.*?</h1>\s*<p>(.*?)</p>', raw)
            desc = p_m.group(1).strip() if p_m else "Interactive semantic model."
            
            type_m = re.search(r'data-type=\"(.*?)\"|data-kind=\"(.*?)\"', raw)
            m_type = (type_m.group(1) or type_m.group(2)) if type_m else ''
            
            # Extract controls HTML
            ctrl_m = re.search(r'<div id=\"controls\">(.*?)</div>\s*</div>|<div class=\"panel\" id=\"controls\">(.*?)</div>\s*<section|<div id=\"controls\" class=\"panel\">(.*?)</div>\s*<section|<section class=\"panel\" aria-label=\"Model controls\">(.*?)</section>', raw, re.DOTALL)
            ctrl_html = ""
            if ctrl_m:
                ctrl_html = (ctrl_m.group(1) or ctrl_m.group(2) or ctrl_m.group(3) or ctrl_m.group(4) or "").strip()
            
            # Clean up controls HTML
            ctrl_html = re.sub(r'class=[\"\']inputgrid[\"\']', 'class="sim-controls"', ctrl_html)
            ctrl_html = re.sub(r'<div id=\"controls\">', '', ctrl_html)
            
            unit_num = (i // 2) + 1
            models.append({
                'idx': i + 1,
                'unit': unit_num,
                'title': title,
                'desc': desc,
                'type': m_type,
                'controls': ctrl_html
            })
            
        print(f"{slug}: {len(models)} models extracted.")
        
        # Now construct <slug>-sims.js
        # We wrap the simulation logic in a self-executing adapter that hooks into SimulationEngine.initSimulation
        target_path = os.path.join(ROOT, 'src', 'subjects', 'logic-and-systems-science', slug, f"{slug}-sims.js")
        
        js_content = f"""/* {slug} Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var MODELS = {json.dumps(models, indent=2)};

  // Original calculation logic adapted for scoped execution
{sim_js_code}

  if (!window.SimulationEngine) {{
    window.SimulationEngine = {{}};
  }}

  window.SimulationEngine.initSimulation = function(containerId, simType) {{
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';

    var unitNum = 1;
    if (simType) {{
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    }} else {{
      var bMatch = document.body.dataset.chapterIndex || window.location.pathname.match(/chapter-(\\d+)/);
      if (bMatch) {{
        unitNum = typeof bMatch === 'string' ? (parseInt(bMatch, 10) + 1) : parseInt(bMatch[1], 10);
      }}
    }}

    var modelsForUnit = MODELS.filter(function(m) {{ return m.unit === unitNum; }});
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m, idx) {{
      var card = document.createElement('section');
      card.className = 'logic-sim-card';
      card.setAttribute('aria-label', m.title);
      card.id = 'sim-card-' + m.idx;

      var headerHtml = 
        '<div>' +
          '<span class="sim-tag">Unit ' + unitNum + '</span>' +
          '<span class="sim-tag">Interactive Model ' + m.idx + ' of 16</span>' +
        '</div>' +
        '<h3>' + m.title + '</h3>' +
        '<p class="sim-desc">' + m.desc + '</p>';

      var controlsContainer = document.createElement('div');
      controlsContainer.className = 'sim-controls';
      controlsContainer.innerHTML = m.controls || '<div style=\"color:#94a3b8;font-size:0.88rem;\">Model evaluates live parameter derivations.</div>';

      var outputEl = document.createElement('div');
      outputEl.className = 'sim-output';
      outputEl.id = 'output-' + m.idx;
      outputEl.setAttribute('aria-live', 'polite');
      outputEl.innerHTML = '<div style=\"color:#94a3b8;font-size:0.88rem;\">Evaluating local formal semantics…</div>';

      card.innerHTML = headerHtml;
      card.appendChild(controlsContainer);
      card.appendChild(outputEl);
      container.appendChild(card);

      // Scoped update runner
      function runUpdate() {{
        document.body.dataset.type = m.type;
        document.body.dataset.kind = m.type;

        // Route document.querySelector / document.getElementById to local card
        var prevOutput = document.getElementById('output');
        var outputWrapper = outputEl;
        
        // Execute update if available
        if (typeof update === 'function') {{
          // redirect output
          var oldOut = document.querySelector('#output');
          var tempOut = document.createElement('div');
          tempOut.id = 'output';
          document.body.appendChild(tempOut);
          
          try {{
            update();
            outputWrapper.innerHTML = tempOut.innerHTML;
          }} catch(e) {{
            outputWrapper.innerHTML = '<p class=\"warn\">Evaluating derivation step...</p>';
          }} finally {{
            tempOut.remove();
          }}
        }} else if (typeof calculate === 'function') {{
          try {{
            var num = function(name, defVal) {{
              var inp = card.querySelector('[name=\"' + name + '\"], #' + name);
              var v = inp ? Number(inp.value) : defVal;
              return Number.isFinite(v) ? v : defVal;
            }};
            var res = calculate(m.type, num('n', 3), num('a', 3), num('b', 2));
            if (res && res.title && res.rows) {{
              var h = '<h4 style=\"margin:0 0 8px;color:#38bdf8;font-size:1rem;\">' + res.title + '</h4><ol>';
              res.rows.forEach(function(r) {{ h += '<li>' + r + '</li>'; }});
              h += '</ol>';
              outputWrapper.innerHTML = h;
            }}
          }} catch(e) {{
            outputWrapper.innerHTML = '<p class=\"warn\">Evaluating calculation...</p>';
          }}
        }} else if (typeof run === 'function') {{
          try {{
            run();
          }} catch(e) {{}}
        }}
      }}

      // Attach event listeners
      card.querySelectorAll('input, select').forEach(function(inp) {{
        inp.addEventListener('input', runUpdate);
        inp.addEventListener('change', runUpdate);
      }});
      var rerunBtn = card.querySelector('#rerun, button');
      if (rerunBtn) rerunBtn.addEventListener('click', runUpdate);

      // Initial run
      runUpdate();
    }});
  }};

  // Auto-init when DOM is ready if #sim-container is present
  if (typeof document !== 'undefined') {{
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', function() {{
        if (document.getElementById('sim-container')) {{
          window.SimulationEngine.initSimulation('sim-container');
        }}
      }});
    }} else {{
      if (document.getElementById('sim-container')) {{
        window.SimulationEngine.initSimulation('sim-container');
      }}
    }}
  }}
}})(typeof window === 'undefined' ? globalThis : window);
"""
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"  Wrote {target_path}")

print("Simulation generator finished.")
