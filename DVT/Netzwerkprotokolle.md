---
fach: DVT
thema: Netzwerkprotokolle
tags: [netzwerk, protokolle]
datum: 2026-04-14
typ: notiz
---

## Uebersicht der wichtigsten Protokolle

| Protokoll | Schicht (OSI) | Typ | Aufgabe |
|---|---|---|---|
| **Ethernet** | 1-2 | LAN | Frame-basierte Datenuebertragung im lokalen Netz |
| **STP/RSTP** | 2 | Schleifenvermeidung | Verhindert Loops in redundanten Switch-Topologien |
| **VLAN (802.1q)** | 2 | Segmentierung | Logische Trennung von Netzwerken auf einem Switch |
| **ARP** | 2 | Adressaufloesung | IP-Adresse → MAC-Adresse |
| **ICMP** | 3 | Steuerung | Fehlermeldungen und Diagnose (Ping) |
| **IP** | 3 | Vermittlung | Logische Adressierung und Routing |
| **TCP** | 4 | Transport | Zuverlaessige, verbindungsorientierte Uebertragung |
| **UDP** | 4 | Transport | Schnelle, verbindungslose Uebertragung |
| **DHCP** | 7 | Anwendung | Automatische IP-Konfiguration |
| **DNS** | 7 | Anwendung | Namensaufloesung (Domain → IP) |
| **HTTP/HTTPS** | 7 | Anwendung | Webseiten-Uebertragung |
| **FTP** | 7 | Anwendung | Dateiuebertragung |
| **SMTP/POP/IMAP** | 7 | Anwendung | E-Mail Versand und Empfang |
| **SSH** | 7 | Anwendung | Verschluesselter Fernzugriff (ersetzt Telnet) |

---

## TCP (Transmission Control Protocol)

**Schicht:** 4 (Transport) | **Verbindungsorientiert** | **Zuverlaessig**

### Eigenschaften
- Stellt eine **logische Verbindung** zwischen zwei Endpunkten her, bevor Daten uebertragen werden
- Garantiert die **korrekte Reihenfolge** der Datenpakete
- **Fehlererkennung**: Verlorene Pakete werden erneut gesendet
- **Flusskontrolle**: Passt Sendegeschwindigkeit an den Empfaenger an
- Datenströme werden in **Segmente** aufgeteilt und beim Empfaenger wieder zusammengesetzt

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
|Offset | Res.  |U|A|P|R|S|F|        Window-Groesse            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Pruefsumme            |        Urgent-Pointer         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Feld | Bits | Beschreibung |
|---|---|---|
| **Quell-Port** | 16 | Portnummer der sendenden Anwendung |
| **Ziel-Port** | 16 | Portnummer der empfangenden Anwendung |
| **Sequenznummer** | 32 | Nummeriert die gesendeten Bytes zur Reihenfolge-Kontrolle |
| **Acknowledgement-Nr.** | 32 | Bestaetigt empfangene Bytes (naechstes erwartetes Byte) |
| **Data Offset** | 4 | Laenge des TCP-Headers in 32-Bit-Bloecken |
| **Flags** | 6 | Steuerbits (siehe unten) |
| **Window-Groesse** | 16 | Groesse des Empfangspuffers (Flusskontrolle) |
| **Pruefsumme** | 16 | Fehlererkennung ueber Header und Daten |
| **Urgent-Pointer** | 16 | Zeigt auf dringend zu verarbeitende Daten |

### TCP-Flags

| Flag | Name | Bedeutung |
|---|---|---|
| **SYN** | Synchronize | Verbindungsaufbau einleiten |
| **ACK** | Acknowledge | Empfangsbestaetigung |
| **FIN** | Finish | Verbindungsabbau einleiten |
| **RST** | Reset | Verbindung sofort abbrechen |
| **PSH** | Push | Daten sofort an Anwendung weiterleiten |
| **URG** | Urgent | Dringende Daten (Urgent-Pointer gueltig) |

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

1. Client sendet **SYN** mit einer zufaelligen Sequenznummer
2. Server antwortet mit **SYN+ACK** (eigene Sequenznummer + Bestaetigung)
3. Client bestaetigt mit **ACK** → Verbindung ist aufgebaut

### Verbindungsabbau (4-Way-Handshake)

```
Client                          Server
  |  FIN  →                        |
  |<−  ACK                         |
  |                                |
  |                  ←  FIN        |
  |  ACK  →                        |
```

Beide Seiten muessen ihre Senderichtung einzeln beenden (FIN + ACK).

---

## UDP (User Datagram Protocol)

**Schicht:** 4 (Transport) | **Verbindungslos** | **Unzuverlaessig**

### Eigenschaften
- Kein Verbindungsaufbau noetig (kein Handshake)
- Keine Empfangsbestaetigung → Absender weiss nicht ob Paket ankam
- Keine Reihenfolge-Garantie
- Kein Retransmit bei Paketverlust
- **Vorteil**: Geringerer Overhead, schneller, weniger Latenz

