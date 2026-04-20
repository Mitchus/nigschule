#!/usr/bin/env python3
"""
Smart Rename - Gives meaningful short names to notes with sentence-fragment filenames.
"""

import logging
import re
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).parent.parent
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

# Manual renames: old stem -> new stem
# Based on actual note content analysis
RENAMES = {
    # === LF5 ===
    "Als Projekt wird ein Vorgehen bezeichnet, welches": "Projektdefinition",
    "Auch wenn Python Datentypen von sich aus intern er": "Python Datentypen",
    "Aufgabe 1Erstellen Sie ein PAP, welcher das Betan": "Aufgabe PAP Betankung",
    "Aufgaben Legen Sie ein Projekt und eine": "Aufgabe Python Projekt anlegen",
    "Bearbeiten Sie den Kompetenzcheck auf S. 464 A1.De": "Aufgabe Kompetenzcheck Projekt",
    "Benutzereingaben über die Konsole werden in Python": "Python Eingabe und Typkonvertierung",
    "Erstellen Sie eine Konsolenanwendung Rom.Das Progr": "Aufgabe Konsolenanwendung Römische Zahlen",
    "Erstellen Sie in Python ein Programm mit folgender": "Aufgabe Python Verzweigungen",
    "Es gibt verschiedene Möglichkeiten mit Python zu a": "Python IDE Einrichtung",
    "Finden Sie die Syntaxfehler (ohne einen Editor zu": "Aufgabe Syntaxfehler finden",
    "Für einen Nettoverkaufspreis wird die Mehrwertsteu": "Aufgabe MwSt Berechnung",
    "Informationen S. 518 ff Pro": "Programmablaufpläne",
    "Informationen zu Wie werden aus Zeichen Informati": "Daten und Information",
    "Legen Sie ein neues Projekt in Python an.Kopieren": "Aufgabe Fehlersuche Python",
    "Lesen Sie die Buchseiten S. 549 - 552. und beantwo": "Aufgabe Schleifen Theorie",
    "Lesen Sie die Seiten S. 492 f509-511. über Projektmanagem": "Aufgabe Projektmanagement lesen",
    "Nach IEEE ist unter einem Softwareentwurf ein Proz": "Softwareentwurf nach IEEE",
    "Nützliches in Partnerarbeit zu lösenBezeichner": "Python Bezeichner und Syntax",
    "Operatoren Operatoren sind Symbole die Verarbei": "Python Operatoren",
    "Partnerarbeit Prozessphasen beschreibenSchauen S": "Aufgabe Prozessphasen",
    "Partnerarbeit Wie jedes Produkt unterliegt auch S": "Aufgabe Softwarequalität",
    "Recherchieren Sie die 3te Kategorie „Nutzungsrecht": "Aufgabe Softwarelizenzierung",
    "SituationSie beschäftigen sich in Ihrer Ausbildun": "Situation Softwareentwurf",
    "Software lässt sich auf verschiedene Art und Weise": "Softwarekategorien",
    "Text eingerahmt; Ecken abgerundet 10 Pixel; Absta": "Python IDE Thonny Hinweise",
    "To Do(S. 472)Rechnen Sie 100010, 25610, 1310, 34": "Aufgabe Dezimal zu Dual",
    "To Do(S. 472)Rechnen Sie die Hexadezimalzahlen i": "Aufgabe Hexadezimal umrechnen",
    "To DoÜbertragen Sie den Quellcode aus der S. 537": "Aufgabe Quellcode übertragen",
    "Unter dem Begriff Softwareentwicklung versteht man": "Softwareentwicklung Definition",
    "„Sie sollen in einem Projekt mitarbeiten, in dem e": "Handlungssituation LF5",
    "Aufgaben zu Darstellung von auditiven, grafischen, Datums- und Zeitangaben Darstellungen": "Aufgabe Datendarstellungen",

    # === LF3 ===
    "Willkommen zum Kurs Clients in Netzwerke einbinde": "Kursübersicht LF3",
    "Kurs-Literatur & Software": "Literatur und Software LF3",
    "Handlungssituation dieser Lerneinheit Während I": "Handlungssituation Netzwerktechnik",
    "Handlungssituation in diesem Lernfeld Nairobi b": "Handlungssituation Anforderungsanalyse",
    "Handlungssituation in dieser Lerneinheit Nairob": "Handlungssituation Verkabelung",
    "Handlungssituation dieser LerneinheitAlles kla": "Handlungssituation Konfiguration",
    "Die folgende Liste soll Ihnen dabei helfen zu üb": "Lernziel-Checkliste",
    "Abschnitt 4 - Netzwerk der Zerotake erweitern und": "Netzwerk ZeroTake erweitern",
    "Abschnitt I - ISO-GERECHTe Strukturierte Verkabelu": "Strukturierte Verkabelung ISO",
    "Abschnitt II - Anforderungen eines Projekts bestim": "Anforderungen bestimmen",
    "Abschnitt II - Bedarfsanalyse Aktiver Netzwerkkomp": "Bedarfsanalyse aktive Komponenten",
    "Abschnitt II - Netzwerkmedien im netzwerk kennenle": "Netzwerkmedien kennenlernen",
    "Abschnitt II - osi-Modell zu kollaborativen erarbe": "OSI-Modell erarbeiten",
    "Abschnitt III - Bedarfsanalyse passive komponenten": "Bedarfsanalyse passive Komponenten",
    "Nachdem wir in der letzten Einheit uns mit den pas": "Einführung aktive Komponenten",
    "In dieser Lerneinheit werden wir uns mit der physi": "Einführung physische Infrastruktur",
    "Abschnitt II - Themen in der Netzwerktechnik erarb... (Kopie)": "Netzwerktechnik Themen",
    "Nach der Einheit...Wenden Sie Ihre neues Wisse": "Übung Bedarfsanalyse",
    "Übungen zum OSI-Modell zur eigenständigen Vert": "Übung OSI-Modell",
    "Arbeitsbuch Gratzke, S. 191, Aufgabe 15 - OSI von": "Aufgabe OSI vs DoD Modell",
    "3.6 Clients einbinden &amp; konfigurieren": "3.6 Clients einbinden und konfigurieren",

    # === LF5 consolidated ===
    "Die Divisionsmethode (Dezimalzahl in Dualzahl umwa": "Divisionsmethode",
    "Die Multiplikationsmethode (Dualzahl in Dezimalzah": "Multiplikationsmethode",
    "Die Subtraktionsmethode (Dezimalzahl in Dualzahl u": "Subtraktionsmethode",
}


