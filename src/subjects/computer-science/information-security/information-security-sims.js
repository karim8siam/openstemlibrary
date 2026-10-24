/* OpenSTEM Information Security — original bounded educational simulations.
   Safe local mathematical models only: no requests, scanning, exploitation or credentials.
*/
(function (root) {
  'use strict';
  function finite(x, min, max, label) {
    if (typeof x !== 'number' || !Number.isFinite(x) || x < min || x > max)
      throw new RangeError((label || 'Value') + ' must be in [' + min + ', ' + max + ']');
    return x;
  }
  function integer(x, min, max, label) {
    finite(x, min, max, label);
    if (!Number.isInteger(x)) throw new RangeError((label || 'Value') + ' must be an integer');
    return x;
  }
  const computations = {
    exposureRate(assets, exposed, factor) {
      integer(assets,1,100000); integer(exposed,0,assets); finite(factor,0,1);
      return {exposed,assets,exposedFraction:exposed/assets,estimatedAffected:exposed*factor};
    },
    riskReduction(probability,impact,effectiveness) {
      finite(probability,0,1);finite(impact,0,1000000);finite(effectiveness,0,1);
      return {baselineExpectedLoss:probability*impact,residualExpectedLoss:probability*impact*(1-effectiveness)};
    },
    nonceCollision(bits,draws) {
      integer(bits,32,256);integer(draws,0,1000000);
      const n=draws, exponent=Math.log(2)*bits, approx=-Math.expm1(-n*(n-1)/2*Math.exp(-exponent));
      return {approxProbability:approx,securityModel:'independent uniform random identifiers'};
    },
    cryptographicOverhead(messages,payloadBytes,tagBytes) {
      integer(messages,0,1000000);integer(payloadBytes,0,10000000);integer(tagBytes,0,256);
      const data=messages*payloadBytes, overhead=messages*tagBytes;
      return {payloadBytes:data,tagBytes:overhead,totalBytes:data+overhead,overheadFraction:!data&&!overhead?null:overhead/(data+overhead)};
    },
    permissionMatrix(accounts,objects,actions,allowRatio) {
      integer(accounts,1,100);integer(objects,1,100);integer(actions,1,50);finite(allowRatio,0,1);
      const total=accounts*objects*actions;
      return {total,estimatedAllowed:Math.floor(total*allowRatio),estimatedDenied:total-Math.floor(total*allowRatio)};
    },
    memoryBounds(start,size,requestStart,requestLength) {
      [start,size,requestStart,requestLength].forEach((x,i)=>integer(x,0,100000000,['start','size','requestStart','requestLength'][i]));
      return {inBounds:requestStart>=start && requestStart+requestLength<=start+size,regionEnd:start+size};
    },
    throughput(capacity, legitimate, noisy, rejected) {
      [capacity, legitimate, noisy, rejected].forEach((v,i) => finite(v,0,10000,['capacity','legitimate','noisy','rejected'][i]));
      if(capacity<=0 || rejected>noisy) throw new RangeError('Capacity must be positive; rejected cannot exceed noisy traffic');
      const offered=legitimate+noisy, admitted=offered-rejected;
      return {before:offered,after:admitted,headroom:capacity-admitted,utilization:admitted/capacity,overloaded:admitted>capacity};
    },
    reachability(edges, start) {
      integer(start,0,7,'start');
      if (!Array.isArray(edges) || edges.length>64) throw new RangeError('Bounded edge list required');
      const adjacency=Array.from({length:8},()=>[]);
      for(const e of edges) {if(!Array.isArray(e)||e.length!==2)throw new TypeError('Expected [source,target]');integer(e[0],0,7);integer(e[1],0,7);adjacency[e[0]].push(e[1]);}
      const visited=new Set([start]),queue=[start];
      while(queue.length) for(const v of adjacency[queue.shift()]) if(!visited.has(v)){visited.add(v);queue.push(v);}
      return [...visited].sort((a,b)=>a-b);
    },
    authorization(principals,resources,actions,allowed) {
      integer(principals,1,100);integer(resources,1,100);integer(actions,1,50);integer(allowed,0,principals*resources*actions);
      const total=principals*resources*actions;
      return {total,allowed,denied:total-allowed,allowFraction:allowed/total};
    },
    idleExpiry(created, idleMinutes, maxMinutes, requestTimes) {
      finite(created,0,1440);integer(idleMinutes,1,240);integer(maxMinutes,1,1440);
      if(!Array.isArray(requestTimes)||requestTimes.length>50)throw new RangeError('Too many requests');
      let last=created,deadline=created+idleMinutes;
      const absolute=created+maxMinutes,success=[];
      for(const t of requestTimes) {finite(t,created,2880); if(t<last)throw new RangeError('Requests must be ordered');
        const accepted=t<=deadline && t<=absolute;success.push(accepted); if(accepted)deadline=Math.min(absolute,t+idleMinutes);last=t;
      }
      return {accepted:success,deadline:Math.min(deadline,absolute),absolute};
    },
    rewrap(keys,msPerKey,workers) {
      integer(keys,0,1000000);finite(msPerKey,0.01,1000);integer(workers,1,256);
      return {serialSeconds:keys*msPerKey/1000,idealSeconds:Math.ceil(keys/workers)*msPerKey/1000};
    },
    privacyCell(groupSize,reportedCount,threshold) {
      integer(groupSize,0,100000);integer(reportedCount,0,groupSize);integer(threshold,2,1000);
      const small=groupSize<threshold || reportedCount<threshold || (groupSize-reportedCount)<threshold;
      return {groupSize,reportedCount,threshold,small,release:!small,warning:small?'Flag small reported or complementary cells for suppression review':'Still assess auxiliary information and repeated releases'};
    },
    alerts(total,prevalence,sensitivity,falsePositiveRate) {
      integer(total,1,1000000);[prevalence,sensitivity,falsePositiveRate].forEach((v,i)=>finite(v,0,1,['prevalence','sensitivity','falsePositiveRate'][i]));
      const bad=total*prevalence,good=total-bad,TP=bad*sensitivity,FN=bad-TP,FP=good*falsePositiveRate,TN=good-FP;
      return {TP,FN,FP,TN,alerts:TP+FP,precision:TP+FP===0?null:TP/(TP+FP),recall:bad===0?null:TP/bad};
    },
    recovery(lastPoint,incidentTime,recoveryStart,duration,rpo,rto) {
      [lastPoint,incidentTime,recoveryStart,duration,rpo,rto].forEach((v,i)=>finite(v,0,100000,['lastPoint','incidentTime','recoveryStart','duration','rpo','rto'][i]));
      if(lastPoint>incidentTime || recoveryStart<incidentTime)throw new RangeError('Inconsistent timeline');
      const lost=incidentTime-lastPoint, elapsed=recoveryStart+duration-incidentTime;
      return {lost,elapsed,finish:recoveryStart+duration,rpoPass:lost<=rpo,rtoPass:elapsed<=rto};
    },
    transitions(states,permitted) {
      integer(states,1,100);integer(permitted,0,states*states);
      return {possible:states*states,permitted,denied:states*states-permitted};
    },
    coverage(requirements,tested) {
      integer(requirements,1,10000);integer(tested,0,requirements);
      return {tested,untested:requirements-tested,fraction:tested/requirements};
    }
  };
  const configs={
    'sec-exposure':{title:'Asset exposure model',description:'Synthetic inventory fraction; exposure is not a compromise probability.',parameters:[['assets','Assets',100,1,1000],['exposed','Exposed assets',20,0,100],['factor','Illustrative affected fraction',0.2,0,1,0.1]],run:p=>computations.exposureRate(p.assets,p.exposed,p.factor),display:r=>`Exposure: ${(r.exposedFraction*100).toFixed(1)}% of inventory; modeled affected assets: ${r.estimatedAffected.toFixed(1)}. No prediction is implied.`},
    'sec-risk':{title:'Expected-loss sensitivity model',description:'Hypothetical probability and consequences; numbers are not measured forecasts.',parameters:[['probability','Event probability',0.1,0,1,0.05],['impact','Impact units',1000,0,10000,100],['effectiveness','Assumed control effectiveness',0.5,0,1,0.05]],run:p=>computations.riskReduction(p.probability,p.impact,p.effectiveness),display:r=>`Baseline modeled loss ${r.baselineExpectedLoss.toFixed(2)}; residual modeled loss ${r.residualExpectedLoss.toFixed(2)}.`},
    'crypto-nonce':{title:'Random identifier collision',description:'Birthday approximation under uniform independent draws; NOT replay protection.',parameters:[['bits','Random bits',96,32,128,32],['draws','Identifiers generated',100000,0,1000000,10000]],run:p=>computations.nonceCollision(p.bits,p.draws),display:r=>`Approximate collision probability: ${r.approxProbability.toExponential(4)}. Replay rejection still needs state.`},
    'crypto-overhead':{title:'Authenticated-encryption tag overhead',description:'Simplified framing overhead only; excludes headers and implementation overhead.',parameters:[['messages','Messages',1000,0,10000],['payloadBytes','Payload bytes/message',1024,0,8192],['tagBytes','Tag bytes/message',16,0,64]],run:p=>computations.cryptographicOverhead(p.messages,p.payloadBytes,p.tagBytes),display:r=>`Payload ${r.payloadBytes.toLocaleString()} bytes; tags ${r.tagBytes.toLocaleString()} bytes; share ${r.overheadFraction===null?'undefined':(r.overheadFraction*100).toFixed(2)+'%'}.`},
    'systems-grants':{title:'Effective permission counts',description:'Synthetic access matrix size, not an access-control proof.',parameters:[['accounts','Accounts',10,1,100],['objects','Objects',20,1,100],['actions','Actions',2,1,10],['allowRatio','Fraction of permitted operations',0.1,0,1,0.05]],run:p=>computations.permissionMatrix(p.accounts,p.objects,p.actions,p.allowRatio),display:r=>`Potential requests ${r.total}; estimated allowed ${r.estimatedAllowed}; denied ${r.estimatedDenied}.`},
    'systems-memory':{title:'Memory range validation',description:'Checks a synthetic region; no operating-system memory access.',parameters:[['start','Region start',100,0,1000],['size','Region length',200,0,500],['requestStart','Request start',150,0,1500],['requestLength','Request length',100,0,400]],run:p=>computations.memoryBounds(p.start,p.size,p.requestStart,p.requestLength),display:r=>`Request is ${r.inBounds?'inside':'outside'} the configured region ending at ${r.regionEnd}.`},
    throughput:{title:'Defensive capacity model', description:'Average-rate only. Not a latency guarantee.',parameters:[['capacity','Sustainable requests/s',240,10,500],['legitimate','Legitimate requests/s',150,0,500],['noisy','Extra requests/s',110,0,500],['rejected','Rejected extra requests/s',50,0,500]],display:r=>`Demand before: ${r.before.toFixed(1)}/s; after: ${r.after.toFixed(1)}/s. Headroom: ${r.headroom.toFixed(1)}/s. ${r.overloaded?'Overloaded':'Within average capacity'}.`},
    reachability:{title:'Network zone reachability',description:'Synthetic directed edges only; no network traffic is generated.',parameters:[['direct','Allow public-to-database edge',0,0,1]],run:p=>({nodes:computations.reachability([[0,1],[1,2],[3,1],...(p.direct?[[0,2]]:[])],0),direct:Boolean(p.direct)}),display:r=>`Reachable nodes from public: ${r.nodes.join(', ')} (0 public, 1 API, 2 database). Direct public-to-database edge: ${r.direct?'YES — extra exposure':'NO — only mediated path'}. Connectivity does not imply authorization.`},
    authorization:{title:'Authorization matrix',description:'Counts possible and denied requests, not system security.',parameters:[['principals','Principals',3,1,12],['resources','Resources',2,1,12],['actions','Actions',2,1,6],['allowed','Allowed combinations',6,0,12]],display:r=>`Total: ${r.total}; allowed: ${r.allowed}; denied: ${r.denied}. Check that real rules match this simplified matrix.`},
    idleExpiry:{title:'Session expiry',description:'Synthetic relative minutes from login with fixed timeout policy.',parameters:[['created','Login minute',0,0,300],['idleMinutes','Idle timeout (minutes)',20,1,120],['maxMinutes','Absolute maximum (minutes)',480,30,600],['requestTime','Next request at minute',25,0,600]],run:p=>computations.idleExpiry(p.created,p.idleMinutes,p.maxMinutes,[p.requestTime]),display:r=>`Request ${r.accepted[0]?'accepted':'rejected'}; idle deadline minute ${r.deadline}; absolute deadline ${r.absolute}.`},
    rewrap:{title:'Encryption key rewrap estimate',description:'Ideal worker scheduling; excludes storage and provider latency.',parameters:[['keys','Key count',120000,0,200000],['msPerKey','Processing ms/key',2,1,20],['workers','Parallel workers',20,1,64]],display:r=>`Serial processing: ${r.serialSeconds.toFixed(2)}s; idealized concurrent lower bound: ${r.idealSeconds.toFixed(2)}s.`},
    privacyCell:{title:'Small-cell publication risk',description:'Checks small reported and complementary cells; suppression heuristic, not a proof of anonymity.',parameters:[['groupSize','Group size',3,0,50],['reportedCount','Reported count',3,0,50],['threshold','Small-cell threshold',5,2,15]],display:r=>`Group ${r.groupSize}, reported ${r.reportedCount}, threshold ${r.threshold}. ${r.release?'Not automatically suppressed':'Flag for suppression'}. ${r.warning}.`},
    alerts:{title:'Detection confusion matrix',description:'Expected values can be fractional; inputs are synthetic rates.',parameters:[['total','Sessions/day',100000,100,200000],['prevalence','Malicious fraction',0.001,0,0.05,0.001],['sensitivity','True-positive rate',0.9,0,1,0.05],['falsePositiveRate','False-positive rate',0.02,0,0.3,0.01]],display:r=>`Expected TP ${r.TP.toFixed(1)}, FP ${r.FP.toFixed(1)}, FN ${r.FN.toFixed(1)}; precision ${r.precision===null?'undefined':(r.precision*100).toFixed(2)+'%'}.`},
    recovery:{title:'Backup recovery objectives',description:'Times expressed in minutes from start of a fictional day.',parameters:[['lastPoint','Last backup minute',840,0,1400],['incidentTime','Detection minute',910,0,1400],['recoveryStart','Restore start minute',920,0,1400],['duration','Restore duration',70,0,500],['rpo','RPO (minutes)',120,0,400],['rto','RTO (minutes)',90,0,400]],display:r=>`Possible data-loss window ${r.lost}m (${r.rpoPass?'RPO pass':'RPO fail'}); recovery ${r.elapsed}m (${r.rtoPass?'RTO pass':'RTO fail'}).`},
    transitions:{title:'Workflow state-transition matrix',description:'Count of edges in a bounded transition model.',parameters:[['states','States',4,1,10],['permitted','Permitted directed transitions',4,0,16]],display:r=>`${r.possible} possible pairs, ${r.permitted} permitted, ${r.denied} denied. Actor permissions still require separate checks.`},
    coverage:{title:'Assurance evidence coverage',description:'Tested requirements are NOT the percentage of system security.',parameters:[['requirements','Defined requirements',10,1,50],['tested','Requirements with tests',7,0,50]],display:r=>`${(r.fraction*100).toFixed(1)}% of defined requirements have tests; ${r.untested} remain without test evidence.`}
  };
  // Ensure invalid combinations are rejected, not silently misreported as results.
  function run(name,p) {
    if(!Object.prototype.hasOwnProperty.call(configs,name))throw Error('Unknown model');
    const f=configs[name].run||((x)=>computations[name](...configs[name].parameters.map(q=>x[q[0]])));
    return f(p);
  }
  function mount(el,name) {
    if(!el)throw Error('Missing mount'); const c=configs[name];if(!c)throw Error('Unknown model');
    el.textContent='';const header=document.createElement('h3');header.textContent=c.title;el.appendChild(header);
    const note=document.createElement('p');note.textContent=c.description;el.appendChild(note);
    const fields={},initial={}; const form=document.createElement('form');form.noValidate=true;
    for(const [id,label,def,min,max,step] of c.parameters){
      const row=document.createElement('label');row.textContent=label+' ';const input=document.createElement('input');
      input.type='range';input.min=String(min);input.max=String(max);input.step=String(step||1);input.value=String(def);input.setAttribute('aria-label',label);
      const out=document.createElement('output');out.textContent=String(def);input.addEventListener('input',()=>{out.textContent=input.value;calculate();});
      row.appendChild(input);row.appendChild(out);form.appendChild(row);fields[id]=input;initial[id]=def;
    }
    const reset=document.createElement('button');reset.type='button';reset.textContent='Reset';reset.addEventListener('click',()=>{for(const [id,def] of Object.entries(initial)){fields[id].value=String(def);fields[id].dispatchEvent(new Event('input'));}});form.appendChild(reset);
    const result=document.createElement('p');result.setAttribute('role','status');result.setAttribute('aria-live','polite');el.appendChild(form);el.appendChild(result);
    function calculate(){try{const p={};for(const [id,input] of Object.entries(fields))p[id]=Number(input.value); result.textContent=c.display(run(name,p)); result.dataset.valid='true';}
      catch(e){result.textContent='Check input: '+e.message; result.dataset.valid='false';}}
    calculate();return {calculate,fields,result};
  }
  root.OpenSTEMSecurityModels={computations,configs,run,mount};
})(typeof window!=='undefined'?window:globalThis);

/* SimulationEngine adapter for Information Security */
(function(root){
  if (typeof document !== 'undefined') {
    var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
    root.SimulationEngine = root.SimulationEngine || {};
    root.SimulationEngine.initSimulation = function(containerId, simType) {
      var el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
      if (root.OpenSTEMSecurityModels && root.OpenSTEMSecurityModels.configs && root.OpenSTEMSecurityModels.configs[simType]) {
        return root.OpenSTEMSecurityModels.mount(el, simType);
      }
      if (typeof previous === 'function') {
        return previous.call(this, containerId, simType);
      }
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
