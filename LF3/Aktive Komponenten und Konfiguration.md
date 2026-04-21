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
| **D**  | 224.0.0.0 - 239.x.x.x | –         | Multicast     |
| **E**  | 240.0.0.0 - 255.x.x.x | –         | Reserviert    |

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
| 0.0.0.0          | Unbekannter Host / Standardroute      |
| 127.0.0.1        | Localhost (Loopback)                  |
| 169.254.x.x      | **APIPA** (kein DHCP erreichbar)      |
| 255.255.255.255  | Broadcast (alle im Netzwerk)          |
| x.x.x.0          | Netzwerkadresse                       |
| x.x.x.255        | Broadcast-Adresse (/24)               |

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

### VLSM (Variable Length Subnet Mask)

Verschiedene Subnetze im selben Netzwerk können **unterschiedliche Präfixlängen** haben. So wird der Adressraum effizienter genutzt (z.B. eine Abteilung /25, eine andere /27).

### Subnetting-Beispiel (IHK-typisch)

**Gegeben:** `172.16.50.130/27`

1. /27 = 27 Netz-Bits, **5 Host-Bits**
2. Blockgröße = 2^5 = **32**
3. Subnetz-Grenzen bei Vielfachen von 32: ...96, **128**, 160...
4. 130 liegt im Block **128-159**
5. **Netzadresse:** `172.16.50.128`
6. **Broadcast:** `172.16.50.159`
7. **Nutzbarer Bereich:** `.129` bis `.158` (30 Hosts)

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

> [!success] Lösung
> **1. Switch – Paketweiterleitung:**
> Ein Switch verbindet mehrere Geräte innerhalb eines lokalen Netzwerks (LAN) und leitet eingehende Ethernet-Frames gezielt an den richtigen Zielport weiter. Dazu lernt er selbstständig die MAC-Adressen der angeschlossenen Geräte und speichert sie in einer MAC-Adresstabelle (CAM-Table). Kommt ein Frame an, schlägt der Switch die Ziel-MAC-Adresse in der Tabelle nach und sendet den Frame nur an den entsprechenden Port – anders als ein Hub, der an alle Ports sendet (Flooding). Dies reduziert Kollisionen und erhöht die Effizienz erheblich.
>
> **2. Access Point – Funktion:**
> Ein Access Point (AP) dient als Brücke (Bridge) zwischen dem kabelgebundenen LAN und einem WLAN. Er empfängt Datenpakete aus dem Ethernet-Netzwerk und überträgt sie per Funk an WLAN-Clients (Smartphones, Laptops) – und umgekehrt. Der AP selbst ist per Ethernet-Kabel (oft via PoE) mit dem Switch verbunden. Mehrere APs können ein Netzwerk flächendeckend abdecken und sich eine SSID teilen, sodass Clients nahtlos zwischen APs wechseln können (Roaming).
>
> **3. Router – Funktion:**
> Ein Router verbindet zwei oder mehr unterschiedliche Netzwerke (z. B. LAN und Internet) und leitet IP-Pakete anhand der Ziel-IP-Adresse und seiner Routing-Tabelle weiter. Er führt NAT (Network Address Translation) durch, um private IP-Adressen auf eine öffentliche Adresse abzubilden. Häufig sind auch DHCP-Server und Firewall-Funktionen integriert. Der Router ist das Standard-Gateway für alle Geräte im lokalen Netzwerk.
>
> **4. OSI-Schichtzuordnung:**
> | Gerät | OSI-Schicht | Adressierungsebene | Weiterleitung basierend auf |
> | ----- | ----------- | ------------------ | --------------------------- |
> | **Hub / Repeater** | Schicht 1 (Bitübertragung) | – | Kein Filtern – sendet an alle Ports |
> | **Switch** | Schicht 2 (Sicherung) | MAC-Adresse | MAC-Adresstabelle (CAM-Table) |
> | **Access Point** | Schicht 1–2 (Bridge) | MAC-Adresse | Überbrückt LAN ↔ WLAN |
> | **Router** | Schicht 3 (Vermittlung) | IP-Adresse | Routing-Tabelle |
> | **Layer-3-Switch** | Schicht 2–3 | MAC + IP | Kombiniert Switching und Routing |

