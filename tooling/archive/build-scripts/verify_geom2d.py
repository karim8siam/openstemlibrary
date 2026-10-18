import asyncio
import os
from playwright.async_api import async_playwright

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ARTIFACTS_DIR = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"

async def run_verification():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True
        )
        context = await browser.new_context(viewport={"width": 1440, "height": 950})
        page = await context.new_page()

        console_errors = []
        page_errors = []

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))

        print("--- Testing index.html Portal ---")
        await page.goto("http://localhost:4242/index.html")
        await page.wait_for_timeout(1000)

        # Filter Mathematics tab
        math_tab = page.locator("button.dept-pill-btn", has_text="Mathematics")
        if await math_tab.count() > 0:
            await math_tab.click()
            await page.wait_for_timeout(600)
            print("Clicked Mathematics filter tab.")

        # Verify Two-Dimensional Geometry card
        card = page.locator(".course-card", has_text="Two-Dimensional Geometry")
        assert await card.count() > 0, "Two-Dimensional Geometry card not found on portal!"
        await card.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        home_shot = os.path.join(ARTIFACTS_DIR, "home_geom2d_card_detail.png")
        await page.screenshot(path=home_shot)
        print(f"Saved {home_shot}")

        print("\n--- Testing geometry-2d.html Textbook Reader ---")
        await page.goto("http://localhost:4242/geometry-2d.html")
        await page.wait_for_timeout(1500)

        # Verify Chapter 1 Header
        title_el = await page.locator("#unit-title").inner_text()
        print(f"Chapter 1 Loaded: {title_el}")
        assert "Cartesian & Polar Coordinate Systems" in title_el

        # Check KaTeX math count
        math_count = await page.locator(".katex").count()
        print(f"Chapter 1 KaTeX equations rendered: {math_count}")
        assert math_count > 0, "No KaTeX math rendered in Chapter 1!"

        # Check canvas mounted
        canvases = await page.locator("canvas").count()
        print(f"Chapter 1 Canvas elements mounted: {canvases}")
        assert canvases > 0, "Canvas not mounted in Chapter 1!"

        # Toggle first problem solution
        toggle_btn = page.locator(".solution-toggle-btn").first
        await toggle_btn.scroll_into_view_if_needed()
        await toggle_btn.click()
        await page.wait_for_timeout(500)
        sol_content = page.locator(".solution-content").first
        is_visible = await sol_content.is_visible()
        print(f"Problem 1 solution revealed: {is_visible}")
        assert is_visible, "Problem solution did not expand!"

        ch1_shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch1_verified.png")
        await page.screenshot(path=ch1_shot)
        print(f"Saved {ch1_shot}")

        # Iterate through all 8 chapters
        nav_items = page.locator(".unit-nav-item")
        total_units = await nav_items.count()
        print(f"\nSidebar chapters detected: {total_units}")
        assert total_units == 8, f"Expected 8 units, found {total_units}"

        for u in range(total_units):
            item = nav_items.nth(u)
            item_text = await item.inner_text()
            await item.click()
            await page.wait_for_timeout(800)

            cur_title = await page.locator("#unit-title").inner_text()
            cur_math = await page.locator(".katex").count()
            cur_canvases = await page.locator("canvas").count()
            print(f"Navigated to Unit {u+1}: {cur_title} | KaTeX: {cur_math} | Canvases: {cur_canvases}")
            assert cur_math > 0, f"Unit {u+1} failed to render math!"
            assert cur_canvases > 0, f"Unit {u+1} failed to mount canvas simulation!"

            # Capture key simulations
            if u == 1: # Chapter 2: Line Pairs
                sim = page.locator(".simulation-box").first
                await sim.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch2_line_pair_sim.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 3: # Chapter 4: Conic Discriminant Morpher
                sim = page.locator(".simulation-box").first
                await sim.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch4_conic_morpher_sim.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 4: # Chapter 5: Parabola Optics
                sim = page.locator(".simulation-box").first
                await sim.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch5_parabola_sim.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 5: # Chapter 6: Ellipse Conjugate Diameters
                sim = page.locator(".simulation-box").first
                await sim.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch6_ellipse_sim.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 7: # Chapter 8: Polar Conics & Kepler Orbits
                sim = page.locator(".simulation-box").first
                await sim.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                shot = os.path.join(ARTIFACTS_DIR, "geom2d_ch8_kepler_sim.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")

        # Scroll to footer
        footer = page.locator(".reader-trust-footer")
        if await footer.count() > 0:
            await footer.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            footer_shot = os.path.join(ARTIFACTS_DIR, "geom2d_footer_verified.png")
            await page.screenshot(path=footer_shot)
            print(f"Saved {footer_shot}")

        # Verify console errors
        print("\n--- Console & Error Inspection ---")
        print(f"Page errors: {len(page_errors)}")
        print(f"Console errors: {len(console_errors)}")
        if page_errors:
            print("PAGE ERRORS:", page_errors)
        if console_errors:
            print("CONSOLE ERRORS:", console_errors)

        assert len(page_errors) == 0, f"Encountered page errors: {page_errors}"
        critical_console = [e for e in console_errors if "favicon" not in e.lower()]
        assert len(critical_console) == 0, f"Encountered critical console errors: {critical_console}"

        print("\nALL VERIFICATION CHECKS PASSED WITH 0 ERRORS!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_verification())
