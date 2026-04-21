---
fach: LF3
thema: Netzwerkprotokolle und Standards
tags: [lf3, netzwerk, protokolle, tcp, udp, dns, dhcp, arp, http, ftp, ssh, tls, vlan, routing, ipv6, nat]
datum: 2026-04-21
typ: notiz
---

# Netzwerkprotokolle und Standards

## Protokollübersicht

| Protokoll | Schicht (OSI) | Typ | Aufgabe |
|---|---|---|---|
| **Ethernet** | 1-2 | LAN | Frame-basierte Datenübertragung im lokalen Netz |
| **STP/RSTP** | 2 | Schleifenvermeidung | Verhindert Loops in redundanten Switch-Topologien |
| **VLAN (802.1q)** | 2 | Segmentierung | Logische Trennung von Netzwerken auf einem Switch |
| **ARP** | 2 | Adressauflösung | IP-Adresse → MAC-Adresse |
| **ICMP** | 3 | Steuerung | Fehlermeldungen und Diagnose (Ping) |
| **IP** | 3 | Vermittlung | Logische Adressierung und Routing |
| **TCP** | 4 | Transport | Zuverlässige, verbindungsorientierte Übertragung |
| **UDP** | 4 | Transport | Schnelle, verbindungslose Übertragung |
| **TLS/SSL** | 5-6 | Sicherheit | Verschlüsselung und Authentifizierung |
| **DHCP** | 7 | Anwendung | Automatische IP-Konfiguration |
| **DNS** | 7 | Anwendung | Namensauflösung (Domain → IP) |
| **HTTP/HTTPS** | 7 | Anwendung | Webseiten-Übertragung |
| **FTP** | 7 | Anwendung | Dateiübertragung |
| **SMTP/POP/IMAP** | 7 | Anwendung | E-Mail Versand und Empfang |
| **SSH** | 7 | Anwendung | Verschlüsselter Fernzugriff (ersetzt Telnet) |

---

## Kapselung (Encapsulation)

Beim Senden durchlaufen Daten die Schichten von oben nach unten. Jede Schicht fügt ihren eigenen Header hinzu:

```
Anwendungsschicht:  [Daten]
Transportschicht:   [TCP/UDP-Header][Daten]            → Segment
Vermittlungsschicht:[IP-Header][TCP-Header][Daten]     → Paket
Sicherungsschicht:  [Frame-H][IP-H][TCP-H][Daten][FCS] → Frame
Bitübertragung:      01101001011010...                  → Bits
```

Beim Empfänger wird der Prozess umgekehrt: Jede Schicht entfernt ihren Header (**Dekapselung**).

---

# Schicht 1-2: Netzzugang

## Ethernet-Frame

**Schicht:** 1-2 (Bitübertragung / Sicherung) | **Rahmenformat für LAN-Kommunikation**

```
+----------+-----+----------+----------+--------+--------+-----+
| Präambel | SFD | Ziel-MAC | Quell-MAC|Typ/Len | Daten  | FCS |
|  7 Byte  |1 B  |  6 Byte  |  6 Byte  | 2 Byte |46-1500B|4 B  |
+----------+-----+----------+----------+--------+--------+-----+
```

| Feld | Größe | Beschreibung |
|---|---|---|
| **Präambel** | 7 Byte | Synchronisationsmuster (101010...) |
| **SFD** (Start Frame Delimiter) | 1 Byte | Markiert den Beginn des Frames |
| **Ziel-MAC** | 6 Byte | MAC-Adresse des Empfängers |
| **Quell-MAC** | 6 Byte | MAC-Adresse des Senders |
| **Typ/Länge** | 2 Byte | Ethernet II: Protokolltyp (z.B. `0x0800`=IPv4, `0x0806`=ARP) |
| **Daten** | 46-1500 Byte | Nutzdaten (Payload). Min. 46 Byte (ggf. Padding) |
| **FCS** (Frame Check Sequence) | 4 Byte | CRC-32 Prüfsumme zur Fehlererkennung |

### MAC-Adresse

- 48 Bit (6 Byte), Schreibweise: `AA:BB:CC:DD:EE:FF`
- Erste 3 Byte: **OUI** (Herstellerkennung, z.B. Intel, Realtek)
- Letzte 3 Byte: Gerätekennung (vom Hersteller vergeben)
- `FF:FF:FF:FF:FF:FF` = **Broadcast** (an alle Geräte im LAN)
- Weltweit einzigartig, fest in der Netzwerkkarte gespeichert

### Frame-Größen

- **Minimum:** 64 Byte (ohne Präambel/SFD)
- **Maximum:** 1518 Byte (ohne Präambel/SFD), 1522 Byte mit VLAN-Tag
- **MTU** (Maximum Transmission Unit): 1500 Byte Nutzdaten

---

## ARP (Address Resolution Protocol)

**Schicht:** 2 (Sicherung) | **Adressauflösung IP → MAC**

### Problem

Geräte in einem lokalen Netz kommunizieren über **MAC-Adressen** (Schicht 2). IP-Adressen (Schicht 3) müssen daher in MAC-Adressen aufgelöst werden.

### Funktionsweise

```
1. Host A will an 192.168.1.5 senden, kennt aber die MAC-Adresse nicht
2. Host A sendet ARP-Request als Broadcast (FF:FF:FF:FF:FF:FF):
   "Wer hat die IP 192.168.1.5? Antwort bitte an [meine MAC]"
3. ALLE Geräte im Netz empfangen den Broadcast
4. Nur Host B (192.168.1.5) antwortet mit ARP-Reply:
   "192.168.1.5 bin ich, meine MAC ist AA:BB:CC:DD:EE:FF"
5. Host A speichert das Ergebnis im ARP-Cache
```

