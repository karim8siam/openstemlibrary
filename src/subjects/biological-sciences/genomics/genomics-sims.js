/* Genomics Interactive Simulation Suite */
"use strict";
// OpenSTEM Genomics: standalone pedagogical models with fixed synthetic assumptions.
const predictions = {
 repeat:x=>x/100, ploidy:x=>x/20, phred:x=>Math.pow(10,-x/10),
 coverage:x=>x, kmers:x=>201-x, n50:x=>x,
 vaf:x=>x/100, allele:x=>x/200, fold:x=>Math.log2(x/40),
 occupancy:x=>x/(25+x), hwe:x=>2*(x/100)*(1-x/100),
 bonferroni:x=>0.05/(1000*x), prevalence:x=>(.90*(x/1000))/(.90*(x/1000)+.05*(1-x/1000)),
 penetrance:x=>x/20, doublets:x=>x/2000, metareads:x=>x/10000
};
const unitLabels={repeat:'fraction',ploidy:'pg',phred:'error probability',coverage:'×',kmers:'positions',n50:'Mb',vaf:'fraction',allele:'allele-copy fraction',fold:'log₂ ratio',occupancy:'fraction',hwe:'fraction',bonferroni:'threshold',prevalence:'fraction',penetrance:'fraction',doublets:'fraction',metareads:'fraction'};
function fmt(v){if(!Number.isFinite(v))return 'Undefined';if(Math.abs(v)>0&&Math.abs(v)<0.0001)return v.toExponential(3);return Number(v.toPrecision(5)).toString()}
function computeModel(k,x){if(!Object.prototype.hasOwnProperty.call(predictions,k))throw Error('Unknown model '+k);return predictions[k](x)}
function chart(model,active){let pts=[];const f=predictions[model.kind],N=80,ys=[];
 for(let i=0;i<=N;i++){const x=model.min+(model.max-model.min)*i/N;ys.push(f(x));}
 const lo=Math.min(...ys),hi=Math.max(...ys),span=(hi-lo)||1;
 for(let i=0;i<=N;i++){const px=20+i/N*460,py=158-125*(ys[i]-lo)/span;pts.push(px.toFixed(1)+','+py.toFixed(1));}
 const xNorm=(active-model.min)/(model.max-model.min);
 const yNorm=(f(active)-lo)/span;
 const v=`<svg viewBox="0 0 500 180" role="img" aria-label="Plot of ${model.title.replace(/[&<>"']/g,'')} as slider value changes; range is automatically scaled"><line x1="20" y1="158" x2="482" y2="158" stroke="#b7cbc5" stroke-width="2"/><polyline points="${pts.join(' ')}" fill="none" stroke="#146a60" stroke-width="3"/><circle cx="${(20+460*xNorm).toFixed(1)}" cy="${(158-125*yNorm).toFixed(1)}" r="6" fill="#c16123" stroke="#fff" stroke-width="2"/><text x="20" y="174" font-size="11" fill="#425d58">${model.min}</text><text x="472" y="174" text-anchor="end" font-size="11" fill="#425d58">${model.max}</text></svg>`;
 return v;
}
function setup(){document.querySelectorAll('.model[data-kind]').forEach(section=>{
 let model={kind:section.dataset.kind,min:Number(section.dataset.min),max:Number(section.dataset.max),title:section.dataset.title};
 const slider=section.querySelector('input[type="range"]'),out=section.querySelector('output'),viz=section.querySelector('.viz');
 if(!slider||!out||!viz||!predictions[model.kind])return;
 const update=()=>{const x=Number(slider.value),y=computeModel(model.kind,x);out.textContent=`Input ${fmt(x)} → ${fmt(y)} ${unitLabels[model.kind]||''}`;viz.innerHTML=chart(model,x);};
 slider.addEventListener('input',update);update();
 });}
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',setup);else setup()}
if(typeof module!=='undefined')module.exports={computeModel,predictions,unitLabels};


