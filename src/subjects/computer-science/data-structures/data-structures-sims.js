/* OpenSTEM: Data Structures model library. Original educational source.
 * Exact models have explicit assumptions; does not claim to profile real runtimes.
 * The CommonJS exports support unit testing without DOM or external packages. */
(function(root){
'use strict';
const defs=[
 {id:'array-growth',unit:1,name:'Geometric array growth',min:1,max:64,start:9,summary:'Capacity starts at 1 and doubles when full; counts copies during reallocations.'},
 {id:'scan',unit:1,name:'Minimum scan comparisons',min:1,max:64,start:12,summary:'Initialize the minimum with element zero and compare each remaining item once.'},
 {id:'linked-walk',unit:2,name:'Linked-list index traversal',min:1,max:50,start:9,summary:'A pointer traversal visits one node per element up to the requested one-based position.'},
 {id:'ringqueue',unit:2,name:'Circular queue index wrap',min:1,max:40,start:8,summary:'After n dequeue operations, head advances by n modulo a fixed capacity of 7.'},
 {id:'bst-height',unit:3,name:'Sorted versus balanced BST height',min:1,max:64,start:12,summary:'Compares height in edges for increasing-key insertion with the minimum possible binary-tree height.'},
 {id:'bst-path',unit:3,name:'BST search path',min:1,max:15,start:7,summary:'Fixed tree: insert 8,3,10,1,6,14,4,7,13, then look for a target key.'},
 {id:'hash-chains',unit:4,name:'Separate-chaining collisions',min:1,max:30,start:12,summary:'Insert keys 1,8,15,22,… into 7 buckets with h(k)=k mod 7.'},
 {id:'probing',unit:4,name:'Linear-probing collision trace',min:1,max:16,start:6,summary:'Insert keys 1,18,35,… into a capacity-17 open-addressed table.'},
 {id:'heap-push',unit:5,name:'Sift-up heap insertion',min:1,max:10,start:6,summary:'Insert a prefix of fixed priorities into a min-heap and show heap array order.'},
 {id:'heap-min',unit:5,name:'Min-priority queue removals',min:1,max:10,start:6,summary:'Extract priorities in nondecreasing order from a fixed set; ties are not present.'},
 {id:'bfs',unit:6,name:'Breadth-first search levels',min:1,max:6,start:4,summary:'Explore a full binary tree to the selected number of levels; nodes at level ℓ equal 2^ℓ.'},
 {id:'components',unit:6,name:'Connected-component unions',min:1,max:7,start:4,summary:'Count components among 8 vertices after the first n edges of a fixed undirected graph.'},
 {id:'trie',unit:7,name:'Trie prefix sharing',min:1,max:8,start:5,summary:'Insert a prefix of eight fixed words; count distinct trie nodes including the root.'},
 {id:'fenwick',unit:7,name:'Fenwick prefix sums',min:1,max:12,start:5,summary:'Sum the first k values of a fixed array using a Fenwick tree; show visited one-based indices.'},
 {id:'memory',unit:8,name:'Packed array versus node chain',min:1,max:100,start:20,summary:'Lower bounds only: 4-byte numeric value in either representation and an extra 8-byte pointer per node.'},
 {id:'iterator',unit:8,name:'Iterator generation validity',min:1,max:12,start:5,summary:'Model a fail-fast versioned iterator after n mutations; it demonstrates a contract, not native pointer safety.'}
];
const inputNumbers=[8,3,7,1,9,2,5,4,6,10];
function heapInsert(h,x){h.push(x);let i=h.length-1;while(i>0){let p=Math.floor((i-1)/2);if(h[p]<=h[i])break;[h[p],h[i]]=[h[i],h[p]];i=p;}}
function bst(){let root=null;for(const k of [8,3,10,1,6,14,4,7,13]){if(!root){root={k,l:null,r:null};continue;}let cur=root;while(true){const c=k<cur.k?'l':'r';if(!cur[c]){cur[c]={k,l:null,r:null};break;}cur=cur[c];}}return root;}
function components(n){let p=Array.from({length:8},(_,i)=>i);function find(i){while(p[i]!==i)i=p[i];return i;}let count=8;const edges=[[0,1],[1,2],[3,4],[5,6],[2,4],[4,6],[6,7]];for(let i=0;i<n;i++){const[a,b]=edges[i],x=find(a),y=find(b);if(x!==y){p[y]=x;count--;}}return count;}
function simulate(id,value){
 const d=defs.find(x=>x.id===id||'ds-'+x.id===id);if(!d)throw Error('Unknown model: '+id);
 const n=Number(value);if(!Number.isInteger(n)||n<d.min||n>d.max)throw Error('Input must be an integer from '+d.min+' to '+d.max);
 let values=[],headline='',detail='';
 switch(d.id){
 case 'array-growth':{let cap=1,copies=0,events=[];for(let k=0;k<n;k++)if(k===cap){copies+=cap;cap*=2;events.push(k);}values=[n,cap,copies];headline=`${n} elements · capacity ${cap} · ${copies} copies`;detail='Reallocations before insertion counts: '+(events.join(', ')||'none')+'; copies count moved old elements, not newly written ones.';break;}
 case 'scan':values=[n,Math.max(0,n-1)];headline=`${Math.max(0,n-1)} comparisons`;detail='The first value initializes the minimum; every following value is compared exactly once.';break;
 case 'linked-walk':values=[n,n-1];headline=`${n-1} next-pointer hops`;detail=`For one-based index ${n}, start at head (position 1), then advance ${n-1} links.`;break;
 case 'ringqueue':values=[n,n%7];headline=`head=${n%7} after ${n} dequeues`;detail='Initial head is zero; indices wrap modulo capacity 7. Requires enough enqueued values to perform all dequeues.';break;
 case 'bst-height':{const worst=n-1,best=Math.ceil(Math.log2(n+1))-1;values=[worst,best];headline=`sorted height ${worst}; minimum ${best}`;detail='Heights count edges. The minimum is possible in a maximally filled tree, not guaranteed by a plain BST.';break;}
 case 'bst-path':{let node=bst(),path=[];while(node){path.push(node.k);if(n===node.k)break;node=n<node.k?node.l:node.r;}values=path;headline=(node?'Found':'Absent')+` after ${path.length} comparisons`;detail='Visited keys: '+path.join(' → ');break;}
 case 'hash-chains':{values=Array(7).fill(0);for(let i=0;i<n;i++)values[(7*i+1)%7]++;headline=`${n} entries in bucket 1`;detail='All values collide deliberately; a chain still distinguishes equal-hash keys by key equality.';break;}
 case 'probing':{values=Array.from({length:n},(_,i)=>(1+i)%17);headline=`${n} probes to insert key ${1+17*(n-1)}`;detail='Slots visited in the collision cluster: '+values.join(', ');break;}
 case 'heap-push':{let heap=[];for(const x of inputNumbers.slice(0,n))heapInsert(heap,x);values=heap;headline=`heap minimum ${heap[0]}`;detail='Physical heap array: ['+heap.join(', ')+']; this is not a sorted array.';break;}
 case 'heap-min':{let a=inputNumbers.slice(0,n).sort((x,y)=>x-y);values=a;headline=`removed priorities: ${a.join(', ')}`;detail='A min-priority queue removes the smallest current priority on each extraction.';break;}
 case 'bfs':{values=Array.from({length:n},(_,i)=>2**i);const total=2**n-1;headline=`${total} vertices in ${n} BFS levels`;detail='Frontier sizes by depth: '+values.join(', ');break;}
 case 'components':{values=Array.from({length:n+1},(_,i)=>i===0?8:components(i));headline=`${components(n)} connected components`;detail='The example unions vertices of an eight-vertex graph; the plotted series includes initial state.';break;}
 case 'trie':{const words=['cat','car','cart','dog','dot','dove','care','careful'];const set=new Set(['']);for(const word of words.slice(0,n)){let p='';for(const ch of word){p+=ch;set.add(p)}}values=[n,set.size];headline=`${set.size} trie nodes including root`;detail='Inserted words: '+words.slice(0,n).join(', ');break;}
 case 'fenwick':{const a=[2,1,3,4,5,1,2,6,7,3,4,8],ft=Array(13).fill(0);for(let i=1;i<=12;i++)for(let j=i;j<=12;j+=j&-j)ft[j]+=a[i-1];let j=n,sum=0,visited=[];while(j){visited.push(j);sum+=ft[j];j-=j&-j;}values=visited;headline=`prefix sum ${sum}`;detail='Fenwick entries visited (one-based): '+visited.join(' → ');break;}
 case 'memory':values=[4*n,12*n];headline=`${4*n} bytes packed vs ≥${12*n} bytes linked`;detail='Illustrative lower bound excluding alignment, allocator/object headers, and container metadata.';break;
 case 'iterator':values=[0,n];headline='iterator invalid after mutation';detail='Versioned container increments its modification counter from 0 to '+n+'; earlier iterator holds generation 0.';break;
 }
 if(values.some(v=>!Number.isFinite(v)))throw Error('Non-finite model output');
 return {id:d.id,n,headline,detail,values};
}
function chart(values){const w=320,h=105,absMax=Math.max(1,...values.map(Math.abs));const barW=Math.max(3,(w-16)/Math.max(1,values.length)-3);return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Bar chart showing ${values.length} numeric observations"><path d="M1 ${h-2} H${w}" stroke="currentColor" opacity=".5"/>${values.map((v,i)=>{const bh=Math.max(1,Math.abs(v)/absMax*85);const x=8+i*(w-16)/values.length;return `<rect x="${x.toFixed(1)}" y="${(h-3-bh).toFixed(1)}" width="${barW.toFixed(1)}" height="${bh.toFixed(1)}" fill="#157c85"/>`}).join('')}</svg>`;}
function render(host,id){if(typeof document==='undefined'||!host)return;const d=defs.find(x=>x.id===id||'ds-'+x.id===id);if(!d)return;host.innerHTML='';const p=document.createElement('section');p.className='openstem-simulation';p.style='padding:1em;margin:1em 0;border:1px solid #96aeba;border-radius:12px';const h=document.createElement('h4');h.textContent=d.name;const note=document.createElement('p');note.textContent=d.summary;const label=document.createElement('label');label.textContent='Input: ';const input=document.createElement('input');input.type='range';input.min=d.min;input.max=d.max;input.step=1;input.value=d.start;const output=document.createElement('output');output.textContent=String(d.start);input.setAttribute('aria-label',d.name+' input');label.append(input,output);const result=document.createElement('div');result.setAttribute('aria-live','polite');const plot=document.createElement('div');const info=document.createElement('p');const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';function update(){try{const x=simulate(d.id,Number(input.value));output.textContent=String(x.n);result.textContent=x.headline;plot.innerHTML=chart(x.values);info.textContent=x.detail;}catch(e){result.textContent=e.message;plot.replaceChildren();info.textContent='';}}input.addEventListener('input',update);reset.addEventListener('click',()=>{input.value=d.start;update()});p.append(h,note,label,result,plot,info,reset);host.append(p);update();}
const API={defs,simulate,render};if(typeof module!=='undefined'&&module.exports)module.exports=API;root.OpenSTEMDataStructuresSims=API;
if(typeof document!=='undefined'){
 const prior=root.SimulationEngine&&root.SimulationEngine.initSimulation;
 root.SimulationEngine=root.SimulationEngine||{};
 root.SimulationEngine.initSimulation=function(containerId,simType){if(String(simType).startsWith('ds-')){render(document.getElementById(containerId),simType);}else if(typeof prior==='function'){prior.call(this,containerId,simType);}};
}
})(typeof window!=='undefined'?window:globalThis);
