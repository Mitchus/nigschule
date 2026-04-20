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

> [!success] Lösung
> ```
>                    ╔══════════════╗
>                    ║    START     ║
>                    ╚══════╤═══════╝
>                           │
>                           ▼
>                    ┌──────────────┐
>                    │ Versuche = 0 │
>                    └──────┬───────┘
>                           │
>                           ▼
>                    ┌──────────────────────────┐
>                    │ Eingabe: Benutzername,    │
>                    │         Passwort          │
>                    └──────┬───────────────────┘
>                           │
>                           ▼
>                    ┌──────────────────────┐
>                    │ Versuche = Versuche+1 │
>                    └──────┬───────────────┘
>                           │
>                           ▼
>              ┌────────────◇────────────────┐
>              │  Benutzername UND Passwort  │
>              │         korrekt?            │
>              └──────┬──────────────┬───────┘
>                   ja│              │nein
>                     │              │
>                     ▼              ▼
>             ┌───────────┐  ┌───────────────────┐
>             │ Ausgabe:  │  │ Ausgabe:           │
>             │ "Anmeldung│  │ "Falsche Eingabe"  │
>             │ erfolgreich│  └────────┬──────────┘
>             └─────┬─────┘           │
>                   │                 ▼
>                   │       ┌─────────◇──────────┐
>                   │       │  Versuche >= 3?    │
>                   │       └──────┬──────┬──────┘
>                   │            ja│      │nein
>                   │              │      │
>                   │              ▼      └──────────────────┐
>                   │     ┌────────────────┐                 │
>                   │     │ Sperre Zugang  │                 │
>                   │     │ für 24 Stunden │                 │
>                   │     └──────┬─────────┘                 │
>                   │            │                           │
>                   │            ▼                           │
>                   │     ┌────────────────┐                 │
>                   │     │ Benachrichtige │                 │
>                   │     │ Administrator  │                 │
>                   │     └──────┬─────────┘                 │
>                   │            │                           │
>                   ▼            ▼            ◄──────────────┘
>                  ╔═════════════════════════╗
>                  ║          ENDE           ║
>                  ╚═════════════════════════╝
> ```
>
> **Erläuterung:**
> - Oval (╔═╗): Start / Ende
> - Rechteck (┌─┐): Anweisung / Eingabe
> - Raute (◇): Bedingung / Verzweigung
> - Der Zähler `Versuche` wird bei jedem Durchlauf erhöht
> - Bei korrekter Eingabe endet das Programm mit Erfolg
> - Bei 3 Fehlversuchen: Sperrung + Admin-Benachrichtigung
> - Bei weniger als 3 Fehlversuchen: erneute Eingabe möglich

> [!example] Aufgabe 2 - PAP Aufgaben
> - Ergänze einen PAP für einen mobilen Roboter
> - Finde Fehler in vorgegebenen PAPs
> - PAP für Rechnungsnummernprüfung
> - PAP Zahlenrätsel mit Schreibtischtest