### UDP-Header (8 Byte)

| Feld | Bits | Beschreibung |
|---|---|---|
| **Quell-Port** | 16 | Port des Senders |
| **Ziel-Port** | 16 | Port des Empfaengers |
| **Laenge** | 16 | Gesamtgroesse des UDP-Pakets in Byte |
| **Checksumme** | 16 | Fehlerpruefung (optional bei IPv4) |

### Einsatzgebiete
- **DNS**-Anfragen (schnelle Einzelanfragen)
- **DHCP** (IP-Konfiguration)
- **VoIP** und Video-Streaming (Echtzeitdaten)
- **Online-Gaming** (Latenz wichtiger als Zuverlaessigkeit)
- **TFTP** (Trivial File Transfer)

### Vergleich TCP vs. UDP

| Eigenschaft | TCP | UDP |
|---|---|---|
| Verbindung | verbindungsorientiert | verbindungslos |
| Zuverlaessigkeit | ja (ACK, Retransmit) | nein |
| Reihenfolge | garantiert | nicht garantiert |
| Geschwindigkeit | langsamer (Overhead) | schneller |
| Header-Groesse | mind. 20 Byte | 8 Byte |
| Flusskontrolle | ja | nein |
| Einsatz | Web, E-Mail, Dateitransfer | Streaming, DNS, Gaming |

---

## ICMP (Internet Control Message Protocol)

**Schicht:** 3 (Vermittlung, Teil von IP) | **Diagnose und Fehlermeldungen**

### Aufgaben
- Uebermittlung von **Statusinformationen und Fehlermeldungen** der Protokolle IP, TCP und UDP
- Rechner und Router koennen sich gegenseitig auf Probleme mit Datenpaketen hinweisen
- ICMP selbst ist unzuverlaessig: Gehen ICMP-Meldungen verloren, wird keine Fehlermeldung ausgeloest

### Wichtige ICMP-Nachrichtentypen

| Typ | Name | Beschreibung |
|---|---|---|
| 0 | **Echo Reply** | Antwort auf Ping |
| 3 | **Destination Unreachable** | Ziel nicht erreichbar (versch. Codes fuer Port/Host/Netz) |
| 5 | **Redirect** | Umleitung zu besserem Router |
| 8 | **Echo Request** | Ping-Anfrage |
| 11 | **Time Exceeded** | TTL abgelaufen (genutzt von Traceroute) |

### Praxistools
- **Ping**: Sendet Echo Request (Typ 8) → Empfaenger antwortet mit Echo Reply (Typ 0). Misst Erreichbarkeit und Antwortzeit (RTT)
- **Traceroute**: Nutzt TTL-Feld aus. Sendet Pakete mit TTL=1, 2, 3... Jeder Router auf dem Weg antwortet mit "Time Exceeded" (Typ 11). So wird die Route zum Ziel sichtbar

---

## ARP (Address Resolution Protocol)

**Schicht:** 2 (Sicherung) | **Adressaufloesung**

### Problem
Geraete in einem lokalen Netz kommunizieren ueber **MAC-Adressen** (Schicht 2). IP-Adressen (Schicht 3) muessen daher in MAC-Adressen aufgeloest werden.

### Funktionsweise

```
1. Host A will an 192.168.1.5 senden, kennt aber die MAC-Adresse nicht
2. Host A sendet ARP-Request als Broadcast (FF:FF:FF:FF:FF:FF):
   "Wer hat die IP 192.168.1.5? Antwort bitte an [meine MAC]"
3. ALLE Geraete im Netz empfangen den Broadcast
4. Nur Host B (192.168.1.5) antwortet mit ARP-Reply:
   "192.168.1.5 bin ich, meine MAC ist AA:BB:CC:DD:EE:FF"
5. Host A speichert das Ergebnis im ARP-Cache
```

### ARP-Cache
- Speichert bereits aufgeloeste IP→MAC Zuordnungen
- **Dynamische Eintraege**: werden automatisch erzeugt, laufen nach einer Zeit ab
- **Statische Eintraege**: manuell konfiguriert, bleiben dauerhaft
- Anzeige unter Windows: `arp -a` / unter Linux: `ip neigh`

### Bei Zielen ausserhalb des eigenen Subnetzes
- ARP loest die MAC-Adresse des **Default-Gateways** (Router) auf
- Der Router leitet das Paket dann weiter und fuehrt ggf. einen neuen ARP-Vorgang im Zielnetz durch

---

## DHCP (Dynamic Host Configuration Protocol)

**Schicht:** 7 (Anwendung) | **Automatische Netzwerkkonfiguration** | Port 67 (Server), 68 (Client)

### Aufgabe
Automatische Vergabe von IP-Adresse, Subnetzmaske, Standard-Gateway, DNS-Server an Geraete im Netzwerk.

