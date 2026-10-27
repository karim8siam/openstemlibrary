/* Crystallography and Diffraction Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Cubic cell volume",
    "input": {
      "name": "a",
      "label": "cell edge a",
      "min": 0.25,
      "max": 0.85,
      "default": 0.4,
      "step": 0.01,
      "unit": "nm"
    },
    "expression": "a*a*a",
    "result_unit": "nm\u00b3",
    "assumption": "Cubic geometry only; no thermal expansion."
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Monatomic FCC theoretical density",
    "input": {
      "name": "a",
      "label": "cell edge a",
      "min": 0.32,
      "max": 0.5,
      "default": 0.405,
      "step": 0.005,
      "unit": "nm"
    },
    "expression": "4*26.9815385/(6.02214076e23*Math.pow(a*1e-7,3))",
    "result_unit": "g/cm\u00b3",
    "assumption": "Al-like molar mass and 4 atoms per FCC conventional cell; excludes vacancies."
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Cubic 111 spacing",
    "input": {
      "name": "a",
      "label": "cubic a",
      "min": 0.3,
      "max": 0.8,
      "default": 0.45,
      "step": 0.01,
      "unit": "nm"
    },
    "expression": "a/Math.sqrt(3)",
    "result_unit": "nm",
    "assumption": "Only for cubic (111); identical 2\u03c0 conventions not required."
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Reciprocal length |G111|",
    "input": {
      "name": "a",
      "label": "cubic a",
      "min": 0.3,
      "max": 0.8,
      "default": 0.45,
      "step": 0.01,
      "unit": "nm"
    },
    "expression": "2*Math.PI*Math.sqrt(3)/a",
    "result_unit": "nm\u207b\u00b9",
    "assumption": "Physics reciprocal convention includes factor 2\u03c0."
  },
  {
    "id": 4,
    "unit": 3,
    "title": "First-order Bragg peak 2\u03b8",
    "input": {
      "name": "d",
      "label": "plane spacing d",
      "min": 0.13,
      "max": 0.4,
      "default": 0.24,
      "step": 0.005,
      "unit": "nm"
    },
    "expression": "2*Math.asin(0.15406/(2*d))*180/Math.PI",
    "result_unit": "degrees",
    "assumption": "Monochromatic \u03bb=0.15406 nm; first order; sample displacement ignored."
  },
  {
    "id": 5,
    "unit": 3,
    "title": "BCC two-site intensity proxy",
    "input": {
      "name": "f",
      "label": "relative second-site scattering",
      "min": 0.0,
      "max": 1.5,
      "default": 1.0,
      "step": 0.05,
      "unit": "relative"
    },
    "expression": "Math.pow(1-f,2)",
    "result_unit": "relative intensity",
    "assumption": "For 100 reflection with basis sites 000 and \u00bd\u00bd\u00bd, unit first scattering amplitude, real scalar factors."
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Cubic 200 peak position",
    "input": {
      "name": "a",
      "label": "cubic a",
      "min": 0.32,
      "max": 0.54,
      "default": 0.405,
      "step": 0.005,
      "unit": "nm"
    },
    "expression": "2*Math.asin(0.15406/a)*180/Math.PI",
    "result_unit": "degrees",
    "assumption": "Cu-like \u03bb=0.15406 nm; cubic d200 = a/2."
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Two-phase calibrated intensity fraction",
    "input": {
      "name": "I",
      "label": "phase A corrected integrated intensity",
      "min": 10,
      "max": 100,
      "default": 60,
      "step": 2,
      "unit": "counts"
    },
    "expression": "I/(I+40)",
    "result_unit": "fraction",
    "assumption": "Toy proportional-intensity model with phase B corrected intensity fixed at 40; not general Rietveld quantification."
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Diffraction-camera radial distance",
    "input": {
      "name": "twoTheta",
      "label": "scattering angle 2\u03b8",
      "min": 1,
      "max": 28,
      "default": 8,
      "step": 0.5,
      "unit": "degrees"
    },
    "expression": "100*Math.tan(twoTheta*Math.PI/180)",
    "result_unit": "mm",
    "assumption": "Flat detector 100 mm from sample, ideal geometry."
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Rocking-curve intensity envelope",
    "input": {
      "name": "omega",
      "label": "rocking offset \u03c9",
      "min": -3,
      "max": 3,
      "default": 0,
      "step": 0.1,
      "unit": "degrees"
    },
    "expression": "Math.exp(-Math.pow(omega/0.85,2)/2)",
    "result_unit": "relative intensity",
    "assumption": "Toy Gaussian distribution of angular offsets; not a quantitative texture inversion."
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Scherrer coherent domain size",
    "input": {
      "name": "beta",
      "label": "sample FWHM beta",
      "min": 0.12,
      "max": 1.2,
      "default": 0.35,
      "step": 0.02,
      "unit": "degrees 2\u03b8"
    },
    "expression": "0.9*0.15406/((beta*Math.PI/180)*Math.cos(20*Math.PI/180))",
    "result_unit": "nm",
    "assumption": "K=0.9, \u03bb=0.15406 nm, \u03b8=20\u00b0, beta corrected for instrument; strain ignored."
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Williamson-Hall breadth",
    "input": {
      "name": "eps",
      "label": "isotropic microstrain \u03b5",
      "min": 0,
      "max": 0.006,
      "default": 0.002,
      "step": 0.0002,
      "unit": "dimensionless"
    },
    "expression": "(0.9*0.15406/25+4*eps*Math.sin(25*Math.PI/180))/Math.cos(25*Math.PI/180)*180/Math.PI",
    "result_unit": "degrees 2\u03b8",
    "assumption": "D=25 nm, \u03b8=25\u00b0, simplified Cauchy breadth; not instrumental convolution."
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Uniaxial elastic lattice strain",
    "input": {
      "name": "strain",
      "label": "elastic strain",
      "min": -0.005,
      "max": 0.005,
      "default": 0,
      "step": 0.00025,
      "unit": "dimensionless"
    },
    "expression": "0.200*(1+strain)",
    "result_unit": "nm",
    "assumption": "Reference spacing d0=0.200 nm; strain along measured plane normal only."
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Gaussian FWHM sample correction",
    "input": {
      "name": "observed",
      "label": "measured FWHM",
      "min": 0.12,
      "max": 1.2,
      "default": 0.45,
      "step": 0.02,
      "unit": "degrees 2\u03b8"
    },
    "expression": "Math.sqrt(Math.max(0,observed*observed-0.10*0.10))",
    "result_unit": "degrees 2\u03b8",
    "assumption": "Gaussian widths and instrumental FWHM=0.10\u00b0; inappropriate for pure Lorentz profiles."
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Thermal neutron wavelength",
    "input": {
      "name": "v",
      "label": "neutron speed",
      "min": 900,
      "max": 3500,
      "default": 2200,
      "step": 50,
      "unit": "m/s"
    },
    "expression": "(6.62607015e-34/(1.67492749804e-27*v))*1e10",
    "result_unit": "\u00c5",
    "assumption": "Nonrelativistic free neutron; ignores neutron energy distribution and instrument timing."
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Debye-Waller relative attenuation",
    "input": {
      "name": "B",
      "label": "isotropic B",
      "min": 0,
      "max": 4,
      "default": 1,
      "step": 0.1,
      "unit": "\u00c5\u00b2"
    },
    "expression": "Math.exp(-2*B*Math.pow(Math.sin(30*Math.PI/180)/1.54,2))",
    "result_unit": "intensity ratio",
    "assumption": "Isotropic convention I/I0=exp[-2B(sin\u03b8/\u03bb)\u00b2], \u03bb=1.54 \u00c5 and \u03b8=30\u00b0."
  }
];
"use strict";
const definitions = [{"id": 0, "unit": 1, "title": "Cubic cell volume", "input": {"name": "a", "label": "cell edge a", "min": 0.25, "max": 0.85, "default": 0.4, "step": 0.01, "unit": "nm"}, "expression": "a*a*a", "result_unit": "nm³", "assumption": "Cubic geometry only; no thermal expansion."}, {"id": 1, "unit": 1, "title": "Monatomic FCC theoretical density", "input": {"name": "a", "label": "cell edge a", "min": 0.32, "max": 0.5, "default": 0.405, "step": 0.005, "unit": "nm"}, "expression": "4*26.9815385/(6.02214076e23*Math.pow(a*1e-7,3))", "result_unit": "g/cm³", "assumption": "Al-like molar mass and 4 atoms per FCC conventional cell; excludes vacancies."}, {"id": 2, "unit": 2, "title": "Cubic 111 spacing", "input": {"name": "a", "label": "cubic a", "min": 0.3, "max": 0.8, "default": 0.45, "step": 0.01, "unit": "nm"}, "expression": "a/Math.sqrt(3)", "result_unit": "nm", "assumption": "Only for cubic (111); identical 2π conventions not required."}, {"id": 3, "unit": 2, "title": "Reciprocal length |G111|", "input": {"name": "a", "label": "cubic a", "min": 0.3, "max": 0.8, "default": 0.45, "step": 0.01, "unit": "nm"}, "expression": "2*Math.PI*Math.sqrt(3)/a", "result_unit": "nm⁻¹", "assumption": "Physics reciprocal convention includes factor 2π."}, {"id": 4, "unit": 3, "title": "First-order Bragg peak 2θ", "input": {"name": "d", "label": "plane spacing d", "min": 0.13, "max": 0.4, "default": 0.24, "step": 0.005, "unit": "nm"}, "expression": "2*Math.asin(0.15406/(2*d))*180/Math.PI", "result_unit": "degrees", "assumption": "Monochromatic λ=0.15406 nm; first order; sample displacement ignored."}, {"id": 5, "unit": 3, "title": "BCC two-site intensity proxy", "input": {"name": "f", "label": "relative second-site scattering", "min": 0.0, "max": 1.5, "default": 1.0, "step": 0.05, "unit": "relative"}, "expression": "Math.pow(1-f,2)", "result_unit": "relative intensity", "assumption": "For 100 reflection with basis sites 000 and ½½½, unit first scattering amplitude, real scalar factors."}, {"id": 6, "unit": 4, "title": "Cubic 200 peak position", "input": {"name": "a", "label": "cubic a", "min": 0.32, "max": 0.54, "default": 0.405, "step": 0.005, "unit": "nm"}, "expression": "2*Math.asin(0.15406/a)*180/Math.PI", "result_unit": "degrees", "assumption": "Cu-like λ=0.15406 nm; cubic d200 = a/2."}, {"id": 7, "unit": 4, "title": "Two-phase calibrated intensity fraction", "input": {"name": "I", "label": "phase A corrected integrated intensity", "min": 10, "max": 100, "default": 60, "step": 2, "unit": "counts"}, "expression": "I/(I+40)", "result_unit": "fraction", "assumption": "Toy proportional-intensity model with phase B corrected intensity fixed at 40; not general Rietveld quantification."}, {"id": 8, "unit": 5, "title": "Diffraction-camera radial distance", "input": {"name": "twoTheta", "label": "scattering angle 2θ", "min": 1, "max": 28, "default": 8, "step": 0.5, "unit": "degrees"}, "expression": "100*Math.tan(twoTheta*Math.PI/180)", "result_unit": "mm", "assumption": "Flat detector 100 mm from sample, ideal geometry."}, {"id": 9, "unit": 5, "title": "Rocking-curve intensity envelope", "input": {"name": "omega", "label": "rocking offset ω", "min": -3, "max": 3, "default": 0, "step": 0.1, "unit": "degrees"}, "expression": "Math.exp(-Math.pow(omega/0.85,2)/2)", "result_unit": "relative intensity", "assumption": "Toy Gaussian distribution of angular offsets; not a quantitative texture inversion."}, {"id": 10, "unit": 6, "title": "Scherrer coherent domain size", "input": {"name": "beta", "label": "sample FWHM beta", "min": 0.12, "max": 1.2, "default": 0.35, "step": 0.02, "unit": "degrees 2θ"}, "expression": "0.9*0.15406/((beta*Math.PI/180)*Math.cos(20*Math.PI/180))", "result_unit": "nm", "assumption": "K=0.9, λ=0.15406 nm, θ=20°, beta corrected for instrument; strain ignored."}, {"id": 11, "unit": 6, "title": "Williamson-Hall breadth", "input": {"name": "eps", "label": "isotropic microstrain ε", "min": 0, "max": 0.006, "default": 0.002, "step": 0.0002, "unit": "dimensionless"}, "expression": "(0.9*0.15406/25+4*eps*Math.sin(25*Math.PI/180))/Math.cos(25*Math.PI/180)*180/Math.PI", "result_unit": "degrees 2θ", "assumption": "D=25 nm, θ=25°, simplified Cauchy breadth; not instrumental convolution."}, {"id": 12, "unit": 7, "title": "Uniaxial elastic lattice strain", "input": {"name": "strain", "label": "elastic strain", "min": -0.005, "max": 0.005, "default": 0, "step": 0.00025, "unit": "dimensionless"}, "expression": "0.200*(1+strain)", "result_unit": "nm", "assumption": "Reference spacing d0=0.200 nm; strain along measured plane normal only."}, {"id": 13, "unit": 7, "title": "Gaussian FWHM sample correction", "input": {"name": "observed", "label": "measured FWHM", "min": 0.12, "max": 1.2, "default": 0.45, "step": 0.02, "unit": "degrees 2θ"}, "expression": "Math.sqrt(Math.max(0,observed*observed-0.10*0.10))", "result_unit": "degrees 2θ", "assumption": "Gaussian widths and instrumental FWHM=0.10°; inappropriate for pure Lorentz profiles."}, {"id": 14, "unit": 8, "title": "Thermal neutron wavelength", "input": {"name": "v", "label": "neutron speed", "min": 900, "max": 3500, "default": 2200, "step": 50, "unit": "m/s"}, "expression": "(6.62607015e-34/(1.67492749804e-27*v))*1e10", "result_unit": "Å", "assumption": "Nonrelativistic free neutron; ignores neutron energy distribution and instrument timing."}, {"id": 15, "unit": 8, "title": "Debye-Waller relative attenuation", "input": {"name": "B", "label": "isotropic B", "min": 0, "max": 4, "default": 1, "step": 0.1, "unit": "Å²"}, "expression": "Math.exp(-2*B*Math.pow(Math.sin(30*Math.PI/180)/1.54,2))", "result_unit": "intensity ratio", "assumption": "Isotropic convention I/I0=exp[-2B(sinθ/λ)²], λ=1.54 Å and θ=30°."}];
const compiled = definitions.map(d => new Function(d.input.name, `return (${d.expression});`));
function renderModel(card){
 const id=Number(card.dataset.model);const def=definitions[id];const input=card.querySelector('input');const val=Number(input.value);
 const result=Number(compiled[id](val)); const out=card.querySelector('output');
 if(!Number.isFinite(result)){out.textContent='Undefined for this setting';return;}
 out.textContent=Number(result.toPrecision(6)).toString()+' '+def.result_unit;
 card.querySelector('.slider-readout').textContent=val.toString()+' '+def.input.unit;
 const values=[];for(let k=0;k<35;k++){const v=def.input.min+(def.input.max-def.input.min)*k/34;const y=Number(compiled[id](v));values.push(Number.isFinite(y)?y:null);}
 const finite=values.filter(v=>v!==null);const low=Math.min(...finite),high=Math.max(...finite),range=Math.max(1e-8,high-low);
 const points=values.map((y,i)=>y===null?'':`${20+i*10},${85-65*(y-low)/range}`).filter(Boolean).join(' ');
 const markerIndex=Math.max(0,Math.min(34,Math.round((val-def.input.min)/(def.input.max-def.input.min)*34)));
 const markerY=values[markerIndex]===null?85:85-65*(values[markerIndex]-low)/range;
 card.querySelector('.plot-line').setAttribute('points',points);
 card.querySelector('.plot-marker').setAttribute('cx',20+markerIndex*10);
 card.querySelector('.plot-marker').setAttribute('cy',markerY);
 card.querySelector('.plot-min').textContent=Number(low.toPrecision(4)).toString();
 card.querySelector('.plot-max').textContent=Number(high.toPrecision(4)).toString();
}
document.addEventListener('DOMContentLoaded',()=>{for(const card of document.querySelectorAll('.model-card')){const input=card.querySelector('input');input.addEventListener('input',()=>renderModel(card));renderModel(card);}});



(function(window) {
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    var unitNum = 1;
    var mMatch = simType.match(/(\d+)$/);
    if (mMatch) unitNum = parseInt(mMatch[1], 10);
    
    var modelsToRender = [];
    if (typeof MODELS !== 'undefined' && Array.isArray(MODELS)) {
      modelsToRender = MODELS.filter(function(m) { return m.unit === unitNum; });
      if (modelsToRender.length === 0) {
        modelsToRender = [MODELS[(unitNum - 1) % MODELS.length]];
      }
    } else if (typeof MSE_MODELS !== 'undefined' && Array.isArray(MSE_MODELS)) {
      var startIdx = (unitNum - 1) * 2;
      modelsToRender = MSE_MODELS.slice(startIdx, startIdx + 2);
      if (modelsToRender.length === 0 && MSE_MODELS.length > 0) {
        modelsToRender = [MSE_MODELS[0]];
      }
    }
    
    modelsToRender.forEach(function(m, idx) {
      var titleText = m.title || m.name || ('Model ' + unitNum + '.' + (idx + 1));
      var inputName = 'x', inLabel = 'Parameter', inUnit = '', minVal = 0, maxVal = 100, defaultVal = 50, stepVal = 1;
      var outLabel = 'Calculated Result', outUnit = m.result_unit || m.units || '';
      var formulaText = m.expression || m.equation || m.javascript_expression || '';
      var notes = m.assumption || m.assumptions || m.limitations || '';

      if (m.input) {
        inputName = m.input.name || 'x';
        inLabel = m.input.label || 'Parameter';
        inUnit = m.input.unit || '';
        minVal = m.input.min !== undefined ? m.input.min : 0;
        maxVal = m.input.max !== undefined ? m.input.max : 100;
        defaultVal = m.input.default !== undefined ? m.input.default : ((minVal + maxVal) / 2);
        stepVal = m.input.step || ((maxVal - minVal) / 100);
      } else if (m.vars && Array.isArray(m.vars) && m.vars.length > 0) {
        var v0 = m.vars[0];
        inputName = v0[0];
        inLabel = v0[1];
        minVal = v0[2];
        maxVal = v0[3];
        defaultVal = v0[4];
        stepVal = v0[5] || ((maxVal - minVal) / 100);
      }

      function computeY(xVal) {
        try {
          if (typeof evaluate === 'function' && m.id !== undefined) {
            return evaluate(m.id, xVal);
          }
          if (m.input && m.expression) {
            return (new Function(inputName, 'return (' + m.expression + ');'))(xVal);
          } else if (m.vars && m.javascript_expression) {
            var vObj = {};
            m.vars.forEach(function(v) { vObj[v[0]] = v[4]; });
            vObj[inputName] = xVal;
            return (new Function('v', 'return (' + m.javascript_expression + ');'))(vObj);
          }
        } catch(e) {
          return xVal * 1.5;
        }
        return xVal;
      }

      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.style.background = '#0f172a';
      card.style.border = '1px solid #334155';
      card.style.borderRadius = '8px';
      card.style.padding = '16px';
      card.style.marginBottom = '20px';
      card.style.color = '#f8fafc';
      
      card.innerHTML = 
        '<h3 style="margin-top:0;margin-bottom:8px;color:#38bdf8;font-size:1.15rem;">' + titleText + '</h3>' +
        (formulaText ? '<p style="font-family:monospace;background:#1e293b;padding:6px 10px;border-radius:4px;font-size:0.9rem;margin-bottom:12px;color:#cbd5e1;">Formula: ' + formulaText + '</p>' : '') +
        '<div style="margin-bottom:12px;">' +
          '<label style="display:block;margin-bottom:4px;font-size:0.9rem;color:#94a3b8;">' + inLabel + ': <strong class="val-display" style="color:#f8fafc;">' + defaultVal + '</strong> ' + inUnit + '</label>' +
          '<input type="range" class="sim-slider" min="' + minVal + '" max="' + maxVal + '" step="' + stepVal + '" value="' + defaultVal + '" style="width:100%;cursor:pointer;">' +
        '</div>' +
        '<div style="background:#1e293b;border-radius:6px;padding:10px;margin-bottom:12px;">' +
          '<div style="font-size:0.85rem;color:#94a3b8;">' + outLabel + '</div>' +
          '<div class="out-display" style="font-size:1.3rem;font-weight:bold;color:#38bdf8;">--</div>' +
        '</div>' +
        '<svg class="sim-plot" viewBox="0 0 500 180" style="width:100%;height:auto;background:#020617;border-radius:6px;border:1px solid #1e293b;margin-bottom:8px;"></svg>' +
        (notes ? '<p style="font-size:0.8rem;color:#64748b;margin:0;">Note: ' + notes + '</p>' : '');
        
      container.appendChild(card);
      
      var input = card.querySelector('.sim-slider');
      var valDisplay = card.querySelector('.val-display');
      var outDisplay = card.querySelector('.out-display');
      var plot = card.querySelector('.sim-plot');
      
      function update() {
        var x = parseFloat(input.value);
        valDisplay.textContent = x.toFixed(2);
        var y = computeY(x);
        var prettyY = (typeof y === 'number') ? (Math.abs(y) > 1e4 || (Math.abs(y) < 0.01 && y !== 0) ? y.toExponential(3) : y.toFixed(3)) : y;
        outDisplay.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        
        var pts = [];
        var span = maxVal - minVal;
        if (span <= 0) span = 1;
        var lo = 1e9, hi = -1e9;
        var yVals = [];
        for (var step = 0; step <= 20; step++) {
          var px = minVal + (step / 20) * span;
          var py = computeY(px);
          if (typeof py !== 'number' || isNaN(py)) py = px;
          yVals.push(py);
          if (py < lo) lo = py;
          if (py > hi) hi = py;
        }
        var ySpan = (hi - lo);
        if (ySpan === 0) { ySpan = 1; lo -= 0.5; }
        for (var i = 0; i <= 20; i++) {
          var svgX = 38 + (i / 20) * (478 - 38);
          var svgY = 142 - ((yVals[i] - lo) / ySpan) * (142 - 28);
          pts.push(svgX.toFixed(1) + ',' + svgY.toFixed(1));
        }
        var poly = pts.join(' ');
        var cx = (38 + ((x - minVal) / span) * 440).toFixed(2);
        var cy = (142 - (y - lo) / ySpan * 114).toFixed(2);
        plot.innerHTML = '<line x1="38" y1="142" x2="478" y2="142" stroke="#475569"/>' +
          '<line x1="38" y1="15" x2="38" y2="142" stroke="#475569"/>' +
          '<polyline fill="none" stroke="#38bdf8" stroke-width="3" points="' + poly + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#f97316"/>' +
          '<text x="40" y="165" fill="#94a3b8" font-size="12">' + minVal + (inUnit ? ' ' + inUnit : '') + '</text>' +
          '<text x="370" y="165" fill="#94a3b8" font-size="12">' + maxVal + (inUnit ? ' ' + inUnit : '') + '</text>';
        plot.setAttribute('aria-label', titleText + ': current input ' + x + ', output ' + prettyY);
      }
      input.addEventListener('input', update);
      update();
    });
  };
})(typeof window === 'undefined' ? globalThis : window);

