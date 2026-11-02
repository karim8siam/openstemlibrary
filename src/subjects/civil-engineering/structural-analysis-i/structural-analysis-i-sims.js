/* Structural Analysis I Interactive Simulation Suite */
(function(window) {
  'use strict';

  var f = function(n, k) { k = (k === undefined) ? 3 : k; return Number(n).toLocaleString('en-US', {maximumFractionDigits: k}); };
  var line = function(n, fn) { return Array.from({length: n + 1}, function(_, i) { return {x: i / n, y: fn(i / n)}; }); };
  var arrsum = function(a) { return a.reduce(function(x, y) { return x + y; }, 0); };
  var momentOrd = function(L, c, z) { return z <= c ? z * (L - c) / L : c * (L - z) / L; };

  function runModel(labId, vals) {
    var v = vals, points = [], out = [], equation = '', explain = '', xLabel = 'Position', yLabel = 'Response';
    var add = function(name, unit, value) { out.push({name: name, unit: unit, value: value}); };
    var getBeam = function() {
      var L = v.L || 8, P = v.P !== undefined ? v.P : 28, a = v.a !== undefined ? v.a : 0.45, w = v.w !== undefined ? v.w : 3;
      var loc = a * L;
      var RA = P * (L - loc) / L + w * L / 2, RB = P * loc / L + w * L / 2;
      return {
        L: L, P: P, a: loc, w: w, RA: RA, RB: RB,
        M: function(x) { return RA * x - w * x * x / 2 - P * Math.max(0, x - loc); },
        V: function(x) { return RA - w * x - (x >= loc ? P : 0); }
      };
    };

    switch(labId){
case'beam-reactions':{let b=getBeam();points=line(160,t=>b.RA-b.w*t*b.L-(t*b.L>=b.a?b.P:0));
points=line(160,t=>b.P*(1-t)+b.w*b.L/2); xLabel='Moving point location a / L';yLabel='Left reaction (kN)';add('Left reaction','kN',b.RA);add('Right reaction','kN',b.RB);add('Vertical residual','kN',b.RA+b.RB-b.P-b.w*b.L);equation='RA=P(L-a)/L + wL/2; RB=Pa/L + wL/2';explain='A pin and roller are assumed. A moving point force shifts reaction to the nearer support; stiffness does not enter these determinate reactions.';break}
case'shear-moment':{let b=getBeam();points=line(160,t=>v.mode===0?b.V(t*b.L):b.M(t*b.L));add('Left reaction','kN',b.RA);add('Peak sagging moment','kN·m',Math.max(...points.map(p=>p.y)));add('Right-end moment residual','kN·m',b.M(b.L));equation='V(x)=RA-wx-P·H(x-a), M(x)=RAx-wx²/2-P·max(0,x-a)';explain='Plot shows bending moment. A point-force jump in shear produces a corner in M. Look for V=0 when finding maximum moment.';yLabel=v.mode===0?'Shear force (kN)':'Bending moment (kN·m)';break}
case'beam-deflection':{let {L,P,w,E,I}=v;const EI=E*1e9*I*1e-4,W=w*1e3,Q=P*1e3;
let df=x=>{let q=Math.min(x,L-x);return 1000*(W*x*(L*L*L-2*L*x*x+x*x*x)/(24*EI)+Q*q*(3*L*L-4*q*q)/(48*EI))};points=line(160,t=>df(t*L));add('Midspan downward deflection','mm',df(L/2));add('Span / deflection','—',L*1000/Math.max(1e-12,df(L/2)));add('Flexural rigidity EI','MN·m²',EI/1e6);yLabel='Downward deflection (mm)';xLabel='x / L';equation='δmid=5wL⁴/(384EI)+PL³/(48EI)';explain='Linear superposition for a simple beam with full-span w and center-applied P. The plot ignores shear deformation and second-order effects.';break}
case'triangle-truss':{let {L,h,P}=v;let sin=h/Math.hypot(L/2,h),tan=2*h/L;let comp=P/(2*sin),tie=P/(2*tan);points=Array.from({length:161},(_,i)=>{let height=.75+i/160*7;return {x:height,y:P/(2*(height/Math.hypot(L/2,height)))}});add('Each diagonal compression','kN',comp);add('Bottom tie tension','kN',tie);add('Apex vertical residual','kN',2*comp*sin-P);xLabel='Apex rise (m)';yLabel='Diagonal compression (kN)';equation='|Ndiagonal|=P/(2sinθ); Ntie=P/(2tanθ), θ=atan(2h/L)';explain='Symmetric 3-bar truss under apex load only. Curve shows the diagonal compression as the rise varies at the same span and load.';break}
case'truss-displacement':{let {L,h,P,E,A}=v; let sl=Math.hypot(L/2,h),sin=h/sl,tan=2*h/L,ea=E*1e9*A*1e-4;let compliance=sl/(2*ea*sin*sin)+L/(4*ea*tan*tan);let d=P*1e3*compliance*1000;
points=Array.from({length:161},(_,i)=>{let H=.75+i/160*7,ls=Math.hypot(L/2,H),si=H/ls,ta=2*H/L;return {x:H,y:P*1e6*(ls/(2*ea*si*si)+L/(4*ea*ta*ta))}});add('Apex downward displacement','mm',d);add('Bar EA','MN',ea/1e6);add('Displacement per force','mm/kN',d/Math.max(P,1e-6));yLabel='Apex displacement (mm)';xLabel='Apex rise (m)';equation='δ=PΣ[(Ni/P)² Li/(EiAi)] for 3-bar symmetric truss';explain='Axial-only virtual-work model. Bottom tie contribution is included; no joint slip, bending, or column buckling.';break}
case'three-hinged-arch':{let {L,f,P,a}=v;let la=a*L,RA=P*(L-la)/L,mc=RA*L/2-P*Math.max(0,L/2-la),H=mc/f;
points=line(160,t=>{let x=t*L,y=4*f*x*(L-x)/(L*L);return RA*x-P*Math.max(0,x-la)-H*y});add('Horizontal thrust','kN',H);add('Left vertical reaction','kN',RA);add('Crown moment','kN·m',RA*L/2-P*Math.max(0,L/2-la)-H*f);xLabel='x / L';yLabel='Arch bending (kN·m)';equation='H=Mbeam(L/2)/f; March(x)=Mbeam(x)-H·y(x)';explain='Parabolic 3-hinged arch with pinned crown at midspan. The crown moment is constrained to zero, regardless of off-center point-load position.';break}
case'cable-sag':{let {L,f,w}=v;let H=w*L*L/(8*f),V=w*L/2,T=Math.hypot(H,V),len=0;const n=1000,dx=L/n;for(let i=0;i<n;i++){let xx=(i+.5)*dx,dy=4*f*(L-2*xx)/(L*L);len+=Math.hypot(1,dy)*dx}
points=line(160,t=>4*f*t*(1-t));add('Horizontal cable force','kN',H);add('End tension','kN',T);add('Cable arc length','m',len);xLabel='x / L';yLabel='Sag ordinate (m)';equation='H=wL²/(8f); T_end=sqrt(H²+(wL/2)²)';explain='Uniform loading is per horizontal projected meter, NOT per cable arc length. The cable is treated as a perfectly flexible parabolic line.';break}
case'cantilever-virtual':{let {L,P,w,E,I}=v;let EI=E*1e9*I*1e-4,an=1000*(P*1e3*L**3/(3*EI)+w*1e3*L**4/(8*EI));points=line(160,t=>{let x=t*L;return (P*1e3*(L-x)+w*1e3*(L-x)**2/2)*(L-x)/EI});let integral=0,n=1000;for(let i=0;i<n;i++){let x=(i+.5)*L/n;integral+=(P*1e3*(L-x)+w*1e3*(L-x)**2/2)*(L-x)/EI*L/n}add('Analytic tip deflection','mm',an);add('Numerical unit-load result','mm',integral*1000);add('Relative integration error','%',100*(integral*1000-an)/Math.max(an,1e-10));xLabel='x / L';yLabel='M·m/EI (dimensionless)';equation='δ=∫M(x)m(x)/(EI)dx = PL³/(3EI)+wL⁴/(8EI)';explain='Plot is the virtual-work integrand, not the beam deflected shape. Numerical midpoint integration checks the analytical formula.';break}
case'moment-influence':{let {L,c,P,z}=v,section=c*L,x=z*L;points=line(160,t=>momentOrd(L,section,t*L));add('Moment influence ordinate','m',momentOrd(L,section,x));add('Moment from chosen load','kN·m',P*momentOrd(L,section,x));add('Peak ordinate at section','m',section*(L-section)/L);xLabel='Moving load position z / L';yLabel='Moment influence (m)';equation='ILM(z)=z(L-c)/L for z≤c; c(L-z)/L for z≥c';explain='The same fixed section is observed while a unit downward load moves over the span. Section moment is force times influence ordinate.';break}
case'axle-train':{let {L,c,P1,P2,d}=v,sec=L*c;const response=x=> {let z1=x,z2=x-d;return (z1>=0&&z1<=L?P1*momentOrd(L,sec,z1):0)+(z2>=0&&z2<=L?P2*momentOrd(L,sec,z2):0)};
points=Array.from({length:251},(_,i)=>{let x=-d+(L+2*d)*i/250;return {x,y:response(x)}});let mx=Math.max(...points.map(p=>p.y)),arg=points.findIndex(p=>p.y==mx),x=-d+(L+2*d)*arg/250;add('Scan peak section moment','kN·m',mx);add('Front axle at scan peak','m',x);add('Scan positional step','m',(L+2*d)/250);xLabel='Front axle position (m)';yLabel='Section moment (kN·m)';equation='M(c)=Σ Pi·ILM(c,zi) for 0≤zi≤L';explain='This scan locates an approximate peak for a two-axle quasistatic vehicle. Loads outside the bridge contribute zero. Refine around candidates for an exact critical location.';break}
case'propped-cantilever':{let {L,w,P,s,E,I}=v,EI=E*1e9*I*1e-4;let r0=P+3*w*L/8,rb=r0-3*EI*(s/1000)/(L**3)/1e3;points=line(160,t=>r0-3*EI*(30*t/1000)/(L**3)/1e3);add('Computed prop reaction','kN upward',rb);add('Fixed-end vertical reaction','kN upward',w*L+P-rb);add('Predicted contact status','',rb>=0?'compression':'uplift / model invalid');xLabel='Settlement swept 0–30 mm';yLabel='Prop reaction (kN)';equation='RB=P+3wL/8−3EI·s/L³';explain='The formula imposes a bilateral vertical restraint. When RB<0 a compression-only prop cannot enforce compatibility; contact must be remodeled.';break}
case'moving-envelope':{let {L,P1,P2,d}=v;const m=(c,z)=> (z>=0&&z<=L?momentOrd(L,c,z):0);let span=150,scan=220;points=line(span,t=>{let c=t*L,best=0;for(let i=0;i<=scan;i++){let x=-d+(L+2*d)*i/scan;best=Math.max(best,P1*m(c,x)+P2*m(c,x-d))}return best});let vMax=Math.max(...points.map(p=>p.y)),at=points.find(p=>p.y===vMax)?.x*L;add('Peak envelope moment','kN·m',vMax);add('Peak approximate section','m',at);add('Vehicle scan step','m',(L+2*d)/scan);xLabel='Structural section c / L';yLabel='Envelope max M (kN·m)';equation='Envelope(c)=maxvehicle positions Σ Pi·ILM(c,zi)';explain='Each x-coordinate is the maximum over many two-axle vehicle positions; the envelope is not a single instantaneous bending diagram.';break}
case'verification-convergence':{let {L,P,w,E,I,n}=v,EI=E*1e9*I*1e-4;const integrand=x=>(P*1e3*(L-x)+w*1e3*(L-x)**2/2)*(L-x)/EI;const appr=N=>{let dx=L/N,s=0;for(let i=0;i<N;i++)s+=integrand((i+.5)*dx)*dx;return s*1000};let exact=1000*(P*1e3*L**3/(3*EI)+w*1e3*L**4/(8*EI));points=Array.from({length:40},(_,i)=>({x:2+i*2,y:Math.abs(appr(2+(i*2))-exact)}));add('Exact displacement','mm',exact);add('Numerical displacement','mm',appr(n));add('Relative error','%',100*Math.abs(appr(n)-exact)/Math.max(exact,1e-9));xLabel='Integration panels (count)';yLabel='Abs error (mm)';equation='Compare midpoint Σ M(xi)m(xi)Δx/EI with analytic δtip';explain='Refining integration panels reduces quadrature error but does not validate the physical model or linear elastic assumptions.';break}
}


    return {points: points, out: out, equation: equation, explain: explain, xLabel: xLabel, yLabel: yLabel};
  }

  var MODELS = [];
  var labsConfig = [{"id": "beam-reactions", "title": "Beam reactions and load balance", "desc": "Compare reaction shifts for a point load and an equivalent distributed load. Verify vertical force and moment balance for several load locations. The plotted bending field is a secondary view of this same determinate system.", "config": {"name": "Beam reactions and load balance", "controls": [{"id": "L", "name": "Span", "unit": "m", "initial": 8, "min": 3, "max": 18, "step": 0.5}, {"id": "P", "name": "Point force", "unit": "kN", "initial": 28, "min": 0, "max": 120, "step": 1}, {"id": "a", "name": "Point location", "unit": "fraction", "initial": 0.45, "min": 0.1, "max": 0.9, "step": 0.01}, {"id": "w", "name": "Uniform load", "unit": "kN/m", "initial": 3, "min": 0, "max": 15, "step": 0.2}]}, "unit": 1}, {"id": "shear-moment", "title": "Shear and bending-moment fields", "desc": "Move a point load across a simple beam and observe the section moment diagram. Differentiate the moment function away from the point force to understand the shear field.", "config": {"name": "Shear and bending-moment fields", "controls": [{"id": "L", "name": "Span", "unit": "m", "initial": 10, "min": 3, "max": 20, "step": 0.5}, {"id": "P", "name": "Point force", "unit": "kN", "initial": 25, "min": 0, "max": 100, "step": 1}, {"id": "a", "name": "Point location", "unit": "fraction", "initial": 0.35, "min": 0.1, "max": 0.9, "step": 0.01}, {"id": "w", "name": "Uniform load", "unit": "kN/m", "initial": 4, "min": 0, "max": 15, "step": 0.2}, {"id": "mode", "name": "Diagram: 0 shear / 1 moment", "unit": "choice", "initial": 1, "min": 0, "max": 1, "step": 1}]}, "unit": 1}, {"id": "beam-deflection", "title": "Elastic beam deflection laboratory", "desc": "Explore deflection from a center point load and full-span uniform action. Change span and stiffness to quantify the fourth-power sensitivity and test small-deflection applicability.", "config": {"name": "Elastic beam deflection laboratory", "controls": [{"id": "L", "name": "Span", "unit": "m", "initial": 8, "min": 3, "max": 15, "step": 0.5}, {"id": "P", "name": "Central point force", "unit": "kN", "initial": 20, "min": 0, "max": 80, "step": 1}, {"id": "w", "name": "Uniform load", "unit": "kN/m", "initial": 3, "min": 0, "max": 10, "step": 0.1}, {"id": "E", "name": "Elastic modulus", "unit": "GPa", "initial": 200, "min": 50, "max": 240, "step": 5}, {"id": "I", "name": "Second moment", "unit": "10\u207b\u2074 m\u2074", "initial": 4, "min": 0.5, "max": 15, "step": 0.5}]}, "unit": 2}, {"id": "triangle-truss", "title": "Triangular truss forces", "desc": "Vary the height of a symmetric pin-jointed triangle. The diagnostic curve traces the required diagonal compression for a range of rises, revealing why shallow trusses can demand larger member forces.", "config": {"name": "Triangular truss forces", "controls": [{"id": "L", "name": "Bottom span", "unit": "m", "initial": 8, "min": 4, "max": 20, "step": 0.5}, {"id": "h", "name": "Apex rise", "unit": "m", "initial": 3, "min": 1, "max": 8, "step": 0.25}, {"id": "P", "name": "Apex downward force", "unit": "kN", "initial": 45, "min": 0, "max": 120, "step": 1}]}, "unit": 3}, {"id": "truss-displacement", "title": "Truss virtual-work displacement", "desc": "Explore the axial-only apex displacement of a three-bar triangular truss. Change member area, modulus and rise; compare the relative contribution of diagonal compression and tie tension.", "config": {"name": "Truss virtual-work displacement", "controls": [{"id": "L", "name": "Bottom span", "unit": "m", "initial": 8, "min": 4, "max": 16, "step": 0.5}, {"id": "h", "name": "Apex height", "unit": "m", "initial": 3, "min": 1, "max": 8, "step": 0.25}, {"id": "P", "name": "Apex force", "unit": "kN", "initial": 30, "min": 0, "max": 100, "step": 1}, {"id": "E", "name": "Young modulus", "unit": "GPa", "initial": 200, "min": 50, "max": 240, "step": 10}, {"id": "A", "name": "Member area", "unit": "cm\u00b2", "initial": 12, "min": 2, "max": 50, "step": 1}]}, "unit": 3}, {"id": "three-hinged-arch", "title": "Three-hinged arch bending", "desc": "Move a single load along a three-hinged parabolic arch. Check that the crown bending moment remains zero and inspect changes in horizontal thrust and bending along the curved centerline.", "config": {"name": "Three-hinged arch bending", "controls": [{"id": "L", "name": "Span", "unit": "m", "initial": 18, "min": 8, "max": 40, "step": 1}, {"id": "f", "name": "Rise", "unit": "m", "initial": 4, "min": 1, "max": 10, "step": 0.25}, {"id": "P", "name": "Point force", "unit": "kN", "initial": 90, "min": 0, "max": 250, "step": 5}, {"id": "a", "name": "Force position", "unit": "fraction", "initial": 0.36, "min": 0.1, "max": 0.9, "step": 0.01}]}, "unit": 4}, {"id": "cable-sag", "title": "Parabolic cable sag and thrust", "desc": "For a cable loaded uniformly per horizontal meter, vary sag and span. Observe the inverse relation between sag and horizontal tension. This is a parabolic-cable idealization, not a catenary under self-weight.", "config": {"name": "Parabolic cable sag and thrust", "controls": [{"id": "L", "name": "Horizontal span", "unit": "m", "initial": 40, "min": 10, "max": 120, "step": 2}, {"id": "f", "name": "Sag", "unit": "m", "initial": 5, "min": 1, "max": 18, "step": 0.25}, {"id": "w", "name": "Vertical load per horizontal m", "unit": "kN/m", "initial": 2, "min": 0.2, "max": 8, "step": 0.1}]}, "unit": 4}, {"id": "cantilever-virtual", "title": "Cantilever unit-load integration", "desc": "The graph plots the virtual-work integrand over the cantilever, allowing the analytical tip displacement to be checked by numerical quadrature. Vary load distribution and compare contributions.", "config": {"name": "Cantilever unit-load integration", "controls": [{"id": "L", "name": "Length", "unit": "m", "initial": 5, "min": 2, "max": 10, "step": 0.25}, {"id": "P", "name": "Tip force", "unit": "kN", "initial": 16, "min": 0, "max": 60, "step": 1}, {"id": "w", "name": "Distributed load", "unit": "kN/m", "initial": 2, "min": 0, "max": 9, "step": 0.1}, {"id": "E", "name": "Elastic modulus", "unit": "GPa", "initial": 200, "min": 50, "max": 240, "step": 10}, {"id": "I", "name": "Second moment", "unit": "10\u207b\u2074 m\u2074", "initial": 3, "min": 0.5, "max": 12, "step": 0.5}]}, "unit": 5}, {"id": "moment-influence", "title": "Moment influence-line explorer", "desc": "Keep the beam section fixed and slide the moving force. The plotted curve is a response influence line, not a spatial moment diagram. Multiply its ordinate by a wheel force to obtain the section moment.", "config": {"name": "Moment influence-line explorer", "controls": [{"id": "L", "name": "Span", "unit": "m", "initial": 16, "min": 6, "max": 36, "step": 1}, {"id": "c", "name": "Section position", "unit": "fraction", "initial": 0.4, "min": 0.15, "max": 0.85, "step": 0.01}, {"id": "P", "name": "Moving unit-scaled force", "unit": "kN", "initial": 40, "min": 1, "max": 120, "step": 1}, {"id": "z", "name": "Force location", "unit": "fraction", "initial": 0.65, "min": 0, "max": 1, "step": 0.01}]}, "unit": 6}, {"id": "axle-train", "title": "Two-axle moving-load optimization", "desc": "Two axles move together across a simply supported bridge. Follow moment at a fixed section and identify a numerical critical location; a finer grid can refine the reported maximum.", "config": {"name": "Two-axle moving-load optimization", "controls": [{"id": "L", "name": "Bridge span", "unit": "m", "initial": 20, "min": 8, "max": 48, "step": 1}, {"id": "c", "name": "Response section", "unit": "fraction", "initial": 0.5, "min": 0.15, "max": 0.85, "step": 0.01}, {"id": "P1", "name": "Front axle", "unit": "kN", "initial": 65, "min": 10, "max": 180, "step": 5}, {"id": "P2", "name": "Rear axle", "unit": "kN", "initial": 90, "min": 10, "max": 180, "step": 5}, {"id": "d", "name": "Axle spacing", "unit": "m", "initial": 4, "min": 1, "max": 12, "step": 0.5}]}, "unit": 6}, {"id": "propped-cantilever", "title": "Compatibility and support settlement", "desc": "A redundant right-end prop restrains a loaded cantilever. Evaluate reaction as the prop settles and observe where a negative force means the compression-only contact assumption has failed.", "config": {"name": "Compatibility and support settlement", "controls": [{"id": "L", "name": "Cantilever length", "unit": "m", "initial": 7, "min": 3, "max": 12, "step": 0.5}, {"id": "w", "name": "Uniform load", "unit": "kN/m", "initial": 5, "min": 0, "max": 12, "step": 0.25}, {"id": "P", "name": "Point load at prop", "unit": "kN", "initial": 12, "min": 0, "max": 60, "step": 1}, {"id": "s", "name": "Settlement downward", "unit": "mm", "initial": 4, "min": 0, "max": 30, "step": 0.5}, {"id": "E", "name": "Elastic modulus", "unit": "GPa", "initial": 200, "min": 50, "max": 240, "step": 5}, {"id": "I", "name": "Second moment", "unit": "10\u207b\u2074 m\u2074", "initial": 5, "min": 0.5, "max": 20, "step": 0.5}]}, "unit": 7}, {"id": "moving-envelope", "title": "Moment envelope along a bridge", "desc": "Build the maximum positive bending moment envelope over all possible vehicle positions at every beam section. This differs from the diagram at any one instant.", "config": {"name": "Moment envelope along a bridge", "controls": [{"id": "L", "name": "Bridge span", "unit": "m", "initial": 24, "min": 10, "max": 48, "step": 1}, {"id": "P1", "name": "Axle one", "unit": "kN", "initial": 70, "min": 15, "max": 180, "step": 5}, {"id": "P2", "name": "Axle two", "unit": "kN", "initial": 85, "min": 15, "max": 180, "step": 5}, {"id": "d", "name": "Axle distance", "unit": "m", "initial": 5, "min": 1, "max": 12, "step": 0.5}]}, "unit": 8}, {"id": "verification-convergence", "title": "Quadrature accuracy and equilibrium", "desc": "Compare numerical midpoint integration of beam virtual work with its closed-form answer. Adjust panel number to observe convergence and distinguish computation error from modeling error.", "config": {"name": "Quadrature accuracy and equilibrium", "controls": [{"id": "L", "name": "Cantilever length", "unit": "m", "initial": 6, "min": 2, "max": 14, "step": 0.5}, {"id": "P", "name": "End force", "unit": "kN", "initial": 18, "min": 0, "max": 80, "step": 1}, {"id": "w", "name": "Uniform load", "unit": "kN/m", "initial": 3, "min": 0, "max": 10, "step": 0.25}, {"id": "E", "name": "Elastic modulus", "unit": "GPa", "initial": 200, "min": 50, "max": 240, "step": 10}, {"id": "I", "name": "Second moment", "unit": "10\u207b\u2074 m\u2074", "initial": 5, "min": 0.5, "max": 20, "step": 0.5}, {"id": "n", "name": "Integration panels", "unit": "count", "initial": 12, "min": 2, "max": 60, "step": 2}]}, "unit": 8}];

  labsConfig.forEach(function(labItem, idx) {
    var labId = labItem.id;
    var unit = labItem.unit;
    var cfg = labItem.config;

    var controlsHtml = cfg.controls.map(function(c) {
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="' + labId + '_' + c.id + '">' + c.name + ' <span id="v_' + labId + '_' + c.id + '" style="font-weight:700;color:#d97706;">' + c.initial + ' ' + c.unit + '</span></label>' +
             '<input id="' + labId + '_' + c.id + '" data-cid="' + c.id + '" type="range" min="' + c.min + '" max="' + c.max + '" step="' + c.step + '" value="' + c.initial + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + labItem.title + '</h3><p>' + labItem.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<svg class="canvas" viewBox="0 0 760 380" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg>' +
               '<div class="equation" style="font-family:monospace;font-size:0.875rem;background:#f1f5f9;padding:0.75rem;border-radius:6px;margin-top:0.75rem;color:#0f172a;"></div>' +
               '<p class="explain" style="font-size:0.8125rem;color:#475569;margin-top:0.5rem;"></p>';

    MODELS.push({
      idx: idx + 1,
      unit: unit,
      id: labId,
      html: html,
      init: function(card) {
        try {
          var vals = {};
          cfg.controls.forEach(function(c) { vals[c.id] = c.initial; });

          var svgEl = card.querySelector('.canvas');
          var metricsEl = card.querySelector('.metrics');
          var eqEl = card.querySelector('.equation');
          var expEl = card.querySelector('.explain');

          function renderChart(points, xLabel, yLabel) {
            if (!svgEl) return;
            var W = 760, H = 380, margin = {top: 24, right: 30, bottom: 50, left: 60};
            var xs = points.map(function(p) { return p.x; }), ys = points.map(function(p) { return p.y; });
            var xMin = Math.min.apply(null, xs), xMax = Math.max.apply(null, xs);
            var yMin = Math.min.apply(null, ys), yMax = Math.max.apply(null, ys);
            if (xMin === xMax) { xMin -= 1; xMax += 1; }
            if (yMin === yMax) { yMin -= 1; yMax += 1; }
            var yPad = (yMax - yMin) * 0.1 || 1; yMin -= yPad; yMax += yPad;
            var tx = function(x) { return margin.left + (x - xMin) / (xMax - xMin) * (W - margin.left - margin.right); };
            var ty = function(y) { return H - margin.bottom - (y - yMin) / (yMax - yMin) * (H - margin.top - margin.bottom); };
            var path = points.map(function(p, i) { return (i ? 'L' : 'M') + tx(p.x).toFixed(2) + ',' + ty(p.y).toFixed(2); }).join(' ');

            var s = '<rect width="' + W + '" height="' + H + '" fill="#ffffff" rx="6"/>';
            for (var i = 0; i <= 4; i++) {
              var y = yMin + (yMax - yMin) * i / 4, yy = ty(y);
              s += '<line x1="' + margin.left + '" x2="' + (W - margin.right) + '" y1="' + yy + '" y2="' + yy + '" stroke="#e2e8f0"/>' +
                   '<text x="' + (margin.left - 8) + '" y="' + (yy + 4) + '" font-size="11" fill="#64748b" text-anchor="end">' + f(y, 2) + '</text>';
            }
            for (var j = 0; j <= 5; j++) {
              var x = xMin + (xMax - xMin) * j / 5, xx = tx(x);
              s += '<line x1="' + xx + '" x2="' + xx + '" y1="' + margin.top + '" y2="' + (H - margin.bottom) + '" stroke="#e2e8f0"/>' +
                   '<text x="' + xx + '" y="' + (H - margin.bottom + 20) + '" text-anchor="middle" fill="#64748b" font-size="11">' + f(x, 2) + '</text>';
            }
            s += '<path d="' + path + '" stroke="#d97706" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" fill="none"/>' +
                 '<text x="' + (W / 2) + '" y="' + (H - 10) + '" font-size="13" fill="#1e293b" text-anchor="middle">' + xLabel + '</text>' +
                 '<text x="18" y="' + (H / 2) + '" transform="rotate(-90 18 ' + (H / 2) + ')" fill="#1e293b" font-size="13" text-anchor="middle">' + yLabel + '</text>';
            svgEl.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
            svgEl.innerHTML = s;
          }

          function update() {
            cfg.controls.forEach(function(c) {
              var inp = card.querySelector('#' + labId + '_' + c.id);
              if (inp) vals[c.id] = Number(inp.value);
              var lbl = card.querySelector('#v_' + labId + '_' + c.id);
              if (lbl) lbl.textContent = f(vals[c.id]) + ' ' + c.unit;
            });
            var cur = runModel(labId, vals);
            renderChart(cur.points, cur.xLabel, cur.yLabel);
            if (eqEl) eqEl.textContent = cur.equation;
            if (expEl) expEl.textContent = cur.explain;
            if (metricsEl) {
              metricsEl.innerHTML = cur.out.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m.name + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m.value === 'number' ? f(m.value, 4) : m.value) + ' ' + m.unit + '</output></div>';
              }).join('');
            }
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', update);
          });
          update();
        } catch (err) {
          console.warn('Structural Analysis I sim error in lab ' + labId + ':', err);
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