### DORA-Prozess (Ablauf)

```
Client                          DHCP-Server
  |  1. DISCOVER (Broadcast)       |
  |------------------------------->|
  |  2. OFFER (IP-Angebot)         |
  |<-------------------------------|
  |  3. REQUEST (IP anfordern)     |
  |------------------------------->|
  |  4. ACK (Bestaetigung)         |
  |<-------------------------------|
```

1. **Discover**: Client sucht per Broadcast nach einem DHCP-Server
2. **Offer**: Server bietet eine freie IP-Adresse an
3. **Request**: Client akzeptiert das Angebot
4. **Acknowledge**: Server bestaetigt und vergibt die Adresse fuer eine bestimmte **Lease-Time**

### Lease-Time
- IP-Adresse wird nur fuer eine bestimmte Zeit vergeben
- Client muss vor Ablauf eine Verlaengerung anfragen
- Ermoeglicht Wiederverwendung von Adressen bei abgemeldeten Geraeten

---

## DNS (Domain Name System)

**Schicht:** 7 (Anwendung) | **Namensaufloesung** | Port 53 (UDP/TCP)

### Aufgabe
Uebersetzung von menschenlesbaren Domainnamen in IP-Adressen:
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
- **Autoritative Nameserver**: Kennen die tatsaechlichen IP-Adressen einer Domain

### Ablauf einer DNS-Anfrage

1. Client fragt den **lokalen DNS-Resolver** (meist vom ISP oder Router)
2. Falls nicht im Cache: Resolver fragt **Root-Server** → erhaelt Verweis auf TLD-Server
3. Resolver fragt **TLD-Server** → erhaelt Verweis auf autoritativen Nameserver
4. Resolver fragt **autoritativen Nameserver** → erhaelt die IP-Adresse
5. Ergebnis wird im Cache gespeichert (TTL-basiert)

### DNS-Record-Typen

| Typ | Beschreibung |
|---|---|
| **A** | IPv4-Adresse |
| **AAAA** | IPv6-Adresse |
| **CNAME** | Alias (Verweis auf anderen Domainnamen) |
| **MX** | Mailserver fuer die Domain |
| **NS** | Autoritativer Nameserver |
| **PTR** | Reverse-DNS (IP → Name) |
| **TXT** | Freitext (z.B. SPF-Records fuer E-Mail) |

---

## HTTP/HTTPS (Hypertext Transfer Protocol)

**Schicht:** 7 (Anwendung) | **Webkommunikation** | Port 80 (HTTP), 443 (HTTPS)

### Funktionsweise
- Client (Browser) sendet **Request** an Server
- Server verarbeitet Anfrage und sendet **Response** zurueck
- **Zustandslos**: Jede Anfrage ist unabhaengig (Cookies/Sessions fuer Zustandsverwaltung)
- Basiert auf **TCP** (zuverlaessige Uebertragung)

### HTTP-Methoden

| Methode | Beschreibung |
|---|---|
| **GET** | Daten vom Server anfordern (z.B. Webseite laden) |
| **POST** | Daten an Server senden (z.B. Formular absenden) |
| **PUT** | Ressource vollstaendig ersetzen/aktualisieren |
| **DELETE** | Ressource loeschen |
| **PATCH** | Ressource teilweise aendern |
| **HEAD** | Wie GET, aber nur Header zurueck (ohne Body) |

### HTTP-Request (Aufbau)

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

- **Methode + Pfad + Version** in der ersten Zeile
- Danach folgen **Header** (Metadaten)
- Optional ein **Body** (z.B. bei POST mit Formulardaten)

### HTTP-Response (Aufbau)

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

- **Version + Statuscode + Statustext** in der ersten Zeile
- Header mit Metadaten (Content-Type, Content-Length etc.)
- **Body** mit den eigentlichen Daten

### Statuscodes

| Code | Kategorie | Beispiele |
|---|---|---|
| **1xx** | Information | 100 Continue |
| **2xx** | Erfolg | 200 OK, 201 Created |
| **3xx** | Umleitung | 301 Moved Permanently, 302 Found |
| **4xx** | Client-Fehler | 400 Bad Request, 403 Forbidden, 404 Not Found |
| **5xx** | Server-Fehler | 500 Internal Server Error, 503 Service Unavailable |

### HTTPS und TLS

**HTTPS** = HTTP + **TLS** (Transport Layer Security) Verschluesselung

```
Client                          Server
  |  1. ClientHello              |
  |  (unterstuetzte Cipher)      |
  |------------------------------->|
  |  2. ServerHello + Zertifikat |
  |  (gewaehlte Cipher)          |
  |<-------------------------------|
  |  3. Client prueft Zertifikat |
  |  Schluesselaustausch          |
  |------------------------------->|
  |  4. Verschluesselte           |
  |  Verbindung steht             |
  |<==============================>|
```

