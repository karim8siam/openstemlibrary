import asyncio
import json
import glob
import os
from playwright.async_api import async_playwright

async def audit():
    html_files = sorted([f for f in glob.glob('*.html') if f not in ['index.html', 'about.html', 'privacy.html', 'terms.html']])
    print(f"Total textbook HTML files to audit: {len(html_files)}")
    
    results = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1200, 'height': 800})
        page = await context.new_page()
        
        for idx, book_file in enumerate(html_files):
            url = f'http://localhost:4242/{book_file}'
            book_errors = []
            
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=8000)
                await page.wait_for_selector('.unit-nav-item', timeout=5000)
                # Wait for initial renderMath
                await page.wait_for_timeout(350)
                
                nav_items = page.locator('.unit-nav-item')
                units_count = await nav_items.count()
                
                for u in range(units_count):
                    if u > 0:
                        await nav_items.nth(u).dispatch_event('click')
                        await page.wait_for_timeout(350)
                    
                    unit_issues = await page.evaluate(r'''() => {
                        const issues = [];
                        
                        // 1. Katex errors
                        document.querySelectorAll('.katex-error').forEach(e => {
                            issues.push({
                                type: 'katex-error',
                                title: e.getAttribute('title') || 'KaTeX error',
                                text: e.textContent.slice(0, 150)
                            });
                        });
                        
                        // 2. Unrendered math-display
                        document.querySelectorAll('.math-display').forEach(md => {
                            if (!md.querySelector('.katex')) {
                                issues.push({
                                    type: 'unrendered-math-display',
                                    text: md.textContent.trim().slice(0, 150)
                                });
                            }
                        });
                        
                        // 3. Raw LaTeX syntax outside .katex (e.g. \frac, \begin, \alpha, \beta, etc.)
                        const article = document.querySelector('.chapter-article') || document.body;
                        const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, {
                            acceptNode: function(node) {
                                let p = node.parentElement;
                                while (p) {
                                    if (p.classList && (p.classList.contains('katex') || p.classList.contains('katex-html') || p.classList.contains('inline-simulation-wrapper'))) {
                                        return NodeFilter.FILTER_REJECT;
                                    }
                                    if (['SCRIPT', 'STYLE', 'CODE', 'PRE'].includes(p.tagName)) {
                                        return NodeFilter.FILTER_REJECT;
                                    }
                                    p = p.parentElement;
                                }
                                return NodeFilter.FILTER_ACCEPT;
                            }
                        });
                        
                        let node;
                        const brokenRegex = /\\(?:frac|sqrt|partial|sum|int|begin|end|alpha|beta|gamma|delta|lambda|mu|sigma|omega|theta|phi|psi|nabla|approx|infty|cdot|times|le|ge|ne|in|to)\b|\$\$|\\\[|\\\]|[\x00-\x08\x0b\x0c\x0e-\x1f]/;
                        while (node = walker.nextNode()) {
                            const val = node.nodeValue;
                            if (brokenRegex.test(val)) {
                                issues.push({
                                    type: 'broken-text-or-math',
                                    text: val.trim().slice(0, 150),
                                    parentTag: node.parentElement ? node.parentElement.tagName : 'UNKNOWN'
                                });
                            }
                        }
                        
                        return issues;
                    }''')
                    
                    if unit_issues:
                        for iss in unit_issues:
                            iss['unit'] = u + 1
                        book_errors.extend(unit_issues)
                        
            except Exception as e:
                book_errors.append({'type': 'page-load-exception', 'error': str(e), 'unit': 0})
            
            if book_errors:
                print(f"[{idx+1}/{len(html_files)}] ❌ {book_file}: {len(book_errors)} issues found!", flush=True)
                for err in book_errors[:5]:
                    detail = err.get('title') or err.get('text') or err.get('error')
                    print(f"     Unit {err.get('unit')}: [{err['type']}] {detail}", flush=True)
                results[book_file] = book_errors
            else:
                print(f"[{idx+1}/{len(html_files)}] ✅ {book_file}: Clean", flush=True)
        
        await browser.close()
        
    with open('audit_results.json', 'w', encoding='utf-8') as fp:
        json.dump(results, fp, indent=2)
    print(f"\n==========================================", flush=True)
    print(f"Audit complete! {len(results)} books have issues out of {len(html_files)} books.", flush=True)
    print(f"Results written to audit_results.json", flush=True)
    print(f"==========================================", flush=True)

if __name__ == '__main__':
    asyncio.run(audit())
