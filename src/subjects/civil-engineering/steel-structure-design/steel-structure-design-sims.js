/* Steel Structure Design Interactive Simulation Suite */
(function(window) {
  'use strict';

  const lin=(n,f)=>Array.from({length:n+1},(_,i)=>f(i/n));
const S={
 steel:{title:'Steel stress–strain laboratory',unit:1,why:'Explore elastic modulus, yield stress, strain hardening, and the difference between nominal material strength and member resistance.',assumptions:'Monotonic idealized uniaxial tension at room temperature. Bilinear hardening is an educational constitutive idealization; necking, ductile fracture and rate/temperature effects are excluded.',inputs:[['E','Young modulus (GPa)',160,220,200,5],['fy','Yield strength (MPa)',200,550,355,5],['Et','Post-yield tangent modulus (GPa)',0,8,2,0.5],['ep','Maximum plotted strain (%)',0.5,8,3,0.5]],calc:p=>{let ee=p.fy/(p.E*1000),v=lin(160,t=>{let e=t*p.ep/100;return [e*100,e<=ee?p.E*1000*e:p.fy+p.Et*1000*(e-ee)]});return {series:[['Idealized stress (MPa)',v]],metrics:[['Elastic yield strain',100*ee,'%'],['Stress at final strain',v.at(-1)[1],'MPa'],['Yield-to-elastic slope ratio',p.Et/p.E,'-']],x:'Engineering strain (%)',note:'The graph does not identify actual ultimate tensile strength or ductility of a specified grade.'}}},
 tension:{title:'Gross section versus net section',unit:2,why:'Vary plate geometry and a single hole to compare gross yielding and an illustrative net-section rupture limit.',assumptions:'Single plate in pure axial tension; one transverse through-hole; perfectly uniform axial stress away from hole; no shear lag, block shear or code resistance factors. Fu must be independently specified.',inputs:[['b','Plate width (mm)',80,400,200,10],['t','Plate thickness (mm)',6,30,12,1],['d','Hole diameter (mm)',8,50,22,1],['fy','Yield strength (MPa)',230,460,355,5],['fu','Ultimate tensile strength (MPa)',400,660,510,5]],calc:p=>{let gross=p.b*p.t,net=Math.max(0,(p.b-p.d)*p.t),gy=gross*p.fy/1000,nr=net*p.fu/1000,curve=lin(80,q=>[q*p.d,Math.max(0,(p.b-q*p.d)*p.t)*p.fu/1000]);return {series:[['Net-section nominal rupture vs opening (kN)',curve],['Gross-yield nominal force (kN)',[[0,gy],[p.d,gy]]]],metrics:[['Gross yield idealization',gy,'kN'],['Net rupture idealization',nr,'kN'],['Smaller of two idealizations',Math.min(gy,nr),'kN']],x:'Illustrative hole diameter (mm)',note:'This is NOT an AISC or Eurocode tension-member design check. Actual details require stagger, shear lag, block shear, connection rupture and relevant safety factors.'}}},
 holes:{title:'Bolt-hole pattern and effective net width',unit:2,why:'Inspect how hole count and plate width affect straight-line net area for a candidate tension path.',assumptions:'Uniform plate in pure tension, a straight transverse path through the same number of circular holes, no stagger correction, no shear lag and no block-shear mechanism.',inputs:[['b','Plate width (mm)',100,500,280,10],['t','Plate thickness (mm)',6,30,14,1],['nh','Holes across one section',1,4,2,1],['d','Hole diameter (mm)',10,32,22,1],['fy','Yield strength (MPa)',230,500,355,5]],calc:p=>{let w=Math.max(0,p.b-p.nh*p.d),a=w*p.t;let curve=lin(120,q=>{let db=q*32;return [db,Math.max(0,p.b-p.nh*db)*p.t]});return {series:[['Net area (mm²)',curve]],metrics:[['Gross cross-sectional area',p.b*p.t,'mm²'],['Net area for displayed path',a,'mm²'],['Net area / gross area',a/(p.b*p.t),'-']],x:'Hole diameter (mm)',note:'A staggered rupture path must be calculated separately. Holes may create several candidate fracture paths; the minimum must be identified.'}}},
 euler:{title:'Euler column buckling',unit:3,why:'Explore the dependence of ideal elastic buckling on effective length, stiffness and radius of gyration.',assumptions:'Perfectly straight prismatic elastic pin-equivalent column; no imperfections, residual stress, local buckling, inelastic column curve or code strength factors.',inputs:[['L','Physical column length (m)',1,12,5,0.25],['K','Effective-length factor K',0.5,2.0,1,0.05],['E','Elastic modulus (GPa)',160,220,200,5],['I','Weak-axis inertia (million mm⁴)',2,120,18,1],['A','Area (mm²)',1000,18000,4800,100]],calc:p=>{let len=p.L*1000,pcr=Math.PI**2*p.E*1000*p.I*1e6/(p.K*len)**2/1000,r=Math.sqrt(p.I*1e6/p.A);let curve=lin(140,q=>{let x=(1+11*q);return [x,Math.PI**2*p.E*1000*p.I*1e6/(p.K*x*1000)**2/1000]});return {series:[['Ideal Euler critical load (kN)',curve]],metrics:[['Elastic Euler load',pcr,'kN'],['Weak-axis radius r',r,'mm'],['Effective slenderness KL/r',p.K*len/r,'-']],x:'Physical length (m)',note:'The Euler expression is an eigenvalue, not an allowable compression resistance. Check inelastic, local, flexural–torsional and frame stability separately.'}}},
 columns:{title:'Buckling-versus-yield crossover',unit:3,why:'Compare ideal elastic instability with nominal squash load over a range of column lengths.',assumptions:'Ideal axial compression of a member with constant area and weak-axis inertia; yield and Euler bounds are plotted without reduction factors or local buckling.',inputs:[['A','Gross area (mm²)',1000,16000,5000,100],['I','Inertia (million mm⁴)',2,120,24,1],['E','Elastic modulus (GPa)',170,215,200,5],['fy','Yield strength (MPa)',200,550,355,5],['K','Effective length factor K',0.5,2,1,0.05]],calc:p=>{let yld=p.A*p.fy/1000,curve=lin(160,q=>{let L=0.75+11.25*q;return [L,Math.PI**2*p.E*1000*p.I*1e6/(p.K*L*1000)**2/1000]});let cross=Math.PI*Math.sqrt(p.E*1000*p.I*1e6/(p.A*p.fy))/p.K/1000;return {series:[['Elastic buckling idealization (kN)',curve],['Yield-force idealization (kN)',[[0.75,yld],[12,yld]]]],metrics:[['Gross yield load',yld,'kN'],['Ideal crossover length',cross,'m'],['Radius of gyration',Math.sqrt(p.I*1e6/p.A),'mm']],x:'Physical length (m)',note:'Real compression resistance may be well below both plotted simple bounds because of imperfections and residual stresses.'}}},
 local:{title:'Plate-element slenderness explorer',unit:3,why:'Visualize a flat-element width-to-thickness ratio and its scaling with material properties.',assumptions:'Geometric slenderness only. The plotted reference scale sqrt(E/fy) is not a code classification limit; edge restraint, element type and stress gradient determine actual classification.',inputs:[['b','Flat element width (mm)',40,500,180,10],['t','Element thickness (mm)',3,30,10,0.5],['E','Elastic modulus (GPa)',160,220,200,5],['fy','Yield strength (MPa)',200,550,355,5]],calc:p=>{let ratio=p.b/p.t,scale=Math.sqrt(p.E*1000/p.fy),curve=lin(140,q=>{let thick=3+27*q;return [thick,p.b/thick]});return {series:[['Element b/t (dimensionless)',curve],['Reference sqrt(E/fy) (NOT code limit)',[[3,scale],[30,scale]]]],metrics:[['Plate slenderness b/t',ratio,'-'],['Reference scale sqrt(E/fy)',scale,'-'],['Normalized geometric ratio',ratio/scale,'-']],x:'Element thickness (mm)',note:'Do not classify a steel section from this chart. Check whether the element is an outstand or internal element and select the correct code limit.'}}},
 beam:{title:'Beam shear and bending moment',unit:4,why:'Change load and span to see shear zero-crossing, moment peaks and elastic deformation trends for a determinate beam.',assumptions:'Simply supported prismatic beam, uniform full-span vertical load only, small displacements and linear-elastic bending. Self-weight is included only if entered in the load.',inputs:[['L','Span (m)',2,15,7,0.25],['w','Uniform load (kN/m)',1,60,18,1],['E','Young modulus (GPa)',170,220,200,5],['I','Major-axis inertia (million mm⁴)',10,650,150,10]],calc:p=>{let R=p.w*p.L/2,V=lin(120,t=>[t*p.L,R-p.w*t*p.L]),M=lin(120,t=>{let x=t*p.L;return [x,R*x-p.w*x*x/2]});let de=5*(p.w)*((p.L*1000)**4)/(384*p.E*1000*p.I*1e6);return {series:[['Shear V (kN)',V],['Bending M (kN·m)',M]],metrics:[['Each support reaction',R,'kN'],['Peak moment',p.w*p.L*p.L/8,'kN·m'],['Elastic peak deflection',de,'mm']],x:'Distance from left support (m)',note:'Shear and moment share a chart with different units: compare their shapes, not direct heights. Deflection uses w in N/mm (numerically equal to kN/m).'}}},
 lt:{title:'Elastic lateral–torsional buckling',unit:4,why:'Investigate how unsupported length and warping/torsional stiffness influence the ideal elastic critical bending moment.',assumptions:'Doubly-symmetric uniform I-section, ideal simply supported warping/twist end conditions, constant bending moment, no load-height correction or moment-gradient modification. Not a code LTB resistance.',inputs:[['Lb','Unbraced length (m)',1,12,5,0.25],['Iy','Weak-axis I (million mm⁴)',1,80,12,1],['J','Torsion constant J (thousand mm⁴)',20,2000,150,10],['Cw','Warping constant Cw (billion mm⁶)',10,10000,650,10],['E','Young modulus E (GPa)',170,220,200,5]],calc:p=>{let E=p.E*1000,G=E/2.6,Iy=p.Iy*1e6,J=p.J*1000,Cw=p.Cw*1e9;let fn=L=>{let x=L*1000;return Math.PI/x*Math.sqrt(E*Iy*G*J+Math.PI**2*E**2*Iy*Cw/(x*x))/1e6};return {series:[['Ideal elastic Mcr (kN·m)',lin(160,t=>{let L=1+11*t;return [L,fn(L)]})]],metrics:[['Ideal elastic critical moment',fn(p.Lb),'kN·m'],['Shear modulus (ν = 0.30)',G/1000,'GPa'],['Buckling tendency vs Lb = 1 m',fn(p.Lb)/fn(1),'-']],x:'Unbraced length (m)',note:'Moment gradient, load height, flange restraint, imperfections and inelastic behavior invalidate direct use as member design resistance.'}}},
 defl:{title:'Beam span–deflection trade-off',unit:4,why:'Study why serviceability often governs long-span beams despite acceptable bending strength.',assumptions:'Elastic simply-supported prismatic beam under uniform load; Euler–Bernoulli bending without shear deformation, connection slip or dynamic vibration.',inputs:[['L','Span (m)',2,16,8,0.25],['w','Uniform load (kN/m)',1,40,12,1],['E','Elastic modulus (GPa)',160,220,200,5],['I','Second moment (million mm⁴)',20,850,220,10]],calc:p=>{let f=L=>5*p.w*(L*1000)**4/(384*p.E*1000*p.I*1e6);return {series:[['Peak elastic deflection (mm)',lin(160,q=>{let L=2+14*q;return [L,f(L)]})]],metrics:[['Peak deflection at selected L',f(p.L),'mm'],['Span / peak deflection',p.L*1000/f(p.L),'-'],['Midspan moment',p.w*p.L*p.L/8,'kN·m']],x:'Span length (m)',note:'The span/deflection ratio is descriptive, not an automatic serviceability pass; identify the correct limit for the application.'}}},
 combined:{title:'Axial force–moment interaction screen',unit:5,why:'Compare a first-order linear utilization screen with a family of axial and bending demands.',assumptions:'Illustrative unity-sum demand model P/P_ref + |M|/M_ref; NOT a code beam-column resistance equation, and not a stability analysis.',inputs:[['P','Axial compression P (kN)',0,2500,850,25],['M','Applied major-axis M (kN·m)',0,700,180,10],['Pref','Illustrative axial reference P (kN)',200,3500,1500,25],['Mref','Illustrative bending reference M (kN·m)',100,850,410,10]],calc:p=>{let u=p.P/p.Pref+p.M/p.Mref;return {series:[['Illustrative boundary M (kN·m)',lin(100,q=>{let px=q*p.Pref;return [px,p.Mref*(1-q)]})],['Current demand',[[p.P,p.M],[p.P+0.005,p.M+0.005]]]],metrics:[['Axial reference utilization',p.P/p.Pref,'-'],['Bending reference utilization',p.M/p.Mref,'-'],['Illustrative combined index',u,'-']],x:'Axial force P (kN)',note:'The simplified boundary neglects second-order amplification, biaxial interaction, member stability, local buckling and code-prescribed interaction forms.'}}},
 pdelta:{title:'Second-order P–Δ amplification',unit:5,why:'Visualize how a simple geometric amplification estimate diverges near the ideal Euler instability load.',assumptions:'Linearized single-mode geometric approximation delta = delta0/(1 − P/Pcr), valid only below Pcr. A real frame requires stiffness analysis, imperfections and load combinations.',inputs:[['P','Compression load (kN)',50,1800,450,25],['Pcr','Ideal elastic critical load (kN)',200,2500,1250,25],['d0','First-order sway (mm)',1,90,15,1]],calc:p=>{let ratio=p.P/p.Pcr,amp=ratio>=1?null:1/(1-ratio),curve=lin(140,q=>{let r=.02+.95*q;return [r,p.d0/(1-r)]});return {series:[['Amplified lateral displacement (mm)',curve]],metrics:[['P/Pcr',ratio,'-'],['Amplification factor',amp===null?'unstable idealization':amp,'-'],['Amplified sway',amp===null?'not defined':p.d0*amp,'mm']],x:'Compression ratio P/Pcr',note:ratio>=1?'P ≥ Pcr: the idealized linear-equilibrium expression has no stable solution.':'Near Pcr the estimate becomes extremely sensitive. Actual buckling loads and stiffness may differ from the assumed Pcr.'}}},
 bolt:{title:'Eccentrically loaded four-bolt group',unit:6,why:'Resolve direct shear and elastic secondary shear in a rectangular four-bolt arrangement; see the effect of pitch and eccentricity.',assumptions:'Four identical bolts at ±px/2 and ±py/2; planar elastic bolt-group method with rigid plate and equal bolt stiffness. No prying, slip, bearing, yielding or interaction-based design checks.',inputs:[['V','Vertical shear V (kN)',20,400,120,5],['e','Shear eccentricity e (mm)',0,350,100,5],['px','Horizontal pitch (mm)',50,300,140,5],['py','Vertical pitch (mm)',50,300,110,5]],calc:p=>{let pts=[[-p.px/2,-p.py/2],[p.px/2,-p.py/2],[p.px/2,p.py/2],[-p.px/2,p.py/2]],J=pts.reduce((a,[x,y])=>a+x*x+y*y,0),M=p.V*p.e,rs=pts.map(([x,y])=>Math.hypot(-M*y/J,p.V/4+M*x/J));return {series:[['Bolt force (kN)',rs.map((r,i)=>[i+1,r])]],metrics:[['Direct shear per bolt',p.V/4,'kN'],['Group torsional moment',M/1000,'kN·m'],['Largest bolt resultant',Math.max(...rs),'kN']],x:'Bolt index (1–4)',note:'The sign of secondary shear follows the chosen load convention. Verify vector equilibrium and design each bolt, connected plate and weld separately.'}}},
 weld:{title:'Fillet-weld throat demand',unit:6,why:'Compare simple direct shear stress for two parallel fillet-weld lines with weld size and total effective length.',assumptions:'Two straight welds of equal effective length, direct shear only, uniform load sharing and throat = 0.707 × leg size. No eccentricity, directionality, weld strength or fatigue rules.',inputs:[['V','Applied shear (kN)',10,550,160,10],['s','Fillet leg size (mm)',3,16,6,0.5],['L','Effective length of each weld (mm)',30,450,180,5]],calc:p=>{let f=L=>p.V*1000/(2*0.707*p.s*L);return {series:[['Illustrative average throat shear (MPa)',lin(110,q=>{let L=30+420*q;return [L,f(L)]})]],metrics:[['Total effective throat area',2*.707*p.s*p.L,'mm²'],['Average shear stress',f(p.L),'MPa'],['Per-line shear force',p.V/2,'kN']],x:'Effective length of each weld (mm)',note:'Actual welding procedures and strength checks use the governing welding and structural codes; leg size is not directly throat size.'}}},
 truss:{title:'Two-bar braced roof apex',unit:7,why:'Explore axial force and horizontal spread demand as the angle of two symmetric inclined bars changes.',assumptions:'Two equal pin-connected bars forming an idealized triangular truss; centered downward nodal load, axial forces only; stable lower supports; no chord effects or buckling capacity checks.',inputs:[['P','Apex downward force (kN)',10,550,125,5],['angle','Bar angle to horizontal (deg)',15,75,35,1],['L','Horizontal half-span (m)',1,8,3.5,0.25]],calc:p=>{let a=p.angle*Math.PI/180,F=p.P/(2*Math.sin(a)),curve=lin(120,q=>{let t=15+60*q;return [t,p.P/(2*Math.sin(t*Math.PI/180))]});return {series:[['Axial compression magnitude per bar (kN)',curve]],metrics:[['Force in each inclined bar',F,'kN'],['Horizontal reaction magnitude',F*Math.cos(a),'kN'],['Truss rise',p.L*Math.tan(a),'m']],x:'Bar angle to horizontal (deg)',note:'The diagonal bars are compressive for the stated geometry and loading. Individual compression resistance, member stability and joint capacities are not included.'}}},
 corrosion:{title:'Section loss and steel durability',unit:8,why:'See how assumed uniform metal loss reduces steel cross-sectional area over time; connect maintenance assumptions to structural capacity.',assumptions:'Uniform corrosion on both broad faces of a rectangular plate, constant penetration rate, constant width, no pits, fatigue, coating deterioration or electrochemical coupling. Illustrative only.',inputs:[['b','Plate width (mm)',100,500,220,10],['t','Initial plate thickness (mm)',6,40,16,1],['rate','Uniform penetration per exposed face (mm/year)',0,0.25,0.035,0.005],['years','Elapsed years',0,80,30,1],['fy','Yield strength (MPa)',200,550,355,5]],calc:p=>{let thick=y=>Math.max(0,p.t-2*p.rate*y),a=p.b*thick(p.years),curve=lin(120,q=>{let y=80*q;return [y,p.b*thick(y)*p.fy/1000]});return {series:[['Gross yield-force idealization (kN)',curve]],metrics:[['Remaining thickness',thick(p.years),'mm'],['Remaining gross area',a,'mm²'],['Area retained',100*a/(p.b*p.t),'%']],x:'Years since exposure',note:'The assumed loss rate is arbitrary and must NOT be treated as a forecast. Local pitting, crevice corrosion, stress and inspection history matter.'}}}
};

  function formatNum(x){if(typeof x==='string')return x;if(!Number.isFinite(x))return '—';return Number(x).toLocaleString(undefined,{maximumFractionDigits:3})}
function node(name,attributes={}){const n=document.createElementNS('http://www.w3.org/2000/svg',name);for(const [k,v] of Object.entries(attributes))n.setAttribute(k,v);return n}
function plot(svg,sets,xlab){svg.replaceChildren();svg.setAttribute('viewBox','0 0 860 410');svg.setAttribute('role','img');svg.setAttribute('aria-label','Live engineering result chart');let all=sets.flatMap(s=>s[1]).filter(v=>Array.isArray(v)&&Number.isFinite(v[0])&&Number.isFinite(v[1]));if(!all.length)return;let loX=Math.min(...all.map(v=>v[0])),hiX=Math.max(...all.map(v=>v[0])),loY=Math.min(...all.map(v=>v[1])),hiY=Math.max(...all.map(v=>v[1]));if(loX===hiX)hiX+=1;if(loY===hiY){loY-=1;hiY+=1}let py=(hiY-loY)*.08;loY-=py;hiY+=py;const X=x=>65+(x-loX)*740/(hiX-loX),Y=y=>337-(y-loY)*270/(hiY-loY);for(let i=0;i<6;i++){let x=65+148*i,y=67+54*i;svg.append(node('line',{x1:65,y1:y,x2:805,y2:y,stroke:'#35516c','stroke-width':'1'}));svg.append(node('line',{x1:x,y1:67,x2:x,y2:337,stroke:'#35516c','stroke-width':'1'}));for(let [tx,ty,fmt,anchor] of [[59,y+4,formatNum(hiY-(hiY-loY)*i/5),'end'],[x,357,formatNum(loX+(hiX-loX)*i/5),'middle']]){const t=node('text',{x:tx,y:ty,fill:'#b9cad7','font-size':12,'text-anchor':anchor});t.textContent=fmt;svg.append(t)}}const colors=['#3cdbbb','#f1b96c','#b7a5fa'];sets.forEach((series,i)=>{let vals=series[1].filter(v=>Number.isFinite(v[0])&&Number.isFinite(v[1]));if(vals.length>1)svg.append(node('polyline',{points:vals.map(v=>X(v[0]).toFixed(2)+','+Y(v[1]).toFixed(2)).join(' '),fill:'none',stroke:colors[i%3],'stroke-width':3,'stroke-linejoin':'round'}));let k=node('text',{x:68+(i%2)*365,y:23+18*Math.floor(i/2),fill:colors[i%3],'font-size':13});k.textContent=series[0];svg.append(k)});let xx=node('text',{x:440,y:398,fill:'#ccdbe4','text-anchor':'middle','font-size':14});xx.textContent=xlab;svg.append(xx)}
function scheme(svg,key,p){svg.replaceChildren();svg.setAttribute('viewBox','0 0 760 128');let line=(x1,y1,x2,y2,c='#64dfc1',w=4)=>svg.append(node('line',{x1,y1,x2,y2,stroke:c,'stroke-width':w,'stroke-linecap':'round'}));let label=(x,y,s)=>{let t=node('text',{x,y,fill:'#cbdfea','font-size':14});t.textContent=s;svg.append(t)};let rect=(x,y,w,h,color='#244966')=>svg.append(node('rect',{x,y,width:w,height:h,rx:5,fill:color}));if(['beam','lt','defl','combined','pdelta'].includes(key)){line(155,82,580,82,'#7bc6df',12);line(160,88,145,110,'#dfb771');line(160,88,175,110,'#dfb771');line(575,88,561,110,'#dfb771');line(575,88,589,110,'#dfb771');for(let x=215;x<=550;x+=67){line(x,20,x,64,'#f0ad77',2)}label(22,32,'Beam / member');label(610,65,'ideal supports')}
else if(['euler','columns','local','corrosion','steel'].includes(key)){rect(310,10,95,96);line(357,3,357,16,'#df9e71');label(18,34,'Prismatic steel member');label(485,65,'Idealized profile')}
else if(['bolt','holes','tension','weld'].includes(key)){rect(270,22,200,83);for(const xy of [[310,42],[430,42],[310,84],[430,84]])svg.append(node('circle',{cx:xy[0],cy:xy[1],r:8,fill:'#e8b66a'}));label(30,39,'Plate & connection');label(506,61,'schematic only')}
else if(key==='truss'){line(165,103,382,18,'#82d1e6',8);line(382,18,600,103,'#82d1e6',8);line(165,103,600,103,'#879fad',3);line(382,7,382,17,'#e4ab74',4);label(28,27,'Pinned two-bar truss');label(613,101,'support')}
else {rect(270,22,200,83);label(20,45,'Idealized member')}
}


  var MODELS_LIST = [];
  var modelKeys = Object.keys(S);

  modelKeys.forEach(function(key, idx) {
    var mDef = S[key];
    var unit = mDef.unit || 1;

    var controlsHtml = mDef.inputs.map(function(v) {
      var vid = v[0], label = v[1], min = v[2], max = v[3], def = v[4], step = v[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ssd_' + key + '_' + vid + '">' + label + ' <span id="v_ssd_' + key + '_' + vid + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="ssd_' + key + '_' + vid + '" data-var="' + vid + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.about + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="schematic" style="margin:1rem 0;display:block;"><svg class="sch-svg" viewBox="0 0 760 128" style="width:100%;height:auto;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 860 410" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {
        try {
          var p = {};
          mDef.inputs.forEach(function(v) { p[v[0]] = v[4]; });
          var metricsEl = card.querySelector('.metrics');
          var schSvg = card.querySelector('.sch-svg');
          var plotSvg = card.querySelector('.plot-svg');
          var noteEl = card.querySelector('.model-note');

          function updateSteel() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var vid = inp.dataset.var;
              p[vid] = Number(inp.value);
              var vLbl = card.querySelector('#v_ssd_' + key + '_' + vid);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var out = mDef.calc(p);
            if (metricsEl && out.metrics) {
              metricsEl.innerHTML = out.metrics.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? formatNum(m[1]) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }).join('');
            }

            if (schSvg) {
              scheme(schSvg, key, p);
            }

            if (plotSvg && out.series) {
              plot(plotSvg, out.series, out.xLabel || 'Parameter');
            }

            if (noteEl) noteEl.textContent = out.note || mDef.assumptions || '';
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateSteel);
          });
          updateSteel();
        } catch (err) {
          console.warn('Steel Structure sim error in model ' + key + ':', err);
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
