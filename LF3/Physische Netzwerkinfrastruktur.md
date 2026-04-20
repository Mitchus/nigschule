---
fach: LF3
thema: Physische Netzwerkinfrastruktur
tags: [lf3, verkabelung, twisted-pair, lwl, wlan, passive-komponenten]
datum: 2026-04-20
typ: notiz
---

# Physische Netzwerkinfrastruktur

## Strukturierte Verkabelung (EN 50173 / ISO 11801)

Die universale Gebäudeverkabelung (UGV) stellt eine herstellerunabhängige, standardisierte Infrastruktur bereit.

### Drei Ebenen der UGV

| Ebene       | Bereich                    | Verbindung                    |
| ----------- | -------------------------- | ----------------------------- |
| **Primär**  | Campusverkabelung          | Gebäude ↔ Gebäude             |
| **Sekundär** | Gebäudeverkabelung        | Stockwerk ↔ Stockwerk (Steigzone) |
| **Tertiär** | Etagenverkabelung          | Verteiler ↔ Anschlussdose     |

### Channel-Link (Tertiäre Ebene)

```
Patchpanel → Verlegekabel → Anschlussdose → Patchkabel → Endgerät
   ↑                                                          ↑
Patchkabel                                              (max. 5m)
vom Switch
(max. 5m)
```

**Maximale Länge:** 100 m (davon max. 90 m Verlegekabel + 2× 5 m Patchkabel)

### Passive Komponenten

| Komponente         | Funktion                                    |
| ------------------ | ------------------------------------------- |
| **Verlegekabel**   | Feste Installation in Wänden/Kanälen        |
| **Patchkabel**     | Flexible Verbindung Switch↔Patchpanel, Dose↔PC |
| **Patchpanel**     | Zentrale Anschlussstelle im Rack            |
| **Anschlussdose**  | RJ45-Wanddose für Endgeräte                |
| **Netzwerkschrank** | 19"-Rack für aktive/passive Komponenten    |

---

## Twisted-Pair (TP) Kabel

Kupferkabel mit verdrillten Adernpaaren zur Reduzierung elektromagnetischer Störungen.

### Kategorien

| Kategorie | Max. Frequenz | Max. Geschwindigkeit | Einsatz                    |
| --------- | ------------- | -------------------- | -------------------------- |
| Cat 5e    | 100 MHz       | 1 Gbit/s             | Büro (Standard)            |
| Cat 6     | 250 MHz       | 1 Gbit/s             | Büro (besser)              |
| Cat 6a    | 500 MHz       | 10 Gbit/s            | Rechenzentrum, Büro        |
| Cat 7     | 600 MHz       | 10 Gbit/s            | Hochleistungsnetzwerke     |
| Cat 8     | 2000 MHz      | 25/40 Gbit/s         | Rechenzentren (kurz)       |

> [!info] Für ein typisches Büro reicht Cat 6a. Cat 8 (40 Gbit/s) ist nur für kurze Distanzen im Rechenzentrum sinnvoll.

### Abschirmung

| Kürzel  | Beschreibung                                    |
| ------- | ----------------------------------------------- |
| **UTP** | Ungeschirmt (Unshielded Twisted Pair)           |
| **FTP** | Foliengeschirmt (Foiled Twisted Pair)           |
| **STP** | Geflechtgeschirmt (Shielded Twisted Pair)       |
| **S/FTP** | Geflecht gesamt + Folie je Paar              |

### Belegungsstandards (RJ45)

| Standard  | Pin 1-2     | Pin 3-6     | Verwendung                  |
| --------- | ----------- | ----------- | --------------------------- |
| **T568A** | Weiß-Grün, Grün | Weiß-Orange, Orange | US-Standard        |
| **T568B** | Weiß-Orange, Orange | Weiß-Grün, Grün | Europäischer Standard |

> [!warning] Beide Seiten eines Patchkabels müssen den **gleichen Standard** verwenden (1:1 Kabel)! Crossover-Kabel sind bei modernen Switches dank Auto-MDI/X nicht mehr nötig.

---

## Lichtwellenleiter (LWL)

Glasfaserkabel zur Übertragung von Daten per Licht.

### Aufbau

