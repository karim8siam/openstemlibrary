/* Nanomaterials and Surfaces Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "id": 0,
    "unit": 1,
    "title": "Specific surface area of nonporous spheres",
    "input": {
      "name": "d",
      "label": "Sphere diameter",
      "min": 5,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "nm"
    },
    "expression": "1000/d",
    "result_unit": "m\u00b2/g",
    "assumptions": "Identical solid spheres of density 6000 kg/m\u00b3, S_mass=6/(\u03c1d); sample has no pores, agglomeration or accessible-area restriction",
    "synthetic": true
  },
  {
    "id": 1,
    "unit": 1,
    "title": "Estimated fraction of near-surface atoms",
    "input": {
      "name": "d",
      "label": "Particle diameter",
      "min": 5,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "nm"
    },
    "expression": "100*(1-Math.pow(1-1/d,3))",
    "result_unit": "%",
    "assumptions": "A spherical shell of thickness t=0.5 nm in a homogeneous sphere: surface volume fraction=1\u2212(1\u22122t/d)^3; not exact atom counting",
    "synthetic": true
  },
  {
    "id": 2,
    "unit": 2,
    "title": "Gibbs\u2013Thomson spherical melting estimate",
    "input": {
      "name": "r",
      "label": "Particle radius",
      "min": 2,
      "max": 50,
      "default": 10,
      "step": 1,
      "unit": "nm"
    },
    "expression": "1200*(1-0.25/r)",
    "result_unit": "K",
    "assumptions": "Illustrative isotropic spherical particle; Tbulk=1200 K, interfacial-energy and latent-heat constants chosen to give \u2113=0.25 nm; excludes shape, chemistry and premelting",
    "synthetic": true
  },
  {
    "id": 3,
    "unit": 2,
    "title": "Debye length in monovalent aqueous electrolyte",
    "input": {
      "name": "I",
      "label": "Ionic strength",
      "min": 0.001,
      "max": 0.1,
      "default": 0.01,
      "step": 0.001,
      "unit": "mol/L"
    },
    "expression": "0.304/Math.sqrt(I)",
    "result_unit": "nm",
    "assumptions": "Approximate 298 K aqueous 1:1-electrolyte Debye length; continuum electrostatics, dilute solution and constant dielectric",
    "synthetic": true
  },
  {
    "id": 4,
    "unit": 3,
    "title": "Classical homogeneous nucleation barrier",
    "input": {
      "name": "g",
      "label": "Driving free energy density",
      "min": 0.8,
      "max": 2.0,
      "default": 1.2,
      "step": 0.05,
      "unit": "10^8 J/m\u00b3"
    },
    "expression": "(16*Math.PI*Math.pow(0.1,3)/(3*Math.pow(g*1e8,2)))/(1.380649e-23*298)",
    "result_unit": "kBT",
    "assumptions": "Homogeneous spherical nucleus with isotropic interfacial energy \u03b3=0.1 J/m\u00b2 at 298 K; assumes capillarity and continuum free energy",
    "synthetic": true
  },
  {
    "id": 5,
    "unit": 3,
    "title": "One-dimensional diffusion distance",
    "input": {
      "name": "t",
      "label": "Diffusion time",
      "min": 10,
      "max": 3600,
      "default": 600,
      "step": 10,
      "unit": "s"
    },
    "expression": "Math.sqrt(2*1e-18*t)*1e9",
    "result_unit": "nm",
    "assumptions": "One-dimensional diffusion displacement RMS sqrt(2Dt), D=10\u207b\u00b9\u2078 m\u00b2/s constant, no trapping or advection",
    "synthetic": true
  },
  {
    "id": 6,
    "unit": 4,
    "title": "Scherrer coherence length estimate",
    "input": {
      "name": "b",
      "label": "Corrected diffraction peak FWHM",
      "min": 0.2,
      "max": 2,
      "default": 0.6,
      "step": 0.05,
      "unit": "degrees"
    },
    "expression": "0.9*0.15406/((b*Math.PI/180)*Math.cos(20*Math.PI/180))",
    "result_unit": "nm",
    "assumptions": "K=0.9, Cu K\u03b1 \u03bb=0.15406 nm, Bragg angle \u03b8=20\u00b0, \u03b2 is strain- and instrument-corrected FWHM in radians; length is coherent domain not particle diameter",
    "synthetic": true
  },
  {
    "id": 7,
    "unit": 4,
    "title": "XPS substrate intensity attenuation",
    "input": {
      "name": "t",
      "label": "Uniform overlayer thickness",
      "min": 0,
      "max": 12,
      "default": 3,
      "step": 0.2,
      "unit": "nm"
    },
    "expression": "100*Math.exp(-t/(3*Math.cos(45*Math.PI/180)))",
    "result_unit": "%",
    "assumptions": "Simple planar overlayer with effective attenuation length 3 nm, detection angle 45\u00b0 relative to surface normal, no elastic effects or roughness",
    "synthetic": true
  },
  {
    "id": 8,
    "unit": 5,
    "title": "Langmuir ideal site occupancy",
    "input": {
      "name": "c",
      "label": "Adsorbate concentration",
      "min": 1,
      "max": 1000,
      "default": 100,
      "step": 5,
      "unit": "\u00b5mol/L"
    },
    "expression": "100*(0.1*c)/(1+0.1*c)",
    "result_unit": "%",
    "assumptions": "Single-site independent adsorption, K=10^5 L/mol; c input \u00b5mol/L so Kc=0.1c; no interactions, competition or irreversible chemistry",
    "synthetic": true
  },
  {
    "id": 9,
    "unit": 5,
    "title": "Surface-reaction Arrhenius temperature ratio",
    "input": {
      "name": "T",
      "label": "Temperature",
      "min": 290,
      "max": 390,
      "default": 330,
      "step": 2,
      "unit": "K"
    },
    "expression": "Math.exp(-(45000/8.314462618)*(1/T-1/298))",
    "result_unit": "relative",
    "assumptions": "Rate constant relative to 298 K; activation energy 45 kJ/mol fixed, neglects diffusion control, coverage changes and mechanism shifts",
    "synthetic": true
  },
  {
    "id": 10,
    "unit": 6,
    "title": "Electron-in-a-box confinement energy",
    "input": {
      "name": "L",
      "label": "Quantum well width",
      "min": 3,
      "max": 30,
      "default": 10,
      "step": 0.5,
      "unit": "nm"
    },
    "expression": "(Math.PI*Math.PI*Math.pow(6.62607015e-34/(2*Math.PI),2)/(2*0.13*9.1093837139e-31*Math.pow(L*1e-9,2)))/1.602176634e-19",
    "result_unit": "eV",
    "assumptions": "Infinite one-dimensional well, effective mass 0.13 m_e, single-particle ground-state contribution; ignores excitons, nonparabolicity and finite barriers",
    "synthetic": true
  },
  {
    "id": 11,
    "unit": 6,
    "title": "Coulomb charging energy of a nanosphere",
    "input": {
      "name": "r",
      "label": "Particle radius",
      "min": 2,
      "max": 30,
      "default": 8,
      "step": 0.5,
      "unit": "nm"
    },
    "expression": "1.43996448/(2*5*r)",
    "result_unit": "eV",
    "assumptions": "Isolated spherical conductor model E=e\u00b2/(2C), C=4\u03c0\u03b50\u03b5r r, \u03b5r=5 constant; quantum tunneling and electrochemical environment excluded",
    "synthetic": true
  },
  {
    "id": 12,
    "unit": 7,
    "title": "Young equilibrium contact angle",
    "input": {
      "name": "dg",
      "label": "Surface-energy difference \u03b3SV\u2212\u03b3SL",
      "min": -30,
      "max": 30,
      "default": 0,
      "step": 2,
      "unit": "mN/m"
    },
    "expression": "Math.acos(dg/72)*180/Math.PI",
    "result_unit": "degrees",
    "assumptions": "Smooth rigid chemically homogeneous planar solid, \u03b3LV=72 mN/m; ideal equilibrium under ambient conditions, ignores hysteresis",
    "synthetic": true
  },
  {
    "id": 13,
    "unit": 7,
    "title": "Wenzel apparent angle for an ideal rough surface",
    "input": {
      "name": "r",
      "label": "True-to-projected surface-area ratio",
      "min": 1,
      "max": 2.5,
      "default": 1.5,
      "step": 0.05,
      "unit": "dimensionless"
    },
    "expression": "Math.acos(r*Math.cos(110*Math.PI/180))*180/Math.PI",
    "result_unit": "degrees",
    "assumptions": "Chemically homogeneous fully wetted rough solid with intrinsic Young angle 110\u00b0, Wenzel cos\u03b8*=r cos\u03b8; no trapped air or metastable pinning",
    "synthetic": true
  },
  {
    "id": 14,
    "unit": 8,
    "title": "Stokes settling speed for dense nano spheres",
    "input": {
      "name": "r",
      "label": "Sphere radius",
      "min": 10,
      "max": 500,
      "default": 100,
      "step": 10,
      "unit": "nm"
    },
    "expression": "(2/9)*1000*9.81*Math.pow(r*1e-9,2)/0.001*1e9",
    "result_unit": "nm/s",
    "assumptions": "Dilute spheres with density excess 1000 kg/m\u00b3 in waterlike fluid \u03b7=0.001 Pa s, low Reynolds number; neglect Brownian motion and aggregation",
    "synthetic": true
  },
  {
    "id": 15,
    "unit": 8,
    "title": "Stokes\u2013Einstein translational diffusivity",
    "input": {
      "name": "r",
      "label": "Hydrodynamic radius",
      "min": 5,
      "max": 100,
      "default": 20,
      "step": 1,
      "unit": "nm"
    },
    "expression": "(1.380649e-23*298/(6*Math.PI*0.001*r*1e-9))*1e12",
    "result_unit": "\u00b5m\u00b2/s",
    "assumptions": "Hydrodynamic sphere in Newtonian waterlike medium \u03b7=0.001 Pa s at 298 K, no slip and negligible interactions or confinement",
    "synthetic": true
  }
];
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Specific surface area of nonporous spheres", "input": {"name": "d", "label": "Sphere diameter", "min": 5, "max": 100, "default": 20, "step": 1, "unit": "nm"}, "expression": "1000/d", "result_unit": "m²/g", "assumptions": "Identical solid spheres of density 6000 kg/m³, S_mass=6/(ρd); sample has no pores, agglomeration or accessible-area restriction", "synthetic": true}, {"id": 1, "unit": 1, "title": "Estimated fraction of near-surface atoms", "input": {"name": "d", "label": "Particle diameter", "min": 5, "max": 100, "default": 20, "step": 1, "unit": "nm"}, "expression": "100*(1-Math.pow(1-1/d,3))", "result_unit": "%", "assumptions": "A spherical shell of thickness t=0.5 nm in a homogeneous sphere: surface volume fraction=1−(1−2t/d)^3; not exact atom counting", "synthetic": true}, {"id": 2, "unit": 2, "title": "Gibbs–Thomson spherical melting estimate", "input": {"name": "r", "label": "Particle radius", "min": 2, "max": 50, "default": 10, "step": 1, "unit": "nm"}, "expression": "1200*(1-0.25/r)", "result_unit": "K", "assumptions": "Illustrative isotropic spherical particle; Tbulk=1200 K, interfacial-energy and latent-heat constants chosen to give ℓ=0.25 nm; excludes shape, chemistry and premelting", "synthetic": true}, {"id": 3, "unit": 2, "title": "Debye length in monovalent aqueous electrolyte", "input": {"name": "I", "label": "Ionic strength", "min": 0.001, "max": 0.1, "default": 0.01, "step": 0.001, "unit": "mol/L"}, "expression": "0.304/Math.sqrt(I)", "result_unit": "nm", "assumptions": "Approximate 298 K aqueous 1:1-electrolyte Debye length; continuum electrostatics, dilute solution and constant dielectric", "synthetic": true}, {"id": 4, "unit": 3, "title": "Classical homogeneous nucleation barrier", "input": {"name": "g", "label": "Driving free energy density", "min": 0.8, "max": 2.0, "default": 1.2, "step": 0.05, "unit": "10^8 J/m³"}, "expression": "(16*Math.PI*Math.pow(0.1,3)/(3*Math.pow(g*1e8,2)))/(1.380649e-23*298)", "result_unit": "kBT", "assumptions": "Homogeneous spherical nucleus with isotropic interfacial energy γ=0.1 J/m² at 298 K; assumes capillarity and continuum free energy", "synthetic": true}, {"id": 5, "unit": 3, "title": "One-dimensional diffusion distance", "input": {"name": "t", "label": "Diffusion time", "min": 10, "max": 3600, "default": 600, "step": 10, "unit": "s"}, "expression": "Math.sqrt(2*1e-18*t)*1e9", "result_unit": "nm", "assumptions": "One-dimensional diffusion displacement RMS sqrt(2Dt), D=10⁻¹⁸ m²/s constant, no trapping or advection", "synthetic": true}, {"id": 6, "unit": 4, "title": "Scherrer coherence length estimate", "input": {"name": "b", "label": "Corrected diffraction peak FWHM", "min": 0.2, "max": 2, "default": 0.6, "step": 0.05, "unit": "degrees"}, "expression": "0.9*0.15406/((b*Math.PI/180)*Math.cos(20*Math.PI/180))", "result_unit": "nm", "assumptions": "K=0.9, Cu Kα λ=0.15406 nm, Bragg angle θ=20°, β is strain- and instrument-corrected FWHM in radians; length is coherent domain not particle diameter", "synthetic": true}, {"id": 7, "unit": 4, "title": "XPS substrate intensity attenuation", "input": {"name": "t", "label": "Uniform overlayer thickness", "min": 0, "max": 12, "default": 3, "step": 0.2, "unit": "nm"}, "expression": "100*Math.exp(-t/(3*Math.cos(45*Math.PI/180)))", "result_unit": "%", "assumptions": "Simple planar overlayer with effective attenuation length 3 nm, detection angle 45° relative to surface normal, no elastic effects or roughness", "synthetic": true}, {"id": 8, "unit": 5, "title": "Langmuir ideal site occupancy", "input": {"name": "c", "label": "Adsorbate concentration", "min": 1, "max": 1000, "default": 100, "step": 5, "unit": "µmol/L"}, "expression": "100*(0.1*c)/(1+0.1*c)", "result_unit": "%", "assumptions": "Single-site independent adsorption, K=10^5 L/mol; c input µmol/L so Kc=0.1c; no interactions, competition or irreversible chemistry", "synthetic": true}, {"id": 9, "unit": 5, "title": "Surface-reaction Arrhenius temperature ratio", "input": {"name": "T", "label": "Temperature", "min": 290, "max": 390, "default": 330, "step": 2, "unit": "K"}, "expression": "Math.exp(-(45000/8.314462618)*(1/T-1/298))", "result_unit": "relative", "assumptions": "Rate constant relative to 298 K; activation energy 45 kJ/mol fixed, neglects diffusion control, coverage changes and mechanism shifts", "synthetic": true}, {"id": 10, "unit": 6, "title": "Electron-in-a-box confinement energy", "input": {"name": "L", "label": "Quantum well width", "min": 3, "max": 30, "default": 10, "step": 0.5, "unit": "nm"}, "expression": "(Math.PI*Math.PI*Math.pow(6.62607015e-34/(2*Math.PI),2)/(2*0.13*9.1093837139e-31*Math.pow(L*1e-9,2)))/1.602176634e-19", "result_unit": "eV", "assumptions": "Infinite one-dimensional well, effective mass 0.13 m_e, single-particle ground-state contribution; ignores excitons, nonparabolicity and finite barriers", "synthetic": true}, {"id": 11, "unit": 6, "title": "Coulomb charging energy of a nanosphere", "input": {"name": "r", "label": "Particle radius", "min": 2, "max": 30, "default": 8, "step": 0.5, "unit": "nm"}, "expression": "1.43996448/(2*5*r)", "result_unit": "eV", "assumptions": "Isolated spherical conductor model E=e²/(2C), C=4πε0εr r, εr=5 constant; quantum tunneling and electrochemical environment excluded", "synthetic": true}, {"id": 12, "unit": 7, "title": "Young equilibrium contact angle", "input": {"name": "dg", "label": "Surface-energy difference γSV−γSL", "min": -30, "max": 30, "default": 0, "step": 2, "unit": "mN/m"}, "expression": "Math.acos(dg/72)*180/Math.PI", "result_unit": "degrees", "assumptions": "Smooth rigid chemically homogeneous planar solid, γLV=72 mN/m; ideal equilibrium under ambient conditions, ignores hysteresis", "synthetic": true}, {"id": 13, "unit": 7, "title": "Wenzel apparent angle for an ideal rough surface", "input": {"name": "r", "label": "True-to-projected surface-area ratio", "min": 1, "max": 2.5, "default": 1.5, "step": 0.05, "unit": "dimensionless"}, "expression": "Math.acos(r*Math.cos(110*Math.PI/180))*180/Math.PI", "result_unit": "degrees", "assumptions": "Chemically homogeneous fully wetted rough solid with intrinsic Young angle 110°, Wenzel cosθ*=r cosθ; no trapped air or metastable pinning", "synthetic": true}, {"id": 14, "unit": 8, "title": "Stokes settling speed for dense nano spheres", "input": {"name": "r", "label": "Sphere radius", "min": 10, "max": 500, "default": 100, "step": 10, "unit": "nm"}, "expression": "(2/9)*1000*9.81*Math.pow(r*1e-9,2)/0.001*1e9", "result_unit": "nm/s", "assumptions": "Dilute spheres with density excess 1000 kg/m³ in waterlike fluid η=0.001 Pa s, low Reynolds number; neglect Brownian motion and aggregation", "synthetic": true}, {"id": 15, "unit": 8, "title": "Stokes–Einstein translational diffusivity", "input": {"name": "r", "label": "Hydrodynamic radius", "min": 5, "max": 100, "default": 20, "step": 1, "unit": "nm"}, "expression": "(1.380649e-23*298/(6*Math.PI*0.001*r*1e-9))*1e12", "result_unit": "µm²/s", "assumptions": "Hydrodynamic sphere in Newtonian waterlike medium η=0.001 Pa s at 298 K, no slip and negligible interactions or confinement", "synthetic": true}];
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

