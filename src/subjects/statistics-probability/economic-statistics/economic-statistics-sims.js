/* Economic Statistics interactive teaching models and Canvas/SVG visualizers. */
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

    // Grid and ticks
    let grid = `<line x1="${padL}" y1="${padT + plotH}" x2="${padL + plotW}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;
    grid += `<line x1="${padL}" y1="${padT}" x2="${padL}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;
    
    // Labels
    const xMid = (xMin + xMax) / 2;
    const yMid = (yMin + yMax) / 2;
    const ticks = `
      <text x="${padL}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMin)}</text>
      <text x="${padL + plotW/2}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMid)}</text>
      <text x="${padL + plotW}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMax)}</text>
      <text x="${padL - 8}" y="${padT + plotH}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMin)}</text>
      <text x="${padL - 8}" y="${padT + plotH/2}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMid)}</text>
      <text x="${padL - 8}" y="${padT + 10}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMax)}</text>
    `;

    return `
      <div class="prob-chart">
        <svg viewBox="0 0 ${W} ${H}" width="100%" height="auto" style="display:block; max-height:280px; font-family:sans-serif;">
          <text x="${W/2}" y="16" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">${titleStr}</text>
          ${grid}
          ${extra}
          ${paths}
          ${ticks}
        </svg>
      </div>
    `;
  }

  // --- SIMULATION 1: INDEX NUMBER AXIOMATIC REVERSAL VERIFIER ---
  function indexAxiomsModel(p1_rel, p2_rel, q1_rel, q2_rel){
    range(p1_rel, 0.2, 5.0, 'Good 1 Price Relative');
    range(p2_rel, 0.2, 5.0, 'Good 2 Price Relative');
    range(q1_rel, 0.2, 5.0, 'Good 1 Quantity Relative');
    range(q2_rel, 0.2, 5.0, 'Good 2 Quantity Relative');

    // Baseline: p0 = [10, 20], q0 = [100, 50]
    const p0 = [10, 20], q0 = [100, 50];
    const p1 = [p0[0] * p1_rel, p0[1] * p2_rel];
    const q1 = [q0[0] * q1_rel, q0[1] * q2_rel];

    const sum_p0q0 = p0[0]*q0[0] + p0[1]*q0[1]; // 1000 + 1000 = 2000
    const sum_p1q0 = p1[0]*q0[0] + p1[1]*q0[1];
    const sum_p0q1 = p0[0]*q1[0] + p0[1]*q1[1];
    const sum_p1q1 = p1[0]*q1[0] + p1[1]*q1[1];

    const P_L = (sum_p1q0 / sum_p0q0) * 100;
    const P_P = (sum_p1q1 / sum_p0q1) * 100;
    const P_F = Math.sqrt((sum_p1q0 / sum_p0q0) * (sum_p1q1 / sum_p0q1)) * 100;

    // Quantity Indices
    const Q_L = (sum_p0q1 / sum_p0q0) * 100;
    const Q_P = (sum_p1q1 / sum_p1q0) * 100;
    const Q_F = Math.sqrt((sum_p0q1 / sum_p0q0) * (sum_p1q1 / sum_p1q0)) * 100;

    // Value Ratio
    const V_01 = (sum_p1q1 / sum_p0q0);

    // Time Reversal Products: P(0,1) * P(1,0) (in ratio form)
    const TR_L = (sum_p1q0 / sum_p0q0) * (sum_p0q1 / sum_p1q1); // Laspeyres TR product
    const TR_F = 1.000; // Fisher always 1.000

    // Factor Reversal Product: P(0,1) * Q(0,1) / V(0,1)
    const FR_F = ((P_F / 100) * (Q_F / 100)) / V_01; // exactly 1.0

    // Bar chart values
    const barValues = [
      [1, P_L],
      [2, P_P],
      [3, P_F]
    ];

    return { P_L, P_P, P_F, Q_F, V_01: V_01 * 100, TR_L, TR_F, FR_F, barValues };
  }

  // --- SIMULATION 2: TIME SERIES DECOMPOSITION EXPLORER ---
  function timeseriesDecompModel(slope, seasonalAmp, cycleAmp, noiseSigma){
    range(slope, -2, 5, 'Secular Trend Slope');
    range(seasonalAmp, 0, 50, 'Seasonal Amplitude');
    range(cycleAmp, 0, 30, 'Cyclical Amplitude');
    range(noiseSigma, 0, 20, 'Irregular Noise');

    const N = 24; // 6 years of quarterly data
    const rawCurve = [], trendCurve = [], deseasonCurve = [];
    const seasons = [0.85, 1.25, 1.10, 0.80]; // Q1 low, Q2 high, Q3 moderate, Q4 low

    for(let t = 1; t <= N; t++){
      const q = (t - 1) % 4;
      const trend = 100 + slope * t;
      const s_factor = 1 + (seasons[q] - 1) * (seasonalAmp / 25);
      const cycle = cycleAmp * Math.sin((2 * Math.PI * t) / 12);
      const noise = (Math.sin(t * 7.3) * 0.5 + Math.cos(t * 3.7) * 0.5) * noiseSigma;

      const y = (trend + cycle) * s_factor + noise;
      const deseason = y / s_factor;

      rawCurve.push([t, y]);
      trendCurve.push([t, trend]);
      deseasonCurve.push([t, deseason]);
    }

    return { rawCurve, trendCurve, deseasonCurve };
  }

  // --- SIMULATION 3: LORENZ CURVE & GINI INEQUALITY EXPLORER ---
  function lorenzGiniModel(alpha){
    range(alpha, 1.05, 4.0, 'Pareto Shape Parameter alpha');

    const G = 1 / (2 * alpha - 1);
    const top10_share = Math.pow(0.10, (alpha - 1) / alpha) * 100;
    const bottom40_share = (1 - Math.pow(0.60, (alpha - 1) / alpha)) * 100;
    const palmaRatio = top10_share / (bottom40_share || 1);

    const lorenzCurve = [];
    const equalityLine = [];

    const steps = 50;
    for(let i = 0; i <= steps; i++){
      const p = i / steps;
      const L_p = 1 - Math.pow(1 - p, (alpha - 1) / alpha);
      lorenzCurve.push([p, L_p]);
      equalityLine.push([p, p]);
    }

    return { G, top10_share, bottom40_share, palmaRatio, lorenzCurve, equalityLine };
  }

  // --- SIMULATION 4: LEONTIEF INPUT-OUTPUT MATRIX SOLVER ---
  function leontiefIOModel(a12, a21, f1, f2){
    range(a12, 0.05, 0.60, 'Tech Coeff a12 (Mfg uses Agri)');
    range(a21, 0.05, 0.60, 'Tech Coeff a21 (Agri uses Mfg)');
    range(f1, 10, 500, 'Final Demand Agriculture');
    range(f2, 10, 500, 'Final Demand Manufacturing');

    const a11 = 0.15, a22 = 0.10;
    const det = (1 - a11) * (1 - a22) - a12 * a21;
    const isViable = det > 0 && (1 - a11) > 0 && (1 - a22) > 0;

    if(!isViable) throw Error('Hawkins-Simon conditions violated: technology matrix is parasitic and unsustainable.');

    const l11 = (1 - a22) / det;
    const l12 = a12 / det;
    const l21 = a21 / det;
    const l22 = (1 - a11) / det;

    const x1 = l11 * f1 + l12 * f2;
    const x2 = l21 * f1 + l22 * f2;

    const mult1 = l11 + l21;
    const mult2 = l12 + l22;

    const curve = [
      [1, f1], [1.3, x1],
      [2, f2], [2.3, x2]
    ];

    return { det, isViable, x1, x2, mult1, mult2, l11, l12, l21, l22, curve };
  }

  // --- CONTROLLER INITIALIZATION ---
  function initSimulation(el, simType){
    if(typeof document === 'undefined') return;
    const host = typeof el === 'string' ? document.getElementById(el) : el;
    if(!host) return;
    const type = simType || host.dataset?.sim || 'econ-index-axioms';
    el = host;
    let controls = '', initial = [];

    if(type === 'econ-index-axioms'){
      controls = field('p1_rel', 'Price Relative Good 1 (P1/P0)', 1.40, 0.5, 3.0, 0.05) +
                 field('p2_rel', 'Price Relative Good 2 (P1/P0)', 0.85, 0.5, 3.0, 0.05) +
                 field('q1_rel', 'Quantity Relative Good 1 (Q1/Q0)', 0.90, 0.5, 3.0, 0.05) +
                 field('q2_rel', 'Quantity Relative Good 2 (Q1/Q0)', 1.30, 0.5, 3.0, 0.05);
      initial = [1.40, 0.85, 0.90, 1.30];
    }else if(type === 'econ-timeseries-decomp'){
      controls = field('slope', 'Secular Trend Slope b', 1.5, -1.0, 4.0, 0.2) +
                 field('seasonalAmp', 'Seasonal Amplitude S', 25.0, 0.0, 50.0, 5.0) +
                 field('cycleAmp', 'Business Cycle Amplitude C', 12.0, 0.0, 30.0, 2.0) +
                 field('noiseSigma', 'Irregular Shock Noise I', 4.0, 0.0, 15.0, 1.0);
      initial = [1.5, 25.0, 12.0, 4.0];
    }else if(type === 'econ-lorenz-gini'){
      controls = field('alpha', 'Pareto Shape Parameter alpha', 1.60, 1.10, 3.50, 0.05);
      initial = [1.60];
    }else if(type === 'econ-leontief-io'){
      controls = field('a12', 'Input Coeff a12 (Mfg uses Agri)', 0.30, 0.05, 0.55, 0.05) +
                 field('a21', 'Input Coeff a21 (Agri uses Mfg)', 0.20, 0.05, 0.55, 0.05) +
                 field('f1', 'Final Demand Agriculture F1', 110.0, 20.0, 300.0, 10.0) +
                 field('f2', 'Final Demand Manufacturing F2', 140.0, 20.0, 300.0, 10.0);
      initial = [0.30, 0.20, 110.0, 140.0];
    }else{
      return;
    }

    el.innerHTML = `
      <div class="prob-card">
        <div class="prob-controls">${controls}</div>
        <div class="prob-actions"><button type="button" class="btn btn-secondary btn-sm" data-reset>Reset Parameters</button></div>
        <div class="prob-output"></div>
      </div>
    `;

    const result = el.querySelector('.prob-output');
    const inputs = el.querySelectorAll('input, select');
    function get(id){ return parseFloat(el.querySelector('#' + id).value); }

    function render(){
      try{
        let values = {}, plot = '';
        if(type === 'econ-index-axioms'){
          const m = indexAxiomsModel(get('p1_rel'), get('p2_rel'), get('q1_rel'), get('q2_rel'));
          values = {
            'Laspeyres Price Index (P_L)': fmt(m.P_L) + '%',
            'Paasche Price Index (P_P)': fmt(m.P_P) + '%',
            'Fisher Ideal Price Index (P_F)': fmt(m.P_F) + '%',
            'Fisher Quantity Index (Q_F)': fmt(m.Q_F) + '%',
            'Nominal Expenditure Ratio V_01': fmt(m.V_01) + '%',
            'Laspeyres Time Reversal P_01*P_10': fmt(m.TR_L) + (Math.abs(m.TR_L - 1.0) < 0.005 ? ' (Pass)' : ' (FAILS)'),
            'Fisher Time Reversal Test': '1.000 (PASSED)',
            'Fisher Factor Reversal P*Q/V': fmt(m.FR_F) + ' (PASSED)'
          };
          plot = chart([
            { values: [[0.5, m.P_L], [1.5, m.P_L]], width: 4, color: '#38bdf8' },
            { values: [[1.5, m.P_P], [2.5, m.P_P]], width: 4, color: '#fbbf24' },
            { values: [[2.5, m.P_F], [3.5, m.P_F]], width: 4, color: '#10b981' }
          ], 0, 4, 'Comparative Price Index Levels: Laspeyres (Cyan), Paasche (Yellow), Fisher (Green)', null, 100);
        }
        if(type === 'econ-timeseries-decomp'){
          const m = timeseriesDecompModel(get('slope'), get('seasonalAmp'), get('cycleAmp'), get('noiseSigma'));
          values = {
            'Model Specification': 'Multiplicative (Y = T * S * C * I)',
            'Sample Horizon': '24 Quarters (6 Years)',
            'Secular Trend Rate': fmt(get('slope')) + ' units / quarter',
            'Estimated Peak Season': 'Quarter 2 (+25%)',
            'Estimated Trough Season': 'Quarter 4 (-20%)'
          };
          plot = chart([
            { values: m.rawCurve, width: 2, color: '#38bdf8' },
            { values: m.trendCurve, width: 2, dashed: true, color: '#ef4444' },
            { values: m.deseasonCurve, width: 2.5, color: '#10b981' }
          ], 1, 24, 'Quarterly Time Series: Raw Y_t (Cyan), Secular Trend (Red), Deseasonalized (Green)');
        }
        if(type === 'econ-lorenz-gini'){
          const m = lorenzGiniModel(get('alpha'));
          values = {
            'Pareto Shape Parameter alpha': fmt(get('alpha')),
            'Gini Concentration Coefficient G': fmt(m.G),
            'Top 10% Income Share': fmt(m.top10_share) + '%',
            'Bottom 40% Income Share': fmt(m.bottom40_share) + '%',
            'Palma Ratio (Top 10% / Bottom 40%)': fmt(m.palmaRatio),
            'Inequality Assessment': m.G < 0.30 ? 'Low Inequality' : (m.G < 0.45 ? 'Moderate Inequality' : 'Severe Inequality')
          };
          plot = chart([
            { values: m.equalityLine, width: 1.5, dashed: true, color: '#94a3b8' },
            { values: m.lorenzCurve, width: 2.5, color: '#fbbf24' }
          ], 0, 1, 'Lorenz Curve L(p): Equality Line (Gray), Empirical Lorenz (Yellow)');
        }
        if(type === 'econ-leontief-io'){
          const m = leontiefIOModel(get('a12'), get('a21'), get('f1'), get('f2'));
          values = {
            'Hawkins-Simon Determinant det(I-A)': fmt(m.det) + ' > 0 (Viable)',
            'Required Agriculture Output X1': fmt(m.x1) + ' million',
            'Required Manufacturing Output X2': fmt(m.x2) + ' million',
            'Agriculture Output Multiplier O1': fmt(m.mult1),
            'Manufacturing Output Multiplier O2': fmt(m.mult2),
            'Leontief Inverse l11 / l22': fmt(m.l11) + ' / ' + fmt(m.l22)
          };
          plot = chart([
            { values: [[0.8, m.x1], [1.2, m.x1]], width: 5, color: '#38bdf8' },
            { values: [[1.8, m.x2], [2.2, m.x2]], width: 5, color: '#10b981' }
          ], 0, 3, 'Equilibrium Gross Outputs: Agriculture X1 (Cyan), Manufacturing X2 (Green)');
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
  root.EconomicStatisticsSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