### ARP-Cache

- Speichert bereits aufgelöste IP→MAC Zuordnungen
- **Dynamische Einträge**: automatisch erzeugt, Timeout nach ca. **2 Minuten** Inaktivität
- **Statische Einträge**: manuell konfiguriert, bleiben bis zum Neustart
- Anzeige: Windows `arp -a` / Linux `ip neigh`

### Bei Zielen außerhalb des eigenen Subnetzes

- ARP löst die MAC-Adresse des **Default-Gateways** (Router) auf
- Der Router leitet das Paket dann weiter und führt ggf. einen neuen ARP-Vorgang im Zielnetz durch

### Gratuitous ARP

- Host sendet ARP-Request für **seine eigene** IP-Adresse
- Zweck: IP-Konflikte erkennen und ARP-Caches anderer Hosts aktualisieren (z.B. nach NIC-Wechsel)

### ARP-Spoofing (Sicherheitsrisiko)

- Angreifer sendet gefälschte ARP-Replies und ordnet **seine MAC** der IP eines anderen Hosts zu
- Leitet so Traffic über sich um → **Man-in-the-Middle-Angriff**
- Funktioniert nur im **selben lokalen Netz** (Ethernet oder WLAN)
- Gegenmaßnahme: Dynamic ARP Inspection (DAI) auf Managed Switches

---

## STP (Spanning Tree Protocol) - IEEE 802.1d

**Schicht:** 2 (Sicherung) | **Schleifenvermeidung in geswitchten Netzen**

### Problem: Switching Loops

Mehrere physische Verbindungen zwischen Switches → **Schleifen**:
- Broadcast-Frames werden endlos im Kreis geschickt (**Broadcast-Storm**)
- MAC-Adresstabellen werden verfälscht (MAC-Flapping)
- Netzwerk wird komplett lahmgelegt

### Lösung: Spanning Tree

STP erstellt einen **logischen Baum**, in dem zu jedem Ziel nur **ein Pfad** existiert. Redundante Verbindungen werden **blockiert**, bei Ausfall automatisch aktiviert.

### Ablauf

**1. Root Bridge wählen**
- Switches tauschen **BPDUs** (Bridge Protocol Data Units) alle 2 Sekunden aus
- **Bridge ID** = Priorität (Standard: 32768) + MAC-Adresse
- Niedrigste Bridge ID → **Root Bridge**

**2. Pfadkosten berechnen**

| Bandbreite | Pfadkosten |
|---|---|
| 10 Mbit/s | 100 |
| 100 Mbit/s | 19 |
| 1 Gbit/s | 4 |
| 10 Gbit/s | 2 |

**3. Portrollen zuweisen**

| Portrolle | Beschreibung |
|---|---|
| **Root Port** | Port mit geringsten Kosten zur Root Bridge (einer pro Non-Root-Switch) |
| **Designated Port** | Bedient ein Segment Richtung Root Bridge, leitet Daten weiter |
| **Blocked Port** | Redundanter Port, keine Datenweiterleitung |

### RSTP (Rapid Spanning Tree) - IEEE 802.1w

- Konvergenzzeit unter **1 Sekunde** (statt 30-50 Sek. bei STP)
- Neue Rollen: **Alternate Port** (Backup für Root Port), **Backup Port** (Backup für Designated Port)

---

## VLAN (Virtual Local Area Network) - IEEE 802.1q

**Schicht:** 2 (Sicherung) | **Logische Netzwerktrennung**

### Was ist ein VLAN?

Ein VLAN teilt ein physisches Netzwerk in mehrere **logische Netze**. Geräte im selben VLAN können kommunizieren, Geräte in verschiedenen VLANs **nicht** (ohne Router).

### Vorteile

- **Broadcast-Reduktion**: Broadcasts bleiben innerhalb des VLANs
- **Sicherheit**: Trennung ohne separate Hardware
- **Flexibilität**: Gruppierung unabhängig vom physischen Standort
- **Performance**: Weniger unnötige Broadcasts

### VLAN-Tag (802.1q)

```
+----------+----------+----------+----------+--------+-----+
| Ziel-MAC | Quell-MAC| VLAN-Tag | Typ/Len  | Daten  | FCS |
|  6 Byte  |  6 Byte  |  4 Byte  |  2 Byte  |        |4 B  |
+----------+----------+----------+----------+--------+-----+
```

- **TPID** (Tag Protocol Identifier): `0x8100`
- **VID** (VLAN Identifier): 12 Bit → **4096 mögliche VLANs** (IDs 0 und 4095 reserviert)
- **PCP** (Priority Code Point): 3 Bit → **8 Prioritätsstufen** (0-7) für QoS
- **DEI** (Drop Eligible Indicator): 1 Bit → Frames die bei Überlast zuerst verworfen werden

### Porttypen

| Porttyp | Beschreibung |
|---|---|
| **Access Port** | Gehört zu einem VLAN, Frames ohne Tag (für Endgeräte) |
| **Trunk Port** | Transportiert mehrere VLANs (getaggt), zwischen Switches |
| **Native VLAN** | Untagged über Trunk (Standard: VLAN 1) |

### Inter-VLAN-Routing

- Kommunikation zwischen VLANs erfordert **Layer-3-Switch** oder Router
- **Router-on-a-Stick**: Router mit Subinterfaces für jedes VLAN an einem Trunk-Port

### Beispiel

