/* Cell Biology Interactive Simulation Suite */
"use strict";
(function(global){
  const definitions = [{"unit": "fold", "name": "Population doubling", "key": "doubling", "xlabel": "Elapsed time (h)", "xmin": 0, "xmax": 12, "xinit": 4, "plabel": "Doubling interval (h)", "pmin": 0.5, "pmax": 4, "pinit": 1.5, "unitName": "fold", "limit": "Ideal exponential growth without carrying capacity or death"}, {"unit": "nm", "name": "Diffraction resolution", "key": "resolution", "xlabel": "Wavelength (nm)", "xmin": 400, "xmax": 700, "xinit": 550, "plabel": "Numerical aperture", "pmin": 0.4, "pmax": 1.4, "pinit": 1.2, "unitName": "nm", "limit": "Rayleigh-scale idealization for ordinary diffraction-limited imaging"}, {"unit": "normalized flux", "name": "Passive diffusive flux", "key": "diffusion", "xlabel": "External concentration (mM)", "xmin": 0, "xmax": 20, "xinit": 12, "plabel": "Internal concentration (mM)", "pmin": 0, "pmax": 20, "pinit": 4, "unitName": "normalized flux", "limit": "Constant permeability for neutral solute; signed flux direction"}, {"unit": "mV", "name": "Nernst voltage", "key": "nernst", "xlabel": "External concentration (mM)", "xmin": 1, "xmax": 150, "xinit": 5, "plabel": "Internal concentration (mM)", "pmin": 1, "pmax": 150, "pinit": 140, "unitName": "mV", "limit": "Monovalent cation, ideal activities, 37 °C; not total membrane voltage"}, {"unit": "mV", "name": "Proton motive-force magnitude", "key": "pmf", "xlabel": "Electrical potential magnitude (mV)", "xmin": 50, "xmax": 220, "xinit": 150, "plabel": "pH difference", "pmin": 0, "pmax": 2, "pinit": 0.8, "unitName": "mV", "limit": "Aligned magnitude convention, 37 °C; not directly ATP yield"}, {"unit": "% delivered", "name": "Two-stage cargo transfer", "key": "traffic", "xlabel": "Elapsed time (min)", "xmin": 0, "xmax": 20, "xinit": 10, "plabel": "Stage rate (min⁻¹)", "pmin": 0.05, "pmax": 1, "pinit": 0.2, "unitName": "% delivered", "limit": "Two irreversible sequential exponential stages, equal rate and no recycling"}, {"unit": "% occupied", "name": "Single-site receptor occupancy", "key": "receptor", "xlabel": "Ligand concentration (nM)", "xmin": 0, "xmax": 100, "xinit": 24, "plabel": "Dissociation constant Kd (nM)", "pmin": 1, "pmax": 100, "pinit": 8, "unitName": "% occupied", "limit": "Equilibrium independent sites; occupancy is not necessarily signal output"}, {"unit": "response", "name": "Negative-feedback steady state", "key": "feedback", "xlabel": "Normalized input", "xmin": 0, "xmax": 10, "xinit": 6, "plabel": "Feedback gain k", "pmin": 0, "pmax": 5, "pinit": 2, "unitName": "response", "limit": "Production u/(1+kx), first-order removal x; nonnegative steady state"}, {"unit": "% time", "name": "Single-cell S-phase allocation", "key": "cycle", "xlabel": "S-phase duration (h)", "xmin": 1, "xmax": 18, "xinit": 8, "plabel": "G1 duration (h)", "pmin": 1, "pmax": 22, "pinit": 9, "unitName": "% time", "limit": "One trajectory with fixed G2=3 h and M=1 h, not population phase fraction"}, {"unit": "% probability", "name": "At-least-one segregation error", "key": "segregation", "xlabel": "Observed divisions", "xmin": 1, "xmax": 1000, "xinit": 40, "plabel": "Error probability per division", "pmin": 0, "pmax": 0.2, "pinit": 0.01, "unitName": "% probability", "limit": "Independent Bernoulli trials with one detectable class of error"}, {"unit": "seconds", "name": "Ideal slip-bond lifetime", "key": "bond", "xlabel": "Tensile force (pN)", "xmin": 0, "xmax": 30, "xinit": 10, "plabel": "Bond-distance scale (nm)", "pmin": 0.1, "pmax": 1.5, "pinit": 0.4, "unitName": "seconds", "limit": "Slip bond with kBT=4.1 pN nm and 100-s zero-force lifetime"}, {"unit": "µm", "name": "Random-migration RMS distance", "key": "randomwalk", "xlabel": "Elapsed time (min)", "xmin": 0, "xmax": 120, "xinit": 25, "plabel": "Motility D (µm²/min)", "pmin": 0.05, "pmax": 2, "pinit": 0.8, "unitName": "µm", "limit": "Unbiased two-dimensional diffusive limit; not path length"}, {"unit": "% output", "name": "Normalized stress-response switch", "key": "apoptosis", "xlabel": "Stress input", "xmin": 0, "xmax": 10, "xinit": 4, "plabel": "Threshold K", "pmin": 1, "pmax": 9, "pinit": 3, "unitName": "% output", "limit": "Hill exponent 4; modeled response, not calibrated death probability"}, {"unit": "% remaining", "name": "First-order cargo clearance", "key": "clearance", "xlabel": "Elapsed time (h)", "xmin": 0, "xmax": 20, "xinit": 9, "plabel": "Cargo half-life (h)", "pmin": 1, "pmax": 10, "pinit": 3, "unitName": "% remaining", "limit": "Well-mixed first-order pool, ignores cargo formation and lysosomal saturation"}, {"unit": "% normalized", "name": "FRAP recovery", "key": "frap", "xlabel": "Recovery time (s)", "xmin": 0, "xmax": 120, "xinit": 25, "plabel": "Recovery rate (s⁻¹)", "pmin": 0.005, "pmax": 0.1, "pinit": 0.035, "unitName": "% normalized", "limit": "Single-exponential recovery to 100% mobile fraction; geometry omitted"}, {"unit": "% gated", "name": "Illustrative gating fraction", "key": "gating", "xlabel": "Gate threshold (normalized)", "xmin": -3, "xmax": 3, "xinit": 0, "plabel": "Population mean", "pmin": -2, "pmax": 2, "pinit": 0.5, "unitName": "% gated", "limit": "Logistic-distributed toy marker intensity with unit scale, not actual flow data"}];
  const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
  function value(id,x,p){
    if(typeof x!=="number" || typeof p!=="number" || !Number.isFinite(x) || !Number.isFinite(p))throw new TypeError("Nonfinite model input");
    const d=definitions.find(z=>z.key===id);if(!d)throw new Error("Unknown model: "+id);
    if(x<d.xmin||x>d.xmax||p<d.pmin||p>d.pmax)throw new RangeError("Outside the documented model range");
    switch(id){
      case "doubling": return Math.pow(2,x/p);
      case "resolution": return .61*x/p;
      case "diffusion": return .1*(x-p);
      case "nernst": return 26.7*Math.log(x/p);
      case "pmf": return x+59.5*p;
      case "traffic": {const z=x*p;return 100*(1-(1+z)*Math.exp(-z));}
      case "receptor": return 100*x/(p+x);
      case "feedback": return p===0?x:2*x/(1+Math.sqrt(1+4*p*x));
      case "cycle": return 100*x/(x+p+4);
      case "segregation": return 100*(-Math.expm1(x*Math.log1p(-p)));
      case "bond": return 100*Math.exp(-x*p/4.1);
      case "randomwalk":return Math.sqrt(4*p*x);
      case "apoptosis":return 100*Math.pow(x,4)/(Math.pow(p,4)+Math.pow(x,4));
      case "clearance": return 100*Math.pow(2,-x/p);
      case "frap": return 100*(-Math.expm1(-x*p));
      case "gating":return 100/(1+Math.exp(x-p));
    }
  }
  function schematicSvg(id,x,p,y){
    const cell=(cx,cy,col='#7dd3fc',radius=9)=>`<ellipse cx="${cx}" cy="${cy}" rx="${radius}" ry="${radius*.75}" fill="${col}" stroke="#d7f1ff" stroke-width="1"/>`;
    const txt=(x,y,v,sz=13)=>`<text x="${x}" y="${y}" font-size="${sz}" fill="#e2f3ff">${v}</text>`;
    let shapes='', caption='';
    if(id==='doubling'){
       const n=Math.min(28,Math.max(1,Math.round(y)));
       for(let i=0;i<n;i++)shapes+=cell(30+(i%14)*40,45+Math.floor(i/14)*47,'#34d399',10);
       caption='Illustrative visible cells (capped at 28), not literal population scale';
    }else if(id==='diffusion'){
       shapes+='<path d="M298 5 V102" stroke="#fbbf24" stroke-width="13" stroke-dasharray="4 4"/>';
       let a=Math.round(Math.min(16,x)),b=Math.round(Math.min(16,p));
       for(let i=0;i<a;i++)shapes+=cell(23+(i%8)*29,28+Math.floor(i/8)*37,'#7dd3fc',5);
       for(let i=0;i<b;i++)shapes+=cell(360+(i%8)*29,28+Math.floor(i/8)*37,'#fb7185',5);
       shapes+=txt(220,118, y>=0?'net inward →':'← net outward',15);
       caption='Two pools separated by an idealized membrane; particles represent relative concentrations';
    }else if(id==='traffic'){
       const z=x*p,P0=100*Math.exp(-z),P1=100*z*Math.exp(-z),P2=y;
       for(const [i,label,val,col] of [[0,'Initial',P0,'#7dd3fc'],[1,'Intermediate',P1,'#fbbf24'],[2,'Delivered',P2,'#34d399']]){
         shapes+=`<rect x="${25+i*195}" y="30" width="${Math.max(0,Math.min(155,val*1.55))}" height="35" fill="${col}" rx="4"/>`+txt(25+i*195,23,label)+txt(25+i*195,90,val.toFixed(1)+'%');
       }caption='Sequential cargo compartments; three fractions sum to approximately 100%';
    }else if(id==='receptor'){
       for(let i=0;i<24;i++)shapes+=`<rect x="${12+i*24}" y="40" rx="5" width="17" height="33" stroke="#d7f1ff" fill="${i<Math.round(24*y/100)?'#34d399':'#2a415e'}"/>`;
       caption='Twenty-four schematic receptor sites; green indicates the modeled occupied fraction';
    }else if(id==='cycle'){
       const lengths=[p,x,3,1],names=['G1','S','G2','M'],cols=['#60a5fa','#34d399','#fbbf24','#f472b6'];let at=20,total=lengths.reduce((a,b)=>a+b,0);
       for(let i=0;i<4;i++){let width=550*lengths[i]/total;shapes+=`<rect x="${at}" y="41" width="${width}" height="43" fill="${cols[i]}"/>`+txt(at+4,30,names[i]);at+=width;}
       caption='One-cell timeline; segment widths are durations, not fractions from a growing population';
    }else if(id==='clearance'||id==='frap'||id==='apoptosis'){
       const frac=id==='clearance'?y/100:(id==='frap'?y/100:y/100);
       for(let i=0;i<36;i++)shapes+=cell(35+(i%12)*47,30+Math.floor(i/12)*29,i<Math.round(frac*36)?'#34d399':'#405370',8);
       caption=id==='clearance'?'Green marks hypothetical remaining cargo':id==='frap'?'Green marks hypothetical recovered fluorescence':'Green marks modeled normalized response, not actual dying cells';
    }else if(id==='bond'){
       shapes+='<path d="M70 70 H520" stroke="#38bdf8" stroke-width="7"/><path d="M70 55 L35 70 L70 85 M520 55 L555 70 L520 85" fill="none" stroke="#fbbf24" stroke-width="4"/>';
       shapes+=txt(180,40,'τ = '+y.toFixed(1)+' s at '+x.toFixed(1)+' pN');
       caption='Force applied to a single idealized slip bond, not a complete cellular adhesion';
    }else{return '';}
    return `<svg role="img" aria-label="Illustrative cell-biology schematic for ${id}" viewBox="0 0 610 142" xmlns="http://www.w3.org/2000/svg"><title>Schematic demonstration</title><rect width="610" height="142" rx="10" fill="#0c1627"/>${shapes}${txt(12,132,caption,10)}</svg>`;
  }

  function buildCard(element,modelId){
    const d=definitions.find(s=>s.key===modelId);if(!d)throw new Error(modelId);
    element.classList.add("simulator");element.innerHTML='';
    const heading=document.createElement('h4');heading.textContent=d.name;element.appendChild(heading);
    const aside=document.createElement('p');aside.className='sim-limit';aside.textContent='Model assumption: '+d.limit;element.appendChild(aside);
    const controls=document.createElement('div');controls.className='control-grid';element.appendChild(controls);
    const mk=(label,min,max,val,id)=>{
      const wrap=document.createElement('label');wrap.className='control';wrap.textContent=label;
      const txt=document.createElement('output');txt.id=id+'-display';txt.textContent=String(val);wrap.appendChild(txt);
      const r=document.createElement('input');r.type='range';r.id=id;r.min=min;r.max=max;
      r.step=(max-min)<=1?'0.001':(max-min)<=10?'0.01':'0.1';r.value=val;
      r.setAttribute('aria-label',label);wrap.appendChild(r);controls.appendChild(wrap);return {r,txt,val};
    };
    const a=mk(d.xlabel,d.xmin,d.xmax,d.xinit,'x-'+modelId),b=mk(d.plabel,d.pmin,d.pmax,d.pinit,'p-'+modelId);
    const readout=document.createElement('p');readout.className='sim-readout';readout.setAttribute('aria-live','polite');element.appendChild(readout);
    const fig=document.createElement('div');fig.className='figure';element.appendChild(fig);
    const sketch=document.createElement('div');sketch.className='figure schematic';element.appendChild(sketch);
    const reset=document.createElement('button');reset.type='button';reset.className='secondary';reset.textContent='Reset model';element.appendChild(reset);
    let count=0;
    function draw(){
      const xv=Number(a.r.value),pv=Number(b.r.value);a.txt.textContent=xv.toPrecision(4);b.txt.textContent=pv.toPrecision(4);
      const current=value(modelId,xv,pv);readout.textContent='Predicted output: '+Number(current.toPrecision(6))+' '+d.unit;
      const vals=[];for(let i=0;i<=64;i++){const x=d.xmin+(d.xmax-d.xmin)*i/64;vals.push(value(modelId,x,pv));}
      let low=Math.min(...vals,current),high=Math.max(...vals,current);if(Math.abs(high-low)<1e-12){high+=1;low-=1;}
      const fx=i=>55+535*i/64, fy=v=>185-145*(v-low)/(high-low);
      const path=vals.map((v,i)=>(i?'L':'M')+fx(i).toFixed(2)+' '+fy(v).toFixed(2)).join(' ');
      const xdot=55+535*(xv-d.xmin)/(d.xmax-d.xmin);
      const ydot=fy(current);
      fig.innerHTML='<svg role="img" aria-label="Interactive curve for '+d.name+'; marker is current choice" viewBox="0 0 620 230" xmlns="http://www.w3.org/2000/svg"><title>'+d.name+' model output</title><rect x="0" y="0" width="620" height="230" fill="#0c1627" rx="8"/><path d="M55 25 V185 H590" stroke="#7f8ba4" fill="none" stroke-width="1.2"/><path d="'+path+'" stroke="#38bdf8" fill="none" stroke-width="3"/><circle cx="'+xdot.toFixed(2)+'" cy="'+ydot.toFixed(2)+'" r="5.8" fill="#fbbf24" stroke="#fff" stroke-width="1.2"/><text x="55" y="207" fill="#d6e7f7" font-size="13">'+d.xmin+'</text><text x="568" y="207" fill="#d6e7f7" font-size="13">'+d.xmax+'</text><text x="18" y="33" fill="#d6e7f7" font-size="12">'+Number(high.toPrecision(3))+'</text><text x="18" y="183" fill="#d6e7f7" font-size="12">'+Number(low.toPrecision(3))+'</text><text x="240" y="225" fill="#d6e7f7" font-size="12">'+d.xlabel+'</text></svg>';
      sketch.innerHTML=schematicSvg(modelId,xv,pv,current);
      element.dataset.renders=String(++count);
    }
    a.r.addEventListener('input',draw);b.r.addEventListener('input',draw);
    reset.addEventListener('click',()=>{a.r.value=d.xinit;b.r.value=d.pinit;draw();});draw();
  }
  const api={definitions,value,buildCard};global.CellModels=api;
  root.OpenSTEMCellSims = api; if(typeof module!=='undefined'&&module.exports)module.exports=api;
  if(typeof document!=='undefined')document.addEventListener('DOMContentLoaded',()=>document.querySelectorAll('[data-cell-model]').forEach(el=>buildCard(el,el.dataset.cellModel)));
})(typeof window==='undefined'?globalThis:window);



/* SimulationEngine adapter for Cell Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (root.OpenSTEMCellSims && root.OpenSTEMCellSims.buildCard) {
      root.OpenSTEMCellSims.buildCard(host, simType);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

