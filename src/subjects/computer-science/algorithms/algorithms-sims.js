/* Algorithms Simulation Suite (Units & Laboratory Models) */
/* OpenSTEM five-volume discrete simulation collection.
   Source: original educational models for bounded inputs, not measured production hardware.
   Each module is generated with a distinct BOOK_ID and model definitions.
*/
(function(root){
'use strict';
const BOOK_ID="algorithms";
const UNIT_TITLES=["Algorithm analysis", "Searching and sorting", "Divide and conquer", "Greedy methods", "Dynamic programming", "Graph algorithms", "Complexity and approximation", "Randomized algorithms"];
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


/* OpenSTEM original subject-specific laboratory models; independent tests in QA scripts. */
(function(root){
'use strict';
const defs=[
  {id:"algorithms-lab-1",unit:1,name:"Binary-search worst-case probes",summary:"How many comparisons does ordinary binary search need in its longest successful or failed path for a sorted array of n distinct values?",description:"An iterative binary search halves the remaining interval after each unsuccessful probe. The maximum number of examined elements is floor(log2 n)+1. It is not the number of comparisons needed to sort the input.",min:1,max:12,start:5,compute(n){const v=Math.floor(Math.log2(n))+1;return result(n,v,"worst-case inspected midpoints",[n,v],"Sorted distinct keys; no preprocessing included. Each midpoint counts as one probe.");}},
  {id:"algorithms-lab-2",unit:2,name:"Merging two sorted runs",summary:"Two sorted sequences of n distinct values can be merged with at most 2n\u22121 element comparisons, when their keys alternate until the last element.",description:"The merge algorithm repeatedly compares the head items and advances the smaller one. Once one run is empty, the remainder is copied without comparisons. For two length-n runs the longest comparison sequence has length 2n\u22121.",min:1,max:12,start:5,compute(n){return result(n,2*n-1,"worst-case merge comparisons",[n,n,2*n-1],"Both input runs contain n keys. A final unpaired element needs no comparison.");}},
  {id:"algorithms-lab-3",unit:3,name:"Quicksort ordered-input degeneration",summary:"With first-element pivot selection and an already increasing array, every partition can leave an empty left side and n\u22121 elements on the right.",description:"The recurrence is C(n)=C(n\u22121)+(n\u22121), C(1)=0. Its solution is n(n\u22121)/2 comparisons, not the expected O(n log n) typical of balanced pivots. Changing the pivot policy changes this example.",min:1,max:12,start:5,compute(n){return result(n,n*(n-1)/2,"ordered-input comparisons",[n,n*(n-1)/2],"Worst case for the specified first-pivot partition convention; does not represent randomized pivot selection.");}},
  {id:"algorithms-lab-4",unit:4,name:"Greedy exchange on interval scheduling",summary:"A set of n half-open unit-length intervals starting at consecutive integers is pairwise compatible, so the earliest-finish strategy selects all n.",description:"An exchange argument compares the greedy interval ending first to the first interval in an optimal solution. Substituting it does not displace any later interval. The example is intentionally simple; larger overlapping schedules need the actual sort and compatibility check.",min:1,max:12,start:5,compute(n){return result(n,n,"compatible unit intervals selected",[n,n],"Intervals [i,i+1) for i=0..n−1. Adjacent endpoints are compatible in this half-open convention.");}},
  {id:"algorithms-lab-5",unit:5,name:"Zero-one knapsack exact dynamic program",summary:"Choose items with weights 2,3,4,5 and values 3,4,5,8 under a capacity of n. The objective is to maximize the total value without choosing any item twice.",description:"A one-dimensional descending-capacity dynamic program prevents an item from being used repeatedly. If capacity is 5, choosing the weight-five item yields value eight; weights two plus three yield only seven.",min:1,max:12,start:5,compute(n){const W=[2,3,4,5],V=[3,4,5,8],dp=Array(n+1).fill(0);for(let k=0;k<4;k++)for(let c=n;c>=W[k];c--)dp[c]=Math.max(dp[c],dp[c-W[k]]+V[k]);return result(n,dp[n],"maximum knapsack value",[n,dp[n]],"Each item is available at most once. Descending capacity updates enforce this restriction.");}},
  {id:"algorithms-lab-6",unit:6,name:"Dijkstra path comparison",summary:"Compare the path A\u2192B\u2192C\u2192D (edge weights 1,n,1) with the direct A\u2192D edge of weight n+3, for n positive.",description:"The three-edge route has cost n+2, which is smaller by one for every input. Dijkstra is applicable because all weights are nonnegative. Changing the graph to contain negative edges would invalidate this solver.",min:1,max:12,start:5,compute(n){return result(n,n+2,"shortest A-to-D cost",[n+2,n+3],"Directed edges A-B=1, B-C=n, C-D=1, A-D=n+3; all nonnegative.");}},
  {id:"algorithms-lab-7",unit:7,name:"Vertex-cover approximation on a star",summary:"For a star with n leaves, the minimum vertex cover consists solely of the center, while selecting both endpoints of any maximal-matching edge gives a cover of size two.",description:"This model exhibits an approximation ratio of two on a family of graphs. It demonstrates a worst-case bound that can actually be reached, rather than claiming the algorithm always uses twice the optimum.",min:1,max:12,start:5,compute(n){return result(n,2,"matching-endpoint cover size",[1,2,n+1],"One center and n leaves. Optimal cover=1; maximal matching has one edge, yielding two selected endpoints.");}},
  {id:"algorithms-lab-8",unit:8,name:"Seeded Monte Carlo disk estimator",summary:"Estimate \u03c0 using 400n deterministic pseudorandom points sampled uniformly in the unit square, counting the fraction in the quarter-circle x\u00b2+y\u00b2\u22641.",description:"The expected indicator of inside the quarter-circle equals \u03c0/4. Four times the empirical mean estimates \u03c0. A fixed seed permits repeatable student tests but is not a proof of convergence and does not replace statistical uncertainty assessment.",min:1,max:12,start:5,compute(n){let seed=20261023,inside=0,total=400*n;function rnd(){seed=(Math.imul(1664525,seed)+1013904223)>>>0;return seed/4294967296;}for(let i=0;i<total;i++){let x=rnd(),y=rnd();if(x*x+y*y<=1)inside++;}const v=4*inside/total;return result(n,Number(v.toFixed(5)),"estimated pi",[Math.PI,v],"Seeded linear congruential generator; toy Monte Carlo error varies by sample size.");}},
];
function result(n,value,units,values,detail){return {n,value,units,values,headline:String(value)+' '+units,detail};}
function run(id,input){const d=defs.find(x=>x.id===id);if(!d)throw Error('Unknown simulation ID');const n=Number(input);
 if(!Number.isInteger(n)||n<d.min||n>d.max)throw Error('Input outside the defined integer range');return d.compute(n);}
function render(target,id){const d=defs.find(x=>x.id===id);if(!d||!target||typeof document==='undefined')return;
 target.replaceChildren();const outer=document.createElement('section');outer.className='openstem-simulation';outer.style.cssText='padding:1rem;border:1px solid #819cac;border-radius:12px;margin:1rem 0';
 const heading=document.createElement('h4');heading.textContent=d.name;
 const note=document.createElement('p');note.textContent=d.summary;
 const lab=document.createElement('label');lab.textContent='Input parameter: ';
 const control=document.createElement('input');control.type='range';control.min=d.min;control.max=d.max;control.step=1;control.value=d.start;control.setAttribute('aria-label',d.name+' input');
 const out=document.createElement('output');out.textContent=String(d.start);lab.append(control,out);
 const status=document.createElement('p');status.setAttribute('aria-live','polite');const graphic=document.createElement('div');
 const detail=document.createElement('p');const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';
 function draw(){try{const x=run(id,Number(control.value));out.textContent=String(x.n);status.textContent=x.headline;
  const vals=x.values.filter(v=>typeof v==='number'&&Number.isFinite(v));const max=Math.max(1,...vals.map(Math.abs));
  graphic.replaceChildren();const bars=document.createElement('div');bars.style.cssText='display:flex;align-items:end;min-height:100px;gap:8px';
  vals.forEach((v,i)=>{const bar=document.createElement('div');bar.style.cssText='height:'+Math.max(4,Math.abs(v)/max*92)+'px;background:#327b91;flex:1;min-width:8px';
  bar.title='Series '+(i+1)+': '+v;bar.setAttribute('aria-label',bar.title);bars.append(bar);});graphic.append(bars);detail.textContent=x.detail;
 }catch(e){status.textContent=e.message;graphic.replaceChildren();detail.textContent='';}}
 control.addEventListener('input',draw);reset.addEventListener('click',()=>{control.value=d.start;draw();});
 outer.append(heading,note,lab,status,graphic,detail,reset);target.append(outer);draw();}
const api={defs,run,render};if(typeof module!=='undefined'&&module.exports)module.exports=api;
root.OpenSTEMLabModels=root.OpenSTEMLabModels||{};root.OpenSTEMLabModels["algorithms"]=api;
if(typeof document!=='undefined'){const previous=root.SimulationEngine&&root.SimulationEngine.initSimulation;
root.SimulationEngine=root.SimulationEngine||{};
root.SimulationEngine.initSimulation=function(containerId,simType){
  if(defs.some(d=>d.id===simType))render(document.getElementById(containerId),simType);
  else if(typeof previous==='function')previous.call(this,containerId,simType);
};}
})(typeof window!=='undefined'?window:globalThis);