```
Switch 1                      Switch 2
+--------+    Trunk (tagged)  +--------+
| VLAN 10|====================| VLAN 10|  (Buchhaltung)
| VLAN 20|====================| VLAN 20|  (Entwicklung)
| VLAN 30|====================| VLAN 30|  (Gäste)
+--------+                    +--------+
```

---

# Schicht 3: Vermittlung

## ICMP (Internet Control Message Protocol)

**Schicht:** 3 (Vermittlung, Teil von IP) | **Diagnose und Fehlermeldungen**

### Aufgaben

- Übermittlung von **Statusinformationen und Fehlermeldungen** der Protokolle IP, TCP und UDP
- Rechner und Router können sich gegenseitig auf Probleme mit Datenpaketen hinweisen
- ICMP selbst ist unzuverlässig: Gehen ICMP-Meldungen verloren, wird keine Fehlermeldung ausgelöst

### Wichtige ICMP-Nachrichtentypen

| Typ | Name | Beschreibung |
|---|---|---|
| 0 | **Echo Reply** | Antwort auf Ping |
| 3 | **Destination Unreachable** | Ziel nicht erreichbar (versch. Codes für Port/Host/Netz) |
| 5 | **Redirect** | Umleitung zu besserem Router |
| 8 | **Echo Request** | Ping-Anfrage |
| 11 | **Time Exceeded** | TTL abgelaufen (genutzt von Traceroute) |

### Praxistools

- **Ping** (Packet Internet Groper): Sendet Echo Request (Typ 8) → Empfänger antwortet mit Echo Reply (Typ 0). Misst Erreichbarkeit und Antwortzeit (RTT)
- **Traceroute**: Nutzt TTL-Feld aus. Sendet Pakete mit TTL=1, 2, 3... Jeder Router auf dem Weg antwortet mit "Time Exceeded" (Typ 11). So wird die Route zum Ziel sichtbar

### ICMPv6 und NDP

In IPv6 ersetzt **ICMPv6** nicht nur ICMP, sondern auch ARP durch das **Neighbor Discovery Protocol (NDP)**:

| Typ | Name | Funktion |
|---|---|---|
| 133 | Router Solicitation | Host sucht Router |
| 134 | Router Advertisement | Router teilt Präfix und Gateway mit |
| 135 | Neighbor Solicitation | Ersetzt ARP-Request (IP → MAC) |
| 136 | Neighbor Advertisement | Ersetzt ARP-Reply |

> [!warning] ICMPv6 darf **nicht** per Firewall geblockt werden – IPv6 ist darauf angewiesen (SLAAC, NDP).

---

## Routing

**Schicht:** 3 (Vermittlung) | **Wegfindung für IP-Pakete**

### Routing-Tabelle

| Zielnetz | Subnetzmaske | Next Hop | Interface | Metrik |
|---|---|---|---|---|
| 192.168.1.0 | 255.255.255.0 | direkt verbunden | eth0 | 0 |
| 10.0.0.0 | 255.0.0.0 | 192.168.1.1 | eth0 | 1 |
| 0.0.0.0 | 0.0.0.0 | 192.168.1.254 | eth0 | - |

- **Default Route** (0.0.0.0/0): Wenn kein spezifischer Eintrag passt → Paket ans **Default Gateway**

### Routing-Entscheidung

```
Paket kommt an (Ziel-IP: 10.5.3.7)
         |
         v
Ist das Ziel im eigenen Subnetz?
   Ja → direkt zustellen (via ARP)
   Nein → Routing-Tabelle prüfen
              |
              v
     Spezifischer Eintrag?
        Ja → an Next Hop weiterleiten
        Nein → an Default Gateway senden
```

### Statisches vs. Dynamisches Routing

| Eigenschaft | Statisch | Dynamisch |
|---|---|---|
| Konfiguration | Manuell durch Admin | Automatisch durch Protokoll |
| Anpassung | Manuell bei Änderungen | Automatisch |
| Aufwand | Gering bei kleinen Netzen | Gering bei großen Netzen |
| Fehleranfälligkeit | Hoch (vergessene Routen) | Gering (selbstheilend) |
| Einsatz | Kleine Netze | Große, komplexe Netze |

### Dynamische Routing-Protokolle

| Protokoll | Typ | Metrik | Einsatz |
|---|---|---|---|
| **RIP** | Distance Vector | Hop Count (max. 15) | Kleine Netze |
| **OSPF** | Link State | Kosten (Bandbreite) | Große Unternehmensnetze |
| **BGP** | Path Vector | AS-Pfad | Internet (zwischen ISPs) |

> [!info] RIP-Details: Tauscht Routing-Tabellen alle **30 Sekunden** aus. Hop Count **16 = unerreichbar**. Konvergenz nach Router-Ausfall dauert **mehrere Minuten** → ungeeignet für große Netze.

---

## NAT/PAT (Network Address Translation)

**Schicht:** 3 (Vermittlung) | **Adressübersetzung privat ↔ öffentlich**

### Problem

Private IP-Adressen (10.x.x.x, 172.16-31.x.x, 192.168.x.x) sind im Internet **nicht routbar**.

### Arten von NAT

| Art | Zuordnung | Einsatz |
|---|---|---|
| **Static NAT** | 1 privat : 1 öffentlich | Server von außen erreichbar |
| **Dynamic NAT** | n privat : m öffentlich (Pool) | Mehrere öffentliche IPs |
| **PAT / Overloading** | n privat : 1 öffentlich (Ports) | Am häufigsten (Heimrouter) |

### PAT-Ablauf

