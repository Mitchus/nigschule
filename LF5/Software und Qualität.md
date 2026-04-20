---
fach: LF5
thema: Software und Qualität
tags: [lf5, software, qualität, testverfahren]
datum: 2026-04-20
typ: notiz
---

# Software und Qualität

## Softwarekategorien

Software lässt sich auf verschiedene Weisen kategorisieren:

### Nach Funktion

| Kategorie           | Beispiele                                      |
| ------------------- | ---------------------------------------------- |
| **Systemsoftware**  | Betriebssysteme, Treiber, Firmware             |
| **Anwendungssoftware** | Office, Browser, Bildbearbeitung            |
| **Entwicklungssoftware** | IDE, Compiler, Debugger                  |

### Nach Verbreitung

| Kategorie           | Beschreibung                                   |
| ------------------- | ---------------------------------------------- |
| **Standardsoftware** | Fertige Lösung für viele Nutzer (z.B. Office) |
| **Individualsoftware** | Maßgeschneidert für einen Kunden           |
| **Branchensoftware** | Spezialisiert für eine Branche (z.B. CAD)    |

### Nutzungsrechte von Software

| Lizenzmodell     | Beschreibung                                      |
| ---------------- | ------------------------------------------------- |
| **Proprietär**   | Quellcode geschlossen, Nutzung gegen Lizenzgebühr |
| **Open Source**   | Quellcode offen, frei nutzbar/änderbar            |
| **Freeware**     | Kostenlos, aber geschlossener Quellcode           |
| **Shareware**    | Testversion, danach kostenpflichtig               |
| **Public Domain** | Ohne Urheberrecht, völlig frei                   |

---

## Arten der Softwareanpassung

| Art              | Beschreibung                                       |
| ---------------- | -------------------------------------------------- |
| **Customizing**  | Konfiguration bestehender Software                 |
| **Parametrisierung** | Anpassung über Einstellungen/Parameter         |
| **Programmierung** | Eigene Module/Plugins entwickeln                 |
| **Integration**  | Verschiedene Systeme verbinden                     |

---

## Softwarequalität

Software muss den Anforderungen zweier Gruppen entsprechen:
- **Auftraggeber** (funktionale Anforderungen)
- **Hersteller** (nicht-funktionale Anforderungen)

### Qualitätskriterien (nicht-funktional)

| Kriterium          | Beschreibung                                     |
| ------------------ | ------------------------------------------------ |
| **Zuverlässigkeit** | Funktioniert fehlerfrei unter definierten Bedingungen |
| **Benutzbarkeit** | Einfach zu erlernen und zu bedienen                |
| **Effizienz**     | Schnell und ressourcenschonend                     |
| **Wartbarkeit**   | Leicht zu ändern, erweitern, korrigieren           |
| **Portabilität**  | Auf verschiedenen Systemen einsetzbar              |
| **Sicherheit**    | Schutz vor unberechtigtem Zugriff                  |
| **Skalierbarkeit** | Wächst mit steigenden Anforderungen              |

### Anforderungsspezifikation

- **Lastenheft** - Was will der Auftraggeber? (Anforderungen)
- **Pflichtenheft** - Wie setzt der Auftragnehmer es um? (Lösungskonzept)

---

## Testverfahren

| Verfahren          | Beschreibung                                     |
| ------------------ | ------------------------------------------------ |
| **Black-Box-Test** | Testen ohne Kenntnis des Quellcodes              |
| **White-Box-Test** | Testen mit Kenntnis des Quellcodes               |
| **Modultest**      | Einzelne Komponenten isoliert testen             |
| **Integrationstest** | Zusammenspiel der Komponenten testen           |
| **Systemtest**     | Gesamtes System testen                           |
| **Abnahmetest**    | Kunde prüft ob Anforderungen erfüllt sind        |

---

## Compiler und Interpreter

| Eigenschaft     | Compiler                          | Interpreter                     |
| --------------- | --------------------------------- | ------------------------------- |
| **Arbeitsweise** | Übersetzt gesamten Quelltext     | Übersetzt Zeile für Zeile       |
| **Geschwindigkeit** | Programm läuft schnell        | Programm läuft langsamer        |
| **Fehler**      | Alle auf einmal gemeldet          | Beim Auftreten gestoppt         |
| **Beispiele**   | C, C++, Rust                      | Python, JavaScript, Ruby        |

**JIT-Compiler** (Just-In-Time): Kompiliert zur Laufzeit - Kombination aus beiden Ansätzen. Beispiel: Java (Bytecode → JVM → JIT).

