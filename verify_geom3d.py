import os
import sys
import time
from playwright.sync_api import sync_playwright

def run_verification():
    print("Starting automated Playwright verification for 3D & Vector Geometry...")
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

        # Find 3D Geometry card
        geom3d_card = page.locator(".course-card:has-text('Three-Dimensional & Vector Geometry')")
        assert geom3d_card.count() > 0, "Three-Dimensional & Vector Geometry card not found in catalog!"
        geom3d_card.first.scroll_into_view_if_needed()
        time.sleep(0.5)
        geom3d_card.first.screenshot(path=os.path.join(artifacts_dir, "home_geom3d_card_detail.png"))
        print("Captured: home_geom3d_card_detail.png")

        # 2. Open 3D Geometry Book
        print("Navigating to 3D Geometry (geometry-3d.html)...")
        page.goto("http://localhost:4242/geometry-3d.html", wait_until="networkidle")
        time.sleep(1.5)

        # Wait for KaTeX to finish initial typesetting
        page.wait_for_selector(".katex", timeout=10000)
        katex_count = page.locator(".katex").count()
        print(f"Chapter 1 KaTeX equations count: {katex_count}")
        assert katex_count > 80, f"Expected >80 KaTeX elements in Ch.1, found {katex_count}"

        # Verify Ch 1 Simulation
        sim1 = page.locator("#sim-container-sim_geom3d_coords canvas")
        assert sim1.count() > 0, "Ch 1 Coordinates simulation canvas not found!"
        print("Ch 1 Coordinates simulation canvas verified.")

        # Test solution toggle in Ch 1
        toggle_btn = page.locator("#btn-sol-geom3d-prob-1-1")
        sol_content = page.locator("#sol-content-geom3d-prob-1-1")
        if toggle_btn.count() > 0:
            toggle_btn.first.click()
            time.sleep(0.3)
            assert sol_content.first.is_visible(), "Solution content not revealed on click!"
            print("Solution toggle for Example 1.1 verified.")

        page.screenshot(path=os.path.join(artifacts_dir, "geom3d_ch1_verified.png"))
        print("Captured: geom3d_ch1_verified.png")

        # 3. Test Navigation through all 8 chapters
        sim_capture_map = {
            1: "geom3d_ch2_planes_sim.png",
            2: "geom3d_ch3_skew_lines_sim.png",
            3: "geom3d_ch4_spheres_sim.png",
            4: "geom3d_ch5_cones_sim.png",
            5: "geom3d_ch6_conicoids_sim.png",
            6: "geom3d_ch7_vector_products_sim.png",
            7: "geom3d_ch8_spatial_apps_sim.png"
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
            assert ch_katex > 40, f"KaTeX rendering low in Chapter {idx + 1}: {ch_katex}"

            # Check canvas
            canvases = page.locator("canvas")
            assert canvases.count() > 0, f"No canvas found in Chapter {idx + 1}"

            # Take screenshot of simulation card
            sim_box = page.locator(".sim-box-wrapper")
            if sim_box.count() > 0:
                sim_box.first.scroll_into_view_if_needed()
                time.sleep(0.4)
                # Test slider adjustment if available
                sliders = sim_box.first.locator("input[type='range']")
                if sliders.count() > 0:
                    sliders.first.evaluate("el => { el.value = (parseFloat(el.value) + 2).toString(); el.dispatchEvent(new Event('input')); }")
                    time.sleep(0.2)
                sim_box.first.screenshot(path=os.path.join(artifacts_dir, sim_capture_map[idx]))
                print(f"Captured: {sim_capture_map[idx]}")

        # 4. Footer Verification
        footer = page.locator(".reader-trust-footer")
        assert footer.count() > 0, "Footer not found!"
        footer.first.scroll_into_view_if_needed()
        time.sleep(0.5)
        footer.first.screenshot(path=os.path.join(artifacts_dir, "geom3d_footer_verified.png"))
        print("Captured: geom3d_footer_verified.png")

        browser.close()

    print("\n--- Playwright Verification Summary ---")
    print(f"Console Errors: {len(console_errors)}")
    for ce in console_errors:
        print(f"  [Console Error] {ce}")
    print(f"Page Errors: {len(errors)}")
    for pe in errors:
        print(f"  [Page Error] {pe}")

    if len(errors) == 0 and len(console_errors) == 0:
        print("✅ VERIFICATION PASSED: 0 errors detected across all 8 chapters & interactive simulations!")
    else:
        print("❌ VERIFICATION FAILED: Errors were encountered.")
        sys.exit(1)

if __name__ == "__main__":
    run_verification()