```
┌─────────────────────────────┐
│  Kern (Core)                │ ← Licht wird hier übertragen
│  ┌───────────────────────┐  │
│  │  Mantel (Cladding)    │  │ ← Totalreflexion
│  │  ┌─────────────────┐  │  │
│  │  │  Coating/Buffer  │  │  │ ← Schutz
│  │  └─────────────────┘  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

### Single-Mode vs. Multi-Mode

| Eigenschaft    | Single-Mode           | Multi-Mode              |
| -------------- | --------------------- | ----------------------- |
| **Kerndurchmesser** | 9 µm             | 50/62,5 µm             |
| **Reichweite** | bis 100 km            | bis 2 km               |
| **Geschwindigkeit** | Sehr hoch        | Hoch                   |
| **Kosten**     | Teurer (Laser)        | Günstiger (LED)         |
| **Einsatz**    | WAN, Backbone         | LAN, Gebäudeverkabelung |

### Vorteile von LWL

- Keine elektromagnetische Störung (kein Crosstalk)
- Höhere Bandbreite als Kupfer
- Größere Reichweiten
- Abhörsicher
- Geringerer Platzbedarf

> [!info] Auf der tertiären Ebene (Büro) werden meist TP-Kabel statt LWL verwendet, da LWL-Stecker und -Adapter deutlich teurer sind und TP für 1-10 Gbit/s ausreicht.

---

## Funkübertragung (WLAN / Wi-Fi)

### Aktuelle Wi-Fi Standards

| Standard | Wi-Fi | Max. Geschwindigkeit | Frequenzbänder        |
| -------- | ----- | -------------------- | --------------------- |
| 802.11n  | Wi-Fi 4 | 600 Mbit/s         | 2,4 + 5 GHz          |
| 802.11ac | Wi-Fi 5 | 6,9 Gbit/s         | 5 GHz                 |
| 802.11ax | Wi-Fi 6 | 9,6 Gbit/s         | 2,4 + 5 GHz          |
| 802.11ax | Wi-Fi 6E | 9,6 Gbit/s        | 2,4 + 5 + 6 GHz      |

### Frequenzbänder

| Band       | Reichweite     | Durchdringung | Geschwindigkeit |
| ---------- | -------------- | ------------- | --------------- |
| **2,4 GHz** | Groß          | Gut           | Niedriger       |
| **5 GHz**  | Mittel          | Mittel        | Hoch            |
| **6 GHz**  | Klein           | Gering        | Sehr hoch       |

### Nachteile von WLAN

- Geteiltes Medium (Bandbreite wird aufgeteilt)
- Störanfällig (andere Geräte, Wände, Wetter)
- Sicherheitsrisiken (Funkwellen sind empfangbar)
- Geringere Geschwindigkeit als Kabel

### WLAN-Sicherheit

| Verschlüsselung | Sicherheit   | Status         |
| ---------------- | ------------ | -------------- |
| WEP              | Unsicher     | Veraltet       |
| WPA              | Mittel       | Veraltet       |
| WPA2             | Gut          | Standard       |
| WPA3             | Sehr gut     | Aktuell        |

Weitere Maßnahmen: SSID verstecken, MAC-Filterung, RADIUS-Authentifizierung

---

## Aufgaben

> [!example] Aufgabe 1 - Strukturierte Verkabelung (S. 311-314)
> 1. Welche Funktion erfüllt die UGV?
> 2. In welche Teile lässt sich die UGV unterteilen?
> 3. Welche passiven Komponenten enthält die UGV?

> [!example] Aufgabe 2 - Twisted-Pair
> 1. Kundengespräch: Sind 40 Gbit/s TP-Leitungen für ein Büro sinnvoll?
> 2. Muss beim Crimpen eine Seite T568A und die andere T568B sein?
> 3. Brauchen elektrische Übertragungsmedien Abschirmung?

> [!example] Aufgabe 3 - LWL
> 1. Warum werden auf der tertiären Ebene meist TP statt LWL eingesetzt?
> 2. Skizziere den Aufbau eines LWL
> 3. Erkläre Single-Mode und Multi-Mode
> 4. Nenne drei Vorteile von LWL

> [!example] Aufgabe 4 - WLAN
> 1. Nachteile der Funkübertragung?
> 2. Aktueller Wi-Fi-Standard mit Geschwindigkeit und Frequenzen?
> 3. Drei Frequenzbänder vergleichen
> 4. Vorteile von WLAN für Unternehmen?
> 5. Sicherheitsmaßnahmen beschreiben

> [!example] Aufgabe 5 - Bedarfsanalyse ZeroTake Coffee
> Bestimme anhand des Lastenhefts und Lageplans alle passiven Netzwerkkomponenten:
> - Verkabelung (Typ, Länge)
> - Patchkabel (Switch↔Patchpanel)
> - Unterputzdosen RJ45
> - Patchpanel
> Recherchiere Preise und erstelle eine Aufstellung (Einzelpreis, Gesamt, Link, Netto/Brutto)

---

## Materialien

- ![[files/LE4_02_Tafelbild_Strukturierte_Verkabelung.pdf]]
- ![[files/LE4_00_ZeroTake_Coffee_Grundriss.pdf]]
- ![[files/LE4_00_Lastenheftauszug_ZeroTake_Coffee_k.pdf]]

---

## Siehe auch

- [[Netzwerk-Grundlagen und OSI]]
- [[Aktive Komponenten und Konfiguration]]
