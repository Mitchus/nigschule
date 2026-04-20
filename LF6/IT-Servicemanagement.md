---
fach: LF6
thema: IT-Servicemanagement
tags: [lf6, service, itil, sla, governance]
datum: 2026-04-20
typ: notiz
---

# IT-Servicemanagement

## Was ist ein IT-Service?

Ein IT-Service ist eine Dienstleistung, die IT-Infrastruktur, Anwendungen und Support kombiniert, um einen geschäftlichen Mehrwert zu schaffen.

### Servicearten

| Art                    | Beschreibung                                |
| ---------------------- | ------------------------------------------- |
| **Infrastruktur-Service** | Netzwerk, Server, Storage bereitstellen  |
| **Anwendungs-Service** | Software betreiben und warten               |
| **Support-Service**    | Helpdesk, Störungsbeseitigung               |
| **Beratungs-Service**  | IT-Strategie, Planung                       |
| **Cloud-Service**      | IaaS, PaaS, SaaS                           |

### Service beschreiben

Ein Service wird beschrieben durch:
- **Leistungsumfang** - Was wird bereitgestellt?
- **Verfügbarkeit** - Wann ist der Service erreichbar?
- **Reaktionszeit** - Wie schnell wird auf Störungen reagiert?
- **Qualität** - Welche Kennzahlen werden gemessen?
- **Kosten** - Was kostet der Service?

---

## Service Level Agreement (SLA)

Ein SLA ist ein **Vertrag** zwischen Dienstleister und Kunde, der die Qualität der Dienstleistung definiert.

### Bestandteile eines SLA

| Element            | Beschreibung                                  |
| ------------------ | --------------------------------------------- |
| **Servicezeit**    | Mo-Fr 8-18 Uhr, 24/7                         |
| **Verfügbarkeit**  | z.B. 99,9% (max. 8,76 h Ausfall/Jahr)        |
| **Reaktionszeit**  | Zeit bis zur ersten Rückmeldung               |
| **Lösungszeit**    | Zeit bis zur Behebung der Störung             |
| **Eskalation**     | Wer wird wann informiert?                     |
| **Pönalen**        | Vertragsstrafen bei Nichteinhaltung            |

### Verfügbarkeitsklassen

| Verfügbarkeit | Ausfallzeit/Jahr | Bezeichnung            |
| ------------- | ---------------- | ---------------------- |
| 99%           | 3,65 Tage        | Standard               |
| 99,9%         | 8,76 Stunden     | Hoch                   |
| 99,99%        | 52,6 Minuten     | Sehr hoch              |
| 99,999%       | 5,26 Minuten     | Höchstverfügbar        |

> [!success] Lösung – Muster-SLA: E-Mail-Service für KMU
>
> **Service Level Agreement – E-Mail-Dienst**
> *Zwischen: IT-Solutions GmbH (Dienstleister) und Musterfirma GmbH (Kunde)*
>
> | SLA-Element           | Vereinbarung                                                                 |
> | --------------------- | ---------------------------------------------------------------------------- |
> | **Servicebezeichnung** | Betrieb des unternehmensweiten E-Mail-Dienstes (Microsoft 365 Exchange)     |
> | **Servicezeit**        | Mo–Fr 07:00–19:00 Uhr (außer gesetzliche Feiertage NRW)                    |
> | **Verfügbarkeit**      | 99,5 % pro Monat (max. ca. 3,6 h Ausfall/Monat)                            |
> | **Reaktionszeit**      | Kritisch (kein E-Mail-Empfang): 30 Minuten / Sonstige Störung: 4 Stunden   |
> | **Lösungszeit**        | Kritisch: 4 Stunden / Sonstige: nächster Werktag                            |
>
> **Eskalationsstufen:**
>
> | Stufe   | Auslöser                          | Ansprechpartner                      |
> | ------- | --------------------------------- | ------------------------------------ |
> | Stufe 1 | Störung gemeldet                  | 1st-Level-Support (Helpdesk)         |
> | Stufe 2 | Reaktionszeit überschritten       | 2nd-Level-Support (Systemadmin)      |
> | Stufe 3 | Lösungszeit überschritten         | Projektleiter + Geschäftsführung     |
>
> **Pönalen (Vertragsstrafen bei Nichteinhaltung):**
> - Unterschreitung der Verfügbarkeit: Gutschrift von 5 % der monatlichen Servicegebühr je angefangene Stunde Ausfall über dem Limit
> - Max. Gutschrift: 30 % der monatlichen Gebühr
>
> **Ausschlüsse:** Geplante Wartungsfenster (Sa 02:00–05:00 Uhr, mind. 48 h Vorankündigung), Störungen durch den Kunden oder höhere Gewalt

