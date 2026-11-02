/* Strength of Materials Interactive Simulation Suite */
(function(window) {
  'use strict';

  var svgNS = 'http://www.w3.org/2000/svg';
  var palette = ['#38bdf8', '#34d399', '#f472b6', '#facc15', '#a78bfa', '#fb923c'];
  var escapeHTML = function(s) { return String(s).replace(/[&<>"']/g, function(c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); };
  var f = function(n, d) { d = (d === undefined) ? 3 : d; return !Number.isFinite(n) ? '—' : Math.abs(n) >= 1e5 ? n.toExponential(2) : Number(n.toFixed(d)).toLocaleString('en-US', {maximumFractionDigits: d}); };
  var clamp = function(x, a, b) { return Math.max(a, Math.min(b, x)); };
  var arange = function(a, b, n) { return Array.from({length: n}, function(_, i) { return a + (b - a) * i / (n - 1); }); };
  var metric = function(k, val, unit, info) { return [k, val, unit || '', info || '']; };

  var definitions = {"axial": {"title": "Axial Bar Laboratory", "keys": ["pk", "lm", "amm", "eg"]}, "material": {"title": "Material Stress–Strain & Unloading", "keys": ["eg", "fy", "et", "eps"]}, "torsion": {"title": "Circular Shaft Torsion", "keys": ["tnm", "dmm", "lm", "gg"]}, "beamvm": {"title": "Beam Shear–Moment Designer", "keys": ["lm", "pk", "am", "qk"]}, "deflection": {"title": "Elastic Beam Deflection", "keys": ["lm", "pk", "qk", "eg", "imm"]}, "section": {"title": "Section Geometry Studio", "keys": ["bmm", "hmm", "hole"]}, "mohr": {"title": "Mohr’s Circle and Stress Rotation", "keys": ["sx", "sy", "txy", "angle"]}, "combined": {"title": "Combined Axial + Bending Stress", "keys": ["bmm", "hmm", "nk", "mkn"]}, "buckling": {"title": "Euler Column Stability", "keys": ["bmm", "hmm", "lm", "eg", "fy", "kfac"]}, "pressure": {"title": "Thin-Wall Pressure Cylinder", "keys": ["pmpa", "rmm", "tmm", "fy"]}, "gauge": {"title": "Strain-Gauge Bridge Measurement", "keys": ["pk", "amm", "eg", "gf", "vexc"]}, "fatigue": {"title": "Fatigue S–N Explorer", "keys": ["sa", "sref", "bexp"]}, "beamshear": {"title": "Rectangular Beam Shear Distribution", "keys": ["vk", "bmm", "hmm"]}};
  var controls = {"pk": {"label": "Axial/point load P", "min": 1, "max": 100, "step": 1, "val": 24, "unit": "kN"}, "lm": {"label": "Length L", "min": 0.5, "max": 10, "step": 0.1, "val": 3, "unit": "m"}, "amm": {"label": "Area A", "min": 100, "max": 2500, "step": 50, "val": 500, "unit": "mm²"}, "eg": {"label": "Elastic modulus E", "min": 20, "max": 230, "step": 5, "val": 200, "unit": "GPa"}, "fy": {"label": "Yield strength fy", "min": 80, "max": 700, "step": 10, "val": 250, "unit": "MPa"}, "et": {"label": "Tangent modulus Et", "min": 1, "max": 30, "step": 1, "val": 10, "unit": "GPa"}, "eps": {"label": "Total strain", "min": 0.0002, "max": 0.02, "step": 0.0002, "val": 0.006, "unit": "mm/mm"}, "tnm": {"label": "Torque T", "min": 20, "max": 1800, "step": 20, "val": 420, "unit": "N·m"}, "dmm": {"label": "Shaft diameter d", "min": 12, "max": 100, "step": 2, "val": 42, "unit": "mm"}, "gg": {"label": "Shear modulus G", "min": 10, "max": 110, "step": 2, "val": 77, "unit": "GPa"}, "am": {"label": "Point load position a", "min": 0.5, "max": 9, "step": 0.1, "val": 1.5, "unit": "m"}, "qk": {"label": "Uniform load w", "min": 0, "max": 18, "step": 0.5, "val": 3, "unit": "kN/m"}, "imm": {"label": "Second moment I", "min": 10, "max": 400, "step": 5, "val": 75, "unit": "×10⁶ mm⁴"}, "bmm": {"label": "Section width b", "min": 30, "max": 350, "step": 10, "val": 120, "unit": "mm"}, "hmm": {"label": "Section height h", "min": 40, "max": 500, "step": 10, "val": 220, "unit": "mm"}, "hole": {"label": "Centered hole scale", "min": 0, "max": 0.8, "step": 0.05, "val": 0.3, "unit": "ratio"}, "sx": {"label": "Normal stress σx", "min": -150, "max": 150, "step": 5, "val": 80, "unit": "MPa"}, "sy": {"label": "Normal stress σy", "min": -150, "max": 150, "step": 5, "val": 20, "unit": "MPa"}, "txy": {"label": "In-plane shear τxy", "min": -120, "max": 120, "step": 5, "val": 40, "unit": "MPa"}, "angle": {"label": "Plane normal θ", "min": -90, "max": 90, "step": 2, "val": 20, "unit": "°"}, "nk": {"label": "Axial force N (+ tension)", "min": -250, "max": 250, "step": 10, "val": 40, "unit": "kN"}, "mkn": {"label": "Bending moment M", "min": -40, "max": 40, "step": 1, "val": 18, "unit": "kN·m"}, "kfac": {"label": "End condition K", "min": 0.5, "max": 2, "step": 0.5, "val": 1, "unit": "K"}, "pmpa": {"label": "Internal pressure p", "min": 0.1, "max": 12, "step": 0.1, "val": 2, "unit": "MPa"}, "rmm": {"label": "Inner radius r", "min": 30, "max": 500, "step": 10, "val": 200, "unit": "mm"}, "tmm": {"label": "Wall thickness t", "min": 2, "max": 60, "step": 2, "val": 10, "unit": "mm"}, "gf": {"label": "Gauge factor GF", "min": 1.5, "max": 3, "step": 0.1, "val": 2.1, "unit": "ratio"}, "vexc": {"label": "Bridge excitation", "min": 1, "max": 12, "step": 0.5, "val": 5, "unit": "V"}, "sa": {"label": "Stress amplitude Sa", "min": 80, "max": 450, "step": 10, "val": 220, "unit": "MPa"}, "sref": {"label": "Reference amplitude at 10⁶ cycles", "min": 120, "max": 380, "step": 10, "val": 220, "unit": "MPa"}, "bexp": {"label": "Basquin exponent b", "min": -0.2, "max": -0.04, "step": 0.01, "val": -0.1, "unit": "ratio"}, "vk": {"label": "Beam shear V", "min": 1, "max": 80, "step": 1, "val": 15, "unit": "kN"}};

  function calc(labKey, v){
  const x=v,L=x.lm??3,E=(x.eg??200)*1000; let res;
  switch(labKey){
  case 'axial':{
   const stress=x.pk*1000/x.amm,eps=stress/E,delta=eps*L*1000;
   const rows=arange(0,L,101).map(s=>[s,s/L*delta,stress]);
   res={title:'Axial displacement along the bar',x:'Position along bar (m)',y:'Extension (mm)',columns:['position_m','extension_mm','stress_MPa'],rows,series:[{name:'Displacement',j:1}],metrics:[metric('Nominal axial stress',stress,'MPa'),metric('Average strain',eps*1e6,'µε'),metric('End elongation',delta,'mm'),metric('Elastic stiffness',E*x.amm/(L*1000)/1000,'kN/mm')],note:'Concentric tensile force; uniform area; small-strain linear isotropic elasticity. Positive stress means tension.'}; break;}
  case 'material':{
   const Ee=E,fy=x.fy,Et=x.et*1000,ey=fy/Ee,s=x.eps<=ey?Ee*x.eps:fy+Et*(x.eps-ey),pr=Math.max(0,x.eps-s/Ee);
   const rows=arange(0,0.022,121).map(e=>[e,e<=ey?Ee*e:fy+Et*(e-ey),e<=x.eps?s+(e-x.eps)*Ee:null]);
   const unload=arange(0,1,60).map(t=>[pr+(x.eps-pr)*t,s*t,null]);
   res={title:'Idealized bilinear loading with elastic unloading',x:'Engineering strain (mm/mm)',y:'Engineering stress (MPa)',columns:['strain','stress_loading_MPa','unload_reference_MPa'],rows,series:[{name:'Loading',j:1},{name:'Unloading',data:unload,j:1}],metrics:[metric('Current stress',s,'MPa'),metric('Yield strain',ey*1e6,'µε'),metric('Residual strain after unload',pr*1e6,'µε'),metric('Secant stiffness',s/x.eps/1000,'GPa')],note:'Phenomenological bilinear illustration. No cyclic hardening, necking or specimen fracture model.'};break;}
  case 'torsion':{
   const d=x.dmm,J=Math.PI*d**4/32,T=x.tnm*1000,r=d/2,tau=T*r/J,theta=T*L*1000/(x.gg*1000*J);
   const rows=arange(0,r,101).map(rr=>[rr,T*rr/J,theta*180/Math.PI]);
   res={title:'Radial shear stress in a circular shaft',x:'Distance from shaft axis (mm)',y:'Shear stress (MPa)',columns:['radius_mm','shear_stress_MPa','twist_deg'],rows,series:[{name:'τ(r)',j:1}],metrics:[metric('Maximum shear stress',tau,'MPa'),metric('Total angle of twist',theta*180/Math.PI,'°'),metric('Polar second moment J',J/1e6,'×10⁶ mm⁴'),metric('Torsional energy',0.5*(x.tnm)*theta,'J')],note:'Solid circular, linearly elastic shaft under uniform torque; end warping, keys and stress concentrations neglected.'};break;}
  case 'beamvm':{
   const a=clamp(x.am,0.05,L-0.05),Rb=(x.pk*a + x.qk*L*L/2)/L,Ra=x.pk+x.qk*L-Rb;
   const rows=arange(0,L,151).map(s=>[s,Ra-x.qk*s-(s>=a?x.pk:0),Ra*s-x.qk*s*s/2-x.pk*Math.max(0,s-a)]);
   const pmax=Math.max(...rows.map(r=>r[2]));
   res={title:'Shear force V and bending moment M',x:'Distance along beam (m)',y:'V (kN) / M (kN·m)',columns:['x_m','shear_kN','moment_kNm'],rows,series:[{name:'Shear V',j:1},{name:'Bending M',j:2}],metrics:[metric('Left reaction RA',Ra,'kN'),metric('Right reaction RB',Rb,'kN'),metric('Peak sampled positive moment',pmax,'kN·m'),metric('Vertical equilibrium residual',Ra+Rb-x.pk-x.qk*L,'kN')],note:'Simply supported beam; upward reactions and sagging bending positive. Position a auto-clamped within current span. Moment extrema are sampled approximately.'};break;}
  case 'deflection':{
   const EI=x.eg*x.imm*1000;
   const pt=s=>{const xx=Math.min(s,L-s);return x.pk*1000*xx*(3*L*L-4*xx*xx)/(48*EI)*1000};
   const udl=s=>x.qk*1000*s*(L**3-2*L*s*s+s**3)/(24*EI)*1000;
   const rows=arange(0,L,151).map(s=>[s,pt(s),udl(s),pt(s)+udl(s)]);
   res={title:'Downward elastic deflection along simply supported span',x:'Distance along beam (m)',y:'Deflection down (mm)',columns:['position_m','point_load_deflection_mm','udl_deflection_mm','total_deflection_mm'],rows,series:[{name:'Total',j:3},{name:'Midpoint load',j:1},{name:'Uniform load',j:2}],metrics:[metric('Peak deflection',Math.max(...rows.map(r=>r[3])),'mm'),metric('Point-load midspan component',pt(L/2),'mm'),metric('Uniform-load midspan component',udl(L/2),'mm'),metric('Flexural rigidity EI',EI/1e6,'MN·m²')],note:'Simply supported linear-elastic Euler–Bernoulli beam. No shear deformation; no self-weight unless entered as a distributed load.'};break;}
  case 'section':{
   const b=x.bmm,h=x.hmm,f=x.hole,A=b*h*(1-f*f),I=b*h**3*(1-f**4)/12,S=2*I/h,rows=arange(-h/2,h/2,101).map(y=>[y,((Math.abs(y)<f*h/2)?b*(1-f):b),y*y]);
   res={title:'Available material width through section depth',x:'Vertical coordinate y (mm)',y:'Material width (mm)',columns:['y_mm','material_width_mm','y_squared_mm2'],rows,series:[{name:'Solid material width',j:1}],metrics:[metric('Area A',A,'mm²'),metric('Second moment Ix',I/1e6,'×10⁶ mm⁴'),metric('Elastic section modulus Sx',S/1000,'×10³ mm³'),metric('Radius of gyration',Math.sqrt(I/A),'mm')],note:'Rectangular outer section with centered similar rectangular opening. Sides assumed straight; no local buckling or fabrication details.'};break;}
  case 'mohr':{
   const c=(x.sx+x.sy)/2,h=(x.sx-x.sy)/2,R=Math.hypot(h,x.txy),th=x.angle*Math.PI/180,sig=c+h*Math.cos(2*th)+x.txy*Math.sin(2*th),tau=-h*Math.sin(2*th)+x.txy*Math.cos(2*th),thetaP=Math.atan2(2*x.txy,x.sx-x.sy)*90/Math.PI;
   const rows=arange(0,360,181).map(a=>[a,c+R*Math.cos(a*Math.PI/180),R*Math.sin(a*Math.PI/180)]);
   res={title:'Mohr circle (normal stress vs shear stress)',x:'Normal stress (MPa)',y:'Shear stress (MPa)',xy:true,columns:['circle_angle_deg','normal_MPa','shear_MPa'],rows,series:[{name:'Mohr circle',j:2,xj:1}],markers:[{x:sig,y:tau,label:'Rotated state'}],metrics:[metric('Rotated normal stress',sig,'MPa'),metric('Rotated shear stress',tau,'MPa'),metric('Principal stresses σ1 / σ2',`${f(c+R)} / ${f(c-R)}`,'MPa'),metric('Principal angle θp',thetaP,'°')],note:'Plane-stress convention uses physical counter-clockwise plane normal angle θ, and the displayed τ formula follows the stated orientation.'};break;}
  case 'combined':{
   const b=x.bmm,h=x.hmm,I=b*h**3/12,A=b*h,c=x.nk*1000/A,k=x.mkn*1e6/I;
   const rows=arange(-h/2,h/2,101).map(y=>[y,c-k*y,c,k*y]);
   const s1=c-k*h/2,s2=c+k*h/2;
   res={title:'Longitudinal stress across section depth',x:'Vertical coordinate y (mm)',y:'Normal stress (MPa)',columns:['y_mm','combined_stress_MPa','uniform_axial_stress_MPa','bending_component_MPa'],rows,series:[{name:'Combined stress',j:1},{name:'Axial component',j:2},{name:'Bending magnitude/sign',j:3}],metrics:[metric('Upper fiber stress',s1,'MPa'),metric('Lower fiber stress',s2,'MPa'),metric('Maximum absolute stress',Math.max(Math.abs(s1),Math.abs(s2)),'MPa'),metric('Neutral-axis coordinate',k===0?NaN:c/k,'mm')],note:'Homogeneous linear-elastic rectangular section. Signed N represents positive tension; moment sign defines which edge is tensile.'};break;}
  case 'buckling':{
   const b=x.bmm,h=x.hmm,I=b*h**3/12,A=b*h,K=x.kfac,Le=K*L*1000,Pcr=Math.PI**2*E*I/(Le**2)/1000,Py=x.fy*A/1000,ratio=Pcr/Py;
   const rows=arange(0.5,2,121).map(k=>[k,Math.PI**2*E*I/(k*L*1000)**2/1000,Py]);
   res={title:'Ideal Euler load versus effective-length factor',x:'Effective length factor K',y:'Axial force (kN)',columns:['K','euler_critical_load_kN','gross_yield_force_kN'],rows,series:[{name:'Euler Pcr',j:1},{name:'Gross yield reference',j:2}],metrics:[metric('Euler elastic critical load',Pcr,'kN'),metric('Gross axial yield force',Py,'kN'),metric('Ideal elastic-to-yield ratio',ratio,'ratio'),metric('Slenderness K L/r',Le/Math.sqrt(I/A),'ratio')],note:ratio>=1?'Warning: Euler Pcr exceeds gross yield reference; purely elastic buckling model may be inapplicable. This is not code design capacity.':'Ideal elastic Euler model assumes straight, centered column and perfect restraints. Actual allowable load requires code-based imperfection and inelasticity checks.'};break;}
  case 'pressure':{
   const hoop=x.pmpa*x.rmm/x.tmm,long=hoop/2,rr=x.tmm/x.rmm; const rows=arange(0,360,121).map(a=>[a,hoop,long]);
   res={title:'Circumferential and longitudinal membrane stresses',x:'Angular position around cylinder (°)',y:'Membrane stress (MPa)',columns:['angle_deg','hoop_stress_MPa','longitudinal_stress_MPa'],rows,series:[{name:'Hoop stress',j:1},{name:'Longitudinal stress',j:2}],metrics:[metric('Hoop stress',hoop,'MPa'),metric('Longitudinal stress',long,'MPa'),metric('Thickness / radius',rr,'ratio'),metric('Hoop stress / yield',hoop/x.fy,'ratio')],note:rr>0.1?'OUTSIDE TEACHING THIN-WALL RANGE (t/r > 0.10). Results shown only to expose the breakdown of this approximation.':'Approximation for thin, closed-end, smooth cylindrical shell; excludes openings, end restraints, corrosion and pressure-code checks.'};break;}
  case 'gauge':{
   const stress=x.pk*1000/x.amm,eps=stress/E,vb=x.vexc*x.gf*eps/4,rows=arange(0,x.pk,101).map(P=>[P,P*1000/x.amm/E*1e6,x.vexc*x.gf*P*1000/x.amm/E/4*1e6]);
   res={title:'Quarter bridge output versus applied axial load',x:'Applied axial load (kN)',y:'Strain (µε) / Bridge output (µV)',columns:['axial_load_kN','strain_microstrain','quarter_bridge_output_microvolt'],rows,series:[{name:'Strain',j:1},{name:'Bridge output',j:2}],metrics:[metric('Bar normal stress',stress,'MPa'),metric('Axial strain',eps*1e6,'µε'),metric('Bridge output',vb*1e6,'µV'),metric('Bridge signal / 10 µV',vb*1e6/10,'ratio')],note:'First-order quarter-bridge response of ideal longitudinal gauge in elastic bar; temperature compensation and wiring effects ignored.'};break;}
  case 'fatigue':{
   const b=x.bexp,N=1e6*Math.pow(x.sa/x.sref,1/b),rows=arange(3,8,101).map(logN=>[logN,x.sref*Math.pow(Math.pow(10,logN)/1e6,b)]);
   res={title:'Synthetic Basquin S–N curve',x:'log10(cycles)',y:'Stress amplitude (MPa)',columns:['log10_cycles','stress_amplitude_MPa'],rows,series:[{name:'Fitted amplitude',j:1}],metrics:[metric('Predicted cycles (illustrative)',N,'cycles'),metric('log10 predicted cycles',Math.log10(N),'log10 cycles'),metric('Reference stress amplitude',x.sref,'MPa'),metric('Exponent b',b,'dimensionless')],note:'SYNTHETIC demonstration ONLY: outside calibrated stress/life range and without mean stress, scatter or environment corrections. Never use for service life prediction.'};break;}
  case 'beamshear':{
   const A=x.bmm*x.hmm,max=1.5*x.vk*1000/A,rows=arange(-x.hmm/2,x.hmm/2,101).map(y=>[y,max*(1-4*y*y/(x.hmm*x.hmm))]);
   res={title:'Parabolic shear traction through beam height',x:'Vertical coordinate y (mm)',y:'Transverse shear stress (MPa)',columns:['height_coordinate_mm','shear_stress_MPa'],rows,series:[{name:'τ(y)',j:1}],metrics:[metric('Mean V/A shear',x.vk*1000/A,'MPa'),metric('Peak at neutral axis',max,'MPa'),metric('Top/bottom surface shear',0,'MPa'),metric('Total shear resultant',x.vk,'kN')],note:'Rectangular straight prism, classical beam-theory shear distribution away from supports and concentrated load introduction.'};break;}
  }
  return res;
 }
 

  function createEl(tag, attrs, txt) {
    var el = document.createElementNS(svgNS, tag);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    if (txt !== undefined) el.textContent = txt;
    return el;
  }

  var MODELS = [];
  var labKeys = Object.keys(definitions);
  var labUnits = {"axial": 1, "material": 3, "torsion": 4, "beamvm": 5, "deflection": 6, "section": 1, "mohr": 7, "combined": 7, "buckling": 8, "pressure": 9, "gauge": 2, "fatigue": 9, "beamshear": 5};

  labKeys.forEach(function(key, idx) {
    var def = definitions[key];
    var unit = labUnits[key] || 1;
    var controlsHtml = def.keys.map(function(k) {
      var c = controls[k];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="' + key + '_' + k + '">' + c.label + ' <span id="v_' + key + '_' + k + '" style="font-weight:700;color:#d97706;">' + c.val + ' ' + c.unit + '</span></label>' +
             '<input id="' + key + '_' + k + '" data-key="' + k + '" type="range" min="' + c.min + '" max="' + c.max + '" step="' + c.step + '" value="' + c.val + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Lab ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + def.title + '</h3></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<svg class="sim-plot" viewBox="0 0 840 430" style="width:100%;height:auto;background:#091d2f;border-radius:8px;display:block;"></svg>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS.push({
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {
        try {
          var v = {};
          def.keys.forEach(function(k) { v[k] = controls[k].val; });
          var plotSvg = card.querySelector('.sim-plot');
          var metricsEl = card.querySelector('.metrics');
          var noteEl = card.querySelector('.model-note');

          function drawPlotLocal(r) {
            if (!plotSvg) return;
            while (plotSvg.firstChild) plotSvg.removeChild(plotSvg.firstChild);
            var left = 68, right = 770, top = 30, bottom = 355, w = right - left, h = bottom - top;
            var all = [];
            for (var si = 0; si < r.series.length; si++) {
              var s = r.series[si];
              var rows = s.data !== undefined ? s.data : r.rows;
              for (var ri = 0; ri < rows.length; ri++) {
                var row = rows[ri];
                var xx = r.xy ? row[s.xj !== undefined ? s.xj : 1] : row[0];
                var yy = row[s.j];
                if (Number.isFinite(xx) && Number.isFinite(yy)) all.push([xx, yy]);
              }
            }
            for (var mi = 0; mi < (r.markers || []).length; mi++) all.push([r.markers[mi].x, r.markers[mi].y]);
            if (!all.length) return;
            var xmin = Math.min.apply(null, all.map(function(p) { return p[0]; }));
            var xmax = Math.max.apply(null, all.map(function(p) { return p[0]; }));
            var ymin = Math.min.apply(null, all.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, all.map(function(p) { return p[1]; }));
            if (Math.abs(xmax - xmin) < 1e-12) { xmin -= 1; xmax += 1; }
            if (Math.abs(ymax - ymin) < 1e-12) { ymin -= 1; ymax += 1; }
            var px = (xmax - xmin) * 0.04, py = (ymax - ymin) * 0.13;
            xmin -= px; xmax += px; ymin -= py; ymax += py;
            if (r.xy) {
              var xmid = (xmin + xmax) / 2, ymid = (ymin + ymax) / 2;
              var unitsPerPixel = Math.max((xmax - xmin) / w, (ymax - ymin) / h);
              xmin = xmid - unitsPerPixel * w / 2; xmax = xmid + unitsPerPixel * w / 2;
              ymin = ymid - unitsPerPixel * h / 2; ymax = ymid + unitsPerPixel * h / 2;
            }
            var X = function(a) { return left + (a - xmin) / (xmax - xmin || 1) * w; };
            var Y = function(a) { return bottom - (a - ymin) / (ymax - ymin || 1) * h; };

            plotSvg.appendChild(createEl('rect', {x: left, y: top, width: w, height: h, fill: '#091d2f', rx: '6'}));
            for (var gi = 0; gi <= 5; gi++) {
              var gx = left + (right - left) * gi / 5, gy = top + (bottom - top) * gi / 5;
              plotSvg.appendChild(createEl('line', {x1: gx, y1: top, x2: gx, y2: bottom, stroke: '#27465c', 'stroke-width': 1}));
              plotSvg.appendChild(createEl('line', {x1: left, y1: gy, x2: right, y2: gy, stroke: '#27465c', 'stroke-width': 1}));
              plotSvg.appendChild(createEl('text', {x: gx, y: bottom + 21, fill: '#b7cad7', 'font-size': 12, 'text-anchor': 'middle'}, f(xmin + (xmax - xmin) * gi / 5, 2)));
              plotSvg.appendChild(createEl('text', {x: left - 12, y: gy + 4, fill: '#b7cad7', 'font-size': 12, 'text-anchor': 'end'}, f(ymax - (ymax - ymin) * gi / 5, 2)));
            }
            for (var si2 = 0; si2 < r.series.length; si2++) {
              var s2 = r.series[si2];
              var rows2 = s2.data !== undefined ? s2.data : r.rows;
              var pts = rows2.filter(function(row) {
                return Number.isFinite(r.xy ? row[s2.xj !== undefined ? s2.xj : 1] : row[0]) && Number.isFinite(row[s2.j]);
              }).map(function(row) {
                return X(r.xy ? row[s2.xj !== undefined ? s2.xj : 1] : row[0]) + ',' + Y(row[s2.j]);
              }).join(' ');
              if (pts) plotSvg.appendChild(createEl('polyline', {points: pts, fill: 'none', stroke: palette[si2 % palette.length], 'stroke-width': 3, 'stroke-linejoin': 'round', 'stroke-linecap': 'round'}));
            }
            for (var mi2 = 0; mi2 < (r.markers || []).length; mi2++) {
              var m2 = r.markers[mi2];
              plotSvg.appendChild(createEl('circle', {cx: X(m2.x), cy: Y(m2.y), r: 7, fill: '#f97316', stroke: 'white', 'stroke-width': 1.5}));
              plotSvg.appendChild(createEl('text', {x: X(m2.x) + 10, y: Y(m2.y) - 12, fill: '#fed7aa', 'font-size': 14}, m2.label));
            }
            plotSvg.appendChild(createEl('text', {x: 430, y: 408, fill: '#dceaf3', 'font-size': 14, 'text-anchor': 'middle'}, r.x));
            plotSvg.appendChild(createEl('text', {transform: 'translate(16 194) rotate(-90)', fill: '#dceaf3', 'font-size': 14, 'text-anchor': 'middle'}, r.y));
          }

          function updateLab() {
            var inputs = card.querySelectorAll('input[type="range"]');
            inputs.forEach(function(inp) {
              var k = inp.dataset.key;
              v[k] = Number(inp.value);
              var lbl = card.querySelector('#v_' + key + '_' + k);
              if (lbl) lbl.textContent = inp.value + ' ' + controls[k].unit;
            });
            var res = calc(key, v);
            if (metricsEl) {
              metricsEl.innerHTML = res.metrics.map(function(x) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + escapeHTML(x[0]) + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof x[1] === 'string' ? escapeHTML(x[1]) : f(x[1], 3)) + ' ' + escapeHTML(x[2]) + '</output></div>';
              }).join('');
            }
            if (noteEl) noteEl.textContent = 'Model boundary: ' + res.note;
            drawPlotLocal(res);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateLab);
          });
          updateLab();
        } catch (err) {
          console.warn('Strength of Materials sim error in lab ' + key + ':', err);
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
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 9) unitNum = 1;
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
