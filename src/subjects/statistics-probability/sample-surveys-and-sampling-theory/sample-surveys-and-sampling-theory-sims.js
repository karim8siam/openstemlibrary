/* Original sample surveys teaching models and interactive Canvas/SVG visualizers. */
(function(root){
  'use strict';
  function range(v,a,b,name){if(!Number.isFinite(v)||v<a||v>b)throw Error(name+' must be from '+a+' to '+b+'.');return v;}
  function integer(v,a,b,name){range(v,a,b,name);if(!Number.isInteger(v))throw Error(name+' must be an integer.');return v;}

  function fpcModel(N, n, s2){
    integer(N, 10, 100000, 'Population size N');
    integer(n, 1, N, 'Sample size n');
    range(s2, 0.001, 10000, 'Population variance S^2');
    const f = n / N;
    const fpc = (N - n) / N; // 1 - f
    const vWOR = (fpc / n) * s2;
    const vWR = s2 / n;
    const gainPct = vWOR > 0 ? ((vWR - vWOR) / vWOR) * 100 : 0;
    
    // Sample curve from k = 1 to N
    const pointsWOR = [];
    const pointsWR = [];
    const steps = 60;
    for(let i = 1; i <= steps; i++){
      const k = Math.max(1, Math.round(i * N / steps));
      const f_k = k / N;
      pointsWOR.push([k, ((1 - f_k) / k) * s2]);
      pointsWR.push([k, s2 / k]);
    }
    return { N, n, s2, f, fpc, vWOR, seWOR: Math.sqrt(vWOR), vWR, seWR: Math.sqrt(vWR), gainPct, pointsWOR, pointsWR };
  }

  function stratModel(w1, w2, w3, s1, s2, s3, n, N = 10000){
    range(w1, 0.01, 1, 'Stratum 1 weight');
    range(w2, 0.01, 1, 'Stratum 2 weight');
    range(w3, 0.01, 1, 'Stratum 3 weight');
    range(s1, 0.1, 100, 'Stratum 1 std dev');
    range(s2, 0.1, 100, 'Stratum 2 std dev');
    range(s3, 0.1, 100, 'Stratum 3 std dev');
    integer(n, 10, N, 'Total sample size n');

    const totalW = w1 + w2 + w3;
    const W = [w1 / totalW, w2 / totalW, w3 / totalW];
    const S = [s1, s2, s3];

    // Proportional allocation: n_h = n * W_h
    const nProp = W.map(wh => Math.max(2, Math.round(n * wh)));
    
    // Neyman allocation: n_h = n * (W_h * S_h) / sum(W_k * S_k)
    const wsSum = W.reduce((sum, wh, idx) => sum + wh * S[idx], 0);
    const nNeyman = W.map((wh, idx) => Math.max(2, Math.round(n * (wh * S[idx]) / wsSum)));

    // Equal allocation
    const nEqual = [Math.round(n / 3), Math.round(n / 3), n - 2 * Math.round(n / 3)];

    // Variances: V = sum( W_h^2 * (1 - n_h/N_h) * S_h^2 / n_h )
    const f = n / N;
    const vProp = (1 - f) / n * W.reduce((sum, wh, idx) => sum + wh * S[idx] * S[idx], 0);
    const vNeyman = (wsSum * wsSum) / n - (1 / N) * W.reduce((sum, wh, idx) => sum + wh * S[idx] * S[idx], 0);
    const vEqual = W.reduce((sum, wh, idx) => sum + (wh * wh * S[idx] * S[idx]) / nEqual[idx], 0) * (1 - f);

    const savingPct = vProp > 0 ? ((vProp - vNeyman) / vProp) * 100 : 0;
    return { W, S, n, nProp, nNeyman, nEqual, vProp, seProp: Math.sqrt(vProp), vNeyman, seNeyman: Math.sqrt(vNeyman), vEqual, seEqual: Math.sqrt(vEqual), savingPct };
  }

  function clusterModel(numPSU, M, rho, s2){
    integer(numPSU, 2, 500, 'Number of sampled clusters n');
    integer(M, 2, 200, 'Cluster size M');
    range(rho, -0.05, 0.80, 'Intraclass correlation rho');
    range(s2, 0.1, 5000, 'Unit variance S^2');

    const mTotal = numPSU * M;
    const deff = 1 + (M - 1) * rho;
    const nEff = mTotal / deff;
    const vSRS = s2 / mTotal;
    const vCluster = vSRS * deff;
    const lossPct = deff > 1 ? ((deff - 1) / deff) * 100 : 0;

    const curve = [];
    for(let m = 2; m <= 100; m += 2){
      curve.push([m, 1 + (m - 1) * rho]);
    }
    return { numPSU, M, rho, s2, mTotal, deff, nEff, vSRS, seSRS: Math.sqrt(vSRS), vCluster, seCluster: Math.sqrt(vCluster), lossPct, curve };
  }

  function ppsModel(cvX, cvY, rhoXY, n){
    range(cvX, 0.05, 2.5, 'Coefficient of variation of X (CV_x)');
    range(cvY, 0.05, 2.5, 'Coefficient of variation of Y (CV_y)');
    range(rhoXY, 0.0, 0.99, 'Correlation rho_xy');
    integer(n, 2, 1000, 'Sample size n');

    // Approximation of relative efficiency: RE = V_SRS / V_PPS
    // In equal-probability SRS: V_SRS propto CV_y^2
    // In PPS: V_PPS propto CV_y^2 + CV_x^2 - 2 * rho_xy * CV_x * CV_y
    const vRelSRS = cvY * cvY;
    const vRelPPS = Math.max(0.001, cvY * cvY + cvX * cvX - 2 * rhoXY * cvX * cvY);
    const relEff = vRelSRS / vRelPPS;
    const gainPct = (relEff - 1) * 100;

    const curve = [];
    for(let r = 0; r <= 0.98; r += 0.02){
      const v_pps_r = Math.max(0.001, cvY * cvY + cvX * cvX - 2 * r * cvX * cvY);
      curve.push([r, vRelSRS / v_pps_r]);
    }
    return { cvX, cvY, rhoXY, n, relEff, gainPct, curve, threshold: cvX / (2 * cvY) };
  }

  const api = { fpcModel, stratModel, clusterModel, ppsModel };
  if(typeof module !== 'undefined' && module.exports) module.exports = api;
  if(root) root.SurveyMath = api;
  if(!root) return;

  const doc = root.document;
  const fmt = v => v === null ? 'Undefined' : Number.isFinite(v) ? Number(v.toFixed(5)).toLocaleString('en-US', {maximumFractionDigits: 5}) : 'Unavailable';
  function field(id, label, value, min, max, step = 1){
    return `<label for="${id}">${label}<input id="${id}" type="number" value="${value}" min="${min}" max="${max}" step="${step}"></label>`;
  }
  function summary(values){
    return '<dl class="prob-summary">' + Object.entries(values).map(([k,v]) => `<div><dt>${k}</dt><dd>${typeof v === 'string' ? v : fmt(v)}</dd></div>`).join('') + '</dl>';
  }
  function chart(series, lo, hi, label, reference){
    const ymin = 0, ymax = Math.max(0.01, ...series.flatMap(s => s.values.map(p => p[1])), reference || 0) * 1.15;
    const px = x => 50 + 520 * (x - lo) / (hi - lo);
    const py = y => 205 - 170 * (y - ymin) / (ymax - ymin);
    let html = '<line x1="50" y1="205" x2="570" y2="205" stroke="currentColor"/><line x1="50" y1="35" x2="50" y2="205" stroke="currentColor"/>';
    if(reference !== undefined) html += `<line x1="50" y1="${py(reference)}" x2="570" y2="${py(reference)}" stroke="#fbbf24" stroke-dasharray="5 4"/>`;
    series.forEach((s, j) => {
      const color = ['#38bdf8', '#fbbf24', '#a78bfa', '#34d399'][j % 4];
      if(s.bars){
        const width = Math.min(35, 450 / (s.values.length + 1));
        s.values.forEach(([x, y]) => html += `<rect x="${px(x) - width/2}" y="${py(y)}" width="${width}" height="${Math.max(1, 205 - py(y))}" fill="${color}" opacity=".75"/>`);
      } else {
        html += `<path d="${s.values.map(([x,y], i) => (i ? 'L' : 'M') + px(x).toFixed(3) + ' ' + py(y).toFixed(3)).join(' ')}" fill="none" stroke="${color}" stroke-width="2.5"/>`;
      }
    });
    for(let i = 0; i < 5; i++){
      const x = lo + (hi - lo) * i / 4;
      html += `<text x="${px(x)}" y="228" fill="currentColor" text-anchor="middle">${fmt(x)}</text>`;
    }
    html += `<text x="43" y="40" fill="currentColor" text-anchor="end">${fmt(ymax)}</text><text x="42" y="208" fill="currentColor" text-anchor="end">0</text>`;
    return `<svg viewBox="0 0 620 245" role="img" aria-label="${label}" class="prob-chart"><title>${label}</title>${html}</svg>`;
  }

  function initSimulation(containerId, type){
    const el = doc.getElementById(containerId);
    if(!el || el.dataset.surveyMounted) return;
    el.dataset.surveyMounted = 'true';
    el.classList.add('prob-explorer');

    let title = '', note = '', controls = '';
    const f = (key, label, value, min, max, step) => field(containerId + '-' + key, label, value, min, max, step);

    if(type === 'survey-fpc'){
      title = 'Finite Population Correction (FPC) Convergence Explorer';
      note = 'Compares sampling without replacement (SRSWOR, blue curve) with sampling with replacement (SRSWR, yellow curve). As sampling fraction f = n/N approaches 1, SRSWOR variance collapses to zero.';
      controls = f('N', 'Universe size N', 1000, 50, 10000, 50) + f('n', 'Sample size n', 150, 1, 10000, 10) + f('s2', 'Unit variance S^2', 100, 1, 1000, 10);
    }
    if(type === 'survey-stratification'){
      title = 'Stratified Neyman Allocation Optimizer';
      note = 'Compares Proportional Allocation (blue bars) vs Neyman Optimal Allocation (yellow bars) across 3 heterogeneous strata. Neyman shifts sample units to strata with higher internal standard deviations.';
      controls = f('w1', 'Stratum 1 size (N_1)', 500, 10, 5000, 50) + f('s1', 'Stratum 1 std dev (S_1)', 10, 1, 100, 1) +
                 f('w2', 'Stratum 2 size (N_2)', 300, 10, 5000, 50) + f('s2', 'Stratum 2 std dev (S_2)', 25, 1, 100, 1) +
                 f('w3', 'Stratum 3 size (N_3)', 200, 10, 5000, 50) + f('s3', 'Stratum 3 std dev (S_3)', 50, 1, 100, 1) +
                 f('n', 'Total sample size n', 180, 15, 1000, 15);
    }
    if(type === 'survey-cluster-deff'){
      title = 'Cluster Sampling Variance Inflator & Intraclass Correlation Simulator';
      note = 'Demonstrates the variance inflation and Design Effect Deff = 1 + (M - 1) * rho as cluster size M increases. Intraclass correlation rho measures within-cluster homogeneity.';
      controls = f('psu', 'Number of clusters (n)', 20, 2, 200, 2) + f('M', 'Cluster size (M)', 30, 2, 100, 2) + f('rho', 'Intraclass correlation (rho)', 0.08, -0.05, 0.8, 0.01) + f('s2', 'Unit variance S^2', 120, 1, 1000, 10);
    }
    if(type === 'survey-pps'){
      title = 'PPS vs Equal Probability (SRS) Efficiency Comparator';
      note = 'Plots the Relative Efficiency RE = V_SRS / V_PPS against the correlation rho between study variable Y and size measure X. Blue curve demonstrates variance gains when rho > CV_x / (2 CV_y).';
      controls = f('cvX', 'Measure of size CV_x', 0.60, 0.1, 2.0, 0.05) + f('cvY', 'Outcome variable CV_y', 0.50, 0.1, 2.0, 0.05) + f('rho', 'Correlation rho_xy', 0.75, 0.0, 0.99, 0.05) + f('n', 'Sample size n', 50, 5, 500, 5);
    }

    if(!title){ el.textContent = 'Unknown survey simulation.'; return; }
    el.innerHTML = `<h4>${title}</h4><p>${note}</p><div class="prob-fields">${controls}</div><button type="button" data-reset>Reset</button><div class="prob-results" role="status" aria-live="polite"></div>`;

    const inputs = [...el.querySelectorAll('input,select')];
    const initial = inputs.map(i => i.value);
    const result = el.querySelector('.prob-results');
    const get = key => {
      const input = doc.getElementById(containerId + '-' + key);
      return input.value.trim() === '' ? NaN : Number(input.value);
    };

    function render(){
      try{
        let values = {}, plot = '';
        if(type === 'survey-fpc'){
          const N = get('N'), n = Math.min(get('n'), N), s2 = get('s2');
          const m = fpcModel(N, n, s2);
          values = {
            'Sampling fraction (f = n/N)': fmt(m.f),
            'Finite population correction (1 - f)': fmt(m.fpc),
            'SRSWOR variance V(y_wor)': fmt(m.vWOR),
            'SRSWR variance V(y_wr)': fmt(m.vWR),
            'SRSWOR standard error': fmt(m.seWOR),
            'SRSWR standard error': fmt(m.seWR),
            'Precision gain of WOR over WR': fmt(m.gainPct) + '%'
          };
          plot = chart([
            { values: m.pointsWOR },
            { values: m.pointsWR }
          ], 1, N, 'Sampling variance: Blue = SRSWOR with FPC, Yellow = SRSWR without FPC');
        }
        if(type === 'survey-stratification'){
          const w1 = get('w1'), s1 = get('s1'), w2 = get('w2'), s2 = get('s2'), w3 = get('w3'), s3 = get('s3'), n = get('n');
          const m = stratModel(w1, w2, w3, s1, s2, s3, n);
          values = {
            'Proportional sample (n1, n2, n3)': m.nProp.join(', '),
            'Neyman sample (n1, n2, n3)': m.nNeyman.join(', '),
            'Variance under Proportional allocation': fmt(m.vProp),
            'Variance under Neyman allocation': fmt(m.vNeyman),
            'Variance under Equal allocation': fmt(m.vEqual),
            'Neyman variance reduction over Proportional': fmt(m.savingPct) + '%'
          };
          plot = chart([
            { values: m.nProp.map((nh, idx) => [idx + 1, nh]), bars: true },
            { values: m.nNeyman.map((nh, idx) => [idx + 1.25, nh]), bars: true }
          ], 0.5, 3.75, 'Allocated sample size: Blue = Proportional, Yellow = Neyman Optimal');
        }
        if(type === 'survey-cluster-deff'){
          const psu = get('psu'), M = get('M'), rho = get('rho'), s2 = get('s2');
          const m = clusterModel(psu, M, rho, s2);
          values = {
            'Total sample size (n * M)': m.mTotal,
            'Design effect Deff': fmt(m.deff),
            'Effective sample size (n_eff)': fmt(m.nEff),
            'Cluster standard error SE(y_cl)': fmt(m.seCluster),
            'SRS equivalent standard error': fmt(m.seSRS),
            'Information loss percentage': fmt(m.lossPct) + '%'
          };
          plot = chart([
            { values: m.curve }
          ], 2, 100, 'Design effect (Deff = 1 + (M - 1)*rho) as a function of cluster size M', 1.0);
        }
        if(type === 'survey-pps'){
          const cvX = get('cvX'), cvY = get('cvY'), rho = get('rho'), n = get('n');
          const m = ppsModel(cvX, cvY, rho, n);
          values = {
            'Relative efficiency RE = V(SRS) / V(PPS)': fmt(m.relEff),
            'Precision gain': fmt(m.gainPct) + '%',
            'Correlation threshold for PPS superiority': fmt(m.threshold),
            'Current correlation rho_xy': fmt(rho),
            'Recommendation': rho > m.threshold ? 'PPS is superior to equal-probability SRS' : 'SRS is superior (correlation too weak for PPS)'
          };
          plot = chart([
            { values: m.curve }
          ], 0.0, 1.0, 'Relative efficiency RE = V_SRS / V_PPS vs correlation rho_xy (yellow line at RE = 1.0)', 1.0);
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
  root.SurveySimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
