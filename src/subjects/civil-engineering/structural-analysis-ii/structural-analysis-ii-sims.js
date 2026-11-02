/* Structural Analysis II Interactive Simulation Suite */
(function(window) {
  'use strict';

  const LABS = [
 {id:'01',name:'Indeterminate axial load sharing',u:1,desc:'Two elastic members restrain the same loaded node. Compatibility gives equal displacement; stiffness determines the force split.', inputs:[['P','Load, kN',100,10,400,10],['k1','Member 1 stiffness, kN/mm',15,1,100,1],['k2','Member 2 stiffness, kN/mm',25,1,100,1]]},
 {id:'02',name:'Propped cantilever compatibility',u:1,desc:'Remove the prop and impose zero end deflection to recover the redundant vertical reaction under a uniform load.',inputs:[['w','Downward load, kN/m',12,1,50,1],['L','Span, m',6,2,15,.5],['EI','Flexural rigidity, MN·m²',30,5,200,5]]},
 {id:'03',name:'Two-span continuous beam FEM',u:2,desc:'Euler–Bernoulli beam stiffness assembly with three simple vertical supports and free nodal rotations. Observe deformation and middle-support moment.',inputs:[['L1','Left span, m',5,2,10,.5],['L2','Right span, m',7,2,10,.5],['w1','Left UDL, kN/m',10,0,40,1],['w2','Right UDL, kN/m',8,0,40,1],['EI','EI, MN·m²',28,5,200,1]]},
 {id:'04',name:'Moment distribution and joint rotation',u:2,desc:'Two spans with fixed outer end rotations and a free interior joint. The joint equilibrium is identical to the one-DOF direct stiffness solution.',inputs:[['L1','Left span, m',5,2,12,.5],['L2','Right span, m',5,2,12,.5],['w1','Left UDL, kN/m',12,0,40,1],['w2','Right UDL, kN/m',8,0,40,1],['EI','EI, MN·m²',25,5,200,5]]},
 {id:'05',name:'Planar three-bar truss matrix',u:3,desc:'Assemble the 2×2 top-joint stiffness from directional bar contributions. All lower joints are fixed; show force redistribution and top displacement.',inputs:[['P','Vertical load, kN',120,10,400,10],['a','Half-width, m',3,1,6,.5],['h','Height, m',4,1,8,.5],['E','Young modulus, GPa',200,70,220,10],['A','Bar area, cm²',10,2,30,1]]},
 {id:'06',name:'Planar rigid portal-frame stiffness',u:3,desc:'Use a 2D frame with axial and bending DOFs, rigid roof joints, and both column bases fixed. Lateral load produces sway and end moments.',inputs:[['H','Frame height, m',5,3,9,.5],['L','Bay width, m',6,3,12,.5],['F','Horizontal load, kN',80,10,250,10],['EI','EI members, MN·m²',35,5,150,5],['EA','EA members, MN',900,200,2500,100]]},
 {id:'07',name:'Continuous-beam support settlement',u:4,desc:'A prescribed downward settlement creates redundant reactions even without external load. Supports A and C stay vertically fixed; B settles.',inputs:[['L1','Left span, m',5,2,9,.5],['L2','Right span, m',6,2,9,.5],['d','Middle settlement, mm',10,0,35,1],['EI','EI, MN·m²',28,5,100,5]]},
 {id:'08',name:'Restrained thermal elongation',u:4,desc:'Two axial segments in series connect immovable ends. Free expansion is opposed by one uniform compressive force when mean heating is positive.',inputs:[['T1','Segment 1 temperature rise, °C',45,-40,120,5],['T2','Segment 2 temperature rise, °C',25,-40,120,5],['L1','Segment 1 length, m',3,1,8,.5],['L2','Segment 2 length, m',4,1,8,.5],['A1','Area 1, cm²',15,5,40,1],['A2','Area 2, cm²',12,5,40,1]]},
 {id:'09',name:'Euler buckling and moment amplification',u:5,desc:'Compare ideal Euler critical load for four boundary conditions. A first-order moment-amplifier is illustrative only, not a nonlinear design solution.',inputs:[['L','Member length, m',5,2,12,.5],['EI','Flexural rigidity, MN·m²',5,1,30,1],['K','Effective length factor',1,.5,2,.1],['ratio','P/Pcr',.45,.05,.9,.05]]},
 {id:'10',name:'Moving two-axle load and moment influence',u:6,desc:'Move a two-axle vehicle across a simply supported bridge. Only axles on the span contribute; calculate reactions and section bending moments.',inputs:[['L','Bridge span, m',20,10,40,2],['P1','Front axle, kN',80,10,200,10],['P2','Rear axle, kN',110,10,250,10],['space','Axle spacing, m',4,1,9,.5],['front','Front axle position, m',9,0,40,.5],['section','Section x/L',.5,.1,.9,.05]]},
 {id:'11',name:'Two-floor shear-building modes',u:7,desc:'Solve det(K−ω²M)=0 for the two natural frequencies of a shear building and display normalized modal vectors.',inputs:[['m1','Floor 1 mass, tonnes',50,10,140,5],['m2','Floor 2 mass, tonnes',35,10,140,5],['k1','Story 1 stiffness, MN/m',18,3,50,1],['k2','Story 2 stiffness, MN/m',12,3,50,1]]},
 {id:'12',name:'Damped SDOF harmonic response',u:7,desc:'Numerically integrate m ü + c u̇ + k u = F sin(ωt) using Newmark average acceleration. The response develops from zero initial conditions.',inputs:[['m','Mass, tonnes',4,1,15,.5],['k','Stiffness, MN/m',2,.3,10,.1],['z','Damping ratio',.05,0,.3,.01],['ratio','Forcing frequency / ωn',.9,.2,2.0,.05],['F','Force amplitude, kN',20,5,100,5]]},
 {id:'13',name:'Plastic collapse mechanism',u:8,desc:'Idealized fixed-ended beam under a central point load. For three ideal plastic hinges (both ends and midspan), virtual work gives Pcollapse=8Mp/L.',inputs:[['Mp','Plastic moment capacity, kN·m',220,50,600,10],['L','Span, m',8,3,15,.5],['P','Applied center load, kN',130,10,650,10]]},
 {id:'14',name:'Load and stiffness uncertainty',u:8,desc:'Repeat an elastic central-point deflection calculation with reproducible pseudo-random variations; show quantiles, not structural reliability certification.',inputs:[['P','Mean load, kN',100,20,250,10],['E','Mean E, GPa',200,70,220,10],['I','I, ×10⁻⁴ m⁴',4,1,15,.5],['L','Span, m',7,3,12,.5],['covP','Load CV, %',12,0,35,1],['covE','Modulus CV, %',6,0,20,1]]},
 {id:'15',name:'Beam mesh convergence at x=0.37L',u:8,desc:'Compare a Hermite interpolation inside the finite element with the closed-form Euler–Bernoulli deflection under UDL. Beam FEM nodal accuracy can hide interpolation errors.',inputs:[['L','Span, m',8,4,14,.5],['w','Downward UDL, kN/m',15,3,40,1],['EI','EI, MN·m²',18,4,100,1]]}
];

  function gaussian(a,b){const n=b.length,A=a.map((row,i)=>[...row,b[i]]);for(let j=0;j<n;j++){let k=j;for(let i=j+1;i<n;i++)if(Math.abs(A[i][j])>Math.abs(A[k][j]))k=i;if(Math.abs(A[k][j])<1e-11)throw Error('Singular stiffness matrix: check supports and material stiffness');[A[j],A[k]]=[A[k],A[j]];let p=A[j][j];for(let c=j;c<=n;c++)A[j][c]/=p;for(let i=0;i<n;i++)if(i!==j){let s=A[i][j];for(let c=j;c<=n;c++)A[i][c]-=s*A[j][c];}}return A.map(r=>r[n]);}
function zeros(n,m){return Array.from({length:n},()=>Array(m).fill(0));}
function beamK(EI,L){let c=EI/L**3;return [[12,6*L,-12,6*L],[6*L,4*L*L,-6*L,2*L*L],[-12,-6*L,12,-6*L],[6*L,2*L*L,-6*L,4*L*L]].map(r=>r.map(v=>c*v));}
function beamSolver(Ls,ws,EI,vknown,thetaKnown={}){const n=Ls.length+1,N=2*n,K=zeros(N,N),f=Array(N).fill(0),els=[];for(let e=0;e<Ls.length;e++){let L=Ls[e],k=beamK(EI,L),ids=[2*e,2*e+1,2*e+2,2*e+3],fl=[-ws[e]*L/2,-ws[e]*L*L/12,-ws[e]*L/2,ws[e]*L*L/12];els.push({L,k,ids,fl,w:ws[e]});for(let i=0;i<4;i++){f[ids[i]]+=fl[i];for(let j=0;j<4;j++)K[ids[i]][ids[j]]+=k[i][j];}}let known={};for(let [id,v] of Object.entries(vknown))known[2*Number(id)]=v;for(let [id,v] of Object.entries(thetaKnown))known[2*Number(id)+1]=v;let free=Array.from({length:N},(_,i)=>i).filter(i=>known[i]===undefined),u=Array(N).fill(0);for(let [i,val] of Object.entries(known))u[+i]=val;if(free.length){let red=free.map(i=>free.map(j=>K[i][j])),rhs=free.map(i=>f[i]-Object.keys(known).reduce((s,j)=>s+K[i][j]*known[j],0)),sol=gaussian(red,rhs);free.forEach((i,j)=>u[i]=sol[j]);}const reactions=K.map((r,i)=>r.reduce((s,k,j)=>s+k*u[j],0)-f[i]);let ends=els.map(e=>e.ids.map((d,i)=>e.k[i].reduce((s,k,j)=>s+k*u[e.ids[j]],0)-e.fl[i]));return {u,reactions,ends,els};}
function beamCurve(res,Ls,EI){const arr=[],Ltot=Ls.reduce((a,b)=>a+b,0);let offset=0;Ls.forEach((L,e)=>{const v1=res.u[2*e],t1=res.u[2*e+1],v2=res.u[2*e+2],t2=res.u[2*e+3];for(let j=0;j<=35;j++){let r=j/35,x=offset+r*L,v=(1-3*r*r+2*r*r*r)*v1+(r-2*r*r+r*r*r)*L*t1+(3*r*r-2*r*r*r)*v2+(-r*r+r*r*r)*L*t2;arr.push([x,v*1000]);}offset+=L;});return arr;}
function curve(fn,min,max,n=100){let arr=[];for(let i=0;i<=n;i++){let x=min+(max-min)*i/n;arr.push([x,fn(x)]);}return arr;}
function frameLocal(EA,EI,L){let a=EA/L,b=12*EI/L**3,c=6*EI/L**2,d=4*EI/L,e=2*EI/L;return [[a,0,0,-a,0,0],[0,b,c,0,-b,c],[0,c,d,0,-c,e],[-a,0,0,a,0,0],[0,-b,-c,0,b,-c],[0,c,e,0,-c,d]];}
function frame2D(){let H=state.H,L=state.L,EI=state.EI*1000,EA=state.EA*1000,nodes=[[0,0],[0,H],[L,H],[L,0]],bars=[[0,1],[1,2],[2,3]],K=zeros(12,12),el=[];for(let [a,b] of bars){let dx=nodes[b][0]-nodes[a][0],dy=nodes[b][1]-nodes[a][1],len=Math.hypot(dx,dy),c=dx/len,s=dy/len,rot=[[c,s,0],[-s,c,0],[0,0,1]],T=zeros(6,6);for(let q=0;q<3;q++)for(let r=0;r<3;r++){T[q][r]=rot[q][r];T[q+3][r+3]=rot[q][r];}let kl=frameLocal(EA,EI,len),temp=zeros(6,6),kg=zeros(6,6);for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(let p=0;p<6;p++)temp[i][j]+=kl[i][p]*T[p][j];for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(let p=0;p<6;p++)kg[i][j]+=T[p][i]*temp[p][j];let ids=[3*a,3*a+1,3*a+2,3*b,3*b+1,3*b+2];for(let i=0;i<6;i++)for(let j=0;j<6;j++)K[ids[i]][ids[j]]+=kg[i][j];el.push({len,kl,T,ids});}
let f=Array(12).fill(0);f[6]=state.F;let free=[3,4,5,6,7,8],solution=gaussian(free.map(i=>free.map(j=>K[i][j])),free.map(i=>f[i])),u=Array(12).fill(0);free.forEach((i,j)=>u[i]=solution[j]);let baseR=K.map((r,i)=>r.reduce((s,k,j)=>s+k*u[j],0)-f[i]);let endmom=el.map(e=>{let local= e.T.map(row=>row.reduce((s,k,j)=>s+k*u[e.ids[j]],0));let ff=e.kl.map(row=>row.reduce((s,k,j)=>s+k*local[j],0));return [ff[2],ff[5]];});return {u,baseR,endmom,nodes};}
function eigen2(m1,m2,k1,k2){const b=(k1+k2)*m2+k2*m1,disc=Math.sqrt(Math.max(0,b*b-4*m1*m2*k1*k2)),l1=(b-disc)/(2*m1*m2),l2=(b+disc)/(2*m1*m2);let mode=l=>{let y=(k1+k2-l*m1)/k2;return [1/y,1];};return {l1,l2,m1:mode(l1),m2:mode(l2)};}
function sdof(s){let m=s.m*1000,k=s.k*1e6,z=s.z,F=s.F*1000,wn=Math.sqrt(k/m),wf=s.ratio*wn,c=2*z*Math.sqrt(k*m),dt=(2*Math.PI/wn)/90,steps=600,beta=.25,gamma=.5,x=0,v=0,a=0,pts=[];for(let i=0;i<=steps;i++){let t=i*dt,force=F*Math.sin(wf*t),xpred=x+dt*v+dt*dt*(.5-beta)*a,vpred=v+dt*(1-gamma)*a,an=(force-c*vpred-k*xpred)/(m+gamma*dt*c+beta*dt*dt*k);x=xpred+beta*dt*dt*an;v=vpred+gamma*dt*an;a=an;pts.push([t,x*1000]);}return {pts,wn,dt};}
function rng(seed){let x=seed>>>0;return ()=>{x=(1664525*x+1013904223)>>>0;return (x+.5)/4294967296;};}
function normal(rand){return Math.sqrt(-2*Math.log(rand()))*Math.cos(2*Math.PI*rand());}

  function solve(){const s=state,id=lab.id;let pts=[],metrics=[],notes='',yx='x',yy='response',extra=[];const m=(a,b,unit='')=>metrics.push([a,Number.isFinite(b)?Number(b.toFixed(5)):b,unit]);
if(id==='01'){let delta=s.P/(s.k1+s.k2),f1=s.k1*delta,f2=s.k2*delta;m('Common displacement',delta,'mm');m('Member 1 force',f1,'kN');m('Member 2 force',f2,'kN');m('Equilibrium residual',f1+f2-s.P,'kN');pts=[[1,f1],[2,f2]];yx='Branch number';yy='Member axial force (kN)';notes='Ideal axial springs act in parallel and share the same displacement. This is not a flexural member model.';}
else if(id==='02'){let R=3*s.w*s.L/8,Ra=s.w*s.L-R,Ma=-s.w*s.L*s.L/8,EI=s.EI*1000;m('Prop reaction',R,'kN');m('Fixed-end vertical reaction',Ra,'kN');m('Fixed-end moment',Ma,'kN·m');m('Free cantilever tip deflection without prop',s.w*s.L**4/(8*EI)*1000,'mm');pts=curve(x=> (-s.w*x*x*(6*s.L*s.L-4*s.L*x+x*x)/(24*EI)+R*x*x*(3*s.L-x)/(6*EI))*1000,0,s.L);yx='Distance from fixed end (m)';yy='Downward-negative deflection (mm)';notes='Linear elastic, constant EI, negligible shear deformation. Prop reaction follows compatibility; beam deflection sign assumes upward positive.';}
else if(id==='03'||id==='04'||id==='07'){let Ls=[s.L1,s.L2],EI=s.EI*1000,ws=id==='07'?[0,0]:[s.w1,s.w2],vs=id==='07'?{0:0,1:-s.d/1000,2:0}:{0:0,1:0,2:0},ths=id==='04'?{0:0,2:0}:{};let r=beamSolver(Ls,ws,EI,vs,ths);pts=beamCurve(r,Ls,EI);m('Rotation at intermediate joint',r.u[3]*1000,'mrad');m('Reaction A',r.reactions[0],'kN');m('Reaction B',r.reactions[2],'kN');m('Reaction C',r.reactions[4],'kN');m('Left-span end moment at B',r.ends[0][3],'kN·m');m('Right-span end moment at B',r.ends[1][1],'kN·m');m('Vertical equilibrium residual',r.reactions[0]+r.reactions[2]+r.reactions[4]-(ws[0]*s.L1+ws[1]*s.L2),'kN');yx='Distance along beam (m)';yy='Hermite-interpolated deflection (mm)';notes='Constant-EI two-node elements; 2 elements total. Deflection is cubic interpolation (uniform-load particular shape omitted), so it is NOT a mesh-converged continuous displacement field. End rotations and nodal reactions follow assembled stiffness.';}
else if(id==='05'){let E=s.E*1e6,A=s.A*1e-4,top=[0,s.h],bases=[[-s.a,0],[0,0],[s.a,0]],K=zeros(2,2),bars=[];bases.forEach((p,i)=>{let dx=top[0]-p[0],dy=top[1]-p[1],L=Math.hypot(dx,dy),cx=dx/L,cy=dy/L,k=E*A/L;K[0][0]+=k*cx*cx;K[0][1]+=k*cx*cy;K[1][0]+=k*cy*cx;K[1][1]+=k*cy*cy;bars.push({L,cx,cy,k});});let [ux,uy]=gaussian(K,[0,-s.P]);m('Top lateral displacement',ux*1000,'mm');m('Top vertical displacement',uy*1000,'mm');bars.forEach((b,i)=>m('Bar '+(i+1)+' axial force',b.k*(b.cx*ux+b.cy*uy),'kN'));pts=bars.map((b,i)=>[i+1,b.k*(b.cx*ux+b.cy*uy)]);yx='Bar number';yy='Axial force (kN, + tension)';notes='All bar ends are ideal pins. Middle bar is vertical and lower nodes are immovable. Units: GPa→kN/m² and cm²→m².';}
else if(id==='06'){let r=frame2D();m('Roof sway at left',r.u[3]*1000,'mm');m('Roof sway at right',r.u[6]*1000,'mm');m('Left base horizontal reaction',r.baseR[0],'kN');m('Right base horizontal reaction',r.baseR[9],'kN');m('Horizontal equilibrium residual',r.baseR[0]+r.baseR[9]+s.F,'kN');r.endmom.forEach((a,i)=>{m('Member '+(i+1)+' near-end M',a[0],'kN·m');m('Member '+(i+1)+' far-end M',a[1],'kN·m');});pts=[[0,0],[s.H,r.u[3]*1000],[s.H+s.L,r.u[6]*1000],[2*s.H+s.L,0]];yx='Unfolded frame perimeter (m)';yy='Nodal horizontal sway (mm)';notes='Plane frame uses 3 DOFs per node: axial translation, transverse translation and rotation. Base joints are fixed and roof joints rigid. Diagram is a trace of nodal drift, not a physical deformation plot.';}
else if(id==='08'){let alpha1=12e-6,alpha2=17e-6,E1=200e6,E2=70e6,A1=s.A1*1e-4,A2=s.A2*1e-4,free=alpha1*s.T1*s.L1+alpha2*s.T2*s.L2,comp=s.L1/(E1*A1)+s.L2/(E2*A2),N=-free/comp;m('Unrestrained total expansion',free*1000,'mm');m('Common axial force (− compression)',N,'kN');m('Segment 1 stress',N/A1/1000,'MPa');m('Segment 2 stress',N/A2/1000,'MPa');let dl1=(alpha1*s.T1+N/(E1*A1))*s.L1,dl2=(alpha2*s.T2+N/(E2*A2))*s.L2;pts=[[0,0],[s.L1,dl1*1000],[s.L1+s.L2,(dl1+dl2)*1000]];yx='Distance along bar (m)';yy='Actual axial displacement (mm)';notes='Fixed-fixed axial member, uniform segment temperatures and freely expanding connection; neglects joints, creep, nonlinear temperature dependence and buckling.';}
else if(id==='09'){let cr=Math.PI**2*s.EI*1000/(s.K*s.L)**2;m('Ideal elastic critical load',cr,'kN');m('Applied load',cr*s.ratio,'kN');m('Illustrative amplification factor',1/(1-s.ratio),'×');pts=curve(r=>1/(1-r),0,.92);yx='Axial load P/Pcr';yy='Amplification (idealized)';notes='Euler formula applies only to an ideal prismatic elastic member with ideal end restraints. Moment amplification here is a heuristic based on a single-mode approximation, not a P–Δ frame analysis.';}
else if(id==='10'){let x1=s.front,x2=s.front-s.space,axles=[[x1,s.P1],[x2,s.P2]].filter(a=>a[0]>=0&&a[0]<=s.L),Rb=axles.reduce((sum,[x,P])=>sum+P*x/s.L,0),Ra=axles.reduce((sum,[x,P])=>sum+P,0)-Rb,section=s.section*s.L,M=x=>Ra*x-axles.reduce((sum,[xx,P])=>sum+P*Math.max(0,x-xx),0);m('Reaction A',Ra,'kN');m('Reaction B',Rb,'kN');m('Moment at selected section',M(section),'kN·m');m('Vertical equilibrium residual',Ra+Rb-axles.reduce((sum,a)=>sum+a[1],0),'kN');pts=curve(M,0,s.L);yx='Position on beam (m)';yy='Bending moment (kN·m)';notes='Axles outside [0,L] do not load the bridge. Quasi-static, simply supported, no impact factor, distributed axle footprint, eccentricity or dynamic interaction.';}
else if(id==='11'){let m1=s.m1*1000,m2=s.m2*1000,k1=s.k1*1e6,k2=s.k2*1e6,e=eigen2(m1,m2,k1,k2);m('Mode 1 frequency',Math.sqrt(e.l1)/(2*Math.PI),'Hz');m('Mode 2 frequency',Math.sqrt(e.l2)/(2*Math.PI),'Hz');m('Mode 1 period',2*Math.PI/Math.sqrt(e.l1),'s');m('Mode 2 period',2*Math.PI/Math.sqrt(e.l2),'s');pts=[[0,0],[1,e.m1[0]],[2,e.m1[1]]];extra=[[0,0],[1,e.m2[0]],[2,e.m2[1]]];yx='Floor';yy='Normalized lateral mode shape';notes='Lumped two-floor, shear-only model. Mode shapes are normalized by roof movement; sign is arbitrary. Second mode displayed as dashed line.';}
else if(id==='12'){let r=sdof(s);pts=r.pts;m('Natural frequency',r.wn/(2*Math.PI),'Hz');m('Time step',r.dt,'s');m('Maximum |u|',Math.max(...pts.map(p=>Math.abs(p[1]))),'mm');m('Static displacement F/k',s.F/s.k,'mm');yx='Time (s)';yy='Displacement (mm)';notes='Newmark average acceleration β=1/4, γ=1/2. Force and zero initial conditions are synthetic. At low damping, transient evolution may require more cycles than plotted.';}
else if(id==='13'){let Pc=8*s.Mp/s.L,ratio=s.P/Pc;m('Fixed-fixed mechanism collapse load',Pc,'kN');m('Applied / collapse load',ratio,'×');m('Simply supported hinge collapse load',4*s.Mp/s.L,'kN');pts=curve(x=>x<=Pc?s.Mp*x/Pc:s.Mp,0,Math.max(Pc*1.35,s.P*1.05));yx='Applied point load (kN)';yy='Illustrative controlling plastic moment (kN·m)';notes='Rigid-perfectly-plastic mechanism model; a linear trace below Pc is schematic, not a complete elastic-plastic moment distribution. Lateral stability and section classification not assessed.';}
else if(id==='14'){let random=rng(1029),vals=[];for(let i=0;i<350;i++){let P=Math.max(.05,s.P*(1+normal(random)*s.covP/100)),E=Math.max(.05,s.E*(1+normal(random)*s.covE/100));vals.push(P*1000*s.L**3/(48*E*1e9*(s.I*1e-4))*1000);}vals.sort((a,b)=>a-b);let q=p=>vals[Math.floor(p*(vals.length-1))],mean=vals.reduce((a,b)=>a+b,0)/vals.length;m('Mean deflection',mean,'mm');m('5th percentile',q(.05),'mm');m('95th percentile',q(.95),'mm');m('Nominal elastic deflection',s.P*1000*s.L**3/(48*s.E*1e9*s.I*1e-4)*1000,'mm');pts=vals.map((v,i)=>[i/vals.length,v]);yx='Sorted sample quantile';yy='Deflection (mm)';notes='350 deterministic pseudo-random Gaussian perturbations truncated at positive values; NOT a calibrated probability-of-failure, material reliability or code design model.';}
else if(id==='15'){const exact=x=> -s.w*x*(s.L**3-2*s.L*x*x+x**3)/(24*s.EI*1000)*1000, target=.37*s.L,mesh=[2,3,4,6,8,12,16,24],out=[];for(let n of mesh){let ls=Array(n).fill(s.L/n),r=beamSolver(ls,Array(n).fill(s.w),s.EI*1000,{0:0,[n]:0});let i=Math.min(n-1,Math.floor(target/(s.L/n))),rr=(target-i*s.L/n)/(s.L/n),Le=s.L/n,va=r.u[2*i],ta=r.u[2*i+1],vb=r.u[2*i+2],tb=r.u[2*i+3],num=((1-3*rr*rr+2*rr**3)*va+(rr-2*rr*rr+rr**3)*Le*ta+(3*rr*rr-2*rr**3)*vb+(-rr*rr+rr**3)*Le*tb)*1000;out.push([n,Math.abs(num-exact(target))]);if(n===24)m('24-element interpolated deflection',num,'mm');}m('Exact deflection at x=0.37L',exact(target),'mm');m('24-element absolute error',out[out.length-1][1],'mm');pts=out;yx='Beam elements';yy='Absolute interpolation error (mm)';notes='The exact closed-form solution uses small-displacement Euler–Bernoulli beam theory. FE results use Hermite interpolation within elements; nodal quantities may converge faster than the interior field.';}
return {pts,extra,metrics,notes,xLabel:yx,yLabel:yy};}
function svgPlot(series,other,xlabel,ylabel){const all=[...series,...(other||[])],width=770,height=325,pad={l:76,r:24,t:20,b:64};if(!all.length)return '';let xs=all.map(d=>d[0]),ys=all.map(d=>d[1]),xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);if(xmax===xmin)xmax=xmin+1;if(ymax===ymin){ymax+=1;ymin-=1;}let dy=ymax-ymin;ymin-=dy*.1;ymax+=dy*.1;let px=x=>pad.l+(x-xmin)/(xmax-xmin)*(width-pad.l-pad.r),py=y=>height-pad.b-(y-ymin)/(ymax-ymin)*(height-pad.t-pad.b),path=data=>data.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+','+py(p[1]).toFixed(2)).join(' ');let g='';for(let i=0;i<=5;i++){let y=ymin+(ymax-ymin)*i/5;g+=`<line x1="${pad.l}" y1="${py(y)}" x2="${width-pad.r}" y2="${py(y)}" stroke="#dbe4ef"/><text x="${pad.l-10}" y="${py(y)+5}" text-anchor="end" font-size="12" fill="#52657b">${Number(y.toFixed(3))}</text>`;}for(let i=0;i<=5;i++){let x=xmin+(xmax-xmin)*i/5;g+=`<text x="${px(x)}" y="${height-pad.b+23}" text-anchor="middle" font-size="12" fill="#52657b">${Number(x.toFixed(2))}</text>`;}return `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="${ylabel} versus ${xlabel}"><rect width="${width}" height="${height}" fill="#fff" rx="12"/>${g}<path d="${path(series)}" stroke="#006ecb" fill="none" stroke-width="3"/>${other&&other.length?`<path d="${path(other)}" stroke="#df7a16" fill="none" stroke-dasharray="8,5" stroke-width="2.8"/>`:''}<text x="${width/2}" y="${height-10}" font-size="14" text-anchor="middle" fill="#233647">${xlabel}</text><text transform="translate(19 ${height/2}) rotate(-90)" font-size="14" text-anchor="middle" fill="#233647">${ylabel}</text></svg>`;}

