## Slide 1: Das Problem - Warum DevOps?

**Hauptpunkte:**

- **Traditionelles Silo-Problem**: Entwickler und Operations arbeiten komplett getrennt mit unterschiedlichen Zielen
    
    - Devs wollen Innovation und neue Features pushen → schnelle Änderungen
    - Ops will Stabilität und Sicherheit → keine Änderungen
    - Führt zu ständigen Konflikten
- **"Works on my machine" Syndrom**:
    
    - Dev entwickelt lokal, funktioniert perfekt
    - Deployment in Production schlägt fehl
    - Schuldzuweisungen zwischen Teams beginnen
- **Release-Zyklen früher**:
    
    - Monate bis Jahre zwischen Releases (z.B. Windows Vista: 5 Jahre Entwicklung)
    - Manuelle Deployments → fehleranfällig, stressig, oft nachts/am Wochenende

**Background:**

- **Patrick Debois** (belgischer IT-Consultant):
    - Erfand 2009 den Begriff "DevOps"
    - Organisierte erste "DevOpsDays" Konferenz in Gent
    - Frustriert über die Kluft zwischen Dev und Ops in seinen Projekten
    - Wollte beide Welten zusammenbringen

---

## Slide 2: Was ist DevOps?

**Hauptpunkte:**

- **Nicht nur Tools!** Häufiger Fehler: DevOps = Jenkins + Docker
    
- DevOps ist eine **Philosophie/Kultur**: Mindset-Change
    
- **Drei Säulen:**
    
    1. **Kultur**: Zusammenarbeit statt Blame-Game
    2. **Methoden**: Agile Praktiken, Automatisierung
    3. **Tools**: Jenkins, GitLab CI, Docker, Kubernetes etc.
- **Kernziel**: Time-to-Market reduzieren
    
    - Von Monaten auf Stunden/Tage
    - Beispiel: Amazon deployt alle 11,6 Sekunden (!)
- **"You build it, you run it"** (Amazon-Prinzip):
    
    - Wer den Code schreibt, ist auch für den Betrieb verantwortlich
    - Erhöht Qualitätsbewusstsein
    - Dev muss nachts nicht raus wenn's brennt → schreibt besseren Code

**Praxis-Beispiel für Vortrag:** "Netflix deployt täglich tausende Male in Production - ohne dass ihr als User was merkt. Das ist DevOps."

---

## Slide 3: Kernkonzepte

**CI/CD:**

- **Continuous Integration**: Code wird ständig zusammengeführt und getestet
    - Jeder Push triggert automatisch Tests
    - Fehler werden sofort erkannt (nicht erst nach Wochen)
- **Continuous Deployment**: Automatisches Deployment nach erfolgreichen Tests
    - Kein manuelles "Freitag um 23 Uhr deployen"

**Infrastructure as Code (IaC):**

- Server-Konfiguration in Code (z.B. Terraform, Ansible)
- Versionierbar, wiederholbar, dokumentiert
- Beispiel: "Server aufsetzen" = `terraform apply` statt 50 manuelle Schritte

**Monitoring & Feedback:**

- **Prometheus**: Sammelt Metriken (CPU, RAM, Response-Times)
- **Grafana**: Visualisiert die Daten in Dashboards
- Wichtig: Proaktiv Probleme erkennen, nicht reaktiv fixen

**Shared Ownership:**

- Kein "Das ist ein Ops-Problem"
- Alle sind für das Produkt verantwortlich
- On-Call-Rotationen gemeinsam

**Kleine, häufige Releases:**

- Statt 1x pro Jahr ein Mega-Update
- Lieber täglich kleine Änderungen
- Weniger Risiko, schnelleres Feedback

---

## Slide 4: Vor- und Nachteile (Vergleich)

**Wasserfall:**

- "Old School" - linearer Prozess
- Sehr viel Planung vorweg
- Wenig flexibel, langsam
- Abteilungen arbeiten getrennt
- Beispiel: Traditionelle Banken, Behörden

**Agile:**

- Fokus auf flexible Entwicklung
- Schnelle Sprints, viel Kundenfeedback
- Aber: Deployment bleibt oft manuell/langsam
- Beispiel: Scrum-Teams ohne Automatisierung

**DevOps:**

