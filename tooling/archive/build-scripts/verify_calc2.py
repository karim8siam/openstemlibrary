import os
import sys
import time
from playwright.sync_api import sync_playwright

def run_verification():
    print("Starting automated Playwright verification for Calculus II...")
    artifacts_dir = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"

    errors = []
    console_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        context = browser.new_context(viewport={"width": 1440, "height": 960})
        page = context.new_page()

        page.on("pageerror", lambda err: errors.append(f"PageError: {err}"))
        page.on("console", lambda msg: console_errors.append(f"Console {msg.type}: {msg.text}") if msg.type in ["error"] else None)

        # 1. Test Portal Index Card
        print("Navigating to Portal (index.html)...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        time.sleep(1)

        # Filter by Mathematics
        math_tab = page.locator(".dept-filter-btn:has-text('Mathematics')")
        if math_tab.count() > 0:
            math_tab.first.click()
            time.sleep(0.5)

        # Find Calculus II card
        calc2_card = page.locator(".course-card:has-text('Calculus II')")
        assert calc2_card.count() > 0, "Calculus II card not found in catalog!"
        calc2_card.first.scroll_into_view_if_needed()
        time.sleep(0.5)
        calc2_card.first.screenshot(path=os.path.join(artifacts_dir, "home_calc2_card_detail.png"))
        print("Captured: home_calc2_card_detail.png")

        # 2. Open Calculus II
        print("Navigating to Calculus II (calculus-2.html)...")
        page.goto("http://localhost:4242/calculus-2.html", wait_until="networkidle")
        time.sleep(1.5)

        # Wait for KaTeX to finish initial typesetting
        page.wait_for_selector(".katex", timeout=10000)
        katex_count = page.locator(".katex").count()
        print(f"Chapter 1 KaTeX equations count: {katex_count}")
        assert katex_count > 100, f"Expected >100 KaTeX elements in Ch.1, found {katex_count}"

        # Verify Ch 1 Simulation
        sim1 = page.locator("#sim-container-sim_calc2_reduction canvas")
        assert sim1.count() > 0, "Ch 1 Reduction simulation canvas not found!"
        print("Ch 1 Reduction simulation canvas verified.")

        # Test solution toggle in Ch 1
        toggle_btn = page.locator("#btn-sol-calc2-prob-1-1")
        sol_content = page.locator("#sol-content-calc2-prob-1-1")
        if toggle_btn.count() > 0:
            toggle_btn.first.click()
            time.sleep(0.3)
            assert sol_content.first.is_visible(), "Solution content not revealed on click!"
            print("Solution toggle for Example 1.1 verified.")

        page.screenshot(path=os.path.join(artifacts_dir, "calc2_ch1_verified.png"))
        print("Captured: calc2_ch1_verified.png")

        # 3. Test Navigation through all 8 chapters
        sim_capture_map = {
            1: "calc2_ch2_riemann_sim.png",
            2: "calc2_ch3_solids_sim.png",
            3: "calc2_ch4_polar_sim.png",
            4: "calc2_ch5_improper_sim.png",
            5: "calc2_ch6_gamma_sim.png",
            6: "calc2_ch7_power_sim.png",
            7: "calc2_ch8_taylor_sim.png"
        }

        nav_items = page.locator(".unit-nav-item")
        total_units = nav_items.count()
        print(f"Total chapters in sidebar: {total_units}")
        assert total_units == 8, f"Expected 8 chapters, found {total_units}"

        for idx in range(1, total_units):
            print(f"Clicking Chapter {idx + 1}...")
            nav_items.nth(idx).click()
            time.sleep(1.0)
            page.wait_for_selector(".katex", timeout=8000)

            ch_katex = page.locator(".katex").count()
            print(f"Chapter {idx + 1} KaTeX count: {ch_katex}")
            assert ch_katex > 50, f"KaTeX rendering low in Chapter {idx + 1}: {ch_katex}"

            # Check canvas
            canvases = page.locator("canvas")
            assert canvases.count() > 0, f"No canvas found in Chapter {idx + 1}"

            if idx in sim_capture_map:
                fname = sim_capture_map[idx]
                page.screenshot(path=os.path.join(artifacts_dir, fname))
                print(f"Captured: {fname}")

        # 4. Check Footer
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        footer = page.locator(".reader-trust-footer")
        assert footer.count() > 0, "Trust footer not found!"
        footer.first.screenshot(path=os.path.join(artifacts_dir, "calc2_footer_verified.png"))
        print("Captured: calc2_footer_verified.png")

        browser.close()

    print("\n--- Playwright Verification Summary ---")
    print(f"Total Page Errors: {len(errors)}")
    print(f"Total Console Errors: {len(console_errors)}")

    if errors:
        for err in errors:
            print(f"  [PAGE ERROR] {err}")
    if console_errors:
        for cerr in console_errors:
            print(f"  [CONSOLE ERROR] {cerr}")

    assert len(errors) == 0, f"Encountered {len(errors)} page errors!"
    assert len(console_errors) == 0, f"Encountered {len(console_errors)} console errors!"
    print("\n>>> ALL CALCULUS II VERIFICATION CHECKS PASSED WITH 0 ERRORS! <<<")

if __name__ == "__main__":
    run_verification()
