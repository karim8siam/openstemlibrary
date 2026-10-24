/* OpenSTEM Computer Graphics — local editorial demonstrations, not production integration.
 * The core calculate function is intentionally pure and independently testable.
 */
(function (root) {
'use strict';
const CONFIG = Object.freeze({
 'cg-u1-a':{title:'Affine point mapping',label:'transformed x coordinate',note:'Input n is local x; fixed scale x2 and translation +5. Local y=2, scale y3, translation y−1.',min:2,max:12},
 'cg-u1-b':{title:'Pinhole horizontal projection',label:'image x coordinate',note:'Positive camera depth Z=n, horizontal X=3, focal length f=2. Ideal pinhole model; no distortion.',min:2,max:12},
 'cg-u2-a':{title:'Parametric line clipping',label:'visible segment length',note:'Segment from (−2,1) to (6,1+n/2) clipped to [0,4]×[0,4]; length measured in viewport units.',min:2,max:12},
 'cg-u3-a':{title:'Circle chord deviation',label:'maximum radial error in pixels',note:'Radius 100 pixels, regular inscribed n-gon with n=4k; exact error 100[1−cos(pi/n)].',min:2,max:12},
 'cg-u3-b':{title:'Triangle subdivision growth',label:'triangle count',note:'Start with 200 triangles and apply n−2 uniform levels, each replacing one triangle by four.',min:2,max:12},
 'cg-u2-b':{title:'Barycentric temperature',label:'interpolated temperature',note:'Triangle (0,0),(4,0),(0,4); point (n/5,1), temperatures 10,20,50. This is an interpolated estimate.',min:2,max:12},
 'cg-u4-a':{title:'Diffuse radiance and incidence angle',label:'outgoing radiance (W/m² sr)',note:'Lambertian reflectance 0.6; normal-incidence irradiance 100 W/m²; angle=5n degrees. Outgoing radiance=(60/pi)cos(angle).',min:2,max:12},
 'cg-u4-b':{title:'Dielectric Fresnel reflectance',label:'normal-incidence reflected fraction',note:'Air index 1; dielectric index=1+n/10. Lossless single interface, normal incidence.',min:2,max:12},
 'cg-u5-a':{title:'Sphere first-hit ray distance',label:'first-hit ray parameter',note:'Sphere radius 2 at origin, ray starts (0,0,-n), direction (0,0,1). At n=2 ray starts on the surface.',min:2,max:12},
 'cg-u5-b':{title:'Beer–Lambert transmission',label:'direct-path transmittance',note:'Homogeneous medium with extinction coefficient 0.2 m^-1; distance=n metres. In-scattering omitted.',min:2,max:12},
 'cg-u6-a':{title:'Ease-in/ease-out Hermite position',label:'position',note:'Zero-velocity cubic Hermite between positions 2 and 10, normalized time u=n/12.',min:2,max:12},
 'cg-u6-b':{title:'Two-link elbow angle',label:'elbow angle (degrees)',note:'Link lengths 3 and 2, target distance r=1+n/4, positive elbow branch. All slider targets are reachable.',min:2,max:12},
 'cg-u7-a':{title:'Render pixel count under scaling',label:'relative pixel count',note:'Scale each image dimension by n/12; relative pixel count is (n/12)^2.',min:2,max:12},
 'cg-u7-b':{title:'CPU/GPU throughput bound',label:'maximum estimated FPS',note:'CPU stage 11 ms, GPU stage n+8 ms. Ideal overlapped steady throughput 1000/max(CPU,GPU).',min:2,max:12},
 'cg-u8-a':{title:'Area-weighted temperature anomaly',label:'weighted mean anomaly (°C)',note:'Two regions: first anomaly n/3 °C with weight 0.75, second -1 °C with weight 0.25.',min:2,max:12},
 'cg-u8-b':{title:'Volume opacity per sample',label:'per-step opacity',note:'Homogeneous extinction 0.4 m^-1; step length n/4 metres; alpha=1-exp(-sigma*d).',min:2,max:12}
});
function clip(p0,p1,box){
 const d=[p1[0]-p0[0],p1[1]-p0[1]];
 let low=0,high=1;
 for(let axis=0;axis<2;axis++){
  const a=p0[axis],v=d[axis],mn=box[axis*2],mx=box[axis*2+1];
  if(v===0){if(a<mn||a>mx)return null;continue;}
  let t0=(mn-a)/v,t1=(mx-a)/v;
  if(t0>t1){const t=t0;t0=t1;t1=t;}
  low=Math.max(low,t0);high=Math.min(high,t1);
  if(low>high)return null;
 }
 return {t0:low,t1:high,a:p0.map((x,i)=>x+low*d[i]),b:p0.map((x,i)=>x+high*d[i])};
}
function calculate(id,n){
 if(!Object.prototype.hasOwnProperty.call(CONFIG,id))throw new RangeError('unknown model');
 if(!Number.isInteger(n)||n<2||n>12)throw new RangeError('n must be integer from 2 to 12');
 if(id==='cg-u1-a')return 2*n+5;
 if(id==='cg-u1-b')return 6/n;
 if(id==='cg-u2-a'){
  const c=clip([-2,1],[6,1+n/2],[0,4,0,4]);
  return c===null?0:Math.hypot(c.b[0]-c.a[0],c.b[1]-c.a[1]);
 }
 if(id==='cg-u3-a')return 100*(1-Math.cos(Math.PI/(4*n)));
 if(id==='cg-u3-b')return 200*4**(n-2);
 if(id==='cg-u2-b'){
  const x=n/5,y=1;
  const a=1-x/4-y/4,b=x/4,c=y/4;
  return 10*a+20*b+50*c;
 }
 if(id==='cg-u4-a')return (60/Math.PI)*Math.cos(n*5*Math.PI/180);
 if(id==='cg-u4-b'){const r=(1-(1+n/10))/(1+(1+n/10));return r*r;}
 if(id==='cg-u5-a')return n-2;
 if(id==='cg-u5-b')return Math.exp(-0.2*n);
 if(id==='cg-u6-a'){const u=n/12;return 2+8*(3*u*u-2*u*u*u);}
 if(id==='cg-u6-b'){const r=1+n/4;return Math.acos((r*r-13)/12)*180/Math.PI;}
 if(id==='cg-u7-a')return (n/12)**2;
 if(id==='cg-u7-b')return 1000/Math.max(11,n+8);
 if(id==='cg-u8-a')return n/4-0.25;
 if(id==='cg-u8-b')return 1-Math.exp(-0.4*n/4);
 throw new Error('unreachable');
}
function initSimulation(containerId,id){
 if(typeof document==='undefined')throw new Error('browser required');
 const container=document.getElementById(containerId);
 if(!container)throw new Error('missing container '+containerId);
 const spec=CONFIG[id];if(!spec)throw new Error('unknown simulation');
 const h=document.createElement('h3');h.textContent=spec.title;
 const desc=document.createElement('p');desc.textContent=spec.note;
 const label=document.createElement('label');label.textContent='Input n: ';
 const input=document.createElement('input');input.type='range';input.min=spec.min;input.max=spec.max;input.value='6';input.step='1';input.setAttribute('aria-label',spec.title+' parameter n');
 const value=document.createElement('output');value.setAttribute('aria-live','polite');
 const reset=document.createElement('button');reset.type='button';reset.textContent='Reset';
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 320 90');svg.setAttribute('role','img');svg.setAttribute('aria-label',spec.title+' illustrative response bar');
 const bar=document.createElementNS('http://www.w3.org/2000/svg','rect');bar.setAttribute('x','12');bar.setAttribute('y','20');bar.setAttribute('height','35');bar.setAttribute('rx','5');bar.setAttribute('fill','#317ca5');svg.appendChild(bar);
 const curve=document.createElementNS('http://www.w3.org/2000/svg','polyline');curve.setAttribute('fill','none');curve.setAttribute('stroke','#a34424');curve.setAttribute('stroke-width','2.5');svg.appendChild(curve);
 const point=document.createElementNS('http://www.w3.org/2000/svg','circle');point.setAttribute('r','5');point.setAttribute('fill','#163d57');svg.appendChild(point);
 function render(){
  const n=Number(input.value),y=calculate(id,n);
  value.textContent=`n = ${n}; ${spec.label} = ${Number(y.toFixed(6))}`;
  const ys=[];for(let k=spec.min;k<=spec.max;k++)ys.push(calculate(id,k));
  const hi=Math.max(...ys),lo=Math.min(...ys),span=hi-lo;
  const xAt=k=>12+296*(k-spec.min)/(spec.max-spec.min);
  const yAt=v=>75-(span===0?0.5:(v-lo)/span)*56;
  curve.setAttribute('points',ys.map((v,i)=>`${xAt(spec.min+i)},${yAt(v)}`).join(' '));
  point.setAttribute('cx',String(xAt(n)));point.setAttribute('cy',String(yAt(y)));
  bar.setAttribute('width',String(hi===0?0:Math.max(1,Math.min(290,290*Math.abs(y)/(Math.max(Math.abs(hi),Math.abs(lo))||1)))));
 }
 input.addEventListener('input',render);reset.addEventListener('click',()=>{input.value='6';render();});
 label.appendChild(input);container.append(h,desc,label,value,reset,svg);render();
 return {input,value,reset,svg};
}
const API=Object.freeze({calculate,clip,initSimulation,config:CONFIG});
if(typeof module!=='undefined'&&module.exports)module.exports=API;
root.ComputerGraphicsSimulations=API;
})(typeof window!=='undefined'?window:globalThis);

/* SimulationEngine adapter for Computer Graphics */
(function(root){
  if (typeof document !== 'undefined') {
    var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
    root.SimulationEngine = root.SimulationEngine || {};
    root.SimulationEngine.initSimulation = function(containerId, simType) {
      if (root.ComputerGraphicsSimulations && root.ComputerGraphicsSimulations.config && root.ComputerGraphicsSimulations.config[simType]) {
        return root.ComputerGraphicsSimulations.initSimulation(containerId, simType);
      }
      if (typeof previous === 'function') {
        return previous.call(this, containerId, simType);
      }
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