> [!example] Aufgabe 2 - Bedarfsanalyse aktive Komponenten
> Wähle aus dem Lieferantenkatalog passende Switches und Access Points für die ZeroTake Coffee UG.
> Dokumentiere: Modell, Leistungsmerkmale, Preise.

> [!example] Aufgabe 3 - IPv4 (S. 306/307)
> 1. Netzwerktopologien studieren
> 2. IPv4-Grundlagen: Private/öffentliche Adressen, CIDR, Subnetting
> 3. Default Gateway erklären
> 4. CLI-Befehle testen: `ipconfig`, `ping`, Broadcast

> [!success] Lösung
> **1. Netzwerktopologien – Zusammenfassung:**
> | Topologie | Aufbau | Vorteil | Nachteil |
> | --------- | ------ | ------- | -------- |
> | Stern | Alle Geräte am zentralen Switch | Einfach, Ausfall eines Geräts unkritisch | Switch = Single Point of Failure |
> | Ring | Geräte in geschlossener Kette | Deterministische Übertragung | Ein Ausfall unterbricht das ganze Netz |
> | Bus | Alle an einem Kabel | Günstig, wenig Kabel | Kollisionen, schwer zu erweitern |
> | Mesh | Jeder mit jedem verbunden | Sehr ausfallsicher | Teuer, hoher Verkabelungsaufwand |
> | Baum | Hierarchische Sternstruktur | Skalierbar, strukturiert | Root-Knoten ist kritisch |
> In modernen LANs wird fast ausschließlich die **Sterntopologie** eingesetzt (physisch), während logisch oft eine Baumstruktur entsteht.
>
> **2. IPv4-Grundlagen:**
> Eine IPv4-Adresse besteht aus 32 Bit (4 Oktette), z. B. `192.168.1.100/24`. Die Subnetzmaske (`/24` = `255.255.255.0`) trennt den Netzanteil vom Hostanteil.
> - **Private Adressen** (RFC 1918): `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` – nur im internen Netz, nicht im Internet routbar
> - **Öffentliche Adressen**: weltweit eindeutig, vom ISP zugewiesen
> - **CIDR** (Classless Inter-Domain Routing): flexible Subnetzmaske statt fixer Klassen (`/24`, `/25` etc.)
> - **Subnetting-Formel**: Hosts = 2^(32 − Präfix) − 2 (−2 für Netz- und Broadcastadresse)
> - **Beispiel /26**: 2^(32−26) − 2 = 62 nutzbare Hosts
>
> **3. Default Gateway:**
> Das Default Gateway ist die IP-Adresse des Routers im lokalen Netzwerk. Wenn ein Gerät ein Paket an eine IP-Adresse außerhalb des eigenen Subnetzes senden will, schickt es das Paket an das Gateway, das es dann ins richtige Netzwerk weiterleitet. Ohne konfiguriertes Gateway ist keine Kommunikation über das eigene Subnetz hinaus möglich.
> Beispiel: PC `192.168.1.100/24` → Gateway `192.168.1.1` → Internet
>
> **4. Wichtige CLI-Befehle:**
> | Befehl | OS | Funktion |
> | ------ | -- | -------- |
> | `ipconfig` | Windows | Zeigt IP-Adresse, Subnetzmaske, Gateway |
> | `ipconfig /all` | Windows | Zeigt zusätzlich MAC-Adresse, DHCP-Server, DNS |
> | `ip a` / `ifconfig` | Linux | Netzwerkkonfiguration anzeigen |
> | `ping 192.168.1.1` | beide | Erreichbarkeit des Gateways prüfen |
> | `ping 255.255.255.255` | beide | Broadcast-Ping an alle im Subnetz |
> | `tracert` / `traceroute` | Win/Linux | Route zum Zielgerät mit allen Hops anzeigen |
> | `arp -a` | beide | ARP-Tabelle (IP ↔ MAC Zuordnungen) anzeigen |

> [!example] Aufgabe 4 - Cisco Packet Tracer
> 1. Cisco PT Training durcharbeiten
> 2. Übungsaufgabe lösen
> 3. ZeroTake-Netzwerk in PT konfigurieren (Excel-Planung → PT-Umsetzung)

> [!example] Aufgabe 5 - IPv4-Header
> Analysiere im PT-Simulationsmodus den IPv4-Header eines Pakets. Recherchiere die Felder.

