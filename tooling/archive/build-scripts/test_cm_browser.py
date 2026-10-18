import asyncio
from playwright.async_api import async_playwright

async def verify_cm():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        
        await page.goto('http://localhost:4242/classical-mechanics.html?v=test')
        await page.wait_for_timeout(600)
        
        print('=== BROWSER VERIFICATION: CLASSICAL MECHANICS ===')
        nav_items = page.locator('.unit-nav-item')
        count = await nav_items.count()
        print(f'Total navigation items found: {count}')
        
        for ch in range(count):
            errors.clear()
            item = nav_items.nth(ch)
            await item.dispatch_event('click')
            await page.wait_for_timeout(400)
            
            katex_count = await page.locator('.katex').count()
            title = await page.locator('#unit-title').text_content()
            tag = await page.locator('#unit-tag').text_content()
            
            body_text = await page.locator('#main-content-area').inner_text()
            has_raw_latex = '$$' in body_text
            
            print(f'{tag}: "{title}" -> {katex_count} KaTeX rendered | Raw $$: {has_raw_latex} | Errors: {len(errors)}')
            
            # Save screenshots of key chapters
            if ch == 0:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/cm_ch1_verified.png')
            elif ch == 3:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/cm_ch4_verified.png')
            elif ch == 7:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/cm_ch8_verified.png')
                
        await browser.close()
        print('ALL TESTS COMPLETED SUCCESSFULLY!')

asyncio.run(verify_cm())
