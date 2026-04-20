from dotenv import load_dotenv
import os, time
from playwright.sync_api import sync_playwright

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("https://moodle.bbs1-lg.de/login/index.php", wait_until="networkidle")
    page.fill("#username", os.getenv("MOODLE_USERNAME"))
    page.fill("#password", os.getenv("MOODLE_PASSWORD"))
    page.click("#loginbtn")
    page.wait_for_load_state("networkidle")

    page.goto("https://moodle.bbs1-lg.de/course/view.php?id=268", wait_until="networkidle")
    time.sleep(2)

    # Tiles format: each tile is a clickable section
    # Click on tile 1 (first content tile) to see what happens
    tiles = page.query_selector_all("li.section")
    print(f"Sections: {len(tiles)}")

    for i, sec in enumerate(tiles):
        sid = sec.get_attribute("id") or ""
        dsec = sec.get_attribute("data-section") or ""
        classes = (sec.get_attribute("class") or "")[:80]
        text = sec.inner_text().replace("\n", " ")[:60]
        print(f"  [{i}] id={sid} data-section={dsec} text='{text}'")

    # Try clicking on tile #1
    if len(tiles) > 1:
        tile = tiles[1]
        link = tile.query_selector("a")
        if link:
            href = link.get_attribute("href")
            print(f"\nTile 1 link: {href}")

        # Click it
        try:
            tile.click()
            time.sleep(2)

            # Check if a modal/panel opened
            modal = page.query_selector(".modal.show, #tilecontentmodal, .tile-modal")
            if modal:
                print(f"\nModal found! Text: {modal.inner_text()[:300]}")
            else:
                # Check if page content changed
                new_text = page.query_selector("#region-main").inner_text()
                print(f"\nAfter click, main text ({len(new_text)} chars):")
                for line in new_text.split("\n")[:30]:
                    if line.strip():
                        print(f"  {line.strip()[:100]}")
        except Exception as e:
            print(f"Click failed: {e}")

    # Also try direct section URL
    print("\n=== Trying direct section URL ===")
    page.goto("https://moodle.bbs1-lg.de/course/view.php?id=268&section=1", wait_until="networkidle")
    time.sleep(1)
    main = page.query_selector("#region-main")
    if main:
        text = main.inner_text()
        print(f"Section 1 text ({len(text)} chars):")
        for line in text.split("\n")[:40]:
            if line.strip():
                print(f"  {line.strip()[:120]}")

    browser.close()
