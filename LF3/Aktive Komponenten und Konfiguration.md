---
fach: LF3
thema: Aktive Komponenten und Netzwerkkonfiguration
tags: [lf3, switch, router, accesspoint, ipv4, cisco]
datum: 2026-04-20
typ: notiz
---

# Aktive Komponenten und Konfiguration

## Aktive Netzwerkkomponenten

### Switch

Leitet Datenpakete innerhalb eines Netzwerks (Layer 2) anhand der **MAC-Adresse** weiter.

| Eigenschaft      | Beschreibung                                |
| ---------------- | ------------------------------------------- |
| **OSI-Schicht**  | 2 (Sicherungsschicht), manche L3            |
| **Adressierung** | MAC-Adressen                                |
| **Funktion**     | Frames an den richtigen Port weiterleiten   |
| **Lernfähig**    | Ja (MAC-Adresstabelle)                      |
| **Broadcast**    | Innerhalb des VLANs                         |

**Auswahlkriterien:**
- Anzahl Ports (8, 16, 24, 48)
- Geschwindigkeit (Fast Ethernet, Gigabit, 10G)
- PoE-Fähigkeit (Power over Ethernet)
- Managed vs. Unmanaged
- Stackable

### Access Point (AP)

Erweitert das kabelgebundene Netzwerk um WLAN.

| Eigenschaft      | Beschreibung                                |
| ---------------- | ------------------------------------------- |
| **Funktion**     | Bridge zwischen LAN und WLAN                |
| **Anbindung**    | Per Ethernet-Kabel (oft PoE)                |
| **Reichweite**   | 30-100 m (je nach Umgebung)                 |
| **Standards**    | Wi-Fi 5/6/6E                                |

**Auswahlkriterien:**
- Unterstützte Wi-Fi-Standards
- Gleichzeitige Nutzeranzahl
- Dual-Band / Tri-Band
- Indoor vs. Outdoor
- PoE-Unterstützung

### Router

Verbindet verschiedene Netzwerke miteinander und leitet Pakete anhand der **IP-Adresse** weiter (Layer 3).

| Eigenschaft      | Beschreibung                                |
| ---------------- | ------------------------------------------- |
| **OSI-Schicht**  | 3 (Vermittlungsschicht)                     |
| **Adressierung** | IP-Adressen                                 |
| **Funktion**     | Routing zwischen Netzwerken                 |
| **NAT**          | Übersetzung private ↔ öffentliche Adressen  |
| **Firewall**     | Oft integriert                              |

---

## IPv4-Adressierung

### Aufbau einer IPv4-Adresse

```
192.168.1.100 / 24
 ↑              ↑
IP-Adresse    Subnetzmaske (CIDR-Notation)
```

4 Oktette à 8 Bit = 32 Bit gesamt

### Adressklassen (veraltet, aber Prüfungsrelevant)

| Klasse | Bereich               | Netzanteil | Hosts/Netz    |
| ------ | --------------------- | ---------- | ------------- |
| **A**  | 1.0.0.0 - 126.x.x.x  | /8         | 16.777.214    |
| **B**  | 128.0.0.0 - 191.x.x.x | /16       | 65.534        |
| **C**  | 192.0.0.0 - 223.x.x.x | /24       | 254           |

### Private IP-Adressen (RFC 1918)

| Klasse | Bereich                       | CIDR  |
| ------ | ----------------------------- | ----- |
| A      | 10.0.0.0 - 10.255.255.255    | /8    |
| B      | 172.16.0.0 - 172.31.255.255  | /12   |
| C      | 192.168.0.0 - 192.168.255.255 | /16  |

> [!info] Private Adressen sind **nicht** im Internet routbar. Für den Internetzugang wird **NAT** (Network Address Translation) verwendet.

### Besondere Adressen

| Adresse          | Bedeutung                    |
| ---------------- | ---------------------------- |
| 0.0.0.0          | Unbekannter Host             |
| 127.0.0.1        | Localhost (Loopback)         |
| 255.255.255.255  | Broadcast (alle im Netzwerk) |
| x.x.x.0          | Netzwerkadresse              |
| x.x.x.255        | Broadcast-Adresse (/24)      |

### Subnetzmaske und CIDR

Die Subnetzmaske trennt den Netzanteil vom Hostanteil:

```
IP:     192.168.1.100
Maske:  255.255.255.0    = /24
        ───────────┬──
        Netz: 192.168.1  Host: .100
```