- Server sendet **Zertifikat** (von einer CA signiert) zur Identitaetspruefung
- **Asymmetrische Verschluesselung** fuer den Schluesselaustausch
- **Symmetrische Verschluesselung** fuer die eigentliche Datenuebertragung (schneller)
- Schuetzt vor Abhoeren, Manipulation und Man-in-the-Middle-Angriffen

---

## FTP (File Transfer Protocol)

**Schicht:** 7 (Anwendung) | **Dateiuebertragung** | Port 21 (Steuerung), 20 (Daten)

### Eigenschaften
- Verwendet **zwei getrennte Verbindungen**: Steuerkanal und Datenkanal
- Basiert auf TCP
- Uebertraegt Daten **unverschluesselt** (Benutzername, Passwort, Dateien im Klartext)
- Unterstuetzt Hoch- und Herunterladen von Dateien, Verzeichnisnavigation

### Steuerkanal vs. Datenkanal

| Kanal | Port | Aufgabe |
|---|---|---|
| **Steuerkanal** | 21 | Befehle und Antworten (Login, cd, ls, get, put) |
| **Datenkanal** | 20 (aktiv) / dynamisch (passiv) | Eigentliche Dateiuebertragung |

### Aktiver vs. Passiver Modus

**Aktiver Modus:**
```
Client                          Server
  | 1. Steuerverbindung (Port 21) |
  |------------------------------->|
  | 2. Client nennt seinen Port    |
  |------------------------------->|
  | 3. Server verbindet sich       |
  |    von Port 20 zum Client      |
  |<-------------------------------|
```
- Server baut die Datenverbindung **zum Client** auf
- Problem: Firewall des Clients blockiert oft eingehende Verbindungen

**Passiver Modus:**
```
Client                          Server
  | 1. Steuerverbindung (Port 21) |
  |------------------------------->|
  | 2. PASV-Befehl                 |
  |------------------------------->|
  | 3. Server nennt Port           |
  |<-------------------------------|
  | 4. Client verbindet sich       |
  |    zum genannten Port           |
  |------------------------------->|
```
- Client baut **beide** Verbindungen auf → firewall-freundlicher
- Heute Standard in den meisten FTP-Clients

### Sichere Alternativen
- **FTPS**: FTP ueber TLS (verschluesselt, Ports 989/990)
- **SFTP**: SSH File Transfer Protocol (laeuft ueber SSH, Port 22)

---

## SMTP, POP3 und IMAP (E-Mail-Protokolle)

**Schicht:** 7 (Anwendung) | **E-Mail-Kommunikation**

### Ueberblick: E-Mail-Weg

```
Absender                                                    Empfaenger
[Mail-Client] --SMTP--> [Mail-Server] --SMTP--> [Mail-Server] <--POP3/IMAP-- [Mail-Client]
  (Outlook)              (Absender)              (Empfaenger)                  (Thunderbird)
```

- **SMTP** wird zum **Senden** verwendet (Client→Server und Server→Server)
- **POP3 oder IMAP** wird zum **Abrufen** verwendet (Server→Client)

### SMTP (Simple Mail Transfer Protocol)

| Eigenschaft | Wert |
|---|---|
| **Port** | 25 (unverschluesselt), 587 (STARTTLS), 465 (SSL/TLS) |
| **Aufgabe** | E-Mail-Versand und -Weiterleitung |
| **Protokoll** | TCP |

- Textbasiertes Protokoll (Befehle: HELO, MAIL FROM, RCPT TO, DATA, QUIT)
- Zustaendig fuer den **Transport** der E-Mail, nicht fuer das Abrufen

### POP3 (Post Office Protocol v3)

| Eigenschaft | Wert |
|---|---|
| **Port** | 110 (unverschluesselt), 995 (SSL/TLS) |
| **Aufgabe** | E-Mail-Abruf vom Server |

- Laedt E-Mails herunter und **loescht sie vom Server** (Standardverhalten)
- E-Mails werden **lokal gespeichert** → nur auf einem Geraet verfuegbar
- Einfach, geringer Speicherbedarf auf dem Server

### IMAP (Internet Message Access Protocol)

| Eigenschaft | Wert |
|---|---|
| **Port** | 143 (unverschluesselt), 993 (SSL/TLS) |
| **Aufgabe** | E-Mail-Verwaltung auf dem Server |

- E-Mails **bleiben auf dem Server** → von mehreren Geraeten abrufbar
- Unterstuetzt Ordnerstruktur, Suchfunktion, Flags (gelesen/ungelesen)
- Benoetigt mehr Serverspeicher

### Vergleich POP3 vs. IMAP

| Eigenschaft | POP3 | IMAP |
|---|---|---|
| Speicherort | Lokal (Client) | Server |
| Mehrere Geraete | Nein (nur eins) | Ja |
| Ordner/Struktur | Nein | Ja |
| Offline-Zugriff | Ja (nach Download) | Eingeschraenkt |
| Serverspeicher | Gering | Hoch |
| Synchronisation | Keine | Alle Geraete synchron |

