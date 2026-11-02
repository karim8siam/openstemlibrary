#!/usr/bin/env python3
"""
Generate Interactive Simulation Suites for Civil Engineering Batch 3:
1. fluid-mechanics-and-hydraulics
2. hydrology
3. water-resources-engineering
4. water-supply-and-wastewater-engineering
"""

import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793628498354_3f84ba9b.zip'

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
    # 1. Fluid Mechanics and Hydraulics
    # =========================================================================
    print("Building fluid-mechanics-and-hydraulics-sims.js...")
    fm_labs_raw = z.read("OpenSTEM-Civil-Engineering/books/fluid-mechanics-and-hydraulics/assets/simulations.js").decode("utf-8", errors="ignore")
    # Extract LABS dictionary definition
    labs_match = re.search(r'const\s+LABS\s*=\s*\{([\s\S]*?)\n\};', fm_labs_raw)
    labs_code = labs_match.group(0) if labs_match else ""

    fm_models = []
    for i in range(1, 17):
        lab_html = z.read(f"OpenSTEM-Civil-Engineering/books/fluid-mechanics-and-hydraulics/labs/lab-{i:02d}.html").decode("utf-8", errors="ignore")
        title_m = re.search(r'<h1>(.*?)</h1>', lab_html)
        title = title_m.group(1).replace('Lab ' + f'{i:02d}: ', '').replace('Lab ' + f'{i:02d} — ', '') if title_m else f"Simulation {i}"
        desc_m = re.search(r'<header>[\s\S]*?<p>(.*?)</p>', lab_html)
        desc = desc_m.group(1) if desc_m else ""
        spec_m = re.search(r'<script type="application/json" id="lab-spec">([\s\S]*?)</script>', lab_html)
        spec = json.loads(spec_m.group(1)) if spec_m else {}
        unit = (i + 1) // 2
        fm_models.append({
            "idx": i,
            "unit": unit,
            "title": title,
            "desc": desc,
            "kind": spec.get("kind"),
            "controls": spec.get("controls", []),
            "output": spec.get("output", "Value"),
            "outputUnit": spec.get("outputUnit", "")
        })

    fm_js = f"""/* Fluid Mechanics and Hydraulics Interactive Simulation Suite */
(function(window) {{
  'use strict';

  const G = 9.81;
  {labs_code}

  var FM_SPECS = {json.dumps(fm_models, indent=2)};

  var MODELS = FM_SPECS.map(function(spec) {{
    var controlsHtml = spec.controls.map(function(c, ci) {{
      var name = c[0], unit = c[1], def = c[2], min = c[3], max = c[4], step = c[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="fm_' + spec.idx + '_' + ci + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_fm_' + spec.idx + '_' + ci + '" style="font-weight:700;color:#0284c7;">' + def + '</span></label>' +
             '<input id="fm_' + spec.idx + '_' + ci + '" data-cidx="' + ci + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#0284c7;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#e0f2fe;color:#0369a1;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + spec.idx + ' · Unit ' + spec.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.title + '</h3>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + spec.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdf4;border-left:4px solid #16a34a;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#166534;font-weight:600;text-transform:uppercase;">' + spec.output + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#15803d;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#14532d;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: spec.idx,
      unit: spec.unit,
      html: html,
      init: function(card) {{
        try {{
          var p = spec.controls.map(function(c) {{ return c[2]; }});
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(samples, currP) {{
            if (!svgEl || !samples.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var ymin = Math.min(0, Math.min.apply(null, samples.map(function(d) {{ return d[1]; }})));
            var ymax = Math.max.apply(null, samples.map(function(d) {{ return d[1]; }}));
            if (ymax <= ymin) ymax = ymin + 1;
            var xmin = samples[0][0], xmax = samples[samples.length - 1][0];
            var xx = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yy = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var k = 0; k <= 4; k++) {{
              var v = ymin + k * (ymax - ymin) / 4, yPos = yy(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pts = samples.map(function(d) {{ return xx(d[0]) + ',' + yy(d[1]); }}).join(' ');
            node('polyline', {{ points: pts, fill: 'none', stroke: '#0284c7', 'stroke-width': '2.5' }});

            var currRes = LABS[spec.kind](currP);
            var currY = currRes[0];
            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xx(currP[0]), cy: yy(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, spec.controls[0][0] + ' (' + spec.controls[0][1] + ')');
            node('text', {{ x: L, y: H - B + 18, fill: '#64748b', 'font-size': '10' }}, Number(xmin.toPrecision(3)).toString());
            node('text', {{ x: W - R, y: H - B + 18, 'text-anchor': 'end', fill: '#64748b', 'font-size': '10' }}, Number(xmax.toPrecision(3)).toString());
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var ci = parseInt(inp.dataset.cidx, 10);
              p[ci] = Number(inp.value);
              var vLbl = card.querySelector('#v_fm_' + spec.idx + '_' + ci);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var res = LABS[spec.kind](p);
            var val = res[0], note = res[1];
            if (valEl) {{
              valEl.textContent = Number.isFinite(val) ? Number(val.toPrecision(5)) + ' ' + spec.outputUnit : 'Out of range';
            }}
            if (interpEl) interpEl.textContent = note;

            // Generate sensitivity points varying first control
            var s = spec.controls[0], samples = [];
            for (var k = 0; k <= 60; k++) {{
              var x = s[3] + (s[4] - s[3]) * k / 60;
              var t = p.slice();
              t[0] = x;
              var y = LABS[spec.kind](t)[0];
              if (Number.isFinite(y)) samples.push([x, y]);
            }}
            drawGraph(samples, p);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('FM sim error on lab ' + spec.idx, err);
        }}
      }}
    }};
  }});
{get_engine_footer('fluid-mechanics-and-hydraulics')}"""

    fm_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'fluid-mechanics-and-hydraulics', 'fluid-mechanics-and-hydraulics-sims.js')
    with open(fm_out_path, 'w', encoding='utf-8') as f:
        f.write(fm_js)
    print(f"Wrote {fm_out_path}")

    # =========================================================================
    # 2. Hydrology
    # =========================================================================
    print("Building hydrology-sims.js...")
    hydro_labs_raw = z.read("OpenSTEM-Civil-Engineering/books/hydrology/assets/simulations.js").decode("utf-8", errors="ignore")
    # Extract MODELS dictionary definition
    hydro_models_match = re.search(r'const\s+MODELS\s*=\s*\{([\s\S]*?)\n\};', hydro_labs_raw)
    hydro_models_code = re.sub(r'const\s+MODELS\s*=', 'const HYDRO_MODELS =', hydro_models_match.group(0)) if hydro_models_match else ""

    h_models = []
    for i in range(1, 17):
        lab_html = z.read(f"OpenSTEM-Civil-Engineering/books/hydrology/labs/lab-{i:02d}.html").decode("utf-8", errors="ignore")
        title_m = re.search(r'<h1>(.*?)</h1>', lab_html)
        title = title_m.group(1).replace('Hydrology Lab ' + f'{i}: ', '').replace('Lab ' + f'{i:02d} — ', '') if title_m else f"Simulation {i}"
        desc_m = re.search(r'<header>[\s\S]*?<p>(.*?)</p>', lab_html)
        desc = desc_m.group(1) if desc_m else ""
        spec_m = re.search(r'<script type="application/json" id="lab-spec">([\s\S]*?)</script>', lab_html)
        spec = json.loads(spec_m.group(1)) if spec_m else {}
        unit = (i + 1) // 2
        h_models.append({
            "idx": i,
            "unit": unit,
            "title": title,
            "desc": desc,
            "kind": spec.get("kind"),
            "controls": spec.get("controls", []),
            "output": spec.get("output", "Value"),
            "unitLabel": spec.get("unit", "")
        })

    hydro_js = f"""/* Hydrology Interactive Simulation Suite */
(function(window) {{
  'use strict';

  const gamma = 0.5772156649015329;
  const G = 9.81;
  {hydro_models_code}

  var HYDRO_SPECS = {json.dumps(h_models, indent=2)};

  var MODELS = HYDRO_SPECS.map(function(spec) {{
    var controlsHtml = spec.controls.map(function(c, ci) {{
      var name = c[0], unit = c[1], def = c[2], min = c[3], max = c[4], step = c[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="h_' + spec.idx + '_' + ci + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_h_' + spec.idx + '_' + ci + '" style="font-weight:700;color:#0d9488;">' + def + '</span></label>' +
             '<input id="h_' + spec.idx + '_' + ci + '" data-cidx="' + ci + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#0d9488;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#ccfbf1;color:#0f766e;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + spec.idx + ' · Unit ' + spec.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.title + '</h3>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + spec.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdfa;border-left:4px solid #0d9488;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#115e59;font-weight:600;text-transform:uppercase;">' + spec.output + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#0f766e;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#134e4a;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: spec.idx,
      unit: spec.unit,
      html: html,
      init: function(card) {{
        try {{
          var p = spec.controls.map(function(c) {{ return c[2]; }});
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(samples, currP) {{
            if (!svgEl || !samples.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var ymin = Math.min(0, Math.min.apply(null, samples.map(function(d) {{ return d[1]; }})));
            var ymax = Math.max.apply(null, samples.map(function(d) {{ return d[1]; }}));
            if (ymax <= ymin) ymax = ymin + 1;
            var xmin = samples[0][0], xmax = samples[samples.length - 1][0];
            var xx = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yy = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var k = 0; k <= 4; k++) {{
              var v = ymin + k * (ymax - ymin) / 4, yPos = yy(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pts = samples.map(function(d) {{ return xx(d[0]) + ',' + yy(d[1]); }}).join(' ');
            node('polyline', {{ points: pts, fill: 'none', stroke: '#0d9488', 'stroke-width': '2.5' }});

            var currRes = HYDRO_MODELS[spec.kind](currP);
            var currY = currRes[0];
            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xx(currP[0]), cy: yy(currY), r: 6, fill: '#f97316', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, spec.controls[0][0] + ' (' + spec.controls[0][1] + ')');
            node('text', {{ x: L, y: H - B + 18, fill: '#64748b', 'font-size': '10' }}, Number(xmin.toPrecision(3)).toString());
            node('text', {{ x: W - R, y: H - B + 18, 'text-anchor': 'end', fill: '#64748b', 'font-size': '10' }}, Number(xmax.toPrecision(3)).toString());
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var ci = parseInt(inp.dataset.cidx, 10);
              p[ci] = Number(inp.value);
              var vLbl = card.querySelector('#v_h_' + spec.idx + '_' + ci);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var res = HYDRO_MODELS[spec.kind](p);
            var val = res[0], note = res[1];
            if (valEl) {{
              valEl.textContent = Number.isFinite(val) ? Number(val.toPrecision(5)) + ' ' + spec.unitLabel : 'Out of range';
            }}
            if (interpEl) interpEl.textContent = note;

            // Generate sensitivity points
            var s = spec.controls[0], samples = [];
            for (var k = 0; k <= 60; k++) {{
              var x = s[3] + (s[4] - s[3]) * k / 60;
              var t = p.slice();
              t[0] = x;
              var y = HYDRO_MODELS[spec.kind](t)[0];
              if (Number.isFinite(y)) samples.push([x, y]);
            }}
            drawGraph(samples, p);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('Hydrology sim error on lab ' + spec.idx, err);
        }}
      }}
    }};
  }});
{get_engine_footer('hydrology')}"""

    hydro_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'hydrology', 'hydrology-sims.js')
    with open(hydro_out_path, 'w', encoding='utf-8') as f:
        f.write(hydro_js)
    print(f"Wrote {hydro_out_path}")

    # =========================================================================
    # 3. Water Resources Engineering
    # =========================================================================
    print("Building water-resources-engineering-sims.js...")
    wre_models_json = json.loads(z.read("OpenSTEM-Civil-Engineering/books/water-resources-engineering/assets/models.json").decode("utf-8", errors="ignore"))
    wre_models_js = z.read("OpenSTEM-Civil-Engineering/books/water-resources-engineering/assets/models.js").decode("utf-8", errors="ignore")
    # Extract compute function
    compute_fn_match = re.search(r'function compute\(id,v\)\{([\s\S]*?)\n\}\n\s*(?:if|root)', wre_models_js)
    compute_fn_body = compute_fn_match.group(1) if compute_fn_match else ""

    wre_js = f"""/* Water Resources Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  const max = Math.max, min = Math.min, exp = Math.exp, log = Math.log, sqrt = Math.sqrt, PI = Math.PI;

  function compute(id, v) {{
    {compute_fn_body}
  }}

  var WRE_MODELS = {json.dumps(wre_models_json, indent=2)};

  var MODELS = WRE_MODELS.map(function(mDef) {{
    var controlsHtml = mDef.params.map(function(p, pi) {{
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="wre_' + mDef.id + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_wre_' + mDef.id + '_' + pi + '" style="font-weight:700;color:#2563eb;">' + p.default + '</span></label>' +
             '<input id="wre_' + mDef.id + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#2563eb;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#dbeafe;color:#1e40af;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Model ' + mDef.id + ' · Unit ' + mDef.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + mDef.title + '</h3>' +
               '<div style="background:#eff6ff;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#1e40af;margin-bottom:0.75rem;">' + (mDef.equation || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (mDef.assumption || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdf4;border-left:4px solid #16a34a;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div class="metrics-grid" style="display:flex;flex-wrap:wrap;gap:1rem;"></div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#14532d;margin-top:0.5rem;font-style:italic;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 780 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: mDef.id,
      unit: mDef.unit,
      html: html,
      init: function(card) {{
        try {{
          var pVals = mDef.params.map(function(p) {{ return p.default; }});
          var metricsGrid = card.querySelector('.metrics-grid');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(series, title) {{
            if (!svgEl || !series.length) return;
            svgEl.innerHTML = '';
            var W = 780, H = 330, L = 70, R = 24, T = 27, B = 58;
            var good = series.filter(function(p) {{ return p.y !== null && Number.isFinite(p.y); }});
            if (!good.length) return;
            var xmin = Math.min.apply(null, good.map(function(p) {{ return p.x; }}));
            var xmax = Math.max.apply(null, good.map(function(p) {{ return p.x; }}));
            var ymin = Math.min(0, Math.min.apply(null, good.map(function(p) {{ return p.y; }})));
            var ymax = Math.max.apply(null, good.map(function(p) {{ return p.y; }}));
            if (xmax === xmin) xmax = xmin + 1;
            if (ymax === ymin) ymax = ymin + 1;

            var X = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var Y = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i < 5; i++) {{
              var yVal = ymin + (ymax - ymin) * i / 4, yPos = Y(yVal);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '4 6' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(yVal.toPrecision(3)).toString());
            }}
            for (var j = 0; j < 5; j++) {{
              var xVal = xmin + (xmax - xmin) * j / 4;
              node('text', {{ x: X(xVal), y: H - B + 20, 'text-anchor': 'middle', fill: '#64748b', 'font-size': '11' }}, Number(xVal.toPrecision(3)).toString());
            }}

            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pts = good.map(function(p) {{ return X(p.x).toFixed(1) + ',' + Y(p.y).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pts, fill: 'none', stroke: '#2563eb', 'stroke-width': '2.5' }});
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_wre_' + mDef.id + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var out = compute(mDef.id, pVals);
            if (metricsGrid && out.res) {{
              var resKeys = Object.keys(out.res);
              metricsGrid.innerHTML = resKeys.map(function(k) {{
                var val = out.res[k];
                var displayVal = Number.isFinite(val) ? Number(val.toPrecision(4)) : String(val);
                return '<div style="min-width:130px;"><span style="font-size:0.75rem;color:#166534;font-weight:600;display:block;">' + k + '</span><span style="font-size:1.25rem;font-weight:700;color:#15803d;">' + displayVal + '</span></div>';
              }}).join('');
            }}
            if (interpEl) interpEl.textContent = out.note || '';
            if (out.series) drawGraph(out.series, mDef.title);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('WRE sim error on model ' + mDef.id, err);
        }}
      }}
    }};
  }});
{get_engine_footer('water-resources-engineering')}"""

    wre_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'water-resources-engineering', 'water-resources-engineering-sims.js')
    with open(wre_out_path, 'w', encoding='utf-8') as f:
        f.write(wre_js)
    print(f"Wrote {wre_out_path}")

    # =========================================================================
    # 4. Water Supply and Wastewater Engineering
    # =========================================================================
    print("Building water-supply-and-wastewater-engineering-sims.js...")
    wsw_models_json = json.loads(z.read("OpenSTEM-Civil-Engineering/books/water-supply-and-wastewater-engineering/assets/models.json").decode("utf-8", errors="ignore"))
    wsw_lab_js = z.read("OpenSTEM-Civil-Engineering/books/water-supply-and-wastewater-engineering/assets/lab.js").decode("utf-8", errors="ignore")
    # Extract solve function
    solve_match = re.search(r'function solve\(kind,p\)\{([\s\S]*?)\n\}\nfunction svgChart', wsw_lab_js)
    solve_fn_body = solve_match.group(1) if solve_match else ""

    wsw_js = f"""/* Water Supply and Wastewater Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  const pi = Math.PI, g = 9.81;

  function solve(kind, p) {{
    {solve_fn_body}
  }}

  var WSW_MODELS = {json.dumps(wsw_models_json, indent=2)};

  var MODELS = WSW_MODELS.map(function(mDef, idx) {{
    var controlsHtml = mDef.params.map(function(p, pi) {{
      var name = p[0], unit = p[1], min = p[2], max = p[3], def = p[4], step = p[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="wsw_' + (idx + 1) + '_' + pi + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_wsw_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#059669;">' + def + '</span></label>' +
             '<input id="wsw_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#059669;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#d1fae5;color:#065f46;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Model ' + (idx + 1) + ' · Unit ' + mDef.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + mDef.title + '</h3>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (mDef.question || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#ecfdf5;border-left:4px solid #059669;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#065f46;font-weight:600;text-transform:uppercase;">' + (mDef.yLabel || 'Result') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#047857;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#064e3b;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 730 310" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.8rem;color:#64748b;margin-top:0.5rem;font-style:italic;">' + (mDef.note || '') + '</div>';

    return {{
      idx: idx + 1,
      unit: mDef.unit,
      html: html,
      init: function(card) {{
        try {{
          var pVals = mDef.params.map(function(p) {{ return p[4]; }});
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(xData, yData, currX, currY) {{
            if (!svgEl || !xData.length) return;
            svgEl.innerHTML = '';
            var W = 730, H = 310, left = 64, right = 22, top = 25, bottom = 52;
            var x0 = Math.min.apply(null, xData), x1 = Math.max.apply(null, xData);
            var y0 = Math.min(0, Math.min.apply(null, yData), currY);
            var y1 = Math.max(1e-10, Math.max.apply(null, yData), currY);
            if (y1 - y0 < 1e-8) y1 = y0 + 1;

            var xp = function(x) {{ return left + (x - x0) / (x1 - x0 || 1) * (W - left - right); }};
            var yp = function(y) {{ return H - bottom - (y - y0) / (y1 - y0 || 1) * (H - top - bottom); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i < 5; i++) {{
              var v = y0 + (y1 - y0) * i / 4, Ypos = yp(v);
              node('line', {{ x1: left, y1: Ypos, x2: W - right, y2: Ypos, stroke: '#e2e8f0', 'stroke-dasharray': '3 6' }});
              node('text', {{ x: left - 8, y: Ypos + 5, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            for (var j = 0; j < 5; j++) {{
              var xV = x0 + (x1 - x0) * j / 4;
              node('text', {{ x: xp(xV), y: H - bottom + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': '11' }}, Number(xV.toPrecision(3)).toString());
            }}

            node('line', {{ x1: left, y1: top, x2: left, y2: H - bottom, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: left, y1: H - bottom, x2: W - right, y2: H - bottom, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pts = xData.map(function(x, idx) {{ return xp(x).toFixed(1) + ',' + yp(yData[idx]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pts, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (left + W - right) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, mDef.xLabel || 'Input');
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_wsw_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var res = solve(mDef.kind, pVals);
            if (valEl) {{
              valEl.textContent = Number.isFinite(res.y) ? Number(res.y.toPrecision(4)) + ' ' + (mDef.yUnit || '') : '--';
            }}
            if (interpEl) interpEl.textContent = res.info || '';

            // Generate sensitivity curve varying parameter 0
            var p0Def = mDef.params[0];
            var min0 = p0Def[2], max0 = p0Def[3];
            var xData = [], yData = [];
            for (var s = 0; s <= 40; s++) {{
              var xV = min0 + (max0 - min0) * s / 40;
              var curP = pVals.slice();
              curP[0] = xV;
              var ptRes = solve(mDef.kind, curP);
              if (Number.isFinite(ptRes.y)) {{
                xData.push(xV);
                yData.push(ptRes.y);
              }}
            }}
            drawGraph(xData, yData, pVals[0], res.y);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('WSW sim error on model ' + (idx + 1), err);
        }}
      }}
    }};
  }});
{get_engine_footer('water-supply-and-wastewater-engineering')}"""

    wsw_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'water-supply-and-wastewater-engineering', 'water-supply-and-wastewater-engineering-sims.js')
    with open(wsw_out_path, 'w', encoding='utf-8') as f:
        f.write(wsw_js)
    print(f"Wrote {wsw_out_path}")

print("Batch 3 simulation suites generated successfully!")
