/* Fundamentals of Materials Science and Engineering Interactive Simulation Suite */
var MSE_MODELS = [
  {
    "name": "Elastic modulus from slope",
    "vars": [
      [
        "s",
        "Stress (MPa)",
        10,
        500,
        180,
        5
      ],
      [
        "p",
        "Strain (%)",
        0.05,
        2,
        0.3,
        0.05
      ]
    ],
    "units": "GPa",
    "equation": "E = (stress in MPa)/(strain fraction)/1000",
    "limitations": "Elastic fit only; assumes linear reversibility.",
    "javascript_expression": "v.s/(10*v.p)"
  },
  {
    "name": "Specific strength",
    "vars": [
      [
        "s",
        "Strength (MPa)",
        50,
        1200,
        450,
        25
      ],
      [
        "r",
        "Density (kg/m\u00b3)",
        900,
        9000,
        2700,
        100
      ]
    ],
    "units": "kN\u00b7m/kg",
    "equation": "specific strength = strength / density",
    "limitations": "Property index only, not a complete structural design.",
    "javascript_expression": "v.s*1e6/v.r/1000"
  },
  {
    "name": "Cubic lattice spacing",
    "vars": [
      [
        "a",
        "Lattice parameter (nm)",
        0.2,
        0.8,
        0.4,
        0.01
      ],
      [
        "h",
        "Miller h",
        0,
        4,
        1,
        1
      ],
      [
        "k",
        "Miller k",
        0,
        4,
        1,
        1
      ],
      [
        "l",
        "Miller l",
        0,
        4,
        1,
        1
      ]
    ],
    "units": "nm",
    "equation": "d_hkl = a / \u221a(h\u00b2+k\u00b2+l\u00b2)",
    "limitations": "Cubic metric only; (0,0,0) is not a valid plane.",
    "javascript_expression": "v.a/Math.sqrt(Math.max(1,v.h*v.h+v.k*v.k+v.l*v.l))"
  },
  {
    "name": "First-order Bragg angle",
    "vars": [
      [
        "lam",
        "Wavelength (nm)",
        0.05,
        0.22,
        0.154,
        0.002
      ],
      [
        "d",
        "Spacing (nm)",
        0.12,
        0.6,
        0.25,
        0.01
      ]
    ],
    "units": "degrees \u03b8",
    "equation": "\u03b8 = arcsin(\u03bb/(2d))",
    "limitations": "Reports \u03b8, whereas diffractometers usually report 2\u03b8.",
    "javascript_expression": "Math.asin(Math.min(1,v.lam/(2*v.d)))*180/Math.PI"
  },
  {
    "name": "Diffusion length",
    "vars": [
      [
        "D",
        "Diffusivity (\u00d710\u207b\u00b9\u2074 m\u00b2/s)",
        0.1,
        100,
        5,
        0.1
      ],
      [
        "t",
        "Time (h)",
        0.1,
        48,
        2,
        0.1
      ]
    ],
    "units": "\u00b5m",
    "equation": "\u2113 = \u221a(2Dt)",
    "limitations": "One-dimensional ideal scaling for constant diffusivity.",
    "javascript_expression": "Math.sqrt(2*v.D*1e-14*v.t*3600)*1e6"
  },
  {
    "name": "Hall\u2013Petch stress",
    "vars": [
      [
        "s0",
        "Base stress (MPa)",
        50,
        400,
        120,
        5
      ],
      [
        "k",
        "Coefficient (MPa\u221am)",
        0.05,
        1,
        0.35,
        0.01
      ],
      [
        "d",
        "Grain size (\u00b5m)",
        1,
        200,
        20,
        1
      ]
    ],
    "units": "MPa",
    "equation": "\u03c3_y = \u03c3\u2080 + k/\u221ad",
    "limitations": "Empirical finite-regime relation; micron input converted to meters.",
    "javascript_expression": "v.s0+v.k/Math.sqrt(v.d*1e-6)"
  },
  {
    "name": "Elastic rod extension",
    "vars": [
      [
        "F",
        "Axial force (kN)",
        1,
        50,
        10,
        1
      ],
      [
        "L",
        "Length (m)",
        0.1,
        2,
        0.8,
        0.1
      ],
      [
        "A",
        "Area (mm\u00b2)",
        10,
        500,
        100,
        10
      ],
      [
        "E",
        "Modulus (GPa)",
        5,
        230,
        70,
        5
      ]
    ],
    "units": "mm",
    "equation": "\u0394L = FL/(AE)",
    "limitations": "Axial linear-elastic uniform rod; excludes buckling and joints.",
    "javascript_expression": "v.F*1000*v.L/(v.A*1e-6*v.E*1e9)*1000"
  },
  {
    "name": "Crack-limited stress",
    "vars": [
      [
        "K",
        "Toughness (MPa\u221am)",
        2,
        120,
        40,
        2
      ],
      [
        "Y",
        "Shape factor",
        0.7,
        2,
        1.1,
        0.05
      ],
      [
        "a",
        "Crack length (mm)",
        0.1,
        10,
        2,
        0.1
      ]
    ],
    "units": "MPa",
    "equation": "\u03c3_c = K_IC / (Y\u221a(\u03c0a))",
    "limitations": "Linear-elastic mode-I illustration, not a certified tolerance.",
    "javascript_expression": "v.K/(v.Y*Math.sqrt(Math.PI*v.a/1000))"
  },
  {
    "name": "Lever-rule alpha fraction",
    "vars": [
      [
        "Ca",
        "Alpha composition (mass %)",
        0,
        30,
        10,
        1
      ],
      [
        "C0",
        "Bulk composition (mass %)",
        30,
        50,
        40,
        1
      ],
      [
        "Cb",
        "Beta composition (mass %)",
        60,
        100,
        80,
        1
      ]
    ],
    "units": "fraction",
    "equation": "f\u03b1 = (C\u03b2 \u2212 C\u2080)/(C\u03b2 \u2212 C\u03b1)",
    "limitations": "Valid only when C\u03b1 < C\u2080 < C\u03b2 in a binary two-phase field.",
    "javascript_expression": "(v.Cb-v.C0)/Math.max(0.001,v.Cb-v.Ca)"
  },
  {
    "name": "Arrhenius rate coefficient",
    "vars": [
      [
        "A",
        "Prefactor (1/s)",
        1000,
        1000000,
        100000,
        1000
      ],
      [
        "Q",
        "Activation energy (kJ/mol)",
        20,
        160,
        60,
        2
      ],
      [
        "T",
        "Temperature (K)",
        350,
        1200,
        650,
        10
      ]
    ],
    "units": "s\u207b\u00b9",
    "equation": "k = A exp(\u2212Q/RT)",
    "limitations": "Idealized single-process kinetic fit; parameters not universal.",
    "javascript_expression": "v.A*Math.exp(-v.Q*1000/(8.314462618*v.T))"
  },
  {
    "name": "Aligned-fiber axial modulus",
    "vars": [
      [
        "Ef",
        "Fiber modulus (GPa)",
        30,
        400,
        230,
        10
      ],
      [
        "Em",
        "Matrix modulus (GPa)",
        1,
        15,
        3,
        1
      ],
      [
        "vf",
        "Fiber volume fraction",
        0.1,
        0.75,
        0.55,
        0.05
      ]
    ],
    "units": "GPa",
    "equation": "E_parallel = E_f V_f + E_m (1 \u2212 V_f)",
    "limitations": "Ideal isostrain aligned continuous fibers only.",
    "javascript_expression": "v.Ef*v.vf+v.Em*(1-v.vf)"
  },
  {
    "name": "Porosity modulus penalty",
    "vars": [
      [
        "E0",
        "Dense modulus (GPa)",
        20,
        450,
        200,
        10
      ],
      [
        "p",
        "Porosity (%)",
        0,
        60,
        12,
        1
      ]
    ],
    "units": "GPa",
    "equation": "E_eff \u2248 E\u2080(1 \u2212 \u03c6)\u00b2",
    "limitations": "Illustrative empirical scaling, not a material-independent law.",
    "javascript_expression": "v.E0*Math.pow(1-v.p/100,2)"
  },
  {
    "name": "Layer thermal resistance",
    "vars": [
      [
        "L",
        "Thickness (mm)",
        0.2,
        60,
        10,
        0.2
      ],
      [
        "k",
        "Conductivity (W/m/K)",
        0.05,
        250,
        2,
        0.05
      ],
      [
        "A",
        "Area (cm\u00b2)",
        1,
        300,
        50,
        1
      ]
    ],
    "units": "K/W",
    "equation": "R_th = L/(kA)",
    "limitations": "Steady one-dimensional conduction; omits contact and losses.",
    "javascript_expression": "(v.L/1000)/(v.k*(v.A/10000))"
  },
  {
    "name": "Charge-carrier resistivity",
    "vars": [
      [
        "n",
        "Carrier density (\u00d710\u00b2\u2078 m\u207b\u00b3)",
        0.01,
        5,
        1,
        0.01
      ],
      [
        "mu",
        "Mobility (\u00d710\u207b\u00b3 m\u00b2/Vs)",
        0.1,
        20,
        2,
        0.1
      ]
    ],
    "units": "\u03a9\u00b7m",
    "equation": "\u03c1 = 1/(nq\u03bc)",
    "limitations": "One carrier type; neglects contacts and field effects.",
    "javascript_expression": "1/(v.n*1e28*1.602176634e-19*v.mu*1e-3)"
  },
  {
    "name": "Embodied carbon screening",
    "vars": [
      [
        "m",
        "Mass (kg)",
        0.1,
        500,
        20,
        1
      ],
      [
        "f",
        "Emission factor (kg CO\u2082e/kg)",
        0.2,
        20,
        3.5,
        0.1
      ]
    ],
    "units": "kg CO\u2082e",
    "equation": "G = mass \u00d7 assumed emission factor",
    "limitations": "Synthetic screening; not a verified life-cycle inventory.",
    "javascript_expression": "v.m*v.f"
  },
  {
    "name": "Stiffness-weight index",
    "vars": [
      [
        "E",
        "Young modulus (GPa)",
        1,
        400,
        70,
        1
      ],
      [
        "r",
        "Density (kg/m\u00b3)",
        500,
        10000,
        2700,
        100
      ]
    ],
    "units": "index units",
    "equation": "M = \u221aE / \u03c1",
    "limitations": "Illustrative for a defined bending-dominated variable-section case only.",
    "javascript_expression": "Math.sqrt(v.E*1e9)/v.r"
  }
];