---

## SSH (Secure Shell)

**Schicht:** 7 (Anwendung) | **Verschluesselter Fernzugriff** | Port 22

### Aufgabe
Sichere, verschluesselte Verbindung zu einem entfernten Rechner ueber ein unsicheres Netzwerk.

### Eigenschaften
- Vollstaendig **verschluesselte** Kommunikation (Authentifizierung + Daten)
- Ersetzt das unsichere **Telnet** (Port 23), das alles im Klartext uebertraegt
- Basiert auf TCP

### Authentifizierungsmethoden

| Methode | Beschreibung |
|---|---|
| **Passwort** | Benutzername + Passwort (verschluesselt uebertragen) |
| **Public-Key** | Schluesselpaar: privater Key beim Client, oeffentlicher Key auf dem Server. Sicherer als Passwort |

### SSH vs. Telnet

| Eigenschaft | SSH | Telnet |
|---|---|---|
| Port | 22 | 23 |
| Verschluesselung | Ja (komplett) | Nein (Klartext) |
| Sicherheit | Hoch | Keine |
| Authentifizierung | Passwort oder Key | Nur Passwort |
| Einsatz heute | Standard | Veraltet / nur in isolierten Netzen |

### Einsatzgebiete
- **Remote-Administration**: Kommandozeile auf Servern, Routern, Switches
- **SCP** (Secure Copy): Dateikopie ueber SSH
- **SFTP**: Dateiuebertragung ueber SSH (sicherer FTP-Ersatz)
- **SSH-Tunnel / Port-Forwarding**: Verschluesselte Weiterleitung von Ports

---

## Wichtige Portnummern

| Port | Protokoll | Dienst |
|---|---|---|
| 20/21 | TCP | FTP (Daten/Steuerung) |
| 22 | TCP | SSH (sichere Shell) |
| 23 | TCP | Telnet (unsicher) |
| 25 | TCP | SMTP (E-Mail-Versand) |
| 53 | UDP/TCP | DNS |
| 67/68 | UDP | DHCP (Server/Client) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 (E-Mail-Abruf) |
| 143 | TCP | IMAP (E-Mail-Abruf) |
| 443 | TCP | HTTPS (verschluesselt) |
| 3389 | TCP | RDP (Remote Desktop) |

**Portbereiche:**
- 0-1023: **Well-Known Ports** (reserviert fuer Standarddienste)
- 1024-49151: **Registered Ports** (registrierte Anwendungen)
- 49152-65535: **Dynamic/Private Ports** (temporaer, frei verwendbar)

---

## Ethernet-Frame

**Schicht:** 2 (Sicherung) | **Rahmenformat fuer LAN-Kommunikation**

Ethernet-Frames sind die Datenpakete auf Schicht 2. Jedes Frame hat folgenden Aufbau:

```
+----------+-----+----------+----------+--------+--------+-----+
| Praeambel| SFD | Ziel-MAC | Quell-MAC|Typ/Len | Daten  | FCS |
|  7 Byte  |1 B  |  6 Byte  |  6 Byte  | 2 Byte |46-1500B|4 B  |
+----------+-----+----------+----------+--------+--------+-----+
```

| Feld | Groesse | Beschreibung |
|---|---|---|
| **Praeambel** | 7 Byte | Synchronisationsmuster (101010...) |
| **SFD** (Start Frame Delimiter) | 1 Byte | Markiert den Beginn des Frames |
| **Ziel-MAC** | 6 Byte | MAC-Adresse des Empfaengers |
| **Quell-MAC** | 6 Byte | MAC-Adresse des Senders |
| **Typ/Laenge** | 2 Byte | Ethernet II: Protokolltyp (z.B. 0x0800=IPv4, 0x0806=ARP). 802.3: Laengenangabe |
| **Daten** | 46-1500 Byte | Nutzdaten (Payload). Min. 46 Byte (ggf. mit Padding aufgefuellt) |
| **FCS** (Frame Check Sequence) | 4 Byte | CRC-32 Pruefsumme zur Fehlererkennung |

### MAC-Adresse
- 48 Bit (6 Byte), geschrieben als `AA:BB:CC:DD:EE:FF`
- Erste 3 Byte: **OUI** (Herstellerkennung, z.B. Intel, Realtek)
- Letzte 3 Byte: Geraetekennung (vom Hersteller vergeben)
- `FF:FF:FF:FF:FF:FF` = Broadcast (an alle Geraete im LAN)
- Weltweit einzigartig, fest in der Netzwerkkarte gespeichert

### Frame-Groessen
- **Minimum:** 64 Byte (ohne Praeambel/SFD)
- **Maximum:** 1518 Byte (ohne Praeambel/SFD), 1522 Byte mit VLAN-Tag
- **MTU** (Maximum Transmission Unit): 1500 Byte Nutzdaten

