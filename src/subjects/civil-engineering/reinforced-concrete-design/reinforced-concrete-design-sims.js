/* Reinforced Concrete Design Interactive Simulation Suite */
(function(window) {
  'use strict';

  const RC_MODELS = {
  loads:{title:'Load paths and illustrative beam envelopes',unit:1,about:'Compare dead and live line loads using an explicitly illustrative factored combination. A simply supported beam has linear shear and parabolic bending moment for uniform loading.',assumptions:'One span, pin and roller supports, uniformly distributed gravity load, 1.2D + 1.6L used solely as a teaching example; local load combinations may differ.',vars:[['D','Dead load D (kN/m)',2,30,6,.5],['L','Live load L (kN/m)',0,25,8,.5],['span','Span (m)',2,12,6,.25]],calc:p=>{let w=1.2*p.D+1.6*p.L,R=w*p.span/2,M=w*p.span*p.span/8;return {metrics:[['Illustrative factored line load',w,'kN/m'],['Each support reaction',R,'kN'],['Maximum sagging moment',M,'kN·m']],series:[['Bending moment (kN·m)',points(100,x=>[x*p.span,w*x*p.span*(p.span-x*p.span)/2])],['Shear force (kN)',points(100,x=>[x*p.span,R-w*x*p.span])]],xLabel:'Position along beam (m)',note:'Concentrated loads, continuity, pattern loading, load paths and actual jurisdiction-specific combinations are not represented.'}}},
  flexure:{title:'Singly reinforced rectangular-section flexure',unit:2,about:'Explore the equilibrium of a rectangular compression block and yielded reinforcing steel in a simplified nominal flexural resistance model.',assumptions:'Steel yielding assumed; concrete stress block 0.85 f′c; constant beta1=0.85 for introductory illustration, not a general current-code prescription; no strength-reduction factor.',vars:[['fc','Concrete f′c (MPa)',20,50,30,1],['fy','Rebar fy (MPa)',300,600,420,10],['b','Beam width b (mm)',200,500,300,10],['d','Effective depth d (mm)',300,750,500,10],['As','Tension steel As (mm²)',300,4200,1600,50]],calc:p=>{let a=p.As*p.fy/(.85*p.fc*p.b),c=a/.85,eps=.003*(p.d-c)/c,M=p.As*p.fy*(p.d-a/2)/1e6;return {metrics:[['Compression-block depth a',a,'mm'],['Nominal moment Mn',M,'kN·m'],['Steel strain proxy',eps*1000,'‰']],series:[['Moment versus steel area (kN·m)',points(100,t=>{let A=200+4000*t, aa=A*p.fy/(.85*p.fc*p.b);return [A,A*p.fy*(p.d-aa/2)/1e6]})]],xLabel:'Tension reinforcement area (mm²)',note:(a>=p.d?'WARNING: compression block exceeds effective depth; simplified model is invalid. ':'')+'Nominal strength only. Check strain domain, minimum/maximum reinforcement, development, cover, detailing, deflection and governing code.'}}},
  shear:{title:'Concrete and stirrup shear-force components',unit:3,about:'Study a simple additive shear model and the influence of stirrup spacing, concrete strength and steel yield strength.',assumptions:'Demonstration form Vc=0.17 sqrt(f′c) bwd and Vs=Av fy d/s for vertical reinforcement in SI units, with neither phi factors nor full code limits.',vars:[['fc','Concrete f′c (MPa)',20,60,32,1],['bw','Web width bw (mm)',200,450,280,10],['d','Effective depth d (mm)',250,700,500,10],['Av','Stirrup area Av (mm²)',50,400,160,10],['fy','Stirrup yield fy (MPa)',250,600,420,10],['s','Stirrup spacing s (mm)',75,350,175,5]],calc:p=>{let Vc=.17*Math.sqrt(p.fc)*p.bw*p.d/1000,Vs=p.Av*p.fy*p.d/(p.s*1000);return {metrics:[['Concrete-model contribution',Vc,'kN'],['Stirrup-model contribution',Vs,'kN'],['Sum (not design strength)',Vc+Vs,'kN']],series:[['Sum versus stirrup spacing (kN)',points(120,t=>{let s=75+275*t;return [s,Vc+p.Av*p.fy*p.d/(s*1000)]})]],xLabel:'Stirrup spacing (mm)',note:'This is not a code check: actual shear resistance depends on member type, size effects, axial stress, stirrup placement, minimum reinforcement and upper limits.'}}},
  slab:{title:'One-way slab strip response',unit:4,about:'Use a one-metre-wide idealized slab strip to link applied area pressure, maximum moment, support shear and gross-section short-term elastic deflection.',assumptions:'Simply supported one-way 1 m strip. Gross uncracked inertia and Ec=4700 sqrt(f′c) MPa approximate short-term stiffness; excludes cracking, creep and detailing.',vars:[['q','Uniform area load (kN/m²)',1,20,6,.5],['L','Clear span (m)',2,8,4,.25],['h','Thickness h (mm)',100,300,170,5],['fc','Concrete f′c (MPa)',20,50,30,1]],calc:p=>{let M=p.q*p.L*p.L/8,V=p.q*p.L/2,Ec=4700*Math.sqrt(p.fc),I=1000*Math.pow(p.h,3)/12,delta=5*p.q*Math.pow(p.L*1000,4)/(384*Ec*I);return {metrics:[['Strip moment',M,'kN·m/m'],['Strip shear',V,'kN/m'],['Uncracked elastic deflection',delta,'mm']],series:[['Moment versus span (kN·m/m)',points(100,t=>{let L=2+6*t;return [L,p.q*L*L/8]})],['Gross-elastic deflection (mm)',points(100,t=>{let L=2+6*t;return [L,5*p.q*Math.pow(L*1000,4)/(384*Ec*I)]})]],xLabel:'Span (m)',note:'A real slab may be two-way, continuous or edge-restrained; use governing structural system, factored loads, code moment methods and cracked long-term deflection checks.'}}},
  doubly:{title:'Doubly reinforced beam sectional equilibrium',unit:2,about:'A strain-compatible compression reinforcement contribution changes force equilibrium and available nominal bending resistance.',assumptions:'Rectangular equivalent block with beta1=0.85; yielded bottom tensile steel assumed; compression steel uses elastic-perfectly plastic law; no concrete compression-steel displacement correction.',vars:[['fc','Concrete f′c (MPa)',20,50,30,1],['fy','Steel fy (MPa)',300,600,420,10],['b','Width (mm)',200,500,300,10],['d','Tension depth d (mm)',350,750,525,5],['dp','Compression cover depth d′ (mm)',35,90,55,5],['As','Tension steel As (mm²)',800,4000,2400,50],['Ap','Compression steel As′ (mm²)',0,1800,650,25]],calc:p=>{let E=200000,beta=.85, C=c=>.85*p.fc*p.b*beta*c+ p.Ap*clamp(E*.003*(c-p.dp)/c,-p.fy,p.fy);let lo=1,hi=p.d*6,T=p.As*p.fy;for(let i=0;i<80;i++){let m=(lo+hi)/2;if(C(m)>T)hi=m;else lo=m};let c=(lo+hi)/2,a=beta*c,fs=clamp(E*.003*(c-p.dp)/c,-p.fy,p.fy),Mn=(T*(p.d-a/2)+p.Ap*fs*(a/2-p.dp))/1e6;return {metrics:[['Neutral-axis depth c',c,'mm'],['Compression steel stress fs′',fs,'MPa'],['Nominal section moment',Mn,'kN·m']],series:[['Nominal moment versus compression steel (kN·m)',points(80,t=>{let Ap=t*1800,T=p.As*p.fy,lo=1,hi=4*p.d;for(let j=0;j<55;j++){let mm=(lo+hi)/2;let cc=.85*p.fc*p.b*.85*mm+Ap*clamp(E*.003*(mm-p.dp)/mm,-p.fy,p.fy);if(cc>T)hi=mm;else lo=mm};let c=(lo+hi)/2,aa=.85*c,ss=clamp(E*.003*(c-p.dp)/c,-p.fy,p.fy);return [Ap,(T*(p.d-aa/2)+Ap*ss*(aa/2-p.dp))/1e6]})]],xLabel:'Compression steel area (mm²)',note:'Assumption of yielded tension reinforcement may be false for heavily reinforced sections; examine tension strain and displacement of concrete before any design use.'}}},
  column:{title:'Column axial–moment interaction (fiber-like strain compatibility)',unit:5,about:'Trace an idealized P–M interaction curve as the neutral-axis depth changes. Vary reinforcement, section dimensions and concrete strength.',assumptions:'Symmetric two-layer steel, linear strain variation and upper-fiber concrete strain 0.003; equivalent rectangular stress block beta1=0.85; nominal resistance only.',vars:[['fc','Concrete f′c (MPa)',20,55,32,1],['fy','Steel fy (MPa)',300,600,420,10],['b','Column width (mm)',250,650,400,10],['h','Column depth (mm)',250,700,450,10],['Ast','Total steel Ast (mm²)',400,5500,2400,100],['cover','Layer center cover (mm)',35,90,55,5]],calc:p=>{let results=points(120,t=>{let c=15+3*p.h*t,a=Math.min(.85*c,p.h),Fcon=.85*p.fc*p.b*a;let P=Fcon,M=Fcon*(p.h/2-a/2);for(let y of [p.cover,p.h-p.cover]){let eps=.003*(c-y)/c,Fs=p.Ast/2*clamp(200000*eps,-p.fy,p.fy);P+=Fs;M+=Fs*(p.h/2-y)}return [P/1000,M/1e6]});let maxM=Math.max(...results.map(a=>a[1]));return {metrics:[['Peak sampled nominal moment',maxM,'kN·m'],['Peak sampled compression',Math.max(...results.map(a=>a[0])),'kN'],['Total steel ratio',100*p.Ast/(p.b*p.h),'%']],series:[['Nominal P–M locus (M versus P)',results]],xLabel:'Nominal axial force P (kN)',note:'Not a code interaction diagram. No phi factor, confinement, slenderness, biaxial effects, eccentricity minima, tie design, or cover/spacing checks. Negative axial values are tensile states.'}}},
  footprint:{title:'Isolated footing: soil bearing, bending and punching demands',unit:6,about:'Investigate how footing plan dimension changes nominal uniform soil reaction, one-way cantilever demand and an average punching-shear stress.',assumptions:'Rigid square footing, centered vertical load, uniform reaction, square column; punching control perimeter approximated at distance d/2 from column face.',vars:[['P','Column service load (kN)',400,3200,1200,50],['B','Footing width B (m)',1.5,4.5,2.8,.1],['c','Column width c (m)',.25,.7,.45,.01],['d','Effective depth d (mm)',250,750,500,10]],calc:p=>{let q=p.P/(p.B*p.B),a=(p.B-p.c)/2,M=q*a*a/2,b0=4*(p.c+p.d/1000),Vu=q*(p.B*p.B-Math.pow(p.c+p.d/1000,2)),vp=Vu/(b0*p.d/1000);return {metrics:[['Uniform soil pressure',q,'kPa'],['Cantilever moment per metre',M,'kN·m/m'],['Approx. punching stress',vp,'kPa']],series:[['Bearing pressure versus footing width (kPa)',points(100,t=>{let b=1.5+3*t;return [b,p.P/(b*b)]})],['Punching stress versus width (kPa)',points(100,t=>{let b=Math.max(p.c+p.d/1000+.01,1.5+3*t),qq=p.P/b**2;return [b,qq*(b*b-(p.c+p.d/1000)**2)/(b0*p.d/1000)]})]],xLabel:'Footing width B (m)',note:'If B is smaller than c+d, the control perimeter is outside the footing and this simplified punching formula fails. Geotechnical pressure, settlement, overturning and building-code resistance are omitted.'}}},
  bond:{title:'Development length as bond-force transfer',unit:7,about:'Balance a steel bar axial force against average circumferential bond shear, then reveal why bar diameter and assumed bond stress affect transfer length.',assumptions:'Uniform interfacial bond stress τ, perfect circular bar, steel force Abar fy, ignoring splitting, confinement and anchorage specifics; purely mechanics-based surrogate.',vars:[['db','Bar diameter db (mm)',10,40,20,1],['fy','Bar yield strength fy (MPa)',300,600,420,10],['tau','Assumed average bond stress τ (MPa)',1,6,2.5,.1]],calc:p=>{let ld=p.db*p.fy/(4*p.tau);return {metrics:[['Theoretical transfer length',ld,'mm'],['Length in bar diameters',ld/p.db,'db'],['Bar tensile force',Math.PI*p.db*p.db*p.fy/4000,'kN']],series:[['Idealized steel stress (MPa)',points(100,t=>{let x=t*ld*1.3;return [x,Math.min(p.fy,4*p.tau*x/p.db)]})]],xLabel:'Embedded length (mm)',note:'Do not use as a code development length. Actual anchorage depends on concrete strength, cover, transverse reinforcement, coating, bar position, hooks and confinement.'}}},
  cracking:{title:'Crack width and strain transfer thought experiment',unit:7,about:'Explore how effective crack spacing and average steel–concrete strain difference influence an approximate visible surface crack opening.',assumptions:'Uniform mean strain difference Δε over mean spacing s: w≈sΔε, without a calibrated code-specific crack-spacing or tension-stiffening equation.',vars:[['s','Mean crack spacing (mm)',40,350,150,5],['eps','Mean strain difference (µstrain)',50,2000,650,25],['scale','Strain-transfer multiplier',.5,1.5,1,.05]],calc:p=>{let w=p.s*p.eps*1e-6*p.scale;return {metrics:[['Idealized crack width',w,'mm'],['Mean crack spacing',p.s,'mm'],['Strain difference',p.eps,'µε']],series:[['Crack width versus strain difference (mm)',points(100,t=>{let eps=50+1950*t;return [eps,p.s*eps*1e-6*p.scale]})]],xLabel:'Mean strain difference (µstrain)',note:'A real crack-width calculation requires reinforcement spacing, cover, bond, tension stiffening, loading duration and an applicable serviceability method.'}}},
  deflection:{title:'Cracked transformed section and immediate deflection',unit:7,about:'Solve the cracked-section neutral axis by transformed-area equilibrium and use the resulting stiffness in a basic beam deflection estimate.',assumptions:'Singly reinforced rectangular beam under uniform load; zero concrete tension; linear elastic steel; constant fully cracked EI; simply supported beam, immediate deflection only.',vars:[['fc','Concrete f′c (MPa)',20,50,30,1],['b','Beam width (mm)',200,450,300,10],['d','Steel effective depth (mm)',300,700,500,10],['As','Steel area (mm²)',400,3500,1600,50],['w','Uniform beam load (kN/m)',2,22,8,.5],['L','Span (m)',3,10,6,.25]],calc:p=>{let Ec=4700*Math.sqrt(p.fc),n=200000/Ec,B=n*p.As,xx=(-B+Math.sqrt(B*B+2*p.b*B*p.d))/p.b,I=p.b*xx**3/3+B*(p.d-xx)**2,def=5*p.w*(1000*p.L)**4/(384*Ec*I);return {metrics:[['Cracked neutral axis',xx,'mm'],['Cracked inertia Icr',I/1e6,'×10⁶ mm⁴'],['Immediate deflection estimate',def,'mm']],series:[['Immediate deflection versus span (mm)',points(110,t=>{let L=3+7*t;return [L,5*p.w*(1000*L)**4/(384*Ec*I)]})]],xLabel:'Span (m)',note:'No effective inertia, creep, shrinkage, tensile concrete, slab participation or actual load-history effects. The fully cracked constant-stiffness approximation may be conservative or unconservative in specific cases.'}}},
  layout:{title:'Reinforcement fit, clear spacing and section geometry',unit:7,about:'See the geometric consequences of increasing bar diameter or bar count inside a rectangular beam cage.',assumptions:'One horizontal row of equal bars, symmetric arrangement, centerline approximation, nominal rectangular stirrup; no aggregate sizing, tolerance or multilayer analysis.',vars:[['b','Beam width (mm)',200,500,300,10],['cover','Clear cover (mm)',20,70,40,5],['stirrup','Stirrup diameter (mm)',6,16,10,1],['db','Longitudinal bar diameter (mm)',12,36,20,2],['n','Number of bottom bars',2,7,4,1]],calc:p=>{let As=p.n*Math.PI*p.db*p.db/4,clear=(p.b-2*(p.cover+p.stirrup)-p.n*p.db)/(p.n-1);return {metrics:[['Total steel area',As,'mm²'],['Clear bar-to-bar spacing',clear,'mm'],['Free inside width',p.b-2*(p.cover+p.stirrup),'mm']],series:[['Clear spacing versus bar count (mm)',points(6,t=>{let n=2+Math.round(t*5);return [n,(p.b-2*(p.cover+p.stirrup)-n*p.db)/(n-1)]})]],xLabel:'Number of bars in one row',note:(clear<0?'WARNING: Bars geometrically overlap in this arrangement. ':'')+'Check actual code minimum clear spacing, aggregate size, bend radii, development, constructability and tolerance.'}}},
  wall:{title:'Cantilever lateral response of an idealized shear wall',unit:6,about:'A lateral load applied to a wall top produces base moment, curvature and elastic drift that increase strongly with wall height.',assumptions:'Homogeneous linearly elastic cantilever, lumped horizontal force at roof, constant uncracked flexural rigidity; ignores axial interaction, shear deformation and cracking.',vars:[['F','Top horizontal force (kN)',20,450,140,10],['H','Wall height (m)',3,20,9,.5],['EI','Effective EI (MN·m²)',5,600,110,5]],calc:p=>{let drift=p.F*p.H**3/(3*p.EI),M=p.F*p.H;return {metrics:[['Elastic roof drift',drift,'mm'],['Base overturning moment',M,'kN·m'],['Drift ratio',100*drift/(1000*p.H),'%']],series:[['Wall lateral deformation (mm)',points(110,t=>{let x=t*p.H,df=p.F*x*x*(3*p.H-x)/(6*p.EI);return [x,df]})]],xLabel:'Elevation above base (m)',note:'This is a flexural cantilever analogy, not reinforced-concrete shear-wall seismic design. Ductility, inelasticity, coupling, shear demand and P-delta effects are absent.'}}},
  durability:{title:'Cover versus an idealized carbonation front',unit:8,about:'Probe the square-root-of-time surrogate used to discuss carbonation depth and how cover changes exposure time before a front reaches reinforcement.',assumptions:'x=k sqrt(t) for constant environment and fixed k. No direct prediction of steel corrosion or service life; cover and exposure quality must be measured.',vars:[['k','Front coefficient k (mm/√year)',1,9,4,.25],['cover','Concrete cover (mm)',20,80,40,5],['years','Exposure duration (years)',1,100,40,1]],calc:p=>{let depth=p.k*Math.sqrt(p.years),threshold=(p.cover/p.k)**2;return {metrics:[['Estimated front depth',depth,'mm'],['Illustrative cover arrival',threshold,'years'],['Remaining front-to-steel cover',p.cover-depth,'mm']],series:[['Estimated front penetration (mm)',points(101,t=>{let y=t*100;return [y,p.k*Math.sqrt(y)]})],['Rebar cover (mm)',[[0,p.cover],[100,p.cover]]]],xLabel:'Exposure time (years)',note:'Cracking, wetting/drying, binder chemistry, curing, chlorides and oxygen transport can invalidate a fixed k; no durability certification follows.'}}},
  eccentric:{title:'Axial load eccentricity and uncracked stress gradients',unit:5,about:'Compare a concentric compressive stress with flexural stress caused by a shifted resultant in an uncracked rectangular gross section.',assumptions:'Linear elasticity and uncracked cross section; no tension cutoff, confined concrete effects or strength limit; simple eccentric compressive load.',vars:[['P','Axial compressive load P (kN)',100,2500,900,50],['b','Section width (mm)',250,600,400,10],['h','Section depth (mm)',250,700,500,10],['e','Eccentricity (mm)',0,200,55,5]],calc:p=>{let sigma=p.P*1000/(p.b*p.h),sflex=6*p.P*1000*p.e/(p.b*p.h*p.h);return {metrics:[['Average axial compression',sigma,'MPa'],['Maximum edge compression',sigma+sflex,'MPa'],['Opposite edge stress',sigma-sflex,'MPa']],series:[['Gross linear stress across depth (MPa)',points(100,t=>[t*p.h,sigma+sflex*(1-2*t)])]],xLabel:'Depth coordinate (mm)',note:(sigma-sflex<0?'Tension occurs in the gross elastic calculation, so the uncracked assumption is likely invalid. ':'')+'Eccentric-column design requires interaction, ties/spirals, slenderness and design reduction factors.'}}},
  variability:{title:'Sensitivity of nominal moment to uncertain inputs',unit:8,about:'A deterministic ensemble of small independent input variations shows sensitivity; it is not a structural reliability analysis or probability of failure.',assumptions:'Educational ± ranges: concrete ±15%, steel area ±8%, effective depth ±5%. Samples use deterministic sequences, not calibrated probability distributions.',vars:[['fc','Nominal f′c (MPa)',20,55,32,1],['b','Section width (mm)',200,450,300,10],['d','Nominal effective depth (mm)',300,700,520,10],['As','Nominal steel area (mm²)',600,3400,1700,50],['fy','Steel yield fy (MPa)',300,600,420,10],['Mu','Illustrative demand (kN·m)',50,750,300,10]],calc:p=>{let vals=[],n=141;for(let i=0;i<n;i++){let fc=p.fc*(1+.15*Math.sin(i*2.23)),A=p.As*(1+.08*Math.sin(i*1.81+.3)),d=p.d*(1+.05*Math.sin(i*2.71+1.1)),a=A*p.fy/(.85*fc*p.b),Mn=A*p.fy*(d-a/2)/1e6;vals.push([i,Mn]);}let min=Math.min(...vals.map(v=>v[1])),max=Math.max(...vals.map(v=>v[1])),unders=vals.filter(v=>v[1]<p.Mu).length;return {metrics:[['Minimum sampled Mn',min,'kN·m'],['Maximum sampled Mn',max,'kN·m'],['Samples below demand',unders+'/'+n,'cases']],series:[['Nominal moment across cases (kN·m)',vals],['Selected demand (kN·m)',[[0,p.Mu],[n-1,p.Mu]]]],xLabel:'Deterministic illustrative sample',note:'“Cases below demand” is not a calibrated failure probability. Strength reduction, correlated uncertainties, model error and probability distributions are excluded.'}}}
};

  function points(N,fn){return Array.from({length:N+1},(_,i)=>fn(i/N))}
function clamp(x,a,b){return Math.max(a,Math.min(b,x))}
function fmt(n){if(typeof n==='string')return n;return !Number.isFinite(n)?'invalid':Math.abs(n)>=10000?n.toLocaleString(undefined,{maximumFractionDigits:0}):n.toLocaleString(undefined,{maximumFractionDigits:3})}
function svgElem(tag,attrs={}){let e=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));return e}
function schematic(key,p){let el=document.createElementNS('http://www.w3.org/2000/svg','svg');el.setAttribute('viewBox','0 0 660 128');el.setAttribute('role','img');el.setAttribute('aria-label','Schematic of the idealized concrete member and external actions');el.classList.add('scheme');const l=(x1,y1,x2,y2,color='#43a2b7',width=2)=>el.append(svgElem('line',{x1,y1,x2,y2,stroke:color,'stroke-width':width}));const rect=(x,y,w,h,fill='#294d65')=>el.append(svgElem('rect',{x,y,width:w,height:h,fill,rx:4}));const tx=(x,y,t)=>{let o=svgElem('text',{x,y,fill:'#d9e8f4','font-size':13});o.textContent=t;el.append(o)};
if(['flexure','doubly','shear','layout','deflection','cracking','bond'].includes(key)){rect(180,23,280,75);for(let i=0;i<4;i++){el.append(svgElem('circle',{cx:205+i*77,cy:84,r:6,fill:'#e9b46a'}))}tx(15,27,'Concrete section / member');tx(492,61,'Steel (gold)');tx(492,81,'Concrete (blue)');if(key==='doubly'){for(let i=0;i<4;i++){el.append(svgElem('circle',{cx:205+i*77,cy:37,r:5,fill:'#e9b46a'}))}}}
else if(['column','eccentric','wall','variability'].includes(key)){rect(275,14,120,98);for(let y of [27,98]){el.append(svgElem('circle',{cx:296,cy:y,r:5,fill:'#e9b46a'}));el.append(svgElem('circle',{cx:375,cy:y,r:5,fill:'#e9b46a'}))}l(335,0,335,15,'#ed9367',4);tx(350,14,'P or lateral F');tx(30,28,'Idealized section')}
else if(key==='footprint'){rect(210,20,230,88);rect(292,38,66,48,'#dc9367');tx(25,33,'Square footing');tx(460,37,'Central column');}
else if(key==='durability'){rect(205,22,245,83);l(237,22,237,105,'#ed9367',4);l(390,22,390,105,'#e9b46a',5);tx(15,31,'Front (orange)');tx(468,43,'Steel (gold)')}
else {l(142,87,520,87,'#72c8d2',10);for(let i=0;i<12;i++){let x=150+i*33;l(x,21,x,69,'#f1af69',2);el.append(svgElem('path',{d:`M${x-5} 61L${x} 70L${x+5} 61`,fill:'none',stroke:'#f1af69','stroke-width':2}))}tx(30,22,'Idealized beam/slab');tx(540,90,'support')}
return el}
function drawPlot(svg,sets,xLabel){let all=sets.flatMap(x=>x[1]).filter(v=>Number.isFinite(v[0])&&Number.isFinite(v[1]));svg.replaceChildren();svg.setAttribute('viewBox','0 0 820 360');svg.setAttribute('role','img');svg.setAttribute('aria-label','Interactive Cartesian plot '+xLabel);if(!all.length)return;let minX=Math.min(...all.map(x=>x[0])),maxX=Math.max(...all.map(x=>x[0])),minY=Math.min(...all.map(x=>x[1])),maxY=Math.max(...all.map(x=>x[1]));if(maxX===minX)maxX+=1;if(maxY===minY){maxY+=1;minY-=1}let pad=(maxY-minY)*.08;minY-=pad;maxY+=pad;let X=x=>60+(x-minX)/(maxX-minX)*725,Y=y=>310-(y-minY)/(maxY-minY)*265;for(let i=0;i<=5;i++){let yy=45+i*53;svg.append(svgElem('line',{x1:60,x2:785,y1:yy,y2:yy,stroke:'#40556a','stroke-width':1}));let num=svgElem('text',{x:55,y:yy+4,'text-anchor':'end',fill:'#9db8c8','font-size':11});num.textContent=fmt(maxY-i*(maxY-minY)/5);svg.append(num)}for(let i=0;i<=6;i++){let xx=60+i*725/6;svg.append(svgElem('line',{x1:xx,x2:xx,y1:45,y2:310,stroke:'#40556a','stroke-width':.7}));let num=svgElem('text',{x:xx,y:330,'text-anchor':'middle',fill:'#9db8c8','font-size':11});num.textContent=fmt(minX+i*(maxX-minX)/6);svg.append(num)}let palette=['#64dfcc','#f8bd67','#d9a6fb','#8bc5ff'];sets.forEach((entry,i)=>{let valid=entry[1].filter(x=>Number.isFinite(x[0])&&Number.isFinite(x[1]));if(valid.length<2)return;let path=svgElem('polyline',{points:valid.map(p=>X(p[0]).toFixed(1)+','+Y(p[1]).toFixed(1)).join(' '),fill:'none',stroke:palette[i%4],'stroke-width':3,'stroke-linejoin':'round'});svg.append(path);let lg=svgElem('text',{x:65+Math.min(i,2)*235,y:17+(Math.floor(i/3)*18),fill:palette[i%4],'font-size':12});lg.textContent=entry[0];svg.append(lg)});let label=svgElem('text',{x:420,y:351,'text-anchor':'middle',fill:'#d3e5ef','font-size':13});label.textContent=xLabel;svg.append(label)}


  var MODELS_LIST = [];
  var modelKeys = Object.keys(RC_MODELS);

  modelKeys.forEach(function(key, idx) {
    var mDef = RC_MODELS[key];
    var unit = mDef.unit || 1;

    var controlsHtml = mDef.vars.map(function(v) {
      var vid = v[0], label = v[1], min = v[2], max = v[3], def = v[4], step = v[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="rc_' + key + '_' + vid + '">' + label + ' <span id="v_rc_' + key + '_' + vid + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="rc_' + key + '_' + vid + '" data-var="' + vid + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.about + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="schematic" style="margin:1rem 0;display:block;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 860 380" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS_LIST.push({
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {
        try {
          var p = {};
          mDef.vars.forEach(function(v) { p[v[0]] = v[4]; });
          var metricsEl = card.querySelector('.metrics');
          var schEl = card.querySelector('.schematic');
          var plotSvg = card.querySelector('.plot-svg');
          var noteEl = card.querySelector('.model-note');

          function updateRC() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var vid = inp.dataset.var;
              p[vid] = Number(inp.value);
              var vLbl = card.querySelector('#v_rc_' + key + '_' + vid);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var out = mDef.calc(p);
            if (metricsEl && out.metrics) {
              metricsEl.innerHTML = out.metrics.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m[1] === 'number' ? fmt(m[1]) : m[1]) + ' ' + (m[2] || '') + '</output></div>';
              }).join('');
            }

            if (schEl) {
              while (schEl.firstChild) schEl.removeChild(schEl.firstChild);
              var sch = schematic(key, p);
              if (sch) schEl.appendChild(sch);
            }

            if (plotSvg && out.series) {
              drawPlot(plotSvg, out.series, out.xLabel || 'Position');
            }

            if (noteEl) noteEl.textContent = out.note || mDef.assumptions || '';
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateRC);
          });
          updateRC();
        } catch (err) {
          console.warn('Reinforced Concrete sim error in model ' + key + ':', err);
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
