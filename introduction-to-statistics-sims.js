/* Original, finite-data teaching explorers. Pure calculations exposed for independent checks. */
(function () {
  'use strict';
  const mean = x => x.reduce((a,b)=>a+b,0)/x.length;
  function quantile(x,p) {
    if(!x.length || !Number.isFinite(p) || p<0 || p>1 || x.some(v=>!Number.isFinite(v)))return null;
    const s=[...x].sort((a,b)=>a-b),h=(s.length-1)*p,j=Math.floor(h),g=h-j;
    return s[j]+g*((s[j+1]??s[j])-s[j]);
  }
  function summary(x) {
    if(!x.length || x.some(v=>!Number.isFinite(v)))return null;
    const n=x.length,m=mean(x),d=x.map(v=>v-m),m2=mean(d.map(v=>v*v)),m3=mean(d.map(v=>v**3)),m4=mean(d.map(v=>v**4));
    const q1=quantile(x,.25),median=quantile(x,.5),q3=quantile(x,.75),iqr=q3-q1,lo=q1-1.5*iqr,hi=q3+1.5*iqr;
    const inside=x.filter(v=>v>=lo&&v<=hi);
    return {n,mean:m,total:m*n,deviations:d,sxx:m2*n,m2,m3,m4,sampleVariance:n>1?m2*n/(n-1):null,
      sdN:Math.sqrt(m2),sampleSD:n>1?Math.sqrt(m2*n/(n-1)):null,q1,median,q3,iqr,lowerFence:lo,upperFence:hi,
      lowerWhisker:Math.min(...inside),upperWhisker:Math.max(...inside),flags:x.filter(v=>v<lo||v>hi),
      skewness:m2>0?m3/m2**1.5:null,rawKurtosis:m2>0?m4/m2**2:null,excessKurtosis:m2>0?m4/m2**2-3:null,
      cv:m>0&&n>1?Math.sqrt(m2*n/(n-1))/m:null};
  }
  function regression(x,y) {
    if(x.length!==y.length||x.length<2||[...x,...y].some(v=>!Number.isFinite(v)))return null;
    const n=x.length,mx=mean(x),my=mean(y),dx=x.map(v=>v-mx),dy=y.map(v=>v-my);
    const sxx=dx.reduce((s,v)=>s+v*v,0),syy=dy.reduce((s,v)=>s+v*v,0),sxy=dx.reduce((s,v,i)=>s+v*dy[i],0);
    const slope=sxx>0?sxy/sxx:null,intercept=slope===null?null:my-slope*mx;
    const fitted=slope===null?null:x.map(v=>intercept+slope*v),residuals=fitted?y.map((v,i)=>v-fitted[i]):null;
    const sse=residuals?residuals.reduce((s,v)=>s+v*v,0):null,ssr=slope===null?null:slope*slope*sxx;
    return {n,mx,my,sxx,syy,sxy,slope,intercept,fitted,residuals,sse,ssr,
      r:sxx>0&&syy>0?sxy/Math.sqrt(sxx*syy):null,rSquared:sxx>0&&syy>0?ssr/syy:null};
  }
  const population=[2,4,4,6,6,8,12,14,14,16,16,18];
  function sample(n,bias,seed) {
    if(!Number.isInteger(n)||n<1||n>population.length||!Number.isFinite(bias)||bias<=0)return null;
    let state=(seed>>>0)||1;
    const random=()=>{state=(Math.imul(1664525,state)+1013904223)>>>0;return(state+.5)/4294967296;};
    const entries=population.map((v,i)=>({i,v,key:-Math.log(random())/(i>=6?bias:1)}));
    return entries.sort((a,b)=>a.key-b.key).slice(0,n).sort((a,b)=>a.i-b.i);
  }
  window.StatisticsMath={mean,quantile,summary,regression,sample,population};
  const fmt=v=>v===null||!Number.isFinite(v)?'Unavailable':Number(v.toFixed(6)).toLocaleString('en-US',{maximumFractionDigits:6});
  function svg(content,label) {return `<svg viewBox="0 0 640 240" role="img" aria-label="${label}" class="stat-chart">${content}</svg>`;}
  function dotPlot(values,ref) {
    const lo=Math.min(0,...values,ref??0),hi=Math.max(1,...values,ref??0),scale=v=>45+(v-lo)/(hi-lo)*550;
    let s='<line x1="45" y1="160" x2="595" y2="160" stroke="currentColor"/>';
    const counts=new Map();
    values.forEach(v=>{const k=counts.get(v)||0;counts.set(v,k+1);s+=`<circle cx="${scale(v)}" cy="${145-k*20}" r="7" fill="#38bdf8"/>`;});
    s+=`<text x="45" y="195" fill="currentColor">${fmt(lo)}</text><text x="540" y="195" fill="currentColor">${fmt(hi)}</text>`;
    if(ref!==undefined)s+=`<line x1="${scale(ref)}" y1="35" x2="${scale(ref)}" y2="170" stroke="#fbbf24" stroke-dasharray="5 4"/><text x="45" y="25" fill="currentColor">Yellow line: mean ${fmt(ref)}</text>`;
    return svg(s,'Dot plot of the displayed data; the mean is marked when available.');
  }
  function rows(object) {return '<dl class="stat-summary">'+Object.entries(object).map(([k,v])=>`<div><dt>${k}</dt><dd>${typeof v==='string'?v:fmt(v)}</dd></div>`).join('')+'</dl>';}
  function control(id,label,value,min,max,step=1){return `<label for="${id}">${label}<input id="${id}" type="range" min="${min}" max="${max}" step="${step}" value="${value}"><output for="${id}">${value}</output></label>`;}
  function initSimulation(containerId,type) {
    const el=document.getElementById(containerId);if(!el||el.dataset.statMounted)return;
    el.dataset.statMounted='true';el.classList.add('stat-explorer');
    let controls='',title='',note='',initial=0;
    if(type==='stat-sampling'){
      title='Sampling, variation and selection preference';
      controls=control(containerId+'-n','Sample size',4,1,12)+control(containerId+'-bias','High-group selection weight (1 = equal)',1,1,10);
      note='Synthetic population: low group 2, 4, 4, 6, 6, 8; high group 12, 14, 14, 16, 16, 18. Weighted pseudorandom sampling without replacement. Draws illustrate a mechanism, not a real survey.';
    }else if(type==='stat-histogram'){
      title='Histogram area with unequal widths';initial=20;controls=control(containerId+'-value','Second bin width',initial,10,40);
      note='Fixed counts: eight in the first width-10 bin and twelve in the adjacent adjustable-width bin. Heights use count density, so areas recover counts.';
    }else{
      const settings={
        'stat-boxplot':['Type-seven quartiles and box-plot flags',30,8,60],
        'stat-location':['Mean and median sensitivity',13,8,113],
        'stat-variation':['Variance denominators and changing spread',13,8,63],
        'stat-shape':['Centred moments and distribution shape',3,0,15],
        'stat-association':['Paired association and a changing response',4,0,12],
        'stat-regression':['Least-squares line and residual checks',4,0,12]
      }[type];
      if(!settings){el.textContent='Unknown statistics explorer.';return;}
      [title,initial]=settings;controls=control(containerId+'-value','Final observation',initial,settings[2],settings[3]);
      note='Artificial finite data. The control changes one displayed observation; all summaries are recalculated using the definitions in this chapter. No causal or population claim is implied.';
    }
    el.innerHTML=`<h4>${title}</h4><p>${note}</p><div class="stat-controls">${controls}</div><div class="stat-buttons">${type==='stat-sampling'?'<button type="button" data-draw>Draw another sample</button>':''}<button type="button" data-reset>Reset</button></div><div class="stat-results" aria-live="polite"></div>`;
    const results=el.querySelector('.stat-results');let seed=42,history=[];
    function render() {
      el.querySelectorAll('input').forEach(input=>{input.nextElementSibling.textContent=input.value;});
      const inputs=[...el.querySelectorAll('input')],v=Number(inputs[0].value);
      if(inputs.some(input=>!Number.isFinite(Number(input.value))||Number(input.value)<Number(input.min)||Number(input.value)>Number(input.max))){results.textContent='Input is outside the documented range.';return;}
      if(type==='stat-sampling'){
        const bias=Number(inputs[1].value),selected=sample(v,bias,seed);if(!selected){results.textContent='Invalid sample size or weight.';return;}
        const data=selected.map(e=>e.v),m=mean(data);history.push(m);if(history.length>200)history.shift();
        results.innerHTML=rows({'Population mean':mean(population),'Sample mean':m,'Sample count':data.length,'High-group count':selected.filter(e=>e.i>=6).length,'Draws under current settings':history.length,'Running mean of displayed draws':mean(history)})+`<p>Selected unit indices: ${selected.map(e=>e.i+1).join(', ')}. Values: ${data.join(', ')}.</p>`+dotPlot(data,m);
      }else if(type==='stat-histogram'){
        const h1=.8,h2=12/v,totalWidth=10+v,sx=550/totalWidth,sy=145/Math.max(h1,h2);
        results.innerHTML=rows({'First count density':h1,'Second count density':h2,'First area':10*h1,'Second area':v*h2,'First relative density':h1/20,'Second relative density':h2/20})+svg(`<rect x="45" y="${180-h1*sy}" width="${10*sx}" height="${h1*sy}" fill="#38bdf8"/><rect x="${45+10*sx}" y="${180-h2*sy}" width="${v*sx}" height="${h2*sy}" fill="#a78bfa"/><text x="45" y="215" fill="currentColor">Widths: 10 and ${v}; areas: 8 and 12</text>`,'Two adjacent unequal-width bins with count-density heights and fixed count areas.');
      }else if(type==='stat-association'||type==='stat-regression'){
        const x=[1,2,3,4],y=[2,3,5,v],r=regression(x,y),maxY=Math.max(6,...y,...r.fitted),minY=Math.min(0,...y,...r.fitted),sx=t=>45+(t-1)/3*550,sy=t=>185-(t-minY)/(maxY-minY)*145;
        let drawing=`<line x1="${sx(1)}" y1="${sy(r.fitted[0])}" x2="${sx(4)}" y2="${sy(r.fitted[3])}" stroke="#fbbf24" stroke-width="2"/>`;
        x.forEach((a,i)=>{drawing+=`<line x1="${sx(a)}" y1="${sy(y[i])}" x2="${sx(a)}" y2="${sy(r.fitted[i])}" stroke="#94a3b8" stroke-dasharray="3 3"/><circle cx="${sx(a)}" cy="${sy(y[i])}" r="7" fill="#38bdf8"/>`;});
        drawing+='<text x="45" y="220" fill="currentColor">Blue: observed pairs; yellow: fitted line; dashed: residuals</text>';
        results.innerHTML=rows({'Pearson r':r.r,'Slope (y per x unit)':r.slope,'Intercept':r.intercept,'R-squared':r.rSquared,'SST':r.syy,'SSR':r.ssr,'SSE':r.sse,'Residual sum':r.residuals.reduce((a,b)=>a+b,0)})+`<p>Pairs: ${x.map((a,i)=>`(${a}, ${y[i]})`).join(', ')}. Residuals: ${r.residuals.map(fmt).join(', ')}.</p>`+svg(drawing,'Scatter plot with fitted line and vertical residuals for the displayed four pairs.');
      }else{
        const data=type==='stat-boxplot'?[1,2,3,4,5,6,7,v]:type==='stat-shape'?[0,0,v]:[2,4,4,7,v],s=summary(data);
        let output={'Mean':s.mean,'Median (type 7)':s.median};
        if(type==='stat-boxplot')output={'Q1 (type 7)':s.q1,'Median':s.median,'Q3 (type 7)':s.q3,'IQR':s.iqr,'Lower fence':s.lowerFence,'Upper fence':s.upperFence,'Lower whisker':s.lowerWhisker,'Upper whisker':s.upperWhisker,'Flagged values':s.flags.join(', ')||'None','Mean':s.mean};
        if(type==='stat-variation')output={'Mean':s.mean,'Squared-deviation sum':s.sxx,'Descriptive variance (n)':s.m2,'Sample variance (n−1)':s.sampleVariance,'Descriptive SD':s.sdN,'Sample SD':s.sampleSD,'Sample CV':s.cv};
        if(type==='stat-shape')output={'Mean':s.mean,'m2 (denominator n)':s.m2,'m3 (denominator n)':s.m3,'m4 (denominator n)':s.m4,'Descriptive skewness g1':s.skewness,'Raw kurtosis b2':s.rawKurtosis,'Excess kurtosis g2':s.excessKurtosis};
        let plot=dotPlot(data,s.mean);
        if(type==='stat-boxplot'){
          const scale=a=>45+a/Math.max(1,...data)*550;
          plot=svg(`<line x1="${scale(s.lowerWhisker)}" y1="100" x2="${scale(s.upperWhisker)}" y2="100" stroke="currentColor"/><rect x="${scale(s.q1)}" y="70" width="${scale(s.q3)-scale(s.q1)}" height="60" fill="#38bdf8" fill-opacity=".3" stroke="#38bdf8"/><line x1="${scale(s.median)}" y1="70" x2="${scale(s.median)}" y2="130" stroke="#fbbf24"/>${[s.lowerWhisker,s.upperWhisker].map(a=>`<line x1="${scale(a)}" y1="85" x2="${scale(a)}" y2="115" stroke="currentColor"/>`).join('')}${s.flags.map(a=>`<circle cx="${scale(a)}" cy="100" r="6" fill="#f472b6"/>`).join('')}<text x="45" y="200" fill="currentColor">Box: Q1 to Q3; yellow: median; pink: flagged observations</text>`,'Type-seven box plot; whiskers end at actual nonflagged observations.');
        }
        results.innerHTML=rows(output)+`<p>Values: ${data.join(', ')}. Centred deviations: ${s.deviations.map(fmt).join(', ')}.</p>`+plot+(s.m2===0?'<p>Standardized shape is unavailable because all observations are equal.</p>':'');
      }
    }
    el.querySelectorAll('input').forEach(input=>input.addEventListener('input',()=>{history=[];seed=42;render();}));
    el.querySelector('[data-draw]')?.addEventListener('click',()=>{seed++;render();});
    el.querySelector('[data-reset]').addEventListener('click',()=>{inputsReset();history=[];seed=42;render();});
    function inputsReset(){el.querySelectorAll('input').forEach(input=>input.value=input.defaultValue);}
    render();
  }
  window.SimulationEngine={initSimulation};
})();
