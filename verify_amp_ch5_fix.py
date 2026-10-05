import asyncio
from playwright.async_api import async_playwright
import shutil

ARTIFACT_DIR = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"

async def verify_amp_ch5():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        errors = []
        page.on("console", lambda msg: errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(f"Page error: {err}"))

        url = "http://localhost:4242/atomic-molecular-physics.html"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="networkidle")
        await asyncio.sleep(1.0)

        # Click Chapter 5 in the sidebar
        ch5_btn = page.locator(".unit-nav-item").nth(4)
        await ch5_btn.click()
        print("Clicked Chapter 5!")
        await asyncio.sleep(1.5)

        # Scroll to Anomalous Zeeman section
        # Find section containing "The Anomalous Zeeman Effect"
        await page.evaluate("""() => {
            const el = Array.from(document.querySelectorAll('h4')).find(h => h.innerText.includes('Anomalous Zeeman'));
            if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
        }""")
        await asyncio.sleep(1.5)

        # Check for broken strings on the page
        content = await page.content()
        broken_strings = ["Seq0", "pprox 2", "ec{\\mu}", "ec{J}"]
        found_broken = []
        for bs in broken_strings:
            if bs in content:
                found_broken.append(bs)

        if found_broken:
            print(f"FAILED: Found broken strings on Chapter 5: {found_broken}")
        else:
            print("PASSED: Zero broken strings found on Chapter 5!")

        # Screenshot the exact view
        screenshot_path = "amp_ch5_zeeman_verified.png"
        await page.screenshot(path=screenshot_path, full_page=False)
        print(f"Saved verified screenshot to {screenshot_path}")

        # Also copy to artifacts directory
        artifact_path = f"{ARTIFACT_DIR}/amp_ch5_zeeman_verified.png"
        shutil.copyfile(screenshot_path, artifact_path)
        print(f"Copied screenshot to artifacts: {artifact_path}")

        print(f"Total console/page errors: {len(errors)}")
        if errors:
            for e in errors:
                print(f"  {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_amp_ch5())
