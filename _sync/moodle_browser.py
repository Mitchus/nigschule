#!/usr/bin/env python3
"""
Moodle Browser Scraper - Visits each course section via ?section=N
and scrapes all visible content including tile content.

Usage:
    python moodle_browser.py                  # Scrape all courses
    python moodle_browser.py --course-id 268  # Specific course
    python moodle_browser.py --headed         # Show browser
"""

import argparse
import json
import logging
import os
import re
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

SCRIPT_DIR = Path(__file__).parent
VAULT_DIR = SCRIPT_DIR.parent


def load_config():
    with open(SCRIPT_DIR / "config.json") as f:
        return json.load(f)


def map_folder(name, mapping):
    for pat, folder in mapping.items():
        if not pat.startswith("_") and pat.lower() in name.lower():
            return folder
    return re.sub(r'[<>:"/\\|?*]', '', name)[:80].strip()


def sanitize(name):
    name = re.sub(r"<[^>]+>", "", name)
    name = name.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r'[<>:"/\\|?*]', '', re.sub(r"\s+", " ", name)).strip()[:120]


def html_to_md(html):
    if not html:
        return ""
    t = html
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"</?p[^>]*>", "\n", t, flags=re.I)
    t = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", t, flags=re.I | re.S)
    t = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", t, flags=re.I | re.S)
    t = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", t, flags=re.I | re.S)
    t = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", t, flags=re.I | re.S)
    for i in range(6, 0, -1):
        t = re.sub(rf"<h{i}[^>]*>(.*?)</h{i}>", rf"\n{'#' * i} \1\n", t, flags=re.I | re.S)
    t = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", t, flags=re.I | re.S)
    t = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", t, flags=re.I | re.S)
    t = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',  r"![](\1)", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def login(page, base, user, pw):
    log.info("Logging in...")
    page.goto(f"{base}/login/index.php", wait_until="networkidle")
    page.fill("#username", user)
    page.fill("#password", pw)
    page.click("#loginbtn")
    page.wait_for_load_state("networkidle")
    ok = "login" not in page.url
    log.info("Login OK" if ok else "Login FAILED")
    return ok


def get_courses(page, base):
    page.goto(f"{base}/my/courses.php", wait_until="networkidle")
    time.sleep(1)
    courses = {}
    for link in page.query_selector_all("a[href*='/course/view.php']"):
        href = link.get_attribute("href") or ""
        m = re.search(r"id=(\d+)", href)
        if m:
            cid = int(m.group(1))
            name = link.inner_text().strip()
            if name and len(name) > 3 and cid not in courses:
                courses[cid] = {"id": cid, "name": name, "url": href}
    return list(courses.values())


def scrape_section(page, base_url, course_id, section_num):
    """Load a single section via URL and scrape all content."""
    url = f"{base_url}/course/view.php?id={course_id}&section={section_num}"
    try:
        page.goto(url, wait_until="networkidle", timeout=15000)
    except Exception:
        return None
    time.sleep(0.5)

    main = page.query_selector("#region-main")
    if not main:
        return None

    # Get section title
    title_el = page.query_selector(".sectionname, h3.sectionname, .section-title")
    section_title = title_el.inner_text().strip() if title_el else f"Abschnitt {section_num}"

    # Get all activity content
    items = []

    # Get activities
    activities = main.query_selector_all("li.activity, div.activity")
    for act in activities:
        name_el = act.query_selector(".instancename, .activity-name-text, .activityname a")
        name = name_el.inner_text().strip() if name_el else ""
        # Remove "Forum", "Datei" etc suffixes from name
        name = re.sub(r"\s*(Forum|Datei|Aufgabe|Test|URL|Textseite|Verzeichnis|Lektion|Feedback)\s*$", "", name)

        # Get description/content
        desc_el = act.query_selector(".contentafterlink, .activity-description, .no-overflow, .contentwithoutlink")
        desc_html = desc_el.inner_html() if desc_el else ""

        # Get activity link for deeper scraping
        link_el = act.query_selector("a[href*='/mod/']")
        link_href = link_el.get_attribute("href") if link_el else ""

        # Determine type
        classes = act.get_attribute("class") or ""
        mod_type = ""
        for cls in classes.split():
            if cls.startswith("modtype_"):
                mod_type = cls.replace("modtype_", "")

        items.append({
            "name": name,
            "content_html": desc_html,
            "content": html_to_md(desc_html),
            "type": mod_type,
            "url": link_href,
        })

    # Also get label content that might not be in activity containers
    for label in main.query_selector_all(".label .no-overflow, .modtype_label .contentafterlink"):
        html = label.inner_html()
        md = html_to_md(html)
        if md and len(md) > 20:
            # Check if already captured
            if not any(md[:50] in item.get("content", "") for item in items):
                items.append({"name": "", "content": md, "type": "label", "url": ""})

    full_text = main.inner_text()
    if not items and len(full_text) < 50:
        return None

    return {
        "title": section_title,
        "section_num": section_num,
        "items": items,
        "full_text": full_text,
    }


