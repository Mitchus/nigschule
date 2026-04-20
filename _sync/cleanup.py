#!/usr/bin/env python3
"""
Vault Cleanup - Consolidates synced notes, fixes titles, adds WikiLinks.

Usage:
    python cleanup.py              # Run full cleanup
    python cleanup.py --dry-run    # Preview changes
"""

import argparse
import logging
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).parent.parent
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

# Topic keywords -> canonical WikiLink targets
# Format: keyword -> (link_target, display_name)
TOPIC_LINKS = {
    # Networking (DVT)
    "osi": ("DVT/IsoOsi", "ISO/OSI-Modell"),
    "osi-modell": ("DVT/IsoOsi", "ISO/OSI-Modell"),
    "iso/osi": ("DVT/IsoOsi", "ISO/OSI-Modell"),
    "schichtenmodell": ("DVT/IsoOsi", "ISO/OSI-Modell"),
    "netzwerktechnik": ("DVT/Netzwerktechnik", "Netzwerktechnik"),
    "tcp/ip": ("DVT/Netzwerkprotokolle", "Netzwerkprotokolle"),
    "netzwerkprotokoll": ("DVT/Netzwerkprotokolle", "Netzwerkprotokolle"),
    "ipv4": ("DVT/IPV4", "IPv4"),
    "ip-adress": ("DVT/IP-Adressierung und Subnetting", "IP-Adressierung"),
    "subnetting": ("DVT/IP-Adressierung und Subnetting", "Subnetting"),
    "switch": ("DVT/Switch", "Switch"),
    "access point": ("DVT/AccessPoint", "Access Point"),
    "accesspoint": ("DVT/AccessPoint", "Access Point"),
    "wlan": ("DVT/WIFI IEEE 802.11", "WLAN"),
    "wifi": ("DVT/WIFI IEEE 802.11", "WLAN"),
    "ieee 802.11": ("DVT/WIFI IEEE 802.11", "WLAN IEEE 802.11"),
    # Hardware (DVT)
    "cpu": ("DVT/CPU", "CPU"),
    "prozessor": ("DVT/CPU", "CPU"),
    "gpu": ("DVT/GPU", "GPU"),
    "grafikkarte": ("DVT/GPU", "GPU"),
    "ram": ("DVT/Ram", "RAM"),
    "arbeitsspeicher": ("DVT/Ram", "RAM"),
    "festplatte": ("DVT/Festplatten", "Festplatten"),
    "ssd": ("DVT/Festplatten", "Festplatten"),
    "hdd": ("DVT/Festplatten", "Festplatten"),
    "eva-prinzip": ("DVT/Eingabe und Ausgabe", "EVA-Prinzip"),
    # Programming (LF5)
    "python": ("LF5/Python Grundlagen", "Python"),
    "struktogramm": ("LF5/Struktogramme", "Struktogramm"),
    "nassi-shneiderman": ("LF5/Struktogramme", "Struktogramm"),
    "pseudocode": ("LF5/Pseudocode", "Pseudocode"),
    "programmablaufplan": ("LF5/PAP", "PAP"),
    "flussdiagramm": ("LF5/PAP", "PAP"),
    "pap": ("LF5/PAP", "PAP"),
    # Software Engineering (LF5)
    "wasserfallmodell": ("LF5/Vorgehensmodelle", "Wasserfallmodell"),
    "v-modell": ("LF5/Vorgehensmodelle", "V-Modell"),
    "scrum": ("LF5/Vorgehensmodelle", "Scrum"),
    "vorgehensmodell": ("LF5/Vorgehensmodelle", "Vorgehensmodelle"),
    "softwaretest": ("LF5/Softwarequalität", "Softwaretests"),
    "softwarequalität": ("LF5/Softwarequalität", "Softwarequalität"),
    "entscheidungstabelle": ("LF5/Entscheidungstabellen", "Entscheidungstabelle"),
    # Data (LF5)
    "zahlensystem": ("LF5/Zahlensysteme", "Zahlensysteme"),
    "dualsystem": ("LF5/Zahlensysteme", "Zahlensysteme"),
    "binärsystem": ("LF5/Zahlensysteme", "Zahlensysteme"),
    "hexadezimal": ("LF5/Zahlensysteme", "Zahlensysteme"),
    # Business (LF2)
    "kalkulation": ("LF2/Listenpreis", "Kalkulation"),
    "listenpreis": ("LF2/Listenpreis", "Listenpreis"),
    # Networking (LF3)
    "strukturierte verkabelung": ("LF3/Strukturierte Verkabelung", "Strukturierte Verkabelung"),
    "cisco packet tracer": ("LF3/Cisco Packet Tracer", "Cisco Packet Tracer"),
    "lastenheft": ("LF3/Lastenheft ZeroTake", "Lastenheft"),
}