---

## STP (Spanning Tree Protocol) - IEEE 802.1d

**Schicht:** 2 (Sicherung) | **Schleifenvermeidung in geswitchten Netzen**

### Problem: Switching Loops
Wenn zwischen zwei Switches mehrere physische Verbindungen existieren (Redundanz), entstehen **Schleifen**:
- Broadcast-Frames werden endlos im Kreis geschickt (**Broadcast-Storm**)
- MAC-Adresstabellen werden verfaelscht (MAC-Flapping)
- Das Netzwerk wird komplett lahmgelegt

### Loesung: Spanning Tree
STP erstellt aus dem physischen Netzwerk einen **logischen Baum** (Tree), in dem zu jedem Ziel nur **ein einziger Pfad** existiert. Redundante Verbindungen werden **blockiert**, aber bei Ausfall automatisch aktiviert.

### Ablauf

**1. Root Bridge waehlen**
- Alle Switches tauschen **BPDUs** (Bridge Protocol Data Units) alle 2 Sekunden aus
- Jeder Switch hat eine **Bridge ID** = Prioritaet (Standard: 32768) + MAC-Adresse
- Der Switch mit der **niedrigsten Bridge ID** wird zur **Root Bridge**
- Prioritaet manuell konfigurierbar (in 4096er-Schritten)

**2. Pfadkosten berechnen**
Jeder Port hat Kosten, die von der Bandbreite abhaengen:

| Bandbreite | Pfadkosten |
|---|---|
| 10 Mbit/s | 100 |
| 100 Mbit/s | 19 |
| 1 Gbit/s | 4 |
| 10 Gbit/s | 2 |

**3. Portrollen zuweisen**

| Portrolle | Beschreibung |
|---|---|
| **Root Port** | Port mit den geringsten Pfadkosten zur Root Bridge. Jeder Non-Root-Switch hat genau einen |
| **Designated Port** | Port, der ein Netzwerksegment zur Root Bridge hin bedient. Leitet Daten weiter |
| **Blocked Port** | Redundanter Port, der keine Daten weiterleitet. Empfaengt nur BPDUs |

### Portzustaende (STP)

| Zustand | Lernt MAC? | Leitet Daten? | Dauer |
|---|---|---|---|
| **Blocking** | Nein | Nein | - |
| **Listening** | Nein | Nein | 15 Sek. |
| **Learning** | Ja | Nein | 15 Sek. |
| **Forwarding** | Ja | Ja | - |
| **Disabled** | Nein | Nein | - |

### Konvergenzzeit
- Bei Topologie-Aenderung dauert die Neuberechnung bis zu **30-50 Sekunden**
- Waehrend dieser Zeit kein Datenverkehr moeglich

### RSTP (Rapid Spanning Tree) - IEEE 802.1w
- Abwaertskompatibel zu STP
- Konvergenzzeit unter **1 Sekunde**
- Das Netz arbeitet mit der bestehenden Struktur weiter, waehrend der neue Baum berechnet wird
- Neue Portrollen: **Alternate Port** (Backup fuer Root Port), **Backup Port** (Backup fuer Designated Port)

---

## VLAN (Virtual Local Area Network) - IEEE 802.1q

**Schicht:** 2 (Sicherung) | **Logische Netzwerktrennung**

### Was ist ein VLAN?
Ein VLAN teilt ein physisches Netzwerk in mehrere **logische Netze** auf. Geraete im selben VLAN koennen kommunizieren, Geraete in verschiedenen VLANs **nicht** (ohne Router).

### Vorteile
- **Broadcast-Reduktion**: Broadcasts bleiben innerhalb des VLANs
- **Sicherheit**: Trennung von Abteilungen/Bereichen ohne separate Hardware
- **Flexibilitaet**: Geraete koennen unabhaengig vom physischen Standort gruppiert werden
- **Performance**: Weniger unnoetige Broadcasts = weniger Last

### Portbasiertes VLAN (untagged)
- Switch-Ports werden einem VLAN zugeordnet
- Einfachste Form: Port 1-12 = VLAN 10, Port 13-24 = VLAN 20
- Frames werden ohne VLAN-Tag uebertragen (**Access Port**)

### Tagged VLAN (IEEE 802.1q)
Das Ethernet-Frame wird um einen **4-Byte VLAN-Tag** erweitert:

```
+----------+----------+----------+----------+--------+-----+
| Ziel-MAC | Quell-MAC| VLAN-Tag | Typ/Len  | Daten  | FCS |
|  6 Byte  |  6 Byte  |  4 Byte  |  2 Byte  |        |4 B  |
+----------+----------+----------+----------+--------+-----+
                       |
          +------------+------------+
          | TPID (2B)  | TCI (2B)   |
          | 0x8100     | PCP|DEI|VID|
          +------------+---+---+----+
                        3b  1b  12b
```

