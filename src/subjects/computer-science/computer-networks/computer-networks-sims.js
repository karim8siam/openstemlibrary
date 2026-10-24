/* OpenSTEM Computer Networks — sixteen bounded instructional models.
   These are deliberately simplified mathematical models, not packet captures or
   guarantees of behavior on the public Internet. Tested against Python oracles. */
(function(root){'use strict';
const BOOK='computer-networks';
const models={
'cn-header-overhead': {title:'Header efficiency',unit:1,measure:'percent payload',notes:'Assume one 1200-byte payload and n additional 20-byte headers, with no other overhead.',fn:n=>100*1200/(1200+20*n)},
'cn-fiber-delay': {title:'Fiber propagation delay',unit:1,measure:'ms one-way',notes:'n segments of 100 km of fiber each, group velocity 200,000 km/s; excludes router and queue delay.',fn:n=>n*100/200000*1000},
'cn-serialization': {title:'Link serialization time',unit:2,measure:'ms',notes:'Exactly 1500 bytes and n megabits/second; no medium contention or link preamble.',fn:n=>12000/(n*1e6)*1000},
'cn-aloha': {title:'Pure ALOHA throughput',unit:2,measure:'successful frames per frame time',notes:'Poisson offered load G=n/10, idealized pure ALOHA S=G exp(-2G); never a model of CSMA or Wi-Fi.',fn:n=>(n/10)*Math.exp(-2*n/10)},
'cn-ipv4-hosts': {title:'IPv4 ordinary subnet host count',unit:3,measure:'host addresses',notes:'An ordinary IPv4 subnet with n host bits has 2^n addresses, subtract network and directed broadcast; not /31 or /32.',fn:n=>2**n-2},
'cn-router-serialization': {title:'Store-and-forward pipeline',unit:3,measure:'ms serialization total',notes:'n identical hops of a 1500-byte frame over 100 Mbit/s; assumes complete-frame store-and-forward and ignores propagation.',fn:n=>n*12000/100e6*1000},
'cn-stopwait': {title:'Stop-and-wait useful goodput',unit:4,measure:'Mbit/s',notes:'12,000 useful bits, 1.2 ms transmit time, n ms total acknowledgment round trip, no losses or processing.',fn:n=>12000/((n+1.2)/1000)/1e6},
'cn-bdp': {title:'Bandwidth-delay product',unit:4,measure:'bytes',notes:'10 Mbit/s path capacity and n ms RTT; bytes of data in flight ignoring headers and retransmission.',fn:n=>10e6*(n/1000)/8},
'cn-cache-misses': {title:'DNS-style deterministic TTL',unit:5,measure:'cache misses',notes:'One identical query each integer time step, zero-based starting at t=0, TTL exactly 5 steps, no prefetch.',fn:n=>Math.ceil(n/5)},
'cn-http-cache': {title:'HTTP cache origin fetches',unit:5,measure:'origin fetches',notes:'Repeated same cacheable resource, requests once per second, freshness lifetime four seconds, no revalidation or eviction.',fn:n=>Math.ceil(n/4)},
'cn-exposure': {title:'Independent-event illustration',unit:6,measure:'percent chance of at least one event',notes:'Fictional independent 1% per-event probability; NOT an empirical breach probability and not a security risk score.',fn:n=>100*(1-0.99**n)},
'cn-handshake': {title:'Handshake latency budget',unit:6,measure:'ms modeled',notes:'A toy handshake requiring two network RTTs of n ms plus fixed 3 ms processing; not a measured TLS 1.3 or QUIC handshake.',fn:n=>2*n+3},
'cn-queue-length': {title:'M/M/1 expected queue system size',unit:7,measure:'jobs in system',notes:'Stationary M/M/1 queue: Poisson arrival n jobs/s, exponential service 20 jobs/s, n strictly below 20.',fn:n=>n/(20-n)},
'cn-queue-wait': {title:'M/M/1 mean queue waiting time',unit:7,measure:'ms waiting',notes:'Wq=lambda/[mu(mu-lambda)] seconds for lambda=n/s and mu=20/s; excludes service and network propagation.',fn:n=>n/(20*(20-n))*1000},
'cn-hop-delay': {title:'Underlay hop delay budget',unit:8,measure:'ms one-way',notes:'Assume fixed 3 ms propagation for a path and 0.3 ms per hop over n hops; ignore queuing and congestion.',fn:n=>3+0.3*n},
'cn-ecmp-unused': {title:'Expected unused equal-cost lanes',unit:8,measure:'unused lanes expected',notes:'n independent uniformly hashed flows across four ECMP lanes, no elephant-flow weights; expectation 4(3/4)^n.',fn:n=>4*(0.75**n)}
};
const ids=Object.keys(models);
function calculate(type,n){
  if(!Object.hasOwn(models,type))throw new RangeError('Unknown simulation type');
  if(!Number.isInteger(n)||n<2||n>16)throw new RangeError('Input n must be integer 2..16');
  const m=models[type],value=m.fn(n);
  if(!Number.isFinite(value))throw Error('Nonfinite model result');
  return {book:BOOK,type,unit:m.unit,n,value,unitLabel:m.measure,notes:m.notes,title:m.title};
}
function initSimulation(elementId,type){
 if(typeof document==='undefined')return false;
 const el=document.getElementById(elementId);if(!el||!Object.hasOwn(models,type))return false;
 const m=models[type];el.textContent='';
 const title=document.createElement('h4');title.textContent=m.title;
 const label=document.createElement('label');label.textContent='Input n (2–16): ';
 const slider=document.createElement('input');slider.type='range';slider.min='2';slider.max='16';slider.step='1';slider.value='6';slider.setAttribute('aria-label',m.title+' input n');label.append(slider);
 const output=document.createElement('output');output.setAttribute('aria-live','polite');
 const explain=document.createElement('p');
 const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('role','img');svg.setAttribute('viewBox','0 0 360 145');svg.setAttribute('aria-label',m.title+' across permitted input values');svg.style.width='100%';svg.style.maxWidth='640px';
 function render(){const n=Number(slider.value),res=calculate(type,n);output.value='n='+n+' → '+Number(res.value.toPrecision(7))+' '+res.unitLabel;output.textContent=output.value;explain.textContent='Assumptions and limits: '+res.notes;
   svg.replaceChildren();const values=Array.from({length:15},(_,k)=>calculate(type,k+2));const max=Math.max(1e-12,...values.map(x=>x.value));
   values.forEach((v,i)=>{const bar=document.createElementNS('http://www.w3.org/2000/svg','rect');bar.setAttribute('x',String(8+i*23));bar.setAttribute('y',String(130-115*v.value/max));bar.setAttribute('height',String(Math.max(0,115*v.value/max)));bar.setAttribute('width','17');bar.setAttribute('rx','2');bar.setAttribute('fill',v.n===n?'#d9962d':'#227a9e');const t=document.createElementNS('http://www.w3.org/2000/svg','title');t.textContent='n='+v.n+', '+Number(v.value.toPrecision(6))+' '+res.unitLabel;bar.append(t);svg.append(bar);});
 }
 slider.addEventListener('input',render);reset.addEventListener('click',()=>{slider.value='6';render()});
 el.append(title,label,output,svg,explain,reset);render();return true;
}
root.OpenSTEMModel={book:BOOK,ids,calculate,initSimulation,models};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