window.GENOMICS_MODELS = [
  {
    "id": "genome_frac",
    "unit": 1,
    "title": "Fraction annotated as repeat sequence",
    "label": "Repeat-annotated bases out of 100",
    "kind": "repeat",
    "min": 0,
    "max": 100,
    "initial": 42,
    "step": 1,
    "formula": "Repeat fraction = flagged bases / total",
    "caveat": "Toy percentage only"
  },
  {
    "id": "ploidy",
    "unit": 1,
    "title": "Haploid size from diploid DNA content",
    "label": "Measured diploid content \u00d70.1 pg",
    "kind": "ploidy",
    "min": 2,
    "max": 40,
    "initial": 16,
    "step": 1,
    "formula": "Haploid mass = diploid mass / 2",
    "caveat": "Only ordinary diploid-nuclear assumption"
  },
  {
    "id": "phred",
    "unit": 2,
    "title": "Base-call error from a Phred score",
    "label": "Phred quality score",
    "kind": "phred",
    "min": 5,
    "max": 45,
    "initial": 30,
    "step": 1,
    "formula": "P(error)=10^(\u2212Q/10)",
    "caveat": "Does not include mapping error"
  },
  {
    "id": "coverage",
    "unit": 2,
    "title": "Nominal average read depth",
    "label": "Aligned gigabases \u00d70.1",
    "kind": "coverage",
    "min": 1,
    "max": 80,
    "initial": 30,
    "step": 1,
    "formula": "Depth = aligned bases / genome length",
    "caveat": "Assume 100 Mb reference, uniformity not implied"
  },
  {
    "id": "kmers",
    "unit": 3,
    "title": "Count of k-mer starting positions",
    "label": "k-mer length for a 200-bp string",
    "kind": "kmers",
    "min": 10,
    "max": 100,
    "initial": 31,
    "step": 1,
    "formula": "Positions = 200\u2212k+1",
    "caveat": "Positions, not necessarily unique strings"
  },
  {
    "id": "n50",
    "unit": 3,
    "title": "Two-contig balance and length N50",
    "label": "Largest contig size (Mb), total=10Mb",
    "kind": "n50",
    "min": 5,
    "max": 9,
    "initial": 7,
    "step": 1,
    "formula": "N50 of [x,10\u2212x] is x if x\u22655",
    "caveat": "N50 is not a correctness metric"
  },
  {
    "id": "vaf",
    "unit": 4,
    "title": "Observed alternate-read fraction",
    "label": "Alternate reads (total high-quality reads=100)",
    "kind": "vaf",
    "min": 0,
    "max": 100,
    "initial": 30,
    "step": 1,
    "formula": "VAF=alternate/total",
    "caveat": "VAF does not equal clonal cell fraction"
  },
  {
    "id": "allele",
    "unit": 4,
    "title": "Copy count per diploid reference locus",
    "label": "Alternate allele copies (2n=200)",
    "kind": "allele",
    "min": 0,
    "max": 200,
    "initial": 30,
    "step": 1,
    "formula": "Frequency=allele copies/200",
    "caveat": "Assumes all calls complete and diploid"
  },
  {
    "id": "fold",
    "unit": 5,
    "title": "Regulatory signal log2 fold-change",
    "label": "After-condition signal (before=40)",
    "kind": "fold",
    "min": 10,
    "max": 160,
    "initial": 80,
    "step": 5,
    "formula": "log2FC=log2(after/40)",
    "caveat": "Scales must be comparable"
  },
  {
    "id": "occupancy",
    "unit": 5,
    "title": "Toy binding curve under mass action",
    "label": "Ligand concentration in arbitrary units",
    "kind": "occupancy",
    "min": 0,
    "max": 100,
    "initial": 30,
    "step": 1,
    "formula": "\u03b8=L/(Kd+L), Kd=25",
    "caveat": "Not a TF binding inference from motif sequence"
  },
  {
    "id": "hwe",
    "unit": 6,
    "title": "Expected heterozygote fraction under HWE",
    "label": "Allele frequency p (%)",
    "kind": "hwe",
    "min": 0,
    "max": 100,
    "initial": 45,
    "step": 1,
    "formula": "H=2p(1\u2212p)",
    "caveat": "Idealized randomly mating diploid benchmark"
  },
  {
    "id": "bonferroni",
    "unit": 6,
    "title": "Family-wise significance threshold",
    "label": "Number of thousands of tests",
    "kind": "bonferroni",
    "min": 1,
    "max": 50,
    "initial": 10,
    "step": 1,
    "formula": "\u03b1/m with \u03b1=.05; m=1000x",
    "caveat": "Conservative threshold under simple correction"
  },
  {
    "id": "prevalence",
    "unit": 7,
    "title": "Toy Bayes positive predictive value",
    "label": "Prior prevalence per 1000",
    "kind": "prevalence",
    "min": 1,
    "max": 100,
    "initial": 10,
    "step": 1,
    "formula": "PPV=Se p/[Se p+(1\u2212Sp)(1\u2212p)]",
    "caveat": "Sensitivity=.90 and specificity=.95 assumed; not clinical"
  },
  {
    "id": "penetrance",
    "unit": 7,
    "title": "Observed sample penetrance",
    "label": "Affected among 20 ascertained adult carriers",
    "kind": "penetrance",
    "min": 0,
    "max": 20,
    "initial": 16,
    "step": 1,
    "formula": "Observed proportion=affected/20",
    "caveat": "Selected sample, not population risk"
  },
  {
    "id": "doublets",
    "unit": 8,
    "title": "Barcode doublet-flag percentage",
    "label": "Suspected doublets among 2000 barcodes",
    "kind": "doublets",
    "min": 0,
    "max": 400,
    "initial": 100,
    "step": 10,
    "formula": "Flagged fraction = 100\u00d7x/2000",
    "caveat": "Screening statistic not a true cell identity diagnosis"
  },
  {
    "id": "metareads",
    "unit": 8,
    "title": "Compositional relative read fraction",
    "label": "Assigned reads for taxon A of 10,000",
    "kind": "metareads",
    "min": 0,
    "max": 10000,
    "initial": 2000,
    "step": 100,
    "formula": "Relative reads = x/10,000",
    "caveat": "Not absolute biomass or organism count"
  }
];


