"""Moodle Web Services API client - downloads course data and files."""

import logging
from pathlib import Path
from urllib.parse import urlencode

import requests

log = logging.getLogger(__name__)


class MoodleClient:
    def __init__(self, base_url: str, username: str, password: str, service: str = "moodle_mobile_app"):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.service = service
        self.token = None
        self.session = requests.Session()
        self.user_id = None

    def login(self) -> bool:
        """Get API token from Moodle."""
        url = f"{self.base_url}/login/token.php"
        data = {
            "username": self.username,
            "password": self.password,
            "service": self.service,
        }
        resp = self.session.post(url, data=data)
        resp.raise_for_status()
        result = resp.json()

        if "token" in result:
            self.token = result["token"]
            log.info("Moodle login successful")
            # Get user info
            info = self._api_call("core_webservice_get_site_info")
            if info:
                self.user_id = info.get("userid")
                log.info(f"Logged in as: {info.get('fullname')} (ID: {self.user_id})")
            return True
        else:
            log.error(f"Moodle login failed: {result.get('error', 'unknown error')}")
            return False

    def _api_call(self, function: str, **params) -> dict | list | None:
        """Call a Moodle Web Services API function."""
        if not self.token:
            log.error("Not authenticated - call login() first")
            return None

        url = f"{self.base_url}/webservice/rest/server.php"
        data = {
            "wstoken": self.token,
            "wsfunction": function,
            "moodlewsrestformat": "json",
            **params,
        }
        try:
            resp = self.session.post(url, data=data)
            resp.raise_for_status()
            result = resp.json()

            if isinstance(result, dict) and "exception" in result:
                log.warning(f"API error for {function}: {result.get('message', '')}")
                return None
            return result
        except Exception as e:
            log.error(f"API call {function} failed: {e}")
            return None

    def get_courses(self) -> list[dict]:
        """Get all enrolled courses for the current user."""
        if not self.user_id:
            return []

        courses = self._api_call("core_enrol_get_users_courses", userid=self.user_id)
        if not courses:
            return []

        return [
            {
                "id": c["id"],
                "shortname": c.get("shortname", ""),
                "fullname": c.get("fullname", ""),
                "category": c.get("categoryid", 0),
                "visible": c.get("visible", 1),
            }
            for c in courses
            if c.get("visible", 1) == 1
        ]

    def get_course_contents(self, course_id: int) -> list[dict]:
        """Get all sections and resources for a course."""
        sections = self._api_call("core_course_get_contents", courseid=course_id)
        if not sections:
            return []
        return sections

    def get_assignments(self, course_id: int) -> list[dict]:
        """Get assignments for a course."""
        result = self._api_call(
            "mod_assign_get_assignments",
            **{"courseids[0]": course_id}
        )
        if not result or "courses" not in result:
            return []

        assignments = []
        for course in result["courses"]:
            for assign in course.get("assignments", []):
                assignments.append({
                    "id": assign["id"],
                    "name": assign.get("name", ""),
                    "intro": assign.get("intro", ""),
                    "duedate": assign.get("duedate", 0),
                    "files": assign.get("introattachments", []),
                })
        return assignments

    def download_file(self, file_url: str, dest: Path) -> bool:
        """Download a file from Moodle using the API token."""
        try:
            # Append token to URL
            separator = "&" if "?" in file_url else "?"
            url = f"{file_url}{separator}token={self.token}"

            resp = self.session.get(url, stream=True)
            resp.raise_for_status()

            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)

            log.info(f"Downloaded: {dest.name}")
            return True
        except Exception as e:
            log.error(f"Failed to download {file_url}: {e}")
            return False

    def extract_files_from_sections(self, sections: list[dict]) -> list[dict]:
        """Extract all downloadable files from course sections."""
        files = []
        for section in sections:
            section_name = section.get("name", "Allgemein")
            for module in section.get("modules", []):
                mod_name = module.get("name", "")
                mod_type = module.get("modname", "")

                # Direct file resources
                for content in module.get("contents", []):
                    if content.get("type") == "file":
                        files.append({
                            "filename": content.get("filename", ""),
                            "fileurl": content.get("fileurl", ""),
                            "filesize": content.get("filesize", 0),
                            "timemodified": content.get("timemodified", 0),
                            "section": section_name,
                            "module_name": mod_name,
                            "module_type": mod_type,
                        })

                # Activity descriptions with embedded content
                if module.get("description"):
                    files.append({
                        "filename": f"{mod_name}.html",
                        "content": module["description"],
                        "section": section_name,
                        "module_name": mod_name,
                        "module_type": mod_type,
                        "is_content": True,
                    })

        return files
