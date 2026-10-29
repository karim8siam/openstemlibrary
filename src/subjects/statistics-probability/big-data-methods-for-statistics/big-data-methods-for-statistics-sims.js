/* Big Data Methods for Statistics interactive teaching models and SVG visualizers. */
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

  function field(id, label, val, min, max, step){
    return `<label class="prob-control" for="${id}"><span>${label}</span><input type="number" id="${id}" value="${val}" min="${min}" max="${max}" step="${step}"/></label>`;
  }
  function select(id, label, options){
    const opts = options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('');
    return `<label class="prob-control" for="${id}"><span>${label}</span><select id="${id}">${opts}</select></label>`;
  }
  function summary(vals){
    return '<div class="prob-summary stat-results" aria-live="polite">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(4)) : 'NaN';
  }

  // PRNG helper
  function mulberry32(a) {
    return function() {
      var t = a += 0x6D2B79F5;
      t = Math.imul(t ^ t >>> 15, t | 1);
      t ^= t + Math.imul(t ^ t >>> 7, t | 61);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    }
  }

  // Standard Normal sampler (Box-Muller)
  function normalRandom(prng) {
    let u = 0, v = 0;
    while(u === 0) u = prng();
    while(v === 0) v = prng();
    return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  }

  // 1. High-Dimensional Distance & Angle Concentration Model
  function concentrationModel(p, n, seed){
    integer(p, 2, 500, 'Dimension p');
    integer(n, 20, 200, 'Sample size n');
    const prng = mulberry32(seed || 12345);

    // Generate n points in R^p from N(0, I_p)
    const points = [];
    for(let i = 0; i < n; i++){
      const pt = new Float64Array(p);
      for(let j = 0; j < p; j++){
        pt[j] = normalRandom(prng);
      }
      points.push(pt);
    }

    // Pairwise distances & angles
    const dists = [];
    const angles = [];
    let minD = Infinity;
    let maxD = -Infinity;
    let sumD = 0;
    let sumAngle = 0;
    let count = 0;

    for(let i = 0; i < n; i++){
      for(let k = i + 1; k < n; k++){
        let sqDist = 0;
        let dot = 0;
        let normA = 0;
        let normB = 0;
        for(let j = 0; j < p; j++){
          const diff = points[i][j] - points[k][j];
          sqDist += diff * diff;
          dot += points[i][j] * points[k][j];
          normA += points[i][j] * points[i][j];
          normB += points[k][j] * points[k][j];
        }
        const d = Math.sqrt(sqDist);
        dists.push(d);
        if(d < minD) minD = d;
        if(d > maxD) maxD = d;
        sumD += d;

        const cosTheta = Math.max(-1, Math.min(1, dot / (Math.sqrt(normA) * Math.sqrt(normB))));
        const deg = Math.acos(cosTheta) * (180 / Math.PI);
        angles.push(deg);
        sumAngle += deg;
        count++;
      }
    }

    const meanD = sumD / count;
    let varD = 0;
    for(let i = 0; i < count; i++){
      varD += (dists[i] - meanD) ** 2;
    }
    varD /= count;
    const sdD = Math.sqrt(varD);
    const meanAngle = sumAngle / count;
    const distRatio = (maxD - minD) / minD;
    const relDispersion = sdD / meanD;

    return {
      p, n, minD, maxD, meanD, sdD, distRatio, relDispersion, meanAngle, dists, angles
    };
  }

  // 2. Lasso vs Ridge Regularization Path Model
  function regularizationPathModel(method, lambda, noise, seed){
    range(lambda, 0.001, 20.0, 'Lambda');
    range(noise, 0.0, 2.0, 'Noise level');
    const prng = mulberry32(seed || 42);

    // True sparse coefficients in 6 dimensions
    const trueBeta = [3.0, -2.5, 1.5, 0.0, 0.0, 0.0];
    const p = trueBeta.length;
    const n = 100;

    // Generate correlated predictors X
    const X = [];
    const y = [];
    for(let i = 0; i < n; i++){
      const row = new Float64Array(p);
      for(let j = 0; j < p; j++){
        row[j] = normalRandom(prng);
      }
      // Add correlation between features 1 and 2
      row[1] = 0.6 * row[0] + 0.8 * row[1];
      let yVal = 0;
      for(let j = 0; j < p; j++) yVal += row[j] * trueBeta[j];
      yVal += noise * normalRandom(prng);
      X.push(row);
      y.push(yVal);
    }

    // Unpenalized Gram matrix X^T X / n and X^T y / n
    const G = Array.from({length: p}, () => new Float64Array(p));
    const Xy = new Float64Array(p);
    for(let i = 0; i < n; i++){
      for(let j = 0; j < p; j++){
        Xy[j] += X[i][j] * y[i] / n;
        for(let k = 0; k < p; k++){
          G[j][k] += X[i][j] * X[i][k] / n;
        }
      }
    }

    const betaHat = new Float64Array(p);

    if(method === 'ridge'){
      // Ridge regression via simple regularized Gauss-Seidel / coordinate descent
      for(let iter = 0; iter < 100; iter++){
        for(let j = 0; j < p; j++){
          let r = Xy[j];
          for(let k = 0; k < p; k++){
            if(k !== j) r -= G[j][k] * betaHat[k];
          }
          betaHat[j] = r / (G[j][j] + lambda);
        }
      }
    } else {
      // Lasso coordinate descent with soft-thresholding
      for(let iter = 0; iter < 100; iter++){
        for(let j = 0; j < p; j++){
          let r = Xy[j];
          for(let k = 0; k < p; k++){
            if(k !== j) r -= G[j][k] * betaHat[k];
          }
          // Soft-threshold operator
          const denom = G[j][j];
          const raw = r / denom;
          const thresh = lambda / denom;
          if(raw > thresh) betaHat[j] = raw - thresh;
          else if(raw < -thresh) betaHat[j] = raw + thresh;
          else betaHat[j] = 0.0;
        }
      }
    }

    let activeCount = 0;
    let l1Norm = 0;
    let l2NormSq = 0;
    for(let j = 0; j < p; j++){
      if(Math.abs(betaHat[j]) > 1e-4) activeCount++;
      l1Norm += Math.abs(betaHat[j]);
      l2NormSq += betaHat[j] * betaHat[j];
    }

    return {
      method, lambda, betaHat: Array.from(betaHat), trueBeta, activeCount,
      l1Norm, l2Norm: Math.sqrt(l2NormSq)
    };
  }

  // 3. Stochastic Optimization Simulation Model
  function optimizationModel(optimizer, lr, batchSize, steps, seed){
    range(lr, 0.001, 1.0, 'Learning rate');
    integer(batchSize, 1, 128, 'Batch size');
    integer(steps, 20, 300, 'Iterations');
    const prng = mulberry32(seed || 999);

    // Quadratic objective: f(x, y) = 0.5 * (10 * x^2 + y^2) (Condition number 10)
    // with stochastic gradient noise: g = [10*x + noise_x, y + noise_y]
    let theta = [4.0, 4.0];
    const trajectory = [[theta[0], theta[1]]];
    const losses = [0.5 * (10 * theta[0]**2 + theta[1]**2)];

    // Optimizer states
    let m_t = [0, 0];
    let v_t = [0, 0];
    const beta1 = 0.9, beta2 = 0.999, eps = 1e-8;

    for(let t = 1; t <= steps; t++){
      // Generate stochastic gradient with batch noise ~ N(0, 16 / B)
      const noiseScale = 4.0 / Math.sqrt(batchSize);
      let gx = 10.0 * theta[0];
      let gy = 1.0 * theta[1];

      if(optimizer !== 'gd'){
        gx += noiseScale * normalRandom(prng);
        gy += noiseScale * normalRandom(prng);
      }

      if(optimizer === 'adam'){
        m_t[0] = beta1 * m_t[0] + (1 - beta1) * gx;
        m_t[1] = beta1 * m_t[1] + (1 - beta1) * gy;
        v_t[0] = beta2 * v_t[0] + (1 - beta2) * (gx * gx);
        v_t[1] = beta2 * v_t[1] + (1 - beta2) * (gy * gy);

        const mHat0 = m_t[0] / (1 - Math.pow(beta1, t));
        const mHat1 = m_t[1] / (1 - Math.pow(beta1, t));
        const vHat0 = v_t[0] / (1 - Math.pow(beta2, t));
        const vHat1 = v_t[1] / (1 - Math.pow(beta2, t));

        theta[0] -= (lr * mHat0) / (Math.sqrt(vHat0) + eps);
        theta[1] -= (lr * mHat1) / (Math.sqrt(vHat1) + eps);
      } else {
        theta[0] -= lr * gx;
        theta[1] -= lr * gy;
      }

      // Constrain extremes
      theta[0] = Math.max(-10, Math.min(10, theta[0]));
      theta[1] = Math.max(-10, Math.min(10, theta[1]));

      trajectory.push([theta[0], theta[1]]);
      losses.push(0.5 * (10 * theta[0]**2 + theta[1]**2));
    }

    const finalLoss = losses[losses.length - 1];
    const distFromOpt = Math.sqrt(theta[0]**2 + theta[1]**2);

    return {
      optimizer, lr, batchSize, steps, trajectory, losses, finalLoss, distFromOpt
    };
  }

  // 4. Benjamini-Hochberg False Discovery Rate Model
  function fdrModel(qStar, pi0, mTests, effectSize, seed){
    range(qStar, 0.01, 0.30, 'Target FDR q*');
    range(pi0, 0.3, 0.98, 'Null proportion pi0');
    integer(mTests, 40, 500, 'Number of tests m');
    range(effectSize, 1.0, 5.0, 'Effect size');
    const prng = mulberry32(seed || 777);

    const m0 = Math.round(pi0 * mTests);
    const m1 = mTests - m0;

    // Normal CDF approximation
    function pnorm(z) {
      const a1 =  0.254829592, a2 = -0.284496736, a3 =  1.421413741;
      const a4 = -1.453152027, a5 =  1.061405429, p =  0.3275911;
      const sign = z < 0 ? -1 : 1;
      const x = Math.abs(z) / Math.SQRT2;
      const t = 1.0 / (1.0 + p * x);
      const erf = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
      return 0.5 * (1.0 + sign * erf);
    }

    const pvals = [];
    for(let i = 0; i < mTests; i++){
      const isNull = i < m0;
      const z = isNull ? normalRandom(prng) : (effectSize + normalRandom(prng));
      const p = 2 * (1 - pnorm(Math.abs(z)));
      pvals.push({ p: Math.max(1e-12, Math.min(1.0, p)), isNull, origIndex: i });
    }

    // Sort p-values ascending
    pvals.sort((a, b) => a.p - b.p);

    // Benjamini-Hochberg procedure
    let maxK = -1;
    for(let k = 1; k <= mTests; k++){
      const thresh = (k / mTests) * qStar;
      if(pvals[k - 1].p <= thresh){
        maxK = k;
      }
    }

    const discoveries = maxK > 0 ? maxK : 0;
    let falseDiscoveries = 0;
    for(let i = 0; i < discoveries; i++){
      if(pvals[i].isNull) falseDiscoveries++;
    }
    const trueDiscoveries = discoveries - falseDiscoveries;
    const empiricalFDP = discoveries > 0 ? (falseDiscoveries / discoveries) : 0.0;

    return {
      qStar, pi0, mTests, m0, m1, discoveries, trueDiscoveries, falseDiscoveries,
      empiricalFDP, pvals, maxK
    };
  }

  // SVG Chart rendering helpers
  function renderConcentrationPlot(m){
    const w = 480, h = 220, pad = 40;
    // Render histogram of pairwise distances
    const dists = m.dists;
    const minX = m.minD * 0.9;
    const maxX = m.maxD * 1.1;
    const numBins = 24;
    const binWidth = (maxX - minX) / numBins;
    const bins = new Array(numBins).fill(0);

    for(let d of dists){
      const bIdx = Math.min(numBins - 1, Math.max(0, Math.floor((d - minX) / binWidth)));
      bins[bIdx]++;
    }
    const maxBin = Math.max(1, ...bins);

    let bars = '';
    for(let i = 0; i < numBins; i++){
      const x = pad + (i / numBins) * (w - 2 * pad);
      const bW = Math.max(1, (w - 2 * pad) / numBins - 2);
      const bH = (bins[i] / maxBin) * (h - 2 * pad);
      const y = h - pad - bH;
      bars += `<rect x="${x}" y="${y}" width="${bW}" height="${bH}" fill="#38bdf8" rx="2" opacity="0.85"/>`;
    }

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Pairwise Distance Distribution (Dimension p = ${m.p})</text>
      ${bars}
      <line x1="${pad}" y1="${h - pad}" x2="${w - pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1.5"/>
      <text x="${pad}" y="${h - 12}" fill="#94a3b8" font-size="10">${fmt(minX)}</text>
      <text x="${w - pad}" y="${h - 12}" fill="#94a3b8" font-size="10" text-anchor="end">${fmt(maxX)}</text>
      <text x="${w/2}" y="${h - 12}" fill="#38bdf8" font-size="10" text-anchor="middle">Mean: ${fmt(m.meanD)} (Rel Disp: ${fmt(m.relDispersion)})</text>
    </svg>`;
  }

  function renderLassoPlot(m){
    const w = 480, h = 220, pad = 40;
    const p = m.betaHat.length;
    const barW = (w - 2 * pad) / (p * 2);

    let bars = '';
    for(let j = 0; j < p; j++){
      const trueVal = m.trueBeta[j];
      const estVal = m.betaHat[j];
      const x1 = pad + j * 2 * barW;
      const x2 = x1 + barW - 2;

      const yZero = h / 2;
      const scale = 25;

      const hTrue = Math.abs(trueVal) * scale;
      const yTrue = trueVal >= 0 ? (yZero - hTrue) : yZero;
      bars += `<rect x="${x1}" y="${yTrue}" width="${barW - 4}" height="${hTrue}" fill="#64748b" opacity="0.5" rx="1"/>`;

      const hEst = Math.abs(estVal) * scale;
      const yEst = estVal >= 0 ? (yZero - hEst) : yZero;
      const col = Math.abs(estVal) > 1e-4 ? '#10b981' : '#ef4444';
      bars += `<rect x="${x2}" y="${yEst}" width="${barW - 4}" height="${hEst}" fill="${col}" rx="1"/>`;

      bars += `<text x="${x1 + barW - 2}" y="${h - 15}" fill="#cbd5e1" font-size="10" text-anchor="middle">β${j+1}</text>`;
    }

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Estimated vs. True Coefficients (${m.method.toUpperCase()} λ = ${m.lambda})</text>
      <line x1="${pad}" y1="${h/2}" x2="${w - pad}" y2="${h/2}" stroke="#475569" stroke-width="1"/>
      ${bars}
      <text x="${pad}" y="35" fill="#64748b" font-size="9">■ Gray = True</text>
      <text x="${pad + 75}" y="35" fill="#10b981" font-size="9">■ Green = Active</text>
      <text x="${pad + 155}" y="35" fill="#ef4444" font-size="9">■ Red = Zeroed</text>
    </svg>`;
  }

  function renderOptimizerPlot(m){
    const w = 480, h = 220, pad = 40;
    const losses = m.losses;
    const maxLoss = Math.max(...losses);
    const minLoss = Math.min(...losses);

    let pts = [];
    for(let i = 0; i < losses.length; i++){
      const x = pad + (i / (losses.length - 1)) * (w - 2 * pad);
      const normY = maxLoss > minLoss ? (losses[i] - minLoss) / (maxLoss - minLoss) : 0.5;
      const y = h - pad - normY * (h - 2 * pad);
      pts.push(`${x.toFixed(1)},${y.toFixed(1)}`);
    }

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Loss Trajectory over Iterations (${m.optimizer.toUpperCase()})</text>
      <line x1="${pad}" y1="${h - pad}" x2="${w - pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1.5"/>
      <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1.5"/>
      <polyline points="${pts.join(' ')}" fill="none" stroke="#f59e0b" stroke-width="2"/>
      <text x="${pad}" y="${pad - 8}" fill="#94a3b8" font-size="9">Loss: ${fmt(maxLoss)}</text>
      <text x="${w - pad}" y="${h - 12}" fill="#94a3b8" font-size="10" text-anchor="end">Step ${m.steps}</text>
      <text x="${pad}" y="${h - 12}" fill="#94a3b8" font-size="10">Step 0</text>
    </svg>`;
  }

  function renderFdrPlot(m){
    const w = 480, h = 220, pad = 40;
    const mTests = m.mTests;
    const pvals = m.pvals;

    // Log-log or linear scatter of sorted p-values
    let circles = '';
    const maxK = m.maxK;

    for(let i = 0; i < mTests; i++){
      const k = i + 1;
      const x = pad + (k / mTests) * (w - 2 * pad);
      const y = h - pad - pvals[i].p * (h - 2 * pad);
      const isRej = k <= maxK;
      const col = isRej ? (pvals[i].isNull ? '#ef4444' : '#10b981') : '#64748b';
      const r = isRej ? 3.5 : 1.5;
      circles += `<circle cx="${x}" cy="${y}" r="${r}" fill="${col}" opacity="${isRej ? 0.9 : 0.4}"/>`;
    }

    // BH line
    const xEnd = w - pad;
    const yEnd = h - pad - m.qStar * (h - 2 * pad);
    const bhLine = `<line x1="${pad}" y1="${h - pad}" x2="${xEnd}" y2="${yEnd}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>`;

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Sorted p-values vs. Benjamini-Hochberg Boundary (q* = ${m.qStar})</text>
      <line x1="${pad}" y1="${h - pad}" x2="${w - pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1"/>
      <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1"/>
      ${bhLine}
      ${circles}
      <text x="${w - pad}" y="${yEnd - 6}" fill="#38bdf8" font-size="9" text-anchor="end">BH Critical Line</text>
      <text x="${pad + 10}" y="${pad + 15}" fill="#10b981" font-size="9">● True Pos: ${m.trueDiscoveries}</text>
      <text x="${pad + 10}" y="${pad + 28}" fill="#ef4444" font-size="9">● False Pos: ${m.falseDiscoveries}</text>
    </svg>`;
  }

  function initSimulation(el, type){
    if(typeof document === 'undefined') return;
    const host = typeof el === 'string' ? document.getElementById(el) : el;
    if(!host) return;
    const simType = type || (host.getAttribute ? host.getAttribute('data-sim') : null) || 'bigdata-dim-concentration';
    el = host;
    let controls = '';

    if(simType === 'bigdata-dim-concentration'){
      controls = field('dimP', 'Dimension p', 50, 2, 500, 10) +
                 field('dimN', 'Sample Points n', 60, 20, 200, 10);
    } else if(simType === 'bigdata-lasso-path'){
      controls = select('regMethod', 'Penalty Type', [['lasso', 'Lasso (L1 Regularization)'], ['ridge', 'Ridge (L2 Regularization)']]) +
                 field('regLambda', 'Tuning Parameter λ', 0.5, 0.001, 10.0, 0.1) +
                 field('regNoise', 'Gaussian Noise σ', 0.5, 0.0, 2.0, 0.1);
    } else if(simType === 'bigdata-sgd-optimizer'){
      controls = select('optAlgo', 'Optimizer', [['gd', 'Batch Gradient Descent'], ['sgd', 'Stochastic GD (B=1)'], ['minibatch', 'Mini-batch SGD'], ['adam', 'Adam Optimizer']]) +
                 field('optLr', 'Learning Rate η', 0.08, 0.001, 0.5, 0.01) +
                 field('optBatch', 'Batch Size B', 16, 1, 128, 4) +
                 field('optSteps', 'Iterations', 100, 20, 300, 10);
    } else if(simType === 'bigdata-fdr-benjamini'){
      controls = field('fdrQ', 'Target FDR q*', 0.10, 0.01, 0.25, 0.01) +
                 field('fdrPi0', 'True Null Proportion π0', 0.80, 0.40, 0.95, 0.05) +
                 field('fdrM', 'Number of Hypotheses m', 150, 40, 400, 10) +
                 field('fdrMu', 'Alternative Effect Size μ', 2.5, 1.0, 4.5, 0.25);
    }

    el.innerHTML = `<div class="prob-panel">
      <div class="prob-controls">${controls}</div>
      <div class="prob-actions"><button type="button" class="btn btn-secondary" data-reset>Reset</button></div>
      <div class="prob-output"></div>
    </div>`;

    const result = el.querySelector('.prob-output');
    const inputs = Array.from(el.querySelectorAll('input, select'));
    const initial = inputs.map(input => input.value);

    function get(id){
      const el = doc.getElementById(id);
      return el ? (el.tagName === 'SELECT' ? el.value : parseFloat(el.value)) : 0;
    }

    function render(){
      try{
        let values = {};
        let plot = '';

        if(simType === 'bigdata-dim-concentration'){
          const m = concentrationModel(Math.round(get('dimP')), Math.round(get('dimN')), 12345);
          values = {
            'Dimension p': m.p,
            'Pairwise Distance Range': `[${fmt(m.minD)}, ${fmt(m.maxD)}]`,
            'Distance Spread Ratio (Dmax - Dmin)/Dmin': fmt(m.distRatio),
            'Relative Dispersion SD(D)/E[D]': fmt(m.relDispersion),
            'Average Pairwise Angle': fmt(m.meanAngle) + '° (Near-Orthogonality)'
          };
          plot = renderConcentrationPlot(m);
        } else if(simType === 'bigdata-lasso-path'){
          const m = regularizationPathModel(get('regMethod'), get('regLambda'), get('regNoise'), 42);
          values = {
            'Regularization Method': m.method.toUpperCase(),
            'Active Non-Zero Features': `${m.activeCount} / ${m.betaHat.length}`,
            'L1 Norm of Coefficients': fmt(m.l1Norm),
            'L2 Norm of Coefficients': fmt(m.l2Norm),
            'Coefficients': m.betaHat.map(b => fmt(b)).join(', ')
          };
          plot = renderLassoPlot(m);
        } else if(simType === 'bigdata-sgd-optimizer'){
          const algo = get('optAlgo');
          const batch = algo === 'gd' ? 500 : (algo === 'sgd' ? 1 : Math.round(get('optBatch')));
          const m = optimizationModel(algo, get('optLr'), batch, Math.round(get('optSteps')), 999);
          values = {
            'Selected Optimizer': m.optimizer.toUpperCase(),
            'Effective Batch Size': m.batchSize,
            'Final Objective Loss': fmt(m.finalLoss),
            'Distance from Optimum (0,0)': fmt(m.distFromOpt)
          };
          plot = renderOptimizerPlot(m);
        } else if(simType === 'bigdata-fdr-benjamini'){
          const m = fdrModel(get('fdrQ'), get('fdrPi0'), Math.round(get('fdrM')), get('fdrMu'), 777);
          values = {
            'Target FDR Level q*': fmt(m.qStar),
            'Total Discoveries R': m.discoveries,
            'True Discoveries (Hits)': m.trueDiscoveries,
            'False Discoveries (False Positives)': m.falseDiscoveries,
            'Empirical False Discovery Proportion': fmt(m.empiricalFDP)
          };
          plot = renderFdrPlot(m);
        }

        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    const resetBtn = el.querySelector('[data-reset]');
    if(resetBtn){
      resetBtn.addEventListener('click', () => {
        inputs.forEach((input, i) => input.value = initial[i]);
        render();
      });
    }
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.BigDataSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
