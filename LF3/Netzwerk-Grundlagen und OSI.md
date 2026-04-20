---
fach: LF3
thema: Netzwerk-Grundlagen und OSI-Modell
tags: [lf3, netzwerk, osi, grundlagen]
datum: 2026-04-20
typ: notiz
---

# Netzwerk-Grundlagen und OSI-Modell

## Handlungssituation

> Projekt: Netzwerkerweiterung der **ZeroTake Coffee UG** in Hamburg. Zusammenarbeit mit Kollege Helsinki bei der JIKU IT-Solutions GmbH. Aufgabe: Planung und Umsetzung der Netzwerkinfrastruktur für eine neue Etage.

**Literatur:** Gratzke (2025) - IT-Berufe Grundstufe LF 1-5, Westermann
**Software:** Cisco Packet Tracer (kostenlos)

---

## Netzwerk-Grundbegriffe

### Was ist ein Netzwerk?

Ein Netzwerk verbindet mehrere Geräte zum Austausch von Daten und Ressourcen.

**Vorteile:**
- Gemeinsame Ressourcennutzung (Drucker, Speicher, Internet)
- Kommunikation und Zusammenarbeit
- Zentrale Datenverwaltung und -sicherung
- Kosteneinsparung

### Netzwerkreichweiten

| Bezeichnung | Reichweite            | Beispiel                     |
| ----------- | --------------------- | ---------------------------- |
| **PAN**     | Persönlich (< 10 m)   | Bluetooth-Kopfhörer          |
| **LAN**     | Lokal (< 1 km)        | Büronetzwerk, Schule         |
| **MAN**     | Stadtweit (< 100 km)  | Stadtweites Glasfasernetz    |
| **WAN**     | Weltweit               | Internet                     |

### Client-Server vs. Peer-to-Peer

| Eigenschaft    | Client-Server              | Peer-to-Peer              |
| -------------- | -------------------------- | ------------------------- |
| **Struktur**   | Zentraler Server           | Gleichberechtigte Geräte  |
| **Verwaltung** | Zentral                    | Dezentral                 |
| **Sicherheit** | Hoch (zentrale Kontrolle)  | Gering                    |
| **Kosten**     | Höher (Serverhardware)     | Niedrig                   |
| **Beispiel**   | Firmen-LAN, Webserver      | Dateitausch, Heimnetzwerk |

### Netzwerktopologien

| Topologie    | Beschreibung                             | Vor-/Nachteile              |
| ------------ | ---------------------------------------- | --------------------------- |
| **Stern**    | Alle Geräte an zentralem Switch/Hub      | Einfach, Ausfall eines Geräts unkritisch; Switch = Single Point of Failure |
| **Ring**     | Geräte in geschlossener Kette            | Deterministisch; Ausfall stoppt alles |
| **Bus**      | Alle Geräte an einem Kabel               | Günstig; Kollisionen, schwer erweiterbar |
| **Mesh**     | Jeder mit jedem verbunden                | Ausfallsicher; teuer und komplex |
| **Baum**     | Hierarchisch (Stern-Kombination)         | Skalierbar; Root-Ausfall kritisch |

---

## OSI-Referenzmodell

Das **Open Systems Interconnection**-Modell beschreibt die Kommunikation in 7 Schichten:

| Schicht | Name            | Funktion                          | Protokolle/Geräte            |
| ------- | --------------- | --------------------------------- | ---------------------------- |
| **7**   | Anwendung       | Schnittstelle zum Benutzer        | HTTP, FTP, SMTP, DNS         |
| **6**   | Darstellung     | Datenformate, Verschlüsselung    | SSL/TLS, JPEG, ASCII         |
| **5**   | Sitzung         | Verbindungsaufbau/-steuerung      | NetBIOS, RPC                 |
| **4**   | Transport       | Ende-zu-Ende-Kommunikation        | TCP, UDP                     |
| **3**   | Vermittlung     | Routing, logische Adressierung    | IP, ICMP, Router             |
| **2**   | Sicherung       | Fehlererkennung, MAC-Adressen     | Ethernet, WLAN, Switch       |
| **1**   | Bitübertragung  | Physikalische Übertragung         | Kabel, Funk, Hub, Repeater   |

> [!tip] Merksatz (von oben nach unten):
> **A**lle **D**eutschen **S**tudenten **T**rinken **V**erschiedene **S**orten **B**ier

### OSI vs. DoD/TCP-IP-Modell

