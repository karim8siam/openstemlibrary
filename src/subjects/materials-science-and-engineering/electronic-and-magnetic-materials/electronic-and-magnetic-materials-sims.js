/* Electronic and Magnetic Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Metal resistivity versus temperature",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 260,
      "max": 400,
      "default": 300,
      "step": 2,
      "unit": "K"
    },
    "expression": "1.7*(1+0.0039*(T-293))",
    "result_unit": "microohm cm",
    "assumptions": "Linear temperature coefficient \u03b1=0.0039 K\u207b\u00b9 relative to 293 K; \u03c1_ref=1.7 \u03bc\u03a9 cm; illustrative metallic regime only",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Conductive thin-film sheet resistance",
    "input": {
      "name": "t",
      "label": "Film thickness",
      "min": 20,
      "max": 500,
      "default": 100,
      "step": 5,
      "unit": "nm"
    },
    "expression": "1000/t",
    "result_unit": "ohm per square",
    "assumptions": "Uniform film resistivity 100 \u03bc\u03a9 cm and t in nm; ignores interface scattering and lateral variation",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Planar dielectric capacitance",
    "input": {
      "name": "d",
      "label": "Insulator thickness",
      "min": 1,
      "max": 40,
      "default": 10,
      "step": 0.5,
      "unit": "micrometers"
    },
    "expression": "8.8541878188e-12*20*0.0001/(d*1e-6)*1e9",
    "result_unit": "nF",
    "assumptions": "Ideal parallel plates, A=1 cm\u00b2, \u03b5r=20 independent of field and frequency; no fringing",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Debye dielectric loss tangent",
    "input": {
      "name": "f",
      "label": "Drive frequency",
      "min": 50,
      "max": 100000,
      "default": 5000,
      "step": 50,
      "unit": "Hz"
    },
    "expression": "(16*(2*Math.PI*f*0.0001)/(1+Math.pow(2*Math.PI*f*0.0001,2)))/(4+16/(1+Math.pow(2*Math.PI*f*0.0001,2)))",
    "result_unit": "dimensionless",
    "assumptions": "Single relaxation time \u03c4=100 \u03bcs, \u03b5\u221e=4, \u0394\u03b5=16; excludes conduction and distributions of relaxation times",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Curie\u2013Weiss paraelectric permittivity",
    "input": {
      "name": "T",
      "label": "Temperature above assumed Curie point",
      "min": 425,
      "max": 700,
      "default": 500,
      "step": 5,
      "unit": "K"
    },
    "expression": "5+80000/(T-400)",
    "result_unit": "relative permittivity",
    "assumptions": "Paraelectric branch, T > 400 K, phenomenological C=80,000 K and background 5; not valid through transition",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Linear converse piezoelectric displacement",
    "input": {
      "name": "V",
      "label": "Applied voltage",
      "min": 0,
      "max": 50,
      "default": 10,
      "step": 1,
      "unit": "V"
    },
    "expression": "0.2*V",
    "result_unit": "nm",
    "assumptions": "Unclamped longitudinal d33=200 pm/V, uniform field, quasistatic small-signal linear response; no domain switching or resonance",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Curie paramagnetic susceptibility",
    "input": {
      "name": "T",
      "label": "Absolute temperature",
      "min": 100,
      "max": 500,
      "default": 300,
      "step": 5,
      "unit": "K"
    },
    "expression": "1.5/T",
    "result_unit": "dimensionless",
    "assumptions": "Noninteracting paramagnetic limit \u03c7=C/T with assumed C=1.5 K; no Curie\u2013Weiss offset",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Single Bohr-magneton Zeeman energy",
    "input": {
      "name": "B",
      "label": "Flux density",
      "min": 0.1,
      "max": 5,
      "default": 1,
      "step": 0.1,
      "unit": "T"
    },
    "expression": "9.2740100657e-24/(1.602176634e-19*1e-3)*B",
    "result_unit": "meV",
    "assumptions": "Absolute energy \u03bc_B B for magnitude of one Bohr magneton; spin orientation and g factors not included",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Lamination eddy-current loss proxy",
    "input": {
      "name": "f",
      "label": "Frequency",
      "min": 50,
      "max": 3000,
      "default": 500,
      "step": 50,
      "unit": "Hz"
    },
    "expression": "Math.pow(f/1000,2)",
    "result_unit": "normalized",
    "assumptions": "Reference unity at 1 kHz; Peddy \u221d f\u00b2 for constant flux amplitude, thickness, resistivity and waveform",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Uniaxial anisotropy field",
    "input": {
      "name": "K",
      "label": "Anisotropy energy density",
      "min": 10000,
      "max": 500000,
      "default": 100000,
      "step": 5000,
      "unit": "J/m\u00b3"
    },
    "expression": "2*K/(1.25663706127e-06*1000000)/1000",
    "result_unit": "kA/m",
    "assumptions": "Coherent rotation estimate with Ms=10^6 A/m; neglects reversal nucleation, multidomains and defects",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Thermal magnetic relaxation time",
    "input": {
      "name": "E",
      "label": "Anisotropy barrier",
      "min": 0.1,
      "max": 0.6,
      "default": 0.3,
      "step": 0.01,
      "unit": "eV"
    },
    "expression": "1e-9*Math.exp(E*1.602176634e-19/(1.380649e-23*300))",
    "result_unit": "s",
    "assumptions": "N\u00e9el\u2013Arrhenius \u03c40=1 ns, T=300 K, isolated single-domain particles; no barrier distribution",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Symmetric Julliere magnetoresistance",
    "input": {
      "name": "P",
      "label": "Interface spin polarization",
      "min": 0.1,
      "max": 0.8,
      "default": 0.45,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "100*2*P*P/(1-P*P)",
    "result_unit": "%",
    "assumptions": "Two identical ideal independent electrode spin polarizations, elastic tunneling, no spin flips or bias dependence",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Magnetic tunnel junction area resistance",
    "input": {
      "name": "t",
      "label": "Nominal insulating barrier thickness",
      "min": 0.6,
      "max": 2.0,
      "default": 1.1,
      "step": 0.02,
      "unit": "nm"
    },
    "expression": "10*Math.exp(1.5*(t-1))",
    "result_unit": "ohm micrometer\u00b2",
    "assumptions": "Phenomenological RA(1 nm)=10 \u03a9 \u03bcm\u00b2 and \u03b2=1.5 nm\u207b\u00b9; does not represent a certified stack",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Simplified exchange-bias field",
    "input": {
      "name": "J",
      "label": "Interface coupling energy",
      "min": 0.05,
      "max": 0.5,
      "default": 0.2,
      "step": 0.01,
      "unit": "mJ/m\u00b2"
    },
    "expression": "(J*1e-3)/(1.25663706127e-06*800000*10e-9)/1000",
    "result_unit": "kA/m",
    "assumptions": "Nominal Ms=800 kA/m and ferromagnet thickness 10 nm, ideal single interfacial coupling; no training or nonuniform exchange",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Magnetizing field in a test solenoid",
    "input": {
      "name": "I",
      "label": "Coil current",
      "min": 0.1,
      "max": 5,
      "default": 1,
      "step": 0.1,
      "unit": "A"
    },
    "expression": "200*I/0.5",
    "result_unit": "A/m",
    "assumptions": "Long-solenoid approximation N=200, magnetic path length=0.5 m; result is H, not B, and ignores demagnetization",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Volumetric hysteresis loss rate",
    "input": {
      "name": "f",
      "label": "Repetition frequency",
      "min": 10,
      "max": 500,
      "default": 100,
      "step": 10,
      "unit": "Hz"
    },
    "expression": "500*f",
    "result_unit": "W/m\u00b3",
    "assumptions": "Assumed constant cycle loop area 500 J/m\u00b3; not valid if loop area changes with f, amplitude or temperature",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Metal resistivity versus temperature", "input": {"name": "T", "label": "Absolute temperature", "min": 260, "max": 400, "default": 300, "step": 2, "unit": "K"}, "expression": "1.7*(1+0.0039*(T-293))", "result_unit": "microohm cm", "assumptions": "Linear temperature coefficient α=0.0039 K⁻¹ relative to 293 K; ρ_ref=1.7 μΩ cm; illustrative metallic regime only", "synthetic": true}, {"id": 1, "unit": 1, "title": "Conductive thin-film sheet resistance", "input": {"name": "t", "label": "Film thickness", "min": 20, "max": 500, "default": 100, "step": 5, "unit": "nm"}, "expression": "1000/t", "result_unit": "ohm per square", "assumptions": "Uniform film resistivity 100 μΩ cm and t in nm; ignores interface scattering and lateral variation", "synthetic": true}, {"id": 2, "unit": 2, "title": "Planar dielectric capacitance", "input": {"name": "d", "label": "Insulator thickness", "min": 1, "max": 40, "default": 10, "step": 0.5, "unit": "micrometers"}, "expression": "8.8541878188e-12*20*0.0001/(d*1e-6)*1e9", "result_unit": "nF", "assumptions": "Ideal parallel plates, A=1 cm², εr=20 independent of field and frequency; no fringing", "synthetic": true}, {"id": 3, "unit": 2, "title": "Debye dielectric loss tangent", "input": {"name": "f", "label": "Drive frequency", "min": 50, "max": 100000, "default": 5000, "step": 50, "unit": "Hz"}, "expression": "(16*(2*Math.PI*f*0.0001)/(1+Math.pow(2*Math.PI*f*0.0001,2)))/(4+16/(1+Math.pow(2*Math.PI*f*0.0001,2)))", "result_unit": "dimensionless", "assumptions": "Single relaxation time τ=100 μs, ε∞=4, Δε=16; excludes conduction and distributions of relaxation times", "synthetic": true}, {"id": 4, "unit": 3, "title": "Curie–Weiss paraelectric permittivity", "input": {"name": "T", "label": "Temperature above assumed Curie point", "min": 425, "max": 700, "default": 500, "step": 5, "unit": "K"}, "expression": "5+80000/(T-400)", "result_unit": "relative permittivity", "assumptions": "Paraelectric branch, T > 400 K, phenomenological C=80,000 K and background 5; not valid through transition", "synthetic": true}, {"id": 5, "unit": 3, "title": "Linear converse piezoelectric displacement", "input": {"name": "V", "label": "Applied voltage", "min": 0, "max": 50, "default": 10, "step": 1, "unit": "V"}, "expression": "0.2*V", "result_unit": "nm", "assumptions": "Unclamped longitudinal d33=200 pm/V, uniform field, quasistatic small-signal linear response; no domain switching or resonance", "synthetic": true}, {"id": 6, "unit": 4, "title": "Curie paramagnetic susceptibility", "input": {"name": "T", "label": "Absolute temperature", "min": 100, "max": 500, "default": 300, "step": 5, "unit": "K"}, "expression": "1.5/T", "result_unit": "dimensionless", "assumptions": "Noninteracting paramagnetic limit χ=C/T with assumed C=1.5 K; no Curie–Weiss offset", "synthetic": true}, {"id": 7, "unit": 4, "title": "Single Bohr-magneton Zeeman energy", "input": {"name": "B", "label": "Flux density", "min": 0.1, "max": 5, "default": 1, "step": 0.1, "unit": "T"}, "expression": "9.2740100657e-24/(1.602176634e-19*1e-3)*B", "result_unit": "meV", "assumptions": "Absolute energy μ_B B for magnitude of one Bohr magneton; spin orientation and g factors not included", "synthetic": true}, {"id": 8, "unit": 5, "title": "Lamination eddy-current loss proxy", "input": {"name": "f", "label": "Frequency", "min": 50, "max": 3000, "default": 500, "step": 50, "unit": "Hz"}, "expression": "Math.pow(f/1000,2)", "result_unit": "normalized", "assumptions": "Reference unity at 1 kHz; Peddy ∝ f² for constant flux amplitude, thickness, resistivity and waveform", "synthetic": true}, {"id": 9, "unit": 5, "title": "Uniaxial anisotropy field", "input": {"name": "K", "label": "Anisotropy energy density", "min": 10000, "max": 500000, "default": 100000, "step": 5000, "unit": "J/m³"}, "expression": "2*K/(1.25663706127e-06*1000000)/1000", "result_unit": "kA/m", "assumptions": "Coherent rotation estimate with Ms=10^6 A/m; neglects reversal nucleation, multidomains and defects", "synthetic": true}, {"id": 10, "unit": 6, "title": "Thermal magnetic relaxation time", "input": {"name": "E", "label": "Anisotropy barrier", "min": 0.1, "max": 0.6, "default": 0.3, "step": 0.01, "unit": "eV"}, "expression": "1e-9*Math.exp(E*1.602176634e-19/(1.380649e-23*300))", "result_unit": "s", "assumptions": "Néel–Arrhenius τ0=1 ns, T=300 K, isolated single-domain particles; no barrier distribution", "synthetic": true}, {"id": 11, "unit": 6, "title": "Symmetric Julliere magnetoresistance", "input": {"name": "P", "label": "Interface spin polarization", "min": 0.1, "max": 0.8, "default": 0.45, "step": 0.01, "unit": "fraction"}, "expression": "100*2*P*P/(1-P*P)", "result_unit": "%", "assumptions": "Two identical ideal independent electrode spin polarizations, elastic tunneling, no spin flips or bias dependence", "synthetic": true}, {"id": 12, "unit": 7, "title": "Magnetic tunnel junction area resistance", "input": {"name": "t", "label": "Nominal insulating barrier thickness", "min": 0.6, "max": 2.0, "default": 1.1, "step": 0.02, "unit": "nm"}, "expression": "10*Math.exp(1.5*(t-1))", "result_unit": "ohm micrometer²", "assumptions": "Phenomenological RA(1 nm)=10 Ω μm² and β=1.5 nm⁻¹; does not represent a certified stack", "synthetic": true}, {"id": 13, "unit": 7, "title": "Simplified exchange-bias field", "input": {"name": "J", "label": "Interface coupling energy", "min": 0.05, "max": 0.5, "default": 0.2, "step": 0.01, "unit": "mJ/m²"}, "expression": "(J*1e-3)/(1.25663706127e-06*800000*10e-9)/1000", "result_unit": "kA/m", "assumptions": "Nominal Ms=800 kA/m and ferromagnet thickness 10 nm, ideal single interfacial coupling; no training or nonuniform exchange", "synthetic": true}, {"id": 14, "unit": 8, "title": "Magnetizing field in a test solenoid", "input": {"name": "I", "label": "Coil current", "min": 0.1, "max": 5, "default": 1, "step": 0.1, "unit": "A"}, "expression": "200*I/0.5", "result_unit": "A/m", "assumptions": "Long-solenoid approximation N=200, magnetic path length=0.5 m; result is H, not B, and ignores demagnetization", "synthetic": true}, {"id": 15, "unit": 8, "title": "Volumetric hysteresis loss rate", "input": {"name": "f", "label": "Repetition frequency", "min": 10, "max": 500, "default": 100, "step": 10, "unit": "Hz"}, "expression": "500*f", "result_unit": "W/m³", "assumptions": "Assumed constant cycle loop area 500 J/m³; not valid if loop area changes with f, amplitude or temperature", "synthetic": true}];
function evaluate(id, x){const d=MODELS[id];return Number(new Function(d.input.name,`return (${d.expression});`)(x));}
function redraw(card){const id=Number(card.dataset.model),d=MODELS[id],r=card.querySelector('input'),x=Number(r.value),result=evaluate(id,x);
 const out=card.querySelector('output');out.textContent=Number.isFinite(result)?Number(result.toPrecision(7)).toString()+' '+d.result_unit:'Out of range';
 card.querySelector('.input-value').textContent=x+' '+d.input.unit;
 const pts=[];let ymin=Infinity,ymax=-Infinity;for(let n=0;n<45;n++){let xx=d.input.min+(d.input.max-d.input.min)*n/44;let yy=evaluate(id,xx);pts.push(yy);if(Number.isFinite(yy)){ymin=Math.min(ymin,yy);ymax=Math.max(ymax,yy)}}
 let rr=Math.max(1e-12,ymax-ymin);let path=pts.map((y,n)=>Number.isFinite(y)?`${16+8*n},${91-70*(y-ymin)/rr}`:null).filter(Boolean).join(' ');
 card.querySelector('polyline').setAttribute('points',path);
 let k=Math.max(0,Math.min(44,Math.round((x-d.input.min)/(d.input.max-d.input.min)*44)));let mark=card.querySelector('circle');
 mark.setAttribute('cx',String(16+8*k));mark.setAttribute('cy',String(91-70*(pts[k]-ymin)/rr));
 card.querySelector('.plot-min').textContent=Number(ymin.toPrecision(3));card.querySelector('.plot-max').textContent=Number(ymax.toPrecision(3));
}
document.addEventListener('DOMContentLoaded',()=>{for(const card of document.querySelectorAll('.model-card')){
 const r=card.querySelector('input');r.addEventListener('input',()=>redraw(card));redraw(card);
}});



(function(window) {
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    var unitNum = 1;
    var mMatch = (simType || '').match(/(\d+)$/);
    if (!mMatch && typeof document !== 'undefined') {
      var bIdx = document.body.dataset.chapterIndex;
      if (bIdx !== undefined && bIdx !== null && bIdx !== '') {
        unitNum = parseInt(bIdx, 10) + 1;
      }
    }
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