- Maximale Geschwindigkeit UND Stabilität
- Vollständige Automatisierung (Build, Test, Deploy)
- Gesamtorganisation muss mitmachen (nicht nur Dev-Team)
- Produkt + Betrieb + Automatisierung als Einheit
- Beispiel: Netflix, Spotify, Amazon

**Wichtiger Punkt für Vortrag:** "DevOps ist die Weiterentwicklung von Agile - Agile hat die Entwicklung beschleunigt, DevOps beschleunigt den kompletten Lifecycle bis in Production."

---

## Zusätzliche Talking Points:

**Häufige Missverständnisse:**

- ❌ "DevOps = DevOps Engineer einstellen" → Nein, ist eine Kultur
- ❌ "DevOps = nur Tools" → Tools sind Mittel zum Zweck
- ❌ "DevOps ersetzt Ops" → Nein, alle werden zu DevOps

**Konkrete Tools erwähnen:**

- **CI/CD**: Jenkins, GitLab CI, GitHub Actions
- **Container**: Docker, Kubernetes
- **IaC**: Terraform, Ansible
- **Monitoring**: Prometheus, Grafana, ELK-Stack

**Erfolgsgeschichte:** "Amazon konnte durch DevOps von einem Deployment alle 11,6 Stunden auf ein Deployment alle 11,6 **Sekunden** skalieren."

Viel Erfolg bei der Präsi


# DevOps Präsentation - Spickzettel

## FOLIE 1: Das Problem - Warum DevOps?

**Traditionelles Silo-Problem:**

- Dev & Ops = getrennte Teams, getrennte Ziele
- Dev: Will schnelle neue Features
- Ops: Will stabile Systeme, keine Änderungen
- Führt zu Konflikten

**Konkrete Probleme:**

- "Works on my machine" - läuft lokal, crasht in Production
- Lange Release-Zyklen (Monate/Jahre)
- Manuelle Deployments → fehleranfällig
- Deployments nachts/am Wochenende = Stress

**Geschichte:**

- Begriff 2008-2009 entstanden
- Patrick Debois (belgischer IT-Consultant)
- Erste DevOpsDays Konferenz 2009 in Gent
- Flickr-Talk 2008: "10+ Deploys per Day"

---

## FOLIE 2: Was ist DevOps?

**Kernpunkte:**

- NICHT nur Tools! = Kultur + Methoden + Tools
- Mindset-Change: Zusammenarbeit statt Blame-Game

**Drei Säulen:**

1. Kultur (Zusammenarbeit)
2. Methoden (Agile, Automatisierung)
3. Tools (Jenkins, Docker, Kubernetes)

**Ziel:**

- Schneller von Code → Production
- Amazon: Deployment alle 11,6 Sekunden!
- Netflix: Tausende Deployments täglich

**"You build it, you run it":**

- Dev schreibt Code UND ist für Betrieb verantwortlich
- Erhöht Qualität (weil Dev nachts nicht raus will)

**Development + Operations vereint:**

- Gemeinsame Verantwortung
- Lifecycle-Automatisierung
- Gemeinsame Ziele

---

## FOLIE 3: Kernkonzepte

**CI/CD:**

- Continuous Integration: Code ständig testen
- Continuous Deployment: Automatisch deployen
- Keine manuellen "Freitag 23 Uhr" Deployments mehr

**Infrastructure as Code (IaC):**

- Server-Config in Code (Terraform, Ansible)
- Versionierbar, wiederholbar
- `terraform apply` statt 50 manuelle Schritte

**Monitoring & Feedback:**

- Prometheus: Metriken sammeln
- Grafana: Visualisierung
- Proaktiv Probleme erkennen

**Collaboration: Shared Ownership:**

- Alle verantwortlich für Produkt
- Kein "Das ist Ops-Problem" mehr
- On-Call gemeinsam

**Iterativ: Kleine, häufige Releases:**

- Täglich statt jährlich
- Weniger Risiko, schnelleres Feedback
- Amazon-Beispiel: alle 11,6 Sekunden

---

## FOLIE 4: Vor- und Nachteile

**WASSERFALL:**