| OSI-Schicht       | TCP/IP-Schicht     |
| ------------------ | ------------------ |
| 7 Anwendung        | Anwendung          |
| 6 Darstellung      | Anwendung          |
| 5 Sitzung          | Anwendung          |
| 4 Transport        | Transport          |
| 3 Vermittlung      | Internet           |
| 2 Sicherung        | Netzzugang         |
| 1 Bitübertragung   | Netzzugang         |

### Datenkapselung

Beim Senden werden auf jeder Schicht Header (und ggf. Trailer) hinzugefügt:

```
Daten
→ [TCP-Header | Daten]                    = Segment
→ [IP-Header | TCP-Header | Daten]        = Paket
→ [Eth-Header | IP | TCP | Daten | FCS]   = Frame
→ Bits auf dem Kabel                       = Signal
```

---

## Anforderungsanalyse (ZeroTake Coffee)

### Projektziel

Netzwerkerweiterung in die 1. Etage der ZeroTake Coffee UG.

### Funktionale Anforderungen

- Clients anbinden und Zugang zum Netzwerk ermöglichen
- WiFi-Abdeckung auf beiden Etagen
- Verkabelung nach Lageplan-Markierungen
- Ausreichende Übertragungsgeschwindigkeit

### Nicht-funktionale Anforderungen

- Energieeffizienz beachten
- Vorschriften und Normen einhalten
- Vorhandene Kabelkanäle nutzen
- Netzwerk-Rack im Serverraum verwenden
- Budget: max. **1.750 €**

### Konfigurationsanforderungen

- 10 Arbeitsplätze (7 Desktop, 3 Laptops)
- 2 Netzwerkdrucker
- Private und öffentliche Netzwerkadressen
- Aktuelle WLAN-Verschlüsselung mit SSID/Passwort

---

## Aufgaben

> [!example] Aufgabe 1 - Netzwerke im Alltag (15 Min.)
> Identifiziere Netzwerke in deinem Alltag. Welche Funktionen erfüllen sie?

> [!success] Lösung
> | Netzwerk | Typ | Funktion |
> | -------- | --- | -------- |
> | **Heimnetzwerk (Router/WLAN)** | LAN | Verbindet Smartphones, PCs, Smart-TV – gemeinsamer Internetzugang |
> | **Mobilfunknetz (4G/5G)** | WAN | Ermöglicht mobiles Internet und Telefonie über Sendemasten |
> | **Bluetooth-Verbindung (Kopfhörer, Smartwatch)** | PAN | Kurzstrecken-Datenübertragung zwischen persönlichen Geräten |
> | **Schulnetzwerk / Firmennetzwerk** | LAN | Zentrale Ressourcennutzung (Drucker, Server, Internetzugang, Benutzerkonten) |
> | **Internet** | WAN | Weltweites Netz aus Millionen Einzelnetzwerken – Datenaustausch, Kommunikation, Dienste |
> | **Kassensystem im Supermarkt** | LAN/WAN | Vernetzt Kassen mit zentralem Server, Lagerverwaltung und Zahlungsdienstleister |
> | **Smart-Home (Zigbee/Z-Wave)** | PAN | Verbindet Lampen, Thermostate und Sensoren zur automatisierten Haussteuerung |

> [!example] Aufgabe 2 - Teamvorträge (S. 282-296)
> Themen: Netzwerke und Funktionen, Server, Clients, Netzwerkreichweiten, Rechenzentren

> [!success] Lösung
> **Netzwerke und Funktionen:** Ein Netzwerk ist der Zusammenschluss mehrerer Geräte über ein Übertragungsmedium (Kabel oder Funk). Hauptfunktionen: gemeinsame Ressourcennutzung, Kommunikation, zentrale Datenspeicherung und -sicherung. Unterschieden wird nach Übertragungsmedium, Reichweite und Topologie.
>
> **Server:** Ein Server stellt Dienste und Ressourcen für andere Geräte (Clients) bereit. Typen: Dateiserver (Dateifreigabe), Webserver (HTTP), Druckserver, DHCP-Server (IP-Vergabe), DNS-Server (Namensauflösung), Mailserver. Server laufen meist dauerhaft und haben leistungsfähige Hardware (ECC-RAM, RAID).
>
> **Clients:** Ein Client ist ein Endgerät, das Dienste eines Servers in Anspruch nimmt. Beispiele: PC, Laptop, Smartphone. Im Client-Server-Modell initiiert der Client immer die Verbindung; der Server antwortet. Clients haben in der Regel keine zentrale Verwaltungsrolle.
>
> **Netzwerkreichweiten:** Netzwerke werden nach ihrer geografischen Ausdehnung klassifiziert – PAN (persönlich, < 10 m), LAN (lokal, Gebäude/Campus), MAN (städtisch, bis 100 km), WAN (weltweit, z. B. Internet). Die Reichweite bestimmt auch die eingesetzte Technologie und Übertragungsgeschwindigkeit.
>
> **Rechenzentren (Data Centers):** Rechenzentren sind speziell gesicherte Gebäude oder Räume, die Server, Netzwerkkomponenten und Speichersysteme beherbergen. Sie gewährleisten hohe Verfügbarkeit (USV, redundante Kühlung, Brandschutz), physische Sicherheit und schnelle Internetanbindung. Cloud-Dienste (AWS, Azure) basieren auf globalen Rechenzentren.