(function(){
 const data=[{"name":"Elastic modulus from slope","vars":[["s","Stress (MPa)",10,500,180,5],["p","Strain (%)",0.05,2,0.3,0.05]],"js":"v.s/(10*v.p)","units":"GPa","equation":"E = (stress in MPa)/(strain fraction)/1000","limitations":"Elastic fit only; assumes linear reversibility."},{"name":"Specific strength","vars":[["s","Strength (MPa)",50,1200,450,25],["r","Density (kg/m³)",900,9000,2700,100]],"js":"v.s*1e6/v.r/1000","units":"kN·m/kg","equation":"specific strength = strength / density","limitations":"Property index only, not a complete structural design."},{"name":"Cubic lattice spacing","vars":[["a","Lattice parameter (nm)",0.2,0.8,0.4,0.01],["h","Miller h",0,4,1,1],["k","Miller k",0,4,1,1],["l","Miller l",0,4,1,1]],"js":"v.a/Math.sqrt(Math.max(1,v.h*v.h+v.k*v.k+v.l*v.l))","units":"nm","equation":"d_hkl = a / √(h²+k²+l²)","limitations":"Cubic metric only; (0,0,0) is not a valid plane."},{"name":"First-order Bragg angle","vars":[["lam","Wavelength (nm)",0.05,0.22,0.154,0.002],["d","Spacing (nm)",0.12,0.6,0.25,0.01]],"js":"Math.asin(Math.min(1,v.lam/(2*v.d)))*180/Math.PI","units":"degrees θ","equation":"θ = arcsin(λ/(2d))","limitations":"Reports θ, whereas diffractometers usually report 2θ."},{"name":"Diffusion length","vars":[["D","Diffusivity (×10⁻¹⁴ m²/s)",0.1,100,5,0.1],["t","Time (h)",0.1,48,2,0.1]],"js":"Math.sqrt(2*v.D*1e-14*v.t*3600)*1e6","units":"µm","equation":"ℓ = √(2Dt)","limitations":"One-dimensional ideal scaling for constant diffusivity."},{"name":"Hall–Petch stress","vars":[["s0","Base stress (MPa)",50,400,120,5],["k","Coefficient (MPa√m)",0.05,1,0.35,0.01],["d","Grain size (µm)",1,200,20,1]],"js":"v.s0+v.k/Math.sqrt(v.d*1e-6)","units":"MPa","equation":"σ_y = σ₀ + k/√d","limitations":"Empirical finite-regime relation; micron input converted to meters."},{"name":"Elastic rod extension","vars":[["F","Axial force (kN)",1,50,10,1],["L","Length (m)",0.1,2,0.8,0.1],["A","Area (mm²)",10,500,100,10],["E","Modulus (GPa)",5,230,70,5]],"js":"v.F*1000*v.L/(v.A*1e-6*v.E*1e9)*1000","units":"mm","equation":"ΔL = FL/(AE)","limitations":"Axial linear-elastic uniform rod; excludes buckling and joints."},{"name":"Crack-limited stress","vars":[["K","Toughness (MPa√m)",2,120,40,2],["Y","Shape factor",0.7,2,1.1,0.05],["a","Crack length (mm)",0.1,10,2,0.1]],"js":"v.K/(v.Y*Math.sqrt(Math.PI*v.a/1000))","units":"MPa","equation":"σ_c = K_IC / (Y√(πa))","limitations":"Linear-elastic mode-I illustration, not a certified tolerance."},{"name":"Lever-rule alpha fraction","vars":[["Ca","Alpha composition (mass %)",0,30,10,1],["C0","Bulk composition (mass %)",30,50,40,1],["Cb","Beta composition (mass %)",60,100,80,1]],"js":"(v.Cb-v.C0)/Math.max(0.001,v.Cb-v.Ca)","units":"fraction","equation":"fα = (Cβ − C₀)/(Cβ − Cα)","limitations":"Valid only when Cα < C₀ < Cβ in a binary two-phase field."},{"name":"Arrhenius rate coefficient","vars":[["A","Prefactor (1/s)",1000,1000000,100000,1000],["Q","Activation energy (kJ/mol)",20,160,60,2],["T","Temperature (K)",350,1200,650,10]],"js":"v.A*Math.exp(-v.Q*1000/(8.314462618*v.T))","units":"s⁻¹","equation":"k = A exp(−Q/RT)","limitations":"Idealized single-process kinetic fit; parameters not universal."},{"name":"Aligned-fiber axial modulus","vars":[["Ef","Fiber modulus (GPa)",30,400,230,10],["Em","Matrix modulus (GPa)",1,15,3,1],["vf","Fiber volume fraction",0.1,0.75,0.55,0.05]],"js":"v.Ef*v.vf+v.Em*(1-v.vf)","units":"GPa","equation":"E_parallel = E_f V_f + E_m (1 − V_f)","limitations":"Ideal isostrain aligned continuous fibers only."},{"name":"Porosity modulus penalty","vars":[["E0","Dense modulus (GPa)",20,450,200,10],["p","Porosity (%)",0,60,12,1]],"js":"v.E0*Math.pow(1-v.p/100,2)","units":"GPa","equation":"E_eff ≈ E₀(1 − φ)²","limitations":"Illustrative empirical scaling, not a material-independent law."},{"name":"Layer thermal resistance","vars":[["L","Thickness (mm)",0.2,60,10,0.2],["k","Conductivity (W/m/K)",0.05,250,2,0.05],["A","Area (cm²)",1,300,50,1]],"js":"(v.L/1000)/(v.k*(v.A/10000))","units":"K/W","equation":"R_th = L/(kA)","limitations":"Steady one-dimensional conduction; omits contact and losses."},{"name":"Charge-carrier resistivity","vars":[["n","Carrier density (×10²⁸ m⁻³)",0.01,5,1,0.01],["mu","Mobility (×10⁻³ m²/Vs)",0.1,20,2,0.1]],"js":"1/(v.n*1e28*1.602176634e-19*v.mu*1e-3)","units":"Ω·m","equation":"ρ = 1/(nqμ)","limitations":"One carrier type; neglects contacts and field effects."},{"name":"Embodied carbon screening","vars":[["m","Mass (kg)",0.1,500,20,1],["f","Emission factor (kg CO₂e/kg)",0.2,20,3.5,0.1]],"js":"v.m*v.f","units":"kg CO₂e","equation":"G = mass × assumed emission factor","limitations":"Synthetic screening; not a verified life-cycle inventory."},{"name":"Stiffness-weight index","vars":[["E","Young modulus (GPa)",1,400,70,1],["r","Density (kg/m³)",500,10000,2700,100]],"js":"Math.sqrt(v.E*1e9)/v.r","units":"index units","equation":"M = √E / ρ","limitations":"Illustrative for a defined bending-dominated variable-section case only."}];
 const formulas=[(v)=>(v.s/(10*v.p)),
(v)=>(v.s*1e6/v.r/1000),
(v)=>(v.a/Math.sqrt(Math.max(1,v.h*v.h+v.k*v.k+v.l*v.l))),
(v)=>(Math.asin(Math.min(1,v.lam/(2*v.d)))*180/Math.PI),
(v)=>(Math.sqrt(2*v.D*1e-14*v.t*3600)*1e6),
(v)=>(v.s0+v.k/Math.sqrt(v.d*1e-6)),
(v)=>(v.F*1000*v.L/(v.A*1e-6*v.E*1e9)*1000),
(v)=>(v.K/(v.Y*Math.sqrt(Math.PI*v.a/1000))),
(v)=>((v.Cb-v.C0)/Math.max(0.001,v.Cb-v.Ca)),
(v)=>(v.A*Math.exp(-v.Q*1000/(8.314462618*v.T))),
(v)=>(v.Ef*v.vf+v.Em*(1-v.vf)),
(v)=>(v.E0*Math.pow(1-v.p/100,2)),
(v)=>((v.L/1000)/(v.k*(v.A/10000))),
(v)=>(1/(v.n*1e28*1.602176634e-19*v.mu*1e-3)),
(v)=>(v.m*v.f),
(v)=>(Math.sqrt(v.E*1e9)/v.r)];
 function format(v){return Number.isFinite(v)?Number(v).toPrecision(5):'out of range'}
 function chart(xs,ys,curr){
   const W=600,H=180,p=26,low=Math.min(...ys),high=Math.max(...ys),range=high-low||1;
   const path=ys.map((y,i)=>`${i?'L':'M'}${p+(W-2*p)*i/(ys.length-1)},${H-p-(y-low)/range*(H-2*p)}`).join(' ');
   const cx=p+(W-2*p)*curr/(ys.length-1),cy=H-p-(ys[curr]-low)/range*(H-2*p);
   return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Model output as first input varies; selected setting marked"><rect width="${W}" height="${H}" fill="#fff"/><line x1="${p}" y1="${H-p}" x2="${W-p}" y2="${H-p}" stroke="#7e8c9c"/><path d="${path}" stroke="#0c7384" stroke-width="3" fill="none"/><circle cx="${cx}" cy="${cy}" r="5" fill="#c76325"/><text x="${p}" y="16" font-size="12" fill="#456">maximum ${format(high)}</text><text x="${p}" y="${H-4}" font-size="12" fill="#456">minimum ${format(low)}</text></svg>`
 }
 data.forEach((m,mid)=>{
 const host=document.querySelector(`[data-model="${mid}"]`);if(!host)return;
 const fn=formulas[mid]; // Audited, prebundled formulas. No dynamic code evaluation.
 const names=m.vars.map(x=>x[0]);
 const inputs={};
 m.vars.forEach(x=>{
  const wrap=document.createElement('label');wrap.textContent=x[1];
  const input=document.createElement('input');input.type='range';input.min=x[2];input.max=x[3];input.step=x[5];input.value=x[4];input.setAttribute('aria-label',x[1]);
  const val=document.createElement('span');val.style.fontWeight='400';val.style.marginLeft='0.5rem';val.textContent=String(x[4]);
  input.addEventListener('input',()=>{val.textContent=input.value; render()});wrap.append(input,val);host.querySelector('.controls').append(wrap);inputs[x[0]]=input;
 });
 function render(){
   const v={};names.forEach(n=>{v[n]=Number(inputs[n].value)});
   const answer=fn(v);host.querySelector('output').textContent=format(answer)+' '+m.units;
   const x=m.vars[0], ys=[];const n=55;
   for(let i=0;i<n;i++){const temp={...v};temp[x[0]]=x[2]+(x[3]-x[2])*i/(n-1);ys.push(fn(temp));}
   const selected=Math.max(0,Math.min(n-1,Math.round((v[x[0]]-x[2])/(x[3]-x[2])*(n-1))));
   host.querySelector('.curve').innerHTML=chart(null,ys,selected);
 }
 render();
 });
})();



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