---

## Managementarten

| Art                      | Fokus                                    |
| ------------------------ | ---------------------------------------- |
| **Incident Management**  | Störungen schnell beheben                |
| **Problem Management**   | Ursachen dauerhaft beseitigen            |
| **Change Management**    | Änderungen kontrolliert durchführen      |
| **Configuration Mgmt.**  | IT-Komponenten dokumentieren (CMDB)     |
| **Capacity Management**  | Ausreichende Ressourcen sicherstellen    |
| **Availability Mgmt.**   | Verfügbarkeit planen und überwachen     |

---

## Frameworks und Standards

### ITIL (IT Infrastructure Library)

Best-Practice-Framework für IT-Servicemanagement.

**ITIL 4 - Wertschöpfungskette:**
```
Engage → Plan → Design & Transition → Obtain/Build → Deliver & Support → Improve
```

**Kernprinzipien:**
- Wertorientierung
- Dort anfangen, wo man steht
- Iteratives Vorgehen mit Feedback
- Zusammenarbeiten und Transparenz fördern
- Ganzheitlich denken und arbeiten
- Einfach und praktisch halten
- Optimieren und automatisieren

### Weitere Standards

| Standard       | Fokus                                       |
| -------------- | ------------------------------------------- |
| **ISO 20000**  | Zertifizierung für IT-Servicemanagement     |
| **ISO 27001**  | Informationssicherheit (ISMS)               |
| **COBIT**      | IT-Governance Framework                     |

---

## Governance und Compliance

### IT-Governance

Sicherstellt, dass IT-Investitionen Geschäftsziele unterstützen.

**Aufgaben:**
- IT-Strategie an Unternehmensstrategie ausrichten
- Risikomanagement
- Ressourcenmanagement
- Leistungsmessung

### Compliance

Einhaltung von Gesetzen, Vorschriften und internen Richtlinien:

- **DSGVO** - Datenschutz-Grundverordnung
- **IT-Sicherheitsgesetz** - Schutz kritischer Infrastrukturen
- **Urheberrecht** - Softwarelizenzen einhalten
- **Aufbewahrungspflichten** - Geschäftsdaten archivieren

### Urheberrecht, Markenrecht und Lizenzen

**Urheberrecht (UrhG):**
Schützt die Rechte geistiger Schöpfer an ihren Werken (Texte, Bilder, Musik, Software). Entsteht automatisch bei Schaffung. Der Urheber hat Persönlichkeitsrechte sowie Nutzungs- und Verwertungsrechte. Verletzungen werden strafrechtlich verfolgt.

**Markenrecht (MarkenG):**
Schützt Marken, geschäftliche Bezeichnungen und geografische Herkunftsangaben. Marken können Wörter, Bilder, Klänge, Zahlen oder 3D-Gestaltungen sein. Marken dürfen nur mit Einwilligung des Inhabers verwendet werden.

**Creative-Commons-Vereinbarungen (CC):**
Erlauben es Urhebern, ihre Werke unter bestimmten Bedingungen zur freien Nutzung freizugeben:

| Kürzel    | Bedeutung                                       |
| --------- | ----------------------------------------------- |
| **CC BY** | Vervielfältigen, Verbreiten, Verändern erlaubt (Namensnennung) |
| **CC BY-SA** | Wie BY, Weitergabe unter gleicher Lizenz     |
| **CC BY-NC** | Wie BY, aber keine kommerzielle Nutzung      |
| **CC BY-ND** | Namensnennung, keine Bearbeitung erlaubt     |
| **CC0**   | Gemeinfrei, keine Einschränkungen               |

---

### Lizenzvereinbarungen

| Lizenztyp       | Beschreibung                                                   |
| --------------- | -------------------------------------------------------------- |
| **EULA**        | End User License Agreement - regelt Nutzung proprietärer Software, wird bei Installation angezeigt |
| **GNU GPL**     | Freie Software: nutzen, studieren, kopieren, verändern erlaubt; Copyleft: Ableitungen müssen ebenfalls GPL sein |
| **LGPL**        | Weniger strenge GPL: darf in proprietäre Software integriert werden |
| **BSD / MIT**   | Permissive Open-Source-Lizenzen, kein Copyleft-Zwang           |
| **Freeware**    | Kostenlos nutzbar, Quellcode geschlossen                       |
| **Shareware**   | Testversion kostenlos, Vollversion kostenpflichtig              |
| **OEM**         | Vorinstallierte Lizenz, an Hardware gebunden                   |

