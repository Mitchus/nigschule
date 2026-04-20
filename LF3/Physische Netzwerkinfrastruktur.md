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

> [!success] Lösung
> **1. Funktion der UGV (Universale Gebäudeverkabelung):**
> Die UGV stellt eine herstellerunabhängige, genormte Netzwerkinfrastruktur nach EN 50173 / ISO 11801 bereit. Sie bildet die physische Grundlage für alle Datendienste (LAN, Telefonie, Gebäudeautomation) in einem Gebäude – unabhängig von der aktiven Technik. Dadurch können Netzwerkkomponenten verschiedener Hersteller einfach integriert und ausgetauscht werden.
>
> **2. Unterteilung der UGV in drei Ebenen:**
> | Ebene | Bereich | Verbindung |
> | ----- | ------- | ---------- |
> | **Primär (Campusverkabelung)** | Außenbereich zwischen Gebäuden | Gebäudeverteiler ↔ Gebäudeverteiler (LWL) |
> | **Sekundär (Gebäudeverkabelung)** | Vertikale Verbindung im Gebäude | Gebäudeverteiler ↔ Etagenverteiler (Steigzone) |
> | **Tertiär (Etagenverkabelung)** | Horizontale Verbindung je Etage | Etagenverteiler ↔ Anschlussdose am Arbeitsplatz |
>
> **3. Passive Komponenten der UGV:**
> | Komponente | Funktion |
> | ---------- | -------- |
> | **Verlegekabel** | Fest in Wänden/Kabelkanälen installiertes Kabel (TP oder LWL) |
> | **Patchkabel** | Flexible Verbindung zwischen Switch und Patchpanel bzw. Dose und Endgerät |
> | **Patchpanel** | Zentrales Anschlussfeld im Rack – bündelt alle Verlegekabel |
> | **Anschlussdose (RJ45)** | Wanddose als Endpunkt des Verlegekabels am Arbeitsplatz |
> | **Netzwerkschrank (Rack)** | 19"-Gehäuse zur geordneten Aufnahme aller aktiven und passiven Komponenten |
> | **Kabelkanal** | Führt und schützt Kabel in Wänden, Böden und Decken |

> [!example] Aufgabe 2 - Twisted-Pair
> 1. Kundengespräch: Sind 40 Gbit/s TP-Leitungen für ein Büro sinnvoll?
> 2. Muss beim Crimpen eine Seite T568A und die andere T568B sein?
> 3. Brauchen elektrische Übertragungsmedien Abschirmung?

> [!success] Lösung
> **1. Sind 40 Gbit/s TP-Leitungen (Cat 8) für ein Büro sinnvoll?**
> Nein, in der Regel nicht. Cat 8 (40 Gbit/s) ist für sehr kurze Distanzen im Rechenzentrum konzipiert (max. 30 m) und deutlich teurer als Cat 6a. Für ein typisches Büro ist **Cat 6a mit 10 Gbit/s** mehr als ausreichend und zukunftssicher. Der Mehraufwand für Cat 8 ist wirtschaftlich nicht gerechtfertigt, da auch die übrige Netzwerkhardware (Switches, Server-NICs) kaum 40 Gbit/s unterstützt.
>
> **2. Muss beim Crimpen eine Seite T568A und die andere T568B belegt sein?**
> Nein – das wäre ein **Crossover-Kabel**, das früher für direkte Gerät-zu-Gerät-Verbindungen verwendet wurde (z. B. PC ↔ PC). Ein normales **Patchkabel** muss auf **beiden Seiten den gleichen Standard** (T568A oder T568B) verwenden, sodass Pin 1 auf Pin 1 trifft usw. (1:1-Kabel). Moderne Netzwerkgeräte unterstützen **Auto-MDI/X**, womit Crossover-Kabel ohnehin überflüssig sind.
>
> **3. Brauchen elektrische Übertragungsmedien Abschirmung?**
> Es kommt auf den Einsatzbereich an. In störungsarmen Umgebungen (typisches Büro) reicht **UTP** (ungeschirmt) aus. In industriellen Umgebungen, bei langen Kabelwegen neben Stromleitungen oder in Bereichen mit starken elektromagnetischen Feldern ist Abschirmung (**FTP, STP oder S/FTP**) notwendig, um Crosstalk und Interferenzen zu reduzieren. Generell gilt: je kritischer die Umgebung, desto höher die empfohlene Abschirmklasse.

> [!example] Aufgabe 3 - LWL
> 1. Warum werden auf der tertiären Ebene meist TP statt LWL eingesetzt?
> 2. Skizziere den Aufbau eines LWL
> 3. Erkläre Single-Mode und Multi-Mode
> 4. Nenne drei Vorteile von LWL

