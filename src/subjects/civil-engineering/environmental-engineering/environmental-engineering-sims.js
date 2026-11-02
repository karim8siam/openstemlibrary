/* Environmental Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  function eeCalc(id, x, a, b) {
    switch(id) {
      case 'cstr': return b / (1 + a * x);
      case 'decay': return a * Math.exp(-b * x);
      case 'mixing': return (a * 2 + x * b) / (a + x);
      case 'oxygen': {
        let kd = 0.24, kr = b, d0 = 0.5;
        if (Math.abs(kr - kd) < 1e-8) return kd * a * x * Math.exp(-kd * x) + d0 * Math.exp(-kd * x);
        return kd * a / (kr - kd) * (Math.exp(-kd * x) - Math.exp(-kr * x)) + d0 * Math.exp(-kr * x);
      }
      case 'settling': return 100 * Math.min(1, a / (b / x));
      case 'filter': return (0.001 * x * (a / 3600)) / (1000 * 9.81 * (b * 1e-10));
      case 'disinfect': return a * Math.exp(-b * x);
      case 'fm': return (5000 * a) / (x * b);
      case 'monod': return a * x / (b + x);
      case 'nutrient': return 0.001 * a * (b - x);
      case 'plume': {
        let sy = 0.12 * Math.pow(x, 0.9), sz = 0.06 * Math.pow(x, 0.85);
        return 1e6 * a / (Math.PI * b * sy * sz) * Math.exp(-900 / (2 * sz * sz));
      }
      case 'capture': return 1e-6 * x * a * b / 100;
      case 'recycle': return x * a * b * 0.85;
      case 'landfill': return a * b * 1e5 * Math.exp(-a * x);
      case 'exposure': return a * x / b;
      case 'carbon': return x * a * b;
      default: return NaN;
    }
  }

  var EE_SPECS = [
  {
    "number": 1,
    "name": "Complete-Mix Reactor",
    "id": "cstr",
    "unit": 1,
    "parameters": [
      {
        "name": "First-order removal k",
        "unit": "1/day",
        "min": 0.05,
        "max": 1,
        "step": 0.01,
        "default": 0.3
      },
      {
        "name": "Inlet concentration C_in",
        "unit": "mg/L",
        "min": 5,
        "max": 100,
        "step": 1,
        "default": 30
      }
    ],
    "formula": "C_out = C_in/(1+k \u03c4)",
    "xmin": 0.2,
    "xmax": 15,
    "xLabel": "Residence time \u03c4 (days)",
    "yLabel": "C_out (mg/L)",
    "yUnit": "mg/L",
    "xUnit": "days",
    "limits": "Well-mixed steady-state first-order model. Short circuiting, toxicity and kinetics changes omitted.",
    "prompt": "Compare a CSTR with plug flow at the same residence time and degradation coefficient."
  },
  {
    "number": 2,
    "name": "Pollutant Decay and Half-life",
    "id": "decay",
    "unit": 1,
    "parameters": [
      {
        "name": "Initial concentration",
        "unit": "mg/L",
        "min": 5,
        "max": 100,
        "step": 1,
        "default": 40
      },
      {
        "name": "Reaction rate k",
        "unit": "1/day",
        "min": 0.01,
        "max": 0.6,
        "step": 0.01,
        "default": 0.15
      }
    ],
    "formula": "C(t)=C\u2080exp(\u2212kt)",
    "xmin": 0,
    "xmax": 30,
    "xLabel": "Time (days)",
    "yLabel": "C (mg/L)",
    "yUnit": "mg/L",
    "xUnit": "days",
    "limits": "One-compartment constant-temperature first-order kinetics; not a validated environmental fate model.",
    "prompt": "At what time does predicted concentration fall to 25% and what happens if k is halved?"
  },
  {
    "number": 3,
    "name": "Stream Mixing and Load Balance",
    "id": "mixing",
    "unit": 2,
    "parameters": [
      {
        "name": "River discharge Q_r",
        "unit": "m\u00b3/s",
        "min": 0.2,
        "max": 12,
        "step": 0.1,
        "default": 3
      },
      {
        "name": "Effluent concentration C_e",
        "unit": "mg/L",
        "min": 1,
        "max": 60,
        "step": 0.5,
        "default": 15
      }
    ],
    "formula": "C_mix=(Q_r C_r+Q_e C_e)/(Q_r+Q_e), C_r=2 mg/L",
    "xmin": 0,
    "xmax": 3,
    "xLabel": "Effluent Q_e (m\u00b3/s)",
    "yLabel": "Mix concentration (mg/L)",
    "yUnit": "mg/L",
    "xUnit": "m\u00b3/s",
    "limits": "Complete conservative mixing, fixed river background. Local mixing zones and reactions omitted.",
    "prompt": "Which intervention helps most: cutting effluent flow or improving effluent quality?"
  },
  {
    "number": 4,
    "name": "River Oxygen Sag",
    "id": "oxygen",
    "unit": 2,
    "parameters": [
      {
        "name": "Ultimate BOD L\u2080",
        "unit": "mg/L",
        "min": 2,
        "max": 40,
        "step": 1,
        "default": 18
      },
      {
        "name": "Reaeration k_r",
        "unit": "1/day",
        "min": 0.15,
        "max": 1.3,
        "step": 0.05,
        "default": 0.5
      }
    ],
    "formula": "D=(k_d L\u2080/(k_r\u2212k_d))(e^(\u2212k_d t)\u2212e^(\u2212k_r t))+D\u2080e^(\u2212k_r t)",
    "xmin": 0,
    "xmax": 12,
    "xLabel": "Travel time t (days)",
    "yLabel": "Oxygen deficit D (mg/L)",
    "yUnit": "mg/L",
    "xUnit": "days",
    "limits": "Illustrative Streeter\u2013Phelps equation, k_d=0.24/day, D\u2080=0.5 mg/L; no daylight cycles or multiple sources.",
    "prompt": "Why does an oxygen deficit sometimes peak downstream rather than at the outfall?"
  },
  {
    "number": 5,
    "name": "Clarifier Particle Capture",
    "id": "settling",
    "unit": 3,
    "parameters": [
      {
        "name": "Settling velocity v_s",
        "unit": "m/day",
        "min": 2,
        "max": 70,
        "step": 1,
        "default": 12
      },
      {
        "name": "Flow Q",
        "unit": "m\u00b3/day",
        "min": 1000,
        "max": 10000,
        "step": 250,
        "default": 4000
      }
    ],
    "formula": "Ideal capture=min(1,v_s/(Q/A)); A varies on x-axis",
    "xmin": 40,
    "xmax": 400,
    "xLabel": "Area A (m\u00b2)",
    "yLabel": "Ideal capture (%)",
    "yUnit": "%",
    "xUnit": "m\u00b2",
    "limits": "Ideal discrete-particle Hazen overflow model only; flocculation and hydraulic short circuiting omitted.",
    "prompt": "Would doubling clarifier depth necessarily double ideal removal?"
  },
  {
    "number": 6,
    "name": "Filter Darcy Head Loss",
    "id": "filter",
    "unit": 3,
    "parameters": [
      {
        "name": "Superficial filtration rate",
        "unit": "m/h",
        "min": 1,
        "max": 12,
        "step": 0.25,
        "default": 5
      },
      {
        "name": "Intrinsic permeability k",
        "unit": "\u00d710\u207b\u00b9\u2070 m\u00b2",
        "min": 0.25,
        "max": 5,
        "step": 0.05,
        "default": 2
      }
    ],
    "formula": "h=\u03bcLv/(\u03c1gk), \u03bc=0.001 Pa\u00b7s",
    "xmin": 0.3,
    "xmax": 2.5,
    "xLabel": "Media depth L (m)",
    "yLabel": "Hydraulic head loss h (m)",
    "yUnit": "m",
    "xUnit": "m",
    "limits": "Clean-media Darcy model, uniform permeability; clogging and backwash dynamics omitted.",
    "prompt": "How might increasing media grain size reduce head loss but worsen capture?"
  },
  {
    "number": 7,
    "name": "Disinfectant Residual Decay",
    "id": "disinfect",
    "unit": 3,
    "parameters": [
      {
        "name": "Initial residual C\u2080",
        "unit": "mg/L",
        "min": 0.3,
        "max": 3,
        "step": 0.1,
        "default": 1.5
      },
      {
        "name": "Decay rate k",
        "unit": "1/min",
        "min": 0.002,
        "max": 0.1,
        "step": 0.001,
        "default": 0.025
      }
    ],
    "formula": "C(t)=C\u2080exp(\u2212kt), integrated CT=\u222bCdt",
    "xmin": 0,
    "xmax": 60,
    "xLabel": "Contact time (min)",
    "yLabel": "Residual (mg/L)",
    "yUnit": "mg/L",
    "xUnit": "min",
    "limits": "Chemical residual and integrated concentration, not validated microbial inactivation or regulatory log credit.",
    "prompt": "Compare nominal contact time with short-circuiting in a real contact chamber."
  },
  {
    "number": 8,
    "name": "Activated-Sludge Food / Biomass",
    "id": "fm",
    "unit": 4,
    "parameters": [
      {
        "name": "Influent BOD",
        "unit": "mg/L",
        "min": 60,
        "max": 450,
        "step": 10,
        "default": 220
      },
      {
        "name": "Mixed liquor biomass X",
        "unit": "mg/L",
        "min": 1000,
        "max": 5000,
        "step": 100,
        "default": 2800
      }
    ],
    "formula": "F/M = Q S/(V X), Q=5000 m\u00b3/day, V varies",
    "xmin": 1000,
    "xmax": 7000,
    "xLabel": "Reactor volume (m\u00b3)",
    "yLabel": "F/M (1/day)",
    "yUnit": "1/day",
    "xUnit": "m\u00b3",
    "limits": "Screening F/M using consistent concentration basis, no clarifier losses or biodegradability adjustment.",
    "prompt": "Explain why the same F/M does not imply the same effluent quality at all temperatures."
  },
  {
    "number": 9,
    "name": "Monod Substrate Dependence",
    "id": "monod",
    "unit": 4,
    "parameters": [
      {
        "name": "Maximum growth \u03bc_max",
        "unit": "1/day",
        "min": 0.2,
        "max": 3,
        "step": 0.1,
        "default": 1.1
      },
      {
        "name": "Half-saturation K_s",
        "unit": "mg/L",
        "min": 5,
        "max": 120,
        "step": 5,
        "default": 40
      }
    ],
    "formula": "\u03bc = \u03bc_max S/(K_s+S)",
    "xmin": 0,
    "xmax": 250,
    "xLabel": "Substrate S (mg/L)",
    "yLabel": "Specific growth \u03bc (1/day)",
    "yUnit": "1/day",
    "xUnit": "mg/L",
    "limits": "Single-substrate intrinsic Monod curve; excludes oxygen, inhibition, decay and mixed populations.",
    "prompt": "What substrate concentration reaches half of the specified maximum growth?"
  },
  {
    "number": 10,
    "name": "Nutrient Removal Mass Balance",
    "id": "nutrient",
    "unit": 4,
    "parameters": [
      {
        "name": "Flow Q",
        "unit": "m\u00b3/day",
        "min": 500,
        "max": 15000,
        "step": 250,
        "default": 8000
      },
      {
        "name": "Influent nutrient",
        "unit": "mg/L",
        "min": 1,
        "max": 20,
        "step": 0.5,
        "default": 6
      }
    ],
    "formula": "Removed load=0.001Q(C_in\u2212C_out)",
    "xmin": 0,
    "xmax": 15,
    "xLabel": "Effluent concentration C_out (mg/L)",
    "yLabel": "Net removal / release (kg/day)",
    "yUnit": "kg/day",
    "xUnit": "mg/L",
    "limits": "Simple flow-weighted nutrient mass accounting; captured mass requires responsible handling.",
    "prompt": "How can removal fall below zero in a mass balance and what should an investigator check?"
  },
  {
    "number": 11,
    "name": "Simplified Ground-Level Plume",
    "id": "plume",
    "unit": 5,
    "parameters": [
      {
        "name": "Emission Q",
        "unit": "g/s",
        "min": 0.2,
        "max": 12,
        "step": 0.2,
        "default": 3
      },
      {
        "name": "Wind u",
        "unit": "m/s",
        "min": 0.5,
        "max": 8,
        "step": 0.25,
        "default": 3
      }
    ],
    "formula": "C=Q/(\u03c0u\u03c3_y\u03c3_z)exp(\u2212H\u00b2/(2\u03c3_z\u00b2))",
    "xmin": 100,
    "xmax": 3000,
    "xLabel": "Downwind x (m)",
    "yLabel": "Centerline C (\u00b5g/m\u00b3)",
    "yUnit": "\u00b5g/m\u00b3",
    "xUnit": "m",
    "limits": "Flat terrain, neutral illustrative spreads \u03c3_y=0.12x^0.9, \u03c3_z=0.06x^0.85; H=30 m. Not EPA AERMOD.",
    "prompt": "Why may near-field ground levels be lower than values farther downwind?"
  },
  {
    "number": 12,
    "name": "Particulate Control Mass Removal",
    "id": "capture",
    "unit": 5,
    "parameters": [
      {
        "name": "Inlet concentration",
        "unit": "mg/m\u00b3",
        "min": 10,
        "max": 300,
        "step": 10,
        "default": 150
      },
      {
        "name": "Removal efficiency",
        "unit": "%",
        "min": 50,
        "max": 99.5,
        "step": 0.5,
        "default": 95
      }
    ],
    "formula": "C_out=C_in(1\u2212\u03b7); captured=Q_g(C_in\u2212C_out)",
    "xmin": 500,
    "xmax": 15000,
    "xLabel": "Gas flow (m\u00b3/h)",
    "yLabel": "Captured mass (kg/h)",
    "yUnit": "kg/h",
    "xUnit": "m\u00b3/h",
    "limits": "Equal inlet and outlet gas flow basis; assumes stable particle composition and control uptime.",
    "prompt": "What field measurements distinguish a perfect filter from a leaking bypass?"
  },
  {
    "number": 13,
    "name": "Materials Recovery Yield",
    "id": "recycle",
    "unit": 6,
    "parameters": [
      {
        "name": "Plastic share",
        "unit": "fraction",
        "min": 0.05,
        "max": 0.35,
        "step": 0.01,
        "default": 0.18
      },
      {
        "name": "Capture efficiency",
        "unit": "fraction",
        "min": 0.2,
        "max": 0.95,
        "step": 0.05,
        "default": 0.7
      }
    ],
    "formula": "Recovered = feed \u00d7 share \u00d7 capture \u00d7 processing yield 0.85",
    "xmin": 20,
    "xmax": 200,
    "xLabel": "Waste input (t/day)",
    "yLabel": "Recovered (t/day)",
    "yUnit": "t/day",
    "xUnit": "t/day",
    "limits": "Assumed constant 85% processing yield; market demand and quality constraints omitted.",
    "prompt": "How does contamination change saleable mass despite unchanged collection tonnage?"
  },
  {
    "number": 14,
    "name": "Landfill Methane Generation",
    "id": "landfill",
    "unit": 6,
    "parameters": [
      {
        "name": "Decomposition rate k",
        "unit": "1/year",
        "min": 0.01,
        "max": 0.15,
        "step": 0.005,
        "default": 0.05
      },
      {
        "name": "Gas potential L\u2080",
        "unit": "m\u00b3/t",
        "min": 40,
        "max": 220,
        "step": 5,
        "default": 120
      }
    ],
    "formula": "G(t)=k L\u2080 M exp(\u2212kt), M=100000 t",
    "xmin": 0,
    "xmax": 60,
    "xLabel": "Years after waste placement",
    "yLabel": "Generation (m\u00b3/year)",
    "yUnit": "m\u00b3/year",
    "xUnit": "",
    "limits": "One deposit and single first-order decay coefficient; collection, oxidation and multiyear filling omitted.",
    "prompt": "What changes to peak generation if the same lifetime gas potential is released more slowly?"
  },
  {
    "number": 15,
    "name": "Illustrative Water Exposure Dose",
    "id": "exposure",
    "unit": 7,
    "parameters": [
      {
        "name": "Water contaminant",
        "unit": "mg/L",
        "min": 0.001,
        "max": 0.1,
        "step": 0.001,
        "default": 0.015
      },
      {
        "name": "Body mass",
        "unit": "kg",
        "min": 30,
        "max": 100,
        "step": 1,
        "default": 65
      }
    ],
    "formula": "CDI=C\u00d7IR/BW, IR varies; continuous daily intake",
    "xmin": 0.5,
    "xmax": 4,
    "xLabel": "Water intake IR (L/day)",
    "yLabel": "Daily intake CDI (mg/kg/day)",
    "yUnit": "mg/kg/day",
    "xUnit": "L/day",
    "limits": "Noncancer screening of daily oral exposure only; no contaminant-specific reference dose or toxicity claim.",
    "prompt": "Why does the same concentration produce a different intake per body mass for a child?"
  },
  {
    "number": 16,
    "name": "Operational Electricity Footprint",
    "id": "carbon",
    "unit": 8,
    "parameters": [
      {
        "name": "Energy intensity",
        "unit": "kWh/m\u00b3",
        "min": 0.15,
        "max": 1.5,
        "step": 0.05,
        "default": 0.45
      },
      {
        "name": "Grid emission factor",
        "unit": "kg CO\u2082e/kWh",
        "min": 0.1,
        "max": 1.0,
        "step": 0.05,
        "default": 0.6
      }
    ],
    "formula": "CO\u2082e=Q\u00d7e\u00d7EF",
    "xmin": 1000,
    "xmax": 20000,
    "xLabel": "Water treated Q (m\u00b3/day)",
    "yLabel": "Electricity emissions (kg CO\u2082e/day)",
    "yUnit": "kg CO\u2082e/day",
    "xUnit": "m\u00b3/day",
    "limits": "Only purchased electricity with illustrative factor; no chemical, process, construction or avoided-emission credits.",
    "prompt": "How would a change in grid carbon intensity affect ranking of two designs?"
  }
];

  var MODELS = EE_SPECS.map(function(s, idx) {
    var controlsHtml = s.parameters.map(function(p, pi) {
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ee_' + (idx + 1) + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_ee_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#059669;">' + p.default + '</span></label>' +
             '<input id="ee_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#059669;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#d1fae5;color:#065f46;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + (idx + 1) + ' · Unit ' + s.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + s.name + '</h3>' +
               '<div style="background:#f0fdf4;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#065f46;margin-bottom:0.75rem;">' + (s.formula || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (s.prompt || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#ecfdf5;border-left:4px solid #059669;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#065f46;font-weight:600;text-transform:uppercase;">' + (s.yLabel || 'Result') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#047857;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#064e3b;margin-top:0.25rem;">' + (s.limits || '') + '</div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {
      idx: idx + 1,
      unit: s.unit,
      html: html,
      init: function(card) {
        try {
          var pVals = s.parameters.map(function(p) { return p.default; });
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xmin = s.xmin, xmax = s.xmax;
            var ys = pts.map(function(p) { return p[1]; }).filter(Number.isFinite);
            var lo = Math.min(0, Math.min.apply(null, ys), currY);
            var hi = Math.max.apply(null, ys);
            if (hi <= lo) hi = lo + 1;

            var xp = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var yp = function(y) { return H - B - (y - lo) / (hi - lo || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var i = 0; i <= 4; i++) {
              var v = lo + (hi - lo) * i / 4, yPos = yp(v);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pathPts = pts.map(function(d) { return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }).join(' ');
            node('polyline', { points: pathPts, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, s.xLabel || 'Input');
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_ee_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var midX = (s.xmin + s.xmax) / 2;
            var currY = eeCalc(s.id, midX, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {
              valEl.textContent = Number.isFinite(currY) ? Number(currY.toPrecision(4)) + ' ' + (s.yUnit || '') : '--';
            }

            var pts = [];
            for (var k = 0; k <= 50; k++) {
              var x = s.xmin + (s.xmax - s.xmin) * k / 50;
              var y = eeCalc(s.id, x, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(y)) pts.push([x, y]);
            }
            drawGraph(pts, midX, currY);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('EE sim error on lab ' + (idx + 1), err);
        }
      }
    };
  });

  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) { return m.unit === 1; });
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'ce-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    var autoInit = function() {
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoInit);
    } else {
      autoInit();
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
