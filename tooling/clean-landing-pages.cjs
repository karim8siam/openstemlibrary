const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const catalogCtx = { window: {} };
vm.createContext(catalogCtx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), catalogCtx);
const departments = catalogCtx.window.LIBRARY_CATALOG.departments;

const targetDepts = ['materials-science-and-engineering', 'earth-space-sciences'];

for (const deptId of targetDepts) {
  const dept = departments.find(d => d.id === deptId);
  if (!dept) continue;
  const deptDir = path.join(groupedRoot, deptId);
  if (!fs.existsSync(deptDir)) continue;

  for (const bookFolder of fs.readdirSync(deptDir)) {
    const landingHtmlPath = path.join(deptDir, bookFolder, `${bookFolder}.html`);
    if (!fs.existsSync(landingHtmlPath)) continue;

    const courseMeta = dept.courses.find(c => c.id === bookFolder);
    const content = fs.readFileSync(landingHtmlPath, 'utf8');
    const dom = new JSDOM(content);
    const doc = dom.window.document;

    // 1. Remove statistical simulation stylesheet
    doc.querySelectorAll('link[href*="statistical-simulation-and-monte-carlo-methods.css"]').forEach(el => el.remove());

    // 2. Set brand title
    const brandTitle = doc.querySelector('.brand-title');
    if (brandTitle && courseMeta && courseMeta.title) {
      brandTitle.textContent = courseMeta.title;
    }

    // 3. Set badge course
    const badgeCourse = doc.querySelector('.badge-course');
    if (badgeCourse) {
      badgeCourse.textContent = dept.name;
    }

    // 4. Set breadcrumbs
    doc.querySelectorAll('script[type="application/ld+json"]').forEach(script => {
      try {
        const data = JSON.parse(script.textContent);
        if (data['@type'] === 'BreadcrumbList' && Array.isArray(data.itemListElement)) {
          const deptItem = data.itemListElement.find(item => item.position === 2);
          if (deptItem) {
            deptItem.name = dept.name;
            deptItem.item = `https://openstemlibrary.com/#dept-${dept.id}`;
          }
          const bookItem = data.itemListElement.find(item => item.position === 3);
          if (bookItem && courseMeta) {
            bookItem.name = courseMeta.title;
            bookItem.item = `https://openstemlibrary.com/${bookFolder}`;
          }
          script.textContent = JSON.stringify(data);
        }
      } catch (e) {}
    });

    fs.writeFileSync(landingHtmlPath, dom.serialize(), 'utf8');
    dom.window.close();
    console.log(`Cleaned landing page: ${deptId}/${bookFolder}`);
  }
}
console.log('All target landing pages updated.');
