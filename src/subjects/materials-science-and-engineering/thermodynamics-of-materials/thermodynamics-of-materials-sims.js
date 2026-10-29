/* Thermodynamics of Materials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Sensible heat for a fixed specimen",
    "input": {
      "name": "mass_kg",
      "label": "Specimen mass",
      "min": 0.2,
      "max": 3.0,
      "default": 1.0,
      "step": 0.1,
      "unit": "kg"
    },
    "expression": "0.9*120*mass_kg",
    "result_unit": "kJ",
    "assumptions": "Q=m c \u0394T, c=0.9 kJ/(kg K), \u0394T=120 K; no phase change",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Temperature-dependent molar enthalpy increment",
    "input": {
      "name": "T",
      "label": "Final temperature",
      "min": 350,
      "max": 1200,
      "default": 850,
      "step": 10,
      "unit": "K"
    },
    "expression": "(25*(T-300)+0.005*(T-300)**2)/1000",
    "result_unit": "kJ/mol",
    "assumptions": "Cp(T)=25+0.01(T\u2212300) J/(mol K), integrated from 300 K; one-phase illustrative fit",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Entropy increment under constant molar heat capacity",
    "input": {
      "name": "T",
      "label": "Final temperature",
      "min": 320,
      "max": 1000,
      "default": 650,
      "step": 10,
      "unit": "K"
    },
    "expression": "25*Math.log(T/300)",
    "result_unit": "J/(mol K)",
    "assumptions": "\u0394S=Cp ln(T/300), Cp=25 J/(mol K), reversible state-function path",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Reaction Gibbs energy versus temperature",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 300,
      "max": 900,
      "default": 550,
      "step": 10,
      "unit": "K"
    },
    "expression": "-45+0.08*T",
    "result_unit": "kJ/mol",
    "assumptions": "\u0394H=\u221245 kJ/mol and \u0394S=\u22120.080 kJ/(mol K), assumed constant; defined reaction basis",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Ideal B chemical-potential mixing term",
    "input": {
      "name": "x",
      "label": "Mole fraction B",
      "min": 0.03,
      "max": 0.97,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "8.31446261815324*850*Math.log(x)",
    "result_unit": "J/mol",
    "assumptions": "\u03bcB\u2212\u03bcB\u00b0=RT ln x at 850 K; ideal solution",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Ideal-gas reservoir contribution to chemical potential",
    "input": {
      "name": "P",
      "label": "Partial pressure ratio P/P\u00b0",
      "min": 0.01,
      "max": 10,
      "default": 1,
      "step": 0.01,
      "unit": "ratio"
    },
    "expression": "8.31446261815324*900*Math.log(P)",
    "result_unit": "J/mol",
    "assumptions": "\u0394\u03bc=RT ln(P/P\u00b0), at 900 K; ideal-gas fugacity approximation",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Ideal binary mixing free energy",
    "input": {
      "name": "x",
      "label": "Mole fraction B",
      "min": 0.02,
      "max": 0.98,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "8.31446261815324*800*(x*Math.log(x)+(1-x)*Math.log(1-x))/1000",
    "result_unit": "kJ/mol",
    "assumptions": "Ideal random binary solution at 800 K",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Symmetric regular-solution mixing free energy",
    "input": {
      "name": "x",
      "label": "Mole fraction B",
      "min": 0.02,
      "max": 0.98,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "(8.31446261815324*700*(x*Math.log(x)+(1-x)*Math.log(1-x))+16000*x*(1-x))/1000",
    "result_unit": "kJ/mol",
    "assumptions": "700 K, \u03a9=16,000 J/mol; mean-field random mixing",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Lever-rule B-rich phase fraction",
    "input": {
      "name": "C0",
      "label": "Overall mole fraction B",
      "min": 0.21,
      "max": 0.79,
      "default": 0.44,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "(C0-0.2)/(0.8-0.2)",
    "result_unit": "mole fraction",
    "assumptions": "Tie-line end compositions C\u03b1=0.20 and C\u03b2=0.80, fixed T,P",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Clapeyron coexistence slope",
    "input": {
      "name": "deltaV",
      "label": "Transformation molar volume change",
      "min": 0.5,
      "max": 6,
      "default": 2,
      "step": 0.1,
      "unit": "cm\u00b3/mol"
    },
    "expression": "10/(deltaV*1e-6)/1e6",
    "result_unit": "MPa/K",
    "assumptions": "\u0394S=10 J/(mol K); \u0394V=variable in cm\u00b3/mol; slope=\u0394S/\u0394V",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Equilibrium vacancy fraction",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 600,
      "max": 1800,
      "default": 1100,
      "step": 25,
      "unit": "K"
    },
    "expression": "Math.exp(-1/(8.617333262145e-5*T))",
    "result_unit": "fraction",
    "assumptions": "Dilute independent vacancies, formation free energy 1 eV; no trapping",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Interfacial Gibbs energy",
    "input": {
      "name": "area",
      "label": "Additional interface area",
      "min": 0.01,
      "max": 2,
      "default": 0.5,
      "step": 0.01,
      "unit": "m\u00b2"
    },
    "expression": "0.7*area",
    "result_unit": "J",
    "assumptions": "Isotropic interface \u03b3=0.7 J/m\u00b2; fixed chemistry and temperature",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Equilibrium-reaction constant",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 400,
      "max": 1200,
      "default": 800,
      "step": 10,
      "unit": "K"
    },
    "expression": "Math.exp(-(10000-20*T)/(8.31446261815324*T))",
    "result_unit": "dimensionless",
    "assumptions": "\u0394G\u00b0=10 kJ/mol\u22120.020 kJ/(mol K)\u00b7T; activities dimensionless",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Equilibrium Nernst potential",
    "input": {
      "name": "Q",
      "label": "Dimensionless reaction quotient",
      "min": 0.01,
      "max": 100,
      "default": 1,
      "step": 0.01,
      "unit": "ratio"
    },
    "expression": "1.10-(8.31446261815324*298/(2*96485.33212))*Math.log(Q)",
    "result_unit": "V",
    "assumptions": "Two-electron balanced cell; T=298 K, E\u00b0=1.10 V, ideal activities",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Regular-solution critical temperature",
    "input": {
      "name": "Omega",
      "label": "Binary interaction energy",
      "min": 4000,
      "max": 24000,
      "default": 16000,
      "step": 500,
      "unit": "J/mol"
    },
    "expression": "Omega/(2*8.31446261815324)",
    "result_unit": "K",
    "assumptions": "Symmetric composition-independent \u03a9, mean-field critical point at x=0.5",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Homogeneous critical nucleus radius",
    "input": {
      "name": "drive",
      "label": "Bulk free-energy driving magnitude",
      "min": 50,
      "max": 500,
      "default": 200,
      "step": 5,
      "unit": "MJ/m\u00b3"
    },
    "expression": "2*0.30/(drive*1e6)*1e9",
    "result_unit": "nm",
    "assumptions": "Spherical \u03b3=0.30 J/m\u00b2; \u0394gv=\u2212drive\u00d710\u2076 J/m\u00b3; capillarity-only",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Sensible heat for a fixed specimen", "input": {"name": "mass_kg", "label": "Specimen mass", "min": 0.2, "max": 3.0, "default": 1.0, "step": 0.1, "unit": "kg"}, "expression": "0.9*120*mass_kg", "result_unit": "kJ", "assumptions": "Q=m c ΔT, c=0.9 kJ/(kg K), ΔT=120 K; no phase change", "synthetic": true}, {"id": 1, "unit": 1, "title": "Temperature-dependent molar enthalpy increment", "input": {"name": "T", "label": "Final temperature", "min": 350, "max": 1200, "default": 850, "step": 10, "unit": "K"}, "expression": "(25*(T-300)+0.005*(T-300)**2)/1000", "result_unit": "kJ/mol", "assumptions": "Cp(T)=25+0.01(T−300) J/(mol K), integrated from 300 K; one-phase illustrative fit", "synthetic": true}, {"id": 2, "unit": 2, "title": "Entropy increment under constant molar heat capacity", "input": {"name": "T", "label": "Final temperature", "min": 320, "max": 1000, "default": 650, "step": 10, "unit": "K"}, "expression": "25*Math.log(T/300)", "result_unit": "J/(mol K)", "assumptions": "ΔS=Cp ln(T/300), Cp=25 J/(mol K), reversible state-function path", "synthetic": true}, {"id": 3, "unit": 2, "title": "Reaction Gibbs energy versus temperature", "input": {"name": "T", "label": "Temperature", "min": 300, "max": 900, "default": 550, "step": 10, "unit": "K"}, "expression": "-45+0.08*T", "result_unit": "kJ/mol", "assumptions": "ΔH=−45 kJ/mol and ΔS=−0.080 kJ/(mol K), assumed constant; defined reaction basis", "synthetic": true}, {"id": 4, "unit": 3, "title": "Ideal B chemical-potential mixing term", "input": {"name": "x", "label": "Mole fraction B", "min": 0.03, "max": 0.97, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "8.31446261815324*850*Math.log(x)", "result_unit": "J/mol", "assumptions": "μB−μB°=RT ln x at 850 K; ideal solution", "synthetic": true}, {"id": 5, "unit": 3, "title": "Ideal-gas reservoir contribution to chemical potential", "input": {"name": "P", "label": "Partial pressure ratio P/P°", "min": 0.01, "max": 10, "default": 1, "step": 0.01, "unit": "ratio"}, "expression": "8.31446261815324*900*Math.log(P)", "result_unit": "J/mol", "assumptions": "Δμ=RT ln(P/P°), at 900 K; ideal-gas fugacity approximation", "synthetic": true}, {"id": 6, "unit": 4, "title": "Ideal binary mixing free energy", "input": {"name": "x", "label": "Mole fraction B", "min": 0.02, "max": 0.98, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "8.31446261815324*800*(x*Math.log(x)+(1-x)*Math.log(1-x))/1000", "result_unit": "kJ/mol", "assumptions": "Ideal random binary solution at 800 K", "synthetic": true}, {"id": 7, "unit": 4, "title": "Symmetric regular-solution mixing free energy", "input": {"name": "x", "label": "Mole fraction B", "min": 0.02, "max": 0.98, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "(8.31446261815324*700*(x*Math.log(x)+(1-x)*Math.log(1-x))+16000*x*(1-x))/1000", "result_unit": "kJ/mol", "assumptions": "700 K, Ω=16,000 J/mol; mean-field random mixing", "synthetic": true}, {"id": 8, "unit": 5, "title": "Lever-rule B-rich phase fraction", "input": {"name": "C0", "label": "Overall mole fraction B", "min": 0.21, "max": 0.79, "default": 0.44, "step": 0.01, "unit": "fraction"}, "expression": "(C0-0.2)/(0.8-0.2)", "result_unit": "mole fraction", "assumptions": "Tie-line end compositions Cα=0.20 and Cβ=0.80, fixed T,P", "synthetic": true}, {"id": 9, "unit": 5, "title": "Clapeyron coexistence slope", "input": {"name": "deltaV", "label": "Transformation molar volume change", "min": 0.5, "max": 6, "default": 2, "step": 0.1, "unit": "cm³/mol"}, "expression": "10/(deltaV*1e-6)/1e6", "result_unit": "MPa/K", "assumptions": "ΔS=10 J/(mol K); ΔV=variable in cm³/mol; slope=ΔS/ΔV", "synthetic": true}, {"id": 10, "unit": 6, "title": "Equilibrium vacancy fraction", "input": {"name": "T", "label": "Temperature", "min": 600, "max": 1800, "default": 1100, "step": 25, "unit": "K"}, "expression": "Math.exp(-1/(8.617333262145e-5*T))", "result_unit": "fraction", "assumptions": "Dilute independent vacancies, formation free energy 1 eV; no trapping", "synthetic": true}, {"id": 11, "unit": 6, "title": "Interfacial Gibbs energy", "input": {"name": "area", "label": "Additional interface area", "min": 0.01, "max": 2, "default": 0.5, "step": 0.01, "unit": "m²"}, "expression": "0.7*area", "result_unit": "J", "assumptions": "Isotropic interface γ=0.7 J/m²; fixed chemistry and temperature", "synthetic": true}, {"id": 12, "unit": 7, "title": "Equilibrium-reaction constant", "input": {"name": "T", "label": "Temperature", "min": 400, "max": 1200, "default": 800, "step": 10, "unit": "K"}, "expression": "Math.exp(-(10000-20*T)/(8.31446261815324*T))", "result_unit": "dimensionless", "assumptions": "ΔG°=10 kJ/mol−0.020 kJ/(mol K)·T; activities dimensionless", "synthetic": true}, {"id": 13, "unit": 7, "title": "Equilibrium Nernst potential", "input": {"name": "Q", "label": "Dimensionless reaction quotient", "min": 0.01, "max": 100, "default": 1, "step": 0.01, "unit": "ratio"}, "expression": "1.10-(8.31446261815324*298/(2*96485.33212))*Math.log(Q)", "result_unit": "V", "assumptions": "Two-electron balanced cell; T=298 K, E°=1.10 V, ideal activities", "synthetic": true}, {"id": 14, "unit": 8, "title": "Regular-solution critical temperature", "input": {"name": "Omega", "label": "Binary interaction energy", "min": 4000, "max": 24000, "default": 16000, "step": 500, "unit": "J/mol"}, "expression": "Omega/(2*8.31446261815324)", "result_unit": "K", "assumptions": "Symmetric composition-independent Ω, mean-field critical point at x=0.5", "synthetic": true}, {"id": 15, "unit": 8, "title": "Homogeneous critical nucleus radius", "input": {"name": "drive", "label": "Bulk free-energy driving magnitude", "min": 50, "max": 500, "default": 200, "step": 5, "unit": "MJ/m³"}, "expression": "2*0.30/(drive*1e6)*1e9", "result_unit": "nm", "assumptions": "Spherical γ=0.30 J/m²; Δgv=−drive×10⁶ J/m³; capillarity-only", "synthetic": true}];
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