```
Internes Netz                    Router (NAT)              Internet
192.168.1.10:3000  ──→  203.0.113.5:40001  ──→  93.184.216.34:80
192.168.1.20:3000  ──→  203.0.113.5:40002  ──→  93.184.216.34:80
192.168.1.30:4500  ──→  203.0.113.5:40003  ──→  93.184.216.34:80
```

Der Router speichert Zuordnungen in einer **NAT-Tabelle** und leitet Antworten an den richtigen internen Host zurück.

### SNAT vs. DNAT

| Art | Beschreibung |
|---|---|
| **SNAT** (Source NAT) | Ändert die Quelladresse ausgehender Pakete (Standard-NAT nach außen) |
| **DNAT** (Destination NAT) | Ändert die Zieladresse eingehender Pakete (Port Forwarding) |

### Port Forwarding

- Zugriff von **außen auf interne Server** (= DNAT)
- Router leitet eingehende Verbindungen auf einem bestimmten Port an eine interne IP weiter
- Beispiel: Port 80 von außen → 192.168.1.100:80 intern (Webserver)

### CG-NAT (Carrier-Grade NAT)

- ISP weist Kunden **private IPs** zu und macht NAT auf Provider-Ebene
- Resultat: **doppeltes NAT** (Kunden-Router + Provider-NAT)
- Kein Port Forwarding möglich, höhere Latenz
- Lösung: IPv6 (kein NAT nötig)

---

## IPv6 (Internet Protocol Version 6)

**Schicht:** 3 (Vermittlung) | **Nachfolger von IPv4**

### Warum IPv6?

- IPv4: nur ~**4,3 Milliarden** Adressen (2^32) → Adressraum erschöpft
- IPv6: **340 Sextillionen** Adressen (2^128) → praktisch unerschöpflich
- Vereinfachter Header, eingebaute Sicherheit (IPsec), kein NAT nötig

### Adressformat

- **128 Bit**, 8 Gruppen zu je 4 Hexadezimalziffern, durch Doppelpunkte getrennt
- Beispiel: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

### Kürzungsregeln

1. **Führende Nullen** weglassen: `0db8` → `db8`
2. **Aufeinanderfolgende Null-Gruppen** einmalig durch `::` ersetzen

```
Voll:    2001:0db8:0000:0000:0000:0000:0000:0001
Kurz:    2001:db8::1
```

### Adresstypen

| Typ | Beschreibung | Beispiel |
|---|---|---|
| **Unicast** | An ein einzelnes Interface | `2001:db8::1` |
| **Multicast** | An eine Gruppe von Interfaces | `ff02::1` (alle Knoten) |
| **Anycast** | An den nächsten aus einer Gruppe | Routing-optimiert |
| **Link-Local** | Nur im lokalen Netzwerk gültig | `fe80::/10` |
| **Global Unicast** | Weltweit routbar | `2000::/3` |
| **Loopback** | Eigenes Gerät | `::1` |

### Vergleich IPv4 vs. IPv6

| Eigenschaft | IPv4 | IPv6 |
|---|---|---|
| Adresslänge | 32 Bit | 128 Bit |
| Notation | Dezimal (192.168.1.1) | Hexadezimal (2001:db8::1) |
| Adressanzahl | ~4,3 Milliarden | ~340 Sextillionen |
| Header-Größe | 20-60 Byte (variabel) | 40 Byte (fix) |
| NAT | Häufig nötig | Nicht nötig |
| Broadcast | Ja | Nein (ersetzt durch Multicast) |
| IPsec | Optional | Integriert |
| Autokonfiguration | DHCP | SLAAC + DHCPv6 |

### SLAAC (Stateless Address Autoconfiguration)

IPv6-Hosts können sich **ohne DHCP** selbst eine Adresse zuweisen:

1. Host erzeugt **Link-Local-Adresse** (`fe80::` + Interface Identifier aus MAC)
2. Host sendet **Router Solicitation** (ICMPv6 Typ 133)
3. Router antwortet mit **Router Advertisement** (Typ 134) inkl. globalem Präfix
4. Host kombiniert **Präfix + Interface Identifier** = Global Unicast Adresse
5. **Duplicate Address Detection** (DAD) prüft auf Konflikte

**Modified EUI-64** (Interface Identifier aus MAC):
```
MAC:     00:1A:2B:3C:4D:5E
         ↓ FF:FE einfügen ↓ 7. Bit invertieren
EUI-64:  02:1A:2B:FF:FE:3C:4D:5E
```

> [!info] Standard-Präfixlänge ist **/64**, weil SLAAC 64 Bit für den Interface Identifier benötigt. Windows verwendet aus Datenschutzgründen **Privacy Extensions** (zufälliger IID statt EUI-64).

### Weitere IPv6-Adresstypen

| Typ | Präfix | Beschreibung |
|---|---|---|
| **Unique-Local** | `fc00::/7` | IPv6-Pendant zu privaten Adressen (RFC 1918) |
| **Site-Local** | `fec0::/10` | Veraltet (deprecated) |

### Übergangsmechanismen

- **Dual-Stack**: Gerät spricht IPv4 und IPv6 gleichzeitig
- **Tunneling**: IPv6-Pakete werden in IPv4-Pakete verpackt (z.B. 6to4)
- **Translation**: NAT64 übersetzt zwischen IPv4 und IPv6

---

# Schicht 4: Transport

## TCP (Transmission Control Protocol)

**Schicht:** 4 (Transport) | **Verbindungsorientiert** | **Zuverlässig**

### Eigenschaften

