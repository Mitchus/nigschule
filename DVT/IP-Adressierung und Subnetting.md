|              | IPV4              | IPV6                |     |
| ------------ | ----------------- | ------------------- | --- |
| Schreibweise | Dezimal           | Hexa                |     |
| Notation     | Punkt-Notation    | Doppelpunktnotation |     |
| Aufbau       | 32 bit in 4 bytes | 128bit 16byte       |     |
| Größe        | 2³²               | 2¹²⁸                |     |

Bereich von 0.0.0.0 bis 255.255.255.255 (Broadcast)
![[Pasted image 20240521095704.png]]
![[Pasted image 20240517112123.png]]

1. 0.0.0.0 bis 127.0.0.0
2. 128-191.255.0.0
3. 192-223.255.255.0
4. 255.0.0.0
5. 255.255.0.0
6. 255.255.255.0
7. 10.0.0.0 | 172.16.255.255 - 172.31.255.255 | 192.168.255.255
8.  2⁸ = 256 Hosts -2 | 2²⁴ =16,777,216
9. 65536 2¹⁶
10.  256 Netzwerke
### Aufteilen von Netze in Subnetze 
![[Pasted image 20240517114058.png]]
80.245.65.0/24" das Netz von 80.245.65.0 bis 80.245.65.255
![[Pasted image 20240517113630.png]]

Subnetting
192.168.0.1
11000000.10101000.00000000.00000001
Maske:
255.255.255.0
11111111.11111111.11111111.00000000

4 Neue Subnetze = 2 Bits
11111111.11111111.11111111.11000000
255.255.255.192
neue Hosts pro Subnetzwerk= 2⁶

| Ip             | Subnetzmaske    | Netzwerkadresse | Geräteteil | Broadcast | Default Gateway | max Ips |
| -------------- | --------------- | --------------- | ---------- | --------- | --------------- | ------- |
| 192.168.213.15 | 255.255.255.192 | 192.168.213.0   |            |           | 192.168.213.1   |         |
| 172.16.5.254   | 255.255.255.0   |                 |            |           |                 |         |
| 172.254.13.8   | 255.255.248.0   |                 |            |           |                 |         |
| 10.38.133.5    | 255.255.0.0     |                 |            |           |                 |         |
| 10.0.0.15      | 255.0.0.0       |                 |            |           |                 |         |
1.
11000000.10101000.11010101.11000000
0 . 0. 0. 01000000

213.148.129.30
11010101 10010100 10000001 00011110

255.255.224.0(IPv4)  
11111111.11111111.11100000.00000000
217.169.4.44(IPv4)
11011001.10101001.00000100.00101100
217.169.30.254(IPv4)  
11011001.10101001.00011110.11111110
217.169.32.1(IPv4)  
11011001.10101001.00100000.00000001


11000000.10101000.00000101.0000|0000

1.     **Nennen** Sie die drei Adressierungsverfahren und **beschreiben**, wie diese sich unterscheiden.
Unicast Einer Broadcast Alle MultiCast Mehrere

2.     Folgend ist eine IP-Adresse dargestellt. **Beschriften** Sie an dieser die folgenden Begriffe:        _Hostanteil, Netzanteil, Oktett, 32 Bit, Subnetzmaske, CIDR-Notation_

172.10.77.2 / 16
Netz  | Host
255.255.0.0

3.     Eine IPv4-Adresse unterteilt sich in einen Netzanteil und eine Hostanteil. **Beschreiben** Sie, wofür wir diese beiden Bereiche verwenden.
Netz Anteil beschreibt in welchem Netzwerk, Host Anteil welcher Host in diesem Netzwerk
4.     Lucas, unser Administrator, möchte ein neues Netzwerk konfigurieren. In diesem sollen 55 Hosts eingebunden werden. **Bestimmen** Sie für die folgenden Netzbereiche die mögliche Anzahl an Adressen, die für Host vergeben werden können. **Entscheiden** Sie anschließend, ob diese für Lucas Vorhaben ausreichend sind.

|         |                  |                                 |                  |
| ------- | ---------------- | ------------------------------- | ---------------- |
| **Nr.** | **Netzbereich**  | **Mögliche Anzahl an Adressen** | **Ausreichend?** |
| 1       | 192.168.0.0 / 27 | 30                              |                  |
| 2       | 192.168.0.0 / 24 | 254                             |                  |
| 3       | 192.168.0.0 / 30 | 4                               |                  |
| 4       | 192.168.0.0 / 23 | 512                             |                  |

5.     **Beschreiben** Sie in 2 – 3 Sätzen, was wir unter dem Default Gateway verstehen und wo wir es in der Regel in einem Netzwerk konfigurieren.

Erste Adresse des Netzwerks, Verbindung zum Internet/anderes Netzwerken / Router

6.     **Beschreiben** Sie kurz, wie sich private und öffentliche IP-Adressen unterscheiden und warum diese Unterscheidung eingeführt wurde.
Private IPs/ Localips


7.     **Nennen** Sie den Command Line Befehl, um die eigene Netzwerkkonfiguration eines Hosts anzuzeigen.
ifconfig
8.     **Nennen** Sie den Command Line Befehl, mit dem wir überprüfen, ob ein anderer Host im Netzwerk erreichbar ist.
ping
9.     **Nennen** Sie den Befehl, den Sie im CLI eingeben, wenn Sie für das Netzwerk 192.168.0.0 / 24 einen Broadcast an alle Hosts in dem Netzwerk versenden wollen.
Curl / Ping