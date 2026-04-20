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

> [!example] Aufgabe 2 - Teamvorträge (S. 282-296)
> Themen: Netzwerke und Funktionen, Server, Clients, Netzwerkreichweiten, Rechenzentren

> [!example] Aufgabe 3 - OSI-Modell (S. 322-326)
> 1. Welchen Zweck erfüllt das OSI-Modell?
> 2. Warum wurde es entwickelt?
> 3. Nenne alle 7 Schichten mit Namen und Aufgaben
> 4. Vergleiche OSI mit dem DoD-Modell (S. 191, Aufgabe 15)

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
