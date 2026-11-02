/* Hydrology Interactive Simulation Suite */
(function(window) {
  'use strict';

  const gamma = 0.5772156649015329;
  const G = 9.81;
  const HYDRO_MODELS ={
 balance:p=>[p[0]-p[1]-p[2],'Closure residual; unmeasured fluxes can bias this result.'],
 thiessen:p=>[p[3]*p[0]+p[4]*p[1]+(1-p[3]-p[4])*p[2],'Area weights sum to one; verify map representation.'],
 idf:p=>[p[1]/Math.pow(p[0]+p[2],p[3]),'Synthetic IDF only; never treat these parameters as official design rainfall.'],
 storm:p=>[p[0]+Math.max(0,p[2]-1)*p[1],'One peak hour plus remaining hours at background intensity.'],
 et0:p=>[0.0023*(p[0]+17.8)*Math.sqrt(p[1])*p[2],'Reference ET is not necessarily actual landscape water use.'],
 greenampt:p=>{let [t,K,psi,d]=p,A=psi*d;let lo=0,hi=Math.max(1,K*t+A*15);for(let k=0;k<100;k++){let mid=(lo+hi)/2;let f=mid-K*t-A*Math.log1p(mid/A);if(f>0)hi=mid;else lo=mid;}return [(lo+hi)/2,'Continuous ponding and a homogeneous sharp wetting front assumed.'];},
 curve:p=>{let [P,CN,lam]=p,S=25400/CN-254,Ia=lam*S;return [P<=Ia?0:Math.pow(P-Ia,2)/(P-Ia+S),'Empirical event depth; lambda is a selectable assumption.'];},
 rational:p=>[0.278*p[0]*p[1]*p[2],'Peak-only screening equation; valid intensity duration is not established here.'],
 triangle:p=>[2*p[0]*1000*p[1]/(p[2]*3600),'Triangular shape conserves volume when integrated across base duration.'],
 linear:p=>[p[0]+(p[1]-p[0])*Math.exp(-p[2]/p[3]),'Constant inflow linear storage approximation.'],
 muskingum:p=>{let [K,X,dt]=p,den=2*K*(1-X)+dt,C0=(dt-2*K*X)/den,C1=(dt+2*K*X)/den,C2=(2*K*(1-X)-dt)/den;return [C0,'C1='+C1.toFixed(3)+', C2='+C2.toFixed(3)+', sum='+(C0+C1+C2).toFixed(3)+(Math.min(C0,C1,C2)<-1e-9?' [WARNING: negative coefficient]':'')];},
 reservoir:p=>[p[0]+(p[1]-p[2])*p[3]*3.6,'Negative storage implies infeasible releases under this simple model.'],
 gumbel:p=>{let [mean,sd,T]=p,y=-Math.log(-Math.log(1-1/T));return [mean+Math.sqrt(6)/Math.PI*sd*(y-gamma),'Statistical illustration, not an approved frequency analysis.'];},
 baseflow:p=>[p[0]*Math.exp(-p[1]/p[2]),'Recession assumes no active recharge.'],
 detention:p=>[Math.max(0,(p[2]*p[1]*p[0]/360-p[3])*p[4]*3600),'This is a constant-intensity volume screen, not routed storage design.'],
 nse:p=>{let obs=[10,25,40,20],sim=[12,23,36,22].map(x=>x*p[0]+p[1]),mu=obs.reduce((a,b)=>a+b)/4,SST=obs.reduce((a,b)=>a+(b-mu)**2,0),SSE=obs.reduce((a,b,i)=>a+(b-sim[i])**2,0);return [1-SSE/SST,'Synthetic four-point series; NSE alone misses operational failure modes.'];}
};

  var HYDRO_SPECS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Annual catchment water balance",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "balance",
    "controls": [
      [
        "Precipitation",
        "mm/y",
        1250,
        500,
        2500,
        25
      ],
      [
        "Evapotranspiration",
        "mm/y",
        680,
        200,
        1500,
        20
      ],
      [
        "Runoff",
        "mm/y",
        360,
        20,
        1500,
        20
      ]
    ],
    "output": "Storage-change residual",
    "unitLabel": "mm/y"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Thiessen weighted basin rainfall",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "thiessen",
    "controls": [
      [
        "Gauge 1",
        "mm",
        78,
        0,
        200,
        2
      ],
      [
        "Gauge 2",
        "mm",
        105,
        0,
        200,
        1
      ],
      [
        "Gauge 3",
        "mm",
        54,
        0,
        200,
        2
      ],
      [
        "Gauge 1 weight",
        "fraction",
        0.35,
        0.1,
        0.6,
        0.01
      ],
      [
        "Gauge 2 weight",
        "fraction",
        0.3,
        0.1,
        0.35,
        0.01
      ]
    ],
    "output": "Area-weighted storm rainfall",
    "unitLabel": "mm"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Synthetic intensity\u2013duration relationship",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "idf",
    "controls": [
      [
        "Duration",
        "minutes",
        30,
        5,
        360,
        5
      ],
      [
        "Empirical coefficient a",
        "model units",
        380,
        120,
        850,
        10
      ],
      [
        "Offset b",
        "minutes",
        12,
        3,
        60,
        1
      ],
      [
        "Exponent n",
        "fraction",
        0.75,
        0.35,
        1.1,
        0.05
      ]
    ],
    "output": "Synthetic rainfall intensity",
    "unitLabel": "mm/h"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Storm depth from changing intensity",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "storm",
    "controls": [
      [
        "Peak 1-hour intensity",
        "mm/h",
        50,
        10,
        150,
        5
      ],
      [
        "Background intensity",
        "mm/h",
        8,
        0,
        30,
        1
      ],
      [
        "Storm duration",
        "hours",
        5,
        1,
        18,
        1
      ]
    ],
    "output": "Total storm depth",
    "unitLabel": "mm"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Reference ET temperature method",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "et0",
    "controls": [
      [
        "Mean temperature",
        "\u00b0C",
        26,
        5,
        40,
        1
      ],
      [
        "Daily Tmax\u2212Tmin",
        "\u00b0C",
        11,
        2,
        22,
        1
      ],
      [
        "Extraterrestrial radiation",
        "mm/day equivalent",
        15,
        5,
        23,
        0.5
      ]
    ],
    "output": "Reference ET (Hargreaves)",
    "unitLabel": "mm/day"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Green\u2013Ampt cumulative infiltration",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "greenampt",
    "controls": [
      [
        "Time since ponding",
        "hours",
        3,
        0.25,
        12,
        0.25
      ],
      [
        "Saturated hydraulic conductivity",
        "mm/hour",
        14,
        2,
        80,
        1
      ],
      [
        "Suction head",
        "mm",
        100,
        20,
        250,
        5
      ],
      [
        "Moisture deficit",
        "fraction",
        0.25,
        0.08,
        0.5,
        0.01
      ]
    ],
    "output": "Cumulative ponded infiltration",
    "unitLabel": "mm"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "NRCS curve-number event excess",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "curve",
    "controls": [
      [
        "Event rainfall",
        "mm",
        90,
        5,
        260,
        5
      ],
      [
        "Curve number",
        "0\u2013100",
        78,
        45,
        98,
        1
      ],
      [
        "Initial-abstraction ratio",
        "fraction",
        0.2,
        0.05,
        0.3,
        0.01
      ]
    ],
    "output": "Excess rainfall depth",
    "unitLabel": "mm"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Rational-method design peak",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "rational",
    "controls": [
      [
        "Runoff coefficient",
        "fraction",
        0.68,
        0.15,
        0.95,
        0.01
      ],
      [
        "Design intensity",
        "mm/h",
        70,
        10,
        180,
        5
      ],
      [
        "Catchment area",
        "km\u00b2",
        0.45,
        0.05,
        3,
        0.05
      ]
    ],
    "output": "Estimated peak discharge",
    "unitLabel": "m\u00b3/s"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Triangular direct-runoff hydrograph",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "triangle",
    "controls": [
      [
        "Basin area",
        "km\u00b2",
        8,
        1,
        50,
        1
      ],
      [
        "Excess rainfall",
        "mm",
        15,
        2,
        70,
        1
      ],
      [
        "Triangle base duration",
        "hours",
        9,
        2,
        30,
        1
      ]
    ],
    "output": "Triangular hydrograph peak",
    "unitLabel": "m\u00b3/s"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Linear reservoir routing",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "linear",
    "controls": [
      [
        "Constant inflow",
        "m\u00b3/s",
        55,
        0,
        150,
        5
      ],
      [
        "Initial outflow",
        "m\u00b3/s",
        12,
        0,
        110,
        2
      ],
      [
        "Time",
        "hours",
        4,
        0,
        24,
        0.5
      ],
      [
        "Storage timescale",
        "hours",
        6,
        0.5,
        20,
        0.5
      ]
    ],
    "output": "Routed outflow",
    "unitLabel": "m\u00b3/s"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Muskingum routing coefficient",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "muskingum",
    "controls": [
      [
        "Storage travel parameter K",
        "hours",
        3,
        1,
        10,
        0.5
      ],
      [
        "Weight X",
        "fraction",
        0.2,
        0,
        0.45,
        0.05
      ],
      [
        "Time step",
        "hours",
        2,
        0.25,
        10,
        0.25
      ]
    ],
    "output": "C0 inflow weight",
    "unitLabel": "dimensionless"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Reservoir storage balance",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "reservoir",
    "controls": [
      [
        "Initial active storage",
        "thousand m\u00b3",
        300,
        0,
        2000,
        50
      ],
      [
        "Inflow",
        "m\u00b3/s",
        35,
        0,
        110,
        5
      ],
      [
        "Release",
        "m\u00b3/s",
        22,
        0,
        90,
        2
      ],
      [
        "Duration",
        "hours",
        6,
        0.5,
        24,
        0.5
      ]
    ],
    "output": "Ending storage",
    "unitLabel": "thousand m\u00b3"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Gumbel annual-maximum quantile",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "gumbel",
    "controls": [
      [
        "Mean annual maximum",
        "m\u00b3/s",
        340,
        60,
        1000,
        10
      ],
      [
        "Sample standard deviation",
        "m\u00b3/s",
        85,
        20,
        270,
        5
      ],
      [
        "Return period",
        "years",
        50,
        2,
        200,
        1
      ]
    ],
    "output": "Method-of-moments quantile",
    "unitLabel": "m\u00b3/s"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Baseflow recession hydrograph",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "baseflow",
    "controls": [
      [
        "Initial dry-weather flow",
        "m\u00b3/s",
        18,
        1,
        100,
        1
      ],
      [
        "Elapsed time",
        "days",
        8,
        0,
        45,
        1
      ],
      [
        "Recession timescale",
        "days",
        20,
        2,
        65,
        1
      ]
    ],
    "output": "Estimated baseflow",
    "unitLabel": "m\u00b3/s"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Urban stormwater detention screen",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "detention",
    "controls": [
      [
        "Urban basin area",
        "hectares",
        18,
        1,
        80,
        1
      ],
      [
        "Storm intensity",
        "mm/h",
        50,
        5,
        140,
        5
      ],
      [
        "Runoff coefficient",
        "fraction",
        0.7,
        0.2,
        0.95,
        0.05
      ],
      [
        "Allowable outflow",
        "m\u00b3/s",
        1.3,
        0,
        6,
        0.1
      ],
      [
        "Duration",
        "hours",
        2,
        0.5,
        8,
        0.5
      ]
    ],
    "output": "Idealized storage required",
    "unitLabel": "m\u00b3"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Nash\u2013Sutcliffe skill sensitivity",
    "desc": "Change the parameters and test a specific hydrological hypothesis.",
    "kind": "nse",
    "controls": [
      [
        "Multiplicative prediction factor",
        "\u2013",
        0.9,
        0.4,
        1.6,
        0.05
      ],
      [
        "Additive prediction bias",
        "m\u00b3/s",
        2,
        -15,
        15,
        1
      ]
    ],
    "output": "Illustrative NSE",
    "unitLabel": "dimensionless"
  }
];

  var MODELS = HYDRO_SPECS.map(function(spec) {
    var controlsHtml = spec.controls.map(function(c, ci) {
      var name = c[0], unit = c[1], def = c[2], min = c[3], max = c[4], step = c[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="h_' + spec.idx + '_' + ci + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_h_' + spec.idx + '_' + ci + '" style="font-weight:700;color:#0d9488;">' + def + '</span></label>' +
             '<input id="h_' + spec.idx + '_' + ci + '" data-cidx="' + ci + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#0d9488;"></div>';
    }).join('');

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

    return {
      idx: spec.idx,
      unit: spec.unit,
      html: html,
      init: function(card) {
        try {
          var p = spec.controls.map(function(c) { return c[2]; });
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(samples, currP) {
            if (!svgEl || !samples.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var ymin = Math.min(0, Math.min.apply(null, samples.map(function(d) { return d[1]; })));
            var ymax = Math.max.apply(null, samples.map(function(d) { return d[1]; }));
            if (ymax <= ymin) ymax = ymin + 1;
            var xmin = samples[0][0], xmax = samples[samples.length - 1][0];
            var xx = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var yy = function(y) { return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var k = 0; k <= 4; k++) {
              var v = ymin + k * (ymax - ymin) / 4, yPos = yy(v);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pts = samples.map(function(d) { return xx(d[0]) + ',' + yy(d[1]); }).join(' ');
            node('polyline', { points: pts, fill: 'none', stroke: '#0d9488', 'stroke-width': '2.5' });

            var currRes = HYDRO_MODELS[spec.kind](currP);
            var currY = currRes[0];
            if (Number.isFinite(currY)) {
              node('circle', { cx: xx(currP[0]), cy: yy(currY), r: 6, fill: '#f97316', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, spec.controls[0][0] + ' (' + spec.controls[0][1] + ')');
            node('text', { x: L, y: H - B + 18, fill: '#64748b', 'font-size': '10' }, Number(xmin.toPrecision(3)).toString());
            node('text', { x: W - R, y: H - B + 18, 'text-anchor': 'end', fill: '#64748b', 'font-size': '10' }, Number(xmax.toPrecision(3)).toString());
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var ci = parseInt(inp.dataset.cidx, 10);
              p[ci] = Number(inp.value);
              var vLbl = card.querySelector('#v_h_' + spec.idx + '_' + ci);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var res = HYDRO_MODELS[spec.kind](p);
            var val = res[0], note = res[1];
            if (valEl) {
              valEl.textContent = Number.isFinite(val) ? Number(val.toPrecision(5)) + ' ' + spec.unitLabel : 'Out of range';
            }
            if (interpEl) interpEl.textContent = note;

            // Generate sensitivity points
            var s = spec.controls[0], samples = [];
            for (var k = 0; k <= 60; k++) {
              var x = s[3] + (s[4] - s[3]) * k / 60;
              var t = p.slice();
              t[0] = x;
              var y = HYDRO_MODELS[spec.kind](t)[0];
              if (Number.isFinite(y)) samples.push([x, y]);
            }
            drawGraph(samples, p);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('Hydrology sim error on lab ' + spec.idx, err);
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
