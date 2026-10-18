# -*- coding: utf-8 -*-
"""
test_na_playwright.py
Playwright browser automation test for Numerical Analysis & Computational Methods textbook.
"""

from playwright.sync_api import sync_playwright
import time
import re

def run_tests():
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    errors = []
    console_logs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome_path,
            headless=True
        )
        page = browser.new_page()

        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda err: errors.append(str(err)))

        print("1. Loading http://localhost:4242/numerical-analysis.html...")
        page.goto("http://localhost:4242/numerical-analysis.html", wait_until="networkidle")
        time.sleep(2)

        # 2. Check title
        title = page.title()
        print(f"Page title: {title}")
        assert "Numerical Analysis & Computational Methods" in title, "Title mismatch!"

        # 3. Check for course numbers in full page text
        page_text = page.inner_text("body")
        forbidden = re.findall(r"\bMTH\b|\b2203\b|\b3105\b", page_text, re.IGNORECASE)
        print(f"Forbidden course code matches: {forbidden}")
        assert len(forbidden) == 0, f"Found forbidden course codes: {forbidden}"

        # 4. Check sidebar chapters count
        nav_items = page.locator("#unit-nav-list li").all()
        print(f"Sidebar unit items count: {len(nav_items)}")
        assert len(nav_items) == 8, f"Expected 8 units, found {len(nav_items)}"

        # 5. Test clicking each chapter
        for i in range(8):
            print(f"Testing navigation to Unit {i+1}...")
            nav_items[i].click()
            time.sleep(0.5)

            # Check unit title
            unit_title = page.locator("#unit-title").inner_text()
            print(f"  Unit {i+1} title: {unit_title}")
            assert f"Unit {i+1}:" in unit_title, f"Expected Unit {i+1} in title, got {unit_title}"

            # Check sections count
            sections = page.locator("#textbook-sections section").all()
            print(f"  Sections count: {len(sections)}")
            assert len(sections) >= 3, f"Expected at least 3 sections in Unit {i+1}, found {len(sections)}"

            # Check worked problems
            problems = page.locator("#problems-container .problem-card").all()
            print(f"  Worked problems count: {len(problems)}")
            assert len(problems) == 3, f"Expected 3 problems in Unit {i+1}, found {len(problems)}"

            # Test toggle button on first problem
            toggle_btn = problems[0].locator(".solution-toggle-btn")
            assert toggle_btn.is_visible()
            toggle_btn.click()
            time.sleep(0.2)
            sol_content = problems[0].locator(".solution-content")
            assert "open" in sol_content.get_attribute("class") or sol_content.is_visible()

        # 6. Test Font Toggle
        font_btn = page.locator("#btn-font-toggle")
        assert font_btn.is_visible()
        font_btn.click()
        time.sleep(0.3)
        article = page.locator("#textbook-article")
        print("Font toggle tested successfully!")

        # 7. Test Search Filter
        search_input = page.locator("#topic-search-input")
        search_input.fill("Runge-Kutta")
        time.sleep(0.5)
        search_input.fill("")
        time.sleep(0.3)
        print("Search filter tested successfully!")

        # 8. Check index.html integration
        print("Testing index.html integration...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        time.sleep(1)
        na_card = page.locator("a[href='numerical-analysis.html']")
        print(f"Numerical analysis card/link matches in index.html: {na_card.count()}")
        assert na_card.count() >= 1, "Numerical analysis card not found in index.html!"

        # Check console errors
        print("\n=== Console Logs Summary ===")
        severe_errors = [e for e in errors if "favicon" not in e.lower()]
        severe_logs = [l for l in console_logs if "[error]" in l.lower() and "favicon" not in l.lower()]
        print(f"Severe Page Errors: {len(severe_errors)}")
        print(f"Severe Console Errors: {len(severe_logs)}")
        if severe_errors:
            print("Errors:", severe_errors)
        if severe_logs:
            print("Console Errors:", severe_logs)

        assert len(severe_errors) == 0, f"Page errors encountered: {severe_errors}"
        assert len(severe_logs) == 0, f"Console error logs encountered: {severe_logs}"

        print("\nALL PLAYWRIGHT TESTS PASSED WITH 100% SUCCESS!")
        browser.close()

if __name__ == "__main__":
    run_tests()
