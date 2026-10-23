/* Industrial and Official Statistics interactive teaching models and SVG visualizers. */
(function(root){
  'use strict';
  const doc = typeof document !== 'undefined' ? document : null;
  if(!doc) return;

  function range(v, a, b, name){
    if(!Number.isFinite(v) || v < a || v > b) throw Error(name + ' must be between ' + a + ' and ' + b + '.');
    return v;
  }

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

    let yMax = -Infinity, yMin = Infinity;
    seriesList.forEach(s => {
      s.values.forEach(([x, y]) => {
        if(Number.isFinite(y)){
          if(y > yMax) yMax = y;
          if(y < yMin) yMin = y;
        }
      });
    });

    if(!Number.isFinite(yMax) || yMax === yMin){ yMax = 1; yMin = 0; }
    if(yMin > 0 && yMin < yMax * 0.2) yMin = 0;
    const ySpan = (yMax - yMin) || 1;
    yMax += ySpan * 0.05;
    yMin -= ySpan * 0.05;

    function toSvg(x, y){
      const sx = padL + ((x - xMin) / (xMax - xMin || 1)) * plotW;
      const sy = padT + (1 - (y - yMin) / (yMax - yMin)) * plotH;
      return [sx, sy];
    }

    let paths = '';
    seriesList.forEach(s => {
      let d = '';
      s.values.forEach(([x, y], idx) => {
        const [sx, sy] = toSvg(x, y);
        d += (idx === 0 ? `M ${sx.toFixed(1)} ${sy.toFixed(1)}` : ` L ${sx.toFixed(1)} ${sy.toFixed(1)}`);
      });
      const dash = s.dashed ? 'stroke-dasharray="4,4"' : (s.dotted ? 'stroke-dasharray="2,3"' : '');
      paths += `<path d="${d}" fill="none" stroke="${s.color || '#38bdf8'}" stroke-width="${s.width || 2}" ${dash} />`;
    });

    let extra = '';
    if(vRef !== null && Number.isFinite(vRef) && vRef >= xMin && vRef <= xMax){
      const [vx] = toSvg(vRef, yMin);
      extra += `<line x1="${vx.toFixed(1)}" y1="${padT}" x2="${vx.toFixed(1)}" y2="${padT + plotH}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />`;
    }
    if(hRef !== null && Number.isFinite(hRef) && hRef >= yMin && hRef <= yMax){
      const [, hy] = toSvg(xMin, hRef);
      extra += `<line x1="${padL}" y1="${hy.toFixed(1)}" x2="${padL + plotW}" y2="${hy.toFixed(1)}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="2,2" />`;
    }

    let grid = `<line x1="${padL}" y1="${padT + plotH}" x2="${padL + plotW}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;
    grid += `<line x1="${padL}" y1="${padT}" x2="${padL}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;

    const xMid = (xMin + xMax) / 2;
    const yMid = (yMin + yMax) / 2;
    const ticks = `
      <text x="${padL}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMin)}</text>
      <text x="${padL + plotW / 2}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMid)}</text>
      <text x="${padL + plotW}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMax)}</text>
      <text x="${padL - 8}" y="${padT + plotH}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMin)}</text>
      <text x="${padL - 8}" y="${padT + plotH / 2}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMid)}</text>
      <text x="${padL - 8}" y="${padT}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMax)}</text>
    `;

    const titleSvg = `<text x="${W / 2}" y="16" fill="#7dd3fc" text-anchor="middle" font-weight="600" font-size="12">${titleStr}</text>`;

    return `<svg class="prob-chart" viewBox="0 0 ${W} ${H}" width="100%" height="auto" aria-label="${titleStr}">${titleSvg}${grid}${extra}${paths}${ticks}</svg>`;
  }

  // --- SIMULATION 1: SHEWHART X-BAR & R CONTROL CHART WITH 3-SIGMA LIMITS ---
  function indXbarModel(mu0, sigma0, shiftDelta, nSubgroup, numSubgroups){
    range(mu0, 10, 500, 'Process Target mu0');
    range(sigma0, 0.5, 50, 'Process Standard Deviation sigma0');
    range(shiftDelta, -3.0, 3.0, 'Mean Shift in Sigmas');
    range(nSubgroup, 3, 10, 'Subgroup Size n');
    range(numSubgroups, 10, 40, 'Subgroups Count');

    // d2 factor table for unbiasing sample range R
    const d2Map = { 3: 1.693, 4: 2.059, 5: 2.326, 6: 2.534, 7: 2.704, 8: 2.847, 9: 2.970, 10: 3.078 };
    const d2 = d2Map[nSubgroup] || 2.326;

    const seXbar = sigma0 / Math.sqrt(nSubgroup);
    const uclX = mu0 + 3 * seXbar;
    const lclX = mu0 - 3 * seXbar;
    const clX = mu0;

    // Simulated deterministic trajectory with shift introduced at subgroup floor(numSubgroups / 2)
    const shiftStart = Math.floor(numSubgroups / 2);
    const xbarSeries = [];
    const uclSeries = [], lclSeries = [], clSeries = [];

    // Deterministic pseudo-random variation based on sine hashes
    let outOfControlCount = 0;
    for(let k = 1; k <= numSubgroups; k++){
      const noise = Math.sin(k * 12.9898 + 78.233) * 0.9 + Math.cos(k * 4.1414) * 0.5;
      const currentShift = k >= shiftStart ? shiftDelta * sigma0 : 0;
      const xVal = mu0 + currentShift + noise * seXbar;
      xbarSeries.push([k, xVal]);
      uclSeries.push([k, uclX]);
      lclSeries.push([k, lclX]);
      clSeries.push([k, clX]);
      if(xVal > uclX || xVal < lclX) outOfControlCount++;
    }

    // Theoretical Average Run Length (ARL)
    // Shift in units of seXbar is kShift = shiftDelta * sqrt(nSubgroup)
    const kShift = shiftDelta * Math.sqrt(nSubgroup);
    // Probability of exceeding limits: 1 - Phi(3 - kShift) + Phi(-3 - kShift)
    function normalCdf(x){
      const t = 1 / (1 + 0.2316419 * Math.abs(x));
      const d = 0.39894228 * Math.exp(-x * x / 2);
      const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
      return x > 0 ? 1 - prob : prob;
    }
    const betaRisk = normalCdf(3 - kShift) - normalCdf(-3 - kShift);
    const pDetect = 1 - betaRisk;
    const arl1 = pDetect > 1e-4 ? (1 / pDetect) : 10000;
    const arl0 = 1 / (2 * (1 - normalCdf(3))); // ~370.4

    return {
      mu0, sigma0, uclX, lclX, clX, outOfControlCount, arl0, arl1, shiftStart,
      xbarSeries, uclSeries, lclSeries, clSeries
    };
  }

  // --- SIMULATION 2: PROCESS CAPABILITY CP, CPK, CPM & DEFECT PPM ---
  function indCapabilityModel(lsl, usl, mu, sigma, targetT){
    range(lsl, 0, 1000, 'LSL');
    range(usl, lsl + 1, 2000, 'USL');
    range(mu, lsl - 20, usl + 20, 'Process Mean');
    range(sigma, 0.1, 50, 'Process Sigma');
    range(targetT, lsl, usl, 'Target T');

    const cp = (usl - lsl) / (6 * sigma);
    const cpu = (usl - mu) / (3 * sigma);
    const cpl = (mu - lsl) / (3 * sigma);
    const cpk = Math.min(cpu, cpl);

    // Taguchi Cpm: accounts for deviation of mean from target T
    const sigmaTaguchi = Math.sqrt(sigma * sigma + Math.pow(mu - targetT, 2));
    const cpm = (usl - lsl) / (6 * sigmaTaguchi);

    function normalCdf(x){
      const t = 1 / (1 + 0.2316419 * Math.abs(x));
      const d = 0.39894228 * Math.exp(-x * x / 2);
      const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
      return x > 0 ? 1 - prob : prob;
    }

    const pBelow = normalCdf((lsl - mu) / sigma);
    const pAbove = 1 - normalCdf((usl - mu) / sigma);
    const totalDefectProb = pBelow + pAbove;
    const ppm = totalDefectProb * 1e6;

    // Normal curve points
    const xMin = Math.min(lsl - 2 * sigma, mu - 4 * sigma);
    const xMax = Math.max(usl + 2 * sigma, mu + 4 * sigma);
    const pdfCurve = [];
    for(let x = xMin; x <= xMax; x += (xMax - xMin) / 80){
      const z = (x - mu) / sigma;
      const y = (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * z * z);
      pdfCurve.push([x, y]);
    }

    return {
      cp, cpk, cpu, cpl, cpm, ppm, xMin, xMax, pdfCurve
    };
  }

  // --- SIMULATION 3: CUSUM & EWMA SMALL-SHIFT PROCESS MONITORING ---
  function indCusumEwmaModel(shift, kRef, hThreshold, lambdaEwma){
    range(shift, 0.0, 3.0, 'Shift in Sigmas');
    range(kRef, 0.2, 1.5, 'CUSUM Reference k');
    range(hThreshold, 2.0, 8.0, 'CUSUM Threshold h');
    range(lambdaEwma, 0.05, 0.50, 'EWMA Weight Lambda');

    const steps = 40;
    const shiftStart = 15;
    const cusumPosSeries = [], cusumNegSeries = [];
    const ewmaSeries = [], ewmaUclSeries = [], ewmaLclSeries = [];

    let cPlus = 0, cMinus = 0;
    let zEwma = 0;
    let cusumSignalStep = null, ewmaSignalStep = null;

    for(let t = 1; t <= steps; t++){
      const mean = t >= shiftStart ? shift : 0;
      const noise = Math.sin(t * 11.234) * 0.8 + Math.cos(t * 3.456) * 0.4;
      const x = mean + noise;

      // Tabular CUSUM recursions
      cPlus = Math.max(0, cPlus + (x - kRef));
      cMinus = Math.max(0, cMinus - (x + kRef));
      cusumPosSeries.push([t, cPlus]);
      cusumNegSeries.push([t, -cMinus]);

      if(cPlus > hThreshold && cusumSignalStep === null) cusumSignalStep = t;

      // EWMA recursion
      zEwma = lambdaEwma * x + (1 - lambdaEwma) * zEwma;
      ewmaSeries.push([t, zEwma]);

      // Time-varying EWMA limits (with L = 3 sigma)
      const sigmaZ = Math.sqrt((lambdaEwma / (2 - lambdaEwma)) * (1 - Math.pow(1 - lambdaEwma, 2 * t)));
      const uclZ = 3 * sigmaZ;
      const lclZ = -3 * sigmaZ;
      ewmaUclSeries.push([t, uclZ]);
      ewmaLclSeries.push([t, lclZ]);

      if((zEwma > uclZ || zEwma < lclZ) && ewmaSignalStep === null) ewmaSignalStep = t;
    }

    return {
      cPlus, cMinus, cusumSignalStep, ewmaSignalStep,
      cusumPosSeries, cusumNegSeries, ewmaSeries, ewmaUclSeries, ewmaLclSeries
    };
  }

  // --- SIMULATION 4: ACCEPTANCE SAMPLING OC CURVE, AQL, LTPD & AOQL ---
  function indOcSamplingModel(nSample, cAccept, aqlPct, ltpdPct){
    range(nSample, 10, 500, 'Sample Size n');
    range(cAccept, 0, 10, 'Acceptance Number c');
    range(aqlPct, 0.1, 5.0, 'AQL (%)');
    range(ltpdPct, aqlPct + 0.5, 20.0, 'LTPD (%)');

    function poissonCdf(lambda, k){
      let sum = 0, term = Math.exp(-lambda);
      for(let i = 0; i <= k; i++){
        sum += term;
        term *= lambda / (i + 1);
      }
      return sum;
    }

    // Poisson approximation for Operating Characteristic: Pa(p) = sum_{d=0}^c e^(-np) (np)^d / d!
    function probAccept(p){
      return poissonCdf(nSample * p, cAccept);
    }

    const aql = aqlPct / 100;
    const ltpd = ltpdPct / 100;

    const paAql = probAccept(aql);
    const producerRiskAlpha = (1 - paAql) * 100;

    const paLtpd = probAccept(ltpd);
    const consumerRiskBeta = paLtpd * 100;

    // AOQ curve: AOQ(p) = p * Pa(p)
    // Find AOQL = max_{p} AOQ(p)
    let aoql = 0, pAtAoql = 0;
    const ocCurve = [], aoqCurve = [];
    for(let p = 0; p <= 0.15; p += 0.002){
      const pa = probAccept(p);
      ocCurve.push([p * 100, pa]);
      const aoq = p * pa * 100;
      aoqCurve.push([p * 100, aoq]);
      if(aoq > aoql){
        aoql = aoq;
        pAtAoql = p * 100;
      }
    }

    return {
      paAql, producerRiskAlpha, paLtpd, consumerRiskBeta, aoql, pAtAoql,
      ocCurve, aoqCurve
    };
  }

  function initSimulation(containerId, type){
    const el = typeof containerId === 'string' ? doc.getElementById(containerId) : containerId;
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    const simType = type || el.dataset.sim;
    let title = '', note = '', controls = '';
    const idPrefix = typeof containerId === 'string' ? containerId : (el.id || simType);
    const f = (key, label, value, min, max, step) => field(idPrefix + '-' + key, label, value, min, max, step);

    if(simType === 'ind-xbar-r-chart'){
      title = 'Shewhart X̄ Control Chart & Out-of-Control Shift Detector';
      note = 'Simulates subgroup sampling with target μ₀ and 3-sigma control limits. Introduce a process mean shift δ at the midpoint to evaluate detection probability and ARL.';
      controls = f('mu0', 'Target Process Mean (μ₀)', 100.0, 20.0, 300.0, 5.0)
        + f('sigma0', 'Process Sigma (σ₀)', 5.0, 1.0, 20.0, 0.5)
        + f('shiftDelta', 'Process Mean Shift (δ in σ)', 1.5, -3.0, 3.0, 0.25)
        + f('nSubgroup', 'Subgroup Sample Size (n)', 5, 3, 10, 1)
        + f('numSubgroups', 'Total Subgroups (k)', 25, 15, 40, 5);
    }else if(simType === 'ind-capability-cpk'){
      title = 'Process Capability Analysis: C_p, C_pk, Taguchi C_pm & Defect PPM Explorer';
      note = 'Inspect the relationship between manufacturing tolerances [LSL, USL], process centering μ, variability σ, and resulting parts-per-million (PPM) defect rates.';
      controls = f('lsl', 'Lower Spec Limit (LSL)', 85.0, 50.0, 150.0, 1.0)
        + f('usl', 'Upper Spec Limit (USL)', 115.0, 90.0, 200.0, 1.0)
        + f('mu', 'Process Mean (μ)', 102.0, 70.0, 130.0, 0.5)
        + f('sigma', 'Process Standard Dev (σ)', 4.2, 0.5, 12.0, 0.2)
        + f('targetT', 'Nominal Target (T)', 100.0, 80.0, 120.0, 1.0);
    }else if(simType === 'ind-cusum-ewma-chart'){
      title = 'Tabular CUSUM & EWMA Small-Shift Statistical Process Monitoring';
      note = 'Demonstrates how Cumulative Sum (CUSUM) and Exponentially Weighted Moving Average (EWMA) rapidly detect subtle process shifts (0.5σ to 1.5σ) where Shewhart charts lag.';
      controls = f('shift', 'Process Mean Shift (δ in σ)', 1.0, 0.0, 3.0, 0.2)
        + f('kRef', 'CUSUM Allowance Reference (k)', 0.5, 0.2, 1.2, 0.1)
        + f('hThreshold', 'CUSUM Decision Bound (h)', 4.5, 2.5, 8.0, 0.5)
        + f('lambdaEwma', 'EWMA Smoothing Weight (λ)', 0.20, 0.05, 0.50, 0.05);
    }else if(simType === 'ind-oc-sampling-plan'){
      title = 'Acceptance Sampling Plan OC Curve, Producer/Consumer Risks & AOQL';
      note = 'Design attribute lot inspection plans (n, c) and compute the Operating Characteristic (OC) curve, Producer’s Risk α at AQL, Consumer’s Risk β at LTPD, and AOQL.';
      controls = f('nSample', 'Sample Size (n)', 80, 20, 300, 10)
        + f('cAccept', 'Acceptance Number (c)', 2, 0, 6, 1)
        + f('aqlPct', 'Acceptable Quality Limit AQL (%)', 1.5, 0.2, 4.0, 0.1)
        + f('ltpdPct', 'Lot Tolerance Defective LTPD (%)', 6.0, 2.0, 15.0, 0.5);
    }

    el.innerHTML = `<h4>${title}</h4><p class="prob-note">${note}</p><div class="prob-fields">${controls}</div><div class="prob-actions"><button type="button" data-reset>Reset Defaults</button></div><div class="prob-results" aria-live="polite"></div>`;

    const inputs = [...el.querySelectorAll('input, select')];
    const initial = inputs.map(input => input.value);
    const result = el.querySelector('.prob-results');

    function render(){
      try{
        const get = id => {
          const inp = el.querySelector('#' + idPrefix + '-' + id);
          return inp ? (inp.tagName === 'SELECT' ? inp.value : parseFloat(inp.value)) : 0;
        };
        let values = {}, plot = '';

        if(simType === 'ind-xbar-r-chart'){
          const m = indXbarModel(get('mu0'), get('sigma0'), get('shiftDelta'), get('nSubgroup'), get('numSubgroups'));
          values = {
            'Target Center Line (CL)': fmt(m.clX),
            'Upper Control Limit (UCL)': fmt(m.uclX),
            'Lower Control Limit (LCL)': fmt(m.lclX),
            'Out-of-Control Subgroups': `${m.outOfControlCount} / ${get('numSubgroups')}`,
            'In-Control ARL₀': fmt(m.arl0) + ' subgroups',
            'Out-of-Control ARL₁': fmt(m.arl1) + ' subgroups'
          };
          plot = chart([
            { values: m.xbarSeries, width: 2.2, color: '#38bdf8' },
            { values: m.uclSeries, width: 1.5, dashed: true, color: '#ef4444' },
            { values: m.lclSeries, width: 1.5, dashed: true, color: '#ef4444' },
            { values: m.clSeries, width: 1.2, dotted: true, color: '#10b981' }
          ], 1, get('numSubgroups'), 'Shewhart X̄ Subgroups (Cyan) with 3σ Control Limits (Red Dashed) & Shift (Vertical Red)', m.shiftStart);
        }else if(simType === 'ind-capability-cpk'){
          const m = indCapabilityModel(get('lsl'), get('usl'), get('mu'), get('sigma'), get('targetT'));
          values = {
            'Potential Capability C_p': fmt(m.cp) + (m.cp >= 1.33 ? ' (Capable)' : ' (Inadequate)'),
            'Actual Capability C_pk': fmt(m.cpk) + (m.cpk >= 1.33 ? ' (Capable & Centered)' : ' (Off-Center / Inadequate)'),
            'Upper Capability C_pu': fmt(m.cpu),
            'Lower Capability C_pl': fmt(m.cpl),
            'Taguchi Index C_pm': fmt(m.cpm),
            'Expected Nonconforming PPM': fmt(m.ppm) + ' PPM'
          };
          plot = chart([
            { values: m.pdfCurve, width: 2.5, color: '#38bdf8' }
          ], m.xMin, m.xMax, 'Process Distribution vs Tolerances: LSL (x=' + get('lsl') + '), USL (x=' + get('usl') + '), Mean μ (x=' + get('mu') + ')', get('mu'));
        }else if(simType === 'ind-cusum-ewma-chart'){
          const m = indCusumEwmaModel(get('shift'), get('kRef'), get('hThreshold'), get('lambdaEwma'));
          values = {
            'CUSUM High Accumulation C⁺': fmt(m.cPlus),
            'CUSUM Detection Signal': m.cusumSignalStep !== null ? `Step ${m.cusumSignalStep}` : 'No signal',
            'EWMA Detection Signal': m.ewmaSignalStep !== null ? `Step ${m.ewmaSignalStep}` : 'No signal'
          };
          plot = chart([
            { values: m.cusumPosSeries, width: 2.2, color: '#38bdf8' },
            { values: m.ewmaSeries, width: 2.0, dashed: true, color: '#10b981' },
            { values: [[1, get('hThreshold')], [40, get('hThreshold')]], width: 1.5, dotted: true, color: '#ef4444' }
          ], 1, 40, 'CUSUM Accumulator C⁺ (Cyan), EWMA (Green Dashed), and CUSUM Bound h (Red Dotted)', 15);
        }else if(simType === 'ind-oc-sampling-plan'){
          const m = indOcSamplingModel(get('nSample'), get('cAccept'), get('aqlPct'), get('ltpdPct'));
          values = {
            'Acceptance Prob at AQL P_a(AQL)': (m.paAql * 100).toFixed(1) + '%',
            'Producer’s Risk α at AQL': m.producerRiskAlpha.toFixed(2) + '%',
            'Acceptance Prob at LTPD P_a(LTPD)': (m.paLtpd * 100).toFixed(1) + '%',
            'Consumer’s Risk β at LTPD': m.consumerRiskBeta.toFixed(2) + '%',
            'Average Outgoing Quality Limit (AOQL)': m.aoql.toFixed(3) + '% (at p=' + m.pAtAoql.toFixed(1) + '%)'
          };
          plot = chart([
            { values: m.ocCurve, width: 2.5, color: '#38bdf8' },
            { values: m.aoqCurve.map(([p, v]) => [p, v / 5]), width: 1.8, dashed: true, color: '#f59e0b' }
          ], 0, 15, 'Operating Characteristic OC Curve P_a (Cyan) & Scaled AOQ (Amber Dashed)', get('aqlPct'));
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
  root.IndustrialAndOfficialStatisticsSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
