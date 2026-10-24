/* Original OpenSTEM Database Systems teaching simulations.
   Outputs are toy mathematical models under explicit assumptions, not DBMS benchmarks.
   Book 7: 16 independent interactive models across eight units.
*/
(function(root){
'use strict';
const BOOK_ID="database-systems";
const UNIT_TITLES=["Data modeling", "Relational systems", "Storage engines", "Query processing", "Transactions", "Recovery and integrity", "Distributed databases", "Application databases"];
const defs=UNIT_TITLES.flatMap((name,i)=>[{id:BOOK_ID+'-unit-'+(i+1),unit:i+1,name:name+' — foundations',min:1,max:12,start:6},{id:BOOK_ID+'-advanced-'+(i+1),unit:i+1,name:name+' — comparative experiment',min:1,max:12,start:6}]);
function check(n){if(!Number.isInteger(n)||n<1||n>12) throw Error('Input must be an integer from 1 to 12');}
function choose(n,k){if(k<0||k>n)return 0;let ans=1;for(let i=1;i<=k;i++)ans=ans*(n-k+i)/i;return Math.round(ans);}
function result(n,value,units,plot,detail){return {n,value,units,values:plot,headline:`${String(value)} ${units}`,detail};}
function simulate(id,input){
  const def=defs.find(d=>d.id===id); if(!def) throw Error('Unknown model: '+String(id));
  const n=Number(input);check(n); const u=def.unit; let values=[];
  if(BOOK_ID==='database-systems' && id.startsWith(BOOK_ID+'-advanced-')){
    if(u===1){ // Multiplicity from independently joining child relations with 2 and 3 matches.
      return result(n,6*n,'joined rows',[n,2*n,6*n],`For ${n} parents, each with two Enrollment and three Contact rows, a raw two-child join yields 6n rows. Group children first when calculating parent measures.`);
    }
    if(u===2){ // LEFT JOIN retains unmatched odd student IDs; even IDs have two matches.
      const matched=Math.floor(n/2),rows=2*matched+(n-matched);
      return result(n,rows,'left-join rows',[n,matched,rows],`Students 1..${n}: even IDs have two enrollments and odd IDs have none. LEFT JOIN returns two rows for each even ID and one for each odd ID.`);
    }
    if(u===3){
      const entries=100*n, packed=Math.ceil(entries/64),filled=Math.ceil(entries/48);
      return result(n,filled,'B+tree leaf pages at 75% fill',[packed,filled],`The toy leaf holds 64 entries at 100% or 48 at 75%. Count=${entries}; internal pages and fragment history excluded.`);
    }
    if(u===4){
      const outer=100*n,inner=20*n, nested=outer*inner, hash=outer+inner;
      return result(n,Number((nested/hash).toFixed(3)),'toy nested-loop/hash row-work ratio',[nested,hash],`Nested loop uses ${nested} comparisons; a simplified in-memory hash join handles ${hash} input rows. Ignore output volume, hash collisions and spilling.`);
    }
    if(u===5){
      return result(n,n-1,'increments lost by simultaneous read–modify–write',[1,n],`${n} clients all read counter zero and each writes one, without locking. Final observed counter is one; correct serial increments produce ${n}. This is a deliberately unsafe schedule.`);
    }
    if(u===6){
      const generated=3*n, boundary=Math.floor(n/4)*4, replay=n-boundary;
      return result(n,replay,'transactions since last toy checkpoint',[n,boundary,replay],`Checkpoint at multiples of four transactions, and one toy transaction after another. This only counts transactions since a boundary; real engines replay according to log and dirty pages.`);
    }
    if(u===7){
      let moved=0;for(let k=1;k<=n;k++)if(k%3!==k%4)moved++;
      return result(n,moved,'IDs remapped from 3 to 4 shards',[n,moved],`Student IDs 1..${n}, routed by id % shard_count; changing modulus from 3 to 4 moves ${moved} keys. Toy key movement is not proof of balanced workload.`);
    }
    if(u===8){
      const trace=[1,2,1,3,2,4,1,2,5,1,3,4],cache=[],hits=[];let h=0;
      for(const v of trace.slice(0,n)){if(cache.includes(v)){h++;}else {if(cache.length===3)cache.shift();cache.push(v);}hits.push(h);}
      return result(n,h,'FIFO cache hits',[n,h],`Three-entry FIFO cache on fixed trace 1,2,1,3,2,4,1,2,5,1,3,4. Compare with foundation simulation using LRU.`);
    }
  }
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
 root.SimulationEngine.initSimulation=function(containerId,simType){if(String(simType).startsWith(BOOK_ID+'-unit-')||String(simType).startsWith(BOOK_ID+'-advanced-'))render(document.getElementById(containerId),simType);else if(typeof original==='function')original.call(this,containerId,simType);};
}
})(typeof window!=='undefined'?window:globalThis);
