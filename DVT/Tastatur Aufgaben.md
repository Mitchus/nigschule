---
fach: DVT
thema: Tastatur Aufgaben
tags: [hardware, eingabe]
datum: 2024-04-18
typ: aufgabe
---
1. **Unterschied QUERTZ- und QUERTY-Tastatur:**
   - **QUERTZ:** Buchstabenanordnung Q-W-E-R-T-Z
   - **QUERTY:** Buchstabenanordnung Q-W-E-R-T-Y
   - Hat ein anderes Layout

2. **Tastenkombination (Alt) + (Druck) in Windows:**
   - Erstellt Screenshot des aktiven Fensters in Zwischenablage

3. **Verwendung der „fn-Taste“ auf portablen Geräten:**
   - Zusätzliche Funktionen auf Tasten (z.B. Helligkeit, Lautstärke)

4. **Erzeugen des @-Zeichens bei E-Mail-Adressen:**
   - Tastenkombination: `Alt Gr` + `Q`

5. **Änderung durch (Einfg)-Taste in Textverarbeitungsprogramm:**
   - Wechsel in Einfügemodus, neue Zeichen werden eingefügt

6. **Anschlussmöglichkeiten von Tastaturen an Rechner:**
   - Kabelgebunden (USB)
   - Drahtlos (Bluetooth/Funk)

7. **Arten der Datenübertragung von Tastatur zum Rechner:**
   - Kabelgebunden (z.B. USB)
   - Bluetooth
   - Funk

8. **Vier Tasten-Arten:**
   - Buchstabentasten
   - Funktionstasten (F-Tasten)
   - Sondertasten (z.B. Enter, Shift)
   - Nummerntasten

1. **Tastaturzuordnung zu Aussagen (A), (B), (C):**
   - 1: (C) Rubberdome
   - 2: (B) Mechanische Tastatur
   - 3: (A) Funk-/Bluetooth-Tastatur

# 1. Vorteile von LEDs in Scannern

LEDs in Scannern bieten:
- Energieeffizienz
- Kompaktheit
- Schnelles Ein- und Ausschalten
- Farbstabilität
- Umweltfreundlichkeit

# 2. Bedeutung von Single-Pass-Scanner

Ein Single-Pass-Scanner erfasst die Vorlage in einem Durchgang, was schneller ist.

# 3. Funktion eines OCR-Programms

OCR wandelt gedruckten Text in editierbaren digitalen Text um.

# 4. Scannerauflösung und Angabe

Scannerauflösung (in dpi) bestimmt Detailgenauigkeit. Typische Werte:
- Flachbett: 600-4800 dpi
- Einzug: 300-900 dpi
- Diascanner: 1200-9600 dpi

# 5. TWAIN-Standard

TWAIN ist ein Kommunikationsprotokoll für Scanner-Software-Integration.

# 6. Funktionsweise eines Flachbettscanners

Vorlage auf Glasplatte, bewegliche Scaneinheit scannt von unten.

# 7. Aufbau eines Flachbettscanners

Besteht aus Umlenkspiegeln, Scaneinheit/Vorlage, LEDs (Lichtquelle), Sensoren.

![[Flachbettscanner]]# Projektplanung: Netzwerkinfrastruktur 1. OG ZeroTake Coffee

## 1. Bestandsaufnahme & Anforderungen

### Aus dem Grundriss ermittelte Anschlusspunkte:

Basierend auf den grünen Markierungen im Plan:

- **R1.1:** 2 Doppeldosen (4 Ports)
- **R1.2:** 2 Doppeldosen (4 Ports)
- **R1.3:** 2 Doppeldosen (4 Ports)
- **R1.4:** 3 Doppeldosen (6 Ports)
- **R1.5:** 1 Doppeldose (2 Ports)
- **R1.6:** Serverraum (nur Infrastruktur)
- **EG (R0.2):** 1 Access Point für Gast-WLAN

**Gesamt:** 10 Doppeldosen = 20 Ports im 1. OG + 1 AP im EG

---

## 2. Materialliste mit Preisen

### 2.1 Verkabelung