- Stellt eine **logische Verbindung** her, bevor Daten übertragen werden
- Garantiert die **korrekte Reihenfolge** der Datenpakete
- **Fehlererkennung**: Verlorene Pakete werden erneut gesendet
- **Flusskontrolle**: Passt Sendegeschwindigkeit an den Empfänger an
- Datenströme werden in **Segmente** aufgeteilt und beim Empfänger zusammengesetzt
- **MSS** (Maximum Segment Size): typisch **1460 Byte** (MTU 1500 − 20 IP-Header − 20 TCP-Header)

### TCP-Header (mind. 20 Byte)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Quell-Port           |          Ziel-Port            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Sequenznummer                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgement-Nummer                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Offset | Res.  |U|A|P|R|S|F|        Window-Größe              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Prüfsumme            |        Urgent-Pointer          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Feld | Bits | Beschreibung |
|---|---|---|
| **Quell-Port** | 16 | Portnummer der sendenden Anwendung |
| **Ziel-Port** | 16 | Portnummer der empfangenden Anwendung |
| **Sequenznummer** | 32 | Nummeriert die gesendeten Bytes zur Reihenfolge-Kontrolle |
| **Acknowledgement-Nr.** | 32 | Bestätigt empfangene Bytes (nächstes erwartetes Byte) |
| **Data Offset** | 4 | Länge des TCP-Headers in 32-Bit-Blöcken |
| **Flags** | 6 | Steuerbits (SYN, ACK, FIN, RST, PSH, URG) |
| **Window-Größe** | 16 | Größe des Empfangspuffers (Flusskontrolle) |
| **Prüfsumme** | 16 | Fehlererkennung über Header und Daten |
| **Urgent-Pointer** | 16 | Zeigt auf dringend zu verarbeitende Daten |

### TCP-Flags

| Flag | Name | Bedeutung |
|---|---|---|
| **SYN** | Synchronize | Verbindungsaufbau einleiten |
| **ACK** | Acknowledge | Empfangsbestätigung |
| **FIN** | Finish | Verbindungsabbau einleiten |
| **RST** | Reset | Verbindung sofort abbrechen |
| **PSH** | Push | Daten sofort an Anwendung weiterleiten |
| **URG** | Urgent | Dringende Daten (Urgent-Pointer gültig) |

### 3-Way-Handshake (Verbindungsaufbau)

```
Client                          Server
  |                                |
  |  1. SYN (seq=x)               |
  |------------------------------->|
  |                                |
  |  2. SYN+ACK (seq=y, ack=x+1)  |
  |<-------------------------------|
  |                                |
  |  3. ACK (ack=y+1)             |
  |------------------------------->|
  |                                |
  |  === Verbindung steht ===      |
```

1. Client sendet **SYN** mit einer zufälligen Sequenznummer
2. Server antwortet mit **SYN+ACK** (eigene Sequenznummer + Bestätigung)
3. Client bestätigt mit **ACK** → Verbindung ist aufgebaut

### Verbindungsabbau (4-Way-Handshake)

```
Client                          Server
  |  FIN  →                        |
  |<−  ACK                         |
  |                                |
  |                  ←  FIN        |
  |  ACK  →                        |
```

Beide Seiten müssen ihre Senderichtung einzeln beenden (FIN + ACK).

---

## UDP (User Datagram Protocol)

**Schicht:** 4 (Transport) | **Verbindungslos** | **Unzuverlässig**

### Eigenschaften

- Kein Verbindungsaufbau nötig (kein Handshake)
- Keine Empfangsbestätigung → Absender weiß nicht ob Paket ankam
- Keine Reihenfolge-Garantie
- Kein Retransmit bei Paketverlust
- **Vorteil**: Geringerer Overhead, schneller, weniger Latenz

### UDP-Header (8 Byte)

| Feld | Bits | Beschreibung |
|---|---|---|
| **Quell-Port** | 16 | Port des Senders |
| **Ziel-Port** | 16 | Port des Empfängers |
| **Länge** | 16 | Gesamtgröße des UDP-Pakets in Byte |
| **Checksumme** | 16 | Fehlerprüfung (optional bei IPv4) |

### Einsatzgebiete

- **DNS**-Anfragen (schnelle Einzelanfragen)
- **DHCP** (IP-Konfiguration)
- **VoIP** und Video-Streaming (Echtzeitdaten)
- **Online-Gaming** (Latenz wichtiger als Zuverlässigkeit)
- **TFTP** (Trivial File Transfer)

### Vergleich TCP vs. UDP

| Eigenschaft | TCP | UDP |
|---|---|---|
| Verbindung | verbindungsorientiert | verbindungslos |
| Zuverlässigkeit | ja (ACK, Retransmit) | nein |
| Reihenfolge | garantiert | nicht garantiert |
| Geschwindigkeit | langsamer (Overhead) | schneller |
| Header-Größe | mind. 20 Byte | 8 Byte |
| Flusskontrolle | ja | nein |
| Einsatz | Web, E-Mail, Dateitransfer | Streaming, DNS, Gaming |

---

# Schicht 5-6: Sitzung & Darstellung

## TLS/SSL (Transport Layer Security)

**Schicht:** 5-6 (Sitzung/Darstellung) | **Verschlüsselung & Authentifizierung**

### Was ist TLS?

**TLS** (Transport Layer Security) ist der Nachfolger von **SSL** (Secure Sockets Layer). Es verschlüsselt die Kommunikation zwischen zwei Endpunkten und stellt sicher, dass Daten nicht abgehört oder manipuliert werden können.