**Java-Übersetzungsweg:**
```
Quellcode (.java) → Compiler → Bytecode (.class) → JVM (Interpreter/JIT) → Maschinencode
```

---

## Aufgaben

> [!example] Aufgabe 1 - Softwarekategorien
> Recherchiere die 3. Kategorie "Nutzungsrechte von Software" (S. 459f)

> [!success] Lösung
> Software unterliegt dem Urheberrecht. Der Hersteller legt durch die **Lizenz** fest, in welchem Umfang die Software genutzt, weitergegeben oder verändert werden darf.
>
> | Lizenzmodell | Quellcode | Kosten | Weitergabe/Änderung | Beispiele |
> | ------------ | --------- | ------ | ------------------- | --------- |
> | **Proprietär** | Geschlossen | Kostenpflichtig (Lizenzgebühr) | Nicht erlaubt | Microsoft Windows, Adobe Photoshop |
> | **Open Source** | Offen | Meist kostenlos | Erlaubt, oft unter Bedingungen (z.B. GPL) | Linux, LibreOffice, Firefox |
> | **Freeware** | Geschlossen | Kostenlos | Weitergabe erlaubt, keine Änderungen | VLC Media Player (ältere Versionen), Skype |
> | **Shareware** | Geschlossen | Testversion kostenlos, Vollversion kostenpflichtig | Eingeschränkt | WinRAR, ältere Spiele-Demos |
> | **Public Domain** | Offen | Kostenlos | Uneingeschränkt erlaubt | Alte Werke deren Urheberrecht abgelaufen ist |
>
> Wichtige Unterscheidung: **Freeware** ist kostenlos, aber nicht frei (kein Quellcode, keine Änderungen). **Open Source** ist frei im Sinne von Freiheit (Quellcode einsehbar und änderbar), nicht zwingend kostenlos.

> [!example] Aufgabe 2 - Softwarequalität (S. 511-515)
> Think-Pair-Share:
> 1. Was ist eine Anforderungsspezifikation?
> 2. Bearbeite mind. 6 nicht-funktionale Qualitätskriterien mit je 2 Beispielen
> 3. Erstelle eine Skizze (Mindmap/Organigramm)

> [!success] Lösung
> **1. Anforderungsspezifikation:**
> Eine Anforderungsspezifikation ist ein Dokument, das alle Anforderungen an ein Softwareprodukt vollständig, eindeutig und nachprüfbar beschreibt. Sie bildet die Grundlage für die gesamte Entwicklung und wird in zwei Teilen festgehalten:
> - **Lastenheft** (vom Auftraggeber): beschreibt *was* die Software leisten soll – aus Kundensicht, ohne technische Details.
> - **Pflichtenheft** (vom Auftragnehmer): beschreibt *wie* die Anforderungen technisch umgesetzt werden – verbindliche Grundlage für Entwicklung und Abnahme.
>
> **2. Sechs nicht-funktionale Qualitätskriterien mit je zwei Beispielen:**
>
> | Kriterium | Beispiel 1 | Beispiel 2 |
> | --------- | ---------- | ---------- |
> | **Zuverlässigkeit** | Eine Bankingsoftware darf keine Transaktionen verlieren, auch bei Serverabsturz | Ein medizinisches System läuft 24/7 ohne Ausfall |
> | **Benutzbarkeit** | Eine App ist ohne Anleitung bedienbar (intuitive Navigation) | Fehlermeldungen sind klar verständlich auf Deutsch formuliert |
> | **Effizienz** | Eine Webseite lädt in unter 2 Sekunden | Eine Datenbank verarbeitet 10.000 Anfragen pro Sekunde ohne Leistungsabfall |
> | **Wartbarkeit** | Der Quellcode ist mit Kommentaren dokumentiert, sodass neue Entwickler ihn verstehen | Module sind lose gekoppelt, sodass eine Änderung keine Kettenreaktion auslöst |
> | **Portabilität** | Eine Java-Anwendung läuft ohne Änderungen auf Windows, Linux und macOS | Eine App ist als Android- und iOS-Version verfügbar |
> | **Sicherheit** | Passwörter werden nur verschlüsselt (gehasht) gespeichert | Zugriff auf Admin-Funktionen nur nach Zwei-Faktor-Authentifizierung |
> | **Skalierbarkeit** | Ein Webshop bleibt stabil, wenn an Black Friday 10x mehr Nutzer gleichzeitig zugreifen | Eine Datenbank lässt sich ohne Umprogrammierung auf mehrere Server verteilen |
>
> **3. Skizze (Mindmap-Struktur):**
> ```
> Softwarequalität
> ├── Funktional (Was tut die Software?)
> │   ├── Korrektheit
> │   └── Vollständigkeit
> └── Nicht-funktional (Wie tut sie es?)
>     ├── Zuverlässigkeit
>     ├── Benutzbarkeit
>     ├── Effizienz
>     ├── Wartbarkeit
>     ├── Portabilität
>     ├── Sicherheit
>     └── Skalierbarkeit
> ```