- ❌ Linear, unflexibel
- ❌ Sehr langsam (Jahre!)
- ❌ Planung & Dokumentation-lastig
- ❌ Abteilungen getrennt
- ❌ Testen erst am Ende
- ✅ Gut für Hardware, Brückenbau
- Beispiel: FBI Virtual Case File (170M$, 5 Jahre, gescheitert)

**AGILE:**

- ✅ Flexibel, schnelle Sprints
- ✅ Viel Kundenfeedback
- ⚠️ ABER: Deployment oft noch manuell/langsam
- ⚠️ Tests teilweise (nicht alles automatisiert)
- ✅ Team-orientiert
- Beispiel: Scrum-Teams ohne CI/CD

**DEVOPS:**

- ✅ Maximale Geschwindigkeit UND Stabilität
- ✅ Vollständige Automatisierung (Build, Test, Deploy)
- ✅ Gesamtorganisation beteiligt
- ✅ Produkt + Betrieb + Automatisierung als Einheit
- ⚠️ Erfordert Kultur-Wandel im ganzen Unternehmen
- Beispiel: Netflix, Spotify, Amazon

**Key-Message:** "DevOps = Agile für den kompletten Lifecycle, nicht nur Development"

---

## BONUS-WISSEN (falls gefragt wird):

**Zero-Downtime Deployment:**

- Blue-Green: 2 Umgebungen, instant Switch
- Rolling: Server nacheinander updaten
- Canary: 1% → 5% → 100% schrittweise
- Feature Flags: Deploy ≠ Aktivieren
- Load Balancer + Health Checks machen's möglich

**Dev vs Ops erklärt:**

- Dev: Schreibt Code, will Innovation
- Ops: Betreibt Server, will Stabilität
- Konflikt: "Works on my machine" vs. "Production brennt"

**Warum "Silo"?:**

- Getreidesilo = abgeschlossener Turm
- Jedes Team in eigenem Silo
- Keine Kommunikation zwischen Silos
- DevOps bricht Silos auf

**Wichtige Zahlen:**

- High-Performer deployen 200x häufiger
- 24x schnellere Recovery
- 3x niedrigere Fehlerrate

---

## SCHLUSSSATZ:

"DevOps ist keine Job-Bezeichnung, sondern eine kulturelle Bewegung, die Dev und Ops zusammenbringt für schnellere, stabilere Software-Releases."


8+13+15+18+21+26+33+32+35+37+5+(7+10+10+15+18+6+9+14+15+17+22+27)
25 Buchsen
Layer3 Switch 2

# Bedarfsanalyse passive Netzwerkkomponenten

## ZeroTake Coffee UG - 1. Obergeschoss

**Projektbezeichnung:** Netzwerkinfrastruktur 1. OG  
**Standort:** Ottenser Allee 42, 20335 Hamburg  
**Bearbeiter:** Mitch  
**Datum:** 09.12.2025

---

## 1. Anforderungsanalyse

### 1.1 Räumliche Gegebenheiten

- **Etage:** 1. Obergeschoss (Räume R1.1 bis R1.6)
- **Serverraum:** R1.6 (EV) mit vorhandenem 19" Rack
- **Verbindung zum EG:** Cat. 7 F/STP Kabel vom Serverraum R0.5 (EG) bereits verlegt

### 1.2 Anschlussbedarfe

- **Anzahl Netzwerkdosen:** 25 Stück (laut Planung)
- **Anschlüsse pro Dose:** 2x RJ45 (Doppeldosen)
- **Gesamt Ports:** 50 Ports
- **Kabelverlegung:** In vorhandenen Brüstungskanälen
- **Geschwindigkeit:** Gigabit Ethernet (1000 Mbit/s)

### 1.3 Technische Anforderungen

- **Standard:** ISO/IEC 11801, EN 50173
- **Kategorie:** Cat. 6 (Klasse E) - ausreichend für Gigabit Ethernet
- **Übertragungsfrequenz:** 250 MHz
- **Leistungskategorie:** Klasse E (cat. 6) gemäß aktuellem EG-Patchpanel

---

## 2. Mengenermittlung

### 2.1 Verkabelung (Installationskabel)

**Kalkulation:**

- Durchschnittliche Kabellänge pro Port: ca. 20m (geschätzt aus Raumplan)
- Anzahl Ports: 50
- Reserve/Verschnitt: 15%
- **Bedarf:** 50 × 20m × 1,15 = 1.150m