| Version | Status | Anmerkung |
|---|---|---|
| SSL 2.0 / 3.0 | Veraltet, unsicher | Nicht mehr verwenden |
| TLS 1.0 / 1.1 | Veraltet | Seit 2020 abgekündigt |
| TLS 1.2 | Aktuell | Weit verbreitet, sicher |
| TLS 1.3 | Aktuell (empfohlen) | Schneller, sicherer, weniger Handshake-Schritte |

### Funktionen

- **Vertraulichkeit**: Daten werden verschlüsselt (symmetrisch mit AES etc.)
- **Integrität**: Manipulation wird durch MACs (Message Authentication Codes) erkannt
- **Authentifizierung**: Server (und optional Client) weist seine Identität per **Zertifikat** nach

### TLS-Handshake (vereinfacht)

```
Client                              Server
  |  1. ClientHello                    |
  |  (TLS-Version, Cipher Suites)     |
  |----------------------------------->|
  |                                    |
  |  2. ServerHello + Zertifikat       |
  |  (gewählte Cipher Suite)           |
  |<-----------------------------------|
  |                                    |
  |  3. Client prüft Zertifikat        |
  |  (CA-Kette verifizieren)           |
  |                                    |
  |  4. Schlüsselaustausch             |
  |  (Pre-Master Secret / ECDHE)       |
  |----------------------------------->|
  |                                    |
  |  5. Beide berechnen Session Key    |
  |                                    |
  |  === Verschlüsselte Verbindung === |
  |<===================================>|
```

### Schlüsselaustausch

1. **Asymmetrische Verschlüsselung** (RSA / ECDHE) für den Schlüsselaustausch
2. **Symmetrische Verschlüsselung** (AES) für die eigentliche Datenübertragung → schneller
3. Der **Session Key** wird bei jedem Verbindungsaufbau neu ausgehandelt

### Zertifikate

- Ausgestellt von einer **CA** (Certificate Authority), z.B. Let's Encrypt, DigiCert
- Enthalten: Domainname, öffentlicher Schlüssel, Gültigkeitszeitraum, CA-Signatur
- **Vertrauenskette**: Root-CA → Intermediate-CA → Server-Zertifikat
- Browser/OS haben eine Liste vertrauenswürdiger Root-CAs vorinstalliert

**Validierungsstufen:**