| CIDR | Subnetzmaske        | Hosts  |
| ---- | ------------------- | ------ |
| /24  | 255.255.255.0       | 254    |
| /25  | 255.255.255.128     | 126    |
| /26  | 255.255.255.192     | 62     |
| /27  | 255.255.255.224     | 30     |
| /28  | 255.255.255.240     | 14     |

**Formel:** Hosts = 2^(32 - Präfix) - 2

### Default Gateway

Das Standard-Gateway ist die IP-Adresse des Routers - der Weg ins Internet oder andere Netzwerke.

```
PC (192.168.1.100) → Switch → Router (192.168.1.1) → Internet
                               ↑
                        Default Gateway
```

---

## Wichtige CLI-Befehle

| Befehl (Windows)     | Befehl (Linux)     | Funktion                          |
| -------------------- | ------------------ | --------------------------------- |
| `ipconfig`           | `ifconfig` / `ip a` | Netzwerkkonfiguration anzeigen   |
| `ipconfig /all`      | `ip addr show`     | Detaillierte Konfiguration        |
| `ping 192.168.1.1`   | `ping 192.168.1.1` | Erreichbarkeit prüfen            |
| `tracert`            | `traceroute`       | Route zum Ziel anzeigen           |
| `nslookup`           | `dig` / `nslookup` | DNS-Abfrage                      |
| `arp -a`             | `arp -a`           | ARP-Tabelle anzeigen             |

---

## Cisco Packet Tracer

Simulationssoftware für Netzwerke. Damit werden Netzwerke geplant, gebaut und getestet.

**Wichtige Funktionen:**
- Geräte platzieren und verbinden
- IP-Adressen konfigurieren
- Ping und Konnektivitätstests durchführen
- Simulationsmodus: Pakete verfolgen

### IPv4-Header

| Feld              | Größe    | Beschreibung                        |
| ------------------ | -------- | ----------------------------------- |
| Version            | 4 Bit    | IPv4 = 4                           |
| Header Length      | 4 Bit    | Headerlänge in 32-Bit-Wörtern      |
| TTL                | 8 Bit    | Time to Live (Hop-Limit)           |
| Protocol           | 8 Bit    | TCP=6, UDP=17, ICMP=1              |
| Source Address      | 32 Bit   | Absender-IP                        |
| Destination Address | 32 Bit  | Empfänger-IP                       |

---

## Aufgaben

> [!example] Aufgabe 1 - Aktive Komponenten
> 1. Erkläre die Funktion eines Switches (Paketweiterleitung)
> 2. Erkläre die Funktion eines Access Points
> 3. Erkläre die Funktion eines Routers
> 4. Ordne die Geräte den OSI-Schichten zu

> [!example] Aufgabe 2 - Bedarfsanalyse aktive Komponenten
> Wähle aus dem Lieferantenkatalog passende Switches und Access Points für die ZeroTake Coffee UG.
> Dokumentiere: Modell, Leistungsmerkmale, Preise.

> [!example] Aufgabe 3 - IPv4 (S. 306/307)
> 1. Netzwerktopologien studieren
> 2. IPv4-Grundlagen: Private/öffentliche Adressen, CIDR, Subnetting
> 3. Default Gateway erklären
> 4. CLI-Befehle testen: `ipconfig`, `ping`, Broadcast

> [!example] Aufgabe 4 - Cisco Packet Tracer
> 1. Cisco PT Training durcharbeiten
> 2. Übungsaufgabe lösen
> 3. ZeroTake-Netzwerk in PT konfigurieren (Excel-Planung → PT-Umsetzung)

> [!example] Aufgabe 5 - IPv4-Header
> Analysiere im PT-Simulationsmodus den IPv4-Header eines Pakets. Recherchiere die Felder.

> [!example] Aufgabe 6 - OSI-Modell erweitern
> Erweitere deine OSI-Übersicht um: Topologien, IPv4-Adressierung, Header-Struktur, Konnektivitätstests

---

## Materialien

- ![[files/LE4_06_JIKU_Switch_Auswahl.pdf]]
- ![[files/LE4_08_JIKU_AccessPoint_Auswahl.pdf]]
- ![[files/Schulung-Cisco Packet Tracer.pdf]]
- ![[files/Übungsaufgabe Cisco PT.pdf]]
- ![[files/LE5_08_IPv4_Header.docx]]

---

## Siehe auch

- [[Netzwerk-Grundlagen und OSI]]
- [[Physische Netzwerkinfrastruktur]]
