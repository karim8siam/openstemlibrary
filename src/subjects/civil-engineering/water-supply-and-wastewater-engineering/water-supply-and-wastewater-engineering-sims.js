/* Water Supply and Wastewater Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  const pi = Math.PI, g = 9.81;

  function solve(kind, p) {
    
 let x=p[0],y=0,info='',more={};
 switch(kind){
 case 'demand':{let av=x*p[1]/86400,peak=av*p[2];y=peak; info=`Mean: ${av.toFixed(2)} L/s; daily domestic volume: ${(av*86.4).toFixed(1)} m³/day`; break;}
 case 'source':{y=x-p[1]-p[2]; info=`Available for users: ${(x-p[1]).toFixed(2)} ML/day; demand: ${p[2].toFixed(2)} ML/day`;break;}
 case 'tank':{y=Math.max(0,x-p[1])*p[2]*3.6; info=`Net withdrawal: ${(x-p[1]).toFixed(2)} L/s; duration: ${p[2].toFixed(1)} h`;break;}
 case 'pipe':{let q=x/1000,D=p[1],L=p[2],f=p[3],v=4*q/(pi*D*D);y=f*(L/D)*v*v/(2*g);info=`Velocity ${v.toFixed(3)} m/s; Reynolds and roughness not solved`;break;}
 case 'pump':{let hs=x,h0=p[1],a=p[2],k=p[3];y=hs>=h0?0:Math.sqrt((h0-hs)/(a+k));let head=hs+k*y*y;info=`Operating head: ${head.toFixed(2)} m; pump H=H₀−aQ²; system H=Hstatic+kQ²`;break;}
 case 'chlorine':{y=p[1]*Math.exp(-p[2]*x);info=`Removed by assumed bulk reaction: ${(p[1]-y).toFixed(3)} mg/L`;break;}
 case 'mix':{let G=Math.sqrt(x/(p[2]*p[1]));y=G;info=`G×t = ${(G*p[3]*60).toFixed(0)} (dimensionless), time ${p[3]} min`;break;}
 case 'settling':{let sor=x/p[1];y=Math.min(1,p[2]/sor)*100;info=`Surface overflow rate: ${sor.toFixed(2)} m/day`;break;}
 case 'filter':{let q=x/3600,vel=q/p[1],k=p[3]*1e-9,mu=.001,rho=1000;y=mu*p[2]*vel/(rho*g*k);info=`Superficial velocity ${(vel*3600).toFixed(2)} m/h; clean-bed idealization`;break;}
 case 'ct':{let eff=p[1]*p[2];y=x*eff;info=`Effective contact time: ${eff.toFixed(1)} min`;break;}
 case 'sewer':{let A=pi*x*x/4,R=x/4;y=1000/p[1]*A*Math.pow(R,2/3)*Math.sqrt(p[2]);info=`Full-flow area ${A.toFixed(3)} m²; hydraulic radius ${R.toFixed(3)} m`;break;}
 case 'runoff':{y=2.7777777778*x*p[1]*p[2];info=`Rational method: Q(L/s)=2.778 C i(mm/h) A(ha)`;break;}
 case 'bod':{y=p[1]*(1-Math.exp(-p[2]*x));info=`Remaining ultimate demand: ${(p[1]-y).toFixed(2)} mg/L`;break;}
 case 'fm':{y=(x*p[1])/(p[2]*p[3]);info=`Incoming BOD: ${(x*p[1]/1000).toFixed(1)} kg/day; tank solids inventory ${(p[2]*p[3]/1000).toFixed(1)} kg`;break;}
 case 'clarifier':{y=x/p[1];info=`Daily flow ${x.toFixed(0)} m³/day; surface area ${p[1]} m²`;break;}
 case 'sludge':{let gross=x*p[1]/1000*p[2],decay=p[3]*p[4];y=gross-decay;info=`Gross biomass synthesis ${gross.toFixed(1)} kg/day; endogenous loss ${decay.toFixed(1)} kg/day`;break;}
 default:throw new Error('unknown simulation '+kind);
 }
 return {y,info};
  }

  var WSW_MODELS = [
  {
    "title": "Demand and peak factors",
    "kind": "demand",
    "unit": 1,
    "question": "Population and per-capita use",
    "xLabel": "People",
    "yLabel": "Avg and peak demand (L/s)",
    "params": [
      [
        "Population",
        "people",
        5000,
        150000,
        30000,
        1000
      ],
      [
        "Use",
        "L/person/day",
        60,
        300,
        135,
        5
      ],
      [
        "Peak factor",
        "\u00d7",
        1,
        3.5,
        2.2,
        0.1
      ]
    ],
    "note": "The peak factor scales the mean domestic demand; do not confuse peak hour with maximum daily volume.",
    "yUnit": "L/s"
  },
  {
    "title": "Seasonal source shortfall",
    "kind": "source",
    "unit": 1,
    "question": "Reliable supply margin",
    "xLabel": "Available yield (ML/day)",
    "yLabel": "Daily margin (ML/day)",
    "params": [
      [
        "Source yield",
        "ML/day",
        1,
        30,
        8,
        0.5
      ],
      [
        "Mandatory reserve",
        "ML/day",
        0,
        10,
        1,
        0.5
      ],
      [
        "Demand",
        "ML/day",
        1,
        25,
        9,
        0.5
      ]
    ],
    "note": "Subtract non-abstractable flow and planned demand; a negative balance flags deficit rather than proving a source is unusable.",
    "yUnit": "ML/day"
  },
  {
    "title": "Water tank deficit",
    "kind": "tank",
    "unit": 2,
    "question": "Temporary supply imbalance",
    "xLabel": "Deficit flow (L/s)",
    "yLabel": "Required deficit volume (m\u00b3)",
    "params": [
      [
        "Demand",
        "L/s",
        10,
        200,
        65,
        5
      ],
      [
        "Inflow",
        "L/s",
        0,
        150,
        40,
        5
      ],
      [
        "Deficit duration",
        "h",
        1,
        24,
        8,
        1
      ]
    ],
    "note": "A one-interval storage deficit is not a full tank-sizing calculation.",
    "yUnit": "m\u00b3"
  },
  {
    "title": "Darcy\u2013Weisbach pipe headloss",
    "kind": "pipe",
    "unit": 2,
    "question": "Friction and diameter sensitivity",
    "xLabel": "Pipe flow (L/s)",
    "yLabel": "Headloss (m)",
    "params": [
      [
        "Flow",
        "L/s",
        5,
        80,
        25,
        1
      ],
      [
        "Diameter",
        "m",
        0.08,
        0.5,
        0.15,
        0.01
      ],
      [
        "Length",
        "m",
        50,
        1500,
        200,
        25
      ],
      [
        "Friction factor",
        "\u2014",
        0.012,
        0.06,
        0.025,
        0.001
      ]
    ],
    "note": "Use a prescribed f only for an illustration; realistic friction varies with Reynolds number and relative roughness.",
    "yUnit": "m"
  },
  {
    "title": "Pump\u2013system operating point",
    "kind": "pump",
    "unit": 2,
    "question": "Intersection of quadratic curves",
    "xLabel": "Static lift (m)",
    "yLabel": "Operating flow (L/s)",
    "params": [
      [
        "Static lift",
        "m",
        0,
        35,
        12,
        1
      ],
      [
        "Shutoff pump head",
        "m",
        20,
        70,
        48,
        1
      ],
      [
        "Pump coefficient",
        "m/(L/s)\u00b2",
        0.001,
        0.02,
        0.006,
        0.001
      ],
      [
        "System coefficient",
        "m/(L/s)\u00b2",
        0.001,
        0.02,
        0.003,
        0.001
      ]
    ],
    "note": "A head intersection excludes pump efficiency, NPSH and speed limits.",
    "yUnit": "L/s"
  },
  {
    "title": "Bulk disinfectant decay",
    "kind": "chlorine",
    "unit": 4,
    "question": "First-order residual decay",
    "xLabel": "Time (h)",
    "yLabel": "Residual (mg/L)",
    "params": [
      [
        "Water age",
        "h",
        0,
        48,
        8,
        1
      ],
      [
        "Initial residual",
        "mg/L",
        0.2,
        3,
        1.2,
        0.1
      ],
      [
        "Rate constant",
        "1/h",
        0.01,
        0.3,
        0.06,
        0.01
      ]
    ],
    "note": "Residual alone cannot establish microbiological safety or regulatory compliance.",
    "yUnit": "mg/L"
  },
  {
    "title": "Rapid mixing intensity",
    "kind": "mix",
    "unit": 3,
    "question": "Mixing velocity gradient",
    "xLabel": "Dissipated power (W)",
    "yLabel": "Velocity gradient G (1/s)",
    "params": [
      [
        "Power",
        "W",
        50,
        3000,
        500,
        25
      ],
      [
        "Basin volume",
        "m\u00b3",
        50,
        1000,
        200,
        25
      ],
      [
        "Dynamic viscosity",
        "Pa\u00b7s",
        0.0007,
        0.0015,
        0.001,
        0.0001
      ],
      [
        "Retention",
        "min",
        5,
        50,
        20,
        1
      ]
    ],
    "note": "G and GT are design descriptors, not evidence of sufficient particle destabilization.",
    "yUnit": "1/s"
  },
  {
    "title": "Ideal settling capture",
    "kind": "settling",
    "unit": 3,
    "question": "Surface overflow and fall speed",
    "xLabel": "Flow (m\u00b3/day)",
    "yLabel": "Ideal particle capture (%)",
    "params": [
      [
        "Flow",
        "m\u00b3/day",
        1000,
        15000,
        5000,
        250
      ],
      [
        "Plan area",
        "m\u00b2",
        50,
        800,
        250,
        25
      ],
      [
        "Settling speed",
        "m/day",
        1,
        60,
        15,
        1
      ]
    ],
    "note": "This ideal Type I capture model ignores flocculation, turbulence and density currents.",
    "yUnit": "%"
  },
  {
    "title": "Porous-media clean-bed headloss",
    "kind": "filter",
    "unit": 3,
    "question": "Clean-bed Darcy resistance",
    "xLabel": "Flow (m\u00b3/h)",
    "yLabel": "Headloss (m)",
    "params": [
      [
        "Flow",
        "m\u00b3/h",
        10,
        400,
        100,
        10
      ],
      [
        "Filter area",
        "m\u00b2",
        10,
        100,
        30,
        5
      ],
      [
        "Media depth",
        "m",
        0.5,
        2,
        1,
        0.1
      ],
      [
        "Permeability",
        "m\u00b2 \u00d710\u207b\u2079",
        0.3,
        5,
        1,
        0.1
      ]
    ],
    "note": "Porous permeability is constant here and does not represent fouling or breakthrough.",
    "yUnit": "m"
  },
  {
    "title": "Disinfection CT illustration",
    "kind": "ct",
    "unit": 4,
    "question": "Residual \u00d7 effective contact",
    "xLabel": "Residual (mg/L)",
    "yLabel": "Nominal CT (mg\u00b7min/L)",
    "params": [
      [
        "Residual",
        "mg/L",
        0.1,
        3,
        0.8,
        0.1
      ],
      [
        "Nominal residence",
        "min",
        5,
        120,
        50,
        5
      ],
      [
        "Baffling factor",
        "\u2014",
        0.1,
        1,
        0.5,
        0.05
      ]
    ],
    "note": "A CT calculation is not a log-inactivation claim without relevant validation and water chemistry.",
    "yUnit": "mg\u00b7min/L"
  },
  {
    "title": "Gravity sewer full-pipe Manning",
    "kind": "sewer",
    "unit": 5,
    "question": "Uniform flow and pipe slope",
    "xLabel": "Diameter (m)",
    "yLabel": "Full-flow capacity (L/s)",
    "params": [
      [
        "Diameter",
        "m",
        0.15,
        1.2,
        0.4,
        0.01
      ],
      [
        "Manning n",
        "\u2014",
        0.01,
        0.025,
        0.013,
        0.001
      ],
      [
        "Slope",
        "m/m",
        0.0005,
        0.03,
        0.004,
        0.0005
      ]
    ],
    "note": "Full circular pipe flow is a reference capacity; partial flow or surcharging needs a different computation.",
    "yUnit": "L/s"
  },
  {
    "title": "Wet-weather runoff screening",
    "kind": "runoff",
    "unit": 5,
    "question": "Rational runoff approximation",
    "xLabel": "Rain intensity (mm/h)",
    "yLabel": "Runoff (L/s)",
    "params": [
      [
        "Rain intensity",
        "mm/h",
        5,
        100,
        25,
        5
      ],
      [
        "Runoff coefficient",
        "\u2014",
        0.15,
        0.95,
        0.7,
        0.05
      ],
      [
        "Impervious catchment",
        "ha",
        1,
        25,
        6,
        1
      ]
    ],
    "note": "Rain-derived inflow is not groundwater infiltration. Time of concentration and drainage connection matter.",
    "yUnit": "L/s"
  },
  {
    "title": "Biochemical demand kinetics",
    "kind": "bod",
    "unit": 6,
    "question": "First-order exerted oxygen demand",
    "xLabel": "Time (days)",
    "yLabel": "BOD exerted (mg/L)",
    "params": [
      [
        "Time",
        "days",
        0,
        15,
        5,
        0.5
      ],
      [
        "Ultimate demand",
        "mg/L",
        50,
        500,
        250,
        25
      ],
      [
        "Kinetic constant",
        "1/day",
        0.05,
        0.6,
        0.23,
        0.01
      ]
    ],
    "note": "Fitted rate constants vary; this model is not a laboratory BOD5 result.",
    "yUnit": "mg/L"
  },
  {
    "title": "Activated sludge F/M",
    "kind": "fm",
    "unit": 6,
    "question": "Substrate load per biomass inventory",
    "xLabel": "Influent flow (m\u00b3/day)",
    "yLabel": "F/M (1/day)",
    "params": [
      [
        "Influent flow",
        "m\u00b3/day",
        1000,
        20000,
        8000,
        500
      ],
      [
        "BOD concentration",
        "mg/L",
        80,
        600,
        250,
        10
      ],
      [
        "Tank volume",
        "m\u00b3",
        500,
        7000,
        2500,
        100
      ],
      [
        "MLSS",
        "mg/L",
        1000,
        6000,
        3000,
        200
      ]
    ],
    "note": "MLSS substitutes for actual active biomass; temperature and kinetics are not modeled.",
    "yUnit": "1/day"
  },
  {
    "title": "Secondary clarifier overflow rate",
    "kind": "clarifier",
    "unit": 7,
    "question": "Hydraulic surface loading",
    "xLabel": "Flow (m\u00b3/day)",
    "yLabel": "Overflow rate (m/day)",
    "params": [
      [
        "Influent flow",
        "m\u00b3/day",
        1000,
        30000,
        10000,
        500
      ],
      [
        "Surface area",
        "m\u00b2",
        100,
        2000,
        500,
        50
      ]
    ],
    "note": "Surface overflow rate is only one constraint; solids flux and settleability also matter.",
    "yUnit": "m/day"
  },
  {
    "title": "Net biological solids generation",
    "kind": "sludge",
    "unit": 7,
    "question": "Growth minus endogenous decay",
    "xLabel": "Influent flow (m\u00b3/day)",
    "yLabel": "Net solids generation (kg/day)",
    "params": [
      [
        "Influent flow",
        "m\u00b3/day",
        1000,
        15000,
        6000,
        250
      ],
      [
        "Removed substrate",
        "mg/L",
        50,
        450,
        180,
        10
      ],
      [
        "Yield coefficient",
        "kg/kg",
        0.2,
        0.85,
        0.5,
        0.05
      ],
      [
        "Biomass inventory",
        "kg",
        500,
        12000,
        2500,
        100
      ],
      [
        "Decay coefficient",
        "1/day",
        0.01,
        0.16,
        0.06,
        0.01
      ]
    ],
    "note": "This only estimates net biological solids growth, not total sludge for disposal.",
    "yUnit": "kg/day"
  }
];

  var MODELS = WSW_MODELS.map(function(mDef, idx) {
    var controlsHtml = mDef.params.map(function(p, pi) {
      var name = p[0], unit = p[1], min = p[2], max = p[3], def = p[4], step = p[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="wsw_' + (idx + 1) + '_' + pi + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_wsw_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#059669;">' + def + '</span></label>' +
             '<input id="wsw_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#059669;"></div>';
    }).join('');

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

    return {
      idx: idx + 1,
      unit: mDef.unit,
      html: html,
      init: function(card) {
        try {
          var pVals = mDef.params.map(function(p) { return p[4]; });
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(xData, yData, currX, currY) {
            if (!svgEl || !xData.length) return;
            svgEl.innerHTML = '';
            var W = 730, H = 310, left = 64, right = 22, top = 25, bottom = 52;
            var x0 = Math.min.apply(null, xData), x1 = Math.max.apply(null, xData);
            var y0 = Math.min(0, Math.min.apply(null, yData), currY);
            var y1 = Math.max(1e-10, Math.max.apply(null, yData), currY);
            if (y1 - y0 < 1e-8) y1 = y0 + 1;

            var xp = function(x) { return left + (x - x0) / (x1 - x0 || 1) * (W - left - right); };
            var yp = function(y) { return H - bottom - (y - y0) / (y1 - y0 || 1) * (H - top - bottom); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var i = 0; i < 5; i++) {
              var v = y0 + (y1 - y0) * i / 4, Ypos = yp(v);
              node('line', { x1: left, y1: Ypos, x2: W - right, y2: Ypos, stroke: '#e2e8f0', 'stroke-dasharray': '3 6' });
              node('text', { x: left - 8, y: Ypos + 5, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            for (var j = 0; j < 5; j++) {
              var xV = x0 + (x1 - x0) * j / 4;
              node('text', { x: xp(xV), y: H - bottom + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': '11' }, Number(xV.toPrecision(3)).toString());
            }

            node('line', { x1: left, y1: top, x2: left, y2: H - bottom, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: left, y1: H - bottom, x2: W - right, y2: H - bottom, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pts = xData.map(function(x, idx) { return xp(x).toFixed(1) + ',' + yp(yData[idx]).toFixed(1); }).join(' ');
            node('polyline', { points: pts, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (left + W - right) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, mDef.xLabel || 'Input');
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_wsw_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var res = solve(mDef.kind, pVals);
            if (valEl) {
              valEl.textContent = Number.isFinite(res.y) ? Number(res.y.toPrecision(4)) + ' ' + (mDef.yUnit || '') : '--';
            }
            if (interpEl) interpEl.textContent = res.info || '';

            // Generate sensitivity curve varying parameter 0
            var p0Def = mDef.params[0];
            var min0 = p0Def[2], max0 = p0Def[3];
            var xData = [], yData = [];
            for (var s = 0; s <= 40; s++) {
              var xV = min0 + (max0 - min0) * s / 40;
              var curP = pVals.slice();
              curP[0] = xV;
              var ptRes = solve(mDef.kind, curP);
              if (Number.isFinite(ptRes.y)) {
                xData.push(xV);
                yData.push(ptRes.y);
              }
            }
            drawGraph(xData, yData, pVals[0], res.y);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('WSW sim error on model ' + (idx + 1), err);
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