> [!success] Lösung
> **1. Warum TP statt LWL auf der tertiären Ebene?**
> Auf der tertiären Ebene (Etagenverkabelung bis zum Arbeitsplatz) sind die Distanzen kurz (< 100 m) und die benötigten Bandbreiten mit Cat 6a (10 Gbit/s) gut abgedeckt. LWL-Komponenten (Transceiver, Stecker, Spleißgeräte) sind erheblich teurer und aufwändiger zu installieren als TP. Da kein wirtschaftlicher Vorteil besteht, wird LWL auf der tertiären Ebene nur in Ausnahmefällen (z. B. EMV-kritische Umgebungen) eingesetzt.
>
> **2. Aufbau eines LWL:**
> ```
> [Coating/Buffer] ← äußerer Schutzmantel
>   [Cladding]     ← Mantel aus Glas/Kunststoff (niedrigerer Brechungsindex)
>     [Core]       ← Kern (Lichtleiter, höherer Brechungsindex)
> ```
> Das Licht wird im Kern durch **Totalreflexion** an der Grenze zwischen Kern und Mantel geleitet.
>
> **3. Single-Mode vs. Multi-Mode:**
> | Eigenschaft | Single-Mode | Multi-Mode |
> | ----------- | ----------- | ---------- |
> | Kerndurchmesser | 9 µm | 50 / 62,5 µm |
> | Lichtquelle | Laser | LED |
> | Reichweite | bis 100 km | bis 2 km |
> | Bandbreite | Sehr hoch | Hoch |
> | Kosten | Höher | Geringer |
> | Einsatz | WAN, Backbone, Primärverkabelung | LAN, Gebäudeverkabelung |
>
> Single-Mode lässt nur einen Lichtpfad (Mode) zu → weniger Dispersion → größere Reichweite. Multi-Mode lässt viele Lichtpfade zu → günstigere Komponenten, aber begrenzte Distanz.
>
> **4. Drei Vorteile von LWL:**
> - **Keine elektromagnetische Störanfälligkeit** – ideal in industriellen oder EMV-belasteten Umgebungen
> - **Sehr große Reichweiten** – bis 100 km ohne Repeater (Single-Mode)
> - **Abhörsicher** – Licht tritt nicht aus dem Kabel aus, physikalisches Anzapfen ist sofort erkennbar

> [!example] Aufgabe 4 - WLAN
> 1. Nachteile der Funkübertragung?
> 2. Aktueller Wi-Fi-Standard mit Geschwindigkeit und Frequenzen?
> 3. Drei Frequenzbänder vergleichen
> 4. Vorteile von WLAN für Unternehmen?
> 5. Sicherheitsmaßnahmen beschreiben

> [!success] Lösung
> **1. Nachteile der Funkübertragung:**
> - Geteiltes Medium: Alle Geräte teilen sich die verfügbare Bandbreite
> - Störanfälligkeit durch Wände, andere Funkgeräte (Mikrowellen, Bluetooth), Wetterbedingungen
> - Sicherheitsrisiko: Funksignale können außerhalb des Gebäudes empfangen werden
> - Geringere und schwankende Übertragungsgeschwindigkeit im Vergleich zu Kabelverbindungen
> - Latenz kann höher sein als bei kabelgebundenen Lösungen
>
> **2. Aktueller Wi-Fi-Standard:**
> Der aktuellste Standard ist **Wi-Fi 6E (IEEE 802.11ax)** mit bis zu **9,6 Gbit/s** (theoretisch). Er nutzt alle drei Frequenzbänder: **2,4 GHz, 5 GHz und 6 GHz**. Wi-Fi 6 (ohne E) ist ebenfalls aktuell und nutzt 2,4 + 5 GHz.
>
> **3. Frequenzbänder im Vergleich:**
> | Band | Reichweite | Wanddurchdringung | Geschwindigkeit | Typischer Einsatz |
> | ---- | ---------- | ----------------- | --------------- | ----------------- |
> | **2,4 GHz** | Groß (> 50 m) | Gut | Niedrig | Smarthome, IoT, weite Räume |
> | **5 GHz** | Mittel (~ 30 m) | Mittel | Hoch | Büro, Streaming, Gaming |
> | **6 GHz** | Klein (~ 15 m) | Gering | Sehr hoch | Kurzstrecke, hohe Dichte |
>
> **4. Vorteile von WLAN für Unternehmen:**
> - Flexibler Arbeitsplatz: Mitarbeiter können sich frei im Gebäude bewegen
> - Einfache Anbindung von mobilen Geräten (Laptops, Tablets, Smartphones)
> - Kein Aufwand für zusätzliche Kabelinstallation bei neuen Arbeitsplätzen
> - Gäste-WLAN ermöglicht sicheren Internetzugang für Besucher ohne Zugriff auf interne Systeme
> - Skalierbar durch einfaches Hinzufügen weiterer Access Points
>
> **5. Sicherheitsmaßnahmen:**
> | Maßnahme | Beschreibung |
> | -------- | ------------ |
> | **WPA3-Verschlüsselung** | Aktueller Standard, ersetzt WPA2; schützt Datenübertragung |
> | **Starkes SSID-Passwort** | Mindestens 12 Zeichen, Groß-/Kleinbuchstaben, Zahlen, Sonderzeichen |
> | **SSID verstecken** | SSID-Broadcast deaktivieren – leichte Hürde gegen opportunistische Angreifer |
> | **MAC-Filterung** | Nur bekannte MAC-Adressen erhalten Zugang (aufwändig, umgehbar) |
> | **Gäste-WLAN trennen** | Separate SSID mit eigenem VLAN – isoliert Gäste vom Firmennetzwerk |
> | **RADIUS-Authentifizierung** | Unternehmensauthentifizierung per 802.1X – jeder Nutzer mit eigenem Login |

