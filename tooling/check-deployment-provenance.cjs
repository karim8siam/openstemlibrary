// Diagnostic, read-only comparison of immutable Pages deployment and custom domain.
'use strict';
const crypto = require('node:crypto');
const hosts = [
  'https://93c7f816.openstemlibrary.pages.dev',
  'https://openstemlibrary.com'
];
const paths = ['/', '/reader', '/calculus-1', '/calculus-1-chapter-2', '/calculus-1-data.js', '/sitemap.xml', '/tooling/README.md', '/publishing/README.md'];
(async () => {
  const output = [];
  for (const host of hosts) {
    for (const path of paths) {
      const url = host + path;
      const ctrl = new AbortController();
      const timeout = setTimeout(() => ctrl.abort(), 15000);
      try {
        const res = await fetch(url, { redirect: 'follow', signal: ctrl.signal, headers: {'User-Agent':'OpenSTEM-deployment-provenance/1.0'} });
        const body = Buffer.from(await res.arrayBuffer());
        output.push({
          url, status:res.status, finalUrl:res.url, size:body.length,
          sha256:crypto.createHash('sha256').update(body).digest('hex').slice(0,24),
          contentType:res.headers.get('content-type'), cache:res.headers.get('cf-cache-status'),
          cfRay:res.headers.get('cf-ray'), xRobotsTag:res.headers.get('x-robots-tag')
        });
      } catch (e) { output.push({url, error: String(e)}); }
      finally { clearTimeout(timeout); }
    }
  }
  console.log(JSON.stringify({checked:new Date().toISOString(), results:output},null,2));
})();