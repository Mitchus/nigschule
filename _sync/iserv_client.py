"""IServ file browser client - downloads files from IServ group folders via JSON API."""

import logging
from pathlib import Path
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


class IServClient:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) ObsidianSync/1.0"
        })
        self._logged_in = False

    def login(self) -> bool:
        """Authenticate with IServ and initialize file module session."""
        login_url = f"{self.base_url}/iserv/auth/login"
        # Get login page for CSRF token
        resp = self.session.get(login_url)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        csrf_input = soup.find("input", {"name": "_csrf_token"})
        csrf_token = csrf_input["value"] if csrf_input else ""

        data = {
            "_username": self.username,
            "_password": self.password,
            "_csrf_token": csrf_token,
        }
        resp = self.session.post(login_url, data=data, allow_redirects=True)
        resp.raise_for_status()

        self._logged_in = "iserv/auth/logout" in resp.text or "/iserv/" in resp.url
        if self._logged_in:
            log.info("IServ login successful")
        else:
            log.error("IServ login failed - check credentials")
        return self._logged_in

    def _ensure_file_session(self, path: str):
        """Trigger OAuth redirect for the file module so JSON API works."""
        # The file module requires a separate OAuth-style auth flow.
        # A regular GET triggers redirects that set the required cookies.
        self.session.get(f"{self.base_url}{path}")

    def list_files(self, path: str) -> list[dict]:
        """List files and folders at the given IServ file path using JSON API.

        IServ returns JSON when Accept: application/json header is set.
        Returns list of dicts with keys: name, url, is_dir, modified
        """
        if not self._logged_in:
            self.login()

        url = f"{self.base_url}{path}"

        # First request initializes file module session (OAuth redirects)
        if not hasattr(self, "_file_session_init"):
            self._ensure_file_session(path)
            self._file_session_init = True

        resp = self.session.get(url, headers={
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
        })
        resp.raise_for_status()

        try:
            data = resp.json()
        except Exception:
            log.warning(f"Failed to parse JSON from {path}")
            return []

        items = []
        for entry in data.get("data", []):
            name_data = entry.get("name", {})
            name = name_data.get("text", "")
            link = name_data.get("link", "")
            is_dir = "folder" in name_data.get("icon", "").lower()

            # For files, the link has ?show=true - strip that for download URL
            download_url = link.split("?")[0] if not is_dir else link

            modified_data = entry.get("modified", {})
            modified = modified_data.get("display", "") if isinstance(modified_data, dict) else str(modified_data)

            if name:
                items.append({
                    "name": name,
                    "url": download_url,
                    "is_dir": is_dir,
                    "modified": modified,
                })

        return items

    def list_files_recursive(self, path: str) -> list[dict]:
        """Recursively list all files under the given path."""
        all_files = []
        items = self.list_files(path)

        for item in items:
            if item["is_dir"]:
                subpath = item["url"]
                if subpath.startswith("http"):
                    subpath = subpath.replace(self.base_url, "")
                sub_items = self.list_files_recursive(subpath)
                for sub in sub_items:
                    sub["rel_path"] = f"{item['name']}/{sub.get('rel_path', sub['name'])}"
                all_files.extend(sub_items)
            else:
                item["rel_path"] = item["name"]
                all_files.append(item)

        return all_files

    def download_file(self, url: str, dest: Path) -> bool:
        """Download a file from IServ to the destination path."""
        if not self._logged_in:
            self.login()

        try:
            if not url.startswith("http"):
                url = f"{self.base_url}{url}"

            resp = self.session.get(url, stream=True)
            resp.raise_for_status()

            # Check if we got HTML instead of a file (auth redirect)
            ct = resp.headers.get("content-type", "")
            if "text/html" in ct and resp.headers.get("content-length", "999999") == "0":
                log.warning(f"Got HTML instead of file for {dest.name} - possible auth issue")
                return False

            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)

            log.info(f"Downloaded: {dest.name}")
            return True
        except Exception as e:
            log.error(f"Failed to download {url}: {e}")
            return False
