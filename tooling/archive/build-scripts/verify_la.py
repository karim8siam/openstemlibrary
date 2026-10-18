# -*- coding: utf-8 -*-
"""
Verification script for Linear Algebra & Spectral Theory textbook and portal integration.
Tests homepage catalog, chapter switching across all 8 units, KaTeX math rendering,
Canvas simulation engines, slider interactivity, tiered problem reveals, and footer links.
"""
import os
import sys
from playwright.sync_api import sync_playwright

ARTIFACTS_DIR = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"

def run_verification():
    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error"] else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        print("=== Step 1: Verify Homepage Catalog (index.html) ===")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Check total books in All Subjects
        all_btn = page.locator(".dept-pill-btn[data-dept='all']")
        print("All Subjects tab text:", all_btn.inner_text())
        assert "27" in all_btn.inner_text(), f"Expected 27 books in All Subjects, found {all_btn.inner_text()}"

        # Click Mathematics tab
        math_btn = page.locator(".dept-pill-btn[data-dept='mathematics']")
        print("Math tab text:", math_btn.inner_text())
        assert "7" in math_btn.inner_text(), f"Expected 7 books in Mathematics, found {math_btn.inner_text()}"
        math_btn.click()
        page.wait_for_timeout(800)

        # Locate Linear Algebra card
        la_card = page.locator("a[href='linear-algebra.html']").locator("xpath=..")
        assert la_card.count() > 0, "Linear Algebra card not found in Mathematics grid!"
        print("Found Linear Algebra card on homepage!")

        # Screenshot home card detail
        home_card_path = os.path.join(ARTIFACTS_DIR, "home_la_card_detail.png")
        la_card.first.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        la_card.first.screenshot(path=home_card_path)
        print(f"Saved {home_card_path}")

        print("\n=== Step 2: Navigate to linear-algebra.html ===")
        page.goto("http://localhost:4242/linear-algebra.html", wait_until="networkidle")
        page.wait_for_timeout(1500)

        # Check Title
        page_title = page.title()
        print("Page title:", page_title)
        assert "Linear Algebra & Spectral Theory" in page_title

        # Check Ch. 1 pre-rendered
        h1_text = page.locator("#unit-title").inner_text()
        print("Chapter 1 Title:", h1_text)
        assert "Unit 1" in h1_text

        # Check KaTeX rendering in Ch. 1
        katex_count = page.locator(".katex").count()
        print(f"Chapter 1 KaTeX elements count: {katex_count}")
        assert katex_count > 20, f"Expected > 20 KaTeX elements, found {katex_count}"

        # Check Unit 1 Canvas
        canvas1 = page.locator("canvas")
        print(f"Canvas count in Unit 1: {canvas1.count()}")
        assert canvas1.count() >= 1

        # Test Ch. 1 interactive slider
        slider = page.locator("input[type='range']").first
        if slider.count() > 0:
            slider.evaluate("el => { el.value = '2.0'; el.dispatchEvent(new Event('input')); }")
            page.wait_for_timeout(500)
            print("Successfully exercised Ch. 1 slider via evaluate")

        # Reveal Tier 1 problem
        tier1_btn = page.locator(".solution-toggle-btn").first
        tier1_btn.click()
        page.wait_for_timeout(500)
        sol1 = page.locator(".solution-content").first
        assert sol1.is_visible(), "Tier 1 solution should be visible after click!"
        print("Tier 1 solved problem revealed successfully!")

        # Screenshot Ch 1
        ch1_img = os.path.join(ARTIFACTS_DIR, "la_ch1_verified.png")
        page.screenshot(path=ch1_img)
        print(f"Saved {ch1_img}")

        # Check All 8 Chapters via Sidebar Navigation
        chapter_screenshots = {
            3: "la_ch4_four_subspaces_sim.png",
            4: "la_ch5_transformations_sim.png",
            5: "la_ch6_eigen_sim.png",
            6: "la_ch7_gram_schmidt_sim.png",
            7: "la_ch8_quadratic_forms_sim.png"
        }

        for idx in range(8):
            print(f"\n--- Testing Chapter {idx + 1} ---")
            nav_item = page.locator(f".unit-nav-item[data-unit-index='{idx}']")
            nav_item.click()
            page.wait_for_timeout(1000)

            # Assert Title
            cur_title = page.locator("#unit-title").inner_text()
            print(f"Chapter {idx + 1} Title: {cur_title}")
            assert f"Unit {idx + 1}" in cur_title

            # KaTeX count
            k_count = page.locator(".katex").count()
            print(f"Chapter {idx + 1} KaTeX count: {k_count}")
            assert k_count > 15, f"Chapter {idx + 1} KaTeX count low: {k_count}"

            # Canvas simulation
            c_count = page.locator("canvas").count()
            print(f"Chapter {idx + 1} Canvas count: {c_count}")
            assert c_count >= 1, f"Chapter {idx + 1} missing Canvas simulation!"

            # Slider test
            ch_slider = page.locator("input[type='range']").first
            if ch_slider.count() > 0:
                ch_slider.evaluate("el => { el.value = (parseFloat(el.min) + (parseFloat(el.max) - parseFloat(el.min))*0.6).toString(); el.dispatchEvent(new Event('input')); }")
                page.wait_for_timeout(400)

            # Problem reveals test
            prob_btn = page.locator(".solution-toggle-btn").first
            prob_btn.click()
            page.wait_for_timeout(300)
            assert page.locator(".solution-content").first.is_visible()

            # Screenshot if in dictionary
            if idx in chapter_screenshots:
                img_path = os.path.join(ARTIFACTS_DIR, chapter_screenshots[idx])
                # Scroll to simulation
                sim_el = page.locator(".sim-box-wrapper").first
                if sim_el.count() > 0:
                    sim_el.scroll_into_view_if_needed()
                    page.wait_for_timeout(500)
                    sim_el.screenshot(path=img_path)
                    print(f"Saved simulation screenshot: {img_path}")

        print("\n=== Step 3: Verify Universal Reader Footer ===")
        footer = page.locator(".reader-trust-footer")
        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        footer_links = footer.locator("a")
        print(f"Footer links count: {footer_links.count()}")
        assert footer_links.count() >= 30, f"Expected >= 30 footer links, found {footer_links.count()}"

        # Assert Linear Algebra link and Discord link in footer
        la_link = footer.locator("a[href='linear-algebra.html']")
        assert la_link.count() >= 1, "linear-algebra.html link missing in footer!"

        discord_link = footer.locator("a[href='https://discord.gg/tBBKtvFJzW']")
        assert discord_link.count() >= 1, "Discord link missing in footer!"

        footer_img = os.path.join(ARTIFACTS_DIR, "la_footer_verified.png")
        footer.screenshot(path=footer_img)
        print(f"Saved {footer_img}")

        print("\n=== Step 4: Console & Error Audit ===")
        print(f"Console errors: {len(console_errors)}")
        for err in console_errors:
            print("  -", err)
        print(f"Page errors: {len(page_errors)}")
        for err in page_errors:
            print("  -", err)

        assert len(console_errors) == 0, f"Found {len(console_errors)} console errors!"
        assert len(page_errors) == 0, f"Found {len(page_errors)} page errors!"

        browser.close()

    print("\n✅ ALL VERIFICATION CHECKS PASSED PERFECTLY WITH ZERO ERRORS!")

if __name__ == "__main__":
    run_verification()
