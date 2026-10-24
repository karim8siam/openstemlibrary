/* Operating Systems Simulation Suite (Units & Laboratory Models) */
/* OpenSTEM five-volume discrete simulation collection.
   Source: original educational models for bounded inputs, not measured production hardware.
   Each module is generated with a distinct BOOK_ID and model definitions.
*/
(function(root){
'use strict';
const BOOK_ID="operating-systems";
const UNIT_TITLES=["OS organization", "Processes and threads", "Concurrency", "Memory management", "File systems", "Storage and I/O", "Isolation and security", "Distributed and practical systems"];
const defs=UNIT_TITLES.map((name,i)=>({id:BOOK_ID+'-unit-'+(i+1),unit:i+1,name,min:1,max:12,start:6}));
function check(n){if(!Number.isInteger(n)||n<1||n>12) throw Error('Input must be an integer from 1 to 12');}
function choose(n,k){if(k<0||k>n)return 0;let ans=1;for(let i=1;i<=k;i++)ans=ans*(n-k+i)/i;return Math.round(ans);}
function result(n,value,units,plot,detail){return {n,value,units,values:plot,headline:`${String(value)} ${units}`,detail};}
function simulate(id,input){
  const def=defs.find(d=>d.id===id); if(!def) throw Error('Unknown model: '+String(id));
  const n=Number(input);check(n); const u=def.unit; let values=[];
  if(BOOK_ID==='algorithms'){
    if(u===1){const v=n*n, log=Math.ceil(n*Math.log2(Math.max(2,n)));return result(n,v,'quadratic reference operations',[log,v],`Compare a quadratic workload with n log2 n. These are models, not CPU timings.`);}
    if(u===2){const inv=n*(n-1)/2;return result(n,inv,'inversions on reversed unique keys',[n,inv],`Insertion sorting reversed input requires one comparison for each inversion; n(n−1)/2.`);}
    if(u===3){const k=Math.ceil(Math.log2(n)),c=n*k-Math.pow(2,k)+1;return result(n,c,'worst-case merge comparisons',[n,c],`Standard comparison mergesort worst-case recurrence, with n distinct keys and careful unequal splits.`);}
    if(u===4){const options=Array.from({length:n},(_,i)=>({start:i,end:i+((i%3)+1)}));let chosen=0,finish=-1;for(const x of options.slice().sort((a,b)=>a.end-b.end||a.start-b.start)){if(x.start>=finish){chosen++;finish=x.end;}}return result(n,chosen,'compatible intervals selected',[n,chosen],`Earliest-finish greedy scheduling on a deterministic list of n half-open intervals.`);}
    if(u===5){const dp=[0];for(let i=1;i<=n;i++)dp[i]=Math.min(...[1,3,4].filter(c=>c<=i).map(c=>dp[i-c]+1));let rem=n,greedy=0;for(const c of [4,3,1]){greedy+=Math.floor(rem/c);rem%=c;}return result(n,dp[n],'optimal coins',[dp[n],greedy],`Compares optimal DP and descending-denomination greedy for coins 1,3,4; 6 is a known greedy failure.`);}
    if(u===6){const dist=Array(n).fill(Infinity);dist[0]=0;for(let i=0;i<n;i++){if(i+1<n)dist[i+1]=Math.min(dist[i+1],dist[i]+1);if(i+2<n)dist[i+2]=Math.min(dist[i+2],dist[i]+3);}return result(n,dist[n-1],'shortest path cost from node 0 to last node',[n-1,dist[n-1]],`Directed DAG with adjacent edges weight 1 and two-hop edges weight 3; edges are nonnegative.`);}
    if(u===7){const maximal=Math.floor(n/2);return result(n,2*maximal,'cover vertices chosen',[n,2*maximal],`Endpoints of a maximal matching on a path graph; a valid 2-approximate vertex cover (not necessarily minimum).`);}
    const p=1/n;return result(n,Number(p.toFixed(6)),'probability each item is retained',[p,1-p],`Reservoir sampling of one element among n items; each item is kept with exact probability 1/n.`);
  }
  if(BOOK_ID==='discrete-structures-for-computer-science'){
    if(u===1)return result(n,Math.pow(2,n),'binary truth assignments',[n,Math.pow(2,n)],`There are two choices independently for each of n Boolean variables.`);
    if(u===2){const counts=[0,0,0];for(let i=0;i<n;i++)counts[i%3]++;return result(n,Math.max(...counts),'largest residue-class size modulo 3',counts,`Partitions integers 0..n−1 into congruence classes under mod 3.`);}
    if(u===3){const c=choose(n,Math.floor(n/2));return result(n,c,'middle binomial coefficient',[n,c],`Counts unordered subsets of size floor(n/2) selected from n distinct objects.`);}
    if(u===4){const p=n/Math.pow(2,n);return result(n,Number(p.toFixed(6)),'probability of exactly one head',[p,1-p],`Assumes n independent fair coin tosses. Exactly n sequences have one head among 2^n equally likely sequences.`);}
    if(u===5)return result(n,n-1,'edges in a path tree',[n,n-1],`A connected acyclic path on n vertices has n−1 edges.`);
    if(u===6){let a=0,b=1;for(let j=0;j<n;j++){const t=a+b;a=b;b=t;}return result(n,a,'Fibonacci F(n)',[n,a],`Starting with F(0)=0 and F(1)=1, computes recurrence F(n)=F(n−1)+F(n−2).`);}
    if(u===7){let inv=0;for(let i=1;i<13;i++)if((i*n)%13===1){inv=i;break;}return result(n,inv,'inverse modulo prime 13',[n,inv],`The inverse exists because 13 is prime and 1≤n≤12.`);}
    const bits=n.toString(2);const ones=[...bits].filter(x=>x==='1').length;return result(n,ones%2===0?'accept':'reject','even-one-parity DFA',[ones,bits.length],`The two-state DFA toggles on every '1' of binary representation ${bits}; accepts even parity.`);
  }
  if(BOOK_ID==='computer-architecture'){
    if(u===1){const sec=n*1e8*1.5/3e9;return result(n,Number(sec.toFixed(4)),'ideal CPU seconds',[n,sec],`Instructions=n·100 million, CPI=1.5, frequency=3 GHz. Ignores I/O and OS overhead.`);}
    if(u===2){const raw=(n*19)%256, signed=raw>=128?raw-256:raw;return result(n,signed,'signed 8-bit interpretation',[raw,signed],`Pattern is n×19 reduced modulo 256, interpreted as two's-complement.`);}
    if(u===3){const raw=250+n,low=raw%256;return result(n,low,'8-bit ALU output',[raw,low],`Unsigned addition 250+n; carry-out=1 if sum exceeds 255.`);}
    if(u===4){const serial=5*n,pipe=5+n-1;return result(n,Number((serial/pipe).toFixed(3)),'ideal pipeline speedup',[pipe,serial],`A five-stage ideal pipeline vs five serial stages, equal cycle time and no hazards.`);}
    if(u===5){const misses=Math.ceil(n/4);return result(n,misses,'compulsory 16-byte block misses',[n,misses],`n sequential 4-byte accesses from byte address 0, empty non-evicting cache; each block covers four accesses.`);}
    if(u===6){const work=20*n;return result(n,work,'microseconds of direct interrupt service',[n,work],`n interrupts of 20 µs handler cost each; excludes context and cache overhead.`);}
    if(u===7){const speedup=1/(0.2+0.8/n);return result(n,Number(speedup.toFixed(3)),'Amdahl speedup',[n,speedup],`80% perfectly parallel and 20% serial work; n identical workers, no communication overhead.`);}
    const voltage=1-0.025*n,power=voltage*voltage;return result(n,Number(power.toFixed(4)),'relative dynamic power',[voltage,power],`P proportional to V² at unchanged activity, capacitance and frequency. V ranges from 0.975 to 0.700.`);
  }
  if(BOOK_ID==='operating-systems'){
    if(u===1)return result(n,n*2,'microseconds of direct syscall overhead',[n,n*2],`Assumes each of n system calls has constant 2 µs transition overhead and no I/O delay.`);
    if(u===2){let remaining=[n,Math.max(1,Math.floor(n/2))],clock=0,finish=[0,0];while(remaining[0]>0||remaining[1]>0){for(let p=0;p<2;p++){if(remaining[p]>0){let used=Math.min(2,remaining[p]);remaining[p]-=used;clock+=used;if(!remaining[p])finish[p]=clock;}}}return result(n,(finish[0]+finish[1])/2,'mean round-robin turnaround units',finish,`Both jobs arrive at time zero; bursts n and floor(n/2), quantum 2, no switch cost.`);}
    if(u===3){const arrangements=choose(2*n,n);return result(n,arrangements,'interleavings of two ordered instruction streams',[n,arrangements],`Each thread has n steps retaining its own order; ignores locks and memory effects.`);}
    if(u===4){const refs=[1,2,3,1,4,2,5,1,2,3,4,5],mem=[],queue=[];let faults=0;for(const r of refs.slice(0,n)){if(!mem.includes(r)){faults++;if(mem.length===3){const old=queue.shift();mem.splice(mem.indexOf(old),1);}mem.push(r);queue.push(r);}}return result(n,faults,'FIFO page faults',[n,faults],`Three initially empty page frames; FIFO advances insertion order only upon a miss.`);}
    if(u===5){const size=1000*n;return result(n,Math.ceil(size/4096),'4096-byte blocks allocated',[size,Math.ceil(size/4096)],`Dense file of n×1000 bytes; no sparse extents, inline storage or filesystem metadata.`);}
    if(u===6){const requests=[55,10,90,65,20,80,25,75,30,70,35,60];let pos=50,seek=0;for(const x of requests.slice(0,n)){seek+=Math.abs(x-pos);pos=x;}return result(n,seek,'FCFS head-movement cylinders',[n,seek],`Fixed request sequence starting at cylinder 50; measures movement, not SSD latency.`);}
    if(u===7){const mode=n%8;return result(n,mode,'Unix owner permission digit',[Boolean(mode&4)?1:0,Boolean(mode&2)?1:0,Boolean(mode&1)?1:0],`r=${Boolean(mode&4)}, w=${Boolean(mode&2)}, x=${Boolean(mode&1)}; owner digit only, not a full ACL.`);}
    const rate=n*0.5,mean=1/(10-rate);return result(n,Number(mean.toFixed(4)),'M/M/1 mean time in system (seconds)',[rate,mean],`Poisson arrival λ=${rate}/s, exponential service μ=10/s and λ<μ; stable steady-state formula.`);
  }
  if(BOOK_ID==='database-systems'){
    if(u===1)return result(n,n*2,'enrollment relationships',[n,n*2],`A synthetic model with n students each related to exactly two courses; unique student-course pairs assumed.`);
    if(u===2){const matches=n+Math.floor(n/2);return result(n,matches,'equijoin result rows',[n,matches],`n student IDs; enrollment includes one row per student plus one extra for each of first floor(n/2) students.`);}
    if(u===3){const records=n*100,leaves=Math.ceil(records/64);return result(n,leaves,'idealized B+tree leaf pages',[records,leaves],`Each leaf has capacity 64 entries at 100% occupancy; ignores fill factor and metadata.`);}
    if(u===4){const comparisons=(n*100)*(n*20);return result(n,comparisons,'nested-loop predicate comparisons',[n*100,n*20],`Cross compares n·100 outer with n·20 inner rows, without indexes or short-circuiting.`);}
    if(u===5)return result(n,n,'correct counter increments with serialization',[1,n],`n clients each increment once. Serial execution results in n; unprotected simultaneous read-modify-write could result in 1.`);
    if(u===6){const log=2*n+1;return result(n,log,'illustrative write-ahead log records',[n,log],`Assumes two change records per transaction plus one checkpoint record; a toy record-count model, not a DBMS implementation.`);}
    if(u===7){const N=5,R=(n%5)+1,W=3,intersection=R+W>N;return result(n,intersection?'yes':'no','read/write quorums intersect',[R,W],`For N=5, R=${R}, W=3, intersection guaranteed iff R+W>N; does not by itself enforce linearizability.`);}
    const seq=[1,2,1,3,2,4,1,2,5,1,3,4],cache=[],hits=[];let h=0;for(const x of seq.slice(0,n)){const ix=cache.indexOf(x);if(ix>=0){h++;cache.splice(ix,1);}else if(cache.length===3)cache.shift();cache.push(x);hits.push(h);}return result(n,h,'LRU cache hits',[n,h],`Three-entry LRU cache, initially empty, with a fixed request trace; misses=${n-h}.`);
  }
  throw Error('Unknown book module');
}
function draw(data){
 const nums=data.values.map(x=>Number(x));const max=Math.max(1,...nums.filter(Number.isFinite).map(Math.abs));
 const cols=nums.map((v,i)=>{const h=Number.isFinite(v)?Math.max(2,Math.round(Math.abs(v)/max*72)):2;return `<g transform="translate(${18+i*63},0)"><rect y="${85-h}" height="${h}" width="45" rx="4" fill="${i%2?'#17858d':'#355ea9'}"></rect><text x="22" y="101" text-anchor="middle" font-size="10" fill="currentColor">${Number.isFinite(v)?Number(v.toFixed(3)):''}</text></g>`;}).join('');
 return `<svg viewBox="0 0 ${Math.max(220,nums.length*63+26)} 110" role="img" aria-label="Numerical model output bars" style="width:100%;max-height:180px;overflow:visible">${cols}</svg>`;
}
function render(host,id){
 if(typeof document==='undefined'||!host)return;
 const d=defs.find(x=>x.id===id);if(!d)return;
 host.replaceChildren();
 const panel=document.createElement('section');panel.className='openstem-simulation';panel.style='margin:1rem 0;padding:1rem;border:1px solid #8bb9c0;border-radius:12px';
 const head=document.createElement('h4');head.textContent=d.name+' — interactive model';
 const label=document.createElement('label');label.textContent='Input size / parameter: ';
 const slider=document.createElement('input');slider.type='range';slider.min=d.min;slider.max=d.max;slider.step='1';slider.value=d.start;slider.setAttribute('aria-label',d.name+' parameter');
 const numeric=document.createElement('output');numeric.textContent=String(d.start);label.append(slider,numeric);
 const status=document.createElement('p');status.setAttribute('aria-live','polite');const plot=document.createElement('div');const assumptions=document.createElement('p');
 const button=document.createElement('button');button.type='button';button.textContent='Reset';
 function update(){try{const x=simulate(id,Number(slider.value));numeric.textContent=String(x.n);status.textContent=x.headline;plot.innerHTML=draw(x);assumptions.textContent=x.detail;}catch(e){status.textContent=e.message;plot.replaceChildren();assumptions.textContent='';}}
 slider.addEventListener('input',update);button.addEventListener('click',()=>{slider.value=d.start;update();});panel.append(head,label,status,plot,assumptions,button);host.append(panel);update();
}
const API={defs,simulate,render};if(typeof module!=='undefined'&&module.exports)module.exports=API;
root.OpenSTEMNext5=root.OpenSTEMNext5||{};root.OpenSTEMNext5[BOOK_ID]=API;
if(typeof document!=='undefined'){
 const original=root.SimulationEngine&&root.SimulationEngine.initSimulation;
 root.SimulationEngine=root.SimulationEngine||{};
 root.SimulationEngine.initSimulation=function(containerId,simType){if(String(simType).startsWith(BOOK_ID+'-unit-'))render(document.getElementById(containerId),simType);else if(typeof original==='function')original.call(this,containerId,simType);};
}
})(typeof window!=='undefined'?window:globalThis);


