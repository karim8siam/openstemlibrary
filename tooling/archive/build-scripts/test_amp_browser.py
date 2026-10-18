import asyncio
from playwright.async_api import async_playwright

async def verify_amp():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        
        await page.goto('http://localhost:4242/atomic-molecular-physics.html?v=test')
        await page.wait_for_timeout(800)
        
        print('=== BROWSER VERIFICATION: ATOMIC & MOLECULAR PHYSICS ===')
        nav_items = page.locator('.unit-nav-item')
        count = await nav_items.count()
        print(f'Total navigation items found: {count}')
        
        assert count == 6, f"Expected 6 units, found {count}"
        
        for ch in range(count):
            errors.clear()
            item = nav_items.nth(ch)
            await item.dispatch_event('click')
            await page.wait_for_timeout(500)
            
            katex_count = await page.locator('.katex').count()
            title = await page.locator('#unit-title').text_content()
            tag = await page.locator('#unit-tag').text_content()
            
            body_text = await page.locator('#main-content-area').inner_text()
            has_raw_latex = '$$' in body_text
            
            canvas_count = await page.locator('canvas').count()
            prob_count = await page.locator('.problem-card').count()
            
            print(f'{tag}: "{title}" -> {katex_count} KaTeX rendered | Canvas sims: {canvas_count} | Problems: {prob_count} | Raw $$: {has_raw_latex} | Errors: {len(errors)}')
            
            if len(errors) > 0:
                print(f"ERRORS ENCOUNTERED: {errors}")
            assert len(errors) == 0, f"Encountered errors: {errors}"
            assert katex_count > 10, f"Expected formulas, got {katex_count}"
            assert not has_raw_latex, f"Found unrendered $$ in chapter {ch+1}"
            
            # Save screenshots of key chapters
            if ch == 0:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/amp_ch1_verified.png')
            elif ch == 1:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/amp_ch2_verified.png')
            elif ch == 3:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/amp_ch4_verified.png')
            elif ch == 4:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/amp_ch5_verified.png')
            elif ch == 5:
                await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/amp_ch6_verified.png')

        # Now verify homepage catalog integration
        print('\n=== BROWSER VERIFICATION: HOMEPAGE CATALOG ===')
        errors.clear()
        await page.goto('http://localhost:4242/index.html?v=test')
        await page.wait_for_timeout(600)
        
        # Check initial cards and See More button
        see_more_btn = page.locator('.btn-see-more[data-dept="physics"]')
        btn_visible = await see_more_btn.is_visible()
        print(f'Physics See More button visible: {btn_visible}')
        assert btn_visible, "Expected Physics See More button to be visible since it has 11 courses (>6)"
        
        btn_text = await see_more_btn.inner_text()
        print(f'Initial button text: "{btn_text}"')
        assert "+5 More" in btn_text, f"Expected '+5 More' in text, got: {btn_text}"
        
        # Click to expand
        await see_more_btn.click()
        await page.wait_for_timeout(400)
        btn_text_after = await see_more_btn.inner_text()
        print(f'Button text after expand: "{btn_text_after}"')
        assert "Show Fewer" in btn_text_after, f"Expected 'Show Fewer' in text, got: {btn_text_after}"
            
        # Verify Atomic & Molecular Physics card exists and is visible
        amp_card = page.locator('a[href="atomic-molecular-physics.html"]').first
        amp_card_visible = await amp_card.is_visible()
        print(f'Atomic & Molecular Physics link visible after expanding: {amp_card_visible}')
        assert amp_card_visible, "Atomic & Molecular Physics card should be visible after expanding"
        
        await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/home_amp_verified.png')
        
        await browser.close()
        print('\nALL 6 CHAPTERS + HOMEPAGE PASSED 100% PERFECT VERIFICATION!')

asyncio.run(verify_amp())
