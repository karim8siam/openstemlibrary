/* Concrete Technology Interactive Simulation Suite */
(function(window) {
  'use strict';

  var F = function(n, d) { d = (d === undefined) ? 2 : d; return Number.isFinite(n) ? Number(n).toFixed(d) : '—'; };

  const base={
 grading:{title:'Aggregate grading blend',unit:1,subtitle:'Mass-weighted passing curves, not a segregation predictor.',inputs:[['sand','Sand fraction',0.42,0.20,0.75,0.01,'fraction'],['fines','Fine-aggregate passing adjustment',0, -12,12,1,'percentage points'],['coarse','Coarse passing adjustment',0,-12,12,1,'percentage points']],formula:'Pblend(sieve)=fsand·Psand+(1−fsand)·Pcoarse',caveat:'Demonstrates blending only. Packing, workability and specifications require separate evidence.'},
 hydration:{title:'Hydration kinetics (illustrative)',unit:2,subtitle:'A calibrated-style curve, not a universal cement model.',inputs:[['rate','Illustrative rate coefficient',0.085,0.02,0.2,0.005,'1/day'],['shape','Growth exponent',1.2,0.6,2.1,0.05,'—'],['limit','Asymptotic reacted fraction',0.85,0.60,0.98,0.01,'fraction']],formula:'α(t)=α∞[1−exp(−(k t)^n)]',caveat:'The parameters are hypothetical and must be fitted to actual binder measurements.'},
 maturity:{title:'Temperature-time maturity',unit:2,subtitle:'Nurse–Saul index under a synthetic daily temperature cycle.',inputs:[['temp','Mean temperature',24,4,42,1,'°C'],['swing','Daily temperature amplitude',6,0,14,1,'°C'],['datum','Datum temperature',-10,-15,10,1,'°C']],formula:'M=Σ max(Taverage−Tdatum,0)·Δt',caveat:'Strength cannot be inferred from maturity without a mixture-specific calibration.'},
 heat:{title:'Heat of hydration: lumped thermal model',unit:2,subtitle:'Competing heat release and simplified thermal loss.',inputs:[['binder','Binder mass',380,250,650,10,'kg/m³'],['total','Reaction heat (assumed)',230,100,370,5,'kJ/kg'],['loss','Cooling factor',0.060,0.01,0.20,0.005,'1/hour']],formula:'dT/dt=[H·m·g(t)]/(ρc)−h(T−Tamb), g(t)=exp(−t/τ)/τ',caveat:'Uniform-temperature lumped model; not suitable for temperature-gradient or crack design.'},
 rheology:{title:'Bingham flow-curve explorer',unit:3,subtitle:'Distinguish yield stress from plastic viscosity in a fluid-like approximation.',inputs:[['tau','Yield stress',80,10,250,5,'Pa'],['mu','Plastic viscosity',16,3,55,1,'Pa·s'],['rate','Selected shear rate',5,0.5,20,0.5,'1/s']],formula:'τ=τy+μp·γ̇ (for yielded flow)',caveat:'Fresh concrete may be thixotropic and non-Bingham; this is a simplified flow model, not a slump predictor.'},
 yield:{title:'Absolute-volume mix balance',unit:4,subtitle:'Convert masses to absolute volumes and check nominal batch yield.',inputs:[['water','Mixing water',170,120,240,5,'kg/m³'],['binder','Total binder',360,250,550,5,'kg/m³'],['sand','SSD sand',800,550,1000,10,'kg/m³']],formula:'Vyield=Σ(mi/ρi)+Vair; densities assumed (binder 3100, sand 2650, stone 2700 kg/m³)',caveat:'Demonstration assumes stone 1020 kg/m³, air 2%, and SSD conditions; verify actual densities.'},
 moisture:{title:'SSD aggregate moisture correction',unit:4,subtitle:'Convert specified SSD mass to actual wet mass and adjust added water.',inputs:[['ssd','Target SSD sand mass',800,400,1200,10,'kg'],['abs','Absorption',1,0.2,3.5,0.1,'% dry'],['wet','Measured total moisture',4,0,9,0.25,'% dry']],formula:'Mdry=MSSD/(1+A); Mwet=Mdry(1+T); Wsurface=Mdry(T−A)',caveat:'Moisture and absorption percentages use oven-dry mass; negative surface water implies absorption from mixture.'},
 wc:{title:'Water-to-binder and strength sensitivity',unit:4,subtitle:'Compare a hypothetical locally fitted strength curve.',inputs:[['ratio','Water / binder',0.48,0.28,0.70,0.01,'ratio'],['ref','Reference strength at w/cm 0.50',30,20,60,1,'MPa'],['power','Fitted sensitivity exponent',1.6,0.8,2.5,0.1,'—']],formula:'f28=fref·(0.50/(w/cm))^p',caveat:'NOT a universal strength law. Trial batches and tests must calibrate every binder/aggregate system.'},
 shrinkage:{title:'Restrained shrinkage stress envelope',unit:5,subtitle:'Elastic upper-bound with simplified relaxation factor.',inputs:[['strain','Free shrinkage',350,50,850,10,'µε'],['modulus','Elastic modulus',30,15,50,1,'GPa'],['restraint','Effective restraint',0.55,0.1,1,0.05,'fraction']],formula:'σ≈E·εsh·R·(1−relaxation) (assumed 45% relaxation)',caveat:'Highly simplified elastic stress estimate; creep, cracking, gradients and reinforcement need mechanical analysis.'},
 sorptivity:{title:'Capillary uptake comparison',unit:6,subtitle:'Idealized initial sorptivity, I=S·√t.',inputs:[['s','Sorptivity coefficient',1.1,0.2,3,0.1,'mm/√hour'],['time','Exposure duration',24,1,96,1,'hours'],['factor','Curing-improvement multiplier',0.75,0.4,1.3,0.05,'fraction']],formula:'I(t)=S·√t; comparison Icuring(t)=factor·S·√t',caveat:'Early-time sorptivity approximation; not hydraulic permeability and not a measured curing multiplier.'},
 carbonation:{title:'Carbonation front vs reinforcement cover',unit:6,subtitle:'Square-root-of-time depth, hypothetical exposure coefficient.',inputs:[['k','Carbonation coefficient',3,0.5,9,0.25,'mm/√year'],['age','Age',20,1,90,1,'years'],['cover','Nominal cover',35,15,80,1,'mm']],formula:'x=k·√t; nominal intersection time=(cover/k)²',caveat:'Front position is not proof of corrosion. k, cover and exposure are uncertain and need field calibration.'},
 chloride:{title:'Idealized chloride diffusion profile',unit:6,subtitle:'Constant surface concentration and effective diffusivity (Fickian).',inputs:[['D','Effective D',22,4,100,2,'mm²/year'],['age','Exposure duration',20,1,70,1,'years'],['cs','Surface chloride concentration',0.8,0.2,2,0.05,'% binder']],formula:'C(x,t)=Cs·erfc[x/(2√(D·t))]',caveat:'Diffusivity and Cs are fixed illustrative values; not a service-life or corrosion-initiation design model.'},
 qc:{title:'Strength test series and variability',unit:7,subtitle:'Check dispersion independently from a project acceptance rule.',inputs:[['mean','Underlying target mean',39,24,65,1,'MPa'],['sd','Batch and test variability',3,0.5,9,0.25,'MPa'],['shift','Production mean shift',-1,-8,8,0.5,'MPa']],formula:'xi=μ+Δ+σ·zi for fixed synthetic standardized offsets; s=sqrt(Σ(xi−x̄)²/(n−1))',caveat:'These synthetic results illustrate monitoring; they do not encode acceptance under ACI, ASTM or local codes.'},
 carbon:{title:'Binder embodied CO₂e scenario',unit:8,subtitle:'One narrow production-stage accounting boundary.',inputs:[['replace','SCM replacement by mass',25,0,65,1,'%'],['binder','Total binder',400,260,600,10,'kg/m³'],['cementEF','Cement factor',0.85,0.45,1.2,0.025,'kgCO₂e/kg']],formula:'E=(binder·(1−r))·EFcement+(binder·r)·EFscm, EFscm=0.12 assumed',caveat:'Illustrative factors, not verified EPDs. Excludes transport, aggregate, construction, service life and end of life.'}
};
function erf(x){let s=Math.sign(x);x=Math.abs(x);const t=1/(1+0.3275911*x);const y=1-(((((1.061405429*t-1.453152027)*t)+1.421413741)*t-0.284496736)*t+0.254829592)*t*Math.exp(-x*x);return s*y;}
function solve(id,v){let arr=[],main='',secondary='',xLab='',yLab='';const push=(x,y)=>arr.push([x,y]);
 if(id==='grading'){let sieves=[0.15,0.3,0.6,1.18,2.36,4.75,9.5,19],a=[4,11,28,53,80,97,100,100],b=[0,0,0,1,3,6,42,94];sieves.forEach((s,i)=>push(s,v.sand*Math.max(0,Math.min(100,a[i]+v.fines))+(1-v.sand)*Math.max(0,Math.min(100,b[i]+v.coarse))));main=`Blended passing at 4.75 mm: ${F(arr[5][1])}%`;secondary=`Sand ${F(v.sand*100,0)}% + coarse ${F((1-v.sand)*100,0)}% (dry mass)`;xLab='Sieve opening (mm)';yLab='Passing (%)';}
 if(id==='hydration'){for(let t=0;t<=56;t++)push(t,100*v.limit*(1-Math.exp(-Math.pow(v.rate*t,v.shape))));main=`Day 28 reacted fraction: ${F(arr[28][1],1)}%`;secondary='Day 7: '+F(arr[7][1],1)+'%; day 56: '+F(arr[56][1],1)+'%';xLab='Age (days)';yLab='Illustrative reacted fraction (%)';}
 if(id==='maturity'){let m=0;for(let h=0;h<=72;h++){if(h>0){const T=v.temp+v.swing*Math.sin(2*Math.PI*(h-.5)/24);m+=Math.max(0,T-v.datum);}push(h,m);}main=`72-hour maturity: ${F(m,0)} °C·h`;secondary=`Mean ${v.temp} °C, datum ${v.datum} °C; hourly summation`;xLab='Time (hours)';yLab='Maturity (°C·h)';}
 if(id==='heat'){const tau=40, ambient=24,cap=2400;let T=ambient;for(let h=0;h<=168;h++){push(h,T); const power=v.binder*v.total/tau*Math.exp(-h/tau); T+=(power/cap)-v.loss*(T-ambient);}main=`Peak simulated temperature: ${F(Math.max(...arr.map(x=>x[1])))} °C`;secondary=`Adiabatic upper-bound rise: ${F(v.binder*v.total/2400)} °C`;xLab='Time (hours)';yLab='Uniform concrete temperature (°C)';}
 if(id==='rheology'){for(let g=0;g<=20;g+=0.5)push(g,v.tau+v.mu*g);main=`Stress at selected rate: ${F(v.tau+v.mu*v.rate,1)} Pa`;secondary=`τy = ${F(v.tau,0)} Pa; μp = ${F(v.mu,1)} Pa·s`;xLab='Shear rate (1/s)';yLab='Shear stress (Pa)';}
 if(id==='yield'){const c=1020,air=.02,calc=w=>w/1000+v.binder/3100+v.sand/2650+c/2700+air;for(let w=120;w<=240;w+=3)push(w,calc(w));main=`Predicted absolute yield: ${F(calc(v.water),3)} m³`;secondary=`w/cm = ${F(v.water/v.binder,3)}; yield discrepancy ${F((calc(v.water)-1)*100,1)}%`;xLab='Added water (kg)';yLab='Volume total (m³)';}
 if(id==='moisture'){const dry=v.ssd/(1+v.abs/100);const surf=dry*(v.wet-v.abs)/100;for(let t=0;t<=9;t+=0.25)push(t,dry*(t-v.abs)/100);main=`Batch wet sand: ${F(dry*(1+v.wet/100),1)} kg`;secondary=`Sand contribution to mixing water: ${F(surf,1)} kg (negative means uptake)`;xLab='Actual total moisture (% dry)';yLab='Water correction (kg)';}
 if(id==='wc'){let f=r=>v.ref*Math.pow(.5/r,v.power);for(let r=.28;r<=.70;r+=.01)push(r,f(r));main=`Illustrative 28-day strength: ${F(f(v.ratio))} MPa`;secondary=`This is a scenario comparison, not a validated mixture prediction.`;xLab='w/cm';yLab='Modeled strength (MPa)';}
 if(id==='shrinkage'){let stress=e=>v.modulus*1000*e*1e-6*v.restraint*.55;for(let e=0;e<=850;e+=25)push(e,stress(e));main=`Nominal restrained tension: ${F(stress(v.strain))} MPa`;secondary=`Assumes 45% stress relaxation and ${F(v.restraint*100,0)}% effective restraint`;xLab='Free shrinkage (µε)';yLab='Calculated elastic stress (MPa)';}
 if(id==='sorptivity'){for(let t=0;t<=96;t+=2)push(t,v.s*v.factor*Math.sqrt(t));main=`Uptake at ${v.time} h: ${F(v.s*v.factor*Math.sqrt(v.time))} mm`;secondary=`Unmodified uptake ${F(v.s*Math.sqrt(v.time))} mm`;xLab='Time (hours)';yLab='Equivalent uptake (mm)';}
 if(id==='carbonation'){for(let y=0;y<=100;y++)push(y,v.k*Math.sqrt(y));main=`Front depth at ${v.age} years: ${F(v.k*Math.sqrt(v.age))} mm`;secondary=`Nominal cover intersection: ${F(Math.pow(v.cover/v.k,2),1)} years`;xLab='Exposure age (years)';yLab='Carbonation depth (mm)';}
 if(id==='chloride'){let c=x=>v.cs*(1-erf(x/(2*Math.sqrt(v.D*v.age))));for(let x=0;x<=90;x+=2)push(x,c(x));main=`Concentration at 35 mm: ${F(c(35),3)} % binder`;secondary=`Penetration length 2√(Dt) = ${F(2*Math.sqrt(v.D*v.age),1)} mm`;xLab='Depth from surface (mm)';yLab='Concentration (% binder)';}
 if(id==='qc'){let z=[-1.4,-0.7,0.4,0.2,1.0,-0.4,1.5,-0.9,0.1,0.6,-1.1,0.8,-0.2,0.9,-0.6,0.4];z.forEach((q,i)=>push(i+1,v.mean+v.shift+v.sd*q));let a=arr.map(p=>p[1]),avg=a.reduce((p,q)=>p+q,0)/a.length,sd=Math.sqrt(a.reduce((p,q)=>p+(q-avg)**2,0)/(a.length-1));main=`Series mean: ${F(avg)} MPa`;secondary=`Sample standard deviation ${F(sd)} MPa (n=${a.length})`;xLab='Specimen result index';yLab='Compressive strength (MPa)';}
 if(id==='carbon'){let e=r=>v.binder*((1-r/100)*v.cementEF+(r/100)*.12);for(let r=0;r<=65;r+=1)push(r,e(r));main=`Binder-stage CO₂e: ${F(e(v.replace),1)} kg/m³`;secondary=`Difference vs same-binder all-cement reference: ${F(e(0)-e(v.replace),1)} kg/m³`;xLab='SCM replacement by mass (%)';yLab='Binder CO₂e (kg/m³)';}
 return {arr,main,secondary,xLab,yLab};
}
function ssvg(points,xlabel,ylabel){const W=780,H=344,L=72,R=20,T=18,B=62;let xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);let minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(...ys),maxY=Math.max(...ys);if(minY>0)minY=0;if(maxY===minY)maxY=minY+1;let pad=(maxY-minY)*.08;maxY+=pad;minY-=pad*.3;const xp=x=>L+(x-minX)/(maxX-minX)*(W-L-R),yp=y=>T+(maxY-y)/(maxY-minY)*(H-T-B);let line=points.map((p,i)=>(i?'L':'M')+xp(p[0]).toFixed(2)+' '+yp(p[1]).toFixed(2)).join(' ');let grid='';for(let i=0;i<=5;i++){let yy=T+(H-T-B)*i/5,val=maxY-(maxY-minY)*i/5;grid+=`<line x1="${L}" x2="${W-R}" y1="${yy}" y2="${yy}" stroke="#334a59" stroke-dasharray="3 5"/><text x="${L-10}" y="${yy+4}" text-anchor="end" font-size="12" fill="#a7b9c8">${F(val,Math.abs(val)<1?2:1)}</text>`;}for(let i=0;i<=4;i++){let xx=L+(W-L-R)*i/4,val=minX+(maxX-minX)*i/4;grid+=`<text x="${xx}" y="${H-B+18}" text-anchor="middle" font-size="12" fill="#a7b9c8">${F(val,Math.abs(val)<1?2:1)}</text>`;}
return `<svg role="img" aria-label="${xlabel} versus ${ylabel}" viewBox="0 0 ${W} ${H}">${grid}<path d="${line}" fill="none" stroke="#6be3cb" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><text x="${W/2}" y="${H-12}" fill="#dcebf4" font-size="14" text-anchor="middle">${xlabel}</text><text x="19" y="${H/2}" fill="#dcebf4" font-size="13" text-anchor="middle" transform="rotate(-90 19 ${H/2})">${ylabel}</text></svg>`;
}


  var MODELS = [];
  var modelKeys = Object.keys(base);

  modelKeys.forEach(function(key, idx) {
    var mDef = base[key];
    var unit = mDef.unit;

    var controlsHtml = mDef.inputs.map(function(inp) {
      var pid = inp[0], label = inp[1], def = inp[2], min = inp[3], max = inp[4], step = inp[5], unitStr = inp[6];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ct_' + key + '_' + pid + '">' + label + ' <span id="v_ct_' + key + '_' + pid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="ct_' + key + '_' + pid + '" data-pid="' + pid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.subtitle + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">' +
                 '<div class="stat-box" id="stat-main" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">Primary Metric</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">—</output></div>' +
                 '<div class="stat-box" id="stat-sec" style="background:#f1f5f9;border-left:4px solid #64748b;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">Reference Balance</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">—</output></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="equation" style="font-family:monospace;font-size:0.875rem;background:#f1f5f9;padding:0.75rem;border-radius:6px;margin-top:0.75rem;color:#0f172a;">Formula: ' + mDef.formula + '</div>' +
               '<p class="caveat" style="font-size:0.8125rem;color:#475569;margin-top:0.5rem;font-style:italic;">Caveat: ' + mDef.caveat + '</p>';

    MODELS.push({
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {
        try {
          var v = {};
          mDef.inputs.forEach(function(inp) { v[inp[0]] = inp[2]; });
          var plotEl = card.querySelector('.plot');
          var mainStat = card.querySelector('#stat-main output');
          var secStat = card.querySelector('#stat-sec output');

          function updateCT() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pid = inp.dataset.pid;
              v[pid] = Number(inp.value);
              var lbl = card.querySelector('#v_ct_' + key + '_' + pid);
              if (lbl) lbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            });

            var res = solve(key, v);
            if (plotEl && res.arr) plotEl.innerHTML = ssvg(res.arr, res.xLab, res.yLab);
            if (mainStat) mainStat.textContent = res.main;
            if (secStat) secStat.textContent = res.secondary;
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateCT);
          });
          updateCT();
        } catch (err) {
          console.warn('Concrete Technology sim error in model ' + key + ':', err);
        }
      }
    });
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
