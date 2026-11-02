/* Foundation Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  var PI = Math.PI;
  var n = function(a, b, N) { N = N || 51; return Array.from({length: N}, function(_, i) { return a + (b - a) * i / (N - 1); }); };
  var safe = function(x) { return Number.isFinite(x) ? x : 0; };
  var series = function(label, values) { return {label: label, values: values.map(safe)}; };
  var fmt = function(v, d) { d = (d === undefined) ? 3 : d; return Number.isFinite(v) ? Number(v.toFixed(d)).toLocaleString('en-US') : '—'; };

  function solve(id,p){let xs=[],lines=[],met=[],yLabel='',xLabel='', warning='';
switch(id){
case 'investigation': {
 xs=n(0,p.spacing,81);const arr=xs.map(x=>{let near=Math.min(x,p.spacing-x);return p.variability*(near/p.spacing)*100+p.bias*Math.exp(-(((x-0.62*p.spacing)/(p.spacing/7))**2))});
 lines=[series('Illustrative uncertainty index',arr)];met=[['Max index',fmt(Math.max(...arr),1)],['Borehole spacing',fmt(p.spacing)+' m'],['Interpretation','Heuristic']];xLabel='Distance along line (m)';yLabel='Uncertainty index';break;}
case 'groundwater': {
 xs=n(0,22);let sig=xs.map(z=>p.gamman*Math.min(z,p.water)+p.gammasat*Math.max(0,z-p.water));let pore=xs.map(z=>9.81*Math.max(0,z-p.water));lines=[series('Total stress',sig),series('Pore pressure',pore),series('Effective stress',sig.map((v,i)=>v-pore[i]))];met=[['Effective stress at 20 m',fmt(p.gamman*Math.min(20,p.water)+p.gammasat*Math.max(0,20-p.water)-9.81*Math.max(0,20-p.water))+' kPa'],['Water-table depth',fmt(p.water)+' m']];xLabel='Depth (m)';yLabel='Vertical stress (kPa)';break;}
case 'bearing': {
 let ph=p.phi*PI/180,tan=Math.tan(ph),Nq=Math.exp(PI*tan)*Math.tan(PI/4+ph/2)**2,Ng=2*(Nq+1)*tan;
 xs=n(0.8,6);let val=xs.map(B=>18*p.depth*Nq+0.5*18*B*Ng);lines=[series('Idealized ultimate pressure',val)];let at=18*p.depth*Nq+0.5*18*p.width*Ng;met=[['At selected B',fmt(at)+' kPa'],['Nq',fmt(Nq,2)],['Nγ',fmt(Ng,2)],['Illustrative q/3',fmt(at/3)+' kPa']];xLabel='Footing width B (m)';yLabel='Ultimate pressure (kPa)';break;}
case 'eccentric':{
 let B=p.width,N=p.force,L=3,e=p.ecc;xs=n(-B/2,B/2,81);
 let q0=N/(B*L),qmax=0,qmin=0,contact=B;
 if(e<=B/6){qmax=q0*(1+6*e/B);qmin=q0*(1-6*e/B);lines=[series('Contact pressure',xs.map(x=>q0*(1+12*e*x/B**2)))];}
 else if(e<B/2){contact=3*(B/2-e);qmax=2*N/(contact*L);lines=[series('Contact pressure',xs.map(x=>x<B/2-contact?0:qmax*(x-(B/2-contact))/contact))];warning='Partial base contact: the compression-only approximation applies.';}
 else{lines=[series('Contact pressure',xs.map(_=>0))];warning='Applied eccentricity is outside the base; overturning, not ordinary contact, governs.'}
 met=[['Peak pressure',fmt(qmax)+' kPa'],['Minimum pressure',fmt(qmin)+' kPa'],['Contact length',fmt(contact)+' m'],['Middle-third limit',fmt(B/6)+' m']];xLabel='Base position (m)';yLabel='Normal contact stress (kPa)';break;}
case 'settlement':{
 xs=n(50,350);let coefficient=p.width*(1-.3**2)*1.12/(p.E*1000)*1000;
 lines=[series('Immediate settlement',xs.map(q=>q*coefficient))];met=[['At chosen pressure',fmt(p.pressure*coefficient)+' mm'],['Assumed E',fmt(p.E)+' MPa'],['Influence factor','1.12']];xLabel='Net pressure (kPa)';yLabel='Settlement (mm)';break;}
case 'raft':{
 xs=n(0,12,121);let W=p.spread;
 const density=(x,c)=>Math.exp(-.5*((x-c)/W)**2);const val=xs.map(x=>p.load1*density(x,3)+p.load2*density(x,9));
 const dx=xs[1]-xs[0],area=val.reduce((s,y,i)=>s+y*(i===0||i===val.length-1?.5:1),0)*dx;
 const dist=val.map(y=>y*(p.load1+p.load2)/area);
 lines=[series('Illustrative line reaction',dist)];met=[['Total applied load',fmt(p.load1+p.load2)+' kN'],['Integrated reaction',fmt(dist.reduce((s,v,i)=>s+v*(i===0||i===dist.length-1?.5:1),0)*dx)+' kN'],['Peak reaction',fmt(Math.max(...dist))+' kN/m']];xLabel='Raft position (m)';yLabel='Reaction (kN/m)';break;}
case 'rafttilt':{
 xs=n(0,10);let k=xs.map(x=>p.kl+(p.kr-p.kl)*x/10),s=k.map(v=>p.pressure/v);lines=[series('Local spring settlement',s)];met=[['Left settlement',fmt(s[0])+' mm'],['Right settlement',fmt(s.at(-1))+' mm'],['Angular distortion',fmt(Math.abs(s.at(-1)-s[0])/10000,6)+' rad']];xLabel='Raft position (m)';yLabel='Local displacement (mm)';break;}
case 'pile':{
 xs=n(0,30);let Qb=PI*p.D*p.D*p.qb/4;lines=[series('Shaft resistance',xs.map(L=>PI*p.D*L*p.fs)),series('Shaft + base',xs.map(L=>PI*p.D*L*p.fs+Qb))];met=[['At 20 m total',fmt(PI*p.D*20*p.fs+Qb)+' kN'],['Toe contribution',fmt(Qb)+' kN']];xLabel='Embedded length (m)';yLabel='Nominal axial resistance (kN)';break;}
case 'group':{
 xs=n(1,16,16);lines=[series('Group nominal',xs.map(x=>x*p.eta*p.single)),series('Unreduced sum',xs.map(x=>x*p.single))];met=[['Selected pile count',p.n],['Group nominal',fmt(p.n*p.eta*p.single)+' kN'],['Efficiency used',fmt(p.eta,2)]];xLabel='Pile count';yLabel='Resistance (kN)';break;}
case 'earth':{
 let Ka=Math.tan(PI/4-p.phi*PI/360)**2;xs=n(0,p.H,71);let soil=xs.map(z=>Ka*10*z), water=xs.map(z=>9.81*Math.max(0,z-p.water));lines=[series('Active effective-soil component',soil),series('Water component',water),series('Combined',soil.map((a,i)=>a+water[i]))];let wet=Math.max(0,p.H-p.water);met=[['Active coefficient',fmt(Ka,3)],['Total thrust',fmt(.5*Ka*10*p.H**2+.5*9.81*wet**2)+' kN/m'],['Base pressure',fmt(Ka*10*p.H+9.81*wet)+' kPa']];xLabel='Depth below surface (m)';yLabel='Lateral pressure (kPa)';break;}
case 'wall':{
 xs=n(100,900);let R=p.mu*p.W;lines=[series('Sliding resistance / thrust',xs.map(P=>R/P))];met=[['Chosen resistance',fmt(R)+' kN/m'],['Ratio at chosen thrust',fmt(R/p.P,2)],['Limitation','No partial factors applied']];xLabel='Driving earth thrust (kN/m)';yLabel='Illustrative R/P ratio';break;}
case 'heave':{
 xs=n(0,12);let strainPercent=xs.map(w=>p.coeff*w),heave=strainPercent.map(e=>p.active*10*e);lines=[series('Simplified possible heave',heave)];met=[['At selected Δw',fmt(p.active*10*p.coeff*p.wet)+' mm'],['Assumed swelling strain',fmt(p.coeff*p.wet)+' %']];xLabel='Moisture-content change (%)';yLabel='Illustrative heave (mm)';break;}
case 'consolidation':{
 let S=p.Cc*p.thick/2*Math.log10((80+p.delta)/80)*1000,cv=1,Hd=p.thick/2;
 xs=n(0,30,101);function U(t){if(t<=0)return 0;let Tv=cv*t/(Hd*Hd);return Tv<0.2?Math.min(1,Math.sqrt(4*Tv/PI)):Math.min(1,1-8/(PI*PI)*Math.exp(-PI*PI*Tv/4))}
 lines=[series('One-dimensional settlement',xs.map(t=>S*U(t)))];met=[['Final primary settlement',fmt(S)+' mm'],['Approximate t90',fmt(.848*Hd*Hd/cv)+' years'],['Double drainage Hd',fmt(Hd)+' m']];xLabel='Time (years)';yLabel='Settlement (mm)';break;}
case 'liq':{
 xs=n(1,20);let zWater=p.water;let csrs=xs.map(z=>{let total=18*Math.min(z,zWater)+20*Math.max(0,z-zWater);let eff=total-9.81*Math.max(0,z-zWater);let rd=Math.max(.7,1-.015*z);return .65*p.pga*(total/Math.max(eff,1))*rd});lines=[series('Illustrative CSR',csrs),series('Chosen CRR',xs.map(_=>p.crr))];met=[['Screening FS at 10 m',fmt(p.crr/csrs[23] ,2)],['Layers where CSR > CRR',csrs.filter(v=>v>p.crr).length+' / '+csrs.length]];xLabel='Depth (m)';yLabel='Cyclic stress/resistance ratio';break;}
case 'lateral':{
 let y0=1000*p.H/p.k;xs=n(0,15);lines=[series('Lateral displacement',xs.map(z=>y0*(1+z/p.decay)*Math.exp(-z/p.decay)))];met=[['Pile head displacement',fmt(y0)+' mm'],['Characteristic length',fmt(p.decay)+' m']];xLabel='Depth below head (m)';yLabel='Illustrative lateral movement (mm)';break;}
case 'selection':{
 xs=[1,2,3];let ratings=[[6,7,9],[7,9,6],[8,5,7]],w=[p.cost,p.service,p.construct],sum=w.reduce((a,b)=>a+b,0)||1;
 let values=ratings.map(row=>row.reduce((tot,v,i)=>tot+v*w[i],0)/sum);lines=[series('Weighted preference score',values)];met=[['Option 1','Spread footing: '+fmt(values[0],2)],['Option 2','Raft: '+fmt(values[1],2)],['Option 3','Piles: '+fmt(values[2],2)],['Highest in this example',['Spread footing','Raft','Piles'][values.indexOf(Math.max(...values))]]];xLabel='1 spread footing · 2 raft · 3 piles';yLabel='Illustrative preference (0–10)';break;}
}
return {xs,lines,met,xLabel,yLabel,warning};}
const colors=['#7adbd0','#f6b66b','#a6a0ff','#f48fa5'];
function chart(result){let xs=result.xs,ys=result.lines.flatMap(t=>t.values),minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(0,...ys),maxY=Math.max(1,...ys),W=800,H=365,L=82,R=24,T=25,B=60;
let X=x=>L+(x-minX)/(maxX-minX||1)*(W-L-R),Y=y=>H-B-(y-minY)/(maxY-minY||1)*(H-T-B);
let body=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Engineering response plot: ${result.xLabel} versus ${result.yLabel}">`;
for(let i=0;i<=5;i++){let x=L+(W-L-R)*i/5,y=T+(H-T-B)*i/5;body+=`<line x1="${x}" y1="${T}" x2="${x}" y2="${H-B}" stroke="#28445a"/><text x="${x}" y="${H-B+22}" fill="#a4bac8" text-anchor="middle" font-size="12">${fmt(minX+(maxX-minX)*i/5,1)}</text>`;body+=`<line x1="${L}" y1="${y}" x2="${W-R}" y2="${y}" stroke="#28445a"/><text x="${L-12}" y="${y+4}" fill="#a4bac8" text-anchor="end" font-size="12">${fmt(maxY-(maxY-minY)*i/5,1)}</text>`}
result.lines.forEach((line,idx)=>{let pts=line.values.map((v,i)=>`${X(xs[i]).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');body+=`<polyline points="${pts}" fill="none" stroke="${colors[idx%colors.length]}" stroke-width="3" stroke-linejoin="round"/>`});
body+=`<text x="${W/2}" y="${H-9}" fill="#d7e5ed" text-anchor="middle" font-size="15">${result.xLabel}</text><text x="17" y="${H/2}" transform="rotate(-90 17 ${H/2})" fill="#d7e5ed" text-anchor="middle" font-size="15">${result.yLabel}</text></svg>`;
body+=`<div class="legend">${result.lines.map((l,i)=>`<span><i style="background:${colors[i%colors.length]}"></i>${l.label}</span>`).join('')}</div>`;return body;}


  var FE_SPECS = [{"idx": 1, "unit": 1, "id": "investigation", "title": "Borehole Spacing and Confidence", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "spacing", "name": "Exploration spacing", "min": 10, "max": 80, "step": 2, "def": 30, "unit": "m"}, {"key": "variability", "name": "Deposit variability", "min": 0.05, "max": 0.8, "step": 0.01, "def": 0.3, "unit": "index"}, {"key": "bias", "name": "Local anomaly magnitude", "min": 0, "max": 8, "step": 0.2, "def": 2, "unit": "m"}]}, {"idx": 2, "unit": 1, "id": "groundwater", "title": "Groundwater and Effective Stress", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "water", "name": "Water-table depth", "min": 0, "max": 15, "step": 0.5, "def": 3, "unit": "m"}, {"key": "gamman", "name": "Moist unit weight", "min": 15, "max": 21, "step": 0.5, "def": 18, "unit": "kN/m\u00b3"}, {"key": "gammasat", "name": "Saturated unit weight", "min": 18, "max": 23, "step": 0.5, "def": 20, "unit": "kN/m\u00b3"}]}, {"idx": 3, "unit": 2, "id": "bearing", "title": "Strip Footing Bearing Capacity", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "width", "name": "Footing width", "min": 0.8, "max": 5, "step": 0.1, "def": 2, "unit": "m"}, {"key": "depth", "name": "Embedment", "min": 0, "max": 3, "step": 0.1, "def": 1, "unit": "m"}, {"key": "phi", "name": "Friction angle", "min": 10, "max": 40, "step": 1, "def": 30, "unit": "\u00b0"}]}, {"idx": 4, "unit": 2, "id": "eccentric", "title": "Footing Pressure Under Eccentric Load", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "ecc", "name": "Load eccentricity", "min": 0, "max": 1.2, "step": 0.02, "def": 0.2, "unit": "m"}, {"key": "width", "name": "Base width", "min": 2, "max": 6, "step": 0.1, "def": 4, "unit": "m"}, {"key": "force", "name": "Vertical load", "min": 400, "max": 2600, "step": 50, "def": 1200, "unit": "kN"}]}, {"idx": 5, "unit": 3, "id": "settlement", "title": "Elastic Settlement Sensitivity", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "E", "name": "Young modulus", "min": 8, "max": 90, "step": 1, "def": 30, "unit": "MPa"}, {"key": "pressure", "name": "Net contact pressure", "min": 50, "max": 350, "step": 5, "def": 150, "unit": "kPa"}, {"key": "width", "name": "Footing width", "min": 1, "max": 7, "step": 0.2, "def": 3, "unit": "m"}]}, {"idx": 6, "unit": 3, "id": "raft", "title": "Raft Reaction Redistribution", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "load1", "name": "Left column load", "min": 400, "max": 2000, "step": 50, "def": 900, "unit": "kN"}, {"key": "load2", "name": "Right column load", "min": 400, "max": 2000, "step": 50, "def": 1200, "unit": "kN"}, {"key": "spread", "name": "Illustrative influence spread", "min": 0.5, "max": 3, "step": 0.1, "def": 1.3, "unit": "m"}]}, {"idx": 7, "unit": 4, "id": "rafttilt", "title": "Differential Settlement and Tilt", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "kl", "name": "Left soil spring stiffness", "min": 8, "max": 70, "step": 2, "def": 20, "unit": "MN/m\u00b3"}, {"key": "kr", "name": "Right soil spring stiffness", "min": 8, "max": 70, "step": 2, "def": 45, "unit": "MN/m\u00b3"}, {"key": "pressure", "name": "Uniform surface pressure", "min": 50, "max": 250, "step": 5, "def": 120, "unit": "kPa"}]}, {"idx": 8, "unit": 4, "id": "pile", "title": "Pile Shaft and Toe Resistance", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "D", "name": "Pile diameter", "min": 0.3, "max": 1.6, "step": 0.05, "def": 0.7, "unit": "m"}, {"key": "fs", "name": "Average shaft resistance", "min": 20, "max": 110, "step": 5, "def": 55, "unit": "kPa"}, {"key": "qb", "name": "Toe resistance", "min": 300, "max": 3800, "step": 100, "def": 1400, "unit": "kPa"}]}, {"idx": 9, "unit": 5, "id": "group", "title": "Pile Group Interaction", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "n", "name": "Number of piles", "min": 2, "max": 16, "step": 1, "def": 9, "unit": "piles"}, {"key": "eta", "name": "Assumed group efficiency", "min": 0.55, "max": 1.0, "step": 0.01, "def": 0.8, "unit": "ratio"}, {"key": "single", "name": "Single-pile nominal resistance", "min": 300, "max": 2200, "step": 50, "def": 800, "unit": "kN"}]}, {"idx": 10, "unit": 5, "id": "earth", "title": "Earth Pressure and Water Pressure", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "H", "name": "Wall height", "min": 3, "max": 12, "step": 0.2, "def": 6, "unit": "m"}, {"key": "phi", "name": "Soil friction angle", "min": 20, "max": 40, "step": 1, "def": 30, "unit": "\u00b0"}, {"key": "water", "name": "Water-table depth below surface", "min": 0, "max": 12, "step": 0.25, "def": 4, "unit": "m"}]}, {"idx": 11, "unit": 6, "id": "wall", "title": "Retaining Wall Sliding Check", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "W", "name": "Wall vertical weight", "min": 350, "max": 1700, "step": 50, "def": 850, "unit": "kN/m"}, {"key": "P", "name": "Active earth thrust", "min": 100, "max": 900, "step": 25, "def": 350, "unit": "kN/m"}, {"key": "mu", "name": "Base friction coefficient", "min": 0.25, "max": 0.75, "step": 0.02, "def": 0.45, "unit": ""}]}, {"idx": 12, "unit": 6, "id": "heave", "title": "Expansive Soil Heave Sensitivity", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "active", "name": "Active-zone depth", "min": 0.5, "max": 5, "step": 0.1, "def": 2.5, "unit": "m"}, {"key": "wet", "name": "Change in water content", "min": 1, "max": 12, "step": 0.5, "def": 5, "unit": "%"}, {"key": "coeff", "name": "Swelling strain per 1% moisture", "min": 0.03, "max": 0.4, "step": 0.01, "def": 0.12, "unit": "% strain"}]}, {"idx": 13, "unit": 7, "id": "consolidation", "title": "Soft Clay Consolidation Response", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "Cc", "name": "Compression index", "min": 0.12, "max": 0.65, "step": 0.01, "def": 0.32, "unit": ""}, {"key": "thick", "name": "Compressible layer thickness", "min": 2, "max": 14, "step": 0.5, "def": 6, "unit": "m"}, {"key": "delta", "name": "Effective stress increment", "min": 10, "max": 160, "step": 5, "def": 60, "unit": "kPa"}]}, {"idx": 14, "unit": 7, "id": "liq", "title": "Liquefaction Triggering Screening", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "pga", "name": "Peak ground acceleration", "min": 0.1, "max": 0.6, "step": 0.02, "def": 0.28, "unit": "g"}, {"key": "crr", "name": "Cyclic resistance ratio", "min": 0.08, "max": 0.45, "step": 0.01, "def": 0.23, "unit": ""}, {"key": "water", "name": "Water table", "min": 0, "max": 8, "step": 0.5, "def": 2, "unit": "m"}]}, {"idx": 15, "unit": 8, "id": "lateral", "title": "Laterally Loaded Pile Decay", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "H", "name": "Head lateral force", "min": 30, "max": 350, "step": 10, "def": 120, "unit": "kN"}, {"key": "k", "name": "Illustrative lateral head stiffness", "min": 5000, "max": 80000, "step": 1000, "def": 22000, "unit": "kN/m"}, {"key": "decay", "name": "Characteristic decay length", "min": 1, "max": 7, "step": 0.2, "def": 3, "unit": "m"}]}, {"idx": 16, "unit": 8, "id": "selection", "title": "Foundation Alternatives Decision Matrix", "lead": "Interactive foundation mechanics model.", "inputs": [{"key": "cost", "name": "Cost priority", "min": 0, "max": 10, "step": 1, "def": 5, "unit": "weight"}, {"key": "service", "name": "Serviceability priority", "min": 0, "max": 10, "step": 1, "def": 8, "unit": "weight"}, {"key": "construct", "name": "Constructability priority", "min": 0, "max": 10, "step": 1, "def": 4, "unit": "weight"}]}];
  var MODELS_LIST = [];

  FE_SPECS.forEach(function(item, idx) {
    var labId = item.id;
    var unit = item.unit;

    var controlsHtml = item.inputs.map(function(inp) {
      var kid = inp.key, label = inp.name, min = inp.min, max = inp.max, step = inp.step, def = inp.def, unitStr = inp.unit || '';
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="fe_' + labId + '_' + kid + '">' + label + ' <span id="v_fe_' + labId + '_' + kid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="fe_' + labId + '_' + kid + '" data-key="' + kid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + item.idx + ' · Unit ' + unit + '</span><h3>' + item.title + '</h3><p>' + item.lead + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({
      idx: item.idx,
      unit: unit,
      id: labId,
      html: html,
      init: function(card) {
        try {
          var p = {};
          item.inputs.forEach(function(inp) { p[inp.key] = inp.def; });
          var metricsEl = card.querySelector('.metrics');
          var plotEl = card.querySelector('.plot');
          var noteEl = card.querySelector('.model-note');

          function updateFE() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var kid = inp.dataset.key;
              p[kid] = Number(inp.value);
              var vLbl = card.querySelector('#v_fe_' + labId + '_' + kid);
              if (vLbl) vLbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            });

            var res = solve(labId, p);
            if (metricsEl && res.met) {
              metricsEl.innerHTML = res.met.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + m[1] + '</output></div>';
              }).join('');
            }

            if (plotEl && res.lines) {
              plotEl.innerHTML = chart(res);
            }

            if (noteEl && res.warning) {
              noteEl.textContent = res.warning;
            }
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateFE);
          });
          updateFE();
        } catch (err) {
          console.warn('Foundation Engineering sim error in lab ' + labId + ':', err);
        }
      }
    });
  });

  var MODELS = MODELS_LIST;

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
