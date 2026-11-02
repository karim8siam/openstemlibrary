/* Soil Mechanics Interactive Simulation Suite */
(function(window) {
  'use strict';

  const model={
 phase:p=>{const e=p.e,G=p.Gs,S=p.Sr/100,gammaW=9.81;const out=[['Dry unit weight',G*gammaW/(1+e),'kN/m³'],['Saturated unit weight',(G+e)*gammaW/(1+e),'kN/m³'],['Bulk unit weight',(G+S*e)*gammaW/(1+e),'kN/m³'],['Porosity',100*e/(1+e),'%'],['Gravimetric water content',100*S*e/G,'%']];const d=[];for(let s=0;s<=100;s+=2)d.push([s,(G+s/100*e)*gammaW/(1+e)]);return result(out,[{name:'Bulk unit weight versus saturation',points:d}],'Saturation (%)','Bulk unit weight (kN/m³)',['Relationships are mass/volume identities with fixed void ratio; no swelling is modeled.']);},
 plastic:p=>{let PI=p.LL-p.PL,LI=PI>0?(p.w-p.PL)/PI:NaN;let pts=[];for(let ll=20;ll<=100;ll+=2)pts.push([ll,.73*(ll-20)]);return result([['Plasticity index',PI,'percentage points'],['Liquidity index',LI,''],['A-line PI at LL',.73*(p.LL-20),'percentage points']],[{name:'Casagrande A-line (reference)',points:pts}],'Liquid limit (%)','PI (percentage points)',['The shown A-line is an engineering classification reference; the plotted line is not a strength curve.','LL must exceed PL for a physically interpretable PI.']);},
 darcy:p=>{let k1=p.k1*1e-6,k2=p.k2*1e-6,h1=p.h1,h2=p.h2;let kh=(k1*h1+k2*h2)/(h1+h2),kv=(h1+h2)/(h1/k1+h2/k2);let pts=[];for(let i=0;i<=0.5;i+=.01)pts.push([i,1e6*kv*i]);return result([['Parallel-layer conductivity',kh*1e6,'µm/s'],['Perpendicular-layer conductivity',kv*1e6,'µm/s'],['Vertical Darcy flux',kv*p.i*86400*1000,'mm/day'],['Anisotropy kh/kv',kh/kv,'']],[{name:'Vertical flux',points:pts}],'Hydraulic gradient','Vertical flux (µm/s)',['Layer conductivities assumed isotropic individually; no lateral bypass or capillarity.']);},
 stress:p=>{let a=[],b=[],c=[],zmax=p.maxz;for(let j=0;j<=80;j++){let z=zmax*j/80,st=p.gd*Math.min(z,p.gw)+p.gs*Math.max(0,z-p.gw),u=9.81*Math.max(0,z-p.gw);a.push([z,st]);b.push([z,u]);c.push([z,st-u]);}const z=zmax,st=p.gd*Math.min(z,p.gw)+p.gs*Math.max(0,z-p.gw),u=9.81*Math.max(0,z-p.gw);return result([['Total stress at bottom',st,'kPa'],['Pore pressure at bottom',u,'kPa'],['Effective stress at bottom',st-u,'kPa']],[{name:'Total σv',points:a},{name:'Pore u',points:b},{name:'Effective σ′v',points:c}],'Depth (m)','Stress (kPa)',['Single hydrostatic water table; no seepage or capillary suction.']);},
 proctor:p=>{let opt=p.opt-(p.energy-1)*2.5,peak=p.peak+1.2*(p.energy-1),a=[],min=Math.max(1,opt-12),max=opt+12;for(let w=min;w<=max;w+=0.3){const gd=Math.max(1,peak*(1-Math.pow((w-opt)/p.width,2)*0.1));a.push([w,gd]);}return result([['Illustrative optimum',opt,'%'],['Illustrative maximum dry unit weight',peak,'kN/m³'],['At w = 12%',peak*(1-0.1*Math.pow((12-opt)/p.width,2)),'kN/m³']],[{name:'Illustrative moisture–density curve',points:a}],'Water content (%)','Dry unit weight (kN/m³)',['Invented smooth curve for teaching only. Actual values must be measured by a Proctor series; do not extrapolate.']);},
 fieldcomp:p=>{let dry=p.wet/(1+p.water/100),rc=100*dry/p.lab,pts=[];for(let w=0;w<=24;w+=0.5)pts.push([w,100*(p.wet/(1+w/100))/p.lab]);return result([['Field dry unit weight',dry,'kN/m³'],['Relative compaction',rc,'%'],['Illustrative margin',rc-p.target,'percentage points']],[{name:'Calculated RC if measured bulk density held constant',points:pts}],'Measured water content (%)','Relative compaction (%)',['Changing water content without changing bulk density is a mathematical sensitivity only; it is not a field moisture conditioning model.','The target is user-defined, not a standard universal criterion.']);},
 settlement:p=>{let pc=Math.max(p.pc,p.p0),pf=p.pf;function delta(s){if(s<=p.p0)return 0;return p.Cr*Math.log10(Math.min(s,pc)/p.p0)+p.Cc*Math.log10(Math.max(s,pc)/pc);}let de=delta(Math.max(p.p0,pf)),s=1000*p.H*de/(1+p.e);let pts=[];for(let x=p.p0;x<=450;x+=3)pts.push([x,p.e-delta(x)]);return result([['Compression Δe',de,''],['Primary settlement estimate',s,'mm'],['Overconsolidation ratio',pc/p.p0,'']],[{name:'Piecewise e–log stress response',points:pts}],'Final effective stress (kPa)','Void ratio e',['e–log relation assumes one-dimensional compression; constant Cc and Cr. Negative compression is not computed for unloading.']);},
 time:p=>{const Hdr=p.depth/p.drain,cv=p.cv*1e-7,tv=cv*p.days*86400/(Hdr*Hdr);function U(t){let sum=0;for(let j=0;j<120;j++){let m=2*j+1;sum+=Math.exp(-m*m*Math.PI*Math.PI*t/4)/(m*m);}return Math.max(0,Math.min(1,1-8*sum/(Math.PI*Math.PI)));}let pts=[];for(let day=0;day<=1800;day+=20)pts.push([day,100*U(cv*day*86400/(Hdr*Hdr))]);return result([['Drainage path',Hdr,'m'],['Time factor Tv',tv,''],['Mean degree of consolidation',100*U(tv),'%']],[{name:'Degree of consolidation',points:pts}],'Elapsed time (days)','Mean consolidation U (%)',['Terzaghi 1-D idealized uniform initial excess pore-pressure solution; assumes constant cv.']);},
 shear:p=>{const ph=p.phi*Math.PI/180,pts=[];for(let x=0;x<=300;x+=5)pts.push([x,p.c+x*Math.tan(ph)]);return result([['Effective normal stress',p.total-p.pore,'kPa'],['Failure resistance τf',p.c+Math.max(0,p.total-p.pore)*Math.tan(ph),'kPa'],['Reduction from pore pressure',p.pore*Math.tan(ph),'kPa']],[{name:'Mohr–Coulomb envelope',points:pts}],'Effective normal stress (kPa)','Shear strength (kPa)',['Negative effective normal stress outside domain is clipped for simple teaching visualization.']);},
 triax:p=>{const s1=p.s1-p.u,s3=p.s3-p.u,pmean=(s1+2*s3)/3,q=s1-s3;let pts=[];for(let u=0;u<=100;u+=2)pts.push([u,(p.s1+2*p.s3)/3-u]);return result([['Effective mean stress p′',pmean,'kPa'],['Deviator stress q',q,'kPa'],['Major effective principal stress',s1,'kPa'],['Minor effective principal stress',s3,'kPa']],[{name:'p′ versus pore pressure at fixed total stresses',points:pts}],'Pore pressure (kPa)','Effective mean stress p′ (kPa)',['Axisymmetric compression; q is invariant to a common hydrostatic pore-pressure subtraction.']);},
 bouss:p=>{let pts=[];for(let r=0;r<=p.rmax;r+=p.rmax/70){let ds=3*p.Q/(2*Math.PI*p.z*p.z)*Math.pow(1+(r/p.z)*(r/p.z),-2.5);pts.push([r,ds]);}return result([['Stress directly below load',3*p.Q/(2*Math.PI*p.z*p.z),'kPa'],['Stress at radial offset z',3*p.Q/(2*Math.PI*p.z*p.z)/Math.pow(2,2.5),'kPa']],[{name:'Vertical stress increment',points:pts}],'Radius r (m)','Δσz (kPa)',['Point load, homogeneous isotropic elastic half-space; no use at z=0.']);},
 rankine:p=>{let phi=p.phi*Math.PI/180,ka=Math.pow(Math.tan(Math.PI/4-phi/2),2),kp=1/ka,pts=[];for(let d=0;d<=p.H;d+=p.H/50)pts.push([d,ka*(p.gamma*d+p.q)]);return result([['Active coefficient Ka',ka,''],['Passive coefficient Kp',kp,''],['Active soil thrust',0.5*ka*p.gamma*p.H*p.H,'kN/m'],['Active surcharge thrust',ka*p.q*p.H,'kN/m']],[{name:'Active lateral pressure with depth',points:pts}],'Depth below surface (m)','Horizontal stress (kPa)',['Wall displacement sufficient to mobilize active earth pressure; no hydrostatic water pressure.']);},
 slope:p=>{let be=p.beta*Math.PI/180,ph=p.phi*Math.PI/180;let tn=p.gamma*p.z*Math.sin(be)*Math.cos(be),ne=p.gamma*p.z*Math.cos(be)**2-p.u,fs=(p.c+Math.max(0,ne)*Math.tan(ph))/Math.max(1e-8,tn),pts=[];for(let beta=5;beta<=42;beta+=.5){let b=beta*Math.PI/180,t=p.gamma*p.z*Math.sin(b)*Math.cos(b),n=p.gamma*p.z*Math.cos(b)**2-p.u;pts.push([beta,(p.c+Math.max(0,n)*Math.tan(ph))/t]);}return result([['Mobilized shear',tn,'kPa'],['Effective normal stress',ne,'kPa'],['Illustrative factor of safety',fs,'']],[{name:'FS versus slope angle',points:pts}],'Slope angle (°)','Factor of safety',['Infinite-slope approximation; fixed pore pressure represents the failure plane. Outside positive effective stress, frictional term is clipped.']);},
 bearing:p=>{let qut=5.7*p.su+p.q,qapp=p.load/p.width,pts=[];for(let s=10;s<=120;s+=2)pts.push([s,5.7*s+p.q]);return result([['Idealized ultimate pressure',qut,'kPa'],['Applied bearing pressure',qapp,'kPa'],['Capacity ratio (not design FS)',qut/qapp,'']],[{name:'φ=0 strip footing ultimate pressure',points:pts}],'Undrained strength su (kPa)','Ultimate bearing pressure (kPa)',['Only classic φ=0 Terzaghi benchmark with Nc≈5.7, Nq=1, Nγ=0; not a permissible bearing pressure.']);},
 sampling:p=>{const rec=100*p.retr/p.length,area=100*((p.inner+2*p.thick)**2-p.inner**2)/(p.inner**2);let pts=[];for(let t=.5;t<=5;t+=.1)pts.push([t,100*((p.inner+2*t)**2-p.inner**2)/(p.inner**2)]);return result([['Sample recovery ratio',rec,'%'],['Geometric area ratio',area,'%'],['Exceeds advance length?',p.retr>p.length?1:0,'1=yes']],[{name:'Tube area ratio versus wall thickness',points:pts}],'Wall thickness (mm)','Area ratio (%)',['Area ratio uses tube cutting-edge diameters only; it is not a universal sample-quality classification.']);},
 uncertainty:p=>{let state=20260317;function rand(){state=(state*1664525+1013904223)>>>0;return (state+0.5)/4294967296;}let fs=[];for(let i=0;i<p.count;i++){let a=rand(),b=rand(),z=Math.sqrt(-2*Math.log(a))*Math.cos(2*Math.PI*b),ph=Math.max(1,Math.min(89,p.mu+p.sd*z));fs.push(Math.tan(ph*Math.PI/180)/Math.tan(p.beta*Math.PI/180));}fs.sort((a,b)=>a-b);let pts=[];for(let i=0;i<fs.length;i+=Math.max(1,Math.floor(fs.length/100)))pts.push([100*i/(fs.length-1),fs[i]]);let lo=fs[Math.floor(fs.length*.05)],med=fs[Math.floor(fs.length*.5)],hi=fs[Math.floor(fs.length*.95)];return result([['Simulated 5th percentile FS',lo,''],['Simulated median FS',med,''],['Simulated 95th percentile FS',hi,''],['Count with FS < 1',fs.filter(x=>x<1).length,'samples']],[{name:'Assumed-distribution FS quantiles',points:pts}],'Empirical percentile (%)','Illustrative FS',['Fixed-seed normal model for friction angle (not field evidence). Percent below one is not a validated site failure probability.']);}
};

  function result(values,series,xLabel,yLabel,notes){return {values,series,xLabel,yLabel,notes};}
const colors=['#61dacb','#fdc776','#a78bfa','#7ab1f3'];
function pathFor(pts,minX,maxX,minY,maxY,W,H,pad){return pts.filter(v=>Number.isFinite(v[0])&&Number.isFinite(v[1])).map((v,i)=>`${i?'L':'M'}${(pad+(v[0]-minX)* (W-2*pad)/(maxX-minX||1)).toFixed(2)},${(H-pad-(v[1]-minY)*(H-2*pad)/(maxY-minY||1)).toFixed(2)}`).join(' ');}
function chart(series,xLabel,yLabel){const W=780,H=360,pad=58,all=series.flatMap(s=>s.points).filter(p=>Number.isFinite(p[0])&&Number.isFinite(p[1]));if(!all.length)return '<svg role="img" aria-label="No numerical data"></svg>';let xs=all.map(p=>p[0]),ys=all.map(p=>p[1]),minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(...ys),maxY=Math.max(...ys);if(minY===maxY){minY-=1;maxY+=1;}let buff=(maxY-minY)*.1;minY-=buff;maxY+=buff;let s=`<svg class="diagram" viewBox="0 0 ${W} ${H}" role="img" aria-label="${xLabel} versus ${yLabel}; detailed numbers are provided below">`;
for(let k=0;k<=5;k++){let v=minY+(maxY-minY)*k/5,y=H-pad-k*(H-2*pad)/5;s+=`<line x1="${pad}" y1="${y}" x2="${W-pad}" y2="${y}" stroke="#294b5d"/><text x="${pad-8}" y="${y+5}" fill="#aac4d0" font-size="12" text-anchor="end">${Number(v.toPrecision(3))}</text>`;}
for(let k=0;k<=5;k++){let v=minX+(maxX-minX)*k/5,x=pad+k*(W-2*pad)/5;s+=`<text x="${x}" y="${H-pad+20}" fill="#aac4d0" text-anchor="middle" font-size="12">${Number(v.toPrecision(3))}</text>`;}
series.forEach((t,i)=>{s+=`<path d="${pathFor(t.points,minX,maxX,minY,maxY,W,H,pad)}" stroke="${colors[i%colors.length]}" fill="none" stroke-width="3"/><text x="${W-pad-6}" y="${24+i*18}" text-anchor="end" font-size="13" fill="${colors[i%colors.length]}">${t.name.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</text>`;});s+=`<text x="${W/2}" y="${H-5}" text-anchor="middle" fill="#d8edf0" font-size="13">${xLabel}</text><text transform="translate(17 ${H/2}) rotate(-90)" text-anchor="middle" fill="#d8edf0" font-size="13">${yLabel}</text></svg>`;return s;}
const specs=window.SOIL_SPEC;


  var SOIL_SPECS = [{"idx": 1, "unit": 1, "title": "Phase Relations Explorer", "lead": "Three-phase solids/water/air and derived state quantities. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "phase", "params": [["Gs", "Particle specific gravity", 2, 3, 0.02, 2.7, ""], ["e", "Void ratio", 0.2, 1.8, 0.02, 0.65, ""], ["Sr", "Saturation", 0, 100, 1, 65, "%"]]}}, {"idx": 2, "unit": 1, "title": "Plasticity State Map", "lead": "Atterberg limits and consistency index. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "plastic", "params": [["LL", "Liquid limit", 25, 90, 1, 50, "%"], ["PL", "Plastic limit", 10, 45, 1, 25, "%"], ["w", "Water content", 5, 90, 1, 32, "%"]]}}, {"idx": 3, "unit": 2, "title": "Layered Darcy Seepage", "lead": "Head loss and equivalent conductivities of horizontal layers. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "darcy", "params": [["k1", "Upper-layer k", 1, 100, 1, 35, "\u00b5m/s"], ["k2", "Lower-layer k", 1, 100, 1, 8, "\u00b5m/s"], ["h1", "Upper thickness", 1, 8, 0.2, 3, "m"], ["h2", "Lower thickness", 1, 8, 0.2, 3, "m"], ["i", "Hydraulic gradient", 0, 0.5, 0.01, 0.08, ""]]}}, {"idx": 4, "unit": 2, "title": "Effective Stress with Water Table", "lead": "Piecewise total, pore and effective vertical stresses. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "stress", "params": [["gw", "Water-table depth", 0, 6, 0.1, 2, "m"], ["gd", "Moist unit weight", 14, 22, 0.5, 18, "kN/m\u00b3"], ["gs", "Saturated unit weight", 16, 24, 0.5, 20, "kN/m\u00b3"], ["maxz", "Profile depth", 4, 12, 0.5, 8, "m"]]}}, {"idx": 5, "unit": 3, "title": "Moisture\u2013Density Proctor Lab", "lead": "Illustrative dry-density curve with energy-dependent optimum. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "proctor", "params": [["opt", "Reference optimum water", 6, 20, 0.5, 12, "%"], ["peak", "Reference maximum dry unit weight", 14, 22, 0.2, 18.5, "kN/m\u00b3"], ["energy", "Relative effort", 0.6, 1.5, 0.05, 1, ""], ["width", "Curve width", 4, 14, 0.5, 8, "%"]]}}, {"idx": 6, "unit": 3, "title": "Field Compaction Compliance", "lead": "Measured dry density, water content and relative compaction. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "fieldcomp", "params": [["wet", "Field bulk unit weight", 16, 23, 0.1, 20, "kN/m\u00b3"], ["water", "Water content", 4, 24, 0.5, 12, "%"], ["lab", "Lab maximum dry unit weight", 16, 22, 0.1, 19, "kN/m\u00b3"], ["target", "Illustrative target", 90, 100, 1, 95, "%"]]}}, {"idx": 7, "unit": 4, "title": "e\u2013log Consolidation Settlement", "lead": "Recompression and virgin compression with preconsolidation. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "settlement", "params": [["H", "Clay thickness", 1, 10, 0.2, 4, "m"], ["e", "Initial void ratio", 0.4, 1.8, 0.05, 0.9, ""], ["Cc", "Virgin compression index", 0.1, 0.8, 0.02, 0.32, ""], ["Cr", "Recompression index", 0.01, 0.2, 0.01, 0.06, ""], ["p0", "Initial effective stress", 30, 200, 5, 80, "kPa"], ["pc", "Preconsolidation pressure", 30, 300, 5, 120, "kPa"], ["pf", "Final effective stress", 60, 450, 5, 220, "kPa"]]}}, {"idx": 8, "unit": 4, "title": "Consolidation Time &amp; Drainage", "lead": "Terzaghi series solution for average consolidation. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "time", "params": [["cv", "Consolidation coefficient", 0.2, 8, 0.2, 2, "\u00d710\u207b\u2077 m\u00b2/s"], ["depth", "Layer thickness", 1, 10, 0.2, 4, "m"], ["drain", "Drainage faces", 1, 2, 1, 2, "faces"], ["days", "Elapsed time", 10, 1800, 10, 365, "days"]]}}, {"idx": 9, "unit": 5, "title": "Mohr\u2013Coulomb Direct Shear", "lead": "Peak strength envelope and pore-pressure sensitivity. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "shear", "params": [["c", "Effective cohesion intercept", 0, 40, 1, 8, "kPa"], ["phi", "Friction angle", 15, 45, 1, 30, "\u00b0"], ["pore", "Pore pressure", 0, 100, 5, 25, "kPa"], ["total", "Total normal stress", 75, 300, 5, 150, "kPa"]]}}, {"idx": 10, "unit": 5, "title": "Triaxial Stress Path", "lead": "Stress invariants and pore-pressure effect. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "triax", "params": [["s1", "Major total principal stress", 150, 500, 10, 300, "kPa"], ["s3", "Minor total principal stress", 50, 250, 10, 100, "kPa"], ["u", "Pore pressure", 0, 100, 5, 25, "kPa"]]}}, {"idx": 11, "unit": 6, "title": "Boussinesq Stress Bulb", "lead": "Vertical stress under a concentrated surface load. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "bouss", "params": [["Q", "Surface point load", 30, 500, 10, 100, "kN"], ["z", "Depth", 0.5, 12, 0.25, 3, "m"], ["rmax", "Horizontal extent", 1, 14, 0.5, 9, "m"]]}}, {"idx": 12, "unit": 6, "title": "Rankine Earth Pressure", "lead": "Active/passive coefficients and soil/surcharge thrust. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "rankine", "params": [["phi", "Drained friction angle", 18, 42, 1, 30, "\u00b0"], ["gamma", "Backfill unit weight", 15, 22, 0.5, 18, "kN/m\u00b3"], ["H", "Wall height", 2, 10, 0.25, 5, "m"], ["q", "Uniform surcharge", 0, 40, 1, 10, "kPa"]]}}, {"idx": 13, "unit": 7, "title": "Infinite-Slope Stability", "lead": "Shear versus effective normal resistance in a shallow planar slope. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "slope", "params": [["beta", "Slope angle", 5, 40, 1, 25, "\u00b0"], ["phi", "Friction angle", 15, 45, 1, 32, "\u00b0"], ["c", "Effective cohesion", 0, 30, 1, 5, "kPa"], ["gamma", "Unit weight", 15, 22, 0.5, 19, "kN/m\u00b3"], ["z", "Vertical depth", 0.5, 5, 0.25, 2, "m"], ["u", "Pore pressure on plane", 0, 45, 1, 5, "kPa"]]}}, {"idx": 14, "unit": 7, "title": "Simplified Strip Bearing Capacity", "lead": "Classical \u03c6=0 strip-footing benchmark. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "bearing", "params": [["su", "Undrained strength", 10, 120, 5, 40, "kPa"], ["q", "Embedment surcharge", 0, 70, 2, 20, "kPa"], ["width", "Footing width", 1, 5, 0.1, 2, "m"], ["load", "Applied load / length", 50, 800, 10, 300, "kN/m"]]}}, {"idx": 15, "unit": 8, "title": "Sampler Recovery &amp; Disturbance", "lead": "Recovery ratio and sample handling checks. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "sampling", "params": [["length", "Advanced length", 0.25, 1.5, 0.05, 1, "m"], ["retr", "Recovered length", 0.1, 1.5, 0.05, 0.85, "m"], ["thick", "Tube wall thickness", 0.5, 5, 0.1, 2, "mm"], ["inner", "Inside diameter", 40, 110, 2, 75, "mm"]]}}, {"idx": 16, "unit": 8, "title": "Parameter Uncertainty Explorer", "lead": "Reproducible distributions for slope friction angle. Explore physically meaningful parameter changes and document a reproducible thought experiment.", "spec": {"model": "uncertainty", "params": [["mu", "Mean friction angle", 20, 40, 0.5, 32, "\u00b0"], ["sd", "Assumed standard deviation", 0.5, 8, 0.5, 3, "\u00b0"], ["beta", "Slope angle", 10, 35, 1, 25, "\u00b0"], ["count", "Sample count", 100, 1200, 100, 500, "samples"]]}}];
  var MODELS_LIST = [];

  SOIL_SPECS.forEach(function(item, idx) {
    var spec = item.spec;
    var modelId = spec.model;
    var unit = item.unit;

    var controlsHtml = spec.params.map(function(p) {
      var pid = p[0], label = p[1], min = p[2], max = p[3], step = p[4], def = p[5], unitStr = p[6] || '';
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sm_' + modelId + '_' + pid + '">' + label + ' <span id="v_sm_' + modelId + '_' + pid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="sm_' + modelId + '_' + pid + '" data-pid="' + pid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + item.idx + ' · Unit ' + unit + '</span><h3>' + item.title + '</h3><p>' + item.lead + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({
      idx: item.idx,
      unit: unit,
      key: modelId,
      html: html,
      init: function(card) {
        try {
          var p = {};
          spec.params.forEach(function(param) { p[param[0]] = param[5]; });
          var metricsEl = card.querySelector('.metrics');
          var plotEl = card.querySelector('.plot');
          var noteEl = card.querySelector('.model-note');

          function updateSoil() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pid = inp.dataset.pid;
              p[pid] = Number(inp.value);
              var vLbl = card.querySelector('#v_sm_' + modelId + '_' + pid);
              if (vLbl) vLbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            });

            var fn = model[modelId];
            if (!fn) return;
            var out = fn(p);

            if (metricsEl && out.values) {
              metricsEl.innerHTML = out.values.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? m[1].toFixed(3) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }).join('');
            }

            if (plotEl && out.series) {
              plotEl.innerHTML = chart(out.series, out.xLabel, out.yLabel);
            }

            if (noteEl && out.notes) {
              noteEl.textContent = out.notes.join(' ');
            }
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateSoil);
          });
          updateSoil();
        } catch (err) {
          console.warn('Soil Mechanics sim error in model ' + modelId + ':', err);
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