/* SimulationEngine adapter for Genomics */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof computeModel !== 'function' || typeof chart !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var models = window.GENOMICS_MODELS || [];
    var m = models.filter(function(x){ return x.unit === u; })[0] || models[0];
    if (m) {
      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.dataset.kind = m.kind;
      card.dataset.min = m.min;
      card.dataset.max = m.max;
      card.dataset.title = m.title;
      card.innerHTML = '<h4>' + m.title + '</h4>' +
        '<p class="formula"><code>' + m.formula + '</code></p>' +
        '<label>' + m.label + ':<br><input type="range" min="' + m.min + '" max="' + m.max + '" step="' + m.step + '" value="' + m.initial + '"></label>' +
        '<output style="display:block;margin:0.5rem 0;font-weight:600;color:#38bdf8;"></output>' +
        '<div class="viz"></div>' +
        '<p class="readout">' + (m.caveat || '') + '</p>';
      host.appendChild(card);
      var slider = card.querySelector('input[type="range"]');
      var out = card.querySelector('output');
      var viz = card.querySelector('.viz');
      var update = function() {
        var x = Number(slider.value), y = computeModel(m.kind, x);
        out.textContent = 'Input ' + fmt(x) + ' → ' + fmt(y) + ' ' + (unitLabels[m.kind] || '');
        viz.innerHTML = chart(m, x);
      };
      slider.addEventListener('input', update);
      update();
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