> [!example] Aufgabe 5 - Bedarfsanalyse ZeroTake Coffee
> Bestimme anhand des Lastenhefts und Lageplans alle passiven Netzwerkkomponenten:
> - Verkabelung (Typ, Länge)
> - Patchkabel (Switch↔Patchpanel)
> - Unterputzdosen RJ45
> - Patchpanel
> Recherchiere Preise und erstelle eine Aufstellung (Einzelpreis, Gesamt, Link, Netto/Brutto)

> [!success] Lösung
> Musteraufstellung für die ZeroTake Coffee UG (10 Arbeitsplätze, 2 Netzwerkdrucker, 1. Etage):
>
> **Annahmen:** 10 Arbeitsplätze + 2 Drucker = 12 Anschlussdosen; pro Arbeitsplatz 1 Dose; durchschnittliche Kabellänge ~15 m je Stich + Reserve; Budget max. 1.750 €.
>
> | Pos. | Komponente | Typ/Spezifikation | Menge | Einzelpreis (netto) | Gesamt (netto) | Gesamt (brutto) |
> | ---- | ---------- | ----------------- | ----- | ------------------- | -------------- | --------------- |
> | 1 | Verlegekabel | Cat 6a S/FTP, 100 m Rolle | 3 | 45,00 € | 135,00 € | 160,65 € |
> | 2 | Anschlussdosen RJ45 | Cat 6a Keystonemodul + Rahmen UP | 14 | 8,50 € | 119,00 € | 141,61 € |
> | 3 | Patchpanel | 24-Port Cat 6a, 1 HE, 19" | 1 | 55,00 € | 55,00 € | 65,45 € |
> | 4 | Patchkabel (Switch↔Patchpanel) | Cat 6a, 0,5 m, RJ45 | 14 | 3,50 € | 49,00 € | 58,31 € |
> | 5 | Patchkabel (Dose↔Endgerät) | Cat 6a, 2 m, RJ45 | 14 | 4,50 € | 63,00 € | 74,97 € |
> | 6 | Kabelkanal | 40×60 mm, 2 m Stücke | 10 | 6,00 € | 60,00 € | 71,40 € |
> | 7 | Netzwerkschrank | 12 HE, 19", abschließbar | 1 | 180,00 € | 180,00 € | 214,20 € |
> | 8 | Kleinmaterial (Dübel, Klemmen) | Sortiment | 1 | 25,00 € | 25,00 € | 29,75 € |
> | | **Summe** | | | | **686,00 €** | **816,34 €** |
>
> Das Budget von 1.750 € wird eingehalten. Der verbleibende Betrag steht für aktive Komponenten (Switch, Access Points, Router) zur Verfügung.
> *Hinweis: Genaue Mengen und Längen sind aus dem Lageplan zu entnehmen. Preise sind Richtwerte (z. B. Reichelt, Conrad, Amazon Business).*

---

## Materialien

- ![[files/LE4_02_Tafelbild_Strukturierte_Verkabelung.pdf]]
- ![[files/LE4_00_ZeroTake_Coffee_Grundriss.pdf]]
- ![[files/LE4_00_Lastenheftauszug_ZeroTake_Coffee_k.pdf]]

---

## Siehe auch

- [[Netzwerk-Grundlagen und OSI]]
- [[Aktive Komponenten und Konfiguration]]