def scrape_activity_page(page, url):
    """Visit an activity page and get its full content."""
    if not url or "/mod/resource/" in url or "/mod/forum/" in url:
        return ""
    try:
        page.goto(url, wait_until="networkidle", timeout=10000)
        time.sleep(0.5)
        for sel in [".box.generalbox .no-overflow", ".box.generalbox", "#region-main .content", "#page-content .box"]:
            el = page.query_selector(sel)
            if el:
                html = el.inner_html()
                md = html_to_md(html)
                if len(md) > 30:
                    return md
    except Exception:
        pass
    return ""


def scrape_course(page, course, base, mapping):
    """Scrape all sections of a course."""
    folder = map_folder(course["name"], mapping)
    log.info(f"\n=== {course['name']} -> {folder}/ ===")

    # First, determine how many sections exist
    page.goto(f"{base}/course/view.php?id={course['id']}", wait_until="networkidle")
    time.sleep(1)

    # Find section count from the page
    sections_els = page.query_selector_all("li.section, li[id^='section-']")
    section_ids = set()
    for el in sections_els:
        ds = el.get_attribute("data-section")
        if ds:
            section_ids.add(int(ds))

    if not section_ids:
        # Fallback: try sections 0-20
        section_ids = set(range(0, 20))

    max_section = max(section_ids) if section_ids else 10
    log.info(f"  Found sections: {sorted(section_ids)} (max: {max_section})")

    # Scrape each section
    all_sections = []
    empty_count = 0
    for sec_num in range(0, max_section + 1):
        result = scrape_section(page, base, course["id"], sec_num)
        if result and result["items"]:
            log.info(f"  Section {sec_num}: '{result['title']}' - {len(result['items'])} items")

            # For items with URLs (pages, lessons, quizzes), fetch full content
            for item in result["items"]:
                if item.get("url") and item["type"] in ("page", "book", "lesson", "hvp") and len(item.get("content", "")) < 50:
                    extra = scrape_activity_page(page, item["url"])
                    if extra:
                        item["content"] = extra
                        log.info(f"    + {item['name'][:40]} ({len(extra)} chars from page)")

            all_sections.append(result)
            empty_count = 0
        else:
            empty_count += 1
            if empty_count > 3:
                break  # Stop after 3 consecutive empty sections

    # Save to vault
    save_sections(all_sections, folder)
    return len(all_sections)


def save_sections(sections, folder):
    """Save scraped sections as Obsidian notes."""
    folder_path = VAULT_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    (folder_path / "files").mkdir(exist_ok=True)
    datum = datetime.now().strftime("%Y-%m-%d")
    created = 0

    for sec in sections:
        title = sec["title"]
        items = sec["items"]
        safe_name = sanitize(title)
        if not safe_name:
            safe_name = f"Abschnitt {sec['section_num']}"

        note_path = folder_path / f"{safe_name} (Browser).md"

        content = f"""---
fach: {folder}
thema: {title}
tags: [{folder.lower()}, moodle]
datum: {datum}
typ: notiz
quelle: moodle-browser
---

# {title}

"""
        for item in items:
            name = item.get("name", "")
            text = item.get("content", "")
            if not text and not name:
                continue

            if name:
                content += f"## {name}\n\n"
            if text:
                content += f"{text}\n\n"
            content += "---\n\n"

        # Only write if meaningful content
        body = re.sub(r"---\s*$", "", content.split("---\n", 2)[-1]).strip()
        if len(body) > 50:
            note_path.write_text(content, encoding="utf-8")
            created += 1
            log.info(f"  -> {note_path.name}")

    log.info(f"  Total: {created} notes created from {len(sections)} sections")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-id", type=int)
    parser.add_argument("--headed", action="store_true")
    args = parser.parse_args()

    load_dotenv(SCRIPT_DIR / ".env")
    config = load_config()
    base = config["moodle"]["base_url"]
    mapping = config.get("course_mapping", {})

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        if not login(page, base, os.getenv("MOODLE_USERNAME"), os.getenv("MOODLE_PASSWORD")):
            browser.close()
            return

        courses = get_courses(page, base)
        if args.course_id:
            courses = [c for c in courses if c["id"] == args.course_id]
            if not courses:
                courses = [{"id": args.course_id, "name": f"Course {args.course_id}",
                           "url": f"{base}/course/view.php?id={args.course_id}"}]

        log.info(f"Found {len(courses)} courses")
        for c in courses:
            log.info(f"  {c['name']} (ID: {c['id']})")

        total = 0
        for course in courses:
            total += scrape_course(page, course, base, mapping)

        browser.close()
        log.info(f"\nDone! {total} sections scraped across {len(courses)} courses.")


if __name__ == "__main__":
    main()
