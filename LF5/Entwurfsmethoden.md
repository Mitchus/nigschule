---
fach: LF5
thema: Entwurfsmethoden
tags: [lf5, pap, struktogramm, pseudocode, entscheidungstabelle]
datum: 2026-04-20
typ: notiz
---

# Entwurfsmethoden

## Softwareentwurf nach IEEE

> Nach IEEE ist unter einem Softwareentwurf ein Prozess zu verstehen, in dem die **Architektur**, die **Komponenten**, die **Schnittstellen** und andere Merkmale eines Systems definiert werden.

Grafische Modelle vereinfachen die Kommunikation zwischen Auftraggeber und Entwickler.

---

## Programmablaufplan (PAP)

Der PAP stellt imperative Programmierung grafisch dar (auch: Flussdiagramm).

### Symbole

| Symbol | Bedeutung         | Form        |
| ------ | ----------------- | ----------- |
| ○      | Start / Ende      | Oval        |
| □      | Anweisung         | Rechteck    |
| ◇      | Bedingung         | Raute       |
| ▱      | Ein-/Ausgabe      | Parallelogramm |
| →      | Flussrichtung     | Pfeil       |

### Kontrollstrukturen im PAP

**Sequenz (Anweisungsfolge):**
```
┌─────────┐
│ Start   │
└────┬────┘
     ↓
┌─────────┐
│ Schritt1│
└────┬────┘
     ↓
┌─────────┐
│ Schritt2│
└────┬────┘
     ↓
┌─────────┐
│  Ende   │
└─────────┘
```

**Verzweigung (if/else):**
```
        ◇ Bedingung?
       / \
    ja/   \nein
     /     \
   □ A     □ B
     \     /
      \   /
       ↓
```

**Schleife (kopfgesteuert):**
```
    ──→ ◇ Bedingung?
   |      |  nein →
   |    ja↓
   |    □ Aktion
   └──────┘
```

**Fallunterscheidung (Mehrfachauswahl):**
```
        ◇ Variable?
      / | | \
    1/ 2| 3|  \sonst
    □   □  □   □
```

---

## Struktogramm (Nassi-Shneiderman)

Struktogramme zeigen den Programmablauf in geschachtelten Blöcken.

**Sequenz:**
```
┌────────────────────┐
│ Anweisung 1        │
├────────────────────┤
│ Anweisung 2        │
├────────────────────┤
│ Anweisung 3        │
└────────────────────┘
```

**Verzweigung:**
```
┌────────────────────────────────┐
│         Bedingung?             │
├───────────────┬────────────────┤
│     ja        │      nein     │
│ Anweisung A   │ Anweisung B   │
└───────────────┴────────────────┘
```

**Schleife (kopfgesteuert):**
```
┌────────────────────────────────┐
│ SOLANGE Bedingung              │
│  ┌─────────────────────────┐   │
│  │ Anweisung               │   │
│  └─────────────────────────┘   │
└────────────────────────────────┘
```

> [!tip] Tool: **Struktogrammer** - Programm zur Erstellung von Struktogrammen (offline)
> Online: [structorizer.fisch.lu](https://structorizer.fisch.lu)

---

## Pseudocode

Algorithmus in halbformaler Sprache beschreiben - Zwischenstufe zwischen natürlicher Sprache und Programmcode.

```
EINGABE: Benutzername, Passwort
Versuche = 0

WIEDERHOLE
    LESE Benutzername
    LESE Passwort
    Versuche = Versuche + 1

    WENN Benutzername korrekt UND Passwort korrekt DANN
        AUSGABE "Anmeldung erfolgreich"
        Starte Hauptprogramm
    SONST
        AUSGABE "Falsche Eingabe"
    ENDE WENN

BIS Versuche >= 3

WENN Versuche >= 3 DANN
    Sperre Zugang für 24 Stunden
    Benachrichtige Administrator
ENDE WENN
```

---

## Entscheidungstabelle

Übersichtliche Darstellung aller Bedingungen und zugehörigen Aktionen.

**Aufbau:**

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| **Bedingung 1** | J | J | N | N |
| **Bedingung 2** | J | N | J | N |
| **Aktion A** | X | | X | |
| **Aktion B** | | X | | X |

**Beispiel: Rabattvergabe**

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Stammkunde? | J | J | N | N |
| Bestellung > 100€? | J | N | J | N |
| 15% Rabatt | X | | | |
| 10% Rabatt | | X | | |
| 5% Rabatt | | | X | |
| Kein Rabatt | | | | X |

---

## draw.io

Kostenloses Tool zur Erstellung von PAPs, Struktogrammen und anderen Diagrammen.
Online: [app.diagrams.net](https://app.diagrams.net)

---

## Aufgaben

> [!example] Aufgabe 1 - PAP Anmeldung
> Erstelle einen PAP: In einem Anmeldeformular sollen Benutzername und Passwort eingegeben werden. Bei 3 Fehlversuchen wird der Zugang 24h gesperrt und der Admin benachrichtigt.

> [!example] Aufgabe 2 - PAP Aufgaben
> - Ergänze einen PAP für einen mobilen Roboter
> - Finde Fehler in vorgegebenen PAPs
> - PAP für Rechnungsnummernprüfung
> - PAP Zahlenrätsel mit Schreibtischtest

> [!example] Aufgabe 3 - Struktogramme
> - Lese vorgegebene Struktogramme und beschreibe den Ablauf
> - Erstelle ein Struktogramm (S. 524 A3, A4)
> - Erstelle ein Struktogramm für "Zufallszahl"

> [!example] Aufgabe 4 - Entscheidungstabellen (S. 533/524)
> Aufgabe 5: Aktien - Erstelle eine Entscheidungstabelle

---

## Materialien

- ![[files/02_PAP_Bibliothek.pdf]]
- ![[files/PAP_mobilerRoboter.pdf]]
- ![[files/PAP_Fehlersuche.pdf]]
- ![[files/03_PAP_Rechnungsnummerpruefen.pdf]]
- ![[files/04_PAP_Schreibtischtest.pdf]]
- ![[files/01_Strukto.pdf]]
- ![[files/02_Strukto.pdf]]
- ![[files/03_Strukto.pdf]]
- ![[files/Entscheidungstabelle.pdf]]
- ![[files/EntscheidungstabelleWellness.pdf]]
- ![[files/02_Pseudocode_Zustand.pdf]]

---

## Siehe auch

- [[Software und Qualität]]
- [[Zahlensysteme und Daten]]