/* Original OpenSTEM Operating Systems lab simulations — bounded educational models.
 * Designed to run without an external server; not production kernel benchmarks.
 */
(function(root){
'use strict';
const book='operating-systems';
const defs=Array.from({length:8},(_,i)=>({id:`operating-systems-lab-${i+1}`,unit:i+1,name:[
  'Partial-read progress and record framing','Round-robin scheduling with fixed bursts','Protected versus racing counter increments',
  'LRU page replacement trace','File-system block allocation and slack','I/O batch setup amortization',
  'Sandbox rights selection','End-to-end speedup and slow-stage bottlenecks'][i],min:1,max:12,start:5}));
function valid(id,n){if(!defs.some(d=>d.id===id))throw Error('Unknown Operating Systems lab model');if(!Number.isInteger(n)||n<1||n>12)throw Error('Input must be integer 1 through 12');}
function rr(bursts,quantum){
 const remaining=bursts.slice(),completion=remaining.map(()=>0);let clock=0,switches=0,last=-1;
 while(remaining.some(v=>v>0)){
  for(let i=0;i<remaining.length;i++){
   if(remaining[i]<=0)continue;
   if(last>=0&&last!==i)switches++;
   last=i;const dt=Math.min(quantum,remaining[i]);clock+=dt;remaining[i]-=dt;if(remaining[i]===0)completion[i]=clock;
  }
 }
 return {completion,switches,mean:completion.reduce((a,b)=>a+b,0)/completion.length};
}
function lru(seq,frames){const resident=[],out=[];let faults=0,hits=0;
 for(const x of seq){const ix=resident.indexOf(x);if(ix<0){faults++;if(resident.length>=frames)resident.shift();}else{hits++;resident.splice(ix,1);}resident.push(x);out.push(resident.slice());}
 return {faults,hits,frames:resident,out};}
function simulate(id,n){
 valid(id,n);const u=Number(id.split('-').at(-1));let value,units,values=[],detail;
 switch(u){
 case 1:{const length=7*n,chunk=5,calls=Math.ceil(length/chunk),last=length-chunk*(calls-1);
   value=calls;units='read calls';values=[length,calls,last];detail=`Need ${length} payload bytes, at most ${chunk} bytes per read. ${calls} reads; last transfers ${last}. A short read is not EOF.`;break;}
 case 2:{const b=[5,3,7],x=rr(b,n);value=Number(x.mean.toFixed(3));units='mean turnaround units';values=[...x.completion,x.switches];detail=`All arrivals at zero, bursts [5,3,7], time quantum ${n}, no switch cost. Completion times ${x.completion.join(',')}; ${x.switches} cross-job switches.`;break;}
 case 3:{value=2*n;units='correct protected increments';values=[n,2*n];detail=`Two workers each increment ${n} times: serializable protected result ${2*n}. An unsafe coordinated stale-read schedule can lose updates; the lower bar n is an illustration, not the only possible race outcome.`;break;}
 case 4:{const refs=[1,2,3,1,4,2,5,1,2,3,4,5],x=lru(refs.slice(0,n),3);value=x.faults;units='LRU page faults';values=[n,x.faults,x.hits];detail=`Three initially empty frames, fixed reference prefix length ${n}. Hits ${x.hits}; final MRU order ${x.frames.join(',')}.`;break;}
 case 5:{const size=9000*n,block=4096,blocks=Math.ceil(size/block),slack=blocks*block-size;value=blocks;units='allocated data blocks';values=[size,blocks,slack];detail=`Dense ${size}-byte file, ${block}-byte blocks, no metadata or compression; trailing slack ${slack} bytes.`;break;}
 case 6:{const simple=52*n,batch=50*Math.ceil(n/3)+2*n;value=simple-batch;units='microseconds setup savings';values=[simple,batch,value];detail=`${n} records, fixed setup 50 µs per I/O plus 2 µs/record; batches hold up to 3 records. No batch wait or queueing included.`;break;}
 case 7:{const mask=n&15,rights=['read','write','network','execute'].filter((_,i)=>(mask&(1<<i))!==0);value=rights.length;units='granted modeled capabilities';values=[Number(Boolean(mask&1)),Number(Boolean(mask&2)),Number(Boolean(mask&4)),Number(Boolean(mask&8))];detail=`Policy mask ${mask} exposes ${rights.join(', ')||'no rights'}. Demonstrates rights accounting; it is not an actual process sandbox.`;break;}
 case 8:{const newTime=30+170/n;value=Number((200/newTime).toFixed(4));units='end-to-end speedup factor';values=[200,newTime,value];detail=`200-ms baseline = 30-ms other + 170-ms slow stage; speed that stage by ${n}×. New total ${newTime.toFixed(3)} ms, max possible overall speedup 200/30.`;break;}
 default:throw Error('No model');
 }
 return {n,value,units,values,headline:`${value} ${units}`,detail};
}
function plot(data){const nums=data.values.map(Number),largest=Math.max(1,...nums.map(Math.abs));return `<svg viewBox="0 0 ${Math.max(240,nums.length*68+28)} 126" role="img" aria-label="Modeled input and output values" style="width:100%;max-height:174px">${nums.map((v,i)=>{const h=Math.max(2,Math.round(Math.abs(v)/largest*80));return `<g transform="translate(${16+i*68},0)"><rect y="${92-h}" width="48" height="${h}" rx="4" fill="${i%2?'#0e8686':'#355ea9'}"></rect><text x="24" y="112" text-anchor="middle" font-size="10" fill="currentColor">${Number.isFinite(v)?Number(v.toFixed(2)):''}</text></g>`;}).join('')}</svg>`;}
function render(host,id){if(!host||typeof document==='undefined')return;const d=defs.find(v=>v.id===id);if(!d)return;
 host.replaceChildren();const pane=document.createElement('section');pane.className='openstem-simulation';pane.style='padding:1rem;border:1px solid #9cc4c9;border-radius:11px;margin:1rem 0;max-width:100%';
 const h=document.createElement('h3');h.textContent=d.name;const label=document.createElement('label');label.textContent='Parameter: ';
 const input=document.createElement('input');input.type='range';input.min=d.min;input.max=d.max;input.step=1;input.value=d.start;input.setAttribute('aria-label',d.name+' parameter');
 const output=document.createElement('output');label.append(input,output);const status=document.createElement('p');status.setAttribute('aria-live','polite');
 const graph=document.createElement('div'),note=document.createElement('p'),reset=document.createElement('button');reset.type='button';reset.textContent='Reset';
 function update(){try{const r=simulate(id,Number(input.value));output.textContent=' '+r.n;status.textContent=r.headline;graph.innerHTML=plot(r);note.textContent=r.detail;}catch(e){status.textContent=e.message;graph.replaceChildren();note.textContent='';}}
 input.addEventListener('input',update);reset.addEventListener('click',()=>{input.value=d.start;update();});pane.append(h,label,status,graph,note,reset);host.append(pane);update();}
const API={defs,simulate,render,rr,lru};if(typeof module!=='undefined'&&module.exports)module.exports=API;
root.OpenSTEMOSLabs=API;
if(typeof document!=='undefined'){
  const previous=root.SimulationEngine&&root.SimulationEngine.initSimulation;
  root.SimulationEngine=root.SimulationEngine||{};
  root.SimulationEngine.initSimulation=function(id,type){if(String(type).startsWith('operating-systems-lab-'))return render(document.getElementById(id),type);if(typeof previous==='function')return previous.call(this,id,type);};
}
})(typeof window!=='undefined'?window:globalThis);

