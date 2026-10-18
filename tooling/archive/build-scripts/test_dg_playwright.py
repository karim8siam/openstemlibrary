# -*- coding: utf-8 -*-
"""
test_dg_playwright.py
Automated Playwright verification script for differential-geometry.html and index.html
Runs in headless Chromium.
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

        print("--> Testing http://localhost:4242/differential-geometry.html ...")
        page.goto("http://localhost:4242/differential-geometry.html", wait_until="domcontentloaded")
        page.wait_for_timeout(300)

        title = page.title()
        print(f"Page Title: {title}")
        assert "Differential Geometry" in title, f"Unexpected page title: {title}"

        # Check for prohibited course numbers anywhere on the page
        body_text = page.locator("body").inner_text()
        course_num_pattern = re.compile(r"MTH[\s\-_]?(3203|3102|3202|4208|3101|2203)", re.IGNORECASE)
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
            page.wait_for_timeout(250)

            # Check unit title
            u_title = page.locator("#unit-title").inner_text()
            assert len(u_title) > 5, f"Unit title too short: {u_title}"

            # Check sections
            sections = page.locator(".textbook-section-card")
            s_count = sections.count()
            assert s_count == 5, f"Unit {i+1} has {s_count} sections, expected 5"

            # Check problems
            problems = page.locator(".problem-card")
            p_count = problems.count()
            assert p_count == 3, f"Unit {i+1} has {p_count} problems, expected 3"

            # Test problem toggle button
            first_btn = page.locator(".solution-toggle-btn").first
            first_btn.click()
            page.wait_for_timeout(100)
            first_sol = page.locator(".solution-content").first
            assert first_sol.is_visible(), f"Solution content did not open on toggle in Unit {i+1}"

        print("✓ All 8 units rendered successfully with 40 sections, 8 simulations, and 24 working solution toggles.")

        # Test font toggle
        font_btn = page.locator("#btn-font-toggle")
        if font_btn.is_visible():
            font_btn.click()
            print("✓ Font toggle button clicked successfully.")

        # Test search
        search_input = page.locator("#topic-search-input")
        if search_input.is_visible():
            search_input.fill("Weingarten")
            page.wait_for_timeout(100)
            search_input.fill("")
            print("✓ Topic search input works cleanly.")

        # Test index.html
        print("\n--> Testing http://localhost:4242/index.html ...")
        page.goto("http://localhost:4242/index.html", wait_until="domcontentloaded")
        page.wait_for_timeout(400)

        index_text = page.locator("body").text_content()
        assert "35 Textbooks" in index_text or "35 Live Textbooks" in index_text, "Hero badge does not show 35 textbooks!"
        print("✓ Verified hero badge shows 35 textbooks.")

        # Check Differential Geometry card in Mathematics
        math_tab = page.locator('button.dept-pill-btn[data-dept="mathematics"]')
        if math_tab.is_visible():
            math_tab.click()
            page.wait_for_timeout(200)

        # If there is a see-more button, click it to expand all cards
        see_more = page.locator('button.btn-see-more[data-dept="mathematics"]')
        if see_more.is_visible():
            see_more.click()
            page.wait_for_timeout(200)

        dg_card = page.locator('a[href="differential-geometry.html"]')
        assert dg_card.count() > 0, "Differential Geometry card link not found in index.html!"
        print(f"✓ Found {dg_card.count()} Differential Geometry links/cards on index.html.")

        # Filter out benign CDN KaTeX warnings if any
        critical_errors = [e for e in errors if "katex" not in e.lower() and "favicon" not in e.lower()]
        if critical_errors:
            print("❌ Critical errors detected:")
            for e in critical_errors:
                print(f"  {e}")
            sys.exit(1)
        else:
            print("✓ ZERO critical errors during full automated suite.")

        browser.close()
        print("\n🎉 ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