> [!example] Aufgabe 3 - Compiler/Interpreter (S. 510)
> 1. Beschreibe Arbeitsweise von Compilern und Interpretern mit je einem Vor-/Nachteil
> 2. Recherchiere JIT-Compiler mit Beispiel
> 3. Beschreibe den Java-Übersetzungsweg

> [!success] Lösung
> **1. Compiler und Interpreter im Vergleich:**
>
> *Compiler:*
> Ein Compiler übersetzt den gesamten Quellcode **vor der Ausführung** in Maschinencode. Das fertige Programm kann anschließend direkt vom Prozessor ausgeführt werden, ohne dass der Quellcode noch vorhanden sein muss.
> - Vorteil: Das kompilierte Programm läuft sehr schnell, da die Übersetzung nur einmal stattfindet.
> - Nachteil: Fehler werden erst nach der vollständigen Übersetzung gemeldet; die Entwicklungsiteration (Code ändern → testen) ist langsamer.
> - Beispiele: C, C++, Rust, Go
>
> *Interpreter:*
> Ein Interpreter liest den Quellcode **zur Laufzeit** Zeile für Zeile und führt jede Anweisung sofort aus, ohne vorher einen Maschinencode zu erzeugen.
> - Vorteil: Fehler werden sofort an der betroffenen Stelle gemeldet; einfachere Entwicklung und schnelles Testen.
> - Nachteil: Das Programm läuft langsamer, da jede Zeile bei jeder Ausführung neu übersetzt werden muss.
> - Beispiele: Python, JavaScript (ohne JIT), Ruby, PHP
>
> **2. JIT-Compiler (Just-In-Time):**
> Der JIT-Compiler ist ein Hybridansatz: Der Quellcode wird zunächst in einen plattformunabhängigen **Zwischencode** (z.B. Bytecode) übersetzt. Dieser wird zur Laufzeit von einer virtuellen Maschine (VM) interpretiert – häufig genutzte Code-Abschnitte werden dabei jedoch dynamisch in nativen Maschinencode kompiliert und gecacht. Dadurch wird die Ausführung über die Zeit deutlich beschleunigt.
> - Beispiel: Die **Java Virtual Machine (JVM)** nutzt JIT. Auch **V8** (JavaScript-Engine in Chrome/Node.js) verwendet JIT-Kompilierung.
> - Vorteil gegenüber reinem Interpreter: Deutlich höhere Ausführungsgeschwindigkeit bei häufig genutztem Code.
> - Vorteil gegenüber reinem Compiler: Plattformunabhängigkeit durch den Zwischencode.
>
> **3. Java-Übersetzungsweg:**
> Java kombiniert Compiler und Interpreter/JIT in einem zweistufigen Prozess:
> ```
> Quellcode (.java)
>     └→ javac (Java-Compiler)
>         └→ Bytecode (.class) [plattformunabhängig]
>             └→ JVM (Java Virtual Machine)
>                 ├→ Interpreter (führt Bytecode direkt aus)
>                 └→ JIT-Compiler (kompiliert häufig genutzten Code zu nativem Maschinencode)
>                     └→ Nativer Maschinencode (läuft auf der Hardware)
> ```
> Der Bytecode ist plattformunabhängig ("Write once, run anywhere") – er läuft auf jeder JVM, unabhängig vom Betriebssystem.

---

## Materialien

- ![[files/00_4_Software.pdf]]
- ![[files/00_4_Software_Anpassung.pdf]]
- ![[files/00_4_Softwarequalität.pdf]]
- ![[files/00_4_Softwaretestverfahren.pdf]]
- ![[files/Softwarequalitaet_IHK18Gh1.pdf]]
- ![[files/EinstiegSoftwareentwurf_2024.pdf]]

---

## Siehe auch

- [[Projektmanagement und Softwareentwicklung]]
- [[Vorgehensmodelle]]
- [[Entwurfsmethoden]]
