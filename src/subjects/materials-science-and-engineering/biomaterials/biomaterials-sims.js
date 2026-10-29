/* Biomaterials Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Uniaxial linear-elastic stress",
    "input": {
      "name": "eps",
      "label": "Engineering strain",
      "min": 0.001,
      "max": 0.05,
      "default": 0.01,
      "step": 0.001,
      "unit": "dimensionless"
    },
    "expression": "2000*eps",
    "result_unit": "MPa",
    "assumptions": "Illustrative E=2 GPa, small-strain isotropic homogeneous solid; not living tissue, fatigue or a full implant stress model",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Open-cell porosity\u2013modulus scaling",
    "input": {
      "name": "p",
      "label": "Pore volume fraction",
      "min": 0,
      "max": 0.8,
      "default": 0.4,
      "step": 0.02,
      "unit": "fraction"
    },
    "expression": "2000*Math.pow(1-p,2)",
    "result_unit": "MPa",
    "assumptions": "Power-law teaching approximation E*=Es(1-p)^2, Es=2 GPa, prefactor unity; not fitted to a real scaffold or proven connectivity",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Idealized single-protein adsorption sites",
    "input": {
      "name": "C",
      "label": "Protein concentration",
      "min": 0,
      "max": 150,
      "default": 40,
      "step": 2,
      "unit": "\u00b5g/mL"
    },
    "expression": "100*(0.02*C)/(1+0.02*C)",
    "result_unit": "% sites",
    "assumptions": "Single protein, identical independent sites, illustrative K=0.02 mL/\u00b5g and fixed equilibrium; real biological fluids are competitive",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Diffusive displacement near an interface",
    "input": {
      "name": "t",
      "label": "Diffusion time",
      "min": 30,
      "max": 3600,
      "default": 600,
      "step": 30,
      "unit": "s"
    },
    "expression": "Math.sqrt(2*1e-11*t)*1e6",
    "result_unit": "\u00b5m RMS",
    "assumptions": "1D RMS displacement with constant D=10^-11 m\u00b2/s; no binding, convection, cells or chemical reaction",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Ideal hydrogel network shear modulus",
    "input": {
      "name": "nu",
      "label": "Active-chain molar density",
      "min": 1,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "mol/m\u00b3"
    },
    "expression": "nu*8.314462618*298/1000",
    "result_unit": "kPa",
    "assumptions": "Ideal network G=\u03bdRT at T=298 K; dangling strands, phantom-network correction, entanglement, swelling and nonlinear strain omitted",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "Dilute solution osmotic pressure",
    "input": {
      "name": "c",
      "label": "Solute concentration",
      "min": 1,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "mol/m\u00b3"
    },
    "expression": "c*8.314462618*298/1000",
    "result_unit": "kPa",
    "assumptions": "Ideal van\u2019t Hoff \u03a0=cRT at T=298 K; gel elasticity, ion activity and fixed charges omitted",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Illustrative first-order remaining mass",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 0,
      "max": 180,
      "default": 60,
      "step": 2,
      "unit": "days"
    },
    "expression": "100*Math.exp(-0.012*t)",
    "result_unit": "% remaining",
    "assumptions": "Assumed effective rate 0.012 day^-1 for a declared mass population in well-controlled conditions; not a real hydrolysis or device-strength dataset",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "Illustrative reservoir release fraction",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 0,
      "max": 90,
      "default": 20,
      "step": 1,
      "unit": "days"
    },
    "expression": "100*(1-Math.exp(-0.035*t))",
    "result_unit": "% released",
    "assumptions": "Assumed well-mixed single-reservoir first-order rate 0.035 day^-1 and no burst; not a drug-release or dosing prediction",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Ideal parallel composite stiffness bound",
    "input": {
      "name": "v",
      "label": "Stiff phase volume fraction",
      "min": 0,
      "max": 0.8,
      "default": 0.35,
      "step": 0.02,
      "unit": "fraction"
    },
    "expression": "2+68*v",
    "result_unit": "GPa",
    "assumptions": "E1=70 GPa, E2=2 GPa, perfectly bonded aligned components under parallel strain; ignores porosity and tissue remodeling",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Illustrative porous compressive strength",
    "input": {
      "name": "p",
      "label": "Porosity fraction",
      "min": 0.02,
      "max": 0.75,
      "default": 0.4,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "100*Math.pow(1-p,2)",
    "result_unit": "MPa",
    "assumptions": "Nominal dense-matrix strength 100 MPa, quadratic scaling solely for sensitivity; not qualified for brittle fracture, fatigue or actual ceramics",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Ideal rigid-tube Newtonian wall shear",
    "input": {
      "name": "Q",
      "label": "Volumetric flow",
      "min": 10,
      "max": 250,
      "default": 100,
      "step": 5,
      "unit": "mL/min"
    },
    "expression": "4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))",
    "result_unit": "Pa",
    "assumptions": "Steady fully developed laminar flow, fluid viscosity 0.0035 Pa\u00b7s, fixed tube radius 1 mm; not whole-blood hemocompatibility",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Ideal rigid-tube Newtonian pressure loss",
    "input": {
      "name": "Q",
      "label": "Volumetric flow",
      "min": 10,
      "max": 250,
      "default": 100,
      "step": 5,
      "unit": "mL/min"
    },
    "expression": "8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000",
    "result_unit": "kPa",
    "assumptions": "Poiseuille rigid circular tube, viscosity 0.0035 Pa\u00b7s, length 0.2 m, radius 1 mm, no entrance or pulsatile effects",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "1D oxygen-like molecule diffusion distance",
    "input": {
      "name": "t",
      "label": "Elapsed time",
      "min": 1,
      "max": 900,
      "default": 60,
      "step": 1,
      "unit": "s"
    },
    "expression": "Math.sqrt(2*2e-9*t)*1e6",
    "result_unit": "\u00b5m RMS",
    "assumptions": "Constant D=2\u00d710^-9 m\u00b2/s, one dimension, diffusion without cellular consumption, boundary loss or reaction; not oxygen sufficiency",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Porosity-based permeability geometry factor",
    "input": {
      "name": "e",
      "label": "Void fraction",
      "min": 0.15,
      "max": 0.85,
      "default": 0.5,
      "step": 0.01,
      "unit": "fraction"
    },
    "expression": "Math.pow(e,3)/Math.pow(1-e,2)",
    "result_unit": "relative",
    "assumptions": "Kozeny-type geometric trend \u03b5\u00b3/(1\u2212\u03b5)\u00b2 without scale or tortuosity; not absolute permeability or cell-infiltration proof",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Ideal Arrhenius relative aging rate",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 298,
      "max": 338,
      "default": 318,
      "step": 1,
      "unit": "K"
    },
    "expression": "Math.exp(-(50000/8.314462618)*(1/T-1/298))",
    "result_unit": "relative to 298 K",
    "assumptions": "Single stable mechanism, constant activation energy 50 kJ/mol; not validated material shelf-life acceleration",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Chance of detecting a rare independent defect",
    "input": {
      "name": "n",
      "label": "Independent inspected units",
      "min": 1,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "units"
    },
    "expression": "100*(1-Math.pow(0.95,n))",
    "result_unit": "% chance",
    "assumptions": "Each truly independent unit has p=0.05 chance of a perfectly detectable defect; no clustering, misclassification or lot drift",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Uniaxial linear-elastic stress", "input": {"name": "eps", "label": "Engineering strain", "min": 0.001, "max": 0.05, "default": 0.01, "step": 0.001, "unit": "dimensionless"}, "expression": "2000*eps", "result_unit": "MPa", "assumptions": "Illustrative E=2 GPa, small-strain isotropic homogeneous solid; not living tissue, fatigue or a full implant stress model", "synthetic": true}, {"id": 1, "unit": 1, "title": "Open-cell porosity–modulus scaling", "input": {"name": "p", "label": "Pore volume fraction", "min": 0, "max": 0.8, "default": 0.4, "step": 0.02, "unit": "fraction"}, "expression": "2000*Math.pow(1-p,2)", "result_unit": "MPa", "assumptions": "Power-law teaching approximation E*=Es(1-p)^2, Es=2 GPa, prefactor unity; not fitted to a real scaffold or proven connectivity", "synthetic": true}, {"id": 2, "unit": 2, "title": "Idealized single-protein adsorption sites", "input": {"name": "C", "label": "Protein concentration", "min": 0, "max": 150, "default": 40, "step": 2, "unit": "µg/mL"}, "expression": "100*(0.02*C)/(1+0.02*C)", "result_unit": "% sites", "assumptions": "Single protein, identical independent sites, illustrative K=0.02 mL/µg and fixed equilibrium; real biological fluids are competitive", "synthetic": true}, {"id": 3, "unit": 2, "title": "Diffusive displacement near an interface", "input": {"name": "t", "label": "Diffusion time", "min": 30, "max": 3600, "default": 600, "step": 30, "unit": "s"}, "expression": "Math.sqrt(2*1e-11*t)*1e6", "result_unit": "µm RMS", "assumptions": "1D RMS displacement with constant D=10^-11 m²/s; no binding, convection, cells or chemical reaction", "synthetic": true}, {"id": 4, "unit": 3, "title": "Ideal hydrogel network shear modulus", "input": {"name": "nu", "label": "Active-chain molar density", "min": 1, "max": 100, "default": 20, "step": 1, "unit": "mol/m³"}, "expression": "nu*8.314462618*298/1000", "result_unit": "kPa", "assumptions": "Ideal network G=νRT at T=298 K; dangling strands, phantom-network correction, entanglement, swelling and nonlinear strain omitted", "synthetic": true}, {"id": 5, "unit": 3, "title": "Dilute solution osmotic pressure", "input": {"name": "c", "label": "Solute concentration", "min": 1, "max": 100, "default": 20, "step": 1, "unit": "mol/m³"}, "expression": "c*8.314462618*298/1000", "result_unit": "kPa", "assumptions": "Ideal van’t Hoff Π=cRT at T=298 K; gel elasticity, ion activity and fixed charges omitted", "synthetic": true}, {"id": 6, "unit": 4, "title": "Illustrative first-order remaining mass", "input": {"name": "t", "label": "Elapsed time", "min": 0, "max": 180, "default": 60, "step": 2, "unit": "days"}, "expression": "100*Math.exp(-0.012*t)", "result_unit": "% remaining", "assumptions": "Assumed effective rate 0.012 day^-1 for a declared mass population in well-controlled conditions; not a real hydrolysis or device-strength dataset", "synthetic": true}, {"id": 7, "unit": 4, "title": "Illustrative reservoir release fraction", "input": {"name": "t", "label": "Elapsed time", "min": 0, "max": 90, "default": 20, "step": 1, "unit": "days"}, "expression": "100*(1-Math.exp(-0.035*t))", "result_unit": "% released", "assumptions": "Assumed well-mixed single-reservoir first-order rate 0.035 day^-1 and no burst; not a drug-release or dosing prediction", "synthetic": true}, {"id": 8, "unit": 5, "title": "Ideal parallel composite stiffness bound", "input": {"name": "v", "label": "Stiff phase volume fraction", "min": 0, "max": 0.8, "default": 0.35, "step": 0.02, "unit": "fraction"}, "expression": "2+68*v", "result_unit": "GPa", "assumptions": "E1=70 GPa, E2=2 GPa, perfectly bonded aligned components under parallel strain; ignores porosity and tissue remodeling", "synthetic": true}, {"id": 9, "unit": 5, "title": "Illustrative porous compressive strength", "input": {"name": "p", "label": "Porosity fraction", "min": 0.02, "max": 0.75, "default": 0.4, "step": 0.01, "unit": "fraction"}, "expression": "100*Math.pow(1-p,2)", "result_unit": "MPa", "assumptions": "Nominal dense-matrix strength 100 MPa, quadratic scaling solely for sensitivity; not qualified for brittle fracture, fatigue or actual ceramics", "synthetic": true}, {"id": 10, "unit": 6, "title": "Ideal rigid-tube Newtonian wall shear", "input": {"name": "Q", "label": "Volumetric flow", "min": 10, "max": 250, "default": 100, "step": 5, "unit": "mL/min"}, "expression": "4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))", "result_unit": "Pa", "assumptions": "Steady fully developed laminar flow, fluid viscosity 0.0035 Pa·s, fixed tube radius 1 mm; not whole-blood hemocompatibility", "synthetic": true}, {"id": 11, "unit": 6, "title": "Ideal rigid-tube Newtonian pressure loss", "input": {"name": "Q", "label": "Volumetric flow", "min": 10, "max": 250, "default": 100, "step": 5, "unit": "mL/min"}, "expression": "8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000", "result_unit": "kPa", "assumptions": "Poiseuille rigid circular tube, viscosity 0.0035 Pa·s, length 0.2 m, radius 1 mm, no entrance or pulsatile effects", "synthetic": true}, {"id": 12, "unit": 7, "title": "1D oxygen-like molecule diffusion distance", "input": {"name": "t", "label": "Elapsed time", "min": 1, "max": 900, "default": 60, "step": 1, "unit": "s"}, "expression": "Math.sqrt(2*2e-9*t)*1e6", "result_unit": "µm RMS", "assumptions": "Constant D=2×10^-9 m²/s, one dimension, diffusion without cellular consumption, boundary loss or reaction; not oxygen sufficiency", "synthetic": true}, {"id": 13, "unit": 7, "title": "Porosity-based permeability geometry factor", "input": {"name": "e", "label": "Void fraction", "min": 0.15, "max": 0.85, "default": 0.5, "step": 0.01, "unit": "fraction"}, "expression": "Math.pow(e,3)/Math.pow(1-e,2)", "result_unit": "relative", "assumptions": "Kozeny-type geometric trend ε³/(1−ε)² without scale or tortuosity; not absolute permeability or cell-infiltration proof", "synthetic": true}, {"id": 14, "unit": 8, "title": "Ideal Arrhenius relative aging rate", "input": {"name": "T", "label": "Temperature", "min": 298, "max": 338, "default": 318, "step": 1, "unit": "K"}, "expression": "Math.exp(-(50000/8.314462618)*(1/T-1/298))", "result_unit": "relative to 298 K", "assumptions": "Single stable mechanism, constant activation energy 50 kJ/mol; not validated material shelf-life acceleration", "synthetic": true}, {"id": 15, "unit": 8, "title": "Chance of detecting a rare independent defect", "input": {"name": "n", "label": "Independent inspected units", "min": 1, "max": 100, "default": 20, "step": 1, "unit": "units"}, "expression": "100*(1-Math.pow(0.95,n))", "result_unit": "% chance", "assumptions": "Each truly independent unit has p=0.05 chance of a perfectly detectable defect; no clustering, misclassification or lot drift", "synthetic": true}];
function evaluate(id,x){switch(id){
case 0:return 2000*x;
case 1:return 2000*Math.pow(1-x,2);
case 2:return 100*(0.02*x)/(1+0.02*x);
case 3:return Math.sqrt(2*1e-11*x)*1e6;
case 4:return x*8.314462618*298/1000;
case 5:return x*8.314462618*298/1000;
case 6:return 100*Math.exp(-0.012*x);
case 7:return 100*(1-Math.exp(-0.035*x));
case 8:return 2+68*x;
case 9:return 100*Math.pow(1-x,2);
case 10:return 4*0.0035*(x*1e-6/60)/(Math.PI*Math.pow(0.001,3));
case 11:return 8*0.0035*0.2*(x*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000;
case 12:return Math.sqrt(2*2e-9*x)*1e6;
case 13:return Math.pow(x,3)/Math.pow(1-x,2);
case 14:return Math.exp(-(50000/8.314462618)*(1/x-1/298));
case 15:return 100*(1-Math.pow(0.95,x));
default:throw Error("unknown model");}}
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
if(typeof document !== 'undefined') document.addEventListener('DOMContentLoaded',()=>{for(const card of document.querySelectorAll('.model-card')){
 const r=card.querySelector('input');r.addEventListener('input',()=>redraw(card));redraw(card);
}});

if(typeof module!=="undefined" && module.exports){module.exports={evaluate};}



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