function structuralDiagram(res){const s=state,id=lab.id;let items='';const line=(x1,y1,x2,y2,col='#0f6fa8',w=4)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" stroke-width="${w}" stroke-linecap="round"/>`;const circ=(x,y,r,col)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${col}"/>`;
if(id==='06'){let m=res.metrics,d1=m[0][1],d2=m[1][1],sc=42/Math.max(5,Math.abs(d1),Math.abs(d2)),yroof=50,x1=100,x2=540,bottom=210;items+=line(x1,bottom,x1,yroof,'#c4d2e0',6)+line(x1,yroof,x2,yroof,'#c4d2e0',6)+line(x2,yroof,x2,bottom,'#c4d2e0',6);items+=line(x1,bottom,x1+d1*sc,yroof)+line(x1+d1*sc,yroof,x2+d2*sc,yroof)+line(x2+d2*sc,yroof,x2,bottom);items+=circ(x1+d1*sc,yroof,6,'#df7a16')+circ(x2+d2*sc,yroof,6,'#df7a16');items+=`<text x="20" y="25" fill="#385a7b" font-size="13">Light gray: undeformed · Blue: exaggerated roof drift</text>`;}
else if(id==='05'){let uy=res.metrics[1][1],ux=res.metrics[0][1],left=90,center=330,right=570,roof=55,ground=220,ex=Math.max(-45,Math.min(45,ux*8)),ey=Math.max(-45,Math.min(45,-uy*12));for(let x of [left,center,right]){items+=line(x,ground,center,roof,'#c4d2e0',5)+line(x,ground,center+ex,roof+ey);items+=circ(x,ground,6,'#375b7e');}items+=circ(center+ex,roof+ey,7,'#df7a16')+`<text x="20" y="25" fill="#385a7b" font-size="13">Three fixed bases, free top joint · deformation exaggerated</text>`;}
else if(id==='03'||id==='07'){let all=res.pts,xmax=Math.max(...all.map(p=>p[0])),ymin=Math.min(...all.map(p=>p[1])),ymax=Math.max(...all.map(p=>p[1])),amp=Math.max(1,Math.abs(ymin),Math.abs(ymax)),scale=55/amp,py=v=>115-v*scale,pts=all.map(p=>((50+560*p[0]/xmax).toFixed(2))+','+py(p[1]).toFixed(2)).join(' ');items+=line(50,115,610,115,'#c4d2e0',5)+`<polyline points="${pts}" stroke="#0f6fa8" fill="none" stroke-width="3"/>`;for(let x of [0,s.L1,s.L1+s.L2]){let xx=50+560*x/xmax,yy=id==='07'&&x===s.L1?115+s.d*2:115;items+=`<path d="M ${xx-12} ${yy+15} L${xx+12} ${yy+15} L${xx} ${yy} Z" fill="#d17b18"/>`;}items+=`<text x="20" y="25" fill="#385a7b" font-size="13">Beam displacement shape exaggerated · triangular symbols are support positions</text>`;}
else if(id==='10'){let left=50,right=610,yy=155;items+=line(left,yy,right,yy);for(let x of [left,right])items+=`<path d="M${x} ${yy+2} l-10 17 h20 z" fill="#375b7e"/>`;for(let [x,p] of [[s.front,s.P1],[s.front-s.space,s.P2]])if(x>=0&&x<=s.L){let xx=left+560*x/s.L;items+=line(xx,yy-58,xx,yy-5,'#df7a16',3)+circ(xx,yy-58,8,'#df7a16')+`<text x="${xx}" y="${yy-74}" text-anchor="middle" font-size="14" fill="#234763">${p} kN</text>`;}items+=`<text x="20" y="25" fill="#385a7b" font-size="13">Only axles currently on the bridge transfer load to supports</text>`;}
else if(id==='11'){let d1=Math.max(-60,Math.min(60,res.pts[1][1]*60)),d2=Math.max(-60,Math.min(60,res.pts[2][1]*60));items+=line(320,230,320,55,'#b9ccdd',7)+line(320,230,320+d1,145)+line(320+d1,145,320+d2,60);items+=line(260+d1,145,380+d1,145)+line(260+d2,60,380+d2,60)+line(250,230,390,230,'#607d9a',6);items+=`<text x="20" y="25" fill="#385a7b" font-size="13">Mode 1 normalized roof movement; mode shape is not physical amplitude</text>`;}
else return '';
return `<svg viewBox="0 0 660 255" role="img" aria-label="Structural geometry and response" style="width:100%;max-width:700px;height:auto"><rect width="660" height="255" rx="12" fill="#f9fbfe"/>${items}</svg>`;
}
let state={},lab;


  var MODELS = [];

  LABS.forEach(function(labItem, idx) {
    var unit = labItem.u;
    var controlsHtml = labItem.inputs.map(function(inp) {
      var key = inp[0], label = inp[1], def = inp[2], min = inp[3], max = inp[4], step = inp[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sa2_' + labItem.id + '_' + key + '">' + label + ' <span id="v_sa2_' + labItem.id + '_' + key + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="sa2_' + labItem.id + '_' + key + '" data-key="' + key + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + labItem.id + ' · Unit ' + unit + '</span><h3>' + labItem.name + '</h3><p>' + labItem.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="diag" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS.push({
      idx: idx + 1,
      unit: unit,
      id: labItem.id,
      html: html,
      init: function(card) {
        try {
          var stateLocal = {};
          labItem.inputs.forEach(function(inp) { stateLocal[inp[0]] = inp[2]; });
          var plotEl = card.querySelector('.plot');
          var diagEl = card.querySelector('.diag');
          var metricsEl = card.querySelector('.metrics');
          var noteEl = card.querySelector('.model-note');

          function updateSA2() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              stateLocal[inp.dataset.key] = Number(inp.value);
              var vLbl = card.querySelector('#v_sa2_' + labItem.id + '_' + inp.dataset.key);
              if (vLbl) vLbl.textContent = inp.value;
            });

            lab = labItem;
            state = stateLocal;
            var res = solve();

            if (plotEl) plotEl.innerHTML = svgPlot(res.pts, res.other, res.yx, res.yy);
            if (diagEl) diagEl.innerHTML = structuralDiagram(res);
            if (metricsEl) {
              metricsEl.innerHTML = res.metrics.map(function(m) {
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + m[1] + '</output></div>';
              }).join('');
            }
            if (noteEl) noteEl.textContent = res.notes || '';
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', updateSA2);
          });
          updateSA2();
        } catch (err) {
          console.warn('Structural Analysis II sim error in model ' + labItem.id + ':', err);
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
