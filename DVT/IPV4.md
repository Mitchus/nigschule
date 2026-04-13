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

## Grenzen von IPv4
- Nur ca. **4,3 Milliarden** mögliche Adressen (2^32)
- Adressraum ist erschöpft → Lösung: **IPv6** mit 128-Bit-Adressen
- Übergangslösungen: NAT (Network Address Translation), CIDR

## Siehe auch
- [[IP-Adressierung und Subnetting]]
- [[Netzwerktechnik]]
- [[DVT Index]]
