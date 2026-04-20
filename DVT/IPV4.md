---
fach: DVT
thema: IPV4
tags: [netzwerk, ipv4]
datum: 2024-04-18
typ: notiz
---

## Definition
- **IPv4** = Internet Protocol Version 4
- Protokoll zur eindeutigen Adressierung von Geräten in einem Netzwerk
- Grundlage der Internetkommunikation seit den 1980er Jahren

## Aufbau einer IPv4-Adresse
- Besteht aus **32 Bit**, aufgeteilt in 4 Oktette (je 8 Bit)
- Schreibweise: dezimal, durch Punkte getrennt → z. B. `192.168.1.1`
- Jedes Oktett kann Werte von **0 bis 255** annehmen
- Adresse besteht aus zwei Teilen: **Netzanteil** und **Hostanteil** (durch Subnetzmaske getrennt)

## Adressklassen (klassisch)
| Klasse | Bereich | Einsatz |
|---|---|---|
| A | 1.0.0.0 – 126.255.255.255 | Sehr große Netze |
| B | 128.0.0.0 – 191.255.255.255 | Mittelgroße Netze |
| C | 192.0.0.0 – 223.255.255.255 | Kleine Netze |

## Private IP-Adressbereiche
- `10.0.0.0 – 10.255.255.255` (Klasse A)
- `172.16.0.0 – 172.31.255.255` (Klasse B)
- `192.168.0.0 – 192.168.255.255` (Klasse C)
- Private Adressen sind nicht im öffentlichen Internet geroutet → werden mit **NAT** übersetzt

## Subnetzmaske
- Gibt an, welcher Teil der IP-Adresse zum Netz und welcher zum Host gehört
- Beispiel: `255.255.255.0` entspricht `/24` in CIDR-Notation
- Netzadresse: erstes Gerät im Subnetz (nicht nutzbar)
- Broadcastadresse: letztes Gerät im Subnetz (nicht nutzbar)

## Besondere Adressen
- `127.0.0.1` = Loopback-Adresse ("localhost") – verweist auf das eigene Gerät
- `0.0.0.0` = Standardroute / nicht zugewiesen
- `255.255.255.255` = begrenzte Broadcast-Adresse

## IPv4-Header

Jedes IPv4-Paket beginnt mit einem Header (mindestens **20 Byte**). Die maximale Paketgroesse betraegt 65.535 Byte. Der Header ist in 32-Bit-Bloecke organisiert.

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |    ToS        |         Paketlaenge           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Kennung               |Flags|    Fragment-Offset      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    TTL        |  Protokoll    |     Header-Checksumme         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Quell-IP-Adresse                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Ziel-IP-Adresse                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Optionen (optional)              | Padding |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Felder im Detail

| Feld                             | Bits  | Beschreibung                                                                                                                                  |
| -------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Version**                      | 4     | IP-Protokollversion (`4` fuer IPv4)                                                                                                           |
| **IHL** (Internet Header Length) | 4     | Laenge des Headers als Vielfaches von 32 Bit. Min. 5 (=20 Byte), Max. 15 (=60 Byte)                                                           |
| **ToS** (Type of Service)        | 8     | Dienstequalitaet (QoS). 3 Bit Prioritaet + 5 Bit Uebertragungseigenschaften                                                                   |
| **Paketlaenge**                  | 16    | Gesamtlaenge des IP-Pakets in Byte (Header + Nutzdaten). Max. 65.535 Byte                                                                     |
| **Kennung** (Identification)     | 16    | Eindeutige, fortlaufende Nummer zur Identifikation. Wird bei Fragmentierung benoetigt um Fragmente zusammenzusetzen                           |
| **Flags**                        | 3     | Fragmentierungskontrolle: Bit 1 = reserviert (0), Bit 2 = **DF** (Don't Fragment), Bit 3 = **MF** (More Fragments = weitere Fragmente folgen) |
| **Fragment-Offset**              | 13    | Position des Fragments im urspruenglichen Paket (in 8-Byte-Einheiten)                                                                         |
| **TTL** (Time to Live)           | 8     | Lebensdauer: Jeder Router zieht mindestens 1 ab. Bei 0 wird das Paket verworfen. Typisch: 64 oder 128. Verhindert endloses Kreisen im Netz    |
| **Protokoll**                    | 8     | Uebergeordnetes Protokoll: `1` = ICMP, `6` = TCP, `17` = UDP                                                                                  |
| **Header-Checksumme**            | 16    | Pruefsumme ueber den Header. Jeder Router prueft und berechnet neu (da TTL sich aendert)                                                      |
| **Quell-IP-Adresse**             | 32    | IP-Adresse des Absenders                                                                                                                      |
| **Ziel-IP-Adresse**              | 32    | IP-Adresse des Empfaengers (oder Multicast-Adresse)                                                                                           |
| **Optionen**                     | 0-320 | Optional: Routing-, Debugging-, Sicherheitsinformationen. Mit Nullen aufgefuellt (Padding) auf 32-Bit-Grenze                                  |

### Fragmentierung

Wenn ein IP-Paket groesser ist als die **MTU** (Maximum Transmission Unit) eines Netzwerksegments (Ethernet: 1500 Byte), wird es fragmentiert:
- Jedes Fragment bekommt die gleiche **Kennung**
- Der **Fragment-Offset** gibt die Position im Originalpaket an
- Das **MF-Flag** zeigt an, ob weitere Fragmente folgen
- Erst der Empfaenger setzt die Fragmente wieder zusammen

## NAT (Network Address Translation)

- Uebersetzt private IP-Adressen in oeffentliche und umgekehrt
- Ermoeglicht mehreren Geraeten mit privaten IPs den Zugang zum Internet ueber eine oeffentliche IP
- Router merkt sich in einer **NAT-Tabelle**, welcher interne Host welche Verbindung hat
- **PAT** (Port Address Translation): Unterscheidung ueber Portnummern

## CIDR (Classless Inter-Domain Routing)

- Ersetzt das starre Klassensystem (A/B/C) durch flexible Praefixlaengen
- Notation: `192.168.1.0/24` (die 24 gibt die Anzahl der Netzbits an)
- Ermoeglicht effizientere Nutzung des Adressraums
- Beispiel: `/25` = 128 Adressen, `/26` = 64 Adressen, `/27` = 32 Adressen

| CIDR | Subnetzmaske | Hosts |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

## Grenzen von IPv4
- Nur ca. **4,3 Milliarden** moegliche Adressen (2^32)
- Adressraum ist erschoepft → Loesung: **IPv6** mit 128-Bit-Adressen
- Uebergangsloesungen: NAT, CIDR, Dual-Stack, Tunneling

## Siehe auch
- [[IP-Adressierung und Subnetting]]
- [[Netzwerkprotokolle]]
- [[IsoOsi]]
- [[Netzwerktechnik]]
- [[DVT Index]]
