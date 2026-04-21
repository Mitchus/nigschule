---
fach: LF3
thema: LE 6 - Netzwerkkonfiguration & Packet Tracer
tags: [lf3, moodle, ipv4, cisco, topologien]
datum: 2026-04-20
typ: notiz
quelle: moodle-browser
---

# LE 6 - Netzwerkkonfiguration & Cisco Packet Tracer

## Handlungssituation

Mail von Nairobi: Bedarfsanalyse wurde vom Kunden angenommen. Umbauten abgeschlossen - Netzwerk kann jetzt eingerichtet/erweitert werden. Bogota steht bei Fragen zur Verfügung (Helsinki im Urlaub).

**Materialien:**
- Lastenheftauszug Kap. 5 - ZeroTake Coffee
- Netzwerkkonfiguration (.xlsx)
- PT-Datei: Netzwerk der ZeroTake

---

## A1.1 - Projektanforderungen erarbeiten

**Anforderungen an das Netzwerk:**
- OG mit EG verbinden und Verkauf zuordnen
- Private und öffentliche Netzwerkadressen verwenden
- Aktuelle Verschlüsselung mit vorgegebener SSID und Passwort
- Einhaltung und Erweiterung des Netzwerkplans
- 10 Arbeitsplätze (7 Desktop, 3 Laptops) + 2 Drucker einrichten
- Client-Funktionalität testen

---

## A2.1 - Logische Netzwerkpläne (Topologien)

**Aufgabe:** Recherche (Internet + Gratzke S. 306/307) zur zugeteilten Topologie:
- Kurze Beschreibung
- Einfache Abbildung
- Vor- und Nachteile

---

## A2.2 - IPv4-Adressierung

**Aufgaben:**

1. Drei Adressierungsverfahren nennen und unterscheiden (Unicast, Broadcast, Multicast)

2. IP-Adresse beschriften:
   ```
   172.10.77.2 / 16
   ├── Netzanteil ──┤├ Hostanteil ┤
   Subnetzmaske: 255.255.0.0
   ```

3. Netzanteil vs. Hostanteil erklären

4. Hosts für verschiedene Netzbereiche berechnen:

   | Nr. | Netzbereich | Hosts | Ausreichend für 55 Hosts? |
   |---|---|---|---|
   | 1 | 192.168.0.0/27 | 30 | Nein |
   | 2 | 192.168.0.0/24 | 254 | Ja |
   | 3 | 192.168.0.0/30 | 2 | Nein |
   | 4 | 192.168.0.0/23 | 510 | Ja |

5. Default Gateway beschreiben (Router-IP, Weg ins Internet)

6. Private vs. öffentliche IP-Adressen unterscheiden (RFC 1918, NAT)

7. CLI-Befehl für Netzwerkkonfiguration: `ipconfig` / `ip a`

8. CLI-Befehl für Erreichbarkeit: `ping`

9. Broadcast an alle Hosts in 192.168.0.0/24: `ping 192.168.0.255`

---

## A3 - Cisco Packet Tracer Schulung

1. Foliensatz Einführung PT durcharbeiten
2. Übungsaufgabe lösen
3. Quiz: Neue Kenntnisse überprüfen

---

## A4.1 - Netzwerkerweiterung ZeroTake planen und umsetzen

**Aufgaben:**
1. Konfiguration in der Excel-Datei planen
2. Funktionen notieren, die das Netzwerk nach Umsetzung erfüllen muss
3. Planungen in Packet Tracer übertragen und Hosts konfigurieren

> [!tip] Wi-Fi-Konfiguration im PT: Video ab Min. 18:30

**Abgabe:** PT-Datei + Netzwerkdokumentation

---

## A5.1 - IPv4-Header im Detail

**Aufgaben:**
1. ICMP-Paket im PT-Simulationsmodus öffnen → "Outbound PDU Details" → IPv4-Header ansehen
2. Aufbau des IPv4-Headers recherchieren und mit PT-Werten vergleichen
3. Ergebnisse notieren (Vorlage verfügbar)

---

## OSI-Modell erweitern (15 Min.)

**Gruppenarbeit** - Zusammenfassung (max. 4 Sätze) zu:
- Logische Netzwerkpläne (Topologien)
- IPv4-Adresse: Eigenschaften & Aufbau
- IPv4-Header
- Konnektivität testen

---

## Checkliste LE 3.6

- [ ] Projektanforderungen aus Lastenheft erarbeitet
- [ ] Topologien (Stern, Ring, Bus, Mesh, Baum) unterscheidbar
- [ ] IPv4-Adressierung verstanden (CIDR, Subnetting, private/öffentliche)
- [ ] Default Gateway erklärbar
- [ ] Cisco Packet Tracer Schulung abgeschlossen
- [ ] ZeroTake-Netzwerk in PT konfiguriert und getestet
- [ ] IPv4-Header-Felder bekannt
