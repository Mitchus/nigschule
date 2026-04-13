### Einteilung des OSI-Schichtenmodells

- Das OSI-Schichtenmodell besteht aus 7 Schichten.
- Jeder Schicht ist eine bestimmte Aufgabe zugeordnet.
- Einzelne Schichten können angepasst, zusammengefasst oder ausgetauscht werden.
- Die Schichten 1..4 sind transportorientierte Schichten.
- Die Schichten 5..7 sind anwendungsorientierte Schichten.
- Das Übertragungsmedium ist nicht festgelegt.

### Schicht 1: Bitübertragungsschicht / Physical Layer

##### Maßnahmen und Verfahren zur Übertragung von Bitfolgen

Die Bitübertragungsschicht definiert die elektrische, mechanische und funktionale Schnittstelle zum Übertragungsmedium. Die Protokolle dieser Schicht unterscheiden sich nur nach dem eingesetzten Übertragungsmedium und -verfahren. Das Übertragungsmedium ist jedoch kein Bestandteil der Schicht 1.

### Schicht 2: Sicherungsschicht / Data Link Layer

Logische Verbindungen mit Datenpaketen und elementare Fehlererkennungsmechanismen

Die Sicherungsschicht sorgt für eine zuverlässige und funktionierende Verbindung zwischen Endgerät und Übertragungsmedium. Zur Vermeidung von Übertragungsfehlern und Datenverlust enthält diese Schicht Funktionen zur Fehlererkennung, Fehlerbehebung und Datenflusskontrolle.  
Auf dieser Schicht findet auch die physikalische Adressierung von Datenpaketen statt.

### Schicht 3: Vermittlungsschicht / Network Layer

##### Routing und Datenflusskontrolle

Die Vermittlungsschicht steuert die zeitliche und logische getrennte Kommunikation zwischen den Endgeräten, unabhängig vom Übertragungsmedium und der Topologie. Auf dieser Schicht erfolgt erstmals die logische Adressierung der Endgeräte. Die Adressierung ist eng mit dem Routing (Wegfindung vom Sender zum Empfänger) verbunden.

### Schicht 4: Transportschicht / Transport Layer

##### Logische Ende-zu-Ende-Verbindungen

Die Transportschicht ist das Bindeglied zwischen den transportorientierten und anwendungsorientierten Schichten. Hier werden die Datenpakete einer Anwendung zugeordnet.

### Schicht 5: Kommunikationsschicht / Session Layer

##### Prozess-zu-Prozess-Verbindungen

Die Kommunikationsschicht organisiert die Verbindungen zwischen den Endsystemen. Dazu sind Steuerungs- und Kontrollmechanismen für die Verbindung und dem Datenaustausch implementiert.

### Schicht 6: Darstellungsschicht / Presentation Layer

##### Ausgabe von Daten in Standardformate

Die Darstellungsschicht wandelt die Daten in verschiedene Codecs und Formate. Hier werden die Daten zu oder von der Anwendungsschicht in ein geeignetes Format umgewandelt.

### Schicht 7: Anwendungsschicht / Application Layer

##### Dienste, Anwendungen und Netzmanagement

Die Anwendungsschicht stellt Funktionen für die Anwendungen zur Verfügung. Diese Schicht stellt die Verbindung zu den unteren Schichten her. Auf dieser Ebene findet auch die Dateneingabe und -ausgabe statt.

### Kurzbeschreibung des OSI-Schichtenmodells

1. Schicht / **Anwendung**: Funktionen für Anwendungen, sowie die Dateneingabe und -ausgabe.  
2. Schicht / **Darstellung**: Umwandlung der systemabhängigen Daten in ein unabhängiges Format.  
3. Schicht / **Kommunikation**: Steuerung der Verbindungen und des Datenaustauschs.  
4. Schicht / **Transport**: Zuordnung der Datenpakete zu einer Anwendung.  
5. Schicht / **Vermittlung**: Routing der Datenpakete zum nächsten Knoten.  
6. Schicht / **Sicherung**: Segmentierung der Pakete in Frames und Hinzufügen von Prüfsummen.  
7. Schicht / **Bitübertragung**: Umwandlung der Bits in ein zum Medium passendes Signal und physikalische Übertragung.