| Stufe | Prüfung | Aufwand |
|---|---|---|
| **DV** (Domain Validated) | Nur Domain-Besitz | Minuten, kostenlos (Let's Encrypt) |
| **OV** (Organisation Validated) | Organisation wird geprüft | Tage, kostenpflichtig |
| **EV** (Extended Validation) | Gründliche Identitätsprüfung | Wochen, teuer |

### TLS 1.3 Neuerungen

- RSA-Schlüsselaustausch entfernt → nur noch **ECDHE** (Perfect Forward Secrecy)
- Handshake selbst ist verschlüsselt
- Unsichere Algorithmen entfernt (RC4, MD5, SHA-1, CBC-Mode)
- **0-RTT**: Schnellere Wiederaufnahme bekannter Verbindungen (aber anfällig für Replay)

### Cipher Suite (Beispiel)

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
 │    │     │        │    │    │
 │    │     │        │    │    └─ Hash-Algorithmus (Integrität)
 │    │     │        │    └────── Betriebsmodus (Authenticated Encryption)
 │    │     │        └─────────── Symmetrischer Algorithmus (Verschlüsselung)
 │    │     └──────────────────── Authentifizierung (Zertifikat-Typ)
 │    └────────────────────────── Schlüsselaustausch
 └─────────────────────────────── Protokoll
```

### TLS in der Praxis

| Protokoll | Ohne TLS | Mit TLS | Port |
|---|---|---|---|
| HTTP | Port 80 | **HTTPS** (Port 443) | 443 |
| SMTP | Port 25 | **SMTPS** / STARTTLS | 465/587 |
| IMAP | Port 143 | **IMAPS** | 993 |
| POP3 | Port 110 | **POP3S** | 995 |
| FTP | Port 21 | **FTPS** | 990 |
| LDAP | Port 389 | **LDAPS** | 636 |

### Schutzziele

- **Abhören** verhindern (Vertraulichkeit)
- **Manipulation** erkennen (Integrität)
- **Man-in-the-Middle-Angriffe** verhindern (Authentifizierung)
- **Replay-Angriffe** verhindern (Sequenznummern im Handshake)

---

# Schicht 7: Anwendung

## DHCP (Dynamic Host Configuration Protocol)

**Schicht:** 7 (Anwendung) | **Automatische Netzwerkkonfiguration** | Port 67 (Server), 68 (Client)

### Aufgabe

Automatische Vergabe von IP-Adresse, Subnetzmaske, Standard-Gateway und DNS-Server an Geräte im Netzwerk.

### DORA-Prozess (Ablauf)

```
Client                          DHCP-Server
  |  1. DISCOVER (Broadcast)       |
  |------------------------------->|
  |  2. OFFER (IP-Angebot)         |
  |<-------------------------------|
  |  3. REQUEST (IP anfordern)     |
  |------------------------------->|
  |  4. ACK (Bestätigung)          |
  |<-------------------------------|
```

1. **Discover**: Client sucht per Broadcast nach einem DHCP-Server
2. **Offer**: Server bietet eine freie IP-Adresse an
3. **Request**: Client akzeptiert das Angebot
4. **Acknowledge**: Server bestätigt und vergibt die Adresse für eine bestimmte **Lease-Time**

### Details zum DORA-Prozess

- **Discover** verwendet Quell-IP `0.0.0.0` und Ziel `255.255.255.255` (Client hat noch keine IP)
- **Offer** enthält: angebotene IP, Lease-Time, Subnetzmaske, DHCP-Server-IP
- DHCP kann zusätzlich vergeben: DNS-Server, WINS-Server, Domainname, NTP-Server

### Lease-Time

- IP-Adresse wird nur für eine bestimmte Zeit vergeben
- Client versucht Verlängerung nach **50%** der Lease-Time (DHCP-REQUEST an den Server)
- Bei keiner Antwort: erneuter Versuch bei **87,5%** per Broadcast
- Bei 100% abgelaufen: beginnt komplett neu mit DISCOVER

### APIPA (Automatic Private IP Addressing)

Wenn **kein DHCP-Server** erreichbar ist, weisen sich Hosts automatisch eine Adresse aus `169.254.0.0/16` zu (Link-Local). Damit ist nur Kommunikation im lokalen Netz möglich, **kein** Internetzugang.

---

## DNS (Domain Name System)

**Schicht:** 7 (Anwendung) | **Namensauflösung** | Port 53 (UDP/TCP)

### Aufgabe

Übersetzung von menschenlesbaren Domainnamen in IP-Adressen:
`www.example.com` → `93.184.216.34`

### Hierarchischer Aufbau

```
              . (Root)
             / \
          .de   .com   .org  ...
          /       \
     example    google
       /           \
     www          mail
```

- **Root-Server**: Oberste Ebene, verweisen auf TLD-Server
- **TLD-Server** (Top-Level-Domain): `.de`, `.com`, `.org` etc.
- **Autoritative Nameserver**: Kennen die tatsächlichen IP-Adressen einer Domain

### Rekursive vs. Iterative Auflösung

| Art | Beschreibung |
|---|---|
| **Rekursiv** | Resolver übernimmt die komplette Auflösung für den Client (fragt alle Server durch) |
| **Iterativ** | DNS-Server antwortet nur mit Verweis auf nächsten Server; Anfragender muss selbst weitersuchen |

Typisch: Client → Resolver ist **rekursiv**, Resolver → Root/TLD/Autoritativ ist **iterativ**.

### Ablauf einer DNS-Anfrage

1. Client prüft lokalen Cache und **hosts-Datei** (`/etc/hosts` bzw. `C:\Windows\System32\drivers\etc\hosts`)
2. Client fragt den **lokalen DNS-Resolver** (meist vom ISP oder Router)
3. Falls nicht im Cache: Resolver fragt **Root-Server** → erhält Verweis auf TLD-Server
4. Resolver fragt **TLD-Server** → erhält Verweis auf autoritativen Nameserver
5. Resolver fragt **autoritativen Nameserver** → erhält die IP-Adresse
6. Ergebnis wird im Cache gespeichert (TTL-basiert)

> [!info] DNS nutzt **UDP** für normale Anfragen (schnell, < 512 Byte). Bei großen Antworten und **Zonentransfers** (Replikation zwischen Nameservern) wird **TCP** verwendet.

### DNS-Record-Typen

| Typ | Beschreibung |
|---|---|
| **A** | IPv4-Adresse |
| **AAAA** | IPv6-Adresse |
| **CNAME** | Alias (Verweis auf anderen Domainnamen) |
| **MX** | Mailserver für die Domain |
| **NS** | Autoritativer Nameserver |
| **PTR** | Reverse-DNS (IP → Name) |
| **SOA** | Start of Authority (Zonen-Parameter, Kontaktinfo) |
| **SRV** | Service-Lokalisierung (z.B. Active Directory) |
| **TXT** | Freitext (z.B. SPF-Records für E-Mail) |

---

## HTTP/HTTPS (Hypertext Transfer Protocol)

**Schicht:** 7 (Anwendung) | **Webkommunikation** | Port 80 (HTTP), 443 (HTTPS)

### Funktionsweise

- Client (Browser) sendet **Request** an Server
- Server verarbeitet Anfrage und sendet **Response** zurück
- **Zustandslos**: Jede Anfrage ist unabhängig (Cookies/Sessions für Zustandsverwaltung)
- Basiert auf **TCP** (zuverlässige Übertragung)

### HTTP-Methoden

| Methode | Beschreibung |
|---|---|
| **GET** | Daten vom Server anfordern (z.B. Webseite laden) |
| **POST** | Daten an Server senden (z.B. Formular absenden) |
| **PUT** | Ressource vollständig ersetzen/aktualisieren |
| **DELETE** | Ressource löschen |
| **PATCH** | Ressource teilweise ändern |
| **HEAD** | Wie GET, aber nur Header zurück (ohne Body) |

### HTTP-Request (Aufbau)

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### HTTP-Response (Aufbau)

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

### Statuscodes

| Code | Kategorie | Beispiele |
|---|---|---|
| **1xx** | Information | 100 Continue |
| **2xx** | Erfolg | 200 OK, 201 Created |
| **3xx** | Umleitung | 301 Moved Permanently, 302 Found |
| **4xx** | Client-Fehler | 400 Bad Request, 403 Forbidden, 404 Not Found |
| **5xx** | Server-Fehler | 500 Internal Server Error, 503 Service Unavailable |

### HTTP-Versionen

| Version | Besonderheiten |
|---|---|
| **HTTP/1.1** | Eine Anfrage pro TCP-Verbindung, Pipelining möglich |
| **HTTP/2** | **Multiplexing** (viele Anfragen über eine TCP-Verbindung), Header-Kompression, Server Push, binäres Protokoll |
| **HTTP/3** | Basiert auf **QUIC** (UDP statt TCP), integriert TLS 1.3, bessere Performance bei Paketverlust |

### HTTPS

**HTTPS** = HTTP + **TLS** Verschlüsselung (Port 443)

- Gesamte HTTP-Kommunikation wird durch TLS-Tunnel geleitet
- Schützt vor Abhören, Manipulation und Man-in-the-Middle-Angriffen
- Erkennbar am Schloss-Symbol im Browser und `https://` in der URL

---

## FTP (File Transfer Protocol)

**Schicht:** 7 (Anwendung) | **Dateiübertragung** | Port 21 (Steuerung), 20 (Daten)

### Eigenschaften

- Verwendet **zwei getrennte Verbindungen**: Steuerkanal und Datenkanal
- Basiert auf TCP
- Überträgt Daten **unverschlüsselt** (Benutzername, Passwort im Klartext)
- Unterstützt Hoch- und Herunterladen, Verzeichnisnavigation

### Steuerkanal vs. Datenkanal

| Kanal | Port | Aufgabe |
|---|---|---|
| **Steuerkanal** | 21 | Befehle und Antworten (Login, cd, ls, get, put) |
| **Datenkanal** | 20 (aktiv) / dynamisch (passiv) | Eigentliche Dateiübertragung |

### Aktiver vs. Passiver Modus

**Aktiver Modus:** Server baut Datenverbindung zum Client auf (Port 20) → Problem: Firewall blockiert oft eingehende Verbindungen

**Passiver Modus:** Client baut **beide** Verbindungen auf → firewall-freundlicher, heute Standard

### Sichere Alternativen

- **FTPS**: FTP über TLS (verschlüsselt, Ports 989/990)
- **SFTP**: SSH File Transfer Protocol (läuft über SSH, Port 22)

---

## SMTP, POP3 und IMAP (E-Mail-Protokolle)

**Schicht:** 7 (Anwendung) | **E-Mail-Kommunikation**

### E-Mail-Weg

```
Absender                                                    Empfänger
[Mail-Client] --SMTP--> [Mail-Server] --SMTP--> [Mail-Server] <--POP3/IMAP-- [Mail-Client]
  (Outlook)              (Absender)              (Empfänger)                  (Thunderbird)
```

- **SMTP** wird zum **Senden** verwendet (Client→Server und Server→Server)
- **POP3 oder IMAP** wird zum **Abrufen** verwendet (Server→Client)

### SMTP (Simple Mail Transfer Protocol)

| Port | 25 (unverschlüsselt), 587 (STARTTLS), 465 (SSL/TLS) |
|---|---|
| **Aufgabe** | E-Mail-Versand und -Weiterleitung |
| **Befehle** | HELO, MAIL FROM, RCPT TO, DATA, QUIT |

### POP3 vs. IMAP

| Eigenschaft | POP3 (Port 110/995) | IMAP (Port 143/993) |
|---|---|---|
| Speicherort | Lokal (Client) | Server |
| Mehrere Geräte | Nein (nur eins) | Ja |
| Ordner/Struktur | Nein | Ja |
| Offline-Zugriff | Ja (nach Download) | Eingeschränkt |
| Serverspeicher | Gering | Hoch |
| Synchronisation | Keine | Alle Geräte synchron |

---

## SSH (Secure Shell)

**Schicht:** 7 (Anwendung) | **Verschlüsselter Fernzugriff** | Port 22

### Eigenschaften

- Vollständig **verschlüsselte** Kommunikation (Authentifizierung + Daten)
- Ersetzt das unsichere **Telnet** (Port 23, Klartext)
- Basiert auf TCP

### Authentifizierungsmethoden

| Methode | Beschreibung |
|---|---|
| **Passwort** | Benutzername + Passwort (verschlüsselt übertragen) |
| **Public-Key** | Schlüsselpaar: privater Key beim Client, öffentlicher Key auf dem Server. Sicherer |

### SSH vs. Telnet

| Eigenschaft | SSH | Telnet |
|---|---|---|
| Port | 22 | 23 |
| Verschlüsselung | Ja (komplett) | Nein (Klartext) |
| Authentifizierung | Passwort oder Key | Nur Passwort |
| Einsatz heute | Standard | Veraltet |

### Einsatzgebiete

- **Remote-Administration**: Kommandozeile auf Servern, Routern, Switches
- **SCP** (Secure Copy): Dateikopie über SSH
- **SFTP**: Dateiübertragung über SSH
- **SSH-Tunnel / Port-Forwarding**: Verschlüsselte Weiterleitung von Ports

---

# Referenz

## Wichtige Portnummern

| Port | Protokoll | Dienst |
|---|---|---|
| 20/21 | TCP | FTP (Daten/Steuerung) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet (unsicher) |
| 25 | TCP | SMTP (E-Mail-Versand) |
| 53 | UDP/TCP | DNS |
| 67/68 | UDP | DHCP (Server/Client) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (STARTTLS) |
| 636 | TCP | LDAPS |
| 989/990 | TCP | FTPS |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3389 | TCP | RDP (Remote Desktop) |

**Portbereiche:**
- **0-1023**: Well-Known Ports (reserviert für Standarddienste)
- **1024-49151**: Registered Ports (registrierte Anwendungen)
- **49152-65535**: Dynamic/Private Ports (temporär, frei verwendbar)

---

## Siehe auch

- [[Netzwerk-Grundlagen und OSI]]
- [[Physische Netzwerkinfrastruktur]]
- [[Aktive Komponenten und Konfiguration]]