|Position|Artikel|Menge|Einzelpreis|Gesamt|Bezugsquelle|
|---|---|---|---|---|---|
|1|**Verlegekabel Cat. 6A S/FTP** 500m Rolle (LSZH)|1|220,00 €|220,00 €|Reichelt / Conrad|
|2|**UAE-Doppeldosen** (2x RJ45, Cat. 6A, Unterputz)|10|8,50 €|85,00 €|Reichelt|
|3|**Keystones RJ45** Cat. 6A (Reserve)|5|3,20 €|16,00 €|Reichelt|

**Erklärung Verkabelung:**

- Cat. 6A statt Cat. 7: Kostengünstiger, bis 10 Gbit/s, erfüllt aktuelle Standards (EN 50173)
- 500m reichen für ca. 50m durchschnittliche Kabellänge pro Dose + Reserve
- S/FTP = Schirmung gegen Störungen

---

### 2.2 Patchpanel & Verteilung

|Position|Artikel|Menge|Einzelpreis|Gesamt|Bezugsquelle|
|---|---|---|---|---|---|
|4|**Patchpanel 24-Port** Cat. 6A, 19", 1HE|1|65,00 €|65,00 €|Reichelt|
|5|**Switch 24-Port Gigabit** (unmanaged, energieeffizient)|1|95,00 €|95,00 €|TP-Link TL-SG1024D|
|6|**Patchkabel Cat. 6** 0,5m (grau)|24|2,10 €|50,40 €|Reichelt|
|7|**Patchkabel Cat. 6** 2m (blau, Uplink)|2|3,50 €|7,00 €|Reichelt|

**Erklärung Patchpanel:**

- 24 Ports: 20 für Dosen + 2 Uplinks (EG + Reserve) + 2 Reserve
- Unmanaged Switch: Kostengünstig, niedriger Stromverbrauch (~10W)

---

### 2.3 WLAN-Infrastruktur

|Position|Artikel|Menge|Einzelpreis|Gesamt|Bezugsquelle|
|---|---|---|---|---|---|
|8|**Access Point TP-Link EAP225** (Dual-Band, PoE, Decken-/Wandmontage)|2|65,00 €|130,00 €|Amazon / Reichelt|
|9|**PoE-Injektor** (802.3af)|2|12,50 €|25,00 €|TP-Link TL-PoE150S|

**Erklärung WLAN:**

- 1x AP für 1. OG (zentral in R1.4 oder Flur)
- 1x AP für EG Café-Bereich (R0.2)
- PoE = Stromversorgung über Netzwerkkabel (keine Extra-Steckdosen nötig)
- Getrennte Netzwerke möglich (Mitarbeiter/Gast-WLAN)

---

### 2.4 Rack-Zubehör & Kleinmaterial

|Position|Artikel|Menge|Einzelpreis|Gesamt|Bezugsquelle|
|---|---|---|---|---|---|
|10|**19" Rackschienen** (falls Rack keine hat)|1 Set|25,00 €|25,00 €|Conrad|
|11|**Kabelbinder** (100 Stück)|1|8,00 €|8,00 €|Baumarkt|
|12|**Beschriftungsband** für Labelgerät|2|6,50 €|13,00 €|Amazon|
|13|**Werkzeugset** (LSA-Auflegewerkzeug, Crimpzange RJ45)|-|-|0,00 €|Vorhanden|

---

## 3. Gesamtkalkulation

|Kategorie|Netto|MwSt. (19%)|Brutto|
|---|---|---|---|
|Verkabelung|321,00 €|60,99 €|381,99 €|
|Patchpanel & Switch|217,40 €|41,31 €|258,71 €|
|WLAN|155,00 €|29,45 €|184,45 €|
|Kleinmaterial|46,00 €|8,74 €|54,74 €|
|**GESAMT**|**739,40 €**|**140,49 €**|**879,89 €**|

**✓ Budget: 1.750 € → Einhaltung mit Puffer von 870 €**

---

## 4. Verlegungsplan

### 4.1 Kabelwege (Stern-Topologie von R1.6)

Alle Kabel laufen vom **Serverraum R1.6** sternförmig zu den Dosen:

```
R1.6 (Serverraum, 19" Rack)
├── Patchpanel 24-Port
├── Switch 24-Port
├── PoE-Injektoren (2x)
│
├─── nach R1.1 (2 Dosen) → Verlegung durch Brüstungskanal Westwand
├─── nach R1.2 (2 Dosen) → Verlegung durch Brüstungskanal Südwand
├─── nach R1.3 (2 Dosen) → Verlegung durch Brüstungskanal Südwand
├─── nach R1.4 (3 Dosen) → Verlegung durch Brüstungskanal Nordwand
├─── nach R1.5 (1 Dose) → Verlegung durch Brüstungskanal Ostwand
├─── Uplink EG → Vorhandenes Cat. 7 Kabel zum EG-Switch
└─── AP 1. OG → Zentrale Position (Empfehlung: Decke Flur oder R1.4)
```

**Vom EG-Switch:**

```
R0.5 (EG-Serverraum)
└─── nach R0.2 (Café) → AP für Gast-WLAN
```

---

### 4.2 Konkrete Verlegungsschritte

#### **Schritt 1: Kabel vorbereiten & kennzeichnen**

- 500m Rolle Cat. 6A bereitlegen
- Kabel für jeden Raum vorher beschriften (z.B. "R1.1-D1", "R1.1-D2")
- Kabellängen großzügig bemessen (+ 2m Reserve pro Kabel)

#### **Schritt 2: Verkabelung vom Rack zu den Dosen**

1. **Start im Serverraum R1.6:**
    
    - Kabel vom Rack durch Brüstungskanal führen
    - An Ecken/Abzweigungen mit Kabelbindern fixieren
2. **Pro Raum:**
    
    - Kabel durch Brüstungskanal bis zur markierten Position ziehen
    - Am Zielort ca. 30cm Überlänge für Montage lassen
    - UAE-Dose in Brüstungskanal einbauen
    - Adern nach T568A oder T568B Standard auflegen (Farbcode beachten!)
    - **Wichtig:** Einheitlich T568B verwenden (in Deutschland üblich)
3. **Zurück im Serverraum:**
    
    - Alle Kabel ins Rack führen
    - Beschriften mit selbstklebenden Labels
    - An Patchpanel anschließen (gleiche Farbcodierung wie Dosen!)

#### **Schritt 3: Patchpanel & Switch im Rack**

```
19" Rack Aufbau (von oben nach unten):
┌─────────────────────────┐
│ 1 HE: Patchpanel 24-Port│  ← Hier kommen alle Wanddosen an
├─────────────────────────┤
│ 1 HE: Switch 24-Port    │  ← Verbindung zum Patchpanel mit kurzen Patchkabeln
├─────────────────────────┤
│ Freiraum für PoE-Inject.│  ← Neben dem Rack oder auf Boden
└─────────────────────────┘
```

**Verkabelung im Rack:**

- Patchpanel Port 1-20: Dosen R1.1 bis R1.5
- Patchpanel Port 21: Uplink zum EG (Cat. 7 Kabel)
- Patchpanel Port 22: Access Point 1. OG
- Patchpanel Port 23-24: Reserve

**Vom Patchpanel zum Switch:**

- Mit 0,5m Patchkabeln entsprechende Ports verbinden
- Ports 1-20: Arbeitsplätze
- Port 21: Uplink EG
- Port 22: AP über PoE-Injektor

#### **Schritt 4: Access Points installieren**

**AP im 1. OG (z.B. Flurdecke oder R1.4):**

1. Netzwerkkabel vom Switch-Port über PoE-Injektor zum AP-Standort
2. AP an Decke/Wand montieren (Montageplatte verwenden)
3. Kabel anschließen (PoE liefert Strom + Daten)

**AP im EG Café (R0.2):**

1. Kabel vom EG-Switch zu R0.2 verlegen
2. Über PoE-Injektor anschließen
3. AP im vorderen Café-Bereich montieren

#### **Schritt 5: Dokumentation**

**Patchpanel-Beschriftung (wie im EG-Beispiel):**

```
Port | Raum  | Bezeichnung    | Typ
-----|-------|----------------|------
01   | R1.1  | Arbeitsplatz 1 | Doppeldose
02   | R1.1  | Arbeitsplatz 2 | Doppeldose
03   | R1.2  | Arbeitsplatz 3 | Doppeldose
...
21   | Uplink| EG-Serverraum  | Cat. 7
22   | AP-1OG| Access Point   | PoE
```

---