### Fachbegriffe aus dem Lizenzrecht

| Begriff              | Beschreibung                                                      |
| -------------------- | ----------------------------------------------------------------- |
| **User-Lizenz**      | Je Benutzer lizenziert                                            |
| **CAL**              | Client Access License - Zugriffslizenzen für Client/Server-Umgebungen |
| **NUL**              | Named User Licence - auf einen benannten Benutzer beschränkt      |
| **Concurrent Access** | Maximale gleichzeitige Zugriffe lizenziert (Floating/Netzwerklizenz) |
| **KMS**              | Key Management Service - Volumenlizenzen im eigenen Netzwerk aktivieren |
| **CPU-Klausel**      | Lizenzierung nach Prozessorkernen (Oracle, VMware)                |
| **Maintenance**      | Wartungs- und Supportvertrag des Herstellers                      |
| **SPLA**             | Service Provider License Agreement - Lizenzen über Cloud-Provider |
| **Zweitkopierecht**  | Lizenz auf Desktop + Notebook erlaubt                             |

---

## Aufgaben: Copyright & Lizenzen (Fallstudie Turtle WoW)

> [!example] Aufgabe 1 - Klage Blizzard vs. Turtle WoW
> Fassen Sie zusammen, worum es in der Klage konkret geht.

> [!success] Lösung
> Blizzard Entertainment hat Klage gegen die Betreiber des inoffiziellen WoW-Privatservers **Turtle WoW** eingereicht. Die Vorwürfe:
> - **Urheberrechtsverletzung:** Turtle WoW nutzt Blizzards geschützten Quellcode und Game-Assets (Grafiken, Icons, Spielwelt) ohne Genehmigung
> - **Markenrechtsverletzung:** Der Name "World of Warcraft" und zugehörige Marken werden ohne Erlaubnis verwendet
> - **Kommerzieller Profit:** Die Betreiber verdienen durch Spieler-Spenden möglicherweise Millionen Dollar an fremdem geistigem Eigentum
> - **Vertragsbruch:** Hunderttausende Nutzer wurden dazu gebracht, gegen Blizzards Nutzungsbedingungen (EULA/ToS) zu verstoßen
> - **Geplante Eskalation:** Turtle WoW plante ein "2.0"-Remake in Unreal Engine 5 und betrieb aktives Marketing über Social Media und Influencer
>
> **Blizzard fordert:** Vollständige Abschaltung, Herausgabe aller Daten und Einnahmen, Übertragung der Domain an Blizzard, Schadensersatz.
>
> **Aktueller Stand (2026):** Ein US-Bundesrichter (Judge Stephen V. Wilson) hat Blizzard in **allen sieben Klagepunkten** Recht gegeben - darunter Urheberrechtsverletzung, Markenrechtsverletzung, Umgehung von Kopierschutz und sogar RICO-Vorwürfe (organisierte Kriminalität). Die Betreiber (Josiah Zimmer / AFKCraft Ltd.) haben einer vertraulichen Einigung zugestimmt. Das Urteil verbietet das "Entwickeln, Programmieren, Betreiben, Aktualisieren und Warten" des Servers vollständig. Der Fall wird voraussichtlich bis Juni 2026 endgültig eingestellt.
>
> Quellen: [Icy Veins - Blizzard Wins Legal Battle](https://www.icy-veins.com/wow/news/turtle-wow-is-over-blizzard-wins-major-legal-battle/) | [Massively OP - Lawsuit Breakdown](https://massivelyop.com/2025/09/10/lawful-neutral-breaking-down-the-blizzard-v-turtle-wow-lawsuit/) | [CourtListener - Case Docket](https://www.courtlistener.com/docket/71235075/blizzard-entertainment-inc-v-turtle-wow/)

> [!example] Aufgabe 2 - Warum Copyrights? Warum problematisch?
> Erläutern Sie, warum es Regelungen zu Copyrights gibt, aber auch warum diese problematisch für den Alltag sein können.

> [!success] Lösung
> **Warum Copyrights notwendig sind:**
> - Schutz der kreativen und finanziellen Investition von Urhebern (Entwickler, Künstler, Autoren)
> - Anreiz für Innovation - ohne Schutz lohnt sich die Entwicklung neuer Werke wirtschaftlich nicht
> - Rechtssicherheit für Lizenzgeber und Lizenznehmer
> - Verhinderung von Trittbrettfahrern, die ohne eigenen Aufwand profitieren
>
> **Warum sie im Alltag problematisch sein können:**
> - **Komplexität:** Unterschiedliche Lizenzmodelle (GPL, MIT, CC, EULA) sind schwer zu überblicken
> - **Grauzone Privatkopie:** Was darf man privat kopieren? Wo endet Fair Use?
> - **Markenrecht im Internet:** Verwendung von Markennamen in Google Ads oder Social Media kann Abmahnungen auslösen
> - **Memes/Screenshots:** Alltägliche Internetkultur nutzt urheberrechtlich geschütztes Material
> - **Open-Source-Fallstricke:** GPL-Code in proprietärer Software kann das gesamte Projekt "infizieren" (Copyleft)
> - **Kosten:** Lizenzen für professionelle Software sind für kleine Unternehmen/Privatpersonen oft teuer

> [!example] Aufgabe 3 - Vergleichstabelle vervollständigen
> Vervollständigen Sie die Tabelle zu Urheberrecht, Markenrecht, CC-Lizenzen, EULA, GNU GPL.

> [!success] Lösung
>
> | Aspekt | Urheberrecht | Markenrecht | CC-Lizenzen | EULA | GNU GPL |
> | --- | --- | --- | --- | --- | --- |
> | **Schutzgegenstand** | Werke (Texte, Bilder, Musik, Software) | Marken, Logos, Geschäftsbezeichnungen | Werke, die der Urheber freigeben möchte | Proprietäre Software (Binärcode) | Software (Quellcode + Binärcode) |
> | **Entstehung** | Automatisch bei Schaffung | Eintragung beim DPMA/EUIPO (oder Benutzung) | Freiwillige Kennzeichnung durch Urheber | Vertrag bei Installation/Kauf | Lizenzwahl durch Entwickler |
> | **Zweck** | Schutz geistigen Eigentums | Unterscheidung von Waren/Dienstleistungen | Kontrollierte Freigabe von Werken | Nutzungsrechte regeln, Haftung ausschließen | Freiheit der Software sichern |
> | **Grundprinzip** | "Alle Rechte vorbehalten" | Exklusives Nutzungsrecht des Inhabers | "Manche Rechte vorbehalten" | "Nutzung nur wie erlaubt" | "Alle Freiheiten, solange Copyleft erhalten" |
> | **Nutzung durch andere** | Nur mit Erlaubnis | Nur mit Lizenz des Inhabers | Ja, unter CC-Bedingungen | Nur im Rahmen der EULA | Ja, frei für jeden Zweck |
> | **Veränderung erlaubt** | Nur mit Erlaubnis | Nein (Marke muss unverändert bleiben) | Abhängig von Lizenz (ND = nein) | Nein (Reverse Engineering meist verboten) | Ja, aber Änderungen müssen unter GPL stehen |
> | **Weitergabe erlaubt** | Nur mit Erlaubnis | Nein (ohne Lizenz) | Ja, unter gleichen Bedingungen | Nein (meist an Gerät/Nutzer gebunden) | Ja, inkl. Quellcode (Copyleft) |
> | **Typische Bedingungen** | Lizenzvertrag nötig | Markenanmeldung, Nutzungsvereinbarung | Namensnennung, ggf. nicht-kommerziell | Akzeptieren bei Installation | Quellcode mitliefern, GPL beibehalten |
> | **Beispiel** | Buch, Film, Musik | Apple-Logo, "iPhone", Coca-Cola | Wikipedia (CC BY-SA), Flickr-Fotos | Microsoft Office, Adobe Photoshop | Linux, LibreOffice, VLC |

> [!example] Aufgabe 4 - Rechtliche Vorgabe mit aktuellem Beispiel
> Suchen Sie sich eine rechtliche Vorgabe aus und erläutern deren Funktion mit einem aktuellen Beispiel.

> [!success] Lösung
> **GNU GPL am Beispiel Linux und Red Hat (2023/2024):**
>
> Die GNU GPL garantiert vier Freiheiten: Software nutzen, studieren, kopieren und verändern. Jede Weiterverbreitung muss ebenfalls unter GPL mit Quellcode erfolgen (Copyleft).
>
> **Aktuelles Beispiel:** Red Hat (IBM) schränkte 2023 den öffentlichen Zugang zum RHEL-Quellcode ein und stellte ihn nur noch zahlenden Kunden bereit. Die Community kritisierte dies als Verstoß gegen den Geist der GPL. Daraufhin entstanden Forks wie **AlmaLinux** und **Rocky Linux**, die den Quellcode über alternative Wege beziehen. Red Hat argumentiert, dass die GPL nur verlangt, den Quellcode an Empfänger der Binärdateien zu liefern - nicht an die Öffentlichkeit. Dieser Fall zeigt, wie die GPL-Lizenz zwar rechtlich eingehalten, aber durch geschäftliche Maßnahmen faktisch umgangen werden kann.

---

## Aufgaben: Arbeitsauftrag Präsentationen übernehmen

> [!example] Aufgabe 5 - Rechtliche Verstöße bei Übernahme von Präsentationen
> Sie möchten Präsentationen von einem TaskCards-Board ohne Prüfung übernehmen. Welche rechtlichen Verstöße sind möglich?

> [!success] Lösung
> - **Urheberrechtsverletzung:** Texte, Bilder und Grafiken in den Präsentationen können urheberrechtlich geschützt sein - Übernahme ohne Genehmigung des Urhebers ist illegal
> - **Bilderrechte:** Stockfotos oder Abbildungen aus dem Internet unterliegen oft einer kostenpflichtigen Lizenz
> - **Zitatrecht überschritten:** Zitate ohne Quellenangabe oder über den zulässigen Umfang hinaus
> - **Markenrechtsverletzung:** Logos oder Markennamen in den Präsentationen dürfen nicht ohne Genehmigung weiterverwendet werden
> - **Plagiat:** Übernahme fremder Texte als eigene Arbeit - auch ohne strafrechtliche Folgen ein Verstoß gegen akademische/berufliche Ehrlichkeit
> - **Datenschutz (DSGVO):** Präsentationen könnten personenbezogene Daten (Namen, Fotos von Personen) enthalten

> [!example] Aufgabe 6 - Probleme im Arbeitsalltag umgehen
> Wie kann man diese Probleme umgehen?

> [!success] Lösung
> - **Quellen prüfen:** Lizenz jeder Präsentation und jedes eingebetteten Bildes vor Übernahme prüfen
> - **Creative-Commons-Inhalte nutzen:** CC-lizenzierte Materialien verwenden und Bedingungen einhalten (Namensnennung, nicht-kommerziell etc.)
> - **Eigene Inhalte erstellen:** Texte selbst formulieren, lizenzfreie Bilder verwenden (z.B. Unsplash, Pixabay mit CC0)
> - **Quellenangaben:** Immer Urheber, Quelle und Lizenz angeben
> - **Genehmigung einholen:** Bei unklarer Lizenz den Ersteller direkt um Erlaubnis bitten
> - **Unternehmensrichtlinie:** Interne Vorgaben zum Umgang mit fremden Materialien beachten
> - **Stockfoto-Abonnements:** Für den professionellen Einsatz lizenzierte Bilddatenbanken nutzen

> [!example] Aufgabe 7 - Vertiefung: Star-Wars-Bild für Werbeflyer
> Sie möchten ein Bild von pxhere.com mit dem Slogan "Möge die Macht mit dir sein." für einen Werbeflyer verwenden. Ist dies ohne Weiteres möglich?

> [!success] Lösung
> **Nein**, das ist **nicht** ohne Weiteres möglich. Es gibt zwei getrennte Probleme:
>
> **1. Das Bild (pxhere.com):**
> Bilder auf pxhere.com stehen oft unter CC0 (Public Domain). Das Bild selbst dürfte daher frei verwendbar sein - **aber:** Wenn darauf Star-Wars-Figuren oder -Szenen abgebildet sind, greift das **Urheberrecht von Lucasfilm/Disney** an den abgebildeten Charakteren, Kostümen und Designs. Die CC0-Lizenz des Fotografen befreit nicht vom Urheberrecht des dargestellten Inhalts.
>
> **2. Der Slogan "Möge die Macht mit dir sein":**
> Der Satz "May the Force be with you" bzw. die deutsche Übersetzung ist ein ikonisches Zitat aus Star Wars und als **Marke von Lucasfilm/Disney** geschützt. Die Verwendung in einem **kommerziellen Werbeflyer** wäre eine **Markenrechtsverletzung** und könnte eine Abmahnung nach sich ziehen.
>
> **Fazit:** Beide Elemente zusammen in einem kommerziellen Kontext zu verwenden ist rechtlich unzulässig ohne Genehmigung von Disney/Lucasfilm.

---

## Materialien

- ![[files/01- AB.pdf]]
- ![[files/02- AB Services beschreiben.pdf]]
- ![[files/02-Servicemanagement.pdf]]
- ![[files/03- AB Managmentarten.pdf]]
- ![[files/03-Frameworks.pdf]]
- ![[files/03-Standards und Frameworks.pdf]]
- ![[files/04-Governance and Compliance.pdf]]
- ![[files/05-Copyrights.pdf]]
- ![[files/SB5.pdf]]
