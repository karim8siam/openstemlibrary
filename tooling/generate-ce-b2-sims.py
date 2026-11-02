import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793628498354_3f84ba9b.zip'

print("Generating Batch 2 Civil Engineering Simulation Suites...")

def get_engine_footer(book_name, total_units=8):
    return f"""
  if (!window.SimulationEngine) window.SimulationEngine = {{}};
  window.SimulationEngine.initSimulation = function(containerId, simType) {{
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {{
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    }} else {{
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {{
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }}
    }}
    if (isNaN(unitNum) || unitNum < 1 || unitNum > {total_units}) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) {{ return m.unit === unitNum; }});
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) {{ return m.unit === 1; }});
    modelsForUnit.forEach(function(m) {{
      var card = document.createElement('section');
      card.className = 'ce-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    }});
  }};

  if (typeof document !== 'undefined') {{
    var autoInit = function() {{
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {{
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }}
    }};
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', autoInit);
    }} else {{
      autoInit();
    }}
  }}
}})(typeof window === 'undefined' ? globalThis : window);
"""

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    # =========================================================================
    # 1. Reinforced Concrete Design (8 units, 15 simulation models)
    # =========================================================================
    print("Building reinforced-concrete-design-sims.js...")
    rc_src = z.read("OpenSTEM-Civil-Engineering/books/reinforced-concrete-design/assets/models.js").decode("utf-8", errors="ignore")

    # Extract MODELS object and helpers
    models_obj_str = rc_src[rc_src.find('const MODELS = {'):rc_src.find('function points(')]
    models_obj_str = models_obj_str.replace('const MODELS = {', 'const RC_MODELS = {')
    helpers_str = rc_src[rc_src.find('function points('):rc_src.find('function mount()')]

    rc_js = f"""/* Reinforced Concrete Design Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {models_obj_str}
  {helpers_str}

  var MODELS_LIST = [];
  var modelKeys = Object.keys(RC_MODELS);

  modelKeys.forEach(function(key, idx) {{
    var mDef = RC_MODELS[key];
    var unit = mDef.unit || 1;

    var controlsHtml = mDef.vars.map(function(v) {{
      var vid = v[0], label = v[1], min = v[2], max = v[3], def = v[4], step = v[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="rc_' + key + '_' + vid + '">' + label + ' <span id="v_rc_' + key + '_' + vid + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="rc_' + key + '_' + vid + '" data-var="' + vid + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.about + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="schematic" style="margin:1rem 0;display:block;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 860 380" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({{
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {{
        try {{
          var p = {{}};
          mDef.vars.forEach(function(v) {{ p[v[0]] = v[4]; }});
          var metricsEl = card.querySelector('.metrics');
          var schEl = card.querySelector('.schematic');
          var plotSvg = card.querySelector('.plot-svg');
          var noteEl = card.querySelector('.model-note');

          function updateRC() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var vid = inp.dataset.var;
              p[vid] = Number(inp.value);
              var vLbl = card.querySelector('#v_rc_' + key + '_' + vid);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var out = mDef.calc(p);
            if (metricsEl && out.metrics) {{
              metricsEl.innerHTML = out.metrics.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? fmt(m[1]) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }}).join('');
            }}

            if (schEl) {{
              while (schEl.firstChild) schEl.removeChild(schEl.firstChild);
              var sch = schematic(key, p);
              if (sch) schEl.appendChild(sch);
            }}

            if (plotSvg && out.series) {{
              drawPlot(plotSvg, out.series, out.xLabel || 'Position');
            }}

            if (noteEl) noteEl.textContent = out.note || mDef.assumptions || '';
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateRC);
          }});
          updateRC();
        }} catch (err) {{
          console.warn('Reinforced Concrete sim error in model ' + key + ':', err);
        }}
      }}
    }});
  }});

  var MODELS = MODELS_LIST;
"""
    rc_js += get_engine_footer('Reinforced Concrete Design', 8)
    rc_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'reinforced-concrete-design', 'reinforced-concrete-design-sims.js')
    with open(rc_dest, 'w', encoding='utf-8') as f:
        f.write(rc_js)
    print(f"Wrote {rc_dest}")

    # =========================================================================
    # 2. Steel Structure Design (8 units, 15 simulation models)
    # =========================================================================
    print("Building steel-structure-design-sims.js...")
    steel_src = z.read("OpenSTEM-Civil-Engineering/books/steel-structure-design/assets/models.js").decode("utf-8", errors="ignore")

    lin_str = steel_src[steel_src.find('const lin='):steel_src.find('function formatNum(')]
    helpers_steel_str = steel_src[steel_src.find('function formatNum('):steel_src.find('function mount()')]

    steel_js = f"""/* Steel Structure Design Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {lin_str}
  {helpers_steel_str}

  var MODELS_LIST = [];
  var modelKeys = Object.keys(S);

  modelKeys.forEach(function(key, idx) {{
    var mDef = S[key];
    var unit = mDef.unit || 1;

    var controlsHtml = mDef.inputs.map(function(v) {{
      var vid = v[0], label = v[1], min = v[2], max = v[3], def = v[4], step = v[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ssd_' + key + '_' + vid + '">' + label + ' <span id="v_ssd_' + key + '_' + vid + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="ssd_' + key + '_' + vid + '" data-var="' + vid + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.about + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="schematic" style="margin:1rem 0;display:block;"><svg class="sch-svg" viewBox="0 0 760 128" style="width:100%;height:auto;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 860 410" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({{
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {{
        try {{
          var p = {{}};
          mDef.inputs.forEach(function(v) {{ p[v[0]] = v[4]; }});
          var metricsEl = card.querySelector('.metrics');
          var schSvg = card.querySelector('.sch-svg');
          var plotSvg = card.querySelector('.plot-svg');
          var noteEl = card.querySelector('.model-note');

          function updateSteel() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var vid = inp.dataset.var;
              p[vid] = Number(inp.value);
              var vLbl = card.querySelector('#v_ssd_' + key + '_' + vid);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var out = mDef.calc(p);
            if (metricsEl && out.metrics) {{
              metricsEl.innerHTML = out.metrics.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? formatNum(m[1]) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }}).join('');
            }}

            if (schSvg) {{
              scheme(schSvg, key, p);
            }}

            if (plotSvg && out.series) {{
              plot(plotSvg, out.series, out.xLabel || 'Parameter');
            }}

            if (noteEl) noteEl.textContent = out.note || mDef.assumptions || '';
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateSteel);
          }});
          updateSteel();
        }} catch (err) {{
          console.warn('Steel Structure sim error in model ' + key + ':', err);
        }}
      }}
    }});
  }});

  var MODELS = MODELS_LIST;
"""
    steel_js += get_engine_footer('Steel Structure Design', 8)
    steel_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'steel-structure-design', 'steel-structure-design-sims.js')
    with open(steel_dest, 'w', encoding='utf-8') as f:
        f.write(steel_js)
    print(f"Wrote {steel_dest}")

    # =========================================================================
    # 3. Soil Mechanics (8 units, 16 simulation models)
    # =========================================================================
    print("Building soil-mechanics-sims.js...")
    soil_src = z.read("OpenSTEM-Civil-Engineering/books/soil-mechanics/assets/soil-labs.js").decode("utf-8", errors="ignore")

    models_soil_str = soil_src[soil_src.find('const model={'):soil_src.find('function result(')]
    helpers_soil_str = soil_src[soil_src.find('function result('):soil_src.find('function init()')]

    # Read specs from the 16 HTML files
    soil_specs = []
    for i in range(1, 17):
        html_p = f"OpenSTEM-Civil-Engineering/books/soil-mechanics/labs/lab-{i:02d}.html"
        c = z.read(html_p).decode("utf-8", errors="ignore")
        title_m = re.search(r'<h1>(.*?)</h1>', c)
        title = title_m.group(1) if title_m else f"Lab {i}"
        lead_m = re.search(r'<p class="lead">(.*?)</p>', c)
        lead = lead_m.group(1) if lead_m else ""
        spec_m = re.search(r'window\.SOIL_SPEC=(\{.*?\});', c)
        spec = json.loads(spec_m.group(1)) if spec_m else {"model": "phase", "params": []}
        unit = ((i - 1) // 2) + 1
        soil_specs.append({
            "idx": i,
            "unit": unit,
            "title": title,
            "lead": lead,
            "spec": spec
        })

    soil_js = f"""/* Soil Mechanics Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {models_soil_str}
  {helpers_soil_str}

  var SOIL_SPECS = {json.dumps(soil_specs)};
  var MODELS_LIST = [];

  SOIL_SPECS.forEach(function(item, idx) {{
    var spec = item.spec;
    var modelId = spec.model;
    var unit = item.unit;

    var controlsHtml = spec.params.map(function(p) {{
      var pid = p[0], label = p[1], min = p[2], max = p[3], step = p[4], def = p[5], unitStr = p[6] || '';
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sm_' + modelId + '_' + pid + '">' + label + ' <span id="v_sm_' + modelId + '_' + pid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="sm_' + modelId + '_' + pid + '" data-pid="' + pid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + item.idx + ' · Unit ' + unit + '</span><h3>' + item.title + '</h3><p>' + item.lead + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({{
      idx: item.idx,
      unit: unit,
      key: modelId,
      html: html,
      init: function(card) {{
        try {{
          var p = {{}};
          spec.params.forEach(function(param) {{ p[param[0]] = param[5]; }});
          var metricsEl = card.querySelector('.metrics');
          var plotEl = card.querySelector('.plot');
          var noteEl = card.querySelector('.model-note');

          function updateSoil() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pid = inp.dataset.pid;
              p[pid] = Number(inp.value);
              var vLbl = card.querySelector('#v_sm_' + modelId + '_' + pid);
              if (vLbl) vLbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            }});

            var fn = model[modelId];
            if (!fn) return;
            var out = fn(p);

            if (metricsEl && out.values) {{
              metricsEl.innerHTML = out.values.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? m[1].toFixed(3) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }}).join('');
            }}

            if (plotEl && out.series) {{
              plotEl.innerHTML = chart(out.series, out.xLabel, out.yLabel);
            }}

            if (noteEl && out.notes) {{
              noteEl.textContent = out.notes.join(' ');
            }}
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateSoil);
          }});
          updateSoil();
        }} catch (err) {{
          console.warn('Soil Mechanics sim error in model ' + modelId + ':', err);
        }}
      }}
    }});
  }});

  var MODELS = MODELS_LIST;
"""
    soil_js += get_engine_footer('Soil Mechanics', 8)
    soil_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'soil-mechanics', 'soil-mechanics-sims.js')
    with open(soil_dest, 'w', encoding='utf-8') as f:
        f.write(soil_js)
    print(f"Wrote {soil_dest}")

    # =========================================================================
    # 4. Foundation Engineering (8 units, 16 simulation models)
    # =========================================================================
    print("Building foundation-engineering-sims.js...")
    fe_src = z.read("OpenSTEM-Civil-Engineering/books/foundation-engineering/assets/foundation-labs.js").decode("utf-8", errors="ignore")
    fe_specs = json.loads(z.read("OpenSTEM-Civil-Engineering/books/foundation-engineering/assets/lab-specs.json").decode("utf-8"))

    # Extract helpers and solve
    helpers_fe_str = fe_src[fe_src.find('const $=id=>'):fe_src.find('function init()')]

    fe_specs_list = []
    for idx, sp in enumerate(fe_specs, 1):
        html_p = f"OpenSTEM-Civil-Engineering/books/foundation-engineering/labs/lab-{idx:02d}.html"
        c = z.read(html_p).decode("utf-8", errors="ignore") if html_p in z.namelist() else ""
        t_m = re.search(r'<h1>(.*?)</h1>', c)
        title = t_m.group(1) if t_m else sp["id"].replace('-', ' ').title()
        lead_m = re.search(r'<p class="lead">(.*?)</p>', c)
        lead = lead_m.group(1) if lead_m else "Interactive foundation mechanics model."
        unit = ((idx - 1) // 2) + 1
        if unit > 8: unit = 8
        fe_specs_list.append({
            "idx": idx,
            "unit": unit,
            "id": sp["id"],
            "title": title,
            "lead": lead,
            "inputs": sp["inputs"]
        })

    fe_js = f"""/* Foundation Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var PI = Math.PI;
  var n = function(a, b, N) {{ N = N || 51; return Array.from({{length: N}}, function(_, i) {{ return a + (b - a) * i / (N - 1); }}); }};
  var safe = function(x) {{ return Number.isFinite(x) ? x : 0; }};
  var series = function(label, values) {{ return {{label: label, values: values.map(safe)}}; }};
  var fmt = function(v, d) {{ d = (d === undefined) ? 3 : d; return Number.isFinite(v) ? Number(v.toFixed(d)).toLocaleString('en-US') : '—'; }};

  {helpers_fe_str[helpers_fe_str.find('function solve('):]}

  var FE_SPECS = {json.dumps(fe_specs_list)};
  var MODELS_LIST = [];

  FE_SPECS.forEach(function(item, idx) {{
    var labId = item.id;
    var unit = item.unit;

    var controlsHtml = item.inputs.map(function(inp) {{
      var kid = inp.key, label = inp.name, min = inp.min, max = inp.max, step = inp.step, def = inp.def, unitStr = inp.unit || '';
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="fe_' + labId + '_' + kid + '">' + label + ' <span id="v_fe_' + labId + '_' + kid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="fe_' + labId + '_' + kid + '" data-key="' + kid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + item.idx + ' · Unit ' + unit + '</span><h3>' + item.title + '</h3><p>' + item.lead + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({{
      idx: item.idx,
      unit: unit,
      id: labId,
      html: html,
      init: function(card) {{
        try {{
          var p = {{}};
          item.inputs.forEach(function(inp) {{ p[inp.key] = inp.def; }});
          var metricsEl = card.querySelector('.metrics');
          var plotEl = card.querySelector('.plot');
          var noteEl = card.querySelector('.model-note');

          function updateFE() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var kid = inp.dataset.key;
              p[kid] = Number(inp.value);
              var vLbl = card.querySelector('#v_fe_' + labId + '_' + kid);
              if (vLbl) vLbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            }});

            var res = solve(labId, p);
            if (metricsEl && res.met) {{
              metricsEl.innerHTML = res.met.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + m[1] + '</output></div>';
              }}).join('');
            }}

            if (plotEl && res.lines) {{
              plotEl.innerHTML = chart(res);
            }}

            if (noteEl && res.warning) {{
              noteEl.textContent = res.warning;
            }}
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateFE);
          }});
          updateFE();
        }} catch (err) {{
          console.warn('Foundation Engineering sim error in lab ' + labId + ':', err);
        }}
      }}
    }});
  }});

  var MODELS = MODELS_LIST;
"""
    fe_js += get_engine_footer('Foundation Engineering', 8)
    fe_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'foundation-engineering', 'foundation-engineering-sims.js')
    with open(fe_dest, 'w', encoding='utf-8') as f:
        f.write(fe_js)
    print(f"Wrote {fe_dest}")

print("\nBatch 2 simulation suites generated successfully!")
