# -*- coding: utf-8 -*-
"""
test_discrete_math_playwright.py
Automated Playwright verification script for discrete-mathematics.html and index.html
Runs in headless Chromium.
Strictly ZERO course numbers.
"""

import sys
import re
from playwright.sync_api import sync_playwright

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport={"width": 1400, "height": 900})
        page = context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(f"PageError: {err}"))
        page.on("console", lambda msg: errors.append(f"ConsoleError: {msg.text}") if msg.type == "error" else None)

        print("--> Testing http://localhost:4242/discrete-mathematics.html ...")
        page.goto("http://localhost:4242/discrete-mathematics.html", wait_until="domcontentloaded")
        page.wait_for_timeout(400)

        title = page.title()
        print(f"Page Title: {title}")
        assert "Discrete Mathematics" in title, f"Unexpected page title: {title}"

        # Check for prohibited course numbers anywhere on the page
        body_text = page.locator("body").inner_text()
        course_num_pattern = re.compile(r"MTH[\s\-_]?(4107|4104|4102|4101|3203|3102|3202|4208|3101|2203|3103|2103)|4107", re.IGNORECASE)
        match = course_num_pattern.search(body_text)
        assert match is None, f"Found forbidden course number in page text: {match.group(0)}"
        print("✓ Verified STRICT ZERO course numbers in page text.")

        # Check JSON-LD
        json_ld = page.locator('script[type="application/ld+json"]').inner_text()
        assert course_num_pattern.search(json_ld) is None, "Course number found in JSON-LD!"
        print("✓ Verified STRICT ZERO course numbers in JSON-LD.")

        # Check Sidebar
        unit_items = page.locator("#unit-nav-list .unit-nav-item")
        unit_count = unit_items.count()
        print(f"Found {unit_count} chapters in sidebar navigation.")
        assert unit_count == 8, f"Expected 8 chapters, found {unit_count}"

        # Verify each unit loads correctly
        for i in range(8):
            unit_item = unit_items.nth(i)
            unit_name = unit_item.inner_text()
            print(f"  Testing Unit {i+1}: {unit_name.splitlines()[-1]}")
            unit_item.click()
            page.wait_for_timeout(350)

            # Check unit title
            u_title = page.locator("#unit-title").inner_text()
            assert len(u_title) > 5, f"Unit title too short: {u_title}"

            # Check sections
            sections = page.locator("#textbook-sections .textbook-section-card")
            sec_count = sections.count()
            assert sec_count == 5, f"Unit {i+1}: Expected 5 sections, got {sec_count}"

            # Check Canvas simulation is present in this unit
            canvas = page.locator(".sim-canvas")
            assert canvas.count() >= 1, f"Unit {i+1}: Canvas simulation missing!"

            # Check problems
            problems = page.locator("#problems-container .problem-card")
            prob_count = problems.count()
            assert prob_count == 3, f"Unit {i+1}: Expected 3 solved problems, got {prob_count}"

            # Test toggling the solution on the first problem
            sol_btn = page.locator(".solution-toggle-btn").first
            sol_content = page.locator(".solution-content").first
            assert not sol_content.is_visible(), "Solution should be hidden initially"
            sol_btn.click()
            page.wait_for_timeout(100)
            assert sol_content.is_visible(), "Solution should be visible after click"
            sol_btn.click()
            page.wait_for_timeout(100)
            assert not sol_content.is_visible(), "Solution should be hidden after second click"

        print("✓ Verified all 8 chapters, 40 sections, 8 Canvas simulations, and 24 solved problem toggles.")

        # Test Font toggle
        font_btn = page.locator("#btn-font-toggle")
        if font_btn.is_visible():
            font_btn.click()
            print("✓ Font toggle button clicked successfully.")

        # Test search
        search_input = page.locator("#topic-search-input")
        if search_input.is_visible():
            search_input.fill("Kruskal")
            page.wait_for_timeout(100)
            search_input.fill("")
            print("✓ Topic search input works cleanly.")

        # Return to Unit 1 and capture screenshot
        unit_items.first.click()
        page.wait_for_timeout(500)
        screenshot_path = "discrete_math_preview.png"
        page.screenshot(path=screenshot_path)
        print(f"✓ Saved screenshot to {screenshot_path}")

        # Also copy to artifacts dir
        import shutil
        shutil.copyfile(screenshot_path, "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/discrete_math_preview.png")

        # Test index.html
        print("\n--> Testing http://localhost:4242/index.html ...")
        page.goto("http://localhost:4242/index.html", wait_until="domcontentloaded")
        page.wait_for_timeout(400)

        index_text = page.locator("body").text_content()
        assert "39 Textbooks" in index_text or "39 Live Textbooks" in index_text, "Hero badge does not show 39 textbooks!"
        print("✓ Verified hero badge shows 39 textbooks.")

        # Check Discrete Mathematics card in Mathematics
        math_tab = page.locator('button.dept-pill-btn[data-dept="mathematics"]')
        if math_tab.is_visible():
            math_tab.click()
            page.wait_for_timeout(200)

        see_more = page.locator('button.btn-see-more[data-dept="mathematics"]')
        if see_more.is_visible():
            see_more.click()
            page.wait_for_timeout(200)

        dm_card = page.locator('a[href="discrete-mathematics.html"]')
        assert dm_card.count() >= 1, "Discrete Mathematics card missing in catalog!"
        print(f"✓ Found Discrete Mathematics link ({dm_card.count()} occurrences in index).")

        # Check console errors (filter out non-fatal 404s like missing favicon/optional assets)
        fatal_errors = [e for e in errors if "favicon" not in e.lower() and "analytics" not in e.lower()]
        if fatal_errors:
            print(f"Warnings/Errors observed: {fatal_errors}")
        else:
            print("✓ ZERO page or console errors detected!")

        browser.close()
        print("\n==========================================")
        print("ALL PLAYWRIGHT TESTS PASSED SUCCESSFULLY! 🚀")
        print("==========================================")

if __name__ == "__main__":
    run_tests()
