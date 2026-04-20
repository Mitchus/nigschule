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

> [!example] Aufgabe 2 - Softwarequalität (S. 511-515)
> Think-Pair-Share:
> 1. Was ist eine Anforderungsspezifikation?
> 2. Bearbeite mind. 6 nicht-funktionale Qualitätskriterien mit je 2 Beispielen
> 3. Erstelle eine Skizze (Mindmap/Organigramm)

> [!example] Aufgabe 3 - Compiler/Interpreter (S. 510)
> 1. Beschreibe Arbeitsweise von Compilern und Interpretern mit je einem Vor-/Nachteil
> 2. Recherchiere JIT-Compiler mit Beispiel
> 3. Beschreibe den Java-Übersetzungsweg

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