> [!success] Lösung
> **Mobiler Roboter (PAP ergänzen):**
> Der PAP steuert einen Roboter durch einen Parcours. Fehlende Elemente sind typischerweise:
> - Startbedingung / Initialisierung (Sensoren initialisieren, Startposition setzen)
> - Hinderniserkennung: Bedingung „Hindernis voraus?" → ja: ausweichen / nein: vorwärts fahren
> - Schleifenende: Bedingung „Ziel erreicht?" → ja: Stopp / nein: weiter navigieren
> - Fehlerbehandlung: Batterie leer → Notstopp und Meldung ausgeben
>
> **Fehler in PAPs finden:**
> Typische Fehler in vorgegebenen PAPs:
> - Fehlende Verbindungspfeile zwischen Symbolen
> - Falsche Symbol-Typen (z. B. Raute statt Rechteck für eine Anweisung)
> - Endlosschleifen ohne Abbruchbedingung
> - Mehrere Startpunkte oder kein Endpunkt
> - Pfeile die in falsche Richtung zeigen
> - Bedingungen ohne „ja"- oder „nein"-Beschriftung
>
> **PAP Rechnungsnummernprüfung:**
> Ziel: Prüfen, ob eine eingegebene Rechnungsnummer gültig ist.
> Ablauf:
> 1. Eingabe der Rechnungsnummer
> 2. Prüfe: Hat die Nummer genau 8 Stellen? → nein: Fehlerausgabe
> 3. Prüfe: Beginnt die Nummer mit „RE"? → nein: Fehlerausgabe
> 4. Prüfe: Sind die restlichen 6 Zeichen Ziffern? → nein: Fehlerausgabe
> 5. Ausgabe: „Rechnungsnummer gültig"
>
> **PAP Zahlenrätsel mit Schreibtischtest:**
> Der PAP für ein Zahlenrätsel (z. B. Zahl raten) wird durch einen **Schreibtischtest** manuell überprüft.
> Dabei wird der PAP schrittweise mit konkreten Beispielwerten durchgespielt und alle Variablenwerte
> in einer Tabelle festgehalten:
>
> | Schritt | Versuche | Eingabe | Zielzahl | Bedingung       | Ausgabe           |
> |---------|----------|---------|----------|-----------------|-------------------|
> | 1       | 0        | –       | 42       | –               | –                 |
> | 2       | 1        | 30      | 42       | 30 < 42 → wahr  | „Zu klein!"       |
> | 3       | 2        | 50      | 42       | 50 > 42 → wahr  | „Zu groß!"        |
> | 4       | 3        | 42      | 42       | 42 == 42 → wahr | „Richtig geraten" |

> [!example] Aufgabe 3 - Struktogramme
> - Lese vorgegebene Struktogramme und beschreibe den Ablauf
> - Erstelle ein Struktogramm (S. 524 A3, A4)
> - Erstelle ein Struktogramm für "Zufallszahl"

> [!success] Lösung
> **Struktogramm lesen – Beispiel: Summe berechnen**
>
> Das folgende Struktogramm berechnet die Summe der Zahlen 1 bis N:
> ```
> ┌────────────────────────────────────────┐
> │ Eingabe: N                             │
> ├────────────────────────────────────────┤
> │ Summe = 0                              │
> ├────────────────────────────────────────┤
> │ i = 1                                  │
> ├────────────────────────────────────────┤
> │ SOLANGE i <= N                         │
> │ ┌──────────────────────────────────┐   │
> │ │ Summe = Summe + i               │   │
> │ ├──────────────────────────────────┤   │
> │ │ i = i + 1                       │   │
> │ └──────────────────────────────────┘   │
> ├────────────────────────────────────────┤
> │ Ausgabe: Summe                         │
> └────────────────────────────────────────┘
> ```
> Ablauf: N wird eingelesen, der Zähler i läuft von 1 bis N,
> bei jedem Durchlauf wird i zur Summe addiert. Am Ende wird
> die Gesamtsumme ausgegeben.
>
> ---
>
> **Struktogramm: Zufallszahl (Zahlen-Ratespiel)**
>
> Der Computer wählt eine Zufallszahl zwischen 1 und 100.
> Der Spieler versucht, sie zu erraten. Nach jeder Eingabe
> gibt das Programm einen Hinweis: „zu groß", „zu klein" oder „richtig".
>
> ```
> ┌────────────────────────────────────────────────┐
> │ Zufallszahl = Zufallszahl(1, 100)              │
> ├────────────────────────────────────────────────┤
> │ Versuche = 0                                   │
> ├────────────────────────────────────────────────┤
> │ geraten = FALSCH                               │
> ├────────────────────────────────────────────────┤
> │ SOLANGE geraten = FALSCH                       │
> │ ┌──────────────────────────────────────────┐   │
> │ │ Eingabe: Tipp                           │   │
> │ ├──────────────────────────────────────────┤   │
> │ │ Versuche = Versuche + 1                 │   │
> │ ├──────────────────────────────────────────┤   │
> │ │        Tipp < Zufallszahl?              │   │
> │ │ ┌──────────────────┬───────────────┐    │   │
> │ │ │       ja         │     nein      │    │   │
> │ │ │ Ausgabe:         │ Tipp > Zahl?  │    │   │
> │ │ │ "Zu klein!"     ├───────┬───────┤    │   │
> │ │ │                 │  ja   │ nein  │    │   │
> │ │ │                 │"Zu    │geraten│    │   │
> │ │ │                 │groß!" │= WAHR │    │   │
> │ │ └──────────────────┴───────┴───────┘    │   │
> │ └──────────────────────────────────────────┘   │
> ├────────────────────────────────────────────────┤
> │ Ausgabe: "Richtig! Versuche: ", Versuche       │
> └────────────────────────────────────────────────┘
> ```
>
> **Aufbau-Erklärung:**
> - Außenrahmen = gesamter Algorithmus
> - Horizontal geteilte Blöcke = Sequenz (Schritt für Schritt)
> - SOLANGE-Block = Wiederholung (Schleife, kopfgesteuert)
> - Vertikal geteilter Block = Verzweigung (if / else)
> - Verschachtelungen entstehen durch Blöcke im Block