> [!success] Lösung
> Der IPv4-Header ist mindestens 20 Byte groß und enthält folgende wichtige Felder:
>
> | Feld | Größe | Beschreibung |
> | ---- | ----- | ------------ |
> | **Version** | 4 Bit | Protokollversion – bei IPv4 immer `4` |
> | **IHL (Internet Header Length)** | 4 Bit | Länge des Headers in 32-Bit-Wörtern (min. 5 = 20 Byte) |
> | **DSCP / TOS** | 8 Bit | Dienstgüte (Quality of Service) – Priorität des Pakets |
> | **Total Length** | 16 Bit | Gesamtlänge des IP-Pakets (Header + Nutzdaten) in Byte |
> | **Identification** | 16 Bit | ID zur Zusammensetzung fragmentierter Pakete |
> | **Flags** | 3 Bit | Steuerung der Fragmentierung (z. B. DF = Don't Fragment) |
> | **Fragment Offset** | 13 Bit | Position dieses Fragments im ursprünglichen Paket |
> | **TTL (Time to Live)** | 8 Bit | Maximale Hop-Anzahl; wird bei jedem Router um 1 verringert – bei 0 wird das Paket verworfen |
> | **Protocol** | 8 Bit | Übergeordnetes Protokoll: TCP = 6, UDP = 17, ICMP = 1 |
> | **Header Checksum** | 16 Bit | Prüfsumme des Headers zur Fehlererkennung |
> | **Source Address** | 32 Bit | IP-Adresse des Absenders |
> | **Destination Address** | 32 Bit | IP-Adresse des Empfängers |
> | **Options** | variabel | Optionale Felder (selten genutzt, z. B. Routing-Vorgaben) |
>
> Im Cisco Packet Tracer Simulationsmodus kann man ein Paket anklicken und im PDU-Fenster alle Headerfelder mit ihren aktuellen Werten einsehen.

> [!example] Aufgabe 6 - OSI-Modell erweitern
> Erweitere deine OSI-Übersicht um: Topologien, IPv4-Adressierung, Header-Struktur, Konnektivitätstests

> [!success] Lösung
> Erweiterung der OSI-Übersicht um die in dieser Lerneinheit behandelten Inhalte:
>
> | Schicht | Name | Ergänzungen aus LF3 |
> | ------- | ---- | ------------------- |
> | **7** | Anwendung | Konnektivitätstests: `ping`, `tracert` nutzen ICMP auf höherer Ebene; DNS-Auflösung (nslookup) |
> | **6** | Darstellung | – (keine direkten Ergänzungen in dieser LE) |
> | **5** | Sitzung | – (keine direkten Ergänzungen in dieser LE) |
> | **4** | Transport | TCP/UDP-Protokollfeld im IPv4-Header (Protocol-Feld = 6/17); Ports identifizieren Dienste |
> | **3** | Vermittlung | **IPv4-Adressierung**: private/öffentliche Adressen, CIDR, Subnetting; **IPv4-Header**: TTL, Protocol, Src/Dst Address; **Routing** über Default Gateway; Geräte: Router, Layer-3-Switch |
> | **2** | Sicherung | **Topologien** (physisch): Stern, Ring, Bus, Mesh, Baum; **Switch** (MAC-Adresstabelle, Paketweiterleitung); **Access Point** (Bridge LAN↔WLAN); Ethernet-Frames mit MAC-Adressen |
> | **1** | Bitübertragung | **Verkabelung**: TP (Cat 6a), LWL (Single/Multi-Mode); **WLAN** (Wi-Fi 6/6E, Frequenzbänder); **Topologie** (physisch): bestimmt, wie Geräte physisch verbunden sind |
>
> **Konnektivitätstests im Überblick:**
> | Test | Befehl | Getestete Schicht | Zweck |
> | ---- | ------- | ----------------- | ----- |
> | Loopback | `ping 127.0.0.1` | Schicht 3 (lokal) | TCP/IP-Stack des eigenen Geräts prüfen |
> | Gateway | `ping 192.168.x.1` | Schicht 3 | LAN-Verbindung und Router prüfen |
> | Internet | `ping 8.8.8.8` | Schicht 3 | Internetverbindung prüfen |
> | DNS | `nslookup google.com` | Schicht 7 | DNS-Auflösung prüfen |
> | Route | `tracert / traceroute` | Schicht 3 | Alle Hops auf dem Weg zum Ziel anzeigen |

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