- **TPID** (Tag Protocol Identifier): `0x8100` kennzeichnet einen getaggten Frame
- **VID** (VLAN Identifier): 12 Bit → **4096 moegliche VLANs** (0 und 4095 reserviert)
- **PCP** (Priority Code Point): 3 Bit fuer QoS-Prioritaet (0-7)

### Trunk Port
- Verbindung zwischen Switches, die **mehrere VLANs** transportiert
- Frames werden mit VLAN-Tag versehen (tagged)
- Ein **Native VLAN** kann untagged ueber den Trunk laufen

### Inter-VLAN-Routing
- Kommunikation zwischen VLANs erfordert einen **Layer-3-Switch** oder Router
- **Router-on-a-Stick**: Ein Router mit Subinterfaces fuer jedes VLAN an einem Trunk-Port

### Beispiel

```
Switch 1                      Switch 2
+--------+    Trunk (tagged)  +--------+
| VLAN 10|====================| VLAN 10|  (Buchhaltung)
| VLAN 20|====================| VLAN 20|  (Entwicklung)
| VLAN 30|====================| VLAN 30|  (Gaeste)
+--------+                    +--------+
```

---

## Routing

**Schicht:** 3 (Vermittlung) | **Wegfindung fuer IP-Pakete**

### Was ist Routing?
Routing ist der Prozess, bei dem ein Router entscheidet, ueber welchen Ausgangsport (Interface) ein eingehendes IP-Paket weitergeleitet wird, um sein Ziel zu erreichen.

### Routing-Tabelle
Jeder Router und jeder Host besitzt eine **Routing-Tabelle**, die festlegt, wohin Pakete fuer bestimmte Zielnetze gesendet werden:

| Zielnetz | Subnetzmaske | Next Hop | Interface | Metrik |
|---|---|---|---|---|
| 192.168.1.0 | 255.255.255.0 | direkt verbunden | eth0 | 0 |
| 10.0.0.0 | 255.0.0.0 | 192.168.1.1 | eth0 | 1 |
| 0.0.0.0 | 0.0.0.0 | 192.168.1.254 | eth0 | - |

- **Zielnetz**: Das Netzwerk, das erreicht werden soll
- **Next Hop**: Die IP-Adresse des naechsten Routers auf dem Weg
- **Metrik**: "Kosten" des Weges (Hop-Count, Bandbreite etc.)
- **Default Route** (0.0.0.0/0): Wird genutzt, wenn kein spezifischer Eintrag passt → Paket geht ans **Default Gateway**

### Default Gateway
- Der Router, an den ein Host alle Pakete sendet, die **nicht im eigenen Subnetz** liegen
- Wird per DHCP oder manuell konfiguriert
- Ohne Default Gateway kann ein Host nur im lokalen Netz kommunizieren

### Routing-Entscheidung (vereinfacht)

```
Paket kommt an (Ziel-IP: 10.5.3.7)
         |
         v
Ist das Ziel im eigenen Subnetz?
   Ja → direkt zustellen (via ARP)
   Nein → Routing-Tabelle pruefen
              |
              v
     Spezifischer Eintrag fuer 10.x.x.x?
        Ja → an Next Hop weiterleiten
        Nein → an Default Gateway senden
```

### Statisches vs. Dynamisches Routing

| Eigenschaft | Statisch | Dynamisch |
|---|---|---|
| Konfiguration | Manuell durch Admin | Automatisch durch Protokoll |
| Anpassung | Manuell bei Aenderungen | Automatisch bei Topologieaenderungen |
| Aufwand | Gering bei kleinen Netzen | Gering bei grossen Netzen |
| Fehleranfaelligkeit | Hoch (vergessene Routen) | Gering (selbstheilend) |
| Ressourcen | Kaum CPU/RAM | Mehr CPU/RAM fuer Berechnung |
| Einsatz | Kleine Netze, Sonderfaelle | Grosse, komplexe Netze |

### Dynamische Routing-Protokolle (Ueberblick)

| Protokoll | Typ | Metrik | Einsatz |
|---|---|---|---|
| **RIP** | Distance Vector | Hop Count (max. 15) | Kleine Netze |
| **OSPF** | Link State | Kosten (Bandbreite) | Grosse Unternehmensnetze |
| **BGP** | Path Vector | AS-Pfad | Internet (zwischen ISPs) |

---

## IPv6 (Internet Protocol Version 6)

**Schicht:** 3 (Vermittlung) | **Nachfolger von IPv4**

### Warum IPv6?
- IPv4 hat nur ca. **4,3 Milliarden** Adressen (2^32) → Adressraum erschoepft
- IPv6 bietet **340 Sextillionen** Adressen (2^128) → praktisch unerschoepflich
- Vereinfachter Header, eingebaute Sicherheit (IPsec), kein NAT noetig

### Adressformat
- **128 Bit**, dargestellt als 8 Gruppen zu je 4 Hexadezimalziffern
- Gruppen durch **Doppelpunkte** getrennt
- Beispiel: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