def read_note(path: Path) -> tuple[dict, str]:
    """Read a note and split into frontmatter dict + body content."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = {}
    body = text

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    fm[key.strip()] = val.strip()
            body = parts[2].strip()

    return fm, body


def is_stub(body: str) -> bool:
    """Check if a note is just a stub (PDF embed + minimal text)."""
    lines = [l.strip() for l in body.split("\n") if l.strip()]
    # Remove heading and section info
    content_lines = [l for l in lines if not l.startswith("#") and not l.startswith("*Abschnitt") and not l.startswith("Heruntergeladen") and not l.startswith("Datei von")]
    # Check if only content is a file embed
    real_content = [l for l in content_lines if not l.startswith("![[")]
    text_len = sum(len(l) for l in real_content)
    return text_len < 80


def get_section(body: str) -> str:
    """Extract section name from note body."""
    m = re.search(r"\*Abschnitt:\s*(.+?)\*", body)
    return m.group(1).strip() if m else ""


def get_embeds(body: str) -> list[str]:
    """Extract file embeds from note body."""
    return re.findall(r"!\[\[(.+?)\]\]", body)


def fix_title(filename: str) -> str:
    """Fix truncated or messy filenames."""
    name = filename.replace(".md", "")

    # Remove trailing dots from truncation
    name = re.sub(r"\.{3,}$", "", name)

    # Clean up HTML entities
    name = name.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

    # Clean up weird whitespace
    name = re.sub(r"\s+", " ", name).strip()

    return name


def build_section_index(notes: list[dict]) -> dict[str, list[dict]]:
    """Group notes by their Moodle section."""
    sections = {}
    for note in notes:
        section = note.get("section", "Allgemein") or "Allgemein"
        sections.setdefault(section, []).append(note)
    return sections


def add_wiki_links(body: str, current_file: str) -> str:
    """Add WikiLinks for known topics mentioned in the body."""
    added_links = set()

    for keyword, (target, display) in TOPIC_LINKS.items():
        # Don't link to self
        if target.lower() in current_file.lower():
            continue

        # Case-insensitive search for the keyword in body text (not in existing links)
        pattern = re.compile(r"(?<!\[\[)(?<!\|)\b(" + re.escape(keyword) + r")\b(?!\]\])(?!\|)", re.IGNORECASE)
        if pattern.search(body) and target not in added_links:
            added_links.add(target)

    # Add "Siehe auch" section if we found links
    if added_links:
        see_also = "\n\n## Siehe auch\n\n"
        for target in sorted(added_links):
            display = TOPIC_LINKS.get(target.split("/")[-1].lower(), (target, target.split("/")[-1]))[1]
            # Find the display name from TOPIC_LINKS
            for kw, (t, d) in TOPIC_LINKS.items():
                if t == target:
                    display = d
                    break
            see_also += f"- [[{target}|{display}]]\n"

        # Only add if not already present
        if "## Siehe auch" not in body:
            body += see_also

    return body


def consolidate_folder(folder: Path, dry_run: bool = False) -> dict:
    """Consolidate notes in a folder: merge stubs into topic notes, fix titles, add links."""
    folder_name = folder.name
    md_files = sorted(folder.glob("*.md"))
    index_file = folder / f"{folder_name} Index.md"

    stats = {"renamed": 0, "consolidated": 0, "linked": 0, "deleted": 0}

    stubs = []
    content_notes = []
    all_notes = []

    for f in md_files:
        if f.name == f"{folder_name} Index.md":
            continue
        fm, body = read_note(f)
        section = get_section(body)
        embeds = get_embeds(body)
        stub = is_stub(body)

        note_info = {
            "path": f,
            "frontmatter": fm,
            "body": body,
            "section": section,
            "embeds": embeds,
            "is_stub": stub,
            "title": fix_title(f.stem),
        }
        all_notes.append(note_info)
        if stub:
            stubs.append(note_info)
        else:
            content_notes.append(note_info)

    log.info(f"{folder_name}: {len(all_notes)} notes ({len(content_notes)} with content, {len(stubs)} stubs)")

    # Step 1: Fix truncated filenames
    for note in all_notes:
        old_name = note["path"].stem
        new_name = fix_title(old_name)
        if new_name != old_name:
            new_path = note["path"].parent / f"{new_name}.md"
            if not new_path.exists():
                log.info(f"  Rename: {old_name} -> {new_name}")
                if not dry_run:
                    note["path"].rename(new_path)
                    note["path"] = new_path
                stats["renamed"] += 1

    # Step 2: Group stubs by section and consolidate
    sections = build_section_index(stubs)
    for section_name, section_stubs in sections.items():
        if len(section_stubs) < 2:
            continue
        if not section_name or section_name == "Allgemein":
            continue

        # Create consolidated note for this section
        safe_name = re.sub(r'[<>:"/\\|?*]', '', section_name)[:80]
        consolidated_path = folder / f"{safe_name}.md"

        # Build content from stubs
        content_parts = []
        embed_list = []
        stub_paths_to_remove = []

        for stub in section_stubs:
            title = stub["title"]
            embeds = stub["embeds"]
            body_clean = stub["body"]
            # Remove heading and section line
            body_clean = re.sub(r"^#.*\n*", "", body_clean)
            body_clean = re.sub(r"\*Abschnitt:.*\*\n*", "", body_clean)
            body_clean = re.sub(r"Heruntergeladen am.*\n*", "", body_clean)
            body_clean = re.sub(r"Datei von IServ.*\n*", "", body_clean)
            body_clean = body_clean.strip()

            if embeds:
                for e in embeds:
                    embed_list.append((title, e))
            elif body_clean:
                content_parts.append(f"### {title}\n\n{body_clean}")

            stub_paths_to_remove.append(stub["path"])

        if not consolidated_path.exists() or dry_run:
            datum = datetime.now().strftime("%Y-%m-%d")
            note_content = f"""---