> [!example] Aufgabe 3 - OSI-Modell (S. 322-326)
> 1. Welchen Zweck erfüllt das OSI-Modell?
> 2. Warum wurde es entwickelt?
> 3. Nenne alle 7 Schichten mit Namen und Aufgaben
> 4. Vergleiche OSI mit dem DoD-Modell (S. 191, Aufgabe 15)

> [!success] Lösung
> **1. Zweck des OSI-Modells:**
> Das OSI-Modell (Open Systems Interconnection) ist ein Referenzmodell, das Netzwerkkommunikation in 7 abstrakte Schichten unterteilt. Es dient als gemeinsame Sprache für Hersteller und Entwickler, um interoperable Netzwerksysteme zu bauen. Es hilft bei der Fehlersuche (Troubleshooting) und beim Verständnis, auf welcher Ebene ein Problem auftritt.
>
> **2. Warum wurde es entwickelt?**
> In den 1970er–80er Jahren existierten viele inkompatible, proprietäre Netzwerkprotokolle verschiedener Hersteller (IBM, DEC etc.). Die ISO (International Organization for Standardization) entwickelte das OSI-Modell 1984, um einen herstellerunabhängigen Standard für Netzwerkkommunikation zu schaffen und die Interoperabilität zwischen verschiedenen Systemen zu ermöglichen.
>
> **3. Die 7 OSI-Schichten:**
> | Schicht | Name | Aufgabe | Protokolle/Geräte |
> | ------- | ---- | -------- | ----------------- |
> | 7 | Anwendung | Schnittstelle zu Benutzerprogrammen | HTTP, FTP, SMTP, DNS |
> | 6 | Darstellung | Datenformatierung, Verschlüsselung, Komprimierung | SSL/TLS, JPEG, ASCII |
> | 5 | Sitzung | Aufbau, Verwaltung und Abbau von Sitzungen | NetBIOS, RPC |
> | 4 | Transport | Zuverlässige Ende-zu-Ende-Übertragung, Segmentierung | TCP, UDP |
> | 3 | Vermittlung | Logische Adressierung, Routing | IP, ICMP, Router |
> | 2 | Sicherung | Fehlererkennung, MAC-Adressierung, Frames | Ethernet, WLAN, Switch |
> | 1 | Bitübertragung | Physikalische Übertragung von Bits | Kabel, Funk, Hub, Repeater |
>
> **4. OSI vs. DoD/TCP-IP-Modell:**
> | OSI (7 Schichten) | DoD/TCP-IP (4 Schichten) | Erläuterung |
> | ----------------- | ------------------------ | ----------- |
> | 7 Anwendung | Anwendung | Alle anwendungsnahen Protokolle zusammengefasst |
> | 6 Darstellung | Anwendung | In TCP/IP nicht separat – in Anwendungsschicht integriert |
> | 5 Sitzung | Anwendung | In TCP/IP nicht separat – in Anwendungsschicht integriert |
> | 4 Transport | Transport | TCP/UDP – identische Funktion |
> | 3 Vermittlung | Internet | IP-Routing – identische Funktion |
> | 2 Sicherung | Netzzugang | Zusammengefasst in einer Schicht |
> | 1 Bitübertragung | Netzzugang | Zusammengefasst in einer Schicht |
>
> Das DoD-Modell ist praxisorientierter und bildet die Grundlage des tatsächlich genutzten Internets. Das OSI-Modell ist konzeptioneller und eignet sich besser für Lehre und Fehleranalyse.

---

## Materialien

- ![[files/00_Einführung_LF3.pdf]]
- ![[files/Gratzke_OSI_Layer.pdf]]
- ![[files/Topologien_uebersicht_IT25B.pdf]]
- ![[files/LE3_02_Tafelbild_Anforderung_neu.pdf]]
- ![[files/LE4_00_Lastenheftauszug_ZeroTake_Coffee_k.pdf]]
- ![[files/LE4_00_ZeroTake_Coffee_Grundriss.pdf]]

---

## Siehe auch

- [[Physische Netzwerkinfrastruktur]]
- [[Aktive Komponenten und Konfiguration]]