**Beschaffung:**

- 11x 100m Rollen oder
- 2x 500m Trommel + 2x 100m Rolle
- **Gewählt:** 2x 500m Trommel (für einheitliche Charge)

### 2.2 Unterputzdosen RJ45

**Bedarf:** 25 Doppeldosen (2x RJ45 pro Dose)

- Montage in Brüstungskanälen (Aufputz)
- LSA-Anschlußtechnik
- Cat. 6 zertifiziert

### 2.3 Patchpanel

**Bedarf:**

- 50 Ports für 1. OG
- Montage im 19" Rack in R1.6
- **Lösung:** 2x 24-Port Patchpanel (48 Ports + 2 Reserve)

### 2.4 Patchkabel Switch/Patchpanel

**Bedarf:**

- 50 Patchkabel für Verbindung Patchpanel → Switch
- Länge: 0,5m (für 19" Rack)
- Cat. 6 S/FTP
- **Beschaffung:** 50 Stück

---

## 3. Produktauswahl und Preisrecherche

Alle Preise recherchiert auf www.alternate.de (Stand: 09.12.2025)

| Pos. | Komponente                 | Produkt                                                  | Artikelnr. | Menge | Einzelpreis (netto) | Gesamtpreis (netto) | Link                                                                                                   |
| ---- | -------------------------- | -------------------------------------------------------- | ---------- | ----- | ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------ |
| 1    | Verlegekabel Cat.6 U/UTP   | goobay Netzwerkkabel Cat.6, U/UTP, weiß, 100m            | 100068409  | 5     | 29,41€              | 147,05€             | [Link](https://www.alternate.de/goobay/Netzwerkkabel-Cat-6-U-UTP/html/product/100068409)               |
| 2    | Doppeldose 2x RJ45 Aufputz | Digitus Datenanschlussdose CAT.6, Aufputz, weiß, 2x RJ45 | 144957     | 25    | 6,71€               | 167,75€             | [Link](https://www.alternate.de/Digitus/Datenanschlussdose-CAT-6-Klasse-E-Aufputz/html/product/144957) |
| 3    | 24-Port Patchpanel Cat.6   | DeLOCK 19" Patchpanel 24 Port Cat.6, grau, 1 HE          | 1668184    | 2     | 78,07€              | 156,14€             | [Link](https://www.alternate.de/DeLOCK/19-Zoll-Patchpanel-24-Port-Cat-6/html/product/1668184)          |
| 4    | Patchkabel 0,5m Cat.6      | Sharkoon Patchkabel Cat.6 S/FTP, grün, 0,25m             | 1100891    | 50    | 1,76€               | 88,00€              | [Link](https://www.alternate.de/Sharkoon/Patchkabel-RJ45-Cat-6-S-FTP/html/product/1100891)             |

### Kostenübersicht

|Position|Netto|MwSt (19%)|Brutto|
|---|---|---|---|
|**Gesamt Komponenten**|**558,94€**|**106,20€**|**665,14€**|

**Budgetrahmen:** 1.750,00€  
**Verbleibend für aktive Komponenten:** 1.084,86€

---

## 4. Leistungsmerkmale der gewählten Komponenten

### 4.1 Verlegekabel goobay Cat.6 U/UTP

- **Typ:** Installationskabel, starr (Solid Core AWG 23/1)
- **Abschirmung:** U/UTP (ungeschirmt)
- **Bandbreite:** 250 MHz
- **Geschwindigkeit:** bis 1000 Mbit/s (Gigabit Ethernet)
- **Material:** CCA (kupferkaschiertes Aluminium)
- **Mantel:** PVC, Eca-Brandschutzklasse
- **Maximale Länge:** 50m (laut Spezifikation)
- **Normen:** ISO/IEC 11801, EN 50173

**Begründung:** Kostengünstige Lösung, ausreichend für die Anforderungen im Büroumfeld. CCA-Leiter sind für SOHO-Anwendungen geeignet, echte Kupferleiter wären teurer aber bieten hier keinen Mehrwert.

### 4.2 Digitus Doppeldose Cat.6

- **Typ:** Aufputzdose mit Metallgehäuse
- **Anschlüsse:** 2x RJ-45 Buchsen (8P8C)
- **Montage:** LSA-Leisten, farbcodiert EIA/TIA 568 A & B
- **Schirmung:** Vollschirmung durch Metallgehäuse
- **Zugentlastung:** Integriert
- **Abmessungen:** 80x80mm Rahmen, 50x50mm Zentralplatte

**Begründung:** Hochwertige Qualität von Digitus, passend für Aufputzmontage in Brüstungskanälen. Vollschirmung schützt vor Störungen.

### 4.3 DeLOCK 19" Patchpanel Cat.6

- **Typ:** 19" Rackmount, 1 HE
- **Ports:** 24x RJ-45
- **Montage:** LSA-Leisten
- **Material:** Metall
- **Farbe:** Grau (passend zu Standard-Racks)

**Begründung:** Etablierter Hersteller, gutes Preis-Leistungs-Verhältnis. 2x 24-Port deckt alle 50 Ports ab mit kleiner Reserve.

### 4.4 Sharkoon Patchkabel Cat.6 S/FTP 0,25m

- **Typ:** Flexible Patchkabel mit Knickschutz
- **Abschirmung:** S/FTP (doppelt geschirmt)
- **Länge:** 0,25m (optimal für Rackmontage)
- **Stecker:** Vergoldete Kontakte
- **Farbe:** Grün (farbliche Kodierung möglich)

**Begründung:** Kurze Patchkabel für saubere Verkabelung im Rack. S/FTP-Schirmung minimiert Störungen, besonders wichtig bei vielen parallel geführten Kabeln im Rack.

---

## 5. Energieeffizienz-Betrachtung

Die passive Verkabelung selbst verbraucht keine Energie. Energieeinsparungen ergeben sich durch:

1. **Kupferkaschierte Aluminiumleiter (CCA):** Geringfügig höherer Widerstand als Vollkupfer, aber bei den kurzen Distanzen (<50m) vernachlässigbar
2. **Effiziente Leitungsführung:** Kurze Patchkabel im Rack minimieren Signal-Dämpfung
3. **Qualität der Verbindungen:** LSA-Anschlußtechnik bietet stabile, wartungsarme Verbindungen

**Hinweis für aktive Komponenten:** Bei der Switch-Auswahl sollte auf Energy Efficient Ethernet (IEEE 802.3az) geachtet werden.

---

## 6. Dokumentation und Normen

Die Installation erfolgt nach folgenden Standards:

- **ISO/IEC 11801:** Internationale Norm für Gebäudeverkabelung
- **EN 50173:** Europäische Norm für strukturierte Verkabelung
- **EIA/TIA 568 A/B:** Farbcodierung und Pinbelegung
- **EN 50575 (CPR):** Brandschutzklasse Eca für Kabel

---

## 7. Installationshinweise

### 7.1 Verkabelung

1. Kabel nicht über Mindestradiusbiegen (8× Kabeldurchmesser)
2. Maximale Zugkraft 150N während Installation
3. Verdrillte Paare dürfen max. 13mm aufgedreht werden
4. LSA-Anschlußtechnik: Farbcodierung beachten (568B-Standard)

### 7.2 Patchpanel-Belegung

- **Port 1-24:** Raum R1.1 - R1.5 (nach Plan)
- **Port 25-48:** Fortsetzung + Serverraum R1.6
- **Port 49-50:** Reserve

### 7.3 Kennzeichnung

Alle Ports sollten beschriftet werden nach Schema:

- Format: `[Raum]-[Dose]-[Port]`
- Beispiel: `R1.3-D02-P1`

---

## Zusammenfassung

Mit der vorgeschlagenen Komponentenauswahl kann die Netzwerkinfrastruktur im 1. OG professionell und kostengünstig ausgebaut werden. Die Gesamtkosten für passive Komponenten von **665,14€ brutto** liegen deutlich unter dem Budget und lassen genügend Spielraum für qualitativ hochwertige aktive Komponenten (Switch, Access Points).

Die gewählten Komponenten erfüllen alle normativen Anforderungen und bieten eine zukunftssichere Gigabit-Ethernet-Infrastruktur für die Angestellten der ZeroTake Coffee Rösterei.