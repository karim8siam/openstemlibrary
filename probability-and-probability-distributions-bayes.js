(function(root){
  'use strict';
  function model(weights,rates){
    if(!Array.isArray(weights)||!Array.isArray(rates)||weights.length!==3||rates.length!==3)throw Error('Supply three source weights and three flag rates.');
    if([...weights,...rates].some(x=>!Number.isFinite(x)||x<0||x>1))throw Error('Every weight and rate must be between zero and one.');
    if(Math.abs(weights.reduce((a,b)=>a+b,0)-1)>1e-12)throw Error('Source weights must sum to one.');
    const joint=weights.map((w,i)=>w*rates[i]);
    const flagProbability=joint.reduce((a,b)=>a+b,0);
    return {weights:[...weights],rates:[...rates],joint,flagProbability,posterior:flagProbability>0?joint.map(x=>x/flagProbability):null};
  }
  function sample(weights,rates,n,seed){
    const law=model(weights,rates);
    if(!Number.isInteger(n)||n<1||n>100000)throw Error('Trial count must be an integer from one to 100,000.');
    if(!Number.isInteger(seed)||seed<0||seed>4294967295)throw Error('Seed must be an unsigned 32-bit integer.');
    let state=seed>>>0;
    function random(){
      state=(state+0x6D2B79F5)>>>0;let t=state;
      t=Math.imul(t^(t>>>15),t|1);t^=t+Math.imul(t^(t>>>7),t|61);
      return ((t^(t>>>14))>>>0)/4294967296;
    }
    const sourceCounts=[0,0,0],flagCounts=[0,0,0];
    for(let trial=0;trial<n;trial++){
      const u=random();const source=u<weights[0]?0:u<weights[0]+weights[1]?1:2;
      sourceCounts[source]++;
      if(random()<rates[source])flagCounts[source]++;
    }
    const flags=flagCounts.reduce((a,b)=>a+b,0);
    return {n,seed,sourceCounts,flagCounts,flags,flagFrequency:flags/n,posteriorFrequency:flags>0?flagCounts.map(x=>x/flags):null,exact:law};
  }
  function mount(container){
    if(!container||!container.ownerDocument)throw Error('A DOM container is required.');
    const doc=container.ownerDocument;
    const prefix='prob-bayes-'+(container.id||'explorer');
    container.innerHTML='<section class="prob-bayes"><h3>Sources after a flag</h3><p>Change the source mix and conditional flag rates. The exact calculation uses every source contributing to the flagged population. Rates are invented model assumptions.</p><div class="prob-fields"></div><p class="prob-model-status" role="status" aria-live="polite"></p><div class="prob-table-scroll" tabindex="0" aria-label="Source probability table"><table><caption>Exact model values and sampled counts</caption><thead><tr><th scope="col">Source</th><th scope="col">Prior</th><th scope="col">Flag rate within source</th><th scope="col">Expected flagged count per 10,000 trials</th><th scope="col">Exact source probability given a flag</th><th scope="col">Sampled flagged count</th></tr></thead><tbody></tbody></table></div><p class="prob-draw-status" role="status" aria-live="polite">No random trials generated.</p><div class="prob-actions"><button type="button" data-draw>Generate 10,000 trials with fixed seed</button><button type="button" data-reset>Reset</button></div><p>Expected counts may be fractional. Sampled counts are integers and fluctuate around the model values. The seed is 20261013; repeating the same inputs reproduces the same trials. This explorer checks a stipulated probability model, not a real inspection process.</p></section>';
    const style=doc.createElement('style');style.textContent='.prob-bayes{font:inherit;line-height:1.6;max-width:100%}.prob-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}.prob-fields label{display:block}.prob-fields input{display:block;width:100%;box-sizing:border-box;padding:10px;font:inherit}.prob-table-scroll{max-width:100%;overflow-x:auto;margin:12px 0}.prob-bayes table{border-collapse:collapse;min-width:620px;width:100%}.prob-bayes th,.prob-bayes td{padding:8px;border:1px solid #64748b;text-align:left}.prob-actions{display:flex;flex-wrap:wrap;gap:10px}.prob-actions button{font:inherit;min-height:44px;padding:8px 14px}.prob-bayes input:focus-visible,.prob-bayes button:focus-visible,.prob-table-scroll:focus-visible{outline:3px solid #0ea5e9;outline-offset:3px}';container.append(style);
    const settings=[['weight-h','Source H prior probability',.2],['weight-m','Source M prior probability',.5],['rate-h','Flag probability within H',.08],['rate-m','Flag probability within M',.03],['rate-l','Flag probability within L',.01]];
    const fields=container.querySelector('.prob-fields'),inputs=[];
    for(const [key,label,value]of settings){const wrap=doc.createElement('div'),lab=doc.createElement('label'),input=doc.createElement('input');input.id=prefix+'-'+key;input.type='number';input.min='0';input.max='1';input.step='.01';input.value=String(value);lab.htmlFor=input.id;lab.textContent=label;wrap.append(lab,input);fields.append(wrap);inputs.push(input);}
    let observed=null;
    const status=container.querySelector('.prob-model-status'),drawStatus=container.querySelector('.prob-draw-status'),tbody=container.querySelector('tbody'),drawButton=container.querySelector('[data-draw]');
    function current(){const values=inputs.map(input=>input.value.trim()===''?NaN:Number(input.value));const remaining=1-values[0]-values[1];return model([values[0],values[1],Math.abs(remaining)<1e-12?0:remaining],values.slice(2));}
    function format(value){return value.toFixed(6).replace(/0+$/,'').replace(/\.$/,'');}
    function render(){
      tbody.replaceChildren();
      try{
        const law=current();drawButton.disabled=false;
        status.textContent='Source L prior = '+format(law.weights[2])+'. Overall flag probability = '+format(law.flagProbability)+'.'+(law.posterior?'':' A flag is impossible under these inputs; its posterior is undefined.');
        ['H','M','L'].forEach((label,i)=>{const row=doc.createElement('tr'),name=doc.createElement('th');name.scope='row';name.textContent=label;row.append(name);for(const value of [format(law.weights[i]),format(law.rates[i]),format(10000*law.joint[i]),law.posterior?format(law.posterior[i]):'Undefined',observed?String(observed.flagCounts[i]):'Not sampled']){const cell=doc.createElement('td');cell.textContent=value;row.append(cell);}tbody.append(row);});
        drawStatus.textContent=observed?'Generated '+observed.n+' trials; '+observed.flags+' flags. Sampled flag frequency = '+format(observed.flagFrequency)+'.'+(observed.posteriorFrequency?' Sampled source probabilities among flags: '+observed.posteriorFrequency.map(format).join(', ')+'.':' No sampled flags; a sampled posterior frequency is unavailable.'):'No random trials generated.';
      }catch(error){drawButton.disabled=true;status.textContent=error.message;drawStatus.textContent='Correct the inputs before generating trials.';}
    }
    inputs.forEach(input=>input.addEventListener('input',()=>{observed=null;render();}));
    drawButton.addEventListener('click',()=>{try{const law=current();observed=sample(law.weights,law.rates,10000,20261013);render();}catch(error){status.textContent=error.message;}});
    container.querySelector('[data-reset]').addEventListener('click',()=>{settings.forEach((setting,i)=>{inputs[i].value=String(setting[2]);});observed=null;render();});
    render();return {render,current};
  }
  const api={model,sample,mount};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  if(root)root.ProbabilityBayes=api;
})(typeof window!=='undefined'?window:null);