### Kuerzungsregeln
1. **Fuehrende Nullen** in einer Gruppe weglassen: `0db8` → `db8`
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
| **Anycast** | An den naechsten aus einer Gruppe | Routing-optimiert |
| **Link-Local** | Nur im lokalen Netzwerk gueltig | `fe80::/10` |
| **Global Unicast** | Weltweit routbar (wie oeffentliche IPv4) | `2000::/3` |
| **Loopback** | Eigenes Geraet | `::1` |

### Vergleich IPv4 vs. IPv6

| Eigenschaft | IPv4 | IPv6 |
|---|---|---|
| Adresslaenge | 32 Bit | 128 Bit |
| Notation | Dezimal (192.168.1.1) | Hexadezimal (2001:db8::1) |
| Adressanzahl | ~4,3 Milliarden | ~340 Sextillionen |
| Header-Groesse | 20-60 Byte (variabel) | 40 Byte (fix) |
| NAT | Haeufig noetig | Nicht noetig |
| Broadcast | Ja | Nein (ersetzt durch Multicast) |
| IPsec | Optional | Integriert |
| Autokonfiguration | DHCP | SLAAC + DHCPv6 |

### Uebergangsmechanismen
- **Dual-Stack**: Geraet spricht IPv4 und IPv6 gleichzeitig
- **Tunneling**: IPv6-Pakete werden in IPv4-Pakete verpackt (z.B. 6to4)
- **Translation**: NAT64 uebersetzt zwischen IPv4 und IPv6

---

## NAT/PAT (Network Address Translation)

**Schicht:** 3 (Vermittlung) | **Adressuebersetzung**

### Problem
Private IP-Adressen (10.x.x.x, 172.16-31.x.x, 192.168.x.x) sind im Internet **nicht routbar**. Trotzdem muessen Geraete mit privaten IPs ins Internet.

### Loesung: NAT
Der Router uebersetzt private IP-Adressen in eine oder mehrere oeffentliche IP-Adressen.

### Arten von NAT

**Static NAT (1:1)**
- Eine private IP wird fest einer oeffentlichen IP zugeordnet
- Einsatz: Server, die von aussen erreichbar sein muessen

**Dynamic NAT (n:m)**
- Private IPs werden dynamisch aus einem Pool oeffentlicher IPs zugewiesen
- Wenn der Pool leer ist, koennen keine weiteren Verbindungen aufgebaut werden

**PAT / NAT Overloading (n:1)** ← Am haeufigsten
- Viele private IPs teilen sich **eine** oeffentliche IP
- Unterscheidung ueber **Portnummern**

### PAT-Ablauf (Beispiel)

```
Internes Netz                    Router (NAT)              Internet
192.168.1.10:3000  ──→  203.0.113.5:40001  ──→  93.184.216.34:80
192.168.1.20:3000  ──→  203.0.113.5:40002  ──→  93.184.216.34:80
192.168.1.30:4500  ──→  203.0.113.5:40003  ──→  93.184.216.34:80
```

### NAT-Tabelle

Der Router speichert die Zuordnungen:

| Interne Adresse | Interner Port | Externe Adresse | Externer Port |
|---|---|---|---|
| 192.168.1.10 | 3000 | 203.0.113.5 | 40001 |
| 192.168.1.20 | 3000 | 203.0.113.5 | 40002 |
| 192.168.1.30 | 4500 | 203.0.113.5 | 40003 |

Antworten werden anhand der Tabelle zurueck an den richtigen internen Host geleitet.

### Port Forwarding
- Ermoeglicht Zugriff von **aussen auf interne Server**
- Router leitet eingehende Verbindungen auf einem bestimmten Port an eine interne IP weiter
- Beispiel: Port 80 von aussen → 192.168.1.100:80 intern (Webserver)

Siehe auch: [[IPV4]] fuer weitere Details zu NAT und CIDR.

---

## Kapselung (Encapsulation)

Beim Senden durchlaufen Daten die Schichten von oben nach unten. Jede Schicht fuegt ihren eigenen Header hinzu:

```
Anwendungsschicht:  [Daten]
Transportschicht:   [TCP/UDP-Header][Daten]           → Segment
Vermittlungsschicht:[IP-Header][TCP-Header][Daten]    → Paket
Sicherungsschicht:  [Frame-H][IP-H][TCP-H][Daten][FCS]→ Frame
Bituebertr.:         01101001011010...                 → Bits
```

Beim Empfaenger wird der Prozess umgekehrt: Jede Schicht entfernt ihren Header (**Dekapselung**).

## Siehe auch
- [[IPV4]]
- [[IsoOsi]]
- [[IP-Adressierung und Subnetting]]
- [[Switch]]
- [[AccessPoint]]
- [[WIFI IEEE 802.11]]
- [[Netzwerktechnik]]
- [[DVT Index]]
