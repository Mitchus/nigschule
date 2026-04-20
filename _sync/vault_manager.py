"""Obsidian vault manager - creates notes and organizes files."""

import logging
import re
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


class VaultManager:
    def __init__(self, vault_path: str, course_mapping: dict[str, str]):
        self.vault_path = Path(vault_path)
        self.course_mapping = course_mapping

    def map_course_to_folder(self, course_name: str) -> str:
        """Map a Moodle course name to a vault folder using substring matching."""
        for pattern, folder in self.course_mapping.items():
            if pattern.startswith("_"):
                continue
            if pattern.lower() in course_name.lower():
                return folder
        # Fallback: sanitize course name as folder
        return self._sanitize_name(course_name)

    def _sanitize_name(self, name: str) -> str:
        """Sanitize a name for use as a file/folder name."""
        # Remove HTML tags
        name = re.sub(r"<[^>]+>", "", name)
        # Remove characters invalid in filenames
        name = re.sub(r'[<>:"/\\|?*]', "", name)
        # Collapse whitespace
        name = re.sub(r"\s+", " ", name).strip()
        return name[:100]  # Limit length

    def ensure_folder(self, folder_name: str) -> Path:
        """Create a vault folder with files/ subfolder if it doesn't exist."""
        folder = self.vault_path / folder_name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "files").mkdir(exist_ok=True)
        return folder

    def create_note(
        self,
        folder: str,
        title: str,
        content: str,
        fach: str = "",
        thema: str = "",
        tags: list[str] | None = None,
        typ: str = "notiz",
        overwrite: bool = False,
    ) -> Path:
        """Create an Obsidian markdown note with YAML frontmatter."""
        folder_path = self.ensure_folder(folder)
        filename = self._sanitize_name(title) + ".md"
        filepath = folder_path / filename

        if filepath.exists() and not overwrite:
            log.debug(f"Note already exists, skipping: {filepath}")
            return filepath

        tags = tags or []
        datum = datetime.now().strftime("%Y-%m-%d")

        frontmatter = f"""---
fach: {fach}
thema: {thema}
tags: [{', '.join(tags)}]
datum: {datum}
typ: {typ}
quelle: sync
---
"""
        full_content = frontmatter + "\n" + content
        filepath.write_text(full_content, encoding="utf-8")
        log.info(f"Created note: {filepath.name}")
        return filepath

    def html_to_markdown(self, html: str) -> str:
        """Convert HTML content to basic Markdown."""
        if not html:
            return ""

        soup = BeautifulSoup(html, "html.parser")

        # Remove script/style tags
        for tag in soup.find_all(["script", "style"]):
            tag.decompose()

        # Convert common HTML to markdown
        for tag in soup.find_all("strong"):
            tag.replace_with(f"**{tag.get_text()}**")
        for tag in soup.find_all("b"):
            tag.replace_with(f"**{tag.get_text()}**")
        for tag in soup.find_all("em"):
            tag.replace_with(f"*{tag.get_text()}*")
        for tag in soup.find_all("i"):
            tag.replace_with(f"*{tag.get_text()}*")
        for tag in soup.find_all("code"):
            tag.replace_with(f"`{tag.get_text()}`")

        # Convert headers
        for i in range(1, 7):
            for tag in soup.find_all(f"h{i}"):
                tag.replace_with(f"\n{'#' * i} {tag.get_text()}\n")

        # Convert links
        for tag in soup.find_all("a", href=True):
            text = tag.get_text(strip=True)
            href = tag["href"]
            tag.replace_with(f"[{text}]({href})")

        # Convert lists
        for tag in soup.find_all("li"):
            tag.replace_with(f"- {tag.get_text(strip=True)}\n")

        # Convert paragraphs
        for tag in soup.find_all("p"):
            tag.replace_with(f"\n{tag.get_text()}\n")

        # Convert line breaks
        for tag in soup.find_all("br"):
            tag.replace_with("\n")

        text = soup.get_text()
        # Clean up excessive newlines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def update_index(self, folder: str, fach: str) -> Path:
        """Create or update the index file for a subject folder."""
        folder_path = self.ensure_folder(folder)
        index_path = folder_path / f"{folder} Index.md"

        # Collect all markdown files in the folder (except index)
        notes = sorted([
            f.stem for f in folder_path.glob("*.md")
            if f.stem != f"{folder} Index" and not f.stem.startswith("_")
        ])

        if not notes:
            return index_path

        # Build index content
        frontmatter = f"""---
fach: {fach}
thema: Index
tags: [index, {fach.lower()}]
datum: {datetime.now().strftime("%Y-%m-%d")}
typ: index
---
"""
        content = f"# {folder}\n\n"

        # Group by existing sections if index exists
        if index_path.exists():
            existing = index_path.read_text(encoding="utf-8")
            # Find notes not yet in the index
            new_notes = [n for n in notes if f"[[{n}]]" not in existing]
            if not new_notes:
                return index_path
            # Append new notes
            content = existing.rstrip() + "\n\n## Neu synchronisiert\n\n"
            for note in new_notes:
                content += f"- [[{note}]]\n"
            index_path.write_text(content, encoding="utf-8")
        else:
            content = frontmatter + content
            for note in notes:
                content += f"- [[{note}]]\n"
            index_path.write_text(content, encoding="utf-8")

        log.info(f"Updated index: {index_path.name}")
        return index_path

    def file_dest(self, folder: str, filename: str) -> Path:
        """Get the destination path for a file attachment."""
        folder_path = self.ensure_folder(folder)
        return folder_path / "files" / self._sanitize_name(filename)
