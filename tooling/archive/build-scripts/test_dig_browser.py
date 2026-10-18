import asyncio
from playwright.async_api import async_playwright

async def verify_digital_electronics():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        
        await page.goto('http://localhost:4242/digital-electronics.html?v=test')
        await page.wait_for_timeout(800)
        
        print('=== BROWSER VERIFICATION: DIGITAL ELECTRONICS ===')
        nav_items = page.locator('.unit-nav-item')
        count = await nav_items.count()
        print(f'Total navigation items found: {count}')
        
        assert count == 8, f"Expected 8 units, found {count}"
        
        total_katex = 0
        total_sims = 0
        total_probs = 0

        for ch in range(count):
            errors.clear()
            item = nav_items.nth(ch)
            await item.dispatch_event('click')
            await page.wait_for_timeout(600)
            
            katex_count = await page.locator('.katex').count()
            title = await page.locator('#unit-title').text_content()
            tag = await page.locator('#unit-tag').text_content()
            
            body_text = await page.locator('#main-content-area').inner_text()
            has_raw_latex = '$$' in body_text
            
            canvas_count = await page.locator('canvas').count()
            prob_count = await page.locator('.problem-card').count()

            total_katex += katex_count
            total_sims += canvas_count
            total_probs += prob_count
            
            print(f'{tag}: "{title}" -> {katex_count} KaTeX rendered | Canvas sims: {canvas_count} | Problems: {prob_count} | Raw $$: {has_raw_latex} | Errors: {len(errors)}')
            
            if len(errors) > 0:
                print(f"ERRORS ENCOUNTERED in chapter {ch+1}: {errors}")
            assert len(errors) == 0, f"Encountered errors: {errors}"
            assert katex_count > 10, f"Expected formulas, got {katex_count}"
            assert not has_raw_latex, f"Found unrendered $$ in chapter {ch+1}"
            
            # Save screenshots of all 8 chapters
            await page.screenshot(path=f'/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/dig_ch{ch+1}_verified.png')

        print(f'\nTotal KaTeX across 8 chapters: {total_katex} | Total Sims: {total_sims} | Total Solved Problems: {total_probs}')
        assert total_sims == 16, f"Expected 16 simulations, found {total_sims}"
        assert total_probs == 24, f"Expected 24 solved problems, found {total_probs}"

        # Now verify homepage catalog integration
        print('\n=== BROWSER VERIFICATION: HOMEPAGE CATALOG ===')
        errors.clear()
        await page.goto('http://localhost:4242/index.html?v=test')
        await page.wait_for_timeout(600)
        
        # Check initial cards and See More button
        see_more_btn = page.locator('.btn-see-more[data-dept="physics"]')
        btn_visible = await see_more_btn.is_visible()
        print(f'Physics See More button visible: {btn_visible}')
        assert btn_visible, "Expected Physics See More button to be visible since it has 14 courses (>6)"
        
        btn_text = await see_more_btn.inner_text()
        print(f'Initial button text: "{btn_text}"')
        assert "+8 More" in btn_text, f"Expected '+8 More' in text, got: {btn_text}"
        
        # Click to expand
        await see_more_btn.click()
        await page.wait_for_timeout(400)
        btn_text_after = await see_more_btn.inner_text()
        print(f'Button text after expand: "{btn_text_after}"')
        assert "Show Fewer" in btn_text_after, f"Expected 'Show Fewer' in text, got: {btn_text_after}"
            
        # Verify Digital Electronics card exists and is visible
        dig_card = page.locator('#grid-physics a[href="digital-electronics.html"]').first
        dig_card_visible = await dig_card.is_visible()
        print(f'Digital Electronics link visible after expanding: {dig_card_visible}')
        assert dig_card_visible, "Digital Electronics card should be visible after expanding"
        
        await dig_card.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await page.screenshot(path='/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/home_dig_card_verified.png')
        
        await browser.close()
        print('\nALL 8 CHAPTERS + HOMEPAGE PASSED 100% PERFECT VERIFICATION!')

asyncio.run(verify_digital_electronics())