> [!example] Aufgabe 4 - Entscheidungstabellen (S. 533/524)
> Aufgabe 5: Aktien - Erstelle eine Entscheidungstabelle

> [!success] Lösung
> **Entscheidungstabelle: Aktienhandel**
>
> Szenario: Ein automatisches Handelssystem entscheidet, ob Aktien gekauft,
> gehalten oder verkauft werden sollen, basierend auf drei Bedingungen:
> - Kurs steigt (Trend positiv)
> - Kurs liegt unter dem Kaufkurs (Verlustposition)
> - Nachrichten sind positiv
>
> | Bedingungen / Aktionen          | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
> |---------------------------------|----|----|----|----|----|----|----|-----|
> | **Kurs steigt?**                | J  | J  | J  | J  | N  | N  | N  | N  |
> | **Kurs unter Kaufkurs?**        | J  | J  | N  | N  | J  | J  | N  | N  |
> | **Nachrichten positiv?**        | J  | N  | J  | N  | J  | N  | J  | N  |
> | **Aktien kaufen**               | X  |    | X  |    |    |    |    |    |
> | **Aktien halten**               |    | X  |    | X  |    |    | X  |    |
> | **Aktien verkaufen**            |    |    |    |    | X  |    |    | X  |
> | **Sofort verkaufen (Stop-Loss)**|    |    |    |    |    | X  |    |    |
>
> **Erläuterung der Regeln:**
> - **R1** (Kurs steigt + Verlust + pos. News): Kurs erholt sich → nachkaufen (Averaging)
> - **R2** (Kurs steigt + Verlust + neg. News): Vorsicht, nur halten und beobachten
> - **R3** (Kurs steigt + kein Verlust + pos. News): Guter Zeitpunkt → weiterkaufen
> - **R4** (Kurs steigt + kein Verlust + neg. News): Gewinne halten, abwarten
> - **R5** (Kurs fällt + Verlust + pos. News): Evtl. Erholung erwartet → verkaufen mit Limit
> - **R6** (Kurs fällt + Verlust + neg. News): Hoher Verlustdruck → sofortiger Stop-Loss-Verkauf
> - **R7** (Kurs fällt + kein Verlust + pos. News): Im Plus, aber fallend → halten, Nachrichten abwarten
> - **R8** (Kurs fällt + kein Verlust + neg. News): Verkaufen solange noch Gewinn vorhanden
>
> **Vollständigkeit:** 3 Bedingungen → 2³ = 8 Regeln → Tabelle ist vollständig.
> **Widerspruchsfreiheit:** Jede Regel führt zu genau einer Aktion → kein Widerspruch.

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
