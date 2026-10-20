/* Demography and Population Statistics interactive teaching models and Canvas/SVG visualizers. */
(function(root){
  'use strict';
  const doc = typeof document !== 'undefined' ? document : null;
  if(!doc) return;

  function range(v, a, b, name){
    if(!Number.isFinite(v) || v < a || v > b) throw Error(name + ' must be between ' + a + ' and ' + b + '.');
    return v;
  }
  function integer(v, a, b, name){
    range(v, a, b, name);
    if(!Number.isInteger(v)) throw Error(name + ' must be an integer.');
    return v;
  }

  // --- SVG UI & Rendering Helpers ---
  function field(id, label, val, min, max, step){
    return `<label class="prob-control" for="${id}"><span>${label}</span><input type="number" id="${id}" value="${val}" min="${min}" max="${max}" step="${step}"/></label>`;
  }
  function select(id, label, options){
    const opts = options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('');
    return `<label class="prob-control" for="${id}"><span>${label}</span><select id="${id}">${opts}</select></label>`;
  }
  function summary(vals){
    return '<div class="prob-summary">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(3)) : 'NaN';
  }

  function chart(seriesList, xMin, xMax, titleStr, vRef = null, hRef = null){
    const W = 620, H = 240, padL = 50, padR = 25, padT = 25, padB = 35;
    const plotW = W - padL - padR, plotH = H - padT - padB;

    let yMax = 0, yMin = 0;
    seriesList.forEach(s => {
      s.values.forEach(([x, y]) => {
        if(Number.isFinite(y)){
          if(y > yMax) yMax = y;
          if(y < yMin) yMin = y;
        }
      });
    });
    if(yMax <= yMin) yMax = yMin + 1;
    const ySpan = yMax - yMin;
    const yDispMax = yMax + 0.1 * ySpan;
    const yDispMin = yMin >= 0 ? 0 : yMin - 0.1 * ySpan;

    const px = (x) => padL + ((x - xMin) / (xMax - xMin)) * plotW;
    const py = (y) => padT + plotH - ((y - yDispMin) / (yDispMax - yDispMin)) * plotH;

    let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${titleStr}" class="prob-chart"><title>${titleStr}</title>`;
    svg += `<rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15, 23, 42, 0.45)" rx="4"/>`;

    // Horizontal grid lines
    for(let i = 0; i <= 4; i++){
      const yVal = yDispMin + ((yDispMax - yDispMin) / 4) * i;
      const yPos = py(yVal);
      svg += `<line x1="${padL}" y1="${yPos}" x2="${padL + plotW}" y2="${yPos}" stroke="rgba(148, 163, 184, 0.15)" stroke-width="1"/>`;
      svg += `<text x="${padL - 8}" y="${yPos + 4}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yVal)}</text>`;
    }

    // Horizontal axis labels
    for(let i = 0; i <= 5; i++){
      const xVal = xMin + ((xMax - xMin) / 5) * i;
      const xPos = px(xVal);
      svg += `<line x1="${xPos}" y1="${padT}" x2="${xPos}" y2="${padT + plotH}" stroke="rgba(148, 163, 184, 0.12)" stroke-width="1"/>`;
      svg += `<text x="${xPos}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xVal)}</text>`;
    }

    // Render series
    seriesList.forEach(s => {
      const d = s.values.map(([x, y], i) => (i === 0 ? 'M' : 'L') + px(x).toFixed(1) + ' ' + py(y).toFixed(1)).join(' ');
      const strokeColor = s.color || (s.dashed ? '#fbbf24' : '#38bdf8');
      const dashArr = s.dashed ? 'stroke-dasharray="4 3"' : (s.dotted ? 'stroke-dasharray="2 2"' : '');
      svg += `<path d="${d}" fill="none" stroke="${strokeColor}" stroke-width="${s.width || 2}" ${dashArr}/>`;
    });

    if(vRef !== null && Number.isFinite(vRef)){
      const rx = px(vRef);
      if(rx >= padL && rx <= padL + plotW){
        svg += `<line x1="${rx}" y1="${padT}" x2="${rx}" y2="${padT + plotH}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>`;
        svg += `<text x="${rx + 4}" y="${padT + 14}" fill="#f43f5e" font-size="11">Inflection: ${fmt(vRef)}</text>`;
      }
    }

    svg += `</svg>`;
    return svg;
  }

  // --- Specialized Population Pyramid Renderer ---
  function renderPyramidSvg(ageLabels, malePcts, femalePcts, titleStr){
    const W = 620, H = 260, padL = 45, padR = 45, padT = 25, padB = 25;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const midX = padL + plotW / 2;
    const halfW = plotW / 2 - 20;

    let maxPct = 0;
    for(let i = 0; i < malePcts.length; i++){
      if(malePcts[i] > maxPct) maxPct = malePcts[i];
      if(femalePcts[i] > maxPct) maxPct = femalePcts[i];
    }
    maxPct = Math.max(6, Math.ceil(maxPct * 1.15));

    let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${titleStr}" class="prob-chart"><title>${titleStr}</title>`;
    svg += `<rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15, 23, 42, 0.45)" rx="4"/>`;

    // Center divider
    svg += `<line x1="${midX}" y1="${padT}" x2="${midX}" y2="${padT + plotH}" stroke="#64748b" stroke-width="1.5"/>`;

    // Column labels
    svg += `<text x="${midX - 35}" y="${padT + 14}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="end">◄ Males (%)</text>`;
    svg += `<text x="${midX + 35}" y="${padT + 14}" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="start">Females (%) ►</text>`;

    const nRows = ageLabels.length;
    const rowH = Math.max(3, (plotH - 25) / nRows);

    for(let i = 0; i < nRows; i++){
      // Invert row index so youngest (0-4) is at the bottom
      const y = padT + plotH - (i + 1) * rowH;
      const bH = rowH * 0.85;

      const mBarW = (malePcts[i] / maxPct) * halfW;
      const fBarW = (femalePcts[i] / maxPct) * halfW;

      // Male bar (extends left from center)
      svg += `<rect x="${midX - 15 - mBarW}" y="${y}" width="${mBarW}" height="${bH}" fill="rgba(56, 189, 248, 0.75)" rx="1"/>`;
      // Female bar (extends right from center)
      svg += `<rect x="${midX + 15}" y="${y}" width="${fBarW}" height="${bH}" fill="rgba(244, 114, 182, 0.75)" rx="1"/>`;

      // Age label in center
      if(i % 2 === 0 || i === nRows - 1){
        svg += `<text x="${midX}" y="${y + bH * 0.8}" fill="#94a3b8" font-size="9" text-anchor="middle">${ageLabels[i]}</text>`;
      }
    }

    svg += `</svg>`;
    return svg;
  }

  // --- Demographic Simulation Models ---
  function pyramidModel(stage, srb){
    range(srb, 100, 115, 'srb');
    const ageLabels = ['0–4', '5–9', '10–14', '15–19', '20–24', '25–29', '30–34', '35–39', '40–44', '45–49', '50–54', '55–59', '60–64', '65–69', '70–74', '75+'];
    const pMale = srb / (srb + 100.0);
    const pFem = 1.0 - pMale;

    let baseDist = [];
    if(stage === 'expansive'){
      // Stage 1/2: High fertility, young base
      baseDist = [14.0, 13.0, 12.0, 10.5, 9.5, 8.5, 7.5, 6.0, 5.0, 4.0, 3.2, 2.5, 1.8, 1.2, 0.8, 0.5];
    } else if(stage === 'dividend'){
      // Stage 3: Low child fertility, bulge in working ages 20-40
      baseDist = [7.0, 7.2, 7.5, 8.2, 9.5, 9.8, 9.4, 8.5, 7.5, 6.5, 5.5, 4.5, 3.8, 2.8, 1.6, 1.2];
    } else if(stage === 'stationary'){
      // Stage 4: Balanced rectangular
      baseDist = [5.8, 5.9, 6.0, 6.1, 6.3, 6.5, 6.7, 6.8, 6.7, 6.5, 6.2, 5.8, 5.2, 4.5, 3.5, 3.5];
    } else {
      // Stage 5: Constrictive / severe aging (urn shape)
      baseDist = [3.5, 3.8, 4.2, 4.8, 5.5, 6.0, 6.5, 7.0, 7.5, 7.8, 8.0, 8.2, 7.5, 6.5, 5.5, 6.7];
    }

    const sumBase = baseDist.reduce((a, b) => a + b, 0);
    const malePcts = [], femalePcts = [];
    let childPop = 0, workPop = 0, agedPop = 0;

    for(let i = 0; i < baseDist.length; i++){
      const pct = (baseDist[i] / sumBase) * 100.0;
      // Sex differential mortality factor
      const maleSurvivalFactor = Math.max(0.65, 1.0 - i * 0.022);
      const mVal = pct * pMale * 2.0 * maleSurvivalFactor;
      const fVal = pct * pFem * 2.0;
      malePcts.push(mVal / 2.0);
      femalePcts.push(fVal / 2.0);

      const totGroup = (mVal + fVal) / 2.0;
      if(i <= 2) childPop += totGroup; // 0-14
      else if(i <= 12) workPop += totGroup; // 15-64
      else agedPop += totGroup; // 65+
    }

    const cdr = (childPop / workPop) * 100.0;
    const odr = (agedPop / workPop) * 100.0;
    const tdr = cdr + odr;

    return {
      stage, srb, ageLabels, malePcts, femalePcts,
      childPct: childPop,
      workPct: workPop,
      agedPct: agedPop,
      cdr, odr, tdr
    };
  }

  function lifeTableCurveModel(e0, family){
    range(e0, 40, 90, 'e0');
    // Gompertz-Makeham parameter scaling to match e0
    // mu(x) = A + B * c^x
    const c = 1.095;
    const B = 0.00035 * Math.pow(0.95, e0 - 50);
    const A = family === 'north' ? 0.0005 : (family === 'south' ? 0.0020 : 0.0010);
    const q0 = Math.max(0.003, Math.min(0.12, 0.08 - (e0 - 50) * 0.0018));

    const lCurve = [];
    let lx = 100000;
    let t0 = 0;
    for(let x = 0; x <= 95; x++){
      lCurve.push([x, lx]);
      t0 += lx;
      let qx = 0;
      if(x === 0){
        qx = q0;
      } else {
        const hazard = A + B * Math.pow(c, x);
        qx = 1.0 - Math.exp(-hazard);
      }
      lx = Math.max(0, lx * (1.0 - qx));
    }

    const l65 = lCurve[65] ? lCurve[65][1] : 0;
    const prob65 = (l65 / 100000.0) * 100.0;
    const entropy = Math.max(0.12, Math.min(0.75, 0.65 - (e0 - 50) * 0.012));

    return {
      e0, family, q0: q0 * 1000,
      prob65,
      entropy,
      lCurve
    };
  }

  function growthModelSim(mtype, rPct, K, P0){
    range(rPct, 0.5, 5.0, 'rPct');
    range(K, 50, 1000, 'K');
    range(P0, 5, K, 'P0');
    const r = rPct / 100.0;
    const beta = (K - P0) / P0;

    const curve = [];
    let tInflect = null, maxVelocity = null;
    if(mtype === 'logistic'){
      tInflect = beta > 0 ? Math.log(beta) / r : 0;
      maxVelocity = (r * K) / 4.0;
      for(let t = 0; t <= 100; t += 2){
        const pt = K / (1.0 + beta * Math.exp(-r * t));
        curve.push([t, pt]);
      }
    } else {
      // Exponential
      for(let t = 0; t <= 100; t += 2){
        const pt = P0 * Math.exp(r * t);
        if(pt <= K * 2.5) curve.push([t, pt]);
      }
    }

    const doublingTime = Math.log(2) / r;

    return {
      mtype, rPct, K, P0,
      tInflect, maxVelocity, doublingTime,
      curve
    };
  }

  function lotkaStableModel(rPct, T){
    range(rPct, -1.5, 3.5, 'rPct');
    range(T, 25, 33, 'T');
    const r = rPct / 100.0;

    // Synthetic Gompertz survival p(x)
    const curve = [];
    let sumWeight = 0;
    const pxList = [];
    for(let x = 0; x <= 90; x++){
      const px = Math.exp(-0.0005 * x - 0.00004 * Math.pow(1.09, x));
      pxList.push(px);
      const w = Math.exp(-r * x) * px;
      sumWeight += w;
    }

    const b = 1.0 / sumWeight;
    const d = b - r;

    let youthPct = 0, agedPct = 0;
    for(let x = 0; x <= 90; x++){
      const cx = b * Math.exp(-r * x) * pxList[x];
      curve.push([x, cx * 100.0]);
      if(x < 15) youthPct += cx * 100.0;
      if(x >= 65) agedPct += cx * 100.0;
    }

    return {
      rPct, T,
      b: b * 1000.0,
      d: d * 1000.0,
      youthPct, agedPct,
      nrr: Math.exp(r * T),
      curve
    };
  }

  function initSimulation(containerId, type){
    const el = doc.getElementById(containerId);
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    let title = '', note = '', controls = '';
    const f = (key, label, value, min, max, step) => field(containerId + '-' + key, label, value, min, max, step);
    const s = (key, label, options) => select(containerId + '-' + key, label, options);

    if(type === 'demo-pyramid-explorer'){
      title = 'Population Pyramid & Demographic Dividend Explorer';
      note = 'Simulates age-sex structural profiles across the Five Stages of Demographic Transition and calculates Child, Old-Age, and Total Dependency Ratios.';
      controls = s('stage', 'Demographic Stage', [
        ['expansive', 'Stage 1/2: Expansive (High Fertility, Youth Bulge)'],
        ['dividend', 'Stage 3: Demographic Dividend (Working-Age Surge)'],
        ['stationary', 'Stage 4: Stationary (Replacement Balance)'],
        ['constrictive', 'Stage 5: Constrictive (Sub-Replacement Aging)']
      ]) + f('srb', 'Sex Ratio at Birth (M per 100 F)', 105, 100, 115, 1);
    }
    if(type === 'demo-lifetable-curves'){
      title = 'Life Table Survival Curve (lx) & Rectangularization Modeler';
      note = 'Models cohort survival from age 0 to 95 and illustrates how advancing life expectancy induces rectangularization and compression of mortality.';
      controls = f('e0', 'Life Expectancy at Birth (e₀)', 72, 45, 88, 1)
        + s('family', 'Coale-Demeny Pattern', [
          ['west', 'West Family (Standard Global)'],
          ['north', 'North Family (Low Infant, High Adult)'],
          ['south', 'South Family (High Child 1-4 Hazard)']
        ]);
    }
    if(type === 'demo-growth-models'){
      title = 'Verhulst Logistic vs Malthusian Exponential Growth Modeler';
      note = 'Compares unconstrained exponential growth against the density-dependent Verhulst logistic model, identifying the inflection point at half carrying capacity.';
      controls = s('mtype', 'Growth Model', [
        ['logistic', 'Verhulst-Pearl Logistic Model'],
        ['exponential', 'Malthusian Exponential Growth']
      ]) + f('rPct', 'Annual Growth Rate (%)', 2.5, 0.5, 4.5, 0.25)
        + f('K', 'Carrying Capacity K (k)', 300, 100, 600, 50)
        + f('P0', 'Initial Population P₀ (k)', 30, 10, 150, 10);
    }
    if(type === 'demo-lotka-stable-age'){
      title = 'Lotka Stable Age Distribution Engine';
      note = 'Solves the continuous stable population distribution c(x) = b e^(-rx) l(x) and demonstrates how positive growth tilts the distribution toward youth while negative growth drives aging.';
      controls = f('rPct', 'Intrinsic Growth Rate r (%)', 1.5, -1.0, 3.0, 0.25)
        + f('T', 'Mean Generation Length T (yrs)', 28.5, 25.0, 32.0, 0.5);
    }

    el.innerHTML = `
      <div class="prob-header">
        <div>
          <h3 class="prob-title">${title}</h3>
          <p class="prob-note">${note}</p>
        </div>
        <button type="button" class="prob-reset" data-reset>Reset</button>
      </div>
      <div class="prob-controls">${controls}</div>
      <div class="prob-result" data-result></div>
    `;

    const inputs = el.querySelectorAll('input, select');
    const result = el.querySelector('[data-result]');
    const initial = Array.from(inputs).map(inp => inp.value);

    function get(k){
      const target = el.querySelector('#' + containerId + '-' + k);
      if(!target) return null;
      return target.tagName === 'SELECT' ? target.value : parseFloat(target.value);
    }

    function render(){
      try{
        let values = {}, plot = '';
        if(type === 'demo-pyramid-explorer'){
          const stage = get('stage'), srb = get('srb');
          const m = pyramidModel(stage, srb);
          values = {
            'Demographic Stage': stage.toUpperCase(),
            'Sex Ratio at Birth': fmt(m.srb),
            'Child Share (0–14)': fmt(m.childPct) + '%',
            'Working-Age Share (15–64)': fmt(m.workPct) + '%',
            'Elderly Share (65+)': fmt(m.agedPct) + '%',
            'Child Dependency (CDR)': fmt(m.cdr) + ' / 100 workers',
            'Old-Age Dependency (ODR)': fmt(m.odr) + ' / 100 workers',
            'Total Dependency (TDR)': fmt(m.tdr) + ' / 100 workers'
          };
          plot = renderPyramidSvg(m.ageLabels, m.malePcts, m.femalePcts, 'Population Age-Sex Pyramid');
        }
        if(type === 'demo-lifetable-curves'){
          const e0 = get('e0'), family = get('family');
          const m = lifeTableCurveModel(e0, family);
          values = {
            'Target Life Expectancy e₀': fmt(m.e0) + ' years',
            'Model Family': m.family.toUpperCase(),
            'Infant Mortality Rate (q₀)': fmt(m.q0) + ' per 1,000',
            'Survival to Age 65 (l₆₅ / l₀)': fmt(m.prob65) + '%',
            'Keyfitz Entropy Parameter H': fmt(m.entropy)
          };
          plot = chart([
            { values: m.lCurve, width: 2.5, color: '#38bdf8' }
          ], 0, 95, 'Cohort Survival Schedule l(x) (Radix = 100,000)');
        }
        if(type === 'demo-growth-models'){
          const mtype = get('mtype'), rPct = get('rPct'), K = get('K'), P0 = get('P0');
          const m = growthModelSim(mtype, rPct, K, P0);
          values = {
            'Model Type': mtype.toUpperCase(),
            'Annual Growth Rate': fmt(m.rPct) + '%',
            'Initial Population P₀': fmt(m.P0) + 'k',
            'Carrying Capacity K': fmt(m.K) + 'k',
            'Doubling Time T_d': fmt(m.doublingTime) + ' years'
          };
          if(m.tInflect !== null){
            values['Inflection Time t*'] = fmt(m.tInflect) + ' years';
            values['Peak Velocity (dP/dt)_max'] = fmt(m.maxVelocity) + 'k / yr';
          }
          plot = chart([
            { values: m.curve, width: 2.5, color: '#10b981' }
          ], 0, 100, 'Population Trajectory P(t) over 100 Years', m.tInflect);
        }
        if(type === 'demo-lotka-stable-age'){
          const rPct = get('rPct'), T = get('T');
          const m = lotkaStableModel(rPct, T);
          values = {
            'Intrinsic Rate of Increase r': fmt(m.rPct) + '%',
            'Mean Generation Length T': fmt(m.T) + ' years',
            'Implied Net Reproduction Rate (NRR)': fmt(m.nrr),
            'Intrinsic Birth Rate b': fmt(m.b) + ' per 1,000',
            'Intrinsic Death Rate d': fmt(m.d) + ' per 1,000',
            'Youth Proportion (<15)': fmt(m.youthPct) + '%',
            'Senior Proportion (65+)': fmt(m.agedPct) + '%'
          };
          plot = chart([
            { values: m.curve, width: 2.5, color: '#fbbf24' }
          ], 0, 90, 'Stable Age Density Function c(x) (%)');
        }
        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    el.querySelector('[data-reset]').addEventListener('click', () => {
      inputs.forEach((input, i) => input.value = initial[i]);
      render();
    });
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.DemographySimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
