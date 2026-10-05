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
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        console_errors = []
        page_errors = []

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))

        print("--- Testing index.html ---")
        await page.goto("http://localhost:4242/index.html")
        await page.wait_for_timeout(1000)

        # Check mathematics department tab
        math_tab = page.locator("button.dept-pill-btn", has_text="Mathematics")
        if await math_tab.count() > 0:
            await math_tab.click()
            await page.wait_for_timeout(600)
            print("Clicked Mathematics tab on home portal.")

        # Capture home card screenshot
        calc1_card = page.locator(".course-card", has_text="Calculus I")
        assert await calc1_card.count() > 0, "Calculus I course card not found in index.html!"
        print("Found Calculus I course card in index.html!")

        home_shot = os.path.join(ARTIFACTS_DIR, "home_calc1_card_verified.png")
        await page.screenshot(path=home_shot, full_page=False)
        print(f"Saved {home_shot}")

        print("\n--- Testing calculus-1.html ---")
        await page.goto("http://localhost:4242/calculus-1.html")
        await page.wait_for_timeout(1500)

        # Verify Chapter 1
        title_el = await page.locator("#unit-title").inner_text()
        print(f"Chapter 1 Loaded: {title_el}")
        assert "Foundations of Functions" in title_el

        # Check KaTeX rendering
        katex_elements = await page.locator(".katex").count()
        print(f"Chapter 1 KaTeX equations rendered: {katex_elements}")
        assert katex_elements > 0, "No KaTeX equations rendered!"

        # Check Canvas mounting
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

        ch1_shot = os.path.join(ARTIFACTS_DIR, "calc1_ch1_verified.png")
        await page.screenshot(path=ch1_shot)
        print(f"Saved {ch1_shot}")

        # Iterate through all 8 chapters via sidebar navigation
        nav_items = page.locator(".unit-nav-item")
        total_units = await nav_items.count()
        print(f"\nSidebar chapters detected: {total_units}")
        assert total_units == 8, f"Expected 8 units, found {total_units}"

        for u in range(total_units):
            item = nav_items.nth(u)
            item_text = await item.inner_text()
            await item.click()
            await page.wait_for_timeout(700)

            cur_title = await page.locator("#unit-title").inner_text()
            cur_math = await page.locator(".katex").count()
            cur_canvases = await page.locator("canvas").count()
            print(f"Navigated to Unit {u+1}: {cur_title} | KaTeX: {cur_math} | Canvases: {cur_canvases}")
            assert cur_math > 0, f"Unit {u+1} failed to render math!"
            assert cur_canvases > 0, f"Unit {u+1} failed to mount canvas simulation!"

            # Capture key representative chapters
            if u == 2:  # Chapter 3: Epsilon-Delta
                shot = os.path.join(ARTIFACTS_DIR, "calc1_ch3_epsilon_delta_verified.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 4:  # Chapter 5: Secant-Tangent
                shot = os.path.join(ARTIFACTS_DIR, "calc1_ch5_secant_tangent_verified.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 6:  # Chapter 7: MVT
                shot = os.path.join(ARTIFACTS_DIR, "calc1_ch7_mvt_verified.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")
            elif u == 7:  # Chapter 8: Curve Sketching & Optimization
                shot = os.path.join(ARTIFACTS_DIR, "calc1_ch8_optimization_verified.png")
                await page.screenshot(path=shot)
                print(f"Saved {shot}")

        # Scroll to universal trust footer
        footer = page.locator(".reader-trust-footer")
        if await footer.count() > 0:
            await footer.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            footer_shot = os.path.join(ARTIFACTS_DIR, "calc1_footer_verified.png")
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
        # Filter benign favicon 404s if any
        critical_console = [e for e in console_errors if "favicon" not in e.lower()]
        assert len(critical_console) == 0, f"Encountered critical console errors: {critical_console}"

        print("\nALL VERIFICATION CHECKS PASSED WITH 0 ERRORS!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_verification())
