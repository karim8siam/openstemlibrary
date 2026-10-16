/* Generate crawlable chapter pages from unchanged course data and the shared renderer.
   Setup: npm install --prefix tooling jsdom@26.1.0
   Run: node tooling/build-library.cjs */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');
const root = path.resolve(__dirname, '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const changedPages = new Set();
const write = (file, text) => {
  const target = path.join(root, file);
  if (!fs.existsSync(target) || fs.readFileSync(target, 'utf8') !== text) {
    if (file.endsWith('.html')) changedPages.add(file);
    fs.writeFileSync(target, text);
  }
};
const publicationDate = new Intl.DateTimeFormat('en-CA', {timeZone:'Asia/Dhaka',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
const version = '20261016_review_fix';
const portalVersion = crypto.createHash('sha256').update(['departments-data.js','portal.js','portal.css'].map(read).join('\n')).digest('hex').slice(0,16);
const context = { window: {} }; vm.createContext(context);
vm.runInContext(read('departments-data.js'), context);
const departments = context.window.LIBRARY_CATALOG.departments.filter(d => d.courses.some(c => c.status === 'AVAILABLE'));
const books = departments.flatMap(d => d.courses.filter(c => c.status === 'AVAILABLE'));
const controller = read('app.js').split('\nif (document.readyState === "loading")')[0];
function prepare(html, filename, book, index) {
  const dom = new JSDOM(html, { url: `https://openstemlibrary.com/${filename.replace(/\.html$/, '')}`, runScripts: 'outside-only' });
  const w = dom.window, doc = w.document;
  w.setTimeout = () => 0; w.scrollTo = () => {};
  doc.body.dataset.bookPath = book.url;
  doc.body.dataset.chapterIndex = String(index);
  doc.querySelector('link[rel="canonical"]').href = `https://openstemlibrary.com/${filename.replace(/\.html$/, '')}`;
  for (const el of doc.querySelectorAll('meta[property="og:url"]')) el.content = `https://openstemlibrary.com/${filename.replace(/\.html$/, '')}`;
  for (const el of doc.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const value = el.getAttribute(attr);
    if (/^(app\.js|styles\.css)(\?|$)/.test(value)) el.setAttribute(attr, value.split('?')[0] + '?v=' + version);
  }
  // Normalize older and newer reader wrappers without changing their content.
  if (!doc.getElementById('problems-mount') && !doc.getElementById('problems-container') && !doc.getElementById('problem-cards-list')) {
    const problems = doc.createElement('div'); problems.id = 'problems-mount';
    const sections = doc.getElementById('textbook-sections');
    sections.querySelectorAll('.problem-card').forEach(card => problems.append(card));
    sections.after(problems);
  }
  for (const link of doc.querySelectorAll('a[href="algebra-trigonometry.html"]')) link.setAttribute('href', 'basic-algebra.html');
  for (const link of doc.querySelectorAll('a[href="quantum-mechanics-1.html"]')) link.setAttribute('href', 'reader.html');
  for (const link of doc.querySelectorAll('a[href="special-relativity.html"],a[href="general-relativity.html"]')) link.remove();
  for (const script of doc.querySelectorAll('script[type="application/ld+json"]')) {
    script.textContent = script.textContent.replaceAll('https://openstemlibrary.org/', 'https://openstemlibrary.com/');
    const legacy = {
      'https://openstemlibrary.com/physics/quantum-mechanics': 'reader.html',
      'https://openstemlibrary.com/physics/mechanics': 'mechanics.html',
      'https://openstemlibrary.com/physics/electrodynamics': 'electrodynamics.html',
      'https://openstemlibrary.com/physics/optics': 'optics.html',
      'https://openstemlibrary.com/physics/statistical-mechanics': 'statistical-mechanics.html',
      'https://openstemlibrary.com/physics/properties-of-matter': 'properties-of-matter.html',
      'https://openstemlibrary.com/physics/electricity-and-magnetism': 'electricity-magnetism.html',
      'https://openstemlibrary.com/physics/thermal-physics': 'thermal-physics.html'
    };
    for (const [old, target] of Object.entries(legacy)) script.textContent = script.textContent.replaceAll(old, 'https://openstemlibrary.com/'+target);
    script.textContent = script.textContent.replace(/https:\/\/openstemlibrary\.com\/([a-z0-9-]+)\.html/g, 'https://openstemlibrary.com/$1');
  }
  for (const link of doc.querySelectorAll('a[href]')) {
    const href=link.getAttribute('href');
    if (!/^(https?:|mailto:|#)/.test(href)) link.setAttribute('href',href.replace(/\.html(?=[?#]|$)/,''));
  }
  // Presentation text must not imply Google approval while review is pending.
  for (const el of doc.querySelectorAll('.reader-trust-copy')) {
    el.textContent = el.textContent.replace('Google AdSense Certified Academic Publisher', 'Free Open-Access Academic Library').replace('Peer-Reviewed University Textbooks', 'Interactive University Study Resources');
  }
  const dataScript = [...doc.querySelectorAll('script[src]')].map(el => el.getAttribute('src').split('?')[0]).find(src => /(?:-data|course-data)\.js$/.test(src));
  if (!dataScript) throw Error(`No course data for ${book.url}`);
  w.eval(read(dataScript));
  return {dom, w, doc};
}
function chapterUrl(book, index) { return index === 0 ? book.url.replace(/\.html$/, '') : book.url.replace(/\.html$/, `-chapter-${index+1}`); }
function navigation(doc, book, units, selected) {
  const list = doc.getElementById('unit-nav-list');
  if (!list) throw Error(`No chapter list: ${book.url}`);
  list.innerHTML = '';
  units.forEach((unit, index) => {
    const li = doc.createElement('li'); li.className = 'unit-nav-item' + (selected === index ? ' active' : '');
    li.dataset.unitIndex = index;
    const a = doc.createElement('a'); a.href = chapterUrl(book, index); a.className = 'unit-nav-link';
    if (index === selected) a.setAttribute('aria-current', 'page');
    const num = doc.createElement('span'); num.className = 'unit-nav-num'; num.textContent = 'Ch.'+(unit.number || unit.unitNumber || index+1);
    const text = doc.createElement('span'); text.className = 'unit-nav-text'; text.textContent = unit.title;
    a.append(num,text); li.append(a); list.append(li);
  });
  doc.querySelectorAll('.chapter-pagination').forEach(el => el.remove());
  const nav = doc.createElement('nav'); nav.className = 'chapter-pagination'; nav.setAttribute('aria-label','Chapter navigation');
  for (const [index, label] of [[selected-1,'← Previous chapter'],[0,'Book contents'],[selected+1,'Next chapter →']]) {
    if (index < 0 || index >= units.length || (label === 'Book contents' && selected === 0)) continue;
    const a = doc.createElement('a'); a.href = chapterUrl(book,index); a.textContent = label; nav.append(a);
  }
  (doc.querySelector('.reader-main-column,.chapter-article') || doc.querySelector('main')).append(nav);
}
let generated = 0;
const chapterPaths = [];
async function build() {
for (const book of books.filter(book => !process.env.OPENSTEM_BOOK || book.id === process.env.OPENSTEM_BOOK)) {
  if (process.env.OPENSTEM_HOMEPAGE_ONLY === '1') continue;
  const original = read(book.url);
  const base = prepare(original,book.url,book,0);
  const units = base.w.COURSE_DATA.units;
  if (!Array.isArray(units) || !units.length) throw Error(`Empty course: ${book.url}`);
  navigation(base.doc,book,units,0);
  // The legacy Quantum Mechanics landing page contained nested duplicate
  // sections and an empty worked-problem mount. Rebuild from its course data.
  if (book.url === 'reader.html') {
    base.doc.querySelectorAll('.textbook-section-card,.problem-card').forEach(el => el.remove());
    base.doc.getElementById('textbook-sections').innerHTML = '';
    base.w.eval(controller); base.w.startApp();
    base.doc.getElementById('unit-title').textContent = units[0].title;
    base.doc.getElementById('unit-desc').textContent = units[0].leadSummary || units[0].description || '';
    base.doc.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
    base.doc.querySelector('.sidebar')?.removeAttribute('id');
    navigation(base.doc, book, units, 0);
  }
  write(book.url,base.dom.serialize().replace(/^[ \t]+$/gm, ''));
  base.w.close();
  for (let index=1; index<units.length; index++) {
    const filename = chapterUrl(book,index)+'.html';
    const {dom,w,doc} = prepare(original,filename,book,index);
    // Render using the existing application functions; no textbook rewriting.
    doc.querySelectorAll('.textbook-section-card,.problem-card').forEach(el=>el.remove());
    doc.getElementById('textbook-sections').innerHTML = '';
    w.eval(controller); w.startApp();
    doc.getElementById('unit-title').textContent = units[index].title;
    doc.getElementById('unit-tag').textContent = `Chapter ${units[index].number || units[index].unitNumber || index+1} • Theory & Derivations`;
    doc.getElementById('unit-desc').textContent = units[index].leadSummary || units[index].description || '';
    doc.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el=>el.remove());
    doc.querySelector('.sidebar')?.removeAttribute('id');
    navigation(doc,book,units,index);
    doc.title = `${units[index].title} | ${book.title} | OpenSTEM Library`;
    const summary = units[index].leadSummary || units[index].description || '';
    if (summary) doc.querySelector('meta[name="description"]').content = summary;
    if (book.id === 'introduction-to-statistics' || book.id === 'probability-and-probability-distributions') {
      for (const selector of ['meta[property="og:title"]','meta[name="twitter:title"]']) doc.querySelector(selector).content = doc.title;
      for (const selector of ['meta[property="og:description"]','meta[name="twitter:description"]']) doc.querySelector(selector).content = summary;
    }
    for (const script of doc.querySelectorAll('script[type="application/ld+json"]')) {
      try {
        const data = JSON.parse(script.textContent);
        const update = node => {
          if (!node || typeof node !== 'object') return;
          if (node.url === `https://openstemlibrary.com/${book.url.replace(/\.html$/, '')}`) node.url = `https://openstemlibrary.com/${filename.replace(/\.html$/, '')}`;
          if (node['@type'] === 'Book' || node['@type'] === 'LearningResource') node.name = `${book.title}: ${units[index].title}`;
          if (book.id === 'probability-and-probability-distributions' && node['@type'] === 'BreadcrumbList') {
            const last=node.itemListElement?.at(-1);
            if(last){last.name=units[index].title;last.item=`https://openstemlibrary.com/${filename.replace(/\.html$/, '')}`;}
          }
          Object.values(node).forEach(v => { if (Array.isArray(v)) v.forEach(update); else if (v && typeof v === 'object') update(v); });
        };
        update(data); script.textContent = JSON.stringify(data);
      } catch {}
    }
    write(filename,dom.serialize()); chapterPaths.push(filename); generated++; w.close();
    await new Promise(setImmediate);
    if (global.gc) global.gc();
  }
}
// Keep the homepage readable and usable even before JavaScript runs.
let home = read('index.html');
home = home.replace(/The library currently hosts \d+ comprehensive university courses/g,`The library currently hosts ${books.length} comprehensive university courses`);
home = home.replace(/Live Now • \d+ Textbooks/g,`Live Now • ${books.length} Textbooks`).replace(/Explore \d+ Live Textbooks/g,`Explore ${books.length} Live Textbooks`);
home = home.replace('Protected reader interface. Google AdSense compliant open-access academic library.','Free open-access academic library.');
const homeDom = new JSDOM(home, {url:'https://openstemlibrary.com/',runScripts:'outside-only'});
const hw=homeDom.window, hd=hw.document;
hw.eval(read('departments-data.js')); hw.eval(read('portal.js')); hd.dispatchEvent(new hw.Event('DOMContentLoaded'));
let entries=hd.querySelector('.department-entry-grid');
if (!entries) { entries=hd.createElement('nav'); entries.className='department-entry-grid'; entries.setAttribute('aria-label','Browse departments'); hd.querySelector('.hero-section').append(entries); }
entries.innerHTML='';
for(const dept of departments) {
  const a=hd.createElement('a'); a.className='department-entry'; a.href='#dept-'+dept.id;
  const label=hd.createElement('strong'); label.textContent=dept.icon+' '+dept.name;
  const availableCount=dept.courses.filter(c=>c.status==='AVAILABLE').length;
  const count=hd.createElement('span'); count.textContent=availableCount+(availableCount===1?' book →':' books →');
  a.append(label,count); entries.append(a);
  [...hd.querySelectorAll('.footer-link')].filter(a=>a.textContent.trim()===dept.name+' Department').forEach(a=>a.href='#dept-'+dept.id);
}
for(const el of hd.querySelectorAll('script[src],link[rel="stylesheet"]')) {
  const attr=el.tagName==='SCRIPT'?'src':'href', value=el.getAttribute(attr);
  if (/^(departments-data\.js|portal\.js|portal\.css)(\?|$)/.test(value)) el.setAttribute(attr,value.split('?')[0]+'?v='+portalVersion);
}
const description='Free university textbooks in Physics, Mathematics, Chemistry, and Statistics & Probability, with solved problems and interactive simulations.';
for (const selector of ['meta[name="description"]','meta[property="og:description"]','meta[name="twitter:description"]']) hd.querySelector(selector).content=description;
hd.querySelector('#portal-search-input').placeholder='Search by topic or course (e.g., Statistics, Regression, Calculus, Quantum Mechanics)...';
// New books belong in the department catalog; do not recreate announcement boxes.
hd.querySelectorAll('.latest-textbook').forEach(el=>el.remove());
const departmentFooter=hd.querySelector('a.footer-link[href="#dept-physics"]')?.parentElement;
if(departmentFooter){
  departmentFooter.querySelectorAll('a[href^="#dept-"]').forEach(a=>a.remove());
  for(const dept of [...departments].reverse()){
    const a=hd.createElement('a'); a.className='footer-link'; a.href='#dept-'+dept.id; a.textContent=dept.name+' Department'; departmentFooter.prepend(a);
  }
}
const footerLinks=hd.querySelector('.portal-footer .footer-links') || hd.querySelector('footer .footer-links');
if(footerLinks && !hd.querySelector('.footer-book-directory')) {
  const details=hd.createElement('details'); details.className='footer-book-directory';
  const summary=hd.createElement('summary'); summary.textContent=`Browse all ${books.length} textbooks`;
  const bookLinks=hd.createElement('div'); bookLinks.className='footer-links';
  [...footerLinks.querySelectorAll('a')].filter(a=>books.some(b=>b.url.replace(/\.html$/, '')===a.getAttribute('href').replace(/\.html$/, ''))).forEach(a=>bookLinks.append(a));
  details.append(summary,bookLinks); footerLinks.before(details);
}
const directory = hd.querySelector('.footer-book-directory');
if (directory) {
  directory.querySelector('summary').textContent = `Browse all ${books.length} textbooks`;
  const links = directory.querySelector('.footer-links');
  links.innerHTML = '';
  for (const book of books) {
    const a=hd.createElement('a'); a.className='footer-link'; a.href=book.url.replace(/\.html$/, ''); a.textContent=book.title; links.append(a);
  }
}
for (const link of hd.querySelectorAll('a[href]')) { const href=link.getAttribute('href'); if(!/^(https?:|mailto:|#)/.test(href)) link.setAttribute('href',href.replace(/\.html(?=[?#]|$)/,'')); }
hd.querySelector('link[rel="canonical"]').href='https://openstemlibrary.com/';
write('index.html',homeDom.serialize().replace(/^[ \t]+$/gm,'')); hw.close();
// All chapter URLs are explicit, crawlable links and sitemap entries.
const sitemapDom = new JSDOM(read('sitemap.xml'),{contentType:'text/xml'});
const sd=sitemapDom.window.document, ns='http://www.sitemaps.org/schemas/sitemap/0.9';
for (const loc of sd.querySelectorAll('loc')) loc.textContent = loc.textContent.replace(/\.html$/, '');
const existing = new Set([...sd.querySelectorAll('loc')].map(n=>n.textContent));
for(const filename of [...books.map(b=>b.url), ...chapterPaths]) {
  const url='https://openstemlibrary.com/'+filename.replace(/\.html$/, '');
  if(existing.has(url)) continue;
  const node=sd.createElementNS(ns,'url'), loc=sd.createElementNS(ns,'loc'), mod=sd.createElementNS(ns,'lastmod');
  loc.textContent=url; mod.textContent=publicationDate; node.append(loc,mod); sd.documentElement.append(node); existing.add(url);
}
for(const entry of sd.querySelectorAll('url')) {
  const loc=entry.querySelector('loc')?.textContent;
  const file=loc==='https://openstemlibrary.com/'?'index.html':loc?.replace('https://openstemlibrary.com/','')+'.html';
  if(changedPages.has(file)) {
    let mod=entry.querySelector('lastmod');
    if(!mod){mod=sd.createElementNS(ns,'lastmod');entry.append(mod);}
    mod.textContent=publicationDate;
  }
}
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n'+sd.documentElement.outerHTML+'\n');
sitemapDom.window.close();
console.log(JSON.stringify({books:books.length,generatedChapterPages:generated}));

process.exit(0);
}
build().catch(err=>{console.error(err);process.exit(1)});