fach: {folder_name}
thema: {section_name}
tags: [{folder_name.lower()}, zusammenfassung]
datum: {datum}
typ: notiz
quelle: sync
---

# {section_name}

"""
            # Add text content
            for part in content_parts:
                note_content += part + "\n\n"

            # Add materials section
            if embed_list:
                note_content += "## Materialien\n\n"
                for title, embed in embed_list:
                    note_content += f"- **{title}**: ![[{embed}]]\n"
                note_content += "\n"

            # Add links
            note_content = add_wiki_links(note_content, str(consolidated_path))

            log.info(f"  Consolidate: {len(section_stubs)} stubs -> {safe_name}.md")
            if not dry_run:
                consolidated_path.write_text(note_content, encoding="utf-8")
                # Remove individual stubs
                for p in stub_paths_to_remove:
                    if p.exists() and p != consolidated_path:
                        p.unlink()
                        stats["deleted"] += 1

            stats["consolidated"] += 1

    # Step 3: Add WikiLinks to remaining content notes
    for note in content_notes:
        new_body = add_wiki_links(note["body"], str(note["path"]))
        if new_body != note["body"]:
            log.info(f"  Link: {note['path'].stem}")
            if not dry_run:
                fm_text = note["path"].read_text(encoding="utf-8", errors="replace")
                if fm_text.startswith("---"):
                    parts = fm_text.split("---", 2)
                    if len(parts) >= 3:
                        new_text = f"---{parts[1]}---\n\n{new_body}"
                        note["path"].write_text(new_text, encoding="utf-8")
                        stats["linked"] += 1

    return stats


def create_course_index(folder: Path, title: str, description: str, dry_run: bool = False):
    """Create a well-structured index for a course folder."""
    folder_name = folder.name
    index_path = folder / f"{folder_name} Index.md"

    # Collect all notes
    md_files = sorted(f for f in folder.glob("*.md") if f.name != f"{folder_name} Index.md")
    if not md_files:
        return

    # Categorize notes
    materials = []  # typ: material
    notes = []  # typ: notiz
    assignments = []  # typ: aufgabe
    other = []

    for f in md_files:
        fm, body = read_note(f)
        typ = fm.get("typ", "notiz")
        entry = {"name": f.stem, "typ": typ, "section": get_section(body)}

        if typ == "aufgabe":
            assignments.append(entry)
        elif typ == "material":
            materials.append(entry)
        elif typ in ("notiz", "zusammenfassung"):
            notes.append(entry)
        else:
            other.append(entry)

    datum = datetime.now().strftime("%Y-%m-%d")
    content = f"""---
