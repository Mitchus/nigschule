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

### Urheberrecht bei Software

| Lizenztyp        | Nutzungsrecht                              |
| ---------------- | ------------------------------------------ |
| Einzellizenz     | Ein Arbeitsplatz                           |
| Volumenlizenz    | Mehrere Arbeitsplätze, günstiger           |
| Subscription     | Zeitbasiert (monatlich/jährlich)            |
| Open Source      | Frei nutzbar (Lizenz beachten: GPL, MIT)   |

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