## 5. Verkabelungsschema (Beispiel R1.4)

```
Serverraum R1.6                          Raum R1.4 (3 Doppeldosen)
┌──────────────┐                         ┌──────────────┐
│  19" Rack    │                         │ Brüstungs-   │
│ ┌──────────┐ │                         │ kanal        │
│ │Patchpanel│ │  Cat. 6A S/FTP         │ ┌──────┐     │
│ │Port 10───┼─┼─────────────────────────┼─┤Dose 1│     │ PC
│ │Port 11───┼─┼─────────────────────────┼─┤Dose 2│     │ Drucker
│ │Port 12───┼─┼─────────────────────────┼─┤Dose 3│     │ VoIP
│ └──────────┘ │                         │ └──────┘     │
│ ┌──────────┐ │                         └──────────────┘
│ │ Switch   │ │
│ │ 24-Port  │ │ 0,5m Patchkabel
│ │Port 10◄──┤ │
│ └──────────┘ │
└──────────────┘
```

---

## 6. Zeitplanung (grob)

|Phase|Dauer|Beschreibung|
|---|---|---|
|Vorbereitung|1h|Material bereitstellen, Räume vorbereiten|
|Verkabelung R1.1-R1.5|4-6h|Kabel ziehen, Dosen montieren|
|Rack-Aufbau R1.6|2h|Patchpanel, Switch installieren & patchen|
|WLAN-Installation|2h|Access Points montieren & konfigurieren|
|Testen & Dokumentation|2h|Durchgangstests, Beschriftung, Doku|
|**GESAMT**|**11-13h**|Für 1-2 Personen|

---

## 7. Tests & Inbetriebnahme

### 7.1 Kabeltests

- **Durchgangsprüfung:** Alle 20 Ports mit Kabeltester prüfen (Verkabelungsfehler?)
- **Längen prüfen:** Max. 90m Installationskabel + 10m Patchkabel = 100m gesamt
- **Schirmung prüfen:** Bei S/FTP wichtig für Störsicherheit

### 7.2 Netzwerk-Tests

- Switch einschalten → Link-LEDs müssen grün leuchten
- PC an jede Dose anschließen → IP per DHCP erhalten
- Geschwindigkeitstest: Mind. 1 Gbit/s zwischen Clients
- WLAN-Messung: Signalstärke in allen Bereichen > -70 dBm

### 7.3 WLAN-Konfiguration

- **SSID Mitarbeiter:** "ZeroTake-Staff" (WPA3, versteckt)
- **SSID Gäste:** "ZeroTake-Guest" (WPA2, sichtbar, isoliert)
- Gastnetzwerk: Bandbreitenbegrenzung, kein Zugriff auf internes Netz

---

## 8. Optimierungen & Hinweise

### Energieeffizienz (im Budget berücksichtigt):

✓ Unmanaged Switch: ~10W statt managed ~25W  
✓ PoE-Injektoren statt PoE-Switch: ~200€ Ersparnis  
✓ LEDs nachts automatisch dimmen (AP-Einstellung)

### Zukunftssicherheit:

✓ Cat. 6A: Bereit für 10 Gbit/s  
✓ 24-Port Panel: 4 Ports Reserve für Erweiterung  
✓ Access Points: Firmware-Updates für Jahre garantiert

### Einhaltung Standards:

✓ EN 50173 (Verkabelung)  
✓ ISO/IEC 11801 (Strukturierte Verkabelung)  
✓ T568B Farbcode (Deutschland-Standard)

---

## 9. Bezugsquellen-Übersicht

**Hauptlieferanten:**

- **Reichelt Elektronik:** Kabel, Dosen, Patchpanel, Kleinteile
- **Amazon Business:** Access Points, PoE-Injektoren (oft günstiger)
- **Conrad Electronic:** Alternative für Notbestellungen

**Lieferzeit:** 2-3 Werktage  
**Versandkosten:** Ab 60€ meist versandkostenfrei

---

**Gesamtkosten: 879,89 € (inkl. MwSt.)**  
**Budget-Ausnutzung: 50,3% von 1.750 €**  
**Puffer: 870 € für unvorhergesehene Kosten oder Upgrades**

Brauchst du noch Details zu bestimmten Punkten oder eine Visualisierung der Verkabelung? 🔧