def rename_note(old_path: Path, new_stem: str, dry_run: bool = False) -> Path | None:
    """Rename a note and update references in other files."""
    new_path = old_path.parent / f"{new_stem}.md"
    if new_path.exists():
        log.warning(f"  Target exists, skipping: {new_stem}")
        return None

    old_stem = old_path.stem
    log.info(f"  {old_stem[:50]:50s} -> {new_stem}")

    if dry_run:
        return new_path

    # Rename the file
    old_path.rename(new_path)

    # Update frontmatter thema field
    text = new_path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(
        r"(thema:\s*).+",
        rf"\g<1>{new_stem}",
        text,
        count=1,
    )
    new_path.write_text(text, encoding="utf-8")

    # Update WikiLinks in all files in the same folder and parent
    for md in list(old_path.parent.glob("*.md")) + list(VAULT.glob("**/*.md")):
        if md == new_path or not md.exists():
            continue
        try:
            content = md.read_text(encoding="utf-8", errors="replace")
            if f"[[{old_stem}]]" in content or f"[[{old_stem}|" in content:
                content = content.replace(f"[[{old_stem}]]", f"[[{new_stem}]]")
                content = re.sub(rf"\[\[{re.escape(old_stem)}\|", f"[[{new_stem}|", content)
                md.write_text(content, encoding="utf-8")
        except Exception:
            pass

    return new_path


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    count = 0
    for folder_name in ["LF2", "LF3", "LF5", "LF6", "Deutsch", "Englisch", "Religion", "ZQ"]:
        folder = VAULT / folder_name
        if not folder.is_dir():
            continue

        renamed_any = False
        for md in sorted(folder.glob("*.md")):
            stem = md.stem
            if stem in RENAMES:
                if not renamed_any:
                    log.info(f"\n=== {folder_name} ===")
                    renamed_any = True
                rename_note(md, RENAMES[stem], dry_run=args.dry_run)
                count += 1

    log.info(f"\n{count} Notizen umbenannt.")


if __name__ == "__main__":
    main()