fach: {folder_name}
thema: {title}
tags: [index, {folder_name.lower()}]
datum: {datum}
typ: index
---

# {title}

{description}

"""

    if notes:
        content += "## Notizen\n\n"
        for n in sorted(notes, key=lambda x: x["name"]):
            content += f"- [[{n['name']}]]\n"
        content += "\n"

    if materials:
        content += "## Materialien\n\n"
        for n in sorted(materials, key=lambda x: x["name"]):
            content += f"- [[{n['name']}]]\n"
        content += "\n"

    if assignments:
        content += "## Aufgaben\n\n"
        for n in sorted(assignments, key=lambda x: x["name"]):
            content += f"- [[{n['name']}]]\n"
        content += "\n"

    if other:
        content += "## Sonstiges\n\n"
        for n in sorted(other, key=lambda x: x["name"]):
            content += f"- [[{n['name']}]]\n"
        content += "\n"

    log.info(f"  Index: {index_path.name} ({len(md_files)} Einträge)")
    if not dry_run:
        index_path.write_text(content, encoding="utf-8")


# Course descriptions for index files
COURSE_INFO = {
    "LF2": ("LF2 - Arbeitsplätze ausstatten", "Lernfeld 2: Planung, Konfiguration und Bereitstellung von IT-Arbeitsplätzen inkl. kaufmännischer Grundlagen."),
    "LF3": ("LF3 - Clients in Netzwerke einbinden", "Lernfeld 3: Netzwerkinfrastruktur planen und Clients in bestehende Netzwerke integrieren (ZeroTake Coffee Szenario)."),
    "LF5": ("LF5 - Software & Daten", "Lernfeld 5: Softwareentwicklung, Zahlensysteme, Programmierung mit Python und Softwareprojektmanagement."),
    "LF6": ("LF6 - Serviceanfragen bearbeiten", "Lernfeld 6: IT-Servicemanagement, SLAs und Kundenbetreuung."),
    "Deutsch": ("Deutsch", "Sprachkompetenz, Kommunikation und Textanalyse."),
    "Englisch": ("Englisch", "Business English, Technical Communication und Prüfungsvorbereitung."),
    "Religion": ("Religion", "Ethik, Moral und Wertevermittlung."),
    "ZQ": ("ZQ - Zusatzqualifikation", "Zusatzqualifikation Prompting und KI-Kompetenz."),
}


def main():
    parser = argparse.ArgumentParser(description="Cleanup and consolidate vault notes")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    args = parser.parse_args()

    folders = ["LF2", "LF3", "LF5", "LF6", "Deutsch", "Englisch", "Religion", "ZQ"]
    total_stats = {"renamed": 0, "consolidated": 0, "linked": 0, "deleted": 0}

    for folder_name in folders:
        folder = VAULT / folder_name
        if not folder.is_dir():
            continue

        log.info(f"\n=== {folder_name} ===")
        stats = consolidate_folder(folder, dry_run=args.dry_run)
        for k, v in stats.items():
            total_stats[k] += v

        # Create proper index
        if folder_name in COURSE_INFO:
            title, desc = COURSE_INFO[folder_name]
            create_course_index(folder, title, desc, dry_run=args.dry_run)

    # Also add links to existing DVT notes
    dvt = VAULT / "DVT"
    if dvt.is_dir():
        log.info(f"\n=== DVT (Verlinkung) ===")
        for f in dvt.glob("*.md"):
            if f.name == "DVT Index.md":
                continue
            fm, body = read_note(f)
            new_body = add_wiki_links(body, str(f))
            if new_body != body and not args.dry_run:
                text = f.read_text(encoding="utf-8", errors="replace")
                if text.startswith("---"):
                    parts = text.split("---", 2)
                    if len(parts) >= 3:
                        f.write_text(f"---{parts[1]}---\n\n{new_body}", encoding="utf-8")
                        total_stats["linked"] += 1
                        log.info(f"  Link: {f.stem}")

    log.info(f"\n=== Fertig ===")
    log.info(f"Umbenannt: {total_stats['renamed']}")
    log.info(f"Konsolidiert: {total_stats['consolidated']} Abschnitte")
    log.info(f"Gelöscht: {total_stats['deleted']} Stubs")
    log.info(f"Verlinkt: {total_stats['linked']} Notizen")


if __name__ == "__main__":
    main()
