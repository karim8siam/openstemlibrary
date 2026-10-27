const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');

const mseBooks = [
  { slug: 'fundamentals-of-materials-science', title: 'Fundamentals of Materials Science' },
  { slug: 'crystallography-and-diffraction', title: 'Crystallography and Diffraction' },
  { slug: 'thermodynamics-of-materials', title: 'Thermodynamics of Materials' },
  { slug: 'diffusion-and-kinetics', title: 'Diffusion and Kinetics in Materials' },
  { slug: 'mechanical-behavior-of-solids', title: 'Mechanical Behavior of Solids' },
  { slug: 'phase-transformations', title: 'Phase Transformations' },
  { slug: 'physical-metallurgy', title: 'Physical Metallurgy' },
  { slug: 'ceramic-materials', title: 'Ceramic Materials' },
  { slug: 'polymer-science', title: 'Polymer Science and Engineering' },
  { slug: 'composite-materials', title: 'Composite Materials' },
  { slug: 'semiconductor-materials', title: 'Semiconductor Materials' },
  { slug: 'electronic-and-magnetic-materials', title: 'Electronic and Magnetic Materials' },
  { slug: 'optical-and-photonic-materials', title: 'Optical and Photonic Materials' },
  { slug: 'nanomaterials-and-surfaces', title: 'Nanomaterials and Surfaces' },
  { slug: 'biomaterials', title: 'Biomaterials' },
  { slug: 'materials-characterization', title: 'Materials Characterization' },
  { slug: 'corrosion-and-degradation', title: 'Corrosion and Degradation' },
  { slug: 'sustainable-materials-and-circularity', title: 'Sustainable Materials and Circularity' },
  { slug: 'materials-processing-and-manufacturing', title: 'Materials Processing and Manufacturing' },
  { slug: 'computational-materials-science-design-and-selection', title: 'Computational Materials Science, Design and Selection' }
];

const essBooksToClean = [
  { slug: 'seismology', title: 'Seismology' },
  { slug: 'geodesy-and-earth-observation', title: 'Geodesy and Earth Observation' },
  { slug: 'planetary-science', title: 'Planetary Science' },
  { slug: 'astrobiology', title: 'Astrobiology' },
  { slug: 'environmental-geoscience', title: 'Environmental Geoscience' }
];

function generateCleanCss(title) {
  return `/* ${title} textbook stylesheet */
@import url("styles.css?v=20261016_review_fix");

.openstem-simulation, .sim-card, .model-card {
  padding: 1.25rem;
  border: 1px solid #334155;
  border-radius: 12px;
  background: #0b1729;
  color: #e2e8f0;
  margin: 1.5rem 0;
  box-sizing: border-box;
}

.openstem-simulation h4, .sim-card h3, .sim-card h4, .model-card h3 {
  color: #38bdf8;
  margin-top: 0;
  font-size: 1.15rem;
  font-weight: 600;
}

.openstem-simulation label, .sim-card label, .model-card label {
  display: block;
  margin: 0.75rem 0;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.openstem-simulation input[type="range"], .sim-card input[type="range"], .model-card input[type="range"] {
  display: block;
  width: 100%;
  max-width: 480px;
  margin: 0.5rem 0;
  accent-color: #0284c7;
}

.openstem-simulation output, .sim-card output, .model-card output {
  font-weight: 600;
  color: #f59e0b;
  margin-left: 0.5rem;
}

.openstem-simulation p, .sim-card p, .model-card p, .model-card .note {
  color: #94a3b8;
  font-size: 0.9rem;
  line-height: 1.5;
}

.openstem-simulation button, .sim-card button, .model-card button {
  min-height: 38px;
  padding: 6px 14px;
  background: #1e293b;
  color: #f8fafc;
  border: 1px solid #475569;
  border-radius: 6px;
  cursor: pointer;
  font: inherit;
  margin-top: 0.5rem;
}

.openstem-simulation button:hover, .sim-card button:hover, .model-card button:hover {
  background: #334155;
}

.card-plot { fill: none; stroke: #38bdf8; stroke-width: 2.5; }
.card-dot { fill: #f97316; }
`;
}

console.log('Cleaning MSE CSS files...');
for (const b of mseBooks) {
  const cssPath = path.join(root, `${b.slug}.css`);
  fs.writeFileSync(cssPath, generateCleanCss(b.title), 'utf8');
  console.log(`  Updated ${b.slug}.css`);
}

console.log('Cleaning ESS CSS files...');
for (const b of essBooksToClean) {
  const cssPath = path.join(root, `${b.slug}.css`);
  fs.writeFileSync(cssPath, generateCleanCss(b.title), 'utf8');
  console.log(`  Updated ${b.slug}.css`);
}

console.log('All CSS files successfully updated to clean OpenSTEM standards.');
