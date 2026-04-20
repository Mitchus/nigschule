#!/usr/bin/env python3
"""
School Sync Tool - Syncs IServ files and Moodle course data into an Obsidian vault.

Usage:
    python sync.py                  # Sync everything
    python sync.py --iserv          # Only sync IServ files
    python sync.py --moodle         # Only sync Moodle courses
    python sync.py --dry-run        # Show what would be synced without downloading
    python sync.py --list-courses   # List all Moodle courses and their mapped folders
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from iserv_client import IServClient
from moodle_client import MoodleClient
from vault_manager import VaultManager

SCRIPT_DIR = Path(__file__).parent
VAULT_DIR = SCRIPT_DIR.parent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def load_config() -> dict:
    config_path = SCRIPT_DIR / "config.json"
    with open(config_path) as f:
        return json.load(f)


def load_sync_state(state_file: Path) -> dict:
    if state_file.exists():
        with open(state_file) as f:
            return json.load(f)
    return {"iserv_files": {}, "moodle_files": {}, "last_sync": None}


def save_sync_state(state_file: Path, state: dict):
    state["last_sync"] = datetime.now().isoformat()
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def sync_iserv(config: dict, vault: VaultManager, state: dict, dry_run: bool = False):
    """Sync files from IServ group folder."""
    log.info("=== IServ Sync ===")

    username = os.getenv("ISERV_USERNAME")
    password = os.getenv("ISERV_PASSWORD")
    if not username or not password:
        log.error("ISERV_USERNAME and ISERV_PASSWORD must be set in .env")
        return

    iserv = IServClient(config["iserv"]["base_url"], username, password)
    if not iserv.login():
        return

    group_path = config["iserv"]["group_path"]
    log.info(f"Listing files at {group_path} ...")
    files = iserv.list_files_recursive(group_path)

    if not files:
        log.warning("No files found on IServ (page structure may have changed)")
        return

    log.info(f"Found {len(files)} files on IServ")
    ignore_ext = set(config.get("ignore_extensions", []))

    downloaded = 0
    skipped = 0
    for file_info in files:
        rel_path = file_info.get("rel_path", file_info["name"])
        ext = Path(rel_path).suffix.lower()

        if ext in ignore_ext:
            continue

        # Determine target folder from the subfolder structure
        parts = Path(rel_path).parts
        if len(parts) > 1:
            subfolder = parts[0]
            folder = vault.map_course_to_folder(subfolder)
        else:
            folder = "IServ"  # Files in root go to IServ folder

        # Check sync state
        state_key = f"iserv:{rel_path}"
        file_modified = file_info.get("modified", "")
        if state_key in state.get("iserv_files", {}) and state["iserv_files"][state_key] == file_modified:
            skipped += 1
            continue

        dest = vault.file_dest(folder, Path(rel_path).name)

        if dry_run:
            log.info(f"  [DRY RUN] Would download: {rel_path} -> {folder}/files/{dest.name}")
            downloaded += 1
            continue

        if iserv.download_file(file_info["url"], dest):
            state.setdefault("iserv_files", {})[state_key] = file_modified
            downloaded += 1

            # Create a note for certain file types
            if ext == ".pdf":
                vault.create_note(
                    folder=folder,
                    title=dest.stem,
                    content=f"![[files/{dest.name}]]\n\nDatei von IServ heruntergeladen am {datetime.now().strftime('%Y-%m-%d')}.",
                    fach=folder,
                    thema=dest.stem,
                    tags=["iserv", folder.lower()],
                    typ="material",
                )

    log.info(f"IServ: {downloaded} downloaded, {skipped} unchanged")


def sync_moodle(config: dict, vault: VaultManager, state: dict, dry_run: bool = False):
    """Sync course data and files from Moodle."""
    log.info("=== Moodle Sync ===")

    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")
    if not username or not password:
        log.error("MOODLE_USERNAME and MOODLE_PASSWORD must be set in .env")
        return

    moodle = MoodleClient(config["moodle"]["base_url"], username, password)
    if not moodle.login():
        return

    courses = moodle.get_courses()
    if not courses:
        log.warning("No enrolled courses found")
        return

    log.info(f"Found {len(courses)} enrolled courses")
    ignore_ext = set(config.get("ignore_extensions", []))

    for course in courses:
        course_name = course["fullname"]
        folder = vault.map_course_to_folder(course_name)
        log.info(f"\n--- {course_name} -> {folder}/ ---")

        # Get course contents
        sections = moodle.get_course_contents(course["id"])
        if not sections:
            log.warning(f"  No content found for {course_name}")
            continue

        files = moodle.extract_files_from_sections(sections)
        log.info(f"  Found {len(files)} items")

        downloaded = 0
        notes_created = 0

        for file_info in files:
            # Handle inline content (descriptions, activity text)
            if file_info.get("is_content"):
                md_content = vault.html_to_markdown(file_info.get("content", ""))
                if md_content and len(md_content) > 50:
                    section = file_info.get("section", "")
                    title = file_info.get("module_name", "Unbenannt")

                    if dry_run:
                        log.info(f"  [DRY RUN] Would create note: {title}")
                        notes_created += 1
                        continue

                    heading = f"# {title}\n\n"
                    if section:
                        heading += f"*Abschnitt: {section}*\n\n"

                    vault.create_note(
                        folder=folder,
                        title=title,
                        content=heading + md_content,
                        fach=folder,
                        thema=title,
                        tags=["moodle", folder.lower(), file_info.get("module_type", "")],
                        typ="notiz",
                    )
                    notes_created += 1
                continue

            # Handle file downloads
            filename = file_info.get("filename", "")
            ext = Path(filename).suffix.lower()
            if ext in ignore_ext:
                continue

            state_key = f"moodle:{course['id']}:{filename}"
            file_modified = str(file_info.get("timemodified", 0))

            if state_key in state.get("moodle_files", {}) and state["moodle_files"][state_key] == file_modified:
                continue

            dest = vault.file_dest(folder, filename)

            if dry_run:
                log.info(f"  [DRY RUN] Would download: {filename} -> {folder}/files/")
                downloaded += 1
                continue

            fileurl = file_info.get("fileurl", "")
            if fileurl and moodle.download_file(fileurl, dest):
                state.setdefault("moodle_files", {})[state_key] = file_modified
                downloaded += 1

                # Create linking note for documents
                if ext in (".pdf", ".docx", ".pptx", ".xlsx"):
                    section = file_info.get("section", "")
                    mod_name = file_info.get("module_name", dest.stem)
                    vault.create_note(
                        folder=folder,
                        title=mod_name,
                        content=(
                            f"# {mod_name}\n\n"
                            f"![[files/{dest.name}]]\n\n"
                            f"*Abschnitt: {section}*\n"
                            f"Heruntergeladen am {datetime.now().strftime('%Y-%m-%d')} von Moodle."
                        ),
                        fach=folder,
                        thema=mod_name,
                        tags=["moodle", folder.lower()],
                        typ="material",
                    )

        # Get assignments
        assignments = moodle.get_assignments(course["id"])
        for assign in assignments:
            title = assign["name"]
            state_key = f"moodle:assign:{assign['id']}"

            if state_key in state.get("moodle_files", {}):
                continue

            if dry_run:
                log.info(f"  [DRY RUN] Would create assignment note: {title}")
                continue

            due_str = ""
            if assign.get("duedate"):
                due_str = datetime.fromtimestamp(assign["duedate"]).strftime("%Y-%m-%d %H:%M")

            intro_md = vault.html_to_markdown(assign.get("intro", ""))
            content = f"# {title}\n\n"
            if due_str:
                content += f"**Fällig:** {due_str}\n\n"
            content += intro_md

            vault.create_note(
                folder=folder,
                title=title,
                content=content,
                fach=folder,
                thema=title,
                tags=["moodle", "aufgabe", folder.lower()],
                typ="aufgabe",
            )
            state.setdefault("moodle_files", {})[state_key] = "created"

        # Update index
        if not dry_run:
            vault.update_index(folder, folder)

        if downloaded or notes_created:
            log.info(f"  {course_name}: {downloaded} files, {notes_created} notes")


def list_courses(config: dict):
    """List all Moodle courses and their mapped folders."""
    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")
    if not username or not password:
        log.error("MOODLE_USERNAME and MOODLE_PASSWORD must be set in .env")
        return

    moodle = MoodleClient(config["moodle"]["base_url"], username, password)
    if not moodle.login():
        return

    courses = moodle.get_courses()
    vault = VaultManager(config["vault_path"], config.get("course_mapping", {}))

    print(f"\n{'Kurs':<50} {'-> Ordner':<30}")
    print("-" * 80)
    for c in courses:
        folder = vault.map_course_to_folder(c["fullname"])
        print(f"{c['fullname']:<50} -> {folder:<30}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Sync IServ & Moodle to Obsidian Vault")
    parser.add_argument("--iserv", action="store_true", help="Only sync IServ")
    parser.add_argument("--moodle", action="store_true", help="Only sync Moodle")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be synced")
    parser.add_argument("--list-courses", action="store_true", help="List Moodle courses")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Load env
    env_path = SCRIPT_DIR / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    else:
        log.warning(f"No .env file found at {env_path} - copy .env.example to .env and fill in credentials")
        sys.exit(1)

    config = load_config()

    if args.list_courses:
        list_courses(config)
        return

    vault = VaultManager(config["vault_path"], config.get("course_mapping", {}))
    state_file = VAULT_DIR / config.get("sync_state_file", "_sync/sync_state.json")
    state = load_sync_state(state_file)

    sync_all = not args.iserv and not args.moodle

    try:
        if sync_all or args.iserv:
            sync_iserv(config, vault, state, dry_run=args.dry_run)

        if sync_all or args.moodle:
            sync_moodle(config, vault, state, dry_run=args.dry_run)

        if not args.dry_run:
            save_sync_state(state_file, state)
            log.info(f"\nSync complete. State saved.")
    except KeyboardInterrupt:
        log.info("\nSync interrupted.")
        if not args.dry_run:
            save_sync_state(state_file, state)
    except Exception as e:
        log.error(f"Sync failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
