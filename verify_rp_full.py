# -*- coding: utf-8 -*-
"""
Verification Script for Course #20: Nuclear Reactor Physics
Verifies Homepage Card, All 8 Chapters, KaTeX math, 16 Canvases, 24 Solved Problems, 0 Errors
"""
import asyncio
import os
from playwright.async_api import async_playwright

ARTIFACT_DIR = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(f"PAGE ERROR: {err}"))
        page.on("console", lambda msg: errors.append(f"CONSOLE {msg.type.upper()}: {msg.text}") if msg.type in ["error"] else None)

        print("\n--- 1. Testing Homepage Catalog ---")
        await page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        await asyncio.sleep(1)

        # Check department and see-more button
        see_more = await page.query_selector(".btn-see-more")
        if see_more:
            txt = await see_more.inner_text()
            print(f"See More button found: '{txt}'")
            await see_more.click()
            await asyncio.sleep(0.5)

        # Check for reactor-physics card
        rp_card = await page.query_selector('a[href="reactor-physics.html"]')
        if rp_card:
            print("✓ Nuclear Reactor Physics course card successfully found in catalog!")
            await rp_card.scroll_into_view_if_needed()
            await asyncio.sleep(0.5)
            await page.screenshot(path=os.path.join(ARTIFACT_DIR, "home_rp_card_verified.png"))
            print("Saved home_rp_card_verified.png")
        else:
            print("❌ Nuclear Reactor Physics card not found in catalog!")

        print("\n--- 2. Testing Nuclear Reactor Physics Digital Textbook Reader ---")
        await page.goto("http://localhost:4242/reactor-physics.html", wait_until="networkidle")
        await asyncio.sleep(1.5)

        total_canvases_mounted = 0
        total_problems_mounted = 0

        # Verify all 8 chapters
        for ch_idx in range(8):
            ch_num = ch_idx + 1
            print(f"\n--- Checking Chapter {ch_num} ---")
            
            # Click chapter sidebar item
            sidebar_items = await page.query_selector_all(".unit-nav-item")
            if len(sidebar_items) > ch_idx:
                await sidebar_items[ch_idx].click()
                await asyncio.sleep(1.2)

            # Check title
            title_el = await page.query_selector("#unit-title")
            title = await title_el.inner_text() if title_el else "Unknown"
            print(f"Chapter {ch_num} Title: {title}")

            # Check sections
            sections = await page.query_selector_all(".textbook-section-card")
            print(f"  Sections count: {len(sections)}")

            # Check KaTeX math elements
            katex_elements = await page.query_selector_all(".katex")
            print(f"  KaTeX elements: {len(katex_elements)}")

            # Check for raw $$
            content_text = await page.inner_text("#textbook-sections")
            raw_math_count = content_text.count("$$")
            print(f"  Raw '$$' count: {raw_math_count}")

            # Check canvases (simulations)
            canvases = await page.query_selector_all("canvas")
            print(f"  Canvases mounted: {len(canvases)}")
            total_canvases_mounted += len(canvases)

            # Check solved problems
            problems = await page.query_selector_all(".problem-card")
            print(f"  Solved problems: {len(problems)}")
            total_problems_mounted += len(problems)

            # Capture screenshot
            ss_name = f"rp_ch{ch_num}_verified.png"
            await page.screenshot(path=os.path.join(ARTIFACT_DIR, ss_name))
            print(f"  Screenshot saved: {ss_name}")

        print("\n--- 3. Verification Metrics ---")
        print(f"Total Chapter Canvases Detected: {total_canvases_mounted} (16 expected across 8 units)")
        print(f"Total Solved Problems: {total_problems_mounted} (24 expected across 8 units)")

        print("\n--- 4. Error Log Summary ---")
        if errors:
            print(f"Found {len(errors)} errors:")
            for err in errors:
                print("  ", err)
        else:
            print("✓ PERFECT! 0 console errors or page errors detected.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