|   |   |   |
|---|---|---|
|Schicht 7|Anwendung|Telnet, FTP, HTTP, SMTP, NNTP|
|Schicht 6|Darstellung|Telnet, FTP, HTTP, SMTP, NNTP, NetBIOS|
|Schicht 5|Kommunikation|Telnet, FTP, HTTP, SMTP, NNTP, NetBIOS, TFTP|
|Schicht 4|Transport|TCP, UDP, SPX, NetBEUI|
|Schicht 3|Vermittlung|IP, IPX, ICMP, T.70, T.90, X.25, NetBEUI|
|Schicht 2|Sicherung|LLC/MAC, X.75, V.120, ARP, HDLC, PPP|
|Schicht 1|Übertragung|Ethernet, Token Ring, FDDI, V.110, X.25, Frame Relay, V.90, V.34, V.24|
TCP/IP-Model vs. OSI-Model

Das TCP/IP-Modell ist älter als das OSI-Modell. Die folgende Abbildung zeigt die Beziehungen ihrer entsprechenden Layer.

![](https://resource.fs.com/mall/generalImg/CK3cbEF8NoIhpYxzsNccvtt3nrg.jpeg)
![[Pasted image 20250409144713.png]]
Abbildung 4: OSI-Modell vs. TCP/IP-Modell und TCP/IP-Protokollsuite

Vergleicht man die Schichten des TCP/IP-Modells und des OSI-Modells, so ähnelt die Anwendungsschicht (Application Layer) des TCP/IP-Modells den kombinierten OSI-Schichten 5, 6, 7, aber das TCP/IP-Modell hat keine separate Präsentations- oder Sitzungsschicht (Presentation layer or Session layer). Die Transportschicht (Transport Layer) von TCP/IP umfasst die Verantwortlichkeiten der OSI-Transportschicht und einige der Verantwortlichkeiten der OSI-Sitzungsschicht (Session Layer). Die Netzwerkzugriffsschicht (Network Access Layer) des TCP/IP-Modells umfasst die Datenverbindung und die physikalischen Schichten des OSI-Modells. Beachten Sie, dass die Internetschicht (Internet Layer) von TCP/IP die Vorteile von Sequenzierungs- und Bestätigungsdiensten, die in der Sicherungsschicht (Data Link Layer) des OSI-Modells vorhanden sein könnten, nicht nutzt. Im TCP/IP-Modell liegt die Verantwortung bei der Transportschicht.

Betrachtet man die Bedeutung der beiden Referenzmodelle, so ist das OSI-Modell nur ein konzeptionelles Modell. Es wird hauptsächlich zur Beschreibung, Diskussion und zum Verständnis einzelner Netzwerkfunktionen verwendet. TCP/IP ist jedoch vor allem dazu gedacht, eine bestimmte Reihe von Problemen zu lösen, anstatt als Generierungsbeschreibung für die gesamte Netzwerkkommunikation als OSI-Modell zu fungieren. Das OSI-Modell ist generisch, protokollunabhängig, aber die meisten Protokolle und Systeme halten sich daran, während das TCP/IP-Modell auf Standardprotokollen basiert, die das Internet entwickelt hat. Eine weitere Besonderheit im OSI-Modell ist, dass nicht alle Schichten in einfacheren Anwendungen verwendet werden. Während die Schichten 1, 2, 3 für jede Datenkommunikation obligatorisch sind, kann die Anwendung anstelle der üblichen oberen Schichten im Modell auch eine bestimmte Schnittstellenschicht für die Anwendung verwenden.

Zusammenfassung

Das TCP/IP-Modell und das OSI-Modell sind beide konzeptionelle Modelle zur Beschreibung der gesamten Netzwerkkommunikation, während TCP/IP selbst aber auch ein wichtiges Protokoll für alle Internetoperationen darstellt. Im Allgemeinen sprechen wir, wenn wir über Schicht 2, Schicht 3 oder Schicht 7 sprechen, in der ein Netzwerkgerät arbeitet, vom OSI-Modell. Das TCP/IP-Modell wird sowohl für die Modellierung der aktuellen Internetarchitektur als auch für die Bereitstellung eines Regelwerks verwendet, dem alle Formen der Übertragung über das Netzwerk folgen.


Die Netzwerkadresse bezeichnet ein Netz, welches in der Regel mehrere Hosts beherbergen kann. Vergleich im analogen Leben: Die Straße in der Postadresse.

Die Hostadresse bezeichnet einen konkreten Rechner. Vergleich im analogen Leben: Das Haus (die Hausnummer) in der Straße. Die Hausnummer allein nützt Dir nichts, Du benötigst auch den Straßennamen.

Mit der Broadcastadresse sprichst Du alle Rechner in einem Netz an.

Technisch: Bei einer Netzadresse sind alle Bits, die den Host bezeichnen, auf Null gesetzt. Bei der Broadcastadresse sind alle Bits, die den Host bezeichnene, auf Eins gesetzt.

Beispiel:

192.168.1.0 mit der Subnetzmaske 255.255.255.0 bedeutet, dass 192.168.1 der Straßenname ist. Das letzte Byte bezeichnet also den Host. Hier ist das Byte auf Null gesetzt, deshalb ist das die Netzadresse, also der Straßenname.

192.168.1.15 - das ist ein Adresse, die einen Host im obigen Netz bezeichnet.

192.168.1.255 ist die Broadcastadresse. Alle Bits im letzten Byte, also alle Bits, die die Hosts bezeichnen, sind auf 1 gesetzt.

## Der Aufbau einer URL

Eine URL besteht in der einfachsten Beschreibung aus drei Teilen: Protokoll (https://, ftp://), Domain- oder Server-Name (www.domain.de) und Dateipfad (/verzeichnis/datei.html). Der Dateipfad kann aus mehreren Verzeichnisebenen bestehen.

Anstelle des Server-Namens könnte auch eine IP-Adresse stehen.

Wird eine Datei nicht über einen Browser oder anderen Client im Web abgerufen, sondern von einem anderen Server, kann eine URL auch so aussehen:

https://peter:beispiel@www.beispiel.de:8080/index.html

In diesem Fall besteht die URL neben dem Protokoll/Schema noch aus dem User-Namen mit Kennwort, dem Host der Datei (www.beispiel.de) sowie dem Port (8080), über welchen die Daten abgerufen werden können.


0.016 106 127 360
14Pb 14 000 000 000 MB
4 398 046 511 104 Bytes


7 x 13 
294 840 000 Bits pro bild
**Lösung:**

1. Umrechnung in Inch:
    - Breite: 33,02 cm ÷ 2,54 = 13 Inch
    - Höhe: 17,78 cm ÷ 2,54 = 7 Inch
2. Pixel berechnen:
    - Breite: 13 × 300 = 3.900 Pixel
    - Höhe: 7 × 300 = 2.100 Pixel
    - Gesamt: 3.900 × 2.100 = 8.190.000 Pixel
3. Speicherbedarf pro Bild:
    - Pro Pixel: 3 Kanäle × 12 Bit = 36 Bit = 4,5 Byte
    - Pro Bild: 8.190.000 × 4,5 = 36.855.000 Byte
4. Für 1000 Bilder:
    - 36.855.000 × 1.000 = 36.855.000.000 Byte
    - **= 36,855 GB = 34,33 GiB = 0,03369 TiB**


786 432 Pixel x 12Bit/Pixel
9 437 184 Bits pro Bild
31 850 496 000 Bytes pro Video uncompressed
318 504 960 compressed 
1 592 524 800 000 Bytes 5k Vids
1,448 392 868 TiB



BC lwl können einfACH BRECHEN MAX BIEGE RADIUS

![[Pasted image 20251118085106.png]]
Wir unterscheiden grundsätzlich in zwei Arten von LWL, je nachdem wieviele Moden “gleichzeitig” übertragen werden; Eine Mode (Single- bzw. Monomode) oder mehrere Moden (Multimode) [2].

Multimode-Faser mit Stufenindexprofil
![[Pasted image 20251118085450.png]]

Gesamtdurchmesser von 200 bis 500 µm
mehrere Lichtwellen gleichzeitig geschickt
Signal hart reflektiert
Ausgangssignal wird dadurch schlechter

Multimode-Faser mit Gradientenindexprofil
![[Pasted image 20251118085510.png]]
Gesamtdurchmesser von 125 µm
mehrere Lichtwellen gleichzeitig
Signal weich reflektiert (Gradient)
Ausgangssignal ist noch sehr gut

Monomode-Faser / Singlemode-Faser
![[Pasted image 20251118085529.png]]
Gesamtdurchmesser von 125 µm
weite Strecken
nur ein Modus (Moden)
erfordern den Einsatz sehr teurer Laser
für Stadt- und Zugangsnetze optimiert


Störungfreies Übertragungsmittel 
Schelligkeit
Distanz
