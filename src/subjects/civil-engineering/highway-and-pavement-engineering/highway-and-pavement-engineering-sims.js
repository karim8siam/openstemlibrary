/* Highway and Pavement Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  const g = 9.81;

  function formula(id, x, a, b) {
    switch(id) {
      case 'earthworks': return x * (a + b) / 2;
      case 'profile': return (a / 100) * x + ((b - a) / 100) * x * x / (2 * 200);
      case 'ssd': { let v = x / 3.6; return v * a + v * v / (2 * b); }
      case 'radius': return x * x / (127 * (a + b));
      case 'gradation': return x >= a ? 100 : 100 * Math.pow(Math.max(0, x) / a, b);
      case 'binder': return a * Math.exp(-b * (x - 20));
      case 'stress': return a * (1 - Math.pow(1 + Math.pow(b / x, 2), -1.5));
      case 'fatigue': return b * Math.pow(150 / x, a);
      case 'rut': return 1 + a * Math.pow(x, b);
      case 'plate': return (a * 1000 * Math.pow(x, 3)) / (12 * (1 - b * b));
      case 'joint': return a * 1e-3 * b * x;
      case 'compaction': return Math.max(0, b - 0.045 * Math.pow(x - a, 2));
      case 'endarea': return x * (a + b) / 2;
      case 'runoff': return 0.00278 * b * x * a;
      case 'npv': { let s = 0; for (let t = 0; t <= x; t += 7) s += b / Math.pow(1 + a / 100, t); return s; }
      case 'wetbrake': { let v = x / 3.6; return v * b + v * v / (2 * a * g); }
      default: return NaN;
    }
  }

  var HP_LABS = [
  {
    "number": 1,
    "title": "Earthwork Volume Sensitivity",
    "id": "earthworks",
    "unit_number": 1,
    "params": [
      {
        "name": "Section 1 area",
        "unit": "m\u00b2",
        "min": 5,
        "max": 80,
        "step": 1,
        "value": 20
      },
      {
        "name": "Section 2 area",
        "unit": "m\u00b2",
        "min": 5,
        "max": 80,
        "step": 1,
        "value": 35
      }
    ],
    "formula": "Mean end-area: V = L(A\u2081+A\u2082)/2",
    "unit": "m\u00b3",
    "xmin": 0,
    "xmax": 120,
    "xlabel": "Chainage length (m)",
    "limit": "Area changes assume no intermediate curvature and no conversion between in-place and compacted volumes.",
    "task": "Compare two terrain surveys with identical end areas but different middle profiles. Where would the approximation fail?"
  },
  {
    "number": 2,
    "title": "Parabolic Road Profile",
    "id": "profile",
    "unit_number": 2,
    "params": [
      {
        "name": "Initial grade",
        "unit": "%",
        "min": -6,
        "max": 7,
        "step": 0.25,
        "value": 3
      },
      {
        "name": "Final grade",
        "unit": "%",
        "min": -8,
        "max": 5,
        "step": 0.25,
        "value": -2
      }
    ],
    "formula": "y = g\u2081x + (g\u2082\u2212g\u2081)x\u00b2/(2L); L=200 m",
    "unit": "m",
    "xmin": 0,
    "xmax": 200,
    "xlabel": "Chainage x (m)",
    "limit": "The plot is geometry only; it does not prove available stopping sight distance.",
    "task": "Where does grade change sign when g\u2081 and g\u2082 have opposite signs?"
  },
  {
    "number": 3,
    "title": "Stopping Sight Distance",
    "id": "ssd",
    "unit_number": 2,
    "params": [
      {
        "name": "Reaction time",
        "unit": "s",
        "min": 1,
        "max": 3.5,
        "step": 0.1,
        "value": 2.5
      },
      {
        "name": "Deceleration",
        "unit": "m/s\u00b2",
        "min": 2,
        "max": 5,
        "step": 0.1,
        "value": 3.4
      }
    ],
    "formula": "SSD = vt + v\u00b2/(2a)",
    "unit": "m",
    "xmin": 20,
    "xmax": 120,
    "xlabel": "Speed (km/h)",
    "limit": "Level road, constant reaction and deceleration. Sightline restrictions and vehicle limits are omitted.",
    "task": "Why does increasing speed affect braking distance more rapidly than reaction distance?"
  },
  {
    "number": 4,
    "title": "Horizontal Curve Radius",
    "id": "radius",
    "unit_number": 2,
    "params": [
      {
        "name": "Superelevation e",
        "unit": "fraction",
        "min": 0,
        "max": 0.12,
        "step": 0.005,
        "value": 0.06
      },
      {
        "name": "Side-friction f",
        "unit": "fraction",
        "min": 0.05,
        "max": 0.2,
        "step": 0.005,
        "value": 0.12
      }
    ],
    "formula": "R = V\u00b2 / [127(e+f)]",
    "unit": "m",
    "xmin": 30,
    "xmax": 120,
    "xlabel": "Speed (km/h)",
    "limit": "Simplified balance; allowable e and f require local design policies and environmental context.",
    "task": "At the same speed, how sensitive is the radius to friction when banking is small?"
  },
  {
    "number": 5,
    "title": "Aggregate Gradation Curve",
    "id": "gradation",
    "unit_number": 3,
    "params": [
      {
        "name": "Maximum particle size",
        "unit": "mm",
        "min": 10,
        "max": 40,
        "step": 1,
        "value": 25
      },
      {
        "name": "Shape exponent n",
        "unit": "dimensionless",
        "min": 0.3,
        "max": 2.5,
        "step": 0.05,
        "value": 0.9
      }
    ],
    "formula": "Passing(d) = 100(d/Dmax)^n, d \u2264 Dmax",
    "unit": "% passing",
    "xmin": 0,
    "xmax": 40,
    "xlabel": "Sieve aperture (mm)",
    "limit": "A synthetic grading family, not a standard specification envelope or measured sieve dataset.",
    "task": "Does increasing n make the mix coarser or finer at a fixed aperture?"
  },
  {
    "number": 6,
    "title": "Asphalt Modulus vs Temperature",
    "id": "binder",
    "unit_number": 3,
    "params": [
      {
        "name": "Reference modulus",
        "unit": "MPa",
        "min": 1000,
        "max": 8000,
        "step": 250,
        "value": 4000
      },
      {
        "name": "Thermal sensitivity \u03b1",
        "unit": "1/\u00b0C",
        "min": 0.02,
        "max": 0.12,
        "step": 0.005,
        "value": 0.065
      }
    ],
    "formula": "E*(T) = Eref exp[\u2212\u03b1(T\u221220)]",
    "unit": "MPa",
    "xmin": 0,
    "xmax": 60,
    "xlabel": "Temperature (\u00b0C)",
    "limit": "Illustrative curve; real binder and mix data are frequency-, aging- and moisture-dependent.",
    "task": "Compare predicted modulus change between 10\u201320\u00b0C and 40\u201350\u00b0C."
  },
  {
    "number": 7,
    "title": "Wheel Contact Stress With Depth",
    "id": "stress",
    "unit_number": 4,
    "params": [
      {
        "name": "Contact pressure",
        "unit": "kPa",
        "min": 300,
        "max": 1200,
        "step": 25,
        "value": 700
      },
      {
        "name": "Contact radius",
        "unit": "m",
        "min": 0.08,
        "max": 0.25,
        "step": 0.005,
        "value": 0.15
      }
    ],
    "formula": "\u03c3z=q[1\u2212(1+(a/z)\u00b2)^(\u22123/2)]",
    "unit": "kPa",
    "xmin": 0.05,
    "xmax": 1.5,
    "xlabel": "Depth z (m)",
    "limit": "Homogeneous isotropic elastic half-space; not a layered pavement strain solution.",
    "task": "What changes when the contact radius increases while nominal pressure stays constant?"
  },
  {
    "number": 8,
    "title": "Asphalt Fatigue Sensitivity",
    "id": "fatigue",
    "unit_number": 4,
    "params": [
      {
        "name": "Fatigue exponent",
        "unit": "dimensionless",
        "min": 2,
        "max": 7,
        "step": 0.25,
        "value": 4
      },
      {
        "name": "Reference life",
        "unit": "million cycles",
        "min": 0.5,
        "max": 5,
        "step": 0.25,
        "value": 2
      }
    ],
    "formula": "Nf=Nref(150 \u03bc\u03b5/\u03b5)^m",
    "unit": "million cycles",
    "xmin": 100,
    "xmax": 300,
    "xlabel": "Tensile microstrain",
    "limit": "Hypothetical power law; actual fatigue parameters require validated mix and field data.",
    "task": "Why can an apparently small strain increase cause a large life reduction?"
  },
  {
    "number": 9,
    "title": "Rutting Accumulation Model",
    "id": "rut",
    "unit_number": 4,
    "params": [
      {
        "name": "Scale coefficient",
        "unit": "mm",
        "min": 2,
        "max": 15,
        "step": 0.5,
        "value": 7
      },
      {
        "name": "Exponent b",
        "unit": "dimensionless",
        "min": 0.25,
        "max": 1.25,
        "step": 0.05,
        "value": 0.6
      }
    ],
    "formula": "d(N)=1 mm + k(N/10\u2076)^b",
    "unit": "mm",
    "xmin": 0,
    "xmax": 3,
    "xlabel": "Load repetitions (millions)",
    "limit": "Toy aggregate rutting model: no calibrated material-specific prediction.",
    "task": "What does changing exponent do to early-stage versus late-stage rut growth?"
  },
  {
    "number": 10,
    "title": "Concrete Slab Flexural Rigidity",
    "id": "plate",
    "unit_number": 5,
    "params": [
      {
        "name": "Elastic modulus E",
        "unit": "GPa",
        "min": 20,
        "max": 45,
        "step": 1,
        "value": 30
      },
      {
        "name": "Poisson ratio \u03bd",
        "unit": "dimensionless",
        "min": 0.1,
        "max": 0.3,
        "step": 0.01,
        "value": 0.2
      }
    ],
    "formula": "D=Eh\u00b3/[12(1\u2212\u03bd\u00b2)]",
    "unit": "MN\u00b7m",
    "xmin": 0.12,
    "xmax": 0.36,
    "xlabel": "Slab thickness (m)",
    "limit": "Ideal homogeneous elastic thin plate; stiffness alone cannot determine slab thickness.",
    "task": "What makes a small thickness increase more influential than a similar percentage of E?"
  },
  {
    "number": 11,
    "title": "Thermal Joint Movement",
    "id": "joint",
    "unit_number": 5,
    "params": [
      {
        "name": "Expansion coefficient \u03b1",
        "unit": "\u00d710\u207b\u2076/\u00b0C",
        "min": 7,
        "max": 15,
        "step": 0.5,
        "value": 10
      },
      {
        "name": "Joint spacing L",
        "unit": "m",
        "min": 3,
        "max": 7,
        "step": 0.25,
        "value": 5
      }
    ],
    "formula": "\u0394L=\u03b1L\u0394T",
    "unit": "mm",
    "xmin": -30,
    "xmax": 50,
    "xlabel": "Temperature change (\u00b0C)",
    "limit": "Free thermal movement only. Concrete drying shrinkage, restraint and cracking are excluded.",
    "task": "How do large temperature swings change theoretical movement for widely spaced joints?"
  },
  {
    "number": 12,
    "title": "Compaction Moisture\u2013Density",
    "id": "compaction",
    "unit_number": 6,
    "params": [
      {
        "name": "Optimum moisture",
        "unit": "%",
        "min": 6,
        "max": 22,
        "step": 0.5,
        "value": 12
      },
      {
        "name": "Maximum dry density",
        "unit": "kN/m\u00b3",
        "min": 16,
        "max": 22,
        "step": 0.25,
        "value": 19
      }
    ],
    "formula": "\u03b3d=\u03b3max\u22120.045(w\u2212wopt)\u00b2",
    "unit": "kN/m\u00b3",
    "xmin": 4,
    "xmax": 26,
    "xlabel": "Water content w (%)",
    "limit": "An educational parabolic approximation, not measured Proctor test data.",
    "task": "Why can a field wet-density value not be used directly for percent compaction?"
  },
  {
    "number": 13,
    "title": "End-Area Earthwork Quantity",
    "id": "endarea",
    "unit_number": 6,
    "params": [
      {
        "name": "End area A\u2081",
        "unit": "m\u00b2",
        "min": 2,
        "max": 100,
        "step": 1,
        "value": 25
      },
      {
        "name": "End area A\u2082",
        "unit": "m\u00b2",
        "min": 2,
        "max": 100,
        "step": 2,
        "value": 40
      }
    ],
    "formula": "V=L(A\u2081+A\u2082)/2",
    "unit": "m\u00b3",
    "xmin": 0,
    "xmax": 150,
    "xlabel": "Station spacing L (m)",
    "limit": "End-area method; abrupt local geometry, soil conversions and unsuitable material ignored.",
    "task": "At which station spacing does interpolation uncertainty become material?"
  },
  {
    "number": 14,
    "title": "Highway Drainage Runoff",
    "id": "runoff",
    "unit_number": 6,
    "params": [
      {
        "name": "Drainage area",
        "unit": "ha",
        "min": 0.2,
        "max": 10,
        "step": 0.2,
        "value": 2
      },
      {
        "name": "Runoff coefficient",
        "unit": "fraction",
        "min": 0.2,
        "max": 0.95,
        "step": 0.05,
        "value": 0.75
      }
    ],
    "formula": "Q=0.00278CiA",
    "unit": "m\u00b3/s",
    "xmin": 10,
    "xmax": 180,
    "xlabel": "Intensity i (mm/h)",
    "limit": "Rational-method peak approximation; not an inlet or culvert capacity design.",
    "task": "Which parameter uncertainty dominates on a rapidly urbanizing catchment?"
  },
  {
    "number": 15,
    "title": "Discounted Maintenance Costs",
    "id": "npv",
    "unit_number": 7,
    "params": [
      {
        "name": "Discount rate",
        "unit": "%",
        "min": 1,
        "max": 12,
        "step": 0.5,
        "value": 5
      },
      {
        "name": "Treatment cost",
        "unit": "thousand units",
        "min": 30,
        "max": 250,
        "step": 10,
        "value": 100
      }
    ],
    "formula": "PV=C/(1+r)^t; repeat at years 0, 7, 14",
    "unit": "thousand present-value units",
    "xmin": 0,
    "xmax": 25,
    "xlabel": "Analysis year",
    "limit": "Illustrative recurring agency cost schedule, without benefits, end condition or user delay costs.",
    "task": "Compare a lower initial treatment requiring frequent repeats with a longer-lasting alternative."
  },
  {
    "number": 16,
    "title": "Wet-Braking Sensitivity",
    "id": "wetbrake",
    "unit_number": 8,
    "params": [
      {
        "name": "Tire\u2013road friction \u03bc",
        "unit": "fraction",
        "min": 0.15,
        "max": 0.8,
        "step": 0.025,
        "value": 0.4
      },
      {
        "name": "Reaction time",
        "unit": "s",
        "min": 1,
        "max": 3.5,
        "step": 0.1,
        "value": 2.5
      }
    ],
    "formula": "SSD=vt+v\u00b2/(2\u03bcg)",
    "unit": "m",
    "xmin": 30,
    "xmax": 120,
    "xlabel": "Speed (km/h)",
    "limit": "Ideal friction-limited comparison; not a replacement for adopted deceleration criteria.",
    "task": "How could polished wet pavement amplify the risk of modest speed increases?"
  }
];

  var MODELS = HP_LABS.map(function(spec, idx) {
    var unitNum = spec.unit_number || spec.unit || ((idx >> 1) + 1);
    var controlsHtml = spec.params.map(function(p, pi) {
      var defVal = p.value !== undefined ? p.value : (p.default !== undefined ? p.default : p.min);
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="hp_' + (idx + 1) + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_hp_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#ea580c;">' + defVal + '</span></label>' +
             '<input id="hp_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + defVal + '" style="width:100%;accent-color:#ea580c;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#ffedd5;color:#c2410c;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + (idx + 1) + ' · Unit ' + unitNum + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.title + '</h3>' +
               '<div style="background:#fff7ed;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#c2410c;margin-bottom:0.75rem;">' + (spec.formula || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (spec.task || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#fff7ed;border-left:4px solid #ea580c;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#9a3412;font-weight:600;text-transform:uppercase;">' + (spec.xlabel || 'Calculated Metric') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#c2410c;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#7c2d12;margin-top:0.25rem;">' + (spec.limit || '') + '</div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {
      idx: idx + 1,
      unit: unitNum,
      html: html,
      init: function(card) {
        try {
          var pVals = spec.params.map(function(p) { return p.value !== undefined ? p.value : (p.default !== undefined ? p.default : p.min); });
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) { return p[0]; });
            var ys = pts.map(function(p) { return p[1]; }).filter(Number.isFinite);
            var xmin = spec.xmin !== undefined ? spec.xmin : Math.min.apply(null, xs);
            var xmax = spec.xmax !== undefined ? spec.xmax : Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var yp = function(y) { return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var i = 0; i <= 4; i++) {
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pathPts = pts.map(function(d) { return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }).join(' ');
            node('polyline', { points: pathPts, fill: 'none', stroke: '#ea580c', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, spec.xlabel || 'Input');
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_hp_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var xmin = spec.xmin !== undefined ? spec.xmin : 0;
            var xmax = spec.xmax !== undefined ? spec.xmax : 100;
            var midX = (xmin + xmax) / 2;
            var curVal = formula(spec.id, midX, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {
              valEl.textContent = Number.isFinite(curVal) ? Number(curVal.toPrecision(4)) + ' ' + (spec.unit || '') : '--';
            }

            var pts = [];
            for (var k = 0; k <= 50; k++) {
              var xV = xmin + (xmax - xmin) * k / 50;
              var yV = formula(spec.id, xV, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(yV)) pts.push([xV, yV]);
            }
            drawGraph(pts, midX, curVal);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('HP sim error on lab ' + (idx + 1), err);
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
